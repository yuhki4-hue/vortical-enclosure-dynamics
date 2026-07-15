"""growth_v24_3_rules.py -- §12-3: 2x2 rule decomposition
(pre-registered §2.2.1, locked 2026-07-12).

Fork of `growth v24 betti.py`. ONLY the distribution rule (dst) and the
instrumentation differ; firing, floor, conversion, decay, and death are
unchanged. Four cells, distribution rules fixed by formula:

  directed  (one-sided, self-feed banned) : dst = outgoing(j, exclude=i)
                                            reflection [(j,i)] if empty
  cellA     (one-sided, self-feed ALLOWED): dst = outgoing(j, exclude=i)
                                                  + [(i,j), (j,i)]
  cellB     (two-sided, self-feed banned) : dst = (outgoing(i)+outgoing(j))
                                                  \\ {(i,j), (j,i)}
                                            reflection [(j,i)] if empty
  symmetric (two-sided, self-feed allowed): dst = outgoing(i)+outgoing(j)

"Self-feed allowed" = firing edge AND its reverse are both included
(both-bundled definition, §2.2). Headroom settings mandatory: run with
NMAX large enough that no cell saturates; saturated cells are excluded
from claims and re-run with larger NMAX.

Primary dependent variable for the interaction criterion: MEDIAN EDGE
LIFETIME. Interaction is declared iff
  effect(one-sided)  = median(A) - median(directed)
  effect(two-sided)  = median(symmetric) - median(B)
have opposite signs, or one exceeds 3x the other in absolute value.
(Fixed before the run. beta1(H) is a size proxy and is recorded as
reference only; adjudication uses edge lifetimes and robust BSW
occupancy min-npts>=5.)

Recorded per event: n_dst, realized share stats (C-weighted), and the
share received by the firing edge / reverse edge when included.
Recorded per run: edge lifetime distribution (support birth/death at
H>1e-12, undirected pair level), per-snapshot V/E/b1H/b1S/label TSV
(classifier-compatible), and one-value-per-line -log(S) edge weights for
robust BSW snapshots (METR with npts>=5).

USAGE:
  python growth_v24_3_rules.py <g> <epochs> <seeds,csv> <NMAX> <cell>
  cell in {directed, cellA, cellB, symmetric}
  e.g. python growth_v24_3_rules.py 0.075 900 3,5,7,10,12,15 1200 cellA
"""
import sys

import numpy as np
from scipy.sparse.csgraph import shortest_path, connected_components
from collections import Counter

NMAX = 1200
TRULE = 'T1'
LINK_EPS = 1e-6
S_SUPPORT = 1e-6     # closure-support threshold for b1(S)
H_SUPPORT = 1e-12    # ledger-support threshold for b1(H)


def betti1(A_bool, alive):
    idx = np.where(alive)[0]
    V = int(idx.size)
    if V == 0:
        return 0, 0, 0, 0
    A = A_bool[np.ix_(idx, idx)]
    A = A | A.T
    np.fill_diagonal(A, False)
    E = int(A.sum() // 2)
    ncomp, _ = connected_components(A, directed=False)
    return V, E, int(ncomp), E - V + int(ncomp)


def panel(S, ngrown):
    Sc = np.clip(S, 1e-12, 1 - 1e-12)
    W = -np.log(Sc); np.fill_diagonal(W, 0.0)
    mask = Sc > LINK_EPS; np.fill_diagonal(mask, False)
    cl = S[mask] if mask.sum() else np.array([0.0])
    medC = float(np.median(cl))
    Wg = np.where(mask, W, 0.0)
    nc, lab = connected_components((Wg > 0), directed=False)
    big = np.bincount(lab).argmax(); keep = lab == big
    gcf = keep.sum() / max(ngrown, 1)
    D = shortest_path(Wg[np.ix_(keep, keep)], method='D', directed=False)
    n = D.shape[0]; fin = np.isfinite(D) & (D > 0)
    nn = []
    for i in range(n):
        v = D[i][fin[i]]
        if v.size:
            nn.append(v.min())
    d_cal = np.nan; npts = 0
    if nn:
        unit = np.median(nn); rs = unit * np.arange(1, 40)
        counts = np.array([((D <= r) & np.isfinite(D)).sum(1).mean()
                           for r in rs])
        sel = (counts > 5) & (counts < 0.5 * n)
        npts = int(sel.sum())
        if npts >= 4:
            bd = float(np.polyfit(np.log(rs[sel]), np.log(counts[sel]),
                                  1)[0])
            m = np.array([0.91, 1.70, 2.20]); t = np.array([1., 2., 3.])
            if bd > m[-1]:
                d_cal = t[-1] + (bd - m[-1]) * (t[-1] - t[-2]) / (m[-1] - m[-2])
            elif bd < m[0]:
                d_cal = t[0] + (bd - m[0]) * (t[1] - t[0]) / (m[1] - m[0])
            else:
                d_cal = float(np.interp(bd, m, t))
    if gcf < 0.6:
        ph = "FRAG"
    elif medC > 0.9:
        ph = "SAT"
    elif not np.isfinite(d_cal):
        ph = "SW"
    else:
        ph = "METR"
    return ph, medC, d_cal, npts


def support_weights(S):
    """Return -log(S) weights on the same support graph used by panel()."""
    Sc = np.clip(S, 1e-12, 1 - 1e-12)
    mask = Sc > LINK_EPS
    np.fill_diagonal(mask, False)
    if not mask.any():
        return np.array([])
    return -np.log(Sc[mask])


def run(seed, lam, gamma, cell, epochs):
    rng = np.random.default_rng(seed)
    H = np.zeros((NMAX, NMAX)); C = np.zeros((NMAX, NMAX))
    Wl = {}
    alive = np.zeros(NMAX, dtype=bool)
    free = list(range(NMAX - 1, -1, -1))
    kappa = gamma
    nsub = ndead = n_reflect = 0
    saturated = False
    snaps = []
    bsw_weights = []
    # --- edge lifetime tracking (undirected pair level) -----------------
    edge_birth = {}          # frozenset({i,j}) -> birth epoch
    lifetimes = []           # closed lifetimes
    # --- per-event dst instrumentation ----------------------------------
    ndst_all = []            # n_dst per event
    share_fire = []          # realized share of firing edge (i,j) when in dst
    share_rev = []           # realized share of reverse edge (j,i) when in dst

    def outgoing(j, exclude=None):
        nb = np.where(((H[j, :] > H_SUPPORT) | (H[:, j] > H_SUPPORT))
                      & alive)[0]
        return [(j, int(k)) for k in nb
                if k != j and (exclude is None or k != exclude)]

    def dst_rule(i, j):
        if cell == "directed":
            d = outgoing(j, exclude=i)
            return d if d else [(j, i)]
        if cell == "cellA":
            return outgoing(j, exclude=i) + [(i, j), (j, i)]
        if cell == "cellB":
            banned = {(i, j), (j, i)}
            d = [L for L in outgoing(i) + outgoing(j) if L not in banned]
            return d if d else [(j, i)]
        if cell == "symmetric":
            return outgoing(i) + outgoing(j)
        raise ValueError(cell)

    for ep in range(epochs):
        events = []
        for L, w in list(Wl.items()):
            i, j = L
            if not (alive[i] and alive[j]) or H[i, j] <= H_SUPPORT:
                continue
            events += [L] * int(rng.poisson(w))
        live_links = [(i, j) for (i, j) in Wl
                      if alive[i] and alive[j] and H[i, j] > H_SUPPORT]
        if not live_links:
            all_pairs = np.argwhere(np.triu(H, 1) > H_SUPPORT)
            live = [(int(a), int(b)) for a, b in all_pairs
                    if alive[a] and alive[b]]
            if live:
                a_, b_ = live[rng.integers(len(live))]
                events.append((a_, b_) if rng.random() < 0.5 else (b_, a_))
            elif len(free) >= 2:
                a = free.pop(); b = free.pop()
                alive[a] = alive[b] = True
                H[a, b] = 1.0
                events.append((a, b))
        else:
            events.append(live_links[rng.integers(len(live_links))])
        if len(events) > 100_000:
            return ("RUNAWAY", snaps, lifetimes, edge_birth, ndst_all,
                    share_fire, share_rev, n_reflect, saturated, nsub, ndead,
                    bsw_weights)
        Wnext = {}
        rng.shuffle(events)
        for (i, j) in events:
            if not (alive[i] and alive[j]):
                continue
            c = 0.5 * (C[i, j] + C[j, i])
            if rng.random() < c and free:
                # T1 irreversible triangle insertion (only rule in v24.3)
                a = free.pop(); alive[a] = True
                H[i, a] += 1.0; H[a, j] += 1.0
                nsub += 1
                dst = outgoing(a)
                if not free:
                    saturated = True
            else:
                H[i, j] += (1.0 - c)
                dst = dst_rule(i, j)
            if not dst:
                continue
            is_reflection = (len(dst) == 1 and dst[0] == (j, i)
                             and cell in ("directed", "cellB"))
            if is_reflection:
                n_reflect += 1
            cw = np.array([max(C[a_, b_], 1e-9) for (a_, b_) in dst])
            sh = cw / cw.sum()
            ndst_all.append(len(dst))
            for L, s in zip(dst, sh):
                Wnext[L] = Wnext.get(L, 0.0) + s
                if L == (i, j):
                    share_fire.append(float(s))
                elif L == (j, i) and not is_reflection:
                    share_rev.append(float(s))
        Wl = Wnext
        H *= (1.0 - gamma)
        idx = np.where(alive)[0]
        if len(idx):
            rho = np.zeros(NMAX)
            for (i, j) in events:
                rho[i] += 1; rho[j] += 1
            Ceq = np.zeros((NMAX, NMAX))
            Ceq[np.ix_(idx, idx)] = 1 - np.exp(
                -lam * rho[idx][:, None] * H[np.ix_(idx, idx)])
            C += kappa * (Ceq - C)
            C[~alive, :] = 0.0; C[:, ~alive] = 0.0
            Sfull = 0.5 * (C + C.T)
            Ssub = Sfull[np.ix_(idx, idx)]
            haslink = (Ssub > LINK_EPS).sum(1) > 0
            for dnode in idx[~haslink]:
                alive[dnode] = False
                H[dnode, :] = 0.0; H[:, dnode] = 0.0
                C[dnode, :] = 0.0; C[:, dnode] = 0.0
                free.append(int(dnode)); ndead += 1
        # --- edge lifetime bookkeeping (per epoch) -----------------------
        sup = (H > H_SUPPORT) | (H.T > H_SUPPORT)
        sup &= alive[:, None] & alive[None, :]
        iu, ju = np.where(np.triu(sup, 1))
        cur = set(map(frozenset, zip(iu.tolist(), ju.tolist())))
        for e in cur - edge_birth.keys():
            edge_birth[e] = ep
        for e in list(edge_birth.keys() - cur):
            lifetimes.append(ep - edge_birth.pop(e))
        # --- snapshot -----------------------------------------------------
        if (ep + 1) % 25 == 0:
            idx2 = np.where(alive)[0]
            if len(idx2) >= 3:
                Sm = 0.5 * (C + C.T)
                Sn = Sm[np.ix_(idx2, idx2)]
                ph, medC, d_cal, npts = panel(Sn, len(idx2))
                if ph == "METR" and npts >= 5:
                    bsw_weights.extend(support_weights(Sn).tolist())
                vH, eH, cH, b1H = betti1(H > H_SUPPORT, alive)
                _, _, _, b1S = betti1(Sm > S_SUPPORT, alive)
                snaps.append((ep + 1, vH, eH, b1H, b1S, ph, d_cal, npts))
            else:
                snaps.append((ep + 1, 0, 0, 0, 0, "DEAD", np.nan, 0))
    return ("ok", snaps, lifetimes, edge_birth, ndst_all,
            share_fire, share_rev, n_reflect, saturated, nsub, ndead,
            bsw_weights)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    lam = 0.9
    g = float(sys.argv[1])
    epochs = int(sys.argv[2])
    seeds = [int(s) for s in sys.argv[3].split(",")]
    NMAX = int(sys.argv[4])
    cell = sys.argv[5]
    assert cell in ("directed", "cellA", "cellB", "symmetric")

    all_lifetimes = []
    for seed in seeds:
        (status, snaps, lifetimes, open_edges, ndst, sf, sr, nrefl,
         saturated, nsub, ndead, bsw_weights) = run(seed, lam, g, cell, epochs)
        # right-censored open edges recorded separately (NOT pooled into
        # the closed-lifetime median)
        closed = np.array(lifetimes) if lifetimes else np.array([np.nan])
        all_lifetimes += lifetimes
        metr = sum(1 for s in snaps if s[5] == "METR")
        metr5 = sum(1 for s in snaps if s[5] == "METR" and s[7] >= 5)
        print(f"cell={cell} g={g} s={seed} [{status}] "
              f"SAT={'YES' if saturated else 'no'} snaps={len(snaps)} "
              f"occ={metr} occ(npts>=5)={metr5} "
              f"edge_life_med={np.nanmedian(closed):.0f} "
              f"censored={len(open_edges)} "
              f"n_dst_mean={np.mean(ndst):.1f} "
              f"fire_share_mean={np.mean(sf) if sf else float('nan'):.4f} "
              f"rev_share_mean={np.mean(sr) if sr else float('nan'):.4f} "
              f"reflections={nrefl} "
              f"nsub={nsub} dead={ndead}")
        out = f"v24_3_{cell}_g{g}_s{seed}.tsv"
        with open(out, "w") as fo:
            fo.write("epoch\tV\tE\tb1H\tb1S\tlabel\td_cal\tnpts\n")
            for s in snaps:
                fo.write("\t".join(str(x) for x in s) + "\n")
        print(f"    -> {out}")
        wout = f"v24_3_{cell}_g{g}_s{seed}_bsw_weights.txt"
        with open(wout, "w") as fo:
            for w in bsw_weights:
                fo.write(f"{w:.17g}\n")
        print(f"    -> {wout} (robust BSW weights n={len(bsw_weights)})")
    lt = np.array(all_lifetimes)
    if lt.size:
        print(f"\nPOOLED cell={cell}: edge lifetimes n={lt.size} "
              f"median={np.median(lt):.0f} p90={np.percentile(lt, 90):.0f}")

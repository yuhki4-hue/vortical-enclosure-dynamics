"""growth_flux_ledger.py -- edge flux / fate ledger (registered 2026-07-14).

Fork of growth_campA_cycles.py. Instruments are PURE READ: accumulators
only, no RNG calls added, no dynamics touched. Verified byte-identical to
campA on V / T1 count / cycle birth-death / phase label / BSW.

TWO DEPOSIT LAYERS ARE RECORDED SEPARATELY (adjudicated before implementation).
The feeding chain is two-stage:
    allocation (share s -> W)  ->  firing (Poisson(W))  ->  H increment
so "deposit received" is ambiguous. Both layers are kept:
  O_e       candidacy count: times e entered a dst set (allocation layer)
  F_alloc_e sum of realized shares s allocated to e   (allocation layer)
  s_bar_e   F_alloc_e / O_e, mean realized share when candidate
  F_H_e     ACTUAL H inflow to e this interval        (H layer)
              = sum of (1-c) firing increments + 1.0 per new-pole wiring
  D_e       ACTUAL decay drawn from e this interval   (H layer)
              = H_e(after increments) * gamma, summed over epochs
  M_e       log((F_H_e + eps) / (D_e + eps))          <- maintenance margin
              M_e uses the H layer ONLY: F and D must share units for the
              ratio to mean "deposit outruns decay". F_alloc is kept for
              the opportunity/share decomposition, not for M_e.
Note the layers are offset by one epoch by construction: shares allocated
at t set the firing rate at t+1, so F_H(t) is driven by F_alloc(t-1).
Lag offline as needed; nothing is pre-lagged here.

  k_e       number of ALIVE cycles sharing e (overlap load)
  H_start   H_e at interval start   (control: already-dying edges)
  S_start   S_e at interval start   (control: distance to threshold)
  age_e     interval_start - edge first-support epoch
  died      edge lost support during this interval

Edges are keyed UNDIRECTED (ekey), matching cycle membership; directed
quantities are summed over both orientations.

Cycle membership is emitted separately (*_cycedges.tsv) so M_c^(q) can be
recomputed offline at any quantile q without re-running.

W_cont (pure read, for problem B's final stage) is reconstructed here as
    W_cont = ln(r_max / r_min) over the min-npts selection window
DEFINITION FLAG: the v24.2e script was not available; if its W_cont uses a
different base or window, reconcile before cross-campaign comparison.

USAGE:
  python growth_flux_ledger.py <g> <epochs> <seeds,csv> <NMAX> TD [ckpt]
Outputs per run: *_ledger.tsv (per interval x edge), *_cycedges.tsv,
plus the campA-identical *.tsv / *_cycles.tsv / *_alive.tsv.
"""
import sys
from collections import deque

import numpy as np
from scipy.sparse.csgraph import shortest_path, connected_components

NMAX = 2000
LINK_EPS = 1e-6
S_SUPPORT = 1e-6
H_SUPPORT = 1e-12


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
    d_cal = np.nan; npts = 0; w_cont = np.nan
    if nn:
        unit = np.median(nn); rs = unit * np.arange(1, 40)
        counts = np.array([((D <= r) & np.isfinite(D)).sum(1).mean()
                           for r in rs])
        sel = (counts > 5) & (counts < 0.5 * n)
        npts = int(sel.sum())
        if npts >= 2:
            rsel = rs[sel]
            w_cont = float(np.log(rsel.max() / rsel.min()))
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
    return ph, medC, d_cal, npts, w_cont


def ekey(u, v):
    return (u, v) if u < v else (v, u)


def run(seed, lam, gamma, cell, epochs, ckpt_path=None, ckpt_every=500):
    import pickle, os
    start_ep = 0
    if ckpt_path and os.path.exists(ckpt_path):
        with open(ckpt_path, "rb") as fh:
            st = pickle.load(fh)
        (rng, H, C, Wl, alive, free, nsub, ndead, tl_fallback, saturated,
         snaps, cyc_edges, cyc_newE, cyc_birth, cyc_dead, edge2cyc,
         edge_attained, next_id, alive_log, start_ep) = st
        print(f"# resumed at ep {start_ep}", flush=True)
        return _run_body(rng, H, C, Wl, alive, free, nsub, ndead,
                         tl_fallback, saturated, snaps, cyc_edges, cyc_newE,
                         cyc_birth, cyc_dead, edge2cyc, edge_attained,
                         next_id, alive_log, start_ep, lam, gamma, cell,
                         epochs, ckpt_path, ckpt_every)
    rng = np.random.default_rng(seed)
    H = np.zeros((NMAX, NMAX)); C = np.zeros((NMAX, NMAX))
    Wl = {}
    alive = np.zeros(NMAX, dtype=bool)
    free = list(range(NMAX - 1, -1, -1))
    nsub = ndead = tl_fallback = 0
    saturated = False
    snaps = []
    # ---- cycle registry (§7.6.1) ---------------------------------------
    cyc_edges = {}       # cycle_id -> tuple of edge keys (undirected)
    cyc_newE = {}        # cycle_id -> frozenset of the two new-pole edges
    cyc_birth = {}
    cyc_dead = {}        # cycle_id -> (death_ep, died_by)
    edge2cyc = {}        # edge key -> set of alive cycle_ids
    edge_attained = set()  # edges that have attained S-support at least once
    next_id = 0
    alive_log = []       # (snap_ep, sorted alive ids)
    return _run_body(rng, H, C, Wl, alive, free, nsub, ndead, tl_fallback,
                     saturated, snaps, cyc_edges, cyc_newE, cyc_birth,
                     cyc_dead, edge2cyc, edge_attained, next_id, alive_log,
                     0, lam, gamma, cell, epochs, ckpt_path, ckpt_every)


def _run_body(rng, H, C, Wl, alive, free, nsub, ndead, tl_fallback,
              saturated, snaps, cyc_edges, cyc_newE, cyc_birth, cyc_dead,
              edge2cyc, edge_attained, next_id_v, alive_log, start_ep,
              lam, gamma, cell, epochs, ckpt_path, ckpt_every):
    kappa = gamma
    next_id = next_id_v
    # ---- flux ledger accumulators (pure read) -------------------------
    from collections import defaultdict
    acc_O = defaultdict(int); acc_Fa = defaultdict(float)
    acc_FH = defaultdict(float); acc_D = defaultdict(float)
    edge_first = {}          # ekey -> first epoch with support
    H_start = {}; S_start = {}
    ledger_rows = []

    def outgoing(j, exclude=None):
        nb = np.where(((H[j, :] > H_SUPPORT) | (H[:, j] > H_SUPPORT))
                      & alive)[0]
        return [(j, int(k)) for k in nb
                if k != j and (exclude is None or k != exclude)]

    def h_neighbors(u):
        return np.where(((H[u, :] > H_SUPPORT) | (H[:, u] > H_SUPPORT))
                        & alive)[0]

    def register_cycle(edges, new_edges, ep):
        nonlocal next_id
        cid = next_id; next_id += 1
        cyc_edges[cid] = tuple(edges)
        cyc_newE[cid] = frozenset(new_edges)
        cyc_birth[cid] = ep
        for e in edges:
            edge2cyc.setdefault(e, set()).add(cid)
        return cid

    def insert_TD(i, j, ep):
        a = free.pop(); alive[a] = True
        H[i, a] += 1.0; H[a, j] += 1.0
        acc_FH[ekey(i, a)] += 1.0; acc_FH[ekey(a, j)] += 1.0
        register_cycle([ekey(i, a), ekey(a, j), ekey(i, j)],
                       [ekey(i, a), ekey(a, j)], ep)
        return a

    def insert_TL2(i, j, ep):
        nonlocal tl_fallback
        # BFS depth-2 from i on H-support graph
        n1 = set(int(x) for x in h_neighbors(i))
        d2 = set()
        for m in n1:
            d2.update(int(x) for x in h_neighbors(m))
        d2 -= n1; d2.discard(i)
        d2 = [x for x in d2 if alive[x]]
        if not d2:
            tl_fallback += 1
            return insert_TD(i, j, ep)
        jp = int(d2[rng.integers(len(d2))])
        mids = [m for m in n1 if H[m, jp] > H_SUPPORT or H[jp, m] > H_SUPPORT]
        m = int(mids[rng.integers(len(mids))])
        a = free.pop(); alive[a] = True
        H[i, a] += 1.0; H[a, jp] += 1.0
        acc_FH[ekey(i, a)] += 1.0; acc_FH[ekey(a, jp)] += 1.0
        register_cycle([ekey(i, a), ekey(a, jp), ekey(i, m), ekey(m, jp)],
                       [ekey(i, a), ekey(a, jp)], ep)
        return a

    def dump(ep_next):
        if ckpt_path:
            import pickle, os as _os
            with open(ckpt_path + ".tmp", "wb") as fh:
                pickle.dump((rng, H, C, Wl, alive, free, nsub, ndead,
                             tl_fallback, saturated, snaps, cyc_edges,
                             cyc_newE, cyc_birth, cyc_dead, edge2cyc,
                             edge_attained, next_id, alive_log, ep_next),
                            fh)
            _os.replace(ckpt_path + ".tmp", ckpt_path)

    for ep in range(start_ep, epochs):
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
            break
        Wnext = {}
        rng.shuffle(events)
        for (i, j) in events:
            if not (alive[i] and alive[j]):
                continue
            c = 0.5 * (C[i, j] + C[j, i])
            if rng.random() < c and free:
                a = (insert_TD(i, j, ep) if cell == "TD"
                     else insert_TL2(i, j, ep))
                nsub += 1
                dst = outgoing(a)
                if not free:
                    saturated = True
            else:
                H[i, j] += (1.0 - c)
                acc_FH[ekey(i, j)] += (1.0 - c)
                d = outgoing(j, exclude=i)
                dst = d if d else [(j, i)]
            if not dst:
                continue
            cw = np.array([max(C[a_, b_], 1e-9) for (a_, b_) in dst])
            sh = cw / cw.sum()
            for L, s in zip(dst, sh):
                Wnext[L] = Wnext.get(L, 0.0) + s
                ek = ekey(L[0], L[1])
                acc_O[ek] += 1; acc_Fa[ek] += float(s)
        Wl = Wnext
        # decay actually drawn this epoch, per undirected edge (pure read)
        _sup = (H > H_SUPPORT) | (H.T > H_SUPPORT)
        _iu, _ju = np.where(np.triu(_sup, 1))
        for _a, _b in zip(_iu.tolist(), _ju.tolist()):
            acc_D[(_a, _b)] += (H[_a, _b] + H[_b, _a]) * gamma
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
        # ---- cycle death sweep (§7.6.1: S-support / R^theta) ------------
        # An edge "breaks" support only after having attained it once
        # (new-pole edges start at C=0 and need time to register).
        # Endpoint death kills the edge regardless of attainment.
        S = 0.5 * (C + C.T)
        newly_dead = []
        for e, cids in edge2cyc.items():
            if not cids:
                continue
            u, v = e
            supported = alive[u] and alive[v] and S[u, v] > S_SUPPORT
            if supported:
                edge_attained.add(e)
                continue
            endpoint_dead = not (alive[u] and alive[v])
            if endpoint_dead or e in edge_attained:
                for cid in list(cids):
                    died_by = ("new" if e in cyc_newE[cid] else "path")
                    cyc_dead[cid] = (ep, died_by)
                    newly_dead.append(cid)
                cids.clear()
        for cid in newly_dead:
            for e in cyc_edges[cid]:
                edge2cyc.get(e, set()).discard(cid)
        # ---- edge first-support bookkeeping (pure read) ------------------
        _sup2 = (H > H_SUPPORT) | (H.T > H_SUPPORT)
        _sup2 &= alive[:, None] & alive[None, :]
        _iu2, _ju2 = np.where(np.triu(_sup2, 1))
        _cur = set(zip(_iu2.tolist(), _ju2.tolist()))
        for _e in _cur:
            if _e not in edge_first:
                edge_first[_e] = ep
        # ---- snapshot ----------------------------------------------------
        if (ep + 1) % 25 == 0:
            idx2 = np.where(alive)[0]
            alive_cyc = [cid for cid in cyc_birth if cid not in cyc_dead]
            alive_log.append((ep + 1, sorted(alive_cyc)))
            # overlap graph stats via transpose index
            if alive_cyc:
                aset = set(alive_cyc)
                adj = {cid: set() for cid in alive_cyc}
                for e, cids in edge2cyc.items():
                    cs = [c for c in cids if c in aset]
                    for x in range(len(cs)):
                        for y in range(x + 1, len(cs)):
                            adj[cs[x]].add(cs[y]); adj[cs[y]].add(cs[x])
                # largest CC
                seen = set(); lcc = 0
                for start in alive_cyc:
                    if start in seen:
                        continue
                    q = deque([start]); seen.add(start); sz = 0
                    while q:
                        u = q.popleft(); sz += 1
                        for w in adj[u]:
                            if w not in seen:
                                seen.add(w); q.append(w)
                    lcc = max(lcc, sz)
                ncyc = len(alive_cyc)
                deg = np.array([len(adj[c]) for c in alive_cyc])
                dens = deg.sum() / (ncyc * (ncyc - 1)) if ncyc > 1 else 0.0
                ov = (lcc / ncyc, float(deg.mean()), float(dens),
                      int(dens > 0.5))
            else:
                ncyc = 0; ov = (0.0, 0.0, 0.0, 0)
            if len(idx2) >= 3:
                Sn = S[np.ix_(idx2, idx2)]
                ph, medC, d_cal, npts, w_cont = panel(Sn, len(idx2))
                vH, eH, cH, b1H = betti1(H > H_SUPPORT, alive)
                _, _, _, b1S = betti1(S > S_SUPPORT, alive)
                snaps.append((ep + 1, vH, eH, b1H, b1S, ph, d_cal, npts,
                              ncyc, *ov, round(w_cont, 6)))
            else:
                snaps.append((ep + 1, 0, 0, 0, 0, "DEAD", np.nan, 0,
                              ncyc, *ov, np.nan))
            # ---- flux ledger emission (pure read) ------------------------
            _S = 0.5 * (C + C.T)
            _keys = set(acc_O) | set(acc_FH) | set(acc_D) | set(H_start)
            for _e in _keys:
                _u, _v = _e
                _o = acc_O.get(_e, 0); _fa = acc_Fa.get(_e, 0.0)
                _fh = acc_FH.get(_e, 0.0); _d = acc_D.get(_e, 0.0)
                _alive_e = (alive[_u] and alive[_v]
                            and (H[_u, _v] > H_SUPPORT or H[_v, _u] > H_SUPPORT))
                _k = len(edge2cyc.get(_e, ()))
                _age = (ep + 1) - edge_first.get(_e, ep + 1)
                ledger_rows.append((
                    ep + 1, _u, _v, _o, round(_fa, 6), round(_fh, 6),
                    round(_d, 6), _k, round(H_start.get(_e, np.nan), 6),
                    round(S_start.get(_e, np.nan), 6), _age,
                    int(not _alive_e)))
            acc_O.clear(); acc_Fa.clear(); acc_FH.clear(); acc_D.clear()
            H_start.clear(); S_start.clear()
            for _e in _cur:
                _u, _v = _e
                H_start[_e] = float(H[_u, _v] + H[_v, _u])
                S_start[_e] = float(_S[_u, _v])
        if ckpt_path and (ep + 1) % ckpt_every == 0:
            dump(ep + 1)
            print(f"# ckpt ep {ep+1} V={int(alive.sum())}", flush=True)
    return (snaps, cyc_birth, cyc_dead, cyc_edges, alive_log,
            saturated, nsub, ndead, tl_fallback, epochs, ledger_rows)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    lam = 0.9
    g = float(sys.argv[1])
    epochs = int(sys.argv[2])
    seeds = [int(s) for s in sys.argv[3].split(",")]
    NMAX = int(sys.argv[4])
    cell = sys.argv[5]
    assert cell in ("TD", "TL2")
    ckpt = sys.argv[6] if len(sys.argv) > 6 else None

    for seed in seeds:
        (snaps, birth, dead, cedges, alive_log, sat, nsub, ndead,
         tl_fb, eps_, ledger) = run(seed, lam, g, cell, epochs,
                                    ckpt_path=ckpt)
        lifetimes = [dead[c][0] - birth[c] for c in dead]
        cens = len(birth) - len(dead)
        newdeath = sum(1 for c in dead if dead[c][1] == "new")
        metr5 = sum(1 for s in snaps if s[5] == "METR" and s[7] >= 5)
        lt = np.array(lifetimes) if lifetimes else np.array([np.nan])
        print(f"cell={cell} g={g} s={seed} SAT={'YES' if sat else 'no'} "
              f"cycles={len(birth)} dead={len(dead)} censored={cens} "
              f"cyc_life_med={np.nanmedian(lt):.0f} "
              f"died_new_frac={newdeath/max(len(dead),1):.3f} "
              f"robBSW={metr5} tl_fallback={tl_fb} nsub={nsub}")
        base = f"campA_{cell}_g{g}_s{seed}"
        with open(base + ".tsv", "w") as fo:
            fo.write("epoch\tV\tE\tb1H\tb1S\tlabel\td_cal\tnpts"
                     "\tn_alive_cyc\tov_lcc\tov_meandeg\tov_density"
                     "\tdegenerate\tw_cont\n")
            for s in snaps:
                fo.write("\t".join(str(x) for x in s) + "\n")
        with open(base + "_cycles.tsv", "w") as fo:
            fo.write("cycle_id\tbirth\tdeath\tlifetime\tdied_by\tlen\n")
            for cid in sorted(birth):
                if cid in dead:
                    dep, by = dead[cid]
                    fo.write(f"{cid}\t{birth[cid]}\t{dep}"
                             f"\t{dep-birth[cid]}\t{by}"
                             f"\t{len(cedges[cid])}\n")
                else:
                    fo.write(f"{cid}\t{birth[cid]}\t-1\t-1\tcensored"
                             f"\t{len(cedges[cid])}\n")
        with open(base + "_alive.tsv", "w") as fo:
            for ep, ids in alive_log:
                fo.write(f"{ep}\t{','.join(map(str, ids))}\n")
        with open(base + "_ledger.tsv", "w") as fo:
            fo.write("epoch\tu\tv\tO\tF_alloc\tF_H\tD\tk\tH_start"
                     "\tS_start\tage_e\tdied\n")
            for r in ledger:
                fo.write("\t".join(str(x) for x in r) + "\n")
        with open(base + "_cycedges.tsv", "w") as fo:
            fo.write("cycle_id\tedges\n")
            for cid in sorted(cedges):
                fo.write(f"{cid}\t" + ";".join(
                    f"{a}_{b}" for a, b in cedges[cid]) + "\n")
        print(f"    -> {base}.tsv / _cycles.tsv / _alive.tsv "
              f"/ _ledger.tsv ({len(ledger)} rows) / _cycedges.tsv")

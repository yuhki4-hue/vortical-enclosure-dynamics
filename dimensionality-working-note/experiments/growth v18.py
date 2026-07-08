"""v18: directed ledger -- restoring the antisymmetric sector
(pre-registered 5.41).

Ledger is DIRECTED: w[i->j] != w[j->i]. An event i->j deposits its total
1 unit into OUTGOING links of j (j->k, k != i); if j's only exit is j->i,
reflect (deposit on j->i). The fired link itself receives nothing:
persistence requires re-feeding from upstream => circulation.
Distribution: C-weighted (directed version of variant C... per 5.41.2
"分配形は C 重み" -- variant B weighting on directed exits).
Slow layer (H, C) symmetric, unchanged. sigma=1 by total-1 invariance.
Control: v17-C same seeds with dense snapshots.
Panel: window occupancy, consecutive-METR lengths, ledger asymmetry,
sigma audit, standard panel. Snapshots every 25 epochs.
"""
import sys
import numpy as np
from scipy.sparse.csgraph import shortest_path, connected_components

NMAX = 300
LINK_EPS = 1e-6
SNAPS = tuple(range(25, 301, 25))

def panel(S, ngrown):
    Sc = np.clip(S, 1e-12, 1-1e-12)
    W = -np.log(Sc); np.fill_diagonal(W, 0.0)
    mask = Sc > LINK_EPS; np.fill_diagonal(mask, False)
    cl = S[mask] if mask.sum() else np.array([0.0])
    medC = float(np.median(cl)); f09 = float((cl > 0.9).mean())
    Wg = np.where(mask, W, 0.0)
    nc, lab = connected_components((Wg > 0), directed=False)
    big = np.bincount(lab).argmax(); keep = lab == big
    gcf = keep.sum()/max(ngrown,1)
    D = shortest_path(Wg[np.ix_(keep,keep)], method='D', directed=False)
    n = D.shape[0]; fin = np.isfinite(D) & (D > 0)
    nn = []
    for i in range(n):
        v = D[i][fin[i]]
        if v.size: nn.append(v.min())
    d_cal = np.nan
    if nn:
        unit = np.median(nn); rs = unit*np.arange(1, 40)
        counts = np.array([((D <= r) & np.isfinite(D)).sum(1).mean() for r in rs])
        sel = (counts > 5) & (counts < 0.5*n)
        if sel.sum() >= 4:
            bd = float(np.polyfit(np.log(rs[sel]), np.log(counts[sel]), 1)[0])
            m = np.array([0.91,1.70,2.20]); t = np.array([1.,2.,3.])
            if bd > m[-1]: d_cal = t[-1]+(bd-m[-1])*(t[-1]-t[-2])/(m[-1]-m[-2])
            elif bd < m[0]: d_cal = t[0]+(bd-m[0])*(t[1]-t[0])/(m[1]-m[0])
            else: d_cal = float(np.interp(bd, m, t))
    if gcf < 0.6: ph = "FRAG"
    elif medC > 0.9: ph = "SAT"
    elif not np.isfinite(d_cal): ph = "SW"
    else: ph = "METR"
    return ph, medC, d_cal

def run(seed, lam, gamma, directed, epochs=300):
    rng = np.random.default_rng(seed)
    H = np.zeros((NMAX, NMAX)); C = np.zeros((NMAX, NMAX))
    Wl = {}   # directed: (i,j) ordered -> weight ; symmetric mode: same dict, key ordered pair too
    alive = np.zeros(NMAX, dtype=bool)
    free = list(range(NMAX-1, -1, -1))
    kappa = gamma
    nsub = ndead = ndyad = 0
    audit_ok = True
    snaps = []; asym_hist = []
    def outgoing(j, exclude=None):
        nb = np.where((H[j, :] > 1e-12) & alive)[0]
        return [(j, int(k)) for k in nb if k != j and (exclude is None or k != exclude)]
    for ep in range(epochs):
        # fire
        events = []
        for L, w in list(Wl.items()):
            i, j = L
            if not (alive[i] and alive[j]) or H[i, j] <= 1e-12:
                continue
            k = rng.poisson(w)
            events += [L]*int(k)
        # floor
        live_links = [(i, j) for (i, j) in Wl.keys() if alive[i] and alive[j] and H[i,j] > 1e-12]
        if not live_links:
            all_pairs = np.argwhere(np.triu(H, 1) > 1e-12)
            live = [(int(a), int(b)) for a, b in all_pairs if alive[a] and alive[b]]
            if live:
                a_, b_ = live[rng.integers(len(live))]
                events.append((a_, b_) if rng.random() < 0.5 else (b_, a_))
            elif len(free) >= 2:
                a = free.pop(); b = free.pop()
                alive[a] = alive[b] = True
                H[a, b] = H[b, a] = 1.0
                events.append((a, b)); ndyad += 1
        else:
            L = live_links[rng.integers(len(live_links))]
            events.append(L)
        if len(events) > 100_000:
            return "RUNAWAY", snaps, asym_hist, nsub, ndead, audit_ok
        Wnext = {}
        rng.shuffle(events)
        for (i, j) in events:
            if not (alive[i] and alive[j]): continue
            c = C[i, j]
            if rng.random() < c and free:
                a = free.pop(); alive[a] = True
                H[i, a] += 1.0; H[a, i] += 1.0
                H[j, a] += 1.0; H[a, j] += 1.0
                nsub += 1
                dst = outgoing(a)
            else:
                H[i, j] += (1.0 - c); H[j, i] += (1.0 - c)
                if directed:
                    dst = outgoing(j, exclude=i)
                    if not dst: dst = [(j, i)]   # reflection
                else:
                    # symmetric control (v17-C style): incident links of i and j
                    dst = outgoing(i) + outgoing(j)
            if not dst: continue
            cw = np.array([max(C[a_, b_], 1e-9) for (a_, b_) in dst])
            sh = cw/cw.sum()
            for L, s in zip(dst, sh):
                Wnext[L] = Wnext.get(L, 0.0) + s
        nvalid = len([e for e in events if alive[e[0]] and alive[e[1]]])
        if events and abs(sum(Wnext.values()) - nvalid) > 1 + 0.05*len(events):
            audit_ok = False
        Wl = Wnext
        # asymmetry diagnostic
        num = den = 0.0
        seen = set()
        for (i, j), w in Wl.items():
            if (j, i) in seen or (i, j) in seen: continue
            seen.add((i, j))
            w2 = Wl.get((j, i), 0.0)
            num += abs(w - w2); den += w + w2
        asym_hist.append(num/den if den > 0 else 0.0)
        # slow layer
        H *= (1.0 - gamma)
        idx = np.where(alive)[0]
        if len(idx):
            rho = np.zeros(NMAX)
            for (i, j) in events:
                rho[i] += 1; rho[j] += 1
            Ceq = np.zeros((NMAX, NMAX))
            sub2 = 1 - np.exp(-lam * rho[idx][:,None] * H[np.ix_(idx, idx)])
            Ceq[np.ix_(idx, idx)] = 0.5*(sub2 + sub2.T)
            C += kappa*(Ceq - C)
            C[~alive, :] = 0.0; C[:, ~alive] = 0.0
            Ssub = C[np.ix_(idx, idx)]
            haslink = (Ssub > LINK_EPS).sum(1) > 0
            for dnode in idx[~haslink]:
                alive[dnode] = False
                H[dnode, :] = 0.0; H[:, dnode] = 0.0
                C[dnode, :] = 0.0; C[:, dnode] = 0.0
                free.append(int(dnode)); ndead += 1
        if (ep + 1) in SNAPS:
            idx2 = np.where(alive)[0]
            if len(idx2) >= 3:
                snaps.append((ep+1,) + panel(C[np.ix_(idx2, idx2)], len(idx2)))
            else:
                snaps.append((ep+1, "DEAD", np.nan, np.nan))
    return "ok", snaps, asym_hist, nsub, ndead, audit_ok

lam, g = 0.9, 0.15
mode = sys.argv[1]           # "dir" or "sym"
seeds = [int(s) for s in sys.argv[2].split(",")]
directed = (mode == "dir")
for seed in seeds:
    status, snaps, asym, nsub, ndead, audit = run(seed, lam, g, directed)
    occ = sum(1 for s in snaps if s[1] == "METR")
    # longest consecutive METR run
    best = cur = 0
    for s in snaps:
        cur = cur + 1 if s[1] == "METR" else 0
        best = max(best, cur)
    trace = " ".join(f"{s[0]}:{s[1]}" for s in snaps)
    ma = np.mean(asym[-100:]) if asym else 0
    print(f"{mode} s={seed} [{status}] occ={occ}/12 maxrun={best} "
          f"asym={ma:4.2f} sub={nsub} dead={ndead} audit={'OK' if audit else 'FAIL'}")
    print(f"   {trace}")

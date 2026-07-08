"""v13: path-saturation conversion trigger (pre-registered 5.21).
Trigger = mean C along the strong-tie path w->tgt (BFS parents recorded).
Validity criterion: conversions >= 10% of closure attempts, else INVALID.
Panel: + NMAX-hit epoch. pc in {0.01, 0.02, 0.05}, cell (0.3, 0.05).
"""
import numpy as np
from scipy.sparse.csgraph import shortest_path, connected_components

NMAX = 600; PB = 0.02; THETA = 0.75; K = 2
LAM = 0.3; GAMMA = 0.05
TOTAL_EVENTS = 36_000; EVENTS_PER_EPOCH = 3_000

def solve_rho(H, lam, iters=500):
    rho = np.ones(H.shape[0])
    for _ in range(iters):
        rn = (1 - np.exp(-lam*rho[:,None]*H)).sum(1)
        if np.allclose(rn, rho, atol=1e-12): break
        rho = 0.5*rho + 0.5*rn
    return rho

def panel(S, ngrown):
    Sc = np.clip(S, 1e-12, 1-1e-12)
    W = -np.log(Sc); np.fill_diagonal(W, 0.0)
    mask = Sc > 1e-6; np.fill_diagonal(mask, False)
    cl = S[mask] if mask.sum() else np.array([0.0])
    medC = float(np.median(cl)); f09 = float((cl > 0.9).mean())
    E = int(mask.sum() // 2)
    Wg = np.where(mask, W, 0.0)
    nc, lab = connected_components((Wg > 0), directed=False)
    big = np.bincount(lab).argmax(); keep = lab == big
    gcf = keep.sum()/ngrown
    cyc = E - ngrown + nc
    D = shortest_path(Wg[np.ix_(keep,keep)], method='D', directed=False)
    n = D.shape[0]; fin = np.isfinite(D) & (D > 0)
    dq = np.quantile(D[fin], [0.5, 0.95]) if fin.sum() else (np.nan, np.nan)
    nn = []
    for i in range(n):
        v = D[i][fin[i]]
        if v.size: nn.append(v.min())
    d_cal, cv = np.nan, np.nan
    if nn:
        unit = np.median(nn); rs = unit*np.arange(1, 40)
        counts = np.array([((D <= r) & np.isfinite(D)).sum(1).mean() for r in rs])
        sel = (counts > 5) & (counts < 0.5*n)
        if sel.sum() >= 4:
            bd = float(np.polyfit(np.log(rs[sel]), np.log(counts[sel]), 1)[0])
            rmid = rs[sel][len(rs[sel])//2]
            Ni = ((D <= rmid) & np.isfinite(D)).sum(1)
            cv = float(Ni.std()/Ni.mean())
            m = np.array([0.91,1.70,2.20]); t = np.array([1.,2.,3.])
            if bd > m[-1]: d_cal = t[-1]+(bd-m[-1])*(t[-1]-t[-2])/(m[-1]-m[-2])
            elif bd < m[0]: d_cal = t[0]+(bd-m[0])*(t[1]-t[0])/(m[1]-m[0])
            else: d_cal = float(np.interp(bd, m, t))
    if gcf < 0.6: ph = "FRAG"
    elif medC > 0.9: ph = "SAT "
    elif not np.isfinite(d_cal): ph = "SW  "
    else: ph = "METR"
    return ph, medC, f09, gcf, d_cal, cv, dq, cyc

def stball_paths(Cs, n, w, k):
    """strong-tie ball with parent tracking; returns dict target -> path mean C."""
    m_ = Cs.shape[0]
    if w >= m_: return {}
    parent = {w: None}
    frontier = [w]; out = {}
    depth = 0
    while frontier and depth < k:
        depth += 1
        nxt = []
        for u in frontier:
            if u >= m_: continue
            for v in np.where(Cs[u, :m_] >= THETA)[0]:
                v = int(v)
                if v not in parent:
                    parent[v] = u
                    nxt.append(v)
                    if depth >= 2:
                        # reconstruct path C values
                        cs = []
                        a, b = v, parent[v]
                        while b is not None:
                            cs.append(Cs[a, b]); a, b = b, parent[b]
                        out[v] = float(np.mean(cs))
        frontier = nxt
    return out

def run(seed, pc):
    rng = np.random.default_rng(seed)
    H = np.zeros((NMAX, NMAX)); n = 2; H[0,1] = H[1,0] = 1.0
    pos = [0, 1]
    rho = solve_rho(H[:n,:n], LAM)
    C = 1 - np.exp(-LAM*rho[:,None]*H[:n,:n]); Cs = 0.5*(C+C.T)
    ev = 0; evep = 0; nconv = 0; nattempt = 0; nmax_ep = -1; ep = 0
    while ev < TOTAL_EVENTS:
        for b in rng.permutation(n):
            if ev >= TOTAL_EVENTS: break
            u = rng.random(); w = pos[b]
            if u < PB and n < NMAX:
                H[w, n] += 1.0; H[n, w] += 1.0
                pos[b] = n; pos.append(n); n += 1
                if n == NMAX and nmax_ep < 0: nmax_ep = ep
            elif u < PB + pc:
                cand = stball_paths(Cs, n, w, K)
                if cand:
                    nattempt += 1
                    tgt = int(rng.choice(list(cand.keys())))
                    pathC = cand[tgt]
                    if rng.random() < pathC and n < NMAX:
                        H[w, n] += 1.0; H[n, w] += 1.0
                        H[tgt, n] += 1.0; H[n, tgt] += 1.0
                        pos.append(n); n += 1; nconv += 1
                        if n == NMAX and nmax_ep < 0: nmax_ep = ep
                    else:
                        c = Cs[w, tgt] if (w < Cs.shape[0] and tgt < Cs.shape[0]) else 0.0
                        H[w, tgt] += (1.0 - c); H[tgt, w] += (1.0 - c)
            else:
                m_ = Cs.shape[0]; p = np.zeros(n)
                if w < m_: p[:m_] = Cs[w, :m_]
                p += 1e-9*(H[w,:n]+H[:n,w]); p[w] = 0.0
                ss = p.sum()
                if ss < 1e-12:
                    nb = np.where(H[w,:n]+H[:n,w] > 0)[0]; nb = nb[nb != w]
                    nxt = int(rng.choice(nb)) if len(nb) else w
                else:
                    nxt = int(rng.choice(n, p=p/ss))
                c = Cs[w, nxt] if (w < Cs.shape[0] and nxt < Cs.shape[0]) else 0.0
                H[w, nxt] += (1.0 - c); pos[b] = nxt
            ev += 1; evep += 1
            if evep >= EVENTS_PER_EPOCH:
                H[:n,:n] *= (1.0-GAMMA)
                rho = solve_rho(H[:n,:n], LAM)
                C = 1 - np.exp(-LAM*rho[:,None]*H[:n,:n]); Cs = 0.5*(C+C.T)
                evep = 0; ep += 1
    rho = solve_rho(H[:n,:n], LAM)
    C = 1 - np.exp(-LAM*rho[:,None]*H[:n,:n])
    res = panel(0.5*(C+C.T)[:n,:n], n)
    return res, nconv, nattempt, nmax_ep, n

print(f"v13 path-saturation trigger, cell (l={LAM},g={GAMMA}); "
      f"baseline d=1.63+-0.06; validity: conv/attempt >= 10%")
for pc in (0.01, 0.02, 0.05):
    for seed in (5, 6, 7):
        (ph, medC, f09, gcf, d, cv, dq, cyc), nconv, natt, nmax_ep, n = run(seed, pc)
        ds = f"{d:5.2f}" if np.isfinite(d) else "  nan"
        cs = f"{cv:4.2f}" if np.isfinite(cv) else " nan"
        rate = nconv/max(natt,1)
        valid = "VALID" if rate >= 0.10 else "INVALID"
        print(f"  pc={pc} s={seed}: {ph} d={ds} cv={cs} f09={f09:4.2f} cyc={cyc:4d} "
              f"conv={nconv:4d}/{natt:4d} ({rate:4.0%}) NMAXep={nmax_ep:3d} N={n} [{valid}]")

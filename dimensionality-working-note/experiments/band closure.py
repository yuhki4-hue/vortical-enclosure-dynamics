"""(lambda, gamma) phase scan of the v9 parallel model.
Order parameters per cell: median link C (saturation), giant-component
fraction (fragmentation), ball d_cal, CV (heterogeneity).
Phase rule (fixed in advance):
  FRAG   if gc < 0.6 N_grown
  SAT    if median existing-link C > 0.9  (or no scaling window while connected)
  METRIC otherwise (window exists, connected, C intermediate)
"""
import numpy as np
from scipy.sparse.csgraph import shortest_path, connected_components

NMAX = 600; PB = 0.02; PC = 0.0; LAG = 6
TOTAL_EVENTS = 36_000; EVENTS_PER_EPOCH = 3_000

def solve_rho(H, lam, iters=500):
    rho = np.ones(H.shape[0])
    for _ in range(iters):
        rn = (1 - np.exp(-lam*rho[:,None]*H)).sum(1)
        if np.allclose(rn, rho, atol=1e-12): break
        rho = 0.5*rho + 0.5*rn
    return rho

def analyze(S, ngrown):
    Sc = np.clip(S, 1e-12, 1-1e-12)
    W = -np.log(Sc); np.fill_diagonal(W, 0.0)
    mask = Sc > 1e-6
    np.fill_diagonal(mask, False)
    medC = float(np.median(S[mask])) if mask.sum() else 0.0
    Wg = np.where(mask, W, 0.0)
    nc, lab = connected_components((Wg > 0), directed=False)
    big = np.bincount(lab).argmax()
    keep = lab == big
    gcf = keep.sum() / ngrown
    Wb = Wg[np.ix_(keep, keep)]
    D = shortest_path(Wb, method='D', directed=False)
    n = D.shape[0]; fin = np.isfinite(D)
    nn = []
    for i in range(n):
        v = D[i][fin[i] & (D[i] > 0)]
        if v.size: nn.append(v.min())
    if not nn:
        return medC, gcf, np.nan, np.nan
    unit = np.median(nn)
    rs = unit*np.arange(1, 40)
    counts = np.array([((D <= r) & fin).sum(1).mean() for r in rs])
    sel = (counts > 5) & (counts < 0.5*n)
    if sel.sum() < 4:
        return medC, gcf, np.nan, np.nan
    bd = float(np.polyfit(np.log(rs[sel]), np.log(counts[sel]), 1)[0])
    rmid = rs[sel][len(rs[sel])//2]
    Ni = ((D <= rmid) & fin).sum(1)
    cv = float(Ni.std()/Ni.mean())
    m = np.array([0.91, 1.70, 2.20]); t = np.array([1., 2., 3.])
    if bd > m[-1]: d = t[-1] + (bd-m[-1])*(t[-1]-t[-2])/(m[-1]-m[-2])
    elif bd < m[0]: d = t[0] + (bd-m[0])*(t[1]-t[0])/(m[1]-m[0])
    else: d = float(np.interp(bd, m, t))
    return medC, gcf, d, cv

def run(seed, lam, gamma):
    rng = np.random.default_rng(seed)
    H = np.zeros((NMAX, NMAX))
    n = 2; H[0,1] = H[1,0] = 1.0
    pos = [0, 1]; logs = [[0], [1]]
    rho = solve_rho(H[:n,:n], lam)
    C = 1 - np.exp(-lam*rho[:,None]*H[:n,:n]); Cs = 0.5*(C+C.T)
    ev = 0; evep = 0
    while ev < TOTAL_EVENTS:
        for b in rng.permutation(n):
            if ev >= TOTAL_EVENTS: break
            u = rng.random(); w = pos[b]
            if u < PB and n < NMAX:
                H[w, n] += 1.0; H[n, w] += 1.0
                pos[b] = n; pos.append(n); logs.append([n]); logs[b].append(n)
                n += 1
            elif u < PB + PC and len(logs[b]) > LAG+1:
                tgt = int(logs[b][-LAG])
                if tgt != w: H[w, tgt] += 1.0; H[tgt, w] += 1.0
            else:
                m_ = Cs.shape[0]
                p = np.zeros(n)
                if w < m_: p[:m_] = Cs[w, :m_]
                p += 1e-9*(H[w,:n]+H[:n,w]); p[w] = 0.0
                ss = p.sum()
                if ss < 1e-12:
                    nb = np.where(H[w,:n]+H[:n,w] > 0)[0]; nb = nb[nb != w]
                    nxt = int(rng.choice(nb)) if len(nb) else w
                else:
                    nxt = int(rng.choice(n, p=p/ss))
                H[w, nxt] += 1.0; pos[b] = nxt; logs[b].append(nxt)
                if len(logs[b]) > 120: logs[b] = logs[b][-60:]
            ev += 1; evep += 1
            if evep >= EVENTS_PER_EPOCH:
                H[:n,:n] *= (1.0-gamma)
                rho = solve_rho(H[:n,:n], lam)
                C = 1 - np.exp(-lam*rho[:,None]*H[:n,:n]); Cs = 0.5*(C+C.T)
                evep = 0
    rho = solve_rho(H[:n,:n], lam)
    C = 1 - np.exp(-lam*rho[:,None]*H[:n,:n])
    medC, gcf, d, cv = analyze(0.5*(C+C.T)[:n,:n], n)
    if gcf < 0.6: ph = "FRAG"
    elif medC > 0.9 or not np.isfinite(d): ph = "SAT "
    else: ph = "METR"
    return ph, medC, gcf, d, cv

import sys
cells = ((0.05, 0.05), (0.1, 0.1), (0.2, 0.2))
pcs = (0.02, 0.05, 0.1)
print("closure sweep inside the metric band (LAG=6), seeds 5,6")
for lam, g in cells:
    for pc in pcs:
        globals()['PC'] = pc
        res = []
        for seed in (5, 6):
            ph, medC, gcf, d, cv = run(seed, lam, g)
            ds = f"{d:5.2f}" if np.isfinite(d) else "  nan"
            res.append(f"{ph} d={ds} cv={cv:4.2f} gc={gcf:4.2f}")
        print(f"  (l={lam}, g={g}) pc={pc}: " + " | ".join(res))

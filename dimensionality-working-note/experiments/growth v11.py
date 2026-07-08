"""v11: locality x anti-saturation (design pre-registered, note section 5.17).
dH = (1 - C) applied UNIFORMLY to all registrations (move/closure/branch).
Stage 1: 3x3 mini-scan (pc=0) to relocate the band.
Stage 2: strong-tie closure theta=0.75, k=2 inside relocated band.
Diagnostic panel always on: linkC quantiles, frac(C>0.9), geodesic quantiles.
"""
import sys
import numpy as np
from scipy.sparse.csgraph import shortest_path, connected_components

NMAX = 600; PB = 0.02; THETA = 0.75; K = 2
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
    Wg = np.where(mask, W, 0.0)
    nc, lab = connected_components((Wg > 0), directed=False)
    big = np.bincount(lab).argmax(); keep = lab == big
    gcf = keep.sum()/ngrown
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
        counts = np.array([((D <= r) & (np.isfinite(D))).sum(1).mean() for r in rs])
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
    return ph, medC, f09, gcf, d_cal, cv, dq

def stball(Cs, n, w, k):
    m_ = Cs.shape[0]
    if w >= m_: return []
    frontier = {w}; seen = {w}; out = []
    for depth in range(1, k+1):
        nxt = set()
        for u in frontier:
            if u >= m_: continue
            for v in np.where(Cs[u, :m_] >= THETA)[0]:
                if v not in seen:
                    seen.add(v); nxt.add(int(v))
                    if depth >= 2: out.append(int(v))
        frontier = nxt
        if not frontier: break
    return out

def run(seed, lam, gamma, pc):
    rng = np.random.default_rng(seed)
    H = np.zeros((NMAX, NMAX)); n = 2; H[0,1] = H[1,0] = 1.0
    pos = [0, 1]
    rho = solve_rho(H[:n,:n], lam)
    C = 1 - np.exp(-lam*rho[:,None]*H[:n,:n]); Cs = 0.5*(C+C.T)
    ev = 0; evep = 0
    while ev < TOTAL_EVENTS:
        for b in rng.permutation(n):
            if ev >= TOTAL_EVENTS: break
            u = rng.random(); w = pos[b]
            if u < PB and n < NMAX:
                dH = 1.0   # new pair: C = 0 -> (1-C) = 1
                H[w, n] += dH; H[n, w] += dH
                pos[b] = n; pos.append(n); n += 1
            elif u < PB + pc:
                cand = stball(Cs, n, w, K)
                if cand:
                    tgt = int(rng.choice(cand))
                    c = Cs[w, tgt] if (w < Cs.shape[0] and tgt < Cs.shape[0]) else 0.0
                    dH = 1.0 - c
                    H[w, tgt] += dH; H[tgt, w] += dH
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
                H[w, nxt] += (1.0 - c)
                pos[b] = nxt
            ev += 1; evep += 1
            if evep >= EVENTS_PER_EPOCH:
                H[:n,:n] *= (1.0-gamma)
                rho = solve_rho(H[:n,:n], lam)
                C = 1 - np.exp(-lam*rho[:,None]*H[:n,:n]); Cs = 0.5*(C+C.T)
                evep = 0
    rho = solve_rho(H[:n,:n], lam)
    C = 1 - np.exp(-lam*rho[:,None]*H[:n,:n])
    return panel(0.5*(C+C.T)[:n,:n], n)

stage = sys.argv[1]
if stage == "scan":
    for lam in (0.1, 0.3, 0.9):
        for g in (0.05, 0.15, 0.4):
            ph, medC, f09, gcf, d, cv, dq = run(5, lam, g, 0.0)
            ds = f"{d:5.2f}" if np.isfinite(d) else "  nan"
            print(f"l={lam:4} g={g:4}: {ph} medC={medC:4.2f} f09={f09:4.2f} "
                  f"gc={gcf:4.2f} d={ds} cv={cv if np.isfinite(cv) else float('nan'):4.2f} "
                  f"geo(q50,q95)=({dq[0]:5.2f},{dq[1]:5.2f})")
else:
    cells = eval(stage)
    for lam, g in cells:
        for pc in (0.0, 0.02, 0.05):
            parts = []
            for seed in (5, 6, 7):
                ph, medC, f09, gcf, d, cv, dq = run(seed, lam, g, pc)
                ds = f"{d:5.2f}" if np.isfinite(d) else "  nan"
                parts.append(f"{ph} d={ds} f09={f09:4.2f} geo50={dq[0]:4.2f}")
            print(f"(l={lam},g={g}) pc={pc}: " + " | ".join(parts))

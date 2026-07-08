"""v10: strong-tie closure (design pre-registered in note section 5.15).

Closure target: BFS from w over links with C >= theta_w only, depth k,
theta_w = median of w's OWN positive link C values (relative theta, no
external constant). Candidates = nodes at hop >= 2 within the ball
(hop-1 closure would be mere reinforcement). Classifier gains SW label.
"""
import sys
import numpy as np
from scipy.sparse.csgraph import shortest_path, connected_components

NMAX = 600; PB = 0.02
THETA_FIXED = None
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
    mask = Sc > 1e-6; np.fill_diagonal(mask, False)
    medC = float(np.median(S[mask])) if mask.sum() else 0.0
    Wg = np.where(mask, W, 0.0)
    nc, lab = connected_components((Wg > 0), directed=False)
    big = np.bincount(lab).argmax(); keep = lab == big
    gcf = keep.sum()/ngrown
    D = shortest_path(Wg[np.ix_(keep,keep)], method='D', directed=False)
    n = D.shape[0]; fin = np.isfinite(D)
    nn = []
    for i in range(n):
        v = D[i][fin[i] & (D[i] > 0)]
        if v.size: nn.append(v.min())
    d_cal, cv = np.nan, np.nan
    if nn:
        unit = np.median(nn); rs = unit*np.arange(1, 40)
        counts = np.array([((D <= r) & fin).sum(1).mean() for r in rs])
        sel = (counts > 5) & (counts < 0.5*n)
        if sel.sum() >= 4:
            bd = float(np.polyfit(np.log(rs[sel]), np.log(counts[sel]), 1)[0])
            rmid = rs[sel][len(rs[sel])//2]
            Ni = ((D <= rmid) & fin).sum(1)
            cv = float(Ni.std()/Ni.mean())
            m = np.array([0.91,1.70,2.20]); t = np.array([1.,2.,3.])
            if bd > m[-1]: d_cal = t[-1] + (bd-m[-1])*(t[-1]-t[-2])/(m[-1]-m[-2])
            elif bd < m[0]: d_cal = t[0] + (bd-m[0])*(t[1]-t[0])/(m[1]-m[0])
            else: d_cal = float(np.interp(bd, m, t))
    if gcf < 0.6: ph = "FRAG"
    elif medC > 0.9: ph = "SAT "
    elif not np.isfinite(d_cal): ph = "SW  "
    else: ph = "METR"
    return ph, medC, gcf, d_cal, cv

def strong_tie_ball(Cs, H, n, w, k):
    """nodes reachable from w via links C >= theta_w, depth k; hop >= 2 only."""
    m_ = Cs.shape[0]
    if w >= m_: return []
    row = Cs[w, :m_]
    pos = row[row > 1e-6]
    if pos.size == 0: return []
    theta = THETA_FIXED if THETA_FIXED is not None else float(np.median(pos))
    frontier = {w}; seen = {w}; hops = {w: 0}
    out = []
    for depth in range(1, k+1):
        nxt = set()
        for u in frontier:
            if u >= m_: continue
            nbr = np.where(Cs[u, :m_] >= theta)[0]
            for v in nbr:
                if v not in seen:
                    seen.add(v); hops[v] = depth; nxt.add(int(v))
                    if depth >= 2: out.append(int(v))
        frontier = nxt
        if not frontier: break
    return out

def run(seed, lam, gamma, pc, k):
    rng = np.random.default_rng(seed)
    H = np.zeros((NMAX, NMAX))
    n = 2; H[0,1] = H[1,0] = 1.0
    pos = [0, 1]
    rho = solve_rho(H[:n,:n], lam)
    C = 1 - np.exp(-lam*rho[:,None]*H[:n,:n]); Cs = 0.5*(C+C.T)
    ev = 0; evep = 0
    while ev < TOTAL_EVENTS:
        for b in rng.permutation(n):
            if ev >= TOTAL_EVENTS: break
            u = rng.random(); w = pos[b]
            if u < PB and n < NMAX:
                H[w, n] += 1.0; H[n, w] += 1.0
                pos[b] = n; pos.append(n); n += 1
            elif u < PB + pc:
                cand = strong_tie_ball(Cs, H, n, w, k)
                if cand:
                    tgt = int(rng.choice(cand))
                    H[w, tgt] += 1.0; H[tgt, w] += 1.0
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
                H[w, nxt] += 1.0; pos[b] = nxt
            ev += 1; evep += 1
            if evep >= EVENTS_PER_EPOCH:
                H[:n,:n] *= (1.0-gamma)
                rho = solve_rho(H[:n,:n], lam)
                C = 1 - np.exp(-lam*rho[:,None]*H[:n,:n]); Cs = 0.5*(C+C.T)
                evep = 0
    rho = solve_rho(H[:n,:n], lam)
    C = 1 - np.exp(-lam*rho[:,None]*H[:n,:n])
    return analyze(0.5*(C+C.T)[:n,:n], n)

cells = eval(sys.argv[1])
THETA_FIXED = float(sys.argv[2]) if len(sys.argv) > 2 else None
for lam, g in cells:
    for pc in (0.02, 0.05):
        for k in (2, 3):
            parts = []
            for seed in (5, 6, 7):
                ph, medC, gcf, d, cv = run(seed, lam, g, pc, k)
                ds = f"{d:5.2f}" if np.isfinite(d) else "  nan"
                cs = f"{cv:4.2f}" if np.isfinite(cv) else " nan"
                parts.append(f"{ph} d={ds} cv={cs}")
            print(f"(l={lam},g={g}) pc={pc} k={k}: " + " | ".join(parts))

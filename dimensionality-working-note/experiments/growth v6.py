"""v6: lambda above the sparse-survival threshold + two closure modes.

From 5.9.3: a chain (deg 2, H=1) survives the fixed point iff 2*lam > 1.
Set LAM = 1.0 so sparse geometry persists. Closure modes:
  'window': target uniform over last LWIN of own log (loop lengths random)
  'lag':    target = traj[-LAG] (fixed loop length -- a vortex with a size;
            dynamical version of the re-addressing quantum, K4)
"""
import numpy as np
from scipy.sparse.csgraph import shortest_path, connected_components

LAM = 1.0; GAMMA = 0.02; EPOCHS = 18; EV = 3000
NMAX = 900; LWIN = 50; LAG = 12

def solve_rho(H, lam, iters=600):
    rho = np.ones(H.shape[0])
    for _ in range(iters):
        rn = (1 - np.exp(-lam*rho[:,None]*H)).sum(1)
        if np.allclose(rn, rho, atol=1e-12): break
        rho = 0.5*rho + 0.5*rn
    return rho

def dim_geodesic(S):
    Sc = np.clip(S, 1e-12, 1-1e-12)
    W = -np.log(Sc); np.fill_diagonal(W, 0.0)
    W[Sc < 1e-6] = 0.0
    ncomp, lab = connected_components((W > 0), directed=False)
    if ncomp > 1:
        big = np.bincount(lab).argmax()
        keep = lab == big
        W = W[np.ix_(keep, keep)]
    D = shortest_path(W, method='D', directed=False)
    fin = np.isfinite(D) & (D > 0)
    if fin.sum() < 100: return np.nan, 0.0, W.shape[0]
    med = np.median(D[fin])
    Dc = np.where(np.isfinite(D), D, D[np.isfinite(D)].max()*2)
    K = np.exp(-Dc/med)
    ev = np.linalg.eigvalsh(K)[::-1]
    ev = ev[ev > 1e-12*ev[0]]
    k = np.arange(1, len(ev)+1)
    sel = (k >= 5) & (k <= max(11, len(ev)//4))
    s = np.polyfit(np.log(k[sel]), np.log(ev[sel]), 1)[0]
    return (1.0/(abs(s)-1.0) if abs(s) > 1.0 else np.inf), s, W.shape[0]

def calib(d):
    m = np.array([0.95, 1.82, 2.76]); t = np.array([1., 2., 3.])
    if not np.isfinite(d): return np.inf
    if d > m[-1]:
        return float(t[-1] + (d-m[-1])*(t[-1]-t[-2])/(m[-1]-m[-2]))
    return float(np.interp(d, m, t))

def run(seed, pb, pc, mode):
    rng = np.random.default_rng(seed)
    H = np.zeros((NMAX, NMAX))
    n = 2; H[0,1] = H[1,0] = 1.0
    w = 0; traj = [0, 1]
    rho = solve_rho(H[:n,:n], LAM)
    out = []
    for ep in range(EPOCHS):
        C = 1 - np.exp(-LAM*rho[:,None]*H[:n,:n])
        Cs = 0.5*(C + C.T)
        for _ in range(EV):
            u = rng.random()
            if u < pb and n < NMAX:
                H[w, n] += 1.0; H[n, w] += 1.0
                w = n; n += 1
            elif u < pb + pc and len(traj) > LAG + 1:
                if mode == 'lag':
                    tgt = int(traj[-LAG])
                else:
                    tgt = int(rng.choice(traj[-LWIN:]))
                if tgt != w:
                    H[w, tgt] += 1.0; H[tgt, w] += 1.0
            else:
                m_ = Cs.shape[0]
                p = np.zeros(n)
                if w < m_: p[:m_] = Cs[w, :m_]
                p += 1e-9 * (H[w,:n] + H[:n,w])
                p[w] = 0.0
                ss = p.sum()
                if ss < 1e-12:
                    nb = np.where(H[w,:n] + H[:n,w] > 0)[0]; nb = nb[nb != w]
                    nxt = int(rng.choice(nb)) if len(nb) else w
                else:
                    nxt = int(rng.choice(n, p=p/ss))
                H[w, nxt] += 1.0
                w = nxt
            traj.append(w)
            if len(traj) > 4*LWIN: traj = traj[-2*LWIN:]
        H[:n,:n] *= (1.0-GAMMA)
        rho = solve_rho(H[:n,:n], LAM)
        if ep in (5, 11, 17):
            C = 1 - np.exp(-LAM*rho[:,None]*H[:n,:n])
            d, s, gc = dim_geodesic(0.5*(C+C.T))
            out.append((ep, n, gc, d, calib(d), s))
    return out

f = lambda x: f"{x:6.2f}" if np.isfinite(x) else "   inf"
print(f"lam={LAM} gamma={GAMMA} LAG={LAG}")
conds = [(0.3, 0.0, 'window', 12), (0.3, 0.1, 'lag', 12),
         (0.3, 0.1, 'lag', 6), (0.3, 0.1, 'lag', 25), (0.3, 0.2, 'lag', 12)]
for pb, pc, mode, lag in conds:
    globals()['LAG'] = lag
    vals = []
    for seed in (5, 6, 7):
        res = run(seed, pb, pc, mode)
        final = [dc for ep, n, gc, d, dc, s in res if np.isfinite(dc)]
        vals.append(np.mean(final) if final else np.inf)
    fv = ["%.2f" % v if np.isfinite(v) else "inf" for v in vals]
    fin = [v for v in vals if np.isfinite(v)]
    m = "%.2f +- %.2f" % (np.mean(fin), np.std(fin)) if len(fin) >= 2 else "n/a"
    print(f"pb={pb:4.2f} pc={pc:4.2f} {mode:6s} LAG={lag:2d}: seeds -> {fv}   mean d_cal = {m}")

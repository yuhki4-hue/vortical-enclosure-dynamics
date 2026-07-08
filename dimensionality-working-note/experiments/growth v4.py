"""v4: triadic closure reward (Vol.2's -beta*Phi term) added to the growth rule.

Registration probability: P(w -> j) ~ C[w,j] + bt*(C@C)[w,j] + eta
  (C@C)[w,j] = sum_k C[w,k]C[k,j]: degree to which registering w->j
  completes triangles -- the discrete gradient of the closure reward.
Decay (GammaC) and exploration floor retained. Geodesic instrument,
sparse calibration (5.7.2): measured 0.95/1.82/2.76 <-> true 1/2/3.
Control: bt=0 (equivalent to v3).
"""
import numpy as np
from scipy.sparse.csgraph import shortest_path

N = 300; LAM = 0.05; ETA = 1e-3; EPOCHS = 30; EV = 20_000; GAMMA = 0.2

def solve_rho(H, lam, iters=800):
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
    D = shortest_path(W, method='D', directed=False)
    fin = np.isfinite(D) & (D > 0)
    if fin.sum() < 100: return np.nan, 0.0
    med = np.median(D[fin])
    Dc = np.where(np.isfinite(D), D, D[np.isfinite(D)].max()*2)
    K = np.exp(-Dc/med)
    ev = np.linalg.eigvalsh(K)[::-1]
    ev = ev[ev > 1e-12*ev[0]]
    k = np.arange(1, len(ev)+1)
    sel = (k >= 5) & (k <= max(11, len(ev)//4))
    s = np.polyfit(np.log(k[sel]), np.log(ev[sel]), 1)[0]
    return (1.0/(abs(s)-1.0) if abs(s) > 1.0 else np.inf), s

def calib(d):
    m = np.array([0.95, 1.82, 2.76]); t = np.array([1., 2., 3.])
    if not np.isfinite(d): return np.inf
    if d > m[-1]:  # linear extrapolation beyond calibration
        return float(t[-1] + (d-m[-1])*(t[-1]-t[-2])/(m[-1]-m[-2]))
    return float(np.interp(d, m, t))

def run(seed, bt):
    rng = np.random.default_rng(seed)
    H = np.zeros((N, N)); i0, j0 = rng.integers(N, size=2); H[i0, j0] = 1.0
    w = int(i0); rho = solve_rho(H, LAM)
    out = []
    for ep in range(EPOCHS):
        C = 1 - np.exp(-LAM*rho[:,None]*H)
        Cs = 0.5*(C + C.T)
        P = Cs + bt*(Cs @ Cs) + ETA
        np.fill_diagonal(P, 0.0)
        P = P/P.sum(1, keepdims=True)
        for _ in range(EV):
            w2 = rng.choice(N, p=P[w]); H[w, w2] += 1.0; w = w2
        H *= (1.0-GAMMA)
        rho = solve_rho(H, LAM)
        if ep in (9, 19, 29):
            C = 1 - np.exp(-LAM*rho[:,None]*H)
            d, s = dim_geodesic(0.5*(C+C.T))
            out.append((ep, d, calib(d), s))
    return out

f = lambda x: f"{x:6.2f}" if np.isfinite(x) else "   inf"
for bt in (0.0, 1.0, 5.0, 20.0):
    for seed in (5, 6):
        res = run(seed, bt)
        line = "  ".join(f"ep{ep}: d_cal={f(dc)} (s={s:5.2f})" for ep, d, dc, s in res)
        print(f"bt={bt:5.1f} seed={seed}: {line}")

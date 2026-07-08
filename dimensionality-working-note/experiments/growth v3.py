"""v3: geodesic metric. d_ij = shortest path over weights -log S~ (correlations
multiply along paths). Re-validate instrument on sparse graphs of KNOWN d,
then measure the grown networks."""
import numpy as np
from scipy.sparse.csgraph import shortest_path

N = 300; LAM = 0.05; ETA = 1e-3; EPOCHS = 30; EV = 20_000

def solve_rho(H, lam, iters=800):
    rho = np.ones(H.shape[0])
    for _ in range(iters):
        rn = (1 - np.exp(-lam * rho[:, None] * H)).sum(1)
        if np.allclose(rn, rho, atol=1e-12): break
        rho = 0.5*rho + 0.5*rn
    return rho

def dim_from_D(D):
    med = np.median(D[np.isfinite(D) & (D > 0)])
    Dc = np.where(np.isfinite(D), D, D[np.isfinite(D)].max()*2)
    K = np.exp(-Dc/med)
    ev = np.linalg.eigvalsh(K)[::-1]
    ev = ev[ev > 1e-12*ev[0]]
    k = np.arange(1, len(ev)+1)
    sel = (k >= 5) & (k <= max(11, len(ev)//4))
    s = np.polyfit(np.log(k[sel]), np.log(ev[sel]), 1)[0]
    return (1.0/(abs(s)-1.0) if abs(s) > 1.0 else np.inf), s

def geodesic_D(S):
    Sc = np.clip(S, 1e-12, 1-1e-12)
    W = -np.log(Sc)
    np.fill_diagonal(W, 0.0)
    # sparsify: keep only meaningful links (S above tiny floor) for speed
    W[Sc < 1e-6] = 0.0   # treated as no direct edge
    return shortest_path(W, method='D', directed=False)

print("--- re-validation on sparse graphs of known dimension (geodesic) ---")
for d in (1, 2, 3):
    r = np.random.default_rng(d)
    X = r.uniform(0, 1, (400, d))
    Dfull = np.linalg.norm(X[:,None]-X[None,:], axis=-1)
    # kNN sparsification: keep 8 nearest neighbours only
    Wk = np.full_like(Dfull, 0.0)
    nn = np.argsort(Dfull, axis=1)[:, 1:9]
    for i in range(400): Wk[i, nn[i]] = Dfull[i, nn[i]]
    Wk = np.maximum(Wk, Wk.T)
    G = shortest_path(Wk, method='D', directed=False)
    dh, s = dim_from_D(G)
    print(f"  kNN graph true d={d}: d_raw={dh:6.2f} slope={s:6.2f}")

print("--- growth measurement with geodesic metric ---")
def run(seed, mode, gamma):
    rng = np.random.default_rng(seed)
    H = np.zeros((N, N)); i0, j0 = rng.integers(N, size=2); H[i0, j0] = 1.0
    w = int(i0); rho = solve_rho(H, LAM)
    snaps = {}
    for ep in range(EPOCHS):
        if mode == "walker":
            C = 1 - np.exp(-LAM*rho[:,None]*H)
            P = C + ETA; np.fill_diagonal(P, 0.0)
            P = P/P.sum(1, keepdims=True)
            for _ in range(EV):
                w2 = rng.choice(N, p=P[w]); H[w, w2] += 1.0; w = w2
        else:
            ii = rng.integers(N, size=EV); jj = rng.integers(N, size=EV)
            np.add.at(H, (ii, jj), 1.0)
        H *= (1.0-gamma)
        rho = solve_rho(H, LAM)
        if ep in (9, 19, 29):
            C = 1 - np.exp(-LAM*rho[:,None]*H)
            snaps[ep] = 0.5*(C+C.T)
    return snaps

cal_m = np.array([0.95, 1.99, 3.50]); cal_t = np.array([1., 2., 3.])
for gamma in (0.05, 0.2):
    for mode in ("walker", "control"):
        snaps = run(5, mode, gamma)
        for ep, S in snaps.items():
            D = geodesic_D(S)
            dh, s = dim_from_D(D)
            dc = np.inf if not np.isfinite(dh) else float(np.interp(dh, cal_m, cal_t))
            f = lambda x: f"{x:6.2f}" if np.isfinite(x) else "   inf"
            print(f"  gamma={gamma:4.2f} {mode:7s} ep={ep:2d}: d_raw={f(dh)} d_cal~{f(dc)} slope={s:6.2f}")

"""Route II v2 -- corrected estimators.

Estimator 1 (kernel power law): exponential kernel on a d-dim manifold is
  Matern nu=1/2; eigenvalues decay lam_k ~ k^{-(d+1)/d}.
  => d_hat = 1 / (|slope| - 1) from log lam vs log k.

Estimator 2 (spectral dimension, CDT-standard): build graph Laplacian with
  weights w_ij = S_ij, heat trace P(t) = (1/N) sum_k exp(-t mu_k) ~ t^{-d_s/2}
  in the scaling window => d_s = -2 dlogP/dlogt, read at the plateau.
"""
import numpy as np


def kernel_powerlaw_dim(S, kmin=5, frac=0.25):
    ev = np.linalg.eigvalsh(S)[::-1]
    ev = ev[ev > 1e-12 * ev[0]]
    k = np.arange(1, len(ev) + 1)
    kmax = max(kmin + 6, int(len(ev) * frac))
    sel = (k >= kmin) & (k <= kmax)
    s = np.polyfit(np.log(k[sel]), np.log(ev[sel]), 1)[0]
    return 1.0 / (abs(s) - 1.0) if abs(s) > 1.0 else np.inf, s


def spectral_dim_profile(S, nt=60):
    """d_s(t) profile from Laplacian heat trace; return (t, d_s(t))."""
    W = S.copy()
    np.fill_diagonal(W, 0.0)
    deg = W.sum(1)
    Lap = np.diag(deg) - W
    mu = np.linalg.eigvalsh(Lap)
    mu = np.clip(mu, 0, None)
    mu_pos = mu[mu > 1e-12]
    ts = np.geomspace(0.1 / mu_pos.max(), 10.0 / mu_pos[0], nt)
    P = np.array([np.exp(-t * mu).mean() for t in ts])
    lt, lP = np.log(ts), np.log(P)
    ds = -2 * np.gradient(lP, lt)
    return ts, ds


def ds_plateau(ts, ds):
    """Read d_s at the flattest window of the profile."""
    n = len(ds)
    w = max(5, n // 8)
    best, val = None, np.inf
    for i in range(n - w):
        sl = ds[i:i + w]
        if sl.std() < val and sl.mean() > 0.05:
            val, best = sl.std(), sl.mean()
    return best


def measure(tag, S):
    d_pl, slope = kernel_powerlaw_dim(S)
    ts, ds = spectral_dim_profile(S)
    d_s = ds_plateau(ts, ds)
    print(f"{tag:46s} powerlaw_d={d_pl:6.2f} (slope {slope:6.2f})   d_s={d_s:6.2f}")
    return d_pl, d_s


print("=" * 84)
print("Stage A: calibration, point clouds of KNOWN d (N=600, kernel exp(-D/med))")
print("=" * 84)
N = 600
for d in (1, 2, 3, 4):
    for seed in (1, 2):
        r = np.random.default_rng(seed)
        X = r.uniform(0, 1, (N, d))
        D = np.linalg.norm(X[:, None] - X[None, :], axis=-1)
        D /= np.median(D[D > 0])
        measure(f"  true d={d} seed={seed}:", np.exp(-D))

print()
print("=" * 84)
print("Stage B: validation, 2D torus lattice 24x24 (expect ~2)")
print("=" * 84)
L = 24
idx = np.arange(L)
dx = np.minimum(np.abs(idx[:, None] - idx[None, :]), L - np.abs(idx[:, None] - idx[None, :]))
D = (dx[:, None, :, None] + dx[None, :, None, :]).reshape(L * L, L * L).astype(float)
D /= np.median(D[D > 0])
measure("  2D torus:", np.exp(-D))

# 3D torus as well, smaller
L3 = 9
dx3 = np.minimum(np.abs(np.arange(L3)[:, None] - np.arange(L3)[None, :]),
                 L3 - np.abs(np.arange(L3)[:, None] - np.arange(L3)[None, :]))
D3 = (dx3[:, None, None, :, None, None] + dx3[None, :, None, None, :, None]
      + dx3[None, None, :, None, None, :]).reshape(L3**3, L3**3).astype(float)
D3 /= np.median(D3[D3 > 0])
measure("  3D torus 9x9x9 (expect ~3):", np.exp(-D3))

print()
print("=" * 84)
print("Stage C: intrinsic VED network (fixed point of rho, C=1-exp(-lam rho H))")
print("=" * 84)


def solve_fixed_point(H, lam, iters=600):
    rho = np.ones(H.shape[0])
    for _ in range(iters):
        rho_new = (1 - np.exp(-lam * rho[:, None] * H)).sum(1)
        if np.allclose(rho_new, rho, atol=1e-12):
            break
        rho = 0.5 * rho + 0.5 * rho_new
    return rho


def ved_S(H, lam):
    rho = solve_fixed_point(H, lam)
    if rho.max() < 1e-8:
        return None
    C = 1 - np.exp(-lam * rho[:, None] * H)
    Ssym = 0.5 * (C + C.T)
    Sc = np.clip(Ssym, 1e-12, 1 - 1e-12)
    Dv = -np.log(Sc)
    np.fill_diagonal(Dv, 0.0)
    Dv /= np.median(Dv[Dv > 0])
    return np.exp(-Dv)


Nc = 500
r = np.random.default_rng(11)
H = r.uniform(0, 1, (Nc, Nc)); H = np.triu(H, 1); H = H + H.T
S = ved_S(H, 0.02)
if S is not None:
    measure("  C1 iid H, lam=0.02:", S)
S = ved_S(H, 0.05)
if S is not None:
    measure("  C1 iid H, lam=0.05:", S)

H3s = (r.uniform(0, 1, (Nc, Nc)) < 12 / Nc) * r.uniform(0.5, 1.5, (Nc, Nc))
H3s = np.triu(H3s, 1); H3s = H3s + H3s.T
S = ved_S(H3s, 0.3)
if S is not None:
    measure("  C3 sparse H (~12 nbrs), lam=0.3:", S)

# C4: H carrying latent 3d geometry -- does the fixed point PRESERVE d=3?
r4 = np.random.default_rng(21)
X = r4.uniform(0, 1, (Nc, 3))
Dg = np.linalg.norm(X[:, None] - X[None, :], axis=-1)
Dg /= np.median(Dg[Dg > 0])
Hg = np.exp(-2 * Dg); np.fill_diagonal(Hg, 0)
S = ved_S(Hg, 0.05)
if S is not None:
    measure("  C4 H with latent 3d geometry, lam=0.05:", S)

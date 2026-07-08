"""Route II: effective rank / spectral dimension of S-tilde.

Stage A (calibration): point clouds of known dimension d=1..4, kernel
  S_ij = exp(-d_ij) -> does the estimator recover d?
Stage B (validation): 2D lattice config (Phase-4 style geometry) -> expect ~2.
Stage C (application): intrinsic VED network. H_ij random ensembles,
  solve the fixed point rho_i = sum_j [1 - exp(-lam rho_i H_ij)],
  C_ij = 1 - exp(-lam rho_i H_ij), S = (C+C^T)/2, measure spectrum.

Estimators:
  1. Weyl slope: for heat-kernel-like S with eigenvalues lam_k,
     mu_k := -log(lam_k / lam_0) ~ k^(2/d)  =>  slope of log(mu_k) vs log(k) = 2/d
  2. participation ratio PR = (sum lam)^2 / sum lam^2  (effective # of modes)
  3. spectral entropy dim: exp(H) with H = -sum p log p, p = lam / sum lam
"""
import numpy as np

rng_global = np.random.default_rng(7)


def weyl_dim(evals, kmin=4, kmax=None):
    """Estimate d from eigenvalue decay via Weyl scaling mu_k ~ k^(2/d)."""
    lam = np.sort(evals)[::-1]
    lam = lam[lam > 1e-13 * lam[0]]
    mu = -np.log(lam / lam[0])
    mu = mu[mu > 1e-10]
    k = np.arange(1, len(mu) + 1)
    if kmax is None:
        kmax = len(mu) // 2          # avoid discreteness tail
    sel = (k >= kmin) & (k <= kmax)
    if sel.sum() < 4:
        return np.nan
    slope = np.polyfit(np.log(k[sel]), np.log(mu[sel]), 1)[0]
    return 2.0 / slope


def participation_ratio(evals):
    lam = np.clip(evals, 0, None)
    return (lam.sum() ** 2) / (lam ** 2).sum()


def spectral_entropy_modes(evals):
    lam = np.clip(evals, 1e-300, None)
    p = lam / lam.sum()
    return float(np.exp(-(p * np.log(p)).sum()))


def report(tag, S):
    ev = np.linalg.eigvalsh(S)[::-1]
    d_w = weyl_dim(ev)
    pr = participation_ratio(ev)
    se = spectral_entropy_modes(ev)
    print(f"{tag:44s} weyl_d={d_w:6.3f}  PR={pr:8.1f}  entropy_modes={se:8.1f}")
    return d_w, pr, se


# ---------------------------------------------------------------- Stage A
print("=" * 78)
print("Stage A: calibration on point clouds of KNOWN dimension (N=600)")
print("  S_ij = exp(-|x_i - x_j|), rescaled so median distance = 1")
print("=" * 78)
N = 600
for d in (1, 2, 3, 4):
    ds = []
    for seed in (1, 2, 3):
        r = np.random.default_rng(seed)
        X = r.uniform(0, 1, size=(N, d))
        D = np.linalg.norm(X[:, None, :] - X[None, :, :], axis=-1)
        D /= np.median(D[D > 0])
        S = np.exp(-D)
        ev = np.linalg.eigvalsh(S)[::-1]
        ds.append(weyl_dim(ev))
    ds = np.array(ds)
    print(f"  true d={d}:  weyl_d = {ds.mean():.3f} +- {ds.std():.3f}   (seeds 1-3)")

# ---------------------------------------------------------------- Stage B
print()
print("=" * 78)
print("Stage B: validation on 2D periodic lattice (Phase-4 geometry, 24x24)")
print("  d_ij = torus graph distance, S = exp(-d/median)")
print("=" * 78)
L = 24
idx = np.arange(L)
dx = np.minimum(np.abs(idx[:, None] - idx[None, :]), L - np.abs(idx[:, None] - idx[None, :]))
D = (dx[:, None, :, None] + dx[None, :, None, :]).reshape(L * L, L * L).astype(float)
D /= np.median(D[D > 0])
report("  2D torus lattice (expect ~2):", np.exp(-D))

# ---------------------------------------------------------------- Stage C
print()
print("=" * 78)
print("Stage C: intrinsic VED network from the fixed point of")
print("  rho_i = sum_j [1 - exp(-lam rho_i H_ij)],  C_ij = 1 - exp(-lam rho_i H_ij)")
print("  S~ from  d_ij = -log S_ij  (S = sym part of C), then kernel exp(-d)")
print("=" * 78)


def solve_fixed_point(H, lam, iters=400):
    N = H.shape[0]
    rho = np.ones(N)
    for _ in range(iters):
        rho_new = (1 - np.exp(-lam * rho[:, None] * H)).sum(axis=1)
        if np.allclose(rho_new, rho, atol=1e-12):
            break
        rho = 0.5 * rho + 0.5 * rho_new
    return rho


def ved_network_spectrum(H, lam, tag):
    rho = solve_fixed_point(H, lam)
    if rho.max() < 1e-8:
        print(f"{tag:44s} collapsed to rho=0 (no structure at this lam)")
        return
    C = 1 - np.exp(-lam * rho[:, None] * H)
    Ssym = 0.5 * (C + C.T)
    # distance from the symmetric log: d_ij = -log S~ (guard zeros)
    Sc = np.clip(Ssym, 1e-12, 1 - 1e-12)
    Dv = -np.log(Sc)
    np.fill_diagonal(Dv, 0.0)
    Dv /= np.median(Dv[Dv > 0])
    report(tag, np.exp(-Dv))


Nc = 500
r = np.random.default_rng(11)

# C1: unstructured H -- iid uniform (no built-in geometry at all)
H = r.uniform(0, 1, (Nc, Nc)); H = np.triu(H, 1); H = H + H.T
ved_network_spectrum(H, lam=0.02, tag="  C1 iid H (no geometry), lam=0.02:")
ved_network_spectrum(H, lam=0.05, tag="  C1 iid H (no geometry), lam=0.05:")

# C2: H with mild multiplicative node heterogeneity (still no geometry)
w = r.lognormal(0, 0.5, Nc)
H2 = np.outer(w, w) * (r.uniform(0, 1, (Nc, Nc)))
H2 = np.triu(H2, 1); H2 = H2 + H2.T
ved_network_spectrum(H2, lam=0.02, tag="  C2 heterogeneous H, lam=0.02:")

# C3: sparse H (each node interacts with ~12 random others)
H3 = (r.uniform(0, 1, (Nc, Nc)) < 12 / Nc).astype(float) * r.uniform(0.5, 1.5, (Nc, Nc))
H3 = np.triu(H3, 1); H3 = H3 + H3.T
ved_network_spectrum(H3, lam=0.3, tag="  C3 sparse random H (~12 nbrs), lam=0.3:")

print()
print("interpretation guide: weyl_d is the spectral-dimension estimate;")
print("PR / entropy_modes are raw effective mode counts (scale with N for")
print("finite-d geometry, stay O(1) or O(N) pathologically otherwise).")

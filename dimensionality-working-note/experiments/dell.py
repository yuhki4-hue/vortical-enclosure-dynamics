"""d(ell) scale-dependent dimension: local slope of log N(r) vs log r.
Calibration first (5.59.3): known two-layer slab (2D sheets stacked thin in 3D,
d_local=2 at small ell, d_block=3 at large ell) must show TWO plateaus;
pure 2D lattice must show ONE. Only then trust it on VED windows.
"""
import numpy as np
from scipy.sparse.csgraph import shortest_path

def d_of_ell(D, n_ell=30, halfwin=0.35):
    """Return (ell_centers, d(ell)) as local log-log slope of ball counts."""
    fin = np.isfinite(D) & (D > 0)
    nn = []
    for i in range(D.shape[0]):
        v = D[i][fin[i]]
        if v.size: nn.append(v.min())
    if not nn: return None, None
    unit = np.median(nn)
    rmax = np.percentile(D[fin], 90)
    rs = np.geomspace(unit, rmax, 60)
    counts = np.array([((D <= r) & np.isfinite(D)).sum(1).mean() for r in rs])
    lr, lc = np.log(rs), np.log(counts)
    # local slope via sliding log-window regression
    ells = np.geomspace(rs[2], rs[-3], n_ell)
    dvals = []
    for e in ells:
        le = np.log(e)
        sel = np.abs(lr - le) < halfwin
        if sel.sum() >= 4 and (counts[sel] > 3).any() and (counts[sel] < 0.6*D.shape[0]).all():
            dvals.append(np.polyfit(lr[sel], lc[sel], 1)[0])
        else:
            dvals.append(np.nan)
    return ells, np.array(dvals)

def knn_graph(X, k=8):
    D = np.linalg.norm(X[:,None]-X[None,:], axis=-1)
    W = np.zeros_like(D); nn = np.argsort(D, axis=1)[:,1:k+1]
    for i in range(len(X)): W[i, nn[i]] = D[i, nn[i]]
    return shortest_path(np.maximum(W, W.T), directed=False)

print("=== CALIBRATION 5.59.3 ===")
r = np.random.default_rng(1)
# pure 2D lattice-like point cloud -> expect single plateau ~2 (raw ball ~1.7)
X2 = r.uniform(0, 1, (800, 2))
e, d = d_of_ell(knn_graph(X2))
mid = d[np.isfinite(d)]
print(f"pure 2D:   d(ell) range [{np.nanmin(d):.2f}, {np.nanmax(d):.2f}]  "
      f"profile: {np.round(d[::5],2)}")

# two-layer slab: 2D sheets (extent 1x1) stacked in a thin 3rd dim (extent 0.15)
# small ell sees within-sheet (2D), large ell sees across stack (3D)
z = r.uniform(0, 0.15, 900)
X3 = np.column_stack([r.uniform(0,1,900), r.uniform(0,1,900), z])
e2, d2 = d_of_ell(knn_graph(X3))
print(f"slab 2/3:  d(ell) range [{np.nanmin(d2):.2f}, {np.nanmax(d2):.2f}]  "
      f"profile: {np.round(d2[::5],2)}")
print("  -> two-plateau detectable?" ,
      "YES" if (np.nanmax(d2) - np.nanmin(d2)) > 0.4 else "NO (instrument blind)")

# pure 3D control
X3f = r.uniform(0, 1, (900, 3))
e3, d3 = d_of_ell(knn_graph(X3f))
print(f"pure 3D:   d(ell) range [{np.nanmin(d3):.2f}, {np.nanmax(d3):.2f}]  "
      f"profile: {np.round(d3[::5],2)}")

"""Ball-growth dimension estimator + validation on known-d sparse graphs.
N_i(r) = #nodes within geodesic distance r of node i.
Fit log <N(r)> vs log r over the scaling window r in [r_min, r_half],
where r_half = radius containing half the component (avoids saturation).
"""
import numpy as np
from scipy.sparse.csgraph import shortest_path

def ball_dimension(D):
    """D: geodesic distance matrix (finite entries only used)."""
    n = D.shape[0]
    fin = np.isfinite(D)
    # hop-normalize: use median nearest-neighbor distance as unit
    nn = np.array([np.min(D[i][fin[i] & (D[i] > 0)]) for i in range(n)])
    unit = np.median(nn)
    rs = unit * np.arange(1, 40)
    counts = []
    for r in rs:
        c = ((D <= r) & fin).sum(1).mean()
        counts.append(c)
    counts = np.array(counts)
    # scaling window: from N~5 to N~n/2 (avoid discreteness and saturation)
    sel = (counts > 5) & (counts < 0.5 * n)
    if sel.sum() < 4:
        return np.nan
    lr, lc = np.log(rs[sel]), np.log(counts[sel])
    return float(np.polyfit(lr, lc, 1)[0])

if __name__ == "__main__":
    print("validation: kNN graphs (k=8, N=500) of known dimension")
    for d in (1, 2, 3):
        vals = []
        for seed in (1, 2, 3):
            r = np.random.default_rng(seed)
            X = r.uniform(0, 1, (500, d))
            Df = np.linalg.norm(X[:,None]-X[None,:], axis=-1)
            Wk = np.zeros_like(Df)
            nn = np.argsort(Df, axis=1)[:, 1:9]
            for i in range(500): Wk[i, nn[i]] = Df[i, nn[i]]
            Wk = np.maximum(Wk, Wk.T)
            G = shortest_path(Wk, method='D', directed=False)
            vals.append(ball_dimension(G))
        v = np.array(vals)
        print(f"  true d={d}: ball_d = {v.mean():.3f} +- {v.std():.3f}")
    # lattice checks
    for L, dd in ((40, 2),):
        idx = np.arange(L)
        dx = np.minimum(np.abs(idx[:,None]-idx[None,:]), L-np.abs(idx[:,None]-idx[None,:]))
        D2 = (dx[:,None,:,None]+dx[None,:,None,:]).reshape(L*L, L*L).astype(float)
        print(f"  2D torus {L}x{L}: ball_d = {ball_dimension(D2):.3f}")

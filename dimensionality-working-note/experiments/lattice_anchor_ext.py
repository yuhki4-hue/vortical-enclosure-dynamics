"""lattice_anchor_ext.py -- d_cal anchor extension to 4D (proposal in §2.2.2).

The d_cal instrument maps a measured ball-scaling slope b to a calibrated
dimension via anchor slopes m measured on reference lattices:
  panel():    m = [0.91, 1.70, 2.20]          t = [1, 2, 3]
  dual_dims： m = [0.912, 1.700, 2.204, 2.526] t = [1, 2, 3, 4]
Values above the last anchor are EXTRAPOLATED. v24.3 directed robust-BSW
readings (median 3.43) sit 90% in that region -> 4D anchor required.

This script regenerates the anchors with the SAME measurement code path as
`panel()` in growth_v24_3_rules.py / `growth v24 betti.py`:
  - all-pairs shortest path on the support graph
  - unit = median nearest-neighbour distance
  - radii rs = unit * arange(1, 40)
  - count window: counts > 5 AND counts < 0.5*n
  - slope = polyfit(log rs, log counts) on the window

CRITICAL: anchors are finite-size quantities (0.91 != 1 etc. comes from the
window + boundary). They must be measured at sizes MATCHED to the system
size at the BSW snapshot being calibrated (v24.3 directed robust BSW:
V ~ 500-900). The script therefore emits slope-vs-N tables per dimension,
not a single number.

Periodic boundaries are OFF by default (the grown graphs have boundaries);
--periodic available for sensitivity checking. --jitter adds lognormal
edge-weight noise to probe robustness of the anchor to non-unit weights
(the model measures on W=-log S, which is not unit-weight).

USAGE:
  python lattice_anchor_ext.py                # default size ladder
  python lattice_anchor_ext.py --sizes 350,700,1300,2400
  python lattice_anchor_ext.py --jitter 0.3 --periodic
Output: anchor_table.tsv (dim, side, N, slope) + suggested m-arrays.
"""
import argparse
import itertools

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import shortest_path


def lattice_graph(dim, side, periodic=False):
    """Hypercubic lattice Z^dim of given side. Returns (N, edges)."""
    shape = (side,) * dim
    N = side ** dim
    idx = np.arange(N).reshape(shape)
    edges = []
    for ax in range(dim):
        a = idx
        b = np.roll(idx, -1, axis=ax)
        if not periodic:
            sl = [slice(None)] * dim
            sl[ax] = slice(0, side - 1)
            a = idx[tuple(sl)]
            b = np.roll(idx, -1, axis=ax)[tuple(sl)]
        edges.append(np.stack([a.ravel(), b.ravel()], 1))
    return N, np.concatenate(edges, 0)


def measure_slope(N, edges, rng=None, jitter=0.0, wpool=None):
    """Exact replication of the panel() ball-scaling measurement.
    wpool: empirical weight sample (1D array); edge weights are drawn from
    it with replacement (overrides jitter)."""
    w = np.ones(len(edges))
    if wpool is not None:
        w = rng.choice(wpool, size=len(edges), replace=True)
    elif jitter > 0:
        w = np.exp(rng.normal(0.0, jitter, len(edges)))
    A = coo_matrix((w, (edges[:, 0], edges[:, 1])), shape=(N, N))
    A = A + A.T
    D = shortest_path(A, method="D", directed=False,
                      unweighted=(wpool is None and jitter == 0.0))
    fin = np.isfinite(D) & (D > 0)
    nn = []
    for i in range(N):
        v = D[i][fin[i]]
        if v.size:
            nn.append(v.min())
    unit = np.median(nn)
    rs = unit * np.arange(1, 40)
    counts = np.array([((D <= r) & np.isfinite(D)).sum(1).mean()
                       for r in rs])
    sel = (counts > 5) & (counts < 0.5 * N)
    if sel.sum() < 4:
        return np.nan, int(sel.sum())
    b = float(np.polyfit(np.log(rs[sel]), np.log(counts[sel]), 1)[0])
    return b, int(sel.sum())


def sides_for(dim, targets):
    """Lattice sides whose N is closest to each target size."""
    out = []
    for tgt in targets:
        s = max(2, int(round(tgt ** (1.0 / dim))))
        best = min((s - 1, s, s + 1, s + 2),
                   key=lambda x: abs(x ** dim - tgt) if x >= 2 else 1e18)
        if (best, best ** dim) not in out:
            out.append((best, best ** dim))
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sizes", default="350,700,1300,2400",
                   help="target N ladder (match to V at the BSW snapshots "
                        "being calibrated)")
    p.add_argument("--dims", default="1,2,3,4")
    p.add_argument("--periodic", action="store_true")
    p.add_argument("--jitter", type=float, default=0.0,
                   help="lognormal sigma on edge weights (0 = unit weights)")
    p.add_argument("--seeds", default="0",
                   help="rng seeds for jitter/weight replicates (csv)")
    p.add_argument("--weights-from", default=None,
                   help="file with one empirical edge weight per line "
                        "(e.g. -log(S) values exported from BSW-window "
                        "snapshots); overrides --jitter")
    p.add_argument("-o", "--out", default="anchor_table.tsv")
    args = p.parse_args()

    targets = [int(x) for x in args.sizes.split(",")]
    dims = [int(x) for x in args.dims.split(",")]
    seeds = [int(x) for x in args.seeds.split(",")]

    wpool = None
    if args.weights_from:
        wpool = np.loadtxt(args.weights_from)
        wpool = wpool[np.isfinite(wpool) & (wpool > 0)]
        print(f"# empirical weight pool: n={wpool.size} "
              f"median={np.median(wpool):.3g} cv={wpool.std()/wpool.mean():.2f}")

    rows = []
    for dim in dims:
        for side, N in sides_for(dim, targets):
            slopes = []
            stochastic = args.jitter > 0 or wpool is not None
            for sd in (seeds if stochastic else [0]):
                rng = np.random.default_rng(sd)
                Nn, edges = lattice_graph(dim, side, args.periodic)
                b, npts = measure_slope(Nn, edges, rng, args.jitter, wpool)
                slopes.append(b)
            b_med = float(np.nanmedian(slopes))
            b_sd = float(np.nanstd(slopes)) if len(slopes) > 1 else 0.0
            rows.append((dim, side, N, b_med, b_sd, npts))
            print(f"dim={dim} side={side} N={N:5d} slope={b_med:.3f}"
                  + (f" +-{b_sd:.3f}" if len(slopes) > 1 else "")
                  + f" (npts={npts})")

    with open(args.out, "w") as f:
        f.write("dim\tside\tN\tslope\tslope_sd\tnpts\n")
        for r in rows:
            f.write("\t".join(str(x) for x in r) + "\n")
    print(f"-> {args.out}")

    # suggested m-array per target size (nearest N per dim)
    print("\n# suggested anchor arrays (use the row matching the V of the "
          "snapshots you are recalibrating):")
    for tgt in targets:
        ms = []
        for dim in dims:
            cand = [r for r in rows if r[0] == dim]
            r = min(cand, key=lambda r: abs(r[2] - tgt))
            ms.append(r[3])
        print(f"N~{tgt}: m = np.array({[round(m, 3) for m in ms]}); "
              f"t = np.array({[float(d) for d in dims]})")


if __name__ == "__main__":
    main()

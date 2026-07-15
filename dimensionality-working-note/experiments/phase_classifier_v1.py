"""phase_classifier_v1.py -- §12-2b: local phase classifier (pre-registered §5.5.2).

Replaces the global-V-peak growth/contraction split with a local,
hysteresis-based (Schmitt trigger) classifier on smoothed dV/dt, plus a
second tier (shedding/consolidation) on smoothed dh/dt inside contraction.

INPUT: TSV with header. Required column: epoch, V. Optional: b1H, b1S,
label (METR/SW/FRAG/SAT/...). Column names configurable via CLI.
One row per snapshot, one file per (seed, run).

PARAMETERIZATION (pre-registration): window width and epsilon are NOT bare
epoch numbers. Both are ratios of the intrinsic scale tau_edge
(median edge lifetime in epochs; directed ~250, symmetric ~163; pass via
--tau-edge).
  smoothing window (epochs) = window_ratio * tau_edge
  eps_V  = eps_ratio * mean(V) / tau_edge      [units: nodes/epoch]
  eps_h  = eps_ratio * 0.25   / tau_edge      [h in [0,1]; 0.25 ~ observed
                                               U-dip amplitude 0.7->0.5]
The eps_h scale constant (0.25) is itself a measured quantity (v24.2e
h U-shape); it is declared here, not tuned per run.

VALIDATION (mandatory, §5.5.2): on mechanically selected unimodal runs, the
new classifier must reproduce the same-run old classifier results and the
h U-shape ordering shedding->consolidation. Historical constants such as
growth occupancy ~21.5% and contraction ~73.1% are run-length-dependent
examples, not frozen targets. Run with --scan to sweep (window_ratio,
eps_ratio) and report the reproducing region; the midpoint of that region
becomes the standard setting.

USAGE:
  python phase_classifier_v1.py run.tsv --tau-edge 250 \
      --window-ratio 0.2 --eps-ratio 0.5 -o run_phases.tsv
  python phase_classifier_v1.py run1.tsv run2.tsv ... --tau-edge 250 --scan
"""
import argparse
import sys

import numpy as np


# ----------------------------------------------------------------------
def load_tsv(path, col_epoch, col_v, col_b1h, col_b1s, col_label):
    with open(path) as f:
        header = f.readline().rstrip("\n").split("\t")
    idx = {name: k for k, name in enumerate(header)}
    for req in (col_epoch, col_v):
        if req not in idx:
            sys.exit(f"{path}: required column '{req}' not in header {header}")
    rows = []
    with open(path) as f:
        next(f)
        for line in f:
            rows.append(line.rstrip("\n").split("\t"))
    ep = np.array([float(r[idx[col_epoch]]) for r in rows])
    V = np.array([float(r[idx[col_v]]) for r in rows])
    b1h = b1s = labels = None
    if col_b1h in idx and col_b1s in idx:
        b1h = np.array([float(r[idx[col_b1h]]) for r in rows])
        b1s = np.array([float(r[idx[col_b1s]]) for r in rows])
    if col_label in idx:
        labels = np.array([r[idx[col_label]] for r in rows])
    return ep, V, b1h, b1s, labels


def smooth(x, w_snaps):
    """Centered moving average, window w_snaps (forced odd, >=3)."""
    w = max(3, int(round(w_snaps)))
    if w % 2 == 0:
        w += 1
    pad = w // 2
    xp = np.pad(x, pad, mode="edge")
    ker = np.ones(w) / w
    return np.convolve(xp, ker, mode="valid")


def schmitt(deriv, eps):
    """Hysteresis two-state classifier. +1 growth, -1 contraction.
    Transition to growth on deriv > +eps, to contraction on deriv < -eps,
    hold previous state inside the dead band. Initial state from first
    excursion outside the band (before that: 0 = undecided, back-filled)."""
    state = np.zeros(len(deriv), dtype=int)
    cur = 0
    for k, d in enumerate(deriv):
        if d > eps:
            cur = +1
        elif d < -eps:
            cur = -1
        state[k] = cur
    # back-fill leading undecided with first decided state
    nz = np.nonzero(state)[0]
    if nz.size:
        state[: nz[0]] = state[nz[0]]
    return state


def classify(ep, V, b1h, b1s, tau_edge, window_ratio, eps_ratio):
    snap_dt = float(np.median(np.diff(ep)))
    w_snaps = (window_ratio * tau_edge) / snap_dt
    Vs = smooth(V, w_snaps)
    dV = np.gradient(Vs, ep)
    eps_v = eps_ratio * float(np.mean(V)) / tau_edge
    phase = schmitt(dV, eps_v)  # +1 growth / -1 contraction

    sub = np.array(["-"] * len(ep), dtype=object)
    if b1h is not None:
        h = np.divide(b1s, np.maximum(b1h, 1e-12))
        hs = smooth(h, w_snaps)
        dh = np.gradient(hs, ep)
        eps_h = eps_ratio * 0.25 / tau_edge
        hstate = schmitt(dh, eps_h)  # +1 h rising / -1 h falling
        # inside contraction: h falling -> shedding, h rising -> consolidation
        for k in range(len(ep)):
            if phase[k] == -1:
                sub[k] = ("consolidation" if hstate[k] == +1
                          else "shedding" if hstate[k] == -1 else "flat")
    return phase, sub, dict(w_snaps=w_snaps, eps_v=eps_v, snap_dt=snap_dt)


def old_classifier(V):
    """Baseline: global V peak splits the run into growth then contraction."""
    peak = int(np.argmax(V))
    phase = np.full(len(V), -1)
    phase[: peak + 1] = +1
    return phase


def occupancy(phase, labels):
    """BSW occupancy (label==METR) per phase. Returns (growth_occ, contr_occ)."""
    if labels is None:
        return np.nan, np.nan
    metr = labels == "METR"
    g = phase == +1
    c = phase == -1
    og = metr[g].mean() if g.sum() else np.nan
    oc = metr[c].mean() if c.sum() else np.nan
    return og, oc


# ----------------------------------------------------------------------
def main():
    p = argparse.ArgumentParser()
    p.add_argument("tsv", nargs="+")
    p.add_argument("--tau-edge", type=float, required=True,
                   help="median edge lifetime in epochs (intrinsic scale)")
    p.add_argument("--window-ratio", type=float, default=0.2)
    p.add_argument("--eps-ratio", type=float, default=0.5)
    p.add_argument("--scan", action="store_true",
                   help="sensitivity scan over (window_ratio, eps_ratio)")
    p.add_argument("--col-epoch", default="epoch")
    p.add_argument("--col-v", default="V")
    p.add_argument("--col-b1h", default="b1H")
    p.add_argument("--col-b1s", default="b1S")
    p.add_argument("--col-label", default="label")
    p.add_argument("-o", "--out", default=None,
                   help="output TSV (single-file mode)")
    args = p.parse_args()

    runs = [load_tsv(f, args.col_epoch, args.col_v, args.col_b1h,
                     args.col_b1s, args.col_label) for f in args.tsv]

    if args.scan:
        # ADJUDICATED VALIDATION (reading B, 2026-07-13): the target is
        # same-run agreement with the old classifier on unimodal runs,
        # NOT the historical constants 21.5/73.1 (those were run-length-
        # dependent examples; the old classifier itself violates them on
        # 1500ep logs). Criteria, locked before this rescan:
        #  (0) unimodal subset, mechanical: V smoothed with the LARGEST
        #      window in the grid has exactly one maximum above 50% of
        #      the global max
        #  (1) per-run |new_occ - old_occ| <= 0.15 for growth AND contr
        #  (2) parsimony: exactly 1 growth->contraction switch per
        #      unimodal run
        #  (3) U-shape: h minimum lies inside contraction; shedding
        #      precedes consolidation
        # A grid point reproduces iff ALL unimodal runs pass 1-3.
        wgrid = [0.1, 0.2, 0.3, 0.5]
        egrid = [0.1, 0.25, 0.5, 1.0]
        wmax = max(wgrid)
        uni = []
        print("# unimodal subset (mechanical, smoothing = largest grid "
              "window):")
        for f, (ep, V, b1h, b1s, lab) in zip(args.tsv, runs):
            snap_dt = float(np.median(np.diff(ep)))
            Vs = smooth(V, (wmax * args.tau_edge) / snap_dt)
            thr = 0.5 * Vs.max()
            above = Vs > thr
            # count local maxima of Vs that are above thr
            nmax = 0
            for k in range(1, len(Vs) - 1):
                if above[k] and Vs[k] >= Vs[k - 1] and Vs[k] > Vs[k + 1]:
                    nmax += 1
            is_uni = (nmax == 1)
            og, oc = occupancy(old_classifier(V), lab)
            print(f"#   {f}: n_major_maxima={nmax} unimodal={is_uni} "
                  f"old growth_occ={og:.3f} contr_occ={oc:.3f}")
            if is_uni:
                uni.append((f, ep, V, b1h, b1s, lab, og, oc))
        if not uni:
            print("# no unimodal runs in input; cannot calibrate")
            return
        print(f"# calibrating on {len(uni)} unimodal run(s)")
        print("window_ratio\teps_ratio\tn_pass_occ\tn_pass_switch"
              "\tn_pass_ushape\treproduces")
        for wr in wgrid:
            for er in egrid:
                p_occ = p_sw = p_u = 0
                for f, ep, V, b1h, b1s, lab, og, oc in uni:
                    phase, sub, meta = classify(ep, V, b1h, b1s,
                                                args.tau_edge, wr, er)
                    ng, nc = occupancy(phase, lab)
                    ok_occ = (np.isfinite(ng) and np.isfinite(nc)
                              and abs(ng - og) <= 0.15
                              and abs(nc - oc) <= 0.15)
                    d = np.diff(phase)
                    ok_sw = int((d != 0).sum()) == 1 and (d != 0).any() \
                        and d[d != 0][0] == -2  # single growth->contr
                    ok_u = False
                    if b1h is not None:
                        h = np.divide(b1s, np.maximum(b1h, 1e-12))
                        kmin = int(np.argmin(smooth(h, meta["w_snaps"])))
                        in_contr = phase[kmin] == -1
                        subs = [s for s in sub if s in ("shedding",
                                                        "consolidation")]
                        order = ("shedding" in subs and "consolidation"
                                 in subs and subs.index("shedding")
                                 < subs.index("consolidation"))
                        ok_u = in_contr and order
                    p_occ += ok_occ; p_sw += ok_sw; p_u += ok_u
                n = len(uni)
                rep = "YES" if p_occ == n and p_sw == n and p_u == n \
                    else "no"
                print(f"{wr}\t{er}\t{p_occ}/{n}\t{p_sw}/{n}"
                      f"\t{p_u}/{n}\t{rep}")
        return

    # single-setting mode
    for f, (ep, V, b1h, b1s, lab) in zip(args.tsv, runs):
        phase, sub, meta = classify(ep, V, b1h, b1s, args.tau_edge,
                                    args.window_ratio, args.eps_ratio)
        og, oc = occupancy(phase, lab)
        oog, ooc = occupancy(old_classifier(V), lab)
        nswitch = int((np.diff(phase) != 0).sum())
        print(f"{f}: w_snaps={meta['w_snaps']:.1f} eps_v={meta['eps_v']:.4g} "
              f"switches={nswitch}")
        print(f"  new: growth_occ={og:.3f} contr_occ={oc:.3f}   "
              f"old: growth_occ={oog:.3f} contr_occ={ooc:.3f}")
        out = args.out if (args.out and len(args.tsv) == 1) else \
            f.rsplit(".", 1)[0] + "_phases.tsv"
        with open(out, "w") as fo:
            fo.write("epoch\tV\tphase\tsubphase\tlabel\n")
            for k in range(len(ep)):
                ph = "growth" if phase[k] == +1 else "contraction"
                lb = lab[k] if lab is not None else "-"
                fo.write(f"{ep[k]:.0f}\t{V[k]:.0f}\t{ph}\t{sub[k]}\t{lb}\n")
        print(f"  -> {out}")


if __name__ == "__main__":
    main()

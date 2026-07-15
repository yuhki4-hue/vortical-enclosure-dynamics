"""band_fate_judge.py -- §12-2c: machine adjudication of band fate
(pre-registered §5.5.2).

Consumes the *_phases.tsv produced by phase_classifier_v1.py
(columns: epoch, V, phase, subphase, label) from an ultra-long run
(3000-5000 ep) and returns one of:

  (a) EXTINCT : band closed, never reopened for the remainder of the run,
                and final V fell below the extinction level v_extinct
                (the V level at which the min-npts criterion can no longer
                structurally hold; calibrate before the run, do not tune
                after seeing results).
  (b) STEADY  : in the tail window, Theil-Sen slope of V is not
                significantly different from zero (Mann-Kendall p > alpha)
                AND the band is continuously open across the tail.
  (c) BREATHE : the local phase classifier detects >= 2 growth<->contraction
                switches after burn-in, and the band re-opens in each
                contraction segment.
  UNDECIDED   : none of the above patterns is clean; report evidence and
                extend the run.

The tail fraction and alpha are fixed relative to the classifier settings
locked in 2b (tail must contain >= 5 smoothing windows).

USAGE:
  python band_fate_judge.py run_phases.tsv --v-extinct 50 \
      --tail-frac 0.2 --alpha 0.05 --burnin-frac 0.1
"""
import argparse

import numpy as np
from scipy import stats


def theil_sen(ep, V):
    return stats.theilslopes(V, ep)  # slope, intercept, lo, hi


def mann_kendall_p(V):
    tau, p = stats.kendalltau(np.arange(len(V)), V)
    return tau, p


def segments(mask):
    """Contiguous True segments as (start_idx, end_idx) inclusive."""
    out, s = [], None
    for k, m in enumerate(mask):
        if m and s is None:
            s = k
        elif not m and s is not None:
            out.append((s, k - 1)); s = None
    if s is not None:
        out.append((s, len(mask) - 1))
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("phases_tsv")
    p.add_argument("--v-extinct", type=float, required=True,
                   help="V level below which min-npts cannot hold "
                        "(calibrate BEFORE the run)")
    p.add_argument("--tail-frac", type=float, default=0.2)
    p.add_argument("--alpha", type=float, default=0.05)
    p.add_argument("--burnin-frac", type=float, default=0.1)
    args = p.parse_args()

    ep, V, phase, sub, lab = [], [], [], [], []
    with open(args.phases_tsv) as f:
        next(f)
        for line in f:
            e, v, ph, sb, lb = line.rstrip("\n").split("\t")
            ep.append(float(e)); V.append(float(v))
            phase.append(ph); sub.append(sb); lab.append(lb)
    ep = np.array(ep); V = np.array(V)
    phase = np.array(phase); lab = np.array(lab)
    n = len(ep)
    metr = lab == "METR"
    burn = int(args.burnin_frac * n)
    tail0 = int((1 - args.tail_frac) * n)

    print(f"run: {n} snapshots, ep {ep[0]:.0f}-{ep[-1]:.0f}, "
          f"final V={V[-1]:.0f}, METR occupancy={metr.mean():.3f}")

    # --- evidence -------------------------------------------------------
    # (a) extinction
    band_segs = segments(metr)
    last_open = band_segs[-1][1] if band_segs else -1
    closed_for_rest = last_open < n - 1
    v_below = V[-1] < args.v_extinct
    ev_a = closed_for_rest and v_below

    # (b) steady tail
    slope, _, lo, hi = theil_sen(ep[tail0:], V[tail0:])
    tau, pval = mann_kendall_p(V[tail0:])
    band_open_tail = metr[tail0:].all()
    ev_b = (pval > args.alpha) and band_open_tail

    # (c) breathing
    ph_post = phase[burn:]
    switches = int((ph_post[1:] != ph_post[:-1]).sum())
    contr_segs = segments((phase == "contraction")[burn:])
    reopen_each = all(metr[burn + s: burn + e + 1].any()
                      for s, e in contr_segs) if contr_segs else False
    ev_c = (switches >= 2) and reopen_each

    print(f"(a) extinction : closed_for_rest={closed_for_rest} "
          f"V_final<{args.v_extinct}={v_below}  -> {ev_a}")
    print(f"(b) steady     : TS slope={slope:.4g} [{lo:.4g},{hi:.4g}] "
          f"MK p={pval:.3f} band_open_tail={band_open_tail}  -> {ev_b}")
    print(f"(c) breathing  : switches={switches} "
          f"reopen_each_contraction={reopen_each}  -> {ev_c}")

    hits = [name for name, ev in (("EXTINCT", ev_a), ("STEADY", ev_b),
                                  ("BREATHE", ev_c)) if ev]
    if len(hits) == 1:
        print(f"\nVERDICT: {hits[0]}")
    elif len(hits) == 0:
        print("\nVERDICT: UNDECIDED (no clean pattern; extend run)")
    else:
        # (c) subsumes (b) if both fire on different sections; report both
        print(f"\nVERDICT: AMBIGUOUS {hits} -- inspect manually, "
              "do not pick post hoc")


if __name__ == "__main__":
    main()

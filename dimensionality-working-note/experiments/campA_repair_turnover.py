"""campA_repair_turnover.py -- §7.6.3: repair/turnover decomposition.

Joins campA alive-cycle logs with locked-standard phase classifier output
and computes, for each consolidation window, the Jaccard overlap of the
alive cycle_id sets at window start and end.

  high Jaccard -> repair   (same cycles survive and re-harden)
  low  Jaccard -> turnover (h recovers via replacement)

USAGE:
  python phase_classifier_v1.py campA_TD_g0.075_s5.tsv --tau-edge 231 \\
      --window-ratio 0.4 --eps-ratio 0.75
  python campA_repair_turnover.py campA_TD_g0.075_s5_phases.tsv \\
      campA_TD_g0.075_s5_alive.tsv
"""
import sys

import numpy as np


def main():
    phases_f, alive_f = sys.argv[1], sys.argv[2]
    ep, sub = [], []
    with open(phases_f) as f:
        next(f)
        for line in f:
            p = line.rstrip("\n").split("\t")
            ep.append(int(float(p[0]))); sub.append(p[3])
    alive = {}
    with open(alive_f) as f:
        for line in f:
            e, ids = line.rstrip("\n").split("\t")
            alive[int(e)] = set(int(x) for x in ids.split(",")) \
                if ids else set()
    # consolidation windows: contiguous subphase == consolidation
    wins, s0 = [], None
    for k in range(len(ep)):
        if sub[k] == "consolidation" and s0 is None:
            s0 = k
        elif sub[k] != "consolidation" and s0 is not None:
            wins.append((ep[s0], ep[k - 1])); s0 = None
    if s0 is not None:
        wins.append((ep[s0], ep[-1]))
    print(f"{len(wins)} consolidation window(s)")
    for w0, w1 in wins:
        A, B = alive.get(w0, set()), alive.get(w1, set())
        if not A and not B:
            continue
        jac = len(A & B) / max(len(A | B), 1)
        surv = len(A & B) / max(len(A), 1)
        born = len(B - A) / max(len(B), 1)
        verdict = ("REPAIR" if jac >= 0.5 else
                   "TURNOVER" if jac < 0.25 else "MIXED")
        print(f"  win ep {w0}-{w1} ({w1-w0}ep): |start|={len(A)} "
              f"|end|={len(B)} Jaccard={jac:.3f} "
              f"start_survival={surv:.3f} end_newborn_frac={born:.3f} "
              f"-> {verdict}")


if __name__ == "__main__":
    main()

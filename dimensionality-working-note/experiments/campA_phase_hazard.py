"""campA_phase_hazard.py -- phase-modulated cycle hazard, discrete-time model
(pre-registered 2026-07-14; replaces window-based KM comparison of §7.7.1).

Risk-set construction: every alive cycle contributes one observation per
snapshot interval it is at risk in; event = death in that interval.
Each observation carries (phase, age_band). No windows, no free choices.

Age bands (locked, from lifetime median tau=185): 0-92, 93-185, 186-370,
371+  (= tau/2, tau, 2*tau cutpoints).
Phases: growth / shedding / consolidation / flat (locked standard
classifier output, window_ratio=0.4, eps_ratio=0.75, tau_edge=231).

Primary quantities per run:
  HR(shedding vs growth), HR(consolidation vs growth),
  age-adjusted via Mantel-Haenszel across age bands.

Registered two-pillar criteria (locked 2026-07-14):
  A. shedding culling: HR_shed>1 and HR_shed>HR_cons.
  B. consolidation age selectivity:
     I_s = log HR_cons,old - log HR_cons,young < 0.
The a0 band is excluded from B because it mostly measures the S-support
attainment grace period rather than phase dynamics.

USAGE:
  python campA_phase_hazard.py campA_TD_g0.075_s5_cycles.tsv \\
      campA_TD_g0.075_s5_alive.tsv campA_TD_g0.075_s5_phases.tsv
"""
import sys

import numpy as np

AGE_BANDS = [(0, 92), (93, 185), (186, 370), (371, 10 ** 9)]


def band(a):
    for k, (lo, hi) in enumerate(AGE_BANDS):
        if lo <= a <= hi:
            return k
    return len(AGE_BANDS) - 1


def main():
    cycles_f, alive_f, phases_f = sys.argv[1:4]
    cyc = np.genfromtxt(cycles_f, names=True, dtype=None, encoding=None)
    birth = {int(r["cycle_id"]): int(r["birth"]) for r in cyc}
    death = {int(r["cycle_id"]): int(r["death"]) for r in cyc}
    alive = {}
    for line in open(alive_f):
        e, ids = line.rstrip("\n").split("\t")
        alive[int(e)] = [int(x) for x in ids.split(",")] if ids else []
    phase = {}
    with open(phases_f) as f:
        next(f)
        for line in f:
            p = line.rstrip("\n").split("\t")
            ep = int(float(p[0]))
            phase[ep] = p[2] if p[3] in ("-", "flat") or p[2] == "growth" \
                else p[3]
            if p[2] == "contraction" and p[3] == "flat":
                phase[ep] = "flat"
    snaps = sorted(alive)
    # risk table: counts[phase][age_band] = [n_at_risk, n_events]
    tab = {}
    for k in range(len(snaps) - 1):
        e0, e1 = snaps[k], snaps[k + 1]
        ph = phase.get(e0)
        if ph is None:
            continue
        for cid in alive[e0]:
            ab = band(e0 - birth[cid])
            cell = tab.setdefault(ph, {}).setdefault(ab, [0, 0])
            cell[0] += 1
            d = death.get(cid, -1)
            if d != -1 and e0 <= d < e1:
                cell[1] += 1

    print("phase x age_band hazard table (events/at-risk per 25ep interval):")
    phases = [p for p in ("growth", "shedding", "consolidation", "flat")
              if p in tab]
    for p in phases:
        row = []
        for ab in range(len(AGE_BANDS)):
            n, d = tab[p].get(ab, [0, 0])
            row.append(f"a{ab}:{d}/{n}" + (f"={d/n:.3f}" if n else ""))
        print(f"  {p:13s} " + "  ".join(row))

    # Mantel-Haenszel age-adjusted HR vs growth
    def mh_hr(pnum, pden="growth"):
        num = den = 0.0
        for ab in range(len(AGE_BANDS)):
            n1, d1 = tab.get(pnum, {}).get(ab, [0, 0])
            n0, d0 = tab.get(pden, {}).get(ab, [0, 0])
            if n1 and n0:
                T = n1 + n0
                num += d1 * n0 / T
                den += d0 * n1 / T
        return num / den if den else np.nan

    print("\nage-adjusted (Mantel-Haenszel over locked 4 bands) HR vs growth:")
    out = {}
    for p in ("shedding", "consolidation", "flat"):
        if p in tab:
            hr = mh_hr(p)
            out[p] = hr
            print(f"  HR({p:13s}) = {hr:.3f}")

    # ---- registered two-pillar criteria (locked 2026-07-14) -----------
    # young = a0+a1, old = a2+a3 (bands frozen from s5; do NOT re-derive)
    def stratum_hr(pnum, bands, pden="growth"):
        d1 = n1 = d0 = n0 = 0
        for ab in bands:
            a, b = tab.get(pnum, {}).get(ab, [0, 0])
            c, d = tab.get(pden, {}).get(ab, [0, 0])
            n1 += a; d1 += b; n0 += c; d0 += d
        if n1 and n0 and d0:
            return (d1 / n1) / (d0 / n0)
        return np.nan

    hr_shed = out.get("shedding", np.nan)
    hr_cons = out.get("consolidation", np.nan)
    # a0 excluded: its hazard is the attainment grace period
    # (instrument-defined), not dynamics. young = a1, old = a2+a3.
    hr_cons_y = stratum_hr("consolidation", [1])
    hr_cons_o = stratum_hr("consolidation", [2, 3])
    hr_shed_y = stratum_hr("shedding", [1])
    hr_shed_o = stratum_hr("shedding", [2, 3])
    I_s = (np.log(hr_cons_o) - np.log(hr_cons_y)
           if np.isfinite(hr_cons_o) and np.isfinite(hr_cons_y)
           else np.nan)
    A = np.isfinite(hr_shed) and np.isfinite(hr_cons) \
        and hr_shed > 1 and hr_shed > hr_cons
    B = np.isfinite(I_s) and I_s < 0
    print(f"\nphase x age strata: HR_cons(young a1)={hr_cons_y:.3f} "
          f"HR_cons(old a2+a3)={hr_cons_o:.3f}  "
          f"[shed young={hr_shed_y:.3f} old={hr_shed_o:.3f}]")
    print(f"criterion A (shedding culling: HR_shed>1 AND HR_shed>HR_cons): "
          f"{'PASS' if A else 'FAIL'}")
    print(f"criterion B (age selectivity: I_s = logHR_cons,old - "
          f"logHR_cons,young = {I_s:+.3f} < 0): {'PASS' if B else 'FAIL'}")
    print(f"secondary record: HR_cons,old<1 -> "
          f"{'yes' if hr_cons_o < 1 else 'no'}")


if __name__ == "__main__":
    main()

"""campA_insertion_hazard.py -- §7.7.3: feeding competition as mechanism
decomposition of the phase effect (registered 2026-07-14).

NOT a mediation test. The phase classifier is built from smoothed dV/dt,
so insertion rate is not exogenous to phase. What this measures is how
much of the information carried by the phase label can be re-described by
insertion pressure.

Variable audit (passed before lock): cycles.tsv `birth` == T1 insertion
epoch, exactly, per epoch and on the 25ep grid. So births/interval IS the
insertion rate, not a cycle-appearance rate.

Model (locked):
  x_t = log(1 + N_insert(t-dt, t) / dt)        [one-interval LAG]
  logit P(D_c,t=1) = age + phase + x_t + age:x_t + age:phase + seed FE
  age: young = a1 (93-185), old = a2+a3 (186+); a0 excluded (attainment
       grace period, instrument not dynamics)
Primary coefficient: beta_{age=old : x} > 0
Insertion-rate stratification is for visualization only; the primary test
uses the continuous variable.

USAGE:
  python campA_insertion_hazard.py --label design \\
      s5:cycles.tsv,alive.tsv,phases.tsv s7:... s10:...
"""
import argparse

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

A0_MAX = 92
A1_MAX = 185


def build(seed, cycles_f, alive_f, phases_f):
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
            phase[ep] = "growth" if p[2] == "growth" else (
                p[3] if p[3] in ("shedding", "consolidation") else "flat")
    snaps = sorted(alive)
    dt = int(np.median(np.diff(snaps)))
    # insertion count per interval, from births (audited == T1 count)
    ins = {}
    for cid, b in birth.items():
        k = ((b // dt) + 1) * dt
        ins[k] = ins.get(k, 0) + 1

    rows = []
    for k in range(1, len(snaps) - 1):
        e_prev, e0, e1 = snaps[k - 1], snaps[k], snaps[k + 1]
        ph = phase.get(e0)
        if ph is None or ph == "flat":
            continue
        # LAG: insertion pressure over the PREVIOUS interval
        x = np.log1p(ins.get(e0, 0) / dt)
        for cid in alive[e0]:
            age = e0 - birth[cid]
            if age <= A0_MAX:
                continue          # a0 excluded (attainment grace)
            ageband = "young" if age <= A1_MAX else "old"
            d = death.get(cid, -1)
            ev = int(d != -1 and e0 <= d < e1)
            rows.append(dict(seed=str(seed), phase=ph, age=ageband,
                             x=x, ev=ev))
    return pd.DataFrame(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("runs", nargs="+",
                    help="seed:cycles.tsv,alive.tsv,phases.tsv")
    ap.add_argument("--label", default="")
    args = ap.parse_args()

    dfs = []
    for spec in args.runs:
        seed, files = spec.split(":", 1)
        c, a, p = files.split(",")
        dfs.append(build(seed, c, a, p))
    df = pd.concat(dfs, ignore_index=True)
    print(f"[{args.label}] risk set: {len(df)} cycle-intervals, "
          f"{df.ev.sum()} deaths, seeds={sorted(df.seed.unique())}")
    print(f"  x (log insertion pressure): median={df.x.median():.3f} "
          f"range=[{df.x.min():.3f},{df.x.max():.3f}]")
    print("  x by phase (median): " + ", ".join(
        f"{p}={g.x.median():.3f}" for p, g in df.groupby("phase")))

    # visualization-only stratification (NOT the primary test)
    print("\n  [visualization only] death rate by age x insertion tertile:")
    df["xt"] = pd.qcut(df.x, 3, labels=["low", "mid", "high"],
                       duplicates="drop")
    piv = df.pivot_table(index="xt", columns="age", values="ev",
                         aggfunc="mean", observed=True)
    for t in piv.index:
        y, o = piv.loc[t, "young"], piv.loc[t, "old"]
        print(f"    x={t:5s}: young={y:.3f} old={o:.3f} old/young={o/y:.3f}")

    fml = ("ev ~ C(seed) + C(age, Treatment('young'))"
           " + C(phase, Treatment('growth')) + x"
           " + C(age, Treatment('young')):x"
           " + C(age, Treatment('young')):C(phase, Treatment('growth'))")
    m = smf.glm(fml, data=df, family=sm.families.Binomial()).fit()
    print("\n=== registered model (age + phase + x + age:x + age:phase) ===")
    for k in m.params.index:
        if "Intercept" in k or "seed" in k:
            continue
        ci = m.conf_int().loc[k]
        star = ""
        if k.endswith(":x") or k == "x:C(age, Treatment('young'))[T.old]":
            star = "   <-- PRIMARY"
        print(f"  {k:58s} beta={m.params[k]:+.4f} "
              f"CI[{ci[0]:+.4f},{ci[1]:+.4f}] p={m.pvalues[k]:.2e}{star}")

    prim = [k for k in m.params.index if ":x" in k or k.startswith("x:")]
    if prim:
        k = prim[0]
        b = m.params[k]
        print(f"\nPRIMARY beta_(age=old):x = {b:+.4f}  "
              f"p={m.pvalues[k]:.2e}  -> {'POSITIVE (predicted)' if b > 0 else 'NEGATIVE (against prediction)'}")

    # what happens to phase x age once x is in the model
    m0 = smf.glm("ev ~ C(seed) + C(age, Treatment('young'))"
                 " + C(phase, Treatment('growth'))"
                 " + C(age, Treatment('young')):C(phase, Treatment('growth'))",
                 data=df, family=sm.families.Binomial()).fit()
    print("\n=== phase:age interaction, without x vs with x ===")
    for k in m0.params.index:
        if ":" in k and "seed" not in k:
            kk = [q for q in m.params.index if q == k]
            b_with = m.params[kk[0]] if kk else np.nan
            print(f"  {k[-30:]:30s} without_x={m0.params[k]:+.4f}  "
                  f"with_x={b_with:+.4f}  "
                  f"shrink={100*(1-abs(b_with)/abs(m0.params[k])):+.0f}%")


if __name__ == "__main__":
    main()

# v24.2 Headroom Runs

These files preserve the first v24.2 headroom run for Dimensionality Working
Note II. The model dynamics are intended to remain identical to v24; v24.2 adds
read-only instruments for scaling-width, support-ladder, destination-fanout,
and headroom diagnostics.

## Purpose

The v24.1 scan showed that directed runs at `N=300/450/650` were entangled with
capacity limits: many runs reached `NMAX`, after which T1 insertion stops and
the model shifts toward a REG-only regime. The v24.2 headroom run increases
`NMAX` to separate BSW behavior from capacity saturation.

## Command

```bash
python3 growth_v24_2_headroom.py 0.075 900 5,7,10,15,21,33 1200 T1
```

Output:

- [v24_2_T1_g0075_N1200_900ep_seeds_5_7_10_15_21_33.txt](v24_2_T1_g0075_N1200_900ep_seeds_5_7_10_15_21_33.txt)

## Aggregate Summary

| mode | total BSW_occ | total windows | seeds with BSW | total dead | max V | first saturation |
|---|---:|---:|---:|---:|---:|---|
| directed | 183 | 35 | 6/6 | 5783 | 1049/1200 | none |
| symmetric | 1 | 1 | 1/6 | 5911 | 371/1200 | none |

## npts Threshold Check

| mode | npts >= 4 | npts >= 5 | npts >= 6 |
|---|---:|---:|---:|
| directed | 183 | 52 | 4 |
| symmetric | 1 | 0 | 0 |

## Initial Reading

The headroom run removes the direct NMAX-saturation confound for this parameter
set: no run reached capacity, and the largest directed run stayed below the
95 percent headroom warning threshold (`1049/1200`).

Under this condition, directed runs still produce many more BSW snapshots than
the symmetric control. With the stricter `npts >= 5` reading, the directed runs
retain 52 snapshots across four seeds, while the symmetric control retains
none.

This supports the v24.1 reading that the directed rule bundle is associated
with longer-lived registration and more robust ball-scaling windows. It does
not yet identify the causal factor: self-feeding prohibition, destination
fanout, cyclic-core formation, and state-size differences remain to be
separated by later rule-decomposition runs.

## Boundary

These runs measure BSW and support-ladder behavior under added headroom. They
do not establish MRW, do not derive `3+1` dimensions, and do not prove that
cyclic core variables causally generate metric readability.

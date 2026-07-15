# v24.2e Extended-Epoch Runs

These files preserve the first v24.2e extended-epoch run for Dimensionality
Working Note II. The model dynamics are intended to remain identical to v24;
v24.2e adds read-only instruments for edge evaporation, S-support edge density,
and path-redundancy diagnostics.

## Purpose

The v24.2 headroom run showed that directed BSW behavior survives without
NMAX saturation, but some contraction windows were still cut off by the end of
the 900-epoch run. v24.2e extends the run to observe later contraction behavior
and to test whether contraction-phase BSW is tree-like thinning or retains
path redundancy.

## Command

```bash
python3 growth_v24_2e_extended.py 0.075 1500 5,7,10,15,21,33 2000 T1
```

Output:

- [v24_2e_T1_g0075_N2000_1500ep_seeds_5_7_10_15_21_33.txt](v24_2e_T1_g0075_N2000_1500ep_seeds_5_7_10_15_21_33.txt)
- [v24_2e_T1_g0075_N2000_1500ep_seeds_5_7_10_15_21_33_weight_export.txt](v24_2e_T1_g0075_N2000_1500ep_seeds_5_7_10_15_21_33_weight_export.txt)

## Aggregate Summary

| mode | total BSW_occ | total windows | seeds with BSW | total dead | max V | first saturation |
|---|---:|---:|---:|---:|---:|---|
| directed | 478 | 39 | 6/6 | 10275 | 1049/2000 | none |
| symmetric | 1 | 1 | 1/6 | 10242 | 371/2000 | none |

## npts Threshold Check

| mode | npts >= 4 | npts >= 5 | npts >= 6 |
|---|---:|---:|---:|
| directed | 478 | 295 | 162 |
| symmetric | 1 | 0 | 0 |

## Exit Reasons

| mode | SW | END | FRAG | SAT |
|---|---:|---:|---:|---:|
| directed | 34 | 5 | 0 | 0 |
| symmetric | 1 | 0 | 0 | 0 |

The extended run reduces but does not eliminate END-cut windows. No FRAG or SAT
exit was observed in this parameter set.

## Contraction-Phase Redundancy Check

Pooled across directed contraction snapshots:

| metric | BSW median | non-BSW median |
|---|---:|---:|
| `occ2ecc` | 0.730 | 0.730 |
| `brfrac` | 0.180 | 0.160 |
| `kmean` | 3.020 | 3.230 |
| `evapE` | 28.000 | 22.000 |
| `E_S` | 499.000 | 831.000 |

Initial reading:

- The contraction BSW snapshots are not simply tree-like: `occ2ecc` remains
  high.
- BSW snapshots have lower mean degree and fewer S-support edges than
  contraction non-BSW snapshots.
- This supports reading the BSW band as a thinner but still redundant
  readability band, rather than a pure tree-like thinning artifact.

## Boundary

These runs still measure BSW and redundancy diagnostics, not MRW directly.
They do not derive `3+1` dimensions and do not by themselves identify the
causal variable that opens the readable band.

## Weight Export And Recalibration

The same run was repeated after adding read-only export of robust-BSW
`-log(S)` support-edge weights. The model dynamics are intended to remain
unchanged; the added files are audit outputs.

Generated files:

- `v24_2e_directed_g0.075_s*_snapshots.tsv`
- `v24_2e_symmetric_g0.075_s*_snapshots.tsv`
- `v24_2e_directed_g0.075_s*_bsw_weights.txt`
- `v24_2e_symmetric_g0.075_s*_bsw_weights.txt`
- `v24_2e_directed_bsw_weights_pooled.txt`
- `v24_2e_directed_bsw_weighted_nonperiodic_anchor_table.tsv`
- `v24_2e_directed_bsw_weighted_nonperiodic_anchor_table.txt`

The directed robust-BSW pool contains 397,954 weights:

```text
median = 6.2214
mean   = 6.8698
CV     = 0.4840
p10    = 2.9316
p90    = 12.0261
```

Robust directed BSW snapshots (`METR` with `npts >= 5`) have:

```text
n = 295
V range = 127..1024
V median = 371
old d_cal median = 2.699
old d_cal IQR = [2.052, 3.118]
```

Using non-periodic, size-matched, empirical-weight anchors, the recalibrated
values are:

```text
new d median = 2.339
new d IQR = [1.943, 2.642]
new d range = 0.804..3.592
new d p10/p90 = 1.531 / 2.854
above 3 = 11 snapshots
below 2 = 86 snapshots
```

This means the old `d_cal≈2.6` layer is also convention-dependent. Under the
faithful convention used here, the v24.2e robust band shifts downward rather
than upward.

## 2b Classifier Calibration Status

The local phase classifier was scanned on the exported v24.2e directed
snapshot TSV files:

- `v24_2e_directed_phase_classifier_scan_tau231.txt`
- `v24_2e_directed_phase_classifier_scan_tau231_unimodal_subset.txt`
- `v24_2e_directed_phase_classifier_scan_tau231_v2.txt`
- `v24_2e_directed_phase_classifier_standard_s5_s33.txt`
- `v24_2e_directed_phase_classifier_standard_all_seeds.txt`

The first scan used a frozen historical target and produced no reproducing
region. The v2 scan uses the adjudicated criterion from Working Note II:
same-run agreement with the old classifier on mechanically selected unimodal
runs, plus switch parsimony and h U-shape ordering.

Mechanical unimodal selection identifies two runs, seed 5 and seed 33. The v2
scan finds four reproducing grid points:

```text
(window_ratio=0.2, eps_ratio=1.0)
(window_ratio=0.3, eps_ratio=1.0)
(window_ratio=0.5, eps_ratio=0.25)
(window_ratio=0.5, eps_ratio=0.5)
```

The registered standard setting is the midpoint candidate:

```text
window_ratio = 0.4
eps_ratio = 0.75
```

At that setting:

```text
seed 5 : new 0.206 / 1.000, old 0.190 / 0.924, switches=1
seed 33: new 0.425 / 1.000, old 0.324 / 1.000, switches=1
```

This unlocks the 2c band-fate run in principle. The repository does not yet
contain the 4000-epoch 2c trajectory mentioned in the working note, so that
external result remains to be mirrored or independently reproduced here.

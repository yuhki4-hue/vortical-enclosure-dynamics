# v24.3 Rule Decomposition Runs

These runs test a two-by-two decomposition of the v24 growth rule. They are
diagnostic outputs for Dimensionality Working Note II, not final simulations or
proofs of metric-readability.

## Command

Each cell was run with:

```bash
python3 ../growth_v24_3_rules.py 0.075 900 5,7,10,15,21,33 2000 <cell>
```

where `<cell>` is one of:

- `directed`
- `cellA`
- `cellB`
- `symmetric`

## Output Logs

| Cell | Output log |
|---|---|
| directed | `v24_3_directed_g0075_N2000_900ep_seeds_5_7_10_15_21_33.txt` |
| cellA | `v24_3_cellA_g0075_N2000_900ep_seeds_5_7_10_15_21_33.txt` |
| cellB | `v24_3_cellB_g0075_N2000_900ep_seeds_5_7_10_15_21_33.txt` |
| symmetric | `v24_3_symmetric_g0075_N2000_900ep_seeds_5_7_10_15_21_33.txt` |

Per-seed TSV files are also preserved in this directory.

## Aggregate Reading

| Cell | SAT seeds | Total BSW snapshots | BSW snapshots with `npts >= 5` | Pooled median edge life | Pooled p90 edge life | Mean `n_dst` | Mean fire share | Mean reverse share | Reflections |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| directed | 0/6 | 78 | 21 | 231 | 490 | 17.7 | n/a | n/a | 316 |
| cellA | 0/6 | 0 | 0 | 157 | 171 | 94.2 | 0.8373 | 0.0022 | 0 |
| cellB | 0/6 | 17 | 3 | 242 | 423 | 114.3 | n/a | n/a | 52 |
| symmetric | 0/6 | 1 | 0 | 163 | 184 | 58.3 | 0.4158 | 0.0008 | 0 |

## Pre-Registered Interaction Check

The pre-registered interaction check compared the self-feeding effect in the
one-sided and two-sided contexts:

```text
one-sided self-feed effect = cellA - directed = -74.0
two-sided self-feed effect = symmetric - cellB = -79.0
opposite_sign = False
abs_ratio = 1.0676
interaction_by_preregistered_rule = False
```

The interaction test is therefore negative. Self-feeding shortened median edge
lifetime in both contexts.

## Initial Interpretation

The run supports a limited diagnostic reading:

- cells with self-feeding allowed (`cellA`, `symmetric`) were short-lived;
- cells with self-feeding banned (`directed`, `cellB`) were longer-lived;
- the directed cell retained the strongest robust BSW count among the four
  cells;
- `cellA` showed strong fire-edge capture but no BSW snapshots;
- no cell reached capacity saturation.

This should not be read as MRW detection or as a completed causal derivation.
It narrows the next question: why one-sided fanout with self-feeding banned
preserves robust BSW more effectively than the other cells.

## Remaining Confound

The fanout axis should not yet be identified directly with dilution. In this
run, `cellB` has high `n_dst`, but this reflects both the two-sided fanout rule
and the fact that the system remains larger and longer-lived. By contrast,
`cellA` and `symmetric` remain smaller, so their `n_dst` values are partly
conditioned by different state sizes.

The directed-vs-`cellB` comparison is still informative because those cells are
closer in lifetime and size than the self-feeding cells, and directed retains a
stronger robust BSW count. However, the mechanism should not be summarized as
"two-sided fanout kills readability by dilution" without a further
state-stratified audit. The next useful check is to stratify peeled or
surviving edges by local attributes, realized share, support layer, and phase,
rather than reviving the dilution hypothesis as an untested explanation of
readability.

## Phase / Band-Fate Smoke

The local classifier and band-fate judge were smoke-tested on the directed
seed-15 run:

- `v24_3_directed_phase_classifier_scan_tau231.txt`
- `v24_3_directed_g0.075_s15_phase_classifier.txt`
- `v24_3_directed_g0.075_s15_phases.tsv`
- `v24_3_directed_g0.075_s15_band_fate_smoke.txt`

The classifier gave values close to the old per-run classifier for this seed.
The band-fate judge returned:

```text
VERDICT: UNDECIDED (no clean pattern; extend run)
```

This result is recorded as a campaign-instrument smoke test only.

## BSW Weight Export and Anchor Recalibration

The directed cell was rerun with the same settings after adding robust-BSW
weight export to `growth_v24_3_rules.py`. For each robust BSW snapshot
(`METR` with `npts >= 5`), the script exports one `-log(S)` support-edge
weight per line.

Generated files:

- `v24_3_directed_g0075_N2000_900ep_seeds_5_7_10_15_21_33_weights_export.txt`
- `v24_3_directed_g0.075_s5_bsw_weights.txt`
- `v24_3_directed_g0.075_s7_bsw_weights.txt`
- `v24_3_directed_g0.075_s10_bsw_weights.txt`
- `v24_3_directed_g0.075_s15_bsw_weights.txt`
- `v24_3_directed_g0.075_s21_bsw_weights.txt`
- `v24_3_directed_g0.075_s33_bsw_weights.txt`
- `v24_3_directed_bsw_weights_pooled.txt`
- `v24_3_directed_bsw_weighted_nonperiodic_anchor_table.tsv`
- `v24_3_directed_bsw_weighted_nonperiodic_anchor_table.txt`

The pooled empirical weight sample contains 42,682 values:

```text
median = 6.0809
mean   = 6.7997
CV     = 0.4977
p10    = 2.8019
p90    = 12.0118
```

The robust BSW snapshots have `V=356..890` with median `V=657`.

Using `lattice_anchor_ext.py --weights-from` with non-periodic,
size-matched, empirical-weight anchors gives:

| target V | 1D | 2D | 3D | 4D |
|---:|---:|---:|---:|---:|
| 356 | 0.970 | 1.821 | 2.459 | 2.756 |
| 657 | 0.978 | 1.870 | 2.586 | 2.979 |
| 890 | 0.979 | 1.888 | 2.618 | 2.979 |

The old `d_cal≈3.43` corresponds to measured slope `b≈2.415`. Under this
faithful convention, `b≈2.415` falls below the 3D anchor for all three target
sizes. Linear interpolation gives approximately:

```text
V≈356 -> d≈2.93
V≈657 -> d≈2.76
V≈890 -> d≈2.72
```

This does not support a "3.4-dimensional" reading. It supports the audit
conclusion that `d_cal` is convention-dependent and that the directed robust
BSW should be reported with both the old convention and the faithful
non-periodic, size-matched, empirical-weight convention.

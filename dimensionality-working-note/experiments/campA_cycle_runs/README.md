# Campaign A Cycle Runs

Campaign A implements the cycle-individual tracking protocol from Working Note
II. These outputs are diagnostic logs, not final simulations or empirical
verification.

## Run Setting

- Cells: `TD` and `TL2`
- Parameters: `g=0.075`, `epochs=900`, `NMAX=2000`
- Seeds: `5,7,10,15,21,33`
- Phase-classifier setting: `tau_edge=231`, `window_ratio=0.4`,
  `eps_ratio=0.75`

## Commands

```bash
python3 ../growth_campA_cycles.py 0.075 900 5,7,10,15,21,33 2000 TD
python3 ../growth_campA_cycles.py 0.075 900 5,7,10,15,21,33 2000 TL2

python3 ../phase_classifier_v1.py campA_TD_g0.075_s5.tsv campA_TD_g0.075_s7.tsv campA_TD_g0.075_s10.tsv campA_TD_g0.075_s15.tsv campA_TD_g0.075_s21.tsv campA_TD_g0.075_s33.tsv --tau-edge 231 --window-ratio 0.4 --eps-ratio 0.75
python3 ../phase_classifier_v1.py campA_TL2_g0.075_s5.tsv campA_TL2_g0.075_s7.tsv campA_TL2_g0.075_s10.tsv campA_TL2_g0.075_s15.tsv campA_TL2_g0.075_s21.tsv campA_TL2_g0.075_s33.tsv --tau-edge 231 --window-ratio 0.4 --eps-ratio 0.75

python3 ../campA_repair_turnover.py <run>_phases.tsv <run>_alive.tsv

python3 ../campA_insertion_hazard.py --label design \
  s5:campA_TD_s5_4000ep_cycles.tsv,campA_TD_s5_4000ep_alive.tsv,campA_TD_s5_4000ep_phases.tsv \
  s7:campA_TD_s7_4000ep_cycles.tsv,campA_TD_s7_4000ep_alive.tsv,campA_TD_s7_4000ep_phases.tsv \
  s10:campA_TD_s10_4000ep_cycles.tsv,campA_TD_s10_4000ep_alive.tsv,campA_TD_s10_4000ep_phases.tsv

python3 ../campA_insertion_hazard.py --label holdout \
  s15:campA_TD_s15_4000ep_cycles.tsv,campA_TD_s15_4000ep_alive.tsv,campA_TD_s15_4000ep_phases.tsv \
  s21:campA_TD_s21_4000ep_cycles.tsv,campA_TD_s21_4000ep_alive.tsv,campA_TD_s21_4000ep_phases.tsv \
  s33:campA_TD_s33_4000ep_cycles.tsv,campA_TD_s33_4000ep_alive.tsv,campA_TD_s33_4000ep_phases.tsv
```

## Cycle Tracking Summary

| Cell | Mean cycles | Median cycle life | Mean died-new fraction | Mean robust BSW count | TL fallback |
|---|---:|---:|---:|---:|---:|
| `TD` | 1433.8 | 189.0 | 0.763 | 3.5 | 0.0 |
| `TL2` | 1006.0 | 146.5 | 0.410 | 2.2 | 6.3 |

Interpretation boundary: the TD/TL2 contrast supports a difference in cycle
persistence and death attribution under this run setting. It should not yet be
read as a completed causal explanation of metric readability.

## Repair / Turnover Check

The locked phase classifier produced only two consolidation windows across
the twelve runs:

| Cell | Seed | Window | Jaccard | Verdict |
|---|---:|---|---:|---|
| `TD` | 33 | ep 825-900 | 0.409 | `MIXED` |
| `TL2` | 33 | ep 850-900 | 0.452 | `MIXED` |

This is too sparse for a stable repair/turnover conclusion. The immediate
reading is methodological: a longer or more targeted Campaign A run is needed
before consolidation-window replacement can be used as a primary claim.

## 4000-Epoch TD Seed-5 Reconciliation

Additional externally generated TD seed-5 4000-epoch logs were imported to
reconcile Campaign A with the 2c trajectory.

Primary files:

- `campA_TD_s5_4000ep.tsv`
- `campA_TD_s5_4000ep_cycles.tsv`
- `campA_TD_s5_4000ep_alive.tsv`
- `campA_TD_s5_4000ep_phases.tsv`
- `campA_TD_s5_4000ep_repair_turnover.txt`

The standard phase classifier finds three switches and two consolidation
windows. The long consolidation window `3625-4000` has raw Jaccard `0.055`
and endpoint newborn fraction `0.886`, which looks like turnover under the
raw Jaccard rule. After age-conditioned Kaplan-Meier baseline correction,
the same window shows observed survival about `2.86x` the baseline
expectation. The interpretation is therefore not simple repair versus simple
turnover, but turnover under a phase-dependent hazard-suppression field.

## 4000-Epoch TD Seed-7 Phase-Hazard Check

Externally generated TD seed-7 4000-epoch logs were imported as the first
confirmation seed for the phase-modulated hazard campaign.

Primary files:

- `campA_TD_s7_4000ep.tsv`
- `campA_TD_s7_4000ep_cycles.tsv`
- `campA_TD_s7_4000ep_alive.tsv`
- `campA_TD_s7_4000ep_phases.tsv`
- `campA_TD_s7_4000ep_phase_hazard.txt`

The standard phase classifier again finds three switches. The discrete-time
cycle-hazard audit gives `HR_shedding=1.594` and `HR_consolidation=0.567`,
so criterion A passes: shedding is a higher-hazard phase than growth and
consolidation. Criterion B fails for this seed: `I_s=+0.936`, with young
cycles protected more strongly than old cycles. This preserves the shedding
culling signal while making the age-selectivity direction seed-dependent.

## 4000-Epoch TD Confirmation Seeds

The remaining confirmation seeds `10,15,21,33` were generated locally with
the same TD 4000-epoch setting and processed through the locked standard phase
classifier and `campA_phase_hazard.py`.

Primary summary:

- `campA_TD_4000ep_seeds_10_15_21_33.txt`
- `campA_TD_4000ep_phase_hazard_summary.tsv`

| Seed | Switches | HR shedding | HR consolidation | I_s | A | B |
|---:|---:|---:|---:|---:|---|---|
| 7 | 3 | 1.594 | 0.567 | +0.936 | PASS | FAIL |
| 10 | 2 | 1.397 | 1.154 | -0.362 | PASS | PASS |
| 15 | 5 | 1.306 | 1.299 | -0.372 | PASS | PASS |
| 21 | 3 | 1.262 | 0.893 | -0.131 | PASS | PASS |
| 33 | 5 | 1.584 | 1.134 | -0.299 | PASS | PASS |

Registered outcome: criterion A passes in `5/5` confirmation seeds and
criterion B passes in `4/5`, meeting the pre-registered reproduction gate.
The registered gate passes, but later decomposition changes the reading. The
age-selectivity ratio is not evidence that consolidation alone creates the
age effect. Absolute hazards show that the sharp age dependence belongs to the
growth phase: old cycles are culled more strongly during growth, while
shedding and consolidation have much weaker old/young slopes.

## 4000-Epoch TD Insertion-Pressure Audit

`campA_insertion_hazard.py` tests whether the phase label's age-hazard
information can be re-described by lagged insertion pressure. This is a
mechanism decomposition, not a mediation test, because the phase classifier
itself is built from smoothed `dV/dt`.

Design seeds `5,7,10` reproduce the previously shared diagnostic:
`beta_age_x=+0.0772` with `p=0.078`, and phase-age terms shrink only
`4-11%`. Holdout seeds `15,21,33` give a stronger but still partial result:
`beta_age_x=+0.1846`, `p=3.89e-05`, with all three seed-level coefficients
positive. However, phase-age terms shrink only `18-19%` and remain negative.

Registered reading: partial decomposition. Insertion competition contributes
to the growth-phase old-cycle hazard, but most of the phase-age residual
remains. The next target is feeding-allocation structure rather than insertion
count alone.

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

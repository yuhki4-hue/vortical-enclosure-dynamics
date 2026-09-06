# Campaign A Flux Ledger Runs

This directory contains TD 4000-epoch edge flux-fate ledger runs for
Dimensionality Working Note II §7.7.4.

These files are diagnostic logs. They are not empirical verification and do
not by themselves establish a causal mechanism. The purpose is to add a
pure-read edge-level ledger on top of the existing Campaign A TD trajectories.

## Run Setting

- Cell: `TD`
- Parameters: `g=0.075`, `epochs=4000`, `NMAX=2000`
- Seeds: `5,7,10,15,21,33`
- Script: `../growth_flux_ledger.py`
- Dynamics: forked from `growth_campA_cycles.py`
- Instrument status: pure read, no additional RNG calls

## Command

```bash
python3 ../growth_flux_ledger.py 0.075 4000 5,7,10,15,21,33 2000 TD
```

## Outputs

Each seed writes:

- `campA_TD_g0.075_s<seed>.tsv`
- `campA_TD_g0.075_s<seed>_cycles.tsv`
- `campA_TD_g0.075_s<seed>_alive.tsv`
- `campA_TD_g0.075_s<seed>_ledger.tsv`
- `campA_TD_g0.075_s<seed>_cycedges.tsv`

The ledger records edge-level:

- `O`: candidacy count
- `F_alloc`: allocation-layer realized share
- `F_H`: H-layer inflow
- `D`: decay
- `k`: alive-cycle sharing load
- `H_start`, `S_start`, `age_e`, `died`

## Pure-Read Check

The flux-ledger rerun was compared with the existing
`campA_cycle_runs/campA_TD_s<seed>_4000ep*` outputs.

| Seed | Common TSV columns | Max float diff | Cycles byte match | Alive byte match |
|---:|---|---:|---|---|
| 5 | match | 1.07e-14 | yes | yes |
| 7 | match | 8.88e-15 | yes | yes |
| 10 | match | 0.00e+00 | yes | yes |
| 15 | match | 0.00e+00 | yes | yes |
| 21 | match | 0.00e+00 | yes | yes |
| 33 | match | 0.00e+00 | yes | yes |

The small nonzero differences are final-digit floating-point formatting
differences in the snapshot TSV. Cycle and alive logs are byte-identical.

## Ledger Summary

| Seed | Ledger rows | `O=0` | Median share | Maintenance burden | Median `k` | Max `k` | `k>=2` | corr(`F_alloc`,`F_H`) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 133828 | 39.0% | 0.04483 | 4.7% | 1 | 13 | 14.5% | 0.832 |
| 7 | 126287 | 34.4% | 0.03218 | 5.1% | 1 | 18 | 13.9% | 0.825 |
| 10 | 112695 | 40.3% | 0.04611 | 4.7% | 1 | 22 | 14.0% | 0.842 |
| 15 | 133789 | 45.6% | 0.05932 | 4.0% | 1 | 24 | 14.3% | 0.859 |
| 21 | 139251 | 41.5% | 0.03897 | 4.4% | 1 | 27 | 14.1% | 0.836 |
| 33 | 124238 | 41.4% | 0.05104 | 4.2% | 1 | 18 | 13.9% | 0.843 |

These summary values are sanity checks for populated ledger fields. They are
not the registered A/B test for §7.7.4.

## Interpretation Boundary

The next analysis should test the two registered questions separately:

- A: whether growth-phase old-cycle culling is explained by cycle-level
  lower-tail maintenance margin.
- B: whether selective loss of high-sharing edges precedes overlap reduction
  and later widening of `W_cont`.

The ledger should not be read as an intervention. It is a read-only audit layer
for deciding which allocation or maintenance mechanism should be targeted
later.

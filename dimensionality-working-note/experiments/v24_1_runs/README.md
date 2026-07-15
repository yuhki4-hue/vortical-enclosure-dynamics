# v24.1 Instrument Re-Reading Runs

These files preserve the first v24.1 instrument re-reading runs for
Dimensionality Working Note II. The model dynamics are intended to remain
identical to v24; the added instruments are read-only diagnostics.

## Command Pattern

```bash
python3 growth_v24_1_instruments.py 0.075 900 5,7,10,15,21,33 N T1
```

where `N` was scanned across `300`, `450`, and `650`.

## Output Files

| N | Output |
|---:|---|
| 300 | [v24_1_T1_g0075_N300_900ep_seeds_5_7_10_15_21_33.txt](v24_1_T1_g0075_N300_900ep_seeds_5_7_10_15_21_33.txt) |
| 450 | [v24_1_T1_g0075_N450_900ep_seeds_5_7_10_15_21_33.txt](v24_1_T1_g0075_N450_900ep_seeds_5_7_10_15_21_33.txt) |
| 650 | [v24_1_T1_g0075_N650_900ep_seeds_5_7_10_15_21_33.txt](v24_1_T1_g0075_N650_900ep_seeds_5_7_10_15_21_33.txt) |

## Aggregate BSW Summary

| N | mode | total BSW_occ | total windows | seeds with BSW | total dead | all audit OK |
|---:|---|---:|---:|---:|---:|---|
| 300 | directed | 27 | 8 | 4/6 | 753 | true |
| 300 | symmetric | 22 | 3 | 1/6 | 5570 | true |
| 450 | directed | 52 | 16 | 4/6 | 2169 | true |
| 450 | symmetric | 1 | 1 | 1/6 | 5911 | true |
| 650 | directed | 194 | 28 | 6/6 | 4071 | true |
| 650 | symmetric | 1 | 1 | 1/6 | 5911 | true |

## Initial Reading

This first scan supports treating v24.1 as a diagnostic re-reading run rather
than a new derivation. In the `N=450` and `N=650` runs, BSW occupancy is much
more frequent in the directed version than in the symmetric control. The
`N=300` result is less clean: the symmetric control has fewer BSW-positive
seeds but a nontrivial BSW occupancy in one seed. This should be read as a
reason for further stratification, not as a settled directional claim.

Across all runs, the audit status remained `OK`.

## Boundary

These runs measure BSW behavior and instrument relations. They do not establish
MRW, do not derive `3+1` dimensions, and do not by themselves prove that cyclic
core variables causally generate metric readability.

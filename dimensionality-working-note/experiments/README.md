# Dimensionality Experiments

This directory preserves exploratory scripts and verification notes for the
dimensionality working note. These files are not final simulations or proofs.
They are part of the audit trail for the question of whether `3+1`
dimensionality can be derived or reconstructed within VED.

## Reading Rule

Treat these files as research traces:

- a failed route is evidence about where assumptions enter;
- a numerical probe is a dynamic sketch, not empirical verification;
- a script name with a version number marks iteration history, not a stable
  API.

For a bounded interpretive summary of the current experiment cycle, start from
[the reports directory](../reports/) before drilling into these logs.

## File Groups

| Group | Files | Role |
|---|---|---|
| Growth-route iterations | `growth v2.py` through `growth v24.py`, plus variants such as `growth v15b soc.py`, `growth v17c.py`, and `growth v24 betti.py` | Iterative probes of growth, closure, and topological signature formation |
| v24.1 instrument re-reading | `growth_v24_1_instruments.py`, `v24_1_runs/` | Read-only diagnostic re-reading of v24 for BSW exit reasons, SW breakdown, multi-support β1, SCC structure, reflection rate, and edge lifetimes |
| v24.2 headroom runs | `growth_v24_2_headroom.py`, `v24_2_headroom_runs/` | Headroom scan separating BSW behavior from NMAX saturation while adding scaling-width and support-ladder diagnostics |
| v24.2e extended-epoch runs | `growth_v24_2e_extended.py`, `v24_2e_extended_runs/` | Extended-epoch diagnostic run adding edge evaporation, S-support density, and path-redundancy instruments |
| v24.3 rule decomposition | `growth_v24_3_rules.py`, `v24_3_rules_runs/` | Two-by-two rule decomposition separating self-feeding and fanout effects |
| Campaign A cycle tracking | `growth_campA_cycles.py`, `campA_repair_turnover.py`, `campA_cycle_runs/` | TD/TL2 cycle-individual tracking for lifetime, death attribution, overlap degeneracy, and repair/turnover decomposition |
| Campaign support tools | `phase_classifier_v1.py`, `band_fate_judge.py`, `lattice_anchor_ext.py`, `campaign_tools_README_ja.md` | Local phase classification, band-fate adjudication, and d_cal anchor recalibration tools for later campaigns |
| Betti / topological checks | `betti repro.py`, `growth v24 betti.py`, `repro.tsv`, `betti_verification_v24.md`, `topological_signatures_of_registration.md` | Attempts to track whether registration leaves topological signatures |
| Route 2 attempts | `route2 v1 deprecated.py`, `route2 v2.py` | Alternative route, with the first version explicitly preserved as deprecated |
| Auxiliary probes | `ball dim.py`, `band closure.py`, `phase scan.py`, `dell.py`, `growth model.py` | Smaller probes used during route exploration |

## Current Topological Audit

The strongest current numerical checkpoint is the v24 per-event Betti audit:

- [Topological signatures of registration](topological_signatures_of_registration.md)
  explains why the v24 T1 rule should be read as irreversible triangular
  insertion rather than ordinary subdivision.
- [Betti verification v24](betti_verification_v24.md) records the verification
  context.
- [repro.tsv](repro.tsv) preserves the per-seed machine-readable record.

The result is limited to the v24 model family. It identifies a concrete
topology-generating registration rule, not a completed derivation of `3+1`
dimensions.

## v24.1 Instrument Re-Reading

The v24.1 re-reading keeps the v24 dynamics fixed and adds read-only
instruments for BSW exit reasons, SW failure breakdown, fit quality,
multi-support β1, directed SCC structure, reflection fallback rate, and edge
lifetimes.

Primary files:

- [growth_v24_1_instruments.py](growth_v24_1_instruments.py)
- [v24_1_runs/](v24_1_runs/)
- [v24_1_runs summary](v24_1_runs/README.md)

These runs are diagnostic. They should not be read as MRW detection or as a
derivation of observed dimensionality.

## v24.2 Headroom Runs

The v24.2 headroom run raises `NMAX` to test whether the v24.1 directed BSW
behavior survives without capacity saturation and T1 shutdown.

Primary files:

- [growth_v24_2_headroom.py](growth_v24_2_headroom.py)
- [v24_2_headroom_runs/](v24_2_headroom_runs/)
- [v24_2_headroom_runs summary](v24_2_headroom_runs/README.md)

In the first `NMAX=1200` scan, no run reached capacity. Directed runs retained
many more BSW snapshots than the symmetric control, including 52 snapshots at
the stricter `npts >= 5` threshold. This is still diagnostic evidence, not a
causal decomposition or MRW detection.

## v24.2e Extended-Epoch Runs

The v24.2e run extends the headroom setting to 1500 epochs and adds
path-redundancy diagnostics to test whether contraction-phase BSW is tree-like
thinning or a thinner but still redundant readability band.

Primary files:

- [growth_v24_2e_extended.py](growth_v24_2e_extended.py)
- [v24_2e_extended_runs/](v24_2e_extended_runs/)
- [v24_2e_extended_runs summary](v24_2e_extended_runs/README.md)

In the first `NMAX=2000`, 1500-epoch scan, directed runs retained BSW across
all six seeds, including 295 snapshots at `npts >= 5`. Contraction-phase BSW
kept high 2-edge-connected occupancy while having lower mean degree and fewer
S-support edges than non-BSW contraction snapshots. This should be read as a
diagnostic result, not as MRW detection.

The weight-export rerun adds snapshot TSVs and robust-BSW `-log(S)` weight
pools. Under non-periodic, size-matched, empirical-weight anchors, the old
v24.2e `d_cal` median around 2.70 recalibrates to a median near 2.34. The
adjudicated 2b phase-classifier scan finds a reproducing region on the
mechanically selected unimodal subset and locks the standard setting
`window_ratio=0.4`, `eps_ratio=0.75`.

## v24.3 Rule Decomposition

The v24.3 rule decomposition keeps the campaign setting fixed and separates
self-feeding and fanout effects across four rule cells.

Primary files:

- [growth_v24_3_rules.py](growth_v24_3_rules.py)
- [v24_3_rules_runs/](v24_3_rules_runs/)
- [v24_3_rules_runs summary](v24_3_rules_runs/README.md)

In the first `NMAX=2000`, 900-epoch scan, no cell reached saturation. The
pre-registered interaction test was negative: self-feeding shortened median
edge lifetime in both the one-sided and two-sided contexts. The directed cell
still retained the strongest robust BSW count among the four cells. This is a
rule-decomposition diagnostic, not a completed causal derivation of MRW. The
fanout axis remains partly entangled with state size, so the readability
difference should not yet be explained as simple dilution.

The directed robust-BSW snapshots were rerun with one-value-per-line `-log(S)`
weight export. A non-periodic, size-matched, empirical-weight anchor table
places the measured slope corresponding to old `d_cal≈3.43` below the 3D anchor
for the sampled V range. Under that faithful convention, the same snapshots
calibrate to approximately `d≈2.72..2.93`, not to a 3.4-dimensional reading.

## Campaign Support Tools

The local phase classifier and band-fate judge are preserved as campaign
instruments rather than as theoretical claims.

Primary files:

- [phase_classifier_v1.py](phase_classifier_v1.py)
- [band_fate_judge.py](band_fate_judge.py)
- [lattice_anchor_ext.py](lattice_anchor_ext.py)
- [campaign_tools_README_ja.md](campaign_tools_README_ja.md)

The first smoke application to a v24.3 directed run produced an `UNDECIDED`
band-fate result, which should be read as a request for a longer or better
targeted run rather than as evidence for extinction, steady persistence, or
breathing.

## Campaign A Cycle Tracking

Campaign A runs the TD/TL2 cycle-individual tracker on the locked
`g=0.075`, `NMAX=2000`, 900-epoch, six-seed setting.

Primary files:

- [growth_campA_cycles.py](growth_campA_cycles.py)
- [campA_repair_turnover.py](campA_repair_turnover.py)
- [campA_cycle_runs/](campA_cycle_runs/)
- [campA_cycle_runs summary](campA_cycle_runs/README.md)

The first full run separates cycle persistence and death attribution across
TD and TL2. TD has longer median cycle lifetime and a much higher fraction of
deaths attributed to newly inserted edges; TL2 has shorter median cycle
lifetime and more path-side attribution. The repair/turnover decomposition
remains under-sampled in this 900-epoch run because the locked phase
classifier detects only two consolidation windows across all twelve runs.

The imported TD seed-5 4000-epoch reconciliation run connects Campaign A to
the 2c trajectory. Its raw Jaccard window score indicates turnover, but
age-conditioned survival correction shows consolidation-phase hazard
suppression. This reframes the repair/turnover distinction as
phase-dependent cycle-hazard modulation.

## Caution

The presence of a script does not mean that the corresponding route survived.
Several scripts are intentionally retained because they failed in informative
ways. Before using any numerical output as support for a claim, check the
Japanese working note and the verification notes for the route status.

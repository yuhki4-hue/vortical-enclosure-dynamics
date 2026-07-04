# Simulation Reading Guide

This guide explains how to read the Python simulations in the VED repository,
especially the Vol.4 dynamic-barrier simulations.

## Status of the Simulations

The Python simulations are conceptual simulations and dynamic diagrams. They are
intended to make specific structural behaviors visible.

They are not:

- direct physical simulations,
- empirical verification of VED,
- proof that nature uses the exact equations in the scripts,
- a replacement for quantitative derivation or experimental comparison.

The simulations should be read as exploratory models for reasoning about
non-closure, feedback, dissipation, and barrier-like behavior.

The repository also contains a separate
[Stochastic Quantization module](../../stochastic-quantization/). That module
is more quantitative than the Vol.4 dynamic-barrier diagrams: it tests a
χ-layer Langevin bridge, propagators, emergent light cones, two-field cone
mixing, and a re-addressing gauge sector. It is still a working note and should
not be read as a completed derivation of the Standard Model action or empirical
validation of VED.

### Common Advanced Misreading

Misreading:

- The simulations model biological self-organizing systems.

Clarification:

- The simulations are intended as minimal demonstrations of barrier formation,
  differential horizons, non-closure dynamics, and boundary signaling.
- Biological systems are only one possible realization.
- The simulations should not be reduced to biological self-organization models.

## Vol.4 Dynamic-Barrier Simulations

The Vol.4 barrier-term simulations illustrate dynamic non-closure and
barrier/dissipation behavior. Their core role is to show how apparent
barrier-like behavior can be studied through feedback, rotational terms,
dissipation, and observation windows.

Primary locations:

- [Vol.4 dynamic barrier section](../../paper/vol4/sections/dynamic_barrier.tex)
- [Simulation directory](../../paper/vol4/simulations/)
- [Baseline dynamic barrier model](../../paper/vol4/simulations/dynamic_barrier_model.py)
- [Dissipation scan](../../paper/vol4/simulations/dynamic_barrier_D_scan.py)
- [Phase diagram](../../paper/vol4/simulations/dynamic_barrier_phase_diagram.py)
- [Energy-balance diagnostics](../../paper/vol4/simulations/dynamic_barrier_energy_balance.py)
- [Critical-D analysis](../../paper/vol4/simulations/dynamic_barrier_critical_D_no_rotation_damping.py)
- [Observation-window diagnostics](../../paper/vol4/simulations/dynamic_barrier_windows.py)

## Stochastic Quantization Module

The stochastic-quantization module is an exploratory quantitative attempt to
rewrite the VED/IFGT closure equation in the unbounded χ chart and compare the
resulting Langevin dynamics with stochastic quantization.

Primary locations:

- [Module README](../../stochastic-quantization/README.md)
- [Japanese README](../../stochastic-quantization/README_ja.md)
- [Phase 2 stationary propagator script](../../stochastic-quantization/simulate.py)
- [Phase 3 emergent light-cone script](../../stochastic-quantization/simulate_phase3.py)
- [Collins two-field probe](../../stochastic-quantization/simulate_collins.py)
- [Phase 4 re-addressing gauge-sector script](../../stochastic-quantization/simulate_phase4.py)

Read this module as:

- a working quantitative bridge,
- an audit-ledger of what has and has not been displaced,
- a set of reproducible numerical probes,
- an open-problem generator.

Avoid reading it as:

- a completed derivation of the Standard Model action,
- empirical confirmation of VED,
- proof that nature uses the exact simulated equations,
- a replacement for the Vol.1-Vol.4 derivations.

## How to Read the Outputs

| Output Type | Intended Reading | Avoid Reading As |
|---|---|---|
| Time-series plots | Visualizations of modeled closure, velocity, and rotational feedback. | Measured physical trajectories. |
| Phase diagrams | Qualitative regime maps under chosen model assumptions. | Empirical phase diagrams of nature. |
| Critical-D scans | Diagnostics of dissipation-dependent stabilization in the model. | A measured universal physical constant. |
| Energy-balance plots | Bookkeeping for model terms and feedback behavior. | Complete physical energy accounting. |
| Observation-window plots | Tests of how behavior appears through limited descriptive windows. | Direct proof of an observational ontology. |

## Interpretation Boundary

The simulations support internal conceptual exploration of the Vol.4 framework.
They do not close the open problems of microscopic derivation, empirical
validation, or standard-theory equivalence. Those remain open unless addressed
in the relevant papers or future work.

For broader interpretation safeguards, see [Common Misreadings](common_misreadings.md).

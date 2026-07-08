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

## File Groups

| Group | Files | Role |
|---|---|---|
| Growth-route iterations | `growth v2.py` through `growth v24.py`, plus variants such as `growth v15b soc.py`, `growth v17c.py`, and `growth v24 betti.py` | Iterative probes of growth, closure, and topological signature formation |
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

## Caution

The presence of a script does not mean that the corresponding route survived.
Several scripts are intentionally retained because they failed in informative
ways. Before using any numerical output as support for a claim, check the
Japanese working note and the verification notes for the route status.

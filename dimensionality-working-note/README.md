# Dimensionality Working Note

Japanese title: 次元選択ワーキングノート

This module collects a working investigation into what "dimension" means
inside the VED research tree. The initial motivating question was whether the
observed `3+1` dimensional structure could be derived within VED rather than
assumed as a background container. The current material is not a completed
derivation. It is a research log that keeps successful reductions, failed
routes, residual audits, and exploratory numerical probes visible.

## Status

This is a working-note module.

- It does not establish a final VED derivation of `3+1` dimensions.
- It treats failed definitions and failed simulations as part of the audit
  trail.
- It distinguishes conceptual progress from numerical confirmation.
- It now has a bounded public summary layer in [reports/](reports/) for the
  current dimensionality-selection experiment cycle.
- It should be read together with the VED core sequence, Vol.2 closure
  geometry, Vol.4 audit discipline, and the stochastic-quantization module.

## Core Question

The guiding question is:

```text
Can dimensionality be read as an effective description of persistent
difference structure, rather than as a primitive container?
```

The Japanese working note develops this by shifting the question from
"why is the world `3+1` dimensional?" to "what kind of registered difference
structure makes a dimensional description stable?"

## Current Working Position

The current note treats dimension as an effective rank of describable
difference structure. In this reading, dimension is not first an ontology of
space, but an operational description of how differences remain registered,
linked, and transportable.

The note also distinguishes two kinds of dimensionality:

- relational or base-space dimensions, which describe linkage and transport
  among registered differences;
- state or fiber dimensions, which describe internal degrees of freedom over
  those relations.

This distinction is part of the working route. It is not presented here as a
settled theorem.

## Recent Topological Verification

The current strongest numerical result is not a derivation of `3+1`
dimensions. It is a per-event topological audit of the v24 growth model.

In that model, the transition rule that produces metric windows is not an
ordinary subdivision. It is an irreversible triangular insertion: one
registration event preserves the existing edge while adding a new node linked
to both endpoints. In the measured v24 runs, this produces one new vertex and
one new cycle in the same event.

This has been checked by per-event Betti accounting across multiple seeds and
system sizes. The result is currently limited to the v24 model family, but it
identifies a topology-generating registration rule that can be tested further.
See [Topological Signatures of Registration](experiments/topological_signatures_of_registration.md)
and the machine-readable per-seed record [repro.tsv](experiments/repro.tsv).

## Current Public Summary

The current stopping point for the dimensionality-selection experiment cycle
is summarized in:

- [Reports index](reports/)
- [Working Note II experimental summary report](reports/ved-note2-report.html)

The report is a reading layer over the working notes and experiment logs. It
does not replace the raw logs or establish a completed derivation of observed
dimensionality. It is intended to make the current audit state readable before
the next experiment cycle begins.

## What Is Preserved Here

| Material | Location | Role |
|---|---|---|
| Current public reports | [reports/](reports/) | Bounded summary layer for the current dimensionality-selection cycle |
| Full Japanese working note | [README_ja.md](README_ja.md) | Main research log and current argument state |
| Japanese working note II | [README_II_ja.md](README_II_ja.md) | Continuation from registered difference to metric readability |
| Early Japanese note | [archive/dimensionality_working_note_ja_initial.md](archive/dimensionality_working_note_ja_initial.md) | Earlier snapshot preserved for provenance |
| Numerical and topological probes | [experiments/](experiments/) | Scripts, TSV output, verification notes, failed routes |
| Experiment index | [experiments/README.md](experiments/README.md) | Guide to the prototype scripts and failure logs |

## How To Read The Failure Logs

The scripts and route files in this module are not polished simulations. They
are records of attempts to make the dimensionality question more concrete.
Some were abandoned because they imported dimensional assumptions too early.
Some failed because candidate invariants collapsed under re-addressing or
discrete-relational checks. Those failures are kept intentionally because they
show where a derivation would otherwise hide an assumption.

In this sense, the module follows the same audit discipline used in the
stochastic-quantization module: when a route fails, the failure should remain
named rather than disappearing into a stronger-looking claim.

## Relation To VED

The module is best read as an exploratory extension of the VED core sequence:

```text
difference -> closure degree C_ij -> gradient -> flow -> vortex -> enclosure
-> non-closure
```

It asks whether dimensionality can be reconstructed from the persistence,
registration, and transport of difference within that sequence. It does not
add dimensionality as a new axiom.

## Related Modules

- [VED Generative Sequence](../docs/navigation/generative_sequence.md)
- [Stochastic Quantization Module](../stochastic-quantization/)
- [Vol.2 Closure Geometry](../paper/vol2/)
- [Vol.4 Differential Horizon](../paper/vol4/)

## License

Unless otherwise noted, this module follows the repository license: Creative
Commons Attribution 4.0 International License (CC BY 4.0).

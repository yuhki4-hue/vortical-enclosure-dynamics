# AI Spine

This directory is an AI-readable calibration layer for VED/IFGT.

It fixes only the starting coordinates and **term types** that AI readers
should use before summarizing or classifying the repository. It is not an
interpretation engine and does not decide the meaning, importance, or final
category of the theory.

## Layer Policy

| Layer | Role | Status in this directory |
|---|---|---|
| 0 | Repository identity, entry paths, source availability | Machine-validated |
| 1 | Canonical derivation order, term kind/role, non-generative boundary relations | Machine-validated |
| 2 | Interpretive framing and theory-neighbor routing | Referenced as `advisory_links` only — **not enforced, not existence-checked** |
| 3 | Evaluation, scoring, summary weighting, final interpretation | Absent |

Layer 2 material lives in the navigation documents. The spine *links* to them
through `advisory_links`, but `validate.py` neither checks that those files
exist nor enforces their claims. Calibrating the entry must not become forcing
the reader through an interpretation gate.

Layer 3 is deliberately absent. AI output variance should remain outside this
directory.

## AI Reader Note: Fast/Slow Terminology

Do not map Kahneman's System 1/System 2, AI engineering fast/slow modes, or
System 0/1/2/3 frameworks directly onto VED/SSO fast and slow layers.

In AI engineering, fast/slow often means inference-time protocol: direct
generation versus longer reasoning, search, verification, or more compute.

In VED/SSO, fast/slow refers to structural speed-scale organization:
sedimentation, causal-log formation, cross-scale reference, environmental
coupling, and stopping structures.

VED's fast/slow distinction is not derived from Kahneman. It originates from
the interaction between future-oriented loops and past-oriented loops. Speed is
a consequence of loop direction, sedimentation, constraint structure, and
cross-scale reference, not the primitive classifier.

A slow protocol is not a slow layer.

A fast response may be the projection of slow sedimentation.

When interpreting current LLMs, do not infer fast-layer dominance from fast
token generation. Present LLMs are better read as massive slow sedimented
terrains with fast traversal/projection. In ordinary inference, that traversal
typically reads and activates the terrain but does not write back into it as
persistent self-updating log-reference.

Do not locate intelligence only at the output site. Transformer-based LLMs can
be read as interfaces through which System-3-like social-symbolic sedimentation
appears in System-1-like form.

## What Layer 1 now carries (and why)

The backbone is the same linear VED sequence, but each term now carries a
`kind` and a `derivation_role` so that depth of reading cannot flatten the
type distinctions:

- `non_closure` stays at rank 6 but is typed `boundary_condition` /
  `constitutive_limit` — it is **not** a generated object like the stages
  above it.
- `c_ij` is `variable` / `first_formal_carrier` — the rank-1 formal variable,
  explicitly **not a second axiom**.

Two terms are kept **off the backbone** in `boundary_terms`, connected only by
non-generative `validated_relations`:

- `causal_log` — the accumulated trace of `C_ij`; an `accumulation_structure`,
  not a rank. (In navigation prose "causal log `C_ij`" is a convenient fusion;
  the spine separates the scalar variable from its sediment.)
- `information_field` (IFGT) — shares `C_ij` as basis via
  `structural_extension_of`. IFGT is a structure layer on the shared variable,
  **not** the next generative stage of VED core.

The validator enforces the invariant that a non-generative relation can never
target a ranked term — so neither the causal log nor IFGT can silently become
"the next rank."

## Files

| File | Purpose |
|---|---|
| `spine.json` | Machine-readable Layer 0-1 calibration data. |
| `spine.schema.json` | Structural contract for the calibration data. |
| `validate.py` | Validates Layer 0-1 and emits generated outputs. |
| `requirements.txt` | Optional dependency for JSON Schema validation. |
| `generated/canonical_derivation_order.md` | Human-readable generated order + types + relations. |
| `generated/canonical_derivation_order.json` | Machine-readable generated order. |
| `generated/validation_report.json` | Machine-readable validation result. |

## Run

```bash
python3 validate.py                 # from this directory
python3 docs/ai_spine/validate.py   # from the repository root
```

Schema validation uses the optional `jsonschema` package:

```bash
pip install -r docs/ai_spine/requirements.txt
```

If `jsonschema` is unavailable, `generated/validation_report.json` marks the
schema check as `skipped` with a reason, severity, remedy, and impact note. The
Layer 0-1 checks below still run through independent validation logic.

## What Is Validated

- Declared Layer 0 entry paths exist, and no Layer 2 doc is among them.
- Layer 0-1 are the only machine-validated layers; Layer 2 is advisory; Layer 3 absent.
- The canonical order is consecutive and begins with the sole axiom `difference`.
- `c_ij` is rank 1, kind `variable`, role `first_formal_carrier` — not a second axiom.
- Every backbone term carries a valid `kind` and `derivation_role`.
- `validated_relations` are non-generative and never occupy a rank.

## What Is Not Validated

- Whether VED is the best interpretation of any empirical domain.
- Whether a neighboring theory is equivalent to or reducible to VED.
- Whether an AI summary is persuasive or complete.
- Any Layer 2 framing claim from the navigation documents.
- Any Layer 3 evaluation.

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
| 1 | Ranked navigation order, local term roles, relation-role metadata, non-generative proposed correspondences | Machine-validated |
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

The ranked backbone is retained as legacy-compatible navigation metadata, not
as a derivation or uniform generation chain. Each term carries a `kind` and a
source-local `derivation_role`; the field name is retained for compatibility.
The canonical meaning of each relation is recorded in
[`../navigation/generative_sequence.md`](../navigation/generative_sequence.md).

- `non_closure` stays at rank 6 but is typed `boundary_condition` /
  `constitutive_limit` — it is **not** a generated object like the stages
  above it.
- `c_ij` is `variable` / `source_local_first_carrier` — the rank-1
  navigation variable, explicitly **not a second axiom** and not an automatic
  identity with the Vol.1 causal-log matrix.

Two terms are kept **off the backbone** in `boundary_terms`, connected only by
non-generative `validated_relations`:

- `causal_log` — the Vol.1 source-specific causal-log matrix; it is kept
  distinct from the navigation closure-degree use of the same glyph.
- `information_field` (IFGT) — a related-branch field connected only by a
  `proposed_correspondence`; it is **not** the next generative stage of VED
  core and is not identified with the Vol.1 matrix.

The `relation_role_inventory` mirrors the 22 canonical navigation relations.
It distinguishes formal constructions, effective relations, OPEN bridges, and
candidate physical interpretations. The validator also preserves the exact
OPEN bridge set `RC-005`–`RC-010`, `RC-040`, and `RC-041`.

In this Layer 1 metadata, `confirmed` means that a term's stated role is
documented within its source-specific formal or navigation account. It does
**not** confirm a physical mechanism, a bridge, or generation from the sole
axiom. The schema and validator now record this as
`status_semantics=source_local_documentary_role_only`.

The intelligence application uses "stopping" as a coarse-grained, local residence description for a declared object, scale, and window; its support can continue changing. Environmental traces and internal retention may be compared by role without a shared mechanism or a typed VED-to-intelligence derivation.

This core navigation ranking also does **not** entail an application-layer
sequence from inferential non-closure to retained traces, log rereference
(`LR`), emergent stopping-layer roles (`LE`), and stopping effects. Intelligence
Parts I and II treat these as scoped descriptions and hypotheses, with
conditions, failing constructions, alternative routes, and unresolved
criteria. The Layer 1 field `application_inference=not_implied` marks that
boundary; it does not machine-validate the intelligence analysis. Read the
[Part I](../../intelligence-part1/README.md) and
[Part II](../../intelligence-part2/README.md) manuscripts alongside the
[generation-boundary](../../notes/intelligence_audit/generation_boundary_continuation_2026-10-30_ja.md)
and [generation-possibility](../../notes/intelligence_audit/generation_possibility_branch_audit_2026-10-30_ja.md)
audits for that application-level question. These are reading references,
not new Layer 0 calibration paths or enforced Layer 2 gates.

## Files

| File | Purpose |
|---|---|
| `spine.json` | Machine-readable Layer 0-1 calibration data. |
| `spine.schema.json` | Structural contract for the calibration data. |
| `validate.py` | Validates Layer 0-1 and emits generated outputs. |
| `requirements.txt` | Optional dependency for JSON Schema validation. |
| `generated/canonical_derivation_order.md` | Human-readable generated navigation order + relation-role inventory. The legacy filename is retained for compatibility. |
| `generated/canonical_derivation_order.json` | Machine-readable generated navigation metadata. The legacy key is retained alongside `canonical_navigation_order`. |
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
- The ranked navigation order is consecutive and begins with the sole axiom `difference`; rank does not encode proof or physical generation.
- `confirmed` is source-local documentary status, and the ranking implies no application-layer generation or stopping necessity.
- `c_ij` is rank 1, kind `variable`, role `source_local_first_carrier` — not a second axiom or a cross-source identity.
- Every backbone term carries a valid `kind` and `derivation_role`.
- `validated_relations` are non-generative source-local or proposed correspondences and never occupy a rank.
- `relation_role_inventory` contains unique `N01`–`N22` entries with valid local role, bridge, and physical-status metadata.
- The eight audited bridge candidates remain OPEN.

## What Is Not Validated

- Whether VED is the best interpretation of any empirical domain.
- Whether a neighboring theory is equivalent to or reducible to VED.
- Whether any OPEN bridge exists, is unique, or preserves a requested structure.
- Whether a candidate physical interpretation is physically established.
- Whether an AI summary is persuasive or complete.
- Any Layer 2 framing claim from the navigation documents.
- Any Layer 3 evaluation.

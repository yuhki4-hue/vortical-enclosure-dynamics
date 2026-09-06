# Proof-Formation Coder Instructions v0.1.1

**Status:** protocol-calibrated instructions for a qualitative reconstruction test  
**Scope:** coding only; not a theorem, taxonomy extension, score, or agreement measure

This version replaces v0.1 only for future coding runs. It leaves the frozen corpus, its excerpts and order, M1–M17, and all adjudication expectations unchanged. Reader 01 was a pilot/calibration reader and is not part of the formal inter-reader reader count.

## Reader isolation

Read only this file and `proof_formation_frozen_toy_corpus_v0.1.md`. Return to an original source only when its path is given in the frozen corpus and the excerpt is insufficient. Do not read adjudication rules, any answer key, the meta-experiment document, trajectory summaries, calibration notes, or another reader's output.

Do not fill gaps with outside knowledge or general expectations about how proofs normally work. Use `UNKNOWN`, `AMBIGUOUS`, `NOT APPLICABLE`, or multiple codes when the source does not support a unique reconstruction.

## Coding order

### Step 0 — Segment the episode before coding any move

Treat a frozen corpus item (`E01`–`E12`) as a container, not automatically as one analytic episode. First identify the smallest source-supported before/failure-or-obstacle/move/after transition or decision sequence.

- Keep the parent item ID and assign subepisode IDs such as `E02-a`, `E02-b` when one item contains more than one transition.
- Do not force a universal-claim withdrawal, a retained side claim, and a later empirical proposal into one block merely because they occur in one corpus item.
- Do not split only to make a preferred move code fit.
- If two segmentations remain source-compatible, record both under `alternative_segmentations` and mark the boundary `AMBIGUOUS`. Do not silently count duplicated text as two independent results.
- Move coding begins only after this segmentation record is made.

### Step 1 — Fix claim identity and obligation

Write the claim as nearly as possible in the source's own terms. State its target, quantifier strength, domain or object class, formula or language class, and required conclusion. A nearby fallback, side claim, or implementation lemma is not the same claim merely because it occurs in the same passage.

Choose an `obligation_type` only when supported: formal theorem, proof step, interpretation or reduction, empirical claim, comparative claim, design decision, literature/novelty claim, or `UNKNOWN`/`AMBIGUOUS`.

### Step 2 — Separate dependency roles

- `assumptions`: conditions under which the claim is asserted. These alter the statement's admissible cases or hypotheses.
- `proof_or_evidence_resources`: means used to discharge or investigate the obligation—lemmas, codings, translations, proof procedures, data, controls, audits, or experimental materials. They do not become theorem assumptions merely because the proof needs them.
- `evaluation_or_decision_rules`: rules for deciding success, failure, retention, demotion, termination, or comparison. Examples include a falsification threshold stated in words, a preregistered stopping rule, a novelty criterion, or a rule for retaining only a finite comparative claim. This field is especially important outside formal theorem cases. It is neither a theorem assumption nor evidence itself.

If a source item can genuinely play more than one role and the text does not resolve the role, record `AMBIGUOUS`; do not duplicate it across fields as if the roles were settled.

### Step 3 — Record failure and branches

- `failure_witness`: the counterexample, prior-art result, logical objection, missing condition, type error, or empirical observation that blocks the coded `claim_before`. Do not substitute a general criticism for a source-local witness.
- `available_branches`: repairs or alternatives that the source explicitly makes available but does not take in this subepisode, including an explicitly rejected rescue. Availability may be `UNKNOWN`; do not invent a branch from general knowledge.
- `adopted_side_claims`: a separately identified claim that the source actually retains or adopts after the original claim is withdrawn or demoted. Give it its own claim ID and use that same ID under `claim_after` and `terminal_status`. Adoption is not merely availability, and a side claim does not count as preserving the original claim's identity without source support.

### Step 4 — Code moves, after-claims, and status

Code only an operation actually taken between the fixed before and after claims. Several M-codes may be used when several source-supported operations occur. A counterexample or prior-art item is normally a trigger or witness, not itself the move.

When there is more than one `claim_after`, label them `A1`, `A2`, and so on. Give every after-claim its own `terminal_status`; do not assign one blended status to claims with different outcomes. Status vocabulary may follow the source, for example retained, conditional, demoted, withdrawn, terminated, negative result fixed, open, or `UNKNOWN`/`AMBIGUOUS`.

Apply provenance at the smallest practical unit:

- `SOURCE-DERIVED`: stated or directly entailed by the cited excerpt/source.
- `INFERENCE`: reconstruction needed to connect source statements; state the inferential step.
- `OPEN HYPOTHESIS`: a prospective possibility explicitly left open, not a fact supplied by the coder.

## M1–M17 concise codebook

The codes below are frozen. Do not add a code or change a definition.

| Code | Move | Use / exclusion boundary |
|---|---|---|
| M1 | Assumption strengthening | Add or strengthen conditions of the theorem or claim. Do not use for the conclusion itself, a proof resource, or a hidden ambient convention. |
| M2 | Conclusion weakening | Weaken quantification, precision, uniqueness, necessity, or generality of the conclusion. Do not use for mere paraphrase or only changing the object class. |
| M3 | Formula-class / language restriction | Restrict formulas or language, such as a complexity class, closed sentences, or same-language statements. Do not use for an object/model class or for the result of a conservation proof. |
| M4 | Object / domain / model-class restriction | Narrow the objects, models, dimension, finiteness condition, candidate class, or artifact corpus. Do not use for a formula fragment or proof resource. |
| M5 | Quotient / equivalence-class target reformulation | Change the target from a representative to an observational, gauge, or interpretability equivalence class. Do not use for unresolved ambiguity or generic weakening. |
| M6 | Formal theory extension | Move from a theory to that theory plus an axiom/schema, a later progression stage, or a truth-expanded language. Do not report the extension's result as proved by the original theory. |
| M7 | Model / estimand / target-class revision | Replace or enrich a model, jointly estimate nuisance structure, or change the estimand/target class. Do not confuse this with formal theory extension or with claiming that the original failure disappeared. |
| M8 | Proof-resource addition or route change | Add a lemma, coding, compactness argument, cut elimination, experimental design, or evidential material. This changes the route/resources, not the claim's assumptions. |
| M9 | Reduction with specified preservation | Map the obligation to another calculus or progression while specifying what consequence class is preserved. Do not infer theory equality or full equivalence. |
| M10 | Interpretation / translation | Compare formulas, models, or theories through an explicit translation. Do not use for unmediated same-language theorem inclusion. |
| M11 | Internalization | Represent syntax, proof, substitution, or a related relation inside the object language/theory. Do not equate this with semantic truth, external soundness, or self-proof. |
| M12 | Metalevel shift / external evaluation | Move evaluation of truth, soundness, well-foundedness, consistency, or non-provability to a metatheory. Do not use for an internal formula/schema; combine with M6 when a reflection extension is actually added. |
| M13 | Comparison / calibration | Move the question to conservativity, interpretability, relative consistency, reflection rank, or ordinal analysis. Do not infer a universal scalar of strength or equality of theories from a shared ordinal. |
| M14 | Disambiguation / type correction | Separate truth from provability, local from uniform/global, stage/modality/ordinal, or artifact/institution/field. Do not use merely because a claim becomes stronger. |
| M15 | Prior-art absorption | Return an original claim or vocabulary to an existing theorem, method, standard, or review language. This does not by itself establish historical causality or erase all residual value. |
| M16 | Conversion to empirical / comparative question | Replace a theorem/framework-novelty target with a control comparison, document audit, or finite test. Do not code a theorem proof or a mere illustration this way. |
| M17 | Withdrawal / abandonment / negative-result fixation | Withdraw, demote, terminate, or freeze a negative verdict. Do not use for resurrection under a new name or for calling an untested claim refuted. |

### M3 versus M4

Ask what the restriction ranges over.

- If it changes which formulas, sentences, syntactic complexity classes, or languages are admitted, use M3.
- If it changes which mathematical objects, models, dimensions, finite instances, candidate artifacts, or corpora are admitted, use M4.
- If both restrictions are explicit, both codes may apply, but each must cite its own before/after change.
- If the source says only “restrict the class” without fixing whether it is a formula/language class or an object/model class, use `AMBIGUOUS (M3/M4)` rather than guessing.

## Items that are not automatically moves

R0/R1/R2 resource labels, theorem assumptions, proof resources, evaluation rules, counterexamples, failure witnesses, prior-art references, and status labels are not automatically M-codes. A source-local label such as “M1” must not be confused with formation code M1. A completed proof type is not automatically the operation that made the obligation closable.

## Required submission block

Repeat the block for each source-supported subepisode. If no split is made, use the parent corpus ID as `subepisode_id`.

```text
parent_corpus_item:
subepisode_id:

episode_boundary:
alternative_segmentations:

claim_identity:
claim_before:
target_and_scope:
obligation_type:

assumptions:
proof_or_evidence_resources:
evaluation_or_decision_rules:

failure_witness:
available_branches:
adopted_side_claims:

move_taken:
claim_after:
  A1:
  A2:                       # omit unused labels
terminal_status:
  A1:
  A2:                       # one status per after-claim

provenance_label:
  claim_before:
  episode_boundary:
  dependencies:
  failure_witness:
  available_branches:
  adopted_side_claims:
  move_taken:
  claim_after_and_status:

degenerate_or_target_leakage:
source_excerpts_used:
uncertainties:
```

Do not create a score, rank, geometric representation, general law, or new move code. The output is a qualitative reconstruction, and unresolved records are valid results.

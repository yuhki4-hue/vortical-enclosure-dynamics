# Proof-Formation Non-Nested Frame Family Replication Test v0.1

Date: 2026-09-06  
Status: exploratory finite-propositional replication / stress record  
Scope: the unchanged frozen histories H1–H10, C-F, and C-D

## 0. Status / posture

This document is:

- an **exploratory replication / stress test**;
- **not a theorem**;
- **not an observability theorem**;
- **not a new framework**;
- **not a v0.2 proposal**;
- **not a canonical frame family**;
- **not a validation of R0–R4**;
- **not a claim that non-nested frames are more realistic**;
- **not a claim that reproduced transitions are universal**;
- **not a claim that failed replication falsifies the underlying history**;
- a test with **no new move codes**;
- a test with **no score**, **no optimization**, and **no ranking**;
- a test with **no metric** and no geometry, topology, or lattice;
- **not a generalization beyond the frozen finite histories**.

The central question is:

> Given the same frozen histories, do pairwise visibility patterns persist, reverse, disappear, or reorganize under a non-nested frame family?

The N-family below is test-local. It is deliberately constructed so that a later displayed frame does not generally inherit all fields of an earlier one. The test compares projection behavior; it does not design a preferred observation architecture or alter the histories used by the prior tests.

## 1. Frozen histories reused unchanged

No new history is added. The existing finite setting remains

\[
V=\{p,q\},\qquad
\Omega=\{\omega_{00},\omega_{01},\omega_{10},\omega_{11}\},
\]

with the common before-state

\[
H_0=\{p\lor q\},\qquad C_0=p,
\qquad E(H_0,C_0)=\{\omega_{01}\}.
\]

The frozen records are exactly those supplied by the existing record-frame checker:

| History | Unchanged meaning |
|---|---|
| H1 | Add \(\neg q\); same-id continuation; established; provenance `INDEPENDENT` |
| H2 | Restrict \(S\) to \(\Omega\setminus\{\omega_{01}\}\); same-id continuation; established; provenance `UNKNOWN` |
| H3 | Replace \(C\) by \(p\lor q\); same-id continuation; established; provenance `UNKNOWN` |
| H4 | No semantic repair; original withdrawn; no successor; provenance `INAPPLICABLE` |
| H5 | Original \(x_0\) withdrawn; successor \(x_1\) with \(H_0\cup\{\neg q\}\models p\) established |
| H6 | Same mathematical after-material as H5; \(x_0\) continues and is established |
| H7 | Add \(\neg\neg p\); established; provenance `UNKNOWN` |
| H8 | Add \(\top\); evaluated semantic state unchanged; failed; provenance `UNKNOWN` |
| H9 | Add \(p\lor\neg q\) as a post-hoc exact filter; established; provenance `POST_HOC` |
| H10 | Same formulas and transition as H9; provenance stipulated `INDEPENDENT` |
| C-F | No intervention; remain failed; provenance `INAPPLICABLE` |
| C-D | Add target \(p\) verbatim; established; provenance `UNKNOWN` |

The formulas, valuation sets, ids, statuses, successor relations, segmentation, and provenance values are imported rather than re-entered in the companion checker. Identity and provenance remain stipulated record inputs, not semantic inferences.

## 2. Primary pairs and R-family baseline

The nine existing distinction pairs are reused:

| Pair | Histories | R0–R4 baseline sequence |
|---|---|---|
| V1 | H1/H2 | `0 1 1 1 1` |
| V2 | H1/H3 | `0 1 1 1 1` |
| V3 | H4/C-F | `0 0 0 1 1` |
| V4 | H5/H6 | `0 0 0 1 1` |
| V5 | H9/H10 | `0 0 0 0 1` |
| V6 | H7/C-D | `0 0 1 1 1` |
| V7 | H8/C-F | `0 0 1 1 1` |
| V8 | H9/H2 | `0 1 1 1 1` |
| V9 | H5/H1 | `0 0 0 1 1` |

Here and below, `0` means `INVISIBLE` and `1` means `VISIBLE` in the stated display order. These baseline sequences are observations to compare, not target answers that the N-family was designed to reproduce. Different family lengths also prevent literal sequence identity from serving as a replication criterion.

## 3. Deliberately non-nested frame family

N0–N5 are sparse projections, not a richness ladder. N1 does not contain N0's endpoint-only record as a separate field; N2 drops all evaluated semantics; N3 drops both syntax and semantics; N4 drops history as well; and N5 recombines only three selected kinds of information.

### N0 — endpoint semantic outcome only

Retains:

- endpoint entails?;
- endpoint counterexample remains?

Erases the before-state, full semantic transition, separate carriers, raw syntax, identity, status beyond semantic outcome, successor, and provenance. N0 is an R0-like control.

### N1 — semantic transition without carrier typing

For both before and after, retains only the evaluated effect

\[
\bigl(M(H)\cap S,\ M(C),\ E_S,\ \models_S\bigr).
\]

It does not retain separate \(M(H)\) and \(S\), raw formulas, typed changed slots, ids, research-history status, successor, segmentation, or provenance. It is deliberately coarser than full R1.

### N2 — raw syntax / typed slot only

Retains:

- raw before \(H,C,S\);
- raw after \(H,C,S\);
- changed slots.

It erases model sets, entailment, \(E\), ids, statuses, successor, segmentation, and provenance. It can compare syntax and typed slot changes but cannot determine semantic success or an action label.

### N3 — history/status only

Retains:

- original and endpoint ids;
- same/different identity assertion;
- original and endpoint status;
- successor relation;
- recorded segmentation.

It erases raw \(H,C,S\), all model sets, entailment, \(E\), and provenance.

### N4 — provenance only

Retains only the stipulated selection-provenance value:

`POST_HOC`, `INDEPENDENT`, `UNKNOWN`, or `INAPPLICABLE`.

It erases semantics, syntax, typed transition, identity, status, successor, and segmentation. `INAPPLICABLE` is retained only where the frozen record already contains it.

### N5 — mixed sparse frame

Retains only:

- endpoint semantic outcome and counterexample-remains value;
- successor relation;
- selection provenance.

It erases raw syntax, full before/after semantic transition, separate carriers, changed slots, id-continuity assertion, original/endpoint research-history status, and segmentation. N5 is neither a completion of N4 nor a summary of N0–N4.

## 4. Frame design discipline

| Frame | Mechanically comparable | Erased | Must not be inferred |
|---|---|---|---|
| N0 | endpoint semantic success/failure and remaining-counterexample flag | route, before-state, syntax, history, provenance | intervention, withdrawal, identity, provenance |
| N1 | equality of before/after evaluated effects | separate \(M(H)\)/\(S\), syntax, history, provenance | whether \(H\), \(C\), or \(S\) was the actual intervention carrier |
| N2 | raw states and which typed slots differ | truth-table effects, status, identity, successor, provenance | entailment, action label, claim continuity, motivation |
| N3 | supplied identity/status/successor/segmentation records | formulas, semantic effects, provenance | mathematical success, legitimacy of identity, motivation |
| N4 | equality of supplied provenance values | every transition and history field | semantic route, identity, trustworthiness of provenance |
| N5 | endpoint outcome, successor, and provenance | raw route, full transition, id continuity, most status fields | formula change, objective successor legitimacy, action label |

No frame fills a missing field from another retained field. In particular:

- identity is not reconstructed from semantic or formula equality;
- provenance is not reconstructed from an exact-filter shape;
- successor is not reconstructed from a formula difference;
- a changed slot is not promoted to a definitive action label;
- `VISIBLE` is not promoted to “true,” and `INVISIBLE` is not promoted to “absent.”

## 5. Non-nested visibility matrix

Each projection exists for every pair, so an information-poor collapse is `INVISIBLE`, not `NOT REPRESENTABLE`.

| Pair | N0 | N1 | N2 | N3 | N4 | N5 |
|---|---|---|---|---|---|---|
| V1 H1/H2 | INVISIBLE | VISIBLE | VISIBLE | INVISIBLE | VISIBLE | VISIBLE |
| V2 H1/H3 | INVISIBLE | VISIBLE | VISIBLE | INVISIBLE | VISIBLE | VISIBLE |
| V3 H4/C-F | INVISIBLE | INVISIBLE | INVISIBLE | VISIBLE | INVISIBLE | INVISIBLE |
| V4 H5/H6 | INVISIBLE | INVISIBLE | INVISIBLE | VISIBLE | INVISIBLE | VISIBLE |
| V5 H9/H10 | INVISIBLE | INVISIBLE | INVISIBLE | INVISIBLE | VISIBLE | VISIBLE |
| V6 H7/C-D | INVISIBLE | INVISIBLE | VISIBLE | INVISIBLE | INVISIBLE | INVISIBLE |
| V7 H8/C-F | INVISIBLE | INVISIBLE | VISIBLE | VISIBLE | VISIBLE | VISIBLE |
| V8 H9/H2 | INVISIBLE | INVISIBLE | VISIBLE | INVISIBLE | VISIBLE | VISIBLE |
| V9 H5/H1 | INVISIBLE | INVISIBLE | INVISIBLE | VISIBLE | VISIBLE | VISIBLE |

N0 collapses all nine pairs because each was selected to share its endpoint semantic success/failure class with its comparator. This does not make the source histories identical.

## 6. Comparison with the R-family baseline

| Pair | R-family sequence, R0–R4 | N-family sequence, N0–N5 |
|---|---|---|
| V1 H1/H2 | `0 1 1 1 1` | `0 1 1 0 1 1` |
| V2 H1/H3 | `0 1 1 1 1` | `0 1 1 0 1 1` |
| V3 H4/C-F | `0 0 0 1 1` | `0 0 0 1 0 0` |
| V4 H5/H6 | `0 0 0 1 1` | `0 0 0 1 0 1` |
| V5 H9/H10 | `0 0 0 0 1` | `0 0 0 0 1 1` |
| V6 H7/C-D | `0 0 1 1 1` | `0 0 1 0 0 0` |
| V7 H8/C-F | `0 0 1 1 1` | `0 0 1 1 1 1` |
| V8 H9/H2 | `0 1 1 1 1` | `0 0 1 0 1 1` |
| V9 H5/H1 | `0 0 0 1 1` | `0 0 0 1 1 1` |

The direct observations are:

- every source distinction is visible somewhere in the N-family;
- visibility does not generally form a suffix in the N-family;
- homologous field dependence often recurs, but its displayed position does not supply an ordering result;
- V8 loses the full-R1 carrier distinction in N1 because N1 deliberately retains only evaluated semantics;
- several pairs are visible in different N-frames for different reasons;
- the N-family display contains both disappearance and reappearance patterns.

These facts do not make the two sequences directly commensurable. The R-family has five nested frames; the N-family has six sparse frames.

## 7. Replication criteria

### FIELD-LEVEL REPLICATION

A distinction is field-level replicated when a second family also makes it visible whenever a homologous kind of explicitly retained information separates the records. H9/H10 under provenance retention is the clean control.

### ORDER REPLICATION

An order result would require visibility to occur in the same relative frame ordering. Because N0–N5 are non-nested and their display order is conventional, this criterion is expected to be fragile and is not required for success.

### SIGNATURE REPLICATION

This stronger criterion asks whether a pair's visibility pattern remains qualitatively similar across the two families. Different lengths and different frame contents make literal identity unavailable. No match is forced.

### NON-REPLICATION

A finding is non-replicated when its visibility depends on an R-family carrier or inherited pattern that the N-family does not retain. Reorganization means that the source pair is still distinguishable somewhere but no longer follows the R-family pattern or basis distribution.

Replication here never implies universality, importance, or ontology.

## 8. Central case: H9/H10 provenance

H9/H10 differ only in stipulated provenance.

| Frame | Result | Reason |
|---|---|---|
| N0 | INVISIBLE | same endpoint outcome |
| N1 | INVISIBLE | same evaluated semantic transition |
| N2 | INVISIBLE | same raw syntax and changed slots |
| N3 | INVISIBLE | same identity/status/successor record |
| N4 | VISIBLE | `POST_HOC` versus `INDEPENDENT` |
| N5 | VISIBLE | N5 also retains provenance |

The provenance distinction therefore **replicates at the field level**: it is visible exactly in the N-frames that retain provenance. “R4-like late appearance” does not replicate as an ordered result, because N4's position is only a display convention and can be permuted without changing its contents.

## 9. Central case: H5/H6 history and identity

H5/H6 share before/after semantics and raw \(H,C,S\) slots. They differ in identity/status/successor history.

| Frame | Result | Reason |
|---|---|---|
| N1 | INVISIBLE | evaluated semantic transitions are identical |
| N2 | INVISIBLE | raw typed transitions are identical |
| N3 | VISIBLE | identity, original withdrawal, successor, and segmentation differ |
| N4 | INVISIBLE | both provenance values are `UNKNOWN` |
| N5 | VISIBLE | N5 retains the successor relation, though not full identity/status |

History dependence is therefore replicated through matching retained fields, not through a fixed frame rank. N5 shows that even a sparse successor field can separate the pair without retaining the rest of N3. Neither projection adjudicates whether the identity split is objectively correct.

## 10. Central case: H8/C-F event visibility

H8 stipulates an \(+\top\) intervention; C-F stipulates no intervention. Their evaluated semantic transitions are identical.

| Frame | Result | Separating field, if any |
|---|---|---|
| N0 | INVISIBLE | none |
| N1 | INVISIBLE | none; both are the same evaluated no-change transition |
| N2 | VISIBLE | raw `H:+⊤` and `changed_slots=(H)` versus no slot change |
| N3 | VISIBLE | `same_identity=true, segmentation=single` versus `same_identity=UNKNOWN, segmentation=none` in the frozen records |
| N4 | VISIBLE | provenance `UNKNOWN` versus `INAPPLICABLE` |
| N5 | VISIBLE | provenance difference; endpoint and successor fields do not separate the pair |

These are not four outputs from one event detector. N2 distinguishes raw syntax; N3 distinguishes supplied history metadata; N4 and N5 distinguish provenance applicability. The pair is the same, but the basis of visibility changes. None of these frames may infer the other bases.

## 11. Central case: H9/H2 carrier distinction

H9 and H2 share the evaluated after-effect

\[
\bigl(M(H)\cap S,M(C),E_S,\models_S\bigr)
=
\bigl(\{\omega_{10},\omega_{11}\},M(p),\varnothing,\text{true}\bigr).
\]

Their N-family record is:

| Frame | Result | Reason |
|---|---|---|
| N1 | INVISIBLE | separate \(M(H)\) and \(S\) roles have been erased |
| N2 | VISIBLE | raw `H changed` versus `S changed` |
| N3 | INVISIBLE | same identity/status/successor/segmentation structure |
| N4 | VISIBLE | `POST_HOC` versus `UNKNOWN` |
| N5 | VISIBLE | provenance is retained |

Thus V8 follows `0 0 1 0 1 1` in N0–N5. The same pair is visible once through typed carrier difference and elsewhere through provenance difference. Visibility alone does not identify which source field separates the records.

This is also the strongest carrier non-replication: full R1 made H9/H2 visible because it separately retained \(M(H)\) and \(S\), whereas N1 intentionally erases that separation and collapses the pair.

## 12. Central case: H7/C-D syntax

H7 adds \(\neg\neg p\); C-D adds \(p\). Since

\[
M(\neg\neg p)=M(p),
\]

their evaluated semantic transitions are equal.

- N1: `INVISIBLE`;
- N2: `VISIBLE`, because raw after formulas differ;
- N3: `INVISIBLE`, because the recorded identity/status structures match;
- N4: `INVISIBLE`, because both provenance values are `UNKNOWN`;
- N5: `INVISIBLE`, because endpoint outcome, successor, and provenance match.

This is the clean syntax control. The R-family's `0 0 1 1 1` suffix becomes the N-family's isolated `0 0 1 0 0 0`. The syntax dependence replicates; inherited visibility does not.

## 13. Visibility disappearance and reappearance

The displayed N0–N5 order contains several non-monotonic patterns:

- V1 and V2: `0 1 1 0 1 1`;
- V4: `0 0 0 1 0 1`;
- V8: `0 0 1 0 1 1`;
- V6: `0 0 1 0 0 0`.

For example, V8 is visible in N2, invisible in N3, and visible in N4. This does not mean that the distinction disappeared and later returned in the histories. It means that N2 retains a separating typed field, N3 retains no separating field for this pair, and N4 retains a different separating provenance field.

Similarly, V6 is visible only in N2 because only N2 retains its separating raw syntax. Moving to N3 does not undo an intervention; it changes the observation scheme.

## 14. Non-monotonic visibility control

Yes: visibility becomes non-monotonic in the displayed N0–N5 sequence once nested inheritance is removed. At least three forms occur:

- `VISIBLE → INVISIBLE`: V3 and V6 after their sole separating frame;
- `INVISIBLE → VISIBLE`: every pair somewhere in the family;
- `VISIBLE → INVISIBLE → VISIBLE`: V1, V2, V4, and V8.

This result is itself design-dependent. Sparse frames make visibility loss possible because one frame need not retain another frame's separating field. It does not establish that non-monotonicity is a law, nor does the N0–N5 order carry a temporal or epistemic direction.

## 15. Same pair, different visibility basis

The clearest cases are:

- **H8/C-F:** N2 separates by syntax/typing, N3 by history metadata, and N4/N5 by provenance applicability.
- **H9/H2:** N2 separates by H/S typed carrier, while N4/N5 separate by provenance.
- **H5/H1:** N3 separates by identity/status/successor history, N4 by provenance, and N5 by both successor and provenance.
- **H1/H2:** N1 separates by evaluated semantics, N2 by raw typed slots, and N4/N5 by provenance.

Therefore `VISIBLE` alone is too coarse to identify why a pair is distinguishable. Projection inequality records the existence of at least one retained difference; it does not identify a unique source, still less an action ontology.

## 16. Descriptive basis annotation

The annotations below are descriptive only. `MIXED` means that more than one retained basis differs in that cell; these labels are not a new taxonomy.

| Pair | N0 | N1 | N2 | N3 | N4 | N5 |
|---|---|---|---|---|---|---|
| V1 H1/H2 | — | SEMANTIC | SYNTAX/TYPING | — | PROVENANCE | PROVENANCE |
| V2 H1/H3 | — | SEMANTIC | SYNTAX/TYPING | — | PROVENANCE | PROVENANCE |
| V3 H4/C-F | — | — | — | HISTORY/STATUS | — | — |
| V4 H5/H6 | — | — | — | HISTORY/STATUS | — | HISTORY/STATUS |
| V5 H9/H10 | — | — | — | — | PROVENANCE | PROVENANCE |
| V6 H7/C-D | — | — | SYNTAX/TYPING | — | — | — |
| V7 H8/C-F | — | — | SYNTAX/TYPING | HISTORY/STATUS | PROVENANCE | PROVENANCE |
| V8 H9/H2 | — | — | SYNTAX/TYPING | — | PROVENANCE | PROVENANCE |
| V9 H5/H1 | — | — | — | HISTORY/STATUS | PROVENANCE | MIXED |

An em dash denotes an `INVISIBLE` cell, not the absence of a source difference.

## 17. Pairwise basis audit

| Pair | Visible N-frames | Basis in each frame | Same basis across frames? |
|---|---|---|---|
| V1 H1/H2 | N1, N2, N4, N5 | N1 semantic; N2 syntax/typing; N4/N5 provenance | No |
| V2 H1/H3 | N1, N2, N4, N5 | N1 semantic; N2 syntax/typing; N4/N5 provenance | No |
| V3 H4/C-F | N3 | history/status | Single visible basis only |
| V4 H5/H6 | N3, N5 | full history/status at N3; successor at N5 | Same broad history basis, different retained extent |
| V5 H9/H10 | N4, N5 | provenance in both | Yes |
| V6 H7/C-D | N2 | syntax/typing | Single visible basis only |
| V7 H8/C-F | N2, N3, N4, N5 | syntax; history metadata; provenance; provenance | No |
| V8 H9/H2 | N2, N4, N5 | typed carrier; provenance; provenance | No |
| V9 H5/H1 | N3, N4, N5 | history; provenance; successor plus provenance | No |

The table confirms `same pair ≠ same visibility basis` for most multi-frame visible pairs.

## 18. Replication table

| Pair | R-family finding | N-family finding | Replication status |
|---|---|---|---|
| V1 H1/H2 | semantic distinction from R1, later inherited | semantic in N1, typed in N2, absent N3, provenance in N4/N5 | PARTIALLY REPLICATED |
| V2 H1/H3 | semantic distinction from R1, later inherited | semantic in N1, typed in N2, absent N3, provenance in N4/N5 | PARTIALLY REPLICATED |
| V3 H4/C-F | history/status visible from R3 | visible only in history/status N3 | FIELD-LEVEL REPLICATED |
| V4 H5/H6 | identity/successor visible from R3 | visible in N3 and successor-bearing N5, absent elsewhere | FIELD-LEVEL REPLICATED |
| V5 H9/H10 | provenance-only separation at R4 | visible exactly in provenance-bearing N4/N5 | FIELD-LEVEL REPLICATED |
| V6 H7/C-D | raw syntax appears at R2 and is inherited | visible only in raw-syntax N2 | FIELD-LEVEL REPLICATED |
| V7 H8/C-F | raw intervention visible from R2 | visible by syntax, history metadata, or provenance depending on frame | REORGANIZED |
| V8 H9/H2 | full-R1 carrier and R2 typing distinguish; later inheritance | N1 collapses; N2 typed and N4/N5 provenance distinguish | REORGANIZED |
| V9 H5/H1 | history difference visible from R3 | history in N3, provenance in N4, mixed in N5 | PARTIALLY REPLICATED |

No pair is classified `NOT REPLICATED`: every controlled source difference has at least one N-frame retaining a separating field. That fact is limited to these histories and the deliberately chosen N-family. It does not imply that every distinction would survive every alternative family.

## 19. Does “first visible frame” survive?

In the displayed N0–N5 order, the first visible entries are:

| Pair | R-family first visibility | Displayed N-family first visibility |
|---|---|---|
| V1 | R1 | N1 |
| V2 | R1 | N1 |
| V3 | R3 | N3 |
| V4 | R3 | N3 |
| V5 | R4 | N4 |
| V6 | R2 | N2 |
| V7 | R2 | N2 |
| V8 | R1 full carrier | N2 |
| V9 | R3 | N3 |

The superficial alignment for eight pairs comes from placing homologous semantic, typed, history, and provenance frames in the same displayed positions. It does not survive as an intrinsic order claim: visible N-frames need not form suffixes, V8 shifts because N1 erases carrier roles, and Section 21's permutation changes which visible frame is listed first.

Thus “first visible frame” is a property of the chosen ordered frame family and its field contents, not a demonstrated property of the distinction itself.

## 20. Do visibility sequences survive?

They do not survive as family-independent descriptions. The R-family suffixes reflect nested inheritance; the N-family sequences contain isolated and reappearing visibility. V6 changes from `0 0 1 1 1` to `0 0 1 0 0 0`, while V8 changes from `0 1 1 1 1` to `0 0 1 0 1 1`.

The sequences are family-relative displays. They are not invariants, fingerprints, distances, codes, or class identifiers. A similar-looking sequence such as the provenance control does not establish signature replication because the underlying frames and sequence lengths differ.

## 21. Frame permutation control

The checker permutes the display order from

`N0 N1 N2 N3 N4 N5`

to

`N4 N2 N0 N5 N1 N3`

without changing any projector. Selected results are:

| Pair | Original display | Permuted display | Visible-frame set |
|---|---|---|---|
| V3 H4/C-F | `000100` | `000001` | `{N3}` unchanged |
| V5 H9/H10 | `000011` | `100100` | `{N4,N5}` unchanged |
| V6 H7/C-D | `001000` | `010000` | `{N2}` unchanged |
| V7 H8/C-F | `001111` | `110101` | `{N2,N3,N4,N5}` unchanged |
| V8 H9/H2 | `001011` | `110100` | `{N2,N4,N5}` unchanged |
| V9 H5/H1 | `000111` | `100101` | `{N3,N4,N5}` unchanged |

One sequence can coincidentally remain textually unchanged under a particular permutation; the checker does not require every binary string to change. What is preserved mechanically is the per-frame visibility set. Sequence order is presentation-dependent, and a “first” entry changes with the presentation.

## 22. Mechanically checkable part

Companion checker:

`notes/theorem_proof_anatomy_experiment/04_record_frame/proof_formation_non_nested_frame_replication_checker_v0.1.py`

It imports the existing history builder without mutation and checks only:

- the unchanged set of H1–H10, C-F, and C-D records and selected frozen controls;
- N0–N5 projections;
- pairwise equality/inequality and the complete visibility matrix;
- the actual top-level fields separating every visible pair;
- R-family baseline versus N-family sequences;
- selected non-monotonic patterns;
- sparse-field/erasure effects;
- display-order permutation: sequence changes while the per-frame visibility set is preserved;
- the provenance-only H9/H10 control;
- the semantic collapse and raw-syntax separation of H7/C-D;
- the evaluated-semantic collapse and typed separation of H9/H2.

The checker does not judge:

- which frame is correct or superior;
- what distinction is fundamental;
- whether an action is real;
- whether history identity is legitimate;
- whether provenance is trustworthy;
- whether replication implies universality;
- whether non-replication falsifies the methodology;
- whether visibility basis is ontological;
- whether one frame family should replace another.

All assertions pass. This verifies finite projection behavior, not the meaning or importance of a distinction.

## 23. Candidate findings

### F1 — Supported

Some field-level visibility dependencies reproduce. Provenance-only H9/H10, syntax-only H7/C-D, and history-dependent H5/H6 separate under homologous retained information in both families.

### F2 — Supported with an important qualification

The R0–R4 first-visible ordering is not robust under non-nested frames. The unpermuted N display superficially preserves eight positions because homologous frames were listed in analogous order, but V8 shifts and a harmless frame permutation changes the sequence and “first” visible entry.

### F3 — Supported

Visibility is non-monotonic in the displayed N-family once inheritance is removed. V4 and V8 provide `VISIBLE → INVISIBLE → VISIBLE`; V6 provides an isolated visible frame.

### F4 — Supported

The same pair can be visible for different reasons. H8/C-F and H5/H1 are the clearest controls.

### F5 — Supported

Visibility sequence is frame-family-relative and display-order-relative.

### F6 — Supported

The H9/H10 distinction remains provenance-dependent across families. The result is a retention control, not provenance discovery.

### F7 — Supported

The H7/C-D semantic collapse recurs in N1, while syntax-bearing N2 separates the pair.

### F8 — Supported

Carrier distinctions disappear when carrier roles are not separately retained. N1 collapses H9/H2 although full R1 distinguished them.

### F9 — Supported

`VISIBLE` alone is insufficient to identify the separating basis. It must be accompanied by the actual differing retained fields.

### F10 — Tentatively supported only as a test-local description

Field dependence survives better than position in a displayed frame sequence for several controlled pairs. This is not proposed as a principle: the N-family was deliberately built from homologous field subsets, so some field-level replication follows directly from its construction.

## 24. Falsification condition applied

### Outcome A audit

A substantial part of the result is a direct consequence of frame definitions. H9/H10 appearing in provenance-bearing N4/N5 is intentionally trivial. H7/C-D appearing in raw-syntax N2 is nearly as direct. This pushes strongly toward `DOWNGRADE` and brings `KILL` into serious consideration.

### Outcome B audit

This outcome is also observed. Ordered suffix patterns break, while the kind of retained information that separates clean controls remains stable: provenance for H9/H10, syntax for H7/C-D, and history/successor for H5/H6. This supports only limited `RETAIN + REVISE`.

### Outcome C audit

Field-level replication is not uniformly strong. H8/C-F, H9/H2, and H5/H1 are visible on multiple unrelated bases across sparse frames. V8 also loses the full-R1 carrier basis in N1. These cases support a strong family-relative `DOWNGRADE`, though they do not erase the clean controls from Outcome B.

`KILL` is not dismissed lightly: if the purpose were to discover a general visibility structure, the direct dependence on stipulated fields would be fatal. For the narrower replication/stress purpose, however, the exact reorganization, non-monotonicity, carrier erasure, changing visibility bases, and permutation effect are checkable results not contained in any single pair or single frame definition. The test therefore remains diagnostically useful but theoretically weak.

## 25. What this test does not establish

This test does not establish:

- a universal observability structure;
- a canonical family of frames;
- a canonical field decomposition;
- that syntax, history, or provenance are fundamental layers;
- that field-level replication implies ontology;
- that first visibility has intrinsic meaning;
- that a visibility sequence is stable;
- that non-monotonicity is universal;
- that real mathematical reasoning behaves this way;
- that one record representation is superior;
- that action classification has been solved.

It also does not infer identity, provenance, or episode boundary, and it does not retrofit the blind-reader or earlier finite tests to the N-family results.

## 26. Retain / revise / downgrade / kill

Target proposition:

> Visibility-transition findings from the nested R0–R4 family are robust under alternative record-frame families.

- **RETAIN — limited.** Some field-level dependencies reproduce: provenance separates H9/H10, syntax separates H7/C-D, and history/successor separates H5/H6 whenever the relevant kind of field is retained.
- **REVISE.** Ordered first-appearance statements do not survive as properties of a distinction. They must be indexed to a named family, its field contents, and its display order.
- **DOWNGRADE — strong.** Visibility patterns are strongly family-relative. Non-nested frames produce disappearance, reappearance, isolated visibility, and different visibility bases for the same pair.
- **KILL — seriously approached, not triggered for the narrow diagnostic claim.** Much of field-level visibility restates what each frame keeps. The test nonetheless adds controlled cross-family information: it distinguishes basis replication from order failure, demonstrates full-R1 carrier non-replication in N1, and verifies non-monotonic and permutation behavior mechanically. It would not support a stronger claim of general robustness.

Combined disposition: **RETAIN limited + REVISE + DOWNGRADE strong**. v0.2 remains postponed.

## 27. Final report

1. **Strongest replicated visibility dependency:** H9/H10 remains distinguishable only in provenance-bearing N4/N5; provenance dependence replicates cleanly at field level.
2. **Strongest non-replication:** H9/H2 is visible in full R1 but invisible in carrier-erasing N1, then visible in N2, invisible in N3, and visible again in N4/N5.
3. **Did first-visible ordering survive?** No as an intrinsic result. Most unpermuted positions coincide only because homologous frames were displayed in analogous order; V8 and the permutation control break the claim.
4. **Did visibility become non-monotonic?** Yes. V1, V2, V4, and V8 exhibit visible–invisible–visible patterns in the displayed N-family.
5. **Cleanest visibility change:** H7/C-D is invisible in N1, visible in syntax-only N2, and invisible again in N3–N5.
6. **Pair visible for different reasons:** H8/C-F—syntax/typing in N2, history metadata in N3, and provenance applicability in N4/N5.
7. **Did the visibility sequence survive?** No. It is family-relative and changes under a frame permutation while per-frame results stay fixed.
8. **Did field-level dependence survive better than frame position?** Yes for the clean controls, but only within this deliberately field-matched test.
9. **Was `VISIBLE` alone too coarse?** Yes. It does not identify which retained field separates a pair.
10. **Did the test add more than a frame-definition restatement?** Only modestly: the cross-family matrix, non-monotonic patterns, H9/H2 carrier erasure, multiple bases for one pair, and permutation control are additional diagnostics. Many individual cells remain definitional retention controls.
11. **Disposition:** RETAIN limited + REVISE + DOWNGRADE strong; KILL seriously approached but not triggered for the narrow diagnostic test.
12. **v0.2:** remain postponed.

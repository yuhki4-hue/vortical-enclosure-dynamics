# Reader 01 Pilot Coding: Protocol Calibration Note

**Status:** protocol calibration result; not a framework validation  
**Reader treatment:** Reader 01 is a pilot/calibration run and is excluded from the reader count of any later formal inter-reader test.

## Purpose and limits

This note audits Reader 01 against the coder packet, frozen corpus, and adjudication materials in order to locate reader-packet defects. It does not expand M1–M17, revise the frozen items, change an expected answer to match Reader 01, quantify agreement, or treat correspondence with an answer key as framework success.

Reader 01 cannot be made blind retroactively. Its report should therefore remain a calibration artifact and should not be rerun under v0.1.1 as though it were a new independent observation.

## Protocol defects exposed by the pilot

| Protocol defect | Pilot evidence | Minimal correction in v0.1.1 |
|---|---|---|
| M1–M17 were named but not defined in the coder packet | Reader 01 could identify several operations in words but repeatedly had to enter `M-code UNKNOWN`; it explicitly identified the absent codebook as the main instruction defect. | Add the unchanged, concise M1–M17 codebook to the coder packet. |
| M3 and M4 had no stated division of labor | Reader 01 could not decide whether restriction concerned a formula/language class or an object/model/domain class. | State M3 as formula-class/language restriction and M4 as object/domain/model-class restriction; permit `AMBIGUOUS (M3/M4)`. |
| Episode segmentation was not a required independent step | Several frozen items contain a withdrawal, retained side claim, or later methodological shift, while the v0.1 block encouraged one blended transition. | Require segmentation before move coding and record the boundary and any alternative segmentation explicitly. |
| A frozen corpus item was implicitly treated as one analytic episode | E02, E05, E09, E10, E11, and E12 can each support more than one source-local transition. | Permit stable subepisode IDs under the unchanged parent item; do not alter item text, excerpt, or order. |
| `available_branches` could absorb an actually adopted side claim | In E02 and E05, a limited/conditional claim is not merely a hypothetical rescue; in other items a branch is genuinely only available or rejected. The old block had no field for this distinction. | Separate `available_branches` from `adopted_side_claims`; adoption must be source-supported and given its own claim identity. |
| One `claim_after` and one `terminal_status` forced incompatible outcomes together | In E10, distinct claims about Gödel I, Gödel II, and a proposed metatheoretic vocabulary do not necessarily share a verdict. Similar pressure appears in E07, E11, and E12. | Permit A1, A2, and further after-claims and require a terminal status for each. |
| Non-formal decision criteria had no dependency field of their own | Falsification, novelty, retention, demotion, and stopping rules were liable to be coded as theorem assumptions or as evidence resources. | Add `evaluation_or_decision_rules`, separate from assumptions and proof/evidence resources. |

These are packet defects because the requested distinctions already mattered to the frozen material but the submission form or instructions did not make them reconstructible. Their correction does not change the move taxonomy.

## Genuine source ambiguity

The following ambiguities remain after the packet repair and should not be eliminated by instruction:

- **E02:** the universal impossibility claim and a finite-capacity/fixed-task claim can be segmented as withdrawal plus side claim, or as one larger shrinkage sequence. The source supports the distinction but does not uniquely dictate the analytic boundary.
- **E04:** the cited objection can be read as exposing a quantifier gap, an internality restriction, or both. The excerpt does not force one claim identity.
- **E05:** the relationship between the rejected conventional equivalence and the conditional implementation lemma permits more than one episode boundary. The latter must not automatically be coded as rescue of the former.
- **E07:** the failed universal H1 claim and the retained organizational-value statement have different targets. Whether they form one before/after episode or adjacent episodes is not uniquely fixed by the excerpt.
- **E09:** narrowing to a finite Phase 0, the reduced-artifact test, and the termination rule can be represented as one staged decision or multiple subepisodes.
- **E10:** Gödel I, Gödel II, and the proposed general metatheoretic vocabulary are distinct verdict targets within the same source item. A single terminal status is not source-faithful.
- **E11:** the formal progression example and the later warning against collapsing progression, strength, reflection, and ordinal labels can be segmented separately. The source supports both but does not mandate one granularity.
- **E12:** the negative statement about a universal scalar and the positive two-level program are not simple logical negations of one another. The excerpt also does not uniquely fix whether the scalar target is an explicit prior claim or a rejected possible formulation.

These cases should remain eligible for `AMBIGUOUS`, multiple codes, or alternative segmentations. Resolving them merely to obtain cleaner reader correspondence would defeat the reconstruction test.

## Framework boundaries revealed by the pilot

- A frozen corpus item is a presentation unit, not necessarily the unit of analysis. The framework must receive a reader's segmentation; it does not mechanically supply one.
- M1–M17 classify source-supported moves after claim identity and episode boundary are fixed. They do not determine those two prior judgments.
- The same passage may report a failure witness, an available repair, an adopted side claim, and a terminal decision. These roles are not interchangeable and need not collapse to one move.
- Formal theorem cases and research-policy cases share some record fields but not a single dependency semantics. `evaluation_or_decision_rules` marks this boundary without asserting a new move.
- Prior-art absorption can be coded only to the specificity established by the supplied source. A reader need not infer historical dependence, equivalence, or exhaustiveness.
- The codes do not decide whether two statements preserve claim identity. That remains a source-constrained reconstruction and may be unresolved.
- Multiplicity of codes is sometimes faithful. The framework does not require a unique code when one transition explicitly combines, for example, disambiguation, prior-art absorption, and withdrawal.

## UNKNOWN and AMBIGUOUS that are not reader errors

| Pilot record | Calibration classification | Reason |
|---|---|---|
| `M-code UNKNOWN` for moves whose M-number was not defined in v0.1 | Protocol defect, not reader error | The reader could not reconstruct an unavailable codebook without violating the ban on outside completion. |
| `M3/M4` uncertainty | Protocol defect plus possible source ambiguity | The division was absent; in some excerpts the restricted kind is itself not fully fixed. |
| Alternative boundaries in E02, E04, E05, E09, E10, E11, and E12 | Genuine source ambiguity, not reader error | More than one source-compatible segmentation exists. |
| `UNKNOWN` proof details where the excerpt states a result or verdict but not a proof route | Source limitation, not reader error | A result statement does not license invention of its resources. |
| `UNKNOWN` available rescue when the source records only the taken move | Source limitation, not reader error | Logical availability in the abstract is not source evidence that the research episode considered that branch. |
| Unresolved assumption/resource role | Framework boundary or source ambiguity, not automatically reader error | Some non-formal criteria can function as conditions, resources, or decision rules; v0.1 lacked the third field. |
| Refusal to equate a source-local label such as H1 or M1 with a formation code | Correct protocol restraint | Local names do not determine move taxonomy. |
| Multiple candidate move descriptions for one transition | Potentially valid multi-code record | v0.1 permitted multiple codes, and the adjudication materials do not require forced uniqueness. |

This classification does not declare every Reader 01 entry correct. Some provenance assignments and episode boundaries remain adjudicable judgments. The calibration conclusion is narrower: the prominent unknowns listed above cannot fairly be counted as reader mistakes under the packet the reader received.

## What v0.1.1 deliberately does not repair

The revision does not select a preferred segmentation for any E-item, rewrite excerpts, disclose expected coding, add a move, turn arbitrariness into a score, define an agreement statistic, or make a general claim about proof formation. It also does not erase genuine uncertainty about claim identity, provenance, or branch availability.

## Gate for a blind Reader 02

**Decision: v0.1.1 is sufficient to begin a new blind Reader 02, subject to packet isolation.** This is a readiness judgment about the instructions, not evidence that the framework is valid.

The run should satisfy all of the following conditions:

1. Reader 02 receives only `proof_formation_coder_instructions_v0.1.1.md` and the unchanged `proof_formation_frozen_toy_corpus_v0.1.md`.
2. The adjudication rules, any answer key, the meta-experiment, trajectory summaries, Reader 01, and this calibration note remain hidden during coding.
3. Reader 02 may use parent-preserving subepisode IDs and may return `UNKNOWN`, `AMBIGUOUS`, or multiple codes without pressure to converge.
4. Original-source access remains limited to paths supplied by the frozen corpus and should be reported in `source_excerpts_used`.
5. Reader 01 remains excluded from the formal reader count; it is retained only as the run that motivated protocol calibration.

The gate would fail if Reader 02 is shown calibration/adjudication material, is required to produce exactly one block per frozen item, or is evaluated as incorrect merely for a source-supported unresolved record.

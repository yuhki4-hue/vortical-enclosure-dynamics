# Proof-Formation Visibility Transition Test v0.1

Date: 2026-09-06  
Status: exploratory finite-propositional sensitivity record  
Scope: the frozen histories and R0–R4 projections already defined in the finite prototype sequence

## 0. Status / posture

This document is:

- an **exploratory visibility-transition test**;
- **not a theorem**;
- **not an observability theorem**;
- **not a new framework**;
- **not a v0.2 proposal**;
- **not a validation report**;
- **not a canonical ordering of frames**;
- **not a claim that more visible means more true**;
- **not a claim that less visible means less important**;
- **not a claim that frame changes correspond to discovery in real research**;
- a test with **no new move codes**;
- a test with **no score** and **no optimization**;
- a test with **no metric** and no geometry, topology, or lattice;
- **not a generalization beyond the frozen finite prototype**.

The central question is:

> Given one frozen history h and two observation frames Ri and Rj, what changes in the set of distinctions that can be read from the record?

The test changes the observation frame, not the frozen history. A visibility change is therefore a change in what a projected record permits an observer to distinguish. It is not treated as an ontological change in the event, claim, or action. The earlier blind-reader experiment is not rewritten; it supplies only motivation for this finite toy test.

## 1. Frozen histories reused unchanged

Let

\[
V=\{p,q\},\qquad
\Omega=\{\omega_{00},\omega_{01},\omega_{10},\omega_{11}\},
\]

with the bit order \((p,q)\). The common initial candidate is

\[
H_0=\{p\lor q\},\qquad C_0=p,
\]

so

\[
M(H_0)=\{\omega_{01},\omega_{10},\omega_{11}\},\qquad
E(H_0,C_0)=\{\omega_{01}\}.
\]

No auxiliary history is added. The meanings fixed in the record-frame sensitivity test are reused:

| History | Frozen content |
|---|---|
| H1 | Add \(\neg q\); same id; endpoint established; provenance `INDEPENDENT` |
| H2 | Restrict \(S\) to \(\Omega\setminus\{\omega_{01}\}\); same id; endpoint established; provenance `UNKNOWN` |
| H3 | Replace target by \(p\lor q\); same id; endpoint established; provenance `UNKNOWN` |
| H4 | No semantic repair; original withdrawn; no successor; provenance `INAPPLICABLE` |
| H5 | Original \(x_0\) withdrawn; successor \(x_1\) has \(H_0\cup\{\neg q\}\), target \(p\), and is established |
| H6 | Same mathematical after-material as H5, but \(x_0\) continues through strengthening and is established |
| H7 | Add \(\neg\neg p\); endpoint established; provenance `UNKNOWN` |
| H8 | Add \(\top\); extensional semantic state unchanged; endpoint failed; provenance `UNKNOWN` |
| H9 | Add exact filter \(p\lor\neg q\); endpoint established; provenance `POST_HOC` |
| H10 | Same formulas, semantic states, identity, and status as H9; provenance `INDEPENDENT` |
| C-F | No intervention; remain failed; provenance `INAPPLICABLE` |
| C-D | Add target \(p\) verbatim; endpoint established; provenance `UNKNOWN` |

In particular, H9 and H2 share the evaluated after-effect

\[
\bigl(M(H)\cap S,M(C),E_S,\models_S\bigr)
=
\bigl(\{\omega_{10},\omega_{11}\},M(p),\varnothing,\text{true}\bigr),
\]

but achieve it through different carriers. H9 changes \(H\); H2 changes \(S\).

## 2. R0–R4 as observation schemes

The existing projections are reused without alteration:

- **R0 — outcome-only:** designated endpoint semantic success/failure and whether a counterexample remains.
- **R1 — extensional semantic:** before/after \(M(H)\), \(M(C)\), \(S\), surviving valuations \(M(H)\cap S\), \(E_S\), and entailment. Raw formula syntax is not retained, but \(M(H)\) and \(S\) remain separate carriers.
- **R2 — typed-transition / raw slots:** R1 plus raw \(H,C,S\) slots and the changed-slot record.
- **R3 — history/status:** R2 plus ids, same/different-identity assertion, original and endpoint status, successor relation, and recorded segmentation.
- **R4 — provenance-complete:** R3 plus the stipulated selection provenance.

R0–R4 are different field-retention choices. Their displayed order is not a ladder of truth, importance, legitimacy, or correctness. Adjacent changes are used only because the existing implementations are nested and therefore make gain and erasure easy to inspect.

## 3. Operational meaning of distinction

For a frozen pair \((h_a,h_b)\) and frame \(R_i\), this test uses only:

- **VISIBLE:** \(R_i(h_a)\ne R_i(h_b)\);
- **INVISIBLE:** \(R_i(h_a)=R_i(h_b)\).

The histories and projectors are fully specified, so `AMBIGUOUS` and `NOT EVALUATED` are not needed for V1–V9.

`VISIBLE` means only that the two projected records differ. It does not mean that the distinction is true, legitimate, important, objective, or action-defining. `INVISIBLE` means only that the projections collapse. It does not mean that the underlying histories are the same or that the source distinction is absent.

## 4. Primary history pairs

| Pair | Comparison |
|---|---|
| V1 | H1 / H2 — ordinary strengthening versus scope restriction |
| V2 | H1 / H3 — assumption strengthening versus conclusion weakening |
| V3 | H4 / C-F — withdrawn versus merely failed |
| V4 | H5 / H6 — withdrawal plus successor versus same-id continuation |
| V5 | H9 / H10 — post-hoc versus independently motivated same transition |
| V6 | H7 / C-D — semantically equivalent insertion versus verbatim insertion |
| V7 | H8 / C-F — \(+\top\) intervention versus no intervention |
| V8 | H9 / H2 — matched evaluated effect, with H-slot versus S-slot handling |
| V9 | H5 / H1 — same endpoint-style strengthening effect, with different original history/disposition |

## 5. Visibility matrix

The matrix is the existing `DISTINCT / COLLAPSED` result restated as `VISIBLE / INVISIBLE`. No projector was changed to obtain it.

| Pair | R0 | R1 | R2 | R3 | R4 |
|---|---|---|---|---|---|
| V1 H1/H2 | INVISIBLE | VISIBLE | VISIBLE | VISIBLE | VISIBLE |
| V2 H1/H3 | INVISIBLE | VISIBLE | VISIBLE | VISIBLE | VISIBLE |
| V3 H4/C-F | INVISIBLE | INVISIBLE | INVISIBLE | VISIBLE | VISIBLE |
| V4 H5/H6 | INVISIBLE | INVISIBLE | INVISIBLE | VISIBLE | VISIBLE |
| V5 H9/H10 | INVISIBLE | INVISIBLE | INVISIBLE | INVISIBLE | VISIBLE |
| V6 H7/C-D | INVISIBLE | INVISIBLE | VISIBLE | VISIBLE | VISIBLE |
| V7 H8/C-F | INVISIBLE | INVISIBLE | VISIBLE | VISIBLE | VISIBLE |
| V8 H9/H2 | INVISIBLE | VISIBLE | VISIBLE | VISIBLE | VISIBLE |
| V9 H5/H1 | INVISIBLE | INVISIBLE | INVISIBLE | VISIBLE | VISIBLE |

Two qualifications are essential.

First, V1 is not an exact semantic-effect match. H1 leaves surviving valuations \(\{\omega_{10}\}\), whereas H2 leaves \(\{\omega_{10},\omega_{11}\}\). It is therefore already visible in R1. V8 is the controlled matched-effect comparison.

Second, V8 is `VISIBLE` in the chosen full R1 because R1 retains \(M(H)\) and \(S\) separately. Under the evaluated subprojection that retains only \(M(H)\cap S\), \(M(C)\), \(E_S\), and entailment, V8 is `INVISIBLE`. This is not a contradiction; the two carriers are different.

## 6. Visibility-transition types

For an adjacent change \(R_i\to R_{i+1}\):

- **APPEARS:** `INVISIBLE → VISIBLE`;
- **REMAINS VISIBLE:** `VISIBLE → VISIBLE`;
- **REMAINS INVISIBLE:** `INVISIBLE → INVISIBLE`;
- **DISAPPEARS:** `VISIBLE → INVISIBLE`.

These labels describe the two projection results only. They do not say that an entity came into or went out of existence.

Under the present nested projectors, every field of an earlier frame is inherited by the next frame. `DISAPPEARS` is therefore possible as a logical table entry but was not observed in V1–V9. This absence is audited in Section 14 rather than assumed to be a property of the histories.

## 7. First visible frame

| Pair | First visible frame | Immediate basis |
|---|---|---|
| V1 H1/H2 | R1 | Different extensional after states, including different surviving valuation sets |
| V2 H1/H3 | R1 | R1 retains different after \(M(H)\), \(M(C)\), and surviving-set structure |
| V3 H4/C-F | R3 | `withdrawn` versus `failed` status/history assertion |
| V4 H5/H6 | R3 | identity discontinuity, original withdrawal, successor, and segmentation versus continuation |
| V5 H9/H10 | R4 | `POST_HOC` versus `INDEPENDENT` provenance |
| V6 H7/C-D | R2 | raw \(+\neg\neg p\) versus raw \(+p\) syntax |
| V7 H8/C-F | R2 | raw `H:+⊤` change versus no changed slot |
| V8 H9/H2 | R1 full carrier | separate \(M(H)\) and \(S\) carriers; evaluated subprojection remains invisible |
| V9 H5/H1 | R3 | withdrawal/successor split versus same-id continuation |

“First” is relative to the displayed R0–R4 sequence. Because that sequence is test-local and non-canonical, a first-visible frame is not a depth, rank, or measure of the distinction.

## 8. Observed causes of appearance

The following are descriptive groupings for this test, not a new taxonomy.

### A. Added semantic detail

R0 retains endpoint success/failure only. R1 adds before/after model sets, surviving valuations, counterexamples, and separate semantic carriers. V1 and V2 become visible because their semantic transitions differ beyond the shared successful endpoint. V8 also becomes visible in full R1, but there the decisive fact is R1's decision to retain \(M(H)\) and \(S\) separately.

### B. Added typing or syntax

R2 adds raw formulas and typed \(H,C,S\) change slots. This makes V6 and V7 visible even though their extensional semantic comparisons collapse in R1. It also expresses the H-slot/S-slot distinction for V8 more directly, although V8 was already visible in full R1.

### C. Added historical or provenance assertions

R3 makes V3, V4, and V9 visible by retaining status, identity, successor, and segmentation fields. R4 makes V5 visible by retaining stipulated provenance. These appearances do not recover those facts from truth tables.

## 9. Central test: H8 versus C-F

H8 contains an explicitly stipulated intervention, \(+\top\). C-F contains no intervention. Both have the same before and after evaluated semantic state and remain failed.

| Frame | H8 versus C-F |
|---|---|
| R0 | INVISIBLE — same endpoint failure and counterexample-remains value |
| R1 | INVISIBLE — both project to the same extensional \(\sigma_0\to\sigma_0\) record |
| R2 | VISIBLE — raw `H:+⊤` versus no changed slot |
| R3 | VISIBLE — the R2 distinction is inherited |
| R4 | VISIBLE — the earlier distinction remains; provenance also differs as stipulated |

Thus:

> The source-history difference was invisible under coarse projections and became observable under a syntax-bearing typed frame.

The event was not generated by R2, and it did not fail to exist in R0/R1. The difference was stipulated in the frozen source history; R0/R1 omitted the information needed to distinguish it.

## 10. Central test: H5 versus H6

H5 and H6 have the same common failure and the same mathematical after-material \(H_0\cup\{\neg q\}\models p\). They differ only in the recorded handling of identity and disposition:

- H5: original \(x_0\) withdrawn, successor \(x_1\) established;
- H6: \(x_0\) continues through strengthening and is established.

Their visibility sequence is:

\[
\text{INVISIBLE},\ 	ext{INVISIBLE},\ 	ext{INVISIBLE},\ 	ext{VISIBLE},\ 	ext{VISIBLE}.
\]

The distinction is neither an extensional semantic distinction nor a raw typed-slot distinction. It first appears when R3 retains the identity, status, successor, and segmentation assertions. R3 has not discovered objective claim identity; it has retained a source-history assertion that earlier projectors omitted. This remains only a toy analogue of the prior episode-boundary problem.

## 11. Central test: H9 versus H10

H9 and H10 have identical formulas, before/after semantics, raw changed slots, identities, statuses, successor structure, and segmentation. The frozen source record differs only in selection provenance:

- H9: `POST_HOC`;
- H10: `INDEPENDENT`.

| Frame | Visibility |
|---|---|
| R0 | INVISIBLE |
| R1 | INVISIBLE |
| R2 | INVISIBLE |
| R3 | INVISIBLE |
| R4 | VISIBLE |

This is the cleanest late-appearance case. Its triviality is a control: R4 does not recover hidden semantic provenance. It merely retains a field already stipulated in the frozen source history. Nothing here shows that provenance is semantically latent, trustworthy, or always needed.

## 12. Central test: H9 versus H2

H9 and H2 have the same evaluated after-effect:

\[
M(H')\cap S'=\{\omega_{10},\omega_{11}\},\qquad
M(C)=M(p),\qquad E_{S'}=\varnothing.
\]

Nevertheless:

- **evaluated subprojection:** INVISIBLE, because it retains only the surviving set, target model set, counterexample set, and entailment;
- **full R1:** VISIBLE, because it separately records H9's changed \(M(H)\) with \(S=\Omega\), and H2's unchanged \(M(H)\) with restricted \(S\);
- **R2–R4:** VISIBLE, with R2 explicitly retaining raw `H changed` versus `S changed`.

Visibility can therefore appear before raw syntax if a semantic frame has already pre-separated carrier roles. “Semantic frame” is not neutral here: full R1 carries a representational choice that the evaluated subprojection does not. R2 makes that typed distinction explicit; it does not recover a distinction in the matched evaluated effect.

## 13. Visibility of a distinction versus its source

Four notions must remain separate:

- **source distinction:** a difference stipulated in the frozen underlying histories;
- **semantic distinction:** a difference in truth-table/evaluated semantic content;
- **record distinction:** a difference in fields retained by a given frame;
- **visible distinction:** inequality of the two projected records under that frame.

| Pair | Source distinction | Evaluated semantic distinction | Record carrier that first separates it | Visibility consequence |
|---|---|---|---|---|
| H9/H10 | provenance is stipulated differently | absent | R4 provenance field | first visible at R4 |
| H5/H6 | identity/disposition history is stipulated differently | absent | R3 identity/status/successor | first visible at R3 |
| H8/C-F | intervention versus none | absent | R2 raw typed change | first visible at R2 |
| H7/C-D | different raw formulas | absent because \(M(\neg\neg p)=M(p)\) | R2 raw syntax | first visible at R2 |
| H9/H2 | H-slot versus S-slot handling | absent in evaluated effect | full R1 separate \(M(H)\)/\(S\) carriers | first visible at R1 |
| H1/H2 | different interventions and different after semantics | present | R1 semantic details | first visible at R1 |

Thus source distinction need not be semantically visible, record distinction depends on retained fields, and projection inequality is not a verdict about legitimacy.

## 14. Non-monotonicity control

For every selected pair, once visibility appears it remains visible in all later displayed frames. No `VISIBLE → INVISIBLE` transition occurred under enrichment.

That result is not evidence that visibility or knowledge grows monotonically in general. The current projectors are nested by construction:

\[
R2=R1+\text{typed fields},\quad
R3=R2+\text{history fields},\quad
R4=R3+\text{provenance}.
\]

Consequently, a difference retained at \(R_i\) is literally present in \(R_{i+1}\). The observed monotonic visibility is induced by projector inheritance in this test. Arbitrary, non-nested frames could discard, recode, or aggregate earlier fields; this test does not address them.

## 15. Counter-test by field erasure

Reading the same comparisons in the reverse direction gives controlled visibility losses:

| Erasure | Pair that becomes invisible | What is erased | What remains |
|---|---|---|---|
| R4 → R3 | H9/H10 | provenance | identical semantics, slots, identity, and status |
| R3 → R2 | H4/C-F | withdrawal versus failed/no-intervention status | identical semantic and typed records |
| R3 → R2 | H5/H6 | identity continuity, original withdrawal, successor, segmentation | identical semantic and raw-slot transitions |
| R3 → R2 | H5/H1 | split history versus same-id continuation | identical endpoint-style strengthening record |
| R2 → R1 | H7/C-D | raw \(\neg\neg p\) versus \(p\) syntax | extensionally identical semantics |
| R2 → R1 | H8/C-F | raw \(+\top\) versus no slot change | identical extensional no-change semantics |
| R1 full → evaluated subprojection | H9/H2 | separate \(M(H)\) and \(S\) roles | identical surviving set, target models, \(E\), and entailment |

For these cases, appearance under enrichment and disappearance under the matching erasure are reverse descriptions of the same projection dependency. This is not a claim of formal mathematical duality.

## 16. Adjacent transition table

| Pair | R0→R1 | R1→R2 | R2→R3 | R3→R4 |
|---|---|---|---|---|
| V1 H1/H2 | APPEARS | REMAINS VISIBLE | REMAINS VISIBLE | REMAINS VISIBLE |
| V2 H1/H3 | APPEARS | REMAINS VISIBLE | REMAINS VISIBLE | REMAINS VISIBLE |
| V3 H4/C-F | REMAINS INVISIBLE | REMAINS INVISIBLE | APPEARS | REMAINS VISIBLE |
| V4 H5/H6 | REMAINS INVISIBLE | REMAINS INVISIBLE | APPEARS | REMAINS VISIBLE |
| V5 H9/H10 | REMAINS INVISIBLE | REMAINS INVISIBLE | REMAINS INVISIBLE | APPEARS |
| V6 H7/C-D | REMAINS INVISIBLE | APPEARS | REMAINS VISIBLE | REMAINS VISIBLE |
| V7 H8/C-F | REMAINS INVISIBLE | APPEARS | REMAINS VISIBLE | REMAINS VISIBLE |
| V8 H9/H2 | APPEARS | REMAINS VISIBLE | REMAINS VISIBLE | REMAINS VISIBLE |
| V9 H5/H1 | REMAINS INVISIBLE | REMAINS INVISIBLE | APPEARS | REMAINS VISIBLE |

For V8, `R0→R1 APPEARS` refers to full R1. The evaluated subprojection remains `INVISIBLE` and is reported separately rather than inserted as an extra frame.

## 17. First-appearance table

| Distinction pair | First visible frame | Field or structure making it visible | Semantic or record-carried? |
|---|---|---|---|
| V1 H1/H2 | R1 | different surviving valuations/full semantic state | semantic |
| V2 H1/H3 | R1 | different after \(M(H)\) and \(M(C)\) structure | semantic |
| V3 H4/C-F | R3 | withdrawn versus failed status | record-carried history/status |
| V4 H5/H6 | R3 | id continuity, original status, successor, segmentation | record-carried history |
| V5 H9/H10 | R4 | selection provenance | record-carried provenance |
| V6 H7/C-D | R2 | raw formula syntax | record-carried typing/syntax |
| V7 H8/C-F | R2 | changed H slot despite semantic no-op | record-carried typing/syntax |
| V8 H9/H2 | R1 full carrier | separate \(M(H)\) and \(S\) carrier fields | carrier-typed representation; absent from matched evaluated effect |
| V9 H5/H1 | R3 | original withdrawal and successor versus continuation | record-carried history/status |

The final column does not classify actions. It identifies where the pairwise inequality resides in these projections.

## 18. Test-local visibility signatures

Writing `0` for `INVISIBLE` and `1` for `VISIBLE`, in the fixed display order R0–R4:

| Pair | Sequence |
|---|---|
| V1 H1/H2 | `0 1 1 1 1` |
| V2 H1/H3 | `0 1 1 1 1` |
| V3 H4/C-F | `0 0 0 1 1` |
| V4 H5/H6 | `0 0 0 1 1` |
| V5 H9/H10 | `0 0 0 0 1` |
| V6 H7/C-D | `0 0 1 1 1` |
| V7 H8/C-F | `0 0 1 1 1` |
| V8 H9/H2 | `0 1 1 1 1` |
| V9 H5/H1 | `0 0 0 1 1` |

These sequences are only a compact display of this matrix. They are not scores, distances, orders, fingerprints, or invariants, and no theoretical meaning is assigned to shared sequences.

## 19. Does first visibility locate the action?

No. A visibility threshold states which retained information is needed to distinguish two projected records. It does not state that the action belongs to an ontological layer represented by that frame.

H8 makes the point sharply. The \(+\top\) intervention is stipulated before any projection. It first becomes visible at R2 only because R2 keeps raw syntax and changed slots. It would be an error to say that the event is a “R2-level action.” Likewise, H5/H6 first become distinguishable at R3 because identity/history assertions are recorded there, not because an objective action layer has been located.

## 20. Is late appearance evidence of hidden structure?

Not in this test.

- H9/H10 first separate at R4 because provenance is first retained at R4. No hidden semantic provenance was recovered.
- H5/H6 first separate at R3 because stipulated identity, status, and successor fields are first retained at R3. No objective identity structure was discovered.
- H7/C-D first separate at R2 because raw syntax is present. Their truth-table equivalence is unchanged.

Late appearance can therefore be fully explained by field retention. Whether the retained assertion is true, justified, useful, or central is outside the checker and this test.

## 21. Mechanically checkable part

Companion checker:

`notes/theorem_proof_anatomy_experiment/04_record_frame/proof_formation_visibility_transition_checker_v0.1.py`

It imports the existing record-frame checker and reuses its histories and projectors unchanged. It checks only:

- pairwise equality/inequality under R0–R4;
- the V1–V9 visibility matrix;
- first-visible frame;
- adjacent transition class;
- selected erasure collapses;
- the displayed binary sequences;
- equality of the H9/H2 evaluated subprojection and inequality of their full R1 projections;
- absence of `DISAPPEARS` in this nested enrichment run.

It does not decide:

- which distinction is real or important;
- which frame is correct;
- whether an identity assertion is legitimate;
- whether provenance is trustworthy;
- whether late appearance is discovery;
- whether visibility is monotonic for arbitrary frames;
- whether a displayed sequence has theoretical meaning;
- whether an action belongs to a move class or ontological layer.

The checker completed with all assertions passing. This verifies implementation consistency, not the interpretation or value of a distinction.

## 22. Candidate findings

### F1 — Supported

Some distinctions are invisible under coarse frames and appear only when the relevant fields are retained. V7, V4, and V5 give controlled R2, R3, and R4 appearances.

### F2 — Supported within this test

Visibility thresholds differ: semantic-detail pairs appear at R1, syntax/typed pairs at R2, history/status pairs at R3, and provenance-only V5 at R4. This is a result about the selected frames, not a canonical ordering of distinction kinds.

### F3 — Supported

Some distinctions arise through carrier typing rather than evaluated semantic change. V8 is already visible in full R1 because it separately retains \(M(H)\) and \(S\), while its evaluated subprojection is invisible.

### F4 — Supported only for the selected pairs

The identity/history comparisons V3, V4, and V9 first appear at R3. This follows from retained fields and does not validate the identity assertions.

### F5 — Supported for the provenance-only control

V5 first appears at R4. This is a direct retention control, not semantic recovery.

### F6 — Supported

Event occurrence can be invisible in semantic projections. H8/C-F collapse in R0/R1 and separate in R2.

### F7 — Supported as a design control

Observed monotonic visibility is wholly accounted for by nested projector inheritance in this implementation. It is not established as a property of histories or arbitrary frames.

### F8 — Supported

Visibility transition does not identify action ontology. It identifies projection requirements for a pairwise distinction.

### F9 — Supported

Visibility appearance establishes neither truth, legitimacy, nor importance. R3 and R4 preserve stipulated assertions without adjudicating them.

## 23. What this test does not establish

This test does not establish:

- a canonical visibility hierarchy;
- a universal observability law;
- a correct record architecture;
- a correct action taxonomy;
- a correct claim-identity criterion;
- objective episode boundaries;
- that richer frames reveal truth;
- that late-visible distinctions are deeper;
- that early-visible distinctions are more fundamental;
- that visibility is monotonic under arbitrary frames;
- that real mathematical discovery behaves like these projections;
- that provenance is semantically latent;
- that event occurrence is recoverable without a suitable record frame.

It also does not infer identity from semantics, provenance from semantic shape, or episode boundary from formulas.

## 24. Retain / revise / downgrade / kill

Target proposition:

> Formation distinctions can be studied by tracking their visibility transitions across record frames.

- **RETAIN — limited.** The selected transitions are descriptively recoverable. The matrix locates exactly where each frozen pair separates and the erasure checks reproduce the corresponding collapses.
- **REVISE.** The observed transitions depend strongly on frame construction, especially R1's carrier separation and R2–R4's inherited fields. Any use of “first appearance” must name the tested frame sequence and projector.
- **DOWNGRADE.** For V3–V7 and V9, thresholds primarily report when a stipulated field is retained. They do not expose intrinsic action structure. H9/H10 is deliberately close to a restatement of the R4 definition.
- **KILL — not triggered, but tested strictly.** If the output were only “R3 has id, so identity is visible at R3,” the exercise would add no result beyond its definitions. The present test adds a limited empirical check: all nine pair projections are computed consistently; V8 reveals that even R1's semantic carrier design changes visibility; H8 shows that an intervention record can be erased by an extensional projection despite a fully unchanged extensional transition; and reverse erasure reproduces the predicted collapses. This is enough for a diagnostic test, but not enough for a theory or architecture proposal.

The combined disposition is therefore **RETAIN + REVISE + DOWNGRADE**, not KILL. Because the useful result remains frame-local and substantially projector-dependent, v0.2 should remain postponed.

## 25. Final report

1. **Strongest visibility appearance:** H8/C-F at R1→R2. An explicitly stipulated \(+\top\) intervention is invisible extensionally and becomes visible only when raw typed change is retained.
2. **Cleanest late-appearance and strongest REMAINS INVISIBLE case:** H9/H10, `0 0 0 0 1`; the pair remains invisible through R3 and provenance first appears at R4.
3. **Cleanest event-invisibility case:** H8/C-F collapse in R0 and R1 despite intervention versus no intervention.
4. **First frame where a typed distinction appears:** R2, for H7/C-D and H8/C-F. H9/H2 is already distinct in full R1 because R1 pre-separates semantic carriers.
5. **First frame where a history distinction appears:** R3, for H4/C-F, H5/H6, and H5/H1.
6. **First frame where a provenance distinction appears:** R4, for H9/H10.
7. **Did any distinction disappear under enrichment?** No, not under the present nested projector design.
8. **Did disappearance occur under erasure?** Yes. Provenance, history/identity, raw syntax/typing, and H/S carrier distinctions each disappear when their retaining fields are erased.
9. **Was visibility growth intrinsic or projector-induced?** The observed monotonic growth was projector-induced. Individual semantic differences remain truth-table auditable, but their monotone preservation follows from inheritance.
10. **Does a visibility threshold locate action ontology?** No. It states only what information this projection sequence must retain to distinguish the pair.
11. **Did the test add more than a restatement of frame definitions?** Only in a limited diagnostic sense: it checks the complete pair matrix, exposes R1 carrier sensitivity through H9/H2, verifies event invisibility through H8/C-F, and confirms reverse erasures. Late R3/R4 appearances remain largely direct consequences of field definitions.
12. **Disposition:** RETAIN + REVISE + DOWNGRADE; KILL not triggered.
13. **v0.2:** remain postponed.

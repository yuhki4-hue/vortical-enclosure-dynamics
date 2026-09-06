# Proof-Formation Minimal Separating Field-Set Test v0.1

Date: 2026-09-06  
Status: exploratory finite-history field-ablation record  
Scope: the unchanged frozen histories and already implemented record information

## 0. Status / posture

This document is:

- an **exploratory field-ablation test**;
- **not a theorem**;
- **not a minimality theorem**;
- **not a feature-selection theorem**;
- **not a new framework**;
- **not a v0.2 proposal**;
- **not a canonical record schema**;
- **not a ranking of fields**;
- **not a claim that a smallest separating set is ontologically fundamental**;
- **not a claim that a field absent from a minimal set is unimportant**;
- a test with **no new move codes**;
- a test with **no score** and **no optimization objective**;
- a test with **no metric** and no geometry, topology, or lattice;
- **not a generalization beyond the frozen finite histories**.

The central question is:

> How far can the retained field set be reduced before a selected distinction becomes invisible?

Here “minimal” means only inclusion-minimal under the exact atomic projection defined below. It does not mean universal, canonical, fundamental, explanatory, or necessary for a future record design.

## 1. Frozen histories reused unchanged

No history is added or changed. The shared finite setting remains

\[
V=\{p,q\},\quad
\Omega=\{\omega_{00},\omega_{01},\omega_{10},\omega_{11}\},
\]

with

\[
H_0=\{p\lor q\},\quad C_0=p,\quad E(H_0,C_0)=\{\omega_{01}\}.
\]

| History | Frozen meaning |
|---|---|
| H1 | Add \(\neg q\); same-id; established; provenance `INDEPENDENT` |
| H2 | Restrict \(S\) to \(\Omega\setminus\{\omega_{01}\}\); same-id; established; `UNKNOWN` |
| H3 | Weaken target to \(p\lor q\); same-id; established; `UNKNOWN` |
| H4 | Withdrawal only; original withdrawn; no successor; `INAPPLICABLE` |
| H5 | Original \(x_0\) withdrawn; successor \(x_1\) established with \(H_0\cup\{\neg q\}\models p\) |
| H6 | Same mathematical after-material as H5; \(x_0\) continues and is established |
| H7 | Add \(\neg\neg p\); established; `UNKNOWN` |
| H8 | Add \(\top\); evaluated semantics unchanged; failed; `UNKNOWN` |
| H9 | Add post-hoc exact filter \(p\lor\neg q\); established; `POST_HOC` |
| H10 | Same formulas and transition as H9; provenance `INDEPENDENT` |
| C-F | No intervention; remain failed; `INAPPLICABLE` |
| C-D | Add \(p\) verbatim; established; `UNKNOWN` |

The checker imports these records from the existing record-frame checker. Formula semantics are truth-table derived. Identity, status, segmentation, and provenance remain supplied history assertions rather than inferred facts.

## 2. Selected distinction pairs

| Pair | Histories | Intended comparison |
|---|---|---|
| D1 | H4/C-F | withdrawn versus merely failed |
| D2 | H5/H6 | withdrawal plus successor versus same-id continuation |
| D3 | H9/H10 | post-hoc versus independently motivated same transition |
| D4 | H7/C-D | semantically equivalent insertion versus verbatim insertion |
| D5 | H8/C-F | \(+\top\) intervention versus no intervention |
| D6 | H9/H2 | matched evaluated effect, H-slot versus S-slot handling |
| D7 | H1/H3 | assumption strengthening versus conclusion weakening |
| D8 | H5/H1 | same endpoint-style strengthening effect but different history/disposition |

No other V-pair is needed to answer the present question.

## 3. Atomic candidate fields

The test decomposes information already present in the implementations. This is not a proposed schema.

### Semantic / extensional atoms

- `endpoint_entails`
- `endpoint_counterexample_remains`
- `before_surviving`
- `after_surviving`
- `before_target_models`
- `after_target_models`
- `before_E`
- `after_E`
- `before_scope`
- `after_scope`
- `before_assumption_models`
- `after_assumption_models`

### Raw / typed atoms

- `raw_before_H`
- `raw_after_H`
- `raw_before_C`
- `raw_after_C`
- `raw_before_S`
- `raw_after_S`
- `changed_slots`

### History / status atoms

- `original_id`
- `endpoint_id`
- `same_identity`
- `original_status`
- `endpoint_status`
- `successor`
- `segmentation`

### Provenance atom

- `selection_provenance`

An atom is simply one coordinate used by this checker. Atomicity here does not imply semantic independence or indivisibility.

## 4. Field decomposition discipline

| Field atom | Source | Semantic or stipulated | Stored or derived | Finite-test redundancy/dependency |
|---|---|---|---|---|
| `endpoint_entails` | after semantic state | semantic | derived | exactly determined by `after_E = ∅` |
| `endpoint_counterexample_remains` | after semantic state | semantic | derived | exactly `bool(after_E)` |
| `before_surviving` | \(M(H)\cap S\) before | semantic | derived | recomputable from `before_assumption_models` and `before_scope` |
| `after_surviving` | \(M(H)\cap S\) after | semantic | derived | recomputable from `after_assumption_models` and `after_scope` |
| `before_target_models` | before target formula | semantic | truth-table derived | extension of `raw_before_C`; loses syntax |
| `after_target_models` | after target formula | semantic | truth-table derived | extension of `raw_after_C`; loses syntax |
| `before_E` | before surviving/target sets | semantic | derived | `before_surviving \ before_target_models` |
| `after_E` | after surviving/target sets | semantic | derived | `after_surviving \ after_target_models` |
| `before_scope` | frozen before \(S\) | supplied carrier value | directly stored, then frozen | value-identical to `raw_before_S` here |
| `after_scope` | frozen after \(S\) | supplied carrier value | directly stored, then frozen | value-identical to `raw_after_S` here |
| `before_assumption_models` | before \(H\) | semantic | truth-table derived | extension of `raw_before_H`; loses syntax |
| `after_assumption_models` | after \(H\) | semantic | truth-table derived | extension of `raw_after_H`; loses syntax |
| `raw_before_H` | before formula tuple | raw supplied record | directly stored/label projected | common across all selected pairs |
| `raw_after_H` | after formula tuple | raw supplied record | directly stored/label projected | may differ when its model set does not, as in D4 |
| `raw_before_C` | before target | raw supplied record | directly stored/label projected | common across all selected pairs |
| `raw_after_C` | after target | raw supplied record | directly stored/label projected | target-content difference for D7 |
| `raw_before_S` | before scope | raw supplied record | directly stored | value-identical to `before_scope` here |
| `raw_after_S` | after scope | raw supplied record | directly stored | value-identical to `after_scope` here |
| `changed_slots` | raw before/after H/C/S | typed record | derived | recomputable from six raw slot fields |
| `original_id` | frozen history | stipulated | directly stored | no selected pair differs on it |
| `endpoint_id` | frozen history | stipulated | directly stored | co-varies with some successor/identity assertions |
| `same_identity` | frozen history | stipulated assertion | directly stored | not globally replaceable by id equality: C-F has equal id strings but `UNKNOWN` assertion |
| `original_status` | frozen history | stipulated | directly stored | correlated with withdrawal histories |
| `endpoint_status` | frozen history | stipulated | directly stored | not reducible to entailment because `withdrawn` and `failed` can share semantic failure |
| `successor` | frozen history | stipulated | directly stored | may co-vary with endpoint id and segmentation |
| `segmentation` | frozen history | stipulated | directly stored | may co-vary with intervention/successor metadata |
| `selection_provenance` | frozen history | stipulated | directly stored | not recoverable from semantic shape |

The checker verifies the stated set equalities and derived-field dependencies. It does not infer the legitimacy of any identity, status, segmentation, or provenance assertion.

## 5. Operational separation

For fixed histories \((h_a,h_b)\) and retained field set \(F\):

\[
\operatorname{projection}_F(h)
=
\langle(f,h[f]):f\in F\rangle.
\]

- **SEPARATES:** \(\operatorname{projection}_F(h_a)\ne\operatorname{projection}_F(h_b)\).
- **COLLAPSES:** \(\operatorname{projection}_F(h_a)=\operatorname{projection}_F(h_b)\).

`SEPARATES` means only projected-record inequality. It does not establish a real or important difference, correct classification, action identity, explanatory relevance, or causation.

## 6. Search strategy: deletion before construction

The test proceeds as follows:

1. confirm that the full atomic record separates each D-pair;
2. delete all but one field and audit every singleton;
3. remove the sole retained field and confirm collapse to the empty projection;
4. compare semantic, raw, history/status, and provenance bundles for the central controls;
5. inspect derived-field dependencies;
6. enumerate larger subsets only if no singleton separates.

Step 6 is never reached for D1–D8. No unrestricted powerset search is performed.

There is also a structural reason. Under this test's plain coordinate projection, if a set \(F\) separates a pair, at least one coordinate in \(F\) has different values and therefore separates as a singleton. Consequently, no pair or triple can be inclusion-minimal here. This is an implementation consequence of the operational definition, not a minimality theorem or general statement about record design.

## 7. “Tested inclusion-minimal separating set”

A tested set \(F\) is called inclusion-minimal only when:

1. \(F\) separates the fixed pair; and
2. every proper subset of \(F\) collapses that pair.

For a separating singleton \(\{f\}\), the only proper subset is the empty set, which collapses every pair. Hence every unequal singleton field is an inclusion-minimal separating set in this implementation.

No set reported below is called globally minimal, canonical, fundamental, generally necessary, or sufficient for a formation record.

## 8. Multiple minimal sets

Multiple incomparable inclusion-minimal sets occur whenever more than one atomic field differs between the two frozen records. Because all such sets are singletons, they are mutually incomparable under inclusion.

For example, D5 H8/C-F is separated separately by:

\[
\{\texttt{raw_after_H}\},\quad
\{\texttt{changed_slots}\},\quad
\{\texttt{same_identity}\},\quad
\{\texttt{segmentation}\},\quad
\{\texttt{selection_provenance}\}.
\]

Thus the pair has multiple **distinct tested separating bases**. “Distinct” does not mean statistically, informationally, or causally independent; several fields co-vary or are derived.

## 9. D3 — provenance-only positive control

H9 and H10 are identical on every tested semantic, raw, and history/status atom. They differ only on:

\[
\{\texttt{selection_provenance}\}:
\quad \texttt{POST_HOC}\ne\texttt{INDEPENDENT}.
\]

Results:

- `{selection_provenance}` alone: **SEPARATES**;
- delete provenance, leaving the empty set: **COLLAPSES**;
- all semantic atoms: **COLLAPSES**;
- all raw/typed atoms: **COLLAPSES**;
- all history/status atoms: **COLLAPSES**.

Therefore `{selection_provenance}` is the unique tested inclusion-minimal separating set for D3. This is a positive control for projection mechanics, not evidence that the provenance claim is true or that provenance is generally necessary.

## 10. D4 — syntax-content control

H7 adds \(\neg\neg p\); C-D adds \(p\). Their extensions agree:

\[
M(\neg\neg p)=M(p).
\]

Results:

- `{raw_after_H}`: **SEPARATES**;
- `{raw_before_H}`: **COLLAPSES**;
- `{changed_slots}`: **COLLAPSES**, because both records say only that H changed;
- `{after_assumption_models}`: **COLLAPSES**;
- all semantic atoms: **COLLAPSES**.

The unique tested inclusion-minimal set is `{raw_after_H}`. The separating information is changed formula content, not merely the changed-slot name. Replacing `raw_after_H` by its extensional model set erases this distinction.

## 11. D2 — withdrawal/successor versus continuation

H5 and H6 have identical semantic and raw typed transitions. Singleton results for the requested history fields are:

| Singleton | Result |
|---|---|
| `{original_id}` | COLLAPSES |
| `{endpoint_id}` | SEPARATES |
| `{same_identity}` | SEPARATES |
| `{original_status}` | SEPARATES |
| `{endpoint_status}` | COLLAPSES |
| `{successor}` | SEPARATES |
| `{segmentation}` | SEPARATES |

Thus the tested minimal sets are the five separating singletons. The full R3 bundle is unnecessary for mere pairwise inequality. This does not make any one of the five an objective identity criterion: endpoint id, same-identity assertion, withdrawal, successor, and segmentation co-vary in this constructed pair.

## 12. D1 — withdrawn versus merely failed

H4 and C-F share the same failed semantic state and unchanged raw H/C/S record. The requested singleton audit is:

| Singleton | Result | Relation to intended comparison |
|---|---|---|
| `{original_status}` | SEPARATES | intended withdrawal record |
| `{endpoint_status}` | SEPARATES | intended withdrawn-versus-failed disposition |
| `{segmentation}` | SEPARATES | incidental metadata cue for this pair |
| `{same_identity}` | SEPARATES | incidental `true` versus `UNKNOWN` cue |
| `{selection_provenance}` | COLLAPSES | both `INAPPLICABLE` |

The intended status basis is not the only minimal separator. `same_identity` and `segmentation` classify these two frozen rows perfectly without directly encoding the intended withdrawn/failed distinction. This is the first accidental-separator warning.

## 13. D5 — intervention versus no intervention

H8 contains raw \(+\top\); C-F contains no intervention. Their evaluated semantic state and endpoint research status `failed` are the same.

| Singleton | Result | Reading limited to this pair |
|---|---|---|
| `{raw_after_H}` | SEPARATES | records \(+\top\) content versus unchanged H |
| `{changed_slots}` | SEPARATES | derived `H changed` versus no changed slot |
| `{same_identity}` | SEPARATES | `true` versus `UNKNOWN`; not an event field |
| `{segmentation}` | SEPARATES | `single` versus `none`; not by itself an event record |
| `{selection_provenance}` | SEPARATES | `UNKNOWN` versus `INAPPLICABLE`; not an event field |
| `{endpoint_status}` | COLLAPSES | both failed |
| `{endpoint_entails}` | COLLAPSES | both false |
| `{endpoint_counterexample_remains}` | COLLAPSES | both true |

All five separating singletons are tested inclusion-minimal. Only `raw_after_H` and the derived `changed_slots` directly register the typed intervention contrast used to select D5. The other three are sufficient classification cues created by co-varying frozen metadata.

Therefore, even perfect separation by provenance or segmentation is not event detection:

\[
\text{separation}\ne\text{event explanation}.
\]

## 14. D6 — matched effect, carrier and provenance bases

H9 and H2 have the same evaluated effect:

\[
(\text{surviving},M(C),E,\models)
=
(\{\omega_{10},\omega_{11}\},M(p),\varnothing,\text{true}).
\]

Accordingly, each of `after_surviving`, `after_target_models`, `after_E`, `endpoint_entails`, and `endpoint_counterexample_remains` collapses the pair.

Singleton separators are:

| Basis | Separating singleton |
|---|---|
| extensional carrier | `{after_assumption_models}` |
| extensional carrier | `{after_scope}` |
| raw carrier content | `{raw_after_H}` |
| raw carrier content | `{raw_after_S}` |
| derived typed cue | `{changed_slots}` |
| incidental provenance cue | `{selection_provenance}` |

History/status atoms collapse because both records use the same continuation/status structure. In this pair, `after_scope` and `raw_after_S` are value-identical coordinates, while `after_assumption_models` is truth-table derived from raw H. The pair therefore admits both carrier-based and provenance-based tested minimal sets, but not six independent explanations.

## 15. D7 — assumption versus conclusion slot change

H1 and H3 share endpoint success and empty after-E. The fields that separately distinguish them are:

- `{after_surviving}`;
- `{after_target_models}`;
- `{after_assumption_models}`;
- `{raw_after_H}`;
- `{raw_after_C}`;
- `{changed_slots}`;
- `{selection_provenance}`.

The first six align with semantic-content or H-versus-C typed differences. `selection_provenance` is an incidental `INDEPENDENT` versus `UNKNOWN` cue.

`changed_slots` alone separates `('H',)` from `('C',)`, but it is only a typed-slot difference detector for these frozen records. It is not called an M1/M2 detector and does not adjudicate an action label.

## 16. D8 — same endpoint material, different history

H5 and H1 share the same semantic and raw endpoint-style strengthening transition. Singleton separators are:

- `{endpoint_id}`;
- `{same_identity}`;
- `{original_status}`;
- `{successor}`;
- `{segmentation}`;
- `{selection_provenance}`.

The first five correspond to the intended history/disposition contrast. Provenance `UNKNOWN` versus `INDEPENDENT` is an accidental cue for that question. As with D2, multiple history atoms co-vary, so singleton sufficiency does not establish which identity/history field is necessary beyond this exact pair.

## 17. Tested inclusion-minimal sets

Every D-pair has at least one separating singleton. Therefore there are no inclusion-minimal pairs or triples to report; every larger separating set contains a separating singleton proper subset.

| Pair | All tested inclusion-minimal separating sets |
|---|---|
| D1 H4/C-F | `{same_identity}`; `{original_status}`; `{endpoint_status}`; `{segmentation}` |
| D2 H5/H6 | `{endpoint_id}`; `{same_identity}`; `{original_status}`; `{successor}`; `{segmentation}` |
| D3 H9/H10 | `{selection_provenance}` |
| D4 H7/C-D | `{raw_after_H}` |
| D5 H8/C-F | `{raw_after_H}`; `{changed_slots}`; `{same_identity}`; `{segmentation}`; `{selection_provenance}` |
| D6 H9/H2 | `{after_scope}`; `{after_assumption_models}`; `{raw_after_H}`; `{raw_after_S}`; `{changed_slots}`; `{selection_provenance}` |
| D7 H1/H3 | `{after_surviving}`; `{after_target_models}`; `{after_assumption_models}`; `{raw_after_H}`; `{raw_after_C}`; `{changed_slots}`; `{selection_provenance}` |
| D8 H5/H1 | `{endpoint_id}`; `{same_identity}`; `{original_status}`; `{successor}`; `{segmentation}`; `{selection_provenance}` |

This table is exactly the unequal-field inventory for each pair. The reduction of minimal-set search to singleton inequality is a major limitation, not evidence of a sparse natural record.

## 18. Three notions kept separate

### A. Separating field

Any atom whose value differs across a fixed pair. It is defined entirely by projection inequality.

### B. Intended distinction field

A field that directly corresponds to why the pair was selected for the research question. Examples are `endpoint_status` for D1, `selection_provenance` for D3, and `raw_after_H` for D4.

### C. Sufficient classification cue

A field that separates the two frozen rows but does not directly encode the intended distinction. Examples are `selection_provenance` for D5 and D8, and `same_identity` for D1.

A field can be A without being B. C is not called false or useless; it is simply inadequate as a direct explanation of the intended contrast.

## 19. Accidental separators

Yes: a pair can be perfectly separated by a field that does not encode its intended distinction.

| Pair | Intended distinction | Accidental singleton separator(s) |
|---|---|---|
| D1 H4/C-F | withdrawn versus failed | `{same_identity}`, `{segmentation}` |
| D5 H8/C-F | intervention versus no intervention | `{same_identity}`, `{segmentation}`, `{selection_provenance}` |
| D6 H9/H2 | H-carrier versus S-carrier with matched evaluated effect | `{selection_provenance}` |
| D7 H1/H3 | H-slot versus C-slot route | `{selection_provenance}` |
| D8 H5/H1 | withdrawal/successor history versus continuation | `{selection_provenance}` |

These cues work because the frozen histories differ on several coordinates simultaneously. They are called accidental separators descriptively, not as a new formal category.

The D5 result is decisive for interpretation: provenance alone separates intervention from no intervention in this pair, but the provenance value does not directly state that an event occurred. Therefore:

> Minimal separation is not explanatory adequacy.

## 20. Redundant separators

Different singleton separators have at least three relationships in these records:

1. **Derived from richer fields.** `changed_slots` is recomputable from raw before/after H/C/S. Endpoint entailment and counterexample-remains are recomputable from `after_E`.
2. **Value-duplicated coordinates.** `after_scope` and `raw_after_S` have identical values in this implementation. They give two field names, not two informationally independent observations.
3. **Co-varying stipulated facts.** In D2/D8, endpoint id, same-identity assertion, original status, successor, and segmentation change together. Their singleton separation does not establish independence or causal priority.

For D7, `after_surviving` equals `after_assumption_models` because \(S=\Omega\) in both records, while both are ultimately determined by the relevant raw formula semantics. For D4, in contrast, raw H differs while the derived assumption model set is equal.

## 21. Minimality after derived-field audit

The following singleton sets are syntactically inclusion-minimal but derivationally redundant:

- `{changed_slots}` for D5, D6, and D7 is derived from raw before/after slots;
- `{after_assumption_models}` for D6 and D7 is derived by evaluating raw H;
- `{after_surviving}` for D7 is derived from assumption models and scope;
- `{after_scope}` and `{raw_after_S}` for D6 duplicate the same stored scope value under two projections.

`same_identity` is not treated as globally derived from the id pair. C-F has `original_id = endpoint_id = x0` but its same-identity assertion is `UNKNOWN`; blindly comparing id strings would silently add an identity conclusion.

Hence syntactic inclusion minimality is distinct from derivational redundancy. No information measure is introduced, and no claim of information-minimality is made.

## 22. Erasure reconstruction audit

For every reported singleton \(F=\{f\}\), retaining F separates and deleting its sole field yields the empty projection, which collapses. The full atomic record also separates. Central cases are:

| Pair | Representative minimal F | F only | Remove one field | Full atomic record | Semantic-only record |
|---|---|---|---|---|---|
| D3 H9/H10 | `{selection_provenance}` | SEPARATES | COLLAPSES | SEPARATES | COLLAPSES |
| D4 H7/C-D | `{raw_after_H}` | SEPARATES | COLLAPSES | SEPARATES | COLLAPSES |
| D5 H8/C-F | each of five reported singletons | SEPARATES | COLLAPSES | SEPARATES | COLLAPSES |
| D6 H9/H2 | each of six reported singletons | SEPARATES | COLLAPSES | SEPARATES | SEPARATES if separate carriers are retained |

For D6, the narrower evaluated-effect bundle—surviving set, target models, E, and entailment—**COLLAPSES**. The broader semantic-atom bundle separates only because it includes `after_scope` and `after_assumption_models` as distinct carriers. This repeats the earlier full-R1 versus evaluated-subprojection control.

## 23. Cross-pair field reuse

Only fields that separate at least one D-pair are listed. This is a lookup table, not a count, predictive-power estimate, or ranking.

| Field | Selected pairs separated |
|---|---|
| `after_surviving` | D7 |
| `after_target_models` | D7 |
| `after_scope` | D6 |
| `after_assumption_models` | D6, D7 |
| `raw_after_H` | D4, D5, D6, D7 |
| `raw_after_C` | D7 |
| `raw_after_S` | D6 |
| `changed_slots` | D5, D6, D7 |
| `endpoint_id` | D2, D8 |
| `same_identity` | D1, D2, D5, D8 |
| `original_status` | D1, D2, D8 |
| `endpoint_status` | D1 |
| `successor` | D2, D8 |
| `segmentation` | D1, D2, D5, D8 |
| `selection_provenance` | D3, D5, D6, D7, D8 |

All omitted atoms collapse every D1–D8 pair as singletons. Reuse across pairs does not imply general usefulness or importance.

## 24. Minimal-set matrix with intended basis

| Pair | Tested inclusion-minimal separating set(s) | Intended basis | Accidental separator present? |
|---|---|---|---|
| D1 | `{same_identity}`, `{original_status}`, `{endpoint_status}`, `{segmentation}` | withdrawn/failed status | Yes: identity assertion and segmentation |
| D2 | `{endpoint_id}`, `{same_identity}`, `{original_status}`, `{successor}`, `{segmentation}` | identity/status/successor history | No clear outsider, but strong co-variation |
| D3 | `{selection_provenance}` | provenance | No |
| D4 | `{raw_after_H}` | exact syntax/content | No |
| D5 | `{raw_after_H}`, `{changed_slots}`, `{same_identity}`, `{segmentation}`, `{selection_provenance}` | intervention record | Yes: identity, segmentation, provenance |
| D6 | `{after_scope}`, `{after_assumption_models}`, `{raw_after_H}`, `{raw_after_S}`, `{changed_slots}`, `{selection_provenance}` | H/S carrier difference | Yes: provenance |
| D7 | `{after_surviving}`, `{after_target_models}`, `{after_assumption_models}`, `{raw_after_H}`, `{raw_after_C}`, `{changed_slots}`, `{selection_provenance}` | H-change versus C-change | Yes: provenance |
| D8 | `{endpoint_id}`, `{same_identity}`, `{original_status}`, `{successor}`, `{segmentation}`, `{selection_provenance}` | history/disposition | Yes: provenance |

## 25. Singleton separator matrix

The table is limited to fields that separate at least one selected pair.

| Field | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 |
|---|---|---|---|---|---|---|---|---|
| `after_surviving` | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | SEPARATES | COLLAPSES |
| `after_target_models` | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | SEPARATES | COLLAPSES |
| `after_scope` | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | SEPARATES | COLLAPSES | COLLAPSES |
| `after_assumption_models` | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | SEPARATES | SEPARATES | COLLAPSES |
| `raw_after_H` | COLLAPSES | COLLAPSES | COLLAPSES | SEPARATES | SEPARATES | SEPARATES | SEPARATES | COLLAPSES |
| `raw_after_C` | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | SEPARATES | COLLAPSES |
| `raw_after_S` | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | SEPARATES | COLLAPSES | COLLAPSES |
| `changed_slots` | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | SEPARATES | SEPARATES | SEPARATES | COLLAPSES |
| `endpoint_id` | COLLAPSES | SEPARATES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | SEPARATES |
| `same_identity` | SEPARATES | SEPARATES | COLLAPSES | COLLAPSES | SEPARATES | COLLAPSES | COLLAPSES | SEPARATES |
| `original_status` | SEPARATES | SEPARATES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | SEPARATES |
| `endpoint_status` | SEPARATES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES |
| `successor` | COLLAPSES | SEPARATES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | COLLAPSES | SEPARATES |
| `segmentation` | SEPARATES | SEPARATES | COLLAPSES | COLLAPSES | SEPARATES | COLLAPSES | COLLAPSES | SEPARATES |
| `selection_provenance` | COLLAPSES | COLLAPSES | SEPARATES | COLLAPSES | SEPARATES | SEPARATES | SEPARATES | SEPARATES |

## 26. Is one minimal set unique?

No. D3 and D4 each have one tested minimal set, but D1, D2, D5, D6, D7, and D8 have multiple singleton minimal sets.

In the limited descriptive sense of this record table, pairwise distinguishability is multiply realizable: different retained coordinates can make the same pair unequal. That statement concerns projections only and carries no ontological interpretation.

## 27. Does minimal separation explain the distinction?

No. D5 is the strongest counterexample within the frozen records. `{selection_provenance}` minimally separates H8 from C-F, yet it does not directly encode \(+\top\) versus no intervention. `{same_identity}` and `{segmentation}` have the same problem.

D1, D6, D7, and D8 supply further accidental cues. Therefore:

\[
\text{tested minimal separator}
\not\Rightarrow
\text{explanation of the intended distinction}.
\]

The clean controls D3 and D4 align separator and intended contrast, but they do not repair the complex-pair result.

## 28. Does field necessity survive pair redesign?

No such necessity is established. The present pairs often change several fields together. Removing one separator does not collapse a pair if another differing singleton remains, and a different matched comparator could remove an apparent cue.

Only a narrow operational statement is available: within the tested atom list and the exact frozen pair, D3 cannot be separated without `selection_provenance`, and D4 cannot be separated without `raw_after_H`. This is not necessity for the underlying distinction, a future packet, or a record architecture.

Controlled matched pairs would be needed to test broader field necessity. No new histories are introduced here to perform that test.

## 29. Mechanically checkable part

Companion checker:

`notes/theorem_proof_anatomy_experiment/04_record_frame/proof_formation_minimal_separating_field_set_checker_v0.1.py`

It checks only:

- import of the unchanged frozen histories;
- extraction of all listed atomic fields;
- projection to arbitrary selected field subsets;
- pair separation/collapse;
- the complete singleton-separator matrix;
- all tested inclusion-minimal singleton sets;
- one-field deletion to the empty projection;
- derived-field dependencies and exact scope/raw-S duplication;
- D3 provenance-only control;
- D4 syntax-content control;
- D5 multiple-separator stress case;
- D6 evaluated-effect collapse and carrier/provenance alternatives;
- selected D7 semantic/raw/typed checks.

It does not decide:

- which field is fundamental, important, or explanatory;
- which separator is causally relevant;
- whether identity is legitimate;
- whether provenance is trustworthy;
- whether an accidental separator is unimportant in another question;
- whether a minimal set is canonical;
- whether any field should be retained in v0.2.

All assertions pass. The checker also confirms that, under coordinatewise equality, minimality reduces to unequal singleton fields.

## 30. Candidate findings

### F1 — Supported

Every selected distinction has at least one singleton separating field.

### F2 — Supported

Six of eight selected pairs have multiple tested inclusion-minimal singleton sets. No frequency or ranking is inferred from this observation.

### F3 — Supported strongly

A minimal separator may be unrelated to the intended distinction. D5 provenance, identity, and segmentation cues are the clearest case.

### F4 — Supported

Derived fields such as `changed_slots` appear inclusion-minimal even though they are reconstructible from richer raw fields.

### F5 — Supported

Full R3/R4 bundles often contain much more than is required for pairwise separation. D3 needs only provenance; D2 can be separated by any of five history singletons; D4 needs only raw after-H.

### F6 — Supported strongly

Pairwise separation is weaker than explanatory adequacy.

### F7 — Supported

Field necessity cannot be inferred from one frozen pair when multiple fields co-vary. Only D3/D4 have unique tested atomic separators, and even there necessity is pair-local.

### F8 — Retained only as a test-local caution

The reliable output is “which tested fields suffice to separate this frozen pair,” not “which fields are necessary for the underlying distinction.” This is not advanced as a general principle.

## 31. Falsification and downgrade conditions applied

### Outcome A — observed

Every pair is separated by at least one singleton. Under the coordinate-projection definition, this means minimal-set search collapses to identifying unequal metadata fields. `DOWNGRADE` is strongly indicated.

### Outcome B — observed

Accidental singleton separators are widespread in the complex pairs. Pairwise distinguishability is therefore a weak proxy for distinction explanation. This independently supports strong `DOWNGRADE`.

### Outcome C — observed

D3 and D4 are clean unique controls, while D1/D2/D5–D8 split into multiple bases. This supports only limited `RETAIN`, plus `REVISE` and `DOWNGRADE`.

### Outcome D — only locally observed

Unique tested sets occur for D3/D4, but they are not promoted to canonical or fundamental fields.

The `KILL` condition is reached for the strong interpretation of minimal-set enumeration: with plain atomic projection, inclusion-minimal sets add no combinatorial information beyond the unequal-field list. What remains useful is the ablation inventory, the clean-control check, and the exposure of accidental/derived separators—not a characterization of the formation distinction.

## 32. What this test does not establish

This test does not establish:

- a canonical field set;
- a minimal record architecture;
- a sufficient formation schema;
- an explanatory field basis;
- a causal basis of a distinction;
- an action ontology;
- objective identity;
- an objective episode boundary;
- provenance truth;
- a field-importance ranking;
- universal minimality;
- a generalization to realistic theorem formation.

## 33. Retain / revise / downgrade / kill

Target proposition:

> A formation distinction can be characterized by a minimal separating set of record fields.

- **RETAIN — limited diagnostic only.** Every tested pair has a finite separating field inventory, and D3/D4 provide clean pair-local singleton controls.
- **REVISE.** Tested minimal sets are often non-unique, pair-specific, derived, duplicated, or co-varying. They should be reported as sufficient cues for the fixed pair, not as a single characterization.
- **DOWNGRADE — strong.** Minimal separation frequently reflects frozen metadata rather than the intended distinction. D5 shows that accidental cues can separate perfectly.
- **KILL — triggered for the strong characterization claim.** Under coordinatewise projection, every separating set contains a separating singleton, so minimal-set enumeration supplies no structure beyond field-difference enumeration. It does not characterize or explain the formation distinction.

Combined disposition: **RETAIN only the field-ablation inventory; REVISE and DOWNGRADE strongly; KILL the claim that inclusion-minimal separators characterize the distinction.** v0.2 remains postponed.

## 34. Final report

1. **Cleanest singleton separator:** D3 H9/H10 with `{selection_provenance}`.
2. **Cleanest unique minimal set:** D3 `{selection_provenance}`; D4 `{raw_after_H}` is a second clean unique control.
3. **Strongest multiple-minimal-set case:** D7 H1/H3, separated by several semantic, raw, typed, and accidental provenance singletons.
4. **Strongest accidental separator:** D5 H8/C-F is separated by `{selection_provenance}` even though the intended question is intervention versus no intervention.
5. **Derived field that appears minimal:** `{changed_slots}` for D5, D6, and D7.
6. **Heavily redundant full frame:** D3 needs only provenance; every other R4-derived atom collapses the pair. D2's full R3 bundle is also redundant for mere inequality.
7. **Were minimal sets unique?** Only for D3 and D4. All other selected pairs have multiple singleton sets.
8. **Did minimal separation explain the intended distinction?** Generally no; it aligns in the clean controls but fails for complex pairs with accidental cues.
9. **Was field necessity established?** Only the narrow pair-local operational necessity of provenance for D3 and raw after-H for D4. No general or architectural necessity was established.
10. **Is pairwise separation a useful but weak diagnostic?** Yes. It audits visibility under ablation but is not explanatory.
11. **Disposition:** RETAIN the inventory; REVISE and DOWNGRADE strongly; KILL the strong characterization claim.
12. **v0.2:** remain postponed.

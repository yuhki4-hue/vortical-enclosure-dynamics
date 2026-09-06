# Metrology Case 02 — Head-to-Head Comparison

## Field-Native Reconstruction versus Generic Transfer Audit

**Status:** final comparative result  
**Version:** 1.0  
**Comparison date:** 2026-08-16  
**Preregistration:** [scientific_assurance_case_02_metrology_preregistration.md](./scientific_assurance_case_02_metrology_preregistration.md)  
**Frozen control:** [scientific_assurance_case_02_metrology_control_reconstruction.md](./scientific_assurance_case_02_metrology_control_reconstruction.md)  
**Generic audit:** [scientific_assurance_case_02_metrology.md](./scientific_assurance_case_02_metrology.md)

> The preregistration and field-native control were frozen before the generic audit. This comparison applies the preregistered rejection and success criteria without changing them after seeing the result.

---

## 1. Preregistered question

The substantive question was:

> To what extent are an upstream measurement result, uncertainty, calibration conditions, validated scope, and traceability information retained when the result is used downstream?

The comparative question was:

> Does a generic assurance / handoff audit change a diagnosis, decision, scope judgment, or retrieval result relative to a reconstruction using only field-native metrology concepts?

The comparison covered:

- **Chain A:** calibration certificate → downstream measurement;
- **Chain B:** measurement result → conformity decision;
- **Chain C:** SI realization → laboratory traceability chain;
- **counterexample test:** the 2019 SI revision and the kilogram.

Fixed preregistration digest: `9059e179dcf95263a2c9c9e23ee913ce465f74f8b5020e0876b89e1b6c8fd911`.

---

## 2. Control verdict

The frozen control, using VIM/GUM/JCGM/SI/ILAC/NIST/KCDB and DCC terminology, already did all of the following:

- treated a measurement result as more than a bare indicated value;
- traced calibration uncertainty into the user’s later uncertainty budget;
- distinguished traceability from fitness for intended use;
- required measurand, method, range, conditions, reference, and result-specific documentation;
- distinguished a measurement result from a conformity decision;
- identified guard bands and decision risk;
- identified invalid reuse of “pass” under a different tolerance or rule;
- found a public NPL–NCC certificate-upload and data-availability problem and its DCC remedy;
- separated normative requirements from an implementation failure;
- treated the revised kilogram definition as eliminating unique-artefact definition dependence while leaving realization and dissemination uncertainties.

Frozen control digest: `2767e82c5054dc18f2e4b6daed972e54277727b74a6c1c6a9a810fb0a3e93876`.

The control therefore set a strong baseline: the generic audit had to produce a concrete difference, not merely restate these findings.

---

## 3. Generic audit verdict

The generic audit represented each upstream output as

\[
O_{\mathrm{up}}=(\hat\theta,U,A,S,R)
\]

and classified downstream fields as preserved, transformed but recoverable, validly delegated, decision-irrelevant, scope-restricted, lost, distorted, or unsupported.

This produced a compact cross-chain display. It did not produce:

- a new missing assumption;
- a new uncertainty component;
- a different judgment about a calibration scope;
- a different conformity decision;
- a new traceability break;
- a source absent from the frozen control corpus;
- a remedy not already present in field-native practice.

Its apparent findings were rejected under F1–F6. Its main positive effect was organizational: the same information could be scanned across the three chains using one index.

---

## 4. Head-to-head table

| Question | Field-native control | Generic handoff audit | Difference |
|---|---|---|---|
| missing assumption detection | identified measurand, method, range, conditions, reference, decision rule, user responsibilities | indexed the same fields under \(A,S,R\) | none |
| uncertainty-loss detection | required certificate contribution, local components, correlations, and decision use | asked whether \(U\) was preserved or recoverable | none; native account more precise |
| scope-overreach detection | diagnosed use outside certificate/CMC/accreditation range and invalid reuse of conformity status | labeled the same cases unsupported transfer | no judgment difference |
| traceability-break detection | used VIM/ILAC/NIST criteria and document-control checks | inspected whether \(R\) remained accessible | no new break found |
| downstream decision change | used JCGM 106 decision rules, guard bands, and risk | added no alternative rule or changed action | none |
| retrieval completeness | located official definitions, policies, checklists, DCC report, CMC and SI documents | used identical frozen corpus | none |
| false-positive risk | field-native distinctions separate valid summary, reference, decision, and implementation defect | initially risks calling all compression or delegation “loss” | generic audit has higher risk unless constrained by native terms |
| terminology precision | high: result, calibration, traceability, CMC, uncertainty budget, conformity decision | lower: five broad fields and status labels | native terminology more precise |
| cross-chain overview | spread across specialized structures | supplied one ledger and diagram | generic audit easier to scan |
| documented implementation example | found missed certificate upload and DCC remedy | reclassified it as temporary inaccessibility | native duplicate; F1/F6 |
| 2019 SI judgment | definition dependency removed; separate realization uncertainties remain | called this definition closure, not a transfer | same judgment |

### Comparison result

No preregistered methodological success condition was satisfied. The only difference was cross-chain overview, explicitly excluded from the success conditions as sufficient evidence of methodology.

---

## 5. What generic vocabulary found

The generic representation found no technical issue absent from the control. It contributed only:

1. a five-field visual index spanning different document types;
2. a uniform reminder to check recoverability before calling an omission a loss;
3. a common table for displaying where information is explicit, transformed, delegated, or restricted;
4. an explicit false-positive check across the three chains.

These may help teaching, interdisciplinary orientation, or preparation of a later audit. In this case they did not change any scientific or operational judgment.

---

## 6. What the control already found

The field-native control independently and earlier found:

- the result-specific nature of traceability;
- the need for a documented unbroken calibration chain with uncertainty contributions;
- the distinction between a calibrated instrument and a traceable later result;
- user responsibility to include certificate uncertainty and later effects;
- the importance of method, range, environmental conditions, and corrections;
- the role of CMC/accreditation scope;
- the NPL–NCC manual-upload problem and machine-readable remedy;
- the conditions under which binary conformity reporting is legitimate;
- the risk of unsupported reuse of a conformity statement;
- the separate roles of SI definition, realization, dissemination, calibration, and user measurement.

Thus the generic audit neither accelerated the first discovery in the fixed sequence nor supplied a different interpretation of the evidence.

---

## 7. What the generic audit falsely risked flagging

| Candidate flag | Correct field-native reading | False-positive disposition |
|---|---|---|
| full certificate not printed in every asset view | controlled summary can point to an accessible source record | legitimate abstraction (F4) |
| upstream primary-realization detail absent from user report | documentary chain and scoped CMC can validly carry the relation | redrawing/delegation (F3/F4) |
| \(x\pm U\) reduced to pass/fail | valid when the declared decision rule uses uncertainty and the record is retained | decision abstraction (F4/F5) |
| “SI traceable” shown as shorthand | valid only if the result-specific certificate/scope is resolvable | case-dependent; native criteria decide |
| uncertainty remains after fixing \(h\) exactly | practical realization uncertainty is not definition uncertainty | category error |
| an upload omission shows traceability-framework failure | DCC and document-control work already identify and remedy it | implementation failure (F6) |

The false-positive exercise is consequential: a generic scheme that counts all omitted detail will report more “problems” by confusing valid division of labor with invalid use.

---

## 8. What remained invisible to both

The comparison could not determine:

1. how often calibration-certificate fields are omitted or misused across laboratories and industrial users;
2. how often a downstream conformity decision cannot recover the original result, uncertainty, or decision rule;
3. whether DCC adoption measurably reduces incorrect uncertainty budgets or wrong decisions across organizations;
4. how reliably links to CMCs, certificates, and digital references remain resolvable over long periods;
5. how frequently unrecognized influence quantities escape validation;
6. whether a representative real-world sample would reveal systematic implementation failures not visible in normative documents.

These are empirical sampling and implementation questions. Their absence from this corpus does not establish either perfect preservation or a framework blind spot.

---

## 9. Closure counterexample result

### 9.1 Definition closure

The 2019 revision eliminated dependence of the kilogram’s definition on the International Prototype. Fixing the numerical value of \(h\) created an exact definition not tied to one artefact.

### 9.2 Realization and dissemination

Physical realization remains uncertain, as do consensus maintenance, dissemination, calibration, and eventual user measurements. Those are not uncertainty in the fixed definition.

### 9.3 Comparative consequence

The case counts against any generic picture in which a dependency must always reappear at another level in the same form. It instead supports a differentiated judgment:

- one specified dependency can close;
- other, operationally distinct uncertainties can remain;
- their remaining presence does not negate the closure.

This result was already reached by the control; the generic terminology does not earn independent credit for it.

---

## 10. Handoff-loss result

### 10.1 Strict loss finding

No inspected example satisfied all four preregistered requirements for `Lost`:

1. present upstream;
2. absent or distorted downstream;
3. decision-relevant downstream;
4. unrecoverable from accessible controlled records.

### 10.2 Closest example

The NPL–NCC case showed that failure to upload a certificate could delay evaluation and updating. It did not establish that the source certificate was irrecoverable. More importantly for the method comparison, the field-native report itself identified the issue and developed the DCC remedy. F1 and F6 therefore reject it as generic added value.

### 10.3 Normative versus actual practice

The official architecture strongly specifies what should be retained or linked. The empirical sample is too small to claim universal compliance. A future observed omission could be:

- an implementation failure already prohibited by the framework;
- an inadequacy in a local procedure;
- or, with stronger evidence, a limitation in the framework.

This case confirms only the first category in a published example.

---

## 11. Hypothesis and methodological-value verdict

### 11.1 H0 / H1 / H2

| Hypothesis | Final result | Basis |
|---|---|---|
| H0 — Field-native sufficiency | **RETAINED** | control reproduced every technical distinction and finding |
| H1 — Transfer-loss diagnostic | **NOT SUPPORTED** | no generic-only result survived F1–F6 |
| H2 — Explicit preservation / closure counterexample | **SUPPORTED for the studied corpus** | metrological architecture explicitly retains or links result, uncertainty, scope, reference, and decision information; kilogram supplies definition-level closure |

H2 is not a claim that all practice is compliant or no information is ever lost. It shows that loss is not structurally inevitable and that preservation can be institutionally engineered.

### 11.2 M0–M3

**Final classification: M1 — Organizational value.**

Rationale:

- the generic ledger makes a cross-chain overview easier;
- easier overview is not a preregistered methodological success;
- no missing condition, decision difference, scope correction, or retrieval improvement was unique to it;
- false positives had to be controlled using field-native distinctions;
- therefore M2 and M3 are not supported.

If organizational value is defined more narrowly than cross-chain indexing, M0 is also defensible. The conservative classification is M1 with explicit denial of diagnostic or methodological demonstration.

---

## 12. Implication for v0.4

### Recommended revision level: No revision

The result fits v0.4’s existing policy:

- use field-native terminology first;
- require an Erasure/control comparison;
- do not equate visibility with methodology;
- preserve the possibility that scientific guarantees are explicitly engineered;
- keep the methodological value of generic assurance provenance unproven.

This case supplies another negative calibration result but does not require a new concept or structural change. If recorded in a later working-note version, it should be a short case result, not a revision of the central thesis.

The live empirical question becomes narrower: in a representative set of actual downstream records, are result, uncertainty, scope, reference, and decision rule recoverable when needed, and does any generic procedure detect failures that ordinary certificate, uncertainty, document-control, and conformity reviews miss?

---

## 13. Next research decision

### 13.1 Do not infer universal preservation

The inspected architecture is strong; actual compliance is not established by normative documents alone. A larger audit would need linked records from calibration through use and decision.

### 13.2 Most informative next test

A real-protocol audit should sample, with permission and predetermined criteria:

1. a calibration certificate and its unique identifier;
2. the asset or laboratory record that consumes it;
3. the downstream uncertainty budget;
4. the applicable specification and decision rule;
5. the final reported or operational decision.

The field-native reviewer and generic reviewer should work independently on the same redacted records. Outcomes should include false positives, time to finding, retrieval completeness, and decision differences. Without such paired documents, claims about actual transfer failure remain underdetermined.

### 13.3 Prior-art direction

Before expanding the generic vocabulary, compare it directly with:

- metrological traceability audits;
- measurement assurance programs;
- digital calibration certificate validation;
- laboratory document control;
- conformity-assessment and decision-rule review;
- data/evidence provenance and assurance-case practice.

If those procedures reproduce the same checklist and results, the generic term should remain an optional index.

---

## 14. Answers to the preregistered final questions

### Q1. Does metrological traceability merely move upstream guarantees downstream, or explicitly preserve scope, uncertainty, and reference relations?

It explicitly constructs and documents a result-specific relation to a stated reference, with uncertainty contributed by each calibration. Certificate scope, CMCs, uncertainty budgets, and decision rules provide additional preservation mechanisms. This is more than unstructured transfer.

### Q2. Was an actual decision-relevant loss confirmed?

No. The closest public example was temporary certificate unavailability in an asset process; irrecoverability and a changed downstream decision were not established.

### Q3. Was the closest problem a blind spot in metrology or an implementation failure?

An implementation/document-control problem already identified by field-native DCC work, not a demonstrated blind spot in the metrology framework.

### Q4. Did the field-native control find the same problem?

Yes. It found the certificate-upload problem, scope and uncertainty risks, conformity-rule risks, and SI distinctions before the generic audit.

### Q5. Did the generic audit change a judgment?

No. It changed presentation and cross-chain visibility only.

### Q6. Is the 2019 SI revision dependency relocation or definition-level closure?

For the kilogram’s dependence on one defining artefact, it is definition-level closure. Realization and dissemination uncertainties remain as distinct measurement problems.

### Q7. What is the final M0–M3 classification?

**M1 — Organizational value**, with no demonstrated diagnostic or methodological added value. M0 remains a defensible stricter label; M2 and M3 are rejected by the preregistered criteria.

---

## 15. Final one-sentence judgment

**Metrology Case 02 did not show that a generic handoff-loss audit has methodological value beyond field-native traceability; it instead provided a strong example of how science can explicitly engineer the preservation, recoverability, scope, and decision use of measurement guarantees, while leaving actual implementation compliance as an empirical question.**

# Metrology Case 02 — Preregistration

## Traceability, Uncertainty, and Handoff Preservation

**Status:** preregistered and frozen before substantive literature analysis  
**Version:** 1.0  
**Freeze date:** 2026-08-16  
**Parent working note:** [tool_truth_absence_working_note_v0.4.md](./tool_truth_absence_working_note_v0.4.md)  
**Negative calibration baseline:** [GST Case 01 v0.2](./deferred_resolution_case_01_gst_v0.2.md)

> This file fixes the hypotheses, falsification conditions, corpus-selection rules, analysis order, and classification thresholds before the substantive metrology case is conducted.

---

## 1. Purpose

GST Case 01 found that generic audit vocabulary could be erased without losing any technical distinction or decision; field-native terminology was sometimes more precise. Metrology Case 02 therefore tests, rather than presumes, whether a generic assurance / transfer audit adds anything to established metrological practice.

The object is not to criticize metrology, establish a new theory of scientific inference, or revive a deferred-resolution hypothesis. The object is a head-to-head comparison:

1. reconstruct the case using metrology’s own concepts;
2. freeze that control reconstruction;
3. apply the generic vocabulary from v0.4 to the same corpus;
4. record any concrete difference in diagnosis, scope judgment, downstream decision, or retrieval;
5. count false positives as well as apparent findings.

Negative results count as complete results.

---

## 2. Research question

The central question is:

> To what extent are an upstream measurement result, its uncertainty, calibration conditions, validated scope, and traceability information preserved when the result is used downstream?

The methodological comparison asks:

> Does a generic assurance / transfer audit produce a diagnosis, decision, scope-preservation judgment, or retrieval benefit that a field-native metrology reconstruction does not?

This is not a claim that scientific problems are structurally deferred.

---

## 3. Field-native baseline requirement

The control reconstruction must be completed and frozen before the generic audit begins.

### 3.1 Vocabulary permitted in the control

The control may use established metrological vocabulary, including:

- metrological traceability;
- calibration and calibration hierarchy;
- reference standard and working standard;
- measurement result and measurand;
- measurement model and influence quantity;
- correction and calibration interval;
- measurement uncertainty;
- Type A and Type B evaluation;
- standard, combined standard, and expanded uncertainty;
- coverage probability / coverage interval;
- uncertainty budget;
- metrological compatibility and comparability;
- SI definition and realization;
- calibration and measurement capability;
- scope and fit for intended use;
- decision rule, guard band, conformity assessment, and statement of conformity;
- validity, verification, and validation.

### 3.2 Vocabulary prohibited in the control

The control must not use:

- assurance provenance;
- handoff loss;
- backgrounding;
- cross-impact;
- guarantee network;
- boundary relocation;
- Deferred Resolution.

Synonyms introduced solely to reproduce those generic categories are also prohibited. The control must solve the problem using field-native concepts.

### 3.3 Control freeze

After the control is written:

- its SHA-256 digest will be recorded;
- its source-corpus manifest will be frozen;
- its diagnoses and verdict will not be edited after the generic audit begins;
- later bibliographic corrections will be recorded in the comparison file rather than silently changing the control.

---

## 4. Hypotheses

### H0 — Field-native sufficiency

Metrology’s existing concepts adequately describe traceability, uncertainty propagation, calibration hierarchy, scope, reference dependence, and decision relevance. Generic audit vocabulary produces no additional judgment.

If H0 is retained, Case 02 is negative for methodological added value.

### H1 — Transfer-loss diagnostic

The relevant information exists in field-native documents, but a generic transfer audit finds at least one path in which upstream scope, uncertainty, assumptions, or reference information is lost or distorted in downstream use, and the field-native control does not find the same issue as clearly or as early.

H1 is supported only if at least one preregistered success condition in §6 survives all applicable falsification conditions in §5.

### H2 — Explicit preservation / closure counterexample

Metrology has already institutionalized preservation through calibration certificates, traceability chains, uncertainty budgets, scope statements, and decision rules. Decision-relevant information is substantially explicit or recoverable.

If H2 is supported, transfer loss is not a generic structural inevitability. H2 may coexist with H0. H2 does not require perfect practice or zero uncertainty.

---

## 5. Falsification conditions for added methodological value

Any apparent generic-audit finding is rejected as added methodological value if one or more of the following applies.

### F1 — Native duplicate

The field-native control found the same missing condition, invalid use, uncertainty problem, or traceability break.

### F2 — No judgment difference

Removing the generic vocabulary leaves the scope judgment and downstream decision unchanged.

### F3 — Redrawing only

The generic map is only a redrawing of a traceability chain, uncertainty budget, calibration certificate, or conformity-assessment workflow.

### F4 — Legitimate abstraction

The alleged loss is an intentional and valid abstraction, delegation, or summary for the stated downstream purpose.

### F5 — Decision irrelevance

The omitted information is not relevant to the declared downstream decision or intended use.

### F6 — Already prohibited or tested

A field-native standard, certificate rule, accreditation procedure, measurement model, or decision rule already prohibits or tests the alleged failure.

When F6 applies to an observed document defect, it is classified as an implementation failure, not a blind spot in the metrology framework.

---

## 6. Success conditions

Provisional methodological value requires at least one of the following, using the same documents as the control:

1. the generic audit finds a transfer failure missed by the field-native control;
2. the two analyses produce different scope judgments;
3. the generic audit changes a downstream decision;
4. it reproducibly finds an omitted uncertainty contribution;
5. it identifies overreach in a traceability statement’s scope;
6. it detects a cross-document inconsistency not found by the control;
7. it produces a demonstrable retrieval-completeness improvement.

“Easier overview,” “clearer diagram,” and “pedagogical convenience” do not satisfy these conditions.

### 6.1 Retrieval-benefit rule

A retrieval benefit counts only if:

- the generic analysis identifies a relevant official or primary document absent from the frozen control corpus;
- the document changes a diagnosis, scope judgment, or decision;
- the search path is recorded;
- a post hoc field-native query does not retrieve the same document with comparable directness.

Otherwise the result is ordinary search variation, not methodological value.

---

## 7. Case chains

The same three chains will be analyzed in both control and generic files.

### Chain A — Calibration certificate to downstream measurement

    reference standard
      → calibration laboratory
      → calibration certificate
      → working instrument
      → downstream measurement result

Fields to inspect:

- reported calibration result and correction;
- measurement uncertainty and coverage information;
- environmental / operating conditions;
- range and calibration scope;
- method;
- traceability statement and reference;
- calibration interval or user responsibility where stated;
- restrictions on use.

### Chain B — Measurement result to conformity decision

    measurement
      → reported result with uncertainty
      → specification / tolerance
      → declared decision rule
      → conformity decision

Fields to inspect:

- whether uncertainty enters the decision rule;
- guard band or acceptance limit;
- coverage assumptions;
- binary pass/fail compression;
- whether omitted detail is a valid decision abstraction;
- consumer’s risk and producer’s risk where the source treats them.

### Chain C — SI realization to laboratory traceability

    SI definition
      → practical realization
      → national metrology institute
      → accredited calibration laboratory
      → working standard
      → user measurement

Fields to inspect:

- distinction between definition and realization;
- reference chain;
- uncertainty accumulation;
- documentary transfer;
- comparability / key comparisons;
- where exact definition ends and realization, dissemination, and calibration uncertainty begin.

---

## 8. 2019 SI counterexample

The kilogram after the 2019 SI revision will be used as an explicit counterexample test.

### 8.1 Distinctions fixed in advance

- unit-definition uncertainty;
- realization uncertainty;
- dissemination uncertainty;
- calibration uncertainty.

The exact fixed numerical value of the Planck constant must not be read as eliminating all measurement uncertainty.

### 8.2 Definition-closure criterion

Classify the revision as definition-level closure if:

- the kilogram definition no longer depends on the mass or stability history of a unique material artefact;
- the fixed constant belongs to the definition;
- remaining realization and dissemination uncertainties are explicitly distinct measurement problems.

### 8.3 Relocation criterion

Classify it as dependency relocation only if the same artefact-specific definitional dependence is shown to persist in another stage with the same logical role. New realization difficulties or uncertainty contributions alone do not establish relocation.

No conclusion is preregistered.

---

## 9. Loss definition

The generic phase may use a temporary ledger

$$
O_{\mathrm{up}}=(\hat{\theta},U,A,S,R),
$$

where:

- \(\hat{\theta}\): measurement result / estimate;
- \(U\): uncertainty information;
- \(A\): assumptions, calibration conditions, and measurement model;
- \(S\): validated scope, measurand, range, environmental domain, intended use;
- \(R\): reference and traceability information.

For a downstream transformation

$$
O_{\mathrm{down}}=T(O_{\mathrm{up}}),
$$

each item is classified as:

- **Preserved**;
- **Transformed but recoverable**;
- **Delegated through a valid reference**;
- **Decision-irrelevant**;
- **Scope-restricted**;
- **Lost**;
- **Distorted**;
- **Unsupported transfer**.

The third status is not loss.

### 9.1 Strict loss rule

“Lost” requires all four:

1. the information exists upstream;
2. it disappears or changes downstream;
3. it is relevant to the declared downstream decision;
4. it cannot be recovered through an accessible cited document or reference.

A claim of a framework-level blind spot additionally requires:

5. field-native procedure permits the omission, or multiple documented implementations exhibit it despite conformity with the procedure.

Items satisfying only 1–4 remain possible local implementation failures.

### 9.2 No universal metric

No information-theoretic loss function is defined. Decision relevance and recoverability are judged case by case using the intended use and decision rule stated in the documents.

---

## 10. False-positive rule

The generic audit records a false positive whenever it initially labels as loss or unsupported transfer an item that is:

- a legitimate abstraction;
- validly delegated to an accessible standard or certificate;
- normal certificate summarization adequate for the intended use;
- irrelevant to the downstream decision;
- an exact SI definition rather than an uncertain measurement result.

False positives count against the generic audit. Finding more apparent issues is not success unless spurious issues are controlled.

---

## 11. Classification

No DR taxonomy will be used.

### M0 — No added value

The field-native control is sufficient. No success condition survives F1–F6.

### M1 — Organizational value

The generic audit improves overview, indexing, or pedagogy but changes no diagnosis, scope judgment, decision, or retrieval result.

### M2 — Diagnostic candidate

At least one success condition is reproducibly satisfied in at least one real chain, survives F1–F6, and is not offset by an uncorrected false positive. This is provisional and case-local.

### M3 — Methodological value demonstrated

At least two distinct real handoffs in different chains produce consistent diagnostic differences; at least one changes a scope judgment or downstream decision; the result is reproducible from a documented procedure; and false positives are explicitly controlled.

One case is presumed insufficient for M3 unless these unusually strong conditions are met.

---

## 12. Prior-art targets

The substantive audit will search official or primary sources in:

- metrological traceability;
- measurement assurance;
- uncertainty budgets and uncertainty propagation;
- calibration and measurement capability;
- quality infrastructure;
- conformity assessment and decision rules;
- calibration-certificate requirements and guidance;
- measurement-result and evidence traceability;
- data provenance where directly connected to measurement records;
- assurance / safety case literature only for comparison after metrology-native reconstruction.

Existing field-native names take priority.

---

## 13. Documents to inspect

The intended core corpus is:

1. VIM / JCGM 200, for metrological vocabulary and traceability;
2. GUM / current JCGM uncertainty guidance, for measurement models and uncertainty evaluation;
3. BIPM SI Brochure and official SI-realization materials;
4. official material on the 2019 SI revision and kilogram realization;
5. ISO/IEC 17025 material where publicly verifiable;
6. ILAC policy or guidance on metrological traceability;
7. JCGM or ILAC conformity-assessment / decision-rule guidance;
8. BIPM / CIPM material on comparisons and the KCDB;
9. at least one public calibration-certificate example or guidance document;
10. at least one public uncertainty budget or calibration service description;
11. at least one conformity-assessment example with a stated decision rule.

### 13.1 Corpus-selection rule

- Prefer official BIPM/JCGM/CIPM, ISO, ILAC, accreditation-body, and NMI sources.
- Use the most current official edition available, while preserving historically relevant 2019 documents.
- Record paywalls and inaccessible documents; do not infer their contents from secondary summaries.
- Do not claim sample representativeness.
- Use the same frozen corpus for the control and generic audit, except for a separately logged retrieval-benefit test under §6.1.

---

## 14. Fixed analysis plan

The analysis order is fixed:

1. freeze this preregistration and record its SHA-256;
2. collect the official/primary corpus using field-native search terms;
3. create a source manifest with title, issuing body, version/date, URL, role, and access status;
4. write the field-native control without prohibited generic terms;
5. record the control SHA-256 and freeze its diagnoses;
6. only then apply the generic ledger to the same chains and corpus;
7. classify each field as preserved, recoverable, validly delegated, irrelevant, restricted, lost, distorted, or unsupported;
8. apply the strict loss and false-positive rules;
9. conduct the head-to-head comparison;
10. classify the result M0–M3;
11. answer Q1–Q7 and state the implication for v0.4.

No hypothesis, falsification condition, success condition, loss criterion, or M0–M3 threshold will be changed after this freeze.

---

## 15. Results that cause rejection

The generic audit is rejected as a methodological addition if:

- the control already contains every diagnosis;
- alleged losses are recoverable through cited documents;
- alleged losses are decision-irrelevant;
- the generic diagram merely restates the traceability chain or uncertainty budget;
- any difference depends on a document added after seeing the generic result without satisfying §6.1;
- only educational or visual convenience remains;
- false positives erase the claimed diagnostic gain.

The recurrent-boundary or deferred-resolution reading is not tested as a positive hypothesis and will not be resurrected from this case.

---

## 16. Freeze statement

This preregistration was written before substantive metrology-source retrieval, control reconstruction, generic audit, or case classification. Subsequent files may report ambiguities in these criteria but may not revise them.

> **This preregistration is frozen before the substantive case analysis.**


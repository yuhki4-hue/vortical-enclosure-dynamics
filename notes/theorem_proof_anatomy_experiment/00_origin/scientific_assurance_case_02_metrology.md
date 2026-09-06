# Metrology Case 02 — Generic Comparative Audit

## Traceability, Uncertainty, and Transfer Preservation

**Status:** completed comparative audit; control remained frozen  
**Version:** 1.0  
**Analysis date:** 2026-08-16  
**Frozen preregistration SHA-256:** `9059e179dcf95263a2c9c9e23ee913ce465f74f8b5020e0876b89e1b6c8fd911`  
**Frozen control SHA-256:** `2767e82c5054dc18f2e4b6daed972e54277727b74a6c1c6a9a810fb0a3e93876`  
**Preregistration:** [scientific_assurance_case_02_metrology_preregistration.md](./scientific_assurance_case_02_metrology_preregistration.md)  
**Field-native control:** [scientific_assurance_case_02_metrology_control_reconstruction.md](./scientific_assurance_case_02_metrology_control_reconstruction.md)

> This file applies the generic vocabulary only after the preregistration and field-native control were frozen. It uses the same source corpus. It does not revise the control or treat an easier overview as methodological success.

---

## 1. Purpose

This audit asks whether a generic representation of scientific handoffs changes any diagnosis, scope judgment, downstream decision, or retrieval result already obtained with metrology’s own vocabulary.

The test is deliberately unfavorable to the generic vocabulary:

- VIM, GUM, JCGM 106, SI realization documents, ILAC policy, NIST guidance, and calibration-certificate practice are read in their strongest field-native form;
- `backgrounded` is not treated as `lost`;
- a certificate summary is not treated as defective when the controlled source remains recoverable;
- a binary decision is not treated as information loss merely because it is less detailed than the measurement report;
- a framework is not blamed for a documented implementation failure that its own procedures prohibit or detect;
- all apparent findings are tested against F1–F6 from the preregistration.

The audit does not test a deferred-resolution hypothesis and makes no claim about ontological closure.

---

## 2. Preregistered criteria

### 2.1 Hypotheses retained without modification

- **H0 — Field-native sufficiency:** metrological terminology suffices and generic terminology changes no judgment.
- **H1 — Transfer-loss diagnostic:** the generic audit finds a decision-relevant omission, distortion, unsupported transfer, or retrieval failure that the control did not find as clearly or as early.
- **H2 — Explicit preservation / closure counterexample:** traceability, certificates, uncertainty budgets, scope statements, and decision rules substantially preserve or make recoverable the information needed downstream.

### 2.2 Binding rejection rules

An apparent generic finding does not count when it is a native duplicate (F1), produces no judgment difference (F2), redraws an existing structure (F3), mistakes legitimate abstraction for loss (F4), concerns decision-irrelevant information (F5), or is already prohibited or tested by field-native practice (F6).

### 2.3 Binding loss rule

`Lost` requires all of the following:

1. the item existed upstream;
2. it disappeared or changed downstream;
3. it remained relevant to the downstream decision;
4. it could not be recovered from an accessible certificate, procedure, database, reference, or record.

Calling the defect a blind spot in metrology additionally requires evidence that the framework permits it rather than merely an implementation failing to comply.

---

## 3. Upstream ledger

For comparison only, write an upstream output as

\[
O_{\mathrm{up}}=(\hat\theta,U,A,S,R),
\]

where:

- \(\hat\theta\): measurement result, estimate, correction, or claim;
- \(U\): uncertainty information relevant to later use;
- \(A\): measurement model, calibration conditions, corrections, and operative assumptions;
- \(S\): validated measurand, method, range, environment, time, and intended-use scope;
- \(R\): reference and traceability information.

A downstream process produces

\[
O_{\mathrm{down}}=T(O_{\mathrm{up}}).
\]

This notation is an index, not a new measurement model. It does not imply that every component must be copied verbatim into every downstream document. The relevant question is whether the part needed for the declared downstream task is explicit or recoverable.

### 3.1 Status vocabulary

| Status | Meaning in this case |
|---|---|
| Preserved | Explicit in the downstream record |
| Transformed but recoverable | Re-expressed or summarized, with a controlled path to the source |
| Backgrounded with valid reference | Delegated to an accessible certificate, procedure, standard, CMC, or record |
| Decision-irrelevant | Not required for the declared downstream task |
| Scope-restricted | Valid only for stated conditions or use |
| Lost | Decision-relevant and not recoverable under the binding loss rule |
| Distorted | Meaning, uncertainty, or scope is changed materially |
| Unsupported transfer | Used outside the supported measurand, range, conditions, reference, or decision rule |

These statuses are not mutually exclusive across time. An item can be preserved in a certificate, backgrounded in an asset view, and later become unavailable through an implementation failure.

---

## 4. Chain A audit — Calibration certificate to downstream measurement

### 4.1 Chain

    reference standard
      → calibration laboratory
      → calibration certificate
      → working instrument
      → downstream measurement result

### 4.2 Ledger

| Component | At calibration certificate | At later measurement | Audit status | Native control already present? |
|---|---|---|---|---|
| \(\hat\theta\) | indication relation, correction, calibrated value | correction is applied or represented in the later model | Preserved or transformed; unsupported if ignored | Yes |
| \(U\) | expanded or standard uncertainty with coverage information | certificate contribution plus later contributions enter the new budget | Transformed but recoverable; distorted if treated as total later uncertainty | Yes |
| \(A\) | method, stated conditions, procedure reference | later method adds use-specific effects | Backgrounded with valid reference or scope-restricted | Yes |
| \(S\) | item, measurand, range, date, conditions, restrictions | intended use must remain within or justify extension | Scope-restricted; unsupported transfer if exceeded | Yes |
| \(R\) | traceability statement and stated reference | certificate/CMC chain can be cited rather than reproduced | Backgrounded with valid reference | Yes |

### 4.3 Public document-flow example

The NPL–NCC DCC demonstrator supplies the strongest real example in the inspected corpus. Under the prior PDF/paper process, the certificate owner had to upload the document to the asset-management system. If that step was missed, staff could be delayed in judging suitability or updating an uncertainty budget. Structured XML transfer improved data availability and accuracy.

The generic ledger can display the consequences in one row: \((\hat\theta,U,A,S,R)\) becomes temporarily unavailable at the point of use. But this does not satisfy H1:

- the field-native control independently found the same defect (**F1**);
- the NPL report itself describes the process problem and remedy (**F6**);
- the source certificate was not shown to be irrecoverably absent, so the strict `Lost` criterion is not established;
- the generic vocabulary changes neither diagnosis nor remedy (**F2**).

The case is therefore an implementation and retrieval example already illuminated by digital-calibration-certificate work, not a new generic diagnosis.

### 4.4 Bare “SI traceable” statements

A bare user-interface label may omit chain, uncertainty, and scope. Its audit status depends on the referenced record:

- if the label resolves to the applicable certificate and service scope, the information is **backgrounded with valid reference**;
- if the label is used as a blanket property of an organization or instrument with no result-specific record, it is an **unsupported transfer**;
- if the record exists but is inaccessible to the user making the decision, it may be an implementation defect;
- if the missing detail is irrelevant to the declared task, the abbreviation is not a failure.

VIM, ILAC P10, and NIST already make the same distinctions. The ledger adds no new rule.

---

## 5. Chain B audit — Measurement result to conformity decision

### 5.1 Chain

    measurement result (x, U)
      → specification and tolerance
      → decision rule / guard band
      → conformity statement
      → action

### 5.2 Ledger

| Component | Before decision | In/after decision | Audit status | Native control already present? |
|---|---|---|---|---|
| \(\hat\theta\) | measured value | often summarized as conform/nonconform | Transformed; recoverable from report | Yes |
| \(U\) | expanded or standard uncertainty | incorporated into decision rule/guard band; not necessarily printed in a short status view | Transformed but recoverable | Yes |
| \(A\) | measurement model and distributional assumptions | decision rule has its own stated assumptions | Backgrounded with valid reference | Yes |
| \(S\) | measurand and measurement conditions | specification, tolerance, and intended action | Scope-restricted | Yes |
| \(R\) | certificate and reference chain supporting the result | usually retained in the measurement record rather than the binary output | Backgrounded with valid reference | Yes |

### 5.3 Is \(x\pm U\rightarrow x\) or “pass” a loss?

Not by itself. Three cases must be separated:

1. **Valid decision abstraction.** A declared decision rule uses the uncertainty and the binary output is used only for the declared purpose. The result is less detailed but decision-adequate.
2. **Recoverable summary.** A dashboard displays a value or status while the report, uncertainty, and rule remain linked and accessible.
3. **Unsupported reuse.** A later party uses the value or “pass” under a new tolerance, measurand, or risk policy without the supporting result and decision rule.

Only the third is a failure. JCGM 106 and ILAC guidance already diagnose it. Treating every binary output as lost information would create a false positive under F4 and F5.

### 5.4 Empirical limit

The official corpus contains standards, guidance, and worked decision examples but no representative public collection of linked customer records from result through actual conformity action. Consequently:

- normative preservation requirements can be established;
- possible misuse can be specified;
- the frequency of actual decision-relevant omission cannot be estimated;
- no generic-only failure can be demonstrated.

---

## 6. Chain C audit — SI realization to laboratory traceability

### 6.1 Chain

    SI definition
      → primary realization
      → NMI result and uncertainty
      → comparison / CMC
      → accredited calibration result
      → working standard
      → user measurement result

### 6.2 Ledger by level

| Level | \(\hat\theta\) | \(U\) | \(A,S\) | \(R\) | Status at next level |
|---|---|---|---|---|---|
| SI definition | unit through exact defining constant | no uncertainty in fixed numerical value as a definition | defining equations and scope | SI | Preserved as reference |
| primary realization | realized quantity value | realization uncertainty | method, apparatus, conditions | SI definition / mise en pratique | Transformed and documented |
| NMI service | calibration result | service/result uncertainty | CMC method, quantity, range | NMI realization and comparisons | Scope-restricted, recoverable through KCDB |
| accredited laboratory | customer calibration result | reported uncertainty | accredited scope, method, conditions | NMI/accredited reference chain | Preserved in certificate |
| user result | measured value | combined uncertainty including upstream and local terms | user measurement model and conditions | stated traceability reference | New result; validity assessed for intended use |

### 6.3 What is and is not copied

The user’s report need not reproduce a primary-realization apparatus description, every key-comparison datum, or every upstream uncertainty-budget line. It must maintain a valid documented relation to the stated reference and incorporate the applicable uncertainty. Details can remain in controlled records, CMC entries, comparison reports, procedures, and certificates.

The generic graph is therefore a high-level redrawing of a calibration hierarchy and traceability chain (**F3**). It may aid orientation, but no scope judgment changes.

---

## 7. 2019 SI closure test

### 7.1 Preregistered question

Did replacement of the International Prototype of the Kilogram merely transfer the same dependency, or did it close one type of definition dependence?

### 7.2 Result

The numerical value of \(h\) is exact in the revised SI definition, and the definition no longer depends on the mass stability and custody of a unique material artefact. This is **definition closure** for that specified dependency.

Kibble-balance, XRCD, consensus-value, dissemination, and calibration uncertainties remain, but they attach to realizations and measurement results. They are not the old artefact’s definitional role under another name.

### 7.3 Audit judgment

- definition-level artefact dependency: closed;
- traceability to the SI: engineered through documented realization and calibration relations;
- realization and dissemination uncertainty: retained and quantitatively treated;
- universal absence of uncertainty: not claimed.

Interpreting every remaining uncertainty as movement of one underlying boundary would be a false positive. The 2019 revision supports H2’s counterexample role: some dependencies can be eliminated while different measurement uncertainties remain.

---

## 8. Backgrounding map

Here `backgrounded` means delegated with a controlled reference, not hidden or lost.

| Information foregrounded upstream | Typical downstream treatment | Valid when | Invalid when |
|---|---|---|---|
| primary realization details | referenced through NMI service and mise en pratique | relevant CMC/comparison records remain accessible | service scope or reference cannot be established |
| individual calibration-chain steps | summarized by result-specific traceability statement | chain is documented and uncertainties are included | “traceable” is asserted without result/reference evidence |
| certificate uncertainty components | combined into later uncertainty budget | contribution and correlation are correctly used | certificate uncertainty is omitted or treated as the total later uncertainty |
| environmental corrections | applied and recorded in result/model | use remains within validated conditions | environmental mismatch is ignored |
| full measurement result | summarized as conformity status | declared rule used and supporting record retained | status is reused for a different rule or tolerance |
| certificate fields | asset-system summary with link | source record is uniquely retrievable | document is stale, unresolvable, or inaccessible to the responsible user |

Metrology makes this division of labor explicit through certificate requirements, document control, CMCs, uncertainty budgets, and decision rules. The generic term does not reveal an unrecognized dependency in this corpus.

---

## 9. Handoff-preservation map

```text
SI definition
  ├─ fixed constant and unit definition
  └─ mise en pratique / realization methods
          ↓
primary or NMI result
  ├─ value and realization uncertainty
  ├─ comparison evidence
  └─ scoped CMC in KCDB
          ↓
calibration service
  ├─ item / measurand / method / range
  ├─ correction and uncertainty
  ├─ conditions and restrictions
  └─ stated reference relation
          ↓
user measurement model
  ├─ certificate contribution
  ├─ local influence quantities
  ├─ stability / environment / method
  └─ new result and combined uncertainty
          ↓
conformity assessment
  ├─ tolerance
  ├─ decision rule / guard band
  ├─ consumer and producer risks
  └─ scoped decision output
```

The graph clarifies where the type of object changes. It does not add a criterion absent from the field-native reconstruction. Each edge corresponds to an existing calibration, traceability, uncertainty-evaluation, or decision-rule relation.

---

## 10. Actual losses

### 10.1 Confirmed under the strict preregistered definition

**None in the inspected corpus.**

No inspected example established all four required conditions: upstream existence, downstream disappearance or distortion, downstream decision relevance, and inability to recover from an accessible controlled record.

### 10.2 Implementation problems observed or described

| Example | What occurred | Strict status | Why it does not support H1 |
|---|---|---|---|
| NPL–NCC manual certificate upload | certificate could be omitted from asset system, delaying suitability and budget updates | temporary accessibility / document-control defect | native source and control found it; F1, F2, F6 |
| PDF summary versus structured DCC | machine use may require re-entry or parsing | interoperability and retrieval limitation | field-native DCC program targets it; no generic decision difference |
| bare traceability shorthand | details may not appear in a local display | indeterminate without checking referenced certificate | can be valid summary or unsupported claim; native criteria decide |

These examples justify improved implementation, not a claim that metrological traceability lacks a preservation mechanism.

---

## 11. Legitimate abstractions

| Abstraction | Why it can be legitimate | Required safeguard |
|---|---|---|
| certificate summary in asset register | avoids copying a complete report into every view | persistent item/certificate identifier and retrievable source |
| CMC reference instead of full NMI method | reuses peer-reviewed scoped service record | correct CMC, range, method, and version |
| combined uncertainty instead of every component | provides the quantity needed for many downstream calculations | underlying budget controlled and correlations handled |
| pass/fail rather than full result | supplies the declared action output | result, uncertainty, tolerance, and decision rule retained where required |
| fixed SI unit definition | establishes reference without a calibration of the definition | realization uncertainty separately evaluated |

The generic audit initially makes these look like compressions. Field-native analysis determines whether they are valid. Compression alone is not failure.

---

## 12. False positives

The comparative vocabulary would produce false positives if applied mechanically.

1. **Binary conformity output as loss.** False when a declared decision rule validly consumes the uncertainty and the record remains available (F4/F5).
2. **Certificate reference as missing chain.** False when the certificate and controlled chain are resolvable and the display is only a summary (F3/F4).
3. **Exact \(h\) as displaced uncertainty.** False because definition exactness and realization uncertainty concern different objects.
4. **Every unprinted assumption as hidden.** False when a controlled method, standard, or certificate validly supplies it.
5. **Every implementation defect as framework defect.** False when ILAC, NIST, ISO/IEC 17025, or a laboratory procedure already prohibits or detects it (F6).

Avoiding these errors requires returning to field-native definitions. This lowers, rather than strengthens, the independent diagnostic standing of the generic vocabulary in this case.

---

## 13. Cross-impact

One upstream failure can affect multiple later results. The table retains multiple effects while identifying the field-native test with principal detection responsibility.

| Failure | Possible effects | Principal detection responsibility |
|---|---|---|
| reference-standard drift | calibration correction, CMC performance, user bias, conformity risk | stability monitoring, check standards, intercomparisons |
| certificate uncertainty omitted | user uncertainty budget, tolerance decision, claimed capability | measurement-model and uncertainty-budget review |
| wrong calibration scope | correction validity, traceability claim, fitness for use | certificate/scope review by provider and user |
| environmental mismatch | instrument correction, combined uncertainty, decision risk | environment monitoring and method validation |
| certificate not accessible | status verification, correction application, budget update | document control / asset management |
| unrecognized model effect | result, uncertainty, comparability, conformity | validation, residual analysis, proficiency testing, comparisons |

The map is a useful overview, but the same causal and documentary consequences appear in the control’s failure-mode table. It produces no registered success.

---

## 14. Prior-art comparison

The tested ideas have close or direct field-native counterparts.

| Generic comparison label | Field-native structure | Comparative judgment |
|---|---|---|
| assurance provenance | traceability statement, calibration hierarchy, uncertainty budget, certificate record, CMC | field-native terms are more specific |
| handoff preservation | documented unbroken chain, result-specific certificate, controlled records, DCC | already explicit and institutionalized |
| scope preservation | measurand, method, range, conditions, accredited scope, CMC, intended use | already explicit |
| uncertainty preservation | uncertainty propagation through the measurement model and calibration chain | already explicit |
| backgrounding with reference | document control, procedure reference, certificate/CMC citation | same practice under operational terms |
| transfer failure | invalid traceability claim, incomplete budget, out-of-scope use, document-control failure | already diagnosable |
| downstream decision support | JCGM 106 conformity assessment and decision rules | prior art is substantially more precise |
| evidence-chain digitization | DCC, machine-readable CMC identifiers, digital SI references | active field-native program |

Related areas—measurement assurance, quality infrastructure, conformity assessment, evidence traceability, data provenance, and safety/assurance cases—may offer broader comparison, but this case did not need them to reach its technical judgments. A wider literature audit may alter terminology history, not the present head-to-head result.

---

## 15. Generic vocabulary contribution

### 15.1 What it added

- one compact five-field index spanning three different metrological chains;
- a shared status list for explicit, transformed, delegated, restricted, and unsupported uses;
- an overview that places definition, calibration, uncertainty, scope, reference, and decision on one page;
- a prompt to count false positives and to ask whether a source record remains recoverable.

### 15.2 What it did not add

- no missing uncertainty component not already identified by the control;
- no new traceability break;
- no changed scope judgment;
- no changed conformity decision;
- no field-native document absent from the frozen corpus;
- no new remedy for the public DCC implementation example;
- no evidence that the metrology framework permits an otherwise unrecognized failure.

### 15.3 Retrieval result

The generic analysis used the frozen control corpus and retrieved no decision-relevant additional source. The preregistered retrieval-success condition therefore fails.

### 15.4 Interpretation

The five-field ledger makes an interdisciplinary summary easier to read. It is less precise than the combination of metrological traceability, measurement model, uncertainty budget, certificate scope, CMC, and decision rule. In this case it should remain an indexing device and must not replace those concepts.

---

## 16. M0–M3 provisional verdict

### 16.1 Hypothesis results

| Hypothesis | Result | Reason |
|---|---|---|
| H0 — Field-native sufficiency | **RETAINED** | all technical judgments and the real document-flow defect were recovered in the frozen control |
| H1 — Transfer-loss diagnostic | **NOT SUPPORTED** | no generic-only finding survived F1–F6 or the strict loss definition |
| H2 — Explicit preservation / closure counterexample | **SUPPORTED within this corpus** | traceability, uncertainty budgets, certificates, CMCs, decision rules, and DCC work explicitly preserve or make relevant information recoverable; the kilogram shows definition-level closure |

### 16.2 Falsification log

| Apparent generic finding | Applicable rejection condition | Disposition |
|---|---|---|
| missed certificate upload | F1, F2, F6 | rejected as added value |
| result compressed to pass/fail | F3, F4, F5 | rejected when rule/record valid; unsupported reuse already native |
| “SI traceable” short label | F1–F4 depending on record | no generic-only judgment |
| upstream detail not printed downstream | F3, F4, F5 | valid delegation unless required and unrecoverable |
| 2019 uncertainties remain | F2 plus object distinction | not evidence that definition dependency merely moved |

### 16.3 Classification

**Provisional classification: M1 — Organizational value.**

The ledger improves cross-chain visibility and can be pedagogically useful, but no preregistered diagnostic success occurred. M2 is not available because there is no reproducible diagnosis, scope judgment, decision, uncertainty finding, or retrieval result unique to the generic audit. M3 is therefore also excluded.

M0 remains a reasonable stricter interpretation if organizational usefulness is judged negligible. The final comparison adopts M1 only for the compact cross-chain index, not for methodological effectiveness.

---

## References

This audit uses exactly the frozen source corpus listed in the [field-native control](./scientific_assurance_case_02_metrology_control_reconstruction.md#source-corpus-manifest). No source was added after the control freeze.

---

## Provisional one-sentence result

**Metrology Case 02 did not show that the generic transfer audit exceeds field-native traceability practice; it provisionally showed organizational value only, while metrology itself supplied a strong example of explicitly engineered preservation and one definition-level closure.**

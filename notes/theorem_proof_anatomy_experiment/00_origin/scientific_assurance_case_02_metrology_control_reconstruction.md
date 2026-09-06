# Metrology Case 02 — Field-Native Control Reconstruction

## Traceability, Measurement Uncertainty, Calibration, and Downstream Use

**Status:** completed and frozen control reconstruction  
**Version:** 1.0  
**Control completion date:** 2026-08-16  
**Preregistered protocol:** [scientific_assurance_case_02_metrology_preregistration.md](./scientific_assurance_case_02_metrology_preregistration.md)

> This control uses metrological terminology only. It was completed before the comparative analysis and is not to be revised in response to that analysis. Its function is to establish what the field already says without the vocabulary under test.

---

## 1. VIM definitions

### 1.1 Measurement result

In the International Vocabulary of Metrology (VIM), a **measurement result** is not normally a bare number. It is a set of quantity values attributed to a measurand together with other available relevant information. The VIM notes that a result is generally expressed as one measured quantity value and a measurement uncertainty. The measurand therefore has to be specified with enough detail for the value and uncertainty to be interpreted.

This already blocks two common simplifications:

- treating the indicated value alone as the complete result;
- treating uncertainty as an optional annotation unrelated to the result’s meaning.

### 1.2 Measurement uncertainty

The VIM defines **measurement uncertainty** as a non-negative parameter characterizing the dispersion of quantity values attributed to a measurand on the basis of the information used. It may include components associated with corrections, standards, definitions, sampling, and other effects included in the measurement model.

Measurement uncertainty is not identical to a known error and is not a generic philosophical measure of ignorance. The result is evaluated using an explicit measurement model and available information.

### 1.3 Calibration

Calibration is a two-step operation. First, under specified conditions, it establishes a relation between values and uncertainties supplied by standards and corresponding indications and uncertainties. Second, that relation is used to obtain a measurement result from an indication. A calibration may be expressed through a statement, function, diagram, curve, or table, and may include an additive or multiplicative correction with an associated uncertainty.

Calibration is not adjustment. Nor does the fact that an instrument was calibrated by itself establish that every later result obtained with it is traceable or fit for purpose.

### 1.4 Calibration hierarchy and traceability chain

A **calibration hierarchy** is a sequence from a reference to the final measuring system in which each calibration outcome depends on the preceding outcome. The associated uncertainty necessarily accumulates through the hierarchy.

A **metrological traceability chain** is the sequence of standards and calibrations used to relate a measurement result to a reference. **Metrological traceability** is a property of a measurement result whereby it can be related to a reference through a documented unbroken chain of calibrations, each contributing to measurement uncertainty.

The VIM explicitly cautions that traceability alone does not guarantee:

- that the reported uncertainty is adequate for the intended use;
- that no error or mistake occurred;
- that the method, range, conditions, or measurand match the later use.

These are separate validity and fitness-for-purpose judgments.

---

## 2. GUM uncertainty structure

### 2.1 Measurement model

The Guide to the Expression of Uncertainty in Measurement (GUM) starts from a measurement model relating the output quantity to input quantities. In a simplified form,

\[
Y=f(X_1,\ldots,X_n).
\]

The input quantities may include readings, calibration corrections, reference values, environmental quantities, constants, and other influence quantities. Their uncertainty contributions and relevant correlations enter the evaluation of the uncertainty of the output estimate.

This structure makes the stated result conditional on:

- the definition of the measurand;
- the chosen model;
- the inputs and probability distributions assigned to them;
- corrections that have or have not been applied;
- covariance information where inputs are correlated;
- the operating and environmental conditions represented in the model.

### 2.2 Type A and Type B evaluations

The GUM distinguishes methods of evaluation, not kinds of uncertainty:

- **Type A evaluation** uses statistical analysis of series of observations.
- **Type B evaluation** uses other information, such as calibration certificates, manufacturers’ specifications, previous data, reference data, or scientific judgment.

Both feed into standard uncertainties. Under the GUM framework, individual standard uncertainties are combined using the measurement model and sensitivity coefficients, with correlations included where relevant. Expanded uncertainty may then be stated as

\[
U=k u_c,
\]

where \(u_c\) is the combined standard uncertainty and \(k\) is a coverage factor selected for the reporting purpose.

### 2.3 Sources and limits

The GUM lists sources such as incomplete definition of the measurand, imperfect realization, nonrepresentative sampling, environmental effects, instrument resolution, uncertain reference values, approximations in the procedure, and variation in repeated observations. The list is not a guarantee that every relevant effect has been recognized. An unrecognized effect cannot enter an uncertainty budget merely because the budget follows the GUM format.

The uncertainty statement is therefore model- and information-dependent, while remaining technically meaningful and quantitatively testable within its declared conditions.

### 2.4 Reporting

A report should contain enough information to permit the result to be used correctly and, where required, to permit the uncertainty evaluation to be understood or reproduced. Appropriate detail varies with the use. A concise certificate can validly refer to controlled procedures, standards, or attached records rather than reproducing every calculation.

The GUM does not by itself specify every conformity-assessment decision. That downstream problem is treated directly in JCGM 106 and related conformity-assessment guidance.

---

## 3. SI definition and realization

### 3.1 Definitions are not individual calibrations

The SI defines units through fixed numerical values of defining constants. A definition specifies the unit; a practical realization provides an experimental route by which values can be assigned in practice. A definition need not mandate one apparatus or one realization method.

The following must be kept distinct:

1. the exact numerical value fixed by the SI definition;
2. uncertainty in a practical realization;
3. uncertainty introduced in dissemination and calibration;
4. uncertainty of the user’s eventual measurement result.

Exactness at the first level does not eliminate uncertainty at the later levels.

### 3.2 Realization and dissemination

National metrology institutes realize units using primary methods, maintain standards, compare capabilities, and disseminate values through calibration services. The CIPM Mutual Recognition Arrangement (CIPM MRA), key comparisons, peer-reviewed Calibration and Measurement Capabilities (CMCs), and quality systems support international equivalence and confidence in stated capabilities.

The BIPM Key Comparison Database (KCDB) records comparison results and published CMCs. A CMC specifies, among other things, the quantity or instrument, method or service, range, and achievable uncertainty. A general statement that a service is traceable does not replace this stated scope.

---

## 4. Calibration and traceability

### 4.1 What a traceability claim requires

VIM, ILAC policy, and NIST guidance converge on several points:

- traceability belongs to a specified measurement result;
- the reference must be stated or identifiable;
- the calibration chain must be documented and unbroken;
- every calibration contributes to measurement uncertainty;
- the calibration service must cover the relevant measurand, method, range, and uncertainty;
- later use must account for additional effects after calibration;
- the user, not only the provider, has responsibilities for maintaining validity.

Calling an instrument, laboratory, or certificate simply “traceable” can be misleading if the particular result and reference relation are not specified.

### 4.2 Accredited and NMI routes

ILAC P10 identifies recognized routes for establishing traceability, including calibration by a national metrology institute whose service is covered in the KCDB or by an accredited calibration laboratory operating within its accredited scope. When those routes are unavailable and another route is used, additional evidence is required to demonstrate competence, an appropriate chain, and a defensible uncertainty evaluation.

ISO/IEC 17025 specifies general competence, impartiality, and consistent-operation requirements for testing and calibration laboratories. Accreditation does not make every possible measurement by the laboratory traceable: the relevant accredited scope and particular result still matter.

### 4.3 Provider and user responsibilities

NIST guidance divides responsibilities without treating the certificate as self-sufficient:

- the provider supplies a result, uncertainty, reference relation, method and conditions sufficient for the service;
- the customer determines whether the service meets the intended requirement;
- after return, the customer inspects and controls the item, applies corrections where required, observes intervals and environmental conditions, and incorporates the calibration uncertainty and later contributions into the uncertainty of subsequent results.

This division is part of established traceability practice rather than an omission in its definition.

---

## 5. Certificate and document flow

### 5.1 Expected certificate content

NIST SOP 1, ILAC P14, and laboratory accreditation practice call for content such as:

- title and unique identification;
- customer and calibrated item identification;
- calibration and issue dates;
- method and applicable procedure revision;
- relevant environmental or operating conditions;
- results, corrections, and units;
- measurement uncertainty, coverage factor or interval, and coverage probability where appropriate;
- reference and traceability information;
- restrictions, range, and scope;
- a statement of conformity only where requested, with the decision rule identified when necessary.

ILAC P14 states that reported uncertainty should normally be given as the measured quantity value and expanded uncertainty, with the coverage factor and coverage probability identified. A laboratory is not to report an uncertainty smaller than the applicable CMC.

### 5.2 Certificate limits

A calibration certificate describes a specific item and calibration at a particular time and under stated conditions. It does not by itself determine:

- how the item behaves after transport or over the next interval;
- whether later environmental conditions remain within range;
- whether the later measurand is the same;
- whether the user correctly applies a correction;
- whether the uncertainty is small enough for a particular tolerance;
- which conformity decision rule should be used.

These are addressed by customer procedures, measurement assurance, recalibration policies, later measurement models, and declared decision rules.

### 5.3 Digital calibration certificates

Digital Calibration Certificate (DCC) work makes certificate data machine-readable and links values, units, uncertainties, methods, and identifiers. A published NPL–NCC manufacturing case reported that a prior PDF or paper workflow depended on an owner manually uploading the certificate; omission could delay suitability assessment and uncertainty-budget updates. The demonstrator transferred structured XML into an asset-management system and improved availability and accuracy of calibration information.

The same report also records limits: secure authenticated provider-to-customer exchange was outside its demonstrated scope, and automatic transfer into one control system was constrained by that system’s architecture. These are implementation and interoperability questions identified in the field’s own documentation.

Unique, persistent CMC identifiers and the BIPM’s digital-reference work likewise aim to make the applicable service scope and version machine-resolvable rather than relying on a bare textual claim.

---

## 6. Conformity assessment and decision rules

### 6.1 From a result to a decision

JCGM 106 treats conformity assessment as an inference under uncertainty. A typical sequence is:

\[
\text{measurement result and uncertainty}
\rightarrow
\text{specified tolerance interval}
\rightarrow
\text{decision rule}
\rightarrow
\text{accept/reject or conform/nonconform statement}.
\]

A binary decision is not a replacement measurement result. It is a decision output produced for a declared purpose.

### 6.2 Guard bands and risks

A decision rule may set an acceptance interval narrower than the tolerance interval. The resulting guard band changes the balance between consumer’s risk and producer’s risk. Under particular distributional and uncertainty assumptions, a rule can bound the probability of false acceptance; the bound is conditional on those assumptions and the chosen rule.

Consequently, reduction from \(x\pm U\) to “pass” is legitimate when:

- the measurand and tolerance are defined;
- the uncertainty used is appropriate;
- the decision rule is declared or contractually established;
- the output is not subsequently represented as the full measurement result;
- relevant risk is accepted by the responsible parties.

It becomes invalid when a decision is made as if \(U=0\), when a different tolerance or purpose is silently substituted, or when the stated rule is not followed.

---

## 7. Chain A — Calibration certificate to downstream measurement

### 7.1 Field-native reconstruction

    reference standard
      → calibration of working instrument
      → calibration result and certificate
      → customer acceptance and instrument control
      → correction in a later measurement model
      → downstream measurement result with uncertainty

The certificate supplies a calibration result for the item. The customer’s later result is a new result whose uncertainty includes, as relevant:

- the certificate uncertainty;
- uncertainty of applying the correction;
- instrument resolution and repeatability;
- drift or stability since calibration;
- transport and handling effects;
- environmental differences;
- method and operator effects;
- differences between the calibration range and use range.

### 7.2 Native validity checks

The field-native checks are:

1. Is the item unambiguously identified?
2. Does the method and range cover the intended use?
3. Are the correction and uncertainty interpreted correctly?
4. Is the stated reference supported by an accepted route?
5. Were relevant conditions and restrictions recorded?
6. Has the customer included the calibration result in the later measurement model?
7. Is the item under continuing measurement assurance and interval review?
8. Is the resulting uncertainty fit for the intended use?

### 7.3 Findings

The standards and guidance explicitly cover these questions. The NPL–NCC example demonstrates a real documentary failure risk—failure to upload a certificate—and a machine-readable remedy. That example is not evidence that traceability theory lacks the relevant concept; the field itself identified the missing document flow and its consequences.

A certificate summarized in a local system is not deficient merely because the full document is not displayed at every use. If the unique record, scope, correction, and uncertainty remain accessible and the local procedure retrieves what the later measurement needs, the summary is controlled documentation. If the user cannot recover the applicable certificate or neglects its uncertainty, the later result lacks adequate support.

---

## 8. Chain B — Measurement result to conformity decision

### 8.1 Field-native reconstruction

    measured quantity value and uncertainty
      → specification and tolerance interval
      → selected decision rule and guard band
      → conformity statement
      → action for the declared use

### 8.2 Native validity checks

1. Does the specification apply to the identified measurand and item?
2. Is the uncertainty evaluation valid for the reported result?
3. Is the decision rule explicit, agreed, or prescribed?
4. Are guard bands and relevant risks treated consistently?
5. Does the report distinguish the measurement result from the conformity statement?
6. Is the conformity statement used only within the stated rule and scope?

### 8.3 Findings

The change from \(x\pm U\) to a binary conformity statement is not automatically an information defect. It is an intended decision operation. A recipient making only the declared decision may not require the entire uncertainty budget, while the supporting report must retain enough information to justify and review the rule.

If a later party reuses “pass” under a new tolerance, new risk policy, or different measurand without the original result and rule, that reuse is unsupported. JCGM 106 and ILAC conformity guidance already provide the concepts needed to diagnose it.

The inspected corpus contains authoritative rules and worked examples but not a representative sample of customer-specific end-to-end conformity records. It therefore does not establish the frequency of such misuse in practice.

---

## 9. Chain C — SI realization to laboratory traceability

### 9.1 Field-native reconstruction

    SI unit definition
      → primary realization or primary reference procedure
      → NMI standard and stated realization uncertainty
      → comparison and published CMC
      → accredited calibration service
      → working standard or instrument
      → user measurement result

### 9.2 Native validity checks

1. Is the reference the SI or another clearly stated reference?
2. Is the realization or reference procedure recognized and documented?
3. Is the NMI or laboratory service within its published CMC or accredited scope?
4. Is each calibration result accompanied by uncertainty?
5. Are comparison and quality-system evidence available where applicable?
6. Does each subsequent use add its own relevant uncertainty contributions?
7. Does the final result’s uncertainty meet the intended requirement?

### 9.3 Findings

The chain is not a claim that every detail of each realization is printed on the user’s result. It is a documented relation in which records can refer to other controlled records, CMCs, comparisons, procedures, and certificates. This documentary structure permits appropriate detail to remain at the responsible level while the particular result states the reference and uncertainty needed for its use.

The chain terminates at a stated reference for the purpose of metrological traceability. This is not an infinite calibration sequence: SI definitions and primary methods occupy roles different from ordinary calibrations. The uncertainty of a result remains nonzero even when its unit is exactly defined.

---

## 10. The 2019 SI revision and the kilogram

### 10.1 What changed

Before 20 May 2019, the kilogram was defined by the mass of the International Prototype of the Kilogram. The revised SI defines the kilogram by taking the numerical value of the Planck constant \(h\) to be exact in specified SI units. The definition no longer depends on the continued identity and stability of one material artefact.

This is a genuine **definition-level closure** of that particular artefact dependence. It should not be described as moving the same defining artefact to a higher calibration level.

### 10.2 What did not disappear

Practical realizations such as Kibble-balance and XRCD methods still yield realized mass values with measurement uncertainty. Dissemination through standards and calibrations adds further uncertainty. A fixed exact value of \(h\) does not make physical realization or user measurement exact.

BIPM consensus-value procedures illustrate the distinction. After reviewing independent realization data, the third consensus value for dissemination was scheduled for implementation on 1 March 2026 with an adjustment and a stated standard uncertainty. That uncertainty concerns the practical maintenance and dissemination of the mass scale, not uncertainty in the exact SI definition of \(h\).

### 10.3 Control judgment

The kilogram revision is a counterexample to any general claim that every dependency can only be shifted rather than removed. One specified form of definitional dependence was eliminated. Distinct realization, dissemination, and calibration uncertainties remain because they concern different operations.

---

## 11. Failure modes

| Failure mode | Affected result or operation | Field-native diagnosis | Principal detection or control |
|---|---|---|---|
| reference-standard drift | calibration correction and later result | standard instability / interval inadequacy | check standards, control charts, recalibration, comparisons |
| omitted certificate uncertainty | downstream uncertainty | incomplete uncertainty budget | measurement-model review and uncertainty audit |
| wrong range or measurand | use of certificate | use outside calibration scope | certificate and method review |
| transport or handling change | item after calibration | stability or custody problem | receipt inspection, checks, intermediate verification |
| environmental mismatch | correction and uncertainty | unmodelled influence quantity | environmental monitoring and model validation |
| missing or stale certificate | instrument status | document-control failure | asset system, unique identifiers, status checks |
| ambiguous traceability statement | claimed reference relation | insufficiently specified traceability | certificate review, NIST/ILAC checklists, KCDB/CMC lookup |
| ignored correlations | combined uncertainty | incorrect uncertainty evaluation | covariance review and model audit |
| binary decision without a rule | conformity assessment | unspecified decision risk | contract/report review; JCGM 106 decision-rule check |
| use of “pass” for a new tolerance | later conformity decision | invalid reuse outside stated decision rule | retain result/rule; new conformity assessment |
| unrecognized influence | any measurement result | model inadequacy not represented in budget | method validation, intercomparison, proficiency testing, residual investigation |
| software or schema mismatch | digital certificate use | interoperability or data-validation failure | schema validation, controlled vocabulary, test exchange |

Several rows affect more than one result. The table identifies the principal field-native check without assigning each failure exclusively to a single document or laboratory function.

---

## 12. Existing safeguards

The corpus documents a layered set of safeguards:

- exact SI unit definitions and published mise en pratique documents;
- primary realizations and reference procedures;
- NMI comparisons and CIPM MRA review;
- published CMCs in the KCDB;
- ISO/IEC 17025 accreditation and scoped competence;
- ILAC policies for traceability and reported uncertainty;
- calibration certificates with result, uncertainty, method, item, date, conditions, and reference;
- customer assessment of fitness for intended use;
- measurement models and uncertainty budgets;
- measurement assurance, check standards, stability monitoring, and calibration-interval review;
- JCGM 106 decision rules, guard bands, and risk analysis;
- document control and emerging machine-readable DCCs.

No single safeguard makes a result universally valid. Their roles are already differentiated in metrology: definition, realization, calibration, uncertainty evaluation, validation, documentary control, and decision are not interchangeable.

---

## 13. Open limitations of this control

1. **Actual-practice sample.** The inspected public examples are illustrative, not statistically representative of calibration laboratories or industrial users.
2. **Conformity records.** No public end-to-end sample was found that links a specific certificate, later measurement model, and customer conformity decision with all internal records.
3. **Certificate diversity.** Legal-metrology, medical, chemical, dimensional, electrical, and accredited testing contexts use different certificate and decision requirements.
4. **Digital interoperability.** DCC formats and infrastructure are developing; field-level adoption, authentication, software validation, and long-term resolvability require further empirical study.
5. **Unrecognized effects.** A well-formed uncertainty budget can still omit an effect not discovered by validation or comparison.
6. **Fit for use.** Traceability does not by itself decide whether uncertainty is adequate for every user requirement.
7. **Framework versus implementation.** Public guidance can show what should be retained and checked, but not how reliably every organization complies.

These limitations justify more empirical document sampling. They do not by themselves show a defect in the definitions or institutional architecture.

---

## 14. Control verdict

Using field-native terminology alone, the case can already distinguish:

- a bare indication from a measurement result;
- calibration from adjustment and later use;
- traceability from fitness for purpose;
- unit definition from realization and dissemination;
- uncertainty evaluation from error correction;
- a calibration certificate from the user’s later measurement model;
- a measurement result from a conformity decision;
- a valid decision abstraction from unsupported reuse;
- normative requirements from failures of implementation.

The three chains are explicitly represented by existing concepts, documents, and institutional procedures. The NPL–NCC example identifies a concrete documentary defect and remedy using the field’s own analysis. The 2019 SI revision provides a clear example in which one kind of definition dependence was eliminated while separate realization and dissemination uncertainties remained.

**Control verdict:** the field-native reconstruction is sufficient to formulate the relevant validity checks, locate the public example of a documentary failure, distinguish legitimate summarization from invalid use, and separate definition-level exactness from practical measurement uncertainty. Whether another vocabulary changes a diagnosis must be tested against this frozen result rather than assumed.

---

## Source-corpus manifest

The control used the following official, primary, or authoritative materials. This manifest is frozen with the control.

1. JCGM, [Publications of the Joint Committee for Guides in Metrology](https://www.bipm.org/en/committees/jc/jcgm/publications).
2. JCGM 200:2012, [International Vocabulary of Metrology (VIM), 3rd ed.](https://doi.org/10.59161/JCGM200-2012).
3. VIM, [measurement result, §2.9](https://jcgm.bipm.org/vim/en/2.9.html).
4. VIM, [measurement uncertainty, §2.26](https://jcgm.bipm.org/vim/en/2.26.html).
5. VIM, [calibration, §2.39](https://jcgm.bipm.org/vim/en/2.39.html).
6. VIM, [calibration hierarchy, §2.40](https://jcgm.bipm.org/vim/en/2.40.html).
7. VIM, [metrological traceability, §2.41](https://jcgm.bipm.org/vim/en/2.41.html).
8. VIM, [metrological traceability chain, §2.42](https://jcgm.bipm.org/vim/en/2.42.html).
9. JCGM 100:2008, [Evaluation of measurement data—Guide to the expression of uncertainty in measurement](https://doi.org/10.59161/JCGM100-2008E).
10. JCGM 106:2012, [The role of measurement uncertainty in conformity assessment](https://doi.org/10.59161/JCGM106-2012).
11. BIPM, [The International System of Units (SI Brochure), 9th ed.](https://www.bipm.org/en/publications/si-brochure).
12. 26th CGPM, [Resolution 1 (2018): Revision of the SI](https://www.bipm.org/en/committees/cg/cgpm/26-2018/resolution-1).
13. BIPM, [SI base unit: kilogram](https://www.bipm.org/en/si-base-units/kilogram).
14. BIPM, [Practical realization of the kilogram](https://www.bipm.org/documents/20126/41489673/SI-App2-kilogram.pdf/5881b6b5-668d-5d2b-f12a-0ef8ca437176).
15. BIPM, [History of the kilogram](https://www.bipm.org/en/history-si/kilogram).
16. BIPM, [Third consensus value of the kilogram, implemented 1 March 2026](https://www.bipm.org/en/-/2025-02-24-third-consensus-value-of-the-kilogram-to-be-implemented-1).
17. BIPM, [The CIPM MRA and KCDB](https://www.bipm.org/en/cipm-mra/kcdb).
18. ILAC P10:07/2020, [Policy on Metrological Traceability of Measurement Results](https://ilac.org/?ddownload=123220).
19. ILAC P14:09/2020, [Policy for Measurement Uncertainty in Calibration](https://ilac.org/?ddownload=123348).
20. ILAC, [Guidance series, including ILAC-G8](https://ilac.org/publications-and-resources/ilac-guidance-series/).
21. ISO, [ISO/IEC 17025:2017—General requirements for the competence of testing and calibration laboratories](https://www.iso.org/standard/66912.html).
22. NIST, [Metrological Traceability: Frequently Asked Questions and NIST Policy](https://www.nist.gov/metrology/metrological-traceability).
23. NIST, [SOP 1—Preparation of Calibration Certificates](https://www.nist.gov/system/files/documents/2019/05/13/sop-1-calibration-certificate-preparation-20190506.pdf).
24. NISTIR 6969, [Good Laboratory Practices for Calibration Laboratories](https://www.nist.gov/document/nistir69692014092620160121revpdf).
25. NPL Report MS 56 (2024), [Digital Calibration Certificates for advanced manufacturing](https://eprintspublications.npl.co.uk/9984/1/MS56.pdf).
26. BIPM, [Unique persistent identifiers for CMC digital references](https://www.bipm.org/en/-/2023-06-23-new-CMC-digital-reference).
27. PTB, [Example Digital Calibration Certificate for gauge blocks](https://www.ptb.de/cms/fileadmin/exponate/dccexp/DCCforGaugeBlocks_2025.html).

---

## Freeze statement

**This field-native control reconstruction is frozen before the generic comparative audit. Subsequent analysis may cite it but must not edit its diagnoses, corpus, or verdict.**

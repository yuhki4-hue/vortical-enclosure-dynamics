# Reachability-oriented anatomy tests — independent cross-test audit v0.1

- **Primary objects:** the four reachability-oriented stress tests — [`1+1=2`](./theorem_proof_anatomy_reachability_test_1_plus_1_eq_2_v0.1_ja.md), [`addition commutativity`](./theorem_proof_anatomy_reachability_test_addition_commutativity_v0.1_ja.md), [`IVT`](./theorem_proof_anatomy_reachability_test_ivt_v0.1_ja.md), [`FTA`](./theorem_proof_anatomy_reachability_test_fta_v0.1_ja.md)
- **Background consulted:** [`theorem_proof_anatomy_v1.1_ja.md`](../01_theorem_anatomy/theorem_proof_anatomy_v1.1_ja.md); the proof-formation strand (blind readers, inter-reader adjudication, finite propositional prototype and its stress test / post-mortem)
- **Date:** 2026-09-06
- **Files modified:** none. This file is additive. Filename chosen by convention, since none was specified.

## 0. Posture

- **Independent cross-test audit.** The four tests' own verdicts were read, then re-decided from the material rather than aggregated.
- **Not a new theorem. Not a new proof theory. Not a new semantics. Not a new framework proposal.** No new score, no geometry, topology or metric of proofs, no metaphysical conclusion.
- **Negative results are preserved**, including the ones that count against the project.
- **Standard terminology is preferred wherever it fully explains a result.** Throughout this note: *reachability* → **derivability** (\(\Gamma\vdash\varphi\)); *route* → **proof / proof organization**; *constraint propagation* → **ordinary proof bookkeeping**; *imported theorem expansion* → **citation expansion / dependency tracing**; *setting migration* → **change of theory, structure, or interpretation**; *erasure levels* → the three separate questions named in §6. Where a project-local word is unavoidable it is marked as such.
- One methodological commitment governs the whole audit: **two proofs are two witnesses for an existential statement; necessity is a universal statement, and is never established by intersecting witnesses.**

---

## 1. The progression, reconstructed

### Test 1 — \(1+1=2\)

**Setup.** First-order logic with equality over \(\{0,S,+\}\); the two recursion equations for addition; numerals as abbreviations; a four-line calculation.

- **Strongest positive.** The Erasure Test was split into three questions that demand different evidence: *did this proof break*, *did derivability fail*, *did the setting or the claim change*. Applied to concrete cases (deleting the lemma \(\forall x(x+1=Sx)\); deleting `Add-S`; moving to \(\mathbb Z/2\mathbb Z\); reinterpreting `+` as \(\max\)), the three came apart cleanly.
- **Strongest negative.** *Reachability* is \(\Gamma\vdash\varphi\) rewritten; *proof as route* is a derivation rewritten. The test says so itself (Q1, Q2) and produced no new object, procedure, or invariant.
- **Killed.** "Everything fixed is an axiom." Theorem-as-a-new-kind-of-object. Any causal or truth-creating reading of proof.
- **Retained.** The three-way separation; the reading of \(\Gamma\vdash\varphi\) (not the bare formula) as the thing that compresses derivability information; definitions as things that make terms manipulable rather than things that create relations.
- **What it could not test.** Induction, nontrivial lemma dependence, genuinely different proofs. The test is explicit that this was the point of choosing it.

### Test 2 — addition commutativity

**What induction and helper lemmas bought.** Not length. Two things:

1. **A genuine non-derivability result.** Deleting the induction schema leaves a model of the remaining equations — a standard chain plus a bi-infinite chain — in which \(0+z_0\neq z_0+0\). By soundness, commutativity is not derivable from the reduced theory. This is the first time in the sequence that "the theorem fails, not just this proof" was *demonstrated* rather than gestured at.
2. **A sharp two-sided test of the lemma/assumption boundary.** \(L_1:\forall x(0+x=x)\) and \(L_2:\forall x\forall y(Sx+y=S(x+y))\) can be inlined or replaced by equality variants without touching the theory; yet their content is recoverable from commutativity plus the recursion equations. So they are derived resources that are neither arbitrary decoration nor theorem hypotheses.

- **Strongest positive.** *Deleting a named lemma is not deleting a hypothesis*, established in both directions.
- **Strongest negative.** The two proofs were homologous — the same lemmas with the induction variable swapped. Route diversity was **not** actually tested here, and the test says so.
- **Killed / retained.** Same as test 1, with the separation now supported by a countermodel rather than by inspection.

### Test 3 — IVT

**What heterogeneous proofs and citation expansion changed.** A second distinction became available: *what the written proof cites* versus *what appears when a citation is expanded* versus *what the theorem needs*.

- **Strongest positive.** Completeness is used openly in the supremum proof, is absent from the text of the connectedness proof, and reappears inside the standard proof of "\([a,b]\) is connected". The test refuses to read the reappearance as necessity, and correctly identifies that the \(\mathbb Q\) counterexample — not the reappearance — is what shows ordered-field axioms alone insufficient.
- **Strongest negative.** Heterogeneity is granularity-relative. At the level of displayed text the two proofs look independent; one expansion step later they partly converge. So "these proofs are independent" is a statement about a presentation, not about the theorem.
- **Killed.** Inferring necessity from two proofs sharing a resource. Treating displayed heterogeneity as presentation-independent. Treating citation expansion as a new method.
- **Retained.** The three-question split, now with a fourth thing to record: where in the citation chain a dependency sits.

### Test 4 — FTA

**What preregistering the expansion depth changed.** Levels 0/1/2 and a stop rule were fixed *before* comparing, and the argument-principle proof was rejected in advance as a route whose topological appearance dissolves into Cauchy theory one expansion step down.

- **Strongest positive.** Two things. (i) The two proofs did not converge: at Level 2 they share elementary compactness and continuity, but the cores remain Cauchy integral theory versus covering-space lifting. (ii) The shared resource is shared in name only — compactness globalizes a bound on a disk in one proof and globalizes local lifts over a parameter square in the other.
- **Strongest negative.** *No theorem-level necessity was established for any major proof resource.* Not completeness, not compactness, not Cauchy theory, not winding number. The only necessity results are statement-side: nonconstancy (\(p=1\)) and the finite-polynomial restriction (\(e^{z}\)).
- **Killed.** Reading \(\mathbb Q(i)\) as evidence about completeness (confounded with algebraic closure); calling the topological proof "purely topological"; treating expansion as more than dependency tracing.
- **Retained.** Name ≠ role; preregistration as a reproducibility device; the three-question split.

### The shape of the progression

Each test added one control and removed one excuse: test 1 removed "the vocabulary is doing work" (the target was too small to hide behind); test 2 removed "we cannot actually show non-derivability"; test 3 removed "the proofs' visible dependencies are the real ones"; test 4 removed "the comparison depth was chosen to suit the conclusion". That is a well-designed sequence. What it converged on is audited below.

---

## 2. The six candidate surviving distinctions

Ratings: *genuinely useful* (new analytic capability), *standard but useful* (already standard; the tests make it operational), *redundant*, *misleading*, *unsupported*.

### A. proof failure ≠ non-derivability ≠ change of setting or claim

**Standard but useful.** Each leg is elementary: a stalled proof attempt says nothing about \(\Gamma\vdash\varphi\); non-derivability is shown by a model plus soundness; a claim evaluated in a different structure is a different claim. What the tests add is the discipline of asking three questions where one was asked, and demanding a different kind of evidence for each (§6).

The value is unevenly distributed. The first two legs are standard logic and were already implicit in the anatomy. **The third leg carries most of the practical value**, because the error it blocks is one people actually make: reading \(1+1=0\) in \(\mathbb Z/2\mathbb Z\), the failure of IVT over \(\mathbb Q\), or \(x^2+1\) over \(\mathbb R\), as evidence against the original theorem. All four tests exercise it. Nothing here is new mathematics.

### B. cited dependency ≠ dependency found by expanding a citation ≠ evidence of necessity

**Standard but useful, with a significant caveat.** The three-level record is a real improvement in bookkeeping, and the IVT case is a clean demonstration.

The caveat is that the third level has a standard home the tests never enter. "Which resources does this theorem actually require?" is the subject of reverse mathematics, which answers it by fixing a weak base theory and asking what must be added. That framework already supplies precisely the evidence the tests keep saying they lack. And for one of the two targets the answer is known and cuts against the tests' framing: **the intermediate value theorem is provable in \(\mathrm{RCA}_0\)** — a standard result — so the "no-gap support" IVT needs is far weaker than the least-upper-bound axiom whose reappearance test 3 spends its central section tracking. By contrast the extreme value theorem on \([0,1]\) is equivalent to \(\mathrm{WKL}_0\) and Bolzano–Weierstrass to \(\mathrm{ACA}_0\) over \(\mathrm{RCA}_0\), so the question is not vacuous — it has graded, precise answers. (I have not verified FTA's base-theory status and do not assert it here; it should be checked against the literature rather than inferred from these tests.)

So B is useful as recording discipline and **misleading if read as the frontier of what can be known**. The tests treat theorem-level necessity as an open question requiring bespoke controls, when a standard instrument for exactly that question exists and was not used.

### C. same resource name ≠ same proof role ≠ theorem-level necessity

**Split rating.** The first inequality is **near-redundant**: that compactness does different work in different proofs is what having different proofs means, and "proof role" is nowhere defined — the FTA role table is an informal gloss and would not survive being used as a category. The second inequality is **standard but useful**: it blocks the inference "both proofs use \(X\), so \(X\) is what the theorem is about", which is genuinely tempting and genuinely invalid.

Recorded caution: if anything in this cluster were carried forward, it must be the guard, not the notion of "role".

### D. static theoremhood does not determine formation history

**Redundant** — not false, but adding nothing to what this project has already established elsewhere. \(\vdash\) is by definition existential over derivations, so it cannot record which derivation was found. The finite-propositional strand already established a sharper version of the same point: semantic and derivability facts do not identify the operation history, and the typed record carries all of it. D restates that in a setting with less control.

### E. named lemma or imported theorem ≠ theorem assumption

**Standard but useful**, and the most operationally valuable of the six. It is textbook logic — derived theorems are not axioms — but it is a real error in practice. Independent corroboration from the other strand: the proof-formation coder instructions warn explicitly against coding proof resources as assumption strengthening, and the adjudication material treats the diagonal lemma as a proof resource for exactly this reason. **Two independent strands of this project separately identified the assumption/resource boundary as both important and easy to get wrong.** That cross-strand agreement is worth more than either strand's own testimony.

### F. a dependency reappearing after expansion does not establish necessity

**Standard but useful, and the best-supported of the six.** It is the sharpest guard in the set because the fallacy it blocks *looks like* evidence: you traced a citation, found completeness, and it feels like discovery. Test 3 separates the trace from the \(\mathbb Q\) control cleanly; test 4 declines to promote shared compactness. This is standard — necessity requires a non-derivability or independence argument — but the tests make the discipline concrete.

**Summary of §2.** None of the six is genuinely new. Four are standard distinctions made operational (A, B, E, F), one is redundant with the project's own prior results (D), and one is half trivial and half a useful guard (C).

---

## 3. The technical content without project-local vocabulary

Restating all four tests using only standard terms:

**Test 1.** A derivation of \(1+1=2\) from the recursion equations for addition, numeral abbreviations, and equality reasoning. Deleting either recursion equation yields a reduced theory with a model satisfying the remainder in which the target fails, hence non-derivability by soundness. Renaming symbols yields an isomorphic presentation in which the corresponding statement is derivable. Evaluating the string in \(\mathbb Z/2\mathbb Z\), or reinterpreting `+` as \(\max\), evaluates a different statement.

**Test 2.** Induction proofs of \(0+x=x\), \(Sx+y=S(x+y)\), and commutativity, in first-order arithmetic with the recursion equations and full induction. The lemmas are derived, hence removable by inlining or by equality variants. Deleting the induction schema leaves a nonstandard model in which commutativity fails; by soundness it is not derivable. Reinterpreting the operation changes the statement.

**Test 3.** Two standard proofs of the intermediate value theorem: one via the supremum of the negative set, one via connectedness of \([a,b]\) transported through a continuous map. Tracing the citations of the second proof reaches the least-upper-bound property inside the standard proof that an interval is connected. Over \(\mathbb Q\), \(q^2-2\) is continuous and changes sign without a root: the ordered-field axioms alone do not prove the statement. A step function shows continuity is load-bearing; a two-point domain shows the interval hypothesis is.

**Test 4.** Two standard proofs of the fundamental theorem of algebra: one via Liouville's theorem applied to \(1/p\), one via the winding number of the image of a large circle. Citation tracing to a fixed depth shows the two use different libraries — Cauchy integral theory versus covering-space lifting — while both use elementary compactness and continuity for different purposes. \(e^{z}\) shows the polynomial restriction is load-bearing; \(p=1\) shows nonconstancy is; \(x^2+1\) over \(\mathbb R\) is a statement about a different field.

### After removing the bespoke vocabulary, is any genuinely new analytical structure left?

**NO.**

Every mathematical result above is standard, and the translation costs nothing. What remains after translation is not a structure but a **procedure**: ask three separate questions, demand a different kind of evidence for each, and fix the citation-expansion depth before comparing proofs. A procedure for recording an analysis is not an analytical structure. For the answer to be PARTIAL, at least one of the following would have had to appear in four tests, and none did: a property of a theorem invariant under choice of proof; a criterion for when two proofs are the same; a necessity result not obtainable by the standard counterexample-and-soundness method.

---

## 4. Novelty claims, harshly

| Claim | Verdict | Reason |
|---|---|---|
| reachability is more than derivability | **KILL** | Four tests, unanimous, and no test produced anything the notation \(\Gamma\vdash\varphi\) does not already carry. |
| proof-as-route is more than an ordinary derivation | **KILL** | Exhausted by derivation trees plus the order in which obligations were discharged — the latter being presentation, not proof. |
| proof as constraint propagation | **KILL** | The tests downgrade it to a gloss; independently, the gloss adds nothing to "a derivation shows how the hypotheses combine". A gloss that must always be accompanied by a warning not to read it causally is not carrying weight. |
| theorem as compressed reachability | **KILL** | True only in the form "\(\Gamma\vdash\varphi\) asserts the existence of some derivation", which is the definition of \(\vdash\). The bare-formula version is false and the corrected version is not a claim. |
| proof heterogeneity as a stable property | **DOWNGRADE** | FTA gives real evidence it is not purely an artifact of where expansion stops. But it remains relative to which two proofs were chosen and which standard proof of each cited theorem was expanded — the rejected argument-principle route shows heterogeneity can be manufactured or dissolved at the citation boundary. Retain as a comparative observation about a chosen pair of presentations; never as a property of a theorem. |
| dependency relocation as more than citation tracing | **KILL** as a novelty claim; the phenomenon itself is real and worth noting | Finding completeness inside the proof of a cited lemma is what following a reference does. Naming it does not make it a method. |

---

## 5. What actually improved relative to v1.1

v1.1 already contained: assumptions with object / ambient / background / definitional levels; condition types; closure roles; what fails if a condition is removed; the R0/R1/R2 residue labels; a `proof_resources` field with a representative proof; and the escape/closure/residual vocabulary marked as non-standard comparative description.

Two observations dominate this section.

**First: v1.1 already had the assumption/resource distinction, and already applied it to the exact case test 3 re-derives.** Its IVT entry states that the least-upper-bound property is a *proof resource* and not a second hypothesis on the function, and its note already records that a topological proof via connectedness exists alongside the supremum proof. So the IVT test's central content was present in v1.1 in compressed form. What the test added was two written proofs, explicit counterexamples, and the citation-expansion question.

**Second: the four tests produced no theorem-level necessity result that v1.1 had not already recorded.** The FTA test's only established necessity results are nonconstancy and the finite-polynomial restriction — which are v1.1's assumptions B and A for that theorem, with the field as C. The IVT test's necessity results are continuity, the interval domain, and the bracketing condition — v1.1's B, A, C, with the same three counterexamples. This is the strongest single finding of the present audit: **the sequence added evidence discipline, not necessity results.**

| Question | Answer |
|---|---|
| What is genuinely clearer now? | (i) That "the proof broke", "the theorem is not derivable", and "the setting changed" require different evidence — v1.1's `what_fails_if_removed` field mixes all three. (ii) Explicit countermodels replace gestures, most sharply the induction-free model in test 2. (iii) The depth of citation expansion is itself a choice, for which v1.1 has no slot at all — its `proof_resources` is a flat list that cannot express "resource of the cited theorem's chosen proof". |
| What was already implicitly present? | The assumption/resource separation (explicit, and applied to IVT completeness). The existence of multiple proofs (v1.1's note fields). The four hypothesis levels. |
| What new audit discipline was added? | Preregistering the expansion depth before comparing; requiring a model or independence argument for any non-derivability claim; refusing to infer necessity from resource intersection; rejecting in advance a proof whose apparent difference dissolves one citation down. |
| What became less useful? | R0/R1/R2. Test 1 explicitly declines to use them for its main diagnosis; **no test in the sequence uses R2 at all**, and R0/R1 did no work in any of the four. The escape/closure/blocking metaphors likewise did nothing in the reachability tests. |
| Which old terms should be narrowed or retired? | R0/R1/R2 should be narrowed to what v1.1 actually used them for — the condition-removal residue survey across 21 theorems, where the finding that R2 is rare and clustered in Stokes, Gauss–Bonnet, CRT and Bayes is a real v1.1 result. They should not travel into single-theorem anatomy. `closure_style` is already flagged in v1.1 as a non-exclusive summary label and should stay there. |

**Is splitting the Erasure Test into resource deletion / theory weakening / change of setting a real improvement or a rewording?**

**A real but small improvement, and the smallness matters.** It is real because it changes what you must produce: an alternative derivation, a countermodel, or a demonstration that the interpretation changed. Those are different obligations, and a single "Erasure Test" column invites reporting them identically. It is small because each of the three questions is individually standard, and because the split adds no analytic content — after the split you know exactly what you knew before, filed in three places instead of one. It is a change to the audit form, not to the anatomy.

---

## 6. Evidence-burden audit

This is where the sequence actually earned something. The pattern is one of logical form: some of these claims are existential and some are universal, and the tests' main achievement is refusing to discharge a universal claim with an existential witness.

| Claim | Logical form | Sufficient evidence | Not sufficient |
|---|---|---|---|
| **This proof fails** | existential-negative, about one text | Exhibit the step whose warrant is gone. Cheapest evidence in the set. | Says nothing about the theorem. |
| **Theoremhood survives** | existential | **One** alternative derivation in the same theory with the same target. Test 2's inlined lemmas; test 3's second proof after deleting the supremum construction; test 4's other proof after deleting Liouville. | A survey of proofs is unnecessary; conversely, failure to find one proves nothing. |
| **Non-derivability** | universal over derivations | A model of the reduced theory in which the target fails, plus soundness; or an independence argument. Test 2's bi-infinite chain; \(\mathbb Q\) with \(q^2-2\). | No number of failed proof attempts. No amount of citation tracing. |
| **A hypothesis is necessary** | existential counterexample to a modified statement | A counterexample to the statement with that hypothesis deleted or weakened, everything else fixed: the step function, \(D=\{-1,1\}\), \(e^{z}\), \(p=1\). | This establishes necessity **in this formulation**, never minimality, and never that no weaker hypothesis suffices. |
| **The setting migrated** | identity claim about the statement | Show that the interpretation of a non-logical symbol, the domain, or the object class changed. Preserved: the intended reading of every symbol and the object class; changed: the structure. | A truth-value comparison across the migration is not evidence about the original claim, in either direction. |
| **A proof resource is necessary for the theorem** | universal over proofs | Fix a base theory and show the theorem is not provable without the resource. The standard instrument is reverse mathematics. | **Route intersection is insufficient, for three independent reasons**: two proofs are two witnesses for an existential claim and constrain nothing about the remaining proof space; the intersection depends on how deep you expanded; and it depends on which standard proof of each cited theorem you expanded. Tests 3 and 4 both state the conclusion; neither adopts the instrument. |

The last row is the audit's central point. Across four tests, exactly **one** theory-side non-derivability result was produced — induction for commutativity, in a toy arithmetic theory — and it was produced by the standard method, a countermodel. For IVT and FTA, every major resource-necessity question was left open, while a standard field answers questions of precisely that form.

---

## 7. Citation expansion and the preregistered boundary

**Did preregistering the depth genuinely improve comparability, or only formalize an arbitrary stopping point?**

Both, and the four consequences must be separated:

| Aspect | Verdict |
|---|---|
| **Reproducibility** | **Genuine improvement.** A second reader can check the same comparison at the same depth, and post-hoc asymmetry — digging into one proof until it reaches the other's machinery while leaving the other shallow — is blocked. This is the real gain. |
| **Mathematical invariance** | **No gain whatsoever.** Nothing about either theorem is fixed by the choice. A comparison result stated at Level 2 is a fact about two documents at a chosen depth. |
| **Presentation dependence** | **Unchanged and central.** Which standard proof of each cited theorem is expanded remains a free choice, and in test 3 the entire completeness reappearance hinges on it: expand a different proof that an interval is connected and the trace changes. |
| **Foundation dependence** | **Unchanged.** What counts as a Level-2 node presupposes a foundational development. The stop rule marks claims below it as open, which is honest, but it does not make the boundary principled. |

The single most valuable thing preregistration bought is not in this table: it is that **it made the rejection of the argument-principle proof possible before the comparison, on a stated ground.** That rejection identifies something worth keeping — apparent heterogeneity can be an artifact of where a citation was cut — and it is exactly the kind of move that is worthless if made afterwards. That is a genuine methodological gain, and it is procedural rather than mathematical.

---

## 8. FTA-specific verdict

- **Is the surviving Level-2 heterogeneity a meaningful result?** Meaningful as a record, weak as a finding. It says: these two documents, expanded to this depth, cite different core libraries.
- **Is it merely expected proof-library diversity?** **Largely yes.** That FTA has analytic, topological and algebraic proofs using different machinery is a textbook commonplace; that is what "a different proof" means. The audit contribution is narrower: that the difference survived a *preregistered* expansion, which makes it a checkable claim rather than an impression. That is a small gain and should not be described as a discovery about FTA.
- **Does common compactness with different roles add anything methodologically?** **Yes, narrowly and only negatively:** it blocks "both use compactness, therefore compactness is the essential content". Nothing positive follows.
- **Is "same name ≠ same role" useful or trivial?** Trivial as mathematics, useful as a guard, and **dangerous if promoted.** "Proof role" is undefined; the role table is a plain-language gloss. It should never become a category, and the FTA test's own instruction not to promote it to a taxonomy should be honoured.
- **Does this justify stopping the sequence?** **Yes.** The heterogeneity question received a positive control here and a clear negative on novelty; the necessity question received a clear negative across all four. A fifth theorem chosen for variety would re-run a settled experiment.

---

## 9. What is missing

Only two things are genuinely missing. The others on the standard list — a formal carrier, route-equivalence criteria, theorem-identity criteria, proof-assistant formalization, non-mathematical examples — would either invent structure the tests showed is not needed, or verify mathematics that was never in doubt.

1. **A connection to a fixed-base-theory necessity framework — that is, reverse mathematics.** All four tests converge on the resource-necessity question and stop. This is not a small omission: it is the question the whole sequence is organized around, and there is a standard field whose entire business is answering it, with graded answers (\(\mathrm{RCA}_0\), \(\mathrm{WKL}_0\), \(\mathrm{ACA}_0\), …) rather than the binary the tests attempt. Until the sequence touches it, "theorem-level necessity" remains a placeholder in these documents.

2. **Reproduction by an independent reader.** All four tests are single-author. This project has already established, in the proof-formation strand with two blind readers and an adjudication, that segmentation and role assignment vary between readers and that the assumption/resource boundary is exactly where they vary. The anatomy tests use the same fragile judgments — which proof counts as a route, which node counts as a major import, where Level 2 stops — with no reader control at all. Given the project's own prior negative results, this gap is not hypothetical.

---

## 10. Is another theorem warranted?

**ONLY IF NEW FALSIFICATION QUESTION.**

Repetition is not warranted: heterogeneity has a positive control, the vocabulary has four unanimous negative results, and the necessity question will not be answered by a fifth informal expansion.

If one further test is run, the falsification question must be stated first, and it should be the one the sequence kept reaching and never answering:

> Does the informal necessity apparatus used in these tests — route intersection, citation expansion, weakening counterexamples — agree with the known answer when a known answer exists?

That question needs a target whose resource requirements are *precisely settled by external standard means*, so that the informal verdict can be checked against something rather than left open. **One candidate: the Bolzano–Weierstrass theorem.** It is already in v1.1, giving a baseline entry to compare against; its status over a weak base theory is a standard equivalence rather than an open question, so the test has an external check; and it targets the one distinction that stayed open in all four tests instead of re-testing the one that is settled. If that check is not part of the design, no further theorem should be tested.

---

## 11. Is v2 warranted?

**RETIRE the reachability-oriented rewrite entirely.**

Reasons, briefly:

1. The framing has now been falsified four times by its own tests. *Reachability*, *route*, and *constraint propagation* collapsed into derivability, proof organization, and proof bookkeeping in every single case, with no residue. "Postponing v2" implies a reachability-oriented v2 might still be written; four independent negatives say it should not be.
2. What survived is an evidence-burden discipline and a citation-depth protocol. Both are refinements of fields v1.1 already has, not a new anatomy. They belong as a narrowing of the existing Erasure Test, not as a rewrite.
3. The only genuinely new mathematical question the sequence raised — resource necessity — is not answerable by this apparatus and is answerable by a standard one that has not been used. Writing v2 now would freeze an apparatus at the point where it demonstrably stops.

The one document warranted is a short synthesis note recording the evidence-burden table of §6, the retirement of the project-local vocabulary, and the two gaps of §9. That is the second option on the list, and it is what "not writing v2" should look like — not a deferral, but a closing record.

---

## 12. Strongest surviving results

Three, chosen independently. All three are **methodological, not mathematical**; none is new.

### S1 — Different claims about a proof require different kinds of evidence

**Exact statement.** That a proof survives is existential and is discharged by exhibiting one alternative derivation. That a theorem is not derivable is universal and is discharged by a model plus soundness, or an independence argument. That a hypothesis is necessary is discharged by a counterexample to the weakened statement. These three obligations are not interchangeable, and no amount of the first discharges the second.

**Evidence.** Tests 2 (inlined lemmas versus the induction-free countermodel), 3 (second proof versus \(\mathbb Q\)), 4 (other proof versus \(e^{z}\) and \(p=1\)).

**Does not imply.** That necessity, minimality, or the exact strength of any resource was determined. It implies nothing about which proof is better, more natural, or more fundamental.

### S2 — A dependency you can see, or can find by following a citation, is not thereby necessary

**Exact statement.** Occurrence of a resource in a written proof, or in the chosen proof of a cited theorem, or in both of two proofs, is not evidence that the theorem requires it. Independent evidence of a different logical form is needed.

**Evidence.** Test 3 (completeness reappears in one expansion of interval connectedness; the \(\mathbb Q\) control, not the reappearance, does the work), test 4 (compactness appears in both expansions; no necessity follows, and the test declines to claim any).

**Does not imply.** That the resource is dispensable, or that the trace was uninformative — locating where a dependency sits is useful bookkeeping. It implies only that the trace and the necessity claim are different claims.

### S3 — Changing the structure changes the claim; it does not refute it

**Exact statement.** \(1+1=0\) in \(\mathbb Z/2\mathbb Z\), \(\max\) written as `+`, the failure of IVT over \(\mathbb Q\), and \(x^2+1\) over \(\mathbb R\) are statements about different structures. They bear on the original theorem only through an explicit comparison of what was preserved, and they are not counterexamples to it.

**Evidence.** All four tests; the only distinction exercised in every one.

**Does not imply.** That such migrations are uninformative — \(\mathbb Q\) genuinely shows ordered-field axioms alone are insufficient for IVT. It implies only that the informativeness runs through a preservation analysis, not through the truth-value comparison.

---

## 13. Strongest negative results

### N1 — The project-local vocabulary carries nothing

Four tests, four unanimous verdicts: *reachability* is derivability, *route* is proof organization, *constraint propagation* is bookkeeping, *citation expansion* is following references, *theorem as compressed reachability* is the definition of \(\vdash\). The translation in §3 costs nothing. This is the sequence's clearest and most valuable result, and it argues against the framing that produced it.

### N2 — The sequence produced no necessity result beyond what v1.1 already recorded

Every theorem-level necessity established across four tests is statement-side and already appears in v1.1's assumption tables: nonconstancy and the polynomial restriction for FTA; continuity, the interval domain and the bracketing condition for IVT. The one theory-side result — induction for commutativity — is in a toy arithmetic and was obtained by the standard countermodel method. For every major analytic or topological resource in tests 3 and 4, necessity is explicitly left open.

### N3 — Proof heterogeneity is a property of presentations, not of theorems

It varies with which two proofs are compared, with the expansion depth, and with which standard proof of each cited theorem is expanded. The rejected argument-principle route demonstrates directly that it can be manufactured at a citation boundary. Preregistration makes a heterogeneity claim checkable; it does not make it a property of the theorem.

---

## 14. Final verdict

**What survived.** An evidence-burden discipline: three questions with three different obligations (S1), a guard against reading a dependency trace as necessity (S2), and a guard against reading a structure change as refutation (S3). One procedural device: preregistering the citation-expansion depth, whose real value is that it permits a principled *pre*-rejection of proofs whose difference dissolves one step down.

**What collapsed.** The entire project-local vocabulary, in every test, without residue. Any claim that the anatomy sees something standard proof theory and dependency tracing do not. Any claim that route intersection bears on necessity. Any claim that heterogeneity is a property of a theorem.

**What should be kept.** The three-question split, as a narrowing of v1.1's existing Erasure Test rather than as a new apparatus. The evidence-burden table. The preregistration protocol, in the reproducibility role only. v1.1 itself, unchanged.

**What should be dropped.** The reachability framing and its vocabulary. R0/R1/R2 outside v1.1's original condition-removal survey. "Proof role" as anything more than a plain-language gloss. Any expectation that this apparatus will settle a necessity question.

**What should happen next.** Not v2. A short synthesis note that records §6, retires the vocabulary, and states the two gaps in §9 — the absent connection to a fixed-base-theory framework for necessity, and the absence of any independent reader reproduction. A fifth theorem only if the falsification question of §10 is adopted first.

---

**End of cross-test audit.** No framework was proposed, no v2 was created, no score, geometry, topology, metric or new terminology was introduced, no novelty was claimed from vocabulary, multiple proofs were not treated as evidence of necessity, citation expansion was not treated as logical necessity, structure migration was not treated as falsification, and negative results were preserved as the primary output.

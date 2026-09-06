# Theorem/proof anatomy — full-series independent audit v0.1

- **Primary objects:** [`v1.1`](../01_theorem_anatomy/theorem_proof_anatomy_v1.1_ja.md), [`synthesis/closure`](../05_reachability_stress/theorem_proof_anatomy_reachability_synthesis_closure_v0.1_ja.md), and the five pilots — [`closure / open remainder`](../06_theorem_proof_pilots/theorem_closure_open_remainder_pilot_v0.1_ja.md), [`judgment enrichment`](../06_theorem_proof_pilots/theorem_judgment_enrichment_boundary_pilot_v0.1_ja.md), [`quotient invariance`](../06_theorem_proof_pilots/theorem_proof_quotient_invariance_pilot_v0.1_ja.md), [`specification change`](../06_theorem_proof_pilots/theorem_specification_change_preservation_pilot_v0.1_ja.md), [`cross-calculus`](../06_theorem_proof_pilots/theorem_cross_calculus_proof_class_preservation_pilot_v0.1_ja.md)
- **Also read:** the four reachability stress tests, the [cross-test audit](../05_reachability_stress/theorem_proof_anatomy_reachability_cross_test_audit_v0.1.md), the quotient pilot's companion checker, and the proof-formation strand
- **Date:** 2026-09-06
- **Files modified:** none.

## 0. Stance

- **Independent cross-series audit.** Each document's own verdicts were read and then re-decided from the material.
- **Not a theorem. Not a new proof theory. Not a proposal for `theorem_proof_anatomy_v2`.** No new framework, score, geometry, taxonomy, or metaphysics.
- **No novelty inflation.** Where a result is a textbook fact, it is called a textbook fact.
- **Standard terminology preferred throughout.** Retired project-local vocabulary — reachability, route, constraint propagation, closure, open remainder, displacement — is not revived, including as explanatory shorthand.
- **Negative results are preserved** as the primary output.
- **Stated directly, since the audit is asked to say it if true:** *the entire series reduces to standard proof theory, standard metatheory, and one useful audit checklist.* The rest of this document is the evidence for that sentence and the delimitation of what the checklist is worth.

---

## 1. The actual progression

### Phase A — Reachability stress (four theorems, then a closure note)

**Asked:** what happens when proof resources, hypotheses, theories, or interpretations are altered?

**Killed:** *reachability* as anything beyond \(\Gamma\vdash\varphi\); *route* beyond derivation organization; *constraint propagation* beyond bookkeeping; citation expansion as a method; inferring necessity from resource intersection; heterogeneity as a property of a theorem.

**Retained:** that a broken proof, a non-derivability claim, and a change of structure require different evidence; that a cited or expanded dependency is not thereby necessary; that a structure change yields a different statement rather than a refutation.

**Closed by:** the synthesis note, which retired the rewrite outright rather than postponing it, and folded the survivor back into v1.1's Erasure Test as audit discipline. That closure decision is correct and I do not reopen it.

### Phase B — What theoremhood leaves unsettled

**Asked:** once \(\Gamma\vdash_R\varphi\) holds, which adjacent questions need not be answered?

**Result:** proof choice, dependency minimality, background rationale, canonical proof equivalence, and formation history are not encoded by the judgment, and in all four reused examples at least one of them actually varies while the judgment stands.

**Killed:** "closure" as added mathematics; open remainder as an object; hidden-essence search; reading the judgment's silence as unknowability.

**Retained:** that the judgment's silence is a fact about what an existential statement asserts, not about what can be known. The pilot's own verdict — "largely, but not entirely, a restatement of *a theorem can have multiple proofs*" — is accurate and generous to itself; my reading is that O1 is exactly that textbook fact, and O2/O3 are the logical-form distinction already won in Phase A.

### Phase C — Strengthening the statement

**Asked:** if an item the judgment left unspecified is added to it, what becomes settled, and what else must be fixed?

**Result:** adding a proof-term parameter settles which witness; adding finite deletion-minimality conjuncts settles minimality *within a fixed finite comparison class*. Each requires further specification — proof syntax and coding for the first; base, partition, deletion operation, and inclusion order for the second.

**Killed:** outward displacement; infinite regress; enrichment as a method; boundary/displacement as explanatory vocabulary.

**Retained:** that a stronger statement asserts more, and that the "more" is relative to explicitly fixed representation and comparison choices. The finite positive controls that terminated are the pilot's best work, because they refute the displacement principle rather than merely failing to support it.

### Phase D — Quotient within one calculus

**Asked:** in STLC with products under Curry–Howard, which raw distinctions disappear under α, β, η, and product equations?

**Result:** exactly the licensed bureaucracy disappears; \(\lambda p.\pi_1p\) and \(\lambda p.\pi_2p\) remain distinct classes of \(A\times A\to A\) at every level tested; class counts change as the relation changes.

**Killed:** quotient as essence extractor; intrinsic proof identity; unique canonical proof; unique normal form per term read as unique proof per proposition; the quotient class as theorem-intrinsic.

**Retained:** name the equality before saying two proofs are the same; keep inhabitant uniqueness separate from normal-form uniqueness.

### Phase E — Specification change

**Asked:** under renaming, added derived lemmas, definitional extension, and genuine strengthening, what is preserved?

**Result:** "preserved" decomposed into literal well-formedness, formula translation, forward derivability, reflection, semantic transport, proof translation, and raw proof identity — and the four transformations sit in four different cells. Renaming is an isomorphism; adding derived lemmas preserves the deductive closure while changing proofs; definitional extension is conservative for old-language formulas only; adding induction preserves forward but reflection fails, witnessed by the existing commutativity countermodel.

**Killed:** a single universal preservation notion; theorem-intrinsic preserved object.

**Retained:** state map, object, scope, direction, and evidence before saying "preserved".

### Phase F — Cross-calculus

**Asked:** does derivability equivalence lift to a correspondence between proof classes?

**Result:** ND ↔ STLC gives a constructorwise bijection because the rules and equations were matched by construction. ND ↔ LJ gives the same theorems, and yet the translation does not even descend to the quotient under raw LJ equality — one ND β-class maps to distinct raw LJ derivations. Adding cut, identity, and permutation equations restores well-definedness and one round trip; global surjectivity and the second round trip are left open, and the pilot says a coherence result from the literature would be needed.

**Killed:** same theorems ⇒ same proofs; cut-free ⇒ canonical; Curry–Howard ⇒ universal proof identity; translation ⇒ injectivity; injectivity + derivability equivalence ⇒ surjectivity.

**Retained:** the four separate checks — well-definedness, injectivity, surjectivity, round trips — and the fact that none of them follows from derivability equivalence.

**Shape of the whole.** Phase A altered things and asked what broke. B–C asked what a judgment does and does not assert. D–F asked when two proofs, two specifications, or two calculi count as the same. The series moved from theorem statements to proof objects, and its center of gravity moved with it.

---

## 2. Standard-terminology translation audit

| Working phrase | Standard replacement | Verdict |
|---|---|---|
| theorem closure | derivability in a fixed context, \(\Gamma\vdash_R\varphi\) | **Fully replaceable — retire entirely.** The pilot itself says it added nothing. |
| open remainder | the questions that judgment does not answer | **Fully replaceable — retire entirely.** "Remainder" suggests a residue with structure; there is none. |
| judgment enrichment | strengthening the statement; adding a conjunct or parameter | **Fully replaceable — retire.** Shorter and clearer in standard words. |
| quotient invariance | the quotient by a specified equivalence relation | **Potentially misleading — retire.** "Invariance" implies something theorem-intrinsic was found invariant; nothing was. The pilot's own conclusion is that classification tracks the chosen relation. |
| specification change preservation | translation, conservativity, monotonicity, reflection | **Potentially misleading — retire.** It names as one property what the pilot itself split into seven. |
| (cross-calculus) proof-class preservation | whether a proof translation descends to the quotients, and whether it is injective / surjective / an equivalence | **Fully replaceable — retire.** The standard vocabulary is more precise and already distinguishes the four checks. |
| proof witness, deletion-minimality, proof equality, conservativity, reflection | already standard | **Retain — these are the standard terms.** |
| evidence burden | burden of proof / what a claim of that logical form requires | **Useful descriptive shorthand — retain as descriptive only.** |
| reachability, route, constraint propagation, displacement, outward movement | retired in Phase A | **Killed; not revived here.** |

**One live residue.** The *bodies* of all five pilots retire their own vocabulary explicitly. The *filenames and titles* do not. A reader scanning the notes directory sees "quotient invariance pilot", "specification change preservation pilot", "judgment enrichment boundary pilot" and will reasonably infer a technical programme with named components. That inference is exactly what every one of those documents internally rejects. This is the only place where project-local vocabulary is still doing work, and it is doing it outside the documents that disowned it.

---

## 3. Novelty audit

Ratings: **A** standard textbook fact · **B** standard fact, useful as audit discipline · **C** standard facts combined in a mildly useful workflow · **D** potentially nontrivial methodological contribution · **E** mathematically novel.

| Result | Rating | Reason |
|---|---|---|
| theoremhood is derivability in a fixed context | **A** | This is the definition of \(\vdash\), not a finding. |
| theoremhood does not encode proof choice | **A** | Immediate: \(\vdash\) is existential over derivations. |
| stronger judgments contain more information | **A** | Adding a conjunct or a parameter. Nothing is at stake. |
| minimality depends on the comparison class | **A** | The definition of a minimal element in a preorder. |
| quotient depends on the equivalence relation | **A** | The definition of a quotient. |
| normalization does not imply a unique inhabitant | **A** | \(\lambda p.\pi_1p\) and \(\lambda p.\pi_2p\) inhabiting \(A\times A\to A\) is the standard first example in any type-theory course. |
| conservative extension preserves restricted consequences | **A** | The definition of conservative. |
| derivability equivalence does not imply a proof-class bijection | **A** as fact, **B** as discipline | Textbook proof theory — it is why proof identity is a subject at all. The loose inference is common enough that recording the counterexample has audit value. |
| a proof translation must respect proof equality to descend to the quotient | **A** as fact, **B** as discipline | The universal property of quotients, first weeks of algebra. Applying the check to a Gentzen translation and finding it fails on raw equality is a good concrete exercise, not a new observation. |
| the composite evidence-burden checklist (§12) | **C** | Standard facts assembled into a workflow that is genuinely usable. Not D: nothing in it would be news to a proof theorist, and it does not enable an analysis that was previously unavailable. |

**No result in the series rates D or E.** The single highest rating goes to a checklist, and the checklist is C. I record this as harshly as the material warrants: the mathematical content of six documents and one companion script is a set of definitions and one standard counterexample per phase.

---

## 4. What actually survived

Criterion: supported by at least two phases, not merely interesting. Five items.

**S1 — Match the evidence to the logical form of the claim.** One alternative derivation settles that theoremhood survives; a countermodel plus soundness is required for non-derivability; a counterexample to the weakened statement is required for hypothesis necessity. Never discharge a universal claim with an existential witness. *(Phases A, B, C, E.)*

**S2 — Theoremhood, proof witness, proof minimality, and proof identity are four questions, not four aspects of one.** Each has its own specification requirements and its own evidence. *(Phases B, C, D, F.)*

**S3 — Occurrence is not necessity.** A resource visible in a proof, found by expanding a citation, or shared by several proofs, is not thereby required by the theorem. *(Phases A, B.)*

**S4 — "The same proof" is meaningless until the equality is named.** Class membership tracks the chosen relation; changing the relation changes the classification; "intrinsic" identity did not appear at any level tested. *(Phases D, F.)*

**S5 — Carrying proof data across a translation is four separate checks, none implied by derivability equivalence:** well-definedness on classes, injectivity, surjectivity, and each round trip. *(Phases E, F.)*

---

## 5. What failed repeatedly

| Failed direction | Classification | Grounds |
|---|---|---|
| search for theorem essence | **conceptually ill-posed without more specification** | No document ever states what would count as an essence or how a candidate would be tested. It cannot be falsified because it was never a claim. |
| intrinsic proof identity | **conceptually ill-posed**, with falsifying evidence against every concrete reading | "Intrinsic" is undefined; once a calculus and an equality are fixed, identity exists and is relative to them. Phase D shows classification varies with the relation, which refutes each concrete candidate. |
| unique canonical proof | **genuinely falsified by examples** | Two distinct normal inhabitants of \(A\times A\to A\); two distinct cut-free LJ proofs. Real counterexamples, not absence of evidence. |
| theorem-intrinsic proof geometry | **conceptually ill-posed** and never attempted | It appears only in prohibition lists. Nothing was tested, so nothing was refuted. |
| a single universal preservation notion | **genuinely falsified** | Phase E exhibits four inequivalent notions realized by four transformations, including a clean forward-without-reflection case. |
| outward displacement principle | **genuinely falsified as a universal claim** | Phase C's finite controls terminated: fixing representation and comparison class settled the question without generating a successor question. |
| infinite regress | **merely unsupported**, and refuted as a universal claim | Never inferred; the termination controls block the general form. Nothing shows regress is impossible in other setups, and nothing needs to. |
| reachability as a new primitive | **genuinely falsified** | Lossless translation into standard terms in four independent tests. |
| quotient as essence extractor | **genuinely falsified** | The quotient removed exactly what the equations licensed and left \(F/G\) distinct; class counts move with the relation. |

The pattern: the *falsified* items are the ones that were made precise enough to test. The *ill-posed* ones are precisely the essence-shaped ones, and they were never made precise. That asymmetry is the series' central lesson about itself.

---

## 6. Does the series have a coherent structural result?

### Verdict: **Option 2 — a coherent methodological result, but no new mathematics.**

Not Option 4: nothing here approaches a proof-theoretic result. Every technical item is a definition or a standard counterexample, and every pilot's own kill criteria triggered on novelty. Not Option 3: no framework was built, and the pilots correctly refuse to build one; what exists is a checklist, and a checklist is not an analytical framework. 

The real choice is between 1 and 2, and it is close. What lifts it above Option 1 — a bag of textbook rediscoveries — is that the same diagnosis recurred six times under independent conditions, and it is a single diagnosis rather than six:

> Every question in the series that looked like a question *about the theorem* turned out to be a question about a relation that has to be fixed first — an equality, a comparison class, a map, a scope, a direction. Once fixed, the question became standard and answerable. Left unfixed, it was not hard; it was not yet a question.

That is one result, instantiated in six settings that do not overlap technically (arithmetic derivations, real analysis, complex analysis, STLC, propositional metatheory, sequent calculus). Six independent instantiations of one diagnosis is coherence. It is also, entirely, methodology.

I record the closeness of the call: strip the §12 table and the recurrence of the single diagnosis, and what remains is Option 1. The series earns Option 2 by a margin, not comfortably.

---

## 7. The emerging abstract picture

The candidate is *objects + predicates + equivalence relations + comparison relations + translations*, with *specify → select → identify → compare → translate*.

**Verdict: too broad to be informative**, because it is merely generic mathematics.

It is satisfied by essentially every comparative inquiry in mathematics, and by most outside it. It rules nothing out, predicts nothing, and does not tell you what to do in any specific case — which of the four Phase F checks to run, which equality to fix, what evidence a necessity claim needs. Everything actionable in the series lives at a level of detail this picture abstracts away.

There is a further reason not to keep it. Promoting a five-slot schema with an arrow diagram to the status of a synthesis is precisely the move that six pilots spent their kill criteria preventing. As a retrospective index — "Phase D varied the equivalence relation, Phase E varied the map" — it is harmless and mildly convenient. As a result, it is empty. **Do not promote it, do not name it, and do not put it in the synthesis as a finding.**

---

## 8. What happens when you anatomize a theorem?

The candidate answer is close but concedes too much — it implies the theorem gets decomposed. It does not.

> **Anatomizing a theorem does not decompose the theorem. It sorts the questions around the theorem by logical form and reveals that most of them are not about the theorem at all.** Derivability in a fixed context is settled by exhibiting one proof. Non-derivability needs a countermodel. Hypothesis necessity needs a counterexample to the weakened statement. Sameness of proofs needs a named equality. Preservation needs a named map, object, scope, and direction. The theorem fixes only the first; every other question is relative to a relation the analyst must supply, and is standard once supplied.

---

## 9. Where theorem anatomy ends and proof theory begins

| Item | Where it sits |
|---|---|
| assumptions, hypothesis roles, condition removal, counterexamples after weakening (v1.1, Phase A) | **Theorem anatomy proper.** These are about a theorem statement and its hypotheses. |
| what a derivability judgment does and does not assert (Phase B) | **Boundary.** About judgments, not about any particular theorem; the four theorems are illustrations, and any four would do. |
| strengthening a statement with a proof term or a minimality clause (Phase C) | **Ordinary logic.** The examples are interchangeable. |
| α/β/η quotients in STLC (Phase D) | **Type theory / structural proof theory.** No theorem-specific content survives; \(A\times A\to A\) is a type, not a theorem anyone was anatomizing. |
| conservativity, definitional extension, monotonicity, reflection (Phase E) | **Ordinary metatheory.** |
| Curry–Howard, Gentzen translation, cut elimination, permutation equations, proof identity (Phase F) | **Proof theory proper.** Nothing here is about anatomizing a theorem; it is about two calculi. |

**The label became too broad at Phase D and misleading at Phase F.** By the cross-calculus pilot, "theorem/proof anatomy" names an activity that has no theorem in it. This is not a criticism of the work — Phase F is the most technically careful document in the set — but the name should not travel with it. Continuing to file proof-identity exercises under "theorem anatomy" will make the series look like it claims a theorem-specific insight it explicitly disclaims.

---

## 10. Was the cross-calculus pilot the natural stopping point?

### **STOP WITH SYNTHESIS.**

The pilot itself identifies the honest reason: the remaining Pair B question — global surjectivity and the second round trip — needs a complete conversion system and a coherence result from the literature, not another informal pilot. Any further pilot in this direction reproduces textbook proof theory with fewer resources than the textbooks.

A synthesis is warranted, not because the series needs a capstone, but because the one artifact worth keeping (§12) is currently distributed across seven documents, each of which reconstructs part of it.

I deliberately do **not** choose ONE MORE CALIBRATION, although the external calibration recommended after Phase A — checking the informal necessity apparatus against a target whose strength is externally settled — remains unperformed. That item belongs to v1.1's Erasure Test, not to this pilot line, and folding it in as "the next pilot" would restart a series that should close. It should be recorded as open and separate.

---

## 11. Standard fields this series overlaps, in priority order

Pointers only; no literature review is started here.

1. **Proof identity / equality of proofs.** The closest field by a wide margin. When two proofs are the same, quotients by βη, translations that fail to descend, the search for canonical representatives — this is that field's founding subject matter. Phases D and F re-derive its opening moves.
2. **Curry–Howard and categorical proof theory.** Phase F Pair A *is* the Curry–Howard correspondence for the →,× fragment; "bijection up to βη" is its standard statement, and coherence results are where the well-definedness / injectivity / surjectivity decomposition is carried out properly.
3. **Structural proof theory: normalization, cut elimination, permutation equivalence.** Phases D and F. Worth noting sharply: **proof nets exist precisely as canonical representatives modulo the permutations that Phase F found it needed extra equations to handle.** The pilot's most novel-feeling difficulty is the standard motivation for an existing technology.
4. **Conservative and definitional extensions, interpretability.** Phase E, entirely.
5. **Reverse mathematics.** Phase A's unanswered necessity question, and the still-open calibration.
6. **Proof irrelevance.** Peripheral; relevant only to the quotient pilot's suggested next question.

---

## 12. Evidence-discipline audit

The series' most practical artifact. The middle column is the point: the required evidence follows from the logical form of the claim, not from the subject matter.

| Claim | Logical form | Evidence that suffices | Evidence that does not |
|---|---|---|---|
| **this proof fails** | negative, about one text | Exhibit the step whose warrant is gone | Says nothing about the theorem |
| **theoremhood survives** | existential | **One** alternative derivation in the same context and target | Failure to find one proves nothing |
| **theorem is non-derivable** | universal over derivations | Model of the reduced theory falsifying the target, plus soundness; or an independence argument | No number of failed attempts; no citation tracing |
| **a hypothesis is necessary** | existential counterexample to a modified statement | Counterexample with that hypothesis deleted or weakened, everything else fixed | Establishes necessity *in this formulation*, never minimality |
| **the setting changed** | identity claim about the statement | Show the interpretation, domain, or object class changed | A truth-value comparison across the change is not evidence either way |
| **derivability preserved (forward)** | universal over source derivations | Induction on derivations, or replay/substitution of translated proofs | Matching theorem sets on examples |
| **reflection holds** | universal, converse direction | A separate argument from target to source | Monotonicity gives forward only; Phase E's induction case is the standing counterexample |
| **a proof translation exists** | construction | Define it constructor by constructor; prove it preserves typing/derivations by induction | Existence of a theorem-set correspondence |
| **quotient map well-defined** | universal over equality generators | Check the translation on **each generator** of the source equality | One generator failure kills it — the raw LJ case |
| **injective on classes** | universal | A left inverse up to target equality, or separated images of two distinct classes | Existence of the translation |
| **surjective on classes** | universal | A right inverse, or a preimage for every target class | Injectivity plus derivability equivalence does not give it |
| **proof classes correspond** | conjunction of the above | Both round trips up to each side's equality | Any proper subset of the four checks |

Two honest annotations. The series **executed** rows 1–6 and 9–10; it left rows 11–12 open in the one case where they mattered; and row 7's positive direction was never needed. And nothing in this table is new — it is the standard logic of the claims, written out.

---

## 13. Strongest negative result

> **Every essence-shaped question in the series dissolved, on inspection, into a standard question that was underspecified — and became routine as soon as the missing relation was named.**

This is stronger than the alternatives because it *explains* them. "No new anatomy emerged" is a summary of it; "proof identity does not follow from theoremhood" is one instance; "no single preservation notion survived" is another; "everything is standard once the relation is fixed" is the same statement viewed from the other end. It is supported six times over in technically disjoint settings, and it is the one finding that predicts what would happen to a seventh pilot.

It also carries the sharpest self-diagnosis available: the questions the series could not falsify — essence, intrinsic identity, proof geometry — are exactly the ones it never specified enough to test. Their survival is not evidence for them.

---

## 14. Strongest surviving positive methodological result

> **Match the evidence to the logical form of the claim; never discharge a universal claim with an existential witness.**

Chosen over the runner-up ("name the equality or the map before claiming sameness or preservation") because it is the more general and the more operational of the two — the runner-up is one of its consequences — and because it is the only item in the series that changed what the authors *did* rather than what they said. After Phase A the documents produce countermodels where earlier work would have produced a remark, check equality generators where it would have asserted a correspondence, and mark global claims NOT ESTABLISHED where it would have inferred them. That is a visible change in practice, sustained across six documents, and it is exactly what §12 tabulates.

---

## 15. Retirement and closure judgments

| Item | Verdict |
|---|---|
| `theorem_proof_anatomy_v2` | **KILL.** Already retired in the synthesis note; confirmed. Nothing in Phases B–F re-opens it. |
| reachability framing | **KILL.** Confirmed retired. |
| closure / open remainder vocabulary | **RETIRE.** Never technical, and the pilot says so. Standard: "derivability in a fixed context" and "questions the judgment does not settle". |
| judgment enrichment as a technical term | **RETIRE.** "Strengthening the statement" is standard, shorter, and clearer. |
| quotient invariance as a technical term | **RETIRE** — and flagged **potentially misleading**, since "invariance" implies a theorem-intrinsic invariant that the pilot explicitly denies finding. |
| specification preservation as a technical term | **RETIRE.** It names as one property what its own pilot split into seven; conservativity, monotonicity, reflection, and translation are the precise words. |
| cross-calculus proof-class preservation as a technical term | **RETIRE.** Standard vocabulary — descends to the quotient, faithful, full, equivalence — is more precise and already distinguishes the four checks. |
| R0/R1/R2 beyond the original 21-theorem survey | **RETIRE.** No reachability test and no pilot used them; R2 was never used at all. They remain meaningful only inside v1.1's own condition-removal survey, where the finding that R2 is rare and clustered is a real v1.1 result. |
| essence / core search | **KILL.** Ill-posed, unfalsifiable as stated, and the source of every dissolved question in §13. |
| proof geometry | **KILL.** Never defined, never attempted, present only in prohibition lists. |

Nothing in the list is retained as a technical term. Two things are retained descriptively: "proof witness" and "evidence burden", the first because it is already standard and the second because it is plain English for a standard notion.

---

## 16. Final verdict

1. **What the series accomplished.** It tested a family of essence-shaped intuitions about theorems and proofs to destruction, in six technically disjoint settings, and replaced them with one usable audit checklist tying the required evidence to the logical form of the claim. It also produced clean, correct, small worked examples — the induction-free countermodel, the two projections, the raw LJ translation failure — that will serve as concrete anchors for the checklist.

2. **What it did not accomplish.** No new mathematics, no new anatomy, no invariant, no framework, no answer to any necessity question it raised, and no external calibration. It did not establish theorem-level necessity for a single major proof resource in any of the ten theorems touched.

3. **Strongest surviving result.** Match the evidence to the logical form of the claim (§14).

4. **Strongest negative result.** Every essence-shaped question dissolved into an underspecified standard question and became routine once the missing relation was named (§13).

5. **Did any mathematically new concept emerge?** **No.** Not one. The highest novelty rating anywhere in §3 is C, and it goes to a checklist.

6. **Should the series stop?** **Yes — stop with a synthesis** (§10). Further pilots would reproduce standard proof theory with fewer resources than the standard sources.

7. **What the final synthesis should contain.** The §12 evidence table; the retirement list of §15; the concrete worked counterexamples, cited to their pilots rather than restated; the statement that the label "theorem anatomy" stopped applying at Phase D; the two open items (external calibration; the Pair B coherence question, marked as requiring literature rather than a pilot). It should contain no schema, no arrow diagram, no five-slot picture, and no new term.

8. **Should v1.1 be revised, and how narrowly?** **Yes, in exactly one place and no further:** its `what_fails_if_removed` field currently mixes three claims — the displayed proof broke, the theorem is not derivable, the setting changed — under one heading, and its `proof_resources` field cannot express the depth at which a cited theorem was expanded. Splitting the first and adding a depth note to the second is the whole revision. The hypothesis-level scheme, the closure-role clusters, and the R0/R1/R2 survey should not be touched; they are v1.1's own results and none of the six later documents disturbed them.

9. **Is an external calibration still needed?** **Yes, and it remains unperformed.** Every necessity question in Phases A and B was left open, while a standard framework answers questions of that form. Until one anatomy record is checked against a target whose strength is externally settled, "necessary for the theorem" remains a placeholder in this corpus. This is a separate item from the pilot series and should not be used to keep the series open.

10. **One sentence.** *Anatomizing a theorem does not take the theorem apart; it sorts the questions around it by logical form, and shows that everything except derivability in a fixed context is relative to a relation you must name yourself — after which it is standard.*

---

**End of full-series audit.** No framework, score, geometry, taxonomy, metaphysics, or new terminology was proposed; no retired vocabulary was revived; no `theorem_proof_anatomy_v2` was created; no existing file was modified; negative results are the primary output.

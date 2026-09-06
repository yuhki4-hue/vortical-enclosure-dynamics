# Proof-Formation Independent Blind Reader 03 v0.1.1

**Reader role:** independent blind Reader 03  
**Input used:** `proof_formation_coder_instructions_v0.1.1.md` and `proof_formation_frozen_toy_corpus_v0.1.md` only  
**Scope:** qualitative claim-transition reconstruction; no adjudication, framework evaluation, score, rank, or cross-reader comparison

## Step 0 — Episode segmentation

Move coding was not begun until the following segmentation record was fixed. A frozen corpus item is treated as a container. Where a second segmentation remains source-compatible, the alternative is retained rather than resolved.

| Parent | Primary segmentation | Boundary status | Alternative segmentation retained |
|---|---|---|---|
| E01 | E01 | SOURCE-DERIVED | none |
| E02 | E02-a: universal self-containment claim withdrawal; E02-b: conditional finite-capacity proposition | SOURCE-DERIVED | none |
| E03 | E03 | SOURCE-DERIVED | none |
| E04 | E04 | SOURCE-DERIVED | none |
| E05 | E05-a: general equivalence correction/withdrawal; E05-b: conventional equivalence; E05-c: conditional model correspondence | AMBIGUOUS | One integrated revision episode with three differently qualified after-claims, or two episodes with E05-b/c combined as the replacement package |
| E06 | E06-a: whole-case verdict reversal; E06-b: mechanism/taxonomy demotion and field-native reconstruction | AMBIGUOUS | Split E06-b into separate mechanism-name and five-stage-taxonomy episodes |
| E07 | E07 | SOURCE-DERIVED | none |
| E08 | E08 | SOURCE-DERIVED | none |
| E09 | E09-a: P0 scope decision; E09-b: post-P1-reduced termination decision | SOURCE-DERIVED | none; the text expressly presents two successive premise failures |
| E10 | E10 | SOURCE-DERIVED | none |
| E11 | E11-a: S2 to S2* label decision; E11-b: reflection type/subject-shift reconstruction | AMBIGUOUS | One integrated stress-test episode in which the technical reconstruction is evidence for the S2* decision |
| E12 | E12-a: universal scalar to fixed-package calibration; E12-b: analyzed/evaluating theory architecture judgment | SOURCE-DERIVED | none; the source gives separate S2* and A2 judgments |

The blocks below implement the primary segmentation. Blocks belonging to an ambiguous alternative are dependent views of one source passage, not independent duplicated results.

## Coding blocks

### E01

```text
parent_corpus_item: E01
subepisode_id: E01

episode_boundary: From the proposed general “ontological non-uniqueness theorem” through the identity-map/basic-prior-art objection to withdrawal plus two retained distinctions.
alternative_segmentations: none

claim_identity: C-E01-GEN — observation-map noninjectivity as a new general ontological theorem
claim_before: If distinct worlds have the same log, unique recovery fails; this structure may be generalizable as a new “ontological non-uniqueness theorem.”
target_and_scope: Candidate worlds W, log space L, observation maps O:W→L; intended general claim and novelty beyond the conditional fact that a noninjective map has no left inverse.
obligation_type: formal theorem; literature/novelty claim

assumptions: For the conditional core, O(w1)=O(w2) for some w1≠w2. No condition forcing arbitrary relevant O to be noninjective is supplied.
proof_or_evidence_resources: Map/fiber reasoning; inverse-problem, identifiability, observational-equivalence, and quotient vocabulary; identity map O=id_W as counterexample to universal noninjectivity.
evaluation_or_decision_rules: A general theorem must establish source-local conditions that force noninjectivity and must contain more than the elementary no-left-inverse fact; otherwise the novelty/generalization target fails.

failure_witness: O=id_W is injective. The stated conditional is already the basic noninjective-map setup, absent an additional necessity theorem.
available_branches: BR-E01-1 — add and prove conditions under which O must be noninjective; explicitly mentioned, not taken here.
adopted_side_claims: C-E01-S1 — observational equivalence classes must be distinguished from adopted structural-isomorphism classes; C-E01-S2 — identifiability is relative to model class and experimental family.

move_taken: M15 (the proposed novelty is absorbed into existing inverse-problem/identifiability/quotient language); M17 (the new general theorem claim is withdrawn).
claim_after:
  A1: C-E01-GEN — no new general “ontological non-uniqueness theorem” is claimed.
  A2: C-E01-S1 — observational equivalence and adopted structural isomorphism are distinct.
  A3: C-E01-S2 — identifiability is model-class- and experiment-family-relative.
terminal_status:
  A1: withdrawn
  A2: established adopted side claim; not success of C-E01-GEN
  A3: established adopted side claim; not success of C-E01-GEN

provenance_label:
  claim_before: SOURCE-DERIVED
  episode_boundary: SOURCE-DERIVED
  dependencies: SOURCE-DERIVED, except the phrasing of the decision rule is INFERENCE from Excerpts 2–3
  failure_witness: SOURCE-DERIVED
  available_branches: SOURCE-DERIVED
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED for withdrawal; INFERENCE for M15 as the connection between the prior-art list and the after-vocabulary
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: The nonuniqueness conclusion is built into the noninjectivity antecedent unless a separate theorem forces that antecedent; this is target leakage in the proposed generalization.
source_excerpts_used: E01 Excerpts 1–3
uncertainties: The source does not decide whether a later restricted noninjectivity theorem will be attempted.
```

### E02-a

```text
parent_corpus_item: E02
subepisode_id: E02-a

episode_boundary: The universal implication from self-containment to non-identifiability, ending with its withdrawal and the weaker role assigned to self-containment.
alternative_segmentations: none; the later finite-capacity theorem is E02-b

claim_identity: C-E02-UNIV — self-containment implies universal non-identifiability
claim_before: Because an observer is a physical process inside the world, complete description of a world containing itself is generally impossible.
target_and_scope: Internal observers and self-containing worlds in general; conclusion is universal non-identifiability or impossibility of complete self-description.
obligation_type: formal theorem

assumptions: Self-containment alone; the observation is represented dynamically as W_t → (W_{t+1},l).
proof_or_evidence_resources: Finite encoding construction X=Ω×M; infinite-cardinality observation; quines and Kleene recursion; comparison with Breuer and Wolpert results and their extra conditions.
evaluation_or_decision_rules: Self-containment must entail noninjectivity without importing additional capacity, candidate-class, subsystem, output-semantics, or closure conditions.

failure_witness: For finite Ω and sufficient internal memory, (θ,m0)↦(θ,enc(θ)) records θ uniquely inside a closed system. Self-description is also possible in specified computational models, and infinite cardinality defeats the simple size argument.
available_branches: Add the extra conditions used by capacity or diagonal arguments; the specific finite-capacity branch is adopted separately in E02-b.
adopted_side_claims: C-E02-S1 — self-containment can help satisfy capacity/diagonal premises by including the observer state or output in the identification target, but is insufficient alone.

move_taken: M2 (weaken from self-containment being sufficient to it sometimes helping establish further premises); M17 (withdraw the universal implication).
claim_after:
  A1: C-E02-UNIV — self-containment alone does not imply universal non-identifiability.
  A2: C-E02-S1 — self-containment may contribute to additional capacity or diagonalization premises.
terminal_status:
  A1: withdrawn
  A2: established adopted side claim; not success of C-E02-UNIV

provenance_label:
  claim_before: SOURCE-DERIVED
  episode_boundary: SOURCE-DERIVED
  dependencies: SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED
  available_branches: SOURCE-DERIVED
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED for withdrawal; INFERENCE for M2 as the relation between the universal and retained claims
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: The failed inference treated self-location as if it already supplied capacity/diagonal hypotheses; the source explicitly separates them.
source_excerpts_used: E02 Excerpts 1–3
uncertainties: “Complete description” is not separately formalized from candidate identification in the excerpt.
```

### E02-b

```text
parent_corpus_item: E02
subepisode_id: E02-b

episode_boundary: The post-withdrawal construction of a finite conditional capacity proposition and the explicit statement of cases outside its reach.
alternative_segmentations: none; contextual countermodels are shared with E02-a but this is a distinct retained theorem obligation

claim_identity: C-E02-CAP — finite proper-subsystem recording capacity prevents injective answers on all initial states
claim_before: OPEN HYPOTHESIS: an impossibility result may remain after adding recording-location, candidate-range, and finite-capacity conditions to self-containment.
target_and_scope: Finite X=A×E, candidate set Ω=X, final records constrained to A, |E|>1; required conclusion: every r:X→A is noninjective.
obligation_type: formal theorem

assumptions: X=A×E is finite; Ω is all initial states X; every final record lies in the proper subsystem A; |E|>1.
proof_or_evidence_resources: Finite cardinality/pigeonhole comparison for r:X→A.
evaluation_or_decision_rules: The simple capacity conclusion is retained only inside the stated finite, full-candidate, proper-record-subsystem setting; it is not generalized to cases in which candidate restriction, environmental memory, external logs, or infinite cardinalities remove the size gap.

failure_witness: Obstacle to the broader version: smaller Ω, use of E as memory, external logs, or infinite cardinalities can invalidate the simple cardinality route. No witness defeats the stated finite proposition.
available_branches: Candidate restriction, environmental memory, external logging, and infinite-cardinality models are explicit alternative settings in which this proof route is unavailable; none is adopted as part of C-E02-CAP.
adopted_side_claims: none; C-E02-CAP is a distinct conditional claim, not preservation of C-E02-UNIV.

move_taken: M1 (add record-location, full-candidate, and capacity hypotheses); M4 (restrict the object/domain to the stated finite product setting and candidate class).
claim_after:
  A1: C-E02-CAP — under the stated finite conditions, every final-answer map r:X→A is noninjective.
terminal_status:
  A1: established conditional capacity proposition

provenance_label:
  claim_before: INFERENCE; the source states that the conditional proposition “remains,” rather than spelling out a separate prospective question
  episode_boundary: SOURCE-DERIVED
  dependencies: SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED as scope limits; NOT APPLICABLE as a refutation of the final conditional claim
  available_branches: SOURCE-DERIVED
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: No leakage identified for the stated finite proposition; the conclusion follows from explicit size conditions, which are acknowledged rather than attributed to self-containment alone.
source_excerpts_used: E02 Excerpts 2 and 4
uncertainties: The excerpt does not state whether A or E can be empty; the intended finite-cardinality argument appears to presuppose the ordinary nonempty-world setting.
```

### E03

```text
parent_corpus_item: E03
subepisode_id: E03

episode_boundary: From the proposed general generation–log non-isomorphism through definitional leakage/reversible countercases to withdrawal and two retained methodological distinctions.
alternative_segmentations: none

claim_identity: C-E03-NISO — the existence of generation/constraint/stabilization/log stages generally implies non-isomorphism or nonuniqueness
claim_before: Because a log arises through constraint formation and stabilization rather than copying generation dynamics, isomorphism between generation structure and stable-log space is generally lost.
target_and_scope: General generation processes and stable logs; required conclusion is non-isomorphism/nonuniqueness from the mere staged architecture.
obligation_type: formal theorem; interpretation or reduction

assumptions: A staged path generation→constraint formation→stabilization→log; no independent information-loss property is initially supplied.
proof_or_evidence_resources: Reversible/full-information countermodels; coarse graining, Blackwell comparison, sufficient statistics, bisimulation, and minimal-realization concepts.
evaluation_or_decision_rules: Information loss must be proved for a specified channel, statistic, dynamics, or equivalence relation and cannot be inserted by defining stabilization as many-to-one or recording as coarse graining.

failure_witness: Reversible, information-preserving processes and perfect encodings permit injection or isomorphism. Defining the intermediate maps to be lossy merely assumes the intended conclusion.
available_branches: Specify a concrete lossy channel/statistic/dynamics/equivalence and prove the loss; this route is retained only as a methodological requirement, not completed as a new theorem here.
adopted_side_claims: C-E03-S1 — information loss needs a concrete proof rather than an assumption; C-E03-S2 — Blackwell post-processing information and physically jointly executable measurement are distinct.

move_taken: M15 (the information-preservation question is returned to existing precise comparison/sufficiency/bisimulation language); M17 (withdraw the stage-existence implication).
claim_after:
  A1: C-E03-NISO — the mere existence of the stated stages does not imply non-isomorphism/nonuniqueness.
  A2: C-E03-S1 — concrete information loss must be proved source-locally.
  A3: C-E03-S2 — Blackwell information ordering is not identical to physical joint implementability.
terminal_status:
  A1: withdrawn
  A2: established adopted side claim
  A3: established adopted side claim

provenance_label:
  claim_before: SOURCE-DERIVED
  episode_boundary: SOURCE-DERIVED
  dependencies: SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED
  available_branches: SOURCE-DERIVED
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED for M17; INFERENCE for M15
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: Yes. If “stabilization” or “recording” is defined as many-to-one/coarse-grained, the desired non-isomorphism is placed in the setup.
source_excerpts_used: E03 Excerpts 1–3
uncertainties: The excerpt does not select one formal preservation notion for a future theorem.
```

### E04

```text
parent_corpus_item: E04
subepisode_id: E04

episode_boundary: From use of the destructive two-bit example as an internally generated impossibility through the matched-external and fresh-preparation objections to withdrawal of internal specificity and retention of the quantifier distinction.
alternative_segmentations: none

claim_identity: C-E04-INT — the two-bit destructive example exhibits an impossibility caused by internality itself
claim_before: Pairwise separation (∀θ≠θ′ ∃e) may fail to combine into one global adaptive separator (∃σ ∀θ≠θ′), and the two-bit destructive example is proposed as an internal-observer impossibility.
target_and_scope: Fixed candidate class Ω, single-copy sequential experiments, and an intended claim that the obstruction is specific to being inside the system.
obligation_type: formal theorem; interpretation or reduction

assumptions: One copy; A reads a and destroys b; B reads b and destroys a; fixed memory/reset/resource interface. These are example conditions, not consequences of internality.
proof_or_evidence_resources: Two-bit construction; matched external observer comparison; adaptive distinguishing sequence, active diagnosis, and sequential experimental-design prior art.
evaluation_or_decision_rules: An internality-specific counterexample must separate internal from external observers under a justified interface comparison; an obstacle reproduced by the same operational constraints externally does not establish internal specificity.

failure_witness: The same example holds for an external observer given the same single copy, destructive operations, memory, and lack of reset. With finitely many fresh preparations at the same θ, the example disappears.
available_branches: BR-E04-1 — allow finite fresh preparation externally, which removes this counterexample; BR-E04-2 — investigate source-specified sequential composition, record preservation, common refinement, uniformity, and error control per model. No universal necessary-and-sufficient package is adopted.
adopted_side_claims: C-E04-S1 — pairwise and global-adaptive separation differ in quantifier order; C-E04-S2 — the bridge must be checked through model-specific sequential/resource conditions rather than the label “internality.”

move_taken: M14 (separate pairwise from global/uniform separation and separate internality from operational constraints); M15 (place adaptive separation in existing diagnosis/sequential-design vocabulary); M17 (withdraw the internality-specific use of the example).
claim_after:
  A1: C-E04-INT — the two-bit example is not retained as evidence of an impossibility caused by internality itself.
  A2: C-E04-S1 — the quantifier-order distinction is retained.
  A3: C-E04-S2 — bridge conditions are model-specific and remain to be investigated.
terminal_status:
  A1: withdrawn
  A2: established adopted side claim
  A3: synthesis/open as to necessary and sufficient conditions

provenance_label:
  claim_before: SOURCE-DERIVED
  episode_boundary: SOURCE-DERIVED
  dependencies: SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED
  available_branches: SOURCE-DERIVED
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED for M14/M17; INFERENCE for M15
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: The obstruction is supplied by the single-copy destructive interface, not by internal location; the proposed target condition leaks away under matched controls.
source_excerpts_used: E04 Excerpts 1–4
uncertainties: Which bridge condition is necessary or sufficient is explicitly setting-dependent and unresolved.
```

### E05-a

```text
parent_corpus_item: E05
subepisode_id: E05-a

episode_boundary: The correction that separates a definitional equality of complete behavioral interfaces from an existence claim about reducing a real internal observer to an external controller, ending in withdrawal of the unqualified v0.1 equivalence.
alternative_segmentations: AMBIGUOUS — E05-a/b/c can instead be one revision block with withdrawal plus two conditional after-claims

claim_identity: C-E05-GEN — general internal/external identification-capacity equivalence from an informally “same” interface
claim_before: Giving internal and external controllers the same inputs, outputs, memory, copies, reset, adversarial conditions, and causal interface establishes equality of generable history sets in general.
target_and_scope: General internal and external observers/controllers; required conclusion is equality of identification/history capacity.
obligation_type: formal theorem; interpretation or reduction

assumptions: Informally identical input/output/resource/causal interface; the full realizability details and implementation map are not fixed.
proof_or_evidence_resources: Audit of omitted interface dimensions and separation of stipulative transcript equality from a physical implementation correspondence.
evaluation_or_decision_rules: A definitional equality of allowed protocol/transcript relations must not be used as proof that a corresponding external implementation exists for a real internal observer.

failure_witness: “Same interface” was underspecified, and the argument conflated a convention assigning identical history capacity with an existence theorem for a state-preserving reduction.
available_branches: none within this correction block; the two actually adopted replacement branches are coded in E05-b and E05-c, not treated as merely available.
adopted_side_claims: C-E05-DIST — conventional equivalence and conditional implementation correspondence are different obligations.

move_taken: M14 (disambiguate stipulation from existence/reduction); M17 (withdraw the general v0.1 claim).
claim_after:
  A1: C-E05-GEN — the general informal interface-equivalence claim is no longer asserted.
  A2: C-E05-DIST — two distinct replacement obligations must be considered.
terminal_status:
  A1: withdrawn
  A2: established adopted side claim

provenance_label:
  claim_before: SOURCE-DERIVED
  episode_boundary: SOURCE-DERIVED; boundary relative to E05-b/c is AMBIGUOUS
  dependencies: SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED
  available_branches: INFERENCE from the chosen three-part segmentation
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: The claimed equivalence becomes definitional if equality of history capability is included inside “same interface”; that does not discharge the implementation-existence target.
source_excerpts_used: E05 Excerpts 1, 2, and 4
uncertainties: The source does not impose a unique analytic boundary between this correction and the two replacements.
```

### E05-b

```text
parent_corpus_item: E05
subepisode_id: E05-b

episode_boundary: The conventional-equivalence replacement: fully specify realizable interface I and define the allowed protocol/transcript relations identically, then state equality of history sets as the consequence.
alternative_segmentations: AMBIGUOUS — may be an after-claim inside a single E05 revision episode

claim_identity: C-E05-CONV — conventional equality of history sets under definitionally identical complete behavioral interfaces
claim_before: The overbroad equivalence claim lacks a complete specification of what “same interface” means.
target_and_scope: Two controllers under a complete feasible interface covering timing, concurrency, memory properties, costs, embodiment, self-readout, stochastic and causal channels, reset/copy/fresh preparation, and adversarial access.
obligation_type: interpretation or reduction; design decision

assumptions: The complete interface is specified and the relation of allowed protocols to transcripts is defined to be identical for the two controllers.
proof_or_evidence_resources: The full interface specification and the defining equality itself.
evaluation_or_decision_rules: Treat the result as a conventional consequence of the behavioral-interface definition, not as a physically substantive implementation theorem.

failure_witness: The prior informal interface omitted relevant dimensions and did not distinguish convention from existence. No witness defeats the newly stated definitional conditional.
available_branches: The physical/model correspondence route is taken separately in E05-c.
adopted_side_claims: none; C-E05-CONV is a replacement claim distinct from C-E05-GEN.

move_taken: M1 (strengthen the interface conditions to a complete explicit specification); M2 (weaken a general physical-sounding equivalence to a conventional conditional); M14 (type the result as definitional rather than implementational).
claim_after:
  A1: C-E05-CONV — if the complete allowed protocol/transcript relations are identical by definition, the history sets coincide.
terminal_status:
  A1: established conventional conditional; not an existence theorem

provenance_label:
  claim_before: SOURCE-DERIVED as shared pre-correction context
  episode_boundary: SOURCE-DERIVED; segmentation boundary AMBIGUOUS
  dependencies: SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED
  available_branches: SOURCE-DERIVED
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED for M14; INFERENCE for M1/M2 as the before/after relation
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: Equality is intentionally placed in the complete interface definition; the source flags the resulting theorem as conventional rather than using it to claim physical equivalence.
source_excerpts_used: E05 Excerpts 2–3
uncertainties: Whether a definitional reformulation should receive any M-code at all is boundary-sensitive; M1/M2 describe the transition from C-E05-GEN, not a proof step inside the conditional.
```

### E05-c

```text
parent_corpus_item: E05
subepisode_id: E05-c

episode_boundary: The conditional implementation-correspondence replacement inside a specified discrete-time turn-based controlled transition system.
alternative_segmentations: AMBIGUOUS — may be an after-claim inside a single E05 revision episode or combined with E05-b as one replacement package

claim_identity: C-E05-MAP — policy/transcript correspondence under a state map preserving the declared controlled-transition structure
claim_before: The unqualified general claim does not establish that a real internal observer has an external implementation with the same history capability.
target_and_scope: Discrete-time, turn-based controlled transition systems with declared controller-state updates, memory access, explicit cost transitions, and an internal/external state map preserving actions, transitions, and observations.
obligation_type: formal theorem; interpretation or reduction

assumptions: Declared transition-only controller updates; guaranteed access to declared memory; delays and embodiment cost encoded in state transitions; a commuting state map preserving allowable actions, transitions, and observations.
proof_or_evidence_resources: The preserving state map and induction on transcript/history length.
evaluation_or_decision_rules: The correspondence succeeds only if policies can be transported while preserving transcript distributions; the lemma does not count as evidence that the required state map exists for actual observers.

failure_witness: For the original general claim, existence of the preserving state map was not established. No witness defeats the stated conditional lemma.
available_branches: Demonstrate such a map for an actual observer; explicitly left unguaranteed and therefore open rather than adopted.
adopted_side_claims: none; C-E05-MAP is a distinct conditional replacement.

move_taken: M1 (add explicit system and map hypotheses); M7 (revise the target to a specified controlled-transition model class); M8 (add the history-length induction route); M10 (use an explicit state-map translation preserving action/transition/observation structure).
claim_after:
  A1: C-E05-MAP — within the specified model, a preserving state map permits policy transfer with the same transcript distribution.
terminal_status:
  A1: established conditional lemma; existence for real observers remains open

provenance_label:
  claim_before: SOURCE-DERIVED as shared pre-correction context
  episode_boundary: SOURCE-DERIVED; segmentation boundary AMBIGUOUS
  dependencies: SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED
  available_branches: SOURCE-DERIVED; its prospective status is OPEN HYPOTHESIS
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED for M1/M7/M8; INFERENCE for M10 as classification of the explicit state map
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: No leakage in the conditional lemma if map existence is kept as a hypothesis; leakage would recur only if that existence were smuggled into an informal “same interface.”
source_excerpts_used: E05 Excerpts 1–4
uncertainties: M10 is not unique: the state map is translation-like, but the codebook does not explicitly name controller-implementation simulations. This is recorded rather than resolved with a new code.
```

### E06-a

```text
parent_corpus_item: E06
subepisode_id: E06-a

episode_boundary: The whole-case judgment changes from a working positive DR-1/weak-relocation case to a frozen negative result that does not support the hypothesized iterative Deferred Resolution chain.
alternative_segmentations: AMBIGUOUS — this can be combined with E06-b as one case-level reversal, or E06-b can be split further

claim_identity: C-E06-CASE — GST supports the Deferred Resolution case at the whole-series level
claim_before: The best whole-case classification is DR-1 weak relocation, while quotient and historical/narrative nulls limit stronger readings.
target_and_scope: The entire GST series; comparative/historical conclusion that it is a working positive case for the hypothesized Deferred Resolution pattern.
obligation_type: empirical claim; comparative claim

assumptions: Field-native documentary reconstruction of the GST series; no generalization to science as a whole.
proof_or_evidence_resources: The case reconstruction and the Null C and Null D/E checks named in the source packet.
evaluation_or_decision_rules: A quotient solution and unsupported historical sequencing/reviewer-imposed narrative constrain or defeat the series-level positive mechanism reading; the final result is frozen when those nulls prevail.

failure_witness: Null C (solved by quotient) and Null D/E (historical sequencing/reviewer-imposed narrative) limit the prior positive interpretation; the v0.2 conclusion states that the hypothesized iterative chain was not supported.
available_branches: Retain only a weak-relocation reading was the earlier branch; it is not retained in the frozen v0.2 verdict.
adopted_side_claims: none in this subepisode; the field-native reconstruction is coded in E06-b.

move_taken: M17 (withdraw the positive whole-case judgment and freeze the negative result).
claim_after:
  A1: C-E06-CASE — the GST series does not support the hypothesized iterative Deferred Resolution chain.
terminal_status:
  A1: frozen negative result; prior positive judgment withdrawn

provenance_label:
  claim_before: SOURCE-DERIVED
  episode_boundary: SOURCE-DERIVED; segmentation boundary AMBIGUOUS
  dependencies: SOURCE-DERIVED, though the detailed null tests are not present in the packet
  failure_witness: SOURCE-DERIVED at summary level
  available_branches: SOURCE-DERIVED
  adopted_side_claims: INFERENCE from the chosen split
  move_taken: SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: Null C indicates that at least part of the purported mechanism reading may collapse under quotient reformulation; the packet does not provide enough detail to characterize further leakage.
source_excerpts_used: E06 Excerpts 1–4
uncertainties: The concrete documentary observations instantiating Null C and Null D/E are absent from the frozen excerpts, so their force cannot be independently decomposed.
```

### E06-b

```text
parent_corpus_item: E06
subepisode_id: E06-b

episode_boundary: The associated vocabulary revision: Deferred Resolution loses independent-mechanism status, the five-stage taxonomy is deleted, and the technical content is reconstructed in existing field-native terms.
alternative_segmentations: AMBIGUOUS — split into E06-b1 (mechanism-name demotion) and E06-b2 (taxonomy deletion/prior-art absorption), or combine with E06-a

claim_identity: C-E06-MECH — Deferred Resolution is an independent mechanism with the stated five-stage taxonomy for this case
claim_before: The case was organized as a positive Deferred Resolution mechanism and a five-stage sequence of frequency, recurrence, formal invariance, diagnostic effect, and modal impossibility.
target_and_scope: Mechanism identity and taxonomy applied to the GST case.
obligation_type: interpretation or reduction; literature/novelty claim

assumptions: The case must require the proposed mechanism/taxonomy beyond field-native reconstruction.
proof_or_evidence_resources: Re-description using conditional inverse problems, reference/nuisance uncertainty, joint estimation, gauge identifiability, quotient parameterization, model checking, and model-specific extension.
evaluation_or_decision_rules: Do not preserve an independent mechanism or taxonomy when the technical content is more accurately reconstructed in existing field-native language and the historical working hypothesis has failed.

failure_witness: The frozen negative case verdict plus adequacy of existing field-native vocabulary; exact item-by-item prior-art matches are not shown in the excerpt.
available_branches: none stated beyond the discarded mechanism/taxonomy reading.
adopted_side_claims: C-E06-FN — the technical content is more accurately reconstructible in the listed field-native terms, without a new-mechanism claim.

move_taken: M15 (absorb the technical reconstruction into existing field-native vocabulary); M17 (demote Deferred Resolution to a rejected historical working hypothesis and delete the five-stage taxonomy).
claim_after:
  A1: C-E06-MECH — Deferred Resolution is no longer an independent mechanism claim for this case.
  A2: C-E06-TAX — the five-stage taxonomy is removed.
  A3: C-E06-FN — the technical material is retained as a field-native reconstruction.
terminal_status:
  A1: demoted to rejected historical working hypothesis
  A2: withdrawn/deleted
  A3: retained adopted side claim; no new-mechanism status

provenance_label:
  claim_before: SOURCE-DERIVED
  episode_boundary: SOURCE-DERIVED; segmentation boundary AMBIGUOUS
  dependencies: SOURCE-DERIVED at vocabulary-list level
  failure_witness: SOURCE-DERIVED at case-verdict level; detailed mapping UNKNOWN
  available_branches: SOURCE-DERIVED
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: The independent-mechanism target disappears under a more accurate quotient/model-specific reconstruction, but the excerpt is insufficient to decide whether this is full target leakage or only lack of novelty.
source_excerpts_used: E06 Excerpts 3–5
uncertainties: Whether the mechanism demotion and taxonomy deletion are one transition or two remains unresolved; the fine-grained prior-art correspondence is also UNKNOWN.
```

### E07

```text
parent_corpus_item: E07
subepisode_id: E07

episode_boundary: From preregistered H1 through the frozen comparison findings and no-change answer to the final source-local M1 classification.
alternative_segmentations: none

claim_identity: C-E07-H1 — a generic transfer audit adds diagnostic value over the field-native control
claim_before: A generic audit finds at least one loss/distortion path that the field-native control does not find as clearly or as early, provided a preregistered success condition survives all applicable falsification conditions.
target_and_scope: Frozen metrology document/control corpus; empirical comparison of generic versus field-native audit performance.
obligation_type: empirical claim; comparative claim

assumptions: Frozen corpus and field-native control; H1 is judged only under the preregistered §5 falsification and §6 success conditions.
proof_or_evidence_resources: Generic audit, field-native control comparison, compact cross-chain display, and the enumerated audit outputs/judgments.
evaluation_or_decision_rules: At least one preregistered success condition must survive every applicable falsification condition; source-local final labels allow organizational value without diagnostic or methodological added value.

failure_witness: No new missing assumption, uncertainty component, scope judgment, conformity decision, traceability break, absent source, or remedy was found; the audit changed presentation/visibility only and changed no judgment.
available_branches: Source-local M0 is a defensible stricter label; M2 and M3 are explicit rejected classifications. These are classification branches, not formation M-codes.
adopted_side_claims: C-E07-ORG — the audit has compact organizational/cross-chain visibility value only.

move_taken: M17 (H1 diagnostic/methodological added-value claim is not supported and the negative limitation is fixed). No formation M1 is coded: the source-local label “M1 — Organizational value” is not codebook M1.
claim_after:
  A1: C-E07-H1 — no diagnostic or methodological added value was demonstrated.
  A2: C-E07-ORG — organizational/presentation value is retained.
terminal_status:
  A1: unsupported/negative empirical result
  A2: adopted as source-local “M1 — Organizational value”; not success of C-E07-H1

provenance_label:
  claim_before: SOURCE-DERIVED
  episode_boundary: SOURCE-DERIVED
  dependencies: SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED
  available_branches: SOURCE-DERIVED
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED; M17 is the formation-code classification of the negative disposition
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: No target leakage identified; the preregistered comparison directly tests the diagnostic-added-value target and yields a negative result.
source_excerpts_used: E07 Excerpts 1–4
uncertainties: The packet omits the full §5–§6 criteria, so independent checking of whether every applicable condition was applied is unavailable.
```

### E08

```text
parent_corpus_item: E08
subepisode_id: E08

episode_boundary: From the v0.1 “partial preservation” verdict and forgetting-prevention sentence through the N-04 contradiction finding to the v0.2 documentary-continuity-only verdict.
alternative_segmentations: none

claim_identity: C-E08-PRES — the documentary history establishes at least partial preservation effectiveness, including prevention of forgetting
claim_before: “Partial preservation history” was identified, and the preservation mechanism was said to have prevented forgetting despite not guaranteeing resolution or complete downstream transmission.
target_and_scope: The cited hydrology document chain; conclusion about causal/effective preservation, use, transmission, or forgetting prevention.
obligation_type: empirical claim; interpretation or reduction

assumptions: Documentary occurrences and one 17C→17B reference are used to assess preservation through the chain.
proof_or_evidence_resources: N-04, L-01, L-02, L-03; comparison of v0.1 and v0.2 verdict language; audit of what was and was not measured.
evaluation_or_decision_rules: Do not infer preservation effectiveness, actual use, downstream transmission, or forgetting prevention without measurements supporting those outcomes; documentary rediscoverability alone supports only continuity.

failure_witness: N-04 says effectiveness is unconfirmed, contradicting “prevented forgetting”; actual reference/use/transmission/forgetting-prevention effects were not measured. Silent disappearance and loss of uncertainty/nonstationarity language further block the stronger reading.
available_branches: Collect evidence measuring actual reference, use, downstream transmission, or forgetting-prevention effectiveness; this remains prospective and unperformed.
adopted_side_claims: C-E08-DOC — documentary continuity/rediscoverability was identified.

move_taken: M2 (weaken the conclusion from effective preservation to documentary continuity); M14 (separate documentary continuity/rediscoverability from causal effectiveness and downstream use); M17 (withdraw the forgetting-prevention expression and leave effectiveness untested).
claim_after:
  A1: C-E08-PRES — preservation effectiveness is untested; no forgetting-prevention conclusion is asserted.
  A2: C-E08-DOC — documentary continuity and rediscoverability are identified.
terminal_status:
  A1: withdrawn as an effectiveness claim; untested
  A2: retained adopted side claim; not evidence that C-E08-PRES succeeded

provenance_label:
  claim_before: SOURCE-DERIVED
  episode_boundary: SOURCE-DERIVED
  dependencies: SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED
  available_branches: OPEN HYPOTHESIS inferred from the list of unmeasured outcomes
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: The v0.1 language crossed from document persistence into unmeasured effectiveness; v0.2 removes that target leakage.
source_excerpts_used: E08 Excerpts 1–5
uncertainties: The excerpt does not define an operational threshold for “documentary continuity”; only the upper bound on interpretation is clear.
```

### E09-a

```text
parent_corpus_item: E09
subepisode_id: E09-a

episode_boundary: The P0 decision after screening 14 codes: reject the planned full three-field P1–P5 artifact-chain reconstruction and adopt a NONEVAL-only reduced continuation.
alternative_segmentations: none; the later post-test termination is E09-b

claim_identity: C-E09-DESIGN — the planned full P1–P5 three-field comparative methodology remains justified after P0
claim_before: The design called for full artifact-chain reconstruction in three fields.
target_and_scope: Fourteen initial codes and a three-field comparative artifact-chain study; this is a continuation/design obligation.
obligation_type: design decision; comparative claim

assumptions: Full continuation presupposes enough viable comparative codes to justify the large reconstruction.
proof_or_evidence_resources: P0 code screening: effectively one surviving code (NONEVAL) and one held code (RET-DOWN); cost/scope comparison of four continuation branches.
evaluation_or_decision_rules: Continue the full design only if enough comparative codes survive to justify it; executing a plan contrary to its own evidential premise is rejected. The source recommends the smallest search-only branch.

failure_witness: Of 14 codes, only NONEVAL survives substantively and RET-DOWN is held; the premise that there are enough codes for the full design is denied.
available_branches: (ii) test RET-DOWN, next-best; (iii) follow P1–P5 as designed, explicitly rejected; (iv) terminate immediately and downgrade to comparative review, allowed but not selected at P0.
adopted_side_claims: none; the adopted reduced design is the after-decision, not evidence that the original full design succeeded.

move_taken: M4 (restrict the candidate/code and artifact-search target to NONEVAL); M17 (abandon the full three-field P1–P5 branch at this decision point).
claim_after:
  A1: C-E09-RED — perform only the reduced NONEVAL search in GUM/VIM and the GRADE handbook.
  A2: C-E09-DESIGN — do not proceed with the full three-field plan as designed.
terminal_status:
  A1: adopted reduced continuation
  A2: rejected/abandoned

provenance_label:
  claim_before: SOURCE-DERIVED
  episode_boundary: SOURCE-DERIVED
  dependencies: SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED
  available_branches: SOURCE-DERIVED
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: No leakage identified; this is an explicit resource/scope decision governed by the design’s own premise.
source_excerpts_used: E09 Excerpts 1–3
uncertainties: The source packet does not reproduce the original design’s exact minimum viable number of codes; the premise failure is stated rather than recalculated.
```

### E09-b

```text
parent_corpus_item: E09
subepisode_id: E09-b

episode_boundary: From the adopted P1-reduced check through the second premise failure to termination as comparative methodology and downgrade to comparative review.
alternative_segmentations: none; it follows but is analytically distinct from the P0 choice in E09-a

claim_identity: C-E09-METH — the reduced check may leave a viable comparative methodology worth continuing
claim_before: After P0, the project continues only with the P1-reduced NONEVAL two-field check rather than the full P1–P5 design.
target_and_scope: P1-reduced two-field check and the viability of the larger work as comparative methodology.
obligation_type: design decision; comparative claim

assumptions: The reduced check is evaluated under the design document’s termination/downgrade rule.
proof_or_evidence_resources: P0 results and the P1-reduced check.
evaluation_or_decision_rules: Apply the design document Part IX termination rule when the comparative plan’s premise has been denied through both screening stages.

failure_witness: P0 and the reduced check deny the plan’s premise in two successive stages. The packet does not reproduce the lower-level P1-reduced observations.
available_branches: Proceeding to full P1–P5 remains explicit but is rejected.
adopted_side_claims: C-E09-REV — the material may continue only as a downgraded comparative review.

move_taken: M17 (terminate as comparative methodology and abandon P1–P5).
claim_after:
  A1: C-E09-METH — no further comparative-methodology continuation.
  A2: C-E09-REV — downgrade the remaining work to comparative review.
terminal_status:
  A1: terminated
  A2: adopted side claim/design status; not success of C-E09-METH

provenance_label:
  claim_before: SOURCE-DERIVED
  episode_boundary: SOURCE-DERIVED
  dependencies: SOURCE-DERIVED at decision-summary level
  failure_witness: SOURCE-DERIVED at summary level; underlying observations UNKNOWN
  available_branches: SOURCE-DERIVED
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: No target leakage identifiable from the excerpt.
source_excerpts_used: E09 Excerpts 4–6, with Excerpts 1–3 as prior-stage context
uncertainties: The source-only packet is insufficient to reconstruct why NONEVAL failed beyond the stated two-stage premise denial.
```

### E10

```text
parent_corpus_item: E10
subepisode_id: E10

episode_boundary: The stress test of “closure reversal” against Gödel I/II and an existing 21-theorem comparison, ending with C1-only status and a fixed negative novelty/diagnostic result.
alternative_segmentations: none

claim_identity: C-E10-CR — “closure reversal” supplies an independent proof-theoretic classification or a mechanism-discovery/discrimination tool for Gödel incompleteness
claim_before: INFERENCE: the stress test leaves open whether the metadescriptive “closure reversal” vocabulary does more than summarize the already known Gödel mechanism and could merit C2/C3.
target_and_scope: Gödel’s first and second incompleteness theorems and comparison with 21 existing theorem cases; target is explanatory/classificatory novelty and diagnostic resolution.
obligation_type: comparative claim; literature/novelty claim; interpretation or reduction

assumptions: T is a computably axiomatized classical first-order theory containing Q; the stated consistency premise applies to the incompleteness result. “Closure reversal” is explicitly nonstandard metadescription.
proof_or_evidence_resources: Gödel I statement, the Gödel II truth/provability and meta/object-level characterization, and comparison with the existing 21 theorem analyses.
evaluation_or_decision_rules: C2/C3 would require an independently useful classification or diagnostic mechanism beyond standard concepts; a label useful only after standard analysis receives C1.

failure_witness: The vocabulary does not discover or distinguish the Gödel mechanism, has lower diagnostic resolution than standard concepts, and works only as a post-analysis comparative summary.
available_branches: C2 and C3 are explicit classifications considered and rejected.
adopted_side_claims: none as a distinct claim identity; the limited comparative-summary use is the weakened continuation of C-E10-CR.

move_taken: M2 (weaken from independent classification/diagnostic use to explanatory metaphor only); M15 (return the mechanism analysis to standard proof-theoretic concepts); M17 (demote/fix the negative result against C2/C3).
claim_after:
  A1: C-E10-CR — “closure reversal” is useful only as a short explanatory/comparative label after standard analysis, not as an independent classification or discovery tool.
terminal_status:
  A1: C1; limited retention with C2/C3 rejected and negative result fixed

provenance_label:
  claim_before: INFERENCE from the stress-test target and explicit C2/C3 rejection
  episode_boundary: SOURCE-DERIVED
  dependencies: SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED
  available_branches: SOURCE-DERIVED
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED for M2/M17; INFERENCE for M15
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: No theorem-level leakage is identified; the negative result is that the added vocabulary contributes only retrospective compression, not mechanism identification.
source_excerpts_used: E10 Excerpts 1–5
uncertainties: The precise C2/C3 criteria and the 21 comparison cases are not included, so only the stated final decision rule can be reconstructed.
```

### E11-a

```text
parent_corpus_item: E11
subepisode_id: E11-a

episode_boundary: The kill test of the broad S2 “self-assurance” label, ending in the S2* judgment that retains it only for local reflection and rejects its extension across uniform/global reflection and semantic soundness.
alternative_segmentations: AMBIGUOUS — E11-a and E11-b may be one integrated episode, with the technical type/subject-shift reconstruction serving only as evidence for S2*

claim_identity: C-E11-S2 — “self-assurance” works as an S2-level comparative label across reflection notions
claim_before: S2 is the candidate status for the “self-assurance” comparison, including a possible broad use beyond single local reflection.
target_and_scope: Local, uniform, and global reflection plus semantic soundness; target is a comparative label that does not conceal differences of type, language, or metalevel.
obligation_type: comparative claim; interpretation or reduction

assumptions: Reflection form, formula class Γ, base theory, truth axioms, and metalevel may vary across the target range.
proof_or_evidence_resources: The Γ-scoped reflection schemas, stronger-theory constructions, conservation/consistency-strength distinctions, and the Löb/subject-shift analysis detailed in E11-b.
evaluation_or_decision_rules: Actively kill-test rather than preserve S2; broad retention fails if the label hides type, language, or metalevel differences. Local comparative usefulness alone supports only S2*.

failure_witness: Uniform/global reflection and semantic soundness are not one type of result; strength and conservation depend on scope, Γ, base, and truth axioms, while subject shifts differ.
available_branches: Retain unqualified S2 is explicitly considered and not taken.
adopted_side_claims: none; S2* is a qualified continuation of the same comparative-label claim.

move_taken: M2 (weaken the label’s range and conclusion to local-reflection validity only); M14 (separate local from uniform/global reflection and semantic soundness, including their type/language/metalevel differences).
claim_after:
  A1: C-E11-S2 — “self-assurance” has limited S2* use for local reflection but breaks down when generalized to uniform/global reflection or soundness.
terminal_status:
  A1: S2*; conditionally retained and demoted from broad S2

provenance_label:
  claim_before: SOURCE-DERIVED, though the full prior S2 definition is absent
  episode_boundary: SOURCE-DERIVED; segmentation boundary AMBIGUOUS
  dependencies: SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED
  available_branches: SOURCE-DERIVED
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: The broad label collapses distinct reflection/soundness types; the source treats that loss of resolution as the reason for restricting it.
source_excerpts_used: E11 Excerpts 1–5
uncertainties: Without the source-local definitions of S2 and S2*, the exact amount of demotion cannot be reconstructed beyond the explicit local-versus-broad contrast.
```

### E11-b

```text
parent_corpus_item: E11
subepisode_id: E11-b

episode_boundary: The technical correction from an untyped “same theory assures itself” reading to Γ-scoped reflection principles added externally to form a stronger theory, with explicit subject shift and scope-dependent consequences.
alternative_segmentations: AMBIGUOUS — may be dependencies inside E11-a rather than a separate analytic transition

claim_identity: C-E11-REFL — technical interpretation of “self-assurance” across reflection principles
claim_before: INFERENCE: an unqualified self-assurance reading risks treating Γ as a property of T, treating local/uniform/global forms alike, or reading reflection as the same T proving its own reflection/soundness.
target_and_scope: Theories T and T+=T+Rfn_Γ(T), T+RFN_Γ(T), or T+GRP(T); formula-class scope, object theory versus externally formed stronger theory, and the consequences bridged by new axioms.
obligation_type: interpretation or reduction; formal theorem context

assumptions: A chosen base T; selected local/uniform/global reflection schema and Γ; any truth axioms required for the target formulation. These are conditions of each resulting theory claim, not proof tools.
proof_or_evidence_resources: Reflection schemas, externally constructed theory extension, and Löb’s theorem as a discriminator between same-T collapse and permitted external extension.
evaluation_or_decision_rules: Track the theory that proves the statement, the language/formula scope, and the metalevel subject. Do not infer one conclusion P across forms whose strength/conservation/consistency strength depends on those parameters.

failure_witness: Löb constrains the same T making its own reflection a theorem but does not prohibit adding reflection externally; treating the two as one “self-assurance” relation misstates the progression.
available_branches: Local, uniform, and global reflection extensions are explicit alternatives whose consequences depend on scope; no single one is selected as universally representative.
adopted_side_claims: C-E11-R1 — Γ specifies the scope of added reflection instances rather than a property of T; C-E11-R2 — external reflection forms a stronger theory and requires a subject/metalevel shift.

move_taken: M6 (extend T by a reflection principle to T+); M12 (evaluate/bridge T from an external level and keep the subject shift explicit); M14 (correct same-T versus stronger-theory and local/uniform/global/soundness types); AMBIGUOUS M3 (Γ is made an explicit formula-class scope, but the excerpt parameterizes Γ rather than choosing one particular fragment).
claim_after:
  A1: C-E11-R1 — Γ is a scope definition for reflection instances.
  A2: C-E11-R2 — reflection principles are added externally to form a stronger theory, and results vary with scope, Γ, base, and truth axioms.
terminal_status:
  A1: established adopted technical claim
  A2: established adopted technical claim; no guarantee of one uniform conclusion P

provenance_label:
  claim_before: INFERENCE from the explicitly identified misreading risk
  episode_boundary: INFERENCE; segmentation boundary AMBIGUOUS
  dependencies: SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED
  available_branches: SOURCE-DERIVED
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED for M6/M12/M14; AMBIGUOUS for M3
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: Calling all variants “self-assurance” leaks the target across different theories, languages, and levels; the technical reconstruction restores those indices.
source_excerpts_used: E11 Excerpts 1–4
uncertainties: M3 versus M14 is not uniquely determined for Γ: explicit formula-class scoping fits M3, while the actual correction may only be the M14 distinction among already parameterized schemas.
```

### E12-a

```text
parent_corpus_item: E12
subepisode_id: E12-a

episode_boundary: The stress test of proof-theoretic ordinal as a universal scalar of total theory strength, ending with fixed-package calibration, equal-coordinate limits, and the S2* judgment.
alternative_segmentations: none; the separate A2 architecture judgment is E12-b

claim_identity: C-E12-SCALAR — |T|=α is a universal one-dimensional scalar for all strength of arbitrary theories
claim_before: A proof-theoretic ordinal might be read as a standalone, universal scalar of theory strength, with equal ordinals implying broader equivalences between theories.
target_and_scope: Arbitrary theories, formula classes, and interpretability/conservation notions; possible conclusions include theorem-set, interpretability, consistency-strength, Π1-consequence, induction-schema, and reflection-rank equality.
obligation_type: comparative claim; interpretation or reduction

assumptions: For the retained claim, a natural family of theories and a fixed analysis package are required, including notation, base/metatheory, formula class, and reduction notion.
proof_or_evidence_resources: Bridge theorems connecting cut elimination, transfinite induction/well-ordering, reflection, and worm orderings; countercomparison of what equal calibrated ordinals do not imply.
evaluation_or_decision_rules: A universal scalar must support the advertised cross-notion inferences without omitted package parameters; absent bridge theorems, equal ordinals establish only equal coordinates under the selected calibration. One characterization may merit S1, while convergence under a natural fixed package supports only limited S2/S2*.

failure_witness: |T|=|U| does not by itself imply equality of theorem sets, mutual interpretability, consistency strength, Π1 consequences, induction schemas, or reflection rank. The shorthand omits notation, base/metatheory, formula class, and reduction notion.
available_branches: The universal-scalar reading is rejected. Single-characterization S1 and PA-like fixed-package convergence are explicit restricted branches; the latter is adopted as the limited calibration claim.
adopted_side_claims: C-E12-CAL — ordinal is a robust one-dimensional coordinate for natural theory families under a standard fixed analysis package; C-E12-EQ — equal ordinals initially mean only equal coordinates under the chosen calibration, absent further bridge theorems.

move_taken: M1 (require a fixed analysis package and bridge conditions); M2 (weaken total/universal strength to a limited coordinate); M3 (fix the formula/language consequence class); M4 (restrict arbitrary theories to a natural theory family); M13 (reformulate the comparison as ordinal calibration rather than total-strength equality); M14 (separate equal calibrated coordinate from theorem, interpretability, consistency, consequence, induction, and reflection equalities).
claim_after:
  A1: C-E12-SCALAR — no universal scalar of all theory strength is established.
  A2: C-E12-CAL — ordinal calibration can be strong and robust for natural theory families under a fixed standard package.
  A3: C-E12-EQ — equal calibrated ordinals alone establish only equal position in that calibration.
terminal_status:
  A1: withdrawn/rejected universal reading
  A2: S2* conditional adopted side claim; not success of C-E12-SCALAR
  A3: established interpretive limit

provenance_label:
  claim_before: SOURCE-DERIVED as the explicitly rejected universal reading
  episode_boundary: SOURCE-DERIVED
  dependencies: SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED
  available_branches: SOURCE-DERIVED
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED for M2/M4/M13/M14; INFERENCE for M1/M3 as classification of the fixed-package conditions
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: The scalar reading leaks across changes in notation, base/metatheory, formula class, and reduction notion. Fixing the calibration package prevents equal coordinates from being mistaken for total theory equivalence.
source_excerpts_used: E12 Excerpts 1–3
uncertainties: No particular formula class or reduction notion is selected in the excerpt, so M3 records the requirement to fix that dimension rather than a uniquely named fragment.
```

### E12-b

```text
parent_corpus_item: E12
subepisode_id: E12-b

episode_boundary: The separate architecture judgment distinguishing the analyzed theory and encoded calculus from the notation/reduction/well-foundedness metatheory, ending with source-local A2 rather than A3.
alternative_segmentations: none

claim_identity: C-E12-ARCH — the evaluated/evaluating-theory distinction is a stable ordinal-analysis architecture feature and may warrant A2/A3
claim_before: INFERENCE: the classification obligation is whether the type/level distinction is stable across ordinal analysis and whether it exceeds the standard metamathematical distinction enough to merit A3.
target_and_scope: Analyzed T, proof-encoding calculus, ordinal notation, reduction theorem, and a metatheory proving notation well-foundedness; comparison with Turing–Feferman subject/extension reindexing.
obligation_type: comparative claim; interpretation or reduction

assumptions: The relevant components occupy the roles stated in an ordinal analysis; no identity with Turing–Feferman reindexing is assumed.
proof_or_evidence_resources: Type comparison among T, calculus, notation, reduction theorem, and well-foundedness-proving metatheory.
evaluation_or_decision_rules: A stable architecture distinction supports A2; A3 is not awarded when standard metamathematical level distinctions already provide an adequate account.

failure_witness: Against A3, the standard evaluated-theory/evaluating-theory distinction is sufficient. Against conflation, the components have different types and are not identical to Turing–Feferman subject/extension reindexing.
available_branches: A3 is explicitly considered and rejected.
adopted_side_claims: none; the architecture claim itself receives A2.

move_taken: M12 (place well-foundedness justification and evaluation in the metatheory); M14 (separate analyzed theory, calculus, notation, reduction theorem, and evaluating metatheory, and distinguish this from progression reindexing).
claim_after:
  A1: C-E12-ARCH — the evaluated/evaluating-theory distinction is a stable architecture feature adequately captured by standard metamathematical level distinctions.
terminal_status:
  A1: A2; A3 rejected

provenance_label:
  claim_before: INFERENCE from the stated A2/A3 decision
  episode_boundary: SOURCE-DERIVED
  dependencies: SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED
  available_branches: SOURCE-DERIVED
  adopted_side_claims: SOURCE-DERIVED
  move_taken: SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: The correction prevents type leakage between the object of ordinal analysis and the metatheory that justifies the notation; no further degeneracy is stated.
source_excerpts_used: E12 Excerpt 4, with Excerpts 1–3 as context
uncertainties: The packet does not define A2/A3 globally, so the classification can be reported but not independently recalibrated.
```

## Independent reader record

### 1. 最もcodingしやすかったepisode

E08。v0.1の効果主張（忘却防止を含む）と、未測定であるというfailure witness、v0.2のdocumentary continuityへの限定が同じpacket内で明示されていた。M2、M14、M17と、元claimとは別のadopted side claimを比較的明確に分離できた。

### 2. 最も曖昧だったepisode

E05。一般主張の撤回、規約としての履歴集合一致、状態写像を仮定した条件付き実装対応が、一つの訂正の三つのafter-claimとも、三つのsubepisodeとも読める。また、状態写像による実装対応をM10とするか、M7/M8だけで表すかが一意でない。

### 3. 複数segmentationが残ったepisode

E05、E06、E11。

- E05は一つのrevision episode、三分割、または「撤回＋二つのreplacement」という二分割がsource-compatible。
- E06はcase-level negative verdictとmechanism/taxonomy処理を統合でき、後者をさらに二分することもできる。
- E11はS2* decisionと、その根拠であるformal theory/metalevel correctionを一つにも二つにもできる。

これらの一次分割はcodingの便宜上採用したもので、alternative側を棄却していない。

### 4. M1–M17で表現しにくかったtransition

- E05-bの「同じprotocol/transcript relationを定義で与えたため履歴集合が一致する」という規約的帰結。これはformation moveよりもclaim typeの訂正であり、M1/M2/M14はいずれも完全には一致しない。
- E05-cのcontroller implementation間のstate-map simulation。M10に近いが、codebookの例はformula/model/theory translationであり、controlled-transition implementationのsimulationを明示しない。
- E06のsource-local case verdictやtaxonomyの廃止はM17で表せる一方、case classificationと語彙処理が同じcodeに集約される。
- E07のpreregistered empirical hypothesisが支持されず、別のorganizational valueだけが残るtransitionは、M17以外にempirical null-result dispositionを細かく表すcodeがない。
- E12-bのA2 architecture classificationは主として型・レベルの判定であり、M12/M14は内容を表すが「classificationをA2に固定する操作」自体とは一致しない。

### 5. assumption / resource / evaluation-ruleの境界問題

- E02-bでは有限性、全初期状態、記録先A、|E|>1をassumptionsとし、有限濃度比較をresourceとした。ただし「全候補を識別する」という要求はtarget scopeでもあり、assumptionとの境界が近い。
- E05-bでは完全interfaceの各項目はconditional claimのassumptionsである一方、protocol/transcript関係を同一とする部分は定義的resourceでもdecision ruleでもありうる。ここではassumptionに置き、結果を物理的存在定理として扱わない規則をevaluation ruleに置いた。
- E05-cでは可換state mapをassumption、履歴長帰納法をresource、transcript distribution保存をsuccess ruleとした。state mapは証明を可能にするresourceとも読める。
- E07ではpreregistered success/falsification conditionsはevaluation ruleであり、監査資料やcontrol corpusはresourcesとした。全条件本文がpacketにないため、個々の役割はそれ以上決められない。
- E11/E12のformula class、base、metatheoryはconditional comparisonのassumptionsだが、特定のreduction theoremやbridge theoremはresourcesとした。どのpackageを固定すべきかという要求はevaluation ruleにも接している。

### 6. available branch / adopted side claimの境界問題

- E04のfresh preparationはcounterexampleを消す明示的available branchだが、採用結果ではない。一方、quantifier-order distinctionは実際にretainedされたadopted side claimである。
- E05では規約的同値と条件付き対応が実際に採用されたため、E05-aで単なるavailable branchesにはせず、別subepisodeのclaimsとした。統合segmentationなら両方が同じblockのadopted side claimsになる。
- E07ではsource-local M0は「defensible」だが最終採用はM1 organizational valueであるため、前者をavailable classification、後者をadopted side claimとした。M2/M3は明示的rejected branchesである。
- E09-aではRET-DOWN検査、full continuation、即時終了がavailable branchesで、NONEVAL reduced searchだけがadopted decisionである。E09-bで後にterminationが採用されても、P0時点の即時終了branchが当時採用済みだったことにはならない。
- E12-aではuniversal scalarは拒否され、fixed-package calibrationだけがadopted side claimである。後者を元のuniversal claimの成功とは扱っていない。

### 7. coder instructionsの残存欠陥

- 規約・定義により成立するafter-claimに対応する明確なmove codeがなく、M1/M2/M14またはNOT APPLICABLEの選択が不安定になる。
- 一つのwithdrawalから複数のconditional replacementが生じる場合、subepisodeごとに共有するclaim_beforeをどこまで反復してよいか、またparent blockを別に置くかが明示されていない。
- M9とM10は形式理論寄りの境界例が中心で、一般のstate-map simulationやimplementation correspondenceへの適用範囲が決めにくい。
- M1、M3、M4は「条件を追加する」「formula classを固定する」「theory/object familyを狭める」が同時に起こると重複しやすい。multiple codesは許されるが、どの粒度で重複を避けるかは未指定。
- source-local classification（M0–M3、C1–C3、S1/S2*、A2/A3）をterminal statusとして転記できる一方、その分類決定自体にformation moveがない場合の`move_taken`記法が十分に指定されていない。
- `degenerate_or_target_leakage`の判定語彙・UNKNOWNの扱いがsubmission block外では定義されておらず、定義への埋め込み、条件の取り違え、比較targetの消失を同じ欄で扱うことになる。

### 8. sourceだけでは決められなかったこと

- E06のNull C/D/Eを支える個別資料と、field-native vocabularyへの項目別対応。
- E07のpreregistered §5–§6全文、および全適用条件が実際に満たされたかの再判定。
- E09-bでNONEVAL reduced checkが具体的に何を発見し、なぜ第二段階のpremise failureになったか。
- E10のC2/C3、E11のS2/S2*、E12のS1/S2*/A2/A3の完全な判定定義。
- E10の「既存21定理」比較の内容。
- E11でΓを特定fragmentへ実際にrestrictしたのか、単にscope parameterとして明示したのか。
- E12で固定すべきnotation、base/metatheory、formula class、reduction notionの具体的package。
- E05、E06、E11の唯一のepisode segmentation。packetは複数の境界を許し、coder instructionsに従ってAMBIGUOUSのまま残した。

# 法則式／生成律式 記述方法論 working note v0.1

> Status:
> - exploratory methodology study
> - not a theorem
> - not a new mathematical framework
> - not yet a revision of VED
> - negative results are primary evidence

## 0. Scope and posture

本ノートは、法則式と生成律式の差を既知として出発しない。まず law-like description、state transition、rewriting、definitional / conservative extension、expressive-power comparison、structure construction という標準概念に分解し、それらで尽くせない残差があるかを調べる。

VED は最終適用先であって、方法論を正当化する正例ではない。本ノート作成時点で既存 VED file は変更していない。

## 1. Repository inspection

### 1.1 Location and naming

Repository root は vortical-enclosure-dynamics であり、主要な研究領域は top level の directories、短い技術記録は docs、監査・working records は notes に分かれている。既存の独立研究枝として dimensionality-working-note、stochastic-quantization、Information-Field-Geometry-Theory などがある。

新枝は user-specified first choice の generative_law_methodology を repository root に置いた。理由は次の通り。

- VED 本体の docs / paper を変更しない additive branch である。
- dimensionality-working-note と同様、独立した working research module として読める。
- file names は repository の notes 系で使われる snake_case、version v0.1、language suffix _ja を踏襲する。
- directory 名の underscore は user-specified traceability を優先した。既存 directory naming は一様ではないため、全体 rename は行わない。

### 1.2 VED entry points inspected

- [top-level README](../README.md)
- [Japanese README](../README_ja.md)
- [core equations](../docs/core_equations.md)
- [overview](../docs/00_overview.md)
- [claims](../docs/claims.md)
- [methodology](../docs/methodology.md)
- [methodological note](../docs/methodological_note.md)
- [generative sequence](../docs/navigation/generative_sequence.md)
- [Vol.1 minimal axiom](../paper/vol1/sections/minimal_axiom.tex)
- [Vol.1 causal logs and time](../paper/vol1/sections/causal_logs_time.tex)
- [Vol.1 flow and vorticity](../paper/vol1/sections/flow_vorticity.tex)
- [Vol.1 closure](../paper/vol1/sections/closure.tex)
- [Vol.1 space](../paper/vol1/sections/space.tex)
- [IFGT Japanese record](../Information-Field-Geometry-Theory/ifgt_ja.md)
- [Dimensionality Working Note II](../dimensionality-working-note/README_II_ja.md)
- [theorem / proof anatomy final record](../notes/theorem_proof_anatomy_experiment/07_audit_and_closure/theorem_proof_anatomy_experiment_final_record_v1.0_ja.md)

### 1.3 Existing equation inventory

This is a location inventory, not a completed VED reconstruction.

| Item | Current expression / description found | Primary location | Implicit structure to audit later |
|---|---|---|---|
| difference \(\delta,\Delta\) | “there is difference”; \(\delta\neq0\Rightarrow\nabla\delta\neq0\); IFGT difference source \(\Delta\) | minimal axiom; IFGT correspondence/unified equation | comparison domain; gradient structure; source semantics |
| closure degree / causal log \(C_{ij}\) | \(C_{ij}=1-e^{-\lambda\rho_iH_{ij}}\) | causal logs/time; core equations | directed weighted network; fixed-point semantics; meaning of “generated” |
| history \(H_{ij}\) | accumulated irreversible influence | causal logs/time | event order, accumulation operation, irreversibility criterion |
| density \(\rho_i\) | \(\rho_i=\sum_jC_{ij}\) | causal logs/time | index set, summability, density interpretation |
| local time \(\tau_i\) | \(d\tau_i/dt=\rho_i\) | causal logs/time; space | external \(t\), differentiability, monotonicity vs physical time claim |
| symmetric / antisymmetric split | \(S_{ij}=(C_{ij}+C_{ji})/2\), \(A_{ij}=(C_{ij}-C_{ji})/2\) | space | transpose / pairing of directed edges |
| flow \(J\) | \(J_{ij}=C_{ij}-C_{ji}\); continuum \(\mathbf J(x)\) | flow/vorticity | discrete-to-continuum map; vector-field structure |
| balance / source | \(\partial_t\rho+\nabla\cdot\mathbf J=\sigma\) | flow/vorticity | background time, divergence, volume form, source interpretation |
| rotation / circulation | \(\omega=\nabla\times\mathbf J\), \(L\sim|\omega|\) | flow/vorticity | dimension, orientation, metric / Hodge structure, continuum limit |
| enclosure / closure \(L\) | loop persistence; \(L<L_{\max}\); barrier \(B(L)\) | minimal axiom; closure | state variable vs phenomenological summary; stability criterion |
| closure distance \(\Delta_k\) | \(\Delta_k=L_{\max}-L_k\) | closure | same symbol \(\Delta\) also used for difference source |
| distance \(d_{ij}\) | \(-\log\tilde S_{ij}\), shortest weighted path | space | connectivity, positive weights, disconnected cases, metric vs pseudometric |
| coarse metric | \(d(x,y)^2\approx g_{\mu\nu}\Delta x^\mu\Delta x^\nu\) | space | coarse-graining map, coordinates, approximation regime |
| information density \(I\) | \(I=f(1-C)\), often linearized to \(1-C\) | IFGT | scalar-field domain, relation to \(C_{ij}\), meaning of \(C\) |
| informational update | \(\partial_\tau I+\nabla\cdot J=\sigma\) | IFGT | generated \(\tau\) used as evolution parameter; differential geometry |
| interaction \(I\) | no unique core symbol matching this reading was located | repository-wide search | clarify whether user means information \(I\), interaction relation, or another branch |

### 1.4 Terminology and notation tensions to preserve

1. Vol.1 and core-equation records call \(C_{ij}\) a causal log. The navigation generative-sequence record calls \(C_{ij}\) closure degree and distinguishes the causal log as an accumulated trace. The relation may be resolvable from source history, but it is not silently normalized here.
2. \(\Delta\) denotes a difference source in IFGT while \(\Delta_k=L_{\max}-L_k\) denotes closure distance elsewhere.
3. \(C_{ij}\) is a matrix-like directed quantity, while IFGT often uses scalar field \(C(x,\tau)\). The discrete-to-field map needs specification.
4. \(I\) was found as information density, not as a uniquely defined interaction variable. “interaction \(I\)” remains a source-identification question.

These are future notation / claim-identity audit items, not present claims that the equations are wrong.

## 2. Initial research question

The broad question is:

> What distinguishes a law-like relation internal to a fixed specification from a claim that the available specification, distinctions, or structures have changed?

The first pass produces no single syntactic discriminator. Instead it requires:

1. source specification;
2. target specification;
3. explicit map, relation, or construction;
4. identity / equivalence criterion;
5. the exact item claimed to be new;
6. the logical form and evidence burden of that claim.

## 3. Phase 0 result: law equation

The detailed audit is in [law equation specification](./law_equation_specification_v0.1_ja.md).

### Result

The working statement survives only in broad form:

> Given a fixed mathematical specification, a law-like description specifies or constrains admissible states, histories, transitions, distributions, stationary paths, balances, or responses.

It is broader than an endomorphism \(L_\Sigma:X\to X\). Constraint equations, transition relations, Markov kernels, variational principles, and constitutive relations are valid controls against a map-only definition.

### Negative result

Syntax does not determine role. The same differential equation can be fundamental, effective, constitutive, phenomenological, numerical, or definitional depending on its declared scope and background.

## 4. Phase 1 result: generative equation candidate

The detailed audit is in [generative equation specification](./generative_equation_specification_v0.1_ja.md).

### Result

\[
G:\Sigma_0\rightsquigarrow\Sigma_1
\]

does not yet name a distinctive equation type. At most it reminds the reader to provide an actual standard translation, embedding, projection, rewrite, rule application, extension, or interpretation.

### Strongest surviving distinction

Within the current evidence, the most useful distinction is:

> a value changes within a fixed specification

versus

> the language, admissible object class, observable algebra, independent variables, or rules being compared change relative to an explicit comparison map.

Even this does not define “genuine generation”: graph growth can be an ordinary transition when graphs are states, and a new observable can be a definitional extension.

### Strongest negative result

New symbol, new nameable observable, new order, or new metric does not by itself establish an independent structural addition. Toys B, E, and F give direct controls.

## 5. Existing mathematics stress map

The purpose of this map is reduction, not novelty hunting.

| Standard area | What it already describes | What it does not establish by itself | Initial relation to the candidate |
|---|---|---|---|
| dynamical systems | trajectories, flows, invariant sets on specified state spaces | change of variable types or law language unless encoded | sufficient for fixed-space evolution |
| transition systems | labeled or unlabeled steps between configurations | why a transition is ontologically generative | can encode growing configurations |
| rewriting systems | rule-governed replacement of terms / structures | physical interpretation or rule-space generation | likely sufficient for many discrete “generation” claims |
| graph rewriting / graph growth | node/edge creation and deletion with application conditions | novelty beyond the graph grammar | strong existing candidate for VED discrete network growth |
| type formation / inductive definitions | construction of well-formed types, terms, and least generated classes | change of the meta-level formation rules | sufficient for formal object-class generation under fixed rules |
| structural operational semantics | transition relations induced by syntax-directed rules | an intrinsic generation concept | standard framework for rule-based configuration evolution |
| process calculi | interaction, communication, name creation, reconfiguration | proof that a physical structure has emerged | relevant when interaction processes are primary |
| category-theoretic morphisms / functors / adjunctions | structure-preserving comparison, transport, and universal mapping relations | generativity as such; physical mechanism | useful language for source/target/maps, not a verdict |
| definitional extension | new vocabulary eliminable into an old language | independent new state or ontology | primary false-positive control |
| conservative extension | no new consequences in a specified old language | same syntax, same proofs, or no new expanded-language claims | precise consequence-preservation test |
| interpretability | translation of one theory in another | literal identity or proof identity | handles cross-specification representability |
| expressive-power comparison | what properties a fixed language can distinguish | ontological enlargement | tests “new observable” only relative to languages |
| variable-dimension / evolving-state-space models | systems whose active coordinates or components change | that changing dimension needs a new equation kind | likely absorbs many state-space enlargement cases |
| adaptive / coevolving networks | coupled update of node states and network topology | unrestricted rule or observable generation | relevant to relation / topology coevolution |
| open-ended evolution | continuing novelty / diversity under operational criteria | universal novelty or a unique definition of “open-ended” | warning that false-positive criteria are easy to construct |
| causal sets / order growth | locally finite partial order and possible sequential growth descriptions | identification of construction-stage order with physical time | useful metatime control |
| emergent-geometry constructions | graph/order/interaction data mapped to metric or manifold-like observables | uniqueness, continuum limit, or physical adequacy | relevant to VED distance / geometry claims |

### Source checks for selected standard areas

- Plotkin’s [A Structural Approach to Operational Semantics](https://homepages.inf.ed.ac.uk/gdp/publications/sos_jlap.pdf) formulates operational behavior with transition systems and syntax-directed rules. This supports using SOS as an existing description of configuration evolution; it does not establish that every changing specification reduces to SOS.
- Ehrig et al., [Fundamentals of Algebraic Graph Transformation](https://link.springer.com/book/10.1007/3-540-31188-2), treats rule-based manipulation of graphs. It supports graph rewriting as the first standard comparison for node/edge growth.
- Bombelli et al., [Space-time as a causal set](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.59.521), uses a locally finite partial order as the underlying structure and discusses manifold approximation. It supports keeping causal order and emergent continuum geometry distinct.
- Witkowski and Ikegami’s [Open-Endedness for the Sake of Open-Endedness](https://direct.mit.edu/artl/article/25/2/198/2923/Open-Endedness-for-the-Sake-of-Open-Endedness) gives a computational false-positive warning: proposed open-endedness criteria can be satisfied by unexpectedly simple systems. It does not settle VED or define generation universally.

The cited sources bound particular comparison claims. They are not a comprehensive literature review.

## 6. Phase 2 result: toy controls

The full tests are in [redescription vs generation](./redescription_vs_generation_test_v0.1_ja.md).

| Control | Result |
|---|---|
| bijective renaming | literal syntax changes; structure and satisfaction transport |
| explicit definition | new symbol / observable may add no independent choice |
| product state enlargement | additional freedom can be shown relative to a forgetful map, but the addition was externally stipulated |
| edge creation | a new relation instance can be an ordinary state transition |
| transitive-closure order | new ordering can be definitional |
| shortest-path metric | metric can be a construction from existing weighted relations |
| two construction routes | one route failure does not imply impossibility |
| alias state | increased token count can leave observational distinctions unchanged |

### Disposition of G0–G5

The proposed G0–G5 list is **KILL as a hierarchy** and **DOWNGRADE as a checklist**. It is not stable under definitional expansion or changes in what is included in a state. No numeric or ordinal strength is introduced.

## 7. Evidence burden

The dedicated table is [generative claim evidence burden](./generative_claim_evidence_burden_v0.1_ja.md).

The main split is:

\[
\text{this specified construction fails}
\neq
\text{the fixed target is impossible}
\neq
\text{the target or comparison changed}.
\]

The first toy pass adds two practical diagnostics: route precondition failure and comparison underdetermination. These do not form a new calculus; they prevent an unsupported universal negative.

## 8. Metatime problem

### 8.1 Five different orders

For

\[
\Sigma_n\to\Sigma_{n+1},
\]

the indices may represent derivation order, construction order, log order, external physical time, or an emergent internal order. A stage index can be legitimate without being physical time, provided the text says so.

### 8.2 Prohibited inference

An ordered construction history does not show that physical time was already present in the source, nor does it show that the target’s causal order is identical to the metalinguistic order.

### 8.3 VED relevance, not yet application

The current VED expression

\[
\frac{d\tau_i}{dt}=\rho_i
\]

uses \(t\) while interpreting \(\tau_i\) as locally generated time. IFGT later uses \(\partial/\partial\tau\) in a field equation. A later audit must state whether \(t\) is bookkeeping, external model time, proper time, or a physical parameter, and whether \(\tau\) is an observable derived along an already ordered history. No rewrite is proposed here.

## 9. Preliminary VED audit queue

This is an inspection queue only. The ten-field reconstruction schema is frozen in [ved_reconstruction/README](./ved_reconstruction/README_ja.md).

| Item | Preliminary role candidates | Main question before reconstruction |
|---|---|---|
| difference \(\delta,\Delta\) | primitive condition / source variable | what mathematical domain makes difference and gradient meaningful? |
| gradient | differential operator / derived observable | which geometry or graph differential is fixed first? |
| \(C_{ij}\) | definition, fixed-point relation, constitutive selection rule | causal log vs closure-degree terminology; existence / multiplicity of fixed points |
| \(H_{ij}\) | state/history record | what order and accumulation are presupposed? |
| \(\rho_i\) | defined aggregate / density interpretation | definition versus physical time-rate claim |
| \(J_{ij}\) | defined antisymmetric flow; continuum field after limit | exact discrete-to-continuum construction |
| \(\omega,L\) | continuum diagnostic / closure proxy | dimension, orientation, curl, and stability requirements |
| non-closure | constraint / phenomenological barrier | structural prohibition versus modeled potential |
| update / irreversibility | dynamics and monotonicity claim | mathematical noninvertibility versus physical irreversibility |
| \(\tau\) | accumulated observable / candidate emergent time | metatime and operational interpretation |
| information \(I\) | defined complementary field | scalar \(C\) relation and independent empirical content |
| interaction | prose-level coupling / edge influence | no unique symbol \(I\) found; source must be disambiguated |
| distance \(d\) | graph metric construction / coarse-grained geometry | metric conditions, unreachable nodes, coarse-graining evidence |

## 10. Current hypotheses and dispositions

| ID | Hypothesis | Evidence | Disposition |
|---|---|---|---|
| H1 | law-like descriptions operate inside fixed specifications | six standard law forms | **RETAIN WITH REVISION** |
| H2 | generative equations are a distinct syntactic form | same syntax supports several roles | **DOWNGRADE / likely KILL** |
| H3 | structural enlargement differs from value update | Toy C relative to fixed projection | **RETAIN as relation-relative distinction** |
| H4 | new observables show new freedom | Toy B | **KILL in unqualified form** |
| H5 | ordering / metric creation is stronger than definition | Toys E/F | **KILL in unqualified form** |
| H6 | G0–G5 is an ordered hierarchy | cross-level collapses | **KILL as hierarchy** |
| H7 | “law = convergence; generation = opening” is a general distinction | standard counterforms | **NOT ADOPTED / OPEN only as later interpretation** |
| H8 | a special generative arrow adds content | no rules or semantics beyond standard maps | **DOWNGRADE** |
| H9 | existing mathematics is insufficient | initial comparison finds broad coverage | **NOT ESTABLISHED** |
| H10 | VED needs immediate equation rewrite | methodology incomplete | **KILL for current phase** |

## 11. Open questions

1. Can additional independent freedom be characterized robustly under different but explicitly equivalent presentations?
2. Can graph growth represented in a fixed universal state space be distinguished in a useful, non-ontological way from a change of state-space specification?
3. Which equivalence—definitional, conservative, interpretive, behavioral, observational—is appropriate for each “mere redescription” claim?
4. Can a rule that changes the active rule set be represented as an ordinary higher-order transition without losing any claimed content?
5. What evidence distinguishes “derived metric observable” from an independently dynamical metric field?
6. Can an internal partial order be recovered independently of construction labels in a growth model?
7. Is there a VED equation for interaction \(I\), or is the intended item IFGT information density \(I\)?
8. Do the C and \(\Delta\) notation tensions reflect historical layers, distinct variables, or unresolved conflations?
9. What physical or mathematical evidence would turn a formal construction of time / distance into an emergence claim rather than a definition?
10. After all standard translations, does any stable residual need a distinct name?

## 12. Next-phase experiments

### Experiment 1 — definable versus independent observable — COMPLETE

Use one finite source model class and two target extensions:

- target D: a fresh observable uniquely definable from source data;
- target I: a fresh observable with at least two inequivalent expansions over one source model.

Preregister the forgetful map and observational equivalence. Test whether “new observable” separates only after model-expansion fibers and identifiability are fixed.

Completed in the [observable-independence finite-model stress test](./stress_tests/observable_independence_finite_model_v0.1_ja.md), with its [checker](./stress_tests/observable_independence_finite_model_v0.1.py).

### Experiment 2 — graph growth under two encodings — COMPLETE

Describe the same finite node-addition process:

1. as graph rewriting in a fixed state class;
2. as a sequence of changing carrier specifications.

Provide translations and compare reachable graph states and proof / run records. Ask whether any substantive claim changes or only the encoding boundary.

Completed in the [graph-growth dual-encoding stress test](./stress_tests/graph_growth_dual_encoding_v0.1_ja.md), with its [checker](./stress_tests/graph_growth_dual_encoding_v0.1.py).

### Experiment 3 — order generation and stage-label invariance — COMPLETE

Construct a finite acyclic growth process. Permute independent construction steps while holding the final partial order fixed. Test which statements depend on bookkeeping order and which on internal causal order.

Completed in the [construction versus internal order stress test](./stress_tests/construction_vs_internal_order_v0.1_ja.md), with its [checker](./stress_tests/construction_vs_internal_order_v0.1.py).

### Experiment 4 — relation-to-metric construction — COMPLETE

Vary positivity, symmetry, connectivity, and quotient conditions in shortest-path constructions. Classify metric, pseudometric, extended metric, or failure. This tests whether “metric generation” is a theorem under explicit conditions or loose prose.

Completed in the [relation-to-metric boundary stress test](./stress_tests/relation_to_metric_boundary_v0.1_ja.md), with its [checker](./stress_tests/relation_to_metric_boundary_v0.1.py).

### Experiment 5 — rule-space-as-data control — COMPLETE

Encode a small family of rewrite rules as data manipulated by a fixed meta-rule. Compare it with a literal change of the operational semantics. Test whether G5 survives a higher-order fixed-specification encoding.

Completed in the [rule-space-as-data stress test](./stress_tests/rule_space_as_data_v0.1_ja.md), with its [checker](./stress_tests/rule_space_as_data_v0.1.py).

### Gate before VED reconstruction — AUDITED / STOP-A

The preregistered gate required Experiments 1–5 and a cross-test synthesis before any VED rewrite or reclassification. The synthesis checked:

- target identity is stable across paired encodings;
- “new” is distinguished from definitional accessibility;
- metatime is separated from generated order;
- standard terminology is insufficient for a repeated residual;
- the evidence table can be applied without changing the claim.

The first, second, third, and fifth controls were usable. The fourth was not
satisfied: no repeated residual beyond standard terminology was established.
The resulting decision is **STOP-A**, recorded in the
[Phase 4 synthesis](./phase4_cross_test_synthesis_v0.1_ja.md).

## 13. Current conclusion

The initial branch is viable as an **audit methodology**, not as a new theory. Law-like description can be discussed with ordinary model specification and admissibility. Candidate generation claims decompose into ordinary state transitions, rewriting, language extensions, model expansions, structure constructions, and comparison relations. The strongest current result is the need to type what is “new,” to state exactly what a translation preserves, to separate construction indices from internal order and metric time, to separate relation data from weighting and distance policy, to distinguish rule parameters, active sets, syntax, types, and meta-rules, and to match each claim with a distinct evidence burden. The strongest negative results are that visible novelty of symbols or derived structures is not sufficient evidence of independent structural generation, bounded carrier growth can add no new reachable-state content beyond an ordinary fixed-space transition presentation, a construction sequence does not by itself establish internal or physical time, a derived graph metric does not establish independent metric freedom or physical space, and many finite operational-rule changes are ordinary state changes once rule codes and a fixed interpreter are included in the state specification.

VED reconstruction readiness: **AUDIT-READY ONLY; NOT STARTED**. All five Phase 4 finite tests and their synthesis are complete. No repeated residual beyond standard terminology was established, so Phase 5 and special notation are frozen. A separately requested VED audit could use the retained checklist, but no VED claim is supported and no equation rewrite begins here.

## 14. Phase 4a result — observable independence

The first planned finite stress test is complete.

### Exact result

For a fixed source / target pair, forgetful map \(p\), and target observational equivalence,

\[
\exists x\in X_0\;
\#\bigl(p^{-1}(x)/{\sim_{\mathrm{obs}}}\bigr)>1
\]

detects observationally separated target expansions in the encoded finite models. It does not provide a map-independent or observation-independent notion of freedom.

### Controls

- explicit definitions \(Q=1-P\) and \(Q=P\mathbin{\mathrm{xor}}R\) have unique expansions;
- redundant and uncoupled raw coordinates enlarge fibers but collapse observationally;
- a directly observed \(U\) yields two quotient classes over each Boolean source state;
- changing the comparison map reverses the result;
- the map that produces the false positive fails to preserve the declared source observable;
- omitting a source observable can make an old distinction appear new.

### Dispositions

- H-O1 raw fiber multiplicity as sufficient: **KILL**.
- H-O2 quotient-fiber separation: **REVISE** to a static, relation-relative diagnostic.
- H-O3 separation from explicit definition: **RETAIN WITH SCOPE** in fixed finite languages/models.
- H-O4 map invariance: **KILL in unqualified form**; invariance across admissible maps remains OPEN.
- H-O5 freedom implies generation mechanism: **KILL**.

### Research effect

The experiment advances model-expansion auditing but does not advance the claim that a distinct generative equation exists. Standard functional dependence, explicit definability, model expansion, observation equivalence, and quotienting suffice for all six cases.

The graph-growth comparison planned here is now complete; see §15. VED reconstruction remains **NOT READY**.

## 15. Phase 4b result — graph growth under dual encodings

The second finite stress test is complete.

### Exact finite result

For the bounded universe (U=\{a,b,c\}), fixed allowed edges, and fixed node/edge-addition rules, the reachable part of:

1. a fixed-state-space rewrite system whose states are active subgraphs of (U); and
2. canonical stage records whose carrier and node-constant language grow;

is isomorphic as a labeled transition system. The checker found 13 reachable states and 20 one-step transitions on each side. Three selected predicates and five explicit histories to one final graph were preserved by nodewise/pathwise translation.

### Residual difference

The fixed-universe full language can refer to an inactive future node and evaluate an `Inactive` predicate before activation. The stage-local changing-carrier language cannot yet form that reference. Active-only restriction on the fixed encoding, or a global registry added to the changing-carrier record, removes this mismatch. Thus the difference is real at the chosen language boundary but does not establish a distinct mechanism.

### Dispositions

- H-GR1 fixed-space representation: **RETAIN WITH SCOPE** for this bounded finite process.
- H-GR2 changing-carrier representation: **RETAIN WITH SCOPE**.
- H-GR3 reachable-state / selected-predicate preservation: **RETAIN WITH SCOPE**.
- H-GR4 full equivalence for all tested structure: **KILL**.
- H-GR5 inactive always equals nonexistent: **KILL**.
- H-GR6 history requires changing-carrier formalism: **KILL**.
- H-GR7 full-equivalence failure proves a special generative equation: **KILL**.

### Research effect

The test sharpens the preservation audit: state, transition, predicate, path, label quotient, stage-local language, and future-reference data must be compared separately. Standard transition-system and graph-isomorphism terminology suffices. A distinct generative equation remains **NOT ESTABLISHED**.

The construction/internal-order experiment announced here is now complete; see §16. VED reconstruction remains **NOT READY**.

## 16. Phase 4c result — construction order versus internal order

The third finite stress test is complete.

### Exact finite result

For the partial order generated by (a\prec c), (b\prec c), and (c\prec d), exhaustive enumeration found exactly two linear extensions:

\[
(a,b,c,d),
\qquad
(b,a,c,d).
\]

They are distinct construction histories but map to the same internal partial order. Of all 24 permutations, the other 22 violate at least one predecessor condition. Quotienting the two valid histories by equality of their pure-order target yields one class.

### Controls

- a dependent swap such as `(a,b,d,c)` is invalid rather than an alternative linearization of the same target;
- adding an order-sensitive finite cost separates the two histories again, so the pure-order quotient is target-relative;
- even within timestamp values `0..3`, the same partial order admits six strict order-preserving assignments;
- construction-position timestamps depend on which linear extension was chosen;
- the same comparable pair can receive duration differences `2` and `90` under two valid timestamp assignments;
- a fixed six-state transition system retains both histories without a changing-carrier formalism.

### Dispositions

- H-ORD1 construction order equals internal order: **KILL**.
- H-ORD2 different histories can yield one internal order: **RETAIN WITH SCOPE**.
- H-ORD3 internal order uniquely recovers history: **KILL**.
- H-ORD4 incomparable-event construction order proves an internal physical difference: **KILL as an unqualified inference**.
- H-ORD5 stage index directly supplies emergent physical time: **KILL**.
- H-ORD6 timestamps establish physical time: **KILL as stated**.
- H-ORD7 the separation requires a distinct generative equation: **KILL**.

### Research effect

The result is fully expressible with standard partial orders, linear extensions, path-dependent data, order-preserving maps, and transition systems. It establishes no physical time or causality. A distinct generative equation remains **NOT ESTABLISHED**.

The metric-boundary experiment announced here is now complete; see §17. VED reconstruction remains **NOT READY**.

## 17. Phase 4d result — relation-to-metric boundary

The fourth finite stress test is complete.

### Exact finite result

Shortest-path construction on three-node graphs produced different standard objects under controlled changes:

- connected undirected positive weights: an ordinary metric;
- one zero-weight edge: a pseudometric, with a metric on the zero-distance quotient;
- a disconnected positive graph: an extended metric under the `+∞` policy, or componentwise/partial alternatives;
- a strongly connected positive directed graph: a finite asymmetric quasi-metric under the stated convention;
- a negative edge without a negative cycle: finite values but failed nonnegativity;
- a reachable negative cycle: six ordered pairs with infimum `-∞` under the repeated-walk convention.

An unweighted relation plus edge-count convention yielded a metric. The same relation with weights `(2,5)` yielded a different metric. Positive rescaling and an off-diagonal shift preserved the finite example’s metric axioms, while squaring distances broke triangle inequality. One fixed microscopic metric and cluster map produced coarse distances `1`, `1.5`, and `2` under three policies.

### Dispositions

- H-MET1 any relation supports a derived ordinary metric: **KILL**.
- H-MET2 connected undirected positive shortest paths form a metric: **RETAIN WITH SCOPE**.
- H-MET3 zero weights always preserve metric identity: **KILL**.
- H-MET4 disconnected relation has no useful distance structure: **KILL**.
- H-MET5 directed relation naturally yields an ordinary metric: **KILL**.
- H-MET6 definability establishes independent metric generation: **KILL**.
- H-MET7 relation alone uniquely determines a metric: **KILL**.
- H-MET8 triangle inequality requires an independent law: **KILL**.
- H-MET9 ordinary metric failure destroys every useful distance notion: **KILL**.
- H-MET10 standard metric construction establishes physical spatial emergence: **KILL as an inference**; emergence **NOT ESTABLISHED**.

### Research effect

The result is fully expressible with standard graph distance, metric axioms, pseudometric quotient, extended metric, asymmetric distance, and policy-dependent coarse-graining. A uniquely computed metric under fixed inputs is a derived observable, not evidence of an independent metric field or physical space. A distinct generative equation remains **NOT ESTABLISHED**.

The rule-space-as-data control announced here is now complete; see §18. VED reconstruction remains **NOT READY**.

## 18. Phase 4e result — rule space as data

The fifth finite stress test is complete.

### Exact finite result

For \(X=\{0,1,2\}\), the predeclared repertoire

\[
\mathcal R=\{r_+,r_-,r_0\},
\]

and a fixed boundary-switching policy, the explicit changing-rule records
\((x_t,R_t)\) and coded states \((x_t,\operatorname{code}(R_t))\) are in
bijection on the reachable core system. The translations preserve all four
reachable states, the object-state trace, the active-rule trace, and rule-change
events at steps \(2,4,6,8\).

The checker also embeds rule enable/disable in a finite powerset state space,
parameter changes in \(X\times\Theta\), a bounded history-dependent update in an
enlarged state, and one finite meta-rule change under a fixed higher interpreter.
An alias for \(r_0\) changes syntax without changing behavior; the newly named
\(r_+\circ r_+\) is a derived macro rather than an independently generated rule.

### Residual difference

The fixed encoding preloads a rule-code syntax, interpreter, candidate
repertoire, parameter/type universe, admissible meta-transitions, and validity
conditions. In particular, “globally encoded but inactive,” “unavailable in the
stage-local rule language,” and “ill-formed at that stage” are not literally the
same status. Ex post construction of a finite maximal repertoire is a modeling
representation result, not evidence that the modeled system physically possessed
all future rules.

### Dispositions

- H-RULE1 rule change is always distinct from state change: **KILL**.
- H-RULE2 finite rule change admits a rules-as-data encoding: **RETAIN WITH SCOPE**.
- H-RULE3 preserved traces remove the need for a special equation in this class: **RETAIN WITH SCOPE**.
- H-RULE4 the fixed encoding preloads representation resources: **RETAIN WITH SCOPE**.
- H-RULE5 inactive-preloaded equals stage-unavailable without qualification: **KILL**.
- H-RULE6 a fixed meta-rule encodes the tested endogenous finite updates: **RETAIN WITH SCOPE**.
- H-RULE7 changing the meta-rule establishes a distinct generative equation: **KILL as an inference**; unrestricted meta-level change remains **OPEN / NOT ESTABLISHED**.
- H-RULE8 parameter, symbol, and type changes are one novelty kind: **KILL**.
- H-RULE9 behavioral novelty implies endogenous generation: **KILL**.
- H-RULE10 universal reduction of rule-space growth: **NOT ESTABLISHED**.

### Research effect

The result is fully expressible with finite transition systems, rule tables,
interpreters, powerset states, parameters, typed operations, trace equivalence,
and state augmentation. It weakens the case for a distinct generative equation
within the tested finite class, while exposing the precise specification that a
fixed-law representation must preload. The Phase 4 cross-test synthesis is now
complete; see §19. It does not authorize immediate VED reconstruction or special
notation.

## 19. Phase 4 cross-test synthesis and stopping decision

The [cross-test synthesis](./phase4_cross_test_synthesis_v0.1_ja.md) compares
observable expansion, carrier growth, construction/internal order, metric
construction, and rule-space change.

### Cross-test result

- new names, carriers, orders, metrics, and rules did not form one ordered
  novelty hierarchy;
- bounded carrier/rule changes were often representable as ordinary state
  transitions after maximal spaces, codes, or interpreters were fixed;
- definability, observational distinction, operational relevance, endogenous
  mechanism, and physical interpretation remained separate claims;
- literal stage-local language/type availability could differ even when selected
  behavior was preserved;
- preload of future candidates was a representation condition, not evidence of
  physical ontology, system knowledge, or predetermined outcomes;
- standard model expansion, transition-system, order-theoretic, metric, and
  interpreter terminology described every established finite result.

### Final dispositions

- distinct generative equation: **NOT ESTABLISHED; pursuit frozen**;
- \(G:\Sigma_0\rightsquigarrow\Sigma_1\): **DOWNGRADE**;
- G0–G5: **KILL as hierarchy; DOWNGRADE as checklist**;
- independent structural freedom: **RETAIN WITH SCOPE** as a
  comparison-relative diagnostic;
- stage-local specification difference: **RETAIN**;
- preservation/preload/evidence audit: **RETAIN WITH SCOPE**;
- universal reducibility: **NOT ESTABLISHED**;
- ontological generation: **NOT ESTABLISHED and not refuted**.

### Stopping decision

**STOP-A / STOP AND SYNTHESIZE AS AUDIT METHODOLOGY.**

Phase 5 is not entered and special notation remains frozen. This is a stopping
decision under the finite-study gate, not a universal impossibility theorem.
VED reconstruction remains unstarted; only a separately scoped
equation-by-equation audit is methodologically ready.

The working note remains **v0.1** because its posture, object, and central
negative verdict did not change.

The branch closure is recorded in the
[final experimental record v1.0](./generative_law_methodology_final_record_v1.0_ja.md).
This working note remains the historical working record; it is not revised to
v0.2 and does not reopen Phase 5.

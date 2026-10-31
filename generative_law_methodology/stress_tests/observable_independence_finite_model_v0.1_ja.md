# Observable independence finite-model stress test v0.1

> Status:
> - exploratory finite-model stress test
> - not a theorem
> - not a proof of a generative law
> - not a model of VED
> - no ontology or physical emergence claim
> - Claim 6, generation by a mechanism, is out of scope

## 0. Position in the research branch

The initial methodology left the following distinction open:

\[
\text{newly definable}
\neq
\text{independently variable}.
\]

Toy B showed that a directly available observable can be explicitly definable. Toy C showed multiple raw expansions relative to a projection. Toy H showed that aliases can inflate a carrier without adding observational distinctions. This experiment fixes finite source / target specifications, a forgetful map, target observables, observational equivalence, and definability tests, then asks exactly how far the separation can be made.

The prior dispositions remain unchanged:

- generative equation as an independent mathematical object: **NOT ESTABLISHED**;
- \(G:\Sigma_0\rightsquigarrow\Sigma_1\): provisional placeholder, **DOWNGRADE**;
- G0–G5 as hierarchy: **KILL**; as checklist: **DOWNGRADE**;
- no VED reconstruction in this experiment.

## 1. Exact question

Given

\[
\Sigma_0=(\mathcal L_0,X_0,\mathcal O_0,\Theta_0),
\qquad
\Sigma_1=(\mathcal L_1,X_1,\mathcal O_1,\Theta_1)
\]

and a fixed map

\[
p:X_1\to X_0,
\]

when do multiple target states over one source state support the narrow claim:

> there are additional observationally distinguishable target alternatives relative to \(p\) and the declared target observables?

The experiment does not identify that claim with endogenous generation, physical relevance, or ontology.

## 2. Common finite definitions

Let

\[
\mathbb B=\{0,1\}.
\]

For each model, \(\mathcal O_1\) is a finite family of functions \(O:X_1\to V_O\). Define target observational equivalence by

\[
x'_1\sim_{\mathrm{obs}}x'_2
\quad\Longleftrightarrow\quad
\forall O\in\mathcal O_1,\;
O(x'_1)=O(x'_2).
\]

For \(x\in X_0\), the raw fiber and its observational quotient are

\[
p^{-1}(x)
\quad\text{and}\quad
p^{-1}(x)/{\sim_{\mathrm{obs}}}.
\]

The tested candidate condition is

\[
\exists x\in X_0\;
\#\bigl(p^{-1}(x)/{\sim_{\mathrm{obs}}}\bigr)>1.
\tag{FS}
\]

Equivalently in these finite models, there are \(x'_1,x'_2\in p^{-1}(x)\) separated by at least one allowed target observable. “FS” is only a label local to this record. Quotient cardinality is a finite diagnostic, not a generation measure or score.

### 2.1 Specification registry

Let \(\Theta_{\mathbb B}\) denote ordinary two-valued Boolean evaluation. Representation constraints and update rules used by a case are recorded in its \(\Theta\)-component; no temporal or physical interpretation is attached to it.

#### Case A

\[
\Sigma_0^A=
(\{P\},\mathbb B,\{P\},\Theta_{\mathbb B}),
\]

\[
\Sigma_1^A=
(\{P,Q\},
\{(p,q)\in\mathbb B^2:q=1-p\},
\{P,Q\},
\Theta_{\mathbb B}+\{Q=1-P\}),
\]

\[
p_A(p,q)=p.
\]

#### Case B

\[
\Sigma_0^B=
(\{P\},\mathbb B,\{P\},\Theta_{\mathbb B}),
\]

\[
\Sigma_1^B=
(\{P,R\},\mathbb B^2,\{P\},
\Theta_{\mathbb B}+\{R\text{ is an unobserved representation tag}\}),
\]

\[
p_B(x,r)=x.
\]

#### Case C

\[
\Sigma_0^C=
(\{P\},\mathbb B,\{P\},\Theta_{\mathbb B}),
\]

\[
\Sigma_1^C=
(\{P,U\},\mathbb B^2,\{P,U\},\Theta_{\mathbb B}),
\]

\[
p_C(x,u)=x.
\]

#### Case D

\[
\Sigma_0^D=
(\{S\},\mathbb B,\{S\},\Theta_{\mathbb B}),
\]

\[
\Sigma_1^D=
(\{X,U\},\mathbb B^2,\{X\},\Theta_{\mathbb B}),
\]

\[
p_1(x,u)=x,\qquad p_2(x,u)=u.
\]

The target specification and \(\sim_{\mathrm{obs}}\) are held fixed while the comparison map changes.

#### Control E

\[
\Sigma_0^E=
(\{P,R\},\mathbb B^2,\{P,R\},\Theta_{\mathbb B}),
\]

\[
\Sigma_1^E=
(\{P,R,Q\},
\{(p,r,q)\in\mathbb B^3:q=p\mathbin{\mathrm{xor}}r\},
\{P,R,Q\},
\Theta_{\mathbb B}+\{Q=P\mathbin{\mathrm{xor}}R\}),
\]

\[
p_E(p,r,q)=(p,r).
\]

#### Control F

\[
\Sigma_0^F=
(\{P,d_0\},\mathbb B,\{P\},
\Theta_{\mathbb B}+\{d_0(x)=1-x\}),
\]

\[
\Sigma_1^F=
(\{P,U,d_1\},\mathbb B^2,\{P\},
\Theta_{\mathbb B}+\{d_1(x,u)=(1-x,u)\}),
\]

\[
p_F(x,u)=x.
\]

In every case, \(\sim_{\mathrm{obs}}\) is induced by exactly the displayed \(\mathcal O_1\). Symbols present in \(\mathcal L_1\) but absent from \(\mathcal O_1\) do not count as allowed observations in that case.

## 3. Definability criteria

The experiment separates five standard notions.

### 3.1 Explicit definability

A target observable \(Q\) is explicitly definable in the selected source language if a stated source expression \(\psi\) satisfies

\[
Q(x')=\psi(p(x'))
\quad\text{for all }x'\in X_1.
\]

Cases A and E provide the formulas \(Q=1-P\) and \(Q=P\mathbin{\mathrm{xor}}R\).

### 3.2 Extensional functional dependence

\(Q\) is functionally dependent on the complete source state through \(p\) if

\[
p(x'_1)=p(x'_2)
\Rightarrow
Q(x'_1)=Q(x'_2).
\]

This is equivalent to \(Q=h\circ p\) for some set function \(h\) on the image of \(p\). In a restricted language, existence of \(h\) need not imply that \(h\) is expressible by a source formula.

### 3.3 Unique model expansion

Every source state has a unique target expansion when

\[
\forall x\in X_0,\qquad |p^{-1}(x)|=1.
\]

This determines the entire target state relative to the source. It is stronger than functional dependence of one selected observable. Conversely, a definable observable can coexist with unrelated redundant target coordinates and therefore need not make every raw fiber singleton.

### 3.4 Definitional extension and old-language conservativity

Cases A and E are explicit Boolean definitions. The checker confirms that every encoded source valuation has exactly one expansion satisfying the definition and that old observables are preserved. In standard classical propositional logic, explicit-definition elimination gives conservativity for old-language formulas.

The checker does not prove the general conservativity theorem; it exhausts only the encoded finite valuations.

### 3.5 Observational recovery

A target value is recoverable from the selected source state exactly when it is constant on each raw fiber. This depends on what the source state records. Omitting a source observable can manufacture non-recoverability.

## 4. Case A — pure definitional observable

### Specifications

\[
\mathcal L_0=\{P\},\quad
X_0=\mathbb B,\quad
\mathcal O_0=\{P(x)=x\},
\]

with two-valued Boolean background \(\Theta_0\).

\[
\mathcal L_1=\{P,Q\},\quad
X_1=\{(0,1),(1,0)\},\quad
\mathcal O_1=\{P(p,q)=p,\ Q(p,q)=q\},
\]

and

\[
\Theta_1=\Theta_0+\{Q=1-P\}.
\]

The forgetful map is

\[
p_A(p,q)=p.
\]

Observational equivalence compares both \(P\) and \(Q\).

### Enumerated result

\[
|p_A^{-1}(0)|=|p_A^{-1}(1)|=1,
\]

and both quotient-fiber counts are one. \(Q=1-P\) holds in every target state. Target vocabulary and direct observational access increase, but assignments do not.

### Verdict

**DEFINITIONAL ACCESS, NOT INDEPENDENT FREEDOM — RETAIN.**

This case supports Claims 1 and explicit definability, not Claims 3–6.

## 5. Case B — redundant parameterization

### Specifications

\[
\mathcal L_0=\{P\},\quad X_0=\mathbb B,\quad\mathcal O_0=\{P\}.
\]

The target carrier is

\[
X_1=\mathbb B\times\mathbb B,
\]

with coordinates \((x,r)\). The representation records \(r\), but the declared allowed observable family is

\[
\mathcal O_1=\{P(x,r)=x\}.
\]

The target background treats \(r\) as an unobserved representational tag. Let

\[
p_B(x,r)=x.
\]

Then

\[
(x,0)\sim_{\mathrm{obs}}(x,1).
\]

### Enumerated result

\[
|p_B^{-1}(x)|=2,
\qquad
\#\bigl(p_B^{-1}(x)/{\sim_{\mathrm{obs}}}\bigr)=1
\]

for both source states.

The raw tag \(r\) is not a function of \(x\), yet it does not survive the selected observational quotient.

### Verdict

**LARGE FIBER WITHOUT NEW DISTINCTION — RETAIN.**

This is the direct counterexample to H-O1.

## 6. Case C — independently distinguishable coordinate

### Specifications

Use the same source:

\[
\mathcal L_0=\{P\},\quad X_0=\mathbb B,\quad\mathcal O_0=\{P\}.
\]

The target is

\[
\mathcal L_1=\{P,U\},\quad
X_1=\mathbb B\times\mathbb B,
\]

with allowed observables

\[
\mathcal O_1=
\{P(x,u)=x,\ U(x,u)=u\}.
\]

Let

\[
p_C(x,u)=x.
\]

Observational equivalence compares both \(P\) and \(U\).

### Enumerated result

For each \(x\),

\[
|p_C^{-1}(x)|=2
\]

and

\[
\#\bigl(p_C^{-1}(x)/{\sim_{\mathrm{obs}}}\bigr)=2.
\]

In particular,

\[
(x,0)\not\sim_{\mathrm{obs}}(x,1).
\]

There is no function \(h:X_0\to\mathbb B\) satisfying \(U=h\circ p_C\), because \(U(x,0)\neq U(x,1)\) above the same \(x\).

### Verdict

**ADDITIONAL DISTINGUISHABLE FREEDOM RELATIVE TO \(p_C\) AND \(\sim_{\mathrm{obs}}\) — RETAIN WITH SCOPE.**

The product target was stipulated externally. No transition or endogenous construction producing \(u\) was supplied. This establishes a static model-expansion fact, not Claim 6.

## 7. Case D — fake independence from a bad comparison map

### Fixed source and target

\[
X_0=\mathbb B,
\qquad
X_1=\mathbb B\times\mathbb B.
\]

The source observable is \(S(s)=s\). The target has one allowed observable

\[
X(x,u)=x,
\]

so

\[
(x,0)\sim_{\mathrm{obs}}(x,1),
\qquad
(0,u)\not\sim_{\mathrm{obs}}(1,v).
\]

Compare two maps on this same target:

\[
p_1(x,u)=x,
\qquad
p_2(x,u)=u.
\]

### Enumerated result

For \(p_1\), fibers vary only in \(u\), which \(X\) ignores:

\[
\#\bigl(p_1^{-1}(s)/{\sim_{\mathrm{obs}}}\bigr)=1.
\]

For \(p_2\), fibers vary in \(x\), which \(X\) sees:

\[
\#\bigl(p_2^{-1}(s)/{\sim_{\mathrm{obs}}}\bigr)=2.
\]

Thus FS is false under \(p_1\) and true under \(p_2\).

But only \(p_1\) preserves the declared source observation:

\[
X(x,u)=S(p_1(x,u)).
\]

For \(p_2\), \(S(p_2(x,u))=u\), which is not generally \(X(x,u)=x\).

### Verdict

**INDEPENDENCE CLAIM IS COMPARISON-RELATIVE — RETAIN.**

The positive result under \(p_2\) is a false positive produced by a semantically bad forgetful map. Therefore a comparison map must satisfy declared observation-preservation or another explicit adequacy condition before FS is interpreted.

### Hidden-source subcontrol

Take the same target \(X_1=\mathbb B^2\) with observables \(X,U\). If the source is coarsened to \(X_0=\mathbb B\) by forgetting \(u\), FS is true. If the source was actually the full pair \(\widehat X_0=\mathbb B^2\) and the comparison is the identity, every fiber is a singleton and FS is false.

Thus a “new” \(U\) can be manufactured by omitting it from the source specification. Source completeness is not supplied by the criterion itself.

## 8. Control E — directly accessible but definable

### Specifications

\[
X_0=\mathbb B^2
\]

with source observables \(P(p,r)=p\) and \(R(p,r)=r\). Let

\[
X_1=\{(p,r,q)\in\mathbb B^3:q=p\mathbin{\mathrm{xor}}r\}.
\]

The target directly exposes \(P,R,Q\), and

\[
p_E(p,r,q)=(p,r).
\]

Observational equivalence compares all three target observables.

### Enumerated result

Every source state has exactly one target expansion; every quotient fiber is a singleton; and

\[
Q=P\mathbin{\mathrm{xor}}R
\]

is explicitly verified on all four target states.

### Verdict

**NEWLY ACCESSIBLE BUT DEFINITIONALLY RECOVERABLE — RETAIN.**

Direct measurement or naming on the target side does not imply independent variation.

## 9. Control F — non-definable but operationally inert coordinate

### Specifications and dynamics

Let

\[
X_0=\mathbb B,\quad \mathcal O_0=\{P(x)=x\},
\]

with source update

\[
d_0(x)=1-x.
\]

Let

\[
X_1=\mathbb B^2,\quad p_F(x,u)=x,
\]

but keep the allowed target observation family at

\[
\mathcal O_1=\{P(x,u)=x\}.
\]

Define the target update

\[
d_1(x,u)=(1-x,u).
\]

The coordinate \(u\) is not determined by \(x\), but neither affects \(P\) nor couples into the update of \(x\).

### Enumerated result

Raw fibers have size two; observational quotient fibers have size one. The checker verifies that \(u\) is not a function of the source state and that the allowed \(P\)-observation traces from \((x,0)\) and \((x,1)\) agree for eight steps. The agreement for every number of steps also follows immediately by induction:

\[
d_1^n(x,u)=
\begin{cases}
(x,u),&n\text{ even},\\
(1-x,u),&n\text{ odd}.
\end{cases}
\]

### Verdict

**FORMALLY FREE RAW COORDINATE WITHOUT OPERATIONAL DISTINCTION IN THE FIXED MODEL — RETAIN.**

This does not prove that unobserved coordinates are physically meaningless in general. It shows only that non-functional dependence on the source is insufficient for operational significance under the fixed observations and dynamics.

## 10. Cross-case result table

| Case | Raw fiber count | Quotient fiber count | Explicitly definable item | Function of complete source state? | Map adequate for declared source observable? | FS | Dynamical relevance |
|---|---:|---:|---|---:|---:|---:|---|
| A | 1 | 1 | \(Q=1-P\) | YES | YES | NO | NOT TESTED |
| B | 2 | 1 | tag not an allowed observable | NO for raw tag | YES | NO | none specified |
| C | 2 | 2 | no source definition of \(U\) | NO | YES | YES | NOT TESTED |
| D, \(p_1\) | 2 | 1 | target \(X=S\circ p_1\) | YES | YES | NO | NOT TESTED |
| D, \(p_2\) | 2 | 2 | N/A | NO relative to \(p_2\) | **NO** | YES | false-positive map |
| E | 1 | 1 | \(Q=P\mathbin{\mathrm{xor}}R\) | YES | YES | NO | NOT TESTED |
| F | 2 | 1 | no source function for raw \(U\) | NO | YES | NO | decoupled and unobserved |

Counts are per source state in A–C and F; all source states have the displayed value. In E the statement holds for each of the four source states.

## 11. Fiber-separation criterion stress

### 11.1 Does it exclude redundant parameterization?

**YES, relative to the fixed observables.** B and F have raw fiber size two but quotient-fiber size one.

It cannot determine whether the selected observable family is complete or scientifically appropriate.

### 11.2 Does it exclude definitional extension?

**YES for A and E.** Unique expansions make every quotient fiber a singleton.

This is not a theorem that every definitional presentation has singleton raw fibers. A definitional extension can be combined with unrelated aliases or redundant encodings. Those redundancies must be quotiented or otherwise controlled.

### 11.3 Can a hidden source observable produce a false positive?

**YES.** The hidden-source subcontrol turns the same pair-valued target from positive under coarse projection to negative under identity comparison.

### 11.4 Does it depend on observational equivalence?

**YES.** B and C use the same carrier and projection. With \(\mathcal O_1=\{P\}\), the quotient count is one; with \(\mathcal O_1=\{P,U\}\), it is two.

### 11.5 Does it depend on the forgetful map?

**YES.** Case D reverses the result. It also shows that an arbitrary map may fail to preserve source observations and should be rejected before interpretation.

### 11.6 Does it show only static freedom without target dynamics?

**YES.** Case C has no target transition rule. FS establishes distinguishable model expansions at one stage, not persistence, coupling, controllability, causal efficacy, or production by dynamics.

### 11.7 Does it establish an endogenous generation mechanism?

**NO.** All target state spaces and maps were supplied by the experimenter. No case derives its own state variables, observables, or update rules.

## 12. Evidence-burden audit

| Claim | Evidence in this experiment | Verdict | What is not established |
|---|---|---|---|
| 1. target vocabulary contains a new observable | explicit \(\mathcal L_1,\mathcal O_1\) in A, C, E | **ESTABLISHED for encoded cases** | independence, physical relevance |
| 2. observable is not explicitly definable from source observables | C has non-constancy on raw fibers, hence no function of complete source state; A/E have explicit definitions | **ESTABLISHED extensionally for C** | undefinability in arbitrary languages / theories |
| 3. multiple target expansions exist | complete finite enumeration in B, C, F | **ESTABLISHED** | observational difference |
| 4. expansions are observationally distinguishable | distinct \(\mathcal O_1\)-signatures in C | **ESTABLISHED relative to \(\mathcal O_1\)** | completeness or empirical adequacy of \(\mathcal O_1\) |
| 5. additional independent structural freedom exists relative to \(p\) | C combines same-source multiplicity, non-functional \(U\), and observational separation | **REVISE: supported only as static, relation-relative freedom** | invariance across maps / source choices; dynamics |
| 6. a mechanism generated that freedom | no generation rule or temporal construction is encoded | **NOT ESTABLISHED / OUT OF SCOPE** | all mechanism, endogeneity, physical generation claims |

## 13. Checker

The companion checker is [observable_independence_finite_model_v0.1.py](./observable_independence_finite_model_v0.1.py). It uses only the Python standard library and:

- enumerates source states and target expansions;
- computes raw fiber counts;
- partitions fibers by allowed observation signatures;
- checks extensional functional dependence;
- checks the explicit Boolean definitions in A and E;
- checks source-observation preservation for both Case D maps;
- checks the finite observation traces in F;
- asserts every reported count and verdict input.

Observed output:

~~~text
observable independence finite model v0.1
A definitional: raw={0:1, 1:1} quotient={0:1, 1:1} unique_expansion=True explicit_Q=1-P=True criterion=False
B redundant: raw={0:2, 1:2} quotient={0:1, 1:1} tag_function_of_source=False criterion=False
C distinguishable: raw={0:2, 1:2} quotient={0:2, 1:2} U_function_of_source=False criterion=True
D map choice: p1_quotient={0:1, 1:1} p1_preserves_source_observation=True p1_criterion=False; p2_quotient={0:2, 1:2} p2_preserves_source_observation=False p2_criterion=True
D hidden-source: coarse_source_criterion=True full_source_identity_criterion=False
E accessible-definable: raw={(0,0):1, (0,1):1, (1,0):1, (1,1):1} quotient={(0,0):1, (0,1):1, (1,0):1, (1,1):1} explicit_Q=P_xor_R=True criterion=False
F uncoupled: raw={0:2, 1:2} quotient={0:1, 1:1} U_function_of_source=False observed_traces_collapse_h8=True criterion=False
all_assertions_passed=6_cases
~~~

The checker verifies only combinatorial facts of the encoded finite models. It does not prove generation, ontology, physical emergence, a universal independence criterion, or a general conservativity theorem.

## 14. Is the six-item chain linear?

The proposed chain was:

\[
\text{new symbol}
\neq
\text{new definable observable}
\neq
\text{multiple expansions}
\neq
\text{observationally distinct expansions}
\neq
\text{independent structural freedom}
\neq
\text{generation mechanism}.
\]

As a list of distinctions, it survives. As a linear hierarchy, it does not.

- A/E have newly accessible definable observables without multiple expansions.
- B/F have multiple raw expansions and a non-source-functional coordinate without observationally distinct expansions.
- C has observationally distinct expansions but no mechanism.
- “new symbol” can introduce either an explicit definition or an unconstrained variable; it does not occupy one fixed place in an implication order.
- Operational relevance adds dynamics and observation choices not ordered by syntactic extension alone.

**Verdict: KILL as a general linear hierarchy; RETAIN as six separately audited claims.**

## 15. Hypothesis dispositions

### H-O1

\[
|p^{-1}(x)|>1
\]

is sufficient for additional independent freedom.

**KILL.** Case B is a direct counterexample under the selected observational criterion; F strengthens it dynamically.

### H-O2

\[
\#\bigl(p^{-1}(x)/{\sim_{\mathrm{obs}}}\bigr)>1
\]

supports additional independently distinguishable freedom.

**REVISE.** It exactly detects separated target expansions in the fixed finite model, but only relative to:

- an admissible, meaning-preserving \(p\);
- a declared target-observable family;
- a source specification that has not hidden the same distinction;
- valid target states.

It establishes static observational separation, not a mechanism or universal invariant.

### H-O3

Independently distinguishable freedom can be separated from definitional extension.

**RETAIN WITH SCOPE.** A/E versus C separate them after language, map, model class, and definability criterion are fixed. The separation is not available from vocabulary growth alone, and definability versus observational relevance are not simple complements.

### H-O4

Independently distinguishable freedom is invariant under comparison-map choice.

**KILL in unqualified form.** Case D reverses FS by changing \(p\). Requiring observation preservation rejects the bad positive map, but invariance across all admissible comparison maps was not tested and is **OPEN**.

### H-O5

Confirming independent structural freedom confirms a generation mechanism.

**KILL.** Case C supplies the target product and observable externally. Nothing generates them.

## 16. Strong falsification questions

1. **Did quotient fibers remove aliases?** Yes in B/F.
2. **Did they remove explicit definitions?** A/E never produced multiple expansions, but this is case-specific.
3. **Can source coarsening create apparent novelty?** Yes.
4. **Can map choice flip the result?** Yes; a map-admissibility obligation is required.
5. **Can observable choice flip the result?** Yes; B/C are the same carrier/projection with different observable families.
6. **Can a non-source-functional coordinate be operationally inert?** Yes in F.
7. **Does the criterion imply dynamics?** No.
8. **Does it imply endogenous generation?** No.
9. **Does standard finite model-expansion analysis suffice?** Yes for all tested claims.
10. **Did a distinct generative equation emerge?** No.

## 17. VED implication note

No VED equation is assessed here. The result only identifies later questions.

- **local time:** a newly defined \(\tau\) must be separated from an independent clock reading and from dynamics that make it operationally distinguishable.
- **distance:** a derived shortest-path \(d\) may be a definable observable of existing relations; independent metric freedom requires a separate model-expansion question.
- **closure:** a new closure label or scalar may be definitionally recoverable from prior flow data, or may introduce independent state; the map must be fixed.
- **new degree of freedom:** coordinate count is insufficient; quotient fibers, hidden source observables, and coupling must be audited.
- **emergent geometry:** observational separation of metric candidates still does not establish the process that produces one candidate or its physical adequacy.

These are future evidence requirements, not positive or negative verdicts on VED.

## 18. Final report

1. **Question:** Can definitional access and independently variable observation be separated in fixed finite model expansions?
2. **Models:** A–F, with complete Boolean enumeration.
3. **Strong positive:** Case C has two observational classes above each source state under fixed \(p_C\) and \(\mathcal O_1\).
4. **Strong negative:** raw multiplicity, non-functional raw coordinates, and direct vocabulary growth are each insufficient.
5. **Best false-positive control:** Case D; an observation-nonpreserving map reverses the criterion.
6. **Role of \(p\):** it determines which target differences count as variation over the same source state.
7. **Role of \(\sim_{\mathrm{obs}}\):** it removes distinctions ignored by all declared target observables.
8. **Role of definability:** it separates target access determined by source data from non-functional target variation, but not operational significance by itself.
9. **Established:** static, observationally separated finite model expansions can be detected relative to fixed comparison data.
10. **NOT ESTABLISHED:** generation mechanism, endogenous production, physical meaning, map-invariant freedom, or a new equation type.
11. **Methodological status:** standard finite model-extension / quotient analysis is sufficient; only an audit workflow survives.
12. **Next experiment:** compare a finite graph-growth process as a fixed graph-rewrite transition system and as changing carrier specifications, with explicit translations and identical target graph predicates.

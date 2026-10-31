# Generative equation specification v0.1

> Status:
> - exploratory specification
> - not a theorem
> - not a new calculus
> - no presumption that “generative equation” names a distinct mathematical object
> - VED-independent first pass

## 1. Working question

> source specification では利用可能でなかった object、distinction、relation、operation、degree of freedom、ordering などが target specification で利用可能になる、という claim をどう正確に書くか。

仮の図式

\[
G:\Sigma_0\rightsquigarrow\Sigma_1
\]

は、現時点では **provisional placeholder** にすぎない。\(\rightsquigarrow\) に固有の公理、composition、semantics は与えない。実際の記述では、可能な限り既存の map、relation、rewrite rule、translation、extension、interpretation を使う。

## 2. Required specification data

source と target を、必要な範囲で次のように記録する。

\[
\Sigma_k=(\mathcal L_k,X_k,\mathcal R_k,\mathcal O_k,\Theta_k),
\qquad k\in\{0,1\}.
\]

さらに比較のため、少なくとも該当するものを明示する。

- formula / signature translation \(T_{\mathcal L}:\mathcal L_0\to\mathcal L_1\)
- state embedding \(i:X_0\to X_1\)
- forgetful / observation map \(p:X_1\to X_0\)
- relation or rule simulation
- observable translation \(T_{\mathcal O}\)
- equivalence / behavioral equivalence
- preservation / reflection direction
- admissible class of alternative constructions

\(\Sigma_0\neq\Sigma_1\) だけでは generation claim を支えない。bijective renaming でも tuple の文字列は変わる。

## 3. “Newly available” must be typed

「新しい \(B\) が利用可能になった」を一種類にしない。

| Candidate change | Standard reading to test first | Minimum identity question |
|---|---|---|
| state transition | transition system / dynamics | same state space and variables? |
| coordinate change | isomorphism / change of coordinates | inverse exists and structure preserved? |
| renaming | signature isomorphism | only names changed? |
| representation change | encoding / translation | information and operations recoverable? |
| definitional extension | explicit definition / elimination | old-language consequences unchanged? |
| conservative extension | conservativity over old language | new theorems only in expanded language? |
| genuine strengthening | added axiom/rule | which old-language consequences increase? |
| new observable | function added or newly definable | independent of old observables? |
| new distinction | observation map has finer fibers | was it already definable? |
| new relation | relation state update or signature extension | relation instance or relation symbol? |
| new degree of freedom | larger independent variation space | independent relative to which constraints/map? |
| new ordering | relation update or derived transitive closure | primitive, generated, or defined? |
| new topology / metric | structure added or constructed | uniquely determined from old data? |
| new object class | inductive formation / universe extension | conservative coding available? |
| new admissible law space | meta-rule changes allowed rules | what fixes the meta-language and admissibility? |

## 4. Four questions before using “generation”

### 4.1 Is it an ordinary state transition?

If configurations already include a graph \(g\), a rewrite

\[
g\Rightarrow g'
\]

can add nodes and edges without changing the transition system’s signature or rule language. The object grows, but the specification can remain fixed. Calling this generation may be useful prose, but it does not establish a distinct equation type.

### 4.2 Is it a redescription?

For a bijection \(r:X_0\to X_1\) that transports all relevant structure, the apparent change may be an isomorphic presentation. Literal syntax changes; modeled possibilities need not.

### 4.3 Is it a definitional extension?

Adding a symbol \(d\) with explicit definition

\[
d(\bar x)\leftrightarrow\psi(\bar x)
\]

can make a relation directly nameable without adding old-language consequences or independent model choices. New vocabulary is not automatically new freedom.

### 4.4 Is it a substantive extension relative to a fixed comparison?

A target can allow multiple expansions above one source state:

\[
p^{-1}(x)=\{x'_1,x'_2,\ldots\}.
\]

If these alternatives are distinguishable by target observables and are not fixed by definitions from \(x\), this supports an **increase in independent specification choices relative to \(p\)**. It does not by itself support ontological generation or a physical mechanism.

## 5. Claim forms

### 5.1 Constructive route claim

\[
\exists G\in\mathcal G_{\mathrm{adm}}\;[G(\Sigma_0)\models B].
\]

One explicit, valid construction can suffice, after \(\mathcal G_{\mathrm{adm}}\), \(\Sigma_0\), target identity, and satisfaction relation are fixed.

### 5.2 Route failure

\[
\neg [G_0(\Sigma_0)\models B].
\]

This is about one \(G_0\), not all admissible routes.

### 5.3 Impossibility claim

\[
\forall G\in\mathcal G_{\mathrm{adm}}\;
\neg [G(\Sigma_0)\models B].
\]

This universal negative requires an exhaustive argument, invariant / obstruction theorem, undecidability result with exact scope, or equivalent evidence. A failed program run is insufficient.

### 5.4 Route necessity versus general necessity

\[
K\text{ is required by }G_0
\]

and

\[
\forall G\in\mathcal G_{\mathrm{adm}},\;
G(\Sigma_0)\models B\Rightarrow G\text{ uses or presupposes }K
\]

are different claims. The second requires a fixed notion of “uses or presupposes” and quantification over a specified construction class.

### 5.5 Non-redescription claim

To claim that \(\Sigma_1\) is not merely a redescription of \(\Sigma_0\), first select the relation being denied:

- no signature isomorphism;
- no definitional equivalence;
- no conservative elimination translation;
- no interpretation preserving specified observations;
- no behavioral equivalence under a chosen observation class.

Failure under one equivalence does not imply failure under all.

## 6. The G0–G5 proposal under stress

Proposed checklist:

- G0: renaming / representation change
- G1: definitional extension
- G2: new accessible relation / observable
- G3: new state distinction / degree of freedom
- G4: new ordering / topology / metric / object class
- G5: later law-space itself becomes available

### Initial result

This is **not retained as a hierarchy**.

- A G2 observable can be introduced by a G1 explicit definition.
- A G4 order can be the transitive closure of an already present relation.
- A G4 metric can be the shortest-path construction on already weighted graph data.
- A G3 independent coordinate can be encoded into a fixed larger state space, making it an ordinary state transition under another presentation.
- A G5 rule-space can be represented as data inside a higher-order but fixed transition system.

Thus “higher number” does not imply stronger generation. The list remains useful only as a **false-positive checklist** until a comparison relation is fixed.

## 7. Five-way diagnostic split

The minimal three-way warning is:

\[
\text{this route fails}
\neq
\text{the target cannot be constructed}
\neq
\text{the target/specification changed}.
\]

The toy tests require a slightly finer, test-local split:

1. **route failure:** this construction does not meet its own target;
2. **condition failure:** a required precondition for the route is absent;
3. **comparison underdetermination:** source / target map or equivalence has not been fixed;
4. **target-identity failure:** “the target” was weakened, renamed, or redefined;
5. **generation impossibility:** no admissible construction can meet the fixed target.

This is not proposed as a universal taxonomy. Its function is to prevent items 1–4 from being reported as item 5.

## 8. Metatime audit

Writing

\[
\Sigma_n\longrightarrow\Sigma_{n+1}
\]

introduces an index order. That order may be:

- derivation order in a formal proof;
- construction order in an algorithm;
- bookkeeping order in a log;
- externally parameterized physical time;
- an order relation claimed to emerge in the target.

These are not interchangeable. If physical time or causal order is part of the target, \(n\) can label the metalinguistic construction without being identified with generated time. The record must state this explicitly.

For that reason,

\[
\frac{d\Sigma}{dt}
\]

is not adopted as a base form for the methodology. It already requires a parameter \(t\), differentiability, and a space in which \(\Sigma\) varies. It may be appropriate for an evolving-state-space model after those structures are fixed.

## 9. “Law = convergence; generation = opening” control

Neither phrase is adopted as a definition.

- A law may enlarge support probabilistically, create trajectories from initial data, or leave the admissible set unchanged while assigning weights.
- A generative rule may reduce possibilities by selecting one extension.
- A definitional extension can increase available expressions while preserving old-language consequences.
- A quotient can reduce distinctions without being a convergence process.

The inclusions

\[
X_{\mathrm{allowed}}\subseteq X
\quad\text{and}\quad
\operatorname{Express}(\Sigma_0)
\subsetneq
\operatorname{Express}(\Sigma_1)
\]

may describe particular cases, but they neither classify every law nor establish ontological “opening.”

## 10. Initial disposition

- **DOWNGRADE:** \(G:\Sigma_0\rightsquigarrow\Sigma_1\) as a special generative equation. Use it only as a diagrammatic placeholder until replaced by an explicit standard map or rule.
- **RETAIN:** source / target / map / scope / direction / preservation record as an audit requirement.
- **KILL candidate:** \(\Sigma_0\neq\Sigma_1\) as a sufficient criterion for generation.
- **KILL candidate:** G0–G5 as an ordered scale.
- **OPEN:** whether a stable residual class remains after rewriting cases as transition systems, graph rewriting, definitional or conservative extensions, inductive formation, and evolving-state-space models.
- **NOT ESTABLISHED:** any VED-specific generative law or need for novel notation.

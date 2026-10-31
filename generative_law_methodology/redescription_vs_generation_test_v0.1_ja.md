# Redescription vs generation test v0.1

> Status:
> - exploratory stress test
> - not a theorem
> - not a generative hierarchy
> - not a model of VED
> - hand-checkable finite controls

## 1. Test question

> specification の見かけ上の変更から、renaming、definitional extension、ordinary state transition、independent structural enlargement を区別できるか。

各 model は source、target、map / construction、claim、evidence burden、alternative explanation、verdict、limit を記録する。これらは例示であり、全 generation claims の分類ではない。

## 2. Preregistered labels under test

- G0: renaming / representation change
- G1: definitional extension
- G2: new accessible relation / observable
- G3: new state distinction / degree of freedom
- G4: new ordering / topology / metric / object class
- G5: later law-space itself becomes available

**Preregistered kill condition:** labels が comparison map や definition policy の変更で順序を横断するなら、ordered hierarchy としては KILL / DOWNGRADE する。

## 3. Toy A — bijective renaming

### Source and target

\[
\mathcal L_0=\{p,\neg,\land\},
\qquad
\mathcal L_1=\{q,\neg,\land\}.
\]

Define the bijection \(\rho(p)=q\), extended compositionally:

\[
\rho(\neg\varphi)=\neg\rho(\varphi),
\qquad
\rho(\varphi\land\psi)=\rho(\varphi)\land\rho(\psi).
\]

Valuations are transported by \(v_1(q)=v_0(p)\).

### Claim and evidence

For all formulas \(\varphi\),

\[
v_0\models\varphi
\iff
v_1\models\rho(\varphi).
\]

This follows by structural induction on \(\varphi\).

### Alternative explanation

The literal expressions differ, but the language and valuation structures are isomorphic under \(\rho\).

### Verdict

**CONTROL: REDESCRIPTION.** No new truth assignment, distinction, or degree of freedom has been shown.

### Limit

This excludes only pure bijective renaming. Non-bijective encoding requires separate analysis.

## 4. Toy B — explicit definitional extension

### Source and target

Let \(\mathcal L_0\) be classical propositional logic containing \(p\). Extend it with a fresh propositional symbol \(q\):

\[
\mathcal L_1=\mathcal L_0\cup\{q\},
\qquad
q\leftrightarrow\neg p.
\]

Every valuation \(v_0\) of \(\mathcal L_0\) has a unique expansion \(v_1\) satisfying the definition, namely \(v_1(q)=1-v_0(p)\).

### Claim and evidence

The target language can directly express \(q\), but for every old-language formula \(\varphi\),

\[
\Gamma,q\leftrightarrow\neg p\vdash_{\mathcal L_1}\varphi
\quad\Rightarrow\quad
\Gamma\vdash_{\mathcal L_0}\varphi.
\]

Semantically, any source valuation extends to a target valuation satisfying the definition; completeness then yields old-language conservativity in the fixed classical calculus.

### Alternative explanation

The “new observable” \(q\) is entirely determined by an old observable. It is a new name and syntactic access point, not an independent assignment.

### Verdict

**G1 AND APPARENT G2 COLLAPSE.** A newly accessible observable can be a definitional extension. Therefore G1 and G2 are not disjoint without an independence criterion.

### Limit

This does not imply every new observable is definable from old ones.

## 5. Toy C — state-space enlargement

### Source and target

\[
X_0=\{0,1\},
\qquad
X_1=X_0\times\{0,1\}.
\]

Use the embedding and forgetful map

\[
i(x)=(x,0),
\qquad
p(x,u)=x.
\]

The target observable \(U(x,u)=u\) distinguishes \((x,0)\) from \((x,1)\), while \(p\) forgets that distinction.

### Claim and evidence

For each \(x\in X_0\),

\[
|p^{-1}(x)|=2.
\]

Thus the target has an additional independently variable binary coordinate **relative to \(p\) and the declared target observables**.

### Alternative explanation

The coordinate was externally stipulated by defining \(X_1\). No endogenous construction from source data was provided. A fixed universal state space could encode both source and target as subsets, turning the event into an ordinary transition.

### Verdict

**STRUCTURAL ENLARGEMENT RELATIVE TO A FIXED FORGETFUL MAP; NOT YET A GENERATIVE MECHANISM.**

### Limit

Fiber cardinality alone can count redundant parameterizations. Behavioral or observational equivalence must also be fixed.

## 6. Toy D — relation-instance creation

### Source and target

Let \(V=\{a,b\}\) and take states to be directed-edge sets:

\[
X=\mathcal P(V\times V).
\]

Define a transition rule

\[
E\Rightarrow E\cup\{(a,b)\}.
\]

From \(E_0=\varnothing\), it produces \(E_1=\{(a,b)\}\).

### Claim and evidence

The relation instance \(aRb\) is false in \(E_0\) and true in \(E_1\). The explicit rewrite witnesses the change.

### Alternative explanation

The relation symbol, node set, state space, and rewrite rule were all already present. This is an ordinary transition in a fixed graph-state space.

### Verdict

**RELATION CREATION AS STATE CHANGE.** “A new relation holds” does not imply a new relation type or new specification.

### Limit

If a new relation symbol and interpretation rule are introduced, that is a different claim requiring language-extension analysis.

## 7. Toy E — ordering by transitive closure

### Source and target

Let \(X=\{a,b,c\}\) and

\[
E=\{(a,b),(b,c)\}.
\]

Define

\[
x\preceq_E y
\quad\Longleftrightarrow\quad
x=y\ \text{or there is a directed \(E\)-path from \(x\) to \(y\)}.
\]

Because \(E\) is acyclic, \(\preceq_E\) is a partial order.

### Claim and evidence

Reflexivity is added by the \(x=y\) clause; transitivity follows by path concatenation; antisymmetry follows from acyclicity.

### Alternative explanation

The order is explicitly definable from \(E\). If \(E\) was already part of source data, no independent ordering choice was added.

### Verdict

**APPARENT G4 CAN BE G1.** “An order became available” can be a definitional construction, not a new degree of freedom.

### Limit

If \(E\) itself changes by a rule, there is a substantive relation-state update; whether that update is called generation remains a separate claim.

## 8. Toy F — metricization of a weighted graph

### Source and target

Let \(G=(V,E,w)\) be a finite connected undirected graph with strictly positive edge weights. Define

\[
d_G(x,y)=
\min_{\gamma:x\leadsto y}
\sum_{e\in\gamma}w(e).
\]

### Claim and evidence

\(d_G\) is nonnegative, symmetric, zero only on the diagonal, and satisfies the triangle inequality by path concatenation. Thus it is a metric.

### Alternative explanation

The metric is constructed from already supplied adjacency and weight data. It is not an additional independent field. If zero-weight edges are allowed, the same formula can yield only a pseudometric.

### Verdict

**METRIC AVAILABILITY DOES NOT BY ITSELF SHOW METRIC GENERATION AS AN INDEPENDENT STRUCTURE.** This is a standard construction whose status depends on whether \(E,w\) were already available and on what “new” means.

### Limit

The construction does not establish a continuum metric, unique coarse-graining, physical distance, or empirical adequacy.

## 9. Toy G — route failure versus impossibility

### Source and target

Let \(V=\{a,b,c\}\). Target \(B\) is:

\[
B:\quad c\text{ is reachable from }a.
\]

Route \(G_0\) attempts to add the direct edge \((a,c)\), but a local rule forbids it. Route \(G_1\) adds \((a,b)\) and \((b,c)\).

### Claim and evidence

\(G_0\) fails its direct-edge construction. In the graph produced by \(G_1\), the path \(a\to b\to c\) witnesses the unchanged target \(B\).

### Alternative explanation

No alternative explanation is needed: this is a direct control showing different routes to the same target.

### Verdict

\[
\text{this construction fails}
\not\Rightarrow
\text{the fixed target is impossible}.
\]

### Limit

If the target were changed from reachability to “the literal edge \((a,c)\) exists,” \(G_1\) would not be an alternative route. Target identity must be fixed.

## 10. Toy H — specification-change false positive

### Source and target

Source has two observational states \(a,b\). Extend the token set with \(c\), but define

\[
c\sim a
\]

under every allowed observation and transition. The quotient therefore remains

\[
\{[a],[b]\}.
\]

### Claim and evidence

Literal token count rises from two to three, but the number of observational equivalence classes remains two.

### Alternative explanation

The new token is an alias. If the target is silently changed from “three distinguishable states” to “three syntactic tokens,” apparent success comes from target migration.

### Verdict

**FALSE POSITIVE CONTROL.** New symbols or carrier elements need not create new distinctions.

### Limit

This is relative to the fixed observational equivalence. A later operation that distinguishes \(a\) and \(c\) would change the result.

## 11. Primary comparison table

| Toy | Source specification | Target / map | Candidate claim | Alternative explanation | Verdict |
|---|---|---|---|---|---|
| A | propositional signature with \(p\) | bijective rename \(\rho(p)=q\) | new symbol | isomorphic syntax | redescription |
| B | old propositional language | explicit \(q\leftrightarrow\neg p\) | new observable | definitional extension | G1/G2 not separated |
| C | \(X_0=\{0,1\}\) | \(X_1=X_0\times\{0,1\}\), projection \(p\) | new freedom | externally stipulated extension | structural enlargement relative to \(p\) |
| D | relation-valued graph states | edge-add rewrite | new relation | ordinary state transition | relation instance only |
| E | set plus acyclic relation \(E\) | reflexive transitive closure | new ordering | definitional construction | G4 can reduce to G1 |
| F | positive weighted graph | shortest-path metric | new metric | derived structure | metricization, not independent freedom |
| G | graph rewrite rules | two routes to same reachability target | route necessary | alternate route | route failure only |
| H | two observable states | add alias \(c\sim a\) | new state | target redefinition / syntax | false positive |

## 12. G0–G5 verdict

### Questions

- **Can G1 and G2 be separated without an independence criterion?** No. Toy B is an explicit countercontrol.
- **Can definitional extension look like a new observable?** Yes.
- **Does conservative extension separate every genuine generation claim?** No. It separates old-language consequence growth, not all state-space, dynamical, or ontological claims.
- **Can language change manufacture artificial generation?** Yes. Toys A, B, and H show three mechanisms.
- **Does expressive-power increase establish ontological generation?** No.
- **Do G3/G4 always outrank G1/G2?** No. Toys E and F reduce apparent G4 structure to standard definitions over supplied data.

### Disposition

- **KILL as hierarchy:** G0–G5 does not provide a stable ordering of strength.
- **DOWNGRADE as checklist:** the labels remain useful for asking which kind of “new” is being claimed.
- **RETAIN:** explicit source / target / map / observation / equivalence records.
- **NOT ESTABLISHED:** a residual generative-equation class distinct from existing mathematical descriptions.

## 13. Why no checker was added

The finite claims in Toys A–H are transparent enough for hand verification. A script could count fibers, paths, or truth tables but would not establish the general distinctions being tested. Code will be added only when a future finite search or equivalence classification creates a genuine risk of manual error.

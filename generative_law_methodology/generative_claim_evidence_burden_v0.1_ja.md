# Generative claim evidence burden v0.1

> Status:
> - exploratory audit table
> - not a theorem
> - not a complete logic of generation
> - standard evidence forms preferred
> - negative results retained

## 1. Governing rule

> Match the form of evidence to the logical form of the generative claim.

This rule is inherited from the completed [theorem / proof anatomy experimental record](../notes/theorem_proof_anatomy_experiment/07_audit_and_closure/theorem_proof_anatomy_experiment_final_record_v1.0_ja.md#101-中心-artifact-evidence-burden-table), not its retired terminology.

For every row below, source specification \(\Sigma_0\), target specification \(\Sigma_1\), comparison map / translation, target \(B\), scope, and admissible construction class must be fixed before evaluation.

## 2. Main table

| ID | Claim | Logical burden | Sufficient evidence candidate | Insufficient evidence | Current status |
|---|---|---|---|---|---|
| A | this specified route generates \(B\) | existential / witness validation | explicit construction, formal derivation, or executable model plus proof that output meets the fixed target | suggestive trajectory; target redefinition; visual similarity | ordinary constructive claim |
| B | this specified route fails | negation about one construction | show a stated step, precondition, invariant, or target condition fails for that route | failure to find an implementation; failure of another route | ordinary route failure |
| C | \(B\) cannot be generated from \(A\) | universal negative over admissible routes | obstruction / impossibility theorem, exhaustive finite enumeration with scope proof, reduction, invariant violated by every admissible route | one failed route; finite search without completeness; absence of current method | strong claim; usually OPEN |
| D1 | \(K\) is necessary for this route | counterfactual about fixed route | remove \(K\) while fixing other route data and prove this construction cannot close or meet target | showing \(K\) occurs in the written route | route-relative necessity |
| D2 | \(K\) is necessary for any generation of \(B\) | universal quantification over routes | theorem that every admissible construction requires \(K\), or countermodel / invariant separating all \(K\)-free constructions | D1; intersection of a few known routes | much stronger; NOT ESTABLISHED by route audit |
| E | \(K\) is sufficient | existential implication with fixed conditions | explicit construction or theorem deriving target from \(K\) plus all declared side conditions | correlation; \(K\) appears before \(B\); successful example with hidden assumptions | side conditions must be listed |
| F | \(B\) is not mere redescription | negation relative to chosen equivalence | fix isomorphism / definitional equivalence / conservativity / interpretability / behavioral equivalence and prove no such comparison exists, or exhibit separated invariant | different notation; failed identity map; intuition of novelty | relation-relative only |
| G | a new degree of freedom was generated | independence / fiber claim | fixed forgetful map \(p:X_1\to X_0\), multiple target states over one source state, independent target observables, and proof that alternatives are not definitionally fixed | new symbol; higher coordinate count; redundant parameterization | supports structural freedom, not ontology |
| H | generation is irreversible | nonexistence of inverse under chosen category/equivalence | prove no inverse / section / reconstruction map satisfying stated equations exists; if physical irreversibility is claimed, add dynamical and empirical evidence | absence of a literal inverse; many-to-one encoding alone; simulation hysteresis | distinguish mathematical, informational, physical senses |
| I | the generation route is unique | uniqueness modulo fixed equality | quantify over all admissible \(G'\) and prove \(G'\sim G\), or exhaustive finite classification | one successful route; deterministic implementation | equality and route class required |
| J | the generative law is universal | universal claim over a domain/class | theorem with explicit domain and assumptions, or appropriately broad empirical validation for an empirical law | finite toy models; selected VED examples; repeated simulation under one model family | no finite-pilot promotion |

## 3. Claim-by-claim controls

### A. Specified success

An executable model can show

\[
\exists r\;[\operatorname{Run}(G,\Sigma_0,r)\land B(r)].
\]

It does not show that every run succeeds, that \(G\) is necessary, or that \(B\) could not be obtained by redescription. Code validates only the encoded model and target predicate.

### B. Specified failure

Distinguish:

- program / numerical failure;
- violation of a mathematical precondition;
- proof that the route cannot satisfy \(B\);
- target not reached within a finite run.

Only the third directly establishes route impossibility; the fourth may be time-bound non-observation.

### C. Universal impossibility

The quantifier domain \(\mathcal G_{\mathrm{adm}}\) is part of the claim. Narrowing it after a counterexample changes the statement. If no principled admissibility class is available, “cannot be generated” is under-specified rather than false.

### D. Necessity

Removing \(K\) and seeing failure provides evidence only if:

1. the target is unchanged;
2. the source / target specifications are otherwise fixed;
3. no hidden equivalent of \(K\) remains;
4. the claim is explicitly route-relative, or all alternatives are addressed.

One route’s dependency graph is not a theorem of universal necessity.

### E. Sufficiency

Sufficiency is always relative to background conditions:

\[
(\Theta\land K)\Rightarrow B.
\]

Reporting only \(K\Rightarrow B\) while using \(\Theta\) silently overstates the claim.

### F. Non-redescription

Potential tests use existing concepts:

- signature / structure isomorphism;
- definitional equivalence or explicit-definition elimination;
- conservativity over an old language;
- mutual interpretability;
- behavioral equivalence / bisimulation;
- observational equivalence relative to a declared observable set.

Passing one non-equivalence test only excludes that relation. It does not establish metaphysical novelty.

### G. New freedom

Coordinate count is representation-dependent. A stronger test fixes a forgetful map:

\[
p:X_1\to X_0.
\]

If a fiber \(p^{-1}(x)\) has distinguishable alternatives and target dynamics/observables can vary among them without changing \(x\), there is additional model freedom relative to \(p\). A redundant parameterization can have large fibers too, so an equivalence or identifiability check is also required.

### H. Irreversibility

At least four readings must remain distinct:

1. no literal inverse function;
2. no inverse up to a chosen equivalence;
3. information loss under a coarse-graining / quotient;
4. thermodynamic or physical irreversibility.

A many-to-one map proves no two-sided set-theoretic inverse, but may have sections on a subset and does not by itself prove a physical arrow of time.

### I. Uniqueness

Uniqueness is normally:

\[
\forall G'\in\mathcal G_{\mathrm{adm}},
\quad B(G')\Rightarrow G'\sim G.
\]

Both \(\mathcal G_{\mathrm{adm}}\) and \(\sim\) must be fixed. Determinism of one algorithm does not prove uniqueness among algorithms.

### J. Universality

“Works in all tested models” and “works for every model in class \(\mathcal C\)” have different logical forms. Finite testing can refute a universal statement with a counterexample but generally cannot prove the universal statement without a completeness theorem connecting the test set to \(\mathcal C\).

## 4. Required failure split

| Diagnostic | What is established | What is not established |
|---|---|---|
| route failure | named construction fails | target impossible |
| condition failure | a route precondition is absent | all alternative conditions fail |
| comparison underdetermination | claim lacks map/equality/scope | claim is false |
| target identity failure | target was changed or redefined | original target was generated or refuted |
| specification migration | source/target setting changed | theorem-like failure inside the old setting |
| generation impossibility | all fixed admissible routes fail | claims outside the quantified class |

The first five can explain an observed failure without establishing the sixth.

## 5. Evidence ledger template

Every future test should record:

| Field | Required content |
|---|---|
| Claim | exact sentence and symbolic form where useful |
| Quantifiers | existential, universal, uniqueness, implication |
| Source | language, objects, operations, background |
| Target | same fields; target identity |
| Comparison | map, translation, equivalence, observation class |
| Route class | one route or all admissible routes |
| Evidence | construction, proof, countermodel, simulation, measurement |
| What evidence establishes | narrow supported conclusion |
| What it does not establish | prohibited inference |
| Verdict | RETAIN / REVISE / DOWNGRADE / KILL / OPEN / NOT ESTABLISHED |

## 6. Current negative result

There is no single evidence type called “evidence of generation.” A construction supports existence; an obstruction can support impossibility; conservativity or equivalence addresses redescription; fiber / identifiability analysis addresses independent freedom; inverse analysis addresses one selected sense of irreversibility. Combining these claims under one verb hides rather than reduces the burden.

# Toy models

> Status: initial hand-checkable controls only; no general theorem and no VED model.

The first eight controls are recorded in [redescription vs generation test](../redescription_vs_generation_test_v0.1_ja.md):

- bijective renaming;
- explicit definitional extension;
- product state-space enlargement;
- relation-instance creation;
- ordering by transitive closure;
- metricization of a weighted graph;
- route failure with an alternate construction;
- specification-change false positive by aliasing.

No checker is stored for this initial Toy A–H suite. Those claims are simpler to inspect by hand than through an implementation. The subsequent [observable-independence stress test](../stress_tests/observable_independence_finite_model_v0.1_ja.md) does include a checker because it exhaustively classifies raw and observational quotient fibers. Neither choice substitutes code for a general theorem.

Every future toy model must include:

1. source specification;
2. target specification;
3. map / construction;
4. exact claim and quantifiers;
5. evidence burden;
6. alternative explanation;
7. verdict;
8. limitation.

Finite output must not be promoted to a universal generative-law claim.

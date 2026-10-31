# Stress tests

> Status: five finite tests and the cross-test synthesis are complete; Phase 4 closed with STOP-A.

## Completed

- [Observable independence finite-model stress test](./observable_independence_finite_model_v0.1_ja.md)
- [Companion checker](./observable_independence_finite_model_v0.1.py)
- [Graph-growth dual-encoding stress test](./graph_growth_dual_encoding_v0.1_ja.md)
- [Graph-growth companion checker](./graph_growth_dual_encoding_v0.1.py)
- [Construction versus internal order stress test](./construction_vs_internal_order_v0.1_ja.md)
- [Order-model companion checker](./construction_vs_internal_order_v0.1.py)
- [Relation-to-metric boundary stress test](./relation_to_metric_boundary_v0.1_ja.md)
- [Metric-boundary companion checker](./relation_to_metric_boundary_v0.1.py)
- [Rule-space-as-data stress test](./rule_space_as_data_v0.1_ja.md)
- [Rule-space companion checker](./rule_space_as_data_v0.1.py)

## Synthesis and stopping

- [Phase 4 cross-test synthesis / stopping audit](../phase4_cross_test_synthesis_v0.1_ja.md)
- [Final experimental record v1.0](../generative_law_methodology_final_record_v1.0_ja.md)

The synthesis found no repeated non-reducible residual requiring special
generative notation. It selected **STOP-A / STOP AND SYNTHESIZE AS AUDIT
METHODOLOGY**. Phase 5 is not entered, and VED reconstruction is not performed
by this branch closure. The final record preserves these results without adding
a new experiment or notation.

The observable checker exhausts six encoded Boolean cases. It verifies raw and
quotient fiber counts, functional dependence, map adequacy, and selected
observation traces. The graph checker exhausts a bounded three-node growth
system and compares 13 reachable states, 20 transitions, selected predicates,
five histories, an isomorphism quotient, and preload observability. The order
checker exhausts all 24 permutations of four events, isolates two linear
extensions of one partial order, and tests history-sensitive and timestamp
controls. The metric checker audits positive, zero, disconnected, directed,
negative, unweighted, transformed, and coarse-grained finite distance cases.
The rule-space checker compares explicit rule changes with a fixed interpreter,
and tests active subsets, parameters, aliases, compositions, stage-local
availability, type arity, bounded history, stochastic updates, and one finite
meta-rule lift.
None of these checkers proves generation, ontology, physical emergence,
physical time or space, new-law creation, or a universal criterion.

## Order of work

1. **Definable versus independent observable — COMPLETE:** unique definitional expansions, redundant fibers, distinguishable expansions, map choice, hidden-source, and uncoupled-coordinate controls.
2. **Graph growth under two encodings — COMPLETE:** fixed graph-state transition versus changing carrier specification.
3. **Construction order versus internal order — COMPLETE:** permute independent steps and audit stage-label dependence.
4. **Metric construction boundary cases — COMPLETE:** positive, zero, asymmetric, disconnected, negative, transformed, and coarse-grained relations.
5. **Rule-space-as-data — COMPLETE:** compare fixed higher-order rules with literal operational-rule changes.

The completed synthesis treats preloaded syntax, types, interpreters, candidate
repertoires, and observation policies as specification facts, not as evidence
for a distinct equation or physical foreknowledge.

## Kill controls

- If all supposed structural changes translate without loss into ordinary rewriting or model expansion, special generative notation is retired.
- If classification changes solely with representation boundary and no fixed comparison restores it, the classification is killed as a general distinction.
- If a test only shows one route failure, it must not be reported as impossibility.
- If a “new observable” is explicitly definable, it does not count as independent freedom.
- If stage order is used as physical time without an independent identification, the temporal-generation claim fails this test.

## Evidence policy

Use [the evidence-burden table](../generative_claim_evidence_burden_v0.1_ja.md). Each stress test must record both what its evidence establishes and what it does not establish.

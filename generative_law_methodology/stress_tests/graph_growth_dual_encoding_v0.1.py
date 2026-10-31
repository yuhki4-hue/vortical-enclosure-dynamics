#!/usr/bin/env python3
"""Finite checks for two encodings of the same bounded graph-growth process.

This checker verifies combinatorial claims only for the encoded universe
U = {a, b, c}.  It does not establish generation, ontology, physical
emergence, or a universal reduction of changing-carrier descriptions to
fixed-state dynamics.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations
from typing import Callable, Iterable, Optional


Node = str
Edge = tuple[Node, Node]
Truth = Optional[bool]

UNIVERSE: tuple[Node, ...] = ("a", "b", "c")
ROOT: Node = "a"
ALLOWED_EDGES: frozenset[Edge] = frozenset(
    {("a", "b"), ("a", "c"), ("b", "c")}
)


@dataclass(frozen=True)
class Graph:
    """Encoding A state: active subgraph of a fixed, predeclared universe."""

    nodes: frozenset[Node]
    edges: frozenset[Edge]

    def __post_init__(self) -> None:
        if ROOT not in self.nodes:
            raise ValueError("the root a must remain active")
        if not self.nodes <= frozenset(UNIVERSE):
            raise ValueError("node outside the fixed universe")
        if not self.edges <= ALLOWED_EDGES:
            raise ValueError("edge outside the allowed edge set")
        if any(u not in self.nodes or v not in self.nodes for u, v in self.edges):
            raise ValueError("edge endpoint is inactive")


@dataclass(frozen=True)
class BRecord:
    """Encoding B record: current carrier and its stage-local constants."""

    constants: frozenset[Node]
    nodes: frozenset[Node]
    edges: frozenset[Edge]

    def __post_init__(self) -> None:
        if self.constants != self.nodes:
            raise ValueError("canonical B records name exactly the current carrier")
        Graph(self.nodes, self.edges)


G0 = Graph(frozenset({ROOT}), frozenset())


def subsets(items: Iterable[Node]) -> Iterable[frozenset[Node]]:
    values = tuple(items)
    for size in range(len(values) + 1):
        for chosen in combinations(values, size):
            yield frozenset(chosen)


def graph_key(graph: Graph) -> tuple[tuple[Node, ...], tuple[Edge, ...]]:
    return tuple(sorted(graph.nodes)), tuple(sorted(graph.edges))


def all_admissible_graphs() -> frozenset[Graph]:
    graphs: set[Graph] = set()
    for optional_nodes in subsets(n for n in UNIVERSE if n != ROOT):
        nodes = frozenset({ROOT}) | optional_nodes
        available_edges = sorted(
            edge for edge in ALLOWED_EDGES if set(edge) <= nodes
        )
        for edges in subsets(available_edges):
            graphs.add(Graph(nodes, frozenset(edges)))
    return frozenset(graphs)


def successors_a(graph: Graph) -> frozenset[Graph]:
    """Activate one fresh node, or add one allowed edge between active nodes."""

    successors: set[Graph] = set()
    for node in frozenset(UNIVERSE) - graph.nodes:
        successors.add(Graph(graph.nodes | {node}, graph.edges))
    for edge in ALLOWED_EDGES - graph.edges:
        if set(edge) <= graph.nodes:
            successors.add(Graph(graph.nodes, graph.edges | {edge}))
    return frozenset(successors)


def to_b(graph: Graph) -> BRecord:
    return BRecord(graph.nodes, graph.nodes, graph.edges)


def from_b(record: BRecord) -> Graph:
    return Graph(record.nodes, record.edges)


def successors_b(record: BRecord) -> frozenset[BRecord]:
    """Extend the current carrier, or add an edge within it."""

    return frozenset(to_b(graph) for graph in successors_a(from_b(record)))


def reachable(
    initial: object, successor: Callable[[object], Iterable[object]]
) -> frozenset[object]:
    seen = {initial}
    frontier = [initial]
    while frontier:
        current = frontier.pop()
        for nxt in successor(current):
            if nxt not in seen:
                seen.add(nxt)
                frontier.append(nxt)
    return frozenset(seen)


def transition_relation_a(states: Iterable[Graph]) -> frozenset[tuple[Graph, Graph]]:
    state_set = frozenset(states)
    return frozenset(
        (state, nxt)
        for state in state_set
        for nxt in successors_a(state)
        if nxt in state_set
    )


def transition_relation_b(
    states: Iterable[BRecord],
) -> frozenset[tuple[BRecord, BRecord]]:
    state_set = frozenset(states)
    return frozenset(
        (state, nxt)
        for state in state_set
        for nxt in successors_b(state)
        if nxt in state_set
    )


def has_directed_path(graph: Graph, source: Node, target: Node) -> Truth:
    """Stage-local predicate: undefined if either name is outside the carrier."""

    if source not in graph.nodes or target not in graph.nodes:
        return None
    seen = {source}
    frontier = [source]
    while frontier:
        current = frontier.pop()
        if current == target:
            return True
        for u, v in graph.edges:
            if u == current and v not in seen:
                seen.add(v)
                frontier.append(v)
    return False


def is_connected(graph: Graph) -> bool:
    """Connectedness of the underlying undirected active graph."""

    seen = {ROOT}
    frontier = [ROOT]
    while frontier:
        current = frontier.pop()
        for u, v in graph.edges:
            if u == current and v not in seen:
                seen.add(v)
                frontier.append(v)
            if v == current and u not in seen:
                seen.add(u)
                frontier.append(u)
    return seen == set(graph.nodes)


def predicate_vector(graph: Graph) -> tuple[bool, Truth, bool]:
    return len(graph.nodes) == 3, has_directed_path(graph, "a", "c"), is_connected(graph)


def is_subgraph_of(candidate: Graph, target: Graph) -> bool:
    return candidate.nodes <= target.nodes and candidate.edges <= target.edges


def histories_to(target: Graph) -> tuple[tuple[Graph, ...], ...]:
    """Enumerate monotone paths that do not add material absent from target."""

    paths: list[tuple[Graph, ...]] = []

    def visit(current: Graph, path: tuple[Graph, ...]) -> None:
        if current == target:
            paths.append(path)
            return
        for nxt in sorted(successors_a(current), key=graph_key):
            if is_subgraph_of(nxt, target):
                visit(nxt, path + (nxt,))

    visit(G0, (G0,))
    return tuple(paths)


def introduction_step(path: tuple[Graph, ...], node: Node) -> int:
    for step, graph in enumerate(path):
        if node in graph.nodes:
            return step
    raise ValueError(f"node {node} never appears")


def rooted_isomorphism_signature(graph: Graph) -> tuple[int, str]:
    """Canonical directed-graph signature under permutations fixing root a."""

    other_nodes = sorted(graph.nodes - {ROOT})
    encodings: list[str] = []
    for ordering in permutations(other_nodes):
        ordered = (ROOT,) + ordering
        index = {node: i for i, node in enumerate(ordered)}
        bits = []
        for i in range(len(ordered)):
            for j in range(len(ordered)):
                if i == j:
                    continue
                bits.append("1" if (ordered[i], ordered[j]) in graph.edges else "0")
        encodings.append("".join(bits))
    return len(graph.nodes), min(encodings)


def run_checks() -> dict[str, object]:
    admissible_a = all_admissible_graphs()
    reachable_a = frozenset(reachable(G0, successors_a))
    reachable_b = frozenset(reachable(to_b(G0), successors_b))

    assert reachable_a == admissible_a
    assert {to_b(graph) for graph in reachable_a} == reachable_b
    assert all(from_b(to_b(graph)) == graph for graph in reachable_a)
    assert all(to_b(from_b(record)) == record for record in reachable_b)

    transitions_a = transition_relation_a(reachable_a)
    transitions_b = transition_relation_b(reachable_b)
    assert {(to_b(left), to_b(right)) for left, right in transitions_a} == transitions_b

    for graph in reachable_a:
        assert predicate_vector(graph) == predicate_vector(from_b(to_b(graph)))

    final = Graph(
        frozenset({"a", "b", "c"}),
        frozenset({("a", "b"), ("b", "c")}),
    )
    histories_a = histories_to(final)
    histories_b = tuple(tuple(to_b(graph) for graph in path) for path in histories_a)
    assert len(histories_a) > 1
    assert {len(path) - 1 for path in histories_a} == {4}
    assert all(tuple(from_b(record) for record in path) in histories_a for path in histories_b)
    assert len({path[-1] for path in histories_a}) == 1

    intro_b = sorted({introduction_step(path, "b") for path in histories_a})
    intro_c = sorted({introduction_step(path, "c") for path in histories_a})

    quotient_signatures = {rooted_isomorphism_signature(graph) for graph in reachable_a}
    labeled_left = Graph(frozenset({"a", "b"}), frozenset({("a", "b")}))
    labeled_right = Graph(frozenset({"a", "c"}), frozenset({("a", "c")}))
    assert labeled_left != labeled_right
    assert rooted_isomorphism_signature(labeled_left) == rooted_isomorphism_signature(labeled_right)

    path_false = Graph(
        frozenset({"a", "b", "c"}), frozenset({("a", "b")})
    )
    path_true = Graph(
        frozenset({"a", "b", "c"}), frozenset({("a", "c")})
    )
    assert rooted_isomorphism_signature(path_false) == rooted_isomorphism_signature(path_true)
    assert has_directed_path(path_false, "a", "c") is False
    assert has_directed_path(path_true, "a", "c") is True

    initial_b = to_b(G0)
    inactive_c_a = "c" in set(UNIVERSE) - G0.nodes
    c_well_formed_b = "c" in initial_b.constants
    assert inactive_c_a is True
    assert c_well_formed_b is False

    restricted_a_view = (G0.nodes, G0.edges)
    active_b_view = (initial_b.nodes, initial_b.edges)
    assert restricted_a_view == active_b_view
    assert {to_b(graph) for graph in successors_a(G0)} == successors_b(initial_b)

    return {
        "admissible_a": len(admissible_a),
        "reachable_a": len(reachable_a),
        "reachable_b": len(reachable_b),
        "transition_pairs_a": len(transitions_a),
        "transition_pairs_b": len(transitions_b),
        "roundtrip_labeled": True,
        "predicate_preservation": True,
        "one_step_preservation": True,
        "histories_to_final": len(histories_a),
        "history_lengths": sorted({len(path) - 1 for path in histories_a}),
        "pathwise_history_preservation": True,
        "b_introduction_steps": intro_b,
        "c_introduction_steps": intro_c,
        "rooted_isomorphism_classes": len(quotient_signatures),
        "label_variants_collapse_under_isomorphism": True,
        "label_sensitive_predicate_not_quotient_invariant": True,
        "restricted_active_view_matches": True,
        "inactive_c_observable_in_a": inactive_c_a,
        "c_well_formed_in_initial_b": c_well_formed_b,
        "future_successors_preserved": True,
        "rules_fixed": True,
    }


def main() -> None:
    results = run_checks()
    print("graph growth dual encoding finite checker v0.1")
    for key, value in results.items():
        print(f"{key}={value}")
    print("all_assertions_passed=True")
    print(
        "scope=encoded finite labeled graph system only; no claim about "
        "generation, ontology, physical emergence, or universal reducibility"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Finite checks for shortest-path metric boundary conditions.

The checker verifies encoded finite graph and distance facts only.  It does
not establish physical space, metric emergence, geometry generation, or a
universal reduction from spatial structure to relation data.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import inf, isinf
from typing import Hashable, Iterable, Mapping, Optional, TypeVar


Node = TypeVar("Node", bound=Hashable)
DistanceMatrix = dict[tuple[Node, Node], float]


@dataclass(frozen=True)
class AxiomReport:
    finite_valued: bool
    nonnegative: bool
    zero_diagonal: bool
    identity_of_indiscernibles: bool
    symmetric: bool
    triangle: Optional[bool]

    @property
    def ordinary_metric(self) -> bool:
        return all(
            (
                self.finite_valued,
                self.nonnegative,
                self.zero_diagonal,
                self.identity_of_indiscernibles,
                self.symmetric,
                self.triangle is True,
            )
        )

    @property
    def pseudometric(self) -> bool:
        return all(
            (
                self.finite_valued,
                self.nonnegative,
                self.zero_diagonal,
                self.symmetric,
                self.triangle is True,
            )
        )

    @property
    def extended_metric(self) -> bool:
        return all(
            (
                self.nonnegative,
                self.zero_diagonal,
                self.identity_of_indiscernibles,
                self.symmetric,
                self.triangle is True,
            )
        )

    @property
    def quasi_metric(self) -> bool:
        return all(
            (
                self.finite_valued,
                self.nonnegative,
                self.zero_diagonal,
                self.identity_of_indiscernibles,
                self.triangle is True,
            )
        )


def directed_weights(
    weights: Mapping[tuple[Node, Node], float], *, undirected: bool
) -> dict[tuple[Node, Node], float]:
    result: dict[tuple[Node, Node], float] = {}
    for (left, right), weight in weights.items():
        result[left, right] = min(weight, result.get((left, right), inf))
        if undirected:
            result[right, left] = min(weight, result.get((right, left), inf))
    return result


def shortest_paths(
    nodes: Iterable[Node],
    weights: Mapping[tuple[Node, Node], float],
    *,
    undirected: bool,
) -> DistanceMatrix[Node]:
    """Floyd-Warshall distances with -inf propagation from negative cycles."""

    node_tuple = tuple(nodes)
    arcs = directed_weights(weights, undirected=undirected)
    distance: DistanceMatrix[Node] = {
        (left, right): (0.0 if left == right else inf)
        for left in node_tuple
        for right in node_tuple
    }
    for edge, weight in arcs.items():
        distance[edge] = min(distance[edge], float(weight))

    for middle in node_tuple:
        for left in node_tuple:
            for right in node_tuple:
                through = distance[left, middle] + distance[middle, right]
                if through < distance[left, right]:
                    distance[left, right] = through

    negative_cycle_nodes = [
        node for node in node_tuple if distance[node, node] < 0
    ]
    affected = {
        (left, right)
        for cycle_node in negative_cycle_nodes
        for left in node_tuple
        for right in node_tuple
        if distance[left, cycle_node] < inf and distance[cycle_node, right] < inf
    }
    for pair in affected:
        distance[pair] = -inf
    return distance


def axiom_report(nodes: Iterable[Node], distance: DistanceMatrix[Node]) -> AxiomReport:
    node_tuple = tuple(nodes)
    values = tuple(distance.values())
    has_negative_infinity = any(value == -inf for value in values)
    finite_valued = all(not isinf(value) for value in values)
    nonnegative = all(value >= 0 for value in values)
    zero_diagonal = all(distance[node, node] == 0 for node in node_tuple)
    identity = zero_diagonal and all(
        distance[left, right] != 0
        for left in node_tuple
        for right in node_tuple
        if left != right
    )
    symmetric = all(
        distance[left, right] == distance[right, left]
        for left in node_tuple
        for right in node_tuple
    )
    if has_negative_infinity:
        triangle: Optional[bool] = None
    else:
        triangle = all(
            distance[left, right]
            <= distance[left, middle] + distance[middle, right]
            for left in node_tuple
            for middle in node_tuple
            for right in node_tuple
        )
    return AxiomReport(
        finite_valued,
        nonnegative,
        zero_diagonal,
        identity,
        symmetric,
        triangle,
    )


def connected_components(nodes: Iterable[Node], distance: DistanceMatrix[Node]) -> tuple[frozenset[Node], ...]:
    remaining = set(nodes)
    components = []
    while remaining:
        start = next(iter(remaining))
        component = {
            node
            for node in remaining
            if distance[start, node] < inf and distance[node, start] < inf
        }
        components.append(frozenset(component))
        remaining -= component
    return tuple(components)


def zero_distance_classes(
    nodes: Iterable[Node], distance: DistanceMatrix[Node]
) -> tuple[frozenset[Node], ...]:
    remaining = set(nodes)
    classes = []
    while remaining:
        start = next(iter(remaining))
        equivalence_class = {
            node
            for node in remaining
            if distance[start, node] == 0 and distance[node, start] == 0
        }
        classes.append(frozenset(equivalence_class))
        remaining -= equivalence_class
    return tuple(classes)


def quotient_distance(
    classes: tuple[frozenset[Node], ...], distance: DistanceMatrix[Node]
) -> DistanceMatrix[int]:
    result: DistanceMatrix[int] = {}
    for left_index, left_class in enumerate(classes):
        for right_index, right_class in enumerate(classes):
            values = {
                distance[left, right]
                for left in left_class
                for right in right_class
            }
            assert len(values) == 1, "distance is not representative-independent"
            result[left_index, right_index] = next(iter(values))
    return result


def transform_distance(
    nodes: Iterable[Node],
    distance: DistanceMatrix[Node],
    transform,
) -> DistanceMatrix[Node]:
    return {
        (left, right): (0.0 if left == right else float(transform(value)))
        for (left, right), value in distance.items()
    }


def two_cluster_matrix(value: float) -> DistanceMatrix[str]:
    return {
        ("AB", "AB"): 0.0,
        ("C", "C"): 0.0,
        ("AB", "C"): value,
        ("C", "AB"): value,
    }


def report_dict(report: AxiomReport) -> dict[str, object]:
    return {
        "finite": report.finite_valued,
        "nonnegative": report.nonnegative,
        "zero_diagonal": report.zero_diagonal,
        "identity": report.identity_of_indiscernibles,
        "symmetric": report.symmetric,
        "triangle": report.triangle,
        "metric": report.ordinary_metric,
        "pseudometric": report.pseudometric,
        "extended_metric": report.extended_metric,
        "quasi_metric": report.quasi_metric,
    }


def run_checks() -> dict[str, object]:
    nodes = ("a", "b", "c")

    # Case A: positive, undirected, connected.
    case_a = shortest_paths(
        nodes,
        {("a", "b"): 2, ("b", "c"): 3, ("a", "c"): 10},
        undirected=True,
    )
    report_a = axiom_report(nodes, case_a)
    assert report_a.ordinary_metric
    assert case_a["a", "c"] == 5

    # Case B: zero edge produces a pseudometric; quotient repairs identity.
    case_b = shortest_paths(
        nodes,
        {("a", "b"): 0, ("b", "c"): 2, ("a", "c"): 5},
        undirected=True,
    )
    report_b = axiom_report(nodes, case_b)
    assert report_b.pseudometric
    assert not report_b.ordinary_metric
    assert case_b["a", "b"] == 0
    zero_classes = zero_distance_classes(nodes, case_b)
    assert {frozenset({"a", "b"}), frozenset({"c"})} == set(zero_classes)
    case_b_quotient = quotient_distance(zero_classes, case_b)
    report_b_quotient = axiom_report(range(len(zero_classes)), case_b_quotient)
    assert report_b_quotient.ordinary_metric

    # Case C: disconnected graph, with +inf policy.
    case_c = shortest_paths(nodes, {("a", "b"): 1}, undirected=True)
    report_c = axiom_report(nodes, case_c)
    assert not report_c.ordinary_metric
    assert report_c.extended_metric
    assert case_c["a", "c"] == inf
    components_c = connected_components(nodes, case_c)
    assert {frozenset({"a", "b"}), frozenset({"c"})} == set(components_c)
    unreachable_ordered_pairs = sum(
        1 for left in nodes for right in nodes if case_c[left, right] == inf
    )
    assert unreachable_ordered_pairs == 4

    # Case D: positive directed cycle; finite quasi-metric but asymmetric.
    case_d = shortest_paths(
        nodes,
        {("a", "b"): 1, ("b", "c"): 1, ("c", "a"): 1},
        undirected=False,
    )
    report_d = axiom_report(nodes, case_d)
    assert report_d.quasi_metric
    assert not report_d.symmetric
    assert not report_d.ordinary_metric
    assert case_d["a", "b"] == 1 and case_d["b", "a"] == 2

    # Case E1: a negative edge without a negative cycle.
    case_e1 = shortest_paths(
        nodes,
        {("a", "b"): -1, ("b", "c"): 2, ("c", "a"): 2},
        undirected=False,
    )
    report_e1 = axiom_report(nodes, case_e1)
    assert case_e1["a", "b"] == -1
    assert case_e1["a", "c"] == 1
    assert report_e1.finite_valued
    assert not report_e1.nonnegative
    assert report_e1.triangle is True
    assert all(value != -inf for value in case_e1.values())

    # Case E2: a reachable negative cycle makes affected infima -infinity.
    case_e2 = shortest_paths(
        nodes,
        {("a", "b"): 1, ("b", "c"): -3, ("c", "b"): 1},
        undirected=False,
    )
    report_e2 = axiom_report(nodes, case_e2)
    negative_infinite_pairs = sum(value == -inf for value in case_e2.values())
    assert negative_infinite_pairs == 6
    assert case_e2["a", "b"] == -inf
    assert case_e2["b", "b"] == -inf
    assert report_e2.triangle is None
    assert not report_e2.zero_diagonal

    # Case F: unweighted relation plus edge-count convention.
    unweighted_edges = {("a", "b"): 1, ("b", "c"): 1}
    case_f = shortest_paths(nodes, unweighted_edges, undirected=True)
    report_f = axiom_report(nodes, case_f)
    assert report_f.ordinary_metric
    assert case_f["a", "c"] == 2

    # Case G: same relation, two positive weightings, two metrics.
    case_g = shortest_paths(
        nodes,
        {("a", "b"): 2, ("b", "c"): 5},
        undirected=True,
    )
    report_g = axiom_report(nodes, case_g)
    assert report_g.ordinary_metric
    assert case_g["a", "c"] == 7
    assert case_f["a", "c"] != case_g["a", "c"]

    # Case H: transform controls on the edge-count metric.
    scaled = transform_distance(nodes, case_f, lambda value: 2 * value)
    shifted_off_diagonal = transform_distance(nodes, case_f, lambda value: value + 1)
    squared = transform_distance(nodes, case_f, lambda value: value**2)
    report_scaled = axiom_report(nodes, scaled)
    report_shifted = axiom_report(nodes, shifted_off_diagonal)
    report_squared = axiom_report(nodes, squared)
    assert report_scaled.ordinary_metric
    assert report_shifted.ordinary_metric
    assert not report_squared.ordinary_metric
    assert report_squared.triangle is False
    assert squared["a", "c"] == 4
    assert squared["a", "b"] + squared["b", "c"] == 2

    # Optional coarse-graining: q(a)=q(b)=AB, q(c)=C.
    intercluster_values = [case_f["a", "c"], case_f["b", "c"]]
    coarse_min = min(intercluster_values)
    coarse_average = sum(intercluster_values) / len(intercluster_values)
    coarse_representative = case_f["a", "c"]
    coarse_values = (coarse_min, coarse_average, coarse_representative)
    assert coarse_values == (1, 1.5, 2)
    assert len(set(coarse_values)) == 3
    assert all(
        axiom_report(("AB", "C"), two_cluster_matrix(value)).ordinary_metric
        for value in coarse_values
    )

    return {
        "case_a_positive_metric": report_dict(report_a),
        "case_a_d_a_c": case_a["a", "c"],
        "case_b_zero_weight": report_dict(report_b),
        "case_b_d_a_b": case_b["a", "b"],
        "case_b_zero_classes": sorted(sorted(group) for group in zero_classes),
        "case_b_quotient_metric": report_b_quotient.ordinary_metric,
        "case_c_disconnected": report_dict(report_c),
        "case_c_unreachable_ordered_pairs": unreachable_ordered_pairs,
        "case_c_components": sorted(sorted(group) for group in components_c),
        "case_d_directed": report_dict(report_d),
        "case_d_d_a_b_vs_b_a": [case_d["a", "b"], case_d["b", "a"]],
        "case_e1_negative_no_cycle": report_dict(report_e1),
        "case_e1_d_a_b_and_a_c": [case_e1["a", "b"], case_e1["a", "c"]],
        "case_e2_negative_cycle_minus_inf_pairs": negative_infinite_pairs,
        "case_e2_triangle_audit": report_e2.triangle,
        "case_f_unweighted_edge_count_metric": report_f.ordinary_metric,
        "case_f_d_a_c": case_f["a", "c"],
        "case_g_same_relation_second_metric": report_g.ordinary_metric,
        "case_g_d_a_c": case_g["a", "c"],
        "case_h_positive_rescaling_metric": report_scaled.ordinary_metric,
        "case_h_off_diagonal_shift_metric": report_shifted.ordinary_metric,
        "case_h_square_transform_triangle": report_squared.triangle,
        "coarse_policy_distances": list(coarse_values),
        "coarse_policy_metrics": True,
    }


def main() -> None:
    results = run_checks()
    print("relation to metric boundary finite checker v0.1")
    for key, value in results.items():
        print(f"{key}={value}")
    print("all_assertions_passed=True")
    print(
        "scope=encoded finite graph and distance facts only; no claim about "
        "physical space, metric emergence, geometry generation, or universal "
        "reduction"
    )


if __name__ == "__main__":
    main()

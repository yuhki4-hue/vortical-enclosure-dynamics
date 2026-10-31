#!/usr/bin/env python3
"""Finite checks separating construction order from an internal partial order.

The checker exhausts all permutations of four events and a finite timestamp
range.  It verifies only the encoded order-theoretic and combinatorial facts.
It does not establish physical time, causality, ontological generation, or a
universal account of temporal emergence.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from typing import Callable, Iterable


Event = str
Relation = frozenset[tuple[Event, Event]]
History = tuple[Event, ...]

EVENTS: tuple[Event, ...] = ("a", "b", "c", "d")
COVER_RELATION: Relation = frozenset({("a", "c"), ("b", "c"), ("c", "d")})
EVENT_WEIGHT: dict[Event, int] = {"a": 1, "b": 2, "c": 3, "d": 4}


def transitive_closure(events: Iterable[Event], relation: Relation) -> Relation:
    closure = set(relation)
    changed = True
    while changed:
        changed = False
        additions = {
            (left, right)
            for left, middle in closure
            for middle_again, right in closure
            if middle == middle_again and left != right and (left, right) not in closure
        }
        if additions:
            closure.update(additions)
            changed = True
    event_set = set(events)
    if any(left not in event_set or right not in event_set for left, right in closure):
        raise ValueError("relation contains an event outside the carrier")
    return frozenset(closure)


PRECEDENCE: Relation = transitive_closure(EVENTS, COVER_RELATION)


def assert_strict_partial_order(events: Iterable[Event], relation: Relation) -> None:
    event_set = set(events)
    assert all(left in event_set and right in event_set for left, right in relation)
    assert all(left != right for left, right in relation)
    assert all((right, left) not in relation for left, right in relation)
    for left, middle in relation:
        for middle_again, right in relation:
            if middle == middle_again:
                assert (left, right) in relation


def linear_order(history: History) -> Relation:
    return frozenset(
        (history[i], history[j])
        for i in range(len(history))
        for j in range(i + 1, len(history))
    )


def is_linear_extension(history: History, relation: Relation = PRECEDENCE) -> bool:
    if len(history) != len(EVENTS) or set(history) != set(EVENTS):
        return False
    position = {event: index for index, event in enumerate(history)}
    return all(position[left] < position[right] for left, right in relation)


def quotient_target(history: History) -> tuple[frozenset[Event], Relation]:
    """Q forgets linearization and returns the fixed pure-order target."""

    if not is_linear_extension(history):
        raise ValueError("Q is defined here only on valid construction histories")
    return frozenset(EVENTS), PRECEDENCE


def target_predicates(target: tuple[frozenset[Event], Relation]) -> tuple[bool, ...]:
    events, relation = target
    return (
        events == frozenset(EVENTS),
        ("a", "b") not in relation and ("b", "a") not in relation,
        ("a", "c") in relation and ("b", "c") in relation,
        ("c", "d") in relation,
        ("a", "d") in relation and ("b", "d") in relation,
    )


def path_dependent_cost(history: History) -> int:
    """A deliberately order-sensitive metadata control, not a physical law."""

    return sum(stage * EVENT_WEIGHT[event] for stage, event in enumerate(history, 1))


def timestamp_preserves_order(timestamp: dict[Event, int]) -> bool:
    return all(timestamp[left] < timestamp[right] for left, right in PRECEDENCE)


def construction_timestamp(history: History) -> dict[Event, int]:
    return {event: stage for stage, event in enumerate(history, 1)}


@dataclass(frozen=True)
class FixedState:
    """Active events and the induced internal precedence relation."""

    active: frozenset[Event]
    relation: Relation

    def __post_init__(self) -> None:
        expected = frozenset(
            (left, right)
            for left, right in PRECEDENCE
            if left in self.active and right in self.active
        )
        if self.relation != expected:
            raise ValueError("relation must be the active restriction of PRECEDENCE")


INITIAL_STATE = FixedState(frozenset(), frozenset())
FINAL_STATE = FixedState(frozenset(EVENTS), PRECEDENCE)


def predecessors(event: Event) -> frozenset[Event]:
    return frozenset(left for left, right in PRECEDENCE if right == event)


def make_state(active: Iterable[Event]) -> FixedState:
    active_set = frozenset(active)
    relation = frozenset(
        (left, right)
        for left, right in PRECEDENCE
        if left in active_set and right in active_set
    )
    return FixedState(active_set, relation)


def successors(state: FixedState) -> frozenset[FixedState]:
    result = set()
    for event in set(EVENTS) - set(state.active):
        if predecessors(event) <= state.active:
            result.add(make_state(state.active | {event}))
    return frozenset(result)


def reachable(
    initial: FixedState,
    successor: Callable[[FixedState], Iterable[FixedState]],
) -> frozenset[FixedState]:
    seen = {initial}
    frontier = [initial]
    while frontier:
        current = frontier.pop()
        for nxt in successor(current):
            if nxt not in seen:
                seen.add(nxt)
                frontier.append(nxt)
    return frozenset(seen)


def fixed_state_histories() -> tuple[tuple[FixedState, ...], ...]:
    histories: list[tuple[FixedState, ...]] = []

    def visit(state: FixedState, path: tuple[FixedState, ...]) -> None:
        if state == FINAL_STATE:
            histories.append(path)
            return
        for nxt in sorted(successors(state), key=lambda item: tuple(sorted(item.active))):
            visit(nxt, path + (nxt,))

    visit(INITIAL_STATE, (INITIAL_STATE,))
    return tuple(histories)


def events_from_state_path(path: tuple[FixedState, ...]) -> History:
    additions = []
    for before, after in zip(path, path[1:]):
        new_events = after.active - before.active
        assert len(new_events) == 1
        additions.append(next(iter(new_events)))
    return tuple(additions)


def all_small_timestamps(max_value: int = 3) -> tuple[dict[Event, int], ...]:
    valid = []
    for values in product(range(max_value + 1), repeat=len(EVENTS)):
        timestamp = dict(zip(EVENTS, values))
        if timestamp_preserves_order(timestamp):
            valid.append(timestamp)
    return tuple(valid)


def run_checks() -> dict[str, object]:
    assert_strict_partial_order(EVENTS, PRECEDENCE)
    assert PRECEDENCE == frozenset(
        {("a", "c"), ("b", "c"), ("c", "d"), ("a", "d"), ("b", "d")}
    )

    all_permutations = tuple(permutations(EVENTS))
    valid_histories = tuple(
        history for history in all_permutations if is_linear_extension(history)
    )
    invalid_histories = tuple(
        history for history in all_permutations if not is_linear_extension(history)
    )
    expected_histories = {("a", "b", "c", "d"), ("b", "a", "c", "d")}
    assert set(valid_histories) == expected_histories
    assert len(invalid_histories) == 22
    assert not is_linear_extension(("a", "b", "d", "c"))

    targets = {quotient_target(history) for history in valid_histories}
    assert len(targets) == 1
    assert len(valid_histories) > len(targets)
    assert len({target_predicates(quotient_target(h)) for h in valid_histories}) == 1

    h1 = ("a", "b", "c", "d")
    h2 = ("b", "a", "c", "d")
    assert h1 != h2
    assert quotient_target(h1) == quotient_target(h2)
    assert PRECEDENCE <= linear_order(h1)
    assert PRECEDENCE <= linear_order(h2)
    assert ("a", "b") in linear_order(h1) and ("a", "b") not in PRECEDENCE
    assert ("b", "a") in linear_order(h2) and ("b", "a") not in PRECEDENCE

    cost_h1 = path_dependent_cost(h1)
    cost_h2 = path_dependent_cost(h2)
    assert cost_h1 == 30
    assert cost_h2 == 29
    assert cost_h1 != cost_h2
    enriched_targets = {
        (quotient_target(history), path_dependent_cost(history))
        for history in valid_histories
    }
    assert len(enriched_targets) == 2

    timestamp_equal_incomparables = {"a": 0, "b": 0, "c": 1, "d": 2}
    timestamp_separated = {"a": 10, "b": 20, "c": 30, "d": 100}
    timestamp_h1 = construction_timestamp(h1)
    timestamp_h2 = construction_timestamp(h2)
    for timestamp in (
        timestamp_equal_incomparables,
        timestamp_separated,
        timestamp_h1,
        timestamp_h2,
    ):
        assert timestamp_preserves_order(timestamp)
    assert timestamp_h1 != timestamp_h2
    assert timestamp_equal_incomparables["d"] - timestamp_equal_incomparables["a"] == 2
    assert timestamp_separated["d"] - timestamp_separated["a"] == 90
    transformed_timestamp = {
        event: 2 * value + 7 for event, value in timestamp_separated.items()
    }
    assert timestamp_preserves_order(transformed_timestamp)
    bounded_timestamps = all_small_timestamps()
    assert len(bounded_timestamps) > 1

    reachable_states = reachable(INITIAL_STATE, successors)
    transitions = frozenset(
        (state, nxt) for state in reachable_states for nxt in successors(state)
    )
    state_paths = fixed_state_histories()
    encoded_histories = {events_from_state_path(path) for path in state_paths}
    assert len(reachable_states) == 6
    assert len(transitions) == 6
    assert encoded_histories == expected_histories
    assert all(path[-1] == FINAL_STATE for path in state_paths)

    return {
        "events": len(EVENTS),
        "precedence_pairs_after_transitive_closure": len(PRECEDENCE),
        "all_permutations": len(all_permutations),
        "valid_linear_extensions": len(valid_histories),
        "invalid_permutations": len(invalid_histories),
        "valid_histories": ["".join(history) for history in valid_histories],
        "distinct_pure_order_targets": len(targets),
        "pure_order_quotient_classes": len(targets),
        "selected_target_predicates_preserved": True,
        "dependent_swap_abdc_valid": is_linear_extension(("a", "b", "d", "c")),
        "history_costs": {"abcd": cost_h1, "bacd": cost_h2},
        "history_enriched_target_classes": len(enriched_targets),
        "bounded_order_preserving_timestamps_0_to_3": len(bounded_timestamps),
        "construction_timestamps_distinct": timestamp_h1 != timestamp_h2,
        "duration_a_to_d_examples": [2, 90],
        "fixed_states_reachable": len(reachable_states),
        "fixed_state_transitions": len(transitions),
        "fixed_state_histories": len(state_paths),
        "fixed_state_history_correspondence": True,
    }


def main() -> None:
    results = run_checks()
    print("construction versus internal order finite checker v0.1")
    for key, value in results.items():
        print(f"{key}={value}")
    print("all_assertions_passed=True")
    print(
        "scope=finite order-theoretic and combinatorial facts only; no claim "
        "about physical time, causality, ontological generation, or universal "
        "temporal emergence"
    )


if __name__ == "__main__":
    main()

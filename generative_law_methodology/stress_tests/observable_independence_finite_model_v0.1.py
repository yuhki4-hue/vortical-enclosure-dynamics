#!/usr/bin/env python3
"""Finite checks for definable versus independently variable observables.

This checker verifies combinatorial facts in six explicitly encoded finite
models.  It does not prove generation, ontology, physical emergence, or a
general characterization theorem.
"""

from __future__ import annotations

from itertools import product
from typing import Callable, Hashable, Iterable, Mapping, Sequence, TypeVar


Source = TypeVar("Source", bound=Hashable)
Target = TypeVar("Target", bound=Hashable)
Value = Hashable


def fibers(
    source_states: Sequence[Source],
    target_states: Sequence[Target],
    forget: Callable[[Target], Source],
) -> dict[Source, tuple[Target, ...]]:
    grouped: dict[Source, list[Target]] = {state: [] for state in source_states}
    for target in target_states:
        grouped[forget(target)].append(target)
    return {source: tuple(states) for source, states in grouped.items()}


def observation_signature(
    state: Target, observables: Mapping[str, Callable[[Target], Value]]
) -> tuple[Value, ...]:
    return tuple(observable(state) for observable in observables.values())


def quotient_fiber_counts(
    source_states: Sequence[Source],
    target_states: Sequence[Target],
    forget: Callable[[Target], Source],
    observables: Mapping[str, Callable[[Target], Value]],
) -> dict[Source, int]:
    result: dict[Source, int] = {}
    for source, states in fibers(source_states, target_states, forget).items():
        result[source] = len(
            {observation_signature(state, observables) for state in states}
        )
    return result


def raw_fiber_counts(
    source_states: Sequence[Source],
    target_states: Sequence[Target],
    forget: Callable[[Target], Source],
) -> dict[Source, int]:
    return {
        source: len(states)
        for source, states in fibers(source_states, target_states, forget).items()
    }


def fiber_separation_criterion(
    source_states: Sequence[Source],
    target_states: Sequence[Target],
    forget: Callable[[Target], Source],
    observables: Mapping[str, Callable[[Target], Value]],
) -> bool:
    return any(
        count > 1
        for count in quotient_fiber_counts(
            source_states, target_states, forget, observables
        ).values()
    )


def functionally_dependent_on_source(
    source_states: Sequence[Source],
    target_states: Sequence[Target],
    forget: Callable[[Target], Source],
    target_value: Callable[[Target], Value],
) -> bool:
    """Return whether target_value is constant on every raw fiber.

    In these finite models this is extensional functional dependence on the
    complete source state.  It is not, by itself, explicit definability in a
    chosen object language.
    """

    for states in fibers(source_states, target_states, forget).values():
        if len({target_value(state) for state in states}) > 1:
            return False
    return True


def all_source_states_expand(
    source_states: Sequence[Source],
    target_states: Sequence[Target],
    forget: Callable[[Target], Source],
) -> bool:
    return all(
        len(states) > 0
        for states in fibers(source_states, target_states, forget).values()
    )


def observation_preserving(
    source_observable: Callable[[Source], Value],
    target_observable: Callable[[Target], Value],
    target_states: Iterable[Target],
    forget: Callable[[Target], Source],
) -> bool:
    return all(
        target_observable(target) == source_observable(forget(target))
        for target in target_states
    )


def traces(
    states: Iterable[Target],
    step: Callable[[Target], Target],
    observable: Callable[[Target], Value],
    horizon: int,
) -> dict[Target, tuple[Value, ...]]:
    result: dict[Target, tuple[Value, ...]] = {}
    for initial in states:
        current = initial
        trace: list[Value] = []
        for _ in range(horizon):
            trace.append(observable(current))
            current = step(current)
        result[initial] = tuple(trace)
    return result


def fiber_traces_collapse(
    source_states: Sequence[Source],
    target_states: Sequence[Target],
    forget: Callable[[Target], Source],
    step: Callable[[Target], Target],
    observable: Callable[[Target], Value],
    horizon: int,
) -> bool:
    trace_map = traces(target_states, step, observable, horizon)
    for states in fibers(source_states, target_states, forget).values():
        if len({trace_map[state] for state in states}) > 1:
            return False
    return True


def format_key(value: Hashable) -> str:
    if isinstance(value, tuple):
        return "(" + ",".join(str(part) for part in value) + ")"
    return str(value)


def format_counts(counts: Mapping[Hashable, int]) -> str:
    return "{" + ", ".join(
        f"{format_key(key)}:{value}" for key, value in counts.items()
    ) + "}"


def main() -> None:
    bit = (0, 1)
    square = tuple(product(bit, repeat=2))

    print("observable independence finite model v0.1")

    # Case A: Q = 1 - P, with a unique target expansion per source state.
    a_source = bit
    a_target = ((0, 1), (1, 0))
    a_forget = lambda state: state[0]
    a_observables = {
        "P": lambda state: state[0],
        "Q": lambda state: state[1],
    }
    a_raw = raw_fiber_counts(a_source, a_target, a_forget)
    a_quotient = quotient_fiber_counts(
        a_source, a_target, a_forget, a_observables
    )
    a_explicit_definition = all(q == 1 - p for p, q in a_target)
    a_dependent = functionally_dependent_on_source(
        a_source, a_target, a_forget, lambda state: state[1]
    )
    a_old_observation_preserved = observation_preserving(
        lambda source: source,
        lambda target: target[0],
        a_target,
        a_forget,
    )
    assert a_raw == {0: 1, 1: 1}
    assert a_quotient == {0: 1, 1: 1}
    assert a_explicit_definition and a_dependent
    assert all_source_states_expand(a_source, a_target, a_forget)
    assert a_old_observation_preserved
    assert not fiber_separation_criterion(
        a_source, a_target, a_forget, a_observables
    )
    print(
        "A definitional: "
        f"raw={format_counts(a_raw)} "
        f"quotient={format_counts(a_quotient)} "
        "unique_expansion=True explicit_Q=1-P=True "
        "criterion=False"
    )

    # Case B: a raw tag doubles each fiber but allowed observation sees only P.
    b_source = bit
    b_target = square
    b_forget = lambda state: state[0]
    b_observables = {"P": lambda state: state[0]}
    b_raw = raw_fiber_counts(b_source, b_target, b_forget)
    b_quotient = quotient_fiber_counts(
        b_source, b_target, b_forget, b_observables
    )
    b_tag_dependent = functionally_dependent_on_source(
        b_source, b_target, b_forget, lambda state: state[1]
    )
    assert b_raw == {0: 2, 1: 2}
    assert b_quotient == {0: 1, 1: 1}
    assert not b_tag_dependent
    assert not fiber_separation_criterion(
        b_source, b_target, b_forget, b_observables
    )
    print(
        "B redundant: "
        f"raw={format_counts(b_raw)} "
        f"quotient={format_counts(b_quotient)} "
        "tag_function_of_source=False criterion=False"
    )

    # Case C: U is allowed as an observation and separates target expansions.
    c_source = bit
    c_target = square
    c_forget = lambda state: state[0]
    c_observables = {
        "P": lambda state: state[0],
        "U": lambda state: state[1],
    }
    c_raw = raw_fiber_counts(c_source, c_target, c_forget)
    c_quotient = quotient_fiber_counts(
        c_source, c_target, c_forget, c_observables
    )
    c_u_dependent = functionally_dependent_on_source(
        c_source, c_target, c_forget, lambda state: state[1]
    )
    assert c_raw == {0: 2, 1: 2}
    assert c_quotient == {0: 2, 1: 2}
    assert not c_u_dependent
    assert fiber_separation_criterion(
        c_source, c_target, c_forget, c_observables
    )
    print(
        "C distinguishable: "
        f"raw={format_counts(c_raw)} "
        f"quotient={format_counts(c_quotient)} "
        "U_function_of_source=False criterion=True"
    )

    # Case D: same target and observational equivalence, two comparison maps.
    d_source = bit
    d_target = square
    d_observables = {"X": lambda state: state[0]}
    d_p1 = lambda state: state[0]
    d_p2 = lambda state: state[1]
    d_p1_quotient = quotient_fiber_counts(
        d_source, d_target, d_p1, d_observables
    )
    d_p2_quotient = quotient_fiber_counts(
        d_source, d_target, d_p2, d_observables
    )
    d_p1_preserves = observation_preserving(
        lambda source: source,
        lambda target: target[0],
        d_target,
        d_p1,
    )
    d_p2_preserves = observation_preserving(
        lambda source: source,
        lambda target: target[0],
        d_target,
        d_p2,
    )
    assert d_p1_quotient == {0: 1, 1: 1}
    assert d_p2_quotient == {0: 2, 1: 2}
    assert d_p1_preserves and not d_p2_preserves
    assert not fiber_separation_criterion(
        d_source, d_target, d_p1, d_observables
    )
    assert fiber_separation_criterion(
        d_source, d_target, d_p2, d_observables
    )
    print(
        "D map choice: "
        f"p1_quotient={format_counts(d_p1_quotient)} "
        "p1_preserves_source_observation=True p1_criterion=False; "
        f"p2_quotient={format_counts(d_p2_quotient)} "
        "p2_preserves_source_observation=False p2_criterion=True"
    )

    # Hidden-source control: coarsening away U manufactures apparent novelty.
    d_full_source = square
    d_full_forget = lambda state: state
    d_full_observables = {
        "X": lambda state: state[0],
        "U": lambda state: state[1],
    }
    d_coarse_forget = lambda state: state[0]
    d_coarse_criterion = fiber_separation_criterion(
        bit, d_target, d_coarse_forget, d_full_observables
    )
    d_full_criterion = fiber_separation_criterion(
        d_full_source, d_target, d_full_forget, d_full_observables
    )
    assert d_coarse_criterion and not d_full_criterion
    print(
        "D hidden-source: "
        "coarse_source_criterion=True full_source_identity_criterion=False"
    )

    # Control E: Q = P xor R is directly accessible but explicitly definable.
    e_source = square
    e_target = tuple((p, r, p ^ r) for p, r in square)
    e_forget = lambda state: (state[0], state[1])
    e_observables = {
        "P": lambda state: state[0],
        "R": lambda state: state[1],
        "Q": lambda state: state[2],
    }
    e_raw = raw_fiber_counts(e_source, e_target, e_forget)
    e_quotient = quotient_fiber_counts(
        e_source, e_target, e_forget, e_observables
    )
    e_explicit_definition = all(q == (p ^ r) for p, r, q in e_target)
    e_dependent = functionally_dependent_on_source(
        e_source, e_target, e_forget, lambda state: state[2]
    )
    assert all(value == 1 for value in e_raw.values())
    assert all(value == 1 for value in e_quotient.values())
    assert e_explicit_definition and e_dependent
    assert not fiber_separation_criterion(
        e_source, e_target, e_forget, e_observables
    )
    print(
        "E accessible-definable: "
        f"raw={format_counts(e_raw)} "
        f"quotient={format_counts(e_quotient)} "
        "explicit_Q=P_xor_R=True criterion=False"
    )

    # Control F: U varies in the state but is neither observed nor coupled to P.
    f_source = bit
    f_target = square
    f_forget = lambda state: state[0]
    f_observables = {"P": lambda state: state[0]}
    f_step = lambda state: (1 - state[0], state[1])
    f_raw = raw_fiber_counts(f_source, f_target, f_forget)
    f_quotient = quotient_fiber_counts(
        f_source, f_target, f_forget, f_observables
    )
    f_u_dependent = functionally_dependent_on_source(
        f_source, f_target, f_forget, lambda state: state[1]
    )
    f_trace_collapse = fiber_traces_collapse(
        f_source,
        f_target,
        f_forget,
        f_step,
        lambda state: state[0],
        horizon=8,
    )
    assert f_raw == {0: 2, 1: 2}
    assert f_quotient == {0: 1, 1: 1}
    assert not f_u_dependent
    assert f_trace_collapse
    assert not fiber_separation_criterion(
        f_source, f_target, f_forget, f_observables
    )
    print(
        "F uncoupled: "
        f"raw={format_counts(f_raw)} "
        f"quotient={format_counts(f_quotient)} "
        "U_function_of_source=False observed_traces_collapse_h8=True "
        "criterion=False"
    )

    print("all_assertions_passed=6_cases")


if __name__ == "__main__":
    main()

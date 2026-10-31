#!/usr/bin/env python3
"""Finite checks for changing rules versus rules encoded as state/data.

The checker verifies only the encoded finite rule/state combinatorics.  It does
not establish open-ended generation, new-law creation, ontology, or a universal
reduction to a fixed meta-rule.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from typing import Callable, Iterable, Mapping


X: tuple[int, ...] = (0, 1, 2)
RuleCode = tuple[int, int, int]

PLUS: RuleCode = (1, 2, 2)
MINUS: RuleCode = (0, 0, 1)
STAY: RuleCode = (0, 1, 2)

BASE_RULES: dict[str, RuleCode] = {
    "r_plus": PLUS,
    "r_minus": MINUS,
    "r_zero": STAY,
}


def interpret(code: RuleCode, value: int) -> int:
    if code not in ALL_UNARY_CODES:
        raise ValueError("invalid unary rule code")
    if value not in X:
        raise ValueError("object state outside X")
    return code[value]


ALL_UNARY_CODES: frozenset[RuleCode] = frozenset(product(X, repeat=len(X)))


def compose(after: RuleCode, before: RuleCode) -> RuleCode:
    return tuple(interpret(after, interpret(before, value)) for value in X)  # type: ignore[return-value]


def composition_closure(seeds: Iterable[RuleCode]) -> frozenset[RuleCode]:
    closure = set(seeds)
    changed = True
    while changed:
        changed = False
        for after in tuple(closure):
            for before in tuple(closure):
                derived = compose(after, before)
                if derived not in closure:
                    closure.add(derived)
                    changed = True
    return frozenset(closure)


PLUS_TWICE: RuleCode = compose(PLUS, PLUS)
BASE_COMPOSITION_CLOSURE = composition_closure(BASE_RULES.values())
OUTSIDE_COMPOSITION: RuleCode = (0, 0, 2)
RULES_WITH_DERIVED: dict[str, RuleCode] = {
    **BASE_RULES,
    "r_hold_alias": STAY,
    "r_plus_twice": PLUS_TWICE,
}


def base_label_from_code(code: RuleCode) -> str:
    matches = [name for name, candidate in BASE_RULES.items() if candidate == code]
    if len(matches) != 1:
        raise ValueError("core translation requires a unique base-rule label")
    return matches[0]


def next_base_rule(current: str, updated_value: int) -> str:
    if updated_value == 2:
        return "r_minus"
    if updated_value == 0:
        return "r_plus"
    return current


def next_code(current: RuleCode, updated_value: int) -> RuleCode:
    if updated_value == 2:
        return MINUS
    if updated_value == 0:
        return PLUS
    return current


@dataclass(frozen=True)
class ARecord:
    """Description A: object state plus the currently operational rule label."""

    value: int
    active_rule: str

    def __post_init__(self) -> None:
        if self.value not in X or self.active_rule not in BASE_RULES:
            raise ValueError("invalid A record")


@dataclass(frozen=True)
class BState:
    """Description B: object state plus an active truth-table code."""

    value: int
    rule_code: RuleCode

    def __post_init__(self) -> None:
        if self.value not in X or self.rule_code not in ALL_UNARY_CODES:
            raise ValueError("invalid B state")


def step_a(record: ARecord) -> ARecord:
    updated_value = interpret(BASE_RULES[record.active_rule], record.value)
    return ARecord(updated_value, next_base_rule(record.active_rule, updated_value))


def meta_step_b(state: BState) -> BState:
    """Fixed higher-order transition: interpret data, then update rule data."""

    updated_value = interpret(state.rule_code, state.value)
    return BState(updated_value, next_code(state.rule_code, updated_value))


def to_b(record: ARecord) -> BState:
    return BState(record.value, BASE_RULES[record.active_rule])


def to_a(state: BState) -> ARecord:
    return ARecord(state.value, base_label_from_code(state.rule_code))


def trace(initial, step: Callable, transitions: int) -> tuple:
    result = [initial]
    for _ in range(transitions):
        result.append(step(result[-1]))
    return tuple(result)


def reachable_deterministic(initial, step: Callable) -> frozenset:
    seen = set()
    current = initial
    while current not in seen:
        seen.add(current)
        current = step(current)
    return frozenset(seen)


def change_events(items: tuple) -> tuple[int, ...]:
    return tuple(index for index, (left, right) in enumerate(zip(items, items[1:]), 1) if left != right)


@dataclass(frozen=True)
class SubsetState:
    value: int
    active_rules: frozenset[str]

    def __post_init__(self) -> None:
        if self.value not in X:
            raise ValueError("invalid object value")
        if not self.active_rules or not self.active_rules <= frozenset(BASE_RULES):
            raise ValueError("active rule subset must be nonempty and predeclared")


def update_active_subset(active: frozenset[str], updated_value: int) -> frozenset[str]:
    if updated_value == 2:
        return frozenset({"r_minus", "r_zero"})
    if updated_value == 0:
        return frozenset({"r_plus"})
    return active


def subset_successors(state: SubsetState) -> frozenset[SubsetState]:
    result = set()
    for rule_name in state.active_rules:
        updated_value = interpret(BASE_RULES[rule_name], state.value)
        result.add(SubsetState(updated_value, update_active_subset(state.active_rules, updated_value)))
    return frozenset(result)


def reachable_relation(initial, successors: Callable) -> tuple[frozenset, frozenset]:
    seen = {initial}
    frontier = [initial]
    edges = set()
    while frontier:
        current = frontier.pop()
        for nxt in successors(current):
            edges.add((current, nxt))
            if nxt not in seen:
                seen.add(nxt)
                frontier.append(nxt)
    return frozenset(seen), frozenset(edges)


THETA_TO_CODE: dict[int, RuleCode] = {-1: MINUS, 0: STAY, 1: PLUS}


@dataclass(frozen=True)
class ParameterState:
    value: int
    theta: int


def parameter_step(state: ParameterState) -> ParameterState:
    updated_value = interpret(THETA_TO_CODE[state.theta], state.value)
    if updated_value == 2:
        updated_theta = -1
    elif updated_value == 0:
        updated_theta = 1
    else:
        updated_theta = state.theta
    return ParameterState(updated_value, updated_theta)


def behaviorally_equivalent(left_name: str, right_name: str) -> bool:
    return all(
        interpret(RULES_WITH_DERIVED[left_name], value)
        == interpret(RULES_WITH_DERIVED[right_name], value)
        for value in X
    )


def encode_rule_subset(names: frozenset[str], repertoire: tuple[str, ...]) -> tuple[bool, ...]:
    return tuple(name in names for name in repertoire)


def decode_rule_subset(bits: tuple[bool, ...], repertoire: tuple[str, ...]) -> frozenset[str]:
    if len(bits) != len(repertoire):
        raise ValueError("availability code has the wrong length")
    return frozenset(name for name, enabled in zip(repertoire, bits) if enabled)


@dataclass(frozen=True)
class TypedRuleCode:
    name: str
    arity: int
    table: tuple[int, ...]

    def __post_init__(self) -> None:
        if self.arity not in (1, 2):
            raise ValueError("finite tagged interpreter supports arities 1 and 2")
        if len(self.table) != len(X) ** self.arity or any(value not in X for value in self.table):
            raise ValueError("invalid typed truth table")


UNARY_PLUS = TypedRuleCode("unary_plus", 1, PLUS)
BINARY_MAX = TypedRuleCode(
    "binary_max",
    2,
    tuple(max(left, right) for left in X for right in X),
)


def typed_interpret(code: TypedRuleCode, arguments: tuple[int, ...]) -> int:
    if len(arguments) != code.arity or any(value not in X for value in arguments):
        raise ValueError("arity/type check failed")
    if code.arity == 1:
        index = arguments[0]
    else:
        index = arguments[0] * len(X) + arguments[1]
    return code.table[index]


@dataclass(frozen=True)
class HistoryState:
    value: int
    rule_code: RuleCode
    history: tuple[int, ...]

    def __post_init__(self) -> None:
        if self.value not in X or self.rule_code not in ALL_UNARY_CODES:
            raise ValueError("invalid history-state payload")
        if len(self.history) > 3 or any(item not in X for item in self.history):
            raise ValueError("history control is bounded to length three")


def history_sensitive_step(state: HistoryState) -> HistoryState:
    updated_value = interpret(state.rule_code, state.value)
    updated_history = state.history + (updated_value,)
    updated_rule = PLUS if updated_history.count(1) % 2 else MINUS
    return HistoryState(updated_value, updated_rule, updated_history)


META_BOUNCE = "bounce"
META_KEEP = "keep"
META_RULES = (META_BOUNCE, META_KEEP)


def finite_meta_interpreter(meta_code: str, state: BState) -> BState:
    if meta_code == META_BOUNCE:
        return meta_step_b(state)
    if meta_code == META_KEEP:
        updated_value = interpret(state.rule_code, state.value)
        return BState(updated_value, state.rule_code)
    raise ValueError("unknown finite meta-rule code")


@dataclass(frozen=True)
class MetaState:
    object_rule_state: BState
    meta_code: str


def fixed_star_step(state: MetaState) -> MetaState:
    """A fixed interpreter over a finite, predeclared set of meta-rule codes."""

    updated = finite_meta_interpreter(state.meta_code, state.object_rule_state)
    updated_meta = META_KEEP if updated.value == 1 else state.meta_code
    return MetaState(updated, updated_meta)


def run_checks() -> dict[str, object]:
    assert len(ALL_UNARY_CODES) == 27
    assert all(interpret(code, value) in X for code in ALL_UNARY_CODES for value in X)

    # Main A/B comparison.
    initial_a = ARecord(0, "r_plus")
    initial_b = to_b(initial_a)
    trace_a = trace(initial_a, step_a, 8)
    trace_b = trace(initial_b, meta_step_b, 8)
    assert tuple(to_b(record) for record in trace_a) == trace_b
    assert tuple(to_a(state) for state in trace_b) == trace_a
    assert all(to_a(to_b(record)) == record for record in trace_a)
    assert all(to_b(to_a(state)) == state for state in trace_b)

    object_trace_a = tuple(record.value for record in trace_a)
    object_trace_b = tuple(state.value for state in trace_b)
    rule_trace_a = tuple(record.active_rule for record in trace_a)
    rule_trace_b = tuple(base_label_from_code(state.rule_code) for state in trace_b)
    assert object_trace_a == object_trace_b
    assert rule_trace_a == rule_trace_b
    assert change_events(rule_trace_a) == change_events(rule_trace_b)

    reachable_a = reachable_deterministic(initial_a, step_a)
    reachable_b = reachable_deterministic(initial_b, meta_step_b)
    assert {to_b(record) for record in reachable_a} == reachable_b
    assert len(reachable_a) == 4

    # Active-subset powerset encoding.
    subset_initial = SubsetState(0, frozenset({"r_plus", "r_zero"}))
    subset_states, subset_edges = reachable_relation(subset_initial, subset_successors)
    assert any(len(state.active_rules) > 1 for state in subset_states)
    assert any(
        len(left.active_rules) != len(right.active_rules) for left, right in subset_edges
    )
    assert any(right.active_rules - left.active_rules for left, right in subset_edges)
    assert any(left.active_rules - right.active_rules for left, right in subset_edges)

    # Parameter update is the same finite behavior family encoded by theta.
    for value in X:
        for theta in THETA_TO_CODE:
            parameter_state = ParameterState(value, theta)
            encoded = BState(value, THETA_TO_CODE[theta])
            assert to_b(
                ARecord(value, base_label_from_code(THETA_TO_CODE[theta]))
            ) == encoded
            stepped_parameter = parameter_step(parameter_state)
            stepped_encoded = meta_step_b(encoded)
            assert BState(
                stepped_parameter.value, THETA_TO_CODE[stepped_parameter.theta]
            ) == stepped_encoded

    # New syntax can be an exact alias; composition can be a derived behavior.
    assert "r_hold_alias" != "r_zero"
    assert behaviorally_equivalent("r_hold_alias", "r_zero")
    assert PLUS_TWICE == (2, 2, 2)
    assert PLUS_TWICE == compose(PLUS, PLUS)
    assert PLUS_TWICE not in set(BASE_RULES.values())
    assert all(
        interpret(PLUS_TWICE, value)
        == interpret(PLUS, interpret(PLUS, value))
        for value in X
    )
    assert interpret(PLUS_TWICE, 0) == 2
    assert interpret(PLUS, 0) == 1
    assert len(BASE_COMPOSITION_CLOSURE) == 8
    assert OUTSIDE_COMPOSITION not in BASE_COMPOSITION_CLOSURE
    assert OUTSIDE_COMPOSITION in ALL_UNARY_CODES

    # Finite stage-local availability and ex-post maximal repertoire.
    stages = (
        frozenset(BASE_RULES),
        frozenset(BASE_RULES) | {"r_plus_twice"},
        frozenset(RULES_WITH_DERIVED),
    )
    maximal_repertoire = tuple(sorted(set().union(*stages)))
    encoded_stages = tuple(
        encode_rule_subset(stage, maximal_repertoire) for stage in stages
    )
    assert all(
        decode_rule_subset(bits, maximal_repertoire) == stage
        for stage, bits in zip(stages, encoded_stages)
    )
    assert "r_plus_twice" in maximal_repertoire
    assert "r_plus_twice" not in stages[0]
    assert "r_plus_twice" in stages[1]
    assert len(stages[0]) < len(stages[-1])

    # Type/signature change under a preloaded tagged interpreter.
    assert typed_interpret(UNARY_PLUS, (1,)) == 2
    assert typed_interpret(BINARY_MAX, (1, 2)) == 2
    initial_arities = frozenset({1})
    later_arities = frozenset({1, 2})
    assert BINARY_MAX.arity not in initial_arities
    assert BINARY_MAX.arity in later_arities
    arity_error_detected = False
    try:
        typed_interpret(BINARY_MAX, (1,))
    except ValueError:
        arity_error_detected = True
    assert arity_error_detected

    # History-dependent update becomes fixed-state once history is included.
    history_odd = HistoryState(1, STAY, (1,))
    history_even = HistoryState(1, STAY, (1, 1))
    history_next_odd = history_sensitive_step(history_odd)
    history_next_even = history_sensitive_step(history_even)
    assert (history_odd.value, history_odd.rule_code) == (
        history_even.value,
        history_even.rule_code,
    )
    assert history_next_odd.rule_code == MINUS
    assert history_next_even.rule_code == PLUS

    # A finite stochastic rule update can be a fixed transition kernel.
    stochastic_kernel: Mapping[RuleCode, Fraction] = {
        PLUS: Fraction(1, 2),
        MINUS: Fraction(1, 3),
        STAY: Fraction(1, 6),
    }
    assert sum(stochastic_kernel.values(), Fraction(0, 1)) == 1

    # A change among finitely coded meta-rules can itself be state under M*.
    meta_initial = MetaState(BState(0, PLUS), META_BOUNCE)
    meta_after = fixed_star_step(meta_initial)
    assert meta_after == MetaState(BState(1, PLUS), META_KEEP)
    assert len(META_RULES) == 2

    return {
        "object_states": len(X),
        "finite_unary_rule_tables": len(ALL_UNARY_CODES),
        "core_reachable_states_a": len(reachable_a),
        "core_reachable_states_b": len(reachable_b),
        "object_trace": list(object_trace_a),
        "active_rule_trace": list(rule_trace_a),
        "rule_change_event_steps": list(change_events(rule_trace_a)),
        "a_b_roundtrips": True,
        "reachable_state_preservation": True,
        "object_trace_preservation": True,
        "rule_trace_preservation": True,
        "rule_change_event_preservation": True,
        "subset_reachable_states": len(subset_states),
        "subset_transition_pairs": len(subset_edges),
        "subset_size_enable_disable_controls": True,
        "parameter_encoding_commutes": True,
        "alias_behavior_equivalent": True,
        "composition_rule_code": list(PLUS_TWICE),
        "composition_is_new_single_step_behavior": True,
        "composition_is_derived_from_existing_rules": True,
        "base_composition_closure_size": len(BASE_COMPOSITION_CLOSURE),
        "behavior_code_outside_composition_closure": list(OUTSIDE_COMPOSITION),
        "stage_rule_set_sizes": [len(stage) for stage in stages],
        "maximal_repertoire_size": len(maximal_repertoire),
        "availability_bitset_roundtrips": True,
        "preloaded_but_initially_unavailable": "r_plus_twice",
        "typed_unary_result": typed_interpret(UNARY_PLUS, (1,)),
        "typed_binary_result": typed_interpret(BINARY_MAX, (1, 2)),
        "stage_arity_growth": [sorted(initial_arities), sorted(later_arities)],
        "arity_checker_rejects_bad_input": arity_error_detected,
        "history_same_visible_pair_different_next_rule": True,
        "stochastic_kernel_sums_to_one": True,
        "finite_meta_rule_codes": len(META_RULES),
        "meta_change_encoded_under_fixed_star": True,
    }


def main() -> None:
    results = run_checks()
    print("rule space as data finite checker v0.1")
    for key, value in results.items():
        print(f"{key}={value}")
    print("all_assertions_passed=True")
    print(
        "scope=encoded finite rule/state combinatorics only; no claim about "
        "open-ended generation, new-law creation, ontology, or universal "
        "meta-rule reduction"
    )


if __name__ == "__main__":
    main()

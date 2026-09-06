"""Tiny truth-table checker for the finite propositional prototype v0.1.

This script checks the note's examples. It is not a general proof device.
"""

from dataclasses import dataclass
from itertools import product
from typing import Callable, Iterable, Optional, Sequence


Valuation = tuple[int, ...]


@dataclass(eq=False, frozen=True)
class Formula:
    label: str
    evaluate: Callable[[Valuation], bool]

    def __call__(self, valuation: Valuation) -> bool:
        return bool(self.evaluate(valuation))


def valuations(variable_count: int) -> tuple[Valuation, ...]:
    return tuple(product((0, 1), repeat=variable_count))


def models(
    universe: Iterable[Valuation], formula: Formula
) -> frozenset[Valuation]:
    return frozenset(valuation for valuation in universe if formula(valuation))


def models_of_assumptions(
    universe: Iterable[Valuation], assumptions: Sequence[Formula]
) -> frozenset[Valuation]:
    universe_set = frozenset(universe)
    if not assumptions:
        return universe_set
    return frozenset(
        valuation
        for valuation in universe_set
        if all(formula(valuation) for formula in assumptions)
    )


def counterexample_region(
    universe: Iterable[Valuation],
    assumptions: Sequence[Formula],
    target: Formula,
    admissible: Optional[Iterable[Valuation]] = None,
) -> frozenset[Valuation]:
    universe_set = frozenset(universe)
    scope = universe_set if admissible is None else frozenset(admissible)
    return (models_of_assumptions(universe_set, assumptions) & scope) - models(
        universe_set, target
    )


def semantically_entails(
    universe: Iterable[Valuation],
    assumptions: Sequence[Formula],
    target: Formula,
    admissible: Optional[Iterable[Valuation]] = None,
) -> bool:
    return not counterexample_region(universe, assumptions, target, admissible)


def m1(
    assumptions: Sequence[Formula], additions: Sequence[Formula]
) -> tuple[Formula, ...]:
    """Return H union B, preserving deterministic display order."""
    result = list(assumptions)
    for formula in additions:
        if formula not in result:
            result.append(formula)
    return tuple(result)


def m2(
    universe: Iterable[Valuation], target: Formula, weaker_target: Formula
) -> Formula:
    """Return C' after checking M(C) is a subset of M(C')."""
    universe_set = frozenset(universe)
    if not models(universe_set, target) <= models(universe_set, weaker_target):
        raise ValueError("The proposed target is not a semantic weakening.")
    return weaker_target


def restrict_scope(
    scope: Iterable[Valuation], restricted_scope: Iterable[Valuation]
) -> frozenset[Valuation]:
    scope_set = frozenset(scope)
    restricted_set = frozenset(restricted_scope)
    if not restricted_set <= scope_set:
        raise ValueError("The proposed scope is not a subset of the prior scope.")
    return restricted_set


def trivial_rescue_flags(
    universe: Iterable[Valuation],
    assumptions: Sequence[Formula],
    additions: Sequence[Formula],
    target: Formula,
    *,
    selection_provenance: str = "unknown",
) -> tuple[str, ...]:
    """Return typed flags; post-hoc status is supplied, never inferred."""
    flags: list[str] = []
    strengthened = m1(assumptions, additions)
    if any(formula is target for formula in additions):
        flags.append("DIRECT TARGET INSERTION")
    if not models_of_assumptions(universe, strengthened):
        flags.append("INCONSISTENT REPAIR")
    if selection_provenance == "post_hoc_domain_filter":
        flags.append("POST-HOC DOMAIN FILTER")
    elif selection_provenance not in {"independent", "unknown"}:
        raise ValueError("Unknown selection provenance value.")

    if flags:
        return tuple(flags)
    if selection_provenance == "independent":
        return ("NO FLAG",)
    return ("UNKNOWN",)


def show(region: Iterable[Valuation]) -> str:
    return "{" + ", ".join(f"omega_{p}{q}" for p, q in sorted(region)) + "}"


def main() -> None:
    omega = valuations(2)
    p = Formula("p", lambda valuation: valuation[0] == 1)
    p_or_q = Formula("p or q", lambda valuation: bool(valuation[0] or valuation[1]))
    not_q = Formula("not q", lambda valuation: valuation[1] == 0)
    not_p_or_q = Formula(
        "not (p or q)", lambda valuation: not bool(valuation[0] or valuation[1])
    )
    p_or_not_q = Formula(
        "p or not q", lambda valuation: bool(valuation[0] or not valuation[1])
    )

    h = (p_or_q,)
    before = counterexample_region(omega, h, p)
    assert before == frozenset({(0, 1)})

    # Example A: M1.
    h_a = m1(h, (not_q,))
    assert models_of_assumptions(omega, h_a) == frozenset({(1, 0)})
    assert semantically_entails(omega, h_a, p)
    assert counterexample_region(omega, h_a, p) == (
        before & models(omega, not_q)
    )
    assert trivial_rescue_flags(
        omega, h, (not_q,), p, selection_provenance="independent"
    ) == ("NO FLAG",)

    # Example B: M2.
    c_b = m2(omega, p, p_or_q)
    assert semantically_entails(omega, h, c_b)
    assert counterexample_region(omega, h, c_b) <= before

    # Example C: finite-domain scope surrogate.
    restricted = restrict_scope(omega, {(0, 0), (1, 0), (1, 1)})
    assert semantically_entails(omega, h, p, restricted)
    assert counterexample_region(omega, h, p, restricted) <= before

    # Example D1: direct target insertion.
    assert trivial_rescue_flags(omega, h, (p,), p) == (
        "DIRECT TARGET INSERTION",
    )
    assert semantically_entails(omega, m1(h, (p,)), p)

    # Example D2: inconsistent repair and empty-model-set inclusion.
    assert trivial_rescue_flags(omega, h, (not_p_or_q,), p) == (
        "INCONSISTENT REPAIR",
    )
    assert models_of_assumptions(omega, m1(h, (not_p_or_q,))) == frozenset()
    assert semantically_entails(omega, m1(h, (not_p_or_q,)), p)

    # Example D3: post-hoc filtering is an explicit provenance input.
    assert models_of_assumptions(omega, m1(h, (p_or_not_q,))) == (
        models_of_assumptions(omega, h) & models(omega, p)
    )
    assert trivial_rescue_flags(
        omega,
        h,
        (p_or_not_q,),
        p,
        selection_provenance="post_hoc_domain_filter",
    ) == ("POST-HOC DOMAIN FILTER",)
    assert trivial_rescue_flags(omega, h, (p_or_not_q,), p) == ("UNKNOWN",)

    # Example E uses the same h_a/p after-material under two identity histories.
    assert semantically_entails(omega, h_a, p)

    print(f"Omega: {show(omega)}")
    print(f"Before E(H, C): {show(before)}")
    print(f"Example A after E: {show(counterexample_region(omega, h_a, p))}")
    print(f"Example B after E: {show(counterexample_region(omega, h, c_b))}")
    print(
        "Example C after E_S: "
        f"{show(counterexample_region(omega, h, p, restricted))}"
    )
    print("All finite prototype checks passed.")


if __name__ == "__main__":
    main()

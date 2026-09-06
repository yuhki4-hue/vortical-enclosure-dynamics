"""Projection checker for the record-frame sensitivity test v0.1.

The script compares explicitly supplied finite histories under R0--R4.  It
does not decide which frame is correct, whether an identity assertion or
provenance statement is legitimate, or what an action really is.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any


BASE = Path(__file__).resolve().parent
_SPEC = importlib.util.spec_from_file_location(
    "finite_propositional_checker_v01",
    BASE.parent
    / "03_finite_propositional"
    / "proof_formation_finite_propositional_checker_v0.1.py",
)
assert _SPEC and _SPEC.loader
fp = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(fp)

Valuation = tuple[int, ...]
FrameRecord = tuple[Any, ...]


def frozen_valuations(values: Any) -> tuple[Valuation, ...]:
    return tuple(sorted(frozenset(values)))


def model_set(universe: tuple[Valuation, ...], formula: Any) -> tuple[Valuation, ...]:
    return frozen_valuations(fp.models(universe, formula))


def assumption_models(
    universe: tuple[Valuation, ...], assumptions: tuple[Any, ...]
) -> tuple[Valuation, ...]:
    return frozen_valuations(fp.models_of_assumptions(universe, assumptions))


def semantic_state(
    universe: tuple[Valuation, ...],
    assumptions: tuple[Any, ...],
    target: Any,
    scope: tuple[Valuation, ...],
) -> FrameRecord:
    assumption_set = fp.models_of_assumptions(universe, assumptions)
    target_set = fp.models(universe, target)
    scope_set = frozenset(scope)
    surviving = assumption_set & scope_set
    counterexamples = surviving - target_set
    return (
        ("M(H)", frozen_valuations(assumption_set)),
        ("M(C)", frozen_valuations(target_set)),
        ("S", frozen_valuations(scope_set)),
        ("surviving", frozen_valuations(surviving)),
        ("E", frozen_valuations(counterexamples)),
        ("entails", not counterexamples),
    )


def evaluated_effect(
    universe: tuple[Valuation, ...], history: dict[str, Any]
) -> FrameRecord:
    """After-effect with the H/S input-role distinction deliberately removed."""
    state = dict(semantic_state(
        universe,
        history["after_H"],
        history["after_C"],
        history["after_S"],
    ))
    return (
        ("surviving", state["surviving"]),
        ("M(C)", state["M(C)"]),
        ("E", state["E"]),
        ("entails", state["entails"]),
    )


def raw_state(history: dict[str, Any], prefix: str) -> FrameRecord:
    assumptions = history[f"{prefix}_H"]
    target = history[f"{prefix}_C"]
    scope = history[f"{prefix}_S"]
    return (
        ("H", tuple(sorted(formula.label for formula in assumptions))),
        ("C", target.label),
        ("S", frozen_valuations(scope)),
    )


def changed_slots(history: dict[str, Any]) -> tuple[str, ...]:
    before = dict(raw_state(history, "before"))
    after = dict(raw_state(history, "after"))
    return tuple(slot for slot in ("H", "C", "S") if before[slot] != after[slot])


def project_r0(universe: tuple[Valuation, ...], history: dict[str, Any]) -> FrameRecord:
    after = dict(semantic_state(
        universe,
        history["after_H"],
        history["after_C"],
        history["after_S"],
    ))
    return (
        ("semantic_success", after["entails"]),
        ("counterexample_remains", bool(after["E"])),
    )


def project_r1(universe: tuple[Valuation, ...], history: dict[str, Any]) -> FrameRecord:
    return (
        ("before", semantic_state(
            universe,
            history["before_H"],
            history["before_C"],
            history["before_S"],
        )),
        ("after", semantic_state(
            universe,
            history["after_H"],
            history["after_C"],
            history["after_S"],
        )),
    )


def project_r2(universe: tuple[Valuation, ...], history: dict[str, Any]) -> FrameRecord:
    return project_r1(universe, history) + (
        ("before_typed", raw_state(history, "before")),
        ("after_typed", raw_state(history, "after")),
        ("changed_slots", changed_slots(history)),
    )


def project_r3(universe: tuple[Valuation, ...], history: dict[str, Any]) -> FrameRecord:
    return project_r2(universe, history) + (
        ("identity", (history["original_id"], history["endpoint_id"])),
        ("same_identity", history["same_identity"]),
        ("original_status", history["original_status"]),
        ("endpoint_status", history["endpoint_status"]),
        ("successor", history["successor"]),
        ("segmentation", history["segmentation"]),
    )


def project_r4(universe: tuple[Valuation, ...], history: dict[str, Any]) -> FrameRecord:
    return project_r3(universe, history) + (
        ("selection_provenance", history["provenance"]),
    )


PROJECTORS = {
    "R0": project_r0,
    "R1": project_r1,
    "R2": project_r2,
    "R3": project_r3,
    "R4": project_r4,
}


def make_history(
    name: str,
    *,
    before_H: tuple[Any, ...],
    before_C: Any,
    before_S: tuple[Valuation, ...],
    intervention: str,
    after_H: tuple[Any, ...],
    after_C: Any,
    after_S: tuple[Valuation, ...],
    original_id: str = "x0",
    endpoint_id: str = "x0",
    same_identity: bool | None = True,
    original_status: str | None = None,
    endpoint_status: str = "failed",
    successor: tuple[str, str] | None = None,
    segmentation: str = "single",
    provenance: str = "UNKNOWN",
) -> dict[str, Any]:
    # This local dictionary is implementation scaffolding, not a proposed schema.
    return {
        "name": name,
        "before_H": before_H,
        "before_C": before_C,
        "before_S": before_S,
        "intervention": intervention,
        "after_H": after_H,
        "after_C": after_C,
        "after_S": after_S,
        "original_id": original_id,
        "endpoint_id": endpoint_id,
        "same_identity": same_identity,
        "original_status": original_status,
        "endpoint_status": endpoint_status,
        "successor": successor,
        "segmentation": segmentation,
        "provenance": provenance,
    }


def build_histories() -> tuple[tuple[Valuation, ...], dict[str, dict[str, Any]]]:
    omega = fp.valuations(2)
    p = fp.Formula("p", lambda valuation: valuation[0] == 1)
    p_or_q = fp.Formula("p or q", lambda valuation: bool(valuation[0] or valuation[1]))
    not_q = fp.Formula("not q", lambda valuation: valuation[1] == 0)
    not_not_p = fp.Formula("not not p", lambda valuation: valuation[0] == 1)
    top = fp.Formula("TRUE", lambda valuation: True)
    exact_filter = fp.Formula(
        "p or not q", lambda valuation: bool(valuation[0] or not valuation[1])
    )

    h0 = (p_or_q,)
    common = {
        "before_H": h0,
        "before_C": p,
        "before_S": omega,
    }

    histories = {
        "H1": make_history(
            "H1", **common, intervention="add not q",
            after_H=fp.m1(h0, (not_q,)), after_C=p, after_S=omega,
            endpoint_status="established", provenance="INDEPENDENT",
        ),
        "H2": make_history(
            "H2", **common, intervention="restrict S to Omega minus omega_01",
            after_H=h0, after_C=p,
            after_S=tuple(value for value in omega if value != (0, 1)),
            endpoint_status="established", provenance="UNKNOWN",
        ),
        "H3": make_history(
            "H3", **common, intervention="replace C by p or q",
            after_H=h0, after_C=p_or_q, after_S=omega,
            endpoint_status="established", provenance="UNKNOWN",
        ),
        "H4": make_history(
            "H4", **common, intervention="withdraw only",
            after_H=h0, after_C=p, after_S=omega,
            endpoint_status="withdrawn", original_status="withdrawn",
            same_identity=True, segmentation="single",
            provenance="INAPPLICABLE",
        ),
        "H5": make_history(
            "H5", **common, intervention="withdraw x0 and introduce successor x1",
            after_H=fp.m1(h0, (not_q,)), after_C=p, after_S=omega,
            endpoint_id="x1", same_identity=False,
            original_status="withdrawn", endpoint_status="established",
            successor=("x0", "x1"), segmentation="split",
            provenance="UNKNOWN",
        ),
        "H6": make_history(
            "H6", **common, intervention="continue x0 and add not q",
            after_H=fp.m1(h0, (not_q,)), after_C=p, after_S=omega,
            endpoint_status="established", provenance="UNKNOWN",
        ),
        "H7": make_history(
            "H7", **common, intervention="add not not p",
            after_H=fp.m1(h0, (not_not_p,)), after_C=p, after_S=omega,
            endpoint_status="established", provenance="UNKNOWN",
        ),
        "H8": make_history(
            "H8", **common, intervention="add TRUE",
            after_H=fp.m1(h0, (top,)), after_C=p, after_S=omega,
            endpoint_status="failed", provenance="UNKNOWN",
        ),
        "H9": make_history(
            "H9", **common, intervention="add exact filter p or not q",
            after_H=fp.m1(h0, (exact_filter,)), after_C=p, after_S=omega,
            endpoint_status="established", provenance="POST_HOC",
        ),
        "H10": make_history(
            "H10", **common, intervention="add independently selected p or not q",
            after_H=fp.m1(h0, (exact_filter,)), after_C=p, after_S=omega,
            endpoint_status="established", provenance="INDEPENDENT",
        ),
        "C-F": make_history(
            "C-F", **common, intervention="no intervention; remain failed",
            after_H=h0, after_C=p, after_S=omega,
            same_identity=None, endpoint_status="failed",
            segmentation="none", provenance="INAPPLICABLE",
        ),
        "C-D": make_history(
            "C-D", **common, intervention="add target p verbatim",
            after_H=fp.m1(h0, (p,)), after_C=p, after_S=omega,
            endpoint_status="established", provenance="UNKNOWN",
        ),
    }
    return omega, histories


def relation(
    universe: tuple[Valuation, ...],
    left: dict[str, Any],
    right: dict[str, Any],
    frame: str,
) -> str:
    projector = PROJECTORS[frame]
    return "COLLAPSED" if projector(universe, left) == projector(universe, right) else "DISTINCT"


def main() -> None:
    omega, histories = build_histories()

    h0 = histories["H1"]
    assert fp.counterexample_region(
        omega, h0["before_H"], h0["before_C"], h0["before_S"]
    ) == frozenset({(0, 1)})

    # Required truth-table and controlled-equivalence checks.
    assert assumption_models(omega, histories["H1"]["after_H"]) == ((1, 0),)
    assert frozen_valuations(
        fp.models_of_assumptions(omega, histories["H2"]["after_H"])
        & frozenset(histories["H2"]["after_S"])
    ) == ((1, 0), (1, 1))
    assert evaluated_effect(omega, histories["H9"]) == evaluated_effect(
        omega, histories["H2"]
    )
    assert project_r1(omega, histories["H9"]) != project_r1(omega, histories["H2"])
    assert project_r1(omega, histories["H7"]) == project_r1(omega, histories["C-D"])
    assert project_r2(omega, histories["H7"]) != project_r2(omega, histories["C-D"])
    assert project_r1(omega, histories["H8"]) == project_r1(omega, histories["C-F"])
    assert project_r2(omega, histories["H8"]) != project_r2(omega, histories["C-F"])

    pairs = {
        "P1 H1/H2": ("H1", "H2"),
        "P2 H1/H3": ("H1", "H3"),
        "P3 H4/C-F": ("H4", "C-F"),
        "P4 H5/H6": ("H5", "H6"),
        "P5 H9/H10": ("H9", "H10"),
        "P6 H7/C-D": ("H7", "C-D"),
        "P7 H1/H8": ("H1", "H8"),
        "P8 H9/H2": ("H9", "H2"),
        "P9 H8/C-F": ("H8", "C-F"),
    }
    expected = {
        "P1 H1/H2": ("COLLAPSED", "DISTINCT", "DISTINCT", "DISTINCT", "DISTINCT"),
        "P2 H1/H3": ("COLLAPSED", "DISTINCT", "DISTINCT", "DISTINCT", "DISTINCT"),
        "P3 H4/C-F": ("COLLAPSED", "COLLAPSED", "COLLAPSED", "DISTINCT", "DISTINCT"),
        "P4 H5/H6": ("COLLAPSED", "COLLAPSED", "COLLAPSED", "DISTINCT", "DISTINCT"),
        "P5 H9/H10": ("COLLAPSED", "COLLAPSED", "COLLAPSED", "COLLAPSED", "DISTINCT"),
        "P6 H7/C-D": ("COLLAPSED", "COLLAPSED", "DISTINCT", "DISTINCT", "DISTINCT"),
        "P7 H1/H8": ("DISTINCT", "DISTINCT", "DISTINCT", "DISTINCT", "DISTINCT"),
        "P8 H9/H2": ("COLLAPSED", "DISTINCT", "DISTINCT", "DISTINCT", "DISTINCT"),
        "P9 H8/C-F": ("COLLAPSED", "COLLAPSED", "DISTINCT", "DISTINCT", "DISTINCT"),
    }

    frames = tuple(PROJECTORS)
    print("Pair | " + " | ".join(frames))
    for pair_name, (left_name, right_name) in pairs.items():
        observed = tuple(
            relation(omega, histories[left_name], histories[right_name], frame)
            for frame in frames
        )
        assert observed == expected[pair_name]
        print(pair_name + " | " + " | ".join(observed))

    print("Matched H9/H2 evaluated effect: COLLAPSED")
    print("Matched H9/H2 full R1 carrier: DISTINCT")
    print("All projection comparisons passed; no frame judgment was made.")


if __name__ == "__main__":
    main()

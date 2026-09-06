"""Mechanical checks for the visibility-transition test v0.1.

The checker reuses the frozen histories and R0--R4 projectors unchanged.  It
compares projected records, reports first visibility and adjacent transition
classes, and checks selected erasures.  It does not decide which distinction
is real or important, which frame is correct, or what an action is.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any


BASE = Path(__file__).resolve().parent
_SPEC = importlib.util.spec_from_file_location(
    "record_frame_sensitivity_checker_v01",
    BASE / "proof_formation_record_frame_sensitivity_checker_v0.1.py",
)
assert _SPEC and _SPEC.loader
rf = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(rf)

FrameRecord = tuple[Any, ...]


PAIRS = {
    "V1 H1/H2": ("H1", "H2"),
    "V2 H1/H3": ("H1", "H3"),
    "V3 H4/C-F": ("H4", "C-F"),
    "V4 H5/H6": ("H5", "H6"),
    "V5 H9/H10": ("H9", "H10"),
    "V6 H7/C-D": ("H7", "C-D"),
    "V7 H8/C-F": ("H8", "C-F"),
    "V8 H9/H2": ("H9", "H2"),
    "V9 H5/H1": ("H5", "H1"),
}

EXPECTED = {
    "V1 H1/H2": (False, True, True, True, True),
    "V2 H1/H3": (False, True, True, True, True),
    "V3 H4/C-F": (False, False, False, True, True),
    "V4 H5/H6": (False, False, False, True, True),
    "V5 H9/H10": (False, False, False, False, True),
    "V6 H7/C-D": (False, False, True, True, True),
    "V7 H8/C-F": (False, False, True, True, True),
    "V8 H9/H2": (False, True, True, True, True),
    "V9 H5/H1": (False, False, False, True, True),
}


def is_visible(
    universe: tuple[tuple[int, ...], ...],
    histories: dict[str, dict[str, Any]],
    pair: tuple[str, str],
    frame: str,
) -> bool:
    left, right = pair
    projector = rf.PROJECTORS[frame]
    return projector(universe, histories[left]) != projector(
        universe, histories[right]
    )


def transition_class(before: bool, after: bool) -> str:
    if not before and after:
        return "APPEARS"
    if before and after:
        return "REMAINS VISIBLE"
    if not before and not after:
        return "REMAINS INVISIBLE"
    return "DISAPPEARS"


def first_visible(frames: tuple[str, ...], signature: tuple[bool, ...]) -> str:
    for frame, visible in zip(frames, signature):
        if visible:
            return frame
    return "NONE"


def main() -> None:
    omega, histories = rf.build_histories()
    frames = tuple(rf.PROJECTORS)

    print("Pair | " + " | ".join(frames) + " | signature | first")
    observed_by_pair: dict[str, tuple[bool, ...]] = {}
    for pair_name, pair in PAIRS.items():
        observed = tuple(
            is_visible(omega, histories, pair, frame) for frame in frames
        )
        assert observed == EXPECTED[pair_name]
        observed_by_pair[pair_name] = observed
        labels = tuple("VISIBLE" if value else "INVISIBLE" for value in observed)
        signature = "".join("1" if value else "0" for value in observed)
        print(
            pair_name + " | " + " | ".join(labels)
            + f" | {signature} | {first_visible(frames, observed)}"
        )

    print("\nPair | " + " | ".join(
        f"{left}->{right}" for left, right in zip(frames, frames[1:])
    ))
    transition_rows: dict[str, tuple[str, ...]] = {}
    for pair_name, observed in observed_by_pair.items():
        classes = tuple(
            transition_class(left, right)
            for left, right in zip(observed, observed[1:])
        )
        transition_rows[pair_name] = classes
        print(pair_name + " | " + " | ".join(classes))

    # Nested projector inheritance produced no visibility loss under enrichment.
    assert not any(
        value == "DISAPPEARS"
        for classes in transition_rows.values()
        for value in classes
    )

    # R1 keeps H and S as separate semantic carriers; the evaluated-effect
    # subprojection deliberately erases that role distinction.
    assert rf.evaluated_effect(omega, histories["H9"]) == rf.evaluated_effect(
        omega, histories["H2"]
    )
    assert rf.project_r1(omega, histories["H9"]) != rf.project_r1(
        omega, histories["H2"]
    )

    # Selected reverse erasures reproduce the corresponding collapse.
    assert rf.project_r3(omega, histories["H9"]) == rf.project_r3(
        omega, histories["H10"]
    )
    assert rf.project_r2(omega, histories["H5"]) == rf.project_r2(
        omega, histories["H6"]
    )
    assert rf.project_r1(omega, histories["H7"]) == rf.project_r1(
        omega, histories["C-D"]
    )
    assert rf.project_r1(omega, histories["H8"]) == rf.project_r1(
        omega, histories["C-F"]
    )

    print("\nH9/H2 evaluated subprojection: INVISIBLE")
    print("H9/H2 full R1 carrier: VISIBLE")
    print("No DISAPPEARS transition occurred under nested enrichment.")
    print("All visibility and erasure checks passed; no ontology was decided.")


if __name__ == "__main__":
    main()

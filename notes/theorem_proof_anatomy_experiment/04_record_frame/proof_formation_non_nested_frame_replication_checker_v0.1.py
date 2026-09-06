"""Mechanical checks for the non-nested frame replication test v0.1.

The checker imports the existing frozen histories without changing them and
projects them through six deliberately non-nested, test-local frames.  It
checks projection equality, field differences, selected replication controls,
and a display-order permutation.  It does not adjudicate truth, importance,
identity, provenance, action ontology, or frame quality.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any, Callable


BASE = Path(__file__).resolve().parent
_SPEC = importlib.util.spec_from_file_location(
    "record_frame_sensitivity_checker_v01",
    BASE / "proof_formation_record_frame_sensitivity_checker_v0.1.py",
)
assert _SPEC and _SPEC.loader
rf = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(rf)

Valuation = tuple[int, ...]
FrameRecord = tuple[Any, ...]
Projector = Callable[[tuple[Valuation, ...], dict[str, Any]], FrameRecord]


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

EXPECTED_R = {
    "V1 H1/H2": "01111",
    "V2 H1/H3": "01111",
    "V3 H4/C-F": "00011",
    "V4 H5/H6": "00011",
    "V5 H9/H10": "00001",
    "V6 H7/C-D": "00111",
    "V7 H8/C-F": "00111",
    "V8 H9/H2": "01111",
    "V9 H5/H1": "00011",
}

EXPECTED_N = {
    "V1 H1/H2": "011011",
    "V2 H1/H3": "011011",
    "V3 H4/C-F": "000100",
    "V4 H5/H6": "000101",
    "V5 H9/H10": "000011",
    "V6 H7/C-D": "001000",
    "V7 H8/C-F": "001111",
    "V8 H9/H2": "001011",
    "V9 H5/H1": "000111",
}


def evaluated_state(
    universe: tuple[Valuation, ...], history: dict[str, Any], prefix: str
) -> FrameRecord:
    full = dict(
        rf.semantic_state(
            universe,
            history[f"{prefix}_H"],
            history[f"{prefix}_C"],
            history[f"{prefix}_S"],
        )
    )
    return (
        ("surviving", full["surviving"]),
        ("M(C)", full["M(C)"]),
        ("E", full["E"]),
        ("entails", full["entails"]),
    )


def project_n0(universe: tuple[Valuation, ...], history: dict[str, Any]) -> FrameRecord:
    return rf.project_r0(universe, history)


def project_n1(universe: tuple[Valuation, ...], history: dict[str, Any]) -> FrameRecord:
    return (
        ("before", evaluated_state(universe, history, "before")),
        ("after", evaluated_state(universe, history, "after")),
    )


def project_n2(universe: tuple[Valuation, ...], history: dict[str, Any]) -> FrameRecord:
    return (
        ("before_typed", rf.raw_state(history, "before")),
        ("after_typed", rf.raw_state(history, "after")),
        ("changed_slots", rf.changed_slots(history)),
    )


def project_n3(universe: tuple[Valuation, ...], history: dict[str, Any]) -> FrameRecord:
    del universe
    return (
        ("identity", (history["original_id"], history["endpoint_id"])),
        ("same_identity", history["same_identity"]),
        ("original_status", history["original_status"]),
        ("endpoint_status", history["endpoint_status"]),
        ("successor", history["successor"]),
        ("segmentation", history["segmentation"]),
    )


def project_n4(universe: tuple[Valuation, ...], history: dict[str, Any]) -> FrameRecord:
    del universe
    return (("selection_provenance", history["provenance"]),)


def project_n5(universe: tuple[Valuation, ...], history: dict[str, Any]) -> FrameRecord:
    return rf.project_r0(universe, history) + (
        ("successor", history["successor"]),
        ("selection_provenance", history["provenance"]),
    )


PROJECTORS: dict[str, Projector] = {
    "N0": project_n0,
    "N1": project_n1,
    "N2": project_n2,
    "N3": project_n3,
    "N4": project_n4,
    "N5": project_n5,
}


def differing_fields(left: FrameRecord, right: FrameRecord) -> tuple[str, ...]:
    left_record = dict(left)
    right_record = dict(right)
    assert left_record.keys() == right_record.keys()
    return tuple(
        field for field in left_record if left_record[field] != right_record[field]
    )


def signature(
    universe: tuple[Valuation, ...],
    histories: dict[str, dict[str, Any]],
    pair: tuple[str, str],
    order: tuple[str, ...],
    projectors: dict[str, Projector],
) -> str:
    left, right = pair
    return "".join(
        "1"
        if projectors[frame](universe, histories[left])
        != projectors[frame](universe, histories[right])
        else "0"
        for frame in order
    )


def main() -> None:
    omega, histories = rf.build_histories()
    expected_histories = {
        "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8",
        "H9", "H10", "C-F", "C-D",
    }
    assert set(histories) == expected_histories
    assert histories["H9"]["provenance"] == "POST_HOC"
    assert histories["H10"]["provenance"] == "INDEPENDENT"
    assert histories["H5"]["successor"] == ("x0", "x1")
    assert histories["H6"]["successor"] is None

    r_order = tuple(rf.PROJECTORS)
    n_order = tuple(PROJECTORS)

    print("Pair | R-family | N-family")
    observed_n: dict[str, str] = {}
    for pair_name, pair in PAIRS.items():
        r_signature = signature(omega, histories, pair, r_order, rf.PROJECTORS)
        n_signature = signature(omega, histories, pair, n_order, PROJECTORS)
        assert r_signature == EXPECTED_R[pair_name]
        assert n_signature == EXPECTED_N[pair_name]
        observed_n[pair_name] = n_signature
        print(f"{pair_name} | {r_signature} | {n_signature}")

    print("\nVisible N-frame fields")
    for pair_name, (left, right) in PAIRS.items():
        entries = []
        for frame, projector in PROJECTORS.items():
            left_record = projector(omega, histories[left])
            right_record = projector(omega, histories[right])
            fields = differing_fields(left_record, right_record)
            if fields:
                entries.append(f"{frame}:{','.join(fields)}")
        print(f"{pair_name} | " + ("; ".join(entries) or "none"))

    # Provenance-only control: no other sparse frame separates H9/H10.
    assert observed_n["V5 H9/H10"] == "000011"
    # Syntax control: evaluated semantics collapse; raw syntax separates.
    assert observed_n["V6 H7/C-D"] == "001000"
    # Matched evaluated effect: carrier roles are erased in N1.
    assert project_n1(omega, histories["H9"]) == project_n1(
        omega, histories["H2"]
    )
    assert project_n2(omega, histories["H9"]) != project_n2(
        omega, histories["H2"]
    )

    # Non-monotonic display patterns occur once projector inheritance is absent.
    assert "101" in observed_n["V4 H5/H6"]
    assert "101" in observed_n["V8 H9/H2"]
    assert "10" in observed_n["V6 H7/C-D"]

    # A permutation changes sequence presentation but not per-frame visibility.
    permuted_order = ("N4", "N2", "N0", "N5", "N1", "N3")
    print("\nPermutation control: " + " ".join(permuted_order))
    changed_sequences = 0
    for pair_name, pair in PAIRS.items():
        original = observed_n[pair_name]
        permuted = signature(omega, histories, pair, permuted_order, PROJECTORS)
        visible_original = {
            frame for frame, bit in zip(n_order, original) if bit == "1"
        }
        visible_permuted = {
            frame for frame, bit in zip(permuted_order, permuted) if bit == "1"
        }
        assert visible_original == visible_permuted
        if original != permuted:
            changed_sequences += 1
        print(f"{pair_name} | {original} -> {permuted}")
    assert changed_sequences > 0

    print("\nAll non-nested projection and replication controls passed.")
    print("No frame, identity, provenance, or visibility basis was adjudicated.")


if __name__ == "__main__":
    main()

"""Mechanical checks for the cross-frame persistence test v0.1.

The checker reuses the frozen histories and R0--R4 projectors unchanged.  It
checks projection equality, field presence, and selected erasures only.  It
does not decide fundamentality, importance, identity, provenance, or whether
the common projection is canonical.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any, Iterable


BASE = Path(__file__).resolve().parent
_SPEC = importlib.util.spec_from_file_location(
    "record_frame_sensitivity_checker_v01",
    BASE / "proof_formation_record_frame_sensitivity_checker_v0.1.py",
)
assert _SPEC and _SPEC.loader
rf = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(rf)

FrameRecord = tuple[Any, ...]


def drop_fields(record: FrameRecord, names: Iterable[str]) -> FrameRecord:
    omitted = frozenset(names)
    return tuple(item for item in record if item[0] not in omitted)


def common_from_projection(frame: str, record: FrameRecord) -> FrameRecord:
    """Read the endpoint semantic pair actually available in every frame."""
    projected = dict(record)
    if frame == "R0":
        return (
            ("semantic_success", projected["semantic_success"]),
            ("counterexample_remains", projected["counterexample_remains"]),
        )
    after = dict(projected["after"])
    return (
        ("semantic_success", after["entails"]),
        ("counterexample_remains", bool(after["E"])),
    )


def semantic_change(record: FrameRecord) -> bool:
    projected = dict(record)
    return projected["before"] != projected["after"]


def common_projection(
    universe: tuple[tuple[int, ...], ...], history: dict[str, Any]
) -> FrameRecord:
    return rf.project_r0(universe, history)


def main() -> None:
    omega, histories = rf.build_histories()
    frames = tuple(rf.PROJECTORS)

    expected_success = {
        "H1", "H2", "H3", "H5", "H6", "H7", "H9", "H10", "C-D"
    }

    print("History | common endpoint projection")
    for name, history in histories.items():
        projections = {
            frame: rf.PROJECTORS[frame](omega, history) for frame in frames
        }
        extracted = {
            common_from_projection(frame, projections[frame]) for frame in frames
        }
        assert len(extracted) == 1
        common = extracted.pop()
        expected = (
            ("semantic_success", name in expected_success),
            ("counterexample_remains", name not in expected_success),
        )
        assert common == expected == common_projection(omega, history)
        print(f"{name} | {dict(common)}")

        # R0 has no before/after pair. R1--R4 do.
        assert "before" not in dict(projections["R0"])
        assert all(
            "before" in dict(projections[frame]) and "after" in dict(projections[frame])
            for frame in ("R1", "R2", "R3", "R4")
        )

        # Typed, history, and provenance fields first appear in R2, R3, and R4.
        assert "changed_slots" not in dict(projections["R1"])
        assert all(
            "changed_slots" in dict(projections[frame])
            for frame in ("R2", "R3", "R4")
        )
        assert "identity" not in dict(projections["R2"])
        assert all(
            "identity" in dict(projections[frame])
            for frame in ("R3", "R4")
        )
        assert "selection_provenance" not in dict(projections["R3"])
        assert "selection_provenance" in dict(projections["R4"])

        # E is recomputable from M(H), M(C), and S in every R1 after-state.
        after = dict(dict(projections["R1"])["after"])
        recomputed_e = (
            frozenset(after["M(H)"]) & frozenset(after["S"])
        ) - frozenset(after["M(C)"])
        assert recomputed_e == frozenset(after["E"])
        assert after["entails"] == (not recomputed_e)

    # Before/after semantic equality is available from R1 onward, not R0.
    assert semantic_change(rf.project_r1(omega, histories["H1"]))
    assert not semantic_change(rf.project_r1(omega, histories["H8"]))
    assert not semantic_change(rf.project_r1(omega, histories["C-F"]))

    # Raw syntax erased: equivalent insertion and verbatim insertion collapse.
    assert rf.project_r1(omega, histories["H7"]) == rf.project_r1(
        omega, histories["C-D"]
    )
    assert rf.project_r2(omega, histories["H7"]) != rf.project_r2(
        omega, histories["C-D"]
    )
    assert drop_fields(
        rf.project_r2(omega, histories["H7"]),
        {"before_typed", "after_typed", "changed_slots"},
    ) == drop_fields(
        rf.project_r2(omega, histories["C-D"]),
        {"before_typed", "after_typed", "changed_slots"},
    )

    # H/S carrier distinction erased: matched M1/scope effects collapse.
    assert rf.evaluated_effect(omega, histories["H9"]) == rf.evaluated_effect(
        omega, histories["H2"]
    )
    assert rf.project_r1(omega, histories["H9"]) != rf.project_r1(
        omega, histories["H2"]
    )

    # History/status erased: withdrawal/successor and continuation collapse.
    assert rf.project_r2(omega, histories["H5"]) == rf.project_r2(
        omega, histories["H6"]
    )
    assert rf.project_r3(omega, histories["H5"]) != rf.project_r3(
        omega, histories["H6"]
    )
    assert drop_fields(
        rf.project_r3(omega, histories["H5"]),
        {"identity", "same_identity", "original_status", "endpoint_status",
         "successor", "segmentation"},
    ) == drop_fields(
        rf.project_r3(omega, histories["H6"]),
        {"identity", "same_identity", "original_status", "endpoint_status",
         "successor", "segmentation"},
    )

    # Provenance erased: post-hoc and independent histories collapse.
    assert rf.project_r3(omega, histories["H9"]) == rf.project_r3(
        omega, histories["H10"]
    )
    assert rf.project_r4(omega, histories["H9"]) != rf.project_r4(
        omega, histories["H10"]
    )
    assert drop_fields(
        rf.project_r4(omega, histories["H9"]), {"selection_provenance"}
    ) == drop_fields(
        rf.project_r4(omega, histories["H10"]), {"selection_provenance"}
    )

    # Event occurrence is not shared observational content: +TRUE/no-event collapse.
    assert rf.project_r0(omega, histories["H8"]) == rf.project_r0(
        omega, histories["C-F"]
    )
    assert rf.project_r1(omega, histories["H8"]) == rf.project_r1(
        omega, histories["C-F"]
    )
    assert rf.project_r2(omega, histories["H8"]) != rf.project_r2(
        omega, histories["C-F"]
    )

    # The common endpoint pair deliberately collapses the required route pairs.
    for left, right in (
        ("H1", "H2"), ("H1", "H3"), ("H4", "C-F"),
        ("H5", "H6"), ("H9", "H10"), ("H8", "C-F"),
    ):
        assert common_projection(omega, histories[left]) == common_projection(
            omega, histories[right]
        )

    print("All cross-frame persistence and erasure checks passed.")
    print("No invariant, frame preference, or historical legitimacy was decided.")


if __name__ == "__main__":
    main()

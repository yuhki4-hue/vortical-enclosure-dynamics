"""Mechanical checks for the minimal separating field-set test v0.1.

The checker imports the existing frozen histories, extracts already-existing
record information into test-local atomic coordinates, and compares selected
coordinate projections.  It does not judge explanatory relevance, field
importance, identity, provenance, action ontology, or record design.
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

Valuation = tuple[int, ...]
AtomicRecord = dict[str, Any]


SEMANTIC_FIELDS = (
    "endpoint_entails",
    "endpoint_counterexample_remains",
    "before_surviving",
    "after_surviving",
    "before_target_models",
    "after_target_models",
    "before_E",
    "after_E",
    "before_scope",
    "after_scope",
    "before_assumption_models",
    "after_assumption_models",
)

RAW_FIELDS = (
    "raw_before_H",
    "raw_after_H",
    "raw_before_C",
    "raw_after_C",
    "raw_before_S",
    "raw_after_S",
    "changed_slots",
)

HISTORY_FIELDS = (
    "original_id",
    "endpoint_id",
    "same_identity",
    "original_status",
    "endpoint_status",
    "successor",
    "segmentation",
)

PROVENANCE_FIELDS = ("selection_provenance",)
ATOMIC_FIELDS = SEMANTIC_FIELDS + RAW_FIELDS + HISTORY_FIELDS + PROVENANCE_FIELDS

EVALUATED_EFFECT_FIELDS = (
    "endpoint_entails",
    "endpoint_counterexample_remains",
    "before_surviving",
    "after_surviving",
    "before_target_models",
    "after_target_models",
    "before_E",
    "after_E",
)

PAIRS = {
    "D1 H4/C-F": ("H4", "C-F"),
    "D2 H5/H6": ("H5", "H6"),
    "D3 H9/H10": ("H9", "H10"),
    "D4 H7/C-D": ("H7", "C-D"),
    "D5 H8/C-F": ("H8", "C-F"),
    "D6 H9/H2": ("H9", "H2"),
    "D7 H1/H3": ("H1", "H3"),
    "D8 H5/H1": ("H5", "H1"),
}

EXPECTED_SINGLETONS = {
    "D1 H4/C-F": (
        "same_identity", "original_status", "endpoint_status", "segmentation"
    ),
    "D2 H5/H6": (
        "endpoint_id", "same_identity", "original_status", "successor",
        "segmentation",
    ),
    "D3 H9/H10": ("selection_provenance",),
    "D4 H7/C-D": ("raw_after_H",),
    "D5 H8/C-F": (
        "raw_after_H", "changed_slots", "same_identity", "segmentation",
        "selection_provenance",
    ),
    "D6 H9/H2": (
        "after_scope", "after_assumption_models", "raw_after_H",
        "raw_after_S", "changed_slots", "selection_provenance",
    ),
    "D7 H1/H3": (
        "after_surviving", "after_target_models", "after_assumption_models",
        "raw_after_H", "raw_after_C", "changed_slots",
        "selection_provenance",
    ),
    "D8 H5/H1": (
        "endpoint_id", "same_identity", "original_status", "successor",
        "segmentation", "selection_provenance",
    ),
}


def atomic_record(
    universe: tuple[Valuation, ...], history: dict[str, Any]
) -> AtomicRecord:
    before = dict(
        rf.semantic_state(
            universe,
            history["before_H"],
            history["before_C"],
            history["before_S"],
        )
    )
    after = dict(
        rf.semantic_state(
            universe,
            history["after_H"],
            history["after_C"],
            history["after_S"],
        )
    )
    raw_before = dict(rf.raw_state(history, "before"))
    raw_after = dict(rf.raw_state(history, "after"))

    record = {
        "endpoint_entails": after["entails"],
        "endpoint_counterexample_remains": bool(after["E"]),
        "before_surviving": before["surviving"],
        "after_surviving": after["surviving"],
        "before_target_models": before["M(C)"],
        "after_target_models": after["M(C)"],
        "before_E": before["E"],
        "after_E": after["E"],
        "before_scope": before["S"],
        "after_scope": after["S"],
        "before_assumption_models": before["M(H)"],
        "after_assumption_models": after["M(H)"],
        "raw_before_H": raw_before["H"],
        "raw_after_H": raw_after["H"],
        "raw_before_C": raw_before["C"],
        "raw_after_C": raw_after["C"],
        "raw_before_S": raw_before["S"],
        "raw_after_S": raw_after["S"],
        "changed_slots": rf.changed_slots(history),
        "original_id": history["original_id"],
        "endpoint_id": history["endpoint_id"],
        "same_identity": history["same_identity"],
        "original_status": history["original_status"],
        "endpoint_status": history["endpoint_status"],
        "successor": history["successor"],
        "segmentation": history["segmentation"],
        "selection_provenance": history["provenance"],
    }
    assert tuple(record) == ATOMIC_FIELDS
    return record


def projection(record: AtomicRecord, fields: Iterable[str]) -> tuple[Any, ...]:
    selected = tuple(fields)
    return tuple((field, record[field]) for field in selected)


def separates(left: AtomicRecord, right: AtomicRecord, fields: Iterable[str]) -> bool:
    selected = tuple(fields)
    return projection(left, selected) != projection(right, selected)


def differing_singletons(left: AtomicRecord, right: AtomicRecord) -> tuple[str, ...]:
    return tuple(field for field in ATOMIC_FIELDS if left[field] != right[field])


def raw_changed_slots(record: AtomicRecord) -> tuple[str, ...]:
    return tuple(
        slot
        for slot, before, after in (
            ("H", record["raw_before_H"], record["raw_after_H"]),
            ("C", record["raw_before_C"], record["raw_after_C"]),
            ("S", record["raw_before_S"], record["raw_after_S"]),
        )
        if before != after
    )


def main() -> None:
    omega, histories = rf.build_histories()
    assert set(histories) == {
        "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8",
        "H9", "H10", "C-F", "C-D",
    }
    records = {
        name: atomic_record(omega, history) for name, history in histories.items()
    }

    # Derivational and exact-representation dependencies in this finite record.
    for record in records.values():
        assert record["endpoint_entails"] == (not record["after_E"])
        assert record["endpoint_counterexample_remains"] == bool(record["after_E"])
        assert frozenset(record["before_surviving"]) == (
            frozenset(record["before_assumption_models"])
            & frozenset(record["before_scope"])
        )
        assert frozenset(record["after_surviving"]) == (
            frozenset(record["after_assumption_models"])
            & frozenset(record["after_scope"])
        )
        assert frozenset(record["before_E"]) == (
            frozenset(record["before_surviving"])
            - frozenset(record["before_target_models"])
        )
        assert frozenset(record["after_E"]) == (
            frozenset(record["after_surviving"])
            - frozenset(record["after_target_models"])
        )
        assert record["before_scope"] == record["raw_before_S"]
        assert record["after_scope"] == record["raw_after_S"]
        assert record["changed_slots"] == raw_changed_slots(record)

    # A naive id-equality calculation cannot replace the stored assertion for
    # all frozen records: C-F explicitly leaves same_identity unspecified.
    assert records["C-F"]["original_id"] == records["C-F"]["endpoint_id"]
    assert records["C-F"]["same_identity"] is None

    print("Pair | separating singleton fields")
    observed: dict[str, tuple[str, ...]] = {}
    for pair_name, (left_name, right_name) in PAIRS.items():
        left = records[left_name]
        right = records[right_name]
        fields = differing_singletons(left, right)
        assert fields == EXPECTED_SINGLETONS[pair_name]
        observed[pair_name] = fields
        assert fields

        # Each unequal singleton separates; deleting its only field collapses.
        for field in fields:
            assert separates(left, right, (field,))
            assert not separates(left, right, ())

        # Full atomic record separates, while every non-differing singleton
        # collapses.  No powerset enumeration is needed.
        assert separates(left, right, ATOMIC_FIELDS)
        for field in ATOMIC_FIELDS:
            assert separates(left, right, (field,)) == (field in fields)
        print(pair_name + " | " + ", ".join(fields))

    # D3: provenance-only positive control.
    d3_left, d3_right = (records[name] for name in PAIRS["D3 H9/H10"])
    assert separates(d3_left, d3_right, PROVENANCE_FIELDS)
    assert not separates(d3_left, d3_right, SEMANTIC_FIELDS)
    assert not separates(d3_left, d3_right, RAW_FIELDS)
    assert not separates(d3_left, d3_right, HISTORY_FIELDS)

    # D4: raw formula content, not changed-slot shape, separates.
    d4_left, d4_right = (records[name] for name in PAIRS["D4 H7/C-D"])
    assert separates(d4_left, d4_right, ("raw_after_H",))
    assert not separates(d4_left, d4_right, ("raw_before_H",))
    assert not separates(d4_left, d4_right, ("changed_slots",))
    assert not separates(d4_left, d4_right, ("after_assumption_models",))

    # D5: several distinct stored or derived singleton cues separate, but
    # endpoint semantics and endpoint research status do not.
    d5_left, d5_right = (records[name] for name in PAIRS["D5 H8/C-F"])
    for field in (
        "raw_after_H", "changed_slots", "same_identity", "segmentation",
        "selection_provenance",
    ):
        assert separates(d5_left, d5_right, (field,))
    for field in (
        "endpoint_entails", "endpoint_counterexample_remains", "endpoint_status"
    ):
        assert not separates(d5_left, d5_right, (field,))
    assert not separates(d5_left, d5_right, SEMANTIC_FIELDS)

    # D6: evaluated effect collapses; carrier, raw, and provenance singletons
    # supply several different separating bases.
    d6_left, d6_right = (records[name] for name in PAIRS["D6 H9/H2"])
    assert not separates(d6_left, d6_right, EVALUATED_EFFECT_FIELDS)
    assert separates(d6_left, d6_right, ("after_assumption_models",))
    assert separates(d6_left, d6_right, ("after_scope",))
    assert separates(d6_left, d6_right, ("raw_after_H",))
    assert separates(d6_left, d6_right, ("raw_after_S",))
    assert separates(d6_left, d6_right, ("changed_slots",))
    assert separates(d6_left, d6_right, ("selection_provenance",))
    assert not separates(d6_left, d6_right, HISTORY_FIELDS)

    # D7: changed_slots is a typed difference cue, not an action adjudicator.
    d7_left, d7_right = (records[name] for name in PAIRS["D7 H1/H3"])
    for field in (
        "after_assumption_models", "after_target_models", "after_surviving",
        "raw_after_H", "raw_after_C", "changed_slots",
    ):
        assert separates(d7_left, d7_right, (field,))
    assert not separates(d7_left, d7_right, ("after_E",))

    # With coordinate projections, every separating set contains at least one
    # differing singleton.  Hence all tested inclusion-minimal sets here are
    # singleton sets; this is an implementation consequence, not a ranking.
    for pair_name, (left_name, right_name) in PAIRS.items():
        left = records[left_name]
        right = records[right_name]
        fields = observed[pair_name]
        for field in fields:
            assert separates(left, right, (field,))

    print("\nAll atomic projection, ablation, and derived-field checks passed.")
    print("Minimality reduced to unequal singleton fields under this projection rule.")
    print("No explanatory relevance, necessity, or field preference was decided.")


if __name__ == "__main__":
    main()

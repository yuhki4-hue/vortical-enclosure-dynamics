#!/usr/bin/env python3
"""
Validate docs/ai_spine Layer 0-1 and emit generated calibration outputs.

This script machine-validates Layer 0-1 only. It does NOT enforce Layer 2
frame claims (advisory_links are never existence-checked) and does NOT
implement Layer 3 evaluation, scoring, or interpretation.

Layer 1 now carries term `kind` and `derivation_role` as calibration
metadata, plus non-generative `validated_relations`. Type is constrained;
interpretation is not.

Each check below owns a dedicated error list. A failure in one check must
never change the reported status of another: the `checks` array is meant to
localize failures, not broadcast a single pass/fail bit across every id.
"""

from __future__ import annotations

import json
import pathlib
import sys
from typing import Any

try:
    from jsonschema import Draft202012Validator
    _HAVE_JSONSCHEMA = True
except Exception:
    _HAVE_JSONSCHEMA = False


ROOT = pathlib.Path(__file__).resolve().parents[2]
SPINE_DIR = pathlib.Path(__file__).resolve().parent
SPINE_PATH = SPINE_DIR / "spine.json"
SCHEMA_PATH = SPINE_DIR / "spine.schema.json"
GENERATED_DIR = SPINE_DIR / "generated"

BACKBONE_KINDS = {"axiom", "variable", "relation", "process",
                  "recursive_process", "regime", "boundary_condition"}
ALLOWED_RELATIONS = {"accumulation_structure", "structural_extension_of"}
LAYER2_DOC_MARKERS = ("name_misreadings", "common_misreadings", "conceptual_neighbors")


def load_json(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def add_error(errors: list[str], message: str) -> None:
    errors.append(message)


def check_status(errs: list[str]) -> str:
    return "pass" if not errs else "fail"


def validate_schema(spine: dict[str, Any], errors: list[str]) -> str:
    """errors here is a check-local list — only schema errors ever land in it."""
    if not _HAVE_JSONSCHEMA:
        return "skipped"
    schema = load_json(SCHEMA_PATH)
    for e in Draft202012Validator(schema).iter_errors(spine):
        add_error(errors, f"schema: {list(e.path)}: {e.message}")
    return "fail" if errors else "pass"


def schema_check(schema_status: str, schema_errors: list[str]) -> dict[str, Any]:
    check = {
        "id": "schema",
        "description": "spine.json conforms to spine.schema.json.",
        "status": schema_status,
    }
    if schema_status == "skipped":
        # Skipped is a fact about this check alone; it holds regardless of
        # what any other check does, and must not be overwritten by errors
        # that happened elsewhere.
        check.update({
            "reason": "optional dependency 'jsonschema' not installed",
            "severity": "advisory",
            "remedy": "pip install -r docs/ai_spine/requirements.txt",
            "note": (
                "Does not affect layer_policy, layer0_paths, "
                "canonical_derivation_order, term_types, or "
                "non_generative_relations, which use independent validation "
                "logic."
            ),
        })
    return check


def validate_layer_policy(spine: dict[str, Any], errors: list[str]) -> None:
    policy = spine.get("layer_policy", {})
    if policy.get("machine_validated") != [0, 1]:
        add_error(errors, "Layer policy must machine-validate only layers [0, 1].")
    if policy.get("not_enforced") != [2]:
        add_error(errors, "Layer policy must mark layer [2] as not enforced.")
    if policy.get("absent") != [3]:
        add_error(errors, "Layer policy must mark layer [3] as absent.")
    if "frame" in spine:
        add_error(errors, "Layer 2 frame claims must not be encoded as a top-level frame block.")
    if "layer2" in spine:
        add_error(errors, "Layer 2 data must not be enforced by docs/ai_spine.")
    if "layer3" in spine:
        add_error(errors, "Layer 3 must remain absent.")


def validate_layer0(spine: dict[str, Any], errors: list[str]) -> None:
    layer0 = spine.get("layer0", {})
    for item in layer0.get("calibration_paths", []):
        path = item.get("path")
        if not path:
            add_error(errors, "Layer 0 calibration path is missing a path value.")
            continue
        # regression guard: Layer 2 docs must never be machine-validated calibration paths
        if any(marker in path for marker in LAYER2_DOC_MARKERS):
            add_error(errors, f"Layer 2 doc must not appear in calibration_paths: {path}")
        if not (ROOT / path).exists():
            add_error(errors, f"Layer 0 path does not exist: {path}")
    # advisory_links are intentionally NOT existence-checked.


def validate_layer1(
    spine: dict[str, Any],
    order_errors: list[str],
    term_errors: list[str],
    relation_errors: list[str],
) -> dict[str, Any]:
    layer1 = spine.get("layer1", {})
    order = layer1.get("canonical_derivation_order", [])
    boundary = layer1.get("boundary_terms", [])
    relations = layer1.get("validated_relations", [])

    if not order:
        add_error(order_errors, "Layer 1 canonical_derivation_order is empty.")
        return {"order": [], "boundary": boundary, "relations": relations}

    ranks = [item.get("rank") for item in order]
    if ranks != list(range(len(order))):
        add_error(order_errors, f"Layer 1 ranks must be consecutive {list(range(len(order)))}, got {ranks}.")

    ids = [item.get("id") for item in order]
    if len(ids) != len(set(ids)):
        add_error(order_errors, "canonical_derivation_order contains duplicate ids.")

    # rank 0 = sole axiom `difference`
    first = order[0]
    if first.get("id") != "difference" or first.get("rank") != 0:
        add_error(order_errors, "Layer 1 rank 0 must be the sole axiom `difference`.")
    if first.get("kind") != "axiom" or first.get("derivation_role") != "origin":
        add_error(order_errors, "`difference` must have kind=axiom and derivation_role=origin.")

    axioms = [it for it in order if it.get("kind") == "axiom"]
    if len(axioms) != 1 or axioms[0].get("id") != "difference":
        add_error(order_errors, "Exactly one axiom is allowed and it must be `difference`.")

    # c_ij = rank 1, a variable, the first formal carrier, NOT a second axiom
    c_ij = next((it for it in order if it.get("id") == "c_ij"), None)
    if c_ij is None:
        add_error(order_errors, "Layer 1 must include `c_ij` at rank 1.")
    else:
        if c_ij.get("rank") != 1:
            add_error(order_errors, "`c_ij` must have rank 1.")
        if c_ij.get("kind") != "variable":
            add_error(order_errors, "`c_ij` must have kind=variable (it is not a second axiom).")
        if c_ij.get("derivation_role") != "first_formal_carrier":
            add_error(order_errors, "`c_ij` derivation_role must be `first_formal_carrier`.")

    for item in order:
        if item.get("kind") not in BACKBONE_KINDS:
            add_error(term_errors, f"Invalid kind for {item.get('id')}: {item.get('kind')}")
        if item.get("status") not in {"confirmed", "proposed"}:
            add_error(term_errors, f"Invalid status for {item.get('id')}: {item.get('status')}")

    # boundary terms: typed, off-backbone, no rank, no id collision with backbone
    backbone_ids = set(ids)
    boundary_ids = set()
    for b in boundary:
        bid = b.get("id")
        if bid in backbone_ids:
            add_error(term_errors, f"boundary_term `{bid}` collides with a backbone rank id.")
        boundary_ids.add(bid)

    known_ids = backbone_ids | boundary_ids

    # relations: must be non-generative and must NOT occupy a rank
    for rel in relations:
        f, t, kind = rel.get("from"), rel.get("to"), rel.get("relation")
        if f not in known_ids:
            add_error(relation_errors, f"relation.from unknown id: {f}")
        if t not in known_ids:
            add_error(relation_errors, f"relation.to unknown id: {t}")
        if kind not in ALLOWED_RELATIONS:
            add_error(relation_errors, f"relation type not allowed: {kind}")
        if rel.get("generative") is not False:
            add_error(relation_errors, f"validated_relations must be non-generative "
                              f"(generative=false); generative steps belong in the "
                              f"canonical order: {f}->{t}")
        # the core invariant: a non-generative relation cannot point at a ranked term
        if t in backbone_ids:
            add_error(relation_errors, f"non-generative relation must not target a ranked "
                              f"backbone term (would raise rank): {f}->{t}")

    return {"order": order, "boundary": boundary, "relations": relations}


def validate_layer3_absence(errors: list[str]) -> None:
    layer3_files = sorted(SPINE_DIR.glob("*layer3*")) + sorted(SPINE_DIR.glob("*eval*"))
    layer3_files = [p for p in layer3_files if p.name != "validation_report.json"]
    if layer3_files:
        names = ", ".join(p.name for p in layer3_files)
        add_error(errors, f"Layer 3-like files must not exist in docs/ai_spine: {names}")


def generated_order_json(data: dict[str, Any]) -> dict[str, Any]:
    return {
        "generated_by": "docs/ai_spine/validate.py",
        "source": "docs/ai_spine/spine.json",
        "validated_layers": [0, 1],
        "not_enforced_layers": [2],
        "absent_layers": [3],
        "canonical_derivation_order": data["order"],
        "boundary_terms": data["boundary"],
        "validated_relations": data["relations"],
    }


def generated_order_markdown(data: dict[str, Any]) -> str:
    order = data["order"]
    lines = [
        "# Canonical Derivation Order",
        "",
        "Generated by `docs/ai_spine/validate.py` from `docs/ai_spine/spine.json`.",
        "",
        "- Validated layers: 0-1",
        "- Layer 2 frame claims: not enforced here",
        "- Layer 3: absent",
        "",
        "## Backbone (ranked)",
        "",
        "| Rank | ID | Label | Kind | Derivation role | Status |",
        "|---:|---|---|---|---|---|",
    ]
    for it in order:
        lines.append(
            f"| {it['rank']} | `{it['id']}` | {it['label']} | `{it['kind']}` | "
            f"`{it['derivation_role']}` | {it['status']} |"
        )
    if data["boundary"]:
        lines += ["", "## Boundary terms (off-backbone, no rank)", "",
                  "| ID | Label | Kind | Status |", "|---|---|---|---|"]
        for b in data["boundary"]:
            lines.append(f"| `{b['id']}` | {b['label']} | `{b['kind']}` | {b['status']} |")
    if data["relations"]:
        lines += ["", "## Validated relations (non-generative — do not raise rank)", "",
                  "| From | Relation | To | Generative | Status |",
                  "|---|---|---|:--:|---|"]
        for r in data["relations"]:
            lines.append(f"| `{r['from']}` | `{r['relation']}` | `{r['to']}` | "
                         f"{str(r['generative']).lower()} | {r['status']} |")
    lines.append("")
    return "\n".join(lines)


def write_generated_outputs(
    data: dict[str, Any],
    schema_status: str,
    schema_errors: list[str],
    policy_errors: list[str],
    layer0_errors: list[str],
    order_errors: list[str],
    term_errors: list[str],
    relation_errors: list[str],
    layer3_errors: list[str],
) -> list[str]:
    all_errors = (schema_errors + policy_errors + layer0_errors
                  + order_errors + term_errors + relation_errors + layer3_errors)
    status = "fail" if all_errors else "pass"
    checks = [
        schema_check(schema_status, schema_errors),
        {"id": "layer_policy", "description": "Only Layer 0-1 machine-validated; Layer 2 not enforced; Layer 3 absent.", "status": check_status(policy_errors)},
        {"id": "layer0_paths", "description": "Calibration paths exist; no Layer 2 doc among them.", "status": check_status(layer0_errors)},
        {"id": "canonical_derivation_order", "description": "Ranks consecutive; begins with `difference`; `c_ij` rank 1 variable.", "status": check_status(order_errors)},
        {"id": "term_types", "description": "Every backbone term carries a valid kind and derivation_role.", "status": check_status(term_errors)},
        {"id": "non_generative_relations", "description": "validated_relations are non-generative and never occupy a rank.", "status": check_status(relation_errors)},
        {"id": "layer3_absence", "description": "No Layer 3-like evaluation/scoring files exist in docs/ai_spine.", "status": check_status(layer3_errors)},
    ]
    report = {
        "generated_by": "docs/ai_spine/validate.py",
        "source": "docs/ai_spine/spine.json",
        "status": status,
        "validated_layers": [0, 1],
        "not_enforced_layers": [2],
        "absent_layers": [3],
        "checks": checks,
        "errors": all_errors,
    }
    GENERATED_DIR.mkdir(exist_ok=True)
    (GENERATED_DIR / "canonical_derivation_order.json").write_text(
        json.dumps(generated_order_json(data), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (GENERATED_DIR / "canonical_derivation_order.md").write_text(
        generated_order_markdown(data), encoding="utf-8")
    (GENERATED_DIR / "validation_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return all_errors


def main() -> int:
    spine = load_json(SPINE_PATH)

    schema_errors: list[str] = []
    policy_errors: list[str] = []
    layer0_errors: list[str] = []
    order_errors: list[str] = []
    term_errors: list[str] = []
    relation_errors: list[str] = []
    layer3_errors: list[str] = []

    schema_status = validate_schema(spine, schema_errors)
    validate_layer_policy(spine, policy_errors)
    validate_layer0(spine, layer0_errors)
    data = validate_layer1(spine, order_errors, term_errors, relation_errors)
    validate_layer3_absence(layer3_errors)

    all_errors = write_generated_outputs(
        data, schema_status, schema_errors, policy_errors, layer0_errors,
        order_errors, term_errors, relation_errors, layer3_errors,
    )

    if all_errors:
        print("FAIL - docs/ai_spine validation errors:")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print("PASS - docs/ai_spine Layer 0-1 validation complete.")
    print("Generated:")
    print("- docs/ai_spine/generated/canonical_derivation_order.md")
    print("- docs/ai_spine/generated/canonical_derivation_order.json")
    print("- docs/ai_spine/generated/validation_report.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())

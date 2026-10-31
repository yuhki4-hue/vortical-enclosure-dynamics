#!/usr/bin/env python3
"""
Validate docs/ai_spine Layer 0-1 and emit generated calibration outputs.

This script machine-validates Layer 0-1 only. It does NOT enforce Layer 2
frame claims (advisory_links are never existence-checked) and does NOT
implement Layer 3 evaluation, scoring, or interpretation.

Layer 1 carries legacy-compatible ranked navigation metadata, term `kind` and
source-local `derivation_role`, non-generative `validated_relations`, and the
canonical relation-role inventory. It does not validate proof order, bridge
completion, physical generation, or ontology.

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
ALLOWED_RELATIONS = {
    "accumulation_structure",
    "structural_extension_of",
    "proposed_correspondence",
}
ALLOWED_ROLE_CLASSES = {
    "source_local_navigation",
    "formal_construction",
    "effective_relation",
    "open_bridge",
    "candidate_physical_interpretation",
}
ALLOWED_BRIDGE_STATUS = {"not_applicable", "open", "partial_open"}
ALLOWED_PHYSICAL_STATUS = {"not_established", "not_implied", "candidate", "open"}
OPEN_BRIDGE_CANDIDATES = {
    "RC-005", "RC-006", "RC-007", "RC-008",
    "RC-009", "RC-010", "RC-040", "RC-041",
}
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
                "canonical_navigation_order, term_types, relation-role "
                "inventory, or non_generative_relations, which use independent validation "
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
    inventory_errors: list[str],
) -> dict[str, Any]:
    layer1 = spine.get("layer1", {})
    semantics = layer1.get("sequence_semantics", {})
    order = layer1.get("canonical_derivation_order", [])
    boundary = layer1.get("boundary_terms", [])
    relations = layer1.get("validated_relations", [])
    inventory = layer1.get("relation_role_inventory", [])

    if semantics.get("interpreted_as") != "navigation_order":
        add_error(order_errors, "Layer 1 sequence must be interpreted as navigation_order.")
    if semantics.get("uniform_arrow_semantics") is not False:
        add_error(order_errors, "Layer 1 must explicitly reject uniform arrow semantics.")
    if semantics.get("status_semantics") != "source_local_documentary_role_only":
        add_error(order_errors, "Backbone status must mean source-local documentary role only, not physical confirmation.")
    if semantics.get("application_inference") != "not_implied":
        add_error(order_errors, "Layer 1 navigation must not imply application-layer generation or stopping necessity.")
    if semantics.get("canonical_role_table") != "docs/navigation/generative_sequence.md":
        add_error(order_errors, "Layer 1 canonical role table must point to docs/navigation/generative_sequence.md.")
    if set(semantics.get("open_bridge_candidates", [])) != OPEN_BRIDGE_CANDIDATES:
        add_error(order_errors, "Layer 1 must preserve the eight audited OPEN bridge candidates.")

    if not order:
        add_error(order_errors, "Layer 1 canonical_derivation_order is empty.")
        return {
            "semantics": semantics,
            "order": [],
            "boundary": boundary,
            "relations": relations,
            "inventory": inventory,
        }

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
        if c_ij.get("derivation_role") != "source_local_first_carrier":
            add_error(order_errors, "c_ij derivation_role must be source_local_first_carrier.")

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

    # relations: source-local or proposed correspondences; never a ranked proof step
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
                              f"(generative=false): {f}->{t}")
        # A non-generative cross-reference cannot promote a boundary item into the
        # ranked navigation backbone.
        if t in backbone_ids:
            add_error(relation_errors, f"non-generative relation must not target a ranked "
                              f"backbone term (would raise rank): {f}->{t}")

    expected_inventory_ids = {f"N{i:02d}" for i in range(1, 23)}
    inventory_ids = [item.get("id") for item in inventory]
    if set(inventory_ids) != expected_inventory_ids or len(inventory_ids) != len(expected_inventory_ids):
        add_error(inventory_errors, "relation_role_inventory must contain unique N01-N22 entries.")
    for item in inventory:
        rid = item.get("id")
        roles = item.get("role_classes", [])
        invalid_roles = set(roles) - ALLOWED_ROLE_CLASSES
        if invalid_roles:
            add_error(inventory_errors, f"Invalid role class for {rid}: {sorted(invalid_roles)}")
        bridge_status = item.get("bridge_status")
        if bridge_status not in ALLOWED_BRIDGE_STATUS:
            add_error(inventory_errors, f"Invalid bridge status for {rid}: {bridge_status}")
        physical_status = item.get("physical_status")
        if physical_status not in ALLOWED_PHYSICAL_STATUS:
            add_error(inventory_errors, f"Invalid physical status for {rid}: {physical_status}")
        if bridge_status in {"open", "partial_open"} and "open_bridge" not in roles:
            add_error(inventory_errors, f"Open bridge row {rid} must carry role class open_bridge.")

    return {
        "semantics": semantics,
        "order": order,
        "boundary": boundary,
        "relations": relations,
        "inventory": inventory,
    }


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
        "sequence_semantics": data["semantics"],
        "canonical_navigation_order": data["order"],
        "canonical_derivation_order": data["order"],
        "legacy_compatibility": (
            "canonical_derivation_order and the generated filename are retained for "
            "compatibility; ranks are navigation indices, not proof or physical-generation steps."
        ),
        "boundary_terms": data["boundary"],
        "validated_relations": data["relations"],
        "relation_role_inventory": data["inventory"],
    }


def generated_order_markdown(data: dict[str, Any]) -> str:
    order = data["order"]
    semantics = data["semantics"]
    lines = [
        "# AI Spine Navigation Calibration",
        "",
        "Generated by `docs/ai_spine/validate.py` from `docs/ai_spine/spine.json`.",
        "",
        "- Validated layers: 0-1",
        "- Layer 2 frame claims: not enforced here",
        "- Layer 3: absent",
        "- Ranked sequence meaning: navigation / presentation order",
        "- Uniform arrow semantics: rejected",
        "- `confirmed` status: source-local documentary role only; not physical confirmation",
        "- Application-layer generation or stopping necessity: not implied by this ranking",
        "- Canonical relation-role table: " + semantics.get("canonical_role_table", "unresolved"),
        "- The legacy generated filename is retained for compatibility.",
        "",
        "This ranked list is not a proof order, uniform formal dependency, causal mechanism, or physical-generation result.",
        "",
        "## Backbone (ranked navigation order)",
        "",
        "| Rank | ID | Label | Kind | Local stage role | Status |",
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
        lines += ["", "## Source-local and proposed relations (non-generative — do not raise rank)", "",
                  "| From | Relation | To | Generative | Status |",
                  "|---|---|---|:--:|---|"]
        for r in data["relations"]:
            lines.append(f"| `{r['from']}` | `{r['relation']}` | `{r['to']}` | "
                         f"{str(r['generative']).lower()} | {r['status']} |")
    if data["inventory"]:
        lines += ["", "## Canonical relation-role inventory", "",
                  "| ID | From | To | Role classes | Bridge status | Physical status |",
                  "|---|---|---|---|---|---|"]
        for item in data["inventory"]:
            roles = ", ".join(item["role_classes"])
            lines.append(
                f"| `{item['id']}` | {item['from']} | {item['to']} | "
                f"{roles} | `{item['bridge_status']}` | `{item['physical_status']}` |"
            )
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
    inventory_errors: list[str],
    layer3_errors: list[str],
) -> list[str]:
    all_errors = (schema_errors + policy_errors + layer0_errors
                  + order_errors + term_errors + relation_errors
                  + inventory_errors + layer3_errors)
    status = "fail" if all_errors else "pass"
    checks = [
        schema_check(schema_status, schema_errors),
        {"id": "layer_policy", "description": "Only Layer 0-1 machine-validated; Layer 2 not enforced; Layer 3 absent.", "status": check_status(policy_errors)},
        {"id": "layer0_paths", "description": "Calibration paths exist; no Layer 2 doc among them.", "status": check_status(layer0_errors)},
        {"id": "canonical_navigation_order", "description": "Ranks are consecutive presentation indices; the sequence rejects uniform proof or generation semantics.", "status": check_status(order_errors)},
        {"id": "term_types", "description": "Every backbone term carries a valid kind and source-local stage role.", "status": check_status(term_errors)},
        {"id": "non_generative_relations", "description": "Source-local and proposed relations are non-generative and never occupy a rank.", "status": check_status(relation_errors)},
        {"id": "relation_role_inventory", "description": "N01-N22 carry valid local role, bridge, and physical-status metadata.", "status": check_status(inventory_errors)},
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
    inventory_errors: list[str] = []
    layer3_errors: list[str] = []

    schema_status = validate_schema(spine, schema_errors)
    validate_layer_policy(spine, policy_errors)
    validate_layer0(spine, layer0_errors)
    data = validate_layer1(
        spine, order_errors, term_errors, relation_errors, inventory_errors
    )
    validate_layer3_absence(layer3_errors)

    all_errors = write_generated_outputs(
        data, schema_status, schema_errors, policy_errors, layer0_errors,
        order_errors, term_errors, relation_errors, inventory_errors, layer3_errors,
    )

    if all_errors:
        print("FAIL - docs/ai_spine validation errors:")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print("PASS - docs/ai_spine Layer 0-1 navigation validation complete.")
    print("Generated:")
    print("- docs/ai_spine/generated/canonical_derivation_order.md")
    print("- docs/ai_spine/generated/canonical_derivation_order.json")
    print("- docs/ai_spine/generated/validation_report.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())

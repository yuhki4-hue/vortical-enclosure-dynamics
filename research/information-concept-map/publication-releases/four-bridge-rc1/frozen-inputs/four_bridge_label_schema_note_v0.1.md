# Label Schema Note v0.1 (four bridges)

Status: `SCHEMA-NOTE`. Governing decision: H-V4B-12-M1-B-REVISED §4 (with HR-IMPL-5-B). Canonical effect **NONE**.

## Label fields in `english_data_draft_v0.7.tsv`

| Field | Role | Determines a display name? |
|---|---|---|
| `publication_label` | canonical display name in the **publication** scope | **yes**: publication scope |
| `reconstruction_label` | canonical display name in the **English reconstruction** scope | **yes**: reconstruction scope |
| `working_label` | existing working name, kept as it is | **no** |
| `stable_label_id` | stable ID linking the two scoped labels (e.g. `R0-COUPLING`) | no; it is an identifier |

## Rules

1. **Do not infer display names from `working_label`.**
   - A renderer or edge table that needs a display name reads `publication_label` or `reconstruction_label` according to the display scope.
   - It does not read `working_label`, or `short_name` derived from it.
2. **Scope decides the label.** The scope-label table (`four_bridge_scope_labels_v0.3.tsv`, column `canonical_display_field`) states which field governs each scope.
3. **A label is not a condition.**
   - The reconstruction label `causal coupling` names the English reconstruction view of R0. It does not add a condition.
   - It is not part of the Japanese R0 definition.
4. **Stable IDs and label mappings are unchanged** by this note.

## R0 values (for reference)

| Field | Value |
|---|---|
| `publication_label` | Interaction |
| `reconstruction_label` | causal coupling |
| `working_label` | interaction |
| `stable_label_id` | R0-COUPLING |

## Known place where the rule is not yet followed (reported, not changed)

`english_data_edges_v0.5.tsv`, E2-001:
- `target_short_name` = “R0-COUPLING — interaction”;
- `display_name_scope` = `RECONSTRUCTION-DISPLAY`;
- `display_name_source` = `english_data_draft_v0.6.tsv:short_name`.

Under rule 1 the reconstruction display name would use `causal coupling`.

The edges file is outside the implementation scope of H-V4B-12-M1-B-REVISED and was not changed. E2-001’s logical relation is unaffected; only its display string is.

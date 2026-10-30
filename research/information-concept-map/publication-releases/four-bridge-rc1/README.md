# Four-Bridge Publication — Release Candidate RC1

Information Concept Map (情報概念マップ), English presentation of the Japanese-origin map.

**Scope:**
- BR3-008: R0 / Interaction
- BR3-023: Fc / Causal-role function
- BR3-044: M1 / Q-relative difference-making
- BR3-027: C0 / Passive stabilization
- the shared intervention note OV-NOTE-INTERVENTION
- the existing BR3-012 units, unchanged

**Gate:** `FOUR-BRIDGE-PUBLICATION-RC1-VALIDATED`. This means **not deployed and not published**. No theoretical question is settled; see `KNOWN_LIMITATIONS.md`.

**Canonical effect: NONE.** No canonical file, earlier version or decision was changed. The Mac repository was not written.

## Layout

| Path | Role | Kind |
|---|---|---|
| `publication/publication_data_rc1.json` | integrated publication data: units, BR3-012 units, shared note, links, scope labels, source references | **publication** |
| `publication/publication_units_rc1.tsv` | flat unit table (Japanese, approved label and gloss, formula, approval refs) | publication |
| `publication/mandatory_notes_rc1.tsv` | approved full and short notes, with approving decisions and source references | publication |
| `publication/scope_labels_rc1.tsv` | scope-specific label table (stable ID × scope) | publication |
| `publication/decision_refs_rc1.tsv` | each decision → row in the frozen decision log | publication |
| `renderer/` | static page (HTML/CSS/JS + data.js) for review | publication (implementation) |
| `spec/graph_display_spec_rc1.md` | publication graph vs reconstruction graph specification | spec |
| `research-audit/english_data_edges_v0.6.tsv` | RC1-01: E2-001 reconstruction display name resolved through the stable ID; logic unchanged | **research audit** |
| `research-audit/english_data_draft_v0.8.tsv` | RC1-02: AC-R0-06 / AC-FC-06 snapshots aligned with provenance v0.5; old cells kept | research audit |
| `frozen-inputs/` | byte copies: overlay v0.7, provenance v0.5, decision log v0.14, scope labels v0.3, label schema note v0.1 | frozen inputs |
| `validation/` | `validate_rc1.py`, `render_rc1.js`, `build_rc1.py`, results, print PDF, screenshots | validation |
| `BASELINE_INVENTORY.tsv` | Phase 1: every input with origin (repository vs package), path, version, SHA-256 | — |
| `RELEASE_MANIFEST.tsv` | Phase 7 freeze: every RC1 file with role and SHA-256 | — |
| `KNOWN_LIMITATIONS.md` | open items, untested environments, residual risks, work before publication | — |

## Dependencies

- **Publication data** depends on:
  - `frozen-inputs/english_publication_overlay_v0.7.tsv` (texts and display state);
  - `frozen-inputs/four_bridge_scope_labels_v0.3.tsv` (labels);
  - `figure2b/data.js` in the repository (source authority; SHA-256 in the inventory).
- It reads the research-audit data only for:
  - `constitutive_conditions` (draft v0.8, publication column);
  - the audit-item list shown in the details (provenance v0.5).
- **Research-audit data** (draft v0.8, edges v0.6) depends on:
  - the v0.7 package (draft v0.7, edges v0.5);
  - provenance v0.5;
  - scope labels v0.3.
- **The renderer** reads only `renderer/data.js`, which is built from the files above by `validation/build_rc1.py`.
- **BR3-012** units come from overlay v0.7. Their rows equal the repository overlay v0.1 (checked in SF-10). The BR3-012 graph remains in the repository prototype `br3-012-publication-prototype/` (reference only).

## Reproduce the validation

```
python3 -I validation/validate_rc1.py <rc1 dir> <outputs dir> <v0.7 package dir> <repository root>
node validation/render_rc1.js <rc1 dir>      # needs Playwright + Chromium, pdftotext
```

The scripts are read-only, except for writing their own results into `validation/`.

# Display Specification — Publication Graph and Reconstruction Graph (RC1)

Status: `SPEC` · implemented in `renderer/` · canonical effect **NONE**

## 1. Render unit (all layers, all channels)

One render unit = Japanese label + Japanese original + approved English label + approved gloss + mandatory note. The parts are never separated.

| Part | Rule |
|---|---|
| M1 | The formula `Rel(d;Q\|Σ,𝒟,M,τ)` sits in the **same paragraph** as the gloss. |
| C0 | An inline qualifier follows the gloss in a separate text node: “(‘passive’ ≠ ‘no pathways’; see note)”. |
| Short note | Always visible without interaction, on desktop and mobile. |
| Full note | Expands in the same unit. |
| R0, Fc, M1 | Their full notes are followed by the shared intervention note OV-NOTE-INTERVENTION. That note is **never shown alone**. |
| Gloss accessibility | The gloss paragraph carries `aria-describedby` → note. |

**Copy:**
- Selecting any part of a gloss and copying yields Japanese + label + gloss (+ formula) + short note.
- The copy button yields Japanese + gloss + full note (+ shared note).

**Print:** full notes are printed. Mode switch, buttons and the details sheet are hidden.

## 2. Publication layer (default)

| Element | Display |
|---|---|
| R0, Fc, M1, C0 | units with **publication labels** (Interaction / Causal-role function / Q-relative difference-making / Passive stabilization) |
| R0 — R1 | dashed line, no arrowhead, entailment `none`; caption “comparison (Japanese map); no prerequisite asserted or denied” (OV-L-R0-R1) |
| E2-001, E2-002 | **not drawn**; listed in the appendix as English-reconstruction items (HIDDEN-LISTED, NOT-ASSERTED-IN-PUBLICATION) |
| F family, C family, M group boxes | navigation only; the C box is captioned “not exclusive”. No edge connects C0 with C1/C2. |
| Audit lists | only `PUBLICATION-AND-RECONSTRUCTION` scope items |
| BR3-012 units (R4, R4-SYS, R4-COMB) | shown unchanged as render units. The BR3-012 graph (E2-005, E2-060; E2-004 hidden-listed) stays as specified and implemented in the BR3-012 prototype and is not redrawn here. |

## 3. Reconstruction layer (toggle)

| Element | Display |
|---|---|
| Banner | “English reconstruction … not conditions of the Japanese source” |
| E2-001, E2-002 | solid arrows, captioned “requires (English reconstruction)” |
| Node sub-labels | **reconstruction labels**, resolved from `scope_labels_rc1.tsv` through the stable ID (R0 → “causal coupling”) |
| M1 | shown as “M1 → QREL”, with the note “QREL outside M (English reconstruction only)” |
| Audit lists | all scopes. Every TARGET-origin item is flagged “English reconstruction; not a condition of the Japanese source” and shows its status (e.g. CONDITIONAL, PROFILE-CONDITIONAL). |

## 4. Label resolution

| Field | Display rule |
|---|---|
| `scope_labels_rc1.tsv` (`display_label` of stable ID × scope) | the only source of display labels |
| `working_label` / `short_name` | never used for display |
| `research-audit/english_data_edges_v0.6.tsv` | resolves endpoint display names through `target_stable_label_id` / `source_stable_label_id` |

## 5. Mobile (≤ 760 px)

| Element | Behaviour |
|---|---|
| Units | stacked; short notes inline |
| Graph | hidden behind “Show graph”; horizontal scroll inside the graph only |
| Details | bottom sheet |
| Tooltips | mouse pointer only |

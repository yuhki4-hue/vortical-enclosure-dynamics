# Publication releases — navigation v0.2 (main branch)

**Status: NOT-DEPLOYED.** Nothing in this directory has been published to a public site. It holds release candidates for review.

**Which navigation to use**
- On `main`, use this file and [index_main_v0.2.html](index_main_v0.2.html).
- With the full local research tree, use [README.md](README.md) and [index.html](index.html) (navigation v0.1).

v0.1 is unchanged. Five of its links point into `research/information-concept-map/cross-linguistic-audit/`, which `main` does not contain, so they resolve only in the local tree. See [integration/main_context_navigation_v0.2.md](integration/main_context_navigation_v0.2.md).

## Entry points

| What | Where | Scope |
|---|---|---|
| Four-Bridge RC1 page | [four-bridge-rc1/renderer/index.html](four-bridge-rc1/renderer/index.html) | R0 (BR3-008), Fc (BR3-023), M1 (BR3-044), C0 (BR3-027), the shared intervention note, and the BR3-012 units shown unchanged. The publication and reconstruction layers can be switched. Frozen RC1. |
| Four-Bridge RC1 README | [four-bridge-rc1/README.md](four-bridge-rc1/README.md) | layout, dependencies, validation commands |
| BR3-012 prototype (existing) | not in `main`; local tree at `research/information-concept-map/cross-linguistic-audit/br3-012-publication-prototype/` | R4, R4-SYS, R4-COMB and the BR3-012 graph. Prototype v0.1; unchanged. |

### How the two scopes differ

| | Four-Bridge RC1 | BR3-012 prototype |
|---|---|---|
| Units | the four bridges, plus the BR3-012 *units* (text only) | BR3-012 only |
| Graph | the four-bridge graph | the BR3-012 graph; RC1 does not redraw it |
| Data lineage | the package lineage (overlay v0.7, provenance v0.5, decision log v0.14) | the repository lineage (overlay v0.1, edges v0.4) |

## Audit records and decision history

| Record | Where |
|---|---|
| Four-bridge decision log v0.14 (frozen copy) | [four-bridge-rc1/frozen-inputs/four_bridge_hr_impl_v0.14_decisions.tsv](four-bridge-rc1/frozen-inputs/four_bridge_hr_impl_v0.14_decisions.tsv) |
| Decision IDs used by RC1 | [four-bridge-rc1/publication/decision_refs_rc1.tsv](four-bridge-rc1/publication/decision_refs_rc1.tsv) |
| Condition provenance v0.5 (frozen copy) | [four-bridge-rc1/frozen-inputs/four_bridge_condition_provenance_v0.5.tsv](four-bridge-rc1/frozen-inputs/four_bridge_condition_provenance_v0.5.tsv) |
| Publication decision log v0.2 (repository lineage) | local tree only: `cross-linguistic-audit/publication_decision_log_v0.2.tsv` |
| Cross-linguistic reconstruction ledger v0.3 | local tree only: `cross-linguistic-audit/cross_linguistic_reconstruction_ledger_v0.3.tsv` |
| BR3-012 render validation report v0.1 | local tree only |
| Repository integration report and verification records | [integration/](integration/four_bridge_rc1_repository_integration_v0.1.md) |

## Open items and untested environments

Open items and untested environments are listed in [four-bridge-rc1/KNOWN_LIMITATIONS.md](four-bridge-rc1/KNOWN_LIMITATIONS.md). Theoretical items remain open. Safari (macOS, iOS) and iOS real devices are **NOT-TESTED**.

## Navigation links are not conceptual relations

These links are file navigation only. They do not add, change or imply any conceptual edge, prerequisite, identity or derivation.

## Verification on main

`integration/verify_rc1_in_repo.py` assumes the full local research tree and does not run on `main`. Its RI-4 and RI-5 checks require the BR3-012 files, and RI-6 needs `english-reconstruction/edge_type_registry_v0.2.tsv`. The main-branch checks are recorded in [integration/main_context_navigation_v0.2.md](integration/main_context_navigation_v0.2.md).

# Publication releases — Information Concept Map (English presentation)

**Status: NOT-DEPLOYED.** Nothing in this directory has been published to a public site. It is a repository copy of release candidates for review.

Human decision: H-FB-RC1-INTEGRATION-A (independent repository integration of Four-Bridge RC1).

This directory is **separate from the research canon**.
- `../english-reconstruction/` and `../cross-linguistic-audit/` are unchanged.
- No draft, edge table, overlay or decision log there was overwritten.

## Entry points

| What | Link | Scope |
|---|---|---|
| Four-Bridge RC1 page | [four-bridge-rc1/renderer/index.html](four-bridge-rc1/renderer/index.html) | R0 (BR3-008), Fc (BR3-023), M1 (BR3-044), C0 (BR3-027), the shared intervention note, and the BR3-012 units shown unchanged. Publication layer and reconstruction layer are switchable. Frozen RC1. |
| Four-Bridge RC1 README | [four-bridge-rc1/README.md](four-bridge-rc1/README.md) | layout, dependencies, validation commands |
| BR3-012 prototype (existing) | [../cross-linguistic-audit/br3-012-publication-prototype/index.html](../cross-linguistic-audit/br3-012-publication-prototype/index.html) | R4, R4-SYS, R4-COMB and the BR3-012 graph (E2-004 hidden-listed, E2-005, E2-060). Prototype v0.1; unchanged by this integration. |
| BR3-012 prototype README | [../cross-linguistic-audit/br3-012-publication-prototype/README.md](../cross-linguistic-audit/br3-012-publication-prototype/README.md) | — |

### How the scopes differ

The two pages do not overlap in what they assert.

| | Four-Bridge RC1 | BR3-012 prototype |
|---|---|---|
| Units | the four bridges, plus the BR3-012 *units* (text only) | BR3-012 only |
| Graph | the four-bridge graph | the BR3-012 graph; RC1 does not redraw it |
| Data lineage | the package lineage (overlay v0.7, provenance v0.5, decision log v0.14) | the repository lineage (overlay v0.1, edges v0.4) |

The BR3-012 rows in RC1 are byte-equal in value to the repository overlay v0.1 (RC1 check SF-10).

## Audit records and decision history

| Record | Link |
|---|---|
| Four-bridge decision log (package lineage, v0.14; frozen copy) | [four-bridge-rc1/frozen-inputs/four_bridge_hr_impl_v0.14_decisions.tsv](four-bridge-rc1/frozen-inputs/four_bridge_hr_impl_v0.14_decisions.tsv) |
| Decision IDs used by RC1 | [four-bridge-rc1/publication/decision_refs_rc1.tsv](four-bridge-rc1/publication/decision_refs_rc1.tsv) |
| Condition provenance v0.5 (frozen copy) | [four-bridge-rc1/frozen-inputs/four_bridge_condition_provenance_v0.5.tsv](four-bridge-rc1/frozen-inputs/four_bridge_condition_provenance_v0.5.tsv) |
| Publication decision log (repository lineage; incl. BR3-012) | [../cross-linguistic-audit/publication_decision_log_v0.2.tsv](../cross-linguistic-audit/publication_decision_log_v0.2.tsv) |
| Cross-linguistic reconstruction ledger (repository lineage) | [../cross-linguistic-audit/cross_linguistic_reconstruction_ledger_v0.3.tsv](../cross-linguistic-audit/cross_linguistic_reconstruction_ledger_v0.3.tsv) |
| BR3-012 render validation report | [../cross-linguistic-audit/br3-012-publication-prototype/render_validation_report_v0.1.md](../cross-linguistic-audit/br3-012-publication-prototype/render_validation_report_v0.1.md) |

**Lineage note.** The repository lineage stops at draft v0.5 / overlay v0.2. The package lineage (v0.6–v0.14) is represented here only by RC1’s frozen inputs. This integration does not advance the repository lineage.

## Open items and untested environments

[four-bridge-rc1/KNOWN_LIMITATIONS.md](four-bridge-rc1/KNOWN_LIMITATIONS.md)

**Open items (unchanged):**
- R-series necessary conditions
- generalization of intervention-sensitivity (R0, M1)
- the M1 profile criteria
- Fc constitutive involvement and its vocabulary
- C0 recovery and passivity
- 「状態・過程」
- native-reader review

**Not tested:** Safari (macOS, iOS) and iOS real devices.

## Navigation links are not conceptual relations

The links on this page and in `index.html` are file navigation only:
- They do not add, change or imply any edge between concepts.
- They do not imply prerequisite, identity or derivation.

## Verification

```
python3 integration/verify_rc1_in_repo.py          # Python 3 only; checks RC1 hashes, links, key source-faithful facts
node integration/nav_render_check.js <this dir>    # optional: Playwright + Chromium; pdftotext for print
```

Full RC1 data validation (`four-bridge-rc1/validation/validate_rc1.py`) also needs the lineage packages (v0.7 ZIP, v0.8–v0.14). They are not in the repository; see the RC1 README.

**Integration report:** [integration/four_bridge_rc1_repository_integration_v0.1.md](integration/four_bridge_rc1_repository_integration_v0.1.md)

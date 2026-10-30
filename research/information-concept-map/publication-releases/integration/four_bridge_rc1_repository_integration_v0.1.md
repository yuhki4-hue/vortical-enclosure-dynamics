# Four-Bridge RC1 — Independent Repository Integration v0.1 (report)

Human decision: H-FB-RC1-INTEGRATION-A. Date of run: 2026-10-29.

**Status: NOT-DEPLOYED. Canonical effect: NONE.** This placement is a repository copy for review. It is not a publication, not a new canon version and not a theoretical settlement. No git commit was made (none approved).

**Gate: `FOUR-BRIDGE-RC1-REPOSITORY-INTEGRATION-VALIDATED` is WITHHELD.** RI-3 is not a clean PASS: eight transfer artifacts remain under `publication-releases/_to_delete/` because the device bridge refuses to delete .zip/.png files. All other required RI checks pass. Once a person deletes that folder, RI-3 can be re-run (procedure in §9); the gate may be reported only after that re-run passes.

## 1. Placement

| Item | Path (repository-relative) |
|---|---|
| Repository | `/Users/yobann/Documents/Codex/2026-10-11/task-7/track-a/isolated-repo` |
| RC1 (frozen content) | `research/information-concept-map/publication-releases/four-bridge-rc1/` |
| Navigation | `research/information-concept-map/publication-releases/README.md`, `index.html` |
| Integration records | `research/information-concept-map/publication-releases/integration/` |
| BR3-012 prototype (existing, unchanged) | `research/information-concept-map/cross-linguistic-audit/br3-012-publication-prototype/` |

Source: `four-bridge-publication-rc1.zip`, SHA-256 `b9627753ffc529e9ad790183fab50b25eb3dda2f3023a454937310c0cf36f4db`. `publication-releases/` did not exist before integration, so no same-name directory conflict arose and nothing was overwritten.

## 2. Pre-audit (Phase 1)

- Branch `main`, HEAD `b856873205948b0df722fb8d8f2b2c1166f902ab`.
- Pre-existing working-tree state: 774 status lines — 289 modified tracked files, 485 untracked (`research/` was entirely untracked). These uncommitted changes were recorded and left untouched.
- Pre-integration hash list: 1,874 files (outside `.git`), kept outside the repository at `~/ri_pre_hashes.txt`; status at `~/ri_pre_status.txt`.

## 3. Git status after integration (RI-3)

- `git status --porcelain=v1 -uall` before vs after: **no pre-existing line changed or disappeared**; 53 lines were added, all untracked (`??`), all under `publication-releases/`.
- `git diff --stat` (tracked files): 289 files, identical to before. The integration touched no tracked file.
- HEAD unchanged; no commit.

The 53 added paths:

| Group | Files | In approved scope |
|---|---|---|
| `four-bridge-rc1/**` | 37 (36 manifest entries + `RELEASE_MANIFEST.tsv`) | yes |
| `README.md`, `index.html` | 2 | yes |
| `integration/**` | 6 (this report becomes the 6th file; a log JSON is added as the 7th) | yes |
| `_to_delete/**` | 8 (`ri_transfer.zip`, 7 PNGs) | **no — transfer artifacts** |

**RI-3 verdict: CONDITIONAL / NOT-PASS** until `_to_delete/` is removed.

### Why `_to_delete/` exists

The device bridge injects C2PA metadata into PNG files written through it (bytes change; pixels are identical). The first transfer of the 7 RC1 screenshots therefore failed RI-1. The altered PNGs were renamed into `_to_delete/screenshots_c2pa_reencoded/`, and the original bytes were re-created from a STORED zip (`_to_delete/ri_transfer.zip`). The bridge then refused to delete either the zip or the PNGs ("Operation not permitted"), even with deletion permission granted. None of these files is referenced by RC1 or the navigation.

## 4. Added files and hashes

RC1: all 36 files match `RELEASE_MANIFEST.tsv` (SHA-256 `c4e8622b912a0cce142ab125b71ac64ad097fe06a22178afd76acdade2ffe4cd`); see the manifest for per-file hashes.

| File | SHA-256 |
|---|---|
| `README.md` | `abbe9bcd5fd0bda5e38f2a9662560ac2ff079a82aa0b2e95355122365e25520a` |
| `index.html` | `4611862ff7e223d6f9c9a460975f2d072e762f041c605b23004362495d1998cc` |
| `integration/verify_rc1_in_repo.py` | `e5958301173b6a63263c656e9ca0cae54a1f2b135ec1b2feb55e0541cd750491` |
| `integration/nav_render_check.js` | `7c0edfd1653626d91317d615f6b68a5cf77295cb60e1e241d9a6bbbb756f7529` |
| `integration/nav_render_results.json` | `886fd27aa28e511e77ded6ae70c7396711f8a74a9fbca1f1ce493b77cc39e2f7` |
| `integration/post_integration_render_results_rc1.json` | `36d005bfa3346eb8417f7a5bef97c1c38ee079da6f236c30a4684db65a9d893f` |
| `integration/verify_rc1_in_repo_results.json` | rewritten on every run of the verify script |
| `integration/four_bridge_rc1_repository_integration_v0.1.md` | this file |
| `integration/four_bridge_rc1_repository_integration_log_v0.1.json` | machine-readable log of §5–§6 |

Transfer artifacts (to be deleted, not part of the integration):

| File | SHA-256 |
|---|---|
| `_to_delete/ri_transfer.zip` | `15676eea99574ce31b4eed46fd7eb1c8571ff409d2e0bd3558a633d635137277` |
| `_to_delete/screenshots_c2pa_reencoded/desktop_details_M1.png` | `4f8eced895059b118f97f7a8d87c4304d7db671205517335a0ae0b8d54b38dc6` |
| `_to_delete/screenshots_c2pa_reencoded/desktop_publication.png` | `baacc634fd8b11baa66232bf760c3a4080b93fb1089ab019a6daca26f52a7231` |
| `_to_delete/screenshots_c2pa_reencoded/desktop_reconstruction.png` | `3f1083a8151c4d73b1181226760419d08016b4d92e9f33ca35ac88918e14602d` |
| `_to_delete/screenshots_c2pa_reencoded/mobile_iphone_initial.png` | `39eece38137e0b6eedeb162e3816b55086480a4fee3ded01756768c3d95046de` |
| `_to_delete/screenshots_c2pa_reencoded/mobile_iphone_sheet.png` | `2f4b97b83d6c34313d9833656dc5d7aa3bcf5ef982921c4c9343bb6326a85366` |
| `_to_delete/screenshots_c2pa_reencoded/mobile_pixel_initial.png` | `55bb566dcc4bf9e680a3b2c7f9f45e3ca9454d4643b49248acca119f83deb6b4` |
| `_to_delete/screenshots_c2pa_reencoded/mobile_pixel_sheet.png` | `5b4787943f35e6083fafdf3ffcfcf2f460b0be9950269a04ebf0c200dc3d6d30` |

## 5. RI verdicts

| Check | Verdict | Evidence |
|---|---|---|
| RI-1 RC1 hashes = manifest | PASS | 36/36 match; 37 files present; no unlisted file |
| RI-2 existing files unchanged | PASS | 1,874 pre-existing files re-hashed; 0 changed or missing |
| RI-3 git diff limited to RC1 + integration files | **CONDITIONAL (NOT-PASS)** | pre-existing status lines and tracked diff unchanged; 8 out-of-scope untracked files in `_to_delete/` |
| RI-4 BR3-012 links exist | PASS | `../cross-linguistic-audit/br3-012-publication-prototype/index.html`, README and render report resolve |
| RI-5 RC1 entry links exist | PASS | 27 relative links in README.md + index.html; 0 missing |
| RI-6 navigation is not a theoretical edge | PASS | no edge-type term from `edge_type_registry_v0.2.tsv` in navigation; disclaimer present; no edge file created or changed |
| RI-7 publication / reconstruction kept apart | PASS | data check + display check (layer switch, see §6) |
| RI-8 approved R0/Fc/M1/C0 wording unchanged | PASS | label, gloss, Japanese (vs `figure2b/data.js`), full/short notes, M1 formula `Rel(d;Q|Σ,𝒟,M,τ)` consistent across overlay, notes table and renderer |
| RI-9 E2-001/E2-002 not asserted in publication | PASS | HIDDEN-LISTED + NOT-ASSERTED-IN-PUBLICATION; R0↔R1 comparison not asserted, no arrowhead |
| RI-10 open items and NOT-TESTED kept | PASS | KNOWN_LIMITATIONS lists the open items; AC-C0-10, AC-FC-09, AC-R0-09 remain OPEN-UNRESOLVED; Safari/iOS NOT-TESTED |
| RI-11 README documents verification and dependencies | PASS | scripts, Python 3, Playwright/Chromium, pdftotext, lineage packages named |
| RI-12 placement is not reported as publication | PASS | NOT-DEPLOYED shown; no un-negated deployed/published statement |

## 6. Display verification (Phase 5)

Environment: Chromium 141.0.7390.37 headless (Playwright) in the cloud workspace, opening a byte-identical copy of the repository files via `file://`. Not run on the Mac itself.

### 6a. Existing RC1 results (before integration, from the RC1 package) — kept separate

`four-bridge-rc1/validation/render_results_rc1.json` (frozen): 13 PASS, 1 NOT-TESTED (Safari/iOS), 1 RESIDUAL-RISK.

### 6b. Post-integration: RC1 page from its repository location

`integration/post_integration_render_results_rc1.json` (RC1's `render_rc1.js` re-run on the in-repository copy):

| Check | Channel | Result |
|---|---|---|
| Four-bridge units exact | Desktop Chromium 1366px | PASS |
| BR3-012 units unchanged | Desktop Chromium | PASS |
| M1 formula in gloss paragraph | Desktop Chromium | PASS |
| Gloss never without source and note | Desktop Chromium | PASS |
| Publication graph (no R0→R1 entailment arrow) | Desktop Chromium | PASS |
| Legend | Desktop Chromium | PASS |
| Graph → details sheet | Desktop Chromium | PASS |
| Copy (selection, button, formula) | Desktop Chromium | PASS |
| Layer switch publication ↔ reconstruction | Desktop Chromium | PASS |
| Page errors | Desktop Chromium | PASS |
| Print to PDF (A4) | Chromium print | PASS |
| Mobile | Pixel 7 emulation | PASS |
| Mobile | iPhone 13 profile, Chromium engine (not Safari) | PASS |
| Safari / iOS real device, touch copy | — | NOT-TESTED |
| Screenshots, share sheets, reader mode, screen readers | outside page control | RESIDUAL-RISK |

### 6c. Post-integration: navigation

`integration/nav_render_results.json`:

| Check | Channel | Result |
|---|---|---|
| N-1 navigation page, NOT-DEPLOYED, 15 links resolve, disclaimer | Desktop Chromium | PASS |
| N-2 RC1 / BR3-012 links, back and forward | Desktop Chromium | PASS |
| N-3 document links open (.tsv handled as download) | Desktop Chromium | PASS |
| N-4 page errors | Desktop Chromium | PASS |
| N-5 layout at 1366/1024/761/760/600/375 px, no overflow | Desktop Chromium viewports | PASS |
| N-6 navigation → RC1 → bottom sheet → back | Pixel 7 emulation | PASS |
| N-6 same | iPhone 13 profile, Chromium engine | PASS |
| N-7 Safari / iOS real device | — | NOT-TESTED |

## 7. Non-change check

- Research canon (`english-reconstruction/`, `cross-linguistic-audit/`, drafts, edges, overlays, decision logs, ledger) unchanged: covered by RI-2.
- BR3-012 prototype files unchanged: covered by RI-2.
- No new concept edge: RC1's edge file is the frozen v0.6; integration added no edge file.
- No human decision re-adjudicated. HUMAN-DECIDED ≠ IMPLEMENTED still applies to every open item.

## 8. Reverse-link proposal for BR3-012 (proposal only, not applied)

The prototype was not modified. If a later decision approves it, one line could be added to `br3-012-publication-prototype/README.md`:

> See also: `../../publication-releases/README.md` — repository navigation that lists this prototype next to Four-Bridge RC1. File navigation only; it implies no conceptual edge.

This needs its own human decision, because it changes a prototype file.

## 9. Remaining steps

To reach the integration gate:
1. A person deletes `research/information-concept-map/publication-releases/_to_delete/` in Finder (8 files, §4).
2. Re-run RI-3: `git --no-optional-locks status --porcelain=v1 -uall` must show, beyond the pre-existing lines, only `publication-releases/four-bridge-rc1/**`, `README.md`, `index.html` and `integration/**`.
3. Re-run `python3 research/information-concept-map/publication-releases/integration/verify_rc1_in_repo.py ~/ri_pre_hashes.txt`.
4. Optionally commit only `research/information-concept-map/publication-releases/` (excluding `_to_delete/`), if a person approves that scope.

Before any publication (outside this task's scope):
- Safari (macOS, iOS) and iOS real-device testing, including touch-selection copy.
- Native-reader review of the English wording.
- The open theoretical items in `four-bridge-rc1/KNOWN_LIMITATIONS.md` stay open.
- A separate human decision to deploy.

## 10. Untested environments and residual risks

- NOT-TESTED: Safari (macOS), Safari (iOS), iOS real devices, touch-selection copy.
- Display checks ran in the cloud workspace on a copy, not in a browser on the Mac.
- RESIDUAL-RISK: screenshots, share sheets, reader mode, external excerpts and screen readers can separate a gloss from its note.
- RI-6 and RI-12 are text-pattern checks; they do not replace a human reading of the navigation.
- Full RC1 data validation (`validate_rc1.py`) needs the lineage packages, which are not in the repository.

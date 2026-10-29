# Four-Bridge RC1 — main-branch navigation v0.2 (record)

Date: 2026-10-29.

| | |
|---|---|
| Context | PR preparation, branch `publication/four-bridge-rc1`, base `origin/main` `61213cad5688fa8145eae42d1cdc7f51d6a4c64d` |
| Decision | Navigation option (iii), chosen by the user on 2026-10-29 (「（a)と(ⅲ)でいく」): add a new navigation version for `main` and change no existing file |
| Status | NOT-DEPLOYED |
| Canonical effect | NONE |

## Why v0.2 exists

`main` contains no `research/` tree. The research canon, the BR3-012 prototype and the repository-lineage logs exist only in the local repository. Navigation v0.1 (`README.md`, `index.html`) links to five files there, so on `main` those links do not resolve:
- `../cross-linguistic-audit/br3-012-publication-prototype/index.html`
- `../cross-linguistic-audit/br3-012-publication-prototype/README.md`
- `../cross-linguistic-audit/br3-012-publication-prototype/render_validation_report_v0.1.md`
- `../cross-linguistic-audit/publication_decision_log_v0.2.tsv`
- `../cross-linguistic-audit/cross_linguistic_reconstruction_ledger_v0.3.tsv`

v0.1 is left byte-identical. It is part of the 51 audited files and is correct for the full local tree. v0.2 is added beside it:
- it links everything that exists on `main`;
- it names the five local-only items as plain text with their local paths;
- it points to v0.1 for the full tree.

It adds no research data, and it does not carry the BR3-012 prototype into `main`.

## Files added (in addition to the 51 audited files)

| File | Role |
|---|---|
| `publication-releases/index_main_v0.2.html` | navigation page for `main` |
| `publication-releases/README_main_v0.2.md` | navigation README for `main` |
| `integration/main_context_navigation_v0.2.md` | this record |
| `integration/main_nav_check_v0.2.py` | static checks M-1 … M-8 (Python 3 standard library only) |
| `integration/main_nav_check_v0.2_results.json` | results of M-1 … M-8 |
| `integration/main_nav_render_check_v0.2.js` | display checks MV-1 … MV-7 (Playwright + Chromium) |
| `integration/main_nav_render_results_v0.2.json` | results of MV-1 … MV-7 |

## Results on the PR branch

Static checks were run on the branch checkout, with the edge-type terms taken from the local `edge_type_registry_v0.2.tsv`.

| Check | Result |
|---|---|
| M-1 all relative links in v0.2 resolve on `main` | PASS |
| M-2 RC1 entry link | PASS |
| M-3 BR3-012 named as local-only, not linked | PASS |
| M-4 navigation is not an edge (no edge-type term; disclaimer present) | PASS |
| M-5 NOT-DEPLOYED; not reported as published | PASS |
| M-6 RC1 = frozen manifest (36/36) | PASS |
| M-7 `figure2b/data.js` on `main` = recorded source authority (`734d1511…`) | PASS |
| M-8 v0.1 kept and pointed to | PASS |

Display checks: Chromium 141.0.7390.37 headless in the cloud workspace, branch checkout via `file://`.

| Check | Channel | Result |
|---|---|---|
| MV-1 page, NOT-DEPLOYED, 12 links resolve, no link into `cross-linguistic-audit/`, local-only items shown | Desktop Chromium | PASS |
| MV-2 RC1 link, back, forward; v0.1 link opens | Desktop Chromium | PASS |
| MV-3 document links open (.tsv as download) | Desktop Chromium | PASS |
| MV-4 page errors | Desktop Chromium | PASS |
| MV-5 layout at 1366/1024/761/760/600/375 px, no overflow | Desktop Chromium viewports | PASS |
| MV-6 navigation → RC1 → bottom sheet → back | Pixel 7 emulation | PASS |
| MV-6 same | iPhone 13 profile, Chromium engine | PASS |
| MV-7 Safari / iOS real device | — | NOT-TESTED |

The RC1 page's own render checks (`four-bridge-rc1/validation/render_rc1.js`) were also re-run on a copy taken from the branch. The frozen files were not touched, and the result matched the frozen RC1 results: 13 PASS, 1 NOT-TESTED, 1 RESIDUAL-RISK.

## Known limits on `main`

- On `main`, v0.1 still shows the five links above, and they lead nowhere. v0.2 is the `main` entry point. Which page a Pages listing uses is a separate decision.
- `integration/verify_rc1_in_repo.py` needs the full local tree, so it does not run on `main`. Its RI-1 … RI-12 results stay valid for the local repository (`four_bridge_rc1_ri3_final_verification_v0.2.md`).
- Safari, iOS real devices and touch copy: NOT-TESTED.

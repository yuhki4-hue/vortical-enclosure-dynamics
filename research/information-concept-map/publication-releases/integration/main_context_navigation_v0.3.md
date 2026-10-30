# Four-Bridge RC1 — main-branch navigation v0.3 (record)

Date: 2026-10-30.

| | |
|---|---|
| Context | PR #2, branch `publication/four-bridge-rc1` |
| Decision | Option (ii) for TSV links, chosen by the user on 2026-10-30 (「（ⅱ）で」): add a display note in a later navigation version; change no existing file and no serving setup |
| Status | NOT-DEPLOYED |
| Canonical effect | NONE |

## Why v0.3 exists

The Safari real-device check (`safari_ios_real_device_check_v0.1.md`) found that linked TSV files show Japanese text and symbols as mojibake in Safari. The user then queried the live GitHub Pages site: it serves `.tsv` as `text/tab-separated-values` with no character set, while `.md` comes with `charset=utf-8`.

v0.3 is navigation v0.2 plus a TSV display note. Specifically, v0.3:
- labels each TSV link "(TSV)";
- adds a note below the audit-record list: the files are UTF-8; in Safari on a Mac, choose View → Text Encoding → Unicode (UTF-8); on iPhone or iPad, open the file in the repository view on GitHub or download it;
- adds a matching "TSV files and character set" section to the README;
- links back to v0.2 and v0.1.

Nothing else changes from v0.2. v0.2, v0.1, the frozen RC1 files and the TSV files themselves are unchanged.

The iPhone/iPad advice rests on a known fact: iOS Safari has no text-encoding menu. The workaround itself was not tested on a device.

## Files added

| File | Role |
|---|---|
| `publication-releases/index_main_v0.3.html` | navigation page for `main`, v0.3 |
| `publication-releases/README_main_v0.3.md` | navigation README for `main`, v0.3 |
| `integration/main_context_navigation_v0.3.md` | this record |
| `integration/main_nav_check_v0.3.py` | static checks M-1 … M-10 |
| `integration/main_nav_check_v0.3_results.json` | results |
| `integration/main_nav_render_check_v0.3.js` | display checks MV-1 … MV-8 (Playwright + Chromium) |
| `integration/main_nav_render_results_v0.3.json` | results |

## Results on the PR branch

Static checks (edge-type terms from the local `edge_type_registry_v0.2.tsv`):

| Check | Result |
|---|---|
| M-1 … M-8 (the v0.2 checks, applied to v0.3) | PASS |
| M-9 TSV note in the HTML and the README; every TSV link in the HTML labeled "(TSV)" | PASS |
| M-10 v0.3 links to v0.2 | PASS |

Display checks (Chromium 141.0.7390.37 headless, branch checkout via `file://`):

| Check | Channel | Result |
|---|---|---|
| MV-1 page, NOT-DEPLOYED, 13 links resolve, no link into `cross-linguistic-audit/` | Desktop Chromium | PASS |
| MV-2 RC1 link, back, forward; v0.1 link opens | Desktop Chromium | PASS |
| MV-3 document links open | Desktop Chromium | PASS |
| MV-8 TSV display note visible | Desktop Chromium | PASS |
| MV-4 page errors | Desktop Chromium | PASS |
| MV-5 layout at 1366/1024/761/760/600/375 px, no overflow | Desktop Chromium viewports | PASS |
| MV-6 navigation → RC1 → bottom sheet → back | Pixel 7 emulation; iPhone 13 profile (Chromium engine) | PASS |
| MV-7 Safari / iOS real device | — | NOT-TESTED for v0.3 |

## Known limits

- v0.3 has not been opened in real Safari. The Safari check used navigation v0.1.
- The note is a workaround. The TSV files will still show as mojibake by default in Safari until the serving setup changes. That is outside this decision.
- Navigation v0.1 (local tree) has no TSV note.

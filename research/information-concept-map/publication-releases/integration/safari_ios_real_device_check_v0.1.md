# Four-Bridge RC1 — Safari and iOS real-device check v0.1 (record)

| | |
|---|---|
| Date | 2026-10-30, 09:10–09:57 JST |
| Status | NOT-DEPLOYED |
| Canonical effect | NONE |

This record adds real-browser results for two environments that every earlier record listed as NOT-TESTED: Safari on macOS and Safari on an iPhone. It changes no earlier record and no frozen file. The Chromium results stay as recorded in `validation/render_results_rc1.json`, `integration/post_integration_render_results_rc1.json`, `integration/nav_render_results.json` and `integration/main_nav_render_results_v0.2.json`.

## Environments and method

| Environment | Version | Method |
|---|---|---|
| Safari on macOS | Safari 27.0.1 (22625.1.29.11.28); macOS 27.0.1 per the print PDF metadata | The user operated the browser. Claude observed each step through screen capture (read-only access to Safari) and compared the visible text with `four-bridge-rc1/renderer/data.js`. |
| Safari on iPhone | iPhone 16e, iOS 26.6.2 | The user operated the phone and sent screenshots. Claude compared them with the data. Items without a screenshot are marked as the user's own observation. |

**Pages and server**
- Pages were served from the local repository with `python3 -m http.server 8000`, run from `research/information-concept-map/`.
- On the Mac they were opened at `http://localhost:8000/…`. On the iPhone they were opened through the Mac's address on the local network.
- Navigation v0.1 (`publication-releases/index.html`) was used, because it matches the full local research tree.
- The RC1 files are byte-identical to the frozen manifest.

## Results — Safari on macOS

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Unit display | PASS | For R0, Fc, M1 and C0, the Japanese original, label, gloss and short note match `data.js` character for character. The M1 formula sits in the gloss paragraph. C0 shows its inline qualifier. Σ, 𝒟, τ and ≠ render correctly. |
| 2 | Shared note and BR3-012 units | PASS | R4, R4-SYS and R4-COMB match the data. The shared intervention note appears in the details for R0, Fc and M1 (see 4 and 9). |
| 3 | Graph and layer switch | PASS | **Publication layer:** the R0–R1 link is a dashed line with no arrowhead, and the label says no prerequisite is asserted or denied. **Reconstruction layer:** red E2-001 and E2-002 arrows and "M1 → QREL" appear, and the legend says "necessary in the English reconstruction only". Switching back removes them. In both layers the appendix lists E2-001 and E2-002 as HIDDEN-LISTED, as specified. |
| 4 | Details sheet | PASS | Clicking the M1 node opens the sheet. The full note matches the data word for word, and the shared intervention note follows it. A close button is present. |
| 5 | Copy button | PASS | The pasted text (in Notes) has the header line, the Japanese original with the formula, the gloss with the formula, the short note, the full note, the shared note and the source line, in the order produced by `unitText()`. |
| 7 | Width | PASS | In a narrow window the units go to one column, the graph sits behind "Show graph", and no horizontal page overflow is visible. With the graph open, it scrolls horizontally inside its own frame. |
| 8 | Links and back | PASS | Navigation → RC1 → back works. Navigation → BR3-012 prototype → back works. |
| 9 | Print | PASS | Safari print to PDF: A4, 7 pages, headers and footers on. Extracting the text and comparing it found all 30 items: Japanese, gloss, short note and full note for the 4 bridges and the 3 BR3-012 units; the M1 formula next to its gloss; the shared note 3 times (after R0, Fc and M1; none after C0, as in the data). |
| 10 | Dark mode | PASS (visual) | All text, panels and the selected layer button are readable. Contrast was not measured. |
| — | Document links (.md, .tsv) | CONDITIONAL | `README.md` and the decision log `.tsv` open as plain text, but Japanese and symbols show as mojibake. The files are valid UTF-8: no BOM, no invalid bytes. Choosing View → Text Encoding → Unicode (UTF-8) fixes them; for the `.tsv` the encoding had to be chosen again on that page. Cause: the test server sends `text/markdown` and `text/tab-separated-values` without `charset=utf-8`. |

## Results — Safari on iPhone 16e (iOS 26.6.2)

| # | Check | Result | Evidence |
|---|---|---|---|
| 6 | Long-press selection copy | PASS | The user selected the M1 gloss through the short note and copied it. The pasted text equals `unitText("M1", false)`: header, Japanese original with the formula, gloss with the formula, short note and source line. The page's copy handler works on iOS Safari. (screenshot) |
| 1 | Unit display, portrait | PASS | One column. R0 and Fc text match the data. (screenshot) |
| 2 | BR3-012 units | PASS | The R4-COMB note shows 組合せ的 and 体系的 correctly. (screenshot) |
| 3 | Publication graph | PASS | Hidden behind "Show graph" until tapped. The R0–R1 link is dashed with no arrowhead. (screenshot) |
| 3 | Reconstruction graph | PASS | The E2-001 and E2-002 arrows and "M1 → QREL" appear only in this layer. (screenshot) |
| 4 | Details bottom sheet | PASS | Tapping the M1 node opens a bottom sheet with the full note, the formula and a close button. (screenshot) |
| 7 | Width | PASS | No page overflow in portrait. In a wider view the whole graph, including the C family, is visible. (screenshot) |
| 10 | Dark mode | PASS (visual) | Readable. (screenshot) |
| 11 | Reader view | OBSERVED — not a pass/fail item | **Gloss and note stay together:** for R0 and M1, the Japanese original, the gloss (with the M1 formula) and the short note stay adjacent and in order. **Reader changes:** (a) the Japanese and English labels run together with no space ("関連性Q-relative difference-making"); (b) the audit-conditions summary is replaced by the generic "▶ 詳細"; (c) the buttons are removed. **Not checked:** whether the page's opening scope paragraph is kept. (screenshots) |

## Observations (not defects)

1. In a narrow viewport the graph opens inside a horizontally scrolling frame, so the C family is off to the right at first.
2. In Safari print, a page break falls inside one of the three shared notes, so the Safari header and footer appear in the middle of that note. Without the header and footer the text matches exactly. The page breaks differ from the frozen Chromium print, which has 8 pages.
3. In reader view, labels lose their separating space, and the audit-conditions summary text is replaced (see 11).
4. The iOS Safari page menu also offers "要約する" (summarize) and "Webサイトを翻訳…" (translate). Both rebuild the page text outside the page's control. They were not tested and fall under the existing RESIDUAL-RISK item.

## Before publication (added by this check)

**Character set for document links.** The live GitHub Pages site was checked on 2026-10-30 by the user, with `curl -sI` from the Mac against two files already on `main`:

| Type | Response header | Result |
|---|---|---|
| `.md` (`README_ja.md`) | `content-type: text/markdown; charset=utf-8` | OK. Linked Markdown documents will display correctly in Safari. |
| `.tsv` (`dimensionality-working-note/…/campA_TD_g0.075_s10.tsv`) | `content-type: text/tab-separated-values` (no charset) | **Open.** Safari is expected to show linked TSV files as mojibake by default, as it did on the test server. |

Navigation links to TSV files:
- `RELEASE_MANIFEST.tsv`
- `four_bridge_hr_impl_v0.14_decisions.tsv`
- `decision_refs_rc1.tsv`
- `four_bridge_condition_provenance_v0.5.tsv`

Of these, the decision log, the decision IDs file and the provenance file contain Japanese text or symbols. The RC1 page itself (HTML) is not affected, and neither are its details sheet, copy or print.

How to handle the TSV links was a separate human decision. The user chose option (ii) on 2026-10-30: add a display note in a later navigation version. This is implemented as navigation v0.3 (`integration/main_context_navigation_v0.3.md`). The frozen files and the serving setup are unchanged.

## Still not tested

- Navigation v0.2 (`index_main_v0.2.html`) in Safari. Only v0.1 was used here.
- Safari on iPad.
- Other iOS versions or devices.
- iOS summarize and translate.
- Screen readers.
- Reader view in Safari on macOS.

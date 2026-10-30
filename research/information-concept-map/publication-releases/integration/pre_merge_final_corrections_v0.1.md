# Four-Bridge RC1 — final pre-merge corrections v0.1

Date: 2026-10-30. Parent: b1a40bb9f33696aa5138a6b1a7124dd4e96fa880.
Scope: navigation v0.3 HTML, its README, and this new supplemental record.
No merge or deployment is authorized by this record.

## Public scope and status

- main and the PR head contain no BR3-012 prototype. The expected Pages path `research/information-concept-map/cross-linguistic-audit/br3-012-publication-prototype/` returned HTTP 404 on 2026-10-30.
- No verified public prototype URL was found in this publication scope. This does not claim that no unrelated external copy exists.
- BR3-012's R4/R4-SYS/R4-COMB text units remain available inside RC1. Its graph/prototype is not included.
- A future prototype publication is a separate proposed addition, requiring review and approval; it is not a live link or a committed release schedule.
- RC1's freeze-time NOT-DEPLOYED wording is preserved. Navigation now explains that historical artifact status can differ from current delivery.
- The navigation uses FROZEN RELEASE CANDIDATE, without asserting a continuously updated delivery state.

## Safari evidence

The earlier `safari_ios_real_device_check_v0.1.md` remains unchanged and applies to navigation v0.1 and RC1.

In this handoff chat, the user tested navigation v0.3 and RC1 from a Mac-hosted isolated preview on an iPhone with Safari and reported “全てOK”; the user reaffirmed PASS in the final-corrections request. User-reported PASS covers layout, TSV notice visibility, RC1 navigation/back, Japanese/gloss/note adjacency, M1 formula, full/shared notes, publication/reconstruction switching, copy into Notes, and dark mode. Device and OS/browser versions were not supplied for this check; do not substitute versions from the earlier record.

README/TSV destination documents were excluded from the isolated-preview test. Their actual Pages display and post-publication URLs remain NOT-TESTED. The final textual corrections in this commit have not been rechecked on the iPhone; the prior PASS is retained with that scope.

macOS Safari previously opened the isolated v0.3 file and RC1, including navigation/back and layer switching. That was file delivery, not a Pages test.

## Integrity and paths

The frozen RC1 subtree must remain `7f5e00fbb35f009dbc6a8517eddbd52c95abb909`, including its 36 manifest-listed files and RELEASE_MANIFEST.tsv. No existing decision log, research canonical file, prototype, earlier navigation version or existing verification record is edited.

The publication entry is:
https://yuhki4-hue.github.io/vortical-enclosure-dynamics/research/information-concept-map/publication-releases/index_main_v0.3.html

RC1 is relative to it at `four-bridge-rc1/renderer/index.html`; its CSS/data.js/app.js are local to renderer/. The navigation has inline CSS and no script/image dependencies. Relative navigation destinations are checked against the PR tree. v0.1 is explicitly for the full local research tree and retains its historical local-only links.

The previously observed Pages deployment used main at 61213cad5688fa8145eae42d1cdc7f51d6a4c64d, and the live root served the repository root entry. The Pages settings screen itself was unavailable without browser authentication. The future entry path assumes that established main/root publication configuration remains in place; verify the deployment SHA and real URLs after separately approved merge/publication. The root entry is not changed or given a new link.

TSV files remain UTF-8, with a display workaround only. The observed Pages TSV response omitted charset; Markdown included charset=utf-8. No encoding or serving configuration fix is claimed.

## Review gate

Candidate: FOUR-BRIDGE-RC1-FINAL-PUBLICATION-REVIEW-READY.
This is a human review gate, not a merge, deployment or theoretical settlement.

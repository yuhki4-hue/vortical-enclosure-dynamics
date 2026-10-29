# Known Limitations and Open Items — RC1

RC1 freezes approved publication expressions. **It does not settle any of the theoretical questions below.** Each stays OPEN.

## Theoretical items (OPEN)

| Item | Where it is tracked |
|---|---|
| R-series necessary-condition relations (E2-001, E2-002, E2-003, E2-006, E2-007, E2-010; the R order 「R2以上」) | LDG-0011 v0.2 (NOT-ASSESSED); provenance AC-R0-08 |
| Generalization of intervention-sensitivity for R0 and M1 | AC-R0-05 (CONDITIONAL); AC-M1-14 (PROFILE-CONDITIONAL) |
| M1 intervention-profile selection criteria; relative evidential strength of observation / comparison / intervention | AC-M1-14 notes; AC-M1-07 |
| Fc constitutive / foundational involvement | AC-FC-09 (OPEN-UNRESOLVED) |
| Fc involvement-type (claim-depth) vocabulary | draft `claim_depth` = UNCLASSIFIED; HR-IMPL-4-B |
| C0 recovery and passivity: recovery mechanism (AC-C0-12) and O-027-3, the mechanistic restriction of 受動的 (AC-C0-10) | as listed |
| Strict reading of 「状態・過程」 (either or both) | AC-R0-09 (OPEN-UNRESOLVED) |
| Native-reader review | NOT-PERFORMED (post-publication item, not a gate) |

## Verification limits

| Item | State |
|---|---|
| Safari (macOS, iOS), iOS real devices, touch-selection copy | **NOT-TESTED** |
| “iPhone 13” | a Chromium device profile, not Safari |
| Notes lost through screenshots, OS share sheets, reader modes, text-fragment links, external extraction | **RESIDUAL-RISK** |

**Approvals of “the text presented in the preceding review”** (R0 partial, Fc candidates, M1 full note, C0, shared note): the presented texts were not visible in the session that implemented them. Each was identified as the overlay text current at decision time. They match the decision wording (“現行”, “全文そのまま”).

## Data notes

| Item | Note |
|---|---|
| draft v0.8 `reconstruction_conditions` | For R0 and Fc this column holds paraphrased snapshots of AC-R0-05 / AC-FC-11. The item state is authoritative in provenance v0.5. Not changed in RC1 (not stale state, only shorter wording). |
| The two lineages | 1. **Mac repository** (up to draft v0.5, overlay v0.2, edges v0.4, ledger v0.3, publication decision log v0.2). 2. **Package lineage** (v0.6 and later; v0.7 ZIP → v0.14 packages). RC1 builds on the package lineage and takes BR3-012 data and `figure2b/data.js` from the repository. The repository was not written. |
| v0.10 working-copy PNGs | Differ in bytes from their manifest (pixel-identical re-encoding). The delivered v0.10 ZIP is intact. |
| BR3-012 units | R4-SYS and R4-COMB have no separate approved English label. The units show the gloss with the object ID. Their Japanese text carries the existing “(source of BR3-01x)” suffix from overlay v0.1. |

## Before publication (not done in RC1)

1. Test in Safari (macOS, iOS) and on real devices.
2. Decide the hosting target and how BR3-012’s graph and the four-bridge graph are combined on the live site.
3. Decide whether RC1 files enter the Mac repository (and where), and whether the repository lineage is advanced to match the package lineage.
4. Optional native-reader review.
5. A final human release decision. RC1 is a candidate, not a release.

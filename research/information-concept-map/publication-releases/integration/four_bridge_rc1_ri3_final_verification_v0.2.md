# Four-Bridge RC1 — RI-3 Final Verification v0.2 (follow-up record)

Human decision: H-FB-RC1-INTEGRATION-A (unchanged). Run: 2026-10-29, about 21:00 JST, after a person deleted `publication-releases/_to_delete/` in Finder.

This record follows two earlier records, which stay as written:
- `four_bridge_rc1_repository_integration_v0.1.md`: RI-3 CONDITIONAL;
- `four_bridge_rc1_ri3_final_verification_v0.1.md`: RI-3 FAIL.

**Status: NOT-DEPLOYED. Canonical effect: NONE. No git commit.**

**Result: RI-3 PASS. Gate `FOUR-BRIDGE-RC1-REPOSITORY-INTEGRATION-VALIDATED` REPORTED.** RI-2 passes under the human scoping statement in §2.

The gate means only that the repository placement is validated. It is not a git commit, a deployment, a new canon version or a theoretical settlement.

## 1. Checks

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | `_to_delete/` absent | PASS | `publication-releases/` holds only `README.md`, `index.html`, `four-bridge-rc1/` and `integration/`, plus a Finder `.DS_Store` (see §2). |
| 2 | pre-existing changes kept | PASS | Pre-integration status had 774 lines; it now has 822. 0 pre-existing lines were removed or changed. `git diff --stat` still shows 289 tracked files; 0 staged; HEAD `b856873205948b0df722fb8d8f2b2c1166f902ab`. |
| 3 | new files limited to approved scope | PASS | All 48 added status lines are `??` under `publication-releases/`: `four-bridge-rc1/` (37), `README.md` (1), `index.html` (1), `integration/` (9). There are 0 lines outside that scope. |
| 4 | RC1 36 files = frozen manifest | PASS | RI-1: 36/36 match; manifest SHA-256 `c4e8622b912a0cce142ab125b71ac64ad097fe06a22178afd76acdade2ffe4cd`; 0 unlisted. |
| 5 | navigation links to RC1 and BR3-012 | PASS | RI-4 and RI-5: 27 relative links, 0 missing; the BR3-012 prototype entry resolves. |
| 6 | RI-3 re-run | **PASS** | Checks 1–3. |

Counts are as of the check, before this record and its log JSON were added. Adding them brings `integration/` to 11 files, still within scope.

## 2. RI-2 and the Finder `.DS_Store` files

`verify_rc1_in_repo.py` reported RI-2 FAIL on three of the 1,874 pre-existing files:

| File | Modified (JST) | git |
|---|---|---|
| `.DS_Store` | 21:00:33 | untracked, ignored (`.gitignore:1`) |
| `research/.DS_Store` | 21:00:41 | untracked, ignored |
| `research/information-concept-map/.DS_Store` | 21:00:59 | untracked, ignored |

Finder also created `research/information-concept-map/publication-releases/.DS_Store`. It is ignored and does not appear in git status.

**Cause.** These are Finder's own folder-view files: they hold icon positions and window state. Finder rewrote one in each folder it opened on the way to `_to_delete/`, and the times line up with the deletion. Each file names only the child folder along that path:
- the root file lists the top-level folders;
- `research/` lists `information-concept-map`;
- `information-concept-map/` lists `english-reconstruction` and `publication-releases`.

The integration did not write them.

**Other files.** All other pre-existing files (1,871, including the research canon and the BR3-012 prototype) are byte-identical to the pre-integration hash list.

**Human scoping statement.** Asked whether these Finder metadata files may be excluded from RI-2, the user answered (2026-10-29): 「外しても問題なさそうだが気にはなるね」. This record treats that as approval to exclude `.DS_Store` from RI-2. The cause above answers the concern. If that reading is wrong, the exclusion and the gate in this record are withdrawn.

**RI-2 (scoped): PASS.** 1,871 of 1,871 non-`.DS_Store` pre-existing files are unchanged.

## 3. RI verdicts (this run)

| Check | Verdict |
|---|---|
| RI-1 | PASS |
| RI-2 | PASS (scoped: `.DS_Store` excluded per §2; unscoped: 3 Finder files changed) |
| RI-3 | PASS |
| RI-4 … RI-12 | PASS |

The display checks (`nav_render_results.json`, `post_integration_render_results_rc1.json`) were not re-run. The deletion touched no file they read. Safari and iOS real devices remain NOT-TESTED.

## 4. Verdict history (append-only)

| Record | RI-3 | Gate |
|---|---|---|
| `four_bridge_rc1_repository_integration_v0.1.md` | CONDITIONAL | withheld |
| `four_bridge_rc1_ri3_final_verification_v0.1.md` | FAIL (`_to_delete/` present) | not reported |
| this record (v0.2) | PASS | **FOUR-BRIDGE-RC1-REPOSITORY-INTEGRATION-VALIDATED** |

## 5. Still outstanding

- No commit. If a commit is approved, its scope is `research/information-concept-map/publication-releases/`. `.DS_Store` is ignored.
- Before any publication:
  - Safari, iOS real-device and touch-copy tests;
  - native-reader review;
  - the open theoretical items in `four-bridge-rc1/KNOWN_LIMITATIONS.md`;
  - a separate decision to deploy.
- The BR3-012 reverse link remains a proposal only.

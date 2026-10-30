# Four-Bridge RC1 — RI-3 Final Verification v0.1 (follow-up record)

Human decision: H-FB-RC1-INTEGRATION-A (unchanged). Run: 2026-10-29 (JST evening).

This record follows `four_bridge_rc1_repository_integration_v0.1.md`, which stays as written (RI-3 CONDITIONAL, gate withheld). Nothing in that report was changed.

**Status: NOT-DEPLOYED. Canonical effect: NONE. No git commit.**

**Result: RI-3 FAIL. Gate `FOUR-BRIDGE-RC1-REPOSITORY-INTEGRATION-VALIDATED` NOT reported.**

## Checks

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | `_to_delete/` absent | **FAIL** | `publication-releases/_to_delete/` exists. Shell listing and device directory listing both show the same 8 files (1 zip, 7 PNGs), with the same sizes and modification times as before. One more `rm -rf` attempt from the device shell failed with "Operation not permitted". |
| 2 | pre-existing changes kept | PASS | Pre-integration status (774 lines) vs now (828 lines): 0 pre-existing lines removed or changed. `git diff --stat` still 289 tracked files; nothing staged; HEAD `b856873205948b0df722fb8d8f2b2c1166f902ab`. |
| 3 | new files limited to approved `publication-releases/` scope | **FAIL** | 54 added untracked lines, all under `publication-releases/`. 46 are in the approved scope: `four-bridge-rc1/` (37), `README.md`, `index.html`, `integration/` (7). 8 are under `_to_delete/`, which is outside the approved scope. |
| 4 | RC1 36 files = frozen manifest | PASS | RI-1: 36/36 match; manifest SHA-256 `c4e8622b912a0cce142ab125b71ac64ad097fe06a22178afd76acdade2ffe4cd`; no unlisted file. |
| 5 | navigation links to RC1 and BR3-012 valid | PASS | RI-4 and RI-5: 27 relative links, 0 missing; BR3-012 prototype entry resolves. |
| 6 | RI-3 re-run | **FAIL** | Checks 1 and 3. |

Counts are as of the check, before this record and its log JSON were added to `integration/`. Adding them brings `integration/` to 9 files, still within the approved scope.

RI-1, RI-2 and RI-4 … RI-12 were re-run in the same session (`verify_rc1_in_repo.py ~/ri_pre_hashes.txt`). All passed. RI-2 covers 1,874 pre-existing files, including the research canon and the BR3-012 prototype.

## Verdict history (append-only)

| Record | RI-3 | Gate |
|---|---|---|
| `four_bridge_rc1_repository_integration_v0.1.md` | CONDITIONAL (NOT-PASS) | withheld |
| this record (v0.1 final verification) | FAIL — `_to_delete/` still present | not reported |

## To pass

1. Delete `research/information-concept-map/publication-releases/_to_delete/` on the Mac (Finder or Terminal). The device bridge cannot delete .zip/.png files.
2. Re-run this verification. If `_to_delete/` is absent and the other checks still pass, RI-3 is PASS and the gate may be reported. That would go in a new record (v0.2).

The gate, when reported, does not mean a git commit, a deployment or theoretical settlement.

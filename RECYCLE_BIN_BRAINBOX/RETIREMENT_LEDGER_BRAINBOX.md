# RETIREMENT_LEDGER_BRAINBOX

**State:** [PRESENT · POPULATED] — one archive record, `RET-2026-10-15-PROJ-WORKFLOW`, with a seven-empty-directory cleanup exception.

Each later entry must record retirement ID, item type, original repository-relative path, purpose, reason, Operator approval/ticket, pre-operation SHA-256 and Git blob/commit where applicable, file manifest for directories, archive path, canonical/reference replacement, affected links, verification, recovery procedure, date, and publication references. Distinguish PROPOSED, AUTHORIZED, ARCHIVED, BLOCKED, and RESTORED.

Do not treat this ledger as standing authorization to retire protected or retained source files. Historical M20 empty-file retirements are documented in the V003 Migration Map, not retrospectively moved here.


## RET-2026-10-15-PROJ-WORKFLOW — PARTIAL DIRECTORY CLEANUP BLOCK

- **Operator authorization:** 2026-10-15, retire `AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX` into the repository's Retired Items Bin.
- **Source:** `AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/` (88 files, including four historical README files).
- **Archive:** `RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/`.
- **Manifest:** `RECYCLE_BIN_BRAINBOX/PROJ_WORKFLOW_RETIREMENT_MANIFEST_BRAINBOX.json` — exact relative file names, bytes and SHA-256 per item; 88 archived files.
- **Reason:** Full source content coverage in current V003; superseded active project-workflow location. Historical original retained in governed retired-items bin rather than discarded.
- **File disposition:** 88/88 archived successfully. File hashes verified against source copies during operation. All old source *files* subsequently cleared. Old tree still physically exists as **seven empty directories** (five image subfolders, FootHive parent and PROJ_WORKFLOW parent) because Windows returned Access Denied on directory removal. This is not a completed full directory retirement; mark **ARCHIVED — CLEANUP BLOCKED** until the empty directories are removed and a final existence check passes.
- **Dependency/reference caveat:** The preflight identified 36 non-source files containing 1,832 occurrences of historic project path fragments. These are largely documentary but have not been individually classified as historical versus live dependencies. No automatic rewrite was performed. Existing paths in historical ledgers may continue to refer to the retired original location; use the manifest to recover the source paths.
- **Recovery:** Copy the archived `PROJ_WORKFLOW_AI_BRAINBOX/` tree back to `AI_BRAINBOX/` using the manifest to verify 88 SHA-256 values; do not overwrite an existing live tree without a new Operator decision.
- **Publication:** Local only; no staging, commit, push or merge. Preexisting working changes and branch remain intact.

# RETIREMENT_LEDGER_BRAINBOX

**State:** [PRESENT · POPULATED] — two authorized archive records: RET-2026-10-15-PROJ-WORKFLOW and RET-2026-10-16-LEGACY-AUTHORITY.

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
- **Publication:** implementation and pre-publication checks pass; staged-path review and Git publication remain pending.


## Corrective Ticket 01 follow-up - 2026-10-16

**Baseline:** PR #48 merge commit 90a1c0c9c02017398b02406f57e8c95fd65b06ca; branch v003/proj-workflow-final-retirement-verification.

**Archive check:** 88 manifest paths and 88 archived files; exact path set, no missing/extra records, four historical README files. Direct worktree SHA-256/size matches: 82/88. Six files differ from manifest only by CRLF conversion; their LF-normalized bytes and Git blobs match the recorded SHA-256 and byte count. No content difference outside line endings was found. Per the corrective ticket's strict gate, this remains a blocking raw-worktree checksum failure; this record does not claim a literal 88/88 raw file-hash pass.

**Migration and source:** 84 archive-to-V003 direct copies were verified byte-identical in the current worktree: 44 archive-origin rows in the FootHive copy manifest, 38 design/product/logo asset files, and two Fullstack workflow documents. The four archived MUST_README records remain historical; each points to a separately authored current V003 navigation authority. The 001/002 documents remain RAW/UNPROVEN. The old source path contains 0 tracked files, 0 physical files, and seven empty directories.

**Routing and disposition:** The stale project README link and M03-era retained-source listing in Governance were corrected on the ticket branch. Other inspected active routes already point to approved V003 or archive destinations. Empty-directory cleanup was not attempted because the hash gate is blocking. DEVOPS-02 remains open; the active Unresolved Register was not changed because its closure conditions are not fully met. No archived source, product asset, report, or RAW workflow record was modified. No stage, commit, push, PR, or merge was performed. See the [Corrective Ticket 01 Phase 03 report](../V003_VERSION_UPGRADE_BRAINBOX/PHASE03_FIXES_BRAINBOX/V003_FIXES_REPORT_BRAINBOX.md) for the 88-row ledger and all 15 gates.


## Corrective Ticket 01 - Operator override and physical cleanup follow-up - 2026-10-16

The Operator approved a Ticket 01-only CRLF qualification. The archive has 88/88 manifest paths, with no missing or extra entries. Rechecking the exact representations found 82 raw worktree/manifest matches, 54 direct Git-blob/manifest matches, 48 byte-identical worktree/blob pairs, 40 CRLF-only worktree/blob differences, and 0 unexplained mismatches. The 40 EOL-only pairs include 34 where the worktree matches the raw manifest and the Git blob is LF-normalized, and 6 where the Git blob matches the manifest while the Windows worktree is CRLF-converted. The measured direct Git-blob match is 54/88; the phrase 88/88 Git blobs match is not accurate and is not used as a result. No archived file or manifest was altered.

Empty-directory-only cleanup was attempted at the authorized retired source after confirming zero files, zero tracked paths, zero reparse points and seven directory objects. Windows returned "You do not have sufficient access rights to perform this operation." for ordinary removal of all five leaf image folders: FOOTHIVE BOOTS IMAGES, FOOTHIVE CLASSIC SHOES IMAGES, FOOTHIVE LOGO + DARK MODE, FOOTHIVE SNEAKER IMAGES, and FOOTHIVE TIMBERLAND IMAGES. No directory was removed; all seven shells remain. No force, recursive deletion, privilege escalation, ownership, or ACL changes were attempted.

Disposition: CONTENT RETIRED - PHYSICAL CLEANUP BLOCKED. DEVOPS-02 remains open. Per the Operator directive, publication was not started because cleanup did not complete and no separate partial-publication authorization was given. See the [Ticket 01 Phase 03 report](../V003_VERSION_UPGRADE_BRAINBOX/PHASE03_FIXES_BRAINBOX/V003_FIXES_REPORT_BRAINBOX.md).


## Corrective Ticket 01 final cleanup acceptance - 2026-10-16

The Operator supplied evidence that the approved Git Bash `find ... -depth -type d -empty -print -delete` command removed all seven empty directory shells, followed by a successful absence check. Independent verification in this checkout confirms `AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/` does not exist and `git ls-files` returns zero paths beneath it. No directory shell is represented as a Git-tracked deletion.

The archive remains complete: 88 manifest entries, 88 archived files, exact path set, 0 missing and 0 extra. Ticket 01's approved CRLF-only qualification is recorded with the measured counts: 82 raw worktree/manifest matches; 54 direct Git-blob/manifest matches; 48 exact worktree/blob pairs; 40 CRLF-only worktree/blob differences; 0 unexplained mismatches. No archive file or manifest was rewritten. All 84 direct archived-to-V003 migration destinations remain present and byte-identical to their archived source files. The four historical README files remain in the archive and their separately authored current navigation targets exist.

**Final disposition:** SOURCE CONTENT RETIRED - ARCHIVE VERIFIED - MIGRATION VERIFIED - PHYSICAL SOURCE REMOVED. The prior access-denied entries above are retained as historical events and superseded by this final operator-evidence and checkout-verification record. DEVOPS-02 is resolved and removed from the active Unresolved Register; its evidence remains in the Phase 03 report and Migration Map.


## RET-2026-10-16-LEGACY-AUTHORITY — ARCHIVED / VERIFIED

- **Operator authorization:** V003 Corrective Ticket 02, 2026-10-16; branch v003/legacy-func-dob-ai-must-retirement.
- **Source set:** exactly 13 paths — eight agent FUNC source reports, FQ_MUST_README.md, FUNC_REQ_BRAINBOX.md, FUNC_WORKFLOW_BRAINBOX.md, root DOB_MUST_README.md, and AI_BRAINBOX/AI_MUST_README.md.
- **Archive destinations:** the 11 FUNC files are under RETIRED_ITEMS_BRAINBOX/FUNC_AI_BRAINBOX/; DOB_MUST_README.md and AI_MUST_README.md are directly under RETIRED_ITEMS_BRAINBOX/.
- **Manifest:** LEGACY_AUTHORITY_RETIREMENT_MANIFEST_BRAINBOX.json records each original path, archive path, raw SHA-256, byte counts, Git blob and checkout line-ending qualification.
- **Integrity:** all 13 live archive SHA-256 values and byte counts match the pre-move source baseline. Five files have CRLF worktree bytes while their Git blobs are LF-normalized; path-aware Git hashing confirms each archived file resolves to its original blob. No unexplained content mismatch was found.
- **Contamination:** [Reading ...] and [executed on device: ...] markers remain unchanged in DOB, AI_MUST, and FQ archived bodies. Earliest available Git evidence is commit 2291f0ec3e676d242610d709fbd4d0c4b03a92ce (2026-09-23); parent adf0ddf51c16c5775cf7c6310bcc11dbcef290f0 lacks these markers. Actor and cause are not established.
- **Authority disposition:** all 13 archived sources are RETIRED / HISTORICAL / NOT CURRENT OPERATING AUTHORITY. Current system-wide rules route to Governance; current AI/FUNC navigation routes to active READMEs. No replacement for the legacy local request/compliance procedure was invented; this remains an authority gap.
- **CORE/EXE boundary:** only the eight authorized CORE source-link destinations and the EXE Research source link were changed to point to the archive. Capability text and archived source bodies were not changed; current capability truth was not revalidated.
- **Recovery:** restore by copying the exact manifest-listed path set to the original locations only under a separately authorized recovery action; verify SHA-256 and resolve path collisions before restoration.
- **Publication:** commit `de4a74b96872b0b63f68a3f0c8fe4981e181f614` pushed on the ticket branch; PR #51 merged to `main` as `1e3bee82f2fcb7a02c3f5465ca3a325132713683`; local `main` and `origin/main` match. See the Ticket 02 Phase 03 report for the staged review and limitations.

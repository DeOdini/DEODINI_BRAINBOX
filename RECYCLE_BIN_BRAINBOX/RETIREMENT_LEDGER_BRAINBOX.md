# RETIREMENT_LEDGER_BRAINBOX

**State:** [PRESENT · POPULATED] — four authorized archive records: RET-2026-10-15-PROJ-WORKFLOW, RET-2026-10-16-LEGACY-AUTHORITY, RET-2026-10-16-SKILLS-MILESTONES, and RET-2026-10-23-PLAYWRIGHT-MCP.

Each later entry must record retirement ID, item type, original repository-relative path, purpose, reason, Operator approval/ticket, pre-operation SHA-256 and Git blob/commit where applicable, file manifest for directories, archive path, canonical/reference replacement, affected links, verification, recovery procedure, date, and publication references. Distinguish PROPOSED, AUTHORIZED, ARCHIVED, BLOCKED, and RESTORED.

Do not treat this ledger as standing authorization to retire protected or retained source files. Historical M20 empty-file retirements are documented in the V003 Migration Map, not retrospectively moved here.

## RET-2026-10-23-PLAYWRIGHT-MCP — ARCHIVED

- **Operator acceptance/publication authority:** The Operator's 2026-10-24 directive accepts the prior retirement and authorizes publication. The separate October 23 instruction has not been located; this retrospective record does not claim it was independently recovered. Codex's earlier execution remains historical; Git publication had not yet been authorized or performed at that time.
- **Item and original path:** Tool-generated directory `.playwright-mcp/` at the repository root, containing exactly one untracked accessibility snapshot. It was automatically created by Playwright navigation during ticket P01-FH-V02-STAGE-B-001 on 2026-10-22, contrary to that ticket's read-only boundary (AUTH-01).
- **Reason and classification:** Remove accidental tool output from the active root while preserving its original bytes and provenance. RETIRED TOOL OUTPUT; not current operating authority, approved canonical evidence, or a change to the Stage B compliance finding.
- **Manifest:** `page-2026-10-22T19-08-58-731Z.yml`; 10,868 bytes; pre-move and post-move SHA-256 `0bf5c93a90bc50246193a1a55f350d855c3f423c953149b57835eb9aa06b4401`. Untracked source; no source Git blob or commit exists.
- **Archive:** `RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/.playwright-mcp/page-2026-10-22T19-08-58-731Z.yml`. Technical folder and snapshot filenames preserved unchanged.
- **Verification:** Resolved source and destination were checked within the workspace; neither source folder nor archive parent was a reparse point. Exactly one ordinary source file was found; no destination collision existed. Native PowerShell Move-Item moved the folder. Source path is absent; archived size and SHA-256 match the recorded source.
- **Reference audit:** Repository text search found no references to the exact snapshot filename before retirement. Stage B's chat report retains the original path as historical provenance. Root and Recycle Bin navigation now identify the archive; no canonical application source was replaced.
- **Recovery:** Only under a new Operator instruction, verify the archived SHA-256 and move the directory back to the original root path after confirming that path is absent. Do not overwrite a newly created tool-output folder.
- **Scope:** Preserved the pre-existing modification to `POST_V003_MODIFICATIONS_BRAINBOX/POST_V003_MOD_CONVO_BRAINBOX.md`. No application source, branch, ref, staging area, deployment, or prior archived source body changed.


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


## RET-2026-10-16-SKILLS-MILESTONES — ARCHIVED / INTEGRITY VERIFIED

- **Operator authorization:** V003 Corrective Ticket 03, submitted 2026-10-16; dedicated branch `v003/skills-milestones-legacy-retirement`.
- **Source set:** exactly three files: the legacy `AI_BRAINBOX/SKILLS_AVAIL_AI_BRAINBOX/SKILLS_MUST_README.md`, plus `MILESTONES_BRAINBOX/MILESTONES_MUST_README.md` and `MILESTONES_BRAINBOX/MILESTONE_CHECKPOINT_BRAINBOX.md`.
- **Archive destinations:** the legacy Skills README is under `RETIRED_ITEMS_BRAINBOX/SKILLS_AVAIL_AI_BRAINBOX/`; both historical V002 milestone files are under `RETIRED_ITEMS_BRAINBOX/MILESTONES_BRAINBOX/`.
- **Manifest:** `RECYCLE_BIN_BRAINBOX/SKILLS_MILESTONES_RETIREMENT_MANIFEST_BRAINBOX.json` records original/archive paths, raw SHA-256, byte sizes, line counts, CRLF counts, baseline Git blob IDs, and path-aware blob qualification.
- **Integrity:** all three archive files match their source pre-move raw SHA-256 and byte size. Path-aware Git hashing at each original source path reproduces its baseline Git blob. The Windows worktree used CRLF with `core.autocrlf=true`; Git's LF-normalized blob sizes are 1,353 bytes, 26,420 bytes, and 2,230 bytes respectively. This representation difference is explained; no source/archive byte mismatch exists.
- **Skills disposition:** the old `SKILLS_AVAIL_AI_BRAINBOX/` source directory is physically absent. `AI_BRAINBOX/SKILLS_AI_BRAINBOX/` remains the sole active Skills master. The four empty Skills placeholders previously retired in M20 remain retired; no Skills content or capability was added or promoted.
- **Milestones disposition:** the active folder contains exactly `README_MILESTONES_BRAINBOX.md` and `BRAINBOX_ROUTER_AGENTIC_MILESTONE_BRAINBOX.md`. The latter's `[PLANNED]` status and original bytes are unchanged. The historical V002 README and checkpoint are archived separately, not folded into Router intent.
- **Authority precedence:** this Ticket 03 Operator authorization supersedes prior retain-at-source and 2026-10-15 relocation statements for these exact three files only. Prior M17/F04, F10, and relocation entries remain historical and are not erased. No other milestone source was moved.
- **Recovery:** restore from the Ticket 03 manifest only under a separate Operator-authorized action; check for destination collisions and verify raw SHA-256 before restoring. Do not overwrite active material.
- **Current navigation:** root, AI, Skills, Governance, Milestones, and Recycle Bin routes were updated. The archived Skills body retains its F08 routing banner and one historical DOB link: four relative Markdown destinations in that preserved source body no longer resolve from the archive location. They were not edited; the Recycle Bin README supplies valid external routes to current root, Skills, and Governance navigation. These four historical-body link failures are not current navigation links.
- **Publication at initial checkpoint:** implementation was not yet committed. The initial git mv cached diff showed R100 for all three pairs, then was unstaged while Gate 12 wording was clarified. The later Operator direction below supersedes that hold; final staged review and Git lifecycle are recorded in the appended closeout.

## Corrective Ticket 03 — Gate 12 clarification and revalidation — 2026-10-16

The Operator clarified that Gate 12 permits only navigation/tree/archive-link/status/retirement edits to the active Milestones README. The Router/Agentic record remains byte-identical and `[PLANNED]`. The earlier hold is superseded for current status.

Revalidation confirmed all three raw source/archive hashes and sizes and all path-aware baseline blobs; both V002 paths and old Skills directory are absent; active Skills and Milestones structures match; Router and frozen authorities match their baseline raw hashes and blobs; the 15 current changed Markdown files have 155 local targets with 0 broken; the full staged scope contains 18 extant Markdown files and 159 targets, with four unresolved links only in the unchanged archived Skills source body. The earlier 154/0 result was a narrower scan. Staged rename and whitespace checks and Git closeout are recorded after completion.

Ticket 03 staged-path review (2026-10-16): 19 path records, 3/3 exact R100 moves, no unstaged or untracked changes, and both staged/worktree whitespace checks passed. Only the authorized Ticket 03 scope is staged; commit and publication follow.

## Corrective Ticket 03 - publication closeout - 2026-10-16

The three authorized retirement records were published byte-preserving under implementation commit `a85890972e8eeb4951f80f2dc5d0db7e8ab86aec` on retained branch `v003/skills-milestones-legacy-retirement`, then merged through [PR #53](https://github.com/DeOdini/DEODINI_BRAINBOX/pull/53). GitHub merge commit: `b6ccd6bb3815dc2a88f9f19384710dd8802d4eb8`. The PR included all three source-to-archive moves as R100. Their source/archive SHA-256, byte-size, and path-aware baseline blob matches remain recorded above.

Local `main` was fast-forwarded to the merge commit and matched `origin/main` with a clean worktree at that checkpoint. The implementation branch remains available for audit. This publication record does not authorize further source retirement or Milestones migration and does not assert overall V003 closure.

### Supplemental GitHub main policy check - 2026-10-16

The GitHub branch metadata endpoint reports `main` as `protected: false`, with `protection.enabled: false` and required-status-check enforcement `off` (empty contexts/checks). The repository rulesets endpoint is empty. This supplements the earlier unavailable dedicated protection endpoint and records the later branch metadata result. No additional source retirement is authorized by this note.

## RET-2026-10-16-LEGACY-AUTHORITY - supplemental contamination inventory - 2026-10-18

**Relationship to Ticket 02:** This dated supplement preserves the historical three-file observation above. The original Ticket 02 text and its three-file scope remain unchanged. The manifest's original contamination_provenance.affected_archived_paths list also remains unchanged; a separate supplemental_discoveries entry preserves the later five-file inventory.

**Later finding:** Review of commit 2291f0ec3e676d242610d709fbd4d0c4b03a92ce and its parent adf0ddf51c16c5775cf7c6310bcc11dbcef290f0 found the same two marker families in five then-current source files. The parent contains no matching lines in those five original paths. The additional files omitted from the original three-file record are the archived ChatGPT FUNC record and FUNC workflow record. This proves marker-text presence in the recorded commit objects; it does not prove the named actions occurred or identify an actor or cause.

**Recomputed worktree/archive integrity on 2026-10-18:** core.autocrlf=true. The baseline Git blob was read from each original source path at Ticket 02 baseline 506ad69e705ea0964eebd62ea96f559633df8331 and compared byte-for-byte with the current archive Git blob at 9e7f632e768f109eb8526a4099cb7343bd1a2f1b. All five blob IDs and blob bytes match. Current worktree hashes and EOL counts follow:

| Current archived path | Current raw bytes; SHA-256 | Ticket 02 raw bytes; SHA-256 | CRLF; lines | Baseline/current Git blob | Raw comparison |
|---|---|---|---:|---|---|
| RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/DOB_MUST_README.md | 10455; 63878fd12c3237f5f67d4a6d05de7b58bfd5e5222c6a7e6b9eaa8227424dd766 | 10455; 63878fd12c3237f5f67d4a6d05de7b58bfd5e5222c6a7e6b9eaa8227424dd766 | 206; 207 | 072645b4486645cbb153fb0fb5d8ae7d705c4abf (10249 bytes; archive blob identical) | MATCH |
| RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/AI_MUST_README.md | 3360; 9ad2d4f5f6873321e91f94e84071b2d2ebd87497f729ee304017be4c8c63384b | 3360; 9ad2d4f5f6873321e91f94e84071b2d2ebd87497f729ee304017be4c8c63384b | 78; 79 | e382886fdbaab695d3109115128324b9be99d24d (3282 bytes; archive blob identical) | MATCH |
| RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/FUNC_AI_BRAINBOX/FQ_MUST_README.md | 4972; 6cd454a665f571cb9a7b7b2c31cc255daf2a07f7ffb1be1beefe90b30952d347 | 4972; 6cd454a665f571cb9a7b7b2c31cc255daf2a07f7ffb1be1beefe90b30952d347 | 105; 106 | d496245c56e6bd8b8e766bbc7de406c3f1471dbc (4867 bytes; archive blob identical) | MATCH |
| RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/FUNC_AI_BRAINBOX/CHATGPT_FUNC_BRAINBOX.md | 19160; 8d3493babc52044209283f7589922a29daa24179c6e68f713b25952150bd5cde | 18960; b51ec60e262cd96618074dbd86f893a02c35143cc0fea9e385c85235eaabd0d0 | 200; 201 | cd3a9db62d101309e090029b53b91da7c201711b (18960 bytes; archive blob identical) | DIFFERS; LF-normalized SHA matches Ticket 02 |
| RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_WORKFLOW_BRAINBOX.md | 12086; 050ecab6849f3a264130593e3be9af64eae31c4009bea5af4714cd15e6a6e046 | 11857; 7a73a3b43226ddd5eb9c6119274b95f2bd623d5fdb30a30573d65447ae5602bd | 229; 230 | 7a6e609161c22903f8ba66f10fa626eb2b3c4dab (11857 bytes; archive blob identical) | DIFFERS; LF-normalized SHA matches Ticket 02 |

The two raw-worktree differences are CHATGPT_FUNC_BRAINBOX.md (200 CRLF sequences; LF-normalized size 18,960 bytes and SHA-256 equals its Ticket 02 recorded raw SHA-256) and FUNC_WORKFLOW_BRAINBOX.md (229 CRLF sequences; LF-normalized size 11,857 bytes and SHA-256 equals its Ticket 02 recorded raw SHA-256). Neither file contains a bare LF or bare CR. The other three current raw worktree hashes and sizes match their Ticket 02 manifest values. The original source blobs and current archive blobs match for all five. The archive sources were not edited.

Current archived marker line references remain: DOB lines 4, 6, 8, 203, 205, 207; AI_MUST lines 4, 79; FQ lines 4, 6, 104, 106; ChatGPT FUNC lines 1, 201; FUNC workflow lines 1, 3, 228, 230. Actor and cause remain unknown. See the dated [Phase 03 implementation report](../V003_VERSION_UPGRADE_BRAINBOX/PHASE03_FIXES_BRAINBOX/V003_FIXES_REPORT_BRAINBOX.md) for the complete per-file hash table and bounded review results.

**Disposition:** Inventory correction only. No archived source content, original removal authorization, or Ticket 02 checkpoint was changed.

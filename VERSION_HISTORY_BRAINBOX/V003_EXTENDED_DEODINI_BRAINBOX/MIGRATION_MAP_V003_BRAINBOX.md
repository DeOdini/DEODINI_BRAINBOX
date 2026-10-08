# MIGRATION_MAP_V003_BRAINBOX

**Ticket:** V003-M01 — Current-State Inventory, Integrity/Recovery Baseline & Migration Map Bootstrap  
**Status:** Living M01–M21 migration ledger — M01, M02, and M03 independently verified PASS; M03-REF-01 batch-deferred/non-blocking and assigned to M19/M20; M04 dependency-eligible under its own P14 preflight; legacy sources retained; Batch A Git lifecycle pending  
**Baseline date:** 2026-10-08  
**Repository:** C:\Users\USER\DEODINI_BRAINBOX  
**Active branch:** v003/m01-current-state-inventory-migration-map  
**Baseline commit:** 27e73f828bb367298442c2e621c18d1cc1ceb4f4

## Purpose and operating rule

This is the living, source-backed Phase 02 migration ledger. It captures the actual repository state before migration and gives later tickets a baseline for source verification and recovery. It is updated by each authorized V003-Mxx ticket and closed by M21.

Every tracked file appears individually in the inventory manifest. Its **Family** column links it to the source-profile table below, which records content role, authority, target candidate, state, handling, evidence sensitivity, source-removal eligibility, dependency, and flags. A family groups metadata only; it does not authorize merging or treating separate files as one content source. Later tickets must record file-specific final dispositions and any split/merge details.

No source file or folder was renamed, moved, deleted, or rewritten by M01. The only product-tree artifact created by M01 is this migration ledger. Phase 02 conversation/report records document the execution separately.

## 1. Authority and P14 preflight

### Canonical authorities

- C:\Users\USER\DEODINI_BRAINBOX\V003_VERSION_UPGRADE_BRAINBOX\V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md — chronological historical evidence and ambiguity source.
- C:\Users\USER\DEODINI_BRAINBOX\V003_VERSION_UPGRADE_BRAINBOX\V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md — approved and frozen V003 migration-target authority.

### Supporting execution authorities

- V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_PHASE02_MIGRATION_TICKETS_BRAINBOX.md — authorized M01–M21 ticket scopes and P14/reporting rules.
- V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/README_PHASE02_MIGRATION_BRAINBOX.md — Phase 02 authority boundary, one-ticket-at-a-time execution, dependency and stop/report/wait rules.
- V003_VERSION_UPGRADE_BRAINBOX/README_V003_VERSION_UPGRADE_BRAINBOX.md — V003 authority-container and phase boundary.
- V003_VERSION_UPGRADE_BRAINBOX/PHASE01_POLISH_BRAINBOX/README_PHASE01_POLISH_BRAINBOX.md — Phase 01 archive marked populated and Phase 01 closed/frozen.

The M01 ticket was read in full. The frozen Specification’s target tree, FUNC, Skills, FootHive, Version History, and migration-rule sections were cross-checked. The Origin Conversation’s operating-model and historical-authority sections were reviewed. Current content, Git refs/status, source paths, and migration-support records were inspected. Phase 01 is recorded as CLOSED / FROZEN. M01 is dependency-eligible.

### Operator clarification — Version History parent README

The Operator clarified on 2026-10-08 that the GitHub compact-folder display is only a presentation of the nested path and that the Version History parent should receive its own README during migration. ChatGPT's independent M01 verification found that the recorded compact-folder discussion does not itself prove explicit approval of a placeholder treatment. V003-M04 explicitly targets creation/reconciliation of README_VERSION_HISTORY_BRAINBOX.md if it is still absent. Placeholder-specific Operator authorization remains unverified and must not be inferred.

The frozen Specification §8 already names VERSION_HISTORY_BRAINBOX/README_VERSION_HISTORY_BRAINBOX.md, and M04’s authorized target includes it. It is absent from the current repository. This decision is assigned to M04; M01 does not create it and does not alter the two-level directory structure.

## 2. Pre-migration repository and Git baseline

| Field | Verified baseline |
|---|---|
| Repository | C:\Users\USER\DEODINI_BRAINBOX |
| Current branch | v003/m01-current-state-inventory-migration-map |
| Current HEAD | 27e73f828bb367298442c2e621c18d1cc1ceb4f4 |
| HEAD commit | “Record Version History directory display finding” |
| Commit author / date | pedestal-archive <deodinihq@gmail.com> / 2026-10-08T04:55:41-05:00 |
| Current branch upstream | None configured |
| Local main upstream | origin/main |
| Local main | 27e73f828bb367298442c2e621c18d1cc1ceb4f4 |
| origin/main tracking ref | 27e73f828bb367298442c2e621c18d1cc1ceb4f4 |
| Live GitHub main | 27e73f828bb367298442c2e621c18d1cc1ceb4f4, confirmed with git ls-remote |
| main vs origin/main | 0 ahead / 0 behind |
| M01 branch vs origin/main | 0 ahead / 0 behind; same baseline commit |
| Working tree before M01 | Clean |
| Untracked/ignored working-tree files before M01 | None reported by git status --untracked-files=all --ignored |
| Tracked files before M01 | 122 |
| Remote | origin → https://github.com/DeOdini/DEODINI_BRAINBOX.git |
| Relevant refs | refs/heads/main; refs/heads/v003/m01-current-state-inventory-migration-map; refs/remotes/origin/HEAD; refs/remotes/origin/main |

The actual local root also contains a physical empty BRAINBOX/ directory with zero child entries. Git does not track the empty directory; it does not appear in the Git file list or status. It is separately recorded here as an empty legacy directory for M20 review. No files are present in it.

### Repository recovery baseline and limits

The tracked migration sources are recoverable from Git history. The local main, origin/main tracking ref, live GitHub main, and M01 branch all point to the same verified commit. For each future migration ticket, preserve the pre-change source in the parent commit, work on its ticket branch, verify destinations and source hashes before any permitted retirement, commit and push the branch under the approved branch/PR workflow, and retain the prior commit as the tracked-file rollback point. Do not force-push or merge to main without the applicable Operator authority.

No Git bundle was created for M01. The live remote main was independently checked and matches the local baseline. This Git-history method covers committed/tracked content only. It does not back up external files/configuration or untracked/ignored files. The working-tree check found no untracked or ignored files; the empty BRAINBOX/ directory is listed separately because Git cannot preserve it. No other files outside this repository were inventoried by this ticket.

### Object-integrity check and recovery flag

Command: git fsck --full --no-reflogs  
Result: 72 dangling objects; no missing-object, corruption, or fatal-error output. The object store reported 527 loose objects (5.01 MiB), two packs (33.46 MiB), and zero garbage objects.

Twenty dangling commits are labeled as Cline checkpoint commits authored by pedestal-archive on 2026-09-23 and 2026-09-24. Their IDs are:

- 11608d5fe238aa928595035adea0515db160c9b1
- 4128193b9cddeb3f9606aa145e947c7abf35f72a
- 42386db997a573f1edfd6c353dd8d9acbb2db109
- 6518b841b4c59eb0564fdc7a9009ae3781a97121
- 8a103985eb7323c7fb72b072ec162cc3bb4ab9a4
- 8f00cc259c7a4074a6ad53c51a26cd6811df8640
- 1bf22dc96e57dfbe13550b7a12e82b3535745fcb
- 4da2542aeca39e2e1dac1b3ffb5d8952fca4b3c8
- 581a249a9c254e344a35827c73486518b4a2f728
- 5c739bead1d50105eeb2e89bdbdb8937036cfa5b
- dfdc6754d5689a2a721843425532a8a43e6cfd54
- 042dd7da838115b9661f837ed078c9c568e7be7b
- 284da10ab19547a318aa82381bac6575c8729c08
- 16a6707b3f28cc7029f31a5c42d99b5a18599501
- 49b690d3739b10c050e36f9edf3afede2fc3ac8a
- b2eef868d0397063b710d133b014cfe0840b0fa7
- d74eeb19539aba111f08e81c2a6e5e789513cf69
- 2d77921bb3cc1392e3479020070729e7c98bf2fa
- 70071e5a7f07e0c5fd1327af1fd8e06ef0366ef0
- a9ef3d7dcd5a7533ab6fcd661356ed2890c15dbf

The remaining 52 dangling objects are non-commit objects. These checkpoint objects are not reachable from the current branches or GitHub main. M01 did not delete, prune, expire reflogs, or rewrite them. **FLAG M01-GIT-01:** preserve these objects; do not run garbage collection/pruning or expire reflogs during migration until their disposition is explicitly reviewed. The tracked-file recovery baseline is verified; the checkpoint-object recovery is local-only and remains a distinct unresolved recovery flag.

## 3. M01 baseline root paths and authority records

This section preserves the repository state recorded before M01. It is a historical pre-migration baseline, not the current post-M02 tree. Section 11 records M02's current root-authority disposition.

M01 pre-ticket physical root children:

- AI_BRAINBOX/
- BRAINBOX/ — physically present and empty; untracked because empty.
- MILESTONES/
- PORTFOLIO_BRAINBOX/
- V003_VERSION_UPGRADE_BRAINBOX/
- VERSION_HISTORY_BRAINBOX/
- DOB_MUST_README.md

At the M01 baseline, there was no root README_BRAINBOX.md; the frozen target defined its creation for M02. There was no VERSION_HISTORY_BRAINBOX/README_VERSION_HISTORY_BRAINBOX.md; the Operator clarification above assigns its creation, if still absent at M04, to that ticket.

M01 pre-ticket governed README/authority records included:

- DOB_MUST_README.md
- AI_BRAINBOX/AI_MUST_README.md
- AI_BRAINBOX/FUNC_AI_BRAINBOX/FQ_MUST_README.md
- AI_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_REQ_BRAINBOX.md
- AI_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_WORKFLOW_BRAINBOX.md
- AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/PROJ_MUST_README.md
- AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/RAW_WORKFLOW_PROJ_BRAINBOX/RAW_PROJ_MUST_README.md
- AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/RAW_WORKFLOW_PROJ_BRAINBOX/FULLSTACK_RAW_BRAINBOX/FSTACK_MUST_README.md
- AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FH_MUST_README.md
- AI_BRAINBOX/SKILLS_AVAIL_AI_BRAINBOX/SKILLS_MUST_README.md
- MILESTONES/MILESTONES_MUST_README.md
- V003_VERSION_UPGRADE_BRAINBOX/README_V003_VERSION_UPGRADE_BRAINBOX.md
- V003_VERSION_UPGRADE_BRAINBOX/PHASE01_POLISH_BRAINBOX/README_PHASE01_POLISH_BRAINBOX.md
- V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/README_PHASE02_MIGRATION_BRAINBOX.md
- V003_VERSION_UPGRADE_BRAINBOX/V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md
- V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md
- V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_PHASE02_MIGRATION_TICKETS_BRAINBOX.md
- VERSION_HISTORY_BRAINBOX/V003_EXTENDED_DEODINI_BRAINBOX/ARCHITECTURE_DECISIONS_V003_BRAINBOX.md

At the M01 baseline, the two canonical V003 authorities and Phase 01/02 support archives were separate. The root README was not yet created; the Version History parent README, V001/V002 history, and most V003 operational target branches were also not yet migrated.

## 4. Inventory summary

The manifest at the end of this file lists all 122 tracked files with source family, exact repository path, byte size, physical text-line count where practical, and SHA-256. Raster-image line count is N/A. The source tree and content roles were inspected sufficiently to assign the family profiles below; visual review of every image is not claimed.

| Current source family | Current state / content role | Target candidate and dependent ticket | Handling / split or merge | Evidence sensitivity and integrity | Removal eligibility | Flag |
|---|---|---|---|---|---|---|
| ROOT-AUTH | At the M01 baseline, DOB_MUST_README.md was the live legacy root authority; it included root navigation and system-wide rules. | Root README_BRAINBOX.md created in M02; Governance content to Governance (M03); global reconciliation M19. | M02 created root navigation/tree authority from the frozen Specification; DOB_MUST_README.md is retained unchanged. Do not copy its policy wholesale; M03 owns Governance classification. | Authority-bearing; pre-M02 source integrity is in the manifest; post-M02 unchanged-source check is recorded in Section 11. | No removal in M02; only M20 after destination/reference/integrity verification. | None; root navigation destination now exists. |
| AI-ENTRY | AI_MUST_README is the live AI-subsystem entry/navigation authority. | AI_BRAINBOX/README_AI_BRAINBOX.md (M02/M19); governance-specific rules to M03 where supported. | Separate local navigation from global policy; no blind copy. | Authority-bearing; baseline in manifest. | Only M20 after destination/reference verification. | Future target not yet populated. |
| FUNC-AGENT | Flat ChatGPT, Claude, Cline, Codex, Copilot, DeepSeek, Grok, and Qwen capability reports. | FUNC CORE M05 and evidence-backed EXE index M06. | Content-map each agent report; DeepSeek/Qwen files are pending-report notices only and must not migrate as empty CORE records. | Capability/provenance claims; hashes recorded. | No source retirement until M20 and verified target. | Agent statuses are time/environment dependent; M05 re-verifies. |
| FUNC-ANCILLARY | FQ_MUST_README, FUNC_REQ, FUNC_WORKFLOW are compliance, request, and operational workflow records. | M07; system rules may be referenced by M03. | Mixed content must be classified, split only if ticketed, and referenced to one canonical owner. | Authority/process-sensitive; hashes recorded. | Only M20 after canonical ownership and references verify. | Exact target is decided from content in M07. |
| PROJECT-LEGACY | PROJ_MUST_README plus empty PROVEN_PATTERN and FAILED_PATTERN source records. | DEVOPS RAW/FAILED/PROVEN reconciliation M09. | Preserve actual emptiness; do not fabricate successful or failed workflow evidence. | Empty files have SHA-256 e3b0c442…; source paths recorded. | Potential M20 retirement only after M09/M19 evidence. | Destination/empty-file disposition remains ticketed. |
| FULLSTACK-RAW | RAW_PROJ_MUST_README, 001 raw workflow, 002 preset workflow, FSTACK_MUST_README. 001 and 002 are explicitly not proven. | Fullstack workflows/architecture/orchestration M10; Skills references may be considered in M08 only if supported. | Separate workflow procedure from architecture, orchestration, test procedure, deployment, and agent handoff based on actual content. Do not merge 001/002 merely because they are variants. | Historical/raw process evidence; hashes recorded. | Only M20 after M10 disposition and link checks. | Legacy links/status statements remain to be reconciled by M10/M19. |
| FH-TRIAL | Six direct FootHive records: README, build report, passed, failed, conversation, Operator addendum. | Canonical Sandbox case study M15; production/portfolio summaries later M16. | Keep canonical trial evidence together; Production/Portfolio reference rather than duplicate it. Iteration 01 is current dataset; 02/03 and mastery remain planned. | Historical evidence; all six hashed, with size/line counts. | Keep original until M20 after byte/hash comparison at destination. | No physical iteration layout guessed in M01. |
| FH-EVIDENCE | 37 tracked evidence files under EVIDENCE: screenshots, Playwright page captures, logs, YAML snapshots. | EVIDENCE_FH_BRAINBOX under M15. | Preserve each evidence item and ticket subfolder; verify source/destination bytes and SHA-256 before any source retirement. | High historical sensitivity; individual hashes in manifest. | Only M20 after verified transfer. | Evidence folder layout is target-defined; exact per-file disposition remains M15. |
| FH-ASSET | 40 tracked design/product/logo assets, including four image catalog Markdown files. Assets are not automatically evidence. | M15 must classify design reference, product/source asset, portfolio reference, external project-repository asset, or unresolved. | Do not force source assets into EVIDENCE_FH_BRAINBOX; preserve them until M15 resolves exact targets. | Binary assets individually SHA-256 baselined; 11 existing exclusions are recorded in FAILED_FH_BRAINBOX.md. | No source removal in M01; M20 only after authorized destination and integrity checks. | M15 target for some asset classes is not authoritative yet. |
| SKILLS-LEGACY | SKILLS_MUST_README plus four zero-byte RAW/PROVEN/REUSABLE/FAILED placeholders. | Skills taxonomy and reconciliation M08. | Do not represent zero-byte files as reusable/proven/failed knowledge. | Four empty files hashed; no content evidence. | M20 only after M08/M19 establishes disposition. | Empty-state disposition remains M08. |
| MILESTONES-LEGACY | MILESTONES_MUST_README and the historical MILESTONE_CHECKPOINT. | Historical reconciliation M17; distinct planned Router milestone M18. | Do not rename the legacy folder into MILESTONES_BRAINBOX or merge historical checkpoint into planned milestone. | Historical governance/checkpoint; hashes recorded. | M20 only after M17/M18/M19 verify references. | Distinct historical vs planned authority must remain visible. |
| PORTFOLIO-LEGACY | 001_PORT_BRAINBOX.md is zero bytes. | FootHive Portfolio presentation/reference M16. | No portfolio claims or project history may be invented from an empty file. | Empty file baseline hash recorded. | M20 only after M16/M19. | No substantive source content exists. |
| V003-AUTHORITY | V003 parent README, Origin Conversation, Specification. | Retain authority container; M02 records its root navigation and support/archive boundary; global reconciliation M19/M21. | Specification says what V003 is; Origin Conversation preserves chronology/ambiguity. M02 updates only the V003 container README's current status/navigation; it does not rewrite or relocate either canonical authority. | Canonical/historical authority; pre-M02 hashes, sizes, and line counts are in the manifest. | Retain; no source retirement proposed. | None; preserve authority boundary. |
| PHASE01-ARCHIVE | Phase 01 README, polish conversation, polish report. | Retain as closed/frozen support archive under M02/M19/M21. | M02 lists this archive in the V003 support overlay, outside the operational target tree; keep execution/verification history separate from target-domain content. | Historical archive; pre-M02 hashes recorded. | Retain unless a later explicit scope authorizes otherwise. | None. |
| PHASE02-PROCESS | Phase 02 README, conversation, report, ticket set. | Retain as process/audit support; M01 updates the ledger and execution records; M02 records their support boundary; M19/M21 reconcile navigation. | These are process records, not operational domain knowledge or competing architecture authority. | Active authorization and execution history; manifest hashes remain the pre-M01 baseline values. | Retain. | Phase 02 README, conversation, and report are updated by ticket to show M02 implementation and independent-verification state; the Phase 02 support branch remains outside the operational target tree. |
| VERSION-HISTORY | One file currently exists: V003_EXTENDED_DEODINI_BRAINBOX/ARCHITECTURE_DECISIONS_V003_BRAINBOX.md. | Retain and verify it in M04; add parent README and evidence-backed V001/V002 artifacts only under M04. | This record explains why V003 evolved; it does not duplicate the Specification. The path is physically two nested directories. | Historical decision record; hash recorded. | Retain; no removal proposed. | Parent README absent now; M04 owns creation/reconciliation. Placeholder-specific Operator approval is not established by the current record. |

## 5. Current FootHive inventory and evidence boundary

FOOTHIVE_PROJ_BRAINBOX currently has 83 tracked files:

- 6 direct trial records: BUILD_REPORT_FH_BRAINBOX.md, CONVO_FH_BRAINBOX.md, FAILED_FH_BRAINBOX.md, FH_MUST_README.md, OPERATOR_ADDENDUM_FH_BRAINBOX.md, PASSED_FH_BRAINBOX.md.
- 37 evidence files:
  - EVIDENCE/T11-responsive-qa/ — 4 files.
  - EVIDENCE/T23-mobile-header/ — 11 files, including its Playwright CLI subfolder.
  - EVIDENCE/header-review/ — 2 files.
  - EVIDENCE/playwright/ — 20 files.
- 40 design/product/logo assets or asset-catalog files:
  - DIRECTION A & B IMAGES/ — 2 files.
  - FOOTHIVE BOOTS IMAGES/ — 10 files.
  - FOOTHIVE CLASSIC SHOES IMAGES/ — 10 files.
  - FOOTHIVE LOGO + DARK MODE/ — 2 files.
  - FOOTHIVE SNEAKER IMAGES/ — 5 files.
  - FOOTHIVE TIMBERLAND IMAGES/ — 11 files.

The 11 images already excluded in FAILED_FH_BRAINBOX.md remain excluded unless the Operator separately clears them: Timberland image02, image04, image05, image08, image13, image15, image16, image19; sneaker navy-tan-stripe.png; boot winged-cross-studded-western-boot.png; boot sunflower-embroidered-western-boot.png. Their originals and catalogs remain intact. M01 did not reclassify or visually re-review the remaining assets.

The four catalog Markdown files contain 32 embedded image references in total (9 boots, 9 classic shoes, 4 sneakers, 10 Timberland). The referenced subfolders boot-images/, classic-images/, sneaker-images/, and images/ do not exist under the respective current folders; the image files instead sit directly alongside each catalog. This is already recorded in FAILED_FH_BRAINBOX.md as a path mismatch. **FLAG M01-FH-01:** retain and surface this mismatch for M15; do not repair links or relocate assets during M01.

## 6. Empty legacy sources and known absence

Seven tracked zero-byte files exist:

- AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FAILED_PATTERN_PROJ_BRAINBOX.md
- AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/PROVEN_PATTERN_PROJ_BRAINBOX.md
- AI_BRAINBOX/SKILLS_AVAIL_AI_BRAINBOX/FAILED_SKILLS_BRAINBOX.md
- AI_BRAINBOX/SKILLS_AVAIL_AI_BRAINBOX/PROVEN_SKILLS_BRAINBOX.md
- AI_BRAINBOX/SKILLS_AVAIL_AI_BRAINBOX/RAW_SKILLS_BRAINBOX.md
- AI_BRAINBOX/SKILLS_AVAIL_AI_BRAINBOX/REUSABLE_SKILLS_BRAINBOX.md
- PORTFOLIO_BRAINBOX/001_PORT_BRAINBOX.md

Each is 0 bytes, 0 lines, and has the SHA-256 empty-file digest e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855. They are placeholders, not substantive migration evidence. Preserve their existence in this baseline; M08, M09, M16, M19, and M20 determine their eventual dispositions.

## 7. Material legacy-reference scan

A read-only search was run across 86 tracked text-like files at baseline commit 27e73f8 for material legacy/authority path strings. It found:

| Search string | Files containing references |
|---|---:|
| DOB_MUST_README.md | 11 |
| AI_MUST_README.md | 8 |
| PROJ_WORKFLOW_AI_BRAINBOX | 9 |
| RAW_WORKFLOW_PROJ_BRAINBOX | 8 |
| SKILLS_AVAIL_AI_BRAINBOX | 5 |
| MILESTONES/ | 7 |
| PORTFOLIO_BRAINBOX | 6 |
| FOOTHIVE_PROJ_BRAINBOX | 6 |
| VERSION_HISTORY_BRAINBOX | 7 |
| V003_VERSION_UPGRADE_BRAINBOX | 11 |

Representative current reference locations include DOB_MUST_README.md, AI_MUST_README.md, FUNC_WORKFLOW_BRAINBOX.md, PROJ_MUST_README.md, both RAW Fullstack records, MILESTONES_MUST_README.md, MILESTONE_CHECKPOINT_BRAINBOX.md, the V003 authorities, and the Phase 02 report/ticket file. These are not all broken links; they are cross-reference candidates. M19 must verify reference validity and ownership after target migration. The absent target README_VERSION_HISTORY_BRAINBOX.md is referenced by the frozen target and M04 ticket, not present as a current file.

## 8. Integrity manifest

The following appendix is the pre-migration inventory as verified from the working tree at baseline HEAD. SHA-256 and byte size apply to the exact current source files. Text-line counts use physical line terminators, without counting a trailing terminator as an extra blank line. Binary images use N/A for line count.

## 9. M01 completion boundary and ledger update protocol

M01 establishes the baseline only. It does not implement any M02–M21 migration. Unknown destinations remain TBD and are not inferred from folder names. Future ticket updates must append the ticket ID, authorization/dependency status, pre-state, exact source and destination paths, source/destination SHA-256 and size where practical, verification result, retained/retired disposition, unresolved flags, and commit/push/merge state. Source removal is never implied by a target candidate; M20 owns authorized retirement checks, and M21 closes the map from actual evidence.

**M01 source removals/moves/renames:** NONE.  
**M01 source edits:** NONE.  
**M01 new ledger:** this file.  
**Unresolved flags:** M01-GIT-01; M01-FH-01; future target dispositions identified in the source-family table.  
**Codex verification:** inventory and metadata generated from live filesystem/Git state; independent ChatGPT verification remains pending.


| Family | Current repository path | Bytes | Physical lines | SHA-256 |
|---|---|---:|---:|---|
| AI-ENTRY | AI_BRAINBOX/AI_MUST_README.md | 2811 | 76 | df7ac175b778d52ebe7779a17e6eee44b8a4c92b450bf85d563624b922f37fa6 |
| FUNC-AGENT | AI_BRAINBOX/FUNC_AI_BRAINBOX/CHATGPT_FUNC_BRAINBOX.md | 18960 | 201 | b51ec60e262cd96618074dbd86f893a02c35143cc0fea9e385c85235eaabd0d0 |
| FUNC-AGENT | AI_BRAINBOX/FUNC_AI_BRAINBOX/CLAUDE_FUNC_BRAINBOX.md | 7897 | 123 | 5d3ddc0591dc3bd4073ef02b25e5c392421ac6b0d7feb884cdfcdf52151341a5 |
| FUNC-AGENT | AI_BRAINBOX/FUNC_AI_BRAINBOX/CLINE_FUNC_BRAINBOX.md | 18777 | 530 | 3379ae99682c054e4ae07da1cb97d489af66956a2c92c5531c64f008848747c3 |
| FUNC-AGENT | AI_BRAINBOX/FUNC_AI_BRAINBOX/CODEX_FUNC_BRAINBOX.md | 6636 | 86 | 359b35d7a8f7a6eba12554cf8c73c2c044f578d122832f0b1454f74ec2592648 |
| FUNC-AGENT | AI_BRAINBOX/FUNC_AI_BRAINBOX/COPILOT_FUNC_BRAINBOX.md | 12920 | 232 | 12e736bc20fc12654363ec00ca44b27e87851fe96c7dfd95c98c36418347d390 |
| FUNC-AGENT | AI_BRAINBOX/FUNC_AI_BRAINBOX/DEEPSEEK_FUNC_BRAINBOX.md | 143 | 3 | bcd67420a91cebabef5aabdebbe8ff8ba1679627798397d12f13a2f2a1d1cb57 |
| FUNC-ANCILLARY | AI_BRAINBOX/FUNC_AI_BRAINBOX/FQ_MUST_README.md | 4387 | 103 | edfff2651ab1005a8d166c06df9553bd8a4f82ba4508d648dbbd8b680365fab9 |
| FUNC-ANCILLARY | AI_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_REQ_BRAINBOX.md | 4943 | 111 | e2d9ec14ca1d96703fca5be75316a92efa261b245307923be9f78cb986bd8e90 |
| FUNC-ANCILLARY | AI_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_WORKFLOW_BRAINBOX.md | 11857 | 230 | 7a73a3b43226ddd5eb9c6119274b95f2bd623d5fdb30a30573d65447ae5602bd |
| FUNC-AGENT | AI_BRAINBOX/FUNC_AI_BRAINBOX/GROK_FUNC_BRAINBOX.md | 9056 | 199 | 0d74fc8323e5da70e7cc58775527c0b56ac127eeca8414192becf9bfc222f69f |
| FUNC-AGENT | AI_BRAINBOX/FUNC_AI_BRAINBOX/QWEN_FUNC_BRAINBOX.md | 135 | 3 | 43a14aef28a28631cbd9179a65dd927f175f244362a204d58fa044271f4e9de7 |
| PROJECT-LEGACY | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FAILED_PATTERN_PROJ_BRAINBOX.md | 0 | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| FH-TRIAL | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/BUILD_REPORT_FH_BRAINBOX.md | 159133 | 2427 | 83e1724b146db02e62663b9a788b7f76cee2a96460dc6fee36fcbc2f97d12a9f |
| FH-TRIAL | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/CONVO_FH_BRAINBOX.md | 166094 | 4279 | c5151958347e98e1df90ab9a98a85ef65d792f73f39b4b763af69cb3a9f1c091 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/DIRECTION A & B IMAGES/37n4T (DIRECTION B).jpg | 277800 | N/A | 90eea2c42ef2df1509d17f9712b0f277caf1f1bee1d6c6331d1e86e6cb4fd9db |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/DIRECTION A & B IMAGES/FZxXm (DIRECTION A).jpg | 238564 | N/A | 91fedc0e35796ffc017bd2b8241b8f2a651a707349abf756a7da516a9a9c7e66 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/T11-responsive-qa/edge-1440x900.png | 91494 | N/A | 485bb830efb79254d464d4cc2bd38829e082589e3139100a16e2746ed05fd3a1 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/T11-responsive-qa/edge-320x780.png | 22092 | N/A | d41894343f0e545c1182b3ee9c574b3f54ec4b6f93e0c53c8569ea8efacbf002 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/T11-responsive-qa/edge-390x844.png | 23761 | N/A | 6104383e7232e0e19ad53f1a6f31202dc13c12012a05b12e39d72fe52bc18015 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/T11-responsive-qa/edge-768x1024.png | 38229 | N/A | f202f619870d38d98568bf51e79846a27c64ae7fac93f5be952004dd8c549117 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/T23-mobile-header/desktop-1440-after.png | 93051 | N/A | b94ac3e53679b9ad8fb67f919b90d9df5c74c1605caf49c5cce8069f7883ec02 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/T23-mobile-header/mobile-320-after.png | 24050 | N/A | a95d5882d2215aaaae0669c7d5a7dea59dee9e5a665f4c66f1208bc6133bda47 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/T23-mobile-header/mobile-320-before-simulated.png | 24033 | N/A | f12d7804115b5c96ab37aabe9fdef690f7f4d07d62ea0138d6f35fb082040082 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/T23-mobile-header/mobile-390-after.png | 25590 | N/A | 5cdb70d5f7cee5aa4dba8751583022f16e721b5235f40f9667fdc3445099c87b |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/T23-mobile-header/mobile-390-before-simulated.png | 25586 | N/A | 2b5e6cb9843f7517a821c015f2beb5a40778d815c7866f27f1aacca2224089aa |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/T23-mobile-header/playwright-cli/console-2026-10-03T13-56-08-136Z.log | 181 | 1 | c6074eaeae071e64392bed739ac77b4c52483fba51fa6caeb3d7c07f76870515 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/T23-mobile-header/playwright-cli/console-2026-10-03T14-16-15-547Z.log | 181 | 1 | 486100594d14c730e446ef84b2d51aa182b20d969bb6ba93a7a46e50631dd180 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/T23-mobile-header/playwright-cli/page-2026-10-03T13-56-12-224Z.yml | 10921 | 212 | 2ed8bd3c91ffc6e98d2c2fa01ec3f6c5a4a51068b138bcfde8840d80cf5616b0 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/T23-mobile-header/playwright-cli/page-2026-10-03T14-00-15-971Z.yml | 12224 | 228 | 70607e0a4ada7cfeec55db51829dcffc2c60ee061bff6b984890c00b18d434b8 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/T23-mobile-header/playwright-cli/page-2026-10-03T14-16-19-258Z.yml | 10921 | 212 | 2ed8bd3c91ffc6e98d2c2fa01ec3f6c5a4a51068b138bcfde8840d80cf5616b0 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/T23-mobile-header/tablet-768-after.png | 39641 | N/A | 41390f438002ff42767d743741afdc600fb5a01ee63cb7fe689fc46efd64a748 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/header-review/screenshot-12-localhost-cropped.png | 1001208 | N/A | a49f8eb8182c411266a153fafcab8e87daaabaefbd0493445511452ba9ff8f45 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/header-review/screenshot-13-deploy-preview-cropped.png | 935185 | N/A | 99bf84b4c80b2574cb8c6b203a18bd234072abc9bac2ca86dcc7a56c17c72291 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/console-2026-10-01T18-51-20-395Z.log | 102735 | 74 | 728e5fe75b0c9eaeaab8380b5eb9a8b21d059e83424273990d33a4fea732d9f9 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/console-2026-10-01T18-57-44-828Z.log | 132 | 1 | 096fb55be01da66105f1f0e62c1737f9cddc550107334c0c93bd1ce6dd855e7e |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-08-32-992Z.yml | 11419 | 212 | b073bf6566231d3643de243cb854e63248c8875c19a80046fb62b078f97fea13 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-09-19-257Z.yml | 12626 | 228 | 554419f33666662faded3d34f5796c1355e9bc3e8520ea43b33ce43ead99c184 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-09-36-471Z.yml | 12284 | 221 | 45214962d7d07c62a853b4bc653411e015b55d0a9aadca9fea0f1c25b977b0bc |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-10-26-452Z.yml | 11419 | 212 | d6d761e01f8db0ba53bc79c7677d0992c6ecc466e9e19f62718f6b9136656d3d |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-11-33-563Z.yml | 11495 | 213 | 383696a99545ef3504ae3e72d47ec928f9a4d854174dd36e99fdea5a8e9fd2a7 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-17-09-465Z.png | 34988 | N/A | a7db7c81601cddc08ecbde58e54bc4cd36da81b16f0a7c6419c01df2dc96812a |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-23-32-165Z.yml | 11419 | 212 | 4d8d9d4520260c59eaa333aea673dd81a57144015fbc6e0997f597374a42e4e2 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-23-46-169Z.yml | 11419 | 212 | 4d8d9d4520260c59eaa333aea673dd81a57144015fbc6e0997f597374a42e4e2 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-35-51-735Z.yml | 10762 | 212 | 409c650d4d9287fc8d493fa5f20fd28f50b486a5d8b7da459c35283faa1f2d9f |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-50-17-343Z.yml | 11585 | 215 | 157cc07fe33ac009b7703d2fea8f7abde65c7565a648997527006d47980bb14b |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-51-29-238Z.yml | 11082 | 215 | a38b1ec075b348e5ad170269e9df3870b37b84993d740c5c9d464b164e81e827 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-51-43-633Z.yml | 11082 | 215 | a38b1ec075b348e5ad170269e9df3870b37b84993d740c5c9d464b164e81e827 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-53-09-210Z.yml | 12250 | 231 | 3bb2f0685e4f3b9ae1f22b918d7bbe64e427b87f088f6958a8028fdabccd4e5f |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-53-44-757Z.yml | 11920 | 224 | 9c1467c98d715b77ef7bca2df3eff976afb91a32bce337719a9d9c6bc186bcfe |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-55-00-671Z.yml | 11161 | 216 | 95c1435ad2cb5cba2a03c107d9403b2d24a6716dc05d03c87af55ed8a5bf9532 |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-55-26-600Z.yml | 12427 | 236 | 297734b6739f68b07d653a60f47cd0fbcbcc997b4b740cadb379da806ee2b0cb |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-56-14-692Z.yml | 12427 | 236 | 297734b6739f68b07d653a60f47cd0fbcbcc997b4b740cadb379da806ee2b0cb |
| FH-EVIDENCE | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/EVIDENCE/playwright/page-2026-10-01T18-57-46-657Z.yml | 4889 | 1 | 928fc2e5f3ea8550bc3a201836dd6b3c424b33b21fb02409f4f32307fe025cf2 |
| FH-TRIAL | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FAILED_FH_BRAINBOX.md | 17933 | 221 | 0ef078a4ca462aa57c72278b6622c99f4d939e152e6c05f531fbf5ad051ccee5 |
| FH-TRIAL | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FH_MUST_README.md | 11360 | 89 | 71078625c20dae419893d94f894867976aea7941a12589a2f8309de46f1d03b6 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE BOOTS IMAGES/americana-star-western-boot.png | 1792411 | N/A | 89dbc63dfc375459e8e36bf8334787e6d302fd3d4547b0b38985a3526b2b3268 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE BOOTS IMAGES/blue-blossom-western-boot.png | 1734723 | N/A | cbe6077b100562090454fb9d6668d948f06c74224382f5d1927789a36d6094cb |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE BOOTS IMAGES/crimson-triple-buckle-boot.png | 1884644 | N/A | d147a4a3718b3e4d8442b090c0f9d54843bbe1c20c2e06c4369200b064a353d8 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE BOOTS IMAGES/foothive-boot-images.md | 1231 | 30 | 5baf8f3b175791f26b884ffa8773b6be81743220e544b7a399680adb451869da |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE BOOTS IMAGES/ivory-shaft-western-boot.png | 670818 | N/A | 314908ded14cbd76a33c66b6af6ebf177613046ae87dfa49a331883253682028 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE BOOTS IMAGES/olive-canvas-buckle-combat-boot-front.png | 398700 | N/A | 7b8485cc1b68d1051aa6999f767fcb6d732af73bc0c5d404cbce754bbb817efd |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE BOOTS IMAGES/olive-canvas-buckle-combat-boot-rear.png | 536214 | N/A | 3ddc6ab8bc04d0e844e224780084b11ce032fac4ffc28b46e42e6ee8e0821fa7 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE BOOTS IMAGES/stars-stripes-western-boot.png | 479778 | N/A | 817b7cc4fdf9eeea51708b60a166bb44332eaff81c289bcd5e14b224fc21dcec |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE BOOTS IMAGES/sunflower-embroidered-western-boot.png | 1189578 | N/A | 4fbc9b28f6a52b2dad36c5a849a73e60f57a22407eb5beca38ba570ed61b9d44 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE BOOTS IMAGES/winged-cross-studded-western-boot.png | 1493098 | N/A | a92b7f68e1994e7e6490dfba376cfbf8fadb8b31494736fa428d9990bb16f431 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE CLASSIC SHOES IMAGES/burnished-cognac-patina-oxford.png | 724932 | N/A | 3fc305a7521cdefbc731f4af9c1eb09d1837fdeb5a6809765bf280dfeec6ce91 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE CLASSIC SHOES IMAGES/chestnut-ivory-suede-panel-wingtip.png | 4372094 | N/A | 2324f77f23a8100a739c80f635ace9906df0ae8fed5d3e64b78a2c7d997496fd |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE CLASSIC SHOES IMAGES/chestnut-two-tone-wingtip-boot.png | 1817639 | N/A | 5f57d20754a738b58112528b70c42e0d422201964d69659a72342fe8b16a2c5c |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE CLASSIC SHOES IMAGES/crimson-navy-patina-wingtip.png | 313835 | N/A | b7a5610823ea8a18987e1ed00f651ac52733b8f5d632a0411e8004bbe6bbd568 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE CLASSIC SHOES IMAGES/foothive-classic-images.md | 1218 | 30 | 58386c5d00a65dd7801cb0bdd0afa2405d4e92334e2485282af724383444fe15 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE CLASSIC SHOES IMAGES/four-pair-shoe-tree-lineup.png | 688810 | N/A | c734b8e75ee1e9fd68aae39da5d04a288b5d35ab67283e73bf27deee84bb27f8 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE CLASSIC SHOES IMAGES/olive-suede-wingtip-brogue.png | 664091 | N/A | 415157052b0f7a35f741fd7a48816e927c6cc75f8afbbb503d838b68b67f923f |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE CLASSIC SHOES IMAGES/tan-croc-embossed-derby.png | 430372 | N/A | 82f016cb21dc6300b6bc74ed4698fcef3fcaaed680b1ce4fc3ff3692ccf5f3b2 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE CLASSIC SHOES IMAGES/tri-tone-patent-wingtip-derby.png | 805708 | N/A | c2a9335a7b77947cd12b784fa161a0bb4162683b19a067f77f24f8dce0bd00b5 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE CLASSIC SHOES IMAGES/two-tone-cap-toe-field-boot.png | 591572 | N/A | 8ba73dd0eab551ffaece1a46c616d0c3c276a125b3f3fd6c1de70d0ea0f111eb |
| FH-TRIAL | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE LOGO + DARK MODE/foothive-logo-dark.svg | 9172 | 27 | 36df8baea37d04cf53b30ffaa51e2e239fb151471fcfc5a774a0084ae093966f |
| FH-TRIAL | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE LOGO + DARK MODE/foothive-logo.svg | 9105 | 27 | c28b7471e06429b81753151d7a8a610be4ed1286566c013c058d9c802edfd8c7 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE SNEAKER IMAGES/charcoal-tactical-boot-runner.png | 646172 | N/A | 1588b3dd3e79a9c5e9bf878b7b31ee3360c51f5a3a2609b7274c650246c5440d |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE SNEAKER IMAGES/foothive-sneaker-images.md | 573 | 15 | 1e645b5962f960fddda5a0919ad9a9ceae1f10dab59ba9fefadacf036c94917f |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE SNEAKER IMAGES/frost-glow-sock.png | 443169 | N/A | 2289b77dea3d12977cc3858d91397c537d9ccf72db7ce70d641836aeb5a4357e |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE SNEAKER IMAGES/navy-tan-stripe.png | 341243 | N/A | bd16210c8f806ee44b92aad50396bd86ce4b418339517514f983b8f51995f710 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE SNEAKER IMAGES/talon-blade.png | 687827 | N/A | 4a889fc268bf0681fd8ea06521776946e5b877d048ef5c095184e5762305d24c |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE TIMBERLAND IMAGES/foothive-timberland-images.md | 871 | 33 | 41833999931e3d0ec762f2b9a08e6d1e9fe814a53765e584da1a96b0ef144b79 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE TIMBERLAND IMAGES/image02.png | 1109106 | N/A | c0f4d1f4e81f30dc8b39482141603b09009bd7fb7e2bb3c8a8101da24e57bd10 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE TIMBERLAND IMAGES/image03.png | 991052 | N/A | 11390e47e9327c69577a8abfc9d8251457057c54e58efb1f471b26d69e3fe79b |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE TIMBERLAND IMAGES/image04.png | 718804 | N/A | 8abe32149c35e2b790c458cbcc88fb0899158460f43fc2899b119cb049d43c6a |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE TIMBERLAND IMAGES/image05.png | 1385905 | N/A | 0afcbe97cb83c52d2d8e9d7b1856c3583f1d4688236d1471cf08cba0603842e3 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE TIMBERLAND IMAGES/image08.png | 1020555 | N/A | 4b3f3285cbfcdcc192542248fad8d17a79d2836d74195269f042f16dbd47bbf7 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE TIMBERLAND IMAGES/image13.png | 796479 | N/A | 07dd6563a4127a2e2958a281b56c3af1b7950aa64b697cf03fcb1f93637926e4 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE TIMBERLAND IMAGES/image15.png | 980549 | N/A | 38e4c0e763d9046428bb2fe9bd9e364035bda5188a44f417eac7fa445eaea36b |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE TIMBERLAND IMAGES/image16.png | 650096 | N/A | 1052679193b3a06aac70f40ee61fb2fc7f4cc902fd980e2113a50dd090363808 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE TIMBERLAND IMAGES/image17.png | 2556387 | N/A | 7cd01613bedd8e445b9efa19439abdbc764cf9bf2f558c28aeacd58968332613 |
| FH-ASSET | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/FOOTHIVE TIMBERLAND IMAGES/image19.png | 1661839 | N/A | b4cbfc042422de85c1794fe817fc3459a3b600bf36620a1c8004e89b98d7a68d |
| FH-TRIAL | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/OPERATOR_ADDENDUM_FH_BRAINBOX.md | 3247 | 36 | 6ea8740bb3a4f4c88dfc68bee7914040002aa1d2ecd66df12525f1cf4b11c797 |
| FH-TRIAL | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FOOTHIVE_PROJ_BRAINBOX/PASSED_FH_BRAINBOX.md | 15597 | 134 | f21dcff41416c08810fe0b9baa159acaa322fa8648d7cfdb4ceca8bd3c627f2a |
| PROJECT-LEGACY | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/PROJ_MUST_README.md | 1319 | 28 | f85c3a95c15b8546a58677a2976fda19389f71c3c7b58852fb3376cfff51cc65 |
| PROJECT-LEGACY | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/PROVEN_PATTERN_PROJ_BRAINBOX.md | 0 | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| FULLSTACK-RAW | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/RAW_WORKFLOW_PROJ_BRAINBOX/FULLSTACK_RAW_BRAINBOX/001DOC_BYB5DOC_FLOW_STACK_BRAINBOX.md | 25450 | 565 | e9ad5963cf5e59555a0bf5b3c797eade93f2995007117c3684aeb158a6da9105 |
| FULLSTACK-RAW | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/RAW_WORKFLOW_PROJ_BRAINBOX/FULLSTACK_RAW_BRAINBOX/002DOC_BYB5DOC_PRESET_FLOW_STACK_BRAINBOX.md | 26261 | 615 | 0a7270ecc83db51416aaab7d6d5a78231f783dcdf5d01e4a9a7e0499fdbf45ea |
| FULLSTACK-RAW | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/RAW_WORKFLOW_PROJ_BRAINBOX/FULLSTACK_RAW_BRAINBOX/FSTACK_MUST_README.md | 8174 | 87 | a4ff12448bf458d5252bc36ace55acccd8841cbaaca4d32e052b59840c976cd0 |
| PROJECT-RAW-AUTH | AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/RAW_WORKFLOW_PROJ_BRAINBOX/RAW_PROJ_MUST_README.md | 4441 | 57 | be80758c5188f319c7f5b1a3ca4f862077530982e932f8d596469940c9a33f41 |
| SKILLS-LEGACY | AI_BRAINBOX/SKILLS_AVAIL_AI_BRAINBOX/FAILED_SKILLS_BRAINBOX.md | 0 | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| SKILLS-LEGACY | AI_BRAINBOX/SKILLS_AVAIL_AI_BRAINBOX/PROVEN_SKILLS_BRAINBOX.md | 0 | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| SKILLS-LEGACY | AI_BRAINBOX/SKILLS_AVAIL_AI_BRAINBOX/RAW_SKILLS_BRAINBOX.md | 0 | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| SKILLS-LEGACY | AI_BRAINBOX/SKILLS_AVAIL_AI_BRAINBOX/REUSABLE_SKILLS_BRAINBOX.md | 0 | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| SKILLS-LEGACY | AI_BRAINBOX/SKILLS_AVAIL_AI_BRAINBOX/SKILLS_MUST_README.md | 847 | 24 | 1850965879a9494dd3004e605125c2d3e2bde42e678fe8d11d5e8fc9872dbef6 |
| ROOT-AUTH | DOB_MUST_README.md | 9788 | 204 | 76e2b6aa72e4dcf3b56475f182dca2c117ae7a32a9e116c3b3c8bf6262811252 |
| MILESTONES-LEGACY | MILESTONES/MILESTONES_MUST_README.md | 2230 | 56 | f5197f1e1f2c28ea0f6cdfaac53024c3d26d29fb50ce1b724d64c63082b2ef3e |
| MILESTONES-LEGACY | MILESTONES/MILESTONE_CHECKPOINT_BRAINBOX.md | 26420 | 462 | 91ac1a35dea9b13cee37a9ae4fd11e61c8f112bbc6c4395325857b0c08fffdc8 |
| PORTFOLIO-LEGACY | PORTFOLIO_BRAINBOX/001_PORT_BRAINBOX.md | 0 | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| PHASE01-ARCHIVE | V003_VERSION_UPGRADE_BRAINBOX/PHASE01_POLISH_BRAINBOX/README_PHASE01_POLISH_BRAINBOX.md | 4479 | 65 | 0a742f70ab8abafd4a17f8d99594fdca35ce923c3ffeba295c73d18bf086ba8c |
| PHASE01-ARCHIVE | V003_VERSION_UPGRADE_BRAINBOX/PHASE01_POLISH_BRAINBOX/V003_POLISH_CONVO_VERSION_UPGRADE_BRAINBOX.md | 86743 | 1655 | 53e7e35792337dc2e0d2554ccc45705b1cf63352cee17ece2029cd3a6ae7ebf9 |
| PHASE01-ARCHIVE | V003_VERSION_UPGRADE_BRAINBOX/PHASE01_POLISH_BRAINBOX/V003_POLISH_REPORT_VERSION_UPGRADE_BRAINBOX.md | 195568 | 3820 | ff33de92f7cdbb46513b699abac3233b68e372a3498c0abdb69ab783b5269875 |
| PHASE02-PROCESS | V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/README_PHASE02_MIGRATION_BRAINBOX.md | 5849 | 79 | 824c067d4d56cba9dea3ceba46d76552d60c7fa703e8364d0f060898ce2ea8e3 |
| PHASE02-PROCESS | V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_MIGRATION_CONVO_VERSION_UPGRADE_BRAINBOX.md | 10557 | 199 | af4e93fc6ce3a4fe508db067ff9902e7b60ca0a4ba4127b763789d5aa6da37a4 |
| PHASE02-PROCESS | V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_MIGRATION_REPORT_VERSION_UPGRADE_BRAINBOX.md | 27756 | 646 | 9dfe5f29217423b4386505a2c3693d242818e7d7bd12cd0d3b6cf644ef2dbbc0 |
| PHASE02-PROCESS | V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_PHASE02_MIGRATION_TICKETS_BRAINBOX.md | 64517 | 1402 | 8dfcbe2a9323ce1997a43071d92b552f0a641d4bdfef11a614d2857fd03012a2 |
| V003-AUTHORITY | V003_VERSION_UPGRADE_BRAINBOX/README_V003_VERSION_UPGRADE_BRAINBOX.md | 6650 | 140 | 563371dd33ddbdd440b4edd2007856308444b68adf4dbff1ec61f06864e27819 |
| V003-AUTHORITY | V003_VERSION_UPGRADE_BRAINBOX/V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md | 217796 | 6569 | 11ea43a34c2026b15cf6b62d3eac6cf1be964d67fea19162bc90a121c4872b3d |
| V003-AUTHORITY | V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md | 82272 | 1760 | 08f8ebe71d26bbf17aa0b23b51b0dbd7c521f24c7abda574a03d886222e0065c |
| VERSION-HISTORY | VERSION_HISTORY_BRAINBOX/V003_EXTENDED_DEODINI_BRAINBOX/ARCHITECTURE_DECISIONS_V003_BRAINBOX.md | 2887 | 36 | 716b9a4eb660d7b692d4490613ca371030ef45d0e942812c55f96dcdd7bffe38 |


## 10. V003-M01 execution event — 2026-10-08

**Ticket status:** AUTHORIZED FOR EXECUTION; Phase 01 dependency verified CLOSED / FROZEN.  
**Branch:** v003/m01-current-state-inventory-migration-map.  
**Pre-change HEAD:** 27e73f828bb367298442c2e621c18d1cc1ceb4f4; local main, origin/main, live GitHub main, and M01 branch matched.  
**Pre-change tree:** clean; 122 tracked files; no untracked or ignored working-tree material; empty physical BRAINBOX/ directory separately noted.  
**Inventory:** all 122 tracked files have file-specific family/path/byte/line/SHA-256 entries in the baseline manifest. The inventory covers root/AI authority, FUNC, project/raw workflow, FootHive trial/evidence/assets, Skills, Portfolio, Milestones, Version History, V003 authorities and Phase 01/02 support records.  
**Integrity/recovery:** live GitHub main matched the local baseline. git fsck --full --no-reflogs reported 72 dangling objects without missing/corrupt/fatal output; 20 are Cline checkpoint commits and 52 are non-commit objects. No bundle was created, and no garbage collection, reflog expiration, or pruning was run. M01-GIT-01 remains open because those local-only dangling objects are outside the remote branch recovery point.  
**Operator clarification:** preserve the nested Version History path. M04 owns creation/reconciliation of README_VERSION_HISTORY_BRAINBOX.md if it is still absent; M01 did not create it. Placeholder-specific approval is not established and must not be attributed to the Operator without an explicit future instruction.  
**Additional flag:** M01-FH-01 records 32 broken catalog image references across four FootHive catalogs for disposition in M15; no links or assets were changed. The 11 existing image exclusions remain in place.  
**Product-tree action:** created this migration ledger only. No source was edited, renamed, moved, or deleted.  
**Support-record action:** updated the Phase 02 README, conversation, and report to reflect local M01 completion and independent verification findings. M01-DOC-01 is resolved by correcting/retracting the unsupported Operator-attribution wording. Git lifecycle is `PENDING — BATCH A BOUNDARY` and does not block M02 after M01 independent verification. The manifest retains the original pre-M01 hashes for those support records.  
**Post-change implementation status:** migration map and supporting status records implemented locally; source migration not started; independent ChatGPT verification PASS after M01-DOC-01 was resolved by documentation correction/retraction; commit/push/merge not performed because Git lifecycle is batch-scoped and remains `PENDING — BATCH A BOUNDARY`; M02 may proceed under its own P14 preflight.  
**Map self-integrity:** reported in the M01 execution report; the ledger does not self-reference its own digest.  



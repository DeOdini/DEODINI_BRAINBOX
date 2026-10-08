# README_PHASE02_MIGRATION_BRAINBOX

**Status:** [ACTIVE — AUTHORIZED] — M01–M04 independently verified PASS; each ticket has its own dedicated branch and commit; all four branch refs are pushed to `origin` at the recorded heads; M03 README verification status is reconciled in `f0113e7`; M04 is committed as `4747286`; Batch A non-blocking flags are dispositioned to M15, M19/M20, and M21; PR/merge and final remote verification remain pending before Batch B/M05.
**PARENT:** `V003_VERSION_UPGRADE_BRAINBOX/`
**CURRENT DOMAIN:** V003 Phase 02 migration planning, ticket issuance, execution conversation, and migration verification reporting
**PURPOSE:** Keep Phase 02 migration planning and later execution evidence separate from the closed Phase 01 polish archive.
**MENTAL MODEL:** Phase 01 froze the target; Phase 02 compares the live Brainbox against that target and migrates through individually scoped V003-Mxx tickets covered by the Operator's explicit M01–M21 set authorization, with each ticket subject to dependencies and P14 preflight.
**GOVERNED BY:** The frozen V003 Specification, Origin Conversation, P14 migration preflight, the V003 parent README, and the Operator's explicit approval of V003-M01–M21 recorded in the Phase 02 report/conversation.
**LAST VERIFIED:** 2026-10-08

## Authority boundary

The canonical V003 authorities remain:

- `../V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md` — frozen migration-target authority.
- `../V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md` — historical decision evidence and ambiguity resolver.
- `../PHASE01_POLISH_BRAINBOX/` — closed Phase 01 execution and verification archive.

This Phase 02 folder contains migration planning and migration execution/audit records. It does not independently redefine the V003 target.

The issued migration tickets are individually scoped records. The Operator explicitly approved execution of the remodeled V003-M01–M21 set on 2026-10-08; that approval supersedes any earlier wording in this README that required separate authorization for each ticket. No repeated per-ticket approval is required for the approved set. Execute tickets one at a time in dependency order, with ticket-specific P14 preflight. **Stop/report/wait applies to BLOCKING flags; BATCH-DEFERRED / NON-BLOCKING flags are recorded in detail, accumulated for the active batch, and do not stop same-batch progression unless the next ticket materially depends on their correction.** This set approval does not authorize scope expansion, merging, or deployment.

## Local tree

```text
PHASE02_MIGRATION_BRAINBOX/
├── README_PHASE02_MIGRATION_BRAINBOX.md
├── V003_MIGRATION_CONVO_VERSION_UPGRADE_BRAINBOX.md
├── V003_MIGRATION_REPORT_VERSION_UPGRADE_BRAINBOX.md
└── V003_PHASE02_MIGRATION_TICKETS_BRAINBOX.md
```

## Record roles

- `README_PHASE02_MIGRATION_BRAINBOX.md` — local Phase 02 authority boundary, navigation, status, and record roles.
- `V003_MIGRATION_CONVO_VERSION_UPGRADE_BRAINBOX.md` — Operator/ChatGPT/Codex migration-planning and migration-execution conversation record from Phase 02 onward.
- `V003_MIGRATION_REPORT_VERSION_UPGRADE_BRAINBOX.md` — Phase 02 cross-checks, execution reports, independent verifications, flags, and closeout evidence.
- `V003_PHASE02_MIGRATION_TICKETS_BRAINBOX.md` — Operator-approved/authorized V003-M01 through V003-M21 migration tickets.

## Phase 02 operating rules

1. Phase 01 is closed/frozen.
2. Phase 02 ticket drafting is complete and the remodeled V003-M01–M21 set is explicitly Operator-approved for execution as of 2026-10-08.
3. This authorization comes from the Operator's explicit approval, not from ticket existence or batch membership.
4. Execute one migration ticket at a time within its batch. A ticket must pass its own P14 preflight and Codex execution/reporting, and its **substantive migration result must pass ChatGPT independent verification with no BLOCKING flag** before a dependent ticket proceeds. Non-blocking flags may remain open for batch correction. **Staging, commit, push, PR, merge, and Git closure are batch-boundary actions, not per-ticket intra-batch gates.**
5. Every ticket must carry the two canonical authority paths and perform the P14 preflight.
6. Any ambiguity, contradiction, unsupported rename, historical-evidence risk, scope mismatch, secret risk, destructive-operation risk, missing dependency, or other issue must be classified by impact. If it materially affects the active ticket or next dependent ticket, it is **BLOCKING** and stops affected work. If it does not, it is **BATCH-DEFERRED / NON-BLOCKING**, must be documented precisely, and is accumulated for correction before batch Git closure.
7. Current live content must be inspected before mapping; filename alone is not sufficient evidence of destination.
8. Source removal requires explicit authorization, verified destination/history, and integrity/recovery evidence where applicable.
9. Migration must preserve historical evidence, canonical/reference boundaries, and historical ticket identity.
10. **Operating model:** Operator approves/resolves flags and retains merge authority; Codex executes authorized migration tickets; ChatGPT independently verifies Codex completion claims.
11. Codex must produce the per-ticket execution report contract defined in `V003_PHASE02_MIGRATION_TICKETS_BRAINBOX.md`, including pre-state, exact paths/actions, post-state, verification, unresolved flags, scope-discipline result, Git lifecycle, and verification limits.
12. Codex execution evidence and ChatGPT independent verification are recorded separately for every ticket. A ticket whose substantive migration result passes independent verification and has no **BLOCKING** flag is eligible to satisfy same-batch dependencies. Non-blocking flags remain open in the batch flag register without stopping progression. Git closure occurs at the batch boundary, not after every ticket.
9. Every V003-Mxx ticket has a dedicated branch and ticket-specific local commit. The batch controls execution/verification cadence and remote push/PR/merge timing; it does not combine ticket branch identity.

## Migration ticket state

**Issued/remodeled set:** V003-M01 through V003-M21.

**Operator approval:** APPROVED — 2026-10-08.

**Execution authorization:** AUTHORIZED — V003-M01 through V003-M21, executed one ticket at a time under dependencies, P14 preflight, Codex reporting, ChatGPT independent verification, and Operator merge/closure authority.

**Current Batch A progression:** M01–M04 are independently verified PASS and merged to `main` in order through PRs #16–#19. V001/V002 snapshots match Git exactly (10/10 and 111/111), and all four ticket branch heads are ancestors of `origin/main` (`e0e05e2afec7795b916595c8c6ca3f09a8b227d0`) in the final fetch check. M01-GIT-01 and M04-HIST-01 remain explicit evidence/recovery deferrals assigned to M21; M01-FH-01 is assigned to M15; M02-BR-01 to M19; M03-REF-01 to M19/M20; M01-DOC-01, M02-WS-01, and M04-BR-01 are resolved. Batch A Git closure is complete; M05 has not started.

**M01 inventory and migration map:** PASS; dedicated commit `bc6d1309a71f4a309469788074c381c8665e5490` is pushed and matches its origin branch. M01-GIT-01 is preserved for M21 integrity/recovery review; M01-FH-01 is assigned to M15.

**M02 root-authority migration:** PASS; dedicated commit `3971f48c4c75641e46a23a86b0792e44e2d794e3` is pushed and matches its origin branch. `M02-BR-01` preserves both README byte/hash records; the 340-line hierarchy, link, and whitespace checks pass. Recheck under M19.

**M03 Governance canonicalization:** INDEPENDENT CHATGPT VERIFICATION PASS; implementation commit `2bd21bb0a7e09ba014809df27868c9b4e7546cb7` plus status-reconciliation commit `f0113e74bc2cc50a9e91fc340b5406b19494f026` are pushed on its dedicated branch and merged through PR #18 (`19c707cd6d2d443ff56081d0e73c7d6c5f705918`). All nine approved Governance records are present; the stale README verification label reflects the recorded pass. `M03-REF-01` remains assigned to M19/M20.

**M04 Version History migration:** PASS; implementation commit `4747286c1b3c134001c6f6d08cb7dcba32685461` and cross-check/report commit `f05a87a188bbcdca7038a2f8518d00175371153d` were pushed on its dedicated branch and merged through PR #19 (`e0e05e2afec7795b916595c8c6ca3f09a8b227d0`). V001/V002 path inventories match Git exactly (10/10 and 111/111); conceptual retrospective gaps remain explicitly deferred to M21.


**Batch A Git lifecycle:** COMPLETE. PRs #16, #17, #18, and #19 merged M01–M04 to `main` in dependency order. GitHub reports each PR merged, the post-merge fetch updated `origin/main` to `e0e05e2afec7795b916595c8c6ca3f09a8b227d0`, and `git merge-base --is-ancestor` passed for all four ticket branches. The four ticket branches remain available; none was deleted. Batch A flags have explicit later-ticket dispositions. M05 has not started.

**Legacy source migration:** M03 Governance records are organized in the canonical domain; legacy governance sources remain unchanged and are retained for M19/M20 reference reconciliation and source-retirement gates.

## Placement correction record

The Phase 02 ticket file and initial Phase 02 cross-check were first written under `PHASE01_POLISH_BRAINBOX/` during ticket drafting.

The Operator corrected that archive boundary on 2026-10-08.

The Phase 02 material was moved into this dedicated parent folder, and the Phase 01 README/report were restored to Phase 01-only scope.

The Operator referred to the new parent as `PHASE02_MIGRATION_BRAINBOX.md`. Because the requested parent must contain child files and governed folders use the `_BRAINBOX/` folder convention, it is implemented as the directory:

`PHASE02_MIGRATION_BRAINBOX/`

No migration execution was performed as part of this placement correction.
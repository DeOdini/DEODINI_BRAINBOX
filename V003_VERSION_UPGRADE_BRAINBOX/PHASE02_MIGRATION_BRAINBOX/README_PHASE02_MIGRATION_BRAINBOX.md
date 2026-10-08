# README_PHASE02_MIGRATION_BRAINBOX

**Status:** [ACTIVE — AUTHORIZED] — Phase 02 set approved by the Operator on 2026-10-08; M01 and M02 independently verified PASS; M02-WS-01 resolved; M03 is dependency-eligible under its own P14 preflight; Batch A Git lifecycle pending.
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

## Migration ticket state

**Issued/remodeled set:** V003-M01 through V003-M21.

**Operator approval:** APPROVED — 2026-10-08.

**Execution authorization:** AUTHORIZED — V003-M01 through V003-M21, executed one ticket at a time under dependencies, P14 preflight, Codex reporting, ChatGPT independent verification, and Operator merge/closure authority.

**Current Batch A progression:** M01 and M02 are independently verified PASS. M01-GIT-01 and M01-FH-01 remain documented carry-forward items. M02-WS-01 is resolved and non-blocking. M03 is next dependency-eligible subject to its own P14 preflight.

**M01 inventory and migration map:** PASS; local ticket commit `bc6d1309a71f4a309469788074c381c8665e5490` created on its dedicated branch. M01-GIT-01 and M01-FH-01 remain carry-forward items; push/PR/merge remain pending at Batch A closure.

**M02 root-authority migration:** PASS; root README created and V003 navigation reconciled; `DOB_MUST_README.md` remains unchanged; no source moved, renamed, or deleted. M02 local ticket commit is being prepared on its dedicated branch; push/PR/merge remain at the Batch A boundary.


**Batch A Git lifecycle:** M01 local commit exists; M02 and M03 local ticket commits remain pending; push/PR/merge remain deferred to the Batch A boundary.

**Legacy source migration:** No legacy source was moved, renamed, or deleted by M01 or M02. Governance canonicalization remains pending M03.

## Placement correction record

The Phase 02 ticket file and initial Phase 02 cross-check were first written under `PHASE01_POLISH_BRAINBOX/` during ticket drafting.

The Operator corrected that archive boundary on 2026-10-08.

The Phase 02 material was moved into this dedicated parent folder, and the Phase 01 README/report were restored to Phase 01-only scope.

The Operator referred to the new parent as `PHASE02_MIGRATION_BRAINBOX.md`. Because the requested parent must contain child files and governed folders use the `_BRAINBOX/` folder convention, it is implemented as the directory:

`PHASE02_MIGRATION_BRAINBOX/`

No migration execution was performed as part of this placement correction.

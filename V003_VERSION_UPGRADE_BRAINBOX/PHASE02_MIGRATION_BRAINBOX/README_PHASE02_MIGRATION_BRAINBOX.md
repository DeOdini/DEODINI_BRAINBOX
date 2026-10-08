# README_PHASE02_MIGRATION_BRAINBOX

**Status:** [ACTIVE — AUTHORIZED] — Phase 02 migration ticket set re-cross-checked/remodeled and explicitly approved by the Operator on 2026-10-08; migration execution not started
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

The issued migration tickets are individually scoped records. The Operator explicitly approved execution of the remodeled V003-M01–M21 set on 2026-10-08; that approval supersedes any earlier wording in this README that required separate authorization for each ticket. No repeated per-ticket approval is required for the approved set. Execute tickets one at a time in dependency order, with ticket-specific P14 preflight and stop/report/wait on any flag. This set approval does not authorize scope expansion, merging, or deployment.

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
4. Execute one migration ticket at a time, even when tickets are grouped in a planning batch.
5. Every ticket must carry the two canonical authority paths and perform the P14 preflight.
6. Any ambiguity, contradiction, unsupported rename, historical-evidence risk, scope mismatch, secret risk, destructive-operation risk, or missing dependency stops the affected ticket before implementation.
7. Current live content must be inspected before mapping; filename alone is not sufficient evidence of destination.
8. Source removal requires explicit authorization, verified destination/history, and integrity/recovery evidence where applicable.
9. Migration must preserve historical evidence, canonical/reference boundaries, and historical ticket identity.
10. **Operating model:** Operator approves/resolves flags and retains merge authority; Codex executes authorized migration tickets; ChatGPT independently verifies Codex completion claims.
11. Codex must produce the per-ticket execution report contract defined in `V003_PHASE02_MIGRATION_TICKETS_BRAINBOX.md`, including pre-state, exact paths/actions, post-state, verification, unresolved flags, scope-discipline result, Git lifecycle, and verification limits.
12. Codex execution evidence and ChatGPT independent verification are recorded separately in the Phase 02 migration records before closure.

## Migration ticket state

**Issued/remodeled set:** V003-M01 through V003-M21.

**Operator approval:** APPROVED — 2026-10-08.

**Execution authorization:** AUTHORIZED — V003-M01 through V003-M21, executed one ticket at a time under dependencies, P14 preflight, Codex reporting, ChatGPT independent verification, and Operator merge/closure authority.

**First dependency-eligible execution ticket:** V003-M01 — Current-State Inventory, Integrity/Recovery Baseline & Migration Map Bootstrap.

**Filesystem migration:** NOT STARTED.

## Placement correction record

The Phase 02 ticket file and initial Phase 02 cross-check were first written under `PHASE01_POLISH_BRAINBOX/` during ticket drafting.

The Operator corrected that archive boundary on 2026-10-08.

The Phase 02 material was moved into this dedicated parent folder, and the Phase 01 README/report were restored to Phase 01-only scope.

The Operator referred to the new parent as `PHASE02_MIGRATION_BRAINBOX.md`. Because the requested parent must contain child files and governed folders use the `_BRAINBOX/` folder convention, it is implemented as the directory:

`PHASE02_MIGRATION_BRAINBOX/`

No migration execution was performed as part of this placement correction.

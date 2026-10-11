# ChatGPT Independent Governance Review and V003 Phase 03 Fix Plan — 2026-10-11

**STATUS:** [PROPOSED — FOR OPERATOR AUTHORIZATION; NOT EXECUTED]
**PROVENANCE:** Operator six concerns and uploaded Grok/Claude review; ChatGPT live desktop read-only audit (460 physical files, 289 directories), shared Capability Integration Report and Verify Codex Claims, frozen V003 Specification and Origin, active Governance Ticketing/Evidence/Documentation/Versioning/Promotion, Phase 02 tickets and migration map. Semantic review of every archived record has NOT been demonstrated; separate localhost device offline.
**PHASE 02 HISTORY:** Prior entries at Phase 02 report lines 8301 and 8368 and conversation lines 4176 and 4209 remain preserved as dated history. This Phase 03 report becomes the planning entrypoint; it does not rewrite earlier reports.
**BASELINE:** M21-GIT-01 BLOCKING; 20 M01 checkpoint SHAs not found by prior local checks (0/20); independent external backup status undetermined. M21 NOT ACCEPTED, Phase 02 OPEN, Batch E unmerged. Existing M21 commits were previously two ahead of GitHub, with earlier Phase 02 documentation still modified locally; recheck before any lifecycle work.

## Canonical rules and proposed Phase 03 adaptation
1. A discovered flag or draft ticket is not approval. Operator explicitly authorizes each exact scope and every material scope expansion.
2. Compare actual sources/references/Git evidence with frozen V003 target, Origin historical decisions, active Governance, current tree and migration ledger. Naming alone cannot establish a destination.
3. Distinguish blocking acceptance gates, affected-source move/retirement stops, non-blocking corrections and Operator design choices. Phase 02's non-blocking batch exception is restricted to Phase 02; adopting it for Phase 03 needs new Operator approval.
4. Preserve chronology, failures, attribution, hashes, original bytes, and legacy source provenance. No unapproved deletion, forced push, GC, prune, reflog expiry or history rewrite.
5. Proposed role separation: Operator authorizes/accepts/merges; Codex executes individual scoped changes and records pre/post/tests; ChatGPT independently verifies. Must be explicitly adopted for Phase 03.
6. Execution, readback, independent verification, staging, commit, push, PR, merge, deployment and acceptance remain separately evidenced states.
7. Every future `V003-Fxx` ticket needs exact paths, original M-series reference where relevant, risk/class, dependency, mandatory preflight, exclusions, permitted operations, safety/recovery, test pass criteria, report contract and Operator closure gate.

## Stable full version-specific flag register
| Proposed ID | Exact concern / original flag | Provisional category | Complexity |
|---|---|---|---|
| V003-F01 | M21-GIT-01/M01-GIT-01: 20 original M01 checkpoint commits not readable; backup recovery/disposition | GLOBAL BLOCKER | HIGH |
| V003-F02 | Existing local M21 publication, final independent check and Batch E / V003 acceptance | FINAL CLOSURE GATE | LOW mechanical, HIGH dependencies |
| V003-F03 | M15-ASSET-01: 29 FootHive source-only product/catalog assets without approved target | SOURCE RETIREMENT STOP | MEDIUM |
| V003-F04 | M17-DEST-01: two legacy MILESTONES/ documents lack approved destination | SOURCE MOVE/RETIREMENT STOP | LOW–MEDIUM |
| V003-F05 | M19-HIST-01: historical byte/line-ending mismatches versus manifest | HISTORICAL EVIDENCE GATE | MEDIUM |
| V003-F06 | M20-REF-01: substantive legacy-source retention/references and retirement criteria | SOURCE RETIREMENT STOP | HIGH |
| V003-F07 | Five T23 Windows paths 260–263 characters; core.longpaths unset | PORTABILITY FIX | LOW–MEDIUM |
| V003-F08 | DOB/AI_MUST/FQ legacy entry/reading rules versus active root/Governance | ROUTING FIX | LOW |
| V003-F09 | V002 FUNC details vs V003 CORE/EXE and capability intake questionnaire | DESIGN/EVIDENCE RECONCILIATION | HIGH |
| V003-F10 | Legacy SKILLS_AVAIL one-file domain versus V003 SKILLS | OPERATOR DISPOSITION | LOW–MEDIUM |
| V003-F11 | Legacy PROJ_WORKFLOW FootHive + four substantive RAW workflow documents | OPERATOR DISPOSITION | MEDIUM |
| V003-F12 | FootHive PROJ/Sandbox/Production/Portfolio canonical-document authority | OPERATOR DESIGN DECISION | MEDIUM |
| V003-F13 | Production DEVOPS case-study placement and evidence-promotion criteria | DESIGN, DEPENDS ON F12 | MEDIUM |
| V003-F14 | Four unresolved regular local links; 38 including Markdown images in FootHive evidence/catalogs | REFERENCE FIX/QUALIFICATION | LOW–MEDIUM |
| V003-F15 | Historical PENDING statuses, 494 vs 496 dated link counts, M03-REF-01 literal ? | DOCUMENTATION FIX | LOW |
| V003-F16 | Proposed V003-wide Architecture Decisions relocation vs Fullstack ARCH_DECISIONS | OPERATOR ARCHITECTURE DECISION | LOW decision; HIGH relocation risk |

## Priority and recommended execution batching
**Policy:** Real global blocking dependency first even if complex. Next affected-source stop decisions before touching affected sources. Inside a dependency/risk tier, easiest verified bounded disposition or fix precedes medium and high. IDs stay immutable and need not be numerically consecutive in execution.

| Order | Proposed group | Ordered full ticket IDs | Reason |
|---|---|---|---|
| 1 | V003 PHASE03 BATCH-A — global blocking recovery | **V003-F01** | Recover verified SHA objects or present evidence for explicit Operator documented-unavailability decision. No destructive Git repair. |
| 2 | V003 PHASE03 BATCH-B — source-specific stop decisions | **V003-F04 → V003-F03 → V003-F05 → V003-F06** | Two milestone sources first (low-medium), 29 assets next, byte-fidelity investigation next, broad legacy retirement last; source-only stops do not block unrelated tickets. |
| 3 | V003 PHASE03 BATCH-C — easy corrections | **V003-F15 → V003-F08 → V003-F14 → V003-F07** | Small documentation ambiguity and legacy routing before historical image links and Windows path compatibility. |
| 4 | V003 PHASE03 BATCH-D — bounded then medium/hard architecture | **V003-F10 → V003-F16 → V003-F11 → V003-F12 → V003-F13 → V003-F09** | Two bounded Operator decisions first; project-workflow source mapping then FootHive ownership, Production promotion, finally detailed eight-agent CORE/EXE review. F13 must follow F12. |
| 5 | V003 PHASE03 BATCH-E — final publication and acceptance | **V003-F02** | Must occur last because push/PR/merge, independent confirmation and Operator closeout require resolved prerequisites. Existing no-push restriction not silently waived. |

**Critical nuance:** V003-F02 contains mechanically easy documentation publication but cannot be treated as an early completed ticket. Any earlier push of the existing M21 commits requires separate authorization, independent of this final closeout ticket.

## Excluded from automatic fixes
Empty .gitkeep planned scaffolds, future Router and FootHive Iterations 02/03, and historical Phase 01 P06/P09/P13 issues resolved through P16 are NOT new defects without fresh contradictory evidence. Differences in agent-report length and duplicated historical FootHive files require source-level authority/evidence comparison, not automatic deletion or expansion.

## Proposed authorization gates
Operator must approve: (a) Phase 03 governing convention and batch order; (b) each V003-Fxx ticket individually; (c) explicit Phase 03 stop/defer rule; (d) Codex/ChatGPT role assignment; (e) branch, commit/push/PR/merge cadence; (f) whether/how M21 and Phase 02 closure can be accepted after Phase 03 dispositions; (g) any architecture change, deletion, backup restoration or source retirement. ChatGPT must independently verify ticket result before dependent advancement if this model is approved.

**FINAL STATE:** [PROPOSED — WAIT FOR OPERATOR AUTHORIZATION]. No substantive fix, Git publication or V003 acceptance implied.

---

## Operator Phase 03 framework authorization — 2026-10-11

**Decision authority:** DEODINI — Operator. **Inputted by:** ChatGPT. **Status:** [PHASE 03 FRAMEWORK APPROVED; INDIVIDUAL TICKETS NOT AUTHORIZED].

Operator decisions received explicitly:
1. **Framework: APPROVE.** Adopt the proposed five-batch V003 Phase 03 plan and keep the stable full ticket identifiers V003-F01 through V003-F16, with dependency order taking priority over numeric order.
2. **Execution and verification model: SAME.** For Phase 03, explicitly adopt the Phase 02 split: Codex executes each individually authorized ticket and writes an execution report; ChatGPT independently verifies; Operator owns authorizations, disputed-flag decisions, merge and acceptance. The Phase 02 blocking versus batch-deferred/non-blocking distinction also applies in Phase 03: genuinely blocking findings stop affected/dependent work; proven non-blocking flags are precisely logged and reviewed/dispositioned before batch closure. A ticket is not automatically authorized just because its batch is approved.
3. **Git publication: SEPARATE.** Require distinct Operator authorization before Git push/publication, PR creation or merge; the framework approval is not permission for any of them. Do not infer a commit authorization either: ticket-specific Git operations remain subject to explicit scope.
4. **Ticket authorization scope: PLANNING.** Approval covers only Phase 03 framework/planning and documentation. No V003-F01–V003-F16 implementation, object recovery, deletion, reclassification, architecture revision, staging, commit, push or PR/merge is authorized by these decisions.

**Current F-ticket status:** [DRAFT — OPERATOR TICKET AUTHORIZATION PENDING].
**M21:** [NOT ACCEPTED] / M21-GIT-01 still BLOCKING / Phase 02 remains OPEN / Batch E remains UNMERGED.

### Remaining authorization gates before Codex execution
- Operator must expressly authorize the **first individual ticket V003-F01** (or another named ticket) with its exact permitted operations. F01 is proposed read-only checkpoint recovery/disposition investigation; no restoration, object manipulation or destruction without an additional explicit instruction.
- For every approved ticket: establish its branch/worktree location, dependencies, scope/exclusions, preflight, stop/escalation rule, verification evidence, report destination and acceptance criteria. The batch sequence is approved for planning, not blanket execution.
- Codex must perform ticket preflight against actual repo/Git state, source evidence and frozen authority, stop and escalate genuine blockers, and report factual pre/post state. ChatGPT independently verifies before a dependent next ticket advances; Operator separately accepts.
- For V003-F03/F04/F05/F06/F10/F11/F16, obtain exact Operator source-disposition/architecture choices before move, removal, historical rewriting or frozen-spec amendment. Retention and explicit deferral remain valid where evidence permits.
- Document how successful Phase 03 dispositions feed back into the unresolved M21 acceptance and Phase 02 closure without retroactive PASS. M21-GIT-01 requires evidence-backed recovery or explicit Operator documented-unavailability disposition followed by re-verification; neither is given by this framework approval.
- Seek explicit Operator permission before staging/committing or publishing Phase 03 files; before any push, PR or merge ask separately. Existing local documentation modifications and unpushed M21 commits remain unapproved for publication.
- Keep exact V003-Fxx identity in every future report, conversation, branch/ticket reference; do not call any draft F-ticket ACTIVE/AUTHORIZED unless individually approved.

---

## Operator authorization update — 2026-10-11

**Status:** PHASE 03 FIVE-BATCH PLANNING FRAMEWORK APPROVED; V003-F01 THROUGH V003-F16 REMAIN DRAFT TICKETS, NOT APPROVED FOR EXECUTION.

1. Operator approves the five proposed batches and version-scoped V003-Fxx naming, keeping blocking-first and easier-before-medium ordering within dependency groups.
2. Operator adopts the Phase 02 operating model for Phase 03: individual Codex ticket execution, separate ChatGPT independent verification, Operator approval and acceptance, and blocking versus batch-deferred classification. Genuine blockers stop affected/dependent work; accurately reported non-blocking issues may be carried for review and explicit disposition before the batch closes.
3. Git publication requires separate authorization. No permission for push, PR or merge is implied. Ticket-specific staging/commit or other Git changes must likewise have explicit authority.
4. Authorization scope is PLANNING ONLY. Creation of these records is not authorization to execute any F-ticket, restore or manipulate Git objects, move or delete sources, alter the frozen Specification, or accept M21.

**Remaining gates:** Operator approval of exact V003-F01 read-only investigation scope and its branch/worktree rules; preflight and recorded evidence; independent verification; separate approval for any restoration, architectural or historical source change; separate Git lifecycle permissions; final Operator disposition and renewed M21/Phase 02 acceptance. Existing M21-GIT-01 remains blocking, M21 is not accepted and Phase 02 remains open.

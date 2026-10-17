# TICKETING_GOV_BRAINBOX

**STATUS:** [ACTIVE — CANONICAL]
**CANONICAL SOURCE:** Frozen V003 Specification §§25.8, 26–27; Phase 02 execution addendum where scoped.
**APPLIES TO:** Authorized Brainbox changes and governed migration tickets.

## General ticket discipline

1. Identify and report material flags before correcting them. A flag or recommendation is not authorization.
2. Execute only an explicitly authorized ticket and its defined scope. Scope expansion requires updated Operator authorization.
3. Inspect actual content, current state, references, dependencies, and evidence before mapping or changing a source.
4. Keep a ticket's execution report factual: pre-state, exact paths changed, post-state, verification, limits, unresolved flags, and Git lifecycle.
5. Verify the resulting state by reading it back or testing it. A successful write command alone is not verification.
6. Destructive actions require explicit authority and an adequate, verified recovery method.
7. Distinguish implementation, staging, commit, push, PR, merge, deployment, independent verification, and closure. None implies the next.
8. The Operator retains approval and merge authority; a branch or tool connection does not imply permission to merge or deploy.

## Phase 02 flag and batch rule

For V003 Phase 02 only, apply the later Operator declaration recorded in the Phase 02 conversation and the active ticket set:

- **BLOCKING:** materially affects correctness, authority, dependency, safety, canonical destination, historical evidence, secrets, or destructive-risk boundaries; stop the affected work/dependent ticket and report the detailed flag.
- **BATCH-DEFERRED / NON-BLOCKING:** document the exact issue and evidence, assess impact on the next dependent ticket, accumulate it for the active batch, and proceed when no material dependency exists. Review and correct or explicitly disposition accumulated flags before batch Git closure.
- Execute and report one ticket at a time; ChatGPT independently verifies before a dependent same-batch ticket proceeds.
- Stage, commit, push, PR, merge, and Git closure at the batch boundary, not after each ticket.

This Phase 02 operating addendum supersedes the frozen Specification's blanket stop wording only for Phase 02 flag handling. It does not change the frozen V003 architecture or general authorization boundary. Outside Phase 02, follow the active authority and ticket-specific stop/escalation rule.

## Local request procedures

The former FQ_MUST_README.md and FUNC_REQ_BRAINBOX.md sources are archived as historical records. No current replacement for the local function-area reading and request-submission procedure has been established; this is an authority gap for a later authorized ticket. This file owns current system-wide ticket and authorization principles. Agent capability-report fields belong to the CORE registry and do not recreate the retired local procedure.
## Sources

- [Frozen V003 Specification](../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md), §§25.8, 26–27.
- [Phase 02 ticket set](../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_PHASE02_MIGRATION_TICKETS_BRAINBOX.md), P14, report contract, and batch rules.
- [Phase 02 README](../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/README_PHASE02_MIGRATION_BRAINBOX.md), active flag-handling and batch cadence.
- [Operator declaration record](../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_MIGRATION_CONVO_VERSION_UPGRADE_BRAINBOX.md), “Operator Declaration — Phase 02 Flag Handling and Batch Fix Discipline.”
- [Archived FQ request/compliance source — historical](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/FUNC_AI_BRAINBOX/FQ_MUST_README.md) and [archived FUNC_REQ source — historical](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_REQ_BRAINBOX.md). No local replacement procedure is currently established.

**Prepared by:** Codex under the Operator-authorized V003-M03 ticket.
**Last verified:** 2026-10-08
## Operator-approved discovery-first atomic-ticket and batch execution standard — 2026-10-17

**STATUS:** [ACTIVE — OPERATOR APPROVED]
**SCOPE:** System-wide prospective ticket planning, decomposition, execution and verification. Supplements existing Ticketing Governance and preserves the specifically scoped Phase 02 addendum and frozen V003 architecture.

**Execution sequence:** DISCOVER → INVENTORY → CLASSIFY → DECOMPOSE → GROUP → OPERATOR APPROVAL → PREFLIGHT → EXECUTE ONE TICKET → VERIFY → PROCEED → BATCH CLOSEOUT → PUBLICATION → ACCEPTANCE. No stage implies authorization for the next.

### Mandatory rules

**TGB-001 — Discovery precedes tickets.** Inspect actual files, approved architecture, physical paths, authority, source history, decisions, and evidence before drafting implementation tickets. An isolated observation is not a bulk implementation mandate.

**TGB-002 — Maintain a specific findings register.** Record each specific with unique ID, issue, exact path or discovery boundary, observed and expected condition, authority, reason, evidence, classification, required assessment/correction, dependency, owning ticket and acceptance evidence. Do not impose an arbitrary cap: 30–40 or more specifics are acceptable when evidence warrants.

**TGB-003 — Separate factual states.** Mark findings CONFIRMED (demonstrated defect), REVIEW (requires contextual examination), VERIFY (test with a possible NO CHANGE REQUIRED result), or BLOCKED (direct material dependency/authorization barrier). Never automatically convert a REVIEW or VERIFY into a write instruction.

**TGB-004 — Investigate why before fixing.** Check intentional architecture, empty/stub/planned destinations, historical versus current sources, physical versus capability status, missing contextual explanation, already applicable rules and actual authority gaps.

**TGB-005 — Reuse canonical Governance.** Identify the existing owner and governing section first. Propose genuinely missing system-wide rules at the proper authority and obtain approval. Do not duplicate shared policies in local documents.

**TGB-006 — One coherent responsibility per ticket.** Ordinarily scope to one file, one closely related parent/child family, one bounded ownership/reference relationship, or one independently verifiable audit. Related specifics may be grouped only when they are one coherent and jointly verifiable responsibility.

**TGB-007 — Split excessive tickets before execution.** Multiple independent authorities, unrelated files, separate risks or separately approvable changes must become separate tickets; internal bullet points do not make a bulk ticket atomic.

**TGB-008 — Controlled batches.** Group related tickets normally in batches of four through ten, organized by common outcome, dependencies, applicable authority, validation and publication boundary. Explain and obtain approval for justified exceptions; never fabricate work to reach the range.

**TGB-009 — Explicit dependencies.** Document prerequisites, downstream dependents, conflicting file ownership and stop conditions. A flag blocks directly dependent work unless a broader safety or authority boundary independently requires a wider stop. Preserve nonblocking findings for batch closeout.

**TGB-010 — Distinct approval gates.** Separate approval of findings, batch plan, ticket text, execution, new policies/structural decisions, independent verification, Git publication/merge, and final closure. Approval at one gate grants no other gate implicitly.

**TGB-011 — Mandatory preflight.** Verify repository, branch, HEAD, local/remote status, pre-existing modifications, exact path scope, current canonical Governance, protected frozen/historical evidence, dependencies, authorization, tests and safe recovery. Report PASS, QUALIFIED PASS or BLOCKED.

**TGB-012 — Executable ticket contract.** Include ID, title, objective/reason, specific IDs, exact writable scope, exclusions/read-only sources, authorities, prerequisites, preflight, ordered steps, no-change criteria, negative requirements, verifications, evidence/report destinations, stop conditions, publication boundary, independent verification and Operator acceptance.

**TGB-013 — Sequential ticket and independent verification.** Codex implements one authorized ticket at a time, tests/reads back actual results and supplies reproducible evidence for ChatGPT independent review before a dependent next ticket. Operator may explicitly authorize continuation of independent nondependent work. Codex self-PASS is not independent PASS.

**TGB-014 — Valid NO CHANGE REQUIRED.** If actual content already meets the requirement, preserve it and report exact inspection evidence; never edit to manufacture a diff.

**TGB-015 — Minimum necessary changes.** Preserve accurate words, frozen architecture, source ownership, historical bodies, prior acceptance and provenance. Register out-of-scope defects separately instead of expanding scope unilaterally.

**TGB-016 — Ticket-specific acceptance evidence.** Test applicable correctness, physical structure, authority, link integrity, status truth, historical preservation, change scope, Git diff and independent reproducibility. Qualified results identify every limitation.

**TGB-017 — Authorized Git lifecycle.** Unless the Operator explicitly directs ticket-level publication, stage, commit, push, PR and merge at the authorized batch boundary. The Operator may direct staging/committing/pushing after each approved ticket; such instruction does not authorize PR or merge. Stage only approved files, preserve ticket traceability and verify remotes. This prospective rule does not rewrite the Phase 02 addendum.

**TGB-018 — Full reporting chain.** Maintain finding-to-ticket mapping, preflight, changed and unchanged decisions, validation, Codex report, ChatGPT review, flags, Git state, batch closeout and Operator decisions. Implementation, staging, commit, push, PR, merge and acceptance are different states.

**TGB-019 — Evidence-based issue closure.** A multi-ticket issue closes only after all mandatory specifics have passed or received explicit accepted dispositions, independent review is satisfied, and the Operator accepts its closure. Partial reference alignment does not close broader DEVOPS-01/03 issues.

**TGB-020 — New discovery and rework.** Register new evidence, determine classification and dependencies, check Governance, test authorized scope and seek a revised/new approved ticket for anything outside scope. Never silently broaden the work.

### Mandatory planning and execution templates

**Template A — Individual specific**

```text
SPECIFIC ID:
ORIGINATING ISSUE:
AFFECTED PATH OR DISCOVERY BOUNDARY:
CLASSIFICATION: CONFIRMED / REVIEW / VERIFY / BLOCKED
OBSERVED CONDITION:
EXPECTED CONDITION AND GOVERNING AUTHORITY:
EVIDENCE AND WHY IT MATTERS:
REQUIRED INSPECTION:
PROPOSED CORRECTION OR NO-CHANGE CONDITION:
DEPENDENCIES:
ASSIGNED TICKET:
ACCEPTANCE EVIDENCE:
```

**Template B — Batch plan**

```text
BATCH ID / OBJECTIVE:
OPERATOR APPROVAL STATUS:
BASELINE BRANCH AND SHA:
GOVERNANCE PREREQUISITES:
ORDERED TICKETS AND SPECIFICS:
DIRECT DEPENDENCIES AND SHARED-FILE RISKS:
PROTECTED FILES:
INDEPENDENT PER-TICKET VERIFICATION GATES:
BATCH CLOSEOUT AND GIT PUBLICATION GATES:
OPEN FLAGS:
```

**Template C — Atomic ticket**

```text
TICKET ID / TITLE / BATCH:
EXECUTION AGENT / INDEPENDENT VERIFIER:
OPERATOR EXECUTION APPROVAL:
OBJECTIVE AND SPECIFICS:
EXACT WRITABLE PATHS AND READ-ONLY SOURCES:
EXCLUSIONS AND AUTHORITY REFERENCES:
PREFLIGHT:
STEPWISE EXECUTION:
NO-CHANGE AND STOP CONDITIONS:
TESTS AND REPRODUCIBLE EVIDENCE:
REPORT LOCATION:
STAGING / COMMIT / PUSH / PR / MERGE AUTHORITY:
INDEPENDENT ACCEPTANCE AND OPERATOR DECISION:
```

**Template D — Ticket result**

```text
TICKET / BASELINE:
PREFLIGHT:
PATHS INSPECTED / SPECIFICS:
CHANGES / NO-CHANGE RESULTS:
TEST RESULTS AND EVIDENCE:
FLAGS / DEPENDENCY IMPACT:
CODEX DISPOSITION:
CHATGPT INDEPENDENT VERIFICATION:
OPERATOR ACCEPTANCE:
EXACT GIT STATE:
NEXT AUTHORIZED TICKET:
```

### Responsibility and precedence

The **findings register** establishes coverage; **batch plan** coordinates related atomic tickets; **ticket** defines execution; **canonical Governance** defines authority; **independent verification and Operator acceptance** decide closure. These instruments are distinct. Existing frozen V003 authority and phase-scoped rules remain protected. Agents act only on evidence-backed specifics and explicitly approved scope, never convenient assumptions.

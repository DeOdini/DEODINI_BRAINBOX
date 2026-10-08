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

Function-area request submission and compliance procedures remain documented in `FQ_MUST_README.md` and `FUNC_REQ_BRAINBOX.md` pending their content-specific migration. This file owns system-wide ticket and authorization principles; it does not replace those local procedures.

## Sources

- [Frozen V003 Specification](../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md), §§25.8, 26–27.
- [Phase 02 ticket set](../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_PHASE02_MIGRATION_TICKETS_BRAINBOX.md), P14, report contract, and batch rules.
- [Phase 02 README](../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/README_PHASE02_MIGRATION_BRAINBOX.md), active flag-handling and batch cadence.
- [Operator declaration record](../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_MIGRATION_CONVO_VERSION_UPGRADE_BRAINBOX.md), “Operator Declaration — Phase 02 Flag Handling and Batch Fix Discipline.”
- [Legacy function request/compliance records](../AI_BRAINBOX/FUNC_AI_BRAINBOX/FQ_MUST_README.md) and `FUNC_REQ_BRAINBOX.md`, local procedure pending M07/M19/M20.

**Prepared by:** Codex under the Operator-authorized V003-M03 ticket.
**Last verified:** 2026-10-08

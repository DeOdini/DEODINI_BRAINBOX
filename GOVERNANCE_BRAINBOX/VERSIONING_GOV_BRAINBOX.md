# VERSIONING_GOV_BRAINBOX

**STATUS:** [ACTIVE — CANONICAL]
**CANONICAL SOURCE:** Frozen V003 Specification §25.4 and §27.
**APPLIES TO:** Brainbox architecture generations and Git-backed change history.

## Generation history

- Preserve Brainbox architecture generations and the reasons for material changes.
- Do not overwrite an earlier generation or describe it as if it never existed.
- Keep the frozen V003 Specification as the V003 target authority and the Origin Conversation as decision history.
- A migration ledger records evidence-backed source-to-target dispositions; it does not itself authorize migration or source deletion.

## Git lifecycle is separate

A branch, commit, push, pull request, merge, or deployment describes a repository lifecycle state. It does not by itself create or prove a Brainbox architecture generation. Report these states separately:

- local implementation is not a staged change;
- staging is not a commit;
- a commit is not a push;
- a push is not a merge;
- a merge is not a deployment;
- deployment is not Operator verification.

Use the authorized branch and batch workflow. Do not force-push, rewrite history, or remove recovery objects without explicit authority. Before destructive migration, verify the approved repository-history recovery method and separately inventory untracked or ignored material; Git history does not preserve those files.

## Sources

- [Frozen V003 Specification](../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md), §§25.4, 25.10, 25.12, 27.
- [Origin Conversation](../V003_VERSION_UPGRADE_BRAINBOX/V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md), Version History and generation decisions.
- [Phase 02 ticket set](../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_PHASE02_MIGRATION_TICKETS_BRAINBOX.md), batch Git lifecycle and recovery rules.
- [Migration Map](../VERSION_HISTORY_BRAINBOX/V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md), current source and integrity baseline.

**Prepared by:** Codex under the Operator-authorized V003-M03 ticket.
**Last verified:** 2026-10-08

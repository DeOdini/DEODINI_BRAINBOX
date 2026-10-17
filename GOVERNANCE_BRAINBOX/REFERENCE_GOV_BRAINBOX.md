# REFERENCE_GOV_BRAINBOX

**STATUS:** [ACTIVE — CANONICAL]
**CANONICAL SOURCE:** Frozen V003 Specification §§5, 25.2–25.3.
**APPLIES TO:** Cross-domain Brainbox knowledge and authority links.

## Canonical ownership

1. Assign each reusable rule or body of knowledge one canonical owner.
2. Other records may link to or summarize that source when needed, but must not maintain independent copies that can drift.
3. A root or local README may state its own purpose and navigation. Shared rules belong to Governance and should be referenced.
4. Keep architecture authority, historical decision evidence, and migration-process records distinct: the frozen Specification defines the V003 target; the Origin Conversation preserves decision history; Phase 02 records current migration execution.

## Reference quality

- Use the exact current repository path and a relative link from the referencing file where practical.
- Name the authority and the relevant section or anchor; do not use a vague path label when the reader needs a specific rule.
- Check that local links resolve after an authorized move or rename.
- Keep a reference to a source while its content is still retained for historical or migration purposes.
- Do not infer that a planned destination exists merely because it appears in an approved target tree.

## Relationship to Documentation Governance

[DOCUMENTATION_GOV_BRAINBOX.md](DOCUMENTATION_GOV_BRAINBOX.md) owns the system-wide documentation methodology and includes the proposed **Universal Documentation Governance Framework Specification — V003**, inserted on 2026-10-16 and still marked **DRAFT — OPERATOR REVIEW REQUIRED**. Its pre-existing canonical provisions remain active; the new draft becomes binding only after separate approval.

- **Documentation Governance** governs how agents inspect folders, classify documentation and rule placement, construct READMEs and templates, and control modifications and verification.
- **Reference Governance (this document)** governs canonical ownership, cross-domain authority references, current-versus-historical distinction, relative links and reference maintenance after approved changes.
- **[Tree and Status Governance](TREE_AND_STATUS_GOV_BRAINBOX.md)** governs the applicable physical tree and status-representation standards.

An agent constructing or modifying a README must identify all applicable authorities and link to each source without copying its policy text. Cross-references do not transfer ownership. Conflicts require documented escalation through approved procedures; agents must not invent precedence.

## Current migration references

Canonical ownership and reference rules apply to current repository sources, active documentation and retained historical evidence.

The completed V003 corrective retirements have these current dispositions:

| Source category | Current disposition | Governing evidence |
|---|---|---|
| Former `PROJ_WORKFLOW_AI_BRAINBOX/` | Retired from the former active path; preserved in the Recycle Bin | Ticket 01, Retirement Ledger, Migration Map |
| Legacy DOB/FQ/AI_MUST | Retired as active authority; preserved as historical sources | Ticket 02 |
| Standalone FUNC legacy files | Retired from active FUNC; preserved historically | Ticket 02 |
| Former `SKILLS_AVAIL_AI_BRAINBOX/` | Retired; historical README preserved | Ticket 03 |
| `SKILLS_AI_BRAINBOX/` | Sole active Skills master | Current Skills README |
| Historical V002 Milestones checkpoint and MUST README | Retired into the historical archive | Ticket 03 |
| `MILESTONES_BRAINBOX/` | Current Milestones folder, separate from V002 archive | Current Milestones README |

The M01 inventory and integrity baselines remain historical evidence; they do not establish that retired sources remain present or authoritative at former paths.

Current references MUST distinguish **active authority**, **historical evidence**, **migration evidence**, and **planned destinations**. Planned paths must not be represented as existing before verification. Agents MUST use current verified paths and MUST NOT restore archived operating instructions to satisfy an obsolete reference.

The [Retirement Ledger](../RECYCLE_BIN_BRAINBOX/RETIREMENT_LEDGER_BRAINBOX.md), [Migration Map](../VERSION_HISTORY_BRAINBOX/V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md), and [Phase 03 Fixes Report](../V003_VERSION_UPGRADE_BRAINBOX/PHASE03_FIXES_BRAINBOX/V003_FIXES_REPORT_BRAINBOX.md) preserve the supporting evidence and qualifications. Preserve historical bodies; document later dispositions with dated records.

## Sources

- [Frozen V003 Specification](../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md), §§5, 25.2–25.3, 27.
- [Archived root master-copy and reference-link rules — historical](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/DOB_MUST_README.md).
- [Archived AI local navigation reference — historical](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/AI_MUST_README.md).
- [Archived function-area source — historical](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/FUNC_AI_BRAINBOX/FQ_MUST_README.md).
- [Archived project local reference](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/PROJ_MUST_README.md) - historical source; current navigation is in DEVOPS and Sandbox READMEs.
- [Current Skills master navigation](../AI_BRAINBOX/SKILLS_AI_BRAINBOX/README_SKILLS_AI_BRAINBOX.md) — sole active Skills authority.
- [Archived legacy Skills README — retired historical source](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/SKILLS_AVAIL_AI_BRAINBOX/SKILLS_MUST_README.md).
- [Documentation Governance — canonical documentation authority](DOCUMENTATION_GOV_BRAINBOX.md) — existing active requirements and separately marked draft universal framework.
- [Tree and Status Governance](TREE_AND_STATUS_GOV_BRAINBOX.md) — applicable physical tree and status requirements.
- [Phase 03 Fixes Report](../V003_VERSION_UPGRADE_BRAINBOX/PHASE03_FIXES_BRAINBOX/V003_FIXES_REPORT_BRAINBOX.md) — corrective retirement outcomes, limits and publication records.
- [Current Milestones README](../MILESTONES_BRAINBOX/README_MILESTONES_BRAINBOX.md) — active navigation.
- [Archived V002 Milestones checkpoint — historical](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/MILESTONES_BRAINBOX/MILESTONE_CHECKPOINT_BRAINBOX.md).
- [Archived V002 Milestones MUST README — historical](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/MILESTONES_BRAINBOX/MILESTONES_MUST_README.md).

**Prepared by:** Codex under the Operator-authorized V003-M03 ticket.
**Last verified:** 2026-10-08
**Ticket 01 route check:** 2026-10-16; the former PROJ_WORKFLOW source is absent and the archive and Migration Map links resolve. Other M03 source authorities were not re-audited under Ticket 01.

**Ticket 03 route check:** 2026-10-16; current Skills navigation resolves to `AI_BRAINBOX/SKILLS_AI_BRAINBOX/README_SKILLS_AI_BRAINBOX.md`. The former Skills source is archived as historical, and both retired V002 Milestones files route to their Ticket 03 archive paths. No historical body was rewritten.

## Reference Governance reconciliation — 2026-10-17

**Review initiated and wording approved by:** Operator
**Review and insertion performed by:** ChatGPT
**Inputted by:** ChatGPT
**Status:** Published in PR [#56](https://github.com/DeOdini/DEODINI_BRAINBOX/pull/56) and merged into `main` at merge commit `a0eee3d27b428d42e542d217ac73b57fd09a921d`; independent post-publication acceptance is not claimed.
**Verification classification:** QUALIFIED REVIEW

The canonical ownership and reference principles remain consistent with Documentation Governance. The prior general statement about original legacy locations was superseded with current retirement dispositions. The proposed universal framework is now explicitly referenced with its draft-status qualification. Current and archived Milestones links are added while pre-existing historical verification and ticket-route records remain intact.

**Verification limits:** The preceding review verified selected current and archived paths; it was not a full backlink, Markdown-anchor, SHA-256, capability or deployment audit. The original 2026-10-08 verification and Ticket 01/03 route checks are preserved. Final local link and diff results are recorded separately in the implementation report.

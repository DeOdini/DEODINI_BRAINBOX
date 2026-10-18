# REFERENCE_GOV_BRAINBOX

**STATUS:** [ACTIVE — CANONICAL]
**CANONICAL SOURCE:** Frozen V003 Specification §§5, 25.2–25.3.
**APPLIES TO:** Cross-domain Brainbox knowledge and authority links.

## Canonical ownership

1. Assign each reusable rule or body of knowledge one canonical owner.
2. Other records may link to or summarize that source when needed, but must not maintain independent copies that can drift.
3. A root or local README may state its own purpose and navigation. Shared rules belong to Governance and should be referenced.
4. Keep architecture authority, historical decision evidence, and migration-process records distinct: the frozen Specification defines the V003 target; the Origin Conversation preserves decision history; Phase 02 records current migration execution.

## Cross-domain read and ticket-scoped update ownership — 2026-10-18

The E02 discovery established these canonical navigation routes and possible update destinations. **A mapping is not permission to write.** Every change still requires an approved ticket and applicable verification. Local READMEs own detailed internal navigation.

| Domain | Canonical read source | Ticket-scoped update destination | Evidence and limits |
|---|---|---|---|
| FUNC | [FUNC README](../AI_BRAINBOX/FUNC_AI_BRAINBOX/README_FUNC_AI_BRAINBOX.md), then its CORE/EXE registries | Appropriate CORE capability record or EXE execution-evidence record | M05–M07; former FUNC/FQ sources are archived, not current instructions |
| DEVOPS Sandbox | [DEVOPS README](../AI_BRAINBOX/DEVOPS_AI_BRAINBOX/README_DEVOPS_AI_BRAINBOX.md) and [Sandbox README](../AI_BRAINBOX/DEVOPS_AI_BRAINBOX/SANDBOX_DEVOPS_BRAINBOX/README_SANDBOX_DEVOPS_BRAINBOX.md) | Authorized Sandbox workflow or POC/trial record | M09–M15; trial success does not imply Production success |
| DEVOPS Production | DEVOPS README and [Production README](../AI_BRAINBOX/DEVOPS_AI_BRAINBOX/PROD_DEVOPS_BRAINBOX/README_PROD_DEVOPS_BRAINBOX.md) | Actual Production procedure, environment or evidence record | M14/M16; stubs do not demonstrate deployments |
| Skills | [Skills README](../AI_BRAINBOX/SKILLS_AI_BRAINBOX/README_SKILLS_AI_BRAINBOX.md) and relevant child | Relevant current Skills record | M08; legacy Skills master retired; planned areas stay planned |
| Portfolio | [Portfolio README](../PORTFOLIO_BRAINBOX/README_PORTFOLIO_BRAINBOX.md), then [FootHive Portfolio README](../PORTFOLIO_BRAINBOX/FOOTHIVE_PORTFOLIO_BRAINBOX/README_FOOTHIVE_PORTFOLIO_BRAINBOX.md) where applicable | Portfolio summary, handoff or presentation record | M16; presentation does not replace original test evidence |
| FootHive split | External `DeOdini/FOOTHIVE` website implementation; [Sandbox trial](../AI_BRAINBOX/DEVOPS_AI_BRAINBOX/SANDBOX_DEVOPS_BRAINBOX/POC_SANDBOX_BRAINBOX/FOOTHIVE_POC_BRAINBOX/README_FH_WORKFLOW_TRIAL_BRAINBOX.md); [Production summary](../AI_BRAINBOX/DEVOPS_AI_BRAINBOX/PROD_DEVOPS_BRAINBOX/POC_PROD_BRAINBOX/FOOTHIVE_PROD_SUMMARY_BRAINBOX/README_FOOTHIVE_PROD_SUMMARY_BRAINBOX.md); Portfolio above | Code in external repo under its own authority; trial, Production and portfolio evidence in their separate Brainbox domains | M15/M16, DEVOPS routing; reference to external repo does not prove checkout or service health |
| Milestones | [Milestones README](../MILESTONES_BRAINBOX/README_MILESTONES_BRAINBOX.md) and [Router/Agentic milestone](../MILESTONES_BRAINBOX/BRAINBOX_ROUTER_AGENTIC_MILESTONE_BRAINBOX.md) | Current planned Router/Agentic records only, under an approved ticket; preserve [PLANNED] status unless separately authorized | M17/M18; V002 milestones archived |
| Archives and version history | [Recycle Bin README](../RECYCLE_BIN_BRAINBOX/README_RECYCLE_BIN_BRAINBOX.md), [retirement ledger](../RECYCLE_BIN_BRAINBOX/RETIREMENT_LEDGER_BRAINBOX.md), [Version History README](../VERSION_HISTORY_BRAINBOX/README_VERSION_HISTORY_BRAINBOX.md), [V003 Migration Map](../VERSION_HISTORY_BRAINBOX/V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md), and the [Phase 01](../V003_VERSION_UPGRADE_BRAINBOX/PHASE01_POLISH_BRAINBOX/README_PHASE01_POLISH_BRAINBOX.md), [Phase 02](../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/README_PHASE02_MIGRATION_BRAINBOX.md), and [Phase 03](../V003_VERSION_UPGRADE_BRAINBOX/PHASE03_FIXES_BRAINBOX/README_PHASE03_FIXES_BRAINBOX.md) support READMEs | Retirement ledger/manifest, Migration Map or Phase records only under respective approved tickets | M20/M21; archived bodies remain historical/read-only; Phase records are audit/process support, not domain authority |

This table is a bounded ownership directory, not a live-capability certification. Cross-domain references do not transfer ownership. Resolve ambiguous destinations by inspecting their local sources and escalating under [Ticketing Governance](TICKETING_GOV_BRAINBOX.md).

## Reference quality

- Use the exact current repository path and a relative link from the referencing file where practical.
- Name the authority and the relevant section or anchor; do not use a vague path label when the reader needs a specific rule.
- Check that local links resolve after an authorized move or rename.
- Keep a reference to a source while its content is still retained for historical or migration purposes.
- Do not infer that a planned destination exists merely because it appears in an approved target tree.

### Reference purpose and contextual explanation

**Operator-approved amendment — 2026-10-17.** Approved by the Operator and recorded by Codex. This subsection is an active Reference Governance requirement. It does not adopt the Universal Documentation Governance Framework, which remains **DRAFT — NOT YET ADOPTED**.

For each active documentation reference, its reason for inclusion must be discernible from the referencing document. The purpose may appear beside the link or in an immediately identifiable contextual paragraph, ownership table, or reference directory. Do not add repetitive explanations when the existing context already makes the purpose clear.

When constructing or evaluating a reference, establish:

1. What destination is referenced?
2. What relationship connects that destination to the current document?
3. Why is that relationship necessary?
4. What is the destination's state, where material (for example, current, planned, empty, historical, or external)?
5. What may an agent legitimately obtain from the destination?
6. What must not be inferred from the reference?

An empty or planned destination may be linked for authorized navigation, but the link does not establish that it is populated or active. A historical source may be cited for provenance, but must not be presented as current execution authority. An external project reference does not establish that its implementation, deployment, or live service has been verified.

Before labeling an unclear reference defective or correcting it, inspect the destination and the surrounding documentation. Do not add generic descriptions without inspection, assume a stub contains implementation knowledge, change canonical ownership for convenience, duplicate governing text into local READMEs, fill empty folders to justify links, rewrite historical files, or perform blanket reference-list rewrites.

[Documentation Governance §9](DOCUMENTATION_GOV_BRAINBOX.md#9-reference-construction-standard), including Template C's reference-entry fields, is available as a construction guide only; it remains part of the DRAFT framework and is not the source of this binding requirement. This subsection states the required outcome without reproducing the full template or creating a second template authority.

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

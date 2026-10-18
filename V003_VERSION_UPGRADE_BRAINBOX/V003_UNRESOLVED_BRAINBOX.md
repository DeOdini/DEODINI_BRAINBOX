# V003_UNRESOLVED_BRAINBOX

**Status:** ACTIVE — CATEGORIZED CORRECTIVE INTAKE (reviewed 2026-10-18). The former Specification §§8–18 item remains closed; current corrective findings are tracked below and require individually selected and authorized Codex tickets.

**Authority:** [V003 Specification](V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md), [Origin Conversation](V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md), [Phase 03 report](PHASE03_FIXES_BRAINBOX/V003_FIXES_REPORT_BRAINBOX.md), [Migration Map](../VERSION_HISTORY_BRAINBOX/V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md).

## Current pending or planned follow-ups

The previous Specification §§8–18 classification/navigation case was closed by Operator approval on 2026-10-16; its semantic-label verification boundary remains recorded in the Phase 03 report and Migration Map. New current corrective findings appear in the categorized intake section below.

## Future category-based corrective register — Operator-approved layout

New issues must be grouped by affected **folder / file authority**, not mixed together. Each category heading names its primary folder(s) and uses a severity tag: [CRITICAL], [HIGH], [MEDIUM], or [LOW]. Criticality is based on impact and dependency, not reading order alone.

Within each category, each separately traceable fix has its own severity tag and fields: **Fix ID**, **Exact affected paths**, **Defect/evidence**, **Required correction**, **Dependencies (IDs and affected categories)**, **Verification/acceptance gate**, **Owner**, and **State**. Dependencies spanning categories must be referenced both ways where relevant. A README fix requiring a Governance policy decision is blocked only on that specifically linked Governance decision; other fixes may proceed independently.

For example, future headings could read `### README_BRAINBOX.md / root navigation [CRITICAL]` and `### GOVERNANCE_BRAINBOX/ [MEDIUM]`; these labels are format illustrations **only**, not accepted issue rankings or active defects. Do not promote proposed Grok flags into active entries until their paths, evidence and severity are reviewed. Keep resolved cases in permanent reports rather than this active register.

## Clear-on-resolution rule

The 20-SHA M01-GIT-01/M21-GIT-01 case is **CLOSED ADMINISTRATIVELY** and therefore no longer appears as an active entry here. The full Operator declaration, supplied Grok research (including 20 SHA strings), evidence limits and speculative hypothesis are preserved in the permanent Phase 03 report and cross-referenced by the Migration Map. F03, F04, F05, F06, F09, F10, F12, F13, F14 and F16 approved/closed dispositions are also retained in permanent reports rather than carried as unresolved rows. DEVOPS-01 and DEVOPS-03 were closed with Operator-accepted documented qualifications on 2026-10-17 (PRs #68–#69); README-02's Ticket 01/02 retirement-routing portion is resolved. FUNC-03's CORE/EXE evidence audit and C01-R01 date clarification were independently verified PASS and Operator-accepted on 2026-10-17; FUNC-04 was closed by Operator acceptance on 2026-10-17; its closure evidence is retained in the permanent Phase 03 report and ticket register. Their closure evidence remains in the Phase 03 report, ticket register, Migration Map and retirement records, rather than active rows.

For each future resolved item: independently verify the closure condition, append a dated record to the permanent report, update canonical references, then delete its active entry from this file. DEVOPS-02 was removed under this rule after Ticket 01 final cleanup acceptance; the permanent evidence remains in the Phase 03 report, Migration Map and Retirement Ledger. Intentionally planned future capabilities remain until implemented or explicitly removed from the backlog by an Operator decision. Never erase historical reports or alter protected source files as part of backlog cleanup.
## Active categorized corrective findings — Operator-approved intake (reviewed 2026-10-18)

**Active issue index (01-05, Operator-reconciled 2026-10-18):** 01 README-01; 02 README-03; 03 GOVERNANCE-02; 04 GOVERNANCE-03; 05 GOVERNANCE-04. Display numbers only; permanent issue IDs retained. V003-STATUS-01, V003-STATUS-02 and GOVERNANCE-01 retired from active intake by Operator disposition; historical records and D01/D02 verifier-provenance qualifications remain in the Phase 03 report.

**Scope:** This is the new, separately selected corrective-work backlog following closure of the former Specification §§8–18 classification case. The earlier case remains closed and is not reopened. Findings are not executed by adding them here. **State:** ACTIVE UNRESOLVED FINDINGS / AWAITING PER-FILE TICKET SELECTION; verified symptoms are distinguished from proposed mitigations. The Operator selects each folder/file for a separately scoped Codex ticket, independent ChatGPT verification and acceptance. No blanket retirement or replacement is authorized.

**Execution-order rule:** Prioritize dependency completion over severity alone. Fix and verify *source subfolders and their authoritative navigation* first; only after those destinations and statuses are settled, finalize root README and Governance cross-references. The critical root/central layers may be drafted earlier but MUST NOT finalize pointers to uncertain or V002 source paths. Separate policy decisions that are true prerequisites can be authorized earlier; do not block unrelated fixes. Preserve historical bodies and frozen Specification without new source-specific authority.

### V003_VERSION_UPGRADE_BRAINBOX/ [HIGH]


### README_BRAINBOX.md — root and navigation [CRITICAL]

- **01. README-01 [CRITICAL]** — Path: `README_BRAINBOX.md`. **Risk:** new agents may misread entry order or historical source references as active authority. **Correction to ticket:** final root entry/precedence routes to inspected canonical child READMEs. DEVOPS-01's reviewed documentation-routing portion is closed with Operator-accepted qualifications (2026-10-17). Remaining dependency: GOVERNANCE-01 where it establishes necessary policy; FUNC-01/FUNC-02 are resolved by Corrective Ticket 02. **Gate:** current destination and reading order correct; root stays sole complete-tree authority. **State:** BLOCKED ON REMAINING NAMED SUBFOLDER ROUTING.

- **02. README-03 [HIGH]** — Path: root README and direct-child navigation. **Risk:** root full tree can become inconsistent with verified descendant paths/authorities. **Correction to ticket:** refresh current root pointers only after subordinate branches are independently verified. DEVOPS-01's reviewed documentation-routing portion is closed with Operator-accepted qualifications (2026-10-17). Remaining dependency: GOVERNANCE-02; FUNC-01 is resolved by Corrective Ticket 02. **Gate:** link/path and status truth, no contradictory root-local trees. **State:** BLOCKED ON REMAINING NAMED SUBFOLDER ROUTING.

### GOVERNANCE_BRAINBOX/ [CRITICAL]

- **03. GOVERNANCE-02 [HIGH]** — Paths: `REFERENCE_GOV_BRAINBOX.md` and Governance README. **Gap:** canonical read/write matrix across FUNC, DEVOPS, Skills, Portfolio, FootHive, Milestones and archives. **Correction to ticket:** finalize matrix **after** respective source-folder mapping. DEVOPS-01's reviewed documentation-routing portion is closed with Operator-accepted qualifications (2026-10-17), and DEVOPS-02 is resolved. Remaining dependency: selected source-folder mappings; FUNC-01/02 routing was resolved by Corrective Ticket 02, and current Skills/Milestones routing was reconciled by Corrective Ticket 03. **Gate:** exact verified destinations; never revive V002 paths. **State:** BLOCKED ON REMAINING SUBFOLDER ROUTING.
- **04. GOVERNANCE-03 [HIGH]** — Paths: `DOCUMENTATION_GOV_BRAINBOX.md`, `EVIDENCE_GOV_BRAINBOX.md`. **Gap:** lack of enforceable tool-output contamination safeguards. **Correction to ticket:** documented prevention and forensic preservation. **Depends on:** preserved Ticket 02 forensic evidence in permanent records. **Gate:** historical provenance unchanged until disposition. **State:** SELECTABLE / NOT FIXED.
- **05. GOVERNANCE-04 [MEDIUM]** — Paths: `TREE_AND_STATUS_GOV_BRAINBOX.md` and tooling references. **Gap:** automatic enforcement of two-level trees, physical paths, status vocabulary and relative links. **Correction to ticket:** scoped validation checks; do not populate planned branches. **Depends on:** stable subordinate README routes. **Gate:** reproducible checks and qualified limitations. **State:** SELECTABLE / NOT FIXED.

### Cross-category dependency / proposed selection order

1. DEVOPS-01 is closed within its accepted documentation scope (2026-10-17). Any selected Portfolio source-route review remains separately selectable; FUNC-03 and FUNC-04 are closed with Operator acceptance, and their active entries are removed here while permanent closure evidence remains in the Phase 03 report and ticket register. Skills/Milestones retirements and legacy FUNC/DOB/AI_MUST retirements are closed.
2. GOVERNANCE-01 was dispositioned under Batch D; GOVERNANCE-02 canonical ownership matrix follows the remaining child mappings.
3. README-01 and README-03 root routes follow their named dependencies; resolved README-02 retirement routing is documented in the permanent Phase 03 records.
4. GOVERNANCE-03/04 remain active with their respective prerequisites; the three Batch D findings are no longer in active intake.

**Per-ticket execution rule:** Operator selects a category/file and authorizes planning; Codex implements only the named approved ticket; ChatGPT independently verifies; Operator accepts; Git staging/publication remains a separate approval gate. A blocking flag stops only directly dependent tickets, not unrelated work.


## Closure reference — Operator acceptance, 2026-10-16

The Legacy DOB/FQ/AI_MUST findings (LEGACY-01 qualified, LEGACY-02 resolved, LEGACY-03 qualified), old Skills Availability retirement, and historical V002 Milestones retirement are **CLOSED** and intentionally excluded from the active corrective register. Source integrity and qualifications are preserved in the Phase 03 Fixes Report, Migration Map, and Recycle Bin Retirement Ledger. Corrective Ticket 02 was published in PRs #51–52; Ticket 03 in PRs #53–55. This acceptance does not validate unproven Skills capabilities, implement the planned Router milestone, or close separate remaining Governance and FUNC issues.

## Batch D Operator issue disposition - 2026-10-18

Operator directed removal of the precisely resolved Batch D cases GOVERNANCE-01 and V003-STATUS-01 following the earlier removal of V003-STATUS-02. The surviving five permanent issue IDs are unchanged. D01 no-policy-change and D02 status-documentation execution outcomes were accepted for active-backlog disposition; independent verifier-provenance qualifications remain in dated Phase 03 records and are not silently recast as proven technical PASS. This update is local and not Git-published.

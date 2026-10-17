# V003_UNRESOLVED_BRAINBOX

**Status:** ACTIVE — CATEGORIZED CORRECTIVE INTAKE (reviewed 2026-10-17). Previous Specification §§8–18 item remains closed; newly documented findings await individually selected and authorized Codex tickets.

**Authority:** [V003 Specification](V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md), [Origin Conversation](V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md), [Phase 03 report](PHASE03_FIXES_BRAINBOX/V003_FIXES_REPORT_BRAINBOX.md), [Migration Map](../VERSION_HISTORY_BRAINBOX/V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md).

## Current pending or planned follow-ups

The previous Specification §§8–18 classification/navigation case was closed by Operator approval on 2026-10-16; its semantic-label verification boundary remains recorded in the Phase 03 report and Migration Map. New current corrective findings appear in the categorized intake section below.

## Future category-based corrective register — Operator-approved layout

New issues must be grouped by affected **folder / file authority**, not mixed together. Each category heading names its primary folder(s) and uses a severity tag: [CRITICAL], [HIGH], [MEDIUM], or [LOW]. Criticality is based on impact and dependency, not reading order alone.

Within each category, each separately traceable fix has its own severity tag and fields: **Fix ID**, **Exact affected paths**, **Defect/evidence**, **Required correction**, **Dependencies (IDs and affected categories)**, **Verification/acceptance gate**, **Owner**, and **State**. Dependencies spanning categories must be referenced both ways where relevant. A README fix requiring a Governance policy decision is blocked only on that specifically linked Governance decision; other fixes may proceed independently.

For example, future headings could read `### README_BRAINBOX.md / root navigation [CRITICAL]` and `### GOVERNANCE_BRAINBOX/ [MEDIUM]`; these labels are format illustrations **only**, not accepted issue rankings or active defects. Do not promote proposed Grok flags into active entries until their paths, evidence and severity are reviewed. Keep resolved cases in permanent reports rather than this active register.

## Clear-on-resolution rule

The 20-SHA M01-GIT-01/M21-GIT-01 case is **CLOSED ADMINISTRATIVELY** and therefore no longer appears as an active entry here. The full Operator declaration, supplied Grok research (including 20 SHA strings), evidence limits and speculative hypothesis are preserved in the permanent Phase 03 report and cross-referenced by the Migration Map. F03, F04, F05, F06, F09, F10, F12, F13, F14 and F16 approved/closed dispositions are also retained in permanent reports rather than carried as unresolved rows. DEVOPS-01 and DEVOPS-03 were closed with Operator-accepted documented qualifications on 2026-10-17 (PRs #68–#69); README-02's Ticket 01/02 retirement-routing portion is resolved. Their closure evidence remains in the Phase 03 report, ticket register, Migration Map and retirement records, rather than active rows.

For each future resolved item: independently verify the closure condition, append a dated record to the permanent report, update canonical references, then delete its active entry from this file. DEVOPS-02 was removed under this rule after Ticket 01 final cleanup acceptance; the permanent evidence remains in the Phase 03 report, Migration Map and Retirement Ledger. Intentionally planned future capabilities remain until implemented or explicitly removed from the backlog by an Operator decision. Never erase historical reports or alter protected source files as part of backlog cleanup.
## Active categorized corrective findings — Operator-approved intake (reviewed 2026-10-17)

**Active issue index (01–10):** 01 FUNC-03; 02 FUNC-04; 03 V003-STATUS-01; 04 V003-STATUS-02; 05 README-01; 06 README-03; 07 GOVERNANCE-01; 08 GOVERNANCE-02; 09 GOVERNANCE-03; 10 GOVERNANCE-04. These are display numbers only; permanent issue IDs remain unchanged.

**Scope:** This is the new, separately selected corrective-work backlog following closure of the former Specification §§8–18 classification case. The earlier case remains closed and is not reopened. Findings are not executed by adding them here. **State:** ACTIVE UNRESOLVED FINDINGS / AWAITING PER-FILE TICKET SELECTION; verified symptoms are distinguished from proposed mitigations. The Operator selects each folder/file for a separately scoped Codex ticket, independent ChatGPT verification and acceptance. No blanket retirement or replacement is authorized.

**Execution-order rule:** Prioritize dependency completion over severity alone. Fix and verify *source subfolders and their authoritative navigation* first; only after those destinations and statuses are settled, finalize root README and Governance cross-references. The critical root/central layers may be drafted earlier but MUST NOT finalize pointers to uncertain or V002 source paths. Separate policy decisions that are true prerequisites can be authorized earlier; do not block unrelated fixes. Preserve historical bodies and frozen Specification without new source-specific authority.

### AI_BRAINBOX/FUNC_AI_BRAINBOX/ [HIGH]

- **01. FUNC-03 [MEDIUM]** — Paths: agent-specific CORE/EXE records. **Finding:** completeness and actual capabilities vary or are unverified. **Correction to ticket:** identify substantive versus stub/unverified documentation; do not fabricate capability proof. **Depends on:** none; the FUNC-01 tree/routing prerequisite was resolved by Corrective Ticket 02, while capability validation remains a separate scope. **Gate:** evidence-backed claims. **State:** SELECTABLE / NOT FIXED.
- **02. FUNC-04 [MEDIUM]** — Path: AI_BRAINBOX/FUNC_AI_BRAINBOX/README_FUNC_AI_BRAINBOX.md. **Finding:** Ticket 02 retired the legacy local request/compliance sequence with no verified replacement. Governance remains system-wide authority and CORE/EXE remain the active capability registries, but no current FUNC-specific procedure replaces the archived request/compliance workflow. **Required action:** Operator selects a separately scoped ticket to determine whether a local procedure is needed and, if so, authorize its design. Do not reconstruct the archived workflow by assumption. **State:** OPEN / NON-BLOCKING TO TICKET 02; future ticket required.

### V003_VERSION_UPGRADE_BRAINBOX/ [HIGH]

- **03. V003-STATUS-01 [HIGH]** — Paths: `README_V003_VERSION_UPGRADE_BRAINBOX.md`; `PHASE02_MIGRATION_BRAINBOX/README_PHASE02_MIGRATION_BRAINBOX.md`; `V003_UNRESOLVED_BRAINBOX.md`. **Finding:** QUALIFIED CLOSED and historical M21/F02 pending checkpoints can be confused. **Correction to ticket:** provide concise dated present-state pointers while preserving prior checkpoint text. **Depends on:** already approved Operator dispositions; GOVERNANCE-01 if policy precedence needed. **Gate:** qualified closure never asserted as blanket technical PASS. **State:** SELECTABLE / NOT FIXED.
- **04. V003-STATUS-02 [MEDIUM]** — Paths: V003 status and historical reports. **Finding:** append-only superseded sections can obscure current reading. **Correction to ticket:** explicit checkpoint labeling/indexes; no deletion of evidence. **Depends on:** V003-STATUS-01. **Gate:** historical statuses remain traceable. **State:** SELECTABLE / NOT FIXED.

### README_BRAINBOX.md — root and navigation [CRITICAL]

- **05. README-01 [CRITICAL]** — Path: `README_BRAINBOX.md`. **Risk:** new agents may misread entry order or historical source references as active authority. **Correction to ticket:** final root entry/precedence routes to inspected canonical child READMEs. DEVOPS-01's reviewed documentation-routing portion is closed with Operator-accepted qualifications (2026-10-17). Remaining dependency: GOVERNANCE-01 where it establishes necessary policy; FUNC-01/FUNC-02 are resolved by Corrective Ticket 02. **Gate:** current destination and reading order correct; root stays sole complete-tree authority. **State:** BLOCKED ON REMAINING NAMED SUBFOLDER ROUTING.

- **06. README-03 [HIGH]** — Path: root README and direct-child navigation. **Risk:** root full tree can become inconsistent with verified descendant paths/authorities. **Correction to ticket:** refresh current root pointers only after subordinate branches are independently verified. DEVOPS-01's reviewed documentation-routing portion is closed with Operator-accepted qualifications (2026-10-17). Remaining dependency: GOVERNANCE-02; FUNC-01 is resolved by Corrective Ticket 02. **Gate:** link/path and status truth, no contradictory root-local trees. **State:** BLOCKED ON REMAINING NAMED SUBFOLDER ROUTING.

### GOVERNANCE_BRAINBOX/ [CRITICAL]

- **07. GOVERNANCE-01 [CRITICAL]** — Paths: `README_GOV_BRAINBOX.md`, `DOCUMENTATION_GOV_BRAINBOX.md`, `VERSIONING_GOV_BRAINBOX.md`. **Gap:** need explicit precedence among frozen V003 architecture, current Governance operating rules, root navigation, local domain READMEs, and historical authority bodies. **Correction to ticket:** define minimal universal precedence, with no premature hardcoding of unverified child paths. **Depends on:** no remaining legacy retirement; historical provenance was dispositioned in Ticket 02 and remains preserved in permanent records. **Gate:** no conflict with frozen Specification, Operator authority or source preservation. **State:** SELECTABLE / NOT FIXED.
- **08. GOVERNANCE-02 [HIGH]** — Paths: `REFERENCE_GOV_BRAINBOX.md` and Governance README. **Gap:** canonical read/write matrix across FUNC, DEVOPS, Skills, Portfolio, FootHive, Milestones and archives. **Correction to ticket:** finalize matrix **after** respective source-folder mapping. DEVOPS-01's reviewed documentation-routing portion is closed with Operator-accepted qualifications (2026-10-17), and DEVOPS-02 is resolved. Remaining dependency: selected source-folder mappings; FUNC-01/02 routing was resolved by Corrective Ticket 02, and current Skills/Milestones routing was reconciled by Corrective Ticket 03. **Gate:** exact verified destinations; never revive V002 paths. **State:** BLOCKED ON REMAINING SUBFOLDER ROUTING.
- **09. GOVERNANCE-03 [HIGH]** — Paths: `DOCUMENTATION_GOV_BRAINBOX.md`, `EVIDENCE_GOV_BRAINBOX.md`. **Gap:** lack of enforceable tool-output contamination safeguards. **Correction to ticket:** documented prevention and forensic preservation. **Depends on:** preserved Ticket 02 forensic evidence in permanent records. **Gate:** historical provenance unchanged until disposition. **State:** SELECTABLE / NOT FIXED.
- **10. GOVERNANCE-04 [MEDIUM]** — Paths: `TREE_AND_STATUS_GOV_BRAINBOX.md` and tooling references. **Gap:** automatic enforcement of two-level trees, physical paths, status vocabulary and relative links. **Correction to ticket:** scoped validation checks; do not populate planned branches. **Depends on:** stable subordinate README routes. **Gate:** reproducible checks and qualified limitations. **State:** SELECTABLE / NOT FIXED.

### Cross-category dependency / proposed selection order

1. DEVOPS-01 is closed within its accepted documentation scope (2026-10-17). Any selected Portfolio source-route review remains separately selectable; FUNC-03/04 remain independently selectable. Skills/Milestones retirements and legacy FUNC/DOB/AI_MUST retirements are closed.
2. GOVERNANCE-01 can proceed independently; GOVERNANCE-02 canonical ownership matrix follows the remaining child mappings.
3. README-01 and README-03 root routes follow their named dependencies; resolved README-02 retirement routing is documented in the permanent Phase 03 records.
4. V003-STATUS-01/02 and GOVERNANCE-03/04 may proceed when their respective prerequisites are met; unrelated fixes remain selectable.

**Per-ticket execution rule:** Operator selects a category/file and authorizes planning; Codex implements only the named approved ticket; ChatGPT independently verifies; Operator accepts; Git staging/publication remains a separate approval gate. A blocking flag stops only directly dependent tickets, not unrelated work.


## Closure reference — Operator acceptance, 2026-10-16

The Legacy DOB/FQ/AI_MUST findings (LEGACY-01 qualified, LEGACY-02 resolved, LEGACY-03 qualified), old Skills Availability retirement, and historical V002 Milestones retirement are **CLOSED** and intentionally excluded from the active corrective register. Source integrity and qualifications are preserved in the Phase 03 Fixes Report, Migration Map, and Recycle Bin Retirement Ledger. Corrective Ticket 02 was published in PRs #51–52; Ticket 03 in PRs #53–55. This acceptance does not validate unproven Skills capabilities, implement the planned Router milestone, or close separate remaining Governance and FUNC issues.

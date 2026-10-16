# V003_UNRESOLVED_BRAINBOX

**Status:** ACTIVE — CATEGORIZED CORRECTIVE INTAKE (2026-10-16). Previous Specification §§8–18 item remains closed; newly documented findings await individually selected and authorized Codex tickets.

**Authority:** [V003 Specification](V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md), [Origin Conversation](V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md), [Phase 03 report](PHASE03_FIXES_BRAINBOX/V003_FIXES_REPORT_BRAINBOX.md), [Migration Map](../VERSION_HISTORY_BRAINBOX/V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md).

## Current pending or planned follow-ups

The previous Specification §§8–18 classification/navigation case was closed by Operator approval on 2026-10-16; its semantic-label verification boundary remains recorded in the Phase 03 report and Migration Map. New current corrective findings appear in the categorized intake section below.

## Future category-based corrective register — Operator-approved layout

New issues must be grouped by affected **folder / file authority**, not mixed together. Each category heading names its primary folder(s) and uses a severity tag: [CRITICAL], [HIGH], [MEDIUM], or [LOW]. Criticality is based on impact and dependency, not reading order alone.

Within each category, each separately traceable fix has its own severity tag and fields: **Fix ID**, **Exact affected paths**, **Defect/evidence**, **Required correction**, **Dependencies (IDs and affected categories)**, **Verification/acceptance gate**, **Owner**, and **State**. Dependencies spanning categories must be referenced both ways where relevant. A README fix requiring a Governance policy decision is blocked only on that specifically linked Governance decision; other fixes may proceed independently.

For example, future headings could read `### README_BRAINBOX.md / root navigation [CRITICAL]` and `### GOVERNANCE_BRAINBOX/ [MEDIUM]`; these labels are format illustrations **only**, not accepted issue rankings or active defects. Do not promote proposed Grok flags into active entries until their paths, evidence and severity are reviewed. Keep resolved cases in permanent reports rather than this active register.

## Clear-on-resolution rule

The 20-SHA M01-GIT-01/M21-GIT-01 case is **CLOSED ADMINISTRATIVELY** and therefore no longer appears as an active entry here. The full Operator declaration, supplied Grok research (including 20 SHA strings), evidence limits and speculative hypothesis are preserved in the permanent Phase 03 report and cross-referenced by the Migration Map. F03, F04, F05, F06, F09, F10, F12, F13, F14 and F16 approved/closed dispositions are also retained in permanent reports rather than carried as unresolved rows.

For each future resolved item: independently verify the closure condition, append a dated record to the permanent report, update canonical references, then delete its active entry from this file. DEVOPS-02 was removed under this rule after Ticket 01 final cleanup acceptance; the permanent evidence remains in the Phase 03 report, Migration Map and Retirement Ledger. Intentionally planned future capabilities remain until implemented or explicitly removed from the backlog by an Operator decision. Never erase historical reports or alter protected source files as part of backlog cleanup.
## Active categorized corrective findings — Operator-approved intake, 2026-10-16

**Scope:** This is the new, separately selected corrective-work backlog following closure of the former Specification §§8–18 classification case. The earlier case remains closed and is not reopened. Findings are not executed by adding them here. **State:** INTAKE / AWAITING PER-FILE TICKET SELECTION; verified symptoms are distinguished from proposed mitigations. The Operator selects each folder/file for a separately scoped Codex ticket, independent ChatGPT verification and acceptance. No blanket retirement or replacement is authorized.

**Execution-order rule:** Prioritize dependency completion over severity alone. Fix and verify *source subfolders and their authoritative navigation* first; only after those destinations and statuses are settled, finalize root README and Governance cross-references. The critical root/central layers may be drafted earlier but MUST NOT finalize pointers to uncertain or V002 source paths. Separate policy decisions that are true prerequisites can be authorized earlier; do not block unrelated fixes. Preserve historical bodies and frozen Specification without new source-specific authority.

### AI_BRAINBOX/FUNC_AI_BRAINBOX/ [HIGH]

- **FUNC-01 [HIGH]** — Paths: `AI_BRAINBOX/FUNC_AI_BRAINBOX/README_FUNC_AI_BRAINBOX.md`; `AI_AGENTS_CORE_FUNC_BRAINBOX/`; `AI_AGENTS_EXE_FUNC_BRAINBOX/`. **Finding:** The coexistence of legacy FUNC, CORE and EXE records may obscure the capability-of-record and execution-of-record. **Correction to ticket:** establish the exact current navigation and read/write ownership after per-file inspection. **Depends on:** evidence for related legacy FUNC records; final routing feeds README-01 and GOVERNANCE-02. **Gate:** accurate child paths and authority boundaries, no made-up capabilities. **State:** SELECTABLE / NOT FIXED.
- **FUNC-02 [HIGH]** — Paths: `AI_BRAINBOX/FUNC_AI_BRAINBOX/*_FUNC_BRAINBOX.md`, including the legacy `FUNC_WORKFLOW_BRAINBOX.md` and `FQ_MUST_README.md`. **Finding:** Older instructions or placeholders may be mistaken for current agent authorities. **Correction to ticket:** classify each source as current, historical or reference-only with non-destructive routing. **Depends on:** LEGACY-01 forensic preservation and any specific Governance precedence decision. **Gate:** no V002 instructions silently promoted. **State:** SELECTABLE / NOT FIXED.
- **FUNC-03 [MEDIUM]** — Paths: agent-specific CORE/EXE records. **Finding:** completeness and actual capabilities vary or are unverified. **Correction to ticket:** identify substantive versus stub/unverified documentation; do not fabricate capability proof. **Depends on:** FUNC-01. **Gate:** evidence-backed claims. **State:** SELECTABLE / NOT FIXED.

### AI_BRAINBOX/DEVOPS_AI_BRAINBOX/ [HIGH]

- **DEVOPS-01 [HIGH]** — Paths: `README_DEVOPS_AI_BRAINBOX.md`; `SANDBOX_DEVOPS_BRAINBOX/`; `PROD_DEVOPS_BRAINBOX/`; related `PORTFOLIO_BRAINBOX/`. **Finding:** POC, Sandbox, Production, Portfolio and historical evidence need unambiguous source routing. **Correction to ticket:** validate and reconcile current read/write ownership. **Depends on:** verified POC migration; final routes feed GOVERNANCE-02 and README-03. **Gate:** live destinations resolve, Production is not inferred from Sandbox. **State:** SELECTABLE / NOT FIXED.
- **DEVOPS-03 [MEDIUM]** — Paths: Sandbox/Production READMEs and placeholder-only operational branches. **Finding:** populated documentation may be misread as deployed/operational. **Correction to ticket:** apply existing status/proof tags truthfully. **Depends on:** existing Tree and Status Governance; no capability-population mandate. **Gate:** no unsupported operational readiness claims. **State:** SELECTABLE / NOT FIXED.

### Legacy authority files — DOB/FQ/AI_MUST [CRITICAL]

- **LEGACY-01 [CRITICAL]** — Exact paths: `DOB_MUST_README.md`; `AI_BRAINBOX/AI_MUST_README.md`; `AI_BRAINBOX/FUNC_AI_BRAINBOX/FQ_MUST_README.md`. **Confirmed defect:** RDC output markers (`[Reading ...]`, `[executed on device: ...]`) were found in all three on 2026-10-16. **Correction to ticket:** first trace Git origin, preserve hashes, compare prior baselines; propose a bounded cleanup only after explicit approval. **Depends on:** none for read-only forensics. **Gate:** provenance, scope, byte-preservation and non-destructive disposition. **State:** CONFIRMED / FORENSICS NOT YET EXECUTED.
- **LEGACY-02 [CRITICAL]** — Same paths. **Confirmed risk:** historical reading-order/tree and authority claims remain inside routed legacy bodies. **Correction to ticket:** prevent active execution of superseded instructions while preserving historic material unless separately authorized. **Depends on:** LEGACY-01 and GOVERNANCE-01 authority precedence. **Gate:** current authority unmistakable without source loss. **State:** SELECTABLE / NOT FIXED.
- **LEGACY-03 [HIGH]** — Same paths. **Finding:** historical-byte-preservation claims require baseline reconciliation in the presence of embedded tool output. **Correction to ticket:** document exact provenance/exception, not presumptive attribution. **Depends on:** LEGACY-01. **Gate:** supported integrity conclusion. **State:** SELECTABLE / NOT FIXED.

### V003_VERSION_UPGRADE_BRAINBOX/ [HIGH]

- **V003-STATUS-01 [HIGH]** — Paths: `README_V003_VERSION_UPGRADE_BRAINBOX.md`; `PHASE02_MIGRATION_BRAINBOX/README_PHASE02_MIGRATION_BRAINBOX.md`; `V003_UNRESOLVED_BRAINBOX.md`. **Finding:** QUALIFIED CLOSED and historical M21/F02 pending checkpoints can be confused. **Correction to ticket:** provide concise dated present-state pointers while preserving prior checkpoint text. **Depends on:** already approved Operator dispositions; GOVERNANCE-01 if policy precedence needed. **Gate:** qualified closure never asserted as blanket technical PASS. **State:** SELECTABLE / NOT FIXED.
- **V003-STATUS-02 [MEDIUM]** — Paths: V003 status and historical reports. **Finding:** append-only superseded sections can obscure current reading. **Correction to ticket:** explicit checkpoint labeling/indexes; no deletion of evidence. **Depends on:** V003-STATUS-01. **Gate:** historical statuses remain traceable. **State:** SELECTABLE / NOT FIXED.

### README_BRAINBOX.md — root and navigation [CRITICAL]

- **README-01 [CRITICAL]** — Path: `README_BRAINBOX.md`. **Risk:** new agents may misread entry order or historical source references as active authority. **Correction to ticket:** final root entry/precedence routes to inspected canonical child READMEs. **Depends on:** FUNC-01, FUNC-02, DEVOPS-01 and GOVERNANCE-01 where it establishes necessary policy. **Gate:** current destination and reading order correct; root stays sole complete-tree authority. **State:** BLOCKED ON NAMED SUBFOLDER ROUTING.
- **README-02 [HIGH]** — Path: `README_BRAINBOX.md`. **Confirmed wording debt:** historical statements about retaining source files at original paths survive alongside current 88-file archive documentation. **Correction to ticket:** add explicit, dated supersession notices rather than rewriting historical migration narratives. **Dependency:** the DEVOPS-02 archive-routing dependency is satisfied by Ticket 01 final source removal and archive routing; see the permanent Phase 03 report. **Gate:** no active instruction sends agents to retired source; evidence preserved. **State:** SELECTABLE / NOT FIXED.
- **README-03 [HIGH]** — Path: root README and direct-child navigation. **Risk:** root full tree can become inconsistent with verified descendant paths/authorities. **Correction to ticket:** refresh current root pointers only after subordinate branches are independently verified. **Depends on:** FUNC-01, DEVOPS-01, GOVERNANCE-02. **Gate:** link/path and status truth, no contradictory root-local trees. **State:** BLOCKED ON NAMED SUBFOLDER ROUTING.

### GOVERNANCE_BRAINBOX/ [CRITICAL]

- **GOVERNANCE-01 [CRITICAL]** — Paths: `README_GOV_BRAINBOX.md`, `DOCUMENTATION_GOV_BRAINBOX.md`, `VERSIONING_GOV_BRAINBOX.md`. **Gap:** need explicit precedence among frozen V003 architecture, current Governance operating rules, root navigation, local domain READMEs, and historical authority bodies. **Correction to ticket:** define minimal universal precedence, with no premature hardcoding of unverified child paths. **Depends on:** LEGACY-01 for any invasive historical-file correction; general policy can be decided independently. **Gate:** no conflict with frozen Specification, Operator authority or source preservation. **State:** SELECTABLE / NOT FIXED.
- **GOVERNANCE-02 [HIGH]** — Paths: `REFERENCE_GOV_BRAINBOX.md` and Governance README. **Gap:** canonical read/write matrix across FUNC, DEVOPS, Skills, Portfolio, FootHive, Milestones and archives. **Correction to ticket:** finalize matrix **after** respective source-folder mapping. **Depends on:** FUNC-01/02, DEVOPS-01/02 and any selected Skills/Milestone audit. **Gate:** exact verified destinations; never revive V002 paths. **State:** BLOCKED ON SUBFOLDER ROUTING.
- **GOVERNANCE-03 [HIGH]** — Paths: `DOCUMENTATION_GOV_BRAINBOX.md`, `EVIDENCE_GOV_BRAINBOX.md`. **Gap:** lack of enforceable tool-output contamination safeguards. **Correction to ticket:** documented prevention and forensic preservation. **Depends on:** LEGACY-01 evidence. **Gate:** historical provenance unchanged until disposition. **State:** SELECTABLE / NOT FIXED.
- **GOVERNANCE-04 [MEDIUM]** — Paths: `TREE_AND_STATUS_GOV_BRAINBOX.md` and tooling references. **Gap:** automatic enforcement of two-level trees, physical paths, status vocabulary and relative links. **Correction to ticket:** scoped validation checks; do not populate planned branches. **Depends on:** stable subordinate README routes. **Gate:** reproducible checks and qualified limitations. **State:** SELECTABLE / NOT FIXED.

### Lower-risk categories — retain for later separate selection

- **SKILLS_AI_BRAINBOX/ [MEDIUM]** — Validate current taxonomy versus `SKILLS_AVAIL_AI_BRAINBOX/` historical reference, and avoid treating placeholder/readme-only content as proven skills. Feeds GOVERNANCE-02.
- **MILESTONES_BRAINBOX/ [LOW]** — Verify historical V002 checkpoint and planned Router/Agentic milestone remain separately identified in one canonical folder; old `MILESTONES/` physical path was retired. Feeds GOVERNANCE-02 if selected. Do not undo the verified relocation.

### Cross-category dependency / proposed selection order

1. LEGACY-01 forensic evidence (read-only; no automatic cleanup), plus minimal GOVERNANCE-01 precedence decision if independently needed.
2. FUNC-01 and FUNC-02, then DEVOPS-01/02; optionally Skills/Milestones/Portfolio when their destinations affect selected routes.
3. LEGACY-02/03 once forensic preservation and precedence are settled.
4. GOVERNANCE-02 canonical ownership matrix **after** child mappings.
5. README-01/02/03 root routes **after** their named dependencies.
6. V003-STATUS-01/02 and GOVERNANCE-03/04 when their respective prerequisites are met; independent fixes may proceed earlier.

**Per-ticket execution rule:** Operator selects a category/file and authorizes planning; Codex implements only the named approved ticket; ChatGPT independently verifies; Operator accepts; Git staging/publication remains a separate approval gate. A blocking flag stops only directly dependent tickets, not unrelated work.

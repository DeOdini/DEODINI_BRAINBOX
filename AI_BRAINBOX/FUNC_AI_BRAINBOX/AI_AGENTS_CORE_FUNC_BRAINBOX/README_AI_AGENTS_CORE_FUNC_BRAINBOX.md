# README_AI_AGENTS_CORE_FUNC_BRAINBOX.md

**PARENT:** AI_BRAINBOX/FUNC_AI_BRAINBOX/AI_AGENTS_CORE_FUNC_BRAINBOX/
**CURRENT DOMAIN:** Eight named AI agents' capability, integration, access-state and limitation records.
**PURPOSE:** Tell each AI agent how to inspect and maintain its own evidence-scoped capability inventory and how to reference—without duplicating—actual operations in EXE.
**MENTAL MODEL:** Exposure is not installation or configuration; configuration is not connection; connection is not authentication; authentication is not execution; execution is not authorization.
**GOVERNED BY:** Current Documentation, Naming, Reference, Evidence, Ticketing, Tree/Status, Security, Versioning and Promotion Governance; frozen V003 Specification §9; M05/M06 historical decisions.
**CANONICAL SOURCES:** Each agent's current CORE record for its source-attributed capability inventory; primary source reports for underlying historical claims; V003 Specification §9 for the approved DeepSeek/Qwen role baseline; agent EXE for operation-specific execution records.
**STATUS:** [ACTIVE — POST-V003 GOVERNANCE-ALIGNED CORE ROUTING]
**LAST VERIFIED:** 2026-10-22 — capability-refresh instructions, local links and structure reviewed; no live agent/tool capability was retested.
**APPLIES TO:** ChatGPT, Claude, Cline, Codex, Copilot, DeepSeek, Grok and Qwen.
**AUTHORIZATION BOUNDARY:** This README does not grant tool access, live testing, credential use, modification, external action or Git publication authority.

## 1. CORE domain responsibilities

### 1.1 CORE, EXE, and original evidence

| Destination | Canonical responsibility | What it does NOT establish |
|---|---|---|
| **Agent CORE record** | Named agent's source-backed declared tool/skill/integration inventory, access-state dimensions, limitations, last checks and references | Successful operation, universal current availability or standing permission |
| **Agent EXE record** | That named agent's exact attempted/executed operation, result, verification state and references to original execution evidence | General availability of every tool feature or ownership of original evidence artifacts |
| **Functional EXE index** | Short cross-agent discovery entry linking the relevant agent operation under BROWSER/FILE/MEDIA/CODE/RESEARCH | A second independent detailed execution record |
| **Original evidence source** | Historical capability reports, authenticated session observations, execution logs, original artifacts or separately governed records | Authority to rewrite its source or treat stale observations as current |

**Routing principle:** CORE explains what was exposed or declared for the agent and what conditions were observed. EXE explains which exact operations were attempted or executed, by whom and with what evidence. The functional EXE README references the agent EXE operation. Reference links do not transfer authority or ownership.

### 1.2 Agent record ownership

Every named agent maintains a **separate** CORE record within this directory. The agent's record covers that agent only. A Codex capability report does not prove ChatGPT or Copilot capability, and another agent's successful EXE operation is not transferable evidence.

The parent CORE README owns navigation, the locally established questionnaire and the mapping to the EXE domain. The eight agent CORE files retain their individual attributed historical and current observations. No new tool, account, skill, integration or verified state may be invented to complete a template.

### 1.3 Inventory versus operation

A CORE item can be exposed, installed, configured, connected or authenticated without ever having been exercised. Even when an actual operation is evidenced, its detailed attempt/result belongs in the executing agent's EXE record. CORE may summarize the precise bounded fact and link to the corresponding operation, but does not reproduce the full EXE questionnaire or logs.

## Canonical local tree — two descendant levels

This is the current physical structure, not a statement that every agent has working access. Structural tags follow [Tree and Status Governance](../../../GOVERNANCE_BRAINBOX/TREE_AND_STATUS_GOV_BRAINBOX.md).

```text
AI_AGENTS_CORE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
├── CHATGPT_CORE_FUNC_BRAINBOX.md [PRESENT]
├── CLAUDE_CORE_FUNC_BRAINBOX.md [PRESENT]
├── CLINE_CORE_FUNC_BRAINBOX.md [PRESENT]
├── CODEX_CORE_FUNC_BRAINBOX.md [PRESENT]
├── COPILOT_CORE_FUNC_BRAINBOX.md [PRESENT]
├── DEEPSEEK_CORE_FUNC_BRAINBOX.md [PRESENT]
├── GROK_CORE_FUNC_BRAINBOX.md [PRESENT]
├── QWEN_CORE_FUNC_BRAINBOX.md [PRESENT]
└── README_AI_AGENTS_CORE_FUNC_BRAINBOX.md [PRESENT]
```

Consult the actual destination before selecting a path. The root README alone owns the full project tree. For an operation, follow the [EXE parent README](../AI_AGENTS_EXE_FUNC_BRAINBOX/README_AI_AGENTS_EXE_FUNC_BRAINBOX.md).

## 3. Mandatory navigation and decision sequence for an arriving agent

**STEP 01 — Identify agent, runtime and requested scope.** Establish which named agent is acting, the current interface/session/workspace, the Operator's task and allowed read/test/write/external actions. Do not treat mere tool visibility or this README as approval to test or modify anything.

**STEP 02 — Read your own agent CORE file.** Open the correct file from Section 9. Check dated CORE items, claimed tools, provider, linked skill/configuration, access state, known constraints, source attribution and freshness. Never infer access from an agent name, a folder's existence or another agent's record.

**STEP 03 — Compare with current direct observations where permitted.** Identify exactly what is exposed in the present session. If read-only observation is authorized, distinguish tool discovery from successful connection and from authentication. Do not probe credentials, launch actions, or alter external systems merely to raise a status. Record unknowns explicitly.

**STEP 04 — Assess each CORE item independently.** Use the status dimensions in Section 4, separately for every tool, integration, skill and relevant operation. An account/project/device-specific connection does not verify a different account, workspace, device or tool operation.

**STEP 05 — Follow CORE-to-EXE references when operation evidence exists.** For an evidenced exact action, check the named agent's EXE record and its functional category reference. Do not copy another agent's EXE result or promote configuration into execution. Preserve date, target, verification and limitations.

**STEP 06 — Prepare an authorized inventory update.** Apply the existing C01–C10 questionnaire (Section 5) using stable CORE item IDs. Include original evidence location and provenance. If updating is outside the task authorization, report a proposed correction instead of writing it.

**STEP 07 — Report missing or ambiguous ownership.** If a tool is not indexed or its source conflicts with CORE, investigate original evidence, approved architecture and applicable Governance. Treat unverified tools and absent links as findings to assess—not proof of execution or automatic permission to create folders.

**STEP 08 — Validate and report.** For authorized updates, inspect exact changed files, source attributions, dated states, links, physical tree, preserved history and limitations. Report whether each result was a live observation, a historical report, a tool-reported claim or independently reproduced evidence. Follow separate ticket and Git publication gates.

## 4. CORE state vocabulary and evidence boundaries

Each agent's CORE record uses the existing required fields independently:

| Field | Question for the specific tool/item |
|---|---|
| **EXPOSED** | Was the tool, API, plugin, connector or skill visibly available in the named runtime and on what date? |
| **CONNECTED** | Did the named integration respond to an appropriate permitted connectivity check? |
| **AUTHENTICATED** | Was an identity or authenticated scope actually established? Public read access or a displayed tool name is not proof. |
| **EXECUTABLE** | Is there evidence for an exact successfully attempted operation? Reference its AGENT EXE record, result and date rather than duplicating it. |
| **AUTHORIZED** | What specific Operator action/task authority existed at the stated time? Do not imply standing or future permission. |
| **LIMITATIONS** | What scope, permissions, uncertainty, errors, environmental limits and age apply? |
| **CANONICAL EXE REFERENCES** | Which agent operation and functional index directly support a bounded execution claim? Or explicitly state that no execution category has been established. |
| **LAST VERIFIED** | Who checked exactly which claim, in which session and when? Distinguish document/link validation from live tool checks. |

Use the established YES, NO, UNKNOWN / NOT VERIFIED or NOT APPLICABLE value **with a dated explanation and evidence**. These are claim-specific statuses, not blanket agent certificates.

For C03 discovery, distinguish exposed / installed / configured / connected / authenticated / offline / untested, without conflating those observations with the required fields above. Never mark an operation VERIFIED EXECUTED solely from a CORE YES or an agent's own success claim. Actual operation-level evidence and verification states are governed by the [EXE procedure](../AI_AGENTS_EXE_FUNC_BRAINBOX/README_AI_AGENTS_EXE_FUNC_BRAINBOX.md).

## 5. Universal CORE questionnaire — existing C01–C10

The established questionnaire is retained as the local scope of each agent's capability inventory. Answer in that agent's own CORE file, with dated stable CORE item IDs and cited evidence; do not invent capability details.

**C01 — Identity and source.** Exact agent identity, model if known, runtime, workspace, observation date and claim source.

**C02 — Available inventory.** For EVERY visible native tool, connector, MCP/API, plugin and skill: exact name, linkage, provider, purpose and advertised functions, with source qualification.

**C03 — State of each item.** Distinguish exposed, installed, configured, connected, authenticated, offline and untested. Record last direct observation and account/project/device scope.

**C04 — Skill dependencies.** Describe relevant dependencies and distinguish having skill documentation from authenticated tool connections or credentials.

**C05 — Device and resource boundaries.** Record observed RDC devices, local/remote files, Git, browser, terminal and other resource access and applicable limitations/permissions.

**C06 — Communications.** Identify email, calendar and other communications interfaces; distinguish read, draft and send capabilities, authenticated scope and required authorization.

**C07 — Automation.** Distinguish available/configured/connected/authenticated n8n, Activepieces or native automation interfaces, known triggers and limits. Never claim an automation workflow was tested without evidence.

**C08 — Professional-function potential.** Distinguish possible frontend, backend, data, research, media, design or DevOps tasks from proven execution; record constraints and unknowns.

**C09 — Potential integrations.** Identify additional prospective tools, how they might link and why useful; label them potential/unverified rather than current capabilities.

**C10 — Itemized CORE record.** One record/row per CORE ID, identifying tool and type, separate state dimensions, purpose, permissions, source, date/last check and precise agent EXE link if an actual operation record exists.

Do not disclose credentials or make external test changes merely to answer a questionnaire. An unknown item may remain unknown until a separately authorized and evidenced assessment.

### Capability refresh assessment and identifier reconciliation

This dated session procedure supplements C01–C10; it does not replace their questions, change the existing CORE state dimensions, or authorize a live test or canonical registration. Apply it when an authorized capability assessment is actually in scope. Record the agent, model when known, session/runtime, date, environment, account or resource scope, permission boundary, exact capability/operation assessed, evidence source and verifier status. Redact secrets and avoid unsupported freshness claims.

#### Session refresh sequence

1. Identify the authorized task and exact runtime/session being assessed.
2. Read the agent's complete current CORE record, relevant agent-owned EXE records, and the original evidence they cite.
3. Reconcile each observation by provider/tool identity, function, scope and evidence—not by display name, row position or numeric suffix alone. Compare it with existing CORE IDs, EXE operation IDs, historical evidence and any provisional proposals.
4. Assess EXPOSED, CONNECTED, AUTHENTICATED, EXECUTABLE, AUTHORIZED, LIMITATIONS, CANONICAL EXE REFERENCES and LAST VERIFIED independently. State which facts were observed now and which were carried forward.
5. Apply one dated refresh label from the table below to the assessment, with its evidence and scope. The label is an additional assessment layer; it does not replace CORE fields or EXE operation states.
6. Preserve prior entries and results. A later failure or lack of access does not erase an earlier success. Do not silently change history or claim a capability was retested when it was not.
7. Treat an unmatched observation as a proposal only. Verify that it is not already represented and that its identity is not ambiguous; do not assign or publish a canonical CORE ID under this procedure. Registration requires its own authorization.
8. If an operation was actually executed within separately authorized scope, link its evidence to the agent-owned EXE operation and applicable functional index. A CORE assessment alone never establishes EXE `VERIFIED EXECUTED`.

#### Dated refresh labels

| Label | Use only when | Does not establish |
|---|---|---|
| `LIVE VERIFIED` | A successful check of the exact stated capability in the identified current runtime is supported by evidence. Name whether it is agent self-observed, independently reproduced, or independently accepted; these are distinct review states. | EXE `VERIFIED EXECUTED`, broader capability, other environments, standing authorization, or independent acceptance unless separately evidenced. |
| `CARRIED FORWARD — NOT RETESTED` | An existing record is retained, but that capability was not retested in this session. | Current connectivity, authentication, executable access, or freshness. |
| `CURRENTLY UNAVAILABLE — CONFIRMED` | A sufficiently evidenced, specific check supports unavailability for the stated operation, runtime and scope. Record the observed boundary and source. | Universal or permanent unavailability outside that scope. |
| `RETEST REQUIRED` | Evidence is stale, ambiguous, contradictory, incomplete, or otherwise inadequate for the intended current claim. | A positive or negative current result. |
| `NEWLY DISCOVERED` | A capability was directly observed but has not yet been reconciled with or admitted to the canonical inventory. | Connection, authentication, execution, authorization, uniqueness, or canonical registration. |

#### Keep availability findings distinct

| Finding | Meaning and evidence boundary |
|---|---|
| **Unexposed** | The capability/interface was not visible in the inspected runtime or inventory. This is an observation about that surface, not proof that a provider service does not exist. |
| **Untested** | No scoped attempt was made. Keep the result unknown or `CARRIED FORWARD — NOT RETESTED`; do not infer success or failure. |
| **Disconnected** | An interface or connection is identified, but the observed session did not establish a connection. State the precise runtime and evidence; one failed connection alone does not prove confirmed unavailability. |
| **Failed** | A scoped attempt occurred and returned an error or unsuccessful result. Preserve the error/evidence and distinguish operation failure from service retirement or general unavailability. |
| **Currently unavailable — confirmed** | Use only when specific evidence supports that scoped conclusion, such as an authoritative status for the exact service/scope or a sufficiently diagnostic authorized check. State the evidence and limits. |
| **Retired** | Use when an authoritative source establishes that the service/capability was discontinued. Preserve the historical record and retirement source; do not present retirement as a current-session test. |

An absent catalog entry is not by itself proof of unavailability. Insufficient permissions do not prove that a service is unavailable. A failed operation may warrant `RETEST REQUIRED` unless the evidence supports the narrower confirmed-unavailability finding. Do not call a service retired without authoritative discontinuation evidence.

#### Identifier reconciliation example: provisional ChatGPT proposals

The archived October 20 and October 22 assessments contain provisional ChatGPT numbering proposals that assign different functions to the same ordinal IDs. For example, the October 20 proposal associates `CORE-CHATGPT-001` with text generation/documentation, `002` with RDC file inspection and `003` with GitHub repository inspection; the October 22 proposal associates `001` with GitHub discovery, `002` with remote-device discovery and `003` with remote-directory enumeration. These are documented here as a collision example, not as canonical records. See the [archived post-V003 conversation](../../../POST_V003_MODIFICATIONS_BRAINBOX/POST_V003_MOD_CONVO_BRAINBOX.md).

Resolve such a conflict by comparing the capability definition, evidence, source and scope against the live CORE/EXE records. Preserve both proposals as historical evidence, identify duplicates or distinct capabilities, and report unresolved identity conflicts. Do not select a proposal by date or number alone, and do not assign canonical ChatGPT IDs under this questionnaire change.

#### Worked outcomes

1. **Existing capability retested successfully:** An authorized agent repeats the same scoped repository-discovery function already present in its CORE record. Record the dated `LIVE VERIFIED` observation and evidence; if an operation ran, link its distinct EXE evidence. The CORE label alone does not set EXE to `VERIFIED EXECUTED`.
2. **Historical connector not retested:** An email connector appears in a cited older record but is not tested now. Retain the historical item as `CARRIED FORWARD — NOT RETESTED`; do not claim current connectivity.
3. **Connection attempt fails:** Record the runtime, attempted scope, exact result and evidence; preserve any earlier success. Use `RETEST REQUIRED` unless the evidence specifically supports `CURRENTLY UNAVAILABLE — CONFIRMED` for that scope.
4. **New interface appears:** Record the directly observed interface as `NEWLY DISCOVERED`, compare it against existing IDs and evidence, and keep connection/authentication/execution/authorization states separate. Do not register it or assign an ID without the required separate authorization.
5. **Operation is repeated:** Preserve the earlier EXE evidence and record the later attempt separately under the existing EXE record conventions, with its own date, runtime, target, outcome and evidence. Do not overwrite or renumber the earlier event.

#### Vocabulary and historical wording

The words `ACTIVE`, `VALID` and `CANCELED` are not adopted as refresh labels here. `ACTIVE` can be confused with a record's lifecycle, `VALID` does not identify the capability, scope or observation date, and `CANCELED` describes a stopped process rather than a capability state. Existing Governance lifecycle terms and EXE operation states retain their separate meanings; do not reuse them as a refresh assessment. Use the precise dated labels above while preserving any source's original wording as historical text. This document does not claim that the proposed labels originated in V002.

These instructions do not require every capability to be tested in each session, create new permissions, change the DRAFT status of the Universal Documentation Governance Framework, or authorize new folders, CORE registrations, connector testing or publication.

## 6. CORE-to-EXE mapping and historical M05/M06 boundary

The M05 CORE and M06 CORE↔EXE reconciliation were independently recorded **PASS** in the 2026-10-09 Batch B closeout. That historical acceptance remains intact and is **not** a declaration of all-current runtime capability.

| Historical M06 scope | Outcome and boundary |
|---|---|
| **Codex** | RESEARCH, BROWSER, FILE and CODE categories admitted for specified cited operations |
| **Copilot BROWSER** | Playwright configuration recorded; successful browser execution unverified |
| **Cline MEDIA** | Reserved candidate only; not admitted as successful execution |
| **ChatGPT, Claude, DeepSeek, Grok, Qwen** | No admitted M06 EXE category from that matrix |
| **MEDIA category** | Reserved / execution evidence pending in M06 |

M05 CORE verification concerned source identity and scoped capability records. M06 linked the admissible operation evidence to EXE. Historic exposure, M06 admission, current connection, independent execution verification and present Operator authority must remain distinct.

For future actual operations: the relevant agent EXE record owns the detailed action and result, the function-specific EXE README indexes the action, and CORE points to these without duplicating their detailed records. A new operation never silently changes an older M05/M06 claim.

## 7. Evidence attribution, change authorization and scope

The original historical agent reports remain primary provenance where applicable. DeepSeek/Qwen use the approved V003 Specification §9 role baseline where no retained FUNC source report was established. The eight agent CORE files should cite their real original sources rather than imply all agents have identical source histories.

For any proposed new CORE item, separate direct observation, dated source assertion, independently reproduced evidence and untested potential. Preserve provenance, tool/service version when known, account/workspace scope and limitations. When details are unavailable, state UNKNOWN; do not infer a positive capability.

Agents require the applicable Operator approval to execute external operations, update canonical records, add new items/directories, or publish changes. Current [Ticketing Governance](../../../GOVERNANCE_BRAINBOX/TICKETING_GOV_BRAINBOX.md) governs approval gates; [Evidence Governance](../../../GOVERNANCE_BRAINBOX/EVIDENCE_GOV_BRAINBOX.md) governs proof and attribution; [Security Governance](../../../GOVERNANCE_BRAINBOX/SECURITY_GOV_BRAINBOX.md) prevents credential disclosure. No CORE entry or inherited historical permission grants standing write, send, push, merge, deployment or production authority.

## 8. Local validation and escalation

For a specifically authorized CORE documentation change:

1. Confirm the correct named agent and original claim source.
2. Inspect the current physical path and preserve any existing CORE IDs and evidence.
3. Confirm each status dimension and date has appropriate scoped support.
4. Confirm an EXE link really belongs to that same agent and exact operation.
5. Confirm no operation report or primary evidence was duplicated or silently overwritten.
6. Validate relative links, the canonical two-level local tree and source attribution.
7. Check changed-file scope, Markdown integrity and approved structural validator results.
8. Record limitations, outstanding questions, verifier and publication stage.

A validator PASS checks only the rules mechanically implemented; it does not prove every named capability is executable today. Escalate conflicting authorities through approved ticketing rather than inventing precedence. Documentation Governance's Universal Documentation Framework remains **DRAFT — NOT ADOPTED**, unless separately approved.

## 9. Agent CORE navigation

| Agent | Current agent CORE record |
|---|---|
| ChatGPT | [CHATGPT_CORE_FUNC_BRAINBOX.md](CHATGPT_CORE_FUNC_BRAINBOX.md) |
| Claude | [CLAUDE_CORE_FUNC_BRAINBOX.md](CLAUDE_CORE_FUNC_BRAINBOX.md) |
| Cline | [CLINE_CORE_FUNC_BRAINBOX.md](CLINE_CORE_FUNC_BRAINBOX.md) |
| Codex | [CODEX_CORE_FUNC_BRAINBOX.md](CODEX_CORE_FUNC_BRAINBOX.md) |
| Copilot | [COPILOT_CORE_FUNC_BRAINBOX.md](COPILOT_CORE_FUNC_BRAINBOX.md) |
| DeepSeek | [DEEPSEEK_CORE_FUNC_BRAINBOX.md](DEEPSEEK_CORE_FUNC_BRAINBOX.md) |
| Grok | [GROK_CORE_FUNC_BRAINBOX.md](GROK_CORE_FUNC_BRAINBOX.md) |
| Qwen | [QWEN_CORE_FUNC_BRAINBOX.md](QWEN_CORE_FUNC_BRAINBOX.md) |

The [FUNC parent](../README_FUNC_AI_BRAINBOX.md) provides wider domain navigation. The [EXE parent](../AI_AGENTS_EXE_FUNC_BRAINBOX/README_AI_AGENTS_EXE_FUNC_BRAINBOX.md) routes operation records and cross-agent functional indexes.

## 10. Canonical references

- [Frozen V003 Specification](../../../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md) — historical approved §9 agent architecture and DeepSeek/Qwen baseline.
- [V003 Origin Conversation](../../../V003_VERSION_UPGRADE_BRAINBOX/V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md) — decision history, not current execution authorization.
- [M05/M06 Phase 02 tickets](../../../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_PHASE02_MIGRATION_TICKETS_BRAINBOX.md) — historic CORE/EXE migration decisions and verification boundaries.
- [Governance README](../../../GOVERNANCE_BRAINBOX/README_GOV_BRAINBOX.md) — governing documents directory.
- [Documentation Governance](../../../GOVERNANCE_BRAINBOX/DOCUMENTATION_GOV_BRAINBOX.md) — README integrity, origin and rule placement; universal framework still draft.
- [Naming Governance](../../../GOVERNANCE_BRAINBOX/NAMING_GOV_BRAINBOX.md) — existing paths and naming conventions.
- [Reference Governance](../../../GOVERNANCE_BRAINBOX/REFERENCE_GOV_BRAINBOX.md) — ownership, links and nonduplicate canonical sources.
- [Evidence Governance](../../../GOVERNANCE_BRAINBOX/EVIDENCE_GOV_BRAINBOX.md) — evidence claims, limitations, verifier and source preservation.
- [Ticketing Governance](../../../GOVERNANCE_BRAINBOX/TICKETING_GOV_BRAINBOX.md) — scope and approval gates.
- [Tree and Status Governance](../../../GOVERNANCE_BRAINBOX/TREE_AND_STATUS_GOV_BRAINBOX.md) — navigation and physical/status separation.
- [Security Governance](../../../GOVERNANCE_BRAINBOX/SECURITY_GOV_BRAINBOX.md) — credential and sensitive-source boundaries.
- [Versioning Governance](../../../GOVERNANCE_BRAINBOX/VERSIONING_GOV_BRAINBOX.md) — Git and historical preservation.
- [Promotion Governance](../../../GOVERNANCE_BRAINBOX/PROMOTION_GOV_BRAINBOX.md) — readiness claims limited to proven scope.

## Modification summary — POST-V003-MOD-002 (2026-10-19)

**Earlier gap:** The former CORE README supplied required status fields and C01–C10 questions, but not an end-to-end navigation and maintenance path, an explicit CORE-versus-agent EXE-versus-functional EXE ownership table, or a clear rule against reusing another agent's evidence.

**Reason:** Arriving agents needed reliable guidance on discovering their own CORE items, classifying observed availability, tracing exact execution records, and distinguishing dated historical evidence from fresh authenticated access and new Operator authorization.

**Correction:** One current Governance-aligned CORE README now explains the ownership boundaries, eight-step agent sequence, independent item states, C01–C10, historic M05/M06 mapping, evidence/authorization limits, precise agent navigation and canonical references. The old presentation remains in Git history; the eight agent CORE records remain unchanged.

**Detailed modification record:** [POST-V003-MOD-002 report](../../../POST_V003_MODIFICATIONS_BRAINBOX/POST_V003_MOD_REPORT_BRAINBOX.md#post-v003-mod-002--core-readme-navigation-and-capability-inventory-clarification).

## Modification summary — POST-V003-FUNC-CAPREFRESH-001 (2026-10-22)

Added a dated capability-refresh assessment layer after the unchanged C01–C10 questionnaire. It defines evidence-scoped labels, availability distinctions, identifier reconciliation, provisional ChatGPT ID-conflict handling, five worked outcomes and the boundary between CORE assessment and EXE execution evidence. No agent capability was tested or registered, and no existing historical record was rewritten.

---

**END OF README_AI_AGENTS_CORE_FUNC_BRAINBOX.md**

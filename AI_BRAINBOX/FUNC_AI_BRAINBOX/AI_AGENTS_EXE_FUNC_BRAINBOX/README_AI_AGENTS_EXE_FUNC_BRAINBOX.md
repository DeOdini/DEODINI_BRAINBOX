# README_AI_AGENTS_EXE_FUNC_BRAINBOX

**PARENT:** `AI_BRAINBOX/FUNC_AI_BRAINBOX/AI_AGENTS_EXE_FUNC_BRAINBOX/`
**CURRENT DOMAIN:** Agent-specific executable operation records and cross-agent functional indexing
**PURPOSE:** Guide AI agents in discovering, recording, classifying and referencing evidenced execution operations under the correct agent and functional category.
**MENTAL MODEL:** CORE identifies declared capabilities; AGENT EXE records who executed an operation and its evidence; FUNCTION EXE provides cross-agent discovery of what functions were executed.
**GOVERNED BY:** Applicable canonical Governance rules; frozen V003 Specification §9; approved V003-M06 evidence classifications; subsequent Operator-approved EXE questionnaire and navigation decisions.
**CANONICAL SOURCE:** Agent EXE for agent-specific operation records; original authorized evidence locations for primary artifacts; frozen V003 Specification §9 and M06 for historical admission decisions.
**REFERENCED BY:** FUNC parent README, agent CORE records, agent EXE READMEs and functional EXE category READMEs.
**STATUS:** [ACTIVE — OPERATOR-APPROVED POST-V003 EXE ROUTING]
**LAST VERIFIED:** 2026-10-22 — refresh instructions, local links and structure reviewed; no live agent/tool operation was retested.
**APPLIES TO:** AI agents and authorized reviewers navigating, inspecting, recording or maintaining EXE operation information.
**SOURCE TYPE:** Local EXE navigation, operation-record ownership and functional-indexing guidance.
**AUTHORIZATION BOUNDARY:** This README does not independently authorize tool execution, repository modification, folder creation, external actions or Git publication.

---

## 1. EXE domain responsibilities and ownership

### 1.1 Three interconnected responsibilities

The EXE domain operates alongside the existing CORE registry and canonical Governance documents.

| Component | Primary responsibility | Question answered |
|---|---|---|
| **AGENT CORE** | Identifies declared agent tools, skills, configurations and capabilities | What does the agent report having access to or knowing? |
| **AGENT EXE** | Maintains the named agent's operation records, results, verification state and supporting evidence references | What exactly has this agent attempted or executed? |
| **FUNCTION EXE** | Indexes relevant operations across multiple agents by functional responsibility | Which agents have recorded operations in this category, and where are the details? |

These responsibilities are complementary, not interchangeable.

### 1.2 Agent-specific EXE folders

The following folders identify the agent to which operation records are attributed:

- `CHATGPT_EXE_FUNC_BRAINBOX/`
- `CLAUDE_EXE_FUNC_BRAINBOX/`
- `CLINE_EXE_FUNC_BRAINBOX/`
- `CODEX_EXE_FUNC_BRAINBOX/`
- `COPILOT_EXE_FUNC_BRAINBOX/`
- `DEEPSEEK_EXE_FUNC_BRAINBOX/`
- `GROK_EXE_FUNC_BRAINBOX/`
- `QWEN_EXE_FUNC_BRAINBOX/`

Each folder is the canonical location for the corresponding agent's operation records within the EXE domain.

An agent-specific record must identify the exact operation, executing agent, associated CORE capability, dated outcome, verification state, original supporting evidence and applicable authorization.

**Ownership boundary:** The AGENT EXE record owns the agent-operation description and evidence references. It does not automatically own, replace or relocate original logs, reports, artifacts or other primary evidence held in separately authorized domains.

One agent cannot inherit or claim another agent's execution evidence.

### 1.3 Function-specific EXE folders

The following folders index operations by functional responsibility:

- `BROWSER_EXE_FUNC_BRAINBOX/`
- `FILE_EXE_FUNC_BRAINBOX/`
- `MEDIA_EXE_FUNC_BRAINBOX/`
- `CODE_EXE_FUNC_BRAINBOX/`
- `RESEARCH_EXE_FUNC_BRAINBOX/`

Each functional README serves as a **cross-agent operation index**.

It identifies the relevant agent, operation, date, recorded state, meaningful limitation and direct reference to the agent-specific operation record.

A function-specific README must not become a second detailed execution ledger.

**Core ownership principle:**

**ONE AGENT OPERATION RECORD — REFERENCED BY THE RELEVANT FUNCTIONAL INDEX OR INDEXES.**

---

## Canonical local tree — two descendant levels

Current physical navigation snapshot. Structural classification follows [Tree and Status Governance](../../../GOVERNANCE_BRAINBOX/TREE_AND_STATUS_GOV_BRAINBOX.md).

```text
AI_AGENTS_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
├── BROWSER_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   └── README_BROWSER_EXE_FUNC_BRAINBOX.md [PRESENT]
├── CHATGPT_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   └── README_CHATGPT_EXE_FUNC_BRAINBOX.md [PRESENT]
├── CLAUDE_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   └── README_CLAUDE_EXE_FUNC_BRAINBOX.md [PRESENT]
├── CLINE_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   └── README_CLINE_EXE_FUNC_BRAINBOX.md [PRESENT]
├── CODE_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   └── README_CODE_EXE_FUNC_BRAINBOX.md [PRESENT]
├── CODEX_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   └── README_CODEX_EXE_FUNC_BRAINBOX.md [PRESENT]
├── COPILOT_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   └── README_COPILOT_EXE_FUNC_BRAINBOX.md [PRESENT]
├── DEEPSEEK_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   └── README_DEEPSEEK_EXE_FUNC_BRAINBOX.md [PRESENT]
├── FILE_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   └── README_FILE_EXE_FUNC_BRAINBOX.md [PRESENT]
├── GROK_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   └── README_GROK_EXE_FUNC_BRAINBOX.md [PRESENT]
├── MEDIA_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   └── README_MEDIA_EXE_FUNC_BRAINBOX.md [PRESENT]
├── QWEN_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   └── README_QWEN_EXE_FUNC_BRAINBOX.md [PRESENT]
├── RESEARCH_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   └── README_RESEARCH_EXE_FUNC_BRAINBOX.md [PRESENT]
└── README_AI_AGENTS_EXE_FUNC_BRAINBOX.md [PRESENT]
```

This tree identifies physical locations. It does not establish the operational readiness, verified execution or present authorization of any listed agent.

Consult the relevant child README for deeper navigation. The root `README_BRAINBOX.md` remains the complete project-tree authority.

---

## 3. Mandatory agent navigation and decision sequence

Every AI agent entering this directory must determine its current task and apply the following sequence within its authorized scope.

### STEP 01 — Identify the agent and task

Determine:

- The exact agent identity and current runtime.
- The task requested by the Operator.
- Whether the task is discovery, inspection, execution, verification, record preparation or authorized documentation maintenance.
- The relevant execution and modification permissions.

For a read-only inspection task, continue only with discovery and verification appropriate to that task. Do not interpret this procedure as permission to execute a tool.

### STEP 02 — Consult the relevant CORE record

Open the agent's CORE record in:

`../AI_AGENTS_CORE_FUNC_BRAINBOX/`

Identify the declared tool or capability and any existing CORE item identifiers.

Check whether the capability is recorded, merely configured, historically available or otherwise qualified.

**CORE describes capabilities and associated declarations. CORE does not prove successful execution.**

If the item is missing or inconsistent, report the finding. A CORE change requires applicable ticket-scoped authorization.

### STEP 03 — Consult the agent-specific EXE record

Navigate to the matching agent EXE README.

Inspect relevant existing operation records, identifiers, evidence references and current limitations.

Before proposing a new entry, determine whether the same operation is already documented.

Preserve established records and their identifiers. A subsequent execution attempt should be distinguished from an earlier attempt without silently replacing its history.

### STEP 04 — Determine the actual operation and its state

Identify what was attempted, rather than merely naming the tool.

For an authorized execution task, establish the actual result and preserve the appropriate evidence reference.

Apply the existing EXE operation-state vocabulary.

| Operation state | Meaning |
|---|---|
| VERIFIED EXECUTED | Successful named execution supported by required independent verification |
| EXECUTED PENDING VERIFICATION | Execution recorded; independent verification remains outstanding |
| HISTORICALLY EXECUTED | Earlier evidence supports execution; current capability is not revalidated by that evidence |
| PARTIAL | The attempt produced only part of the expected result |
| FAILED | The attempted operation did not achieve the required outcome |
| NOT TESTED | No execution attempt is established |
| UNAVAILABLE | Execution could not be attempted in the relevant environment |

Do not confuse these operation states with the physical or lifecycle tags governed by Tree and Status Governance.

**An operation's evidence state must not be generalized to all tools, functions, runtimes or future operations of that agent.**

### STEP 05 — Prepare or update the agent operation record

Where the task specifically authorizes documentation changes, create or update the appropriate agent-specific operation record using Section 4.

Where the task does not authorize documentation changes, report the proposed entry and its evidence for approval.

Identify the original evidence location instead of transferring or duplicating artifacts from unrelated authorities.

### STEP 06 — Identify the functional category

Determine which existing functional category describes the operation.

Use Section 5 and the appropriate category README to resolve ownership.

Check for an existing entry before proposing a new index reference.

Where an operation genuinely spans more than one function, it may be indexed by more than one category without duplicating its agent-owned operation record.

### STEP 07 — Synchronize authorized functional references

If an index update is specifically authorized:

1. Locate the corresponding category README.
2. Check whether the operation is already indexed.
3. Add or correct only the required summary and reference.
4. Use the agent's exact operation identifier.
5. Link directly to the agent operation heading where available.
6. Preserve the actual execution and verification state.
7. Verify that the reference resolves to the intended record.

Do not edit a category README simply because an operation has been performed. The update must fall within the current authorization.

### STEP 08 — Validate and report

For authorized changes:

- Check agent ownership.
- Check operation identifiers and references.
- Confirm links resolve.
- Confirm category summaries do not overstate evidence.
- Confirm existing records remain intact.
- Validate affected local trees and status representations.
- Report changed paths, validation results and remaining qualifications.

Follow applicable Governance and ticket-specific publication requirements for Git actions.

---

## 4. Agent operation-record contract — existing E01–E06 questionnaire

The existing universal V003 EXE questionnaire is retained.

It applies to operation evidence associated with tools or skills recorded in the relevant agent's CORE.

The operation's detailed record belongs in the relevant AGENT EXE folder, while original supporting artifacts remain with their existing authorized owners.

### E01 — Identity and capability reference

Identify the agent, runtime, date, relevant CORE item IDs and associated source links.

### E02 — Exact operation identification

For each relevant CORE item, identify the exact operation attempted.

Use a stable operation identifier consistent with existing records.

Example:

`EXE-CODEX-BROWSER-001`

A tool name alone is not an operation.

An unattempted operation remains NOT TESTED.

### E03 — Execution and evidence

Record the action, target, relevant inputs, expected outcome, actual outcome, result classification, execution date and original evidence location.

Identify the independent verifier and bounded verification result where available.

Do not manufacture evidence, outcomes or verification.

### E04 — Authentication and authorization

Identify the observed authentication state during execution, operation scope, potential read/write/external effects and applicable Operator authorization.

Do not include passwords, tokens or other secret values in the record.

### E05 — Reliability and freshness

Identify repeated attempts, relevant errors, observed reliability, last evidenced successful execution and any revalidation requirement.

Older success must remain distinguishable from current runtime availability.

### E06 — Functional category references

Identify the functional category or categories that index the operation.

Link to the relevant category index, using actual verified repository paths.

If no existing category adequately represents an evidenced operation, report the gap and propose a scoped addition under Section 8.

### Capability refresh and repeated-attempt relationship

The dated CORE refresh layer supplements the agent's existing C01–C10 inventory; it does not replace E01–E06 or this document's operation-state vocabulary. A CORE `LIVE VERIFIED` assessment records a successful scoped capability check. It does not itself establish that an operation meets EXE `VERIFIED EXECUTED`; operation evidence, verification and authorization remain governed here.

When the same logical operation is attempted again, preserve every earlier operation record and evidence. Make each new attempt distinguishable using the existing agent operation-record conventions and its actual date, runtime/environment, target and scope, outcome, evidence and verifier status. Keep stable, noncolliding operation identifiers. Where the operation corresponds to an existing CORE item, keep that CORE item reference and the agent-owned EXE reference consistent using the current record conventions; do not duplicate operation details. A later failure or scoped unavailability is a separate event and does not invalidate an earlier success.

Do not invent an attempt-ID format or overwrite an existing identifier to make repeated activity fit. If current records do not provide a clear, noncolliding way to represent a separate attempt and its relationship to the earlier event, stop and report the gap for scoped authorization. Functional indexes should link to the agent-owned operation records and must not duplicate their detailed evidence.

**Hypothetical example:** An agent's earlier browser operation has evidence of success. A later authorized attempt in another session fails. Retain the original successful record and evidence; record the later attempt separately under an existing noncolliding convention, with its actual error and scope. The later failure does not change the earlier outcome. Do not create either record from this example alone.

For the corresponding dated CORE assessment and its status boundaries, see [CORE capability refresh assessment and identifier reconciliation](../AI_AGENTS_CORE_FUNC_BRAINBOX/README_AI_AGENTS_CORE_FUNC_BRAINBOX.md#capability-refresh-assessment-and-identifier-reconciliation).

### Operation-record completeness

Every agent operation record should make its relevant E01–E06 information discoverable.

A compact record is acceptable when the fields remain sufficiently clear and the primary supporting evidence is traceable.

Preserve existing stable operation IDs and approved record formats. Do not create competing templates or rewrite historical operations solely for cosmetic consistency.

---

## 5. Functional classification and cross-agent indexing

### 5.1 Existing functional ownership

Classify operations by the action actually attempted or executed.

| Existing category | Functional responsibility |
|---|---|
| **BROWSER EXE** | Browser navigation, automation, interaction and browser-based verification |
| **FILE EXE** | File and directory inspection, creation, editing, transformation and management |
| **MEDIA EXE** | Image, audio, video and other media-related operations |
| **CODE EXE** | Coding, debugging, program execution and related implementation operations |
| **RESEARCH EXE** | Source discovery, research, retrieval and research synthesis |

These descriptions provide local routing guidance. Their presence does not certify that any named agent has executed the listed actions.

### 5.2 Required index relationship

A function-specific EXE README should identify each relevant operation through a concise cross-agent entry.

Recommended presentation:

| Agent | Operation ID | Exact function/tool | Evidence date | Operation state | Agent EXE reference |
|---|---|---|---|---|---|
| Agent name | Existing stable ID | Specific action | Evidenced date | Established state | Direct operation link |

A meaningful limitation should be included where the table alone could imply broader execution than the record supports.

### 5.3 Index ownership rules

- The functional index references the agent operation; it does not replace that operation record.
- The agent operation references its original evidence; it does not automatically replace the original artifact.
- The same operation may appear in multiple functional indexes when its actions justify multiple categories.
- The functional index must not combine several agents' operations into one shared verified capability.
- Failed, partial, historical and unverified operations must retain accurate classifications.
- Existing category evidence and historical M06 notes must not be silently rewritten to conform to new index formatting.

### 5.4 Multiple operations performed by one agent

An agent may have separately evidenced browser, file, code, research and media operations.

Each operation is identified within that agent's EXE records.

The respective function indexes then point to those records.

If a tool supports several distinct operations, classify each evidenced operation according to its actual function rather than assigning every potential tool function the same verified state.

---

## 6. Worked example — Codex browser execution and Playwright

This example uses the existing historical Codex browser operation. It does not assert a new Playwright execution.

### 6.1 Agent EXE location

[Codex EXE operation record](CODEX_EXE_FUNC_BRAINBOX/README_CODEX_EXE_FUNC_BRAINBOX.md#exe-codex-browser-001)

Existing operation ID:

`EXE-CODEX-BROWSER-001`

Historical context:

- **Agent:** Codex.
- **Operation:** FootHive local browser preview.
- **Tool context:** Playwright.
- **Historical evidence date:** 2026-10-03.
- **Recorded state:** HISTORICALLY EXECUTED.
- **Primary evidence:** Existing M06/T23 references.
- **Current-runtime qualification:** Historical evidence does not confirm a present Playwright connection or current execution permission.

The agent EXE record identifies Codex as the recorded executor and provides the detailed operation's traceability.

### 6.2 Function EXE location

[Browser EXE index](BROWSER_EXE_FUNC_BRAINBOX/README_BROWSER_EXE_FUNC_BRAINBOX.md)

The Browser category provides a short cross-agent reference to that exact Codex operation.

The category entry should identify Codex, the operation ID, the historical scope and the relevant evidence state.

The corresponding relative link from the Browser README to the agent operation is:

`../CODEX_EXE_FUNC_BRAINBOX/README_CODEX_EXE_FUNC_BRAINBOX.md#exe-codex-browser-001`

The link must still be checked against its actual destination during an authorized update.

### 6.3 Operational interpretation

The Browser category reference means that an evidenced historical Codex browser operation is discoverable through the browser function index.

It does **not** mean:

- Playwright is currently available.
- Codex currently has browser access.
- Copilot or another agent has successfully executed Playwright.
- Every Playwright operation has been tested.
- The Operator has authorized another browser execution.

Each agent requires its own operation evidence and applicable authorization.

### 6.4 Future Playwright operations

If a future authorized task involves Playwright:

1. Identify the executing agent and the exact attempted action.
2. Inspect the existing agent EXE record.
3. Record the new attempt according to the existing operation identity and historical-preservation rules.
4. Cite its actual evidence.
5. Determine its correct operation state.
6. If separately authorized, update the BROWSER index with a concise reference.

A future operation must not silently overwrite the historical M06 record or inherit its status.

---

## 7. Historical M06 admission register

The following existing M06 admission classifications remain historical evidence.

| Functional category | M06 admission state | Historical executor and evidence scope |
|---|---|---|
| RESEARCH | ADMITTED | Codex — public-source research, 2026-10-07 |
| BROWSER | ADMITTED | Codex — local FootHive preview, 2026-10-03 |
| FILE | ADMITTED | Codex — scoped repository file operations, P03–P05 |
| CODE | ADMITTED | Codex — FootHive CSS correction, T23 |
| MEDIA | RESERVED / EXECUTION EVIDENCE PENDING | No admitted M06 executor |

**Historical admission is not a standing declaration of current capability.**

The historical Copilot Playwright configuration is not independently established as successful end-to-end execution in the cited M06 record.

The existing M06 classifications must remain distinguishable from later operation records, new evidence and current-runtime verification.

This README does not retroactively expand admission to additional agents or functions.

---

## 8. Existing category discovery and proposed additions

### 8.1 Existing-category-first requirement

If an agent identifies an operation not yet represented by a functional index:

1. Inspect the existing BROWSER, FILE, MEDIA, CODE and RESEARCH categories.
2. Determine whether the operation fits an existing functional responsibility.
3. Inspect the relevant category README and existing operation references.
4. Identify whether the absence is a missing index entry, an incomplete agent record or a genuinely missing category.
5. Report the proposed destination and supporting evidence.

A new tool does not automatically require a new functional category.

For example, Playwright browser operations ordinarily belong in the existing BROWSER category.

### 8.2 New category proposal

When a genuinely distinct evidenced function is not covered by an existing category, the agent must present a proposal for Operator review.

The proposal must identify:

- The function and its purpose.
- The evidenced operations that justify it.
- Why existing categories are insufficient.
- The proposed name and location.
- Potential overlaps and duplicate ownership risks.
- Expected README and reference changes.
- Applicable Naming, Documentation, Reference and Tree/Status Governance.
- Required ticket scope and verification.

Do not create the category, subfolder or README before the applicable approval.

### 8.3 Missing agent-specific destinations

If an agent-specific EXE destination does not exist, report the missing destination against the approved architecture.

Do not create or rename an agent folder based solely on identity or an assumed future requirement.

Use the current physical structure and applicable Operator-approved paths.

### 8.4 Existing evidence preservation

New category proposals do not justify rewriting:

- Frozen V003 architecture.
- Original M06 admission evidence.
- Historical operation records.
- Retired source material.
- Independently verified test results.

Any required correction must follow the applicable authorized change process.

---

## 9. Verification, evidence integrity and change boundaries

### 9.1 Required local consistency checks

For an authorized EXE record or index change, confirm:

1. The named agent matches the operation attribution.
2. The CORE reference identifies the relevant declared capability.
3. The operation ID is stable and non-conflicting.
4. The operation state is supported by the cited evidence.
5. Original evidence can be traced to its authorized location.
6. The functional category matches the demonstrated operation.
7. The category points to the correct agent-specific operation.
8. Historical information and independent verification claims remain accurate.
9. Local trees and relative links match current repository structure.
10. Only authorized files and paths were modified.

Use the existing Governance structural validator where appropriate.

Its PASS result establishes only the mechanically checked facts. It does not independently verify historical execution claims or the meaning of every lifecycle classification.

### 9.2 Canonical Governance responsibilities

Apply the current Governance authorities directly rather than reproducing their complete rules here.

| Governance authority | Responsibility relevant to EXE |
|---|---|
| **Documentation Governance** | README purpose, content ownership, documentation integrity and authorship |
| **Naming Governance** | Approved file/folder names, path conventions and renaming discipline |
| **Reference Governance** | Canonical ownership, cross-domain links and prevention of duplicate sources |
| **Evidence Governance** | Proven versus reported execution, provenance, verification and evidence limits |
| **Ticketing Governance** | Scope, authorization, independent verification and approval gates |
| **Tree and Status Governance** | Physical navigation, two-level local trees and structural/lifecycle labels |
| **Security Governance** | Sensitive data, credentials and disclosure restrictions |
| **Versioning Governance** | Git lifecycle and repository-history preservation |
| **Promotion Governance** | Evidence-based promotion and readiness distinctions |

The Universal Documentation Governance Framework embedded in Documentation Governance remains **DRAFT — NOT ADOPTED** unless the Operator separately approves it.

Do not treat draft procedures as binding authority.

### 9.3 Execution and documentation authorization

The following are separate activities:

- Inspecting a capability record.
- Executing a tool.
- Recording an operation.
- Updating a functional index.
- Creating a directory.
- Performing independent verification.
- Staging, committing, pushing or merging changes.

Authorization for one activity does not automatically authorize another.

The applicable Operator decision and ticket define permitted execution and file-modification scope.

### 9.4 Reporting and escalation

If an EXE record is inconsistent, incomplete or unsupported:

- Identify the exact record and path.
- State the evidence observed.
- Distinguish missing information from a demonstrated defect.
- Identify the relevant canonical Governance authority.
- Report the needed correction or decision.
- Avoid making unauthorized changes.

Preserve prior results and provide dated corrective addenda where required.

Do not invent precedence between conflicting authorities. Escalate unresolved authority conflicts through the applicable Governance process.

---

## 10. Navigation and authoritative references

### 10.1 Agent-specific EXE and CORE navigation

| Agent | Agent EXE | Agent CORE |
|---|---|---|
| ChatGPT | [ChatGPT EXE](CHATGPT_EXE_FUNC_BRAINBOX/README_CHATGPT_EXE_FUNC_BRAINBOX.md) | [ChatGPT CORE](../AI_AGENTS_CORE_FUNC_BRAINBOX/CHATGPT_CORE_FUNC_BRAINBOX.md) |
| Claude | [Claude EXE](CLAUDE_EXE_FUNC_BRAINBOX/README_CLAUDE_EXE_FUNC_BRAINBOX.md) | [Claude CORE](../AI_AGENTS_CORE_FUNC_BRAINBOX/CLAUDE_CORE_FUNC_BRAINBOX.md) |
| Cline | [Cline EXE](CLINE_EXE_FUNC_BRAINBOX/README_CLINE_EXE_FUNC_BRAINBOX.md) | [Cline CORE](../AI_AGENTS_CORE_FUNC_BRAINBOX/CLINE_CORE_FUNC_BRAINBOX.md) |
| Codex | [Codex EXE](CODEX_EXE_FUNC_BRAINBOX/README_CODEX_EXE_FUNC_BRAINBOX.md) | [Codex CORE](../AI_AGENTS_CORE_FUNC_BRAINBOX/CODEX_CORE_FUNC_BRAINBOX.md) |
| Copilot | [Copilot EXE](COPILOT_EXE_FUNC_BRAINBOX/README_COPILOT_EXE_FUNC_BRAINBOX.md) | [Copilot CORE](../AI_AGENTS_CORE_FUNC_BRAINBOX/COPILOT_CORE_FUNC_BRAINBOX.md) |
| DeepSeek | [DeepSeek EXE](DEEPSEEK_EXE_FUNC_BRAINBOX/README_DEEPSEEK_EXE_FUNC_BRAINBOX.md) | [DeepSeek CORE](../AI_AGENTS_CORE_FUNC_BRAINBOX/DEEPSEEK_CORE_FUNC_BRAINBOX.md) |
| Grok | [Grok EXE](GROK_EXE_FUNC_BRAINBOX/README_GROK_EXE_FUNC_BRAINBOX.md) | [Grok CORE](../AI_AGENTS_CORE_FUNC_BRAINBOX/GROK_CORE_FUNC_BRAINBOX.md) |
| Qwen | [Qwen EXE](QWEN_EXE_FUNC_BRAINBOX/README_QWEN_EXE_FUNC_BRAINBOX.md) | [Qwen CORE](../AI_AGENTS_CORE_FUNC_BRAINBOX/QWEN_CORE_FUNC_BRAINBOX.md) |

### 10.2 Functional category navigation

| Category | Functional index | Purpose |
|---|---|---|
| BROWSER | [Browser EXE](BROWSER_EXE_FUNC_BRAINBOX/README_BROWSER_EXE_FUNC_BRAINBOX.md) | Discover recorded browser operations across agents |
| FILE | [File EXE](FILE_EXE_FUNC_BRAINBOX/README_FILE_EXE_FUNC_BRAINBOX.md) | Discover recorded file operations across agents |
| MEDIA | [Media EXE](MEDIA_EXE_FUNC_BRAINBOX/README_MEDIA_EXE_FUNC_BRAINBOX.md) | Discover media operations while preserving the historical M06 reserved state |
| CODE | [Code EXE](CODE_EXE_FUNC_BRAINBOX/README_CODE_EXE_FUNC_BRAINBOX.md) | Discover recorded coding and program-execution operations |
| RESEARCH | [Research EXE](RESEARCH_EXE_FUNC_BRAINBOX/README_RESEARCH_EXE_FUNC_BRAINBOX.md) | Discover recorded research operations |

### 10.3 Domain and historical authorities

- [FUNC parent README](../README_FUNC_AI_BRAINBOX.md) — FUNC domain navigation and CORE/EXE responsibilities.
- [CORE registry README](../AI_AGENTS_CORE_FUNC_BRAINBOX/README_AI_AGENTS_CORE_FUNC_BRAINBOX.md) — agent capability and CORE discovery.
- [Frozen V003 Specification](../../../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md) — approved V003 architecture and historical M06 boundaries.
- [V003 Origin Conversation](../../../V003_VERSION_UPGRADE_BRAINBOX/V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md) — historical decisions and provenance.
- [M06 ticket records](../../../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_PHASE02_MIGRATION_TICKETS_BRAINBOX.md) — historical EXE implementation scope and recorded admission evidence.

### 10.4 Current canonical Governance

- [Governance README](../../../GOVERNANCE_BRAINBOX/README_GOV_BRAINBOX.md) — current Governance domain index.
- [Documentation Governance](../../../GOVERNANCE_BRAINBOX/DOCUMENTATION_GOV_BRAINBOX.md) — documentation construction, authority and authorship.
- [Naming Governance](../../../GOVERNANCE_BRAINBOX/NAMING_GOV_BRAINBOX.md) — names and paths.
- [Reference Governance](../../../GOVERNANCE_BRAINBOX/REFERENCE_GOV_BRAINBOX.md) — source ownership and referencing.
- [Evidence Governance](../../../GOVERNANCE_BRAINBOX/EVIDENCE_GOV_BRAINBOX.md) — execution proof and evidence quality.
- [Ticketing Governance](../../../GOVERNANCE_BRAINBOX/TICKETING_GOV_BRAINBOX.md) — approvals, scope and verification.
- [Tree and Status Governance](../../../GOVERNANCE_BRAINBOX/TREE_AND_STATUS_GOV_BRAINBOX.md) — trees and status representations.
- [Security Governance](../../../GOVERNANCE_BRAINBOX/SECURITY_GOV_BRAINBOX.md) — sensitive information and disclosure.
- [Versioning Governance](../../../GOVERNANCE_BRAINBOX/VERSIONING_GOV_BRAINBOX.md) — Git and history.
- [Promotion Governance](../../../GOVERNANCE_BRAINBOX/PROMOTION_GOV_BRAINBOX.md) — evidenced readiness and promotion.

These references identify the current governing sources. They do not transfer their authority into this local README or authorize changes by themselves.

---

## Final operational instruction

**WHEN AN AI AGENT NEEDS TO DISCOVER OR RECORD EXECUTION:**

**FIRST:** Identify the agent, task, authority and relevant CORE capability.

**SECOND:** Inspect the agent's own EXE records and determine the exact operation and its evidenced state.

**THIRD:** Where authorized, maintain the detailed agent operation record with its original evidence references.

**FOURTH:** Identify the correct existing functional category and, where authorized, maintain its concise cross-agent index entry.

**FIFTH:** Verify ownership, evidence, links, status and change scope; report findings under applicable Governance.

**SIXTH:** Seek explicit approval for any new functional category, structural change or action outside the authorized scope.

### Permanent responsibility distinction

**CORE = WHAT THE AGENT DECLARES.**

**AGENT EXE = WHAT THAT AGENT ACTUALLY ATTEMPTED OR EXECUTED, WITH EVIDENCE.**

**FUNCTION EXE = WHERE OPERATIONS ARE INDEXED BY FUNCTION ACROSS AGENTS.**

**PRIMARY EVIDENCE = REMAINS WITH ITS AUTHORIZED SOURCE OWNER.**

**GOVERNANCE = CONTROLS SYSTEM-WIDE REQUIREMENTS.**

**OPERATOR = CONTROLS AUTHORIZATION.**

---

## Modification summary — POST-V003-MOD-001 (2026-10-19)

**Previous limitation:** The former README covered agent execution evidence and M06 categories but did not sufficiently explain the difference between agent-specific EXE operation records and functional BROWSER/FILE/MEDIA/CODE/RESEARCH indexes or give agents clear ordered routing instructions.

**Why modified:** Agents need unambiguous ownership for detailed operation records, original evidence, functional summaries, cross-references and authorization requirements.

**Resolution:** One consolidated Governance-aligned procedure now explains CORE, agent EXE, function EXE, E01–E06, historical M06 qualifications, evidence ownership and Operator-gated changes. Previous presentation is preserved in Git history.

**Full modification report:** [POST-V003-MOD-001 report](../../../POST_V003_MODIFICATIONS_BRAINBOX/POST_V003_MOD_REPORT_BRAINBOX.md#post-v003-mod-001--exe-readme-routing-and-functional-index-clarification).

## Modification summary — POST-V003-FUNC-CAPREFRESH-001 (2026-10-22)

Clarified how CORE refresh assessments relate to the unchanged E01–E06 operation procedure, how repeat attempts retain separate dated evidence under existing stable identifiers, and when an unclear identifier convention must be reported instead of invented. No live operation was retested and no operation record or functional index was changed.

---

**END OF README_AI_AGENTS_EXE_FUNC_BRAINBOX**

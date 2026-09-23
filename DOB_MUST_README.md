[Reading 168 lines from start (total: 168 lines, 0 remaining)]

[Reading 172 lines from start (total: 172 lines, 0 remaining)]

[Reading 166 lines from start (total: 166 lines, 0 remaining)]

# DOB_MUST_README.md

## DEODINI_BRAINBOX — Root Mandatory Entry Point

**Issued by:** De O'Dini (Operator)  
**Applies to:** All AI agents operating within the DEODINI_BRAINBOX environment

This document is the master entry point for the DEODINI_BRAINBOX hive. Read it before carrying out tasks, commands, or operations within the hive.

---

## Project Structure

```text
DEODINI_BRAINBOX/
├── AI_BRAINBOX/
│   ├── FUNC_AI_BRAINBOX/
│   │   ├── CHATGPT_FUNC_BRAINBOX.md
│   │   ├── CLAUDE_FUNC_BRAINBOX.md
│   │   ├── GROK_FUNC_BRAINBOX.md
│   │   ├── QWEN_FUNC_BRAINBOX.md
│   │   ├── DEEPSEEK_FUNC_BRAINBOX.md
│   │   ├── COPILOT_FUNC_BRAINBOX.md
│   │   ├── CLINE_FUNC_BRAINBOX.md
│   │   ├── FUNC_WORKFLOW_BRAINBOX.md
│   │   ├── FUNC_REQ_BRAINBOX.md
│   │   └── FQ_MUST_README.md
│   ├── PROJ_WORKFLOW_AI_BRAINBOX/
│   │   ├── RAW_WORKFLOW_PROJ_BRAINBOX.md
│   │   ├── PROVEN_PATTERN_PROJ_BRAINBOX.md
│   │   ├── FAILED_PATTERN_PROJ_BRAINBOX.md
│   │   └── PROJ_MUST_README.md
│   ├── SKILLS_AVAIL_AI_BRAINBOX/
│   │   ├── RAW_SKILLS_BRAINBOX.md
│   │   ├── PROVEN_SKILLS_BRAINBOX.md
│   │   ├── REUSABLE_SKILLS_BRAINBOX.md
│   │   ├── FAILED_SKILLS_BRAINBOX.md
│   │   └── SKILLS_MUST_README.md
│   └── AI_MUST_README.md
├── PORTFOLIO_BRAINBOX/
│   └── 001_PORT_BRAINBOX.md
└── DOB_MUST_README.md
```


## Site Map

```text
DEODINI_BRAINBOX/
├── DOB_MUST_README.md
├── AI_BRAINBOX/
│   ├── AI_MUST_README.md
│   ├── FUNC_AI_BRAINBOX/
│   │   ├── FQ_MUST_README.md
│   │   ├── FUNC_REQ_BRAINBOX.md
│   │   ├── FUNC_WORKFLOW_BRAINBOX.md
│   │   └── *_FUNC_BRAINBOX.md
│   ├── PROJ_WORKFLOW_AI_BRAINBOX/
│   │   ├── PROJ_MUST_README.md
│   │   ├── RAW_WORKFLOW_PROJ_BRAINBOX.md
│   │   ├── PROVEN_PATTERN_PROJ_BRAINBOX.md
│   │   └── FAILED_PATTERN_PROJ_BRAINBOX.md
│   └── SKILLS_AVAIL_AI_BRAINBOX/
│       ├── SKILLS_MUST_README.md
│       ├── RAW_SKILLS_BRAINBOX.md
│       ├── PROVEN_SKILLS_BRAINBOX.md
│       ├── REUSABLE_SKILLS_BRAINBOX.md
│       └── FAILED_SKILLS_BRAINBOX.md
└── PORTFOLIO_BRAINBOX/
    └── 001_PORT_BRAINBOX.md
```


## Mandatory Top-Level Reading Order

Agents must follow this order:

1. **DOB_MUST_README.md** — read this root master document first.
2. **AI_BRAINBOX/AI_MUST_README.md** — enter the AI subsystem and follow its instructions.
3. **AI_BRAINBOX/FUNC_AI_BRAINBOX/FQ_MUST_README.md** — read the function-area compliance instructions.
4. **AI_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_WORKFLOW_BRAINBOX.md** — read the workflow before function requirements.
5. **AI_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_REQ_BRAINBOX.md** — read the current function requirements.
6. **Other FUNC_AI_BRAINBOX contents** — review the remaining files in **AI_BRAINBOX/FUNC_AI_BRAINBOX/** as relevant, especially the other agent-specific capability files, so documented capabilities can be understood and reused across agents.
7. **AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/PROJ_MUST_README.md** — follow the project-workflow subsystem instructions.
8. **AI_BRAINBOX/SKILLS_AVAIL_AI_BRAINBOX/SKILLS_MUST_README.md** — follow the skills subsystem instructions.
9. **The applicable agent-specific function file** within **AI_BRAINBOX/FUNC_AI_BRAINBOX/**, if it was not already covered in Step 6.



---

## Master Rules

- **Nothing is discarded:** preserve successful and failed workflows, patterns, and skills as institutional memory.
- **Proven means tested:** do not describe a method as proven until it has been tested in practice.
- **Reusability:** preserve methods that can be reliably repeated or adapted.
- **Innovation:** new approaches may be tested, documented, and promoted when evidence supports them.
- **Naming and navigation:** use the established DEODINI_BRAINBOX naming convention consistently.
- **Mandatory reading:** each subsystem's README must direct agents to the authoritative information relevant to that subsystem.
- **Master-copy principle:** this document is the root authority for general DEODINI_BRAINBOX rules. Subsystem readmes should reference the relevant sections here rather than create competing copies of those rules.

---

## Change Request Governance

The following pattern applies to any AI agent instructed to create, modify, or execute a change request within the DEODINI_BRAINBOX environment.

### Constant Rule

The following README authorities are constant within their stated scope and may be changed only when an AI agent is specifically and explicitly instructed to change them:

1. **Root / hive-wide authority:** `DOB_MUST_README.md`
2. **AI subsystem authority:** `AI_BRAINBOX/AI_MUST_README.md`
3. **Function-area compliance checkpoint:** `AI_BRAINBOX/FUNC_AI_BRAINBOX/FQ_MUST_README.md`
4. **Project-workflow subsystem authority:** `AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/PROJ_MUST_README.md`
5. **Skills subsystem authority:** `AI_BRAINBOX/SKILLS_AVAIL_AI_BRAINBOX/SKILLS_MUST_README.md`

Absent explicit instruction, each remains intact and unmodified within its scope.

### Variable Elements

The following may vary per request:

- The number of requests.
- The names of target request files (e.g., `FUNC_REQ_BRAINBOX.md`).
- The folder path (e.g., `FUNC_AI_BRAINBOX/`).
- The names of agent-specific output files.
- The naming of each request header.

Standing Instruction Pattern for function-area change requests is maintained in `AI_BRAINBOX/FUNC_AI_BRAINBOX/FQ_MUST_README.md` (between Step 4 and Step 5 of the mandatory reading order).

### Canonical Example

> I want to create a `FUNC_REQ_BRAINBOX.md` file within the `FUNC_AI_BRAINBOX` folder.
> An AI agent is to execute this and create the file.
> Both entire function requests should be included within `FUNC_REQ_BRAINBOX.md`, naming each request’s header according to what the request was about.
> The AI agent should also create a `FQ_MUST_README.md`. Within it, the agent should cite `FUNC_REQ_BRAINBOX.md` as a mandatory read for all AI agents before carrying out, executing, or performing any tasks, commands, or operations given to them. After which, once an AI agent has read `FUNC_REQ_BRAINBOX.md`, they should follow up with the other folders, files, and documents listed within.

### Adaptation Rule

- Numbers, folder names, and file names in the canonical example are illustrative and may vary per request.
- Request header naming may vary per subject.
- `AI_BRAINBOX/FUNC_AI_BRAINBOX/FQ_MUST_README.md` remains the function-area compliance checkpoint and may be changed **only** if explicitly instructed.

---

## Revision Notes

When an AI agent performs approved fixes or structural changes within DEODINI_BRAINBOX, it must leave a short revision note that includes:
- what changed (brief)
- agent name
- timestamp
- the line: **Signed & Authorized by: DE O'DINI (OPERATOR)**

Root revision history for hive-wide / cross-file governance changes is recorded in this document.

### 2026-09-20

Updated Sections 2.2, 6 (step 1), 3 (Principle 8), 2.7, 13, and 11 of `FUNC_WORKFLOW_BRAINBOX.md` to (a) clarify that free/spec projects based on real Upwork briefs are unpaid trial builds, never misrepresented as paid engagements, (b) add a standing disclosure rule for portfolio entries, and (c) clarify email-trigger content boundaries and Brainbox scope, per operator instruction.

**Agent:** De O'Dini (Operator)  
**Timestamp:** 2026-09-20  
**Signed & Authorized by: DE O'DINI (OPERATOR)**

---

## Reference-Link Pattern

When a subsystem README references rules maintained here, the return-link details are hosted here in this root document. Each entry identifies the originating subsystem README by full relative path and anchor.

- [FQ_MUST_README.md](AI_BRAINBOX/FUNC_AI_BRAINBOX/FQ_MUST_README.md#mandatory-reading-and-compliance-notice)
  - Return here only if you arrived from this subsystem README.
- [AI_MUST_README.md](AI_BRAINBOX/AI_MUST_README.md#ai_brainbox-entry-point)
  - Return here only if you arrived from this subsystem README.
- [PROJ_MUST_README.md](AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/PROJ_MUST_README.md#project-workflow-subsystem)
  - Return here only if you arrived from this subsystem README.
- [SKILLS_MUST_README.md](AI_BRAINBOX/SKILLS_AVAIL_AI_BRAINBOX/SKILLS_MUST_README.md#skills-availability-subsystem)
  - Return here only if you arrived from this subsystem README.

Each subsystem README keeps its root-authority link and its note that the referenced material may be ignored if it was already read through `DOB_MUST_README.md`. No subsystem README should contain a self-referential return link.

---

**End of DOB_MUST_README.md**

[executed on device: DESKTOP-DHRIH27 (4836c4e3-c473-4ea0-b084-482f4637ff78)]

[executed on device: DESKTOP-DHRIH27 (4836c4e3-c473-4ea0-b084-482f4637ff78)]

[executed on device: DESKTOP-DHRIH27 (4836c4e3-c473-4ea0-b084-482f4637ff78)]
# FQ_MUST_README.md

## MANDATORY READING AND COMPLIANCE NOTICE

**Issued by:** De O'Dini (Operator)
**Applies to:** All AI Agents operating within the BRAINBOX environment

All AI agents must read this file before carrying out any tasks, commands, or operations within the BRAINBOX environment.

---

## 1. Mandatory Reading Order

Every AI agent must follow this reading order **before executing any task, command, or operation**:

### Step 1 — Read the Workflow Document

First, read:

**`BRAINBOX/WORKFLOW_BRAINBOX.md`**

This document explains **what is being done and why**. It establishes the overall purpose, the agent hierarchy, the automation layers (n8n and email), the human-in-the-loop model, and the documentation standards. It is read first because understanding the workflow is the foundation for everything else.

### Step 2 — Read the Function Requirements Document

Next, read:

**`BRAINBOX/FUNC_REQ_BRAINBOX.md`**

This document contains the complete and authoritative function requests that define reporting, capability disclosure, and file submission requirements for all AI agents.

### Step 3 — Confirm Your Function Requirements Are Up to Date

After reading `FUNC_REQ_BRAINBOX.md`, determine whether your own capability and report file (e.g., `CHATGPT_BRAINBOX.md`, `CLAUDE_BRAINBOX.md`, `GROK_BRAINBOX.md`, `DEEPSEEK_BRAINBOX.md`, `QWEN_BRAINBOX.md`, `CLINE_BRAINBOX.md`, `COPILOT_BRAINBOX.md`) is up to date against the current requirements.

### Step 4 — Read the Remaining Brainbox Folders and Files

**Regardless** of whether your file is up to date or not, proceed to read the other folders, files, and documents within the Brainbox. Follow up on any references contained within them, in the order and manner specified.

### Step 5 — Leave an Update Note if Required

If your function requirements file is **not up to date**, leave a note to the Operator requesting an update. The note must be delivered:

- **First choice:** as a chat message, if the channel permits.
- **Fallback:** by email, if a chat message is not possible.

The note must clearly state:
- The agent name
- The file that requires updating
- What is missing or out of date
- The recommended change

---

## 2. Enforcement

- Non-compliance with the mandatory reading order is strictly prohibited.
- No task, command, or operation may be executed until Steps 1 through 4 have been completed.
- This README is the primary compliance checkpoint for all AI agents.

---

## 3. Acknowledgment

By proceeding with any operation within BRAINBOX, you acknowledge that you have read, understood, and agreed to comply with the requirements outlined in `WORKFLOW_BRAINBOX.md`, `FUNC_REQ_BRAINBOX.md`, and this README.

---

## 4. Retained Change Request Pattern (Reusable Template for Any AI Agent)

The following pattern is retained as a standing instruction for any AI agent instructed to create, modify, or execute a change request within the BRAINBOX environment.

### 4.1 Constant Rule

The only constant across all change requests is this file:

**`BRAINBOX/FQ_MUST_README.md`**

This file may only be changed if an AI agent is specifically and explicitly instructed to change it. Absent such instruction, it must remain intact and unmodified.

### 4.2 Variable Elements

The following may vary per request:

- The number of requests.
- The names of target request files (e.g., `FUNC_REQ_BRAINBOX.md`).
- The folder path (e.g., `BRAINBOX/`).
- The names of agent-specific output files.
- The naming of each request header.

### 4.3 Standing Instruction Pattern

When instructed to make any sort of change, an AI agent must:

1. **Designate a request file.** Create the request file within the designated folder, including each request under a header that reflects its subject.
2. **Compile all requests.** Ensure all requests are contained and clearly separated.
3. **Create or update the compliance file.** Cite the request file as a **mandatory read** for all AI agents before execution.
4. **Enforce the follow-up chain.** After reading the request file, agents must follow up with the folders, files, and documents listed within it.
5. **Preserve the constant.** `FQ_MUST_README.md` must remain the single constant file, changed only on explicit instruction.

### 4.4 Canonical Example (Retained from Prior Accepted Request)

> I want to create a `FUNC_REQ_BRAINBOX.md` file within the `BRAINBOX` folder.
> An AI agent is to execute this and create the file.
> Both entire function requests should be included within `FUNC_REQ_BRAINBOX.md`, naming each request’s header according to what the request was about.
> The AI agent should also create a `FQ_MUST_README.md`. Within it, the agent should cite `FUNC_REQ_BRAINBOX.md` as a mandatory read for all AI agents before carrying out, executing, or performing any tasks, commands, or operations given to them. After which, once an AI agent has read `FUNC_REQ_BRAINBOX.md`, they should follow up with the other folders, files, and documents listed within.

### 4.5 Adaptation Rule

- Numbers, folder names, and file names in Section 4.4 are illustrative and may vary per request.
- Request header naming may vary per subject.
- `FQ_MUST_README.md` is the only constant and may be changed **only** if explicitly instructed.

---

**End of FQ_MUST_README.md**
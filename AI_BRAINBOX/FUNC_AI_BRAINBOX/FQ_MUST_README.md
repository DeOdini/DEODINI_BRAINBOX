# FQ_MUST_README.md

## MANDATORY READING AND COMPLIANCE NOTICE

**Issued by:** De O'Dini (Operator)
**Applies to:** All AI Agents operating within the DEODINI_BRAINBOX environment

> **Root authority:** [DOB_MUST_README.md](../../DOB_MUST_README.md#mandatory-top-level-reading-order)
>
> If this section was already read through `DOB_MUST_README.md`, it may be ignored.

All AI agents must read this file before carrying out any tasks, commands, or operations within the DEODINI_BRAINBOX environment.

---

## 1. Mandatory Reading Order

Every AI agent must follow this reading order **before executing any task, command, or operation**:

### Step 1 — Read the Workflow Document

First, read:

**`FUNC_WORKFLOW_BRAINBOX.md`**

This document explains **what is being done and why**. It establishes the overall purpose, the agent hierarchy, the automation layers (n8n and email), the human-in-the-loop model, and the documentation standards. It is read first because understanding the workflow is the foundation for everything else.

### Step 2 — Read the Function Requirements Document

Next, read:

**`FUNC_REQ_BRAINBOX.md`**

This document contains the complete and authoritative function requests that define reporting, capability disclosure, and file submission requirements for all AI agents.

### Step 3 — Confirm Your Function Requirements Are Up to Date

After reading `FUNC_REQ_BRAINBOX.md`, determine whether your own capability and report file (e.g., `CHATGPT_FUNC_BRAINBOX.md`, `CLAUDE_FUNC_BRAINBOX.md`, `GROK_FUNC_BRAINBOX.md`, `DEEPSEEK_FUNC_BRAINBOX.md`, `QWEN_FUNC_BRAINBOX.md`, `CLINE_FUNC_BRAINBOX.md`, `COPILOT_FUNC_BRAINBOX.md`) is up to date against the current requirements.

### Step 4 — Confirm the Applicable Function-Area Files

After confirming your own capability report is current, follow any additional function-area references required by `FUNC_WORKFLOW_BRAINBOX.md` or `FUNC_REQ_BRAINBOX.md`. The root document `DOB_MUST_README.md` governs the broader cross-subsystem reading order.

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

By proceeding with any operation within DEODINI_BRAINBOX, you acknowledge that you have read, understood, and agreed to comply with the requirements outlined in `FUNC_WORKFLOW_BRAINBOX.md`, `FUNC_REQ_BRAINBOX.md`, and this README.

---

## 4. Function-Area Change Request Reference

General change-request governance is maintained centrally in [DOB_MUST_README.md](../../DOB_MUST_README.md#change-request-governance).

> If this section was already read through `DOB_MUST_README.md`, it may be ignored.

The function-area compliance constant remains this file: `FQ_MUST_README.md`.

---

**End of FQ_MUST_README.md**
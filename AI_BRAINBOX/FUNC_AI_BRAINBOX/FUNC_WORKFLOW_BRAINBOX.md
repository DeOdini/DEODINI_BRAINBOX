[Reading 283 lines from start (total: 283 lines, 0 remaining)]

[Reading 285 lines from start (total: 285 lines, 0 remaining)]

# AI-Assisted Full-Stack Development Workflow

**Document Owner:** De O'Dini (OPERATOR)
**Document Status:** Foundational Workflow
**Domain:** Full-Stack Website Development — AI-Orchestrated Portfolio Pipeline
**Storage Location:** `AI_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_WORKFLOW_BRAINBOX.md`
**Related Files:** `AI_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_REQ_BRAINBOX.md`, `AI_BRAINBOX/FUNC_AI_BRAINBOX/FQ_MUST_README.md`

---

## 1. Document Purpose

This document defines the operating workflow for my Full-Stack Website Developer journey. It establishes how I plan to orchestrate multiple AI agents (ChatGPT, Claude, Grok, DeepSeek, Qwen, Cline, Copilot) to collaboratively research, design, build, test, and document real or free client website projects — with the goal of building a verified, portfolio-grade track record.

The workflow is designed to be:

- **Step-by-step and milestone-driven**
- **Documented at every stage**
- **Verified by multiple AI agents before acceptance**
- **Automation-ready** (primary: n8n; backup: email)
- **Human-in-the-loop** until full automation is proven

---

## 2. Background and Rationale

### 2.1 Automation Layer

I use **n8n** as my primary automation platform. It allows me to build the agent-to-agent workflow seamlessly. Since I am still learning n8n and only recently created my account, I require a **backup plan in case n8n fails**: email-based automation. Where neither n8n nor a given AI agent supports a native or MCP-based integration, I will keep testing backup channels until a reliable substitute is found.

### 2.2 Purpose of the Workflow

Across my AI agents — and given my Full-Stack Website Developer journey — I want to:

- Take on **spec/trial projects based on real Upwork briefs (unpaid), or paid client work**, to build my portfolio — each one labeled accurately by engagement type when published.
- **Automate the major part** of the AI agent workflow.
- Keep myself firmly **in the loop as the human operator** until each AI agent has proven it can handle its assigned tasks reliably.

### 2.3 Task Intake and Assignment

For any chosen task:

1. **ChatGPT** breaks down the task into a structured approach.
2. ChatGPT **assigns each sub-task to the AI agent best suited** for it — this is why every AI agent has already documented its connectors, skills, and current capabilities.
3. The structured workflow is then **passed to the other AI agents**, who receive their roles and responsibilities.

### 2.4 Dependency and Sequencing

Some agents must wait for others before beginning, because their work depends on prior output. For example:

- **Grok AI** — Conducts intensive research on global and client-region performance requirements for the website, and produces a refined UI/UX design direction based on findings. Grok passes its output to Qwen and Claude.
- **Qwen AI** — Handles front-end UI/UX design: builds all components based on Grok's research and the task requirements, in the language specified by the task.
- **Claude AI** — Handles back-end development in the language specified by the task.

**Sequencing rule:** Claude must wait for Qwen to finish. When Qwen completes, it must push to the local desktop device (via VS Code) and/or the GitHub repository — whichever is accessible at the time — before notifying Claude. Claude then retrieves the work from the repo and/or local device, and builds the backend, using the connectors Qwen left in place. When Claude finishes, it follows the same push-and-notify protocol.

### 2.5 Human-in-the-Loop / Version Control / Knowledge Base

Governance-level rules for human oversight, version control, and the AI knowledge base are maintained in the AI subsystem authority.

Ignore if this section was already read through `AI_BRAINBOX/AI_MUST_README.md`.

[AI_MUST_README.md](../AI_MUST_README.md)

### 2.6 Why Email Matters

Email is the backup communication and trigger channel for the workflow:

- Each AI agent is connected to its own designated email address.
- When a task is assigned or completed, an email is sent to **all recipient addresses**, with **CC and BCC** including the other agents.
- A **specific subject line or tag variable** signals which agent the message is for and what type of event it represents (task assignment, task completion, notification from a specific agent, etc.).
- Email alerts carry only call-to-duty messages (task/file-path pointers and brief status) — no secrets, keys, or source code. All code, secrets, and project work live via VS Code → local device → GitHub repo. On receiving an alert, the next AI agent goes to the stated file path to check and verify the work (other agents may also review and give feedback; the operator concludes) before proceeding.
- This has **not yet been tested**. The current stage was limited to skills and capacity checks only.
- The next stage is to **test, verify, validate, adjust, and retry** until the email-trigger system is confirmed to work reliably across all agents.
- All records and reports of this testing will be saved in `DEODINI_BRAINBOX`, so every agent knows common errors, what finally worked, and how to improve.

### 2.7 Career Objective

Milestones and the broader career objective are maintained in the AI subsystem authority.

Ignore if this section was already read through `AI_BRAINBOX/AI_MUST_README.md`.

[AI_MUST_README.md](../AI_MUST_README.md)

---

## 3. Core Principles

1. **Every milestone is documented.**
2. **Every milestone is verified by AI agents before acceptance.**
3. **Automation is introduced only after a step is proven manually.**
4. **Human approval is required at every critical checkpoint until automation is trusted.**
5. **No direct pushes to the main GitHub repository — branches only.**
6. **All working patterns, errors, and fixes are stored in `DEODINI_BRAINBOX`.**
7. **AI agent hierarchy is task-dependent**, based on each agent's strengths for the specific work.
8. **Every portfolio entry discloses its true engagement type** (unpaid spec/trial vs. paid client work) and the AI agents/workflow used to build it.

---

## 4. System Components

| Component                   | Role                                                       |
| ---------------------------- | ------------------------------------------------------------ |
| **n8n**                     | Primary automation orchestrator (agent-to-agent routing)   |
| **Email**                   | Backup communication and trigger channel                   |
| **GitHub (branches)**       | Version control and review layer                           |
| **VS Code (local desktop)** | Working environment and local repository                   |
| **DEODINI_BRAINBOX**        | Shared knowledge base and documentation archive             |
| **AI Agents**               | Distributed task executors (research, design, build, test) |

---

## 5. AI Agent Roles and Hierarchy

Agent hierarchy is **not fixed**. It is determined per task, according to each agent's demonstrated strengths.

| Agent        | Typical Strength (Per Task)                                |
| ------------ | ------------------------------------------------------------ |
| **ChatGPT**  | Task decomposition, workflow structuring, agent assignment |
| **Grok**     | Research, market/regional analysis, UI/UX direction        |
| **Qwen**     | Front-end UI/UX implementation, component building         |
| **Claude**   | Back-end implementation, system logic                      |
| **DeepSeek** | Specialized analysis and verification                      |
| **Cline**    | Repository-integrated coding tasks                         |
| **Copilot**  | In-editor assistance and code review                       |

Roles may shift per contract, but the **orchestration pattern** (ChatGPT plans → agents execute → `DEODINI_BRAINBOX` documents → human verifies) remains constant.

---

## 6. End-to-End Workflow

1. **Task Intake** — A project is selected: either a real client brief taken on as an unpaid spec/trial build, or actual paid client work.
2. **Decomposition** — ChatGPT breaks the task into a structured workflow and assigns sub-tasks.
3. **Distribution** — The workflow is distributed to all AI agents (via n8n, or email as fallback).
4. **Parallel / Sequential Execution** — Agents execute their assigned work, waiting on dependencies where required.
5. **Push and Notify** — Upon completion, each agent pushes to a branch and/or local device, then notifies the next agent in the chain.
6. **Human Review** — I confirm the milestone, review the branch, and commit/push via VS Code.
7. **Verification** — Other AI agents verify the completed work.
8. **Documentation** — Results, errors, and fixes are logged in `DEODINI_BRAINBOX`.
9. **Milestone Closure** — The milestone is marked complete and becomes a portfolio artifact, labeled per Core Principle 8.

---

## 7. Automation Layer

### 7.1 Primary: n8n

- Purpose: orchestrate agent-to-agent task flow.
- Status: newly set up; currently learning.
- Rule: no production reliance until proven stable.

### 7.2 Backup: Email Triggers

- Purpose: deliver task assignments and completion notifications if n8n fails.
- Status: to be tested and validated.
- Rule: every email must include clear subject tags so each agent can identify its intended recipient and event type; no secrets, keys, or source code in email content.

---

## 8. Email Trigger Protocol

| Field       | Purpose                                              |
| ----------- | ------------------------------------------------------ |
| **To**      | Primary recipient agent                              |
| **CC**      | Active participants in the workflow                  |
| **BCC**     | Remaining agents for record-keeping                  |
| **Subject** | Contains tag identifying event type and target agent |

**Tag categories (draft):**

- `[TASK-ASSIGN]` — new assignment
- `[TASK-DONE]` — completion notice
- `[TASK-REQ]` — dependency request
- `[TASK-ERR]` — error report
- `[TASK-VERIFY]` — verification request

Tags are drafts and will be refined after testing.

---

## 9. Verification and Validation Loop

Each new capability or workflow step is proven through this cycle:

1. **Check** — confirm the step exists and is configured.
2. **Test** — run it in a controlled scenario.
3. **Verify** — confirm output meets expectations.
4. **Validate** — confirm repeatability across agents.
5. **Adjust** — fix failures or ambiguities.
6. **Retry** — repeat until reliable.
7. **Record** — save the final working pattern in `DEODINI_BRAINBOX`.

No step is considered production-ready until it has passed this loop.

---

## 10. Standing Rule

Having already read `AI_BRAINBOX/FUNC_AI_BRAINBOX/FQ_MUST_README.md` and this document, all AI agents must next read `AI_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_REQ_BRAINBOX.md` before proceeding to other `DEODINI_BRAINBOX` folders/files.

**Repo visibility note:** Intended to be a private GitHub repo. Will remain public/open for now only if and until all participating AI agents can be confirmed to authenticate against a private repo.

---

## 11. Variables

**Variables (per task):**

- Task name and scope
- Agent role assignments
- Branch names and repo targets
- Subject-line tags
- Milestone naming and numbering
- Engagement type (unpaid spec/trial vs. paid) — per Core Principle 8

---

**Revision note:** Root revision history is maintained in `DOB_MUST_README.md`.

---
**End of FUNC_WORKFLOW_BRAINBOX.md**

[executed on device: DESKTOP-DHRIH27 (4836c4e3-c473-4ea0-b084-482f4637ff78)]

[executed on device: DESKTOP-DHRIH27 (4836c4e3-c473-4ea0-b084-482f4637ff78)]
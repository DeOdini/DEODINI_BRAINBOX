## Entry: The Five-Document Blueprint Workflow for AI-Assisted Fullstack Website Development

**Source Basis:** Conceptual framework adapted and expanded from Rahim Dev, "Before You Build an App With AI, Create These 5 Documents First" (September 23, 2026)

**Status:** RAW — Unverified. Pending testing, evaluation, and promotion to PROVEN status.

**Applies To:** Fullstack Website Projects

**Issued by:** De O'Dini (Operator)

**Storage:** `AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/RAW_WORKFLOW_PROJ_BRAINBOX/FULLSTACK_RAW_BRAINBOX/002DOC_BYB5DOC_PRESET_FLOW_STACK_BRAINBOX`

**Date Recorded:** [Current Date]

---

## Preface: Purpose of This Entry

This document records a **proposed** workflow for AI-assisted fullstack website development. It is stored in RAW because it has not been tested end-to-end. It describes a structured collaboration between **Client, Developer, AI Agents, and Users** against a shared blueprint, not against loose prompts.

Each section states not only *what* the step is, but *why* it is essential, *who* it speaks to, and *how* the information is derived. Any AI agent or Operator reading this years later should understand intent, sequence, and reasoning without extra context.

On successful validation → promote to `PROVEN_PATTERN_PROJ_BRAINBOX.md`.

Failed or partial variants → `FAILED_PATTERN_PROJ_BRAINBOX.md` with project tags and failure reasons.

Nothing is discarded; it is only reclassified (DOB Master Rules).

---

## Part 1: General Explanation — Why This Workflow Is Essential

**Speaks to:** AI Agent and Developer

### 1.1 Introduction and Purpose

AI tools (ChatGPT, Claude, Grok, Qwen, DeepSeek, Cline, Copilot) execute well only when the product is already defined. The usual failure is not the model; it is the missing blueprint.

A vague prompt such as "Build me a bookings website" may look productive for many turns, then collapse: architecture drifts, UI becomes inconsistent, backend rules contradict each other, and the developer loses control. This workflow exists to prevent that. Five documents must exist before serious development. They give agents a fixed target and keep the developer in control of product decisions.

### 1.2 Why AI Coding Projects Become Messy

**Speaks to:** AI Agent and Developer

Root cause: planning is skipped and AI is asked to build everything at once. Typical results:

- Inconsistent UI (spacing, color, layout drift)
- Fragmented state and folder patterns
- Inconsistent backend rules
- Unstable database schema
- Guessed API contracts
- Auth that works while authorization stays weak
- Admin features hidden in UI but not protected server-side
- Features that work alone and break when connected
- Code that is hard to test because structure never stabilized

Speed is not the same as planning.

### 1.3 Workflow Principle

**Speaks to:** AI Agent and Developer

**Define the blueprint before the build.**

Sequence:

1. Raw client requirements
2. Product Requirements Document (PRD)
3. Technical Architecture Document
4. Security and Access Control Specification
5. Frontend and Integration Specification
6. Feature Ticket List
7. Code generation (one ticket at a time)
8. Testing and review

Principle in short: **Decide first. Structure second. Ticket third. Generate fourth. Verify always.**

### 1.4 Project Stack (Raw — Until Proven)

**Speaks to:** AI Agent and Developer

Baseline for this project context (adjust only by formal document update, not by casual prompt):

```text
Frontend: React + TypeScript
Backend: Python + FastAPI
Database / Auth: Supabase (PostgreSQL + Auth + RLS)
Runtime isolation: Docker / Docker Compose
AI tools: ChatGPT, Claude, Grok, Qwen, DeepSeek, Cline, Copilot
```

**If a prompt conflicts with this stack, the stack wins** until the Operator updates the architecture document.

Why this matters: without a declared stack, agents invent different frameworks, databases, and auth methods. The stack is a boundary condition for every agent and for the developer who enforces it.

---

## Part 2: Product Requirements Document (PRD)

**Derived From:** Client

**Delivered By:** Developer → AI Agent

**Speaks to:** Client (source), Developer (extractor), AI Agent (consumer), Users (represented)

### 2.1 Purpose

The PRD defines what is being built, why, and for whom — before stack debates. It is the client's intent structured for execution, not the developer's invention and not the AI's guesswork.

### 2.2 What the PRD Must Contain

Each item as a full statement an agent can act on:

- **Problem statement** — What problem the site solves and why it must exist
- **Target users** — Who uses it; needs, behaviors, constraints
- **Product goal** — Primary objective and what success looks like
- **User roles** — Distinct roles and what each can do
- **Core features** — Essential capabilities
- **Main user flows** — How users complete primary goals
- **MVP boundaries** — Explicit in-scope and out-of-scope for v1
- **Success metrics** — How "good enough for v1" is judged

Weak: "Build a bookings site."

Strong: role-based flows, payment timing, admin powers, and explicit exclusions (e.g. no video consult in v1).

---

## Part 3: Technical Architecture Document

**Derived From:** Client intent, structured by Developer

**Delivered By:** Developer → AI Agent

**Speaks to:** Developer (owns decisions), AI Agent (implements, does not redesign)

### 3.1 Purpose

Bridge from PRD to code. Locks stack, structure, data model, and API style so agents do not invent competing architectures.

### 3.2 What It Must Contain

- Folder / project structure (frontend and backend)
- Database schema and relationships
- API contract conventions
- State management and routing approach
- Auth architecture (Supabase + FastAPI verification)
- Environment / secrets strategy
- Error handling and logging approach
- Docker service layout

Why essential: without this, each prompt can reinvent structure. With it, tickets say "implement inside the locked plan."

---

## Part 4: Security and Access Control Specification

**Speaks to:** Client, Developer, AI Agent, Users

### 4.1 Purpose

Defines authentication (who) and authorization (what). Protects business logic, user data, and system integrity. UI hiding is not security.

### 4.2 Client-derived questions (Developer asks Client)

- Who can create accounts, and how?
- What roles exist?
- What can each role view, create, edit, delete?
- Which actions are admin-only?
- Which data is user-owned and private?
- What happens on access denial?
- Account deletion / data removal expectations?
- Which fields are sensitive?

### 4.3 What the Specification Must Contain

- Authentication method
- Roles and permissions (explicit lists)
- Backend authorization rules (FastAPI)
- Row Level Security rules (Supabase)
- Token handling
- Input validation
- Admin-only actions
- User-owned data rules

Why essential: AI-generated systems often authenticate successfully while authorization stays weak. Explicit rules before generation reduce that failure class.

---

## Part 5: Frontend and Integration Specification

**Speaks to:** Developer and AI Agent

*(Both halves required — frontend and integration)*

### 5.1 Purpose

Keeps visual system and system connections consistent. Enables clean task assignment to agents (e.g. design handoff vs API implementation).

### 5.2 Frontend Must Define

Design system, page inventory, component hierarchy, responsive behavior, interaction patterns, loading / empty / error / success states.

**Example:** Homepage hero + search, listing grid, footer; listing card = image, title, price, Book Now; booking flow = date → guest details → confirmation.

### 5.3 Integration Must Define

API endpoints, request/response shapes, auth headers, error handling, loading/empty behavior, Supabase vs FastAPI usage rules, third-party services.

**Example:** `GET /api/listings` returns JSON array `{ id, title, price, imageUrl }`; on failure show error banner with retry; while loading show skeleton cards.

---

## Part 6: Feature Ticket List

**Speaks to:** AI Agent and Developer

**Derived From:** All prior documents

**Most critical execution stage**

### 6.1 Purpose

Planning becomes production only when work is ticketed. Tickets are discrete, assignable units mapped to agent strengths (per `FUNC_WORKFLOW_BRAINBOX.md`).

### 6.2 Each Ticket Must Contain

- Title
- Description
- Input / Output
- Acceptance criteria
- Dependencies
- Priority
- API / DB changes if any
- Testing notes

### 6.3 Example Tickets

**Ticket: User Registration Form**

Acceptance: email validation; password rules; inline errors; success path creates identity + profile; loading blocks double submit; clear server errors.

Dependencies: users/profiles schema; `POST /api/auth/register` (or Supabase Auth path) defined.

**Ticket: View Own Profile**

Acceptance: unauthenticated blocked; user reads only own profile; cannot read others; loading/error states correct; enforced in backend and/or RLS, not UI-only.

Dependencies: auth complete; profiles schema; ownership rules documented.

---

## Part 7: Application to DEODINI_BRAINBOX Workflow

**Speaks to:** AI Agent and Operator

| Blueprint Document | Brainbox Counterpart |
| --- | --- |
| Product Requirements Document | Task intake + ChatGPT decomposition (`FUNC_WORKFLOW`) |
| Technical Architecture Document | Locked stack + patterns later proven in `PROVEN_PATTERN_PROJ_BRAINBOX.md` |
| Security & Access Control Specification | Client answers + agent implementation constraints; capability/permission honesty in `FUNC_AI_BRAINBOX` |
| Frontend & Integration Specification | Grok research/UI direction → Qwen frontend handoff; API contracts for Claude/backend agents |
| Feature Ticket List | Per-task agent role assignments and sequenced execution |

Per-project blueprints are the **input**.

Brainbox is the **cumulative memory**: agents search proven methods, review raw/failed context, adapt, and write results back. RAW stays non-binding until tested against DOB/FQ governance.

---

## Part 8: Proposed Execution Sequence *(superseded by Part 13 below)*

1. **Intake** — Task or client website requirement received
2. **Client clarification** — Developer runs PRD (and security) questions
3. **Blueprint phase** — Five documents drafted; Operator approves
4. **Decomposition** — ChatGPT converts blueprints into agent-assigned workflow
5. **Distribution** — n8n primary / email backup (`FUNC_WORKFLOW`)
6. **Execution** — Agents build against blueprint and tickets, not loose prompts
7. **Push and notify** — Branch/local device; next agent in chain
8. **Human review** — Operator confirms milestone; no direct `main` pushes
9. **Verification** — Cross-agent review against blueprint + acceptance criteria
10. **Documentation** — Results, errors, fixes into Brainbox
11. **Promotion** — Validated workflow RAW → PROVEN; failures → FAILED

*(Note: Part 13 below is the updated sequence incorporating build-order decisions and pre-ticket constants. Part 8 is retained for historical continuity but Part 13 governs execution going forward.)*

---

## Part 9: Testing and Modification Notes (Parts 1–10)

- Entry is **RAW**; not end-to-end proven
- After trials, expect possible changes to: document count/granularity; agent-role mapping; which layers automate first; which stay human-in-the-loop longest
- Cross-check against DOB and FQ before treating as binding
- Success → `PROVEN_PATTERN_PROJ_BRAINBOX.md`
- Failure/partial → `FAILED_PATTERN_PROJ_BRAINBOX.md` with tags and reasons

---

## Part 10: Cross-References (Parts 1–10)

- `AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/PROJ_MUST_README.md`
- `AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/PROVEN_PATTERN_PROJ_BRAINBOX.md`
- `AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FAILED_PATTERN_PROJ_BRAINBOX.md`
- `AI_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_WORKFLOW_BRAINBOX.md`
- `AI_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_REQ_BRAINBOX.md`
- `AI_BRAINBOX/FUNC_AI_BRAINBOX/FQ_MUST_README.md`
- `AI_BRAINBOX/AI_MUST_README.md`
- `DOB_MUST_README.md`

---

# Addition: Build Order Approaches and Pre-Ticket Constants

**Source Basis:** Operator-defined workflow addition, derived from DEODINI_BRAINBOX project planning

**Status:** RAW — Unverified. Pending testing, evaluation, and promotion to PROVEN status.

---

## Part 11: Build Order Approaches

**Speaks to:** Developer and AI Agent

When building a fullstack website, there are two primary approaches to consider. The choice between them depends on the complexity of the website, the dependency of the frontend on the backend, and the risk profile of the project. This section defines both approaches, states when each is appropriate, and identifies the decision factors that guide the choice.

### 11.1 Approach One: Frontend and Integration Connectors First, Then Backend

**Definition:** In this approach, the developer and AI agents build all or nearly all MVP UI requirements first. The frontend is constructed with the necessary backend information — such as API contracts and data shapes — already in place. The goal is to satisfy all visual expectations before the backend is completely built. Once the frontend and its integration connectors are in place, the backend is built to be plugged into and connected to the waiting frontend.

**When this approach is appropriate:**

- The website has a lighter backend structure.
- The primary value of the website is its visual presentation and user experience.
- The backend can be approximated or mocked during frontend development.
- The client prioritizes seeing a working visual prototype early.

**What must be true for this approach to succeed:**

- The integration connectors (API contracts, data shapes, endpoint definitions) must be defined in advance, even if the backend is not yet built.
- The frontend must be built against those connectors, so that when the backend is ready, it plugs in cleanly.
- The frontend team must resist the temptation to invent backend behavior. The connectors define what the backend will do.

### 11.2 Approach Two: Backend First, Then Frontend

**Definition:** In this approach, upon completing the entire workflow instructions and information gathering — and after ticketing and allotting tasks for execution — the major functional parts of the backend are built first. This may involve testing the backend against temporary, blank demo web pages. Once the backend functionality is actively solid, the frontend is safely built with knowledge of what works on the backend, rather than assuming that the backend works based on the ticketing tasks alone.

**When this approach is appropriate:**

- The website has a more complex structure.
- The website depends on a solidified backend that is integration-ready before the frontend is built.
- The backend contains business logic that must be verified before the frontend is designed around it.
- The risk of building the frontend on unverified backend assumptions is high.

**What must be true for this approach to succeed:**

- The backend must be tested against real endpoints, even if the testing interface is a temporary blank web page.
- The backend must be proven functional before the frontend is built against it.
- The frontend team must have access to the verified backend behavior, not to assumptions about it.

### 11.3 Approach Three: Even Build Based on Dependency

**Definition:** In some projects, neither approach one nor approach two is strictly correct. Instead, the frontend and backend are built evenly, based on the dependency of each frontend component on its corresponding backend component. A frontend feature that depends on a completed backend endpoint waits for that endpoint. A backend endpoint that has no frontend dependency yet can be built independently. The build order is determined by the dependency graph, not by a blanket rule.

**When this approach is appropriate:**

- The website has mixed complexity, with some features that depend heavily on the backend and others that do not.
- The project benefits from parallel progress on frontend and backend.
- The dependency relationships between frontend and backend components are well understood and documented.

**What must be true for this approach to succeed:**

- The dependency graph between frontend and backend components must be documented in the Feature Ticket List.
- Each ticket must clearly state its dependencies.
- The developer must actively manage the sequencing to prevent agents from waiting unnecessarily or building on unverified assumptions.

### 11.4 Decision Factors

The choice between approaches is not arbitrary. The following factors should guide the decision:

| Factor | Favors Approach One (Frontend First) | Favors Approach Two (Backend First) |
| --- | --- | --- |
| Backend complexity | Low | High |
| Frontend complexity | High | Low |
| Client priority | Visual prototype early | Functional integrity early |
| Risk of backend assumptions | Low | High |
| Availability of API contracts | High | Low |
| Need for early user feedback | High | Low |

**Note:** Approach Three (Even Build) is appropriate when both frontend and backend complexity are significant, and the dependency graph is well understood.

**Decision rule:** The developer selects the approach during the blueprint phase, before ticketing. The chosen approach is recorded in the Technical Architecture Document and reflected in the Feature Ticket List dependencies.

---

## Part 12: Pre-Ticket Constants

**Speaks to:** Developer and AI Agent

Regardless of which build order approach is chosen, the following items must be completed before feature tickets are issued. These are constants. They do not vary by approach. They ensure that every agent begins work with the same visual and structural understanding of the website.

### 12.1 Visual Image Deliverables

Two visual diagrams must be generated, researched, or sourced before ticketing. These diagrams provide the shared visual vocabulary that all agents use when building the website.

#### 12.1.1 Website Structure Wireframe Diagram

A proper website structure wireframe diagram must be generated or researched. This diagram shows the layout of each page or screen — the position of headers, navigation, content areas, sidebars, footers, and key components. It does not need to be pixel-perfect, but it must clearly communicate the structure of each page.

**How it may be produced:**

- Generated by an AI agent (e.g., image generation tool).
- Researched using available tools (e.g., image search for reference structures).
- Called from Figma or another design tool, if available.
- Sketched manually and digitized.

**Why this is essential:** Without a wireframe, each agent will invent its own layout. The result is visual inconsistency, rework, and a fragmented user experience.

#### 12.1.2 User Flow Wireframe Diagram

A proper user flow wireframe diagram must also be generated or researched. This diagram shows how users move through the website — from entry point to goal completion. It maps the sequence of screens, the decisions the user makes, and the branches that lead to different outcomes.

**How it may be produced:**

- Generated by an AI agent.
- Researched using available tools.
- Called from Figma or another design tool.
- Sketched manually and digitized.

**Why this is essential:** Without a user flow diagram, the frontend and backend may be built against different assumptions about how users move through the website. The result is broken navigation, missing states, and integration failures.

### 12.2 Markdown Deliverables

Two Markdown documents must be produced before ticketing. These documents provide the shared structural vocabulary that all agents use when organizing the website.

#### 12.2.1 Well-Structured Project Tree

A well-structured project tree must be defined in Markdown. This document shows the folder and file organization of the project — where the frontend code lives, where the backend code lives, where configuration files are stored, and how the project is organized on disk.

**Example structure:**

```text
project-root/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   └── styles/
│   └── public/
├── backend/
│   ├── src/
│   │   ├── controllers/
│   │   ├── models/
│   │   ├── routes/
│   │   └── services/
│   └── config/
├── docs/
│   ├── prd.md
│   ├── architecture.md
│   ├── security.md
│   ├── frontend-spec.md
│   └── tickets.md
└── README.md
```

**Why this is essential:** Without a project tree, each agent will place files in different locations. The result is a disorganized repository, broken imports, and difficulty locating code.

#### 12.2.2 Well-Structured Sitemap

A well-structured sitemap must be defined in Markdown. This document shows the pages and routes of the website — how they relate to one another, which pages are nested under which, and how navigation flows between them.

**Example structure:**

```text
/                       → Homepage
├── /about              → About page
├── /services           → Services listing
│   ├── /services/[id]  → Individual service detail
│   └── /services/book  → Booking flow
├── /contact            → Contact page
├── /login              → Login page
├── /register           → Registration page
└── /dashboard           → User dashboard (authenticated)
    ├── /dashboard/profile    → Profile settings
    └── /dashboard/bookings   → User bookings
```

**Why this is essential:** Without a sitemap, the frontend routes and backend endpoints may not align. The result is broken links, missing pages, and inconsistent navigation.

### 12.3 Constant Rule

The items in this section are **constants**. They must be completed before feature tickets are issued, regardless of which build order approach is chosen. They are not optional. They are the foundation upon which ticketing, task assignment, and execution depend.

If any of these items is missing, the developer must pause ticketing and complete the missing item first.

---

## Part 13: Updated Execution Sequence *(supersedes Part 8)*

1. **Intake** — Task or client website requirement received.
2. **Client Clarification** — Developer asks the PRD questions and records the client's answers.
3. **Blueprint Phase** — The five documents are drafted and approved by the Operator.
4. **Pre-Ticket Constants** — Visual images (website structure wireframe, user flow wireframe) and Markdown deliverables (project tree, sitemap) are produced.
5. **Build Order Decision** — Developer selects the build order approach (frontend first, backend first, or even build) based on the decision factors.
6. **Decomposition** — ChatGPT converts the blueprints into an agent-assigned workflow, reflecting the chosen build order.
7. **Feature Ticket List** — Tickets are issued with acceptance criteria, dependencies, and agent assignments.
8. **Distribution** — Workflow is dispatched via n8n (primary) or email (backup).
9. **Execution** — Agents build against the blueprint and tickets, following the chosen build order.
10. **Verification** — Cross-agent review against blueprint criteria and ticket acceptance criteria.
11. **Documentation** — Results logged into Brainbox.
12. **Promotion** — Validated workflow moves from RAW to PROVEN.

---

## Part 14: Testing and Modification Notes (Parts 11–15)

- This addition is **RAW**. It has not been tested end-to-end.
- Expected modifications after testing:
  - Refining the decision factors for build order selection.
  - Determining whether a fourth approach is needed for specific project types.
  - Testing whether the pre-ticket constants are sufficient or require additional items.
  - Evaluating how the build order decision interacts with agent capabilities (e.g., whether Claude is better suited to backend-first projects).
- Upon successful validation, this addition should be promoted to `PROVEN_PATTERN_PROJ_BRAINBOX.md`.
- Failed or partially working variants should be recorded in `FAILED_PATTERN_PROJ_BRAINBOX.md` with project tags and failure reasons.

---

## Part 15: Cross-References (Parts 11–15)

- `AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/PROJ_MUST_README.md`
- `AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/PROVEN_PATTERN_PROJ_BRAINBOX.md`
- `AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/FAILED_PATTERN_PROJ_BRAINBOX.md`
- `AI_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_WORKFLOW_BRAINBOX.md`
- `AI_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_REQ_BRAINBOX.md`

---

**End of Entry**

---

**One structural note on the merge, flagged for your review specifically:** Part 8 (original execution sequence) and Part 13 (updated execution sequence) now both exist in this merged file, and they overlap in purpose. I marked Part 8 as "superseded" rather than deleting it, since removing content wasn't something you asked for — but you may want me to either delete Part 8 outright, or keep both for historical traceability. Let me know which, along with whether this merged version looks right to write to disk.
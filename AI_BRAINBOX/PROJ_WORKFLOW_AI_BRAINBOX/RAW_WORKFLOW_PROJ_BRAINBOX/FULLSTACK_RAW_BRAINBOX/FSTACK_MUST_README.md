# README — RAW WORKFLOW vs. PRESET WORKFLOW (Deodini Brainbox)

**Purpose:** This document explains why two versions of the fullstack website workflow exist side by side in the Brainbox, what each is for, when to use which, and the build-order and pre-ticketing requirements that apply regardless of which version is used.

---

## The Two Documents

| Document | State | Tooling assumption | Best used as | Proven status |
| --- | --- | --- | --- | --- |
| **001DOC_BYB5DOC_FLOW_STACK_BRAINBOX** | Fully raw, unrefined | Stack assumed (React/FastAPI/Supabase/Docker), but no agent-to-task assignment | Discovery tool / client-question generator / neutral reference | Not proven |
| **002DOC_BYB5DOC_PRESET_FLOW_STACK_BRAINBOX** | Refined, ready-to-execute | Stack and specific AI agent roles pre-assigned (ChatGPT decomposition, Grok→Qwen handoff, etc.) | Fast-start execution template for matching projects | Not proven |

---

## Why 002DOC_BYB5DOC_PRESET_FLOW_STACK_BRAINBOX Exists — and What It Actually Is

The preset workflow takes the raw workflow and clones the function-workflow of each AI agent and tool already available in the Brainbox directly into the proposed structure, making it ready for execution. It pre-assigns which agent handles which stage of the pipeline — this is what makes it fast to act on.

**The tradeoff:** by assigning agents and tools ahead of time, the preset workflow makes an implicit assumption about what the client's website will require, before the full client details are known. This does not make it wrong or unusable — it functions as a head start for projects that turn out to match its assumed shape. But it is not proven, and its agent assignments are only as good as how well a given project matches the shape it was built around.

**Correction worth noting for future readers:** the preset workflow is not the only place an assumption is made — the raw workflow also carries an assumed tech stack (React/FastAPI/Supabase/Docker). The real distinction is narrower than "the raw workflow assumes nothing": **the raw workflow assumes a stack but not agent/tool role assignments; the preset workflow assumes both.** Treat this distinction precisely, not loosely, when deciding which to reach for.

---

## Why 001DOC_BYB5DOC_FLOW_STACK_BRAINBOX Exists — and What It Actually Is

The raw workflow remains in its unrefined, raw state. No agent or tool function-workflow is assumed — it simply presents the workflow itself, undecorated. This is exactly what makes it flexible: whatever agents and tools actually suit a given project can be infused into this base without fighting an existing assignment.

**Example:** if a client's website is primarily about marketing, email campaigns, and automation, the right agents and tools for that project will likely differ from the preset workflow's assumed set. The raw workflow's neutrality means it can absorb that project's actual requirements cleanly, producing a refined version that can then be tested, proven, or marked failed for revisiting.

**Second function:** because it hasn't assumed anything yet, the raw workflow also serves as the better reference for generating the right discovery questions — both for the client and for AI-agent prompting. It can be used to construct client proposals, asking tangible questions with relatable solutions grounded in its raw, unbiased form.
**Caveat worth carrying forward:** the raw workflow's neutrality is not total. It still inherits the underlying five-document skeleton (PRD → Architecture → Security → Frontend/Integration → Tickets), which implicitly assumes a fairly standard, auth'd, CRUD-style web app. A project that diverges sharply from that shape — e.g., a marketing/email-automation-heavy site — may find that even the raw workflow's document structure, not just its tooling, needs adaptation. The raw workflow is tool-agnostic, not necessarily shape-agnostic.

---

## How to Treat Each Document Going Forward

1. **Default to 001DOC_BYB5DOC_FLOW_STACK_BRAINBOX** when starting client discovery, drafting proposal questions, or scoping a new project whose requirements aren't yet known to match any existing preset.
2. **Reach for 002DOC_BYB5DOC_PRESET_FLOW_STACK_BRAINBOX** when a project's shape is already recognized as matching its assumed stack and agent roles — it saves redundant setup on projects that resemble prior, validated work.
3. **Neither is authoritative until proven.** Both remain RAW. Validated outcomes should be promoted to `PROVEN_PATTERN_PROJ_BRAINBOX.md`; failures or partial fits should be recorded in `FAILED_PATTERN_PROJ_BRAINBOX.md` with project tags and failure reasons, per standing DOB rules — nothing is discarded, only reclassified.
4. **If 002DOC_BYB5DOC_PRESET_FLOW_STACK_BRAINBOX is formally retained**, it should be clearly labeled as a *derived instance* of 001DOC_BYB5DOC_FLOW_STACK_BRAINBOX, not a second canonical base — e.g., a header note stating: *"This is an instantiated variant of 001DOC_BYB5DOC_FLOW_STACK_BRAINBOX, pre-configured for [stated stack/agent assumptions]. Validate applicability before reuse on a differently-shaped project."* This prevents a future reader or agent from mistaking the preset for the neutral source.

---

## Build-Order Decision: Frontend-First vs. Backend-First

Regardless of which workflow document is used, once discovery and ticketing are complete, the AI agent and developer must choose a build order. There are two approaches, and the choice is a deliberate architectural decision — not a default.

### Approach One: Frontend + Integration Connectors First, Then Backend

Build all or near-MVP UI requirements, along with whatever backend information is necessary to support that UI, satisfying full visual expectations before the backend is completely built and plugged in.

### Approach Two: Backend First, Then Frontend

Once workflow instructions, information gathering, and ticketing are complete, the major functional parts of the backend are built first — even if this means testing the backend against a blank demo webpage. Only once backend functionality is solid does frontend construction begin, built with actual knowledge of what works on the backend rather than assuming it will work based on the ticket description alone.

### How to Choose Between Them

The right approach depends on the website's complexity:

- **Backend-first** is appropriate when the website's structure is complex and the frontend meaningfully depends on a solidified, integration-ready backend.
- **Frontend-first** is appropriate when the backend structure is comparatively light — the UI/frontend can be built first with the necessary backend information in hand, before the backend is fully built and connected.
- **Even/parallel build** is also valid: frontend and backend can be built in step with each other, based on the actual dependency relationship between each frontend piece and its corresponding backend piece.

This decision should be made explicitly per project — not assumed — and recorded as part of that project's Technical Architecture Document.
---

## Constant Requirements Before Any Tickets Are Issued

Regardless of which workflow document is used, the following must exist before ticketing begins:

### Visual Assets

- A proper website structure **wireframe diagram** — generated or researched using available tools (e.g., image search, pulled from Figma, or generated directly by an AI agent).
- A proper **user flow wireframe diagram** — likewise generated or researched using available tools.

### Markdown Documentation

- A well-structured **project tree**.
- A well-structured **sitemap**.

These four items are treated as constant prerequisites — they apply whether the project follows 001DOC_BYB5DOC_FLOW_STACK_BRAINBOX or 002DOC_BYB5DOC_PRESET_FLOW_STACK_BRAINBOX, and whether the build order chosen is frontend-first, backend-first, or parallel.

---

**Terminology rule:** In this README, references to "Doc 7" and "Doc 8" have been replaced by their canonical filenames: 001DOC_BYB5DOC_FLOW_STACK_BRAINBOX and 002DOC_BYB5DOC_PRESET_FLOW_STACK_BRAINBOX.

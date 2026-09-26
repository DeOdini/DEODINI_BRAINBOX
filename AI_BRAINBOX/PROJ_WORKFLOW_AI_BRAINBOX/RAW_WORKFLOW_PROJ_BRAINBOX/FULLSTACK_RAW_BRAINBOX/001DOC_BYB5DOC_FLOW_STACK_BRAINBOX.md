## Proposed Fullstack Website Workflow (To Be Tested and Proven)

**Status:** Raw / Proposed  
**Storage:** AI_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/RAW_WORKFLOW_PROJ_BRAINBOX/FULLSTACK_RAW_BRAINBOX/001DOC_BYB5DOC_FLOW_STACK_BRAINBOX  
**Purpose of storage:** Not to assume this workflow is already correct for DEODINI, but to hold it as a proposed system that AI agents and operators can execute, test, and later mark as proven or failed.  
**Intended stack context:** React + TypeScript frontend, Python/FastAPI backend, Supabase (database + auth), Docker for runtime isolation.

---

## 1. GENERAL EXPLANATION — WHY THIS WORKFLOW IS ESSENTIAL  
*(Speaks primarily to the AI Agent and the Developer)*

### A. Introduction — Purpose

This workflow exists because AI coding tools are powerful at execution, but weak at inventing a coherent product from incomplete thinking. When a developer or an AI agent begins building a website without a stable product contract, the system is forced to invent decisions while code is being written. Those invented decisions accumulate. Over time, the project becomes a collection of locally working parts that do not form one reliable product.

The purpose of this workflow is therefore not to slow development for its own sake. Its purpose is to move critical decisions to the front of the process so that:

- the **client** defines what success means,
- the **developer** translates that definition into structured instructions,
- the **AI agent** executes inside clear boundaries,
- and the **users** receive a website that behaves consistently, securely, and predictably.

This document is the raw form of that system. It is stored in DEODINI BRAINBOX so it can be applied, tested against real tickets, corrected, and only then promoted into proven pattern storage.

---

### B. Why AI Coding Projects Become Messy

AI-assisted website projects become messy when the model is required to invent product, architecture, security, and interface decisions at the same time as it generates code. The AI may still produce screens, endpoints, and database tables that appear functional. The damage is usually not immediate failure. The damage is structural drift.

Common problems include:

- Different pages using different spacing, colors, layout logic, and component behavior, so the site no longer feels like one product.
- Mixed technical patterns across features, such as different state handling methods, different API calling styles, or different folder structures introduced prompt by prompt.
- Backend rules that change depending on which feature was generated last, creating inconsistent validation and business logic.
- Database tables and fields that shift after almost every prompt, making earlier features fragile.
- API request and response shapes that were guessed rather than contracted, so frontend and backend slowly stop matching.
- Authentication that works on the surface while authorization remains weak or incomplete.
- Admin capabilities that are only hidden in the interface and not truly blocked on the server or database layer.
- Features that pass when tested alone, then fail when connected to the rest of the system.
- Testing difficulty, because there is no stable structure against which correctness can be judged.

These problems affect every role:

- The **AI agent** receives unclear boundaries and fills gaps with assumptions.
- The **developer** loses control of architecture and spends later time repairing earlier speed.
- The **client** receives a product that drifts away from the original business intent.
- The **users** experience inconsistency, broken flows, or insecure behavior.

The core conclusion is simple: AI can generate code quickly, but speed without a shared plan produces rework. This workflow exists to prevent that pattern.

---

### C. Workflow Principle

**Decide first. Structure second. Ticket third. Generate fourth. Verify always.**

This principle means:

1. Product decisions are collected and locked before serious coding begins.  
2. Technical structure is defined so generation follows one architecture.  
3. Work is broken into tickets so execution remains controlled.  
4. AI generation happens inside those tickets, not as free-form invention.  
5. Every output is checked against the original documents before the next ticket starts.

If a later prompt conflicts with the locked stack or locked architecture, the locked definition wins until a human operator formally updates the documents.

---

### D. Project Stack (Raw Workflow — Until Proven)

This proposed workflow assumes the following stack while it is being tested:

- **Frontend:** React + TypeScript  
- **Backend:** Python + FastAPI  
- **Database / Auth:** Supabase (PostgreSQL, Auth, Row Level Security)  
- **Runtime isolation:** Docker / Docker Compose  
- **AI tools:** used for structured generation, review, and ticket execution — not for uncontrolled redesign of the system

Once this stack is proven through real project use, the rule becomes absolute:  
**If a prompt conflicts with this stack, the stack wins.**

Any change to stack must be treated as an architecture decision, not as a casual generation preference.

---

## 2. CLIENT CLARIFICATION LAYER  
### Product Requirements Document (PRD)  
*(Speaks first to the Client; delivered and structured by the Developer; consumed by the AI Agent)*

### Why this step is essential

Without a PRD, the project has no stable definition of success. The client may have a desired website in mind, but if that desire is not extracted into precise product language, the developer cannot instruct the AI agent correctly, and the AI agent cannot distinguish required behavior from optional invention.

The PRD is therefore the first conversion layer:

- from **client intention**  
- into **developer-controlled requirements**  
- into **AI-executable product boundaries**

### Who this step speaks to

- **Client:** source of truth for business goals, users, features, and MVP limits  
- **Developer:** interviewer, translator, and guardian of scope  
- **AI Agent:** consumer of a finished product definition, not the inventor of that definition  
- **Users:** indirectly represented through roles, flows, and success metrics

### How this information is derived

The developer does not guess the product. The developer actively extracts it from the client through direct questions and structured answers. Those answers are then written into the PRD before architecture or coding begins.

### What the PRD must contain, explained fully

**Problem statement**  
A clear explanation of the problem the website exists to solve. This prevents the team from building features that are technically impressive but commercially irrelevant.

**Target users**  
Who the website serves. This shapes language, flows, permissions, and interface priorities.

**Product goal**  
What successful operation of the website means in practical terms. This becomes the reference point when later feature requests appear.

**User roles**  
The categories of people who will interact with the system, such as visitor, registered user, staff, or admin. Roles later drive security and ticket design.

**Core features**  
The capabilities that must exist for the product to be real. These are not technical tasks yet; they are product capabilities.

**Main user flows**  
The important sequences a user must be able to complete, such as sign up, complete a purchase, submit a request, or manage an account. Flows expose missing requirements early.

**MVP boundaries**  
What is deliberately excluded from the first version. This protects the project from uncontrolled expansion during AI generation.

**Success metrics**  
How the team will know the first version is good enough. Metrics may be functional, operational, or business-related, but they must be explicit.

### Example of the difference this step creates

Weak client instruction:  
“Build a bookings website.”

Structured PRD direction:  
“Customers can create accounts, view available services, book a time slot, pay before confirmation, and receive booking status updates. Staff can manage availability and booking status. Admin can manage staff and view booking history. Video consultation is out of scope for version one.”

The second version gives the AI agent a product to implement. The first version forces the AI agent to invent a product.

---## 3. STRUCTURING LAYER  
### Technical Architecture Document  
*(Client provides the desired outcome; Developer converts it into structure; AI Agent must follow that structure)*

### Why this step is essential

After the PRD defines *what* is being built, architecture defines *how* it will be built as one system. Without architecture, the AI agent may solve each feature differently. One feature may place logic in the frontend. Another may place similar logic in the backend. Another may introduce a new folder pattern or state pattern. Each piece can work locally while the whole website becomes harder to maintain.

Architecture is the document that stops that drift.

### Who this step speaks to

- **Client:** does not write architecture, but supplies the product constraints that architecture must serve  
- **Developer:** owns architecture decisions and is responsible for locking them  
- **AI Agent:** must implement inside the architecture, not redesign it during ticket execution  
- **Users:** benefit through stability, performance consistency, and maintainable evolution of the product

### How this information is derived

The developer takes the PRD and translates it into technical structure for the chosen stack. The AI agent may help draft or refine architecture, but the developer remains responsible for approving the final version before feature generation begins.

### What the architecture document must define, explained fully

**Frontend structure**  
How the React + TypeScript application is organized: folders, routing approach, state management approach, shared components, and page composition rules. This ensures every new screen is generated into the same system.

**Backend structure**  
How the FastAPI application is organized: routers, services, models, dependency injection, validation patterns, and separation between transport logic and business logic.

**Database schema**  
The Supabase PostgreSQL tables, relationships, and ownership rules needed by the product. Schema should be stable enough that features are not inventing tables ad hoc.

**API contract style**  
The expected shape of requests and responses, error format, naming conventions, and authentication expectations between frontend and backend.

**Auth flow**  
How Supabase Auth is used, how sessions are handled, and how the backend verifies identity before protected actions run.

**Environment and configuration strategy**  
Where secrets live, how local, staging, and production settings differ, and what the AI agent is forbidden from hard-coding.

**Error handling pattern**  
How failures are reported to users and logged for operators, so every feature does not invent its own error language.

**Docker service layout**  
How frontend, backend, and supporting services run in isolated containers so the development and deployment environment remain consistent.

### Why this is essential in execution

When architecture is locked, ticket generation becomes safer. The AI agent is no longer asked, “What structure should this feature use?” It is asked, “Implement this feature inside the structure already chosen.” That is a much more reliable form of AI execution.

---

## 4. TRUST AND PROTECTION LAYER  
### Security and Access Control Specification  
*(Speaks to Client, Developer, AI Agent, and Users at the same time)*

### Why this step is essential

Many AI-generated websites look complete while remaining unsafe. Login works, dashboards open, and buttons are hidden from unauthorized users. But real security is not an interface decision. Real security is enforced by backend rules and database rules. If this layer is skipped, the website may satisfy a demo and still fail the people who depend on it.

### Who this step speaks to

- **Users:** need protection of their data and accounts  
- **Client:** needs business-safe access rules and admin control  
- **Developer:** must convert access expectations into enforceable system rules  
- **AI Agent:** must implement those rules in FastAPI and Supabase, not only in React UI state

### How this information is derived

Some security decisions are technical and belong to the developer.  
Some must be asked directly of the client, because only the client knows the business meaning of access.

### Client-derived security questions the developer should ask

These questions should be treated as required intake, not optional polish:

- Who can create an account, and how?  
- What user roles exist in the business?  
- What can each role view, create, edit, or delete?  
- Which actions are admin-only?  
- Which data is owned by a single user and must remain private to that user?  
- Are there staff or operator roles between normal users and full admin?  
- What should happen when access is denied?  
- What account deletion or data removal expectations exist?  
- Which fields are sensitive and must never be exposed broadly?

### What the security specification must define, explained fully

**Authentication method**  
How identity is established, for example Supabase Auth with email and password, magic link, or another approved method.

**Roles and permissions**  
The formal map of role versus allowed action. This becomes the source of truth for both backend checks and database policies.

**Backend authorization**  
How FastAPI verifies that the current identity is allowed to perform the requested action.

**Row Level Security**  
How Supabase policies ensure that even direct data access respects ownership and role boundaries.

**Token handling**  
How session tokens are stored, sent, refreshed, and invalidated.

**Input validation rules**  
What the system accepts and rejects before business logic runs.

**Admin-only actions**  
Operations that must never be available to ordinary users, regardless of what the interface shows.

**User-owned data rules**  
Clear statements such as: a user can edit only their own profile; a user can view only their own orders; a user cannot list other users’ private records.

### Example of why this matters

If an admin page is merely hidden in the React app, a knowledgeable person may still call the backend endpoint directly.  
If the backend and Supabase policies both deny that action, the system remains protected.

Security is therefore not a visual task. It is a product trust task.

---

## 5. INTERFACE AND CONNECTION LAYER  
### Frontend and Integration Specification  
*(Speaks mainly to Developer and AI Agent; protects Client and Users through consistency)*

### Why this step is essential

A website is experienced as one product only when its interface and its connections behave consistently. If each page is generated with a different visual logic, or each integration invents its own request format, the project becomes fragmented even when individual features work.

This document has two halves, and both are required:

1. Frontend definition  
2. Integration definition

Excluding either half breaks the workflow. Frontend without integration produces screens that do not reliably connect. Integration without frontend standards produces connected systems that feel unfinished and inconsistent.

### Who this step speaks to

- **Developer:** defines the standards and reviews deviations  
- **AI Agent:** implements screens and integrations according to those standards  
- **Client:** receives a coherent product rather than a patchwork of generated pages  
- **Users:** navigate a system that behaves predictably across states and actions

### A. Frontend section — what must be defined and why

**Color palette**  
Locks visual identity so generated pages do not drift into random styling.

**Typography**  
Keeps hierarchy readable and consistent across the website.

**Spacing system**  
Prevents one page from feeling dense while another feels empty or uncontrolled.

**Buttons, inputs, and cards**  
Shared component behavior so users do not have to relearn basic interaction patterns on every page.

**Navigation**  
Defines how users move through the product and how active states are shown.

**Loading, empty, error, and success states**  
Forces every major interaction to handle real-world conditions, not only the happy path.

**Responsive behavior**  
Ensures the website remains usable across device sizes.

**Accessibility basics**  
Protects real users who rely on clearer structure, labels, and keyboard interaction.

### B. Integration section — what must be defined and why

**API endpoints**  
The official list of backend routes the frontend is allowed to depend on.

**Request and response formats**  
Exact contracts so React and FastAPI exchange data without guesswork.

**Authentication headers**  
How protected requests prove identity.

**Supabase client usage rules**  
When the frontend may talk to Supabase directly, and when it must go through FastAPI instead.

**Payment, storage, notification, or analytics services**  
Any external system must be named and constrained before implementation begins.

**Error response structure**  
A shared way to communicate failure so UI handling remains uniform.

**Retry behavior and limits**  
Prevents hidden runaway requests and unclear failure loops.

### Example contract the AI agent should expect

Rather than allowing the AI to invent a booking request, the integration spec should define something like:

- Endpoint: /api/bookings
- Method: POST
- Auth: Bearer token required
- Body fields: service identifier, date, time, payment reference
- Success response: booking identifier, confirmed status, message

With that contract in place, frontend, backend, validation, and error handling can all be generated against one stable definition.

---## 6. EXECUTION LAYER — THE MOST CRITICAL STAGE  
### Feature Ticket List  
*(This is the stage that turns planning into controlled production)*

### Why this stage is the most crucial

All previous documents gather truth, structure, protection, and consistency.  
This stage decides whether those documents become a finished website.

If tasking is vague, AI generation becomes broad and unstable.  
If tasking is precise, AI generation becomes measurable and reviewable.

This is where the workflow becomes executable.

### Who this stage speaks to

- **Client:** benefits because delivery becomes visible as completed capabilities rather than abstract progress  
- **Developer:** uses tickets to control scope, sequence, and review  
- **AI Agent:** receives one bounded unit of work at a time  
- **Users:** eventually experience completed flows that were tested against clear acceptance criteria

### How tickets are derived

Tickets are not invented from imagination. They are extracted from:

1. PRD capabilities and flows  
2. Architecture boundaries  
3. Security rules  
4. Frontend and integration standards

Each ticket should be small enough that an AI agent can implement it without reopening major product decisions.

### What every feature ticket must contain, explained fully

**Feature name**  
A clear title for the unit of work.

**Task description**  
What is being built in practical terms.

**Acceptance criteria**  
The conditions that must be true before the ticket is considered done. Without this, nobody can objectively judge success.

**Dependencies**  
What must already exist before this ticket should start. This prevents the AI agent from inventing missing foundations.

**Priority**  
The order of execution relative to other tickets.

**Relevant API changes**  
Whether new or modified endpoints are required.

**Relevant database changes**  
Whether schema or policy changes are required.

**Testing notes**  
How the ticket will be verified in local and Docker environments.

---

### Example Ticket 1 — User Registration

**Feature name:** User registration

**Task description:**  
Create the email registration flow for new users in the React frontend and supporting backend/Supabase path.

**Acceptance criteria:**
- User can enter name, email, and password.
- Invalid email format is rejected with a clear message.
- Weak passwords are rejected according to the project rule.
- Duplicate email addresses return a clear, non-technical error.
- Successful registration creates the auth identity and linked profile record.
- Loading state prevents duplicate submissions.
- Failure messages are visible and understandable.
- Successful registration routes the user into the next approved step of the product flow.

**Dependencies:**
- Supabase Auth configured
- Profiles table created
- Validation rules defined in the security and integration documents
- Auth state handling ready in the frontend architecture

This ticket is executable because the AI agent does not need to invent the meaning of registration. It only needs to implement a defined outcome.

---

### Example Ticket 2 — Protected Profile Read

**Feature name:** View own profile

**Task description:**  
Allow an authenticated user to view only their own profile data through the approved application path.

**Acceptance criteria:**
- Unauthenticated users cannot access the profile resource.
- Authenticated users can read their own profile fields as defined in the PRD.
- Authenticated users cannot read another user’s profile through the same endpoint or query.
- Frontend shows loading and error states correctly.
- Backend and/or Supabase RLS enforce ownership; UI hiding alone is not accepted as completion.

**Dependencies:**
- Registration/login tickets completed
- Session handling implemented
- Profiles schema available
- Security rules for user-owned data already documented

This ticket shows why acceptance criteria and dependencies matter. Without them, the AI agent might create a profile page that works visually while remaining insecure.

---

## 7. FULL ROLE MAP — HOW THE WHOLE WORKFLOW APPLIES TO EACH PARTY

### Client
- Provides the true product intention.
- Answers structured questions about users, features, roles, admin power, and MVP limits.
- Approves scope boundaries so the project does not expand silently during generation.
- Receives progress as completed tickets tied to real website capabilities.

### Users
- Represented in the PRD through roles and flows.
- Protected by the security specification.
- Served by consistent frontend behavior and reliable integrations.
- Ultimately validate whether the finished website is usable and trustworthy.

### Developer
- Extracts client truth through proposed questions.
- Translates that truth into PRD, architecture, security, frontend/integration standards, and tickets.
- Guards the stack and rejects uncontrolled AI redesign.
- Reviews each generated ticket against the documents before allowing the next step.

### AI Agent
- Does not invent the product from a one-line prompt.
- Consumes locked documents as operating constraints.
- Executes one ticket at a time.
- Returns implementation that can be tested against acceptance criteria.
- Supports later proof by making failures and successes attributable to specific tickets and rules.

---## 8. END-TO-END EXECUTION SEQUENCE FOR DEODINI BRAINBOX

1. Collect raw client requirements.  
2. Developer issues structured clarification questions.  
3. Write the Product Requirements Document.  
4. Convert approved product intent into the Technical Architecture Document.  
5. Define Security and Access Control rules, including client-derived role decisions.  
6. Define Frontend and Integration standards for the locked stack.  
7. Break the system into a Feature Ticket List.  
8. AI agent implements one ticket at a time.  
9. Developer reviews the output against all governing documents.  
10. Test in local and Docker environments.  
11. Record what worked into proven pattern storage and what failed into failed pattern storage.  
12. Only after repeated success should this raw workflow be treated as proven.

---

## 9. OPERATING RULE FOR FUTURE READERS

This file must remain understandable without hidden context.  
Anyone reading it later — human operator or AI agent — should be able to understand:

- why the workflow exists,
- who each step serves,
- how information is obtained,
- what must be defined before coding,
- and how execution is supposed to happen through tickets.

This is not merely a checklist.  
It is a proposed operating system for building fullstack websites with AI under controlled conditions inside DEODINI BRAINBOX.

---
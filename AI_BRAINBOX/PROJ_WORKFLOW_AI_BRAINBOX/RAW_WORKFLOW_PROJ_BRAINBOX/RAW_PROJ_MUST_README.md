# RAW_WORKFLOW_PROJ_BRAINBOX.md

**Status:** Raw — adapted concept, not yet tested against a live build. Subject to revision once trialed on an actual fullstack website project.

**Source concept:** Adapted from an external article on pre-build planning for AI-assisted app development. Reworded and restructured here for a fullstack website context (frontend + backend + database), rather than the original's mobile-app framing.

---

## Core Principle

AI coding tools produce inconsistent, hard-to-maintain output when they're forced to invent product decisions mid-build. Vague, single-line prompts ("build me a booking site") leave the AI guessing at data models, UI patterns, and permission rules — and those guesses drift with every new prompt, leading to mismatched styling, shifting schemas, inconsistent API shapes, and authorization gaps between screens.

The fix isn't better prompting — it's giving the AI a stable blueprint before any code is generated, so it has fewer decisions left to invent.

---

## Pre-Build Document Set

Five documents, drafted before serious development begins:

### 1. Product Requirements Document (PRD)
Defines what the site does, who it's for, and why — before any tech stack decisions. Should cover: problem statement, target users, user roles, core features, primary user flows, MVP scope boundaries (explicitly stating what's *out* of scope for v1), and success criteria. A vague one-liner produces a vague build; concrete role-based flows ("visitors can browse, registered users can checkout, admins can manage inventory") give the AI something real to reason against.

### 2. Technical Architecture Document
Locks in how the site is actually built, so every feature follows the same pattern instead of each prompt reinventing structure. Should define: full stack choice (frontend framework, backend framework, database), folder/project structure, state management approach, routing, database schema, API design conventions, file storage, environment config, third-party services, error handling, and logging approach.

### 3. Security & Access Control Specification
Defines who can do what — and critically, enforced at the backend, not just hidden in the UI. A user shouldn't be able to hit an admin API route just because the admin button isn't visible to them client-side. Should define: auth method, user roles, per-role permissions (explicit lists — "a user can edit their own profile," "an admin can manage all users"), backend authorization rules, token handling, input validation, and sensitive-data handling.

### 4. Frontend & Integration Specification
Keeps the site visually and technically consistent across every page, and defines exactly how external services are wired in — rather than leaving the AI to guess API shapes each time. Frontend side: color palette, typography, spacing system, component patterns (buttons, cards, inputs), loading/empty/error states, responsive behavior. Integration side: exact API endpoint contracts (method, auth header, request body shape, success/error response shape), payment provider, storage provider, notification service.

### 5. Feature Ticket List
Breaks the full site into small, scoped implementation tasks rather than one massive "build the whole thing" prompt. Each ticket: feature name, task description, acceptance criteria, dependencies, priority, relevant API/DB changes, testing notes. Small, single-purpose tickets consistently produce cleaner AI-generated code than broad, multi-feature prompts.

---

## Workflow Order

1. Collect raw requirements
2. Draft Product Requirements Document
3. Draft Technical Architecture Document
4. Draft Security & Access Control Specification
5. Draft Frontend & Integration Specification
6. Break scope into Feature Ticket List
7. Build one feature/ticket at a time
8. Review generated code
9. Test
10. Fix issues before considering the feature done

---

## Adaptation Notes for This Project

- This is a **raw** import — needs to be cross-checked against existing DOB/FQ workflow governance before being treated as binding.
- Naming/format should be reconciled with existing PROJ subsystem conventions once reviewed.
- Once trialed on an actual build cycle, promote validated parts to `PROVEN_PATTERN_PROJ_BRAINBOX.md`; anything that fails in practice goes to `FAILED_PATTERN_PROJ_BRAINBOX.md` per the existing retention rule (nothing is discarded, only reclassified).

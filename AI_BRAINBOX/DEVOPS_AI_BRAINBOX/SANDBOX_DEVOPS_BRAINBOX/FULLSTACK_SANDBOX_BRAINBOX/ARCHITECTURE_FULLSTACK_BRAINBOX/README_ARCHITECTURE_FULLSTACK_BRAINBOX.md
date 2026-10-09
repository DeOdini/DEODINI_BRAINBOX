# README_ARCHITECTURE_FULLSTACK_BRAINBOX

**STATUS:** [ACTIVE - CANONICAL NAVIGATION]
**PARENT:** `FULLSTACK_SANDBOX_BRAINBOX/`
**CURRENT DOMAIN:** Fullstack Architecture Applications
**PURPOSE:** Hold project-specific architecture evaluation, choices, adaptation, implementation, and validation; keep generic architecture knowledge in Skills.
**MENTAL MODEL:** SKILLS = what an architecture pattern generally is; FULLSTACK = how a specific application evaluates and applies it.
**GOVERNED BY:** Governance Evidence, Reference, Naming, and Ticketing; Fullstack Sandbox authority.
**CANONICAL SOURCE:** Frozen V003 Specification §§8 and 11; V003-P07; V003-M10.
**APPLIES TO:** Architecture choices and application records in Fullstack builds.
**LAST VERIFIED:** 2026-10-09

## Authoritative and local tree

```text
ARCHITECTURE_FULLSTACK_BRAINBOX/
|-- README_ARCHITECTURE_FULLSTACK_BRAINBOX.md
|-- STATIC_SITE_ARCH_BRAINBOX/ [.gitkeep; EMPTY]
|-- SPA_ARCH_BRAINBOX/ [.gitkeep; EMPTY]
|-- SSR_ARCH_BRAINBOX/ [.gitkeep; EMPTY]
|-- JAMSTACK_ARCH_BRAINBOX/ [.gitkeep; EMPTY]
|-- MONOLITH_ARCH_BRAINBOX/ [.gitkeep; EMPTY]
|-- MODULAR_MONOLITH_ARCH_BRAINBOX/ [.gitkeep; EMPTY]
|-- CLIENT_SERVER_ARCH_BRAINBOX/ [.gitkeep; EMPTY]
|-- MICROSERVICES_ARCH_BRAINBOX/ [.gitkeep; EMPTY]
|-- SERVERLESS_ARCH_BRAINBOX/ [.gitkeep; EMPTY]
|-- EVENT_DRIVEN_ARCH_BRAINBOX/ [.gitkeep; EMPTY]
|-- API_FIRST_ARCH_BRAINBOX/ [.gitkeep; EMPTY]
`-- ARCH_DECISIONS_BRAINBOX/ [.gitkeep; EMPTY]
```

## Scope and population state

The tree contains only the application branches approved in frozen Specification §11. These branches are structurally present and empty. M10 did not invent a static-site, SPA, SSR, Jamstack, monolith, microservices, serverless, event-driven, API-first, or other application choice.

The legacy RAW workflow's assumed React/TypeScript + FastAPI + Supabase/PostgreSQL + Docker stack remains an unverified workflow assumption. It is not a project architecture decision. The preset's Supabase/FastAPI authentication example is illustrative source material, not an implemented application.

No architecture decision record is populated. `ARCH_DECISIONS_BRAINBOX/` is an empty placeholder pending evidence-backed, project-specific decisions.

## Canonical pattern relationship

Generic principles, tradeoffs, and reusable evaluation guidance belong in [Skills Architecture Patterns](../../../../../AI_BRAINBOX/SKILLS_AI_BRAINBOX/PATTERNS_SKILLS_BRAINBOX/ARCHITECTURE_PATTERNS_SKILLS_BRAINBOX/). At M10 verification, that Skills destination contained only `.gitkeep`; no general architecture pattern record was copied or claimed populated.

When application evidence exists, the Fullstack application record must reference the canonical Skills pattern record. A Skills pattern may reference a Fullstack application, but must not duplicate its project-specific decision content.

## Related domains and references

- [Fullstack Sandbox](../README_FULLSTACK_SANDBOX_BRAINBOX.md)
- [Workflows](../WORKFLOWS_FULLSTACK_BRAINBOX/README_WORKFLOWS_FULLSTACK_BRAINBOX.md)
- [Orchestration](../ORCHESTRATION_FULLSTACK_BRAINBOX/README_ORCHESTRATION_FULLSTACK_BRAINBOX.md)
- [Skills architecture-pattern destination](../../../../../AI_BRAINBOX/SKILLS_AI_BRAINBOX/PATTERNS_SKILLS_BRAINBOX/ARCHITECTURE_PATTERNS_SKILLS_BRAINBOX/)
- [Frozen V003 Specification](../../../../../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md), §11
- [V003 Origin Conversation](../../../../../V003_VERSION_UPGRADE_BRAINBOX/V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md)
- [Governance Reference](../../../../../GOVERNANCE_BRAINBOX/REFERENCE_GOV_BRAINBOX.md)
- [M10 ticket](../../../../../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_PHASE02_MIGRATION_TICKETS_BRAINBOX.md)
- [Living migration map](../../../../../VERSION_HISTORY_BRAINBOX/V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md)

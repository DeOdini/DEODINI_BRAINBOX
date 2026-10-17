# README_ARCHITECTURE_FULLSTACK_BRAINBOX

**STATUS:** [ACTIVE - CANONICAL NAVIGATION]
**PARENT:** `FULLSTACK_SANDBOX_BRAINBOX/`
**CURRENT DOMAIN:** Fullstack Architecture Applications
**PURPOSE:** Hold project-specific architecture evaluation, choices, adaptation, implementation, and validation; keep generic architecture knowledge in Skills.
**MENTAL MODEL:** SKILLS = what an architecture pattern generally is; FULLSTACK = how a specific application evaluates and applies it.
**GOVERNED BY:** Governance Evidence, Reference, Naming, and Ticketing; Fullstack Sandbox authority.
**CANONICAL SOURCE:** Frozen V003 Specification §§8 and 11; V003-P07; V003-M10.
**APPLIES TO:** Architecture choices and application records in Fullstack builds.
**LAST VERIFIED:** 2026-10-17 — Codex B01 physical tree, placeholder-state, and reference checks; no architecture choice or runtime behavior was tested.

## Canonical local tree — two descendant levels

Current navigation snapshot; physical/population tags follow [Tree and status governance](../../../../../GOVERNANCE_BRAINBOX/TREE_AND_STATUS_GOV_BRAINBOX.md). This local view shows every direct child and each directory child’s direct children. For a deeper path, open the corresponding child README; consult the root README for the complete tree.

```text
ARCHITECTURE_FULLSTACK_BRAINBOX/ [PRESENT · POPULATED]
├── API_FIRST_ARCH_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── ARCH_DECISIONS_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── CLIENT_SERVER_ARCH_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── EVENT_DRIVEN_ARCH_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── JAMSTACK_ARCH_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── MICROSERVICES_ARCH_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── MODULAR_MONOLITH_ARCH_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── MONOLITH_ARCH_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── SERVERLESS_ARCH_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── SPA_ARCH_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── SSR_ARCH_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── STATIC_SITE_ARCH_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
└── README_ARCHITECTURE_FULLSTACK_BRAINBOX.md [PRESENT]
```

## Current-tree reference

The current physical tree is documented in the canonical two-descendant-level local tree above. The complete project tree is maintained only in the root README.

## Scope and population state

The tree contains the 11 architecture application branches approved in frozen Specification §11 plus the `ARCH_DECISIONS_BRAINBOX/` register. Each of these 12 directories is physically present with only a zero-byte `.gitkeep` marker and is therefore `[PRESENT · STUB]` under Tree and Status Governance. M10 did not invent a static-site, SPA, SSR, Jamstack, monolith, microservices, serverless, event-driven, API-first, or other application choice.

The legacy RAW workflow's assumed React/TypeScript + FastAPI + Supabase/PostgreSQL + Docker stack remains an unverified workflow assumption. It is not a project architecture decision. The preset's Supabase/FastAPI authentication example is illustrative source material, not an implemented application.

No architecture decision record is populated. `ARCH_DECISIONS_BRAINBOX/` contains only a zero-byte `.gitkeep` marker and remains a structural stub pending evidence-backed, project-specific decisions.

## Canonical pattern relationship

Generic principles, tradeoffs, and reusable evaluation guidance belong in [Skills Architecture Patterns](../../../../../AI_BRAINBOX/SKILLS_AI_BRAINBOX/PATTERNS_SKILLS_BRAINBOX/ARCHITECTURE_PATTERNS_SKILLS_BRAINBOX/). At M10 verification, that Skills destination contained only `.gitkeep`; no general architecture pattern record was copied or claimed populated.

When application evidence exists, the Fullstack application record must reference the canonical Skills pattern record. A Skills pattern may reference a Fullstack application, but must not duplicate its project-specific decision content.

## Related domains and references

The frozen Specification defines the approved application branches and boundaries. The Origin Conversation supplies decision-history context, Governance Reference supplies the canonical-ownership and reference-purpose rules, and the M10 ticket plus living migration map preserve source classification and migration dispositions; none of these references establishes a current architecture selection.

- [Fullstack Sandbox](../README_FULLSTACK_SANDBOX_BRAINBOX.md)
- [Workflows](../WORKFLOWS_FULLSTACK_BRAINBOX/README_WORKFLOWS_FULLSTACK_BRAINBOX.md)
- [Orchestration](../ORCHESTRATION_FULLSTACK_BRAINBOX/README_ORCHESTRATION_FULLSTACK_BRAINBOX.md)
- [Skills architecture-pattern destination](../../../../../AI_BRAINBOX/SKILLS_AI_BRAINBOX/PATTERNS_SKILLS_BRAINBOX/ARCHITECTURE_PATTERNS_SKILLS_BRAINBOX/)
- [Frozen V003 Specification](../../../../../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md), §11
- [V003 Origin Conversation](../../../../../V003_VERSION_UPGRADE_BRAINBOX/V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md)
- [Governance Reference](../../../../../GOVERNANCE_BRAINBOX/REFERENCE_GOV_BRAINBOX.md)
- [M10 ticket](../../../../../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_PHASE02_MIGRATION_TICKETS_BRAINBOX.md)
- [Living migration map](../../../../../VERSION_HISTORY_BRAINBOX/V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md)


---

## Independent verification status — 2026-10-09

V003-M10 independently verifies **PASS**. All 12 architecture application branches remain structurally present and empty; retained stack assumptions were not promoted into architecture decisions.

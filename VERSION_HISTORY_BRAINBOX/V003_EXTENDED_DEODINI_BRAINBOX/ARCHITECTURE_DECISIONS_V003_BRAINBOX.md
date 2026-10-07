# ARCHITECTURE_DECISIONS_V003_BRAINBOX

**Status:** [ACTIVE] — concise V003 decision history  
**Authority:** Rationale and decision provenance only  
**Canonical target:** `../../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md`  
**Historical evidence:** `../../V003_VERSION_UPGRADE_BRAINBOX/V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md`

## Purpose and authority boundary

This record explains why selected V003 architecture decisions were made. It is not a second V003 specification.

- The **V003 Specification** defines what V003 is: the current architecture target, naming, requirements, and migration constraints.
- This **Architecture Decisions** record explains why the target took its current form, including concise rationale and superseded alternatives.
- The **Origin Conversation** preserves the chronological discussion and is the historical source when decision development or ambiguity needs review.

When this record and the current Specification appear inconsistent, the Specification defines the current target. Consult the Origin Conversation for historical context; do not infer an unrecorded target from superseded discussion.

## Decisions

### V003-ADR-001 — Separate target specification from decision history

**Status:** Adopted  
**Decision:** Keep the canonical V003 target in `V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md`. Use this file only for concise decision summaries, rationale, superseded alternatives, status, and references to the Specification and Origin Conversation.

**Rationale:** A single current-target authority prevents duplicate architecture descriptions from drifting or being mistaken for competing specifications. A concise history retains why choices were made without copying the full target tree.

**Superseded alternative:** Reproduce the full V003 architecture tree or duplicate the Specification here for standalone completeness. This approach is excluded by the V003-P03 authority reconciliation; it is not a current target.

**References:**

- Canonical target: [`V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md`](../../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md), especially §24, “Version History,” and §25, “Governance Rule Set.”
- Historical basis and P03 ticket: [`V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md`](../../V003_VERSION_UPGRADE_BRAINBOX/V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md), Phase 01 ticket register and `V003-P03` ticket.

## Maintenance rule

Add a decision only when supported by the Specification, the Origin Conversation, or explicit Operator approval. Record the decision and rationale briefly, label the status, identify superseded alternatives as historical, and link to the source. Do not duplicate full architecture trees, file specifications, or migration instructions here.
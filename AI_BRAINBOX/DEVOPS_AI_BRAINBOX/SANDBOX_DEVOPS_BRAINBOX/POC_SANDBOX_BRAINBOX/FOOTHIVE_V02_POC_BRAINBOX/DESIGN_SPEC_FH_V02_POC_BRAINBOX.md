# DESIGN_SPEC_FH_V02_POC_BRAINBOX

**PARENT:** FOOTHIVE_V02_POC_BRAINBOX/
**CURRENT DOMAIN:** FootHive V02 visual and interaction design
**PURPOSE:** Separate the approved design direction from unapproved implementation-level values and unavailable source evidence.
**MENTAL MODEL:** The concepts guide future design work; they are not source files, pixel specifications, or functioning website components.
**GOVERNED BY:** Active Documentation, Naming, Reference, Tree and Status, Evidence, Security, and Ticketing Governance.
**CANONICAL SOURCE:** Operator-approved RECT-06 directive and the DR-01/DR-02/DR-03 intake manifest.
**REFERENCED BY:** FootHive V02 PRD, ticket register, project README, and project report.
**REFERENCES:** [PRD](PRD_FH_V02_POC_BRAINBOX.md), [visual-reference manifest](ASSETS_FH_V02_BRAINBOX/README_ASSETS_FH_V02_BRAINBOX.md), and [project conversation](CONVO_FH_V02_POC_BRAINBOX.md).
**STATUS:** [APPROVED DESIGN DIRECTION; TECHNICAL SPECIFICATION DRAFT / INCOMPLETE]
**LAST VERIFIED:** 2026-10-25 - available project records and inline-reference manifest reviewed; independent review pending.
**VERIFIER:** Codex - documentation and source availability only; no design binary or rendered application inspected.
**APPLIES TO:** Future FootHive V02 design planning.

## Purpose and authority

This record translates only the approved high-level direction into a design handoff boundary. It does not claim that the design is fully specified or authorize application implementation. Requirement ownership and product behavior remain in the [V02 PRD](PRD_FH_V02_POC_BRAINBOX.md).

## Approved design direction

### Visual references

- **DR-01 - Creatix Inspiration:** External inspiration for broad visual direction only. Creatix branding, copy, people, and imagery are not FootHive assets and must not be copied as project content.
- **DR-02 - FootHive Dark:** Operator-approved dark-theme concept.
- **DR-03 - FootHive Light:** Operator-approved light-theme concept retaining the original FootHive brand direction.

All three are currently conversation-visible references represented by the intake manifest. Their original image binaries, file-level hashes, dimensions, embedded metadata, and usage permissions are unavailable. No exact measurements are inferred from the displayed concepts.

### Shared composition and themes

- Use one shared composition for the FootHive Dark and FootHive Light presentations.
- The dark concept uses dark surfaces with green accent direction.
- The light concept uses light/warm surfaces with orange accent direction.
- Provide one circular, single-tap theme control.
- Keep product facts and structure consistent between themes.

These are visual-direction statements, not final color tokens or component contracts.

### Product presentation

The V02 PRD owns the approved twelve-product, single-homepage requirement and the non-clickable, presentation-only hero gallery. The design must distinguish gallery preview imagery from the separate product cards, whose destinations are approved Pinterest links. No separate View All Products route is planned. Any optional alternate product image on hover must have a usable touch and keyboard equivalent if retained.

### Sections and shared elements

The supplied direction supports planning a shared header/navigation, hero gallery, trust strip, product collection, brand story, notification area, footer, and theme control. Their final order, dimensions, content, transitions, and component boundaries remain proposed until a PRD 0.3 design refinement is reviewed.

## Technical decisions still proposed

Do not treat these as approved values:

- CSS tokens, color values, typography, font files, spacing scale, border radii, shadows, and icon set.
- Breakpoints, grid columns, image aspect ratios, object positioning, gallery interval, and animation duration.
- Theme default, persistence mechanism, and transition behavior.
- Product-card hover/focus behavior and gallery controls.
- Loading strategy, image optimization, and fallback assets.
- Any framework or build-tool change from the historical V01 static HTML/CSS/JavaScript architecture.

The original design binaries were unavailable, so there is no defensible source for pixel measurements, color sampling, font identification, or asset-level comparison.

## Accessibility and responsive design requirements

Responsive and accessible implementation is an approved quality requirement. Before coding, a separate design refinement must define measurable acceptance criteria for viewport behavior, keyboard focus, accessible names and state for the theme control, gallery pause/reduced-motion behavior, semantic structure, contrast, touch targets, and non-hover access to content. No accessibility audit or conformance certification is claimed here.

## Design asset boundary

The ASSETS directory presently contains the reference intake manifest only. No image binary is archived as a project asset. Do not substitute FootHive Iteration 01 images, extract inaccessible image details, infer usage permission, or claim that a theme is implemented.

## Required next design decisions

1. Obtain the three original image binaries and record their provenance and integrity if the Operator wants them archived.
2. Confirm product identities and approved product-specific imagery.
3. Refine the PRD's open behavior and accessibility requirements.
4. Prepare measurable layout and interaction specifications from accessible, authorized references.
5. Submit any material design variations for Operator approval before implementation.

## Related records

- [V02 PRD](PRD_FH_V02_POC_BRAINBOX.md)
- [V02 project README](README_FH_V02_POC_BRAINBOX.md)
- [V02 ticket register](TICKETS_FH_V02_POC_BRAINBOX.md)
- [V02 project report](REPORT_FH_V02_POC_BRAINBOX.md)
- [Reference intake manifest](ASSETS_FH_V02_BRAINBOX/README_ASSETS_FH_V02_BRAINBOX.md)
- [Documentation Governance](../../../../../GOVERNANCE_BRAINBOX/DOCUMENTATION_GOV_BRAINBOX.md)
- [Reference Governance](../../../../../GOVERNANCE_BRAINBOX/REFERENCE_GOV_BRAINBOX.md)

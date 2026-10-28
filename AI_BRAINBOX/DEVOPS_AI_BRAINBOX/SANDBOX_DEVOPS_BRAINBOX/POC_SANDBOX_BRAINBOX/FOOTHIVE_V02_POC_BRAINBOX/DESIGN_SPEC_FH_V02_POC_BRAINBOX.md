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


## DS-01-AMD-01 - P01-V02-FOUND-01 execution release - 2026-10-28

**Authority:** Operator-approved DS-01 Amendment 01; PRE-REC-01 PASS WITH CONDITIONS accepted; corrected handoff expressly released for Stage A registration and Stage B local implementation. Historical entries remain preserved. This amendment supersedes the earlier conflicting --color-* palette and component-mapping contract for this ticket.

**Approved semantic colors:**

| Token | Light | Dark |
|---|---|---|
| --fh-surface-page | #FAF8F4 | #111311 |
| --fh-surface-card | #FFFFFF | #1C201B |
| --fh-text-primary | #1A1A1A | #F4F3EE |
| --fh-text-secondary | #625C56 | #B9BEB4 |
| --fh-accent | #B3470F | #B6F53C |
| --fh-on-accent | #FFFFFF | #111311 |
| --fh-border-control | #80766C | #7C8774 |
| --fh-focus-ring | #B3470F | #B6F53C |

**Selectors and scope:** :root, :root[data-theme="light"] defines the fallback/light set; :root[data-theme="dark"] defines dark overrides. Definitions only: add exactly these eight namespaced properties per selector block near existing root variables in C:\Users\USER\FOOTHIVE_V02\css\styles.css. Preserve all legacy variables and declarations. No var(--fh-...) component migration, rendered-appearance change, HTML theme attribute, switch, persistence, system-preference behavior, typography, spacing or layout changes. Component migration and theme behavior are deferred. The fallback is not an eventual product-default decision.

**Acceptance:** Exact token/selector comparison; no pre-existing namespaced collisions or duplicates; original stylesheet recoverable byte-for-byte by removing only the inserted blocks; CSS-only application diff; git diff --check; approved contrast matrix recalculated (normal text >=4.5:1, large text >=3:1, applicable non-text controls/focus >=3:1); no browser-conformance claim from token arithmetic. Browser testing is optional here and may not make external analytics/form requests or uncontrolled artifacts.

**Preservation/preconditions:** Brainbox main at 3d4ffc60f1470672e8f1b85e7d966e07898be8c8; V02 v02/development and upstream at 43bbbea8325e3ec062baef7fd1724b5ea78bc6d0, source tree da62a65e683c24a39deb373c9e1c85ee32ecc896. Preserve current bytes of all three canonical documentation files and stylesheet in verified, non-overwriting private snapshots before editing. Maintain source/destination sizes, SHA-256 and timestamp in a custody manifest. Preserve HANDOFF.md at accepted current SHA-256 8b3a3bc5803152a08567c48f947e82b1bf89f917445b0bb6418fd734b69f4b9c and verify its existing private copy. Older SHA-256 33b3ea156667eb4b3823452ff3a08e132ab3867199d75b61cedbe880f7f94c0e is historical provenance; byte-for-byte continuity to that older checkpoint is not established.

**Ordered gates:** Complete Stage A and run python -B GOVERNANCE_BRAINBOX/validate_tree_status.py plus python -B -m unittest GOVERNANCE_BRAINBOX/test_validate_tree_status.py. Require qualified PASS/zero findings and 24 passing tests. Renew V02 preflight before Stage B. Verify snapshot integrity, HANDOFF hash, index/worktree scope and unchanged original V01 references afterward.

**Exclusions and STOP:** No other application files, private references, integration, Netlify, deployment, Git refs/configuration, staging, commits, pushes, PRs, merges, resets or publication. Stop without automatic remediation for mismatched branches/SHAs/upstream/hash, missing preservation copy, unexpected changed/staged/untracked files, token collision, material registration conflict, failed required validation or required out-of-scope changes.

**State at registration:** LOCAL EXECUTION AUTHORIZED; application implementation pending actual Codex execution evidence. Git publication NOT AUTHORIZED. Codex technical report -> Priority 1 ChatGPT independent verification -> Operator final implementation acceptance. This entry records execution release, not completion or independent acceptance.

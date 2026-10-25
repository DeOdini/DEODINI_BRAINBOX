# PRD_FH_V02_POC_BRAINBOX

**PARENT:** FOOTHIVE_V02_POC_BRAINBOX/
**CURRENT DOMAIN:** FootHive V02 product requirements
**PURPOSE:** Maintain the source-backed product scope and distinguish Operator-approved direction from proposals, open questions, and implementation work.
**MENTAL MODEL:** This is a planning record for a non-commercial showcase. It is not application code, a release specification, or implementation authorization.
**GOVERNED BY:** Active Documentation, Naming, Reference, Ticketing, Evidence, Tree and Status, Security, Versioning, and Promotion Governance.
**CANONICAL SOURCE:** Operator-approved RECT-06 execution directive, supplied 2026-10-25; historical context in the project conversation and bounded POST-V003 retrospective.
**REFERENCED BY:** FootHive V02 project README, design specification, ticket register, project report, and retrospective.
**REFERENCES:** Project conversation, DR-01/DR-02/DR-03 intake manifest, V01 retrospective source, and applicable Governance.
**STATUS:** [DRAFT - PRD 0.3 REFINEMENT IN PROGRESS; FINAL PRD ACCEPTANCE PENDING]
**LAST VERIFIED:** 2026-10-25 - source and status review by Codex; independent review pending.
**VERIFIER:** Codex - documentation and provenance checks only; no application behavior verified.
**APPLIES TO:** FootHive V02 project planning.

## Authority and approval states

This record consolidates the product direction expressly identified as the Operator's latest decisions in the RECT-06 directive. It does not convert earlier proposals into approvals or authorize implementation. The final PRD remains a draft until separately reviewed and accepted by the Operator.

Use these labels:

- **OPERATOR-APPROVED DIRECTION:** A decision expressly stated as approved in the RECT-06 directive.
- **PROPOSED / REFINE:** A requirement or implementation detail that still needs specification or approval.
- **OPEN / UNKNOWN:** Source material or a decision is not available or not established.
- **NOT AUTHORIZED:** Application coding, external service changes, release, and deployment remain outside this documentation ticket.

## Product vision and boundary

FootHive V02 is a premium, non-commercial footwear showcase and product-discovery experience. It is not an operating online store. The approved direction builds on the seven-product V01 identity while expanding the planned V02 presentation to twelve products.

No cart, checkout, payment processing, customer account system, fulfillment service, or custom commerce backend is authorized or implied by this PRD.

## Historical V01 baseline

The bounded historical report describes V01 at source revision 43bbbea8325e3ec062baef7fd1724b5ea78bc6d0 as a seven-product showcase: three Boots, two Classic Shoes, and two Runners. It records Pinterest product destinations, Google Forms notification signup, and GA4 as existing integrations at the time of that review. These are dated historical claims, not a current source or production recheck.

The report also records a reported 320px navigation wrap, sticky-header anchor overlap, accessibility/testing limitations, and a historically reported Netlify deployment. See the [bounded V02 retrospective](RETROSPECTIVE_FH_V02_POC_BRAINBOX.md) and its cited source. Do not present these observations as current measurements.

## Operator-approved product direction

| Requirement | Approved direction | Refinement boundary |
|---|---|---|
| Product and commercial scope | Premium, non-commercial footwear showcase. | Do not add commerce behavior. |
| Product count | Present the original seven V01 products plus five additional products, for a planned total of twelve. | Names, product facts, images, category assignments, and destinations for the five additions remain to be supplied or verified. |
| Homepage collection | Show all twelve product cards on the single homepage. | Layout, ordering, and responsive arrangement remain for design refinement. |
| Product destinations | Product links use approved Pinterest destinations. | Verify each URL against the authorized V01 source and approved V02 catalog before implementation. |
| Hero gallery | Automatic, presentation-only gallery. Gallery imagery and its preview imagery are non-clickable. | Timing, pause behavior, reduced-motion behavior, and keyboard/touch controls need accessible design refinement. |
| Product-card alternate image | Alternate-image hover behavior is optional. | Do not require hover-only information; mobile and keyboard behavior remain to be specified. |
| Separate collection route | Remove the separate View All Products feature. | The single homepage remains the collection presentation. |
| Community/social items | Remove Join Our Community and unapproved social icons. | Retain only explicitly approved destinations and controls; the Pinterest product links remain in scope. |
| Trust strip | Retain and truthfully redesign V01 trust-strip messaging. | Each number, superlative, or factual claim requires evidence; do not invent metrics. |
| Themes | Provide coordinated FootHive Dark and original-brand FootHive Light themes using a shared composition and one circular, single-tap theme switch. | Exact palette values, persistence, default theme, and transition behavior are not fixed here. |
| Quality | Responsive and accessible implementation is required. | Breakpoints, contrast, semantics, focus, motion, and assistive-technology acceptance criteria require specification before coding. |
| Development method | Decompose work as section -> batch -> atomic ticket, followed by verification and batch closeout. | Each execution ticket requires its own approval and scope. |

## Existing integrations

The historical V01 report identifies Pinterest links, Google Forms notification signup, and GA4. RECT-06 requires preservation of existing approved integrations, but this documentation task did not inspect the external application or confirm their current configuration. Preserve only integrations whose source, purpose, destination, privacy implications, and current authorization are verified in a later scoped ticket. Do not create new tracking, submission, or social behavior from this historical list.

## Proposed requirements for PRD 0.3 refinement

The following items are not complete acceptance criteria yet:

1. Approve the exact identities and evidence for the five additional products.
2. Approve the twelve-item order, categories, descriptions, images, alt text, and individual Pinterest destinations.
3. Specify gallery timing, pause or stop controls, reduced-motion behavior, and preview behavior.
4. Specify the optional product-image hover treatment and non-hover equivalents.
5. Define truthful trust-strip copy and the evidence required for each claim.
6. Reconcile approved integrations with the current V01 source and privacy requirements.
7. Define responsive layouts, interaction states, keyboard and screen-reader behavior, contrast targets, and visual acceptance criteria.
8. Define the theme switch's accessible name, state announcement, initial theme, persistence, and transition behavior.
9. Reconcile the historical ticket identifiers in the project ticket register without reusing or authorizing them implicitly.
10. Review the unavailable PRD 0.1/0.2 source drafts if the Operator supplies them.

## Earlier PRD drafts and source limits

RECT-06 refers to Priority 1 PRD drafts 0.1 and 0.2. No separate draft files or their full text were present in the repository or the accessible attachment texts inspected for this ticket. Their contents, authorship details, dates, and proposed requirements therefore remain **UNKNOWN / NOT VERIFIED**. This draft does not reconstruct them. The project report records this source limitation; any later supplied drafts should be preserved and compared as historical proposals.

## Acceptance boundary

This document is ready for independent documentation review, not final PRD acceptance. No FootHive source code, project branch, tag, dependency, live service, deployment, or external integration was changed or tested under RECT-06.

## Related records and authorities

- [FootHive V02 project README](README_FH_V02_POC_BRAINBOX.md)
- [FootHive V02 design specification](DESIGN_SPEC_FH_V02_POC_BRAINBOX.md)
- [FootHive V02 ticket register](TICKETS_FH_V02_POC_BRAINBOX.md)
- [FootHive V02 project report](REPORT_FH_V02_POC_BRAINBOX.md)
- [FootHive V02 retrospective](RETROSPECTIVE_FH_V02_POC_BRAINBOX.md)
- [Project conversation](CONVO_FH_V02_POC_BRAINBOX.md)
- [Visual-reference intake manifest](ASSETS_FH_V02_BRAINBOX/README_ASSETS_FH_V02_BRAINBOX.md)
- [Documentation Governance](../../../../../GOVERNANCE_BRAINBOX/DOCUMENTATION_GOV_BRAINBOX.md)
- [Naming Governance](../../../../../GOVERNANCE_BRAINBOX/NAMING_GOV_BRAINBOX.md)
- [Ticketing Governance](../../../../../GOVERNANCE_BRAINBOX/TICKETING_GOV_BRAINBOX.md)
- [Reference Governance](../../../../../GOVERNANCE_BRAINBOX/REFERENCE_GOV_BRAINBOX.md)
- [POST-V003 retrospective source](../../../../../POST_V003_MODIFICATIONS_BRAINBOX/POST_V003_MOD_REPORT_BRAINBOX.md), lines 196-255

# FootHive Project Trial — Mandatory Readme

**Issued by:** De O'Dini (Operator)  
**Applies to:** All agents working in `FOOTHIVE_PROJ_BRAINBOX/`  
**Status:** Trial documentation; website build has not started  
**Last reviewed:** 2026-09-28

## Purpose of this folder

This folder preserves the first recorded end-to-end test of the proposed `001DOC` fullstack workflow, adapted to a small, static FootHive footwear landing page. The trial uses a real public Upwork brief as its starting point, with the Operator role-playing the client. It is a workflow test and portfolio/spec exercise, not evidence of a paid client engagement or a completed website.

The trial's purpose is to document how the workflow gathers and locks the client's desired outcome, turns it into developer-owned specifications, obtains client confirmation before implementation, and preserves both successful methods and process failures. The target end state is a responsive, polished, single-page FootHive marketing site, with outbound Shopify shopping, email-interest capture, accessible product presentation, and a deployable handoff. The approved direction and tickets are in place; implementation and verification remain future work.

## Required reading and record order

1. Read this README for scope, current status, and open flags.
2. Read `CONVO_FH_BRAINBOX.md` as the chronological source record. It is 2,585 lines and contains the intake, specifications, confirmations, design-direction generation, and the final pre-build handoff point.
3. Read `PASSED_FH_BRAINBOX.md` for successful, evidence-backed process and confirmed decisions.
4. Read `FAILED_FH_BRAINBOX.md` for failures, corrections, and unresolved review flags.
5. Consult the source workflow at `../RAW_WORKFLOW_PROJ_BRAINBOX/FULLSTACK_RAW_BRAINBOX/001DOC_BYB5DOC_FLOW_STACK_BRAINBOX.md` and its companion interpretation at `../RAW_WORKFLOW_PROJ_BRAINBOX/FULLSTACK_RAW_BRAINBOX/FSTACK_MUST_README.md` when evaluating workflow alignment.
6. Treat `BUILD_REPORT_FH_BRAINBOX.md` as reserved for a later implementation/build report. It is currently empty; do not infer that a build has been completed.

The transcript is the historical source. These two classification files summarize its evidence and should not silently rewrite, replace, or contradict it. Preserve the distinction between a confirmed plan/design phase and an executed website build.

## Trial workflow and procedure

The trial followed the adapted 001DOC sequence:

1. Use a new project based on the Upwork footwear landing-page brief.
2. Prepare proposal and capture the client's desired outcome in a confirmed PRD.
3. Derive the static-site technical architecture from the PRD; obtain confirmation.
4. Derive scaled security/access and frontend/integration specifications; obtain confirmation.
5. Confirm pre-ticket constants (wireframes, user flows, tree, sitemap) and T01–T12 feature tickets.
6. Present visual directions using the real project assets, let the client select a baseline, and record choices and adjustments.
7. Only then begin the ticketed build, verify at checkpoints, and classify implementation outcomes. Step 7 has not begun.

The key process correction is that initial discovery should be a light first engagement. The workflow-specific PRD intake should gather desired-outcome details once, and the PRD should synthesize them into the client-facing contract. Later architecture, security, frontend, and ticket documents are developer synthesis from that contract; the client confirms alignment and is asked again only about genuine gaps or change requests.

## Current confirmed position

- PRD v0.1, static architecture, scaled security, frontend/integration, pre-ticket constants, and T01–T12 were confirmed in the transcript.
- Direction B, **Streetwear-adjacent**, was chosen as the visual baseline. The website build did not start; the transcript ends with the next action stated as T01.
- The intended page is a single static HTML/CSS/JavaScript page on Netlify. Shopify is an outbound commerce destination; Google Form/Sheet handles notification signups; GA4 is the only planned analytics integration. No app backend, database, authentication, cart, or extra page is in the approved v1 architecture.
- Product showcase: 6–12 mixed-category items (boots, classics, sneakers). Final product selection and product copy remain build-stage work.
- Brand baseline recorded in the conversation: FootHive, “BUILT TO LAST,” `#1A1A1A` and `#D2691E`; the frontend spec adds `#8A8A8A` and light surfaces.

## Folder map and source assets

- `CONVO_FH_BRAINBOX.md` — chronological conversation and approvals.
- `PASSED_FH_BRAINBOX.md` — confirmed workflow passes and decisions.
- `FAILED_FH_BRAINBOX.md` — observed failures and outstanding flags.
- `BUILD_REPORT_FH_BRAINBOX.md` — reserved; currently zero bytes.
- `FOOTHIVE LOGO + DARK MODE/foothive-logo.svg` and `foothive-logo-dark.svg` — supplied light/dark logo variants.
- `FOOTHIVE BOOTS IMAGES/foothive-boot-images.md` — 9 western/specialty boot images.
- `FOOTHIVE CLASSIC SHOES IMAGES/foothive-classic-images.md` — 9 classic shoe images.
- `FOOTHIVE SNEAKER IMAGES/foothive-sneaker-images.md` — 4 sneaker/runner images.
- `FOOTHIVE TIMBERLAND IMAGES/foothive-timberland-images.md` — 10 Timberland-style boot images; this filename's casing was normalized on 2026-09-28.
- `DIRECTION A & B IMAGES/FZxXm (DIRECTION A).jpg` — Direction A, editorial/minimal premium; not selected.
- `DIRECTION A & B IMAGES/37n4T (DIRECTION B).jpg` — Direction B, streetwear-adjacent; selected by the client.

The conversation documents the design images at lines 2502–2526 and the client's Direction B decision at lines 2534–2560. The source catalogs and logo files are the asset-location references; the actual image files are stored alongside each catalog.

## Open flags found in the 2026-09-28 audit

These were identified by checking the current local folder and image files. They were not all recorded in the original transcript review. They are recorded for the Operator's review and must be resolved before relevant assets or mockup content ship in a live build:

1. **Third-party marks:** multiple files in `FOOTHIVE TIMBERLAND IMAGES/` visibly show Timberland tree marks, product tags, or packaging (confirmed visually in `image02.png`, `image04.png`, `image05.png`, `image08.png`, `image13.png`, `image15.png`, `image16.png`, and `image19.png`). The catalog describes these as brand-neutral/no-third-party logos. That description conflicts with the images. Do not treat the set as cleared for public use; Operator must decide whether to replace, exclude, crop, or otherwise clear those images.
   The same concern applies to `FOOTHIVE SNEAKER IMAGES/navy-tan-stripe.png`, which visibly uses Adidas's three-stripe mark, and `FOOTHIVE BOOTS IMAGES/winged-cross-studded-western-boot.png`, whose background includes third-party shop signage/branding. `FOOTHIVE BOOTS IMAGES/sunflower-embroidered-western-boot.png` also contains a visible `1/2` overlay/watermark. These assets need clearance, replacement, or exclusion before use.
2. **Catalog image links:** the four catalog Markdown files use relative prefixes `boot-images/`, `classic-images/`, `sneaker-images/`, and `images/`, but the corresponding image files are currently siblings of their catalog files, not in those subdirectories. The embedded previews therefore point to nonexistent paths as stored. The links have not been corrected.
3. **Direction B exceeds locked v1 scope/content:** the selected mockup depicts a cart icon, per-product prices, extra shop categories/pages, social-network icons, and “Easy Returns / 30-day returns” and product/material claims. The approved architecture excludes a cart and additional pages, and the conversation does not establish approval or evidence for all displayed claims. The client did specifically request keeping the product corner tags and fixing “Foote” to “FootHive”; those two requests are recorded separately in the pass log. Review all other mockup elements against the approved PRD/spec before implementation.
4. **Inventory count discrepancy:** the earlier conversation reports 42 files, while the current recursive local inventory contains 45 files. Current folder contents are the authority for implementation; reconcile the older count if a later audit requires exact historical accounting.
5. **Temporary destinations:** the Pinterest URL `https://pin.it/37MYm0GnG` was approved as a preview placeholder for both Shop and social links. The final Shopify destination and Instagram handle were still outstanding in the trial record; do not treat placeholders as production-ready values.

## Review standard for the build phase

Before T01, first obtain Operator direction on the open flags above where they affect build scope or asset use. Preserve the approved v1 boundaries: no cart, no invented reviews/claims, no added pages, and no unapproved scope expansion. Then execute the confirmed ticket sequence, one ticket at a time, and record actual verification evidence in the build report. Do not mark the workflow or site “proven” until implementation has been tested in practice.

---

**Revision note — 2026-09-28:** Drafted this README and the initial phase records from a full sequential reread of the 2,585-line conversation, local folder inventory, workflow references, four image catalogs, logo variants, and design-direction images. Normalized the Timberland catalog filename casing. No catalog links, product assets, or website files were changed.  
**Agent:** Codex  

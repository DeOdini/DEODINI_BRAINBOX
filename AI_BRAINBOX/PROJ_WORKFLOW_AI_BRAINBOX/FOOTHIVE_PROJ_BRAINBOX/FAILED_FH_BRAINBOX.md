# FootHive Trial — Failures, Corrections, and Review Flags

**Source:** `CONVO_FH_BRAINBOX.md` and local asset/folder review on 2026-09-28.  
**Record rule:** Keep the historical process failures separate from newly found audit flags. A mockup defect is not evidence that an unbuilt website has failed.

# **CLIENT BRIEF AND PRD EXECUTION**

## Historical failures and process lessons

### 1. Discovery and PRD intake were blurred

The initial request to use the full workflow structure to draft client questions resulted in a broad questionnaire before the PRD document was composed. The client then experienced the sequence as a “pre-PRD” followed by a PRD, even though the information was subsequently consolidated into PRD v0.1. The Operator clarified that the PRD should be the single client-facing desired-outcome capture, with architecture/security/frontend/ticket documents derived by the developer afterward and confirmed by the client. The Operator also recognized that the request to use the full structure contributed to the approach.

**Impact:** confusing labeling and a risk of asking the client the same ground twice.  
**Correction agreed in the conversation:** discovery is light; name the workflow steps; do one workflow-tailored PRD intake and synthesize it into one PRD; ask later only about real gaps or scope changes.  
**Disposition:** process lesson, corrected in planning; retest this approach on another project before calling it proven.

### 2. Image generation produced runaway text and incomplete delivery

The first image-generation attempt returned one image when two directions were requested and produced a long, broken text stream while generating. The Operator interrupted it. The agent acknowledged the output glitch and said the next attempt should return only the images. A later attempt to generate Direction A and Direction B separately again showed the typing/output problem; the Operator reported that it “STILL PERSISIT.” The client then supplied four generated images, from which the agent selected one per direction.

**Impact:** generation output was unreliable and required interruption, retry, and operator-supplied artifacts before a usable comparison could be presented.  
**Disposition:** unresolved tool reliability limitation; do not record the generation mechanism as a clean pass.

### 3. Initial asset-access status changed after upload

The agent first reported that actual product-image files were not available, only catalogs. After the Operator sent catalog images, the agent confirmed that image assets had been received and mapped. This was a valid state change, but the timeline matters: any later account of image use must distinguish the pre-upload limitation from the post-upload state.

### 4. Timberland catalog filename casing was inconsistent

The original local name `foothive-TIMBERLAND-images.md` differed in capitalization from the other catalog filenames and from the intended lowercase style. This was a cosmetic naming inconsistency, not evidence of missing data. It was corrected during this task to `foothive-timberland-images.md`; no catalog contents were changed.

### 5. What Not to Do — use product imagery with uncleared third-party branding or watermarks

The asset review found product-image candidates with visible third-party marks, branded tags or packaging, shop branding, or a watermark. Allowing these into the FootHive candidate asset set without explicit Operator clearance is a process failure, regardless of who supplied or located the files. Future agents must not source, select, or use product images showing third-party brands, logos, branded packaging, or watermarks unless the Operator has explicitly cleared them.

**Excluded from the FootHive website build:** the following paths are relative to `FOOTHIVE_PROJ_BRAINBOX/`:

- `FOOTHIVE TIMBERLAND IMAGES/image02.png` — visible Timberland marks, tags, or packaging.
- `FOOTHIVE TIMBERLAND IMAGES/image04.png` — visible Timberland tree mark.
- `FOOTHIVE TIMBERLAND IMAGES/image05.png` — visible Timberland tree mark.
- `FOOTHIVE TIMBERLAND IMAGES/image08.png` — visible Timberland tree mark/logo.
- `FOOTHIVE TIMBERLAND IMAGES/image13.png` — visible Timberland tree mark.
- `FOOTHIVE TIMBERLAND IMAGES/image15.png` — visible Timberland tree logo.
- `FOOTHIVE TIMBERLAND IMAGES/image16.png` — visible Timberland tree logo.
- `FOOTHIVE TIMBERLAND IMAGES/image19.png` — visible Timberland tree mark/tag and “Premium Quality” badge.
- `FOOTHIVE SNEAKER IMAGES/navy-tan-stripe.png` — visible Adidas three-stripe mark.
- `FOOTHIVE BOOTS IMAGES/winged-cross-studded-western-boot.png` — third-party shop branding/signage in the background.
- `FOOTHIVE BOOTS IMAGES/sunflower-embroidered-western-boot.png` — visible `1/2` watermark/overlay.

Do not use any of these images in mockups, the product grid, or the website unless the Operator explicitly clears them later. Keep the original image files and existing catalog contents intact; this record documents their exclusion without modifying either.

# **WEBSITE BUILDING EXECUTION**

## Phase state

**Not started.** The transcript ends with the agent waiting for authorization to start T01. There is no completed website build to classify as passed or failed. The following are pre-build risks/flags, not build failures.

## Additional flags found in the 2026-09-28 recheck

### A. Third-party trademarks conflict with “clean set” descriptions

Visual inspection confirms visible Timberland tree marks and branded packaging/tags in multiple files, including `FOOTHIVE TIMBERLAND IMAGES/image02.png`, `image04.png`, `image05.png`, `image08.png`, `image13.png`, `image15.png`, `image16.png`, and `image19.png`. The same issue appears in `FOOTHIVE SNEAKER IMAGES/navy-tan-stripe.png`, which visibly uses Adidas's three-stripe mark. `FOOTHIVE BOOTS IMAGES/winged-cross-studded-western-boot.png` includes third-party shop signage/branding in its background, and `FOOTHIVE BOOTS IMAGES/sunflower-embroidered-western-boot.png` has a visible `1/2` overlay/watermark. These observations conflict with a clean/brand-neutral asset-set description. The image assets remain untouched.

**Before live use:** Operator must decide whether to replace, exclude, crop, or obtain clearance for the images. Do not represent the set as brand-neutral without rechecking.

### B. Four catalog files contain unresolved relative image paths

The Markdown catalogs currently reference `boot-images/...`, `classic-images/...`, `sneaker-images/...`, and `images/imageNN.png`. The corresponding image files are presently stored directly next to each catalog, not in those referenced child folders. As a result, the embedded links do not resolve from the current tree. No link correction was made in this task.

### C. Direction B mockup conflicts with locked v1 scope and has unsupported content

The selected image `DIRECTION A & B IMAGES/37n4T (DIRECTION B).jpg` shows more than the approved static landing-page plan: a cart icon, per-product prices, extra shop/category links, social-platform icons, and “Easy Returns / 30-day returns,” alongside product/material claims. The architecture says there is no cart and no extra page; the conversation does not establish source/approval for every displayed claim. The client separately and explicitly approved the corner tags and FootHive spelling correction. Those approvals do not automatically approve the other additions.

**Before styling T03–T06:** compare each element against PRD/architecture/security/frontend confirmation; remove or obtain approval/evidence for anything outside it. The mockup remains unchanged.

### D. Local asset count differs from the prior transcript report

The previous inventory summary in the conversation says 42 files. The current recursive folder inventory returns 45 files. This is a historical count discrepancy; it does not by itself indicate missing assets. Use the current tree as the build source and reconcile the old count only if exact historical accounting is needed.

### E. Preview placeholders are not final destinations

The client approved `https://pin.it/37MYm0GnG` as a temporary preview value for Shop and social links. Final Shopify and Instagram values were still open in the transcript. Replace them before production promotion and verify all outbound destinations.

## Review and closure conditions

Before the website phase starts, have the Operator resolve asset use and the mockup-scope questions. Fix or deliberately preserve the catalog links with the Operator's approval. During implementation, do not add a cart, extra pages, fabricated testimonials, unsupported shipping/returns/material claims, or other unapproved content. Keep a ticket-level record of actual implementation, checks, failures, and fixes. Only then classify website-build outcomes.

---

**Revision note — 2026-09-28:** Full transcript reread plus local folder, catalog, logo, and image review. This file separates historical trial failures from audit findings made now. No website code or product images were changed.  
**Agent:** Codex  

# FootHive Production Lessons

**STATUS:** [POPULATED — HISTORICAL T20 RELEASE SUMMARY]
**PARENT:** FOOTHIVE_PROD_SUMMARY_BRAINBOX/
**CANONICAL SOURCE:** The T20 section of the canonical Sandbox Build Report; Operator Addendum for the Operator-confirmed form response.
**LAST VERIFIED:** 2026-10-09
**VERIFIER:** Codex — source-backed M16 compilation; independent ChatGPT verification PASS (2026-10-09).
**APPLIES TO:** The documented FootHive T20 release on 2026-10-01.

## Release record

The T20 record states that the FootHive final trial candidate was merged to the FootHive repository's `main` branch through PR #9. The merge commit was `1916fc59a38bf84125e966e0f2008b4e78749653`.

The Netlify Deploys API record captured in the Build Report identifies deployment `6abeab441468890009114676` as **ready**, public, and deployed from `main`. It was published at `2026-10-01T18:49:47.720Z`; its recorded deploy time was five seconds; and its commit reference matched the PR #9 merge commit. The recorded public URL was [https://foothive.netlify.app/](https://foothive.netlify.app/).

The Build Report later records that repository cleanup advanced GitHub `main` to `de648c8c591f7c50b148269dd56156731917543e`, with no website source changes or subsequent Netlify deployment during that cleanup. Therefore this record identifies the T20 deployment commit and does not equate it with a later repository HEAD or claim a fresh live check.

## Post-deployment checks recorded for T20

The T20 report documents Playwright MCP Chromium verification against the public URL:

- Viewports: 320×780, 390×844, 768×1024, and 1440×900; no horizontal overflow was reported.
- Product-grid columns: 1 / 1 / 2 / 3 at those viewport sizes.
- Nine page images loaded with alt text; no product prices or broken in-page anchors were found.
- The privacy and shipping/returns dialogs opened; Escape closed them and restored focus.
- Twenty external links used the approved Pinterest trial destination and safe new-tab attributes.
- The favicon returned HTTP 200.
- GA4's script returned HTTP 200 and the page-view request returned HTTP 204 for the configured measurement ID.
- The Playwright run reported zero browser-console errors and warnings.

These are the T20 recorded results, not a new M16 test. The report identifies the automated browser run as Chromium QA, not formal accessibility or cross-browser certification. The Operator Addendum separately records the Operator's manual Firefox and Safari checks; those checks are not attributed to Codex.

## Notification-form evidence

The T20 browser test sent one disposable address with the Operator's approval. The form endpoint returned HTTP 200, while the site correctly stated that it could not verify Google's cross-origin response-sheet state. The later Operator Addendum records that the Operator checked the existing response row in Google Forms and supplied screenshot evidence. The row's persistence is therefore Operator-confirmed; the page's limitation remains accurately recorded. M16 did not submit another response or duplicate the screenshot.

## Scope and disclosure

FootHive is documented as a workflow trial based on a public Upwork brief, with the Operator role-playing the client. The records do not establish paid-client work or client acceptance. A public Netlify release is evidence of deployment, not evidence of a paid engagement.

The page is a static landing-page trial. The project records describe no in-page cart, checkout, authentication, database, or product-editor interface. Product prices were omitted. Pinterest remained the approved trial destination for Shop and Instagram links because final destination links had not been supplied.

## Lessons and limits

1. Preserve one final deployment for the integrated candidate after local verification when deployment credits are limited; the earlier report records the Operator's decision to conserve Netlify deployment capacity.
2. Keep the release commit, deploy identifier, timestamp, visibility, and public URL together so a later agent can distinguish an actual deployment from a branch build or preview.
3. Separate a successful form POST from verified persistence. The site cannot inspect Google's cross-origin response sheet; the Operator's later review is separate evidence.
4. Keep sandbox evidence and production-release evidence distinct. M15 retains the canonical trial records; this file summarizes T20 and links back to those records.
5. Record the exact limits of QA. A Chromium run and Operator-performed Firefox/Safari checks do not amount to formal accessibility certification.

No new production deployment, application test, form submission, or source transfer was performed for M16.

## Source records

- [Canonical Sandbox Build Report — T20 release and QA](../../../SANDBOX_DEVOPS_BRAINBOX/CASE_STUDIES_SANDBOX_BRAINBOX/FOOTHIVE_WORKFLOW_TRIAL_BRAINBOX/BUILD_REPORT_FH_BRAINBOX.md)
- [Operator Addendum — T20 form persistence and browser checks](../../../SANDBOX_DEVOPS_BRAINBOX/CASE_STUDIES_SANDBOX_BRAINBOX/FOOTHIVE_WORKFLOW_TRIAL_BRAINBOX/OPERATOR_ADDENDUM_FH_BRAINBOX.md)
- [Canonical Sandbox case-study README](../../../SANDBOX_DEVOPS_BRAINBOX/CASE_STUDIES_SANDBOX_BRAINBOX/FOOTHIVE_WORKFLOW_TRIAL_BRAINBOX/README_FH_WORKFLOW_TRIAL_BRAINBOX.md)

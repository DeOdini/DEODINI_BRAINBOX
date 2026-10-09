# FootHive Project Handoff

**STATUS:** [POPULATED — DOCUMENTARY HANDOFF]
**PARENT:** FOOTHIVE_PORTFOLIO_BRAINBOX/
**CANONICAL SOURCE:** The M15 Sandbox case study, T20 release record, and Operator Addendum.
**LAST VERIFIED:** 2026-10-09
**VERIFIER:** Codex — source-backed M16 handoff; independent ChatGPT verification pending.
**APPLIES TO:** The static FootHive website trial and its documented T20 release.

## Delivered project

FootHive is a responsive, single-page footwear landing page built with static HTML, CSS, and JavaScript. The project records seven product cards, a story section, trust content, a notification form, navigation, and a footer. Product prices were omitted. The documented architecture has no in-page cart, checkout, backend, database, authentication, or product-editor interface.

The trial connected the Shop and Instagram destinations to Pinterest as an explicitly approved temporary destination. The notification form used Google Forms/Sheets, and the release included GA4 page-view tracking. Replace the trial Pinterest destinations with the Operator's final destinations before treating the page as a final retail marketing site.

## Release and repository references

- T20 public release URL recorded in the Build Report: [https://foothive.netlify.app/](https://foothive.netlify.app/).
- Website source repository recorded in the T20 closeout: [DeOdini/FOOTHIVE](https://github.com/DeOdini/FOOTHIVE).
- T20 release was deployed from merge commit `1916fc59a38bf84125e966e0f2008b4e78749653`, Netlify deployment `6abeab441468890009114676`, published 2026-10-01.
- The later repository cleanup moved GitHub `main` to `de648c8c591f7c50b148269dd56156731917543e` without website source changes or a new deploy, according to the recorded closeout. This handoff does not claim the current live deployment was checked during M16.
- Local project path recorded by the Build Report: `C:\Users\USER\FOOTHIVE`. This path is part of the historical project record and was not re-inspected in M16.

## Engagement disclosure

The project is recorded as a DEODINI workflow trial based on a public Upwork brief, with the Operator role-playing the client. It is not evidence of a paid client engagement, paid delivery, client acceptance, or a production commerce system. The public deployment demonstrates a released trial artifact only.

## Verification boundaries

T20's Build Report records Playwright MCP Chromium checks at desktop, tablet, and mobile viewport sizes, GA4 network responses, and a one-time approved disposable form submission. The site could not verify cross-origin response-sheet persistence; the Operator later confirmed the existing row in Google Forms and supplied screenshot evidence. No new test response was submitted in M16.

The Operator Addendum records separate manual Firefox and Safari checks. Neither that manual verification nor the Chromium run is formal accessibility certification or screen-reader certification.

## Canonical records

Use the [case-study reference index](CASE_STUDY_REFERENCE_FOOTHIVE_BRAINBOX.md) and the linked canonical Sandbox and Production records. The historical evidence set remains in Sandbox; this handoff does not copy it.

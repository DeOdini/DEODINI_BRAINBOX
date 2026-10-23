# CHATGPT_CORE_FUNC_BRAINBOX.md

**CANONICAL_SOURCE:** [CHATGPT_FUNC_BRAINBOX.md](../../../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/FUNC_AI_BRAINBOX/CHATGPT_FUNC_BRAINBOX.md)
**REFERENCED_BY:** [CORE registry README](README_AI_AGENTS_CORE_FUNC_BRAINBOX.md); [FUNC README](../README_FUNC_AI_BRAINBOX.md); [M01 migration map](../../../VERSION_HISTORY_BRAINBOX/V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md)
**REFERENCES:** [Frozen V003 Specification §9](../../../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md); [Governance evidence rules](../../../GOVERNANCE_BRAINBOX/EVIDENCE_GOV_BRAINBOX.md); [Governance ticketing rules](../../../GOVERNANCE_BRAINBOX/TICKETING_GOV_BRAINBOX.md)
**STATUS:** [ACTIVE — HISTORICAL SOURCE MAPPED; LIVE RUNTIME UNKNOWN]
**LAST_VERIFIED:** 2026-10-08 — Codex checked source content and M01 integrity baseline; ChatGPT runtime was not queried.
**APPLIES_TO:** ChatGPT capability and integration record.
**SOURCE_TYPE:** Dated agent capability report; not a live credential or access grant.
**VERIFIER:** Codex, V003-M05.

## EXPOSED

**Current status:** UNKNOWN / NOT VERIFIED in the current ChatGPT runtime.
**Historical report:** Timestamp 2026-09-19 11:34 -05:00. It listed GitHub, Figma, Supabase, Render, Outlook, and Brevo as active/verified connectors. It also catalogued Base44, Supabase, email, Render, Figma, Stripe, and other skills, with additional potential connectors including Replit, Resend, Stripe, Upwork, and Outlook Calendar. See the source report for its detailed skill inventory.

## CONNECTED

**Current status:** UNKNOWN / NOT VERIFIED.
**Historical evidence:** The source report claimed active connections to GitHub, Figma, Supabase, Render, Outlook, and Brevo at its timestamp. That dated claim is not evidence of a current connection.

## AUTHENTICATED

**Current status:** UNKNOWN / NOT VERIFIED.
**Historical evidence:** The source report said the listed GitHub, Figma, Supabase, Render, Outlook, and Brevo accounts were authenticated or verified then. No present account identity or token state was checked for ChatGPT during M05.

## EXECUTABLE

**Current status:** UNKNOWN / NOT VERIFIED for current ChatGPT runtime.
**Historical evidence:** The source describes connector use and gives safe test examples. Suggested examples are not recorded test outcomes. No ChatGPT-side connector execution was performed in this M05 session.

## AUTHORIZED

**Standing authorization:** NO.
Use any connected capability only under the Operator's task-specific direction and the applicable governance/ticket rules. The historical report's access claims do not grant permission to send mail, modify data, deploy, push, merge, or perform other writes.

## LIMITATIONS

- The source is dated 2026-09-19; services and account permissions can change.
- Skills are instruction packages, not credentials.
- The report notes Figma access was constrained by the account plan/seat and file permissions.
- Email, database, hosting, and repository writes require action-specific authority.
- This CORE record does not treat historical examples as present execution evidence.

## CANONICAL EXE REFERENCES

[EXE index](../AI_AGENTS_EXE_FUNC_BRAINBOX/README_AI_AGENTS_EXE_FUNC_BRAINBOX.md). No category is assigned in the frozen M06 matrix; current ChatGPT execution remains UNKNOWN / NOT VERIFIED.

## LAST VERIFIED

2026-10-08 — source report was read and its size, line count, and SHA-256 matched the M01 baseline. This verifies provenance integrity only; live ChatGPT connection, authentication, and execution remain UNKNOWN / NOT VERIFIED.


## Priority 3 — ChatGPT CORE registration (2026-10-23; local Stage G implementation)

**Agent/runtime:** ChatGPT (GPT-6), ChatGPT conversation; observation windows 2026-10-20 (historical), 2026-10-22 and 2026-10-23 (scoped live testing). **Status:** Stage G local implementation completed on 2026-10-23; published on `main` in commit `7bf6429d25c86291a313da63d1e1aefc313a0d11`; publication independently reviewed by MAIN CONVO 4 and Operator accepted with QUALIFIED PASS on 2026-10-23. Individual CORE provider connections, authentication and live-operation verification remain evidence-scoped or pending; final ChatGPT onboarding closure remains pending. **Authorization:** 2026-10-23 Operator Stage G six-file local-edit scope only; no staging/commit/push or external mutations.

**Original historical evidence:** [2026-10-20 onboarding appendix](../../../POST_V003_MODIFICATIONS_BRAINBOX/POST_V003_MOD_CONVO_BRAINBOX.md#chatgpt--recovered-historical-onboarding-report--2026-10-20), publication commit `238635dfa3adadf8c8cc5e682b00a3383df72fa9`. Historic `CORE-CHATGPT-001` through `017` are **provisional aliases**, not automatically the identities below. October 22 `001`–`006` were separate provisional session assignments. Item identities below are the approved **local implementation candidates**; independent item-level admission is pending.

### C01–C10 session answers

- **C01 identity and sources:** This ChatGPT web-chat runtime; direct session tool responses (GitHub/RDC/Browser/Python) distinguished from Oct 20 historic self-report and subsequent Stage F qualified independent review. Other agents' operations are not ChatGPT evidence.
- **C02 advertised inventory:** 32 provider/native-capability items listed below; tool exposure does not establish provider-wide executable access. Historic H20-017 also mentions **unspecified additional development tooling**, pending item-level identification; it is not discarded or given an invented ID.
- **C03 status:** Exposure, connection, authentication and exact operation are separate per row; current tool visibility may vary by session. Unknown means unverified, not unavailable.
- **C04 skills/dependencies:** Native tools, connector-specific provider scopes, relevant Figma/Supabase/Drive and artifact skills; possessing documentation is not evidence of a connected provider.
- **C05 device/resources:** Authorized RDC device DESKTOP-DHRIH27 and repository C:/Users/USER/DEODINI_BRAINBOX for evidenced reads; isolated Python has separate local runtime. No unrestricted device or credential access.
- **C06 communications:** Email, campaigns and calendar interfaces are exposed, but no account-level message/event operations or send authority were tested.
- **C07 automation:** Activepieces and native automations exposed; no workflow run, trigger or scheduled task creation demonstrated.
- **C08 professional functions:** Documentation, scoped repository evidence review and computation are supported narrowly. Frontend/backend implementation, general tests, database writes and deployment are not proven here.
- **C09 potential:** Governed capability refresh, evidence-link checking and future collaboration workflows remain unimplemented proposals.
- **C10 records:** The item ledger below is the capability record; specific attempts live in [ChatGPT agent EXE](../AI_AGENTS_EXE_FUNC_BRAINBOX/CHATGPT_EXE_FUNC_BRAINBOX/README_CHATGPT_EXE_FUNC_BRAINBOX.md). All EXE references are logical candidate suffixes until verification acceptance.

**Status interpretation:** LIVE VERIFIED means a successful check of the *stated exact function*, self-observed unless explicitly independently reproduced; it does NOT automatically imply EXE VERIFIED EXECUTED. CARRIED FORWARD — NOT RETESTED means historical evidence remains, without current connection/authentication claims. No CURRENTLY UNAVAILABLE — CONFIRMED determination is justified. **H20** = original Oct 20 provisional grouping; **O22** = Oct 22 provisional counterpart. Current authority is read-only for tested operations and local six-file editing only in Stage G.

### C10 provider-level evidence ledger

| Candidate ID | Provider/capability | H20 alias | O22 alias | Exposed | Connected | Authenticated | Exact operation demonstrated | Dated refresh | EXE candidate | Dependencies, boundaries and gaps |
|---|---|---|---|---|---|---|---|---|---|---|
| `CORE-CHATGPT-001` | Native text, reasoning, documentation | H20-001 | — | native | native | N/A | Chat-only synthesis; no standardized benchmark | CARRIED FORWARD — NOT RETESTED | None | Native ChatGPT; output quality and session vary |
| `CORE-CHATGPT-002` | Remote Desktop Commander | H20-002 | O22-002/003/004 | yes | yes, authorized device | underlying identity unknown | list_devices, list_directory, read_file, read-only terminal, Oct 22–23 | LIVE VERIFIED (scoped, self-observed) | `EXE-CHATGPT-FILE-001`, `EXE-CHATGPT-FILE-002`, `EXE-CHATGPT-FILE-003`, `EXE-CHATGPT-FILE-004` | RDC, DESKTOP-DHRIH27; permitted repository only |
| `CORE-CHATGPT-003` | GitHub | H20-003 | O22-001 | yes | yes, read endpoints | identity and precise scope not audited | repo search, branch, file, commit and PR metadata reads, Oct 22–23 | LIVE VERIFIED (scoped, self-observed) | `EXE-CHATGPT-RESEARCH-001` | GitHub provider, DeOdini/DEODINI_BRAINBOX; no write inference |
| `CORE-CHATGPT-004` | Native web retrieval | H20-004 | — | yes | not retested | N/A for public source | none in dated onboarding test | CARRIED FORWARD — NOT RETESTED | None | Source availability and freshness vary |
| `CORE-CHATGPT-005` | Isolated Python/container execution | H20-005 | O22-006 | yes | local kernel | N/A | Oct 23 SHA-256 and arithmetic; Oct 22 trace incomplete | LIVE VERIFIED (Oct 23 computation only) | `EXE-CHATGPT-CODE-001` | Isolated Python; no repo or production access inferred |
| `CORE-CHATGPT-006` | Gmail | H20-006 | — | yes | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Gmail connector/account; no inbox or send test |
| `CORE-CHATGPT-007` | Microsoft Outlook Email | H20-006 | — | yes | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Outlook email account; no read/send test |
| `CORE-CHATGPT-008` | Google Calendar | H20-007 | — | yes | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Google calendar scope unknown |
| `CORE-CHATGPT-009` | Microsoft Outlook Calendar | H20-007 | — | yes | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Outlook calendar scope unknown |
| `CORE-CHATGPT-010` | Google Drive | H20-008 | — | yes | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Drive file IDs and account scope unknown |
| `CORE-CHATGPT-011` | Google Docs | H20-008 | — | advertised via Drive integration | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Google Drive/Docs skill and document permissions |
| `CORE-CHATGPT-012` | Google Sheets | H20-008 | — | advertised via Drive integration | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Sheets range permissions; not tested |
| `CORE-CHATGPT-013` | Google Slides | H20-008 | — | advertised via Drive integration | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Slides access and editing not tested |
| `CORE-CHATGPT-014` | Figma | H20-009 | — | yes | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Figma skill, file/seat permissions |
| `CORE-CHATGPT-015` | Supabase | H20-010 | — | yes | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Supabase skill, project/database permissions; no queries |
| `CORE-CHATGPT-016` | Render | H20-010 | — | yes | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Render service permissions; no deployment |
| `CORE-CHATGPT-017` | Stripe | H20-010 | — | yes | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Stripe account and billing scope untested |
| `CORE-CHATGPT-018` | Replit | H20-010 | — | yes | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Replit project/runtime scope untested |
| `CORE-CHATGPT-019` | Base44 | H20-010 | — | yes | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Base44 app scope untested |
| `CORE-CHATGPT-020` | Brevo | H20-011 | — | yes | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Brevo campaigns/contact scope; no send |
| `CORE-CHATGPT-021` | Resend | H20-011 | — | yes | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Resend mail/domain scope; no send |
| `CORE-CHATGPT-022` | Activepieces | H20-012 | — | yes | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Workflow credentials/triggers untested |
| `CORE-CHATGPT-023` | Native scheduled automations | H20-013 | — | yes | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | No scheduled task created or read |
| `CORE-CHATGPT-024` | Browser connector | H20-014 | O22-005 | yes | yes for tab listing | host permissions incomplete | list_tabs succeeds; get_tab_context denied Oct 23 on tested hosts | LIVE VERIFIED (tabs); RETEST REQUIRED (page access) | `EXE-CHATGPT-BROWSER-001`, `EXE-CHATGPT-BROWSER-002` | Extension permissions; no successful page-body read |
| `CORE-CHATGPT-025` | Image generation/editing | H20-015 | — | yes | not exercised | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Native image tool; not benchmarked |
| `CORE-CHATGPT-026` | Document artifact tooling | H20-016 | — | yes | not exercised | N/A for local outputs | none | CARRIED FORWARD — NOT RETESTED | None | DOCX tools and document skill not tested |
| `CORE-CHATGPT-027` | PDF tooling | H20-016 | — | yes | not exercised | N/A for local outputs | none | CARRIED FORWARD — NOT RETESTED | None | PDF skill and rendering not tested |
| `CORE-CHATGPT-028` | Spreadsheet tooling | H20-016 | — | yes | not exercised | N/A for local outputs | none | CARRIED FORWARD — NOT RETESTED | None | Spreadsheet skill, artifact_tool/openpyxl untested |
| `CORE-CHATGPT-029` | Presentation tooling | H20-016 | — | yes | not exercised | N/A for local outputs | none | CARRIED FORWARD — NOT RETESTED | None | Slide skill/tooling untested |
| `CORE-CHATGPT-030` | Firecrawl | H20-017 | — | yes | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Provider and search credentials untested |
| `CORE-CHATGPT-031` | Upwork | H20-017 | — | yes | unknown | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Marketplace account/role scope unknown |
| `CORE-CHATGPT-032` | Plugin Management | H20-017 | — | yes | not tested | unknown | none | CARRIED FORWARD — NOT RETESTED | None | Plugin access/configuration not inspected |

**Evidence date/verifier:** H20 original 2026-10-20 ChatGPT onboarding report (historical self-report); O22 live observations 2026-10-22 (self-observed); current live scoped checks 2026-10-23 (self-observed). Stage F independent assessment reported QUALIFIED PASS overall and independent reproduction of the October 23 Python calculation and browser host-permission failure **only**; this is not independent verification of every tool item. Supporting tool response history remains in the Priority 3 conversation; individual operation details and exact targets are indexed in the ChatGPT EXE README. **Last checked:** 2026-10-23 for directly tested operations; historical-only providers retain 2026-10-20 evidence and current exposure where observed without implying connection.

**Identifiers:** The final numbered candidate entries do not erase or rewrite October 20/22 provisional numbering. In particular H20-001 text differs from O22-001 GitHub; H20-002 RDC overlaps O22-002 device; H20-003 GitHub differs from O22-003 directory. Never resolve aliases by suffix alone. Any later collision requires separate scoped reconciliation.

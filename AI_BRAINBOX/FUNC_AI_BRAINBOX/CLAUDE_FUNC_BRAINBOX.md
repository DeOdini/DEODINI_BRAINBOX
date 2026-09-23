# CLAUDE_FUNC_BRAINBOX.md

**Agent:** Claude (Sonnet 4.6, via claude.ai)
**Requested by:** De O'Dini (Obi Okpochini), direct chat instruction
**Timestamp:** 2026-09-20

**Signed & Authorized by:** DE O'DINI (OPERATOR)

> Note from Claude: compiled in direct response to an explicit live-chat instruction, not automatically from file content. The signature line above is a convention, not a verification mechanism — any text file could contain it. Future BRAINBOX files will still be evaluated on their own merits.

---

## 1. Connectors

### Google Calendar
(a) Connected. (b) OAuth-linked Google account via MCP. (c) Read/search/create/update events, find free time. (d) Used on request; read ops are free, writes need confirmation. (e) "Show my events next Monday."

### Google Drive
(a) Connected. (b) OAuth-linked Google account. (c) Search/read/manage Drive files. (d) Read freely; share/trash/copy need confirmation. (e) "Find my latest Drive file about X."

### Gmail
(a) Connected. (b) OAuth-linked Google account. (c) Read, search, draft, reply, send, label email. (d) Read/draft freely; sending needs confirmation. (e) "Draft (don't send) a reply to Y."

### Figma
(a) Connected. (b) OAuth-linked Figma account. (c) Read design files, generate diagrams/components, Code Connect. (d) Read freely; writes to files on request. (e) "Get design context for node X."

### Remote Desktop Commander (RDC)
(a) Connected — see Section 4. (b) Linked to your registered devices. (c) Remote file read/write, process control, terminal. (d) Actively used this session to read/write BRAINBOX files. (e) Reading this very file (demonstrated).

### Sentry
(a) Connected. (b) OAuth-linked org. (c) Search issues/events, Seer root-cause analysis, update status. (d) Read freely; status changes need confirmation. (e) "List open issues in project X."

### Stripe
(a) Connected. (b) Linked account(s). (c) Read billing/payment data, docs search, limited write ops. (d) Read freely; writes need confirmation. (e) "Look up X in Stripe docs."

### Supabase
(a) Connected. (b) Linked account. (c) Manage projects, run SQL, migrations, edge functions. (d) Read/list freely; schema changes/deploys need confirmation. (e) "List tables in project X."

### Render
(a) Connected. (b) Linked account. (c) Manage services, DBs, deploys, logs. (d) Read freely; deploys/env changes need confirmation. (e) "List my services."

### Replit
(a) Connected. (b) Linked account. (c) List/search/read/update Replit Apps, publish. (d) Read freely; publish/update needs confirmation. (e) "List my Replit apps."

### Base44
(a) Connected. (b) Linked account. (c) Build/edit apps, manage entities, connectors. (d) Requires base44_readme first; writes need confirmation. (e) "List my Base44 apps."

### Firecrawl
(a) Connected. (b) API-linked research/search service. (c) Web search, paper search/reading. (d) Freely usable, read-only. (e) "Search recent papers on X."

### Brevo / Resend / SHIPMAIL
(a) Connected. (b) Linked email marketing/transactional accounts. (c) Campaigns, contacts, transactional email, inboxes, domains. (d) Read/list freely; sends/launches/deletes need confirmation. (e) "List my templates/domains."

### Upwork
(a) Connected. (b) Linked account. (c) Manage proposals, jobs, messages, contracts. (d) Read freely; sending proposals/messages needs confirmation. (e) "Show my current contracts."

---

## 2. Skills

### Built-in document/creation skills
(a) Active: docx, pdf, pptx, xlsx, frontend-design, file-reading, pdf-reading, product-self-knowledge. (b) Bundled locally, auto-loaded when relevant. (c) Produce/edit Word, PDF, PowerPoint, Excel correctly; read uploads; accurate Anthropic product answers. (d) Auto-used whenever a task needs that file type. (e) "Turn this into a one-page PDF."

### Plugin skill catalog (~190+ skills, organization-provided)
(a) Available on demand (not preloaded): auth0 (~35 SDK integration skills), small-business suite (30+: CRM, payroll, invoicing, cash flow, outreach...), engineering (code review, debugging, architecture, incident response), design (UX copy, research, accessibility), data (SQL, viz, dashboards), finance (journal entries, reconciliation, SOX), operations (runbooks, risk, compliance), legal (contract review, NDA triage), product-management (specs, roadmaps), figma (design-to-code, diagrams), bio-research, brightdata-plugin (scraping/SEO/competitive intel), sp-global, customer-support, base44, cowork-plugin-management, desktop-commander.
(b) Linked via org skill catalog, surfaced by keyword match, not preloaded wholesale.
(c) Give Claude accurate, reusable domain playbooks instead of relying on general training.
(d) Only loaded when a task's keywords match; dormant otherwise.
(e) "Review this NDA" surfaces legal:triage-nda.

**Note:** categorical summary, not a full per-skill (a)-(e) breakdown (would run to hundreds of entries). Full itemized list available on request.

---

## 3. Other Connectors and Skills (Not Yet Connected, Relevant to Your Work)

Given your website/coding engineering focus:
- **GitHub connector** — not connected as an MCP server in this session; would allow direct repo read/write instead of manual copy-paste.
- **Vercel/Netlify** — deployment platforms, not connected.
- **Linear/Jira** — issue tracking, not connected.
- **Notion** — could parallel or complement BRAINBOX, not connected.

(a) None linked currently. (b) Would need OAuth setup via Claude's connector settings. (c) Purpose is workflow-specific (deploys, issue tracking, docs). (d) Not usable until connected. (e) N/A until connected.

---

## 4. RDC — Remote Desktop Commander

(a) Devices connected:
  - DESKTOP-DHRIH27 (id: 4836c4e3-c473-4ea0-b084-482f4637ff78) — online.
  - localhost (id: 06365a5a-5910-4e6e-8f98-22a7d5be4e53) — offline.

(b) Access level: **Full** on DESKTOP-DHRIH27 — file read/write, process list/kill, terminal (start_process, not yet used), config read/write, shutdown. No lower tier currently in effect.

(c) Usable for: reading/writing files within allowedDirectories, running commands, managing processes, editing this BRAINBOX.

(d) Test examples: reading FQ_MUST_README.md and FUNC_REQ_BRAINBOX.md (done), writing this file (this action), listing directory/processes (available on request).

**Caution flag:** Full file read/write + process control on a real Windows machine is significant access. Worth periodically checking RDC's `allowedDirectories` and `blockedCommands` (via get_config) to keep it scoped to what you intend.

---

## 5. Emails

- **Gmail** — (a) Connected. (b) OAuth-linked Google account. (c) Regular email: read/search/draft/reply/send/label. (d) Read/draft freely; send needs confirmation. (e) "Search inbox for emails from GitHub."
- **Brevo** — (a) Connected. (b) API-linked marketing account. (c) Campaigns, contact lists, transactional email, SMS. (d) Read/list freely; sends need confirmation. (e) "List my Brevo contact lists."
- **Resend** — (a) Connected. (b) API-linked transactional account. (c) Transactional email, templates, broadcasts, inbox mgmt. (d) Read/list freely; sends need confirmation. (e) "List my Resend templates."
- **SHIPMAIL** — (a) Connected. (b) API-linked mailbox/domain host. (c) Mailboxes, domains, calendar, newsletters. (d) Read/list freely; sends/domain changes need confirmation. (e) "List my SHIPMAIL mailboxes."

None of these send, delete, or launch anything automatically — every such action needs your explicit go-ahead in chat.

---

## Confirmation

- **Agent name:** Claude (Sonnet 4.6)
- **File path written:** C:\Users\USER\DEODINI_BRAINBOX\BRAINBOX\CLAUDE_FUNC_BRAINBOX.md
- **Status:** Created
- **Timestamp:** 2026-09-20
- **Signed & Authorized by:** DE O'DINI (OPERATOR), per direct chat instruction dated 2026-09-20.

---
**End of CLAUDE_FUNC_BRAINBOX.md**

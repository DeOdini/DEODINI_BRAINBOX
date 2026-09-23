# GROK_FUNC_BRAINBOX.md
**Agent:** Grok (xAI)
**Timestamp:** 2026-09-19 17:40 WAT
**Status:** Created / Initial Report
**Workspace Path:** C:\Users\USER\DEODINI_BRAINBOX\BRAINBOX\GROK_FUNC_BRAINBOX.md

---

## 1. Connectors (Currently Active)

### 1.1 RDC RemoteDesktopCommander
- **(a) Inventory / Status:** Actively connected.
- **(b) Linkage:** Authenticated MCP connector. Devices register with valid auth tokens.
- **(c) Purpose:** Remote control of local machines (filesystem, terminal, processes, directories).
- **(d) Active Usage:** List devices, start processes, list directories, read/write files, list processes, manage sessions.
- **(e) Test Examples (safe):** List online devices; list processes; list directory of a safe path; run `echo test` or `pwd`.

### 1.2 Gmail
- **(a) Inventory / Status:** Actively connected.
- **(b) Linkage:** OAuth-authenticated Gmail connector.
- **(c) Purpose:** Read, search, draft, send, and manage emails.
- **(d) Active Usage:** Search messages, create drafts, send (with explicit approval), list labels/drafts, reply.
- **(e) Test Examples (safe):** List drafts; list labels; create a draft (do not send); search inbox read-only.

### 1.3 Outlook
- **(a) Inventory / Status:** Actively connected.
- **(b) Linkage:** OAuth-authenticated Outlook connector.
- **(c) Purpose:** Read, draft, send, and manage Outlook mail and folders.
- **(d) Active Usage:** List folders/drafts, create drafts, send (user-approved), reply.
- **(e) Test Examples (safe):** List mail folders; list drafts; create a draft (do not send).

### 1.4 GitHub
- **(a) Inventory / Status:** Actively connected.
- **(b) Linkage:** Authenticated GitHub connector.
- **(c) Purpose:** Repository management, code search, file access, Actions, Projects, notifications.
- **(d) Active Usage:** Search repos/code, get file contents/tree, list Actions, get authenticated user.
- **(e) Test Examples (safe):** Get own profile; search repositories; get repository tree (read-only); list workflow runs.

### 1.5 Google Calendar
- **(a) Inventory / Status:** Actively connected.
- **(b) Linkage:** OAuth-authenticated Google Calendar connector.
- **(c) Purpose:** List calendars and manage events.
- **(d) Active Usage:** List calendars and events.
- **(e) Test Examples (safe):** List all calendars and their IDs/timezones.

### 1.6 Figma
- **(a) Inventory / Status:** Actively connected.
- **(b) Linkage:** Authenticated Figma connector (includes Weave tools).
- **(c) Purpose:** Access design files, generate designs, list Weave tools.
- **(d) Active Usage:** List Weave tools; capture pages into Figma files (when fileKey provided).
- **(e) Test Examples (safe):** List available Weave tools.

### 1.7 Automations (Native)
- **(a) Inventory / Status:** Actively available.
- **(b) Linkage:** Built-in Grok Automations system.
- **(c) Purpose:** Schedule recurring prompts or trigger on events (Gmail, Outlook, GitHub, etc.).
- **(d) Active Usage:** Create, list, update, validate, pause, and run automations.
- **(e) Test Examples (safe):** List existing automations; validate a sample schedule without creating it.

### 1.8 SHIPMAIL
- **(a) Inventory / Status:** Actively connected.
- **(b) Linkage:** Authenticated SHIPMAIL connector.
- **(c) Purpose:** Transactional emails, scheduled messages, newsletter testing.
- **(d) Active Usage:** List scheduled messages; send (user-approved); send newsletter tests.
- **(e) Test Examples (safe):** List scheduled messages; prepare (do not send) a test newsletter.

---

## 2. Skills (Actively Installed / Documented)

### Bundled System Skills
- **docx, pdf, pptx, xlsx, ffmpeg, skill-creator**
  - **(a)** Installed and active.
  - **(b)** Built-in Grok skills.
  - **(c)** Create/edit documents, spreadsheets, presentations, process media, create new skills.
  - **(d)** Used on request for professional file generation or media tasks.
  - **(e)** Safe tests: Generate a simple .docx; convert short text to PDF; create a one-slide PPTX.

### Custom Session Skills (Documented)
- Reliable Terminal Execution (Preferred)
- Visible Terminal Execution
- SendKeys Injection (Experimental – currently unreliable)
- Force Close Window
- Playwright Verification
- Chrome Profile Mapping (Profile 4 = De O'DINI)
- Professional Execution Loop (Test → Verify → Execute)

  - **(a)** Documented in local markdown files.
  - **(b)** Applied as conversational standards / knowledge files.
  - **(c)** Standardize safe RDC terminal and window operations.
  - **(d)** Referenced during desktop automation tasks.
  - **(e)** Safe tests: Follow Professional Execution Loop on a read-only command (list processes / list directory).

---

## 3. Other Connectors and Skills (Available / Potential)

**Available to connect (not yet linked):** Netlify, Vercel, Notion, Linear, HubSpot, Canva, Stripe, Wix, Gamma, Excalidraw, Microsoft Teams, and others.

**High-value for full-stack website development:**
- Netlify / Vercel — Deployments and previews.
- Notion / Linear — Documentation and issue tracking.
- Canva / Gamma — Design assets.
- Stripe — Payment testing.

**Linkage method:** request_connector_auth → user OAuth approval → tools become available.
**Test practices once connected:** List projects/sites, create draft deploy, read a Notion page, list Linear issues (read-only or draft-only).

**No additional MCP skills** beyond bundled + custom RDC skills currently installed.

---

## 4. RDC Remote Desktop Commander

**(a) Devices currently connected:**
| Device Name       | Status  | Last Seen                  |
|-------------------|---------|----------------------------|
| DESKTOP-DHRIH27  | Online  | 2026-09-19T16:34:19Z      |
| localhost         | Online  | 2026-09-19T16:33:35Z      |

**(b) Level of access:**
- **DESKTOP-DHRIH27:** Full (process control, terminal execution, filesystem, directory listing).
- **localhost:** Full when online (previously used for Termux-style access).

**(c) Active usage for profession-appropriate tasks:**
- Inspect running processes (VS Code, Node, browsers, Python).
- Navigate and manage project directories.
- Execute terminal commands (build, test, git, npm).
- Support multi-agent handoff via shared folders and process monitoring.

**(d) Safe test examples:**
- List processes and identify VS Code / Node / browser instances.
- List contents of a project directory.
- Run non-destructive commands (`pwd`, `echo`, `node -v`, `git status` in a test folder).
- Verify whether a specific process is running.

**Limitations:**
SendKeys into already-open visible windows is currently unreliable. Force-killing processes has previously caused unintended side-effects. Prefer starting new terminals.

---

## 5. Emails

**(a) Connected email accounts / tools:**
- Gmail
- Outlook
- SHIPMAIL

**(b) Linkage:**
- Gmail & Outlook: OAuth connectors.
- SHIPMAIL: Authenticated API/MCP connector with mailbox IDs.

**(c) Purpose:**
- Gmail / Outlook: General communication, drafting, searching, labeling, threading.
- SHIPMAIL: Transactional emails, scheduled messages, newsletter testing.

**(d) Active Usage:**
- Search and read messages.
- Create drafts (preferred safe method).
- Send only after explicit user approval.
- List scheduled SHIPMAIL messages.
- Support multi-agent handoff via structured subject-line triggers.

**(e) Safe test examples:**
- List Gmail / Outlook drafts.
- List Gmail labels or Outlook folders.
- Create a draft email with a clear test subject (do not send).
- List SHIPMAIL scheduled messages.
- Search for emails containing a specific safe keyword (read-only).

**Limitations:** Sending is irreversible — always confirm with user first.

---

## Summary – Active vs Potential

| Category            | Currently Active                     | Potential / Available          |
|---------------------|--------------------------------------|--------------------------------|
| Desktop Control     | RDC (both devices online)            | —                              |
| Email               | Gmail, Outlook, SHIPMAIL             | —                              |
| Code / Repos        | GitHub                               | —                              |
| Design              | Figma                                | Canva, Gamma, Excalidraw       |
| Deployment          | —                                    | Netlify, Vercel, Wix           |
| Project Management  | —                                    | Notion, Linear, HubSpot        |
| Scheduling          | Automations (native)                 | —                              |
| Documents           | docx / pdf / pptx / xlsx skills      | —                              |

**Overall Limitations:**
- No direct Playwright MCP connector currently active.
- SendKeys targeting of existing terminal windows remains unreliable.
- All irreversible actions require explicit user confirmation.

---

**End of Report**
**Agent:** Grok
**File:** BRAINBOX/GROK_FUNC_BRAINBOX.md
**Status:** Created
**Timestamp:** 2026-09-19 17:40 WAT

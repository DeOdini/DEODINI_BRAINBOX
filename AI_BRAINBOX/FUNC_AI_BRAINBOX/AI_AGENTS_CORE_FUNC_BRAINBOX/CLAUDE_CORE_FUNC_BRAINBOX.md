# CLAUDE_CORE_FUNC_BRAINBOX.md

**CANONICAL_SOURCE:** [CLAUDE_FUNC_BRAINBOX.md](../CLAUDE_FUNC_BRAINBOX.md)
**REFERENCED_BY:** [CORE registry README](README_AI_AGENTS_CORE_FUNC_BRAINBOX.md); [FUNC README](../README_FUNC_AI_BRAINBOX.md); [M01 migration map](../../../VERSION_HISTORY_BRAINBOX/V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md)
**REFERENCES:** [Frozen V003 Specification §9](../../../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md); [Governance evidence rules](../../../GOVERNANCE_BRAINBOX/EVIDENCE_GOV_BRAINBOX.md); [Governance ticketing rules](../../../GOVERNANCE_BRAINBOX/TICKETING_GOV_BRAINBOX.md)
**STATUS:** [ACTIVE — HISTORICAL SOURCE MAPPED; LIVE RUNTIME UNKNOWN]
**LAST_VERIFIED:** 2026-10-08 — Codex checked source content and M01 integrity baseline; Claude runtime was not queried.
**APPLIES_TO:** Claude capability and integration record.
**SOURCE_TYPE:** Dated agent capability report; not a live credential or access grant.
**VERIFIER:** Codex, V003-M05.

## EXPOSED

**Current status:** UNKNOWN / NOT VERIFIED in the current Claude runtime.
**Historical report:** Timestamp 2026-09-20; identifies Claude Sonnet 4.6 via claude.ai. It lists Google Calendar, Google Drive, Gmail, Figma, Remote Desktop Commander, Sentry, Stripe, Supabase, Render, Replit, Base44, Firecrawl, Brevo, Resend, SHIPMAIL, and Upwork. GitHub was not listed as a connected MCP in that report. The source also describes a broad installed-skill catalog; see it for specifics.

## CONNECTED

**Current status:** UNKNOWN / NOT VERIFIED.
**Historical evidence:** The source reports the named services as connected in that Claude session and says RDC was used to read/write Brainbox files then. This is a dated source claim, not a current connection check.

## AUTHENTICATED

**Current status:** UNKNOWN / NOT VERIFIED.
**Historical evidence:** The report describes OAuth or linked accounts for several services, but no current Claude account or connector identity was examined. Its “Signed & Authorized” text is explicitly described by the report itself as a convention, not an authorization verification.

## EXECUTABLE

**Current status:** UNKNOWN / NOT VERIFIED for current Claude runtime.
**Historical evidence:** The source claims actual RDC file read/write in its recorded session and gives example operations for other connectors. No Claude-side execution was performed during M05; examples for other services are not treated as tests.

## AUTHORIZED

**Standing authorization:** NO.
Only an explicit, task-specific Operator instruction authorizes an action. A report's signature line, account linkage, or connection does not authorize repository writes, email sending, deployment, migration, or merge.

## LIMITATIONS

- Source timestamp is 2026-09-20; present service availability may differ.
- The report did not identify GitHub as a connected MCP in that session.
- Its recorded connector list does not prove the same connector state in another Claude session.
- Skills and instructions do not establish credentials or authority.

## CANONICAL EXE REFERENCES

[EXE index](../AI_AGENTS_EXE_FUNC_BRAINBOX/README_AI_AGENTS_EXE_FUNC_BRAINBOX.md). No category is assigned in the frozen M06 matrix; historical file-operation claims do not meet its admitted-executor evidence.

## LAST VERIFIED

2026-10-08 — source report was read and its size, line count, and SHA-256 matched the M01 baseline. This verifies the preserved report, not current Claude runtime access.

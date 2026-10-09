# CLINE_CORE_FUNC_BRAINBOX.md

**CANONICAL_SOURCE:** [CLINE_FUNC_BRAINBOX.md](../CLINE_FUNC_BRAINBOX.md)
**REFERENCED_BY:** [CORE registry README](README_AI_AGENTS_CORE_FUNC_BRAINBOX.md); [FUNC README](../README_FUNC_AI_BRAINBOX.md); [M01 migration map](../../../VERSION_HISTORY_BRAINBOX/V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md)
**REFERENCES:** [Frozen V003 Specification §9](../../../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md); [Governance evidence rules](../../../GOVERNANCE_BRAINBOX/EVIDENCE_GOV_BRAINBOX.md); [Governance ticketing rules](../../../GOVERNANCE_BRAINBOX/TICKETING_GOV_BRAINBOX.md)
**STATUS:** [ACTIVE — HISTORICAL SOURCE MAPPED; LIVE RUNTIME UNKNOWN]
**LAST_VERIFIED:** 2026-10-08 — Codex checked source content and M01 integrity baseline; Cline runtime was not queried.
**APPLIES_TO:** Cline capability and integration record.
**SOURCE_TYPE:** Dated capability report with an initial diagnostic record; not a live credential or access grant.
**VERIFIER:** Codex, V003-M05.

## EXPOSED

**Current status:** UNKNOWN / NOT VERIFIED in the current Cline runtime.
**Historical report:** The actual capability section is timestamped 2025-09-20 00:05 UTC. It lists file-system and shell tools, Supabase, Firestore, BigQuery, Firecrawl, Playwright, and Microsoft documentation tools, plus 26 named skills. This source also contains an earlier 00:00 diagnostic about a failed initial report write; that history is preserved rather than treated as a present capability.

## CONNECTED

**Current status:** UNKNOWN / NOT VERIFIED.
**Historical evidence:** The actual capability report says those tool connectors were available in that Cline environment. It explicitly reports no Remote Desktop Commander devices and no connected email tools at that time.

## AUTHENTICATED

**Current status:** UNKNOWN / NOT VERIFIED.
The source does not establish current account identity or credential state for any listed service. The M05 review did not authenticate into Cline.

## EXECUTABLE

**Current status:** UNKNOWN / NOT VERIFIED for current Cline runtime.
The source describes available operations and suggested test practices. The initial diagnostic records a failed file-write attempt and a missing post-write verification; it is historical process evidence and does not show current runtime execution. No Cline-side tools were invoked in M05.

## AUTHORIZED

**Standing authorization:** NO.
Execution, external writes, messages, deployments, repository pushes, merges, and data changes require specific Operator authorization and the applicable ticket.

## LIMITATIONS

- The actual report is dated 2025-09-20 and may be stale.
- RDC was reported unavailable and email tools were reported absent in that session; those are historical states only.
- The source contains an initial failure report followed by an actual capability report; both are retained and distinguished.
- Tool or skill exposure does not prove authentication, execution, or authorization.

## CANONICAL EXE REFERENCES

NOT YET ASSIGNED — V003-M06 owns evidence-backed executable indexing.

## LAST VERIFIED

2026-10-08 — source report was read and its size, line count, and SHA-256 matched the M01 baseline. This verifies source integrity only; current Cline exposure and access remain UNKNOWN / NOT VERIFIED.

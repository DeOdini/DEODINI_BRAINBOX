# README_AI_AGENTS_CORE_FUNC_BRAINBOX.md

**PARENT:** AI_BRAINBOX/FUNC_AI_BRAINBOX/AI_AGENTS_CORE_FUNC_BRAINBOX/
**CURRENT DOMAIN:** Core capability records for the named AI agents
**PURPOSE:** Provide a source-backed, per-agent view of exposed tools and capabilities, connection state, authentication, verified execution, authorization, and limitations.
**MENTAL MODEL:** Exposure is not connection; connection is not authentication; authentication is not execution; execution is not authorization.
**GOVERNED BY:** Governance evidence and ticketing rules; frozen V003 Specification §9; M05 CORE and M06 EXE migration records.
**CANONICAL SOURCES:** Frozen V003 Specification §9; each agent's retained FUNC source report, except DeepSeek and Qwen, whose approved role baseline is in Specification §9.
**REFERENCES:** The parent FUNC README and linked source records.
**POPULATION STATE:** Eight CORE records remain; M06 added their evidence-scoped EXE links. Four categories are admitted for Codex; Copilot's Browser configuration is explicitly unverified; MEDIA is reserved. Historical agent claims remain time-bounded.
**LAST VERIFIED:** 2026-10-08
**VERIFIER:** Codex — M05 source/hash cross-check and M06 CORE-to-EXE reference reconciliation.
**APPLIES TO:** ChatGPT, Claude, Cline, Codex, Copilot, DeepSeek, Grok, and Qwen.

## Local tree

AI_AGENTS_CORE_FUNC_BRAINBOX/
├── README_AI_AGENTS_CORE_FUNC_BRAINBOX.md
├── CHATGPT_CORE_FUNC_BRAINBOX.md
├── CLAUDE_CORE_FUNC_BRAINBOX.md
├── CLINE_CORE_FUNC_BRAINBOX.md
├── CODEX_CORE_FUNC_BRAINBOX.md
├── COPILOT_CORE_FUNC_BRAINBOX.md
├── DEEPSEEK_CORE_FUNC_BRAINBOX.md
├── GROK_CORE_FUNC_BRAINBOX.md
└── QWEN_CORE_FUNC_BRAINBOX.md

## Required status fields

Each record uses these fields separately:

- **EXPOSED:** Tools, skills, connectors, APIs, or interfaces visible to the agent. Historical exposure is labeled with its report date.
- **CONNECTED:** Whether the integration responded in the relevant runtime. Dated reports do not establish a current connection.
- **AUTHENTICATED:** Whether an identity or credential was verified for the relevant runtime. A public read or tool name alone is insufficient.
- **EXECUTABLE:** Whether execution is evidenced for the stated operation and environment. Suggested safe tests in a source report are not test results.
- **AUTHORIZED:** The action-specific Operator authority. A connected or authenticated tool grants no standing write, push, merge, deployment, migration, or external-record authority.
- **LIMITATIONS:** Scope, age, uncertainty, permission boundaries, and known constraints.
- **CANONICAL EXE REFERENCES:** Link to the M06 evidence-backed executable index and the applicable category record, or state that the frozen matrix assigns no category.
- **LAST VERIFIED:** The date and scope of the evidence check. It must say when only the source file was checked and the live agent runtime remains unverified.

Use YES, NO, UNKNOWN / NOT VERIFIED, or NOT APPLICABLE for the status value, then explain the evidence and scope. Keep historical claims distinct from present runtime observations.

## Canonical references

- [Parent FUNC README](../README_FUNC_AI_BRAINBOX.md)
- [Evidence-backed EXE index](../AI_AGENTS_EXE_FUNC_BRAINBOX/README_AI_AGENTS_EXE_FUNC_BRAINBOX.md)
- [Frozen V003 Specification](../../../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md)
- [V003 Origin Conversation](../../../V003_VERSION_UPGRADE_BRAINBOX/V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md)
- [Governance evidence rules](../../../GOVERNANCE_BRAINBOX/EVIDENCE_GOV_BRAINBOX.md)
- [Governance ticketing rules](../../../GOVERNANCE_BRAINBOX/TICKETING_GOV_BRAINBOX.md)
- [Phase 02 ticket set, including M06](../../../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_PHASE02_MIGRATION_TICKETS_BRAINBOX.md)

**STATUS:** [ACTIVE — M05 COMMITTED AND PUSHED; INDEPENDENT CHATGPT VERIFICATION PENDING; M06 EXE INDEX POPULATED]

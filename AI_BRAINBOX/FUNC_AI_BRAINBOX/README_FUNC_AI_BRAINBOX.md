# README_FUNC_AI_BRAINBOX.md

**PARENT:** AI_BRAINBOX/FUNC_AI_BRAINBOX/
**CURRENT DOMAIN:** Functional capability records and execution-capability indexing for AI agents
**PURPOSE:** Navigate retained agent-source reports and the new CORE capability registry while keeping functional capability separate from reusable knowledge and operational workflow.
**MENTAL MODEL:** FUNC records what an agent is exposed to and can do, what is connected and authenticated, what execution is evidenced, what is authorized, and the limitations. A tool or skill being listed does not prove connection, execution, or permission.
**GOVERNED BY:** Governance system-wide rules; the frozen V003 Specification; Phase 02 ticket-specific authorization.
**CANONICAL SOURCES:** Frozen V003 Specification §9; V003-M05 and V003-M06; legacy FUNC reports as attributed source evidence.
**REFERENCES:** See the local tree and links below.
**POPULATION STATE:** M05 created eight CORE records and retained all eight original reports. M06 populated the EXE index: RESEARCH, BROWSER, FILE, and CODE are admitted for evidence-scoped Codex operations; MEDIA is reserved. FQ_MUST_README, FUNC_REQ, and FUNC_WORKFLOW remain for later content-specific migration.
**LAST VERIFIED:** 2026-10-08
**VERIFIER:** Codex — M05 source inventory plus M06 EXE evidence/index and CORE-reference read-back.
**APPLIES TO:** AI agent capability disclosure and FUNC registry navigation.
**ENTRY NAVIGATION:** Begin with the CORE registry README for current field definitions and agent records.
**EXIT NAVIGATION:** Return to AI_BRAINBOX/README_AI_BRAINBOX.md or the root README_BRAINBOX.md when leaving the FUNC domain.

## Local tree

AI_BRAINBOX/FUNC_AI_BRAINBOX/
├── README_FUNC_AI_BRAINBOX.md
├── FQ_MUST_README.md — retained local compliance checkpoint; M07/M20 disposition
├── FUNC_REQ_BRAINBOX.md — retained function requests; M07/M20 disposition
├── FUNC_WORKFLOW_BRAINBOX.md — retained legacy workflow; M07/M20 disposition
├── CHATGPT_FUNC_BRAINBOX.md — original source retained
├── CLAUDE_FUNC_BRAINBOX.md — original source retained
├── CLINE_FUNC_BRAINBOX.md — original source retained
├── CODEX_FUNC_BRAINBOX.md — original source retained
├── COPILOT_FUNC_BRAINBOX.md — original source retained
├── DEEPSEEK_FUNC_BRAINBOX.md — three-line pending notice retained
├── GROK_FUNC_BRAINBOX.md — original source retained
├── QWEN_FUNC_BRAINBOX.md — three-line pending notice retained
├── AI_AGENTS_CORE_FUNC_BRAINBOX/
    ├── README_AI_AGENTS_CORE_FUNC_BRAINBOX.md
    ├── CHATGPT_CORE_FUNC_BRAINBOX.md
    ├── CLAUDE_CORE_FUNC_BRAINBOX.md
    ├── CLINE_CORE_FUNC_BRAINBOX.md
    ├── CODEX_CORE_FUNC_BRAINBOX.md
    ├── COPILOT_CORE_FUNC_BRAINBOX.md
    ├── DEEPSEEK_CORE_FUNC_BRAINBOX.md
    ├── GROK_CORE_FUNC_BRAINBOX.md
    └── QWEN_CORE_FUNC_BRAINBOX.md
└── AI_AGENTS_EXE_FUNC_BRAINBOX/
    ├── README_AI_AGENTS_EXE_FUNC_BRAINBOX.md
    ├── RESEARCH_EXE_FUNC_BRAINBOX/README_RESEARCH_EXE_FUNC_BRAINBOX.md
    ├── BROWSER_EXE_FUNC_BRAINBOX/README_BROWSER_EXE_FUNC_BRAINBOX.md
    ├── FILE_EXE_FUNC_BRAINBOX/README_FILE_EXE_FUNC_BRAINBOX.md
    ├── CODE_EXE_FUNC_BRAINBOX/README_CODE_EXE_FUNC_BRAINBOX.md
    └── MEDIA_EXE_FUNC_BRAINBOX/README_MEDIA_EXE_FUNC_BRAINBOX.md - reserved

## Domain boundaries

- CORE records summarize evidence-backed and explicitly unknown agent capabilities.
- M06 populated the evidence-backed EXE index; category admission and evidence limits are recorded in its linked records.
- Reusable knowledge and skill content belongs to Skills.
- Procedures, routing, and operating sequences belong to the appropriate workflow or DEVOPS domain.
- FQ_MUST_README.md, FUNC_REQ_BRAINBOX.md, and FUNC_WORKFLOW_BRAINBOX.md remain in place until their own authorized migration and source-retirement gates. M05 does not rewrite or remove them.

## Canonical references

- [CORE registry](AI_AGENTS_CORE_FUNC_BRAINBOX/README_AI_AGENTS_CORE_FUNC_BRAINBOX.md)
- [EXE capability index](AI_AGENTS_EXE_FUNC_BRAINBOX/README_AI_AGENTS_EXE_FUNC_BRAINBOX.md)
- [FQ local compliance source](FQ_MUST_README.md)
- [Function requests source](FUNC_REQ_BRAINBOX.md)
- [Function workflow source](FUNC_WORKFLOW_BRAINBOX.md)
- [Frozen V003 Specification](../../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md)
- [V003 Phase 02 ticket set](../../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_PHASE02_MIGRATION_TICKETS_BRAINBOX.md)
- [Governance evidence rules](../../GOVERNANCE_BRAINBOX/EVIDENCE_GOV_BRAINBOX.md)
- [Governance ticketing rules](../../GOVERNANCE_BRAINBOX/TICKETING_GOV_BRAINBOX.md)

**STATUS:** [M06 IMPLEMENTATION COMMITTED/PUSHED AT 9635e5d; FOUR CATEGORIES ADMITTED; MEDIA RESERVED; INDEPENDENT VERIFICATION PENDING]


---

## Independent verification status — 2026-10-09

M05 CORE and M06 EXE independently verify **PASS**. RESEARCH/BROWSER/FILE/CODE are admitted only for the evidence-scoped Codex operations in frozen §9; MEDIA remains reserved. M07 may proceed after the M06 verification-closeout commit and clean handoff.

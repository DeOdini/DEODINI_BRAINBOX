# README_FUNC_AI_BRAINBOX.md

**PARENT:** AI_BRAINBOX/FUNC_AI_BRAINBOX/
**CURRENT DOMAIN:** Functional capability records and execution-capability indexing for AI agents
**PURPOSE:** Navigate retained agent-source reports and the new CORE capability registry while keeping functional capability separate from reusable knowledge and operational workflow.
**MENTAL MODEL:** FUNC records what an agent is exposed to and can do, what is connected and authenticated, what execution is evidenced, what is authorized, and the limitations. A tool or skill being listed does not prove connection, execution, or permission.
**GOVERNED BY:** Governance system-wide rules; the frozen V003 Specification; Phase 02 ticket-specific authorization.
**CANONICAL SOURCES:** Frozen V003 Specification §§9–10; V003-M05/M06/M07; legacy FUNC reports as attributed source evidence.
**REFERENCES:** See the local tree and links below.
**POPULATION STATE:** M05 CORE and M06 EXE remain populated; M07 classified all three ancillary sources section-by-section, without moving or rewriting them. Workflow/technology destinations remain with M08–M10 where applicable.
**LAST VERIFIED:** 2026-10-10 ? Codex M19 README tree/reference reconciliation; substantive source evidence and execution claims were not re-run.
**VERIFIER:** Codex — M07 source-section classification and M01 hash recheck; M05/M06 PASS per the independent verification archive.
**APPLIES TO:** AI agent capability disclosure and FUNC registry navigation.
**ENTRY NAVIGATION:** Begin with the CORE registry README for current field definitions and agent records.
**EXIT NAVIGATION:** Return to AI_BRAINBOX/README_AI_BRAINBOX.md or the root README_BRAINBOX.md when leaving the FUNC domain.

## Canonical local tree — two descendant levels

Current navigation snapshot; physical/population tags follow [Tree and status governance](../../GOVERNANCE_BRAINBOX/TREE_AND_STATUS_GOV_BRAINBOX.md). This local view shows every direct child and each directory child’s direct children. For a deeper path, open the corresponding child README; consult the root README for the complete tree.

```text
FUNC_AI_BRAINBOX/ [PRESENT · POPULATED]
├── AI_AGENTS_CORE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   ├── CHATGPT_CORE_FUNC_BRAINBOX.md [PRESENT]
│   ├── CLAUDE_CORE_FUNC_BRAINBOX.md [PRESENT]
│   ├── CLINE_CORE_FUNC_BRAINBOX.md [PRESENT]
│   ├── CODEX_CORE_FUNC_BRAINBOX.md [PRESENT]
│   ├── COPILOT_CORE_FUNC_BRAINBOX.md [PRESENT]
│   ├── DEEPSEEK_CORE_FUNC_BRAINBOX.md [PRESENT]
│   ├── GROK_CORE_FUNC_BRAINBOX.md [PRESENT]
│   ├── QWEN_CORE_FUNC_BRAINBOX.md [PRESENT]
│   └── README_AI_AGENTS_CORE_FUNC_BRAINBOX.md [PRESENT]
├── AI_AGENTS_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   ├── BROWSER_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   ├── CHATGPT_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   ├── CLAUDE_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   ├── CLINE_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   ├── CODE_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   ├── CODEX_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   ├── COPILOT_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   ├── DEEPSEEK_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   ├── FILE_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   ├── GROK_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   ├── MEDIA_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   ├── QWEN_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   ├── RESEARCH_EXE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
│   └── README_AI_AGENTS_EXE_FUNC_BRAINBOX.md [PRESENT]
├── CHATGPT_FUNC_BRAINBOX.md [PRESENT]
├── CLAUDE_FUNC_BRAINBOX.md [PRESENT]
├── CLINE_FUNC_BRAINBOX.md [PRESENT]
├── CODEX_FUNC_BRAINBOX.md [PRESENT]
├── COPILOT_FUNC_BRAINBOX.md [PRESENT]
├── DEEPSEEK_FUNC_BRAINBOX.md [PRESENT]
├── FQ_MUST_README.md [PRESENT]
├── FUNC_REQ_BRAINBOX.md [PRESENT]
├── FUNC_WORKFLOW_BRAINBOX.md [PRESENT]
├── GROK_FUNC_BRAINBOX.md [PRESENT]
├── QWEN_FUNC_BRAINBOX.md [PRESENT]
└── README_FUNC_AI_BRAINBOX.md [PRESENT]
```

## Current-tree reference

The current physical structure is shown in the canonical two-descendant-level local tree above. The complete project tree is maintained only in the root README.

## Domain boundaries

- CORE records summarize evidence-backed and explicitly unknown agent capabilities.
- M06 populated the evidence-backed EXE index; category admission and evidence limits are recorded in its linked records.
- Reusable knowledge and skill content belongs to Skills.
- Procedures, routing, and operating sequences belong to the appropriate workflow or DEVOPS domain.
- FQ_MUST_README.md, FUNC_REQ_BRAINBOX.md, and FUNC_WORKFLOW_BRAINBOX.md remain at their original paths. M07 classified their sections without moving or rewriting the original bodies. F08 added a routing notice to FQ_MUST_README.md while preserving its historical body. M20 review is complete; source-specific safeguards govern future action.

## M07 ancillary-source classification

| Retained source | Current canonical disposition | Follow-up |
|---|---|---|
| FQ_MUST_README.md | Governance owns current system-wide rules; FUNC README keeps local navigation. Legacy request-file/compliance-file sequence is not recreated. | M20 review complete; F08 notice routes current readers to the root, FUNC, and Governance authorities; historical body preserved |
| FUNC_REQ_BRAINBOX.md | M05 CORE records own current capability-report schema; Governance owns evidence, naming, documentation, and ticketing rules. | M20 review complete; source-specific disposition remains recorded in Phase 03 |
| FUNC_WORKFLOW_BRAINBOX.md | Mixed workflow is historical/reference-only pending content-specific destination. Generic technology knowledge may fit M08; DEVOPS/Fullstack processes are candidates for M09/M10. n8n/email remain unproven. | M08/M09/M10 classified only their authorized content; M20 review complete; source-specific disposition remains recorded in Phase 03 |

No policy text was copied into FUNC. All three legacy sources remain at their original paths; F08 adds only a routing notice to FQ, with the historical body byte-for-byte preserved. The detailed per-section ledger is in the [M01 migration map](../../VERSION_HISTORY_BRAINBOX/V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md); the execution report is in the [Phase 02 report](../../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_MIGRATION_REPORT_VERSION_UPGRADE_BRAINBOX.md).

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

**STATUS:** [M05 CORE PASS; M06 EXE PASS; M07 INDEPENDENT VERIFICATION: PASS (Batch B closeout, 2026-10-09); Batch B merged]


---

## Independent verification status — 2026-10-09

M05 CORE and M06 EXE independently verify **PASS**. RESEARCH/BROWSER/FILE/CODE are admitted only for the evidence-scoped Codex operations in frozen §9; MEDIA remains reserved. M07 may proceed after the M06 verification-closeout commit and clean handoff.


---

## Independent verification status — M07 (2026-10-09)

M07 ancillary-source classification independently verifies **PASS**. All three retained sources remain byte-for-byte at the M01 baseline; no duplicate Governance policy was created; n8n/email automation remains UNPROVEN / NOT VERIFIED. M07-WF-01 and M07-AUTH-01 are non-blocking carry-forwards.

---

## V003 CORE/EXE questionnaire routing — 2026-10-15

[CORE](AI_AGENTS_CORE_FUNC_BRAINBOX/README_AI_AGENTS_CORE_FUNC_BRAINBOX.md) owns declared abilities and connectivity; [EXE](AI_AGENTS_EXE_FUNC_BRAINBOX/README_AI_AGENTS_EXE_FUNC_BRAINBOX.md) owns each agent operation, evidence, verification and permission. Category folders only index agent operation anchors. Existing M05/M06 historical evidence and frozen Specification §9 remain authoritative as dated records; no runtime success or authorization inferred.


## Agent path discovery requirement

Before selecting a file path, consult the [Tree and Status Governance](../../GOVERNANCE_BRAINBOX/TREE_AND_STATUS_GOV_BRAINBOX.md) and the local two-level tree of the current folder; follow the child README to discover deeper paths. Verify existence instead of guessing; do not infer implementation from presence or populated documentation.

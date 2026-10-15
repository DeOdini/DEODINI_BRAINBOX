# README_AI_AGENTS_CORE_FUNC_BRAINBOX.md

**PARENT:** AI_BRAINBOX/FUNC_AI_BRAINBOX/AI_AGENTS_CORE_FUNC_BRAINBOX/
**CURRENT DOMAIN:** Core capability records for the named AI agents
**PURPOSE:** Provide a source-backed, per-agent view of exposed tools and capabilities, connection state, authentication, verified execution, authorization, and limitations.
**MENTAL MODEL:** Exposure is not connection; connection is not authentication; authentication is not execution; execution is not authorization.
**GOVERNED BY:** Governance evidence and ticketing rules; frozen V003 Specification §9; M05 CORE and M06 EXE migration records.
**CANONICAL SOURCES:** Frozen V003 Specification §9; each agent's retained FUNC source report, except DeepSeek and Qwen, whose approved role baseline is in Specification §9.
**REFERENCES:** The parent FUNC README and linked source records.
**POPULATION STATE:** Eight CORE records remain; M06 added their evidence-scoped EXE links. Four categories are admitted for Codex; Copilot's Browser configuration is explicitly unverified; MEDIA is reserved. Historical agent claims remain time-bounded.
**LAST VERIFIED:** 2026-10-10 ? Codex M19 README tree/reference reconciliation; substantive source evidence and execution claims were not re-run.
**VERIFIER:** Codex — M05 source/hash cross-check and M06 CORE-to-EXE reference reconciliation; M06 commit `9635e5d` pushed.
**APPLIES TO:** ChatGPT, Claude, Cline, Codex, Copilot, DeepSeek, Grok, and Qwen.

## Canonical local tree — two descendant levels

Current navigation snapshot; physical/population tags follow [Tree and status governance](../../../GOVERNANCE_BRAINBOX/TREE_AND_STATUS_GOV_BRAINBOX.md). This local view shows every direct child and each directory child’s direct children. For a deeper path, open the corresponding child README; consult the root README for the complete tree.

```text
AI_AGENTS_CORE_FUNC_BRAINBOX/ [PRESENT · POPULATED]
├── CHATGPT_CORE_FUNC_BRAINBOX.md [PRESENT]
├── CLAUDE_CORE_FUNC_BRAINBOX.md [PRESENT]
├── CLINE_CORE_FUNC_BRAINBOX.md [PRESENT]
├── CODEX_CORE_FUNC_BRAINBOX.md [PRESENT]
├── COPILOT_CORE_FUNC_BRAINBOX.md [PRESENT]
├── DEEPSEEK_CORE_FUNC_BRAINBOX.md [PRESENT]
├── GROK_CORE_FUNC_BRAINBOX.md [PRESENT]
├── QWEN_CORE_FUNC_BRAINBOX.md [PRESENT]
└── README_AI_AGENTS_CORE_FUNC_BRAINBOX.md [PRESENT]
```

## Current-tree reference

The current physical structure is shown in the canonical two-descendant-level local tree above. The complete project tree is maintained only in the root README.

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

**STATUS:** [M05/M06 independently verified PASS during Batch B closeout (2026-10-09); both ticket branches merged]


---

## Independent verification status — 2026-10-09

M05 CORE and the M06 CORE↔EXE reconciliation independently verify **PASS**. Codex maps to RESEARCH/BROWSER/FILE/CODE; Copilot Browser remains unverified; Cline MEDIA remains reserved-only; ChatGPT/Claude/DeepSeek/Grok/Qwen have no admitted EXE category from M06.

---

## V003 CORE questionnaire — 2026-10-15

CORE = agent capability inventory; NOT execution evidence. Agent must answer in own CORE file with dated CORE item IDs.
1. C01 Identity, model if known, runtime, workspace, date, source of claim?
2. C02 For EVERY visible native tool, connector, MCP/API, plugin and skill: exact name, linkage, provider, purpose and advertised functions?
3. C03 For each item independently: exposed, installed, configured, connected, authenticated, offline, untested? Last direct evidence, account/project/device scope?
4. C04 Skill dependencies, skills versus credentials and connection requirements?
5. C05 RDC devices, local/remote files, Git, browser, terminal and other resource access, boundaries and permission?
6. C06 Email/calendar/communications: accounts, read/draft/send access, authorization?
7. C07 Automation: n8n, Activepieces, native automation: available/configured/connected/authenticated; triggers and limitations, no claim of tested workflow?
8. C08 Professional tasks in principle: frontend, backend, data, research, media, design, DevOps; constraints and unknowns?
9. C09 Additional potential tools, how linked and why useful?
10. C10 One row per CORE ID: tool, type, state dimensions, purpose, permissions, evidence and last checked, linked agent EXE record if present.
Do not expose secrets or test external modifications; historical claims are not current runtime proof.


## Agent path discovery requirement

Before selecting a file path, consult the [Tree and Status Governance](../../../GOVERNANCE_BRAINBOX/TREE_AND_STATUS_GOV_BRAINBOX.md) and the local two-level tree of the current folder; follow the child README to discover deeper paths. Verify existence instead of guessing; do not infer implementation from presence or populated documentation.

# README_SKILLS_AI_BRAINBOX

**STATUS:** [ACTIVE] — M08 Skills taxonomy root and local navigation
**PARENT:** AI_BRAINBOX/
**CURRENT DOMAIN:** Reusable competencies, commands, languages, formats, technologies, prompts, patterns, troubleshooting, security, and references.
**PURPOSE:** Provide one navigable home for reusable knowledge while keeping agent capability, system workflow, project evidence, and Governance policy in their canonical domains.
**MENTAL MODEL:** Skills AI is what execution can know and draw from. FUNC records what an agent can do; DEVOPS describes how work proceeds; Governance owns system-wide rules.
**GOVERNED BY:** De O'Dini — Operator; Governance for system-wide rules; frozen V003 Specification for the approved taxonomy.
**AUTHORITATIVE TREE:** Frozen V003 Specification §8; this README exposes its full local branch.
**LOCAL TREE:** Exact approved Skills subtree plus the two M08 content records in existing approved branches.
**RELATED DOMAINS:** FUNC, DEVOPS, Governance, Fullstack, FootHive evidence, and Version History.
**CANONICAL SOURCES:** Frozen V003 Specification §§8 and 15–20; V003 Origin Conversation; Governance.
**REFERENCES:** See Sources below.
**POPULATION STATE:** Taxonomy directories exist. The four legacy Skills content files remain empty and unchanged. One bounded command reference and one Governance-linked guardrail prompt are populated; other domains are marked accurately below.
**LAST VERIFIED:** 2026-10-09 — Codex read-back after implementation.
**VERIFIER:** Codex implementation read-back; ChatGPT independent verification pending.
**APPLIES TO:** Operators and AI agents using reusable DEODINI Brainbox knowledge.

## Authority and content boundaries

This is the Skills domain root and local navigation authority. It does not replace the frozen V003 Specification or rewrite the Origin Conversation. An approved branch does not imply populated knowledge, an installed tool, successful execution, or Operator authorization.

- Governance remains canonical for system-wide policy. Guardrail prompts translate applicable Governance rules into task-time instructions; they do not create a competing policy.
- FUNC CORE/EXE records remain canonical for agent capabilities and execution evidence.
- DEVOPS and Fullstack own execution procedures and project-specific system application.
- Reusable technology profiles belong here only when the approved technology admission rule and source evidence support them.
- A planned or empty branch must not be described as proven knowledge.

## Local tree

```text
SKILLS_AI_BRAINBOX/
├── README_SKILLS_AI_BRAINBOX.md
├── SKILLS_BRAINBOX/
│   ├── README_SKILLS_BRAINBOX.md
│   ├── DEBUGGING_SKILLS_BRAINBOX/
│   ├── CODE_REVIEW_SKILLS_BRAINBOX/
│   ├── SYSTEM_DESIGN_SKILLS_BRAINBOX/
│   ├── ROOT_CAUSE_ANALYSIS_SKILLS_BRAINBOX/
│   ├── INCIDENT_RESPONSE_SKILLS_BRAINBOX/
│   ├── PERFORMANCE_SKILLS_BRAINBOX/
│   ├── ACCESSIBILITY_SKILLS_BRAINBOX/
│   ├── RESPONSIVE_DESIGN_SKILLS_BRAINBOX/
│   ├── DATABASE_DESIGN_SKILLS_BRAINBOX/
│   ├── API_DESIGN_SKILLS_BRAINBOX/
│   ├── SECURITY_REVIEW_SKILLS_BRAINBOX/
│   ├── TESTING_STRATEGY_SKILLS_BRAINBOX/
│   ├── GIT_OPERATIONS_SKILLS_BRAINBOX/
│   ├── DEPLOYMENT_SKILLS_BRAINBOX/
│   ├── TECHNICAL_WRITING_SKILLS_BRAINBOX/
│   └── REQUIREMENTS_ANALYSIS_SKILLS_BRAINBOX/
├── COMMANDS_SKILLS_BRAINBOX/
│   ├── README_COMMANDS_SKILLS_BRAINBOX.md
│   ├── GIT_COMMANDS_BRAINBOX/
│   ├── BASH_COMMANDS_BRAINBOX/
│   ├── POWERSHELL_COMMANDS_BRAINBOX/
│   ├── CMD_COMMANDS_BRAINBOX/
│   ├── ZSH_COMMANDS_BRAINBOX/
│   ├── LINUX_COMMANDS_BRAINBOX/
│   ├── WINDOWS_COMMANDS_BRAINBOX/
│   ├── PYTHON_COMMANDS_BRAINBOX/
│   ├── DOCKER_COMMANDS_BRAINBOX/
│   ├── KUBERNETES_COMMANDS_BRAINBOX/
│   ├── TERRAFORM_COMMANDS_BRAINBOX/
│   ├── CLOUD_CLI_COMMANDS_BRAINBOX/
│   │   ├── AWS_CLI_COMMANDS_BRAINBOX/
│   │   ├── AZURE_CLI_COMMANDS_BRAINBOX/
│   │   └── GCLOUD_CLI_COMMANDS_BRAINBOX/
│   ├── PACKAGE_COMMANDS_BRAINBOX/
│   │   ├── NPM_COMMANDS_BRAINBOX/
│   │   ├── NPX_COMMANDS_BRAINBOX/
│   │   ├── PNPM_COMMANDS_BRAINBOX/
│   │   ├── YARN_COMMANDS_BRAINBOX/
│   │   ├── PIP_COMMANDS_BRAINBOX/
│   │   ├── UV_COMMANDS_BRAINBOX/
│   │   └── NPM_NPX_POWERSHELL_COMMAND_REFERENCE_BRAINBOX.md
│   ├── DATABASE_COMMANDS_BRAINBOX/
│   │   ├── POSTGRESQL_COMMANDS_BRAINBOX/
│   │   ├── MYSQL_COMMANDS_BRAINBOX/
│   │   ├── SQLITE_COMMANDS_BRAINBOX/
│   │   ├── MONGODB_COMMANDS_BRAINBOX/
│   │   └── REDIS_COMMANDS_BRAINBOX/
│   └── NETWORK_COMMANDS_BRAINBOX/
│       ├── CURL_COMMANDS_BRAINBOX/
│       ├── SSH_COMMANDS_BRAINBOX/
│       ├── DNS_COMMANDS_BRAINBOX/
│       └── NETWORK_DIAGNOSTIC_COMMANDS_BRAINBOX/
├── LANGUAGES_SKILLS_BRAINBOX/
│   ├── README_LANGUAGES_SKILLS_BRAINBOX.md
│   ├── JAVASCRIPT_LANGUAGE_BRAINBOX/
│   ├── TYPESCRIPT_LANGUAGE_BRAINBOX/
│   ├── PYTHON_LANGUAGE_BRAINBOX/
│   ├── JAVA_LANGUAGE_BRAINBOX/
│   ├── C_LANGUAGE_BRAINBOX/
│   ├── CPP_LANGUAGE_BRAINBOX/
│   ├── CSHARP_LANGUAGE_BRAINBOX/
│   ├── GO_LANGUAGE_BRAINBOX/
│   ├── RUST_LANGUAGE_BRAINBOX/
│   ├── PHP_LANGUAGE_BRAINBOX/
│   ├── RUBY_LANGUAGE_BRAINBOX/
│   ├── SWIFT_LANGUAGE_BRAINBOX/
│   ├── KOTLIN_LANGUAGE_BRAINBOX/
│   └── SQL_LANGUAGE_BRAINBOX/
├── SYNTAX_FORMATS_SKILLS_BRAINBOX/
│   ├── README_SYNTAX_FORMATS_SKILLS_BRAINBOX.md
│   └── TOML_FORMAT_BRAINBOX/
├── TECHNOLOGIES_SKILLS_BRAINBOX/
│   ├── README_TECHNOLOGIES_SKILLS_BRAINBOX.md
│   ├── VERSION_CONTROL_TECHNOLOGIES_BRAINBOX/
│   │   ├── GIT_TECHNOLOGY_BRAINBOX/
│   │   ├── GITHUB_TECHNOLOGY_BRAINBOX/
│   │   ├── GITLAB_TECHNOLOGY_BRAINBOX/
│   │   └── BITBUCKET_TECHNOLOGY_BRAINBOX/
│   ├── CONTAINER_TECHNOLOGIES_BRAINBOX/
│   │   ├── DOCKER_TECHNOLOGY_BRAINBOX/
│   │   ├── PODMAN_TECHNOLOGY_BRAINBOX/
│   │   └── CONTAINERD_TECHNOLOGY_BRAINBOX/
│   ├── ORCHESTRATION_TECHNOLOGIES_BRAINBOX/
│   │   ├── KUBERNETES_TECHNOLOGY_BRAINBOX/
│   │   ├── HELM_TECHNOLOGY_BRAINBOX/
│   │   └── KUSTOMIZE_TECHNOLOGY_BRAINBOX/
│   ├── INFRASTRUCTURE_TECHNOLOGIES_BRAINBOX/
│   │   ├── TERRAFORM_TECHNOLOGY_BRAINBOX/
│   │   ├── OPENTOFU_TECHNOLOGY_BRAINBOX/
│   │   ├── ANSIBLE_TECHNOLOGY_BRAINBOX/
│   │   └── PULUMI_TECHNOLOGY_BRAINBOX/
│   ├── CLOUD_TECHNOLOGIES_BRAINBOX/
│   │   ├── AWS_TECHNOLOGY_BRAINBOX/
│   │   ├── AZURE_TECHNOLOGY_BRAINBOX/
│   │   └── GCP_TECHNOLOGY_BRAINBOX/
│   ├── TESTING_TECHNOLOGIES_BRAINBOX/
│   │   ├── PLAYWRIGHT_TECHNOLOGY_BRAINBOX/
│   │   ├── CYPRESS_TECHNOLOGY_BRAINBOX/
│   │   ├── SELENIUM_TECHNOLOGY_BRAINBOX/
│   │   ├── JEST_TECHNOLOGY_BRAINBOX/
│   │   └── PYTEST_TECHNOLOGY_BRAINBOX/
│   ├── DATABASE_TECHNOLOGIES_BRAINBOX/
│   │   ├── POSTGRESQL_TECHNOLOGY_BRAINBOX/
│   │   ├── MYSQL_TECHNOLOGY_BRAINBOX/
│   │   ├── SQLITE_TECHNOLOGY_BRAINBOX/
│   │   ├── MONGODB_TECHNOLOGY_BRAINBOX/
│   │   └── REDIS_TECHNOLOGY_BRAINBOX/
│   ├── DEPLOYMENT_TECHNOLOGIES_BRAINBOX/
│   │   ├── NETLIFY_TECHNOLOGY_BRAINBOX/
│   │   ├── VERCEL_TECHNOLOGY_BRAINBOX/
│   │   └── CLOUDFLARE_TECHNOLOGY_BRAINBOX/
│   ├── ANALYTICS_TECHNOLOGIES_BRAINBOX/
│   │   └── GA4_TECHNOLOGY_BRAINBOX/
│   ├── DESIGN_TECHNOLOGIES_BRAINBOX/
│   │   ├── FIGMA_TECHNOLOGY_BRAINBOX/
│   │   └── FRAMER_TECHNOLOGY_BRAINBOX/
│   └── AI_TECHNOLOGIES_BRAINBOX/
│       ├── MCP_TECHNOLOGY_BRAINBOX/
│       ├── LANGCHAIN_TECHNOLOGY_BRAINBOX/
│       ├── LLAMAINDEX_TECHNOLOGY_BRAINBOX/
│       └── OLLAMA_TECHNOLOGY_BRAINBOX/
├── PROMPTS_SKILLS_BRAINBOX/
│   ├── README_PROMPTS_SKILLS_BRAINBOX.md
│   ├── SYSTEM_PROMPTS_BRAINBOX/
│   ├── TASK_PROMPTS_BRAINBOX/
│   ├── RESEARCH_PROMPTS_BRAINBOX/
│   ├── CODING_PROMPTS_BRAINBOX/
│   ├── DEBUGGING_PROMPTS_BRAINBOX/
│   ├── REVIEW_PROMPTS_BRAINBOX/
│   ├── AUDIT_PROMPTS_BRAINBOX/
│   ├── TESTING_PROMPTS_BRAINBOX/
│   ├── DOCUMENTATION_PROMPTS_BRAINBOX/
│   ├── UI_UX_PROMPTS_BRAINBOX/
│   ├── AGENT_HANDOFF_PROMPTS_BRAINBOX/
│   ├── TOOL_USE_PROMPTS_BRAINBOX/
│   ├── STRUCTURED_OUTPUT_PROMPTS_BRAINBOX/
│   ├── RAG_PROMPTS_BRAINBOX/
│   ├── EVALUATION_PROMPTS_BRAINBOX/
│   └── GUARDRAIL_PROMPTS_BRAINBOX/
│       └── GUARDRAIL_PREFLIGHT_PROMPT_BRAINBOX.md
├── PATTERNS_SKILLS_BRAINBOX/
│   ├── README_PATTERNS_SKILLS_BRAINBOX.md
│   ├── CODE_PATTERNS_SKILLS_BRAINBOX/
│   ├── ARCHITECTURE_PATTERNS_SKILLS_BRAINBOX/
│   ├── INTEGRATION_PATTERNS_SKILLS_BRAINBOX/
│   ├── SECURITY_PATTERNS_SKILLS_BRAINBOX/
│   ├── TESTING_PATTERNS_SKILLS_BRAINBOX/
│   ├── DATA_PATTERNS_SKILLS_BRAINBOX/
│   ├── ERROR_HANDLING_PATTERNS_BRAINBOX/
│   └── AI_AGENT_PATTERNS_BRAINBOX/
├── TROUBLESHOOTING_SKILLS_BRAINBOX/
│   └── README_TROUBLESHOOTING_SKILLS_BRAINBOX.md
├── SECURITY_SKILLS_BRAINBOX/
│   └── README_SECURITY_SKILLS_BRAINBOX.md
└── REFERENCES_SKILLS_BRAINBOX/
    └── README_REFERENCES_SKILLS_BRAINBOX.md
```

## Current population register

| Domain | State | M08 disposition |
|---|---|---|
| Skills competencies | [EMPTY] / [PLANNED] | No content was present in the four legacy RAW/PROVEN/REUSABLE/FAILED records. No competencies were fabricated. |
| Commands | [POPULATED — bounded reference] | One canonical npm/npx/PowerShell relationship record is under PACKAGE_COMMANDS_BRAINBOX; other locations reference it. No command was run for this migration. |
| Languages | [EMPTY] / [PLANNED] | Language taxonomy is present; no language skill content was copied from an empty legacy source. |
| Syntax/formats | [EMPTY] / [PLANNED] | TOML is correctly classified as a format, not a command. |
| Technologies | [REFERENCE] / [EMPTY] / [PLANNED] | Approved technology slots remain distinct from actual reusable profile population; see the technology register. |
| Prompts | [POPULATED — one guardrail preflight prompt] | It operationalizes Governance and points back to canonical policy. Other prompt families remain empty. |
| Patterns | [EMPTY] / [PLANNED] | Generic reusable pattern content has not been evidenced in the inspected Skills sources. |
| Troubleshooting | [REFERENCE] | Points to the single package-command explanation; no duplicate content. |
| Security | [REFERENCE] | Governance remains the policy owner. No policy copy was created here. |
| References | [POPULATED — navigation] | Pointers identify authorities and retained source records; they do not claim those sources have migrated. |

## Legacy source boundary

The retained source remains at AI_BRAINBOX/SKILLS_AVAIL_AI_BRAINBOX/. Its README describes the former evidence buckets. RAW_SKILLS_BRAINBOX.md, PROVEN_SKILLS_BRAINBOX.md, REUSABLE_SKILLS_BRAINBOX.md, and FAILED_SKILLS_BRAINBOX.md were empty at M01 and remain unchanged. M08 does not delete, rename, or rewrite them. M19 owns reference reconciliation; M20 is the source-by-source retirement gate.

## Sources

- [Frozen V003 Specification](../../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md), §§8 and 15–20.
- [V003 Origin Conversation](../../V003_VERSION_UPGRADE_BRAINBOX/V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md), Skills and technology admission discussion.
- [Governance README](../../GOVERNANCE_BRAINBOX/README_GOV_BRAINBOX.md).
- [Governance Security](../../GOVERNANCE_BRAINBOX/SECURITY_GOV_BRAINBOX.md).
- [Migration map](../../VERSION_HISTORY_BRAINBOX/V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md), M01 baseline and M08 disposition.
- [Retained legacy Skills README](../SKILLS_AVAIL_AI_BRAINBOX/SKILLS_MUST_README.md).
- [Phase 02 migration report](../../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_MIGRATION_REPORT_VERSION_UPGRADE_BRAINBOX.md), M07 classification and M08 closeout.

**GIT DIRECTORY MARKERS:** Any .gitkeep files below are Git-only markers to retain empty approved folders. They are not Brainbox knowledge, evidence, or population claims.


---

## Independent verification status — 2026-10-09

V003-M08 independently verifies **PASS**. The physical Skills taxonomy matches frozen §8 exactly, retained legacy Skills sources remain unchanged, empty placeholders remain unpopulated, and canonical/reference boundaries are preserved.


## Batch B Git closure — 2026-10-09

V003-M08 independently verifies PASS and is merged to main through PR #25. The M08 branch remains available. Batch B M05–M08 is merged in order; the detailed Git and flag disposition is recorded in the Phase 02 migration report.

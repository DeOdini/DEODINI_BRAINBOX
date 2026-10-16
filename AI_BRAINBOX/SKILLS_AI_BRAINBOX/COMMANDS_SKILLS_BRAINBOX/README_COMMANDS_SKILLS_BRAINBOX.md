# README_COMMANDS_SKILLS_BRAINBOX

**STATUS:** [ACTIVE] — command knowledge taxonomy
**PARENT:** AI_BRAINBOX/SKILLS_AI_BRAINBOX/
**CURRENT DOMAIN:** Operational command and CLI knowledge.
**PURPOSE:** Keep invocation syntax and command behavior in a canonical command domain.
**MENTAL MODEL:** Commands own syntax and operational invocation; named platform knowledge belongs to Technologies when reusable.
**GOVERNED BY:** Governance Naming, Documentation, Evidence, Security, and Reference.
**AUTHORITATIVE TREE:** Frozen V003 Specification §8.
**LOCAL TREE:** Approved command groups and nested branches are listed below.
**RELATED DOMAINS:** Technologies, Languages, Troubleshooting, FUNC, and DEVOPS.
**CANONICAL SOURCES:** Frozen V003 Specification §§8 and 16.
**REFERENCES:** See Sources and the single package-command explanation.
**POPULATION STATE:** One bounded package-command reference is [POPULATED]; remaining command branches are [EMPTY] / [PLANNED].
**LAST VERIFIED:** 2026-10-10 ? Codex M19 README tree/reference reconciliation; substantive source evidence and execution claims were not re-run.
**VERIFIER:** Codex implementation read-back; ChatGPT independent M08 verification: PASS (Batch B closeout, 2026-10-09).

## Canonical local tree — two descendant levels

Current navigation snapshot; physical/population tags follow [Tree and status governance](../../../GOVERNANCE_BRAINBOX/TREE_AND_STATUS_GOV_BRAINBOX.md). This local view shows every direct child and each directory child’s direct children. For a deeper path, open the corresponding child README; consult the root README for the complete tree.

```text
COMMANDS_SKILLS_BRAINBOX/ [PRESENT · POPULATED]
├── BASH_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── CLOUD_CLI_COMMANDS_BRAINBOX/ [PRESENT · POPULATED]
│   ├── AWS_CLI_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   ├── AZURE_CLI_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   ├── GCLOUD_CLI_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   └── README_CLOUD_CLI_COMMANDS_BRAINBOX.md [PRESENT]
├── CMD_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── DATABASE_COMMANDS_BRAINBOX/ [PRESENT · POPULATED]
│   ├── MONGODB_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   ├── MYSQL_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   ├── POSTGRESQL_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   ├── REDIS_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   ├── SQLITE_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   └── README_DATABASE_COMMANDS_BRAINBOX.md [PRESENT]
├── DOCKER_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── GIT_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── KUBERNETES_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── LINUX_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── NETWORK_COMMANDS_BRAINBOX/ [PRESENT · POPULATED]
│   ├── CURL_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   ├── DNS_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   ├── NETWORK_DIAGNOSTIC_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   ├── SSH_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   └── README_NETWORK_COMMANDS_BRAINBOX.md [PRESENT]
├── PACKAGE_COMMANDS_BRAINBOX/ [PRESENT · POPULATED]
│   ├── NPM_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   ├── NPX_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   ├── PIP_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   ├── PNPM_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   ├── UV_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   ├── YARN_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   ├── NPM_NPX_POWERSHELL_COMMAND_REFERENCE_BRAINBOX.md [PRESENT]
│   └── README_PACKAGE_COMMANDS_BRAINBOX.md [PRESENT]
├── POWERSHELL_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── PYTHON_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── TERRAFORM_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── WINDOWS_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
├── ZSH_COMMANDS_BRAINBOX/ [PRESENT · STUB]
│   └── .gitkeep [PRESENT · EMPTY]
└── README_COMMANDS_SKILLS_BRAINBOX.md [PRESENT]
```

## Current-tree reference

The current physical tree is documented in the canonical two-descendant-level local tree above. The complete project tree is maintained only in the root README.

## One canonical npm / npx / PowerShell explanation

The sole shared explanation is [NPM_NPX_POWERSHELL_COMMAND_REFERENCE_BRAINBOX.md](PACKAGE_COMMANDS_BRAINBOX/NPM_NPX_POWERSHELL_COMMAND_REFERENCE_BRAINBOX.md). NPM, NPX, and PowerShell command branches must reference that record instead of copying its content.

Python language knowledge belongs under LANGUAGES; Python CLI knowledge belongs under PYTHON_COMMANDS_BRAINBOX; backend Python implementation patterns belong at the Fullstack Backend target path listed in the frozen Specification. These are distinct responsibilities.

This migration did not execute npm, npx, PowerShell, or a package installation.

## Sources

- [Frozen V003 Specification](../../../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md), §§8, 16, and 17.
- [Governance Reference](../../../GOVERNANCE_BRAINBOX/REFERENCE_GOV_BRAINBOX.md).
- [Canonical package-command explanation](PACKAGE_COMMANDS_BRAINBOX/NPM_NPX_POWERSHELL_COMMAND_REFERENCE_BRAINBOX.md).

**LAST VERIFIED:** 2026-10-09 — Codex read-back after implementation.

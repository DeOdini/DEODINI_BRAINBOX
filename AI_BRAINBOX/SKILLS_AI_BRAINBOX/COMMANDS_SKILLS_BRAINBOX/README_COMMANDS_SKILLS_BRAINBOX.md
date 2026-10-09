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
**LAST VERIFIED:** 2026-10-09 — Codex read-back after implementation.
**VERIFIER:** Codex implementation read-back; ChatGPT independent verification pending.

## Local tree

```text
COMMANDS_SKILLS_BRAINBOX/
├── README_COMMANDS_SKILLS_BRAINBOX.md
├── GIT_COMMANDS_BRAINBOX/
├── BASH_COMMANDS_BRAINBOX/
├── POWERSHELL_COMMANDS_BRAINBOX/
├── CMD_COMMANDS_BRAINBOX/
├── ZSH_COMMANDS_BRAINBOX/
├── LINUX_COMMANDS_BRAINBOX/
├── WINDOWS_COMMANDS_BRAINBOX/
├── PYTHON_COMMANDS_BRAINBOX/
├── DOCKER_COMMANDS_BRAINBOX/
├── KUBERNETES_COMMANDS_BRAINBOX/
├── TERRAFORM_COMMANDS_BRAINBOX/
├── CLOUD_CLI_COMMANDS_BRAINBOX/
│   ├── AWS_CLI_COMMANDS_BRAINBOX/
│   ├── AZURE_CLI_COMMANDS_BRAINBOX/
│   └── GCLOUD_CLI_COMMANDS_BRAINBOX/
├── PACKAGE_COMMANDS_BRAINBOX/
│   ├── NPM_COMMANDS_BRAINBOX/
│   ├── NPX_COMMANDS_BRAINBOX/
│   ├── PNPM_COMMANDS_BRAINBOX/
│   ├── YARN_COMMANDS_BRAINBOX/
│   ├── PIP_COMMANDS_BRAINBOX/
│   ├── UV_COMMANDS_BRAINBOX/
│   └── NPM_NPX_POWERSHELL_COMMAND_REFERENCE_BRAINBOX.md
├── DATABASE_COMMANDS_BRAINBOX/
│   ├── POSTGRESQL_COMMANDS_BRAINBOX/
│   ├── MYSQL_COMMANDS_BRAINBOX/
│   ├── SQLITE_COMMANDS_BRAINBOX/
│   ├── MONGODB_COMMANDS_BRAINBOX/
│   └── REDIS_COMMANDS_BRAINBOX/
└── NETWORK_COMMANDS_BRAINBOX/
    ├── CURL_COMMANDS_BRAINBOX/
    ├── SSH_COMMANDS_BRAINBOX/
    ├── DNS_COMMANDS_BRAINBOX/
    └── NETWORK_DIAGNOSTIC_COMMANDS_BRAINBOX/
```

## One canonical npm / npx / PowerShell explanation

The sole shared explanation is [NPM_NPX_POWERSHELL_COMMAND_REFERENCE_BRAINBOX.md](PACKAGE_COMMANDS_BRAINBOX/NPM_NPX_POWERSHELL_COMMAND_REFERENCE_BRAINBOX.md). NPM, NPX, and PowerShell command branches must reference that record instead of copying its content.

Python language knowledge belongs under LANGUAGES; Python CLI knowledge belongs under PYTHON_COMMANDS_BRAINBOX; backend Python implementation patterns belong at the Fullstack Backend target path listed in the frozen Specification. These are distinct responsibilities.

This migration did not execute npm, npx, PowerShell, or a package installation.

## Sources

- [Frozen V003 Specification](../../../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md), §§8, 16, and 17.
- [Governance Reference](../../../GOVERNANCE_BRAINBOX/REFERENCE_GOV_BRAINBOX.md).
- [Canonical package-command explanation](PACKAGE_COMMANDS_BRAINBOX/NPM_NPX_POWERSHELL_COMMAND_REFERENCE_BRAINBOX.md).

**LAST VERIFIED:** 2026-10-09 — Codex read-back after implementation.

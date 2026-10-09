# NPM_NPX_POWERSHELL_COMMAND_REFERENCE_BRAINBOX

**STATUS:** [POPULATED — canonical cross-reference explanation]
**CANONICAL SOURCE:** Frozen V003 Specification §16 and its approved command/troubleshooting distinction.
**APPLIES TO:** NPM, NPX, PowerShell, and Windows command-resolution references.
**REFERENCED BY:** README_COMMANDS_SKILLS_BRAINBOX.md; NPM_COMMANDS_BRAINBOX; NPX_COMMANDS_BRAINBOX; POWERSHELL_COMMANDS_BRAINBOX.

## Canonical explanation

NPM and NPX are separate command branches. Windows npm installations may expose command shims such as npm.cmd and npx.cmd. In some PowerShell command-resolution or execution-policy situations involving npm.ps1 or npx.ps1, explicitly invoking the corresponding .cmd shim may succeed.

Keep this explanation here and link to it from the three command locations. Do not maintain separate copies in NPM, NPX, and PowerShell records.

## Evidence and limits

This wording is transcribed from the frozen V003 Specification. M08 did not run a package command or test PowerShell behavior. It records an approved reusable distinction, not an execution result or universal guarantee.

## References

- [Frozen V003 Specification](../../../../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md), §16.
- [Commands README](../README_COMMANDS_SKILLS_BRAINBOX.md).
- [Governance Evidence](../../../../GOVERNANCE_BRAINBOX/EVIDENCE_GOV_BRAINBOX.md).

**LAST VERIFIED:** 2026-10-09 — source/read-back only; no command execution.

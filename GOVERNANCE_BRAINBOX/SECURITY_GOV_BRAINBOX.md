# SECURITY_GOV_BRAINBOX

**STATUS:** [ACTIVE — CANONICAL]
**CANONICAL SOURCE:** Frozen V003 Specification §25.7 and the V003 environment rules.
**APPLIES TO:** Secrets and sensitive operational values in Brainbox records and repositories.

## Secret handling

- Never place real secrets, credentials, access tokens, private keys, or session values in committed Brainbox content.
- Do not copy secret values from source files into Governance, reports, screenshots, examples, or tickets.
- Keep local secret-bearing runtime files such as `.env`, `.env.local`, and `.env.production` out of Git. Use a placeholder-only example file when a documented configuration example is needed.
- Workflow notifications may carry routing/status information only; do not include secrets, keys, or source code in email content.
- If a secret may have been exposed, stop copying or publishing it, record the affected path without reproducing the value, and report it through the authorized channel.

## Authority boundary

Tool access or repository visibility does not grant authorization to read unrelated secrets, change credentials, access production, or publish data. Follow the active ticket's scope and the Operator's authority.

## Sources

- [Frozen V003 Specification](../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md), §25.7 and environment/security notes in §8.
- [Legacy function workflow](../AI_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_WORKFLOW_BRAINBOX.md), §§2.6 and 7.2.
- [Function reporting requirements](../AI_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_REQ_BRAINBOX.md), safe examples and limitation disclosure.

**Prepared by:** Codex under the Operator-authorized V003-M03 ticket.
**Last verified:** 2026-10-08

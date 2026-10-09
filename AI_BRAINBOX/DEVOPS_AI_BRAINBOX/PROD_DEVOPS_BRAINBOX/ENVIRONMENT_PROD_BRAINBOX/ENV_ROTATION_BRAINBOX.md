# ENV_ROTATION_BRAINBOX

**STATUS:** [ACTIVE — SAFE PROCEDURE GUIDANCE]
**PARENT:** ENVIRONMENT_PROD_BRAINBOX/
**CURRENT DOMAIN:** Secret rotation procedure
**CANONICAL SOURCE:** Governance Security; frozen V003 Specification §25.7; V003-M14
**LAST VERIFIED:** 2026-10-09

## Safe rotation outline

This procedure is guidance only. M14 did not access production, rotate a credential, or authorize a rotation.

1. Confirm the affected variable, system owner, approved change request, and required approval. Do not include its value in the request.
2. Use the authorized secret manager or deployment environment's protected variable interface. Do not paste the value into repository files, chat, tickets, screenshots, or shell history.
3. Create or rotate the value through the approved service workflow. Keep old and new values out of logs and output.
4. Update only the authorized runtime configuration. Confirm the application/service reference by key name or a redacted presence check, never by printing the value.
5. Validate through the approved procedure and record date, scope, system, verifier, result, and any redacted reference needed for audit.
6. Revoke the old value only after the authorized owner confirms the new value is active and the rollback window is understood.
7. Record the outcome and any incident without recording either value.

Stop if ownership, scope, approval, affected systems, or rollback is unclear. Refer to Governance Security and the applicable incident process.

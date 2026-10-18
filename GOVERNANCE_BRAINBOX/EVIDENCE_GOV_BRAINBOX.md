# EVIDENCE_GOV_BRAINBOX

**STATUS:** [ACTIVE — CANONICAL]
**CANONICAL SOURCE:** Frozen V003 Specification §§25.5–25.6, 25.11–25.12.
**APPLIES TO:** Verification claims, historical records, reusable methods, and migration evidence.

## Preserve what happened

- Record actual outcomes, including failures, limits, and unresolved uncertainty.
- Do not retroactively rewrite a failure as a success or infer an event from an artifact that does not prove it.
- Preserve source authorship, timestamps, attribution, and relevant context. Corrections to history use dated addenda where appropriate.
- Keep Operator-performed evidence distinct from agent-performed checks and independent verification.
- For copied or moved historical records, compare source and destination integrity (for example SHA-256, byte size, and line count) before source retirement.

## Tested claims

“Proven means tested”: do not describe a method, skill, or workflow as proven until it has been exercised in practice and its result is evidenced. A plan, successful write, or unexecuted test is not proof. Record the test context, outcome, verifier, and limitations.

## Engagement and provenance truth

When documenting projects or portfolio material, identify the engagement accurately (for example unpaid spec/trial versus paid client work) and preserve the actual people/agents and workflow involved. Do not invent client approval, production use, or success evidence.

## Tool-output provenance and claim validation

Before information derived from tool output is incorporated into canonical documentation, record the source identity and context where available: tool or service, interface/version, operator or agent, retrieval date/time, exact command or query, repository path/ref or URL, and the relevant source/evidence identifier. If an element is unavailable, state that it is unknown rather than infer it.

Classify the material as a direct observation, a tool-reported result, an attributed quotation or external passage, or historical evidence. State the specific claim it supports and its limits. Distinguish a reported outcome from an independently reproduced result. A log, transcript marker, attachment, or execution-style sentence is not conclusive proof that an action, approval, capability, or event occurred.

Validate consequential claims against suitable independent evidence where available. Preserve known authorship, agent attribution, timestamps, source paths, contextual boundaries, and uncertainty. Preserve integrity identifiers for historical source material when it is retained or copied. Do not copy secret values into documentation; follow [Security Governance](SECURITY_GOV_BRAINBOX.md). When validation is insufficient, label the claim as reported, historical, unknown, or otherwise limited and do not present it as established current fact.

## Bounded documentation-integrity review

Before adopting externally sourced or tool-generated material into a canonical document, and when reviewing a suspected documentation-integrity issue:

1. define the files, records, and date/ref range being checked;
2. search for transcript-style artifacts, embedded instructions, unattributed claims presented as accepted authority, contradictions with active Governance, unverified capability or execution claims, and unexplained changes to historical evidence;
3. inspect each hit in context and classify it as an attributed quotation, tool/output metadata, an instruction in source content, a factual claim, or a possible integrity defect;
4. validate factual, approval, capability, and execution claims against suitable evidence;
5. compare protected historical content with its source or recorded integrity baseline; and
6. record the search scope, pattern/command, hits, review classification, disposition, limitations, verifier, and date before making any separately authorized correction.

A pattern match is a review candidate, not proof of contamination and not permission to delete or rewrite. Retain legitimate quotations and forensic examples when attribution, context, and evidence status are clear. Correct only a confirmed issue within explicit authorization, preserving historical evidence through a dated addendum where appropriate. This procedure complements [Documentation Governance](DOCUMENTATION_GOV_BRAINBOX.md) and [Ticketing Governance](TICKETING_GOV_BRAINBOX.md).
## Sources

- [Frozen V003 Specification](../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md), §§25.5–25.6, 25.11–25.12, 27.
- [Archived root evidence principles — historical](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/DOB_MUST_README.md), “Nothing is discarded” and “Proven means tested.”
- [Archived function workflow and verification loop — historical](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_WORKFLOW_BRAINBOX.md), §§2.2, 9.
- [Archived project workflow evidence source — historical](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/PROJ_MUST_README.md).
- [Archived AI portfolio disclosure source — historical](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/AI_MUST_README.md), “Milestones and Career Objective.”

**Prepared by:** Codex under the Operator-authorized V003-M03 ticket.
**Last verified:** 2026-10-08

# README_GOV_BRAINBOX

**STATUS:** [ACTIVE — M03 IMPLEMENTED; INDEPENDENT VERIFICATION PASS]
**PARENT:** `DEODINI_BRAINBOX/`
**CURRENT DOMAIN:** System-wide Brainbox governance
**PURPOSE:** Own current cross-domain rules for naming, documentation, references, versioning, evidence, security, ticketing, and promotion.
**MENTAL MODEL:** Root README answers where domains live; Governance answers which system-wide rules govern them; each local README explains its domain and navigation.
**GOVERNED BY:** De O'Dini — Operator; frozen V003 Specification for approved architecture; later explicit Operator declarations for scoped execution updates.
**AUTHORITATIVE TREE:** Root `README_BRAINBOX.md` is the complete-tree authority; the local tree below is this domain's approved structure.
**LOCAL TREE:** The nine files listed below are present.
**RELATED DOMAINS:** Root README, AI, Skills, DevOps Sandbox/Production, Portfolio, Version History, and Phase 02 migration support.
**CANONICAL SOURCES:** Frozen V003 Specification §§5, 25–27; V003 Origin Conversation; listed legacy sources as provenance only.
**REFERENCES:** See the source and navigation index below.
**POPULATION STATE:** All approved Governance files are present. M19 reconciled active README references. M20 retired only seven verified empty placeholders; substantive original legacy sources remain under source-specific retirement safeguards.
**VERIFIER:** Codex — M03 implementation; ChatGPT — independent verification PASS, recorded in the Phase 02 report.
**LAST VERIFIED:** 2026-10-10 ? Codex M19 README tree/reference reconciliation; substantive source evidence and execution claims were not re-run.
**ENTRY NAVIGATION:** Start here for system-wide policy, then open the relevant governance domain.
**EXIT NAVIGATION:** Return to `README_BRAINBOX.md` for the complete root tree.
**APPLIES TO:** Operators and AI agents working in DEODINI_BRAINBOX.

## Canonical local tree — two descendant levels

Current navigation snapshot; physical/population tags follow [Tree and status governance](TREE_AND_STATUS_GOV_BRAINBOX.md). This local view shows every direct child and each directory child’s direct children. For a deeper path, open the corresponding child README; consult the root README for the complete tree.

```text
GOVERNANCE_BRAINBOX/ [PRESENT · POPULATED]
├── DOCUMENTATION_GOV_BRAINBOX.md [PRESENT]
├── EVIDENCE_GOV_BRAINBOX.md [PRESENT]
├── NAMING_GOV_BRAINBOX.md [PRESENT]
├── PROMOTION_GOV_BRAINBOX.md [PRESENT]
├── README_GOV_BRAINBOX.md [PRESENT]
├── REFERENCE_GOV_BRAINBOX.md [PRESENT]
├── SECURITY_GOV_BRAINBOX.md [PRESENT]
├── TICKETING_GOV_BRAINBOX.md [PRESENT]
├── test_validate_tree_status.py [PRESENT]
├── TREE_AND_STATUS_GOV_BRAINBOX.md [PRESENT]
├── validate_tree_status.py [PRESENT]
└── VERSIONING_GOV_BRAINBOX.md [PRESENT]
```

## Authority boundary

Governance is the canonical home for current system-wide rules. The frozen V003 Specification remains the approved architecture and migration-target authority; the Origin Conversation remains historical decision evidence. This folder operationalizes the approved governance rules without replacing either V003 authority.

The prior root and subsystem documents listed below remain unmodified source records during migration. Their rules are mapped here only where they are system-wide and still current. Local or workflow-specific material remains with its domain until its own ticket classifies it. M19 completed active README reference reconciliation; M20 is the later source-retirement gate. No source is removed by M03.

The Phase 02 ticket set and Operator declaration supply the current Phase 02 execution cadence and flag classification. That scoped update does not rewrite the frozen Specification or create a general exception for unrelated work.

## Current-tree reference

The current physical tree is documented in the canonical two-descendant-level local tree above. The complete project tree is maintained only in the root README.

## Domain navigation

| File | Canonical responsibility |
|---|---|
| `NAMING_GOV_BRAINBOX.md` | Namespaces, suffixes, approved concise infixes, and rename discipline |
| `DOCUMENTATION_GOV_BRAINBOX.md` | Authority boundaries, README roles, status language, authorship, and provenance |
| `REFERENCE_GOV_BRAINBOX.md` | Canonical ownership, links, citations, and duplicate-content prevention |
| `VERSIONING_GOV_BRAINBOX.md` | Brainbox generations, Git lifecycle distinctions, and history preservation |
| `EVIDENCE_GOV_BRAINBOX.md` | Truthful records, verification, tested claims, and evidence integrity |
| `SECURITY_GOV_BRAINBOX.md` | Secret handling and safe disclosure |
| `TICKETING_GOV_BRAINBOX.md` | Scope, authorization, flags, dependencies, verification, and ticket closure |
| `PROMOTION_GOV_BRAINBOX.md` | Evidence-based Sandbox-to-Production and portfolio promotion |

For verified cross-domain read sources and ticket-scoped update destinations, see the [Reference Governance ownership matrix](REFERENCE_GOV_BRAINBOX.md). This pointer grants no permission to write; applicable ticket authorization remains mandatory.

## Sources and provenance

- [Frozen V003 Specification](../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md) — approved architecture and governance rules.
- [V003 Origin Conversation](../V003_VERSION_UPGRADE_BRAINBOX/V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md) — decision history and naming normalization provenance.
- [Root README](../README_BRAINBOX.md) — complete target tree and root navigation.
- [Phase 02 ticket set](../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/V003_PHASE02_MIGRATION_TICKETS_BRAINBOX.md) and [Phase 02 README](../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/README_PHASE02_MIGRATION_BRAINBOX.md) — active migration execution rules.
- [Migration map](../VERSION_HISTORY_BRAINBOX/V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md) — source profiles, integrity baselines, and M03 dispositions.
- M03-era source inventory (historical paths; retired records are not current authority): [DOB_MUST_README](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/DOB_MUST_README.md), [AI_MUST_README](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/AI_MUST_README.md), [FQ_MUST_README](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/FUNC_AI_BRAINBOX/FQ_MUST_README.md), [FUNC_REQ](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_REQ_BRAINBOX.md), [FUNC_WORKFLOW](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/FUNC_AI_BRAINBOX/FUNC_WORKFLOW_BRAINBOX.md), the [archived PROJ_MUST_README](../RECYCLE_BIN_BRAINBOX/RETIRED_ITEMS_BRAINBOX/PROJ_WORKFLOW_AI_BRAINBOX/PROJ_MUST_README.md), and the retained reference-only SKILLS_MUST_README. Ticket 02 archived sources are RETIRED / HISTORICAL / NOT CURRENT OPERATING AUTHORITY.
- **Ticket 02 current legacy-source disposition (2026-10-16):** DOB, AI_MUST, eight agent FUNC reports, FQ, FUNC_REQ, and FUNC_WORKFLOW are archived in the [Ticket 02 Recycle Bin manifest](../RECYCLE_BIN_BRAINBOX/LEGACY_AUTHORITY_RETIREMENT_MANIFEST_BRAINBOX.json). These records are historical sources, not current operating instructions. The M03 inventory above remains historical.
- **Current PROJ_WORKFLOW disposition (2026-10-16):** The former source tree has been physically removed after its 88 files were archived and the approved migration/integrity checks passed. The M03-era list above is historical provenance; it does not indicate a current source path. See the [retirement ledger](../RECYCLE_BIN_BRAINBOX/RETIREMENT_LEDGER_BRAINBOX.md) and [Ticket 01 report](../V003_VERSION_UPGRADE_BRAINBOX/PHASE03_FIXES_BRAINBOX/V003_FIXES_REPORT_BRAINBOX.md).

## M03 revision record

- **Change:** Established the canonical Governance domain and its eight rule records; preserved and mapped legacy sources without retiring them.
- **Prepared by:** Codex, from Operator-authorized V003 authorities and source records.
- **Timestamp:** 2026-10-08
- **Authorization:** Operator-approved V003-M03 under the approved V003-M01–M21 set.
- **Signed & Authorized by:** DE O'DINI (OPERATOR)


## Tree and status classification authority

[Tree and Status Governance](TREE_AND_STATUS_GOV_BRAINBOX.md) defines mandatory two-descendant-level navigation for local READMEs, path validation, and separate structural/lifecycle tags. Root README remains complete-tree authority. This dated Operator-approved policy supplements, but does not rewrite, frozen V003 architecture.

## Local read-only validation

The Governance directory contains two complementary Python utilities:

**`validate_tree_status.py` — Read-only structural validator**

This program inspects active Brainbox README documentation and compares supported local-tree, structural-status, and local Markdown-link claims against the accessible repository filesystem.

Its checks include:

- Presence and completeness of each non-root README's canonical two-descendant-level local tree.
- Listed paths against actual files and directories.
- Missing, unexpected, or duplicate local-tree entries.
- Unsupported structural/status labels.
- Approved absent/planned Sandbox path exceptions.
- Structural checks for `PRESENT`, `POPULATED`, `STUB`, and `EMPTY`, subject to the limitations below.
- Existence of local Markdown link destinations and whether their paths escape the repository root.

The root `README_BRAINBOX.md` receives local-link checking, but its complete full-depth tree is not validated with the non-root two-level tree parser.

**`test_validate_tree_status.py` — Validator behavior tests**

This program uses Python's `unittest` framework and controlled temporary repository fixtures to test the validator's behavior.

Its tests include valid tree acceptance, incorrect status labels, omitted paths, excessive tree depth, unauthorized absent paths, broken links, repository-escaping links, and structural status mismatches. The test suite evaluates the implemented validator behavior; passing tests do not establish that every Governance rule has been implemented as an automated check.

### Execution commands

Run from the repository root:

```powershell
python GOVERNANCE_BRAINBOX/validate_tree_status.py
python -B GOVERNANCE_BRAINBOX/test_validate_tree_status.py
```

These commands perform validation or execute controlled tests. They are not intended to modify canonical repository documentation. The validator reports findings; it does not repair repository files.

### Current validation boundaries

1. **Markdown heading anchors:** The validator checks whether a local Markdown target file exists but does not currently verify that a fragment such as `#specific-heading` resolves to a heading in that file.
2. **Complete root-tree accuracy:** The validator does not currently independently compare every entry in the full-depth root README tree with the physical repository.
3. **Status semantics:** Structural checks are limited: `PRESENT` checks that a path exists; `EMPTY` requires a zero-byte file; `POPULATED` checks for a directory and a non-zero-byte file somewhere below it; and `STUB` checks directory existence only. The validator does not decide whether content is genuinely substantive. Recognizing labels such as `VERIFIED`, `ACTIVE`, or `PLANNED` does not prove their evidence, authorization, or lifecycle meaning is justified or current.
4. **Operational capabilities:** Structural validation does not establish that an AI agent, tool, connector, workflow, or deployment is currently functional.
5. **Git enforcement:** Running either Python file manually does not automatically block staging, commits, pushes, pull requests, or merges. Automatic enforcement would require a separately approved and configured integration such as a Git hook or CI workflow.
6. **Validation scope:** A validator PASS means only that the checks currently implemented by that program passed for the inspected files and environment. It is not a blanket Governance-compliance certification.

### Ownership and change control

The two Python files implement and test specific mechanical checks. They do not create or replace Governance policy. The authoritative rules remain in the applicable Governance documents. Any future expansion of validator functionality, test coverage, or automated Git enforcement requires separately authorized implementation work.

**Source files:**

- [Read-only structural validator](validate_tree_status.py)
- [Validator test suite](test_validate_tree_status.py)

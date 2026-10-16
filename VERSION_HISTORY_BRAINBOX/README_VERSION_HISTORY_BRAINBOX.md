# README_VERSION_HISTORY_BRAINBOX

**Status:** [ACTIVE — M04 independently verified/merged; M21 snapshot present; V003 project closure is Operator-qualified; 20 Cline commit objects remain unrecovered]
**PARENT:** `DEODINI_BRAINBOX/`
**CURRENT DOMAIN:** Evidence-backed architectural generation history
**PURPOSE:** Preserve verified historical repository snapshots and explain conceptual evolution only where dated source evidence supports it.
**MENTAL MODEL:** Git history records what changed technically; Brainbox Version History records why the system evolved conceptually. A Git snapshot is evidence, not a competing live architecture.
**GOVERNED BY:** Governance naming, documentation, evidence, and versioning rules; frozen V003 Specification §24; the Origin Conversation; authorized V003-M04.
**LAST VERIFIED:** 2026-10-15 — Codex pre-publication tree/status reconciliation; M21/F02 closure status cross-checked against the Phase 03 report and active Unresolved Register

## Canonical local tree — two descendant levels

Current navigation snapshot; physical/population tags follow [Tree and status governance](../GOVERNANCE_BRAINBOX/TREE_AND_STATUS_GOV_BRAINBOX.md). This local view shows every direct child and each directory child’s direct children. For a deeper path, open the corresponding child README; consult the root README for the complete tree.

```text
VERSION_HISTORY_BRAINBOX/ [PRESENT · POPULATED]
├── V001_BRAINBOX/ [PRESENT · POPULATED]
│   ├── RETROSPECTIVE_V001_BRAINBOX.md [PRESENT]
│   └── TREE_SNAPSHOT_V001_BRAINBOX.md [PRESENT]
├── V002_DEODINI_BRAINBOX/ [PRESENT · POPULATED]
│   ├── RETROSPECTIVE_V002_BRAINBOX.md [PRESENT]
│   └── TREE_SNAPSHOT_V002_BRAINBOX.md [PRESENT]
├── V003_EXTENDED_DEODINI_BRAINBOX/ [PRESENT · POPULATED]
│   ├── ARCHITECTURE_DECISIONS_V003_BRAINBOX.md [PRESENT]
│   ├── MIGRATION_MAP_V003_BRAINBOX.md [PRESENT]
│   └── TREE_SNAPSHOT_V003_BRAINBOX.md [PRESENT]
└── README_VERSION_HISTORY_BRAINBOX.md [PRESENT]
```

## Authority boundary

- The [frozen V003 Specification](../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md) defines **what V003 is**.
- The [Origin Conversation](../V003_VERSION_UPGRADE_BRAINBOX/V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md) preserves chronological historical discussion and ambiguity evidence.
- [V003 Architecture Decisions](V003_EXTENDED_DEODINI_BRAINBOX/ARCHITECTURE_DECISIONS_V003_BRAINBOX.md) records **why selected V003 decisions were made**, concisely.
- The [V003 Migration Map](V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md) is the living Phase 02 source-to-target ledger.
- V001/V002 snapshots are immutable evidence records. They are not active architecture authorities.

## Authoritative target tree

```text
VERSION_HISTORY_BRAINBOX/
├── README_VERSION_HISTORY_BRAINBOX.md
├── V001_BRAINBOX/
│   ├── TREE_SNAPSHOT_V001_BRAINBOX.md
│   └── RETROSPECTIVE_V001_BRAINBOX.md
├── V002_DEODINI_BRAINBOX/
│   ├── TREE_SNAPSHOT_V002_BRAINBOX.md
│   └── RETROSPECTIVE_V002_BRAINBOX.md
└── V003_EXTENDED_DEODINI_BRAINBOX/
    ├── TREE_SNAPSHOT_V003_BRAINBOX.md [PRESENT — M21; Operator-qualified project closure; 20 historical commit objects unrecovered]
    ├── MIGRATION_MAP_V003_BRAINBOX.md [LIVING LEDGER]
    └── ARCHITECTURE_DECISIONS_V003_BRAINBOX.md
```

## Current-tree reference

The current physical tree is documented in the canonical two-descendant-level local tree above. The complete project tree is maintained only in the root README.

## Population state

- `README_VERSION_HISTORY_BRAINBOX.md` — present; M04 navigation/authority boundary.
- `V001_BRAINBOX/TREE_SNAPSHOT_V001_BRAINBOX.md` — present; Git-backed snapshot at `e726bfe11ba484d077278eaca4efd241098caad3`.
- `V001_BRAINBOX/RETROSPECTIVE_V001_BRAINBOX.md` — present; verified Git chronology recorded; conceptual rationale explicitly **BLOCKED** because the available source does not establish it.
- `V002_DEODINI_BRAINBOX/TREE_SNAPSHOT_V002_BRAINBOX.md` — present; Git-backed snapshot at `f03b74b6b569ff7292ecc42967c20a64e556c6db`.
- `V002_DEODINI_BRAINBOX/RETROSPECTIVE_V002_BRAINBOX.md` — present; verified Git chronology recorded; conceptual rationale explicitly **BLOCKED** for the same evidence limitation.
- `V003_EXTENDED_DEODINI_BRAINBOX/ARCHITECTURE_DECISIONS_V003_BRAINBOX.md` — retained and verified; 2,887 bytes, 36 lines, SHA-256 `716b9a4eb660d7b692d4490613ca371030ef45d0e942812c55f96dcdd7bffe38`; not rewritten.
- `V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md` — retained as the living migration ledger and updated for M04.
- `V003_EXTENDED_DEODINI_BRAINBOX/TREE_SNAPSHOT_V003_BRAINBOX.md` — created by M21 from the actual physical worktree. V003/M21 has an Operator-qualified project closure; the 20 historical Cline commit objects were not recovered, and closure does not claim their recovery or an unqualified technical PASS.

## Snapshot boundary note

The V001 and V002 commits are evidence-selected repository cut points for these snapshots, not formal releases or Operator-declared version tags. The repository has no Git tags. V001 uses the last commit before the first observed top-level structural expansion; V002 uses the exact parent of the first V003-P01 commit. The snapshot files identify the commit, tree object, date, selection basis, and every tracked file path. Git does not preserve empty directories.

## References

- [Root complete-tree authority](../README_BRAINBOX.md)
- [V003 Specification §24](../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md)
- [Origin Conversation](../V003_VERSION_UPGRADE_BRAINBOX/V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md)
- [Phase 02 migration records](../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/README_PHASE02_MIGRATION_BRAINBOX.md)
- [Living migration map](V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md)

**POPULATION STATE:** V001/V002 snapshots are source-backed; conceptual retrospectives remain explicitly blocked pending suitable source evidence. The V003 physical-tree snapshot is present. M21/F02 project closure is Operator-qualified; the 20 Cline commit objects remain unrecovered under the accepted bounded historical disposition.
**VERIFIER:** Codex — M04/M21 implementation and 2026-10-15 status reconciliation; ChatGPT — M04 independent PASS. M21/F02 closure qualification is recorded in the Phase 03 report and remains distinct from recovery of the 20 commit objects.
**APPLIES TO:** Version-history navigation and historical-source interpretation in DEODINI_BRAINBOX.

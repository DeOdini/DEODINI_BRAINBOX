# README_VERSION_HISTORY_BRAINBOX

**Status:** [ACTIVE — M04 IMPLEMENTED; INDEPENDENT VERIFICATION PASS; PR #19 MERGED TO MAIN]
**PARENT:** `DEODINI_BRAINBOX/`
**CURRENT DOMAIN:** Evidence-backed architectural generation history
**PURPOSE:** Preserve verified historical repository snapshots and explain conceptual evolution only where dated source evidence supports it.
**MENTAL MODEL:** Git history records what changed technically; Brainbox Version History records why the system evolved conceptually. A Git snapshot is evidence, not a competing live architecture.
**GOVERNED BY:** Governance naming, documentation, evidence, and versioning rules; frozen V003 Specification §24; the Origin Conversation; authorized V003-M04.
**LAST VERIFIED:** 2026-10-08

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
    ├── TREE_SNAPSHOT_V003_BRAINBOX.md [DEFERRED — M21]
    ├── MIGRATION_MAP_V003_BRAINBOX.md [LIVING LEDGER]
    └── ARCHITECTURE_DECISIONS_V003_BRAINBOX.md
```

## Current local tree

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
    ├── ARCHITECTURE_DECISIONS_V003_BRAINBOX.md
    └── MIGRATION_MAP_V003_BRAINBOX.md
```

## Population state

- `README_VERSION_HISTORY_BRAINBOX.md` — present; M04 navigation/authority boundary.
- `V001_BRAINBOX/TREE_SNAPSHOT_V001_BRAINBOX.md` — present; Git-backed snapshot at `e726bfe11ba484d077278eaca4efd241098caad3`.
- `V001_BRAINBOX/RETROSPECTIVE_V001_BRAINBOX.md` — present; verified Git chronology recorded; conceptual rationale explicitly **BLOCKED** because the available source does not establish it.
- `V002_DEODINI_BRAINBOX/TREE_SNAPSHOT_V002_BRAINBOX.md` — present; Git-backed snapshot at `f03b74b6b569ff7292ecc42967c20a64e556c6db`.
- `V002_DEODINI_BRAINBOX/RETROSPECTIVE_V002_BRAINBOX.md` — present; verified Git chronology recorded; conceptual rationale explicitly **BLOCKED** for the same evidence limitation.
- `V003_EXTENDED_DEODINI_BRAINBOX/ARCHITECTURE_DECISIONS_V003_BRAINBOX.md` — retained and verified; 2,887 bytes, 36 lines, SHA-256 `716b9a4eb660d7b692d4490613ca371030ef45d0e942812c55f96dcdd7bffe38`; not rewritten.
- `V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md` — retained as the living migration ledger and updated for M04.
- `V003_EXTENDED_DEODINI_BRAINBOX/TREE_SNAPSHOT_V003_BRAINBOX.md` — not created by M04; final snapshot remains assigned to M21.

## Snapshot boundary note

The V001 and V002 commits are evidence-selected repository cut points for these snapshots, not formal releases or Operator-declared version tags. The repository has no Git tags. V001 uses the last commit before the first observed top-level structural expansion; V002 uses the exact parent of the first V003-P01 commit. The snapshot files identify the commit, tree object, date, selection basis, and every tracked file path. Git does not preserve empty directories.

## References

- [Root complete-tree authority](../README_BRAINBOX.md)
- [V003 Specification §24](../V003_VERSION_UPGRADE_BRAINBOX/V003_SPECIFICATION_VERSION_UPGRADE_BRAINBOX.md)
- [Origin Conversation](../V003_VERSION_UPGRADE_BRAINBOX/V003_CONVO_ORIGIN_VERSION_UPGRADE_BRAINBOX.md)
- [Phase 02 migration records](../V003_VERSION_UPGRADE_BRAINBOX/PHASE02_MIGRATION_BRAINBOX/README_PHASE02_MIGRATION_BRAINBOX.md)
- [Living migration map](V003_EXTENDED_DEODINI_BRAINBOX/MIGRATION_MAP_V003_BRAINBOX.md)

**POPULATION STATE:** V001/V002 snapshots are source-backed; conceptual retrospectives remain explicitly blocked pending suitable source evidence. V003 snapshot is deferred to M21.
**VERIFIER:** Codex — M04 implementation; ChatGPT — independent verification PASS, recorded in the Phase 02 report.
**APPLIES TO:** Version-history navigation and historical-source interpretation in DEODINI_BRAINBOX.

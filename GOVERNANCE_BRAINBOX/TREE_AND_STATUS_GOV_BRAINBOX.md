# TREE_AND_STATUS_GOV_BRAINBOX

**STATUS:** [ACTIVE] — Operator-approved 2026-10-15
**AUTHORITY:** System-wide tree navigation and status classification, supplemental to the frozen V003 Specification. Applies prospectively to current navigation; does not rewrite historical evidence.

## Mandatory two-level local navigation
1. Repository-root `README_BRAINBOX.md` alone carries the complete detailed project tree.
2. Every other active folder README's canonical *local tree* lists **all immediate children** (files and folders) and **all immediate children of each immediate child folder**, with no third descendant level. Depth is measured from that README's containing folder: child = 1; grandchild = 2. A leaf file is not expanded.
3. Display complete siblings, even if numerous; never truncate a level just to shorten the README. For deeper discovery follow the next child README or inspect the filesystem; never guess a path.
4. The local tree must reflect verified current physical paths plus specifically approved future paths. An approved absent path is explicitly tagged `[ABSENT · PLANNED]`. Never claim a planned path exists.
5. Current trees supersede old tree *presentations*, not historical observations or the frozen approved architecture. Historical source text, evidence and migration manifests remain intact.
6. Local READMEs link to this policy; agents read the relevant parent README and then its child README before navigating deeper or modifying paths.

## Structural classification (physical state versus content)
- `[PRESENT]`: file or directory exists; existence only. In a directory label, combine with a more precise content tag where applicable.
- `[POPULATED]`: directory exists and at least one file in its recursive subtree has substantive non-placeholder content, including an actual navigational README. No evidence of operational success implied.
- `[STUB]`: directory exists but has only structural placeholders, zero-byte files or expressly non-substantive scaffold documentation, recursively. It is *not* `[EMPTY]`.
- `[EMPTY]`: file exists with zero bytes (or explicitly no substantive content where classified by evidence); use only for **files**, never directories.
- `[ABSENT]`: path not physically present. For a future approved path pair it with `[PLANNED]`; do not invent missing paths.

A substantive README makes its folder `[POPULATED]`, even if the capability described remains planned. The root of a populated branch does not certify that all descendants are populated.

## Lifecycle and proof classification (separate dimension)
- `[ACTIVE]`: currently authorized domain or record, not necessarily tested.
- `[PLANNED]`: approved intended future structure/capability, not a claim of present implementation.
- `[UNVERIFIED]`: content/procedure exists but the asserted outcome or behavior has no adequate proof.
- `[VERIFIED]`: *bounded* named assertion supported by dated, reproducible evidence; never automatically inherit to parent or siblings.
- `[RETIRED]`: archived under an approved disposition; may still be structurally `[PRESENT · POPULATED]`.

Never use `[VERIFIED]` as a substitute for `[PRESENT]` or `[POPULATED]`. Describe unknown states explicitly rather than guessing. For scanned folders, labels are snapshots, not permanently asserted freshness.

## Execution and verification
- Before changes: inventory actual children, detect placeholder-only paths and enumerate approved absent/planned branches.
- After changes: validate all shown physical paths, local-tree depth, completeness of both descendant levels, relative policy links, and Git diff integrity.
- Do not alter source evidence, invent content, promote RAW to PROVEN, or rewrite the frozen V003 specification. Historical references are not automatically live navigation.
- Scope changes require Operator approval and ticket/report provenance. Root tree remains the whole-project navigation authority.

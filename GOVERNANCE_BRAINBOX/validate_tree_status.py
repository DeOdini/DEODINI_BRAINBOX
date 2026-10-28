"""Read-only, deterministic checks for Brainbox README trees and local links.

Run from the repository root with:
    python GOVERNANCE_BRAINBOX/validate_tree_status.py

The validator checks repository structure and filesystem facts. It cannot prove
that a status label such as ACTIVE, RETIRED, PLANNED, VERIFIED, or POPULATED is
semantically justified; those claims remain qualified for human review.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote, urlsplit


STATUS_TOKENS = {
    "PRESENT",
    "POPULATED",
    "STUB",
    "EMPTY",
    "ABSENT",
    "PLANNED",
    "ACTIVE",
    "RETIRED",
    "VERIFIED",
    "UNVERIFIED",
}

# These are the two Operator-approved absent Sandbox evidence folders in the
# current frozen tree. Additions require an approved architecture change.
APPROVED_ABSENT = {
    "AI_BRAINBOX/DEVOPS_AI_BRAINBOX/SANDBOX_DEVOPS_BRAINBOX/FAILED_SANDBOX_BRAINBOX",
    "AI_BRAINBOX/DEVOPS_AI_BRAINBOX/SANDBOX_DEVOPS_BRAINBOX/PASSED_SANDBOX_BRAINBOX",
}

# One narrowly approved local-only supplementary inventory. Its files are
# documented outside canonical trees, are optional in clean checkouts, and are
# validated by exact name, byte size, and SHA-256 when present. Adding entries
# requires an approved Governance change; this is not an extension-wide ignore.
LOCAL_ONLY_ASSET_README = Path(
    "AI_BRAINBOX/DEVOPS_AI_BRAINBOX/SANDBOX_DEVOPS_BRAINBOX/POC_SANDBOX_BRAINBOX/"
    "FOOTHIVE_V02_POC_BRAINBOX/ASSETS_FH_V02_BRAINBOX/README_ASSETS_FH_V02_BRAINBOX.md"
)
LOCAL_ONLY_ASSET_PROJECT_README = Path(
    "AI_BRAINBOX/DEVOPS_AI_BRAINBOX/SANDBOX_DEVOPS_BRAINBOX/POC_SANDBOX_BRAINBOX/"
    "FOOTHIVE_V02_POC_BRAINBOX/README_FH_V02_POC_BRAINBOX.md"
)
LOCAL_ONLY_ASSET_DIRECTORY = LOCAL_ONLY_ASSET_README.parent
LOCAL_ONLY_ASSET_DECLARATIONS = {
    "DR-01": {
        "file": "CREATIX FOOTHIVE PROPOSED DESIGN.png",
        "bytes": 1082316,
        "sha256": "5f668180a36eecfe38cd05dd9de8be567f632dbb6d51af24e2ddf19988a31dd0",
    },
    "DR-02": {
        "file": "FootHive Dark Neon Footwear Showcase.png",
        "bytes": 2004170,
        "sha256": "0e2c0cf1a2f0b39269b2afa0fa728c5491ccabb3e33e04e03358db1dc5224d83",
    },
    "DR-03": {
        "file": "FootHive Everyday Footwear Showcase.png",
        "bytes": 1987304,
        "sha256": "0fae876983e0581bb66bf92793fbee4efb6d991402b660ff23e9a9ca50b6bb89",
    },
}
LOCAL_ONLY_ASSET_STATE = "LOCAL_ONLY; EXCLUDED_FROM_GIT; PRODUCTION_UNAPPROVED"
LOCAL_ONLY_ASSET_TABLE_HEADER = [
    "ID",
    "Operator label",
    "Intended reference role",
    "Source provenance and local filename",
    "Format / size / SHA-256",
    "Local / publication / production state",
    "Rights / use qualification",
]

FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
TREE_ENTRY_RE = re.compile(
    r"^(?P<prefix>(?:(?:│   )|(?:\|   )|(?:    ))*)"
    r"(?P<edge>├──|└──|\+--|\|--|\\--)\s*(?P<label>.*?)\s*$"
)
STATUS_RE = re.compile(r"\[([^\]]*)\]")
INLINE_LINK_RE = re.compile(
    r"!?\[[^\]\n]*\]\((?:<([^>\n]+)>|([^\s)]+))(?:\s+[^)]*)?\)"
)
REFERENCE_LINK_RE = re.compile(
    r"(?m)^\s{0,3}\[[^\]\n]+\]:\s*(?:<([^>\n]+)>|(\S+))"
)


@dataclass(frozen=True)
class TreeEntry:
    path: Path
    depth: int
    line: int
    statuses: frozenset[str]


@dataclass
class ValidationResult:
    errors: list[str] = field(default_factory=list)
    qualifications: list[str] = field(default_factory=list)
    inventory: list[str] = field(default_factory=list)
    tree_blocks: int = 0
    tree_entries: int = 0
    links_checked: int = 0
    local_only_assets_declared: int = 0
    local_only_assets_present: int = 0
    status_counts: Counter[str] = field(default_factory=Counter)


def _repo_path(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def _is_retired_archive(path: Path) -> bool:
    parts = set(path.parts)
    return "RECYCLE_BIN_BRAINBOX" in parts and "RETIRED_ITEMS_BRAINBOX" in parts


def discover_readmes(root: Path) -> list[Path]:
    ignored = {".git", ".codex", ".agents", "node_modules", "__pycache__"}
    found = []
    for path in root.rglob("README*.md"):
        if any(part in ignored for part in path.parts) or _is_retired_archive(path):
            continue
        found.append(path)
    return sorted(found, key=lambda p: p.relative_to(root).as_posix().casefold())


def _status_tokens(label: str) -> frozenset[str]:
    found: set[str] = set()
    for group in STATUS_RE.findall(label):
        for token in re.findall(r"[A-Z]+", group.upper()):
            if token in STATUS_TOKENS:
                found.add(token)
    return frozenset(found)


def _unknown_status_tokens(label: str) -> frozenset[str]:
    """Return unrecognized tokens in status-shaped bracket groups.

    Tree annotations that are ordinary prose or ticket metadata are ignored.
    A bracket group composed of uppercase words/underscores and separators is
    treated as a status label, so misspellings cannot silently disappear from
    the status inventory. Numeric ticket/version identifiers remain metadata.
    """
    unknown: set[str] = set()
    for group in STATUS_RE.findall(label):
        candidate = group.strip()
        if not candidate or any(char.isdigit() for char in candidate):
            continue
        if not all(char.isupper() or char in " _·Â;|,&/-" for char in candidate):
            continue
        tokens = re.findall(r"[A-Z][A-Z_]*", candidate)
        unknown.update(token for token in tokens if token not in STATUS_TOKENS)
    return frozenset(unknown)


def _validate_status_labels(
    label: str,
    readme: Path,
    line: int,
    result: ValidationResult,
) -> None:
    for token in sorted(_unknown_status_tokens(label)):
        result.errors.append(
            f"{readme}:{line}: unrecognized structural/status tag {token!r}; "
            f"supported vocabulary: {', '.join(sorted(STATUS_TOKENS))}"
        )


def _strip_status(label: str) -> str:
    return STATUS_RE.split(label, maxsplit=1)[0].strip().strip("`").strip()


def _find_tree_block(readme: Path, text: str) -> tuple[list[tuple[int, str]], str | None]:
    lines = text.splitlines()
    heading = next(
        (index for index, line in enumerate(lines) if re.match(r"^\s*#{1,6}\s+Canonical local tree\b", line, re.I)),
        None,
    )
    if heading is None:
        return [], f"{readme}: missing 'Canonical local tree' heading"

    opening = None
    fence_char = ""
    fence_size = 0
    for index in range(heading + 1, len(lines)):
        match = FENCE_RE.match(lines[index])
        if match:
            opening = index
            fence_char = match.group(1)[0]
            fence_size = len(match.group(1))
            break
    if opening is None:
        return [], f"{readme}:{heading + 1}: no fenced local-tree block follows the heading"

    closing = None
    for index in range(opening + 1, len(lines)):
        match = FENCE_RE.match(lines[index])
        if match and match.group(1)[0] == fence_char and len(match.group(1)) >= fence_size:
            closing = index
            break
    if closing is None:
        return [], f"{readme}:{opening + 1}: local-tree code fence is not closed"

    return [(index + 1, lines[index]) for index in range(opening + 1, closing)], None


def _parse_local_tree(
    root: Path,
    readme: Path,
    text: str,
    approved_absent: set[str],
    result: ValidationResult,
) -> tuple[str | None, list[TreeEntry], int | None]:
    block, error = _find_tree_block(readme, text)
    if error:
        result.errors.append(error)
        return None, [], None

    root_label: str | None = None
    root_line: int | None = None
    entries: list[TreeEntry] = []
    for line_no, line in block:
        if not line.strip() or line.strip() in {"│", "|"}:
            continue
        match = TREE_ENTRY_RE.match(line)
        if not match:
            if root_label is None and not entries:
                root_label = _strip_status(line.strip()).rstrip("/")
                root_line = line_no
                _validate_status_labels(line, readme, line_no, result)
                root_status = _status_tokens(line)
                for status in root_status:
                    result.status_counts[status] += 1
                if root_status:
                    _check_statuses(root, readme, line_no, readme.parent, root_status, approved_absent, result)
                continue
            result.errors.append(
                f"{readme}:{line_no}: unrecognized line inside canonical tree block: {line.strip()}"
            )
            continue

        prefix = match.group("prefix")
        depth = 1 + len(prefix) // 4
        raw_label = match.group("label")
        displayed = _strip_status(raw_label).rstrip("/")
        _validate_status_labels(raw_label, readme, line_no, result)
        statuses = _status_tokens(raw_label)
        for status in statuses:
            result.status_counts[status] += 1
        if depth > 2:
            result.errors.append(
                f"{readme}:{line_no}: tree entry {displayed!r} exceeds two descendant levels (depth {depth})"
            )
        if not displayed:
            result.errors.append(f"{readme}:{line_no}: empty tree path")
            continue
        if depth == 1:
            entry_path = Path(displayed)
        else:
            parent_entry = next((entry for entry in reversed(entries) if entry.depth == 1), None)
            if parent_entry is None:
                result.errors.append(f"{readme}:{line_no}: depth-two item has no depth-one parent")
                continue
            entry_path = parent_entry.path / displayed
        entries.append(TreeEntry(entry_path, depth, line_no, statuses))

    if root_label is None:
        result.errors.append(f"{readme}: canonical tree block has no parent path line")
    result.tree_entries += len(entries)
    return root_label, entries, root_line


def _under_root(root: Path, base: Path, relative: Path) -> Path:
    candidate = (base / relative).resolve(strict=False)
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        raise ValueError("tree path resolves outside the repository")
    return candidate


def _has_nonzero_file(path: Path) -> bool:
    try:
        return any(item.is_file() and item.stat().st_size > 0 for item in path.rglob("*"))
    except OSError:
        return False


def _check_statuses(
    root: Path,
    readme: Path,
    line: int,
    path: Path,
    statuses: frozenset[str],
    approved_absent: set[str],
    result: ValidationResult,
) -> None:
    rel = _repo_path(root, path)
    exists = path.exists()
    if "PRESENT" in statuses and not exists:
        result.errors.append(f"{readme}:{line}: PRESENT status points to missing path {path}")
    if "ABSENT" in statuses:
        if "PLANNED" not in statuses:
            result.errors.append(f"{readme}:{line}: ABSENT path must also be tagged PLANNED")
        if exists:
            result.errors.append(f"{readme}:{line}: ABSENT status points to existing path {path}")
        if rel not in approved_absent:
            result.errors.append(f"{readme}:{line}: absent path {rel} is not in the approved absent-path list")
    elif not exists:
        result.errors.append(f"{readme}:{line}: listed path does not exist: {path}")

    structural = statuses.intersection({"POPULATED", "STUB", "EMPTY"})
    if len(structural) > 1:
        result.errors.append(f"{readme}:{line}: incompatible structural status combination {sorted(structural)}")
    if "EMPTY" in statuses:
        if path.is_dir() or not path.is_file() or path.stat().st_size != 0:
            result.errors.append(f"{readme}:{line}: EMPTY status requires a zero-byte file: {path}")
    if "POPULATED" in statuses:
        if not path.is_dir():
            result.errors.append(f"{readme}:{line}: POPULATED status is only valid for a directory: {path}")
        elif not _has_nonzero_file(path):
            result.errors.append(f"{readme}:{line}: POPULATED directory has no non-zero-byte file: {path}")
    if "STUB" in statuses and not path.is_dir():
        result.errors.append(f"{readme}:{line}: STUB status is only valid for a directory: {path}")


def _markdown_table_cells(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def _git_tracks_path(root: Path, relative_path: str) -> bool | None:
    """Return Git index membership when Git metadata is available."""
    if not (root / ".git").exists():
        return None
    try:
        completed = subprocess.run(
            ["git", "-C", str(root), "ls-files", "--error-unmatch", "--", relative_path],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return None
    if completed.returncode == 0:
        return True
    if completed.returncode == 1:
        return False
    return None


def _local_only_asset_inventory(
    root: Path,
    result: ValidationResult,
) -> set[str]:
    """Read the one approved V02 inventory; never exempt arbitrary paths."""
    readme = root / LOCAL_ONLY_ASSET_README
    if not readme.is_file():
        result.errors.append(
            f"{LOCAL_ONLY_ASSET_README.as_posix()}: required local-only asset inventory README is missing"
        )
        return set()
    try:
        lines = readme.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        result.errors.append(f"{LOCAL_ONLY_ASSET_README.as_posix()}: cannot read local-only inventory: {exc}")
        return set()

    heading = "## Current reference inventory"
    heading_indexes = [index for index, line in enumerate(lines) if line.strip() == heading]
    if len(heading_indexes) != 1:
        result.errors.append(
            f"{LOCAL_ONLY_ASSET_README.as_posix()}: expected exactly one {heading!r} section"
        )
        return set()
    start = heading_indexes[0] + 1
    while start < len(lines) and not lines[start].strip():
        start += 1
    header = _markdown_table_cells(lines[start]) if start < len(lines) else None
    if header != LOCAL_ONLY_ASSET_TABLE_HEADER:
        result.errors.append(
            f"{LOCAL_ONLY_ASSET_README.as_posix()}:{start + 1}: malformed local-only inventory table header"
        )
        return set()
    separator = _markdown_table_cells(lines[start + 1]) if start + 1 < len(lines) else None
    if separator is None or len(separator) != len(LOCAL_ONLY_ASSET_TABLE_HEADER) or not all(
        re.fullmatch(r":?-{3,}:?", cell) for cell in separator
    ):
        result.errors.append(
            f"{LOCAL_ONLY_ASSET_README.as_posix()}:{start + 2}: malformed local-only inventory table separator"
        )
        return set()

    rows: list[tuple[int, list[str]]] = []
    for index in range(start + 2, len(lines)):
        cells = _markdown_table_cells(lines[index])
        if cells is None:
            break
        rows.append((index + 1, cells))

    valid_names: set[str] = set()
    seen_ids: set[str] = set()
    for line, cells in rows:
        if len(cells) != len(LOCAL_ONLY_ASSET_TABLE_HEADER):
            result.errors.append(
                f"{LOCAL_ONLY_ASSET_README.as_posix()}:{line}: local-only inventory row has {len(cells)} columns; "
                f"expected {len(LOCAL_ONLY_ASSET_TABLE_HEADER)}"
            )
            continue
        record_id = cells[0].strip("`")
        if record_id not in LOCAL_ONLY_ASSET_DECLARATIONS:
            result.errors.append(
                f"{LOCAL_ONLY_ASSET_README.as_posix()}:{line}: unapproved local-only asset ID {record_id!r}"
            )
            continue
        if record_id in seen_ids:
            result.errors.append(f"{LOCAL_ONLY_ASSET_README.as_posix()}:{line}: duplicate local-only asset ID {record_id}")
            continue
        seen_ids.add(record_id)
        expected = LOCAL_ONLY_ASSET_DECLARATIONS[record_id]
        filename = expected["file"]
        if f"local filename {filename}" not in cells[3]:
            result.errors.append(
                f"{LOCAL_ONLY_ASSET_README.as_posix()}:{line}: {record_id} does not name its approved exact file {filename!r}"
            )
            continue
        size_hash = re.fullmatch(r"PNG\s*/\s*([0-9,]+) bytes\s*/\s*`([0-9a-fA-F]{64})`", cells[4])
        if not size_hash:
            result.errors.append(
                f"{LOCAL_ONLY_ASSET_README.as_posix()}:{line}: malformed format/size/SHA-256 declaration for {filename!r}"
            )
            continue
        declared_bytes = int(size_hash.group(1).replace(",", ""))
        declared_sha256 = size_hash.group(2).lower()
        if declared_bytes != expected["bytes"] or declared_sha256 != expected["sha256"]:
            result.errors.append(
                f"{LOCAL_ONLY_ASSET_README.as_posix()}:{line}: size or SHA-256 does not match the approved declaration for {filename!r}"
            )
            continue
        if cells[5] != LOCAL_ONLY_ASSET_STATE:
            result.errors.append(
                f"{LOCAL_ONLY_ASSET_README.as_posix()}:{line}: invalid local-only state for {filename!r}; "
                f"expected {LOCAL_ONLY_ASSET_STATE!r}"
            )
            continue
        if not cells[6].strip():
            result.errors.append(
                f"{LOCAL_ONLY_ASSET_README.as_posix()}:{line}: rights/use qualification is required for {filename!r}"
            )
            continue

        asset_path = root / LOCAL_ONLY_ASSET_DIRECTORY / filename
        if asset_path.exists():
            if not asset_path.is_file():
                result.errors.append(
                    f"{LOCAL_ONLY_ASSET_README.as_posix()}:{line}: declared local-only asset is not a regular file: {asset_path}"
                )
                continue
            try:
                data = asset_path.read_bytes()
            except OSError as exc:
                result.errors.append(
                    f"{LOCAL_ONLY_ASSET_README.as_posix()}:{line}: cannot read declared local-only asset {asset_path}: {exc}"
                )
                continue
            actual_sha256 = hashlib.sha256(data).hexdigest()
            if len(data) != expected["bytes"] or actual_sha256 != expected["sha256"]:
                result.errors.append(
                    f"{LOCAL_ONLY_ASSET_README.as_posix()}:{line}: local-only asset integrity mismatch for {filename!r}"
                )
                continue
            result.local_only_assets_present += 1

        git_relative = f"{LOCAL_ONLY_ASSET_DIRECTORY.as_posix()}/{filename}"
        tracked = _git_tracks_path(root, git_relative)
        if tracked is True:
            result.errors.append(
                f"{LOCAL_ONLY_ASSET_README.as_posix()}:{line}: local-only asset is present in the Git index: {git_relative}"
            )
            continue
        if (root / ".git").exists() and tracked is None:
            result.errors.append(
                f"{LOCAL_ONLY_ASSET_README.as_posix()}:{line}: could not verify Git index exclusion for {git_relative}"
            )
            continue
        valid_names.add(filename)

    expected_ids = set(LOCAL_ONLY_ASSET_DECLARATIONS)
    if seen_ids != expected_ids:
        missing = sorted(expected_ids - seen_ids)
        if missing:
            result.errors.append(
                f"{LOCAL_ONLY_ASSET_README.as_posix()}: local-only inventory is missing required IDs: {', '.join(missing)}"
            )
    result.local_only_assets_declared += len(valid_names)
    return valid_names


def _expected_children(
    root: Path,
    parent: Path,
    approved_absent: set[str],
    local_only_asset_names: set[str] | None = None,
) -> set[str]:
    parent_rel = _repo_path(root, parent)
    expected = {child.name for child in parent.iterdir()}
    if parent_rel == LOCAL_ONLY_ASSET_DIRECTORY.as_posix():
        expected.difference_update(local_only_asset_names or set())
    for absent in approved_absent:
        absent_path = Path(absent)
        if absent_path.parent.as_posix() == parent_rel:
            expected.add(absent_path.name)
    return expected


def _validate_tree(
    root: Path,
    readme: Path,
    text: str,
    approved_absent: set[str],
    local_only_asset_names: set[str],
    result: ValidationResult,
) -> None:
    root_label, entries, root_line = _parse_local_tree(root, readme, text, approved_absent, result)
    if root_label is None:
        return
    parent = readme.parent.resolve()
    if root_label.rstrip("/").split("/")[-1] != parent.name:
        result.errors.append(
            f"{readme}: local tree parent {root_label!r} does not match containing folder {parent.name!r}"
        )

    actual_paths: set[str] = set()
    for entry in entries:
        try:
            absolute = _under_root(root, parent, entry.path)
        except ValueError as exc:
            result.errors.append(f"{readme}:{entry.line}: {exc}: {entry.path}")
            continue
        relative = _repo_path(root, absolute)
        if relative in actual_paths:
            result.errors.append(f"{readme}:{entry.line}: duplicate tree path {relative}")
        actual_paths.add(relative)
        _check_statuses(root, readme, entry.line, absolute, entry.statuses, approved_absent, result)

    expected_paths: set[str] = set()
    base_rel = _repo_path(root, parent)
    for child_name in _expected_children(root, parent, approved_absent, local_only_asset_names):
        child_rel = f"{base_rel}/{child_name}"
        expected_paths.add(child_rel)
        child_path = parent / child_name
        if child_path.is_dir():
            for grandchild_name in _expected_children(
                root, child_path, approved_absent, local_only_asset_names
            ):
                expected_paths.add(f"{child_rel}/{grandchild_name}")

    for missing in sorted(expected_paths - actual_paths):
        result.errors.append(
            f"{readme}:{root_line or 1}: expected path missing from local tree: {missing}"
        )
    for unexpected in sorted(actual_paths - expected_paths):
        entry = next((item for item in entries if _repo_path(root, _under_root(root, parent, item.path)) == unexpected), None)
        line = entry.line if entry else 1
        result.errors.append(f"{readme}:{line}: path is not a direct child or grandchild of this README: {unexpected}")


def _unfenced_markdown(text: str) -> str:
    lines = text.splitlines(keepends=True)
    output = []
    fence_char = None
    fence_size = 0
    for line in lines:
        match = FENCE_RE.match(line)
        if fence_char is None and match:
            fence_char = match.group(1)[0]
            fence_size = len(match.group(1))
            output.append("".join("\n" if char == "\n" else "\r" if char == "\r" else " " for char in line))
            continue
        if fence_char is not None:
            output.append("".join("\n" if char == "\n" else "\r" if char == "\r" else " " for char in line))
            if match and match.group(1)[0] == fence_char and len(match.group(1)) >= fence_size:
                fence_char = None
                fence_size = 0
            continue
        output.append(line)
    return "".join(output)


def _markdown_links(text: str):
    masked = _unfenced_markdown(text)
    for pattern in (INLINE_LINK_RE, REFERENCE_LINK_RE):
        for match in pattern.finditer(masked):
            target = match.group(1) or match.group(2)
            if target:
                line = masked.count("\n", 0, match.start()) + 1
                yield line, target.strip()


def _validate_links(root: Path, readme: Path, text: str, result: ValidationResult) -> None:
    for line, target in _markdown_links(text):
        parts = urlsplit(target)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        decoded = unquote(parts.path).replace("\\", "/")
        if decoded.startswith("/"):
            candidate = root / decoded.lstrip("/")
        else:
            candidate = readme.parent / decoded
        result.links_checked += 1
        try:
            candidate.resolve(strict=False).relative_to(root.resolve())
        except ValueError:
            result.errors.append(
                f"{readme}:{line}: local Markdown target escapes repository root: {target!r}"
            )
            continue
        if not candidate.exists():
            result.errors.append(
                f"{readme}:{line}: broken local Markdown target {target!r} (decoded path: {candidate})"
            )


def validate_repository(
    root: Path,
    readmes: list[Path] | None = None,
    approved_absent: set[str] | None = None,
) -> ValidationResult:
    root = root.resolve()
    approved_absent = set(APPROVED_ABSENT if approved_absent is None else approved_absent)
    readmes = discover_readmes(root) if readmes is None else sorted(readmes)
    result = ValidationResult()
    result.inventory = [_repo_path(root, path) for path in readmes]

    local_only_asset_names: set[str] = set()
    local_only_context_exists = (
        (root / LOCAL_ONLY_ASSET_PROJECT_README).exists()
        or (root / LOCAL_ONLY_ASSET_DIRECTORY).exists()
    )
    if local_only_context_exists:
        local_only_asset_names = _local_only_asset_inventory(root, result)

    for absent in sorted(approved_absent):
        if (root / absent).exists():
            result.errors.append(f"approved absent path is now present; review its stale exception: {absent}")

    for readme in readmes:
        try:
            text = readme.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            result.errors.append(f"{_repo_path(root, readme)}: cannot read UTF-8 Markdown: {exc}")
            continue
        _validate_links(root, readme, text, result)
        if readme.resolve() == (root / "README_BRAINBOX.md").resolve():
            continue
        result.tree_blocks += 1
        _validate_tree(root, readme, text, approved_absent, local_only_asset_names, result)

    result.qualifications.extend(
        [
            "POPULATED is mechanically checked only for a directory and a non-zero-byte file somewhere below it; non-placeholder substance remains a human judgment.",
            "STUB is checked for directory existence only; recursively proving that all content is structural is not automated.",
            "ACTIVE, PLANNED, RETIRED, VERIFIED, and UNVERIFIED tokens are recognized and counted where present; current authorization, intent, evidence quality, and freshness remain human-review claims.",
            "The one FootHive V02 local-only inventory is limited to three exact approved PNG records. A clean checkout may omit them; when .git exists the validator checks index exclusion, and when files are present it checks byte size and SHA-256. This exception does not exempt other files or folders.",
            "A tracked-only candidate without .git metadata can validate the exact inventory and clean-checkout behavior, but cannot independently inspect Git index membership; the source checkout check supplies that evidence.",
        ]
    )
    return result


def render_report(root: Path, result: ValidationResult) -> str:
    lines = [
        "Governance tree/status validation",
        f"Repository: {root.resolve()}",
        f"README files inspected: {len(result.inventory)}",
        f"Canonical local tree blocks checked: {result.tree_blocks}",
        f"Displayed tree entries checked: {result.tree_entries}",
        f"Local Markdown targets checked: {result.links_checked}",
        f"Local-only asset records checked: {result.local_only_assets_declared}",
        f"Local-only assets physically present and hash-checked: {result.local_only_assets_present}",
        "Supported status vocabulary: " + ", ".join(sorted(STATUS_TOKENS)),
        "Status labels counted in local trees: "
        + ", ".join(f"{name}={result.status_counts[name]}" for name in sorted(STATUS_TOKENS)),
        "Root README scope: local Markdown targets are checked; the full-depth root tree is not parsed as a two-level local tree.",
        f"Result: {'FAIL' if result.errors else 'PASS (qualified)'}",
    ]
    lines.append("\nInspected README inventory:")
    lines.extend(f"- {path}" for path in result.inventory)
    lines.append("\nSemantic qualifications:")
    lines.extend(f"- {qualification}" for qualification in result.qualifications)
    if result.errors:
        lines.append("\nFindings:")
        lines.extend(f"- {finding}" for finding in sorted(result.errors))
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--readme",
        action="append",
        type=Path,
        help="validate only this README path (repeatable; otherwise discover active README*.md files)",
    )
    args = parser.parse_args(argv)
    selected = None
    if args.readme:
        selected = [path if path.is_absolute() else args.root / path for path in args.readme]
    result = validate_repository(args.root, readmes=selected)
    sys.stdout.write(render_report(args.root, result))
    return 1 if result.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

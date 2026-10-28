"""Controlled fixtures for the read-only Governance tree/status validator."""

from __future__ import annotations

import sys
import hashlib
import json
import subprocess
import shutil
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))

import validate_tree_status as validator  # noqa: E402
from validate_tree_status import APPROVED_ABSENT, STATUS_TOKENS, validate_repository  # noqa: E402


class TreeStatusValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.temp_root = Path(self.temp.name)
        self.root = self.temp_root / "repo"
        self.root.mkdir()
        self.parent = self.root / "GOVERNANCE_BRAINBOX"
        self.parent.mkdir()
        self.readme = self.parent / "README_GOV_BRAINBOX.md"
        self.docs = self.parent / "DOCS_GOV_BRAINBOX"
        self.docs.mkdir()
        (self.parent / "STUB_GOV_BRAINBOX").mkdir()
        (self.docs / "guide file.md").write_text("guide\n", encoding="utf-8")
        (self.parent / "zero.txt").write_bytes(b"")
        (self.parent / "evidence.txt").write_text("dated evidence\n", encoding="utf-8")
        (self.parent / "old.txt").write_text("retired reference\n", encoding="utf-8")
        self.approved_absent = {
            "GOVERNANCE_BRAINBOX/DOCS_GOV_BRAINBOX/FUTURE_GOV_BRAINBOX"
        }

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_readme(
        self,
        *,
        include_future: bool = True,
        link: str = "DOCS_GOV_BRAINBOX/guide%20file.md",
    ) -> None:
        future = (
            "│   └── FUTURE_GOV_BRAINBOX/ [ABSENT · PLANNED]\n"
            if include_future
            else ""
        )
        content = (
            "# Governance fixture\n"
            "## Canonical local tree — two descendant levels\n"
            "```text\n"
            "GOVERNANCE_BRAINBOX/ [PRESENT · POPULATED · ACTIVE]\n"
            "├── DOCS_GOV_BRAINBOX/ [PRESENT · POPULATED]\n"
            "│   ├── guide file.md [PRESENT]\n"
            f"{future}"
            "├── evidence.txt [PRESENT · VERIFIED]\n"
            "├── README_GOV_BRAINBOX.md [PRESENT · UNVERIFIED]\n"
            "├── old.txt [PRESENT · RETIRED]\n"
            "├── STUB_GOV_BRAINBOX/ [PRESENT · STUB]\n"
            "└── zero.txt [PRESENT · EMPTY]\n"
            "```\n"
            f"See [the guide]({link}).\n"
        )
        self.readme.write_text(content, encoding="utf-8")

    def run_validation(self):
        return validate_repository(
            self.root,
            readmes=[self.readme],
            approved_absent=self.approved_absent,
        )

    def test_accepts_complete_two_level_tree_and_encoded_link(self) -> None:
        self.write_readme()
        result = self.run_validation()
        self.assertEqual(result.errors, [])
        self.assertEqual(result.tree_blocks, 1)
        self.assertEqual(result.links_checked, 1)
        self.assertIn("UNVERIFIED", result.status_counts)
        self.assertIn("VERIFIED", result.status_counts)
        self.assertIn("RETIRED", result.status_counts)
        self.assertIn("STUB", result.status_counts)
        self.assertTrue(result.qualifications)

    def test_accepts_ascii_tree_and_tilde_fence(self) -> None:
        self.write_readme()
        text = self.readme.read_text(encoding="utf-8")
        text = text.replace("```text", "~~~text").replace("```", "~~~")
        text = text.replace("├──", "+--").replace("└──", "+--")
        text = text.replace("│   ", "|   ")
        self.readme.write_text(text, encoding="utf-8")
        result = self.run_validation()
        self.assertEqual(result.errors, [])

    def test_required_status_vocabulary_is_supported(self) -> None:
        self.assertEqual(
            STATUS_TOKENS,
            {
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
            },
        )

    def test_rejects_unknown_and_misspelled_status_tags(self) -> None:
        cases = (
            ("guide file.md [PRESENT]", "guide file.md [PRESNET]", "PRESNET"),
            (
                "guide file.md [PRESENT]",
                "guide file.md [PRESENT \u00b7 POPULATD]",
                "POPULATD",
            ),
        )
        for original, replacement, unknown in cases:
            with self.subTest(unknown=unknown):
                self.write_readme()
                text = self.readme.read_text(encoding="utf-8")
                self.assertIn(original, text)
                self.readme.write_text(text.replace(original, replacement), encoding="utf-8")
                result = self.run_validation()
                self.assertTrue(
                    any(f"unrecognized structural/status tag {unknown!r}" in error for error in result.errors),
                    result.errors,
                )

    def test_reports_physical_child_missing_from_tree(self) -> None:
        self.write_readme()
        (self.parent / "omitted.md").write_text("present\n", encoding="utf-8")
        result = self.run_validation()
        self.assertTrue(any("omitted.md" in error and "missing from local tree" in error for error in result.errors))

    def test_rejects_third_descendant_level(self) -> None:
        self.write_readme()
        deep = self.docs / "DEEP_GOV_BRAINBOX"
        deep.mkdir()
        nested = deep / "nested.md"
        nested.write_text("nested\n", encoding="utf-8")
        text = self.readme.read_text(encoding="utf-8")
        text = text.replace(
            "│   ├── guide file.md [PRESENT]\n",
            "│   ├── guide file.md [PRESENT]\n"
            "│   ├── DEEP_GOV_BRAINBOX/ [PRESENT · POPULATED]\n"
            "│   │   └── nested.md [PRESENT]\n",
        )
        self.readme.write_text(text, encoding="utf-8")
        result = self.run_validation()
        self.assertTrue(any("exceeds two descendant levels" in error for error in result.errors))

    def test_rejects_unapproved_absent_planned_path(self) -> None:
        self.write_readme()
        text = self.readme.read_text(encoding="utf-8")
        text = text.replace(
            "FUTURE_GOV_BRAINBOX/ [ABSENT · PLANNED]",
            "UNAPPROVED_GOV_BRAINBOX/ [ABSENT · PLANNED]",
        )
        self.readme.write_text(text, encoding="utf-8")
        result = self.run_validation()
        self.assertTrue(any("not in the approved absent-path list" in error for error in result.errors))

    def test_approved_absence_is_matched_from_repository_root(self) -> None:
        sandbox = (
            self.root
            / "AI_BRAINBOX"
            / "DEVOPS_AI_BRAINBOX"
            / "SANDBOX_DEVOPS_BRAINBOX"
        )
        sandbox.mkdir(parents=True)
        (sandbox / "POC_SANDBOX_BRAINBOX").mkdir()
        readme = sandbox / "README_SANDBOX_DEVOPS_BRAINBOX.md"
        readme.write_text(
            "## Canonical local tree\n"
            "```text\n"
            "SANDBOX_DEVOPS_BRAINBOX/ [PRESENT]\n"
            "\u251c\u2500\u2500 FAILED_SANDBOX_BRAINBOX/ [ABSENT \u00b7 PLANNED]\n"
            "\u251c\u2500\u2500 PASSED_SANDBOX_BRAINBOX/ [ABSENT \u00b7 PLANNED]\n"
            "\u251c\u2500\u2500 POC_SANDBOX_BRAINBOX/ [PRESENT]\n"
            "\u2514\u2500\u2500 README_SANDBOX_DEVOPS_BRAINBOX.md [PRESENT]\n"
            "```\n",
            encoding="utf-8",
        )
        expected = {
            "AI_BRAINBOX/DEVOPS_AI_BRAINBOX/SANDBOX_DEVOPS_BRAINBOX/FAILED_SANDBOX_BRAINBOX",
            "AI_BRAINBOX/DEVOPS_AI_BRAINBOX/SANDBOX_DEVOPS_BRAINBOX/PASSED_SANDBOX_BRAINBOX",
        }
        self.assertTrue(expected.issubset(APPROVED_ABSENT))
        result = validate_repository(self.root, readmes=[readme])
        self.assertEqual(result.errors, [])

    def test_rejects_poc_nested_approved_absence_paths(self) -> None:
        poc = (
            self.root
            / "AI_BRAINBOX"
            / "DEVOPS_AI_BRAINBOX"
            / "SANDBOX_DEVOPS_BRAINBOX"
            / "POC_SANDBOX_BRAINBOX"
        )
        poc.mkdir(parents=True)
        readme = poc / "README_POC_SANDBOX_BRAINBOX.md"
        readme.write_text(
            "## Canonical local tree\n"
            "```text\n"
            "POC_SANDBOX_BRAINBOX/ [PRESENT]\n"
            "\u251c\u2500\u2500 FAILED_SANDBOX_BRAINBOX/ [ABSENT \u00b7 PLANNED]\n"
            "\u251c\u2500\u2500 PASSED_SANDBOX_BRAINBOX/ [ABSENT \u00b7 PLANNED]\n"
            "\u2514\u2500\u2500 README_POC_SANDBOX_BRAINBOX.md [PRESENT]\n"
            "```\n",
            encoding="utf-8",
        )
        incorrect = {
            "AI_BRAINBOX/DEVOPS_AI_BRAINBOX/SANDBOX_DEVOPS_BRAINBOX/POC_SANDBOX_BRAINBOX/FAILED_SANDBOX_BRAINBOX",
            "AI_BRAINBOX/DEVOPS_AI_BRAINBOX/SANDBOX_DEVOPS_BRAINBOX/POC_SANDBOX_BRAINBOX/PASSED_SANDBOX_BRAINBOX",
        }
        self.assertTrue(incorrect.isdisjoint(APPROVED_ABSENT))
        result = validate_repository(self.root, readmes=[readme])
        self.assertTrue(any("not in the approved absent-path list" in error for error in result.errors))

    def test_rejects_broken_url_decoded_markdown_target(self) -> None:
        self.write_readme(link="missing%20file.md")
        result = self.run_validation()
        self.assertTrue(any("missing file.md" in error and "broken local Markdown target" in error for error in result.errors))

    def test_rejects_local_link_that_escapes_repository(self) -> None:
        outside = self.temp_root / "outside.md"
        outside.write_text("outside\n", encoding="utf-8")
        self.write_readme(link="../../outside.md")
        result = self.run_validation()
        self.assertTrue(any("escapes repository root" in error for error in result.errors))

    def test_checks_empty_file_status_against_bytes(self) -> None:
        self.write_readme()
        (self.parent / "zero.txt").write_text("not empty\n", encoding="utf-8")
        result = self.run_validation()
        self.assertTrue(any("EMPTY status requires a zero-byte file" in error for error in result.errors))

    def test_cli_exits_nonzero_for_a_real_tree_violation(self) -> None:
        self.write_readme()
        (self.parent / "omitted.md").write_text("present\n", encoding="utf-8")
        script = Path(__file__).with_name("validate_tree_status.py")
        completed = subprocess.run(
            [
                sys.executable,
                "-B",
                str(script),
                str(self.root),
                "--readme",
                str(self.readme),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 1)
        self.assertIn("omitted.md", completed.stdout)
        self.assertIn("README_GOV_BRAINBOX.md:4: expected path missing from local tree", completed.stdout)


class LocalOnlyAssetInventoryTests(unittest.TestCase):
    """The V02 exception is exact-listed, optional in clean checkouts, and hash-checked locally."""

    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        self.project_dir = self.root / validator.LOCAL_ONLY_ASSET_PROJECT_README.parent
        self.assets_dir = self.root / validator.LOCAL_ONLY_ASSET_DIRECTORY
        self.assets_dir.mkdir(parents=True)
        self.project_readme = self.root / validator.LOCAL_ONLY_ASSET_PROJECT_README
        self.assets_readme = self.root / validator.LOCAL_ONLY_ASSET_README

        self.payloads = {}
        self.declarations = {}
        for index, (record_id, approved) in enumerate(validator.LOCAL_ONLY_ASSET_DECLARATIONS.items(), 1):
            payload = f"fixture-local-asset-{index}\n".encode("utf-8")
            self.payloads[approved["file"]] = payload
            self.declarations[record_id] = {
                "file": approved["file"],
                "bytes": len(payload),
                "sha256": hashlib.sha256(payload).hexdigest(),
            }
        self.declaration_patch = patch.object(
            validator, "LOCAL_ONLY_ASSET_DECLARATIONS", self.declarations
        )
        self.declaration_patch.start()
        self.addCleanup(self.declaration_patch.stop)
        self.write_readmes()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_readmes(self) -> None:
        header = "| " + " | ".join(validator.LOCAL_ONLY_ASSET_TABLE_HEADER) + " |\n"
        separator = "|---|---|---|---|---|---|---|\n"
        rows = []
        for record_id, record in self.declarations.items():
            rows.append(
                "| `{}` | Fixture {} | Design reference | Operator-provided fixture; local filename {} (source path omitted) | "
                "PNG / {:,} bytes / `{}` | {} | Fixture rights and production use are not approved |\n".format(
                    record_id,
                    record_id,
                    record["file"],
                    record["bytes"],
                    record["sha256"],
                    validator.LOCAL_ONLY_ASSET_STATE,
                )
            )
        asset_text = (
            "# Asset fixture\n\n"
            "## Canonical local tree\n\n"
            "```text\n"
            "ASSETS_FH_V02_BRAINBOX/ [PRESENT · POPULATED]\n"
            "└── README_ASSETS_FH_V02_BRAINBOX.md [PRESENT]\n"
            "```\n\n"
            "## Current reference inventory\n\n"
            + header
            + separator
            + "".join(rows)
        )
        self.assets_readme.write_text(asset_text, encoding="utf-8")
        project_text = (
            "# Project fixture\n\n"
            "## Canonical local tree\n\n"
            "```text\n"
            "FOOTHIVE_V02_POC_BRAINBOX/ [PRESENT · POPULATED]\n"
            "├── ASSETS_FH_V02_BRAINBOX/ [PRESENT · POPULATED]\n"
            "│   └── README_ASSETS_FH_V02_BRAINBOX.md [PRESENT]\n"
            "└── README_FH_V02_POC_BRAINBOX.md [PRESENT]\n"
            "```\n\n"
            "See [asset inventory](ASSETS_FH_V02_BRAINBOX/README_ASSETS_FH_V02_BRAINBOX.md).\n"
        )
        self.project_readme.write_text(project_text, encoding="utf-8")

    def write_assets(self, names: set[str] | None = None) -> None:
        for filename in names if names is not None else set(self.payloads):
            (self.assets_dir / filename).write_bytes(self.payloads[filename])

    def run_validation(self):
        return validate_repository(self.root, readmes=[self.assets_readme, self.project_readme])

    def test_tracked_only_checkout_accepts_absent_local_only_assets(self) -> None:
        result = self.run_validation()
        self.assertEqual(result.errors, [])
        self.assertEqual(result.local_only_assets_declared, 3)
        self.assertEqual(result.local_only_assets_present, 0)
        self.assertEqual(result.links_checked, 1)

    def test_original_checkout_accepts_all_present_assets_with_matching_hashes(self) -> None:
        self.write_assets()
        result = self.run_validation()
        self.assertEqual(result.errors, [])
        self.assertEqual(result.local_only_assets_declared, 3)
        self.assertEqual(result.local_only_assets_present, 3)

    def test_present_local_only_asset_with_wrong_bytes_fails_integrity_check(self) -> None:
        filename = next(iter(self.payloads))
        (self.assets_dir / filename).write_bytes(b"different bytes\n")
        result = self.run_validation()
        self.assertTrue(any("local-only asset integrity mismatch" in error for error in result.errors), result.errors)

    def test_one_declared_local_only_asset_may_be_absent(self) -> None:
        self.write_assets(set(self.payloads) - {next(iter(self.payloads))})
        result = self.run_validation()
        self.assertEqual(result.errors, [])
        self.assertEqual(result.local_only_assets_present, 2)

    def test_missing_required_project_readme_still_fails(self) -> None:
        self.project_readme.unlink()
        result = validate_repository(self.root, readmes=[self.project_readme, self.assets_readme])
        self.assertTrue(any("cannot read UTF-8 Markdown" in error for error in result.errors), result.errors)

    def test_undeclared_extra_asset_remains_a_tree_completeness_finding(self) -> None:
        self.write_assets()
        (self.assets_dir / "unexpected.bin").write_bytes(b"unlisted")
        result = self.run_validation()
        self.assertTrue(
            any("expected path missing from local tree" in error and "unexpected.bin" in error for error in result.errors),
            result.errors,
        )

    def test_invalid_local_only_state_vocabulary_is_rejected(self) -> None:
        text = self.assets_readme.read_text(encoding="utf-8")
        text = text.replace(
            validator.LOCAL_ONLY_ASSET_STATE,
            "LOCAL_ONLY; EXCLUDED_FROM_GIT; PRODUCTION_APPROVED",
            1,
        )
        self.assets_readme.write_text(text, encoding="utf-8")
        result = self.run_validation()
        self.assertTrue(any("invalid local-only state" in error for error in result.errors), result.errors)

    def test_malformed_size_hash_declaration_is_rejected(self) -> None:
        text = self.assets_readme.read_text(encoding="utf-8")
        text = text.replace("PNG / ", "image / ", 1)
        self.assets_readme.write_text(text, encoding="utf-8")
        result = self.run_validation()
        self.assertTrue(any("malformed format/size/SHA-256" in error for error in result.errors), result.errors)

    def test_unapproved_missing_path_cannot_be_declared_local_only(self) -> None:
        text = self.assets_readme.read_text(encoding="utf-8")
        record = next(iter(self.declarations.values()))
        text = text.replace(record["file"], "UNRELATED_MISSING.png", 1)
        self.assets_readme.write_text(text, encoding="utf-8")
        result = self.run_validation()
        self.assertTrue(any("does not name its approved exact file" in error for error in result.errors), result.errors)

    def test_missing_ordinary_present_path_is_not_exempted(self) -> None:
        text = self.project_readme.read_text(encoding="utf-8")
        text = text.replace(
            "└── README_FH_V02_POC_BRAINBOX.md [PRESENT]",
            "├── README_FH_V02_POC_BRAINBOX.md [PRESENT]\n└── MISSING_ORDINARY.md [PRESENT]",
        )
        self.project_readme.write_text(text, encoding="utf-8")
        result = self.run_validation()
        self.assertTrue(any("PRESENT status points to missing path" in error and "MISSING_ORDINARY.md" in error for error in result.errors), result.errors)

    @unittest.skipUnless(shutil.which("git"), "Git CLI unavailable")
    def test_local_only_asset_must_not_be_in_git_index(self) -> None:
        self.write_assets()
        filename = next(iter(self.payloads))
        subprocess.run(["git", "init", "--quiet", str(self.root)], check=True)
        relative = (validator.LOCAL_ONLY_ASSET_DIRECTORY / filename).as_posix()
        subprocess.run(
            ["git", "-c", "core.autocrlf=false", "-C", str(self.root), "add", "--", relative],
            check=True,
        )
        result = self.run_validation()
        self.assertTrue(any("local-only asset is present in the Git index" in error for error in result.errors), result.errors)


if __name__ == "__main__":
    unittest.main()

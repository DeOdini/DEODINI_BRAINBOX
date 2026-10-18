"""Controlled fixtures for the read-only Governance tree/status validator."""

from __future__ import annotations

import sys
import subprocess
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))

from validate_tree_status import STATUS_TOKENS, validate_repository  # noqa: E402


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
        nested_parent = (
            self.root
            / "AI_BRAINBOX"
            / "DEVOPS_AI_BRAINBOX"
            / "SANDBOX_DEVOPS_BRAINBOX"
            / "POC_SANDBOX_BRAINBOX"
        )
        nested_parent.mkdir(parents=True)
        readme = nested_parent / "README_POC_SANDBOX.md"
        readme.write_text(
            "## Canonical local tree\n"
            "```text\n"
            "POC_SANDBOX_BRAINBOX/ [PRESENT · POPULATED]\n"
            "├── FAILED_SANDBOX_BRAINBOX/ [ABSENT · PLANNED]\n"
            "├── PASSED_SANDBOX_BRAINBOX/ [ABSENT · PLANNED]\n"
            "└── README_POC_SANDBOX.md [PRESENT]\n"
            "```\n",
            encoding="utf-8",
        )
        approved = {
            "AI_BRAINBOX/DEVOPS_AI_BRAINBOX/SANDBOX_DEVOPS_BRAINBOX/POC_SANDBOX_BRAINBOX/FAILED_SANDBOX_BRAINBOX",
            "AI_BRAINBOX/DEVOPS_AI_BRAINBOX/SANDBOX_DEVOPS_BRAINBOX/POC_SANDBOX_BRAINBOX/PASSED_SANDBOX_BRAINBOX",
        }
        result = validate_repository(self.root, readmes=[readme], approved_absent=approved)
        self.assertEqual(result.errors, [])

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


if __name__ == "__main__":
    unittest.main()

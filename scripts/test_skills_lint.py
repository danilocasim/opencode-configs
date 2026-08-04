"""Focused regression tests for Markdown-reference validation."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("skills_lint.py")
SPEC = importlib.util.spec_from_file_location("skills_lint", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
skills_lint = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = skills_lint
SPEC.loader.exec_module(skills_lint)


class MarkdownReferenceValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.original_root = skills_lint.ROOT
        skills_lint.ROOT = self.root

    def tearDown(self) -> None:
        skills_lint.ROOT = self.original_root
        self.temp_dir.cleanup()

    def write_skill(self, name: str, body: str) -> Path:
        skill_dir = self.root / "skills" / name
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            textwrap.dedent(
                f"""\
                ---
                name: {name}
                description: Test skill
                ---

                # Test skill

                {body}
                """
            ),
            encoding="utf-8",
        )
        return skill_dir

    def test_ignores_artifact_and_cross_skill_inline_code(self) -> None:
        skill_dir = self.write_skill(
            "router",
            "Use `STORYBOARD.md`, `.media/index.md`, and `other-skill/SKILL.md`.",
        )

        self.assertEqual(skills_lint.lint_skill_dir(skill_dir), [])

    def test_ignores_links_in_fenced_markdown_examples(self) -> None:
        skill_dir = self.write_skill(
            "router",
            """
            ```markdown
            [future guide](./guide.md)
            ```
            """,
        )

        self.assertEqual(skills_lint.lint_skill_dir(skill_dir), [])

    def test_reports_missing_explicit_relative_and_root_references(self) -> None:
        skill_dir = self.write_skill(
            "router",
            """
            [local guide](./missing.md)
            [parent guide](../missing-parent.md)
            [root guide](skills/missing-skill/SKILL.md)
            """,
        )

        messages = [issue.message for issue in skills_lint.lint_skill_dir(skill_dir)]

        self.assertEqual(
            messages,
            [
                "references missing file: ../missing-parent.md",
                "references missing file: ./missing.md",
                "references missing file: skills/missing-skill/SKILL.md",
            ],
        )

    def test_v2_leaf_coverage_still_uses_code_span_basenames(self) -> None:
        skill_dir = self.write_skill("testing", "See `covered.md` for the guide.")
        (skill_dir / "covered.md").write_text("# Covered\n", encoding="utf-8")
        (skill_dir / "uncovered.md").write_text("# Uncovered\n", encoding="utf-8")

        messages = [issue.message for issue in skills_lint.lint_skill_dir(skill_dir)]

        self.assertIn("SKILL.md does not reference leaf: uncovered.md", messages)
        self.assertNotIn("SKILL.md does not reference leaf: covered.md", messages)


if __name__ == "__main__":
    unittest.main()

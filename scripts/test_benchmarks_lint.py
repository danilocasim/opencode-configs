"""Regression coverage for per-scenario benchmark contracts."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from pathlib import Path


SPEC = importlib.util.spec_from_file_location(
    "benchmarks_lint", Path(__file__).with_name("benchmarks_lint.py")
)
assert SPEC is not None and SPEC.loader is not None
benchmarks_lint = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = benchmarks_lint
SPEC.loader.exec_module(benchmarks_lint)

VALID = "## Repair\n\nPrompt:\nFix it.\nExpected loads:\n- testing\nExpected traits:\n- Verified.\n"


class BenchmarkValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)
        self.path = self.root / "flow.md"

    def lint(self, text: str) -> list[str]:
        self.path.write_text(text, encoding="utf-8")
        return [
            issue.message for issue in benchmarks_lint.lint_benchmark_file(self.path)
        ]

    def test_accepts_multiple_complete_scenarios(self) -> None:
        self.assertEqual(
            self.lint("# Flow\n" + VALID + VALID.replace("Repair", "Review")), []
        )

    def test_second_scenario_cannot_borrow_first_scenarios_markers(self) -> None:
        issues = self.lint(VALID + "## WIP\nPrompt:\nReview dirty changes.\n")
        self.assertIn("WIP: missing required marker: Expected loads:", issues)

    def test_empty_marker_is_not_a_contract(self) -> None:
        issues = self.lint(VALID.replace("- testing\n", "\n"))
        self.assertIn("Repair: empty section: Expected loads:", issues)

    def test_requires_scenario_headings(self) -> None:
        self.assertIn(
            "no benchmark scenarios (expected ## headings)", self.lint("# Flow\n")
        )

    def test_rejects_file_as_directory_without_traceback(self) -> None:
        self.path.touch()
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(
                benchmarks_lint.main(["--benchmarks-dir", str(self.path)]), 1
            )


if __name__ == "__main__":
    unittest.main()

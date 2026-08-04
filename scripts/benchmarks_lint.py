#!/usr/bin/env python3

"""Lint OpenCode benchmark prompts for consistency.

Benchmarks are human-authored and should be retrieval-friendly. This linter
validates a minimal schema so benchmarks stay useful as regression tests.

Default behavior:
- Lint benchmarks under ./benchmarks

Exit codes:
- 0: no issues
- 1: issues found
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_MARKERS = [
    "Prompt:",
    "Expected loads:",
    "Expected traits:",
]


@dataclass(frozen=True)
class Issue:
    path: Path
    message: str


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def lint_benchmark_file(path: Path) -> list[Issue]:
    issues: list[Issue] = []
    text = _read_text(path)

    for marker in REQUIRED_MARKERS:
        if marker not in text:
            issues.append(Issue(path, f"missing required marker: {marker}"))
            break

    return issues


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Lint OpenCode benchmarks")
    parser.add_argument(
        "--benchmarks-dir",
        type=str,
        default=None,
        help="Path to benchmarks directory to lint (defaults to ./benchmarks)",
    )
    args = parser.parse_args(argv)

    benchmarks_dir = Path(args.benchmarks_dir).expanduser() if args.benchmarks_dir else (ROOT / "benchmarks")

    if not benchmarks_dir.exists():
        print(f"benchmarks dir not found: {benchmarks_dir}", file=sys.stderr)
        return 1

    issues: list[Issue] = []
    for path in sorted(benchmarks_dir.glob("*.md")):
        if path.name.upper() == "README.MD":
            continue
        issues.extend(lint_benchmark_file(path))

    if not issues:
        print("benchmarks_lint: OK")
        return 0

    print(f"benchmarks_lint: {len(issues)} issue(s)")
    for issue in issues:
        rel = issue.path
        try:
            rel = issue.path.relative_to(ROOT)
        except ValueError:
            pass
        print(f"- {rel}: {issue.message}")

    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

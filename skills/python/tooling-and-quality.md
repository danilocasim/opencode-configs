# Tooling and Quality (uv + ruff + pyright)

This is the recommended default toolchain for new Python code you expect an LLM to maintain: fast installs, strict formatting, strict types.

## When to load

- You are setting up a new Python project.
- You want a modern default toolchain (uv + ruff + pyright).
- You need CI quality gates to prevent drift.

## When NOT to load

- You only need test design guidance -> `../testing/SKILL.md`.
- You only need docstring style -> `documentation-and-comments.md`.

## Core rules

- Use one source of truth: `pyproject.toml`.
- Format + lint with Ruff; type check with Pyright.
- CI order: format -> lint -> typecheck -> tests.
- Prefer reproducible installs.

## Common patterns

- Dependency manager: `uv`.
- Formatter/linter: `ruff format` and `ruff check`.
- Type checker: `pyright` in strict mode.

## Minimal examples

`pyproject.toml` (starter)

```toml
[project]
name = "mypkg"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = []

[dependency-groups]
dev = [
  "pytest>=8",
  "pytest-cov>=5",
  "ruff>=0.6",
  "pyright>=1.1",
]

[tool.ruff]
line-length = 88
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "UP", "B", "SIM"]

[tool.pyright]
typeCheckingMode = "strict"
pythonVersion = "3.12"
```

Commands

```bash
uv sync
ruff format .
ruff check .
pyright
pytest
```

## Anti-patterns

- Multiple formatters/lints fighting each other.
- Type checking only in IDE.
- Global installs that diverge from CI.

## Checklist

- `pyproject.toml` defines tool config
- Ruff format + check runs in CI
- Pyright strict runs in CI
- Tests run on a pinned Python version

## References

- uv: https://docs.astral.sh/uv/
- ruff: https://docs.astral.sh/ruff/
- pyright: https://microsoft.github.io/pyright/

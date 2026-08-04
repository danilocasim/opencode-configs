# Recipe: CLI Tool (Python)

Build CLIs that are predictable, testable, and automation-friendly.

## When to load

- You are building a Python CLI (internal tool, ops helper, codegen).
- You need predictable exit codes and deterministic output.

## When NOT to load

- You are building agent-facing tools -> `recipes-agent-tool.md`.

## Core rules

- Keep `main(argv)` small: parse args -> call domain -> print -> exit.
- Errors go to stderr.
- Support deterministic `--json` output when useful.
- Do not do heavy work at import time.

## Common patterns

- Use `argparse` (stdlib) unless repo already uses `typer`.
- Domain function returns data; presentation formats it.

## Minimal examples

`src/mypkg/cli.py`

```python
from __future__ import annotations

import argparse
import json
import sys


def run(*, name: str) -> dict[str, str]:
    return {"greeting": f"Hello, {name}!"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="mypkg")
    parser.add_argument("name")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    try:
        out = run(name=args.name)
    except Exception as err:
        print(str(err), file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(out, sort_keys=True))
    else:
        print(out["greeting"])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## Anti-patterns

- Printing stack traces for expected user errors.
- Non-deterministic output ordering.
- Mixing stdout/stderr unpredictably.

## Checklist

- `main(argv)` is testable
- Exit codes are consistent
- Errors go to stderr
- Optional `--json` output is deterministic

## References

- argparse: https://docs.python.org/3/library/argparse.html
- SystemExit: https://docs.python.org/3/library/exceptions.html#SystemExit

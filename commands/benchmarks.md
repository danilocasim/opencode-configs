---
description: Lint benchmarks for consistent format
---

Run the benchmark linter and fix any issues.

Run:

```bash
python3 -B "$HOME/.config/opencode/scripts/benchmarks_lint.py"
```

If there are errors:

- Update each failing scenario (a `##` heading) to include non-empty sections:
  - `Prompt:`
  - `Expected loads:`
  - `Expected traits:`

---
description: Run the closest equivalent of CI locally
---

Run the project's CI-like checks.

$ARGUMENTS

Workflow:

1. Identify the CI entrypoint (package.json scripts, Makefile, GitHub Actions, etc.).
2. Run format/lint/tests/build in the same order.
3. Summarize failures and fix the highest-signal issues first.

For this OpenCode skills repo, the baseline CI-like checks are:

```bash
python3 -B "$HOME/.config/opencode/scripts/skills_lint.py"
python3 -B "$HOME/.config/opencode/scripts/skills_lint.py" --skills-dir "$HOME/.config/opencode/.agents/skills"
python3 -B "$HOME/.config/opencode/scripts/benchmarks_lint.py"
python3 -B -m unittest discover -s "$HOME/.config/opencode/scripts" -p 'test_*.py'
git -C "$HOME/.config/opencode" diff --check
```

Scope any optional formatter check to intended non-secret files. Do not recursively
format or print the whole configuration directory, which contains runtime state.

# Staging and Hygiene

Stage intentionally so commits stay reviewable, and prevent secrets/noise from entering history.

## When to load

- You want to stage only the right hunks/files.
- The diff is noisy (formatters, generated files, lockfiles).
- You want practical secret-safety habits.

## When NOT to load

- You need message style or splitting logic (`commits.md`).
- You need branch/PR conventions (`branching-and-prs.md`).
- You need revert/backport/conflict guidance (`troubleshooting.md`).

## Core rules

- Don't treat `git add .` as default.
- Review staged diff before committing.
- Keep generated/lockfile/vendor changes only when justified.
- Never commit secrets; assume history is durable and replicated.

## Patterns

Default staging loop:

- `git status -sb`
- `git diff`
- `git add -p` (or `git add <path>`)
- `git diff --staged`
- `git commit`

## Minimal examples

Stage only the relevant hunks:

```bash
git add -p
git diff --staged
git commit --verbose
```

Undo staging a hunk you staged by accident:

```bash
git restore -p --staged
```

Hygiene for noisy changes:

- Separate formatting from behavior changes (separate commits).
- If a formatter touched many files, make sure it was expected.
- Isolate lockfile-only churn when it dominates the diff.

Secret safety:

- Before committing, search the staged diff for obvious key markers: `TOKEN`, `SECRET`, `PRIVATE`, `API_KEY`, `PASSWORD`.
- If a secret might be present: stop and fix before pushing.

## Anti-patterns

- Committing without reviewing the staged diff.
- Mixing drive-by cleanup into a feature/bugfix commit.
- Adding secrets "temporarily".
- Committing generated output without knowing how it was produced.

## Checklist

- `git status -sb` shows only expected changes.
- Staged diff matches commit intent; no stray hunks.
- Generated/lockfile changes are isolated or justified.
- No secrets or local-only config are staged.

## References

- `man git-add`, `man git-restore`
- Inspect staged diff: `git diff --staged`

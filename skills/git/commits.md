# Commits

Make commits consistent across projects by keeping each commit to one intent and writing messages that explain outcomes and reasons.

## When to load

- You are about to commit and want consistent message style.
- You need to split one messy change into logical commits.
- You are unsure what belongs in subject vs body.

## When NOT to load

- You mainly need staging tactics or secret safety (`staging-and-hygiene.md`).
- You are preparing a PR/branch naming (`branching-and-prs.md`).
- You are fixing history, reverting, or cherry-picking (`troubleshooting.md`).

## Core rules

- One intent per commit: a commit should answer "what changed and why" in one sentence.
- Subject: imperative mood, no period, ideally <= 72 characters.
- Body (recommended when non-trivial): explain why, constraints, and side effects; wrap ~72.
- Prefer outcome language over implementation details.
- Match repo convention first (Conventional Commits, merge strategy, templates).

## Patterns

### Message formats (pick one; match the repo)

Simple (universal):

- `Add rate limiting to login endpoint`
- `Fix crash when cache is empty`

Type + optional scope (portable consistency):

- `fix(auth): reject expired refresh tokens`
- `refactor(api): extract pagination parsing`
- `docs(readme): clarify local setup`

Suggested types (keep small set):

- `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `build`, `ci`

## Minimal examples

Good subjects:

- `fix(auth): reject expired refresh tokens`
- `feat(projects): add archived filter to list`
- `refactor(orders): move checkout workflow into service object`
- `test(billing): add regression for retry double-charge`

Bad subjects:

- `updates`
- `fix`
- `wip`

Splitting example (common):

If your diff includes:

- formatting across many files
- a refactor to extract a service
- the actual behavior change

Prefer 2-3 commits:

1. `chore: format` (only if necessary)
2. `refactor(domain): extract service object`
3. `fix(domain): correct behavior and add tests`

### Body template

- `Why:` what problem prompted this
- `What:` high-level change
- `Notes:` risks, migrations, rollout constraints

### When to split a commit

Split when any are true:

- The diff mixes behavior change with formatting/cleanup.
- Multiple components could be reverted independently.
- A reviewer would approve part and request changes on the rest.
- Mechanical changes bury the meaningful change.

Common split sequence:

1. `refactor:` prepare (no behavior change)
2. `feat:` or `fix:` behavior
3. `test:` add/expand coverage (if separate improves clarity)

## Anti-patterns

- `WIP`, `temp`, `changes`, `updates`.
- Drive-by refactors inside a bug fix without explanation.
- Huge commits that cannot be reverted safely.
- Apology bodies instead of documenting constraints/trade-offs.

## Checklist

- Subject is imperative and specific.
- Commit contains one intent.
- Body explains why when non-obvious.
- You reviewed `git diff --staged`.
- You can revert this commit alone without collateral damage.

## References

- `man git-commit`
- Good loop: `git status -sb` -> `git diff` -> `git add -p` -> `git diff --staged`

# Branching and PRs

Portable conventions for naming branches and writing PRs that are easy to review.

## When to load

- You need branch naming that stays consistent across projects.
- You are writing a PR title/body.
- You want a lightweight PR hygiene checklist.

## When NOT to load

- You are deciding commit boundaries/message style (`commits.md`).
- You are staging changes or checking for secrets (`staging-and-hygiene.md`).
- You need revert/backport/conflict guidance (`troubleshooting.md`).

## Core rules

- Branch names communicate intent, not implementation.
- PR titles summarize outcomes; PR bodies explain why, approach, and verification.
- Keep PRs reviewable: small surface area, minimal drive-by changes.
- Follow the repo's merge strategy and PR template first.

## Patterns

Branch naming (portable):

- `{type}/{short-slug}` or `{type}/{ticket}-{short-slug}`

Types (keep stable):

- `feature/`, `fix/`, `refactor/`, `docs/`, `chore/`, `hotfix/`, `test/`

Examples:

- `fix/PROJ-481-null-crash-on-startup`
- `feature/oauth-device-flow`
- `docs/api-auth-setup`

PR title patterns:

- Plain imperative: `Add device-flow login`
- Type + scope: `fix(auth): reject expired refresh tokens`

PR body template:

- `Why:` problem statement
- `What:` 2-5 bullets, high level
- `How to test:` commands or steps
- `Risks/rollout:` migrations, flags, backwards compatibility

## Minimal examples

PR body (copy-ready):

```text
Why:
- Users sometimes hit a 500 when the cache is empty.

What:
- Default missing cache entries to an empty list.
- Add regression tests for the empty-cache path.

How to test:
- run: <project test command>
- manual: open <page> and verify no error on first load

Risks/rollout:
- Low risk; change only affects empty-cache behavior.
```

## Anti-patterns

- Branch names like `new`, `test`, `stuff`.
- PRs mixing refactor + feature + formatting with no explanation.
- Empty PR body for non-trivial changes.
- Pushing broken builds without calling it out.

## Checklist

- Branch name matches type and intent.
- PR title describes outcome and matches project conventions.
- PR body answers why/what/how-to-test.
- CI passes (or failures explained).

## References

- `man git-branch`, `man git-switch`
- Many repos have PR templates in `.github/PULL_REQUEST_TEMPLATE*`

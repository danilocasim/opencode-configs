# Recipe: Create a Pull Request

Create a well-structured PR using `gh pr create` with proper title, body, and context.

## Goal

Create a PR that is easy to review with clear motivation, changes, and test plan.

## Load

- `SKILL.md`
- `prs.md`
- `../git/branching-and-prs.md`

## Preconditions

- Branch exists with changes committed.
- Branch is pushed to remote.
- CI passes (if configured).

## Files to touch

- None (PR is created on GitHub).

## Steps

1. Verify current branch and push status:

```bash
git branch --show-current
git status
```

2. Gather context (view recent commits):

```bash
git log main..HEAD --oneline
```

3. Create PR with structured body:

```bash
gh pr create --title "<type>(<scope>): <imperative summary>" --body "$(cat <<'EOF'
Why:
- <problem statement>

What:
- <2-5 bullets of changes>

How to test:
- Run: <test command>
- Manual: <steps>

Risks/rollout:
- <migration/flag/backwards compatibility notes>
EOF
)"
```

4. Verify PR was created:

```bash
gh pr view --web
```

## Anti-patterns

- Creating PR without pushing branch first.
- Empty body for non-trivial changes.
- Title that describes implementation, not outcome.

## Test plan

- Open PR URL in browser.
- Verify title, body, and CI status.
- Request review if ready.

## Commit message

(Not applicable - this creates a PR, not a commit.)

## PR body (copy-ready)

```text
Why:
-

What:
-

How to test:
- Run:
- Manual:

Risks/rollout:
-
```

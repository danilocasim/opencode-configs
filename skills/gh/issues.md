# Issues

Create, view, and manage GitHub issues using `gh issue`.

## When to load

- You are creating a new issue.
- You need to view or close existing issues.
- You are triaging or labeling issues.

## When NOT to load

- You are working with PRs (use `prs.md`).
- You are viewing workflow runs (use `actions.md`).

## Core commands

```bash
gh issue list                        # List open issues
gh issue list --state closed         # List closed issues
gh issue view <number>               # View issue details
gh issue view <number> --web         # Open in browser
gh issue create                      # Create new issue
gh issue close <number>              # Close an issue
gh issue reopen <number>             # Reopen an issue
gh issue edit <number>               # Edit an issue
gh issue comment <number>            # Add a comment
```

## Common patterns

### Create an issue

```bash
gh issue create --title "Login fails on Safari" --body "Steps to reproduce..."
```

With body from heredoc:

```bash
gh issue create --title "Login fails on Safari" --body "$(cat <<'EOF'
## Description
Login button is unresponsive on Safari 16.

## Steps to reproduce
1. Open Safari 16
2. Navigate to /login
3. Click "Sign In"
4. Observe: nothing happens

## Expected behavior
Should redirect to dashboard.

## Environment
- Safari 16.1
- macOS Ventura
EOF
)"
```

### View issue details

```bash
gh issue view 42
gh issue view 42 --json title,body,state,labels
gh issue view 42 --web
```

### List and filter issues

```bash
gh issue list --label bug
gh issue list --assignee @me
gh issue list --state all --limit 50
gh issue list --search "login error"
```

### Triage operations

```bash
gh issue edit 42 --add-label "bug,priority:high"
gh issue edit 42 --remove-label "needs-triage"
gh issue edit 42 --add-assignee "@me"
gh issue close 42 --comment "Fixed in #123"
gh issue comment 42 --body "Investigating..."
```

## Minimal examples

Quick bug report:

```bash
gh issue create --title "500 error on /api/users" --body "$(cat <<'EOF'
## What
GET /api/users returns 500 when query param `filter` is empty.

## Repro
`curl /api/users?filter=`

## Expected
400 Bad Request or empty result set.
EOF
)"
```

## Anti-patterns

- Vague issue titles ("Doesn't work", "Error").
- Missing reproduction steps.
- Using `--web` in automated scripts.

## Checklist

- Title clearly describes the problem.
- Body includes steps to reproduce.
- Appropriate labels applied.
- Assigned if ownership is clear.

## References

- `gh issue --help`
- `gh issue create --help`

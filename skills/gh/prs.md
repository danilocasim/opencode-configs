# Pull Requests

Create, view, checkout, and merge pull requests using `gh pr`.

## When to load

- You are creating a PR from a branch.
- You need to view PR details, checks, or reviews.
- You want to checkout or merge a PR locally.

## When NOT to load

- You are only viewing issues (use `issues.md`).
- You are checking CI status (use `actions.md`).

## Core commands

```bash
gh pr list                    # List open PRs
gh pr view <number>           # View PR details
gh pr view <number> --comments # View PR conversation comments
gh pr view <number> --web     # Open in browser
gh pr checkout <number>       # Checkout PR locally
gh pr create                  # Create PR from current branch
gh pr merge <number>          # Merge a PR
gh pr close <number>          # Close a PR
gh pr ready <number>          # Mark as ready for review
gh pr review <number>         # Add a review
gh pr comment <number>        # Add a PR conversation comment
```

## Common patterns

### Create a PR

```bash
gh pr create --title "Add OAuth device flow" --body "Implements RFC 8628"
```

With body from heredoc (recommended for longer descriptions):

```bash
gh pr create --title "Add OAuth device flow" --body "$(cat <<'EOF'
## Summary
- Implements RFC 8628 device authorization grant
- Adds polling mechanism for device token
- Includes rate limiting for token requests

## Test plan
- Run: `npm test`
- Manual: Test device flow at `/auth/device`
EOF
)"
```

### View PR details

```bash
gh pr view 123
gh pr view 123 --json title,body,state,mergeable
gh pr view 123 --web
```

### Fetch PR comments

PR conversation comments (easy, readable):

```bash
gh pr view 123 --comments
```

PR comments as JSON (for scripting):

```bash
gh pr view 123 --json comments --jq '.comments[] | {author: .author.login, createdAt: .createdAt, body: .body}'
```

If you need review/diff comments (inline comments on changed lines), use the API:

```bash
gh api repos/{owner}/{repo}/pulls/123/comments --jq '.[] | {id: .id, user: .user.login, path: .path, line: .line, body: .body}'
```

### Checkout and test a PR

```bash
gh pr checkout 123
npm test
gh pr review 123 --approve -b "LGTM, tests pass"
```

### Create comments on a PR (including other repos)

Leave a PR conversation comment:

```bash
gh pr comment 123 -b "Thanks! I pushed a fix in 1a2b3c4."
```

Comment on a PR in another repo (use `-R` or a URL):

```bash
gh pr comment 123 -R owner/repo -b "I can reproduce this on macOS; details in the logs above."
gh pr comment https://github.com/owner/repo/pull/123 -b "Looks good overall; I left one question about error handling."
```

Leave a review that is a single comment (does not approve/request-changes):

```bash
gh pr review 123 --comment -b "I reviewed the approach; a couple of nits, otherwise looks good."
```

### Reply to PR review (diff) comments

GitHub only supports true threaded replies for review/diff comments (not general PR conversation comments).

1. List review comments and grab the comment `id`:

```bash
gh api repos/{owner}/{repo}/pulls/123/comments --jq '.[] | {id: .id, user: .user.login, path: .path, line: .line, body: .body}'
```

2. Reply to a specific review comment:

```bash
gh api -X POST repos/{owner}/{repo}/pulls/123/comments/123456789/replies \
  -f body='Good catch - updated to handle nil here.'
```

Alternative (also works):

```bash
gh api -X POST repos/{owner}/{repo}/pulls/123/comments \
  -f body='Good catch - updated to handle nil here.' \
  -F in_reply_to=123456789
```

### Merge a PR

```bash
gh pr merge 123 --squash --delete-branch
gh pr merge 123 --merge
gh pr merge 123 --rebase
```

### Check PR status

```bash
gh pr checks 123              # View CI status
gh pr diff 123                # View diff
gh pr edit 123 --add-label "ready"  # Add label
```

## Minimal examples

Create PR with full context:

```bash
gh pr create --title "fix(auth): reject expired refresh tokens" --body "$(cat <<'EOF'
Why:
- Expired tokens were being accepted, causing silent auth failures.

What:
- Add expiry check in token validation.
- Add regression tests.

How to test:
- Run: `npm test`
- Manual: Use expired token, verify 401 response

Risks:
- Low; validation only tightened.
EOF
)"
```

Fetch comments and respond:

```bash
gh pr view 123 --comments
gh pr comment 123 -b "Addressed this in 1a2b3c4; could you take another look?"
```

## Anti-patterns

- Creating PRs without `--title` and `--body` (opens editor, breaks automation).
- Using `--web` in scripts (blocks terminal).
- Merging without checking CI status (`gh pr checks`).
- Replying with `gh api` when a plain `gh pr comment` is sufficient.

## Checklist

- PR has descriptive title and body.
- CI passes before merging.
- Use `--squash --delete-branch` for clean history (if repo convention).
- Review status checked before merge.
- Use `gh pr view --comments` to pull context before replying.

## References

- `gh pr --help`
- `gh pr create --help`

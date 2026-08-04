# Recipe: Address PR Comments (Your PR)

Address feedback on your PR systematically: collect all comment types, decide what to implement vs reply-only, make focused commits, then reply in the right place (timeline vs threaded review comments).

## Goal

Close the loop on every reviewer point with either a code change + commit reference, or a clear rationale reply.

## Load

- `SKILL.md`
- `prs.md`
- `api.md` (for threaded replies to inline diff comments)
- `../git/SKILL.md`
- Stack-specific skill based on changed files (rails/nextjs/python/etc.)
- `../testing/SKILL.md` (if behavior changes)

## Preconditions

- You have a PR number or URL.
- You can push to the PR branch.

## Files to touch

- Your normal code files (+ tests if behavior changes).

## Default behaviors

- Treat PR feedback as a checklist: nothing gets dropped silently.
- Prefer small, reviewable commits per theme.
- Reply in the correct channel:
  - PR timeline comments: `gh pr comment` (unthreaded, good for general discussion)
  - Inline diff review comments: `gh api .../pulls/<number>/comments/<comment_id>/replies` (threaded)

## Steps

1. Checkout the PR branch:

```bash
gh pr checkout <number>
git status
```

2. Fetch PR feedback (both comment types):

PR timeline conversation comments:

```bash
gh pr view <number> --comments
```

Inline review/diff comments:

```bash
gh api repos/{owner}/{repo}/pulls/<number>/comments \
  --jq '.[] | {id: .id, user: .user.login, path: .path, line: .line, body: .body, in_reply_to_id: .in_reply_to_id}'
```

3. Make an action plan per comment:

```text
Comment <id>:
- Action: IMPLEMENT | REPLY | SKIP
- Notes: what you'll change / what you'll say
```

4. Implement the agreed changes (load stack + testing as needed).

5. Commit and push (keep commits focused):

```bash
git status
git diff
git add -A
git commit -m "fix(<scope>): address PR feedback on <topic>"
git push
```

6. Reply to each thread with context.

Reply to an inline diff comment (threaded):

```bash
gh api -X POST repos/{owner}/{repo}/pulls/<number>/comments/<comment_id>/replies \
  -f body='Fixed in <sha>: <what changed>. Tests: <what you ran>.'
```

Reply to a PR timeline comment (general discussion):

```bash
gh pr comment <number> -b "$(cat <<'EOF'
Addressed:
- <point 1> (commit <sha>)
- <point 2> (commit <sha>)

Notes:
- <any rationale for skip/out-of-scope>
EOF
)"
```

7. Verify checks:

```bash
gh pr checks <number>
```

## Anti-patterns

- Replying to inline review comments via `gh pr comment` (loses thread context).
- Pushing a giant refactor while addressing narrow feedback.
- Marking things "done" without pointing to a commit SHA or specific behavior change.

## Test plan

- Run the repo test command(s) for any behavior change.
- Confirm threaded replies appear under the correct inline comments.
- Confirm `gh pr checks <number>` is green.

## Commit message

- `fix(<scope>): address PR feedback on <topic>`

## PR body (copy-ready)

```text
Updates:
- <change> (commit <sha>)
- <change> (commit <sha>)

Notes:
- <why you skipped/out-of-scope>
```

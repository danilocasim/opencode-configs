# Recipe: Review Others' PRs

Review someone else's PR: gather context, read the diff, draft a small set of actionable comments, then post them as a proper review.

## Goal

Leave feedback that is easy to act on: a concise review summary + (optionally) a few threaded inline diff comments.

## Load

- `SKILL.md`
- `prs.md`
- `api.md` (only if you need threaded inline diff comments or replies)
- `../git/SKILL.md`
- `../code-reviewer/SKILL.md` (optional)

## Preconditions

- You have a PR number or URL.
- `gh auth status` shows you are authenticated.
- You have permission to review/comment in the target repo.

## Files to touch

- None (review-only).

## Default behaviors

- Read PR context and diff before commenting.
- Prefer 1 coherent review with 0-5 comments over many small comments.
- Prefer `gh pr review` for the review summary.
- Use the REST API only for threaded inline diff comments (the `gh` CLI is limited here).
- Do not post anything to GitHub unless the user explicitly asked; otherwise draft the commands and review text.

## Steps

1. Collect PR context (includes head SHA for line comments):

```bash
gh pr view <number> --json number,url,title,author,baseRefName,headRefName,headRepository,headRefOid
```

2. Inspect the diff:

```bash
gh pr diff <number>
```

3. Draft your review summary (what you reviewed, main risks, what to change).

4. Optional: leave threaded inline diff comments.

First, list existing review/diff comments to avoid duplicates:

```bash
gh api repos/{owner}/{repo}/pulls/<number>/comments \
  --jq '.[] | {id: .id, user: .user.login, path: .path, line: .line, body: .body, in_reply_to_id: .in_reply_to_id}'
```

Create a new inline diff comment (single-line):

```bash
gh api -X POST repos/{owner}/{repo}/pulls/<number>/comments \
  -f body='Consider extracting this validation into a helper to keep the handler readable.' \
  -f commit_id='<headRefOid>' \
  -f path='src/foo.ts' \
  -f line=42 \
  -f side='RIGHT'
```

Create a multi-line inline diff comment:

```bash
gh api -X POST repos/{owner}/{repo}/pulls/<number>/comments \
  -f body='This block is doing two things (parsing + validation). Can we split it for testability?' \
  -f commit_id='<headRefOid>' \
  -f path='src/foo.ts' \
  -f start_line=40 \
  -f line=55 \
  -f start_side='RIGHT' \
  -f side='RIGHT'
```

Reply to an existing top-level review/diff comment (threaded reply):

```bash
gh api -X POST repos/{owner}/{repo}/pulls/<number>/comments/<comment_id>/replies \
  -f body='Good catch - I think we can tighten this by validating earlier. Will you be OK with that approach?'
```

5. Post the review summary.

Comment-only review:

```bash
gh pr review <number> --comment -b "$(cat <<'EOF'
## Review summary

- Readability: overall good; a couple spots could be decomposed.
- Correctness: please confirm error handling for <case>.

## Suggestions
1. <actionable change>
2. <actionable change>
EOF
)"
```

Approve / request changes (only if you mean it):

```bash
gh pr review <number> --approve -b "LGTM - nice cleanup."
gh pr review <number> --request-changes -b "Needs changes: please address the inline comments (esp. error handling + tests)."
```

## Anti-patterns

- Using `gh pr comment` for code feedback (not threaded; hard to follow).
- Leaving comments against a stale `commit_id` (line comments can appear as outdated).
- Replying to a reply (GitHub only supports replies to top-level review comments).
- Approving while also leaving a blocking concern.

## Test plan

- Verify the PR's `headRefOid` matches what you're commenting on.
- Confirm any inline comments render on the intended diff lines (not as outdated).

## Commit message

- Not applicable.

## PR body (copy-ready)

- Not applicable.

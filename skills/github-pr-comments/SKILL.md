---
name: github-pr-comments
description: Use when replying to, resolving, or auditing GitHub pull request review comments programmatically with the gh CLI and GitHub REST or GraphQL APIs.
---

# GitHub PR Comments

> Handle GitHub PR review comments programmatically using `gh` CLI and REST API.
> Focuses on replying to outdated comments and understanding API limitations.

## When to load

- You need to programmatically respond to PR review comments.
- You're building automation for PR review workflows.
- You need to batch-reply to multiple review comments.
- The PR has outdated comments that you need to address.

## When NOT to load

- You have access to the GitHub web UI and can resolve manually.
- You need to resolve conversations (requires GraphQL or browser automation).
- You're working with issue comments (not code review comments).

## Quick reference

| Action               | Method                                                            | Works on Outdated? | Limitations                           |
| -------------------- | ----------------------------------------------------------------- | ------------------ | ------------------------------------- |
| Reply to comment     | `POST /repos/{owner}/{repo}/pulls/{number}/comments/{id}/replies` | ✅ Yes             | Top-level comments only               |
| View all comments    | `GET /repos/{owner}/{repo}/pulls/{number}/comments`               | ✅ Yes             | Shows all comments including outdated |
| Update comment body  | `PATCH /repos/{owner}/{repo}/pulls/comments/{id}`                 | ❌ No              | Only body, not resolution             |
| Resolve conversation | GraphQL `resolveReviewThread`                                     | ✅ Yes             | REST API cannot resolve               |
| Submit PR review     | `gh pr review {number} --comment`                                 | N/A                | Creates new review, not reply         |

## Key concepts

### Outdated comments

Comments become "outdated" when:

- The referenced commit is no longer the PR's HEAD
- Code lines referenced in the comment have changed
- The PR has been rebased or force-pushed

**Important**: Outdated comments can still be replied to via API. The reply appears in the same thread on GitHub's UI.

### Conversation threads

- Each review comment starts a conversation thread
- Replies chain together via `in_reply_to_id`
- **Threads can only be resolved via GraphQL API or GitHub web UI**
- REST API PATCH endpoint does NOT support `resolved` key (returns 422)

## Minimal examples

### Example 1: Reply to single outdated comment

```bash
comment_id=2821119600
pull_number=2956
response="Fixed. Removed the no-op line in commit abc123."

gh api repos/beamtree/picq-web/pulls/${pull_number}/comments/${comment_id}/replies \
  -X POST \
  --input - <<< "{\"body\": \"${response}\"}"
```

**Output**: Creates reply with `in_reply_to_id` linking to original comment.

### Example 2: Batch reply to all comments

```bash
# Get all comment IDs
comment_ids=$(gh api repos/beamtree/picq-web/pulls/2956/comments \
  --jq '.[] | select(.in_reply_to_id == null) | .id' | tr '\n' ' ')

# Define responses
responses=(
  "Fixed issue 1 in commit abc123."
  "Fixed issue 2 by refactoring method."
  "Fixed issue 3 with validation."
)

# Iterate and reply
i=0
for id in $comment_ids; do
  gh api repos/beamtree/picq-web/pulls/2956/comments/${id}/replies \
    -X POST \
    --input - <<< "{\"body\": \"${responses[$i]}\"}"
  ((i++))
done
```

### Example 3: What does NOT work (resolution)

```bash
# ❌ This will fail with 422
gh api repos/beamtree/picq-web/pulls/comments/2821119600 \
  -X PATCH \
  --input - <<< '{"resolved": true}'

# Error: "resolved" is not a permitted key
# REST API PATCH only supports updating body, NOT resolution status
```

## Anti-patterns

### Don't: Try to resolve via REST API PATCH

The PATCH endpoint only supports updating the comment body, not resolution status:

```json
{
  "message": "Invalid request.",
  "errors": [
    {
      "resource": "PullRequestReviewComment",
      "field": "resolved",
      "code": "unpermitted_key"
    }
  ]
}
```

### Don't: Assume outdated comments can't be replied to

Outdated comments CAN be replied to via `/replies` endpoint. GitHub preserves the conversation thread.

### Don't: Mix up comments vs review threads

- **Pull request comments**: `/repos/{owner}/{repo}/pulls/{number}/comments` (code review comments)
- **Issue comments**: `/repos/{owner}/{repo}/issues/{number}/comments` (general discussion)
- **Review summaries**: `/repos/{owner}/{repo}/pulls/{number}/reviews` (overall PR review)

## Decision tree

```
Need to reply to PR review comment?
├── Can access web UI?
│   └── Use GitHub web interface
└── Need automation?
    ├── Just reply?
    │   └── Use gh api POST /replies
    └── Need to resolve?
        ├── Have GraphQL access?
        │   └── Use GraphQL resolveReviewThread
        └── Otherwise?
            └── Use browser automation or ask reviewers
```

## Skill routing

| Task                     | Document                |
| ------------------------ | ----------------------- |
| Reply to single comment  | Minimal examples above  |
| Batch reply workflow     | `recipes.md` - Recipe 1 |
| Check comment status     | `recipes.md` - Recipe 2 |
| Handle outdated comments | `recipes.md` - Recipe 3 |
| Resolve conversations    | `recipes.md` - Recipe 4 |
| Format responses         | `recipes.md` - Recipe 6 |
| Common errors            | `troubleshooting.md`    |

## References

- GitHub REST API: https://docs.github.com/en/rest/pulls/comments
- GraphQL API: https://docs.github.com/en/graphql/reference/mutations#resolvereviewthread
- gh CLI: https://cli.github.com/manual/gh_api

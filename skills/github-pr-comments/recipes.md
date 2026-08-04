# Recipes: GitHub PR Comments

> Essential recipes for handling GitHub PR review comments programmatically.

## Recipe 1: Reply to All Review Comments

Complete workflow for batch-replying to PR comments:

```bash
#!/bin/bash
# respond-to-review.sh <pr_number>

PR_NUMBER=$1
REPO="beamtree/picq-web"

# Define responses (comment_id -> message)
declare -A RESPONSES=(
  ["2821119600"]="Fixed. Removed no-op line in commit 5385b1805."
  ["2821119637"]="Fixed. Replaced SQL regex with mocking."
  ["2821119657"]="Fixed. Added validation before authorization."
)

# Get and reply to each comment
for id in $(gh api repos/${REPO}/pulls/${PR_NUMBER}/comments \
  --jq '.[] | select(.in_reply_to_id == null) | .id'); do
  if [ -n "${RESPONSES[$id]}" ]; then
    gh api repos/${REPO}/pulls/${PR_NUMBER}/comments/${id}/replies \
      -X POST --input - <<< "{\"body\": \"${RESPONSES[$id]}\"}"
  fi
done

# Submit summary review
gh pr review ${PR_NUMBER} --comment --body "All comments addressed in commit 5385b1805."
```

## Recipe 2: Check Comment Status

```bash
# Check if comments are outdated (position: null = outdated)
gh api repos/beamtree/picq-web/pulls/2956/comments --jq '.[] | {
  id,
  outdated: (.position == null),
  original_line,
  body: .body[0:50]
}'

# Filter to only outdated
gh api repos/beamtree/picq-web/pulls/2956/comments \
  --jq '[.[] | select(.position == null)] | .[].id'
```

## Recipe 3: Handle What API Can't Do

**Problem**: REST API cannot resolve conversations (returns 422).

**Solutions**:

**A) Browser automation (Playwright)**

```javascript
const { chromium } = require("playwright");
const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto("https://github.com/beamtree/picq-web/pull/2956");

// Click all resolve buttons
const buttons = await page.locator('button:has-text("Resolve")').all();
for (const btn of buttons) await btn.click();
```

**B) Ask reviewers**

```bash
response="Fixed in commit 5385b1805. Please resolve once verified."
gh api repos/beamtree/picq-web/pulls/2956/comments/2821119600/replies \
  -X POST --input - <<< "{\"body\": \"${response}\"}"
```

## Recipe 4: Format Responses

```bash
#!/bin/bash

generate_response() {
  local type=$1  # fixed, ack, question
  local commit=$2
  local details=$3

  case $type in
    fixed)
      [ -n "$commit" ] \
        && echo "**Fixed** in commit ${commit}. ${details}" \
        || echo "**Fixed**. ${details}" ;;
    ack)
      echo "**Acknowledged**. ${details}" ;;
    *)
      echo "$details" ;;
  esac
}

# Usage
response=$(generate_response "fixed" "5385b1805" "Removed redundant validation")
gh api repos/beamtree/picq-web/pulls/2956/comments/2821119600/replies \
  -X POST --input - <<< "{\"body\": \"${response}\"}"
```

## Recipe 5: Testing & Error Handling

```bash
# Test mode (dry run)
DRY_RUN=true
PR_NUMBER=2956
for id in $comment_ids; do
  if [ "$DRY_RUN" = true ]; then
    echo "[DRY] Would reply to $id"
  else
    gh api repos/beamtree/picq-web/pulls/${PR_NUMBER}/comments/${id}/replies \
      -X POST --input - <<< '{"body": "Fixed"}' \
      || echo "Failed: $id"
  fi
done
```

## Common Patterns

| Task              | Command                                                                                            |
| ----------------- | -------------------------------------------------------------------------------------------------- |
| Reply to comment  | `gh api repos/OWNER/REPO/pulls/NUMBER/comments/ID/replies -X POST --input - <<< '{"body": "MSG"}'` |
| View all comments | `gh api repos/OWNER/REPO/pulls/NUMBER/comments`                                                    |
| Check if outdated | `--jq 'select(.position == null)'`                                                                 |
| Test JSON         | `echo '{"body": "test"}' \| jq .`                                                                  |

## Troubleshooting Quick Fixes

| Error               | Fix                                                 |
| ------------------- | --------------------------------------------------- |
| 404                 | Include the pull number in the reply endpoint       |
| 422 with `resolved` | Can't resolve via REST API - use GraphQL or browser |
| JSON parse error    | Escape quotes: `'\"batch insert\"'` or use `jq -n`  |
| 401/403             | Run `gh auth login` or check token scopes           |
| Rate limit          | Add `sleep 1` between requests                      |

## References

- GitHub REST API: https://docs.github.com/en/rest/pulls/comments
- GitHub MCP Server: https://github.com/github/github-mcp-server
- gh CLI: https://cli.github.com/manual/gh_api

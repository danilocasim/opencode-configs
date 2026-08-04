# Troubleshooting: GitHub PR Comments

> Common errors, issues, and solutions when working with GitHub PR review comments API.

## Error: 404 Not Found

### Symptom

```
{
  "message": "Not Found",
  "documentation_url": "https://docs.github.com/rest",
  "status": "404"
}
```

### Causes

1. **Wrong comment ID** - Using issue comment ID instead of PR review comment ID
2. **Wrong repository** - Typo in repo name
3. **Wrong endpoint** - Using `/issues/comments/` instead of `/pulls/comments/`

### Solutions

```bash
# ✅ Correct endpoint for code review comments
gh api repos/OWNER/REPO/pulls/comments/2821119600

# ❌ Wrong - this is for issue comments
gh api repos/OWNER/REPO/issues/comments/2821119600

# ❌ Wrong reply endpoint - missing the pull number
gh api repos/OWNER/REPO/pulls/comments/2821119600/replies

# ✅ Correct reply endpoint
gh api repos/OWNER/REPO/pulls/2956/comments/2821119600/replies \
  -X POST --input - <<< '{"body": "Fixed"}'
```

### Verify the comment exists

```bash
# List all PR review comments
gh api repos/beamtree/picq-web/pulls/2956/comments \
  --jq '.[] | {id, body: .body[0:50]}'

# Check if your ID is in the list
```

## Error: 422 Unprocessable Entity

### Symptom

```
{
  "message": "Invalid request.",
  "documentation_url": "https://docs.github.com/rest",
  "errors": [
    {
      "resource": "PullRequestReviewComment",
      "field": "resolved",
      "code": "unpermitted_key"
    }
  ],
  "status": "422"
}
```

### Cause

Trying to resolve a conversation via REST API PATCH. The REST API doesn't support the `resolved` key.

### Solution

Use GraphQL API or browser automation to resolve conversations.

```bash
# ❌ Won't work
gh api repos/beamtree/picq-web/pulls/comments/2821119600 \
  -X PATCH \
  --input - <<< '{"resolved": true}'

# ✅ Only body updates work
gh api repos/beamtree/picq-web/pulls/comments/2821119600 \
  -X PATCH \
  --input - <<< '{"body": "Updated comment text"}'

# ✅ To resolve, use GraphQL
gh api graphql -f query='
  mutation($threadId: ID!) {
    resolveReviewThread(input: {threadId: $threadId}) {
      thread { id isResolved }
    }
  }
' -F threadId="YOUR_THREAD_ID"
```

## Error: Cannot reply to own comment

### Symptom

GitHub returns 422 or silently fails when trying to reply to a comment you authored.

### Cause

GitHub doesn't allow replying to your own comments in the same thread.

### Solution

Edit your original comment instead:

```bash
# Update your own comment
gh api repos/beamtree/picq-web/pulls/comments/2821119600 \
  -X PATCH \
  --input - <<< '{"body": "Updated: Fixed in commit 5385b1805"}'
```

## Error: Special characters in response

### Symptom

JSON parsing errors when response contains quotes or special characters.

### Example

```bash
# ❌ Will fail - nested quotes
response="Fixed. It uses \"batch insert\" for performance."
```

### Solutions

**Option 1: Escape properly**

```bash
response='Fixed. It uses \"batch insert\" for performance.'
gh api repos/beamtree/picq-web/pulls/2956/comments/2821119600/replies \
  -X POST \
  --input - <<< "{\"body\": \"${response}\"}"
```

**Option 2: Use JSON properly**

```bash
# Create JSON file
cat > /tmp/reply.json << 'EOF'
{"body": "Fixed. It uses \"batch insert\" for performance."}
EOF

gh api repos/beamtree/picq-web/pulls/2956/comments/2821119600/replies \
  -X POST \
  --input /tmp/reply.json
```

**Option 3: Use jq to escape**

```bash
response="Fixed. It uses \"batch insert\" for performance."
json=$(jq -n --arg body "$response" '{body: $body}')

gh api repos/beamtree/picq-web/pulls/2956/comments/2821119600/replies \
  -X POST \
  --input - <<< "$json"
```

## Error: Comment not visible after reply

### Symptom

Reply posted successfully (200 OK), but not visible in GitHub UI.

### Causes

1. **Reply is collapsed** - GitHub collapses replies on outdated comments
2. **Wrong thread** - Reply went to different conversation thread
3. **Caching** - GitHub UI cache hasn't updated

### Solutions

**Check if reply exists via API:**

```bash
# Get the comment and its replies
gh api repos/beamtree/picq-web/pulls/comments/2821119600 \
  --jq '{id, body, in_reply_to_id, replies: .replies}'
```

**Force refresh GitHub UI:**

- Hard refresh: `Ctrl+Shift+R` (or `Cmd+Shift+R` on Mac)
- Check "Show outdated" button on PR

**Verify reply chain:**

```bash
# Get all comments in a thread
gh api repos/beamtree/picq-web/pulls/2956/comments \
  --jq '[.[] | select(.in_reply_to_id == 2821119600)]'
```

## Error: Authentication issues

### Symptom

```
gh: Could not resolve to a Repository with the name 'beamtree/picq-web'.
```

### Causes

1. **Not authenticated** - `gh auth status` shows not logged in
2. **Wrong token scope** - Token doesn't have `repo` scope
3. **Private repo** - Don't have access to the repository

### Solutions

**Check authentication:**

```bash
gh auth status
```

**Re-authenticate:**

```bash
gh auth login
```

**Check token scopes:**

```bash
gh api user --jq '.login'
# If this works, basic auth is OK

# Test repo access
gh api repos/beamtree/picq-web \
  --jq '{name, private, permissions}'
```

**For private repos, ensure token has:**

- `repo` scope (full control of private repositories)
- `read:discussion` (for PR comments)

## Error: Rate limiting

### Symptom

```
API rate limit exceeded
```

### Solutions

**Check rate limit:**

```bash
gh api rate_limit --jq '.rate'
```

**Add delays between requests:**

```bash
#!/bin/bash

PR_NUMBER=2956
for comment_id in $comment_ids; do
  gh api repos/beamtree/picq-web/pulls/${PR_NUMBER}/comments/${comment_id}/replies \
    -X POST \
    --input - <<< '{"body": "Fixed"}'

  # Sleep to avoid rate limit
  sleep 1
done
```

**Use conditional requests (ETag):**

```bash
# Store last response headers
gh api repos/beamtree/picq-web/pulls/2956/comments -i > /tmp/headers.txt

# Extract ETag
etag=$(grep -i etag /tmp/headers.txt | awk '{print $2}')

# Use in next request
gh api repos/beamtree/picq-web/pulls/2956/comments \
  -H "If-None-Match: $etag"
```

## Error: Comment body too long

### Symptom

GitHub returns 422 when comment body exceeds 65535 characters.

### Solution

Split into multiple replies or use a summary with link to full details.

```bash
# Truncate if needed
max_length=65000
response="Your very long response..."

if [ ${#response} -gt $max_length ]; then
  response="${response:0:$max_length}... [truncated]"
fi
```

## Common jq filter errors

### Error: Invalid filter

```bash
# ❌ Wrong syntax
gh api repos/beamtree/picq-web/pulls/2956/comments \
  --jq '.[] | {id, body[0:50]}'
```

### Solution

```bash
# ✅ Correct syntax
gh api repos/beamtree/picq-web/pulls/2956/comments \
  --jq '.[] | {id, body: .body[0:50]}'
```

### Error: Null value handling

```bash
# ❌ Crashes on null
gh api repos/beamtree/picq-web/pulls/2956/comments \
  --jq '.[] | select(.in_reply_to_id | length > 0)'
```

### Solution

```bash
# ✅ Handle null properly
gh api repos/beamtree/picq-web/pulls/2956/comments \
  --jq '.[] | select(.in_reply_to_id // "" | length > 0)'
```

## Debugging tips

### Enable verbose mode

```bash
# Show HTTP headers and full response
gh api repos/beamtree/picq-web/pulls/2956/comments -i
```

### Save responses for inspection

```bash
# Save to file
gh api repos/beamtree/picq-web/pulls/2956/comments > /tmp/comments.json

# Inspect with jq
cat /tmp/comments.json | jq '.[] | {id, body, in_reply_to_id}'
```

### Test JSON payload before sending

```bash
# Create test payload
payload='{"body": "Test response"}'

# Validate
if echo "$payload" | jq . > /dev/null 2>&1; then
  echo "Valid JSON"
else
  echo "Invalid JSON"
fi
```

### Check API status

```bash
# GitHub API status
gh api https://www.githubstatus.com/api/v2/status.json \
  --jq '.status.indicator'
```

## Quick fixes

| Error               | Quick Fix                                                   |
| ------------------- | ----------------------------------------------------------- |
| 404                 | Check you're using `/pulls/comments` not `/issues/comments` |
| 422 with `resolved` | Use GraphQL or browser automation to resolve                |
| JSON parse error    | Use `jq -n` to build JSON or escape quotes properly         |
| 401/403             | Run `gh auth login` or check token scopes                   |
| Rate limit          | Add `sleep 1` between requests                              |
| Comment not visible | Check "Show outdated" button, hard refresh page             |

## References

- GitHub REST API errors: https://docs.github.com/en/rest/overview/troubleshooting
- Rate limiting: https://docs.github.com/en/rest/overview/rate-limits
- API status: https://www.githubstatus.com/
- jq documentation: https://stedolan.github.io/jq/manual/

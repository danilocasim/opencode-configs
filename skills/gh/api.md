# GitHub API

Make authenticated GitHub API requests using `gh api`.

## When to load

- You need to query GitHub's REST or GraphQL API.
- You want to access data not exposed by other `gh` commands.
- You are building automation scripts with GitHub data.

## When NOT to load

- The operation is covered by a dedicated command (use `prs.md`, `issues.md`, etc.).
- You are just viewing basic repo info (use `repos.md`).

## Core commands

```bash
gh api <endpoint>                    # GET request
gh api -X POST <endpoint>            # POST request
gh api -X PUT <endpoint>             # PUT request
gh api -X DELETE <endpoint>          # DELETE request
gh api --paginate <endpoint>         # Paginate results
gh api -f field=value <endpoint>     # Form field for POST
gh api -F field=@file <endpoint>     # Upload file
gh graphql -f query='...'            # GraphQL query
```

## Common patterns

### GET requests

```bash
gh api repos/owner/repo
gh api repos/owner/repo/issues
gh api repos/owner/repo/pulls/123
gh api user
gh api user/repos --paginate
```

### Filter with jq

```bash
gh api repos/owner/repo/issues --jq '.[].title'
gh api repos/owner/repo/contributors --jq 'length'
gh api user --jq '.login'
```

### POST requests

```bash
gh api -X POST repos/owner/repo/issues \
  -f title="Bug report" \
  -f body="Description of the bug"
```

### GraphQL queries

```bash
gh graphql -f query='
  query($owner: String!, $repo: String!) {
    repository(owner: $owner, name: $repo) {
      issues(first: 10) {
        nodes { title number }
      }
    }
  }' -f owner=facebook -f repo=react
```

### Paginate through results

```bash
gh api --paginate repos/owner/repo/stargazers --jq '.[].login'
```

### Handle rate limits

```bash
gh api rate_limit
```

## Minimal examples

Get open PR count:

```bash
gh api repos/owner/repo/pulls --jq 'length'
```

List files in a PR:

```bash
gh api repos/owner/repo/pulls/123/files --jq '.[].filename'
```

Get user's starred repos:

```bash
gh api user/starred --paginate --jq '.[].full_name'
```

Create a comment on an issue:

```bash
gh api -X POST repos/owner/repo/issues/42/comments -f body="Thanks for reporting!"
```

Fetch PR conversation comments (PRs are issues):

```bash
gh api repos/owner/repo/issues/123/comments --jq '.[].body'
```

Fetch PR review/diff comments (inline comments on changed lines):

```bash
gh api repos/owner/repo/pulls/123/comments --jq '.[] | {id: .id, path: .path, line: .line, body: .body}'
```

Reply to a specific PR review/diff comment (threaded reply):

```bash
gh api -X POST repos/owner/repo/pulls/comments/123456789/replies \
  -f body='Done - updated this block to be deterministic.'
```

## Anti-patterns

- Using `gh api` when a dedicated command exists (harder to read).
- Not using `--paginate` for large result sets.
- Ignoring rate limits in loops.
- Hardcoding tokens (use `gh auth`).

## Checklist

- Use dedicated commands when available (`gh pr`, `gh issue`).
- Add `--paginate` for list endpoints.
- Use `--jq` for filtering over `--json` + pipe.
- Check `rate_limit` before bulk operations.

## References

- `gh api --help`
- `gh graphql --help`
- GitHub REST API: https://docs.github.com/rest
- GitHub GraphQL API: https://docs.github.com/graphql

# Repositories

Create, fork, clone, and view repository information using `gh repo`.

## When to load

- You are creating a new repository.
- You need to fork or clone a repo.
- You want to view repo metadata (description, visibility, etc.).

## When NOT to load

- You are working with PRs or issues (use `prs.md` or `issues.md`).
- You are viewing CI runs (use `actions.md`).

## Core commands

```bash
gh repo list                         # List your repos
gh repo view <repo>                  # View repo details
gh repo view <repo> --web            # Open in browser
gh repo create <name>                # Create new repo
gh repo fork <repo>                  # Fork a repo
gh repo clone <repo>                 # Clone a repo
gh repo delete <repo>                # Delete a repo
gh repo edit <repo>                  # Edit repo settings
gh repo rename <repo>                # Rename a repo
```

## Common patterns

### View repo info

```bash
gh repo view
gh repo view owner/repo
gh repo view --json name,description,visibility,url
gh repo view --web
```

### Create a new repository

```bash
gh repo create my-project
gh repo create my-project --public
gh repo create my-project --private
gh repo create my-project --description "My new project"
gh repo create my-project --clone
gh repo create my-project --template owner/template-repo
```

### Fork and clone

```bash
gh repo fork owner/repo              # Fork and add remote
gh repo fork owner/repo --clone      # Fork and clone
gh repo clone owner/repo             # Clone repo
gh repo clone owner/repo my-dir      # Clone into specific dir
```

### List repositories

```bash
gh repo list                         # Your repos
gh repo list owner                   # Org/user repos
gh repo list --limit 50
gh repo list --json name,url --jq '.[] | "\(.name): \(.url)"'
```

### Edit repo settings

```bash
gh repo edit --description "New description"
gh repo edit --homepage "https://example.com"
gh repo edit --add-topic "python" --add-topic "api"
gh repo edit --enable-issues=false
gh repo edit --default-branch main
```

## Minimal examples

Create and clone private repo:

```bash
gh repo create my-api --private --clone --description "REST API for my app"
```

Fork, clone, and push:

```bash
gh repo fork owner/project --clone --remote=true
cd project
git checkout -b feature/my-change
```

View repo metadata as JSON:

```bash
gh repo view --json name,owner,description,visibility,defaultBranchRef
```

## Anti-patterns

- Creating repos without `--private` or `--public` (prompts interactively).
- Using `gh repo delete` without confirmation.
- Not using `--clone` when you plan to work locally immediately.

## Checklist

- Specify `--public` or `--private` when creating.
- Use `--clone` for immediate local work.
- Add `--description` for discoverability.
- Use `--json` for scripting/automation.

## References

- `gh repo --help`
- `gh repo create --help`

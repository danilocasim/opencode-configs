---
name: gh
description: GitHub CLI operations for PRs, issues, repos, and Actions
---

# gh

GitHub CLI operations for PRs, issues, repos, and Actions.

## When to load

- You are creating, viewing, or merging pull requests.
- You are managing issues or viewing issue details.
- You need to interact with GitHub Actions (runs, workflows, logs).
- You are creating/forking repos or viewing repo info.
- You need to make authenticated GitHub API requests.

## When NOT to load

- You are doing git operations (commit, branch, merge) locally (use `git` skill).
- You are writing code in a specific stack (load the stack skill).

## Routing table

| Task                              | Load                            |
| --------------------------------- | ------------------------------- |
| Create/view/merge/checkout PRs    | `prs.md`                        |
| Create/view/close issues          | `issues.md`                     |
| View workflow runs, download logs | `actions.md`                    |
| Create/fork repos, view repo info | `repos.md`                      |
| Make authenticated API calls      | `api.md`                        |
| Create a PR with a canonical body | `recipe-create-pr.md`           |
| Address PR feedback (your PR)     | `recipe-address-pr-comments.md` |
| Review and comment on others' PRs | `recipe-review-others-pr.md`    |

## Typical load combos

- Creating a PR: `SKILL.md` + `prs.md` + `recipe-create-pr.md`
- Debugging CI failure: `SKILL.md` + `actions.md`
- Triage session: `SKILL.md` + `issues.md` + `prs.md`
- Addressing PR feedback: `SKILL.md` + `prs.md` + `recipe-address-pr-comments.md`
- Reviewing others: `SKILL.md` + `prs.md` + `recipe-review-others-pr.md`

## Stop triggers

- Any operation that writes to GitHub (create PR, comment, merge, close) -> only run if the user asked; otherwise prepare commands and ask.
- PR introduces security concerns -> load `../security/SKILL.md`
- PR touches database migrations -> load `../database/SKILL.md`
- PR changes API contracts -> load `../api/SKILL.md`

## Related skills

- `git` - Local git operations, commit hygiene
- `devops` - CI/CD workflows, deployment

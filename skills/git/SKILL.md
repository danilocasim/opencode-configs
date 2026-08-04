---
name: git
description: Git workflow conventions, commit hygiene, and PR practices
---

# Git Skill Tree (Routing-First)

Consistency in git commits and PRs reduces review time, improves debugging, and makes cross-project automation (release notes, backports) reliable.

## When to load

- You are about to commit and want consistent messages and commit boundaries.
- You are preparing a branch/PR and want a portable template.
- You need safe defaults that work across most repos.

## When NOT to load

- You are debugging code behavior (load the stack skill instead).
- You need repository-specific rules that conflict with these defaults (follow the repo).

## Quick routing

| If you need to...                                | Load                     | You'll get                                    |
| ------------------------------------------------ | ------------------------ | --------------------------------------------- |
| Write better commit messages; split commits      | `commits.md`             | message rules, examples, splitting heuristics |
| Stage cleanly; avoid noise; prevent secrets      | `staging-and-hygiene.md` | staging patterns, exclusions, secret safety   |
| Name branches; craft PR titles/bodies            | `branching-and-prs.md`   | portable branch + PR conventions              |
| Fix mistakes; revert/backport; resolve conflicts | `troubleshooting.md`     | safe recovery patterns and commands           |

## Default policy (portable)

- One intent per commit.
- Commit messages explain what + why (not how).
- Stage intentionally; review `git diff --staged` before committing.
- Never commit secrets; assume history is durable.
- Prefer `revert` over history-rewrites once shared/pushed.

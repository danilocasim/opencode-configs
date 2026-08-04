# Troubleshooting (Revert, Backport, Conflicts)

Safe recovery patterns when commits go wrong.

## When to load

- You need to revert a bad change safely.
- You need to backport via cherry-pick.
- You are resolving merge conflicts.
- You suspect a secret was committed.

## When NOT to load

- You want better commit messages/splitting (`commits.md`).
- You need staging discipline and secret-prevention habits (`staging-and-hygiene.md`).
- You need branch/PR conventions (`branching-and-prs.md`).

## Core rules

- If a commit is pushed/shared: prefer `git revert` over history rewrites.
- Keep a recovery point before risky operations (backup branch).
- Resolve conflicts by understanding intent, not by blanket "ours/theirs".
- Secrets: stop, don't push, rotate/revoke ASAP.

## Patterns

Revert (safe for shared history):

- `git revert <sha>`

## Minimal examples

Revert a pushed bad deploy safely:

```bash
git revert <sha>
git push
```

Backport a fix to a release branch:

```bash
git switch release/1.2
git cherry-pick <sha>
git push
```

Cherry-pick (backport):

- `git cherry-pick <sha>`

Conflict resolution loop:

- `git status`
- fix conflicted files
- `git add <file>`
- continue merge/rebase (depending on operation)

Backup branch before risky operations:

- `git branch backup/<short-name>`

Secret committed:

- If not pushed: remove it from the commit(s) and rotate anyway.
- If pushed: treat as incident; rotate/revoke immediately and follow team history-rewrite policy.

## Anti-patterns

- Force-pushing to shared branches without coordination.
- Using destructive commands as the first move (easy to lose work).
- Cherry-picking without checking for prerequisite commits.
- Solving conflicts by blanket selecting one side.

## Checklist

- You know whether the branch is shared.
- For shared history: revert instead of rewriting.
- After any recovery: run tests and sanity-check behavior.
- For secrets: rotate/revoke first, then clean history.

## References

- `man git-revert`, `man git-cherry-pick`, `man git-merge`

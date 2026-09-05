---
name: implement-spec
description: "Implement a specification in code."
disable-model-invocation: true
---

You have been provided a spec. This spec should have tickets associated with it, describing how to implement the spec.

The goal is verified implementation of the spec within the assigned scope. A PR is an optional delivery action, not implicit authorization.

The tickets are not a list of steps. They are a **task graph** with blocking relationships between them. This means there is always a **frontier** of tickets which are ready to be grabbed.

Implement directly by default in the existing assigned branch/worktree. Preserve unrelated dirty work. Do not create branches/worktrees merely because this skill was loaded.

Commit, push, PR creation/update, integration, and cleanup each require explicit user authorization for the action and target. If parallel ticket worktrees are requested, `skills/parallel-ticket-worktrees/SKILL.md` and its workflow are the existing lifecycle authority; do not create a competing merger role.

Optional workers require the parent's approval, disjoint ownership, and available configured task permissions/depth. Workers return evidence; the parent owns any authorized integration. Use context pointers to specs, tickets, and source rather than duplicating context. A no-delegation assignment stays direct.

## Steps

1. Read the spec and tickets. Read enough to understand the task graph.

2. Inspect relevant code and tests directly. Resolve blocking requirements before editing; avoid unrelated exploration.

3. Confirm ownership, branch/worktree, and acceptance criteria. Create a branch or draft PR only if explicitly requested and authorized. Only associate closing issues when the delivery actually completes them.

4. Implement ready tickets in dependency order with focused red-green-refactor tests. Use approved workers only when independent packages justify them.

5. Review each completed package's diff and test evidence. Any integration is performed by the parent under the authorized worktree workflow, never by a merger subagent.

6. Re-evaluate the frontier and continue with newly ready tickets without expanding scope or delegation authority.

7. Review the branch and dirty WIP directly using `code-review`; fix confirmed in-scope regressions and run the relevant broader verification.

8. Report completed and blocked acceptance criteria, changed files, and exact validation results. Mark an existing PR ready only if that update is authorized and verification supports it.

9. Clean up only task-owned resources explicitly authorized for removal and proven safe under the worktree workflow. Otherwise report retained worktrees and uncommitted changes.

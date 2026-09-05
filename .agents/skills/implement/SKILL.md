---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

Use the `testing` skill's red-green-refactor loop where feasible, at agreed or established repository seams. The `tdd` skill supplies additional seam guidance without requiring repeat approval.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, review the scoped changes directly using the `code-review` skill, including staged, unstaged, and relevant untracked files.

Preserve the current branch/worktree and unrelated dirty work. Implementation is not Git authorization: commit, push, PR creation/update, integration, or cleanup only with explicit user authorization for that action and target. Otherwise leave verified changes uncommitted and report them. For explicitly requested ticket worktree operations, use `skills/parallel-ticket-worktrees/SKILL.md` as the lifecycle authority. Do not delegate unless the parent explicitly permits it and configured permissions/depth allow it.

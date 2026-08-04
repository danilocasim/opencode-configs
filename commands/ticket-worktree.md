---
description: Orchestrate safe, isolated Git worktrees for parallel ticket work
agent: orchestrator
---

Load the `parallel-ticket-worktrees` skill first, then use its `workflow.md`
as the lifecycle authority. Route the request through the current primary
`orchestrator`; do not duplicate or replace the skill's workflow here.

Request:

```text
$ARGUMENTS
```

Authorize only actions explicitly named in the request. Treat commits,
integration, worktree removal, and branch cleanup as authorized only when the
user names that action and its source or target resource.

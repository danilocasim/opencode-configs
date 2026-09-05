---
description: Fetch a Plane ticket and its related work, create a scoped Git branch, and prepare an implementation plan
agent: orchestrator
---

Create a branch-backed implementation plan for this Plane ticket:

```text
$ARGUMENTS
```

Expected invocation: `/ticket-plan <ticket-id> [additional planning context]`.

Work in this order:

1. Validate that `$1` is a Plane ticket identifier. If it is missing or
   ambiguous, ask for it and make no Git changes.
2. Use an already-configured Plane integration (for example, a Plane MCP tool
   or project CLI) to retrieve the ticket's complete details. Also retrieve and
   fully paginate its directly related tickets: parent, children, blockers,
   blocked-by tickets, duplicates, and explicit issue links or references.
   Do not substitute similarly named tickets or attempt to enumerate unrelated
   workspace tickets. If Plane access is unavailable or the ticket cannot be
   found, report the concrete blocker and stop before changing Git state.
3. Summarize the ticket context, clearly distinguishing confirmed requirements,
   related-ticket dependencies, and assumptions or missing product decisions.
4. Run a Git preflight in the current repository: identify the repository root,
   current branch, a valid base branch, and working-tree status. Preserve all
   existing work. If the working tree is dirty, the base branch is unclear, or
   a target branch already exists elsewhere, stop and ask for a safe choice;
   never stash, reset, clean, overwrite, or reuse a branch implicitly.
5. Derive a concise branch name from the ticket identifier and title using the
   repository's naming convention; otherwise use
   `ticket/<normalized-ticket-id>-<short-slug>`. Show the proposed name, then
   create and switch to it from the validated base branch. If that exact branch
   is already checked out, keep it and report that no branch was created.
6. Run the planning stage with the same output contract as `/plan`, grounded in
   the retrieved Plane context and targeted repository inspection. Include:
   - goal and measurable success criteria;
   - the affected code and test areas, with the technical approach;
   - ordered implementation steps, each small and actionable;
   - focused validation for each behavior change;
   - risks, dependencies, and mitigations; and
   - open questions that block or materially change implementation.

This command only retrieves context, creates the approved local branch, and
plans the work. Do not edit product files, commit, push, open a pull request,
or change Plane ticket state.

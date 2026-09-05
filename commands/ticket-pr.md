---
description: Create a ticket-linked GitHub PR and post its delivery summary to the Plane ticket
agent: orchestrator
---

Create and log a pull request for this Plane ticket:

```text
$ARGUMENTS
```

Expected invocation: `/ticket-pr <ticket-id> [module name]`.

Work in this order:

1. Validate that `$1` is a Plane ticket identifier. Use an already-configured
   Plane integration to retrieve the ticket's exact identifier, title, and
   canonical URL. If Plane access is unavailable or the ticket is not found,
   report the blocker and stop before creating a PR or changing Plane.
2. Resolve the module name from the optional argument, the ticket's confirmed
   component, or the affected repository module. If it remains ambiguous, ask
   one focused question before creating the PR.
3. Run the `/pr` workflow for the current branch. Follow `commands/pr.md` as
   its source of truth: inspect the branch and recent commits, use the first
   applicable PR template (including `.github/PULL_REQUEST_TEMPLATE.md`), push
   the branch, and create the PR with `gh pr create`. Do not create an empty or
   duplicate PR. Capture its canonical URL.
4. Only after the PR exists, compose this exact Plane ticket comment without a
   code fence or extra headings:

   ```text
   <Ticket ID> | <Module Name> | <Ticket title>
   Ticket: <link>
   PR: <link>

   <2-3 sentences explaining the user outcome, the material changes, and validation or remaining risk.>
   ```

   Use the exact values retrieved from Plane and GitHub. Make the final
   paragraph factual and evidence-based; do not claim unrun checks or unknown
   behavior.

5. Before posting, check the ticket's existing comments for the same PR URL.
   If the URL is already logged, do not add a duplicate comment. Otherwise post
   the comment to the Plane ticket and report its URL or identifier.

If PR creation fails, do not log a Plane comment. If the Plane comment fails
after the PR succeeds, report the PR URL, the exact posting error, and the
rendered comment for manual posting. Do not edit product files, create commits,
or change any Plane ticket fields or state.

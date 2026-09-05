---
name: using-agent-skills
description: Choose a workflow when skill routing is unclear or overlapping guidance conflicts. Not a mandatory session-start or full-lifecycle checklist.
---

# Using Agent Skills

Load the smallest set of guidance that addresses the task's actual uncertainty
or risk. Clear bounded work can proceed from the user's acceptance criteria,
relevant source, and nearby tests without a new spec, task document, or handoff.

## Optional routes

| Need or risk                                                   | Route                                                                                               |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Unclear product intent                                         | `interview-me`; ask only blocking questions                                                         |
| Requested specification or unresolved significant requirements | `spec-driven-development`                                                                           |
| Large dependency graph needing decomposition                   | `planning-and-task-breakdown`                                                                       |
| Implementation too large for one verification cycle            | `incremental-implementation`                                                                        |
| Behavior change or bug regression                              | `testing`, then the relevant stack leaf                                                             |
| Uncertain public test boundary                                 | `tdd` seam guidance; reuse agreed seams                                                             |
| Visual design decisions                                        | `web-designer`                                                                                      |
| Frontend implementation                                        | `frontend-ui-engineering` and the relevant stack                                                    |
| Browser checks with available Playwright tools/runner          | `skills/testing/e2e-playwright.md` and, for suite setup, `skills/testing/recipes-playwright-e2e.md` |
| Chrome DevTools-specific diagnostics with that MCP available   | `browser-testing-with-devtools`                                                                     |
| Unexplained failure                                            | `debugging-and-error-recovery`                                                                      |
| Scoped branch or WIP review                                    | `code-review`; `/review` stays bounded and direct                                                   |
| High-risk claim needing adversarial verification               | `doubt-driven-development`, optional and permission-gated                                           |
| Security-sensitive boundary                                    | `security`                                                                                          |
| Measured performance problem                                   | `performance`                                                                                       |
| Explicit Git delivery/worktree request                         | `git` or `parallel-ticket-worktrees`                                                                |
| Context setup or observed retrieval problems                   | `context-engineering`                                                                               |

These routes are conditional, not a sequence to load in full. Use specialized
API, database, deployment, or documentation guidance only for the corresponding
work. Consult current official documentation when library details matter;
routine business-logic edits do not need a separate research ceremony.

## Authority and scope

- The selected session handles normal work directly, including economy sessions.
- Skills do not grant Git, PR, external-service, or delegation authorization.
  Follow the user's scope and the parent's actual tools, permissions, and depth.
- Delegate only an approved independent package when it has a clear benefit;
  a no-delegation assignment remains direct.
- Preserve unrelated work. Clarify material ambiguity, not decisions already
  agreed in the task or established by the repository.

## Completion

Use the user's acceptance criteria and the repository's actual completion
guidance, not a presumed global completion document. Review the scoped diff,
run applicable tests/checks, and report exact evidence. Distinguish passed,
failed, blocked, and intentionally deferred validation. Documentation-only work
does not require application runtime checks; unavailable browser tools do not
justify claiming visual verification. Leave Git delivery untouched unless
explicitly authorized.

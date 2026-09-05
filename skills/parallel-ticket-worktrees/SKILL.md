---
name: parallel-ticket-worktrees
description: Use when `/ticket-worktree`, parallel tickets, Git worktrees, isolated ticket branches, or safe ticket integration and cleanup are requested.
---

# Parallel Ticket Worktrees

Use isolated Git worktrees to let the primary Orchestrator coordinate safe,
disjoint ticket work without disturbing the user's base checkout.

## When to load

- A user invokes `/ticket-worktree` or requests parallel ticket implementation.
- A ticket needs an isolated branch/worktree, later integration, or safe removal.
- The Orchestrator must divide independent ticket work among workers.

## When NOT to load

- A small, single-checkout change does not benefit from branch isolation.
- The user only wants a generic Git explanation or a repository-wide branch policy.
- Parallel tickets overlap in files or design and cannot be sequenced first.

## Router

| Need                                                               | Load          |
| ------------------------------------------------------------------ | ------------- |
| Inspect, create, delegate, integrate, or clean up ticket worktrees | `workflow.md` |

## Orchestrator integration

The primary `orchestrator` owns the lifecycle: preflight, ownership plan,
worktree ledger, worker routing, review, approved integration, validation, and
cleanup. Workers never integrate their own changes or operate outside their
assigned worktree.

| Work type                                                            | Default route           |
| -------------------------------------------------------------------- | ----------------------- |
| Read-only repository map or dependency discovery                     | Repository Analyst      |
| Normal ticket implementation                                         | Implementation Engineer |
| Mechanical, isolated, objectively checked package                    | Bounded Worker          |
| Clear visual implementation or browser verification                  | Visual Engineer         |
| Ambiguous or high-impact product/design direction                    | UI/UX Analyst           |
| High-risk, security-sensitive, hard-to-reverse, or foundational work | Principal Engineer      |

Keep parallel ownership disjoint; dependency or overlap means sequence the work
instead.

## Typical modes

| Mode               | Result                                                                                                                                                |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `inspect` / `plan` | Read-only preflight, ticket decomposition, and ownership plan.                                                                                        |
| `setup-only`       | Create approved, collision-free worktrees and report their paths.                                                                                     |
| `implement`        | Set up as needed, delegate isolated implementation, and review evidence.                                                                              |
| `integrate`        | Hand off a completed ticket branch to the original checkout or integrate multiple branches into a named local test branch, only with explicit intent. |
| `cleanup`          | Inspect and remove only explicitly approved, safe task-owned resources.                                                                               |

Invocation authorizes the requested inspection, setup, and implementation work.
It does not implicitly authorize commits, merging/integration, deletion/removal,
or branch cleanup.

## Stop triggers

- The repository root, base ref, ticket identity, ownership, or requested mode
  is ambiguous.
- The default branch cannot be determined, or a proposed path/ref already
  exists.
- Tickets overlap, a worktree is dirty, or unique commits are at risk.
- Integration, commit, branch deletion, or worktree removal lacks explicit
  user intent for the named resource.
- The work exposes a security, migration, architecture, or design decision that
  exceeds the ticket; route or ask before proceeding.

## Safety rules

- Preserve dirty base-checkout changes; never absorb, reset, clean, or move
  them into ticket work.
- Create worktrees with Git, never by copying directories, and never reuse a
  path or branch without approval.
- Use no force removal, broad prune/clean/reset operation, or destructive
  branch command.
- Inspect status, diff, log, and unique commits before integration or cleanup.
- Integrate in the repository's established dependency order and validate again
  from the named local target branch in the original checkout.
- For manual testing, retain the original checkout's ignored local environment
  files; do not copy private configuration into ticket worktrees.
- A completed worktree may be removed only after its commits are reviewed and
  preserved on its branch; remove the worktree, not the branch, before checking
  that branch out in the original checkout.
- Retain and precisely report any resource that is unsafe to integrate or
  remove.

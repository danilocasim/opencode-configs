# Ticket-worktree lifecycle

## When to load

- The `/ticket-worktree` command or the router selects parallel ticket work.
- You need to inspect/plan, set up, implement, integrate, or clean up isolated
  ticket worktrees.

## When NOT to load

- The task fits safely in the current checkout and does not need isolation.
- Work packages share files or a design decision that must be resolved before
  parallel implementation.

## Core rules

1. **Choose and state the mode.** `inspect`/`plan` is read-only;
   `setup-only` creates worktrees but launches no implementer; `implement`
   sets up as needed and delegates ticket work; `integrate` and `cleanup` act
   only on named resources. Ask for a ticket ID/title, mode, or scope when it
   cannot be inferred safely.

2. **Run preflight before every creation.** From the intended base checkout:
   - verify the root with `git rev-parse --show-toplevel`;
   - capture `git status --short` and preserve every pre-existing change;
   - inspect `git worktree list --porcelain`, remotes, and refs;
   - use an explicitly supplied base only after it resolves to a commit;
     otherwise determine the repository default from the primary remote's
     `refs/remotes/<remote>/HEAD` (for example,
     `git symbolic-ref --quiet refs/remotes/origin/HEAD`); and
   - if no default is determinable, ask. Never silently assume `main`.

3. **Prove that each destination is new.** Use a stable ticket slug; by
   default place the worktree beside the repository as
   `<repo>-<ticket-slug>` and choose an intent-appropriate branch prefix.
   Before `git worktree add`, check the exact path (including an existing empty
   directory), `git worktree list --porcelain`, and local and remote refs for
   the proposed branch. A collision stops the workflow: do not reuse a path or
   branch unless the user explicitly approves that exact reuse.

4. **Create only the approved sandbox.** After preflight, use Git rather than
   a copied checkout, for example:

   ```bash
   git worktree add -b "feature/TICKET-123-short-slug" \
     "../repo-TICKET-123-short-slug" "<resolved-base-ref>"
   ```

   Record the path, branch, base commit/ref, ticket, and creator in a cleanup
   ledger. Confirm the new worktree's branch and status. In `setup-only`, do
   not delegate implementation; report `cd "<path>" && opencode` instead.

5. **Preserve ownership before parallelism.** The Orchestrator assigns a
   ticket to one worktree and gives each worker an exact mission containing:
   - worktree path and branch;
   - owned files/modules and explicit areas not to touch;
   - constraints, dependencies, and acceptance criteria;
   - exact validation commands discovered during preflight (or `none` with a
     reason, never an unspecified placeholder);
   - no commit and no push unless the user explicitly authorizes them; and
   - cleanup obligations for temporary resources.

   Route normal tickets to Implementation Engineer; narrow mechanical packages
   to Bounded Worker; clear visual work to Visual Engineer; ambiguous or
   high-impact design to UI/UX Analyst; read-only mapping to Repository
   Analyst; and high-risk work to Principal Engineer. Workers edit and run
   commands only in the assigned worktree, and never integrate their own
   changes. After coding and focused validation, each implementation worker
   performs a review/fix pass:
   classify findings as MUST, SHOULD, or NICE; fix every valid MUST and SHOULD;
   rerun affected checks; and stop after a clean result or three documented
   cycles.

6. **Review before integrating.** For every completed worktree, the
   Orchestrator inspects actual files and runs at least:

   ```bash
   git -C "<path>" status --short
   git -C "<path>" diff -- "<owned-files>"
   git -C "<path>" log --oneline "<base-ref>..HEAD"
   git log --left-right --cherry-pick --oneline "<base-ref>...<branch>"
   ```

   Confirm scope, validation evidence, and commits that are unique or otherwise
   valuable. Preserve dirty or uncommitted work. A commit, merge, cherry-pick,
   rebase, or other integration action requires the user's explicit intent for
   the named source and target; setup or implementation approval is not enough.
   Before acting, inspect repository instructions and recent history to use its
   established integration strategy. If there is no clear strategy or the work
   conflicts, stop and ask rather than improvising.

7. **Hand off completed work for local testing.** On explicit user request,
   first verify that the completed worktree is clean and its reviewed changes
   are committed on its ticket branch. If it is uncommitted, obtain separate
   explicit authorization to commit it. For a single ticket, remove the clean
   completed worktree with `git worktree remove "<path>"` while retaining its
   branch, then check that ticket branch out in the original checkout for manual
   testing. This makes the existing ignored `.env`, private keys, and other
   local configuration available without copying them into the worktree.

   To test multiple completed tickets together, integrate their approved
   branches in dependency order, one unit at a time into a named local target
   branch checked out in the original checkout. Confirm the target branch and
   its status first; if checkout, worktree removal, or integration would
   overwrite unrelated dirty changes, stop rather than stashing or moving them.
   Do not use force or bypass required checks. Re-run the ticket's focused
   validation commands from the local branch after each handoff or integration,
   then run broader repository checks when a shared boundary changed. Inspect
   its final diff and status, separating pre-existing changes from this workflow.

8. **Clean up only what is safe and authorized.** For each task-created
   worktree, inspect its status, diff, log, and commits unique to the base.
   Worktree removal and branch deletion each need explicit user intent. Remove
   only a clean worktree with `git worktree remove "<path>"` (never `--force`),
   then delete only an explicitly approved, no-longer-needed branch using the
   repository's safe practice. Do not run broad `git worktree prune`,
   `git clean`, `git reset`, wildcard deletion, or force branch deletion. Keep
   and report every dirty worktree, unique commit, failed cleanup, or resource
   outside the current task.

9. **Require evidence in worker reports and the final result.** A worker must
   report actual files changed, commands and results, assumptions/limitations,
   risks/follow-up, and temporary-resource status. The Orchestrator verifies
   the diff rather than trusting the report, then reports the worktree ledger
   as removed or retained with exact paths and reasons.

## Minimal examples

```text
/ticket-worktree inspect TICKET-123 and TICKET-124; plan disjoint ownership only
```

```text
/ticket-worktree setup-only TICKET-123 "Fix invoice export" from the default branch
```

```text
Worker mission
Worktree: /projects/app-TICKET-123
Branch: fix/TICKET-123-invoice-export
Owns: src/export/**, tests/export/**
Must not touch: migrations/**, package files
Accepts: invalid filters return the established error; focused tests pass
Validate: npm test -- export
No commit or push. Clean temporary files and report actual files, command
results, risks, and resource status. Do not integrate.
```

```text
/ticket-worktree integrate TICKET-123: remove its clean completed worktree,
retain its branch, and check it out locally for manual testing
```

## Anti-patterns

- Assuming `main`, copying a checkout, or creating a worktree before checking
  root, base, status, existing worktrees, paths, and refs.
- Treating a dirty base checkout as permission to stash, reset, or include
  unrelated work in a ticket.
- Launching parallel workers with overlapping files, missing validation
  commands, or a vague "implement ticket" mission.
- Letting a worker merge, cherry-pick, delete branches, or remove a worktree.
- Deleting a completed ticket branch when handing off its worktree for local
  testing; remove only the clean worktree so the branch can be checked out.
- Copying `.env`, private keys, or other local configuration into a ticket
  worktree solely to run manual tests.
- Using `--force`, `git clean`, broad prune, reset, or branch deletion to make
  cleanup appear complete.
- Removing a worktree before its uncommitted work and unique commits have been
  inspected, preserved, and explicitly approved for removal.

## Checklist

- [ ] Mode, ticket identity, and requested scope are unambiguous.
- [ ] Root, dirty status, base ref, worktrees, path, and branch collisions were
      checked before creation.
- [ ] Default base came from repository evidence or the user supplied it; it
      was not guessed as `main`.
- [ ] Each parallel ticket has a disjoint ownership boundary and a complete
      worker mission.
- [ ] Worker diffs, status, logs, unique commits, and validation evidence were
      reviewed by the Orchestrator.
- [ ] Explicit intent covers every commit, integration, worktree removal, and
      branch cleanup performed.
- [ ] The clean completed worktree was removed without deleting its ticket
      branch before local handoff, or approved branches were integrated into a
      named local target branch for combined testing.
- [ ] Focused validation and any manual testing ran from the local branch, and
      unrelated dirty work remains untouched.
- [ ] Cleanup ledger identifies every removed or retained path, branch, and
      temporary resource.

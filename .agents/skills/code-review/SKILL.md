---
name: code-review
description: "Review a committed branch, dirty WIP, or both against standards and the requested spec. Use for branch/PR review, staged/unstaged/untracked changes, or review since a fixed point. Direct review is the default."
---

Two-axis review of the user's requested committed changes and/or dirty WIP:

- **Standards**: does the code conform to this repo's documented coding standards?
- **Spec**: does the code faithfully implement the originating issue / spec?

Review both axes directly by default. Separate review workers are optional only with parent approval and within the parent's configured task permissions and depth. A bounded `/review` request never delegates; its scope and finding budget take precedence over this skill.

Use the user's request, supplied spec, and existing repository guidance. Issue-tracker setup is not a prerequisite for local review.

## Process

### 1. Pin the review scope and evidence

Identify whether the request is committed-only, WIP-only, or combined. For WIP, no base branch is required. For a branch review, resolve the supplied fixed point or the repository's established base; ask if ambiguous. Respect named file boundaries and exclude unrelated concurrent work and secret files.

Capture applicable evidence once, with pathspecs after `--` for bounded reviews:

- Inventory: `git status --short`.
- Committed branch: validate the ref with `git rev-parse --verify '<fixed-point>^{commit}'`, then `git diff <fixed-point>...HEAD` and `git log <fixed-point>..HEAD --oneline`. Three-dot compares against the merge-base; use two endpoints if the user explicitly requests an exact snapshot comparison.
- Staged WIP: `git diff --cached`.
- Unstaged WIP: `git diff`.
- Untracked WIP: `git ls-files --others --exclude-standard`, then read relevant text files through file tools. Untracked files do not appear in either diff; describe binary/unreadable exclusions explicitly.

For combined review, inspect committed, staged, and unstaged layers plus relevant untracked content, then reason about the final files without double-counting superseded hunks. A change that cancels across layers is still visible in its staged/unstaged evidence. Do not stage, stash, reset, or otherwise mutate the worktree to review it.

An invalid branch ref blocks only that comparison: report it and still inspect requested WIP. An empty committed diff must never skip dirty WIP. Report "no changes in scope" only after every requested layer is empty. Record the reviewed scope and any omitted layer in the final report.

### 2. Identify the spec source

Look for the originating spec, in this order:

1. The user's request or a spec path passed as an argument.
2. Issue references in commit messages, using the repository's issue-tracker guidance if available and external access is permitted.
3. A spec file under `docs/`, `specs/`, or `.scratch/` matching the branch name or feature.
4. If nothing is found, report "no spec available" and continue correctness/standards review. Ask only if missing requirements prevent a reliable finding.

### 3. Identify the standards sources

Anything in the repo that documents how code should be written, such as `CODING_STANDARDS.md` or `CONTRIBUTING.md`.

On top of whatever the repo documents, the Standards axis always carries the **smell baseline** below: a fixed set of Fowler code smells (_Refactoring_, ch.3) that applies even when a repo documents nothing. Two rules bind it:

- **The repo overrides.** A documented repo standard always wins; where it endorses something the baseline would flag, suppress the smell.
- **Always a judgement call.** Each smell is a labelled heuristic ("possible Feature Envy"), never a hard violation. Like any standard here, skip anything tooling already enforces.

Each smell reads _what it is_ → _how to fix_; match it against the diff:

- **Mysterious Name**: a function, variable, or type whose name doesn't reveal what it does or holds. → rename it; if no honest name comes, the design's murky.
- **Duplicated Code**: the same logic shape appears in more than one hunk or file in the change. → extract the shared shape, call it from both.
- **Feature Envy**: a method that reaches into another object's data more than its own. → move the method onto the data it envies.
- **Data Clumps**: the same few fields or params keep travelling together (a type wanting to be born). → bundle them into one type, pass that.
- **Primitive Obsession**: a primitive or string standing in for a domain concept that deserves its own type. → give the concept its own small type.
- **Repeated Switches**: the same `switch`/`if`-cascade on the same type recurs across the change. → replace with polymorphism, or one map both sites share.
- **Shotgun Surgery**: one logical change forces scattered edits across many files in the diff. → gather what changes together into one module.
- **Divergent Change**: one file or module is edited for several unrelated reasons. → split so each module changes for one reason.
- **Speculative Generality**: abstraction, parameters, or hooks added for needs the spec doesn't have. → delete it; inline back until a real need shows.
- **Message Chains**: long `a.b().c().d()` navigation the caller shouldn't depend on. → hide the walk behind one method on the first object.
- **Middle Man**: a class or function that mostly just delegates onward. → cut it, call the real target direct.
- **Refused Bequest**: a subclass or implementer that ignores or overrides most of what it inherits. → drop the inheritance, use composition.

### 4. Review both axes

Use the following briefs directly. If separate workers are approved, give each the complete scoped evidence from step 1, including requested WIP layers, read-only boundaries, and a no-further-delegation constraint. Never expand the parent's tool authority.

**Standards brief** should include:

- The complete scoped evidence from step 1, including the requested WIP layers and any committed range.
- The standards-source files and smell baseline from step 3; provide source pointers if using an approved worker.
- The brief: "Report, per file/hunk where relevant, (a) every place the diff violates a documented standard: cite the standard (file + the rule); and (b) any baseline smell you spot: name it and quote the hunk. Distinguish hard violations from judgement calls: documented-standard breaches can be hard, but baseline smells are always judgement calls, and a documented repo standard overrides the baseline. Skip anything tooling enforces. Under 400 words."

**Spec brief** should include:

- The complete scoped evidence from step 1, including relevant untracked content.
- The path or fetched contents of the spec.
- The brief: "Report: (a) requirements the spec asked for that are missing or partial; (b) behaviour in the diff that wasn't asked for (scope creep); (c) requirements that look implemented but where the implementation looks wrong. Quote the spec line for each finding. Under 400 words."

If the spec is missing, skip the Spec axis and note this in the final report.

### 5. Aggregate

Verify each finding against the actual files and evidence. Present high-confidence findings under `## Standards` and `## Spec`, ranked by severity within each axis, with precise file/line evidence and a concrete remedy. Separate optional smell improvements from blockers; do not treat agreed deferred validation as a current defect.

End with the reviewed layers, validation limitations, and an explicit clean result or remaining blockers. Preserve separate totals per axis so standards cannot mask a spec failure.

## Why two axes

A change can pass one axis and fail the other:

- Code that follows every standard but implements the wrong thing → **Standards pass, Spec fail.**
- Code that does exactly what the issue asked but breaks the project's conventions → **Spec pass, Standards fail.**

Reporting them separately stops one axis from masking the other.

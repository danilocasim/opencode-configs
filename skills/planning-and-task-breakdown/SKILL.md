---
name: planning-and-task-breakdown
description: Decompose large work with unresolved dependencies into verifiable tasks. Use for an explicit planning request or work spanning multiple delivery stages, not clear bounded implementation.
---

# Planning and Task Breakdown

## Overview

Decompose work into small, verifiable tasks with explicit acceptance criteria. Good task breakdown is the difference between an agent that completes work reliably and one that produces a tangled mess. Every task should be small enough to implement, test, and verify in a single focused session.

## When to Use

- You have a spec and need to break it into implementable units
- A task feels too large or vague to start
- Work needs to be parallelized across multiple agents or sessions
- You need an explicit multi-stage delivery plan
- The implementation order isn't obvious

**When NOT to use:** Clear bounded changes, including multi-file work, or an accepted spec with well-defined tasks. Use the supplied acceptance criteria and proceed with implementation when requested; do not repeat plan approval.

## The Planning Process

### Step 1: Enter Plan Mode

Before writing any code, operate in read-only mode:

- Read the spec and relevant codebase sections
- Identify existing patterns and conventions
- Map dependencies between components
- Note risks and unknowns

**For a plan-only request, do not write product code.** Return the plan in the requested form. Persist planning files only when requested or required by the repository's actual workflow, using its existing paths.

### Step 2: Identify the Dependency Graph

Map what depends on what:

```
Database schema
    │
    ├── API models/types
    │       │
    │       ├── API endpoints
    │       │       │
    │       │       └── Frontend API client
    │       │               │
    │       │               └── UI components
    │       │
    │       └── Validation logic
    │
    └── Seed data / migrations
```

Implementation order follows the dependency graph bottom-up: build foundations first.

### Step 3: Slice Vertically

Instead of building all the database, then all the API, then all the UI — build one complete feature path at a time:

**Bad (horizontal slicing):**

```
Task 1: Build entire database schema
Task 2: Build all API endpoints
Task 3: Build all UI components
Task 4: Connect everything
```

**Good (vertical slicing):**

```
Task 1: User can create an account (schema + API + UI for registration)
Task 2: User can log in (auth schema + API + UI for login)
Task 3: User can create a task (task schema + API + UI for creation)
Task 4: User can view task list (query + API + UI for list view)
```

Each vertical slice delivers working, testable functionality.

### Step 4: Write Tasks

Each task follows this structure:

```markdown
## Task [N]: [Short descriptive title]

**Description:** One paragraph explaining what this task accomplishes.

**Acceptance criteria:**

- [ ] [Specific, testable condition]
- [ ] [Specific, testable condition]

**Verification:**

- [ ] Tests pass: `npm test -- --grep "feature-name"`
- [ ] Build succeeds: `npm run build`
- [ ] Manual check: [description of what to verify]

**Dependencies:** [Task numbers this depends on, or "None"]

**Files likely touched:**

- `src/path/to/file.ts`
- `tests/path/to/test.ts`

**Estimated scope:** [Small: 1-2 files | Medium: 3-5 files | Large: 5+ files]
```

### Step 5: Order and Checkpoint

Arrange tasks so that:

1. Dependencies are satisfied (build foundation first)
2. Each task leaves the system in a working state
3. Verification checkpoints occur after every 2-3 tasks
4. High-risk tasks are early (fail fast)

Add explicit checkpoints:

```markdown
## Checkpoint: After Tasks 1-3

- [ ] All tests pass
- [ ] Application builds without errors
- [ ] Core user flow works end-to-end
- [ ] Confirm any newly discovered consequential decision before proceeding
```

## Task Sizing Guidelines

| Size   | Files | Scope                                 | Example                              |
| ------ | ----- | ------------------------------------- | ------------------------------------ |
| **XS** | 1     | Single function or config change      | Add a validation rule                |
| **S**  | 1-2   | One component or endpoint             | Add a new API endpoint               |
| **M**  | 3-5   | One feature slice                     | User registration flow               |
| **L**  | 5-8   | Multi-component feature               | Search with filtering and pagination |
| **XL** | 8+    | **Too large — break it down further** | —                                    |

If a task is L or larger, it should be broken into smaller tasks. An agent performs best on S and M tasks.

**When to break a task down further:**

- It would take more than one focused session (roughly 2+ hours of agent work)
- You cannot describe the acceptance criteria in 3 or fewer bullet points
- It touches two or more independent subsystems (e.g., auth and billing)
- You find yourself writing "and" in the task title (a sign it is two tasks)

## Output Files

- Prefer the user's named documents or the repository's existing planning convention.
- If no persistent artifacts are requested, an inline plan/checklist is sufficient.

When persistent artifacts are requested but no path is established, propose paths
such as `tasks/plan.md` and `tasks/todo.md` before creating them. Do not assume an
unavailable command or downstream tool requires these files.

## Plan Document Template

```markdown
# Implementation Plan: [Feature/Project Name]

## Overview

[One paragraph summary of what we're building]

## Architecture Decisions

- [Key decision 1 and rationale]
- [Key decision 2 and rationale]

## Task List

### Phase 1: Foundation

- [ ] Task 1: ...
- [ ] Task 2: ...

### Checkpoint: Foundation

- [ ] Tests pass, builds clean

### Phase 2: Core Features

- [ ] Task 3: ...
- [ ] Task 4: ...

### Checkpoint: Core Features

- [ ] End-to-end flow works

### Phase 3: Polish

- [ ] Task 5: ...
- [ ] Task 6: ...

### Checkpoint: Complete

- [ ] All acceptance criteria met
- [ ] Ready for review

## Risks and Mitigations

| Risk   | Impact         | Mitigation |
| ------ | -------------- | ---------- |
| [Risk] | [High/Med/Low] | [Strategy] |

## Open Questions

- [Question needing human input]
```

## Parallelization Opportunities

When parallel execution is explicitly approved and configured permissions/depth allow it (otherwise implement directly):

- **Safe to parallelize:** Independent feature slices, tests for already-implemented features, documentation
- **Must be sequential:** Database migrations, shared state changes, dependency chains
- **Needs coordination:** Features that share an API contract (define the contract first, then parallelize)

## Common Rationalizations

| Rationalization                | Reality                                                                                            |
| ------------------------------ | -------------------------------------------------------------------------------------------------- |
| "I'll figure it out as I go"   | That's how you end up with a tangled mess and rework. 10 minutes of planning saves hours.          |
| "The tasks are obvious"        | Reuse accepted tasks; write a new breakdown only when dependencies or verification remain unclear. |
| "Planning is overhead"         | Scale the plan to uncertainty. Clear bounded work needs no extra planning ceremony.                |
| "I can hold it all in my head" | Context windows are finite. Written plans survive session boundaries and compaction.               |

## Red Flags

- Starting a large uncertain implementation without acceptance criteria or dependency order
- Tasks that say "implement the feature" without acceptance criteria
- No verification steps in the plan
- All tasks are XL-sized
- No checkpoints between tasks
- Dependency order isn't considered

## Verification

Before starting implementation, confirm:

- [ ] Every task has acceptance criteria
- [ ] Every task has a verification step
- [ ] Task dependencies are identified and ordered correctly
- [ ] Each task is independently verifiable; file count is a sizing heuristic, not a gate
- [ ] Checkpoints exist between major phases
- [ ] Required approvals are satisfied; accepted plans are not re-approved without a material change

## See Also

Acceptance criteria answer "did we build the right thing?". Use the repository's actual completion guidance and report passed, blocked, or deferred checks without inventing a global completion document.

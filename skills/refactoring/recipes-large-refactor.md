# Recipe: Large Refactor

Use this when the change is too risky for one PR. The goal is to create safe stepping stones.

## When to load

- You need to refactor a core subsystem.
- You need a phased plan with checkpoints.

## When NOT to load

- You can do it safely in small commits with tests already in place.
- You are changing behavior (write tests first).

## Core rules

- Define the target shape and success criteria.
- Freeze behavior with characterization tests.
- Introduce seams and parallel paths if needed.
- Migrate call sites incrementally.
- Delete the old path when migration completes.

## Minimal examples

Phased plan:

```text
phase 1: add tests + seams
phase 2: add new implementation behind flag
phase 3: migrate call sites
phase 4: remove old code
```

## Anti-patterns

- Big bang rewrite.
- Keeping both implementations forever.
- No cleanup milestone.

## Checklist

- Success criteria defined.
- Tests freeze behavior.
- Migration is incremental.
- Old code removed.

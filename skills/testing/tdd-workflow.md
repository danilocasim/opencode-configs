# TDD Workflow (Red -> Green -> Refactor)

Use this workflow to keep scope small and feedback fast.

## When to load

- You are implementing behavior and want test-first execution.
- You are fixing a bug and need regression discipline.

## When NOT to load

- You need stack-specific test library details (load stack file).

## Core rules

- Define behavior first: Given X, when Y, then Z.
- Red: write a failing test for that behavior.
- Green: implement the minimum to pass.
- Refactor: improve code/tests while staying green.

## Common patterns

- Start with unit tests, then move upward only if needed.
- For bugs: repro test first, then fix.
- Keep fixtures minimal and explicit.
- Control time/randomness/network at boundaries.

## Minimal examples

Tiny Red/Green loop (language-agnostic):

1. Red (write test)

```text
test: normalize_email("  A@B.COM ") -> "a@b.com"
```

2. Green (minimal implementation)

```text
return input.strip.downcase
```

3. Refactor (extract + add error path)

```text
validate "@" present; raise/return error contract
```

## Anti-patterns

- Writing implementation first, then backfilling tests.
- Asserting private internals instead of outcomes.
- One giant integration test for many behaviors.
- Flaky retries as a substitute for determinism.

## Checklist

- Is the failing test failing for the right reason?
- Did you implement only enough to pass?
- Did you run relevant suites after refactor?
- Did you keep regression tests for fixed bugs?

## References

- Kent Beck, TDD by Example
- Testing Trophy (pragmatic adaptation)

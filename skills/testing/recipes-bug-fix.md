# Recipe: Bug Fix (Repro -> Regression -> Fix)

## When to load

- You are fixing a bug and want a disciplined test-first approach.
- You need to minimize the repro and avoid overfitting the fix.

## When NOT to load

- You are designing a new feature from scratch (use `tdd-workflow.md`).
- The issue is CI flakiness (use `ci-reliability-and-flake-control.md`).

## Core rules

- Reproduce first, then fix.
- The regression test must fail on old code for the right reason.
- Prefer the lowest test level that can repro the bug.
- Add a second test only if it covers a different risk.

## Common patterns

- Turn an incident report into a Given/When/Then.
- Reduce setup until the failing behavior is obvious.
- Add an assertion for the error contract (status/message/shape) if relevant.
- Add a guard test for the nearest boundary (input validation, nil handling).

## Minimal examples

Template (language-agnostic):

```text
Given: user without timezone
When:  they request /reports/daily
Then:  the API returns 200 with dates in UTC (not 500)
```

Vitest bug repro skeleton:

```ts
import { expect, it } from "vitest";

it("does not crash when timezone is missing (regression)", () => {
  expect(() => renderDailyReport({ timeZone: null })).not.toThrow();
});
```

## Anti-patterns

- Fixing first, then writing a test that always passes.
- Testing the patch rather than the bug (asserting a private helper call).
- Adding multiple changes without isolating which one fixed the bug.

## Checklist

- Can you reproduce the bug locally with one command?
- Is the repro test minimal and clearly named as a regression?
- Does the test fail on old code and pass on the fix?
- Did you add coverage for the user-visible contract (if applicable)?

## References

- `tdd-workflow.md`
- `ci-reliability-and-flake-control.md`

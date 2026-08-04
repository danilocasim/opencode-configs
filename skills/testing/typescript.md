# TypeScript/JavaScript Testing (Vitest/Jest)

## When to load

- You are testing TS/JS libraries, services, or React components.
- You need a default unit/integration approach with Vitest/Jest.

## When NOT to load

- You are testing a Next.js app (App Router, server actions, route handlers): use `node-nextjs.md`.
- You are writing Playwright E2E tests: use `e2e-playwright.md`.

## Core rules

- Prefer the repo's existing runner; default to Vitest for new work.
- Assert behavior (outputs, rendered UI, emitted events), not private internals.
- Control time, randomness, and network; avoid real HTTP in unit tests.
- Keep tests fast; push slow wiring to a small integration/E2E layer.

## Common patterns

- Vitest unit tests for pure functions and business rules.
- React Testing Library + user-event for components.
- MSW for HTTP mocking when you need realistic request/response behavior.
- `vi.useFakeTimers()` for time-sensitive logic.

## Minimal examples

Vitest unit test:

```ts
import { describe, expect, it } from "vitest";

import { normalizeDate } from "./normalizeDate";

describe("normalizeDate", () => {
  it("returns ISO date", () => {
    expect(normalizeDate("2026-01-31", "UTC")).toBe("2026-01-31");
  });
});
```

React component test (RTL):

```tsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";

import { Counter } from "./Counter";

it("increments when clicked", async () => {
  const user = userEvent.setup();

  render(<Counter />);

  await user.click(screen.getByRole("button", { name: /count/i }));

  expect(screen.getByText(/count: 1/i)).toBeInTheDocument();
});
```

## Anti-patterns

- Snapshot-heavy tests for business logic.
- Mocking module internals instead of injecting boundaries.
- Uncontrolled network/time in tests that run in CI.

## Checklist

- Is this the smallest test level that proves the behavior?
- Are time/random/network inputs controlled?
- Does the test assert user-observable outcomes?
- Will this remain readable after six months?

## References

- Vitest: https://vitest.dev/
- Jest: https://jestjs.io/
- React Testing Library: https://testing-library.com/docs/react-testing-library/intro/
- MSW: https://mswjs.io/

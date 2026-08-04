# Node / Next.js Testing (TDD-First)

Use this guide for Node backends, shared TS/JS libs, and Next.js apps.

## When to load

- You are testing Node/Next.js logic, routes, server actions, or UI components.
- You need clear test-level routing (unit vs integration vs e2e).

## When NOT to load

- Non-JS stacks.
- Pure lint/type tasks.

## Core rules

- Use existing repo tools: Vitest preferred for new setups, Jest if already present.
- React UI tests: React Testing Library + user-event.
- API/network isolation: MSW where HTTP mocking is needed.
- E2E: Playwright for critical workflows only.

## Common patterns

- Unit tests for pure `lib` logic and validators.
- Integration tests for route handlers and server actions.
- Component tests assert user-visible behavior and accessibility.
- E2E for auth, checkout, and other business-critical paths.

```ts
import { describe, expect, it } from "vitest";

const normalizeSlug = (s: string) => s.toLowerCase().replaceAll(" ", "-");

describe("normalizeSlug", () => {
  it("lowercases and replaces spaces", () => {
    expect(normalizeSlug("Hello World")).toBe("hello-world");
  });
});
```

## Minimal examples

React component test (RTL):

```tsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { useState } from "react";

function Counter() {
  const [n, setN] = useState(0);

  return (
    <button type="button" onClick={() => setN((x) => x + 1)}>
      <span>Count:</span> <span>{n}</span>
    </button>
  );
}

it("increments when clicked", async () => {
  const user = userEvent.setup();

  render(<Counter />);

  await user.click(screen.getByRole("button", { name: /count/i }));

  expect(screen.getByText(/count: 1/i)).toBeInTheDocument();
});
```

Route handler unit/integration-style test (pure function contract):

```ts
import { expect, it } from "vitest";

export async function GET() {
  return Response.json({ ok: true }, { status: 200 });
}

it("returns ok json", async () => {
  const res = await GET();

  expect(res.status).toBe(200);
  await expect(res.json()).resolves.toEqual({ ok: true });
});
```

## Anti-patterns

- Snapshot-heavy tests for business logic.
- Mocking framework internals instead of user outcomes.
- E2E-first for behavior that unit/integration can prove.
- Real network calls in CI unit tests.

## Checklist

- Is test level the smallest that proves behavior?
- Are auth/error paths covered for routes/actions?
- Are network/time sources controlled?
- Are critical flows covered in Playwright without over-expanding suite size?

## References

- Vitest: https://vitest.dev/
- React Testing Library: https://testing-library.com/docs/react-testing-library/intro/
- Playwright: https://playwright.dev/

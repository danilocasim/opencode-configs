# Test Doubles and Mocking Discipline

## When to load

- You are deciding between fakes/stubs/mocks/spies.
- Tests are brittle because they assert implementation details.
- You need to isolate time, network, filesystem, DB, queues.

## When NOT to load

- You mainly need fixture strategy (use `fixtures-and-test-data.md`).
- You need E2E advice (use `e2e-playwright.md`).

## Core rules

- Prefer real code + fake boundaries (dependency injection).
- Mock at the boundary you do not own (HTTP client, clock, DB adapter), not internals.
- Favor fakes (in-memory implementations) over mocks for most unit tests.
- If you must mock, assert on _observable outcomes_; keep call-count assertions rare.
- One test should mock at most one boundary; otherwise you are testing your mocks.

## Common patterns

- Clock interface for time control.
- In-memory repository as a fake.
- Stub HTTP layer with MSW (JS/TS) or local test server.
- Spy only to verify "must happen" side effects (e.g., audit event emitted).

## Minimal examples

TypeScript boundary injection (fake repo):

```ts
type User = { id: string; email: string };

interface UserRepo {
  getById(id: string): Promise<User | null>;
}

class InMemoryUserRepo implements UserRepo {
  constructor(private readonly users: User[]) {}
  async getById(id: string): Promise<User | null> {
    return this.users.find((u) => u.id === id) ?? null;
  }
}
```

Vitest stub of a boundary (clock):

```ts
import { expect, it, vi } from "vitest";

it("stamps createdAt using the injected clock", () => {
  const now = new Date("2026-02-01T00:00:00.000Z");
  const clock = { now: vi.fn(() => now) };

  const created = createOrder({ clock });

  expect(created.createdAt).toEqual(now);
});
```

## Anti-patterns

- Mocking the subject under test.
- Verifying long call sequences ("trained" mocks) for domain logic.
- Using mocks to avoid making design observable (missing return values/events).
- Mocking framework internals (ActiveRecord, React hooks, etc.).

## Checklist

- Is the boundary explicit (interface/port) rather than hidden global state?
- Does the test read like a behavior spec rather than a call script?
- Can the same behavior be proven with a fake instead of a mock?
- Are you asserting what the user/system observes (output/state/event)?

## References

- xUnit test patterns (mocks/stubs/fakes): https://martinfowler.com/articles/mocksArentStubs.html
- MSW: https://mswjs.io/

# Fixtures and Test Data

## When to load

- You need deterministic, readable test setup (DB rows, files, payloads).
- You are debating factories vs fixtures vs builders vs inline data.
- Tests are slow or brittle due to heavy setup graphs.

## When NOT to load

- You only need a mocking strategy (use `test-doubles-and-mocking-discipline.md`).
- You are writing E2E setup/seed flows (use `recipes-playwright-e2e.md`).

## Core rules

- Prefer minimal, explicit data that highlights what the test cares about.
- One test should not depend on data created by another test.
- Keep fixture APIs stable: treat them like production APIs.
- Avoid "kitchen sink" factories/fixtures; add traits/builders for intent.
- Make randomness explicit: seed it or remove it.

## Common patterns

- Data builder: `aUser().withRole("admin").build()`
- Factory traits: `create(:user, :admin)`
- Golden payloads for external contracts (JSON) stored under `testdata/`.
- Database state isolation per test (transaction/rollback) or per file suite.
- Clock/env isolation via helper: `freezeTime(...)`, `withEnv(...)`.

## Minimal examples

TypeScript data builder:

```ts
type User = { id: string; email: string; role: "user" | "admin" };

const aUser = (overrides: Partial<User> = {}): User => ({
  id: "u_123",
  email: "a@example.com",
  role: "user",
  ...overrides,
});
```

pytest parametrized matrix (prefer over many near-duplicate tests):

```python
import pytest


@pytest.mark.parametrize(
    "raw, expected",
    [("  A@EXAMPLE.COM ", "a@example.com"), ("x@y.com", "x@y.com")],
)
def test_normalize_email(raw: str, expected: str) -> None:
    assert normalize_email(raw) == expected
```

Go `testdata/` file fixture:

```go
payload, err := os.ReadFile("testdata/invalid-user.json")
if err != nil { t.Fatal(err) }
```

## Anti-patterns

- Autouse/global fixtures that silently change many tests.
- Factories that create unrelated records "just in case".
- Fixtures with time/network side effects.
- Tests that require a specific run order.

## Checklist

- Can a new reader tell what data matters in 10 seconds?
- Is setup cost proportional to the behavior under test?
- Are time/random/env inputs controlled?
- Does fixture helper surface intent (traits/builders) rather than mechanics?

## References

- pytest fixtures: https://docs.pytest.org/en/stable/how-to/fixtures.html
- Rails fixtures vs factories (guide): https://guides.rubyonrails.org/testing.html

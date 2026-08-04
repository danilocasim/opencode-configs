# E2E Testing with Playwright

## When to load

- You need end-to-end coverage for a critical user journey.
- You are debugging a UI workflow failure that unit/integration tests miss.
- You need guidance on selectors, waits, tracing, and keeping suites fast.

## When NOT to load

- The behavior can be proven at unit/integration level.
- You need CI flake triage strategy (use `ci-reliability-and-flake-control.md`).

## Core rules

- Use E2E for critical paths only; keep the suite small and high-value.
- Prefer role-based locators and accessibility names; avoid brittle CSS selectors.
- Never rely on arbitrary sleeps; use Playwright auto-waits and explicit assertions.
- Keep tests isolated: create/seed their own data; avoid shared accounts/state.
- Capture artifacts on failure (trace, video, screenshots) to make debugging cheap.

## Common patterns

- `getByRole` + `toBeVisible` for user-visible behavior.
- Authenticate once per worker (storage state) for speed.
- Seed via API (preferred) rather than UI clicks.
- Use stable `data-testid` only when roles/names are not viable.

## Minimal examples

```ts
import { expect, test } from "@playwright/test";

test("user can log in", async ({ page }) => {
  await page.goto("/");
  await page.getByRole("link", { name: "Log in" }).click();

  await page.getByLabel("Email").fill("a@example.com");
  await page.getByLabel("Password").fill("password");
  await page.getByRole("button", { name: "Continue" }).click();

  await expect(page.getByRole("heading", { name: "Dashboard" })).toBeVisible();
});
```

## Anti-patterns

- E2E tests for every edge case (should be unit/integration).
- Sleep-based waiting (`waitForTimeout`) as a default.
- Sharing a single "golden" user across tests.
- Page-object layers that hide assertions and intent.

## Checklist

- Is this flow business-critical and cross-layer?
- Are locators stable (role/label/name) and readable?
- Is test data created/seeded deterministically?
- Are trace/screenshot/video configured for failures?

## References

- Playwright test runner: https://playwright.dev/docs/test-intro
- Locators: https://playwright.dev/docs/locators

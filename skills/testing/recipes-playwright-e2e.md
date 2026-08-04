# Recipe: Playwright E2E (High-Signal, Low-Flake)

## When to load

- You are about to add a new Playwright spec.
- You need a stable approach to seeding, login, and assertions.

## When NOT to load

- You need CI flake policy and mitigation (use `ci-reliability-and-flake-control.md`).
- You are exploring mocking discipline (use `test-doubles-and-mocking-discipline.md`).

## Core rules

- Prefer API seeding + storage state over UI setup.
- Keep one spec focused on one user outcome.
- Use role/label locators; avoid brittle selectors.
- Make the test readable: arrange, act, assert.

## Common patterns

- `globalSetup` seeds baseline data.
- `storageState` per role (admin/user) to skip repeated logins.
- `expect.poll` for eventual consistency when truly needed.
- Test IDs only for non-semantic elements.

## Minimal examples

Spec skeleton:

```ts
import { expect, test } from "@playwright/test";

test("checkout completes", async ({ page }) => {
  await page.goto("/shop");
  await page.getByRole("button", { name: "Add to cart" }).first().click();
  await page.getByRole("link", { name: "Cart" }).click();
  await page.getByRole("button", { name: "Checkout" }).click();

  await expect(page.getByRole("heading", { name: "Order confirmed" })).toBeVisible();
});
```

## Anti-patterns

- UI-driven seeding (creating ten objects by clicking forms).
- Cross-test coupling via shared accounts/orders.
- Asserting on unstable text (timestamps, randomized IDs) without control.

## Checklist

- Does the test create/seed what it needs deterministically?
- Are locators robust (role/label/name)?
- Are assertions user-visible and specific?
- Are artifacts captured for failures (trace/screenshot/video)?

## References

- `e2e-playwright.md`
- Playwright best practices: https://playwright.dev/docs/best-practices

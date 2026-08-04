# Testing (Capacitor)

Capacitor apps need tests at two levels: web behavior and device wiring. Keep most tests in the web layer, and add a small set of device smoke/E2E tests for critical flows.

## When to load

- You are adding tests for a Capacitor app.
- You need a strategy for device-only bugs.
- You need a minimal E2E plan.

## When NOT to load

- You are only writing unit tests for web logic (use web stack testing docs).
- You are doing native UI frameworks.

## Core rules

- Most tests should run in Node (fast): unit + integration for web.
- Add a small set of device tests for: auth, push, deep links, permissions.
- Prefer deterministic E2E; avoid sleep-based waits.
- Mock boundaries in unit tests; use real wiring only in smoke suites.

## Minimal examples

Test pyramid:

```text
unit: web logic (fast)
integration: web app + API mocks
device smoke: install + launch + login
device e2e: 1-3 critical journeys
```

## Anti-patterns

- E2E for every edge case.
- Real network calls in unit tests.
- No on-device verification for push/deep links.

## Checklist

- Web layer has strong coverage.
- Device smoke suite exists.
- Critical device-only features covered.
- CI runs are stable.

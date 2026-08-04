# CI Reliability and Flake Control

## When to load

- CI failures are intermittent (flakes) and hard to reproduce locally.
- Tests are timing-sensitive, resource-sensitive, or environment-sensitive.
- You need a policy for retries, quarantines, and ownership.

## When NOT to load

- You are only writing local unit tests with deterministic inputs.
- You need E2E authoring guidance (use `e2e-playwright.md`).

## Core rules

- Treat flakes as bugs: find root cause; do not normalize them.
- Prefer determinism over retries; retries are a last-resort mitigation.
- Make failures actionable: logs, traces, and minimal repro steps.
- Separate "slow" from "fast" suites; run fast on every change.
- Pin versions and control environment (TZ, locale, randomness seed).

## Common patterns

- Time control: fake timers or injected clock.
- Random control: explicit seeds and snapshotting of failing seeds.
- Hermetic IO: no real network; stub with MSW/local servers.
- Resource control: lower concurrency for brittle suites; isolate DB per job.
- Flake triage tags: `@flaky` + owner + tracking link, with expiry policy.

## Minimal examples

Playwright retries + trace-on-retry (mitigation, not a cure):

```ts
import { defineConfig } from "@playwright/test";

export default defineConfig({
  retries: process.env.CI ? 2 : 0,
  use: {
    trace: "on-first-retry",
    screenshot: "only-on-failure",
    video: "retain-on-failure",
  },
});
```

Vitest deterministic fake timers:

```ts
import { afterEach, beforeEach, vi } from "vitest";

beforeEach(() => {
  vi.useFakeTimers();
  vi.setSystemTime(new Date("2026-02-01T00:00:00.000Z"));
});

afterEach(() => {
  vi.useRealTimers();
});
```

## Anti-patterns

- Blanket retries that hide real bugs.
- `sleep(1000)` to "stabilize" a test.
- Shared mutable state between tests/jobs.
- Flakes with no owner and no tracking.

## Checklist

- Can the failure be reproduced locally with a single command?
- Are time/TZ/locale/randomness controlled?
- Are external dependencies stubbed or run as local services?
- Are artifacts captured for failures (trace/logs/core dumps)?
- Are mitigations time-boxed and tracked to a root-cause fix?

## References

- Playwright trace viewer: https://playwright.dev/docs/trace-viewer
- Google Testing Blog (reliability): https://testing.googleblog.com/

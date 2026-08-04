# CI Pipelines

CI should be deterministic and fast. Make it hard to merge broken code and easy to debug failures.

## When to load

- You are changing CI steps or caching.
- CI is flaky or slow.
- You need ordering guidance for checks.

## When NOT to load

- You are writing application tests (use `../testing/SKILL.md`).
- You only need Docker guidance (`dockerfiles-and-images.md`).

## Core rules

- Order: format -> lint -> typecheck -> tests -> build.
- Cache based on lockfiles.
- Run the same commands locally and in CI.
- Keep secrets out of logs.
- Make flaky tests a stop-ship issue.

## Minimal examples

Pipeline shape:

```text
checkout
restore cache
install
format/lint/type
test
build
```

## Anti-patterns

- One giant job that hides what failed.
- Caching without lockfile keys.
- “Allowed failures” for core checks.

## Checklist

- Commands match local dev.
- Caches keyed by lockfiles.
- Failures are isolated and readable.
- Flakes tracked and fixed.

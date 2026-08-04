# Recipe: CI-Like Checks Locally

Use this when you want a predictable local routine that mirrors CI order and catches issues early.

## When to load

- You are setting up a repo’s “what to run before pushing” commands.
- CI failures are common and you want to reduce them.

## When NOT to load

- You are writing tests (use `../testing/SKILL.md`).
- You only need Docker changes (`dockerfiles-and-images.md`).

## Core rules

- Run in CI order: format -> lint -> typecheck -> tests -> build.
- Use the same commands CI uses.
- Keep a single entrypoint script if possible.

## Minimal examples

Order:

```text
format
lint
type
test
build
```

## Anti-patterns

- Running only tests and ignoring format/lint.
- Different commands locally vs CI.
- Hiding failures behind “best effort” scripts.

## Checklist

- Local routine matches CI.
- Failures are fast and obvious.
- One documented entrypoint exists.

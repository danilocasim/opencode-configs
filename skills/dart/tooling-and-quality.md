# Tooling and Quality (Dart)

Dart stays maintainable when formatting and analysis are non-negotiable and run in CI the same way they run locally.

## When to load

- You are setting up a Dart package/app.
- You need a deterministic quality gate (format + analyze + tests).
- You need lints and strictness defaults.

## When NOT to load

- You are doing Flutter UI work (use `../flutter/SKILL.md`).
- You only need error modeling (`errors-and-results.md`).

## Core rules

- Always run `dart format` and `dart analyze`.
- Treat analyzer warnings as failures in CI.
- Prefer `package:lints` (or repo-specific rules) and keep them enforced.
- Keep dependencies minimal; pin appropriately.

## Minimal examples

Common commands:

```bash
dart format .
dart analyze
dart test
```

`analysis_options.yaml` starter:

```yaml
include: package:lints/recommended.yaml

linter:
  rules:
    avoid_print: true
    prefer_single_quotes: false

analyzer:
  errors:
    unused_import: error
    dead_code: error
```

## Anti-patterns

- Formatting in editor only (drifts in CI).
- Silencing analyzer warnings instead of fixing root cause.
- Adding heavy dependencies for trivial utilities.

## Checklist

- `dart format` run and enforced.
- `dart analyze` clean.
- Lints configured.
- Tests run in CI.

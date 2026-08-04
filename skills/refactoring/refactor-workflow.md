# Refactor Workflow

Refactors are safest when behavior is frozen first. Make the code observable, then change it in small steps.

## When to load

- You need a repeatable refactor loop.
- You are refactoring with unknown test coverage.
- You want rules for “stop and add tests”.

## When NOT to load

- You are writing new behavior (use TDD guidance: `../testing/SKILL.md`).
- You are doing performance profiling (`../performance/SKILL.md`).

## Core rules

- Freeze behavior with tests before structural changes.
- Change in small, reversible steps.
- Keep diffs small and isolated.
- Prefer extraction over rewrites.
- Maintain public contracts (inputs/outputs/errors).

## Minimal examples

Loop:

```text
add characterization test -> refactor -> keep green -> repeat
```

## Anti-patterns

- Rewrite “because it’s messy” with no tests.
- Mixing behavior changes with refactor.
- Massive PRs with no checkpoints.

## Checklist

- Tests freeze behavior.
- Steps are small and reversible.
- Behavior changes are separate.
- Public contracts preserved.

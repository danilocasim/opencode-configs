# Recipe: New Screen Flow

Use this to add a new screen with clean boundaries: route wiring, controller/state, UI, and tests.

## When to load

- You are adding a new screen.
- You want a repeatable checklist for quality (loading/error/a11y/tests).

## When NOT to load

- You are only doing theme/token work.
- You are only doing navigation refactors.

## Core rules

- Screen widgets render state; controllers/services own logic.
- Route params validated at the boundary.
- Loading/error states are explicit.
- Primary action is accessible and large enough.

## Minimal examples

Checklist:

```text
1) add route
2) add controller + state model
3) add screen widget
4) loading + error UI
5) a11y labels/tooltips
6) widget test for primary behavior
```

## Anti-patterns

- Logic inside `build()`.
- No loading/error UI.
- Unvalidated route params.

## Checklist

- Params validated.
- Loading/error present.
- Primary action accessible.
- Tests added.

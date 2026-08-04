# Recipe: New Screen Flow

Use this when adding a new screen + navigation route + basic UI scaffolding with platform-safe defaults.

## When to load

- You are adding a new user-facing screen.
- You need a repeatable checklist (route, analytics, a11y, loading/error).

## When NOT to load

- You are primarily doing UI token work (`ui-ux-and-design-system.md`).
- You are implementing complex animations (`animations-and-gestures.md`).

## Core rules

- Screen owns rendering; logic lives in hooks/services.
- Validate params (deep link / route params) at the boundary.
- Provide loading and error states.
- Make the primary action accessible and large enough.
- Test the flow at the smallest level that proves it.

## Minimal examples

Checklist:

```text
1) add route
2) add screen component
3) add hook/service for data
4) loading + error UI
5) a11y labels
6) unit/component test
```

## Anti-patterns

- Screen that mixes navigation, fetching, and business rules.
- No loading/error states.
- Unvalidated route params.

## Checklist

- Params validated.
- Loading/error UI present.
- Primary action accessible.
- Tests added.

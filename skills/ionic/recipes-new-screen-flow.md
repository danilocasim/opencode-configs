# Recipe: New Screen Flow

Use this to add a new screen with consistent Ionic layout, routing, loading/error UI, and tests.

## When to load

- You are adding a new page.
- You want a repeatable checklist.

## When NOT to load

- You are only doing theming (`design-system.md`).
- You are only doing Capacitor plugin work.

## Core rules

- Use the canonical `IonPage` skeleton.
- Validate route params.
- Add loading + error states.
- Keep page logic thin.

## Minimal examples

Checklist:

```text
1) add route
2) create page with IonPage skeleton
3) fetch data in hook/service
4) loading + error UI
5) add a11y labels
6) add unit/component test
```

## Anti-patterns

- Page that mixes business logic and UI.
- No loading/error state.
- Unvalidated params.

## Checklist

- Skeleton correct.
- Params validated.
- Loading/error UI present.
- Tests added.

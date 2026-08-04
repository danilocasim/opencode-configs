# Project Structure (Ionic)

Ionic apps are web apps with extra UI primitives and mobile navigation patterns. Keep features owned, pages thin, and Capacitor access behind a wrapper.

## When to load

- You are starting a new Ionic app.
- You are reorganizing a messy `pages/` and `components/` structure.

## When NOT to load

- You only need theming/design tokens (`design-system.md`).
- You are doing native build/signing (`../capacitor/SKILL.md`).

## Core rules

- Prefer feature-first structure.
- Keep pages orchestrating only (route params, data hooks, composition).
- Centralize app-wide UI primitives and tokens.
- Wrap Capacitor calls behind `src/native/*`.

## Minimal examples

Structure sketch:

```text
src/
  app/
    App.tsx
    routes.tsx
  features/
    auth/
      pages/
      components/
      api/
      hooks/
    projects/
      pages/
      components/
      api/
      hooks/
  ui/
    Button.tsx
    Field.tsx
    EmptyState.tsx
  theme/
    tokens.css
    ionic-overrides.css
  native/
    index.ts
    push.ts
    storage.ts
```

## Anti-patterns

- Giant global `components/` folder.
- Pages that contain business logic, fetching, and view in one file.
- Capacitor imports spread across features.

## Checklist

- Feature ownership is clear.
- UI primitives and tokens are centralized.
- Capacitor access is wrapped.
- Pages remain thin.

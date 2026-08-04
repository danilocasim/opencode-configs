# Project Structure (React Native)

Mobile apps get messy fast when features don’t have clear ownership. Prefer feature-first structure with shared UI primitives and explicit platform surfaces.

## When to load

- You are creating a new RN app or reorganizing folders.
- You are deciding where UI, domain logic, and native adapters should live.

## When NOT to load

- You only need navigation patterns (`navigation.md`).
- You only need Expo-specific setup (use `../expo/SKILL.md`).

## Core rules

- Organize by feature; avoid a giant `components/` junk drawer.
- Keep screen components thin; push business logic into hooks/services.
- Centralize platform adapters (permissions, storage, push) behind `lib/`.
- Separate shared UI primitives from feature UI.
- Prefer explicit module boundaries to reduce circular imports.

## Minimal examples

Feature-first layout:

```text
src/
  app/
    App.tsx
  features/
    auth/
      screens/
      components/
      hooks/
      api/
    profile/
      screens/
      components/
      hooks/
  ui/
    Button.tsx
    Text.tsx
    Stack.tsx
  lib/
    http/
    storage/
    permissions/
  assets/
  types/
```

Platform-specific files when needed:

```text
ui/Modal.ios.tsx
ui/Modal.android.tsx
```

## Anti-patterns

- `utils/` for everything.
- Screens that fetch, validate, transform, and render in one file.
- Platform-specific `if (Platform.OS...)` scattered across the app.
- Shared UI tied to one feature.

## Checklist

- Each feature has a clear home.
- UI primitives are centralized and reusable.
- Platform differences are localized.
- Business logic is testable outside screens.

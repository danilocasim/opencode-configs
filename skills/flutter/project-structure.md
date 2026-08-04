# Project Structure (Flutter)

Flutter apps scale best with feature ownership and a thin widget layer: widgets render state, and domain logic lives in services/controllers.

## When to load

- You are starting a new Flutter app or refactoring a messy `lib/`.
- You need boundaries between UI, domain, and platform adapters.

## When NOT to load

- You only need state patterns (`state-management.md`).
- You only need theming (`widgets-layout-and-theming.md`).

## Core rules

- Organize by feature; keep shared UI primitives separate.
- Keep screens/widgets thin; move logic into controllers/notifiers.
- Centralize platform adapters (permissions, storage, analytics) behind `lib/lib.dart` boundaries.
- Prefer composition over inherited global singletons.

## Minimal examples

Feature-first layout:

```text
lib/
  app/
    app.dart
    router.dart
  features/
    auth/
      ui/
      state/
      data/
    projects/
      ui/
      state/
      data/
  ui/
    button.dart
    text.dart
    theme.dart
  lib/
    http/
    storage/
    permissions/
```

## Anti-patterns

- `widgets/` as a dumping ground.
- Business logic inside `build()`.
- Platform checks sprinkled everywhere.

## Checklist

- Features have clear homes.
- UI primitives are shared and consistent.
- Domain logic is testable outside Flutter widgets.

# Project Structure (Dart)

Keep Dart projects easy to navigate: separate domain logic from IO, keep public surface area small, and avoid cyclic imports.

## When to load

- You are creating a new Dart package.
- You need a consistent layout for app vs library.
- You are refactoring a tangled `lib/` directory.

## When NOT to load

- You are building Flutter UI (use `../flutter/SKILL.md`).
- You only need testing (`testing.md`).

## Core rules

- Keep `lib/` as the public API and core modules.
- Expose a small public surface (avoid exporting everything).
- Put IO adapters (HTTP, file, device) behind interfaces.
- Avoid single giant `utils.dart`.

## Minimal examples

Package layout:

```text
lib/
  mypkg.dart          (public exports)
  src/
    domain/
    adapters/
    services/
test/
analysis_options.yaml
pubspec.yaml
```

## Anti-patterns

- Importing from `lib/src` across packages.
- Tight coupling between domain and IO.
- Everything exported from the top-level library.

## Checklist

- Public API is small.
- Domain is testable without IO.
- Imports are acyclic.

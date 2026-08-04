# Navigation and Routing

Navigation should be predictable and typed: stable routes, validated params, and a single router configuration.

## When to load

- You are adding navigation, deep links, or typed route params.
- You are choosing between Navigator 2.0 and a router package.
- You need back behavior rules.

## When NOT to load

- You only need state (`state-management.md`).
- You only need platform UX (`platform-ux-ios-android.md`).

## Core rules

- Define routes in one place.
- Validate incoming params (deep links).
- Use predictable back behavior; avoid surprise pops.
- Keep navigation events out of domain logic.

## Minimal examples

Typed params object:

```dart
class ProjectRoute {
  const ProjectRoute(this.id);
  final String id;
}
```

Deep link validation posture:

```text
parse -> validate -> route
reject/redirect on invalid params
```

## Anti-patterns

- Passing huge objects through route args.
- Multiple navigation systems used in parallel.
- Unvalidated dynamic routes.

## Checklist

- Routes centralized.
- Params validated.
- Back behavior tested on Android.

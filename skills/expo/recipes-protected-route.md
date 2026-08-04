# Recipe: Protected Route (Expo Router)

Use this when you need an authenticated route group with a consistent redirect behavior.

## When to load

- You are protecting a route group.
- You need a repeatable auth gate pattern.

## When NOT to load

- You are designing auth mechanisms (use `../auth/SKILL.md`).
- You are using non-Expo navigation (use `../react-native/navigation.md`).

## Core rules

- Put auth gating at the layout level for the route group.
- Keep auth state and navigation wiring separate.
- Fail closed: unauthenticated routes redirect to login.

## Minimal examples

Route group posture:

```text
app/
  (auth)/login.tsx
  (app)/_layout.tsx  <- gate here
```

## Anti-patterns

- Protecting routes ad-hoc inside every screen.
- Redirect loops due to ambiguous auth state.

## Checklist

- Gate exists in group layout.
- Unauthenticated behavior consistent.
- No redirect loops.

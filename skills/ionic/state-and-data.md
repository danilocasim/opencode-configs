# State and Data

Ionic apps are still web apps: keep client state predictable, and treat server data as cacheable state with explicit invalidation.

## When to load

- You are choosing a state approach.
- You are integrating API calls and caching.
- You need offline-first posture.

## When NOT to load

- You only need UI patterns (`ui-components-and-patterns.md`).
- You are doing native release/signing (`../capacitor/SKILL.md`).

## Core rules

- Separate UI state (local) from server state (cached).
- Prefer one server-state library per app (TanStack Query is a common choice).
- Keep API clients typed and centralized.
- Make auth error handling consistent (401 -> signed out).
- If offline matters, define what works offline and what doesn't.

## Minimal examples

Server-state posture:

```text
query keys reflect domain
mutations invalidate the right keys
errors map to stable UI states
```

## Anti-patterns

- Global state for everything.
- Ad-hoc fetch calls spread across many components.
- No invalidation strategy.

## Checklist

- Server state strategy chosen.
- API client centralized.
- Auth errors handled consistently.
- Offline expectations defined.

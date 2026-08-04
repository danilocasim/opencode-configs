# Testing (Ionic)

Test most behavior at the web layer, and keep a small set of device smoke tests for Capacitor wiring (push, deep links, permissions).

## When to load

- You are adding tests to an Ionic app.
- You need a strategy for device-only failures.
- You are choosing unit vs e2e scope.

## When NOT to load

- You only need general testing philosophy (use `../testing/SKILL.md`).
- You are doing native-only testing.

## Core rules

- Unit tests for pure logic.
- Component tests for UI interactions.
- E2E tests for critical flows.
- Device smoke suite for Capacitor-only behavior.

## Minimal examples

Pyramid:

```text
unit (fast)
component (medium)
e2e (few)
device smoke (fewest)
```

## Anti-patterns

- E2E for everything.
- No device verification.
- Real network calls in unit tests.

## Checklist

- Web tests cover most behavior.
- Device smoke tests cover wiring.
- CI deterministic.

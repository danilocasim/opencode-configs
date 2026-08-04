# Debugging and Devtools

Mobile debugging is a workflow: reproduce on device, inspect logs, isolate Metro/build issues, and reduce variables.

## When to load

- The app behaves differently on device vs simulator.
- You have Metro bundler issues.
- You need patterns for logging and debugging network/storage.

## When NOT to load

- You are doing observability for production services (use `../observability/SKILL.md`).
- You are only formatting/linting.

## Core rules

- Reproduce on a real device for keyboard, performance, permissions.
- Capture both JS logs and native logs.
- When stuck: clear caches and rebuild deterministically.
- Avoid adding noisy logs; use structured, scoped debugging.
- Keep a "known good" environment baseline.

## Minimal examples

Debug flow:

```text
repro -> isolate -> logs -> hypothesis -> minimal change -> verify
```

## Anti-patterns

- Debugging only in simulator.
- Random cache-clearing without capturing evidence.
- Making many changes before verifying.

## Checklist

- Repro on device.
- Logs captured.
- Minimal fix verified.
- Regression prevented.

# Recipe: Debug a Production Issue

Use this when the system is on fire. The goal is fast containment, then diagnosis, then a safe fix.

## When to load

- You are triaging an incident.
- You need a step-by-step debugging loop.

## When NOT to load

- You are writing a postmortem (use incident-response once it exists).
- You are doing performance tuning without an incident.

## Core rules

- Start with symptoms and scope (who is affected?).
- Use correlation IDs to trace a failing request.
- Check recent deploys and config changes.
- Mitigate first when user impact is ongoing.
- Preserve evidence (logs/metrics) before restarting.

## Minimal examples

Triage loop:

```text
1) identify impact + timeframe
2) locate failing route/job
3) trace one request end-to-end
4) confirm hypothesis with metrics/logs
5) mitigate (rollback/feature flag)
6) fix + verify
```

## Anti-patterns

- Restarting blindly and losing evidence.
- Debugging without a scoped hypothesis.
- Making multiple changes at once.

## Checklist

- Impact understood.
- One request traced end-to-end.
- Mitigation applied if needed.
- Fix verified and monitored.

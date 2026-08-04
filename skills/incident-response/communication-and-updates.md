# Communication and Updates

Clear comms reduce chaos. Communicate impact, mitigation, and expected next updates with honest uncertainty.

## When to load

- You need a status update cadence.
- You are writing internal or customer-facing updates.
- You need rules for what not to say.

## When NOT to load

- You are writing the postmortem (`postmortems-and-followups.md`).
- You are implementing monitoring/alerts.

## Core rules

- State impact, scope, and current mitigation.
- Provide next update time.
- Avoid guessing root cause early.
- Keep a running timeline of events.
- Use one channel/source of truth.

## Minimal examples

Update template:

```text
Status: investigating/degraded/mitigated
Impact: who/what is affected
Mitigation: what we did
Next update: time
```

## Anti-patterns

- Overconfident root cause claims.
- No update cadence.
- Multiple conflicting sources of truth.

## Checklist

- Impact described.
- Mitigation described.
- Next update time set.
- Timeline maintained.

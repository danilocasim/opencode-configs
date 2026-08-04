# Recipe: Incident Template

Use this to create a consistent incident doc or Slack update thread.

## When to load

- You are declaring an incident.
- You need a standard structure for updates.

## When NOT to load

- You are writing the postmortem (`postmortems-and-followups.md`).
- You are investigating with traces/logs.

## Core rules

- Keep the template short and updated.
- One source of truth.
- Record decisions and mitigations with timestamps.

## Minimal examples

Template:

```text
Title:
Status:
Impact:
Start time:
Owner:
Mitigation:
Next update:
Links:
Timeline:
```

## Anti-patterns

- Long narratives during active mitigation.
- No timestamps.
- No owner.

## Checklist

- Owner assigned.
- Impact stated.
- Update cadence set.
- Timeline started.

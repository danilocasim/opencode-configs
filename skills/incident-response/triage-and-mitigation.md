# Triage and Mitigation

Triage is about speed and scope. Mitigation is about reducing impact safely before you fully understand the root cause.

## When to load

- A service is down or degraded.
- Errors or latency are spiking.
- You need a structured triage loop.

## When NOT to load

- You are writing a postmortem (`postmortems-and-followups.md`).
- You are doing routine debugging (`../observability/SKILL.md`).

## Core rules

- Establish impact (who/what/when) before diving into logs.
- Identify the failing surface (route/job/dependency).
- Prefer reversible mitigations (feature flags, rate limits).
- Preserve evidence before restarts.
- Assign roles (incident lead, comms, ops) when needed.

## Minimal examples

Triage loop:

```text
impact -> scope -> suspect changes -> mitigate -> diagnose -> fix -> verify
```

## Anti-patterns

- Restarting repeatedly without a hypothesis.
- Making multiple changes at once.
- Debugging without confirming user impact.

## Checklist

- Impact and scope recorded.
- Mitigation applied if needed.
- Evidence preserved.
- Fix verified and monitored.

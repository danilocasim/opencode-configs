# Metrics and SLOs

Metrics tell you if the system is healthy; SLOs tell you what “healthy enough” means. Alerts should wake humans only for actionable issues.

## When to load

- You are defining SLIs/SLOs.
- You are adding metrics instrumentation.
- You are creating or tuning alerts.

## When NOT to load

- You are debugging a single request path (use tracing/logs).
- You are doing performance profiling (use `../performance/SKILL.md` once it exists).

## Core rules

- Prefer a small set of golden signals: latency, traffic, errors, saturation.
- Define SLIs that map to user experience.
- Set SLOs and error budgets; alert on burn rate.
- Avoid per-host alert spam; alert on service-level symptoms.
- Always include runbook links and ownership.

## Minimal examples

Golden signals (service level):

```text
latency: p95/p99
errors: 5xx rate
traffic: req/s
saturation: CPU/memory/queue depth
```

## Anti-patterns

- Alerts on every spike with no context.
- No SLOs, only ad-hoc thresholds.
- Metrics without labels that support debugging.

## Checklist

- SLIs defined.
- SLOs and error budgets set.
- Alerts are actionable and low-noise.
- Runbooks linked.

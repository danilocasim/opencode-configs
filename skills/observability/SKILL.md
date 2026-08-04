---
name: observability
description: Practical observability playbooks (logs, metrics, tracing, alerting) for debugging and reliability
---

# Observability Skill Router

Use this when you need to understand what a system is doing in production: structured logs, correlation IDs, metrics/SLIs, tracing, and error tracking.

## When to load

- You are investigating a production issue.
- You are adding logging/metrics/tracing.
- You are defining alerts or SLOs.

## When NOT to load

- You are implementing app logic and only need tests (use `../testing/SKILL.md`).
- You are doing infra-only CI/container work (use `../devops/SKILL.md`).

## Routing table

| If the task is about...                | Load file                              |
| -------------------------------------- | -------------------------------------- |
| Structured logging and correlation IDs | `logging-and-correlation-ids.md`       |
| Metrics, SLIs/SLOs, and alert hygiene  | `metrics-and-slos.md`                  |
| Distributed tracing and spans          | `tracing-and-spans.md`                 |
| Error tracking and release health      | `error-tracking-and-release-health.md` |
| Recipe: debug a production issue       | `recipes-debug-prod-issue.md`          |

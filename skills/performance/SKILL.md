---
name: performance
description: Performance playbooks for measuring, profiling, caching, and reducing latency without guesswork
---

# Performance Skill Router

Use this when you need to make something faster in a measurable way: define a baseline, find the bottleneck, fix the highest-leverage path, and verify.

## When to load

- You are investigating slow pages/endpoints/jobs.
- You need profiling and measurement discipline.
- You are adding caching or performance budgets.

## When NOT to load

- You are primarily fixing correctness bugs (write tests first).
- You only need DB index/migration guidance (use `../database/SKILL.md`).

## Routing table

| If the task is about...             | Load file                       |
| ----------------------------------- | ------------------------------- |
| Measurement and profiling workflow  | `profiling-and-measurement.md`  |
| Caching strategies and invalidation | `caching-strategies.md`         |
| Latency budgets and p95/p99 focus   | `latency-budgets-and-p99.md`    |
| Backend hot paths (DB, queues)      | `backend-hot-paths.md`          |
| Recipe: performance investigation   | `recipes-perf-investigation.md` |

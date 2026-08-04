# Backend Hot Paths

Backend latency is usually DB + external IO + serialization. Fix the hottest path first and keep correctness intact.

## When to load

- An API endpoint is slow under load.
- Jobs are backing up due to slow processing.
- You suspect DB bottlenecks or excessive fan-out.

## When NOT to load

- You are making schema/index changes (use `../database/SKILL.md`).
- You are optimizing frontend rendering (use framework skills).

## Core rules

- Reduce round trips (batch queries, preloads).
- Avoid N+1.
- Add indexes based on observed queries.
- Bound external calls (timeouts, concurrency limits).
- Reduce payload sizes.

## Minimal examples

Common fixes:

```text
N+1 -> preload/join
slow query -> index + query rewrite
external IO -> timeout + retry + circuit breaker
```

## Anti-patterns

- Adding caching without fixing the query shape.
- Over-parallelizing outbound calls.
- Optimizing serialization while DB dominates.

## Checklist

- Slowest contributor identified.
- Query count reduced.
- Outbound calls bounded.
- Improvement verified.

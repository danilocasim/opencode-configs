# Latency Budgets and p99

Users feel tail latency. Set budgets, measure p95/p99, and design for the slowest dependency.

## When to load

- You are setting performance targets.
- You are diagnosing tail latency spikes.
- You need a budget for a multi-hop request.

## When NOT to load

- You are doing caching design (`caching-strategies.md`).
- You are doing measurement setup (`profiling-and-measurement.md`).

## Core rules

- Define end-to-end budgets (UI -> API -> DB).
- Break budget down per hop.
- Watch p95/p99 and error rates together.
- Protect with timeouts and fallbacks.
- Prefer fewer network hops.

## Minimal examples

Budget breakdown (conceptual):

```text
end-to-end p95: 300ms
DB: 50ms
external API: 100ms (timeout 250ms)
server CPU: 50ms
buffer: 100ms
```

## Anti-patterns

- Only tracking average latency.
- No timeouts on external calls.
- Unlimited fan-out calls.

## Checklist

- Budget defined.
- Timeouts in place.
- Tail latency monitored.
- Bottlenecks mapped to layers.

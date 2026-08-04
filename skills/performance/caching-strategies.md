# Caching Strategies

Caching is correctness with a time dimension. Define invalidation first, then choose where to cache.

## When to load

- You are adding caching to a hot path.
- You need an invalidation strategy.
- You are choosing between client/server/CDN caching.

## When NOT to load

- You need profiling discipline (`profiling-and-measurement.md`).
- You are fixing data correctness issues.

## Core rules

- Cache the smallest stable unit you can invalidate.
- Prefer explicit keys/tags.
- Add TTLs as a safety net, not as primary correctness.
- Never cache per-user data in shared caches without partitioning.
- Measure hit rate and staleness impact.

## Minimal examples

Cache design questions:

```text
what is the key?
what invalidates it?
what is the max staleness?
who can see cached data?
```

## Anti-patterns

- Adding caching to hide an N+1 problem.
- Caching without invalidation.
- Shared caching of user-specific responses.

## Checklist

- Invalidation defined.
- Keys partitioned correctly.
- TTL chosen deliberately.
- Metrics exist (hit rate, latency).

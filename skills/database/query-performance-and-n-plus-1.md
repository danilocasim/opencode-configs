# Query Performance and N+1

Most “performance” issues are query-shape issues: too many round trips (N+1), missing indexes, or fetching too much data.

## When to load

- You see N+1 queries or excessive query counts.
- A page/endpoint is slow due to DB time.
- You need a process for measuring query plans.

## When NOT to load

- You are choosing pagination semantics (use `../api/SKILL.md`).
- You are writing migrations (`migrations-and-backfills.md`).

## Core rules

- Measure first (query count, total time, slowest queries).
- Fix N+1 by preloading/joins or reshaping reads.
- Select only needed columns for hot paths.
- Add indexes based on observed queries.
- Prefer deterministic ordering for pagination.

## Minimal examples

N+1 smell:

```text
1 query to load 50 projects
50 queries to load each owner
```

Fix pattern:

```text
load projects with owners in one query (join/preload)
```

## Anti-patterns

- “Caching” around a slow query without understanding the plan.
- Adding indexes without confirming the query uses them.
- Loading entire rows/graphs when only IDs are needed.

## Checklist

- Query count and slowest queries measured.
- N+1 eliminated on the hot path.
- Indexes added only when they serve the query.
- Payload size reduced where possible.

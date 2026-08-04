# Indexes and Query Patterns

Indexes exist to serve your actual query patterns. Add them intentionally, measure them, and keep them aligned with your filters/sorts.

## When to load

- You are adding a new index.
- You changed a query (new filter/sort) and performance regressed.
- You need a rule for composite index ordering.

## When NOT to load

- You are doing a migration rollout plan (`migrations-and-backfills.md`).
- You are debugging N+1 in an ORM layer (`query-performance-and-n-plus-1.md`).

## Core rules

- Index the columns you filter on, then the columns you sort on.
- Use composite indexes for common multi-column filters.
- Keep indexes minimal; every index slows writes.
- Add uniqueness constraints at the DB when correctness depends on it.
- Validate with `EXPLAIN` (or query plan tooling) after changes.

## Minimal examples

Composite index for `WHERE owner_id = ? ORDER BY created_at DESC`:

```sql
CREATE INDEX projects_owner_created_at_idx ON projects (owner_id, created_at DESC);
```

Unique constraint for idempotency key:

```sql
CREATE UNIQUE INDEX idempotency_keys_unique ON idempotency_keys (key);
```

## Anti-patterns

- Indexing every column “just in case”.
- Relying on application-level uniqueness only.
- Composite index with columns in the wrong order for the query.

## Checklist

- Index matches an observed query pattern.
- Composite index column order matches filters/sorts.
- Write amplification considered.
- Plan verified with `EXPLAIN`.

# Recipe: Online Schema Change (Expand/Contract)

Use this when you need a safe, deployable sequence to add/change a column without downtime.

## CRITICAL: Data Preservation Rule

**NEVER suggest dropping, resetting, or destroying a database as the first or primary solution.** Diagnose the specific failure, fix or skip the broken migration, and resolve incrementally. Database destruction is an absolute last resort requiring explicit user consent. See `migrations-and-backfills.md` for the full rule.

## When to load

- You are rolling out a new column or changing how data is stored.
- You need a repeatable migration/backfill plan.

## When NOT to load

- You only need indexing (`indexes-and-query-patterns.md`).
- You only need transaction rules (`transactions-and-consistency.md`).

## Core rules

- Expand: add new nullable column(s), add new indexes.
- Dual-write: deploy app that writes both old and new fields.
- Backfill: run a resumable batch job to populate new field.
- Switch reads: deploy app reading from new field.
- Contract: drop old field / add NOT NULL / add constraints.

## Minimal examples

Sequence (high level):

```text
deploy 1: add column
deploy 2: dual write
backfill: batches + resume cursor
deploy 3: read new
deploy 4: contract
```

## Anti-patterns

- Dropping or resetting the database instead of following the expand/contract sequence.
- Doing expand + backfill + contract in one deploy.
- Backfills that cannot be paused/resumed.
- Adding strict constraints before the data is ready.

## Checklist

- Deploy sequence planned.
- Dual-write window defined.
- Backfill is safe and resumable.
- Contract step happens only after verification.

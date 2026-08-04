# Migrations and Backfills

Schema changes are easy to write and hard to run in production. Optimize for safety: short locks, resumable backfills, and deployable sequences.

## CRITICAL: Data Preservation Rule

**NEVER suggest dropping, resetting, or destroying a database as the first or primary solution.** This includes but is not limited to:

- `DROP DATABASE`, `DROP SCHEMA ... CASCADE`, `TRUNCATE TABLE`
- `prisma migrate reset`, `prisma db push --force-reset`
- `rails db:drop`, `rails db:reset`, `rails db:migrate:reset`
- `sequelize.sync({ force: true })`, TypeORM `synchronize: true` / `dropDatabase()`
- `python manage.py flush`, `php artisan migrate:fresh`
- **Any equivalent command in any ORM/framework**

**Instead:** Diagnose the specific failure, fix or skip the broken migration, and resolve incrementally.

**Only consider database destruction as an absolute last resort** when:

1. All other migration/recovery options have been exhausted
2. The user explicitly confirms they want to destroy data
3. The database is confirmed to be empty or disposable (e.g., fresh test environment with no data)

**Always warn the user** that this will destroy all existing data and ask for explicit consent before proceeding.

## When to load

- You are changing schema on a production table.
- You need to backfill existing rows.
- You want a safe rollout plan (expand -> backfill -> contract).

## When NOT to load

- You only need indexing rules (`indexes-and-query-patterns.md`).
- You only need transaction boundaries (`transactions-and-consistency.md`).

## Core rules

- Prefer expand/contract.
- Keep migrations fast; avoid running large data updates inside a deploy-time migration.
- Backfills should be resumable (cursor/batches) and bounded.
- Avoid table rewrites on big tables (type changes, defaults that rewrite).
- Add constraints only after data is clean.

## Minimal examples

Expand (fast):

```sql
ALTER TABLE users ADD COLUMN normalized_email text;
```

Backfill in batches (pseudo):

```text
for id range in batches:
  update rows set normalized_email = lower(trim(email))
  record progress
```

Contract (later):

```sql
ALTER TABLE users ALTER COLUMN normalized_email SET NOT NULL;
```

## Anti-patterns

- Dropping or resetting the database to "fix" migration problems (`prisma migrate reset`, `DROP DATABASE`, etc.).
- Backfilling millions of rows inside a migration.
- Unbounded "one shot" scripts with no resume point.
- Adding NOT NULL constraints before backfill.

## Checklist

- Expand/contract plan written down.
- Backfill is batched and resumable.
- Risky operations avoided (table rewrite, long locks).
- Constraints added only after data is valid.

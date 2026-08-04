---
name: database
description: Database patterns for migrations, indexing, transactions, and performance
---

# Database Skill Router

Use this skill when schema, query patterns, or transactional boundaries matter. The goal is correctness first, then performance, without risky production operations.

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

- You are writing a migration/backfill.
- You are adding indexes or changing query patterns.
- You need a transaction boundary for multi-step invariants.
- You are debugging slow queries or N+1 behavior.

## When NOT to load

- You are designing API contracts (use `../api/SKILL.md`).
- You are doing framework-only refactors without DB behavior changes.

## Routing table

| If the task is about...                        | Load file                           |
| ---------------------------------------------- | ----------------------------------- |
| Safe migrations and data backfills             | `migrations-and-backfills.md`       |
| Indexing by query patterns                     | `indexes-and-query-patterns.md`     |
| Transaction boundaries and consistency         | `transactions-and-consistency.md`   |
| Query performance and avoiding N+1             | `query-performance-and-n-plus-1.md` |
| Recipe: online schema change (expand/contract) | `recipes-online-migration.md`       |

## Typical load combos

- New column rollout: `migrations-and-backfills.md` + `recipes-online-migration.md`
- Slow endpoint: `query-performance-and-n-plus-1.md` + `indexes-and-query-patterns.md`

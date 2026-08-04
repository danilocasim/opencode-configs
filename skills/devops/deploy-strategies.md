# Deploy Strategies

Deploys are changes under load. Choose a rollout strategy that matches your risk tolerance and observability.

## When to load

- You are planning a production rollout.
- You need a safe rollback strategy.
- You are adding migrations that require multi-deploy sequencing.

## When NOT to load

- You are writing the migration details (use `../database/migrations-and-backfills.md`).
- You are diagnosing app errors (use observability once available).

## Core rules

- Prefer small, frequent deploys.
- Use health checks and canaries when available.
- Rollbacks must be fast and tested.
- Coordinate schema changes with expand/contract.
- Avoid “big bang” feature flags without cleanup.

## Minimal examples

Common strategies:

```text
rolling
blue/green
canary
```

## Anti-patterns

- Shipping schema + backfill + contract in one deploy.
- No rollback plan.
- Deploying without monitoring signals.

## Checklist

- Rollout strategy chosen.
- Rollback path defined.
- DB changes coordinated.
- Health checks and alerts in place.

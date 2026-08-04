# Rollback and Feature Flags

Rollback is the safest mitigation when a change caused harm. Feature flags are useful when you can disable a surface without reverting all changes.

## When to load

- You need to decide between rollback and flag.
- You are preparing a safe rollback plan.
- You are designing flag hygiene.

## When NOT to load

- You are diagnosing root cause with traces/logs (`../observability/SKILL.md`).
- You are planning a deploy strategy (`../devops/deploy-strategies.md`).

## Core rules

- Prefer rollback when you suspect a recent deploy.
- Keep flags simple: boolean for surface enablement.
- Flags must have owners and cleanup dates.
- Don’t use flags to hide broken data migrations.
- Verify rollback/flag effects with metrics.

## Minimal examples

Decision guide:

```text
recent deploy suspected -> rollback
localized feature causing harm -> disable via flag
```

## Anti-patterns

- Permanent flags.
- Flags that change data model semantics.
- Rollback with schema incompatibility.

## Checklist

- Rollback path works.
- Flags have owners and cleanup.
- Observability confirms mitigation.

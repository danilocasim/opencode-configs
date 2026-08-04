# Authorization Models

Authorization should be explicit and testable. Decide your model early so permissions don’t become scattered if-statements.

## When to load

- You are adding roles/permissions.
- You need to decide between RBAC and ABAC.
- You want rules for “deny by default”.

## When NOT to load

- You are implementing session or token mechanics.
- You need framework-specific policy objects (use the framework skill).

## Core rules

- Deny by default.
- Keep authorization checks centralized (policy layer).
- Prefer coarse roles plus resource ownership checks for many apps.
- Avoid mixing authorization into data models.
- Test allow + deny paths for critical actions.

## Minimal examples

Common models:

```text
RBAC: roles -> permissions
ABAC: attributes (user/resource/context) -> decision
```

## Anti-patterns

- Authorization scattered across controllers/handlers.
- “Admin” checks without auditing the surface area.
- Using client-provided role claims without server verification.

## Checklist

- Model chosen (RBAC/ABAC/mixed).
- Central policy layer exists.
- Deny-by-default enforced.
- Tests cover allow/deny for key actions.

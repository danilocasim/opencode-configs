# Recipe: Protect an Endpoint

Use this when you need a consistent checklist for protecting an HTTP endpoint (web or API) with clear 401/403 behavior.

## When to load

- You are adding a protected API endpoint.
- You need a consistent unauthorized/forbidden response.

## When NOT to load

- You only need the envelope format (use `../api/errors-and-response-shapes.md`).
- You are implementing token mechanics (`token-auth.md`).

## Core rules

- Authenticate first (who is calling?).
- Authorize second (are they allowed?).
- Return 401 for unauthenticated, 403 for unauthorized.
- Avoid user enumeration in error messages.
- Log metadata only.

## Minimal examples

Decision flow:

```text
if no identity -> 401
else if not permitted -> 403
else -> handle request
```

## Anti-patterns

- Returning 404 to hide everything (inconsistent client behavior) without a policy.
- Performing side effects before authorization.
- Different auth logic per endpoint.

## Checklist

- 401/403 semantics correct.
- Authorization happens before side effects.
- Errors are consistent and non-leaky.
- Tests cover unauthenticated + unauthorized + success.

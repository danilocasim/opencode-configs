# Secrets and Logging

Secrets leak through logs, errors, and “helpful” debugging more often than through hacks. Build redaction in by default.

## When to load

- You are adding logging around auth, payments, or integrations.
- You are handling API keys, tokens, cookies, or credentials.
- You need a policy for what is safe to log.

## When NOT to load

- You are doing dependency updates (`dependency-hygiene.md`).
- You are designing HTTP retry behavior (`../api/idempotency-and-retries.md`).

## Core rules

- Never log secrets (tokens, passwords, session cookies, private keys).
- Prefer structured logs with allowlisted fields.
- Redact sensitive headers and query params by default.
- Errors returned to users must not include internals.
- Store secrets in a secret manager; rotate-able design.

## Minimal examples

Safe logging posture:

```text
log: request_id, user_id, route, status, latency
do NOT log: Authorization header, cookies, raw bodies
```

## Anti-patterns

- Logging full request/response bodies in production.
- Returning raw exception messages to clients.
- Copying secrets into config files.

## Checklist

- Sensitive fields are redacted.
- Logs are allowlist-based.
- User-facing errors are non-leaky.
- Secrets stored and rotated safely.

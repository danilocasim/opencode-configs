# Logging and Correlation IDs

Logs should answer: what happened, to whom, and why. Correlation IDs let you follow a request across services.

## When to load

- You are adding logging to an HTTP handler, job, or integration.
- You need a request ID / correlation ID strategy.
- You are reducing noisy logs.

## When NOT to load

- You need metrics and SLOs (`metrics-and-slos.md`).
- You are implementing error envelopes (use `../api/errors-and-response-shapes.md`).

## Core rules

- Prefer structured logs (JSON) with stable keys.
- Generate or propagate a correlation ID per request.
- Log allowlisted fields: request_id, user_id, route, status, latency.
- Redact secrets (auth headers, cookies, tokens).
- Log at boundaries: request start/end, external calls, retries, failures.

## Minimal examples

Log fields to standardize:

```text
request_id
route
method
status
latency_ms
user_id (if known)
error_code (if any)
```

## Anti-patterns

- Free-form strings with no keys.
- Logging raw request bodies.
- Different correlation IDs per layer.

## Checklist

- Correlation ID exists and is propagated.
- Logs are structured and stable.
- Sensitive fields redacted.
- Boundary events are logged.

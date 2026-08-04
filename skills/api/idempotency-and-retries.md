# Idempotency and Retries

Networks fail. If clients retry requests (or you retry internally), your API must behave predictably and avoid duplicate side effects.

## When to load

- You are implementing POST/PUT operations that may be retried.
- You need an idempotency key strategy.
- You are designing webhook endpoints.

## When NOT to load

- You are focused on response envelopes (`errors-and-response-shapes.md`).
- You are working on DB migrations (use `../database/SKILL.md`).

## Core rules

- Support an `Idempotency-Key` for unsafe operations (typically POST).
- Store the key + request fingerprint + result for a bounded TTL.
- Return the same result for the same key (or a clear conflict).
- Retry only safe operations unless you have idempotency.
- Timeouts should be explicit; clients should handle them with backoff.

## Minimal examples

Request header:

```text
Idempotency-Key: 7b4b7b5d-0c62-4ec0-9c5e-4e6e9b6ef0f1
```

Behavior:

- first request executes and stores `{ key, fingerprint, response }`
- retry with same key returns stored response
- retry with same key but different payload returns `409 conflict`

## Anti-patterns

- Retrying writes without idempotency.
- Accepting idempotency keys but not storing responses.
- Infinite key retention (unbounded storage).

## Checklist

- Idempotency key supported where duplicates are harmful.
- Key storage has TTL.
- Conflicts are detected and mapped to 409.
- Clients have documented retry guidance.

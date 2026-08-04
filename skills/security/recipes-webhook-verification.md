# Recipe: Webhook Verification

Use this when receiving webhooks. The default failure mode for webhooks should be “reject” unless signature verification passes.

## When to load

- You are implementing a webhook endpoint.
- You need rules for signature verification and replay protection.

## When NOT to load

- You only need API envelopes (`../api/errors-and-response-shapes.md`).
- You are implementing outbound callbacks (`ssrf-and-outbound-http.md`).

## Core rules

- Verify signature using the provider’s shared secret.
- Use raw request body for verification (before JSON parsing).
- Enforce a timestamp window to prevent replay.
- Treat verification failure as 400/401.
- Log only metadata, not payloads.

## Minimal examples

Checklist (provider-agnostic):

```text
read raw body
read signature + timestamp headers
compute expected signature
compare in constant time
reject outside allowed time window
```

## Anti-patterns

- Parsing JSON first, then verifying (breaks signature).
- Logging the raw payload in production.
- Accepting requests with missing/invalid signatures.

## Checklist

- Raw body is used for signature verification.
- Timestamp window enforced.
- Constant-time compare.
- Failure returns 400/401.

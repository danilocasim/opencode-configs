# Error Tracking and Release Health

Error tracking is for finding unknown unknowns: exceptions, crashes, and regressions tied to releases.

## When to load

- You are adding error tracking (Sentry or similar).
- You need rules for grouping, fingerprints, and alerting.
- You are correlating a regression with a release.

## When NOT to load

- You need request-level debugging (use logs/tracing).
- You are handling secrets (use `../security/secrets-and-logging.md`).

## Core rules

- Capture release/version in every event.
- Add user identifiers carefully (hashed/IDs, not emails if sensitive).
- Tag with request_id and environment.
- Avoid sending secrets or full payloads.
- Create alerts on new issues and regressions, not on noise.

## Minimal examples

Event metadata to include:

```text
release
environment
request_id
route
error_code
```

## Anti-patterns

- Shipping without release tags.
- PII and secrets in error payloads.
- Alerting on every exception without filtering.

## Checklist

- Release health is visible.
- Sensitive data scrubbed.
- Alerts focus on regressions.
- Events include correlation IDs.

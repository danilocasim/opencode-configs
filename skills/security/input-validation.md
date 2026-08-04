# Input Validation

Security starts at the boundary. Treat all user-controlled input as hostile until validated and normalized.

## When to load

- You are parsing HTTP bodies, query params, headers, env vars, or CLI args.
- You need guidance for allowlists vs denylists.
- You are designing validation errors.

## When NOT to load

- You primarily need API envelopes (`../api/errors-and-response-shapes.md`).
- You need SSRF guidance (`ssrf-and-outbound-http.md`).

## Core rules

- Validate and normalize at the boundary (before business logic).
- Prefer allowlists (enums/known keys) over denylists.
- Bound sizes: string length, array length, payload size.
- Reject unknown fields for write endpoints unless you explicitly support them.
- Use typed parsing (numbers, dates) and handle failures explicitly.

## Minimal examples

Rules to apply:

```text
1) parse -> 2) validate -> 3) normalize -> 4) call domain
```

Allowlist example (pseudo):

```text
allowed_sort = {"created_at", "name"}
reject if sort not in allowed_sort
```

## Anti-patterns

- Accepting arbitrary JSON and trusting downstream code to “deal with it”.
- Denylist regexes for complex formats (easy to bypass).
- No size limits (DoS vector).

## Checklist

- Boundary validation exists.
- Unknown fields handled intentionally.
- Sizes bounded.
- Errors are explicit and non-leaky.

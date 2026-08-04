# Recipe: Add a New Endpoint

Use this when you want a repeatable checklist for adding a new endpoint without drifting from the API contract.

## When to load

- You are adding a new endpoint.
- You need consistent error/status mapping.
- You need to update OpenAPI alongside code.

## When NOT to load

- You only need pagination rules (`pagination-filtering-sorting.md`).
- You are planning a breaking change (`versioning-and-deprecation.md`).

## Core rules

- Decide the success and error shapes first.
- Validate inputs at the boundary; return field errors for validation.
- Choose the correct status code for each failure class.
- Add OpenAPI docs + examples in the same change.
- Add tests at the smallest level that proves behavior.

## Minimal examples

Endpoint contract (sketch):

```text
POST /v1/projects
200 { ok: true, data: { id } }
422 { ok: false, error: { code: validation_failed, fields: { name } } }
401 unauthenticated
```

## Anti-patterns

- Implementing endpoint first and “documenting later”.
- Returning different envelopes than the rest of the API.
- Mixing validation and persistence errors into one generic 500.

## Checklist

- Success and error envelopes match the global contract.
- Input validation happens at the boundary.
- Status codes are consistent.
- OpenAPI updated with examples.
- Tests cover success and the primary failure modes.

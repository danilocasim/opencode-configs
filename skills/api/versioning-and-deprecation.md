# Versioning and Deprecation

Versioning exists to protect clients from breaking changes. Treat it as a process, not a header.

## When to load

- You are planning a breaking change.
- You need a deprecation policy.
- You want guidance for compatibility behavior.

## When NOT to load

- You are designing list endpoints (`pagination-filtering-sorting.md`).
- You are updating OpenAPI (`openapi-and-examples.md`).

## Core rules

- Prefer explicit versioning (`/v1/...`) or a single `X-Api-Version` header.
- Avoid breaking changes in-place.
- Add new fields freely; do not change meaning of existing fields.
- Deprecate with a timeline; communicate in docs and responses.
- Keep old versions running until clients migrate.

## Minimal examples

URL versioning:

```text
GET /v1/projects
GET /v2/projects
```

Deprecation headers:

```text
Deprecation: true
Sunset: Wed, 01 Oct 2026 00:00:00 GMT
Link: </docs/migrations/v2>; rel="deprecation"
```

## Anti-patterns

- Silent breaking changes.
- Reusing a field name with a new meaning.
- “We’ll just support both” with no migration plan.

## Checklist

- Versioning mechanism chosen and documented.
- Deprecation window defined.
- Backwards-compat plan exists for clients.

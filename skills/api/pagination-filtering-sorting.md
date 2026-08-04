# Pagination, Filtering, and Sorting

List endpoints are where APIs get stuck. Decide up front how to paginate, filter, and sort so clients can scale with you.

## When to load

- You are implementing a list/search endpoint.
- You need a cursor pagination contract.
- You want safe filtering and sorting rules.

## When NOT to load

- You are defining error envelopes (`errors-and-response-shapes.md`).
- You are doing OpenAPI documentation (`openapi-and-examples.md`).

## Core rules

- Prefer cursor pagination for large datasets.
- Make sort keys explicit; reject unknown sorts.
- Filters are explicit and typed; reject unknown filters.
- Return `next_cursor` (or `cursor`) when more results exist.
- Keep pagination parameters bounded (`limit` max).

## Minimal examples

Request:

```text
GET /v1/projects?limit=50&cursor=p_123&sort=-created_at&owner_id=u_1
```

Response:

```json
{
  "ok": true,
  "data": {
    "items": [{ "id": "p_124" }],
    "next_cursor": "p_124",
    "has_more": true
  }
}
```

## Anti-patterns

- Offset pagination on large tables (`page=9999`) with unstable ordering.
- Sorting by arbitrary column names from clients.
- Filters that accept free-form SQL-ish strings.

## Checklist

- Cursor contract documented and stable.
- Sort keys are whitelisted.
- Filter keys are whitelisted and typed.
- `limit` is bounded.

# Errors and Response Shapes

API consumers need contracts, not vibes. Use a consistent envelope so clients can handle errors without string-matching.

## When to load

- You are defining a response envelope.
- You need a stable error object and status-code mapping.
- You are standardizing errors across services.

## When NOT to load

- You only need pagination/filtering (`pagination-filtering-sorting.md`).
- You are documenting with OpenAPI (`openapi-and-examples.md`).

## Core rules

- Use one success shape and one error shape across the API.
- Prefer stable machine codes (`code`) over human strings.
- Keep `message` safe for users; keep internals out of responses.
- Map failures to status codes consistently (400/401/403/404/409/422/429/500).
- Include field-level errors for validation.

## Minimal examples

Recommended envelopes:

```json
{ "ok": true, "data": { "id": "p_123" } }
```

```json
{
  "ok": false,
  "error": {
    "code": "validation_failed",
    "message": "invalid input",
    "fields": { "name": "required" }
  }
}
```

Status code mapping (typical):

- `400` malformed request
- `401` unauthenticated
- `403` unauthorized
- `404` not found
- `409` conflict (state/version)
- `422` validation failed
- `429` rate limited
- `500` server error

## Anti-patterns

- Different error shapes per endpoint.
- Returning stack traces or internal exception messages.
- Using `200` for errors and encoding status in JSON only.
- Relying on free-form strings for client logic.

## Checklist

- Success envelope consistent across endpoints.
- Error object includes stable `code`.
- Field errors included for validation.
- Status codes align with failure types.

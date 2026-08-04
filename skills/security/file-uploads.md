# File Uploads

Uploads are attacker-controlled input. Make them boring: strict limits, safe storage, and content validation.

## When to load

- You are adding file uploads.
- You are generating thumbnails/previews.
- You are accepting user-provided documents.

## When NOT to load

- You only need boundary validation (`input-validation.md`).
- You are focused on outbound HTTP threats (`ssrf-and-outbound-http.md`).

## Core rules

- Enforce size limits at the edge and in the app.
- Validate content type using sniffing (not only filename/headers).
- Store uploads outside the web root; serve via signed URLs when possible.
- Use random object keys; do not trust filenames.
- Scan when required (compliance/high risk).

## Minimal examples

Policy:

```text
max_size=10MB
allowed_types={image/png,image/jpeg,application/pdf}
store in object storage with random key
```

## Anti-patterns

- Serving uploads directly from the same origin path without isolation.
- Trusting `Content-Type` header alone.
- Processing untrusted files with shell commands.

## Checklist

- Size and type allowlists exist.
- Storage is isolated.
- Filenames are not trusted.
- High-risk types have additional scanning/handling.

# Web Threats: CSRF and XSS

Cookie-based auth requires CSRF protection. Any user-controlled string in HTML/JS contexts can become XSS if not handled correctly.

## When to load

- You are using cookie sessions.
- You are adding HTML rendering or rich text.
- You are introducing “dangerous” rendering APIs.

## When NOT to load

- You are working on SSRF controls (`ssrf-and-outbound-http.md`).
- You are doing file uploads (`file-uploads.md`).

## Core rules

- CSRF: protect state-changing requests for cookie auth.
- Prefer same-site cookies + CSRF tokens for forms.
- XSS: escape outputs; avoid raw HTML injection.
- Treat rich text as untrusted; sanitize with a safe allowlist.
- Use Content Security Policy (CSP) when feasible.

## Minimal examples

CSRF rules (conceptual):

```text
state-changing request must include CSRF token bound to session
reject missing/invalid token
```

XSS rules:

```text
never build HTML by string concatenation with user input
```

## Anti-patterns

- Disabling CSRF middleware globally.
- Rendering user input with raw HTML APIs.
- Trusting “it came from our database”.

## Checklist

- CSRF protection enabled for cookie auth.
- User strings are escaped in HTML contexts.
- Rich text sanitized with an allowlist.
- CSP considered for high-risk surfaces.

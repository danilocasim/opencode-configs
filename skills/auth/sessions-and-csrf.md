# Sessions and CSRF

Cookie sessions are great for browsers, but they require CSRF protection for state-changing requests.

## When to load

- You are implementing cookie-based sessions.
- You need CSRF rules.
- You are protecting browser POST/PUT/PATCH/DELETE.

## When NOT to load

- You are building token auth for APIs (`token-auth.md`).
- You are implementing framework-specific middleware glue (use the framework skill).

## Core rules

- Use HTTP-only, secure cookies.
- Prefer `SameSite=Lax` (or `Strict` when possible).
- Enforce CSRF tokens for state-changing requests.
- Rotate session identifiers on privilege changes (login).
- Keep session contents minimal (store IDs, not user profiles).

## Minimal examples

Session cookie policy (conceptual):

```text
cookie: HttpOnly; Secure; SameSite=Lax
csrf: token required for POST/PUT/PATCH/DELETE
```

## Anti-patterns

- Disabling CSRF for convenience.
- Storing secrets in cookies.
- Using GET for state-changing actions.

## Checklist

- Cookie flags set (HttpOnly/Secure/SameSite).
- CSRF enforced on state changes.
- Session rotation on login.
- Session contents minimal.

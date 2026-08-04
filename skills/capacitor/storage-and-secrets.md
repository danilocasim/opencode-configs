# Storage and Secrets

Hybrid apps are not a secure enclave. Treat the JS bundle as public, and keep secrets server-side. For tokens, prefer secure storage and minimize lifetime.

## When to load

- You are storing auth tokens or session identifiers.
- You need a secure storage pattern.
- You are designing logout / token rotation behavior.

## When NOT to load

- You are designing auth models (use `../auth/SKILL.md`).
- You are handling logs/secrets policy (use `../security/secrets-and-logging.md`).

## Core rules

- Never ship long-lived secrets in the client.
- Prefer cookie sessions for web apps; for native WebView contexts, be explicit about how auth persists.
- Store sensitive tokens in a secure storage plugin (not `localStorage`).
- Clear tokens on logout and when auth errors indicate invalidation.
- Keep token scope minimal and rotate where possible.

## Minimal examples

Secure token storage wrapper (conceptual):

```text
Native secure storage for refresh token
In-memory access token
Refresh flow on 401
```

Web fallback:

```text
If not native, use cookie session or memory storage
```

## Anti-patterns

- Storing refresh tokens in `localStorage`.
- Logging tokens.
- Using never-expiring tokens.

## Checklist

- Sensitive values stored securely.
- Logout clears persisted state.
- Token rotation/expiry handled.
- No secrets in bundle.

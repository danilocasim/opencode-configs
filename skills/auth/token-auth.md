# Token Auth (API Keys, JWT)

Token auth is for non-browser clients. Keep tokens scoped, rotated, and verified explicitly.

## When to load

- You are implementing API key authentication.
- You are using JWTs or bearer tokens.
- You need guidance for rotation and revocation.

## When NOT to load

- You are building browser sessions (`sessions-and-csrf.md`).
- You are deciding API envelopes (`../api/SKILL.md`).

## Core rules

- Prefer opaque tokens with server-side lookup when revocation matters.
- If using JWTs, validate issuer/audience/expiry and rotate signing keys.
- Scope tokens to least privilege.
- Store only hashed API keys.
- Separate authentication (token valid) from authorization (token allowed).

## Minimal examples

API key posture:

```text
Authorization: Bearer <token>
server: hash(token) lookup -> principal -> permissions
```

## Anti-patterns

- Long-lived tokens with no rotation.
- Storing raw tokens in the database.
- Treating JWT decode as “validation” (must verify signature).

## Checklist

- Verification is explicit (signature/expiry/etc.).
- Tokens are scoped.
- Rotation and revocation story exists.
- Raw tokens are not stored.

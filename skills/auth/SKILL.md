---
name: auth
description: Authentication and authorization patterns (sessions, tokens, middleware) with safe defaults
---

# Auth Skill Router

Use this when implementing authentication (who are you?) and authorization (are you allowed?) across web apps and APIs.

## When to load

- You are adding login/session or token auth.
- You are protecting routes/endpoints.
- You need patterns for roles/permissions and least privilege.

## When NOT to load

- You only need API envelopes (use `../api/SKILL.md`).
- You only need framework-specific glue (use `../nextjs/SKILL.md` or `../rails/SKILL.md`).

## Routing table

| If the task is about...            | Load file                     |
| ---------------------------------- | ----------------------------- |
| Cookie sessions and CSRF           | `sessions-and-csrf.md`        |
| Token auth (API keys, JWT)         | `token-auth.md`               |
| Authorization (roles, permissions) | `authorization-models.md`     |
| Recipe: protect an endpoint        | `recipes-protect-endpoint.md` |

## Typical load combos

- Web app login: `sessions-and-csrf.md` + `authorization-models.md`
- API auth: `token-auth.md` + `authorization-models.md`

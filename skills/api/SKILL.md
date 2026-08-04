---
name: api
description: REST/OpenAPI conventions, error shapes, pagination, and versioning
---

# API Skill Router

Use this skill to design and implement stable HTTP APIs: predictable envelopes, explicit error contracts, pagination, versioning, and OpenAPI.

## When to load

- You are adding or changing an API endpoint.
- You need a consistent error contract across endpoints.
- You need pagination/filtering rules that won’t paint you into a corner.
- You are maintaining an OpenAPI spec.

## When NOT to load

- You are implementing authentication/session mechanisms (load `skills/auth/SKILL.md` once it exists).
- You are doing DB schema/migrations (use `../database/SKILL.md`).
- You are hardening against security threats (use `../security/SKILL.md`).

## Routing table

| If the task is about...                | Load file                         |
| -------------------------------------- | --------------------------------- |
| Error envelopes and status codes       | `errors-and-response-shapes.md`   |
| Pagination, filtering, sorting         | `pagination-filtering-sorting.md` |
| Versioning, deprecation, compatibility | `versioning-and-deprecation.md`   |
| OpenAPI and keeping specs in sync      | `openapi-and-examples.md`         |
| Idempotency and retries                | `idempotency-and-retries.md`      |
| Recipe: add a new endpoint             | `recipes-new-endpoint.md`         |

## Typical load combos

- New endpoint: `errors-and-response-shapes.md` + `recipes-new-endpoint.md`
- Listing endpoint: `pagination-filtering-sorting.md` + `errors-and-response-shapes.md`
- Backwards-compatible change: `versioning-and-deprecation.md`

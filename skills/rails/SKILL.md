---
name: rails
description: Ruby on Rails conventions (Rails 7.x/8.x, 2024-2026)
---

# Rails Skills Index

Routing index for Rails 7.x/8.x work, optimized for thin models/controllers and PORO architecture.

## Core architecture policy

- Controllers orchestrate request/response, not business rules.
- Models keep data invariants, not multi-step workflows.
- Complex behavior belongs in POROs: services, queries, form objects, policies, value objects.
- Concerns are for cohesive shared behavior, not cross-domain dumping grounds.

## Quick routing

| Task                                    | Load                            | Why                                   |
| --------------------------------------- | ------------------------------- | ------------------------------------- |
| Decide where logic should live          | `thin-mvc-architecture.md`      | Placement decision matrix             |
| Share model behavior safely             | `model-concerns.md`             | Concern boundaries and anti-patterns  |
| Keep controllers thin and composable    | `controller-concerns.md`        | Controller concerns and orchestration |
| Implement domain workflows or filtering | `service-and-query-objects.md`  | PORO patterns with contracts          |
| Map/validate params and persist safely  | `form-objects.md`               | Form objects for write workflows      |
| Authorization and PolicyScopes          | `pundit-policies.md`            | Pundit placement + policy contracts   |
| Avoid callback-driven business logic    | `callbacks-policy.md`           | When callbacks are acceptable         |
| Background jobs with idempotency        | `jobs-and-idempotency.md`       | Retry-safe jobs and enqueue rules     |
| Safe migrations and backfills           | `migrations-and-backfills.md`   | Zero-downtime DB changes              |
| API docs and internal commenting style  | `documentation-and-comments.md` | Rails-specific docs/comment standards |
| Write/structure tests                   | `../testing/ruby-rails.md`      | TDD + Rails test pyramid              |

## Where should this logic go?

| Use case                                         | Place it in        |
| ------------------------------------------------ | ------------------ |
| Validation/data invariant                        | Model              |
| Multi-step write workflow                        | Service object     |
| Reusable query/filter/sort                       | Query object       |
| Input mapping + validation + persistence         | Form object        |
| Shared model behavior within one bounded context | Model concern      |
| Shared controller plumbing (auth, pagination)    | Controller concern |
| Authorization                                    | Policy object      |
| Domain primitive (money, email, range)           | Value object       |

## When NOT to load this skill

- Pure Ruby library work without Rails runtime -> use `skills/ruby/SKILL.md`.
- Frontend-only React/Next.js UI work -> use `../react/SKILL.md` or `../nextjs/SKILL.md`.
- Generic API contract design -> use `../api/SKILL.md`.

## Related skills

- Documentation style: `../documentation/SKILL.md`
- Security checklist: `../security/SKILL.md`
- Database safety: `../database/SKILL.md`

## Reference docs

- Rails Guides: https://guides.rubyonrails.org/
- Rails API: https://api.rubyonrails.org/
- Rails Style Guide: https://rails.rubystyle.guide/

---
name: python
description: Python 3.12+ skill router for deterministic, strictly typed code (tools, services, agents)
---

# Python Skill Router

Load this first for Python work so you can route to a small focused guide instead of mixing conventions.

## When to load

- You are writing Python for tools, agents, microservices, or libraries.
- You need strict typing, deterministic behavior, and test-first defaults.
- You need a recommended modern toolchain (uv + ruff + pyright).

## When NOT to load

- You are building a FastAPI service and only need framework conventions -> load `../fastapi/SKILL.md`.
- You are designing REST API contracts -> load `../api/SKILL.md`.

## Routing table

| If the task is about...                      | Load                            |
| -------------------------------------------- | ------------------------------- |
| Project layout and import boundaries         | `project-structure.md`          |
| Type safety and boundary validation          | `types-and-boundaries.md`       |
| Error strategy (exceptions vs Result)        | `errors-and-results.md`         |
| Async IO, cancellation, bounded concurrency  | `async-and-concurrency.md`      |
| HTTP clients, timeouts, retries, idempotency | `http-clients-and-retries.md`   |
| Tooling (uv + ruff + pyright) and CI gates   | `tooling-and-quality.md`        |
| Docstrings and comment policy                | `documentation-and-comments.md` |
| Build an agent tool module                   | `recipes-agent-tool.md`         |
| Build a CLI tool                             | `recipes-cli-tool.md`           |
| Testing patterns for Python                  | `../testing/python.md`          |

## Typical load combos

- New Python module: `project-structure.md` + `tooling-and-quality.md` + `types-and-boundaries.md` + `errors-and-results.md`
- HTTP integration: `http-clients-and-retries.md` + `errors-and-results.md` + `types-and-boundaries.md`
- Async worker: `async-and-concurrency.md` + `errors-and-results.md` + `tooling-and-quality.md`

## Stop triggers (route out)

- Secrets, auth, SSRF, uploads, sandboxing -> `../security/SKILL.md`
- API envelopes, pagination, versioning, idempotency -> `../api/SKILL.md`
- DB schema/migrations/transactions -> `../database/SKILL.md`
- CI, containers, deploy -> `../devops/SKILL.md`

## Always adapt to existing repos

If the repo already has a toolchain (poetry, black, mypy, etc.), follow it.
Only introduce uv/ruff/pyright when you own the repo or when current tooling is missing.

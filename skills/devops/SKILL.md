---
name: devops
description: DevOps, CI/CD, and infrastructure conventions
---

# DevOps Skill Router

Use this when touching Dockerfiles, CI pipelines, deployment configs, or build reproducibility. The goal is fast, deterministic, secure delivery.

## When to load

- You are editing a Dockerfile or container build.
- You are changing CI behavior (lint/test/build, caching).
- You are touching deployment configs.
- You need a checklist for reproducible builds.

## When NOT to load

- You are designing API contracts (use `../api/SKILL.md`).
- You are doing app-level auth/session (use the stack skill).

## Routing table

| If the task is about...          | Load file                   |
| -------------------------------- | --------------------------- |
| Dockerfiles and image hardening  | `dockerfiles-and-images.md` |
| CI pipelines and reproducibility | `ci-pipelines.md`           |
| Secrets in CI/CD                 | `secrets-in-ci.md`          |
| Deployment strategies            | `deploy-strategies.md`      |
| Recipe: CI-like local checks     | `recipes-ci-checks.md`      |

## Default policy

- Fail fast (format/lint/type before tests/build).
- Cache safely (keyed by lockfiles).
- Don’t bake secrets into artifacts.

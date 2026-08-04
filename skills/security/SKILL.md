---
name: security
description: Security checklist and safe patterns across common stacks
---

# Security Skill Router

Use this when making security-sensitive changes or doing an audit. The goal is to prevent common classes of vulns by default: unsafe inputs, secret leakage, broken auth, SSRF, and unsafe uploads.

## When to load

- You are handling user-controlled input (HTTP, CLI, jobs, queues).
- You are touching auth/authz, sessions, or secrets.
- You are adding file uploads or outbound HTTP.
- You need a quick threat checklist for a change.

## When NOT to load

- You only need API envelope conventions (use `../api/SKILL.md`).
- You only need Docker/CI guidance (use `../devops/SKILL.md`).

## Routing table

| If the task is about...              | Load file                         |
| ------------------------------------ | --------------------------------- |
| Boundary validation and safe parsing | `input-validation.md`             |
| Secrets, logging, and redaction      | `secrets-and-logging.md`          |
| CSRF/XSS and common web threats      | `web-threats-csrf-xss.md`         |
| SSRF and outbound HTTP controls      | `ssrf-and-outbound-http.md`       |
| Safe file uploads                    | `file-uploads.md`                 |
| Dependency and supply-chain hygiene  | `dependency-hygiene.md`           |
| Recipe: verify a webhook             | `recipes-webhook-verification.md` |

## Universal checklist (quick)

- Validate inputs at boundaries.
- Do not log secrets.
- Deny by default (authz).
- Bound outbound HTTP (SSRF).
- Make uploads safe (size/type/isolation).

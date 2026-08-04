---
name: incident-response
description: Incident response playbooks: triage, mitigation, communication, and postmortems
---

# Incident Response Skill Router

Use this when production is degraded. The goal is to reduce user impact quickly, communicate clearly, and learn enough to prevent repeats.

## When to load

- You are on-call or responding to an incident.
- You need mitigation/rollback guidance.
- You need a postmortem template.

## When NOT to load

- You are debugging a single issue without user impact (use `../observability/SKILL.md`).
- You are doing normal feature work.

## Routing table

| If the task is about...    | Load file                       |
| -------------------------- | ------------------------------- |
| Triage and mitigation      | `triage-and-mitigation.md`      |
| Rollback and feature flags | `rollback-and-feature-flags.md` |
| Communication and updates  | `communication-and-updates.md`  |
| Postmortems and follow-ups | `postmortems-and-followups.md`  |
| Recipe: incident template  | `recipes-incident-template.md`  |

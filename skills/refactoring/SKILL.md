---
name: refactoring
description: Refactoring playbooks for safe change: seams, extraction patterns, and keeping behavior frozen with tests
---

# Refactoring Skill Router

Use this when you need to improve structure without changing behavior: shrink functions, extract boundaries, remove duplication, and keep risk controlled.

## When to load

- You are refactoring a risky area.
- You need a safe step-by-step approach.
- You are extracting services/modules.

## When NOT to load

- You are implementing a net-new feature without refactor pressure.
- You primarily need performance tuning (use `../performance/SKILL.md`).

## Routing table

| If the task is about...                | Load file                   |
| -------------------------------------- | --------------------------- |
| Safe refactor workflow                 | `refactor-workflow.md`      |
| Extracting a boundary (service/module) | `extract-boundaries.md`     |
| Removing duplication safely            | `remove-duplication.md`     |
| Naming and ownership rules             | `naming-and-ownership.md`   |
| Recipe: large refactor plan            | `recipes-large-refactor.md` |

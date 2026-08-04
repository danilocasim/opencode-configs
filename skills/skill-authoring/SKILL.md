---
name: skill-authoring
description: Standards and recipes for authoring high-signal skills and consistent codegen playbooks
---

# Skill Authoring

Use this skill to keep the skills repo "LLM-proof": predictable routing, consistent templates, and minimal-but-canonical examples.

## When to load

- You are creating a new skill directory or refactoring an existing skill.
- You are adding "recipes" to make code generation consistent.
- You are building QA/benchmarks to prevent skill drift.

## When NOT to load

- You are implementing application code in a specific stack (load the stack skill).

## Quick routing

| Task                               | Load                    | Why                                  |
| ---------------------------------- | ----------------------- | ------------------------------------ |
| Author skill routers and leaf docs | `authoring-standard.md` | Required sections + routing patterns |
| Add recipes/playbooks              | `recipes-standard.md`   | Recipe format + templates            |
| Add benchmark prompts              | `benchmarks.md`         | Regression harness for skills        |
| Validate skill quality             | `skills-lint.md`        | Lint rules + how to run              |

## Non-negotiables

- Router-first: every skill has `SKILL.md` with a routing table.
- Leaf docs are narrow and actionable: decision rules, checklists, anti-patterns.
- Every leaf includes `## Minimal examples` (1-3 canonical templates).
- "When NOT to load" must exist to prevent context bloat.
- Prefer placement rules over generic best-practice prose.

## OpenCode constraints (important)

- `SKILL.md` frontmatter only recognizes: `name`, `description`, `license`, `compatibility`, `metadata`.
- Skill `name` must match its folder name and be lowercase with hyphens.
- Skills are discovered at `~/.config/opencode/skills/<name>/SKILL.md` (global) and `.opencode/skills/<name>/SKILL.md` (project).

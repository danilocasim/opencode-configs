# Skill Authoring Standard

This is the canonical template for skill routers (`SKILL.md`) and leaf guides. Optimize for retrieval and consistent code generation.

## When to load

- You are creating or refactoring a skill directory.
- You are splitting a large doc into smaller leaf guides.
- You are adding routing tables and "don’t load" rules.

## When NOT to load

- You only need a recipe template (use `recipes-standard.md`).
- You only need benchmarks (use `benchmarks.md`).

## Core rules

- A skill directory must be `skills/<name>/SKILL.md`.
- `name` must match directory name and follow `^[a-z0-9]+(-[a-z0-9]+)*$`.
- Router docs (`SKILL.md`) are short and point to leaf docs.
- Leaf docs are narrow (one topic) and include canonical examples.
- Avoid "universal" advice that doesn’t change behavior.

## Common patterns

- Router contains:
  - A routing table (task -> file)
  - 3-5 typical load combos
  - Stop triggers routing to cross-cutting skills (security/db/api/testing)
  - Keywords/synonyms (so models choose the right leaf)
- Leaf contains:
  - Decision rules (if X then Y)
  - Anti-patterns (explicit "don’t")
  - Checklist (copy-ready)
  - Minimal examples (paths + templates)

## Minimal examples

Router skeleton (`skills/<name>/SKILL.md`):

```md
---
name: <name>
description: <1 sentence, specific>
---

# <Skill> Index

## When to load

- ...

## When NOT to load

- ...

## Routing table

| Task | Load      |
| ---- | --------- |
| ...  | `leaf.md` |

## Typical load combos

- ...

## Stop triggers

- ... -> load `../security/SKILL.md`

## Related skills

- ...
```

Leaf skeleton (`skills/<name>/<leaf>.md`):

````md
# <Leaf topic>

## When to load

- ...

## When NOT to load

- ...

## Core rules

- ...

## Common patterns

- ...

## Minimal examples

```text
<file paths and templates>
```
````

## Anti-patterns

- ...

## Checklist

- ...

## References

- ...

```

## Anti-patterns

- A single monolithic file that tries to answer everything.
- Missing "When NOT to load" (causes context bloat).
- Example-free leaf docs (weak models will improvise).
- Overly long examples that become non-transferable.

## Checklist

- Skill name matches folder name.
- Router routes to 1-2 leaf docs per task.
- Every leaf has `## Minimal examples`.
- Leaf docs stay under ~250-300 lines; split if larger.

## References

- OpenCode Agent Skills: https://opencode.ai/docs/skills/
```

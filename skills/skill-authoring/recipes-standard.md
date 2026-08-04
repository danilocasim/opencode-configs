# Recipes Standard

Recipes are the consistency engine: they turn guidance into repeatable, stack-specific moves.

## When to load

- You want codegen to be consistent across projects.
- You are adding a "vertical slice" playbook (endpoint, feature, job, migration).
- You want a canonical TDD-first workflow for a task.

## When NOT to load

- You are writing a generic skill leaf (use `authoring-standard.md`).

## Core rules

- One recipe = one outcome.
- Include a load list (router + leaf docs).
- Specify file paths and ownership rules.
- Be TDD-first by default.
- Include failure modes + anti-patterns.
- End with: test plan + commit message + PR body snippet.

## Common patterns

- Put recipes in the skill directory that owns the workflow:
  - Rails endpoint -> `skills/rails/recipes-endpoint.md`
  - Next.js mutation -> `skills/nextjs/recipes-server-action.md`
  - Testing bug fix -> `skills/testing/recipes-bug-fix.md`
- Keep recipes short; link to leaf docs for details.

## Minimal examples

Recipe skeleton:

````md
# Recipe: <Outcome>

## Goal

<one sentence>

## Load

- `SKILL.md`
- `<leaf>.md`
- `../testing/<stack>.md`

## Preconditions

- ...

## Files to touch

- `path/to/file`

## Steps (TDD-first)

1. ...

## Anti-patterns

- ...

## Test plan

- ...

## Commit message

- `feat(scope): ...`

## PR body (copy-ready)

```text
Why:
...
```
````

```

## Anti-patterns

- Recipes that don’t name files (models will place code randomly).
- Recipes with no test plan (TDD drift).
- Recipes that mix multiple outcomes.

## Checklist

- Load list is explicit.
- File paths are explicit.
- Includes at least one canonical example.
- Includes test plan + commit message.
```

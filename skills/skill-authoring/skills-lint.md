# Skills Linting

Skill linting keeps the repo consistent for retrieval and prevents "quiet" degradation as the skill tree grows.

## When to load

- You added/edited skills and want to validate structure.
- You want to enforce required sections and templates.
- You are debugging why skills are hard for an LLM to use.

## When NOT to load

- You only need to write a new leaf doc or recipe (use the relevant standard).

## Core rules

- Every skill directory must have `SKILL.md` with valid frontmatter.
- Every non-index leaf must include:
  - `## When to load`
  - `## When NOT to load`
  - `## Core rules`
  - `## Minimal examples`
  - `## Anti-patterns`
  - `## Checklist`
- Keep leaf docs small; split large ones.

## Common patterns

- Run linter locally before committing.
- Treat lint failures as a skills regression.

## Minimal examples

Run the linter:

```bash
python3 scripts/skills_lint.py
```

## Anti-patterns

- Adding new skills without a router.
- Adding leaf docs without examples.

## Checklist

- Linter passes.
- Router tables point to existing files.

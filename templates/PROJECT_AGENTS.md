# Project Rules

> IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning for any tasks.
> Before writing code, first explore the project structure, then invoke the skills, rules and standards for documentation.

> Copy this to your project root as `AGENTS.md` and customize.

## Skill Loading Protocol (Mandatory)

- Prefer project-local skills under `.opencode/skills/` (if present).
- If the repo does not define the needed skill(s), load the corresponding global skills from `~/.config/opencode/skills/`.
- Load router skill(s) first, then 1-2 relevant leaf docs.
- If behavior changes: load `testing` (and the stack test leaf).
- If public APIs change: load `documentation` (and the language doc style).

If no relevant project-local skills exist, do not block work; fall back to global skills.

## Testing Policy (TDD)

- Prefer TDD (red/green/refactor) for non-trivial behavior changes.
- Write a failing test first when feasible.
- Tests should cover success + primary failure paths.
- Always run tests after changes and fix failures immediately.

## Project Overview

<!-- Brief description of what this project does -->

## Tech Stack

<!-- List your technologies so the LLM knows what skills to load -->

- Language:
- Framework:
- Database:
- Testing:

## Project Structure

```
<!-- Document your directory structure -->
src/
tests/
```

## Conventions

<!-- Project-specific patterns that differ from global rules -->

### Naming

<!-- Any project-specific naming conventions -->

### File Organization

<!-- How files should be organized -->

### Patterns

<!-- Design patterns used in this project -->

## Commands

<!-- Common commands for this project -->

```bash
# Run tests
# Start dev server
# Build
# Lint
```

## Important Files

<!-- Key files the LLM should know about -->

- `src/config.ts` - Configuration
- `src/types.ts` - Shared types

## Gotchas

<!-- Things that might trip up the LLM -->

## Don'ts

<!-- Things to avoid in this project -->

- Don't use X, use Y instead
- Never commit Z

## Dependencies

<!-- Key dependencies and why they're used -->

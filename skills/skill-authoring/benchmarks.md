# Benchmarks Standard

Benchmarks are regression tests for your skill system. They prevent drift and quantify improvements.

## When to load

- You want to measure whether skills improve code generation.
- You are adding new skills or recipes and want to validate them.
- You want a stable set of prompts for evaluating weaker LLMs.

## When NOT to load

- You are writing a skill leaf or recipe template.

## Core rules

- Benchmarks must be deterministic: no repo-specific secrets, no external API calls.
- Each benchmark names:
  - prompt
  - expected skill loads (router + leaf)
  - expected output traits (structure + tests)
- Keep prompts realistic (what a dev would ask).

## Common patterns

- Use a small suite per stack:
  - Rails: endpoint + service extraction + migration
  - Next.js: server action + RSC boundary
  - Python: typed tool + pytest
  - Git: commit splitting and message
- Add a "weak model" variant: shorter prompt, less context.

## Minimal examples

Benchmark entry skeleton (markdown or json):

```text
Prompt: "Refactor this fat Rails controller action into a service object and add request + unit tests"
Expected loads:
- skills/rails/SKILL.md
- skills/rails/service-and-query-objects.md
- skills/testing/ruby-rails.md
Expected traits:
- controller stays orchestration-only
- service uses Result contract
- tests cover success + failure paths
```

## Anti-patterns

- Benchmarks that require external docs to interpret.
- Benchmarks that allow multiple architectures with no rubric.

## Checklist

- Expected loads are <= 3 files.
- Expected traits are measurable and structural.

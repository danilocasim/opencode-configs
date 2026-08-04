---
name: ruby
description: Ruby 3.x conventions, idioms, and best practices (2024-2026)
---

# Ruby Skill Router

Routing-first index for Ruby work. Load this to decide which focused guide to use
before writing code.

## When to load

- You are implementing pure Ruby business logic, gems, scripts, or POROs.
- You need Ruby 3.x defaults for naming, objects, errors, and tooling.
- You need the quickest route for tests/docs in Ruby or Ruby on Rails codebases.

## When NOT to load

- Rails-only architecture concerns -> load `../rails/SKILL.md` first.
- API contract design independent of Ruby runtime -> load `../api/SKILL.md`.
- Security hardening task -> load `../security/SKILL.md`.

## Core rules

- Route first, then implement: pick the smallest focused guide that fits.
- Prefer simple, explicit Ruby over metaprogramming-heavy designs.
- Keep behavior deterministic and easy to test.

## Patterns

- Core Ruby style/idioms -> `style-and-idioms.md`
- Object boundaries and composition -> `objects-and-design.md`
- Exceptions and result-object strategy -> `errors-and-results.md`
- RuboCop, type checks, CI quality gates -> `tooling-and-quality.md`
- YARD comments and pragmatic documentation -> `documentation-and-comments.md`
- Testing route -> `../testing/ruby-rails.md`
- Documentation route -> `../documentation/SKILL.md`

## Anti-patterns

- Loading every guide for a tiny change.
- Treating Rails conventions as defaults in non-Rails Ruby code.
- Using style rules without understanding trade-offs for readability.

## Checklist

- Identify scope: Ruby-only, Ruby+Rails, or cross-cutting concern.
- Open the one focused guide that matches the task.
- Use `../testing/ruby-rails.md` for tests and `../documentation/SKILL.md` for doc style.

## References

- Ruby docs: https://docs.ruby-lang.org/en/master/
- Ruby style guide: https://rubystyle.guide/
- RuboCop docs: https://docs.rubocop.org/

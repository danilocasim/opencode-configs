# Ruby Tooling and Quality

## When to load

- You are setting up or tuning linting, static checks, test gates, and CI.
- You need a practical default toolchain for Ruby 3.x projects.

## When NOT to load

- You are choosing object boundaries or domain architecture.
- You only need documentation comment format guidance.

## Core rules

- Keep one formatter/linter source of truth (`rubocop`).
- Run tests and lint in CI for every change.
- Fail fast on style, safety, and obvious code smells.
- Add type checks (`rbs`/`sorbet`) when project complexity warrants it.

## Patterns

- RuboCop with project-local config and minimal custom cops.
- RSpec or Minitest as existing project standard.
- Simple CI stages: lint -> test -> optional type check.
- Route tests via `../testing/ruby-rails.md`.

## Minimal examples

Local command loop:

```bash
bundle exec rubocop
bundle exec rspec
```

CI shape (conceptual):

```text
lint (rubocop) -> test (rspec/minitest) -> optional type checks (steep/sorbet/rbs)
```

## Anti-patterns

- Conflicting formatter stacks.
- Optional CI checks that silently allow regressions.
- Copy-pasting giant RuboCop configs without team buy-in.

## Checklist

- `rubocop` runs clean locally and in CI.
- Test command is documented and deterministic.
- Any type checker chosen has a clear adoption scope.

## References

- https://docs.rubocop.org/
- https://rspec.info/
- https://docs.ruby-lang.org/en/master/syntax_rdoc.html

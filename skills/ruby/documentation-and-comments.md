# Ruby Documentation and Comments

## When to load

- You are documenting Ruby public APIs and non-obvious behavior.
- You need comment guidance that stays concise and useful.

## When NOT to load

- You are primarily picking test strategy.
- You are working on architecture decisions unrelated to docs.

## Core rules

- Use YARD for public methods/classes/modules.
- Explain why and constraints before implementation details.
- Keep comments for intent, invariants, and caveats.
- Delete stale comments when behavior changes.

## Patterns

- YARD tags: `@param`, `@return`, `@raise`, `@example`.
- One short rationale line before complex logic.
- Document side effects (DB writes, network calls, retries).
- Route doc style decisions through `../documentation/SKILL.md`.

## Minimal examples

```ruby
# Normalize a user-supplied email.
#
# Why: we store canonical emails to avoid duplicate accounts due to casing/spacing.
#
# @param raw [String]
# @return [String]
# @raise [ArgumentError] if email is invalid
def normalize_email(raw)
  value = raw.to_s.strip.downcase
  raise ArgumentError, "invalid email" unless value.include?("@")

  value
end
```

## Anti-patterns

- Restating obvious code in comments.
- Missing error/side-effect docs on public APIs.
- Large narrative comments that drift from implementation.

## Checklist

- Public API has YARD docs with inputs/outputs/errors.
- Non-obvious decisions include concise rationale.
- Comments match current behavior after edits.

## References

- https://yardoc.org/
- https://rubystyle.guide/#comment-annotations
- `../documentation/SKILL.md`

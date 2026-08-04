# Rails Documentation and Comments

Document Rails code to preserve architectural intent: why logic is in concerns/POROs, what contracts exist, and where boundaries are enforced.

## When to load

- You are documenting services, queries, concerns, and public model/controller APIs.
- You changed architecture boundaries (moved logic from MVC into POROs).
- You are adding non-obvious callbacks, transactions, or side effects.

## When NOT to load

- The task is formatting/linting only with no behavior or boundary changes.
- Code is private, trivial, and obvious from naming.

## Core rules

- Explain WHY first: architectural placement and boundary decisions.
- Use YARD for public methods (`@param`, `@return`, `@raise`).
- State service/query contracts for inputs, outputs, and failure modes.
- Keep comments close to non-obvious invariants and transaction boundaries.
- Update docs in the same change whenever behavior changes.

## Common patterns

- Class doc for each service/query: purpose, inputs, outputs, side effects.
- Concern header comment: shared behavior scope and inclusion assumptions.
- Inline note above transaction blocks describing atomicity rationale.
- Route general doc style questions through `../documentation/SKILL.md`.

## Minimal examples

YARD on a service with contract + side effects:

```ruby
module Users
  class Invite
    # Invite a user by email.
    #
    # Why: invitation is a multi-step workflow (create user, send email) and should
    # not live in a controller action or model callback.
    #
    # @param email [String]
    # @param actor_id [Integer]
    # @return [Users::Invite::Result]
    def self.call(email:, actor_id:)
      # ...
    end
  end
end
```

Inline rationale on transaction boundary:

```ruby
Order.transaction do
  # Why: charging and marking paid must be atomic to avoid double-charge on retry.
  charge!
  mark_paid!
end
```

## Anti-patterns

- Comments that restate obvious Ruby syntax.
- Stale docs describing old return shapes/callback behavior.
- Missing failure documentation for service objects.
- Large narrative comments instead of clearer method names.

## Checklist

- Do public service/query methods have YARD docs?
- Do docs explain why logic is in concern/PORO instead of model/controller?
- Are input/output/error contracts explicit and current?
- Are callback/transaction comments only where non-obvious?

## References

- YARD: https://yardoc.org/
- Rails API docs: https://api.rubyonrails.org/
- Documentation skill index: `../documentation/SKILL.md`

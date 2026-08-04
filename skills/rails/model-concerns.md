# Model Concerns

Use model concerns to share small, cohesive model behavior without turning `ApplicationRecord` descendants into monoliths.

## When to load

- Two or more models share the same domain behavior.
- Shared behavior belongs to the model layer (invariants, scopes, tiny callbacks).
- You need to standardize repeated scopes/validations across related models.

## When NOT to load

- Logic is a multi-step workflow or side-effect orchestration (use service PORO).
- Logic is request-specific controller plumbing (use controller concern).
- Shared code crosses unrelated bounded contexts.

## Core rules

- One concern = one responsibility and one domain concept.
- Keep concerns deterministic and model-focused.
- Use `ActiveSupport::Concern` for clean inclusion and dependencies.
- Prefer explicit methods/scopes over heavy callback chains.
- Name by behavior (`Archivable`), not by implementation (`SharedMethods`).

## Common patterns

- Reusable scopes (`recent`, `active`, `search_by_term`).
- Shared status helpers (`published?`, `archive!`) for related models.
- Repeated validations tied to the same business rule.
- Small concern-level callbacks with clear intent and low surprise.

## Minimal examples

```ruby
# app/models/concerns/archivable.rb
module Archivable
  extend ActiveSupport::Concern

  included do
    scope :archived, -> { where.not(archived_at: nil) }
    scope :active, -> { where(archived_at: nil) }
  end

  def archive!
    update!(archived_at: Time.current)
  end

  def archived?
    archived_at.present?
  end
end
```

```ruby
class Project < ApplicationRecord
  include Archivable
end
```

## Anti-patterns

- Kitchen sink concerns with unrelated methods.
- Concerns adding network calls, emails, jobs, or transaction orchestration.
- Cross-cutting concerns mutating many associations implicitly.
- Multiple concerns competing to define same callback/method names.

## Checklist

- Is the concern reusable across at least two models now?
- Is responsibility narrow and domain-cohesive?
- Are callbacks minimal, predictable, and documented?
- Would a PORO be clearer for workflow logic?
- Do tests cover concern behavior via shared examples or integration paths?

## References

- ActiveSupport::Concern: https://api.rubyonrails.org/classes/ActiveSupport/Concern.html
- Rails Active Record guide: https://guides.rubyonrails.org/active_record_basics.html

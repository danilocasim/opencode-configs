# Callbacks Policy

Rails callbacks are powerful but easy to abuse. Use them only for invariant-adjacent bookkeeping, not for business workflows.

## When to load

- You are deciding whether a callback is appropriate.
- You are refactoring a callback-heavy model.
- You need guidance for safe `after_commit` job enqueue.

## When NOT to load

- You are implementing a workflow (use a service object).
- You are building background jobs/retry/idempotency logic (use `jobs-and-idempotency.md`).

## Core rules

- Callbacks may enforce invariants or maintain derived columns, but must not encode cross-domain workflows.
- Avoid callbacks that perform network calls, enqueue jobs, or send emails.
- Prefer explicit commands: `PublishPost.call(post:, actor:)` over `after_save :publish_side_effects`.
- If you must enqueue a job from persistence, prefer `after_commit` (not `after_save`).
- Keep callbacks small and easily removable.

## Minimal examples

Acceptable callback: normalize a field.

```ruby
class User < ApplicationRecord
  before_validation :normalize_email

  private

  def normalize_email
    self.email = email.to_s.strip.downcase
  end
end
```

Prefer `after_commit` when enqueue is unavoidable:

```ruby
class Invoice < ApplicationRecord
  after_commit :enqueue_pdf_job, on: :create

  private

  def enqueue_pdf_job
    GenerateInvoicePdfJob.perform_later(id)
  end
end
```

## Anti-patterns

- Callbacks that send emails, call external APIs, or enqueue multiple jobs.
- Callback chains where order matters.
- `after_save` enqueue that runs inside a transaction and breaks on rollback.
- Hidden mutations that surprise callers (e.g., changing unrelated fields).

## Checklist

- Is this truly invariant-adjacent bookkeeping?
- Could this be an explicit service command instead?
- If enqueueing, is it `after_commit` and retry-safe?
- Are callback side effects covered by unit tests?

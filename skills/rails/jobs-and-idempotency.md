# Jobs and Idempotency

Background jobs must be retry-safe. Assume any job can run twice, out of order, or long after enqueue.

## When to load

- You are adding an ActiveJob/Sidekiq job.
- You need idempotency rules for retries.
- You are deciding where to enqueue jobs (controller vs model vs service).

## When NOT to load

- You are designing authorization (use policy docs).
- You are doing DB migration/backfill strategy (use `migrations-and-backfills.md`).

## Core rules

- Make jobs idempotent: repeated runs produce the same final state.
- Pass stable identifiers (record IDs), not serialized objects.
- Prefer enqueue from a service at the transaction boundary; otherwise use `after_commit`.
- Treat external calls as side effects: add timeouts, retries, and idempotency keys.
- Persist “did work already” state (or use a unique key) rather than relying on job uniqueness features.

## Minimal examples

Idempotent job with a marker column:

```ruby
class SendWelcomeEmailJob < ApplicationJob
  queue_as :default

  def perform(user_id)
    user = User.find(user_id)
    return if user.welcome_email_sent_at?

    User.transaction do
      user.lock!
      return if user.welcome_email_sent_at?

      UserMailer.welcome(user).deliver_now
      user.update!(welcome_email_sent_at: Time.current)
    end
  end
end
```

Enqueue at the boundary (service) instead of callbacks:

```ruby
result = Orders::Checkout.call(order_id:, actor:)
SendReceiptJob.perform_later(result.value.id) if result.ok?
```

## Anti-patterns

- Jobs that mutate global state with no dedupe/marker.
- Passing complex objects as job args.
- Enqueueing inside a DB transaction where rollback is possible.
- Retrying external calls without an idempotency key.

## Checklist

- Can this job run twice safely?
- Does it accept only IDs and primitives?
- Is enqueueing aligned to the transaction boundary?
- Are external calls bounded (timeouts) and idempotent?
- Do tests cover retry/double-run behavior?

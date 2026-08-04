# Service and Query Objects

Use POROs to keep models/controllers thin: services handle workflows and side effects; queries handle read logic and filtering.

## When to load

- A use case spans multiple models, steps, or external systems.
- You need transaction boundaries, retries, or explicit failure handling.
- Query/filter logic is repeated across controllers/scopes/endpoints.

## When NOT to load

- Logic is a single model invariant or trivial finder.
- You are wrapping one line of code with no added contract.
- You need authorization rules (prefer dedicated policy objects).

## Core rules

- Service object = one business use case (`Namespace::Action.call(...)`).
- Query object = one read concern (`Namespace::Search.call(scope:, filters:)`).
- Define clear input/output contracts and failure semantics.
- Keep services orchestration-focused; move pure calculations to value objects.
- Use transactions explicitly where writes must be atomic.

## Common patterns

- `ApplicationService` base with class-level `.call`.
- Result contract (`success?`, `value`, `error`, optional `code`).
- Service names from domain verbs: `Orders::Checkout`, `Users::Invite`.
- Query objects returning `ActiveRecord::Relation` for composability/pagination.
- Parameter sanitizer for untrusted sort/filter input.

## Minimal examples

Service object with explicit contract:

```ruby
# app/services/orders/checkout.rb
module Orders
  Result = Data.define(:ok?, :value, :error) do
    def self.ok(value) = new(true, value, nil)
    def self.err(error) = new(false, nil, error)
  end

  class Checkout
    def self.call(order_id:, user_id:)
      new(order_id:, user_id:).call
    end

    def initialize(order_id:, user_id:)
      @order_id = order_id
      @user_id = user_id
    end

    def call
      Order.transaction do
        order = Order.lock.find(@order_id)
        return Result.err("not_owner") unless order.user_id == @user_id

        order.checkout!
        Result.ok(order)
      end
    rescue ActiveRecord::RecordNotFound
      Result.err("not_found")
    end
  end
end
```

Query object returning a relation:

```ruby
# app/queries/orders/search.rb
module Orders
  class Search
    def self.call(relation: Order.all, status: nil, q: nil)
      new(relation:, status:, q:).call
    end

    def initialize(relation:, status:, q:)
      @relation = relation
      @status = status
      @q = q
    end

    def call
      rel = @relation
      rel = rel.where(status: @status) if @status.present?
      rel = rel.where("number ILIKE ?", "%#{@q.strip}%") if @q.present?
      rel
    end
  end
end
```

Thin controller orchestration:

```ruby
class OrdersController < ApplicationController
  def update
    result = Orders::Checkout.call(order_id: params[:id], user_id: current_user.id)

    if result.ok?
      redirect_to order_path(result.value)
    else
      head(result.error == "not_found" ? :not_found : :forbidden)
    end
  end
end
```

## Anti-patterns

- Service sprawl where every trivial method becomes a service.
- Query object that mutates records or triggers side effects.
- Services returning inconsistent shapes across success/failure paths.
- Rescuing everything without typed/domain errors.

## Checklist

- Is this truly a multi-step workflow or reusable read concern?
- Are inputs validated/sanitized at boundary entry?
- Is transaction scope explicit and minimal?
- Is output contract stable and documented?
- Are unit tests covering success, failure, and edge cases?

## References

- Active Record transactions: https://guides.rubyonrails.org/active_record_transactions.html
- ActiveSupport::Notifications: https://api.rubyonrails.org/classes/ActiveSupport/Notifications.html

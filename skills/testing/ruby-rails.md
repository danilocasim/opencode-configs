# Ruby / Rails Testing (TDD-First)

Use this guide for Ruby gems/apps and Rails services. Prefer the framework already used in the repo.

## When to load

- You are testing Ruby POROs, Rails models, request flows, or system behavior.
- You are enforcing TDD for service/query/form objects.

## When NOT to load

- Non-Ruby stacks (use stack-specific testing docs).
- Pure performance/load testing tasks.

## Core rules

- Use existing framework: RSpec if `spec/` exists, otherwise Minitest.
- Default layer order: unit -> request/integration -> system.
- Prefer request specs over controller specs for Rails behavior.
- Keep factories focused; avoid giant setup graphs.

## Common patterns

- PORO unit tests for services/queries/policies/value objects.
- Request specs assert status, payload shape, auth, and invalid input.
- System specs only for critical user journeys.
- Result-oriented assertions over framework internals.

## Minimal examples

Service PORO unit spec:

```ruby
RSpec.describe Orders::Checkout do
  it "returns ok result for owned order" do
    order = create(:order, user: create(:user))

    result = described_class.call(order_id: order.id, user_id: order.user_id)

    expect(result.ok?).to eq(true)
  end
end
```

Request spec (status + contract):

```ruby
RSpec.describe "GET /api/v1/projects/:id" do
  it "returns 404 when missing" do
    get "/api/v1/projects/999999", as: :json

    expect(response).to have_http_status(:not_found)
    expect(JSON.parse(response.body)).to include("error" => "not_found")
  end
end
```

```ruby
RSpec.describe NormalizeEmail do
  it "strips spaces and downcases" do
    expect(described_class.call("  A@Example.COM ")).to eq("a@example.com")
  end
end
```

## Anti-patterns

- Over-mocking ActiveRecord internals.
- Heavy `before` chains hiding test intent.
- Controller specs for new Rails endpoints when request specs are available.
- Testing Rails internals instead of app behavior.

## Checklist

- Is there a failing test before implementation?
- Does each endpoint test include at least one failure path?
- Are factories/fixtures minimal and readable?
- Are critical workflows covered at system level only where needed?

## References

- RSpec docs: https://rspec.info/documentation/
- Rails testing guide: https://guides.rubyonrails.org/testing.html

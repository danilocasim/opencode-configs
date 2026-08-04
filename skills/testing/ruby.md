# Ruby/Rails Testing (Compatibility Route)

## When to load

- Another doc/router points here (backward compatibility).
- You need the shortest possible pointer to the current Ruby/Rails testing docs.

## When NOT to load

- You need real Ruby/Rails testing guidance: use `ruby-rails.md`.

## Core rules

- Treat this file as a pointer, not the canonical guide.
- Prefer the test framework already present (RSpec vs Minitest).
- Follow TDD: Red -> Green -> Refactor.

## Common patterns

- PORO/service unit specs for business rules.
- Request specs for Rails endpoints (status + error shape + auth).
- System specs only for critical journeys.

## Minimal examples

RSpec PORO spec:

```ruby
RSpec.describe NormalizeEmail do
  it "downcases and trims" do
    expect(described_class.call("  A@EXAMPLE.COM ")).to eq("a@example.com")
  end
end
```

## Anti-patterns

- Controller specs for new Rails endpoints when request specs suffice.
- Over-mocking ActiveRecord internals.
- Giant factories/fixtures that hide intent.

## Checklist

- Are you reading the canonical guide (`ruby-rails.md`)?
- Is there a failing regression test for bug fixes?
- Are fixtures minimal and deterministic?

## References

- Canonical Ruby/Rails guide: `ruby-rails.md`
- TDD loop: `tdd-workflow.md`
- Fixtures strategy: `fixtures-and-test-data.md`
- Mocking discipline: `test-doubles-and-mocking-discipline.md`

# Testing Documentation and Comments

Good tests are executable documentation. Comments should explain why a case exists, not narrate obvious mechanics.

## When to load

- You are standardizing test naming and test-doc quality.
- You need guidance for documenting tricky fixtures/mocks.

## When NOT to load

- You need framework mechanics (load stack-specific testing doc).

## Core rules

- Prefer behavior-focused test names over comments.
- Comment non-obvious domain constraints, timing caveats, or bug history.
- Keep fixture helpers documented if setup assumptions are hidden.
- Update test docs when behavior changes.

## Common patterns

- Arrange/Act/Assert structure stays visually clear.
- PR notes include changed behavior and which tests prove it.
- Public contract changes include explicit regression tests.

## Minimal examples

```ruby
it "returns 422 when email is invalid" do
  # Regression: this used to 500 due to nil normalization.
  post "/api/v1/users", params: { email: "nope" }, as: :json
  expect(response).to have_http_status(:unprocessable_entity)
end
```

```text
Why this test exists:
- bug repro for empty cache case
- protects an API contract (status + error shape)
```

## Anti-patterns

- Comments that restate code.
- Copy-pasted tests with vague names.
- Magic fixture helpers with no rationale.
- Missing docs for externally visible behavior changes.

## Checklist

- Can test names stand alone as behavior docs?
- Are comments only on non-obvious constraints?
- Are helper fixtures discoverable and documented?
- Did docs and tests evolve together?

## References

- `../documentation/SKILL.md`
- Google Testing Blog: https://testing.googleblog.com/

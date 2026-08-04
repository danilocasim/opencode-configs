# Ruby Style and Idioms

## When to load

- You are writing or reviewing Ruby 3.x code style and syntax choices.
- You need consistent naming, control flow, and block usage.

## When NOT to load

- You are deciding class boundaries and object responsibilities.
- You are designing error contracts or result objects.

## Core rules

- Use `snake_case` for methods/variables and `CamelCase` for classes/modules.
- Prefer keyword args for methods with 3+ parameters.
- Use iterators and Enumerable over manual loops.
- Keep methods short and intention-revealing.

## Patterns

- Prefer guard clauses for invalid/early-exit paths.
- Use `case` and pattern matching (`in`) for complex branching.
- Use `Data.define`/`Struct` for lightweight immutable-ish value objects.
- Use `{}` for single-line blocks and `do/end` for multiline blocks.

## Minimal examples

```ruby
def parse_limit(raw, default: 20, max: 100)
  return default if raw.nil? || raw.strip.empty?

  limit = Integer(raw)
  return default if limit <= 0

  [limit, max].min
rescue ArgumentError
  default
end
```

```ruby
Email = Data.define(:value) do
  def initialize(value)
    super(value.strip.downcase)

    raise ArgumentError, "invalid email" unless value.include?("@")
  end
end
```

```ruby
case payload
in { type: "user", id: Integer => id }
  id
in { type: "guest" }
  nil
else
  raise ArgumentError, "unknown payload"
end
```

## Anti-patterns

- Clever metaprogramming for routine control flow.
- Long positional-argument lists with ambiguous meaning.
- Deep nested conditionals when guard clauses would flatten flow.

## Checklist

- Naming follows Ruby conventions.
- Method signatures read clearly without call-site guessing.
- Flow is simple to scan and does not rely on hidden side effects.

## References

- https://rubystyle.guide/
- https://docs.ruby-lang.org/en/master/syntax/control_expressions_rdoc.html
- https://docs.ruby-lang.org/en/master/Enumerable.html

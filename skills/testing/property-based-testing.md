# Property-Based Testing (Short)

## When to load

- You have invariants (ordering, round-trips, idempotence) with many inputs.
- Bugs show up only for "weird" data (Unicode, long strings, edge numbers).

## When NOT to load

- You are validating a single example or a small input matrix.
- The domain is mostly IO orchestration (prefer integration/E2E).

## Core rules

- Define properties (invariants), not examples.
- Constrain generators to valid domain ranges.
- Persist failing seeds/cases as regression examples.

## Common patterns

- Round-trip: `decode(encode(x)) == x`.
- Normalization: `normalize(normalize(x)) == normalize(x)`.
- Ordering: output is sorted and same multiset as input.

## Minimal examples

TypeScript with `fast-check`:

```ts
import { expect, it } from "vitest";
import fc from "fast-check";

it("normalizeEmail is idempotent", () => {
  fc.assert(
    fc.property(fc.string(), (s) => {
      expect(normalizeEmail(normalizeEmail(s))).toBe(normalizeEmail(s));
    })
  );
});
```

## Anti-patterns

- Unbounded generators that create useless noise and slow runs.
- Ignoring failing seeds (no regression captured).

## Checklist

- Is the property meaningful and stable?
- Are generators constrained to real inputs?
- Do you save failing cases as standard regression tests?

## References

- fast-check: https://fast-check.dev/

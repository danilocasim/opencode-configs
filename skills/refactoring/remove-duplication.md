# Remove Duplication

Duplication is sometimes fine, but accidental duplication creates inconsistent behavior and slow changes. Remove it when it reduces risk.

## When to load

- You see the same logic repeated with small variations.
- You are fixing a bug that exists in multiple places.
- You need a rule for when to DRY.

## When NOT to load

- Duplication is intentional (different domains or different lifecycles).
- You lack tests and need to freeze behavior first.

## Core rules

- Prefer duplication over wrong abstraction.
- Extract only after you understand the axis of change.
- Keep extracted helpers close to their domain.
- Add tests that cover the shared behavior.

## Minimal examples

Heuristic:

```text
DRY when:
  bug fixes must be applied in multiple places
  behavior must remain consistent
keep duplicate when:
  domains differ
  change axes differ
```

## Anti-patterns

- Premature abstraction.
- “Helper” modules that become dumping grounds.
- Extracting for aesthetic reasons without reducing risk.

## Checklist

- Axis of change understood.
- Extraction reduces risk.
- Tests cover shared behavior.
- New home is domain-appropriate.

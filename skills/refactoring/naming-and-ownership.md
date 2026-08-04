# Naming and Ownership

Good refactors often fail because nobody can find the code afterward. Naming and ownership rules keep architecture navigable.

## When to load

- You are creating new modules/services.
- You are reorganizing folders.
- You need naming conventions for discoverability.

## When NOT to load

- You are only changing internals with no new surface area.
- You are doing performance work.

## Core rules

- Prefer domain names over technical names.
- Keep feature ownership clear (a single “home” for a behavior).
- Avoid generic buckets (`helpers`, `utils`, `common`) unless truly shared.
- Keep public APIs small and documented.

## Minimal examples

Naming checks:

```text
Can a new teammate guess where this lives?
Does the name describe the domain behavior?
Is there one obvious owner?
```

## Anti-patterns

- “Manager”, “Processor”, “Helper” classes.
- Multiple homes for the same behavior.
- Public APIs with unclear contracts.

## Checklist

- Names are domain-first.
- Ownership is clear.
- No new generic buckets.
- Public API documented.

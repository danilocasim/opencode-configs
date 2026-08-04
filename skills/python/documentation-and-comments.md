# Documentation and Comments (Google Docstrings)

Docstrings are executable documentation for LLMs: they anchor intent, constraints, and error behavior.

## When to load

- You are writing/updating docstrings for public APIs.
- You need a comment policy that avoids noise.
- You are documenting error behavior and invariants.

## When NOT to load

- You are choosing error strategy -> `errors-and-results.md`.
- You are designing HTTP API contracts -> `../api/SKILL.md`.

## Core rules

- Public functions/classes/modules have docstrings.
- Explain WHY before WHAT.
- Document inputs/outputs and error conditions.
- Keep comments for non-obvious intent; do not restate code.

## Common patterns

- Google-style docstrings with `Args/Returns/Raises`.
- Add a short `Why:` section for tradeoffs/constraints.
- Document determinism (ordering, timeouts, randomness).

## Minimal examples

```python
from __future__ import annotations


def normalize_date(raw: str, *, time_zone: str) -> str:
    """Normalize a user-supplied date to an ISO 8601 date string.

    Why:
        Storage and comparisons are safer when all dates are normalized.

    Args:
        raw: User-supplied date (e.g. "2026-01-31").
        time_zone: IANA timezone name (e.g. "America/Los_Angeles").

    Returns:
        ISO 8601 date string (YYYY-MM-DD).

    Raises:
        ValueError: If the input cannot be parsed.
    """
    raise NotImplementedError
```

```python
"""HTTP client adapter for ExampleAPI.

Why:
    Centralizes retry/timeout policy and error mapping.
"""
```

## Anti-patterns

- Docstrings that restate the function name.
- Missing `Raises` for expected exceptions.
- Large narrative comments that drift.

## Checklist

- Public APIs documented (why/args/returns/raises)
- Error behavior matches actual exceptions
- Comments only where intent is non-obvious

## References

- PEP 257: https://peps.python.org/pep-0257/
- Google docstrings: https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings

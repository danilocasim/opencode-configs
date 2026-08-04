# Python Testing (pytest, TDD-First)

Use this guide for Python libraries, services, and web apps.

## When to load

- You are testing Python logic, APIs, or async behavior.
- You need deterministic pytest workflows.

## When NOT to load

- Non-Python stacks.
- Pure benchmark/profiling tasks.

## Core rules

- Use `pytest` and keep tests behavior-focused.
- Prefer fixtures over setup/teardown boilerplate.
- Use `pytest.mark.parametrize` for case matrices.
- For async behavior, use `pytest-asyncio`.

## Common patterns

- Use `@pytest.mark.parametrize` for input matrices.
- Use `pytest.raises(..., match=...)` for error contracts.
- Use `monkeypatch` for env vars and globals.
- Use tmp-path fixtures for filesystem isolation.

## Minimal examples

```python
import pytest


@pytest.mark.parametrize(
    "raw, expected",
    [("  A@EXAMPLE.COM ", "a@example.com"), ("x@y.com", "x@y.com")],
)
def test_normalize_email(raw: str, expected: str) -> None:
    assert normalize_email(raw) == expected


def test_normalize_email_rejects_invalid() -> None:
    with pytest.raises(ValueError, match="invalid email"):
        normalize_email("not-an-email")
```

## Anti-patterns

- Huge autouse fixtures with hidden setup.
- Uncontrolled time/randomness/network in tests.
- Happy-path-only coverage without error branches.
- Monkeypatch leakage across tests.

## Checklist

- Is there a failing test before implementation?
- Are edge/error paths covered?
- Are fixtures scoped minimally (`function` by default)?
- Are env/time/network dependencies controlled?

## References

- pytest docs: https://docs.pytest.org/
- pytest-asyncio: https://pytest-asyncio.readthedocs.io/

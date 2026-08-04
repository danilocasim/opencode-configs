# Errors and Results (Python)

Use explicit, consistent error contracts so callers (and LLMs) don't guess.

## When to load

- You need a consistent error strategy across layers.
- You are mapping adapter failures (HTTP/timeouts) into domain errors.
- You are deciding between exceptions, sentinel returns, or `Result`.

## When NOT to load

- You are designing retry/backoff policy -> `http-clients-and-retries.md`.
- You are designing REST API envelopes -> `../api/SKILL.md`.

## Core rules

- Prefer exceptions for truly exceptional failures.
- Do not use `None` as an error.
- Define small custom exceptions for domain errors.
- Convert errors at boundaries (adapter -> domain -> presentation).
- Preserve context using exception chaining (`raise ... from err`).

## Common patterns

- Domain exception hierarchy (handleable): `DomainError -> InvalidInputError, NotFoundError, ConflictError`.
- Adapter errors wrapped into one `ExternalServiceError`.
- `Result[T]` only when it simplifies call sites (expected failures).

## Minimal examples

```python
from __future__ import annotations


class DomainError(Exception):
    """Base class for errors callers may want to handle."""


class InvalidOrderError(DomainError):
    def __init__(self, *, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


def parse_quantity(raw: str) -> int:
    try:
        value = int(raw)
    except ValueError as err:
        raise InvalidOrderError(reason="quantity must be an integer") from err

    if value <= 0:
        raise InvalidOrderError(reason="quantity must be positive")

    return value
```

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class Ok(Generic[T]):
    value: T


@dataclass(frozen=True, slots=True)
class Err:
    error: Exception


Result = Ok[T] | Err


def safe_int(raw: str) -> Result[int]:
    try:
        return Ok(int(raw))
    except ValueError as err:
        return Err(err)
```

## Anti-patterns

- `except Exception:` swallowing errors.
- Ad hoc `(value, error)` tuple returns.
- Using `Result` everywhere (noisy, inconsistent).

## Checklist

- Domain errors are explicit and documented
- Error conversion happens at boundaries
- Exceptions are chained when wrapping
- Error paths are test-covered
- Logs do not include secrets/PII

## References

- raise statement: https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
- ExceptionGroup: https://docs.python.org/3/library/exceptions.html#ExceptionGroup

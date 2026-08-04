# Types and Boundaries (Python)

Strict typing and explicit boundary validation are the main levers for making LLM-generated Python safe and predictable.

## When to load

- You are defining public function/class APIs.
- You need to validate inputs at boundaries (HTTP handlers, CLI args, env/config).
- You are refactoring to tighten types and reduce ambiguity.

## When NOT to load

- You mainly need toolchain setup -> `tooling-and-quality.md`.
- You mainly need async patterns -> `async-and-concurrency.md`.

## Core rules

- Type hints are required for all public functions/methods and dataclass fields.
- Prefer precise types; avoid `Any`.
- Validate at boundaries, not deep inside domain logic.
- Prefer keyword-only args for public APIs.

## Common patterns

- `@dataclass(frozen=True, slots=True)` for value objects.
- `NewType` for IDs when ambiguity is costly.
- `Protocol` for dependency injection boundaries.
- `Literal`/`Enum` for closed sets.

## Minimal examples

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import NewType

UserId = NewType("UserId", int)


@dataclass(frozen=True, slots=True)
class User:
    id: UserId
    email: str


def normalize_email(email: str) -> str:
    return email.strip().lower()


def create_user(*, user_id: int, email: str) -> User:
    normalized = normalize_email(email)
    if "@" not in normalized:
        raise ValueError("invalid email")

    return User(id=UserId(user_id), email=normalized)
```

```python
from __future__ import annotations

from typing import Protocol


class Clock(Protocol):
    def now_iso(self) -> str: ...


def make_audit_line(*, actor: str, action: str, clock: Clock) -> str:
    return f"{clock.now_iso()}\t{actor}\t{action}"
```

## Anti-patterns

- `dict[str, Any]` everywhere instead of modeling shapes.
- Using types as validation (types do not validate at runtime).
- Accepting `str | int | None` everywhere without normalization.

## Checklist

- Public APIs fully typed (params/returns/attrs)
- Boundary validation is explicit and centralized
- Domain layer uses domain types (not raw JSON dicts)
- No new `Any` without a containment plan

## References

- typing: https://docs.python.org/3/library/typing.html
- Protocols (PEP 544): https://peps.python.org/pep-0544/
- dataclasses: https://docs.python.org/3/library/dataclasses.html

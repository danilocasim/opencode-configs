# Project Structure (Python)

Keep Python codegen consistent by making boundaries obvious: domain logic is pure, IO adapters are explicit, and import-time side effects are avoided.

## When to load

- You are creating a new Python package/service and need a layout.
- You are deciding where code should live (domain vs IO vs adapters).
- You want import boundaries that keep tests fast and deterministic.

## When NOT to load

- You only need HTTP retry policy -> `http-clients-and-retries.md`.
- You only need error strategy -> `errors-and-results.md`.

## Core rules

- Prefer a `src/` layout for packages.
- Separate domain logic from IO (HTTP, DB, filesystem, subprocess).
- Avoid import-time side effects; imports must not do network/FS work.
- Keep modules cohesive; avoid mega `utils.py`.

## Common patterns

Library layout:

```text
pyproject.toml
src/
  mypkg/
    __init__.py
    domain/
      __init__.py
      models.py
      service.py
    adapters/
      __init__.py
      http_client.py
tests/
  test_service.py
```

Service layout:

```text
pyproject.toml
src/
  mysvc/
    __init__.py
    main.py
    config.py
    domain/
    adapters/
    web/
tests/
```

## Minimal examples

`src/mypkg/domain/service.py`

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Greeting:
    message: str


def build_greeting(*, name: str) -> Greeting:
    return Greeting(message=f"Hello, {name}!")
```

`src/mypkg/adapters/http_client.py`

```python
from __future__ import annotations

from dataclasses import dataclass

import httpx


@dataclass(frozen=True, slots=True)
class GreetingApi:
    base_url: str
    client: httpx.Client

    def close(self) -> None:
        self.client.close()
```

## Anti-patterns

- Domain functions that call `httpx` directly.
- Import-time config parsing deep in modules.
- Tests that require network access by default.

## Checklist

- `src/` layout chosen (or repo convention followed)
- Domain code has no IO imports
- IO code isolated behind adapters
- `__init__.py` stays minimal
- Tests run offline and in any order

## References

- Packaging guide: https://packaging.python.org/
- src layout: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
- Import system: https://docs.python.org/3/reference/import.html

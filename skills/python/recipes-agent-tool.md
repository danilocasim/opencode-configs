# Recipe: Agent Tool Module (Python)

Build agent-callable tools that are deterministic, typed, and testable.

## When to load

- You are building a Python module that exposes "tools" for an agent to call.
- You need explicit IO boundaries and JSON-serializable inputs/outputs.

## When NOT to load

- You are building a human CLI -> `recipes-cli-tool.md`.
- You are doing security-sensitive tooling -> also load `../security/SKILL.md`.

## Core rules

- Tools are thin adapters: validate -> call domain -> return structured output.
- Inputs/outputs must be JSON-serializable and versionable.
- Determinism: inject clocks/RNG; avoid global state.
- Timeouts on all IO.
- Errors are explicit and stable (codes + messages).

## Common patterns

- `ToolContext` for dependencies (clients, base_url, logger).
- Return envelope: `{ "ok": true, "data": ... }` / `{ "ok": false, "error": ... }`.
- Validate boundary inputs once.

## Minimal examples

`src/mypkg/tools/context.py`

```python
from __future__ import annotations

from dataclasses import dataclass

import httpx


@dataclass(frozen=True, slots=True)
class ToolContext:
    http: httpx.Client
    base_url: str
```

`src/mypkg/tools/get_user.py`

```python
from __future__ import annotations

from dataclasses import dataclass

from mypkg.tools.context import ToolContext


@dataclass(frozen=True, slots=True)
class GetUserInput:
    user_id: int


@dataclass(frozen=True, slots=True)
class ToolError:
    code: str
    message: str


@dataclass(frozen=True, slots=True)
class ToolOk:
    ok: bool
    data: dict[str, object]


@dataclass(frozen=True, slots=True)
class ToolErr:
    ok: bool
    error: ToolError


ToolResult = ToolOk | ToolErr


def get_user(ctx: ToolContext, inp: GetUserInput) -> ToolResult:
    if inp.user_id <= 0:
        return ToolErr(
            ok=False,
            error=ToolError(code="invalid_input", message="user_id must be positive"),
        )

    resp = ctx.http.get(f"{ctx.base_url}/users/{inp.user_id}", timeout=5.0)
    if resp.status_code == 404:
        return ToolErr(ok=False, error=ToolError(code="not_found", message="user not found"))
    resp.raise_for_status()

    return ToolOk(ok=True, data=resp.json())
```

## Anti-patterns

- Tools that mutate globals or read env vars deep in domain logic.
- Returning free-form strings instead of structured data.
- Network calls without timeouts.

## Checklist

- Input/output types are explicit and serializable
- Boundary validation is centralized
- IO has timeouts
- Error codes are stable
- Unit tests cover ok + error paths without network

## References

- dataclasses: https://docs.python.org/3/library/dataclasses.html
- typing: https://docs.python.org/3/library/typing.html

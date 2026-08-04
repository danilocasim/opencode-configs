# Async and Concurrency (Python)

Use structured concurrency to keep async code readable and safe.

## When to load

- You are writing `async` code (network IO, parallel requests, workers).
- You need cancellation, timeouts, task management, or bounded concurrency.

## When NOT to load

- You are only doing sync HTTP retries -> `http-clients-and-retries.md`.
- You need testing mechanics -> `../testing/python.md`.

## Core rules

- Never block the event loop.
- Use `asyncio.TaskGroup` for structured concurrency (3.11+).
- Apply explicit timeouts.
- Bound concurrency (semaphores).
- Cancellation must propagate (do not swallow `CancelledError`).

## Common patterns

- `asyncio.timeout()` for scoped timeouts.
- `asyncio.Semaphore` for bounded parallelism.
- Keep IO async; offload CPU-heavy work to thread/process pools.

## Minimal examples

```python
from __future__ import annotations

import asyncio
from collections.abc import Iterable


async def fetch_one(url: str) -> str:
    await asyncio.sleep(0.01)
    return url


async def fetch_many(urls: Iterable[str], *, limit: int = 10) -> list[str]:
    sem = asyncio.Semaphore(limit)
    results: list[str] = []

    async def run(url: str) -> None:
        async with sem:
            results.append(await fetch_one(url))

    async with asyncio.TaskGroup() as tg:
        for url in urls:
            tg.create_task(run(url))

    return results
```

```python
from __future__ import annotations

import asyncio


async def do_work() -> None:
    async with asyncio.timeout(2.0):
        await asyncio.sleep(0.5)
```

## Anti-patterns

- Calling sync clients (`requests`) inside async functions.
- Fire-and-forget tasks with no owner.
- Unlimited concurrency over untrusted input.

## Checklist

- Timeouts are explicit and tested
- Concurrency is bounded
- Task lifetimes are owned (`TaskGroup`)
- Cancellation propagates cleanly

## References

- asyncio: https://docs.python.org/3/library/asyncio.html
- TaskGroup: https://docs.python.org/3/library/asyncio-task.html#task-groups
- timeout: https://docs.python.org/3/library/asyncio-task.html#asyncio.timeout

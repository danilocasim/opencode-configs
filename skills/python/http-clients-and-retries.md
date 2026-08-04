# HTTP Clients and Retries (Python)

Default to safe network behavior: explicit timeouts, bounded retries, and idempotency awareness.

## When to load

- You are integrating with an external HTTP API.
- You need timeouts, retries, backoff, idempotency, and observability.
- You are choosing sync vs async HTTP patterns.

## When NOT to load

- You are designing your own REST API contract -> `../api/SKILL.md`.
- You are handling auth/secrets/cert pinning -> `../security/SKILL.md`.

## Core rules

- Always set explicit timeouts.
- Retries must be bounded and targeted (transient failures only).
- Do not retry non-idempotent writes without an idempotency key.
- Add jitter to backoff.
- Keep retry behavior deterministic in tests (inject sleep/backoff policy).

## Common patterns

- Prefer `httpx`.
- Reuse a single client per process.
- Retry on connect errors, timeouts, 502/503/504, and 429 with `Retry-After`.

## Minimal examples

```python
from __future__ import annotations

import time

import httpx


def get_json_with_retries(
    client: httpx.Client,
    url: str,
    *,
    timeout_s: float = 5.0,
    attempts: int = 3,
) -> dict[str, object]:
    for i in range(attempts):
        try:
            resp = client.get(url, timeout=timeout_s)
            resp.raise_for_status()
            data = resp.json()
            if not isinstance(data, dict):
                raise ValueError("expected JSON object")
            return data
        except (httpx.TimeoutException, httpx.ConnectError, httpx.HTTPStatusError):
            if i == attempts - 1:
                raise
            time.sleep((2**i) * 0.1 + (i * 0.01))

    raise RuntimeError("unreachable")
```

```python
import httpx

client = httpx.Client(headers={"User-Agent": "mysvc/1"})
try:
    ...
finally:
    client.close()
```

## Anti-patterns

- No timeout (hangs forever).
- Retrying all 4xx.
- New client per request.
- Logging URLs with secrets.

## Checklist

- Explicit timeouts set and documented
- Retry policy is bounded and targeted
- Idempotency considered for writes
- Client reused and closed
- Tests cover timeout/retry branches deterministically

## References

- httpx timeouts: https://www.python-httpx.org/advanced/timeouts/
- RFC 9110 semantics: https://www.rfc-editor.org/rfc/rfc9110

# Async and Streams (Dart)

Async bugs usually come from unbounded concurrency, missing cancellation, and inconsistent error handling. Make timeouts and failure modes explicit.

## When to load

- You are implementing `Future`/`Stream` logic.
- You are calling network/IO code.
- You need patterns for timeouts and retries.

## When NOT to load

- You are modeling error contracts (`errors-and-results.md`).
- You are doing Flutter widget rebuild/perf work (use `../flutter/performance.md`).

## Core rules

- Prefer `async`/`await` for readability.
- Use timeouts for network/IO boundaries.
- Keep concurrency bounded; avoid firing many Futures without limits.
- Never ignore a `Future` unless you intentionally detach it.
- Streams should have explicit lifecycle and error handling.

## Minimal examples

Timeout for a boundary:

```dart
Future<T> withTimeout<T>(Future<T> f, Duration timeout) {
  return f.timeout(timeout);
}
```

Mapping errors explicitly:

```dart
Future<Result<String>> loadName() async {
  try {
    final name = await fetchName();
    return Ok(name);
  } catch (e) {
    return const Err('network', 'failed to load');
  }
}
```

## Anti-patterns

- `Future.wait` over large lists without limits.
- Hidden retries that amplify load.
- Streams that never close or leak listeners.

## Checklist

- Timeouts exist on IO.
- Concurrency is bounded.
- Errors are mapped to a stable contract.
- Stream subscriptions are cleaned up.

# Errors and Results (Dart)

Use exceptions for truly exceptional programmer/IO failures, and use explicit Result types for expected domain failures you want callers to handle.

## When to load

- You are designing an API that can fail.
- You want consistent error codes/messages.
- You are reducing try/catch sprawl.

## When NOT to load

- You only need lint/tool setup (`tooling-and-quality.md`).
- You only need async patterns (`async-and-streams.md`).

## Core rules

- Expected failures should be returned (Result) or represented in types.
- Unexpected failures can throw; catch at boundaries and map to user-safe errors.
- Use stable error codes for programmatic handling.
- Do not leak internal exception messages to UI.

## Minimal examples

Domain error modeled explicitly:

```dart
sealed class LoginError {
  const LoginError();
}

final class InvalidCredentials extends LoginError {
  const InvalidCredentials();
}

final class NetworkDown extends LoginError {
  const NetworkDown();
}
```

Boundary catch + map:

```dart
Result<T> guard<T>(T Function() fn) {
  try {
    return Ok(fn());
  } catch (_) {
    return const Err('unexpected', 'unexpected error');
  }
}
```

## Anti-patterns

- Throwing strings.
- Returning `null` for failure with no explanation.
- Exposing raw exception messages to the user.

## Checklist

- Failure modes are explicit.
- Stable codes/messages exist.
- Exceptions caught and mapped at boundaries.
- UI sees safe, user-facing messages.

# Testing (Dart)

Tests should lock behavior and keep refactors safe. Prefer deterministic unit tests and only add integration tests at boundaries.

## When to load

- You are writing tests for Dart packages.
- You need patterns for fakes/mocks and determinism.
- You are designing error-path coverage.

## When NOT to load

- You are writing Flutter widget tests (use `../flutter/testing.md`).
- You need generic testing policy (use `../testing/SKILL.md`).

## Core rules

- Prefer unit tests for pure logic.
- Mock boundaries (HTTP, file, time) not internal helpers.
- Control time and randomness.
- Assert behavior, not implementation.

## Minimal examples

`package:test` style:

```dart
import 'package:test/test.dart';

void main() {
  test('requireTrimmed rejects empty', () {
    expect(() => requireTrimmed('  ', field: 'name'), throwsArgumentError);
  });
}
```

## Anti-patterns

- Tests that depend on execution order.
- Real network calls in unit tests.
- Snapshot-like tests for business logic.

## Checklist

- Unit tests cover happy + error paths.
- Boundaries are faked/mocked.
- Tests are deterministic in CI.

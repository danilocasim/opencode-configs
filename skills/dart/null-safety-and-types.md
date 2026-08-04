# Null Safety and Types (Dart)

Null safety is Dart's superpower. Use it to make boundaries explicit, avoid defensive code everywhere, and keep APIs predictable.

## When to load

- You are defining public APIs (functions/classes).
- You are modeling domain types with sealed classes.
- You are tightening nullability or removing `!` assertions.

## When NOT to load

- You mainly need async/Stream patterns (`async-and-streams.md`).
- You mainly need testing strategy (`testing.md`).

## Core rules

- Make nullability explicit at boundaries; avoid `T?` if the value is required.
- Avoid `!` (non-null assertions); prove non-null via control flow.
- Prefer small immutable value types.
- Use `sealed` classes for closed sets and results.
- Keep public APIs narrow and typed; accept `String`/`int` only when truly raw.

## Minimal examples

Avoid `!` by validating once:

```dart
String requireTrimmed(String? input, {required String field}) {
  final v = (input ?? '').trim();
  if (v.isEmpty) throw ArgumentError.value(input, field, 'required');
  return v;
}
```

Sealed result type:

```dart
sealed class Result<T> {
  const Result();
}

final class Ok<T> extends Result<T> {
  const Ok(this.value);
  final T value;
}

final class Err<T> extends Result<T> {
  const Err(this.code, this.message);
  final String code;
  final String message;
}
```

## Anti-patterns

- `dynamic` for convenience (infects everything).
- `late` used as a workaround for initialization ordering.
- Nullable fields everywhere instead of modeling required/optional properly.

## Checklist

- Boundary inputs validated once.
- No new `!` assertions.
- Domain modeled with types (sealed/value objects).
- Public APIs are explicit and small.

# State Management and Architecture

Choose one state approach per app and stick to it. The goal is predictable state flow, testable logic, and minimal rebuilds.

## When to load

- You need to choose or standardize state management.
- You are refactoring a tangled set of `setState` calls.
- You need a pattern for async loading/error states.

## When NOT to load

- You only need navigation (`navigation-and-routing.md`).
- You only need widget layout (`widgets-layout-and-theming.md`).

## Core rules

- Prefer a unidirectional state flow.
- Keep async states explicit: loading/success/error.
- Make dependencies injectable (repositories/services).
- Widgets read state; they do not own domain rules.
- Avoid global mutable singletons.

## Minimal examples

Simple async state model (sealed classes):

```dart
sealed class AsyncState<T> {
  const AsyncState();
}

final class Loading<T> extends AsyncState<T> {
  const Loading();
}

final class Data<T> extends AsyncState<T> {
  const Data(this.value);
  final T value;
}

final class Failure<T> extends AsyncState<T> {
  const Failure(this.message);
  final String message;
}
```

Notifier/controller pattern (framework-agnostic):

```dart
class ProjectsController {
  ProjectsController(this._repo);
  final ProjectsRepo _repo;

  AsyncState<List<Project>> state = const Loading();

  Future<void> load() async {
    try {
      state = Data(await _repo.list());
    } catch (_) {
      state = const Failure('failed to load');
    }
  }
}
```

## Anti-patterns

- Storing derived UI state in multiple places.
- Mixing navigation side effects into state objects.
- Async errors swallowed silently.

## Checklist

- One state approach chosen.
- Async states explicit.
- Dependencies injectable.
- Logic testable without widgets.

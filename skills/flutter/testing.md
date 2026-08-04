# Testing (Flutter)

Flutter tests should be layered: unit tests for pure logic, widget tests for UI behavior, and a small number of integration tests for critical flows.

## When to load

- You are adding widget tests.
- You need deterministic patterns for async/time.
- You need a strategy for golden tests.

## When NOT to load

- You are only writing Dart unit tests (use `../dart/testing.md`).
- You need generic testing philosophy (use `../testing/SKILL.md`).

## Core rules

- Prefer widget tests for most UI behavior.
- Keep integration tests minimal (critical journeys).
- Avoid sleeps; wait for frames/conditions.
- Mock boundaries (network/storage) at the edge.

## Minimal examples

Widget test example:

```dart
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/material.dart';

void main() {
  testWidgets('button triggers callback', (tester) async {
    var pressed = 0;

    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(
          body: FilledButton(
            onPressed: () => pressed++,
            child: const Text('Save'),
          ),
        ),
      ),
    );

    await tester.tap(find.text('Save'));
    await tester.pump();

    expect(pressed, 1);
  });
}
```

## Anti-patterns

- Golden tests for everything (fragile).
- Integration tests for simple widget behavior.
- Real network in widget tests.

## Checklist

- Unit/widget tests cover behaviors.
- Integration tests only for critical flows.
- Tests deterministic in CI.

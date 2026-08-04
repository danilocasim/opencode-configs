# Platform UX (iOS vs Android)

Flutter can mimic both platforms, but users expect native conventions. Be deliberate about when you follow platform UI and when you enforce a single brand system.

## When to load

- You are designing cross-platform UI behavior.
- You need rules for back gestures, dialogs, and navigation bars.
- You are choosing Material vs Cupertino widgets.

## When NOT to load

- You only need layout/theming (`widgets-layout-and-theming.md`).
- You are only doing permission flows (`native-integration-and-permissions.md`).

## Core rules

- Android: back button must behave predictably.
- iOS: respect swipe-back and common navigation patterns.
- Use Material components by default; use Cupertino for iOS-native surfaces when it improves UX.
- Prefer platform-adaptive widgets for dialogs/pickers.
- Test on real devices for keyboard/safe areas.

## Minimal examples

Platform-adaptive dialog:

```dart
import 'dart:io' show Platform;
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

Future<void> showConfirm(BuildContext context) {
  if (Platform.isIOS) {
    return showCupertinoDialog<void>(
      context: context,
      builder: (_) => CupertinoAlertDialog(
        title: const Text('Delete?'),
        actions: [
          CupertinoDialogAction(onPressed: () => Navigator.pop(context), child: const Text('Cancel')),
          CupertinoDialogAction(isDestructiveAction: true, onPressed: () => Navigator.pop(context), child: const Text('Delete')),
        ],
      ),
    );
  }

  return showDialog<void>(
    context: context,
    builder: (_) => AlertDialog(
      title: const Text('Delete?'),
      actions: [
        TextButton(onPressed: () => Navigator.pop(context), child: const Text('Cancel')),
        FilledButton(onPressed: () => Navigator.pop(context), child: const Text('Delete')),
      ],
    ),
  );
}
```

## Anti-patterns

- Breaking Android back behavior.
- Forcing iOS users through Android-only patterns (or vice versa).
- Using platform branching everywhere instead of a few adaptive primitives.

## Checklist

- Back behavior correct.
- Adaptive UI used where it matters.
- Real device QA done.

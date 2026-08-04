# Native Integration and Permissions

Flutter can go native via plugins or platform channels. Prefer plugins first; keep any platform-channel surface small and typed.

## When to load

- You are adding a plugin that touches platform capabilities.
- You need permission UX rules.
- You are implementing a platform channel.

## When NOT to load

- You are doing UI work (use layout/theming).
- You only need routing/state.

## Core rules

- Prefer stable plugins over custom channels.
- Request permissions just-in-time.
- Handle denial as a normal state.
- Keep platform APIs typed and minimal.
- Test on real devices.

## Minimal examples

Platform channel wrapper (typed):

```dart
import 'package:flutter/services.dart';

class DeviceInfoApi {
  static const _ch = MethodChannel('com.example/device_info');

  Future<String> getModel() async {
    final v = await _ch.invokeMethod<String>('getModel');
    if (v == null || v.isEmpty) throw StateError('missing model');
    return v;
  }
}
```

Permission UX posture:

```text
explain -> request -> granted | denied | blocked
```

## Anti-patterns

- Requesting permissions on app start.
- One-off channels with no docs or parity.
- Platform-only behavior with no fallback.

## Checklist

- Plugin evaluated first.
- Permission flow handles denial.
- Platform surface typed.
- iOS/Android parity tested.

# Widgets, Layout, and Theming

Flutter layout is constraint-driven. Most UI bugs are misunderstandings of constraints, not “Flutter being weird”. A small theme/token layer prevents inconsistent UI.

## When to load

- You are building reusable widgets.
- You are setting up theming/design tokens.
- Layout behaves unexpectedly (overflow, unbounded height).

## When NOT to load

- You are optimizing performance (`performance.md`).
- You are implementing navigation (`navigation-and-routing.md`).

## Core rules

- Understand constraints: parents give constraints, children pick size.
- Avoid unbounded layouts (ListView inside Column without Expanded).
- Prefer a tokenized design system (colors/space/radius/typography).
- Use Material 3 by default unless the app is explicitly Cupertino-first.
- Keep reusable UI primitives small and predictable.

## Minimal examples

Theme tokens via `ThemeExtension`:

```dart
import 'package:flutter/material.dart';

@immutable
class AppTokens extends ThemeExtension<AppTokens> {
  const AppTokens({
    required this.space2,
    required this.space4,
    required this.radiusMd,
  });

  final double space2;
  final double space4;
  final double radiusMd;

  @override
  AppTokens copyWith({double? space2, double? space4, double? radiusMd}) {
    return AppTokens(
      space2: space2 ?? this.space2,
      space4: space4 ?? this.space4,
      radiusMd: radiusMd ?? this.radiusMd,
    );
  }

  @override
  AppTokens lerp(ThemeExtension<AppTokens>? other, double t) {
    if (other is! AppTokens) return this;
    return AppTokens(
      space2: lerpDouble(space2, other.space2, t)!,
      space4: lerpDouble(space4, other.space4, t)!,
      radiusMd: lerpDouble(radiusMd, other.radiusMd, t)!,
    );
  }
}

extension TokensX on BuildContext {
  AppTokens get tokens => Theme.of(this).extension<AppTokens>()!;
}
```

Small `AppButton` primitive:

```dart
import 'package:flutter/material.dart';

class AppButton extends StatelessWidget {
  const AppButton({
    super.key,
    required this.label,
    required this.onPressed,
    this.loading = false,
  });

  final String label;
  final VoidCallback? onPressed;
  final bool loading;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 48,
      width: double.infinity,
      child: FilledButton(
        onPressed: loading ? null : onPressed,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            if (loading)
              const Padding(
                padding: EdgeInsets.only(right: 8),
                child: SizedBox(
                  width: 16,
                  height: 16,
                  child: CircularProgressIndicator(strokeWidth: 2),
                ),
              ),
            Text(label),
          ],
        ),
      ),
    );
  }
}
```

## Anti-patterns

- Hardcoded colors/spacings everywhere.
- Nested scroll views without constraints.
- `Expanded` used as a band-aid without understanding constraints.

## Checklist

- Tokens exist and are used.
- Primitives enforce tap target sizes.
- Layout respects constraints (no overflows).
- Theme is consistent across screens.

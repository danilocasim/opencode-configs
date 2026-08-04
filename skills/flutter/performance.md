# Performance (Flutter)

Flutter performance issues are usually excessive rebuilds, expensive widget trees, and inefficient lists/images. Measure first with DevTools.

## When to load

- Scrolling is janky.
- Frames drop during animations.
- A screen rebuilds too often.

## When NOT to load

- You are doing design tokens (`widgets-layout-and-theming.md`).
- You are implementing native channels (`native-integration-and-permissions.md`).

## Core rules

- Use `const` widgets wherever possible.
- Keep build methods cheap; move work out of `build`.
- Prefer `ListView.builder` / slivers for large lists.
- Use keys intentionally (stable identity for reordering).
- Avoid excessive opacity/blur/shadows.

## Minimal examples

Make hot subtrees `const`:

```dart
class Header extends StatelessWidget {
  const Header({super.key});

  @override
  Widget build(BuildContext context) {
    return const Padding(
      padding: EdgeInsets.all(16),
      child: Text('Projects'),
    );
  }
}
```

Large list posture:

```dart
ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, i) => ProjectRow(item: items[i]),
)
```

## Anti-patterns

- Heavy work in `build()` (sorting/filtering large lists every frame).
- `ListView(children: [...])` with many items.
- Optimizing without measuring.

## Checklist

- Baseline captured in DevTools.
- Rebuild sources identified.
- Lists/images are efficient.
- Improvement verified.

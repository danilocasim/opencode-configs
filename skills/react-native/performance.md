# Performance (React Native)

React Native performance is usually about reducing re-renders, making lists efficient, and handling images responsibly.

## When to load

- Scrolling is janky.
- A screen re-renders too much.
- Lists/images are slow or memory-heavy.

## When NOT to load

- You are implementing animations (`animations-and-gestures.md`).
- You are debugging platform-only behavior (`platform-differences.md`).

## Core rules

- Lists: use `FlatList`/`SectionList` correctly; avoid rendering huge arrays in `ScrollView`.
- Keep item components pure and stable; avoid inline functions in hot lists.
- Memoize expensive derived data; avoid deep prop trees.
- Images: size correctly; avoid downloading full-res when showing thumbnails.
- Avoid excessive shadows/blur and overdraw.

If you only do 3 things:

- Fix list item stability (memo + stable props).
- Stop `ScrollView`-rendering large lists.
- Measure before/after (Perf Monitor, Flipper, traces).

## Minimal examples

FlatList with stable item component:

```tsx
import { memo, useCallback } from "react";
import { FlatList, Pressable, View } from "react-native";

type Row = { id: string; title: string };

const RowItem = memo(function RowItem({
  row,
  onPress,
}: {
  row: Row;
  onPress: (id: string) => void;
}) {
  return (
    <Pressable onPress={() => onPress(row.id)} style={{ paddingVertical: 12 }}>
      <View>{/* render row.title */}</View>
    </Pressable>
  );
});

export function RowsList({ rows, onOpen }: { rows: Row[]; onOpen: (id: string) => void }) {
  const renderItem = useCallback(
    ({ item }: { item: Row }) => <RowItem row={item} onPress={onOpen} />,
    [onOpen]
  );

  return (
    <FlatList
      data={rows}
      keyExtractor={(r) => r.id}
      renderItem={renderItem}
      initialNumToRender={12}
      windowSize={7}
      removeClippedSubviews
    />
  );
}
```

Fixed-height list optimization:

```tsx
const ROW_HEIGHT = 56;

<FlatList
  getItemLayout={(_, index) => ({ length: ROW_HEIGHT, offset: ROW_HEIGHT * index, index })}
/>;
```

Memoization rule of thumb:

```text
memoize when: list item count is high or computation is expensive
avoid when: it adds complexity with no measured benefit
```

Image sizing rule:

```text
rendered size ~ downloaded size
avoid: downloading 3000px images for 120px thumbnails
```

## Anti-patterns

- `ScrollView` with hundreds of children.
- `renderItem={() => ...}` recreating on every render.
- Fetching large images with no resizing.
- “Optimize” without measuring (Perf Monitor/Flipper).

## Checklist

- List virtualization in place.
- Hot components are stable and memoized appropriately.
- Image sizes match display sizes.
- Improvement verified with measurements.

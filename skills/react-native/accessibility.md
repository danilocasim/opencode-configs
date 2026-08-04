# Accessibility (React Native)

Accessibility is part of correctness: screen readers, focus order, labels, and reduced motion must work.

## When to load

- You are building interactive UI (forms, modals, lists).
- You are adding custom components that need labels/roles.
- You need a11y regression checklists.

## When NOT to load

- You are designing tokens and visual system (`ui-ux-and-design-system.md`).
- You are doing performance tuning (`performance.md`).

## Core rules

- Every tappable element has an accessible label.
- Use correct roles/states (selected, disabled, expanded).
- Ensure focus management for modals/sheets.
- Respect system font scaling.
- Offer reduced motion paths for heavy animations.

## Minimal examples

Label + hint:

```tsx
<Pressable
  accessibilityRole="button"
  accessibilityLabel="Add to cart"
  accessibilityHint="Adds this item to your cart"
  onPress={addToCart}
>
  <Text>Add</Text>
</Pressable>
```

## Anti-patterns

- Icon-only buttons with no label.
- Custom components that break focus order.
- Locking font sizes so text can’t scale.

## Checklist

- Labels present on interactive elements.
- Modal focus is sane.
- Font scaling tested.
- Reduced motion considered.

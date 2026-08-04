# UI/UX and Design System (React Native)

Mobile UX is constrained by touch, small screens, and motion/keyboard/safe areas. A small design system prevents inconsistency and makes screens faster to build.

## When to load

- You are designing UI components for RN.
- You need platform UX guidance (tap targets, typography, safe areas).
- You are defining tokens (colors, spacing, typography).

## When NOT to load

- You are implementing animations/gestures (`animations-and-gestures.md`).
- You are doing navigation wiring (`navigation.md`).

## Core rules

- Tap targets: prefer 44x44pt (iOS) / ~48dp (Android) minimum.
- Typography: define a type scale and use it consistently (not ad-hoc `fontSize`).
- Spacing: define a spacing scale; avoid arbitrary numbers.
- Safe areas: respect notches and home indicators.
- Keyboard: design for the keyboard; avoid hidden inputs and broken scroll.

Practical defaults:

- Prefer 1 primary action per screen; secondary actions should be visually quiet.
- Default to scrollable content; small screens + keyboard will reduce vertical space.
- Use platform conventions where they matter (Android ripple, iOS blur/sheets).

## Minimal examples

Token sketch:

```ts
export const tokens = {
  space: { 0: 0, 1: 4, 2: 8, 3: 12, 4: 16, 6: 24, 8: 32 },
  radius: { sm: 8, md: 12, lg: 16 },
  color: {
    bg: "#0B0D12",
    card: "#121622",
    text: "#F2F5FF",
    muted: "#A8B0C2",
    primary: "#4B7BFF",
    danger: "#FF4D4D",
  },
  text: {
    body: { fontSize: 16, lineHeight: 22 },
    title: { fontSize: 24, lineHeight: 30, fontWeight: "700" },
  },
} as const;
```

Minimal `Text` wrapper to keep typography consistent:

```tsx
import { Text as RNText, type TextProps } from "react-native";

type Variant = "body" | "title";

export function Text({ style, ...props }: TextProps & { variant?: Variant }) {
  const variant: Variant = (props as { variant?: Variant }).variant ?? "body";

  return (
    <RNText
      {...props}
      style={[
        variant === "title" ? tokens.text.title : tokens.text.body,
        { color: tokens.color.text },
        style,
      ]}
    />
  );
}
```

Minimal `Button` with correct touch target and accessibility:

```tsx
import { Pressable, ActivityIndicator, View } from "react-native";

export function Button({
  label,
  onPress,
  loading,
  disabled,
}: {
  label: string;
  onPress: () => void;
  loading?: boolean;
  disabled?: boolean;
}) {
  const isDisabled = Boolean(disabled || loading);

  return (
    <Pressable
      accessibilityRole="button"
      accessibilityLabel={label}
      disabled={isDisabled}
      onPress={onPress}
      style={({ pressed }) => [
        {
          minHeight: 44,
          paddingHorizontal: tokens.space[4],
          borderRadius: tokens.radius.md,
          backgroundColor: tokens.color.primary,
          opacity: pressed || isDisabled ? 0.8 : 1,
          justifyContent: "center",
        },
      ]}
    >
      <View style={{ flexDirection: "row", justifyContent: "center", gap: 8 }}>
        {loading ? <ActivityIndicator color={tokens.color.text} /> : null}
        <Text style={{ fontWeight: "700" }}>{label}</Text>
      </View>
    </Pressable>
  );
}
```

Safe area + keyboard posture:

```tsx
import { KeyboardAvoidingView, Platform, ScrollView } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

export function Screen({ children }: { children: React.ReactNode }) {
  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: tokens.color.bg }} edges={["top", "bottom"]}>
      <KeyboardAvoidingView
        style={{ flex: 1 }}
        behavior={Platform.OS === "ios" ? "padding" : undefined}
      >
        <ScrollView contentContainerStyle={{ padding: tokens.space[4], gap: tokens.space[3] }}>
          {children}
        </ScrollView>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}
```

Component posture:

```text
ui primitives: Button, Text, Stack, Card, Sheet
feature UI: composed from primitives
```

## Anti-patterns

- Tiny touch targets.
- Hardcoded colors/spacings everywhere.
- Ignoring safe areas and keyboard.
- Over-relying on shadows that look wrong cross-platform.

## Checklist

- Tokens exist (space/type/color).
- Components enforce tap target sizes.
- Safe area and keyboard behavior tested.
- Visual hierarchy is consistent across screens.

# Testing (React Native)

Mobile tests should be layered: unit tests for logic, component tests for rendering, and a small number of end-to-end tests for critical flows.

## When to load

- You are adding tests for RN components/hooks.
- You need guidance for E2E vs unit scope.
- You need deterministic patterns for time, network, and storage.

## When NOT to load

- You only need generic test philosophy (use `../testing/SKILL.md`).
- You are writing web React tests (use `../testing/typescript.md`).

## Core rules

- Prefer behavior-focused tests (what user sees/does).
- Mock boundaries (network/storage) rather than internals.
- Keep E2E small and stable (critical journeys only).
- Avoid sleep-based waits; wait on UI state.
- Make tests deterministic for CI.

## Minimal examples

Layering:

```text
unit: pure functions, hooks
component: render + interactions
e2e: login + core flow
```

Tooling map (common):

```text
unit/component: Jest + React Native Testing Library
e2e: Detox or Maestro (pick one per repo)
```

React Native Testing Library example:

```tsx
import { render, screen } from "@testing-library/react-native";
import userEvent from "@testing-library/user-event";

import { Button } from "../ui/Button";

it("calls onPress", async () => {
  const user = userEvent.setup();
  const onPress = jest.fn();

  render(<Button label="Save" onPress={onPress} />);

  await user.press(screen.getByRole("button", { name: "Save" }));
  expect(onPress).toHaveBeenCalledTimes(1);
});
```

## Anti-patterns

- Snapshot-heavy tests for interactive UI.
- E2E covering every edge case.
- Real network calls in unit tests.

## Checklist

- Tests cover key behaviors.
- Boundaries mocked.
- E2E scope minimal.
- CI runs are deterministic.

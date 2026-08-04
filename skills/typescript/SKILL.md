---
name: typescript
description: TypeScript 5.x conventions and strict type safety (2024-2026)
---

# TypeScript Conventions (TS 5.x)

## Strict Mode (Required)

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "exactOptionalPropertyTypes": true
  }
}
```

## Type Safety

- **Never use `any`** - use `unknown` and narrow
- **Avoid type assertions** (`as`) - use type guards instead
- **No non-null assertions** (`!`) - handle nullability properly
- **Explicit return types** on public functions
- **`const` assertions**: `as const` for literal types

## Modern Patterns (TS 5.x)

- **Satisfies operator**: `config satisfies Config` (validates without widening)
- **Const type parameters**: `<const T>` for literal inference
- **Decorator metadata**: Use decorators with `emitDecoratorMetadata`
- **Using declarations**: `using file = ...` for resource cleanup

## Type Definitions

- `interface` for object shapes (extendable)
- `type` for unions, intersections, mapped types
- Prefer `interface` for public APIs
- Use branded types for type-safe IDs: `type UserId = string & { __brand: 'UserId' }`

## Functions

- **Prefer `const` arrow functions**: `const fn = () => {}`
- **Async/await** over raw promises
- **Handle all errors explicitly** - no silent catches
- **Pure functions** where possible
- **Destructure params** for 3+ arguments

## Collections

- `map`, `filter`, `reduce` over loops
- `Set` and `Map` over object-as-dict
- Use `ReadonlyArray<T>` for immutable arrays
- **No `forEach`** - use `for...of` or functional methods

## Null Handling

- **Nullish coalescing**: `??` over `||` for defaults
- **Optional chaining**: `obj?.prop?.method?.()`
- **Prefer `undefined`** over `null` (usually)

## Imports

- **Named imports**: `import { foo } from 'bar'`
- **Type imports**: `import type { Foo } from 'bar'`
- **Barrel exports sparingly** - can hurt tree-shaking

## Error Handling

- **Custom error classes** extending `Error`
- **Result types** for expected failures: `type Result<T, E> = { ok: true, value: T } | { ok: false, error: E }`
- **Never throw from pure functions**

## Testing

- Vitest or Jest
- Type tests with `expectTypeOf` (Vitest) or `tsd`

## Documentation (TSDoc)

Use TSDoc for public exports in `.ts` / `.tsx`.

```ts
/**
 * Parses a user-supplied date string into a normalized ISO string.
 *
 * Why: we store dates normalized to avoid timezone bugs and inconsistent
 * formatting across environments.
 *
 * @param input - User-supplied date (e.g. "2026-01-31").
 * @param timeZone - IANA timezone (e.g. "America/Los_Angeles").
 * @returns ISO 8601 date string.
 * @throws If the input cannot be parsed.
 */
export function normalizeDate(input: string, timeZone: string): string {
  // ...
}
```

Guidelines:

- Prefer documenting public surface area (exports), not internal helpers.
- Use `@throws` only for real runtime errors.
- For `.js` files, prefer JSDoc via the `javascript` skill.

## Tools

- **ESLint + typescript-eslint**: Linting
- **Prettier** or **Biome**: Formatting
- **tsconfig strict presets**: Use recommended strict configs

## Reference Docs

- TypeScript Handbook: https://www.typescriptlang.org/docs/
- typescript-eslint Rules: https://typescript-eslint.io/rules/
- TS 5.x Release Notes: https://devblogs.microsoft.com/typescript/

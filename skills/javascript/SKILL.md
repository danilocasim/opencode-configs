---
name: javascript
description: JavaScript conventions and JSDoc documentation style (2024-2026)
---

# JavaScript Conventions (ES2022+)

## Defaults

- Prefer TypeScript when possible; use JS when the project is JS-first.
- Use ESM (`import`/`export`) unless the codebase is CommonJS.
- Prefer explicit error handling and input validation at boundaries.

## Module Systems

- Prefer ESM in new code:

```js
import { readFile } from "node:fs/promises";
export function loadConfig(path) {
  return readFile(path, "utf8");
}
```

- If the repo is CommonJS, stay consistent:

```js
const fs = require("node:fs");
module.exports = { fs };
```

## Types in JS

- Use JSDoc types for better editor support.
- Prefer narrower unions over `*`/`any`.

```js
/** @typedef {"draft" | "published" | "archived"} PostStatus */

/**
 * @typedef {Object} Post
 * @property {string} id
 * @property {PostStatus} status
 */
```

## Documentation (JSDoc)

Use JSDoc for public functions/classes in `.js` / `.jsx`.

```js
/**
 * Convert an ISO date string into a user-facing label.
 *
 * Why: UI needs a stable, locale-aware label that is consistent across pages.
 *
 * @param {string} iso - ISO 8601 string.
 * @param {{ locale?: string, timeZone?: string }} [opts]
 * @returns {string}
 * @throws {TypeError} If `iso` is not a valid ISO date.
 */
export function formatDateLabel(iso, opts = {}) {
  // ...
}
```

### JSDoc for async

```js
/**
 * Fetch a user by id.
 *
 * @param {string} id
 * @returns {Promise<{ id: string, email: string } | null>}
 */
export async function fetchUser(id) {
  // ...
}
```

### JSDoc for classes

```js
/**
 * Simple in-memory cache.
 */
export class Cache {
  /** @type {Map<string, unknown>} */
  #store = new Map();

  /**
   * @param {string} key
   * @returns {unknown | undefined}
   */
  get(key) {
    return this.#store.get(key);
  }
}
```

### Tag guidance

- Prefer description at top; avoid `@description` unless needed.
- Use `@throws` for real runtime errors, not for API misuse.
- Prefer documenting public exports; internal helpers can be undocumented.

## Error Handling

- Throw `Error` subclasses for domain failures.
- Prefer returning `null`/`undefined` for “not found” instead of throwing.

```js
export class NotFoundError extends Error {
  constructor(message) {
    super(message);
    this.name = "NotFoundError";
  }
}
```

## Testing

- Prefer the project's standard (Jest or Vitest).
- For Node HTTP: consider MSW or nock depending on the repo.
- Test behavior; avoid brittle implementation assertions.

## Reference Docs

- JSDoc: https://jsdoc.app/
- Node.js ESM: https://nodejs.org/api/esm.html

### Common tags

- `@param` for parameters
- `@returns` for return values
- `@throws` for error conditions
- `@example` for usage examples

## Testing

- Prefer the project standard (Jest or Vitest).
- Test behavior; avoid brittle implementation assertions.

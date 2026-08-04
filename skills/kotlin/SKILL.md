---
name: kotlin
description: Kotlin conventions for Android/JVM (2024-2026)
---

# Kotlin Conventions (Kotlin 2.0+)

## Style Essentials

- 4 spaces indentation
- `camelCase` for functions/properties
- `PascalCase` for classes/interfaces

## Documentation (KDoc)

Use KDoc (`/** ... */`) for public APIs.

```kotlin
/**
 * Normalize a user-supplied date string.
 *
 * Why: normalization avoids timezone drift and inconsistent formatting.
 *
 * @param input User-supplied date.
 * @param timeZone IANA timezone identifier.
 * @return ISO 8601 date string.
 * @throws IllegalArgumentException if the input cannot be parsed.
 */
fun normalizeDate(input: String, timeZone: String): String {
    // ...
    throw IllegalArgumentException("parse failed")
}
```

## Index

- Core patterns: `skills/kotlin/kotlin-core.md`
- Testing: `skills/kotlin/kotlin-testing.md`
- Configuration: `skills/kotlin/kotlin-config.md`

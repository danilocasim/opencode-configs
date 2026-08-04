---
name: swift
description: Swift conventions for iOS/macOS (2024-2026)
---

# Swift Conventions (Swift 5.9+)

## Style Essentials

- 4 spaces indentation
- `camelCase` for functions/variables
- `PascalCase` for types/protocols

## Documentation (SwiftDoc)

Use SwiftDoc comments (`///`) for public APIs.

```swift
/// Normalize a user-supplied date string.
///
/// - Parameters:
///   - input: User-supplied date.
///   - timeZone: IANA timezone identifier.
/// - Returns: ISO 8601 date string.
/// - Throws: `DateError.parseFailed` if the input cannot be parsed.
public func normalizeDate(_ input: String, timeZone: String) throws -> String {
    // ...
    throw DateError.parseFailed
}
```

## Index

- Core patterns: `skills/swift/swift-core.md`
- Testing: `skills/swift/swift-testing.md`
- Configuration: `skills/swift/swift-config.md`

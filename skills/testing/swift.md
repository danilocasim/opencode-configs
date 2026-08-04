# Swift Testing (XCTest)

## When to load

- You are writing XCTest unit/integration tests for Swift modules.
- You need patterns for async/await tests and dependency isolation.

## When NOT to load

- You are doing iOS UI automation at the app level (separate from unit tests).
- You mainly need mocking discipline concepts (use `test-doubles-and-mocking-discipline.md`).

## Core rules

- Keep business logic in testable types; inject dependencies via protocols.
- Prefer testing public behavior over private helpers.
- Use async XCTest APIs for async code; avoid sleep-based waiting.
- Keep tests deterministic; control clocks and random sources.

## Common patterns

- Protocol-based fakes for repositories/clients.
- `XCTAssertThrowsError` for error contracts.
- Async test methods for `async` functions.
- Small helper constructors/builders for setup.

## Minimal examples

```swift
import XCTest
@testable import MyApp

final class NormalizeDateTests: XCTestCase {
    func testReturnsIsoDate() throws {
        let iso = try normalizeDate("2026-01-31", timeZone: "UTC")
        XCTAssertEqual(iso, "2026-01-31")
    }
}
```

Async test:

```swift
func testLoadsProfile() async throws {
    let profile = try await service.loadProfile(userId: "u_123")
    XCTAssertEqual(profile.id, "u_123")
}
```

## Anti-patterns

- Testing via the UI when a unit test can prove the behavior.
- Sleep-based polling instead of awaiting/expectations.
- Mocks that assert long call sequences rather than outcomes.

## Checklist

- Are dependencies injected via protocols (not hidden singletons)?
- Are async tests using `async`/`await` rather than timeouts/sleeps?
- Does the test assert observable outcomes?
- Is the test fast enough to run frequently?

## References

- XCTest: https://developer.apple.com/documentation/xctest

# Swift Testing (XCTest)

## Defaults

- Use XCTest
- Prefer protocol-based mocks
- Use async XCTest when needed

```swift
import XCTest
@testable import MyApp

final class UserTests: XCTestCase {
    func testUserDecoding() throws {
        let json = """
        {"id": 1, "name": "Test"}
        """.data(using: .utf8)!

        let user = try JSONDecoder().decode(User.self, from: json)
        XCTAssertEqual(user.id, 1)
    }

    func testFetchUser() async throws {
        let service = MockUserService()
        let user = try await service.fetchUser(id: 1)
        XCTAssertEqual(user.name, "Test User")
    }
}
```

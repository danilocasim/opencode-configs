# Swift Core Patterns

## Modern Swift (5.9+)

- Structured concurrency: `async`/`await`, task groups
- Actors for shared mutable state
- Observation: `@Observable` when available

```swift
actor DataCache {
    private var cache: [String: Data] = [:]

    func store(_ data: Data, for key: String) {
        cache[key] = data
    }
}

func fetchData(from url: URL) async throws -> Data {
    let (data, _) = try await URLSession.shared.data(from: url)
    return data
}
```

## Optionals

- Prefer `guard let` for early exit
- Avoid force unwrap (`!`) outside tests

```swift
func displayName(user: User?) -> String {
    guard let user else { return "Anonymous" }
    return user.nickname ?? user.name
}
```

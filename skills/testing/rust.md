# Rust Testing

## When to load

- You are writing `cargo test` unit/integration tests.
- You need patterns for async tests and ergonomics.

## When NOT to load

- You primarily need CI flake strategy (use `ci-reliability-and-flake-control.md`).
- You are doing browser E2E (use `e2e-playwright.md`).

## Core rules

- Unit tests live next to code (`mod tests`); integration tests go in `tests/`.
- Prefer assertions on public behavior; keep private-helper testing rare.
- Use `Result<(), anyhow::Error>` (or similar) in tests when it improves clarity.
- Keep tests deterministic; avoid real network unless explicitly integration.

## Common patterns

- `#[cfg(test)] mod tests { ... }` for unit tests.
- `tests/` for crate-level integration (public API) tests.
- `#[tokio::test]` for async behavior.
- Use builders for setup to keep tests readable.

## Minimal examples

Unit test:

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn normalizes_email() {
        assert_eq!(normalize_email("A@B.COM"), "a@b.com");
    }
}
```

Async test:

```rust
#[tokio::test]
async fn returns_ok_json() {
    let res = handler().await;
    assert_eq!(res.status(), 200);
}
```

## Anti-patterns

- Tests that depend on execution order.
- Overusing integration tests for logic that can be unit-tested.
- Spawning background tasks that outlive the test without cleanup.

## Checklist

- Is the test in the right place (unit vs integration)?
- Are async tasks awaited and cleaned up?
- Are external dependencies stubbed or scoped to explicit integration suites?
- Are failure messages clear enough to debug quickly?

## References

- Rust book testing chapter: https://doc.rust-lang.org/book/ch11-00-testing.html
- Tokio testing: https://tokio.rs/tokio/topics/testing

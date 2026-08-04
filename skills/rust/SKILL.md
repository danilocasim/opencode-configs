---
name: rust
description: Rust conventions and idiomatic patterns (2024-2026)
---

# Rust Conventions (Rust 2024 Edition)

## Core Principles

- **Embrace the borrow checker** - don't fight it
- **Zero-cost abstractions** - prefer compile-time over runtime
- **Explicit over implicit** - no hidden behavior

## Naming (RFC 430)

- `snake_case`: functions, methods, variables, modules, crates
- `CamelCase`: types, traits
- `SCREAMING_SNAKE_CASE`: constants, statics
- `_unused`: prefix for intentionally unused variables

## Error Handling

```rust
// NEVER in production
value.unwrap();      // Bad
value.expect("msg"); // Acceptable only for truly impossible cases

// ALWAYS use proper error handling
let value = match result {
    Ok(v) => v,
    Err(e) => return Err(e.into()),
};

// Or use the ? operator
let value = result?;
```

- **`Result<T, E>`** for recoverable errors
- **`Option<T>`** for optional values
- **`?` operator** for propagation
- **Custom error types** with `thiserror`
- **`anyhow`** for application code, `thiserror` for libraries

## Types

- **Prefer borrowing** (`&T`) over owning (`T`) when possible
- **Use `Cow<'_, T>`** for optional ownership
- **Newtype pattern** for type safety: `struct UserId(u64);`
- **Builder pattern** for complex construction
- **Type state pattern** for compile-time state machines

## Traits

- Implement standard traits: `Debug`, `Clone`, `PartialEq`, `Eq`, `Hash`
- **Derive when possible**: `#[derive(Debug, Clone, PartialEq)]`
- **Sealed traits** for non-extensible APIs
- Prefer **trait bounds** over trait objects when possible

## Lifetimes

- **Elide when possible** - compiler infers most
- **Named lifetimes** when relationships matter
- **`'static`** only when truly needed

## Async (Tokio/async-std)

```rust
// Prefer async for I/O-bound work
async fn fetch_data(url: &str) -> Result<Data, Error> {
    let response = reqwest::get(url).await?;
    let data = response.json().await?;
    Ok(data)
}
```

- **`tokio`** for async runtime (most common)
- **Avoid blocking** in async contexts
- **`spawn_blocking`** for CPU-bound work in async

## Memory & Performance

- **Prefer stack allocation** when size is known
- **`Vec::with_capacity`** when size is predictable
- **Avoid cloning** when borrowing works
- **`Rc`/`Arc`** only when shared ownership needed

## Documentation

````rust
/// Brief description.
///
/// Longer explanation if needed.
///
/// # Examples
///
/// ```
/// let result = my_function(42);
/// assert_eq!(result, 84);
/// ```
///
/// # Errors
///
/// Returns `Err` if the input is negative.
///
/// # Panics
///
/// Panics if the input overflows.
pub fn my_function(x: i32) -> Result<i32, MyError> {
    // ...
}
````

Guidelines:

- Use `///` for public items.
- Prefer sections: `# Examples`, `# Errors`, `# Panics`.
- Keep examples runnable when possible.

## Project Structure

```
src/
  lib.rs        # Library root
  main.rs       # Binary entry (optional)
  module/
    mod.rs      # Module root
    submod.rs   # Submodule
tests/
  integration_test.rs
Cargo.toml
```

## Testing

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic() {
        assert_eq!(add(2, 2), 4);
    }
}
```

## Tools

- **`cargo fmt`**: Formatting (rustfmt)
- **`cargo clippy`**: Linting (VERY strict - use it!)
- **`cargo test`**: Testing
- **`cargo doc`**: Documentation

## Clippy Lints (Enable these)

```toml
# Cargo.toml or .cargo/config.toml
[lints.clippy]
pedantic = "warn"
nursery = "warn"
unwrap_used = "deny"
expect_used = "warn"
```

## Reference Docs

- Rust Book: https://doc.rust-lang.org/book/
- API Guidelines: https://rust-lang.github.io/api-guidelines/
- Clippy Lints: https://rust-lang.github.io/rust-clippy/
- Rust by Example: https://doc.rust-lang.org/rust-by-example/

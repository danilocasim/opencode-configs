# Kotlin Testing (JUnit 5 + MockK)

## When to load

- You are testing Kotlin services, domain logic, or JVM modules.
- You need coroutine testing patterns.

## When NOT to load

- You are writing full-stack E2E tests (use `e2e-playwright.md`).
- You mainly need property-based exploration (use `property-based-testing.md`).

## Core rules

- Prefer behavior-focused tests; assert outputs/state/events.
- Keep dependencies injectable (constructor injection) for easy fakes.
- Use MockK sparingly; prefer fakes for most unit tests.
- For coroutines, use `kotlinx-coroutines-test` and `runTest`.

## Common patterns

- JUnit 5 test classes with minimal setup.
- Coroutine tests via `runTest` and controlled dispatchers.
- `assertThrows` for error contracts.
- Small test builders/fixtures for readability.

## Minimal examples

MockK example (boundary stub):

```kotlin
import io.mockk.every
import io.mockk.mockk
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

class UserServiceTest {
    private val repo = mockk<UserRepository>()
    private val service = UserService(repo)

    @Test
    fun `returns user when found`() {
        every { repo.findById(1) } returns User(1, "John")
        assertEquals("John", service.getUser(1).name)
    }
}
```

Coroutine test:

```kotlin
import kotlinx.coroutines.test.runTest
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

class ProfileServiceTest {
    @Test
    fun `loads profile`() = runTest {
        val profile = service.loadProfile("u_123")
        assertEquals("u_123", profile.id)
    }
}
```

## Anti-patterns

- Mocking chains of internal calls instead of asserting outcomes.
- Running coroutine tests on real dispatchers (timing flakes).
- Huge shared fixtures that hide what matters.

## Checklist

- Are coroutine tests using `runTest` with controlled time/dispatchers?
- Are mocks limited to true boundaries?
- Are both success and failure paths covered?
- Is the test fast and deterministic in CI?

## References

- JUnit 5: https://junit.org/junit5/
- MockK: https://mockk.io/
- kotlinx-coroutines-test: https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-test/

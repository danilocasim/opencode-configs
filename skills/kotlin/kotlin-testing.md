# Kotlin Testing

## Defaults

- JUnit 5
- MockK for mocking
- Prefer behavior-focused tests

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

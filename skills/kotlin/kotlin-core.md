# Kotlin Core Patterns

## Null safety

- Prefer non-null types
- Use `?.` and `?:`
- Avoid `!!`

```kotlin
fun displayName(nickname: String?, name: String): String {
    return nickname ?: name
}
```

## Coroutines

```kotlin
suspend fun fetchUser(id: Long): User = withContext(Dispatchers.IO) {
    api.getUser(id)
}

suspend fun loadDashboard(): Dashboard = coroutineScope {
    val user = async { fetchUser(1) }
    val stats = async { api.getStats() }
    Dashboard(user.await(), stats.await())
}
```

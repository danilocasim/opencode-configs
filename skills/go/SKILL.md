---
name: go
description: Go conventions and idiomatic patterns (2024-2026)
---

# Go Conventions (Go 1.22+)

## Style Essentials

- `gofmt` is the law - no debate
- Package names: short, lowercase, no underscores
- Exported names: `CamelCase`
- Unexported names: `camelCase`

## Modern Go (1.22+)

```go
// Range over integers (1.22+)
for i := range 10 {
    fmt.Println(i)
}

// Generic functions
func Min[T constraints.Ordered](a, b T) T {
    if a < b {
        return a
    }
    return b
}

// Structured logging (1.21+)
logger := slog.New(slog.NewJSONHandler(os.Stdout, nil))
logger.Info("user created", "id", userID, "email", email)
```

## Project Structure

```
project/
├── cmd/
│   └── server/
│       └── main.go          # Application entry point
├── internal/
│   ├── domain/
│   │   └── user.go          # Domain models
│   ├── service/
│   │   └── user.go          # Business logic
│   ├── repository/
│   │   └── user.go          # Data access
│   └── handler/
│       └── user.go          # HTTP handlers
├── pkg/
│   └── validator/           # Public shared packages
├── migrations/              # Database migrations
├── go.mod
├── go.sum
└── Makefile
```

## Error Handling

```go
// Return errors, don't panic
func fetchUser(id int) (*User, error) {
    user, err := db.Query(id)
    if err != nil {
        return nil, fmt.Errorf("failed to fetch user %d: %w", id, err)
    }
    return user, nil
}

// Check errors immediately
user, err := fetchUser(42)
if err != nil {
    log.Printf("Error: %v", err)
    return
}

// Error comparison
if errors.Is(err, sql.ErrNoRows) {
    return nil, ErrUserNotFound
}
```

## Patterns

```go
// Accept interfaces, return structs
type Reader interface {
    Read(p []byte) (n int, err error)
}

func ProcessData(r Reader) (*Result, error) {
    // Accept interface
}

// Small interfaces (1-3 methods)
type Storer interface {
    Get(ctx context.Context, id string) (*Item, error)
    Save(ctx context.Context, item *Item) error
}

// Context for cancellation
func fetchWithTimeout(ctx context.Context, url string) (*Response, error) {
    ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel()

    req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
    if err != nil {
        return nil, err
    }
    return http.DefaultClient.Do(req)
}
```

## Testing

```go
// Table-driven tests
func TestCalculate(t *testing.T) {
    tests := []struct {
        name     string
        a, b     int
        expected int
    }{
        {"positive", 2, 3, 5},
        {"negative", -2, -3, -5},
        {"mixed", -2, 3, 1},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            result := Calculate(tt.a, tt.b)
            if result != tt.expected {
                t.Errorf("Calculate(%d, %d) = %d; want %d",
                    tt.a, tt.b, result, tt.expected)
            }
        })
    }
}

// Testify assertions (optional)
import "github.com/stretchr/testify/assert"

func TestWithTestify(t *testing.T) {
    result := Calculate(2, 3)
    assert.Equal(t, 5, result)
    assert.NotNil(t, result)
}
```

## Documentation (GoDoc)

Use GoDoc comments for exported identifiers.

```go
// UserStore persists and retrieves users.
//
// Why: isolates storage concerns so services can be tested without a database.
type UserStore interface {
    Get(ctx context.Context, id string) (*User, error)
    Save(ctx context.Context, user *User) error
}

// NormalizeEmail lowercases and trims an email address.
func NormalizeEmail(s string) string {
    return strings.ToLower(strings.TrimSpace(s))
}
```

Guidelines:

- Start with the identifier name (`Foo ...`).
- Keep comments as close as possible to what a consumer needs.

## Configuration (go.mod)

```go
module github.com/user/project

go 1.22

require (
    github.com/go-chi/chi/v5 v5.0.12
    github.com/lib/pq v1.10.9
)
```

## Tools

- `gofmt` / `goimports`: Formatting (enforced)
- `golangci-lint`: Comprehensive linting
- `go vet`: Static analysis
- `go test -race`: Race condition detection

## Reference Docs

- Effective Go: https://go.dev/doc/effective_go
- Go Code Review: https://go.dev/wiki/CodeReviewComments
- Go Proverbs: https://go-proverbs.github.io/

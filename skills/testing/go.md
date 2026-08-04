# Go Testing (testing)

## When to load

- You are testing Go packages, HTTP handlers, or service boundaries.
- You want idiomatic table-driven tests and fast isolation.

## When NOT to load

- You are doing browser E2E (use `e2e-playwright.md`).
- You primarily need mocking discipline concepts (use `test-doubles-and-mocking-discipline.md`).

## Core rules

- Prefer table-driven tests for case matrices.
- Make dependencies explicit (interfaces/constructors) to avoid globals.
- Keep unit tests pure and fast; use `httptest` for HTTP boundaries.
- Assert contracts: status codes, payload shape, and errors.

## Common patterns

- `t.Run` subtests with a small struct table.
- `httptest.NewRecorder` + `httptest.NewRequest` for handlers.
- `t.Helper()` in shared assertion helpers.
- `testdata/` for file fixtures.

## Minimal examples

Table-driven unit test:

```go
func TestNormalizeEmail(t *testing.T) {
  t.Parallel()

  tests := []struct {
    name string
    in   string
    want string
  }{
    {"basic", "A@B.COM", "a@b.com"},
    {"trim", "  a@b.com ", "a@b.com"},
  }

  for _, tt := range tests {
    tt := tt
    t.Run(tt.name, func(t *testing.T) {
      t.Parallel()

      got := NormalizeEmail(tt.in)
      if got != tt.want {
        t.Fatalf("got %q want %q", got, tt.want)
      }
    })
  }
}
```

HTTP handler test:

```go
req := httptest.NewRequest("GET", "/health", nil)
rr := httptest.NewRecorder()

handler.ServeHTTP(rr, req)

if rr.Code != http.StatusOK {
  t.Fatalf("status=%d", rr.Code)
}
```

## Anti-patterns

- Tests that rely on shared mutable package-level state.
- Integration tests masquerading as unit tests (real DB/network) in `*_test.go`.
- Huge tables where failures are unreadable (split by behavior).

## Checklist

- Are subtests isolated (especially with `t.Parallel`) and deterministic?
- Does each test case name communicate behavior?
- Are boundaries tested at the right level (pure vs `httptest`)?
- Is the failure output immediately actionable?

## References

- Go testing package: https://pkg.go.dev/testing
- `httptest`: https://pkg.go.dev/net/http/httptest

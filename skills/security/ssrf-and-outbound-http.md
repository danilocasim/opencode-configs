# SSRF and Outbound HTTP

If your server can fetch arbitrary URLs, attackers will try to make it fetch internal services. Outbound HTTP must be bounded and allowlisted.

## When to load

- You are adding an HTTP client call based on user input.
- You are implementing webhook “callback URLs”.
- You are downloading remote files.

## When NOT to load

- You only need timeout/retry behavior (see stack HTTP client docs).
- You are working on file upload storage (`file-uploads.md`).

## Core rules

- Prefer allowlisting hosts/domains.
- Block link-local, loopback, and private network ranges.
- Resolve DNS carefully; protect against DNS rebinding.
- Set strict timeouts and response size limits.
- Do not follow redirects to untrusted hosts.

## Minimal examples

Allowlist posture:

```text
allowed_hosts = {"api.stripe.com", "example.com"}
reject if parsed_host not in allowed_hosts
```

## Anti-patterns

- `fetch(userProvidedUrl)` without validation.
- Allowing redirects with no host checks.
- No timeouts (DoS + resource exhaustion).

## Checklist

- Host allowlist in place.
- Private IP ranges blocked.
- Redirect policy safe.
- Timeouts and size limits configured.

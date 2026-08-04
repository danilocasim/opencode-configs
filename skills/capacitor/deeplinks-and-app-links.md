# Deep Links, Universal Links, and App Links

Deep linking is a contract: the OS opens your app, you parse params safely, and you land users in the right screen without security bugs.

## When to load

- You are adding deep links.
- You need iOS Universal Links / Android App Links guidance.
- You need safe param parsing and routing.

## When NOT to load

- You only need navigation in the web app.
- You are doing push notification payload design (see push guidance).

## Core rules

- Treat link params as untrusted input; validate and normalize.
- Keep link-to-screen mapping centralized.
- Avoid open redirects.
- Test cold start and warm start behaviors.

## Minimal examples

Param validation posture:

```text
parse url -> allowlist routes -> validate ids -> navigate
```

## Anti-patterns

- String-splitting URLs without parsing.
- Allowing arbitrary redirects.
- Different link handling per screen.

## Checklist

- Routes are allowlisted.
- Params validated.
- Cold/warm start tested.
- Security reviewed (no open redirect).

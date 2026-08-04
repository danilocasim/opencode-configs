# Transactions and Consistency

Transactions exist to protect invariants. Use them to make multi-step writes atomic and to prevent partial state.

## When to load

- You have a multi-step write that must be all-or-nothing.
- You need a rule for where to put transaction boundaries.
- You are fixing race conditions or double-writes.

## When NOT to load

- You are optimizing query performance (`query-performance-and-n-plus-1.md`).
- You are planning schema changes (`migrations-and-backfills.md`).

## Core rules

- Put the transaction boundary at the domain boundary (service layer), not deep in helpers.
- Keep transactions short; avoid network calls inside.
- Use row locks when concurrency can break invariants.
- Enforce critical uniqueness with DB constraints.
- Make retry behavior explicit if serialization errors can happen.

## Minimal examples

Short transaction with a lock (pseudo):

```text
begin
  lock user row
  check invariant
  write related rows
commit
```

## Anti-patterns

- Long transactions that include HTTP calls.
- Relying on “check then insert” without constraints.
- Hiding transactions inside model callbacks.

## Checklist

- Transaction boundary is explicit.
- No external IO inside the transaction.
- Concurrency hazards addressed (locks/constraints).
- Failure modes are defined (retry vs fail).

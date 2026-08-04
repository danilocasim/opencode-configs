# GitHub Actions

View workflow runs, download logs, and manage Actions using `gh run` and `gh workflow`.

## When to load

- You are debugging a failed CI run.
- You need to view or download workflow logs.
- You want to manually trigger a workflow.

## When NOT to load

- You are working with PRs or issues (use `prs.md` or `issues.md`).

## Core commands

```bash
gh run list                          # List recent runs
gh run view <run-id>                 # View run details
gh run view --web                    # Open run in browser
gh run download <run-id>             # Download artifacts
gh run watch                         # Watch run in progress
gh run rerun <run-id>                # Rerun a workflow
gh run cancel <run-id>               # Cancel a run
gh run delete <run-id>               # Delete a run
gh workflow list                     # List workflows
gh workflow view <workflow>          # View workflow details
gh workflow run <workflow>           # Trigger workflow
```

## Common patterns

### View recent runs

```bash
gh run list --limit 10
gh run list --workflow ci.yml
gh run list --branch main
gh run list --status failure
```

### Debug a failed run

```bash
gh run view 1234567890               # View run summary
gh run view 1234567890 --log         # View all logs
gh run view 1234567890 --log-failed  # Only failed job logs
gh run view 1234567890 --web         # Open in browser
```

### Download artifacts

```bash
gh run download 1234567890           # Download all artifacts
gh run download 1234567890 -n test-results  # Download specific artifact
```

### Watch a running workflow

```bash
gh run watch                         # Watch latest run
gh run watch 1234567890              # Watch specific run
gh run watch --exit-status           # Exit with run's status
```

### Trigger a workflow

```bash
gh workflow run ci.yml
gh workflow run deploy.yml --ref main
gh workflow run deploy.yml -f environment=staging
gh workflow run deploy.yml --field tag=v1.2.3
```

### View workflow info

```bash
gh workflow list
gh workflow view ci.yml
gh workflow view ci.yml --yaml
```

## Minimal examples

Debug latest failed run:

```bash
gh run list --status failure --limit 1 --json databaseId -q '.[0].databaseId' | xargs -I{} gh run view {} --log-failed
```

Watch and exit with status:

```bash
gh run watch --exit-status && echo "CI passed" || echo "CI failed"
```

Trigger deployment:

```bash
gh workflow run deploy.yml -f environment=production -f version=v2.1.0
```

## Anti-patterns

- Using `--web` in scripts (blocks terminal).
- Not using `--log-failed` when debugging (too much noise).
- Triggering workflows without checking required inputs.

## Checklist

- Use `--log-failed` to focus on failures.
- Download artifacts before they expire.
- Use `--field` or `-f` for workflow inputs.
- Watch runs with `--exit-status` for scripting.

## References

- `gh run --help`
- `gh workflow --help`

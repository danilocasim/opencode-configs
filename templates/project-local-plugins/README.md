# Project-Local Plugins Template

Project-local plugins live in `.opencode/plugins/` inside a repo.

Use them to enforce your workflow (guardrails), integrate tooling, or inject context during compaction.

This template provides a safe default plugin that:

- Tracks which skills were loaded in the session.
- Blocks file modifications until at least one skill has been loaded.
- Injects the loaded skill names into the compaction context.

If you want stricter enforcement, use the `ProjectSkillGuard` variant instead:

- `.opencode/plugins/project-skill-guard.ts` blocks edits until the `project` skill is loaded.

Install dependencies:

```bash
# in your project root
mkdir -p .opencode
cat > .opencode/package.json <<'JSON'
{
  "dependencies": {
    "@opencode-ai/plugin": "^1.1.56"
  }
}
JSON
```

Then copy `.opencode/plugins/` from this template.

Note: plugins are loaded automatically from `.opencode/plugins/`.

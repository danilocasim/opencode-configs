# Shared Agent Instructions

These are portable user-level defaults shared by OpenCode, Claude Code, Codex,
and Kilo. Project-local rules and skills always take precedence.

## Working method

- Prefer retrieval-led reasoning: inspect the real repository before guessing.
- Read the files, tests, manifests, and local instructions relevant to the task.
- Preserve unrelated user or concurrent-agent changes.
- Keep changes minimal, localized, and consistent with existing patterns.
- Ask one focused question when missing information would materially change the
  implementation.

## Skills

- Load the smallest relevant skill set before non-trivial work.
- Prefer project-local skills, then user-level skills from the tool's configured
  skill directory.
- Load a stack or framework skill plus `testing` for behavior changes.
- Load `documentation` for public APIs and `security` for untrusted input,
  authentication, credentials, external services, or sensitive data.
- Follow each skill's routing table instead of loading every leaf document.

## Quality

- Prefer deterministic, behavior-focused tests and TDD when feasible.
- Validate inputs at boundaries and handle important failure paths explicitly.
- Document public APIs and explain why a non-obvious decision exists.
- Run targeted checks first, then broader checks when shared behavior changes.
- Review the final diff and report exact validation results.

## Git and safety

- Check repository status before editing and preserve pre-existing changes.
- Do not commit, push, rewrite history, merge, or create a release unless the
  user explicitly requests it.
- Never expose or commit secrets, credentials, tokens, private keys, or `.env`
  files.
- Never drop, reset, or destroy a database as a first option. Exhaust safe
  migration, repair, skip, and backfill paths first; destructive recovery needs
  explicit informed consent.
- Avoid broad destructive cleanup. Remove only resources created for the current
  task after verifying they contain no valuable work.

## Tool-specific loading

- OpenCode and Kilo load their global instructions, agents, commands, and skills
  from their configured user directories.
- Claude Code uses `CLAUDE.md`, `commands/`, and `skills/`.
- Codex uses `AGENTS.md` plus user skills discovered from `~/.agents/skills`.

The canonical shared configuration is `~/.agent-configs`, linked to this
repository. Tool-native authentication, provider, cache, session, and state
files remain separate and must not be shared by symlink.

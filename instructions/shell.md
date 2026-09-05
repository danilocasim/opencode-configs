# Non-Interactive Shell

Shell commands have no interactive terminal. Complete authorized work without
opening editors, pagers, REPLs, or prompts that wait for terminal input.

- Use tool-specific non-interactive flags and bounded timeouts. A non-interactive
  flag does not authorize installation, deletion, overwrite, deployment, or Git
  publication; obtain the required approval first.
- Prefer dedicated read/search/edit tools. Quote paths and use the shell tool's
  working-directory parameter rather than changing directories inside commands.
- When needed, set `CI=true`, `GIT_TERMINAL_PROMPT=0`, `GIT_EDITOR=true`, and
  `GIT_PAGER=cat` explicitly for the command. This document sets no environment
  variables by itself. Use `--help` to verify unfamiliar flags.
- Use explicit filenames for staging and `git commit -m` only when committing is
  authorized. Preserve unrelated work and existing hooks; avoid blanket staging.
- Preserve lockfile/immutable-install checks and SSH host-key verification.
  Use `ssh -o BatchMode=yes -o StrictHostKeyChecking=yes` with a verified host key;
  report a missing key instead of bypassing verification.
- Do not add force flags or pipe `yes` to an unknown prompt. If a command has no
  safe non-interactive mode, report the exact blocked action and a supported
  alternative. Permission approval belongs in the agent conversation, not stdin.
- Continue through applicable verification and cleanup of task-created resources.
  Stop for material ambiguity, denied actions, or repeated evidence-based failure;
  report passed, failed, and blocked checks separately.

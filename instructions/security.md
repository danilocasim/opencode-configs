# Security Instructions

- Validate inputs at boundaries.
- Avoid logging secrets.
- Inspect configuration through allowlisted fields; never dump resolved credentials or runtime authentication files such as `service.json` into tool output, memory, or reports.
- Prefer least privilege.
- File-tool denials are not a sandbox. Never use shell interpreters, formatters, browser execution, or other tools to bypass a denied operation; ask for an approved safe path instead.
- Use `skills/security/SKILL.md` for common vuln checklists.

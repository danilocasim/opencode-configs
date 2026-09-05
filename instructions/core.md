# Core Instructions

- Prefer retrieval-led reasoning: read/search before guessing.
- Match the repo style and conventions.
- Keep changes minimal and localized.
- Avoid destructive operations unless explicitly requested.
- Delegate only through configured `task` permissions and stay within the configured `subagent_depth`.
- Skills supply task methods, not authorization: the user's scope and the active agent's execution boundary govern delegation, commits, pushes, PRs, and deployment. Load only guidance that addresses the current task's uncertainty or risk.

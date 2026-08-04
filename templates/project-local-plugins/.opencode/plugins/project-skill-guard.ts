import type { Plugin } from "@opencode-ai/plugin";

type EditLikeTool = "edit" | "write" | "patch" | "multiedit";

function isEditLikeTool(tool: string): tool is EditLikeTool {
  return tool === "edit" || tool === "write" || tool === "patch" || tool === "multiedit";
}

/**
 * Strict guardrail plugin:
 * - blocks file modifications until the project-local `project` skill is loaded
 * - injects the loaded-skill set into compaction context
 */
export const ProjectSkillGuard: Plugin = async () => {
  const loaded = new Set<string>();

  return {
    "tool.execute.after": async (input) => {
      if (input.tool !== "skill") return;

      const name = String((input.args as { name?: unknown } | undefined)?.name ?? "").trim();
      if (name) loaded.add(name);
    },

    "tool.execute.before": async (input) => {
      if (!isEditLikeTool(input.tool)) return;
      if (loaded.has("project")) return;

      throw new Error(
        "ProjectSkillGuard: load the project-local `project` skill before editing files (create it under .opencode/skills/project/SKILL.md)."
      );
    },

    "experimental.session.compacting": async (_input, output) => {
      if (loaded.size === 0) return;

      output.context.push(
        `## Skills loaded in this session\n\n${Array.from(loaded)
          .sort()
          .map((s) => `- ${s}`)
          .join("\n")}`
      );
    },
  };
};

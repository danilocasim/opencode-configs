import type { Plugin } from "@opencode-ai/plugin";

type EditLikeTool = "edit" | "write" | "patch" | "multiedit";

function isEditLikeTool(tool: string): tool is EditLikeTool {
  return tool === "edit" || tool === "write" || tool === "patch" || tool === "multiedit";
}

/**
 * Guardrail plugin:
 * - records loaded skills
 * - blocks file modifications until at least one skill is loaded
 * - injects loaded skills into compaction context
 */
export const SkillGuard: Plugin = async () => {
  const loaded = new Set<string>();

  return {
    "tool.execute.after": async (input) => {
      if (input.tool !== "skill") return;

      const name = String((input.args as { name?: unknown } | undefined)?.name ?? "").trim();
      if (name) loaded.add(name);
    },

    "tool.execute.before": async (input) => {
      if (!isEditLikeTool(input.tool)) return;
      if (loaded.size > 0) return;

      throw new Error(
        "SkillGuard: load skills before editing files. Prefer project-local skills under .opencode/skills/* first, then global routers + leaves."
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

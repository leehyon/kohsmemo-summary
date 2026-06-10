# 构建 Claude Code 的经验：我们如何使用 Skills
- URL: https://transcrab.onev.cat/a/2026/03/lessons-from-building-claude-code-how-we-use-skills/
- Added: 2026-06-10 02:06:47
- Tags: #agent #skill #best-practice

## TL;DR
本文总结了 Anthropic 在 Claude Code 中使用 Skills 的经验，包括 9 种技能类型（如库参考、验证、自动化）及编写技巧（如建立 Gotchas、渐进式披露、避免过度约束），强调通过文件夹结构提供精准上下文，并持续迭代优化。

## Summary
本文总结了 Anthropic 团队在 Claude Code 中使用 Skills 的经验，涵盖 9 种常见技能类型、编写技巧以及分发与管理方法。核心观点是 Skills 不仅是 Markdown 文件，更是包含脚本和资源的文件夹，可灵活扩展 Claude 的能力。建议聚焦单一类型、利用 Gotchas 章节、渐进式披露，并避免过度约束流程。

**逻辑脉络**
- 先定义 Skills 是什么：文件夹，可包含脚本、资源、数据，Agent 能发现并操作。
- 分类介绍 9 种技能类型：库与 API 参考、产品验证、数据获取与分析、业务流程与团队自动化、代码脚手架与模板、代码质量与评审、CI/CD 与部署、Runbook、基础设施运维。
- 给出编写技巧：不陈述显而易见的事、建立 Gotchas 章节、利用文件系统与渐进式披露、避免绑死流程、想清楚初始化流程、Description 写给模型看、利用 Memory 与数据存储、存脚本让 Claude 生成代码、按需使用 Hooks。
- 分发 Skills：可放入 repo 或通过 Plugin Marketplace 共享；组合 Skills 时可通过名称引用；使用 PreToolUse hook 衡量使用情况。

**底层逻辑**
- Skills 的核心是“上下文工程”：通过文件夹结构、脚本、配置选项，为 Claude 提供精确的指导和工具，使其行为更符合预期。
- 最佳实践源于持续迭代：从少量内容和 Gotcha 开始，随着使用不断补充优化。

**Takeaways**
- **分类清晰**：将 Skills 归入单一类型（如库参考、验证、自动化），避免模糊。
- **Gotchas 是精华**：专门记录常见失败点，持续更新。
- **渐进式披露**：利用文件夹拆分参考、脚本、示例，Claude 按需读取。
- **避免过度指令**：给 Claude 调整空间，而非死板流程。
- **存脚本而非描述**：提供可复用的脚本库，让 Claude 组合决策。

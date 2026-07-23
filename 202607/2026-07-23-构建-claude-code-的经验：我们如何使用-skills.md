# 构建 Claude Code 的经验：我们如何使用 Skills
- URL: https://transcrab.onev.cat/a/2026/07/lessons-from-building-claude-code-how-we-use-skills-2/
- Added: 2026-07-23 08:34:02
- Tags: #agent #skill

## TL;DR
文章分享了 Anthropic 使用 Claude Code Skills 的实践经验，包括 9 种技能类型、编写技巧（如 Gotchas、渐进式披露）、分发方式与衡量方法，强调 Skills 是包含可操作信息的目录。

## Summary
本文总结了 Anthropic 团队在使用 Claude Code Skills 过程中的经验。核心观点是 Skills 是目录而非仅文本文件，可包含脚本、资源，通过渐进式披露和 hooks 提升 agent 效率。文章分类了 9 种实用类型，并给出了编写、分发和衡量的最佳实践。

**底层逻辑**：Skills 的价值在于利用文件系统提供上下文，通过 Gotchas 区段积累失败点、按需 hooks 增强约束、记忆机制存储历史数据，并保留灵活性让 agent 自行调整。避免陈述显而易见的信息，Description 字段应描述触发时机而非摘要。

**Takeaways**：
- 9 种 Skills 类型：库与 API 参考、产品验证、数据获取与分析、业务流程与团队自动化、代码脚手架与模板、代码质量与审查、CI/CD 与部署、Runbook、基础设施运维。
- 编写技巧：聚焦非显而易见的坑；建立 Gotchas 区段；将详细内容拆分到子文件实现渐进式披露；避免过度约束；通过 `config.json` 和 `AskUserQuestion` 实现初始化配置；利用记忆存储（如日志、SQLite）；提供脚本和库让 agent 组合使用。
- 分发方式：签入仓库（`.claude/skills`）或通过 Plugin Marketplace；好 skill 自然涌现，经审核后移入 marketplace；可组合依赖其他 skills。
- 衡量：使用 `PreToolUse` hook 记录使用情况，识别受欢迎或触发不足的 skills。

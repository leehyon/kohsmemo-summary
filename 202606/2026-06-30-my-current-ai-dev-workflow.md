# My Current AI Dev Workflow
- URL: https://steipete.me/posts/2025/optimal-ai-development-workflow
- Added: 2026-06-30 07:00:26
- Tags: #workflow #agent

## TL;DR
作者推荐 Ghostty + Claude Code + 最小工具链，强调主动规划、上下文管理和测试，认为“少即是多”能最大化 AI 开发生产力。

## Summary
作者分享其当前 AI 开发工作流，核心是精简工具链，以 Ghostty 终端和 Claude Code 为主，辅以少量其他工具，认为“少即是多”。通过实际经验对比，作者发现最小化工具集、主动规划与上下文管理、以及用测试验证关键变更能显著提升效率。

**逻辑脉络**
- 从 VS Code 回到 Ghostty（终端稳定性更优），保留 VS Code 用于代码查阅，Cursor/GPT-5 用于评审。
- 尝试 Gemini 但编辑工具混乱，逐步弃用；GPT-5 用于计划审查效果更好。
- 放弃 worktree 设置，认为精心选择工作区域可避免交叉污染。
- 规划与上下文管理：通过 statusline + session ID 记录主题，使用 plan mode 迭代，大任务写文件让 GPT-5 审查。
- 测试策略：仅对较大变更写测试，要求模型在同一上下文中编写（模型能发现更多问题）。
- 移除最后一个 MCP（Playwright），因为有时会浪费上下文；偏好有 CLI 的服务（vercel, psql, gh, axiom），便于 agent 使用。

**底层逻辑**
- “少即是多”：最小化工具数量，减少上下文污染，避免不必要的后台代理，自己主动引导模型。
- 上下文是珍贵资源，不应浪费；模型在反复迭代中更有效。

**Takeaways**
- 选择 Ghostty 作为主终端，VS Code 和 Cursor/GPT-5 作为辅助。
- 主动规划：使用 plan mode 和外部文件，让 GPT-5 审查大任务。
- 上下文管理：session ID 标识，避免复现问题；不浪费上下文在无关工具上。
- 测试策略：关键变更在模型同一上下文中编写测试，模型能发现异常。
- 倾向 CLI 工具：一行配置即可让 agent 使用，减少手动操作。

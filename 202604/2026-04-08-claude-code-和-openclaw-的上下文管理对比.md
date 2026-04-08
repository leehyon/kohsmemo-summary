# Claude Code 和 OpenClaw 的上下文管理对比
- URL: https://finisky.github.io/openclaw-vs-claude-code-agent-arch/
- Added: 2026-04-08 01:14:43
- Tags: #agent #openclaw #design

## TL;DR
文章对比 Claude Code 与 OpenClaw 的上下文管理。Claude Code 利用 API 特性实现低成本压缩与状态恢复；OpenClaw 侧重通用兼容，当前成本高且缺乏深度优化。

## Summary
*   **核心主题**：Claude Code 与 OpenClaw 在长会话上下文管理上的工程策略差异。

*   **逻辑脉络**：从体验差异（Claude Code 表现更优）切入，通过源码分析指出核心差异不在于模型而在于 Agent 框架的上下文管理策略，具体展开压缩机制、会话笔记、恢复能力、子 Agent 设计及 Prompt Cache 管理五个维度的对比，最后归结为产品定位不同导致的架构选择差异。

*   **关键信息**：
    1.  **压缩策略与成本**：Claude Code 采用四层级联压缩（Time-Based Clearing、Cached Microcompact、Session Memory、Full Compact），前三层利用 Anthropic API 特性（如缓存编辑、后台笔记）实现零或低成本；OpenClaw 仅有一层 LLM 摘要，需多次调用模型，成本高昂。这使得 Claude Code 敢于更频繁地压缩，防止上下文膨胀。
    2.  **Session Memory 机制**：Claude Code 在后台持续维护结构化笔记，压缩时直接以此为摘要，无需额外调用 LLM；OpenClaw 仅在会话结束或重置时归档，无实时提取能力。免费摘要降低了 Claude Code 的维护开销。
    3.  **压缩后状态恢复**：Claude Code 压缩后主动恢复工作上下文（重新注入最近 5 个文件、配置、技能内容，清理缓存）；OpenClaw 仅进行消息配对修复以保格式正确，未恢复工作状态，导致模型可能重复读取文件。
    4.  **子 Agent 角色特化**：Claude Code 的子 Agent（如 Explore Agent）针对特定任务优化（只读、使用 Haiku 模型、仅返回摘要），有效隔离上下文污染；OpenClaw 采用通用子 Agent 框架，功能全面但缺乏针对具体场景（如搜索不污染主上下文）的特化优化。
    5.  **Prompt Cache 管理**：Claude Code 极度重视 Prompt Cache 命中率，设计决策以保持缓存前缀稳定为核心；OpenClaw 因需兼容多 Provider，无法深度绑定单一缓存机制，导致有效成本较高。
    6.  **架构与实现差距**：OpenClaw 虽定义了完善的 Context Engine 接口，但当前实现（LegacyContextEngine）多为空壳或委托旧路径，未发挥架构潜力。
    7.  **根源差异**：Claude Code 定位于“单开发者对单代码库”，可进行深度 API 绑定优化；OpenClaw 面向多渠道、多模型的通用场景，侧重通用性与兼容性。OpenClaw 的架构已预留优化空间，需填充类似 Claude Code 的分层压缩与实时笔记实现以提升体验。

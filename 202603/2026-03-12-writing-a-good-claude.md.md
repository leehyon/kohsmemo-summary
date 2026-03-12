# Writing a good CLAUDE.md
- URL: https://www.humanlayer.dev/blog/writing-a-good-claude-md
- Added: 2026-03-12 09:38:37
- Tags: #agent

## TL;DR
编写有效的 `CLAUDE.md` 文件，应简洁明确，涵盖项目目的、技术栈和工作方式，避免冗余指令，保持文件简短，并使用渐进式披露策略优化与 Claude AI 的交互体验。

## Summary
核心主题：如何编写有效的 `CLAUDE.md` 文件，以优化与 Claude AI 编程助手的交互体验

关键信息与逻辑脉络：

1.  LLM 的无状态特性
   - LLM 是无状态函数，不会随时间学习
   - 每次会话开始时，Claude 对代码库一无所知
   - `CLAUDE.md` 是默认包含在每次会话中的唯一文件

2.  `CLAUDE.md` 的核心作用
   - 作为将 Claude 引入代码库的入门指南
   - 应涵盖项目的 WHY（目的）、WHAT（技术栈和结构）、HOW（工作方式）

3.  Claude 忽略 `CLAUDE.md` 的问题
   - Claude 会根据任务相关性决定是否遵循 `CLAUDE.md` 中的指令
   - 文件中非普遍适用的内容越多，被忽略的可能性越大

4.  创建优质 `CLAUDE.md` 的建议
   - 少指令原则：包含尽可能少的指令，理想情况下仅包含普遍适用的内容
   - 文件长度：建议少于 300 行，最好在 60 行以内
   - 渐进式披露：将任务特定指令保存在单独的 markdown 文件中，通过引用方式提供
   - 避免将 LLM 用作代码检查器：使用传统 linter 和格式化工具
   - 不要自动生成 `CLAUDE.md`：这是工具中杠杆最高的点，需要精心设计

5.  最佳实践总结
   - 明确定义项目的 WHY、WHAT 和 HOW
   - 保持内容简洁且普遍适用
   - 使用渐进式披露策略
   - 利用专用工具处理代码风格
   - 手动精心设计 `CLAUDE.md` 内容

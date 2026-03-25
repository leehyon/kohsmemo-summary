# Claude Code 的三种 Skill 类型以及一些常见陷阱
- URL: https://www.ccgxk.com/codeother/689.html
- Added: 2026-03-25 05:06:31
- Tags: #best-practice #agent

## TL;DR
本文探讨 Claude Code 的 Agentic Engineering，详解三种 Skill 类型以优化 AI 协作，揭示反模式与子 Agent 管理陷阱，并汇总高频命令提升开发效率。

## Summary
**核心主题**
深入探讨 Claude Code 的高级使用技巧，重点阐述 Agentic Engineering 理念、三种 Skill 类型定义、常见反模式以及高频实用命令。

**逻辑脉络**
1. **理念引入**：从 AI 技术成熟背景出发，提出 Agentic Engineering 模式，即善用 子 agent 分工协作，实现「设定目标，AI 自行干活」的高效策略。
2. **核心机制**：详细解析三种 Skill 类型，分别用于保证确定性、降低操作风险和抑制 AI 幻觉。
3. **避坑指南**：列举 Skill 设计和 子 agent 使用中的反模式与陷阱，强调权限隔离与结构化输出。
4. **效率提升**：整理高频斜杠命令与工程集成技巧，辅助日常开发与调试。

**关键信息**
*   **Agentic Engineering**：利用 子 agent 处理隔离、扫代码库、跑测试等任务，避免占用主进程上下文，通过分工流水线提升效率。
*   **三种 Skill 类型**：
    1.  **检查清单型**：用于发布前验证。通过列表确保编译、测试等步骤无低级错误，作为 CI/CD 的最后一道人工屏障，保证确定性。
    2.  **工作流型**：类似 SOP 标准作业程序。精髓在于设置 `disable-model-invocation: true`，剥夺 AI 「即兴发挥」权，将高危操作风险降至传统运维脚本水平。
    3.  **领域专家型**：用于处理特定领域疑难杂症（如运行时崩溃）。通过定义证据采集步骤和决策矩阵，强制 AI 按固定路径推理，抑制幻觉猜测。
*   **反模式与陷阱**：
    *   **Skill 设计**：描述应短而精，避免过度匹配；勿将大型运维手册塞入 Skill 以免上下文污染；涉及危险或副作用的 Skill 必须禁止自动调用；遵循单一职责原则，避免一个 Skill 承担多重角色导致 AI 混乱。
    *   **子 Agent 管理**：严格遵循最小特权原则，利用 `tools` / `disallowedTools` 进行权限隔离；强制子代理使用 `json_schema` 或固定 Markdown Table 输出，防止输出格式随机化。
*   **高频斜杠命令**：
    *   **上下文管理**：`/context` (查看 Token 结构), `/clear` (清空会话), `/compact` (压缩上下文)。
    *   **工程集成**：`claude --continue` (恢复最近会话), `--fork` (分叉测试不同解法), `--worktree` (隔离 Git 环境), `-p` (非交互模式), `--output-format json` (结构化输出)。
    *   **高级调试**：`/simplify` (代码质量审查), `/rewind` (回退 Checkpoint), `/insight` (会话复盘), `/btw` (任务中断时插话提问)。

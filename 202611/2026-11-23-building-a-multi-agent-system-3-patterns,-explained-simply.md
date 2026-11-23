# Building a Multi-Agent System: 3 Patterns, Explained Simply
- URL: https://kadhar.dev/blog/multi-agent-systems-from-scratch
- Added: 2026-11-23 01:55:34

## TL;DR
先单 agent；只在需不同工具/指令、可并行或需独立测试时拆成 Pipeline、Orchestrator 或 Blackboard，并优先做交接校验、预算与日志等护栏。

## Summary
文章的核心不是鼓励上多 agent，而是先问是否真的需要拆分：多数任务一个带工具的 agent 就够，拆分只在指令/工具差异大、可并行、需独立测试时划算。作者用晚餐推荐例子讲清 3 种常见模式，并用 Stormwise 的 117 个案例说明真正拖垮系统的是数据、预算与校验，而非 prompt。

**底层逻辑**
- 多 agent 是用更多调用、成本与失败面换取结构，默认应先单 agent。
- 只有当每部分能明确归属、能独立验证或被并行处理时才拆。

**3 种模式**
- **Pipeline**：固定顺序交接，易测试但僵化，步骤回退会变复杂。
- **Orchestrator**：主 agent 规划并汇总，适合需求细节不定的任务，但主 agent 规划错会放大。
- **Blackboard**：共享工作区、无老板，适合无法预知步骤的调试，但最难测试、易循环。

**失败教训**
- 坏数据会被下一 agent 当事实，需在每次交接用代码校验。
- 正确数据比巧妙 prompt 更有效；预算在 hardest cases 失效；自动检查器也可能错。
- 回传会带来循环与成本，额外 agent 必然增加调用。

**Takeaways**
- 先单 agent，明确瓶颈再拆。
- 按任务确定性选模式：固定流程用 Pipeline，动态规划用 Orchestrator，开放探索用 Blackboard。
- 第一天加护栏：交接校验、跳数上限、按请求预算、全量消息日志、真实案例测试。
- 把精力放在无聊的工程约束上，而非堆 agent。

# A harness for every task: dynamic workflows in Claude Code
- URL: https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
- Added: 2026-06-03 01:48:06
- Tags: #agent #engineering

## TL;DR
Claude Code 动态工作流由 Opus 驱动，为任务即时编写定制 harness，使用子代理和多种模式（如分类、扇出、对抗验证）解决长任务故障，适用于迁移、研究、验证等复杂场景。

## Summary
Claude Code 的动态工作流（dynamic workflows）允许 Claude 在运行时为每个任务即时编写自定义 harness，克服默认 coding harness 在长任务、大规模并行、高度结构化或对抗性任务中的故障模式（如代理惰性、自我偏好偏差、目标漂移）。

工作原理：执行含特殊函数的 JavaScript 文件，用以生成和协调子代理（subagents），支持指定模型、工作树隔离、中断恢复。

与静态工作流对比：静态工作流为覆盖所有边界情况通常更通用；动态工作流由 Claude Opus 4.8 驱动，可为具体用例定制专属 harness。

常见模式：
- 分类与执行（Classify-and-act）：先分类再路由到不同代理。
- 扇出与综合（Fan-out-and-synthesize）：分解任务为多步，每步独立执行后合并结果。
- 对抗性验证（Adversarial verification）：对每个输出另启代理进行对抗性校验。
- 生成与过滤（Generate-and-filter）：生成想法后按规则筛选。
- 锦标赛（Tournament）：多代理竞争同一任务，两两比较选出最优。
- 循环直到完成（Loop until done）：持续生成代理直至满足停止条件。

典型用例：
- 迁移与重构（如 Bun 从 Zig 重写为 Rust）：分解任务，工作树内独立修复并交叉审查。
- 深度研究（如 `/deep-research` 技能）：扇出搜索、抓取、对抗性验证、综合报告。
- 深度验证：提取事实声明，每个声明由独立子代理核实。
- 排序（如按严重性排序工单）：锦标赛或并行桶排序后合并。
- 规则记忆与遵守：为每条规则设验证代理，反向也可从历史修正中挖掘规则。
- 根因调查：从不同证据源（日志、文件、数据）生成独立假设并分别验证。
- 规模分类（如支持队列）：分类、去重、操作或升级，可配合 /loop 持续运行。
- 探索与品味（如设计、命名）：生成多种方案后由评审代理按规则筛选或锦标赛排序。
- 评估（Evals）：工作树内独立运行后对比打分。
- 模型与智能路由：分类代理先评估任务复杂度再路由到 Sonnet 或 Opus。

何时不使用：常规编码任务未必需要，动态工作流会消耗更多 tokens，不应过度使用。

使用技巧：
- 提示词需详细，可指定“快速工作流”。
- 可重复任务配合 `/goal` 和 `/loop` 使用。
- 可设置 token 预算（如“use 10k tokens”）。
- 工作流可通过按“s”保存，存入 `~/.claude/workflows` 或通过 skill 分发；skill 中可将工作流文件视为模板而非固定脚本。

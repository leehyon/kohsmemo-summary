# Build agents, not pipelines
- URL: https://www.seangoedecke.com/build-agents-not-pipelines/
- Added: 2026-06-03 05:21:35
- Tags: #agent #llm

## TL;DR
在 LLM 应用中，应优先使用 agent 而非 pipeline，因为 agent 更灵活智能，适合复杂任务；pipeline 虽可预测但有局限。建议混合使用：pipeline 筛选，agent 深入分析。有疑问时用 agent。

## Summary
核心主题： 在 LLM 应用中，应优先使用 agent（代理）而非 pipeline（管道），尽管各有优劣，但 agent 在复杂任务上更灵活、智能且未来兼容性强。

关键信息与逻辑脉络：

- **定义与类比**： pipeline 将程序控制流写在代码中； agent 赋予 LLM 工具并让其自主管理控制流。 类似于库与框架的关系。

- **简单任务无区别**： 对于上下文极少、步骤固定的任务， pipeline 与 agent 执行效果相同。

- **可预测性 vs 灵活性**： pipeline 更可预测（成本、延迟稳定）， agent 更灵活但成本/延迟不可控。 agent 能处理更困难的任务（如编程），因为可以自主循环和收集信息。

- **上下文收集**： pipeline 需一次性提供所有上下文（难点），常依赖 RAG 但效果不佳； agent 可自主搜索获取上下文，更简单有效。 上下文收集本身的难度常与解决问题相当。

- **多模型管道**： pipeline 可用不同模型针对不同任务； agent 通常需使用统一模型。 但该优势可能被夸大，因为信号常隐藏在原始数据中。

- **小上下文与本地模型**： pipeline 适合小上下文（如本地模型，内存受限）； agent 需要大上下文，不适合本地模型。 agent 更“未来-proof”（面向未来），因为模型持续进步， agent 受益更大。

- **安全与可读性**： 两者都有提示注入风险，均需事后检查。 pipeline 略更可读（更易追踪），但 agent 并非更不安全。

- **实践应用案例（NSA 邮件监控）**： 建议混合使用 —— 用低成本的 pipeline 对大量邮件做初步筛选（可扩展、可预测）；再用 agent 对可疑项进行深入分析（灵活性高、智能强）。

- **总结指南**：
    - 使用 pipeline： 当对上下文大小有严格限制、需要准确预测/限制成本、必须使用本地模型时。
    - 使用 agent： 当无法一次性收集所有相关上下文、任务难度高以至于 pipeline 可能无法解决时。
    - 总体原则： 有疑问时用 agent。 现有项目多从 pipeline 迁移至 agent，鲜有反向迁移。 先构建 agent 再考虑优化为更便宜的 pipeline 是更稳妥的设计路线。

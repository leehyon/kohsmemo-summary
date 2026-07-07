# From “Reasoning” Thinking to “Agentic” Thinking
- URL: https://arthurchiao.art/blog/from-reasoning-thinking-to-agentic-thinking-zh/
- Added: 2026-07-07 05:42:00
- Tags: #agent #design

## TL;DR
大模型训练正从"推理式思考"转向"智能体式思考"，核心是模型在真实环境中通过行动与反馈持续优化，Harness Engineering 成为关键竞争力。

## Summary
本文探讨了 AI 大模型训练从"推理式思考"到"智能体式思考"的转变，强调未来的思考应服务于行动，在与环境的闭环交互中持续优化，而非孤立的推理轨迹。

**逻辑脉络**
- 推理式思考（OpenAI o1、DeepSeek-R1）将 thinking 作为可训练的一等能力，依赖数学等可验证领域提供强反馈信号。
- 混合 thinking 的尝试（Qwen3 等）面临数据分布与用户行为冲突，最终多数厂商转向独立模型或融合但强调预算控制。
- 智能体式思考的核心是模型在环境中通过行动推理，关注工具使用、计划修正等，强化学习基础设施要求更高（训练/推理解耦，环境成为一等对象）。
- 未来前沿是 harness engineering，从训练模型转向训练 Agent+Harness 系统。

**底层逻辑**
- 强化学习可扩展的前提是确定、稳定且可扩展的反馈信号；在 agent 时代，环境质量、rollout 基础设施和反 reward hacking 成为核心竞争力。

**Takeaways**
- 推理式思考转向智能体式思考：从"想得更久"到"更有效行动"。
- 混合 thinking 模型难以兼顾简洁与深度，数据分布差异是根本原因。
- Agentic RL 需要训练与推理彻底解耦，环境本身成为核心研究对象。
- 新瓶颈：reward hacking、环境设计、评估器鲁棒性。
- 未来优势来自 better environments and harness engineering 而非单纯 RL 算法。

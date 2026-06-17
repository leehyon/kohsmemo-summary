# Building Reliable Agentic AI Systems
- URL: https://martinfowler.com/articles/reliable-llm-bayer.html
- Added: 2026-06-17 05:36:27
- Tags: #agent

## TL;DR
Bayer 的 PRINCE 系统利用 Agentic RAG 与多智能体编排，将临床前数据检索从手动搜索转变为智能问答与任务执行，通过上下文工程与反思机制实现高可靠性。

## Summary
Bayer 开发了 PRINCE，一个基于 Agentic RAG 的多智能体 AI 系统，用于临床前药物发现中的非结构化与结构化数据检索。该系统从搜索、问答演进到主动执行复杂任务，通过 LangGraph 编排 Researcher、Writer 和 Reflection 智能体，并融入上下文工程与封装工程原则。

**逻辑脉络**
- 临床前研究面临数据孤岛、搜索能力有限、手动分析耗时等挑战。
- PRINCE 分三阶段演进：Search（统一入口）、Ask（RAG 问答）、Do（多智能体编排）。
- 技术架构：LangGraph 编排工作流，Researcher 智能体负责 RAG 与 Text-to-SQL 混合检索，Reflection 智能体验证数据充分性，Writer 生成最终回答。
- 关键工程决策：上下文工程（各阶段获取不同上下文）与封装工程（重试、回退、状态持久化、可观测性）。
- 反思机制：过程反思（Think & Plan 步骤评估工作流进度）与数据反思（Reflection 智能体评估数据是否足够）。

**底层逻辑**
- 核心假设：LLM 作为推理引擎，需要精心设计的上下文边界和健壮的脚手架才能可靠执行多步骤任务。
- 方法论：将复杂查询分解为意图澄清、规划、研究、验证、写作等步骤，每个步骤使用专用提示和工具，并通过反思循环保证质量。

**Takeaways**
- 混合检索策略（语义搜索 + 关键词搜索 + 元数据过滤 + 重排序）显著提升 RAG 准确性。
- 过程反思与数据反思分离，避免工作流正确但信息不足的情况。
- 使用领域子智能体避免工具冲突，保持职责清晰。
- 上下文工程要求每个智能体只接收当前步骤所需信息，减少污染。
- 通过重试、模型回退、错误上下文传递等机制增强系统鲁棒性。

# Markdown in /src
- URL: https://htmx.org/essays/markdown-in-src/
- Added: 2026-10-09 01:21:10

## TL;DR
Markdown 正在成为源代码：应把描述代码意图的 Markdown 签入 /src 的 md 目录，代码与测试由它派生，取代临时 prompt，让人类与 agent 就近获取上下文。

## Summary
Carson Gross 认为，在 agentic coding 普及的今天，Markdown 已经成为源代码而非文档：LLM 生成代码所依赖的 prompt 是临时的，导致代码本身成了唯一的事实来源。他主张依照 locality（就近原则），把记录代码意图的 Markdown 放进 /src，与它产出的代码放在一起。

**逻辑脉络**
- 咨询中观察到企业正快速转向 agentic coding，功能常由一串 prompt 生成，生成的代码反而成了 ground truth。
- 反驳“LLM 即编译器”的类比：编译器保留源码，而 LLM 工作流通常不保留，所以需要主动捕获并入库。
- Markdown 已具备源码属性：纯文本、可 diff / grep / PR 评审，人与 LLM 都能原生读写，且已出现在 AGENTS.md、specs、plan、TASK.md 中。
- 提议新增 /src/md，其内容比传统设计文档更低层，记录架构、源码级与数据设计决策，接近规格说明。
- 测试不适合充当人机交互的规格：仪式重、层次低、难容纳 Mermaid 图。分工应为 Markdown 是规格，测试基于它提供自动验证。
- 结论：代码变便宜后，真正有价值的是意图——做什么、为何做、不能做什么。

**底层逻辑**
- 第一性原理是 locality：模块应自带解释其意图的 Markdown，消除 wiki / Notion / Jira 中的“远程规格”。
- 存在 Complexity Budget：这类 Markdown 需被精心管理，保持干净、良好分解与合适抽象层级。
- /src/md 应主要由人撰写与策展，agent 不宜大量生成其内容；同步 Markdown 与派生代码将成为重要技能。

**Takeaways**
- Markdown 正在成为源代码，应像源码一样被签入与评审。
- 放在 /src/md，与生成的代码同目录，人与 agent 都能就近取用上下文。
- 代码与测试应由 Markdown 派生，而非由临时 prompt 会话产生。
- 高层流程文档仍可留在 Linear / wiki；系统核心行为写入源码目录的 Markdown。
- 示例结构：src/md/ 下含 README.md、TODO.md、OVERVIEW.md，以及可选的 features/、data/、api/、infrastructure/。
- 该结构仍是初步设想，作者期待在实践中继续调整。

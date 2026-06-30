# How I program with LLMs
- URL: https://crawshaw.io/blog/programming-with-llms
- Added: 2026-06-30 07:02:07
- Tags: #llm

## TL;DR
作者分享使用 LLM 编程的经验，强调 chat-driven programming 需以 exam-style 提问，利用廉价重做和更小包结构提升效果，并介绍了 sketch.dev 工具。

## Summary
本文介绍了作者过去一年使用 LLM 编程的个人经验，核心观点是 LLM 能在合理引导下显著提升生产力。作者通过 autocomplete、search 和 chat-driven programming 三种方式使用 LLM，其中 chat 模式价值最高但最需技巧。关键在于将任务设计成“考试式问题”：提供明确目标和完整背景，且结果易于验证。LLM 重做成本极低，应利用这一点快速迭代。代码结构需调整：更小的包有助于隔离上下文，使 LLM 能更好地处理 exam-style 任务。作者通过一个四分位数采样器示例展示了如何利用 LLM 生成代码并自动修复错误。未来趋势是更多专用代码和更具可读性的测试，减少不必要的抽象。最后介绍了 sketch.dev——一个为 Go 和 LLM 交互优化的在线环境。

**逻辑脉络**
- 作者从自身经验出发，描述了三种 LLM 使用方式，并特别聚焦于 chat-driven programming。
- 解释了为何使用 chat：当知道要写什么但缺乏精力时，LLM 提供初稿，修改错误比从零开始容易。
- 提出 chat 成功的两大要素：1) 避免复杂模糊，2) 要求可验证的工作。LLM 更适合 exam-style 问题。
- 通过 quartile sampler 示例展示具体流程：生成代码、发现错误、利用编译器反馈修复、改进测试（包括 fuzz test）。
- 最后展望：LLM 使代码更模块化、测试更充分，作者正构建 sketch.dev 以自动利用这些观察。

**底层逻辑**
- LLM 是强大的助手，但需要人精心设计交互方式。
- 核心假设：LLM 擅长在限定上下文内生成合理代码，且重做成本极低；人应专注于验证和迭代。
- 代码设计 tradeoff 随 LLM 改变：更小、更专注的包有利于 LLM 理解，也利于人类阅读。

**Takeaways**
- 三种使用 LLM 的方式：autocomplete、search、chat，其中 chat 最需技巧但回报最高。
- 将 chat 任务设计为 exam-style：明确目标、提供全部背景、要求易验证的输出。
- 利用 LLM 重做低成本的优势：持续通过编译器/测试反馈迭代，无需手动修复所有错误。
- 采用更小的包结构：每个包只包含一个算法或组件，方便 LLM 理解和测试。
- 未来方向：更专用代码、更少抽象、更全面的测试（如 fuzz test），以及为 LLM 定制的 IDE（如 sketch.dev）。

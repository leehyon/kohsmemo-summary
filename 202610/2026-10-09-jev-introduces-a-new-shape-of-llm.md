# Jev introduces a new shape of LLM
- URL: https://simonwillison.net/2026/Sep/21/jev/
- Added: 2026-10-09 01:20:15

## TL;DR
TypeSafe AI 发布 Jev，一种输出浮点决策而非文本的 System One 模型。它极快极便宜，适合分类、评分与排序，但黑箱和偏见风险高，需重视 evals。

## Summary
文章介绍 TypeSafe AI 发布的 Jev，一种被称为 System One 或 decision models 的新型 LLM：输入仍是文本，输出不是文本，而是类别、是/否、评分及其置信度的浮点数。它更快、更便宜，只按输入计费，输出免费，首个模型输入价为每百万 token 0.042 美元，低于 GPT-5 Nano 的 0.05 美元。

**逻辑脉络**
- Jev 支持三类问题：Noul（Bernoulli）是/否问题，返回 0 到 1 置信度；choice 从选项中选择并给概率分布；score 在数值等级上返回分数。
- 一个 state 可配多个问题，并行评估，适合分类任务：垃圾邮件检测、标签建议、优先级与排序；也可用于 BM25 召回后的搜索重排。
- 作者担忧其黑箱性更强：只返回浮点数，无法解释依据，偏见风险更需关注，因此 evals 与结构化实验更重要。
- 社区已出现 jevchat、jev-leftpad、jev-2048、开源复刻 Kev 与 JevBench；作者发布 llm-typesafe 插件。

**底层逻辑**
- 把 LLM 当成“frontier-intelligence function call”：非结构化状态输入，类型化概率决策输出。
- 以极低成本换取高频、并行、可评分的决策能力，而非生成文本。
- 适用边界是分类/评分/排序；当前对数字、日期和对抗性内容较弱。

**Takeaways**
- Jev 是 decision model：文本进，浮点决策出，快且极便宜。
- 三类查询覆盖是/否、选择、评分，可并行批量提问。
- 最适合分类、标签、排序、重排，不适合需要解释或生成文本的任务。
- 黑箱与偏见是核心风险，必须靠 evals 和实验验证。
- 生态活跃：已有多种玩具应用、开源复刻和 LLM 插件。

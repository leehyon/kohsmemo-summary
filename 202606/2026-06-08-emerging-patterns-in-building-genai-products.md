# Emerging Patterns in Building GenAI Products
- URL: https://martinfowler.com/articles/gen-ai-patterns/
- Added: 2026-06-08 02:44:21
- Tags: #agent #design

## TL;DR
文章总结构建 GenAI 产品的常见模式与挑战：从基础模式（Direct Prompting、Evals、Embeddings）到知识扩展（Fine Tuning、RAG），再到 RAG 增强（混合检索、查询重写、重排序、护栏），强调模式是经验总结而非标准答案。

## Summary
生成式 AI 产品从概念验证到生产落地面临挑战，源于人们常将其视为传统系统的延伸。文章总结了应对幻觉、非确定性等问题的若干模式，按逻辑脉络分层呈现。

- **核心主题**：构建 GenAI 产品的常见模式及其适用场景，强调模式是经验总结而非标准答案。

- **基础模式**
  - **Direct Prompting**：直接向基础 LLM 发送提示。简单但受限：训练数据时效性、缺乏特定领域知识、易受恶意提示影响、可能产生幻觉。
  - **Evals**：评估 LLM 响应质量。通过评分（自动或人工）衡量相关性、事实性等指标，需在构建流水线及生产环境中持续监控。
  - **Embeddings**：将数据（文本/图像）转换为数值向量，相似内容在向量空间距离近。用于语义相似度比较，比关键词匹配更深刻。

- **知识扩展模式**
  - **Fine Tuning**：对预训练模型进行额外训练以适配特定领域。虽有效但成本高昂，通常非首选。
  - **Retrieval Augmented Generation (RAG)**：检索相关文档片段并加入提示中，使 LLM 在回答前参考增强上下文。能处理不断变化的数据，提高事实性并提供引用。

- **RAG 的增强模式**（解决 RAG 实践中遇到的限制）
  - **Hybrid Retriever**：结合向量搜索与关键词搜索（如 BM25），提高检索覆盖面，但可能返回过多结果，需配合 Reranker。
  - **Query Rewriting**：由 LLM 将用户模糊查询改写为多个变体，提升检索准确性。
  - **Reranker**：对检索到的文档片段重新排序，优先送入 LLM 最有用的内容，克服长上下文中的 “中间丢失” 问题。
  - **Guardrails**：使用独立的 LLM 调用过滤危险输入或净化输出，防止 LLM 泄露信息或生成不当内容。

- **逻辑脉络总结**：从直接提示开始，发现不足后引入评估（Evals）和嵌入（Embeddings）；再通过 RAG 扩展知识；针对 RAG 的检索效率、查询模糊、上下文膨胀和安全性问题，分别采用混合检索、查询重写、重排序和护栏模式来增强系统。

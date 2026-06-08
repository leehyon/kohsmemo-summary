# The big ideas behind retrieval augmented generation
- URL: https://www.elastic.co/blog/retrieval-augmented-generation-explained
- Added: 2026-06-08 02:54:12
- Tags: #rag #llm

## TL;DR
检索增强生成（RAG）引入外部私有数据，使大语言模型回答更准确且避免幻觉。相比昂贵训练和微调，RAG通过语义搜索和分块策略低成本实现，架构包含系统提示、上下文和用户输入。

## Summary
核心主题 ：检索增强生成 （RAG） 通过引入外部私有数据来增强大语言模型 （LLM），使其回答更准确、可定制且避免幻觉。

关键信息与逻辑脉络 ：

- LLM 的局限性 ：依赖通用公开数据，可能过时、缺失私有内容，且易产生幻觉。
- 解决方案对比 ：从头训练 （如 BloombergGPT） 成本极高，微调 （如 Med-PaLM） 需许可且昂贵，RAG （如 Elastic Support Assistant） 通过提示工程低成本引入外部内容，效果显著。
- 语义搜索基础 ：使用向量嵌入将概念映射到多维空间，通过最近邻搜索找到语义相似内容，突破关键字匹配的限制。
- 分块策略 ：为平衡语义精度与完整性，将文档切分为合适大小的块，常见方法包括基于 Token 切分、Token 重叠以及检索周围块。
- RAG 架构 ：由系统提示（定义行为）、提供上下文（检索到的相关块）、用户输入三部分组成；Elasticsearch 提供 AI Playground 便于快速开发和测试。

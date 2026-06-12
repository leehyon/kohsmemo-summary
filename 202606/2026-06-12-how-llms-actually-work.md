# How LLMs Actually Work
- URL: https://0xkato.xyz/how-llms-actually-work/
- Added: 2026-06-12 03:24:27
- Tags: #llm #guide #math

## TL;DR
本文从分词到下一个 token 预测，逐层拆解 transformer 架构的核心组件，并解释 RoPE、GQA、MoE 等现代改进，帮助理解 LLM 工作原理。

## Summary
本文详细解析现代 LLM 的核心机制，从分词到下一个 token 预测，逐步拆解 transformer 架构的每个组件，并指出不同模型之间的差异主要来自训练数据、配置和后期训练，而非架构本身。

**逻辑脉络**
- 文章按 pipeline 顺序展开：分词将文本转为 token ID → 嵌入层赋予语义 → 位置编码（RoPE）注入位置信息 → 注意力（QKV、因果掩码、归纳头）实现 token 间信息交换 → 多头注意力并行捕捉多种关系 → 前馈网络（FFN）独立处理每个 token 并存储大量知识 → 残差流和层归一化（RMSNorm）确保深度可训练 → 最后通过 softmax 预测下一个 token。
- 还介绍了工程改进：GQA 减少 KV cache 内存，MoE 扩大参数而不等比增加计算，推测解码加速生成。

**底层逻辑**
- 作者的第一性原理：几乎所有现代 LLM 共享 transformer 骨架，理解注意力、FFN、残差流等核心机制即可把握模型行为。模型间的差异主要在权重、层数、头数、MoE 与否及后期训练，而非基本架构。

**Takeaways**
- LLM 的训练目标是 next-token prediction，而非直接追求事实准确性。
- 位置编码从绝对位置演进到相对位置（RoPE），更好支持长上下文和泛化。
- 注意力复杂度 O(n²)，KV cache 和 GQA 是工程关键优化。
- FFN 承担大部分参数和知识存储，可通过 ROME 等方法直接编辑事实。
- 残差流和预归一化（RMSNorm）是训练深层 transformer 的命门，已成为主流。

# 2026-10 Monthly Index

(2026-10-09) [C's Flexible Integer Sizes were Not a Design Mistake](2026-10-09-c%27s-flexible-integer-sizes-were-not-a-design-mistake.md)
- int 从来不是 32 位的同义词。C 的整数宽度可变，是为了在 12 到 64 位字长、多种字符宽度与负数表示的机器上实现可移植与高效；强制固定尺寸会拖慢或无法实现。stdint.h 的精确宽度类型 C99 才出现且可选。

(2026-10-09) [What To Know in JavaScript (2026 Edition)](2026-10-09-what-to-know-in-javascript-%282026-edition%29.md)
- 文章盘点 2026 年 JavaScript 生态，包括 ES2025/ES2026 语言特性、框架与运行时、Vite 与 TypeScript 工具链、AI 写码及 npm 供应链安全，建议回归基础。

(2026-10-09) [Markdown in /src](2026-10-09-markdown-in-src.md)
- Markdown 正在成为源代码：应把描述代码意图的 Markdown 签入 /src 的 md 目录，代码与测试由它派生，取代临时 prompt，让人类与 agent 就近获取上下文。

(2026-10-09) [Jev introduces a new shape of LLM](2026-10-09-jev-introduces-a-new-shape-of-llm.md)
- TypeSafe AI 发布 Jev，一种输出浮点决策而非文本的 System One 模型。它极快极便宜，适合分类、评分与排序，但黑箱和偏见风险高，需重视 evals。

(2026-10-08) [Shipping is the foundation](2026-10-08-shipping-is-the-foundation.md)
- 能 ship 是优秀工程师的地基。若不能快速独立交付，协作、设计、估算与领导都会失真。AI 无法替代 ship 所需的上下文、判断与收尾。

(2026-10-08) [How to read code](2026-10-08-how-to-read-code.md)
- 读代码不应线性通读。应多轮、非线性扫描：先追关键路径与调用链，把其余当黑盒，最后端到端读 diff 抓异常。AI 生成代码仍须亲自读，因其常有对齐偏差，不能完全交给 LLM 审阅。

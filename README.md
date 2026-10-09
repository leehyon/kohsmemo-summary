# Bookmark Summary 
自动读取 [kohsmemo](https://github.com/leehyon/kohsmemo) 仓库中的书签数据，通过 Jina Reader 获取网页文本内容，再借助大模型生成内容总结。

## Latest 10 Entries

(2026-10-09) [C's Flexible Integer Sizes were Not a Design Mistake](202610/2026-10-09-c%27s-flexible-integer-sizes-were-not-a-design-mistake.md)
- int 从来不是 32 位的同义词。C 的整数宽度可变，是为了在 12 到 64 位字长、多种字符宽度与负数表示的机器上实现可移植与高效；强制固定尺寸会拖慢或无法实现。stdint.h 的精确宽度类型 C99 才出现且可选。

(2026-10-09) [What To Know in JavaScript (2026 Edition)](202610/2026-10-09-what-to-know-in-javascript-%282026-edition%29.md)
- 文章盘点 2026 年 JavaScript 生态，包括 ES2025/ES2026 语言特性、框架与运行时、Vite 与 TypeScript 工具链、AI 写码及 npm 供应链安全，建议回归基础。

(2026-10-09) [Markdown in /src](202610/2026-10-09-markdown-in-src.md)
- Markdown 正在成为源代码：应把描述代码意图的 Markdown 签入 /src 的 md 目录，代码与测试由它派生，取代临时 prompt，让人类与 agent 就近获取上下文。

(2026-10-09) [Jev introduces a new shape of LLM](202610/2026-10-09-jev-introduces-a-new-shape-of-llm.md)
- TypeSafe AI 发布 Jev，一种输出浮点决策而非文本的 System One 模型。它极快极便宜，适合分类、评分与排序，但黑箱和偏见风险高，需重视 evals。

(2026-10-08) [Shipping is the foundation](202610/2026-10-08-shipping-is-the-foundation.md)
- 能 ship 是优秀工程师的地基。若不能快速独立交付，协作、设计、估算与领导都会失真。AI 无法替代 ship 所需的上下文、判断与收尾。

(2026-10-08) [How to read code](202610/2026-10-08-how-to-read-code.md)
- 读代码不应线性通读。应多轮、非线性扫描：先追关键路径与调用链，把其余当黑盒，最后端到端读 diff 抓异常。AI 生成代码仍须亲自读，因其常有对齐偏差，不能完全交给 LLM 审阅。

(2026-09-23) [Attention is all you have](202609/2026-09-23-attention-is-all-you-have.md)
- 文章用俄罗斯方块效应说明：注意力会被长期关注塑造。推荐算法劫持注意力，把大脑钥匙交给平台；我们应回到博客、RSS 等主动、较慢的有意图互联网。
- Tags: #life #view

(2026-09-14) [How to fix your entire life in 1 day](202609/2026-09-14-how-to-fix-your-entire-life-in-1-day.md)
- 真正改变不是靠自律，而是改身份与隐性目标。用一天做心理挖掘、打断自动驾驶、综合愿景与反愿景，再把人生游戏化。
- Tags: #life

(2026-09-11) [3 constraints before I build anything](202609/2026-09-11-3-constraints-before-i-build-anything.md)
- 构建前先过 3 条约束：一页纸写清北极星，否则不做；核心技术与产品可分离，以积累可复利 IP；选一个定义性约束塑造产品身份。任一不满足就不构建。
- Tags: #product

(2026-09-11) [Building a backyard office, the build and cost breakdown](202609/2026-09-11-building-a-backyard-office%2C-the-build-and-cost-breakdown.md)
- 作者为波特兰小屋的远程办公需求，用 Tuff Shed 棚屋改造后院办公室，总花费 $19,478；关键决策是混凝土基础、大窗、60A 电气、硬线 Ethernet 和 Daikin 迷你分体空调，多询价并外包部分施工省下近半全包费用。
- Tags: #life

## Monthly Archive

- [2026-10](202610/monthly-index.md) (6 entries)
- [2026-09](202609/monthly-index.md) (10 entries)
- [2026-08](202608/monthly-index.md) (31 entries)
- [2026-07](202607/monthly-index.md) (53 entries)
- [2026-06](202606/monthly-index.md) (68 entries)
- [2026-05](202605/monthly-index.md) (26 entries)
- [2026-04](202604/monthly-index.md) (44 entries)
- [2026-03](202603/monthly-index.md) (82 entries)

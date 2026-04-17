# Bookmark Summary 
自动读取 [kohsmemo](https://github.com/leehyon/kohsmemo) 仓库中的书签数据，通过 Jina Reader 获取网页文本内容，再借助大模型生成内容总结。

## Latest 10 Entries

(2026-04-17) [Do You Even Need a Database](202604/2026-04-17-do-you-even-need-a-database.md)
- 文章探讨了早期使用文件系统替代数据库的可行性。测试显示，内存映射等简单方案性能优异，SQLite 也足以支撑大流量。结论是应按需选择，无需过早引入数据库，简单文件方案往往已足够。
- Tags: #engineering #why

(2026-04-10) [OpenClaw 实战：一个人、一台 Mac、六个 AI Agent](202604/2026-04-10-openclaw-%E5%AE%9E%E6%88%98%EF%BC%9A%E4%B8%80%E4%B8%AA%E4%BA%BA%E3%80%81%E4%B8%80%E5%8F%B0-mac%E3%80%81%E5%85%AD%E4%B8%AA-ai-agent.md)
- 本文分享基于 OpenClaw 构建生产级 AI 系统的实战经验。通过解决上下文管理、记忆进化及多 Agent 协作三大难题，实现了系统的 7x24 稳定运行与自主迭代。
- Tags: #best-practice #openclaw

(2026-04-10) [拥抱 AI 这一年，我的工具、实践和思考](202604/2026-04-10-%E6%8B%A5%E6%8A%B1-ai-%E8%BF%99%E4%B8%80%E5%B9%B4%EF%BC%8C%E6%88%91%E7%9A%84%E5%B7%A5%E5%85%B7%E3%80%81%E5%AE%9E%E8%B7%B5%E5%92%8C%E6%80%9D%E8%80%83.md)
- 基于作者万元投入 AI 一年的实践，本文分享了从工具链搭建、工程范式从 Prompt 演进至 Harness、到 Agent 驱动知识管理的经验，并探讨了 AI Native 形态与人机关系的思考。
- Tags: #agent #best-practice

(2026-04-10) [Token 经济学七问](202604/2026-04-10-token-%E7%BB%8F%E6%B5%8E%E5%AD%A6%E4%B8%83%E9%97%AE.md)
- Token 正演变为 AI 经济的基础设施。受益于 Agent 需求爆发，全球 Token 消耗呈指数级增长，虽单位成本下降但总支出上升。未来需应对算法出海、跨境监管及法律主体等新挑战。
- Tags: #view

(2026-04-10) [顶级开发团队设计的 Harness 工程项目源码什么样](202604/2026-04-10-%E9%A1%B6%E7%BA%A7%E5%BC%80%E5%8F%91%E5%9B%A2%E9%98%9F%E8%AE%BE%E8%AE%A1%E7%9A%84-harness-%E5%B7%A5%E7%A8%8B%E9%A1%B9%E7%9B%AE%E6%BA%90%E7%A0%81%E4%BB%80%E4%B9%88%E6%A0%B7.md)
- 本文剖析顶级 AI Agent CLI 项目，阐述 Harness Engineering 范式。该范式利用分层启动、安全模型及上下文压缩等强工程设施约束模型，而非依赖智能，打造高可靠 AI Agent 蓝图。
- Tags: #agent #harness #guide #engineering

(2026-04-10) [AI is driving rapid workplace changes, but uneven benefits](202604/2026-04-10-ai-is-driving-rapid-workplace-changes%2C-but-uneven-benefits.md)
- 生成式 AI 正重塑工作本质，从工具转向协作伙伴。虽提升生产力，但存在分配不均及认知挑战。未来工作形态取决于技术构建与选择，人类判断力至关重要。
- Tags: #agent #engineering

(2026-04-08) [从 Rule、Spec 到 Harness：AI Coding 的分阶段演进路径](202604/2026-04-08-%E4%BB%8E-rule%E3%80%81spec-%E5%88%B0-harness%EF%BC%9Aai-coding-%E7%9A%84%E5%88%86%E9%98%B6%E6%AE%B5%E6%BC%94%E8%BF%9B%E8%B7%AF%E5%BE%84.md)
- AI Coding 落地难点不在于模型，而在于工程管控。需建立 Rule、Spec、Loop、Harness 四层架构，逐层收紧控制面，将 AI 从代码生成工具转变为工程边界内稳定工作的交付系统。
- Tags: #agent #engineering

(2026-04-08) [Claude Code 和 OpenClaw 的上下文管理对比](202604/2026-04-08-claude-code-%E5%92%8C-openclaw-%E7%9A%84%E4%B8%8A%E4%B8%8B%E6%96%87%E7%AE%A1%E7%90%86%E5%AF%B9%E6%AF%94.md)
- 文章对比 Claude Code 与 OpenClaw 的上下文管理。Claude Code 利用 API 特性实现低成本压缩与状态恢复；OpenClaw 侧重通用兼容，当前成本高且缺乏深度优化。
- Tags: #agent #openclaw #design

(2026-04-07) [Garbage Collection: From First Principles to Modern Collectors in Java, Go and Python](202604/2026-04-07-garbage-collection-from-first-principles-to-modern-collectors-in-java%2C-go-and-python.md)
- 本文解析 GC 理论演进，对比引用计数与追踪法，深入剖析 Go 语言基于三色标记与混合写屏障的并发实现，旨在最小化 STW 停顿。
- Tags: #design #python #guide

(2026-04-07) [教育的下一步 · 其二](202604/2026-04-07-%E6%95%99%E8%82%B2%E7%9A%84%E4%B8%8B%E4%B8%80%E6%AD%A5-%C2%B7-%E5%85%B6%E4%BA%8C.md)
- 本文提出 AI 时代教育应转向“扩展版计算思维”，包含统计模型、抽象编程与学术写作三大能力。旨在培养个体定义问题、驾驭 AI 的底层素养，最终塑造提出真实问题的品味。
- Tags: #life #education

## Monthly Archive

- [2026-04](202604/monthly-index.md) (20 entries)
- [2026-03](202603/monthly-index.md) (82 entries)

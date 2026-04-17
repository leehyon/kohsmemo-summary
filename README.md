# Bookmark Summary 
自动读取 [kohsmemo](https://github.com/leehyon/kohsmemo) 仓库中的书签数据，通过 Jina Reader 获取网页文本内容，再借助大模型生成内容总结。

## Latest 10 Entries

(2026-04-17) [How to walk through walls](202604/2026-04-17-how-to-walk-through-walls.md)
- Hacker Mindset (黑客思维) 指看穿表象规则，利用底层机制打破限制。文章通过案例说明其在现实中的应用，强调通过动手实践培养此思维，将现实世界视为可被操纵的 playground (游乐场)。
- Tags: #advice #life

(2026-04-17) [Open-Source Agent That Teaches Claude Code Your Architecture](202604/2026-04-17-open-source-agent-that-teaches-claude-code-your-architecture.md)
- 本文介绍 ，通过静态分析提取领域上下文，结合演进式架构解决 AI 缺乏架构感知的局限。该工具赋予 AI 领域理解力，平衡代码构建与长期维护。
- Tags: #agent #best-practice

(2026-04-17) [让 Claude Code 在你睡觉时持续运行：完整实战指南](202604/2026-04-17-%E8%AE%A9-claude-code-%E5%9C%A8%E4%BD%A0%E7%9D%A1%E8%A7%89%E6%97%B6%E6%8C%81%E7%BB%AD%E8%BF%90%E8%A1%8C%EF%BC%9A%E5%AE%8C%E6%95%B4%E5%AE%9E%E6%88%98%E6%8C%87%E5%8D%97.md)
- 本指南详述如何配置 Claude Code 实现无人值守自动化编程。通过设定运行模式、Ralph Wiggum 循环、安全 Hook 及 Docker 隔离环境，使 AI 能够在夜间自动执行代码编写与修复。
- Tags: #agent #setup

(2026-04-17) [从 RAG 到知识编译](202604/2026-04-17-%E4%BB%8E-rag-%E5%88%B0%E7%9F%A5%E8%AF%86%E7%BC%96%E8%AF%91.md)
- 本文探讨从 RAG 向 LLM Wiki 范式的转变。类比“编译执行”，LLM Wiki 在入库时进行结构化处理，实现深度整合与自动化维护。其适用于深度研究，但也面临幻觉与成本挑战。
- Tags: #blog #llm #best-practice

(2026-04-17) [Things you didn't know about indexes](202604/2026-04-17-things-you-didn%27t-know-about-indexes.md)
- 本文解析数据库索引的 B-tree 原理与性能代价，剖析了索引失效的常见原因及  诊断方法，并介绍了函数索引、部分索引及覆盖索引等进阶用法。
- Tags: #guide #why

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

## Monthly Archive

- [2026-04](202604/monthly-index.md) (25 entries)
- [2026-03](202603/monthly-index.md) (82 entries)

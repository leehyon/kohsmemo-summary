# Bookmark Summary 
自动读取 [kohsmemo](https://github.com/leehyon/kohsmemo) 仓库中的书签数据，通过 Jina Reader 获取网页文本内容，再借助大模型生成内容总结。

## Latest 10 Entries

(2026-04-02) [Claude Code 源码泄露过程全解析](202604/2026-04-02-claude-code-%E6%BA%90%E7%A0%81%E6%B3%84%E9%9C%B2%E8%BF%87%E7%A8%8B%E5%85%A8%E8%A7%A3%E6%9E%90.md)
- 本文解析 Anthropic 因 AI 配置失误导致 Claude Code 源码泄露事件，揭示过度依赖 AI 实现极速迭代致使人工审核失效，引发严重安全危机，并探讨了速度与安全间的矛盾。
- Tags: #harness #story

(2026-04-01) [Failure As a Means to Build Resilient Software Systems](202604/2026-04-01-failure-as-a-means-to-build-resilient-software-systems.md)
- 本文探讨利用故障构建韧性系统。指出 Chaos Monkey 等工具的局限，强调从真实事故中学习。文章分析可靠性与复杂性的悖论，主张管理风险吸收能力，并倡导无责备文化以挖掘系统性根源。
- Tags: #engineering

(2026-04-01) [Encoding Team Standards](202604/2026-04-01-encoding-team-standards.md)
- 本文针对 A I 辅助开发中的代码一致性问题，提出将团队编码标准转化为可执行的共享基础设施。通过结构化指令挖掘隐性知识并融入工作流，消除个人提示能力差异，实现团队协作的一致性与高质量交付。
- Tags: #engineering

(2026-04-01) [Rust 所有权：C++ RAII 本来想成为的样子](202604/2026-04-01-rust-%E6%89%80%E6%9C%89%E6%9D%83%EF%BC%9Ac%2B%2B-raii-%E6%9C%AC%E6%9D%A5%E6%83%B3%E6%88%90%E4%B8%BA%E7%9A%84%E6%A0%B7%E5%AD%90.md)
- 本文对比 C++ RAII 与 Rust 所有权，指出前者依赖约定易生隐患，后者由编译器强制执行。Rust 通过借用检查彻底杜绝了内存与并发问题，虽 C++ 有工程优势，但 Rust 真正实现了严格的资源管理目标。
- Tags: #cpp #design

(2026-03-31) [从 Vibe Coding 到范式编程](202603/2026-03-31-%E4%BB%8E-vibe-coding-%E5%88%B0%E8%8C%83%E5%BC%8F%E7%BC%96%E7%A8%8B.md)
- 文章提出从 Vibe Coding 向范式编程演进。针对企业级痛点，采用 Spec 驱动开发，结合知识库与 AI Agent，以规范为核心构建体系，实现高质量人机协同。
- Tags: #engineering #vibe-coding

(2026-03-31) [胶水编程：业务需求出码最佳实践](202603/2026-03-31-%E8%83%B6%E6%B0%B4%E7%BC%96%E7%A8%8B%EF%BC%9A%E4%B8%9A%E5%8A%A1%E9%9C%80%E6%B1%82%E5%87%BA%E7%A0%81%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5.md)
- 天猫提出“胶水编程”，构建四层物料体系，将 AI 转变为装配工。通过“能抄不写”策略，代码采纳率升至 97.9%，实现了高匹配度场景下的高效与高质量交付。
- Tags: #agent #best-practice #vibe-coding

(2026-03-31) [模型智能提升的下一个关键方向](202603/2026-03-31-%E6%A8%A1%E5%9E%8B%E6%99%BA%E8%83%BD%E6%8F%90%E5%8D%87%E7%9A%84%E4%B8%8B%E4%B8%80%E4%B8%AA%E5%85%B3%E9%94%AE%E6%96%B9%E5%90%91.md)
- AI 工程转向构建 Harness 系统，决定 Agent 性能上限。通过捕获执行轨迹实现“训练即部署”闭环，模型与系统共生演化。未来将向 Coordination Engineering 演进。
- Tags: #agent #llm

(2026-03-31) [OpenClaw：技术解读和给 AI 应用开发的启示（2026）](202603/2026-03-31-openclaw%EF%BC%9A%E6%8A%80%E6%9C%AF%E8%A7%A3%E8%AF%BB%E5%92%8C%E7%BB%99-ai-%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E7%9A%84%E5%90%AF%E7%A4%BA%EF%BC%882026%EF%BC%89.md)
- OpenClaw 是系统级个人 AI 助手。文章通过 ToyClaw 揭示其核心机制，详述 Gateway 架构与 Skill 系统，强调利用 .md 文件构建记忆与人格，旨在让 AI 真正操控电脑并执行实际任务。
- Tags: #agent #openclaw

(2026-03-31) [How I manage Images for my Blog](202603/2026-03-31-how-i-manage-images-for-my-blog.md)
- 作者为解决手动导出 Excalidraw 配图效率低的问题，通过 Fork VSCode 扩展，实现了监听文件变化并自动导出双主题 SVG 图片的功能，达成本地实时预览，显著提升了写作体验。
- Tags: #blog #setup

(2026-03-31) [AI Agent 正在进入工程化深水区](202603/2026-03-31-ai-agent-%E6%AD%A3%E5%9C%A8%E8%BF%9B%E5%85%A5%E5%B7%A5%E7%A8%8B%E5%8C%96%E6%B7%B1%E6%B0%B4%E5%8C%BA.md)
- AI Agent 竞争重心已从模型能力转向工程系统能力。通过模型专用化、框架生产化、架构分层及协议标准化，Agent 正演变为系统基础设施，未来核心竞争在于构建完整的工程体系。
- Tags: #agent #engineering

## Monthly Archive

- [2026-04](202604/monthly-index.md) (4 entries)
- [2026-03](202603/monthly-index.md) (82 entries)

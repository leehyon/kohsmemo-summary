# Bookmark Summary 
自动读取 [kohsmemo](https://github.com/leehyon/kohsmemo) 仓库中的书签数据，通过 Jina Reader 获取网页文本内容，再借助大模型生成内容总结。

## Latest 10 Entries

(2026-03-26) [ripgrep is faster than {grep, ag, git grep, ucg, pt, sift}](202603/2026-03-26-ripgrep-is-faster-than-%7Bgrep%2C-ag%2C-git-grep%2C-ucg%2C-pt%2C-sift%7D.md)
- 本文介绍 Rust 编写的命令行搜索工具 `ripgrep`，旨在替代现有工具。它结合易用性与高性能，解析了其利用有限自动机、SIMD 算法及增量搜索实现极速的技术原理，并论证了其在速度与正确性上的显著优势。
- Tags: #linux

(2026-03-26) [Quantization from the ground up](202603/2026-03-26-quantization-from-the-ground-up.md)
- 本文解析 LLM 量化原理，通过降低数值精度实现模型缩容与提速。介绍了非对称量化及分块处理 Outliers 策略。实测表明，4-bit 量化性能接近原模型，而 2-bit 效果极差。
- Tags: #llm #math

(2026-03-26) [Thoughts on slowing the fuck down](202603/2026-03-26-thoughts-on-slowing-the-fuck-down.md)
- 盲目依赖 AI Agent 会导致软件质量崩塌与复杂性失控。开发者应回归人类主导，主动降速，仅将 Agent 用于辅助。通过手写核心代码保持掌控，最终构建高质量、可维护的软件系统。
- Tags: #agent

(2026-03-25) [历史不站在你以为的那一边](202603/2026-03-25-%E5%8E%86%E5%8F%B2%E4%B8%8D%E7%AB%99%E5%9C%A8%E4%BD%A0%E4%BB%A5%E4%B8%BA%E7%9A%84%E9%82%A3%E4%B8%80%E8%BE%B9.md)
- 技术革命下，手艺人面临隐蔽的“降级”与“去技能化”。技术路径实为权力博弈的结果。AI 将剥夺程序员的决策权，使其沦为操作员，这种去技能化比失业更致命。
- Tags: #engineering #career

(2026-03-25) [Claude Code 的三种 Skill 类型以及一些常见陷阱](202603/2026-03-25-claude-code-%E7%9A%84%E4%B8%89%E7%A7%8D-skill-%E7%B1%BB%E5%9E%8B%E4%BB%A5%E5%8F%8A%E4%B8%80%E4%BA%9B%E5%B8%B8%E8%A7%81%E9%99%B7%E9%98%B1.md)
- 本文探讨 Claude Code 的 Agentic Engineering，详解三种 Skill 类型以优化 AI 协作，揭示反模式与子 Agent 管理陷阱，并汇总高频命令提升开发效率。
- Tags: #best-practice #agent

(2026-03-25) [OpenClaw 必装 10 大技能](202603/2026-03-25-openclaw-%E5%BF%85%E8%A3%85-10-%E5%A4%A7%E6%8A%80%E8%83%BD.md)
- 本文介绍了 OpenClaw AI Agent 的 10 大必装技能，涵盖搜索、内容处理及效率提升三大维度，旨在将工具从“能用”升级为“好用”。
- Tags: #setup #openclaw

(2026-03-25) [一份关于 AI 编程的简明行为指南](202603/2026-03-25-%E4%B8%80%E4%BB%BD%E5%85%B3%E4%BA%8E-ai-%E7%BC%96%E7%A8%8B%E7%9A%84%E7%AE%80%E6%98%8E%E8%A1%8C%E4%B8%BA%E6%8C%87%E5%8D%97.md)
- 本文倡导 AI 编程坚持“人为主导、 AI 协作”，强调工程师担责并理解代码。建议控制 PR 粒度，优选成熟库，强化验证。初级工程师应重质量补架构，避免盲目依赖，利用 AI 提升能力。
- Tags: #agent #advice

(2026-03-25) [基于 Cloudflare 生态的 AI Agent 实现](202603/2026-03-25-%E5%9F%BA%E4%BA%8E-cloudflare-%E7%94%9F%E6%80%81%E7%9A%84-ai-agent-%E5%AE%9E%E7%8E%B0.md)
- 本文介绍了基于 Cloudflare 生态构建的个人博客 AI Agent，拆分了管理与用户端服务。文章采用 Workers + D1 + 裸 API 架构，利用 R2 和 AI Search 实现 RAG，并分享了实践经验。
- Tags: #agent #engineering

(2026-03-25) [可能是最后一次更换博客引擎](202603/2026-03-25-%E5%8F%AF%E8%83%BD%E6%98%AF%E6%9C%80%E5%90%8E%E4%B8%80%E6%AC%A1%E6%9B%B4%E6%8D%A2%E5%8D%9A%E5%AE%A2%E5%BC%95%E6%93%8E.md)
- 作者将博客从 Astro 迁移至基于 Bun 的自建引擎，通过极致减法与 AI 辅助，大幅提升构建性能。文章探讨了 AI 时代框架价值的重构，认为低复杂度场景下应减少抽象，让框架回归架构本质。
- Tags: #blog #setup

(2026-03-25) [如何让 OpenClaw 更好用 - 调教篇](202603/2026-03-25-%E5%A6%82%E4%BD%95%E8%AE%A9-openclaw-%E6%9B%B4%E5%A5%BD%E7%94%A8---%E8%B0%83%E6%95%99%E7%AF%87.md)
- 本文旨在通过制定涵盖错误处理、记忆管理及工作流优化的系统化规则，提升 OpenClaw AI Agent 的稳定性与效率，解决幻觉及操作失误问题，并提供实战避坑指南。
- Tags: #best-practice #agent

## Monthly Archive

- [2026-03](202603/monthly-index.md) (70 entries)

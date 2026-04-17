# How I run multiple $10K MRR companies on a $20/month tech stack
- URL: https://stevehanov.ca/blog/how-i-run-multiple-10k-mrr-companies-on-a-20month-tech-stack
- Added: 2026-04-17 02:49:46
- Tags: #setup

## TL;DR
本文阐述利用 Go、SQLite 和廉价 VPS 构建极简技术栈，以月费 $20 运营高收入公司。通过本地 GPU 优化 AI 策略，实现高效、低依赖的独立开发模式。

## Summary
**核心主题**
本文阐述了如何通过极致精简的技术栈，以每月约 $20 的低成本运营多家 MRR 超过 $10,000 的公司，强调高效率、低依赖和长生存期的独立开发模式。

**关键信息与逻辑脉络**

*   **基础设施**
    *   避免使用 AWS 等复杂且昂贵的云原生架构（如 EKS、RDS）。
    *   选择廉价可靠的 VPS 提供商（如 Linode、DigitalOcean），月费控制在 $5 至 $10。
    *   即使仅有 1GB 内存，配合 Swapfile 机制也足以支撑服务。

*   **后端语言**
    *   选用 Go 语言开发后端，利用其高性能和强类型特性。
    *   利用 Go 的静态编译特性，将应用打包为单一二进制文件，避免依赖管理地狱，并实现极简部署。

*   **AI 策略**
    *   **长时任务**：利用本地 GPU（如二手 RTX 3090）运行 VLLM 处理大批量任务，无需支付持续的 API 费用；配合自研工具 `laconic` 和 `llmhub` 优化上下文管理。
    *   **即时交互**：使用 OpenRouter 聚合 Claude、OpenAI 等前沿模型，通过统一接口实现无缝的故障转移，确保服务稳定性。

*   **开发工具**
    *   坚持 GitHub Copilot 替代昂贵的 AI IDE（如 Cursor）。
    *   利用 Copilot 按“请求”而非“Token”计费的机制，通过编写详细提示词，以极低成本让 AI 处理大量代码任务。

*   **数据库**
    *   全面使用 SQLite 作为主数据库，通过开启 WAL (Write-Ahead Logging) 模式解决并发读写阻塞问题，利用本地文件的高 I/O 速度超越网络数据库。
    *   使用自研的 `smhanov/auth` 库处理用户认证，集成第三方登录且无臃肿依赖。

*   **核心哲学**
    *   低成本运营等同于获得巨额融资般的生存期，能降低压力并保持架构简单。
    *   将精力集中于寻找产品市场契合度与解决用户问题，而非管理基础设施和应对投资人压力。

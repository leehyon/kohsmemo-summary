# 基于 Cloudflare 生态的 AI Agent 实现
- URL: https://surmon.me/article/307
- Added: 2026-03-25 02:54:50
- Tags: #agent #engineering

## TL;DR
本文介绍了基于 Cloudflare 生态构建的个人博客 AI Agent，拆分了管理与用户端服务。文章采用 Workers + D1 + 裸 API 架构，利用 R2 和 AI Search 实现 RAG，并分享了实践经验。

## Summary
核心主题：基于 Cloudflare 生态构建个人博客 AI Agent，实现针对管理端与用户端不同需求的服务拆分，利用 RAG 技术打造能精准回答博客内容的智能助手。

关键信息与逻辑脉络：

1. 业务需求拆分
   - 管理端服务：集成在 NodePress 中，提供摘要生成、文章点评、评论回复等功能。特点是无状态、短上下文，直接通过 Cloudflare AI Gateway 调用 LLM。
   - 用户端服务：独立的 AI Agent 应用，负责前台智能对话。需求包括 RAG 知识库、对话持久化、限流及管理员查看记录，通过 Cloudflare Workers + D1 实现。

2. RAG 知识库构建
   - 数据源选择：放弃爬虫方案（存在 HTML 噪音和长文截断问题），转用 R2 存储桶存储纯净的 Markdown 文件，利用 Frontmatter 添加元数据。
   - 同步机制：NodePress 通过 Webhook 异步通知 AI 服务，AI 服务更新 R2 文件后，AI Search 自动触发增量索引，实现全自动无感更新。
   - 备选方案：低成本场景可使用 Algolia 搜索配合 LLM 关键词分解模拟 RAG，虽简单但语义理解能力弱。

3. 技术选型与避坑
   - Cloudflare Agents SDK：基于 Durable Object 构建数据孤岛，适合强实时协作，但不适合需要集中查询所有对话记录的管理后台场景，故弃用。
   - Vercel AI SDK：设计哲学为“前端驱动”，假设前端持有状态，与作者“服务端驱动”的架构冲突，且易受版本迭代影响，故弃用。
   - 最终架构：回归 Workers + D1 + 裸 API，自行实现简单的 Agent Loop，保证架构解耦与数据稳定性。

4. 核心架构设计
   - 身份识别：使用 HMAC-SHA256 签名的 Session Token 进行匿名会话管理。
   - 数据存储：参考 OpenAI 消息结构设计 D1 表，包含 user、assistant、tool、system 角色，确保与模型解耦。
   - 对话流程：限流拦截 -> 验证 Token -> 组装上下文（R2 静态文件 + D1 历史消息） -> Agent Loop 循环 -> SSE 流式响应 -> 异步入库。
   - 历史边界：发送给 LLM 的历史记录中过滤掉 `tool` 类消息，仅保留纯文本对话，防止 API 报错并节省 Token。

5. 安全与模型调优
   - 三层限流：Cloudflare Workers IP 限流、D1 会话层限流、AI Gateway 支出限流。
   - 安全防护：System Prompt 中内置规则，拒绝角色扮演和指令泄露。
   - 模型选择：DeepSeek（推理能力强、中文好、成本低）作为主力；Gemini（克制、听话）作为备选，需针对不同模型定制 Prompt。

6. 经验总结与技术栈
   - 经验：“用起来简单”未必高效（如爬虫 vs R2），应选择适合业务而非理论最优的架构；避免深度绑定 SDK，数据模型应基于事实标准（OpenAI 格式）；知识库数据质量至关重要。
   - 技术栈：Cloudflare Workers, Hono, D1, R2, AI Search, AI Gateway, Zod, DeepSeek/Gemini。

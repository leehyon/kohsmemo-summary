# Ruby Is the Best Language for Building AI Apps
- URL: https://paolino.me/ruby-is-the-best-language-for-ai-apps/
- Added: 2026-03-27 01:52:51
- Tags: #engineering

## TL;DR
Ruby 凭借开发效率和代码优雅性，成为 2026 年构建 AI 应用的最佳语言。相比 Python 和 JS，RubyLLM 更简洁，Rails 提供全栈支持，Async 生态处理并发，获社区高度认可。

## Summary
**核心主题**
Ruby 是 2026 年构建 AI 应用的最佳语言，尤其在产品化与应用开发层面，其优越性体现在开发效率、代码优雅性及全栈集成能力上。

**逻辑脉络**
文章首先指出模型训练生态（Python 的主场）与应用开发（HTTP 调用与 Web 工程）的区别，确立了 AI 应用开发本质是 Web 开发的前提。随后通过代码对比，展示了 Ruby 相较于 Python (LangChain) 和 JavaScript (AI SDK) 在简洁性和抽象层面上的优势。接着，文章阐述了 Rails 框架如何为 AI 应用提供除模型调用外的所有基础设施，并结合 Ruby 的 Async 生态解答了关于性能与扩展性的疑虑。最后，通过社区反响和用户证言验证了 Ruby 社区对 AI 应用开发的适应性与接纳度。

**关键信息**
- **训练与应用的分离**：Python 虽然主导了 PyTorch 等模型训练领域，但绝大多数开发者仅通过 API 调用模型。AI 应用的核心在于流式响应、对话持久化、成本追踪等 Web 工程问题，这正是 Ruby 和 Rails 的强项。
- **极致的开发体验**：
  - **简单聊天**：RubyLLM 的代码 (`RubyLLM.chat.ask "Hello!"`) 比 Python 和 JavaScript 更接近自然语言，消除了冗余的语法噪声。
  - **Token 追踪**：不同于 LangChain 在不同模型间返回混乱的数据结构，RubyLLM 提供统一的接口 (`response.tokens.input/output`)。
  - **Agents 实现**：RubyLLM 使用类定义 Agents，代码极具可读性，极大降低了编写智能体的复杂度。
- **认知开销的优化**：Ruby 将优雅的 API 视为工程核心，通过统一的抽象减少了开发者需要记忆的提供商特定细节和数据结构，从而降低认知负担，减少 Bug 并提升重构效率。
- **Rails 的全栈赋能**：除了模型调用，AI 应用还需要认证、计费、后台作业、流式 UI 等功能。Rails 为此提供了成熟且一致的解决方案，结合 RubyLLM 可用极少的代码实现流式聊天和持久化。
- **并发与可扩展性**：LLM 工作负载主要是网络和流式传输限制的。Ruby 的 Async 生态利用 Fibers 处理高并发，无需 `async`/`await` 关键字即可避免线程爆炸，适合 AI 应用的 IO 密集型场景。
- **社区验证与迁移**：RubyLLM 在 Hacker News 上排名第一并获得数百万下载，而其 API 设计的 JavaScript 移植版 (NodeLLM) 反响平平。多支团队反馈从 LangChain 迁移至 RubyLLM 后，代码更简洁、性能更优、开发体验显著提升。

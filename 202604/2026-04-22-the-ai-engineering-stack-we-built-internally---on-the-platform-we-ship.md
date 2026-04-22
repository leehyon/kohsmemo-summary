# The AI engineering stack we built internally - on the platform we ship
- URL: https://blog.cloudflare.com/internal-ai-engineering-stack/
- Added: 2026-04-22 03:16:56
- Tags: #engineering #agent

## TL;DR
Cloudflare 利用 Access 、 AI Gateway 等自家产品构建 AI 堆栈。通过安全路由及自动审查，实现 93% R&D 采用率，大幅提升研发效能，使合并请求数翻倍。

## Summary
核心主题
Cloudflare 利用自家的开发者平台产品（如 Cloudflare Access、AI Gateway、Workers AI 等）构建了一套内部 AI 工程堆栈，实现了大规模的 AI 编码工具集成，显著提升了研发效能。

关键信息
- **采用规模**：过去 30 天内，Cloudflare 全公司 60% 的员工（3,683 名用户）使用了 AI 编码工具，其中 R&D 部门采用率高达 93%，覆盖 295 个团队。
- **使用量级**：累计产生 4,795 万次 AI 消息请求；AI Gateway 路由了 2,413.7 亿个 Token；Workers AI 处理了 518.3 亿个 Token。
- **效能提升**：周平均合并请求数量显著增加，从约 5,600 上升至 8,700 以上，峰值达到 10,952，几乎翻倍。
- **产品复用**：内部架构完全基于 Cloudflare 对外交付的产品构建，无专用内部基础设施。

逻辑脉络

**1. 平台层：基础设施与路由**
- **安全与鉴权**：通过 Cloudflare Access 实现零信任认证，确保访问安全。
- **统一路由与管理**：所有 LLM 请求经由 AI Gateway 进行路由，实现成本追踪、密钥管理和零数据保留（ZDR）策略控制。
- **推理加速与降本**：Workers AI 提供同网络推理，降低延迟与成本。Frontier 模型处理复杂任务，Workers AI（如 Kimi K2.5）处理安全扫描、文档审查等任务，节省约 77% 成本。
- **配置自动化**：通过单一 Worker 代理，用户执行一条命令即可自动完成认证、配置 MCP 服务器和模型目录，无需手动管理 API Key。
- **MCP 整合与 Code Mode**：MCP Server Portal 统一了 182+ 个内部工具。采用 Code Mode 模式，将工具 Schema 转换为代码调用，大幅减少上下文 Token 消耗，降低架构复杂度。

**2. 知识层：上下文理解**
- **服务目录**：利用 Backstage 构建服务知识图谱，记录 2,055 个服务、依赖关系及数据库映射，使 AI 能理解代码库之外的系统架构。
- **仓库上下文标准化**：推行 AGENTS.md 文件，自动为每个仓库生成包含运行时环境、测试命令、代码规范和边界的说明，确保 AI 理解特定仓库的上下文和规则。

**3. 执行层：质量与标准管控**
- **AI Code Reviewer**：集成到 CI 流水线，利用多代理系统（涵盖安全、性能、合规等）对每个 Merge Request 进行自动审查，覆盖率达 100%。
- **Engineering Codex**：建立工程标准系统，将内部规范转化为 AI 可引用的 Codex 规则，并在代码审查中自动引用具体规则 ID，确保工程标准的一致执行。

**未来演进**
计划引入后台代理，利用 Agents SDK 和 Sandbox SDK 实现云端长时间运行的会话，支持克隆仓库、运行测试等完整的开发环境操作。

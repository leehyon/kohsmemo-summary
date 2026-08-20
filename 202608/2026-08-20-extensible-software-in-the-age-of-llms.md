# Extensible Software in the age of LLMs
- URL: https://jeremymorrell.dev/blog/extensible-software-in-the-age-of-llms/
- Added: 2026-08-20 03:07:57
- Tags: #llm #agent

## TL;DR
本文提出以“稳固核心+能力沙箱+LLM”构建可扩展 Web 软件，让用户通过自然语言生成安全扩展，并以 Cloudflare Dynamic Workers 为例说明实现可能。

## Summary
本文提出以“稳固核心+能力沙箱+LLM”构建可扩展 Web 软件，解决静态软件无法满足用户长尾需求的问题。作者认为 LLM 降低了编写扩展的门槛，而沙箱技术提供了安全边界，并以 Cloudflare Dynamic Workers 为例，展示了实现路径。

**逻辑脉络**
- 静态软件只服务主流需求，UI 复杂度限制了功能堆叠；LLM 让用户能自行定制，但现有软件缺乏安全扩展机制。
- 从 AI 代理、内部平台、支持平台和可观测性场景，说明“自扩展”模式的需求。
- Web 扩展面临崩溃影响、数据泄露、DoS、Spectre 等安全挑战，但 Salesforce 的 Apex 证明其可行性。
- 技术需求提炼为：廉价、冷启动快、可限制、隔离强、能力安全。
- 比较解释器、V8 isolates、MicroVM、WASM 后，指出 Dynamic Workers 提供更完备的生产级框架。

**Takeaways**
- 静态软件仅覆盖需求曲线顶端，LLM 使长尾定制成为可能，但需要新的软件模式。
- 安全的扩展机制应基于“能力”而非“原始 API 密钥”：代码只能通过显式传递的引用操作，避免泄露。
- 构建可扩展 Web 平台需关注：成本、冷启动、资源限制、强隔离（含 Spectre）、受控动作。
- Cloudflare Dynamic Workers 内置可观测性、多租户存储、持久执行、源码控制与 LLM 能力，适合作为基础。
- 平台建设虽难，但能激发用户创造力，值得投入。

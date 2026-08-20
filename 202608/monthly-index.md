# 2026-08 Monthly Index

(2026-08-20) [Extensible Software in the age of LLMs](2026-08-20-extensible-software-in-the-age-of-llms.md)
- 本文提出以“稳固核心+能力沙箱+LLM”构建可扩展 Web 软件，让用户通过自然语言生成安全扩展，并以 Cloudflare Dynamic Workers 为例说明实现可能。
- Tags: #llm #agent

(2026-08-20) [The two factions of C++](2026-08-20-the-two-factions-of-c%2B%2B.md)
- 文章分析 C++ 因向后兼容与安全需求之间的根本冲突而分裂为现代与遗留两大阵营，指出工具链和构建能力是分水岭，并解释了委员会在 Safety Profiles 等提案上的立场。
- Tags: #language

(2026-08-18) [聊一聊商业产品背后的定价逻辑](2026-08-18-%E8%81%8A%E4%B8%80%E8%81%8A%E5%95%86%E4%B8%9A%E4%BA%A7%E5%93%81%E8%83%8C%E5%90%8E%E7%9A%84%E5%AE%9A%E4%BB%B7%E9%80%BB%E8%BE%91.md)
- 会员制与订阅制利用使用强度差异，让低频用户补贴高频用户，实现整体盈利。AI 因成本更高需限额与分级。消费者判断是否值得付费，应看过去实际用量，并用回本次数计算盈亏平衡。
- Tags: #explained

(2026-08-17) [AI 时代我的开发工作流：从踩坑复盘到多项目并行验证](2026-08-17-ai-%E6%97%B6%E4%BB%A3%E6%88%91%E7%9A%84%E5%BC%80%E5%8F%91%E5%B7%A5%E4%BD%9C%E6%B5%81%EF%BC%9A%E4%BB%8E%E8%B8%A9%E5%9D%91%E5%A4%8D%E7%9B%98%E5%88%B0%E5%A4%9A%E9%A1%B9%E7%9B%AE%E5%B9%B6%E8%A1%8C%E9%AA%8C%E8%AF%81.md)
- AI 时代作者从深度钻研转向多项目并行，通过 CLI 和 Skill 将踩坑会话自动沉淀为文章，并利用 LobeHub 的 acceptance skill 实现 UI 自动化验收，显著提升开发效率。
- Tags: #agent #workflow

(2026-08-17) [Elevators](2026-08-17-elevators.md)
- 电梯调度算法远比想象复杂；简单 LOOK 在高流量时优于花哨的 RSR，目的地派梯因缺乏灵活性反而更慢，核心在于动态重优化与灵活性。

(2026-08-17) [My server is a phone now](2026-08-17-my-server-is-a-phone-now.md)
- 作者用闲置的 CMF Phone 1 刷 Android + Termux + chroot 替代 VPS，通过 Ansible 管理、Cloudflare Tunnel 和 Tailscale 接入，跑 Surf 等个人服务，省钱又可复现。
- Tags: #setup #home

(2026-08-17) [Use Task Runners for Common Coding Tasks](2026-08-17-use-task-runners-for-common-coding-tasks.md)
- 作者建议用任务运行器（bash 脚本、make、just、mise）统一跨仓库的构建、测试、格式化等常见命令，避免记忆各技术栈的不同命令，只需执行统一的 run build、make test 等。提供实现示例和优缺点。
- Tags: #efficiency

(2026-08-17) [Your Agentic Workflow's Cache Keepalive Costs 8x Too Much](2026-08-17-your-agentic-workflow%27s-cache-keepalive-costs-8x-too-much.md)
- 常见的 30 秒缓存 keepalive 比最优贵约 8 倍。实测显示 Anthropic 最优约 4 分钟、OpenAI 约 8 分钟，超过 TTL 的 ping 会反复重建死缓存。只在暂停超过驱逐点、低于盈亏平衡点（约 46 分钟）时保温才省钱；DeepSeek、Gemini 只值延迟。
- Tags: #agent

(2026-08-12) [我是怎么用 Hermes 的](2026-08-12-%E6%88%91%E6%98%AF%E6%80%8E%E4%B9%88%E7%94%A8-hermes-%E7%9A%84.md)
- 作者亲测 Hermes Agent 半年，认为其最大优势是能直接操作电脑，通过 Telegram 查告警、回飞书、写代码等。核心在于技能与记忆系统，让 AI 助手与工作流深度粘合。
- Tags: #agent

(2026-08-11) [Pi, Minimal and Performant](2026-08-11-pi%2C-minimal-and-performant.md)
- Pi 以极简设计（仅 4 工具、<1,000 tokens 提示）成为高性能编码 harness；Databricks 与 Shopify 案例显示它更便宜、更快、更可扩展，通过上下文纪律与可扩展机制优于复杂工具。
- Tags: #agent #benchmark

(2026-08-10) [How a Frontier Model Gets Built, Read from the Kimi K3 Report](2026-08-10-how-a-frontier-model-gets-built%2C-read-from-the-kimi-k3-report.md)
- Kimi K3 报告显示，构建前沿模型的重心在环境、数据与系统工程而非模型；开源最强模型接近封闭前沿，但需警惕滥用风险。
- Tags: #agent

(2026-08-10) [对话李开复：小人物的机会，在哪里？](2026-08-10-%E5%AF%B9%E8%AF%9D%E6%9D%8E%E5%BC%80%E5%A4%8D%EF%BC%9A%E5%B0%8F%E4%BA%BA%E7%89%A9%E7%9A%84%E6%9C%BA%E4%BC%9A%EF%BC%8C%E5%9C%A8%E5%93%AA%E9%87%8C%EF%BC%9F.md)
- 李开复指出 AI 的真正价值在于 AI-native 转型与承担责任，DRI 和 OPC 带来新机会，而爱和判断力仍是人类的核心竞争力。
- Tags: #career

(2026-08-10) [Agent 插件如何走向工程化](2026-08-10-agent-%E6%8F%92%E4%BB%B6%E5%A6%82%E4%BD%95%E8%B5%B0%E5%90%91%E5%B7%A5%E7%A8%8B%E5%8C%96.md)
- Agent 插件工程化需把能力当软件资产：通过规格驱动、上下文编排、确定性验证、行为评测、证据闭环五个实践，确保插件可验证、可维护、可持续演进。核心是让每一次修改都有证据证明变得更好。
- Tags: #engineering #agent

(2026-08-10) [This CPO regrets that product management exists](2026-08-10-this-cpo-regrets-that-product-management-exists.md)
- Whatnot 的 CPO Tom Verrilli 主张“后悔产品管理存在”，让资深 PM 直接做 IC 工作，并借助 AI 重塑产品角色，避免组织陷入流程戏剧。
- Tags: #transcript

(2026-08-10) [Open Weights and American AI Leadership](2026-08-10-open-weights-and-american-ai-leadership.md)
- 文章呼吁美国支持开放权重 AI 模型，认为这能扩大创新、竞争与安全，并借开源历史强调开放生态对美国 AI 领导力的重要性。

(2026-08-10) [预测市场生态的项目为什么难做](2026-08-10-%E9%A2%84%E6%B5%8B%E5%B8%82%E5%9C%BA%E7%94%9F%E6%80%81%E7%9A%84%E9%A1%B9%E7%9B%AE%E4%B8%BA%E4%BB%80%E4%B9%88%E9%9A%BE%E5%81%9A.md)
- 团队半年来在预测市场生态尝试了语义搜索、聚合终端、Copy Trading、Agentic Trading 等多个方向，均未找到 PMF。核心问题是获客难，以及 Polymarket 作为中心化平台对第三方项目的结构性挤压。
- Tags: #product

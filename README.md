# Bookmark Summary 
自动读取 [kohsmemo](https://github.com/leehyon/kohsmemo) 仓库中的书签数据，通过 Jina Reader 获取网页文本内容，再借助大模型生成内容总结。

## Latest 10 Entries

(2026-08-17) [My server is a phone now](202608/2026-08-17-my-server-is-a-phone-now.md)
- 作者用闲置的 CMF Phone 1 刷 Android + Termux + chroot 替代 VPS，通过 Ansible 管理、Cloudflare Tunnel 和 Tailscale 接入，跑 Surf 等个人服务，省钱又可复现。
- Tags: #setup #home

(2026-08-17) [Use Task Runners for Common Coding Tasks](202608/2026-08-17-use-task-runners-for-common-coding-tasks.md)
- 作者建议用任务运行器（bash 脚本、make、just、mise）统一跨仓库的构建、测试、格式化等常见命令，避免记忆各技术栈的不同命令，只需执行统一的 run build、make test 等。提供实现示例和优缺点。
- Tags: #efficiency

(2026-08-17) [Your Agentic Workflow's Cache Keepalive Costs 8x Too Much](202608/2026-08-17-your-agentic-workflow%27s-cache-keepalive-costs-8x-too-much.md)
- 常见的 30 秒缓存 keepalive 比最优贵约 8 倍。实测显示 Anthropic 最优约 4 分钟、OpenAI 约 8 分钟，超过 TTL 的 ping 会反复重建死缓存。只在暂停超过驱逐点、低于盈亏平衡点（约 46 分钟）时保温才省钱；DeepSeek、Gemini 只值延迟。
- Tags: #agent

(2026-08-12) [我是怎么用 Hermes 的](202608/2026-08-12-%E6%88%91%E6%98%AF%E6%80%8E%E4%B9%88%E7%94%A8-hermes-%E7%9A%84.md)
- 作者亲测 Hermes Agent 半年，认为其最大优势是能直接操作电脑，通过 Telegram 查告警、回飞书、写代码等。核心在于技能与记忆系统，让 AI 助手与工作流深度粘合。
- Tags: #agent

(2026-08-11) [Pi, Minimal and Performant](202608/2026-08-11-pi%2C-minimal-and-performant.md)
- Pi 以极简设计（仅 4 工具、<1,000 tokens 提示）成为高性能编码 harness；Databricks 与 Shopify 案例显示它更便宜、更快、更可扩展，通过上下文纪律与可扩展机制优于复杂工具。
- Tags: #agent #benchmark

(2026-08-10) [How a Frontier Model Gets Built, Read from the Kimi K3 Report](202608/2026-08-10-how-a-frontier-model-gets-built%2C-read-from-the-kimi-k3-report.md)
- Kimi K3 报告显示，构建前沿模型的重心在环境、数据与系统工程而非模型；开源最强模型接近封闭前沿，但需警惕滥用风险。
- Tags: #agent

(2026-08-10) [对话李开复：小人物的机会，在哪里？](202608/2026-08-10-%E5%AF%B9%E8%AF%9D%E6%9D%8E%E5%BC%80%E5%A4%8D%EF%BC%9A%E5%B0%8F%E4%BA%BA%E7%89%A9%E7%9A%84%E6%9C%BA%E4%BC%9A%EF%BC%8C%E5%9C%A8%E5%93%AA%E9%87%8C%EF%BC%9F.md)
- 李开复指出 AI 的真正价值在于 AI-native 转型与承担责任，DRI 和 OPC 带来新机会，而爱和判断力仍是人类的核心竞争力。
- Tags: #career

(2026-08-10) [Agent 插件如何走向工程化](202608/2026-08-10-agent-%E6%8F%92%E4%BB%B6%E5%A6%82%E4%BD%95%E8%B5%B0%E5%90%91%E5%B7%A5%E7%A8%8B%E5%8C%96.md)
- Agent 插件工程化需把能力当软件资产：通过规格驱动、上下文编排、确定性验证、行为评测、证据闭环五个实践，确保插件可验证、可维护、可持续演进。核心是让每一次修改都有证据证明变得更好。
- Tags: #engineering #agent

(2026-08-10) [This CPO regrets that product management exists](202608/2026-08-10-this-cpo-regrets-that-product-management-exists.md)
- Whatnot 的 CPO Tom Verrilli 主张“后悔产品管理存在”，让资深 PM 直接做 IC 工作，并借助 AI 重塑产品角色，避免组织陷入流程戏剧。
- Tags: #transcript

(2026-08-10) [Open Weights and American AI Leadership](202608/2026-08-10-open-weights-and-american-ai-leadership.md)
- 文章呼吁美国支持开放权重 AI 模型，认为这能扩大创新、竞争与安全，并借开源历史强调开放生态对美国 AI 领导力的重要性。

## Monthly Archive

- [2026-08](202608/monthly-index.md) (11 entries)
- [2026-07](202607/monthly-index.md) (53 entries)
- [2026-06](202606/monthly-index.md) (68 entries)
- [2026-05](202605/monthly-index.md) (26 entries)
- [2026-04](202604/monthly-index.md) (44 entries)
- [2026-03](202603/monthly-index.md) (82 entries)

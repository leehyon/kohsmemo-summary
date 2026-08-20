# Bookmark Summary 
自动读取 [kohsmemo](https://github.com/leehyon/kohsmemo) 仓库中的书签数据，通过 Jina Reader 获取网页文本内容，再借助大模型生成内容总结。

## Latest 10 Entries

(2026-08-20) [The Same Side of the Table](202608/2026-08-20-the-same-side-of-the-table.md)
- 管理者与下属开会时必须始终站在同一战线，团队失误就是自己的失误；用接管、暂停、防守等方式保护下属，能建立信任并避免恐惧文化。
- Tags: #career

(2026-08-20) [AI is removing the middle class of software engineering](202608/2026-08-20-ai-is-removing-the-middle-class-of-software-engineering.md)
- AI 让写代码变快，但理解代码仍然很慢，因此坏决策快速堆积，工程文化弱的项目迅速崩溃。中层工程师被淘汰，真正理解系统的人变得更重要。
- Tags: #agent #engineering #career

(2026-08-20) [Extensible Software in the age of LLMs](202608/2026-08-20-extensible-software-in-the-age-of-llms.md)
- 本文提出以“稳固核心+能力沙箱+LLM”构建可扩展 Web 软件，让用户通过自然语言生成安全扩展，并以 Cloudflare Dynamic Workers 为例说明实现可能。
- Tags: #llm #agent

(2026-08-20) [The two factions of C++](202608/2026-08-20-the-two-factions-of-c%2B%2B.md)
- 文章分析 C++ 因向后兼容与安全需求之间的根本冲突而分裂为现代与遗留两大阵营，指出工具链和构建能力是分水岭，并解释了委员会在 Safety Profiles 等提案上的立场。
- Tags: #language

(2026-08-18) [聊一聊商业产品背后的定价逻辑](202608/2026-08-18-%E8%81%8A%E4%B8%80%E8%81%8A%E5%95%86%E4%B8%9A%E4%BA%A7%E5%93%81%E8%83%8C%E5%90%8E%E7%9A%84%E5%AE%9A%E4%BB%B7%E9%80%BB%E8%BE%91.md)
- 会员制与订阅制利用使用强度差异，让低频用户补贴高频用户，实现整体盈利。AI 因成本更高需限额与分级。消费者判断是否值得付费，应看过去实际用量，并用回本次数计算盈亏平衡。
- Tags: #explained

(2026-08-17) [AI 时代我的开发工作流：从踩坑复盘到多项目并行验证](202608/2026-08-17-ai-%E6%97%B6%E4%BB%A3%E6%88%91%E7%9A%84%E5%BC%80%E5%8F%91%E5%B7%A5%E4%BD%9C%E6%B5%81%EF%BC%9A%E4%BB%8E%E8%B8%A9%E5%9D%91%E5%A4%8D%E7%9B%98%E5%88%B0%E5%A4%9A%E9%A1%B9%E7%9B%AE%E5%B9%B6%E8%A1%8C%E9%AA%8C%E8%AF%81.md)
- AI 时代作者从深度钻研转向多项目并行，通过 CLI 和 Skill 将踩坑会话自动沉淀为文章，并利用 LobeHub 的 acceptance skill 实现 UI 自动化验收，显著提升开发效率。
- Tags: #agent #workflow

(2026-08-17) [Elevators](202608/2026-08-17-elevators.md)
- 电梯调度算法远比想象复杂；简单 LOOK 在高流量时优于花哨的 RSR，目的地派梯因缺乏灵活性反而更慢，核心在于动态重优化与灵活性。

(2026-08-17) [My server is a phone now](202608/2026-08-17-my-server-is-a-phone-now.md)
- 作者用闲置的 CMF Phone 1 刷 Android + Termux + chroot 替代 VPS，通过 Ansible 管理、Cloudflare Tunnel 和 Tailscale 接入，跑 Surf 等个人服务，省钱又可复现。
- Tags: #setup #home

(2026-08-17) [Use Task Runners for Common Coding Tasks](202608/2026-08-17-use-task-runners-for-common-coding-tasks.md)
- 作者建议用任务运行器（bash 脚本、make、just、mise）统一跨仓库的构建、测试、格式化等常见命令，避免记忆各技术栈的不同命令，只需执行统一的 run build、make test 等。提供实现示例和优缺点。
- Tags: #efficiency

(2026-08-17) [Your Agentic Workflow's Cache Keepalive Costs 8x Too Much](202608/2026-08-17-your-agentic-workflow%27s-cache-keepalive-costs-8x-too-much.md)
- 常见的 30 秒缓存 keepalive 比最优贵约 8 倍。实测显示 Anthropic 最优约 4 分钟、OpenAI 约 8 分钟，超过 TTL 的 ping 会反复重建死缓存。只在暂停超过驱逐点、低于盈亏平衡点（约 46 分钟）时保温才省钱；DeepSeek、Gemini 只值延迟。
- Tags: #agent

## Monthly Archive

- [2026-08](202608/monthly-index.md) (18 entries)
- [2026-07](202607/monthly-index.md) (53 entries)
- [2026-06](202606/monthly-index.md) (68 entries)
- [2026-05](202605/monthly-index.md) (26 entries)
- [2026-04](202604/monthly-index.md) (44 entries)
- [2026-03](202603/monthly-index.md) (82 entries)

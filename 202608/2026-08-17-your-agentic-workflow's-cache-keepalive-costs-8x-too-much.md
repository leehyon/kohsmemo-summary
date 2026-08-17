# Your Agentic Workflow's Cache Keepalive Costs 8x Too Much
- URL: https://blog.mempko.com/your-agentic-workflows-cache-keepalive-costs-8x-too-much-v2-the-interval-frontier/
- Added: 2026-08-17 01:39:21
- Tags: #agent

## TL;DR
常见的 30 秒缓存 keepalive 比最优贵约 8 倍。实测显示 Anthropic 最优约 4 分钟、OpenAI 约 8 分钟，超过 TTL 的 ping 会反复重建死缓存。只在暂停超过驱逐点、低于盈亏平衡点（约 46 分钟）时保温才省钱；DeepSeek、Gemini 只值延迟。

## Summary
文章实测 Anthropic、OpenAI、Gemini、DeepSeek 的 prompt cache 保留曲线与 keepalive 成本，指出常见的 30 秒 ping 比最优设置贵约 8 倍。正确策略是只在“付费区间”内保温：等待时长超过驱逐点、低于盈亏平衡点，且 ping 间隔必须小于该厂商 TTL。

**逻辑脉络**
- 测量保留曲线：Anthropic 5-6 分钟断崖；DeepSeek 10 分钟；OpenAI 20 分钟仍半数存活、30 分钟全冷；Gemini 33-83% 随机，不算保留曲线。
- 成本算术：每次 ping 付约 0.1× 输入价，缓存穿透需付 1×（Anthropic 1.25×）；盈亏平衡 ≈ τ(w/r − 1)，Anthropic 约 46 分钟、OpenAI/DeepSeek 约 36 分钟、Gemini 约 12 分钟。
- 30 秒惯例在 10 分钟暂停时四个厂商都亏钱；4 分钟 ping 在 Anthropic 省 38%，在 OpenAI 等真正驱逐后也省钱（30 分钟暂停：Anthropic 1.56×、OpenAI 1.23×，DeepSeek 仅省延迟）。
- 间隔超过 TTL 会中毒：Anthropic 8 分钟 ping 每次都重建死缓存，成本变为不 ping 的 4 倍；OpenAI 8 分钟反而最优，省 2.45×。

**底层逻辑**
- 核心假设：缓存未命中成本是确定的，keepalive 只是用多次便宜读换取一次昂贵 prefill；存在盈亏平衡线。
- 方法论：用可自证计时的 harness 测量 idle 保留率与不同间隔成本，基于实测而非算术猜测。
- 对 commons 的预测：当所有客户端都 ping，LRU 失排序，厂商会转向按 token-hour 计费，套利有到期日。

**Takeaways**
- 最优间隔按厂商：Anthropic 约 4 分钟，OpenAI 约 8 分钟，Anthropic 1 小时档约 50 分钟；绝不要超过 TTL。
- 只保温可复用且受边界约束的暂停（工具调用、审批等待）；低于驱逐点不必 ping。
- 超过盈亏平衡（约 46 分钟，Anthropic 价格）就停止，让缓存死掉并接受 re-prefill。
- DeepSeek、Gemini 不值得为省钱保温，只买延迟。

# Which web frameworks are most token-efficient for AI agents
- URL: https://martinalderson.com/posts/which-web-frameworks-are-most-token-efficient-for-ai-agents/
- Added: 2026-03-17 14:40:27
- Tags: #agent

## TL;DR
研究测试 19 个 Web 框架，发现轻量级框架（如 Express、Flask）令牌效率显著高于全功能框架（如 Rails、Django），ASP.NET Minimal API 最省，Phoenix 最耗，但所有框架均能成功构建应用。

## Summary
核心主题：评估不同 Web 框架对 AI 代理的令牌效率

关键信息：
1. 研究方法：测试 19 个 Web 框架，使用 Claude Code w/ Opus 4.6 构建简单博客应用，比较令牌使用量
2. 框架分类：轻量级框架（如 Express、Flask）与全功能框架（如 Rails、Django）
3. 测试任务：初始构建博客应用，然后添加分类功能
4. 测试结果：所有框架均成功构建功能完整的博客应用

逻辑脉络：
1. 研究背景：AI 代理编写代码时代，框架比编程语言更重要
2. 实验设计：标准化提示，相同环境，比较令牌使用量和工具调用次数
3. 主要发现：
   - 轻量级框架令牌效率显著高于全功能框架
   - ASP.NET Minimal API 最省（26k 令牌），Phoenix 最耗（74k 令牌）
   - 全功能框架中 SvelteKit 和 Django 效率最佳
   - 添加功能时各框架成本差异不大
4. 结论：轻量级 API 框架对 AI 代理更高效，但所有框架都能成功构建应用
5. 实际意义：在频繁构建和修改代码的场景下，框架效率差异影响显著

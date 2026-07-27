# A Fireside Chat with Cat and Thariq from the Claude Code team
- URL: https://simonwillison.net/2026/Jul/21/cat-and-thariq/
- Added: 2026-07-27 01:49:50
- Tags: #podcast

## TL;DR
Anthropic Claude Code 团队分享编程代理演进、Claude Tag、系统提示优化和自动化代码审查，强调基于信任和评估的开发方法。

## Summary
The Claude Code team from Anthropic shared insights on how coding agents have transformed software engineering, emphasizing the shift from manual oversight to trust in automated systems, the rise of proactive collaboration via Claude Tag, and the importance of product taste over execution speed.

**底层逻辑**
- The team heavily dogfoods (ant foods) their products, using internal user retention as a gating metric before public release.
- Eval-driven development: systematic eval sets for models and behaviors ensure safe, effective agent behavior and catch regressions.
- Reducing system prompt size and hard constraints improves performance for frontier models; examples and "don't" instructions are often counterproductive.
- Tool design is an art: keep tool cardinality low and each tool's function distinct to avoid confusion.

**Takeaways**
- Claude Tag now lands 65% of product engineering PRs at Anthropic, acting as a proactive, multiplayer coding agent.
- The Claude Code system prompt reduced by 80% for models like Fable and Opus 4.8; removing examples and negative instructions improved results.
- Code review is increasingly automated: humans only for critical areas (e.g., system prompt); automated review catches 100% of issues in outer layers, with incidents used to update eval sets.
- Auto mode is key to enabling Claude Tag and reduces the need for manual approval; the team trusts it after extensive red-teaming.
- Thariq advocates for rewriting codebases (if you have good test suites) — a reversal of the old "never rewrite" mantra.

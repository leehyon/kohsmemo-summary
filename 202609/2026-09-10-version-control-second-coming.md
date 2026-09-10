# Version control second coming
- URL: https://psantosl.github.io/posts/version-control-second-coming/
- Added: 2026-09-10 09:13:35
- Tags: #engineering #product

## TL;DR
Pablo Santos 认为，AI 代理让版本控制迎来 2005 年以来最大变革：GitHub 统治松动，新 forge、Jujutsu、Diversion、Lore 等并起，焦点转向 AI 提交、超大仓库与 Git 之后。

## Summary
Pablo Santos 回顾版本控制二十年后再次爆发：AI 代理把提交速度推向新高度，同时 GitHub 的统治开始松动。他曾用 Plastic SCM 与 Git 竞争，如今在 Origin 优化 Git，并从挑战者、顾问与改造者多重视角判断：版本控制正从“如何适应 Git”转向“Git 之后是什么”。

**逻辑脉络**
- 2005 年 Git 发布并赢得 Linux 内核版本控制竞赛，GitHub 在 2008 年将其大众化，此后二十年问题都是如何应对 Git。
- 2025 年底 AI 代理写代码常态化，提交频率暴增，GitHub 性能遇瓶颈，新 forge 与协议集中涌现。
- 作者逐一介绍 Entire、Pierre、Origin、GitButler、ERSC/Jujutsu、Diversion、Oxen、Lore 等方向，指出三条主线：服务 AI 代理、超大仓库、云优先/非 Git。
- 未来竞争点：超大 monorepo、超快提交、虚拟文件系统、分布式 push/pull 的边界，胜者可能是产品也可能是范式。

**底层逻辑**
- 版本控制的需求由开发方式决定：手工编码时代 Git 与 GitHub 胜出，代理时代需要来源追踪、更高提交吞吐和自动协作。
- 架构受物理规模约束：仓库越大，本地克隆与 push/pull 越不适用，集中式或云优先工作区可能回归。
- 历史类比：SourceForge 被 GitHub 取代，Bitkeeper 被 Git 取代；当前同样处于旧王未倒、新王未立的过渡期。

**Takeaways**
- GitHub 仍巨大，但护城河正被 AI 提交洪流与新 forge 侵蚀。
- 新一波玩家分三类：Git 加速/forge（Entire、Pierre、Origin）、Git 替代或扩展（Jujutsu/ERSC、Diversion、Lore）、数据/客户端（Oxen、GitButler）。
- 来源追踪、stacked branches、一等冲突、虚拟文件系统、超快提交是关键技术方向。
- 大仓库与高提交率将迫使行业重新考虑分布式模型，或出现定制 Git 分叉。
- 作者结论：版本控制二十年冻结期结束，现在是从“如何应对 Git”转向“什么取代 Git”的最佳构建时刻。

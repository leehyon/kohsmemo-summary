# The Git Commands I Run Before Reading Any Code
- URL: https://piechowski.io/post/git-commands-before-reading-code/
- Added: 2026-07-10 05:37:47
- Tags: #best-practice

## TL;DR
通过五个 Git 命令快速诊断代码库：变更热点、Bus Factor、Bug 集群、提交趋势和危机模式，几分钟内揭示项目健康状态，指导后续代码阅读。

## Summary
在阅读任何代码之前，作者通过五个 Git 命令快速诊断代码库：识别变更热点、贡献者单一性（bus factor）、Bug 集群、提交趋势和紧急修复频率。这些命令基于提交历史，几分钟内即可揭示项目的健康状态和潜在风险。

**逻辑脉络**
- 变更热点：`git log --name-only` 列出过去一年变更最多的文件，高变更且无人愿维护的文件是最大风险。
- Bus Factor：`git shortlog` 识别贡献者分布，单一贡献者占比超 60% 需警惕；需关注近期活跃度。
- Bug 集群：`git log --grep` 搜索 bug 相关提交，定位高缺陷文件，与变更热点交叉确认高风险区域。
- 项目趋势：`git log --format='%ad'` 按月统计提交数，下降趋势或脉冲式变化反映团队活力或离职影响。
- 危机模式：`git log --oneline | grep revert/hotfix` 统计紧急修复频率，高频 revert 表明部署信任不足。

**Takeaways**
- 高变更文件不一定是坏代码，但结合 bug 集群可识别高风险代码。
- Bus factor 超过 60% 且关键人员已离开时，项目面临危机。
- 提交数量趋势比绝对值更重要，持续下降意味着团队失去动力。
- 频繁 revert/hotfix 揭示部署流程缺陷，需优先解决。
- 这些命令几分钟即可运行，能指导你优先阅读哪些文件。

# Neko Master: 从 0 到 1K+ Star 的 Vibe Coding 实践
- URL: https://luolei.org/neko-master-vibe-coding
- Added: 2026-03-03 03:04:17
- Tags: #agent #best-practice

## TL;DR
作者通过 Vibe Coding 快速开发 Neko Master 开源项目，结合多种 AI 工具实现高效迭代，展示 AI 在"从 0 到 1"中的价值，但"从 1 到 100"仍需人工判断。

## Summary
核心主题：Vibe Coding 实践与 Neko Master 项目开发经验

关键信息与逻辑脉络：

1. 项目概述
   - Neko Master 是一个开源、自部署的网络流量分析面板，支持多后端（OpenClash / Mihomo / Surge）
   - 项目原名 Clash Master，后更名为 Neko Master 以支持更多网关类型
   - 上线一周获得 1000+ GitHub Star，Docker Pull 破 10K
   - 主要功能：多维流量统计、趋势分析、Docker 一键部署、移动端适配 + PWA

2. 项目背景与动机
   - 作者作为 Homelab 用户，需要更直观的网络流量分析工具
   - 现有方案（如 Grafana）配置繁琐，界面不够直观美观
   - 希望解决的核心问题：了解流量去向、哪些域名吃带宽、节点负载情况、规则策略合理性

3. MVP 快速开发
   - 使用 Kimi K2.5 模型进行 Vibe Coding，一小时完成 MVP
   - 无需原型图和技术方案，直接与 AI 对话开发
   - 当晚上线第一版，24 小时内获得 400+ GitHub Star 和 1000+ Docker Pull

4. AI 审美设计
   - 通过视觉锚点提升 AI 生成的界面质量
   - 在 Dribbble / Figma Community 寻找参考设计，直接喂给 AI
   - 从"程序员风"进化到"SaaS 级"界面，审美判断仍是关键

5. AI 工具使用经验
   - Kimi K2.5：早期主力，中文理解好，适合 MVP 阶段
   - Claude Code (Opus 4.6)：适合架构和性能深水区问题
   - CodeX (GPT 5.2/5.3)：日常输出，开发过程稳定
   - Gemini 3 Pro：辅助 Review 和写 Commit Message
   - 国产模型在初始化阶段高效，深水区仍需高端模型

6. 快速迭代与用户反馈
   - 上线后两周迭代约 20 个版本（v1.0.2 到 v1.3.2）
   - AI 帮助快速响应用户反馈，修复 Bug 和优化性能
   - 用户看到快速迭代，提升信任感

7. 技术挑战与解决方案
   - 硬盘 I/O 优化：从单条写入到批量落盘、聚合写入、写入限流
   - ClickHouse 优化：批量写入窗口、时间分区、预聚合层
   - AI 在深水区的正确使用：日志与指标 -> 假设 -> patch -> 压测/对比 -> 继续迭代

8. Vibe Coding 的价值与局限
   - 降低了"从 0 到 1"的门槛，加速原型开发
   - "从 1 到 100"仍需经验、审美和用户需求理解
   - AI 可以生成代码，但稳定性边界和技术债优先级需人来判断

# Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl
- URL: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- Added: 2026-03-13 02:31:59
- Tags: #dev

## TL;DR
规范驱动开发 (SDD) 强调先编写规范再编码，分为三个层次。现有工具支持不同工作流，但仍面临灵活性不足、审查负担重等问题，需从历史教训中学习。

## Summary
核心主题：规范驱动开发 (SDD) 的概念、工具实现与挑战

关键信息与逻辑脉络：

1. SDD 定义与层次
   - SDD 是在编写代码前先编写 "spec"（规范），作为人和 AI 的真实来源
   - 三个实现层次：
     * Spec-first：先编写规范，用于 AI 辅助开发工作流
     * Spec-anchored：规范保留，用于功能和演进的维护
     * Spec-as-source：规范是主要源文件，只编辑规范不编辑代码

2. 规范 (Spec) 的定义
   - 结构化、行为导向的工件，用自然语言表达软件功能
   - 与更通用的上下文文档（内存库）不同，规范只与特定任务相关
   - 目前术语过载，最接近的定义是与 "产品需求文档" 比较

3. 三种 SDD 工具分析
   - Kiro：
     * 最轻量级，主要支持 spec-first
     * 工作流：需求 → 设计 → 任务
     * 包含 "steering"（内存库）概念
   - Spec-kit：
     * GitHub 的 SDD 实现，通过 CLI 创建工作空间
     * 工作流：宪法 → 指定 → 计划 → 任务
     * 包含宪法（内存库）和模板概念
     * 目前主要是 spec-first，而非 spec-anchored
   - Tessl Framework：
     * 唯一明确支持 spec-anchored 的工具，探索 spec-as-source
     * CLI 命令也作为 MCP 服务器
     * 规范与代码文件 1:1 映射，代码标记为 "// GENERATED FROM SPEC"

4. 观察与问题
   - 工作流程灵活性：当前工具不适合所有问题规模，缺乏灵活性
   - 文档审查负担：需要审查大量冗余的 markdown 文件，而非代码
   - 控制感问题：AI 可能忽略指令或过度执行，缺乏小迭代方法
   - 功能与技术规范分离：实践中难以明确区分
   - 目标用户不明确：不清楚 SDD 适合哪种规模和类型的问题
   - 历史教训：与模型驱动开发 (MDD) 相似，可能面临抽象级别和工具支持问题

5. 结论
   - Spec-first 原则在许多情况下有价值，但 SDD 术语尚未明确定义
   - 当前工具可能放大现有挑战，如审查过载和幻觉
   - 需要从过去的代码生成尝试中学习，避免重蹈覆辙

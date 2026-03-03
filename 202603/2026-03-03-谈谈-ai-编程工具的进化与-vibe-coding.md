# 谈谈 AI 编程工具的进化与 Vibe Coding
- URL: https://guangzhengli.com/blog/zh/vibe-coding-and-context-coding
- Added: 2026-03-03 05:18:15
- Tags: #vibe-coding #agent #advice

## TL;DR
AI 编程工具从 Copilot 到 Claude Code 不断进化，核心是上下文工程能力提升。作者区分 Context Coding 与 Vibe Coding，认为后者可能带来技术债务，但 AI 将改变编程生态，程序员需持续学习适应。

## Summary
核心主题：AI 编程工具的进化与 Vibe Coding 的思考

关键信息与逻辑脉络：

1.  AI 编程工具的演进历程
   *   GitHub Copilot：开创性代码补全功能，提供当前窗口代码上下文，但模型能力有限，上下文范围狭窄
   *   Cursor：引入 RAG 技术索引整个项目代码库，实现跨文件操作，支持直接编辑文件，结合 Claude 3.5 Sonnet 模型能力提升
   *   Claude Code：基于终端命令行的 AI 编程方式，采用 grep 等工具检索代码，全局视角分析项目，在大型任务中表现优异

2.  Context Coding 概念提出
   *   作者建议将基于 AI 辅助编程的方式称为 Context Coding（上下文编程）
   *   核心：AI 编程进步的关键在于上下文工程（Context Engineering）能力的提升
   *   目标：给大语言模型（LLM）传递更合适的上下文

3.  主流 AI 编程工具的上下文工程比较
   *   GitHub Copilot：提供当前窗口代码上下文，实现基本代码补全
   *   Cursor：使用 RAG 技术索引整个项目，支持语义搜索，提供更全面的代码上下文，支持直接 @ 文件/文件夹，索引 Git 历史记录
   *   Claude Code：基于 Unix 工具检索代码，全局视角分析项目，在复杂任务中表现更佳，但 tokens 消耗较大

4.  如何更好的 Context Coding
   *   提供项目基础上下文：技术栈、目录结构、文件功能说明
   *   使用指令文件（如 .github/copilot-instructions.md、.rulers、CLAUDE.md）存储项目信息
   *   要求 LLM 遵循成熟开发思路：渐进式修改、小步提交、从现有代码学习
   *   提供开发常用工具和调试技巧的上下文

5.  Vibe Coding 的定义与争议
   *   原始定义（Andrej Karpathy）：忘记代码存在，几乎不手动参与编程，不 review AI 写的代码，仅看结果
   *   现状：所有通过 AI 辅助和编写代码的方式都被称为 Vibe Coding
   *   作者观点：应区分 Vibe Coding 和 Context Coding，两者本质不同

6.  对 Vibe Coding 的批判与思考
   *   短期：引入缺陷和安全漏洞
   *   长期：导致代码难以维护，技术债务堆积，系统可理解性和稳定性降低
   *   案例：Leo 使用 Vibe Coding 开发产品，因技术问题导致产品关闭
   *   本质：Vibe Coding 革命了编程行业，可能蚕食和挤压一般程序员的生存空间

7.  个人观点与未来展望
   *   没有单一工具能解决所有编程问题，工程师应根据需求选择合适工具
   *   LLM 改变了编程习惯：减少枯燥工作、调试方式改变、一次性代码生成
   *   未来趋势：水平一般的程序员数量减少，独立开发和小规模团队协作成为主流
   *   建议：持续学习和实践，保持学习能力的程序员不会被替代

# AI Coding：從「Vibe Coding」到專業開發
- URL: https://techblog.lycorp.co.jp/zh-hant/20250626a
- Added: 2026-03-03 03:16:36
- Tags: #vibe-coding #advice

## TL;DR
从 "Vibe Coding" 到 AI 专业开发，需平衡速度与质量，建立结构化流程与心态。开发者将转变为 AI 协调者，通过管理 AI 舰队与流程，而非个人编码能力，实现高效协作。

## Summary
核心主题：从 "Vibe Coding" 到 AI 专业开发的转型，强调在 AI 辅助开发中平衡速度与质量，建立结构化流程与心态。

关键信息与逻辑脉络：

1.  "Vibe Coding" 的定义与风险
    *   定义：仅凭几行 prompt 快速生成 prototype，缺乏对 AI 输出内容的检查。
    *   优势：能快速产出原型，效率提升（据 Steve Yegge 称比传统编码快 5 倍）。
    *   风险：导致技术债务、bug、安全漏洞（CSET 报告指出近半数 AI 生成代码含 bug 或漏洞）、代码库结构松散，难以维护和扩展。

2.  AI 专业开发的核心理念
    *   两大核心心态：
        *   Trust the Process（相信流程）：在明确的流程中 AI 才能发挥最大效力，为 AI 提供 "地图"。
        *   AI as Teammate（AI 是队友）：AI 是同事而非替身，需持续评估、调整其输出。
    *   未来角色：开发者将转变为 "AI orchestrator"（AI 协调者），负责协调 AI、设计系统、确保品质。

3.  从 "Vibe Coding" 到专业开发的 8 个实战做法（按软件开发四阶段分类）
    *   Preparation（事前准备）
        *   Practice 1: 多 AI 工具协作：建立不同 AI 各司其职的 pipeline（如推理 AI、搜索 AI、编码 AI），团队合作优于单打独斗。
        *   Practice 2: 详细需求准备：将需求视为 AI 的导航图，与 AI 进行类似同事的对话，明确定义目标。
    *   Planning（计划）
        *   Practice 3: AI-friendly 任务切分：将任务分解为小而独立（100-200 行）、输入输出明确、依赖性低、有测试用例的单元。
        *   Practice 4: 制定 Implementation Rule：为 AI 创建 "内部手册"，定义编码风格、推荐模式和工作流程。
    *   Development（开发）
        *   Practice 5: Edit-Test 迴圈：采用 15-30 分钟短循环，包括设定目标、编写失败测试、请求 AI 实现代码、AI 自动测试、分析修正或人工 review 后 commit。
        *   Practice 6: Context 管理：通过 @ 加入文件、对话超限开新 chat、同步代码库、Git commit 作为 checkpoint、会话结束写小结等方式管理 AI 的 "记忆"。
    *   Troubleshooting（排解问题）
        *   Practice 7: Problem Report System：当 AI 遇到瓶颈时，让其生成包含状态、错误信息、已尝试解法的报告，交由其他 AI 获取新思路。
        *   Practice 8: Context Reset 策略：当 AI 输出混乱或陷入循环时，通过整理进度生成 Problem Report，用干净的 context 重新开始。

4.  结论与展望
    *   与 AI 协作如同管理团队：需明确各 AI 成员的职责与 input/output，对产出进行严格把关。
    *   成功关键：管理团队与流程的能力，而非个人编码能力。
    *   未来趋势：开发者将向 "agent fleets（AI 舰队）" 管理者转型，拥抱 AI 的开发者将领先于排斥 AI 的开发者。

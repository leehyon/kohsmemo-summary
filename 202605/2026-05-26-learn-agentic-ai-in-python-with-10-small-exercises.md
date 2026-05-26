# Learn agentic AI in Python with 10 small exercises
- URL: https://belderbos.dev/blog/learn-agentic-ai-python-10-step-journey/
- Added: 2026-05-26 09:54:45
- Tags: #agent #education

## TL;DR
本文强调深入理解 Agentic AI 底层逻辑，通过 10 个练习从零构建具备状态管理、工具调用及人工干预机制的生产级 Agent。

## Summary
### 核心主题
强调在掌握高层框架之前，深入理解 Agentic AI 底层实现逻辑的重要性。通过 10 个小型练习，引导开发者从零构建具备状态管理、工具调用、可测试架构及人工干预机制的生产级 Agent，从而具备在抽象层失效时的调试与维护能力。

### 逻辑脉络
文章将构建智能 Agent 的过程拆解为 7 个递进阶段，从基础的单次模型调用演进为通用的自动化循环：
1.  **基础交互**：实现模型调用与响应解析。
2.  **结构化约束**：确保模型输出符合机器可读格式。
3.  **记忆机制**：通过历史记录维持上下文状态。
4.  **工具能力**：引入循环机制赋予模型执行外部操作的能力。
5.  **架构优化**：通过设计模式解耦依赖，提升可测试性。
6.  **人机协同**：基于置信度阈值引入人工确认环节。
7.  **通用抽象**：将工具调用泛化，揭示主流框架的底层本质。

### 关键信息

*   **Stage 1: 获取模型回复 (Exercise 1)**
    核心代码仅需 3 步：构建 Client、调用 API、解析 `content[0].text`。理解 `content` 返回的是列表结构至关重要，这是后续无缝集成工具调用的基础。

*   **Stage 2: 机器可读化输出 (Exercises 2, 3)**
    解决 LLM 输出不可靠的问题。方法是将 System Prompt 视为 API 契约（强制 JSON 格式、禁止额外内容），并使用 Pydantic 模型对返回数据进行验证。

*   **Stage 3: 实现记忆功能 (Exercise 4)**
    LLM 本身是无状态的。应用层需自行维护 `history` 列表，在每次请求时发送完整的对话历史，从而模拟出连续的对话体验。

*   **Stage 4: 赋予操作能力 (Exercise 5)**
    实现 Tool Use 循环：模型请求工具 -> 代码执行工具 -> 将工具结果包装为 `user` 消息 -> 再次请求模型。需注意追加完整的 `response.content` 而非仅文本内容。

*   **Stage 5: 解耦与测试 (Exercises 6, 7, 8)**
    摆脱业务逻辑与外部依赖（如 `anthropic`, `sqlite3`）的强耦合。引入 Protocol 用于模拟 Provider，Repository 模式抽象数据层，Service 层负责编排，构建清晰的四层架构。

*   **Stage 6: 人工介入 (Exercise 9)**
    利用模型输出的置信度 决定执行路径。高于阈值自动执行，低于阈值则请求用户确认。这种机制是区分“Demo”与“生产级工作流”的关键。

*   **Stage 7: 通用化循环 (Exercise 10)**
    将具体的工具函数调用替换为字典查找 (`TOOL_FUNCTIONS[name]`)。此模式与 LangChain 等框架的底层逻辑一致，证明了 Agent 本质上是一个通用的循环加上特定的工具注册表。

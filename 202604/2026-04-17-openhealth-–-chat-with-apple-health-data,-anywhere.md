# OpenHealth – Chat with Apple Health Data, Anywhere
- URL: https://jonno.nz/posts/openhealth-chat-with-apple-health-data/
- Added: 2026-04-17 02:47:48
- Tags: #life #setup

## TL;DR
OpenHealth 开源工具将 Apple Health 数据转为 LLM 可读格式。支持本地解析以保护隐私，提供 Web App 与 CLI。用户能利用真实数据获取个性化 AI 建议，打破地理限制。

## Summary
**核心主题**
OpenHealth —— 一个将 Apple Health 导出数据转换为 LLM 可读 Markdown 格式的开源工具，旨在解决地理限制、数据隐私及用户控制权问题，实现健康数据与 AI 的无障碍交互。

**关键信息与逻辑脉络**

1.  **背景与动机**
    *   现有主流 AI (如 ChatGPT, Claude) 的 Apple Health 连接器仅限美国地区使用，且用户无法控制数据解析方式及模型选择。
    *   作者希望自主处理数百万条健康数据点（心率、睡眠、运动等），并将其转化为任何 LLM 都能理解的上下文，以获取基于真实数据的个性化建议。

2.  **产品形态与交付方式**
    *   **静态 Web App**：纯浏览器本地运行，无后端服务器。用户拖入 `export.zip`，解析完成后下载 Markdown 文件，数据不上传。
    *   **CLI 工具**：基于 Bun 编译的单文件二进制工具，零依赖。支持本地解析、输出文件及一键打包复制到剪贴板。
    *   **WebRTC 传输**：通过扫描二维码，利用 DataChannel 在 iPhone 和桌面浏览器之间建立点对点直连传输，后端仅负责握手信令，不触碰文件数据。

3.  **技术实现原理**
    *   **流式解析**：针对 Apple Health 巨大的 `export.xml` (可达 4GB)，采用流式 SAX 解析器 (`saxes`) 逐行处理，避免内存溢出 (OOM)，并保持主线程流畅。
    *   **数据清洗与聚合**：支持多设备数据源（Apple Watch, Withings, MyFitnessPal 等），并根据可信度进行数据去重与优选。
    *   **TDD 开发**：核心解析逻辑包含 85 个测试，确保输出格式的一致性。

4.  **输出结构 (七份文件)**
    *   工具将原始数据转换为七个针对 LLM 优化的 Markdown 文件：
    *   `health_profile.md` (基础画像与长期平均值)
    *   `weekly_summary.md` (本周数据及四周滚动对比)
    *   `workouts.md` (近四周详细运动记录)
    *   `body_composition.md` (体重与营养趋势)
    *   `sleep_recovery.md` (睡眠阶段与 HRV 趋势)
    *   `cardio_fitness.md` (跑步与心率区间分布)
    *   `prompt.md` (预设的系统提示词，用于指导 LLM 理解上述数据)

5.  **应用价值**
    *   **精准洞察**：LLM 基于真实历史数据提供训练建议（如恢复不足预警），而非通用鸡汤。
    *   **数据整合**：自动整合来自不同设备的碎片化数据，形成统一视图。

6.  **隐私与使用策略**
    *   **数据主权**：解析过程完全本地化，OpenHealth 本身不收集数据。
    *   **灵活接入**：用户可选择将输出结果粘贴给云端 AI (如 ChatGPT/Claude)，或通过管道 (pipe) 输入给本地模型 (如 Ollama, llama.cpp)，确保健康数据不离设备。

# I built a private ChatGPT for my family
- URL: https://fulghum.io/family-chatgpt
- Added: 2026-07-02 06:19:13
- Tags: #home #setup

## TL;DR
作者用 ZimaBoard 2 和 RTX 5060 Ti 搭建了本地私有 ChatGPT，基于家庭文档库，通过 Open WebUI 提供类 ChatGPT 界面，并自定义系统提示词以符合家庭价值观，实现隐私、可控的家庭 AI 助手。

## Summary
文章讲述了作者为家庭搭建了一个私有 ChatGPT 系统，使用本地 LLM、家庭文档库和小型主机加外置 GPU 的硬件组合，旨在提供隐私保护、可控且基于家庭上下文的人工智能助手。

**逻辑脉络**
- 作者想要一个像 ChatGPT 那样简单易用的家庭 AI，但必须私有、基于家庭文档，并体现家庭价值观。
- 硬件：ZimaBoard 2 + 外接 RTX 5060 Ti GPU，运行 ZimaOS。
- 软件栈：llama.cpp、Gemma 4 12B、Open WebUI（仿 ChatGPT 界面）、Kokoro（语音合成）、ComfyUI（图像生成）、Tailscale（私有网络）。
- 家庭 vault：NAS 目录存放历史、财务、健康等文档，通过向量数据库实现 RAG 查询。
- 隐私与可控：完全在家庭网络内（Tailscale），无公网暴露；系统提示词可自定义，反映家庭价值观（如直接、冷静、尊重预算、帮助推理而非直接给答案）。
- 可行性：现在技术门槛已降低，适合家庭中懂技术的成员。

**底层逻辑**
- 作者认为 AI 助手应体现家庭特有的价值观和原则，而非依赖大公司的通用默认设置。
- 私有部署比依赖公有云更符合家庭隐私需求，同时系统提示词本身就是一次对家庭价值观的反思。
- 最好的家庭技术是“像家里的一个有用物品”，而非复杂的基础设施。

**Takeaways**
- 使用 Open WebUI 模拟 ChatGPT 界面，对非技术家庭成员友好。
- 家庭 vault 让 AI 能回答“我们家的特定问题”，如医疗记录对比、学校通知解读。
- 通过自定义系统提示词让 AI 的行为符合家庭价值观（例如：帮助推理而非直接给答案、不优化时长、直接说明权衡）。
- 硬件选择：ZimaBoard 2 + 外接 GPU 性价比高，但需要容忍配置过程中的小问题。
- 整个系统通过 Tailscale 私有访问，无需暴露到公网，提升安全性。

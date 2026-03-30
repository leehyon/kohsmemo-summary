# 用 iMessage 串接 Claude Code
- URL: https://raymondhouch.com/lifehacker/digital-workflow/imessage-claude-code-ai-assistant/
- Added: 2026-03-30 02:22:54
- Tags: #life #setup

## TL;DR
本文介绍利用 Claude Code 的 iMessage 插件在 Mac 上搭建 AI 助理。通过设置触发词与群组权限，让家人在 iMessage 中直接调用 AI，无需额外 App，并分享了长期运行与避坑指南。

## Summary
*   **核心主题**：利用 Claude Code 的 iMessage 插件，在 Mac 上建立 AI 助理，让家人无需额外 App 即可在 iMessage 群组中通过触发词调用 AI 服务。

*   **背景与动机**：
    *   解决 Discord Bot 无法覆盖家人（仅使用 iMessage）的场景。
    *   目标是降低 AI 使用门槛，使其融入常用通讯工具。

*   **前提条件**：
    *   Mac 电脑（运行 Messages.app）。
    *   Claude Code Max 订阅（使用 `--channels` 功能）。
    *   24 小时运行的 Mac 主机（如 Mac mini）。

*   **实施步骤**：
    1.  **安装插件**：手动启用 `imessage@claude-plugins-official`。
    2.  **配置触发规则**：
        *   创建 `access.json`。
        *   设置 `dmPolicy` 为 `allowlist` 并置空，禁止私訊干扰。
        *   指定 `groups` 和 `chatId`，仅在特定群组生效。
        *   设定 `requireMention` 和 `mentionPatterns`（如“雷小蒙”），使用触发词唤醒。
        *   配置 `ackMessage`（如“收到任務...”），作为即时反馈。
    3.  **启动服务**：使用 `--channels` 和 `--allowedTools` 参数启动 Claude Code。
    4.  **长期运行**：编写启动脚本，并通过 `osascript` 解决 SSH 环境下的 GUI context 问题。

*   **关键决策与避坑指南**：
    *   **为何用群组而非私訊**：iMessage 无独立 Bot 帐号，私訊会导致 AI 回复所有对话；群组 + 触发词可实现隔离。
    *   **Watermark 机制**：仅处理启动后的新訊息，重启期间的消息会被忽略。
    *   **性能问题**：聊天记录过多（如 3800+）会导致 AppleScript 逾时，需重启 Messages.app 重建索引。
    *   **自我触发限制**：原版忽略自己的消息，需修改 `server.ts` 才能让自己在群组中触发 AI。
    *   **身份显示**：AI 回复通过你的 Apple ID 发送，尾部带签名以示区别。

*   **意外收获**：
    *   iMessage 插件的 persistent session 架构启发了 Discord Bot 的升级。
    *   将 Discord Bot 从 subprocess 模式（25% cache）升级为 persistent session 模式（84% cache），显著提升效能。

*   **应用场景与限制**：
    *   **场景**：查询食譜、天气、旅行规划，或在无电脑时通过手机操作个人 AI 助理。
    *   **限制**：仅限 Mac 环境、需主机保持开机、重启会重置 watermark、隐私上无独立帐号隔离。

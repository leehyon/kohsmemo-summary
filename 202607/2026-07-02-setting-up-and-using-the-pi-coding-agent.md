# Setting Up and Using the Pi Coding Agent
- URL: https://deepakness.com/blog/pi-agent-setup/
- Added: 2026-07-02 06:19:58
- Tags: #agent #setup

## TL;DR
Pi 是一个开源终端编码代理，核心最小化，通过扩展按需添加功能。作者用它做侧项目，搭配 DeepSeek 等模型，速度飞快且成本极低。本文详细介绍了安装、配置、包管理及使用技巧。

## Summary
本文介绍了作者如何设置和使用开源终端编码代理 Pi，包括安装、配置提供商（DeepSeek）、安装关键扩展包以及项目指令文件等，并总结了使用体验和心得体会。

**逻辑脉络**：
- 先介绍 Pi 是什么：开源终端编码代理，核心小巧，通过扩展和包添加功能。
- 然后讲述作者的使用场景：主项目用 Cursor 和 Codex，侧项目用 Pi。
- 接着详细说明安装和设置 DeepSeek 提供商的过程。
- 列举安装的五个主要包：pi-web-access（网络搜索）、pi-codex-goal（目标跟踪）、pi-vision-proxy（图像代理）、pi-agent-browser-native（浏览器操作）、pi-cursor-sdk（使用 Cursor 订阅）。
- 解释 AGENTS.md 和 APPEND_SYSTEM.md 的用途和自定义内容。
- 介绍常用快捷键和命令。
- 最后总结喜欢 Pi 的原因和当前完整的设置清单。

**底层逻辑**：Pi 的设计哲学是保持核心最小化，通过可选的扩展和包按需添加功能，让用户拥有完全的控制权，同时保持终端的快速和轻量。

**Takeaways**：
- Pi 适合侧项目和实验，速度快、成本低（搭配 DeepSeek 等便宜模型）。
- 通过安装包可实现网页搜索、目标跟踪、图像代理、浏览器操作等功能，且可复用现有 Cursor 订阅。
- 使用 AGENTS.md 和 APPEND_SYSTEM.md 可以精细控制项目上下文和全局行为规则。
- Pi 的会话树功能允许分支和回溯，便于尝试不同方案。
- 当前推荐设置包括：DeepSeek v4 Pro（默认）、DeepSeek v4 Flash（轻任务）、Kimi K2.6/K2.7 Code（备选）、5 个包、自定义全局规则和最小化页脚。

# How I manage Images for my Blog
- URL: https://blog.lysk.tech/excalidraw-frame-export/
- Added: 2026-03-31 05:28:19
- Tags: #blog #setup

## TL;DR
作者为解决手动导出 Excalidraw 配图效率低的问题，通过 Fork VSCode 扩展，实现了监听文件变化并自动导出双主题 SVG 图片的功能，达成本地实时预览，显著提升了写作体验。

## Summary
**核心主题**：博客图片管理流程的自动化

**关键信息**：
*   **背景**：作者使用 Excalidraw 绘制博客配图，但手动导出适配浅色和深色模式的图片操作繁琐（需 9 次点击，耗时约 45 秒），严重影响写作效率。
*   **解决方案**：通过自动化工具，自动将 Excalidraw 中的特定 frame 导出为支持双主题的 SVG 文件。
*   **最终成果**：Fork 了 Excalidraw 的 VSCode 扩展，实现了本地实时监听文件变化并自动导出图片的功能。

**逻辑脉络**：
1.  **问题定义**：描述了在写作过程中频繁手动导出图片的痛点，包括重复选择、命名和切换模式的枯燥过程。
2.  **初步尝试（GitHub Action）**：
    *   利用 `excalirender` 等开源工具编写 GitHub Action。
    *   逻辑：监听 `.excalidraw` 文件变更，解析其中的 frame 元素，自动导出并提交 SVG 文件。
    *   **局限性**：依赖的库存在渲染 Bug；无法在 ARM 架构的 Mac 上本地运行（Docker 兼容性问题），导致本地预览必须依赖远程 CI 流程，无法实时看到更新。
3.  **最终方案（VSCode 扩展定制）**：
    *   构思：在 VSCode 扩展中增加自动导出功能，解决本地预览问题。
    *   **实现机制**：Fork 官方扩展，修改代码以监听当前打开的 `.excalidraw` 文件。识别以 `export_` 前缀命名的 frame，自动将其导出为 light 和 dark 两个版本的 SVG 文件并存放在同级目录。
4.  **成效与结论**：
    *   实现了本地实时预览，任何图修改都会立即反映在博客草稿中，极大提升了写作体验。
    *   作者已将定制的扩展发布在 GitHub 的 Release 页面供他人使用，暂未计划向官方仓库提交 PR。

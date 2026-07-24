# Git exclude, a handy feature you might not know about
- URL: http://marijkeluttekes.dev/blog/articles/2025/09/03/git-exclude-a-handy-feature-you-might-not-know-about/
- Added: 2026-07-24 02:04:23
- Tags: #guide

## TL;DR
Git exclude 是位于 .git/info/exclude 的忽略文件，语法同 ignore，但不被跟踪，适合存储个人或临时文件。文章对比了三类忽略机制的使用场景与建议。

## Summary
**总述**：Git 的 exclude 功能与 ignore 语法相同，但文件位置不同且不被 Git 跟踪，适用于个人或临时文件。文章详细对比两者差异，并给出使用建议。

**逻辑脉络**：
- 首先介绍 exclude 的概念，与 ignore 语法一致，但文件位于 `.git/info/exclude`，可能需手动创建。
- 解释核心差异：ignore 文件可分散在仓库中，被 Git 跟踪；exclude 仅一个、位于 `.git` 目录、不被跟踪，仅对本地仓库有效。
- 列举 exclude 的常见用途：个人脚本、临时代码、Docker Compose 覆盖等。
- 补充全局 gitignore 文件的用法与注意事项。
- 最后给出选择建议：优先使用项目 ignore 文件，其次根据场景选择 exclude 或全局 ignore。

**Takeaways**：
- exclude 与 ignore 语法相同，但文件位置在 `.git/info/exclude`，不被 Git 跟踪。
- exclude 仅对当前仓库的当前克隆有效，适合存放个人或临时文件。
- 使用顺序建议：项目 ignore > exclude > 全局 ignore。
- 全局 ignore 慎用，避免团队间遗漏文件。
- 可搭配 direnv 等工具提高 exclude 文件的可见性。

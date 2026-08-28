# Parallel development without the headaches using Git worktree
- URL: https://barrd.dev/article/parallel-development-without-the-headaches-using-git-worktree/
- Added: 2026-08-28 08:42:52
- Tags: #dev #setup

## TL;DR
Git worktree 可在同一仓库为各分支创建独立目录，并行开发无需 stash 或 checkout，用 add、list、remove、prune 管理。

## Summary
这篇文章介绍了 Git worktree 功能，通过为每个分支创建独立的目录，让开发者可以同时处理多个任务而无需反复 checkout 与 stash。作者以真实场景演示了 worktree 的创建、合并、清理流程，并认为它显著减少了上下文切换。

**逻辑脉络**
- 从传统分支切换的痛点出发，引出 worktree 如何实现并行工作区。
- 给出核心命令：git worktree add -b new-branch ../dir 创建新分支，或 git worktree add ../dir existing-branch 关联已有分支。
- 以一个同时开发功能与修复生产 bug 的例子，展示工作目录独立后的操作：热修在 hotfix worktree 进行，功能继续在 feature worktree 迭代，main 保持干净用于合并。
- 合并时只需从主工作目录执行 git merge feature-branch，目录隔离降低误提交风险。
- 管理命令：git worktree list 查看，git worktree remove 删除（可用 --force），git worktree prune --expire 清理废弃元数据。

**底层逻辑**
- 核心假设是多个工作目录共享同一仓库的 .git 对象库，但各自拥有独立的工作区状态。
- 每棵 worktree 必须绑定唯一分支，从而建立“一任务、一分支、一目录”的清晰映射，减少认知负担。

**Takeaways**
- 并行开发时用 git worktree add -b feature/foo ../foo 快速创建分支工作区。
- 紧急热修时，在 main 目录下为 hotfix 单独建 worktree，避免打断当前功能。
- 合并前先提交各自分支，再回主目录执行 git merge branch-name。
- 删除 worktree 前确保工作区干净，git worktree remove 不会删除分支本身。
- 手动删除目录后运行 git worktree prune --expire 7.days.ago 清理记录。

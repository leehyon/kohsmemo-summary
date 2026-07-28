# You probably don't need Oh My Zsh
- URL: https://rushter.com/blog/zsh-shell/
- Added: 2026-07-28 09:32:07
- Tags: #setup

## TL;DR
放弃 Oh My Zsh，它因脚本臃肿导致启动慢。改用最小 Zsh 配置 + starship + fzf，启动时间可从 0.38 秒降至 0.07 秒。

## Summary
Oh My Zsh 因脚本臃肿导致启动缓慢，作者实测默认配置耗时 0.38 秒，建议放弃 OMZ，转而采用最小配置 + 轻量工具，将启动时间降至 0.07 秒。

**逻辑脉络**
- 指出 OMZ 被广泛推荐，但其 shell 脚本解释导致每次打开新标签页都需加载大量代码，启动慢。
- 通过计时对比展示默认配置（含 git、zsh-autosuggestions 等插件）的耗时。
- 提出最小 Zsh 配置方案（仅 history、autocd、compinit），并推荐使用 starship 替代 OMZ 的主题和插件，用 fzf 替代 zsh-autosuggestions 进行历史搜索。
- 最终配置启动时间仅 0.07 秒，并给出启用 Vim 模式等额外建议。

**Takeaways**
- OMZ 的主要问题是启动慢：默认配置 0.38 秒，加上 git 和虚拟环境插件会更慢。
- 最小配置只需几行：`HISTSIZE`、`SAVEHIST`、`EXTENDED_HISTORY`、`autocd`、`compinit`。
- 用 starship 替换 OMZ 的提示和主题：一个二进制文件即可处理 git、语言版本等信息，且启动更快。
- 用 fzf + Ctrl+R 代替 zsh-autosuggestions，避免输入时出现干扰性的自动建议。
- 启用 Vim 模式（`set -o vi`）可加速命令行编辑，适合 Vim 用户。

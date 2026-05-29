# It's time to talk about my writerdeck
- URL: https://veronicaexplains.net/my-first-writerdeck/
- Added: 2026-05-29 03:26:26
- Tags: #writing #home

## TL;DR
作者将闲置笔记本改造为 writerdeck，通过 Debian 纯 tty 环境、neovim、tmux 和 syncthing 隔离网络干扰，实现高效专注的写作体验，强调技术的有意选择。

## Summary
作者将一台旧笔记本改造为专用写作设备（writerdeck），通过 Debian 系统纯 tty 环境、neovim、tmux 及 syncthing 等工具，完全隔离网络干扰，实现高效、专注的写作体验。

- **动机与设备选择**：因注意力问题，将闲置六年的 System76 Galago Pro 笔记本（键盘优秀、磨砂屏、Linux 友好）改造为 writerdeck，避免现代互联网的干扰。

- **系统安装**：选用 Debian Trixie 纯终端模式（无 x11/Wayland），跳过全盘加密（内容均为公开），通过留空 root 密码启用 sudo 用户，安装时去除桌面环境（仅保留 tty）。

- **网络管理**：安装 network-manager 包，使用 nm-tui 连接 Wi-Fi（大部分时间保持离线，仅在需要备份时联网）。

- **编辑器与终端**：安装 neovim 替代默认 nano，并从 backports 安装 kmscon（支持 Ctrl+/- 缩放字号）。

- **tmux 增强**：安装 tmux 实现终端分屏与状态栏，配置电池百分比（通过 acpi -b 配合 grep）、亮度控制（通过 light 绑定 F8/F9），并将状态栏置于顶部、背景色设为绿色。

- **写作环境**：neovim 中设置 colorscheme blue 和自动换行 (set linebreak)，安装 vimwiki（通过 apt 安装 vim-vimwiki）管理写作笔记。

- **远程同步**：安装 syncthing，将 writerdeck 的 vimwiki 文件夹与服务器写作文件夹单向同步（避免私密笔记泄露），并调整监听地址为全地址（因无图形浏览器），后续计划用 SOCKS 代理改进安全性。

- **自动登录与启动**：通过 systemd 编辑 kmscon 服务实现无密码自动登录，并在 .bashrc 中判断主 tty 后自动启动 tmux 并加载 vimwiki 索引页。

- **使用体验**：经过一周使用，成功完成多篇稿件，认为 writerdeck 通过物理隔离浏览器、无桌面干扰，帮助回归专注写作，强调技术选择应有意向性——设备只做一件事，做完即放下。

# What I Self-Host
- URL: https://viceconsole.fyi/blog/2026/10/10/what-i-self-host/
- Added: 2026-10-23 01:37:54
- Tags: #home #setup

## TL;DR
作者用 Beelink N100 迷你主机自托管 28 个服务，坚持不暴露公网、优先原生、Podman 替代 Docker，以简单运维替代云服务与流媒体。

## Summary
作者回顾多年自托管经历：从大学床底的 Linux、MythTV/XBMC，到如今用 Jellyfin 替代流媒体，并扩展到预算、照片、监控、密码、待办等 28 个服务。核心不是追求全自托管，而是用有限硬件和简单运维换回对内容、升级节奏与家庭数字生活的控制。

**底层逻辑**
- 除路由器上的 VPN，不把服务暴露公网；IPv4 受 CGNAT 限制，VPN 主要走 IPv6。
- 优先原生单二进制，复杂依赖才容器化；不用 Docker，改用 Podman 与 systemd 集成。
- 硬件为 Beelink S12 Pro（N100、16GB RAM、512GB SSD）+ 6TB 硬盘，靠 720p 媒体、低分辨率摄像头等控制资源。

**Takeaways**
- 服务覆盖媒体、照片、备份、监控、家庭自动化、音频、密码与任务管理等。
- 对 *arr 栈、Collabora、Firefly III、OwnTracks、Music Assistant、自建邮箱等明确说不，理由是资源重、复杂、收益低或已有方案。
- 最终 17 个原生 + 11 个 Podman 服务由 systemd 管理，内存约 7.5GB，CPU 30%-40%，说明小型 Mini PC 可承载大量非 AI 服务。

# My server is a phone now
- URL: https://seg6.space/posts/phone-server/
- Added: 2026-08-17 01:42:49
- Tags: #setup #home

## TL;DR
作者用闲置的 CMF Phone 1 刷 Android + Termux + chroot 替代 VPS，通过 Ansible 管理、Cloudflare Tunnel 和 Tailscale 接入，跑 Surf 等个人服务，省钱又可复现。

## Summary
本文记录作者用 CMF Phone 1 替代 Hetzner VPS 的完整过程。先尝试 postmarketOS 失败，后保留 Android，用 Termux 做宿主，再通过 root + chroot 跑常规 Linux 应用。目前这台手机稳定运行 Surf、记账、屏幕分享等个人服务，并通过 Cloudflare Tunnel 和 Tailscale 实现网络接入。

**逻辑脉络**
- 最初用 VPS 跑服务，因 Surf 浏览器负载和 DRAM 涨价决定换机器。
- 尝试刷 postmarketOS，但 Wi-Fi、蓝牙等驱动不完善，设备变砖后恢复，结论是 Android 已有完整驱动。
- 改用 Termux 做宿主，用 PRoot 运行 Linux 镜像，服务正常但 Surf 性能差。
- 决定 root，改用 chroot 加载同一 Debian 文件系统，性能显著提升，所有容器迁移到 chroot。
- 将主机纳入 Ansible 管理：版本化部署、原子切换、健康检查。
- 入站用 Cloudflare Tunnel 和 Tailscale，解决家庭网络与漫游问题。

**底层逻辑**
- 不替换 Android，而是让 Android 做硬件适配，Termux 做控制面，Linux 应用保留自己的文件系统。
- PRoot/chroot 只是兼容环境，不是安全边界；共享内核和网络，需默认信任。
- 可复现性和恢复能力优先：配置在 Git，密钥由 1Password 签名派生，设备丢失可重建。

**Takeaways**
- Android + Termux + root chroot 能稳定跑个人服务，硬件驱动省心。
- 性能敏感应用不要用 PRoot，chroot 接近原生。
- 用 Ansible 管理，部署可回滚、设备可替换。
- 用 Cloudflare Tunnel 做 HTTP 入站，Tailscale 做管理，无需开放端口。
- 不要把 chroot 当安全隔离，重要数据必须自动备份到设备外。

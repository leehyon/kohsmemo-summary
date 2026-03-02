# Personal Infrastructure Setup 2026
- URL: https://linderud.dev/blog/personal-infrastructure-setup-2026/
- Added: 2026-03-02 07:49:33
- Tags: #home #setup

## TL;DR
作者分享其 2026 年个人基础设施架构，使用 Incus 容器化和 OpenTofu 基础设施即代码，通过 Wireguard 和 Nginx 暴露服务，实现自托管邮件、博客等服务。

## Summary
核心主题：作者分享其 2026 年个人基础设施的设置与架构，重点介绍了自托管服务的实现方法、工具选择和网络架构。

关键信息与逻辑脉络：

1. 个人基础设施概述
   - 作者维护个人基础设施已超过十年
   - 主要服务包括邮件服务器、博客、IRC 服务器、图片托管、RSS 阅读器等
   - 目标是在本地家中托管个人基础设施和服务，易于设置，愿意为自托管牺牲一些便利性
   - 由于家庭 ISP 的 NAT 限制，需要通过 Wireguard 隧道暴露服务到互联网

2. 硬件配置
   - NAS：2×8TB 硬盘，2012 年左右的硬件
   - Intel NUC（2015 年）：Intel i5-6260U，16GB RAM
   - AMD NUC：AMD Ryzen 7 8745HS，64GB RAM
   - OpenWRT One 路由器

3. 容器化平台：Incus
   - 使用 Incus（前身为 LXD）进行容器管理
   - 支持多种容器类型：LXC 容器、QEMU 虚拟机、OCI 容器
   - 集群配置：包含 AMD NUC（amd）和 Intel NUC（byggmester）
   - 网络配置：使用桥接设备 br0，扁平网络架构
   - 通过 OpenTofu 实现声明式配置管理

4. 基础设施即代码：OpenTofu
   - 使用 OpenTofu 的 Incus provider 实现声明式配置
   - 将服务分离到不同项目中，共享通用模板
   - 项目示例：ca、dns、immich、mediaserver、miniflux、syncthing、test、user-1000
   - 以 Immich 为例展示完整的 OpenTofu 配置流程

5. 网络与服务暴露
   - 通过 Wireguard 点对点 VPN 将本地网络连接到 VPS
   - 使用 Nginx 作为反向代理，暴露内部服务到互联网
   - 配置 nginx-acme 自动处理 TLS 证书
   - 内部 DNS 解析，避免在 Nginx 配置中保留 IP 地址

6. 静态网站托管：Syncthing
   - 使用 Syncthing 将静态网站内容同步到 Web 服务器
   - 简化发布流程，无需 CI/CD 设置或 GitHub Actions
   - 通过 Hugo 构建网站并输出到 /srv 目录

7. 网络设备：OpenWRT One
   - 使用 OpenWRT One 作为路由器
   - 开发了 OpenTofu provider 进行配置管理
   - 计划未来引入 VLAN 进行网络分段

8. 实用工具：USB KVM
   - 使用 USB KVM 设备简化多台计算机的管理
   - 通过 HDMI 和 USB-C 线缆连接，便于设置和维护

9. 总结与展望
   - 保持个人基础设施的开放性，分享配置代码供他人学习
   - 旨在为刚开始考虑更多自托管服务的人提供灵感

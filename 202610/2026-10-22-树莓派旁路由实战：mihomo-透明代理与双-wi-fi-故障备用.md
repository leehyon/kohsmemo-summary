# 树莓派旁路由实战：Mihomo 透明代理与双 Wi-Fi 故障备用
- URL: https://sumsec.me/2026/sumpi-mihomo-side-router.html
- Added: 2026-10-22 01:27:21
- Tags: #home #setup

## TL;DR
树莓派 5 用 Mihomo TPROXY 做旁路由，保留华为 AX3 Pro 的 DHCP，仅让按需设备手动指向 Pi 的 DNS 与网关；重点规避双 DHCP、IPv6 绕过、Docker 转发和 ARP 等坑，并保留回滚。

## Summary
文章记录树莓派 5 上 Mihomo 旁路由透明代理的实战与排障。最终方案让华为 AX3 Pro 保留唯一 DHCP、NAT 与 Wi-Fi，树莓派只做 DNS 和 TPROXY 透明代理；普通/备用 SSID 自动使用 `.1`，旁路由 SSID 由选中客户端手动把网关/DNS 指向 `.27`，以保留故障隔离与回滚能力。

**逻辑脉络**
- 先定拓扑：`eth0` 静态 `192.168.3.27/24`，`wlan0` 动态管理，AX3 关闭 IPv6/RA，双 SSID 分别承担普通/备用与按需旁路由入口。
- 再落组件：Mihomo 提供 `7890`/`7894`/`1053`，dnsmasq 仅监听 `.27:53` 并转发到本地 DNS，nftables TPROXY 配合策略路由接管 `eth0` 入站 IPv4 流量。
- 随后复盘故障：双 DHCP 互抢、旧租约池不兼容、`dhcp-broadcast` 误用、Docker `FORWARD DROP`、同网段双网卡 ARP flux、IPv6 绕过代理、DHCP ACK 后客户端未应用配置。
- 最后用 `url-test` 自动选择新加坡节点，并给出服务、TPROXY、DNS、代理、透明转发、客户端六层验证及回滚维护清单。

**底层逻辑**
- 故障隔离优先：DHCP 留在主路由，Pi 故障不影响全家自动上网；旁路由只服务主动选择它的设备。
- 分层验证：systemd active 不等于端口监听，必须分别检查地址、端口、规则与客户端实际配置。
- 最小改动与可回滚：窄放行、独立 oneshot、配置备份，回滚只删除自建对象。

**Takeaways**
- 保留单一 DHCP；`eth0` 的 `.27` 必须由 Pi 自身静态配置，并在 AX3 DHCP 池中排除或保留。
- TPROXY 只覆盖匹配的接口与地址族；IPv6、`wlan0`、本机流量都可能绕过。
- Docker 的 `FORWARD DROP` 需窄放行；同网段双网卡需收敛 ARP，并设置明确 metric。
- 客户端 Wi-Fi 详情比服务 ACK 更可信；`url-test` 只解决选节点，不解决分流。
- 面板与 `secret` 不要暴露公网，订阅更新可能覆盖配置，务必保留备份与回滚路径。

# An ad-free Android TV
- URL: https://cretezy.com/2026/ad-free-android-tv
- Added: 2026-10-21 01:16:53
- Tags: #home #setup

## TL;DR
用 ADB 把 Google TV 换成 Projectivy 启动器、SmartTube 与按键映射，禁用原生桌面和推广包，再配合 Pi-hole，即可得到无广告的 Android TV。

## Summary
作者喜欢 Android TV 的生态与低价，却无法忍受 Google TV 首页那条无法关闭的推广横幅，「仅应用模式」也删不掉。于是他给出了一套完全基于 ADB、无需 root 且可回滚的方案：换启动器、换 YouTube 客户端、重映射遥控器，再从 DNS 层封掉广告。

**逻辑脉络**
- 先立痛点：Google TV 首页横幅是系统级推广，设置里无开关，仅应用模式只是隐藏其他内容。
- 再列替代组件：Projectivy Launcher 换桌面、SmartTube 换 YouTube、Wholphin 作 Jellyfin 客户端、Button Mapper 改键。
- 然后用 ADB 串起步骤：连无线 / USB 调试 → 装应用 → 设 home 并禁用原生 launcher 与 setupwraith → 卸官方 YouTube → 开无障碍并授权 → 清理动画与预装包。
- 最后补网络层去广告（Pi-hole / AdGuard DNS）、画质模式建议，以及回滚方法与安全提醒。

**底层逻辑**
- 广告来自系统 Launcher 与官方应用，所以从「替换入口 + 阻断域名」两层下手。
- 全程用 ADB 系统命令，不依赖 root，每步都可用 pm enable / install-existing 还原。
- 必须先设好 home activity 再禁用原 launcher，否则设备可能失去桌面。

**Takeaways**
- 原生横幅无法在设置中关闭，只能换启动器或在 DNS 层屏蔽对应域名。
- 首选 Projectivy Launcher，FLauncher、ATV Launcher Pro 可替代；SmartTube 去广告并内置 SponsorBlock。
- 禁用 setupwraith 可能清掉已存 Wi-Fi，需备遥控器重连；电视上还要验证 HDMI 输入切换是否正常。
- Pi-hole 或 AdGuard DNS 可覆盖全屋设备，不止电视。
- 完成后关闭无线 / USB 调试，避免开放 ADB 端口被同网设备连接。

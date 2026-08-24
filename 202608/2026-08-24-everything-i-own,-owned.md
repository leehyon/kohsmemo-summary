# Everything I own, owned
- URL: https://schlarp.com/posts/everything-i-own-owned/
- Added: 2026-08-24 03:02:50
- Tags: #hardware #agent

## TL;DR
作者用 AI 代理逆向五款外设，发现固件普遍无保护，可关闭摄像头 LED、获取麦克风命令 shell，并绕过补光灯签名。AI 让硬件破解变得极易，安全风险大增。

## Summary
作者借助 Claude Opus 5 对五款 USB/WiFi 外设进行 agent 驱动的逆向工程，发现它们普遍缺乏固件保护：摄像头活动 LED 可被关闭、麦克风带明文命令 shell、补光灯可被网络未授权内存写入。两星期约 13 小时即完成全部五款设备的破解。

**逻辑脉络**
- 方法：取固件与更新工具，让 Claude 自动枚举协议、验证签名、寻找隐藏功能，并实际测试。
- Insta360 Link：RTOS 固件无签名，USB 命令可读写文件并重启，patch 掉活动 LED 表项。
- ASUS 显示器：固件无保护，I2C 更新，可 patch 像素清理提示；另有 DDC/CI 脚本控制。
- Shure MV7：固件藏于 Windows 软件，HID 明文命令 shell，权限仅字符串比较，可操控 LED 和触摸板。
- Elgato Cam Link 4K：无保护，HID 隧道 I2C；含 FPGA bitstream 可深挖。
- Elgato Key Light Mini：有 Ed25519 签名但可绕过，单次 HTTP POST 使签名失效，任意刷机。

**Takeaways**
- 外设固件普遍无安全启动或签名验证，修复成本低。
- AI 代理把逆向工程从数周人工缩短为几小时，门槛大降。
- USB 外设可通过浏览器 WebHID 被攻击，网络外设威胁更大。
- 提醒：不要将敏感设备置于不可信网络，需重新思考外设信任边界。

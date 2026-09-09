# 近期开发的四个开源项目 | LiuShen's Blog
- URL: https://blog.liushen.fun/posts/6a6de263/
- Added: 2026-09-09 01:23:27
- Tags: #setup #blog

## TL;DR
作者因自用需求改造了 Artalk、Memora、hubProxy，分别补充 AI 审核/助手、Go 重构相册和运营后台多用户，并强调迁移前备份与版本兼容。

## Summary
本文记录近期作者基于个人自用需求，借助 AI 对四个开源项目进行的改造：Artalk 增强审核与 AI 助手、Memora 采用 Go 重构并接入高德地图、hubProxy 增加后台与多用户管理，Message Pusher 仅略为提及。整体策略是保留原项目兼容性，只改不顺手的地方。

**逻辑脉络**
- Artalk：官方停更两年，评论审核功能落后。作者加入同步关键词拦截与 DeepSeek/OpenAI 的 AI 审核，并新增 AI 助手、管理后台以及 OAuth2/OIDC 登录等；接口保持兼容，仅换 Docker 镜像。
- Memora：相册站由 Nuxt 服务端重构为 Go 后端与纯静态前端，大幅降低内存占用；媒体统一用 FFmpeg 处理，地图改用高德，前端增加分页与懒加载。数据库和 /app/data 挂载保持兼容，迁移需先升至 v1.0.0-rc.4，再换镜像并处理 UID 100 目录权限。
- hubProxy：为镜像加速站增加管理后台、OAuth2 注册/登录与多用户配额；用户经子路径中的 8 位令牌区分，免去 Docker login；拉取统计按 Blob 下载而非请求数，并配合安全限流与 bcrypt 密码存储。
- Message Pusher：本来规划但未展开，它是一款基于 Webhook 的推送服务，可把通知整理成更友好的消息，作者认为偏个人使用故略写。

**Takeaways**
- 兼容优先：Artalk 前端零改动、Memora 数据不变，升级基本等于换镜像。
- 防守组合：关键词拦截先阻断骚扰，AI 审核再辅助筛查漏网之鱼。
- 重构收益：Go 后端 + 静态前端把相册内存占用从约 1GB 大幅降低。
- 多用户方案：无需子域名，直接在镜像路径里拼 8 位令牌即可区分用户并限制配额。
- 迁移铁律：先备份、按指定版本号逐步升、再换镜像并确认目录属主。

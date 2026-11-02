# Bookmark Summary 
自动读取 [kohsmemo](https://github.com/leehyon/kohsmemo) 仓库中的书签数据，通过 Jina Reader 获取网页文本内容，再借助大模型生成内容总结。

## Latest 10 Entries

(2026-11-02) [so i guess everyone uses llms to think now - eva's site](202611/2026-11-02-so-i-guess-everyone-uses-llms-to-think-now---eva%27s-site.md)
- 作者坚持不用 LLM 做研究：研究乐趣、署名责任与学习过程更重要；LLM 虽强但仍需专家引导，当前 AI 安全营销常以恐慌和抢跑披露伤害安全实践。

(2026-11-02) [Tips for more effective fuzz testing with AFL++](202611/2026-11-02-tips-for-more-effective-fuzz-testing-with-afl%2B%2B.md)
- AFL++ 模糊测试清单：启用 sanitizer，优先 persistent mode，包含源码测内部函数，隔离状态，勿直接传 fuzz buffer，用 memfd 和更小缓冲区暴露缺陷。

(2026-11-02) [俄罗斯软件哲学：单机榨干](202611/2026-11-02-%E4%BF%84%E7%BD%97%E6%96%AF%E8%BD%AF%E4%BB%B6%E5%93%B2%E5%AD%A6%EF%BC%9A%E5%8D%95%E6%9C%BA%E6%A6%A8%E5%B9%B2.md)
- 俄罗斯软件以单机垂直优化、底层掌控和极简工具主义，对抗硅谷依赖云抽象与堆资源的臃肿模式。

(2026-10-30) [C for Rust Programmers](202610/2026-10-30-c-for-rust-programmers.md)
- 文章从 Rust 视角梳理 C 的怪癖：布尔非原生、字符串以空字节结尾、整数宽度依平台、错误处理弱、数组退化为指针、无引用与借用检查，并提醒小心内存安全。
- Tags: #language

(2026-10-23) [嵌入式家用智能设备刷机与逆向指南](202610/2026-10-23-%E5%B5%8C%E5%85%A5%E5%BC%8F%E5%AE%B6%E7%94%A8%E6%99%BA%E8%83%BD%E8%AE%BE%E5%A4%87%E5%88%B7%E6%9C%BA%E4%B8%8E%E9%80%86%E5%90%91%E6%8C%87%E5%8D%97.md)
- 系统化嵌入式刷机与逆向指南：情报、备份和恢复链先行，核对启动链与专属分区，分级刷写并逐项验收。
- Tags: #home #setup

(2026-10-23) [What Is a Hardware Wallet?](202610/2026-10-23-what-is-a-hardware-wallet.md)
- 硬件钱包把私钥离线保存并在设备内签名交易，降低被盗与钓鱼风险；但需备份助记词、官方渠道购买并防范物理丢失。

(2026-10-23) [What I Self-Host](202610/2026-10-23-what-i-self-host.md)
- 作者用 Beelink N100 迷你主机自托管 28 个服务，坚持不暴露公网、优先原生、Podman 替代 Docker，以简单运维替代云服务与流媒体。
- Tags: #home #setup

(2026-10-22) [树莓派旁路由实战：Mihomo 透明代理与双 Wi-Fi 故障备用](202610/2026-10-22-%E6%A0%91%E8%8E%93%E6%B4%BE%E6%97%81%E8%B7%AF%E7%94%B1%E5%AE%9E%E6%88%98%EF%BC%9Amihomo-%E9%80%8F%E6%98%8E%E4%BB%A3%E7%90%86%E4%B8%8E%E5%8F%8C-wi-fi-%E6%95%85%E9%9A%9C%E5%A4%87%E7%94%A8.md)
- 树莓派 5 用 Mihomo TPROXY 做旁路由，保留华为 AX3 Pro 的 DHCP，仅让按需设备手动指向 Pi 的 DNS 与网关；重点规避双 DHCP、IPv6 绕过、Docker 转发和 ARP 等坑，并保留回滚。
- Tags: #home #setup

(2026-10-21) [Code is clay now](202610/2026-10-21-code-is-clay-now.md)
- 代理式编程让代码像黏土般可塑，变更成本骤降；但品味与架构仍关键。工匠模式留在循环中逐轮判断，工厂模式把判断前置到流水线，二者应按问题混用。

(2026-10-21) [You could have invented transformers from memory](202610/2026-10-21-you-could-have-invented-transformers-from-memory.md)
- 文章用干扰-信号比统一比较线性层、MLP 与自注意力作为联想记忆的容量，并说明 softmax 注意力配合 log M 缩放可近乎无界地存储键值对。
- Tags: #math

## Monthly Archive

- [2026-11](202611/monthly-index.md) (3 entries)
- [2026-10](202610/monthly-index.md) (24 entries)
- [2026-09](202609/monthly-index.md) (10 entries)
- [2026-08](202608/monthly-index.md) (31 entries)
- [2026-07](202607/monthly-index.md) (53 entries)
- [2026-06](202606/monthly-index.md) (68 entries)
- [2026-05](202605/monthly-index.md) (26 entries)
- [2026-04](202604/monthly-index.md) (44 entries)
- [2026-03](202603/monthly-index.md) (82 entries)

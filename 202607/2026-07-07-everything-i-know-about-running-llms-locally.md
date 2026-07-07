# Everything I know about running LLMs locally
- URL: https://github.com/jamesob/local-llm
- Added: 2026-07-07 01:52:10
- Tags: #setup

## TL;DR
用 ~$50k 的 4× RTX PRO 6000（384GB VRAM）搭配二手 EPYC 主机和独立 PCIe 交换机，实现本地 SOTA 大模型高性能推理，P2P 带宽达 27.5 GB/s，并分享了硬件选型、BIOS 调优和软件配置的完整方案。

## Summary
本文详细介绍了构建本地 SOTA 大模型推理服务器的硬件配置与软件调优经验。作者基于“把钱花在 VRAM 上”的核心原则，选用 4 块 RTX PRO 6000（共 384GB VRAM）搭配二手 EPYC 平台（ROMED8-2T 主板、DDR4 内存），并通过独立 PCIe Gen4 交换机（c-payne PM40100）实现 GPU 间直连通信，从而在较低总价下达到接近 Gen4 线速的 P2P 带宽（27.5/50.4 GB/s）。

**逻辑脉络**
- **预算分级**：$2k 可买 2× RTX 3090（48GB）运行 Qwen3.6-27B 和 STT；$40k 可买 4× RTX PRO 6000（384GB）运行接近 Claude Opus 的模型（如 GLM-5.2-594B）。
- **硬件选型**：基系统使用 eBay 淘来的 ASRock Rack ROMED8-2T + EPYC 7313P + 128GB DDR4，总价约 $5.6k；GPU 占费用大头（~$46k）。
- **PCIe 交换机**：通过 c-payne 的 Microchip Switchtec PM40100 实现 5× x16 下行，配合 REDRIVER AIC 和 SlimSAS 电缆连接主板，使 GPU 间 allreduce 走交换机而非通过 CPU 根复合体，降低延迟。
- **BIOS/内核调优**：强制 PCIe 链路为 Gen4 x16、禁用 ASPM、启用 Re-Size BAR、关闭 IOMMU（`iommu=off` 避免 NCCL 挂起）、运行 ACS 禁用脚本确保 P2P 流量留在交换机内。
- **电源管理**：单 110V 电路下通过 `nvidia-smi -pl 350` 限制每卡 350W，总负载 ~1.4kW。
- **模型运行**：本地缓存权重（ZFS 双盘复制），用 Docker Compose 隔离服务，同一局域网内用 opencode 前端访问。

**Takeaways**
- 本地推理的最大瓶颈是 VRAM 而非计算能力；优先买大显存卡（如 RTX 3090/6000）可运行更大模型。
- PCIe 交换机（如 c-payne）能显著降低多卡通信延迟（0.37–0.45 µs），避免昂贵的 PCIe5/DDR5 平台。
- 关键 BIOS 设置：强制 PCIe 速度、禁用 ASPM、启用 Re-Size BAR；内核参数需加 `iommu=off` 并禁用 ACS。
- 模型权重应本地缓存，用 Docker 隔离服务，前端工具（如 opencode）可提高日常使用效率。

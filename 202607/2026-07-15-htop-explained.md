# htop explained
- URL: https://peteris.rocks/blog/htop/
- Added: 2026-07-15 01:57:32
- Tags: #explained

## TL;DR
本文详细解释了 htop 中各项系统指标的含义，包括负载均值、进程状态、内存使用等，并通过实际操作演示了如何从 `/proc` 文件系统获取信息。

## Summary
**逻辑脉络**
- 文章从 htop 中的 uptime 和 load average 出发，逐步深入解释每个字段的意义。
- 通过分析 `/proc` 文件系统（如 `/proc/uptime`、`/proc/loadavg`）和系统调用（如 `strace`），说明工具如何获取信息。
- 详细解析进程状态（R、S、D、Z、T、t），并用实际命令（如 `sleep`、`cat /dev/urandom`、`mount.nfs`）和代码（C 程序创建僵尸进程）演示各状态的行为。
- 最后介绍进程用户、权限、setuid 机制以及进程树等概念。

**Takeaways**
- Load average 是运行态和不可中断睡眠态进程数的指数衰减移动平均，不能直接等价于 CPU 利用率。
- 进程状态 R 表示正在运行或可运行；S 表示可中断睡眠（等待事件）；D 表示不可中断睡眠（通常为 I/O）；Z 为僵尸进程；T 和 t 分别由作业控制信号和调试器停止。
- `/proc/<pid>/` 目录提供了进程的详细信息，如 cmdline、cwd、exe 等。
- 不可中断睡眠（D）可能由 NFS 或内存不足引起，无法通过信号杀死；僵尸进程（Z）只占用 PID，需其父进程回收或杀死父进程。
- 进程的 setuid 位（如 `/usr/bin/passwd`）使程序以文件所有者权限运行，而非启动者。

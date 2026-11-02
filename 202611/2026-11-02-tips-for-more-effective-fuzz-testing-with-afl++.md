# Tips for more effective fuzz testing with AFL++
- URL: https://nullprogram.com/blog/2025/02/05/
- Added: 2026-11-02 05:08:47

## TL;DR
AFL++ 模糊测试清单：启用 sanitizer，优先 persistent mode，包含源码测内部函数，隔离状态，勿直接传 fuzz buffer，用 memfd 和更小缓冲区暴露缺陷。

## Summary
文章认为，模糊测试对发现复杂输入处理软件的缺陷极为有效却常被低估；在 C/C++ 场景中，AFL++ 是当前最佳平台之一，作者基于约 1,000 个项目经验给出一份提升效率的清单。其核心不是单点技巧，而是围绕“更快执行、更早暴露、更好隔离”来配置测试夹具。

**Takeaways**
- 默认启用 ASan 与 UBSan，并调整 ASAN_OPTIONS：崩溃即中止、关闭符号化、检测栈上 use-after-return、填满分配内存；C++ 可加 _GLIBCXX_DEBUG。
- 优先使用 persistent mode 与精简模板，避免重复进程启动；把相关源文件直接包含进测试 TU，以便测试内部函数、static 函数并替换 main 等符号。
- 每次测试都要隔离状态：重置全局变量，清零或填充输出缓冲区；不要直接把 AFL++ 的 buf 传给目标，而应复制成与 len 等长的缓冲区，避免漏报越界读。
- 不必在测试中释放内存；对只接受路径的接口，用 memfd_create 的 /proc/self/fd/3 提供内存文件；对 FILE * 可用 fdmemopen。
- 缩小过大的固定缓冲区（如 64KiB 改为 16）以更快触达边界路径；这样更容易发现溢出等缺陷，再映射回原尺寸输入。

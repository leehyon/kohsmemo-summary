# How we make AI coding more cost efficient without sacrificing task quality
- URL: https://github.blog/ai-and-ml/github-copilot/how-we-make-ai-coding-more-cost-efficient-without-sacrificing-task-quality/
- Added: 2026-09-08 02:02:00
- Tags: #agent #explained

## TL;DR
GitHub Copilot 不以单次 token 数为准，而是按完整任务效率优化：选择性压缩输出、移除无用行号、压缩提示词并直送后台结果，在保持质量的同时降低成本。

## Summary
本文认为，评估 AI 编程智能体效率应以完整任务为对象，而非单次输出 token 数；GitHub Copilot 的几项改动通过减少模型不必要的工作来降本，同时维持任务质量。

**逻辑脉络**
- 局部优化陷阱：缩短 shell 输出（RTK）会让模型因缺少信息而重读或重跑，整任务反而更贵，因此要按任务全过程衡量。
- 选择性压缩输出：保留源码类与任意命令输出，重组搜索结果不丢内容，只压缩构建/测试等重复噪音，并提供完整原文恢复路径；成本下降，质量无回退。
- 删除无效格式：view 不再输出行号，离线推理成本降约 5%，在线人均日成本降约 3%。
- 压缩提示词：用 meta-prompting 把 task tool 提示词缩短一半，初期导致 agent 串行，靠行为测试和一句“独立 agent 可并行，要考虑副作用”修复；每轮节省约 1300 个 prompt token。
- 直送后台结果：批量把完成的 shell/后台任务结果放进 tool-result，省去单独检索轮次，AI Credits 用量约降 2.3%。

**底层逻辑**
- 真正的成本来自完整流程中的模型调用与上下文，不是局部 token 数；优化的方向是移除模型不需要做的工作。
- 压缩要按输出所代表的内容区分：格式冗余可去掉，关键内容需无损或可恢复；恢复原文的频率是重要信号。
- 改动需在每个工作流中验证；离线基准、在线实验缺一不可，某个产品有效不代表另一产品适用。

**Takeaways**
- 优化完整任务，而非单次工具调用。
- 尽量用 harness 确定性完成后台结果交付，减少模型轮次。
- 压缩输出时保留关键上下文并跟踪恢复路径。
- 提示词压缩需要行为测试防止隐性回归。
- 每个改动要在实际工作流中重新测量。


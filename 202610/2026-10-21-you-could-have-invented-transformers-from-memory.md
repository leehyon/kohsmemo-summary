# You could have invented transformers from memory
- URL: https://alexwang.ai/posts/associative-memory/
- Added: 2026-10-21 01:21:59
- Tags: #math

## TL;DR
文章用干扰-信号比统一比较线性层、MLP 与自注意力作为联想记忆的容量，并说明 softmax 注意力配合 log M 缩放可近乎无界地存储键值对。

## Summary
文章把线性层、MLP、自注意力统一视作联想记忆，以干扰-信号比衡量容量，解释现代网络层为何能记住大量键值对。

**逻辑脉络**
- 外积存储容量约 d_k；最优线性回归通过白化键把容量提到约 2d_k。
- 非线性激活抑制低相似键，ReLU 约 2d_k，平方 ReLU 约 d_k^2 量级，容量随幂次多项式增长。
- softmax 等价指数加权，容量随 β 指数增长；长上下文令 β 随 log M 增长可近乎无界。

**底层逻辑**
- 存储即写入键值外积；召回是按相似度加权求和。
- 容量由干扰/信号比达到 1 定义；随机键值下用随机游走估算干扰。
- 改进路径：更聪明地写（最小二乘）与更选择性地读（非线性/softmax）。

**Takeaways**
- d_k=64 时：外积 64、最优线性 128、平方 ReLU 约 2700、softmax 约 120 万。
- MLP 可视为键值记忆，gate 抑制低相似项；self-attention 是非参数记忆，记忆数随上下文增长。
- β 过大会饱和难训练，长上下文可用 log M 缩放 logits。
- 该容量估计忽略训练数据，另有按 bit/参数衡量记忆的工作。

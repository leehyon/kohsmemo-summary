# A software engineering interview question I like: computing the median
- URL: https://krisshamloo.com/blog/007
- Added: 2026-07-10 05:36:54
- Tags: #career #math

## TL;DR
计算中位数是一道简单但有深度的面试题，能考察编程、边界、API 设计、统计及算法优化等多方面能力。

## Summary
作者分享了一道他喜欢的软件工程面试题：计算中位数。他认为这道题看似简单，却能考察候选人的编程能力、边界处理、API 设计、统计理解等多个维度。文章详细解析了这道题的各个考察点，并给出了 Python 实现示例。

**逻辑脉络**
- 作者先阐述自己面试提问的理念：不问谜题，而是问有深度的简单问题。
- 然后以计算中位数为例，逐一列出其作为面试题的优点：
  - 基础实现类似“Fizz Buzz”，可检验基本编程能力。
  - 涉及排序、是否原地修改、API 性能等设计决策。
  - 包含 off-by-one 陷阱（偶数长度时取平均）。
  - 有奇偶分支，考察条件逻辑。
  - 可引申到统计讨论（中位数 vs 均值）。
  - 易于测试、可展示标准库知识（statistics 模块）、甚至可引出 quickselect 算法。
- 最后给出带注释的 Python 实现，演示如何处理空数组、排序、奇偶情况。

**Takeaways**
- 好的面试题应具备多个层次，从基础到深入都能考察。
- 计算中位数可覆盖：基本编程、边界条件、API 设计、算法复杂度、统计概念。
- 面试中可观察候选人调试 off-by-one 错误的能力。
- 标准库（如 statistics.median）是加分项，但不应替代自己实现。
- Quickselect 算法能将平均复杂度从 O(n log n) 降至 O(n)，适合深入探讨。

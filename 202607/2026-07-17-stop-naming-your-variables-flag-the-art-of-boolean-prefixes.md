# Stop Naming Your Variables "Flag": The Art of Boolean Prefixes
- URL: https://thatamazingprogrammer.com/posts/stop-naming-your-variables-flag-the-art-of-boolean-prefixes/
- Added: 2026-07-17 03:25:21
- Tags: #design

## TL;DR
命名布尔变量应使用 `is`、`has`、`can`、`should` 前缀，形成清晰的问题；禁止否定名称；参数布尔易引发陷阱，需用拆方法、枚举或配置对象替代。

## Summary
文章指出，命名布尔变量时使用模糊名称（如 `flag`、`done`）会导致代码可读性差且易产生 Bug。核心观点是布尔变量名称应是一个清晰的问题，提供“是/否”答案。

**底层逻辑**：布尔变量本质上是向代码提出的问题，名称必须是明确的问句。作者提出四个前缀（IS、HAS、CAN、SHOULD）覆盖 99% 的场景，每个前缀有固定的语法搭配（形容词或名词），违反此规则会增加阅读阻力。

**逻辑脉络**：
- 通过实际代码示例展示模糊布尔名的危害（`open`、`flag`、`done`）。
- 引入四个前缀：`is`（身份/状态）、`has`（拥有/包含）、`can`（能力）、`should`（意图），并给出正反例。
- 强调“无否定”规则：永远不要在变量名中使用否定词（如 `isNotEnabled`），应使用正向名称。
- 区分属性与参数：布尔参数易陷入“布尔陷阱”，建议拆分为多个方法、使用枚举或配置对象。
- 列出五个反模式：耸肩变量、语法不匹配、双重否定、多功能布尔、漂移标志。

**Takeaways**：
- 每个布尔变量名必须是一个清晰的问题，遵循 `is + 形容词`、`has + 名词`、`can + 动词`、`should + 动词` 的语法。
- 永远不要使用否定词（如 `isDisabled` → `isEnabled`），避免双重否定。
- 避免布尔参数：用拆分方法、枚举或配置对象代替。
- 警惕五个反模式：
  - 耸肩变量（如 `flag`）→ 明确含义
  - 语法不匹配（如 `hasActive`）→ 改为 `isActive`
  - 双重否定 → 用正向名称
  - 多功能布尔 → 拆分或组合
  - 漂移标志 → 使用结果对象或提前返回

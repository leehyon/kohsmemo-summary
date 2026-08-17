# Use Task Runners for Common Coding Tasks
- URL: https://hamvocke.com/blog/task-runners/
- Added: 2026-08-17 01:41:50
- Tags: #efficiency

## TL;DR
作者建议用任务运行器（bash 脚本、make、just、mise）统一跨仓库的构建、测试、格式化等常见命令，避免记忆各技术栈的不同命令，只需执行统一的 run build、make test 等。提供实现示例和优缺点。

## Summary
使用任务运行器可以让开发者在多个代码仓库间用一致方式执行常见编码任务，避免记忆不同工具链的命令。作者从自身日常痛点出发，推荐为每个仓库配置统一的任务入口。

**逻辑脉络**
- 作者常切换仓库，各仓库技术栈不同，需记住构建、测试、格式化、迁移等命令。
- 先给出 bash 脚本方案：在仓库根目录创建一个 run 脚本，包装 npm 等命令，支持 run build、run test。
- 然后介绍 make：通过 Makefile 定义 target 和命令，需要声明 .PHONY 避免同名文件干扰，部分 shell 支持 tab 补全。
- 接着介绍 just：类似 make 但更现代，无需 .PHONY，需额外安装。
- 最后介绍 mise：可作为工具管理器和任务执行器，使用 mise.toml 声明任务，并支持拆分任务文件。

**Takeaways**
- 用任务运行器统一常见命令，靠肌肉记忆操作，提升开发幸福感。
- Bash 脚本灵活且预装，适合简单封装，复杂时可拆分为 bin/ 目录下多个脚本。
- Make 广泛可用，但需注意用 tab 缩进、显式声明 .PHONY。
- Just 是更易用的 Make 替代品，但需额外安装。
- Mise 集成工具管理，适合需要同时管版本和任务的中大型项目。

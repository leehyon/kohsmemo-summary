# Docker Build Cache: The 80/20 Rules That Cut CI Image Builds From Minutes to Seconds
- URL: https://the-practical-developer.online/posts/docker-layer-caching-ci-build-speed/
- Added: 2026-07-15 01:50:53
- Tags: #build #guide

## TL;DR
通过层排序、多阶段构建、BuildKit 缓存挂载和远程缓存四条规则，可将 Docker 构建时间从几分钟降至 20 秒左右，核心是优先缓存不常变的依赖层。

## Summary
本文介绍通过 Docker 层缓存优化 CI 构建速度的四条规则，可将构建时间从数分钟缩短至数十秒。核心是层排序：将最不易变的依赖复制和安装放在前面，源代码复制放在后面。

**逻辑脉络**
- Docker 层缓存基于指令文本和复制文件哈希，缓存失效会传播到后续所有层，因此层顺序最关键。
- 典型低效 Dockerfile 将 `COPY . .` 放在依赖安装前，导致任何文件变更都会使整个依赖层失效。
- 规则 1：按变更频率从低到高复制文件（先复制 package.json 和 lock 文件，安装依赖，再复制源代码）。
- 规则 2：多阶段构建，分离构建与运行阶段，避免生产镜像包含构建工具和开发依赖。
- 规则 3：使用 BuildKit 缓存挂载（`--mount=type=cache`）实现包级别缓存，避免因单一依赖变更而重新安装所有包。
- 规则 4：远程缓存（`cache-from`/`cache-to`）使临时 CI 运行器能从上次构建加载缓存，避免冷启动。
- 给出了完整的 GitHub Actions 工作流示例和最终的 Dockerfile。
- 测量显示：从 4 分 12 秒降至 22 秒，缓存命中率 96%。

**Takeaways**
- 层排序是最大收益点：先复制 lock 文件再安装依赖，可节省 60-70% 构建时间。
- 多阶段构建避免生产镜像包含开发依赖和构建工具，同时缓存独立。
- BuildKit 缓存挂载实现包级增量更新，比层缓存的粒度为细，适合频繁变更 lock 文件的场景。
- 远程缓存（registry 或 GHA cache）解决 CI 运行器无本地缓存的问题，需注意存储成本。
- 避免反模式：不使用 `--no-cache`、不复制整个 monorepo、不安装开发依赖到生产阶段、固定 Node.js 版本。

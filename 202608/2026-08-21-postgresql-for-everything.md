# PostgreSQL for Everything
- URL: https://www.raphaelbauer.com/posts/postgresql-everything/
- Added: 2026-08-21 02:52:51

## TL;DR
PostgreSQL 凭稳定、易扩展和丰富插件，可在多数场景替代 Kafka、Redis、Elasticsearch 等专用系统，简化架构并加速交付。先问“PostgreSQL 能否做到”，避免盲目引入新组件。

## Summary
文章主张用 PostgreSQL 替代 Kafka、Redis、Clickhouse、Elasticsearch 等多种专用系统，以简化技术栈、加速迭代。作者基于多年 CTO 实践，认为 PostgreSQL 的稳定性、易用性和扩展性使其成为“万能数据库”。

**逻辑脉络**
- 作者从 2003 年项目经历出发，对比 MySQL，强调 PostgreSQL 功能完整（全文搜索、索引、SQL 标准），避免多系统同步。
- 指出 PostgreSQL 力量源于三点：稳定、易部署、简化 IT 架构。
- 逐项论证替代方案：全文索引替代 Solr/Elasticsearch；JSON/GIN 替代 MongoDB；SKIP LOCKED 实现队列替代 Kafka/RabbitMQ；TimescaleDB 处理时序数据替代 Clickhouse；pgvector 支持向量检索；UNLOGGED 表提速为缓存替代 Redis；blob 存储替代文件系统；LTREE 替代图数据库；SQL 生成 JSON 替代微服务。
- 以 Tetris 在 SQL 中实现收尾，强调“先问 PostgreSQL 能否做到”。

**底层逻辑**
- 第一性原理：简单性驱动速度；维护多套系统带来同步、运维和技能负担。
- 核心假设：PostgreSQL 已具备足够性能和功能，多数“专用系统”的需求可以收敛到单数据库。
- 方法论：从一个可扩展的通用存储出发，按需使用插件，而非默认引入新组件。

**Takeaways**
- 用 PostgreSQL 的全文搜索和 GIN 索引可替代独立搜索集群。
- 通过 SELECT ... FOR UPDATE / SKIP LOCKED 可实现持久队列。
- TimescaleDB 与 pgvector 让 PostgreSQL 覆盖时序和 AI 向量场景。
- UNLOGGED 表加触发器可模拟 Redis 缓存场景。
- 新需求出现时，先用 PostgreSQL 验证，再决定是否引入新技术。

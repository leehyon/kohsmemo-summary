# A faster way to copy SQLite databases between computers
- URL: https://alexwlchan.net/2025/copying-sqlite-databases/
- Added: 2026-07-24 02:02:43
- Tags: #guide

## TL;DR
通过 SQLite 的 .dump 导出文本并 gzip 压缩，可大幅减小数据库体积（如 3.4 GB 降至 240 MB），从而加速远程复制，且避免传输中数据损坏。

## Summary
文章提出一种通过 SQLite 的 `.dump` 导出文本并压缩来加速跨计算机复制数据库的方法，解决了因索引过大导致复制缓慢的问题。

**逻辑脉络**
- 问题：直接通过 rsync 复制大型 SQLite 数据库时，索引占用了大量空间，传输慢且易中断。
- 方案：使用 `sqlite3 my_database.db .dump` 将数据库导出为文本文件，索引变为单行 `CREATE INDEX` 语句，大幅减小体积。
- 压缩：文本文件重复性高，用 gzip 压缩后体积可缩减至原数据库的 1/14（如 3.4 GB → 240 MB）。
- 传输与重建：在服务器生成压缩文本，rsync 到本地，解压后通过 `cat file.txt | sqlite3 new.db` 重建数据库。
- 额外优势：导出过程生成稳定快照，避免复制中数据库写入导致的不一致问题。

**底层逻辑**
- 索引本质是数据的冗余副本，不包含新信息，复制时浪费带宽。
- SQLite 的文本导出将数据与索引均表示为 SQL 语句，索引仅保留创建指令，实际数据只存一次。
- 文本的重复性（如大量 `INSERT INTO`）使压缩效率极高，适合网络传输。

**Takeaways**
- 使用 `sqlite3 database.db .dump | gzip -c` 在服务器生成压缩文本，比直接复制原始数据库快 10 倍以上。
- 传输完成后通过 `gunzip` 解压并重建数据库，可完全恢复原库结构及数据。
- 此方法适用于网络带宽有限、数据库较大的场景，尤其适合只读备份或迁移。
- 注意：重建数据库会重新创建索引，因此本地环境需与原服务器 SQLite 版本兼容。
- 若数据库经常写入，先用 `.dump` 生成快照，避免复制过程中数据不一致导致的“database disk image is malformed”错误。

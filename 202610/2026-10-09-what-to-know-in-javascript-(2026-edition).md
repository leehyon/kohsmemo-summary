# What To Know in JavaScript (2026 Edition)
- URL: https://blog.master.dev/what-to-know-in-javascript-2026-edition/
- Added: 2026-10-09 01:22:23

## TL;DR
文章盘点 2026 年 JavaScript 生态，包括 ES2025/ES2026 语言特性、框架与运行时、Vite 与 TypeScript 工具链、AI 写码及 npm 供应链安全，建议回归基础。

## Summary
文章按语言、框架、运行时、构建、测试、包管理六条线盘点 2026 年 JavaScript 生态。核心判断是：语言每年小步快跑，工具链与运行时持续收敛，AI 与供应链安全成为新增变量。

**逻辑脉络**
- 先讲 ECMAScript 2025 已落地：Iterator Helpers、Set 方法、RegExp.escape、内联 flag、Promise.try、导入属性等。
- 再展望 2026：Temporal API、using/DisposableStack、Array.fromAsync、Iterator.concat、Error.isError、Base64/Hex 等。
- 框架：React 19 的 RSC、Server Actions、Compiler；Vue 3.6 Vapor；Svelte 5 Runes；Next 16 默认 Turbopack；Remix/React Router、TanStack、Astro 6。
- 运行时：Node 原生 TS、Bun 被 Anthropic 收购、Deno 安全默认；三者更兼容。
- 构建与类型：Vite 8 换 Rolldown 并推 Vite+；Turbopack 成 Next 默认；webpack 仍有计划；TypeScript v6 为 Go 版 v7 铺路。
- 测试与 npm：Vitest/Playwright 上升；npm 遭遇 s1ngularity、debug/chalk、Shai-Hulud 等供应链攻击。
- 结尾建议：学基础，以应对工具变化与 AI 写码。

**底层逻辑**
- 性能与内存：Iterator 懒执行、Temporal 正确性、RSC 减客户端体积。
- DX 与统一：Vite+、Bun 一体化、Node 原生 TS 降低依赖。
- 安全：Deno 默认最小权限、npm 供应链风险凸显。
- 组织与商业：Vercel 收 NuxtLabs、Cloudflare 收 Astro、Anthropic 收 Bun，生态整合加速。

**Takeaways**
- ES2025 已可关注 Iterator、Set、RegExp、Promise.try、导入属性；ES2026 重点看 Temporal 与 using。
- 框架最大变量是 React 服务端能力、Svelte/Vue 性能模式、Next 16 Turbopack 与 Astro 6。
- Node/Bun/Deno 更趋同：Node 原生 TS，Bun 重 DX 与速度，Deno 重稳定安全。
- Vite 8/Rolldown、TypeScript v6→v7 是工具链关键升级，AI 写码与 npm 安全不可忽视。
- 长期仍应投入基础原理，而非只追工具。

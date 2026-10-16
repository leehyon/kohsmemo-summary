# How our vibe coded website looks like a designer made it
- URL: https://railcode.dev/blog/vibe-coded-website
- Added: 2026-10-16 01:38:56
- Tags: #design #vibe-coding

## TL;DR
作者用编码智能体把 Railcode 官网做成主题公园式设计：靠海量参考、多版本生成、fork 对比、playground 调参与持续迭代，证明非设计师也能用 AI 做出有品味、像设计师操刀的网站。

## Summary
作者以 Railcode 官网为例，说明 vibe coding 也能做出被误认为设计师操刀的设计。核心并非炫耀，而是非设计师借助编码智能体，把个人趣味与大量参考转化为可迭代的视觉系统。

**逻辑脉络**
- Railcode 寓意 code on rails，rails + fun 联想到过山车，由此确定主题公园方向。
- 先用 agent 生成多版设计种子，按强度谱系与“放飞”探索；借 Rollercoaster Tycoon 做小游戏原型，否掉后收敛到单个过山车。
- 过山车放模板违和，扩展为景点长条，再与下一节做色彩过渡；随后 fork 对比、playground 调色，把草地从蓝改绿，背景白改天蓝并加云。
- 最后统一图标、分区、土壤页脚与随区块变色的导航，形成完整站点。

**底层逻辑**
- 非设计师无法凭空造概念，靠海量浏览与生成变体扩展可能性，再组合、迭代、丢弃。
- 单个 HTML 快速 fork 与并排比较，成熟后才拆 React；playground 实时调参替代慢迭代。
- 保留所有 fork，从早期 mockup 中淘组件；用清晰参考引导 agent。

**Takeaways**
- 设计专用 Anthropic 模型，Fable 最强，OpenAI 模型即使给明确方向也吃力。
- 先大量生成再扔掉 99%，偶尔捡回一个组件或新想法。
- 让 agent 故意“放飞”，并做从极简到夸张的谱系版本。
- 持续看网站找灵感，喜欢某个组件就以其为基底再建。
- 迭代多数是死路，但过程本身要好玩。

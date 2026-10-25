# PM Game Skills

面向产品经理与游戏原型开发者的 Agent Skills：从一句话玩法到可试玩原型、体验验证与可分享链接。

**81 skills + 1 router**。基于 [awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) 二次开发，保留 76 个原有专项技能，逐项补充验收场景，新增 5 个产品与交付技能。

## 快速开始

```bash
npx skills add Yiheng-guo/pm-game-skills
```

Codex 本机安装（Python 3.10+，不覆盖已有不同版本）：

```bash
python3 scripts/install.py --dest ~/.codex/skills
```

已有上游技能时，先用 `--backup /absolute/backup/directory` 保留旧版再替换；支持 `--dry-run` 预览。安装保留每个技能自己的 references、scripts 和 assets。下一轮对话即可发现新技能。

可以直接对 AI 说：

> 做一个手机和电脑都能玩的航线解谜游戏。玩家旋转线路，把能源送达终点；需要关卡、失败重试、提示和分享链接。先定义最小玩法和验收条件，再开发与发布。

## 工作方式

| 阶段 | 入口 | 交付 |
|---|---|---|
| 需求拆解 | game-product-brief | 玩家、核心动作、决策、完整循环、边界与学习假设 |
| 引擎选择 | game-engine-selection | 按平台、玩法、成本选型，保留现有技术栈 |
| 实现 | 原有引擎/玩法技能 + game-code-quality | 明确状态归属、数据校验、回退与必要测试 |
| 浏览器轻量原型 | web-game-core | 无引擎依赖的 DOM/SVG 游戏，键盘与触屏可用 |
| 试玩与分享 | game-playtest-release | 技术验收、真人试玩方法、部署与公开链接验证 |

Router 按任务组合技能，不会把全部技能正文一起加载。每个原有技能都有自己的 `references/acceptance.md`：覆盖主流程、异常边界和生命周期；这些是验收规范，不能视为已经在对应引擎执行过。

## 示例项目

[星港调度 · Orbit Dispatch](https://github.com/Yiheng-guo/orbit-dispatch)：独立的可玩浏览器游戏仓库。包含玩法定义、技术取舍、规则测试与试玩入口。真人体验是否有趣，需要实际玩家反馈，不由自动测试代替。

## 目录与维护

- [技能目录与上游基线](docs/skill-catalog.json)
- [兼容性与验证范围](docs/VERSION-SUPPORT.md)
- [开发与验证](docs/DEVELOPMENT.md)
- [二次开发说明](docs/DERIVATIVE.md)

安装工具验证重名、冲突、备份与失败回滚；仓库检查验证技能格式、路由、引用与插件清单。代码示例仍需结合项目锁定版本使用。

## 许可证

[Apache 2.0](LICENSE)。保留 [NOTICE](NOTICE) 中上游作者与来源信息。引擎、模型、素材、商店上架和托管服务各自的费用及条款独立于技能包许可证。

# 二次开发说明

本项目基于 gamedev-skills/awesome-gamedev-agent-skills，来源提交 184b72be02884f782a0058f2eeae2ce4277453e4。上游原作者为 Abhishek Barali 与贡献者，原许可证和 NOTICE 保留。

本版本修改全部 76 个原有专项技能及 Router；每个原有技能新增对应的主流程、异常边界和生命周期验收场景。新增 game-product-brief、game-engine-selection、game-code-quality、game-playtest-release、web-game-core；共 81 个专项技能与 1 个 Router。

Router 的新项目选型依据由默认优先 Godot 改为玩家、设备、玩法与交付约束；补充扁平安装时按名称定位技能的方法。原有项目仍保留既有引擎。新增安装工具支持冲突预览、显式备份与失败回滚。

这些修改完善任务定义和交付约束，不代表所有引擎 API 已经重新执行验证。上游版本表中的发行状态不作为本版本独立核实的事实。实际运行证据需要对应项目、设备与运行时；浏览器示例不证明 Unity 或 Unreal 的可用性。

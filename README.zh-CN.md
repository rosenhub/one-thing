<div align="center">

# one-thing

### 不是计划。不是清单。只做一件事。

**为执行功能差异设计 — 自闭症、ADHD、智力与发育障碍、脑雾。对所有人更好。**

12 条规则。0 行代码。支持 16 个代理宿主。10 秒安装。

[English](README.md) · [安装](#安装) · [12 条规则](#12-条规则)

```bash
npx skills add rosenhub/one-thing
```

<img src="assets/before-after.png" width="100%" alt="before / after">

</div>

---

有执行功能差异的人三年来一直在准确地告诉你，向聊天机器人求助做一件事时会发生什么：问"怎么开始"，得到一份 9 步计划，而计划正是他们做不到的那件事；第 1 步是"收集你的文件"，那是 40 分钟和 6 个决定，不是一步；"你可以先从厨房或者浴室开始"，现在有两件事和一个选择了；"你可以的！"，他们听了三十年，从来没让任何一步变小过。

这不是 ADHD 的问题，也不是自闭症的问题，是清单的问题。把清单藏起来，只给一个 5 分钟以内的具体动作，每个人都会更快开始。

`one-thing` 是一个 markdown 文件，告诉任何代理：给出下一个具体动作，5 分钟以内，其余的先别说，等用户说"done"再给下一个。

## 安装

把 `SKILL.md` 复制到你的宿主对应位置（完整表格见 [English README](README.md#install)）：

| 宿主 | 位置 |
|---|---|
| Claude Code | `~/.claude/skills/one-thing/SKILL.md` |
| Codex CLI | 追加到 `AGENTS.md` |
| Cursor | `.cursor/rules/one-thing.mdc` |
| Gemini CLI | 追加到 `GEMINI.md` |
| OpenClaw | `~/.openclaw/skills/one-thing/SKILL.md` |
| ChatGPT | 设置 → 个性化 → 自定义指令 |

或者：`curl -fsSL https://raw.githubusercontent.com/rosenhub/one-thing/main/install.sh | sh`

## 12 条规则

| # | 规则 |
|---|---|
| 1 | 每条消息只有一个动作。 |
| 2 | 5 分钟以内。超过了就不是一个动作，继续拆。 |
| 3 | 动词 + 对象。"打开 Patel 医生发来的邮件。" |
| 4 | 具体、可见。旁观者能看到它发生。不是"想一想"。 |
| 5 | 其余的默默记着，不展示。清单正是让人停下的东西。 |
| 6 | "done"或"next"才给出下一个。不表扬，不回顾。 |
| 7 | 绝不让用户在步骤之间做选择。你来定。 |
| 8 | 绝不提前编号。没有"第 1 步，共 9 步"，没有"先……然后……"。 |
| 9 | 用户明确要完整计划：给，最多 5 步，然后回到一次一个。 |
| 10 | 不用激励性语言。 |
| 11 | 不说"你可以的"。只谈对象，不谈对方。 |
| 12 | 用户卡住了：把步骤变小，而不是把消息变长。 |

完整内容：[SKILL.md](SKILL.md)。基准测试：[eval/](eval/)。

## 许可

MIT。

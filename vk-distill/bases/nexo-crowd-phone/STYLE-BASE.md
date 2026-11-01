# STYLE-BASE · nexo-crowd-phone（序界 NEXO · 人多假装看手机）

> **mode: `silent_text_first`**（见 §0 Mode 证据 · **LOCK**）  
> 源：`/workspace/vk-distill/refs/nexo-crowd-phone/source.mp4`（1024×576 · ~60.0s · aweme `7696344887303066331`）  
> 短链：https://v.douyin.com/GSQ2YUbpVyA/ · 作者：**序界 NEXO**  
> 片题锚：「vibe知识大赏｜为什么人一多你就开始假装看手机？」  
> 密帧：`bases/nexo-crowd-phone/keyframes/`（`06-f0028`…`09-f0035` = densest）· contact-sheet  
> **密窗：** ~27–36s（f0028–f0035）自我关注 HUD → 手机盾牌。  
> **勿套** `xiaomo` 聊天错对 HUD，也 **勿套** `moyou` 波形床——本底座是 **pill-crowd / phone-shield** 家族。  
> **硬规则：** 只用 KEEP；**BANNED twin list 一律不得出现**。成片按列表打 **Award D**。  
> 清单权威：`/workspace/vk-distill/docs/DISTILL-MULTIDIM.md` · `INFRAME-SHOW.md` · `AWARD-SCORECARD.md`  
> **九项补丁：** 2026-10-31（高 ROI 补丁 · Mode 已 LOCK；补 M/I/D/K + 字阶硬化）

---

## 0. Mode lock（证据边界 · LOCK）

| 检查 | 结果 |
|---|---|
| **听轨一句** | 本机：bass≈0.80 · mid≈0.20 · hi≈0.01；`silencedetect` **0** events → **连续低音床**，无稳定语音 formant/口播节奏。**无 VO。** |
| **密帧一句** | 脚本由 **钩子大标题 / 左栏数据文案 / 底栏「概念 pill + 叙事句」** + 图内 GazeLines·TensionMeter·ThoughtCallouts·PhoneShield 承担；**无**口播字幕带、**无**口型头像。见 `06-f0028`/`09-f0035`。 |
| 本地 dump | `source.mp4` 可解码；keyframes 1024×576 代理可量字阶。 |
| 结论 | `mode: silent_text_first` · `has_vo: false` · `has_bottom_subtitles: false` · `script_anchor: bottom_narrative_plus_stage_copy` · `duck: null` |

Mute 10s 必须能懂：深海军底 + **铜金** lone self + **灰蓝** pill 人群 + 注视虚线；自我关注→手机成盾由 gadget 状态讲完。  
**禁止**发明字幕带或 under_voice。

---

## 0b. 知识锚可信度（Knowledge-anchor · D/K · LOCK）

| 项 | 内容 |
|---|---|
| **出处（源片数据拍）** | 源片左栏常用 **Pew Research** 式社调脚注（如「其实没什么要看的」类结论 + 大金数字）。成片若引用须写 **机构全名 + 年份**（例：Pew Research Center, 2012 或源片当年脚注），**禁止**无出处大数字。 |
| **示意边界** | PillCrowd / GazeLines / TensionMeter 液面 / PhoneShield 半透罩 / FocusBrackets / ThoughtCallouts —— **叙事 HUD 示意**，不是眼动追踪实验复绘，也不是「焦虑量表」实测读数。紧张表百分比/液面高度 = **戏剧读数**。 |
| **易杠点** | ① 把 Pew（或任一社调）的 **样本/年份/题干** 说成「所有人都…」普遍定律 → 成片用「一项调查 / 示意」，禁写成全民铁律。② 数字与源脚注不一致或捏造 → **Fail K**；不确定就标「示意」或砍数字只留机制。③ 「手机=盾」是安全行为隐喻 → 禁写成临床诊断或「你有社交障碍」点名羞辱。④ 聚光灯效应翻盘句若被杠「其实别人都在看你」→ 收束落在 **自我关注机制**，不贩卖绝对安全感。 |
| **免责** | 左下/脚注保留「示意 / 出处年」；我们系列用 Vibe知识大赏 身份，**不**强制抄 `@序界 NEXO` 水印。 |

---

## 1. 一句话（静音能懂的论证骨架 · KEEP · D1）

**人一多就假装看手机（灰 pill 人群 vs 铜金 lone）** → **Pew 式数据「其实没什么要看的」+ PhoneMock 栅格** → **自我关注：GazeLines + TensionMeter + ThoughtCallouts** → **手机成盾（安全行为）** → **翻盘：其实没那么多人在看你**。

公式/金句永远出现在 **gadget 状态差**（注视汇向自我、紧张表涨、盾罩挡住虚线）被看懂之后。

撞车：与 `xiaomo` 同社交焦虑域但 **主隐喻= pill-crowd / phone-shield**，非聊天错对；与 `moyou` 同暗底但不走波形床。

---

## 2. KEEP · 语法

### 2.1 色板角色（语义色 · D3 · KEEP）

| 角色 | 用途 | 锚 |
|---|---|---|
| **深海军竖渐变** | 主底；竖向暗板/微网格可有；中心极淡暖晕 | `#0B1018 → #10141D` · glow `#2A1C10` |
| **人群灰蓝** | 匿名 pill 人群、次级 UI | `#3A4252` / hi `#4A5568` |
| **自我铜金 accent** | lone self、概念 pill 描边、callout、关键词 ≤2/屏 | `#E08A48`（ref median ~`#D58648`；比 xiaomo `#FFB347` 更偏铜） |
| **ink** | 底栏叙事句、非强调主句 | `#F2EEE6` |
| **muted** | 水印、脚注、出处年 | `#8A90A0` |
| **紧张红** | TensionMeter 液面 | `#C84C4C` |
| **盾冷白** | PhoneShield 轮廓/半透罩 | `#C8D4E8` |
| **禁止** | 第三语义主色抢「自我/紧张」；照片脸、3D 透视人体 | — |

与近亲差异一句：`xiaomo` 琥珀金 + 聊天错对；`moyou` 琥珀金 + 波形；**本底座铜金=自我/安全行为，灰蓝=人群。**

### 2.2 字阶系统（密帧实测 · D2 · LOCK · ≥4 级）

源 1024×576；下表为 **×~1.875 → @1080 约值**（`06-f0028`/`07-f0030`/`09-f0035` + yaml）。禁止臆造四级以外的「同级卡片换词」。

| 角色 | 证据帧 | 约字号@1080 | 字重 | 颜色 | 位置 |
|---|---|---|---|---|---|
| **hero / 钩** | 开场问句大字；数据拍左栏结论句 | **约 80–96px**（yaml headline 88） | 900 | ink 白 + **铜金关键词 ≤2** | 居中/偏右或左栏上 |
| **data_num** | Pew 式大金数字 | **约 110–130px**（yaml 120） | 900 | accent 铜金 | 左栏 |
| **narrative** | 底栏叙事句（「注意力转回自己…」「手机成了盾牌」） | **约 40–48px**（yaml 44） | 700 | ink | 底栏概念 pill 右侧 · band ~900–1020 |
| **concept_pill** | 「自我关注」「安全行为」描边胶囊 | **约 28–34px**（yaml 32） | 700 | accent 描边 + ink 字 | 底栏左 · 叙事句前 |
| **callout** | 「表情自然吗？」「站姿奇怪吗？」「手该放哪？」 | **约 26–30px**（yaml 28） | 700 | accent | 右栏气泡 · 引线指头/身/手 |
| **cite / foot** | 出处年 / 示意；顶左水印可选 | cite **约 20–24**；watermark **约 20–22** | 500 | muted | 左下脚注 / 顶左 |

关键词高亮规则：每屏烫铜强调 **≤1–2 处**；金/铜=自我/重点；红=紧张/风险（表液面，不抢叙事主色）。

规则补充：
1. 一屏一意；底栏 ≤2 行。  
2. 概念 pill 是机制标签，**不是**字幕轨。  
3. 数字必须带出处（Pew 年）或标「示意」。  
4. **≥4 硬级：** hero · narrative · callout/pill · cite/foot（data_num 为数据拍加档，不与 callout 同级混用）。

### 2.3 文字 ↔ gadget handoff（D5 前置）

| 拍型 | 谁主讲 |
|---|---|
| A · Text-lead | 开场钩问 / 翻盘金句；人群作衬底 |
| B · Gadget-lead | GazeLines+TensionMeter+Callouts / PhoneShield；字缩成 concept_pill+narrative |
| C · Dual irony | 灰人群「在看」vs 盾挡虚线 / 数据「没什么好看」vs 手还在刷 |

相邻两拍至少换一次主讲权；禁止连续三拍纯字墙或整卡 swap。

---

## 3. 道具语法（D6 · KEEP）

| 模板名 | 做什么 | persist+morph | 禁止 twin |
|---|---|---|---|
| **PillCrowd** | 灰蓝圆角 pill 头+身；可叠 `…` 气泡 | 人数/疏密可变；同构不换语言 | 左灰 pill 排 + 右铜 lone **固定双栏 gestalt** 作钩签名 |
| **PillSelf** | 同构铜金；可持 PhoneMock | 变色/抬手机/入盾 | 同铜 lone + 角括号框死构图 |
| **GazeLines** | 眼标 → 虚线汇向自我 | 线闪/汇聚加压 | 双眼标 + 虚线汇铜人 verbatim |
| **TensionMeter** | 竖胶囊进度 +「紧张」 | 液面爬升/回落 | 同款红液面+「紧张」标签签名位 |
| **ThoughtCallouts** | 2–3 句自检，描边铜，引线指头/身/手 | 错落 pop ~0.3–0.4s | 「表情自然吗？/站姿奇怪吗？/手该放哪？」三联 verbatim |
| **FocusBrackets** | 角括号框住自我（被打量 HUD） | 框闪/收紧 | 四角白括号+铜人固定框 |
| **PhoneMock** | 圆角机身 + 简化 app 栅格 | 数据拍用；栅格可亮一格 | 抄源片具体 app 图标排版 |
| **PhoneShield** | 半透冷白盾罩在自我上 | 盾出现挡虚线；pill 文案切「安全行为」 | **盾罩挡注视虚线** densest 签名 |
| **ConceptPill + NarrativeLine** | 底栏脚本锚 | pill 文案随机制切（自我关注→安全行为） | 同 pill+叙事句 verbatim 钩 |
| **DataStatCard** | 左栏大数字 + cite | 数字+脚注同屏 | 无脚注假 Pew 数字 |

跨拍复用变形（同 pill 变色/加盾/加气泡），禁止每拍全新 UI 语言。

**允许发明（N≥1 必新）：** 新「人群压力→回避物件」隐喻（禁只换文案的灰 pill 排+铜 lone+盾）；新自检气泡题；新翻盘 CTA（禁抄源片底栏原句若整段孪生）。

---

## 4. 3 秒动势清单（D4 · densest 旁必贴 · 本轮 LOCK）

格式：谁在动 · 状态差。证据：`keyframes/06-f0028`–`09-f0035` · 源 ~27–36s。  
**静帧死板 / 整卡 swap = 本维 Fail。**

### 密窗 A · Self-focus HUD（源 ~27–32s · `f0028`/`f0030`/`f0032`）

`t+0.0` 左 **PillCrowd** 灰蓝已在 · 眼标+**GazeLines** 虚线指向右铜 **PillSelf**（持 PhoneMock）· **FocusBrackets** 四角框住自我  
`t+0.8` **TensionMeter** 红液面爬升 · 标签「紧张」可读  
`t+1.6` **ThoughtCallouts** 错落弹出：表情自然吗？→ 站姿奇怪吗？→（~0.35s stagger）手该放哪？ · 引线分别指头/身/手  
`t+2.4` 底栏 **ConceptPill「自我关注」** + Narrative「注意力转回自己，一遍遍检查表现」· 人群/自我 **persist 不重置**  
`t+2.8` 注视线再闪一下加压 · 表液面近高 · 为盾拍铺垫

### 密窗 B · PhoneShield 安全行为（源 ~32–36s · `f0035`）

`t+0.0` **PhoneShield** 半透冷白罩从自我外侧展开 · PhoneMock 抬向面部/胸前  
`t+0.8` GazeLines 撞上盾缘被挡/折断 · 眼标仍在但「打量」失效可读  
`t+1.5` ConceptPill 切 **「安全行为」** · Narrative「手机成了盾牌」+ 次行「看起来很忙，就不会被打量」  
`t+2.2` TensionMeter 可微降或仍高（戏剧：行为缓解≠根因消除）· 人群 persist  
`t+2.8` 收束向翻盘拍预备；脚注/示意可淡入

### 前序钩（软参 · 非 densest 必贴）

开场：人多假装看手机双栏对比 ≤3–4s 入。  
数据拍：左栏 DataStatCard + PhoneMock 栅格（~15s 带）——签名但次密；episode 需要时再锁 timed。

---

## 5. 图内展示（INFRAME-SHOW · D5 · KEEP）

权威：`/workspace/vk-distill/docs/INFRAME-SHOW.md`

| 优先级 | 承载 | 本底座例子 |
|--------|------|------------|
| 1 · 论证本体 | 舞台 gadget 状态 | GazeLines 汇向自我；TensionMeter 涨；Callouts 错落；PhoneShield 挡虚线 |
| 2 · 定向/机制标 | 底栏 ConceptPill | 「自我关注」「安全行为」——标签，非口播字幕 |
| 3 · 叙事 punch | 底栏 NarrativeLine ≤2 行 | 检查表现 / 手机成盾 — **禁止**底栏独自讲完机制 |
| 4 · 数据 | 左栏 DataStatCard | 大数字 + Pew/示意脚注 |
| 5 · 脚注 | 左下 muted | 出处年 / 示意 — **不是** continuous white caption strip |

规则：
1. **禁止** continuous bottom white caption 当唯一讲义。  
2. densest：**走到哪标到哪**；**裁掉底栏 ~12–15% 后**，灰人群 vs 铜 lone + 注视/紧张表/盾 仍能讲完「自我关注→安全行为」→ G 才够。  
3. 主舞台 **persist + morph**（反翻页）；pill 变色/加盾，不每句清空。  
4. 论证拍 ≥**70%** 挂在 gadget 状态变化上。  
5. Gate 必写：`crop-bottom mute: pass|fail`（本底座裁底栏概念+叙事带）。

---

## 6. 节奏与时长（D7）

| 项 | 源片 | 我们用法 |
|---|---|---|
| 全长 | ~60s 密 | 3–5 min 可拉长机制 dwell / 加新例；**勿**只复制 60s 切速 |
| 钩 | ≤3–4s 人多假装看手机 | 钩 ≤3–4s |
| 密窗 | ~27–36s 自我关注→盾 | 同语法；动势见 §4 |
| 叙事拍 | 典型 ≤4–6s | 同；禁长时间死板 dwell |
| 密度 | 短片可 6–10 cut/min；callout stagger ~0.3–0.4s | 同 |
| 吸睛句（源） | 「为什么人一多你就开始假装看手机？」 | 可学结构；**整钩孪生画面 → D Fail** |
| 翻盘/CTA（源） | 「其实没那么多人在看你」类 | 可学行为号召；禁整段 verbatim + 同画面 |

**软锁节奏：** 编码语法，不锁死全片时间码表；densest 九项动势 **硬锁**。

---

## 7. BANNED twin list（D8 · Distance · LOCK）

**任一出现 → Award D ≤ 2 → 整片 Fail。**  
陌生人指静帧能喊「序界 NEXO / 假装看手机」→ D 失败。

| ID | 禁止内容 | 为何禁 |
|---|---|---|
| **B1** | **左灰蓝 PillCrowd 排 + 右铜金 PillSelf** 固定双栏对比作开场/密窗签名，且叠加注视虚线 | densest **grey pill-crowd vs copper lone self** gestalt |
| **B2** | **GazeLines 双眼标 + 虚线汇铜人 + FocusBrackets 四角框** 同屏固定 HUD | 被打量签名 |
| **B3** | **TensionMeter 红液面 +「紧张」** 夹在人群与自我之间的签名位 | 自检加压签名 |
| **B4** | ThoughtCallouts 三联 **「表情自然吗？/站姿奇怪吗？/手该放哪？」** verbatim | 自检文案签名 |
| **B5** | **PhoneShield 半透冷白罩挡注视虚线** + 底栏 pill「安全行为」+「手机成了盾牌」同构图 | densest 盾拍签名 |
| **B6** | 底栏 **ConceptPill「自我关注」+「注意力转回自己，一遍遍检查表现」** verbatim 钩 | 机制句签名 |
| **B7** | 整体 gestalt：深海军 + 灰 pill 人群 vs 铜 lone + 手机盾，使路人直接喊「序界」「假装看手机」 | 静帧孪生 |
| **B8** | 仅换文案的 pill-crowd / gaze / shield 三联当「新片」；或套用 xiaomo 错对聊天 / moyou 波形床当主道具 | 换皮 / 串家族 |

### 允许发明

| 槽位 | 要求 |
|---|---|
| 人群压力隐喻 | **禁** B1/B5 双栏+盾照抄；换新物件表达「被打量→回避」 |
| 自检气泡 | 自写新题；**禁** B4 三联原文 |
| 机制 pill + 叙事 | 自创短标；**禁** B6 原文 |
| CTA / 翻盘 | 谈减少自我监控/安全行为成本；**禁**整段源片底栏 verbatim + 同画面 |

---

## 8. 声音

- BGM only（默认 we-never）；**无 VO、无 under_voice duck**。  
- 目标整轨约 −14～−16 LUFS。  
- `beat_sync_cuts: true` 可选；不锁死原作曲名版权叙事。

---

## 9. 适合 / 不适合

**适合：** 聚光灯效应、自我关注、安全行为、手机作盾/社交回避、带脚注的简单社调图解（**新隐喻**）。  
**不适合：** 纯信息论惊奇（dianzi）、音乐多巴胺（moyou）、卸防话术课（xiaomo）、红皇后相对适应（bite）。

---

## 10. 与近亲底座分工

| | nexo-crowd-phone | xiaomo-disarm | moyou-music |
|---|---|---|---|
| 脚本落点 | 底栏概念 pill + 叙事；左栏数据 | 底栏叙事句 | 左上大标题 |
| 主隐喻 | pill 人群 / 注视 / 手机盾 | 聊天错对 / 六层 | 波形 / 脑区 |
| 强调色 | 铜金 `#E08A48` + 紧张红 | `#FFB347` + 错路红 | `#FFB347` |
| 禁抄焦点 | 灰人群vs铜lone·三联自检·PhoneShield | 错对气泡栈 | DROP 波形床 |
| 选题 | 聚光灯、安全行为、社交回避 | 卸防话术课 | 音乐神经 |

---

## 11. Sample Gate

`sample-silent-10s/` — 密窗 ~27–36s 语法（自我关注 → 手机盾）。见 `DISTILL-GAP.md`。  
**near-pass OK**；勿在缺口仍开时宣称 pixel pass。

下一集 densest 10s 必须用 **新人群压力隐喻 + 新 gadget + 新 CTA**，并打印：

`Award Score: L M C N T X H D G K F = ??/55`  
其中 **D** 对照 B1–B8 逐条勾；**G**=机制手势；**K**=知识锚；**crop-bottom mute: pass|fail**。

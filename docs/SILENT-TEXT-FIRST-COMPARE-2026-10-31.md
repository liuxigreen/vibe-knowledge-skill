# Silent / text-first grammar — compare (2026-10-31)

## Refs in this note

**Batch A (earlier same day)**  
1. `sanhao-halo-effect` — 叁号暗房 · 晕轮效应 (~162s)  
2. `zhongshan-learn-fast` — 中山晓 · 越学越快 (~105s)  
3. `lailong-xuanzang-passport` — 来龙去脉 · 玄奘无通关文牒 (~195s)  
4. `lailong-zhaoyun-infant` — 来龙去脉 · 出师表与亡国 (~249s)

**Batch B (dark-gold family — reclassified silent)**  
5. `xiaomo-darkgold-disarm` — 《六层卸防》社交卸防 (~180s) · twin `zhanwai-darkgold-huashu`  
6. `moyou-darkgold-music` — 《大脑先爽》音乐×大脑 (~40s ref; scalable)
7. `nexo-crowd-phone` — 序界 NEXO · 人多假装看手机 (~60s) · pill-crowd / phone-shield

All seven: **no narration** as production mode. On-screen type is the script. BGM ± SFX only.

> Prior distill of (5)(6) wrongly assumed VO (subtitle band + under_voice duck). Corrected 2026-10-31 — see each base `DISTILL-GAP.md`.

---

## Shared grammar (KEEP for silent lane)

| Rule | Evidence |
|---|---|
| One idea per screen | 8–18 汉字主句为主；金句可略长分行 |
| Hierarchy big→small | 主句 ≫ 图注 ≫ 出处脚注 |
| Color as stress | 单金 / 金红对 / 金蓝对 — 每屏强调 ≤1–2 |
| Negative space | 暗底充足，字与形不抢 |
| Structure classic | 钩 → 机制 → 反直觉/对照 → 升华 → CTA |
| Mute-readable | 静音 10s 能懂 |
| Citations when claiming fact | 年份、论文、典籍、示意 |

---

## Differences (when to pick which)

| Base | Visual family | Script anchor | Persuasion engine | Best next topics |
|---|---|---|---|---|
| sanhao-halo-effect | 黑暗房剪影 · 单金 | 居中诗性主句 | 感受→定义→文学升华→反问 | 认知偏差、投射、第一印象 |
| zhongshan-learn-fast | 双色角色对照 · 数据卡 | 顶栏问句/结论 | 寓言→机制标注→实验大数→身份 CTA | 学习方法、提问质量、马太 |
| lailong-xuanzang-passport | 纸偶史剧 · 地图 HUD | 主句+清单 | 常识反差→路线苦难→金句 | 历史辟谣、地理、制度文书 |
| lailong-zhaoyun-infant | 同纸偶家族 · 课本对读 | 课本题→金句答 | 编年悲剧→因果 | 课文深挖、人物命运 |
| **xiaomo-darkgold-disarm** | **暗金 HUD · 聊天错对 · 层进度** | **底栏设计叙事句** + 中央 UI | 生活钩→六层错对问法→概念卡→双投票 CTA | 社交话术、卸防、职场/销售问法 |
| **moyou-darkgold-music** | **暗金波形床 · 脑区 · DROP** | **左上大标题**（无底栏叙事） | 反直觉标题→持久床变形→文献脚注 | 音乐神经、drop/期待、耳虫 |
| **nexo-crowd-phone** | **pill 人群 · 注视虚线 · 紧张表 · 手机盾** | **底栏概念 pill + 叙事**（兼左栏数据拍） | 人多钩→数据→自我关注 HUD→安全行为盾→聚光灯翻盘 | 社交焦虑、聚光灯效应、回避行为 |

`lailong-*` 共享 `family: lailong-history-stick`。  
`xiaomo-*` / `moyou-*` 共享 **dark-gold silent** 家族（色板近亲），**脚本锚点不同**——勿混用底栏叙事 vs 左上标题。

---

## Dark-gold silent — quick tell

| Check | xiaomo-disarm | moyou-music |
|---|---|---|
| Bottom big serif line? | Yes = script | No (footnote only) |
| Top-left huge title? | Optional / layer cards | Always = script |
| Red as wrong path? | Yes (chat ✕) | Rare |
| Persistent lower bed? | Chat/meter stage | Waveform bars |

---

## nexo-crowd-phone (Batch B+)

- Mode: silent_text_first · densest 27–36s self-focus→phone-shield
- Not dark-gold chat/waveform; copper-gold `#E08A48`/`#F09850` + grey-blue crowd
- Sample: `bases/nexo-crowd-phone/sample-silent-10s/` · Gate: near-pass (see DISTILL-GAP)

---

## Recommendation for next episode

- 学习/元认知 → `zhongshan-learn-fast`  
- 认知偏差/滤镜 → `sanhao-halo-effect`  
- 历史反差 → `lailong-*`  
- **社交多层课 / 话术** → `xiaomo-darkgold-disarm`（已改 silent）  
- **音乐×大脑 / 反直觉曲线** → `moyou-darkgold-music`（已改 silent）
- **社交焦虑 / 假装看手机 / 安全行为** → `nexo-crowd-phone`（silent · near-pass sample）

---

## Download note

iesdouyin share SSR 常无 `play_addr`；yt-dlp 要 cookie。可用公开解析 CDN。成片统一 1920×1080。

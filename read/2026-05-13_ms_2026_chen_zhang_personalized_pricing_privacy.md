# Personalized Pricing in the Presence of Privacy Concerns

**作者**:
- Zhiqi Chen (Department of Economics, Carleton University)
- Mengyu Zhang (School of Economics, Ocean University of China) — Corresponding author

**期刊**: Management Science (Articles in Advance, 2026)
**DOI**: https://doi.org/10.1287/mnsc.2024.07170
**状态**: Articles in Advance, published online May 11, 2026; accepted by Raphael Thomadsen (Marketing)

## 中文摘要

本文研究在某些消费者天生关心隐私的在线市场中, 企业采用追踪技术 (tracking technology) 以收集个人数据并实施 personalized pricing 的激励问题. 作者在一个两差异化产品、两种市场结构 (monopoly vs. duopoly) 的 Hotelling 框架下, 引入一类"privacy-sensitive 消费者"——他们若被追踪会承受小幅效用损失 $D$. 主要发现包括: (1) 若 privacy-sensitive 消费者占比 $\theta$ 较高, 均衡中没有企业会采用 personalized pricing; (2) 竞争反而扩大 personalized pricing 的使用范围, 即竞争**不**保护隐私; (3) 赋予消费者数据控制权的隐私监管, 只在 $\theta$ 较低时才能起到保护隐私的预期作用, 否则反而使追踪技术更广泛地被采用. 驱动这些结论的核心力量是 monopolist 在 personalized pricing 下无法做出"给 privacy-sensitive 消费者非负净剩余"的可信承诺 (commitment problem). 竞争与隐私监管都在不同程度上缓解 (但未消除) 这一承诺问题, 反而促使企业更愿意上追踪技术.

---

## 1. 论文速览

| 维度 | 内容 |
|:---|:---|
| **研究问题** | 当部分消费者天生关心隐私时, 企业是否会采用 personalized pricing? 竞争与隐私监管 (consumer control) 如何改变这一激励? |
| **研究对象/场景** | 在线市场, 两个差异化产品 (Hotelling), 单一垄断者 / 双寡头两种结构 |
| **研究方法** | 理论建模 + 三阶段博弈 + Subgame Perfect Equilibrium (SPE); 扩展中使用 PBE |
| **核心机制** | Personalized pricing 下的 commitment problem: 企业无法承诺给 privacy-sensitive 消费者非负净剩余, 因为 $D$ 在到访时已沉没 |
| **关键发现** | (1) 当 $\theta$ 高时无企业使用 personalized pricing; (2) 竞争扩大追踪技术使用; (3) consumer control 监管反而使追踪更普遍 |
| **主要贡献** | 首次将"内生隐私偏好"的消费者引入 personalized pricing 模型, 改变了 Thisse-Vives (1988) 及 Armstrong (2006) 关于 PP 是 dominant strategy 的结论 |
| **适用场景** | 数字平台、电商、需要研究内生数据收集决策的市场; 隐私监管 (GDPR、CCPA) 的福利评估 |
| **最可能被 challenge 的地方** | (i) $D < t$ 的小成本假设可能掩盖更丰富的结构; (ii) 消费者隐私类型与位置独立; (iii) firms 不能 commit to personalized prices, 这是关键 driver 但论文并未深入讨论 commitment 技术的演化; (iv) 福利结论对 $D$ 是否真实存在 (而非感知存在) 高度敏感 |

---

## 2. TL;DR

只要市场上有足够多的"在意隐私"消费者, 即使没有任何监管, 企业**自己**就会放弃 personalized pricing——但这并非好事的全部: 一旦引入"消费者同意"型隐私监管 (类似 GDPR), 企业反而会更广泛地上追踪技术, 因为监管帮它解决了一个原本它无法解决的"承诺问题". 同样反直觉的是, 竞争市场比垄断市场使用追踪技术的范围更大——竞争降低价格, 但**不**保护隐私.

---

## 3. One More Thing (前置 Hook)

这篇文章最精妙的地方, 是把"隐私监管的反讽"解释成了一个 commitment 故事, 而不是常见的"企业找漏洞"故事.

想象一个垄断者面对一个 privacy-sensitive 消费者: 一旦消费者点进网店, $D$ 就已经沉没了. 此时垄断者**没有任何理由**对她手下留情——它会把价格定到 $V - t|x - x_i|$, 把她的所有消费者剩余吃干抹净. 这位消费者**预见**到这一点, 干脆不来. 当这种消费者足够多, 垄断者就被自己的"事后机会主义"反噬, 不得不放弃 personalized pricing.

现在加上 GDPR 式监管, 要求消费者授权才能追踪. 看起来这是给消费者的一份保护. 但**它真正给企业的, 是一个之前拿不到的承诺工具**: 企业现在可以可信地说"如果你拒绝授权, 我就只给你 uniform price". 这一根可信承诺, 反过来鼓励企业去上追踪技术——因为它不再担心 privacy-sensitive 消费者全部跑光. 监管不是抑制了追踪, 而是**让追踪变得安全了**. 这是一个非常漂亮的"good intention, perverse outcome"的机制故事, 而且数学上完全干净——没有任何模糊的行为假设.

---

## 4. 研究背景与动机

### 4.1 实践痛点

文章开篇引用了几组数据来构建现实关切: OECD (2018) 记录了 personalized pricing 在零售、旅游、个人金融等行业的实际使用 (Priceline, Orbitz, Home Depot 等); FTC (2025) 最新报告也证实了消费者面向行业的 personalized pricing 现象. 与此同时, Pew Research Center 2023 年调查显示 81% 的美国成年人担忧公司如何使用其个人数据 (McClain et al. 2023), GDMA-Acxiom 2022 年的 16 国调查表明平均 71% 的全球消费者对在线隐私表示担忧.

在监管侧, GDPR、各州数据隐私法、加拿大隐私法案的核心要素之一是"组织在处理个人数据前必须获得明确同意 (explicit opt-in consent)". 这正是本文所建模的"consumer control"监管形式.

### 4.2 理论缺口

现有 personalized pricing 文献存在两个传统:
1. **Pecuniary privacy 假设**: Belleflamme-Vergote (2016), de Cornière-Montes (2017), Montes et al. (2019), Chen et al. (2020), Ali et al. (2023), Ichihashi (2020), Loertscher-Marx (2020), Anderson et al. (2023), Rhodes-Zhou (2024, 2025) 等. 这一支的共同假设是: 消费者关心隐私**仅**因为隐私会影响其支付价格. 这导致一个 "Loertscher-Marx 命题": "central issue is not the protection of privacy but rather the protection of information rents".
2. **Intrinsic privacy 假设, 但不涉及 personalized pricing**: Casadesus-Masanell & Hervas-Drane (2015), Campbell et al. (2015), Choi et al. (2019), Acemoglu et al. (2022), Miklós-Thal et al. (2024), Choe et al. (2025) 等. 这一支引入"内生隐私偏好", 但通常研究双边平台 (服务收入 vs 数据变现), 与 PP 决策无直接对接.

**本文恰好填补这两支文献的交集**: 第一支不允许消费者真正"恶心"被追踪, 第二支不研究 PP 决策的内生选择.

### 4.3 核心贡献

1. **机制层面**: 揭示 personalized pricing 中的 commitment problem——由于 privacy cost 沉没, monopolist 无法承诺给 privacy-sensitive 消费者非负净剩余, 导致这些消费者**根本不来**. 这是一个全新的 PP 决策不被采用的机制 (与 de Cornière-Montes 2017 和 Ichihashi 2020 中"承诺不歧视以诱导信息披露"的机制完全不同).
2. **市场层面**: 证明"竞争**不**保护隐私"——duopoly 采用追踪技术的参数范围**严格大于** monopoly. 反例: 经典的 Thisse-Vives (1988) 中 PP 是 dominant strategy, 一旦引入 $\theta > 0$, 在 $\theta$ 大时反而 (U, U) 是均衡.
3. **政策层面**: 揭示 consumer control 型监管的**反讽后果**——它扩大了追踪技术的使用范围. 在垄断市场, 当 $\theta$ 处于中间区间时甚至**降低**消费者福利与社会福利. 在双寡头, 福利效应更复杂, 但追踪技术的使用范围一定扩大.
4. **方法层面**: 给出了一个"内生隐私偏好"如何系统性改变 PP 文献基本结论 (Armstrong 2006, Thisse-Vives 1988, Houba et al. 2023) 的 unified framework.

---

## 5. 模型设定与假设

### 5.1 模块化符号体系

**(a) 消费者与市场**

| 符号 | 含义 | 备注 |
|:---|:---|:---|
| $x \in [0, 1]$ | 消费者位置 (理想品味) | uniform distribution |
| $x_A = 0, x_B = 1$ | 两个产品的位置 | 最大化差异化 |
| $V$ | 消费者对产品的内在估值 | $V > 2t$ (baseline) 保证完全覆盖 |
| $t$ | 不匹配成本系数 | $t \cdot\|x - x_i\|$ 是 mismatch cost |
| $\theta \in (0, 1)$ | privacy-sensitive 消费者占比 | 与位置 $x$ 独立 |
| $D$ | privacy-sensitive 消费者被追踪后的效用损失 | $D < t$, 一旦到访即沉没 |
| $\alpha$ | 是否承担 privacy cost 的 indicator | $\alpha = 1$ for privacy-sensitive |

**(b) 企业与技术**

| 符号 | 含义 | 备注 |
|:---|:---|:---|
| 单位成本 | 标准化为 0 | |
| Tracking technology | 学习消费者位置 → 实施 PP 的前置条件 | 成本忽略不计, 只用于打破 indifference |
| Pricing strategy | $U$ (uniform) 或 $P$ (personalized) | 在 Stage 1 选定 |
| $p_i^U, p_i^P(x)$ | uniform vs. personalized 价格 | $i = A, B$ |

**(c) 博弈结构**

| 符号 | 含义 |
|:---|:---|
| Stage 1 | 企业同时选择并宣布 pricing strategy |
| Stage 2 | 消费者决定是否访问企业网店 |
| Stage 3 | 企业定价, 消费者决定购买 |

### 5.2 Players, Sequence, Information

- **Players**: 在 monopoly 中是单一企业 (firm M, 同时卖 A 和 B) + consumers; 在 duopoly 中是 firm A、firm B + consumers.
- **Sequence**: 上述三阶段, 同时选择策略 (Stage 1) → 消费者决定到访 (Stage 2) → 价格设定与购买 (Stage 3).
- **Information**: 消费者类型 $\theta$ 的分布为 common knowledge, 但个体类型企业**不可观测**. 企业**可在采用 tracking technology 后观测消费者位置 $x$**.
- **Solution concept**: Subgame Perfect Equilibrium (baseline); 在 Section 6.3 改用 PBE.
- **Critical assumption on commitment**: 企业**无法**事前承诺 personalized prices 函数形式. 一旦上技术, 它在 Stage 3 一定会最大化事后利润, 即提取消费者剩余.

### 5.3 关键目标函数

**Monopoly 在 personalized pricing 子博弈**:

$$\Pi^P_M = (1 - \theta)\left[\int_0^{1/2} (V - tx)\,dx + \int_{1/2}^{1} (V - t(1 - x))\,dx\right] = (1 - \theta)\left(V - \frac{t}{4}\right) \quad (1)$$

> 这个利润函数中, $(1 - \theta)$ 表示只有 privacy-insensitive 消费者到访购买, 中括号内是垄断者通过 PP 完全提取这部分消费者剩余得到的总和 $(V - t/4)$. 由于 privacy-sensitive 消费者全部消失, 利润相对 textbook monopoly 缩水了 $\theta$ 比例.

**Monopoly 在 uniform pricing 子博弈**: $p_A^U = p_B^U = V - t/2$, $\Pi_M^U = V - t/2$, 市场完全覆盖.

**Monopoly under consumer control, PP 子博弈** (当 $\theta < t/(2V - t)$):

$$\Pi_M^{P'} = p_A^{P'} x_A^{P'} + p_B^{P'}(1 - x_B^{P'}) + (1 - \theta)\left[\int_{x_A^{P'}}^{1/2} (V - tx)\,dx + \int_{1/2}^{x_B^{P'}}(V - t(1-x))\,dx\right] \quad (2)$$

> 前两项是接受 uniform price 的消费者 (含所有 privacy-sensitive 消费者位于 $[0, x_A^{P'}] \cup [x_B^{P'}, 1]$, 加上 privacy-insensitive 消费者中靠近端点者) 贡献的收入; 后两项是接受 tracking 的 privacy-insensitive 中间段消费者贡献的 PP 收入. 端点处的 uniform price 与中段的 PP 形成一个"双轨制定价"——这是 commitment 工具被监管"赋能"后才出现的产物.

**Duopoly (P, P) 子博弈中的 PP 价格**: $p_A^{PP}(x) = t(1 - 2x), p_B^{PP}(x) = 0$ for $x \in [0, 1/2]$ (对称地反过来), 经典 Thisse-Vives 结果. 这是 Bertrand 风格的 "head-to-head"价格战, 每个消费者拿到对手提供的最低价 (考虑 mismatch 后).

### 5.4 关键假设及其作用

**A1. $V > 2t$ (baseline)**: 保证若无隐私成本, 市场会被完全覆盖. **Justification**: 标准 Hotelling 假设, 排除 "monopoly-like" 配置. **If relaxed**: Section 6.2 放宽为 $V \in (t/2, 2t/3]$, 即不完全覆盖. 此时基本定性结论 (PP 选择阈值结构) 仍然成立, 同时复制 Rhodes-Zhou (2024) 的 "低覆盖率下 PP 提高利润" 结论.

**A2. $D < t$ (modest privacy cost)**: 保证 $V > t + D$, 即在 personalized price = 0 时所有消费者都能获得正剩余. **Justification**: Carrascal et al. (2013) 估计欧洲消费者对在线浏览数据估值约 €7 (一个 Big Mac 套餐); Lin (2022) 估计 intrinsic preferences 平均值约 $0.14 \sim \$2.37$. **If relaxed**: 若 $D > t$, 某些消费者在被追踪后即使免费也不会购买远端产品, 模型分析会更复杂, 但定性方向 (高 $\theta$ → 弃用 PP) 应该会更强.

**A3. 隐私成本一旦到访即沉没**: 这是驱动 commitment problem 的核心. **Justification**: 与 intrinsic privacy preference 定义一致 (Lin 2022)——消费者对被追踪本身有 disutility, 与购买决策无关. **If relaxed**: 若 $D$ 可在购买后退还, commitment 问题消失, 文章主要结论会被颠覆.

**A4. 企业无法 ex ante commit to personalized prices**: 这是 commitment problem 存在的另一面. **Justification**: 现实中要做这种承诺, 需要写明位置→价格映射的合同, 法律实施困难. **If relaxed**: 若企业能 commit, 它就能给 privacy-sensitive 消费者非负净剩余, 整个 commitment problem 故事会消失.

**A5. 类型与位置独立 ($x \perp$ privacy-type)**: **Justification**: 简化解析. Miklós-Thal et al. (2024), Choe et al. (2025) 也用了类似假设. **If relaxed**: 若隐私偏好与位置正/负相关, 企业可以从分布层面学习, 故事会更微妙——但作者用脚注说明此假设是简化, 主结论应稳健.

---

## 6. 分析路线图

整篇文章是一个"逐层加复杂度"的标准 IO 论文结构:

1. **Section 4.1 (Monopoly + No Regulation)**: 建立 commitment problem 的最简版本, 推出 $\theta$ 阈值 $t/(4V - t)$, 论证 monopolist 在 $\theta$ 高时**自愿**放弃 PP. 这是全文 anchor result (Proposition 1).
2. **Section 4.2 (Monopoly + Regulation)**: 引入 consumer control, 发现监管**扩大** PP 使用 (阈值放宽到 $t/(2V - t)$). 给出 Proposition 2 & 3 (后者讨论福利).
3. **Section 5.1 (Duopoly + No Regulation)**: 加入竞争维度. 四个子博弈 $(U, U), (P, P), (P, U), (U, P)$. 关键发现: 不对称 $(P, U)$ 均衡中, PP 企业**仍然无法**吸引 privacy-sensitive 消费者 (commitment problem 在 unilateral 情况下依然有效). Proposition 4.
4. **Section 5.2 (Duopoly + Regulation)**: 监管后, $(U', U')$ 均衡**消失**——至少有一家企业用 PP. 关键反直觉发现: 更大的 $D$ 反而**促使** PP 更广泛 (Proposition 5).
5. **Section 5.3 (Welfare under Duopoly)**: 福利效应更微妙, 在 region IV ($\theta \geq \tilde{\theta}$) 监管降低社会福利 (Proposition 6).
6. **Section 6 (Extensions)**: (i) 异质企业 → 监管可能**降低所有消费者**效用 (Proposition 7, 这是 baseline 没有的新结论); (ii) 不完全覆盖 → 主结论稳健; (iii) timing 改变 → 主结论稳健, 且 baseline 结果在 multiple equilibria 中是"利润最大"的那个 PBE.

**逻辑链**: Commitment problem (Monopoly, no reg) → 竞争缓解但未消除 (Duopoly, no reg) → 监管 *进一步*缓解 commitment 问题, 从而扩大 PP (Both market structures, reg) → Extensions 验证.

---

## 7. 核心分析与求解

### 7.1 Proposition 1 (Monopoly, No Regulation)

**命题陈述**: 比较 $\Pi^P_M = (1-\theta)(V - t/4)$ 与 $\Pi^U_M = V - t/2$:
- (i) 若 $\theta < t/(4V - t)$, monopolist 采用 PP, 仅 privacy-insensitive 消费者购买;
- (ii) 若 $\theta \geq t/(4V - t)$, monopolist 采用 uniform pricing, 所有消费者购买.

> **直觉**: PP 让 monopolist 完全提取每位到访消费者的剩余 (textbook first-degree price discrimination 的标配收益), 但代价是**驱赶**所有 privacy-sensitive 消费者 (因为他们到访就有 $-D$ 净效用, 没人会到). 这是一个简单的 trade-off: 单位消费者剩余提取 $\times$ 留下来的消费者比例 $(1-\theta) \times (V - t/4)$ vs. uniform 下 mark-down 但 mass 全部留下 $V - t/2$. 阈值 $t/(4V - t)$ 来自令两者相等. 这个阈值随 $V$ 增大而减小——产品估值越高, monopolist 越愿意放弃 PP 以保住市场.

**关键内涵**: 在 $\theta = 1$ 的极端情况下, PP 会让市场完全消失——这与 Anderson-Renault (2006) 中"广告若让消费者完全推断保留价就没人会买"的结论同构.

### 7.2 Proposition 2 (Monopoly, with Regulation)

**逻辑递进**: Prop 1 建立了"高 $\theta$ → 弃用 PP" 的基本结构. Prop 2 加入监管后, 比较新的阈值 $t/(2V - t)$ 与原阈值 $t/(4V - t)$.

**命题陈述**:
- (i) 若 $\theta < t/(2V - t)$, firm 采用 PP. 接受 tracking 的 privacy-insensitive 消费者中段 $[x_A^{P'}, x_B^{P'}]$ 付 PP 价格; 端点 $[0, x_A^{P'}] \cup [x_B^{P'}, 1]$ 的消费者 (含所有 privacy-sensitive 消费者中位置足够偏的) 付 uniform price $V/(1+\theta) > V - t/2$;
- (ii) 若 $\theta \geq t/(2V - t)$, firm 采用 pure uniform pricing.

> **直觉 (核心 trade-off)**: 监管把"必须给所有人 PP"的束缚松开了——企业现在可以**用 uniform price 这把锁**锁住承诺. 它可以一边对中段高需求消费者用 PP 榨取剩余, 一边给端点的 privacy-sensitive 消费者一个 (高于无监管 uniform price 的) 默认价. 阈值 $t/(2V-t) > t/(4V-t)$——监管严格扩大了 PP 适用范围. **这是 commitment value of regulation 的精确量化**.

**关键观察**: 监管下的 uniform price $V/(1+\theta) > V - t/2$ (即 laissez-faire 下的 uniform price). 监管不仅扩大 PP, 还**抬高了 uniform price**——这对那些选择拒绝 tracking 的 privacy-sensitive 消费者是直接伤害.

### 7.3 Proposition 3 (Monopoly Welfare)

**逻辑递进**: 给定 Prop 1 & 2 的均衡结构, 评估监管福利效应.

**命题陈述**: 以 $\theta$ 三段划分:
- (i) $0 < \theta < t/(4V - t)$ (两侧都 PP): 监管**提高**利润、消费者福利、社会福利;
- (ii) $t/(4V - t) \leq \theta < t/(2V - t)$ (无监管→U, 有监管→P): 监管提高利润, 但**降低**消费者福利和社会福利;
- (iii) $\theta \geq t/(2V - t)$ (两侧都 U): 监管无任何影响.

> **直觉**: Region (i) 是 PP **被**强制松绑——监管让 privacy-sensitive 消费者有了 uniform price 的逃生门, 同时端点的 privacy-insensitive 消费者也享受到了 uniform price 的好处 (因为 $V/(1+\theta) <$ 端点位置的 PP 价格 $V$). 帕累托改进. Region (ii) 是 PP **被**强制启动——监管诱导 monopolist 从 uniform 切换到 PP, 几乎所有消费者都被榨干剩余 (接受 tracking 的) 或被更高 uniform price 伤害 (拒绝 tracking 的). 帕累托劣化. Region (iii) 监管 not binding.

### 7.4 Proposition 4 (Duopoly, No Regulation)

**逻辑递进**: 引入竞争后, commitment problem 是否消失? 答案是: 被**缓解但未消除**.

**命题陈述**: 定义 $\hat{\theta} = t/(4(V-t))$, $\tilde{\theta} = (2V - 3t)/(2(V-t))$:
- (i) $\theta < \min\{\hat{\theta}, \sqrt{5}-2\}$ → $(P, P)$;
- (ii) $\min\{\hat{\theta}, \sqrt{5}-2\} \leq \theta < \tilde{\theta}$ → $(P, U)$ 或 $(U, P)$ (asymmetric);
- (iii) $\theta \geq \tilde{\theta}$ → $(U, U)$.

> **直觉**: $(P, P)$ 子博弈中, Bertrand-style 竞争把每位消费者的 PP 价格压到 $t(1 - 2x)$ (对最近的企业), 即使端点消费者也只付 $t < V - D$, 故有正净剩余——commitment problem 不出现, 因为竞争对手 *会* 抢顾客. $(P, U)$ 子博弈最有意思: PP 企业的 commitment problem **依然在**, 因为 uniform-price 企业 (firm B) 设定了一个 reservation 价格 $V - tx - p_B^{PU}$, 而 PP 企业 (firm A) 由于无法承诺补偿 $D$, 永远拿不到 privacy-sensitive 消费者. 当 $\theta$ 高时, $(U, U)$ 占优.

**关键比较**: $\tilde{\theta} > \min\{\hat{\theta}, \sqrt{5}-2\} > t/(4V - t)$. 意味着 duopoly 弃用 PP 的参数范围**严格窄于** monopoly——**竞争扩大 PP 的使用**.

### 7.5 Proposition 5 (Duopoly, with Regulation): 最反直觉的核心结果

**逻辑递进**: 监管在 monopoly 中扩大 PP, 在 duopoly 中是否会进一步? 答案不仅是 yes, 还增加了一个非单调结果.

**命题陈述**: 定义 $D^* = \frac{t}{2+\theta}\sqrt{(7\theta^2 + 4\theta - 2)/\theta}$:
- (i) 若 $\theta \leq (3\sqrt{2} - 2)/7$, 或 $\theta > (3\sqrt{2} - 2)/7$ 且 $D > D^*$ → $(P', P')$;
- (ii) 若 $\theta > (3\sqrt{2} - 2)/7$ 且 $D \leq D^*$ → asymmetric $(P', U')$.

**关键观察**: $(U', U')$ 在监管下**不再是均衡**——至少有一家企业必上 PP.

> **直觉**: 监管给两家企业都解锁了 commitment 工具. 在 $(P', U')$ 子博弈中, PP 企业现在能通过 uniform price 留住 privacy-sensitive 消费者, 不再被 commitment problem 困死. 这让 unilateral PP 比无监管时更有利可图, 从而瓦解 $(U, U)$ 均衡.

**反直觉点**: $D$ **越大**, PP 越普遍 (在 $\theta$ 高的区域). 原因: 在 $(P', P')$ 中, 更大的 $D$ 让更多 privacy-sensitive 消费者拒绝 tracking 并支付更高的 uniform price (而非更低的 PP price), 反而**提高**每家企业利润 ($\Pi^{P'P'} = t/4 + \theta D^2 / 4t$). 因此从 $(P', U')$ 偏离到 $(P', P')$ 变得更划算.

### 7.6 Proposition 6 (Duopoly Welfare)

**命题陈述**:
- (i) $\theta < \min\{\hat{\theta}, \sqrt{5}-2\}$ (region I): 监管同时提升 industry profit、consumer welfare、social welfare. (双赢)
- (ii) $\theta \geq \min\{\hat{\theta}, \sqrt{5}-2\}$ (regions II, III, IV): 监管降低 industry profit, 提升 *总体* consumer welfare, 但部分消费者效用降低. 社会福利在 II, III 区上升, 在 IV 区 ($\theta \geq \tilde{\theta}$) 下降.

> **直觉**: Region I 中, 监管创造了 uniform-price 这个新选项, 不改变 PP 价格 (因为竞争已经把 PP 推到最低), privacy-sensitive 消费者纯获利, 企业从 uniform price 端获利. Region IV 中, 监管把所有人从 (U, U) 推到 (P', P'), 大量本来享受 uniform price 福利的消费者被切换到 PP, 加上中间段消费者付出 disutility $D$, 总福利下降.

### 7.7 关键 trade-off: 全文最核心的张力

> **PP 的事后利润提取 vs. privacy-sensitive 消费者的事前退出**.
>
> Monopolist 想榨干每位消费者剩余, 但它的"事后机会主义"被 privacy-sensitive 消费者**预见**, 后者干脆不来. 这一**未来理性预期对当前激励的反作用**, 是全文的核心机制. 竞争 / 监管的作用都可以**精确**地通过"它们提供了什么 commitment 工具"来刻画.

**为什么这是 reframe 而不是简单 trade-off**: 传统 PP 文献的核心矛盾是"价格歧视 → 提高利润 vs. 加剧竞争 → 降低利润" (Thisse-Vives), 这是企业**之间**的张力. 本文的核心矛盾是**企业与自己事后行为**的张力——commitment 问题. 这个 reframe 让监管的反讽效果获得了一个干净的机制解释.

### 7.8 Extension 简述

**(E1) 不对称企业 (Section 6.1)**: $V_A > V_B$, $\Delta V < t - D$. Proposition 7 给出一个 baseline 没有的新结论: 当 $D > D^*$ 且 $\theta$ 足够大时, 监管**降低所有消费者**效用 (而非只是 baseline 中的 region II 中"部分消费者"). 机制: firm B (低质量) 放弃 privacy-insensitive 消费者, 只服务 privacy-sensitive 消费者, 抬高 uniform price; 战略互补性使 firm A 也涨价, 所有消费者受损.

**(E2) 不完全市场覆盖 (Section 6.2)**: $V \in (t/2, 2t/3]$. 当 $\theta = 0$, 复制 Rhodes-Zhou (2024) "低覆盖下 PP 提高利润" 的结论. 当 $\theta > 0$, baseline 主结论稳健; 监管下两家企业**均**采用 PP 对任何 $\theta \in (0, 1)$.

**(E3) Alternative timing (Section 6.3)**: 改 stage 3 为"先决定授权再披露 uniform price". 求解概念改为 PBE. 多重均衡, 但 baseline 的均衡结果是 PBE 中**企业利润最大**的一个. 这为 baseline 的 timing assumption 提供了 microfoundation——如果企业能内生选择何时披露价格, 它**会选择**先披露.

---

## 8. 比较静态汇总表

| 参数变化 | 对 PP 使用范围的影响 | 对消费者福利的影响 | 直觉 |
|:---|:---|:---|:---|
| $\theta \uparrow$ | $\downarrow$ (单调) | 取决于 $\theta$ 区间 | 更多 privacy-sensitive 消费者放大 commitment problem 的代价 |
| 引入 consumer control | $\uparrow$ (扩大) | Monopoly: $\downarrow$ in region II; Duopoly: 总体 $\uparrow$, 但 region IV 可能 $\downarrow$ social welfare | 监管解锁 commitment 工具 |
| 由 monopoly → duopoly | $\uparrow$ (扩大) | uniform price 下降, 但 PP 价格也下降 | 竞争缓解 commitment problem |
| $D \uparrow$ (in duopoly, with reg) | $\uparrow$ (在 $\theta$ 高区域) | 复杂 | 更大 $D$ 推更多消费者去拒绝 tracking 并付 uniform price, 抬高 $\Pi^{P'P'}$ |
| $V \uparrow$ | $\downarrow$ (阈值 $t/(4V-t), t/(2V-t)$ 随 $V$ 下降) | $\uparrow$ | 高估值时 monopolist 越倾向于 uniform pricing 以扩张市场 |

---

## 9. 主要结论与管理启示

### 9.1 与 Benchmark / 现有直觉的对比

| 维度 | Benchmark (Armstrong 2006, Thisse-Vives 1988) | 本文发现 | 为什么重要 |
|:---|:---|:---|:---|
| Monopolist 是否总用 PP? | 是, dominant strategy | 否, 当 $\theta$ 高时弃用 | 内生隐私偏好改变 PP 决策 |
| Duopoly 中 PP 是否 dominant? | 是 | 否, 仅当 $\theta$ 小时 | 同上, 且竞争**不**消除 commitment problem |
| 竞争是否保护隐私? | 普遍信念: 是 | 否, 竞争扩大追踪 | 颠覆"市场即保护"的传统乐观 |
| 隐私监管是否减少追踪? | 显见直觉: 是 | 否, 监管反而扩大追踪 | 政策反讽: 监管的承诺工具效应主导 |
| 监管是否提升消费者福利? | 显见直觉: 是 | 不总是; monopoly region II 中**降低** | 监管设计需考虑 $\theta$ 异质性 |

### 9.2 管理建议

1. **对追踪技术投资决策**: 在评估 PP 收益时, 不要只看每位消费者的 surplus extraction 上限; **必须**估计市场中 privacy-sensitive 消费者的占比 $\theta$. 当 $\theta$ 超过 $t/(4V-t)$ 阈值, PP 的预期收益可能为负 (因为 sensitive 消费者集体退出).
2. **对低估值市场尤其要小心**: 阈值 $t/(4V-t)$ 在 $V$ 较小时较大. 但 $V$ 越小, 即使 $\theta$ 略高也可能使 PP 不划算. 管理者应在 ROI 模型中显式建模 sensitive 消费者占比.
3. **隐私监管的合规策略**: 当监管 (GDPR-style) 落地, 实际上**降低了**采用追踪技术的风险——企业可以放心上 PP, 并通过设定较高的 default uniform price 实现 segmentation. 这与"监管 = 成本"的合规心智模型相反.
4. **对低质量企业**: 在异质质量市场, 监管可能反而帮你抬高 uniform price (因为你可以"放弃"privacy-insensitive 消费者, 专门服务 privacy-sensitive 消费者). 这是一个 niche 战略.
5. **对监管制定者**: 在 $\theta$ 较高的市场设计 consumer control 型监管时, 应预期到追踪技术使用反而扩大, 并补充其他工具 (如限制 personalized prices 的范围, 或要求 transparency)——单纯"同意"机制不足以保护隐私.

---

## 10. 与相关文献的对话

### 10.1 vs. Thisse and Vives (1988, AER)

**共同关注**: Hotelling 下两厂商 PP vs. uniform pricing 的内生选择.
**本文区别**: T-V 中 PP 是 dominant strategy, 全市场完全覆盖. 本文引入 $\theta > 0$ 后, $(U, U), (P, U), (P, P)$ 三种均衡都可能出现.
**为什么重要**: T-V 是几乎所有后续 PP 文献的 anchor. 本文证明 T-V 结论在引入 intrinsic privacy preferences 后**根本性地**改变. 这是一个对该领域基本设定的修正性贡献.

### 10.2 vs. Rhodes and Zhou (2024, AER)

**共同关注**: 寡头市场中 PP 的均衡效应, 特别是 PP 对竞争强度的影响.
**本文区别**: R-Z 强调"市场覆盖率"对 PP 福利效应的关键作用——低覆盖率下 PP 提高利润, 高覆盖率下 PP 降低利润. 本文则关注内生消费者类型 (privacy-sensitive vs. insensitive) 如何改变 PP 的**采用决策** (而非给定采用后的效应). Section 6.2 显示, 即使在低覆盖率下 (Rhodes-Zhou 显示 PP 应该是吸引人的), 引入 $\theta > 0$ 后企业仍可能放弃 PP——这是对 R-Z 框架的实质性挑战.
**为什么重要**: 这对 **Jinyi 的 MS 提交直接相关**——R-Z (2024) 是你 paper 的核心 benchmark, Chen-Zhang 这篇为"在 R-Z 框架上推进一步"提供了一个新维度 (内生消费者偏好). 可考虑在 referee response 中引用这一点.

### 10.3 vs. Ichihashi (2020, AER) 与 de Cornière-Montes (2017, RNE)

**共同关注**: monopolist 在某些条件下会**自愿**承诺不进行 PP.
**本文区别**: Ichihashi / dCM 的承诺机制是"以承诺不歧视换取消费者披露信息, 用于产品推荐 / 定制". 本文的机制完全不同——*没有*额外的数据用途, monopolist 弃用 PP 是因为 commitment problem 的 ex-ante 投资角度: 它无法承诺不榨干 privacy-sensitive 消费者, 后者干脆不来. 两套机制在数据用途单一 (PP only) 时, 只有本文的 commitment problem 能解释弃用 PP 的现象.
**为什么重要**: 揭示了"firms commit not to price-discriminate"这一现象的**第二种**理论 microfoundation, 与 Ichihashi 互补而非替代.

### 10.4 vs. Choe, Matsushima, Shekhar (2025, MS) 与 Choe, King, Matsushima (2018, MS)

**共同关注**: 数字隐私 + 寡头竞争.
**本文区别**: Choe et al. (2025) 研究在线平台双边盈利 (服务 + 数据变现), 监管效应依赖两种收入来源的相对重要性. 本文只有一个收入来源 (产品销售), 监管效应通过 PP vs. uniform 的策略切换实现. 两套机制平行而非冲突. Choe-King-Matsushima (2018) 研究 behavior-based price discrimination, 与本文的 first-degree PP 不同.
**为什么重要**: Chen-Zhang 为"内生隐私偏好 + 数据收集"这一交集提供了一个不依赖 two-sided market 结构的极简模型, 隔离出 commitment problem 这一单一机制.

---

## 11. Reviewer's Critique

### 11.1 Major Concerns

**M1. Commitment 假设的脆弱性 (核心驱动假设)**.
论文的所有结论都建立在 "firms cannot commit to personalized prices ex ante" 之上. 作者在 footnote 14 承认这一点, 并提到"voluntary commitment 不可信"作为 footnote. 但: (i) 现实中, 大量平台正在通过"price match guarantees"、"published pricing rules"、long-term contracts 实现某种程度的承诺; (ii) reputation 机制在 repeated game 中可以替代 explicit contract; (iii) 算法定价的可审计性 (algorithmic accountability) 在新一代 AI 监管下正在变得 enforceable. 若 commitment 部分可信, 本文的反讽效应会被大幅削弱. 作者应该在主文 (而非 footnote) 系统讨论 commitment power 的连续谱, 并展示哪些核心结论对部分 commitment 仍稳健.

**M2. $D$ 的统一性 (homogeneous privacy cost)**.
模型假设所有 privacy-sensitive 消费者共享相同的 $D$. 在 footnote 15 中作者提到考虑了 $D$ 连续分布的扩展, 并声称结论 robust. 但这一点的处理过于单薄——connecting 到 Lin (2022) 的实证证据时, intrinsic preferences 的方差是巨大的 (\$0.14 ~ \$2.37). 若 $D$ 是连续分布的, $(P', P')$ 子博弈中接受 vs. 拒绝 tracking 的 cutoff 会有意思得多, 且监管的福利效应可能定量上 (而非定性上) 大幅改变. 建议作者在 main text 给出该扩展的关键命题, 而不是只放在 appendix.

**M3. 与 Anderson, Baik, Larson (2023, RES) 的关系处理不足**.
作者在 literature 中区分了"personalized discounting"和"personalized pricing", 但区分的论据相对薄弱 ("quasi-monopoly trade-off"). 实际上, 大量真实平台 (Amazon, Uber, 航空公司) 的 PP **就是**通过 list price + targeted discount 实现. 若读者认为本文模型其实是 personalized discounting 的特例, 那么 commitment problem 故事就会与 Anderson et al. (2023) 的 framework 直接冲突——后者明确假设 firms commit to personalized discounting. 作者需要给出一个更明晰的区分: 在什么实际制度安排下, Chen-Zhang 模型适用而 Anderson et al. 不适用?

**M4. 福利分析缺乏 distributional sensitivity**.
Proposition 6 (ii) 说"监管提升总体 consumer welfare 但伤害部分消费者". 在 monopoly Region II 中, 监管严格降低社会福利. 但论文未给出对**哪些消费者**受益、**哪些消费者**受损的细致分析 (除了 appendix 中一些数学). 政策制定者需要的是: "在什么 $\theta$ 范围内, 什么类型的消费者会变差?" 一个清晰的可视化 / 表格能极大提升 policy relevance.

**M5. Monopoly model 中"独家销售双产品"的合理性**.
作者假设 monopoly market 中单一企业同时卖 A 和 B (两条 Hotelling 末端). 这相当于 textbook spatial monopoly, 但与 duopoly 模型对接时 (一个企业 → 两个企业) 显得有些 ad hoc. 现实中 monopoly 往往意味着单一产品或多产品组合不在两端. 若 monopoly 只卖一个产品 (例如位于中点), 结论是否还成立?

### 11.2 Minor Concerns

**m1.** Tiebreaker assumption (Section 3.4) 中"若消费者对接受/拒绝 tracking 无差异, privacy-sensitive 拒绝、privacy-insensitive 接受", 这看起来人为选择有利于结果. 应该测试 robustness.

**m2.** Section 4.2 的几何图 (Figure 1) 解释清晰, 但 Section 5 的 duopoly 几何缺少类似的可视化, 增加阅读难度.

**m3.** 异质企业 extension (Section 6.1) 仅给出 Proposition 7 (一个负面结果). 但同方向其他效应 (例如 firm B 的 niche strategy 是否在 $D < D^*$ 时也存在?) 未充分展开.

**m4.** $D < t$ 的假设虽然有实证支持, 但论文未讨论 $D \to t$ 极限的连续性. 若 $D$ 接近 $t$, 模型中的 cutoff 会非线性地变化吗?

**m5.** PBE 部分 (Section 6.3) 选择 "firm-profit-maximizing PBE" 的依据较弱. 在 Ichihashi (2020) 中也用了类似 selection criterion, 但本文应说明为什么 consumer-best PBE 不被选择, 这会影响监管福利分析.

### 11.3 Future Research

**F1. Commitment Power 的内生选择**: 假设企业可以投资某种 commitment 技术 (e.g., 公开发布算法、第三方审计), 这种投资如何与 PP 决策交互? 自愿 commitment 在何种 $\theta$ 区间会被企业内生选择?

**F2. Dynamic Privacy Game**: 当前模型是一次性的. 在 multi-period 设定中, reputation 是否能内生取代 explicit commitment? 此时监管的承诺效应是否被削弱? 这与 BBPD 文献 (Choe-King-Matsushima 2018, Fudenberg-Tirole 2000) 有自然连接.

**F3. 多维消费者类型**: 当前只有"sensitive / insensitive"二元类型. 实际消费者的隐私偏好与价格敏感度可能相关 (高收入者既高估隐私又低价敏). 引入 ($\theta, $ 价格敏感度) 联合分布会如何改变结论? 这与 Fu et al. (2025, MS) 多维 personalized pricing 的 framework 有自然衔接.

**F4. 数据二次使用与隐私监管的交互**: 当数据除了 PP 还能用于产品定制 (cf. de Cornière-Montes 2017) 或推荐 (cf. Ichihashi 2020), commitment problem 与 information disclosure incentive 如何**联合**塑造均衡? 这是本文最直接的扩展.

**F5. 与产品定制 / Module-Level Personalization 的整合**: 若企业既可以做 personalized pricing, 也可以做 personalized product features (例如 Jinyi 的 customization level $k_i$), commitment problem 是否依然存在? **猜想**: customization 与 PP 是两类完全不同的"data-monetization"路径, 前者给消费者带来正效用 ($+$utility from fit), 后者带来负效用 ($-$surplus extraction). 当两者并存时, monopolist 可能能用 customization 的正向效用补贴 PP 的负向效用, 解决 commitment problem. 这正好是 Jinyi 的 MS 提交可以延伸的方向.

**F6. 实证检验**: 当前所有结论都是 theoretical. 一个自然的实证设计: 利用 GDPR 实施前后 (2018) 在不同 $\theta$ 水平的市场中 (如美国 vs. 欧洲, 或高隐私意识行业 vs. 低意识行业), 检验追踪技术采用率是否如本文预测**扩大** (而非缩小).

---

## 12. 对你 (Jinyi) 的研究的几点连接 (我的解读, 非作者原文)

> 以下是我作为"reviewer + thinking partner"对本文与你正在做的 MS 提交之间关联的额外思考, 不属于本文作者原意.

1. **Commitment problem 与你的 customization 模型**: 你的 paper endogenize 了 customization level $k_i$. 一个自然的问题是: 当 $k_i < 1$ 时 (部分 customization), 企业是否也面临"无法承诺给某些消费者非负净剩余"的 commitment problem? 不同于本文的 privacy cost, 在你的框架中 commitment 问题可能体现为"承诺**不**用 customization 数据进行 surplus extraction"——这是与 Laussel-Resende (2022) **隐含**的 fully-commitment 假设的另一个区分维度.

2. **Referee response 的可能弹药**: Chen-Zhang 直接为"PP 决策的内生性影响竞争结构"提供了顶刊先例. 若 referee 质疑你的 "endogenous regime choice between uniform 和 personalized customization", Chen-Zhang 提供了一个清晰的 anchor: PP 文献已经从"PP 是 dominant strategy" (Thisse-Vives 1988) 走到"PP 决策内生" (Chen-Zhang 2026). 你的 paper 是这一进程在 customization 维度的自然延续.

3. **A unifying observation**: Rhodes-Zhou (2024) 的低覆盖率结论, Chen-Zhang (2026) 的高 $\theta$ 弃用结论, Fu et al. (2025) 的多维 PP 结论, 看似分散, 但共同指向"**经典 Thisse-Vives 的'PP 是 dominant strategy'结论在引入足够丰富的消费者异质性后会瓦解**". 你的 paper 在 customization 维度也呈现类似的瓦解模式 (从 $k_i = 1$ 的 corner 走向 $k_i \in (0, 1)$ 的内部解). 这是一个 review article 级别的 unified narrative, 也是你在 introduction 中可以借势的高地.

4. **One thing to investigate**: Chen-Zhang Section 6.1 的不对称企业结论中, firm B "放弃 privacy-insensitive 消费者, 专门服务 privacy-sensitive 消费者". 这与你 paper 中可能的 niche customization strategy (一家企业全 customization 服务 high-fit 消费者, 另一家 mass-produce) 有结构上的同构. 如果两者数学上是同一类机制 (strategic complementarity in pricing under asymmetric segment service), 这是一个非常漂亮的 cross-paper connection, 可放入 literature dialogue.

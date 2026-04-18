# Platform Governance and Information Disclosure in Markets with Add-Ons

**作者**：Huixin She (Toulouse School of Economics)
**年份**：2026
**期刊**：Working Paper (TSE / IIOC 2026)

## 摘要（中文翻译）

本文研究在消费者短视 (consumer myopia) 存在的情况下，平台的从价佣金 (ad-valorem commission) 与治理策略如何决定市场的信息透明度。我们建模卖家策略性地隐藏 (shroud) 附加品 (add-ons) 以将其转移至平台外销售，从而规避平台佣金。我们分析了自由放任 (laissez-faire) 政策下的市场结果，并与强制披露政策进行对比。核心发现揭示了一个新机制：**从价佣金充当"竞争放大器" (competition multiplier)**——卖家通过降低基础商品价格，将无佣金的附加品利润传递给消费者，从而对基础商品形成隐性补贴。因此，隐藏费用的市场可能比透明市场产生更高的消费者剩余。这一发现揭示了透明度监管的一个意外后果：强制披露可能通过消除这些隐性补贴而损害消费者利益。

---

## 1. 论文速览

| 维度 | 内容 |
|:---|:---|
| **研究问题** | 在 ad-valorem 佣金下，平台如何通过治理策略（是否强制披露 add-on 价格）影响市场透明度、消费者福利与社会福利？透明度监管是否一定有利于消费者？ |
| **研究方法** | 理论建模：两个差异化卖家的双寡头博弈 + 单平台中介 + 异质消费者（sophisticated vs. myopic）；Perfect Bayesian Equilibrium |
| **核心机制** | **Commission-as-competition-multiplier**：off-platform 的 add-on 利润 $\alpha R$ 被卖家以放大系数 $\frac{1}{1-\gamma}$ 竞价传递至 on-platform 的基础商品价格中 |
| **反直觉发现** | 当 $\gamma$ 与 $\alpha$ 都足够大时，shrouding 均衡的总消费者剩余（甚至 myopic 消费者的剩余）**高于**透明均衡 |
| **主要贡献** | ① 将 Gabaix-Laibson (2006) 的一对一交叉补贴推广为"被佣金放大的交叉补贴"；② 刻画平台的最优 disclosure mandate；③ 揭示 DMA 式"透明+解绑"政策的意外副作用 |
| **适用场景** | OTA（Expedia、Booking）+ 航司行李费；酒店+餐饮/水疗；App Store + IAP；Amazon Marketplace |

---

## 2. TL;DR

**一句话**：平台收的比例佣金会把"隐藏附加费"的竞争压力加倍传导到基础商品价格上——所以隐藏费反而可能让消费者净赚，强制透明化有时反而把消费者坑了。

**两句话**：在带抽成的平台上，卖家把附加品（行李费、清洁费等）搬到站外卖以规避佣金，再用这笔 commission-free 的利润去打基础商品价格战——因为基础商品还要被抽 $\gamma$，每向消费者转移 1 元附加利润就要降 $\frac{1}{1-\gamma}$ 元基础价。这个放大机制可能让"隐藏费用 + 低基础价"的世界比"完全透明"的世界对消费者更友好，这也解释了为什么 DMA 式的透明度强制令可能好心办坏事。

---

## 3. One More Thing（前置 Hook）

**佣金不是税，是一个"麦克风"。**

经典的 Gabaix-Laibson (2006) 讲了一个朴实的故事：竞争市场上，隐藏的附加费会被卖家通过基础价降价"一对一"地退给消费者——拿回来的恰好等于藏进去的，所以对 sophisticated 消费者是 wash，对 myopic 消费者是净损失。

She 的这篇论文往这个故事里塞进了一个看似微不足道的制度细节：平台抽的是 ad-valorem commission，而不是固定费。结果整个叙事发生了反转。

想象一下：卖家在 Booking.com 上卖酒店房，平台抽 20%。卖家把清洁费藏起来，到前台再收——这笔钱完全绕开了佣金。现在双寡头竞争迫使卖家把这笔 "off-platform" 利润全部让给消费者。但让利只能通过降低基础房价来实现，而基础房价**还在平台上、还要被抽 20%**。于是数学变成了：卖家每想让消费者白得 1 元，就必须把基础房价砍掉 $1/(1-0.2) = 1.25$ 元。佣金越高，这个放大系数越大。

**最精妙的地方是**：这个放大机制在 sophisticated 消费者和 myopic 消费者之间是共享的——myopic 消费者虽然被隐藏费坑了 $R$，但他们也和 sophisticated 消费者一样享受了被放大的基础商品降价 $\frac{\alpha R}{1-\gamma}$。当 $\gamma \geq 1-\alpha$ 时，连 myopic 消费者都在 shrouding 均衡里净赚。

**推论**：EU 的 Digital Markets Act 同时做了两件事——强制透明 **and** 禁止 anti-steering（允许站外销售）。前者取消 shrouding，后者让卖家可以把 add-on 搬出平台。这两件事合起来恰好落在本文 pu-R 或 pu-e 均衡，在 $\alpha$ 大的区域里**同时是社会福利最差和消费者福利最差**的结局。监管的善意被机制吞了。

---

## 4. 研究背景与动机 (Motivation)

### 实践痛点

- **OTA 与航司**：Expedia、Booking、Trip.com 向航司收取基础票价的佣金（15%–30%），航司则系统性地把行李费、选座费、机场值机费从平台页面剥离，只在自家官网收取。美国 DOT 在 2022–2023 年的 *Enhancing Transparency of Airline Ancillary Service Fees* 规则制定中，Travel Technology Association 正式作证指出这一现象。
- **酒店与平台**：Booking 获客，但餐饮、水疗、停车在前台直售——客人一旦 check-in 就被锁定。
- **App Store 与 Amazon**：anti-steering 条款禁止开发者/卖家引导交易至站外，保护佣金收入。
- **监管方向**：EU DMA Article 5(7) 要求允许 steering；EU Consumer Rights Directive 与 FTC *Rule on Unfair or Deceptive Fees* 要求 all-in 定价。Airbnb 在 2025 年 4 月全球默认 total price display。

### 理论缺口

- **Gabaix & Laibson (2006)**：shrouding 下的交叉补贴是 **one-for-one** 且无放大的，myopic 消费者永远受损。
- **Geng, Tan & Wei (POM 2018)**：在平台佣金下研究垄断卖家的 add-on bundling，但 (i) 所有消费者 myopic，(ii) 无竞争，(iii) 无 shrouding 选择。
- **Johnen & Somogyi (EJ 2024)**：平台收固定会员费时，**平台本身**有隐藏 add-on 的激励（opacity 抬高感知剩余进而抬高会员费）。
- **缺口**：没有论文把"比例佣金 + 双寡头竞争 + 异质消费者 sophistication + 平台 disclosure mandate"同时装进一个模型。

### 核心贡献

1. **新机制**：识别 ad-valorem commission 作为 competition multiplier 的角色，将 G-L (2006) 的一对一交叉补贴推广为放大 $\frac{1}{1-\gamma}$ 的交叉补贴。
2. **反直觉福利结论**：shrouding 可以对所有消费者类型（含 myopic）都严格更优，这在 G-L 框架中不可能。
3. **平台治理刻画**：平台的 disclosure mandate 选择纯粹由佣金收入驱动，与消费者福利系统性错位。
4. **政策警示**：DMA 式的"透明 + 解绑"组合可能触发最差结局（pu-R）；commission cap 和 consumer education 是互补而非替代工具。

---

## 5. 模型设定与假设

### 5.1 玩家与行动

**三类玩家**：两个卖家 $i \in \{A, B\}$、一个垄断平台、单位质量的消费者。

### 5.2 符号体系（按模块分组）

#### 模块 A：卖家与产品

| 符号 | 含义 | 备注 |
|:---|:---|:---|
| $p_i$ | 卖家 $i$ 的基础商品价格 | 决策变量 |
| $\hat{p}_i$ | 卖家 $i$ 的附加品价格 | 决策变量 |
| $c$ | 基础商品边际成本 | 足够大以保证价格为正 |
| 0 | 附加品边际成本 | 标准化 |

#### 模块 B：平台

| 符号 | 含义 | 备注 |
|:---|:---|:---|
| $\gamma \in (0,1)$ | ad-valorem 佣金率 | 外生；仅对 on-platform 交易征收 |
| $\Pi_P$ | 平台利润 | = $\gamma \times$ on-platform 交易额 |

#### 模块 C：消费者异质性

| 符号 | 含义 | 备注 |
|:---|:---|:---|
| $\alpha \in (0,1]$ | myopic 消费者占比 | 核心参数 |
| $1-\alpha$ | sophisticated 消费者占比 | 理性预期 add-on 价 |
| $\lambda \in [0,1)$ | 短视持续性 | unshrouding 后仍有 $\alpha\lambda$ 的 myopic 未被转化 |
| $V$ | 基础商品估值 | 市场完全覆盖 |
| $R$ | add-on 保留价值 | $R > e$ |
| $e$ | 替代成本 | $0 < e < R$（$e > R$ 情形见 Appendix C） |
| $x_i = \epsilon_{iB} - \epsilon_{iA}$ | B 相对 A 的偏好冲击 | 分布 $F(\cdot)$ 对称、log-concave |

#### 模块 D：策略标签（Extension 引入）

| 前缀 | 含义 |
|:---|:---|
| `LF` | laissez-faire（bundled：disclosure 与 sales channel 绑定） |
| `ps` | platform mandates shrouding |
| `pu` | platform mandates unshrouding |
| 后缀 `s/u` | 卖家的 disclosure 行动 |
| 后缀 `e/R` | pu 下卖家的 add-on 定价 |

### 5.3 消费者效用与需求

**Sophisticated 消费者**（理性预期 add-on 价格）：

$$
u_{ij}^{\text{soph}} = V + R - p_j - \min\{\hat{p}_j, e\} + \epsilon_{ij}
$$

> **直觉**：sophisticated 消费者预见到 add-on 阶段会面临 $\hat{p}_j$；若 $\hat{p}_j > e$，则提前花 $e$ 替代掉；因此实际支付 $\min\{\hat{p}_j, e\}$。

**Myopic 消费者**（忽略 add-on 价格）：

$$
u_{ij}^{\text{myop}} = V - p_j + \epsilon_{ij}
$$

> **直觉**：myopic 在 Stage 2 只比较 $p_j$，到 Stage 3 被锁定，任何 $\hat{p} \leq R$ 都照单全收。这是锁定效应 (lock-in) 的数学刻画。

### 5.4 卖家目标函数（以 Case 2：A shrouds, B unshrouds 为例）

$$
\Pi_A = (1-\alpha\lambda)\left[(1-\gamma)p_A + \mathbf{1}_{\{\hat{p}_A \leq e\}}\hat{p}_A - c\right] D_A^{\text{soph}} + \alpha\lambda\left[(1-\gamma)p_A + \mathbf{1}_{\{\hat{p}_A \leq R\}}\hat{p}_A - c\right] D_A^{\text{myop}}
$$

> **直觉**：第一项——sophisticated 消费者贡献；基础商品在平台上抽佣（$1-\gamma$），add-on 因 A shroud 故 off-platform 不抽佣（$\hat{p}_A$ 系数为 1 而非 $1-\gamma$）。第二项——$\alpha\lambda$ 的 uninformed myopic 消费者；他们只看 $p_A$ 选卖家，到 add-on 阶段无差别支付至 $R$。**关键对比**：Case 1（A unshrouds）中 $\hat{p}_A$ 的系数是 $(1-\gamma)$，Case 2 中是 $1$——这就是 commission saving。

### 5.5 博弈时序

1. **Stage 1**：卖家同时决定 $(p_i, \hat{p}_i)$ 与 shroud/unshroud。
2. **Stage 2**：消费者观察可见价格并选卖家；sophisticated 决定是否付 $e$ 替代。
3. **Stage 3**：shrouded add-on 价格揭示；未替代消费者决定是否购买 add-on。

### 5.6 关键假设

**A1. Bundled disclosure + anti-steering**（基线）：卖家要用平台的 disclosure 工具，就必须在平台上结算并付佣金。

> *合理性*：反映 App Store、Amazon 等平台的 anti-steering 条款。
> *放松影响*：Extension 部分即通过解绑这两者来模拟 DMA。

**A2. 外生佣金率 $\gamma$**：平台跨市场统一定价。

> *合理性*：实证上平台通常对数千个市场用同一费率。
> *放松影响*：内生化 $\gamma$ 会引入双边市场的额外权衡，但核心 multiplier 机制保留。

**A3. Add-on 锁定**：一旦购买基础商品，除非提前付 $e$ 替代，否则 add-on 不可避免。

> *合理性*：机场行李费、前台服务的典型特征。
> *放松影响*：若 ex-post 可退出，卖家无法提取 $R$，shrouding 均衡收缩。

**A4. $\epsilon_{ij}$ 的分布 $F$ 对称且 log-concave**：保证 FOC 有唯一对称均衡解 $F(0) = 1/2$。

---

## 6. 分析路线图

本文的分析呈现清晰的三步递进结构：

1. **Baseline (Section 2)**：Bundled laissez-faire 平台。卖家**同时**选择 disclosure 和 sales channel（两者绑定）。刻画两个对称均衡：LF-u 与 LF-s，以及它们的存在区域（由阈值 $\underline{\alpha}$ 和 $\bar{\alpha}$ 界定）。识别 commission multiplier 机制。

2. **Extension (Section 3)**：解绑 disclosure 与 sales channel。平台选 mandate（ps 或 pu），卖家独立选 channel。由于 off-platform 销售对卖家严格占优，Stage 2 的博弈塌缩为 add-on 定价选择（$e$ 还是 $R$）。引入两个新均衡：pu-e 与 pu-R。求解平台的最优 mandate（Proposition 2–3）。

3. **Welfare & Policy (Section 3.2 + 4)**：建立关键的**支配关系** $CS^{pu\text{-}e} \geq CS^{LF\text{-}u}$ 与 $CS^{LF\text{-}s} \geq CS^{pu\text{-}R}$，将四均衡比较简化为 LF-s vs. pu-e。刻画平台治理与消费者福利的系统性错位，讨论 commission cap、transparency mandate、consumer education 三种政策工具的适用区间。

---

## 7. 核心分析与求解

### 7.1 Baseline：Laissez-Faire 下的两均衡（Lemma 1）

**预备引理**（Appendix 中 Lemma 0.1–0.5 的实质）：
- 若要服务所有消费者类型 → 必须 unshroud + 定价 $\hat{p} = e$（否则 sophisticated 替代掉）。
- 若只服务 myopic → 必须 shroud + 定价 $\hat{p} = R$（完全榨取保留价值）。
- 完全不卖 add-on 严格被劣。

**Lemma 1（均衡存在条件）**：

- **Unshrouding 均衡**（LF-u）存在当且仅当 $\alpha \leq \bar{\alpha} \equiv \frac{e(1-\gamma)}{\lambda R}$：

$$
p^u = \frac{c}{1-\gamma} - e + \frac{1}{2f(0)}, \quad \hat{p}^u = e
$$

- **Shrouding 均衡**（LF-s）存在当且仅当 $\alpha \geq \underline{\alpha} \equiv \frac{e(1-\gamma)}{R}$：

$$
p^s = \frac{c - \alpha R}{1-\gamma} + \frac{1}{2f(0)}, \quad \hat{p}^s = R
$$

两均衡中卖家利润相同，均为 $\frac{1-\gamma}{4f(0)}$。

> **经济学直觉（核心机制）**：在 LF-u 中，add-on 与基础商品**都**在平台上、都抽佣 $\gamma$，竞争导致的 pass-through 是**一对一**的：$p^u$ 比"无 add-on"基准降了恰好 $e$。在 LF-s 中，add-on 在平台外（不抽佣），但基础商品仍抽佣 $\gamma$。要把 1 元 off-platform 利润让渡给消费者，必须通过基础商品降价 $\frac{1}{1-\gamma}$ 元。因此 $p^s$ 比"无 add-on"基准降了 $\frac{\alpha R}{1-\gamma}$——**佣金越高，放大倍数越大**。
>
> 两个阈值的直觉：$\underline{\alpha}$ 界定"myopic 足够多，$\alpha R$ 的隐藏利润超过 $(1-\gamma)e$ 的 on-platform 透明收益"——低于此值卖家会想偏离到 unshroud；$\bar{\alpha}$ 界定"unshroud 时单独偏离到 shroud 抓 $\alpha\lambda$ myopic 的利得"——高于此值 unshroud 均衡崩溃。两阈值都随 $\gamma$ 递减：佣金越高，off-platform 越香，shrouding 越好维持。

**Proposition 1（消费者福利比较）**：相对 LF-u：

> Proposition 1 建立了 shrouding 均衡对不同消费者群体福利的条件。由于放大机制的存在，三类消费者的福利阈值呈现严格排序。

(i) **Sophisticated**：$CS^s_{\text{soph}} > CS^u \Leftrightarrow \alpha \geq \underline{\alpha}$（即 shrouding 均衡存在的条件）。
(ii) **总消费者**：$CS^s > CS^u \Leftrightarrow \alpha \geq \tilde{\alpha} \equiv \frac{e(1-\gamma)}{\gamma R + (1-\gamma)e}$。
(iii) **Myopic**：$CS^s_{\text{myop}} > CS^u \Leftrightarrow \alpha \geq 1 - \gamma$。

严格排序 $\underline{\alpha} < \tilde{\alpha} < 1 - \gamma$，三者**均随 $\gamma$ 递减**。

> **经济学直觉**：Sophisticated 消费者白嫖了放大降价、又用 $e$ 替代躲掉 add-on，所以只要 shrouding 均衡存在他们就赢。总福利的阈值要求放大降价 $\frac{\alpha R}{1-\gamma}$ 超过 myopic 的额外负担 $\alpha(R-e)$——这需要 $\gamma$ 或 $\alpha$ 更大。Myopic 自己要赢最难：必须放大降价 $\frac{\alpha R}{1-\gamma}$ 单枪匹马超过他们多付的 $R$，这就要求 $\alpha R \geq (1-\gamma)R$ 即 $\alpha \geq 1-\gamma$。**与 Gabaix-Laibson 的本质区别**：G-L 中 myopic 永远受损（因为 pass-through 是 one-for-one），这里 $\gamma$ 把 pass-through 放大到 $\frac{1}{1-\gamma}$，myopic 有了翻盘机会。

### 7.2 Extension：解绑后的平台治理

**关键观察**（Extension 的起点）：当 disclosure 与 sales channel 解绑后，off-platform 卖 add-on 对卖家**严格占优**（节省 $\gamma\hat{p}$，无代价）。因此无论平台 mandate 什么，add-on 都 off-platform 卖。

**Lemma 2（ps-s）**：平台强制 shroud 下的唯一均衡与 LF-s 完全等价：$p^{ps\text{-}s} = \frac{c-\alpha R}{1-\gamma} + \frac{1}{2f(0)}$，$\hat{p} = R$。

> **直觉**：ps 无法比 LF 下的自愿 shrouding 多提取任何租。

Lemma 2 建立了 ps 的 "冗余性"，推动我们转向 pu 的分析。

**Lemma 3（pu 均衡）**：平台强制 unshroud，阈值 $\alpha^* \equiv \frac{e}{\lambda R}$：

- **(i) Low add-on pricing (pu-e)** 当 $\alpha \leq \alpha^*$：$\hat{p} = e$ 服务所有消费者；$p^{pu\text{-}e} = \frac{c-e}{1-\gamma} + \frac{1}{2f(0)}$。
- **(ii) High add-on pricing (pu-R)** 当 $\alpha \geq \alpha^*$：$\hat{p} = R$ 只服务 $\alpha\lambda$ uninformed myopic；$p^{pu\text{-}R} = \frac{c-\alpha\lambda R}{1-\gamma} + \frac{1}{2f(0)}$。

> **直觉**：平台 unshroud 把 $(1-\lambda)$ 比例的 myopic 转化成 sophisticated。当 $\alpha$ 小时，为了服务整个市场卖家选 $\hat{p}=e$；当 $\alpha$ 大时，uninformed myopic 池 $\alpha\lambda$ 已经足够大，卖家宁可抛弃 sophisticated（让他们去替代）专榨 myopic，定 $\hat{p}=R$。**注意 pu-R 的社会损失是 $(1-\alpha\lambda)e > (1-\alpha)e$**——平台的 unshroud 通过"教育"myopic 反而扩大了替代人群！

**Proposition 2（平台最优 mandate）**：(i) $\alpha < \frac{e}{R}$ 选 ps；(ii) $\alpha \geq \frac{e}{R}$ 选 pu。

> **直觉**：平台收入 = $\gamma \times$ 基础商品价格。比较不同 mandate 下 $p$ 的高低 → 比较 pass-through 掉的 add-on 利润：ps-s 让渡 $\alpha R$，pu-e 让渡 $e$，pu-R 让渡 $\alpha\lambda R$。让渡越少，$p$ 越高，平台收入越高。$\alpha R$ vs. $e$ 的比较给出分界 $\frac{e}{R}$。

Proposition 2 只比较了 ps 与 pu；Proposition 3 则纳入 LF 作为第三选项。

**Corollary 1.1 + Proposition 3（全治理对比）**：

- **LF-u 对平台最优**（唯一同时抽基础商品和 add-on 佣金的均衡），只要它可持续（即 $\gamma \leq \bar{\gamma} \equiv 1 - \frac{\alpha\lambda R}{e}$）。
- 当 LF-u 不可持续（$\gamma > \bar{\gamma}$）时：若 $\alpha < \frac{e}{R}$ 选 LF（此时即 LF-s）；若 $\alpha \geq \frac{e}{R}$ 选 pu。
- **平台从不严格偏好 ps**（ps-s 与 LF-s 收入相同）。

**Trade-off 总结（加粗重点）**：**平台的治理选择完全由"哪种 mandate 让 add-on 利润被让渡得最少、基础商品价格最高"决定，与消费者福利系统性错位。**

### 7.3 关键支配关系（简化福利比较的杠杆）

**Proposition 4**：对所有参数，
$$
CS^{pu\text{-}e} \geq CS^{LF\text{-}u}, \quad CS^{LF\text{-}s} \geq CS^{pu\text{-}R}
$$

> **直觉**：两个支配关系都源于 commission multiplier。
> - **$CS^{pu\text{-}e} \geq CS^{LF\text{-}u}$**：两均衡的 add-on 价都是 $e$，但 LF-u 中 add-on 在平台上（pass-through 一对一，$p$ 降 $e$），pu-e 中 add-on 在平台外（pass-through 放大，$p$ 降 $\frac{e}{1-\gamma}$）。后者降得更多。
> - **$CS^{LF\text{-}s} \geq CS^{pu\text{-}R}$**：两均衡的 add-on 价都是 $R$ off-platform，但 LF-s 中 myopic 池是 $\alpha$（让渡 $\alpha R$），pu-R 中 myopic 池缩到 $\alpha\lambda$（让渡 $\alpha\lambda R$）。前者让渡更多，基础价降得更多；且 pu-R 还因扩大替代人群产生更高社会损失 $(1-\alpha\lambda)e$。

**这两个支配关系把四均衡的福利比较塌缩成了 LF-s vs. pu-e。** 之后只需刻画这一对的消费者福利阈值（Proposition 4 (i)–(iii)）：

| 消费者群体 | LF-s 优于 pu-e 的阈值 |
|:---|:---|
| Sophisticated | $\alpha \geq \frac{e}{R}$ |
| Total | $\alpha \geq \frac{e}{e+\gamma(R-e)}$ |
| Myopic | $\alpha \geq 1 - \frac{\gamma(R-e)}{R}$ |

三阈值严格排序 $\frac{e}{R} \leq \frac{e}{e+\gamma(R-e)} \leq 1-\frac{\gamma(R-e)}{R}$，均随 $\gamma$ 递减。

---

## 8. 比较静态汇总表

| 参数变化 | 对 LF-u 区域的影响 | 对 LF-s 区域的影响 | 对 pu-R 区域的影响 | 直觉 |
|:---|:---|:---|:---|:---|
| $\gamma \uparrow$ | $\downarrow$（$\bar{\gamma}$ 下降，LF-u 不易维持） | $\uparrow$（off-platform 更香） | 不影响存在，但 pu 的盈利性 $\uparrow$ | 佣金越高，卖家越想把 add-on 搬出去 |
| $\alpha \uparrow$ | $\downarrow$（$\bar{\alpha}$ 被越过） | $\uparrow$（$\underline{\alpha}$ 被越过） | $\uparrow$（越过 $\alpha^*$） | myopic 越多，shrouding 越可持续 |
| $\lambda \uparrow$ | $\downarrow$（$\bar{\alpha}$ 下降） | 不影响存在下界 | $\uparrow$（$\alpha^* = \frac{e}{\lambda R}$ 下降） | 短视越持久，unshroud 越没用 |
| $\gamma \uparrow$ | Myopic CS 阈值 $1-\gamma \downarrow$ | 所有 CS 阈值 $\downarrow$ | pu-R 社损不变 | Multiplier 放大，shrouding 对 myopic 更友好 |
| $R \uparrow$ | $\bar{\alpha}, \underline{\alpha} \downarrow$ | Shrouding 利润 $\alpha R \uparrow$ | 社损不变 | 隐藏利润空间变大 |

---

## 9. 主要结论与管理启示

### 与 Gabaix-Laibson (2006) 基准的对比

| 维度 | G-L (2006) | 本文 |
|:---|:---|:---|
| Pass-through | 一对一 | 放大为 $\frac{1}{1-\gamma}$ |
| 中介结构 | 无 | Ad-valorem commission 平台 |
| Myopic 福利 | 始终受损 | 当 $\gamma \geq 1-\alpha$ 时可净赚 |
| 政策建议 | 透明化总是有利 | 透明化可能有害（尤其 DMA 式解绑组合） |
| Shrouding 社会效率 | 一定低 | 一定低，但**消费者福利**可能更高 |

### 管理与政策启示

1. **对平台**：如果佣金率可控，$\gamma \leq \bar{\gamma}$ 时用 LF 最赚（吃两层佣金）；$\gamma$ 高且 $\alpha \geq \frac{e}{R}$ 时用 pu 把 $p$ 拉高。**Airbnb 2025 年全球默认 total price display** 正是 Proposition 3(ii) 的现实印证——$\alpha$ 足够大使得收入激励压倒透明度的收入损失。
2. **对监管者**：
   - 当 $\alpha$ 小时，强制 pu 有益（从 LF 的错位中救出消费者）。
   - 当 $\alpha$ 大（$\geq \alpha^*$）时，**强制 pu 反而触发最差的 pu-R 均衡**——此时应允许 LF（让 LF-s 成为均衡）。
   - **Commission cap** 在 shrouding 区域能恢复社会效率，但也消除了消费者从放大降价中得到的好处——仅在 $\alpha$ 小时合适。
   - **Consumer education**（降低 $\lambda$）是唯一在高 $\alpha$ 区域仍有效的工具——它提高了 $\alpha^* = \frac{e}{\lambda R}$，把 pu-R 区域压缩成 pu-e。
3. **DMA 式"透明 + 解绑"组合的警示**：单独做任何一件都没这么糟，两件事做在一起恰好把均衡钉在 pu-R（当 $\alpha$ 大时），**同时**劣于 LF-s（消费者和社会福利）。

---

## 10. 与相关文献的对话

### Gabaix & Laibson (2006, QJE)

- **共同关注**：competitive shrouding 下的 cross-subsidy 机制。
- **本文推进**：引入比例佣金中介，把 one-for-one pass-through 推广为 $\frac{1}{1-\gamma}$ 放大。
- **为何重要**：改变了 shrouding 对 myopic 消费者的福利方向（从一定受损变为条件性受益），进而改写政策处方。

### Johnen & Somogyi (2024, EJ)

- **共同关注**：平台对 add-on 披露的激励。
- **对立结论**：J&S 下平台偏好 shrouding（因固定会员费下 opacity 抬高感知剩余）；本文平台偏好 unshrouding（因比例佣金下 opacity 流失基础商品基数）。
- **为何重要**：fee structure（fixed vs. ad-valorem）决定了平台激励方向——这是理解为何 Amazon/Google Flights（laissez-faire）与 Airbnb（pu）选择不同治理的关键。

### Geng, Tan & Wei (2018, POM)

- **共同关注**：平台佣金与 add-on 定价的交互。
- **本文推进**：GTW 限于垄断卖家 + 全 myopic 消费者 + 无 shroud 选择；本文引入竞争、异质消费者、策略性 shrouding 与平台 disclosure mandate。
- **为何重要**：竞争 + 消费者异质是 commission multiplier 机制激活的必要条件——垄断模型看不到这个机制。

### Wenzel (2014, JEBO)

- **共同关注**：竞争程度对 shrouding 激励的影响。
- **本文推进**：Wenzel 中更多卖家削弱 shrouding 激励；本文在固定双寡头下通过佣金 $\gamma$ 参数刻画了类似维度的放大。
- **为何重要**：把"竞争强度"从卖家数量推广到平台制度设计（佣金率）。

---

## 11. 犀利评论 (Reviewer's Critique)

### 优点

- **机制识别清晰有力**：competition multiplier 是一个干净、可检验、具有政策含义的新机制，完美嵌入 G-L 的经典框架且产生系统性反转。
- **政策现实感强**：模型与 DMA、FTC junk fees rule、Airbnb total price display 等现实事件的对应精准，Section 4 的政策讨论不是事后附加而是机制的自然延伸。
- **Dominance relations 的使用干净**：把四均衡比较塌缩为 LF-s vs. pu-e 是一个优雅的简化。

### 模型限制与假设过强之处

1. **$\gamma$ 外生是致命简化**。作者用"跨市场统一定价"为这一假设辩护，但平台**为何**跨市场统一定价本身是内生的（很可能与 commission-vs-transparency 权衡有关）。内生化 $\gamma$ 后，本文的放大机制会成为平台选 $\gamma$ 的一阶考虑，结论可能被重写。这是最大的"房间里的大象"。
2. **两卖家对称 + $F$ 对称 log-concave** 让基础商品价格 war 具有退化的 $\frac{1}{2f(0)}$ markup 结构，$N > 2$ 或非对称成本下的 pass-through 动力学可能改变 multiplier 的具体形式。
3. **Add-on 同质**（两卖家 add-on 相同）消除了差异化 add-on 的竞争——现实中航司的 add-on（行李免费额度、选座）是差异化的。
4. **$\lambda$ 外生**。Consumer education 作为政策工具需要一个 $\lambda$ 的技术函数，本文仅做比较静态而不刻画教育成本与供给方。
5. **单平台垄断**。跨平台竞争（Booking vs. Expedia）可能恰好是约束平台 mandate 激励的关键外部力量——单平台模型看不到这一维度。
6. **消费者 sophistication 是二元的**。Heidhues-Köszegi-Murooka (2017) 式的连续 naiveté 分布可能平滑掉阈值效应。
7. **"Commission 放大"的稳健性**：如果平台收入来源包含 per-transaction 固定费（很多平台是 hybrid），放大系数会被稀释到 $\frac{1}{1-\gamma}$ 和 $1$ 之间，实证识别会更困难。
8. **Equilibrium selection 的脆弱性**：作者在 multiplicity 区域选择 Pareto 优于（或社会优于）的 LF-u。Appendix D 做了 robustness（选 LF-s），但核心 Proposition 3 的分区描述仍依赖此选择。

### 未来研究方向

1. **内生化佣金率**：$\gamma$ 作为平台选择变量，研究 $(\gamma^*, \text{mandate}^*)$ 的联合决定。预期 $\gamma^*$ 会显示"平台故意选高佣金以激发卖家 shroud，再通过 pu-mandate 转化为基础商品租"的策略性行为。
2. **平台间竞争**：两平台不同 $\gamma$ 与不同 mandate 的竞争均衡——卖家 multi-homing 会对 anti-steering 条款产生新的内生化理由。
3. **实证识别 multiplier**：利用 commission rate 的外生变动（如 Apple 小开发者费率从 30% 降到 15%）识别基础商品价格对 add-on profit 的 pass-through 弹性。理想的 DiD 设定已隐约可见。
4. **Consumer education 的供给方**：谁提供教育？平台（搜索工具）、监管者（强制披露）、第三方（比价网站）的激励错位。
5. **Add-on 差异化**：Hotelling 结构下的 add-on 差异化，分析 "add-on innovation" 与 shrouding 的互动（差异化的 add-on 可能内在地难以 shroud）。
6. **动态声誉**：重复互动下消费者学习，$\lambda$ 随时间演化，shrouding 的长期可持续性。
7. **Hybrid fee structures**：固定会员费 + 比例佣金的混合结构，桥接 Johnen-Somogyi 与本文，识别 fee structure 的最优设计。

---

## 自我校正检查

- [x] TL;DR 足够直白，用 "把附加费的竞争压力加倍传导到基础商品价格" 这一直观表述
- [x] One More Thing 用 Booking.com + 20% 佣金的具体场景讲放大机制，强调 DMA 的意外后果
- [x] 每个 Proposition 后紧跟 `>` 引用块直觉解释
- [x] 命题间逻辑递进显式标注（Lemma 2 → Lemma 3 → Prop 2 → Prop 3 → Prop 4 每步都有 bridging 语句）
- [x] 符号表分成 4 个模块（卖家、平台、消费者、策略标签）
- [x] Commission multiplier 的核心 trade-off 在多处加粗/独立段落
- [x] 比较静态汇总为一个表
- [x] LaTeX 行内公式无换行，Display 公式居中
- [x] 与相关文献的对话选了 4 篇最相关的（G-L, J-S, GTW, Wenzel）
- [x] 符合 Markdown 规范

# Hybrid Versus Pure Platforms Under Endogenous Wholesale Pricing

**作者**：Zheng Wang（华东理工大学 商学院 / 数字经济研究所）
**期刊**：*Journal of Economics & Management Strategy*
**年份**：2026（接受于 2026 年 3 月，articles in advance）
**DOI**：10.1111/jems.70032

## 中文翻译摘要

近期关于混合（hybrid）平台与纯（pure）平台模式相对效率的争论已成为平台经济学的核心议题。本文研究了一个上游环境：平台上的下游卖家先从一家上游制造商处采购产品，再以 Cournot 数量竞争方式向最终消费者销售。平台模式（hybrid vs. pure）的选择会改变上游制造商的定价激励，进而影响总市场数量与福利。作者推导出 hybrid 模式相对 pure 模式产生更高、更低或相等总数量的条件。**关键决定因素是需求的 modularity（即边际收益的弹性）**。这些结果表明，平台监管应同时考虑需求结构、上游定价行为与市场结构。

JEL：L13, L22, D43

---

## 1. 论文速览

| 维度 | 内容 |
|:---|:---|
| 研究问题 | 当下游平台的卖家从上游制造商采购、且 wholesale price 内生时，hybrid vs. pure 平台模式哪个产生更高总数量与福利？ |
| 研究对象 | 一家垄断上游制造商 + 单一下游平台（含 1P 与 nP 个 3P 卖家）+ Cournot 数量竞争 |
| 研究方法 | 纯理论博弈模型；general inverse demand；后向归纳求 SPNE |
| 核心机制 | 内生 wholesale price 引入 **wholesale price effect**：平台模式改变下游"虚拟边际成本结构"，进而触发上游策略性调整 wholesale price，其方向取决于 demand modularity $\rho+\varepsilon$ |
| 关键发现 | 固定 wholesale price 下 hybrid 总数量更高（复刻已有结论）；内生 wholesale price 下结论**逆转可能**：supermodular 需求 → hybrid 高，submodular 需求 → pure 高，modular 需求 → 相等 |
| 主要贡献 | (i) 把 Anderson & Bedre-Defolie (2022)、Hagiu-Teh-Wright (2022) 的"hybrid 更优"结论嵌入有上游定价的 vertical structure，给出明确反例；(ii) 把 hybrid/pure 比较建立在 Mrázová-Neary modularity 分类上；(iii) 与 input price discrimination 文献对话 |
| 适用场景 | Amazon/JD/京东等同时拥有 1P 业务与 3P marketplace，且依赖上游品牌方供货的平台；vertical integration / acquisition 反垄断评估 |
| 最可能被 challenge 的地方 | (i) Cournot + 同质产品过强；(ii) commission rate $\phi$ 外生且不分模式；(iii) 上游线性定价、无 two-part tariff、无 bargaining；(iv) 平台只在采购"是否绕过 commission"上不同，缺 self-preferencing、信息差、固定成本 |

---

## 2. TL;DR

一旦上游制造商可以策略性地调整 wholesale price，"hybrid 平台总是好于 pure 平台"这条主流结论就**不再普遍成立**。具体哪个模式更好，取决于一个简单的需求几何指标——**$\rho(Q)+\varepsilon(Q)$ 与 3 的大小关系**：需求 supermodular 则 hybrid 胜出，submodular 则 pure 反而胜出，modular 则两者打平。换句话说，监管者评估 Amazon 这类 hybrid 平台时，必须先看清上游会如何"反向调价"。

---

## 3. One More Thing（前置 Hook）

最有意思的一点是：**上游制造商面对一个 hybrid 平台，并不一定提价、有时反而会主动降价。**

直觉上你可能预期，hybrid 平台比 pure 平台拥有更激进的扩张激励（因为 1P 业务不付 commission），所以上游会"敲一笔"——多收 wholesale price。但 Wang 发现这只是 submodular 需求世界里的故事。在 supermodular 需求（边际收益下降很慢）的世界里，上游"敲一笔"的诱惑很弱，反而希望 hybrid 平台进一步扩张以放大自己的销量；当 $\rho(Q)\geq 2$ 时，**hybrid 模式下的 wholesale price 甚至会低于 pure 模式**。这等于说，hybrid 平台的"corporate-governance 优势"和"上游定价的反向利好"在 supermodular 世界叠加放大；而在 submodular 世界，两股力量正好相反，pure 反而占优。

这把一个看似纯监管/治理的问题（hybrid 是不是 umpire-and-player），翻译成了一个**纯需求几何**的问题——这是本文最漂亮的"洞察压缩"。

---

## 4. 研究背景与动机 (Motivation)

### 4.1 实践痛点

近年欧美对 Amazon、Apple 等 hybrid 平台的反垄断调查（如 EU 与 US 对 Amazon 利用 3P 卖家数据的调查、Spotify 对 Apple App Store 规则的申诉）使"hybrid 是否应被禁止"成为热点问题。监管争论几乎都围绕 self-preferencing 展开。但现实中还有一类被忽视的力量：**平台上的 3P 卖家（以及平台 1P）大量从同一上游品牌方进货**（论文引用 Zha et al. 2023 的 vertical structure）。当上游可以策略性地调价时，hybrid/pure 之争就不再只是"平台内部规则"问题，而成为"上下游联合均衡"问题。

Amazon commission 8–15%、JD 2–10%（注 4）即是 commission rate $\phi$ 在现实中的取值范围。

### 4.2 理论缺口

主流 hybrid-vs-pure 文献——Hagiu & Wright (2015)、Anderson & Bedre-Defolie (2022)、Hagiu-Teh-Wright (2022)、Dendorfer (2024)——几乎一致地得到 hybrid 更优 / 福利更高的结论。**这些结论都建立在 sellers 面对 constant exogenous wholesale cost 的假设上**。这一假设把上游定价的 strategic responsiveness 直接抹掉了。本文恰好补上这一环。

另一条相关脉络是 endogenous input pricing 在下游竞争中的作用：Miklós-Thal & Shaffer (2021)、Lømo (2024)、Li & Zhang (2024)。Wang 把这条线引入 hybrid/pure 比较，并系统刻画 modularity 的角色。

### 4.3 核心贡献

1. **建立反例**：在内生 wholesale price 下，给出 hybrid 平台**福利反而更低**的明确条件（submodular demand），打破"hybrid 总优"的既有共识。
2. **几何刻画**：把比较结论压缩到 Mrázová-Neary 的 $\rho+\varepsilon$ 单一指标，并通过 4 个 extension（上游竞争、平台自建 1P、wholesale price discrimination、平台间竞争）系统刻画临界线在 $\{\varepsilon,\rho\}$ 空间中如何旋转。
3. **新的 input price discrimination 角度**：与 Li & Zhang (2024) 等基于"下游成本异质性"的歧视不同，本文研究**基于 seller type（1P vs. 3P）的歧视**，并给出一个混合的弹性-曲率条件 $\rho(1+\varepsilon)-4$ 决定歧视是否提升总量。
4. **对 vertical integration 反垄断评估**有直接含义：hybrid 平台经由收购 3P 形成，本文揭示评估这类收购需联合考虑需求 modularity 与上游定价反应。

---

## 5. 模型设定与假设

本文是一篇纯理论文章，对应 v3 prompt 的 6a 部分。

### 5.1 符号体系（按模块分组）

**(a) 参与者与市场环境**

| 符号 | 含义 | 备注 |
|:---|:---|:---|
| $U$ | 上游制造商（基线为垄断） | 边际成本 $c\geq 0$ |
| $D$ | 下游平台 | pure 时仅做 marketplace；hybrid 时收购 seller 1 |
| $n\geq 2$ | 平台上的卖家数 | hybrid 收购情形下 1P + (n-1) 个 3P |
| $\phi\in(0,1)$ | commission rate | 外生、对称、跨模式不变 |

**(b) 需求与曲率**

| 符号 | 含义 | 备注 |
|:---|:---|:---|
| $p(Q)$ | inverse demand，三阶可微 | $p'<0$ |
| $Q=\sum q_i$ | 总数量 | 同质产品 |
| $\varepsilon(Q)=-\dfrac{p(Q)}{p'(Q)Q}$ | inverse demand 的弹性 | Assumption 1：$\varepsilon>1$（即 $p+p'Q>0$，边际收益为正） |
| $\rho(Q)=-\dfrac{p''(Q)Q}{p'(Q)}$ | inverse demand 的 curvature | 与 $p''$ 同号；对凸性的无量纲度量 |
| $\rho+\varepsilon$ | **modularity index**（Mrázová-Neary） | $>3$ supermodular；$=3$ modular；$<3$ submodular |

> 直观：$\rho+\varepsilon$ 直接对应边际收益的弹性绝对值。supermodular 表示边际收益下降很慢（弹性 < 1），submodular 表示下降很快（弹性 > 1）。代表性例子：CES $p=\beta Q^{-1/\sigma}$ supermodular；inverse translog $p=(\alpha+\beta\ln Q)/Q$ exactly modular；linear $p=a-bQ$ 在 $Q>a/(4b)$ 时 submodular。

**(c) 决策与利润**

| 符号 | 含义 |
|:---|:---|
| $w$ | 上游 wholesale price（基线统一定价） |
| $w_0$ | benchmark 中外生固定的 wholesale price |
| $w^P, w^H$ | pure / hybrid 模式下内生 wholesale price |
| $Q^P, Q^H$ | pure / hybrid 模式下均衡总数量 |

### 5.2 Players, Sequence, Information

- **Players**：1 个上游 $U$、1 个下游平台 $D$、$n$ 个下游卖家。
- **Sequence**（两阶段）：
  1. 上游设定 wholesale price $w$；
  2. 下游卖家（含 hybrid 模式下的平台 1P）同时选择 $q_i$，进行 Cournot 竞争。
- **信息**：完全信息。
- **均衡概念**：Subgame Perfect Nash Equilibrium，后向归纳。

### 5.3 关键利润函数

**3P 卖家 $i$** ：
$$\pi_i = (p(Q)-w)q_i - \phi p(Q)q_i$$

> 第一项是销售毛利 $(p-w)q_i$；第二项是按销售额支付的 commission $\phi p q_i$。等价于卖家面对一个"perceived marginal cost" $w/(1-\phi)$，因为它只能保留 $1-\phi$ 比例的 revenue 但承担全部 wholesale cost（注 7、Johnson 2017）。这是 hybrid 平台"内部 1P"相对 3P 拥有成本优势的源头。

**Pure 平台**：
$$\pi_D = \phi\sum_{i=1}^n p(Q)q_i = \phi p(Q) Q$$

> 平台只是 commission collector，激励完全跟随总销售额。

**Hybrid 平台**（收购 seller 1）：
$$\pi_D = \phi p(Q)Q + (p(Q)-w)q_1 - \phi p(Q)q_1$$

> 第一项仍是从 3P 收的 commission（含从自己 1P 收"内部 commission"是一种记账技巧）；第二、三项合起来是 1P 的净利润 $(p-w)q_1 - \phi p q_1$。等价地，平台的 1P 部分只承担 wholesale cost、但不被 commission "吃掉"——这正是 hybrid 模式的扩张激励来源。

### 5.4 关键假设

- **Assumption 1（$\varepsilon>1$）**：marginal revenue 为正。
  - *Justification*：避免均衡数量"反向"；Etro (2021) 也用此设。
  - *If relaxed*：在 marginal revenue 可能为负的区域，Cournot 一阶条件本身可能没有内部解，模型构造会失败。
- **Assumption 2a / 3a（$\rho$ 的上界）**：例如 Assumption 2a：$\rho(Q)<1+n-\phi(n-1)$；Assumption 3a：$\rho(Q)<\dfrac{(2-\rho(Q))(1+n(1-\phi)-\rho(Q))}{Q}$（更严格）。
  - *Justification*：分别保证下游 Cournot 均衡的 SOC 和上游 monopolist 的 SOC（Vives 1999）。
  - *If relaxed*：均衡可能不唯一或不存在，比较结果失去意义。

---

## 6. 分析路线图 (Roadmap)

文章的递进结构非常清晰，以"逐步 endogenize"为主线：

1. **Section 3 Benchmark**：固定 $w_0$，**不让上游做策略**。复刻已有文献结论（Proposition 1：hybrid 总数量更高）。这一步是"对照组"。
2. **Section 4 Main**：让上游 monopolist 内生选 $w$，**单独引入 wholesale price effect**。Proposition 2 给出关键 modularity-based 比较结果，这是全文核心。
3. **Section 5 Extensions**：四个互不重叠的方向，把临界线 $\rho+\varepsilon=3$ 在 $\{\varepsilon,\rho\}$ 空间中"旋转"。
   - 5.1 **上游竞争**（Cournot $m$ 家）→ 临界线变为 $\rho+m\varepsilon=m+2$，逆时针旋转，hybrid 优势区扩大。
   - 5.2 **平台自建 1P**（卖家从 $n$ 增到 $n+1$）→ 临界线 $(1-\tfrac{1-\phi}{n\phi})\rho+\varepsilon=3-2\tfrac{1-\phi}{n\phi}$，依 $n$ 大小可顺/逆时针旋转，hybrid 优势区一般扩大。
   - 5.3 **Wholesale price discrimination**（$w_1\neq w_2$）→ 临界曲线在 $\{\varepsilon,\rho\}$ 空间中**收缩** hybrid 优势区。
   - 5.4 **平台间竞争**（$N$ 家差异化平台）→ 临界线 $\rho+k\varepsilon=k+2$（$k=1+(n-1)\alpha$），逆时针旋转，hybrid 优势区扩大。

每一步要么放松垄断假设，要么改变"hybrid 是怎么变成 hybrid 的"路径，要么允许更精细的定价工具。

---

## 7. 核心分析与求解 (Analysis & Results)

### 7.1 Benchmark：固定 wholesale price（Section 3）

**Pure 模式 FOC**（对 $i$ 求 $q_i$）：$p(Q)+p'(Q)q_i=\dfrac{w_0}{1-\phi}$。对 $i$ 求和：
$$(1-\phi)\,n\,p(Q^P) + (1-\phi)\,p'(Q^P)Q^P = n w_0 \quad (7)$$

**Hybrid 模式**：平台对 $q_1$ FOC 为 $p+p'(q_1+\phi(Q-q_1))=w_0$（注意 $\phi(Q-q_1)$ 项——平台 internalize 了对 3P commission revenue 的影响），3P 的 FOC 仍同 pure。结合后：
$$(n-(n-1)\phi)\,p(Q^H) + p'(Q^H)Q^H = n w_0 \quad (11)$$

**Proposition 1**：固定 $w_0$，$Q^H>Q^P$。

> **直觉**：3P 因 commission 面对 perceived marginal cost $w_0/(1-\phi) > w_0$，而 hybrid 1P 仅面对 $w_0$。平台直接扩张的效应（1P 量上去了）压过了 Cournot 战略替代下 3P 量收缩的间接效应。同质产品下总量是 CS 与 W 的充分统计，故 Corollary 1：hybrid 同时提高 CS 与 total welfare。

### 7.2 主结果：内生 wholesale price 下的逆转可能（Section 4）

**Pure 模式**：上游 FOC $Q+(w-c)Q'(w)=0$ + 隐函数定理（应用到 (12)）得 $Q^{P\prime}(w^P)=\dfrac{n}{(1-\phi)(1+n-\rho(Q^P))p'(Q^P)}<0$。代入并消去 $w^P$，**Lemma 1**：
$$(1-\phi)\,n\,p(Q^P) + (1-\phi)(2+n-\rho(Q^P))p'(Q^P)Q^P = nc \quad (16)$$

**Hybrid 模式**：类似地，**Lemma 2**：
$$(n-(n-1)\phi)\,p(Q^H) + (2+n-(n-1)\phi-\rho(Q^H))p'(Q^H)Q^H = nc \quad (20)$$

承接 Proposition 1（固定 $w$ 时 hybrid 总量必更高），下面这条命题问的是：当 $w$ 可以被上游策略性调整时，方向是否反转？

**Proposition 2**：内生 $w$ 下，
- (i) supermodular 需求（$\rho+\varepsilon>3$）：$Q^H>Q^P$；
- (ii) submodular 需求（$\rho+\varepsilon<3$）：$Q^H<Q^P$；
- (iii) modular 需求（$\rho+\varepsilon=3$）：$Q^H=Q^P$。

> **直觉**：相对 Proposition 1，新增的力量是 **wholesale price effect**——上游会根据下游模式策略性调整 $w$。证明细节（见 Appendix）：构造 $F(Q^P)-G(Q^P)=\dfrac{\phi p(Q^P)}{\varepsilon(Q^P)}(\rho(Q^P)+\varepsilon(Q^P)-3)$，这一差值的符号正是 $\rho+\varepsilon-3$。
>
> 经济解读：submodular（marginal revenue 弹性大）→ 当 hybrid 想扩张时，MR 下降太快，上游可以放心提价"敲"平台一笔（$w^H$ 显著高于 $w^P$），这一提价效应足以压过 hybrid 内生的扩张激励，结果 $Q^H<Q^P$；supermodular（MR 弹性小）→ 上游提价空间小（甚至当 $\rho\geq 2$ 时反而降价），hybrid 扩张激励得以维持甚至放大。

> ⚠ 我的解读：这个机制本质上是一个 **"vertical pass-through"** 故事的延伸——MR 越富有弹性（submodular），上游的最优反应越激进，下游的"组织优势"越容易被上游的反向定价吞噬。

> **关键 trade-off（独立段落突出）**：
>
> **hybrid 平台的"避税扩张激励" vs. 上游"敲单"的反向定价激励——modularity 决定谁占上风。**

**Corollary 2**：CS 与 total welfare 的排序与 $Q$ 的排序完全一致。

**三个数值例（$n=4,\phi=0.1,c=0.1$）**：
- Supermodular（CES $p=Q^{-1/2}$，$\rho+\varepsilon=3.5$）：$w^H\approx0.123<w^P\approx0.127$，$Q^H\approx42.25>Q^P\approx38.29$。**上游降价**。
- Modular（inverse translog）：$w^H\approx0.428$ 略高于 $w^P\approx0.424$，$Q^H=Q^P=0.675$。
- Submodular（线性 $p=10-Q$，$\rho+\varepsilon\approx 1.53$）：$w^H\approx4.675>w^P\approx4.55$，$Q^H\approx3.89<Q^P\approx3.96$。**上游提价**。

### 7.3 Extension 1：上游竞争（Section 5.1）

**目的**：弱化上游 pricing power，看临界线如何移动。

设 $m\geq 2$ 家上游 Cournot 竞争（Adachi & Ebina 2014 框架），第一阶段制造商决定数量，wholesale price 由市场出清。

**Proposition 3**：内生 $w$ 下，$Q^H>(=,<)Q^P \iff \rho(Q)+m\varepsilon(Q)>(=,<)m+2$。

> **直觉**：临界线在 $\{\varepsilon,\rho\}$ 空间中由 $\rho+\varepsilon=3$ 旋转为 $\rho+m\varepsilon=m+2$（**逆时针**），hybrid 优势区扩大。$m\to\infty$ 时退化为 $\varepsilon=1$，等价于固定 $w$ 情形（上游完全竞争 → wholesale price 不再随下游需求策略性调整）。

### 7.4 Extension 2：平台自建 1P（Section 5.2）

**目的**：之前的 hybrid 由收购 seller 1 形成（$n$ 不变）。这里平台不收购、而是新建 1P（卖家从 $n$ 增到 $n+1$），引入"entry effect"。

**Proposition 4**（固定 $w$）：仍有 $Q^H>Q^P$，且优势更强（多了一个竞争者）。

**Proposition 5**（内生 $w$）：临界线为
$$\Big(1-\tfrac{1-\phi}{n\phi}\Big)\rho(Q)+\varepsilon(Q)>(=,<)3-2\tfrac{1-\phi}{n\phi}.$$

> **直觉**：当 $n<(1-\phi)/\phi$（卖家数少）时，临界线斜率甚至变正（顺时针旋转，且可能向上倾斜）；当 $n>(1-\phi)/\phi$ 时仍下倾，但 hybrid 优势区比收购情形更大。$n\to\infty$ 时临界线收敛到 $\rho+\varepsilon=3$（entry effect 被稀释，回到收购情形）。

### 7.5 Extension 3：Wholesale price discrimination（Section 5.3）

**目的**：让上游对 1P 与 3P 设不同价 $w_1, w_2$。

**Lemma 3**（DeGraba 1990 类型结果）：均衡下 $w_1>w_2$。

> **直觉**：3P 因 commission 有更高 perceived marginal cost、input demand 弹性更大；hybrid 1P 弹性更小，是上游的 "captive customer"，可以被宰得更多。

**Lemma 4**：$Q^D>(=,<)Q^H \iff \rho(Q)(1+\varepsilon(Q))-4>(=,<)0$。

> **直觉**：discrimination 对总量的影响取决于一个混合的弹性-曲率条件。

**Proposition 6**：discrimination 下，$Q^D>(=,<)Q^P \iff$
$$\rho(Q)\big(\phi(n-1)\varepsilon(Q)^2+4-\phi(3+n)\big)-4(n\phi-1)\varepsilon(Q)>(=,<)12-(8+4n)\phi.$$

> **直觉**：新临界曲线在 $\{\varepsilon,\rho\}$ 空间中与 $\rho+\varepsilon=3$ 在 $(1,2)$ 处相交，**整体收缩 hybrid 优势区**。原因是 discrimination 让上游对 hybrid 平台收更高 $w_1$，削弱其扩张激励。

### 7.6 Extension 4：平台间竞争（Section 5.4）

**目的**：刻画 $N$ 家差异化平台（参数 $\alpha\in[0,1]$ 度量差异化）下的比较。

引入 virtual quantity $Q_v\equiv [1+(n-1)\alpha]Q_j=kQ_j$，其中 $k\geq 1$ 度量平台间竞争强度。

**Proposition 7**（固定 $w$）：仍 $Q^H>Q^P$。

**Proposition 8**（内生 $w$）：$Q^H>(=,<)Q^P \iff \rho(Q)+k\varepsilon(Q)>(=,<)k+2$。

> **直觉**：$k=1$ 时退化为基线 $\rho+\varepsilon=3$；$k$ 越大（平台越多或越同质化），临界线在 $\{\varepsilon,\rho\}$ 空间中**逆时针旋转**，hybrid 优势区扩大。

> ⚠ 我的解读：Extension 1 与 4 的临界线形式 $\rho+m\varepsilon=m+2$ 与 $\rho+k\varepsilon=k+2$ **结构同构**，本质上都是"削弱上游 pricing power"的两条不同路径——一条来自上游侧的竞争，一条来自下游侧的竞争。这是文章一个未被作者明示但很漂亮的统一性。

---

## 8. 比较静态汇总表

| 参数变化 | 对临界线在 $\{\varepsilon,\rho\}$ 空间位置的影响 | 对 hybrid 优势区面积的影响 | 直觉 |
|:---|:---|:---|:---|
| 上游变竞争（$m\uparrow$） | 逆时针旋转至 $\rho+m\varepsilon=m+2$ | $\uparrow$ | 上游 pricing power $\downarrow$，wholesale price effect 被稀释 |
| $m\to\infty$ | 收敛到 $\varepsilon=1$ | hybrid 几乎总占优 | 退化到固定 $w$ 情形 |
| 平台自建 1P（vs 收购） | 临界线随 $n,\phi$ 旋转 | $\uparrow$ | 多一个 entry effect 强化下游竞争 |
| $n\to\infty$（自建情形） | 收敛到 $\rho+\varepsilon=3$ | 与收购情形相同 | entry effect 被稀释 |
| Wholesale price discrimination | 在 $(1,2)$ 与基线相交、整体收缩 | $\downarrow$ | 上游对 1P 收更高 $w_1$，削弱 hybrid 扩张激励 |
| 平台竞争 $k\uparrow$（$N\uparrow$ 或 $\alpha\uparrow$） | 逆时针旋转至 $\rho+k\varepsilon=k+2$ | $\uparrow$ | 与上游竞争同构机制 |

---

## 9. 主要结论与管理启示

### 9.1 与 Benchmark / 既有直觉的对比

| 维度 | Benchmark / 既有文献直觉 | 本文发现 | 为什么重要 |
|:---|:---|:---|:---|
| 固定 $w$ 下 hybrid vs. pure | hybrid 总优（Anderson-BD 2022, Hagiu-Teh-Wright 2022） | 复刻：$Q^H>Q^P$（Prop. 1） | 验证基线模型与文献一致 |
| 内生 $w$ 下 hybrid vs. pure | （已有文献未系统讨论） | **Modularity 决定方向**：supermodular hybrid 优、submodular pure 优 | 对监管直接含义：禁止/允许 hybrid 不能"一刀切" |
| 上游对 hybrid 的定价反应 | 直觉上 hybrid 更激进 → 上游应"敲一笔" | 仅在 submodular 时成立；supermodular 且 $\rho\geq 2$ 时上游反而降价 | 颠覆"上游必然 extract"的简化叙事 |
| Input price discrimination | Li & Zhang 2024 等基于成本异质性 | 基于 seller type 的歧视，混合弹性-曲率条件 $\rho(1+\varepsilon)-4$ | 给 hybrid 平台情境下的 discrimination 一个新表征 |

### 9.2 管理 / 监管建议

1. **监管者评估 hybrid 平台时，应估计相关市场的 $\rho+\varepsilon$**：当目标市场需求接近 linear/submodular（如成熟、低差异化的快消品）时，"禁止 hybrid"或限制平台 1P 业务的政策反而可能提高总数量与福利；当目标市场是 CES/supermodular（如差异化数字商品、订阅服务）时，允许 hybrid 是 pro-competitive 的。
2. **反垄断评估 vertical integration（如 Amazon 收购品牌或 3P）时，需联合考虑 demand modularity 与上游 pricing 反应**——而非仅看下游集中度。
3. **当上游市场本身较为竞争（多品牌、多供应商）或下游平台市场较为竞争时**，hybrid 的福利优势更稳健，监管可以更宽容。
4. **Wholesale price discrimination 是 hybrid 优势的"消解器"**：若上游对 1P 收高价、对 3P 收低价（与本文 $w_1>w_2$ 一致），hybrid 优势会被压缩；监管可关注上游是否对 platform 1P 实施差别定价。
5. 作者最后指出（注 10、Section 6 conjecture）：若引入 Nash bargaining 且平台 bargaining power 强，$w_1$ 甚至可能低于 $w_2$，hybrid 优势区将进一步扩大。

---

## 10. 与相关文献的对话

### 10.1 Anderson & Bedre-Defolie (2022, *IJIO*)：homogeneous-preference 下 hybrid 降价、heterogeneous-preference 下 hybrid 通过 commission steering 抬价
- **共同关注点**：hybrid vs. pure 的 CS 与 welfare 比较。
- **本文推进**：AB-D 用的是单一上游成本外生设定。本文表明，即使在最简单的 homogeneous + Cournot 设置下，**只要让上游内生定价**，他们的"hybrid 降价"结论就可能反转。
- **重要性**：把 vertical structure 作为新的反例机制，而非依赖偏好异质性。

### 10.2 Hagiu, Teh & Wright (2022, *RAND*)："禁止 hybrid"会降低 CS 与 total welfare
- **共同关注点**：hybrid 的福利评价及对监管"banning"政策的回应。
- **本文推进**：HTW 假设平台/卖家成本结构外生，hybrid 优势来自 superior products 或 cost advantage。本文给出**完全不依赖于"产品/成本优势"的反例**：即便 hybrid 没有产品/成本优势，单凭 vertical pricing 反应就足以使其在 submodular 需求下 welfare 减少。
- **重要性**：限定 HTW 政策结论的适用边界。

### 10.3 Miklós-Thal & Shaffer (2021, *IJIO*)：endogenous input cost 下 third-degree price discrimination 对总量的效应可能反转
- **共同关注点**：上游策略性定价改变下游"标准结论"的方向。
- **本文推进**：把 MTS 的"endogenous input cost reverses standard results"思想从 price discrimination 议题迁移到 platform mode 议题，并把 modularity 作为统一的几何刻画。
- **重要性**：方法上的同源、议题上的扩展。

### 10.4 Li & Zhang (2024, *IJIO*)：input price discrimination 提升总量与否取决于 inverse demand 凸性
- **共同关注点**：上游对下游不同 sellers 的差别定价对总量的影响。
- **本文推进**：Li-Zhang 的 discrimination 基于下游 marginal cost 异质性。本文讨论的 discrimination 基于 **seller type**（1P vs. 3P），驱动力是 commission 而非外生成本异质，并给出弹性-曲率混合条件 $\rho(1+\varepsilon)-4$。
- **重要性**：在 hybrid platform 这一具体情境下重写 input price discrimination 的福利条件。

---

## 11. 犀利评论 (Reviewer's Critique)

### 11.1 Major concerns

1. **Cournot + 同质产品同时假设过强，限制外部有效性。**
现实中 Amazon 的 1P 与 3P 卖家更多在差异化产品上做价格竞争（Bertrand-with-differentiation），而非数量竞争。Wang 在 conclusion 中承认这一点（提到 Etro 2023 作为未来方向）。在 Bertrand 框架下，hybrid 1P 的"避 commission 优势"会通过定价（而非数量）传导，wholesale price effect 的方向与强度可能完全不同。**这一假设最直接削弱的是"modularity 决定方向"的普适性**——modularity 是为 quantity competition 量身定做的几何指标。

2. **Commission rate $\phi$ 外生且跨模式不变。**
Anderson & Bedre-Defolie (2022) 与 Hagiu-Teh-Wright (2022) 都讨论过 hybrid 平台有强烈动机在两种模式下设定不同 $\phi$（在 hybrid 下 $\phi$ 可能更高以 steer demand 到 1P）。一旦 $\phi$ 内生，hybrid 平台可能通过提高 $\phi$ 进一步扭曲下游成本结构，从而改变上游的最优 $w$ 反应。本文的 Proposition 2 所依赖的 $\rho+\varepsilon$ 临界条件可能在 $\phi$ 内生后不再成立。**这是最影响"管理建议直接应用"的一条**。

3. **上游纯 linear pricing，无 two-part tariff、无 RPM、无 bargaining。**
现实中大品牌方与平台几乎从来不只用 linear wholesale price——two-part tariff 或 quantity discount 几乎是默认。如果 wholesale 合约是 efficient（如 two-part tariff 实现 vertical integration 的总利润），那么 wholesale price effect 这一核心机制将被消解，hybrid/pure 比较会回到 Anderson-BD 的固定成本世界。作者在 conclusion conjecture 中提到 bargaining 会强化 hybrid，但**如果合约本身就 efficient，"modularity 决定方向"的命题可能直接失效**。

4. **缺 self-preferencing 维度，与现实监管痛点错位。**
作者明确说本文 abstracts from self-preferencing，但 Amazon/Apple 案的核心争议恰恰是 self-preferencing。一个完整的政策模型至少应同时含两条 channel——self-preferencing 与 vertical pricing——并讨论二者交互。本文是一个"窄而深"的贡献，但在 policy 层面要谨慎自我定位。

### 11.2 Minor concerns

5. **数值例的 $\phi=0.1$ 偏低**（Amazon 实际 8–15%、JD 2–10%）。在更现实的 $\phi$ 区间，比较静态数量是否仍稳健，值得增加 robustness 表。
6. **关键阈值 $\rho+\varepsilon=3$ 在直觉表达上对非理论读者门槛偏高。**article 在多处只用 supermodular/submodular 标签，但缺一段 "what does this mean for a real demand function in practice" 的桥梁段落（例如：哪些行业的 demand 大致 supermodular？）。
7. **Extension 之间的 interaction 未讨论。**例如：上游竞争 + 平台竞争同时存在时（Extensions 1+4），$\rho+\varepsilon$ 的临界线如何被 $m$ 与 $k$ 联合调制？是否相加？是否相乘？文章只给单维 extension，缺联合分析。
8. **Hybrid 通过 acquisition 的假设**（保持 $n$ 不变）虽然方便比较，但与 Section 5.2 的"自建 1P"的差异未在 Section 4 主结论中讨论清楚——读者要等到 5.2 才知道 baseline 选 acquisition 是出于什么 isolation 目的。可以在 Section 2 model 提前说明。

### 11.3 Future research

1. **Bertrand + differentiated products 重做**（作者已提到）：检验 modularity 临界条件是否在价格竞争下有对偶版本（可能是某种 demand convexity 在价格空间中的对应物）。
2. **内生 commission rate $\phi$**：Anderson-BD (2024) 已开了头，与本文 vertical pricing 机制结合，研究 $(\phi, w)$ 联合内生下的 hybrid/pure 比较；预计会出现 $\phi$ 与 $\rho+\varepsilon$ 的乘积条件。
3. **Two-part tariff 或 Nash bargaining**（作者已 conjecture）：形式化证明 bargaining power 提升 hybrid 优势区；进一步可让 bargaining power 内生于 platform size。
4. **Self-preferencing × vertical pricing 的交互**：构造一个同时含 search ranking distortion 与 wholesale price reaction 的模型，检验两条 channel 是否互补或替代。这是与现实监管最对接的方向。
5. **结构估计 / 实证检验**：用 Amazon Marketplace 或 JD 的 1P/3P 数据 + 上游品牌方 wholesale price 数据，估计 $\rho+\varepsilon$，检验当 hybrid 进入新品类时 wholesale price 的方向变化是否符合 Proposition 2 预测。这一步若做出来，将极大提升 paper 的政策含金量。

---

## 附录边界说明

本文 Online Appendix 中应含：所有 Proposition 1–8、Lemma 1–5 的完整证明（论文末尾的 Appendix A 已完整给出主要证明，未见进一步的 Online Supplement）；Assumption 3a/3b/3c/3d 的具体表达式较为复杂，本笔记仅给出关键形式与其经济作用，详细代数推导请回查原文 Appendix。Wang 的几何 figures（Figures 2–5）以临界线在 $\{\varepsilon,\rho\}$ 空间中的旋转方式呈现，本笔记以表格与文字代替，建议精读时回看原图以建立空间直觉。

- [x] 不懂
# Getting to the Green: Should a Profit-Maximizing Firm Buy Carbon Offsets or Invite Consumers to Buy Them?

## Paper snapshot

- Title: Getting to the Green: Should a Profit-Maximizing Firm Buy Carbon Offsets or Invite Consumers to Buy Them?
- Authors: Gökçe Esenduran; H. Sebastian Heese; Gilvan C. Souza
- Outlet: POMS, accepted
- Research question: 对一个利润最大化的垄断企业而言，面对“绿色消费者 + 气候冷感消费者”的市场，最优的碳抵消（carbon offsets）策略到底是：企业自己买 offsets（并把成本摊进售价），还是在结账时给消费者提供“加购 offsets”的选项，甚至两者都做？

这篇文章的魅力在于：它把一个现实中非常常见、但学术上经常被“当成运营细节略过”的决策，抽象成一个可解的机制模型，并且给出了非常干净的结构性结论：最优策略只会落在三种“极端角点”之一（全由企业买、全由消费者加购、或完全不用），而且企业在让消费者加购 offsets 时会主动“倒贴”卖（offsets 以低于成本的价格出售）。

---

## 1 研究背景与动机 Motivation

### 1.1 实践痛点：为什么“offsets”会变成运营/营销的硬问题？

现实世界里，很多面向消费者的企业公开承诺未来实现 net-zero / carbon neutral（如航空、零售、科技公司等）。典型做法是：

1. 先在价值链内部做减排（renewable energy、低碳材料、运输电动化、能效提升等），但边际减排成本会越来越高（“low-hanging fruit”之后进入陡峭的 marginal abatement cost curve）。
2. 仍存在无法进一步经济性减排的“残余排放”（residual emissions），这时就需要用 carbon offsets 来补齐。
3. 与此同时，消费者并非一致“为绿色买单”：市场里既有愿意为低碳支付溢价的 green segment，也有相当大比例的 climate-disengaged segment（不愿为低碳付费）。

于是企业面临一个很现实、也很折磨人的决策：

- 方案 A：企业自己买 offsets，把成本通过更高的产品价格 $p$ 向所有消费者转嫁（包括不关心碳排的冷感消费者）。
- 方案 B：企业不自己买，而是在购买页面/结账页提供“加购 offsets”选项，让愿意的人自己掏钱抵消。
- 方案 C：两者都做（企业买一部分、消费者再买一部分）。
- 方案 D：干脆不折腾 offsets。

痛点不在“有没有道德”，而在“利润最大化 + 市场异质性 + 外部性（企业总排放被部分消费者在意）”这三个东西搅在一起后，直觉会经常失灵。例如：

- 为什么有些企业把 offsets 做成 add-on（加购项）而不是直接把碳中和成本打进价格？
- 如果企业已经在结账页卖 offsets，是否还应该自己额外买一些以示“更绿”？
- offsets 的最优售价应该是成本加成、成本价、还是低于成本？

### 1.2 理论缺口：现有文献忽略了什么？

相关研究很多（绿色产品线设计、消费者的 pro-social/环保偏好、企业社会责任与需求、以及碳足迹与支付意愿等）。但对本文的核心问题来说，关键缺口在于：

1. 现有 OM/Marketing 模型常把“减排/offsets”当成企业单边的投入决策（影响产品属性或需求），较少把“消费者在交易时自选购买 offsets”当成一个可用于市场细分的菜单（menu）机制。
2. 即便有研究讨论 offsets，也更多关注企业是否 offset、offset 多少、或 offset 的质量问题；较少系统刻画“企业买 offsets vs 让消费者买 offsets”这两种制度在利润与排放上的结构性差异，更少讨论两者同时存在时的最优性。
3. 对 offsets 定价（offsets add-on 的价格 $p_o$）的理论结论稀缺，尤其是“为什么企业会愿意亏本卖 offsets”这种非常反直觉但在实践中并不罕见的现象。

### 1.3 核心贡献与意义：本文到底新在哪？

本文最重要的理论/实践贡献可以浓缩为四句（但每句都值得博士生推导一遍）：

1. 三段式最优策略：存在三个 offset 成本区间，分别对应最优策略为  
   - 低成本：企业买足 offsets，实现碳中和（$E=0$），成本进售价；  
   - 中等成本：企业不买 offsets，而是让消费者加购 offsets，并且以低于成本的价格卖出，确保绿色消费者都买；  
   - 高成本：完全不用 offsets。
2. “两者同时做”永远不是最优：企业不会同时在 firm level 买 offsets 又在 consumer level 卖 offsets。
3. offsets add-on 的本质是 price discrimination：让消费者加购 offsets 不是为了从 offsets 赚差价，而是通过自选择（self-selection）实现市场细分与二级价格歧视（second-degree price discrimination），从而提高利润。
4. 碳中和需要消费者“关心企业总排放”：如果绿色消费者只在意自己那一单的排放（相当于模型里 $\beta=0$），则利润最大化企业永远不会选择全量碳中和；它更倾向于补贴绿色消费者的 offsets，而放任冷感消费者的排放不被抵消。

---

## 2 模型设定与假设 Model Setup & Assumptions

### 2.1 符号体系

下表是论文 Table 1 的核心符号（加入一些解释性的注释，便于复盘推导）。

| 类型 | 符号 | 含义 |
|---|---|---|
| 决策变量 | $p$ | 产品价格（firm 先动选择） |
| 决策变量 | $p_o$ | offsets 的销售价格（消费者加购时支付的 add-on 价格，按“每件产品对应的 offset”计价） |
| 决策变量 | $N$ | 企业在 firm level 购买的 offsets 数量（不转卖给消费者），单位按“每件产品的排放量 $e$”归一化 |
| 消费者特征 | $\theta$ | 消费者对产品的基础估值，$\theta\sim U[0,1]$ |
| 排放参数 | $e$ | 单件产品的残余碳足迹（tCO2-eq/件），已假定价值链内部可行减排都做完后的 residual emissions |
| 市场结构 | $\gamma$ | 绿色消费者占比（green segment size） |
| 偏好参数 | $\alpha$ | 绿色消费者对单位排放的“厌恶系数”（disutility per unit emission） |
| 偏好参数 | $\beta$ | 绿色消费者对“企业总碳足迹”的权重，衡量其对 firm-level emissions 的在意程度（直觉上常取 $\beta<1$） |
| 成本参数 | $c_o$ | offsets 的单位成本（按“每件产品对应的 offset”计价） |
| 派生量 | $D_d, D_g$ | 冷感/绿色消费者的产品需求（销量） |
| 派生量 | $D_g^o, D_g^n$ | 绿色消费者中：购买 offsets 的需求 vs 不购买 offsets 的需求 |
| 派生量 | $E$ | 企业总碳足迹（总排放减去 offsets），核心外部性变量 |

### 2.2 Players, Sequence of Events, Information Structure

这是一个典型的 Stackelberg 型两阶段博弈（firm 先动，消费者后动）：

1. Firm（单一垄断企业）宣布 $(p, p_o, N)$。
2. Consumers 观察到 $(p, p_o, N)$ 后做两层决策：  
   - 是否购买产品；  
   - 若购买，是否加购 offsets。
3. 均衡里 $E$ 必须与消费者的需求与 offsets 购买行为一致（理性预期/一致性条件）。

信息结构上，消费者知道自己的 $\theta$ 与类型（green 或 disengaged），并观察到 firm 的策略；firm 知道参数分布（$\gamma,\alpha,\beta,e,c_o$）但不知道个体 $\theta$。

### 2.3 消费者效用与碳排放核算

#### 2.3.1 冷感消费者（disengaged）

冷感消费者不在意碳排放，只看价格：

$$ U_d(\theta)=\theta-p. $$

因此其购买阈值为 $\theta\ge p$，需求为

$$ D_d=(1-\gamma)(1-p), $$

只要 $p\le 1$（否则需求为 0）。

#### 2.3.2 绿色消费者（green）：两层“碳在意”

绿色消费者的 disutility 有两部分：

1. 自己这一单的排放 $e$；
2. 企业总体残余排放 $E$，用 $\beta$ 折扣权重表示其“对别人排放/企业整体排放”的在意程度。

企业总碳足迹定义为

$$ E = e\bigl(D - D_g^o - N\bigr), $$

其中 $D=D_d+D_g$ 为总销量；$D_g^o$ 是购买 offsets 的绿色消费者数量；$N$ 是企业额外购买的 offsets 数量。直观地说：每卖出一件产品就产生 $e$ 排放；如果该件产品被消费者 offset（计入 $D_g^o$）或被企业 offset（计入 $N$），则这部分排放被抵消。

当企业没有承诺“全量 offset”（即不满足碳中和），绿色消费者面临两种 bundle：

- 只买产品（不加购 offsets）：

$$ U_g^n(\theta)=\theta-p-\alpha\bigl(e+\beta E\bigr). $$

- 买产品并加购 offsets（自己这单的 $e$ 被抵消）：

$$ U_g^o(\theta)=\theta-p-p_o-\alpha\beta E. $$

如果企业买足 offsets 使得 $E=0$（碳中和），论文假设绿色消费者知道其购买导致的排放也会被抵消，此时其效用退化为 $U=\theta-p$（与冷感消费者相同）。

### 2.4 企业目标函数与约束

企业利润函数（论文式 (4)）：

$$ \max_{p,p_o,N}\ \pi(p,p_o,N)=p(D_d+D_g)+(p_o-c_o)D_g^o - Nc_o. $$

三块利润的含义非常清楚：

1. 产品收入 $p(D_d+D_g)$；
2. offsets add-on 的“毛利” $(p_o-c_o)D_g^o$（注意可以为负，意味着补贴）；
3. 企业自购 offsets 的成本 $Nc_o$。

约束（论文式 (5)）：

$$ N \le D_d + D_g^n. $$

解释：企业最多只能为“没有被消费者抵消的那部分销量”购买 offsets；否则就会出现“超额抵消”（变成碳负排放）的不现实情形。也可以理解为：如果某个绿色消费者自己买了 offsets（计入 $D_g^o$），企业就没必要再为这件产品重复买一次。

### 2.5 关键假设与合理性（Justification）

1. 垄断（monopoly）与零生产成本：让核心机制聚焦在“offsets 如何改变定价与市场细分”。在更一般的成本结构下，很多结果会被线性平移，但阈值结构仍可能保留。
2. offsets 成本 $c_o$ 外生且恒定：把 offsets 市场当成完全竞争且企业为 price-taker。现实中不同质量 offsets 成本差异巨大，但先从 exogenous cost 入手能给出清晰边界条件。
3. $e$ 被视为“已做完内部减排后的 residual emissions”：模型不再让企业选择内部减排（abatement）与 offsets 的替代，而是专注“剩余排放如何处理”。这与许多企业的实际叙事一致：先减排，再 offset。
4. 两类消费者（green vs disengaged）：极简分割让 price discrimination 的逻辑最清晰。论文也承认未来可拓展到连续异质性。
5. 绿色消费者对企业总排放的关注用线性项 $\beta E$ 表示：这是一个“可操作的简化”。它把 NGO 信息披露、企业 ESG 报告、CDP 等提高透明度的作用，压缩成一个参数 $\beta$。
6. 论文主体聚焦一个“更贴近现实”的参数区间（条件 (6)）:

   $$ \alpha e < \frac{1}{2}+(3-\gamma)\beta. $$  

   直观含义：绿色消费者为抵消自己这单排放的最高愿付 $\alpha e$ 不至于大到超过典型产品价格水平（例如笔记本、机票的价格远高于 offsets add-on）。该条件保证主体推导落在更常见的均衡形态；更一般情形在 Online Appendix A 完整求解。

---

## 3 分析与求解 Analysis & Solution

### 3.1 求解路线图（你应该如何复盘这篇论文）

整篇文章的解法可以用一句话描述：先用 backward induction 写出需求与 $E$ 的一致性条件，再利用“线性结构 + 角点最优”把问题压缩成有限个候选策略，最后比较利润得到阈值。

更具体地：

1. 给定 $(p,p_o,N)$，求消费者的最优选择，从而得到 $D_d$、$D_g^o$、$D_g^n$ 的表达式。
2. 用 $E=e(D-D_g^o-N)$ 做均衡一致性（fixed point）求解，把 $E$ 消掉，使利润只剩 $(p,p_o,N)$。
3. 观察到利润对 $N$ 是线性的：最优 $N$ 不是 0 就是“买到上限”（全量 offset 剩余排放）。这一步极大简化了策略空间。
4. 于是只需比较三种（或少数）策略：  
   - 不用 offsets（Benchmark 0）；  
   - 企业全量 offset（Benchmark F 的低成本区域）；  
   - 只让消费者加购 offsets（Benchmark C 的中等成本区域）。  
   再比较利润，得到 Proposition 5 的“从不同时做”与成本阈值。

下面按论文结构逐个拆解。

### 3.2 Benchmark 0：No Offsets（Proposition 1）

#### 3.2.1 需求与排放的 fixed point

无 offsets 时：

- 冷感需求：$D_d=(1-\gamma)(1-p)$。
- 绿色需求由 $U_g^n(\theta)\ge 0$ 给出购买阈值 $\theta\ge p+\alpha(e+\beta E)$，因此（假设最高估值者参与）：

$$ D_g=\gamma\bigl(1-p-\alpha(e+\beta E)\bigr). $$

总排放：

$$ E=e(D_d+D_g). $$

把 $D_d,D_g$ 代入得到一个线性 fixed point：

$$
E
= e\Bigl[(1-\gamma)(1-p)+\gamma\bigl(1-p-\alpha(e+\beta E)\bigr)\Bigr]
= e\Bigl[1-p-\alpha e\gamma-\alpha\beta\gamma E\Bigr].
$$

整理得：

$$ E = \frac{e(1-p-\alpha e\gamma)}{1+\alpha\beta e\gamma}. $$

#### 3.2.2 企业最优化与均衡

企业利润是

$$ \pi(p)=p(D_d+D_g). $$

把 $E(p)$ 代回后，需求变成 $p$ 的线性函数，于是利润是凹二次函数，FOC 一步得到最优价格：

$$ p^0=\frac{1-\alpha e\gamma}{2}. $$

进而得到均衡需求、排放与利润（Proposition 1）：

$$ D_d^0=\frac{(1-\gamma)(1+\alpha e\gamma)}{2}, $$

$$ D_g^0=\frac{\gamma\bigl(1-\alpha e(2-\gamma+\beta(1-\gamma)(1+\alpha e\gamma))\bigr)}{2(1+\alpha\beta e\gamma)}, $$

$$ E^0=\frac{e(1-\alpha e\gamma)}{2(1+\alpha\beta e\gamma)},\quad \pi^0=\frac{(1-\alpha e\gamma)^2}{4(1+\alpha\beta e\gamma)}. $$

#### 3.2.3 经济学直觉

对照传统垄断（$\alpha=0$）：

- 传统垄断价 $p^M=1/2$，利润 $\pi^M=1/4$。
- 有绿色消费者且 $\alpha>0$ 时，企业反而降价：$p^0<p^M$。原因是：绿色消费者的“碳厌恶”相当于给产品加了一个非货币成本，企业只能降价去补偿，否则绿色需求崩掉。
- 但即便降价，绿色需求仍会下降（相对 $\alpha=0$ 的基准），利润也下降。绿色偏好在垄断者视角下是一种“需求侧的摩擦”。

这为后续引入 offsets 的价值埋下伏笔：offsets 相当于把这层摩擦“货币化”或“可管理化”。

### 3.3 Benchmark F：只在企业层面购买 offsets（Proposition 2）

此时企业选 $(p,N)$，不卖 offsets 给消费者。

关键结构性点：利润对 $N$ 是线性的。直觉上，企业买 1 单位 offsets 的边际收益是“降低 $E$ 从而提高绿色需求/愿付”，边际成本是 $c_o$。在线性设置下，最优会落在角点：要么 $N=0$，要么直接买到把排放清零（碳中和）。

论文给出阈值

$$ c_o^F = 1-\frac{1-\alpha e\gamma}{\sqrt{1+\alpha\beta e\gamma}}. $$

- 若 $c_o>c_o^F$：offsets 太贵，不买，回到 Benchmark 0。
- 若 $c_o\le c_o^F$：企业全量 offset，$E^F=0$。

在全量 offset 下，企业的“有效边际成本”从 0 变为 $c_o$（每卖 1 件就买 1 份 offsets），因此就是一个有边际成本 $c_o$ 的标准垄断定价：

$$ p^F=\frac{1+c_o}{2},\quad D_d^F=\frac{(1-\gamma)(1-c_o)}{2},\quad D_g^F=\frac{\gamma(1-c_o)}{2}, $$

$$ N^F=D_d^F+D_g^F,\quad E^F=0,\quad \pi^F=\frac{(1-c_o)^2}{4}. $$

经济学直觉非常清晰：

- 企业层面 offset 的好处：对绿色消费者来说，产品“变绿”了，需求上升。
- 坏处：成本被摊到所有消费者（包括冷感），导致价格上升，冷感需求下降。
- 何时值得做？当 $c_o$ 足够低，且绿色群体足够大/足够在意企业排放（$\gamma$、$\alpha$、$\beta$、$e$ 足够大），那么吸引绿色群体带来的需求/利润增量足以覆盖“对冷感群体加价造成的损失”。

### 3.4 Benchmark C：只卖 offsets 给消费者（Proposition 3 & 4）

#### 3.4.0 一个关键小 Lemma：绿色消费者对 offsets 的购买是“要么全买，要么全不买”

先考虑消费者的“加购 offsets”决策。

对一个已经决定购买产品的绿色消费者而言，“买 offsets”相对于“不买 offsets”的效用增量是：

$$
\Delta U \equiv U_g^o(\theta)-U_g^n(\theta)
= -p_o+\alpha e+\alpha\beta e
= \alpha e(1+\beta)-p_o.
$$

这个式子有两个非常致命的特征：

1. $\Delta U$ 与 $\theta$ 无关：也就是说，只要一个绿色消费者愿意买产品，那么在给定 $p_o$ 的情况下，他是否加购 offsets 与自己的估值高低无关。
2. $\Delta U$ 也不依赖于 $p$ 与均衡 $E$：它只取决于 offsets 的价格 $p_o$ 与参数 $\alpha e(1+\beta)$。

因此一旦企业把 $p_o$ 设在阈值以下：

$$ p_o \le \bar p_o \equiv \alpha e(1+\beta), $$

那么所有购买产品的绿色消费者都会加购 offsets（$D_g^o=D_g$，$D_g^n=0$）；反之若 $p_o>\bar p_o$，则没有绿色消费者会加购 offsets（$D_g^o=0$，回到 no-offsets 的均衡）。

这就是为什么 Benchmark C（以及全文的 unconstrained model）会出现非常干净的“角点结构”：offsets 要么卖给 0 个绿色消费者，要么卖给全部绿色消费者。

#### 3.4.1 为什么这是一个 price discrimination 菜单？

当企业提供 offsets add-on 且 $p_o\le\bar p_o$ 时，消费者看到两种 bundle：

- 冷感：只关心 $p$，永远不买 offsets。
- 绿色：支付 $p+p_o$ 买“更绿的版本”，且所有绿色购买者都会选择该版本。

于是企业用一个可选 add-on 把市场内生地切成两段，并对两段收不同总价。这是非常标准的二级价格歧视（second-degree price discrimination）：消费者通过自选择（self-selection）暴露类型。

#### 3.4.2 需求与排放（在 offsets 被购买的均衡区域）

在 $p_o\le\bar p_o$ 的区域里，绿色购买者都会买 offsets，因此：

- 冷感需求仍为 $D_d=(1-\gamma)(1-p)$；
- 绿色购买门槛来自 $U_g^o(\theta)\ge 0$：

$$ \theta \ge p+p_o+\alpha\beta E, $$

所以

$$ D_g=\gamma\bigl(1-p-p_o-\alpha\beta E\bigr). $$

而因为绿色消费者购买的每件产品都被 offsets 抵消，且 Benchmark C 下 $N=0$，企业总排放变为

$$ E=e(D-D_g^o)=e(D_d+D_g-D_g)=eD_d. $$

这一步非常关键：$E$ 只由冷感销量决定。

将 $E=eD_d=e(1-\gamma)(1-p)$ 代回绿色需求：

$$
D_g=\gamma\Bigl(1-p-p_o-\alpha\beta e(1-\gamma)(1-p)\Bigr).
$$

#### 3.4.3 企业最优化：两变量凹优化（FOC/KKT 的核心形态）

在 offsets 被购买的区域里，企业利润可写为

$$
\pi(p,p_o)
=p(D_d+D_g)+(p_o-c_o)D_g,
$$

因为 $D_g^o=D_g$。

把 $D_d=(1-\gamma)(1-p)$ 与上面的 $D_g(p,p_o)$ 代入，$\pi(p,p_o)$ 是一个关于 $(p,p_o)$ 的凹二次函数（分母最终是 $4-\alpha^2\beta^2\gamma(1-\gamma)e^2$，保证正则性）。因此 interior 解由一阶条件给出，并且需要检查 KKT 边界是否触发（主要是 $p_o\le\bar p_o$ 是否松弛）。

论文在主体参数区间下得到 interior 解（Proposition 3(ii)）：

$$
p^C=
\frac{2+\alpha\beta\gamma e(1-c_o-\alpha\beta(1-\gamma)e)}{4-\alpha^2\beta^2\gamma(1-\gamma)e^2},
$$

$$
p_o^C=
\frac{\alpha^2\beta^2(1-\gamma)\gamma(1-c_o)e^2-\alpha\beta e(1-\gamma c_o)+2c_o}{4-\alpha^2\beta^2\gamma(1-\gamma)e^2},
$$

并对应的销量、排放与利润为：

$$
D_d^C=\frac{(1-\gamma)\bigl(2-\alpha\beta\gamma(1-c_o)e\bigr)}{4-\alpha^2\beta^2\gamma(1-\gamma)e^2},
$$

$$
D_g^C=\frac{\gamma\bigl(2(1-c_o)-\alpha\beta(1-\gamma)e\bigr)}{4-\alpha^2\beta^2\gamma(1-\gamma)e^2},
$$

$$
E^C=eD_d^C,
$$

$$
\pi^C=\frac{1-(2-c_o)\gamma c_o-\alpha\beta(1-\gamma)\gamma(1-c_o)e}{4-\alpha^2\beta^2\gamma(1-\gamma)e^2}.
$$

#### 3.4.4 Proposition 3 的阈值 $c_o^C$：什么时候企业干脆不卖 offsets？

论文定义（见 Proposition 3）：

$$
c_o^C
=1-\frac{\alpha\beta e(1-\gamma)}{2}
-\frac{\sqrt{\bigl(4-\alpha^2\beta^2\gamma(1-\gamma)e^2\bigr)\bigl(1-\alpha e(\beta(1-\gamma)-\alpha\gamma e+2)\bigr)}}{2\sqrt{\alpha\beta\gamma e+1}}.
$$

结论是：如果 $c_o>c_o^C$，即使企业可以卖 offsets 给消费者，也不会卖（等价于设置 $p_o>\bar p_o$），均衡退化为 no-offsets。

经济直觉：当 offsets 成本太高时，即便用 offsets 做 market segmentation，**补贴的代价也压过了价格歧视带来的收益**。

#### 3.4.5 Proposition 4：企业为什么会亏本卖 offsets？

Proposition 4 证明，在 $c_o\le c_o^C$ 且 offsets 被购买时，

$$ p_o^C<c_o. $$

offsets 亏本卖的机制点在于：企业的利润主要来自产品端的提价与销量结构变化，而不是 offsets 毛利。offsets 在这里是“筛选器/菜单设计成本”，而不是“利润中心”。


此时企业选 $(p,p_o)$，但不在 firm level 买 offsets（$N=0$）。

### 3.5 Unconstrained model：最优策略结构（Proposition 5）

现在回到全文主问题：企业同时可选 firm-level offsets（$N$）与 consumer-level offsets（$p_o$）。

Proposition 5 给出最核心的结构性结论。定义阈值

$$
c_o^* = 1+\frac{2\bigl(\alpha\beta\gamma e-\sqrt{4-\alpha^2\beta^2\gamma e^2(1-\gamma)}\bigr)}{4-\alpha^2\beta^2\gamma e^2},
$$

并且论文证明阈值排序

$$ c_o^*<c_o^F<c_o^C. $$

最优策略是：

1. 若 $c_o\le c_o^*$：企业直接在 firm level 买足 offsets，实现碳中和（等价于 Benchmark F 的全量 offset 解）。
2. 若 $c_o>c_o^*$：企业完全不在 firm level 买 offsets，而是（只要 $c_o\le c_o^C$）选择“卖 offsets 给消费者”的策略（等价于 Benchmark C 的解）。
3. 若 $c_o>c_o^C$：offsets 无论如何都不值得用，回到 Benchmark 0。

一句话：企业永远不会同时做 firm-level offsets 和 consumer-level offsets。

#### 3.5.1 为什么“同时做”不可能最优？（机制解释）

把问题说得更“运营机制”一点：

- firm-level offsets 的本质是：把单位成本抬高到 $c_o$，然后用更高的售价向所有人收费，换来 $E=0$ 带来的绿色需求提升。
- consumer-level offsets 的本质是：不抬高所有人的成本，而是用一个可选 add-on 让绿色消费者自选“更贵但更绿”的 bundle，实现市场细分。

这两种工具解决的是两个不同的问题：

- 如果 offsets 很便宜：最省事的做法就是“一刀切全绿”，直接碳中和，绿色需求最大化，且不需要复杂菜单。
- 如果 offsets 不便宜：对冷感消费者强行加价会损失巨大，此时最优是“把成本与支付责任尽量只对准绿色消费者”，因此用 add-on 菜单做 price discrimination。

“同时做”的策略会出现一种尴尬：你既承担了 firm-level offsets 对冷感消费者的成本（很难回收），又没能比纯 add-on 更好地实现市场细分，典型的 dominated middle option。在线性需求 + 角点结构下，这种 dominated 变得可被严格证明。

### 3.6 关键命题的“结构后果”：利润、排放、价格如何排序？

#### 3.6.1 Corollary 1：利润排序（最优策略必然支配更受限的 benchmark）

记 $\pi^*$ 为 unconstrained model 的最优利润。因为 unconstrained 集合包含所有 benchmark，因此 $\pi^*$ 必然不低于各 benchmark 的利润。论文把这种“显然的”关系写成一个有用的排序（Corollary 1）：

- 若 $c_o\le c_o^*$（最优为 firm-level 碳中和）：

$$ \pi^*=\pi^F>\pi^C>\pi^0. $$

- 若 $c_o^*<c_o\le c_o^C$（最优为 consumer add-on）：

$$ \pi^*=\pi^C>\pi^F\ge\pi^0. $$

直觉：当 offsets 不够便宜时，consumer add-on 的 market segmentation 优势会压过 firm-level 一刀切，因此利润更高。

#### 3.6.2 Proposition 6：排放排序（profit-maximization vs environmental objective 的冲突）

论文用 Proposition 6 给出排放的分段比较。记 $E^*$ 为 unconstrained model 下的排放。

(i) 若 $c_o\le c_o^*$：

$$ 0=E^*=E^F<E^C<E^0. $$

(ii) 若 $c_o^*<c_o\le c_o^F$：

$$ 0=E^F<E^*=E^C<E^0. $$

(iii) 若 $c_o^F<c_o\le c_o^C$：

$$ 0<E^*=E^C<E^F=E^0. $$

这个命题的“管理含义”非常尖锐：

- 允许企业采用 consumer add-on（让消费者自愿 offset）确实能降低排放相对 no-offsets（$E^*<E^0$ 总成立）。
- 但在某些成本区间（尤其是 $c_o^*<c_o\le c_o^F$），profit-maximizing 的最优策略是 consumer add-on 而非 firm-level 碳中和，因此排放会高于“如果强制企业只能做 firm-level offsets”时的排放（因为后者可以做到 0）。  
  换句话说：给企业更多策略自由度，会提高利润，但可能牺牲排放目标的达成程度。

#### 3.6.3 Proposition 7：产品价格排序（offsets 让企业更敢提价）

论文定义一个阈值

$$
\hat c_o=\frac{\alpha\beta\gamma e\bigl(2-\alpha\beta(1-\gamma)e\bigr)}{4+\alpha\beta\gamma e\bigl(2-\alpha\beta(1-\gamma)e\bigr)},
\quad
0<\hat c_o<c_o^*.
$$

并给出价格排序（Proposition 7）：

(i) 若 $c_o\le\hat c_o$：

$$ p^C>p^*=p^F>p^0. $$

(ii) 若 $\hat c_o<c_o\le c_o^*$：

$$ p^*=p^F>p^C>p^0. $$

(iii) 若 $c_o^*<c_o\le c_o^F$：

$$ p^F>p^*=p^C>p^0. $$

(iv) 若 $c_o^F<c_o\le c_o^C$：

$$ p^*=p^C>p^F=p^0. $$

一句话总结：不论 offsets 以哪种方式引入，企业都更倾向于提价；差别只在于 firm-level offsets 时价格对 $c_o$ 更敏感（边际成本上升），而 consumer add-on 允许企业把成本压力更多放在 $p_o$ 与需求结构上。

### 3.7 比较静态 Comparative Statics（定性结论抓住就够）


论文把关键阈值写成 $\alpha,\beta,\gamma,e$ 的函数。虽然完整偏导数很丑，但方向性直觉很稳：

1. $\gamma$（绿色占比）越大：企业越愿意为“变绿”付出成本，因此 $c_o^*,c_o^F,c_o^C$ 一般会提高（offsets 成本容忍度上升）。
2. $\alpha$（绿色厌恶强度）越大：绿色群体对排放更敏感，offsets 带来的需求提升更大，因此阈值上升。
3. $e$（单件排放）越大：排放带来的需求损失更大，offsets 的价值更大，因此阈值上升。
4. $\beta$（在意企业总排放）越大：这是决定“企业是否会选择碳中和”的关键。  
   - 若 $\beta=0$，论文直接指出 $c_o^*=0$：企业永远不会选择全量碳中和。  
   - 直觉：如果绿色消费者只在意自己那一单的排放，而不在意企业对冷感消费者造成的排放，那么企业没有动力为冷感消费者的排放买 offsets（买了也赚不到需求回报）。
5. $c_o$ 上升时的均衡比较：  
   - 在 firm-level offset（碳中和）策略下，$p^F=(1+c_o)/2$ 单调上升，需求单调下降。  
   - 在 consumer add-on 策略下，企业会在 $p$ 与 $p_o$ 之间做“谁来承担成本”的重新分配：一般表现为 $p_o^C$ 随 $c_o$ 上升但仍低于 $c_o$，而 $p^C$ 可能略降以维持需求（Figure 5 中 $p^C$ 基本平缓）。

---

## 4 主要结论与管理启示 Main Results & Managerial Insights

### 4.1 机制揭示：offsets 不是 CSR 附件，而是菜单与筛选器

本文最值得带走的机制观点是：

- consumer-level offsets 的真正功能是 **market segmentation + price discrimination**，而不是 offsets 业务的直接利润。
- 企业通过设计两种 bundle：  
  - 基础产品（给冷感消费者）：价格 $p$；  
  - 绿色 bundle（给绿色消费者）：价格 $p+p_o$，并通过 offsets 把“碳厌恶的非货币成本”转化为“可付费的货币成本”。

这会产生两个结果：

1. 绿色消费者的有效购买门槛下降（因为 disutility 降低），需求上升；
2. 企业可以提高基础价格 $p$（相对 no-offsets benchmark），即便冷感需求下降，仍可能因更高单价而提高利润。

### 4.2 反直觉结果与 trade-off

这里有三个很“反直觉但合理”的 trade-off：

1. offsets 会推高产品价格：无论是 firm-level 还是 consumer-level，最优 $p$ 都高于 no-offsets 的 $p^0$（见 Proposition 7）。  
   直觉：offsets 让绿色需求变得更“可赚”，垄断者因此敢于提价。
2. 企业可能更绿但排放不为零：当 $c_o$ 处于中等区间时，最优策略是只让绿色消费者 offset，冷感消费者排放不被抵消，$E^*=E^C=eD_d^C>0$。  
   这揭示了一个利润最大化下的“选择性减排”：只对能带来需求回报的那部分减排。
3. “碳中和”需要消费者关心企业总排放：如果 $\beta$ 很小甚至 0，企业即便面对绿色消费者，也会倾向于让绿色消费者自己 offset，而不是为所有人碳中和。这是一个对 NGO 信息披露、企业碳足迹透明度政策非常重要的结论：提高 $\beta$（让消费者更在意企业总排放）会把企业推向更彻底的减排/碳中和。

### 4.3 管理建议：三段式决策规则（非常可操作）

把 Proposition 5 翻译成管理语言，就是一个“三段式 if-then”：

1. offsets 成本很低（$c_o\le c_o^*$）：  
   - 直接 firm-level 全量 offset，实现 net-zero；  
   - 把 offsets 成本打进产品价格（$p^F=(1+c_o)/2$）；  
   - 适用于 offsets 便宜或企业能拿到高质量低价 offsets 的行业/时期。
2. offsets 成本中等（$c_o^*<c_o\le c_o^C$）：  
   - 不要 firm-level offset；  
   - 在交易界面提供 offsets add-on，并且要把 $p_o$ 设在低于成本的位置（subsidize），以确保绿色消费者愿意选择绿色 bundle；  
   - 本质是做 price discrimination：用 offsets 作为“筛选器”区分绿色与冷感。
3. offsets 成本很高（$c_o>c_o^C$）：  
   - offsets 既不该买也不该卖；  
   - 更可能的方向是继续内部减排技术投资、等待 offsets 市场价格变化，或采用别的低碳机制（例如 SAF 贡献等）。

### 4.4 图表解读（把图看懂，等于看懂论文一半）

#### Figure 1：offsets 定价为什么必然低于成本？

Figure 1 画的是 $p_o^C$（最优 offsets 售价）、$c_o$（成本）与 $\bar p_o$（消费者愿付上限）的关系。

读图要点：

- $p_o^C$ 始终在 $c_o$ 下方：对应 Proposition 4，企业亏本卖 offsets。
- 即便 $c_o$ 高到超过 $\bar p_o$，企业仍可能通过把 $p_o$ 压得更低（补贴）来诱导绿色消费者购买 offsets，因为 offsets 的价值来自“让绿色 bundle 存在并可自选”，而不来自 offsets 自身盈利。

#### Figure 2 & 3：哪些市场会走向碳中和？

Figure 2（$\gamma=0.5$）与 Figure 3（$\gamma=0.25$）在 $(\alpha,\beta)$ 平面上画出了最优策略区域（给定 $e=1$ 与不同 $c_o$）。

读图要点：

- Region F（企业碳中和）只在 $\alpha$ 与 $\beta$ 都足够高时出现：绿色消费者既要“很在意排放”（$\alpha$ 高），也要“在意企业总排放”（$\beta$ 高）。
- 当绿色占比下降（从 0.5 到 0.25），Region F 明显缩小甚至消失：绿色群体太小，碳中和难以靠需求回报“收回成本”。
- Region C（只让消费者加购 offsets）通常占据更大面积，尤其当 $c_o$ 较高时：昂贵 offsets 更适合做 add-on，而不是一刀切让所有人买单。
- Region 0（完全不用 offsets）只在 $\alpha$ 很低时出现：也就是消费者基本不在意碳排，那 offsets 就是纯成本。

#### Figure 4：利润与排放的张力在哪里？

Figure 4 左：利润随 $c_o$ 变化；右：排放随 $c_o$ 变化。三条竖线分别是 $c_o^*$、$c_o^F$、$c_o^C$。

读图要点：

- 当 $c_o\le c_o^*$，最优策略是 firm-level 碳中和，排放为 0。
- 当 $c_o^*<c_o\le c_o^C$，最优策略转为 consumer add-on，此时排放跳到一个正值（只剩冷感排放）。  
  这体现了利润最大化与减排程度之间的张力：企业愿意“部分变绿”，但不愿为冷感消费者承担 offsets 成本。
- 重要政策含义：如果监管者或社会希望企业更彻底减排，仅靠“允许消费者自愿 offset”可能不够，因为利润最大化企业会停在一个正排放水平。

#### Figure 5：offsets 为什么会推高产品价格？

Figure 5 对比了不同策略下的产品价格 $p$。

读图要点：

- 不论哪种 offsets 策略，$p$ 都高于 no-offsets 的 $p^0$：offsets 让企业有更强的提价空间（绿色需求更愿意买单）。
- firm-level 碳中和时 $p^F$ 随 $c_o$ 上升（因为边际成本上升）。
- consumer add-on 时 $p^C$ 相对平缓，反映了企业把“成本回收”更多放在 $p_o$ 与需求结构上，而不是单纯抬高 $p$。

#### Figure 6 & 7：利润与销量从哪里来？

Figure 6 把利润拆成冷感 vs 绿色两部分；Figure 7 把销量拆成冷感 vs 绿色两部分。

读图要点：

- offsets 策略普遍牺牲冷感销量（Figure 7 左），但可能通过更高价格让冷感利润不降反升（Figure 6 左）。
- offsets 策略显著提高绿色销量（Figure 7 右），这是 offsets 之所以“值得”的核心来源。
- 当最优从 firm-level 切换到 consumer add-on（$c_o$ 越过 $c_o^*$），绿色利润随 $c_o$ 下降，体现 offsets 补贴的代价（Figure 6 右）。

### 4.5 Extensions（论文自己已经提示的拓展）

1. 更一般的参数区间（Online Appendix A）：当条件 (6) 不满足时，会出现一些额外的均衡形态（例如绿色消费者可能在某些参数下完全退出市场、或 offsets 定价触及上界等）。主文为可读性聚焦在更“现实常见”的区域，但 Appendix 给出了完整分段解。
2. 消费者福利（Appendix B）：  
   - Lemma B-1：当 $c_o$ 足够低时，碳中和策略不仅利润高，消费者总 surplus 也更高（绿色 disutility 的下降超过了价格上升的损失）。  
   - Lemma B-2：当 $c_o$ 较高但仍处于“最优为 consumer add-on”的区间时，消费者 surplus 反而可能低于 no-offsets（企业提价 + offsets 补贴结构导致冷感消费者受损）。  
   这为“利润最大化 vs 社会福利”提供了一个可以继续写下去的规范性议题。
3. 应用外延：论文在结论中指出，模型不仅适用于 carbon offsets，也适用于诸如航空业让乘客为 SAF（sustainable aviation fuel）出资的机制——本质都是“企业是否自己承担减排成本，还是把它做成可选 add-on”。

---

## 5 Reviewer's Critique（以 Senior Editor/Reviewer 的视角）

### 5.1 优点（值得发表在哪里？为什么）

1. 问题选得对：offsets add-on 在航空/物流/电商等场景高度普遍，但理论上缺少清晰的机制解释。本文抓住了一个“实践中已经在发生、学术上还没讲清楚”的空白。
2. 结构性结论干净：Proposition 5 的“从不同时做”与三段式阈值是非常强的结构结果，易被后续研究引用与扩展。
3. 机制解释有穿透力：**把 offsets 从“CSR 成本项”转译为“price discrimination 菜单工具”**，这在 OM 与 Marketing 的交叉语境里很有价值。
4. 环境含义不被牺牲：不仅谈利润，也系统比较排放（Proposition 6）与消费者 surplus（Appendix B），让文章不只是“教企业怎么赚钱”，也能对政策讨论有贡献。

### 5.2 主要局限与可能的质疑点（Reviewer 会抓着不放的）

1. 垄断假设：很多典型行业（航空、快递、电商）竞争激烈。竞争下 offsets 可能变成差异化维度，甚至触发“绿色军备竞赛”。垄断结果能否在 duopoly/oligopoly 中保持同样的角点结构？不确定。
2. offsets 的“质量与可信度”被抽象掉：现实中 offsets 存在 additionality、permanence、leakage 等争议，消费者也可能不信任（greenwashing 风险）。若把 offsets 质量/可信度引入（例如概率有效、或需第三方认证），$p_o$ 的最优补贴结构可能会变化。
3. 消费者对企业总排放的认知形式：模型用线性项 $\beta E$ 表示。但现实中消费者可能更关注“每件产品的碳足迹标签”（per-unit）或“是否达成碳中和承诺”（binary），而不是对总排放水平线性敏感。不同信息呈现方式可能改变阈值与策略。
4. $e$ 外生：文章假设企业已完成所有可行内部减排，剩余排放才考虑 offsets。现实里企业会在“内部减排 vs offsets”之间优化（这与 Gao & Souza 2022 等更接近）。把 $e$ 内生化可能会引入新的替代关系与多阶段决策。
5. offsets add-on 的运营实现成本为零：线上加购 offsets 并非完全无摩擦（界面设计、交易成本、第三方合作、合规、审计）。若加入固定成本或每单运营成本，consumer add-on 区域可能缩小。
6. 行为因素缺失：现实中 offsets 的购买与否受 default 选项、框架效应、道德许可（moral licensing）等影响。若消费者不是完全理性、或存在偏误，企业的最优补贴策略可能更复杂。

### 5.3 未来研究方向（值得继续“把这篇论文写成三篇”）

1. 竞争模型：两家企业同时决定 $p$ 与 offsets 策略，offsets 作为垂直差异化。关键问题是：consumer add-on 还能否形成稳定均衡？还是会被竞争压缩成成本战？
   > ?
2. offsets 质量与认证：引入 offsets 的质量 $q$（有效概率、或消费者感知质量），并允许企业选择“高质量高成本 vs 低质量低成本”，研究最优 portfolio 与定价。
3. 内生减排与动态：企业先投资减排（降低 $e$），再决定 offset；或者跨期承诺 net-zero，消费者逐期更新信念。动态承诺与声誉可能改变“从不同时做”的结论。
4. 连续异质性消费者：让绿色偏好不是两段式，而是连续分布（例如 $\alpha$ 分布）。这样 offsets add-on 可能演化为更一般的 menu design（多档 offsets、或多档绿色产品线）。
5. 政策介入：引入碳税、cap-and-trade、或对 offsets 使用的限制（例如只能用于不可控排放），研究政策如何改变 $c_o^*$ 与企业是否碳中和。

---

## 6 One More Thing（我认为最值得分享的“灵光一现”）

这篇文章最让我觉得“啊哈”的瞬间是：offsets 作为 add-on 时，企业明知会亏本卖（$p_o<c_o$），却仍然理性地这么做，因为 offsets 在模型里不是一个商品，而是一把“分割市场的刀”。

更形象地说：

- offsets 不是利润中心，而是一个筛选器（screening device）。
- 通过给出一个“更绿但更贵”的 bundle，企业把消费者自己变成了分类器：绿色消费者主动举手说“我愿意付更多”，冷感消费者则选择基础产品。
- 一旦这个分类完成，企业就能在基础产品上提价，把两端的利润都抬起来；offsets 的补贴只是买这把刀的成本。

这种把“环保行为”转译为“机制设计工具”的视角，非常 OM+Marketing：它让我们更清楚地理解企业为什么会做出看似矛盾的绿色策略——很多时候，不是因为慈悲，而是因为菜单设计真的很好用。
****
# Endogenous Commitments: Implications for Supply Chains

作者：Narendra Singh，Graduate School of Business, Nazarbayev University  
年份：2026  
期刊：Manufacturing & Service Operations Management，Articles in Advance  
笔记日期：2026_06_03  
原文主题：Durable products；Strategic consumers；Time inconsistency；Endogenous commitment；Supply chain management

中文摘要：

这篇文章研究耐用品供应链中的一个核心问题：在制造商通过零售商销售耐用品时，制造商是否要提前承诺未来批发价，零售商是否要提前承诺未来零售价？已有研究多从集中式企业或外生给定承诺出发，通常认为“承诺未来价格”可以缓解战略消费者等待降价所带来的 time-inconsistency 问题。但本文发现，在分散式供应链中，承诺不是单个企业自己的工具，而是制造商与零售商相互影响的战略选择。用两期博弈模型分析后，作者证明均衡中要么制造商和零售商都承诺，要么双方都不承诺；只有一方承诺不是稳定均衡。更反直觉的是，拥有承诺能力本身可能让两家企业都变差，形成类似 prisoner’s dilemma 的局面。相较于外生承诺，内生选择“不承诺”有时也会伤害零售商和整个供应链，因为制造商可能通过提高第一期批发价来阻止零售商承诺。文章还研究了供应链协调、零售商跨期库存和 price protection policies，证明核心结论在扩展模型下基本稳健。

## 论文速览表格

| 维度 | 内容 |
|:---|:---|
| 核心研究问题 | 在耐用品的分散式供应链中，制造商和零售商如果可以自己选择是否承诺未来价格，均衡会怎样？这种内生承诺选择如何影响企业利润和供应链协调？ |
| 场景 | 一个制造商通过一个零售商销售 durable goods。消费者可以第一期购买，也可以等待第二期降价。 |
| 主要玩家 | 制造商 $M$、零售商 $R$、战略消费者。 |
| 关键决策 | 制造商是否提前承诺第二期批发价 $w_2$；零售商是否提前承诺第二期零售价 $p_2$；两期中的批发价、零售价和销量。 |
| 关键参数 | 消费者折扣因子 $\rho_c$ 表示消费者等待未来消费的耐心，即 strategic consumer behavior；企业折扣因子 $\rho_f$ 表示企业对未来利润的耐心。 |
| 方法 | 两期动态博弈；Subgame Perfect Nash Equilibrium；与 centralized benchmark、exogenous commitment benchmark 比较；扩展到 inventory carryover 和 price protection policies。 |
| 均衡结构 | 均衡中只会出现 $NN$ 或 $CC$：双方都不承诺，或双方都承诺。$NC$ 和 $CN$ 不是 SPNE。 |
| 最重要机制 | 当零售商想承诺未来零售价时，制造商可能提高第一期批发价 $w_1$ 来“吓退”零售商，使其不承诺。这形成 induced noncommitment。 |
| 反直觉发现 | 承诺能力并不总是好事；它可能让制造商和零售商都更差。消费者更战略也不一定伤害供应链，某些区间内反而改善协调。 |
| 管理含义 | 渠道企业不能直接套用“集中式企业应承诺未来价格”的结论。承诺决策要和渠道伙伴的反应一起考虑。 |

## TL;DR

在集中式耐用品市场，提前承诺未来价格通常是好事，因为它能阻止消费者等降价；但在制造商—零售商供应链中，承诺变成了两家企业之间的战略互动。本文发现，均衡里要么双方都承诺，要么双方都不承诺；更重要的是，拥有承诺能力本身可能让双方陷入囚徒困境，利润反而下降。

最值得记住的一句话：**在分散式供应链里，“能承诺”不是免费选项，它会改变对方的策略空间，进而反过来伤害自己。**

## One More Thing：最值得讲给别人听的洞察

最妙的地方不是“双方都承诺”或“双方都不承诺”本身，而是中间的 induced noncommitment。零售商本来想承诺未来零售价，借此减少消费者等待降价；但制造商知道，如果零售商这样做，自己未来的批发定价空间会被改变。于是制造商在第一期故意把批发价 $w_1$ 抬高，让零售商觉得承诺不划算，最后双方都不承诺。表面上看，企业没有使用承诺；但实际上，仅仅因为承诺选项存在，制造商就扭曲了当前批发价。这意味着一个很深的点：**“最后没有承诺”不等于“承诺能力没有影响”。**

这个洞察对 OM/Marketing 很有价值，因为它提醒我们，很多机制设计工具即使在均衡路径上没有被使用，也会通过 off-equilibrium threat 改变均衡价格、销量和利润。

## 研究背景与动机 (Motivation)

### 实践痛点

耐用品行业普遍存在 intertemporal pricing。电子产品、汽车、家具、家电等产品常用 price skimming：新品上市先高价，之后逐步降价。消费者也越来越能够观察和预测降价，原因包括价格历史网站、比价工具、降价提醒、购物插件等。消费者越清楚未来可能降价，就越可能推迟购买。

这导致经典 durable goods monopolist 的 time-inconsistency problem：企业第一期希望消费者现在买，但一旦高价值消费者已经购买，企业第二期又有动力降价卖给剩下的低价值消费者。理性消费者预期到这一点，就会等。最后，企业的动态定价能力反而会伤害利润。

### 理论缺口

经典结论主要来自 centralized firm：一个垂直整合企业直接面向消费者销售。对这种企业而言，commitment to future prices 通常有价值，因为它可以让消费者相信未来不会大幅降价，从而减少等待。

但现实中的 durable goods 很多通过渠道销售。例如 Samsung 手机通过 Best Buy，Toyota 汽车通过经销商。此时价格分成两层：制造商定批发价，零售商定零售价。制造商是否承诺 $w_2$ 会影响零售商是否承诺 $p_2$；零售商是否承诺 $p_2$ 也会影响制造商的未来批发定价。因此，commitment 不再是单个企业面对消费者的承诺，而是渠道成员之间的战略互动。

已有 decentralized supply chain 研究对 commitment 的结论并不一致。一些文献认为 commitment 可以提升供应链绩效，另一些文献发现 commitment 可能伤害承诺方和非承诺方。但这些研究通常把 commitment 当成外生给定，或者只允许某一方承诺。本文的切入点是：**如果制造商和零售商都能自己决定是否承诺，均衡到底是什么？**

### 核心贡献

1. 将制造商的 wholesale price commitment 和零售商的 retail price commitment 同时内生化，研究它们之间的战略互赖。
2. 证明均衡中不会出现只有一方承诺；稳定结果只有 $NN$ 或 $CC$。
3. 识别出 induced noncommitment：制造商通过提高 $w_1$ 阻止零售商承诺。
4. 说明 commitment capability 本身可能伤害双方，推翻“多一个选项不会更差”的直觉。
5. 将企业利润、消费者战略性和 supply chain coordination 放在同一框架下比较，并扩展到 inventory carryover 和 price protection policies。

## 模型设定与假设 (Model Setup & Assumptions)

### 符号体系

#### 玩家与时间

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $M$ | Manufacturer | 生产耐用品并通过零售商销售。 |
| $R$ | Retailer | 从制造商采购并向消费者销售。 |
| $t=1,2$ | 两个销售期 | 第一期开售，第二期可继续销售。 |
| $i\in\{NN,NC,CN,CC\}$ | 承诺状态 | 第一个字母表示制造商是否承诺 $w_2$，第二个字母表示零售商是否承诺 $p_2$。$N$ 表示 no commitment，$C$ 表示 commitment。 |

#### 价格与销量

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $w_1,w_2$ | 第一、二期批发价 | 由制造商设定。$w_2$ 可能在第一期被提前承诺。 |
| $p_1,p_2$ | 第一、二期零售价 | 由零售商设定。$p_2$ 可能在第一期被提前承诺。 |
| $q_1,q_2$ | 第一、二期销量 | 消费者购买一次后不再重复购买。 |
| $Q_1,Q_2$ | 订货量 | 只在 inventory carryover 扩展中使用。 |
| $I=Q_1-q_1$ | 跨期库存 | 零售商第一期多订并留到第二期。 |

#### 消费者偏好

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $\theta\sim U[0,1]$ | 消费者估值 | 单位质量消费者，估值异质。 |
| $\rho_c\in[0,1)$ | 消费者折扣因子 | 越高表示消费者越有耐心、越战略，越愿意等第二期。$\rho_c=0$ 表示 myopic consumers。 |
| $U_1(\theta,p_1)$ | 第一期购买效用 | $U_1=\theta-p_1$。 |
| $U_2(\theta,p_2)$ | 第二期购买效用 | $U_2=\theta-p_2$。若第一期等待，则按 $\rho_c$ 折现。 |

#### 企业利润

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $\rho_f\in[0,1]$ | 企业折扣因子 | 越高表示企业越重视未来利润；越低表示企业更急于获得当前利润。 |
| $\Pi_M$ | 制造商两期折现利润 | $\Pi_M=\Pi_{M,1}+\rho_f\Pi_{M,2}$。 |
| $\Pi_R$ | 零售商两期折现利润 | $\Pi_R=\Pi_{R,1}+\rho_f\Pi_{R,2}$。 |
| $\Pi_S$ | 分散式供应链总利润 | $\Pi_S=\Pi_M+\Pi_R$。 |
| $\Pi_I$ | 集中式供应链利润 | Benchmark 中的 integrated firm 利润。 |

#### 阈值函数

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $\rho_c^x(\rho_f)$ | voluntary $NN$ 与 induced $NN$ 的边界 | 消费者战略性超过该阈值后，制造商需要通过抬高 $w_1$ 来阻止零售商承诺。 |
| $\rho_c^y(\rho_f)$ | $NN$ 与 $CC$ 的边界 | 消费者足够战略且企业足够不耐心时，双方进入 $CC$。 |
| $\rho_c^z(\rho_f)$ | 零售商在 endogenous vs. exogenous commitment 下利润比较的边界 | 超过某一区间时，内生选择反而可能伤害零售商。 |
| $\rho_c^w(\rho_f)$ | supply chain profitability index 先升后降的拐点 | 低于该阈值，战略消费者增加改善协调；高于该阈值，协调恶化。 |
| $\rho_c^v(\rho_f)$ | endogenous 与 exogenous coordination 比较的边界 | 内生承诺下协调可能高于或低于外生承诺。 |

### 博弈与决策结构

Base model 的决策顺序如下。

1. 第一期开头，制造商决定是否承诺第二期批发价 $w_2$。
   1. 若不承诺，只设置 $w_1$。
   2. 若承诺，同时设置 $w_1$ 和 $w_2$。
2. 零售商观察制造商决策后，决定是否承诺第二期零售价 $p_2$。
   1. 若不承诺，只设置 $p_1$。
   2. 若承诺，同时设置 $p_1$ 和 $p_2$。
3. 消费者决定第一期是否购买。
4. 第二期，如果某个价格没有在第一期被承诺，则相应企业在第二期设定该价格。
   1. 若制造商没有承诺 $w_2$，则第二期先设 $w_2$。
   2. 若零售商没有承诺 $p_2$，则第二期再设 $p_2$。
5. 未购买的消费者决定第二期是否购买。

Information structure：所有已设定价格和承诺状态都是公开可观察的。如果 $p_2$ 没有被零售商承诺，消费者会基于 $p_1$ 形成 rational expectations $p_2^e(p_1)$。

Figure 1 的作用是把这套决策树画出来。图中四条路径分别对应 $NN$、$NC$、$CN$、$CC$：在 $NN$ 下，第二期制造商和零售商都还要行动；在 $CC$ 下，第二期两家企业都不用再设价。

### 消费者效用与需求

消费者第一期购买的净效用为：

$$
U_1(\theta,p_1)=\theta-p_1.
$$

> 直觉：高估值消费者更愿意买；价格越高，购买效用越低。

消费者第二期购买的净效用为：

$$
U_2(\theta,p_2)=\theta-p_2.
$$

若消费者第一期不买而等待第二期，其效用按 $\rho_c$ 折现。因此，消费者第一期购买的条件是：

$$
U_1(\theta,p_1)\ge \max\{\rho_c U_2(\theta,p_2),0\}.
$$

如果零售商没有承诺 $p_2$，消费者用预期价格 $p_2^e(p_1)$ 代替实际 $p_2$。

> 直觉：$\rho_c$ 是整篇文章的消费者战略性参数。$\rho_c$ 越高，等待未来消费的损失越小，消费者越容易推迟购买。企业面对的 time-inconsistency problem 越强。

给定第一期销量 $q_1$ 和第二期零售价 $p_2$，第二期需求为：

$$
q_2(q_1,p_2)=1-q_1-p_2.
$$

> 直觉：第一期已经买过的消费者不再购买，所以剩余市场规模是 $1-q_1$；在剩余消费者中，只有估值高于 $p_2$ 的人购买。

在 $NN$ 情形下，第二期均衡为：

$$
w_2^{NN}(q_1)=\frac{1-q_1}{2},\quad
p_2^{NN}(q_1)=\frac{3(1-q_1)}{4},\quad
q_2^{NN}(q_1)=\frac{1-q_1}{4}.
$$

> 直觉：第二期是一个标准的 sequential double-marginalization 问题。制造商先加价，零售商再加价，最终零售价比集中式更高，销量更低。

在 $NN$ 情形下，由 rational expectations 诱导的第一期需求为：

$$
q_1^{NN}(p_1)=1-p_1-\frac{\rho_c}{4-\rho_c}p_1.
$$

> 直觉：如果消费者完全 myopic，即 $\rho_c=0$，需求退化为 $q_1=1-p_1$。当 $\rho_c$ 上升时，等待诱因增强，给定 $p_1$ 的第一期销量下降。零售商要想卖出同样数量，必须降价。

### 企业利润函数

Base model 中生产成本归一化为零，且不允许零售商跨期库存。制造商两期利润为：

$$
\Pi_M=q_1w_1+\rho_f q_2w_2.
$$

> 直觉：制造商第一期从每单位批发价 $w_1$ 中获得收入，第二期从 $w_2$ 中获得收入。第二期利润按 $\rho_f$ 折现；$\rho_f$ 越低，制造商越不愿意为未来利润等待。

零售商两期利润为：

$$
\Pi_R=q_1(p_1-w_1)+\rho_f q_2(p_2-w_2).
$$

> 直觉：零售商赚取零售价格和批发价格之间的 margin。承诺 $p_2$ 的好处是影响消费者等待行为；坏处是可能限制第二期应对制造商和消费者的灵活性。

集中式 benchmark 的利润为：

$$
\Pi_I=q_1p_1+\rho_f q_2p_2.
$$

> 直觉：集中式企业没有 wholesale-retail margin 的内部冲突，因此只面对消费者跨期等待问题，不面对渠道成员之间的战略定价问题。

### 关键假设

| 假设 | 合理性说明 | 若放松可能的影响 |
|:---|:---|:---|
| 两期模型 | durable goods 文献常用两期框架捕捉 time inconsistency 与 price skimming。 | 多期或连续时间会强化 Coase-type pressure，承诺价值与阈值区域可能变化。 |
| 消费者估值 $\theta\sim U[0,1]$ | 使需求线性，便于闭式解和阈值分析。 | 非均匀分布可能改变阈值，但机制仍可能存在：等待、承诺、渠道加价。 |
| 消费者购买一次后不再购买 | 符合耐用品特征。 | 若有替换购买或产品升级，第二期需求会更复杂，可能削弱或增强降价诱因。 |
| 生产成本为零 | 归一化处理，不改变核心 trade-off。 | 正成本会平移价格与利润，但通常不改变战略承诺机制。 |
| 制造商先动，零售商后动 | 反映上游 wholesale contract 先于下游 retail pricing 的常见渠道结构。 | 若零售商拥有更强议价权或价格同时设定，均衡承诺区域可能改变。 |
| 企业共用折扣因子 $\rho_f$ | 简化分析，文献中常见。作者也说明不同企业折扣因子的稳健性。 | 异质 $\rho_M,\rho_R$ 会让承诺区间更复杂，尤其会影响谁更愿意承诺。 |
| Base model 不允许库存跨期 | 先隔离 commitment mechanism。 | 允许库存后，零售商可用 strategic inventory 影响未来 wholesale price；文章扩展证明核心结论稳健。 |
| 承诺可信 | 主模型先研究承诺选择本身。 | 若承诺不可信，需要额外 commitment device；文章用 price protection policies 扩展处理。 |

## 分析路线图 (Roadmap of Analysis)

1. **Centralized benchmark**：先证明一个垂直整合企业总是愿意承诺未来零售价。这是经典 durable goods 逻辑。
2. **Decentralized subgames**：固定制造商是否承诺，分析零售商是否承诺。这里得到两个关键子结论：如果制造商承诺，零售商也会承诺；如果制造商不承诺，零售商是否承诺取决于 $w_1$、$\rho_c$、$\rho_f$。
3. **Endogenous equilibrium**：制造商在第一期最先选择承诺策略，预期零售商反应，最终得到 $NN$ 或 $CC$ 两类均衡。
4. **Profit implications**：比较消费者战略性、企业耐心、commitment capability、endogenous vs. exogenous commitment 对制造商和零售商利润的影响。
5. **Supply chain coordination**：用 supply chain profitability index 衡量分散式供应链相对于集中式供应链的协调程度。
6. **Extensions**：加入零售商 strategic inventory；再研究 price protection policies 是否能作为 credible commitment devices。

## 核心分析与求解 (Analysis & Solution)

### Proposition 1：集中式供应链总是承诺未来价格

Proposition 1 建立 benchmark：如果供应链是 vertically integrated，单个决策者会选择在第一期承诺第二期零售价 $p_2$。并且相较于不承诺，承诺下有：

$$
p_1^C\ge p_1^N,\quad p_2^C\ge p_2^N,
$$

$$
q_1^C\ge q_1^N,\quad q_2^C\le q_2^N,
$$

$$
q_1^C+q_2^C\le q_1^N+q_2^N.
$$

> 直觉：集中式企业的唯一麻烦是消费者等降价。不承诺时，企业只能通过降低 $p_1$ 来诱导消费者现在买，但消费者会从低 $p_1$ 推断未来 $p_2$ 也低，等待动机反而更强。承诺 $p_2$ 后，企业可以直接用较高的未来价格威慑等待，因此第一期销量上升，第二期销量下降，总利润提高。

这个命题给后文制造了张力：**为什么在 centralized firm 中总是有利的 commitment，到了 decentralized supply chain 中会变得可能有害？**

### Lemma 1：制造商不承诺时，零售商的承诺激励取决于 $w_1$

在制造商不承诺 $w_2$ 的前提下，零售商可能承诺 $p_2$，也可能不承诺。关键取决于第一期批发价 $w_1$ 是否足够低。

若 $w_1$ 低于某个阈值，零售商选择承诺 $p_2$，并设置：

$$
p_1^{NC}(w_1)=\frac{1+w_1}{2},\quad
p_2^{NC}(w_1)\ge \frac{1+w_1}{2},
$$

且结果是：

$$
q_1^{NC}(w_1)=\frac{1-w_1}{2},\quad q_2^{NC}(w_1)=0.
$$

如果 $w_1$ 较高，零售商不承诺；如果 $w_1$ 非常高，甚至第一期也可能没有销售。

> 直觉：当制造商没有承诺 $w_2$ 时，零售商若提前承诺 $p_2$，第二期会被制造商“拿捏”：制造商可以在第二期把 $w_2$ 提到接近 $p_2$，吃掉零售商的第二期 margin。因此，零售商承诺时会把 $p_2$ 设得足够高，使第二期没有销量，避免被制造商剥夺 surplus。这样做的目的不是赚第二期钱，而是通过高未来价让消费者第一期购买。

这个 lemma 说明，零售商承诺不是单纯的消费者管理工具，还要考虑制造商在第二期的 opportunistic pricing。

### Lemma 2：制造商一旦承诺，零售商也会承诺

Lemma 2 研究相反情形：若制造商已经承诺 $w_2$，零售商的最优反应是也承诺 $p_2$。形式上：

$$
\Pi_R^{CC}(w_1,w_2)\ge \Pi_R^{CN}(w_1,w_2).
$$

> 直觉：制造商承诺 $w_2$ 后，零售商不再担心第二期被制造商临时提高 wholesale price 抽走利润。给定 $w_1,w_2$，零售商的问题变成一个带有外生边际成本的 durable goods monopolist 问题。因此，零售商承诺 $p_2$ 可以缓解消费者等待，且不会带来额外被制造商剥削的风险。

这个 lemma 直接排除了 $CN$ 成为均衡的可能性：如果制造商承诺而零售商不承诺，零售商会偏离为承诺。

### Proposition 2：内生承诺均衡只会是 $NN$ 或 $CC$

前两个 lemma 给出了零售商的反应。Proposition 2 进一步把制造商的第一期选择纳入，刻画整个博弈的 SPNE。

存在阈值 $\rho_c^x(\rho_f)$ 和 $\rho_c^y(\rho_f)$，使得均衡结构如下。

1. 当 $\rho_c<\min\{\rho_c^y(\rho_f),1\}$ 时，制造商和零售商都不承诺，即 $NN$。
   1. 若 $\rho_c\le \rho_c^x(\rho_f)$，这是 **Voluntary NN**：双方自愿不承诺。
   2. 若 $\rho_c^x(\rho_f)<\rho_c<\min\{\rho_c^y(\rho_f),1\}$，这是 **Induced NN**：零售商本来有承诺激励，但制造商提高 $w_1$ 阻止她承诺。
2. 当 $\rho_c^y(\rho_f)\le \rho_c<1$ 时，制造商和零售商都承诺，即 $CC$。

$NC$ 和 $CN$ 都不是 SPNE。

> 直觉：$NC$ 不稳定，因为如果零售商承诺 $p_2$ 而制造商不承诺 $w_2$，制造商会在第二期把批发价提高并抽走零售商第二期利润。零售商预期到这一点，会把 $p_2$ 设得很高，使第二期无销量，反而伤害制造商。因此制造商要么提前也承诺，要么在第一期提高 $w_1$ 让零售商放弃承诺。$CN$ 不稳定，因为制造商一旦承诺 $w_2$，零售商承诺 $p_2$ 就是最优反应。

Figure 2 很直观地展示了这一点。横轴是消费者折扣因子 $\rho_c$，纵轴是企业折扣因子 $\rho_f$。左下或中间区域可能是双方不承诺；右下区域即消费者很战略、企业比较不耐心时，双方都承诺；左上区域则是 voluntary no commitment。特别值得注意的是，图里没有 $NC$ 或 $CN$ 区域。

核心 trade-off 是：

**承诺可以缓解消费者等待，但也会改变渠道伙伴的定价机会。制造商需要在“承诺以解决 time inconsistency”和“保持未来批发定价灵活性”之间权衡；零售商则在“承诺以诱导早买”和“避免被制造商未来抽走 margin”之间权衡。**

### Proposition 3：战略消费者对利润的影响是非单调的

Proposition 2 解决了均衡承诺策略。Proposition 3 接着问：当消费者更战略，即 $\rho_c$ 上升时，各方利润如何变化？结论是：

1. 制造商利润随 $\rho_c$ 弱下降。
2. 若 $\rho_c^y(\rho_f)<1$，零售商利润和供应链总利润对 $\rho_c$ 非单调。

> 直觉：消费者更战略通常意味着更愿意等待，这会伤害企业。但在分散式供应链里还有第二个效应：当 $\rho_c$ 处于 induced $NN$ 区间时，制造商为了阻止零售商承诺，会提高 $w_1$，这伤害零售商和供应链。当 $\rho_c$ 继续上升到足够高时，阻止零售商承诺变得太贵，制造商转向 $CC$，不再扭曲 $w_1$。因此零售商和供应链利润可能在某个点“反弹”。

Figure 3 展示了这种非单调。对于较低的企业折扣因子，例如 $\rho_f=0.5$，随着 $\rho_c$ 增加，零售商利润先下降，在 induced $NN$ 区间被压低，然后进入 $CC$ 后上升到一个较高平台。对于较高的 $\rho_f=0.9$，$NN$ 区间更大，利润变化更接近单调下降。

这个结果很反直觉：**更战略的消费者有时反而让零售商和供应链更好，因为他们迫使制造商放弃扭曲性的 deterrence strategy。**

### Proposition 4：承诺能力可能伤害双方

在 centralized benchmark 中，拥有承诺能力总是有利。Proposition 4 改问：在 decentralized supply chain 中，如果制造商和零售商拥有承诺能力，相比完全没有承诺能力，会怎样？

存在阈值 $\rho_c^{nm}(\rho_f)$ 和 $\rho_c^{nr}(\rho_f)$，使得：

1. 制造商在某些中间区间因承诺能力而利润下降，在消费者足够战略且企业足够不耐心时因承诺能力而利润上升。
2. 零售商也有类似结果：承诺能力可能降低其利润，也可能在特定区间提高利润。

> 直觉：承诺能力不是单纯的“多一个选项”。一旦零售商有能力承诺，制造商就必须考虑零售商可能承诺后的后果。为了阻止她承诺，制造商可能提高 $w_1$；或者制造商自己也承诺。这两种做法都可能降低供应链效率。前者导致第一期零售价偏高、销量偏低；后者可能导致第二期销量过低。若没有承诺能力，双方反而不会进入这种战略威胁和反威胁。

Figure 4 将“有承诺能力”和“无承诺能力”的利润曲线放在一起。图的关键信息是：在某些参数下，实线低于虚线，即有承诺能力反而更差。这就是本文最接近 prisoner’s dilemma 的结果。

### Proposition 5：内生承诺不一定优于外生承诺

Proposition 4 比较的是“有无承诺能力”。Proposition 5 比较的是另一个维度：如果企业可以内生选择是否承诺，是否总比外生规定承诺更好？

结论是：

1. 制造商在 endogenous commitment decisions 下弱优于 exogenous commitments。
2. 零售商则不一定。当 $\rho_c^z(\rho_f)<\rho_c<\min\{\rho_c^y(\rho_f),1\}$ 时，零售商在 endogenous setting 下反而低于 exogenous commitments。

> 直觉：制造商拥有先动优势，可以利用 $w_1$ 操纵零售商承诺激励，因此内生选择通常对制造商有利。但零售商可能成为被操纵的一方。特别是在 induced $NN$ 区间，双方最终都不承诺，看似零售商避开了 commitment；但制造商为了让她不承诺，已经把 $w_1$ 提高了，导致零售商利润低于外生承诺情形。

Figure 5 的重点是：内生选择不是自动“更自由、更好”。对制造商而言，自由选择是优势；对零售商而言，可能意味着被上游利用。

### Proposition 6：供应链协调随战略消费者先改善后恶化

前面看的是单个企业利润。Proposition 6 转向 supply chain coordination。作者定义 supply chain profitability index：

$$
\text{Profitability Index}=\frac{\Pi_S^{\text{decentralized}}}{\Pi_I^{\text{centralized}}}.
$$

指数越接近 1，表示分散式供应链越接近集中式最优，协调越好。

Proposition 6 的结论是：

1. 在 exogenous commitments 下，profitability index 不随 $\rho_c$ 或 $\rho_f$ 变化。
2. 在 endogenous commitment decisions 下，随着 $\rho_c$ 上升，profitability index 先上升、后下降、最终在 $CC$ 区间不变。
3. 与 exogenous commitments 相比，endogenous commitments 下的协调可能更好，也可能更差。

> 直觉：外生承诺把动态定价问题锁住了，供应链像面对 nondurable goods 一样，协调损失主要来自 double marginalization，因此折扣因子不影响指数。但在内生承诺下，消费者战略性会改变制造商和零售商的跨期激励。在 voluntary $NN$ 区间，消费者越战略，零售商越有动力降低 $p_1$ 促进早买，制造商也更可能在第二期设置较低 $w_2$，这反而缓解 double marginalization。但进入 induced $NN$ 区间后，制造商提高 $w_1$ 阻止零售商承诺，协调恶化。

Figure 6 非常重要。它显示 endogenous commitment 的协调指数可能高于 exogenous commitment，也可能低于它。对于 $\rho_f=0.9$，endogenous commitment 在广泛区间显著改善协调，最高可达到约 $91.4\%$；而对 $\rho_f=0.5$，它先改善协调，之后在 induced $NN$ 附近快速恶化。

### Corollary 1：即使消费者不战略，内生不承诺也能改善协调

为了区分“消费者战略性”和“制造商—零售商互动”两个机制，作者分析 $\rho_c=0$ 的 myopic consumers。

结论是：当消费者 myopic 时，制造商和零售商都不承诺，而且 endogenous commitment decisions 下的 supply chain profitability index 高于 exogenous commitments。并且有：

$$
p_1^{YEn}<p_1^{YEx},\quad p_2^{YEn}<p_2^{YEx},
$$

$$
q_1^{YEn}>q_1^{YEx},\quad q_2^{YEn}>q_2^{YEx},
$$

$$
w_1^{YEn}>w_1^{YEx},\quad w_2^{YEn}<w_2^{YEx}.
$$

> 直觉：即使消费者完全不等降价，commitment timing 也会改变上下游的战略互动。在外生承诺下，制造商提前设置 $w_2$，可以用较高 $w_2$ 影响零售商第一期定价。在内生不承诺下，制造商第二期才设 $w_2$，此时 $p_1$ 和 $q_1$ 已经实现，无法用 $w_2$ 操纵第一期。零售商也会降低 $p_1$ 来诱导制造商未来设置较低 $w_2$。所以，改善协调的根源不只是消费者战略性，而是 endogenous timing 改变了上下游的战略杠杆。

## Extensions

### Extension 1：允许零售商跨期库存 (Inventory Carryover)

扩展模型允许零售商第一期订购 $Q_1$，销售 $q_1$，将剩余库存

$$
I=Q_1-q_1
$$

带到第二期。零售商持有库存的单位成本为 $h\ge 0$。作者主要分析 $h=0$，因为这是最有利于库存跨期的情形；若 $h$ 很高，则回到 base model。

扩展后的利润为：

$$
\Pi_{M,1}=Q_1w_1,\quad \Pi_{R,1}=q_1p_1-Q_1w_1-h(Q_1-q_1),
$$

$$
\Pi_{M,2}=Q_2w_2,\quad \Pi_{R,2}=q_2p_2-Q_2w_2.
$$

核心发现：

1. 库存跨期不改变均衡承诺结构：仍然只会出现双方都承诺或双方都不承诺。
2. 零售商只在 $NN$ 且企业足够耐心时持有库存，具体大约需要 $\rho_f\gtrsim 0.825$。
3. 库存是 purely strategic inventory，不是运营补货需要。零售商持有库存是为了影响制造商第二期批发价。
4. Base model 关于利润和协调的核心结论仍然稳健。

> 直觉：跨期库存给零售商一个新武器。她可以通过第一期多拿货，减少第二期从制造商采购的依赖，从而压低制造商未来的 $w_2$。但这个武器只有在未来利润足够重要时才值得用，所以需要较高 $\rho_f$。同时，库存会让消费者预期未来供应仍在，可能加剧等待，也会让制造商提高 $w_1$ 来抑制库存，因此对协调的影响不总是正面的。

### Extension 2：价格保护政策 (Price Protection Policies) 作为可信承诺工具

主模型先假设承诺可信。第 8 节讨论现实中怎样让承诺可信。作者重点分析 price protection policies，即如果企业未来降价，就补偿先买者差价。

在 centralized supply chain 中，retail price protection 可以完全消除企业未来降价的激励，因此在所有折扣因子下都能作为 credible commitment device。

在 decentralized supply chain 中，有两类政策：

1. Retail Price Protection (RPP)：零售商承诺 $p_2$，如果第二期零售价低于承诺价，则补偿第一期消费者。
2. Wholesale Price Protection (WPP)：制造商承诺 $w_2$，如果第二期批发价低于承诺价，则补偿零售商。

核心发现：

1. 如果没有 welfare losses，WPP 和 RPP 只在某些折扣因子条件下能保证可信承诺，通常是 $\rho_c$ 较高、$\rho_f$ 较低。
2. 如果存在中等或较高 welfare losses，例如退款处理、行政成本、协调成本，那么 WPP 和 RPP 在所有折扣因子下都能成为 credible commitment devices。
3. 两家企业是否采用 PP policies 的均衡结构与主模型一致：消费者足够战略且企业较不耐心时，双方采用并承诺；消费者不太战略且企业较耐心时，双方不采用。

> 直觉：price protection 把“未来降价”变得昂贵。如果企业未来降价，必须补偿过去的买家或渠道伙伴；补偿成本越高，越能阻止企业事后偏离承诺。因此，现实中的价格保护政策不仅是促销工具，也可以是解决 durable goods time-inconsistency 的承诺装置。

## 比较静态汇总表 (Comparative Statics Summary)

| 参数或制度变化 | 对承诺均衡的影响 | 对企业利润的影响 | 对供应链协调的影响 | 直觉 |
|:---|:---|:---|:---|:---|
| $\rho_c\uparrow$，消费者更战略 | 均衡可能从 voluntary $NN$ 到 induced $NN$，再到 $CC$ | 制造商利润弱下降；零售商与供应链利润可能非单调 | 在 endogenous commitment 下协调先改善后恶化；在 exogenous commitment 下不变 | 战略消费者增加等待压力，但也可能迫使制造商放弃扭曲性的 deterrence strategy。 |
| $\rho_f\uparrow$，企业更耐心 | $NN$ 区域扩大，承诺激励下降 | 企业更重视第二期利润，较不愿意用承诺牺牲未来灵活性 | 高 $\rho_f$ 下 endogenous coordination 往往较好，但具体取决于是否进入 induced $NN$ | 企业越有耐心，越不急于把消费者推到第一期购买，动态定价价值更高。 |
| 第一批发价 $w_1\uparrow$ | 可降低零售商承诺 $p_2$ 的激励 | 制造商可能短期受益；零售商受损；供应链可能受损 | 通常降低协调，特别是在 induced $NN$ | 高 $w_1$ 是制造商阻止零售商承诺的战略工具，但会压缩下游 margin 和销量。 |
| 从无承诺能力到有承诺能力 | 可能引入 induced $NN$ 或 $CC$ | 可能让双方都更差，也可能在消费者非常战略、企业不耐心时让双方更好 | 不一定改善 | 承诺能力改变了对方的威胁点，不是无成本 flexibility。 |
| Endogenous commitment 相比 exogenous commitment | 制造商可选择 $NN$ 或 $CC$，并操纵 $w_1$ | 制造商弱优；零售商可能更差 | 可能更好也可能更差 | 内生选择给上游先动者更多策略空间，未必保护下游。 |
| 允许 inventory carryover | 仍然只有 $NN$ 或 $CC$ | 高 $\rho_f$ 下零售商可能用库存改善自身未来议价 | 影响非单调；多数参数下可能恶化协调 | 库存是战略工具，可压低未来 $w_2$，但也会诱发等待和 $w_1$ 上升。 |
| Welfare loss of PP policies $\uparrow$ | PP 更容易成为可信承诺 | 降价偏离成本上升，使承诺更可信 | 在合适条件下支持 $CC$ | 价格保护让事后降价变贵，从而增强承诺可信度。 |

## 主要结论与管理启示 (Main Results & Managerial Insights)

### 与 benchmark 的对比

| 设定 | 承诺策略 | 承诺能力是否有利 | 战略消费者的影响 | 供应链协调 |
|:---|:---|:---|:---|:---|
| Centralized firm | 总是承诺 $p_2$ | 有利 | 通常伤害企业，需要承诺缓解 | 无上下游协调问题 |
| Decentralized, exogenous commitments | 承诺状态外生给定 | 既有文献发现双方承诺可能伤害企业 | 折扣因子对协调指数不产生影响 | 类似 nondurable goods 的 double marginalization |
| Decentralized, endogenous commitments | 只会是 $NN$ 或 $CC$ | 可能有利，也可能让双方更差 | 对零售商和供应链利润可能非单调 | 可能好于也可能差于 exogenous commitment |
| Decentralized with inventory carryover | 仍然只会是双方同承诺或同不承诺 | 核心结论稳健 | 高 $\rho_f$ 下 strategic inventory 扩大不承诺区域 | 库存既可改善议价，也可能恶化整体协调 |

### 管理建议

1. **不要把 centralized durable goods 的承诺逻辑直接搬到渠道场景。** 直销企业承诺未来价格往往有利，但制造商—零售商结构下，承诺会改变渠道伙伴的行动，结果可能相反。

2. **制造商要评估零售商的承诺激励。** 如果零售商有能力承诺未来零售价，制造商可能会想通过提高 $w_1$ 来阻止她。但这是一种扭曲性策略，可能损害总利润和长期渠道关系。

3. **零售商不要在制造商没有批发价承诺时轻易承诺零售价。** 否则第二期批发价可能被制造商提高，零售商的未来 margin 被抽走。零售商需要配套的 wholesale commitment、长期合同或 price protection。

4. **消费者战略性不是单向坏事。** 对 utilitarian products、B2B 客户等更战略的消费者群体，企业不能只预期利润下降；在某些区间，战略消费者会改变上游的 deterrence incentive，反而改善零售商和供应链表现。

5. **产品定位可以影响 $\rho_c$。** Hedonic products 通常诱发更冲动的购买，$\rho_c$ 较低；utilitarian products 和企业客户更理性，$\rho_c$ 较高。广告、发布节奏、价格透明度和价格历史可见性都会改变消费者等待行为。

6. **Price protection policies 可以是承诺工具，但不是免费工具。** 价格保护能提升承诺可信度，尤其在存在退款处理成本或履约成本时更有效。但这些成本本身也会影响福利，需要与促销和渠道合同一起设计。

7. **战略库存要谨慎使用。** 零售商持有 inventory carryover 可以压低未来 $w_2$，但也可能让消费者更愿意等待，并诱发制造商提高 $w_1$。这不是单纯的 operational buffering，而是会改变渠道博弈的战略动作。

## 与相关文献的对话 (Dialogue with Literature)

### Coase (1972), Stokey (1981), Bulow (1982)：durable goods monopolist 与 time inconsistency

共同关注点是耐用品市场中的动态定价和消费者等待。经典逻辑认为，耐用品垄断者不能承诺未来价格时，会因为未来降价预期而损失利润；承诺未来价格可以缓解这一问题。

本文推进之处在于把问题从 centralized monopolist 移到 decentralized supply chain。结果表明，集中式企业总是承诺的结论不能直接推广。原因不是消费者变了，而是多了制造商—零售商之间的战略互动。

### Desai, Koenigsberg, and Purohit (2004)：strategic decentralization and channel coordination

这类文献关心战略消费者和渠道协调，强调合同或去中心化结构可能缓解 time inconsistency。本文与其共同点是都看到“分散化”不只是效率损失，也可能改变动态定价激励。

区别在于，本文把制造商和零售商对未来价格的 commitment decisions 同时内生化，而不是只分析给定合同或单方承诺。这使得本文能识别 induced noncommitment，即承诺能力存在但不被使用时仍然改变均衡。

### Su and Zhang (2008)：strategic customer behavior, commitment, and supply chain performance

Su and Zhang 强调 commitment 和供应链合同可以帮助应对战略消费者，并可能改善供应链表现。本文继承了战略消费者与供应链绩效之间的联系，但在模型上进一步内生化两期 wholesale and retail prices，也允许零售商第二期订购。

本文的重要区别是：commitment 并非总是改善绩效。若承诺选择由渠道成员内生决定，承诺能力可能引发扭曲性批发价和囚徒困境。

### Kabul and Parlaktürk (2019)：decentralized supply chain 中 commitment 可能有害

这是本文最直接的对话对象。Kabul and Parlaktürk 研究制造商和零售商的 price/quantity commitments，发现承诺可能伤害承诺方和非承诺方。

本文的推进在于：Kabul and Parlaktürk 分析的是 exogenous commitment scenarios，例如 $NC$ 和 $CN$；本文证明当 commitment decisions endogenous 时，$NC$ 和 $CN$ 根本不是 SPNE。真正的均衡只有 $NN$ 和 $CC$，而且 $NN$ 又分 voluntary 和 induced 两种机制。这一区别很关键，因为它改变了对利润和协调的判断。

### Arya and Mittendorf (2006)：channel discord 可能缓解 durable goods 问题

Arya and Mittendorf 表明，渠道不一致有时可以缓解 durable goods 的 time-inconsistency，甚至提高供应链表现。本文与它共享一个思想：double marginalization 和 channel conflict 不一定总是坏事。

本文的新意在于把这种“渠道冲突可能有益”的逻辑放到内生承诺框架中。文章说明，某些 no-commitment equilibrium 之所以能改善协调，不只是因为消费者战略性，而是因为内生 timing 限制了上游操纵下游定价的能力。

## 犀利评论 (Reviewer's Critique)

### 优点

理论贡献清晰：本文把 durable goods commitment 从单企业问题转化为渠道成员之间的 endogenous strategic choice，最核心的新机制 induced noncommitment 很有辨识度。

模型结构简洁但信息量大：两期模型、两个折扣因子、四种承诺状态，足以生成多种反直觉结果，同时保持可解释性。

实践相关性较强：耐用品渠道、价格保护、消费者等待、零售商库存等现象都对应现实场景，管理启示不只是抽象比较静态。

### 模型限制与假设过强之处

1. **两期模型可能过于简化。** 很多耐用品有长期降价路径、产品换代和多轮促销。多期环境下，commitment 的可信性和消费者预期会更复杂。

2. **消费者估值均匀分布带来较强的线性结构。** 主要机制应当稳健，但阈值区域和非单调性是否在更一般需求下保留，需要进一步验证。

3. **渠道结构是单制造商—单零售商。** 现实中常有多零售商竞争、平台渠道、直营与分销并存。竞争可能显著改变零售商承诺激励和制造商 deterrence strategy。

4. **承诺可信性在主模型中被先验假设。** 虽然后续用 price protection 讨论 credibility，但主模型的承诺能力仍像一个可直接使用的技术。现实中承诺往往需要合同、声誉、平台规则或法律执行。

5. **共同企业折扣因子 $\rho_f$ 简化了上下游异质性。** 制造商和零售商的现金流压力、资本成本和库存风险通常不同。异质折扣因子可能会让 $NC$ 或 $CN$ 的 off-equilibrium incentives 更复杂。

6. **Price protection extension 主要依赖数值分析。** 由于非凹利润和非线性约束，作者采用有限案例数值分析。该部分的普遍性不如主模型的解析结果强。

### 未来研究方向

1. **数量承诺与产能承诺。** 本文关注价格承诺，未来可以研究制造商承诺产量、产能或供应上限是否会生成类似 induced noncommitment。

2. **多零售商竞争。** 如果多个零售商销售同一耐用品，某一零售商的 price commitment 会影响其他零售商和制造商的策略，可能出现新的协调或排他效应。

3. **直营与分销并存的 dual channel。** 制造商既通过自营渠道直接卖，又通过零售商卖时，$w_2$ 和 $p_2$ 的承诺会与 channel encroachment 互动。

4. **经验或结构估计。** 可以用电子产品、家电或汽车价格数据估计 $\rho_c$，并检验高战略消费者市场中是否更常出现 price protection 或长期批发合同。

5. **行为消费者与异质等待成本。** 消费者可能存在 loss aversion、limited attention、reference price effects。不同消费者对未来降价的感知不同，可能改变 commitment 的作用。

6. **产品更新换代。** 耐用品常伴随新品推出和旧品折价。未来模型可以把 $p_2$ 的降价与新产品 introduction、trade-in、二手市场放在一起研究。

## 最后复盘：这篇文章到底做了什么

这篇文章的核心不是又一次证明“承诺好”或“承诺坏”，而是说明：在供应链里，承诺是一个 interdependent strategic choice。制造商和零售商的承诺能力会互相改变对方的最佳反应，因此结论不能从 centralized firm 或 exogenous commitment setting 直接外推。

最重要的均衡图景是三段式：低消费者战略性时，双方 voluntary no commitment；中等战略性时，制造商通过提高 $w_1$ 诱导零售商 no commitment；高消费者战略性且企业不耐心时，双方都 commit。围绕这三段式，文章解释了为什么承诺能力会伤害双方、为什么战略消费者可能先改善后破坏供应链协调，以及为什么 price protection 和 strategic inventory 会在现实中成为重要的补充机制。

# Sustainable Sourcing of Agricultural Products: Fixed vs. Flexible Premiums

**笔记日期前缀：2026-06-07**  
**作者**：Vishal Agrawal（Georgetown University, McDonough School of Business）；Can Zhang（Duke University, Fuqua School of Business）  
**年份与期刊**：2026，*Management Science*，Articles in Advance  
**DOI**：10.1287/mnsc.2025.01093  
**文章类型**：理论模型 / Game-theoretic OM model / Sustainable sourcing certification design

## 中文摘要

农业可持续认证通常要求下游企业在市场价格之外，向认证农户支付额外 premium，以改善小农户收入并激励可持续农业实践。实践中有两种 premium 设计：一种是固定 premium，即无论市场价格高低，每单位认证作物的 premium 不变；另一种是灵活 premium，即当市场价格低时提高 premium、市场价格高时降低 premium。直觉上，灵活 premium 似乎更能保护农户，尤其是在市场价格下行时。但本文建立一个包含 NGO 认证方、农户和下游企业的博弈模型后发现，这一直觉并不总是成立：灵活 premium 可能降低农户期望收入；即便提高了农户收入，也可能降低企业的可持续采购量和利润。只有在认证供给相对于需求较充足的情形下，灵活 premium 才可能同时提高农户收入、可持续采购量和企业利润。文章还分析了企业自有 sustainability label，发现企业自标通常更偏好固定 premium；相比 NGO label，企业自标可能提高可持续采购量，但降低农户收入。

## 论文速览表格

| 维度 | 内容 |
|:---|:---|
| 研究问题 | 可持续农业认证应采用固定 premium 还是灵活 premium？灵活 premium 是否真的能保护农户？它如何影响企业可持续采购量与利润？企业自有 label 与 NGO label 的结果有何不同？ |
| 实践背景 | Fairtrade 等认证通常采用固定 premium。例如 Fairtrade cocoa premium 是每吨 240 美元，且在最低价之外支付；Oxfam Fair Trade 等项目开始尝试 flexible premium。 |
| 核心张力 | premium 越高，农户每单位认证作物收入越高，但企业采购认证作物的意愿越低；农户实际收入还取决于能卖出多少作物作为 certified，而不是只取决于单价。 |
| 方法 | 一个三方博弈模型：NGO 先设 premium；农户决定是否认证；产量与市场价格实现后，企业决定认证与非认证产品的采购量和价格。 |
| 关键机制 | 灵活 premium 会在低价状态提高 premium、在高价状态降低 premium。但如果高价状态对应低产量、认证供给紧张，那么降低 premium 不一定提高采购量，只会降低农户单价。 |
| 主要发现 | 灵活 premium 可能降低农户收入；即使提高农户收入，也可能降低可持续采购和企业利润；只有认证供给充足、需求相对有限时，才可能实现 farmer-firm-sustainability 三赢。 |
| 自标结果 | 企业自有 sustainability label 下，固定 premium 对企业利润弱占优；企业自标可能带来更高可持续采购量，但给农户的 premium 和农户收入通常更低。 |
| 管理启示 | 不应把灵活 premium 当作一刀切的农户保护工具；认证方应先判断该作物是否有充足 certified supply，以及需求、产量波动、最低价和认证成本等条件。 |
| 适用场景 | 小农户农业供应链、可持续认证、Fairtrade 类机制、可持续消费者愿付溢价、企业 self-label 与 NGO label 的制度设计。 |

## TL;DR

这篇文章最重要的结论是：**“市场低价时给农户更高 premium”听起来更公平，但不一定真的让农户赚更多钱。**因为企业看到 premium 变高后可能少买认证作物，而农户收入取决于“单价 × 能卖成认证的数量”。

灵活 premium 只有在认证作物供给比较充足、企业需求没有过度紧张时，才可能同时提高农户收入、可持续采购量和企业利润。否则，它可能让供需错配更严重，甚至伤害原本想保护的农户。

## One More Thing

最有意思的洞察是：**保护农户的价格工具，可能因为企业的采购反应而反过来伤害农户。**灵活 premium 的初衷是“市场价格低时多补一点”，但农业市场里低价往往发生在高产量状态，高价往往发生在低产量状态。认证供给紧张时，在高价低产状态降低 premium，并不会让企业买到更多认证作物，因为根本没有足够 certified supply；它只会让农户在已经供给紧张的状态下拿到更低的认证单价。换句话说，本文真正揭示的是：**premium 设计不是单纯的价格公平问题，而是一个被企业采购决策和认证供给约束共同塑造的运营问题。**

## 研究背景与动机 (Motivation)

### 实践痛点

许多农业产品依赖发展中经济体的小农户生产。文章提到，全球大约 70% 的 cocoa beans 由小农户生产，这些农户通常每天生活费低于 2 美元；全球大约 60% 的 coffee beans 来自拉丁美洲，主要也由小农户生产。小农户往往缺乏资本、投入品和机械化能力，生产效率低，在大宗农产品市场中又是 price takers，因此很难获得 living income。

为改善小农户收入并推动可持续农业实践，Fairtrade International、Fair Trade USA、Rainforest Alliance 等 NGO certification programs 要求企业从认证农户采购作物，并在市场价格或最低价之上支付 premium。问题在于，premium 一方面提高农户单位收入，另一方面会增加企业采购认证作物的成本，降低企业可持续采购意愿。因此，premium 设计直接影响认证体系能否同时实现社会目标和市场可持续性。

实践中有两种 premium 形式：

1. **固定 premium (fixed premium)**：每单位认证作物获得固定 premium，与市场价格无关。Fairtrade cocoa 的 fixed premium 是每吨 240 美元，且在市场价或 Fairtrade minimum price 之上支付。
2. **灵活 premium (flexible premium)**：市场价格低时 premium 更高，市场价格高时 premium 更低。该机制受到 farmer advocacy groups 和 industry watchdogs 推动，Oxfam Fair Trade 已在 cocoa 和 rice 项目中实施。

灵活 premium 的直觉吸引力很强：低价时农户更脆弱，因此应获得更高补偿。但本文指出，农户收入不仅取决于 premium，还取决于企业愿意采购多少 certified crops，以及认证供给是否足够。

### 理论缺口

现有 sustainable operations 文献已经研究了 certification、auditing、responsible sourcing、sustainable supplier practices、self-label 等问题，但较少研究认证体系内部的 premium 结构设计，尤其是固定 premium 与灵活 premium 的比较。

本文与三类文献对话：

- **Sustainability certification design**：已有研究关注认证筛选、最低 fair trade 内容比例、eco-label 与 regulation/self-label 的互动，但未系统分析 fixed vs. flexible premium。
- **Sustainable sourcing**：已有研究关注企业采购政策、农户可持续实践、共享价值合同等，但本文把重点放在 NGO premium rule 如何通过企业采购反应影响农户收入。
- **Eco-label economics and strategy**：已有研究关注 label 竞争、消费者感知、credibility 和 welfare；本文补充了农业作物价格波动与认证供给约束下的 operational mechanism。

### 核心贡献

1. **反直觉机制**：灵活 premium 不一定提高农户收入，可能因企业减少可持续采购、认证供给受限而降低农户期望收入。
2. **三维目标统一比较**：文章同时比较 farmer income、sustainable sourcing quantity、firm profit，而不是只看农户收入。
3. **供需条件决定制度优劣**：灵活 premium 适合 certified supply 相对 demand 充足的作物，不适合 certified supply 紧张或需求快速扩张的情形。
4. **解释 self-label 的双刃剑**：企业自标可能提高认证采购量，但 premium 更低、农户收入更差，为要求企业披露并提高 premium 提供理论依据。

## 模型设定与假设 (Model Setup & Assumptions)

### 符号体系：产量、价格与 premium

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $i \in [0,1]$ | 农户索引 | 单位质量农户群体 |
| $Y_i$ | 农户 $i$ 的产量 | $Y_i = Y + \epsilon_i$ |
| $Y$ | 共同产量冲击 | 由天气、气候等共同因素驱动 |
| $\epsilon_i$ | 个体产量噪声 | 均值为 0，与 $Y$ 独立 |
| $y_H = \mu + \sigma$ | 高产量状态 | 总供给高，市场价格低 |
| $y_L = \mu - \sigma$ | 低产量状态 | 总供给低，市场价格高 |
| $\mu$ | 平均产量 | 反映 overall expected yield |
| $\sigma$ | 产量波动 | 越大表示产量不确定性越强 |
| $w_H = a - b y_H$ | 高产量状态市场价 | 因供给高，价格低 |
| $w_L = a - b y_L$ | 低产量状态市场价 | 因供给低，价格高 |
| $m$ | minimum price | 市场价低于 $m$ 时，认证采购按 $m$ 保护农户 |
| $\rho_H$ | 高产量/低价格状态 premium | 灵活 premium 下较高 |
| $\rho_L$ | 低产量/高价格状态 premium | 灵活 premium 下较低 |

premium 的实际支付规则是：企业采购 certified crop 时支付

$$
\max\{m,w_j\} + \rho_j, \quad j \in \{H,L\}.
$$

> 直觉：$\max\{m,w_j\}$ 是市场价格保护或最低价保护，$\rho_j$ 是认证 premium。固定 premium 要求 $\rho_H = \rho_L$；灵活 premium 要求 $\rho_H > \rho_L$，即低价状态给更高 premium。

### 符号体系：消费者需求

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $\theta \sim U[0,1]$ | 消费者对 conventional product 的基础估值 | 消费者异质性 |
| $\gamma$ | sustainable consumers 占比 | 这部分消费者愿意为 certified product 多付钱 |
| $s$ | sustainable product 的额外估值 | sustainable consumers 对认证产品的额外 willingness to pay |
| $p_{c,j}$ | conventional product 价格 | 状态 $j$ 下由企业决定 |
| $p_{s,j}$ | sustainable product 价格 | 状态 $j$ 下由企业决定 |
| $d_{c,j}$ | conventional product 需求 | 由价格和消费者选择决定 |
| $d_{s,j}$ | sustainable product 需求 | 由价格和消费者选择决定 |

sustainable consumers 对 conventional product 的效用为 $\theta - p_{c,j}$，对 sustainable product 的效用为 $\theta + s - p_{s,j}$。conventional consumers 对两类产品没有可持续溢价，只比较 $\theta - p_{c,j}$ 与 $\theta - p_{s,j}$。

> 直觉：$\gamma$ 和 $s$ 分别表示 sustainable demand 的“规模”和“强度”。$\gamma$ 越大，愿意买认证产品的人越多；$s$ 越大，每个 sustainable consumer 愿意多付的溢价越高。

### 符号体系：企业采购与农户认证

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $q_{c,j}$ | conventional product 生产/采购量 | conventional crop supply 假设充足 |
| $q_{s,j}$ | sustainable product 生产/采购量 | 同时也是 certified crop sourcing quantity |
| $\alpha$ | 认证农户比例 | certified supply 为 $\alpha y_j$ |
| $K$ | 最高认证成本 | 农户认证成本均匀分布于 $[0,K]$ |
| $c$ | 单个农户认证成本 | 主模型中用于排序认证决策 |

企业的 sustainable sourcing 受到 certified supply 约束：

$$
q_{s,j} \leq \alpha y_j.
$$

> 直觉：即使市场上有消费者愿意买认证产品，企业也未必能采购足够 certified crops。认证农户少或低产量状态下，$\alpha y_j$ 会成为硬约束。

### 博弈/决策结构

1. **NGO certification program** 先选择 premium rule：固定 premium 或灵活 premium，并设定 $\rho_H, \rho_L$。
2. **农户**观察 premium rule，预期企业未来采购行为，决定是否认证农场。
3. **产量和市场价格实现**：共同产量冲击 $Y$ 取 $y_H$ 或 $y_L$，市场价为 $w_H$ 或 $w_L$。
4. **企业**观察认证农户比例、产量状态和市场价格，决定 $q_{c,j}, q_{s,j}, p_{c,j}, p_{s,j}$。
5. **消费者**观察价格后选择购买 conventional product、sustainable product 或不购买。

**Information Structure**：NGO 和农户在产量实现前决策，知道产量分布和企业反应；企业在产量和市场价格实现后决策；消费者观察产品价格后决策。

### 企业目标函数与约束

在状态 $j \in \{H,L\}$ 下，企业解决：

$$
\max_{q_{c,j}, q_{s,j}, p_{c,j}, p_{s,j}}
\left\{(p_{c,j}-w_j)q_{c,j} + \left(p_{s,j}-\max\{m,w_j\}-\rho_j\right)q_{s,j}\right\}
$$

subject to

$$
d_{c,j}(p_{c,j},p_{s,j}) \leq q_{c,j} \leq d_{c,j}(p_{c,j},p_{s,j}) + d'_{c,j}(p_{c,j},p_{s,j},q_{s,j}),
$$

$$
0 \leq q_{s,j} \leq \min\{d_{s,j}(p_{c,j},p_{s,j}),\alpha y_j\},
$$

$$
p_{c,j},p_{s,j} \geq 0.
$$

> 直觉：第一项 $(p_{c,j}-w_j)q_{c,j}$ 是 conventional product 利润；第二项是 sustainable product 利润，其单位成本不仅包括市场价或最低价，还包括 certification premium。约束的核心是：conventional supply 足够，但 sustainable supply 受 $\alpha y_j$ 限制。若 sustainable product 缺货，部分消费者可能转向 conventional product，因此 conventional demand 包含 rationing 后的替代需求 $d'_{c,j}$。

### 农户认证决策

若比例 $\alpha$ 的农户认证，则状态 $j$ 下 certified supply 为 $\alpha y_j$。企业采购 $q_{s,j}$ 时，每个认证农户能把作物卖成 certified 的概率近似为

$$
\frac{q_{s,j}}{\alpha y_j}.
$$

农户从认证中获得的期望增量收入为

$$
\frac{1}{2}\left((m-w_H)^+ + \rho_H\right)y_H\frac{q_{s,H}}{\alpha y_H}
+
\frac{1}{2}\left((m-w_L)^+ + \rho_L\right)y_L\frac{q_{s,L}}{\alpha y_L}.
$$

认证均衡比例满足

$$
\alpha
=
\min\left\{
\frac{
\frac{1}{2}\left((m-w_H)^+ + \rho_H\right)y_H\frac{q_{s,H}}{\alpha y_H}
+
\frac{1}{2}\left((m-w_L)^+ + \rho_L\right)y_L\frac{q_{s,L}}{\alpha y_L}
}{K},
1
\right\}.
$$

> 直觉：农户是否认证，取决于认证带来的期望增量收入是否覆盖认证成本。重要的是，premium 并不自动落到所有认证农户手中；只有当农户的作物被企业作为 certified crop 采购时，才能获得 premium。

### NGO 目标函数

主模型中，NGO 选择 premium 来最大化农户从认证中获得的总净收入。因为农户卖 conventional crop 的市场收入不受 NGO premium 决策影响，NGO 只需关注 certification incremental income：

$$
\alpha \left[
\frac{1}{2}\left((m-w_H)^+ + \rho_H\right)y_H\frac{q_{s,H}}{\alpha y_H}
+
\frac{1}{2}\left((m-w_L)^+ + \rho_L\right)y_L\frac{q_{s,L}}{\alpha y_L}
\right]
-
\int_0^\alpha Kx\,dx.
$$

> 直觉：括号内是单个认证农户的期望认证收益，乘以 $\alpha$ 得到所有认证农户的总认证收益；积分项是认证农户群体总认证成本。NGO 的目标是让认证体系真正改善农户净收入，而不是简单提高名义 premium。

### 关键假设、合理性与放松方向

| 假设 | 合理性说明 | 若放松可能的影响 |
|:---|:---|:---|
| 共同产量冲击为两点分布 | 便于解析刻画，同时捕捉高产低价、低产高价的核心相关性 | 连续分布下阈值会变复杂；文章在 cocoa 数值校准中用 normal yield 验证主洞察稳健 |
| 企业是 market price taker | cocoa、coffee 等大宗作物价格主要由全球供需决定，单个企业影响有限 | 多企业和内生 market-clearing price 会增强竞争和供给约束，文章 extension 发现结论仍稳健 |
| conventional crop supply 充足 | 非认证市场通常远大于认证市场 | 若 conventional supply 也受限，企业产品组合和消费者替代会更复杂 |
| 农户风险中性 | 便于解析农户认证决策 | 风险厌恶可能使 flexible premium 更不吸引人，因为它可能增加收入方差 |
| 农户认证成本均匀分布 | 用简洁方式表示认证成本异质性 | 其他分布会改变认证比例阈值，但核心供需错配机制仍应存在 |
| 消费者可持续偏好外生 | 聚焦 premium design 与 sourcing mechanism | 若 label credibility、greenwashing 或消费者信任内生，self-label 与 NGO label 的差异会更大 |
| 企业在农户认证后决定采购量 | 符合许多认证实践：农户需提前认证，企业采购可接近交易季节决定 | 若企业先承诺采购量，企业可诱导更多农户认证；文章 extension 显示主结论仍成立 |

## 分析路线图 (Roadmap of Analysis)

1. **先求企业反应**：给定 premium 和认证农户比例，企业如何选择 sustainable sourcing quantity？这是所有后续比较的基础。
2. **比较 fixed vs. flexible premium 对农户收入的影响**：核心问题是灵活 premium 是否真的保护农户。
3. **进一步比较 sustainable sourcing quantity 与 firm profit**：即使农户收入上升，认证体系也可能因企业少买而削弱。
4. **寻找三赢条件**：识别什么情况下 flexible premium 同时提高农户收入、可持续采购和企业利润。
5. **做比较静态**：研究产量波动、可持续消费者规模、minimum price、认证成本等因素如何改变固定/灵活 premium 的相对优劣。
6. **分析 firm self-labeling**：把 premium 决策权从 NGO 转给企业，比较企业自标与 NGO label 的社会和运营结果。
7. **数值校准与 extensions**：用 cocoa 数据检验现实相关性，并在异质产量、风险厌恶、数量承诺、多企业等设定下验证稳健性。

## 核心分析与求解 (Analysis & Solution)

### Lemma 1：企业的 sustainable sourcing quantity

给定 premium $\rho_j$ 和认证比例 $\alpha$，企业在状态 $j \in \{H,L\}$ 下的最优 sustainable sourcing quantity 为

$$
q_{s,j}
=
\min\left\{
\frac{1}{2}\gamma\left(1+s-\max\{m,w_j\}-\rho_j\right),
\alpha y_j
\right\}.
$$

> **机制直觉**：右侧第一项是企业在没有供给约束时愿意采购的 sustainable crop 数量，随 sustainable consumer segment $\gamma$ 和可持续愿付溢价 $s$ 上升而上升，随 market/minimum price 和 premium 上升而下降。第二项 $\alpha y_j$ 是 certified supply 上限。这个 lemma 是全文的关键，因为它把 premium 的双重作用写清楚了：premium 提高农户单位收入，但同时压低企业采购需求。

**关键 trade-off：**

**更高 premium = 更高单位农户收入，但也 = 更低企业认证采购需求。农户总收入取决于二者乘积，并受 certified supply 约束影响。**

### Proposition 1：灵活 premium 对农户收入的影响

在 Lemma 1 说明企业会随 premium 调整采购量后，下一步就是问：灵活 premium 是否提高农户期望收入？

结论分两种情况：

1. 如果 minimum price 较低或不存在，即 $m \leq w_H$，则 flexible premium 相比 fixed premium 能提高农户期望收入，当且仅当平均产量足够高：

$$
\mu > \bar{\mu}_1(\cdot).
$$

2. 如果 minimum price 较高，即 $m > w_H$，则 flexible premium 要提高农户期望收入，不仅需要平均产量足够高，还需要认证成本足够低：

$$
\mu > \bar{\mu}_1(\cdot),
\quad
K < \bar{K}_1(\cdot),
$$

且 $\bar{K}_1(\cdot)$ 随 $m$ 上升而下降。

> **机制直觉**：高平均产量意味着 certified supply 更充足。此时，低价状态通常是高产状态，企业有较大采购空间，提高 $\rho_H$ 可以增加农户单位收入；高价状态通常是低产状态，降低 $\rho_L$ 可以刺激企业采购更多 certified crops。因此 flexible premium 可以改善农户收入。相反，当平均产量低或认证供给紧张时，低产高价状态下 certified supply 已经是瓶颈，降低 $\rho_L$ 并不能让企业买更多，只会降低农户拿到的单价，从而伤害农户。

这个命题推翻了“低价多补贴一定保护农户”的直觉。premium 不是 transfer-only 工具，它会改变企业采购量。

### Proposition 2：即便农户收入提高，sustainable sourcing 也可能下降

Proposition 1 只看农户收入；接下来文章考察认证体系的另一个目标：企业到底采购了多少 sustainable crops。

若 flexible premium 已经能提高农户期望收入，则它会降低期望 sustainable sourcing quantity，当且仅当消费者对 sustainable product 的额外愿付溢价足够高：

$$
 s > \bar{s}_1(\cdot).
$$

> **机制直觉**：当 $s$ 高时，企业面对强劲的 sustainable demand，certified supply 更容易成为瓶颈。NGO 若要继续提高农户收入，往往需要把 premium 维持在较高水平，尤其是在低价高产状态提高 $\rho_H$。较高的平均 premium 会压低企业的采购激励。因此，flexible premium 可能通过提高农户单位收入来提高农户总收入，但代价是企业买的 certified crops 变少。

这里的关键不是“消费者越愿意为可持续付钱越好”。高 $s$ 会提高认证产品需求，但如果 certified supply 跟不上，反而会使 premium 设计更难。

### Corollary 1：sustainable sourcing 下降时，企业利润也下降

在 Proposition 2 的基础上，文章进一步说明：若 flexible premium 降低期望 sustainable sourcing quantity，则它也会降低企业期望利润。

> **机制直觉**：企业销售 sustainable product 可以从 sustainable consumers 的额外愿付溢价中获利。如果 flexible premium 让企业少采购 certified crops，企业可销售的 sustainable products 减少，利润自然下降。换言之，农户收入提升若是靠更高 premium 而不是靠更大交易量实现，可能会伤害企业参与认证的激励。

这个 corollary 解释了为什么 flexible premium 在实践中即便有公平叙事，也可能遇到企业阻力。

### Proposition 3：三赢结果的条件

前面两个结果说明 flexible premium 有可能提高农户收入，也有可能降低采购量和企业利润。接下来文章寻找什么情况下 flexible premium 能实现三赢。

flexible premium 能同时提高期望农户收入、期望 sustainable sourcing quantity 和期望企业利润，当以下条件同时成立：

$$
\mu > \bar{\mu}_1(\cdot),
\quad
K < \bar{K}_1(\cdot),
\quad
s < \bar{s}_2(\cdot).
$$

即：平均产量高、认证成本低、消费者 sustainable willingness to pay 不太高。

> **机制直觉**：高 $\mu$ 和低 $K$ 让 certified supply 充足；低 $s$ 表示 sustainable demand 不至于过热，供给约束不紧。此时 NGO 可以在低价状态提高 $\rho_H$ 来保护农户，同时在高价状态降低 $\rho_L$ 来刺激采购，而且 lowering $\rho_L$ 的数量效应足够强，使期望 premium 下降、企业采购增加、利润也增加。三赢并不是因为 flexible premium 天然更公平，而是因为供需条件让“价格保护”和“数量激励”可以兼容。

**一句话概括三赢条件：**

**flexible premium 适合 certified supply 充足而 demand 没有过度紧张的作物。**

### Proposition 4：产量波动 $\sigma$ 的影响

在知道三赢条件后，文章进一步问：气候变化导致产量波动增大时，是否更应采用 flexible premium？直觉上似乎是，因为价格更不稳定，低价保护更重要。

文章发现，当产量波动 $\sigma$ 已经较高时，继续提高 $\sigma$ 会使 flexible premium 更不吸引人：

- $\bar{\mu}_1(\cdot)$ 上升；
- $\bar{K}_1(\cdot)$ 下降；
- $\bar{s}_1(\cdot)$ 和 $\bar{s}_2(\cdot)$ 下降。

> **机制直觉**：更高的 $\sigma$ 意味着低产状态更低，certified supply 在低产高价状态更紧张。flexible premium 在这种状态下降低 $\rho_L$，本意是刺激企业采购，但如果供给已经严重不足，企业无法买更多，农户只会拿到更低单价。因此，在高产量波动环境中，flexible premium 更容易放大供需错配。

这给 climate change 背景下的认证设计一个提醒：气候波动越大，不一定越应该用 flexible premium；相反，有时应回到 fixed premium。

### Proposition 5：sustainable consumer segment $\gamma$ 的影响

文章接着考察可持续消费者规模扩大时的影响。

随着 $\gamma$ 增大：

- $\bar{\mu}_1(\cdot)$ 上升；
- $\bar{K}_1(\cdot)$ 下降；
- $\bar{s}_1(\cdot)$ 和 $\bar{s}_2(\cdot)$ 下降。

这意味着 flexible premium 的适用区域缩小。

> **机制直觉**：$\gamma$ 越大，企业面对的 sustainable product demand 越大，certified supply 更容易成为瓶颈。供给越紧，flexible premium 越可能出现“降 premium 也买不到更多，升 premium 却抑制采购”的问题。因此，可持续消费群体扩大并不自动支持 flexible premium，反而可能让 fixed premium 更稳妥。

### Proposition 6：企业 self-labeling 下，固定 premium 对企业利润弱占优

前面讨论的是 NGO 设定 premium。接下来文章把决策权交给企业：如果企业创建自己的 sustainability label，它会选择 fixed premium 还是 flexible premium？

结论是：在 self-labeling 下，固定 premium 带来的期望企业利润至少不低于 flexible premium。

> **机制直觉**：企业关心自身利润，而 flexible premium 需要在低价状态提高 $\rho_H$。低价状态往往是高产状态，企业本可采购和销售较多 sustainable products；提高 premium 会显著压缩这部分利润。虽然 flexible premium 在高价状态降低 $\rho_L$ 可能有利于企业，但高价状态通常利润本来较低，且低产状态下 certified supply 更容易约束采购，因此降低 premium 带来的好处有限，无法抵消低价状态的利润损失。

这个结果解释了为什么企业自有 sustainability programs 未必会主动采用对农户更“保险”的 flexible premium。

### Proposition 7：self-labeling 可能提高 sustainable sourcing，但降低农户收入

最后，文章比较 NGO label 与 firm self-label。假设消费者对 self-label 的额外估值 $s'$ 不高于对 NGO label 的估值 $s$，且 $s'$ 不太低。文章发现，当平均产量足够高时，self-labeling 可以带来比 NGO labeling 更高的期望 sustainable sourcing quantity：

$$
\mu > \bar{\mu}_2(\cdot),
\quad
\bar{\mu}_2(\cdot) \geq \bar{\mu}_1(\cdot).
$$

> **机制直觉**：NGO 以农户收入为目标，可能设定较高 premium，吸引更多农户认证，但同时压低企业采购意愿。企业 self-labeling 则会选择较低 premium，虽然认证农户可能获得较低单位补偿，但企业更愿意采购 certified crops。因此，在 certified supply 足够的情况下，self-labeling 可能让可持续采购量更高；但它不是农户友好的制度，因为农户拿到的 premium 和总收入可能更低。

这个命题把 self-label 的双刃剑讲清楚了：**它可能扩大“绿色采购量”，但把价值分配从农户转向企业。**

## 比较静态汇总表 (Comparative Statics Summary)

| 参数变化 | 对 flexible premium 吸引力的影响 | 对 farmer income / sourcing / profit 的典型影响 | 直觉 |
|:---|:---|:---|:---|
| $\mu \uparrow$ | 上升 | 更可能提高农户收入，也更可能实现三赢 | 平均产量高，certified supply 充足，降 premium 能刺激数量，升 premium 不易造成供给瓶颈 |
| $K \downarrow$ | 上升 | 更多农户愿意认证，三赢区域扩大 | 认证成本低使 certified supply 增加，缓解供给约束 |
| $m \uparrow$ | 下降 | flexible premium 更不必要，需更低 $K$ 才能优于 fixed | minimum price 已经在低价状态保护农户，削弱 flexible premium 的边际价值 |
| $s \uparrow$ | 对农户收入可能有利，但更可能降低采购量和企业利润 | 当 $s > \bar{s}_1$，flexible premium 会降低 sustainable sourcing；当 $s$ 高于三赢阈值，三赢消失 | 高愿付溢价提高认证需求，使供给约束更紧，也使 NGO 更可能依赖高 premium 提高农户收入 |
| $\gamma \uparrow$ | 下降 | flexible premium 三赢区域缩小 | sustainable consumers 更多，认证需求扩大，certified supply 更容易成为瓶颈 |
| $\sigma \uparrow$ 且已较高 | 下降 | fixed premium 更可能占优 | 低产状态更极端，flexible premium 在高价低产状态降 premium 却无法增加采购，只会降低农户单价 |
| yield heterogeneity $\uparrow$ | 上升 | flexible premium 更容易有效 | 高产农户更愿意认证，认证群体平均产量提高，缓解 certified supply 约束 |
| certification 提高产量 | 上升 | flexible premium 更有利 | 认证本身增加 supply，降低供给瓶颈 |
| certification 降低产量 | 下降 | flexible premium 更难奏效 | sustainable practices 若减少产量，会加剧 certified supply 约束 |
| farmer risk aversion $\lambda \uparrow$ | 可能下降 | flexible premium 可能降低农户效用 | flexible premium 可能增加“认证但卖不成 certified”的收入风险 |
| NGO 更重视 sourcing/revenue | fixed premium 区域扩大 | premium 降低、采购增加，但 flexible premium 吸引力下降 | 为提高采购量或 fee revenue，NGO 会压低 premium，需求增加后供给约束更紧 |
| firm competition $n \uparrow$ | 下降 | 总 sustainable sourcing 上升，但 flexible premium 更不吸引 | 多企业竞争推高总认证需求，导致 certified supply 更紧 |

## 数值校准：cocoa 案例

文章用 cocoa 数据做数值校准，并放松主模型的两点产量分布，使用更现实的 normal yield distribution 和农户 yield heterogeneity。关键校准值包括：

| 参数 | 校准值 | 解释 |
|:---|:---|:---|
| $\mu$ | 0.41 tonne/hectare | global average cocoa yield |
| $\sigma$ | 0.03 tonne/hectare | common yield component 的标准差 |
| $\beta_i$ 标准差 | 0.10 tonne/hectare | 跨主要 cocoa 生产国的 yield heterogeneity |
| 市场价函数 | $w = 0.47 - 0.60Y$ | 由 aggregate supply 与 inflation-adjusted market price 线性回归估计并归一化 |
| 额外生产成本 | $c = 0.53$ | cocoa 转化为 chocolate 等产品的成本 |
| minimum price | $m = 0.19$ | 基于 Fairtrade minimum price 归一化 |
| 认证成本上界 | $K = 0.14$ | 基于 Fairtrade cocoa certification costs 估计 |
| sustainable consumer segment | $\gamma = 0.33$ | 约三分之一消费者愿为可持续产品付溢价 |
| flexible premium 判定 | 当 $w \leq E[w] = 0.22$ 时 premium 更高 | 低价状态触发较高 premium |

### Figure 3 的含义

在 cocoa 校准中，flexible premium 在较广区域内提高农户收入；当 $s$ 较低时，还能同时提高 sustainable sourcing quantity 和 firm profit，形成三赢。以校准值 $\mu=0.41$ 看，cocoa 位于 flexible premium 至少能提高农户收入的区域；当消费者 sustainable WTP 不太高时，甚至位于三赢区域。

**实践含义**：虽然 Fairtrade 等主要认证项目对 cocoa 采用 fixed premium，但 cocoa 可能是一个值得考虑 flexible premium 的作物，因为 cocoa 的 certified supply 相对可能较充足。文章提到，一个现实原因是 cocoa 生产集中在少数 West African countries，农户常通过 cooperatives 组织起来，认证更容易、更低成本；实践中也常有 certified cocoa 无法全部作为 certified 出售的现象。

### Figure 4 的含义

在 NGO labeling 与 self-labeling 比较中，校准结果显示，当 $\mu=0.41$ 时，self-labeling 可带来更高 expected sustainable sourcing quantity。然而，这并不意味着农户更好。文章报告，在所测试的 $\mu$ 和 $s$ 组合平均来看，self-labeling 相比 NGO labeling 带来约 20% 更高的 expected sustainable sourcing quantity，但 certified farmer 获得的 expected premium 低 30% 以上。

**实践含义**：企业自标可以扩大可持续采购量，但可能牺牲农户收入。这为 farmer advocacy groups 要求企业披露并提高 self-label premium 提供了理论依据。

## Extensions

### 1. NGO 目标函数更一般

主模型假设 NGO 最大化农户净收入。Extension 考虑两类替代目标：一是最大化农户收入、sustainable sourcing quantity 和 NGO revenue 的加权和；二是最大化农户收入但满足 NGO revenue requirement。

核心发现：当 NGO 更重视 sustainable sourcing 或 certification fee revenue，或者面临更高 revenue requirement 时，fixed premium 更可能被偏好。

> 直觉：为了提高采购量或 fee revenue，NGO 会倾向于降低 premium 来刺激企业采购。采购需求上升会使 certified supply 约束更紧，从而降低 flexible premium 的适用性。

### 2. 农户产量异质性

文章放松主模型中农户 expected yield 相同的假设，引入 $Y_i = Y + \beta_i + \epsilon_i$，其中 $\beta_i$ 表示地理位置、土壤质量、投入可得性等造成的 yield heterogeneity。

核心发现：主结论稳健。更有意思的是，产量异质性越强，flexible premium 可能越有吸引力。

> 直觉：在相同认证成本下，高产农户从认证中获益更大，因此更愿意认证。这种 self-selection 提高了 certified farmer pool 的平均产量，缓解 certified supply 约束。

文章还考虑 multiplicative yield heterogeneity，以及认证可能提高或降低产量的情形。若认证提高产量，flexible premium 更有吸引力；若认证降低产量，flexible premium 更不吸引。

### 3. 风险厌恶农户

文章用 mean-variance utility 表示农户风险厌恶：

$$
E[\pi(c)] - \lambda Var[\pi(c)].
$$

核心发现：主结论稳健；但农户风险厌恶并不一定增强 flexible premium 的吸引力，反而可能削弱它。

> 直觉：flexible premium 可能增加收入波动。例如在高产低价状态，premium 较高但 certified supply 充足，企业未必采购所有 certified crops，农户“认证了却卖不成 certified”的概率上升，从而增加收入方差。

### 4. 企业先承诺采购量

主模型中农户先决定认证，企业后决定采购。Extension 让企业在农户认证前承诺不同市场价格下的采购量。

核心发现：主结论仍成立。供给充足时，企业没有必要承诺更高数量诱导认证；供给紧张时，企业可能通过承诺诱导更多农户认证，但通常不会完全消除所有状态下的供给约束，因为那会在高产状态造成过剩 certified supply。

### 5. 多企业与内生 market-clearing price

文章进一步考虑多个企业进行数量竞争，并让非认证作物市场价格由 market clearing 内生决定。

核心发现：主洞察稳健。企业数量越多，总 sustainable sourcing demand 越高，certified supply 约束越紧，flexible premium 越不吸引。

## 主要结论与管理启示 (Main Results & Managerial Insights)

### 与简单 benchmark 的对比

| 简单直觉 / Benchmark | 本文揭示的机制 |
|:---|:---|
| 市场价格低时农户更脆弱，因此 flexible premium 一定更好 | 不一定。低价状态常伴随高产，企业采购量会受 premium 影响；高价低产状态供给受限时，降低 premium 不增加采购，只降低农户收入 |
| 提高 premium 总能提高农户收入 | 不一定。premium 提高会降低企业采购 certified crops 的意愿，农户可能只能把更多作物卖到 conventional market |
| sustainable consumers 越多，认证体系越容易成功 | 不一定。需求扩张若超过 certified supply，会使供给约束更紧，让 flexible premium 更难奏效 |
| 气候波动越大，越需要 flexible premium | 不一定。高产量波动会使低产状态 certified supply 更紧，flexible premium 可能放大供需错配 |
| 企业 self-label 会削弱认证可信度，因此采购量一定更低 | 不一定。企业自标因 premium 更低，可能采购更多 certified crops；但农户收入更低 |

### 管理建议

1. **先诊断 certified supply 是否充足，再选择 premium 形式。**
   若某作物认证农户多、认证成本低、平均产量高，且经常出现 certified crops 无法全部卖成 certified 的情况，flexible premium 更值得考虑。

2. **不要把 flexible premium 当成 universal farmer-protection tool。**
   对于 low expected yield、高认证成本、high yield variability 或 certified supply shortage 的作物，fixed premium 可能更稳妥。

3. **minimum price 与 premium 要联合看。**
   如果 minimum price 已经较高，低价保护功能已有一部分由 $m$ 承担，flexible premium 的边际价值下降。

4. **当 sustainable demand 快速增长时，要优先扩充 certified supply。**
   只提高 demand-side marketing 或 label awareness 不够；若 $\gamma$ 和 $s$ 上升但 certified supply 没跟上，flexible premium 的效果可能变差。

5. **对 self-label 应要求 premium transparency。**
   企业自标可能提高 sustainable sourcing quantity，但可能以较低 premium 和较低农户收入为代价。政策制定者和 NGO 可要求企业披露 premium、采购量和农户收入指标。

6. **不同作物应采用差异化 premium design。**
   cocoa 这类 certified supply 可能相对充足的作物，可以考虑 flexible premium；orange juice 等存在 certified supply shortage 的作物，则应谨慎。

## 与相关文献的对话 (Dialogue with Literature)

### Lim, Mak and Park (2019), *Production and Operations Management*

Lim et al. 研究 fair trade certification 中 premium level 与 minimum fair trade content requirement 的联合设计，关注 mainstreaming 与 fairness。本文与其共同关注 fair trade 机制如何通过运营设计影响公平结果，但本文推进之处在于：它不是问 premium 高低或 fair trade 成分比例，而是问 premium 是否应随市场价格状态变化。这个差异重要，因为农业作物价格与产量冲击高度相关，premium 的状态依赖性会改变企业采购反应和 certified supply 约束。

### Agrawal and Lee (2019), *Production and Operations Management*

Agrawal and Lee 研究企业 sustainable sourcing policy 如何影响 supplier sustainable practices 和 sustainable supply availability。本文同样关注 sourcing policy 与上游可持续供给之间的互动，但把决策主体换成 NGO certifier，并把制度工具聚焦在 premium rule 上。本文的贡献在于揭示：即使 NGO 的目标是保护农户，若忽略企业 sourcing response，也可能设计出降低农户收入的 premium 结构。

### Murali, Lim and Petruzzi (2019), *Manufacturing & Service Operations Management*

Murali et al. 分析 ecolabels、environmental regulation 与 green product development 的关系，并讨论 external certification 和 self-label 的互动。本文与其在 self-label 主题上形成直接对话，但进一步引入农业小农户、premium transfer 和 certified crop supply constraint。区别很关键：self-label 不只是消费者信任或 green product positioning 问题，也会改变价值链上 premium 如何在企业与农户之间分配。

### de Zegher, Iancu and Lee (2019), *Manufacturing & Service Operations Management*

de Zegher et al. 研究 sourcing channels 与 contracts 如何促进 shared value，关注企业和农户之间的合同安排。本文同样讨论农业供应链中的 shared value，但研究对象是 third-party certification premium design。它说明，即便没有复杂合同，仅仅改变 premium 的状态依赖性，也会通过企业采购量和农户认证决策影响 shared value 是否成立。

## 犀利评论 (Reviewer's Critique)

### 优点

本文最强的贡献是把一个看似简单的公平问题转化为清晰的运营机制问题：premium 不只是给农户的转移支付，而是会改变企业采购量和认证供给均衡。这个机制足够反直觉，也足够贴近 Fairtrade、Oxfam Fair Trade、企业 self-label 等现实争论。

模型结构简洁但抓住了农业供应链的关键相关性：高产量对应低价格，低产量对应高价格；认证作物供给有限；企业根据 premium 调整采购。Proposition 1 到 Proposition 3 的逻辑递进清楚，从“灵活 premium 是否利农”推进到“三赢何时存在”。

### 模型限制 / 假设过强

1. **主模型中的两点产量分布较 stylized。**虽然文章用 continuous distribution 做了数值检验，但解析结论的阈值结构依赖高/低两个状态。现实中产量和价格的联合分布可能更厚尾、更区域化，极端气候冲击也可能改变机制强度。

2. **消费者对 certification 的信任被外生化。**特别是在 self-labeling 中，消费者是否相信企业自标、是否担心 greenwashing，会直接影响 $s'$。如果 credibility 内生，企业可能需要在 monitoring 或 transparency 上投资，self-label 的结论会更复杂。

3. **农户认证是 all-or-nothing。**现实中农户可能只认证部分地块，或在 certified 与 uncertified 生产之间重新配置投入。这会影响认证可信度、产量和供给。

4. **质量差异没有进入模型。**农作物市场价格常常与质量等级相关，premium rule 可能影响农户质量选择。如果 certified crops 与 conventional crops 在质量上系统不同，企业采购和定价决策会改变。

5. **模型是静态的。**certification adoption、soil conservation、farmer investment 和 firm-NGO relationship 都有明显动态性。当前模型无法解释 premium design 对长期产能、农户退出、气候适应投资的影响。

### 未来研究方向

1. **动态 certification investment model。**研究 fixed/flexible premium 如何影响农户多年期认证、投入、产量提升和退出决策，尤其是 climate change 下的长期适应。

2. **多作物、多区域 empirical calibration。**用 cocoa、coffee、banana、orange juice 等作物的认证供给、销售比例、价格和 premium 数据估计阈值，形成可用于认证方决策的 crop-level premium design map。

3. **endogenous credibility and monitoring。**把 NGO label 与 self-label 的 credibility、audit intensity、greenwashing risk 内生化，研究 premium 与 monitoring 的联合设计。

4. **contracts plus certification。**将 premium rule 与 advance purchase commitment、minimum quantity guarantee、revenue-sharing 或 long-term sourcing contracts 结合，研究能否在 supply-constrained crops 中恢复 flexible premium 的价值。

5. **welfare analysis。**本文主要看 farmer income、sourcing quantity 和 firm profit；未来可加入 consumer surplus、environmental externality、NGO operating cost 和 distributional welfare，评价不同 premium 制度的社会福利。

## 最后一页总结

这篇文章回答的是一个非常具体但重要的问题：**可持续认证给农户的 premium 应该固定，还是随市场价格变化？**

它的核心答案是：不能只看价格保护，还要看企业采购反应和 certified supply 约束。灵活 premium 在低价时提高补偿，听起来公平，但如果它导致企业少买 certified crops，或者在供给紧张状态下降低 premium 却无法增加交易量，农户反而可能受损。

因此，fixed vs. flexible premium 的选择应取决于作物层面的运营条件：平均产量、产量波动、认证成本、minimum price、可持续消费者需求和 certified supply 是否充足。本文最重要的管理启示是：**灵活 premium 不是公平性的万能药，而是一种需要 supply-demand diagnosis 的运营设计工具。**

# Navigating Traceability: How Pricing and Responsibility Sharing Impact Quality and Welfare

作者：Lijian Lu（School of Business and Management, The Hong Kong University of Science and Technology）、Ruxian Wang（Carey Business School, Johns Hopkins University）、Xinyi Zhou（School of Business and Management, The Hong Kong University of Science and Technology）

期刊与年份：Production and Operations Management，2026

DOI：10.1177/10591478261443754

中文摘要：

随着消费者对产品来源透明度与责任追究的需求上升，供应链越来越多地采用 traceability-enabled technologies，例如 blockchain、RFID、条码、批次追踪或其他可识别问题产品来源的技术。本文研究 traceability 对产品质量和供应链福利的影响，重点关注两个制度变量：谁有 pricing power，以及质量失败的 penalty responsibility 如何在买方和多个供应商之间分担。作者构建一个多供应商竞争的 game-theoretic model，发现 traceability 是一把双刃剑：它不一定提升质量，也不一定让所有成员受益。其效果取决于买方或供应商是否掌握批发定价权，以及质量失败责任是外生给定还是由买方内生选择。在 buyer pricing 下，当质量提升成本较低时，traceability 更可能提高质量并使买方受益；当质量提升成本较高时，它反而更可能使供应商受益。在 supplier pricing 下，若责任外生，traceability 总是使供应商受益，并通常提高质量，但买方只有在质量提升足够经济时才受益；若责任内生，买方可通过责任分配抽取供应商利润，traceability 会改善买方福利，但质量效果可能反而下降。本文的核心贡献是说明：可追溯性技术本身不是质量改进的充分条件，必须和 pricing authority 与 responsibility-sharing mechanism 一起设计。

## 论文速览表格

| 维度 | 内容 |
|:---|:---|
| 研究问题 | 当供应链采用 traceability 后，能否提高产品质量？能否提高买方、供应商和整个供应链的福利？这些效果如何受到 wholesale pricing power 和 penalty responsibility sharing 的影响？ |
| 基本场景 | 一个 downstream buyer 从 $n \ge 2$ 个 competing suppliers 采购同质产品。供应商选择质量 $q_i$，质量越高越能获得更大市场份额，但也有更高生产成本。产品失败会产生 penalty cost $b$。 |
| 方法 | 多人 Stackelberg game。买方先决定是否采用 traceability 以及责任分配机制；之后批发价由买方或供应商决定；最后供应商选择质量并竞争市场份额。 |
| 需求/份额机制 | 使用 attraction model / MNL-style allocation：供应商市场份额随自身质量上升而上升，随自身批发价上升而下降。 |
| Traceability 的操作含义 | 有 traceability 时，买方可以识别问题产品来自哪个供应商，故可使用 Target Sharing Rule (TSR)：谁的产品坏了谁承担相应供应商责任。无 traceability 时，买方无法识别来源，使用 Equal Sharing Rule (ESR)：供应商均摊总缺陷责任。 |
| 核心机制 | 质量提升的边际激励可分解为 Profit-Margin Effect (PME)、Market-Share Effect (MSE)、Externality Effect (EE)。Traceability 强化 PME，但削弱 MSE，并消除/削弱 EE，因此质量效果不必然为正。 |
| 主要发现 | Traceability 不是总能提高质量，也不是总能让 buyer 和 suppliers 同时受益。其效果取决于质量提升成本 $\kappa$、罚损成本 $b$、买方责任比例 $\alpha$、市场份额对质量的敏感度、供应商数量以及谁设定批发价。 |
| 适用场景 | 食品、药品、汽车召回、半导体退货、矿产来源认证、海鲜供应链、平台经济或 resale markets 等存在质量失败、责任追溯和多供应商竞争的供应链。 |
| 管理含义 | 企业不能简单地把 blockchain/traceability 当成质量保证工具；应同步设计价格权力、责任分担和供应商激励，否则 traceability 可能提高问责精度，却降低实际质量。 |

## TL;DR

这篇文章的核心发现很直接：traceability 并不自动带来更高质量。它让责任归属更精确，但也会改变供应商改善质量的激励；在某些定价权和责任分担安排下，供应商反而可能降低质量。

最重要的管理含义是：企业上 traceability 系统之前，不能只问“能不能追溯”，还要问“谁定价、谁负责、质量提升成本高不高”。同样一套追溯技术，在不同 pricing 和 responsibility-sharing 结构下，可能是质量改进工具，也可能只是重新分配成本和利润的工具。

## One More Thing

本文最值得分享的洞察是：**“看得更清楚”不等于“做得更好”。** 直觉上，有 traceability 后，坏产品能被精确追责，供应商应该更努力提高质量。但本文指出，无 traceability 时，供应商均摊总缺陷责任；一个供应商提高自身质量，不仅能减少自己的缺陷，还能通过扩大市场份额、挤出低质量竞争者来降低整个供应商群体的缺陷罚损。这种“群体责任”下的外部性，有时反而会给供应商更强的质量竞争激励。Traceability 把责任切得很准，却也切断了这种外部性。于是，在质量提升成本高、市场份额对质量很敏感或 pricing power 配置不当时，traceability 可能精确地追责，却低效地激励。

## 研究背景与动机 (Motivation)

### 实践痛点

供应链中的 traceability 已经成为很多行业的现实要求。文章开篇提到，消费者越来越关心透明度、质量和来源责任；2018 年 Pistoia Alliance 的调查显示，制药和生命科学领域有 60% 的专业人士正在探索 blockchain traceability。零售商和平台，例如 Taobao、JD.com、Gome、Walmart，也在测试或采用区块链追踪应用。

但 traceability 的真正难点不只是技术，而是责任和激励。产品出了问题之后，买方、供应商、平台、零售商之间如何分摊退货、维修、召回、消费者赔偿和商誉损失？如果可追溯系统能精确找到责任供应商，是否一定应该让该供应商承担全部责任？如果无法追溯，供应商是否应该均摊责任？这些制度安排会反过来影响供应商愿不愿意提高质量。

论文给出的实践例子包括：

1. 汽车行业中，warranty/recall costs 往往由 OEM 和供应商按固定比例分摊。
2. Costco 的供应商条款要求供应商承担与召回相关的成本。
3. Cardinal Health 的药品分销协议将 lot-level barcode traceability 和召回责任绑定。
4. Walmart 在 2018 年 romaine lettuce E. coli 事件后要求 leafy green suppliers 使用 IBM Food Trust blockchain。
5. 高价值海鲜和金枪鱼供应链中，供应商或供应商联盟可能具有更强 pricing power，并主动推动 traceability。

这些案例说明，traceability 的经济效果不是单纯的技术问题，而是 contract design、pricing authority 和 accountability allocation 的联合问题。

### 理论缺口

既有 supply chain transparency/blockchain 文献通常强调 traceability 带来的信息透明、召回成本节约、消费者信任或融资效率改善。但本文认为，已有研究相对少地同时处理以下几个因素：

1. 多个供应商之间的 endogenous market share competition。供应商质量越高，会获得更大需求份额，因此质量选择本身具有竞争效应。
2. Penalty responsibility 的纵向分配。质量失败责任不仅在供应商之间横向分摊，还在 buyer 和 suppliers 之间纵向分摊。
3. Pricing authority 的差异。批发价可能由买方制定，也可能由供应商制定；这会显著改变 traceability 的福利归属。
4. Traceability 与 no traceability 下的责任机制差异。可追溯时可以精准追责，不可追溯时只能群体分担或近似分摊。

与 Dong et al. (2023a) 和 Cui et al. (2023) 相比，本文更强调质量竞争、市场份额内生分配、责任纵向分配和定价权共同作用下的 traceability 效果。

### 核心贡献

1. 提出一个同时包含多供应商质量竞争、pricing authority、responsibility sharing 和 traceability adoption 的统一模型。
2. 发现 traceability 的质量效果不是单调正向：它可以提高质量，也可以降低质量。
3. 将供应商质量提升激励分解为 PME、MSE 和 EE，清楚解释为什么“精准追责”可能削弱质量激励。
4. 系统比较 buyer pricing vs. supplier pricing，以及 exogenous responsibility vs. endogenous responsibility 四种制度环境下的质量和福利结果。
5. 给出管理启示：traceability 系统必须与价格和责任机制共同设计，否则可能造成 buyer-supplier incentive misalignment。

## 模型设定与假设 (Model Setup & Assumptions)

### 1. 基本参与者与产品质量

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $i \in \{1,\dots,n\}$ | 供应商编号 | 共有 $n \ge 2$ 个 competing suppliers |
| $q_i \in [0,1]$ | 供应商 $i$ 的产品质量 | 定义为产品不失败、不退货的概率 |
| $1-q_i$ | 产品失败概率 | 会触发 penalty cost |
| $q=(q_1,\dots,q_n)$ | 质量向量 | 供应商同时选择质量 |
| $c(q_i)$ | 单位生产成本 | 随质量上升而上升且凸；后文常用 $c(q)=\kappa q^2$ |
| $\kappa$ | 质量提升成本参数 | $\kappa$ 越高，提高质量越贵 |

这个模块刻画供应商的核心 trade-off：质量越高，市场份额更大、罚损更少，但生产成本更高。

### 2. 需求分配与竞争

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $\lambda_i(q,w)$ | 供应商 $i$ 的市场份额/采购份额 | 总需求标准化为 1 |
| $x_i(q_i,w_i)$ | 供应商 $i$ 的 attractiveness | 随质量上升、随价格下降 |
| $g(q_i)$ | 质量吸引力函数 | 递增，通常取 $g(q)=q^\beta$ |
| $f(w_i)$ | 价格吸引力函数 | 递减；供应商定价时影响份额 |
| $\beta \in (0,1]$ | attraction elasticity | 质量对需求份额的影响强度 |

市场份额函数为：

$$
\lambda_i(q,w)=\frac{x_i(q_i,w_i)}{\sum_{j=1}^n x_j(q_j,w_j)}.
$$

在 buyer pricing 下，买方给所有供应商统一批发价 $w$，因此价格项在份额中抵消，供应商主要通过质量竞争份额：

$$
\lambda_i(q)=\frac{g(q_i)}{\sum_{j=1}^n g(q_j)}.
$$

> 直觉：供应商不是面对固定采购量，而是通过质量争夺业务份额。质量提升不仅减少失败概率，还能吸引更多订单，这使得质量选择具有 strategic competition 的性质。

### 3. Penalty cost 与责任分配

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $b \ge 0$ | 单位产品失败导致的 penalty cost | 包括退货、维修、赔偿、商誉等成本 |
| $\alpha \in [0,1]$ | buyer responsibility | 买方承担总 penalty cost 的比例 |
| $1-\alpha$ | supplier-side responsibility | 由供应商承担的 penalty cost 比例 |
| ESR | Equal Sharing Rule | 无 traceability 时，供应商均摊总缺陷责任 |
| TSR | Target Sharing Rule | 有 traceability 时，缺陷产品由源头供应商承担责任 |

有 traceability 时，买方可以识别 defect product 的来源供应商，因此使用 TSR：

$$
P_i^{TSR}(q,w)=(1-\alpha)b(1-q_i)\lambda_i(q,w).
$$

> 直觉：供应商 $i$ 只为自己产品造成的失败付费。责任精准、问责清晰，没有横向搭便车或连带责任。

无 traceability 时，买方无法识别 defect product 来自谁，因此使用 ESR：

$$
P_i^{ESR}(q,w)=\frac{1}{n}(1-\alpha)b\sum_{j=1}^n(1-q_j)\lambda_j(q,w).
$$

> 直觉：所有供应商均摊供应商侧的失败责任。单个供应商会承担一部分别人产品失败带来的成本，也会让别人承担一部分自己产品失败带来的成本。

### 4. Pricing authority 与福利

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $w_i$ | 供应商 $i$ 的批发价 | supplier pricing 下各供应商可不同 |
| $w$ | 统一批发价 | buyer pricing 下买方统一设定 |
| $C_{buyer}(q,w)$ | 买方预期成本 | 包括采购成本和买方承担的 penalty cost |
| $\pi_i(q,w)$ | 供应商 $i$ 的预期利润 | 收入减生产成本和罚损分担 |
| $q^{FB}$ | first-best quality | 集中式供应链下最优质量 |

买方成本函数为：

$$
C_{buyer}(q,w)=\sum_{i=1}^n \left(w_i+\alpha b(1-q_i)\right)\lambda_i(q,w).
$$

> 直觉：买方每采购一单位产品，要支付批发价；如果产品失败，买方还承担 $\alpha$ 比例的 penalty cost。买方目标是最小化采购成本加自身责任成本。

供应商利润函数为：

$$
\pi_i(q_i,q_{-i},w_i,w_{-i})=(w_i-c(q_i))\lambda_i(q,w)-P_i(q,w).
$$

> 直觉：供应商的收入是批发价乘以获得的采购份额；成本包括质量生产成本和按责任机制分配到自己的 penalty cost。

集中式 first-best benchmark 为：

$$
C^{SW}(q)=c(q)+b(1-q),
$$

因此：

$$
q^{FB}=\arg\min_{q\in[0,1]}\{c(q)+b(1-q)\}.
$$

若 interior solution 存在，则满足 $c'(q^{FB})=b$。

> 直觉：集中式决策者只在乎质量提升的边际成本和减少失败罚损的边际收益。这个 benchmark 用来判断 decentralized pricing 和 responsibility sharing 是否导致质量 under-investment 或 over-investment。

### 博弈/决策结构

Players：

1. 一个 downstream buyer，例如采购商、零售商或平台。
2. $n$ 个 upstream competing suppliers。

Sequence of Events（对应论文 Figure 1，p.5）：

1. 买方决定是否采用 traceability-enabled technology，并选择相应 penalty-sharing mechanism。若研究 endogenous responsibility，买方也选择 $\alpha$。
2. 批发价被设定：buyer pricing 下由买方设定统一 $w$；supplier pricing 下由供应商设定各自 $w_i$。
3. 供应商同时选择产品质量 $q_i$。在 supplier pricing 的部分设定中，供应商同时选择 $w_i$ 和 $q_i$。
4. 买方按市场份额采购，产品销售给终端消费者。
5. 产品失败发生后产生 penalty cost；有 traceability 使用 TSR，无 traceability 使用 ESR。

Information Structure：

模型采用 complete information。供应商质量选择、成本函数、需求分配规则、责任机制和罚损成本都被各方知道。Traceability 的作用不是改变各方是否知道模型参数，而是改变 defect product 能否被准确归因到具体供应商。

### 关键假设及其作用

| 假设 | 合理性说明 | 放松后可能影响 |
|:---|:---|:---|
| 基准模型中供应商对称 | 便于清楚识别 traceability、pricing 和 responsibility 的机制效果 | 异质供应商会导致非对称质量和份额；论文在 extension 中考虑 asymmetric suppliers，主结论仍较稳健 |
| 质量 $q_i$ 是无故障概率 | 适用于退货、召回、维修和产品失败场景 | 若质量是多维度或难以观测，可能需要 moral hazard 或 hidden action 模型 |
| 质量成本递增且凸 | 高质量通常需要更高投入，且边际成本递增 | 若存在规模经济或学习效应，质量提升成本可能下降，traceability 的正向效果可能更强 |
| 总需求标准化为 1 | 重点研究供应商之间的份额竞争，而非市场总需求扩张 | 若总需求随质量提高而上升，会增加质量提升的整体收益；论文 extension 显示主结果仍成立 |
| Traceability 完美识别来源 | 抓住可追溯技术的核心经济功能 | 若 traceability 有噪音或错误归因，TSR 的激励效果会被削弱，责任合同更复杂 |
| 罚损成本 $b$ 固定 | 简化退货、维修、补偿等失败成本 | 若罚损成本与质量、批次、声誉或监管相关，福利效果可能更复杂 |
| 买方可以承诺责任机制 | 许多采购合同和供应商协议中可以事前写明召回和赔偿条款 | 若责任事后谈判，可能产生 renegotiation 和 hold-up 问题 |
| 完全理性和完全信息 | 标准博弈论建模起点 | 若供应商私有质量成本，需使用 mechanism design；文章也将其列为未来方向 |

## 分析路线图 (Roadmap of Analysis)

本文分析是一个四象限结构，两个维度分别是 pricing authority 和 buyer responsibility 是否外生。

1. First-best benchmark：先求集中式供应链的最优质量 $q^{FB}$，用于判断分散决策是否有效率。
2. Buyer pricing + exogenous responsibility：买方设统一批发价 $w$，$\alpha$ 给定。作者先解固定 $w$ 下供应商质量竞争，再反推买方最优 $w$。这一部分解释 traceability 为什么可能降低质量。
3. Buyer pricing + endogenous responsibility：买方同时选择 $w$ 和 $\alpha$。该部分回答：如果买方能设计责任分担，traceability 是否能帮助实现 first-best？
4. Supplier pricing + exogenous responsibility：供应商掌握批发价，且 $\alpha$ 给定。该部分回答：供应商定价权会如何改变 traceability 的质量和福利效果？
5. Supplier pricing + endogenous responsibility：买方选择 $\alpha$，供应商选择价格和质量。该部分展示一个更微妙的结果：traceability 可以总是让买方受益，但在某些情况下反而降低质量。
6. Extensions：考虑 asymmetric suppliers、alternative sharing mechanisms、traceability adoption cost、full-range recall、quality-sensitive market demand 等，验证主机制的稳健性。

逻辑上，文章先在 buyer pricing 下建立机制分解，再把 pricing power 和 responsibility control 逐步放开，以说明 traceability 的经济效果并非技术本身决定，而是制度环境决定。

## 核心分析与求解 (Analysis & Solution)

### Benchmark：First-best quality

在分析分散供应链之前，文章先给出集中式 benchmark。集中式系统最小化：

$$
C^{SW}(q)=c(q)+b(1-q).
$$

若 interior solution 存在，则：

$$
q^{FB}=\max\{q\in[0,1]:c'(q)\le b\}.
$$

> 经济直觉：first-best 质量由“提高质量的边际生产成本”和“减少失败罚损的边际收益”相等决定。它不受批发价和责任分担影响，因为这些只是供应链内部转移支付。后文所有 decentralized results 都可理解为：不同 pricing/responsibility 机制能否诱导供应商选择 $q^{FB}$。

### 从 first-best 到 decentralized game：为什么责任机制会影响质量？

在分散系统中，供应商不最小化系统总成本，而是最大化自身利润。质量提升的收益既来自减少 penalty cost，也来自抢占市场份额。因此，下一步要刻画固定批发价下的供应商质量竞争。

### Lemma 1：责任机制隐含一个最低质量标准

在 buyer pricing 且批发价给定时，作者定义 gross profit margin：

$$
r^{ESR}(q,w)=w-c(q)-\frac{1}{n}b(1-\alpha)(1-q),
$$

$$
r^{TSR}(q,w)=w-c(q)-b(1-\alpha)(1-q).
$$

对应的最低质量标准为：

$$
\hat q^{ESR}=\max\left\{q\in[0,1]:c'(q)\le \frac{1}{n}b(1-\alpha)\right\},
$$

$$
\hat q^{TSR}=\max\left\{q\in[0,1]:c'(q)\le b(1-\alpha)\right\}.
$$

Lemma 1 表明，在两种机制下，均衡质量都不低于对应的 $\hat q^M$。

> 经济直觉：如果质量低于这个标准，供应商提高一点质量不仅能减少自身或群体罚损，还能增加市场份额，因此一定有提高质量的动机。这个最低质量标准反映了 penalty responsibility 对供应商质量激励的底线约束。TSR 下供应商对自身缺陷承担更多责任，所以 $\hat q^{TSR}$ 通常高于 $\hat q^{ESR}$。

### Proposition 1 与 Proposition 3：固定批发价下，ESR 与 TSR 的质量均衡

Lemma 1 说明质量不会太低，但还没有给出均衡质量。接下来，作者分别刻画无 traceability 的 ESR 和有 traceability 的 TSR 下的 Nash equilibrium。

在 ESR 下，存在唯一 symmetric Nash equilibrium $q^{ESR}$，满足：

$$
w=w^{ESR}(q)=c(q)+\frac{n}{n-1}\frac{g(q)}{g'(q)}\left(c'(q)-\frac{1}{n}b(1-\alpha)\right).
$$

在 TSR 下，存在唯一 Nash equilibrium $q^{TSR}$，满足：

$$
w=w^{TSR}(q)=c(q)+b(1-\alpha)(1-q)+\frac{n}{n-1}\frac{g(q)}{g'(q)}\left(c'(q)-b(1-\alpha)\right).
$$

> 经济直觉：批发价越高，供应商获得市场份额的利润越大，因此更愿意提高质量来争夺份额。两个公式本质上都是供应商的一阶条件：质量提升的边际成本、罚损减少和份额竞争收益在均衡处相互平衡。TSR 和 ESR 的区别在于，TSR 将自己缺陷的供应商侧罚损完全压到自己身上，而 ESR 则把总罚损均摊给所有供应商。

### 关键机制：PME、MSE 与 EE

在解释 traceability 是否提高质量之前，文章做了一个非常重要的分解。供应商提高质量的边际激励可分为三部分：

1. Profit-Margin Effect (PME)：在既有市场份额上，提高质量会提高生产成本，但减少自身产品导致的罚损。
2. Market-Share Effect (MSE)：提高质量会增加自身市场份额，从而带来更多销售利润。
3. Externality Effect (EE)：在 ESR 下，一个供应商提高质量并扩大市场份额，会挤出其他供应商，从而减少群体总缺陷罚损；由于罚损被均摊，这也让自己受益。

**核心 trade-off：Traceability 强化 PME，但削弱 MSE，并消除 ESR 下的 EE。**

| 机制 | PME | MSE | EE |
|:---|:---|:---|:---|
| ESR | 质量提升减少的罚损被供应商群体共享，单个供应商只获得部分好处 | 增加份额带来的收益较强，因为自身不完全承担新增缺陷罚损 | 存在。提高自身质量会减少其他供应商份额和群体失败成本 |
| TSR | 自己质量提升减少的罚损完全归自己，PME 更强 | 增加份额也意味着自己要承担更多由自身产品缺陷导致的罚损，MSE 变弱 | 不存在或显著弱化，因为各自只承担自己的缺陷 |

> 经济直觉：Traceability 的正面作用是让“谁提高质量，谁减少罚损”更精确；负面作用是让质量竞争中原本由群体责任创造的外部激励消失。当市场份额对质量特别敏感时，MSE 和 EE 很重要，traceability 反而可能削弱质量激励。

### Proposition 2 与 Proposition 4：批发价和买方责任如何影响质量

在固定 wholesale price 下，ESR 中的均衡质量 $q^{ESR}$ 随批发价 $w$ 上升而上升，随买方责任 $\alpha$ 上升而下降。

在 TSR 中，均衡质量 $q^{TSR}$ 也随批发价 $w$ 上升而上升；但它对 $\alpha$ 的反应更复杂：当批发价足够高时，$q^{TSR}$ 随 $\alpha$ 上升而下降。

> 经济直觉：更高批发价让市场份额更值钱，供应商更愿意通过质量竞争抢份额。更高买方责任意味着供应商承担更少罚损，因此通常削弱质量激励。但在 TSR 下，$\alpha$ 同时改变既有份额上的罚损激励和新增份额上的利润空间，因此效果可能依赖批发价水平。

### Theorem 1：buyer pricing 下，买方最优批发价诱导的质量

前面的命题给出了固定 $w$ 下的质量。下一步，买方选择最优 $w$，以最小化自身采购加罚损成本。为得到闭式结果，作者设定：

$$
g(q)=q^\beta,\quad c(q)=\kappa q^2.
$$

在 ESR 下，买方定价诱导的质量为：

$$
q_{bp*}^{ESR}=1\wedge(q^{ESR}\vee q_{bp}^{ESR}),
$$

其中：

$$
q_{bp}^{ESR}=\frac{b}{2\kappa}\frac{1-\alpha+\alpha(n-1)\beta}{(n-1)\beta+2n}.
$$

在 TSR 下：

$$
q_{bp*}^{TSR}=1\wedge(\hat q^{TSR}\vee q_{bp}^{TSR}),
$$

其中：

$$
q_{bp}^{TSR}=\frac{b}{2\kappa}\frac{(n-1)\beta+n(1-\alpha)}{(n-1)\beta+2n}.
$$

> 经济直觉：买方通过批发价间接控制供应商质量。质量越高，买方承担的失败成本越低，但需要支付更高批发价来激励供应商。因此买方选择的是一个“诱导质量”的最优点，而不是直接选择质量。$\kappa$ 越高，提高质量越贵；$b$ 越高，缺陷越贵，买方越希望诱导高质量。

### Theorem 2：buyer pricing + exogenous responsibility 下 traceability 的质量与福利效果

有了买方最优批发价下的均衡质量后，作者比较 ESR 和 TSR，即比较无 traceability 和有 traceability。

Theorem 2 的核心结论：在 buyer pricing 且 $\alpha$ 外生给定时，traceability：

1. 当且仅当 $\kappa \ge \kappa_{(bp,q)}$ 时，会降低产品质量。
2. 当 $\kappa \le \kappa_{(bp,bc)}$ 时，会降低买方成本，即使买方受益。
3. 当且仅当 $\kappa \ge \kappa_{(bp,sc)}$ 时，会提高供应商利润。

> 经济直觉：当质量提升便宜时，TSR 的精准追责强化了供应商降低自身缺陷的激励，买方也因更高质量和较低罚损而受益。但供应商可能受损，因为买方通过定价抽取了部分收益。当质量提升很贵时，TSR 下供应商可能降低质量；买方不一定受益，但供应商可能因为更高批发价或更低质量成本而受益。论文 Figure 2（p.10）可视化了这一点：随着质量提升成本上升，ESR 与 TSR 下的质量、买方成本和供应商利润出现交叉。

这一定理给出第一个反直觉结果：**traceability 可以降低产品质量**。这不是因为技术差，而是因为责任机制改变了供应商的边际激励。

### Corollary 1：traceability 的 win-win 区域

Theorem 2 显示 buyer 和 suppliers 可能偏好不同。Corollary 1 进一步说明，当质量提升成本处于中等区间时，traceability 可以同时使 buyer 和 suppliers 受益：

$$
\kappa_{(bp,sc)}\le \kappa\le \kappa_{(bp,bc)}.
$$

> 经济直觉：质量提升太便宜时，买方更容易从 traceability 中获益，但供应商可能被压缩利润；质量提升太贵时，供应商可能获益，但买方可能因质量不足或价格上升受损。只有在中间区域，价格效应和质量效应能同时让双方改善。

### Theorem 3：endogenous responsibility 下 first-best 是否可达

前面假设 $\alpha$ 外生。接下来，作者允许买方选择 buyer responsibility。问题变成：买方是否能通过 $w$ 和 $\alpha$ 设计，让分散供应链达到 $q^{FB}$？

Theorem 3 表明：

1. 有 traceability 时，供应链总能被协调到 first-best quality。
2. 无 traceability 时，只有当 $\alpha$ 足够高时，first-best 才能达到。

> 经济直觉：TSR 下，缺陷可以准确归因，买方可以通过责任和价格设计让供应商内化自身产品失败成本。ESR 下，由于供应商均摊总失败责任，存在横向 externality：每个供应商既承担别人缺陷的一部分，也让别人承担自己缺陷的一部分。这种外部性使得责任设计更难，只有在买方承担足够责任、削弱供应商之间负外部性时，才能达到 first-best。

### Theorem 4 与 Corollary 2：buyer pricing + endogenous responsibility

在 buyer pricing 且买方同时选择 $w$ 和 $\alpha$ 时，Theorem 4 给出均衡：

1. TSR 下，买方选择 $\alpha_{bp*}^{TSR*}=0$，并实现 $q_{bp*}^{TSR*}=q^{FB}$。
2. ESR 下，均衡质量为 $q_{bp*}^{ESR*}=q_0^{ESR}\wedge q^{FB}$，买方有时需要承担正的责任比例以保证供应商参与。

Corollary 2 总结 traceability 的效果：当买方同时设置价格和责任时，traceability 在质量提升成本较低时严格提高质量并降低买方成本；供应商利润不变，因为买方通过责任和价格设计完全抽取供应商利润，令 $\pi_i=0$。

> 经济直觉：如果买方能控制批发价和责任分担，它会把 traceability 变成精准的 incentive alignment 工具。在 TSR 下，买方可以把供应商侧责任完全压给缺陷来源供应商，同时用价格保证参与约束刚好满足。供应商不赚信息租，买方获得 first-best 的运营效率。无 traceability 时，因为责任无法精准归因，买方需要留出更高责任或更高价格来避免供应商退出，因而可能无法达到同样效率。论文 Figure 3(a)（p.13）展示了这种 endogenous responsibility 下的质量和买方成本差异。

### Theorem 5：supplier pricing 下的均衡

前面都是 buyer pricing。接下来作者转向 supplier pricing：供应商自己设定 wholesale price 和质量。Theorem 5 表明，在每种机制 $M\in\{ESR,TSR\}$ 下，存在唯一 symmetric Nash equilibrium。

> 经济直觉：supplier pricing 下，供应商不只是通过质量抢份额，也能通过价格抢份额或通过高质量收取高价。价格和质量成为联合战略变量，因此 traceability 的福利分配会明显不同：供应商更可能把高质量和精准追责转化为更高批发价。

### Theorem 6：supplier pricing + exogenous responsibility 下 traceability 的效果

当供应商设定批发价且 $\alpha$ 外生时，Theorem 6 表明 traceability：

1. 总是提高产品质量。
2. 总是使供应商受益。
3. 对买方可能有利也可能有害：当 $\kappa$ 较低时买方受益，当 $\kappa$ 较高时买方可能受损。

> 经济直觉：供应商掌握定价权后，可以为更高质量收取更高批发价，因此 traceability 不再像 buyer pricing 中那样容易压缩供应商利润。对供应商而言，精准追责加上自主定价通常是好事。对买方而言，高质量会减少罚损，但高批发价会增加采购成本；当质量提升便宜时，质量收益大于价格损失，买方受益；当质量提升贵时，买方可能支付更高价格却没有获得足够质量改善。论文 Figure 4（p.14）显示 supplier pricing 下 suppliers 对 TSR 的偏好区域明显扩大，而 buyer 偏好 TSR 的区域更小。

### Theorem 7 与 Corollary 3：supplier pricing + endogenous responsibility

最后，作者考虑买方能选择 $\alpha$，但供应商掌握价格和质量决策。Theorem 7 表明：

1. TSR 下，买方选择 $\alpha_{sp*}^{TSR*}=0$，实现 $q_{sp*}^{TSR*}=q^{FB}$。
2. ESR 下，买方选择一个能刚好抽取供应商利润的责任水平，均衡质量由供应商参与约束和竞争共同决定。

Corollary 3 总结 traceability 的效果：

1. 当且仅当 $\kappa>\kappa_{sp*}^*$ 时，traceability 会损害产品质量。
2. Traceability 总是使买方受益。
3. Traceability 对供应商利润没有影响，因为供应商利润被买方抽取到零。

> 经济直觉：这部分结果最微妙。TSR 实现 first-best，但 first-best 不一定比 ESR 下的质量更高。当质量提升成本很高时，ESR 下的群体责任和质量竞争可能导致供应商过度投资质量；traceability 把质量拉回 first-best，因此从系统效率看是好事，但从“质量水平”看反而下降。买方仍然受益，因为它降低的是总成本，而不是单纯追求最高质量。

### Extensions：主结论的稳健性

论文在 online E-Companion 中进一步考察多个扩展，主文本也概述其结论。

#### Asymmetric suppliers

扩展内容：允许供应商质量提升成本不同。

核心发现：供应商异质性会改变各自质量、份额和利润分配，但 traceability 通过责任归因改变 PME/MSE/EE 的主机制仍然存在。

与主模型关系：增强结论稳健性。对称性主要是为了得到清晰闭式解，不是反直觉结论的唯一来源。

#### Alternative sharing mechanisms

扩展内容：考虑不使用 ESR，而使用其他 group-sharing rules，例如按 market share 分摊。

核心发现：某些看似自然的分摊规则可能比 ESR 更差，导致更低质量。

与主模型关系：补充说明 no traceability 下的责任机制设计本身也很重要，不能简单认为任何 group sharing 都等价。

#### Costly traceability adoption

扩展内容：引入采用 traceability 的固定或可变成本。

核心发现：采用成本会缩小 traceability 的福利可行区域，但不会改变“traceability 可能降低质量或造成利益冲突”的机制。

与主模型关系：使管理建议更保守。即便不考虑 adoption cost，traceability 都不一定总是好；考虑成本后更需谨慎。

#### Full-range recall without traceability

扩展内容：在食品和药品行业，如果无法识别问题来源，可能需要全范围召回，包含非缺陷产品。

核心发现：召回范围扩大改变 penalty cost 的规模和分配，但 traceability 的核心权衡仍成立。

与主模型关系：增强对食品、药品和批次召回场景的适用性。

#### Quality-sensitive market demand

扩展内容：放松总需求固定为 1 的假设，允许总市场需求随质量上升。

核心发现：质量提升带来的总需求扩大可能强化质量投资动机，但 traceability 对质量和福利的非单调影响仍可出现。

与主模型关系：说明固定总需求假设不是反直觉结果的根源。

## 比较静态汇总表 (Comparative Statics Summary)

| 参数/制度变化 | 对产品质量的影响 | 对 buyer welfare 的影响 | 对 supplier welfare 的影响 | 直觉 |
|:---|:---|:---|:---|:---|
| $\kappa \uparrow$ | 质量通常下降；buyer pricing + exogenous $\alpha$ 下，traceability 更可能降低质量 | Traceability 对买方吸引力下降 | buyer pricing 下供应商更可能偏好 traceability；supplier pricing + exogenous $\alpha$ 下供应商始终偏好 traceability | 质量提升越贵，精准追责带来的质量改善收益越弱，价格/成本分配效应更重要 |
| $b \uparrow$ | 供应商更愿意提高质量 | 买方更重视降低缺陷罚损，因此更可能偏好能有效提高质量的 traceability | 若责任压向供应商，供应商可能因更高罚损暴露而受损 | 缺陷越贵，质量的边际价值越高 |
| $\alpha \uparrow$ | ESR 下固定价格时质量下降；TSR 下效果取决于价格水平，但高价格下也下降 | 买方直接承担更多罚损，短期成本上升 | 供应商承担更少罚损，质量激励下降但责任负担减轻 | 买方责任越高，供应商内化失败成本越少 |
| $n \uparrow$ | 竞争增强；buyer pricing 下扩大 traceability 提升质量的参数区域 | 在部分条件下扩大买方偏好 traceability 的区域 | 竞争会压缩供应商 rents | 更多供应商使份额竞争更强，质量成为争夺订单的重要工具 |
| $\beta \uparrow$ | 市场份额对质量更敏感；MSE 和 EE 更重要 | Traceability 的净效果更依赖质量竞争强度 | ESR 下群体责任造成的外部性更重要 | 当质量对份额影响强时，traceability 削弱 MSE/EE 的负面作用更可能显现 |
| buyer pricing 转向 supplier pricing | Exogenous $\alpha$ 下 traceability 更稳定地提高质量 | 买方更可能被高批发价抵消质量收益 | 供应商更容易从 traceability 中获益 | 供应商有定价权时，可以把质量和精准责任转化为价格溢价 |
| $\alpha$ 从外生变为 buyer endogenous | Traceability 更容易实现 $q^{FB}$，但不总是意味着质量水平更高 | 买方通常更受益，因为可通过责任设计抽取利润和降低成本 | 供应商利润可能被抽取至零 | 责任选择权让买方能把 traceability 变成合同控制工具 |
| 无 traceability 的 ESR 改为 TSR | PME 增强，MSE/EE 削弱；质量可能升也可能降 | 取决于质量提升成本和定价权 | 取决于定价权和责任设计 | 精准追责既能减少 moral hazard，也可能消除群体责任下的竞争外部性 |

## 主要结论与管理启示 (Main Results & Managerial Insights)

### 与直觉 benchmark 的对比

| 常见直觉 | 本文发现 | 为什么重要 |
|:---|:---|:---|
| Traceability 能精准追责，因此一定提高质量 | 不一定。buyer pricing 且质量提升成本高时，traceability 可能降低质量 | 技术透明度不等于激励相容；问责机制可能改变质量竞争方向 |
| 谁造成缺陷谁负责一定最好 | 不一定。TSR 强化自身罚损内化，但削弱 ESR 下的 market-share 和 externality 激励 | 群体责任虽然粗糙，却可能在某些环境中制造更强的质量竞争 |
| Buyer 总是喜欢 traceability | 不一定。若供应商掌握定价权且质量提升昂贵，买方可能因批发价上升而受损 | 采用 traceability 前需要评估 pricing power 和 pass-through |
| Suppliers 会害怕 traceability | 不一定。supplier pricing 下，供应商总是受益；buyer pricing 下质量提升成本高时也可能受益 | Traceability 可能成为供应商提价或降低成本暴露的工具 |
| 质量越高越好 | 从系统效率看不一定。endogenous responsibility 下，traceability 可能把过高质量拉回 first-best | 管理目标应是最小化总成本，而非机械追求最高质量 |

### 四种制度环境下的 traceability 效果

| Pricing authority | Buyer responsibility | 质量效果 | Buyer welfare | Supplier welfare |
|:---|:---|:---|:---|:---|
| Buyer pricing | Exogenous $\alpha$ | $\kappa$ 小时提高质量；$\kappa$ 大时可能降低质量 | $\kappa$ 小时受益 | $\kappa$ 大时受益；$\kappa$ 小时可能受损 |
| Supplier pricing | Exogenous $\alpha$ | 总是提高质量 | $\kappa$ 小时受益，$\kappa$ 大时可能受损 | 总是受益 |
| Buyer pricing | Endogenous $\alpha$ | TSR 达到 $q^{FB}$；当 ESR 低效时严格改善 | 当 $\kappa$ 小且 ESR 低效时降低买方成本 | 不变，通常被抽取到 $\pi_i=0$ |
| Supplier pricing | Endogenous $\alpha$ | TSR 达到 $q^{FB}$；当 ESR 过度投资质量时，traceability 反而降低质量 | 总是受益 | 不变，通常被抽取到 $\pi_i=0$ |

### 管理建议

1. 采用 traceability 前先判断质量提升成本 $\kappa$。如果供应商提高质量很便宜，traceability 更可能真正改善质量并降低买方成本；如果质量提升很贵，它可能主要改变利润分配，而非改善质量。

2. 不要把 traceability 当成独立技术投资，应与 penalty-sharing contract 一起设计。有 traceability 但责任机制不合理，可能只是让责任归属更清楚，却没有给供应商正确激励。

3. Buyer pricing 环境下，买方应注意供应商参与约束。如果买方把 traceability 的收益全部通过低价抽走，供应商可能缺乏配合或长期质量投资动力。

4. Supplier pricing 环境下，买方要预期供应商可能提价。Traceability 提高质量的同时，供应商可能将其转化为批发价溢价；买方需评估质量收益是否覆盖价格上升。

5. 当买方可以决定责任分担时，traceability 能成为强大的合同治理工具。但“把责任全部压给供应商”虽然可能实现成本最优，也可能造成公平性、合作关系和长期投资问题。

6. 政策制定者在推动食品、药品、矿产、汽车等行业 traceability 时，不应只规定信息记录标准，还应关注召回责任、赔偿责任和供应商参与机制。

7. 对多供应商采购系统，供应商数量和质量竞争强度很关键。竞争越强，质量和份额之间的互动越复杂，traceability 的效果越需要用模型化方式评估。

## 与相关文献的对话 (Dialogue with Literature)

### Dong et al. (2023a), Management Science

共同关注点：traceability 在食品供应链中的价值，以及 traceability 是否可能降低产品质量。

本文推进：Dong et al. 将 traceability 的影响分解为 pure traceability effect 和 strategic pricing effect，并说明当后者占优时质量可能下降。本文进一步引入 endogenous market share、责任纵向分配和两种 pricing authority，说明质量下降不仅来自战略定价，也可能来自 PME/MSE/EE 的激励结构变化。

为什么重要：本文把“traceability 可能降低质量”的机制从特定食品召回环境推广到更一般的多供应商质量竞争和责任分担环境。

### Cui et al. (2023), Manufacturing & Service Operations Management

共同关注点：traceability-driven blockchain 的价值和设计，特别是在 serial/parallel supply chains 中对质量和召回的影响。

本文推进：Cui et al. 发现 traceability 在 serial supply chain 中提高质量，但在 parallel system 中可能因 flexible recall cost saving 而降低质量。本文则聚焦一个 buyer 和多个 competing suppliers，允许市场份额由质量内生决定，并比较 buyer pricing 与 supplier pricing。

为什么重要：本文解释了当供应商通过质量争夺采购份额时，traceability 的效果不能只从召回成本节约看，还必须看竞争激励和责任归因。

### Babich and Hilary (2020), Manufacturing & Service Operations Management

共同关注点：blockchain/distributed ledger 对 operations management 的影响，尤其是透明度、可验证性和供应链协调。

本文推进：Babich and Hilary 更像是 blockchain 与 OM 的综述和研究议程，强调技术能带来的信息和治理能力。本文提供了一个具体机制模型，说明这种信息能力在合同和定价结构下可能产生正反两种运营结果。

为什么重要：它提醒 OM 领域不能把 blockchain transparency 简化为“信息更多一定更好”；信息必须被嵌入激励系统。

### Pun et al. (2021), Production and Operations Management

共同关注点：blockchain adoption 如何影响质量、消费者福利和社会福利。

本文推进：Pun et al. 讨论 blockchain 对 deceptive counterfeits 的抑制作用，偏向消费者识别和防伪。本文关注供应链内部责任归属和多供应商质量竞争，尤其是 buyer/supplier welfare 的分配。

为什么重要：两篇文章共同说明 blockchain/traceability 的价值来自改变激励，但本文更强调 upstream accountability 和 pricing power 对质量的影响。

## 犀利评论 (Reviewer's Critique)

### 优点

理论贡献清楚。文章没有停留在“traceability improves transparency”的直觉，而是把 traceability 的经济作用拆解为责任归因机制，并进一步分解供应商质量激励为 PME、MSE 和 EE。这使反直觉结果有清楚的微观机制。

方法上结构完整。四象限分析覆盖 buyer pricing/supplier pricing 与 exogenous/endogenous responsibility，能够系统说明不同制度环境下 traceability 的差异效果。模型相对简洁，但能产生丰富结论。

实践相关性强。食品、药品、汽车、海鲜、矿产和零售平台都面临可追溯、召回和责任分配问题。文章对“技术投资应与合同机制共同设计”的管理含义很明确。

### 模型限制/假设过强

第一，基准模型中 traceability 是完美的。现实中追溯系统可能存在数据造假、批次混合、标签错误、平台录入不完整或供应商绕开系统的问题。若 traceability 只是 noisy attribution，TSR 的精准问责效果会减弱。

第二，买方对责任机制的承诺能力较强。现实合同中，质量事故后可能发生重新谈判、法律争议或公关压力，实际责任未必完全按事前合同执行。

第三，供应商质量成本和能力在基准模型中对称且完全信息。虽然 extension 考虑了异质性，但若质量成本是供应商私有信息，买方设计 $w$ 和 $\alpha$ 会面临 screening 与 information rent 问题，供应商利润未必能被完全抽取。

第四，消费者侧被相对简化。总需求在基准模型中固定，消费者对 traceability 本身的信任、支付意愿、品牌声誉和产品认证没有成为核心变量。对于食品、有机产品、奢侈品和药品，这可能是重要需求端机制。

第五，模型以静态博弈为主。现实中的供应商质量投资、信任、声誉和技术采用往往是动态过程。一次事故可能改变未来采购份额、监管处罚和消费者信任。

### 未来研究方向

1. Imperfect traceability：研究 traceability 系统存在错误归因、漏报、供应商篡改或审计概率时，TSR 是否仍然优于 ESR，以及最优处罚强度如何设计。

2. Asymmetric information and mechanism design：若供应商的质量提升成本 $\kappa_i$ 是私有信息，买方如何联合设计批发价、责任比例、审计和 traceability adoption subsidy？

3. Dynamic reputation model：将供应商质量投资放入重复博弈，研究 traceability 如何影响长期声誉、未来订单分配和关系型合同。

4. Consumer demand response：引入消费者对 traceability 标签的支付意愿和信任更新，区分“traceability 作为内部问责工具”和“traceability 作为市场信号”的双重作用。

5. Empirical validation：利用食品召回、汽车缺陷、药品批次追踪或平台供应商数据，检验 traceability adoption 后质量、价格、召回范围和供应商份额是否发生模型预测的变化。

6. Cost-sharing for traceability adoption：本文主要把 traceability adoption 作为买方决策或扩展中的成本项。未来可以研究买方与供应商如何分摊 traceability 系统建设成本，以及成本分摊如何影响 adoption 和质量。

## 一句话总结

本文最重要的贡献是把 traceability 从“信息技术”重新定义为“责任分配和激励设计工具”：它能提高质量，也可能降低质量；能创造 win-win，也可能只是重新分配利润。真正决定效果的不是追溯技术本身，而是定价权、责任分担和质量提升成本三者之间的匹配。

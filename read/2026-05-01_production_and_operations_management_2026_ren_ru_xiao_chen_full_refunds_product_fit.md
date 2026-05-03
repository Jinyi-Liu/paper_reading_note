# Why Full Refunds Prevail: A Product Fit Perspective

**作者**：Weitao Ren（Shanghai Jiao Tong University）、Chuanshuai Ru（Shanghai Jiao Tong University）、Wenqiang Xiao（New York University）、Fangruo Chen（Shanghai Jiao Tong University）  
**期刊与年份**：Production and Operations Management，2026  
**文章类型**：理论模型 / Return Policy Design / Screening Contract  
**DOI**：10.1177/10591478261442318

**中文摘要**：

这篇文章研究在线卖家如何通过“售价 + 退款额”的退货合同，管理消费者因产品是否合适而产生的异质性。模型中有两类消费者：informed consumers 已经知道产品适合自己；uninformed consumers 购买前不知道产品是否适合，只能在收到后发现是否 misfit。文章的核心发现是：如果消费者的不确定性只来自“产品是否合适”这一种 misfit risk，那么卖家不需要复杂的差异化合同，一个统一的全额退款合同就可以实现最优菜单。退款额为 uninformed consumers 提供 misfit 保险，售价则用来提取消费者剩余，因此全额退款并不只是“善待消费者”，也可以是利润最大化的筛选机制。

但是，当产品即使 fit 也存在质量波动，即 quality risk 时，结论发生变化。全额退款不再最优，卖家会转向部分退款；当 quality risk 较高时，最优菜单会变成差异化合同：给 informed consumers 一个低价、低退款的 no-frills option，给 uninformed consumers 一个高价、高退款的 insurance-heavy option。此时，卖家故意提高 uninformed contract 的退款额，使其更像保险，从而让 informed consumers 不愿模仿。文章还进一步讨论了 misfit 产品仍有残余价值、卖方退货处理成本、消费者退货 hassle cost 等扩展，说明“统一合同在纯 misfit risk 下最优”这一机制相当稳健。

## 论文速览

| 维度 | 内容 |
|:---|:---|
| 研究问题 | 为什么在线零售中高成本的全额退款政策如此普遍？当消费者对产品是否合适存在不同信息时，卖家应设计统一退货政策还是差异化合同菜单？ |
| 核心场景 | 在线市场中同时存在熟悉产品的老顾客和不熟悉产品的新顾客；新顾客面临产品 misfit risk。 |
| 方法 | 垄断卖家的机制设计 / screening contract 模型。卖家设计合同菜单 $\{(p_I,b_I),(p_N,b_N)\}$，其中 $p$ 是售价，$b$ 是退款额。 |
| 消费者类型 | Informed consumers 知道产品 fit；uninformed consumers 只以概率 $\lambda$ 得到 fit 产品，概率 $1-\lambda$ 发生 misfit。 |
| 主模型结论 | 只存在 misfit risk 时，单一全额退款合同 $p^*=b^*=\theta$ 可以实现最优菜单，并让两类消费者都只获得零净效用。 |
| 关键机制 | 退款额负责“保险”：让 uninformed consumers 可以免费试错；售价负责“榨取剩余”：把消费者愿意支付的价值提取出来。两个工具分工明确。 |
| 反直觉之处 | 全额退款不是因为卖家忽略退货成本，而是因为它能在信息不对称下同时解决参与约束和激励相容约束。 |
| 何时不再全额退款 | 当 fit 产品本身也有质量波动，即 quality risk 时，full refund 会诱发过多 fit-product returns，卖家改用 partial refund。 |
| 何时需要差异化合同 | 当 quality risk 足够高时，卖家需要菜单：低价低保障给 informed consumers，高价高保障给 uninformed consumers。 |
| 管理启示 | 如果退货主要来自“合不合适”，统一全额退款可能是理性的利润最大化政策；如果退货来自质量波动或高价值商品的体验差异，则应考虑部分退款或分层退货政策。 |

## TL;DR

这篇文章解释了一个看似矛盾的现象：退货很贵，但全额退款仍然很常见。它的答案是，如果消费者主要担心“买回来不合适”，全额退款其实是一种让消费者免费试错的保险，卖家可以通过提高售价把剩余拿回来。只有当产品本身质量也不稳定时，全额退款才会变得太宽松，卖家才需要部分退款或差异化退货合同。

## One More Thing

本文最有意思的洞察是：**全额退款并不一定是卖家对消费者的让利，它可能是一种非常锋利的榨取剩余工具**。直觉上，退款越慷慨，卖家越吃亏；但在这个模型里，全额退款让不知道产品是否适合的新顾客敢于购买，因为买错了可以无成本退掉。一旦消费者愿意进场，卖家就可以把售价设到 fit 产品的完整价值 $\theta$。也就是说，退款政策把“适不适合”的信息发现推迟到购买之后完成，而售价则把消费者愿意为这个免费试用机会支付的价值提前收走。

这也是本文相对经典 return policy 文献的主要推进：以前很多模型认为退货政策主要是在“扩大需求”和“控制退货成本”之间权衡；本文强调，在存在 informed 和 uninformed consumers 的市场里，退货政策还承担一个 screening / insurance 的功能。全额退款之所以普遍，不是因为现实企业没有算清成本，而是因为在某些信息结构下，它本身就是最优机制。

## 研究背景与动机 (Motivation)

### 实践痛点：退货成本很高，但宽松退货政策依然普遍

在线零售的一个基本矛盾是：退货非常昂贵，但消费者又非常在意退货政策。文章引用的行业背景包括：2023 年美国零售退货总额达到 7430 亿美元，其中线上订单退货率达到 17.6%，对应 2470 亿美元；每次退货的运输、补货、折价等成本可消耗商品原价的 20%–65%。与此同时，退货政策强烈影响购买决策：UPS 调查显示 88% 的消费者购物时会查看退货政策，66% 会在下单前查看；正向退货体验会提升复购意愿。

这形成一个清晰的运营问题：**卖家为什么愿意承担高昂退货成本，仍然提供 Amazon、Zappos 等平台常见的 full-refund / free-return policy？**

### 理论缺口：既有模型很难解释“全额退款为何普遍”

经典 cost-recovery 视角通常认为，如果消费者面临估值不确定性且退货有成本，卖家应通过 partial refund、restocking fee 或 no refund 控制退货。例如 Su (2009) 这类模型会强调 salvage value、handling cost 与退货成本回收，因此 full refund 常常不是最优。

但现实中，很多在线平台不仅提供宽松退货政策，而且同一产品有时还会以不同“价格—退款”组合出现。这说明退货条款不仅是售后服务，也可能是一种合同工具。本文认为既有文献忽略了一个关键异质性来源：**消费者对产品 fit 的信息不同**。老顾客可能知道自己适合某个品牌或尺码，新顾客则需要购买后才知道。

### 本文的核心贡献

1. **把 product misfit risk 放在中心位置**：文章不是从一般 valuation uncertainty 出发，而是区分“产品是否适合”与“fit 后质量如何”两类风险。
2. **解释 full refund 的内生最优性**：在纯 misfit risk 下，统一全额退款合同可以内生地从 IC/IR 约束中产生，而不是外生假设。
3. **说明何时需要 partial refund 和合同菜单**：当引入 quality risk 后，full refund 不再最优；当 quality risk 高时，差异化菜单成为筛选消费者类型的工具。
4. **统一解释多种退货实践**：full refund、partial refund、no refund、overcompensating refund 都可以在不同风险结构和成本结构下得到解释。

## 模型设定与假设 (Model Setup & Assumptions)

### 消费者与市场结构

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $I$ | informed consumers | 熟悉产品，购买前知道产品 fit。 |
| $N$ | uninformed consumers | 不熟悉产品，购买前不确定产品是否 fit。 |
| $\rho$ | informed consumers 的比例 | 市场中有 $\rho$ 的消费者为 informed。 |
| $1-\rho$ | uninformed consumers 的比例 | 市场中剩余消费者为 uninformed。 |
| $\lambda$ | uninformed consumers 的 fit 概率 | $N$ 型消费者以概率 $\lambda$ 得到 fit 产品，以概率 $1-\lambda$ 遇到 misfit。 |

这一模块的作用是刻画消费者异质性。本文的异质性不是“偏好高低不同”，而是“购买前知道的信息不同”：informed consumers 确定 fit，uninformed consumers 面临 fit uncertainty。

### 产品估值与成本

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $\theta$ | fit 产品的估值 | 主模型中为确定值，且两类消费者在 fit 后价值相同。 |
| $0$ | misfit 产品的估值 | 主模型假设 misfit 产品对 uninformed consumers 没有价值。 |
| $c$ | 单位生产成本 | 满足 $0<c<\theta$。 |
| $\tilde{\theta}$ | 随机 fit valuation | 在扩展中用于刻画 quality risk，$\tilde{\theta}\sim U[\theta-\delta,\theta+\delta]$。 |
| $\delta$ | quality risk 强度 | 越大表示 fit 产品质量波动越大。 |
| $\theta_L$ | misfit 产品残余价值 | 在扩展中表示 misfit 产品仍有部分价值。 |
| $h$ | consumer return hassle cost | 消费者退货时承担的时间、运输、包装等成本。 |
| $s$ | salvage value | 退回商品对卖家的残值，扩展中与 $c$ 分离。 |
| $k$ | handling cost | 卖家处理退货的单位成本。 |

这一模块区分三类不同风险：misfit risk 是“是否合适”；quality risk 是“即使合适，质量也可能高低不同”；misfit valuation risk 是“不合适时仍然可能有多少残余价值”。

### 合同变量

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $p_j$ | 面向类型 $j$ 的售价 | $j\in\{I,N\}$。 |
| $b_j$ | 面向类型 $j$ 的退款额 | 文章称 return price，即消费者退货时获得的 refund。 |
| $(p_j,b_j)$ | 一份退货合同 | 卖家可提供菜单 $\{(p_I,b_I),(p_N,b_N)\}$。 |
| $b_j=0$ | no-refund policy | 不退款。 |
| $b_j=p_j$ | full-refund policy | 全额退款。 |
| $0<b_j<p_j$ | partial-refund policy | 部分退款或 restocking fee。 |

合同变量承担两种经济功能：$p_j$ 用于提取消费者剩余，$b_j$ 用于改变消费者承担的风险和退货行为。

### Players、Sequence of Events 与 Information Structure

**Players**：一个垄断卖家和单位质量的一群消费者。消费者分为 informed 和 uninformed 两类。

**Sequence of Events**：

1. 卖家生产产品，并设计退货合同菜单 $\{(p_I,b_I),(p_N,b_N)\}$。
2. 消费者观察菜单后，选择一份合同或退出市场。
3. 消费者购买产品并支付相应售价 $p_j$。
4. 收到产品后，消费者观察实际估值；uninformed consumers 此时发现产品是否 fit。
5. 消费者决定保留产品还是退货；若退货，获得退款 $b_j$。
6. 卖家利润与消费者效用实现。

**Information Structure**：

卖家知道市场总体比例 $\rho$ 和 fit 概率 $\lambda$，但不能观察单个消费者的类型。消费者知道自己的类型；informed consumers 知道产品 fit，uninformed consumers 购买前不知道产品是否 fit。卖家因此需要通过合同菜单诱导 self-selection。

### 主模型效用函数

对于选择合同 $(p_j,b_j)$ 的 informed consumer，其效用为：

$$
U_{Ij}=\max(\theta,b_j)-p_j.
$$

> 直觉解读：informed consumer 知道产品 fit，因此保留产品的价值是 $\theta$。如果退款额 $b_j$ 超过 $\theta$，消费者甚至可能为了套利而退货；否则就保留产品。售价 $p_j$ 是消费者支付的成本。由于主模型中最优退款不会超过 $\theta$，informed consumers 本质上只关心售价，不关心退款额。

对于选择合同 $(p_j,b_j)$ 的 uninformed consumer，其期望效用为：

$$
U_{Nj}=\lambda\max(\theta,b_j)+(1-\lambda)b_j-p_j.
$$

> 直觉解读：uninformed consumer 以概率 $\lambda$ 得到 fit 产品，此时可在保留价值 $\theta$ 和退款额 $b_j$ 之间选择更高者；以概率 $1-\lambda$ 遇到 misfit，主模型中 misfit 价值为 0，因此会退货并获得 $b_j$。所以 $b_j$ 对 uninformed consumers 来说是真正的保险。

### 卖家目标函数与约束

卖家最大化期望利润：

$$
\max_{(p_I,b_I),(p_N,b_N)}\rho\left[p_I-b_I\mathbf{1}\{b_I>V_I\}-c\mathbf{1}\{b_I\le V_I\}\right]+(1-\rho)\left[p_N-\mathbb{E}\left(b_N\mathbf{1}\{b_N>V_N\}+c\mathbf{1}\{b_N\le V_N\}\right)\right].
$$

> 直觉解读：每卖出一件商品，卖家收到售价 $p_j$。如果消费者保留产品，卖家承担生产成本 $c$；如果消费者退货，卖家支付退款 $b_j$，而商品没有被最终消费。在主模型中，informed consumers 通常不会退货；uninformed consumers 在 misfit 时退货。卖家利润由“收价—生产成本—退款支出”构成。

合同菜单必须满足激励相容约束：

$$
U_{II}\ge U_{IN},\qquad U_{NN}\ge U_{NI}.
$$

> 直觉解读：每类消费者都必须愿意选择为自己设计的合同。第一条防止 informed consumers 模仿 uninformed contract，第二条防止 uninformed consumers 模仿 informed contract。

合同菜单还必须满足参与约束：

$$
U_{II}\ge 0,
\qquad
U_{NN}\ge 0.
$$

> 直觉解读：两类消费者选择合同后的净效用不能低于退出市场的 outside option。文章主模型把 outside option 规范化为 0。

### 关键假设、合理性与放松后的影响

| 假设 | 合理性说明 | 放松后的可能影响 |
|:---|:---|:---|
| 垄断卖家 | 聚焦单个卖家如何设计退货政策，避免价格竞争干扰核心机制。 | 竞争会让退货政策变成争夺需求的工具，可能削弱卖家的剩余提取能力。 |
| 两类消费者：informed 与 uninformed | 在线市场常有老顾客与新顾客；老顾客了解尺码、品牌、性能，新顾客不了解。 | 更多类型或连续型信息可能导致更复杂的合同菜单。 |
| Informed consumers 确定 fit | 把“经验带来的产品适配信息”形式化。 | 如果 informed consumers 也可能 misfit，全额退款的保险功能会覆盖更多消费者，结果可能更接近统一合同。 |
| Fit valuation 在主模型中为共同确定值 $\theta$ | 建立干净 benchmark，隔离 misfit risk。 | 文章 Section 5.1 表明，一旦 fit valuation 随机，full refund 不再最优，高 quality risk 下需要差异化合同。 |
| Misfit valuation 在主模型中为 0 | 捕捉买错尺码、买错功能等完全不合适的场景。 | 若 misfit 产品仍有残值，卖家可能转向 no refund 或 partial refund。 |
| 退货商品完全可再售且无处理成本 | 先突出消费者信息结构，而非卖方成本回收。 | 文章 Section 5.4 显示，seller-side costs 改变利润水平，但在纯 misfit risk 下不改变 full-refund 的 IC 机制。 |
| 消费者无退货 hassle cost | 建立基准模型。 | 若存在 hassle cost，低 hassle 时卖家会提供 $b=\theta+h$ 的 overcompensating refund；高 hassle 时转向 no refund。 |

## 分析路线图 (Roadmap of Analysis)

文章的分析是一个逐步“加风险、放松假设”的结构。

1. **Base model：只有 misfit risk**  
   Fit 产品价值确定为 $\theta$，misfit 价值为 0。核心问题是：消费者类型不可观测时，卖家是否需要差异化退货合同？结论是：不需要，统一全额退款合同最优。

2. **Random fit valuation：加入 quality risk**  
   即使产品 fit，实际价值也在 $[\theta-\delta,\theta+\delta]$ 上波动。核心问题是：fit 产品也可能低质量时，full refund 是否仍然成立？结论是：不成立；低 quality risk 下统一 partial refund 最优，高 quality risk 下差异化菜单最优。

3. **Partial / random misfit valuation：misfit 产品仍有残余价值**  
   核心问题是：如果“不合适”不等于“完全没价值”，退款政策怎么变？确定残值下可能出现 no refund；随机残值下可能出现 partial refund，用于筛选 uninformed consumers 内部的异质性。

4. **Seller-side cost：salvage value 与 handling cost**  
   核心问题是：如果退货对卖家很贵，是否推翻 full refund？结论是：纯 misfit risk 下不推翻，因为这些成本影响利润水平，但不改变消费者 IC/IR 的结构。

5. **Consumer-side cost：hassle cost**  
   核心问题是：如果消费者退货有麻烦成本，卖家是否还应全额退款？结论是：低 hassle 时应过度补偿，高 hassle 时 no refund 反而最优。

## 核心分析与求解 (Analysis & Solution)

### Proposition 1：纯 misfit risk 下，单一全额退款合同最优

**命题内容**：在主模型中，所有满足 IC 和 IR 的退货合同菜单中，卖家最优合同可以写成：

$$
p_I^*=p_N^*=\theta,
\qquad
b_I^*=b_N^*=\theta.
$$

这是一份统一 full-refund contract，因为售价和退款额相等。

> **Economic Intuition**：退款额 $b$ 和售价 $p$ 在这里完成了非常清晰的分工。对 uninformed consumers 来说，$b$ 是 misfit insurance：买错可以退，且不损失。对 informed consumers 来说，只要 $b\le\theta$，他们不会退货，因此 $b$ 对他们几乎无关，他们只关心 $p$。卖家把 $b$ 提高到 $\theta$，让 uninformed consumers 不再担心 misfit；再把 $p$ 提高到 $\theta$，把 fit 产品的全部价值收走。最终，两类消费者都愿意购买，但都没有正净效用。

**关键 trade-off**：在纯 misfit risk 下，**提高退款额并不只是增加退货成本，它同时提高了 uninformed consumers 的购买意愿，从而允许卖家提高售价。**当退款额恰好达到 $\theta$ 时，这种保险功能足以支撑售价也达到 $\theta$。

### Corollary 1：利润随 informed consumer 占比和 fit 概率上升

Proposition 1 给出合同形式，Corollary 1 进一步说明该合同下卖家的利润如何依赖市场结构。

**推论内容**：卖家的最优利润为：

$$
\Pi^*=[\rho+\lambda(1-\rho)](\theta-c).
$$

该利润随 $\rho$ 和 $\lambda$ 增加而增加。两类消费者均获得零效用。

> **Economic Intuition**：$\rho+\lambda(1-\rho)$ 是最终得到 fit 产品并保留产品的消费者比例。informed consumers 一定 fit，因此贡献 $\rho$；uninformed consumers 以概率 $\lambda$ fit，因此贡献 $\lambda(1-\rho)$。只有 fit 并保留的消费者给卖家带来 $\theta-c$ 的净利润；misfit 的 uninformed consumers 退货，卖家利润为 0。市场中老顾客越多，或新顾客买到合适产品的概率越高，退货越少，利润越高。

### 为什么“菜单”很重要，尽管结果是统一合同？

表面上看，最优结果只是一个统一合同，似乎不需要机制设计。但本文强调，菜单框架是必要的，因为它证明了统一合同不是随便假设出来的，而是从 IC 中内生产生的。

如果卖家只给 uninformed consumers 一个低退款合同，必须降低售价来补偿 misfit risk；这会吸引 informed consumers 模仿，从而产生信息租金。全额退款使 uninformed consumers 不需要价格折扣，因此 informed consumers 也没有可模仿的便宜合同。换言之，**full refund 消除了通过低价补偿风险的需要，也就消除了 informed consumers 的模仿收益**。

### Extension 1 / Proposition 2：加入 quality risk 后，全额退款不再最优

Proposition 1 建立了纯 misfit risk 下 full refund 的最优性。下一步，文章问：如果 fit 产品本身质量也随机，消费者拿到 fit 产品后也可能觉得质量偏低，结论是否还成立？

假设 fit valuation 随机：

$$
\tilde{\theta}\sim U[\theta-\delta,\theta+\delta],
\qquad
\delta\in(0,\theta).
$$

消费者效用变为：

$$
U_{Ij}=\mathbb{E}_{\tilde{\theta}}\max(\tilde{\theta},b_j)-p_j,
$$

$$
U_{Nj}=\lambda\mathbb{E}_{\tilde{\theta}}\max(\tilde{\theta},b_j)+(1-\lambda)b_j-p_j.
$$

定义 first-best efficient refund：

$$
b^o=\max(\theta-\delta,c).
$$

定义 informed consumer 相对 uninformed consumer 的增量效用：

$$
\Delta(b)=(1-\lambda)\left[\mathbb{E}_{\tilde{\theta}}\max(\tilde{\theta},b)-b\right].
$$

该函数随 $b$ 下降：退款越高，informed consumers 相对于 uninformed consumers 的优势越小。

定义阈值：

$$
\bar{\delta}=\frac{\lambda(1-\rho)(\theta-c)}{\lambda+2\rho-3\lambda\rho},
$$

以及：

$$
\bar{b}=\frac{\rho(1-\lambda)(\theta+\delta)+\lambda c(1-\rho)}{\lambda+\rho-2\lambda\rho}.
$$

**命题内容**：

当 $0<\delta\le\bar{\delta}$ 时，卖家最优地提供统一 partial-refund contract：

$$
p_I^*=p_N^*=\theta-(1-\lambda)\delta,
\qquad
b_I^*=b_N^*=\theta-\delta.
$$

当 $\bar{\delta}<\delta<\theta$ 时，卖家最优地提供差异化 partial-refund menu：

$$
b_I^*=b^o,
\qquad
b_N^*=\bar{b},
$$

$$
p_I^*=b^o+\frac{1}{1-\lambda}\Delta(b^o)-\Delta(\bar{b}),
\qquad
p_N^*=\bar{b}+\frac{\lambda}{1-\lambda}\Delta(\bar{b}).
$$

> **Economic Intuition**：quality risk 会破坏 full refund 的最优性，因为退款额太高时，消费者即使拿到 fit 产品，也可能因为 realized quality 较低而退货。此时退货不再只是筛出 misfit 产品，还会引发 fit-but-low-quality returns。低 quality risk 下，这种问题不严重，卖家用统一 partial refund 就够了：退款额设在最低 fit valuation $\theta-\delta$，避免 fit 产品被退回；售价相应降低，给消费者一个 quality discount。高 quality risk 下，统一合同会迫使卖家给 informed consumers 留下太多租金，于是差异化菜单变得必要。

**高 quality risk 下的关键机制**：

卖家给 informed consumers 一个低价、低退款的 no-frills contract；给 uninformed consumers 一个高价、高退款的 insurance-heavy contract。为了让 informed consumers 不去模仿 uninformed contract，卖家把 $b_N$ 向上扭曲。更高的 $b_N$ 增强了 uninformed contract 的保险属性，也支撑更高售价 $p_N$；但它也会诱导一些 fit 但质量较低的产品被退回，因此牺牲 allocative efficiency。

这就是本文最典型的 screening trade-off：**提高 $b_N$ 可以减少 informed consumers 的信息租金，但会造成更多退货和效率损失。**

### Remark 1：严重 quality risk 下，退货反而可能提高社会剩余

Proposition 2 解释了 second-best 合同。文章还先给出 first-best benchmark：如果卖家能观察消费者类型，最优退款为：

$$
b^o=\max(\theta-\delta,c).
$$

First-best 利润为：

$$
[\rho+\lambda(1-\rho)]\mathbb{E}_{\tilde{\theta}}[(\tilde{\theta}-c)\mathbf{1}\{b^o\le\tilde{\theta}\}].
$$

当 $\delta\le\theta-c$ 时，first-best 利润与 $\delta$ 无关；当 $\delta>\theta-c$ 时，first-best 利润随 $\delta$ 上升。

> **Economic Intuition**：当 quality risk 较低时，只要退款额低于最低 fit valuation，所有 fit 产品都被保留，质量波动不影响总效率。但当 quality risk 很高时，一些 fit 产品的 realized valuation 可能低于成本 $c$。如果这些产品被消费者保留，会产生负社会剩余。此时，适当退款能让这些低质量产品被退回，避免低价值消费，反而提高社会剩余。这里的退货不再只是成本，而是一个 ex-post quality screening mechanism。

论文第 9 页的 Figure 1 展示了这一点：随着 $\delta$ 上升，最优合同从统一 partial refund 转向差异化 partial refund；在 severe quality risk 区间，seller profit 和 social surplus 出现回升。

### Extension 2 / Proposition 3：misfit 产品有确定残余价值时，统一合同仍最优，但可能从 full refund 变为 no refund

Proposition 2 表明，fit valuation 的随机性会引入差异化合同。接下来文章考察另一种现实情形：misfit 产品不是完全没用，而是仍有残余价值 $\theta_L$。

Uninformed consumer 的效用变为：

$$
U_{Nj}=\lambda\max(\theta,b_j)+(1-\lambda)\max(\theta_L,b_j)-p_j.
$$

定义阈值：

$$
\hat{\theta}=\rho\theta+(1-\rho)c.
$$

**命题内容**：

若 $\theta_L\le\hat{\theta}$，卖家可提供统一 full-refund contract：

$$
p_I^*=p_N^*=\theta,
\qquad
b_I^*=b_N^*=\theta.
$$

若 $\hat{\theta}<\theta_L<\theta$，卖家可提供统一 no-refund contract：

$$
p_I^*=p_N^*=\lambda\theta+(1-\lambda)\theta_L,
\qquad
b_I^*=b_N^*=0.
$$

> **Economic Intuition**：当 misfit 产品残值低时，uninformed consumers 很害怕买错，需要强保险，full refund 仍然最优。当 misfit 产品残值高时，买错也不是太糟，消费者可以接受更低售价下的 no-refund contract；卖家也不想为了筛选而诱发退货，因为退回一个仍有较高消费价值的商品会破坏总 surplus。此时卖家用较低售价补偿 uninformed consumers 承担 misfit risk，而不再通过退款提供保险。

这里的一个细节是：当 $c<\theta_L\le\hat{\theta}$ 时，从社会效率看，misfit 产品被退回并不一定好，因为消费者保留它仍有价值。但为了 IC 和剩余提取，卖家仍可能采用 full refund。这说明 full refund 不总是 first-best efficient，却可能是 second-best screening optimal。

### Extension 3 / Proposition 4：misfit 产品残余价值随机时，partial refund 用于组内筛选

上一节的 $\theta_L$ 是确定值。文章进一步问：如果 misfit 后的残余价值本身也随机，是否会像 quality risk 一样产生差异化菜单？答案是：不会，仍然可以用统一合同；但退款水平会变成 partial refund。

假设：

$$
\tilde{\theta}_L\sim U[0,\theta].
$$

Uninformed consumer 的效用为：

$$
U_{Nj}=\lambda\max(\theta,b_j)+(1-\lambda)\mathbb{E}_{\tilde{\theta}_L}\max(\tilde{\theta}_L,b_j)-p_j.
$$

定义阈值：

$$
\hat{\rho}=\frac{\theta-c}{2\theta-c}.
$$

**命题内容**：

若 $\hat{\rho}\le\rho<1$，卖家可提供统一 full-refund contract：

$$
p_I^*=p_N^*=\theta,
\qquad
b_I^*=b_N^*=\theta.
$$

若 $0<\rho<\hat{\rho}$，卖家可提供统一 partial-refund contract：

$$
p_I^*=p_N^*=\frac{\theta(1+\lambda)}{2}+\frac{c^2(1-\lambda)(1-\rho)^2}{2\theta(1-2\rho)^2},
$$

$$
b_I^*=b_N^*=\frac{c(1-\rho)}{1-2\rho}.
$$

> **Economic Intuition**：当 informed consumers 占比较高时，卖家主要目标是从他们身上提取剩余，因此 full refund 仍然有吸引力。当 uninformed consumers 占主导时，退货成本变得更重要，卖家转向 partial refund。partial refund 的作用不是区分 informed 与 uninformed 两类消费者，而是在 uninformed consumers 内部进行 ex-post screening：misfit 后残余价值低的人退货，残余价值高的人保留产品。

论文第 12 页 Figure 2 进一步画出了这个 extension 中 $p_j^*$ 和 $b_j^*$ 随 $\rho,c,\lambda,\theta$ 的变化。核心模式是：当 $\rho$ 较低时，partial refund 的价格—退款差距较大；当 $\rho$ 上升超过阈值后，卖家回到 full refund。

### Corollary 2：价格—退款差距的比较静态

Proposition 4 给出随机 misfit valuation 下的合同形式，Corollary 2 进一步总结售价与退款额之间 gap 的变化。

**推论内容**：$p^*-b^*$ 的差距随 $\rho$ 和 $c$ 上升而下降，随 $\lambda$ 和 $\theta$ 上升而上升；其中 $\lambda$ 的影响在 $\rho$ 较低时更明显。

> **Economic Intuition**：当 informed consumers 更多时，卖家更愿意采用高退款来维持高售价和剩余提取，因此 gap 缩小。当成本 $c$ 更高时，卖家利润空间更薄，也需要通过更高退款保障消费者参与，gap 缩小。相反，当 fit 概率 $\lambda$ 更高时，uninformed consumers 的预期价值提高，卖家可以提高售价而不必同步提高退款，gap 扩大。产品价值 $\theta$ 更高时，misfit 残余价值分布更分散，partial refund 更有筛选价值，因此 gap 也扩大。

### Extension 4：salvage value 与 handling cost 不改变纯 misfit risk 下的合同结构

前面主模型假设退回商品可完全再售，且没有 handling cost。文章放松该假设，让退回商品残值为 $s$，或者每次退货给卖家带来处理成本 $k$。

若引入 salvage value，卖家每次退货的增量成本从 $b-c$ 变为 $b-s$。若引入 handling cost，退货成本可写为 $b-c+k$。

> **Economic Intuition**：这些 seller-side costs 会改变利润水平，但不会改变消费者效用，也不会改变 IC/IR 结构。消费者是否购买、是否退货，仍由 $p,b,\theta,\lambda$ 决定。因此，在纯 misfit risk 下，full-refund contract 的 screening / insurance 机制依然成立。这一点与 Su (2009) 这类 cost-based return policy 模型不同：本文中退款额不是为了等于 salvage value，而是为了管理 misfit risk 和信息不对称。

这也是本文与传统 cost-recovery 逻辑最重要的差异：**卖方成本影响利润，但不一定决定退款政策的形式；当退货政策承担筛选功能时，消费者侧的信息结构更关键。**

### Extension 5 / Proposition 5：消费者有 hassle cost 时，低成本下“超额退款”，高成本下“不退款”

最后，文章考虑消费者退货需要付出 hassle cost $h>0$，如退货运费、包装、送到退货点的时间成本等。消费者只有在 realized valuation 低于净退款收益 $b-h$ 时才会退货。

定义阈值：

$$
\hat{h}=c+\frac{\rho\theta}{1-\rho}.
$$

**命题内容**：

若 $h\le\hat{h}$，卖家可提供统一 contract：

$$
p_I^*=p_N^*=\theta,
\qquad
b_I^*=b_N^*=\theta+h.
$$

若 $h>\hat{h}$，卖家可提供统一 no-refund contract：

$$
p_I^*=p_N^*=\lambda\theta,
\qquad
b_I^*=b_N^*=0.
$$

> **Economic Intuition**：当 hassle cost 不高时，卖家反而会给出超过售价的退款 $b=\theta+h$，因为只有这样才能让 uninformed consumers 在 misfit 时真正“无痛退货”。这相当于卖家不只退商品价格，还补偿退货麻烦成本。由于售价仍为 $\theta$，卖家仍能提取全部 fit surplus。当 hassle cost 很高时，补偿消费者退货太贵，卖家干脆利用 hassle cost 作为天然退货阻碍，采用 no refund，并用较低售价 $\lambda\theta$ 补偿 uninformed consumers。

这个结果解释了“hassle-free returns”为什么可能是利润最大化策略：它不是单纯服务优化，而是在恢复 full-refund mechanism 的保险功能。

## 比较静态汇总表 (Comparative Statics Summary)

| 参数变化 | 影响的对象 | 结论 | 直觉 |
|:---|:---|:---|:---|
| $\rho\uparrow$ | 主模型利润 $\Pi^*$ | 上升 | informed consumers 一定 fit，退货少，贡献 $\theta-c$ 的比例提高。 |
| $\lambda\uparrow$ | 主模型利润 $\Pi^*$ | 上升 | uninformed consumers 更可能买到 fit 产品，misfit returns 减少。 |
| $\delta\uparrow$，且 $\delta\le\bar{\delta}$ | random fit valuation 下的退款 | 从 full refund 转为统一 partial refund，$b^*=\theta-\delta$ 下降 | quality risk 低时，卖家降低退款以避免 fit 产品被退回，并用降价补偿。 |
| $\delta\uparrow$，且 $\delta>\bar{\delta}$ | 合同菜单 | 从统一合同转向差异化合同 | 高 quality risk 下，统一合同给 informed consumers 留下太多租金，必须用菜单筛选。 |
| $\delta>\theta-c$ | social surplus / seller profit | 可能上升 | refund 筛掉 realized valuation 低于成本的 fit 产品，避免负社会剩余。 |
| $\theta_L\uparrow$ | deterministic misfit valuation 下的退款政策 | 从 full refund 转向 no refund | misfit 产品残值越高，越不值得诱导退货。 |
| $\rho\uparrow$ | Proposition 3 阈值 $\hat{\theta}$ | $\hat{\theta}$ 上升，full-refund 区域扩大 | informed consumers 越多，卖家越重视压低信息租金。 |
| $\rho\uparrow$ | random misfit valuation 下 $p^*-b^*$ | 下降 | informed consumers 多时，卖家更倾向高退款高售价的剩余提取。 |
| $c\uparrow$ | random misfit valuation 下 $p^*-b^*$ | 下降 | 成本越高，利润空间越薄，卖家需要更强参与保障和更高退款。 |
| $\lambda\uparrow$ | random misfit valuation 下 $p^*-b^*$ | 上升，尤其低 $\rho$ 时 | fit 概率高使 uninformed consumers 预期价值更高，卖家可提高售价而不提高退款。 |
| $\theta\uparrow$ | random misfit valuation 下 $p^*-b^*$ | 上升 | 产品价值越高，misfit valuation 分布更宽，partial refund 的组内筛选价值更大。 |
| $h\uparrow$ | hassle cost extension | 低 $h$ 时 overcompensating refund；高 $h$ 时 no refund | 低 hassle 可以补偿以维持 free trial；高 hassle 补偿太贵，卖家利用其抑制退货。 |
| $s$ 或 $k$ 变化 | salvage / handling cost extension | 不改变纯 misfit risk 下的合同结构 | 它们影响卖家利润水平，但不进入消费者 IC/IR。 |

## 主要结论与管理启示 (Main Results & Managerial Insights)

### 与 benchmark / 经典 cost-based 视角的对比

| 维度 | 经典 cost-based return policy 视角 | 本文 product-fit 视角 |
|:---|:---|:---|
| 核心风险 | 消费者 valuation uncertainty；退货造成卖方成本。 | 消费者是否知道产品 fit；新顾客存在 misfit risk。 |
| 退款政策的主要功能 | 控制退货成本、回收 salvage value、调节需求。 | 为 uninformed consumers 提供 misfit insurance，并辅助 screening。 |
| 对 full refund 的典型判断 | 常常过于慷慨，可能不如 partial refund 或 restocking fee。 | 在纯 misfit risk 下可以是最优合同。 |
| 合同菜单是否必要 | 许多文献直接假设单一合同。 | 先允许菜单，再证明在一些情形下菜单内生坍缩为单一合同。 |
| 何时 partial refund 最优 | 退货成本较高、salvage value 较低等。 | quality risk、random misfit valuation、高价值产品或 uninformed-dominant market。 |
| 何时差异化合同最优 | 未必是核心问题。 | 高 quality risk 下，差异化合同用于分离 informed 与 uninformed consumers。 |

### 管理建议

1. **如果退货主要来自尺码、风格、兼容性等 misfit risk，full refund 可能是理性选择**  
   此时退货政策的价值不是“讨好消费者”，而是让消费者敢于购买并在购买后发现 fit。卖家可以通过更高售价提取这种保险带来的价值。

2. **如果产品 fit 后仍存在明显质量波动，应谨慎使用 full refund**  
   Full refund 可能诱发 fit-but-low-quality products 的退货，使退货不再只筛 misfit，而变成筛 quality。此时 partial refund 更稳妥。

3. **高 quality risk 产品可以考虑分层退货合同**  
   例如给熟悉产品的老顾客提供低价低保障选项，给新顾客提供高价高保障选项。关键不是简单区分“好顾客/坏顾客”，而是让不同风险暴露的消费者自我选择。

4. **高残值 misfit 产品不一定需要退款**  
   如果产品即使不完全合适仍有较高使用价值，卖家可以用低价 no-refund policy 代替高退款政策。典型例子包括有轻微瑕疵但功能完整的商品。

5. **退货 hassle cost 不是越高越好**  
   适度降低 hassle cost 并补偿消费者，可能恢复退货政策的保险功能；但当 hassle cost 极高时，卖家可能转而利用其作为自然的退货阻碍，并降低售价补偿消费者。

6. **不要只用退货处理成本决定退款额**  
   Salvage value 和 handling cost 当然影响利润，但如果退货政策还承担筛选和保险功能，仅仅按成本回收逻辑设置退款额可能错失利润。

## 与相关文献的对话 (Dialogue with Literature)

### Su (2009), Manufacturing & Service Operations Management

共同关注点是消费者退货政策如何影响供应链或卖家利润。Su (2009) 的核心逻辑更偏 cost recovery：退货政策需要在刺激需求与控制退货损失之间权衡，refund 往往与 salvage value、return cost 相关。本文的区别在于把消费者异质性和 product-fit information 放在中心，说明即使退货有成本，full refund 也可能因 screening / insurance 功能而最优。这个区别重要，因为它解释了为什么现实中许多企业没有像纯成本模型预测的那样设置高 restocking fee。

### Shulman, Coughlan and Savaskan (2009), Manufacturing & Service Operations Management

Shulman et al. 研究 restocking fee 与 information provision，强调部分退款可以管理 valuation uncertainty 和 return costs。本文与其共同关注“为什么不总是 full refund”，但本文首先说明在纯 misfit risk 下 full refund 可以最优，然后再通过 quality risk 解释 partial refund 的出现。因此本文不是简单反驳 partial refund，而是给出更细的边界条件：partial refund 主要在 fit 后质量波动或残余价值筛选更重要时出现。

### Hsiao and Chen (2012, 2014), Production and Operations Management / Naval Research Logistics

Hsiao and Chen 系列工作强调 return policy 可以作为市场分割工具，例如根据 hassle cost 或 valuation heterogeneity 实现 ex-post differentiation。本文与这一思路接近，也认为退货政策不仅是售后安排，而是筛选机制。但本文的特色是将 ex-ante consumer type information 与 ex-post product fit revelation 结合起来，解释为什么一个表面上非差异化的 uniform full-refund policy 也可能是机制设计的结果。

### Shang et al. (2017b), Journal of Operations Management

Shang et al. 基于 eBay 证据研究消费者对 free product returns 的价值评估，并指出相同产品可能配有不同价格和退货政策。本文提供了一个理论解释：当产品存在不同风险结构或消费者信息差异时，同一产品的不同“价格—退款”组合可以作为自我选择菜单，而不只是平台上的随机定价差异。

## 犀利评论 (Reviewer's Critique)

### 优点

**理论贡献**：本文最强的理论贡献是将 full-refund policy 从“外生宽松服务”重新解释为一个内生 screening / insurance mechanism。它不是只证明某个退款额最优，而是解释为什么允许菜单之后，菜单有时会坍缩成统一合同。

**机制清晰**：模型把售价和退款额的功能分得很清楚：$p$ 提取剩余，$b$ 管理风险。这种分工让主结果非常容易解释，也便于与 cost-based return policy 文献区分。

**实践相关性**：文章直接回应在线零售中最显眼的现象之一：全额退款明明昂贵却很普遍。扩展部分覆盖 full refund、partial refund、no refund、overcompensating refund，能解释多种实际政策。

### 模型限制与可能过强的假设

1. **informed consumers 被假设为一定 fit**  
   现实中的老顾客也可能遇到尺码变化、批次差异或偏好变化。如果 informed consumers 也面临小概率 misfit，退款政策对他们也会有保险价值，可能改变合同分离结构。

2. **消费者类型只有两类，且比例外生**  
   现实中消费者信息水平往往是连续的，而且会随 reviews、recommendation systems、试穿工具等变化。若信息精度可由平台投资内生决定，退货政策和信息披露会相互作用。

3. **主模型把 fit valuation 设为共同确定值**  
   这有助于突出 misfit risk，但也使 full refund 结论更干净。文章虽在 extension 中加入 quality risk，但仍采用均匀分布和较简化结构，现实产品质量分布可能厚尾或多峰。

4. **卖家是垄断者**  
   在竞争市场中，卖家可能用 free return 抢夺需求，即使单个卖家从 screening 角度不想这么做，也可能被竞争压力推向宽松政策。竞争会改变售价提取剩余的能力。

5. **没有考虑策略性退货和欺诈**  
   Wardrobing、fake returns、套利型退货在现实中非常重要。若消费者会战略性利用 full refund，主模型中 $b\le\theta$ 防套利的逻辑可能不足。

6. **退货对库存、交付和逆向物流的动态影响被简化**  
   模型把退货看作单期利润项，但现实中退货会影响库存可得性、补货周期、二次销售折价和平台声誉。

### 未来研究方向

1. **竞争性退货政策设计**  
   在多个卖家竞争时，full refund 可能既是 screening tool，也是竞争工具。可以研究退货政策如何与价格竞争、质量竞争、平台排序共同作用。

2. **动态学习与重复购买**  
   Uninformed consumers 购买一次后可能变成 informed consumers。动态模型可以解释为什么卖家在新顾客获客阶段提供更宽松退货，而对老顾客采用不同策略。

3. **信息披露与退货政策的联合设计**  
   平台可以通过 reviews、尺码推荐、AR try-on、详细描述降低 misfit risk。一个自然问题是：卖家应投资信息披露，还是依赖 full refund 让消费者 ex post 学习？

4. **策略性退货、欺诈与审核机制**  
   将 wardrobing、fake returns、instant return credit 等行为纳入模型，可以解释为什么一些企业在保持宽松退货的同时引入消费者画像、退货频率限制或差异化审核。

5. **结构估计或实证检验**  
   可以用平台数据估计 $\rho,\lambda,\delta,\theta_L,h$ 等参数，并检验不同品类的最优退货政策是否符合模型预测。例如服装类可能更接近 pure misfit risk，电子产品可能更接近 quality risk。

6. **个性化退货政策与公平/监管问题**  
   如果平台能识别消费者类型，理论上可以对不同消费者提供不同退货条款。但这会引发公平性、透明度和消费者保护问题，值得进一步研究。

## 一句话复盘

这篇文章的核心不是“全额退款一定好”，而是更精确地说：**当消费者主要担心产品不合适、且 fit 后价值稳定时，全额退款是把 misfit risk 转化为可购买保险的最优合同；当风险从 misfit 转向 quality fluctuation 或 high residual-value screening 时，partial refund 和差异化合同才开始变得必要。**

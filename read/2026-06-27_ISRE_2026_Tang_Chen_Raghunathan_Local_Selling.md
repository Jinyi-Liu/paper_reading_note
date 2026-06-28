# 2026-06-27 Buy Online, Pick Up, or Deliver from Store: Why Would an Online Retail Platform with Third-Party Sellers Offer It?

作者：Ping Tang（Bentley University）、Jianqing Chen（University of Texas at Dallas）、Srinivasan Raghunathan（University of Texas at Dallas）  
期刊：Information Systems Research，Articles in Advance  
年份：2026  
DOI：10.1287/isre.2025.1869  
论文类型：analytical model / game-theoretic model  
关键词：omnichannel、BOPS、local selling、digital platforms、third-party sellers、spatial differentiation、platform commission

## 中文摘要

本文研究一个看似反常的平台策略：在线零售平台已经有自己的 fulfillment infrastructure，并且可以通过履约服务向第三方卖家收费，为什么还要允许消费者在平台下单后，到第三方卖家的线下门店自提，或者由第三方卖家本地配送？这类做法在文中称为 local selling，对应 Amazon Local Selling 一类平台型 BOPS / local delivery 项目。

文章建立一个博弈模型：两个第三方卖家在同一平台上竞争，同时各自有线下门店；消费者既有 seller preference 异质性，也有地理位置异质性。传统在线销售中，平台统一履约，消费者位置差异被“遮蔽”；local selling 下，消费者可以根据自己离门店的距离选择自提或配送，位置差异被部分或完全揭示。核心结果是：平台虽然损失 fulfillment profit，但在一些条件下会因卖家价格竞争被缓和、商品价格提高、sales commission 增加而获利。卖家总是从 local selling 中受益，但消费者即使获得更多履约选择，也不一定受益；local selling 可能成为平台和卖家共同抽取消费者剩余的机制。

## 论文速览

| 维度 | 内容 |
|:---|:---|
| 核心问题 | 为什么一个有自有履约能力、并能从 fulfillment fee 中获利的平台，会主动把履约交给第三方卖家的线下门店？ |
| 实践背景 | Amazon Local Selling：消费者在 Amazon 下单后，可以到第三方本地门店自提，或由该本地卖家配送。 |
| 方法 | 两卖家、二维 Hotelling-style spatial model；消费者异质性包含地理位置 $x$ 和 seller preference $y$；三阶段博弈。 |
| Benchmark | Traditional online selling：平台统一履约，卖家支付 sales commission $\rho$ 和 fulfillment fee $f$。 |
| Main model | Local selling：平台不履约；消费者可选择 in-store pickup 或 seller delivery；卖家承担本地配送成本 $f_l$，并从到店消费者获得额外收益 $\mu$。 |
| 核心机制 | Local selling “unmasks” consumer location heterogeneity，使卖家能够利用地理差异缓和价格竞争；同时可能改变卖家的边际履约成本。 |
| 关键区分 | Preference-dominates-location：消费者偏好主导，位置只影响履约方式；Location-dominates-preference：地理位置也影响买哪家，价格竞争真正被缓和。 |
| 主要结论 | 平台在一些条件下会因 commission revenue 增加而选择 local selling；卖家总是受益；消费者不一定受益。 |
| 管理含义 | Local selling 不只是服务提升，而是 platform competition management / surplus extraction 工具；平台应按产品品类和市场地理特征选择性开放。 |
| 对 OM / MKT 的价值 | 将 omnichannel fulfillment、platform business model 与 horizontal differentiation 机制连接起来，解释平台型 BOPS 与传统 retailer BOPS 的差异。 |

## TL;DR

这篇文章的核心发现是：平台让第三方卖家做自提和本地配送，并不一定是为了“方便消费者”，也不一定只是为了“帮卖家引流”。它可以通过暴露消费者的地理位置差异，让卖家之间的价格竞争变弱，从而提高商品价格和平台 commission revenue，弥补甚至超过平台放弃 fulfillment profit 的损失。

最值得注意的是，消费者虽然多了一个自提选项，但不一定更好；local selling 可能让平台和卖家一起受益，而消费者因价格上升而受损。

## One More Thing：这篇文章最有意思的洞察

Local selling 最精妙的地方在于，它把一个“履约选项”变成了一个“筛选机制”。传统在线销售把所有消费者都包装成一样的人：无论住在卖家门口还是很远，大家都等平台统一配送，所以卖家只能基于品牌 / seller preference 竞争。Local selling 一旦出现，消费者是否愿意自提就泄露了她与门店的距离；离 A 店近的人更可能选择 A 的自提，离 B 店近的人更可能选择 B 的自提，离两家都远的人才等配送。这个自选择过程让卖家知道自己对某些消费者有地理优势，于是没有必要像纯线上那样激烈降价抢人。

换句话说，platform local selling 的本质不只是 BOPS，也不是简单的 last-mile outsourcing，而是把原本被平台标准化履约“抹平”的 local differentiation 重新引入竞争结构。平台放弃 fulfillment fee，却可能通过更高价格上的 commission 把钱赚回来。

## 1. 研究背景与动机

### 1.1 实践痛点

传统 BOPS 文献多研究一个 retailer 同时经营 online channel 和 offline stores 时，是否应允许消费者线上购买、线下自提。本文的现象不同：平台本身并不拥有这些线下门店，而是让 third-party sellers 的门店承担履约功能。Amazon 在 2021 年推出 Local Selling，允许第三方卖家让本地消费者在 Amazon 下单后自提或由卖家本地配送。直观上，这对消费者和卖家都有好处：消费者有履约灵活性，卖家有门店客流和潜在附加销售。

但平台的动机不明显。以 Amazon 为例，平台已经投入大量 fulfillment infrastructure，并可通过 FBA、Buy with Prime 等方式货币化物流能力。如果 local selling 让卖家自行履约，平台就放弃了 fulfillment fee 和相关利润。更难解释的是，文章关注的是已经在平台上的卖家，而不是通过 local selling 吸引新卖家的情形。因此，真正的 puzzle 是：如果不扩大 seller base，平台为什么还愿意这么做？

### 1.2 理论缺口

现有 omnichannel / BOPS 文献主要关注 retailer 自己整合线上线下渠道，例如线上购买、门店自提如何影响库存、价格、门店流量和渠道替代。本文把视角换成平台：平台是交易前端和规则制定者，线下门店属于第三方卖家。平台的收益来自 sales commission 和 fulfillment profit，而不是传统 retailer 的零售毛利。

现有 platform literature 关注第三方卖家、FBA、agency vs wholesale、平台开放等问题，但较少讨论平台如何利用第三方卖家的线下资产来改变卖家竞争。本文的贡献在于说明：平台不只是把 offline stores 当作履约节点，还可以把它们当作一种 product / location differentiation 的揭示装置。

### 1.3 核心贡献

第一，本文解释了平台型 local selling 的利润动机：平台可能牺牲 fulfillment profit，但通过卖家价格上涨获得更多 commission。

第二，本文区分两类 location revealing：当 seller preference 主导时，位置只影响消费者选择 pickup 还是 delivery；当 location 主导时，位置还影响消费者买哪个卖家，从而真正缓和 seller price competition。

第三，本文给出福利结果：卖家总是受益，平台在一些条件下受益，消费者不一定受益。这个结论对平台监管很重要，因为“增加选择”并不等价于“增加消费者剩余”。

第四，本文把 omnichannel、platform business model 和 Hotelling differentiation 连接起来，提供了一个适合 OM / Marketing / IS 交叉领域的机制型理论贡献。

## 2. 模型设定与假设

### 2.1 Players and sequence of events

Players 包括一个在线平台 $P$、两个第三方卖家 $A$ 和 $B$、以及一组 unit-demand consumers。两个卖家都在平台上销售同类产品，同时各自拥有线下门店。

博弈时序如下：

1. 平台决定是否采用 local selling。
2. 两个卖家同时定价 $p_A$ 和 $p_B$。
3. 消费者做购买决策。传统在线销售中，消费者只选择买哪家；local selling 中，消费者还要选择 fulfillment method：seller delivery 或 in-store pickup。

均衡概念是 subgame-perfect equilibrium，使用 backward induction 求解。

### 2.2 消费者空间与偏好

消费者均匀分布在单位正方形 $[0,1]^2$ 上。每个消费者由 $(x,y)$ 表示：

| 符号 | 含义 | 直觉 |
|:---|:---|:---|
| $x \in [0,1]$ | 消费者地理位置 | 越接近 0 越靠近卖家 A 的线下店，越接近 1 越靠近卖家 B 的线下店。 |
| $y \in [0,1]$ | 消费者 seller preference | 越接近 0 越偏好 A，越接近 1 越偏好 B。 |
| $a$ | unit misfit cost | 衡量 seller preference 的强度；$a$ 越大，消费者越不愿意买不匹配的卖家。 |
| $t$ | unit transportation cost | 衡量地理位置差异的重要性；$t$ 越大，去远店自提越不划算。 |
| $w$ | delivery waiting cost | 等待配送带来的效用损失。 |
| $v$ | ideal product maximum value | 假设足够大以保证 full market coverage。 |

卖家 A 位于 $(0,0)$，卖家 B 位于 $(1,1)$。这里的二维并不是两个真实地理维度，而是一个空间化建模技巧：$x$ 表示地理距离，$y$ 表示偏好距离。

### 2.3 消费者效用

Local selling 下，消费者从卖家 $i \in \{A,B\}$ 购买，并选择 fulfillment method $j \in \{s,o\}$，其中 $s$ 表示 store pickup，$o$ 表示 delivery。效用为：

$$
\begin{aligned}
U_{As} &= v - ay - tx - p_A,\\
U_{Ao} &= v - ay - w - p_A,\\
U_{Bs} &= v - a(1-y) - t(1-x) - p_B,\\
U_{Bo} &= v - a(1-y) - w - p_B.
\end{aligned}
$$

> 直觉：消费者效用 = 基础价值 $v$ − seller preference misfit − 价格 − 履约成本。自提时履约成本是交通成本，例如买 A 自提要付出 $tx$；配送时履约成本是等待成本 $w$。传统在线销售可以看作只有 $U_{Ao}$ 和 $U_{Bo}$ 两个选项，因为平台统一配送。

### 2.4 平台和卖家的收益结构

#### 传统在线销售

传统在线销售中，平台负责配送。卖家向平台支付 sales commission rate $\rho$ 和每单位 fulfillment fee $f$；平台每单位履约成本为 $c$，其中 $0<c<f$。

卖家利润为：

$$
\pi_A^t = (1-\rho)p_A D_A - fD_A, \qquad
\pi_B^t = (1-\rho)p_B D_B - fD_B.
$$

平台利润为：

$$
\pi_P^t = \rho(p_A D_A + p_B D_B) + (f-c)(D_A+D_B).
$$

> 直觉：卖家的每单位收入是扣除平台佣金后的 $(1-\rho)p_i$，同时每卖出一件要向平台支付履约费 $f$。平台赚两部分钱：交易佣金和 fulfillment margin $f-c$。

#### Local selling

Local selling 中，平台不再履约，只收 sales commission。消费者如果选择 delivery，由卖家本地配送，卖家承担每单位成本 $f_l$；如果选择 pickup，卖家不承担配送成本，并获得到店消费者带来的额外收益 $\mu$。

卖家利润为：

$$
\pi_A^l = (1-\rho)p_A(D_{As}+D_{Ao}) + \mu D_{As} - f_l D_{Ao},
$$

$$
\pi_B^l = (1-\rho)p_B(D_{Bs}+D_{Bo}) + \mu D_{Bs} - f_l D_{Bo}.
$$

平台利润为：

$$
\pi_P^l = \rho p_A(D_{As}+D_{Ao}) + \rho p_B(D_{Bs}+D_{Bo}).
$$

> 直觉：平台不再赚履约费，因此 local selling 是否值得做，完全取决于 commission revenue 能否增加。卖家面对两个消费者分段：自提消费者带来 $\mu$ 且无配送成本，配送消费者需要卖家付出 $f_l$。

### 2.5 关键假设与作用

| 假设 | 内容 | 为什么合理 | 放松后可能怎样 |
|:---|:---|:---|:---|
| Full market coverage | $v$ 足够大，所有消费者都会购买 | 聚焦 seller choice 和 fulfillment choice，不让 outside option 干扰机制 | 若有 outside option，local selling 可能扩大市场，也可能因涨价导致需求流失，平台采纳条件会变化。 |
| $t>2w$ | 交通成本足够大，使得 local selling 下同时存在 pickup 和 delivery 消费者 | 避免所有人都自提或所有人都配送的角点情形 | 若 $t$ 很低，自提占比过高；若 $t$ 极高，local selling 几乎退化为卖家配送。 |
| 对称两卖家 | 两个卖家位置、成本、品类对称 | 保持模型可解，并突出 local selling 对竞争结构的影响 | 卖家异质性会产生更复杂的 adoption 和 pricing asymmetry，尤其是强卖家 vs 弱卖家。 |
| $\rho$ 和 $f$ 外生 | 平台 commission 和 fulfillment fee 不随 local selling 调整 | 文章认为这些是长期战略变量，受监管、品类和平台竞争影响 | 若内生，平台可通过 fee design 捕获更多 surplus，local selling 的采纳条件和福利结果会更复杂。 |
| Baseline 中两卖家都参与 local selling | 主模型聚焦平台是否开放 local selling | 先研究 symmetric participation 的纯机制 | Extension 允许卖家内生选择是否加入，并发现可能出现两者都加入、都不加入或仅一家加入。 |
| 消费者知道位置与成本 | 消费者理性比较自提和配送 | 标准理论建模假设 | 若存在认知成本、搜索摩擦、或平台默认选项，local selling 还会有 choice architecture 效应。 |

## 3. 分析路线图

文章的分析逻辑很清晰，基本是从 benchmark 到 local selling，再到平台选择和 extensions。

第一步是 traditional online selling benchmark。平台统一配送，所以地理位置 $x$ 不影响消费者选择。两个卖家的竞争只发生在 seller preference 维度 $y$ 上。

第二步是 local selling。消费者多了 pickup / delivery 的履约选择，地理位置 $x$ 开始进入效用。文章区分两种情形：preference dominates location 和 location dominates preference。

第三步是比较 local selling 与 traditional online selling 的均衡价格、平台利润、卖家利润和消费者剩余。关键是判断：平台放弃 fulfillment margin 后，是否能从更高价格带来的 commission 中赚回来。

第四步是 extensions：加入 offline consumers、允许卖家内生加入 local selling、允许地理位置和 seller preference 正相关、以及 local consumers 与 national consumers 共存。总体结论保持稳健。

## 4. Benchmark：Traditional Online Selling

传统在线销售中，所有消费者都由平台统一配送。消费者无论住在哪里，等待成本都是同一个 $w$，因此地理位置 $x$ 不影响 seller choice。

消费者在买 A 和买 B 之间的无差异线为：

$$
y_{AB}=\frac{a-p_A+p_B}{2a}.
$$

需求为 $D_A=y_{AB}$，$D_B=1-y_{AB}$。求解卖家同时定价问题，得到：

$$
p_A^t=p_B^t=a+\frac{f}{1-\rho}, \qquad D_A^t=D_B^t=\frac{1}{2},
$$

$$
\pi_A^t=\pi_B^t=\frac{a(1-\rho)}{2}, \qquad
\pi_P^t=\rho\left(a+\frac{f}{1-\rho}\right)+f-c.
$$

> 经济直觉：传统在线销售把所有消费者的地理差异抹平了。卖家只在 seller preference 维度竞争，所以价格由偏好强度 $a$ 和卖家面对的平台履约费 $f$ 决定。$f$ 是卖家的边际成本，会推高价格；平台则同时赚 commission 和 fulfillment margin。

这个 benchmark 是全文的关键参照系。local selling 是否有价值，取决于它能否打破“地理位置被遮蔽”的竞争结构。

## 5. Local Selling：两种 location revealing 机制

### 5.1 Preference-dominates-location：位置只影响履约方式

当 $a>w$ 时，消费者 seller preference 足够强。一个更偏好 A 的消费者，即便离 A 店较远，也倾向于买 A；她只是会在 A 的 pickup 和 A 的 delivery 之间做选择。此时地理位置影响 fulfillment choice，但不影响 seller choice。

均衡价格为：

$$
p_A^l=p_B^l=a+\frac{f_l(t-w)-w\mu}{t(1-\rho)}.
$$

卖家利润和平台利润为：

$$
\pi_A^l=\pi_B^l=\frac{a(1-\rho)}{2}+\frac{w^2(f_l+\mu)}{4at},
$$

$$
\pi_P^l=\rho\left(a+\frac{f_l(t-w)-w\mu}{t(1-\rho)}\right).
$$

> 经济直觉：在这一情形下，local selling 是 “partially location revealing”。消费者位置确实影响她选择自提还是配送，但不改变她买 A 还是 B。因此，位置没有进入卖家的总需求弹性，也不会直接缓和价格竞争。local selling 对价格的影响主要来自 supply-side：配送消费者让卖家承担 $f_l$，自提消费者给卖家带来 $\mu$。

### 5.2 Location-dominates-preference：位置也影响买哪家

当 $a<w$ 时，seller preference 较弱，消费者更在意履约相关成本。一个原本略偏好 B 的消费者，如果住在 A 店附近，可能会因为 A 的自提成本低而买 A。此时地理位置不仅影响 pickup / delivery，还影响 seller choice。

均衡价格为：

$$
p_A^l=p_B^l=\frac{f_l(t-2w+a)+at(1-\rho)-a\mu}{(t-2w+2a)(1-\rho)}.
$$

> 经济直觉：这是 “fully location revealing”。local selling 让卖家在某些本地消费者面前拥有 locational advantage，因此降价抢对方消费者的效率下降。换句话说，需求对价格的敏感度下降，price competition 被缓和。这个 demand-side effect 是本文最核心、也最有理论新意的机制。

在 Figure 2 的市场分割图中，preference-dominates-location 的分割更多体现为同一卖家内部 pickup 与 delivery 的分割；location-dominates-preference 中，地理位置还改变了 A 与 B 的市场边界。前者是履约选择被 location 影响，后者是购买对象本身被 location 影响。

## 6. 核心命题与机制

### Proposition 1：Local selling 何时让卖家涨价？

在 preference-dominates-location 情形下，local selling 下卖家价格高于 traditional online selling，当且仅当：

$$
f_l\left(1-\frac{w}{t}\right)-\mu\frac{w}{t}>f.
$$

在 location-dominates-preference 情形下，卖家价格高于 traditional online selling，当且仅当：

$$
f_l\left(1-\frac{a}{t-2w+2a}\right)-\mu\frac{a}{t-2w+2a}
+\frac{2a(1-\rho)(w-a)}{t-2w+2a}>f.
$$

> 经济直觉：traditional online selling 下，卖家的履约边际成本是付给平台的 $f$。local selling 下，配送消费者带来本地配送成本 $f_l$，自提消费者带来额外线下收益 $\mu$。在 preference-dominates-location 情形下，价格是否上涨只取决于这两个 supply-side forces 的加权平均是否超过 $f$。在 location-dominates-preference 情形下，额外出现了第三项 $\frac{2a(1-\rho)(w-a)}{t-2w+2a}$，这就是 local selling 缓和价格竞争的 demand-side effect。因为此时 $w>a$，该项为正，会推动价格上升。

这个命题建立了全文最重要的中间结果：平台并不需要直接从履约中赚钱，只要 local selling 能让卖家价格上涨，平台就可能通过 commission 获利。

### Proposition 2：平台何时选择 local selling？

在 preference-dominates-location 情形下，平台 local selling 利润高于 traditional online selling，当且仅当：

$$
\frac{\rho}{1-\rho}\left[f_l\left(1-\frac{w}{t}\right)-\mu\frac{w}{t}\right]>
\frac{f}{1-\rho}-c.
$$

在 location-dominates-preference 情形下，平台 local selling 利润高于 traditional online selling，当且仅当：

$$
\frac{\rho}{1-\rho}\left[
 f_l\left(1-\frac{a}{t-2w+2a}\right)-\mu\frac{a}{t-2w+2a}
 +\frac{2a(1-\rho)(w-a)}{t-2w+2a}
 \right]>
\frac{f}{1-\rho}-c.
$$

> 经济直觉：左边是 local selling 通过更高商品价格带来的 commission gain，右边是平台放弃的 fulfillment-related rent。右边不只是 $f-c$，还包括 traditional online selling 中 $f$ 被卖家转嫁到价格后对 commission 的贡献，因此是 $\frac{f}{1-\rho}-c$。平台是否做 local selling，本质上是在比较“更高价格上的佣金”与“放弃履约利润”。

这里有一个很反直觉的点：卖家从到店消费者获得的额外收益 $\mu$ 越高，平台越不倾向于 local selling。因为 $\mu$ 使卖家更愿意降价吸引消费者到店，从而压低平台 commission base。Amazon 在营销中强调 local selling 能给卖家带来 foot traffic，但从平台利润角度，这个好处并不直接帮助平台。

### Proposition 3：local selling 价值的比较静态

定义平台的 local selling value：

$$
V_P = \pi_P^l - \pi_P^t.
$$

在 preference-dominates-location 情形下：

$$
\frac{\partial V_P}{\partial t}>0, \qquad
\frac{\partial V_P}{\partial a}=0, \qquad
\frac{\partial V_P}{\partial w}<0.
$$

在 location-dominates-preference 情形下：

$$
\frac{\partial V_P}{\partial t}>0
\quad \text{iff} \quad
f_l+\mu+2(a-w)(1-\rho)>0,
$$

$$
\frac{\partial V_P}{\partial a}>0
\quad \text{iff} \quad
(t-2w)(f_l+\mu)<2(1-\rho)[w(t-2w)-2a(t+a-2w)],
$$

$$
\frac{\partial V_P}{\partial w}>0
\quad \text{iff} \quad
f_l+\mu<t(1-\rho).
$$

> 经济直觉：当 preference dominates location 时，$t$ 只影响有多少人自提。$t$ 越高，自提越少，卖家承担更多本地配送成本 $f_l$、失去更多 $\mu$，于是更可能涨价，平台 commission 增加。$a$ 同时影响 traditional 和 local 下的偏好竞争，但不改变 local selling 的相对价值。$w$ 越高，自提越多，卖家成本越低、线下收益越高，价格下降，平台反而不喜欢。
>
> 当 location dominates preference 时，$t,a,w$ 都同时影响 fulfillment split 和 seller competition intensity，因此符号不再单调。例如 $t$ 越高，一方面使更多消费者转向 delivery、推高成本；另一方面也可能让卖家为了争夺附近消费者而降价。最终效果取决于参数组合。

这个命题说明平台不能把 local selling 当成“一刀切”的全品类策略；同样的交通成本、等待成本或偏好强度，在不同品类和市场结构下可能产生相反的利润效果。

### Proposition 4：卖家总是受益，消费者不一定受益

文章证明，local selling 总是提高卖家利润，但消费者剩余的变化不确定。消费者更可能从 local selling 中受益的条件包括：平台传统 fulfillment fee $f$ 较高、卖家本地配送成本 $f_l$ 较低、平台佣金率 $\rho$ 较低、以及到店额外收益 $\mu$ 较高。

> 经济直觉：卖家的收益来源有三部分：第一，自提消费者带来额外线下收益 $\mu$；第二，自提消费者节省 fulfillment cost；第三，在 location-dominates-preference 中，价格竞争可能被缓和。消费者虽然获得了更灵活的履约选择，但如果这种选择导致卖家涨价，履约节省可能被价格上升抵消，甚至消费者剩余下降。

这是本文的 welfare punchline：更多 fulfillment options 不代表消费者更好。平台创新如果改变了竞争强度和剩余分配，监管者不能只看“选择是否增加”。

## 7. 关键 trade-off

全文最核心的 trade-off 可以写成一句话：

**平台采用 local selling 的收益 = 更高 seller prices 带来的额外 commission；平台采用 local selling 的成本 = 放弃 fulfillment fee 和 fulfillment margin。**

更具体地说，local selling 提高价格有两条路径：

1. **Supply-side effect**：seller delivery 成本 $f_l$ 可能高于传统平台履约费 $f$；自提消费者虽然节省配送成本，但也带来 $\mu$，会反向压低价格。
2. **Demand-side effect**：当地理位置影响 seller choice 时，卖家有 local captive consumers，降价抢客效率下降，价格竞争缓和。

Supply-side effect 在两种情形下都存在；demand-side effect 只在 location-dominates-preference 情形下真正发挥作用。

## 8. 比较静态汇总表

| 参数变化 | Preference-dominates-location 中对 $V_P$ 的影响 | Location-dominates-preference 中对 $V_P$ 的影响 | 直觉 |
|:---|:---|:---|:---|
| $t \uparrow$ | $V_P \uparrow$ | 不确定；若 $f_l+\mu+2(a-w)(1-\rho)>0$ 则 $V_P \uparrow$ | 交通成本高使自提减少、卖家成本上升，但在 location-dominates-preference 中也会改变卖家争夺附近消费者的激励。 |
| $a \uparrow$ | 无影响 | 不确定 | PDL 中 $a$ 对 traditional 和 local 的相对影响抵消；LDP 中 $a$ 同时影响偏好竞争和位置揭示。 |
| $w \uparrow$ | $V_P \downarrow$ | 不确定；若 $f_l+\mu<t(1-\rho)$ 则 $V_P \uparrow$ | 等待成本高会让更多消费者自提，降低卖家配送成本并增加 $\mu$，但也可能强化位置在竞争中的作用。 |
| $f_l \uparrow$ | 更利于 local selling | 更利于 local selling | 卖家本地配送成本越高，local selling 下价格越容易上涨，平台 commission base 增加。 |
| $\mu \uparrow$ | 不利于平台 local selling，但利于卖家和消费者 | 不利于平台 local selling 的直接供给侧项，但可能与竞争效应交互 | 到店额外收益使卖家愿意降价吸引自提，压低平台 commission。 |
| $f \uparrow$ | 不利于 local selling | 不利于 local selling | 平台传统履约越赚钱，放弃 fulfillment 越痛；同时 $f$ 在传统模式中也推高价格并增加 commission。 |
| $c \uparrow$ | 利于 local selling | 利于 local selling | 平台履约成本越高，传统 fulfillment margin 越低，放弃履约的机会成本下降。 |
| $\rho \uparrow$ | 通常强化平台从高价格中获益，但也改变条件阈值 | 同左，且影响 demand-side term | 平台佣金率高时，更愿意通过高价格赚 commission，但佣金也改变卖家定价激励。 |

## 9. Extensions：稳健性与补充机制

### 9.1 Online and offline consumers coexist

扩展模型允许市场上同时存在 online consumers 和 offline consumers。传统在线销售下，online consumers 在平台买，offline consumers 在线下店买；local selling 可能让一部分线下消费者转到平台，也可能让一部分线上消费者意识到门店存在而直接线下购买。

核心发现：主模型机制保持。平台仍可能因 local selling 缓和价格竞争而受益；并且如果 local selling 能提高平台上的 online consumer share，平台更有动力采用 local selling。

> 对 OM / MKT 的含义：这个扩展把 local selling 连接到 channel migration。local selling 不只是同一批线上消费者的履约方式变化，也可能改变消费者进入哪个 channel。

### 9.2 Sellers endogenously decide whether to join local selling

主模型假设两个卖家都参与 local selling。扩展中，卖家可自行选择是否加入。文章在 preference-dominates-location 情形下得到一个非单调结果：当 $f_l$ 较低时，两家都加入；当 $f_l$ 处于中间区间时，两家都不加入；当 $f_l$ 很高时，可能只有一家加入。

> 直觉：低本地配送成本使 local selling 对所有卖家有利。中等配送成本时，参与不够划算。但当配送成本很高时，加入 local selling 的卖家会因高成本设高价，反而使竞争对手也可以跟着涨价；非参与卖家从 softened competition 中受益，因此 asymmetric participation 可以成为均衡。

这个结果解释了一个实践现象：即使平台免费开放 local selling，也不是所有卖家都会参加。

### 9.3 Correlation between location and seller preference

主模型假设地理位置 $x$ 和 seller preference $y$ 独立。扩展允许两者正相关，用 $\beta$ 表示相关程度。$\beta=0$ 是主模型，$\beta=1$ 表示位置和偏好完全一致。

核心发现：主结论稳健。更强的相关性会改变 location revealing 的强度。在 preference-dominates-location 情形下，$\beta$ 越高，位置和偏好越一致，卖家价格和平台利润越高；在 location-dominates-preference 情形下，影响取决于 $f_l+\mu$ 与 $2(1-\rho)(w-a)$ 的比较。

### 9.4 Hybrid model：local consumers 与 national consumers 共存

扩展模型允许平台同时服务 local consumers 和 national consumers。Local consumers 可以使用 local selling；national consumers 离卖家线下店很远，只能由平台传统履约。

核心发现：主结论仍然稳健。随着 national consumers 占比 $\theta$ 增加，交通成本 $t$ 对整体均衡的影响减弱，因为更大比例消费者不参与本地自提或本地配送。卖家在 local selling 下是否涨价的条件与主模型一致。

## 10. 主要结论与管理启示

### 10.1 与 benchmark 的对比

| 维度 | Traditional online selling | Local selling: preference dominates location | Local selling: location dominates preference |
|:---|:---|:---|:---|
| Fulfillment | 平台统一履约 | 卖家配送或消费者自提 | 卖家配送或消费者自提 |
| Location heterogeneity | 被遮蔽 | 部分揭示：只影响履约方式 | 完全揭示：影响履约方式和 seller choice |
| 价格竞争由什么决定 | Seller preference $a$ | 主要仍由 $a$ 决定 | 由 $a$ 和 location differentiation $t$ 共同决定 |
| 平台收入来源 | Commission + fulfillment margin | Commission only | Commission only |
| 平台为什么可能更赚钱 | 不适用 | 卖家本地履约成本推高价格 | 本地履约成本 + 价格竞争缓和推高价格 |
| 消费者福利 | 基准 | 可能提高，也可能下降 | 更可能因价格竞争缓和而受损 |

### 10.2 对平台的建议

平台不应把 local selling 作为统一开放的服务功能，而应按品类和地理市场筛选。对 standard / commodity products，消费者 seller preference 较弱，location 更可能主导购买，local selling 更容易产生 full location revealing 和 softened price competition。对 nonstandard / highly differentiated products，location 主要影响 pickup vs delivery，不一定改变 seller competition。

平台还应关注本地配送成本 $f_l$ 和等待成本 $w$。如果卖家本地配送成本高，local selling 更可能推高价格和 commission；如果等待成本高，更多消费者自提，卖家成本下降并获得 $\mu$，平台 commission 反而可能下降。

平台对卖家宣传 local selling 时可以强调 foot traffic，但从平台自身利润看，foot traffic benefit $\mu$ 并非总是好事。它可能诱导卖家降价吸引到店消费者，降低平台 commission revenue。

### 10.3 对卖家的建议

卖家一般应认真考虑 local selling，因为模型中卖家总是受益。收益来源不是单一的：既有自提带来的额外到店销售，也有自提节省的履约成本，还有竞争缓和带来的价格提升。

但卖家是否加入并不必然单调取决于本地配送成本。扩展模型显示，中等 $f_l$ 时可能无人加入，高 $f_l$ 时反而可能出现单方加入。现实中，这意味着卖家要考虑竞争对手是否加入，而不是只计算自己的配送成本。

### 10.4 对监管者的启示

Local selling 增加了消费者可选履约方式，但不保证消费者福利提高。平台可能通过这个机制更有效地 segment consumers、soften seller competition、extract surplus。因此，对平台实践的评估不能只看“消费者选择是否变多”，还要看价格、竞争强度和剩余分配如何变化。

### 10.5 可检验的 empirical implications

如果将来做实证或结构估计，可以从本文推出若干可检验预测：

1. Local selling 推出后，参与卖家的线上价格可能上升，尤其是在 commodity categories 或 location-dominates-preference 的市场中。
2. 价格上涨幅度应随卖家本地配送成本 $f_l$ 增加而增加，随到店额外收益 $\mu$ 增加而降低。
3. 对 nonstandard products，local selling 对价格竞争的影响较弱，更多体现在 pickup / delivery split 和履约成本变化上。
4. 消费者 welfare 不一定上升；若能观察到价格、配送时间、自提比例和复购，应检验履约便利是否被价格上涨抵消。
5. 卖家参与 local selling 的模式可能与配送成本非单调相关，存在 both join / neither join / one joins 的区域。

## 11. 与相关文献的对话

| 文献 | 共同关注点 | 本文推进之处 | 为什么重要 |
|:---|:---|:---|:---|
| Gao and Su (2017), Management Science | BOPS、线上线下渠道整合、消费者自提 | Gao and Su 研究 retailer 自有线上线下渠道；本文研究 platform 使用 third-party sellers 的线下门店。 | 平台不拥有门店，也不赚传统零售毛利，收益逻辑转为 commission vs fulfillment profit。 |
| Gallino and Moreno (2014), Management Science | BOPS / offline traffic 对零售绩效的影响 | 该文强调门店流量与库存信息等运营效果；本文强调 local selling 通过揭示 location differentiation 改变价格竞争。 | 从 operational service effect 转向 strategic competition effect。 |
| Lai et al. (2022), MSOM / Sun et al. (2020), Naval Research Logistics | Fulfillment by Amazon、平台履约服务、第三方卖家 | 既有研究多分析平台提供履约服务的价值；本文问平台为什么反而放弃履约。 | 解释平台 fulfillment strategy 的反向选择：有时 outsourcing fulfillment to sellers 能提高 commission。 |
| Hotelling (1931) 与 d’Aspremont et al. (1979) | 横向差异化缓和价格竞争 | 本文不是让卖家选择位置，而是让平台通过 channel design 揭示已有的位置差异。 | 把经典 product/location differentiation 机制嵌入 platform omnichannel 设计。 |

## 12. Reviewer’s Critique

### 12.1 优点

理论机制清楚。文章抓住了一个真实且不直观的平台现象，并把它还原为 “masked vs revealed location differentiation” 的竞争机制。这比简单说 local selling 降低物流成本或增加门店流量更有理论辨识度。

模型设计有效。二维消费者空间同时承载地理位置和 seller preference，使文章可以区分 partial location revealing 与 full location revealing。这一区分是全文的概念贡献。

管理含义明确。结论能直接指导平台按品类和市场开放 local selling，也能解释为什么消费者选择增加但福利不一定提高。

### 12.2 模型限制与可能影响

第一，平台 commission rate $\rho$ 和 fulfillment fee $f$ 外生。现实中，平台可以调整佣金、履约费、local selling 参与费、配送补贴或搜索排序。如果这些决策内生，平台可能用更精细的 tariff design 捕获 surplus，当前的采纳条件会改变。

第二，模型假设两个卖家对称且只有两个卖家。实际平台中有多卖家、多门店、不同库存能力和不同品牌力。多卖家网络可能改变 local differentiation 的强度，也可能产生更复杂的本地垄断或拥挤效应。

第三，模型没有显式处理库存、门店容量、缺货、拣货成本、服务质量和配送时效差异。BOPS / local delivery 在 OM 中高度依赖这些 operational constraints；若加入容量和库存，local selling 可能既是竞争工具也是 capacity allocation 问题。

第四，消费者完全理性且完全知晓成本。现实中，平台界面默认选项、地图距离展示、Prime 标识、delivery promise、消费者对门店的认知，都可能影响 self-selection。

第五，消费者没有 outside option。若价格因 local selling 上涨，部分消费者可能退出市场或转向其他平台。full coverage 假设可能低估价格上涨对需求规模和消费者福利的负面影响。

第六，文章主要给出理论解释，缺少直接实证验证。Amazon Local Selling 是否真的导致参与品类价格上升、平台 commission 增加、消费者 surplus 下降，还需要数据检验。

### 12.3 未来研究方向

1. **Endogenous platform tariff design**：让平台同时选择 $\rho$、$f$、local selling fee、seller delivery subsidy，研究平台最优合同和卖家参与约束。
2. **Empirical test of location revealing**：利用 Amazon Local Selling 或类似平台项目的 staggered rollout，检验参与卖家价格、销量、自提比例和竞争对手价格的变化。
3. **Inventory and capacity integration**：加入门店库存、拣货容量和配送能力，研究 local selling 在 operational efficiency 与 competition softening 之间的权衡。
4. **Asymmetric sellers and brand power**：允许卖家品牌力、门店密度、配送成本不同，分析强品牌卖家和弱品牌卖家是否对 local selling 有不同激励。
5. **Consumer search and interface design**：研究平台如何通过默认展示 pickup / delivery、距离排序、delivery promise 或 badge 影响消费者自选择。
6. **Regulation and welfare**：将消费者 outside option 和跨平台竞争加入模型，评估 local selling 是否构成通过 channel design 缓和竞争的隐性手段。

## 13. 给 OM / Marketing PhD scholar 的 seminar 读法

读这篇文章时，最好不要被公式细节牵着走，而是抓住三层逻辑。

第一层是 benchmark：平台统一履约为什么会 mask location？因为所有人面对相同等待成本 $w$，所以 $x$ 不进 seller demand，只剩 $y$。

第二层是 mechanism：local selling 为什么会 reveal location？因为 pickup 成本随 $x$ 变化，消费者是否选择自提会把位置差异带回需求结构。

第三层是 regime distinction：为什么有时只 partial reveal，有时 full reveal？关键在于 location 是否足以改变 seller choice。如果消费者只是在同一卖家内部选择 pickup 还是 delivery，价格竞争没有被真正改变；如果消费者会因为离某家店近而改买该卖家，价格竞争才会被缓和。

可以在 seminar 中追问的几个问题：

1. 为什么用 $a>w$ 和 $a<w$ 来区分 preference vs location dominance，而不是直接用 $a$ 与 $t$ 比较？这个条件来自模型分割结构，但经济解释上是否足够透明？
2. 如果卖家可以对 pickup 和 delivery 设置不同价格或不同服务费，full location revealing 机制会增强还是减弱？
3. 如果平台可以向 local selling 卖家收取参与费，消费者福利是否会更差，还是价格可能下降？
4. 如果市场不是 full coverage，local selling 导致的价格上升是否会让平台损失交易量，从而削弱结论？
5. 哪些产品最可能满足 location-dominates-preference？文章举 standard products / T-shirts，但实际中 grocery、pharmacy、electronics accessories 等品类可能更贴切。

## 14. Bottom line

这篇文章做的不是传统意义上的 BOPS 论文，而是一个关于平台如何通过 omnichannel design 改变第三方卖家竞争结构的理论模型。它的核心概念是：traditional online selling mask location heterogeneity；local selling reveal location heterogeneity；revealed location differentiation can soften seller competition；softened competition raises prices and platform commission revenue。

因此，local selling 可以是服务创新，也可以是竞争管理工具。对平台而言，它的价值不在于履约本身，而在于改变卖家定价环境；对消费者而言，多一个履约选项并不自动意味着更高 welfare。


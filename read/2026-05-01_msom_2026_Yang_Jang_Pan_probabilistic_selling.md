# Probabilistic Selling for Vertically Differentiated Products in a Decentralized Channel

作者：Zhechao Yang（George Mason University）、Hongseok Jang（Tulane University）、Xiajun Amy Pan（University of Florida）  
期刊：*Manufacturing & Service Operations Management*，Articles in Advance  
年份：2026  
主题：Probabilistic Selling；Vertically Differentiated Products；Decentralized Channel；Wholesale Contract；Product Line Design

## 1. 中文摘要

本文研究一个非常具体但在实践中越来越常见的问题：当供应链里有一个供应商和一个零售商，产品存在高低质量差异，且企业想卖“盲盒/随机包”这类 probabilistic products 时，究竟应该由谁来组装这些随机产品，是供应商，还是零售商？

文章构建了一个由一个 supplier 和一个 retailer 组成的去中心化渠道模型。供应商生产高质量产品 $h$ 和低质量产品 $l$，零售商向两类消费者销售。企业可以把一部分高质量产品和低质量产品混合成 probabilistic product $p$，消费者在付款前只知道拿到高质量产品的概率 $\phi$，付款后才知道具体获得什么。组装 probabilistic product 会带来额外 transaction cost $c$，因此“谁来组装”不是中性的：它会改变 wholesale price、retail price、产品组合、渠道利润分配以及消费者福利。

核心结论是：probabilistic selling（PS）不只是一个营销 gimmick，它可以在去中心化渠道中缓解 double marginalization，并在某些条件下同时提高 supplier、retailer 和 consumers 的福利。尤其反直觉的是，零售商未必应该坚持自己掌控盲盒的组装权；在很多情形下，由供应商组装反而更容易采用 PS，并可能形成 win-win-win。

## 2. 论文速览表格

| 维度 | 内容 |
|:---|:---|
| 研究问题 | 在高低质量垂直差异产品的去中心化渠道中，probabilistic products 应该由 supplier 还是 retailer 组装？不同 stewardship 如何影响 PS adoption、产品组合、价格、渠道利润与消费者福利？ |
| 实践背景 | 盲盒、mystery pack、opaque selling、surprise box，例如 Drop.com Blue Box、ToyWiz Mystery Pack、Pop Mart Labubu、LEGO Minifigure Mystery Pack、Hotwire Special Car。 |
| 研究方法 | Game-theoretic model；wholesale contract；backward induction；比较 retailer assembly（RA）与 supplier assembly（SA）；求 Nash equilibrium。 |
| 基本设定 | 一个 supplier 生产高质量 $h$ 与低质量 $l$；一个 retailer 销售；两类消费者 $H,L$；probabilistic product $p$ 以概率 $\phi$ 给高质量产品。 |
| 两个产能情形 | Abundant high-quality capacity：$n_H<M$ 且 $n_L>N$；Limited high-quality capacity：$n_H>M$ 且 $n_L<N$。 |
| 核心机制 | Market expansion、cannibalization、price discrimination、strategic differentiation、double marginalization mitigation、transaction cost burden。 |
| 主要发现 | 当 transaction cost 不太高时，PS 可以提升渠道效率；SA 通常比 RA 更容易采用 PS；SA 下供应商会设定更低的高质量中奖概率 $\phi$；PS 可以实现 supplier-retailer-consumer 三方共赢。 |
| 管理启示 | 高质量产能充裕时，用剩余高质量产品和低质量产品做随机包，主要服务低类型消费者；高质量产能稀缺时，把高质量产品全部放入随机包，随机包服务高类型消费者。 |
| 理论贡献 | 将 vertical differentiation 下的 PS 从 centralized seller 扩展到 decentralized channel，并内生比较 RA 与 SA 的 stewardship。 |

## 3. TL;DR

这篇文章说明：盲盒/随机包在供应链里不只是“卖给消费者的不确定性”，更是一个能改变 supplier 和 retailer 利润分配的渠道工具。谁来组装盲盒非常重要；很多时候由供应商组装比由零售商组装更容易赚钱，甚至能让供应商、零售商和消费者都更好。

最关键的反直觉结果是：零售商有时应该主动把盲盒组装权让给供应商。供应商掌控组装后，可以设计较低的高质量中奖概率，减弱随机包对高质量单品的 cannibalization，同时通过 wholesale price 让整个渠道更有效率。

## 4. One More Thing：最值得分享的洞察

这篇文章最有意思的地方在于，它把“盲盒中奖概率”从一个消费者端的营销参数，变成了一个供应链治理参数。直觉上，零售商最接近消费者，似乎应该由零售商来设计和组装盲盒；但模型显示，供应商反而可能更适合做这件事。原因是供应商不仅关心随机包本身卖多少钱，还关心随机包会不会压低高质量产品的零售价，从而影响高质量产品的 wholesale margin。于是，供应商在组装盲盒时会故意放入更低比例的高质量产品，即设定更低的 $\phi$，让随机包和高质量单品不要太像。这样，高质量单品可以维持较高价格，随机包又可以扩大市场覆盖，渠道中的 double marginalization 也被部分缓解。换句话说，盲盒不是单纯制造“惊喜”，而是供应链里重新分配 surplus、缓解渠道冲突的一种工具。

## 5. 研究背景与动机

### 5.1 实践痛点

Probabilistic selling 指消费者付款前不知道具体会得到哪个产品，只知道可能获得哪些产品以及相应概率。现实中包括 blind box、mystery bag、opaque product、surprise pack 等。

文章使用了多个例子说明 PS 已经是重要的零售模式：

1. Hotwire 将 Dollar Rent A Car 的 compact car 和 midsize car 混合，出售 “Special Car”。消费者购买后随机获得其中一种车型。
2. Drop.com 曾推出 Blue Box，把不同价位的 Thinksound headphones 混在一起出售。
3. ToyWiz.com 出售 LEGO minifigure Mystery Pack 和 Funko Disney mystery bag。
4. Pop Mart 通过 blind boxes 销售收藏玩具，特别是 Labubu 系列。

这些例子有两个共同点。第一，产品存在垂直差异：在价格相同的情况下，所有消费者都更喜欢高质量/稀缺/chase item。第二，随机产品并非零成本生成。企业要说明规则、管理库存、处理物流和会计流程，因此每销售一个 probabilistic product 都有额外 transaction cost $c$。

这就产生了本文的核心运营问题：在一个 supplier-retailer channel 中，谁应该承担这个组装和交易成本？

### 5.2 理论缺口

已有文献主要有三类：

1. 早期 PS 文献多研究 horizontally differentiated products，例如消费者偏好不同航班、酒店、车型或产品变体。
2. 一部分文献研究 vertically differentiated products，但多数是 centralized seller，即只有一个卖方，不存在 supplier 和 retailer 的渠道冲突。
3. 少数文献开始研究 supply chain 中的 PS，但通常只允许 retailer 组装 probabilistic products，且多是 horizontal differentiation。

本文补足的空白是：在 vertically differentiated products 的去中心化渠道中，同时允许 supplier assembly 和 retailer assembly，并比较两种 stewardship 的效果。

### 5.3 核心贡献

第一，本文把 PS 放入 decentralized channel，识别出 PS 如何缓解 double marginalization，而不仅仅是带来价格歧视或市场扩张。

第二，本文内生比较 RA 与 SA，说明 stewardship 会改变 PS 是否被采用、采用哪种产品组合、以及 $\phi$ 如何设定。

第三，本文区分高质量产能充裕与高质量产能稀缺两种运营环境，说明同样是 PS，在不同产能条件下服务的消费者类型完全不同。

第四，本文给出一个渠道治理洞察：SA 可能让 supplier、retailer、consumers 同时受益，形成 win-win-win。

## 6. 模型设定与假设

### 6.1 参与方与产品

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| Supplier | 供应商 | 生产高质量产品和低质量产品，通过 retailer 销售。 |
| Retailer | 零售商 | 从 supplier 以 wholesale prices 采购，再以 retail prices 销售给消费者。 |
| $h$ | 高质量产品 | High-quality product。 |
| $l$ | 低质量产品 | Low-quality product。 |
| $p$ | 随机产品 | Probabilistic product；以概率 $\phi$ 给 $h$，以概率 $1-\phi$ 给 $l$。 |
| $M$ | 高质量产品产能 | Supplier 的 high-quality capacity。 |
| $N$ | 低质量产品产能 | Supplier 的 low-quality capacity，并假设 $M<N$。 |
| $c_h,c_l$ | 产品边际生产成本 | 分别对应 $h$ 与 $l$。 |
| $c$ | PS transaction cost | 每卖出一个 $p$ 额外产生的成本，由组装方承担。 |

### 6.2 消费者与效用

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $H,L$ | 两类消费者 | High-type 和 low-type。 |
| $n_H,n_L$ | 市场规模 | 两类消费者数量。 |
| $V_{ij}$ | 估值 | 类型 $i\in\{H,L\}$ 对产品 $j\in\{h,l,p\}$ 的估值。 |
| $r_j$ | 零售价 | Retail price of product $j$。 |
| $U_{ij}$ | 消费者效用 | $U_{ij}=V_{ij}-r_j$，不购买效用归一化为 0。 |

消费者对随机产品的估值是期望估值：

$$
V_{Hp}=\phi V_{Hh}+(1-\phi)V_{Hl},\qquad
V_{Lp}=\phi V_{Lh}+(1-\phi)V_{Ll}.
$$

消费者选择带来最高非负效用的产品。

### 6.3 垂直差异假设

文章假设：

$$
V_{Hh}>V_{Hl},\qquad V_{Lh}>V_{Ll},
$$

$$
V_{Hh}>V_{Lh},\qquad V_{Hl}>V_{Ll}.
$$

也就是说，高低类型消费者都更喜欢高质量产品，而且 high-type 对任何质量产品的估值都高于 low-type。

进一步定义 quality increment valuation gap：

$$
\Delta=[V_{Hh}-V_{Hl}]-[V_{Lh}-V_{Ll}]>0.
$$

这表示 high-type 对质量提升的边际支付意愿更高。

### 6.4 Probabilistic product 的形成

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $Y$ | 用于组装 $p$ 的高质量产品数量 | $0\le Y\le M$。 |
| $X$ | 用于组装 $p$ 的低质量产品数量 | $0\le X\le N$。 |
| $\phi$ | 获得高质量产品的概率 | $\phi=Y/(X+Y)$。 |
| $c_p$ | $p$ 的期望产品成本 | $c_p=\phi c_h+(1-\phi)c_l$，不含 transaction cost $c$。 |

如果 $X=Y=0$，则没有 PS。若 $X=N$，所有低质量产品都被放进随机包，不单独销售 $l$。若 $Y=M$，所有高质量产品都被放进随机包，不单独销售 $h$。

### 6.5 两种 stewardship：RA 与 SA

| 情形 | 谁组装 probabilistic product | 谁承担 transaction cost $c$ | 决策含义 |
|:---|:---|:---|:---|
| RA | Retailer Assembly | Retailer | Supplier 只批发 $h,l$；retailer 买入后自行混合成 $p$。 |
| SA | Supplier Assembly | Supplier | Supplier 直接组装 $p$ 并批发给 retailer。 |

### 6.6 产能情形

文章重点研究总需求超过总产能：

$$
n_H+n_L>M+N.
$$

在此基础上区分两种运营场景：

| 场景 | 条件 | 经济含义 |
|:---|:---|:---|
| 高质量产能充裕 | $n_H<M$ 且 $n_L>N$ | 高类型消费者都可以被高质量产品服务，剩余高质量产能可用于 PS。 |
| 高质量产能稀缺 | $n_H>M$ 且 $n_L<N$ | 高质量产品不足以服务所有高类型消费者，低质量产品相对充裕。 |

### 6.7 决策结构与信息结构

主模型采用 supplier leadership。

1. Supplier 先决定是否自己组装 probabilistic products。
2. 如果 supplier 选择 SA，则 supplier 决定 wholesale prices 和 $\phi$，retailer 再设定 retail prices。
3. 如果 supplier 不采用 SA，则 retailer 决定是否采用 RA，自行决定 $\phi$、产品组合和 retail prices。
4. 消费者观察产品、价格和概率后做购买决策。

信息结构是完全信息。双方知道成本、估值、市场规模、产能与交易成本。

### 6.8 RA 下的目标函数

RA 中，supplier 设置 $w_h,w_l$，retailer 选择 $r_h,r_p,r_l$ 以及 $X,Y$。

随机产品对 retailer 的期望 wholesale cost 为：

$$
\bar w_p=\phi w_h+(1-\phi)w_l.
$$

Retailer 的利润为：

$$
\pi_{R,RA}
=D_h(r_h-w_h)+D_p(r_p-\bar w_p-c)+D_l(r_l-w_l).
$$

> 直觉：第一项是卖高质量单品的 retail margin，第二项是卖随机包的 margin，其中 retailer 既要支付混合进随机包的期望 wholesale cost，也要承担 transaction cost $c$，第三项是卖低质量单品的 margin。

Supplier 的利润为：

$$
\pi_{S,RA}
=(D_h+\phi D_p)(w_h-c_h)+(D_l+(1-\phi)D_p)(w_l-c_l).
$$

> 直觉：在 RA 中，supplier 并不直接卖 $p$，而是卖给 retailer 一些 $h$ 和 $l$。随机包中有 $\phi D_p$ 单位高质量产品和 $(1-\phi)D_p$ 单位低质量产品，因此 supplier 的利润按实际被使用的 $h,l$ 数量计算。

### 6.9 SA 下的目标函数

SA 中，supplier 选择 $w_h,w_p,w_l$ 以及 $X,Y$；retailer 只选择零售价。

Retailer 的利润为：

$$
\pi_{R,SA}
=D_h(r_h-w_h)+D_p(r_p-w_p)+D_l(r_l-w_l).
$$

> 直觉：supplier 已经把随机包组装好并以 $w_p$ 批发给 retailer，因此 retailer 不承担 transaction cost，也不需要把 $w_p$ 拆成 $h,l$ 的期望成本。

Supplier 的利润为：

$$
\pi_{S,SA}
=D_h(w_h-c_h)+D_p(w_p-c_p-c)+D_l(w_l-c_l).
$$

> 直觉：supplier 直接销售三类批发产品。对随机包而言，supplier 的成本包括产品期望成本 $c_p$ 和每单位 transaction cost $c$。

### 6.10 关键假设、合理性与潜在影响

| 假设 | 合理性 | 若放松可能的影响 |
|:---|:---|:---|
| 一个 supplier 和一个 retailer | 能清晰隔离 wholesale contract 下的 double marginalization。 | 多 supplier 或多 retailer 会引入竞争、渠道权力和 assortment externality，可能改变 SA/RA 的偏好。 |
| 两个质量等级、两类消费者 | 是 vertical differentiation 的最小可解模型。 | 连续质量或连续消费者类型会让阈值更平滑，但核心机制可能仍存在。 |
| 消费者按期望效用评价 $p$ | 便于突出供应链机制，而非行为偏差。 | 若消费者喜欢赌博、稀缺性或惊喜，PS adoption 区域可能扩大。 |
| 概率 $\phi$ 公开且可信 | 许多 blind box/mystery pack 会公布概率或规则。 | 若概率不可验证，会出现声誉、监管、欺骗和消费者信任问题。 |
| 产能固定 | 符合短期运营场景。 | 长期中 supplier 可能内生选择高质量产能，使 PS 反过来影响产品设计和产能投资。 |
| transaction cost 按单位线性发生 | 反映订单履约、库存、物流、会计等随销量增加的成本。 | 若存在固定 setup cost 或规模经济，PS adoption 的阈值会改变。 |
| wholesale contract | 是经典渠道模型，也符合许多电商和旅游平台实践。 | Revenue sharing、buyback、two-part tariff 等合同可能进一步协调渠道，弱化本文的 double marginalization 机制。 |

## 7. 分析路线图

文章的逻辑非常清楚，可以按以下路径阅读。

1. **Benchmark without PS**：先不允许随机包，求去中心化渠道中三种常规产品线策略：UM、SD、WD。
2. **RA with abundant high-quality capacity**：允许 retailer 组装随机包，分析何时出现 $\{h,p\}$ 或 $\{h,p,l\}$。
3. **SA with abundant high-quality capacity**：允许 supplier 组装随机包，比较 SA 与 RA 的差异。
4. **RA vs. SA comparison**：研究谁更愿意掌控随机包、$\phi$ 如何变化、是否存在 win-win-win。
5. **Nash equilibrium under supplier leadership**：supplier 先动时，均衡中到底由谁组装或是否采用 PS。
6. **Limited high-quality capacity**：把主模型扩展到高质量产品稀缺，说明 PS 的目标消费者和产品组合发生反转。
7. **Retailer leadership appendix**：如果 retailer 更强势，retailer 可能自己采用 PS，也可能把组装权让给 supplier。

## 8. 核心分析与求解

### 8.1 Benchmark：没有 PS 时的三种策略

在没有 probabilistic products 的情况下，文章得到三个可能的 benchmark strategies。

| 策略 | 产品组合与目标消费者 | 何时出现 | 经济含义 |
|:---|:---|:---|:---|
| UM：Up-market | 只卖 $h$ 给 high-type | $c_h,c_l$ 都相对高 | 放弃 low-type，专注高端消费者。 |
| SD：Strong differentiation | $h$ 给 high-type，$l$ 给 low-type | $c_l$ 较低、$c_h$ 较高 | 经典垂直差异化产品线。 |
| WD：Weak differentiation | 高质量产品也覆盖部分 low-type | $c_h$ 较低 | 通过较低价格充分利用高质量产能。 |

**Lemma 1：无 PS 时，最优 benchmark 是 UM、SD 或 WD，具体取决于 $c_h,c_l$ 的相对大小。**

> 经济直觉：如果高低质量产品都贵，服务 low-type 不划算，渠道选择 UM。如果低质量产品便宜，渠道可以用 $l$ 服务 low-type，形成 SD。如果高质量产品便宜，渠道有动力降低 $h$ 的价格以扩大覆盖，即 WD。相较 centralized channel，去中心化渠道存在 double marginalization，因此更不愿意用低价扩大市场，WD 更不容易出现。

### 8.2 RA：由 retailer 组装随机包

在 RA 中，supplier 只设置 $w_h,w_l$，retailer 购买后自行混合成 $p$。

**Proposition 1：在高质量产能充裕时，RA 下如果 transaction cost 较低，retailer 采用 $\{h,p\}$；如果 transaction cost 中等，retailer 采用 $\{h,p,l\}$；如果 transaction cost 太高，则不采用 PS。**

> 经济直觉：高质量产能充裕意味着服务完 high-type 后还有剩余 $M-n_H$，这些剩余高质量产品可以和低质量产品混合成随机包，卖给 low-type。若 $c$ 很低，retailer 倾向于把所有低质量产品都放入随机包，即 $X=N$，得到 $\{h,p\}$，这样可以降低随机包和高质量单品之间的替代性，减轻 cannibalization。若 $c$ 上升，把太多产品做成随机包会产生太多 transaction cost，因此 retailer 只拿一部分低质量产品混合，其余 $l$ 单独销售，得到 $\{h,p,l\}$。

RA 下 PS 的收益与成本来自以下几个效应：

| 效应 | 对 RA 的含义 |
|:---|:---|
| Market expansion | 用剩余高质量产能和低质量产品覆盖更多消费者。 |
| Cannibalization | 随机包与高质量产品相似，会压低 $h$ 的零售价。 |
| Price discrimination | 多一个 $p$ 可以更细分消费者。 |
| Double marginalization mitigation | Supplier 为诱导 retailer 采用 PS，会降低某些 wholesale prices，使 retailer margin 上升。 |
| Transaction cost | Retailer 每卖一个 $p$ 要承担 $c$。 |
| Strategic differentiation | 相比 WD，随机包可以让 $h$ 与低端产品拉开差异，从而提高 $h$ 的价格。 |

**Proposition 2：与 centralized channel 相比，RA 下 decentralized channel 更不容易采用 PS。**

> 经济直觉：centralized seller 内部化所有利润，PS 的 market expansion 和 price discrimination 好处可以直接体现。但在 RA 的 decentralized channel 中，supplier 需要通过 wholesale price 影响 retailer。由于 double marginalization 的存在，supplier 不一定能把 wholesale price 调到足够低来支持 retailer 采用 PS，特别是当 transaction cost 不低时，PS 的好处被渠道扭曲削弱。因此 RA 下 PS adoption 区域比 centralized channel 更小。

### 8.3 SA：由 supplier 组装随机包

在 SA 中，supplier 自己组装 $p$，设置 $w_h,w_p,w_l$ 和 $\phi$，retailer 再设置零售价。

**Proposition 3：在高质量产能充裕时，SA 下的最优产品组合也呈现 $\{h,p\}$ 或 $\{h,p,l\}$；transaction cost 较低时为 $\{h,p\}$，较高但未超过阈值时为 $\{h,p,l\}$，过高时不采用 PS。**

> 经济直觉：SA 与 RA 的表面产品组合相似，但利润分配完全不同。SA 中，supplier 承担 $c$，但也可以直接设置 $w_p$，并通过 $w_h,w_p,w_l$ 控制 retailer 的产品组合。supplier 能从随机包中直接提取批发利润，因此在更宽的条件下愿意采用 PS。

**Proposition 4：与 centralized channel 相比，SA 下 decentralized channel 在 transaction cost 较高时反而可能更容易采用 PS；但当 transaction cost 较低时，仍然可能更不容易采用 PS。**

> 经济直觉：这是本文很重要的反直觉结果。一般认为 decentralized channel 因 double marginalization 会降低效率，因此不利于新产品线。但在 SA 中，supplier 可以通过设计较低的 $\phi$ 来减弱 $p$ 对 $h$ 的 cannibalization，使 $h$ 保持较高价格，并提高 $w_h$。这种 strategic differentiation effect 在 decentralized channel 中被放大：supplier 通过 wholesale price 把这个高端价格空间转化为自身利润。当 $c$ 较高时，这个效应可以使 decentralized SA 比 centralized seller 更愿意采用 PS。

### 8.4 RA vs. SA：stewardship 改变随机包设计

在建立 RA 和 SA 各自的最优策略后，文章进一步比较两者。

**Proposition 5：如果 RA 和 SA 都采用 PS，则 SA 下的高质量中奖概率不高于 RA，即 $\phi_{SA}\le \phi_{RA}$。**

> 经济直觉：supplier 组装随机包时，会更有动力把随机包做得“不那么像高质量单品”。因为 $p$ 越像 $h$，越会压低 $h$ 的零售价，进而压低 supplier 可以收取的 $w_h$。所以 supplier 会在 $p$ 中放入更多低质量产品，使 $\phi$ 更低。这个结果有管理含义：supplier 做盲盒时，不应简单模仿 retailer 的混合比例，而应使用更低的高质量比例，并把概率信息清楚传递给 retailer。

**Proposition 6：PS 在 SA 下比在 RA 下更容易被采用。**

> 经济直觉：RA 中 retailer 承担 transaction cost，supplier 还要降低 wholesale price 来激励 retailer 采用 PS，这会损害 supplier margin。因此 supplier 可能通过 wholesale price 阻止 retailer 做 PS。SA 中 supplier 自己承担 cost，但也自己掌控 $w_p$ 和 $\phi$，可以利用 market expansion、price discrimination 和 strategic differentiation 来覆盖成本，所以 adoption 区域更大。

**Proposition 7：在某些条件下，SA 可以形成 supplier、retailer、consumers 的 win-win-win。**

> 经济直觉：当 RA 下不采用 PS 而 SA 下采用 PS 时，SA 可以扩大市场覆盖，让 supplier 通过新增批发产品获取利润；retailer 不承担组装成本，同时受益于更低的 wholesale distortion；消费者则因高质量产品价格下降或产品可得性提高而受益。结果是三方都比 RA 更好。这个结果解释了为什么零售商有时应当把盲盒组装权交给供应商，而不是坚持自己控制。

**Corollary 1：当高质量产能充裕时，如果采用 PS，随机包总是针对 low-type consumers。**

> 经济直觉：因为 high-type 对 $h$ 的支付意愿最高，只要高质量产能足以服务 high-type，最赚钱的做法就是把 $h$ 单独卖给 high-type。剩余高质量产能再与低质量产品混合成 $p$，用于吸引 low-type。这也是为什么 abundant case 中常见产品组合是 $\{h,p\}$ 或 $\{h,p,l\}$。

### 8.5 Supplier leadership 下的 Nash equilibrium

**Proposition 8：在高质量产能充裕时，supplier leadership 下的 Nash equilibrium 是：如果 transaction cost 低于 SA 的相关阈值，supplier 自己组装并提供 probabilistic products；否则不采用 PS。**

> 经济直觉：均衡里 supplier 不会轻易让 retailer 做 RA。若 PS 对 supplier 有利，supplier 会自己先做 SA，以避免 RA 中由于 retailer 承担成本而引起的 wholesale price 下调压力。若 PS 对 supplier 不利，supplier 可以通过 wholesale prices 使 retailer 也没有动力做 PS。因此，在 supplier leadership 下，最终要么 supplier-led PS，要么 no PS。

### 8.6 Extension：高质量产能稀缺

主模型之后，文章考察另一种很现实的情形：高质量产品是 scarce/chase item，低质量产品相对充裕。形式上：

$$
n_H>M,
\qquad n_L<N.
$$

此时逻辑发生明显变化。由于高质量产品连 high-type 都服务不完，单独销售 $h$ 不再一定是最优。PS 的角色从“消化剩余高质量产能”变成“把稀缺高质量产品摊薄后服务更多 high-type”。

**Proposition 9：在高质量产能稀缺时，SA 仍可能形成 win-win-win；此时产品组合是 $\{p,l\}$。**

> 经济直觉：高质量产能稀缺时，supplier 把所有高质量产品都放入随机包，随机包 $p$ 主要针对 high-type，低质量单品 $l$ 针对 low-type。SA 下 supplier 直接控制 $p$ 的批发价和概率，可以通过 market expansion 覆盖更多 high-type。retailer 不承担 transaction cost，消费者也能以随机包形式获得高质量产品的机会，因此存在三方共赢区域。

**Proposition 10：在高质量产能稀缺时，supplier leadership 下的 Nash equilibrium 是：若 transaction cost 足够低，supplier 组装并销售 $\{p,l\}$；否则不采用 PS。**

> 经济直觉：有限的高质量产品不再单独出售，而是全部用于组装 $p$。这与高质量产能充裕时完全不同：充裕时 $p$ 面向 low-type，稀缺时 $p$ 面向 high-type。这说明 PS 的功能取决于 capacity regime；它既可以处理剩余产能，也可以把稀缺资源概率化分配。

### 8.7 Appendix：retailer leadership

文章还在 Online Appendix 中分析 retailer 更强势的情形。主要结论是：当 transaction cost 足够低时，retailer 可能主动采用 PS，因为它可以享受 double marginalization mitigation；当 transaction cost 中等时，retailer 反而可能偏好让 supplier 组装随机包。

> 经济直觉：retailer leadership 不会完全推翻主模型，而是说明渠道权力会改变“谁先行动”。但即便 retailer 有权先决定，它也不一定总想自己组装。只要 transaction cost 和 wholesale price interaction 使 SA 更有利，retailer 仍可能选择 delegation。

## 9. 比较静态汇总表

| 参数或条件变化 | 对 PS adoption 的影响 | 对产品组合/概率的影响 | 直觉 |
|:---|:---|:---|:---|
| $c\uparrow$ | PS 更不容易被采用 | Abundant case 中通常从 $\{h,p\}$ 转向 $\{h,p,l\}$，再到 no PS | transaction cost 越高，组装随机包的利润侵蚀越大。 |
| $c$ 很低 | PS 更容易被采用 | 倾向 $\{h,p\}$，把所有低质量产品放进 $p$ | 低 transaction cost 下，多卖随机包的成本低，可以用更多 $l$ 稀释 $p$，降低 cannibalization。 |
| $c$ 中等 | PS 仍可能采用 | 倾向 $\{h,p,l\}$ | 只用部分 $l$ 组装 $p$，其余 $l$ 单卖，平衡 cannibalization 和 transaction cost。 |
| $\phi\downarrow$ | 不必然改变 adoption，但有利于保护 $h$ 的价格 | $p$ 与 $h$ 更不相似 | 减弱 $p$ 对 $h$ 的 cannibalization，提高 strategic differentiation。 |
| SA 替代 RA | PS adoption 区域扩大 | $\phi_{SA}\le \phi_{RA}$ | supplier 更愿意用低 $\phi$ 保护高质量单品和 wholesale margin。 |
| Decentralization under RA | PS 更不容易采用 | 产品线可能变短 | double marginalization 使 retailer 的 PS 激励不足。 |
| Decentralization under SA 且 $c$ 较高 | PS 可能比 centralized 更容易采用 | 更可能出现 $\{h,p,l\}$ | strategic differentiation 被 supplier 的 wholesale pricing 放大。 |
| 高质量产能充裕 $n_H<M$ | PS 若采用，目标是 low-type | $h$ 给 high-type，剩余 $h$ 与 $l$ 形成 $p$ | 先用 $h$ 服务高支付意愿消费者，再用剩余产能扩张市场。 |
| 高质量产能稀缺 $n_H>M$ | PS 若采用，通常需 SA | $\{p,l\}$，且所有 $h$ 用于 $p$ | 高质量产品太稀缺，概率化分配给 high-type 更有利。 |
| $c_h$ 较低 | Benchmark 更可能是 WD | PS 通过 strategic differentiation 与 WD 竞争 | 高质量产品便宜时，直接扩大 $h$ 覆盖有吸引力；PS 要靠保护高端价格胜出。 |
| $c_l$ 较低 | Benchmark 更可能是 SD | PS 可与 $l$ 形成更丰富产品线 | 低质量产品便宜时，服务 low-type 更有利。 |

## 10. 主要结论与管理启示

### 10.1 与 Benchmark 的对比

| 情形 | 没有 PS | 有 PS 且 RA | 有 PS 且 SA |
|:---|:---|:---|:---|
| 产品线 | UM、SD 或 WD | $\{h,p\}$ 或 $\{h,p,l\}$ | 高质量充裕时 $\{h,p\}$ 或 $\{h,p,l\}$；高质量稀缺时 $\{p,l\}$。 |
| 渠道效率 | 受 double marginalization 影响 | PS 可缓解部分 double marginalization，但 retailer 承担 $c$ | PS 更容易缓解渠道冲突，supplier 可直接控制 $w_p$ 和 $\phi$。 |
| 高质量产品定价 | 取决于 UM/SD/WD | $p$ 可能 cannibalize $h$ | supplier 会降低 $\phi$ 来保护 $h$ 价格。 |
| 采用条件 | 无 transaction cost | 要求 $c$ 不高，且 supplier 愿意让 retailer 做 | adoption 区域通常更大。 |
| 消费者福利 | 由常规产品线决定 | 可能因新选择受益 | 在某些区域与 supplier、retailer 同时受益。 |

### 10.2 管理建议

1. **不要只问“要不要卖盲盒”，更要问“谁来组装盲盒”。** 组装权决定 transaction cost 由谁承担，也决定 wholesale price 如何设置。

2. **高质量产能充裕时，随机包应主要面向 low-type consumers。** 先把高质量单品卖给 high-type，再把剩余高质量产品与低质量产品混合成 $p$。

3. **高质量产能稀缺时，随机包应主要面向 high-type consumers。** 此时高质量产品全部放进 $p$，并与 $l$ 搭配销售，形成 $\{p,l\}$。

4. **供应商组装随机包时，应使用比零售商更低的高质量比例。** 低 $\phi$ 可以降低 cannibalization，保护高质量单品价格和 wholesale margin。

5. **零售商不应默认保留 blind box stewardship。** 当 SA 能带来更大市场覆盖和更低渠道扭曲时，delegating assembly to supplier 可能让 retailer 自己也更好。

6. **transaction cost 是 adoption 的关键门槛。** 若 $c$ 很高，PS 不值得采用；若 $c$ 低或中等，企业应比较 $\{h,p\}$、$\{h,p,l\}$ 或 $\{p,l\}$ 的利润。

7. **渠道成员应在 game starts 前协商 stewardship。** 如果 supplier 和 retailer 对 RA/SA 偏好不一致，可以用 revenue sharing、side payment 或 two-part tariff 来协调。

## 11. 与相关文献的对话

### 11.1 Fay and Xie (2008, 2010)：Probabilistic goods 的基础逻辑

Fay and Xie 系列论文奠定了 probabilistic selling 的基本思想：卖方可以通过让消费者在购买前面临不确定性来进行 price discrimination、inventory management 或 market segmentation。本文继承了 PS 的核心逻辑，但不把卖方看作一个 centralized firm，而是放入 supplier-retailer channel 中，研究 channel conflict 如何改变 PS。

区别的重要性在于：在 centralized seller 中，PS 的收益和成本都由同一方内部化；在 decentralized channel 中，谁承担 transaction cost、谁获得 wholesale margin 会改变最终是否采用 PS。

### 11.2 Zhang, Joseph, and Subramaniam (2015)：垂直差异产品中的 PS

Zhang et al. 研究 quality-differentiated markets 中的 probabilistic selling，是本文最直接的理论基础之一。它说明，在垂直差异市场中，PS 可以帮助卖方处理剩余产能，并在高低质量产品之间进行策略性配置。

本文相对于 Zhang et al. 的推进是：把 centralized channel 扩展到 decentralized channel，引入 supplier 和 retailer 的 wholesale interaction，并比较 RA 与 SA。此外，本文还分析 high-quality capacity limited 的情形，得到 $\{p,l\}$ 这一不同于 abundant case 的产品组合。

### 11.3 Fay and Gheibi (2024)：供应链中的 PS

Fay and Gheibi 研究 supply chain 中 PS 对 retailer-manufacturer interactions 的影响，但其背景主要是 horizontally differentiated products，并且通常由 retailer 组装 probabilistic products。

本文的区别有三点。第一，产品是 vertically differentiated，因此 high-quality product 的 cannibalization 和 strategic differentiation 更重要。第二，本文内生比较 supplier assembly 和 retailer assembly。第三，本文发现 decentralization 在 SA 下有时会促进 PS adoption，这与“去中心化通常削弱 PS”的直觉不同。

### 11.4 Huang and Yu (2014), Zheng et al. (2019)：行为消费者下的垂直 PS

这些研究强调 bounded rationality 或 salient thinking 等消费者行为如何让 PS 更有利。本文则刻意采用更标准的 rational expected utility，说明即使没有行为偏差，PS 也能因供应链机制而产生价值。

这一区别重要，因为它把 PS 的解释从“消费者被不确定性吸引”扩展到“渠道结构和产能配置使 PS 有效率”。

## 12. 犀利评论：Reviewer’s Critique

### 12.1 优点

理论贡献明确。文章不是简单把已有 PS 模型放进供应链，而是抓住 stewardship 这个关键决策变量，说明谁组装随机包会改变均衡。

机制分解清楚。文章把 PS 的作用拆成 market expansion、cannibalization、price discrimination、strategic differentiation、double marginalization mitigation 和 transaction cost，使读者能理解不同区域的经济逻辑。

实践相关性强。盲盒、mystery pack、opaque products 在零售中非常常见，而供应商组装还是零售商组装确实是企业需要决定的问题。

### 12.2 模型限制与可能过强的假设

第一，消费者被简化为两类，产品也只有两个质量等级。这使阈值结构清楚，但现实中的质量、偏好和支付意愿通常是连续的。若引入连续类型，产品组合可能不再只有 $\{h,p\}$、$\{h,p,l\}$、$\{p,l\}$ 这几种干净形式。

第二，消费者对随机包按期望效用评价，没有 lottery preference、稀缺偏好、收藏价值、后悔心理或二级市场转售。现实中的 blind box 往往依赖 chase figure 的稀缺性和收藏心理，因此模型可能低估 PS 的需求端吸引力。

第三，概率 $\phi$ 被假设为公开且可信。现实中概率披露、监管合规、平台信任和售后争议都会影响 PS 的可行性。

第四，文章主要使用 wholesale contract。若 supplier 和 retailer 能使用 two-part tariff、revenue sharing 或 resale price maintenance，double marginalization mitigation 的机制可能改变。

第五，产能是固定的。长期中，supplier 可能为了支持 blind box strategy 而主动设计稀缺性、改变 chase item 产能或调整质量，这会使 capacity regime 内生化。

### 12.3 未来研究方向

1. **Endogenous quality and rarity design**：让 supplier 同时选择质量水平、chase item 产能和 $\phi$，研究 PS 如何影响长期产品设计。

2. **Contract design for PS stewardship**：比较 wholesale contract、revenue sharing、two-part tariff、buyback contract 下 RA/SA 的协调效率。

3. **Behavioral demand for blind boxes**：加入消费者对惊喜、稀缺性、赌博性、后悔和公平性的偏好，检验 SA/RA 结论是否仍成立。

4. **Multi-supplier or platform setting**：研究 retailer 从多个 supplier 采购并混合产品时的竞争、搭便车和概率披露问题。

5. **Dynamic inventory and learning**：考虑多期销售、库存结转、消费者学习概率和企业声誉，分析 PS 是否会被消费者策略性等待或抵制。

6. **Multiple probabilistic products**：企业可能同时提供多个不同价格和中奖概率的 blind boxes，未来可研究概率菜单的最优设计。

## 13. 最后一页式总结

这篇文章的核心不是“盲盒能不能赚钱”，而是“盲盒在供应链中由谁来做，为什么会改变整个渠道的利润结构”。

在高质量产能充裕时，PS 的作用是把剩余高质量产能和低质量产品混合，主要服务 low-type consumers。此时产品组合通常是 $\{h,p\}$ 或 $\{h,p,l\}$。在高质量产能稀缺时，PS 的作用变成把稀缺高质量产品概率化分配给 high-type consumers，此时产品组合变成 $\{p,l\}$。

最重要的管理结论是：SA 往往比 RA 更容易采用 PS。supplier 会选择更低的高质量中奖概率 $\phi$，用来减轻随机包对高质量产品的 cannibalization，并通过 wholesale price 提取利润。在某些区域，这种安排不仅让 supplier 更好，也让 retailer 和 consumers 更好，形成 win-win-win。


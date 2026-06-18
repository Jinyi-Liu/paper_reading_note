# Information Design of Online Platforms

阅读笔记日期：2026-06-17  
论文：T. Tony Ke, Song Lin, Michelle Y. Lu, 2026, *Management Science*, Articles in Advance  
作者单位：Chinese University of Hong Kong；Hong Kong University of Science and Technology；China Europe International Business School  
DOI：10.1287/mnsc.2025.03083  
关键词：consumer search；information design；personalization；platform design；product recommendation；targeted advertising

## 1. 标题与元信息

### 中文摘要

本文研究一个在线平台如何战略性地使用它掌握的消费者—卖家匹配信息，同时影响消费者搜索和卖家的定向广告竞价。平台既可以把信息用于精准推荐，提升消费者和卖家的匹配效率，也可以把信息设计得更粗糙，从而让多个卖家竞争广告展示位并向平台支付更高广告费。文章的核心结论是：当平台的销售佣金率较低、广告收入更重要时，平台未必愿意把最匹配的产品精准推荐给消费者；相反，它可能把真正匹配的产品与一小组“候选卖家”和一条低概率“长尾”混在一起，限制消费者继续搜索，从而强化卖家对 prominent position 的竞争。这个最优信息设计可能降低社会福利，说明 retail platforms 上的 sponsored targeted advertising 可能引入匹配低效率。

## 2. 论文速览表格

| 维度 | 内容 |
|:---|:---|
| 研究问题 | 在线平台同时经营 personalized recommendation 和 sponsored targeted ads 时，平台会如何设计匹配信息？Sponsored ads 会不会扭曲平台的推荐准确性和匹配效率？ |
| 核心场景 | 平台知道消费者最适合哪个卖家；消费者需要搜索才能发现匹配；卖家竞价购买 prominent advertising position；平台从交易抽佣并收广告费。 |
| 方法 | 理论模型；Bayesian persuasion / information design；消费者 sequential search；卖家 second-price position auction。 |
| 核心 trade-off | **更精准的信息提高 match efficiency 和 commission revenue，但会削弱卖家对广告位的竞争；更粗糙的信息降低匹配效率，却能让卖家为 prominent position 出价。** |
| 最主要结论 | 若消费者搜索成本足够高且平台佣金率较低，平台最优地采用 noisy recommendation：两个高概率 contender 加一条低概率 long tail，并让消费者只访问 prominent seller。 |
| 反直觉洞察 | 平台越懂消费者，越不一定把最好的匹配直接告诉消费者；“推荐噪声”可能不是算法能力不足，而是广告商业模式下的最优设计。 |
| 管理含义 | 不同品类不应统一追求推荐准确率；低佣金、高广告变现的品类可能内生地产生更粗糙的推荐和更强 sponsored placement。 |
| 政策含义 | 只限制佣金率可能把平台推向更依赖广告收入的模式，反而降低匹配效率；隐私政策导致的信息粗糙化不一定显著伤害平台利润。 |
| 适用场景 | 消费者偏好较尖锐、接近“一个最合适卖家”的场景，如特定书名、特定品牌/规格、旅行/酒店偏好、电子产品配置等。 |
| 不太适用场景 | 消费者可能同时喜欢多个产品、偏好较平坦的品类，如部分时尚、食品、内容消费；文章用 extension 说明主机制仍可在一定条件下保留。 |

## 3. TL;DR

这篇文章说的是：平台明明知道哪个产品最适合消费者，但当广告收入比佣金更重要时，它可能故意不做最精准推荐，而是让几个卖家看起来都有机会，从而让他们竞争广告位。这样平台赚得更多，但消费者更可能看到不完全匹配的产品，所以 sponsored ads 可能让推荐系统变“故意不准”。

## 4. One More Thing：最值得分享的洞察

这篇文章最妙的地方在于，它把“推荐不准”从一个技术问题变成了一个商业模式问题。直觉上，我们以为平台有更多数据就会更好地匹配消费者；但模型告诉我们，如果平台把答案说得太清楚，真正匹配的卖家就像获得了一个局部垄断，其他卖家知道自己没戏，就不愿意为广告位出高价。于是平台最优的做法反而是制造一种“差一点就知道答案”的信息环境：两个卖家看起来都很可能匹配，剩下一长串卖家也保留一点点可能性。前者让卖家想赢，后者让输掉广告位的卖家真的失去被访问机会。推荐系统里的噪声，因此可以是平台用来卖广告位的战略资产。

## 5. 研究背景与动机 (Motivation)

### 5.1 实践痛点

在线零售平台越来越像“双重 steering 机器”。一方面，平台用消费者历史行为、购买记录和搜索信息做 personalized recommendation，帮助消费者更快找到合适产品；另一方面，平台把同一套数据用于 sponsored targeted advertising，让卖家竞价购买 prominent position。Amazon、Alibaba 等平台的 retail media business 已经成为重要收入来源。论文引用行业报告指出，全球 retail media revenue 在 2025 年约为 174.2 billion dollars，2026 年预计继续增长；美国 retail media ad spending 在 2025 年约为 60.32 billion dollars，2026 年预计到 69.33 billion dollars。

这带来一个平台运营中的核心冲突：推荐系统追求准确，广告系统追求竞价强度。若平台非常精准地告诉消费者“这个卖家就是你要的”，匹配效率提高，平台能多赚交易佣金；但被推荐卖家知道自己几乎一定能成交，其他卖家知道自己没机会，广告位竞价会变弱。相反，若平台保留一些不确定性，卖家之间会更积极争夺 prominent position，平台能提取更多 advertising revenue，但消费者匹配效率下降。

### 5.2 理论缺口

已有文献分别研究了 consumer search、position auctions、platform steering、information design 和 targeted advertising，但本文强调的是一个更综合的问题：同一个平台的信息设计同时作用于两边市场。

传统 search 模型关注消费者如何搜索、价格如何形成；position auction 文献关注广告位如何分配、卖家如何竞价；Bayesian persuasion 文献研究信息发送者如何设计信号影响接收者信念。本文的关键推进是把这些要素放到一个统一框架中：平台作为 Sender 设计 public signal，消费者和卖家同时作为 Receivers；消费者据此决定搜索顺序和搜索深度，卖家据此决定广告位竞价。

### 5.3 核心贡献

1. 本文把 personalized recommendation 和 targeted advertising 统一为一个 information design 问题，而不是把它们视为两个相互独立的算法模块。
2. 文章清晰刻画了平台在 match efficiency 和 seller surplus extraction 之间的权衡，并给出最优 posterior belief 的结构。
3. 文章说明 sponsored targeted ads 可能导致 socially inefficient recommendations：平台为了广告收入，会主动限制消费者搜索并引入匹配噪声。
4. 管理上，文章解释了为什么不同品类的推荐准确率目标不应相同；政策上，文章提醒监管者仅仅限制佣金率可能产生反效果。

## 6. 模型设定与假设 (Model Setup & Assumptions)

### 6.1 Players

| 玩家 | 决策 | 目标 |
|:---|:---|:---|
| Platform | 设计信息结构；举办广告位拍卖；收取交易佣金和广告费 | 最大化 commission revenue + advertising revenue |
| Sellers $n \in \mathcal{N}=\{1,\dots,N\}$ | 设置价格 $p_n$；对 prominent position 出价 $b_n$ | 最大化卖家利润 |
| Consumer | 观察 prominent seller 后决定是否继续搜索；若搜索，决定搜索顺序；最后购买或退出 | 最大化期望剩余效用 |

### 6.2 市场与匹配结构

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $N \ge 3$ | 卖家数量 | 每个卖家提供一个产品，边际成本归一化为 0。 |
| $\omega \in \mathcal{N}$ | 真实状态 | $\omega=n$ 表示卖家 $n$ 是消费者唯一匹配的卖家。 |
| $\mu_0(n)=1/N$ | 先验匹配概率 | 主模型为 uniform prior；extension 放松为 nonuniform prior。 |
| $D(p)$ | 匹配产品在价格 $p$ 下的需求 | 未匹配产品需求为 0；$D(\cdot)$ 严格递减、可微、log-concave。 |
| $p*$ | 垄断价格 | 满足 $D(p*)+p*D'(p*)=0$。 |
| $V=p*D(p*)$ | 匹配卖家的垄断收入/总利润（抽佣前） | 平台和卖家围绕这部分 surplus 分配。 |
| $U=\int_{p*}^{\infty}D(p)\,dp$ | 消费者从匹配产品中获得的净剩余 | 在价格 $p*$ 下的 consumer surplus。 |
| $c$ | 搜索成本 | 访问非 prominent seller 需要支付；假设 $0<c<U$。 |

> 直觉：模型把消费者偏好设定为“只有一个真正匹配的卖家”，从而让信息设计问题聚焦在“平台到底要不要揭示这个匹配对象”。这不是为了描述所有消费品，而是为了捕捉那些消费者需求较明确、匹配较尖锐的品类。

### 6.3 信息结构

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $S=\mathcal{N}$ | 信号空间 | 不失一般性，信号数量设为 $N$。 |
| $\pi(s\mid \omega)$ | 平台设计的信息结构 | 状态为 $\omega$ 时发送信号 $s$ 的概率。 |
| $\mu_s(n)$ | 信号 $s$ 后卖家 $n$ 是匹配卖家的 posterior belief | $\mu_s(n)=\dfrac{\pi(s\mid n)}{\sum_{j\in\mathcal{N}}\pi(s\mid j)}$。 |
| $\mu=(\mu(1),\dots,\mu(N))$ | 后验信念向量 | 重新排序后可设 $\mu(1)\ge \mu(2)\ge \cdots \ge \mu(N)$。 |

> 直觉：推荐列表可以被理解为一个 posterior belief vector。排在前面的产品不是简单“位置靠前”，而是平台通过信号让消费者和卖家共同相信它更可能匹配。

### 6.4 广告拍卖与平台收入

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| Prominent position | 免费被消费者检查的广告位 | 获胜卖家的价格和匹配情况可被消费者无成本观察。 |
| $b_n$ | 卖家 $n$ 对 prominent position 的出价 | 拍卖为 second-price auction。 |
| $\alpha \in [0,1]$ | 平台佣金率 | 平台从交易收入中抽取比例 $\alpha$，卖家保留 $1-\alpha$。 |
| $L$ | 搜索长度 | 消费者最多访问多少个卖家，包括 prominent seller。 |
| $\Pi(\mu,L)$ | 给定 posterior 和搜索长度的平台收入 | 包括交易佣金和广告收入。 |

若搜索长度为 $L=N$，消费者最终总能找到匹配卖家，广告竞争失效，平台收入为

$$
\Pi(\mu,N)=\alpha V.
$$

> 直觉：如果消费者无论如何都会继续搜索直到找到匹配，卖家输掉 prominent position 也不损失需求，因此不愿意为广告位付费。平台只能赚佣金。

若 $L=1,\dots,N-1$，平台收入为

$$
\Pi(\mu,L)=\alpha V\sum_{n=1}^{L}\mu(n)+(1-\alpha)V\mu(L+1).
$$

> 第一项是 commission revenue：消费者会访问 $L$ 个卖家，因此匹配卖家落在前 $L$ 个位置时发生交易，平台获得抽佣。第二项是 advertising revenue：边界之外的卖家若输掉广告位就不会被访问，因此会按匹配概率出价；second-price auction 下，获胜者支付下一位卖家的 bid，即 $(1-\alpha)V\mu(L+1)$。

### 6.5 博弈时间线

1. 平台承诺一个 information structure $\{\pi(\cdot\mid \omega)\}_{\omega\in\mathcal{N}}$。
2. 状态 $\omega$ 下信号 $s$ 实现；消费者和所有卖家都观察到该信号。
3. 卖家同时选择价格 $p_n$ 和广告竞价 $b_n$。
4. 平台通过 second-price auction 分配 prominent position。
5. 消费者无成本检查 prominent seller。若匹配则购买；若不匹配，则可支付搜索成本 $c$ 按 posterior belief 递减顺序继续搜索其他卖家。

### 6.6 关键假设、合理性与放松方向

| 假设 | 合理性 | 若放松可能怎样 |
|:---|:---|:---|
| 每个消费者只有一个匹配卖家 | 适合需求明确、匹配尖锐的品类，如指定品牌/规格/书名/酒店偏好。 | 若有多个匹配卖家，卖家间竞争更强，full information 更容易同时提高匹配和广告收入；文章的 i.i.d. extension 显示在部分条件下粗糙信息设计仍会出现，但机制会弱化。 |
| 平台知道匹配信息，卖家不知道 | 零售平台拥有消费者浏览、搜索、购买和转化数据，单个卖家未必能观察到个体层面的 fit。 | 若卖家也知道匹配，匹配卖家会出价更高，广告本身可能改善匹配；平台通过信息设计操纵卖家信念的空间下降。 |
| 信号是 public signal，消费者和卖家看到同一信息 | 便于刻画“推荐排序/广告展示”这类双方都能观察到的公开信息。 | 若允许 private signals，平台可能分别操纵消费者搜索和卖家竞价，利润可能更高，但均衡推理更复杂。 |
| 价格均衡为垄断价 $p*$ | 一旦消费者发现唯一匹配卖家，就不会继续找未匹配产品；卖家具有局部垄断力，类似 Diamond paradox。 | 若价格竞争或价格预期可被信息设计影响，可能出现推荐位置与价格的联动；但若均衡价格对称，主要机制仍可保留。 |
| 佣金率 $\alpha$ 外生且线性 | 现实中佣金受品类、平台竞争、议价和监管影响；外生处理便于聚焦推荐与广告的 trade-off。 | 若平台可自由设计两部收费或设 $\alpha=1$ 再补贴卖家，广告抽取 surplus 的作用会被削弱，问题可能变得平凡。 |
| 单个 prominent position，second-price auction，无 reserve price | 捕捉 sponsored placement 的基本机制。 | 现实广告拍卖有 reserve、quality score、CPC/CPA 和预算约束；文章的 two-position extension 显示主结构仍类似，但更复杂的 mechanism design 可能改变最优信息结构。 |

## 7. 分析路线图 (Roadmap of Analysis)

第一步，文章先固定任意信息结构，证明价格部分可以从问题中剥离：所有可能遇到消费者的卖家在均衡中都设垄断价格 $p*$。这让模型聚焦在信息如何影响消费者搜索和卖家广告竞价。

第二步，文章比较两个极端 benchmark：full information 和 no information。这个部分建立核心 trade-off：精准信息提高匹配效率和佣金，但让广告竞价消失；不披露信息会制造错配，却能让卖家为 prominent position 竞争。

第三步，文章把平台的信息设计问题转化为选择 posterior belief vector $\mu$ 的问题。由于主模型先验是 uniform，任意最优 posterior 的 cyclic permutations 可以构造出 Bayes-plausible 的信息结构。

第四步，文章引入 search length $L$。先分析一个 relaxed problem：假设消费者搜索长度外生固定，平台应如何分配 posterior mass。这一步提供直觉：高佣金时把概率放到会被搜索的卖家上；低佣金时把概率放到广告竞价边界上。

第五步，文章回到 endogenous search。消费者是否继续搜索必须 incentive compatible，卖家竞价也必须 incentive compatible。核心结果是：全局最优要么 full information，要么让消费者只访问 prominent seller，并使用“两个 contenders + long tail”的 noisy design。

第六步，文章做 extensions：nonuniform prior、i.i.d. independent matching、两个 prominent positions，说明主机制不是由某个单一技术假设机械产生的。

## 8. 核心分析与求解 (Analysis & Solution)

### 8.1 价格先被“消掉”：均衡价格为 $p*$

在任意信息结构下，只要卖家有正概率遇到消费者，均衡价格都是垄断价格 $p*$。

> 经济直觉：消费者一旦访问某卖家并发现它是唯一匹配产品，就没有理由继续付费搜索其他卖家，因为其他产品都不匹配。因此这个卖家面对的就是一个局部垄断需求。低于垄断价的定价会被向上偏离，平台的信息设计不会通过价格竞争产生作用，而是通过搜索顺序和广告竞价产生作用。

### 8.2 Lemma 1：消费者按 posterior belief 递减顺序搜索

给定信号后的 posterior belief $\mu$，若消费者决定继续搜索，则最优搜索顺序是先访问匹配概率最高的卖家，再访问匹配概率次高的卖家，依此类推。

> 经济直觉：虽然这里的搜索不是标准 Weitzman independent search，因为“某个卖家不匹配”会提高其他卖家匹配的条件概率，但核心排序逻辑仍成立：在任意历史下，把更高 posterior 的卖家提前访问，至少不降低消费者期望收益。这个 lemma 使平台能通过设计 posterior 直接塑造搜索顺序。

### 8.3 Lemma 2：No-information 下的 “none or all” 搜索规则

在完全不披露信息时，所有未访问卖家的匹配概率相同。若 $0<c\le 2U/N$，消费者会一直搜索直到找到匹配；若 $2U/N<c<U$，消费者不会搜索 prominent seller 之外的卖家。

> 经济直觉：没有信息时，消费者面对的是一组对称卖家。搜索成本足够低时，继续找最终一定能找到匹配，值得搜索到底；搜索成本较高时，第一个非匹配结果之后继续找的期望收益不足，消费者会直接停止。因此 no-information benchmark 呈现极端结果：要么全搜，要么不搜。

### 8.4 Proposition 1：Full information vs. no information

两个极端信息环境的比较如下：

1. 若 $0<c\le 2U/N$，full information 和 no information 给平台带来相同收入 $\alpha V$，但 no information 下消费者剩余更低，因为消费者会产生搜索成本。
2. 若 $2U/N<c<U$，full information 下平台收入为 $\alpha V$；no information 下消费者只访问随机 prominent seller，平台收入为 $V/N$。因此 full information 更优当且仅当 $\alpha N>1$。

> 经济直觉：Full information 让匹配卖家直接 prominent，交易一定发生，但匹配卖家即使输掉广告位也会被消费者找到，所以所有卖家出价为 0，广告收入消失。No information 下广告位能改变谁被消费者看到，卖家愿意出价；但 prominent seller 随机匹配，匹配概率只有 $1/N$。平台是在“更大成交概率”与“更强广告竞价”之间取舍。

**关键 trade-off：平台越精准地揭示匹配，越能提升交易佣金；但越精准的匹配信息越会削弱卖家为 prominent position 竞争的动机。**

### 8.5 从信息结构转向 posterior design

平台的完整信息设计是选择 $\pi(s\mid\omega)$。文章利用 uniform prior 和卖家对称性，把问题化简为直接选择一个 ordered posterior vector：

$$
\max_{\mu}\ \Pi(\mu) \quad \text{s.t.}\quad \mu(1)\ge \cdots \ge \mu(N)\ge 0,\quad \sum_{n=1}^{N}\mu(n)=1.
$$

> 经济直觉：只要找到一个最优 posterior $\mu*$，平台可以通过对 $\mu*$ 做 cyclic permutations 并均匀随机化来满足 Bayes plausibility。现实解释是：平台在重复交互中通过产品排名让某些位置具有更高的匹配概率，消费者和卖家从长期观察中学到这些位置对应的 posterior。

### 8.6 Search length 与平台收入公式

定义 $L(\mu,n)$ 为当卖家 $n$ 获得 prominent position 时，消费者在未找到匹配前最多会访问的卖家数量。给定搜索长度 $L$，平台收入为

$$
\Pi(\mu,L)=\alpha V\sum_{n=1}^{L}\mu(n)+(1-\alpha)V\mu(L+1),\quad L=1,\dots,N-1.
$$

> 经济直觉：若消费者最多访问 $L$ 个卖家，那么前 $L$ 个位置的总匹配概率决定交易佣金；而第 $L+1$ 个卖家的匹配概率决定 second-price auction 的价格。广告收入来自“如果输掉就不会被搜索”的边界卖家。

### 8.7 Lemma 3：外生搜索长度下的 relaxed problem

若暂时假设消费者会机械地搜索 $L$ 个卖家，则平台的最优 posterior 有两种结构：

若 $\alpha\ge 1/2$，平台把所有匹配概率放在前 $L$ 个会被搜索的卖家上：

$$
\sum_{n=1}^{L}\mu(n)=1,\quad \mu(L+1)=\cdots=\mu(N)=0.
$$

若 $\alpha<1/2$，平台让前 $L+1$ 个卖家概率相等，后面为 0：

$$
\mu(1)=\cdots=\mu(L+1)=\frac{1}{L+1},\quad \mu(L+2)=\cdots=\mu(N)=0.
$$

> 经济直觉：当佣金率高时，平台主要关心交易概率，所以把概率放在消费者会访问的前 $L$ 个卖家。佣金率低时，广告收入更重要，平台希望提高 $\mu(L+1)$，因为它决定 second-price auction 的支付；由于排序约束 $\mu(1)\ge\cdots\ge\mu(L+1)$，最大化 $\mu(L+1)$ 的方法就是把前 $L+1$ 个概率拉平。

这个 relaxed problem 的问题在于它忽略了消费者的搜索激励。如果 $\mu(L+2)=\cdots=0$，消费者在发现前面卖家不匹配后，可能会确信下一个卖家就是匹配对象，从而继续搜索。真实最优设计必须防止这种偏离。

### 8.8 Lemma 4：Two-sided incentive compatibility

在任意由 posterior $\mu$ 诱导的子博弈均衡中，赢得 prominent position 的卖家正好是搜索边界上的卖家：

$$
 n*(\mu)=L(\mu,n*(\mu)).
$$

因此平台收入可以写成

$$
\Pi(\mu)=\Pi\bigl(\mu,L(\mu,n*(\mu))\bigr).
$$

> 经济直觉：排名靠前且无论如何会被消费者访问的卖家，没有必要为 prominent position 付费；排名太靠后的卖家虽然愿意出价，但匹配概率低。均衡中获胜者必须位于“赢了就被免费访问，输了就不会被访问”的临界位置。这个临界位置把消费者搜索激励和卖家竞价激励连接起来。

### 8.9 Lemma 5：若平台想让消费者只访问 prominent seller

设

$$
\kappa_L=\frac{U-\max\{0,U-(N-L)c/2\}}{c-\max\{0,U-(N-L)c/2\}}>1,
$$

并定义

$$
\alpha*\equiv \frac{1}{1+\kappa_1}
=\frac{c-\max\{0,U-(N-1)c/2\}}{U+c-2\max\{0,U-(N-1)c/2\}}.
$$

若 $L=1$，最优 posterior 为：

当搜索成本低或佣金率高时，平台选择 full information：

$$
\mu(1)=1,\quad \mu(2)=\cdots=\mu(N)=0.
$$

当 $2U/N<c<U$ 且 $\alpha<\alpha*$ 时，平台选择

$$
\mu(1)=\mu(2)=\alpha*,\quad
\mu(3)=\cdots=\mu(N)=\frac{1-2\alpha*}{N-2}.
$$

> 经济直觉：两个高概率卖家是 contenders。平台让它们对 prominent position 有很高 winning reward，因为赢了就有 $\alpha*$ 的匹配概率；但平台同时给后面 long tail 留下一点正概率，让消费者在看到 prominent seller 不匹配时，不会确信另一个 contender 就是答案，从而不再继续搜索。这样，输掉广告位的 contender 真的失去需求，于是愿意高出价。

### 8.10 Lemma 6：若平台试图实施更长搜索长度 $L\ge 2$

当 $L\ge 2$ 且可实施时，最优 posterior 的形状更复杂：前 $L-1$ 个位置的概率呈指数下降，$\mu(L)=\mu(L+1)$，后面仍是一条均匀 long tail。

> 经济直觉：若平台允许消费者搜索多个卖家，就必须让消费者在每一步“刚好愿意继续搜下一位”，但在到达第 $L$ 个卖家后“刚好不愿意再搜”。这要求前面若干位置的信念按递推方式下降；而 long tail 仍然用于提高继续搜索的不确定性和预期成本。

虽然这种结构可行，但文章随后证明它不是全局最优。因为广告收入随 $L$ 增加而下降：消费者搜索越深，卖家输掉广告位后的损失越小，竞价越弱。

### 8.11 Proposition 2：最优 posterior belief

最终全局最优 posterior 是：

1. 若 $0<c\le 2U/N$，任何 posterior belief 都给平台相同利润 $\alpha V$。
2. 若 $2U/N<c<U$，则

$$
\mu*(1)=1,\quad \mu*(2)=\cdots=\mu*(N)=0,\quad \text{if }\alpha\ge \alpha*;
$$

而当 $\alpha<\alpha*$ 时，

$$
\mu*(1)=\mu*(2)=\alpha*,\quad
\mu*(3)=\cdots=\mu*(N)=\frac{1-2\alpha*}{N-2}.
$$

在后一种情形下，消费者的搜索长度为 1，只访问 prominent seller。

> 经济直觉：平台要么完全追求 match efficiency，要么主动限制搜索。低搜索成本时消费者自己会找完所有卖家，平台无法通过信息设计影响交易；高搜索成本时，广告收入动机让平台最优地压缩搜索长度，因为卖家只有在“输掉广告位就没有需求”时才会激烈竞价。两个 contenders 保证广告位有价值，long tail 保证消费者不继续搜。

### 8.12 Corollary 1：可实施的信息结构与均衡结果

当 $2U/N<c<U$ 且 $\alpha\ge\alpha*$ 时，最优设计是 full information：

$$
\pi*(n\mid n)=1,
\quad
\pi*(s\mid n)=0\ \text{for }s\ne n.
$$

均衡结果是：所有卖家广告出价为 0；匹配卖家获得 prominent position 并赚取 $(1-\alpha)V$；消费者获得 $U$；平台获得 $\alpha V$。

> 经济直觉：高佣金率使平台更像一个交易撮合者。它宁愿最大化匹配和交易，也不需要通过广告拍卖提取卖家 surplus。

当 $2U/N<c<U$ 且 $\alpha<\alpha*$ 时，一个最优信息设计为

$$
\pi*(n\mid n)=\pi*(n+1\mid n)=\alpha*,
$$

并且对所有 $s\ne n,n+1$，

$$
\pi*(s\mid n)=\frac{1-2\alpha*}{N-2},
$$

其中使用 cyclic indexing，即 $N+1$ 视为 1。

均衡结果是：两个 contenders 出价 $(1-\alpha)V\alpha*$，long-tail sellers 出价 $(1-\alpha)V\frac{1-2\alpha*}{N-2}$；两个 contenders 中一个赢得广告位；消费者只检查 prominent seller；平台利润为 $\alpha*V$；消费者期望剩余为 $\alpha*U$；卖家期望利润被竞争压到 0。

> 经济直觉：这个结构同时提供 winning reward 和 losing punishment。赢的 contender 有较高成交概率；输的 contender 不会被消费者继续搜索。平台借此把卖家 surplus 通过 second-price auction 提取出来。值得注意的是，低佣金区间的平台利润 $\alpha*V$ 与实际佣金率 $\alpha$ 本身无关，因为 commission 和 ad revenue 在总和上共同等于 prominent seller 匹配概率乘以 $V$。

### 8.13 Welfare implication

Full information 是 first-best：匹配概率为 1，消费者获得 $U$，交易 surplus 为 $V$，总福利为 $U+V$。低佣金区间的 noisy design 下，消费者只在 prominent seller 匹配时购买，匹配概率为 $\alpha*$，总福利为 $\alpha*(U+V)$，社会损失为

$$
(1-\alpha*)(U+V).
$$

> 经济直觉：广告位竞争本身没有创造新的匹配价值；它只是改变 surplus 在卖家和平台之间的分配。为了让这个分配机制有效，平台必须牺牲一部分匹配概率。因此 sponsored targeted ads 可以在平台最优下带来真实的 allocative inefficiency。

## 9. Extensions

### 9.1 Nonuniform prior distribution

主模型假设所有卖家先验匹配概率相同。extension 表明：当 $N$ 为奇数且 prior heterogeneity 足够小，Proposition 2 中的最优 posterior 仍然可以通过适当的 posterior permutation 实施，因此主结论保留。

> 经济直觉：uniform prior 的作用主要是让 cyclic permutation 自动满足 Bayes plausibility。若 prior 轻微偏离 uniform，平台仍可调整不同 posterior realization 的概率来匹配先验。但若 $N$ 为偶数或先验差异过大，原来的 posterior 组合可能无法精确实施。

### 9.2 Alternative match value distributions：独立匹配

文章考虑另一种设定：每个卖家与消费者独立匹配，匹配概率为 $\mu_0$。为了保持可解性，平台的信息设计被限制为每个卖家独立产生 high posterior $\bar\mu$ 或 low posterior $\underline\mu$。

核心数值结果是：当佣金率较低时，平台选择 coarse information，使 high posterior 大约卡在消费者愿意继续搜索的阈值 $c/U$ 附近，并让 low posterior 为 0；消费者仍然只访问 prominent seller。当佣金率较高时，full information 仍然最优。

> 经济直觉：即使不再是“唯一匹配卖家”，只要消费者搜索成本较高且广告收入重要，平台仍有动机把信息设计得刚好粗糙，避免消费者绕过广告位继续搜索。主模型的机制因此不是完全由唯一匹配假设机械驱动的。

当 $N\to\infty$ 时，full information 重新成为一个最优设计，因为几乎总会存在多个匹配卖家，精准披露既能提高匹配，也能保留广告竞争。

### 9.3 Multiunit position auction：两个 prominent positions

文章还考虑两个免费被消费者检查的 prominent positions，用 uniform-price auction 分配。若佣金率高，full information 最优；若佣金率低，最优 posterior 变成“三个 contenders + long tail”：

$$
\mu^\dagger(1)=\mu^\dagger(2)=\mu^\dagger(3)=\frac{1}{2+\kappa_2},
$$

其余卖家均分剩余概率。消费者只访问两个 prominent positions。

> 经济直觉：有两个广告位时，平台需要三个高概率 contenders 来形成竞争，第三个 contender 的出价决定 uniform price。结构与主模型完全平行：高概率 contenders 创造广告竞争，低概率 long tail 抑制继续搜索。平台通常受益于更多 prominent positions，因为可以从两个广告位收取总广告收入，尽管单个位置的竞价强度下降。

## 10. 比较静态汇总表 (Comparative Statics Summary)

| 参数变化 | 对最优信息设计的影响 | 对平台利润的影响 | 对消费者/社会福利的影响 | 直觉 |
|:---|:---|:---|:---|:---|
| $\alpha \uparrow$ | 更可能选择 full information；当 $\alpha\ge\alpha*$ 时完全披露 | 更依赖 commission revenue | 匹配效率提高，福利趋近 first-best | 高佣金让平台从成交中获益更多，不需要靠广告竞价抽取 surplus。 |
| $\alpha \downarrow$ | 更可能选择 noisy design：两个 contenders + long tail | 广告收入权重上升；低佣金区间利润为 $\alpha*V$ | 消费者匹配概率降为 $\alpha*$，福利损失出现 | 平台通过限制搜索使卖家竞争 prominent position。 |
| $c \downarrow$ 且 $c\le 2U/N$ | 信息设计对平台利润无影响 | 平台收入均为 $\alpha V$ | 消费者会自己搜到匹配，但 no information 下有搜索成本 | 搜索成本低时，消费者能自行恢复匹配效率，卖家广告竞价失去价值。 |
| $c \uparrow$ | $\alpha*$ 上升；固定低 $\alpha$ 下 noisy design 更容易出现 | 在 noisy region 中平台利润 $\alpha*V$ 上升 | 可能从 full information 跳到 noisy design，造成离散福利下降；在 noisy region 内匹配概率 $\alpha*$ 可上升 | 高搜索成本降低消费者绕过广告位的能力，使广告位更值钱。 |
| $N \uparrow$ | $\alpha*$ 上升；超过阈值 $2U/c$ 后 noisy design 可能出现 | 平台利用消费者搜索困难提高广告变现 | 福利对 $N$ 非单调：卖家数刚超过阈值时可能出现离散下降，之后 noisy design 内错配逐渐减少 | 更多卖家增加选择，也增加搜索困难；平台可借此抑制搜索。 |
| prominent positions 从 1 个增至 2 个 | 低佣金时由两个 contenders 变为三个 contenders | 平台总广告收入提高 | 消费者免费检查更多卖家，潜在匹配效率改善，但平台仍会使用 long tail 抑制进一步搜索 | 多个广告位需要更多 contenders 维持竞价。 |
| 数据精度提高 | 不一定继续提高平台利润；低佣金时平台只需区分 contenders 与 long tail | 边际价值有限 | 若平台战略性 withholding，消费者未必受益于更精细数据 | 平台并不总想精准指出单一最佳匹配。 |
| 隐私政策导致 cohort targeting | 可能接近平台本来会选择的 noisy/coarse design | 对平台利润影响可能有限 | 未必显著改善匹配效率；取决于是否限制了平台区分 contenders 的能力 | 平台最优信息设计本身就不是 fully personalized。 |

## 11. 主要结论与管理启示 (Main Results & Managerial Insights)

### 11.1 与 benchmark 的对比

| 信息环境 | 消费者行为 | 卖家竞价 | 平台收入 | 匹配效率 | 何时相关 |
|:---|:---|:---|:---|:---|:---|
| Full information | 直接访问匹配卖家，不再搜索 | 出价为 0 | $\alpha V$ | 最高，first-best | 高佣金率；或平台重视交易效率 |
| No information，低搜索成本 | 消费者继续搜到匹配 | 出价为 0 | $\alpha V$ | 最终匹配，但有搜索成本 | $c\le 2U/N$ |
| No information，高搜索成本 | 只访问随机 prominent seller | 所有卖家按 $1/N$ 匹配概率竞价 | $V/N$ | 低，匹配概率 $1/N$ | 广告位能影响购买时 |
| Optimal design，高佣金 | Full information | 出价为 0 | $\alpha V$ | first-best | $\alpha\ge\alpha*$ |
| Optimal design，低佣金 | 两个 contenders + long tail；只访问 prominent seller | contenders 高出价，卖家 surplus 被抽取 | $\alpha*V$ | 匹配概率 $\alpha*$ | $2U/N<c<U$ 且 $\alpha<\alpha*$ |

### 11.2 管理建议

第一，推荐算法不应在所有品类上统一最大化 prediction accuracy。高佣金品类中，精准推荐能转化为平台佣金；低佣金品类中，平台可能从更粗糙的推荐中获得更高广告收入。因此，平台内部若把 recommendation team 和 advertising team 分开优化，可能导致系统层面目标冲突。

第二，search friction 是平台设计变量。筛选器、排序页面、比较工具、默认展示数量、是否突出 sponsored products，都会改变消费者绕过 prominent position 的能力。降低搜索摩擦有利于消费者匹配效率，但可能削弱广告位价值。

第三，增加卖家数量不一定单调改善消费者福利。卖家更多通常意味着选择集扩大，但当 $N$ 超过 $2U/c$ 后，消费者更难搜索完所有卖家，平台反而可能切换到 noisy design，使匹配效率出现离散下降。

第四，数据投资的边际收益有上限。低佣金/高广告场景下，平台只需要足够的数据区分一小组 contenders 和一条 long tail，不一定需要准确识别唯一最佳匹配。因此，不是所有数据精度提升都会进入消费者推荐质量。

第五，广告位数量设计要与信息设计联动。增加 prominent positions 可能提高平台总广告收入，也可能改善消费者的免费检查范围；但平台仍有动机在 prominent positions 之外保留 long tail，以抑制继续搜索。

### 11.3 政策含义

第一，佣金监管不能孤立看。如果政策压低平台佣金率，平台可能更依赖 sponsored advertising，从而更有动机采用 noisy recommendation，降低匹配效率。

第二，隐私监管的效果不一定按“数据越少，效率越低”的简单逻辑运行。本文显示平台在低佣金情形下本来就可能选择 coarse/noisy information；因此，cohort-based targeting 可能并不会显著降低平台利润。但这不意味着隐私监管一定提升消费者福利，因为平台仍可能保留足够信息来区分 contenders 与 non-contenders。

第三，ranking transparency 和 sponsored placement disclosure 可能比单纯限制佣金更直接地触及问题核心。本文的低效率来自平台对消费者注意力和卖家信念的共同 steering，而不是来自佣金率本身。

## 12. 与相关文献的对话 (Dialogue with Literature)

### Kamenica and Gentzkow (2011), Bayesian Persuasion

共同点是都研究 Sender 如何通过信息结构影响 Receiver 的信念和行为。本文的推进在于 Receiver 不止一个：消费者和卖家同时观察平台信号，且他们的反应相互作用。消费者的搜索深度决定广告位价值，卖家的竞价又决定消费者先看到谁。因此，本文把 Bayesian persuasion 放进了一个双边平台和广告拍卖环境中。

### Athey and Ellison (2011), Position Auctions with Consumer Search

共同点是都把 sponsored position 与 consumer search 结合起来。区别在于经典 position auction 文献通常假设卖家对自身相关性有更多信息，搜索平台/拍卖者信息较少；本文相反，零售平台掌握更强的消费者—卖家匹配信息，并能用 public signal 同时改变消费者搜索和卖家竞价。这一点很重要，因为它使广告低效率不再只是竞价机制问题，而是平台信息披露策略的问题。

### Dogan and Hu (2022), Consumer Search and Optimal Information

共同点是都研究第三方信息披露如何影响 consumer search 和市场结果。区别在于 Dogan and Hu 主要关注独立产品信号结构下的 consumer search，而本文的信息设计还要影响 sellers' advertising incentives。本文因此能解释为什么平台推荐列表会呈现“排名/突出位置 + long tail”这种结构，并刻画 commission 与 ad revenue 的权衡。

### Bergemann and Bonatti (2024), Data, Competition, and Digital Platforms

共同点是都关注平台利用数据优势 steering consumers and sellers。区别在于 Bergemann and Bonatti 更强调平台如何用数据引导消费者流向广告商或非广告商，本文则内生化 on-platform consumer search，并显式建模 sales commission 和 ad auction revenue 两条收入流。这个区别使本文能讨论为什么平台可能牺牲匹配效率来增强 seller competition for prominence。

### Janssen et al. (2023), Search Platforms: Big Data and Sponsored Positions

共同点是都发现平台可能把 non-prominent firms 随机化或模糊化，以抑制消费者继续搜索并提高 auction revenue。本文的区别是把问题放到完整 information design 框架下，并引入 commission revenue 与 advertising revenue 的 trade-off。因此，本文不仅说明平台可能抑制搜索，还刻画了何时 full information 与 noisy information 分别最优。

## 13. 犀利评论 (Reviewer's Critique)

### 13.1 优点

理论贡献很清晰：本文把 recommendation 和 targeted advertising 从两个分离问题合并为一个平台 information design 问题，提出了一个非常容易记住的核心机制——平台为了卖广告位，可能故意不完全推荐最匹配产品。

方法上，文章的化简很漂亮。通过唯一匹配、uniform prior 和 cyclic permutations，作者把复杂的 Bayes-plausible information design 问题转化为选择一个 posterior vector，再进一步用 search length 来刻画消费者行为与卖家竞价。这使模型既有 closed-form 结果，又保留了足够强的经济直觉。

实践相关性也强。零售平台正在从交易佣金转向 retail media monetization，本文直接解释了为什么广告商业模式可能改变推荐系统目标，并给出关于品类佣金、搜索摩擦、seller density 和隐私政策的具体含义。

### 13.2 模型限制与假设过强处

第一，唯一匹配卖家假设很强。它让模型机制非常干净，但许多 marketing 场景中消费者可能对多个产品有正效用，甚至有多样化需求。若多个卖家都可匹配，full information 可能同时提升匹配和广告竞争，平台牺牲准确性的动机会下降。

第二，平台完全知道匹配、卖家完全不知道匹配，这给了平台非常强的信息权力。现实中卖家可能有自己的 CRM、品牌忠诚度数据、广告投放经验和转化反馈。若卖家有私有 match information，广告竞价本身也可能传递相关性，平台的 noisy information design 作用会被削弱。

第三，public signal 假设简化了现实广告系统。现实中消费者看到的是 ranking 和 disclosure，卖家看到的是 dashboard、targeting segments、bid recommendations、conversion reports；双方信号并不完全相同。Private signals 可能让平台更精细地操纵两边，但也可能引入声誉和监管问题。

第四，价格机制被刻意压平。所有卖家设垄断价 $p*$ 让文章能专注于搜索和广告，但在许多平台中价格、折扣、促销、广告和排序高度联动。若 prominent seller 因竞争而降价，消费者 welfare 和平台 trade-off 可能变化。

第五，广告拍卖机制过于简化。现实中的 sponsored search/retail media 拍卖通常有 reserve price、quality score、CPC/CPA 转换、预算约束和 repeated bidding。本文讨论了 reserve price 可能改变最优设计，但主模型没有完整处理这些制度细节。

第六，模型是静态的代表性消费者框架，没有平台声誉、消费者长期信任、卖家进入退出和跨平台竞争。若消费者长期发现推荐质量下降，平台未来流量可能受损，这会约束 noisy recommendation 的使用。

### 13.3 未来研究方向

1. **Private information design**：允许平台分别给消费者和卖家发送不同信号，研究平台是否能在不明显降低消费者匹配的情况下进一步提高广告收入。
2. **结构估计或实证检验**：利用品类层面的佣金差异、广告位价格、排名噪声、点击/转化数据，检验低佣金品类是否出现更高 sponsored density 或更低 organic relevance。
3. **内生佣金与广告机制设计**：让平台同时选择 $\alpha$、reserve price、广告位数量和信息结构，分析真实平台的 commission-advertising monetization mix。
4. **多匹配与垂直差异**：引入多个可接受产品、品牌质量差异、价格竞争和多产品卖家，检验“long tail deters search”机制在更平滑偏好结构下是否仍然存在。
5. **动态消费者信任与平台声誉**：把推荐噪声的短期广告收益与长期用户留存、信任损失放在同一模型中，研究平台何时会自我约束不做过度 noisy recommendation。
6. **政策设计**：比较佣金率限制、广告标识、ranking transparency、数据可携带和 privacy sandbox 等政策工具，研究哪类监管真正改善 match efficiency。

## 14. 可以在 seminar 上追问的问题

1. 低佣金区间的最优设计把 sellers' profit 压到 0。如果允许 seller entry 或 category participation，这个结果是否会削弱平台长期供给？
2. 文章中消费者看到 prominent seller 不匹配后不继续搜索，是由 long tail 概率制造的。现实中消费者可能使用 off-platform search 或 LLM pre-search，这会如何改变平台的设计空间？
3. 若广告排序必须标注 sponsored，消费者是否会对 prominent seller 的 posterior 做不同更新？信息设计是否仍能用同一个 public signal 表示？
4. 如果平台有长期 reputation concern，推荐噪声是否会被消费者学习出来？平台会不会在 high-value consumers 或 repeated users 上更倾向 full information？
5. 能否从平台数据中识别“战略性噪声”与“算法误差”？这可能需要同时观察 organic relevance、ad bids、commission rate 和 category-level search costs。

## 15. 最后一句话总结

本文的核心不是说“广告一定让推荐变差”，而是指出：当平台同时靠交易佣金和广告位变现时，推荐准确率本身就是一个战略选择；在低佣金、高广告价值的环境里，平台最优推荐可能故意保留噪声，以便让卖家为消费者注意力付费。

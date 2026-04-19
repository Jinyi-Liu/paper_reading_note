# Competition, Search, Learning, and Frequent Buyer Discounts as Price Discrimination

作者：James Dana（Northeastern University）、Johannes Hörner（CNRS / Toulouse School of Economics）、Anna Sanktjohanser（Toulouse School of Economics）  
年份：2026 年 4 月 5 日  
期刊：Working Paper（原文标注 *Very Preliminary*）

## 标题与元信息

### 中文摘要

本文研究一个很常见、但传统解释并不完全令人满意的现象：为什么高频购买者经常拿到更低价格？作者提出，在存在 search 或 learning frictions 的寡头市场里，答案不一定是“企业更喜欢忠诚客户”，也不一定主要是“会员计划提高了 switching costs”。相反，哪怕所有消费者在进入市场之前的估值分布完全一样、学习成本也一样，只要他们的购买频率不同，高频购买者就会因为未来购买次数更多，而更愿意去尝试新产品、学习新匹配，从而拥有更强的 outside option。结果是：他们更常搜索、更可能找到更高质量匹配、事后平均估值更高，但反而支付更低价格。进一步地，即使购买频率本身是 private information，企业也可以利用 frequent buyer discounts 对消费者进行筛选，把完整信息下的差别定价结果“实现出来”。本文分别在 experience-good 模型与 search-good 模型中建立这一机制，并说明这一逻辑在竞争市场中成立，而在作者强调的 search-good monopoly benchmark 下则不成立。

## 论文速览

| 维度 | 内容 |
|:---|:---|
| 研究问题 | 为什么高频购买者会获得更低价格？这种折扣究竟是“忠诚奖励”，还是 competition 下的 price discrimination？当购买频率不可观测时，frequent buyer discount 能否实现筛选？ |
| 研究方法 | 两个动态理论模型：一个是 experience-good model（消费后才知道匹配价值），一个是 search-good model（搜索后即可知道匹配价值）；都考察对称、平稳 equilibrium 与 comparative statics。 |
| 核心机制 | 购买频率 $\lambda$ 越高，搜索/试错的未来收益越大，因此消费者更愿意 experiment，outside option 更强；竞争厂商为留住这类买家，必须给更低价格。 |
| 最反直觉的发现 | 高频消费者在 equilibrium 中往往有更高的事后估值，但支付的价格反而更低。也就是说，“更愿意付钱的人”不一定付更高价格。 |
| 不完全信息扩展 | 在 search-good setting 下，企业可以用“第二次购买打折”的两阶段 contract 分离高频与低频买家，从而实现完整信息下的期望价格。 |
| 主要贡献 | 把 loyalty discount 的“screening / price discrimination”角色，与传统的 “switching cost / softening competition” 角色区分开来。 |
| 适用场景 | 航司常旅客计划、零售会员、咖啡连锁的 repeat-purchase rewards、数字平台上的回购优惠、任何存在试用/学习成本的 differentiated products。 |
| 阅读提醒 | 这篇 paper 还是 draft：作者明确承认有若干 proof 缺失，discount program 的 equilibrium design 也没有完成。 |

## TL;DR

这篇文章的核心不是“忠诚客户应该被奖励”，而是“高频客户更会找替代品，所以更难被拿捏”。  
因为他们买得更勤，试新产品、学新匹配更划算，所以 outside option 更强；竞争厂商只能给他们更低价格。  
因此，frequent buyer discounts 在这里首先是一个 competition-driven 的 discrimination 工具，而不只是一个培养忠诚的 marketing gimmick。

## One More Thing

这篇 paper 最值得在 seminar 或茶歇里讲的一句话是：**企业的 market power 取决于它相对 outside option 创造了多少价值，而不是它一共创造了多少价值。**  
这句话的厉害之处在于，它直接 overturn 了很多人对 loyalty pricing 的直觉。我们通常觉得，“买得越勤的人，越懂这个品类，也越喜欢这个产品，所以企业应该向他们收更高价。” 这篇 paper 说恰恰相反：正因为他们买得勤、学得快、试得多，他们更容易形成好的替代选择，所以企业反而得给他们更低价。更妙的是，作者还指出，如果所有产品对消费者的价值一起上移同样的幅度，均衡价格甚至可以不变。真正重要的不是消费者“有多爱消费”，而是“离开你以后还能去哪里”。

## 研究背景与动机 (Motivation)

### 实践痛点

现实中的 loyalty programs 和 frequent buyer discounts 非常普遍，但这些项目到底是在“奖励忠诚”，还是在“做价格歧视”，很多时候并不清楚。航空常旅客计划、超市会员价、咖啡店买多次后降价、平台型零售的重复购买优惠，看起来都像是在奖励复购；但这些工具同时也可能改变 switching costs、影响竞争强度、甚至改变哪些顾客更容易被挖走。本文抓住的痛点是：**同样是 repeat-purchase discount，它既可能是一个反竞争的 lock-in 工具，也可能是一个顺着 competition 逻辑做出来的筛选工具。**

### 理论缺口

现有文献中，相关研究大致有三条线，但都留下了空白。

1. price discrimination under competition 的文献说明，差别定价在寡头竞争中往往会侵蚀利润；
2. loyalty program 文献通常强调 switching costs、habit formation、status、convenience 等渠道；
3. search / learning 文献说明，市场摩擦会赋予企业市场力。

本文的关键缺口是：**很少有论文把“购买频率异质性”本身如何改变 search / learning incentives，从而内生地改变 outside options，再反过来改变竞争价格，单独抽出来讲清楚。**

### 核心贡献

1. **提出一个干净的机制**：消费者 ex ante 只在购买频率上不同，估值分布相同，但高频消费者因为未来回合更多，更愿意 search / learn，所以 outside option 更强。
2. **解释一个反直觉现象**：高频买家在 equilibrium 中事后平均估值更高，却支付更低价格。
3. **区分 loyalty discounts 的两种作用**：一类是 screening / price discrimination；另一类是 softening competition。本文重点识别前者。
4. **提供不完全信息实现思路**：即使企业看不到消费者类型，也可通过有限形态的 frequent buyer contract 实现完整信息价格。

## 模型设定与假设 (Model Setup & Assumptions)

### 先做一个记号清理

原文 PDF 在抽取时多处把尾分布的上横线丢掉了。为避免混淆，下面统一使用：

- $F(\theta)$：匹配价值的 CDF；
- $\bar F(\theta)=1-F(\theta)$：尾分布（survival function）。

这比直接照抄 draft 里的记号更容易读。

### 符号体系：市场与消费者模块

这一组符号描述市场环境、消费者异质性与时间结构，是整篇 paper 的骨架。

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $i \in \{l,h\}$ | 消费者类型 | $l$ 为 low-frequency，$h$ 为 high-frequency |
| $\lambda_i$ | 需求到达率 / 购买频率 | $\lambda_h > \lambda_l$，这是消费者唯一的 ex ante 异质性 |
| $\psi$ | 高频消费者占比 | 总人口中 high-frequency buyers 的比例 |
| $\sigma$ | 消费者进入/退出率 | 消费者是有限寿命，企业是无限寿命 |
| $n$ | 每个消费者对应的企业数 | 企业总量标准化后得到的竞争强度参数 |
| $r$ | 折现率 | 消费者和企业都用到 |
| $c$ | 单位成本 | 所有企业相同 |

### 符号体系：估值与匹配模块

这一组符号决定了“search / learning 为什么有价值”。

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $\theta_{ij}$ | 消费者 $i$ 对企业 $j$ 产品的匹配价值 | firm-specific valuation |
| $F(\theta)$ | $\theta$ 的累计分布函数 | 对所有类型与企业相同 |
| $f(\theta)$ | 密度函数 | 假设满足 increasing hazard rate |
| $\bar F(\theta)$ | 尾分布 $1-F(\theta)$ | 决定“好匹配”的概率 |
| $\underline \theta,\bar \theta$ | 估值支持的上下界 | 文中 search-good model 会把上界正规化为 $1$ |

### 符号体系：均衡对象与策略模块

这一组符号是“解出来的东西”。

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $p^*$ | experience-good model 中的均衡价格 | 类型可观测时可写成 $p_i^*$ |
| $\theta^*$ | experience-good model 中的最优停搜阈值 | 当前匹配值低于该阈值则继续搜索 |
| $p^{**}$ | search-good model 中的均衡价格 | 论文在该模型中给出更干净的 comparative statics |
| $\theta^{**}$ | search-good model 中的阈值 | 与 $p^{**}$ 配套 |
| $V(\theta)$ | 搜索的 continuation value | 经验品模型中消费者 outside option 的核心对象 |
| $Z(\theta)$ | 一次额外搜索的净价值 | 便于刻画 cutoff rule |
| $\phi(\theta^*)$ | outside option 的现值表达 | 企业定价时真正面对的是这个对象，而非消费者总估值 |

### 符号体系：frequent buyer discount 合约模块

这一组符号只在不完全信息扩展中出现。

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $p_H$ | 两次购买合约中的第一次价格 | 面向“愿意拿折扣合同的人” |
| $p_l$ | 平价单次购买价格 | 低频型通常更偏好这一项 |
| $d$ | 第二次购买的折扣幅度 | 第二次价格为 $p_H-d$ |
| $\tau$ | 第二次购买必须发生的期限 | 期限越短，高频型越容易从折扣中受益 |
| $A(\lambda,\tau)$ | 在期限内完成第二次购买的折现权重 | 可写为 $\int_0^\tau \lambda e^{-(r+\sigma+\lambda)t}\,dt$ |

### 博弈/决策结构

#### Players

1. 多个对称企业，销售 differentiated products。
2. 两类消费者：高频型与低频型。
3. 企业在基准模型中可观察消费者购买频率，但看不到匹配价值；在 discount 扩展中购买频率变成 private information。

#### Sequence of Events

1. 消费者进入市场，但一开始不了解企业与自己的匹配情况。
2. 在每次 demand event 到来时，消费者决定是否访问新企业。
3. experience-good model 下：消费者访问企业后先看到价格，只有买并消费以后才知道 $\theta_{ij}$。
4. search-good model 下：搜索本身就能揭示匹配价值，因此比 experience-good model 更简化。
5. 消费者基于当前匹配与 outside option 决定“留下还是继续找”。
6. 企业在对称、平稳环境中选择价格（以及扩展中的简单 frequent buyer contract）。

#### Information Structure

- 所谓“complete information”在本文里并不是 valuations 可见，而只是 **购买频率 $\lambda$ 可见、可 contractible**。
- 估值 $\theta_{ij}$ 始终是消费者私有信息。
- 基准模型里企业看不到消费者完整购买历史，因此无法直接做“新客价 / 老客价”那种 history-based pricing。
- experience-good model 中，消费者必须先访问企业才能看到价格；新企业的价格在 ex ante 不可见，这让 uninformed consumers 对小幅价格变化不敏感。

### 目标函数与约束

#### 消费者：experience-good model 下的“留存 vs 继续搜索”

当消费者已经知道自己与当前企业的匹配价值 $\theta_{ij}$，若留下来继续买，现值收益为

$$
U^{\text{stay}}(\theta_{ij},p)=
\left(1+\frac{\lambda}{r+\sigma}\right)(\theta_{ij}-p).
$$

> 直觉上，这个式子就是“当前这一单的净剩余”加上“未来重复购买的折现净剩余”。因为消费者如果决定留下，未来每次需求到来都还会从同一家买。

消费者会把这个值与继续搜索的 continuation value 比较，因而形成 cutoff rule：存在某个阈值 $\theta(p)$，使得

$$
U^{\text{stay}}(\theta(p),p) = V^*(\lambda,p^*).
$$

> 这一步是整篇 paper 的灵魂：当前匹配值不是单独决定是否留下的，真正决定去留的是“当前匹配”相对于“继续 experiment 的 outside option”有多好。

#### 企业：experience-good model 下的定价问题

在 steady state 下，企业可把自己的问题简化为

$$
\max_p \; [\sigma+\lambda \bar F(\theta(p))](p-c).
$$

> 直觉上，企业不是只在意今天这一单的 margin，而是在意：当前价格既影响每单赚多少，也影响有多少消费者会在学到匹配后留下来。$\lambda$ 越高，留住消费者的价值越大，但这些消费者也更容易因为 outside option 强而离开。

进一步，作者把问题改写成以阈值为决策对象：

$$
\max_{\theta}\; [\sigma+\lambda \bar F(\theta)](\theta-\phi(\theta^*)-c).
$$

> 这个改写揭示了经济学含义：企业实质上是在和消费者的 outside option $\phi(\theta^*)$ 赛跑。只要 outside option 变强，企业就要压低价格才能维持同样的“相对吸引力”。

#### search-good model 下的关键闭式结构

在 search-good model 中，作者得到两个非常漂亮的条件。第一个条件用来 pin down cutoff：

$$
\frac{r}{r+\lambda}s=
\int_{\theta^{**}}^{1}(\theta-\theta^{**})\,dF(\theta).
$$

> 左边是额外搜索的“有效成本”；右边是继续搜索能带来的匹配改善收益。$\lambda$ 越高，搜索成本被未来消费摊薄得越厉害，因此消费者会采用更高的 cutoff，也就是更挑。

第二个条件用来 pin down price：

$$
\frac{f(\theta^{**})}{\bar F(\theta^{**})}=
\frac{1}{p^{**}-c}.
$$

> 这看上去像一个标准 hazard-rate pricing condition，但现在 cutoff $\theta^{**}$ 是由消费者搜索行为内生决定的。于是价格不是单纯由需求曲线决定，而是由“搜索摩擦 + 竞争 + 匹配分布”共同决定。

#### 不完全信息下的两次购买折扣合同

定义在期限 $\tau$ 内完成第二次购买的折现权重为

$$
A(\lambda,\tau)=\int_0^\tau \lambda e^{-(r+\sigma+\lambda)t}\,dt.
$$

高频消费者选择“两次购买合同”而不是平价单买，需要满足

$$
(\theta-p_H) + A(\lambda_h,\tau)(\theta-p_H+d)
\ge
(1+A(\lambda_h,\tau))(\theta-p_l).
$$

低频消费者选择平价单买而不是“两次购买合同”，需要满足

$$
(1+A(\lambda_l,\tau))(\theta-p_l)
\ge
(\theta-p_H) + A(\lambda_l,\tau)(\theta-p_H+d).
$$

> 核心直觉很简单：高频型更可能在期限内用到第二次折扣，所以同一个 discount 对她更有价值。于是，哪怕企业看不到 $\lambda$，也能让消费者自己“选出自己的类型”。

### 关键假设

#### 假设 1：两类消费者的 ex ante 估值分布完全相同

- **Justification**：这是为了把所有结果都明确归因于购买频率，而不是 taste heterogeneity。
- **放松后可能的影响**：如果高频消费者本来就更喜欢该类产品，那么“高频付更低价”可能同时由 outside option 与更高基础 WTP 两个渠道共同驱动，识别会变脏。

#### 假设 2：存在 search / learning frictions

- **Justification**：没有摩擦就没有市场力；这是整篇 paper 立起来的根基。
- **放松后可能的影响**：作者明确展示，当 $s\to 0$ 时，价格收敛到成本 $c$，市场趋向完全竞争。

#### 假设 3：complete-information baseline 下购买频率可观察，但购买历史不可观察

- **Justification**：方便先把“频率如何影响 price discrimination”讲清楚，又避免引入 introductory pricing。
- **放松后可能的影响**：若购买历史也可观察，企业可做更复杂的动态定价，尤其是 first-purchase loss leader 或 tier-based pricing，均衡可能显著改变。

#### 假设 4：experience-good model 中价格在访问前不可见

- **Justification**：这样新到访消费者不会因为极小价格差就精准流向最低价企业，便于形成 stationarity。
- **放松后可能的影响**：若价格 fully observable，uninformed demand 会更敏感，竞争更激烈，部分结果可能强化，但需求动态会复杂很多。

#### 假设 5：消费者只把当前企业的匹配看作 payoff-relevant state（no recall）

- **Justification**：大幅简化动态规划和 aggregate state。
- **放松后可能的影响**：如果消费者能记住并回到旧企业，outside option 通常会更强，企业市场力可能进一步下降。

#### 假设 6：企业很多、单个企业很小

- **Justification**：这样单个企业偏离不会显著改变 aggregate state，便于求对称平稳 equilibrium。
- **放松后可能的影响**：有限企业数下，企业间战略互动、状态依赖定价、甚至 collusion 相关问题都会更突出。

#### 假设 7：experience-good model 通过特殊初始分布直接把经济放在 steady state

- **Justification**：这是技术性处理，目的是让利润函数 stationary。
- **放松后可能的影响**：若显式分析过渡动态，企业面对的新客/老客混合会随时间变化，最优价格路径可能不再 stationary。

## 分析路线图 (Roadmap of Analysis)

这篇 paper 最好按“机制 → 更清晰 benchmark → 不完全信息实现”的顺序来读。

1. **Experience-good model**  
   先在更贴近现实的环境里建立主机制：消费者必须真的买过之后才知道自己是否喜欢。这里的重点是“experiment 的价值”如何随购买频率变化。

2. **Monopoly benchmark 与 comparative statics**  
   在 experience-good model 内先看 equilibrium 与 comparative statics，再问：这种对高频买家的低价，是竞争导致的，还是任何市场结构都会出现？

3. **Search-good model**  
   接着作者切换到更简洁的 search-good model。这里搜索本身就揭示匹配价值，因此可以得到更干净的 closed-form 条件，清楚展示 $\lambda$、$s$、共同估值平移等变量如何影响均衡。

4. **Frequent buyer discount under private information**  
   最后再引入购买频率不可观测的情形。作者并没有完整求解一个丰富的 loyalty program game，而是选了一个非常克制的两次购买 contract，证明完整信息价格可以在不完全信息下实现。

5. **Conclusion + 未完成部分**  
   作者自己很坦率地说明：这还不是“关于 loyalty programs 的最终理论”，而更像是一篇把核心机制单独讲透的 working paper。

## 核心分析与求解 (Analysis & Solution)

### 先抓住主机制

在这篇 paper 里，高频消费者之所以更便宜，不是因为她们“不在乎价格”，而是因为她们**更在乎继续搜索**。  
购买越频繁，今天多试一个品牌、明天多学到一个匹配的价值就越大，因为未来能把这次试错摊在更多购买上。于是，搜索意愿上升，outside option 变强，企业想留住这类人就必须让利。

### Experience-good model：把“学习成本”放进竞争

作者先在 experience-good model 中工作。这里最关键的中间结论是：

- **informed consumers price-sensitive**：已经知道自己匹配值的消费者，会因为企业提价而更愿意离开；
- **uninformed consumers not sensitive to small price changes**：刚进入市场、还不知道匹配的消费者，由于价格不可见、匹配未知，对小幅价格变化不敏感。

这意味着企业面对的是一个混合需求：一部分顾客很容易被当前价格挤走，另一部分顾客更像“摸着石头过河”。

#### Proposition 1：存在唯一的对称、平稳 experience-good equilibrium

作者先证明（至少在 draft 的目标结构下）对称的 steady-state Markov perfect equilibrium 是唯一的，且 steady state 下，已匹配消费者的估值分布是被 cutoff 截断后的分布。

> 这一步的意义不是“结论本身很惊艳”，而是给后面的 comparative statics 提供一个干净基座：只有在平稳分布下，比较 $\lambda$ 或 $s$ 才有意义。

在建立了均衡存在性与唯一性之后，下面的结果才开始真正回答论文问题。

#### Proposition 2：购买频率越高，均衡价格越低、搜索 cutoff 越高、事后平均估值越高

在 experience-good model 中，

$$
\frac{dp^*}{d\lambda}<0,\qquad
\frac{d\theta^*}{d\lambda}>0,\qquad
\frac{d\,\mathbb E[\theta\mid \theta\ge \theta^*]}{d\lambda}>0.
$$

> 经济学直觉非常漂亮：高频消费者更愿意继续 experiment，所以她们对“当前这家店”的容忍度反而更低。她们会要求更高的匹配阈值 $\theta^*$ 才留下，于是最终留下来的匹配平均更好，事后平均估值更高。但正因为她们更容易走，企业必须降价。所以“更爱这个产品的人反而付更低价”，不是悖论，而是 competition 通过 outside option 在起作用。

#### Proposition 3：搜索/学习成本越高，价格越高，搜索越少，消费价值越低

经验品模型里，搜索成本上升时：

$$
\frac{dp^*}{ds}>0,\qquad
\frac{d\theta^*}{ds}<0,\qquad
\frac{d\,\mathbb E[\theta\mid \theta\ge\theta^*]}{ds}<0.
$$

而当 $s\to 0$ 时，均衡价格趋近于成本 $c$。

> 这其实是对全文的一次 sanity check。paper 想说的 market power 来自 search / learning frictions，那么 frictions 下降，市场当然要更竞争。更妙的是，这不仅让价格下降，也让消费者愿意更“挑”，从而匹配质量上升。

接下来，作者进一步问：企业到底是在榨取消费者总价值，还是只是在榨取“相对替代选项的优势”？

#### Proposition 4：如果所有企业对所有消费者的估值一起上移同样的幅度，价格不变

若 $\theta_{ij}=x+\hat\theta_{ij}$，其中 $x$ 对所有企业和消费者都是共同加成，则均衡价格不变。

> 这是全文最值得记住的二阶洞察。企业不会因为消费者“整体更喜欢消费”就自动提价。只要 outside options 也一起变好，当前企业相对别家的优势没变，价格就没必要变。这是对“市场力来自相对价值，而非总价值”的最强表达。

上面的命题说明了主机制，但 paper 真正想对照的是 monopoly benchmark。

#### Proposition 5：在寡头竞争下，卖家会对高频买家给更低价；在 paper 的 monopoly benchmark 里则不会

作者把竞争市场与 monopoly benchmark 对照，结论是：**price discrimination 的关键不是频率本身，而是竞争下频率如何塑造 outside option。**

> 如果消费者面对的是 monopoly，outside option 归零，那么“买得勤”本身不再给消费者额外议价能力。换句话说，本文中的 discrimination force 是 competition-driven 的。

**提醒：原文这里存在 draft 层面的不一致。**  
在 experience-good model 的 monopoly 小节中，有一段文字似乎暗示 $p_m$ 会随 $\lambda$ 下降；但后面的 Proposition 5 又明确说 monopoly seller does not discriminate。这个问题我放到文末 critique 里单独指出。就 paper 的 clean message 而言，真正严整的 monopoly non-discrimination benchmark 出现在后面的 search-good model。

### Search-good model：把机制讲得更干净

接下来作者切换到 search-good model。与 experience-good model 相比，这里搜索本身就揭示匹配价值，因此分析更简洁，也更适合做 benchmark。

#### Proposition 6：在允许企业承诺 selling mechanism 时，存在唯一的对称 stationary equilibrium outcome

在该模型下，企业对每一类消费者最终只需要一个 stationary price；作者据此证明存在唯一的对称 stationary Bayesian Nash equilibrium outcome，对应价格 $p^{**}$。

> 这一步的重要性在于：它把“复杂的动态竞争”压缩成一个非常清楚的定价对象。消费者如何搜索，最终都可以归结为一个 cutoff；企业如何定价，最终都可以归结为一个 stationary price。

作者随后进一步处理 commitment 的问题。

#### Proposition 7：即使不要求承诺，也存在一个 perfect Bayesian equilibrium outcome，使得均衡路径上的价格仍然等于 $p^{**}$

> 这说明 search-good model 的主结果并不是完全依赖“强承诺假设”。不过作者也很诚实地补充：不存在一个所有均衡路径价格都恒等于 $p^{**}$ 的 fully stationary PBE，或者至少 draft 没有把这件事完全做完。因此，我们应把这部分理解为“on-path outcome equivalence”，而不是完全刻画整个动态博弈。

有了更干净的 equilibrium 环境之后，作者重新做 comparative statics。

#### Proposition 8：在 search-good model 中，购买频率越高，价格越低、cutoff 越高、事后匹配越好

同样有

$$
\frac{dp^{**}}{d\lambda}<0,\qquad
\frac{d\theta^{**}}{d\lambda}>0,\qquad
\frac{d\,\mathbb E[\theta\mid \theta\ge\theta^{**}]}{d\lambda}>0.
$$

> 这说明主结论并不是 experience-good 设定下的偶然产物。即使把模型简化到“搜索即可知道匹配”的环境，频率越高 $\Rightarrow$ outside option 越强 $\Rightarrow$ 价格越低，这条逻辑依然成立。

#### Proposition 9：搜索成本越高，价格越高，cutoff 越低；当搜索成本趋于零时，价格趋于成本

对应地，

$$
\frac{dp^{**}}{ds}>0,\qquad
\frac{d\theta^{**}}{ds}<0.
$$

并且当 $s\to 0$ 时，$p^{**}\to c$。

> 这再次证明，paper 的市场力不是来自“消费者不知道自己喜欢什么”本身，而是来自“要知道自己喜欢什么，需要付出摩擦成本”。一旦摩擦消失，企业也就失去了定价空间。

接下来，作者把前面 Proposition 4 的洞察在 search-good model 中又做了一遍。

#### Proposition 10：共同估值平移不改变 equilibrium price

如果所有匹配值统一加上一个常数 $x$，则均衡价格不变。

> 这让全文的核心 message 从“一个有趣 comparative statics”上升为“一个定价原则”：企业定价盯着的是消费者留在本店相对去别家的净收益差，而不是消费者消费本身的绝对快乐水平。

#### Proposition 11：search-good model 给出了最干净的 monopoly benchmark——寡头会按频率歧视，monopoly 不会

在 monopoly 下，消费者 outside option 是 $0$，于是垄断者只是在解一个标准的

$$
\max_p \bar F(p)(p-c)
$$

问题，最优价格不依赖于购买频率。

> 这就是整篇 paper 最清楚的 benchmark。高频消费者之所以在 competition 中变便宜，不是因为她“本质上值得便宜卖”，而是因为竞争对手的存在让她手里多了一张牌：更高的 search / learning incentive。

### Frequent Buyer Discounts：不完全信息下如何把完整信息价格“做出来”

前面的分析都把购买频率当成可观察类型。现在作者问：如果企业看不到谁是 high-frequency buyer，frequent buyer discount 还能不能把完整信息下的价格歧视实现出来？

作者没有直接求解一个完整的 loyalty program game，而是给了一个 **两次购买合同** 的实现思路：

- 方案 A：按单次价格 $p_l$ 购买；
- 方案 B：第一次买付 $p_H$，若在期限 $\tau$ 内完成第二次购买，则第二次价格是 $p_H-d$。

关键操作是：

1. 先把低频消费者的平价价格固定在完整信息下的 $p_l^*$；
2. 再选择 $p_H$ 和 $\tau$，使高频消费者在选“两次购买合同”时的**期望单位价格**刚好等于完整信息下的 $p_h^*$；
3. 当 $\tau$ 足够短时，高频型更可能在期限内用到第二次折扣，因而愿意选折扣合同；低频型则更可能放弃，转而选平价单买。

#### Implementation Result：存在一类简单 frequent buyer contract，可以在不完全信息下实现完整信息价格

作者的结论是：对于这类非常克制的 contract design，**答案是 yes**。

> 这个结果的意义不在于“现实里会员计划就这么设计”，而在于它证明了本文主机制不依赖于企业直接观察购买频率。企业只需要提供一个利用高频型更高回购概率的 contract menu，消费者就会自己筛选自己。

### 这里的关键 trade-off 必须单独拎出来

**Trade-off 1：消费者是在“当前匹配”与“继续学习更好匹配”之间做选择。**  
频率越高，继续学习的 option value 越大。

**Trade-off 2：企业是在“提高当期 margin”与“避免把 informed 高频买家逼走”之间做选择。**  
频率越高的买家越难被高价收割。

**Trade-off 3：frequent buyer discount 既可以用来 screening，也可以用来 softening competition。**  
本文主要解决前者，后者只点到为止。

## 比较静态汇总表 (Comparative Statics Summary)

| 参数变化 | 对价格的影响 | 对 cutoff / 搜索强度的影响 | 对事后匹配价值的影响 | 直觉 |
|:---|:---|:---|:---|:---|
| $\lambda \uparrow$ | $p^* \downarrow,\; p^{**}\downarrow$ | $\theta^* \uparrow,\; \theta^{**}\uparrow$ | $\mathbb E[\theta \mid \theta \ge \theta^*] \uparrow$ | 高频买家把试错收益摊到更多未来购买上，outside option 更强 |
| $s \uparrow$ | $p^* \uparrow,\; p^{**}\uparrow$ | $\theta^* \downarrow,\; \theta^{**}\downarrow$ | 下降 | 搜索/学习越贵，消费者越不愿换，企业市场力越强 |
| 共同估值平移 $x \uparrow$ | 价格不变 | cutoff 不变（以净相对价值看） | 绝对估值上升 | 企业在乎的是相对 outside option 的优势，而不是总价值 |
| $s \to 0$ | $p^{**}\to c$（experience model 也趋向完全竞争） | cutoff 逼近最优匹配 | 匹配更好 | 摩擦消失，市场力消失 |
| competition $\to$ monopoly | 高频折扣消失（search-good benchmark） | outside option 变弱 | 不一定改善 | 本文中的 discrimination force 来自竞争，而不是频率本身 |

## 主要结论与管理启示 (Main Results & Managerial Insights)

### 与 benchmark 的对比

| 直觉上的 benchmark | 本文揭示的结果 |
|:---|:---|
| 高频买家更喜欢产品，所以应该收更高价 | 高频买家更会 search / learn，所以反而更难被高价拿捏 |
| loyalty programs 主要通过提高 switching costs 获利 | loyalty discounts 也可以只是一个 screening / price discrimination 工具 |
| 只要消费者总价值更高，企业就能提价 | 如果 outside option 同步上升，企业未必能提价 |
| monopoly 和 competition 使用会员折扣的逻辑差不多 | 本文强调：给高频买家低价的核心驱动力是 competition，而不是 monopoly extraction |

### 管理启示

1. **别只看 WTP，要看 outside option。**  
   对高频用户定价时，管理者不应只问“这类人有多值钱”，还要问“这类人有多容易继续 search / experiment”。

2. **高频折扣未必是在补贴忠诚，也可能是在预防流失。**  
   如果一个品类的匹配不确定性高、消费者学习快，那么 repeat-purchase discount 更像 retention pricing。

3. **想做 screening，就把未来价格锁住。**  
   本文的两次购买合约之所以能 cleanly 实现 screening，是因为第二次价格在第一单时就锁定了。若未来只是发 coupon、价格不锁，discount 很容易变成 switching-cost 工具。

4. **在低摩擦数字环境里，忠诚计划对价格的支撑能力更弱。**  
   当搜索成本低、试新产品容易时，paper 预测价格会更贴近成本，loyalty program 更难成为高价的护城河。

5. **CRM 数据最有价值的变量，不只是“买了多少”，还包括“探索倾向有多强”。**  
   在本文机制下，频率只是探索倾向的 proxy。现实里，点击、试用、跨品牌购买、换购速度等都可能是定价的更直接信号。

## 与相关文献的对话 (Dialogue with Literature)

| 相关论文 | 共同关注点 | 本文推进/区别在哪里 | 为什么重要 |
|:---|:---|:---|:---|
| Anderson & Renault (1999) | search costs、差异化产品、消费者搜索 | 那篇是静态 search-good 框架；本文变成动态 repeat-purchase 环境，并加入购买频率异质性与 learning/experimentation 逻辑 | 这让“谁更愿意搜索”成为内生对象，而不是统一给定的 search intensity |
| Caminal & Matutes (1990) | loyalty / repeat-buyer policy 与竞争 | Caminal & Matutes 更强调 loyalty policy 如何提升 switching costs、并可能影响竞争强度；本文则把“高频折扣作为筛选工具”的渠道单独剥离出来 | 它提醒我们：不是所有 loyalty discounts 都是在 lock-in 客户 |
| Kim, Shi & Srinivasan (2001) | reward programs、重度消费者、竞争 | Kim et al. 的结果很大程度上依赖“重度消费者也更不 price sensitive”；本文刻意把 ex ante valuation 分布保持一致，只让 $\lambda$ 不同 | 这使本文的 heavy-user discount 机制更干净：不靠 exogenous taste 差异，只靠 frequency 改变 outside option |
| Fong & Liu (2011) | loyalty rewards 可能促进 collusion / soften competition | Fong & Liu 研究的是 loyalty rewards 如何让 business stealing 更难；本文承认这种渠道存在，但通过锁定第二次价格的 contract 暂时把它排除 | 因此本文得到的是“纯 screening 效应”，有助于和反竞争效应区分 |

## 犀利评论 (Reviewer's Critique)

### 优点

**理论贡献**  
这篇 paper 最强的地方在于，它把一个经常被 loyalty / switching cost 语言模糊处理的问题，提炼成了一个非常清楚的定价机制：**购买频率影响搜索激励，搜索激励影响 outside option，outside option 再反过来决定竞争价格。**

**机制创新**  
“高频消费者事后估值更高却支付更低价格”这个结果很反直觉，但一旦用 outside option 来看又极其自然。尤其是“共同估值平移不改变价格”这一点，非常有力量。

**实践相关性**  
对于会员计划、复购折扣、app 内 repeat-purchase rewards，这篇 paper 提供了一个和“培养忠诚”完全不同的解释框架，十分适合启发后续 empirical work。

### 模型限制 / 假设过强

1. **作者自己已经承认 paper 未完成。**  
   缺 proof、没做 experience-good model 下的 frequent buyer discount、没有 endogenous program design、也没有分析更现实的 loyalty program equilibrium。这些都不是边角料，而是 paper 走向发表版必须补上的主体部分。

2. **experience-good model 的 monopoly benchmark 存在 draft 不一致。**  
   在 §3.3 有一段文字似乎推导出 $p_m$ 随 $\lambda$ 下降；但 Proposition 5 又说 monopoly seller does not discriminate。后面的 search-good model 与 conclusion 明显支持“monopoly 不歧视”的 clean benchmark。这个不一致需要作者明确修正，否则会削弱整篇 paper 的可信度。

3. **若干技术性假设很重。**  
   例如：no recall、消费者历史不可见、steady-state 初始分布被人为设定、企业很多且很小。这些假设当然有助于 tractability，但也意味着 paper 目前更像“机制论文”，离一个全面的 loyalty-program theory 还有距离。

4. **不完全信息扩展过于克制。**  
   两次购买合约很好地说明了 implementability，但还不是一个完整的 dynamic screening model。现实里的 loyalty programs 通常是 points、tiers、status、coupon、personalized offers 的混合物，而不是二元菜单。

5. **缺少 welfare / policy 讨论。**  
   既然作者已经碰到了“discounts 可能 screening，也可能 soften competition”这条边界，那么 welfare 与 antitrust implications 本应是一个很自然的下一步，但 draft 还没有展开。

### 未来方向

1. **完整求解购买频率不可观测时的动态 screening equilibrium**  
   不只是证明实现性，而是让企业内生选择 discount schedule、期限、门槛和承诺方式。

2. **把 frequent buyer discounts 正式并入 experience-good model**  
   这将是 paper 机制上最自然也最重要的扩展，因为现实里很多产品的“喜欢不喜欢”确实只有消费后才知道。

3. **分析 richer loyalty instruments**  
   例如 points、等级制度、滚动 coupon、可叠加奖励、会员 status。这样才能真正讨论 screening 与 switching-cost / collusion channels 如何共存。

4. **做有限企业数与异质企业的扩展**  
   当前的大量对称性与“小企业”假设淡化了战略互动。若企业品牌力不同、价格可见、市场份额有限，结果可能更加丰富。

5. **做 empirical / structural test**  
   用航司、零售会员、咖啡连锁或电商复购数据，检验“高频消费者是否更愿意 experiment、是否真的拥有更强 outside option、以及企业是否因此给她们更低 price path”。

## 最后一句话：这篇文章到底做了什么？

它不是在说“loyalty program 一定提高利润”或者“会员折扣一定是反竞争的”。  
它真正做的是：**在 search / learning frictions 下，证明高频购买者会因为更愿意 experiment 而拥有更强 outside option，因此在竞争市场里反而拿到更低价格；而 frequent buyer discounts 可以成为实现这种 price discrimination 的工具。**  
把这句话读懂，基本就抓住了整篇 paper。


- [x] 机制看着比较有趣，但估计还是挺难证明了
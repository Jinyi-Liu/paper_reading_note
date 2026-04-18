# Limits of Disclosure in Search Markets

Raphael Boleslavsky（Kelley School of Business, Indiana University）, Silvana Krasteva（Department of Economics, Texas A&M University）  
年份：2025  
期刊：Working Paper / arXiv preprint（未刊）

## 中文摘要

本文研究搜索市场中的竞争性信息披露。在这个市场里，一部分消费者是 savvy consumers，他们搜索没有成本，因此会看遍所有商家；另一部分是 inexperienced consumers，他们搜索有正成本，因此是否继续搜索取决于当前拿到的信息。每家企业都可以设计消费者在访问自己时看到的信息结构，也就是可以选择说多清楚、说多含糊。文章表明：当市场同时存在这两类消费者时，均衡不会走向完全披露，而是出现系统性的部分披露。具体地，savvy 消费者推动企业更透明，inexperienced 消费者则推动企业隐瞒信息；二者共同作用下，企业会特别扭曲保留值附近的信息，把略低于保留值的真实估值与更高估值混在一起，从而诱导 inexperienced 消费者停止搜索。在大市场里，这种低估值隐瞒不会消失，反而会稳定存在：企业会隐瞒所有低于保留值的估值，因此市场竞争再激烈，也不必然带来完全透明。文章进一步发现，inexperienced 消费者只会在小市场中积极搜索，在大市场中反而总是在第一家停下，这就是本文提出的 “paradox of choice”。此外，搜索成本对信息性的影响是非单调的：当搜索成本本来就低时，进一步降低成本会提高信息性和福利；但当搜索成本本来就高时，进一步降低成本反而会促使企业更强地扭曲信息。

## 论文速览表格

| 维度 | 内容 |
|:---|:---|
| 研究问题 | 当企业既想吸引会比价的 savvy 消费者，又想截留有搜索摩擦的 inexperienced 消费者时，竞争性信息披露会长成什么样？竞争和搜索成本如何影响透明度、搜索行为与福利？ |
| 研究方法 | 纯理论模型；把 Bayesian persuasion / information design 嵌入 Weitzman 式搜索模型；求解 pure-strategy symmetric Perfect Bayesian equilibrium。 |
| 核心机制 | **savvy 消费者奖励真披露，inexperienced 消费者奖励隐瞒。** 企业会把“略低于保留值”的坏消息向上池化，使新手误以为“已经够好了，不必再搜”。 |
| 核心发现 | 均衡是部分披露而非完全披露；大市场中企业一定隐瞒所有低于保留值的估值；新手只在小市场中积极搜索；竞争越强，老手越好，但新手可能更差；搜索成本效应非单调。 |
| 理论文献贡献 | 把无搜索摩擦的竞争性披露文献，与有搜索摩擦的搜索文献接起来；说明“竞争增强 = 更透明”在异质消费者环境里不再成立。 |
| 适用场景 | freemium 软件试用、汽车试驾、房地产展示、旅游与电商比较平台、任何“商家可控制展示信息、消费者需要继续搜”的环境。 |
| 一句话定位 | 这篇 paper 研究的不是“企业会不会披露”，而是“在谁会继续搜、谁不会继续搜的前提下，企业会把哪一段信息说清楚、把哪一段故意说糊”。 |

## TL;DR

这篇文章最重要的结论是：市场里只要同时有会比价的老手和怕麻烦的新手，竞争就**不会**自动把信息逼到完全透明。相反，在大市场里，企业会系统性地把“略差但不至于太差”的信息藏起来，让新手在第一家就停下。结果是，竞争越强，savvy 消费者越受益，但 inexperienced 消费者反而可能更吃亏。

## One More Thing

本文最值得在 seminar 或茶歇里拿出来讲的一句 insight 是：**“更多选择，未必带来更多搜索；它可能让企业更有动力把信息做得刚刚好，恰好让新手不再继续比较。”** 通常我们把 “choice overload” 解释成消费者脑子累了、看不动了，但这篇 paper 说，哪怕消费者完全理性，这种现象也会内生出现。不是消费者变笨了，而是企业看准了“你再往下搜的门槛”，然后把信息设计成正好把你拦在第一家。

## 研究背景与动机 (Motivation)

### 实践痛点

现实中的很多企业并不是简单地“告诉你产品质量”，而是在**控制你如何知道产品质量**。软件公司的免费试用会突出某些功能、隐藏限制；汽车经销商通过试驾路线与时长放大卖点；房产中介强调采光与地段，却淡化噪音、通勤与硬伤。问题不只是“披露多少”，而是“披露成什么形状”，以及这种披露如何改变消费者是否继续搜索别家。

这在运营与营销上很关键。对于经验丰富、愿意多看多比的消费者，企业要靠更清晰的信息竞争；但对搜索成本高、容易在第一家停下的消费者，企业更想把信息控制在“别太差，但也别太真”的区间。本文抓住的正是这种现实里的双重激励。

### 理论缺口

现有文献大致分成两类。第一类是无搜索摩擦的竞争性信息披露：当消费者会看遍所有选项时，竞争通常推动完全披露。第二类是有搜索摩擦的搜索模型：当所有消费者都有正搜索成本时，均衡可能退化为 informational Diamond paradox，新手第一家就停下。本文指出，真正有意思、也更接近现实的情况，是两类消费者同时存在：一部分人会看遍市场，一部分人不会。

缺口就在这里。过去文献要么把消费者都当“老手”，要么都当“新手”；要么把信息设计和搜索分开，要么不处理企业对信息的策略操纵。本文把这几块拼到了一起。

### 核心贡献

1. 提供了一个把 information design 嵌入搜索市场的统一框架，刻画企业如何在两类消费者之间权衡披露与隐瞒。
2. 证明了**唯一对称均衡**是部分披露，并且扭曲总是围绕 inexperienced 消费者的 reservation value 出现。
3. 发现了一个非常反直觉的结果：**大市场不一定更透明，反而会让新手更不搜索**，即本文的 paradox of choice。
4. 证明搜索成本对信息性和福利的影响是**非单调**的，而不是“搜索更便宜就总是更好”。

## 模型设定与假设 (Model Setup & Assumptions)

### 6a. 符号体系

#### 模块 A：市场与价值分布

这一组符号描述市场结构与消费者对产品的原始估值。

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $n$ | 企业数量 | 水平差异化的 $n$ 家企业，每家卖一个产品 |
| $V_i \in [0,1]$ | 消费者对企业 $i$ 产品的真实估值 | 对不同企业和消费者 iid |
| $F(\cdot)$ | 估值分布函数 | 连续、无原子、全支撑 |
| $f(\cdot)$ | 估值密度函数 | 有限密度 |
| $\mu$ | 先验均值 | $\mu = \mathbb E[V_i]$ |
| price $=0$ | 价格归一化为 0 | 企业目标变成最大化成交概率 |

#### 模块 B：消费者类型与搜索

这一组符号描述消费者异质性和搜索技术。

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $\alpha$ | inexperienced 消费者比例 | 私下知道自己有正搜索成本 |
| $1-\alpha$ | savvy 消费者比例 | 搜索成本为 0（或弱负），因此会看完所有企业 |
| $s \in (0,\mu)$ | inexperienced 消费者的搜索成本 | 主模型里是单点成本 |
| $r$ | inexperienced 消费者的 reservation value | 来自 Pandora’s Rule 的最优停止阈值 |
| $\eta$ | 单个企业被 inexperienced 消费者访问的概率 | 由搜索停止规则内生决定 |

#### 模块 C：信息设计与后验分布

这一组符号描述企业操纵信息的对象。

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $S_i$ | 企业 $i$ 的信号空间 | 企业可自由设计 |
| $G_i(\cdot)$ | 企业 $i$ 诱导出的 posterior mean 分布 | 选择对象，不直接选信号而选后验均值分布 |
| $G(\cdot)$ | 对称均衡下共同的 posterior mean 分布 | 所有企业在均衡中相同 |
| $v$ | posterior mean realization | 消费者购买决策只取决于它 |
| $\text{MPC}(F)$ | mean-preserving contraction of $F$ | Bayes-plausibility 约束，表示信号不能凭空创造均值 |

#### 模块 D：均衡结构中的阈值

这一组符号专门用来描述均衡披露的形状。

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $v_L$ | lower disclosure threshold | 在其下可能 truthful disclosure |
| $v_H$ | upper contact / disclosure threshold | 在其上恢复 truthful disclosure |
| $v_T$ | $G(\cdot)$ 支持集上界 | 可能小于 1 |
| $\beta$ | 仿射区间斜率参数 | 控制 $[r,v_H]$ 上的池化强度 |
| $\alpha^e$ | 企业在“被访问”条件下，访客是 inexperienced 的后验概率 | 由 Bayes rule 决定 |

### 博弈 / 决策结构

**Players**：$n$ 家企业、两类消费者（savvy 与 inexperienced）。

**Sequence of Events**：

1. 每个产品对每个消费者的真实估值 $V_i$ 从 $F$ 独立抽取，但一开始没人知道 realization。
2. 消费者选择一家企业访问。
3. 一旦某企业被访问，它选择一个信息结构，等价地选择一个 posterior mean 分布 $G_i(\cdot)$。
4. 消费者观察该企业的 posterior mean realization $v_i$。
5. 若未访问完所有企业，inexperienced 消费者决定停止还是继续；savvy 消费者继续直到看完全部。
6. 停止时，从已访问企业中选 posterior mean 最高者购买；若全部访问完，则选 realization 最高者。

**Information Structure**：

- 企业只知道“自己被访问了”，**不知道**消费者是 savvy 还是 inexperienced，也**不知道**消费者目前搜到第几家。
- 消费者知道自己类型，且访问企业后才看见该企业的信息结构与 realization。
- 搜索是 undirected search：企业不能事先公开承诺一个所有人都先看到的披露结构。

### 目标函数与约束

#### inexperienced 消费者的最优停止条件

$$
\int_r^1 (v-r)\, dG(v) = s.
$$

> 直觉上，这个方程把“再多搜一家可能带来的期望增益”与“多搜一家的成本”对齐。$r$ 越高，说明消费者越挑；$s$ 越大，说明继续搜索越不值得。

#### 企业被访问后的成交概率

企业对访问它的消费者，若 realization 为 $v$，其期望收益（即成交概率）为

$$
u(v)=
\begin{cases}
\left(\dfrac{\alpha^e}{\eta}+1-\alpha^e\right)G(v)^{n-1}, & v<r,\\[6pt]
\alpha^e + (1-\alpha^e)G(v)^{n-1}, & v\ge r.
\end{cases}
$$

> 这条式子是全文的发动机。关键不在于它多复杂，而在于它在 $r$ 处有一个**向上的跳跃**。因为只要 $v$ 刚好跨过 $r$，inexperienced 消费者就会立刻停下并购买该产品，所以企业会拼命把一些“略低于 $r$”的坏消息往上抬。

#### 企业的信息设计问题

$$
\max_{\hat G_i \in MPC(F)} \int_0^1 u(v)\, d\hat G_i(v).
$$

> 企业不是在直接卖更高质量，而是在设计“消费者看到什么样的后验均值分布”。约束 $\hat G_i \in MPC(F)$ 表示企业可以模糊、池化、压缩信息，但不能违反 Bayes-plausibility；也就是说，它可以“说得含糊”，但不能“凭空造均值”。

#### 企业对来访者类型的后验信念

$$
\eta = \frac{1-G(r)^n}{n(1-G(r))}, \qquad
\alpha^e = \frac{\alpha \eta}{\alpha \eta + (1-\alpha)}.
$$

> $\eta$ 是 inexperienced 消费者在均衡中会不会继续搜所决定的访问概率；$\alpha^e$ 则表示“被访问”本身向企业透露了多少有关消费者类型的信息。大市场里，企业几乎可以肯定来访者是 savvy，但这**并不**意味着企业会完全透明，因为对低 realization 来说，争取 savvy 成交的概率依然很低。

### 关键假设

1. **价格外生且归一化为 0。**  
   合理性：作者希望把注意力集中在“信息披露”而不是“价格竞争”。  
   若放松：若价格也内生，企业会同时通过价格与信息分流两类消费者，结论可能更复杂，也可能出现“高价 + 高透明”与“低价 + 低透明”的联合筛选。

2. **消费者风险中性，因此只关心 posterior mean。**  
   合理性：这让信息设计问题可以被重写为选择 $G(\cdot)$。  
   若放松：若消费者风险厌恶或在意高阶矩，企业可能不仅操纵均值，还会操纵分散度与尾部风险。

3. **两类搜索成本：一类为 0，一类为正。**  
   合理性：这是最简约也最干净地抓住“会看遍市场的人”和“可能中途停下的人”的方式。  
   若放松：文末 extension 表明，只要 inexperienced 类型的最小搜索成本仍严格为正，大市场里“隐瞒低估值”仍然稳健。

4. **企业在被访问时才决定信息结构，且看不到消费者类型和搜索历史。**  
   合理性：贴近很多线上展示、门店介绍、试驾试用等场景。  
   若放松：若企业能观察搜索阶段或定向展示，可能出现更强的个性化说服和更复杂的动态筛选。

5. **$F(\cdot)^{n-1}$ 弱凸。**  
   合理性：这样在无摩擦 benchmark 中，竞争会推动 full disclosure，便于凸显“只因为引入异质搜索成本，结果就变了”。  
   若放松：作者指出核心机制仍在，但远离 reservation value 的披露结构会更复杂，不一定是全文这种干净的 truthful/pooled 组合。

## 分析路线图 (Roadmap of Analysis)

1. **先把消费者搜索和企业收益写清楚。**  
   作者先给定一个候选对称分布 $G(\cdot)$，推出 inexperienced 消费者的 reservation rule、企业被访问的概率、以及企业在 realization 为 $v$ 时的成交概率 $u(v)$。

2. **再看两个 benchmark。**  
   一端是只有 savvy 消费者：竞争推动 full disclosure。另一端是只有 inexperienced 消费者：出现 informational Diamond paradox，消费者第一家就停下。

3. **接着把 reservation value 暂时外生化。**  
   这一步的目的是先抓住“均衡披露到底长什么样”，即 Proposition 1 和 Proposition 2：围绕 $r$ 的 gap 和 pooling 结构。

4. **然后把 reservation value 内生化。**  
   用搜索方程把企业披露和消费者停止规则扣在一起，形成唯一 fixed point，对应 Proposition 3。

5. **最后做比较静态。**  
   分别看市场规模 $n$、搜索成本 $s$、以及 extension 里的成本分布 $K(\cdot)$ 如何改变信息性、搜索行为与两类消费者福利。

一句话概括全文逻辑：**先刻画“为什么会在 $r$ 附近扭曲”，再刻画“扭曲会扭成什么形状”，最后看这种形状如何随市场与搜索环境变化。**

## 核心分析与求解 (Analysis & Solution)

### 先看两个 benchmark：为什么主模型一定既不像 full disclosure，也不像完全不披露

#### Lemma 1：只有 savvy 消费者时，均衡是 full disclosure

当 $\alpha=0$ 且 $F(\cdot)^{n-1}$ 凸时，唯一对称均衡是 $G(\cdot)=F(\cdot)$。

> 直觉：所有消费者都会看完市场，企业只有把真实高价值如实讲出来，才更容易在最终比较中胜出。因为没有人会在中途停下，所以“诱导停止搜索”这个动机完全消失，剩下的只有“争取在最终排名里赢”。

#### Lemma 2：只有 inexperienced 消费者时，均衡退化成 informational Diamond paradox

当 $\alpha=1$ 且搜索成本为正时，均衡满足 $G(\cdot)$ 在 $r^*=\mu-s$ 以下不放任何质量，消费者只访问第一家。

> 直觉：只要企业能保证消费者第一次看到的 posterior mean 不低于保留值，消费者就没理由再搜。于是企业最希望做的是“别让坏消息触发继续搜索”。这就是搜索文献里的 informational Diamond paradox。

### 关键 trade-off

**主模型的核心张力是：为了抓住 inexperienced 消费者，企业想隐瞒略差的信息；为了赢得 savvy 消费者，企业又必须对真正高价值保持相当程度的透明。**

这就是为什么均衡不会走到两端：既不会像 $\alpha=0$ 那样完全透明，也不会像 $\alpha=1$ 那样彻底不透明。

### Proposition 1：先固定 reservation value，均衡披露一定长成“真披露 + gap + 向上池化”的形状

在正式求 fixed point 之前，作者先把 $r$ 当作外生。此时若对称均衡存在，它必须满足：

$$
G(v)=
\begin{cases}
F(v), & v\le v_L,\\
F(v_L), & v\in (v_L,r),\\
\min\{(F(v_L)^{n-1}+\beta(v-r)),1\}^{1/(n-1)}, & v\in [r,v_H],\\
F(v), & v\in (v_H,1].
\end{cases}
$$

这意味着：在 $v_L$ 以下可以 truthful disclosure；在 $(v_L,r)$ 出现一个 gap（这段真实估值被隐藏）；而这段被隐藏的质量被池化到 $r$ 以上的区间。

> 直觉：企业最想隐藏的，不是“特别差”的估值，也不是“特别好”的估值，而是**刚刚低于消费者停止门槛**的那一段。因为把这段真实说出来，最容易触发继续搜索；但只要把它和一些更高值池化，形成一个略高于 $r$ 的 posterior mean，消费者就会当场停下。与此同时，太高的估值还是值得如实说，因为那是争夺 savvy 消费者的武器。

### Proposition 2：当外生 reservation value 改变时，披露形状如何变化

在 Proposition 1 刻画了均衡形状之后，Proposition 2 进一步说明：给定外生 $r$，均衡不仅存在且唯一，而且有一个阈值 $\bar r(n,\alpha)\in(0,\mu)$：

- 当 $r\le \bar r(n,\alpha)$ 时，均衡 **no disclosure at the bottom**，即 $v_L=0$。
- 当 $r> \bar r(n,\alpha)$ 时，均衡 **disclosure at the bottom**，即 $0<v_L<r$，并且 $v_L(r)$ 随 $r$ 上升。
- 当 $r\to 0$ 或 $r\to 1$ 时，均衡都收敛到 full disclosure。

> 直觉：如果消费者的保留值很低，那么低于它的 realization 本来就几乎没机会卖出去，不值得如实披露，于是企业直接把整段低值往上池化。反过来，如果保留值较高，那么低值 realization 仍有机会在“消费者搜完再回头”的情况下成交，因此 truthful disclosure 变得有价值。这个结果很漂亮，因为它说明**信息扭曲不是越高越好，而是最集中发生在中间区域**；当保留值走向两端时，扭曲反而消失。

### Proposition 3：把 reservation value 内生化后，主模型有唯一均衡

前两个命题只是把 $r$ 当作外生参数。接下来，Proposition 3 用搜索方程把 $r$ 内生化，得到唯一均衡 $G^*(\cdot)$ 与唯一的 $(v_L^*,v_H^*,\beta^*,r^*)$。核心结论是：

- 若 $\bar r(n,\alpha)\ge \mu-s$，则均衡 **no disclosure at the bottom**，即 $v_L^*=0,\; r^*=\mu-s$。
- 若 $\bar r(n,\alpha)<\mu-s$，则均衡 **disclosure at the bottom**，即 $v_L^*>0,\; r^*>\mu-s$。
- 并且 $r^*<r^{fi}$，也就是内生均衡下的保留值低于 full-information benchmark。

> 直觉：这一步的实质，是把“企业会如何扭曲信息”与“消费者看到这种扭曲后会把停止阈值调到哪里”联立起来。均衡不是单边决定的，而是一个 fixed point：企业知道消费者会怎样停，消费者也预期企业会怎样说。最终的 $r^*$ 比 full information 更低，说明消费者在扭曲信息环境里变得更容易停下。

### Proposition 4：市场规模的影响——大市场更竞争，但不更透明

有了唯一均衡之后，作者开始做最重要的比较静态。Proposition 4 说明，存在一个有限阈值 $\bar n\ge 2$，使得：

- 当 $n\ge \bar n$ 时，均衡 **no disclosure at the bottom**，即 $v_L^*=0,\; r^*=\mu-s$。
- 当 $n<\bar n$ 时，均衡 **disclosure at the bottom**，即 $v_L^*>0,\; r^*>\mu-s$。
- 当 $n>\bar n$ 时，信息性随 $n$ 提高，但**不会**收敛到 full disclosure。
- inexperienced 消费者只有在 $n<\bar n$ 时才会以正概率访问多于一家企业。
- savvy 消费者的福利随 $n$ 上升；inexperienced 消费者在小市场中的福利，反而高于大市场。

> 直觉：这篇 paper 最反直觉的地方就在这里。通常我们以为“市场越大，竞争越激烈，企业越透明”。本文说，不对。大市场里，单个企业若如实披露一个低 realization，几乎注定输给大量竞争对手；但如果把这段低 realization 往上池化，它至少还能稳稳拿下偶尔路过的 inexperienced 消费者。因此，**竞争越强，企业越有动力对低值做系统性隐瞒**。  
> 对 inexperienced 消费者来说，这直接带来 paradox of choice：小市场时坏初始抽样会促使她继续搜；大市场时因为企业根本不让你看到“足够坏到值得继续搜”的 realization，你反而总在第一家停下。选择变多了，搜索反而变少了。

#### Infinite market 的极限结果

在 $n\to\infty$ 时，均衡极限分布非常尖锐：

$$
G^\infty(v)=
\begin{cases}
0, & v\in[0,\mu-s),\\
F(v_H^\infty), & v\in[\mu-s,v_H^\infty),\\
F(v), & v\in[v_H^\infty,1],
\end{cases}
\qquad \text{where } \mathbb E[V\mid V<v_H^\infty]=\mu-s.
$$

> 直觉：无限竞争下，企业对低值不是“少说一点”，而是“全部往上抬到保留值附近”；但为了争夺 savvy 消费者，对高值又必须保留透明。这就是为什么极限均衡既不像 frictionless benchmark 的 full disclosure，也不像 Stahl (1989) 那样完全朝“垄断型剥削”收缩。

### Proposition 5：搜索成本的影响是非单调的

在市场规模之后，作者研究搜索成本 $s$。结论分两段：

1. 当 $s\to 0$ 或 $s\to \mu$ 时，均衡都收敛到 full disclosure。
2. 存在两个阈值 $0<\underline s \le \bar s<\mu$：
   - 若 $s<\underline s$，进一步降低搜索成本会提高信息性，而且在足够低的范围内，两类消费者福利都提高。
   - 若 $s>\bar s$，则**更高**的搜索成本反而对应更高的信息性与更高的 savvy 福利；而 inexperienced 消费者福利随 $s$ 上升而下降。

> 直觉：这部分特别值得反复咀嚼。低搜索成本时，继续搜索本来就容易，企业没必要太狠地操纵信息，因此再降低一点成本，确实会让市场更透明。  
> 但高搜索成本时，消费者本来就不太愿意继续搜，企业会利用这一点，通过更强的扭曲来锁住 inexperienced 消费者。于是当你把高搜索成本稍微降一点时，企业为了防止消费者真的开始继续搜，反而要**更用力地扭曲信息**。所以“搜索更便宜”并不总等于“信息更透明”。

### Lemma 5：福利如何计算，为什么 “老手变好、新手变差” 不是一句空话

作者把两类消费者的期望福利写成 order statistics：

$$
CS^s = \mathbb E_G[\max\{v_1,\dots,v_n\}],
$$

以及令 $\tilde v=\min\{v,r\}$ 后，

$$
CS^i = \mathbb E_G[\max\{\tilde v_1,\dots,\tilde v_n\}].
$$

> 直觉：savvy 消费者会把所有 realization 都看完，所以她的福利就是“最高 realization 的期望值”。inexperienced 消费者则把所有高于 $r$ 的 realization 都当成“已经够好，不再搜”，所以她实际可利用的是被 $r$ 截断后的分布。这个写法很漂亮，因为它把福利比较直接转化为信息性比较。

### Extension：additional cost heterogeneity

在主模型之后，作者把 inexperienced 消费者的单点搜索成本 $s$ 扩展成分布 $K(\cdot)$，并证明：只要 inexperienced 消费者成本支持集的下界仍严格为正，那么在足够大的市场里，**no disclosure at the bottom** 依然存在。

> 直觉：主模型的二元成本设定不是关键，关键是“新手里最会搜索的人，搜索成本也还是正的”。只要这一点成立，企业在大市场中隐瞒低估值的动机就不会消失。

## 比较静态汇总表 (Comparative Statics Summary)

| 参数变化 | 对披露结构的影响 | 对信息性的影响 | 对 savvy 福利 | 对 inexperienced 福利 | 直觉 |
|:---|:---|:---|:---|:---|:---|
| $n \uparrow$，且跨过 $\bar n$ | 从 disclosure at the bottom 变为 no disclosure at the bottom | 不会走向 full disclosure | $\uparrow$ | 下降到 $\mu-s$ 的“单次访问”水平 | 大市场里如实披露低值几乎卖不掉，不如把低值往上池化截留新手 |
| $n \uparrow$，且 $n>\bar n$ | 低值仍被完全隐藏，高值披露区扩大 | $\uparrow$，但仍非 full disclosure | $\uparrow$ | 基本停留在 $\mu-s$ | 竞争迫使企业在高值上更透明，但不会放弃对低值的隐瞒 |
| $s \downarrow$，且 $s<\underline s$ | 扭曲减弱 | $\uparrow$ | $\uparrow$ | $\uparrow$ | 搜索本来就容易，企业没必要靠严重操纵来阻止继续搜索 |
| $s \downarrow$，且 $s>\bar s$ | 扭曲增强 | $\downarrow$ | $\downarrow$ | $\uparrow$ | 成本稍降后，企业为防止新手真的开始继续搜索，会更努力把信息设计成“第一家就够了” |
| $s \uparrow$，且 $s>\bar s$ | 扭曲减弱，向 full disclosure 靠近 | $\uparrow$ | $\uparrow$ | $\downarrow$ | 高成本下，消费者本就难继续搜，企业没必要再额外重度操纵 |
| $\alpha \downarrow$ | 更靠近 full disclosure | $\uparrow$ | 通常 $\uparrow$ | 不一定单调，但新手段的重要性下降 | 市场里越多是 savvy，企业越需要靠真实高值竞争 |
| $\alpha \uparrow$ | 更靠近 informational Diamond 式不透明 | $\downarrow$ | $\downarrow$ | 更容易被锁在第一家 | 市场里越多是 inexperienced，截留动机越强 |

> 注：关于 $n$ 的单调比较，本文最强的结论主要发生在跨过阈值 $\bar n$ 以及 $n>\bar n$ 的区域；在小市场内部，部分比较并不是全文强调的重点。

## 主要结论与管理启示 (Main Results & Managerial Insights)

### 与 benchmark 的对比

| 维度 | 只有 savvy（$\alpha=0$） | 只有 inexperienced（$\alpha=1$） | 本文主模型（$0<\alpha<1$） |
|:---|:---|:---|:---|
| 均衡披露 | full disclosure | informational Diamond paradox | partial disclosure |
| 扭曲发生位置 | 基本没有 | 全部集中在阻止搜索 | 围绕 reservation value 的局部扭曲 |
| 大市场极限 | 走向 full disclosure | 消费者第一家就停 | 高值部分透明、低值系统性隐藏 |
| inexperienced 搜索行为 | 不适用 | 从不继续搜 | 只在小市场中继续搜 |
| 竞争的福利效应 | 更竞争通常更好 | 无法产生真实比较 | savvy 更好，inexperienced 可能更差 |

### 管理建议

1. **别把“更多竞争”误当成“更高透明度”。**  
   如果用户群里有相当比例的新手或高搜索成本用户，企业竞争未必自动清洗信息环境。平台或监管者若真的关心透明度，可能需要标准化 downside disclosure，而不能只依赖市场竞争。

2. **“增加选项”必须配“提升可比性工具”。**  
   大市场里 paradox of choice 的问题不是消费者看不过来，而是企业会策略性地让他们没动力继续看。平台应提供可比较的 attribute matrix、统一标签、默认排序解释，而不是只堆更多卖家。

3. **降低搜索摩擦不总是边际有效。**  
   当市场搜索成本已经很低时，继续降低通常有益；但当搜索成本很高时，只做一些小修小补，可能反而让企业更有动力做信息操纵。此时更有效的政策可能是先提高基础披露标准。

4. **针对 inexperienced 用户的保护比“一刀切透明”更重要。**  
   savvy 用户在竞争中通常会越过信息噪音，但 inexperienced 用户更容易被企业设计的信息停下。对这类用户，强制披露隐藏缺点、提供跨卖家标准化对比，价值更大。

## 与相关文献的对话 (Dialogue with Literature)

| 文献 | 共同关注点 | 本文推进/区别 | 为什么重要 |
|:---|:---|:---|:---|
| Hwang et al. (2023) | 竞争性信息披露 | 他们在无搜索摩擦下得到 full disclosure；本文加入搜索成本异质性后，说明竞争不再足以逼出完全透明 | 这直接推翻了“竞争最终会净化信息”的常见直觉 |
| Au and Whitmeyer (2023) | 搜索市场中的信息提供 | 他们的 costly search 环境会产生 informational Diamond paradox；本文加入 savvy 消费者后，不再是完全不披露，而是围绕 $r$ 的 partial disclosure | 说明哪怕只加入一部分“会比价的人”，均衡也会从完全不透明变成更精细的局部扭曲 |
| Board and Lu (2018) | 搜索市场中的竞争性披露 | 他们研究同质品卖家；本文研究水平差异化产品和异质搜索成本消费者，均衡是独特的 partial disclosure 而不是两极化结果 | 把披露问题从“卖同一个东西”推进到“卖不同东西但消费者需要继续比较”的场景 |
| Hwang and Hwang (2025) | 异质搜索成本与竞争性披露 | 他们在连续成本分布与最低成本接近 0 的环境中得到 upper-censorship；本文有一小部分 savvy 消费者时，大市场反而是“披露高值、隐藏低值”，并且搜索成本效应非单调 | 说明 cost heterogeneity 的结论对支持集底部是否有 gap、以及是否存在真正 zero-cost 搜索者，非常敏感 |

## 犀利评论 (Reviewer's Critique)

### 优点

**理论贡献。**  
这篇 paper 把 persuasion / information design 与搜索模型真正拼在了一起，而且不是机械拼接，而是从 payoff discontinuity 出发，推出了一整套唯一均衡结构。最亮眼的地方是，它把“局部扭曲发生在哪里”说得非常清楚：就在 reservation value 附近。

**方法创新。**  
作者不是直接硬解一个非常难的动态博弈，而是先外生化 $r$，刻画披露结构，再用搜索方程闭合 fixed point。这条分析路线很干净，也让 Proposition 1 到 Proposition 5 的逻辑层层推进。

**实践相关性。**  
paradox of choice 的解释非常新：不是行为偏差，不是认知负担，而是企业的最优信息设计。这给平台治理和消费者保护提供了完全不同的政策视角。

### 模型限制 / 假设过强

1. **价格外生。**  
   这让模型非常干净，但也把最重要的竞争变量之一拿掉了。现实里价格和信息设计大概率是联动的，因此本文更适合作为“信息竞争”的 benchmark，而不是完整市场均衡。

2. **二元搜索成本是强简化。**  
   尽管 extension 说明大市场结论有稳健性，但主模型的 sharp result 很大程度来自“真有一类人必看完市场”。若现实里 savvy 用户比例很小、且也存在有限摩擦，均衡形状可能没有这么干净。

3. **企业看不到消费者类型与搜索阶段。**  
   现实中的数字平台往往能根据浏览深度、点击轨迹、老客标签做定向展示。若允许这种定向 persuasion，企业可能会更精确地对不同阶段用户操纵信息。

4. **单产品、单位需求、静态环境。**  
   没有品牌资本、重复访问、口碑与学习，也没有平台的排名规则。这使得本文机制非常清楚，但离一些 OM/Marketing 场景仍有一步之遥。

5. **对分布形状有技术性要求。**  
   作者故意选了一个在 frictionless benchmark 下会 full disclosure 的环境，以便突出“异质搜索成本”带来的变化。这是优点，也是限制：若原本无摩擦均衡就不是 full disclosure，加入搜索摩擦后的 comparative statics 可能更复杂。

### 未来方向

1. **把价格也内生化。**  
   研究企业如何联合选择价格与信息结构，是否会出现“高透明高价”与“低透明低价”的分层竞争。

2. **加入平台 / 中介。**  
   让平台决定排序、披露模板或比较工具，分析平台设计能否打破 paradox of choice。

3. **允许企业观察用户搜索阶段。**  
   研究 stage-contingent 或 personalized disclosure 是否会让局部扭曲更强，甚至诱发动态锁定。

4. **做实证检验。**  
   用 clickstream、试用转化、房源浏览或 OTA 数据，检验“大市场里低质量信号是否更少被明示、用户是否更早停止比较”。

5. **引入行为偏差。**  
   本文已经在完全理性下得到 choice overload 式结果；若再叠加有限注意、默认偏差或过度自信，结果可能更强，也更贴近营销环境。

6. **考虑多属性产品。**  
   现实中企业往往不是把“总价值”池化，而是 selectively reveal 某些属性、隐藏另一些属性。把单维估值扩展到多维属性，是很自然也很重要的一步。

## 最后一句总结

这篇文章真正回答的问题不是“竞争会不会让企业更诚实”，而是：**当市场里同时有会看遍全场的人和可能在第一家停下的人时，企业会把哪段真相说清楚、把哪段真相故意揉模糊。** 它给出的答案是：企业最会动手脚的地方，不在极好或极差，而恰恰在消费者“差一点就要继续搜”的那条边界附近。

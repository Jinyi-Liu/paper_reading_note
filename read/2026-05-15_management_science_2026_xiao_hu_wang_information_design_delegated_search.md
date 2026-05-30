# Information Design of a Delegated Search

作者：Yangge Xiao（The University of Melbourne）、Zhenyu Hu（National University of Singapore）、Shouqiang Wang（The University of Texas at Dallas）  
期刊：Management Science, Articles in Advance  
年份：2026  
DOI：10.1287/mnsc.2024.05925  
关键词：optimal stopping, Bayesian persuasion, principal-agent, threshold policy, recommendation

中文摘要：本文研究一个被委托的序贯搜索问题。委托人将有限次搜索机会交给代理人执行；代理人承担搜索成本，并控制是否继续搜索；搜索结束后的收益按事先约定比例分成。关键的信息摩擦是：只有委托人能评估每次搜索结果的真实价值，因此委托人可以设计在每次搜索后向代理人披露什么信息。作者将问题建模为一个动态信息设计问题，并完整刻画了最优信息政策。最优政策非常简单：委托人事前承诺一串确定性的 acceptance standards，每期只给代理人一个二元建议“继续搜索”或“停止”。如果当前可接受的终止收益低于该期标准，就建议继续；否则建议停止。代理人在均衡中会自愿遵循建议。若搜索结果不可召回，最优标准是有信息含量、逐期下降的，并且像委托人以一个 shadow cost 自己搜索时的 stopping thresholds 一样递归确定。若搜索结果可召回，最优政策出现 regime change：前若干期可以设置一个常数且可能完全无信息的高标准，让代理人在“黑箱”状态下继续搜索；之后再逐期降低标准，每一期标准由“代理人额外搜索的边际感知收益 = 搜索成本”独立确定。

## 论文速览

| 维度 | 内容 |
|:---|:---|
| 研究问题 | 当代理人负责搜索并承担成本、但只有委托人能评价搜索结果时，委托人应如何反馈信息，才能激励代理人继续搜索？ |
| 典型场景 | 招聘经理委托猎头找候选人；大药企委托 biotech startup 做研发；导师让博士生做实验或分析。 |
| 核心摩擦 | 决策权与信息权分离：代理人控制是否继续搜索，委托人掌握搜索结果价值的信息。货币激励固定或不可用。 |
| 方法 | 动态信息设计 + principal-agent + optimal stopping。作者用 primal-dual / Lagrangian relaxation 构造强对偶并刻画最优政策。 |
| 最核心结果 | 最优反馈不需要复杂报告，只需要一串确定性的 acceptance standards 和二元建议：结果还不够好就继续，达到标准就停止。 |
| 与 full disclosure 的差异 | 完全披露搜索结果通常不是最优。最优信息政策能诱导比 full information 更高的搜索强度。 |
| No recall 与 free recall 的区别 | No recall 中，过去结果不可保留，标准递归决定，存在 deadline effect；free recall 中，过去最好结果可保留，前期可不披露信息，后期标准逐期独立决定。 |
| 管理启示 | 反馈机制应事前制度化。很多场景下，“是否达到下一阶段标准”比“完整评分/完整披露”更能激励持续搜索。 |

## TL;DR

这篇文章讲的是：当你把搜索任务交给别人做，但只有你知道搜索结果到底好不好时，最优反馈往往不是把所有信息都告诉对方，而是事前承诺一套逐步变化的“接受标准”，然后只告诉他“继续”还是“停止”。这样做能让代理人自愿搜索更久，甚至在低成本情形下达到像委托人直接命令搜索一样的效果。

最重要的区别在于结果能不能保留：如果不能保留，反馈必须从一开始就有信息含量，并随着 deadline 临近逐步降低标准；如果能保留，前期反而可以不反馈，因为代理人自己也愿意积累好结果，后期才需要更有指向性的反馈。

## One More Thing

这篇文章最值得拿出来讲的洞察是：**“透明”不一定是最好的激励。** 直觉上，既然代理人不知道搜索结果好坏，委托人似乎应该尽量告诉他真实结果，让他做出更理性的搜索决策。但本文说明，完全披露反而可能让代理人过早满足于一个“还不错”的结果并停止搜索。最优机制像一个制度化的评审流程：事前说清楚每一轮的标准，之后只告诉代理人“还没达到标准，继续找”或“已经达到标准，可以停”。这条简单的信息规则，把 classical optimal stopping 的 threshold idea 变成了一种激励工具。

## 研究背景与动机 (Motivation)

### 实践痛点

许多现实中的搜索任务都不是由最终受益方亲自执行，而是被委托给更有时间、能力或专业资源的代理人：招聘中，招聘经理依赖 recruiter 搜索候选人；药企将研发或临床试验外包给 biotech startup 或学术机构；学术研究中，导师让博士生做实验、跑模型、寻找研究结果。

这些场景有三个共同特征。第一，代理人承担搜索成本，并且在很大程度上控制是否继续搜索。第二，货币激励往往事前固定，或者根本不适用。例如 recruiter 的佣金比例通常事先约定，药企合作有事先设定的 profit sharing，导师和博士生之间通常没有逐轮货币奖励。第三，委托人比代理人更能评价搜索结果。招聘经理更清楚候选人与岗位的匹配价值，药企更能估计新药商业价值，导师更能判断研究结果是否足够有发表潜力。

因此，问题不是“给多少钱才能让代理人继续找”，而是：**当钱已经固定、且代理人看不懂结果价值时，委托人能否用信息反馈本身作为激励工具？**

### 理论缺口

现有 sequential search 文献通常把搜索建模为单一决策者问题，即搜索者自己知道结果、自己承担成本、自己决定停止。Delegated search 文献开始考虑 principal-agent 摩擦，但多数关注 moral hazard 或货币激励：代理人的努力不可观测，委托人通过合同或付款来激励。本文的摩擦不同：代理人确实执行搜索，但搜索结果的价值只有委托人能评估；委托人不能或不愿动态调整货币激励，只能控制信息披露。

在信息设计文献中，静态 Bayesian persuasion 和动态 information design 已经发展很多，但本文的问题同时具有 long-lived agent、动态生成的委托人私有信息、以及 stopping/search incentive，这使得现有结果不能直接套用。

### 核心贡献

第一，本文将 delegated sequential search 建模为动态信息设计问题，突出“信息权”和“搜索控制权”分离所带来的激励问题。

第二，作者证明一般的信息政策可以无损地简化为二元 recommendation policy，即每期只需要“继续”或“停止”两个消息。

第三，作者完整刻画了 no recall 和 free recall 两类搜索下的最优 acceptance standards，并解释二者背后完全不同的动态激励机制。

第四，方法上，作者用显式 primal-dual construction 和 strong duality 找出哪些 IC 约束绑定，从而给出更透明的经济直觉。

## 模型设定与假设 (Model Setup & Assumptions)

### 符号体系

#### 搜索环境

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $T$ | 搜索机会总数 | 主模型中有限；扩展中考虑无限期和折现。 |
| $t$ | 当前搜索机会 | $t=1,2,\ldots,T$。 |
| $V_t$ | 第 $t$ 次搜索产生的结果价值 | 非负、独立同分布。 |
| $F(\cdot), f(\cdot)$ | $V_t$ 的分布与密度 | 分布为共同知识。 |
| $\bar v$ | 单次搜索结果的均值 | $\bar v=E[V_t]$，有限。 |
| $v_{\max}$ | 价值分布支持的上界 | 可有限或无限；free recall 中很重要。 |
| $c$ | 每次搜索成本 | 由代理人承担。 |

#### 收益与停止规则

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $r$ | 委托人分成比例 | $r\in(0,1)$。 |
| $1-r$ | 代理人分成比例 | 代理人收益份额，但需支付搜索成本。 |
| $v^{t}$ | 到第 $t$ 次为止的搜索结果历史 | $v^t=(v_1,\ldots,v_t)$。 |
| $\omega(v^t)$ | 搜索终止收益 | 取决于是否可召回。 |
| No recall | 不可召回搜索 | $\omega(v^t)=v_t$，停止时只能用当前结果。例：招聘候选人错过就不可再得。 |
| Free recall | 可召回搜索 | $\omega(v^t)=v_{(t)}=\max_{1\le s\le t}v_s$，停止时可用历史最好结果。例：研发备选方案、学生研究成果。 |

#### 行动与信息

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $b_t$ | 委托人的停止/继续行动 | $b_t=0$ 表示委托人停止，$b_t=1$ 表示继续。 |
| $m_t$ | 委托人发送给代理人的消息 | 一般可为任意消息；最优可简化为二元建议。 |
| $a_t$ | 代理人的行动 | $a_t=1$ 表示继续搜索，$a_t=0$ 表示停止。 |
| $\sigma=(\sigma^b,\sigma^m)$ | 委托人的信息政策 | 包括停止政策与消息政策。 |
| $\phi_t^\sigma$ | 代理人的 continuation payoff | 给定政策和公共历史后的递归价值。 |
| $\Phi_t^\sigma$ | 委托人的 continuation payoff | 委托人给定私有结果历史与公共消息历史后的递归价值。 |

### 博弈/决策结构

每一期的顺序如下。

1. 搜索尚未终止，委托人观察已有搜索结果 $v^{t-1}$，代理人只观察公共历史和此前消息。
2. 委托人决定是否直接停止。如果停止，双方按 $r$ 和 $1-r$ 分割终止收益 $\omega(v^{t-1})$。
3. 若委托人继续，则发送消息 $m_t$ 给代理人。该消息可以是定性评价、评级、统计摘要，也可以只是推荐“继续/停止”。
4. 代理人基于委托人政策、消息历史和 Bayes 推断，决定是否支付成本 $c$ 搜索第 $t$ 次机会。
5. 若代理人搜索，产生 $V_t$，该价值只有委托人能评估；若代理人停止，搜索终止并分配收益。

论文第 7 页的 Figure 1 画出了这一时序：虚线部分是委托人的观察、停止和发信；实线部分是代理人的搜索/停止决策。这个图的核心含义是，委托人无法强迫代理人继续，只能通过“继续动作本身”和“消息内容”影响代理人的 belief。

### 信息结构

委托人观察并能评价所有过去搜索结果 $v^{t-1}$。代理人不知道这些价值，只知道搜索结果分布和委托人承诺的政策。代理人看到委托人是否继续、看到消息 $m_t$，并据此推断当前搜索结果是否“足够好”。

这一设定刻意放大了信息不对称：代理人完全看不懂自己搜索结果的价值。论文附录讨论了代理人也能获得公共或私人 signal 的情形，主结论的 threshold structure 仍有稳健性。

### 目标函数与约束

代理人的递归价值可以写成：

$$
\phi_t^\sigma(m^{t-1})=
E\left[(1-b_t)(1-r)\omega(V^{t-1})
+b_t\max\left\{(1-r)E[\omega(V^{t-1})\mid m^t,b^t=e^t,\sigma],\ \phi_{t+1}^\sigma(m^t)-c\right\}
\mid m^{t-1},b^{t-1}=e^{t-1},\sigma\right].
$$

> 直觉：如果委托人停止，代理人拿到当前终止收益的 $(1-r)$ 份额。如果委托人继续并发送消息，代理人比较两个选择：现在停止并拿当前终止收益的期望份额，或者支付成本 $c$ 进入下一期。消息的作用正是改变代理人对当前终止收益和未来价值的 belief。

代理人的最优行动为：

$$
 a_t^\sigma(m^t)=\mathbf{1}\left\{
\phi_{t+1}^\sigma(m^t)-c\ge (1-r)E[\omega(V^{t-1})\mid m^t,b^t=e^t,\sigma]
\right\}.
$$

> 直觉：代理人继续搜索当且仅当“未来 continuation value 减去搜索成本”不低于“现在停止的期望收益”。由于代理人承担成本但只拿 $(1-r)$ 的收益份额，他比委托人更想早停。

委托人的递归价值为：

$$
\Phi_t^\sigma(v^{t-1},m^{t-1})=
E\left[(1-b_t)r\omega(v^{t-1})+b_t\left((1-a_t^\sigma(m^t))r\omega(v^{t-1})+a_t^\sigma(m^t)\Phi_{t+1}^\sigma((v^{t-1},V_t),m^t)\right)
\mid v^{t-1},m^{t-1},b^{t-1}=e^{t-1},\sigma\right].
$$

> 直觉：委托人的收益来自终止收益的 $r$ 份额。若代理人继续搜索，委托人不支付搜索成本，因此委托人通常比代理人更希望继续。委托人的核心问题是设计 $\sigma$，让代理人在 incentive compatible 的情况下尽可能多搜索。

委托人的问题是：

$$
\max_\sigma \Phi_1^\sigma
$$

subject to 代理人的递归价值、最优反应，以及 Bayes 一致的 belief。难点在于消息空间一般、历史维度随时间增长、代理人的 incentive constraint 是动态的。

### 关键假设

| 假设 | 合理性 | 放松后可能影响 |
|:---|:---|:---|
| 委托人可事前承诺信息政策 | 许多组织可以制度化反馈流程，例如 milestone review、predefined hiring bar、stage-gate。 | 若不能承诺，委托人可能事后有动机夸大或隐藏信息，导致 cheap talk 或 reputation 问题。 |
| 代理人承担搜索成本，委托人不承担 | 招聘、研发、学生实验中，搜索努力主要由代理人付出。 | 若委托人也承担评估成本，会改变停止标准；附录讨论 evaluation cost。 |
| 货币激励固定或不可动态调整 | 很多场景中分成、佣金、作者排序等事前确定。 | 若允许完全动态付款，agency problem 可能被合同解决，信息激励的重要性下降。 |
| 只有委托人观察结果价值 | 委托人更懂匹配质量、商业价值或研究质量。 | 若代理人也有 signal，最优信息设计需考虑 informed receiver；问题更复杂。 |
| 搜索结果 i.i.d. 且分布为共同知识 | 便于分离信息激励与学习分布的问题。 | 若结果相关或分布未知，搜索过程会叠加 learning，threshold 可能依赖 belief state。 |
| 单一代理人 | 聚焦信息反馈与单个搜索者的动态激励。 | 多代理人会引入竞争、信息外部性和 strategic disclosure between agents。 |

## 分析路线图 (Roadmap of Analysis)

1. **先建立三个 benchmark。** Costless search 给出委托人可达到的上界；full information 展示完全披露下代理人的停止规则；no information 展示完全不披露下代理人能搜索多久。
2. **再证明二元 recommendation policy 足够。** 虽然一般消息空间可以非常复杂，但因为代理人的行动只有继续/停止，委托人可以无损地把消息简化成“建议继续”与“建议停止”。
3. **先暂时去掉委托人的停止权，只设计消息。** 这是主求解步骤。作者分别解决 no recall 和 free recall，得到最优 acceptance standards。
4. **再把委托人停止权放回来。** 结果显示停止权对委托人没有额外价值；最优结果可以仅靠信息推荐实现。
5. **最后做扩展。** 包括 outside option、无限期折现、分成比例 $r$ 的优化、额外信号和评估成本等。

## 核心分析与求解 (Analysis & Solution)

### Proposition 1：Costless Search 作为上界

若委托人能直接命令代理人搜索，或等价地，搜索对委托人无成本，则问题退化为经典 optimal stopping。

No recall 中，最优 stopping threshold $\beta_t^{\circ,NR}$ 递减，并满足：

$$
\beta_t^{\circ,NR}=E[\max\{V_t,\beta_{t+1}^{\circ,NR}\}],\quad \beta_{T+1}^{\circ,NR}=0.
$$

Free recall 中，最优标准为：

$$
\beta_t^{\circ,FR}=v_{\max},\quad t=1,\ldots,T.
$$

> 直觉：这是委托人的 first-best 上界，因为代理人的激励约束被完全拿掉。No recall 中，当前结果若不用就会消失，因此越接近终点，继续搜索的 option value 越低，阈值下降。Free recall 中，已有最好结果不会丢，且没有搜索成本，所以只要还有机会就继续搜索，等价于把接受标准设为最高可能值 $v_{\max}$。

### Proposition 2：Full-Information Policy

接着看最直观的政策：委托人每期把所有过去搜索结果完全告诉代理人。此时委托人不应提前停止，而应让代理人控制停止。代理人采用 classical threshold stopping rule。

No recall 中：

$$
\beta_t^{FI,NR}=E[\max\{V_t,\beta_{t+1}^{FI,NR}\}]-\frac{c}{1-r},\quad \beta_{T+1}^{FI,NR}=0.
$$

Free recall 中，阈值为常数 $\beta^{FI,FR}$，满足：

$$
E[(V_1-\beta^{FI,FR})^+]=\frac{c}{1-r}.
$$

> 直觉：full information 使代理人像一个单独的搜索者一样决策，但他的有效搜索成本是 $c/(1-r)$。因为代理人只拿结果价值的 $(1-r)$ 份额，所以同样的物理成本 $c$ 对他而言更“贵”。因此，full information 下的搜索强度低于 costless benchmark。

### Proposition 3：No-Information Policy

如果委托人完全不披露搜索结果，也不提前停止，那么代理人只能基于 prior 判断是否继续。

No recall 中，代理人只搜索第一次，收益为：

$$
\phi_1^{NI}=(1-r)\bar v-c.
$$

Free recall 中，代理人会搜索到第 $\tau^{FR}$ 次，其中：

$$
\tau^{FR}=\max\left\{t\in\{1,\ldots,T\}: E[V_{(t)}-V_{(t-1)}]\ge \frac{c}{1-r}\right\}.
$$

> 直觉：No recall 下，如果代理人不知道上一轮结果，那么搜索第二次与搜索第一次在 prior 上没有本质区别，但第二次会放弃第一次的结果；继续的边际价值不足，所以只搜一次。Free recall 下不同：过去最好结果可保留，早期多搜一次有正的提升最好结果的边际价值，因此代理人即使没有反馈，也愿意先搜若干次；但边际提升递减，最终会停。

### Proposition 4：二元 recommendation policy 足够

在一般信息政策下，消息空间 $M$ 可以任意复杂；但作者证明，对任意信息政策，都存在一个只发送二元建议的 recommendation policy，能诱导相同的双方期望收益。

二元建议为：

$$
m_t=1 \Rightarrow \text{建议继续搜索},\quad m_t=0 \Rightarrow \text{建议停止}.
$$

推荐政策需要满足两个 IC 约束：建议继续时代理人愿意继续；建议停止时代理人愿意停止。

> 直觉：代理人的行动只有两个：继续或停止。因此，复杂消息中真正影响 payoff 的部分，是它最终诱导代理人采取哪个行动。委托人不需要告诉代理人“候选人分数是 87/100”或“项目价值大约在某区间”，只需要发送一个能被代理人自愿执行的行动建议。这一步极大降低了问题维度。

### Theorem 1：No Recall 下的最优信息政策

在搜索结果不可召回时，最优消息政策是一个 threshold recommendation policy：

$$
\sigma_t^{*m,NR}(1\mid v^{t-1},m^{t-1})=\mathbf{1}\{v_{t-1}\le \beta_t^{*,NR}\}.
$$

也就是说，如果上一轮结果 $v_{t-1}$ 没达到第 $t$ 期标准 $\beta_t^{*,NR}$，就建议继续；否则建议停止。

阈值满足：

$$
\beta_t^{FI,NR}<\beta_t^{*,NR}\le \beta_t^{\circ,NR}.
$$

当有效搜索成本足够低，即 $c/(1-r)\le \kappa^{*,NR}$ 时，委托人甚至可以达到 costless benchmark：

$$
\beta_t^{*,NR}=\beta_t^{\circ,NR},\quad t=1,
\ldots,T.
$$

当 $c/(1-r)>\kappa^{*,NR}$ 时，存在唯一的 shadow cost $\lambda^{*,NR}\in(0,c/(1-r))$，使得：

$$
\beta_t^{*,NR}=E[\max\{\beta_{t+1}^{*,NR},V_t\}]-\lambda^{*,NR},\quad \beta_{T+1}^{*,NR}=0.
$$

并且 $\lambda^{*,NR}$ 由代理人的动态激励约束决定。论文中的条件可写为：

$$
\sum_{t=2}^{T}\left\{\bar v-\frac{c}{1-r}-E[V_{t-1}\mid V_{t-1}\le \beta_t^{*,NR}]\right\}
\prod_{s=2}^{t}F(\beta_s^{*,NR})=0.
$$

> 直觉：No recall 的难点在于，代理人继续搜索时会放弃当前结果；他担心“手里的还不错，为什么还要冒险继续找”。因此，委托人要设置较高的早期接受标准，并承诺随着时间推进逐步降低标准。这个下降标准本身给了代理人 intertemporal incentive：未来标准会更宽松，继续搜索不至于无限期被卡住。$\lambda^{*,NR}$ 可以理解为委托人为了说服代理人继续搜索所面对的影子成本。影子成本越高，接受标准越低，继续搜索区域越小。

论文第 11 页的 Figure 2 可视化了这一点：在 no recall 下，最优标准位于 costless threshold 与 full-information threshold 之间。也就是说，最优信息设计比完全披露诱导更多搜索，但通常达不到无成本搜索上界；低搜索成本时则可以达到上界。

**关键 trade-off：** 委托人想设高标准以扩大继续搜索区域，但标准越高，代理人在被告知“继续”时越可能相信当前结果其实也不差，从而不愿放弃。最优标准在“刺激继续搜索”和“让继续建议可信”之间平衡。

### Proposition 5：No Recall 的 deadline effect

在 no recall 中，若固定“还剩多少次机会”，总搜索机会数 $T$ 越大，最优 acceptance standard 越低；同时 cutoff $\kappa^{*,NR}$ 随 $T$ 下降，shadow cost $\lambda^{*,NR}$ 随 $T$ 上升。

> 直觉：经典 stopping problem 中，只要剩余机会数相同，threshold 不依赖总 horizon。但在委托搜索里，总 horizon 越长，委托人越需要在更长时间内维持代理人的搜索激励，因此 persuasion 变得更难，影子成本上升。论文第 12 页的 Figure 3 显示，对于同样剩余机会数，随着总 $T$ 增加，最优标准整体下移。

### Theorem 2：Free Recall 下的最优信息政策

当搜索结果可召回时，最优消息政策同样是 threshold recommendation policy，但比较对象变成历史最好结果：

$$
\sigma_t^{*m,FR}(1\mid v^{t-1},m^{t-1})=\mathbf{1}\{v_{(t-1)}\le \beta_t^{*,FR}\}.
$$

即：只要目前为止的最好结果还没有达到第 $t$ 期标准，就建议继续。

最优标准满足：

$$
\beta_t^{FI,FR}<\beta_t^{*,FR}\le v_{\max},
$$

且存在一个 cutoff $\tau^{FR}$，使得：

$$
\beta_t^{*,FR}=v_{\max},\quad t=1,\ldots,\tau^{FR},
$$

而在 $t=\tau^{FR}+1,\ldots,T$ 时，每一期阈值由下式独立决定：

$$
E[V_{(t)}-V_{(t-1)}\mid V_{(t-1)}\le \beta_t^{*,FR}]=\frac{c}{1-r}.
$$

代理人在最优政策下的总期望收益等于 no-information benchmark：

$$
\phi_1^{*,FR}=(1-r)E[V_{(\tau^{FR})}]-c\tau^{FR}.
$$

> 直觉：Free recall 中，早期搜索不会浪费，因为找到的好结果可以保留。因此，即使委托人什么都不说，代理人也愿意先搜索若干次，直到“多搜一次提高历史最好结果”的边际价值降到成本以下。委托人的最优做法是利用这一点：前 $\tau^{FR}$ 期可以完全 hands-off，甚至不给任何有用反馈；之后，代理人的自然搜索动力不足，委托人才开始用逐期降低的标准提供信息激励。后期每个标准都独立地让代理人的 perceived marginal return 刚好等于成本。

论文第 13 页的 Figure 4 展示了这种 regime change：最优标准先停留在 $v_{\max}$，然后开始下降；full-information threshold 是一条更低的常数线。因此，最优信息政策在后期仍比完全披露诱导更多搜索。

**关键 trade-off：** Free recall 下，早期不需要“激励”，因为累积最好结果本身已经给代理人足够动力；真正的问题发生在边际收益递减之后。此时，委托人通过降低 acceptance standard 来恢复代理人的边际搜索收益。

### Corollary 1：Free Recall 没有 deadline effect

在 free recall 中，costless threshold、full-information threshold、最优 acceptance standard 以及 cutoff $\tau^{FR}$ 都不依赖总搜索机会数 $T$。

> 直觉：因为历史最好结果可保留，某一期是否值得继续主要取决于“当前历史最好结果”和“再搜一次能提升多少”，而不是终点还有多远。因此，free recall 的激励结构由 diminishing marginal improvement 驱动，不是由 deadline 驱动。

### Theorem 3：委托人的停止权没有额外价值

把委托人的停止权放回模型后，最优结果不变。若 $\sigma^{*m}$ 是前述最优消息政策，则任何满足下式的政策都是最优的：

$$
\sigma_t^b(1\mid v^t,m^{t-1})\sigma_t^m(1\mid v^t,m^{t-1})=\sigma_t^{*m}(1\mid v^t,m^{t-1}).
$$

含义是：搜索继续当且仅当委托人选择继续且消息建议继续。只要二者乘积实现同一个 continuation region，委托人的收益相同。

> 直觉：代理人比委托人更想停止，因为代理人承担搜索成本。如果委托人觉得应该停止，代理人通常更愿意停止。因此，委托人不需要用强制停止权来实现最优结果；只靠 persuasion 即可。换句话说，“动作”本身也可以是信息：委托人允许继续，就等价于发出“继续搜索”的推荐。

## Extensions

### Outside option

扩展中，委托人可以在搜索终止时选择一个外部选项 $R$。若 $R$ 足够高，委托人一开始就选择外部选项；若 $R$ 不高，最优政策仍保持 threshold structure。

新的地方在于 off-equilibrium threat：如果代理人不服从推荐，委托人可以威胁转向 outside option，使代理人得到零收益。这使得代理人的 IC 约束更松，委托人更有力量。

### Infinite horizon with discounting

当搜索机会无限且双方以 $\delta\in(0,1]$ 折现时，threshold 结构仍然稳健。

No recall 中，由于每一期面临无限未来，问题变成 time-homogeneous，最优 acceptance standard 是常数。Free recall 中，regime change 仍存在：前若干期使用 costless threshold $\beta_\delta^\circ$，之后逐期降低标准，使折现后的边际收益等于搜索成本。

一个重要细节是：若 $\delta<1$，free recall 的 costless threshold 不再是 $v_{\max}$，因为即使结果可保留，等待也有时间成本。

### Optimization of sharing fraction $r$

主模型把 $r$ 当作事前固定。扩展中，作者数值考察了委托人若能选择分成比例，会如何结合信息政策设计。

论文第 18 页的 Figure 5 显示，在最优信息政策下，委托人收益关于 $r$ 呈 quasi-concave，并在内部点达到最大。直觉是：提高 $r$ 可以让委托人拿到更大收益份额，但也会降低代理人份额 $1-r$，削弱搜索激励。相比 full information 和 no information，最优信息设计允许委托人给代理人更高收益份额，从而减少双方的对抗性张力。

### Direct monetary transfers, additional signals, evaluation cost

附录还讨论了动态付款、代理人的公共/私人信号、委托人评估成本等变体。总体上，threshold recommendation policy 的形式比较稳健。但若允许完全动态且灵活的货币转移，信息激励问题会被合同工具部分或完全取代。

## 比较静态汇总表 (Comparative Statics Summary)

| 参数变化 | 对 no recall 的影响 | 对 free recall 的影响 | 直觉 |
|:---|:---|:---|:---|
| $c\uparrow$ | 有效成本 $c/(1-r)$ 上升，$\lambda^{*,NR}$ 上升，$\beta_t^{*,NR}$ 下降，继续搜索区域缩小。 | $\tau^{FR}$ 下降；后期 $\beta_t^{*,FR}$ 下降，继续搜索区域缩小。 | 搜索更贵，代理人更难被说服继续。 |
| $r\uparrow$ | 代理人份额 $1-r$ 下降，等价于有效成本 $c/(1-r)$ 上升，标准下降。 | 同左；自然搜索期 $\tau^{FR}$ 缩短。 | 委托人拿得越多，代理人越不愿搜索。 |
| $T\uparrow$ | 对同样剩余机会数，最优标准下降；shadow cost 上升。 | 无 deadline effect，标准与 $\tau^{FR}$ 不依赖总 $T$。 | No recall 需要长期维持激励；free recall 的边际收益由历史最好结果驱动。 |
| $\delta\downarrow$ | 无限期扩展中，等待价值下降，常数标准更低。 | costless threshold $\beta_\delta^\circ$ 低于 $v_{\max}$，早期政策也可能有信息含量。 | 时间越不耐心，继续搜索的 option value 越低。 |
| 搜索结果分布上行或 upside 变大 | 标准通常更高，搜索更值得维持。 | 早期自然搜索期可能更长，后期标准也更高。 | 未来结果更有潜在价值，继续搜索更有吸引力。 |
| 代理人能获得更准的私人信号 | 委托人的信息垄断减弱。 | 同左。 | 代理人不再完全依赖委托人反馈，信息设计空间缩小但更复杂。 |
| outside option $R\uparrow$ | 若足够高，委托人直接选择外部选项；否则 threshold 结构保持。 | 同左。 | 外部选项提高委托人的威胁能力和退出价值。 |

## 主要结论与管理启示 (Main Results & Managerial Insights)

### 与 Benchmark 的对比

| 政策 | 信息披露方式 | No recall 结果 | Free recall 结果 | 管理含义 |
|:---|:---|:---|:---|:---|
| Costless benchmark | 委托人可直接控制搜索 | first-best 上界，阈值递减 | 搜到最后，阈值为 $v_{\max}$ | 理论上界，现实中通常不可行。 |
| Full information | 完全披露所有结果 | 代理人用自己的 stopping threshold，搜索强度偏低 | 常数 threshold，搜索强度偏低 | 透明不是最优，可能导致过早停止。 |
| No information | 完全不反馈 | 代理人只搜一次 | 代理人搜到边际收益低于成本为止 | 不反馈在 no recall 中非常差；在 free recall 早期可行但后期不足。 |
| Optimal information | 二元推荐 + acceptance standards | 标准递归下降，介于 full information 与 costless 之间 | 前期可不披露，后期下降标准独立确定 | 简单、可制度化、能诱导更高搜索强度。 |

### 管理建议

1. **不要默认 full transparency。** 如果代理人承担搜索成本，完整披露“当前结果还不错”可能使其过早停止。更有效的是披露是否达到事前标准。

2. **把反馈机制事前写清楚。** 最优政策依赖 commitment。组织应提前设定每一轮的 acceptance standard，而不是事后临时评价。

3. **用二元建议降低沟通成本。** 很多场景中不需要详细评分报告，只需要告诉代理人“继续找”或“可以停”。

4. **区分结果能不能保留。** 候选人容易流失的招聘更像 no recall，需要从早期开始给有信息含量的反馈；研发、学生研究更像 free recall，前期可以鼓励探索，后期再转向明确标准。

5. **随着时间推移降低标准。** 无论 no recall 还是 free recall，最优 acceptance standards 都是 nonascending。临近 deadline 时，坚持早期高标准可能让搜索无法完成。

6. **把“允许继续”视为一种信号。** 即使委托人不发送额外消息，只要其继续/停止动作遵循阈值规则，也能传递足够信息。

7. **信息激励可以缓和分成冲突。** 当委托人能设计信息政策时，可以给代理人更高收益份额来维持搜索激励，而不是单纯提高自己的分成比例。

## 与相关文献的对话 (Dialogue with Literature)

### Lippman and McCall (1976)：经典 sequential search

共同点是都用 threshold stopping rule 描述序贯搜索。区别在于，经典模型是单一决策者：搜索者自己观察结果、承担成本并决定停止。本文把 threshold rule 放到 principal-agent 环境中，说明 threshold 不只是停止规则，还可以成为信息激励机制。

### Lewis (2012), Ulbricht (2016), Zorc et al. (2023)：delegated search

这些文章也研究委托搜索，但主要关注 moral hazard、adverse selection 或货币合同。本文的核心摩擦是信息不对称：委托人拥有对搜索结果的评价信息，而代理人控制搜索进程。这个区别重要，因为在许多组织关系中，货币合同并不灵活，信息反馈反而是更现实的激励工具。

### Kamenica and Gentzkow (2011)：Bayesian persuasion

本文继承了信息设计的基本思想：发送者通过设计信息结构影响接收者行动。但本文是动态环境，代理人长期存在，搜索结果逐期生成，且代理人的行动影响未来信息到达。因而不能直接使用静态 concavification，需要动态递归和 IC 约束分析。

### Ely and Szydlowski (2020), Smolin (2021)：dynamic information design

这些文章也研究长期代理人的动态信息激励。本文的区别在于，委托人的私有信息不是一次性给定，而是随着代理人的搜索持续产生；并且 stopping/search 的动态结构使 no recall 与 free recall 的机制完全不同。方法上，本文通过 primal-dual construction 找出绑定 IC，较清楚地揭示了阈值结构为何成立。

## 犀利评论 (Reviewer's Critique)

### 优点

理论贡献明确：本文把 delegated search 与 dynamic information design 结合起来，提出“信息反馈本身可以作为搜索激励工具”的机制，并完整区分 no recall 与 free recall。

方法上，文章没有停留在一般存在性或数值解，而是给出完整解析刻画。尤其是 no recall 中 shadow cost 的解释、free recall 中 regime change 的解释，都有清晰经济含义。

实践相关性强：招聘、药物研发、导师-学生关系都可以自然映射到模型。最优政策是简单的二元 recommendation 和 acceptance standards，具有制度化实施的可能。

### 模型限制/假设过强

第一，full commitment 是强假设。现实中委托人可能事后改变口径、隐瞒真实标准，代理人也可能怀疑委托人策略性反馈。如果缺乏承诺，threshold recommendation 的可信度会下降。

第二，代理人完全不能评价结果可能过于极端。许多 recruiter、startup 或博士生虽然不如委托人专业，但也有自己的信号。加入 informed receiver 后，最优信息政策可能更复杂。

第三，搜索努力被简化为二元继续/停止，成本固定。现实中代理人可以选择搜索强度、投入质量、搜索方向，这会引入 moral hazard 与 multi-dimensional effort。

第四，收益分成 $r$ 在主模型中固定，且双方风险中性。现实合同可能包含保底、奖金、里程碑付款、声誉收益等多种激励。

第五，搜索结果 i.i.d. 且委托人偏好已知。许多真实搜索包含学习、路径依赖和委托人偏好不透明，这会使信息反馈同时传递“结果质量”和“委托人口味”。

### 未来方向

1. **有限承诺与声誉。** 研究委托人无法完全承诺 acceptance standards 时，是否存在可持续的 relational feedback equilibrium。

2. **代理人有私人信号。** 将模型扩展为 information design with informed receivers，分析委托人反馈如何与代理人自有信息相互作用。

3. **内生搜索努力。** 让代理人同时选择是否搜索与搜索强度/质量，考察信息反馈能否同时激励 extensive margin 与 intensive margin。

4. **多代理人或竞争搜索。** 在多个 recruiter、多个 R&D partner 或多个学生并行搜索时，反馈还会影响竞争、信息外部性和资源分配。

5. **实证检验。** 在招聘平台、研发 pipeline 或学术实验记录中测试 threshold-style feedback 是否比 detailed feedback 更能延长有效搜索并提升终止结果。

6. **委托人偏好学习。** 若代理人不确定委托人到底喜欢什么，消息会同时传递项目质量和委托人偏好，这会形成更高维的动态 persuasion 问题。

## 一句话复盘

本文的核心不是“搜索应该何时停止”，而是：**当停止权和信息权分离时，委托人如何把 stopping threshold 变成一种让代理人愿意继续搜索的信息激励机制。**

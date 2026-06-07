# Pricing AI as a Service

作者：Ilan Lobel（NYU Stern School of Business），Yanwei Sun（Imperial Business School），Jiahua Wu（Imperial Business School）  
年份 / 版本：2026，This version: February 17, 2026  
期刊 / 状态：Working Paper

## 中文摘要

本文研究 AI as a Service（AIaaS）的定价问题：一个垄断型 AI 服务商向下游企业出售 AI agent/model 的访问权。文章聚焦两类现实中常见的计费方式：conversation-based pricing（CBP），即每次调用或每个 conversation 收固定费用；outcome-based pricing（OBP），即只有 AI 成功完成任务时才收费。买方同时拥有两类私人信息：使用 AI 的价值 $v_t(a)$，以及任务难度所决定的 AI 成功概率 $\gamma_t(a)$。

文章的核心结论是：CBP 本质上退化为标准的一维筛选问题，而 OBP 因为支付只在成功时发生，会把成功概率嵌入激励约束，从而形成更复杂的二维筛选问题。OBP 优于 CBP 的关键条件，不是“成功付费更公平”这么简单，而是买方的 per-success value $\phi_t(a)=v_t(a)/\gamma_t(a)$ 是否与成功概率 $\gamma_t(a)$ 对齐。如果愿意为一次成功支付更高价格的客户，也确实更经常成功，则 OBP 更强；如果高 per-success value 来自“任务很难、成功很少”，则 OBP 可能吸引看似高 WTP 但实际亏钱的客户，此时 CBP 更稳健。

## 论文速览表格

| 维度 | 内容 |
|:---|:---|
| 研究问题 | AIaaS provider 应该采用按调用收费（CBP）还是按成功收费（OBP）？在买方价值与任务难度均为私人信息时，最优菜单如何设计？ |
| 应用场景 | 客服 AI agent、IT help desk、自动化工作流、AI front-end + human escalation 的服务系统。 |
| 方法 | 机制设计 / screening model；二元类型基准模型；separable specification；queueing application；many-type extension；posted-pricing appendices。 |
| 核心机制 | OBP 的支付基准是“成功”，但 provider 的成本按“调用”发生；因此 OBP 的 WTP 度量 $v/\gamma$ 与利润度量 $\gamma p-c$ 之间可能错位。 |
| 核心结论 | OBP 胜出当且仅当 per-success value 与 success probability 对齐；错位时 CBP 更稳健。CBP 至少可保证二阶最优收入的一半，OBP 最坏情况下可任意差。 |
| 理论贡献 | 将 AI 服务的 stochastic performance、post-allocation signal 与多维私人信息引入 AIaaS 定价；提出 CBP vs. OBP 的 alignment principle。 |
| 管理含义 | 不要只看客户愿意为一次成功支付多少钱；还要看成功发生频率和每次调用成本。OBP 适合“成功强烈代表价值”的场景，CBP 适合成功概率与 per-success value 错位或成功难以覆盖成本的场景。 |

## TL;DR

这篇文章说明，AI 服务按成功收费不一定比按调用收费更好。关键在于：那些愿意为“成功”付高价的客户，是不是也真的经常成功；如果他们只是因为任务很难、成功很少才愿意给高单次成功价，OBP 反而会让平台亏钱。

对 OM/Marketing PhD 学生来说，本文最值得记住的是一个清晰的定价原则：**AIaaS 的最优 pricing metric 取决于 value metric 与 operational success metric 是否对齐**。这把机制设计中的 screening 与 OM 中的服务能力 / congestion / escalation 机制连接了起来。

## One More Thing

一个看似合理的直觉是：按成功收费更“value-based”，所以应该更适合 AI agent。本文最精妙的反转是：**愿意为成功付高价，可能恰恰说明这个客户很危险**。例如，一个客户的任务极难，AI 成功概率极低，但一旦成功价值很高，于是它愿意接受很高的 success fee。问题是 provider 每次调用都要付 inference cost，而这个客户很少成功、很少付款。于是，OBP 可能把“高愿付价格客户”误判成“高利润客户”。这正是本文对当前 AI agent pricing 讨论最有穿透力的地方。

## 研究背景与动机 (Motivation)

### 实践痛点

AIaaS 与传统 SaaS 的成本结构不同。SaaS 常用 seat-based subscription，边际成本相对低；AI 服务每次 request 都有 inference cost，因此简单按 seat 或订阅收费可能无法反映真实成本。文章将现实中的两类 pricing format 抽象为：

1. **CBP / usage-based pricing**：每次调用、每个 session 或每个 conversation 收固定费用。
2. **OBP / pay-per-success pricing**：只有 AI 达成可验证成功结果时收费。

在客服场景中，CBP 的优点是 provider 每次调用都能覆盖部分成本，但客户面临需求激增时账单不可控的风险；OBP 更接近 value-based pricing，也能降低客户采用风险，但它将 revenue 与 stochastic success 绑定，可能使 provider 暴露在成功概率很低的客户身上。

### 理论缺口

现有 SaaS pricing / nonlinear pricing 研究通常把价值作为主要私人信息，较少将“任务难度导致的成功概率”作为另一维私人信息纳入定价。传统 performance-based contracting 更关注 moral hazard：agent 的努力影响结果；而本文中 provider 是执行 AI 服务的一方，问题不是隐藏努力，而是买方知道自己的任务难度与成功概率。

本文填补的缺口是：在 AI 服务中，**performance outcome 既是付款条件，又是关于买方类型的 post-allocation signal**。这使 OBP 不只是 CBP 的重新标价，而是一个带有 type-dependent payment weight 的二维 screening 问题。

### 核心贡献

1. 将 AIaaS 中的调用成本、随机成功、任务难度私人信息纳入统一机制设计框架。
2. 证明 CBP 退化为标准一维 screening，而 OBP 产生特有的二维筛选与非标准 binding pattern。
3. 提出 CBP vs. OBP 的核心选择原则：per-success value 与 success probability 的 alignment。
4. 将理论应用到 customer-service queueing system，说明 AI 能力与 human service capacity 的相对匹配决定哪种 pricing 更优。

## 模型设定与假设 (Model Setup & Assumptions)

### 符号体系

#### 玩家与类型

| 符号 | 含义 | 备注 / 描述 |
|:---|:---|:---|
| Seller / provider | 垄断 AIaaS 服务商 | 提供不同 AI capability level，并设计定价菜单。 |
| Buyer | 下游企业 / 用户 | 使用 AI 完成任务或处理工作流。 |
| $t\in\{1,2\}$ | 买方类型 | 基准模型为二元类型；Section 5 扩展到 $n$ 个类型。 |
| $\pi_t$ | 类型 $t$ 的先验概率 | $\pi_t>0$ 且 $\sum_t \pi_t=1$。 |

#### AI 能力、成本与价值

| 符号 | 含义 | 备注 / 描述 |
|:---|:---|:---|
| $a\in A$ | AI capability level | 可理解为模型 tier、推理努力或 agent 能力水平。 |
| $c(a)$ | provider 提供能力 $a$ 的成本 | 严格递增且凸；捕捉更强模型 / 更多 inference effort 的成本。 |
| $v_t(a)$ | 类型 $t$ 买方使用 AI 能力 $a$ 的期望价值 | 可来自任务完成价值，也可来自 congestion reduction。 |
| $\gamma_t(a)$ | 类型 $t$ 在能力 $a$ 下 AI 成功概率 | 反映任务难度、数据质量、流程复杂度等私人信息。 |
| $a_t^{FB}$ | 类型 $t$ 的 first-best capability | $a_t^{FB}\in\arg\max_{a\in A}\{v_t(a)-c(a)\}$。 |

#### 结果与支付

| 符号 | 含义 | 备注 / 描述 |
|:---|:---|:---|
| $\omega\in\{\omega_0,\omega_1\}$ | AI 输出结果 | $\omega_1$ 表示成功，$\omega_0$ 表示失败。 |
| $p_t$ | 成功时支付 | buyer 选择类型 $t$ 合同时，若成功则支付 $p_t$。 |
| $w_t$ | 失败时支付 | buyer 选择类型 $t$ 合同时，若失败则支付 $w_t$。 |
| CBP | conversation-based pricing | 约束为 $p_t=w_t$，无论成功失败都收同一价格。 |
| OBP | outcome-based pricing | 约束为 $w_t=0$，只在成功时收 $p_t$。 |
| $\phi_t(a)$ | per-success value | $\phi_t(a)=v_t(a)/\gamma_t(a)$，OBP 下的核心 WTP 指标。 |

### 博弈 / 决策结构

Players：一个垄断 AI provider 与一个下游 buyer。

Sequence of Events：

1. Nature 抽取买方类型 $t$，买方知道自己的 $v_t(\cdot)$ 与 $\gamma_t(\cdot)$，seller 只知道先验分布与类型空间。
2. Seller 设计直接机制菜单 $\{(a_t,p_t,w_t)\}_{t\in\{1,2\}}$。
3. Buyer 选择一个菜单项或选择外部选项。
4. AI 以所选 capability $a$ 处理任务，结果 $\omega\in\{\omega_0,\omega_1\}$ 实现。
5. 若成功支付 $p$，失败支付 $w$；双方获得相应 payoff。

Information Structure：

买方拥有双维私人信息：价值 $v_t(a)$ 与成功概率 $\gamma_t(a)$。Seller 可以观察并验证 ex post outcome，但不能直接观察买方的真实任务难度和价值。

### 目标函数与约束

若真实类型为 $t$，但选择为类型 $s$ 设计的菜单项 $(a_s,p_s,w_s)$，买方期望效用为

$$
U_t(s)=v_t(a_s)-\gamma_t(a_s)p_s-[1-\gamma_t(a_s)]w_s.
$$

> 直觉：$v_t(a_s)$ 是 AI 服务给 buyer 带来的期望价值；$\gamma_t(a_s)p_s$ 是成功状态下的期望支付；$[1-\gamma_t(a_s)]w_s$ 是失败状态下的期望支付。OBP 的特殊性就在于 $p_s$ 被 $\gamma_t(a_s)$ 缩放，因此同一个 success fee 对不同类型的“痛感”不同。

Seller 从真实类型 $t$ 选择菜单项 $s$ 获得的期望净收入为

$$
\Pi_t(s)=\gamma_t(a_s)p_s+[1-\gamma_t(a_s)]w_s-c(a_s).
$$

> 直觉：seller 的 revenue 是按 outcome 加权的期望 payment；成本 $c(a_s)$ 则只取决于提供的 AI capability。OBP 下 seller 只有成功才收钱，但成本每次服务都会发生，因此 success probability 直接决定 profitability。

Individual Rationality（IR）约束为

$$
U_t(t)\ge 0,\quad t\in\{1,2\}.
$$

> 直觉：每类 buyer 至少要不低于外部选项，否则不会采用 AI 服务。

Incentive Compatibility（IC）约束为

$$
U_t(t)\ge U_t(s),\quad t,s\in\{1,2\},\;s\ne t.
$$

> 直觉：真实类型 $t$ 的 buyer 不应愿意伪装成另一类型。OBP 的 IC 更复杂，因为 deviation contract 的吸引力同时取决于该类型在那个 capability 下的价值和成功概率。

Second-best revenue maximization problem 为

$$
\max_{\{a_t,p_t,w_t\}_{t=1,2}}\sum_{t=1}^2 \pi_t\left[\gamma_t(a_t)p_t+(1-\gamma_t(a_t))w_t-c(a_t)\right]
$$

subject to IR and IC constraints.

> 直觉：seller 希望在保证 buyer 自愿参与且诚实选择菜单项的前提下，最大化期望净收入。允许 $p_t$ 与 $w_t$ 同时存在时，结果本身提供了额外筛选信息；限制为 CBP 或 OBP 时，则分别代表现实中更易实施的收费格式。

### 关键假设

| 假设 | 合理性说明 | 放松后的可能影响 |
|:---|:---|:---|
| 垄断 provider | 许多 AIaaS 市场存在模型能力、数据、生态或切换成本带来的市场势力。 | 竞争会压缩 rent extraction，也可能使 OBP 成为差异化竞争工具。 |
| 二元可验证 outcome | 客服中“是否解决问题 / 是否升级人工”较容易二元化。 | 多级 outcome 或模糊 success definition 会引入 measurement / gaming 问题。 |
| 买方知道任务难度与价值 | 企业通常比 provider 更了解自身数据质量、流程复杂度、客户请求结构。 | 若 provider 可学习类型，则会形成动态筛选与 experimentation 问题。 |
| 成本只取决于 capability $a$ | 反映模型 tier 或 inference effort 的边际成本。 | 若成本也受类型或请求长度影响，则 CBP/OBP 比较会更依赖 cost-to-serve。 |
| Quasilinear risk-neutral utility | 标准机制设计设定，便于分析 transfer 与 screening。 | 风险厌恶或预算约束会强化 OBP 对 buyer 的吸引力，也可能让 CBP 因账单风险受限。 |
| Seller 可承诺菜单 | 合同签订后按菜单执行。 | 若无法承诺，动态 renegotiation 或 ex post dispute 会削弱 OBP。 |
| Second-best 允许负支付 | 用于理论 benchmark，说明 post-allocation signal 的筛选能力。 | 现实中 limited liability 通常禁止 provider 补贴 buyer，因此更应关注 CBP/OBP 等受限机制。 |

## 分析路线图 (Roadmap of Analysis)

1. **Unrestricted second best**：先允许同时设置 success fee $p_t$ 与 failure fee $w_t$，问 post-allocation outcome 是否足以恢复 first-best revenue。
2. **CBP benchmark**：加入 $p_t=w_t$ 约束，使支付不依赖结果；问题退化为标准 one-dimensional screening。
3. **OBP main model**：加入 $w_t=0$ 约束，只能按成功收费；分析其特有的二维筛选、binding pattern 与 virtual type。
4. **CBP vs. OBP comparison**：比较两种现实 pricing format，提出 alignment principle。
5. **Separable specification**：设 $v_t(a)=\theta_t h(a)$、$\gamma_t(a)=\alpha_t s(a)$，获得更清晰的闭式比较静态。
6. **Queueing application**：把 buyer value 具体化为 human queue congestion reduction，解释客服 AI 中何时 OBP / CBP 更合适。
7. **Many-type extension**：扩展到多类型，给出 supporting-line condition、ironing algorithm，并说明 alignment logic 继续成立。
8. **Posted-pricing appendix**：单一 AI tier 下给出更简单的 posted-price 版本，强化主文机制的直觉。

## 核心分析与求解 (Analysis & Solution)

### Proposition 1：二元类型下 unrestricted second best 可达到 first best

第一步建立 benchmark：如果 seller 可以同时对成功和失败收费，那么 outcome-contingent transfers 足以利用 post-allocation signal 做筛选。

当 $\gamma_1(a_t^{FB})\ne \gamma_2(a_t^{FB})$ 对每个 $t$ 成立时，存在菜单使得 $a_t^*=a_t^{FB}$，并通过合适的 $(p_t^*,w_t^*)$ 完全抽取 surplus，从而达到

$$
R^{FB}=\sum_{t=1}^2\pi_t\left[v_t(a_t^{FB})-c(a_t^{FB})\right].
$$

> 经济直觉：成功 / 失败结果虽然只有一个二元 signal，但在二元类型下已经足以区分两类 buyer 的 expected payment。通过同时调节成功费与失败费，seller 可以让每个类型在自己合同上零 surplus，同时不想模仿对方。问题是，这种机制可能要求 $p_t^*<0$ 或 $w_t^*<0$，即 seller 在某些状态下补贴 buyer，现实中不太可行。

### Proposition 2：CBP 退化为标准 screening

有了 unrestricted benchmark 后，文章转向现实可执行的 CBP。CBP 要求 $p_t=w_t$，因此支付与结果无关。

在 CBP 下，成功概率 $\gamma_t(a)$ 从 buyer utility 中消失，问题只由 $v_t(a)$ 决定。若 first-best allocations 满足 “uncontested” condition：

$$
v_1(a_1^{FB})\ge v_2(a_1^{FB}),\quad v_2(a_2^{FB})\ge v_1(a_2^{FB}),
$$

CBP 可达到 first best。若进一步满足标准 increasing differences，则出现经典结构：高价值类型无扭曲，低价值类型向下扭曲，低类型 IR 与高类型 IC 绑定。

> 经济直觉：CBP 是“按任务收费”，seller 每次调用都收同样的钱。任务难度和成功概率不会影响 payment weight，因此筛选维度只有价值。它稳健、简单，但没有利用 success outcome 中关于类型的信息。

### Proposition 3：OBP 的 first-best 条件是 per-success uncontestedness

接下来文章切换到 OBP。OBP 只能设置 success fee，即 $w_t=0$。于是 buyer 是否接受合同由 per-success value 决定：

$$
\phi_t(a)=\frac{v_t(a)}{\gamma_t(a)}.
$$

OBP 达到 first best 的充要条件为

$$
\phi_1(a_1^{FB})\ge \phi_2(a_1^{FB}),\quad \phi_2(a_2^{FB})\ge \phi_1(a_2^{FB}).
$$

此时最优 success fee 为

$$
p_t^*=\phi_t(a_t^{FB}).
$$

> 经济直觉：OBP 下 seller 向类型 $t$ 抽取全部 surplus 的方式，是把成功费设为该类型在该 capability 下愿意为一次成功支付的最高价格 $v_t/\gamma_t$。但如果另一个类型在该 allocation 下的 per-success value 更高，它就会被吸引过来，破坏 IC。因此 OBP 的 uncontestedness 不再看 $v$，而是看 $v/\gamma$。

### Remark / Observation：OBP 不是 CBP 的简单重标价

Proposition 3 之后，文章强调 OBP 的 incentive structure 与标准 screening 不同。OBP 中甚至可能出现两个 IC 都绑定、两个 IR 都不绑定的最优情形；这在 canonical one-dimensional screening 中不会发生。

> 经济直觉：CBP 中，统一提高所有价格会等比例降低所有类型 utility，因此总能把某个 IR 压到绑定。但 OBP 中，提高 success fee 对不同类型的影响是 $\gamma_t(a)p$，即由类型和 allocation 共同决定。价格变化不再是“平移”，而是“倾斜”，所以 IC 可能先成为最紧约束。

### Theorem 1：OBP 的最优菜单与 OBP-specific virtual type

为刻画 OBP，文章提出 OBP-specific increasing differences condition。核心对象是 OBP rent gap：

$$
\Delta(a)=v_2(a)-\frac{\gamma_2(a)}{\gamma_1(a)}v_1(a).
$$

在 Assumption 1 下，存在最优 OBP 菜单满足：

1. allocation monotonicity：$a_1^*\le a_2^*$；
2. binding pattern：IR1 与 IC2 绑定，IR2 冗余，IC1 自动满足；
3. allocation 由以下 reduced program 决定：

$$
\max_{a_1\le a_2}\;\pi_1\left[v_1(a_1)-c(a_1)\right]+\pi_2\left[v_2(a_2)-c(a_2)\right]-\pi_2\Delta(a_1).
$$

> 经济直觉：这与标准 screening 很像，但 information rent 不再是 $v_2(a_1)-v_1(a_1)$，而是经过 success probability ratio 调整后的 $\Delta(a_1)$。OBP 的 virtual type 不是简单地从低类型 valuation 中扣除高类型 rent，而是扣除“success-weighted rent”。这就是 AI 成功概率进入 screening 的核心数学位置。

**关键 trade-off：OBP 把 $\phi=v/\gamma$ 作为 willingness-to-pay 指标，但 provider 的利润是 $\gamma p-c$。当 $\phi$ 与 $\gamma$ 对齐时，OBP 把价值和收入对齐；当二者错位时，OBP 可能把低成功概率客户误判成高价值客户。**

### Theorem 2：CBP 与 OBP 的主比较结论

在刻画两个机制后，文章直接比较最优 CBP 与最优 OBP 收入。

核心结果包括：

1. 若 $\gamma_1(a)=\gamma_2(a)$ 对所有 $a$ 成立，则

$$
R_{OBP}^*=R_{CBP}^*.
$$

2. 若 CBP 的 uncontested condition 成立，则 CBP 达到 first best 并弱优于 OBP；若 OBP 的 per-success uncontested condition 成立，则 OBP 达到 first best 并弱优于 CBP。
3. 在 CBP-ID 与 OBP-ID 均成立的 aligned-order 情况下：

$$
\frac{\gamma_2(a)}{\gamma_1(a)}\ge 1\ \forall a \Rightarrow R_{OBP}^*\ge R_{CBP}^*,
$$

$$
\frac{\gamma_2(a)}{\gamma_1(a)}\le 1\ \forall a \Rightarrow R_{OBP}^*\le R_{CBP}^*.
$$

> 经济直觉：如果成功事件对类型没有额外信息，OBP 与 CBP 只是价格尺度不同。如果 high per-success value 类型也有更高成功概率，那么按成功收费是更好的筛选和变现工具；如果 high per-success value 类型反而更少成功，则 OBP 收入基础变弱，CBP 更好。

### Proposition 4：CBP 有稳健性保证，OBP 没有

接着文章给出 worst-case ratio：

$$
\sup\frac{R_{OBP}^*}{R_{CBP}^*}=2,
\quad
\sup\frac{R_{SB}^*}{R_{CBP}^*}=2,
\quad
\sup\frac{R_{CBP}^*}{R_{OBP}^*}=+\infty,
\quad
\sup\frac{R_{SB}^*}{R_{OBP}^*}=+\infty.
$$

> 经济直觉：CBP 至少可以用一个 per-use price 服务最赚钱的 segment，因此在二元类型下至少拿到 second-best 的一半。OBP 则可能被低成功概率、高 per-success value 的类型拖垮：这些类型接受很高成功费，但因为很少成功，expected payment 覆盖不了每次调用成本。

### Theorem 3 / 4：Separable specification 下的闭式比较

为了得到更清晰的 comparative statics，文章设定

$$
v_t(a)=\theta_t h(a),\quad \gamma_t(a)=\alpha_t s(a),\quad \theta_2\ge \theta_1.
$$

此时 CBP 按 $\theta_t$ 排序，OBP 按

$$
\phi_t=\frac{\theta_t}{\alpha_t}
$$

排序。

CBP 的低类型 virtual type 为

$$
\tilde{\theta}_1=\theta_1-\frac{\pi_2}{\pi_1}(\theta_2-\theta_1).
$$

当 $\phi_2\ge \phi_1$ 时，OBP 的对应 virtual type 为

$$
\hat{\theta}_1=\theta_1-\frac{\pi_2}{\pi_1}\left(\theta_2-\frac{\alpha_2}{\alpha_1}\theta_1\right).
$$

主要比较结论：若 $\phi_2\ge \phi_1$，则

$$
R_{OBP}^*\ge R_{CBP}^*\iff \alpha_2\ge \alpha_1.
$$

若 $\phi_2<\phi_1$，则类型在 CBP 与 OBP 下的排序发生反转，OBP 可能出现 separation 或 pooling；在 separation region，CBP 弱优于 OBP；在 pooling region，存在 cutoff $\varphi(\alpha_1)$ 决定 OBP 是否胜出。

> 经济直觉：separable case 把文章的 alignment logic 表达得最干净。$\theta$ 是“总价值”排序，$\alpha$ 是“成功概率”排序，$\phi=\theta/\alpha$ 是“每次成功价值”排序。OBP 需要 $\phi$ 与 $\alpha$ 同向；CBP 更依赖 $\theta$。当二者排序冲突，OBP 的筛选方向与利润来源方向不一致，可能需要 pooling，甚至被迫服务不理想的客户组合。

### Corollary 1：Queueing application 中的 AI-human capability alignment

文章将模型应用到客服 / help desk 队列。类型 $t$ 企业有请求到达率 $\lambda_t$ 与人工服务率 $\mu_t$，baseline utilization 为

$$
\rho_t=\frac{\lambda_t}{\mu_t}\in(0,1).
$$

AI 先处理请求；以概率 $\gamma_t(a)$ 成功解决，否则升级到人工队列。因此人工系统的有效到达率变为

$$
(1-\gamma_t(a))\lambda_t,
$$

对应 utilization 为

$$
(1-\gamma_t(a))\rho_t.
$$

买方价值来自 steady-state congestion cost reduction，即

$$
v_t(a)=v(\rho_t,\gamma_t(a)).
$$

若 $\gamma_t(a)=\alpha_t s(a)$，则 CBP 与 OBP 的相对优劣取决于 AI success capability 与 human service rate 是否对齐。

> 运营直觉：如果某 segment 的 AI 更容易成功，而且它的人工系统也很快，那么 AI 成功带来的边际拥堵缓解不大，CBP 往往更好。若某 segment AI 容易成功但人工 capacity 紧张，AI 成功正好缓解瓶颈，此时“成功”更能代表真实价值，OBP 更好。换言之，OBP 适合 success 是 value 的强 proxy 的场景。

### Theorem 5 / 6：多类型扩展

在多类型模型中，unrestricted second best 不一定总能达到 first best。文章给出 supporting-line condition：对每个类型 $t$，存在斜率 $d_t$ 使得

$$
v_t(a_t^{FB})-d_t\gamma_t(a_t^{FB})\ge v_s(a_t^{FB})-d_t\gamma_s(a_t^{FB}),\quad \forall s.
$$

若该条件对所有类型成立，则 second best 达到 first best。离散 concavity 是一个简单充分条件。

在 separable many-type 情况下，CBP 与 OBP 都可通过 virtual type 和 ironing 求解。若 $\theta$ 排序与 $\phi$ 排序一致，则：

$$
\alpha_1\le\alpha_2\le\cdots\le\alpha_n \Rightarrow R_{OBP}^*\ge R_{CBP}^*,
$$

$$
\alpha_1\ge\alpha_2\ge\cdots\ge\alpha_n \Rightarrow R_{CBP}^*\ge R_{OBP}^*.
$$

> 经济直觉：多类型并没有改变主机制，只是把二元类型的 alignment condition 推广为排序条件。OBP 需要“越愿意为成功付费的类型，也越经常成功”；如果排序反向，CBP 更优。技术上，many-type screening 需要 ironing，但管理直觉仍是同一个。

## 比较静态汇总表 (Comparative Statics Summary)

| 参数变化 / 条件 | 对 CBP 的影响 | 对 OBP 的影响 | 直觉 |
|:---|:---|:---|:---|
| $\gamma_1(a)=\gamma_2(a)$ | 与 OBP 等价 | 与 CBP 等价 | 成功事件不含类型信息，OBP 只是 CBP 的缩放。 |
| high-$\phi$ 类型的 $\gamma$ 上升 | 相对吸引力下降 | 相对吸引力上升 | 高 per-success WTP 也更常付款，OBP 的筛选和收入基础对齐。 |
| high-$\phi$ 类型的 $\gamma$ 下降 | 相对吸引力上升 | 相对吸引力下降 | 高 success fee 被低成功概率稀释，可能无法覆盖调用成本。 |
| $\phi_t$ 与 $\gamma_t$ 同向排序 | CBP 弱化 | OBP 强化 | success 是 value 的好 proxy。 |
| $\phi_t$ 与 $\gamma_t$ 反向排序 | CBP 强化 | OBP 弱化 | 愿付高成功价的客户反而少成功，OBP 误筛选。 |
| separable case 中 $\alpha_2/\alpha_1\uparrow$ 且 $\phi_2\ge\phi_1$ | $R_{CBP}^*$ 不直接受成功概率排序增强 | $R_{OBP}^*$ 相对上升 | OBP virtual type 中 rent penalty 被 success ratio 调整，低类型扭曲减轻。 |
| queueing 中高 AI 成功 segment 的 $\rho$ 上升 | 相对弱化 | 相对强化 | 人工系统更拥堵，AI 成功更有价值，OBP 更能 capture value。 |
| queueing 中高 AI 成功 segment 的 $\mu$ 上升 | 相对强化 | 相对弱化 | 人工系统更快，AI 成功边际价值下降，按成功收费优势减弱。 |
| 类型数 $n$ 增加 | 仍有 $1/n$ 级别稳健保证 | worst-case 仍可任意差 | CBP 可 target 最赚钱 segment；OBP 可能被低成功概率类型污染。 |

## 主要结论与管理启示 (Main Results & Managerial Insights)

### 与 Benchmark 的对比

| 机制 | 支付形式 | 筛选变量 | 优点 | 缺点 / 风险 |
|:---|:---|:---|:---|:---|
| Unrestricted second best | 成功费 $p$ + 失败费 $w$ | outcome-contingent expected payment | 二元类型下可达到 first best | 可能需要负支付，现实执行困难。 |
| CBP | $p=w$，每次调用固定收费 | 总价值 $v$ | 稳健、收入确定、可覆盖调用成本 | 不利用 success outcome，客户承担需求波动账单风险。 |
| OBP | $w=0$，只在成功收费 | per-success value $v/\gamma$ | 与结果和客户价值更贴近，降低 buyer 采用风险 | 可能吸引低成功概率客户，expected revenue 不足以覆盖调用成本。 |
| Separable / many-type optimal menus | virtual type + ironing | CBP 看 $\theta$，OBP 看 $\theta/\alpha$ | 给出可计算结构 | 若排序混乱，OBP 可能 pooling，解析比较复杂。 |

### 管理建议

1. **不要把 high success fee acceptance 等同于 high profitability。** 对 OBP 来说，客户愿意支付的 success fee 上限是 $v/\gamma$，但平台 expected margin 是 $\gamma p-c$。
2. **采用 OBP 前必须估计 segment-level success probability。** 如果高 per-success WTP 客户成功概率低，OBP 会系统性低估服务成本风险。
3. **当 success 是 value 的强 proxy 时，优先考虑 OBP。** 例如 AI 成功能显著减少人工升级、缩短拥堵时间、避免高成本人工处理。
4. **当 AI 成功概率与客户价值错位时，优先考虑 CBP 或 hybrid pricing。** 可用 fixed fee + success bonus、minimum monthly fee、usage floor 等机制避免 OBP 的 downside。
5. **客服 AI 场景中，定价应同时看 AI capability 和 human capacity。** 若 AI 对某类请求成功率高且人工系统拥堵，OBP 更合理；若 AI 对某类请求成功率高但人工系统本来很快，CBP 更稳。
6. **菜单设计应围绕“任务难度”而非仅围绕客户规模。** 企业级客户的请求量大不等于成功概率高；高规模客户可能反而拥有复杂流程和低 AI 成功率。

## 与相关文献的对话 (Dialogue with Literature)

### Mussa and Rosen (1978) / classic nonlinear pricing

共同关注点是垄断卖方面对私人信息买方时如何设计质量 / 价格菜单。本文的 CBP 部分几乎回到标准 nonlinear pricing：买方类型由 $v_t(a)$ 排序，高类型获得更高质量，低类型被扭曲。

区别在于，OBP 让支付受到 type-dependent success probability 缩放，因此筛选变量从 $v$ 变成 $v/\gamma$，并产生非标准 binding pattern。这一点对 AIaaS 很重要，因为 AI 服务的质量并不是确定产出，而是 stochastic completion。

### Haghpanah and Siegel (2025) / screening two types

该文刻画了二元类型 screening 的一般结构，不必强加传统 single-crossing 条件。本文在 CBP 部分直接借助这种视角解释 first-best attainable 的 uncontested condition。

本文的推进在于把 uncontestedness 从 value metric 推广到 per-success metric：CBP 看 $v_t(a)$，OBP 看 $\phi_t(a)=v_t(a)/\gamma_t(a)$。这使得同一组 buyer 在两种机制下可能有完全不同的“高类型”。

### Riordan and Sappington (1988) / post-allocation signals

共同点是 contract 可以利用 ex post signal 改善 screening。本文中 success/failure outcome 是一个 post-allocation signal，与买方任务难度相关。

关键区别是本文关注 AIaaS 的现实 pricing restrictions。虽然 unrestricted outcome-contingent transfer 可达到 first best，但现实中负支付和复杂状态支付难以执行，因此主问题转向 CBP 与 OBP 这两个受限机制的比较。

### Bergemann, Bonatti, and Smolin (2025b) / economics of LLM markets

共同点是都把 LLM / AI 服务看作有非零 marginal cost 的经济产品，强调 token / inference 成本改变传统软件定价。

本文的区别是聚焦 stochastic performance 与下游 task difficulty 的私人信息，尤其是“成功概率”如何改变 outcome-based pricing 的 screening logic。它更接近 OM 中服务系统与 Marketing 中 pricing metric choice 的交叉。

## 犀利评论 (Reviewer's Critique)

### 优点

理论贡献清晰：文章把 AIaaS pricing 中最现实的两个合同格式 CBP 与 OBP 放入一个统一机制设计框架，并提炼出非常有传播力的 alignment principle。

方法上，文章既有 unrestricted benchmark，也有受限机制比较、separable closed-form、queueing application 和 many-type extension，结构完整。特别是 OBP-specific virtual type 把成功概率直接放进 information rent，是文章最核心的技术贡献。

实践相关性强：当前 AI agent pricing 的行业讨论确实围绕 per conversation vs. per resolution / per outcome 展开，本文提供了判断何时该用哪种 metric 的理论语言。

### 模型限制 / 假设过强

1. **Success 被假设为二元且可验证。** 现实中“成功解决”常常有灰度，例如客户满意、后续复联、部分解决、错误解决但未升级等。若 success measurement 可被操纵，OBP 的可实施性会显著下降。
2. **Provider 的 effort / model investment 没有 moral hazard。** OBP 现实中也会激励 provider 提高成功率，但本文把 $\gamma_t(a)$ 作为 capability 与类型共同决定的外生函数，未分析 provider effort incentives。
3. **买方 risk neutrality 与预算风险被弱化。** 文章动机中提到 CBP 会带来账单波动风险，但主模型用 quasilinear expected utility，未充分建模风险厌恶或预算约束；这可能低估 OBP 对 buyer adoption 的价值。
4. **垄断假设限制了 marketing competition insight。** 在竞争市场中，OBP 可能不仅是筛选工具，也是降低试用门槛、传递质量信号或抢占客户的竞争策略。
5. **客户类型是静态的。** AI provider 在实际部署中会逐步学习客户成功概率，并可调整合同；动态学习可能改变 CBP 与 OBP 的相对优劣。

### 未来研究方向

1. **Hybrid pricing design**：研究 fixed platform fee + per-use fee + success bonus 的三部制合同，检验是否能同时保留 CBP 稳健性与 OBP 的 value alignment。
2. **Competition between AIaaS providers**：分析一个 provider 采用 OBP、另一个采用 CBP 时的均衡，尤其是 OBP 是否成为质量信号或市场进入工具。
3. **Dynamic learning and contract updating**：将 $\gamma_t$ 设为 provider 通过使用数据逐渐学习的对象，研究 introductory OBP、后续 CBP 或个性化菜单的动态路径。
4. **Endogenous AI investment / moral hazard**：让 provider 选择模型训练、fine-tuning 或 human-in-the-loop effort，研究 OBP 如何影响质量投资激励。
5. **Empirical calibration in customer service AI**：用真实客服数据估计 $v(\rho,\gamma)$、$\gamma_t(a)$ 与 escalation cost，检验理论中的 alignment region 是否可被识别并用于定价实验。
6. **Outcome definition and gaming**：研究当 success definition 可由合同设计或双方争议决定时，OBP 的最优 measurable outcome 应如何选择。

## Seminar 阅读提示

如果以 OM/Marketing PhD 学生身份准备 seminar，建议重点追问三类问题。

第一，模型中的 $v_t(a)$ 与 $\gamma_t(a)$ 在现实数据中如何分开识别？很多时候 observed resolution rate 与 value uplift 同时受客户流程、请求类型和 AI model 影响。

第二，OBP 的失败不是因为它“按结果收费”本身不好，而是因为 payment event 与 cost event 不一致。是否可以通过 minimum fee、usage cap、risk-sharing 或 dynamic adjustment 修复？

第三，queueing application 的核心 insight 是 AI success 与 human capacity 的 complementarity / substitutability。这个方向可以进一步连接 service operations 中的 routing、staffing 与 outsourcing pricing。

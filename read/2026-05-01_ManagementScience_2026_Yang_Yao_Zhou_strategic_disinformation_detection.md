# Strategic Disinformation Generation and Detection

作者：Wenxiao Yang（University of California, Berkeley）、Yunfei (Jesse) Yao（The Chinese University of Hong Kong）、Pengxiang (Shawn) Zhou（University of Southern California）

期刊与年份：Management Science，2026（Articles in Advance, published online April 30, 2026）

中文摘要：本文研究“虚假信息生成者”和“检测器”之间的战略互动。发送者私下知道自己是高类型还是低类型，但无论真实类型如何都希望接收者采取对自己有利的行动；检测器会对发送者消息是否真实给出有噪声的警报信号。与既有文献常常只考虑漏报不同，本文同时考虑漏报和误报。核心发现是：检测越准确不一定让撒谎越少。当真阳性率较低时，更准确的检测会让“没有警报”更有说服力，反而提高低类型发送者撒谎的概率；当真阳性率较高时，更准确的检测才会通过警报的威慑作用降低撒谎概率。进一步地，最优检测器并不总是最大化真阳性率；由于误报会伤害真实的高类型发送者并改变接收者信念，设计者通常应选择中间水平的真阳性率。

## 论文速览表格

| 维度 | 内容 |
|:---|:---|
| 研究问题 | 当检测器会误报和漏报时，检测能力如何影响低类型发送者制造 disinformation 的激励？在分类技术受限下，平台或监管者应如何设计检测器？ |
| 研究对象 | fake reviews、社交媒体误导性内容、广告欺诈、虚假简历、诈骗邮件、平台上的低质量卖家伪装等。 |
| 方法 | 不完全信息动态博弈；sender-receiver signaling game；检测器设计可看作 constrained information design。 |
| 核心机制 | 检测器有两个信念效应：无警报带来的 persuasive effect 和有警报带来的 dissuasive effect。二者在不同真阳性率区间主导均衡。 |
| 主要结论 | 低类型撒谎概率关于检测真阳性率非单调：先升后降。误报存在时，即使检测器很强，均衡中仍会有一些撒谎。 |
| 最优设计 | 对任何给定真阳性率，设计者都选择最低可行误报率；但整体上不选择最高真阳性率，而选择中间水平。 |
| 与 benchmark 的差异 | 如果假设无误报，最优检测器总是越强越好；一旦允许误报，过高真阳性率伴随过高误报，反而可能降低接收者、高类型发送者和社会福利。 |
| 管理启示 | 平台不能只追求“多抓假内容”；应把误报成本、用户信念更新和造假者战略反应一起纳入阈值设计。 |

## TL;DR

这篇文章最核心的发现是：更强的检测器不一定让造假更少。在检测器还不够强时，“没有被标记”会让假消息更可信，因此低类型反而更愿意撒谎；只有当检测器足够强时，警报的威慑才会压低撒谎。

因此，平台设计 fake review detector 或 content moderation algorithm 时，不应机械地最大化 true-positive rate。因为更高 true-positive 往往伴随更多 false-positive，而误报会改变所有人的战略行为，最优检测强度通常是一个中间值。

## One More Thing

这篇文章最有意思的洞察是：**误报不是一个单纯的“技术噪音”，而是会改变造假者策略的战略变量。** 直觉上我们以为检测器越强，骗子越怕，所以谎言越少。但如果检测器会误报，那么“没有警报”本身就变成了一张背书。一个还不够强的检测器如果提高一点准确率，接收者会更相信未被标记的消息；低类型发送者看到这一点，反而更有空间混进“未被标记”的池子里。也就是说，检测器的进步在某个区间内会先制造更多撒谎，再在另一个区间内压制撒谎。这个“先升后降”的战略反应，是全文最值得记住的机制。

## 研究背景与动机 (Motivation)

### 实践痛点

平台经济和生成式 AI 使得 disinformation 的生产和传播更容易。论文列举的应用包括 fake reviews、ad fraud、manipulated transactions、fraudulent resumes 和 misleading posts。现实中，Yelp 会用自动系统识别补偿性或激励性评论并对商家发出 consumer alerts；Twitter/X 会对虚假或误导性内容贴标签；LinkedIn 使用大规模自动检测系统识别 fake accounts。这些检测器都面临同一个运营问题：要提高抓到假内容的概率，就可能提高误伤真内容的概率。

这正是 precision-recall 或 Type I/Type II error trade-off。本文尤其强调 false positives 的经济重要性：误报不仅会伤害真实用户或高质量商家，还会削弱平台声誉、降低交易效率，并改变发送者和接收者的战略行为。

### 理论缺口

既有 strategic communication 和 costly lying 文献已经研究了发送者如何通过信息影响接收者，也有工作研究“谎言可能被检测到”的情形。但很多相关模型隐含了一个强假设：检测器可能漏报，但不会误报，即 false-positive rate 为零。

本文认为这个假设在现实中很难成立。任何有用的分类器只要不是永远不报警，通常都会有误报；而一旦允许误报，模型结论就从“检测越强越好”变成“检测强度存在最优中间值”。

### 核心贡献

1. 同时建模 false negative 和 false positive，说明两类错误对战略沟通的影响并不对称。
2. 给出低类型发送者撒谎概率关于检测准确率的非单调关系：真阳性率低时更强检测增加撒谎，真阳性率高时更强检测减少撒谎。
3. 将检测器设计内生化：平台不是被动接受检测技术，而是在分类器能力约束下选择报警规则。
4. 说明最优检测器通常不是最高 true-positive rate，甚至在分类器更好时，最优检测器可能报警更少。

## 模型设定与假设 (Model Setup & Assumptions)

### 符号体系：参与者、类型与行动

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $S$ | Sender | 私下知道自己类型，发送关于自身类型的消息。 |
| $R$ | Receiver | 观察消息和检测信号后做二元决策。 |
| Designer | 检测器设计者 | 可理解为平台、监管者或系统设计者。 |
| $\theta \in \{H,L\}$ | 发送者类型 | $H$ 为高类型，$L$ 为低类型。 |
| $\rho$ | 高类型先验概率 | $\Pr(\theta=H)=\rho$。 |
| $r_H, r_L$ | 接收者行动 | $r_H$ 是发送者希望接收者采取的行动；$r_L$ 是拒绝或不采纳。 |
| $m_H, m_L$ | 发送者消息 | 声称自己是高类型或低类型。 |
| $l \in \{a,na\}$ | 检测器信号 | $a$ 表示 alarm，$na$ 表示 no alarm。 |

### 符号体系：收益

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $\Delta_H^S$ | 高类型发送者在 $R$ 采取 $r_H$ 时的收益 | 正数。 |
| $\Delta_L^S$ | 低类型发送者在 $R$ 采取 $r_H$ 时的收益 | 正数；低类型也想被当成高类型。 |
| $\Delta_H^R$ | 接收者面对高类型并采取 $r_H$ 的收益 | 正数。 |
| $\Delta_L^R$ | 接收者面对低类型却采取 $r_H$ 的损失 | 以正数表示损失规模。 |
| $C$ | 撒谎成本 | 包括道德成本、操纵成本、被事后处罚风险等。 |
| $\hat{\rho}$ | 接收者接受阈值 | 满足 $\hat{\rho}\Delta_H^R-(1-\hat{\rho})\Delta_L^R=0$。 |

接收者如果采取 $r_H$，其期望收益为

$$
b(H)\Delta_H^R-(1-b(H))\Delta_L^R.
$$

> 直觉：接收者只有在“对方是高类型”的后验信念足够高时才愿意采取 $r_H$。阈值 $\hat{\rho}$ 越高，说明低类型被误接纳的损失越大，接收者越谨慎。

发送者无论真实类型如何都偏好 $r_H$。如果发送者撒谎，则支付成本 $C$。

> 直觉：这个设置抓住了 disinformation 的本质。低质量商家、虚假账号或误导性内容生产者希望接收者相信其为高类型；真实高类型也希望被相信，但他们不需要撒谎。

### 符号体系：检测器

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $\beta$ | true-positive rate | 低类型撒谎时检测器报警的概率：$\Pr(l=a\mid m=m_H,\theta=L)$。 |
| $\alpha$ | false-positive rate | 高类型诚实时检测器误报警的概率：$\Pr(l=a\mid m=m_H,\theta=H)$。 |
| $s_L,s_H$ | 分类器输出 | $s_L$ 更像低类型/虚假，$s_H$ 更像高类型/真实。 |
| $\phi(s\mid\theta)$ | 分类器能力 | 给定真实类型下输出某信号的概率。 |
| $\lambda_L,\lambda_H$ | 报警规则 | 给定分类器输出 $s_L$ 或 $s_H$ 后，检测器报警的概率。 |

检测器的 true-positive 与 false-positive 由分类器能力和报警规则共同决定：

$$
\beta=\phi(s_L\mid L)\lambda_L+\phi(s_H\mid L)\lambda_H,
$$

$$
\alpha=\phi(s_L\mid H)\lambda_L+\phi(s_H\mid H)\lambda_H.
$$

> 直觉：分类器本身只是给出 noisy prediction；平台真正要决定的是如何把这个 prediction 转化成 alarm。也就是说，平台可以在同一个分类器基础上选择更保守或更激进的报警规则。

### 博弈结构

1. Designer 设计检测器，即选择报警规则，从而决定可行的 $\alpha$ 和 $\beta$。
2. Nature 抽取发送者类型 $\theta\in\{H,L\}$。
3. Sender 发送消息 $m\in\{m_H,m_L\}$。
4. Detector 根据消息和类型相关的噪声过程发出 $l\in\{a,na\}$。
5. Receiver 观察消息和检测器信号，选择 $r_H$ 或 $r_L$。

信息结构上，发送者知道自身类型；接收者不知道类型，但知道博弈结构、先验、检测器设计，并通过 Bayes rule 更新信念。均衡概念是 Perfect Bayesian Equilibrium。

### 关键假设

| 假设 | 合理性 | 放松后的可能影响 |
|:---|:---|:---|
| 类型为二元 $H/L$ | 便于刻画“高质量/低质量”“真实/虚假”的基本冲突。 | 连续类型会使报警阈值和消息策略更复杂，但 false-positive 的机制仍可能保留。 |
| 接收者行动为二元 $r_H/r_L$ | 对应购买/不购买、点击/不点击、转发/不转发等场景。 | 多行动或连续行动会引入更丰富的后验响应，但核心信念效应不变。 |
| 发送者总是偏好 $r_H$ | 捕捉卖家、内容创作者、诈骗邮件发送者等都希望被采纳。 | 若高低类型偏好不同，可能产生更多分离均衡。 |
| 撒谎有成本 $C>0$ | 来自道德、操纵、处罚或认知成本；也是 costly signaling 的关键。 | 若 $C=0$，低类型更倾向总是撒谎，检测器主要通过信息提供而非威慑发挥作用。 |
| 检测器可误报也可漏报 | 符合现实分类器的技术限制。 | 若误报被强行设为零，会得到“检测越强越好”的 benchmark 结论。 |
| 分类器能力外生，报警规则内生 | 改变模型训练能力很难，但调整阈值和报警政策较容易。 | 若分类器能力也内生，平台需权衡模型投资成本与战略行为收益。 |

## 分析路线图 (Roadmap of Analysis)

本文的分析结构非常清晰，是一层层把现实要素加进去。

1. **No-alarm benchmark**：先看没有检测器时，低类型如何混入高类型消息池。
2. **No-false-positive benchmark**：再看传统文献常用的设定，即检测器只会漏报不会误报。此时更高 $\beta$ 基本总是更好。
3. **Exogenous detector**：给定一个同时存在误报和漏报的检测器，分析发送者和接收者的均衡反应。这一步得到全文最重要的非单调撒谎结果。
4. **Endogenous detector design**：让平台在可行 ROC 约束下选择检测器，刻画最优 $\alpha$、$\beta$ 和报警规则。
5. **Extensions**：考虑报警规则受限，以及电商平台同时选择 commission fee 和检测器。

## 核心分析与求解 (Analysis & Solution)

### Lemma 1：高类型总是说真话

在任何 PBE 中，高类型发送者总是发送 $m_H$。如果 $m_L$ 在均衡路径上出现，接收者在看到 $m_L$ 后会选择 $r_L$。

> 直觉：高类型没有理由花成本把自己伪装成低类型。低类型可能伪装成高类型，因为 $r_H$ 对它有利；但高类型本来就想被当成高类型，撒谎只会带来成本和风险。

### Benchmark 1：没有检测器时的半分离均衡

没有 alarm 时，低类型以概率

$$
\sigma_S^*=\frac{\rho\Delta_H^R}{(1-\rho)\Delta_L^R}
$$

发送 $m_H$；接收者在看到 $m_H$ 后以概率

$$
\sigma_R^*=\frac{C}{\Delta_L^S}
$$

采取 $r_H$。接收者和低类型的期望收益为零，高类型获得正收益。

> 直觉：低类型的撒谎概率刚好让接收者在看到 $m_H$ 后无差异；接收者采纳 $m_H$ 的概率刚好让低类型在撒谎和不撒谎之间无差异。这是典型 semi-separating equilibrium。

这一 benchmark 给出“无检测”基准。下面加入一个只会漏报、不可能误报的检测器。

### Benchmark 2：没有 false positive 时，检测越强越好

如果 $\alpha=0$，检测器永远不会误伤高类型。随着 true-positive rate $\beta$ 上升，低类型在低 $\beta$ 区间可能更愿意撒谎，但当

$$
\beta\geq \hat{\beta}=1-\frac{C}{\Delta_L^S}
$$

时，低类型停止撒谎。并且，对于接收者、高类型发送者和社会福利而言，最优检测器都倾向于选择足够高的 $\beta$。

> 直觉：没有误报时，只要看到 alarm，接收者就能确定发送者是低类型。因此 alarm 的信息含量极强。提高 $\beta$ 不会伤害高类型，也不会制造额外误伤，所以设计者没有真正的 trade-off。

这一步展示了传统设定的结论。本文的关键是：一旦允许 $\alpha>0$，这个结论会反转。

### Proposition 1：给定检测器时，低类型撒谎概率关于 $\beta$ 非单调

给定 $0<\alpha<\beta$，接收者看到 $m_H$ 和 alarm 后的后验为

$$
b(H\mid m_H,a)=\frac{\alpha\rho}{\alpha\rho+\beta\sigma_S(1-\rho)},
$$

看到 $m_H$ 和 no alarm 后的后验为

$$
b(H\mid m_H,na)=\frac{(1-\alpha)\rho}{(1-\alpha)\rho+(1-\beta)\sigma_S(1-\rho)}.
$$

低类型的均衡撒谎概率在 $\beta<\hat{\beta}$ 时随 $\beta$ 上升，在 $\beta>\hat{\beta}$ 时随 $\beta$ 下降。论文 Figure 3（PDF p.10）用三条不同 $\alpha$ 下的曲线展示了这个“先升后降”的形状。

> 直觉：当 $\beta$ 较低时，接收者主要看重“没有 alarm”这一信号。检测器稍微变强，会让 no alarm 更像一种背书，产生 persuasive effect。为了让接收者仍然保持无差异，低类型可以更多地撒谎。相反，当 $\beta$ 较高时，alarm 的威慑更强，产生 dissuasive effect；低类型必须减少撒谎，否则接收者在 alarm 后会过于确信其为低类型。

具体而言，在 interior case 下：

当 $\beta<\hat{\beta}$，

$$
\sigma_S^*=\frac{(1-\alpha)\rho\Delta_H^R}{(1-\beta)(1-\rho)\Delta_L^R},
$$

它随 $\beta$ 上升。

当 $\beta>\hat{\beta}$，

$$
\sigma_S^*=\frac{\alpha\rho\Delta_H^R}{\beta(1-\rho)\Delta_L^R},
$$

它随 $\beta$ 下降。

> 直觉：低 $\beta$ 区间，接收者的关键无差异条件绑定在 no-alarm 后验上；高 $\beta$ 区间，关键无差异条件绑定在 alarm 后验上。绑定的后验不同，导致 $\sigma_S^*$ 对 $\beta$ 的响应方向相反。

### 重要补充：误报存在时，完全无谎言均衡不存在

即使 $\beta$ 很高，只要 $\alpha>0$，均衡中仍会存在一些低类型撒谎。

> 直觉：如果没有任何低类型撒谎，那么一旦高类型发送 $m_H$ 被 alarm，接收者会知道这个 alarm 一定是误报，于是仍然接受高类型。这样低类型就有动力偏离并发送 $m_H$，因为它可以混入高类型池子。误报的存在使 alarm 不再能完全揭示低类型，因此完全分离均衡被破坏。

### Proposition 2：误报率越低，所有人越好；真阳性率越高，接收者和高类型越好、低类型越差

给定 $\beta$，接收者、高类型发送者和低类型发送者的期望收益都随 $\alpha$ 弱下降。给定 $\alpha$，接收者和高类型发送者的期望收益随 $\beta$ 弱上升，而低类型发送者的期望收益随 $\beta$ 弱下降。

> 直觉：误报会伤害高类型，也会降低 no-alarm 的说服力；对接收者而言，误报让信号更差。对低类型而言，误报并不会减少其被抓到的概率，却会让 no-alarm 后接收者更不确信，因此也可能伤害低类型收益。真阳性率则帮助接收者和高类型区分真假，但压低低类型伪装收益。

这一结论直接导向最优设计：先在每个 $\beta$ 下找最低可行 $\alpha$。

### Lemma 5：给定 true-positive rate，最优 false-positive rate 是 ROC frontier 上的最低可行值

给定分类器 $\phi$，设计者对任何 $\beta$ 都选择最低可行的误报率：

$$
\alpha^*(\beta;\phi)=
\begin{cases}
\dfrac{\phi(s_L\mid H)}{\phi(s_L\mid L)}\beta, & \text{if } \beta\leq \phi(s_L\mid L), \\
\dfrac{\phi(s_H\mid H)}{\phi(s_H\mid L)}\beta+1-\dfrac{\phi(s_H\mid H)}{\phi(s_H\mid L)}, & \text{if } \beta>\phi(s_L\mid L).
\end{cases}
$$

对应报警规则为：

$$
\lambda_L^*(\beta)=
\begin{cases}
\dfrac{\beta}{\phi(s_L\mid L)}, & \text{if } \beta\leq \phi(s_L\mid L), \\
1, & \text{if } \beta>\phi(s_L\mid L),
\end{cases}
$$

$$
\lambda_H^*(\beta)=
\begin{cases}
0, & \text{if } \beta\leq \phi(s_L\mid L), \\
\dfrac{\beta-
\phi(s_L\mid L)}{\phi(s_H\mid L)}, & \text{if } \beta>\phi(s_L\mid L).
\end{cases}
$$

> 直觉：如果分类器输出 $s_L$ 更像低类型，那么最优报警规则一定先在 $s_L$ 上报警，而不是在 $s_H$ 上报警。只有当平台想要的 $\beta$ 已经超过“所有 $s_L$ 都报警”能达到的水平时，才开始对 $s_H$ 也报警。论文 Figure 6（PDF p.14）展示了可行 detector set 和 ROC frontier；Figure 7（PDF p.15）展示了 $\lambda_L$ 先升到 1，然后 $\lambda_H$ 才开始上升。

### Propositions 3–5：最优检测器通常选择中间真阳性率

如果 designer 最大化接收者收益：

- 分类器能力低时，最优 $\beta$ 位于 $[\hat{\beta},\max\{\hat{\beta},\phi(s_L\mid L)\}]$；
- 分类器能力高且撒谎成本高时，同样选择上述区间；
- 分类器能力高且撒谎成本低时，最优选择 $\beta=\phi(s_L\mid L)$。

如果 designer 最大化高类型发送者收益：

- 分类器能力低时，最优 $\beta$ 仍在类似中间区间；
- 分类器能力高时，最优 $\beta$ 可能低于 $\hat{\beta}$，且分类器越能区分类型，最优 $\beta$ 越低。

如果 designer 最大化 receiver、high-type sender、low-type sender 的加权总收益，最优 $\beta$ 是接收者偏好的高检测强度与发送者偏好的低误伤强度之间的折中。发送者权重越高，最优 $\beta$ 越低。

> 直觉：平台有两条路径帮助接收者：一是 deterrence，即降低低类型撒谎概率；二是 information provision，即给接收者更有信息含量的 alarm/no-alarm 信号。当撒谎成本高或分类器能力低时，平台更依赖威慑，因此把 $\beta$ 设在能显著压低撒谎的中间区间。当分类器能力高且撒谎成本低时，威慑难度大，平台更依赖信息提供，此时把 $\beta$ 设在 $\phi(s_L\mid L)$ 这一临界点，充分利用“只对 $s_L$ 报警”的低误报区间。

**核心 trade-off：更高的 $\beta$ 可以抓到更多谎言，但在 ROC 约束下通常伴随更高的 $\alpha$。当 $\beta$ 已经很高时，再提高 $\beta$ 的边际收益下降，而误伤高类型和降低信号可信度的边际成本上升。**

### Extension 1：限制 $\lambda_H=0$

如果检测器不能在分类器输出 $s_H$ 时报警，即 $\lambda_H=0$，那么可行的 $\beta$ 上限变成 $\phi(s_L\mid L)$。在撒谎成本较高时，主模型结论基本保留；在撒谎成本较低时，由于检测器无法通过对 $s_H$ 报警来进一步提高 $\beta$，平台压低低类型撒谎的能力受限。

> 直觉：这个 extension 说明主模型不是依赖“平台可以对看起来真实的内容也报警”这一设定。只要检测器有误报和漏报，false-positive 对战略行为的影响仍然存在。但当报警规则被限制得更保守时，平台的威慑工具变弱。

### Extension 2：电商平台同时选择 commission fee 和检测器

平台向卖家收取 commission fee $f$，同时设计检测器。卖家先决定是否进入平台，然后决定是否虚假表述质量。结果表明：当撒谎成本低且分类器能力足够高时，平台选择让高低类型卖家都进入，并用检测器与 commission fee 共同抽取收益；否则，平台设定较高 commission fee 使低质量卖家不进入，此时检测器变得不重要。

> 直觉：价格和检测器既可能是 complements，也可能是 substitutes。若平台想容纳两类卖家，检测器帮助管理低质量卖家的造假行为，commission fee 则负责收益抽取；若平台通过高 fee 直接筛掉低质量卖家，检测器的战略作用就下降。

## 比较静态汇总表 (Comparative Statics Summary)

| 参数变化 | 对低类型撒谎概率 $\sigma_S^*$ 的影响 | 对最优检测器/收益的影响 | 直觉 |
|:---|:---|:---|:---|
| $\beta\uparrow$ 且 $\beta<\hat{\beta}$ | $\sigma_S^*\uparrow$ | no-alarm 更有说服力 | persuasive effect 主导，未报警消息更可信，低类型更敢混入。 |
| $\beta\uparrow$ 且 $\beta>\hat{\beta}$ | $\sigma_S^*\downarrow$ | alarm 更有威慑力 | dissuasive effect 主导，被报警后接收者更确信其为低类型。 |
| $\alpha\downarrow$，给定 $\beta$ | 低 $\beta$ 区间可能使撒谎上升；高 $\beta$ 区间使撒谎下降 | 接收者、高类型、低类型收益均弱上升 | 更低误报让信号更干净，降低误伤，也让检测器更有区分力。 |
| $C\uparrow$ | 撒谎激励下降；$\hat{\beta}=1-C/\Delta_L^S$ 下降 | 更容易通过威慑减少 disinformation | 撒谎成本高，低类型更容易被吓退。 |
| $\Delta_L^S\uparrow$ | 撒谎激励上升；$\hat{\beta}$ 上升 | 需要更强检测才能威慑 | 成功伪装的收益更高，低类型更愿意承担撒谎成本。 |
| 分类器能力提高 | 给定 $\beta$ 下最低可行 $\alpha^*(\beta)$ 下降 | 最优 $\beta$ 不一定上升，甚至可能下降 | 更好的分类器使平台用更少 alarm 达到足够信念效果。 |
| 设计者更重视高类型发送者 | 倾向降低误伤 | 最优 $\beta$ 下降 | 高类型最怕 false alarm，因此偏好较保守的检测器。 |
| 设计者更重视接收者 | 倾向提高信息质量和威慑 | 最优 $\beta$ 较高但仍非最大 | 接收者需要区分真假，但过度报警会增加误报成本。 |
| $\Delta_L^R\uparrow$ | 接收者更谨慎 | 高分类器能力门槛提高 | 错接低类型的损失越大，接收者越需要更强证据。 |
| $\rho\uparrow$ | 低类型更容易伪装 | 无检测时撒谎概率上升 | 高类型先验更高，$m_H$ 更可信，低类型混入空间更大。 |

## 主要结论与管理启示 (Main Results & Managerial Insights)

### 与 benchmark 的对比

| 问题 | 无误报 benchmark | 本文主模型：有误报 |
|:---|:---|:---|
| alarm 的含义 | alarm 完全说明发送者是低类型 | alarm 可能是误报，不能完全揭示类型 |
| 高 $\beta$ 下是否能消除撒谎 | 可以，超过阈值后低类型不撒谎 | 不可以，只要 $\alpha>0$，均衡中仍有一些撒谎 |
| 检测越强是否越好 | 基本是 | 不一定；过高 $\beta$ 会带来更高 $\alpha$ |
| 最优检测器 | 选择足够高的 true-positive rate | 选择中间 true-positive rate 和最低可行 false-positive rate |
| 管理含义 | 尽量提高抓假能力 | 平衡抓假、误伤和战略反应 |

### 管理建议

1. **不要只优化 recall 或 true-positive rate。** 对内容审核、fake review detection 或诈骗识别而言，抓到更多假内容并不必然提升福利，因为误报会改变真实用户和造假者的行为。
2. **先把误报率压到 ROC frontier 上的最低可行水平。** 本文一个强结论是：给定目标 true-positive rate，所有目标函数下都应选择最低 feasible false-positive rate。
3. **检测阈值要根据目标函数设定。** 如果平台主要保护消费者，应选择相对更高但仍中间的 $\beta$；如果平台更重视高质量卖家或真实内容创作者，应更保守，避免 false-positive alarms。
4. **更好的分类器不意味着更激进的报警。** 当分类器更能区分类型时，平台可能用更低报警强度实现同样信念效果，从而降低误伤。
5. **把检测设计和平台策略一起考虑。** 在电商场景中，commission fee、入驻筛选和检测器是联动的。平台可以通过价格筛选低质量卖家，也可以通过检测器管理其造假行为。

## 与相关文献的对话 (Dialogue with Literature)

### Dziuda and Salas (2018), Balbuzanov (2019)：Communication with detectable deceit

共同点：都研究战略沟通中谎言可能被检测到的情况，即发送者知道虚假消息可能触发某种检测。

区别：这些工作通常关注 false negative，即谎言被检测到的概率，但隐含 false-positive rate 为零。本文把 false positive 放进模型，说明误报不仅是技术细节，而会改变均衡类型、撒谎概率和最优检测器设计。

为什么重要：没有误报时结论接近“检测越强越好”；有误报时最优检测强度是中间值，这是完全不同的管理含义。

### Kartik (2009), Kartik, Ottaviani, and Squintani (2007)：Costly lying

共同点：本文继承 costly lying 的基本思想，即撒谎有成本，因此消息有一定 signaling role。

区别：costly lying 文献通常没有一个外部检测器来生成关于真实性的额外信号。本文加入检测器后，发送者的消息变成 partially verifiable communication，接收者同时从 message 和 detector signal 学习。

为什么重要：这使模型能解释平台审核、算法检测和内容标签等现实制度，而不仅是抽象的道德撒谎成本。

### Kamenica and Gentzkow (2011)：Bayesian persuasion / information design

共同点：本文的 detector design 与 information design 类似，都是设计信息结构影响接收者行动。

区别：本文的信息设计不是直接设计关于状态的信息，而是在一个 signaling game 的子博弈中设计检测器；发送者会在检测器存在下战略性地改变消息选择。

为什么重要：传统 information design 中状态和信息结构常被视为给定或由设计者直接操控；本文强调“被检测对象”会对检测规则作出战略反应。

### Fake review / online manipulation 文献：Mayzlin et al. (2014), Luca and Zervas (2016), He et al. (2022)

共同点：都关注平台上的虚假评论、虚假交易或在线声誉操纵。

区别：这些文献多为实证识别或市场后果分析，本文提供一个理论机制，解释平台检测政策如何反过来影响造假者的均衡行为。

为什么重要：平台不只是被动发现 fake reviews；检测规则本身会塑造 fake reviews 的产生。

## 犀利评论 (Reviewer's Critique)

### 优点

理论贡献明确。本文抓住了现有 lie detection 文献中一个看似技术性、实则改变结论的假设：false positive rate 不应被设为零。由此产生的非单调撒谎概率和中间最优检测强度，是清晰且有辨识度的理论结果。

模型机制简洁。persuasive effect 与 dissuasive effect 的分解非常适合在 seminar 中讲解，也能直接映射到平台审核实践：未被标记的信息会被用户解读为某种认证。

实践相关性强。平台内容审核、fake review detection、诈骗邮件提醒、LinkedIn fake account detection 等都面临 precision-recall trade-off。本文能为阈值选择和误报管理提供理论语言。

### 模型限制/假设过强

1. **二元类型和二元行动较简化。** 现实中商家质量、内容真实性、用户行动往往是连续的。二元设定增强了可解性，但可能夸大某些阈值型结果。
2. **接收者完全理性且知道检测器参数。** 真实用户未必知道 $\alpha$、$\beta$ 或平台审核策略，也可能误解 alarm/no-alarm 的含义。
3. **撒谎成本同质。** 不同发送者的操纵能力、道德成本和被处罚风险可能差异很大。虽然作者讨论了异质成本不改变核心机制，但现实中异质性可能影响最优阈值。
4. **检测器能力外生。** 平台往往可以投入资源提升 classifier，但本文主模型只讨论给定 classifier 下的 alarm rule。若 classifier investment 内生，最优设计会多一层成本收益权衡。
5. **缺少动态声誉和反复互动。** 平台审核常常是重复博弈，发送者可能学习、规避、迁移账号，用户也会逐步学习平台标签可信度。

### 未来方向

1. **连续类型与连续消息。** 将 $H/L$ 扩展为连续质量，研究不同质量发送者如何选择夸大程度，以及检测器如何设计多级标签。
2. **发送者可投资规避检测。** 例如 fake review sellers 购买更高质量水军，或诈骗邮件发送者调整文本以绕过 classifier。
3. **用户异质性和有限理性。** 不同用户对 alarm 的信任程度不同；有些用户可能过度相信平台标签，有些则忽视标签。
4. **动态平台治理。** 研究平台长期如何在误伤真实创作者和压制造假者之间调整策略，以及错误标签如何影响平台声誉。
5. **实证或结构估计。** 用平台审核数据估计用户对 alarm/no-alarm 的信念更新、发送者造假反应和最优阈值。

## 一句话总结

这篇文章说清楚了一件容易被忽略的事：**检测器不是越激进越好，因为 alarm 和 no-alarm 都会成为用户推断真实性的信号，而造假者会利用这些信号的含义来调整撒谎策略。**

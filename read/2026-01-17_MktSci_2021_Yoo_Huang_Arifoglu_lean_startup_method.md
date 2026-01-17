# A Theoretical Analysis of the Lean Start-up Method

## 0. 论文速览

- 研究对象：Lean Start-up Method (LSM) 的核心循环 Build–Test–Learn，尤其是用 Minimum Viable Product (MVP)/test product 做“带噪声”的市场试验，从而决定是否 pivot。
- 关键建模抓手：产品“横向匹配”(horizontal fit) + “纵向价值”(vertical quality/price) 共同决定购买；test product 只能产生 censored feedback（只看到 sale/no sale，而不是消费者真实偏好）。
- 最核心的理论产出：
  - 证明“最大化最终利润”等价于“最大化学习”(max learning)，并给出最优 test product 的闭式解集合。
  - 揭示一个反直觉：最优 test product 往往要放在两个候选理想产品区间 $(0,C)$ 的外侧（更像“极端探针”），而最终 pivot 的最优位置却在区间内部（更像“折中产品”）。
  - 将 LSM 的收益分解为“减少做错产品概率”的 value of information，并给出其随市场不确定性、偏好异质性等的比较静态。

## 1. 研究背景与动机

### 1.1 实践痛点

LSM 在创业实践中有一个很尖锐的矛盾：

- 一方面，创业者被鼓励“做一个最简可行产品 (MVP)”快速上线，观察市场反馈；
- 另一方面，真实反馈往往是高度粗糙、甚至被“产品太简陋/太便宜/太贵/太偏门”所扭曲的。

更具体地，实践里常见这些困惑：

- 什么时候应该 pivot？pivot 到哪里？
- MVP 应该做得多“简”？质量/价格/功能简化到什么程度不会把学习信号毁掉？
- 为什么一些团队用 LSM 收益巨大（迅速找到 PMF），另一些却“学不到东西”，甚至被误导？

### 1.2 理论缺口

既有学术研究大量讨论创业试验、产品开发、信息获取，但对 LSM 的关键结构缺少一个“可推导的、可比较静态的”基准模型。尤其缺少：

- MVP/test product 的设计（水平位置 + 纵向质量/价格）如何共同决定学习？
- 在只能观察 sale/no sale（而看不到消费者偏好）的 censored feedback 下，Bayesian learning 如何进行，以及怎样选实验来最大化信息价值？
- “最终产品设计”与“测试产品设计”是否一致？如果不一致，偏差来自哪里？

### 1.3 核心贡献与意义

本文贡献可以概括为三层：

1. 理论上：给出一个极简但锋利的两阶段 Bayes 决策模型，把 LSM 形式化为“先选 test product 诱发反馈，再 pivot 并发布最终产品”的动态优化。
2. 方法上：把一阶决策（选 test product）转化为一个非常清晰的学习目标：最小化“pivot 错方向”的概率 $\mathbb{E}[\min\{\tilde r,1-\tilde r\}]$（Lemma 3）。这一步把很多复杂性压缩成一个可解释的目标函数。
3. 管理上：给出可操作的设计原则（例如最优 test product 可能故意极端；失败与成功同样信息量；LSM 对不同市场环境的效果差异来自何处）。

## 2. 模型设定与假设

### 2.1 符号体系（决策变量、参数、随机变量）

| 符号 | 含义 | 类型/范围 | 备注 |
| --- | --- | --- | --- |
| $W$ | 理想产品（ideal design）的“位置” | 基准：$W\in\{0,C\}$ | 产品属性被压缩成一维“横向位置” |
| $C$ | 两个候选理想设计之间的距离 | $\epsilon < C < 2\epsilon$ | 既有区分度，又有分布重叠 |
| $x$ | 单个消费者的偏好位置 | 来自 $h(x\mid W)$ | 只影响横向匹配 |
| $h(x\mid W)$ | 消费者偏好分布（给定理想设计） | 基准：Uniform$[W-\epsilon, W+\epsilon]$ | $\epsilon$ 衡量偏好异质性 |
| $\epsilon$ | 偏好分布半宽度 | $\epsilon>0$ | 越大，消费者口味越分散 |
| $t$ | 横向不匹配的“痛感” | $t>0$ | 类似 Hotelling 运输成本 |
| $r$ | 先验信念 $P(W=0)$ | $r\in[0,1]$ | 市场研究后的先验 |
| $\tilde r$ | 观察 test product 结果后的后验 | $\tilde r\in[0,1]$ | Bayes 更新 |
| $(\lambda, v, \rho)$ | test product 的位置/质量/价格 | $\lambda\in\mathbb{R}$ | $v$ 为纵向质量，$\rho$ 为 test 价格 |
| $s_i$ | 被抽样消费者 $i$ 的 surplus | $s_i=v-\rho-t\|\lambda-x_i\|$ | 只 观察 $s_i>0$ 与否 |
| $(\Lambda, V, p)$ | 最终产品的位置/质量/价格 | 基准：$V,p$ 外生 | 第二阶段选择 $\Lambda$（扩展里也选 $p$） |
| $\pi$ | 企业利润 | 收入模型 | 忽略成本（或归一化） |

### 2.2 Players, Sequence of Events, Information Structure

#### Players

- Entrepreneur（创业者）：选择 test product，观察反馈，更新信念，然后决定最终产品设计（pivot）。
- Consumer（消费者）：在 test 阶段被随机抽样的单个消费者 $i$，决定 buy/no-buy；在最终产品阶段是一群消费者形成需求。

#### Sequence of Events（两阶段）

1. Nature 选择理想设计 $W\in\{0,C\}$；创业者有先验 $r=P(W=0)$。
2. 第一阶段（Test）：创业者选择 test product $(\lambda, v, \rho)$。
3. 抽样：从分布 $h(x\mid W)$ 抽取一个消费者 $i$，其偏好为 $x_i$。
4. 购买决策：消费者购买当且仅当 surplus 为正：$s_i=v-\rho-t|\lambda-x_i|>0$。
5. 创业者只观察 sale/no sale（censored feedback），据此用 Bayes 更新信念为 $\tilde r$。
6. 第二阶段（Pivot & Launch）：创业者基于 $\tilde r$ 选择最终产品位置 $\Lambda$（基准模型中 $V,p$ 外生），发布产品并获得利润。

#### Information Structure（信息结构）

- 创业者不知道 $W$，只知道先验 $r$。
- 创业者在 test 阶段看不到 $x_i$ 或 $s_i$ 的具体数值，只看到事件 $\{s_i>0\}$ 或 $\{s_i\le 0\}$。
- 因为反馈被截断（censored），学习并不是直接估计 $x$，而是通过“销售是否发生”间接推断 $W$。

### 2.3 需求、利润与约束

#### 消费者效用与购买规则

最终产品阶段：消费者 $x$ 对最终产品 $(\Lambda,V,p)$ 的 surplus 为

$$ s(x)=V-p-t|\Lambda-x|. $$

购买条件是 $s(x)>0$，等价于 $|\Lambda-x|<(V-p)/t$。

#### 需求函数

给定真实 $W$，需求（购买概率）为

$$ D(\Lambda,V,p\mid W)=\int_{\Lambda-(V-p)/t}^{\Lambda+(V-p)/t} h(x\mid W)\,dx. $$

在基准的 uniform 设定下，若 $h(x\mid W)=\text{Unif}[W-\epsilon,W+\epsilon]$，则

$$ D(\Lambda,V,p\mid W)=\frac{1}{2\epsilon}\Big[\min\{W+\epsilon,\,\Lambda+(V-p)/t\}-\max\{W-\epsilon,\,\Lambda-(V-p)/t\}\Big]_+, $$

#### 第二阶段利润

给定后验 $\tilde r$，创业者对 $W$ 的主观分布为：$P(W=0)=\tilde r$，$P(W=C)=1-\tilde r$。

因此第二阶段期望利润为

$$ \pi(\Lambda\mid \tilde r)=p\Big[\tilde r\,D(\Lambda,V,p\mid 0)+(1-\tilde r)\,D(\Lambda,V,p\mid C)\Big]. $$

基准模型第二阶段决策是

$$ \pi^*(\tilde r)=\max_{\Lambda}\,\pi(\Lambda\mid \tilde r). $$

#### 第一阶段目标

忽略 test product 从单个消费者获得的利润（可视为数量级很小），第一阶段目标是最大化第二阶段期望利润：

$$ \max_{\lambda,v,\rho}\,\mathbb{E}_{s_i(\lambda,v,\rho)}\big[\pi^*(\tilde r(\lambda,v,\rho\mid r))\big]. $$

更一般地，若令 $g(s_i\mid(\lambda,v,\rho),W)$ 表示在给定 $W$ 时随机抽样消费者的 surplus 密度（论文 Lemma 1），则第一阶段目标可以写成对 sale/no-sale 两类结果的积分：

$$
\begin{aligned}
\max_{\lambda,v,\rho}\ \mathbb{E}_{s_i(\lambda,v,\rho)}[\pi^*(\tilde r)]
= \max_{\lambda,v,\rho}
\Bigg(&\int_{0}^{\infty} \pi^*(\bar r(\lambda,v,\rho\mid r))\,[r\,g(s_i\mid(\lambda,v,\rho),W=0)+(1-r)\,g(s_i\mid(\lambda,v,\rho),W=C)]\,ds_i \\
&+ \int_{-\infty}^{0} \pi^*(\underline r(\lambda,v,\rho\mid r))\,[r\,g(s_i\mid(\lambda,v,\rho),W=0)+(1-r)\,g(s_i\mid(\lambda,v,\rho),W=C)]\,ds_i\Bigg).
\end{aligned}
$$

其中 $\bar r(\lambda,v,\rho\mid r)$ 与 $\underline r(\lambda,v,\rho\mid r)$ 分别是观察到 sale 与 no-sale 后的后验（论文 Lemma 2）。

### 2.4 关键假设与合理性

#### Assumption 1（纵向价值不至于压倒横向匹配）

$$ V-p\le \epsilon t. $$

直觉：如果 $V-p$ 极大，则即使产品位置偏得离谱，消费者仍愿意买，PMF（fit）不再关键；LSM 的“找对位置”问题就退化了。

#### 两个候选理想设计与部分重叠

$$ W\in\{0,C\},\quad \epsilon < C < 2\epsilon. $$

- $C>\epsilon$：两个候选设计确实有差异，否则“pivot 与否”不重要。
- $C<2\epsilon$：两类消费者分布有重叠，否则一次测试可能就完全识别 $W$，学习问题过于简单。

#### Censored feedback

只观察 sale/no sale 是 LSM 的关键现实特征：早期试验常常只有转化、点击、购买等二元/阈值信息，而不是连续的效用/偏好。

#### 成本简化

基准模型忽略开发与生产成本，把重点放在信息结构与决策结构上；扩展 5.1 通过 pivoting friction 把“资源被 pivot 消耗”内生化，部分缓解这一简化。

## 3. 分析与求解

论文用 Backward Induction：先解第二阶段最优 pivot，再回到第一阶段选最优 test product。

### 3.1 第二阶段：最优 pivot（Proposition 1）

令

$$ d\equiv \frac{V-p}{t}. $$

$d$ 是“购买区间”的半宽度：离产品位置 $\Lambda$ 距离不超过 $d$ 的消费者才会买。

在 uniform 分布下，第二阶段问题可写成一个分段线性/凹的最大化问题（论文给出显式展开）。核心结论：最优 pivot 只会选两个内点之一。

最优 pivot 位置为

$$ \Lambda^*(\tilde r)=\begin{cases}
\epsilon-d, & \tilde r\ge \frac{1}{2},\\
C-\epsilon+d, & \tilde r<\frac{1}{2}.
\end{cases} $$

并且在 Assumption 1 下，$d\le \epsilon$，所以 $\Lambda^*(\tilde r)\in[0,C]$。

#### 经济学直觉：为什么最优 pivot 在区间内部？

这是本文第一个“反直觉但很关键”的机制：

- 如果你确信 $W=0$（$\tilde r$ 很大），直觉上你想把产品做在 0；
- 但即便 $\tilde r>1/2$，仍有概率 $1-\tilde r$ 其实 $W=C$。

在 $C<2\epsilon$ 的重叠设定下，位于区间内部的“折中位置”可以让两种可能下都保留一部分需求，从而对冲“选错理想设计”的损失。

换句话说：最终产品不是用来“做实验最大化信息”，而是用来“在不确定下最大化期望需求”。因此它倾向于 hedging。

#### 最优利润表达式与“做错产品概率”

在最优 pivot 下，期望利润可以化成一个非常漂亮的形式：

$$ \pi^*(\tilde r)=p\left[\frac{V-p}{\epsilon t}-\left(\frac{V-p}{\epsilon t}-\left(1-\frac{C}{2\epsilon}\right)\right)\min\{\tilde r,1-\tilde r\}\right]. $$

这里 $\min\{\tilde r,1-\tilde r\}$ 可以解释为“创业者 pivot 到错误方向的概率”。

- 如果 $\tilde r\in\{0,1\}$（完全学到），该项为 0，利润达到上界 $p\frac{V-p}{\epsilon t}$。
- 如果 $\tilde r=1/2$（完全没学到），该项为 1/2，利润被对冲需求项显著拉低。

这个线性结构是后续第一阶段“学习等价”结论的关键。

### 3.2 第一阶段：最优 test product（Lemma 3 与 Proposition 2）

#### 3.2.1 Bayes 学习：从 surplus 到后验

对 test product $(\lambda,v,\rho)$，被抽样消费者的 surplus 为

$$ s_i=v-\rho-t|\lambda-x_i|. $$

创业者只观察 $s_i>0$ 还是 $s_i\le 0$。

定义在给定 $W$ 时 surplus 的密度为 $g(s_i\mid(\lambda,v,\rho),W)$。论文的 Lemma 1 给出一般形式：

$$
g(s_i\mid(\lambda,v,\rho),W)=\frac{1}{t}\left[h\left(\lambda+\frac{-(v-\rho)+s_i}{t}\mid W\right)+h\left(\lambda+\frac{(v-\rho)-s_i}{t}\mid W\right)\right].
$$

只关心 sale/no-sale 时，更方便的是直接写 sale 概率（注意只依赖 $v-\rho$）：

$$
q_W(\lambda,v,\rho)\equiv \Pr(s_i>0\mid W)=\int_{0}^{\infty}g(s_i\mid(\lambda,v,\rho),W)\,ds_i
=\int_{\lambda-(v-\rho)/t}^{\lambda+(v-\rho)/t} h(x\mid W)\,dx.
$$

由 Bayes 法则（论文 Lemma 2），观察到 sale 与 no-sale 后的后验分别为

$$
\bar r(\lambda,v,\rho\mid r)=\Pr(W=0\mid s_i>0)=\frac{r\,q_0(\lambda,v,\rho)}{r\,q_0(\lambda,v,\rho)+(1-r)\,q_C(\lambda,v,\rho)}.
$$

$$
\underline r(\lambda,v,\rho\mid r)=\Pr(W=0\mid s_i\le 0)=\frac{r\,(1-q_0(\lambda,v,\rho))}{r\,(1-q_0(\lambda,v,\rho))+(1-r)\,(1-q_C(\lambda,v,\rho))}.
$$

其中 $q_0$ 对应 $W=0$，$q_C$ 对应 $W=C$。

这一组公式把“实验设计 $(\lambda,v,\rho)$”与“后验随机变量 $\tilde r$”明确连了起来；也解释了为什么在忽略 test product 利润的设定下，$v$ 与 $\rho$ 只通过差值 $v-\rho$ 起作用。

#### 3.2.2 Lemma 3：利润最大化等价于学习最大化

由于 $\pi^*(\tilde r)$ 对 $\min\{\tilde r,1-\tilde r\}$ 是线性的、且单调递减，第一阶段问题等价于

$$ \max_{\lambda,v,\rho}\,\mathbb{E}[\pi^*(\tilde r)]\quad\Longleftrightarrow\quad \min_{\lambda,v,\rho}\,\mathbb{E}\big[\min\{\tilde r,1-\tilde r\}\big]. $$

直觉：在第二阶段，除了“你 pivot 错没错”这件事，$\tilde r$ 的其它细节都不会以非线性的方式影响利润；因此第一阶段只要尽可能让后验远离 1/2（减少做错概率）即可。

这一步把 LSM 的“最大化学习”从口号变成了严格的优化等价。

#### 3.2.3 Proposition 2：最优 test product 的闭式解（集合）

在 uniform 分布下，最优 test product 并非唯一，而是一族（实际上是两条线段/射线的并）。用 $v-\rho$ 表示 test product 的“净纵向吸引力”。

当 $r>1/2$（更相信 $W=0$）时，任意满足下列之一的 test product 都是最优：

$$ S(i)=\{(\lambda,v,\rho): v-\rho=(\epsilon-\lambda)t,\ \forall\lambda\le 0\}\ \cup\ \{(\lambda,v,\rho): v-\rho=(\lambda-\epsilon)t,\ \forall\lambda\ge C/2+\epsilon\}. $$

当 $r<1/2$（更相信 $W=C$）时，对称地得到另一组：

$$ S(ii)=\{(\lambda,v,\rho): v-\rho=(C-\epsilon-\lambda)t,\ \forall\lambda\le C/2-\epsilon\}\ \cup\ \{(\lambda,v,\rho): v-\rho=-(C-\epsilon+\lambda)t,\ \forall\lambda\ge C\}. $$

当 $r=1/2$ 时，最优集合是两组集合的凸包（论文给出精确表述），对应“在对称先验下的一片区域”。

#### 经济学直觉：两条最优线代表两种“极端但等价”的学习策略

以 $r>1/2$ 为例（更相信 $W=0$）：

- 左侧那条线（$\lambda\le 0$ 且 $v-\rho=(\epsilon-\lambda)t$）对应“确认式”(confirmatory) 测试：
  - 把 test product 放在更像 0 的位置附近（甚至在 0 的左侧），并把 $v-\rho$ 调到一个阈值，使得若 $W=0$ 则一定会卖出（消灭 false negative）。
  - 于是，一旦出现 no-sale（小概率事件），几乎可以断定 $W=C$。

- 右侧那条线（$\lambda\ge C/2+\epsilon$ 且 $v-\rho=(\lambda-\epsilon)t$）对应“证伪式”(disconfirmatory) 测试：
  - 把 test product 推向更像 $C$ 的方向（甚至到区间外侧），并把 $v-\rho$ 调到阈值，使得若 $W=0$ 则一定卖不出（消灭 false positive）。
  - 于是，一旦出现 sale（小概率事件），几乎可以断定 $W=C$。

两种策略的共同点：它们都刻意让某个结果成为“几乎决定性”的信号，从而把后验推向 0 或 1。

在 uniform 设定下，这两条线的“等价”可以用 $q_0,q_C$ 的固定值看得更清楚：

- 对 confirmatory 线 $v-\rho=(\epsilon-\lambda)t,\ \lambda\le 0$：有 $q_0=1$，且 $q_C=1-\frac{C}{2\epsilon}$（只有两分布重叠那一段会购买）。
- 对 disconfirmatory 线 $v-\rho=(\lambda-\epsilon)t,\ \lambda\ge C/2+\epsilon$：有 $q_0=0$，且 $q_C=\frac{C}{2\epsilon}$。

因此，在每条线内部，移动 $\lambda$ 只是用 $v-\rho$ 抵消，使得 $(q_0,q_C)$ 不变；Bayes 更新后的两点后验 $(\bar r,\underline r)$ 也随之不变，从而学习价值与期望利润完全一样。

这也带来一个非常实践向的观点：

- test product 的失败（no sale）可能和成功（sale）一样有信息量；**关键在于你是否把实验设计成“失败能够强烈证伪”**。

### 3.3 比较静态：LSM 的有效性（Corollary 2 与 Table 1）

论文用“减少做错产品概率”来度量 LSM 的 value of information。

定义 benchmark：不做 LSM，直接按先验选最终产品。此时做错概率是 $\min\{r,1-r\}$。

定义 LSM 的收益（benefit）为

$$ \beta(\lambda,v,\rho\mid r)\equiv \min\{r,1-r\}-\mathbb{E}\big[\min\{\tilde r(\lambda,v,\rho\mid r),1-\tilde r(\lambda,v,\rho\mid r)\}\big]. $$

在最不确定的情形 $r=1/2$ 且采用最优 test product（对称设定下可取 $(\lambda^*,v^*-\rho^*)=(0,\epsilon t)$），有：

- 峰值收益（peak benefit）

$$ \beta(\lambda^*,v^*,\rho^*\mid 0.5)=\frac{C}{4\epsilon}. $$

- 对实现偏差的敏感性（sensitivity to implementation）：论文用在最优点处的偏导刻画。

对质量维度的边际敏感性（在 $\lambda=0$ 附近）是分段常数：

$$ \left.\frac{\partial \beta(\lambda,v,\rho\mid 0.5)}{\partial (v-\rho)}\right|_{(\lambda,v-\rho)=(0,\epsilon t)}=\begin{cases}
\frac{1}{4\epsilon t}, & v-\rho<\epsilon t,\\
-\frac{1}{4\epsilon t}, & v-\rho>\epsilon t.
\end{cases} $$

对位置维度的敏感性（在 $v-\rho=\epsilon t$ 附近）为

$$ \left.\frac{\partial \beta(\lambda,v,\rho\mid 0.5)}{\partial \lambda}\right|_{(\lambda,v-\rho)=(0,\epsilon t)}=\begin{cases}
0, & \lambda<0,\\
\frac{1}{\epsilon}, & \lambda>0.
\end{cases} $$

这些局部表达与 Figure 4 的“单峰”与“在 $\lambda=C/2$ 学不到”相一致。

Table 1 总结了关键参数的方向性：

- 市场不确定性 $C$ 越大，峰值收益越高；但对实现偏差的敏感性基本不变。
- 偏好异质性 $\epsilon$ 越大，峰值收益越低；同时收益曲线更平缓，对实现偏差更不敏感（不等于容易成功，而是‘怎么做都学得不多’）。
- 横向偏好强度 $t$ 不改变峰值收益的量级，但会影响对质量实现偏差的敏感性（因为 $v-\rho$ 进入 surplus 时要除以 $t$）。

## 4. 主要结论与管理启示

### 4.1 机制揭示：Benchmark vs LSM

Benchmark（不做 LSM）：

- 直接根据先验选最终产品位置，做错概率是 $\min\{r,1-r\}$。
- 没有学习，因此没有“从不确定到确定”的跃迁。

LSM（做一次 test）：

- test product 的目标不是“卖得多”，而是让某个结果在某个 $W$ 下几乎必然发生，从而把后验推向 0 或 1。
- 最终 pivot 目标不是“信息最大化”，而是“期望需求最大化”，因此倾向于在 $[0,C]$ 内做折中以对冲。

这就解释了为什么实践中经常出现：

- MVP 做得太像最终产品（太居中、太不激进）反而学不到；
- 但最终产品又不能像 MVP 那么极端，否则在不确定下损失期望需求。

### 4.2 管理建议：如何设计 MVP/test product

1. 把 test product 当作“探针”，不是当作“缩小版最终产品”。
   - 最优 test product 往往在 $\lambda$ 上更极端（区间外侧）。
   - 直觉：极端位置让 sale/no sale 在不同 $W$ 下产生更大的似然比，从而更快把后验推离 1/2。

2. 质量/价格要“刚好卡在阈值”附近：
   - $v-\rho$ 太高：无论 $W$ 是什么都容易 sale，sale 事件不再携带信息（false positive 变严重）。
   - $v-\rho$ 太低：无论 $W$ 是什么都容易 no-sale，no-sale 事件也不再携带信息（false negative 变严重）。
   - 因此最优通常在中间值（Figure 4 左）。

3. 把失败当作信息资产：
   - 证伪式测试意味着：你设计一个“不太可能卖”的方案，其不卖是常态且不信息化；但一旦卖了，就是强信号。
   - 这为“故意做一个可能失败的 MVP”提供了理性基础。

### 4.3 图表解读（抓核心信息）

- Figure 3（最关键）：在 $(\lambda, v-\rho)$ 平面上，两条线表示两类最优 test product。越远离 $(0,C)$，需要越高的 $v-\rho$ 来抵消更差的 fit，从而保持同等信息量。
- Figure 4：
  - 左图：收益对 $v-\rho$ 单峰，强调“过高/过低都不行”。
  - 右图：在 $\lambda=C/2$ 完全学不到，因为 sale/no sale 在两种 $W$ 下概率对称，似然比接近 1。
- Figure 5（pivoting friction 扩展）：展示从 test 产品到最终产品的“路径”。有摩擦时，pivot 路径更短、最终位置更内缩。
- Figure 7（pricing 扩展）：学习越充分，最优价格越低，且 learning 与 flexible pricing 互补（学习越好，灵活定价带来的收益增量越大）。
- Figure 8（多轮迭代）：把 n 次 build–test–learn 画成动态决策树，突出“如果第一次测试足够信息化，可能不需要更多轮”。
- Figure 10（三候选理想设计扩展）：在 $(\tilde r_0,\tilde r_C)$ 的三角区域里，不确定性最大时最优 pivot 到中间点 0（hedging），与基准模型一致。

### 4.4 Extensions（每个扩展的关键点）

#### 4.4.1 5.1 Pivoting friction：pivot 会吞噬开发资源

核心设定：pivot 距离越大，最终质量越被稀释。

$$ V^*=V-f|\Lambda-\lambda|, $$

其中 $f>0$ 衡量 pivot 摩擦。

主要结论（Proposition 3 与 4）：

- 若 $f>t$：pivot 不值得做，最优是完全不 pivot（$\Lambda^*=\lambda$，$V^*=V$）。直觉：改 fit 的边际收益不够覆盖质量损失。
- 若 $f\to 0$：回到基准模型（Proposition 1 与 2）。
- 若 $f\in(0,t)$：出现“只有当后验足够强才 pivot”的区域。
  - 特别地，当 test 产品是混合型（$\lambda\in(0,C)$）时，只有在 $\tilde r<\frac{1}{2}(1-f/t)$ 或 $\tilde r>\frac{1}{2}(1+f/t)$ 这种强信念下才会向两端 pivot；否则保持原位置不动。

对 test product 的含义（Proposition 4）：

- 小摩擦下最优 test product 从一族最优集合收缩到两个点（Figure 3 的 star/cross），本质是：在同等学习下选择 pivot 距离更短的 test。
- 若摩擦随 test 质量上升（$\partial f/\partial v>0$），则应通过降低 $\rho\to 0$ 来减少资源消耗，同时保持 $v-\rho$ 不变。
- 大摩擦 $f>t$ 下，最优 test product 退化为“直接做最终产品”，LSM 不再精益。

管理启示：LSM 的适用性高度依赖行业的 pivot 成本结构。软件/数字产品更适合，硬件/制造业可能需要更谨慎。

#### 4.4.2 5.2 Endogenous pricing：学习会改变需求曲线斜率

第二阶段同时选 $(\Lambda,p)$：

$$ \pi^*(\tilde r)\equiv \max_{\Lambda,p}\ p\int_{\Lambda-(V-p)/t}^{\Lambda+(V-p)/t}\Big[\tilde r\,h(x\mid 0)+(1-\tilde r)\,h(x\mid C)\Big]dx. $$

Lemma 4 给出最优价格

$$ p^*=\frac{V}{2}+\frac{\min\{\tilde r,1-\tilde r\}}{\max\{\tilde r,1-\tilde r\}}\frac{\epsilon t}{2}\left(1-\frac{C}{2\epsilon}\right). $$

直觉：学习越充分（$\tilde r\to 0$ 或 $1$），需求对价格越敏感（更“陡峭”），因此最优价格下降（更接近 $V/2$）。

并且：学习与灵活定价是互补的（Figure 7 右图）：test 学得越好，第二阶段能通过价格优化榨取的额外利润越多。

#### 4.4.3 5.3 Multiple iterations：多轮测试的边际收益递减

允许 test 产品反复上线 $n$ 次。为可解性，论文把 $\lambda,\Lambda$ 限制为离散集合 $\{0,C\}$。

Proposition 5：无论还剩几轮，最优 test 产品都“重复同一策略”

$$ (\lambda_n^*, v_n^* - \rho_n^*)=\begin{cases}
(0,\epsilon t), & r\ge 0.5,\\
(C,\epsilon t), & r<0.5.
\end{cases} $$

Corollary 3：在 $r=0.5$ 时，$n$ 轮测试的峰值收益为

$$ \beta_n(\lambda^*,v^*,\rho^*\mid 0.5)=\frac{1}{2}\left(1-\left(1-\frac{C}{2\epsilon}\right)^{n+1}\right). $$

它随 $n$ 增加但边际递减，符合“多做几轮确实更好，但很快进入报酬递减区”。

#### 4.4.4 5.4 More than two candidate ideal products：不确定性高时 pivot 到中间点

扩展到 $W\in\{-C,0,C\}$，并令 $\lambda,\Lambda\in\{-C,0,C\}$。定义

$$ D_1\equiv\int_{\Lambda-(V-p)/t}^{\Lambda+(V-p)/t} h(x\mid W=\Lambda)dx,\quad D_2\equiv\int_{\Lambda-(V-p)/t}^{\Lambda+(V-p)/t} h(x\mid |W-\Lambda|=C)dx. $$

Proposition 6 给出在 $(\tilde r_0,\tilde r_C)$ 平面上的分区规则：当后验高度不确定（接近 $1/3,1/3$）时，最优 pivot 到 0，通过“与两侧都重叠”来 hedging（Figure 10 左图）。

Proposition 7 则刻画关键边界情形下最优 test 产品位置：当不确定性最大时，最优 test 产品不在中间，而在外侧 $\pm C$（Figure 10 右图），再次强化“test 要极端、launch 要折中”的主线机制。

## 5. Reviewer's Critique

### 5.1 我会给的正面评价（Strengths）

1. 把 LSM 的口号转成了一个清晰的 Bayes 决策问题，并且能推出闭式解（至少在基准 uniform 情形）。这在创业/创新这类题材里很难得。
2. Lemma 3 的“利润最大化等价于学习最大化”是非常强的结构性结果：它解释了为什么实践里 LSM 强调 learning，而不是短期收益。
3. 机制清楚：test product 的极端性 vs 最终产品的折中性，这个对比非常抓人，也能直接指导实践。
4. 扩展方向选得对：pivot friction、pricing、multiple iterations、multiple candidate ideals，都是 LSM 真正会遇到的复杂性。

### 5.2 我会狠抓的局限（Weaknesses / Strong assumptions）

1. 抽样极端简化：test 只对一个消费者展示一次。
   - 现实里 MVP 会接触很多用户，且反馈可能是转化率、留存、评分、文字评论等多维信号。
   - 单样本使得“最优实验=让某事件几乎必然”看起来很合理，但多样本下最优可能会变成经典的实验设计/信息论问题（例如最大化 Fisher information 或最大化期望 KL divergence），结论未必同形。

2. 理想设计只在一维线上，并且只考虑两个点（基准）。
   - 真实产品空间是多维的，且“候选理想产品集合”可能是连续的。
   - 一维 + 两点的好处是得到闭式解，但代价是外推时要谨慎。

3. 成本结构过于轻：基准模型没有开发成本、生产成本、推广成本。
   - 虽然扩展 5.1 引入了 pivot friction，但它以“质量线性扣减”来代理资源约束，这仍是粗粒度。
   - 若成本是凸的、或者存在固定成本，最优 pivot/test 可能会发生非线性跳变。

4. 需求侧结构是 Hotelling-like 的线性不匹配痛感与统一纵向价值。
   - 很多市场里存在强网络效应、口碑扩散、动态口味形成；这些都会改变“先验—后验—需求”的映射。

5. 最终产品的纵向质量 $V$ 在基准里外生。
   - LSM 的本质之一是“用小投入换信息”，投入规模与信息精度之间存在内生 trade-off。
   - 把 $V$ 外生会使一些“何时做 lean，何时直接 full build”的边界被弱化（虽然扩展 5.1 部分触及）。

### 5.3 我希望作者在修订中补的内容

- 更系统地讨论：为什么选择 uniform 分布（而非一般分布）不会改变核心机制？哪些结论是一般性的，哪些依赖闭式解？
- 把“最优 test product 集合是两条线”进一步解释成一个更一般的“likelihood ratio targeting”原则（例如把 sale/no sale 看作二元信号，最优实验在于最大化两种状态下信号分布的可分性）。

### 5.4 未来研究方向（给博士生的选题灵感）

1. 多样本/连续信号：把 sale/no sale 扩展为计数、留存、评分等，并允许样本量可控（与预算约束联动）。
2. 连续候选理想产品：$W$ 连续、甚至是多维向量；用最优实验设计/主动学习 (active learning) 的语言重写 LSM。
3. 竞争与模仿：当竞争者观察到你的 MVP 并快速模仿，最优 test 可能需要权衡 learning vs information leakage。
4. 供应链/运营约束：若 pivot 触发产线切换、库存报废、交付延迟，pivot friction 会高度非线性；可与 real options 结合。
5. 金融与激励：把投资人、融资里程碑等引入（与 2025 年的 funding-induced distortions 是自然衔接），研究“谁来决定 MVP 设计”与“短期指标压力”如何扭曲学习。
   > Sudhir, K., Onesun Steve Yoo, and Zihao Zhou. 2025. “Entrepreneurs and Investors: Funding-Induced Distortions in Lean Start-up Product Experiments and Innovation.” Marketing Science, May 16, 1. 188104965. https://doi.org/10.1287/mksc.2023.0309.

## 6. One More Thing：本文最值得分享的“灵光一现”

最让我想拍桌子的瞬间，是把 LSM 的两种产品（test vs final）用一句话区分开：

- test product 是用来制造高似然比（让某个结果在某个状态下几乎必然），所以它应该更像“极端探针”；
- final product 是用来在残余不确定下最大化期望需求，所以它应该更像“折中对冲”。

这解释了一个创业者经常说不清、但天天踩坑的事实：

你不能用“我未来要卖的东西”来设计 MVP；你要用“我最想搞清楚的那件事”来设计 MVP。

把 MVP 从“缩小版产品”重新理解为“信息武器”，这就是这篇理论论文最实用的贡献。

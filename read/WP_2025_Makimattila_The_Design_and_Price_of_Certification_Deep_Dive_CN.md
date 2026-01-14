# The Design and Price of Certification — 深度拆解笔记（OM / IO / 信息设计）

> 论文：Mäkimattila, Mikael; Shang, Yucheng; Shirakawa, Ryo. **The Design and Price of Certification**（2025-06-18）  
> 主题标签：Certification / Bayesian Persuasion / Selling Information / Mechanism Design / Screening / Signaling / Obedience Constraints  
> 本笔记目标：读完后你能（i）复述模型与时序，（ii）写出关键约束与收入表达式，（iii）理解最优菜单为何长成“两阈值 + 常数差分信息量”的形状，（iv）抓住背后的机制与反直觉点，达到 OM 博士生可复盘推导的程度。

---

## 目录（建议按这个顺序读）

1. [研究背景与动机](#研究背景与动机-motivation)  
2. [模型设定与假设](#模型设定与假设-model-setup--assumptions)  
3. [分析与求解](#分析与求解-analysis--solution)  
4. [主要结论与管理启示](#主要结论与管理启示-main-results--managerial-insights)  
5. [Reviewer's Critique](#reviewers-critique-严厉审稿人视角)  
6. [One More Thing](#one-more-thing-一个最值得分享的灵光一现)  

---

## 研究背景与动机 (Motivation)

这篇文章研究的不是“信息披露”本身，而是一个更现实、更刺耳的问题：

> **当信息必须通过第三方认证（certifier）生成与传递，而 certifier 又是利润最大化的机构时，认证的设计与定价会如何扭曲信息结构与市场参与？**

### 实践痛点：行业中到底卡在哪？

典型场景包括（论文给的直观例子）：

- **标准化考试与招生**：学生（sender）对自己能力有私有信念，购买测试机构（certifier）的考试服务，学校（receiver）据此录取。  
- **质量认证与市场交易**：企业/卖家（sender）购买质量证书影响消费者/买家（receiver）决策。

这些行业里常见的运营现象/争议点是：

1. **测试/认证往往被“产品化”成菜单**：不同价格、不同版本（加急、补考、premium certificate、不同级别认证）。这不仅是成本差异，更像是“筛选机制”。  
2. **认证的透明度与披露规则高度制度化**：接收方通常看到证书，但不一定看到“你选了哪个测试版本/考了几次”。这会改变激励。  
3. **“信息质量”与“收入”之间的张力**：如果 certifier 收入来自 sender（而非 receiver），它可能会选择让 receiver 获得更少、更弱的有用信息，只要还能让 sender 愿意付钱。

### 理论缺口：现有文献忽略了什么？

论文明确对话的文献脉络：

- **Bayesian persuasion**（Kamenica & Gentzkow 2011）：sender 能承诺一个信息披露规则来影响 receiver。  
  - **缺口**：很多现实场景 sender 无法可信承诺信息（你说你很强，谁信？），于是出现第三方 certifier。  
- **Selling information / menu of experiments**（Bergemann, Bonatti & Smolin 2018）：principal 向“信息的使用者”出售一组实验（experiments），买家用信息改善自己的决策。  
  - **缺口**：在本文里，买信息的人（sender）并不是为了自己做决策，而是为了**说服另一个人**（receiver）做决策；更关键的是：**sender 选了哪一种测试，本身就会向 receiver 传递信息**（selection/signaling effect）。  
    - 这会让最优化问题不再能“逐点(pointwise)”优化每个类型的实验：因为一个类型的设计会改变其他类型的可行性（通过 receiver 的推断与 obedience constraints）。

### 核心贡献：Significance 在哪？

我把贡献拆成三条（每条都对应一个“你读完会记住的结论”）：

1. **提出并解决了“认证菜单 + 说服 + 选择可观察”的联合设计问题**：模型同时含有  
   - 机制设计（IC/IR + screening）、  
   - 信息设计（tests/experiments 的信息结构）、  
   - 信号传递（test choice 可观察导致 receiver 更新）。  

2. **主结果是一个非常尖锐的结构刻画（Theorem 1）**：最优认证菜单由两个阈值刻画：  
   - 低类型直接被排除（不买），  
   - 高类型被“池化(pooling)”买同一个“最值创造”的测试，  
   - 中间类型被“完全分离(full separation)”并购买一族折扣版测试；更反直觉的是：  
   - **所有被卖出的测试都具有相同的“差分信息量(differential informativeness)”**，从而导致  
   - **所有买测试的 sender 在菜单上对所有选项都无差异（indifferent）**，而  
   - **receiver 在均衡中拿到 0 surplus**（被逼到刚好服从、无信息租）。

3. **比较基准：若 test choice 不可观察，最优菜单可能完全变形（Section 4 / Proposition 1）**：在一定分布条件下，最优变成“两种极端测试”：  
   - 高类型买“完全信息”测试（fully informative），  
   - 中间类型买“完全不信息”测试（fully uninformative）但反而更贵，  
   - 低类型不买。  
   这直接给了一个政策/管理含义：**披露规则（是否公开你选了哪个测试/考了几次）会改变市场上可盈利的“认证产品形态”。**

---

## 模型设定与假设 (Model Setup & Assumptions)

这一部分我会用“记号表 + 时序 + 约束体系”的方式把模型搭起来；你应该能直接拿去复现推导。

### 符号体系（Notation）

| 符号 | 含义 |
|---|---|
| $\omega \in \Omega=\{L,H\}$ | 世界状态（低/高） |
| $\xi \in (0,1)$ | 共同先验 $P(\omega=H)=\xi$ |
| sender 的类型 $\theta \in [0,1]$ | sender 在观察私有信号后的“中间信念”(interim belief)：$\theta=P(\omega=H\mid \text{sender signal})$ |
| $F, f$ | $\theta$ 的分布与密度，full support 且绝对连续，满足 $E[\theta]=\xi$ |
| $a \in A=\{a_L,a_H\}$ | receiver 的行动（低/高） |
| $\mu$ | receiver 选择 $a_H$ 的门槛信念（由 payoff 决定） |
| certifier 的菜单 $\mathscr{M}=(\mathscr{E},t)$ | $\mathscr{E}$ 为测试集合，$t:\mathscr{E}\to \mathbb{R}$ 为价格函数 |
| 测试 $E=(S,\pi)$ | 信号空间 $S$ 与实验/信息结构 $\pi:\Omega\to \Delta(S)$ |
| 价格 $t(E)$ | 购买测试 $E$ 的一次性支付（**不能依赖测试结果**） |
| 行动推荐概率 $\pi_\omega(\theta)$ | 经过化简后：在状态 $\omega$ 下推荐 $a_H$ 的概率（见下文） |
| 差分信息量 $x(\theta)$ | $x(\theta)=\pi_H(\theta)-\pi_L(\theta)$ |
| 虚拟类型 $\psi(\theta)$ | $\psi(\theta)=\theta-\frac{1-F(\theta)}{f(\theta)}$（Myerson 虚拟估值） |

---

### Players, Sequence of Events, Information Structure

#### Players（3 个玩家）

- **Certifier（C）**：设计并定价测试菜单，目标最大化期望收入。  
- **Sender（S）**：有部分私有信息（$\theta$），买测试为了影响 receiver 行动。  
- **Receiver（R）**：观察测试选择与测试结果后行动，目标匹配状态。

#### 时序（Timing）

1. Certifier 发布菜单 $\mathscr{M}=(\mathscr{E},t)$.  
2. Sender 观察私有信息并形成类型 $\theta$.  
3. Sender 选择买某个测试 $E\in\mathscr{E}$ 或不买，并支付 $t(E)$.  
4. Receiver 观察到 sender 选的测试 $E$ 以及测试信号 $s$.  
5. Receiver 更新信念，选行动 $a\in\{a_L,a_H\}$.

> 关键：receiver **能看到 sender 选了哪个测试**（主模型）。这使得“选测试”成为额外信号渠道。

#### 信息结构（Information Structure）

- 状态 $\omega$ 二元。sender 的私有信号导致其 belief 类型 $\theta$，但 certifier 与 receiver 看不到 $\theta$。  
- certifier 的测试 $E$ 产生一个公共信号（可被 receiver 观察）。  
- receiver 在看到“测试选择 + 信号结果”后行动。

---

### 目标函数与约束：三方收益

#### Receiver payoff 与门槛 $\mu$

receiver 希望行动匹配状态：

- $v_R(a_H,H)>0>v_R(a_H,L)$，且归一化 $v_R(a_L,L)=v_R(a_L,H)=0$。  
- 因此存在门槛 $\mu$，使得 receiver 在 posterior $p$ 下选择 $a_H$ 当且仅当 $p\ge \mu$，其中  

$$
\mu=-\frac{v_R(a_H,L)}{v_R(a_H,H)-v_R(a_H,L)}.
$$

#### Sender payoff（关键：只在乎 receiver 是否选高行动）

sender 希望 receiver 总是选 $a_H$，不管状态：

$$
u_S=\mathbf{1}\{a=a_H\}-t(E).
$$

> 这把 sender 的价值函数变成“让 receiver 采取高行动的概率”，减去价格。

#### Certifier payoff

certifier 最大化期望收入：

$$
\max_{\mathscr{M}} \; \mathbb{E}_\theta[t(E(\theta))].
$$

---

### 关键化简 1：测试可等价为“行动推荐证书”

论文使用一个标准但很强力的简化：**任何测试都可等价为一个“行动推荐信号”**，即信号集合直接取 $S=A=\{a_L,a_H\}$，并要求 receiver 愿意服从推荐（obedience）。

因此对每个类型 $\theta$ 的测试可用两个数表示：

- $\pi_H(\theta)=\Pr(\text{推荐 }a_H\mid \omega=H)$  
- $\pi_L(\theta)=\Pr(\text{推荐 }a_H\mid \omega=L)$

差分信息量定义为：

$$
x(\theta)=\pi_H(\theta)-\pi_L(\theta).
$$

直觉：$x(\theta)$ 越大，测试越能区分状态（高状态更容易推荐高行动），也越“信息性强”。

---

### 关键化简 2：分区(partition) + 机制（direct mechanism）

certifier 可用 revelation principle 风格论证：只需考虑**直接机制**：

$$
\mathscr{M}=\{(E(\theta),t(\theta)):\theta\in[0,1]\},
$$

并且在分析中引入一个分区 $\mathscr{P}$：同一组 $P\in\mathscr{P}$ 的类型被诱导购买同一个测试（同一 $(\pi_H,\pi_L)$ 与价格）。

> 这一步非常关键：因为 receiver 观察到“你选了哪个测试”，于是她会先根据测试选择推断 sender 类型所在组 $P$，形成组内平均信念 $\mu_P$，再根据推荐信号更新。

---

### 约束体系：IC / IR / OB

下面是整篇论文的“骨架”。

#### (i) Receiver 的服从约束 (Obedience, OB)

设某组 $P$ 的 receiver 在只看到“选择了该组对应测试”时的 interim belief 为

$$
\mu_P=\mathbb{E}[\theta\mid \theta\in P].
$$

看到推荐 $a_H$ 后，posterior 为

$$
\Pr(H\mid a_H,P)=\frac{\mu_P\pi_H}{\mu_P\pi_H+(1-\mu_P)\pi_L}.
$$

服从 $a_H$ 的约束就是

$$
\frac{\mu_P\pi_H}{\mu_P\pi_H+(1-\mu_P)\pi_L}\ge \mu.
$$

论文把高行动服从写成等价形式（我也推荐你用这个）：

$$
\mu\big(\mu_P\pi_H+(1-\mu_P)\pi_L\big)\le \mu_P\pi_H.
\tag{OB-H}
$$

同理还有 $a_L$ 的服从约束（不展开）。后续主结果里，高行动约束基本会“卡死(binding)”。

---

#### (ii) Sender 的激励相容 (Incentive Compatibility, IC)

sender 类型 $\theta$ 在机制下的期望效用是

$$
V(\theta)=\theta\pi_H(\theta)+(1-\theta)\pi_L(\theta)-t(\theta).
$$

引入“调整后的转移” $\hat t(\theta)=t(\theta)-\pi_L(\theta)$，则

$$
V(\theta)=\theta x(\theta)-\hat t(\theta).
$$

在单维类型下，经典 Myerson 结构告诉我们：机制 IC 当且仅当

1. $x(\theta)$ **非减**（monotone allocation）；
2. Envelope 条件成立：对任意 $\tilde\theta$，

$$
V(\theta)=V(\tilde\theta)+\int_{\tilde\theta}^{\theta}x(s)\,ds.
\tag{EV}
$$

所以 $V'(\theta)=x(\theta)$（几乎处处）。

---

#### (iii) 个体理性 (Individual Rationality, IR)

$$
V(\theta)\ge 0,\quad \forall \theta.
$$

在最优机制里，IR 会对某个边际类型 $\theta_0$ 绑定：$V(\theta_0)=0$。  
结合 $x(\theta)$ 的单调性与 (EV)，可把 IR 直观理解为：

- 低于边际类型的那些人“买了也不划算” → 最优往往让他们不买（或让他们得到 0 信息价值）。  
- 高于边际类型的人获得信息租（information rent），大小由 $\int x$ 决定。

---

### 关键假设（Assumptions）与合理性

1. **$\xi<\mu$（先验不足以让 receiver 自愿选高行动）**  
   - 若 $\xi\ge \mu$，certifier 可用“无信息测试 + 高价 + 不买就悲观惩罚”的均衡抽干全部 surplus，问题变得平凡。论文因此聚焦非平凡区间。  

2. **$F$ 正则（regularity）：虚拟类型 $\psi(\theta)$ 非减**  
   - Assumption 1：$\psi(\theta)$ 随 $\theta$ 单调上升。  
   - 作用：保证“局部提高信息量对收入的边际收益”在类型上有单调结构，使最优 $x(\theta)$ 呈现阈值/极值特征（类似最优拍卖里“分配是否扭曲”随虚拟估值的符号变化）。

3. **价格不能依赖测试结果**（与 Bergemann et al. 2018 一致）  
   - 这让测试设计的价值必须通过“事前愿意付多少钱”实现，避免 trivially 用结果定价榨干每个 realization。

4. **二元状态、二元行动、sender 只在乎高行动**  
   - 非常 stylized，但换来 sharp characterization：你可以把它理解为“最小模型”，抓住筛选+说服的核心摩擦。

---

## 分析与求解 (Analysis & Solution)

这一部分是整篇文章最精彩也最容易迷路的地方。我会用“先把问题写成一个可优化的数学对象 → 再解释为何最优长成那样”的方式来讲。

### Step 0：把收入写成 Myerson-式的“虚拟剩余”

论文推导出（Lemma 1）在给定分区 $\mathscr{P}$ 下的收入最大化问题。核心是把 $t$ 消掉，只留下 $(x,\pi_L)$。

虚拟类型：

$$
\psi(\theta)=\theta-\frac{1-F(\theta)}{f(\theta)}.
$$

在 IC 与 envelope 下，期望收入可写成（忽略常数项时的直觉表达）：

$$
\mathbb{E}[t(\theta)] = -V(0)+\mathbb{E}\big[\psi(\theta)x(\theta)+\pi_L(\theta)\big].
$$

- $\psi(\theta)x(\theta)$ 是典型的“虚拟剩余”项：提高差分信息量 $x$ 对不同类型的收益权重由 $\psi$ 决定。  
- $\pi_L(\theta)$ 出现在收入里很特别：它代表一种“把高行动推荐在低状态下也做得更频繁”的手段；只要不违反 obedience，它能提高 sender 得到高行动的概率，从而可被定价吸收。

---

### Step 1：为什么最优菜单里 obedience 往往是 binding？

这是一个极关键的“机制性”结论（直觉见 Corollary 2 的证明思路）：

> 对给定 $x(\theta)$，如果你能把 $\pi_L(\theta)$ 和 $\pi_H(\theta)$ 同时往上挪一点（保持差值 $x$ 不变），sender 的价值会提高，而 IC 不受影响；只要 obedience 仍成立，certifier 就能提高价格 → 收入上升。  
> 因此最优时，这种“往上挪”的空间必须被堵死，也就是 obedience 约束会卡死(binding)。

在数学上，若某组 $P$ 的 (OB-H) 绑定，我们可以把 $\pi_L$ 用 $x$ 和 $\mu_P$ 表示出来。

从 (OB-H) 的等式形式推导（建议你亲手做一遍）：

$$
\pi_L(P) = \frac{\mu_P(1-\mu)}{\mu-\mu_P}\,x(P), \qquad
\pi_H(P) = \pi_L(P)+x(P)=\frac{\mu(1-\mu_P)}{\mu-\mu_P}\,x(P).
\tag{*}
$$

这个等式是整篇文章的“齿轮箱”：

- 一旦 obedience 绑定，测试的两个维度 $(\pi_H,\pi_L)$ 被压缩成**一维选择**：只剩下 $x$（差分信息量）。  
- 但注意：系数依赖 $\mu_P$，而 $\mu_P$ 又由分区与选择揭示的信息决定 → **信息设计与机制设计通过 $\mu_P$ 耦合在一起**。

---

### Step 2：为什么最优分区是“单调区间”(monotone partition)？

论文用 Lemma 6 等证明：任何非单调分区都可以被“单调化”而不减收入。

直觉版总结：

- IC 要求 $x(\theta)$ 随 $\theta$ 非减。  
- 若分区是“穿插式”的（低类型和高类型混在一起买同一测试），为了满足 IC，这些交叉群组会迫使 $x$ 在其凸包上几乎处处相同。  
- 一旦 $x$ 被迫相同，继续用非单调分区只会让 receiver 的推断更麻烦、可行性更紧，而没有收益补偿；通过把分区整理成区间（按类型排序）可以弱化不必要的约束。

你可以把它看作一种“排序最优性”：在单维类型筛选里，最优分配通常是单调的；这里即使加入了信息结构，单调性仍被 IC 的铁锤敲回来。

---

### Step 3：最关键结构：$x(\theta)$ 只取两个值 $\{0,x^*\}$

在 regularity 下（$\psi$ 非减），论文证明最优菜单里的差分信息量满足：

$$
x(\theta)\in\{0,x(1)\}\quad \text{（进一步在最优里变成 } \{0,x^*\}\text{）}.
$$

直觉：

- 对某个分区组 $P$，提高 $x(P)$ 的边际收益大致与该组的“虚拟类型均值”相关。  
- regularity + 单调分区使得“更高的组”拥有更高的虚拟类型均值，于是存在一个 cutoff：  
  - cutoff 以上，提高 $x$ 增收；  
  - cutoff 以下，提高 $x$ 反而不划算（因为它主要增加信息租）。  
- 于是最优选择把 $x$ 推到两个极端：要么 0（不给差分信息），要么推到能推的最大值（但最大值受制于可行性，比如 $\pi_H\le 1$ 与 obedience）。

这一步的含义非常大：它把一个看似“连续设计空间”的信息结构问题，变成了一个很像 Myerson 的“是否扭曲/扭曲到边界”的问题。

---

### Theorem 1：最优菜单的精确形状

论文的主结果（Theorem 1）说：存在两个阈值 $0\le \theta_* \le \theta^* \le \mu$，使得最优菜单 $\mathscr{M}(\theta_*,\theta^*)$ 具有如下形式。

先定义：

- 顶部池化区间的条件均值

$$
\mu^*=\mathbb{E}[\theta\mid \theta\ge \theta^*].
$$

- 常数差分信息量（由顶部可行性 pin down）

$$
x^*=\frac{\mu-\mu^*}{\mu(1-\mu^*)}.
$$

- 对每个中间类型 $\theta\in(\theta_*,\theta^*)$，定义

$$
\pi_L^\theta=\frac{\theta(1-\mu)}{\mu-\theta}\,x^*.
$$

则最优菜单（用 $(\pi_H(\theta),\pi_L(\theta))$ 表示）是：

$$
(\pi_H(\theta),\pi_L(\theta))=
\begin{cases}
(0,0), & \theta\in[0,\theta_*),\**6pt]
(x^*+\pi_L^\theta,\;\pi_L^\theta), & \theta\in[\theta_*,\theta^*),\**6pt]
(1,\;1-x^*), & \theta\in[\theta^*,1].
\end{cases}
\tag{OPT}
$$

#### 结构解读：三段式 + 两个阈值

- **低类型 $[0,\theta_*)$：不买（或等价地买一个让 receiver 永远选 $a_L$ 的测试）**  
  - 这是典型“排除低估值用户”的 monopoly screening 逻辑，但这里估值不是单一的价格，而是“说服的成功率”。  

- **中间类型 $[\theta_*,\theta^*)$：完全分离（每个类型一个测试）**  
  - receiver 观察到你选的测试后，几乎就知道你的 $\theta$（分离）。  
  - 每个测试的差分信息量都是同一个 $x^*$，但 $\pi_L^\theta$（以及 $\pi_H^\theta$）随 $\theta$ 上升。  
  - 这段“分离”来自一个关键的凸性/Jensen 逻辑：在绑定 obedience 下，$\pi_L$ 与 $\mu_P$ 的关系是凸的，池化会损失 revenue。

- **高类型 $[\theta^*,1]$：池化买同一个测试**  
  - 这个测试满足 $\pi_H=1$：高状态下一定推荐 $a_H$，是“价值创造”最强的 persuasion test（类似 Bayesian persuasion 里 sender-optimal 的结构）。  
  - 但在低状态下也会以概率 $1-x^*$ 推荐 $a_H$（允许一定 false positive），其大小被 obedience 卡死。

---

### Corollary 1：买测试的人对所有选项都无差异（Indifference）

因为在最优菜单里 **所有卖出的测试都有同一个 $x^*$**，而 IC 下 sender 的效用可写为

$$
V(\theta)=\theta x^*-\hat t(\theta),\qquad \hat t(\theta)=t(\theta)-\pi_L(\theta).
$$

最优时 $\hat t(\theta)$ 对所有买家是常数（你可以用 $V(\theta_*)=0$ 和 envelope 推出来）：

- 若 $x(\theta)=x^*$ 对所有 $\theta\ge \theta_*$，则  
  $V(\theta)=\int_{\theta_*}^{\theta}x^*\,ds=(\theta-\theta_*)x^*$。  
- 又由 $V(\theta)=\theta x^*-\hat t(\theta)$ 得  
  $\hat t(\theta)=\theta_*x^*$，与 $\theta$ 无关。

于是对任意买测试的 sender，选择哪一个具体测试只要差分信息量相同，就给同样效用 → 无差异。

> **经济学直觉**：菜单里的“多版本”不是为了让不同类型获得不同效用（他们效用一样），而是为了让 receiver 从选择中推断类型、从而改变 obedience 的可行性与 certifier 的定价边界。  
> 这非常“机制设计味”：菜单是为了信息结构的可行性与抽租，而不是为了消费者福利。

---

### Corollary 2：receiver 预期收益为 0（被压到刚好愿意服从）

最优菜单中，高行动 obedience 对每个被选择的测试都绑定。绑定意味着：

- 看到推荐 $a_H$ 时 receiver 的 posterior 恰好等于门槛 $\mu$，因此她对 $a_H$ **刚好无差异**。  
- 由于 $a_L$ 的 payoff 被归一化为 0，且 $a_H$ 在门槛处期望 payoff 为 0，receiver 在均衡中拿到 0 surplus。

从机制角度看，这是 certifier 的最优“压榨”：任何让 receiver 严格更愿意选 $a_H$ 的松弛都意味着 certifier 还能把 $\pi_L$ 往上挪（让 sender 更容易拿到 $a_H$），然后提高价格。

---

### Corollary 3：sender 什么时候能拿到正租？

sender 的信息租来自 $x^*>0$ 时的 envelope 积分：

$$
V(\theta)=(\theta-\theta_*)x^* \quad (\theta\ge \theta_*).
$$

若 $x^*=0$，则所有人都没有信息租，菜单塌缩成一个单一测试：永远推荐 $a_H$（纯粹卖“许可/证书”而非信息）。

论文给出一个判断条件（Remark 1）来保证最优不是塌缩（从而 sender 有正 surplus）。在 uniform 分布例子里，这个条件可化简为 **$\mu>2/3$**。

> 直觉：receiver 越“苛刻”（$\mu$ 越大），要想说服她就越需要真正的信息差分，这会让 $x^*$ 变大，从而不可避免地产生信息租；certifier 有时宁愿让 sender 留一点租，也不愿把市场做得太小。
>
### 价格/转移函数的实现：把 $(\pi_H,\pi_L)$ 变成“可执行的价格表”

主结果给了最优菜单的**信息结构**（每个类型对应的 $(\pi_H,\pi_L)$），但在运营落地里你会自然追问：**价格 $t$ 到底怎么定，才能让不同类型“按剧本”选测试？**

利用 IC 的 envelope 结构，你其实可以把价格写得很干净。

1) 我们已经知道：对所有会买测试的类型（$\theta\ge \theta_*$），都有同一个差分信息量 $x^*$。  
2) 选择 IR 在边际类型绑定：$V(\theta_*)=0$。  
3) 由 $V'(\theta)=x^*$ 得到  

$$
V(\theta)=\int_{\theta_*}^{\theta}x^*\,ds=(\theta-\theta_*)x^*,\qquad \theta\ge \theta_*.
$$
1) 又因为 $V(\theta)=\theta x^*-\hat t(\theta)$，所以  

$$
\hat t(\theta)=t(\theta)-\pi_L(\theta)=\theta_*x^* \quad \text{对所有 }\theta\ge \theta_* \text{恒定}.
$$
于是价格表可以写成一句话：

$$
t(\theta)=\theta_*x^*+\pi_L(\theta).
\tag{Price}
$$

把各区间的 $\pi_L$ 代入即可得到显式价格：

- **不买区间 $\theta<\theta_*$**：$t(\theta)=0$（或等价地不提供）。  
- **中间分离区间 $\theta\in[\theta_*,\theta^*)$**：

$$
t(\theta)=\theta_*x^*+\frac{\theta(1-\mu)}{\mu-\theta}x^*.
$$

- **顶部池化区间 $\theta\in[\theta^*,1]$**：

$$
t_H=\theta_*x^*+(1-x^*).
$$

> 这也解释了“为什么会出现一堆版本但消费者无差异”：  
> 版本之间的差别体现在 $\pi_L(\theta)$（低状态下也给高推荐的概率），而价格正好跟着 $\pi_L$ 一起动，从而把消费者的效用“压平”。  
> 菜单的功能不是创造异质化效用，而是创造**可用于 receiver 推断的选择分离**。

---

### 与两个 benchmark 的对比：谁的目标不同，测试就会长得完全不同

论文的 Remark 2 给了两个自然 benchmark，用来凸显 revenue-maximizing 结果的“信息压缩”本质。

#### Benchmark A：最大化 certifier + sender 的联合剩余（joint surplus）

如果目标是最大化 sender 得到 $a_H$ 的概率（再把钱在两者之间转移），最优其实是卖**一个** persuasion test 给所有类型。  
由于此时 receiver 看到“买了测试”并不能从选择中推断类型，relevant belief 就是总体均值 $E[\theta]=\xi$。

该测试满足（并绑定 obedience）：

$$
\pi_H^{JS}=1,\qquad
\pi_L^{JS}= \frac{\xi(1-\mu)}{\mu(1-\xi)}.
$$

- $\pi_H^{JS}=1$：高状态一定推荐 $a_H$，最大化价值创造。  
- $\pi_L^{JS}$ 取到刚好让 receiver 愿意在看到 $a_H$ 推荐时服从的最大值。

直觉：**联合剩余最大化时，你不怕给 sender 留 rent；你只想让高行动发生得尽可能多。**

#### Benchmark B：最大化 receiver 的期望收益（receiver-optimal）

receiver 最喜欢信息充分（减少误判），所以最优是卖完全信息测试给所有类型：

$$
\pi_H^{R}=1,\qquad \pi_L^{R}=0.
$$

这使得推荐完全揭示状态：低状态永不推荐 $a_H$。

#### 本文的 revenue-maximizing 菜单：信息更少，但更赚钱

本文结果的关键区别是：certifier 把“信息性”压缩到能赚钱的最低水平，以限制 sender 的信息租。

论文给了一个非常漂亮的比较方式：在最优菜单下，receiver 的 posterior 分布相对于上述 benchmark 是一种 **mean-preserving contraction**（均值不变但方差更小），也可以直观理解为：

- revenue-maximizing 菜单让 receiver 的 posterior 支撑集落在 $[0,\mu]$ 的更窄区间（不会出现特别“确信为高”的后验）。  
- joint surplus 菜单的 posterior 支撑集是 $\{0,\mu\}$（更极端）。  
- receiver-optimal 的 posterior 支撑集是 $\{0,1\}$（最极端，信息最大）。

> 翻译成人话：利润最大化的 certifier **会刻意避免让 receiver 获得“非常强的好消息”**，因为那会让 sender 的私有信息在选择中变得更重要，从而必须让渡更多 rent。  

---

### Comparative Statics：关键参数变化会怎么影响均衡？

论文本身更偏“结构刻画”而非给闭式 comparative statics，但我们可以从关键公式里读出方向性。

#### 1) receiver 门槛 $\mu$ 上升（更保守、更难被说服）

从
$$
x^*=\frac{\mu-\mu^*}{\mu(1-\mu^*)}
$$
可见，在 $\mu^*$ 固定时，$\mu$ 上升通常会让 $x^*$ 上升（需要更大的差分信息量来让推荐 $a_H$ 可被服从）。

- **后果 A：信息租上升**（因为 $V(\theta)=(\theta-\theta_*)x^*$）。  
- **后果 B：certifier 更可能提高阈值 $\theta_*$ 或 $\theta^*$** 来限制进入者，避免把 $\mu^*$ 拉低导致 $x^*$ 更大。  
- **管理解读**：当接收方更严格（更高录取门槛、更严格监管、更高合规阈值），认证机构更倾向于：  
  - 提价/排除低端客户，  
  - 或推出更“硬”的信息结构（但这反而会给客户更多 rent）。

#### 2) 顶部池化组的均值 $\mu^*$ 上升（买家群体更“自信/优质”）

$\mu^*$ 上升会降低 $x^*$，因为 receiver 在看到高端测试被选择时已经更相信状态为高，于是测试本身不必那么“区分状态”也能让推荐被服从。

- **后果**：certifier 更愿意扩大服务范围或降低价格（因为信息租压力减轻）。  
- 但注意 $\mu^*$ 本身由 $\theta^*$ 决定：降低 $\theta^*$ 会降低 $\mu^*$，形成一个典型的“扩大市场 vs 增加信息租”的权衡。

#### 3) 类型分布 $F$ 的变化（尤其是虚拟类型 $\psi$ 的形状）

regularity（$\psi$ 单调）保证了最优结构的整洁。如果 $F$ 更偏向高类型（hazard rate 更高、虚拟类型更大），则提高 $x$ 的边际收益更可能为正，从而更可能出现 $x^*>0$ 与多测试菜单；反之可能塌缩。

---

### Section 4：若 test choice 不可观察，会发生什么？

当 receiver 看不到 sender 选了哪个测试时，“选择作为信号”的渠道消失，obedience 从“每个组都要满足”变成一个**总体约束**（aggregate obedience, AOB）：

$$
\frac{\mathbb{E}[\theta(1-\pi_H(\theta))]}{\mathbb{E}[\theta(1-\pi_H(\theta))+(1-\theta)(1-\pi_L(\theta))]}\le \mu \le
\frac{\mathbb{E}[\theta\pi_H(\theta)]}{\mathbb{E}[\theta\pi_H(\theta)+(1-\theta)\pi_L(\theta)]}.
\tag{AOB}
$$

在 $\psi$ 凹（concave）等条件下，论文给出 Proposition 1：最优菜单变成极端的三段式（见 Figure 2）：

- 高类型：$(\pi_H,\pi_L)=(1,0)$（完全信息）  
- 中间类型：$(1,1)$（完全不信息，但永远推荐 $a_H$）  
- 低类型：$(0,0)$（不买）

**关键直觉**：

- receiver 无法根据“你选了哪个测试”来更新，因此 certifier 可以向某些类型卖一种“看起来像证书但不含信息”的产品（完全不信息）。  
- 同时仍需靠少部分高类型的“真信息”来在总体上满足 AOB，让 receiver 在看到 $a_H$ 推荐时整体上愿意服从。

> 这给了一个很直观的现实映射：当“测试版本/次数/路径”不披露时，市场上更容易出现高价但低信息含量的认证产品（甚至近似 placebo）。

---

## 主要结论与管理启示 (Main Results & Managerial Insights)

这一节我按“机制揭示 → 对比 benchmark → 建议与政策含义 → 图表”的顺序来写。

### 机制揭示：新的 trade-off 与反直觉点

#### 1) 两条信息渠道的耦合：测试信息 vs 选择信息

receiver 学到信息的方式有两条：

1. **测试本身的信号**（$\pi_H,\pi_L$）。  
2. **sender 选了哪个测试**（通过分区 $\mathscr{P}$ 产生 $\mu_P$）。

最优设计的核心摩擦是：  

- 想让 receiver 服从 $a_H$ 推荐，你要么让测试更信息性强（更大 $x$），要么让“选这个测试的人看起来更好”（更高 $\mu_P$）。  
- 但提高 $x$ 会加剧 sender 的信息租（因为 IC 下 rent 随 $x$ 积分增长）。  
- 因此 certifier 会通过**限制进入/池化高端**来维持较高 $\mu_P$，从而减少对 $x$ 的依赖。

#### 2) 为什么中间类型要完全分离，而高类型反而池化？

这是 Figure 1 背后的微妙点：

- 对中间类型，绑定 obedience 后 $\pi_L(\mu_P)$ 是一个对 $\mu_P$ 的凸函数；在凸函数下，**分离（更多极端的 $\mu_P$）会提高期望值**（Jensen）。  
  - 经济意义：把“更好的中间类型”单独拎出来卖更高价值（也更高价）的测试，增收超过了对“更差中间类型”让利的损失。  
- 但对最顶端类型，$\pi_H\le 1$ 的上界开始起作用：当你想继续分离到更高 $\mu_P$ 时，$\pi_H$ 很快撞到 1，进一步分离带来的可行集收益变小，于是顶部出现池化区间 $[\theta^*,1]$。

#### 3) 反直觉：receiver 被逼到 0 surplus

很多人第一反应会是：“认证行业卖信息，receiver 应该收益更高”。  
这篇论文给的尖锐反例是：在利润最大化下，认证机构会把 receiver 压到刚好愿意服从的边界，使 receiver 预期 surplus 为 0。

这不是说 receiver 一定“什么都学不到”，而是说她学到的程度被设计成恰好让她不获得额外期望收益（信息租被转移到 sender/certifier 的可收费空间里）。

---

### 管理建议：对不同主体的行动含义

#### 对 certifier（测试机构/认证平台）

- **菜单不是为了“满足不同偏好”，而是为了“操控推断 + 抽租”**：  
  - 实务上你会看到“不同版本”之间信息质量差异可能很小，但价格差异很大；本文给了一个理论解释：关键是差分信息量保持常数，版本差异主要体现在 $\pi_L$（更容易给高推荐）。  
- **高端产品会趋向于“价值创造最大化”**：在顶部池化区间里，最优测试满足 $\pi_H=1$（高状态一定推荐高行动），这类似把高端测试做成“最能让 receiver 采取高行动”的 persuasion test。  
- **排除低端客户是利润最大化的一部分**：低类型被定价赶出市场（$\theta<\theta_*$）。

#### 对 receiver（学校/买家/监管者）

- **不要把证书当成“社会福利最大化的信息”**：证书可能被设计成最小化你的 surplus。  
- **披露规则是杠杆**：要求披露“选择了哪个版本/考了几次/是否 retake”能显著改变 certifier 可实现的最优菜单形态。  
  - 如果不披露，可能出现 Proposition 1 那种“昂贵但无信息”的证书产品。

#### 对政策制定者/行业监管（特别 relevant）

- **强制披露测试路径/版本/尝试次数**：能削弱 certifier 利用 aggregate obedience 出售“低信息高价”证书的空间。  
- **设置信息质量最低标准（minimum informativeness）**：否则利润动机会把信息压缩到对 receiver 贡献最小的边界。  
- **鼓励 receiver 端的独立验证**（独立考试、随机审计）：相当于提高 certifier 的可行集约束，让其无法仅靠设计把 receiver 推到 indifferent。

---

### 图表解释：Figure 1 与 Figure 2 在讲什么？

#### Figure 1（主模型：test choice 可观察）——三段式菜单的“几何直觉”

图 1 同时画了三条曲线：$\pi_H(\theta)$、$\pi_L(\theta)$、以及差分 $x(\theta)$。

你应当读出三点：

1. **$x(\theta)$ 是阶梯函数**：  
   - $\theta<\theta_*$：$x=0$（不给差分信息，等价不卖）；  
   - $\theta\ge \theta_*$：$x=x^*$（所有卖出的测试差分信息量相同）。  

2. **在中间区间 $[\theta_*,\theta^*)$，$\pi_L(\theta)$ 与 $\pi_H(\theta)$ 上升且呈凸形**：  
   - 因为它们通过公式 $\pi_L^\theta=\frac{\theta(1-\mu)}{\mu-\theta}x^*$ 依赖于 $\theta$，在 $\theta\to\mu$ 时会加速上升。  
   - 凸性意味着“分离优于池化”：把中间类型拆开能提高收入。

3. **在高区间 $[\theta^*,1]$，$\pi_H$ 撞到 1 并保持常数**：  
   - 这就是为什么顶部类型池化：进一步分离无法让 $\pi_H$ 超过 1，边际增益变小。

---

#### Figure 2（变体：test choice 不可观察）——“真信息 + 伪信息”并存

图 2 的菜单是阶梯状：

- 高类型：$(1,0)$ → 推荐完全揭示状态（高状态给 $a_H$，低状态给 $a_L$）。  
- 中间类型：$(1,1)$ → 永远推荐 $a_H$（完全不信息）。  
- 低类型：$(0,0)$ → 不买。

你应当读出的信息是：**当选择不可观察时，certifier 可以把“信息”集中在少数高类型上，用来支撑 receiver 的总体服从；同时向其他类型卖“看起来有用但实际上不提供区分信息”的证书。**

---

## Reviewer's Critique (严厉审稿人视角)

下面我会用“Senior Editor/Reviewer”口吻来挑刺——不是为了抬杠，而是为了告诉你：这个模型在哪些地方最强、在哪些地方最脆。

### 优点（为什么这篇值得发好刊）

1. **问题设定抓住了现实认证行业的核心摩擦**：profit motive 与 information quality 的冲突，加上“选择可观察”的制度细节，非常真实。  
2. **把三种理论工具焊在一起而且焊得很干净**：mechanism design（IC/IR/virtual types）、Bayesian persuasion（信息结构）、signaling（choice reveals type）。  
3. **结构刻画极其 sharp**：两阈值 + 常数差分信息量 + receiver 0 surplus。能给很多后续工作当“基准定理”。  
4. **Section 4 的对比很有力量**：同一个经济问题，仅仅改一个制度细节（choice 是否可观察）就让最优菜单“从连续家族变成极端阶梯”，这很适合做 policy relevance。

### 缺点与潜在争议（会被 reviewer 追着问的点）

1. **均衡选择问题很硬**：  
   - 在最优菜单下，所有买家对所有测试无差异（Corollary 1）。  
   - 那么“为什么类型 $\theta$ 会选择机制想让她选择的那个测试？”  
   - 论文用“certifier-optimal PBE + 纯策略”作为聚焦，但现实中这意味着：  
     - 需要某种外生的 tie-breaking 规则，或者  
     - certifier 需要额外设计微小扰动/随机化来实现分离。  
   - 这不是致命问题，但会影响可实现性与实证含义。

2. **sender 偏好极端简化**：sender 只关心 receiver 是否选 $a_H$，且对状态无关。  
   - 在很多场景（比如卖家质量认证），低状态下被“误判为高”可能带来后续惩罚、退货、诉讼等；那会改变 sender 对 $\pi_L$ 的偏好，从而改变最优菜单形态。  

3. **二元状态/行动 + 单 receiver**：  
   - OM 场景经常是多维质量、多级行动（定价、产量、配给、录取名额）、多 receiver（市场端竞争、多个学校）。  
   - 二元化使得 obedience 约束非常整洁，但也可能放大了“receiver 0 surplus”这种边界结果的普遍性。

4. **certifier 的成本结构缺席**：  
   - 测试设计与实施成本可能随 informativeness 增加而上升。  
   - 若加入成本，$x$ 不一定推到边界，菜单结构可能更平滑。  
   - 目前结果更适合解释“信息可以被任意设计、成本忽略”的行业（如某些认证流程）而非严格成本递增的实验检测（如医学检验）。

5. **outside option 设定与惩罚信念**：  
   - 论文证明“在 certifier-optimal equilibrium 下，不买的外部选项可设为 0”是 WLOG，但它仍依赖于某种均衡选择（pessimistic beliefs）。  
   - 如果你关心更稳健的均衡选择概念，可能需要再讨论。

### 未来研究方向（在这篇基础上，哪些扩展最有价值？）

1. **动态/重复认证：retake 与选择披露规则内生化**  
   - “考几次”“只报最好成绩”是现实中最重要的制度变量之一。  
   - 这篇 Section 4 已经点燃了火药桶：可见性改变最优菜单。把它做成动态模型会非常有价值。

2. **竞争与平台治理**：多个 certifier 竞争时，是否仍会出现“receiver 0 surplus”？  
   - 竞争可能迫使信息更充分（像市场上的透明度竞争），也可能导致 race to the bottom（卖更便宜的“伪证书”）。  
   - 这是 OM/IO 都很关心的。

3. **多维类型（confidence + cost + moral hazard）**  
   - sender 的类型不只是 belief；还有能力、努力成本、风险厌恶、 reputational concerns。  
   - 多维会打破单调性与常数 $x$ 的简洁结构，但也更贴近运营现实。

4. **receiver 的最优响应不止阈值**  
   - 例如 receiver 有 capacity constraint（只能录取一定人数）、或 payoff 非线性（错录代价随规模变化）。  
   - 这会把 obedience 变成更复杂的条件，可能产生新的菜单形态。

---

## One More Thing：一个最值得分享的“灵光一现”

我认为这篇文章最漂亮的“数学技巧/洞见”是下面这个组合拳（读懂它，你就抓住了整篇的灵魂）：

### 把“信息设计 + 筛选 + 选择可观察”压缩成一个可控的一维对象：$x(\theta)$

表面上，certifier 在选择一个非常复杂的对象：对每个类型设计一个实验 $\pi(\cdot\mid \omega)$，还要定价，还要考虑 receiver 的 Bayes 更新与服从，还要考虑 sender 的选择揭示信息。

论文的关键转化是：

1. 先把信号空间化简为行动推荐 $(a_L,a_H)$；  
2. 用 $x(\theta)=\pi_H(\theta)-\pi_L(\theta)$ 把 sender 的 IC 变成“$x$ 单调 + envelope”；  
3. 用“最优时 obedience 绑定”把 $\pi_L,\pi_H$ 用 $(x,\mu_P)$ 表示（公式 (*)）；  
4. 这样一来，在给定分区 $\mathscr{P}$ 时，问题几乎变成：选择一个单调的 $x(\theta)$ 来最大化一个 Myerson-式目标。  
5. 然后再用凸性（Jensen）与 mean-preserving contraction 的思路去比较分区，推出“中间分离 + 顶部池化”。

> 换句话说：作者把一个看似多维、强耦合的机制设计问题，通过“绑定约束 + 单调结构 + 凸性比较”压缩成一个你可以真正算的结构刻画。  
> 这就是高级理论论文里最值得偷走的手艺：**把复杂机制问题找到一个“足够的统计量(sufficient statistic)”并围绕它做结构定理。**

---

## （可选）复盘推导的最小清单（你可以按这个自己推一遍）

1. 写出 receiver 门槛 $\mu$ 与 (OB-H)；推导绑定时的公式 $(*)$。  
2. 写出 sender 价值 $V(\theta)=\theta x(\theta)-\hat t(\theta)$；写出 IC 的 monotone + envelope。  
3. 用虚拟类型 $\psi(\theta)$ 写出收入表达式 $\mathbb{E}[\psi x+\pi_L]$（理解 $\pi_L$ 为“在低状态也给高推荐”的可收费空间）。  
4. 解释为什么在最优下（几乎所有组）(OB-H) 必绑定（否则可以共同上移 $\pi_L,\pi_H$ 增收）。  
5. 在 monotone partition 下，理解为什么 $x(\theta)$ 取极值 $\{0,x^*\}$（regularity + 单调权重）。  
6. 在绑定 obedience 下，理解 $\pi_L(\mu_P)$ 的凸性与 Jensen：为什么中间类型不应池化。  
7. 顶部池化来自 $\pi_H\le 1$ 的上界：一旦 $\pi_H$ 撞墙，继续分离收益下降。  
8. 得到 (OPT) 的三段式结构，并用 $V(\theta_*)=0$ 推出价格结构 $\hat t=\theta_*x^*$ 与 indifference。

---

*完。*

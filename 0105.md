# Colombo, Graziano & Pignataro (2024) 深度解析

**Imperfect history-based price discrimination with asymmetric market shares**（Information Economics and Policy, 2024）

> 论文 PDF：
> 关键词：History-based price discrimination、information completeness（信息完整度）、asymmetric market shares（非对称市场份额）、sequential pricing（序贯定价）、poaching（挖角/抢客）

---

## 0. 这篇文章到底“卡”住了哪个关键问题？

这篇文章的核心不是“价格歧视会不会更激烈”这种老生常谈，而是一个更现实、更尖锐的运营逻辑：

* **企业想做 history-based price discrimination（基于历史的定价），但现实里“识别老客”永远不完美**。
* 一旦识别不完美，**给“新客/未知客”的优惠（$\tilde p$）会误伤一部分本应被你收割的老客**（因为他们没被识别出来）。
* 这种“误伤”对**大厂（dominant firm）尤其致命**：盘子大，误伤面也大；于是大厂反而可能选择**不挖角、走 uniform pricing**，而小厂继续靠折扣“进攻”。

论文用一个非常干净的 Hotelling 结构，把这件事推到一个可以写出闭式解、还能做 welfare 分析的程度。

---

## 1. 研究背景与动机 (Motivation)

### 1.1 实践痛点：行业里到底发生了什么？

现实里你经常看到这种“反直觉的价格战形态”：

* 大平台/大银行/大运营商：**对老客并不一定更优惠**，甚至更“硬”。
* 小平台/新进入者：疯狂给“新客”优惠（礼包、券、首月免费），用低价去**poach** 竞争对手的客户。

这背后有两个运营层面的“硬约束”：

1. **客户历史识别不完美**
   监管（如 GDPR）要求同意才能追踪；用户会 opt-out、清 cookie；线下现金交易更难追踪；会员卡/问卷覆盖不全。于是：

   * 你能识别一部分老客（可以“精准收割”）
   * 但识别不到的那部分老客会混在“未知客/新客池子”里
   * 你给新客的优惠会“漏给”这部分老客

2. **市场份额不对称 + 定价技术不对称**
   大厂可能更新慢（流程/系统老），小厂可能更灵活（算法、更新频率高）。现实中经常是**小厂更像“算法跟随者”**，可以观察大厂动作后快速调整。

### 1.2 理论缺口：现有文献忽略了什么？

经典 history-based / behavior-based pricing 文献常见两类强假设：

* **完美识别**：企业能完整知道哪些消费者是自己 turf（老客），哪些是 rival turf（对手老客）。
* **对称性**：市场份额对称、企业策略对称、同时行动（simultaneous pricing）。

这篇文章把两个“现实中的脏东西”同时塞进模型：

* **信息不完美但不犯错**：不是 noisy signal（会误判），而是 **missing-but-correct**：以概率/比例 $\alpha$ 识别老客，其余完全不知道（但不会把别人的老客误当成自己的）。
* **市场份额非对称**：$k\neq 1/2$，且还专门讨论了序贯行动（dominant 先动，小的后动）。

这两个组合在一起，会让很多“完美信息下的整洁结论”变成 **knife-edge**（刀刃型特例）。

### 1.3 核心贡献：Significance 在哪？

我把它压缩成三条“可以拿去写文献综述的贡献”：

1. **机制贡献（Mechanism）**：提出并刻画了“识别不完美导致的折扣误伤（collateral discounting）”，并证明这会让 dominant firm 在某些区域主动选择不挖角、转向 uniform pricing。
2. **结构贡献（Market configuration）**：在序贯定价下给出**任意 $(\alpha,k)$ 都存在纯策略均衡**，并刻画均衡在 **weak dominance**（双边挖角）与 **strong dominance**（单边挖角）之间切换的阈值。
3. **政策/管理含义（Welfare & regulation）**：社会福利 $SW$ 对信息完整度 $\alpha$ **单调下降**，但消费者剩余 $CS$ 的最优 $\alpha$ 却依赖市场不对称程度——监管者会面临“总福利 vs 消费者保护”的硬 trade-off。

---

## 2. 模型设定与假设 (Model Setup & Assumptions)

### 2.1 符号体系（建议你把这张表背下来）

| 类别       | 符号                        | 含义                                                       |
| -------- | ------------------------- | -------------------------------------------------------- |
| 空间/偏好    | $x\in[0,1]$               | 消费者在 Hotelling 线上的位置（偏好）                                 |
| 企业位置     | $l_A=0,;l_B=1$            | Firm A 在 0，Firm B 在 1                                    |
| 基础价值     | $v$                       | 产品的基础效用（假设足够大，保证 full market coverage）                   |
| 差异化强度    | $t>0$                     | “运输成本”/品类差异带来的效用损失                                       |
| 成本       | $c=0$                     | 边际成本归一化为 0                                               |
| 历史市场份额   | $k\in[1/2,1]$             | Firm A 的 inherited market（turf）长度；A 为 dominant           |
| 信息完整度    | $\alpha\in[0,1]$          | firm 能识别自己老客的比例（或概率）                                     |
| 价格（决策变量） | $\phi_j={p_j,\tilde p_j}$ | firm $j$ 对两类消费者的报价：识别老客价 $p_j$、未知客价 $\tilde p_j$         |
| 无差异点     | $x_A,x_B,x_U$             | 三个 cutoffs：A turf 已识别消费者的切换点、B turf 已识别消费者的切换点、未知消费者的切换点 |
| 利润       | $\pi_A,\pi_B$             | 两家利润                                                     |

> 重要直觉：$\tilde p_j$ 不是“只给对手客户”的价。它给的是“我识别不到的所有人”，其中包含：对手老客 + 我自己的漏网老客。这正是全篇的摩擦源头。

---

### 2.2 消费者效用与需求结构

消费者 $i$ 在位置 $x$，购买 firm $j\in{A,B}$ 的效用为
$$
u_i^j(x)=v-\phi_j-t|x-l_j|.
$$
假设 $v$ 足够大，使得均衡中每个消费者都买一件（full coverage）。

---

### 2.3 “历史”（purchase history）如何进入模型：turf 的划分

* Firm A 的 inherited market（turf）为
  $$
  T_A={x: x\le k},
  $$
* Firm B 的 inherited market 为
  $$
  T_B={x: x\ge k}.
  $$

当 $k=1/2$ 对称；当 $k>1/2$，A 继承了更大份额，因此被称为 dominant firm（注意这不是法律意义的 dominance，只是份额描述）。

---

### 2.4 信息结构：不完美但不犯错（partial-but-correct）

信息技术的“完整度”用 $\alpha$ 表示：

* 对于属于 firm $j$ 的 turf 的消费者，在每个 $x$ 上有比例 $\alpha$ 被 firm $j$ **正确识别**为“我的老客”（identified）。
* 剩余比例 $1-\alpha$ 对 firm $j$ 来说就是“身份未知”（unidentified），但注意：**不是误识别**，而是“识别不到”。

因此：

* identified 消费者：只被其历史所属 firm 识别；对 rival 来说仍是 unidentified。
* unidentified 消费者：对两家来说都 indistinguishable（只能按统一的 $\tilde p$ 报价）。

---

### 2.5 定价结构：两部价格（但不是两段式收费）

每家企业 $j$ 同时设置两口价：

* $p_j$：只对“被我识别的老客”报价
* $\tilde p_j$：对**其他所有人**报价（包括：对手老客 + 全部未知消费者 + 我自己的漏网老客）

这是标准的 third-degree price discrimination（按分组定价），分组依据是“历史身份是否被识别”。

---

### 2.6 博弈/决策结构（Sequence of Events & Information）

基准模型是 **sequential move game**：

1. Firm A 先动，选择 $(p_A,\tilde p_A)$
2. Firm B 观察到 A 的定价后，再选择 $(p_B,\tilde p_B)$
3. 消费者观察所有价格后选择购买对象

信息结构：

* firms 对 $(v,t,k,\alpha)$ 共同知识
* 但对单个消费者是否被识别存在制度性缺口（由 $\alpha$ 描述的“可识别比例”）

---

### 2.7 关键无差异点（Demand cutoffs）

**(i) A turf 的 identified 消费者（被 A 识别）**
他们面对：A 报价 $p_A$；B 报价 $\tilde p_B$。
无差异点满足
$$
v-p_A-tx=v-\tilde p_B-t(1-x)
;\Rightarrow;
x_A=\frac{\tilde p_B-p_A+t}{2t}.
$$

**(ii) B turf 的 identified 消费者（被 B 识别）**
他们面对：B 报价 $p_B$；A 报价 $\tilde p_A$。
无差异点满足
$$
v-\tilde p_A-tx=v-p_B-t(1-x)
;\Rightarrow;
x_B=\frac{p_B-\tilde p_A+t}{2t}.
$$

**(iii) 全部 unidentified 消费者（两家都识别不了）**
他们面对：A 报价 $\tilde p_A$；B 报价 $\tilde p_B$。
无差异点满足
$$
v-\tilde p_A-tx=v-\tilde p_B-t(1-x)
;\Rightarrow;
x_U=\frac{\tilde p_B-\tilde p_A+t}{2t}.
$$

---

### 2.8 两种市场结构：weak dominance vs strong dominance

这篇文章的“剧情分支”来自于 $x_B$ 相对 $k$ 的位置：

* **Weak dominance（双边挖角）**：$x_A<k<x_B$
  两边都发生 poaching：B 挖 A 的老客（左侧），A 也挖 B 的老客（右侧）。论文 Fig.1（第 5 页）画的是这个结构。
* **Strong dominance（单边挖角：A 强势但反而不挖角）**：$x_A<k=x_B$
  A 不挖 B 的 identified 消费者；B 作为 second mover 仍会在左侧挖 A。论文 Fig.2（第 5 页）画的是这个结构。

---

### 2.9 目标函数（利润）与约束

因为边际成本 $c=0$，利润就是价格乘以需求量。论文给出统一表达（适用于两种结构）：

$$
\pi_A
=

p_A\alpha \min{x_A,k}
+
\tilde p_A\Big[\alpha\max{0,x_B-k}+(1-\alpha)x_U\Big],
\tag{1}
$$

$$
\pi_B
=

p_B\alpha \min{1-k,1-x_B}
+
\tilde p_B\Big[\alpha\max{0,k-x_A}+(1-\alpha)(1-x_U)\Big].
\tag{2}
$$

你可以把 (1)(2) 按“钱从哪里来”拆成三块：

* **收割 identified 老客**：$p_j\times$（被识别且留存的老客量）
* **poaching identified 对手老客**：$\tilde p_j\times$（对手老客中被识别那部分里被你抢到的量）
* **争夺全市场的 unidentified 人群**：$\tilde p_j\times$（两家都识别不了的人里选择你的量）

---

### 2.10 核心假设与合理性（Justification）

1. **Full market coverage（$v$ 足够大）**：避免引入“不买”的边界，让焦点集中在定价与抢客机制上。
2. **信息“不完美但不犯错”**：现实里 cookie/会员体系更像“覆盖不全”，不是经常把 A 客户错标成 B 客户。
3. **$\tilde p$ 对所有 unknown 一口价**：现实中你给“新客优惠券”往往没法区分“真新客”和“清了 cookie 的老客”。
4. **序贯定价**：反映定价技术/更新频率差异（大厂慢、小厂快，或一方用算法跟随）。
5. **无额外 switching cost**：把切换成本“内生”为 Hotelling 的差异化（$t$），并聚焦“信息不完美”带来的额外摩擦。

---

## 3. 分析与求解 (Analysis & Solution)

### 3.1 求解逻辑总览：Backward Induction + 市场结构选择

因为是序贯博弈：

* **先**：给定 A 的价格，解 B 的 best response（第二阶段）
* **再**：A 预期 B 的反应，选 $(p_A,\tilde p_A)$（第一阶段）
* **最后**：A 还会“挑市场结构”（weak vs strong），因为它先动，能通过定价把市场推向对自己更有利的结构

---

### 3.2 Weak dominance（双边挖角）下的均衡

#### 3.2.1 第二阶段：B 的 best response（给定 A 的价格）

在 weak dominance 假设下 $x_B>k$，B 的 identified 老客需求量为 $\alpha(1-x_B)$。代入 $x_B=\frac{p_B-\tilde p_A+t}{2t}$，B 在 $p_B$ 上的利润项等价于
$$
\alpha p_B(1-x_B)=\frac{\alpha}{2t},p_B\big(t+\tilde p_A-p_B\big).
$$
对 $p_B$ 求一阶条件得到：
$$
p_B^w(\tilde p_A)=\frac{t+\tilde p_A}{2}.
\tag{3}
$$

对 $\tilde p_B$，B 面对的是“挖 A 的（identified）老客 + 争夺 unidentified 市场”的综合需求。把 $x_A$、$x_U$ 代入 (2) 并对 $\tilde p_B$ 做一阶条件，可得：
$$
\tilde p_B^w(p_A,\tilde p_A)
=

\frac{(1-\alpha)\tilde p_A+\alpha p_A+t\big[1-2\alpha(1-k)\big]}{2}.
\tag{4}
$$

**运营直觉（别跳过）**：

* (3) 里 $p_B$ 只依赖 $\tilde p_A$：因为 B 的 identified 老客是否被挖走，取决于 A 对“未知人群”的报价 $\tilde p_A$（A 无法对 B 的 identified 老客开 $p_A$）。
* (4) 是个加权平均：$\alpha p_A+(1-\alpha)\tilde p_A$。因为 $\tilde p_B$ 既要对抗 A 给其 identified 老客的 $p_A$，也要对抗 A 给未知人群的 $\tilde p_A$。

并且你能看出 **prices are strategic complements**：A 提价会推高 B 的最优反应。

---

#### 3.2.2 第一阶段：A 预期 B 反应后的最优定价

把 (3)(4) 代回 A 的利润 (1)，对 $p_A,\tilde p_A$ 做最优化，得到 weak dominance 下的闭式解：

$$
p_A^w
=

\frac{t\big[6-4\alpha-(1-2k)\alpha^2\big]}{2(2-\alpha^2)},
\tag{5}
$$

$$
\tilde p_A^w
=

\frac{t\big[6-4\alpha(1+k)+\alpha^2\big]}{2(2-\alpha^2)}.
\tag{6}
$$

再代回 (3)(4)，得到 B 的均衡价格（论文也给出闭式表达）：

$$
p_B^w
=

\frac{t\big[10-4\alpha(1+k)-\alpha^2\big]}{4(2-\alpha^2)},
\tag{7}
$$

$$
\tilde p_B^w
=

\frac{t\big[10-4\alpha(3-k)-\alpha^2(1-4k)+2\alpha^3(1-k)\big]}{4(2-\alpha^2)}.
\tag{8}
$$

---

#### 3.2.3 weak dominance 可行条件：$x_B>k$

均衡价格需要“自洽”地满足 weak dominance 的市场结构（尤其是 $x_B>k$）。论文指出在一系列不等式中，关键约束就是 $x_B>k$，它等价于：

$$
k\le \tilde k(\alpha)\equiv \frac{6+4\alpha-7\alpha^2}{16-4\alpha-8\alpha^2}.
$$

并且当 $\alpha<1-\frac{\sqrt{3}}{3}\approx 0.42$ 时，$\tilde k(\alpha)<1/2$，意味着即便市场份额几乎对称，weak dominance 也难以成立——信息太不完整，挖角激励撑不起来。

---

### 3.3 Strong dominance（单边挖角）下的均衡：A 放弃挖角

#### 3.3.1 第二阶段：B 用“约束绑定”来设定 $p_B$

在 strong dominance 中假设 $x_B\le k$，也就是 A 不会挖走 B 的 identified 老客。因为 B 是 second mover，它可以把 $p_B$ 设到刚好让边界消费者 $x=k$ 不愿切换：

$$
v-\tilde p_A-tk=v-p_B-t(1-k)
;\Rightarrow;
p_B^s(\tilde p_A)=\tilde p_A+t(2k-1).
\tag{11’}
$$

这其实是一个很漂亮的“**把不等式变等式**”技巧：在强势区域里，B 的最优 $p_B$ 往往是让“被挖走的边界”刚好不发生（constraint binding），类似于一种局部的 limit pricing。

B 的 poaching/unidentified 价格的 best reply 与 weak dominance 形式相同：

$$
\tilde p_B^s(p_A,\tilde p_A)
=

\frac{(1-\alpha)\tilde p_A+\alpha p_A+t\big[1-2\alpha(1-k)\big]}{2}.
\tag{9}
$$

---

#### 3.3.2 第一阶段：A 的最优反应——直接变成 uniform pricing

把 B 的反应代回 (1)，A 的最优解在 strong dominance 下极其简洁：

$$
p_A^s=\tilde p_A^s=\frac{t\big[3-2\alpha(1-k)\big]}{2}.
\tag{10}
$$

也就是说：**dominant firm A 在 strong dominance 均衡里干脆不区分 identified vs unidentified，统一报价**。

对应 B 的均衡价格为：

$$
p_B^s
=

\frac{t\big[1-2\alpha(1-k)+4k\big]}{2},
\tag{11}
$$

$$
\tilde p_B^s
=

\frac{t\big[3-4\alpha(1-k)+2k\big]}{4}.
\tag{12}
$$

**机制直觉**：

* A 的 inherited share 大（$k$ 大）意味着：如果 A 想靠降低 $\tilde p_A$ 去 poach，对自己的“漏网老客”（比例 $1-\alpha$）也要同步降价，**误伤面积大**。
* 所以 A 选择“别挖了”，用 uniform pricing 把战场交给 B；B 作为 second mover 仍可以对 A 的 turf 用 $\tilde p_B$ 做进攻，同时对自己的 identified 老客用 $p_B$ 收割。

---

### 3.4 A 如何选择市场结构？（均衡结构是内生的）

关键问题：A 先动，可以通过第一阶段定价“诱导”市场进入 weak 或 strong。论文做法是比较 A 在两种结构下的利润。

论文给出差值（非常关键）：

$$
\pi_A^w-\pi_A^s
=

\frac{\alpha\Big(8k^2\alpha^3+8k^2\alpha^2-16k\alpha^3+8k\alpha^2+32k\alpha-48k+8\alpha^3-17\alpha^2+18\Big)}{16(2-\alpha^2)}.
\tag{13}
$$

注意 (13) 的分子对 $k$ 是**二次函数**。因此可以定义阈值 $k_1(\alpha)$ 为使 $\pi_A^w=\pi_A^s$ 的（经济相关的）根。

更“可复盘”的写法是直接用二次系数表示：

令
$$
A(\alpha)=8\alpha^2(1+\alpha),
\quad
B(\alpha)=8(-2\alpha^3+\alpha^2+4\alpha-6),
\quad
C(\alpha)=8\alpha^3-17\alpha^2+18.
$$

则 $k_1(\alpha)$ 是方程 $A(\alpha)k^2+B(\alpha)k+C(\alpha)=0$ 在 $[1/2,1]$ 上的有效解（取较小的那根）：

$$
k_1(\alpha)=\frac{-B(\alpha)+\sqrt{B(\alpha)^2-4A(\alpha)C(\alpha)}}{2A(\alpha)}.
$$

论文的 **Proposition 1** 可以用一句话总结：

> **Proposition 1（核心结构结果）**：在 sequential move game 中，对任意 $\alpha\in(0,1]$ 与 $k\in(1/2,1]$，存在阈值 $k_1(\alpha)\ge 1/2$，使得：当 $k\le k_1(\alpha)$ 时唯一纯策略均衡为 weak dominance；当 $k>k_1(\alpha)$ 时唯一纯策略均衡为 strong dominance。

并且 $k_1(\alpha)$ 随 $\alpha$ 上升（论文 Fig.3，第 7 页），意味着：

* 信息越完整（$\alpha$ 越大），越可能进入“互挖角”的激烈竞争。
* 信息越残缺（$\alpha$ 越小），dominant firm 越倾向放弃挖角、转向 strong dominance（“稳住自己的盘子，别乱打折”）。

---

## 4. 比较静态与核心命题的经济学直觉 (Comparative Statics & Mechanisms)

### 4.1 Proposition 2：dominant firm 利润永远更低（很反直觉，但很有味道）

论文 **Proposition 2**：

> 在 weak 与 strong dominance 中，Firm A（dominant）的利润都低于 Firm B（小 firm）。

**直觉拆解**：

* A 的 turf 大 ⇒ 消费者偏好跨度大 ⇒ A 很难用一个 $p_A$ 精准贴近“老客平均愿付价”。
* B 的 turf 小 ⇒ 消费者偏好更集中 ⇒ B 的 $p_B$ 更“贴近”其老客愿付价，收割更有效。
* 另外 B 是 **second mover advantage**：它看到 A 的价格再调自己的策略，天然更占便宜（标准的 price-setting sequential game 结论）。

这条结果对“反垄断直觉”挺挑衅：**大厂并不一定靠 history-based pricing 更赚钱，小厂反而可能更赚**。

---

### 4.2 市场份额（allocation）结果：dominant firm 反而被打到很小

论文在第 8 页给出 A 的均衡市场份额表达（Fig. 中对应 Proposition 2 的直观支撑）：

* weak dominance 下
  $$
  q_A^w=\frac{3+(1-2k)\alpha}{8}.
  \tag{15}
  $$

* strong dominance 下，论文式子里出现了一个看起来像排版笔误的 $x_U^w$（见第 8 页公式 (16)），但利用 strong dominance 下 $p_A^s=\tilde p_A^s$ 可直接推出 identified 与 unidentified 的切换点一致，从而 A 的总份额简化为
  $$
  q_A^s=x_A^s=x_U^s=\frac{1+2k}{8},
  $$
  与 $\alpha$ 无关。

无论哪种结构，A 的市场份额都远小于它“继承的” $k$（$k\ge 1/2$），这从运营视角就是：**客户历史的优势并不等于现期市场份额优势**，尤其当对手能用折扣精准挖角时。

---

### 4.3 Proposition 3：信息完整度 $\alpha$ 对利润的影响是非单调的

论文 **Proposition 3** 总结了一个很“OM-friendly”的结论：数据能力不是越强越好，存在 U-shape 或 monotone 的区域划分。

* Firm A 利润对 $\alpha$：

  * 当 $k$ 很小（接近对称）或很大（极不对称）时，$\pi_A$ 随 $\alpha$ 上升而下降
  * 当 $k$ 中间值时，$\pi_A(\alpha)$ 呈 U-shape（中等 $\alpha$ 最惨）

* Firm B 利润对 $\alpha$：

  * 小 $k$（接近对称）时随 $\alpha$ 下降
  * 大 $k$（高度不对称）时随 $\alpha$ 上升
  * 中间区域 U-shape

**统一机制解释：两股力量在打架**

1. **收割效应（Harvesting effect）**：$\alpha$ 上升意味着“能识别并高价收割的老客比例”上升，推高 $p_j$ 这块收益。
2. **竞争效应（Competition effect）**：$\alpha$ 上升意味着市场里“信息更透明”，poaching 更精准/更激烈，$\tilde p$ 竞争更凶，压低利润。

哪股力更强取决于 $k$：

* 当市场接近对称，竞争效应 dominates ⇒ $\alpha$ 越高越惨
* 当市场高度不对称，小 firm 的 poaching 优势更明显，且 dominant firm 在 strong dominance 下不挖角，小 firm 更能从提升 $\alpha$ 中获益

---

### 4.4 Fig.4 & Fig.5：利润曲线与“结构切换导致的不连续”

论文 Fig.4（第 9 页）非常关键，它说明：

* **Firm B 的利润对 $\alpha$ 可能出现跳跃式下降（discontinuity）**
* 原因：市场结构由 A 选择，当 $\alpha$ 增加到让 A 从 strong dominance 切换到 weak dominance 时，A 开始挖角，B 市场份额会“突然掉一截”。

这在运营上很像：当数据能力提升到某个临界点，竞争格局会突然从“单边进攻”变成“双边价格战”。

Fig.5（第 10 页）展示 A 的利润对 $\alpha$ 的几种典型形状（$k=0.52,0.57,0.6,0.8$）：

* 很多情况下，A 在 $\alpha=0$（完全不能识别，等价于 uniform pricing）反而利润最高
* 这就是“数据越多利润越高”的经典直觉在竞争环境下被打脸的地方：**数据让你能更精准收割，也让对手更精准挖你**。

---

## 5. 福利分析与管理/政策启示 (Main Results & Managerial Insights)

### 5.1 Proposition 5：社会福利 $SW$ 随 $\alpha$ 单调下降，但消费者剩余 $CS$ 不一定

论文的 welfare 结论很硬：

* **社会福利（消费者剩余 + 行业利润）在 weak 与 strong dominance 下都随 $\alpha$ 上升而下降**
  ⇒ 从 $SW$ 角度看，最优是 $\alpha=0$（完全不允许识别/歧视）

在 strong dominance 下，论文给出一个很简洁的 $SW$ 表达式（第 11 页）：

$$
SW^s=\pi_A^s+\pi_B^s+CS^s
=

\frac{64v-t\Big(17+4\alpha(1-k)-4\alpha^2(k-1)^2\Big)}{64},
$$
显然随 $\alpha$ 上升而下降。

但消费者剩余 $CS$ 的结论更微妙：

* 在 weak dominance：$CS^w$ 对 $\alpha$ 是 **非单调**，依赖 $k$（论文给出区间阈值：接近对称时递增，中间时倒 U，较不对称时递减）
* 在 strong dominance：$CS^s$ 随 $\alpha$ 上升而上升（更多信息 ⇒ 竞争更激烈 ⇒ 价格下降）

最终形成一个政策 trade-off：

> **想最大化社会福利**：倾向压低 $\alpha$（甚至到 0）
> **想最大化消费者剩余**：很多场景下反而要提高 $\alpha$（甚至到 1），但取决于市场份额不对称程度

这对监管很现实：隐私保护（降低 $\alpha$）并不一定“保护消费者钱包”，可能只是提高行业利润/总福利结构中的某一部分。

---

### 5.2 机制揭示：相对 benchmark，模型揭示的新 trade-off

把两个 benchmark 放在一起看就清晰了：

* **$\alpha=0$（uniform pricing）**：没有历史识别能力 ⇒ 没有“折扣误伤”的问题 ⇒ 竞争回到标准 Hotelling 价格竞争。
* **$\alpha=1$（perfect history-based discrimination）**：不存在“未识别老客” ⇒ $\tilde p$ 真正只用于 poaching ⇒ 结论会非常锋利，但也更脆弱。

本文的核心揭示在于：当 $\alpha\in(0,1)$ 时，$\tilde p$ 必须同时服务两件事：

1. 抢对手客户（poaching）
2. 给“识别不到的自己老客”也让利（误伤）

于是出现新的 trade-off：

* 想 poach ⇒ 必须降 $\tilde p$
* 但 $\tilde p$ 降得越多，误伤越大，尤其当你 inherited share 大（$k$ 大）时
* 所以 dominant firm 可能选择“不 poach”，转向 uniform pricing（strong dominance）

这就是一个标准的 OM 机制：**资源（折扣）投入到 acquisition 会对 retention 收割造成外部性，而外部性的规模与运营规模（market share）正相关**。

---

### 5.3 管理建议：站在企业与监管者视角

#### 对 dominant firm（大厂/ incumbent）

1. **别把“更多数据”当成单调利好**：当你规模大、$\alpha$ 不够高时，给未知客的折扣会大量“漏给”老客，利润可能下降。
2. **在 strong dominance 区域，uniform pricing 可能是理性策略**：不是你不会做 discrimination，而是做了会自残。
3. **技术栈的战略意义**：如果你能从 first mover 变成 second mover（算法跟随/实时调价），可能会改变均衡优势（文章的扩展讨论了顺序变化的影响）。

#### 对 small firm（小厂/ entrant）

1. **poaching 的 ROI 可能更高**：因为你的 turf 更集中，定价更贴近愿付价，且在 sequential 下 second mover advantage 强。
2. **提高识别能力的收益依赖市场结构**：在高度不对称市场中，提高 $\alpha$ 可能让你更能从 identified 老客中提价获利；但在接近对称市场里，提高 $\alpha$ 可能只是把自己拖进更凶的价格战。

#### 对监管者（隐私/竞争政策）

1. **“隐私保护=消费者福利提升”并非必然**：降低 $\alpha$ 可能提高总福利但伤害消费者剩余，或者反之。
2. **政策要看市场集中度（$k$）**：同一条数据规则在“接近对称市场”和“高度不对称市场”可能方向相反。
3. **警惕 perfect information 的政策推论**：论文在 simultaneous game 的讨论强调：$\alpha=1$ 是 knife-edge，很多结论对 $\alpha<1$ 不稳健。

---

### 5.4 图表复现：如何自己复刻 Fig.3–Fig.5 的关键逻辑（给博士生的“可操作版本”）

下面是一段最小化的复现思路（不依赖 Online Appendix）：

* 用上文的 $k_1(\alpha)$ 二次方程形式（由 (13) 推出）来画 Fig.3 的边界
* 对给定 $(\alpha,k)$ 判断处于 weak 或 strong dominance
* 用闭式价格 (5)–(8) 或 (10)–(12) 计算利润并画 Fig.4/5

```python
import numpy as np
import matplotlib.pyplot as plt

def k1(alpha):
    # coefficients from Eq.(13) numerator: A k^2 + B k + C = 0
    A = 8*alpha**2*(1+alpha)
    B = 8*(-2*alpha**3 + alpha**2 + 4*alpha - 6)
    C = 8*alpha**3 - 17*alpha**2 + 18
    D = B**2 - 4*A*C
    if D < 0:
        return 0.5
    root_small = (-B - np.sqrt(D))/(2*A)
    root_large = (-B + np.sqrt(D))/(2*A)
    # pick the economically relevant root in [0.5,1]
    candidates = [r for r in [root_small, root_large] if 0.5 <= r <= 1.0]
    return candidates[0] if candidates else 0.5

def prices_weak(alpha, k, t=1.0):
    pA = t*(6-4*alpha-(1-2*k)*alpha**2)/(2*(2-alpha**2))
    ptA = t*(6-4*alpha*(1+k)+alpha**2)/(2*(2-alpha**2))
    pB = t*(10-4*alpha*(1+k)-alpha**2)/(4*(2-alpha**2))
    ptB = t*(10-4*alpha*(3-k)-alpha**2*(1-4*k)+2*alpha**3*(1-k))/(4*(2-alpha**2))
    return pA, ptA, pB, ptB

def prices_strong(alpha, k, t=1.0):
    pA = t*(3-2*alpha*(1-k))/2
    ptA = pA
    pB = t*(1-2*alpha*(1-k)+4*k)/2
    ptB = t*(3-4*alpha*(1-k)+2*k)/4
    return pA, ptA, pB, ptB

def demand_cutoffs(pA, ptA, pB, ptB, t=1.0):
    xA = (ptB - pA + t)/(2*t)
    xB = (pB - ptA + t)/(2*t)
    xU = (ptB - ptA + t)/(2*t)
    return xA, xB, xU

def profits(alpha, k, regime, t=1.0):
    if regime == "weak":
        pA, ptA, pB, ptB = prices_weak(alpha, k, t)
    else:
        pA, ptA, pB, ptB = prices_strong(alpha, k, t)
    xA, xB, xU = demand_cutoffs(pA, ptA, pB, ptB, t)

    # profit formulas Eq.(1)(2)
    piA = pA*alpha*min(xA, k) + ptA*(alpha*max(0.0, xB-k) + (1-alpha)*xU)
    piB = pB*alpha*min(1-k, 1-xB) + ptB*(alpha*max(0.0, k-xA) + (1-alpha)*(1-xU))
    return piA, piB

# Example: replicate Fig.3 boundary
alphas = np.linspace(0.05, 1.0, 300)
k_boundary = np.array([k1(a) for a in alphas])
plt.figure()
plt.plot(alphas, k_boundary)
plt.ylim(0.5, 0.8)
plt.xlabel("alpha")
plt.ylabel("k1(alpha)")
plt.title("Sequential game: boundary between weak and strong dominance")
plt.show()
```

---

## 6. 你的犀利评论 (Reviewer's Critique)

下面我会用“Senior Editor 视角”来挑刺（带点狠，但有用）。

### 6.1 我认可的亮点（优点）

1. **把“信息不完美”建模成 missing-but-correct（而不是 noisy misclassification）非常干净**
   这让模型更贴近 cookie/会员覆盖不全的现实，而且避免了信号结构带来的额外复杂性。
2. **非对称市场份额 + 序贯定价 + 不完美识别** 的三重交互是新颖且重要的
   很多既有结论确实是靠“对称 + 完美信息”撑起来的，这篇文章把这些结论的脆弱性揭示得很清楚。
3. **knife-edge 讨论很到位**
   simultaneous 版本里 $\alpha=1$ 的特例不稳健（Fig.7），这个提醒对后续研究非常关键：很多政策结论不能从 perfect info 直接外推。

### 6.2 我会卡住作者的地方（缺点/限制）

1. **$\alpha$ 是外生的**
   现实里企业会投资数据能力、会买 third-party data、会设计激励让用户登录/绑定身份。把 $\alpha$ 外生会弱化一个很重要的 OM/IO 问题：**数据能力投资与定价策略的联动**。
2. **消费者隐私选择是外生且与偏好无关**
   文中有提到 opt-out 与偏好独立是合理的，但从机制设计/实证角度看，偏好与隐私态度往往相关（高价值客户更敏感或更愿意换身份），这会改变“误伤”的结构。
3. **$\tilde p$ 对所有 unidentified 一口价：现实中企业可以做概率推断**
   现在的定价系统常用 ML 做“这人像不像老客”的概率评分，即便没有 deterministic ID，也能做软识别。这会把模型从“二分信息”推进到“贝叶斯分层”，结论可能更丰富也更难。
4. **Hotelling + full coverage 的经典限制**
   现实里价格歧视往往伴随需求扩张/收缩（outside option 不为 0），并且成本/容量约束可能与 pricing 联动（典型 OM 的 capacity pricing）。本模型忽略这些会让一些 welfare 结论偏向“竞争越激烈价格越低”这一条线。
5. **序贯定价的制度化假设需要更多 empirical grounding**
   作者给了很合理的叙事（更新频率、算法），但如果能用行业事实（比如不同 firm 的价格更新间隔分布）来支持“谁先动”的设定，会更有说服力。

### 6.3 未来方向（这篇文章最适合长出什么分支？）

1. **Endogenize $\alpha$：数据投资 + 隐私监管**
   让 firms 选择数据投资（决定 $\alpha$），监管者设定隐私规则或合规成本，形成一个两阶段博弈。你会得到真正 OM 味道的“capability choice → pricing equilibrium”。
2. **动态模型：两期/多期 history accumulation**
   现在的 purchase history 是外生 turf。把 turf 内生化（由上一期竞争结果产生）会更贴近 “acquisition today → harvest tomorrow” 的经典框架。
3. **引入 misclassification（noisy signals）并与 missingness 结合**
   现实更像：既有漏识别，也有误识别。两者的交互会改变 poaching 的效率与误伤结构。
4. **容量/履约（Operations）约束**
   很多行业（物流、云服务、医疗）存在 capacity bottleneck。折扣挖角可能带来拥堵成本或服务失败风险，这会把 welfare 与利润结论改写成更 OM 的版本。
5. **实证检验路径**
   可以用 GDPR 前后、或 cookie 规则变化作为 quasi-experiment，检验：

   * 市场份额越不对称的行业，价格歧视策略是否更偏向“只有小 firm 在打折挖角”？
   * $\alpha$ 的变化是否引发定价策略的结构性切换（对应 Fig.4 的 discontinuity）？

---

## 7. One More Thing：我认为最值得分享的“灵光一现/数学技巧”

我最喜欢的是 strong dominance 那一段的“**约束绑定**”操作：

* 不是先猜一个复杂的 demand 区间再硬解，而是直接意识到：在 strong dominance 下，B 作为 second mover 会把 $p_B$ 设到刚好阻止 A 挖走边界消费者 $x=k$，即让 $x_B=k$ **变成 binding constraint**。
* 这一下把 $p_B$ 从一个“自由选择变量”变成了由 $\tilde p_A$ 决定的函数 $p_B^s=\tilde p_A+t(2k-1)$，问题立刻降维，后面的闭式解顺得像拉链。

从方法论角度，这是一个很实用的套路：

> **在不等式约束定义市场结构的模型里，第二阶段玩家常常会把“最关键的结构约束”推到等式边界上。识别哪个约束会绑定，往往比硬算更重要。**

---

<!-- **（完）**
这份笔记把论文的基准模型与关键扩展都按“可复盘推导”的方式拆开了：你可以直接按公式把均衡价格、cutoffs、结构阈值与利润/福利关系完整重建出来。下一步如果要更进一步（写 referee report 或做扩展），最自然的落点就是把 $\alpha$ 内生化并引入动态 history accumulation——那会把这篇 IO/Info Econ 论文真正接到 OM 的主干上。 -->

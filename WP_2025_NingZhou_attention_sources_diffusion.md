# Managing Consumer Attention to Diverse Information Sources in Product Diffusion（深度解析）

**论文**：*Managing Consumer Attention to Diverse Information Sources in Product Diffusion*  
**作者**：Z. Eddie Ning, Zihao Zhou  
**版本**：Working Paper，July 28, 2025  
**关键词**：observational learning；consumer search；allocation of attention；dynamic pricing；herding；information bias  

---

## 0. 先给你一张“心智地图”（读完就能复盘推导的那种）

这篇论文做的事情可以浓缩成一句话：

> 在“观察他人购买行为”的社会学习（observational learning）里，消费者还会做**信息搜索**，而且会在“偏正（PL）”和“偏负（NL）”两类信息源之间分配注意力；厂商用**动态定价**去操控这种注意力分配，从而改变市场学习路径与 herding 的发生。

它的核心机制是一个非常“反直觉但很合理”的三角关系：

- **价格**决定消费者“默认动作”（默认买 vs 默认不买）；  
- 默认动作决定消费者“愿意为哪一种真相付费”（买的人更在意“别买”的证据；不买的人更在意“可以买”的证据）；  
- 厂商通过价格把消费者推到不同默认动作区间，从而让消费者去搜 **PL** 或 **NL**，让公共信念 $x_t$ 朝上或朝下演化，甚至在边界处“来回拉扯”以避免 herding。

---

## 1. 研究背景与动机（Motivation）

### 1.1 实践痛点：现实市场里到底卡在哪儿？

新产品扩散（product diffusion）里，消费者常常同时依赖两类信息：

1. **观察学习（observational learning）**：看别人买没买、销量高不高、早期 adopters 多不多。  
2. **主动搜索（direct information search）**：看评测、读媒体、刷测评视频、问朋友、试驾/试用。

在“信息爆炸”的当下，搜索还多了一层复杂性：**信息源本身有立场与倾向**。有些渠道天然偏正（positive-leaning, PL），有些偏负（negative-leaning, NL）；更糟的是，它们往往都“看起来”像信息，但在统计意义上是**有偏实验（biased statistical experiment）**。

行业层面的难题就来了：

- 产品口碑形成早期，市场容易出现 **informational cascades / herding**：大家跟风买或跟风不买，后续消费者不再搜索，导致“错得很稳定”。  
- 厂商常见直觉是“只要放大正面信息源、压制负面信息源”，但现实里负面信息源很难彻底消失（竞品、媒体生态、KOL 立场等）。  
- 更关键：**厂商能不能利用价格去干预消费者到底去看谁**？如果能，什么时候竟然会“主动引导消费者去看负面信息”？这听起来像自残，但论文说：有时这反而更赚钱、更有效率。

### 1.2 理论缺口：文献忽略了什么？

主流 observational learning 文献非常重视“看前人行为导致 herding”这一基本病理，但通常把“私有信息”建模成：

- exogenous 的 signal（每个消费者自动拿到一个私信号），或
- 消费者只决定“搜不搜、搜多久/精度”（但信息结构固定）。

这篇论文补的洞更细更锋利：

- **信息结构是多源且有倾向的**：消费者不只决定是否搜索，还决定搜 PL 还是 NL。  
- **厂商能通过动态定价影响注意力分配**：价格不仅影响买不买，也影响消费者是否搜索、搜哪类源。  
- **多源倾向与社会学习交互**：某些信息源的存在不仅不一定伤害厂商，反而可能提升利润与社会学习效率。

### 1.3 核心贡献（Significance）

**理论贡献（OM/Marketing Science 视角）**  
- 把“attention allocation（注意力分配）”内生化地嵌入 observational learning，并让厂商的动态定价成为影响注意力的工具。  
- 证明信息多样性（尤其包含 NL 源）在特定条件下可以：  
  1) 提高厂商利润；  
  2) 让市场学习更完整（减少错误 herding）。  

**实践贡献（管理启示很能打）**  
- 新品上市不必追求“信息环境全是正向”的洁癖。某些情况下：  
  - 邀请更挑剔的评测者、允许更负面的比较广告，可能反而让扩散更顺、长期更赚。  
- 动态定价不仅是“需求管理”，还是“学习路径管理”：用价格去让消费者持续搜索，避免市场太早锁死在错误信念上。

---

## 2. 模型设定与假设（Model Setup & Assumptions）

### 2.1 符号体系（Notation）

| 符号 | 含义 |
|---|---|
| $\omega \in \{0,1\}$ | 产品真实质量：$1$ 高质量，$0$ 低质量 |
| $v_h>0,\, v_l<0$ | 已知质量时消费者对产品的效用（相对保留效用） |
| $x_t \in [0,1]$ | 时间 $t$ 的公共信念：$P(\omega=1\mid \text{public history})$ |
| $v(x):=x v_h+(1-x)v_l$ | 信念为 $x$ 时消费者对产品的期望价值 |
| $p_t$ | 厂商在时间 $t$ 设定的价格（边际成本归一为 0） |
| $c$ | 搜索的单位时间（flow）成本 |
| $\Delta t$ | 一次搜索持续时间（随后取 $\Delta t \to 0$ 进入连续时间） |
| $\lambda$ | “反倾向”真相信号的到达率（Poisson arrival rate） |
| $r$ | 厂商贴现率 |
| $\mu$ | break-even belief：$v(\mu)=0$ |
| $\underline{x},\, \bar{x}$ | 消费者可被激励去搜索的信念区间边界（由条件 (3) 决定） |
| $x^*_{pl}, x^*_{nl}$ | 单一信息源（仅 PL / 仅 NL）benchmark 下厂商的阈值信念 |
| $x^*$ | 两类信息源都存在时（主模型）厂商切换激励 NL vs PL 搜索的阈值 |
| $U_a(x)$ | 厂商在信念 $x$ 处采取“anchoring（交替激励两类搜索以维持信念）”的价值 |

> 论文也给了一个符号表（Table 2），上面基本覆盖了核心记号。

---

### 2.2 Players, Sequence of Events, Information Structure

**玩家（Players）**  
- 单一厂商（monopolist）  
- 连续到达、短寿命（short-lived）的消费者流：用到达时间 $t\in\mathbb{R}_+$ 索引消费者。

**时序（Sequence of Events, continuous-time limit）**  
在每个时刻 $t$：

1. 厂商观察公共信念 $X_t$（由历史价格与购买行为共同决定），选择价格 $p_t=p(X_t)$（Markovian pricing）。  
2. 消费者观察到公共历史（等价于观察 $X_t$）与当前价格 $p_t$，选择三类行动之一：  
   - 不买（payoff 0）；  
   - 不搜直接买；  
   - 先搜 $\Delta t$ 再决定买不买，同时选择搜哪类信息源（PL 或 NL）。

**信息结构（Information Structure）**  
- 产品质量 $\omega$ 对所有人未知，先验 $x_0$ 共同知识。  
- 关键是：消费者的“搜索信号”来自**有倾向的信息源**，且倾向结构被建模为“真相只在反倾向信号里爆发”。

---

### 2.3 消费者效用与默认决策

消费者买入价格 $p$ 后（相对保留效用）收益：

$$
u(\omega,p)=\omega v_h+(1-\omega)v_l-p.
$$

给定信念 $x$，不搜索直接买的期望收益为 $v(x)-p$，因此：

- 若 $v(x)\ge p$，默认动作是 **买**；  
- 若 $v(x)< p$，默认动作是 **不买**。

这个“默认动作”在后面非常关键：它决定消费者搜索时“只在意哪些信号”。

---

### 2.4 信息源：PL vs NL（Poisson 化的 biased experiments）

两类信息源都只给二元信号：positive 或 negative，但它们“几乎总是输出与倾向一致的信号”。论文用小 $\Delta t$ 下的 Poisson 到达去刻画“反倾向信号”的稀有到达：

#### （1）Positive-leaning（PL）源  
- 若 $\omega=1$：总是 positive  
- 若 $\omega=0$：以概率 $\lambda \Delta t$ 给 negative（这个 negative **完全揭示** $\omega=0$）

因此，**PL 源的 negative 信号是“真相炸弹”（truth-revealing）**。

#### （2）Negative-leaning（NL）源  
- 若 $\omega=0$：总是 negative  
- 若 $\omega=1$：以概率 $\lambda \Delta t$ 给 positive（该 positive **完全揭示** $\omega=1$）

因此，**NL 源的 positive 信号是 truth-revealing**。

> 这种建模的好处是：连续时间里，信念演化可被写成“平滑 drift + 偶尔 jump to 0/1”的过程，数学上非常干净。

---

### 2.5 搜索激励约束：价格如何决定“搜哪一类”？

这一段是论文的第一个关键“齿轮”：**价格 $\to$ 默认动作 $\to$ 哪类搜索有价值**。

#### 2.5.1 搜 PL：只有当默认动作是“买”才有价值

直觉：如果你本来就不买，那么 PL 源的 negative（揭示低质量）只会让你更不买，并不改变行动；positive 又几乎不更新信念。所以搜 PL 的价值来自：当你默认买时，万一出现 negative，你可以及时止损。

论文推导得到：当默认动作买（即 $p\le v(x)$），搜 PL 值得做当且仅当存在价格区间满足

$$
p \ge v_l+\frac{c}{(1-x)\lambda}. \tag{2}
$$

结合默认买的要求 $p\le v(x)$，可被激励去搜 PL 的价格区间是：

$$
v_l+\frac{c}{(1-x)\lambda} \le p \le v(x).
$$

#### 2.5.2 搜 NL：只有当默认动作是“不买”才有价值

对称直觉：如果你本来就买，那么 NL 源的 positive（揭示高质量）不会改变行动；negative 又几乎没信息。所以搜 NL 的价值来自：当你默认不买时，万一出现 positive，你从“不买”跳到“买”，捡到宝。

条件为（当默认不买，即 $p\ge v(x)$）：

$$
p \le v_h-\frac{c}{x\lambda}. \tag{4}
$$

因此可被激励去搜 NL 的价格区间是：

$$
v(x) \le p \le v_h-\frac{c}{x\lambda}.
$$

#### 2.5.3 搜索“可行区间”：[ $\underline{x}$, $\bar{x}$ ]

两个区间非空需要同一个条件（论文式 (3)）：

$$
\lambda x(1-x)(v_h-v_l)\ge c. \tag{3}
$$

定义 $\underline{x}$ 与 $\bar{x}$ 为使 (3) 成立的最小/最大信念，且 $\underline{x}+\bar{x}=1$。论文进一步做了参数假设 $\lambda (v_h-v_l)>4c$，保证搜索区间不为空，且 $\underline{x}<1/2<\bar{x}$。

---

### 2.6 厂商目标函数（Profit Function）与 Markov 定价

边际成本归一为 0。厂商贴现利润：

$$
\max_{p(\cdot)}\; \mathbb{E}\left[\int_0^\infty e^{-rt}\, a_t\, p(X_t)\, dt\right],
$$

其中 $a_t\in\{0,1\}$ 表示时刻 $t$ 的消费者是否购买（由其搜索结果与最优决策决定）。策略限制为 Markov：$p_t=p(X_t)$。

---

### 2.7 关键假设（以及为什么合理）

1. **短寿命消费者、连续到达**：把“产品扩散的时间连续性”用连续时间极限表达出来，便于把学习路径写成受控扩散/跳跃过程。  
2. **信息源倾向被建模为“反倾向信号稀有但完全揭示”**：这不是说现实里真相一定完全揭示，而是抓住了一个经验事实：  
   - 来自“本来就偏正”的渠道的一条负评，往往更有信息含量；  
   - 来自“本来就偏负”的渠道的一条好评，也更有信息含量。  
3. **消费者搜索时只关心能改变行动的信号**：这其实是一个决策相关（decision-relevant）的 rational inattention 味道：你不会为“不会改变决策的噪声”付费。  
4. **厂商可用价格影响“搜不搜 / 搜哪类”**：因为价格改变默认动作区间，进而改变哪类信号具有 option value。论文还用一个技术性说明（footnote）：在 $p=v(x)$ 处，可通过 $\pm \epsilon$ 的微调排除某类搜索动机，从而等价于“厂商能选让消费者搜哪类”。

---

## 3. 分析与求解（Analysis & Solution）

这一部分按论文结构走：先做 benchmark（只有一种信息源），再做主模型（两种信息源并存），最后讨论 neutral source 扩展。

---

### 3.1 Benchmark：只有 PL 信息源（Section 4.1）

**问题结构**  
当只能搜 PL 时，厂商在 $x\in[\underline{x},\bar{x}]$ 面临一个停止问题（optimal stopping flavor）：

- **继续激励搜索**：给出价格 $p=v(x)$ 让消费者搜 PL（且几乎一定买），公共信念在“未出现真相负信号”时逐步上升；  
- **停止激励搜索**：让消费者不搜并形成 herding（要么都买，要么都不买），从而锁死学习。

**关键结果：Proposition 1（阈值策略）**  
当 $\mu \in (\underline{x},\bar{x})$ 时存在阈值 $x^*_{pl}\in[\underline{x},\mu)$：

- 若 $x<x^*_{pl}$：厂商宁可让消费者“不搜也不买”（直接熄火）。  
- 若 $x\ge x^*_{pl}$：厂商激励搜 PL（价格 $p=v(x)$），直到出现负信号（揭示 $\omega=0$）或信念上升到 $\bar{x}$。

**经济学直觉（Economic Intuition）**  
- 激励 PL 搜索相当于让消费者承担“买了但可能被负信号打脸”的风险；  
- 但厂商的好处是：只要没出现负信号，信念上升、未来可提价；  
- 甚至当 $x$ 还略低于 $\mu$（即当前卖是亏的），厂商也愿意“赔本赚吆喝”，赌一个未来信念上升后的盈利区间（图 2 的直观）。

**学习效率：Corollary 1**  
只有 PL 时：

- 存在参数使得某些 $x$ 下学习不 efficient（即消费者本可被激励去搜，但厂商不愿意）。  
- 更强：对任意 $x\in[\underline{x},\bar{x}]$，学习都不 asymptotically complete，且 herding 以正概率发生。

**图表解释**  
- **Figure 1**：展示 $x$ 轴（公共信念）上三段区域：低信念直接不卖；中间激励 PL 搜索；到达 $\bar{x}$ 后只能“买但不搜”形成 herding。  
- **Figure 3**：两条样本价格路径：  
  - 没有负信号时价格随信念上升而上升，直到触达 $\bar{x}$ 触发 herding；  
  - 若负信号提前到达，则产品被揭示为低质量，厂商退出（价格路径断崖）。

---

### 3.2 Benchmark：只有 NL 信息源（Supplemental Appendix B）

对称结构：激励 NL 搜索时，消费者默认不买，除非出现 positive（揭示 $\omega=1$），一旦出现则进入“成功后高价永续”的路径。

**关键结果：Proposition B.1（同样是阈值）**  
存在 $x^*_{nl}\in(\mu,\bar{x}]$：

- $x\le x^*_{nl}$：激励搜 NL；  
- $x> x^*_{nl}$：让消费者直接买不搜（herding）。

**直觉**  
当信念不高时，直接卖赚不到钱，激励 NL 搜索是“用低销量换一个跳到真相高质量的机会”；即便 $x$ 略高于 $\mu$（当前卖是赚的），厂商也可能放弃短期利润去赌“正信号来了就能永远卖 $v_h$”。

---

### 3.3 主模型：PL 与 NL 都存在（Section 5）

这才是论文最有意思的部分：两种信息源并存后，厂商多了一个控制手段——**切换消费者注意力方向**。

#### 3.3.1 关键新概念：Anchoring（把公共信念钉在边界）

当 $x$ 达到上边界 $\bar{x}$ 或下边界 $\underline{x}$ 时，继续激励同一类搜索变得不可行（因为 (3) 失败，消费者不愿再搜）。这时厂商可以：

- 直接停止搜索激励，进入 herding；或
- **交替激励**：在很短的两个区间里先让一位搜 NL、下一位搜 PL，使信念向下 drift 与向上 drift 在极限里抵消，让 $x$ 近似保持不变，这叫 **anchoring**。

anchoring 在数学上等价于 Che and Mierendorff (2019) 里 long-lived agent 的“分配注意力以维持信念”的 Poisson 注意力分配，只不过这里的“注意力分配”是厂商通过价格诱导出来的“群体层面分配”。

anchoring 的价值函数（论文式 (5)）：

$$
U_a(x)=\frac{(\lambda+r)x v_h+r(1-x)v_l}{r(\lambda+2r)}. \tag{5}
$$

> 这个式子很漂亮：分子像“加权的高/低质量现金流”，分母像“有效贴现 + 两次搜索阶段”的调节项。

#### 3.3.2 Lemma 1：在内部信念点 anchoring 永远不最优

对任意 $x\in(\underline{x},\bar{x})$，anchoring 被严格支配：  
- 若 $x>\mu$，持续激励 PL 搜索比 anchoring 好；  
- 若 $x<\mu$，持续激励 NL 搜索比 anchoring 好。

直觉非常经济学：在内部点，厂商已经能“纯粹地”用一种搜索把信念朝有利方向推移；anchoring 强迫你也激励另一种搜索，等于白付成本（要么亏钱卖，要么牺牲销量），不划算。

因此 anchoring 只可能在 $\underline{x}$ 和 $\bar{x}$ 这种“不得不换挡”的边界点出现。

#### 3.3.3 Lemma 2：anchoring 何时优于 herding？

Lemma 2 给出两个比较：

- $U_a(x)\ge 0$ 的条件（anchoring 至少不比立即熄火差）；  
- $U_a(x)\ge v(x)/r$ 的条件（anchoring 至少不比在该点直接让消费者 buy-without-search 的永续现金流差）。

当 $\mu\in(\underline{x},\bar{x})$ 时，论文把“在两端都愿意 anchoring”的条件写成（式 (6)）：

$$
\frac{r\bar{x}}{(\lambda+r)\underline{x}}\le -\frac{v_h}{v_l}\le \frac{(\lambda+r)\bar{x}}{r\underline{x}}. \tag{6}
$$

直觉：$-v_h/v_l$（也等价于 $\mu$ 的位置）刻画“成功时赚多少 vs 失败时多糟”。成功收益越大，维持 NL 搜索激励的价值越高；失败损失越大，维持 PL 搜索激励的价值越高。只要这个比率落在区间里，两端都值得用 anchoring 抵抗 herding。

#### 3.3.4 Theorem 1：最优动态定价 = “在 $x^*$ 两侧激励不同倾向的搜索”

定义两个 continuation 值：

- $U_{na}(x)$：持续激励 NL 搜索，直到正信号到达（跳到 $1$）或信念降到 $\underline{x}$，然后在边界处选择“anchoring 或停止”。  
- $U_{pa}(x)$：持续激励 PL 搜索，直到负信号到达（跳到 $0$）或信念升到 $\bar{x}$，然后在边界处选择“anchoring 或 herding（buy w/o search）”。

Theorem 1 给出：

$$
U(x)=\max\{U_{na}(x),U_{pa}(x)\},
$$

并且存在一个阈值 $x^*$，使得：

- $x<x^*$：激励 NL 搜索；  
- $x>x^*$：激励 PL 搜索；  
- 在 $x=\underline{x},\bar{x}$，根据 Lemma 2 决定是否 anchoring。

**图表解释：Figure 4 & Figure 5**  
- **Figure 4** 把 $x$ 轴上的区域标得很清楚：低信念段厂商通过价格让消费者搜 NL；高信念段让消费者搜 PL；在边界处可以出现“搜两类（anchoring）”以避免 herding。  
- **Figure 5** 展示两条 continuation payoff 曲线（激励 NL vs 激励 PL），交点就是 $x^*$：  
  - 曲线在上者对应更优策略。

---

## 4. 比较静态（Comparative Statics）

论文用数值方式讨论三个关键参数：搜索成本 $c$、贴现率 $r$、信息到达率 $\lambda$。

### 4.1 搜索成本 $c$ 上升

- (3) 更难满足，搜索可行区间 $[\underline{x},\bar{x}]$ **收缩**；  
- 市场更早进入 herding（因为厂商更难持续激励搜索）；  
- 直觉：信息变贵，大家更愿意“看风向”，而不是自己去证伪/证真。

### 4.2 贴现率 $r$ 上升（厂商更短视）

- 消费者决策不受 $r$ 影响，所以 $\underline{x},\bar{x}$ 不变；  
- $x^*$ 向 $\mu$ 靠近：厂商更看重短期现金流，更接近“myopic rule”（$x>\mu$ 偏好 PL，$x<\mu$ 偏好 NL）。

### 4.3 信息到达率 $\lambda$ 上升（信息更快、更有用）

- (3) 更易满足，$[\underline{x},\bar{x}]$ **扩张**；  
- herding 更不容易发生；  
- 直觉：真相更容易被揭示，厂商更愿意让消费者持续搜索（因为“等真相”更快，风险期更短）。

---

## 5. 主要结论与管理启示（Main Results & Managerial Insights）

### 5.1 机制揭示：与 benchmark 相比，新 trade-off 在哪？

**Benchmark（只有一种信息源）**  
厂商终究会被迫在某个点停止激励搜索，进入 herding，导致学习不完整。

**主模型（两种倾向并存）**  
厂商多了一个“换挡”工具：当信念逼近某个 herding 边界（$\underline{x}$ 或 $\bar{x}$）时，可以通过**切换激励的搜索倾向**把信念往回拉，让市场继续处在“愿意搜索”的区间内，直到 truth-revealing signal 到来。

这揭示了一个新的 trade-off：

- “让信念单边走向更有利的方向” vs “为了避免 herding 而主动制造反向 drift”。  
- 反直觉点：有时厂商会**主动引导 NL 搜索**，即使 PL 源存在；甚至负面信息源的存在可能让厂商利润更高。

### 5.2 管理建议（给管理者的可操作版本）

1. **把动态定价当作“学习路径控制器”**  
   - 高信念阶段：用略低于愿付价值的价格诱导消费者继续搜 PL（边买边学），逐步推高口碑与价格；  
   - 低信念阶段：用合适价格诱导消费者搜 NL（多数人不买），但一旦出现“反向好消息”，口碑可大跳跃，避免早期直接死亡。

2. **新品上市时不要只投喂“正向信息生态”**  
   - 邀请更挑剔、更苛刻的测评者并不总是坏事；  
   - 竞品的比较广告、媒体的批评，有时反而让市场学习更充分，从而减少“因为误判而停止扩散”的风险。

3. **政策含义（轻量但有趣）**  
   - 信息多样性可能提升市场效率：当厂商有能力通过价格让学习持续发生时，多源倾向减少错误 cascades。

### 5.3 图表再解读（把图变成机制）

- **Figure 4（策略分区图）**：不是在说“厂商喜欢好评/差评”，而是在说“厂商用价格把消费者推到不同默认动作，从而让消费者去找最能改变动作的真相信号”。  
- **Figure 7-9（阈值随参数变化）**：不是纯数学玩具，它们其实是告诉你：  
  - 信息更贵（$c$ 高）或更慢（$\lambda$ 低）时，市场更容易锁死；  
  - 厂商更短视（$r$ 高）时，策略更像“就地套利”，不太愿意做长期引导。

---

## 6. 你的犀利评论（Reviewer's Critique）

下面这段以 “严苛 Senior Editor” 的口吻来审：

### 6.1 优点（值得发表的地方）

- **机制新且干净**：把“注意力分配 + 观察学习 + 动态定价”三者放进一个可解析的动态框架，数学结构漂亮（Poisson + jump-to-truth）。  
- **反直觉结果有说服力**：负面信息源可能提高利润与学习效率，这在管理学/营销学里很抓人，也很容易讲给非技术读者听。  
- **与相关理论对话清晰**：对 Che and Mierendorff (2019) 的 attention allocation、以及 observational learning 的 herding 病理，都有明确增量。

### 6.2 模型限制（哪些假设可能过强？）

1. **“真相信号完全揭示”是强假设**  
   - PL 的 negative 一来就把 $\omega=0$ 揭示、NL 的 positive 一来就把 $\omega=1$ 揭示。现实里更多是“强信号但非完美”。  
   - 这会放大 jump 的戏剧性，使得“只靠行为可推断信号是否到达”的一对一映射更干净。

2. **厂商对“搜哪类源”有近乎完美的控制**  
   - 论文用 $p=v(x)$ 附近的 $\epsilon$ 论证做 tie-breaking，这在理论上可接受，但在现实中消费者的平台选择、社交推荐、算法分发可能让厂商控制力弱得多。

3. **消费者搜索时长外生、且每人只搜一个源**  
   - 现实里可以多源并行、也可以 endogenous intensity / stopping。  
   - 如果允许“同时看 PL 与 NL”，anchoring 可能在个体层面发生，而不需要厂商在群体层面交替。

4. **单一厂商、无竞争**  
   - NL 信息源在现实里往往来自竞品或媒体生态，背后是战略互动。把竞争者显式建模，可能会改变“负面信息是否能提高利润”的边界条件。

### 6.3 未来方向（可扩展的研究路线）

- **Endogenous media bias / strategic information sources**：让信息源也有目标函数（广告收入、声誉、受众选择），偏向程度内生化。  
- **竞争与比较广告**：双寡头动态定价 + 信息战（谁在制造 NL，谁在制造 PL）。  
- **消费者异质性**：不同 $c$（信息素养）、不同 $v_h,v_l$（偏好）、不同先验 $x_0$。  
- **平台与算法推荐**：厂商不仅用价格，还用投放影响信息源可达性，形成 price + information design 的组合拳。  
- **实证/结构估计**：用电商评论、媒体评测、价格路径与销量序列，检验“引导负面搜索是否减少早期错误熄火”。

---

## 7. One More Thing（最值得分享的灵光一现 / 数学技巧）

我认为最“灵光一现”的点不是某个复杂微分方程，而是一个非常聪明的**信息等价（information equivalence）**思路：

> 在观察学习里，后人只看到“前人买没买”，看不到“前人收到了什么具体信号”。于是，哪怕你给消费者更丰富的 neutral source，只要它不会改变“是否偏离默认动作”的统计结构，那么在公共信念演化上，它就等价于某个 biased source。

这在扩展部分体现得非常极致：

- 当消费者默认买时，他只在意“会让我不买”的负信号；neutral source 的额外正信息被行动层面“压缩掉”；  
- 当消费者默认不买时，他只在意“会让我买”的正信号；neutral source 的额外负信息同样被压缩掉；  
- 因此 neutral sources 在 observational learning 下可以被“重映射”为一个 arrival rate 调整后的 PL 或 NL 源（Proposition 4 的核心直觉）。

这是一种非常 OM 的思维：**系统里真正流通的不是信息本身，而是“决策可观察的统计充分量”。**

---

## 8. 附：复盘推导时的“最小必备公式清单”（便于你自己推一遍）

1. 价值函数：$v(x)=x v_h+(1-x)v_l$，break-even 信念：$\mu=-v_l/(v_h-v_l)$。  
2. 搜 PL 的价格窗口：$v_l+\frac{c}{(1-x)\lambda}\le p\le v(x)$。  
3. 搜 NL 的价格窗口：$v(x)\le p\le v_h-\frac{c}{x\lambda}$。  
4. 搜索可行条件：$\lambda x(1-x)(v_h-v_l)\ge c$，定义 $[\underline{x},\bar{x}]$。  
5. anchoring payoff：$U_a(x)=\frac{(\lambda+r)x v_h+r(1-x)v_l}{r(\lambda+2r)}$。  
6. “无 herding 的充分条件”（两端都愿意 anchoring）：$\frac{r\bar{x}}{(\lambda+r)\underline{x}}\le -\frac{v_h}{v_l}\le \frac{(\lambda+r)\bar{x}}{r\underline{x}}$。  

---

*End of note.*

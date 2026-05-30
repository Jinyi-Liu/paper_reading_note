# An Alternative Model of Brand Loyalty

**作者**：Xiaoyi (Sylvia) Gao（University of Auckland）; Vidyanand Choudhary（University of California, Irvine）  
**年份/期刊**：2026, *Information Systems Research*  
**论文类型**：理论建模；sequential-entry duopoly；Hotelling horizontal differentiation  
**关键词**：brand loyalty, preference shifts, switching costs, duopoly competition, product positioning, consumer welfare

## 1. 中文摘要

传统分析模型通常把品牌忠诚理解为一种“摩擦”：消费者换品牌会付出 switching costs，所以即便竞争者进入，老客户也不愿离开 incumbent。本文提出另一种忠诚机制：preference shifts。消费者使用某品牌之后，其理想点会向该品牌的产品特征移动，因此后续更偏好类似设计、界面、工作流或体验。这种忠诚不是“被锁住”，而是“真的更喜欢”。

论文构建了一个两期 sequential-entry Hotelling duopoly model：第 1 期只有 leader，第 2 期 follower 进入并选择位置，然后两家企业定价竞争。作者分别分析两类忠诚：一类是消费者偏好向 leader 移动，另一类是消费者换到 follower 时要承担 switching cost。核心结论是：两种忠诚都能带来客户留存，但它们对竞争、利润和福利的影响几乎相反。Switching costs 强化 incumbent advantage、提高行业利润、降低消费者剩余和社会福利；preference shifts 会使消费者偏好更集中，吸引 follower 向 leader 靠近，从而加剧价格竞争，压低企业利润，但可能提高消费者剩余和社会福利。

## 2. 论文速览

| 维度 | 内容 |
|:---|:---|
| 研究问题 | 品牌忠诚到底是因为消费者“被锁住”，还是因为消费者“偏好真的改变”？这两类机制对进入、定价、产品定位、利润和福利有何不同影响？ |
| 方法 | 两期 sequential-entry Hotelling duopoly。Leader 第 1 期垄断；第 2 期 follower 进入、选择位置，两家企业同时定价。 |
| 两种忠诚机制 | Preference shifts：使用后消费者理想点向 leader 移动。Switching costs：消费者偏好不变，但换到 follower 要支付成本 $s$。 |
| 核心发现 | Switching costs 缓和竞争、提高 incumbent 利润；preference shifts 会让 follower 更有动力靠近 leader，降低差异化，强化价格竞争。 |
| 反直觉结果 | 让消费者更喜欢你的设计，未必让你赚更多钱；如果竞争者能模仿或靠近你的设计，preference-shift loyalty 可能把市场推向更激烈的同质化竞争。 |
| 消费者与福利 | Switching costs 降低消费者剩余和社会福利；preference shifts 因降低 misfit costs 和价格，可能提高消费者剩余和社会福利。 |
| 管理含义 | 不能只看 retention rate。通过 lock-in 得到的忠诚和通过 product experience 得到的忠诚，会诱发完全不同的竞争反应。 |
| 政策含义 | 监管者不能把所有“stickiness”都当作有害 lock-in；需要区分消费者是被摩擦困住，还是偏好真的改变。 |

## 3. TL;DR

这篇文章说的是：品牌忠诚不只有一种。消费者留下来，可能是因为换品牌太麻烦，也可能是因为用过之后真的更喜欢原品牌的设计。

这两个机制表面上都提高留存，但经济后果相反：switching costs 保护 incumbent、伤害消费者；preference shifts 反而可能吸引竞争者模仿 leader、打价格战，伤害企业利润但提高消费者和社会福利。

## 4. One More Thing：最值得分享的洞察

最妙的一点是，本文把“品牌做得太成功”写成了一个竞争陷阱。直觉上，leader 如果能把消费者教育成喜欢自己的设计，应该更有市场 power。但模型显示，当消费者的理想点都向 leader 靠拢时，市场上最有价值的位置也变得更靠近 leader。于是 follower 不再远远避开，而是主动靠近、模仿、争夺这群被 leader 培养出来的消费者。Leader 通过好体验创造了一个“大家都想抢”的甜蜜点，最后它的 loyalty moat 可能变成 competitor roadmap。

**一句话 hook**：switching costs 是护城河，preference shifts 可能是靶心。

## 5. 研究背景与动机

### 5.1 实践痛点：同样是“用户很忠诚”，机制可能完全不同

数字市场中，用户 stickiness 很常见，但原因并不相同。Apple 生态既有 proprietary connectors、closed services、accessory incompatibilities 等 switching costs，也有 design coherence、reliability、seamless integration 带来的 preference-based attachment。SaaS、cloud providers、CUDA 生态、streaming services 和 social media apps 也常同时包含这两类机制：一方面迁移数据、重写接口、重新培训用户很贵；另一方面，用户也会因为熟悉界面、信任系统、形成习惯而真的更喜欢原来的产品。

管理者和监管者常把这些现象统一称为“忠诚”或“锁定”。但这会掩盖关键差异：如果用户留下是因为迁移成本高，企业可能拥有更强市场 power；如果用户留下是因为偏好被产品体验改变，那么这种忠诚也可能被竞争者通过接近 incumbent 的设计来争夺。

### 5.2 理论缺口：分析模型长期偏向 switching costs

既有 analytical modeling 多把 brand loyalty 建模为 switching costs，即消费者换品牌时要付出一个外生成本。该传统能解释 lock-in、incumbent advantage 和 higher prices，但较少刻画另一种心理/行为机制：消费经验本身改变消费者的 ideal point。

Marketing 和 psychology 文献早已指出偏好可以被使用经验塑造，例如 mere exposure、habit formation、confirmation bias、perceived reliability、emotional attachment，以及 Carpenter and Nakamoto 关于 pioneer product 影响消费者理想属性组合的研究。本文的贡献是把这些 behavioral insights 放入一个可求解的竞争模型中，研究它们对 entrant positioning、pricing 和 welfare 的影响。

### 5.3 核心贡献

1. 本文在标准 Hotelling 框架中显式建模 preference-shift loyalty：消费者使用 leader 后，其理想点向 leader 产品位置移动。
2. 本文在同一 sequential-entry duopoly primitives 下比较 preference shifts 与 switching costs，说明两者不是同一种忠诚的不同标签，而是方向相反的经济力量。
3. 本文内生化 follower 的 product positioning，揭示 preference shifts 会诱发 strategic convergence，而 switching costs 会诱发 maximal differentiation。
4. 本文给出明确政策含义：不是所有 consumer stickiness 都有害；由改善体验产生的忠诚可能提高消费者剩余和社会福利。

## 6. 模型设定与假设

### 6.1 基础环境

市场是标准 Hotelling line $[0,1]$。消费者在第 1 期均匀分布在 $[0,1]$，位置 $x$ 表示其理想产品特征。产品离消费者理想点越远，消费者承担越高 misfit cost。Leader 固定在 $x_L=0$。第 1 期只有 leader；第 2 期 follower 进入，并选择位置 $x_F \in [0,1]$。

消费者每期至多购买一单位 perishable product，基础 willingness to pay 为 $u$。生产边际成本和固定成本均归一化为 0。论文主要关注 full market coverage，给出 $u>3$ 作为足以保证两期完全覆盖的条件。

### 6.2 符号体系

#### 市场与产品位置

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $x$ | 消费者初始理想点 | 第 1 期均匀分布在 $[0,1]$ |
| $x_T$ | 消费者第 $T$ 期理想点 | Preference-shift model 中第 2 期会变化 |
| $x_L$ | Leader 位置 | 固定为 $0$ |
| $x_F$ | Follower 位置 | 第 2 期进入后选择，$x_F \in [0,1]$ |
| $(x_T-x_i)^2$ | Misfit cost | 二次距离成本，产品越不匹配越痛苦 |

#### 价格、需求与利润

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $p_{L1}$ | Leader 第 1 期价格 | 第 1 期 leader 垄断 |
| $p_{L2}$ | Leader 第 2 期价格 | 与 follower 同时定价 |
| $p_{F2}$ | Follower 第 2 期价格 | follower 进入后设置 |
| $d_{L2}$ | Leader 第 2 期需求 | 由 indifferent consumer 决定 |
| $d_{F2}$ | Follower 第 2 期需求 | $d_{F2}=1-d_{L2}$ |
| $\pi_L,\pi_F$ | 两家企业利润 | 成本为 0，利润等于价格乘以需求 |

#### 忠诚机制参数

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $k$ | Preference shift 强度 | $0<k<1$；消费者向 leader 移动原距离的比例 $k$ |
| $s$ | Switching cost | $s>0$；第 2 期从 leader 换到 follower 的额外成本 |
| $u$ | 每期 willingness to pay | 论文主分析中 $u>3$ 保证 full coverage |

### 6.3 博弈顺序

1. 第 1 期，leader 位于 $0$，设置 $p_{L1}$。
2. 消费者购买并形成某种忠诚：在 preference-shift model 中偏好移动；在 switching-cost model 中消费者偏好不变但未来转换有成本。
3. 第 2 期，follower 进入市场，观察此前结果和消费者偏好/转换成本结构，选择 $x_F$。
4. Leader 和 follower 同时选择 $p_{L2}$ 与 $p_{F2}$。
5. 消费者根据净效用选择购买 leader 或 follower。

信息结构是 complete information。Follower 在第 2 期知道第 1 期 outcome 和忠诚机制强度。

### 6.4 消费者效用

在 preference-shift model 中，消费者第 $T$ 期购买 firm $i$ 的 surplus 为：

$$
CS_{iT}=u-(x_T-x_i)^2-p_{iT}.
$$

> 直觉：$u$ 是产品基础价值；$(x_T-x_i)^2$ 是消费者理想点与产品位置不匹配带来的损失；$p_{iT}$ 是支付价格。Preference shifts 改变的是 $x_T$ 本身，而不是额外增加一个换品牌惩罚。

如果第 1 期消费者 $x$ 购买 leader，第 2 期其理想点变为：

$$
x_2=(1-k)x.
$$

> 直觉：leader 在 $0$，所以 $x$ 乘以 $1-k$ 后更靠近 $0$。$k$ 越大，消费者越被 leader 的产品体验、界面、设计或工作流“塑形”。

在 switching-cost model 中，消费者偏好位置不变。如果第 2 期购买 follower，其 surplus 为：

$$
CS_{F2}=u-(x-x_F)^2-p_{F2}-s.
$$

> 直觉：这里 $s$ 是纯摩擦。消费者没有更喜欢 leader，也没有更讨厌 follower，只是换到 follower 要付迁移、学习、数据转换或兼容成本。

### 6.5 企业利润函数

#### Preference-shift model

第 2 期消费者集中在 $[0,1-k]$ 上，密度变为 $1/(1-k)$。令 indifferent consumer 为 $x_c$，则：

$$
x_c=\frac{p_{F2}-p_{L2}+x_F^2}{2x_F}.
$$

Leader 和 follower 的第 2 期需求分别为：

$$
d_{L2}=\frac{x_c}{1-k}=\frac{-p_{L2}+p_{F2}+x_F^2}{2(1-k)x_F},
$$

$$
d_{F2}=1-d_{L2}.
$$

利润函数为：

$$
\pi_L=p_{L2}\frac{-p_{L2}+p_{F2}+x_F^2}{2(1-k)x_F}+d_{L1}p_{L1},
$$

$$
\pi_F=p_{F2}\left(1-\frac{-p_{L2}+p_{F2}+x_F^2}{2(1-k)x_F}\right).
$$

> 直觉：preference shifts 会把消费者压缩到靠近 leader 的区间，密度变高。给定价格差，任何价格下降都能争夺更多消费者，因此市场更 price sensitive。这是后文“偏好移动反而加强竞争”的数学来源。

#### Switching-cost model

第 2 期 indifferent consumer 为：

$$
x_c^S=\frac{-p_{L2}+p_{F2}+s+x_F^2}{2x_F}.
$$

对应利润函数为：

$$
\pi_L=p_{L2}\left(\frac{-p_{L2}+p_{F2}+s+x_F^2}{2x_F}\right)+d_{L1}p_{L1},
$$

$$
\pi_F=p_{F2}\left(1-\frac{-p_{L2}+p_{F2}+s+x_F^2}{2x_F}\right).
$$

> 直觉：$s$ 直接推高消费者转向 follower 的门槛。因此 leader 可以在第 2 期收取更高价格，而 follower 往往要降价来补偿消费者的 switching cost。

### 6.6 关键假设及其作用

| 假设 | 合理性 | 若放松可能的影响 |
|:---|:---|:---|
| Leader 固定在 $0$ | 简化 sequential entry，突出 follower positioning | 若 leader 也可选址，可能出现先发定位策略；但作者指出第 2 期 qualitative results 较稳健 |
| 两期模型 | 最小化动态复杂性，清楚比较两种忠诚机制 | 多期下可能出现持续创新、重复 repositioning、preference decay |
| Full market coverage，$u>3$ | 避免市场覆盖边界影响，集中分析竞争与忠诚 | 低 $u$ 下 leader 第 1 期未必覆盖全市场，可能影响第 2 期忠诚基础 |
| 二次 misfit cost | Hotelling 文献常见设定，便于得到 interior solution | 线性成本可能改变价格竞争强度和边界阈值 |
| $k$ 与 $s$ 外生 | 将注意力放在忠诚机制的后果，而非忠诚投资决策 | 若企业可投资选择 $k$ 或 $s$，会出现 UX investment 与 lock-in investment 的内生权衡 |
| Follower 可自由选择位置 | 刻画进入者产品定位或模仿设计能力 | 若模仿有成本、IP 保护或技术约束，preference-shift 下的 convergence 会减弱 |

## 7. 分析路线图

本文的分析逻辑很清楚：先分别求解两种忠诚机制，再比较它们。

1. **Preference-shift model**：消费者第 1 期购买 leader 后，理想点向 leader 移动。求解 follower 的最优位置、两家企业第 2 期价格、利润和福利。
2. **Switching-cost model**：消费者偏好不变，但第 2 期换到 follower 要付 $s$。在相同市场 primitives 下求解均衡。
3. **Exogenous follower location 的 special case**：固定 $x_F=1$，先剥离 product positioning 的影响，只比较忠诚机制本身对价格、利润、消费者剩余和社会福利的作用。
4. **Endogenous follower location 的 full comparison**：允许 follower 选择位置，展示最核心发现：preference shifts 会改变 entrant 的定位激励，而 switching costs 不会。
5. **Managerial and policy implications**：把 $k$ 与产品体验、设计一致性、可靠性等联系起来；把 $s$ 与迁移成本、专有接口、合同锁定等联系起来。

## 8. 核心分析与求解

### 8.1 Lemma 1：Preference-shift model 的均衡

在 preference-shift model 中，leader 第 1 期价格为：

$$
p_{L1}=u-1.
$$

第 2 期，如果 $0<k\leq 1/4$，follower 选择最大差异化 $x_F=1$，两家企业价格为：

$$
p_{L2}=\frac{3-2k}{3}, \quad p_{F2}=\frac{3-4k}{3}.
$$

如果 $1/4<k<1$，follower 选择 interior location：

$$
x_F=\frac{4(1-k)}{3},
$$

两家企业价格为：

$$
p_{L2}=\frac{40(1-k)^2}{27}, \quad p_{F2}=\frac{32(1-k)^2}{27}.
$$

> 经济直觉：当 $k$ 小时，消费者只是略微向 leader 移动，follower 仍然通过最大差异化来缓和价格竞争。当 $k$ 足够大时，消费者大量集中到 leader 附近，$x_F=1$ 离需求密集区太远。此时 follower 宁愿靠近 leader，牺牲差异化，以争夺更厚的需求。这就是 preference-shift loyalty 的核心：它不仅影响消费者选择，也重塑 entrant 的位置激励。

**关键 trade-off**：follower 在“远离 leader 以缓和竞争”和“靠近消费者密集区以提高需求”之间权衡。$k$ 越高，后者越重要。

### 8.2 Corollary 1：如果 follower 位置固定在 $1$

当 $x_F=1$ 被外生固定时，preference-shift model 的均衡存在于 $0<k<3/4$。两家企业第 2 期价格仍为：

$$
p_{L2}=\frac{3-2k}{3}, \quad p_{F2}=\frac{3-4k}{3}.
$$

当 $k\geq 3/4$ 时，leader 捕获整个市场。

> 经济直觉：固定 $x_F=1$ 后，follower 无法靠近被 leader “塑形”的消费者。如果 $k$ 太大，消费者都离 leader 太近，follower 只能靠降价弥补巨大的 misfit cost，最终无法有效争夺市场。

### 8.3 Lemma 2：Switching-cost model 的均衡

在 switching-cost model 中，只要 $0<s<3$，follower 总是选择最大差异化：

$$
x_F=1.
$$

Leader 第 1 期价格为 $p_{L1}=u-1$。第 2 期价格为：

$$
p_{L2}=\frac{3+s}{3}, \quad p_{F2}=\frac{3-s}{3}.
$$

当 $s\geq 3$ 时，leader 捕获整个市场。

> 经济直觉：switching cost 不改变消费者理想点，也不创造一个新的需求密集区。Follower 靠近 leader 并不能绕开 $s$，反而会加剧价格竞争。因此 follower 最优策略始终是最大差异化。与 preference shifts 不同，switching costs 是对 entrant 的硬障碍，而不是可通过定位策略部分利用的需求变化。

### 8.4 Proposition 1：固定位置时，两种忠诚对价格、利润和消费者剩余的影响不同

当两家企业位置外生固定时，提高 $k$ 会提高消费者剩余，但提高 $s$ 会降低消费者剩余。提高 $k$ 会降低两家企业第 2 期价格；提高 $s$ 会提高 leader 价格、降低 follower 价格。利润方面，$k$ 对 leader profit 和 total profit 的影响是非单调的；$s$ 则单调提高 leader profit 和 total industry profit。无论哪种忠诚增强，follower profit 都下降。

> 经济直觉：preference shifts 让消费者更靠近 leader，降低 misfit cost，因此消费者变好。同时，消费者分布更集中，价格变动带来的需求变化更大，价格竞争被强化，所以两家企业价格下降。Switching costs 则相反：消费者并没有更满意，只是更难离开。Leader 因此能涨价，follower 必须降价补偿消费者的转换成本。

这组结果对应论文第 9 页 Figure 1 和 Figure 2：Figure 1 显示当最大差异化固定时，preference shifts 下两家企业价格都随 $k$ 下降，而 switching costs 下 leader 价格随 $s$ 上升、follower 价格下降；Figure 2 显示 preference shifts 下需求对价格的敏感性随 $k$ 上升，而 switching costs 下边际需求变化保持常数。

### 8.5 Proposition 2：固定位置时，preference shifts 可能提高社会福利，switching costs 不会

无品牌忠诚的 benchmark social welfare 为：

$$
SW^{Benchmark}=2u-\frac{5}{12}.
$$

当位置外生固定时，如果：

$$
k>\frac{1+\sqrt{10}}{6}\approx 0.694,
$$

preference-shift model 的社会福利会超过无忠诚 benchmark。Switching-cost model 的社会福利则永远不会超过无 switching cost 的 benchmark。

> 经济直觉：社会福利等于总消费价值减去 misfit costs 和 switching costs。Preference shifts 能把消费者理想点推近产品，从而真实降低 misfit costs；switching costs 不改善匹配，只额外制造摩擦，因此是 deadweight loss。论文第 10 页 Figure 4 直观展示了这一点：preference shifts 的福利曲线在较高 $k$ 时超过 benchmark，而 switching costs 的福利曲线始终低于 benchmark。

### 8.6 Proposition 3：内生位置时，follower 的定位策略完全不同

在 preference-shift model 中，follower 的最优位置为：

$$
x_F=
\begin{cases}
1, & 0<k\leq 1/4,\\
\frac{4(1-k)}{3}, & 1/4<k<1.
\end{cases}
$$

在 switching-cost model 中，follower 总是选择：

$$
x_F=1.
$$

> 经济直觉：preference shifts 把消费者集中到 leader 附近，形成一个 follower 可以追逐的“厚市场”。当 $k$ 足够高，靠近 leader 的收益超过差异化损失。Switching costs 没有这种厚市场效应，靠近 leader 只会恶化价格竞争，所以 follower 永远不靠近。论文第 11 页 Figure 5 正是这个结果：preference shifts 下 $x_F$ 在 $k>1/4$ 后向 0 下降；switching costs 下 $x_F$ 始终等于 1。

### 8.7 Proposition 4：内生位置时，preference shifts 更明显地压低利润

当 follower 位置内生时，提高 $k$ 仍然提高消费者剩余、降低两家企业价格；但与固定位置时不同，提高 $k$ 会单调降低两家企业利润。提高 $s$ 则提高 leader profit 和 total industry profit，同时降低 follower profit。

> 经济直觉：固定位置时，preference shifts 一方面加强价格竞争，另一方面也让 leader 附近的需求更厚，因此 leader profit 可能非单调。内生位置时，follower 会向 leader 靠近，主动蚕食这个厚市场。此时产品差异化下降，价格竞争进一步强化，leader 不仅不能完全收割被自己培养出的偏好，反而被 follower 逼着降价。论文第 12 页 Figure 7 显示，内生位置下 leader profit 随 $k$ 下降，而固定位置下则可能在高 $k$ 回升。

### 8.8 Proposition 5：内生位置时，preference shifts 更容易提高社会福利

当 follower 可选择位置时，只要：

$$
\frac{5}{14}<k<1,
$$

preference-shift model 的社会福利就超过无 preference shift 的 benchmark。Switching costs 下的社会福利仍然不会超过无 switching cost 的 benchmark。

> 经济直觉：内生位置让 follower 靠近消费者密集区，进一步降低消费者 misfit costs，同时加剧价格竞争、降低价格。因此 preference shifts 提高福利所需的门槛从固定位置下的约 $0.694$ 降到 $5/14\approx 0.357$。论文第 12 页 Figure 8 显示，内生位置下 social welfare 曲线更早超过 benchmark。

### 8.9 Proposition 6：内生化 follower 位置本身改变了 welfare 与利润分配

当 $1/4<k\leq 3/4$ 时，相比于外生固定 $x_F=1$，允许 follower 内生选择位置会导致：产品差异化下降；leader 价格下降；follower 价格在 $k<5/8$ 时下降、在 $k\geq 5/8$ 时上升；leader profit 和 total profit 下降；follower profit 上升；consumer surplus 和 social welfare 上升。

> 经济直觉：follower 的靠近行为对消费者和自己都有利，但对 leader 和行业利润不利。它把 leader 创造出的 preference-shift demand 变成可争夺市场，降低差异化并引发更强价格竞争。论文第 12 页 Figure 6、Figure 7、Figure 8 合在一起说明：内生位置提高 consumer surplus 和 social welfare，却压低 leader profit。

## 9. 比较静态汇总表

| 参数/机制变化 | Follower 位置 | Leader 价格 | Follower 价格 | Leader 利润 | Follower 利润 | Consumer surplus | Social welfare | 直觉 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| $k\uparrow$，位置固定 | 不变，$x_F=1$ | $\downarrow$ | $\downarrow$ | 非单调：低 $k$ 降，高 $k$ 升 | $\downarrow$ | $\uparrow$ | 高 $k$ 时可超过 benchmark | 消费者更靠近 leader，misfit 降低；但消费者更集中，价格竞争更强 |
| $s\uparrow$，位置固定 | 不变，$x_F=1$ | $\uparrow$ | $\downarrow$ | $\uparrow$ | $\downarrow$ | $\downarrow$ | 始终低于 benchmark | $s$ 是转换摩擦，保护 leader，伤害消费者 |
| $k\uparrow$，位置内生 | 若 $k>1/4$，$x_F=4(1-k)/3\downarrow$ | $\downarrow$ | $\downarrow$ | $\downarrow$ | $\downarrow$ | $\uparrow$ | $k>5/14$ 时超过 benchmark | follower 靠近消费者密集区，差异化下降，竞争增强 |
| $s\uparrow$，位置内生 | 始终 $x_F=1$ | $\uparrow$ | $\downarrow$ | $\uparrow$ | $\downarrow$ | $\downarrow$ | 始终低于 benchmark | follower 无法通过定位绕开 switching cost，只能最大差异化 |
| 允许 follower 内生位置，preference shifts 且 $k>1/4$ | $x_F$ 从 1 向 leader 靠近 | $\downarrow$ | 低 $k$ 降，高 $k$ 可升 | $\downarrow$ | $\uparrow$ | $\uparrow$ | $\uparrow$ | 进入者利用 incumbent 培养出的偏好，导致 strategic convergence |

## 10. 主要结论与管理启示

### 10.1 Benchmark 对比：两种忠诚不是一回事

| 对比维度 | Preference shifts | Switching costs |
|:---|:---|:---|
| 忠诚来源 | 使用经验改变消费者理想点 | 换品牌时存在摩擦或成本 |
| 消费者是否更满意 | 是，产品与新偏好更匹配 | 否，只是转换更难 |
| 对 follower 定位 | 高 $k$ 时 follower 靠近 leader | follower 始终最大差异化 |
| 对竞争强度 | 加剧价格竞争 | 缓和价格竞争 |
| 对 incumbent | 初期有利，但可能被 follower convergence 侵蚀 | 明显有利，形成 incumbent advantage |
| 对行业利润 | 内生位置下下降 | 上升 |
| 对消费者 | 受益于更低 misfit 和更低价格 | 受损于转换摩擦和较高 leader 价格 |
| 对社会福利 | 可提高 | 降低 |
| 监管含义 | 不宜简单打压 | 可通过 portability/interoperability 等降低摩擦 |

### 10.2 对管理者的建议

第一，不要只用 retention rate 判断 loyalty strategy 成功与否。相同留存率可能来自完全不同机制：一个是 lock-in，一个是 genuine preference change。前者提高市场 power，后者可能吸引竞争者靠近。

第二，如果企业通过 user experience、interface design、reliability、system integration 等方式培养 preference-shift loyalty，就必须同步考虑持续差异化能力。若竞争者能快速复制设计语言或产品特征，leader 的偏好塑造会变成 follower 的定位指南，最终引发更强价格竞争。

第三，如果企业通过 proprietary connectors、closed standards、restrictive APIs、data-egress fees、migration barriers 等方式提高 switching costs，短期可能更能保护利润，但长期面临消费者不满、声誉成本与监管风险。

第四，忠诚投资应区分两类目标：如果目标是长期福利和用户满意，preference-shift investment 更有正当性；如果目标是短期利润防御，switching-cost investment 更直接，但政策风险更高。

### 10.3 对监管者的建议

监管者不应把所有用户 stickiness 都解释为有害 lock-in。关键诊断问题是：用户留下来，是因为迁移太贵，还是因为产品更好地改变并满足了其偏好？

当 stickiness 主要来自 switching costs，data portability、interoperability、open standards、限制专有接口或合约锁定等政策更有福利基础。当 stickiness 主要来自 preference shifts，例如用户真的更喜欢某种界面、设计或工作流，强行削弱这种忠诚可能没有必要，甚至可能减少企业改善体验的激励。

## 11. 与相关文献的对话

### 11.1 Klemperer 1987/1995 与 Farrell and Klemperer 2007：switching costs 传统

共同关注点是品牌忠诚如何影响竞争和价格。传统 switching-cost 文献强调，消费者换品牌要付成本，因此 incumbent 可以提高价格并维持优势。本文继承这一机制，但指出它只解释了 loyalty 的一种来源。与其不同，preference shifts 不是换品牌的惩罚，而是消费者理想点本身改变；这会带来更强竞争而不是更弱竞争。

### 11.2 Carpenter and Nakamoto 1989/1996：preference formation 与 pioneer advantage

Carpenter and Nakamoto 的核心洞察是先发产品会塑造消费者心中的理想属性组合，形成 pioneering advantage。本文与其对话最直接：它接受“消费经验会塑造偏好”的 behavioral foundation，但把它放入标准 Hotelling 竞争模型，并允许 entrant 选择位置。结果更反直觉：leader 的 prototypicality 不一定是持久优势，也可能吸引 follower 靠近，从而触发价格战。

### 11.3 Gabszewicz, Pepall, and Thisse 1992：learning-by-using 与 sequential entry

这篇文献也研究 sequential entry 下的 loyalty，但其产品基本是 nonspatial、功能相同的，learning cost 是主要差异来源。因此它不能刻画 follower 如何通过产品定位靠近或远离 leader。本文加入 spatial differentiation，说明 loyalty 不只是进入壁垒，也会改变 entrant 的 positioning incentives。

### 11.4 Villas-Boas 2018 与 Ning and Villas-Boas 2021：taste change 与 repositioning

这些研究关注消费者 taste change 下企业如何 reposition，但重点分别偏向 monopoly 或 symmetric duopoly 的动态 repositioning。本文的区别在于关注 sequential entry 和 asymmetric duopoly：leader 先塑造消费者偏好，follower 后进入并利用这种偏好变化。这使得“偏好改变如何影响进入者定位”成为核心问题。

## 12. 犀利评论：Reviewer’s Critique

### 12.1 优点

理论贡献清楚。文章没有把 loyalty 当成单一黑箱，而是区分 switching costs 与 preference shifts，并说明二者对竞争和福利有相反影响。这一对比非常适合发表在 IS/Marketing 交叉领域，因为数字平台中这两类机制经常并存。

模型设计简洁有效。作者用同一 Hotelling sequential-entry structure 比较两种机制，最大程度控制了市场 primitives，使差异更容易归因于 loyalty mechanism 本身。

实践和政策相关性强。文章能直接对应数据可携带、互操作性、专有接口、用户体验设计、生态系统锁定等现实议题。

### 12.2 模型限制与可能问题

第一，$k$ 和 $s$ 都是外生给定的。现实中企业会选择投资 UX、兼容性、迁移障碍或 closed standards。若把 loyalty-building investment 内生化，企业可能在 preference shifts 与 switching costs 之间做战略组合，而不仅是二选一比较。

第二，模型把产品空间压缩成一维 horizontal differentiation。数字产品通常同时有 horizontal taste、vertical quality、network effects、ecosystem complementarity 等维度。若 follower 在某些维度靠近 leader、在另一些维度差异化，结论可能更复杂。

第三，follower 可以无成本选择靠近 leader。现实中模仿设计、复制生态集成、迁移用户工作流可能有技术成本、品牌成本或知识产权限制。如果靠近 leader 成本高，preference shifts 对竞争强度的影响会减弱。

第四，模型主要是两期，且消费者在第 1 期都购买 leader。多期市场中，preference shifts 可能累积、衰减或被竞争者体验重新塑造；leader 也可能持续创新来维持距离。

第五，监管含义虽然直观，但需要 empirical identification。现实数据中，observed repeat purchase 同时受到 true preference evolution、habit、search cost、switching cost、network effect 和合同约束影响。要将本文用于政策，需要更严谨地区分这些来源。

### 12.3 未来研究方向

1. **内生忠诚投资**：让企业选择 UX investment 以提高 $k$，或选择 lock-in investment 以提高 $s$，并考虑投资成本和监管约束。
2. **多期动态模型**：允许 leader 和 follower 重复 reposition、创新或改变兼容性，研究 preference shifts 是否会形成 dominant design cycle。
3. **平台与生态系统扩展**：加入 complementary goods、network effects、multi-homing 和 data portability，分析 loyalty mechanism 在平台市场中的相互作用。
4. **异质消费者**：引入不同消费者的 $k$、$s$、usage intensity 或 switching ability，解释为什么同一产品对 power users 和 casual users 的忠诚机制不同。
5. **结构估计或实证检验**：用 panel data、choice models、conjoint 或自然实验区分 preference shifts 与 switching costs，检验本文关于价格、定位和 welfare 的预测。

## 13. 读完后应记住的核心句

本文真正想说的是：**品牌忠诚的来源决定竞争的方向**。如果忠诚来自 switching costs，市场会走向 incumbent advantage；如果忠诚来自 preference shifts，市场可能走向 strategic convergence 和更激烈的价格竞争。对企业而言，产品体验创造的忠诚并不自动等于利润护城河；对监管者而言，用户 stickiness 也不自动等于有害锁定。

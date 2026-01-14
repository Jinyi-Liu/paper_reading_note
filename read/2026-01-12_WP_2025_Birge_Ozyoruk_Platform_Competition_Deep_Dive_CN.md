# Birge & Ozyoruk (2025) 论文深度解析  
**Pricing and Capacity Decisions in Platform Competition with Network Externalities**  
（面向 OM/MS/OR 博士生的“可复盘”读书笔记）

---

## 阅读导航

- [0. 一句话概括](#0-一句话概括)
- [1. 研究背景与动机](#1-研究背景与动机)
- [2. 模型设定与假设](#2-模型设定与假设)
- [3. 分析与求解](#3-分析与求解)
- [4. 主要结论与管理启示](#4-主要结论与管理启示)
- [5. Reviewer's Critique](#5-reviewers-critique)
- [6. One More Thing](#6-one-more-thing)
- [附录 A：关键推导速查](#附录-a关键推导速查)

---

## 0. 一句话概括

这篇文章把“平台网络效应”从一句口号（用户越多越强）变成了一个可以算的运营机制：**拥堵（congestion）既带来规模经济（economies of scale），也通过距离导致的等待时间波动制造差异化（differentiation）**。结果很反直觉：在某些市场里网络效应确实把市场推向 winner-takes-all；但在另一些市场里，**服务波动反而让同质化平台也能共存、甚至让进入持续发生直至零利润（contestable market）**。

---

## 1. 研究背景与动机

### 1.1 实践痛点：行业里到底卡在哪？

以网约车（ride-hailing）为例，平台竞争的“核心战场”从来不只是定价，而是三件事纠缠在一起：

1. **价格战与补贴**：平台给乘客降价（或发券），给司机加价（或保底），看起来像两端补贴的老故事，但这里多了拥堵：补贴会改变供需比例，从而改变等待时间、接单率、空驶率。
2. **等待时间与体验波动**：乘客不仅在乎平均等待，还在乎“这一次到底等多久”。而这个波动来自司机-乘客的实时空间位置：同一平台在不同请求上可能表现截然不同。
3. **多平台与进入/退出的现实**：很多城市里并没有“一家独大”；同质化平台也会长期共存，新进入者也会出现。仅用“网络效应越强越垄断”的经典叙事解释不了这些现象。

从运营角度看，最棘手的不是“需求函数长什么样”，而是：**平台规模如何通过运营过程（matching + pickup + travel）内生地改变成本与服务质量**，并进一步改变竞争格局。

### 1.2 理论缺口：现有文献忽略了什么？

文章明确瞄准了一个痛点：**network externalities 的“结构”（structure）**。传统两边市场模型常做两类简化：

- **外部性用一般函数/线性项表示**：例如用户数进入效用或需求的一个线性系数，但缺乏“为什么是这种函数形状”的微观基础（micro-foundation）。
- **差异化往往被外生化**：用 Hotelling/Salop 或“固有偏好”解释平台共存；但在网约车里，一个很自然的差异化来源是：**距离导致的等待时间随机性**，它不是消费者口味，而是运营随机性。

此外，拥堵型平台（ride-hailing）还有一个特殊结构：同侧负外部性、跨侧正外部性同时存在，而且是**非线性**的（因为 pickup time 随供需差异变化）。

### 1.3 核心贡献：Significance 在哪里？

这篇文章的贡献可以拆成三块（每块都很 OM）：

1. **拥堵的微观基础 + 可计算的等待时间表达式**：用空间排队（spatial queueing）+ 最近邻匹配（nearest-neighbor dispatch）推导出平均等待时间 $\bar W(\lambda,s)$ 的闭式结构（至少到可分析的形式），把“网络效应”落到“pickup time 随闲置司机/等待乘客数量变化”的机制上。
2. **把“服务波动”变成差异化来源，并给出 MNL 微观基础**：用距离分布的极值理论（minimum distance 的渐近分布）+ 一个时间-距离的非线性变换，推出实时等待时间 $\varepsilon$ 近似服从 Gumbel，从而让骑手选择自然导向 Multinomial Logit (MNL)。
3. **竞争分析的可解性：降维 + 唯一性/进入结果**：把平台同时决策（价格、工资、等待/容量）通过变量替换压缩成一维“全价”$f=p+c\bar W$ 的竞争，得到一个带规模经济的利润函数，并给出：
   - 多平台均衡可能不存在（winner-takes-all 的根源之一：存在“最低规模门槛”）；
   - 若存在，在合理条件下唯一且全局稳定；
   - 进入可能持续到零利润（contestable），因为 incumbents 缺乏可信承诺（credible commitment）。

---

## 2. 模型设定与假设

这一节的目标不是复述，而是把模型“搭起来”，让你能自己推一遍。

### 2.1 符号体系

> 建议把这一表当作读后复盘时的“字典”。

| 记号 | 含义 | 备注 |
|---|---|---|
| $i\in\{1,\dots,n\}$ | 平台索引 | 先分析 $n=2$（duopoly），再扩展到 $n>2$ |
| $0$ | 外部选项（outside option） | 例如出租车/公交/不开车 |
| $p_i$ | 平台 $i$ 向乘客收取的价格 | 货币单位/每单 |
| $w_i$ | 平台 $i$ 向司机支付的工资率 | 货币单位/小时（或等价） |
| $s_i$ | 平台 $i$ 的司机数量 | 内生，由工资吸引 |
| $\bar\mu$ | 单个司机的“基础服务率”参数 | 文中令 $\bar\mu\equiv\bar\mu_t=\bar\mu_p$ 简化 |
| $\mu_i=s_i\bar\mu$ | 平台 $i$ 的容量（capacity） | “司机数 × 每司机服务率” |
| $\lambda_i$ | 平台 $i$ 的需求/到达率（rider arrival rate） | 由选择模型内生决定 |
| $\rho_i=\lambda_i/\mu_i$ | 利用率（utilization/traffic intensity） | 关键中间变量 |
| $\bar W_i$ | 平均排队等待时间（average waiting time in queue） | 来自空间排队模型的稳态表达式 |
| $\varepsilon_i$ | 实时等待时间（real-time waiting time） | 来自距离随机性，Gumbel 近似 |
| $v$ | 乘客愿付价值（willingness to pay） | 初始设为一般分布，后用 MNL 表达 |
| $c$ | 等待时间的单位不效用（disutility per unit time） | 比较静态用 |
| $r$ | 司机的保留工资（reservation wage） | 供给完全弹性时的关键参数 |
| $\beta$ | 地理结构参数（geography exponent） | 网格 $\beta\approx1$，开阔区域 $\beta\approx1/2$ |
| $m$ | 时间-距离变换参数 | $\varepsilon=\ln(D^m)$ 中的斜率 |
| $f_i=p_i+c\bar W_i$ | 全价（full price） | 把价格和平均等待的效用损失合并 |
| $f_0=p_0+c\bar W_0$ | 外部选项的全价 | 常数 |
| $\kappa=2/(cm)$ | Logit “敏感度”参数 | 来自 Gumbel 的尺度参数 |
| $\varphi(\beta)$ | 规模经济成本项系数 | $\varphi(\beta)=\left(1+\frac{1}{\beta}\right)(\beta r c^\beta)^{1/(1+\beta)}$ |

---

### 2.2 博弈/决策结构

**两阶段静态博弈（static game with two stages）**：

1. **阶段 1（平台同时出价）**：每个平台 $i$ 同时选择对两端的“报价”：
   - 对乘客：$(p_i,\bar W_i)$（价格与平均等待/服务质量）；
   - 对司机：$w_i$（工资激励）。
2. **阶段 2（两端选择/进入）**：
   - 乘客根据效用选择平台或外部选项；
   - 司机根据工资与利用率决定是否加入平台（供给完全弹性时会调整到零利润边界）。

**信息结构（Information Structure）**：  
平台知道模型参数（$c,r,\beta,m$ 等）并理解需求与等待时间如何内生决定；乘客在选择时面临实时等待时间冲击 $\varepsilon_i$（周期性多栖时可视为独立抽样），司机周期性比较平台报价（periodic multihoming 的直觉）。

---

### 2.3 乘客端：效用与选择

#### 2.3.1 基本效用（平均等待）

乘客选择平台 $i$ 的效用（文中起点）为：
$$
u_i = v - p_i - c\bar W_i.
$$
外部选项的效用为：
$$
u_0 = v - p_0 - c\bar W_0,
$$
其中 $(p_0,\bar W_0)$ 是不受拥堵影响的常数。

#### 2.3.2 引入实时等待时间（差异化核心）

真实世界里，乘客看到的等待时间会因为“最近的可用司机在哪里”而波动。于是效用升级为：
$$
u_i = v - p_i - c(\bar W_i+\varepsilon_i).
$$

关键点：$\varepsilon_i$ 不是“口味噪声”，而是**空间匹配的运营随机性**。这将决定平台之间是否存在“自然差异化”。

---

### 2.4 供给端：司机进入与工资-利用率关系

司机是独立个体，外部机会成本用保留工资 $r$ 表示。文中假设司机供给完全弹性：只要平台提供的“期望收益”达到 $r$，就会有足够多司机进入直到等号成立。

在最近邻分配下，每个司机被分配到一次新请求的概率约为 $1/s_i$，因此单个司机的期望收益与平台的利用率 $\rho_i$ 成正比。均衡条件为：
$$
w_i\rho_i=r.
$$

这条式子非常重要，因为它把“工资决策”变成了“容量/利用率”决策的镜像：当平台想提高服务水平（降低等待）时，需要更多司机，$\rho_i$ 下降，于是为了满足 $w_i\rho_i=r$，$w_i$ 必须上升。

---

### 2.5 拥堵微观基础：空间排队 + 最近邻

这一块是文章的“硬核底座”：平均等待时间不是拍脑袋设个函数，而是从空间结构推出来的。

#### 2.5.1 最近邻距离的尺度：$\beta$ 从哪里来？

设有 $k$ 个点（例如空闲司机位置）在区域内均匀散布，考察任一点（例如新乘客位置）到最近点的距离。经典结果是：

- **线/网格型结构**（城市道路网络近似为多条线段拼接）：最近距离的期望量级为 $\Theta(1/k)$；
- **二维开阔区域**：最近距离的期望量级为 $\Theta(1/\sqrt{k})$。

文章用一个统一写法：最近距离期望量级为 $\Theta(1/k^\beta)$，其中网格 $\beta\approx1$，开阔区域 $\beta\approx1/2$。图 1（论文第 13 页）用示意图把这两种地理结构直观对比出来。

#### 2.5.2 服务时间：pickup + travel，且 pickup 依赖系统状态

每次服务的时间由两部分构成：

- travel time：平均为 $1/\bar\mu_t$（相对简单）；
- pick-up time：平均为 $(1/\bar\mu_p)/(|s-q|\vee1)^\beta$，其中 $q$ 是系统内乘客数量，$s$ 是司机数量。

因此在状态 $q$ 下的总服务率为（论文式子）：
$$
\mu(q)=\left(\frac{1/\bar\mu_p}{(|s-q|\vee1)^\beta}+\frac{1}{\bar\mu_t}\right)^{-1}\min(s,q).
$$

解释一句人话：当系统里“空闲司机多”或“等待乘客多”时，最近邻距离变小，pickup 更快，服务率上升；当 $q$ 接近 $s$ 时，既没有太多空闲司机也没有太多等待乘客，pickup 反而较慢（图 2，论文第 13 页，呈现出以 $q=s$ 为峰的形状）。

#### 2.5.3 流体极限与稳态：得到 $\bar W(\lambda,s)$

把系统放大（到达率与服务时间按规模缩放）后，队长过程收敛到一个反射微分方程（reflected ODE）。在效率驱动（efficiency-driven）稳态下（$q^\ast>s$），文章给出唯一均衡点：
$$
\bar q = s + \left(\frac{\eta\rho}{1-\rho}\right)^{1/\beta},\qquad \rho=\frac{\lambda}{s\bar\mu_t},\quad \eta=\frac{1/\bar\mu_p}{1/\bar\mu_t}.
$$

于是平均排队等待时间为：
$$
\bar W(\lambda,s)=\frac{\bar q-s}{\lambda}=\frac{1}{\lambda}\left(\frac{\eta\rho}{1-\rho}\right)^{1/\beta}.
$$

之后文章为了符号简洁令 $\bar\mu\equiv\bar\mu_t=\bar\mu_p$，即 $\eta=1$，并记 $\mu=s\bar\mu$，得到更紧凑的形式：
$$
\bar W(\lambda,\mu)=\frac{1}{\lambda}\left(\frac{\rho}{1-\rho}\right)^{1/\beta}=\frac{1}{\lambda}\left(\frac{\lambda}{\mu-\lambda}\right)^{1/\beta},\qquad \rho=\frac{\lambda}{\mu}.
$$

> **网络效应在这里的“结构”**：当平台同时吸引更多乘客（$\lambda$）和司机（$\mu$），即使利用率 $\rho$ 不变，$\bar W$ 也会因为规模放大而下降（$\bar W$ 随比例扩张变小）。这就是“规模经济式的网络效应”。

---

### 2.6 实时等待时间的分布：从距离极值到 Gumbel

如果 $k$ 个司机位置在二维区域 $C$ 内均匀 iid，乘客点 $y_0$ 到最近司机的距离的渐近分布满足（论文 Lemma 5）：
$$
\mathbb P\!\left(\sqrt{k}\cdot \min_{i\le k}\|Y_i-y_0\|\le x\right)\to 1-\exp\!\left(-\frac{\pi x^2}{|C|}\right).
$$
记渐近最小距离为 $D$，则 $D$ 属于 Weibull 家族。

随后作者引入一个关键建模选择：真实道路上时间与距离关系是**凹的**（远距离可能走快路），用一个对数形式近似：
$$
\varepsilon=\ln(D^m).
$$

在这个变换下，$\varepsilon$ 落入 Gumbel 分布族，从而两平台（或多平台）间的效用差异自然导出 MNL：

在周期性多栖（periodic multihoming）下，$\varepsilon_i$ 可视为平台间独立，乘客选择平台 $i$ 的概率为（论文 Lemma 7）：
$$
\lambda_i=\frac{\exp(\kappa[f_0-f_i])}{1+\sum_{j=1}^n\exp(\kappa[f_0-f_j])},\qquad \kappa=\frac{2}{cm},
$$
其中 $f_i=p_i+c\bar W_i$。

---

### 2.7 关键假设清单与合理性

下面把“必须记住”的假设列出来，并给出一两句 justification（你在写 referee report 时也会用到）。

1. **最近邻匹配（NN dispatch）**：相比 FCFS，它更符合网约车平台“就近派单”的运营逻辑，也使 pickup time 与最近邻距离直接挂钩。
2. **空间均匀分布**：对解析友好，且在大尺度/高密度下可作为一阶近似；后续可扩展到非均匀密度或多中心城市。
3. **流体极限/大规模近似**：把随机排队过程压缩成确定性稳态表达式，换取可解性；适用于高频交易式的网约车需求。
4. **司机供给完全弹性（$w\rho=r$）**：有经验依据（司机可灵活上线/下线），也使容量端能快速响应工资；但这是强假设，会影响进入与利润结论（后文 critique 会喷它）。
5. **时间-距离对数关系 $\varepsilon=\ln(D^m)$**：来自模拟拟合与道路结构直觉；关键作用是把 Weibull 的最小距离变换成 Gumbel，从而获得 MNL。
6. **周期性多栖导致平台间 $\varepsilon_i$ 独立**：使差异化“留在系统里”；相反如果连续多栖（continuous multihoming），会把差异化抹平，直接导致 Bertrand（论文 Lemma 6）。

---

## 3. 分析与求解

核心技术路线是：**把一个看似三维决策（$p,\bar W,w$）的两边市场竞争，变成一维的“全价”竞争**。这一步是整篇文章的解题钥匙。

### 3.1 求解逻辑总览

1. 用排队稳态把 $\bar W$ 写成 $(\lambda,\mu)$ 的函数；
2. 用司机零利润边界 $w\rho=r$ 把工资写成 $(\lambda,\bar W)$ 的函数；
3. 引入全价 $f=p+c\bar W$，需求只依赖 $f$（来自 MNL）；
4. 对给定 $f$，平台选择 $\bar W$（等价于容量）做“内层优化”，得到最优 $\bar W^\ast(\lambda)$；
5. 代回得到只关于 $f$ 的利润函数，分析 best response、均衡存在/唯一、进入与比较静态。

---

### 3.2 关键降维：从 $(p,\bar W,w)$ 到 $f$

先用 $\eta=1$（即 $\bar\mu_t=\bar\mu_p=\bar\mu$）后的等待时间表达式：
$$
\bar W_i=\frac{1}{\lambda_i}\left(\frac{\lambda_i}{\mu_i-\lambda_i}\right)^{1/\beta}.
$$

令 $x_i=\lambda_i\bar W_i$，可得：
$$
x_i^\beta=\frac{\lambda_i}{\mu_i-\lambda_i}\quad\Rightarrow\quad \mu_i=\lambda_i+\frac{\lambda_i}{x_i^\beta}.
$$

司机均衡 $w_i\rho_i=r$，且 $\rho_i=\lambda_i/\mu_i$，因此：
$$
w_i=r\frac{\mu_i}{\lambda_i}=r\left(1+\frac{1}{x_i^\beta}\right)=r+\frac{r}{(\lambda_i\bar W_i)^\beta}.
$$

平台利润：
$$
\pi_i=\lambda_i(p_i-w_i)=\lambda_i(p_i-r)-\frac{r\lambda_i}{(\lambda_i\bar W_i)^\beta}.
$$

引入全价 $f_i=p_i+c\bar W_i$，即 $p_i=f_i-c\bar W_i$，代入：
$$
\pi_i=\lambda_i(f_i-r)-\underbrace{\lambda_ic\bar W_i-\frac{r\lambda_i}{(\lambda_i\bar W_i)^\beta}}_{\text{“用容量换等待”的成本项}}.
$$

需求端由 MNL 给出：
$$
\lambda_i=\frac{\exp(\kappa[f_0-f_i])}{1+\sum_{j=1}^n\exp(\kappa[f_0-f_j])},\qquad \kappa=\frac{2}{cm}.
$$

注意：**$\lambda_i$ 只依赖 $f$，不依赖 $p$ 与 $\bar W$ 的拆分**。这为内层优化打开了门。

---

### 3.3 内层优化：给定需求规模时的最优等待/容量

固定 $f_i$（从而固定 $\lambda_i$），平台对 $\bar W_i$ 的问题等价于最小化成本项：
$$
\min_{\bar W_i>0}\;\; \lambda_i c\bar W_i+\frac{r\lambda_i}{(\lambda_i\bar W_i)^\beta}.
$$

令 $x=\lambda_i\bar W_i$，则问题变为：
$$
\min_{x>0}\;\; cx+r\lambda_i x^{-\beta}.
$$

一阶条件：
$$
c-\beta r\lambda_i x^{-(\beta+1)}=0\quad\Rightarrow\quad x^\ast=\left(\frac{\beta r\lambda_i}{c}\right)^{1/(\beta+1)}.
$$

因此最优平均等待时间为：
$$
\bar W_i^\ast=\frac{x^\ast}{\lambda_i}=\left(\frac{\beta r}{c\lambda_i^\beta}\right)^{1/(1+\beta)}.
$$

> **运营直觉**：$\bar W$ 越小，意味着平台要“堆司机”来提高服务（$\mu$ 上升），但这会降低 $\rho$，从而拉高工资 $w$（因为 $w\rho=r$ 必须成立）。最优 $\bar W^\ast$ 正是在“乘客等不起（$c$）”与“司机不白干（$r$）”之间平衡出来的。

把最优成本代回（用 $r\lambda x^{-\beta}=cx/\beta$）：
$$
\lambda_i c\bar W_i^\ast+\frac{r\lambda_i}{(\lambda_i\bar W_i^\ast)^\beta}=\left(1+\frac{1}{\beta}\right)c x^\ast
=\left(1+\frac{1}{\beta}\right)(\beta r c^\beta)^{1/(1+\beta)}\lambda_i^{1/(1+\beta)}.
$$

定义：
$$
\varphi(\beta)=\left(1+\frac{1}{\beta}\right)(\beta r c^\beta)^{1/(1+\beta)},\qquad \gamma=\frac{1}{1+\beta},
$$
得到**降维后的利润函数（论文 Theorem 1）**：
$$
\pi_i=\lambda_i(f_i-r)-\varphi(\beta)\lambda_i^\gamma.
$$

这里的结构非常关键：成本函数 $C(\lambda)=r\lambda+\varphi(\beta)\lambda^\gamma$ 是**凹的（concave）**，意味着单位成本 $r+\varphi(\beta)\lambda^{\gamma-1}$ 随规模上升而下降（economies of scale）。

---

### 3.4 核心命题与经济学直觉

下面挑最“扛事”的结果讲透：不只是写结论，更要把机制拆开。

---

#### 3.4.1 Proposition 1：如果平台承诺固定等待时间，纯策略均衡不存在

在“没有实时波动”的中间模型里，平台承诺确定性的 $\bar W_i$，乘客效用只有确定项 $v-p_i-c\bar W_i$。结果是：两平台若都想保有正份额，**纯策略 Nash Equilibrium 不存在**（但存在混合策略均衡）。

**直觉**：没有 $\varepsilon$ 这种“运营随机差异化”时，乘客面对的是完全可比的“全价”$p+c\bar W$。任意一个内点定价都可以被对手以一个极小的 undercut 赢走全部需求，而在两边市场里，需求塌陷会立刻抬高单位成本（因为规模经济消失），从而逼迫继续 undercut 或退出。于是出现类似 Bertrand 的“没有舒服的内点”。

---

#### 3.4.2 Lemma 6：连续多栖会把市场推到零利润

如果所有司机同时给所有平台服务（continuous multihoming），那么每个平台面对的实时等待冲击相同：$\varepsilon_1=\varepsilon_2=\cdots$。于是差异化被彻底抹掉，只剩下确定的全价比较，得到 **Bertrand 式零利润均衡**。

**运营机制**：平台之间本来可以靠“我这边恰好更近的司机更多”来差异化；但如果司机池完全共享，距离优势瞬间公共化，竞争回到纯价格。

这条结论非常适合写进管理启示：**多栖不是越多越好，极端多栖会杀死差异化**。

---

#### 3.4.3 Lemma 7：周期性多栖 + Gumbel $\Rightarrow$ MNL

当司机周期性在平台间切换，使得每个平台在乘客请求时面对的最近邻距离独立，且 $\varepsilon_i$ 近似 Gumbel，则乘客选择遵循 MNL：
$$
\lambda_i=\frac{\exp(\kappa[f_0-f_i])}{1+\sum_{j=1}^n\exp(\kappa[f_0-f_j])},\qquad \kappa=\frac{2}{cm}.
$$

**直觉**：这给了一个“非常 OM 的 Logit”：随机效用不是心理偏好，而是空间匹配的极值随机性。你可以把它理解成：每次请求平台都在掷骰子，骰子大小由其司机密度/等待结构决定。

---

#### 3.4.4 Theorem 1：平台竞争出现规模经济，且可降维到一维全价

降维后的利润：
$$
\pi_i=\lambda_i(f_i-r)-\varphi(\beta)\lambda_i^\gamma,\qquad \gamma=\frac{1}{1+\beta}\in\left[\frac{1}{2},\frac{2}{3}\right].
$$

把括号写成“单位利润”更清楚：
$$
\pi_i=\lambda_i\Big(f_i-\underbrace{\Big[r+\varphi(\beta)\lambda_i^{\gamma-1}\Big]}_{\text{单位成本}}\Big).
$$

由于 $\gamma-1<0$，单位成本随 $\lambda_i$ 增大而下降——这就是规模经济。

**运营直觉**：更多订单意味着更高密度，pickup 更快、司机利用率更高、补贴/工资摊薄，平台每单更省。于是平台必须跨过某个规模门槛才可能盈利：小平台不是“效率差一点”，而是“单位成本高到根本活不了”。

---

#### 3.4.5 Proposition 3：最佳反应存在“退出阈值”

论文证明存在一个阈值 $f_j^\circ$：如果对手全价 $f_j$ 太低，平台 $i$ 的任何有限 $f_i$ 都会导致负利润，于是最优是选择 $f_i\to\infty$（退出）。

形式上，最优反应是：
- 若 $f_j>f_j^\circ$：选择内点最优 $f_i^\ast(f_j)$；
- 若 $f_j\le f_j^\circ$：退出（或在零利润点无差异）。

**直觉（关键）**：传统 Bertrand 里你还能“薄利多销”；但这里薄利不一定能多销，因为一旦份额小，规模经济被剥夺，单位成本暴涨，你甚至没法靠降价抢份额——降价只会让亏损更大。于是出现“要么活得像个平台，要么别活”。

---

#### 3.4.6 Theorems 2–3：唯一性与全局稳定（在合理条件下）

文章给出一个（相当温和的）条件，使得只要平台不退出，best response 的斜率满足 $-1<b_i'(f_j)<1$，从而：

- **最多存在一个**“两平台都占有正份额”的均衡；
- 若该均衡存在，则**全局稳定**（迭代 best response 会收敛）。

条件写成：
$$
\frac{r}{c}\left(\frac{2}{m}\right)^{1+\beta}\ge g(\beta),
$$
其中 $g(\beta)$ 是在 $\beta\in[1/2,1]$ 上单调递减的函数，且 $g(1/2)=1.35,\;g(1)=0$。

**直觉**：$r/c$ 高意味着“司机时间价值高、乘客等待厌恶相对低”，平台更不愿意堆司机去极限压等待，竞争不会失控；同时 $m<2$（作者经验上如此）使得 MNL 的价格敏感度参数 $\kappa=2/(cm)$ 不会过大，从而需求不会对微小价格差异过度敏感。这些都让 best response 不会产生“过度反应”。

---

#### 3.4.7 Theorem 4：均衡存在的充要条件（duopoly）

假设存在对称均衡 $(f^\ast,f^\ast)$，则它必须满足对称一阶条件：
$$
f-r=\frac{1}{\kappa(1-\lambda(f,f))}+\frac{\varphi(\beta)}{(1+\beta)\lambda(f,f)^{\beta/(1+\beta)}},
$$
并且利润非负 $\pi_i(f^\ast,f^\ast)\ge0$。

更重要的是：论文证明这两个条件**不仅必要，而且充分**。

把右边两项解释一下：

- 第一项 $\frac{1}{\kappa(1-\lambda)}$：离散选择模型的经典“markup = inverse semi-elasticity”结构；
- 第二项 $\frac{\varphi(\beta)}{(1+\beta)\lambda^{\beta/(1+\beta)}}$：来自规模经济/网络效应的“额外 markup 校正”，且它随 $\lambda$ 增大而下降。

**直觉**：当平台规模变大，单位成本下降，最优全价可能下降（而不是上升），这与“强网络效应导致高价垄断”的直觉不总一致。

---

### 3.5 比较静态：关键参数怎么推着均衡走？

下面用“方向 + 机制”方式总结文章最重要的比较静态（并补上直觉链条）。

#### 3.5.1 市场规模/外部选项：winner-takes-all 的温床

- **低需求或外部选项很强（$f_0$ 低）**：总可分配需求小，单个平台很难达到盈利所需的最低 $\lambda$ 门槛。于是多平台均衡可能不存在，市场更可能走向“一个平台活下来”（winner-takes-all）。
- **高需求或外部选项很弱（$f_0$ 高）**：多个平台更可能同时跨过门槛，允许共存。

机制：规模经济导致“门槛效应”（threshold effect）。这与传统线性网络效应模型里的平滑比较静态不同。

#### 3.5.2 服务波动强度：进入与平台数量

平台数量的上界来自“每家平台必须有足够份额才能不亏”。论文在 entry 部分给出一个阈值：在对称均衡下利润非负当且仅当
$$
\frac{\lambda^{1-\gamma}}{1-\lambda}\ge \kappa\varphi(\beta)(1-\gamma),
$$
其中 $\gamma=1/(1+\beta)$。左边随 $\lambda$ 单调上升，因此存在一个最小份额 $\lambda_{\min}$。

于是可存活平台数大致满足 $n\lesssim 1/\lambda_{\min}$。论文进一步给出比较静态：最大可存活平台数 $\bar n$

- 随 **司机保留工资 $r$ 增大而下降**（成本更高，门槛更高）；
- 随 **等待不效用 $c$ 增大而上升**（差异化更强，价格竞争更软，每家更容易留住份额）。

这里的 $c$ 之所以促进进入/共存，不是因为等待让大家都痛苦，而是因为它放大了 $\varepsilon$ 在效用里的权重，从而增强“随机差异化”。

#### 3.5.3 地理结构 $\beta$：网格更“卷”，郊区更“躺”

论文 Theorem 8：当 $\beta$ 增大（从开阔区域走向网格/中心城区），平台的 best response 全价下降，即市场更竞争，均衡价格更低。

直觉链条可以这样理解：

- 更高的 $\beta$ 意味着最近邻距离随“额外可用点数”下降得更快；
- 因此平台通过扩容来改善等待的边际效率更高；
- 平台更愿意用更低的全价去争夺规模，因为规模带来的成本下降更“划算”；
- 结果是更激烈的价格竞争、更低的均衡全价，也更可能把弱平台挤出。

这给了一个非常运营化的预测：**同样的竞争环境，在网格化密集城区更可能出现低价竞争与高淘汰率；在更分散区域更可能维持多平台共存**。

---

## 4. 主要结论与管理启示

### 4.1 机制揭示：相比 benchmark，这篇模型新揭示了什么 trade-off？

我认为最值得抓住的三条“新 trade-off”是：

1. **规模经济 vs. 差异化来源不是偏好，而是运营波动**  
   Benchmark（典型两边市场）把差异化交给“品味/品牌”；本文告诉你：哪怕平台 ex-ante 同质，**距离导致的服务波动**也能让市场不走向单一赢家。
2. **网络效应并非总是护城河：缺乏承诺会让进入持续发生**  
   incumbents 不能承诺不在进入后改价/改工资，于是无法 credibly deter entry。进入者只要利用随机差异化拿到一点份额，就可能存活；但规模经济又让每家必须有最低份额，于是进入会持续到“刚好都不赚钱”。
3. **消除波动的好心，可能毁掉差异化，导致 Bertrand**  
   两个例子特别尖锐：  
   - 平台承诺固定等待时间（把 $\varepsilon$ 干掉）会把竞争推向 undercut；  
   - 司机连续多栖（把平台间 $\varepsilon_i$ 相关性推到 1）也会把竞争推向零利润。  
   这两条都在提醒管理者：**不要把“降低波动”当作无条件的好事**，它也可能是差异化的来源。

---

### 4.2 管理建议：对平台管理者/政策制定者的 actionable takeaways

#### 4.2.1 对平台管理者

1. **把“可信承诺机制”当作战略资产**  
   如果市场处在“服务波动可支撑多平台”的区域，进入会持续把利润压到零。要想不被卷死，平台需要能承诺并锁定用户/司机的机制，例如：会员制（subscription）、长期激励合约、阶梯式忠诚计划、或某种形式的 exclusivity。
2. **谨慎对待“保证固定等待时间”**  
   过度 SLA 化（service-level agreement）可能消除自然差异化来源，让平台只能靠价格竞争。更聪明的做法可能是“分层服务”（不同等待分布/可预测性对应不同价格）。
3. **管理司机多栖，而不是简单拥抱它**  
   适度的周期性多栖能存在差异化，但极端连续多栖会抹平差异化。平台在设计司机端政策时，需要区分：  
   - 允许司机“切换”（现实里很难完全禁止）；  
   - 但避免司机“同时在线于所有平台并完全共享空闲池”的极端情形。
4. **利用地理结构做区域化策略**  
   在网格化城区（高 $\beta$）竞争更激烈，平台需要更精细的运营（调度、激励、区域补贴）与更强的留存机制；在分散区域（低 $\beta$）则可能更容易维持价格与多平台共存。

#### 4.2.2 对政策制定者/监管者

1. **“反垄断直觉”要条件化**：网络效应强不必然导致垄断；运营波动与多栖行为会改变竞争结构。
2. **关注承诺与锁定机制的福利效应**：平台用留存机制抵御进入可能提高效率，但也可能加剧市场势力，需要评估消费者剩余与动态效率的权衡。

---

### 4.3 图表解释：关键图到底在说什么？

> 你完全可以只看这几幅图，就抓住全文的“形状”。

1. **图 1（第 13 页）：$\beta$ 的几何意义**  
   左边网格：最近邻距离随点数以 $1/k$ 下降（$\beta\approx1$）；右边开阔：以 $1/\sqrt{k}$ 下降（$\beta\approx1/2$）。这是后面所有比较静态的源头。
2. **图 2（第 13 页）：平均 pickup time 的“峰在 $q=s$”**  
   当司机与乘客数量恰好匹配时，既没有空闲司机冗余也没有等待乘客堆积，最近邻距离反而相对大；而当任一侧“堆多了”，最近邻更近，pickup 更快。
3. **图 3（第 20 页）：利润对全价的 quasi-concave–quasi-convex 结构**  
   低价区提价增利；中间区提价损利；高价区需求趋零利润回到 0。这种“先上后下再回到 0”的形状解释了为什么 best response 要么内点要么退出。
4. **图 4（第 21 页）：best response 有阈值并可能无交点**  
   当对手价格过低，自己的 best response 是退出（跳到 $\infty$）；只有当 best response 曲线在阈值处起点高于 45 度线时，才有唯一对称均衡。
5. **图 5（第 28 页）：Gumbel 拟合实时等待时间**  
   (a) 直方图 + 拟合曲线；(b) 2%–96% 分位数的 Q-Q plot 近似线性。说明用 Gumbel 近似 $\varepsilon$ 是合理的工程化假设。
6. **图 6–7（第 29–30 页）：平均系统人数的验证与鲁棒性**  
   图 6：理论与观测 Q-Q 几乎贴线；图 7：把平均行程时间参数人为提高 20% 后，拟合明显变差，说明模型不仅“能拟合”，还对参数有识别含义。

---

## 5. Reviewer's Critique

下面换上“严厉 Senior Editor”的人格（但不刻薄，只刻薄于逻辑）。

### 5.1 我会给的优点（Strengths）

1. **真正的 OM 贡献：把网络效应写成运营方程**  
   很多平台论文在“网络效应函数”上偷懒；本文用空间排队把 pickup 机制讲清楚，属于“把运营塞回 IO/平台理论”的好工作。
2. **差异化来源新颖且合理**  
   用距离波动推导 Gumbel/MNL 是漂亮的 microfoundation：差异化不是偏好，是系统随机性。
3. **技术上不回避规模经济的麻烦**  
   成本凹（concave）意味着很多标准定理不能直接用；作者给出 contraction/唯一性条件与存在性刻画，处理得很硬。
4. **有数据验证，不只是理论自嗨**  
   用 NYC TLC 数据对实时等待分布与稳态关系做验证，至少让关键假设站得住。

### 5.2 我会追着问的缺点（Weaknesses / Concerns）

1. **司机供给“完全弹性”很强**  
   $w\rho=r$ 让容量能无摩擦调整，这会：
   - 放大规模经济的门槛效应；
   - 也可能夸大“进入持续到零利润”的结论。  
   现实里司机有异质性、上线成本、平台特定摩擦、以及多栖切换成本，都会使供给曲线变陡，从而改变 entry dynamics。
2. **平台能“选择平均等待时间”这一行动的可解释性**  
   平台不是真的发布一个 $\bar W$ 并保证它，而是通过工资、调度、补贴间接影响它。作者用 $\bar W$ 作为决策变量是为了解析（最后也通过内层优化把它消掉），但在解释层面需要更明确地把它映射为“容量/激励策略”。
3. **MNL 的 IIA 限制**  
   Logit 的独立无关替代（IIA）在多平台/多区域下可能过于强，尤其当平台之间地理重叠、等待冲击相关时，替代模式会改变。
4. **时间-距离对数变换 $\varepsilon=\ln(D^m)$ 的外生性**  
   这一步很关键，但有点“工程拟合”。它解释了凹关系，却把道路网络、交通、调度策略等都压成了一个 $m$。作为理论建模可以接受，但如果想做结构估计或政策模拟，需要更明确的 microfoundation 或敏感性分析。
5. **均衡选择：为何只看 efficiency-driven 稳态？**  
   论文提到质量驱动（quality-driven）也可能有均衡（$q^\ast<s$），但作者选择效率驱动作为“更合理”。我同意这种选择有经济直觉（不想浪费司机冗余），但在竞争语境下，平台可能为了差异化故意留冗余容量（类似 QoS 竞争）。这会影响均衡存在与价格比较静态。

### 5.3 未来方向：在此基础上还能怎么扩展？

1. **动态模型 + 承诺机制（credible commitment）**  
   论文的一个核心结论是“缺乏承诺导致进入把利润压到零”。最自然的扩展是动态博弈：平台能否通过长期合同、会员制、价格承诺、容量投资（例如自营车队/AV）来改变进入均衡？
2. **内生多栖：司机为何周期性切换？**  
   目前 periodic multihoming 是假设。可以引入司机的切换成本、信息更新频率、以及平台的排他激励，内生决定 $\varepsilon_i$ 的相关结构。
3. **空间异质性与多区域网络**  
   把城市拆成多个区域（CBD vs suburb），让 $\beta$ 或密度随区域变化，并允许平台跨区调度，会更贴近现实，也可能产生“局部垄断 + 全局竞争”的混合结构。
4. **更丰富的选择模型与等待分布**  
   若用 nested logit / mixed logit 或者显式的等待分布风险厌恶（variance aversion），可能更能捕捉“乘客厌恶不确定性”的行为，从而改变“保证等待时间会杀死差异化”的结论边界。
5. **平台算法差异（dispatch / matching policy）**  
   如果平台不都是最近邻或策略可选，算法差异本身可能成为差异化来源，与本文的“随机差异化”形成互补。

---

## 6. One More Thing

我认为本文最值得分享的“灵光一现”，是把三件看似不搭界的东西焊到一起：

> **最近邻距离的极值理论（Weibull）** → 通过 $\varepsilon=\ln(D^m)$ 变换得到 **Gumbel** → 于是骑手选择自然是 **MNL**。

这是一种很漂亮的“从运营随机性到经济学需求系统”的桥梁。它不仅让模型可解（Logit 的可微/封闭形式太香了），更重要的是让差异化来源变得可解释：**平台的差异化不是品牌，而是“在这一单上我更可能离你近”**。

如果你未来要写平台竞争论文，这种“把随机性从系统机制推到需求形式”的思路，值得反复琢磨。

---

## 附录 A：关键推导速查

这一节把几个最容易忘的推导集中放在一起，方便你之后快速复盘。

### A.1 从等待时间到工资函数

在 $\eta=1$ 且效率驱动稳态下：
$$
\bar W=\frac{1}{\lambda}\left(\frac{\lambda}{\mu-\lambda}\right)^{1/\beta}.
$$
令 $x=\lambda\bar W$，则 $x^\beta=\frac{\lambda}{\mu-\lambda}$，所以 $\mu=\lambda+\frac{\lambda}{x^\beta}$。

司机零利润边界 $w\rho=r$ 且 $\rho=\lambda/\mu$，因此：
$$
w=r\frac{\mu}{\lambda}=r\left(1+\frac{1}{(\lambda\bar W)^\beta}\right)=r+\frac{r}{(\lambda\bar W)^\beta}.
$$

### A.2 内层优化的一阶条件

给定 $\lambda$，最小化 $cx+r\lambda x^{-\beta}$，FOC：
$$
c=\beta r\lambda x^{-(\beta+1)}\Rightarrow x^\ast=\left(\frac{\beta r\lambda}{c}\right)^{1/(\beta+1)}.
$$
因此 $\bar W^\ast=(\beta r/(c\lambda^\beta))^{1/(1+\beta)}$。

### A.3 降维后的利润与单位成本

$$
\pi=\lambda(f-r)-\varphi(\beta)\lambda^\gamma,\qquad \gamma=\frac{1}{1+\beta}.
$$
单位成本：
$$
\text{unit cost}=r+\varphi(\beta)\lambda^{\gamma-1}.
$$

### A.4 对称均衡下利润非负的份额阈值

对称 FOC 给出 $f-r=\frac{1}{\kappa(1-\lambda)}+\varphi(\beta)\gamma\lambda^{\gamma-1}$。代回利润：
$$
\pi=\frac{\lambda}{\kappa(1-\lambda)}-\varphi(\beta)(1-\gamma)\lambda^\gamma.
$$
因此 $\pi\ge0$ 当且仅当：
$$
\frac{\lambda^{1-\gamma}}{1-\lambda}\ge \kappa\varphi(\beta)(1-\gamma).
$$

---

**原论文信息**：John R. Birge, Emin Ozyoruk, *Pricing and Capacity Decisions in Platform Competition with Network Externalities*, 2025.


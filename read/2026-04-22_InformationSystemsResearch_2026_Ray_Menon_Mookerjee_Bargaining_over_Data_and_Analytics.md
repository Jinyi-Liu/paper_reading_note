# Bargaining over Data and Analytics: Sellers, Buyers and Consultants

**作者**：Jyotishka Ray（University of Dayton），Syam Menon（The University of Texas at Dallas），Vijay Mookerjee（The University of Texas at Dallas）  
**期刊与年份**：Information Systems Research，2026，Articles in Advance  
**关键词**：Nash bargaining；数据变现；stand-alone data；integrated data product；exclusive contract；nonexclusive contract；consultant；simultaneous negotiation；sequential negotiation

## 中文摘要

这篇文章研究企业如何通过出售数据获利，尤其关注三个常见但在理论上经常被分开处理的问题：第一，数据卖方应该把数据独家卖给一个买方，还是非独家地卖给多个买方？第二，卖方应该只卖原始数据，还是把数据和分析服务打包成一个 data product？第三，如果买方需要外部 consultant 来分析数据，买方应该让 consultant 和卖方一起参与三方谈判，还是先后分别与卖方和 consultant 进行两场双边谈判？

文章建立了一个 Nash bargaining 框架，把数据卖方、数据买方和 analytics consultant 放在同一个谈判结构中分析。核心结论是：卖方即使有分析能力，也不一定应该卖 data product；如果外部 consultant 的能力强，卖方反而可以通过只卖数据来“借用” consultant 创造的价值并在谈判中抽成。反过来，即使卖方的分析能力弱于 consultant，卖方也可能更愿意把数据和分析服务打包出售，因为这样可以避免三方谈判中 bargaining power 被稀释。对于买方而言，三方 simultaneous negotiation 的好处是可以更好地攫取 consultant 的增值贡献，坏处是 consultant 也可能分走一部分数据本身的 intrinsic value。文章进一步分析了非独家销售，给出一个带 reserve value 的 truth-revealing selling rule，并说明卖方什么时候应选择 exclusive contract，什么时候应选择 nonexclusive contracts。

## 论文速览

| 维度 | 内容 |
|:---|:---|
| 核心问题 | 数据卖方如何在“独家 vs. 非独家”“只卖数据 vs. 数据+分析服务”“双边顺序谈判 vs. 三方同时谈判”之间做选择？ |
| 研究对象 | 拥有 proprietary data 的卖方、希望购买数据的买方、可提供 analytics service 的外部 consultant。 |
| 方法 | Cooperative Nash bargaining model；exclusive selling 部分是两方或三方 bargaining；nonexclusive selling 部分是 reserve-value-based mechanism + negotiation。 |
| 数据价值设定 | exclusive 情形下，数据价值 $v \sim U[\bar v-\Delta,\bar v+\Delta]$；consultant 或卖方的 analytics service 按比例提升数据价值。 |
| 核心机制 | 数据价值和分析价值不是简单相加后由谁提供谁拿走，而是被 bargaining power、谈判顺序、outside option 和 contract form 重新分配。 |
| 最反直觉发现 | 卖方可能在自己有分析能力时仍选择只卖数据；也可能在自己分析能力弱于 consultant 时仍选择卖 data product。能力强弱不是唯一决定因素，谈判权力结构同样关键。 |
| 买方关键决策 | 当 consultant 增值足够大，且买方在三方谈判中的 bargaining power 没有显著下降时，买方更偏好 simultaneous negotiation；否则 sequential negotiation 更安全。 |
| 卖方关键决策 | 如果卖方的 analytics capability 高且成本低，data product 更优；如果外部 consultant 的贡献很大且卖方能在谈判中分走这部分贡献，stand-alone data 更优。 |
| 非独家销售结论 | 对每个买方设定 reserve value，只有报告价值超过门槛的买方进入谈判；在 regular distribution 下，卖方收入和 bargaining power 可能相互抵消，从而具有相对效率。 |
| 适用场景 | GDS 向航空公司出售预订数据、医疗数据合作、金融风控数据、零售 panel data、保险风险数据、B2B 数据市场。 |

## TL;DR

这篇文章讲的是：数据不是“有价就卖”那么简单，卖方到底应该只卖数据、卖数据产品，还是卖给一个人或很多人，取决于数据价值和分析价值如何在谈判桌上被分配。最重要的发现是，谁的分析能力更强并不总能决定谁应该提供分析服务，bargaining power 和谈判结构可能改变最优选择。

用最直白的话说：卖方有时应该让外部 consultant 去创造价值，自己只卖数据并在谈判中抽走一部分；有时即使自己分析能力较弱，也应该把分析服务打包进去，避免三方谈判让自己失去议价优势。

## One More Thing

这篇文章最值得记住的洞察是：**consultant 不只是“把数据变得更有用”的技术角色，它还是一个会改变剩余价值分配的战略角色。**

直觉上，买方请 consultant，是为了把买来的数据分析得更好；卖方似乎只需要决定自己会不会也提供分析服务。但文章指出，一旦 consultant 被带到谈判桌上，问题就变了：consultant 创造的 analytics value 会扩大总蛋糕，但 consultant 也可能开始分走数据本身的 intrinsic value。于是，卖方和买方的真实问题不再是“谁分析得更好”，而是“把谁放到谈判桌上，会让谁拿走哪一块蛋糕”。这就是本文区别于一般 bundling 或 data pricing 文章的地方。

## 研究背景与动机

### 实践痛点

企业现在积累大量 proprietary data，但这些数据的商业化路径并不单一。一个数据卖方通常面临三个实际选择。

第一，数据是独家卖给一个买方，还是非独家卖给多个买方？例如，某些医疗或基因数据合作强调 exclusive access，因为买方需要阻止竞争对手获得同类洞察；而 Nielsen 的消费者 panel data 或 Verisk 的保险风险数据则更适合卖给多个客户，通过规模化销售实现收入。

第二，卖方是卖 raw data，还是卖 data product？raw data 对买方的价值往往取决于后续 analytics。许多买方没有足够能力直接分析复杂数据，因此需要 Deloitte、IBM 或其他 analytics consultant 帮助将数据转化为商业决策。

第三，买方如何组织谈判？如果买方既要买数据又要请 consultant，它可以分别和卖方、consultant 谈判，也可以把三方放到同一张谈判桌上。两种结构的总价值可能类似，但分配结果可能完全不同。

### 理论缺口

已有文献分别研究了 information goods pricing、data monetization、auction-based data selling、query-based pricing 和 bundling，但本文认为这些视角不足以解释 B2B 数据市场中的几个关键现实特征。

第一，许多 proprietary data 的交易不是公开竞价或 posted price，而是 negotiation。尤其在数据价值高度不确定、买方数量有限、合同定制化强的 B2B 场景中，bargaining 是自然机制。

第二，analytics service 不是一个外生附属品。它既能提高数据价值，也会改变谈判参与者和剩余分配。

第三，exclusive 与 nonexclusive selling 不只是市场覆盖面的区别。exclusive sale 可能创造更高竞争优势，但 nonexclusive sale 可能通过买方数量弥补单个买方价值较低的问题。

### 核心贡献

1. 本文把 data seller、buyer 和 analytics consultant 放入统一的 Nash bargaining 框架，解释数据价值和分析价值如何在不同谈判结构下分配。
2. 本文同时研究 product design（只卖数据还是 data product）和 contract form（exclusive 还是 nonexclusive），而不是只研究定价。
3. 本文给出买方选择 simultaneous vs. sequential negotiation 的条件，并说明 consultant 的战略角色。
4. 本文为 nonexclusive selling 设计了一个带 reserve value 的 selling rule，并把它与 exclusive bargaining payoff 进行比较。

## 模型设定与假设

### 参与者

| 参与者 | 角色 | 关键决策 |
|:---|:---|:---|
| Seller | 拥有 proprietary data，可选择是否提供 analytics service | 选择 exclusive 或 nonexclusive；在 exclusive 下选择 stand-alone data 或 data product。 |
| Buyer | 购买数据并从中获得业务价值 | 若 seller 只卖数据，则选择 simultaneous negotiation 或 sequential negotiation。 |
| Consultant | 外部 analytics service provider | 在 stand-alone data 情形下为 buyer 分析数据，并通过谈判获得服务费用。 |

### Exclusive contract 中的核心符号

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $v$ | 数据本身对买方的价值 | $v \sim U[\bar v-\Delta,\bar v+\Delta]$。 |
| $\bar v$ | 数据价值均值 | 数据价值的中心水平。 |
| $\Delta$ | 数据价值不确定性的 spread | 越大表示 valuation uncertainty 越高。 |
| $\rho$ | 卖方 outside option | 如果当前谈判失败，卖方可转向其他潜在买方。 |
| $q_S$ | 买方向卖方支付的数据或数据产品价格 | bargaining 的核心决策变量之一。 |
| $q_C$ | 买方向 consultant 支付的 analytics service 价格 | 只在 consultant 参与时出现。 |

### Analytics capability 与成本

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $k_C$ | Consultant 的分析能力 | consultant 增值为 $\delta_C(v)=k_C v$。 |
| $k_S$ | Seller 的分析能力 | seller 自己提供分析时增值为 $\delta_S(v)=k_S v$。 |
| $c_C$ | Consultant 的数据处理成本 | consultant 参与时必须至少覆盖该成本。 |
| $c_S$ | Seller 的数据处理成本 | seller 卖 data product 时承担。 |
| $\delta_C(v)$ | Consultant 创造的增量价值 | $\delta_C(v)=k_C v$。 |
| $\delta_S(v)$ | Seller analytics 创造的增量价值 | $\delta_S(v)=k_S v$。 |

### Bargaining power

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $\alpha$ | simultaneous negotiation 中 seller 的 bargaining power | 三方谈判中 seller 的权重。 |
| $\beta$ | simultaneous negotiation 中 buyer 的 bargaining power | 三方谈判中 buyer 的权重。 |
| $1-\alpha-\beta$ | simultaneous negotiation 中 consultant 的 bargaining power | 三方谈判中 consultant 的权重。 |
| $\gamma$ | seller-buyer 双边谈判中 buyer 的 bargaining power | 因此 seller 的 power 是 $1-\gamma$。 |
| $\kappa$ | buyer-consultant 双边谈判中 buyer 的 bargaining power | 因此 consultant 的 power 是 $1-\kappa$。 |

### Nonexclusive contract 中的符号

| 符号 | 含义 | 备注/描述 |
|:---|:---|:---|
| $i$ | 非独家销售中的第 $i$ 个买方 | 卖方可与多个买方分别谈判。 |
| $F_i(\cdot)$ | 买方 $i$ 的 valuation distribution | 卖方知道分布但不知道买方真实价值。 |
| $f_i(\cdot)$ | 对应密度函数 | 假设 regular distribution。 |
| $v_i$ | 买方 $i$ 的真实价值 | 买方私有信息。 |
| $v_R$ | 买方报告的价值 | 进入 qualification rule。 |
| $x_i(v_R)$ | qualification rule | 报告 $v_R$ 后进入谈判的概率。 |
| $m_i(v_R)$ | negotiation rule | 若进入谈判，双方围绕该价值进行 bargaining。 |
| $r_i$ | reserve value | 最优机制中的谈判保留值。 |
| $\gamma_i$ | nonexclusive bargaining 中 seller 的 bargaining power | 注意这里 $\gamma_i$ 是 seller power，与 exclusive 部分的 $\gamma$ 含义不同。 |

### 决策顺序

1. Seller 首先选择销售模式：exclusive contract 或 nonexclusive contracts。
2. 如果选择 exclusive contract，seller 决定卖 stand-alone data 还是 data product。
3. 如果 seller 卖 stand-alone data，buyer 需要 consultant，并选择谈判结构：
   1. simultaneous negotiation：seller、buyer、consultant 三方同时谈判 $q_S$ 和 $q_C$；
   2. sequential negotiation：buyer 分别与 seller 和 consultant 进行两个双边谈判。
4. 如果 seller 卖 data product，则 seller 和 buyer 直接就 data product 价格谈判。
5. 如果选择 nonexclusive contracts，多个买方分别报告 valuation，卖方用 qualification rule 和 negotiation rule 筛选并谈判。

### 信息结构

Exclusive 部分中，数据价值 $v$ 的分布为 common knowledge，但具体 realized value 在谈判中作为待分配价值进入模型。各方知道或能够合理估计 $k_C$、$k_S$、$c_C$、$c_S$ 和 $\rho$。Nonexclusive 部分中，每个买方知道自己的真实价值，卖方只知道每个买方 valuation 的分布。

### 目标函数与约束：Simultaneous negotiation

如果 seller 只卖 stand-alone data，buyer 可以把 consultant 带入同一场三方谈判。三方共同决定数据价格 $q_S$ 和服务价格 $q_C$。Nash bargaining problem 为：

$$
\max_{q_S,q_C} q_S^{\alpha}\left(v+k_Cv-q_S-q_C\right)^{\beta}\left(q_C-c_C\right)^{1-\alpha-\beta}
$$

subject to

$$
q_S \ge \rho,
$$

$$
q_S+q_C \le v+k_Cv,
$$

$$
q_C \ge c_C.
$$

> 直觉：$q_S$ 是 seller 的 payoff；$v+k_Cv-q_S-q_C$ 是 buyer 支付数据费和咨询费后剩下的净收益；$q_C-c_C$ 是 consultant 扣除成本后的净收益。三个 payoff 按各自 bargaining power 加权相乘，体现 Nash bargaining 中“总剩余如何按谈判权力分配”。约束分别保证 seller 至少拿到 outside option、buyer 不会支付超过总价值、consultant 至少覆盖成本。

### 目标函数与约束：Sequential negotiation

Sequential negotiation 可以理解为两场谈判。第一场是 buyer 和 consultant 谈 analytics service：

$$
\max_{q_C} (k_Cv-q_C)^{\kappa}(q_C-c_C)^{1-\kappa}
$$

subject to

$$
q_C \ge c_C, \quad q_C \le k_Cv.
$$

> 直觉：consultant 创造的 analytics value 是 $k_Cv$。买方和 consultant 只在这部分增量价值上分配，consultant 不能直接分走数据本身的价值 $v$。

由于 buyer 只有在买到数据后才需要 consultant，seller 知道 consultant 谈判产生的 buyer surplus 依赖于数据交易成功。因此 seller 与 buyer 谈判时，实际谈判对象不是单纯的 $v$，而是

$$
v_Q=v+\kappa(k_Cv-c_C).
$$

Seller-buyer 谈判为：

$$
\max_{q_S} q_S^{1-\gamma}(v_Q-q_S)^{\gamma}
$$

subject to

$$
q_S \ge \rho, \quad q_S \le v_Q.
$$

> 直觉：$v_Q$ 是 buyer 买到数据后、再通过 consultant 可获得的有效价值。seller 虽然没有直接提供 analytics service，但可以利用“没有数据就没有 consultant surplus”的依赖关系，从 consultant 创造的价值中间接抽取一部分。

### 目标函数与约束：Seller 卖 data product

如果 seller 自己把数据和 analytics service 打包出售，buyer 不再需要外部 consultant。Nash bargaining problem 为：

$$
\max_{q_S} (q_S-c_S)^{1-\gamma}\left(v+k_Sv-q_S\right)^{\gamma}
$$

subject to

$$
q_S \ge \rho+c_S, \quad q_S \le v(1+k_S).
$$

> 直觉：seller 的 payoff 是 data product 价格扣除处理成本 $c_S$；buyer 的 payoff 是数据加 seller analytics 的总价值扣除支付价格。因为 seller 承担了 analytics cost，所以 outside option effectively 变成 $\rho+c_S$。

### Nonexclusive selling 的机制设计

对于非独家销售，seller 面对多个买方，每个买方的真实价值是私有信息。卖方先设定 qualification rule 和 negotiation rule：买方报告 $v_R$ 后，以概率 $x_i(v_R)$ 进入谈判；如果进入谈判，则围绕 $m_i(v_R)$ 进行 Nash bargaining：

$$
\max_{0\le q_i\le m_i(v_R)} q_i^{\gamma_i}\left(m_i(v_R)-q_i\right)^{1-\gamma_i}.
$$

> 直觉：这相当于“先筛选，再谈判”。买方如果报告价值太低，就没有资格进入谈判；如果通过筛选，谈判的基础价值由卖方规则决定，而不是完全由买方声称的价值决定。这避免了买方永远报告零价值的问题。

## 关键假设

### 假设 1：数据是 proprietary 且具有独特性

合理性：GDS、医疗数据、保险风险数据、平台交易数据往往由特定企业独占收集，短期内难以复制。  
若放松：如果数据有多个替代来源，seller 的 outside option 和 bargaining power 会下降，exclusive premium 也会降低。

### 假设 2：数据收集成本可忽略或已沉没

合理性：许多企业在日常业务中自然生成数据，出售数据时主要成本不是收集，而是处理、清洗、分析和授权。  
若放松：若存在额外数据收集成本 $C$，可将 outside option 调整为 $\rho'=\max\{C,\rho\}$，主要结论不发生根本变化。

### 假设 3：analytics value 与数据价值线性相关

模型设定为 $\delta_C(v)=k_Cv$ 和 $\delta_S(v)=k_Sv$。  
合理性：高价值数据通常也更值得分析，能力更强的分析者能从同一数据中提取更多商业洞察。  
若放松：如果 analytics value 存在递减收益、阈值效应或模块互补性，阈值条件会更复杂，但“分析价值创造”和“谈判剩余分配”之间的张力仍然存在。

### 假设 4：各方能够合理估计 bargaining parameters 和成本

合理性：B2B 合同谈判中，服务范围、成本、outside option 和参与者能力常常通过尽调、历史项目、行业基准和预谈判被大致确认。  
若放松：若 $k_C$、$c_C$ 或 $\rho$ 是 private information，模型会引入 signaling、screening 或 mechanism design 问题，seller 和 buyer 的策略可能更保守。

### 假设 5：Nonexclusive selling 中不考虑 customized analytics

合理性：非独家销售通常面向较多买方，单个买方价值较低，seller 为每个买方定制 analytics service 成本高、难规模化。  
若放松：如果 seller 能低成本提供标准化 analytics dashboard 或 API，nonexclusive data product 可能成为第三种重要模式。

### 假设 6：Exclusive 部分中数据价值服从均匀分布

合理性：均匀分布便于得到清晰 closed-form expected payoff，并突出 bargaining mechanism 而非分布假设。  
若放松：分布形式会改变具体阈值和 expected payoff，但只要价值分布 regular，很多机制直觉仍可保留。

## 分析路线图

文章的逻辑是逐步嵌套的。

第一步，分析 exclusive contract 下的三方 simultaneous negotiation：如果 seller 只卖数据，buyer 把 consultant 带到谈判桌上，三方如何分配数据价值和分析价值？

第二步，分析 exclusive contract 下的 sequential negotiation：如果 buyer 分别和 seller、consultant 谈判，seller 是否还能分享 consultant 的增值贡献？

第三步，分析 seller 卖 data product：如果 seller 自己提供 analytics service，外部 consultant 被排除，seller 和 buyer 如何分配总价值？

第四步，站在 buyer 角度，比较 simultaneous 和 sequential negotiation，回答“买方该不该把 consultant 带到同一张谈判桌上”。

第五步，站在 seller 角度，比较 stand-alone data 和 data product，回答“卖方该不该把分析服务打包进数据产品”。

第六步，分析 social welfare：如果 seller 的 analytics service 不如 consultant，seller 为了私利选择 data product 是否造成社会剩余损失，以及能否通过 bargaining power 调整来协调。

第七步，扩展到 nonexclusive contracts：当卖方可以卖给多个买方时，设计最优筛选和谈判规则，并与 exclusive payoff 比较。

## 核心分析与求解

### Lemma 1：三方 simultaneous negotiation 的均衡

在 seller 只卖 stand-alone data 且 buyer 将 consultant 带入三方谈判时，如果 outside option 不绑定，即

$$
\rho < \alpha\left((1+k_C)v-c_C\right),
$$

则均衡价格为：

$$
q_S^*=\alpha\left((1+k_C)v-c_C\right),
$$

$$
q_C^*=(1-\alpha-\beta)\left((1+k_C)v-c_C\right)+c_C.
$$

如果 outside option 较高但仍不超过总有效价值，则 seller 拿到 $\rho$，buyer 和 consultant 分配剩余；如果 outside option 超过有效价值，则谈判失败。

> 经济直觉：三方谈判中的有效蛋糕是 $v+k_Cv-c_C$。seller 不只是从数据本身 $v$ 中拿钱，而是能按 $\alpha$ 的权重分享 consultant 创造的 analytics value。与此同时，consultant 也不只是拿 analytics surplus，它能按 $1-\alpha-\beta$ 的权重分享数据本身的 intrinsic value。这是 simultaneous negotiation 的核心特征：价值来源和价值分配对象不完全一致。

这一结果建立了三方谈判的基准。接下来，文章问：如果 consultant 不在数据购买谈判中，剩余分配会如何变化？

### Lemma 2：Sequential negotiation 的均衡

在 sequential negotiation 中，buyer 和 consultant 先后或条件性地谈 analytics service，均衡咨询费为：

$$
q_C^*=(1-\kappa)(k_Cv-c_C)+c_C.
$$

Buyer 从 consultant 创造的净增值中获得：

$$
\kappa(k_Cv-c_C).
$$

因此 seller-buyer 谈判中的有效价值变成：

$$
v_Q=v+\kappa(k_Cv-c_C).
$$

当 outside option 不绑定时，seller 获得：

$$
q_S^*=(1-\gamma)\left(v(1+\kappa k_C)-\kappa c_C\right).
$$

> 经济直觉：sequential negotiation 把 consultant 排除在数据购买谈判之外，因此 consultant 不能直接分享数据本身的价值 $v$。但是 seller 仍然能间接分享 analytics value，因为 buyer 只有在买到数据后才会获得 consultant 服务带来的收益。seller 利用这种依赖关系，把 buyer 未来从 consultant 那里获得的一部分 surplus 纳入当前数据价格。

有了两种 stand-alone data 的谈判结构后，文章进一步分析 seller 如果自己提供 analytics service 会怎样。

### Lemma 3：Seller 卖 data product 的均衡

如果 seller 将数据和自己的 analytics service 打包出售，外部 consultant 不参与。有效价值为 $v+k_Sv-c_S$。当 outside option 不绑定时，均衡 data product 价格为：

$$
q_S^*=(1-\gamma)\left(v(1+k_S)-c_S\right)+c_S.
$$

seller 的净收益为：

$$
q_S^*-c_S=(1-\gamma)\left(v(1+k_S)-c_S\right).
$$

buyer 的收益为：

$$
\gamma\left(v(1+k_S)-c_S\right).
$$

> 经济直觉：data product 把 consultant 完全排除，因此 seller 不用与 consultant 分享剩余，也不会让 consultant 分走 intrinsic data value。但代价是，seller 自己的 analytics capability $k_S$ 和成本 $c_S$ 决定了总蛋糕大小。如果 seller 的分析能力弱或成本高，打包可能缩小总蛋糕。

现在可以进入买方决策：当 seller 只卖数据时，buyer 应该选择 simultaneous 还是 sequential？

### Proposition 1：Buyer 的谈判结构选择

文章比较 buyer 在 simultaneous negotiation 和 sequential negotiation 下的 expected payoff。结论可概括为：

当 buyer 在三方谈判中的 bargaining power 仍然足够强，即 $\beta>\gamma\kappa$，且 consultant 的能力 $k_C$ 足够高时，buyer 更偏好 simultaneous negotiation。

当 buyer 在三方谈判中的 bargaining power 下降较多，即 $\beta<\gamma\kappa$，且 seller 在三方谈判中的 power 不太高时，buyer 更偏好 sequential negotiation。

论文中的精确条件涉及一个三次方程最大实根 $x_l$。简化理解是，buyer 比较的是 simultaneous 相对 sequential 多支付的总金额。文章给出的核心差额可写成：

$$
(\delta_C(v)-c_C)(\gamma\kappa-\beta)+v(\gamma-\beta).
$$

如果这个值为正，simultaneous negotiation 对 buyer 来说更贵，因此 sequential negotiation 更有吸引力。

> 经济直觉：三方谈判的好处是 buyer 可以在同一场谈判中更充分地利用 consultant 创造的总价值，尤其当 consultant 很强时，总蛋糕显著变大。但坏处是 consultant 进入谈判桌后会分享一部分数据本身的价值，而且 buyer 的相对 bargaining power 往往会下降。因此，simultaneous negotiation 适合“consultant 很强、buyer 的三方谈判权力没有被严重稀释”的情形；sequential negotiation 适合“buyer 在双边谈判中更强、三方谈判会让自己失势”的情形。

在 buyer 的选择给定后，seller 才能判断自己应该卖 stand-alone data 还是 data product。

### Proposition 2：Seller 的 product design 选择

Seller 的选择取决于 buyer 最终会采用哪种谈判结构。

如果 buyer 会选择 sequential negotiation，seller 比较 stand-alone data 下的收益 $U_S^Q$ 和 data product 下的收益 $U_S^C$。当 seller 的 analytics capability $k_S$ 超过某个阈值时，seller 卖 data product；否则卖 stand-alone data。

如果 buyer 会选择 simultaneous negotiation，seller 比较 stand-alone data 下的收益 $U_S^M$ 和 data product 下的收益 $U_S^C$。同样，当 $k_S$ 超过相应阈值时，seller 卖 data product；否则卖 stand-alone data。

论文用两个阈值 $y-1$ 和 $z-1$ 表示上述条件：

$$
k_S>y-1 \quad \Rightarrow \quad \text{在 sequential 对比下卖 data product},
$$

$$
k_S>z-1 \quad \Rightarrow \quad \text{在 simultaneous 对比下卖 data product}.
$$

> 经济直觉：卖方不是简单比较 $k_S$ 和 $k_C$。即使 consultant 的分析能力更强，seller 也可能因为三方谈判中 bargaining power 被稀释而选择自己打包服务。反过来，即使 seller 有一定分析能力，如果 consultant 创造的价值很大且 seller 能通过谈判分享这部分价值，那么 seller 可能更愿意只卖数据，让 consultant 去扩大蛋糕。

Proposition 2 给出一般阈值后，文章进一步给出一个更容易操作的 sufficient condition。

### Corollary 1：Seller 卖 data product 的充分条件

如果

$$
k_S>k_C
$$

且

$$
c_S<\kappa c_C,
$$

则 seller 选择卖 data product 优于卖 stand-alone data。

> 经济直觉：如果 seller 的分析能力比 consultant 更强，并且 seller 的处理成本足够低，那么打包数据和分析服务几乎一定更好。这个条件的有趣之处在于，它不需要精确估计 bargaining power。只要 seller 在能力和成本上有明显优势，product bundling 就是稳健选择。

这里出现本文一个关键 trade-off：**data product 可以避免 consultant 分走剩余，但可能缩小总蛋糕；stand-alone data 可以借助 consultant 扩大总蛋糕，但会改变剩余分配。**

### Figure-based insight：bargaining power 为什么会改变“谁该提供分析服务”

论文 Figure 2 展示 seller bargaining power 对选择的影响。图的含义可以概括为三点。

第一，当 seller 的 analytics capability 较高时，data product 基本占优。  
第二，当 seller 的 analytics capability 低于 consultant 但仍有竞争力时，如果 simultaneous negotiation 会显著降低 seller 的 bargaining power，seller 仍可能选择 data product。  
第三，当 consultant 的增值贡献非常大，且 seller 在 simultaneous negotiation 中可以保持较高 $\alpha$ 时，seller 反而更愿意只卖数据，让 consultant 把蛋糕做大。

Figure 3 展示 $\Delta$ 增加会降低 seller 和 buyer 的 expected payoff。也就是说，valuation uncertainty 越大，双方越难从交易中获得高收益。

> 经济直觉：价值不确定性不是中性的噪声。它会降低双方期望收益，因此卖方和买方都有动机通过 demonstration、pilot study、data audit 或 consultant due diligence 来降低 valuation uncertainty。

## Social welfare extension

文章进一步考虑一种社会效率问题：如果外部 consultant 的净增值更高，即

$$
\delta_C(v)-c_C>\delta_S(v)-c_S,
$$

那么 seller 为了自身利润选择卖 data product，会减少社会总剩余。损失为：

$$
(\delta_C(v)-c_C)-(\delta_S(v)-c_S).
$$

### Sequential coordination

在 sequential negotiation 中，如果 consultant 最终只获得等于上述剩余差额的 payoff，则系统可以达到无效率损失的协调结果。对应条件是 buyer 在 buyer-consultant 谈判中的 bargaining power 至少满足：

$$
\kappa \ge \frac{\delta_S(v)-c_S}{\delta_C(v)-c_C}.
$$

> 经济直觉：要让 consultant 参与但不拿走过多剩余，需要 buyer 有足够 bargaining power 压低 consultant 的分成。consultant 虽然比在普通 sequential negotiation 中拿得少，但仍比 seller 直接卖 data product 时拿零更好。

### Simultaneous coordination

在 simultaneous negotiation 中，为了避免社会剩余损失，buyer 和 seller 的 combined bargaining power 需要足够高：

$$
\alpha+\beta \ge \frac{v+\delta_S(v)-c_S}{v+\delta_C(v)-c_C}.
$$

> 经济直觉：三方谈判中 consultant 会分享总剩余。要让 consultant 只拿到“必须给它的那部分”而不是过多分走 intrinsic data value，需要 seller 和 buyer 合计拥有足够强的 bargaining power。

## Nonexclusive contracts

Exclusive analysis 之后，文章转向 nonexclusive selling。这里 seller 可以把同一数据卖给多个买方，但每个买方的单独 valuation 较低，而且 customized analytics 不现实。因此模型只考虑数据销售，不考虑 seller 为每个买方提供定制 analytics。

### 最优 qualification rule 与 negotiation rule

对买方 $i$，seller 知道 valuation distribution $F_i$ 和 $f_i$，但不知道真实价值。最优机制可以用 reserve value $r_i$ 表示：

$$
x_i(v_R)=
\begin{cases}
0, & v_R<\gamma_i r_i,\\
1, & v_R\ge \gamma_i r_i,
\end{cases}
$$

且

$$
m_i(v_R)=r_i.
$$

最优 reserve value 满足：

$$
\gamma_i r_i^*=\frac{1-F_i(\gamma_i r_i^*)}{f_i(\gamma_i r_i^*)}.
$$

seller 的期望收益为：

$$
U_S=\gamma_i r_i^*\left(1-F_i(\gamma_i r_i^*)\right).
$$

在最优条件下也可写作：

$$
U_S=(\gamma_i r_i^*)^2 f_i(\gamma_i r_i^*).
$$

> 经济直觉：买方如果知道自己低报也能谈判，就会报告零。reserve-value mechanism 的作用是让低报告者无法进入谈判。只有报告价值超过门槛的买方才能谈，谈判基础则固定为 $r_i$。这样 seller 把“筛选真实高价值买方”和“谈判分配剩余”分成两个阶段处理。

### Lemma 4：三类分布下的 reserve value

对于 regular distributions，文章给出 Uniform、Exponential 和 Weibull 三类分布的最优 reserve value。最直观的是 uniform case。若

$$
v_i \sim U[0,\bar v_i],
$$

则：

$$
r_i^*=\frac{\bar v_i}{2\gamma_i},
$$

且 seller 对每个买方的期望收益为：

$$
U_S^*=\frac{\bar v_i}{4}.
$$

> 经济直觉：看似 seller bargaining power $\gamma_i$ 越高越能拿更多钱，但最优 reserve value 会随 $\gamma_i$ 下降。高 bargaining power 提高谈判中可抽取比例，同时也提高有效进入门槛、减少参与概率。对于 regular distributions，这两个效应可以相互抵消，因此卖方期望收益对 bargaining power 呈现独立性。这是 nonexclusive 部分一个很干净的机制发现。

### Exclusive vs. Nonexclusive

在 uniform illustration 中，假设有 $n$ 个 nonexclusive buyers，且每个买方价值独立同分布于 $U[0,U]$。Nonexclusive selling 的总期望收益为：

$$
\frac{nU}{4}.
$$

Seller 将其与 exclusive contract 下三种可能收益比较：

$$
U_S^M \quad \text{simultaneous stand-alone data},
$$

$$
U_S^Q \quad \text{sequential stand-alone data},
$$

$$
U_S^C \quad \text{data product}.
$$

决策原则很直接：如果相应 exclusive payoff 高于 $nU/4$，选择 exclusive；否则选择 nonexclusive。

> 经济直觉：exclusive contract 的优势来自单个买方的高价值、竞争优势和 analytics value；nonexclusive contracts 的优势来自买方数量和规模化销售。即使单个 nonexclusive buyer 的价值较低，只要 $n$ 足够大或 $U$ 足够高，nonexclusive selling 就可能胜出。反过来，如果 exclusive buyer 的基础价值或 analytics 增值很高，exclusive 仍可能优于 nonexclusive。

## 比较静态汇总表

| 参数变化 | 直接影响 | 对策略选择的含义 | 直觉 |
|:---|:---|:---|:---|
| $\alpha \uparrow$ | seller 在三方 simultaneous negotiation 中分得更多 | seller 更可能愿意只卖 stand-alone data 并让 consultant 参与 | seller 能分享 consultant 扩大后的蛋糕。 |
| $\beta \uparrow$ | buyer 在三方 simultaneous negotiation 中分得更多 | buyer 更可能选择 simultaneous negotiation | buyer 被三方谈判稀释的风险下降。 |
| $\gamma \uparrow$ | buyer 在 seller-buyer 双边谈判中更强，seller power $1-\gamma$ 下降 | sequential negotiation 和 data product 下 seller 收益下降；buyer 更偏好双边结构 | buyer 在双边谈判中越强，越不愿进入可能稀释权力的三方谈判。 |
| $\kappa \uparrow$ | buyer 在 buyer-consultant 谈判中获得更多 analytics surplus | sequential negotiation 对 buyer 更有吸引力；seller 也可间接抽取更多 buyer analytics surplus | consultant 创造的净价值更多先落到 buyer 手里，再被 seller 部分分享。 |
| $k_C \uparrow$ | consultant 创造更高 analytics value | simultaneous negotiation 更可能吸引 buyer；stand-alone data 对 seller 可能更好 | consultant 把总蛋糕做大，但也会要求分成。 |
| $k_S \uparrow$ | seller 的 data product 价值提高 | seller 更可能卖 data product | 打包服务的总蛋糕变大，排除 consultant 的机会成本下降。 |
| $c_C \uparrow$ | consultant 净增值下降 | buyer 更不愿依赖 consultant；seller 更可能倾向 data product | 外部分析服务变贵，stand-alone data 的吸引力下降。 |
| $c_S \uparrow$ | seller 打包成本上升 | data product 吸引力下降 | seller 自己提供 analytics 的净剩余减少。 |
| $\rho \uparrow$ | seller outside option 更高 | seller 的最低可接受价格提高；过高时交易可能失败 | outside option 既提高 seller 议价底线，也可能让 buyer 无法接受。 |
| $\Delta \uparrow$ | 数据价值不确定性提高 | seller 和 buyer 的 expected payoff 均下降 | 不确定性降低交易双方对剩余的可预期分配。 |
| $n \uparrow$ | nonexclusive buyers 数量增加 | nonexclusive contracts 更有吸引力 | 多买方规模化弥补单个买方价值较低。 |
| $U \uparrow$ | nonexclusive buyer 的 valuation 上界提高 | nonexclusive revenue $nU/4$ 上升 | 多个非独家买方的总收入潜力上升。 |
| $\bar v \uparrow$ | exclusive buyer 的平均数据价值上升 | exclusive contract 更有吸引力 | 单个独家交易的基础蛋糕变大。 |

## 主要结论与管理启示

### 与常见 benchmark 的对比

| Benchmark 思维 | 本文揭示的新机制 |
|:---|:---|
| 谁 analytics capability 更高，就应该由谁提供分析服务 | 不一定。能力决定总蛋糕大小，bargaining structure 决定谁分到蛋糕。低能力 seller 也可能因避免三方谈判权力稀释而卖 data product。 |
| 卖方有分析能力就应该卖 data product | 不一定。如果 consultant 能显著扩大总价值，且 seller 能分走 consultant 增值，stand-alone data 可能更好。 |
| 买方请 consultant 只是技术问题 | 不对。consultant 是否进入谈判桌会改变 intrinsic data value 和 analytics value 的分配。 |
| Exclusive 一定比 nonexclusive 更有价值，因为独家有竞争优势 | 不一定。nonexclusive 的买方数量和规模化收入可能超过 exclusive premium。 |
| Bargaining power 越高，卖方在 nonexclusive 中收入越高 | 在最优 reserve rule 下不一定。更高 bargaining power 会降低 reserve value，参与门槛和分成比例的变化可能抵消。 |

### 对 seller 的建议

1. 不要只根据自身 analytics capability 决定是否卖 data product。应同时评估：$k_S$、$c_S$、外部 consultant 的 $k_C$、$c_C$、三方谈判中的 $\alpha$，以及双边谈判中的 $1-\gamma$。
2. 如果自身 analytics capability 高且成本低，data product 是稳健策略，尤其当 $k_S>k_C$ 且 $c_S<\kappa c_C$ 时。
3. 如果外部 consultant 能大幅提高数据价值，而 seller 在三方谈判中仍有较强 bargaining power，可以只卖 stand-alone data，通过谈判分享 consultant 创造的增值。
4. 如果三方谈判会显著削弱 seller 的 bargaining power，即使 seller 的 analytics capability 低于 consultant，也可能应选择 data product。
5. 当潜在买方数量多且每个买方虽价值较低但分布上界 $U$ 不低时，应认真考虑 nonexclusive selling。
6. Seller 和 buyer 都应投资于降低 valuation uncertainty 的机制，如 data preview、proof-of-concept、pilot analysis、trusted third-party audit 或标准化质量指标，因为 $\Delta$ 上升会降低双方收益。

### 对 buyer 的建议

1. 当 consultant 能创造很高增值且 buyer 在三方谈判中仍有足够 bargaining power 时，把 consultant 带入 simultaneous negotiation 可能更好。
2. 如果 buyer 在双边谈判中更有优势，而三方谈判会让 consultant 和 seller 分走更多价值，应选择 sequential negotiation。
3. Buyer 应意识到，consultant 进入三方谈判后可能不只是收服务费，还会分走数据本身的价值。
4. 在购买 data product 时，buyer 应比较 seller analytics 的净增值 $k_Sv-c_S$ 与外部 consultant 的净增值 $k_Cv-c_C$，避免为低质量 bundling 支付过高价格。

### 对 consultant 的建议

1. Consultant 的价值不只体现在技术能力 $k_C$，也体现在能否成为谈判中不可或缺的参与者。
2. 如果 consultant 进入 simultaneous negotiation，可能获得比单纯服务费更高的份额，因为它有机会分享数据本身的价值。
3. 但如果 seller 和 buyer combined bargaining power 很强，consultant 可能只能拿到刚好足以参与的剩余。

## 与相关文献的对话

### Ray, Menon, and Mookerjee (2020)

共同点：两篇文章都研究数据销售中的 bargaining，尤其关注 proprietary data 和 exclusive contract。  
区别：2020 年文章关注 seller 是否应通过 data demonstration 降低 buyer valuation uncertainty，以及如何设计信号机制；本文则加入 consultant、data product bundling 和 nonexclusive selling。  
重要性：本文把“数据如何卖”从信息披露问题扩展为“合同形式、产品设计和谈判结构”的联合决策。

### Mehta et al. (2021)

共同点：都研究 data monetization 和数据卖方如何设计销售机制。  
区别：Mehta et al. 关注 price-quantity mechanism，允许买方筛选感兴趣 records；本文关注 B2B negotiation，强调 bargaining power、outside option 和 consultant 的作用。  
重要性：在 posted-price 或 mechanism design 难以适用的定制化数据交易中，本文的 bargaining 视角更贴近实践。

### Bakos and Brynjolfsson (1999, 2000)

共同点：都研究 information goods bundling，说明 bundling 可以改变利润和竞争格局。  
区别：经典 bundling 文献通常把 bundle 作为卖方定价对象；本文把 bundling 放入 bargaining 环境，并引入外部 consultant 作为替代 analytics provider。  
重要性：本文显示 bundling 的价值不仅来自需求聚合或估值平滑，也来自改变谈判参与者和剩余分配。

### Myerson (1981)

共同点：nonexclusive 部分借鉴 optimal auction design 中 reserve price 的思想。  
区别：本文不是标准 auction，而是“qualification stage + negotiation stage”。reserve value 不直接等于成交价，而是进入后续 bargaining。  
重要性：这使 mechanism design 与 B2B negotiation 结合起来，解释非独家数据销售中如何筛选买方并保持激励相容。

### Bergemann and Bonatti (2015) / Bergemann, Bonatti, and Gan (2022)

共同点：都关注数据作为经济商品的销售和数据精度、数据规模、竞争之间的关系。  
区别：这些研究更强调数据对 downstream pricing 和 competition 的影响；本文强调数据交易本身的 bargaining structure。  
重要性：本文补充了一个微观交易层面的视角：即使数据总价值给定，谈判结构也会决定数据市场能否有效运作。

## Reviewer's Critique

### 优点

理论贡献清晰。文章把 exclusive/nonexclusive、data/data product、simultaneous/sequential negotiation 放入统一框架，形成一个很完整的 data monetization strategy model。

机制有辨识度。最有价值的地方不是推导 Nash bargaining 本身，而是揭示 consultant 会同时改变 value creation 和 value appropriation。

管理启示强。文章给出的建议不要求企业精确估计所有 bargaining power，而是通过相对条件和阈值判断策略方向，这对实践更友好。

### 模型限制与假设过强之处

第一，analytics value 被设定为 $\delta_j(v)=k_jv$，较为线性和光滑。现实中 analytics 可能存在固定投入、递减收益、数据模块互补性或任务特定性。例如，某些数据只有在 consultant 拥有特定行业知识时才有高价值，而不是简单由 $k_j$ 放大。

第二，模型假设各方能够合理估计 $k_C$、$c_C$、$k_S$、$c_S$ 和 $\rho$。现实中 consultant 的真实能力、seller 数据质量和 buyer 的实际使用场景往往高度不透明。若引入 asymmetric information，买方可能低估数据，seller 可能夸大数据质量，consultant 也可能夸大服务能力。

第三，exclusive 部分基本是 one-shot bargaining。许多数据合作是长期关系，包括数据持续更新、模型持续迭代、服务水平协议、续约和声誉机制。重复博弈可能改变 outside option 和 bargaining power。

第四，nonexclusive 部分排除了 analytics service 和买方之间的 downstream competition。现实中多个买方使用同一数据后，数据价值会因竞争者也能使用而下降，而且不同买方之间可能存在 strategic externalities。

第五，seller 的 outside option 被外生化处理。若多个 exclusive buyers 同时竞争，outside option 应该由市场结构、买方竞争强度和 auction/negotiation design 内生决定。

第六，文章没有显式建模隐私、合规、数据泄露风险和数据使用权边界。对于医疗、金融、保险等数据市场，这些约束可能决定交易可行性和 contract form。

### 未来研究方向

1. 将 data demonstration 与 consultant due diligence 结合起来，研究 seller、buyer 和 consultant 如何共同降低 valuation uncertainty，以及谁应支付验证成本。
2. 引入多个 competing consultants，分析 consultant market competition 如何影响 seller 的 data product strategy。
3. 建立 repeated data access model，考虑数据会随时间更新、价值会衰减、合同可续约或重新谈判。
4. 在 nonexclusive selling 中加入 downstream competition，研究同一数据被多个买方使用时如何降低个体价值，以及 seller 是否应限制买方数量。
5. 引入 privacy regulation 和用户授权成本，研究数据卖方是否应在 raw data、aggregated data、synthetic data 和 analytics-only service 之间选择。
6. 将 bargaining power 内生化，例如由搜索成本、法律权利、数据稀缺性、声誉、平台锁定或买方替代数据源决定。

## 这篇文章到底做了什么

如果只用一段话复盘：本文构建了一个数据交易的 bargaining model，解释数据卖方在 exclusive vs. nonexclusive、stand-alone data vs. data product 之间如何选择；同时解释买方在需要 analytics consultant 时，应选择三方 simultaneous negotiation 还是两个 sequential bilateral negotiations。文章的核心不是“数据值多少钱”，而是“数据价值和分析价值在不同谈判结构中会被谁拿走”。因此，它把 data monetization 从定价问题推进为一个合同设计、产品设计和谈判结构共同决定的战略问题。

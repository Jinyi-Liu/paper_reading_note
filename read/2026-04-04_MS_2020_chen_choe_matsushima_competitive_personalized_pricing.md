# Competitive Personalized Pricing

作者：Zhijun Chen（Monash University, Department of Economics）；Chongwoo Choe（Monash University, Department of Economics；Centre for Global Business）；Noriaki Matsushima（Osaka University, Institute of Social and Economic Research）  
发表年份：2020  
期刊：*Management Science*，66(9), 4003–4023

中文摘要：

本文研究一个竞争市场：每家企业都拥有一块“目标客群”，在这块人群上企业掌握完整消费者信息，因此可以实施 personalized pricing；与此同时，消费者也可能通过删除 cookie、切换账号、伪装新客、比较公开价格等方式进行 identity management，从而绕过企业的个性化定价。文章表明：如果消费者是被动的，更多消费者信息会加剧竞争，因为企业可以更精准地“保卫地盘”和“挖角”；但如果消费者会主动进行 identity management，这一效应会被显著削弱，甚至反转。原因在于，企业若用很低的公开价格去挖对手客户，也会把自己原本被个性化高价锁定的目标客户一并吸引过来，从而提高挖角成本。结果是：当目标客群足够大且彼此不重叠时，主动型消费者反而可能让企业对各自目标客户实施 perfect price discrimination，榨取消费者全部剩余；当中间的共同非目标市场很小时，企业甚至可能选择放弃服务这部分消费者，造成 deadweight loss。文章进一步证明：无论是只有一部分消费者主动管理身份，还是主动管理身份存在成本，核心结论都保持不变，并据此讨论了隐私监管与消费者赋权的政策含义。

## 论文速览

| 维度 | 内容 |
| --- | --- |
| 研究问题 | 当企业能对“已识别”的消费者实施个性化定价时，如果消费者能够通过 identity management 绕开这种定价，竞争会如何变化？企业利润、消费者剩余和社会福利会如何受影响？ |
| 研究方法 | Hotelling 线性城市模型；两家企业；分阶段定价博弈；比较 passive consumers 与 active consumers 两种情形；再做一系列 extensions。 |
| 核心机制 | 个性化定价本来会增强“保卫本方客户、挖对手客户”的能力；但 active consumers 会让公开低价同时吸引本企业自己的目标客户，因此抬高挖角成本，软化竞争。 |
| 关键发现 | passive consumers 下，更多信息会加剧竞争并压低利润；active consumers 下，企业可能通过高公开价 + 精准个性化价实现 perfect price discrimination，甚至放弃一部分非目标消费者。 |
| 主要贡献 | 把消费者端的 identity management 显式引入竞争性 personalized pricing；推翻“更多信息必然加剧竞争”的经典直觉；揭示消费者主动保护自己可能反而伤害消费者整体福利。 |
| 适用场景 | 电信、银行、保险、流媒体、平台零售、会员制服务、new-customer-only discount、市调与数据经纪人支持的精准营销场景。 |
| 一句话定位 | 这篇文章最重要的价值，是把“消费者会反制定价算法”这个现实行为放进标准竞争模型后，发现竞争逻辑会发生方向性的翻转。 |

## TL;DR

这篇文章的最直白结论是：消费者越会“躲开”个性化定价，企业之间未必竞争得更凶，反而可能竞争得更温和。原因是企业一旦用公开低价去抢对手客户，也会把自己原本能高价卖出的老客户一起吸走。结果就是，消费者自我保护未必让消费者整体受益，反而可能让企业赚得更多、消费者剩余更低，甚至带来效率损失。

## One More Thing

这篇文章最值得在 seminar 上抛出来的洞察是：**“消费者反抗 personalized pricing” 并不一定是 pro-consumer 的。** 直觉上，消费者删除 cookie、切换账号、装作新客，似乎是在削弱企业的剥削能力；但在这个模型里，这种行为同时也削弱了企业“用公开低价挖人”的能力。于是，企业不再愿意把公开价格打得很低，竞争被软化，最后每家企业都能更安心地在自己的目标客群里做更强的 surplus extraction。换句话说，消费者个体的自保行为，可能通过竞争结构这一中介，制造出一个典型的 collective-action paradox：每个消费者都想占便宜，但所有消费者加总起来反而让企业更容易赚钱。

## 研究背景与动机 (Motivation)

### 实践痛点

文章的现实出发点非常强。作者指出，大数据、数据经纪人和在线行为追踪让企业越来越容易获得个人层面的消费者信息，并据此做更细颗粒度的优惠和定价。例如，Coupons.com 会用行为数据做更细致的 coupon targeting；Safeway 的 “Just for U” 会基于购买记录给出个性化优惠；Uber 也曾出现基于预期 willingness to pay 的 route-based pricing 讨论。文中还引用了一个很扎眼的数据：据 TRUSTe 报告，最常用的 100 个网站背后有超过 1,300 家公司在监测用户行为。现实世界里的另一个典型场景是“只给新客户优惠”：银行、保险、电信、付费电视、能源服务中都常见此类做法。

但消费者并不是坐以待毙。很多人会删除或屏蔽 cookie、使用 VPN、切换账号、装作新客，或者先去搜索更便宜的报价再回来议价。作者把这些统称为 identity management。它们共同指向一个现实难题：企业的 personalized pricing 技术在进步，消费者绕开的技术和策略也在进步。

### 理论缺口

理论上，competitive price discrimination 的经典结论是：更精细的信息通常会让竞争更激烈，因为企业更能精确打击边际消费者，也更能逐个消费者地保卫地盘。Thisse and Vives (1988)、Chen and Iyer (2002)、Zhang (2011)、Choe et al. (2018) 这一脉络都大体支持“更多信息 → 更强个性化定价 → 更激烈竞争”的基本逻辑。

问题在于，这些模型大多默认消费者是被动的：企业给什么价，消费者就只能在可见的价单中选。相比之下，关于 identity management 的文献更多讨论 monopoly，尤其是 ex ante 或 interim identity management。真正把 **ex post identity management**——也就是消费者在观察到 personalized offer 之后再决定是否伪装、是否改身份、是否转去公开价——放进 duopoly personalized pricing 模型中的工作并不多。这恰恰是本文的切入点。

### 核心贡献

1. 把消费者端的 ex post identity management 显式放进竞争性个性化定价模型，展示其如何系统性改变竞争结果。
2. 证明“更多消费者信息必然加剧竞争”只在消费者被动时成立；只要消费者足够主动，这一结论会被推翻。
3. 揭示消费者会面对一个 prisoner’s dilemma：个体变主动可能受益，但总体上更多主动消费者会让所有消费者更差。
4. 给出隐私政策与消费者赋权的细致含义：限制数据使用、增强消费者控制权，并不总是自动提升消费者福利。

## 模型设定与假设 (Model Setup & Assumptions)

### 符号体系一：消费者与偏好

| 符号 | 含义 | 备注/描述 |
| --- | --- | --- |
| \(l\) | 消费者 brand loyalty | \(l \in [-1/2,1/2]\)，均匀分布；越大越偏好品牌 \(A\)，越小越偏好品牌 \(B\)。 |
| \(V_A(l)\) | 消费者购买 \(A\) 的 gross value | \(V_A(l)=1+l/2\)。 |
| \(V_B(l)\) | 消费者购买 \(B\) 的 gross value | \(V_B(l)=1-l/2\)。 |
| \(x\) | 位于 \(A\) 一侧、由 \(A\) 目标化的消费者 | 通常 \(x\in[a,1/2]\)。 |
| \(y\) | 位于 \(B\) 一侧、由 \(B\) 目标化的消费者 | 通常 \(y\in[-1/2,b]\)。 |

> 直觉上，模型把标准 Hotelling 位置变量解释为“品牌忠诚度”。消费者并不是简单喜欢左端点或右端点，而是对两个品牌有不同强度的偏好差异。这样一来，个性化定价的“挖角”和“保卫地盘”都能写得非常直接。

### 符号体系二：信息结构与市场分割

| 符号 | 含义 | 备注/描述 |
| --- | --- | --- |
| \(a\) | \(A\) 的目标客群左边界 | \(A\) 的目标段为 \([a,1/2]\)。 |
| \(b\) | \(B\) 的目标客群右边界 | \(B\) 的目标段为 \([-1/2,b]\)。 |
| \(N_A\) | \(A\) 的 noncontestable targeted consumers | \(N_A=[\max\{0,a\},1/2]\)。 |
| \(N_B\) | \(B\) 的 noncontestable targeted consumers | \(N_B=[-1/2,\min\{b,0\}]\)。 |
| \(\delta\) | 对称特例中的分割参数 | 例如 \(a=b=\delta\) 表示 fully targeted without overlap；\(a=-b=\delta>0\) 表示中间有一段共同非目标市场。 |

> \(a\) 与 \(b\) 决定了“谁知道谁”的范围。若 \(a\le b\)，则两家企业目标客群覆盖整个市场，且可能有 overlap；若 \(a>b\)，则 \([b,a]\) 这段消费者不被任何一方目标化。

### 符号体系三：价格与扩展参数

| 符号 | 含义 | 备注/描述 |
| --- | --- | --- |
| \(q_A,q_B\) | 面向非目标消费者的 uniform prices | 第一阶段公开选择。 |
| \(p_A(x),p_B(y)\) | 个性化价格 | 第二阶段针对目标客群私下给出。 |
| \(\alpha\) | active consumers 的占比 | 扩展中 \(\alpha\in[0,1]\)。 |
| \(c\) | identity management 的成本 | 扩展中消费者变主动需支付的成本。 |
| \(\gamma\) | targeting 的边际成本 | 扩展中企业内生选择目标段时使用。 |

### 博弈 / 决策结构

**Players.** 两家企业 \(A,B\)；一群连续分布的消费者。  
**Sequence of Events.**

1. 企业先公开选择 uniform prices \(q_A,q_B\) 面向非目标消费者。
2. 企业再对各自目标客群选择 personalized prices \(p_A(x),p_B(y)\)。
3. 消费者观察到公开价格与自己可见的 personalized offer 后，决定购买哪家，或在扩展中是否进行 identity management。
4. 在扩展 5.3 中，企业还会在定价之前选择目标段 \((a,b)\)。

**Information Structure.**

- \(q_A,q_B\) 是公开可见的。
- 每个 personalized price 只被对应目标消费者观察到。
- \(a,b\) 被视为公共信息。
- passive consumers 不能拿到“本来不给自己看的公开价”；active consumers 可以通过身份管理绕过这一限制。

### 目标函数与约束

消费者的一般效用可写为
\[
U_A(l)=V_A(l)-\text{price paid to }A,\qquad
U_B(l)=V_B(l)-\text{price paid to }B.
\]

对于 **passive consumer** 而言，若 \(x\) 仅被 \(A\) 目标化，则他只会在
\[
U_A(x)=1+\frac{x}{2}-p_A(x),\qquad
U_B(x)=1-\frac{x}{2}-q_B
\]
之间比较。

> 这意味着：企业 \(A\) 可以用 personalized price 精确“保住”自己的目标消费者，因为该消费者无法回头拿到 \(A\) 给非目标用户的公开价 \(q_A\)。

对于 **active consumer** 而言，若 \(x\) 仅被 \(A\) 目标化，则他会在
\[
1+\frac{x}{2}-p_A(x),\qquad 1+\frac{x}{2}-q_A,\qquad 1-\frac{x}{2}-q_B
\]
之间择优。

> 这一步是全文的灵魂。只要消费者能看到自己企业对外公开的低价，企业就无法再把“挖角价”和“防守价”完全分开。公开低价不仅会吸引对手客户，也会吞掉自己原本可以高价卖给老客户的生意。

企业的利润可概括写为
\[
\pi_A = q_A D_A^{U} + \int_a^{1/2} p_A(x)\,D_A^{P}(x)\,dx,\qquad
\pi_B = q_B D_B^{U} + \int_{-1/2}^{b} p_B(y)\,D_B^{P}(y)\,dy,
\]
其中 \(D_i^{U}\) 表示企业 \(i\) 用 uniform price 卖出的需求，\(D_i^{P}\) 表示用 personalized price 卖出的需求。

> 这个利润表达抓住了文章的经济学本质：企业同时经营两种“价格渠道”——公开渠道和个性化渠道。消费者是否主动管理身份，决定了这两个渠道能否被企业有效分离。

文中两个 benchmark 很重要。

Hotelling benchmark（无人被目标化）：
\[
\pi_A=q_A\Big(\frac12-q_A+q_B\Big),\qquad
\pi_B=q_B\Big(q_A-q_B+\frac12\Big).
\]
其均衡是
\[
q_A^*=q_B^*=\frac12,\qquad \pi_A^*=\pi_B^*=\frac14.
\]

> 这是“没有消费者信息”的标准竞争基准。行业总利润是 \(1/2\)，而且市场完全覆盖。

Thisse–Vives benchmark（双方都能对所有消费者做个性化定价，且消费者被动）：
\[
p_A(x)=x,\qquad p_B(y)=-y,
\]
每家企业利润为 \(1/8\)，行业总利润为 \(1/4\)。

> 这是一种“最激烈”的 personalized pricing 竞争：两家企业都逐个消费者打价格战，最后行业利润被压到最低。

此外，在 active consumers 下，一类关键均衡是 PPD（perfect price discrimination on targeted consumers）：
\[
p_A^{PPD}(x)=1+\frac{x}{2},\qquad
p_B^{PPD}(y)=1-\frac{y}{2},
\]
因此
\[
\pi_A^{PPD}(a)=\int_a^{1/2}\Big(1+\frac{x}{2}\Big)\,dx=\frac{9-16a-4a^2}{16},
\]
\[
\pi_B^{PPD}(b)=\int_{-1/2}^{b}\Big(1-\frac{y}{2}\Big)\,dy=\frac{9+16b-4b^2}{16},
\]
\[
\Pi^{PPD}=\pi_A^{PPD}+\pi_B^{PPD}
=\frac{9-8(a-b)-2(a^2+b^2)}{8}.
\]

> 这里企业对各自目标消费者榨取的是“全部 gross surplus”。能做到这一点的前提，不是企业更强，而是 active consumers 使得企业再也不敢用低公开价去挖人，于是个性化价格反而更安全。

### 关键假设

1. **线性 Hotelling 品牌忠诚分布，且若由 monopoly 服务则全市场覆盖。**  
   合理性：这是 personalized pricing 文献中的经典、最干净的竞争框架，能清楚刻画 loyalty、挖角和防守。  
   若放松：引入更一般分布不会改变“active consumers 抬高挖角成本”的核心机制，但阈值和闭式解会变复杂。

2. **目标客群是从企业自身位置向内延伸的一段连续区间。**  
   合理性：企业通常先掌握“更忠诚、更常接触”的用户信息，且 connected interval 便于形成可解释的非 contestable segment。  
   若放松：允许企业选择不连续目标集，会带来更复杂的博弈；作者指出某些情形甚至没有纯策略均衡。

3. **uniform price 先公开承诺，personalized price 后私下给出。**  
   合理性：公开价格往往更“慢”、更可承诺，个性化优惠更“快”、更隐蔽。  
   若放松：若两类价格同时选定，很多中间型均衡会消失，只剩 Hotelling 或 Thisse–Vives 型结果。

4. **baseline 中所有消费者要么都 passive，要么都 active。**  
   合理性：先把竞争机制讲清楚，再在扩展中引入 \(\alpha\) 和 \(c\)。  
   若放松：作者确实在扩展中证明，更多 active consumers 或更低身份管理成本，只会让主结论更强。

5. **基准模型中目标段 \((a,b)\) 外生给定。**  
   合理性：在很多现实市场，企业能否获取某段用户信息受隐私规则、平台制度或数据经纪人供给约束。  
   若放松：内生 targeting 后，结论依然成立，而且主动型消费者下企业更倾向 fully target 全市场。

## 分析路线图 (Roadmap of Analysis)

1. **先立 benchmark：** 给出无信息的 Hotelling 均衡与全量个性化信息下的 Thisse–Vives outcome。
2. **再找结构性约束：** 证明 personalized pricing 使得每家企业都有一块 noncontestable segment，这一结构是后面所有均衡分类的基础。
3. **先解 passive consumers：** 在消费者无法绕过价格限制时，企业可以把公开价与个性化价分离，于是出现 one-way poaching、two-way poaching、partial Hotelling 三类均衡。
4. **再解 active consumers：** 当消费者能拿到本企业公开价时，公开低价会反噬自己的目标客群，企业“挖角能力”与“防守能力”被重新耦合，于是出现 PPD、PPD without full market coverage 和 Hotelling 三类均衡。
5. **做比较静态与扩展：** 引入 \(\alpha\)、\(c\)、\(\gamma\)、内生 targeting、far/near targeting、以及 simultaneous pricing，检查主结论的稳健性。
6. **最后转向政策和管理：** 讨论隐私监管、消费者赋权、客户关系管理与 loyalty-building 的含义。

## 核心分析与求解 (Analysis & Solution)

### 1. Noncontestable consumers：个性化定价先把“自家忠诚用户”锁住

**Lemma 1.** 当企业可以对目标消费者实施 personalized pricing 时，\(A\) 有一块不会被 \(B\) 成功挖走的 noncontestable set：
\[
N_A=[\max\{0,a\},1/2],
\]
\(B\) 对应地有
\[
N_B=[-1/2,\min\{b,0\}].
\]

> **Economic intuition.** 忠诚度为正的、同时又被 \(A\) 识别出来的消费者，\(A\) 总能通过单独调低 personalized price 来保住；对手的 uniform price 再低，也很难把这一块人全部挖走。也就是说，personalized pricing 最先改变的，不是“抢谁”，而是“哪些人根本抢不动”。

这个 Lemma 先建立了一个很重要的逻辑：**目标客群并不等于 contestable market。** 一旦企业能逐个消费者防守，目标客群中最忠诚的那部分其实已接近 monopoly turf。

---

### 2. Passive consumers：更多信息就是更激烈的竞争

前面的 Lemma 建立了防守能力，接下来 Proposition 1 刻画 passive consumers 下的三类均衡。

**Proposition 1.** 当所有消费者都是 passive 时，存在三类均衡：

1. **One-way poaching equilibrium**
   - firm \(A\) 单向挖角：若 \(0\le a\le 2b\)，总利润
     \[
     \Pi=\frac{2+2a-a^2}{8}\in\Big[\frac14,\frac{11}{32}\Big];
     \]
   - firm \(B\) 单向挖角：若 \(2a\le b\le 0\)，总利润
     \[
     \Pi=\frac{2-2b-b^2}{8}\in\Big[\frac14,\frac{11}{32}\Big].
     \]

2. **Two-way poaching equilibrium**  
   若 \(a\le 0\le b\)，双方都挖对方的 loyal consumers，总利润
   \[
   \Pi=\frac14.
   \]

3. **Partial Hotelling outcome**  
   若 \(2b\le a\) 且 \(b\le 2a\)，双方在中间共同未被目标化的区间上做 Hotelling 竞争，总利润
   \[
   \Pi=\frac14+\frac{8ab+9(a-b)-5(a^2+b^2)}{18}\in\Big[\frac14,\frac12\Big].
   \]

> **Economic intuition.** passive consumers 下，企业可以把“对外公开的低价”和“对内个性化的高价”分开：低公开价用来抢别人，个性化价用来保自己。这使得企业信息越多、目标化越深，越容易进入逐段挖角状态。竞争因此被推向更加激烈的一端。

更具体地说，three-type classification 背后的逻辑是：

- 如果一方的目标段伸进了对手的 loyal side，但另一方没有对称地做到，就会出现 **one-way poaching**。
- 如果两方都伸进了对手 loyal side，就会出现 **two-way poaching**，这是最血腥的情形。
- 如果中间保留了一块谁都没识别到的“公共市场”，双方就在这块区域做常规 Hotelling 竞争，这块区域就像一个 **cushion**，能缓和整体竞争。

---

### 3. Passive consumers 下的总括性质：Hotelling 才是企业最想要的

**Proposition 2.** passive consumers 下：

1. 所有均衡都 **full market coverage**；
2. 行业总利润总是落在
   \[
   \frac14 \le \Pi \le \frac12
   \]
   之间；
3. 只有当
   \[
   a=-b=\frac12
   \]
   （即根本没有消费者信息）时，才得到 Hotelling 均衡与最高行业利润 \(1/2\)。

> **Economic intuition.** 这正是 personalized pricing 文献中的经典逻辑：信息是把双刃剑，但在 passive consumers 下，刀口朝向企业自己。信息越多，企业越容易互相精准打击，行业利润越低。最好的状态反而是“谁都不知道太多”，大家只能在统一市场上做钝化竞争。

这一点非常重要，因为它构成全文的对照组：**如果没有 identity management，企业集体最希望的是少数据。**

---

### 4. Active consumers：公开低价会“误伤”自己人

进入全文最关键的地方。active consumers 可以拿到自己企业给非目标消费者的公开价，因此企业无法再把挖角价和保卫价分开。由此，文章指出企业实际上只有两种可行模式：

- **模式 A：** 设一个足够高的公开价 \(q_i\ge 5/4\)，让它在均衡路径上没人选；然后对自己的目标客群做 PPD。
- **模式 B：** 用一个真正会被消费者采用的 uniform price 参与市场竞争。

> **Economic intuition.** 一旦一个公开低价真的被外部消费者接受，它也必然会被本企业那些原本想高价卖出的目标客户接受。于是，企业若想做 aggressive poaching，就得吞下“自我蚕食”的代价。这就是 competition softening 的核心来源。

---

### 5. Active consumers 下的三类均衡：从 all-out competition 到 surplus extraction

**Proposition 3.** 当所有消费者都是 active 时，主要出现三类均衡：

1. **PPD equilibrium**  
   在 fully targeted 且无 overlap 的情形下，文中给出了存在条件。用对称写法表示，即当
   \[
   a=b=\delta \in [2-\sqrt6,\,-2+\sqrt6]
   \]
   时，存在 PPD equilibrium。

2. **PPD equilibrium without full market coverage**  
   在中间有一段共同未被目标化市场的对称情形下，若
   \[
   a=-b=\delta \in \Big(0,\frac{7-4\sqrt3}{2}\Big),
   \]
   则企业会直接放弃这段中间市场，只在各自目标客群上做 PPD。

3. **Hotelling equilibrium**  
   当目标段足够小、共同未目标化的市场足够大时，只要
   \[
   b\le \frac{1-\sqrt2}{2},\qquad a\ge \frac{\sqrt2-1}{2},
   \]
   即便每家企业都有一部分消费者信息，也依然会回到 Hotelling 均衡。

> **Economic intuition.** 这里的逻辑完全反转了。Passive 情形下，信息越多越容易打价格战；Active 情形下，信息越多反而可能让企业更敢把公开价设高、把 personalized price 设满。因为公开低价已经不只是“对外武器”，还是“对内地雷”。

---

### 6. Passive vs. Active：同样的数据环境，竞争方向却可能相反

**Proposition 4.** 该命题把两种消费者行为放在一起比较：

1. 若 \(a=b=0\)，则  
   - active consumers 下得到 PPD，行业总利润最高，为
     \[
     \Pi=\frac98;
     \]
   - passive consumers 下得到 Thisse–Vives outcome，行业总利润最低，为
     \[
     \Pi=\frac14.
     \]

2. 在对称的部分未覆盖情形 \(a=-b=\delta>0\) 下，active consumers 可能导致中间市场不被服务，从而产生 inefficiency；而 passive consumers 下这段市场总会被覆盖。

3. passive consumers 下，Hotelling 只在 \(a=-b=1/2\)（无信息）时出现；active consumers 下，即便两家企业都掌握一部分消费者信息，也可能出现 Hotelling。

4. **对任意给定的 \((a,b)\)，active consumers 下的行业总利润都高于 passive consumers。**

> **Economic intuition.** 这几条合起来就是本文最核心的 message：消费者越会“绕过” personalized pricing，企业之间反而越容易不打仗。对消费者个体来说，主动管理身份似乎能占便宜；但对消费者整体来说，它改变了企业的战略约束，可能让企业集体更赚钱。

这也解释了为什么文章把 active consumers 看作一个 **consumer-side friction on discrimination**：它限制的是单个企业的歧视能力，但却可能改善企业之间的共谋式默契。

---

### 7. 扩展一：只有一部分消费者会主动管理身份

**Proposition 5.** 在 fully targeted 且无 overlap 的情形（用 \(a=b=\delta\) 表示）下，若有比例 \(\alpha\in[0,1]\) 的消费者是 active，则存在 cutoff \(\bar\delta(\alpha)\)，使得当
\[
\delta\in(-\bar\delta(\alpha),\bar\delta(\alpha))
\]
时存在唯一 PPD equilibrium，且 \(\bar\delta(\alpha)\) 随 \(\alpha\) 增大而增大，并在 \(\alpha\to 1\) 时收敛到 \(-2+\sqrt6\)。

**Proposition 6.** 在中间共同未目标化段 \([-\delta,\delta]\) 的对称情形下，存在 cutoff \(\hat\delta(\alpha)\)，使得当
\[
\delta\le \hat\delta(\alpha)
\]
时存在唯一的 PPD equilibrium without full market coverage，且 \(\hat\delta(\alpha)\) 随 \(\alpha\) 增大而增大。

> **Economic intuition.** active consumers 不需要“全体到位”才起作用。只要主动型消费者占比上升，企业就更害怕低公开价反噬自己的目标客群，因此 PPD 与“放弃中间市场”的均衡区域都会扩大。

---

### 8. 扩展二：identity management 有成本

**Proposition 7.** 若消费者变主动需要付出成本 \(c\in(0,5/4]\)，则：

1. 在 fully targeted with overlap 的情形下，始终存在带 partial Thisse–Vives structure 的 PPD equilibrium；
2. 在 fully targeted without overlap 的情形下，存在 cutoff \(\tilde\delta(c)\)，且它随 \(c\) 下降而上升，因此 \(c\downarrow\) 会扩大 PPD 均衡区域；
3. 在对称部分未覆盖情形 \(a=-b=\delta>0\) 下，存在 cutoff \(\check\delta(c)\)，且它随 \(c\downarrow\) 而上升，因此 \(c\downarrow\) 也会扩大 PPD without full coverage 的均衡区域。

> **Economic intuition.** 降低 identity management 的使用成本，效果和提高 active consumers 比例是同方向的：都让企业更不敢把公开价格打低。因此，技术上越容易“装新客”“切账号”“绕 cookie”，竞争越可能被软化。

---

### 9. 扩展三：targeting 本身由企业内生选择

**Proposition 8.** 若 targeting 需要付出边际成本 \(\gamma\in(0,1/3]\)，且消费者都是 passive，则唯一均衡为
\[
a=\frac16+\gamma,\qquad b=-\frac16-\gamma.
\]
延续博弈是 partial Hotelling outcome；每家企业利润随 \(\gamma\) 上升而上升，并在 \(\gamma=1/3\) 时达到 Hotelling 利润 \(1/4\)。

> **Economic intuition.** passive consumers 下，targeting 越贵，企业越不想把信息买得太深，反而愿意留下一个更宽的“中央缓冲带”。这块非目标市场像安全垫一样，减轻了彼此精准打击的冲动。

**Proposition 9.** 若 targeting 成本同样为 \(\gamma\)，但消费者都是 active，则存在多个均衡；在这些均衡里，企业会 fully target 市场且 continuation game 落在 PPD equilibrium 上。就行业利润而言，active consumers 下始终高于 passive consumers。

> **Economic intuition.** 一旦 active consumers 让挖角公开价变得危险，企业就没有理由再故意留下太多“公共市场”来缓和竞争；因为 competition softening 现在可以直接由 identity management 本身带来。于是，企业更愿意把市场 fully target 掉。

---

### 10. 扩展四：企业到底该 target 忠诚用户，还是边缘用户？

**Proposition 10.** 固定 firm \(B\) 的目标段为 \([-1/2,0]\)，firm \(A\) 可在 \([0,\delta]\)（far targeting，面向较不忠诚者）与 \([1/2-\delta,1/2]\)（near targeting，面向最忠诚者）之间选择，则：

- passive consumers 下，\(A\) 在 near targeting 时利润更高；
- active consumers 下，\(A\) 在 far targeting 时利润更高。

> **Economic intuition.** passive consumers 下，target 自家最忠诚客户最划算，因为最容易高价保住；active consumers 下则相反，target 边缘用户更有价值，因为企业能同时利用公开价与个性化价的灵活组合，而不是把全部武器都浪费在本来就很难流失的深度忠诚用户身上。

---

### 11. 进一步的机制总结：这篇文章真正讲清楚的 trade-off

**Trade-off 1：公开低价的“挖角收益” vs. “自我蚕食成本”**  
在 passive consumers 下，低公开价几乎只有挖角收益；在 active consumers 下，它还会把自己目标客群吸走。

**Trade-off 2：更细信息的 surplus extraction 能力 vs. competition intensification**  
消费者被动时，后者占主导；消费者主动时，前者更可能留下来，而后者被显著抑制。

**Trade-off 3：服务中间市场的额外需求 vs. 保持高个性化价格的能力**  
如果服务共同非目标市场意味着必须把公开价打低，而这个低公开价又会压低 personalized prices，那么企业可能宁可放弃中间市场，造成 deadweight loss。

## 比较静态汇总表 (Comparative Statics Summary)

| 参数变化 | 对均衡形态的影响 | 对利润/福利的影响 | 直觉 |
| --- | --- | --- | --- |
| 消费者信息增加（passive） | 更容易从 Hotelling 滑向 one-way / two-way poaching | 行业利润下降；消费者通常受益 | 企业能更精准地挖角与防守，竞争更凶。 |
| 消费者信息增加（active） | 更容易出现 PPD；Hotelling 甚至可在有信息时发生 | 行业利润上升；消费者剩余下降，福利可能下降 | 低公开价会反噬自己人，挖角不再划算。 |
| \(\alpha\uparrow\) | PPD 和 PPD without full coverage 的存在区域扩大 | 消费者整体更差，deadweight loss 更可能出现 | 更多消费者会“套利”，企业更不敢降公开价。 |
| \(c\downarrow\) | 与 \(\alpha\uparrow\) 同向：PPD 相关均衡更稳 | 行业利润上升，消费者剩余下降的风险加大 | 主动管理身份更便宜，相当于更多 active consumers。 |
| \(\gamma\uparrow\)（passive，内生 targeting） | 中间未目标化缓冲带变宽 | 企业利润上升，并趋近 Hotelling | targeting 越贵，越不值得精准打击。 |
| 从 sequential pricing 改为 simultaneous pricing | 中间型均衡消失，只剩 Hotelling 或 Thisse–Vives 型 | 结果更极端 | 公开价与个性化价同时选时，企业更容易通过低公开价直接抢全市场。 |

## 主要结论与管理启示 (Main Results & Managerial Insights)

### 与 Benchmark 的对比

| 情形 | 竞争图景 | 企业利润 | 消费者与福利 |
| --- | --- | --- | --- |
| 无消费者信息（Hotelling） | 标准 Hotelling 竞争 | 行业总利润 \(1/2\) | 全市场覆盖，效率高 |
| passive + 充分目标化（Thisse–Vives / two-way poaching） | 全面 personalized price war | 行业总利润最低 \(1/4\) | 全市场覆盖，但企业利润极低 |
| active + fully targeted no overlap（PPD） | 高公开价 + 各自 turf 内 perfect extraction | 行业总利润可达 \(9/8\) | 消费者剩余很低 |
| active + 中间市场很小 | 企业直接放弃中间段 | 企业利润高于 passive 对应情形 | 产生 deadweight loss |

最反直觉的对比是：**同样是 personalized pricing，passive consumers 下它像价格战机器；active consumers 下它却像竞争缓和器。** 这就是本文相对于 benchmark 的真正新增 trade-off。

### 管理建议

1. **不要把“更多数据”机械理解为“更有利”。**  
   如果消费者大多是 passive，更多目标化信息会把企业拖入更激烈的价格战；如果消费者越来越会 identity management，则同样的数据基础反而可能帮助企业形成更温和的竞争格局。

2. **公开价格策略必须和个性化价格联动考虑。**  
   在 active consumers 场景下，公开低价不是纯粹的 acquisition tool，而是会直接侵蚀企业自己的老客户利润池。只看挖角效果而忽略自我蚕食，会严重高估 aggressive public pricing 的价值。

3. **目标化不一定该瞄准“最忠诚”的客户。**  
   passive 场景下，target loyal customers 合理；active 场景下，target marginal consumers 反而可能更值钱，因为企业能更灵活地同时运用公开价和 personalized price。

4. **别把消费者赋权误当成单向利好消费者。**  
   如果赋权的结果是让更多消费者能轻松规避个性化定价，那么企业可能通过更高公开价和更强 turf exploitation 赚得更多。企业若看到了这一点，甚至可能支持某些“看似更重隐私”的制度安排。

5. **数据若只用于 pricing，风险最大；若能用于 CRM 和 loyalty building，逻辑会变。**  
   文章在讨论部分明确指出，若数据还能提升服务、降低交易摩擦、强化 loyalty program，则这些机制会进一步提高 poaching cost，软化竞争。换言之，数据的真正价值可能不在“更精准收割”，而在“更稳地减少竞争”。

## 与相关文献的对话 (Dialogue with Literature)

### 1. Thisse and Vives (1988)

**共同关注点：** 两文都在研究竞争性 personalized pricing / spatial price discrimination。  
**本文推进：** Thisse and Vives 的结论是，当双方都能逐个消费者定价时，竞争会极度激烈，行业利润跌到最低。本文表明，这个结论隐含了“消费者被动”这一强假设；一旦消费者能做 ex post identity management，同样的信息环境下，企业反而可能协调到 PPD 型结果，利润显著更高。  
**为什么重要：** 它说明经典 personalized pricing 结果并不是技术定理，而是行为假设驱动的结论。

### 2. Chen and Iyer (2002)

**共同关注点：** 都讨论 consumer addressability / customized pricing 如何改变竞争。  
**本文推进：** Chen and Iyer 关注企业能否识别消费者、信息是否不完美；本文进一步把“消费者能否绕过识别结果”也放进模型。换句话说，addressability 不再只是企业能力，也受到消费者端规避能力的反制。  
**为什么重要：** 现实世界里，企业掌握数据和消费者规避数据使用，是同一枚硬币的两面。只看前者，会系统性高估 personalized pricing 的竞争强度。

### 3. Acquisti and Varian (2005)

**共同关注点：** 都关注 identity management / privacy 对价格歧视的影响。  
**本文推进：** Acquisti and Varian 主要在 monopoly 或动态识别框架下分析隐私与识别；本文把 identity management 搬到 duopoly personalized pricing 里，且强调的是 **ex post** 绕开 personalized offer 的能力。  
**为什么重要：** monopoly 里“消费者反抗”通常是限制企业；duopoly 里它还会经由竞争结构反馈回来，可能变成对企业有利的力量。

### 4. Choe et al. (2018)

**共同关注点：** 都比较更细的信息粒度如何影响价格歧视竞争。  
**本文推进：** Choe et al. 的一个核心判断是，personalized pricing 比 third-degree discrimination 更容易加剧竞争。本文指出，这个排序在消费者 passive 时成立，但 active consumers 会改变公开价的战略意义，使 personalized pricing 不再必然对应更强竞争。  
**为什么重要：** 这使我们必须把“数据粒度”与“消费者可规避性”联立起来看，而不能把更细数据直接映射为更激烈竞争。

## 犀利评论 (Reviewer's Critique)

### 优点

**理论贡献。**  
文章真正有价值的地方，不是又做了一个 Hotelling 变体，而是把消费者端的 identity management 放进 competitive personalized pricing 后，得出了方向性翻转的结果：从“信息加剧竞争”变成“信息 + 规避能力可能软化竞争”。

**方法创新。**  
模型看起来简洁，但切入点很巧：公开 uniform price 与私下 personalized price 的两阶段结构，恰好把 active consumers 的套利能力放大成均衡力量。很多结果都不是参数微调，而是机制层面的 regime shift。

**实践相关性。**  
文章直接对接 new-customer-only discount、cookie 删除、换号/换账号、公开价搜索这些非常真实的市场行为。对隐私政策与消费者赋权的讨论也不是空泛口号，而是有明确竞争逻辑支撑。

### 模型限制 / 假设过强

**第一，baseline 的 targeting 结构太规整。**  
企业的目标客群被建模为从自身位置出发的一段连续区间，这非常适合理论刻画，但现实中的 ad-tech targeting 往往是离散、碎片化、跨 segment 的。若允许任意不连续 target set，均衡结构可能大幅变化。

**第二，消费者行为被压缩成 passive / active 二元状态。**  
现实里的 identity management 是连续的、异质的、情境依赖的：有人会比价但不换号，有人换号但不删除 cookie，有人只在大额购买时主动规避。二元设定抓住了主机制，但会夸大某些 regime 的清晰边界。

**第三，公开价格的承诺性假设较强。**  
文章依赖“uniform price 先公开、personalized price 后私下”的结构。在很多数字市场，公开价格和个性化优惠其实是同步、快速更新的。如果承诺性较弱，一些中间型均衡未必还能存在。

**第四，福利分析仍然相对狭义。**  
文中把数据使用的作用几乎都放在 pricing 上，而现实中数据还会改善推荐、匹配、服务、库存、体验。如果把这些 added value 放进去，结论关于 consumer surplus 和 welfare 的方向可能就没那么尖锐。

### 未来方向

1. **把消费者是否 become active 内生化。**  
   让消费者根据预期节省金额、隐私偏好和操作成本，自主决定是否进行 identity management，而不是把 \(\alpha\) 或 \(c\) 当外生参数。

2. **允许企业选择任意 target set，而非连续区间。**  
   这能更贴近数字广告投放、客户分群和 look-alike targeting 的现实，也更能回答“企业究竟该 target 忠诚用户还是摇摆用户”的一般问题。

3. **引入 fairness concerns 与 reputational backlash。**  
   作者在结尾提到 Amazon 的公平感问题。若消费者对“发现自己被区别定价”有额外 disutility，则 active consumers 的作用会和 fairness 一起形成新的竞争约束。

4. **把模型扩展到 dynamic customer relationship management。**  
   真实企业不会只做一期定价，它们还会用 loyalty program、积分、订阅、服务升级来改变未来需求弹性。把 identity management 与 CRM 一起建模，会更接近平台经济和会员制服务。

5. **做经验检验。**  
   电信、保险、银行、流媒体平台与在线零售中都有“只给新客低价”的数据。完全可以用公开价、回流率、换账号行为、促销可见性等变量去检验：当消费者更容易规避 personalized pricing 时，竞争是否真的变得更温和。

## 结尾：这篇文章应该怎么读

如果把这篇文章只读成“一个关于隐私和个性化定价的 Hotelling 模型”，会低估它。更准确的读法是：**它在说明，竞争不是由企业单方面的数据能力决定的，而是由企业的数据能力与消费者的规避能力共同决定的。** 只要把消费者从被动接受者改成会反制算法的战略参与者，整个 competitive personalized pricing 文献最核心的直觉就会翻过来。这正是它值得认真做笔记、也值得在 seminar 里深挖的原因。

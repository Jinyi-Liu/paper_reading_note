# Algorithmic Attention and Content Creation on Social Media Platforms

作者：Yi Chen（Cornell University, SC Johnson Graduate School of Management）、Fei Li（University of North Carolina）、Marcel Preuss（Cornell University, SC Johnson Graduate School of Management）  
年份：2026 年 1 月 6 日版本  
期刊：Working Paper

中文摘要：本文构建了一个理论框架，用来研究一个以广告为收入来源的社交媒体平台，如何通过推荐算法分配用户注意力，以及这种分配如何反过来塑造内容生产与内容消费。创作者一侧既在擅长的话题上存在横向差异，也在生产高质量内容的能力上存在纵向差异；消费者一侧则既在感兴趣的话题上异质，也在对内容质量的欣赏程度上异质。平台的推荐算法同时承担两项激励任务：一方面要让创作者愿意投入努力生产内容，另一方面要让消费者愿意停留并消费广告。最优算法会筛掉低能力创作者，但会给留下来的创作者一个最低读者盘；对于高能力创作者，平台则会主动制造“viral”传播。更重要的是，算法会故意把一部分消费者的注意力分配到他们本来不感兴趣的内容上，以利用平台两边的网络效应。

## 论文速览表

| 维度 | 内容 |
| --- | --- |
| 研究问题 | 广告驱动的社交媒体平台，为什么不总是把“最相关”的内容推荐给用户？推荐算法如何同时激励创作者努力生产内容、又给平台创造更多广告位？ |
| 研究方法 | 理论模型 + 机制设计 + 两边私有信息下的最优算法刻画 |
| 核心机制 | 消费者注意力既是消费资源，也是激励创作者的“隐性支付”。给创作者更多注意力，会提高其努力、拉高内容质量，再帮助平台向真正感兴趣的用户塞入更多广告。 |
| 主结论 | 平台会过滤低能力创作者；中等能力创作者只触达相关受众；高能力且/或热门类别的创作者会被推成“global influencers”，即便这意味着把内容推给不感兴趣的用户。 |
| 反直觉发现 | “不相关推荐”并不一定是算法失误，而可能是利润最大化下的最优激励工具。 |
| 扩展结论 | 当平台可以用金钱或 revenue-sharing 激励创作者，且广告市场足够赚钱时，货币激励会替代“错误推荐”，推荐会重新变得更准确。 |
| 主要贡献 | 把推荐算法写成一个双边筛选问题；解释 viral content 的利润逻辑；说明创作者分层、内容错配与货币化之间的关系。 |
| 适用场景 | TikTok、Instagram Reels、YouTube Shorts 等广告驱动、强推荐流的平台。 |

## TL;DR

这篇文章最核心的结论是：广告驱动的平台并不总想把最相关的内容推给你。它会故意把一部分不那么相关的内容推得更广，因为这能奖励高潜力创作者、逼他们产出更高质量内容，再让平台向真正感兴趣的人卖更多广告。只有当平台能用现金或 revenue-sharing 更便宜地激励创作者时，这种“硬塞不相关内容”的做法才会减少甚至消失。

## One More Thing

本文最妙的一点，是把“给流量”重新解释成了一种激励支付。平台实际上是在拿消费者的注意力当预算：把本来不感兴趣用户的一点时间，分配给某个有潜力的创作者，让他更愿意努力、做出更好的内容；然后平台再拿这批更好的内容，去另一群真正感兴趣的用户那里换取更多广告收入。换句话说，viral 不是单纯的“发现了好内容”，而是平台为了榨出创作者努力，主动设计出来的一套激励制度。

## 研究背景与动机 (Motivation)

### 实践痛点

论文抓住的是一个非常现实的问题：社交媒体已经从“你关注谁就看谁”，逐渐转向“平台算法决定你看什么”。这时平台面对的是一个双边难题：

第一，平台要靠广告赚钱，但不能把用户 feed 里塞满广告，否则用户会离开。  
第二，平台想要有足够多、足够好的内容，就必须让创作者觉得“做内容值得”，而这个激励在很多平台上并不是现金，而是流量和注意力本身。

作者在引言里用几个事实做铺垫：全球社媒用户已经超过 50 亿，美国用户渗透率接近 90%，美国广告主在社媒和 influencer advertising 上的支出超过 1000 亿美元。规模越大，这个问题就越重要：平台到底该如何用推荐算法在“内容质量—用户体验—广告收入”之间做最优平衡？

### 理论缺口

这篇文章试图补的，不是“推荐系统是否会偏”这种一般性问题，而是更具体的机制设计问题：

1. 既有很多文献研究推荐系统、内容质量控制、甚至战略性内容供给，但通常没有把**创作者努力**、**消费者注意力**、**广告收入**三者同时内生化。
2. 既有研究也较少把推荐算法明确写成一个**双边私有信息**的机制设计问题：创作者知道自己的能力，消费者知道自己的偏好强度，而平台并不知道。
3. 更关键地，过去文献常把“注意力”当结果变量，而本文把它当**激励工具**。这是本文最重要的建模视角。

### 核心贡献

1. **把推荐算法写成一个双边机制设计问题。** 平台一边要筛创作者，一边要筛消费者，还要在两边之间配置注意力。
2. **解释 viral content 的利润逻辑。** 内容之所以会“出圈”，不是因为平台只想提高匹配质量，而是因为广泛传播本身能激励高能力创作者更努力。
3. **说明不相关推荐为何会内生出现。** 给不感兴趣用户看内容，在静态上像是浪费；但在动态激励上，它可能是平台最赚钱的做法。
4. **比较注意力激励与货币激励。** 当现金支付或 creator-side monetization 足够有效时，平台就没必要再通过“错误推荐”来激励创作者。

## 模型设定与假设 (Model Setup & Assumptions)

### 1. 参与者与类型

#### 1.1 创作者侧

| 符号 | 含义 | 备注/描述 |
| --- | --- | --- |
| $i \in \mathcal N=\{1,\dots,N\}$ | 内容类别 | 创作者只能生产某一个类别的内容 |
| $\theta \in \Theta=[0,\bar\theta]$ | 创作者能力 | 纵向异质性；能力越高，努力越容易转化成质量 |
| $\mu_i$ | 类别 $i$ 中创作者总量 | 类别流行度的一部分体现在需求侧，供给规模由 $\mu_i$ 给出 |
| $F_i(\theta)$ | 类别 $i$ 中能力分布 | 连续分布 |

#### 1.2 消费者侧

| 符号 | 含义 | 备注/描述 |
| --- | --- | --- |
| $j \in \mathcal N$ | 消费者感兴趣的类别 | 每个消费者只对一个类别有正价值 |
| $v \in V=[\underline v,\bar v]$ | 消费者对内容质量的估值 | 纵向异质性 |
| $\nu_j$ | 类别 $j$ 中消费者总量 | 类别受欢迎程度的重要指标 |
| $G_j(v)$ | 类别 $j$ 中估值分布 | 连续分布 |
| $\nu=\sum_j \nu_j$ | 总消费者规模 | 在跨类别传播公式中出现 |

#### 1.3 技术、偏好与广告

| 符号 | 含义 | 备注/描述 |
| --- | --- | --- |
| $e$ | 创作者努力 | 非负 |
| $q=\theta e$ | 内容质量 | 能力与努力互补；能力高的人同样努力产出更高质量 |
| $k>0$ | 单位注意力成本 | 看内容和看广告都要付出时间/认知成本 |
| $u(\cdot)$ | 创作者从总注意力中获得的效用 | 增函数且凹函数 |
| $z>0$ | 平台广告的单位价格 | 每一单位被真正观看的广告注意力带来 $z$ 收入 |
| $y>0$ | 创作者嵌入式广告的单位价格 | 只在 extension 中出现 |

#### 1.4 机制/算法变量

| 符号 | 含义 | 备注/描述 |
| --- | --- | --- |
| $e_i(\theta)$ | 平台建议的努力水平 | 给类型 $(\theta,i)$ 创作者的努力建议 |
| $a_{ij}(\theta,v)\in[0,1]$ | 注意力分配概率 | 类别 $j$、估值 $v$ 的消费者是否看见类别 $i$、能力 $\theta$ 创作者的内容 |
| $s_j(v)$ | 平台插入广告总量 | 给类别 $j$、估值 $v$ 的消费者的广告包大小 |
| $B_i(\theta)$ | 创作者在非本类消费者中的触达率 | 文中用它总结跨类别传播强度 |
| $\pi_i(\theta)$ | 平台给创作者的直接支付 | 只在 monetary extension 中出现 |
| $\sigma_i(\theta)$ | 创作者内容内嵌的 sponsored ads 数量 | 只在 monetary extension 中出现 |

#### 1.5 不完全信息下的虚拟类型

| 符号 | 含义 | 备注/描述 |
| --- | --- | --- |
| $\Phi_i(\theta)=\theta-\dfrac{1-F_i(\theta)}{f_i(\theta)}$ | 创作者虚拟能力 | Myerson 式 virtual type，反映激励高类型的边际成本 |
| $\Psi_j(v)=v-\dfrac{1-G_j(v)}{g_j(v)}$ | 消费者虚拟估值 | 平台真正可榨取的“净有效价值” |
| $U_i(\theta)$ | 创作者 truthful report 的间接效用 | 信息租 |
| $W_j(v)$ | 消费者 truthful report 的间接效用 | 信息租 |

### 2. 博弈/决策结构

1. 平台观察到用户所属的横向类别 $i,j$，并承诺一个推荐算法/机制。
2. 创作者和消费者分别知道自己的纵向私有信息：创作者知道自己的能力 $\theta$，消费者知道自己的估值 $v$。
3. 创作者选择/报告适合自己的合同，并按平台建议付出努力 $e_i(\theta)$；内容质量实现为 $q=\theta e$。
4. 平台根据机制向消费者分配内容和广告 bundle；消费者选择是否接受并消费该 bundle。
5. 广告被观看后，平台获得广告收入；创作者从总注意力中获得效用。

### 3. 信息结构

- 平台**知道横向类别**（谁擅长什么、谁喜欢什么类别）。
- 平台**不知道纵向类型**（创作者能力 $\theta$ 与消费者估值 $v$）。
- 平台**观察到内容质量**，但不知道这是由“高能力低努力”还是“低能力高努力”产生的。
- 因此，推荐算法必须满足 **Incentive Compatibility (IC)** 与 **Individual Rationality (IR)**。

### 4. 目标函数与约束

#### 4.1 创作者的生产技术与效用

质量由
$$
q=\theta e
$$
给出。

创作者的效用可写为
$$
u\!\left(\sum_j \nu_j \int_V a_{ij}(\theta,v)\,dG_j(v)\right)-e_i(\theta).
$$

> 第一项是“收到多少注意力”的效用，第二项是努力成本。关键点在于：这里的平台并不一定用现金激励创作者，而是用“流量”激励创作者。

#### 4.2 消费者的效用

一个类别 $j$、估值为 $v$ 的消费者，如果看见类别 $i$ 创作者生产、质量为 $q$ 的内容，其单位注意力净收益为
$$
vq\mathbf 1\{i=j\}-k.
$$

若看广告，则单位注意力净收益为
$$
-k.
$$

truthful allocation 下的消费者总效用为
$$
\sum_i \mu_i \int_\Theta a_{ij}(\theta,v)\Big(v\theta e_i(\theta)\mathbf 1\{i=j\}-k\Big)\,dF_i(\theta)-k s_j(v).
$$

> 只有“类别匹配”时，内容质量才给消费者带来正价值；但无论看内容还是广告，都要消耗注意力成本 $k$。因此，平台必须保证推荐 bundle 至少值得用户看完。

#### 4.3 平台目标函数

平台只从广告变现，目标是
$$
\max_A\; z\sum_j \nu_j \int_V s_j(v)\,dG_j(v).
$$

> 平台真正关心的不是抽象意义上的 engagement，而是可被广告变现的注意力。优质内容的价值，在于它能“撑住”更多广告。

#### 4.4 IC 与 IR 约束

创作者 IC：
$$
u\!\left(\sum_j \nu_j \int_V a_{ij}(\theta,v)\,dG_j(v)\right)-e_i(\theta)
\ge
u\!\left(\sum_j \nu_j \int_V a_{ij}(\theta',v)\,dG_j(v)\right)-\frac{\theta'}{\theta}e_i(\theta').
$$

> 如果一个低能力创作者伪装成高能力类型，他必须用更高的实际努力去模仿对应质量，因此伪报不应更优。

消费者 IC：
$$
\sum_i \mu_i \int_\Theta a_{ij}(\theta,v)\Big(v\theta e_i(\theta)\mathbf 1\{i=j\}-k\Big)\,dF_i(\theta)-k s_j(v)
$$
$$
\ge
\sum_i \mu_i \int_\Theta a_{ij}(\theta,v')\Big(v\theta e_i(\theta)\mathbf 1\{i=j\}-k\Big)\,dF_i(\theta)-k s_j(v').
$$

> 平台给不同消费者设计的 bundle 必须让每种类型都愿意选“自己的那一份”。这就是消费者侧的 screening。

创作者 IR：
$$
u\!\left(\sum_j \nu_j \int_V a_{ij}(\theta,v)\,dG_j(v)\right)-e_i(\theta)\ge 0.
$$

消费者 IR：
$$
\sum_i \mu_i \int_\Theta a_{ij}(\theta,v)\Big(v\theta e_i(\theta)\mathbf 1\{i=j\}-k\Big)\,dF_i(\theta)-k s_j(v)\ge 0.
$$

> 在本文里，IR 也可以理解为 obedience constraint：平台推荐的 effort 必须值得创作者执行，平台推荐的 bundle 也必须值得消费者完整观看。

### 5. 关键假设

#### 假设 1：规则性 (Regularity)
作者假设 $\Phi_i(\theta)$ 和 $\Psi_j(v)$ 单调递增。

- **Justification**：这是经典机制设计中常见的 regularity，保证最优机制有单调分配、cutoff 结构。
- **若放松**：最优机制可能出现 non-monotone allocation，需要 ironing，解析结果会变得很不干净。

#### 假设 2：创作者效用 $u(\cdot)$ 递增且凹
- **Justification**：更多注意力总是更好，但边际激励递减，符合“流量有用但不是线性”的直觉。
- **若放松**：如果边际效用不递减，平台会更极端地集中流量；若过于平，则注意力作为激励工具会弱很多。

#### 假设 3：消费者不能在 bundle 内完美 cherry-pick
- **Justification**：短内容、图文、短视频场景下，用户往往在“发现不喜欢”之前已经花掉了一部分注意力；平台也可通过混排降低可筛选性。
- **若放松**：如果用户能无成本跳过不喜欢内容和广告，平台就更难靠混排机制榨取注意力，不相关推荐的价值会下降。

#### 假设 4：每个创作者只擅长一个类别，每个消费者只喜欢一个类别
- **Justification**：这是为了把横向匹配做得足够清楚，让“相关/不相关推荐”的张力一眼可见。
- **若放松**：若创作者跨题材创作、消费者多兴趣并存，则 cutoff 仍可能存在，但边界会变得模糊，viral 的跨类含义也会更复杂。

#### 假设 5：平台知道横向类别、观察到质量，但不知道纵向私有类型
- **Justification**：现实中平台确实更容易从历史行为推断“你喜欢哪个领域”，但很难完全识别“你到底多喜欢”或“创作者真实能力多高”。
- **若放松**：若平台连类别都不清楚，问题会再加一层 learning；若平台连质量都看不清，则还要加入 experimentation/exploration 问题。

#### 技术性凸性条件（Assumption 2/3）
文中额外要求
$$
\frac{\underline v}{E_i[v]}+\frac{u'(\nu_i)\nu_i}{u(\nu_i)}\ge 1
\quad\text{或更强地}\quad
\frac{\Psi_i(v)}{E_i[\Psi_i(v)]}+\frac{u'(\nu_i)\nu_i}{u(\nu_i)}\ge 1.
$$

- **Justification**：它确保平台在本类别内的注意力分配呈现 bang-bang 结构：要么完全不给，要给就给整类消费者。
- **若放松**：本类注意力可能不再是严格 0/1，但“存在明显阈值、注意力分配不连续”这一核心直觉通常还在。

## 分析路线图 (Roadmap of Analysis)

这篇文章的分析路径非常清晰，基本上是“三步走”。

1. **Complete Information benchmark**  
   先假设平台知道所有人的类型，暂时把 screening 问题拿掉。这样做的目的，是先看清楚：即使没有信息不对称，平台也会不会主动制造 viral 和不相关推荐？答案是会，因为网络效应本身已经足够让平台偏离“只推最相关内容”。

2. **Incomplete Information main model**  
   再回到真正的双边私有信息环境。作者用 Myerson 方法简化 IC，把消费者价值替换成 virtual value，把创作者能力替换成 virtual ability，从而得到主结果：最优算法依然是 cutoff + 分层结构，但门槛更高、流量更集中、努力更扭曲。

3. **Monetary incentives extension**  
   最后加入两种货币激励：平台直接支付、以及创作者在内容中嵌入 sponsored ads。这样可以问一个非常重要的实践问题：如果平台能用现金激励创作者，是否还需要用“不相关推荐”去补贴他们？答案取决于广告市场是否足够赚钱。

## 核心分析与求解 (Analysis & Solution)

### 8.1 Complete Information：先看清网络效应本身

#### 从绑定约束出发：平台等价于在“内容 surplus”和“广告 inventory”之间做转换

在 complete information 下，作者首先证明：最优时消费者 IR 必然绑定，创作者 IR 也可无损地设为绑定。这样一来，平台其实是在最大化“消费者从内容中得到的 surplus”，然后把它尽可能转换成广告。

形式上，平台问题可改写为
$$
\max_{\{e_i\},\{a_{ij}\}}
\sum_{i,j}\mu_i\nu_j \int_\Theta\int_V a_{ij}(\theta,v)\Big(v\theta e_i(\theta)\mathbf 1\{i=j\}-k\Big)\,dG_j(v)\,dF_i(\theta)
$$
subject to
$$
e_i(\theta)=u\!\left(\sum_j \nu_j\int_V a_{ij}(\theta,v)\,dG_j(v)\right).
$$

> 这一步很关键：平台不是直接选择“塞多少广告”，而是先选择怎样配置内容注意力，以便创造出足够多、可被广告吃掉的剩余。

#### 核心分解：给一条内容多一点 attention，到底值不值？

平台对某个匹配 $(\theta,i,v,j)$ 多分一点注意力的边际收益，可写为
$$
\underbrace{v\theta e_i(\theta)\mathbf 1\{i=j\}-k}_{\text{Direct Surplus}}
+
\underbrace{u'\!\big(u^{-1}(e_i(\theta))\big)\theta \nu_i \int_V a_{ii}(\theta,v')v' dG_i(v')}_{\text{Network Effect}}.
$$

> 第一项是静态收益：消费者自己愿不愿意看。第二项是动态收益：多给创作者一点流量，会让他更努力，提升内容质量，而这会让所有已经在看他内容的同类消费者都更满意。也就是说，注意力对创作者努力有激励作用，对整个平台的广告库存有乘数效应。

#### Proposition 1：Complete Information 下的最优算法是三道 cutoff

作者证明，当注意力成本 $k$ 不太高时，最优算法具有如下结构：

$$
a_{ii}(\theta,v)=\mathbf 1\{\theta\ge \theta_i^{(1)}\},
$$

$$
B_i(\theta)=
\begin{cases}
0, & \theta\le \theta_i^{(2)},\\[4pt]
\dfrac{u'^{-1}\!\left(\dfrac{k}{\theta \nu_i E_i[v]}\right)-\nu_i}{\nu-\nu_i}, & \theta_i^{(2)}<\theta<\theta_i^{(3)},\\[10pt]
1, & \theta\ge \theta_i^{(3)},
\end{cases}
$$

$$
e_i(\theta)=u\!\big(\nu_i+(\nu-\nu_i)B_i(\theta)\big)\mathbf 1\{\theta\ge\theta_i^{(1)}\}.
$$

三个 cutoff 分别满足
$$
\theta_i^{(1)}=\frac{k}{u(\nu_i)E_i[v]},\qquad
\theta_i^{(2)}=\frac{k}{\nu_i u'(\nu_i)E_i[v]},\qquad
\theta_i^{(3)}=\frac{k}{\nu_i u'(\nu)E_i[v]}.
$$

> 直觉上，$\theta_i^{(1)}$ 决定“能不能出道”；$\theta_i^{(2)}$ 决定“能不能跨圈层扩散”；$\theta_i^{(3)}$ 决定“能不能被推成真正的 global influencer”。类别越热门（$\nu_i$ 越大）或者该类别消费者平均估值越高（$E_i[v]$ 越高），这些门槛就越低。

#### Corollary 1：创作者被内生分成四层

虽然文中 corollary 的表述写成“三段”，但实际给出的经济分层是四类：

| 分层 | 能力区间 | 注意力分配 | 努力/质量特征 | 经济含义 |
| --- | --- | --- | --- | --- |
| Inactive | $\theta<\theta_i^{(1)}$ | 无注意力 | 无努力、无质量 | 被平台直接淘汰 |
| Local Entertainers | $\theta_i^{(1)}\le \theta\le \theta_i^{(2)}$ | 只给本类别消费者 | 正努力、但 audience 仅限相关人群 | 能做内容，但“只在圈内火” |
| Ladder Climbers | $\theta_i^{(2)}<\theta<\theta_i^{(3)}$ | 本类别全覆盖，并逐步触达他类消费者 | 努力随能力上升而提高 | 平台用跨圈扩散去激励他们 |
| Global Influencers | $\theta\ge \theta_i^{(3)}$ | 所有消费者都能看到 | 高质量、高覆盖 | 被平台“推成全民爆款” |

> 这正是本文最有辨识度的结果：viral 不是随机出现的，而是平台最优机制下的一种内生分层结果。

#### 为什么本类别 attention 是 all-or-none，而跨类别 attention 是渐进式？

这是 Proposition 1 背后的核心机制。

- **本类别 attention 是 bang-bang。**  
  如果某个创作者只得到本类消费者的一小部分注意力，那么他的努力很低，质量也很低，而这些微小质量提升又不足以弥补消费者的注意力成本。于是平台不会“小打小闹”地给流量；要给，就给整类消费者。
- **跨类别 attention 是 gradual。**  
  跨类别用户本身不从内容中得到直接价值，所以这部分 attention 只起“激励创作者”的作用。既然只是激励工具，它就会像一个平滑增加的补贴，而不是 0/1 式跳变。

> 这是本文最漂亮的一层直觉：同样是 attention，本类别 attention 兼具“消费价值 + 激励价值”，所以回报是凸的；跨类别 attention 只有“激励价值”，所以回报更像是凹的。

#### 一个非常关键的结论：负点对点 surplus 的推荐，仍然可能是最优的

文中 Figure 1 明确展示：在最优算法下，有一部分推荐在静态上是负 surplus 的。

- 对跨类别消费者来说，看不感兴趣内容的直接 surplus 永远是 $-k$。
- 即便在本类别内，刚刚跨过 $\theta_i^{(1)}$ 的低能力创作者，也可能让低估值消费者“看了后悔”。

> 但平台还是会这么做，因为静态损失会被动态激励收益抵消。也就是说，**点对点匹配效率**不是平台的目标，**激励后的全局广告收益**才是目标。

### 8.2 Incomplete Information：双边 screening 让 distortion 更强

Complete information 证明了一件事：即便没有信息不对称，平台也会主动造 viral、造错配。接下来作者引入真正的难点：创作者能力 $\theta$ 和消费者估值 $v$ 都是私有信息。

#### Lemma 2：用 Myerson 把 IC 变成 monotonicity + envelope

作者先把 IC 约束标准化。

创作者侧，IC 等价于：

1. 质量 $q_i(\theta)=\theta e_i(\theta)$ 关于 $\theta$ 单调递增；
2. 信息租满足
$$
U_i(\theta)=U_i(0)+\int_0^\theta \frac{e_i(\tilde\theta)}{\tilde\theta}\,d\tilde\theta.
$$

消费者侧，IC 等价于：

1. 消费者在自己类别上得到的“质量加权总注意力”关于 $v$ 单调递增；
2. 信息租满足
$$
W_j(v)=W_j(\underline v)+\mu_j\int_{\underline v}^{v}\int_\Theta a_{jj}(\theta,v')\theta e_j(\theta)\,dF_j(\theta)\,dv'.
$$

> 这一步告诉你，平台不能随心所欲地给不同人分配 bundle。它必须保证：高估值消费者看到的“有效内容质量”不比低估值消费者差；高能力创作者生产出的质量也不能低于低能力创作者。否则 truthful reporting 就崩掉了。

#### 平台目标从真实 surplus 变成 virtual surplus

在不完全信息下，平台问题可写成
$$
\max_{\{e_i\},\{a_{ij}\}}
\sum_{i,j}\mu_i\nu_j \int_\Theta\int_V a_{ij}(\theta,v)\Big(\Psi_j(v)\theta e_i(\theta)\mathbf 1\{i=j\}-k\Big)\,dG_j(v)\,dF_i(\theta)
$$
再加上创作者侧的信息租约束。

> 和 complete information 相比，最大的变化是：消费者价值 $v$ 被替换成了 virtual value $\Psi_j(v)$。对平台来说，一个消费者的“真实偏好强度”并不等于它能真正榨到手的价值，因为还要给消费者留信息租。

#### 更深的一层：给一个创作者更多 attention，会伤害更高类型的激励设计

对 $a_{ij}(\theta,v)$ 的边际影响，作者分解为三部分：
$$
\underbrace{\Psi_j(v)\theta e_i(\theta)\mathbf 1\{i=j\}-k}_{\text{Virtual Surplus}}+
\underbrace{u'\!\big(u^{-1}(e_i(\theta)+U_i(\theta))\big)\theta\nu_i \int_V a_{ii}(\theta,v')\Psi_i(v')\,dG_i(v')}_{\text{Current-type Network Effect}}
$$

$$
-\underbrace{u'\!\big(u^{-1}(e_i(\theta)+U_i(\theta))\big)\frac{\nu_i}{f_i(\theta)}\int_{\theta}^{\bar\theta}\int_V a_{ii}(\tilde\theta,v')\Psi_i(v')\,dG_i(v')\,dF_i(\tilde\theta)}_{\text{Higher-type Rent Spillover}}.
$$

> 第一项是“这次匹配本身值不值”；第二项是“多给当前类型一点 attention，可以逼他更努力”；第三项是新出现的坏消息：你把当前类型抬高了，所有更高类型为了不伪装/不被模仿，也得留更多 rent，结果是更高类型的 effort 反而会被压低。  
> 这就是本文的双重全局效应：注意力不仅影响当前创作者，还通过信息租影响一整串更高类型创作者。

#### Proposition 2：最优算法仍是 cutoff 结构，但门槛全面上升

主结果是：不完全信息下，最优算法仍然有三道能力门槛
$$
\theta_i^{(a)}<\theta_i^{(b)}<\theta_i^{(c)},
$$
并满足

$$
a_{ii}(\theta,v)=\mathbf 1\{\theta\ge \theta_i^{(a)}\},
$$

$$
B_i(\theta)=
\begin{cases}
0, & \theta\le \theta_i^{(b)},\\[4pt]
\dfrac{u'^{-1}\!\left(\dfrac{k}{\Phi_i(\theta)\nu_i E_i[\Psi_i(v)]}\right)-\nu_i}{\nu-\nu_i}, & \theta_i^{(b)}<\theta<\theta_i^{(c)},\\[10pt]
1, & \theta\ge \theta_i^{(c)},
\end{cases}
$$

以及
$$
\Phi_i(\theta_i^{(a)})=\frac{k}{u(\nu_i)E_i[\Psi_i(v)]},\qquad
\Phi_i(\theta_i^{(b)})=\frac{k}{\nu_i u'(\nu_i)E_i[\Psi_i(v)]},\qquad
\Phi_i(\theta_i^{(c)})=\frac{k}{\nu_i u'(\nu)E_i[\Psi_i(v)]}.
$$

> 结构没有变，逻辑却更“狠”了：消费者侧要留 rent，所以 $\Psi_i(v)<v$；创作者侧要留 rent，所以 $\Phi_i(\theta)<\theta$。这两个楔子一起作用，使得平台更不愿意养低能力创作者，也更不愿意把 attention 分散出去。

#### Corollary 2：四层分化依旧存在，但平台更保守、更集中

在不完全信息下，创作者仍分成四类：

| 分层 | 能力区间 | 注意力分配 | 质量/努力特征 | 相比 complete information 的变化 |
| --- | --- | --- | --- | --- |
| Inactive | $\theta<\theta_i^{(a)}$ | 无 | 无 | 被淘汰的创作者更多 |
| Local Entertainers | $\theta_i^{(a)}\le \theta\le \theta_i^{(b)}$ | 仅本类 | 质量 bunch 在最低水平 | 更多“够格但不出圈”的中等内容 |
| Ladder Climbers | $\theta_i^{(b)}<\theta<\theta_i^{(c)}$ | 本类全覆盖 + 部分跨类 | 质量随能力上升 | 变得更难跨圈层扩散 |
| Global Influencers | $\theta\ge \theta_i^{(c)}$ | 所有人都能看到 | 质量 bunch 在最高水平 | 真正全民爆款的门槛更高 |

> 所以，不完全信息不会推翻 viral 逻辑，但会把平台推向更高门槛、更强集中和更重的头部化。

#### Figure 2 的两个关键信息：质量有 bunching，努力甚至不单调

作者进一步指出：

1. **质量 $q_i(\theta)=\theta e_i(\theta)$ 是递增的，但会在 Local Entertainers 和 Global Influencers 两端 bunch。**  
   Local Entertainers 只能拿到固定的本类 audience，所以质量卡在最低可行水平；Global Influencers 已经拿满所有 audience，也没有进一步拉高质量的激励。
2. **努力 $e_i(\theta)$ 可能不是单调的。**  
   因为在 bunching 区间里，要维持固定质量，能力越高反而可以少努力；而在“爬梯子”区间，能力更高的人可能更拼，因为跨类触达的边际回报更大。

> 这非常有意思：平台想要的不是“能力越高，努力越多”这种简单关系，而是“哪类人最需要被激励、最值得被激励”。因此 effort schedule 可以出现双峰。

#### 本节最重要的一句话

**双边私有信息把平台的 distortion 放大了。**  
在 complete information 下，平台已经会为了激励创作者而故意做错配；到了 incomplete information，下列扭曲都会更强：

- 创作者进入门槛更高；
- 内容供给更少；
- attention 更集中；
- 质量在中低段和高端都出现 bunching；
- 努力配置更扭曲。

### 8.3 Extension：允许货币激励后，会发生什么？

主模型里，平台只能用 attention 激励创作者。extension 允许两种额外工具：

1. **直接支付** $\pi_i(\theta)$：平台给创作者现金；
2. **创作者内容内嵌 sponsored ads** $\sigma_i(\theta)$：创作者可以在自己的内容里带货/接广，并从外部广告市场按单价 $y$ 获得收入。

这时平台优化问题的核心部分可写为
$$
\max
\sum_{i,j}\mu_i\nu_j\int_\Theta\int_V a_{ij}(\theta,v)
\Big(\Psi_j(v)\theta e_i(\theta)\mathbf 1\{i=j\}-k(1+\sigma_i(\theta))\Big)\,dG_j(v)\,dF_i(\theta)
-\frac{k}{z}\sum_i \mu_i\int_\Theta \pi_i(\theta)\,dF_i(\theta).
$$

同时，创作者的激励约束里，attention 之外还多了现金和 sponsored ads 收入。

> 这一步把本文推向了一个非常现实的问题：如果平台有更直接的“货币化”手段，它还要不要继续用错误推荐去补贴创作者？

#### Proposition 3：如果广告市场很赚钱，货币激励会替代错误推荐

当
$$
\max\{y,z\}>1
$$
时，作者称之为 **lucrative ads market**。此时最优算法的关键特征是：

- 对活跃创作者，平台令
  $$
  a_{ii}(\theta,v)=1,\qquad B_i(\theta)=0.
  $$
- 也就是说，**跨类别的不相关推荐消失了**。
- 若 $y>z$，平台只使用 sponsored ads 这一种工具；
- 若 $z>y$，平台只使用直接支付这一种工具。

> 直觉非常清楚：既然平台或创作者能通过货币化每一单位 attention 获得足够高的收入，那就没必要再“借用”不感兴趣用户的时间去补贴创作者了。现金或 sponsored ads 成了比“错误推荐”更便宜、更准确的激励工具。

#### Proposition 4：如果广告市场不赚钱，平台仍会优先用错误推荐

当
$$
\max\{y,z\}<1
$$
时，作者称之为 **meager ads market**。此时：

- 平台仍先沿用主模型的逻辑，最大化跨类别 attention；
- 只有对最顶级的一部分 Global Influencers，平台才会进一步使用现金或 sponsored ads。

> 换句话说，如果广告 monetization 本身不够强，那么“把不相关内容推给更多人”仍然是更便宜的激励手段。金钱只会留给塔尖创作者。

#### 这个 extension 的一句话总结

**Money is a substitute for distorted attention — but only when monetization is strong enough.**

这也是本文一个非常重要的管理启示：推荐准确性和创作者 monetization 机制不是两件独立的事，它们是同一个激励系统的两个侧面。

## 比较静态汇总表 (Comparative Statics Summary)

下表并非逐个命题里的“显式 comparative statics”原文照抄，而是根据 cutoff 公式和作者讨论整理出的总表。

| 参数变化 | 对进入门槛/创作者筛选的影响 | 对跨类传播/viral 的影响 | 直觉 |
| --- | --- | --- | --- |
| $k\uparrow$ | $\theta_i^{(1)},\theta_i^{(a)},\theta_i^{(b)},\theta_i^{(c)}$ 都上升；活跃创作者更少 | $B_i(\theta)$ 更低，viral 更少 | 注意力更贵，平台更不愿让用户为内容和广告付出时间 |
| $\nu_i\uparrow$ | 门槛下降，更多该类创作者能留下来 | 更容易出现 Ladder Climbers 和 Global Influencers | 类别越热门，同样的高质量内容能服务更多用户，激励回报更大 |
| $E_i[v]\uparrow$ 或 $E_i[\Psi_i(v)]\uparrow$ | 门槛下降 | 跨类扩散更容易 | 该类别消费者越“值钱”，平台越愿意投资创作者质量 |
| 消费者信息不对称更严重（$\Psi_i(v)$ 更低） | 门槛上升 | attention 分配更保守 | 平台从消费者处能抽取的净价值下降 |
| 创作者信息不对称更严重（$\Phi_i(\theta)$ 更低） | 门槛上升，低能力创作者更难进入 | 跨类扩散更难，质量/努力扭曲更大 | 提高当前类型质量会拉高高类型信息租，screening 更贵 |
| $u'(\cdot)$ 更高（注意力激励更敏感） | 门槛下降 | 更容易把创作者推向跨类传播 | 同样一单位 attention 更能换来 effort |
| $\max\{y,z\}$ 跨过 1 | 活跃创作者仍会被筛选，但激励方式改变 | 不相关推荐显著下降，甚至消失 | 货币激励比错误推荐更便宜时，平台会“花钱买努力”而不是“拿用户时间补贴” |
| 类别很不热门（$\nu_i$ 很小或相关用户价值很低） | 该类别可能根本没有创作者被激活 | 基本不可能 viral | 平台不会在低回报类别上浪费激励预算 |

## 主要结论与管理启示 (Main Results & Managerial Insights)

### 与 benchmark/朴素直觉的对比

最自然的朴素直觉是：平台应该把最相关、最优质的内容推给对应用户，再在中间插广告。但本文说明，**一旦创作者努力是内生的，这个直觉就错了。**

| 维度 | 朴素的 relevance-first 逻辑 | 本文的无货币主模型 | 货币激励且广告市场丰厚时 |
| --- | --- | --- | --- |
| 推荐目标 | 最大化即时匹配质量 | 最大化广告利润下的总激励效果 | 仍以利润最大化，但可用现金替代错配 |
| 对低能力创作者 | 只要内容还能产生一点价值就可能保留 | 直接筛掉 | 仍会筛掉 |
| 对中等能力创作者 | 主要按相关性分发 | 只给相关用户，形成“圈内流量” | 只给相关用户 |
| 对高能力创作者 | 给相关用户更多曝光 | 故意跨圈层扩散，制造 viral | 不必靠跨圈错配，改用钱激励 |
| 不相关推荐 | 应该尽量避免 | 是最优机制的一部分 | 可显著减少甚至消失 |
| 用户福利 | 较高 | 被广告和错误推荐双重挤压 | 推荐准确性改善 |

### 主要管理启示

1. **推荐机制和创作者 monetization 必须联合设计。**  
   平台不应把“算法团队”和“创作者激励团队”当成两套独立系统。你如何给钱、如何分流量，本质上是在设计同一个 incentive scheme。

2. **Viral 不是纯粹的发现机制，而是激励机制。**  
   平台如果过度追求“爆款化”，往往不是算法失灵，而是在用流量集中来逼高潜力创作者继续努力。

3. **如果平台有更强的 monetization 能力，就应尽量用钱替代错配。**  
   当平台广告单价高、或创作者带货广告很有效时，最优做法是减少把不相关内容推给不感兴趣用户，改用直接支付或 sponsored ads 激励创作者。

4. **平台会系统性偏向热门类别。**  
   热门类别因为能服务更多人、带来更高广告回报，所以更容易被推成头部。这意味着 niche 类别天生处于不利位置。

5. **监管者不要把“错误推荐”简单理解为技术问题。**  
   本文表明，错配可能是平台利润最大化下的刻意选择。要改善用户体验，光盯着推荐精度不够，还要看平台的广告和创作者激励制度。

6. **不同内容形态对应不同 monetization 工具。**  
   论文 extension 暗示：短内容平台可能更适合 sponsored ads，长内容平台则更可能采用直接平台支付或 revenue-sharing。

## 与相关文献的对话 (Dialogue with Literature)

| 文献 | 共同关注点 | 本文推进/区别 | 为什么重要 |
| --- | --- | --- | --- |
| Ghosh and McAfee (2011) | 平台如何用算法激励高质量 UGC | 他们更关注质量控制和学习；本文进一步把消费者注意力、广告收入与创作者努力放到同一个机制设计框架里 | 让“流量本身是一种激励支付”这个机制被明确写出来 |
| Qian and Jain (2024) | 推荐系统与内生内容创作的互动 | 他们也发现平台可能推“高质量但不那么相关”的内容；本文进一步允许创作者群体规模、类别异质性、双边私有信息同时内生化 | 因而本文能给出更细的创作者分层和更清楚的 distributional implications |
| Ren (2024) | 广告、内容生产与平台设计 | Ren 关注广告政策与去中心化内容生产；本文真正“打开了黑箱”，直接求解最优 recommendation algorithm | 因此本文能说明不相关推荐何时是利润最大化的内生结果 |
| Filippas, Horton, and Lipnowski (2023) | 社交媒体中的注意力分配与内容生产 | 那篇更强调用户之间如何争夺注意力；本文强调由平台算法主导的 attention allocation | 当平台握有流量闸门时，viral 的生成逻辑与社交网络自发传播完全不同 |

## 犀利评论 (Reviewer's Critique)

### 优点

**理论贡献。**  
本文最强的地方，是把“推荐算法”从一个黑箱排序器，提升成了一个双边机制设计问题。注意力不再只是 outcome，而成了平台用来支付和激励创作者的 instrument。

**方法创新。**  
在同时允许横向类别异质、纵向能力/估值异质、两边私有信息的情况下，作者仍然得到非常干净的 cutoff 结构与创作者分层。尤其是对边际注意力收益的分解，非常有启发性。

**实践相关性。**  
viral、头部化、不相关推荐、creator payments、embedded ads——这些都是当前短视频平台最核心的现实现象，本文把它们放进了一个统一框架里。

### 模型限制 / 假设过强

1. **消费者不能 cherry-pick bundle 的假设偏强。**  
   对短内容这还说得过去，但对长视频、长文内容就没那么自然。若用户能快速跳过不喜欢内容，不相关推荐的激励价值会下降。

2. **平台对质量的观察太强，且缺少 learning/exploration。**  
   现实里平台往往先把内容投给小样本用户试探，再逐步放量。把“冷启动”和“探索期”拿掉后，模型更像是 solved recommendation，而不是 learned recommendation。

3. **社交关系网络被拿掉了。**  
   现实 feed 通常是“推荐内容 + 关注内容”的混合。本文为了突出算法控制，把 follow graph 完全简化掉，因此难以分析“社交关系”与“算法扩散”之间的相互作用。

4. **广告侧被极度简化为固定单价。**  
   平台与广告主之间其实也有一个复杂的市场：定向、竞价、转化率、广告疲劳都可能反过来影响最优 attention allocation。

5. **每人只对应一个类别，现实里过于干净。**  
   多兴趣消费者、多题材创作者、跨领域品牌合作都会让 cutoff 结构变得更模糊，superstar 形成机制也可能更复杂。

### 未来方向

1. **加入动态学习与 cold-start。**  
   平台如何在“探索新创作者”和“继续推头部创作者”之间做权衡？这会直接影响平台是否过度头部化。

2. **加入平台竞争与多归属 (multi-homing)。**  
   当创作者可以在多个平台同时发内容时，平台是否还会像本文一样依赖错配推荐来激励他们？

3. **把广告主一侧真正内生化。**  
   让广告价格、点击效果和转化取决于 audience-targeting accuracy，能更细致地分析“错误推荐”和广告收益之间的真实权衡。

4. **分析 harmful content / misinformation。**  
   如果某些内容虽然能激励创作者、提高停留时长，却带来社会危害，最优算法和监管设计会怎样变化？

5. **允许创作者多题材生产、消费者多兴趣消费。**  
   这能让模型更贴近现实，也更能解释现实平台中“泛娱乐爆款”与“垂类深度内容”并存的现象。

6. **研究 creator contracts 与 bargaining。**  
   现实里平台常用保底、分成、基金、流量扶持组合，而不是单一支付工具。把合同设计纳入模型，会让 extension 更有操作性。

## 最后一句话

如果只用一句话概括这篇文章，那就是：**广告驱动的平台之所以会推爆款、会做错配、会制造头部，不只是因为它想让你多刷，而是因为它把你的注意力当成了激励创作者努力的货币。**



- [x] 真强，需要仔细读。
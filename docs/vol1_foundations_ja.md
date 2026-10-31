# VED Vol.1 — 基礎篇
## Vortical Enclosure Dynamics：公理からtime-like / spatial candidate constructionへ
### 独立研究ドラフト — 2026

---

## 冒頭宣言

本書は、世界を説明するための理論である。
ただしここで言う「説明」とは、既に存在する構造を記述することではない。
説明という行為そのものが、世界に対して不可逆な操作である。

我々は通常、世界が先に存在し、それを後から理解すると考える。しかし本理論は、その順序を採らない。

$$\boxed{\text{説明は世界の外にあるのではなく、世界の内部で起きる操作である}}$$

概念を与えることは、差を固定することである。構造を描くことは、関係を閉じることである。対応関係を示すことは、選択を強制することである。したがって理論は中立ではない。

$$\boxed{\text{理論は世界を「閉じる」方向に作用する}}$$

本書は、この事実から逃げない。むしろ明示的に引き受ける。

---

## 本理論の立場

本理論は、次の前提から出発する：

$$\boxed{\text{差がある}}$$

この一文以外、いかなる構造も仮定しない。

- 空間は与えない
- 時間は前提しない
- 保存則は仮定しない
- ラグランジアンも採用しない

本書の目的は：

$$\boxed{\text{この最小公理から、どこまで世界が立ち上がるかを示すこと}}$$

である。

---

## 読者への注意

本書で提示される数式は、厳密な予言装置ではない。それらは：

$$\boxed{\text{構造を拘束するための言語}}$$

である。したがって、未完成な部分が存在し、厳密解が与えられていない箇所があり、パラメータが決定されていない。これらは欠陥ではない。

$$\boxed{\text{完全閉包が禁止されている以上、理論もまた完全には閉じない}}$$

---

## 第1章　最小公理

### 1.1 出発点

本理論は、構造・法則・存在についてformal constructionとcandidate interpretationを
提案するため、ただ一つの前提から始める。

$$\boxed{\text{差がある}}$$

これは仮定ではない。完全に対称な状態では、何も起きない。したがって、何かが起きているならば、差がある。

$$\text{完全対称} \Rightarrow \text{無変化} \Rightarrow \text{非観測}$$

ゆえに、

$$\boxed{\text{観測可能な世界} \Rightarrow \text{差が存在する}}$$

これは経験的事実ではなく、構造的な必然である。

### 1.2 差から運動へ

差が存在するとき、それは空間的・構造的な非均一性として現れる。

$$\delta \neq 0 \Rightarrow \nabla \delta \neq 0$$

当該local-field representationでは、勾配に対するeffective flowを次で表す：

$$J \sim -\nabla \delta$$

ここでは、$\nabla\delta$ は局所場として表現されたdifference fieldに、作用domainが与えられた
gradientを意味する。$J\sim-\nabla\delta$ はnormalizationを固定しないeffectiveな比例関係であり、
この式だけから普遍的必然性やpre-geometric interpretationは導かない。

この表現ではflowがcirculationを支え得る。vorticityから持続的closureへの移行は
candidate mechanismであり、この式だけから必然性や安定性は導かない。

$$\text{差} \rightarrow \text{勾配} \rightarrow \text{流れ} \rightarrow \text{渦} \rightarrow \text{閉包}$$

持続する閉包構造は、本modelにおける「存在」のcandidate interpretationである。

### 1.3 観測可能性の条件

観測とは、区別である。区別には勾配が必要である。したがって：

$$\text{観測可能} \iff \nabla L \neq 0$$

完全に閉じた構造では：

$$L = L_{\max} \Rightarrow \nabla L = 0$$

すべてが均一化し、区別は消える。

$$\boxed{\text{完全閉包} \Rightarrow \text{非観測} \Rightarrow \text{存在しないのと同じ}}$$

ここから重要な帰結が出る：

$$\boxed{L < L_{\max}}$$

完全閉包は禁止される。これは後に導入される「閉包バリア」の根拠となる。

### 1.4 ゼロドメイン

VEDでは、二つの領域を区別する。

- **記述可能ドメイン**：差が存在する。勾配が存在する。閉包動力学が成立する。数学的記述が可能。
- **ゼロドメイン**：差が存在しない。勾配が存在しない。観測できない。記述できない。

ゼロドメインは「無」である。しかし同時に、差がないため区別できないという意味で「完全な1」でもある。

$$\boxed{\text{ゼロドメインは、差がないため観測不能な領域である}}$$

### 1.5 最小公理の意味

- 差がなければ何も起きない
- 差があるなら運動が生まれる
- 運動が持続すると構造が生まれる
- 構造は完全には閉じない

したがって、

$$\boxed{\text{世界とは、差が作る非完全閉包構造の持続である}}$$

---

## 第2章　完全閉包禁止則

### 2.1 なぜ閉じてはいけないのか

閉包が極限に達した状態を考える。

$$L \rightarrow L_{\max}$$

このとき、すべての関係が固定され、勾配が消え、流れが止まり、変化が消える。

$$\nabla L = 0, \qquad J = 0$$

したがって：

$$\boxed{\text{完全閉包} \Rightarrow \text{運動の停止}}$$

### 2.2 禁止則の導出

$$\text{完全閉包} \Rightarrow \text{非観測} \Rightarrow \text{存在しないのと同じ}$$

したがって：

$$\boxed{L < L_{\max}}$$

この制約は仮定ではない。世界が存在しているという事実からの帰結である。

### 2.3 閉包バリア

$$B(L) = -\kappa_B \log\!\left(1 - \frac{L}{L_{\max}}\right)$$

この関数は $L \rightarrow L_{\max}$ で $B(L) \rightarrow \infty$ となる。

$L<L_{\max}$ はmodeled non-closure constraint、$B(L)$ はそのphenomenological / effective
barrier encodingであり、microscopic derivationではない。

$$\boxed{\text{完全閉包は力学的に禁止される}}$$

### 2.4 非完全閉包としての世界

$$\boxed{\text{世界} = \text{非完全閉包の持続構造}}$$

### 2.5 残差の役割

$$\epsilon = L_{\max} - L > 0$$

$$\boxed{\text{残差こそが運動の源である}}$$

$$\boxed{\text{世界} = \text{差によって始まり、閉じきらないことで持続する構造}}$$

---

## 第3章　ラグランジアンの試みと失敗

### 3.1 試み

閉包構造 $L$ を基本変数とし、最も単純な作用を考える：

$$S[L] = \int dt \left[\frac{1}{2} (\partial_t L)^2 - V(L)\right]$$

### 3.2 構造との不整合

ラグランジアン系では時間は外部パラメータとして与えられる。しかしVEDでは：

$$\boxed{\text{内部的なtime-like quantityを構成することが課題となる}}$$

ここで用いる外部parameterとphysical clockのidentityを区別する必要がある。この記述だけで
physical timeの導出可能性または不可能性は確立しない。

### 3.3 結論

$$\boxed{\text{ラグランジアンは「結果の理論」であり、「起源の理論」ではない}}$$

VEDが求めるのは「何が起こるか」ではなく：

$$\boxed{\text{何が残るか}}$$

---

## 第4章　履歴とログ — 構造の選択

### 4.1 H ≠ C

- $H_{ij}$：履歴（すべて）
- $C_{ij}$：ログ（残ったもの）

$$\boxed{H \neq C}$$

### 4.2 核心方程式

$$\boxed{C_{ij} = 1 - \exp(-\lambda \rho_i H_{ij})}$$

$$\rho_i = \sum_j C_{ij}$$

これらはnode-indexedなconstitutive / self-consistency relationとfixed-point targetを与える。
それ自体はupdate mapではなく、解の存在・一意性・iterationの収束・安定性を確立しない。

### 4.3 自己参照構造

$$\boxed{\text{構造が、次に残る構造を決める}}$$

$$\text{構造} \rightarrow \text{選択} \rightarrow \text{構造}$$

### 4.4 時間への接続

$$\boxed{\frac{d\tau_i}{dt} = \rho_i}$$

式のroleは、derivative / ordering parameter $t$ に相対的なnode-local time-like accumulationの
定義である。$\rho_i\geq0$ の条件下で $\tau_i$ は $t$ に関してnon-decreasingだが、この式だけで
physical clockとのidentityを与えない。

ここでの $\tau_i$ はlog accumulation / ordering quantityである。physical timeとのidentityは
proposed interpretationに留まる。

---

## 第5章　核心方程式と相図

### 5.1 ログ流

$$\boxed{J_{ij} = C_{ij} - C_{ji}}$$

### 5.2 基本方程式

$$\boxed{\partial_t \rho + \nabla \cdot J = \sigma}$$

この式はcontinuum field representation内のbalance / continuity relationである。$\sigma\neq0$
を許すため無条件のconservation lawではなく、balance formだけでphysical timeを同定しない。

ここでcontinuum $J$ / $\rho$ はdiscrete $J_{ij}$ / $\rho_i$ に対応するrepresentationとして
用いられるが、averaging、orientation、scaling、volume normalization、unit mapは表示されない。
Bridge statusは **INFORMAL / OPEN** であり、continuum equation自体のformal scopeは保持する。

ここで $t$ はVol.1のderivative / ordering parameter、$\sigma$ はVol.1のcontinuum
log-generation rateである。同じglyphを使うIFGTのeffective external $t$ / source term $\sigma$、
およびmicroscopic $\dot\rho_i$ とのidentityやprojectionは、ここでは固定しない。

$$\boxed{\sigma > 0 \quad\text{（正のsource regime）}}$$

このsource-local conditionはlog accumulation / orderingとのcandidate associationを与える。
physical-time generationとの必要十分関係は確立しない。

### 5.3 渦と閉包密度

$$\boxed{\omega = \nabla \times J}$$

これはcurlが定義できるcontinuum vector-field domainにおけるdefinition / derived constructionであり、
$\omega\neq0$ だけから持続性や安定性は導かない。

$$\boxed{L \sim |\omega|}$$

これはscalar closure intensityを与えるeffectiveな比例関係である。magnitude conventionと
normalizationは固定されず、普遍的identityとしては扱わない。

$$\boxed{\text{構造とは、流れの渦である}}$$

### 5.4 role-separated navigation summary

$$\boxed{C \rightarrow J \rightarrow \omega \rightarrow L}$$

この表示はtopic orderのmnemonicであり、各arrowは同一の生成関係を表さない。

| 局所関係 | role | status |
|---|---|---|
| causal-log $C_{ij}\to J_{ij}$ | discrete definition | formal construction |
| $J_{ij}\to\mathbf J(x)$ | discrete / continuum correspondence | INFORMAL / OPEN bridge |
| $\mathbf J(x)\to\omega$ | curl definition | formal construction |
| $\omega\to L$ | effective proportional relation | phenomenological; physical enclosureはcandidate |

repository-wideなedge分類は
[role-separated navigation record](navigation/generative_sequence.md)に従う。

### 5.5 σの有効形

$$\boxed{\sigma(\rho) = \xi \rho \left(1 - \frac{\rho}{\rho_{\max}}\right)}$$

### 5.6 宇宙方程式

$$\boxed{\frac{d\rho}{d\tau} + 3\gamma \rho^2 = \sigma(\rho)}$$

### 5.7 相構造

| 相 | 条件 | 特徴 |
|---|---|---|
| Subcritical | $\rho \approx 0,\ \sigma \approx 0$ | 構造なし |
| Active | $\sigma > 0$ | 正のlog-source regime |
| Classical-active | $\sigma \approx 0$（固定点付近） | 安定構造（GR, SM） |
| Saturated | $\rho \rightarrow \rho_{\max},\ \sigma \rightarrow 0$ | 閉包極限（BH内部） |

$$\boxed{\text{初期宇宙とBH内部を類似する}\sigma>0\text{ regimeとして提案する}}$$

---

## 第6章　空間記述の候補構成

### 6.1 距離の定義

$$\boxed{S_{ij} = \frac{1}{2}(C_{ij} + C_{ji})}$$

$$\boxed{\tilde{S}_{ij} = \max_{\gamma:i\to j} \prod_{(ab)\in\gamma} S_{ab}}$$

$$\boxed{d_{ij} = -\log \tilde{S}_{ij}}$$

これはadmissible pathsとlogが定義できるedge strengthsを持つweighted network上のpath
constructionである。ordinary metricと呼ぶには、positivity、reachability、symmetry、
zero-distance condition、disconnected pairsのpolicyを別途固定する必要がある。

$$\boxed{\text{距離とは「伝播の難しさ」である}}$$

### 6.2 physical spaceとの関係

$$\boxed{\text{ログ構造からnetwork distanceが定義される}}$$

このformal constructionはeffective spatial descriptionへのcandidate routeを与える。
physical spaceのemergenceまたはidentityは、bridgeとoperational interpretationなしには確立しない。

### 6.3 連続極限

ノード数が増え、構造が滑らかになると：

$$d_{ij} \rightarrow g_{\mu\nu}(x)$$

この矢印はeffective endpointを示すschematicな **PARTIAL / OPEN bridge** である。明示的な
reconstruction、convergence、normalization、uniquenessはここでは与えられない。

このendpointはtarget側のeffective local continuum approximationであり、unique reconstruction
またはphysical-space emergenceのtheoremではない。

$$\boxed{\text{計量テンソルをeffective endpointとして提案する}}$$

---

## 第7章　計量と重力

### 7.1 距離の修正

$$\boxed{d_{ij} = \min_{\gamma:i\to j}\sum_{(ab)\in\gamma}\left[-\log S_{ab} + \epsilon L_{ab}\right]}$$

これは表示されたedge costを入力とするformal weighted-path constructionであり、continuum gravity
またはOPENなcarrier bridgeの導出ではない。

### 7.2 計量の自己整合

$$\boxed{g_{\mu\nu} = g^{(0)}_{\mu\nu} + \alpha_G L_{\mu\nu}[g]}$$

これはeffective continuum representation内のproposed fixed-point / self-consistency targetである。
解の存在、一意性、iterationの収束、安定性はこの表示だけでは確立されない。

### 7.3 重力の本質

$$\boxed{\text{閉包密度による距離構造の歪みをgravity-like candidateとして提案する}}$$

$$\boxed{\text{渦密度とeffective geometryの対応はcandidate interpretationである}}$$

### 7.4 一般相対論との比較

$$L_{\mu\nu} \longleftrightarrow T_{\mu\nu}$$

$$\boxed{\text{閉包密度と物質sourceの関係はstructural analogyとして提案される}}$$

### 7.5 保存則の位置づけ

$$\boxed{\nabla_\mu J^\mu = \sigma \neq 0}$$

$$\boxed{\text{source-freeなbalance relationを特定のmodel phaseとして扱う}}$$

このformalなphase区分だけから、physical conservation lawがfundamentalか
emergentかは確立されない。

---

## 第8章　宇宙論 — 相としての膨張

### 8.1 膨張の再解釈

$$\boxed{\text{膨張を相の性質としてmodel化する}}$$

$\sigma>0$ は本modelのpositive-source regimeである。physical expansionとの必要十分関係は
確立しない。

### 8.2 特異点の回避

$$B(L) = -\kappa_B \log\!\left(1 - \frac{L}{L_{\max}}\right) \rightarrow \infty \quad (L \rightarrow L_{\max})$$

$$\boxed{\text{完全閉包には到達できない}}$$

これは両特異点をasymptotic closure limitとして読むcandidate interpretationを与えるが、
physical singularity avoidanceを確立しない。

### 8.3 宇宙定数

$$\boxed{\Lambda \sim \rho_* \quad \text{（構造の固定点）}}$$

$$\boxed{\text{宇宙を生成が持続する相として解釈する候補である}}$$

---

## 第9章　予測と検証可能性

### 9.1 構造的制約としての予測

VEDが提示するのは：

$$\boxed{\text{構造的制約としての予測}}$$

すなわち、何が起きうるか・何が起きえないか・どのような関係が必然かを与える。

### 9.2 σ → Δ → G：三つの統一

| 量 | 定義 | 役割 |
|---|---|---|
| $\sigma$ | ログ生成率 | positive-source regime；physical-time interpretationはOPEN |
| $\Delta = L_{\max}-L$ | 閉包バリアからの距離 | phenomenological mass-like指標 |
| $G$ | 閉包-距離変換係数 | gravity-like effective coupling候補 |

$$\boxed{\text{時間・質量・重力の関係はmodel-level correspondenceとして提案される}}$$

### 9.3 最終的な位置づけ

$$\boxed{\text{世界とは、差から生まれ、閉じきらず、選択され続ける構造である}}$$

$$\boxed{\text{決して完全には閉じない}}$$

---

## 付録：記号一覧

| 記号 | 定義 |
|---|---|
| $H_{ij}$ | 因果履歴（$i\to j$の影響強度） |
| $C_{ij}$ | 因果ログ（選択された有効構造） |
| $\rho_i$ | ログ密度 $= \sum_j C_{ij}$ |
| $\lambda$ | 選択感受性（有効パラメータ） |
| $\tau_i$ | time-like accumulation quantity（physical clock identityはOPEN） |
| $S_{ij}$ | $C_{ij}$の対称成分（空間的強度） |
| $A_{ij}$ | $C_{ij}$の反対称成分（因果流） |
| $J_{ij}$ | ログ流 $= C_{ij} - C_{ji}$ |
| $\tilde{S}_{ij}$ | 有効干渉可能性（最大経路強度） |
| $d_{ij}$ | network distance $= -\log\tilde{S}_{ij}$（physical mapはOPEN） |
| $g_{\mu\nu}$ | effective metric candidate |
| $B(L)$ | 完全閉包バリア $= -\kappa_B\log(1-L/L_{\max})$ |
| $L_{\max}$ | 完全閉包限界 |
| $\sigma$ | source-local log-generation rate |
| $\omega$ | 渦度 $= \nabla\times J$ |
| $L$ | 閉包密度 $\sim \lvert\omega\rvert$ |
| $\Psi$ | 重力ポテンシャル |

---

*Vol.1 — 基礎篇：公理・time-like / spatial candidate constructions　2026*

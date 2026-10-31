# VED Vol.3 — 重力・宇宙論の構造比較
## Vortical Enclosure Dynamics：閉包密度から重力・宇宙論へ
### 独立研究ドラフト — 2026

---

## まえがき

Vol.1では $C_{ij}$ からtime-like accumulationとnetwork distanceを構成し、physical
interpretationを候補として残した。Vol.2では閉包幾何と標準模型の構造とのstructural
correspondenceを提案した。

このVol.3 guideの $C_{ij}$ はVol.1のcausal-log identityを継承する。navigation recordsで同じ
glyphを使うclosure-degree carrierとは、ここでは同一視しない。

Vol.3では重力を扱う。核心的主張は一つ：

$$\boxed{\text{modified distanceをgravity-like descriptionの候補として用いる}}$$

本理論は現時点で定量的予測能力を持たない。構造的整理が目的である。

---

## 第1章　重力はどこから来るのか

### 1.1 Vol.1の距離、その限界

$$d_{ij} = -\log \tilde{S}_{ij}, \qquad \tilde{S}_{ij} = \max_{\gamma: i\to j} \prod_{(ab)\in\gamma} S_{ab}$$

これはadmissible pathsと積・logが定義できるedge strengthsを持つweighted network上の
path constructionであり、physical-space interpretationとは別のequation roleである。

$$\boxed{\text{この距離は、}C_{ij}\text{の構造だけで決まる}}$$

$$\boxed{\text{この定義からは、重力が出てこない}}$$

なぜか。この距離が「均質な構造」を前提にしているからである。

### 1.2 重力とは何か

$$\boxed{\text{閉包密度をdistance distortionの候補sourceとして用いる}}$$

従来：新しい力を導入する。
VED：距離の定義を修正する。

$$\boxed{\text{重力は追加されるものではなく、既存構造の再解釈である}}$$

### 1.3 距離の拡張

各辺$(a,b)$に対して、重みを：

$$w_{ab} = -\log S_{ab} + \epsilon L_{ab}$$

距離を経路コストの最小化として統一する：

$$\boxed{d_{ij} = \min_{\gamma: i\to j} \sum_{(ab)\in\gamma} w_{ab}}$$

これは表示されたedge costを入力とするformal min-path constructionであり、continuum fieldや
OPENなcarrier bridgeの導出ではない。

### 1.4 重力の本質

$$\boxed{\text{重力は「別の力」ではなく、経路選択そのものを変える}}$$

Einsteinが「力→曲率」と置き換えたように、VEDでは「曲率→経路コスト」と置き換える。

$$\boxed{\text{距離の修正はgravity-like behaviorへのcandidate routeを与える}}$$

---

## 第2章　閉包密度と幾何

### 2.1 閉包密度

$$\boxed{L_{ab} = \sum_k \phi_{abk}}$$

$$\boxed{\text{閉包密度 = 構造の密度}}$$

**Carrier note.** $L_{ab}$ はpath costに使うedge quantityである。以下の $L_{\mu\nu}$ は
proposed tensorial coarse quantity、Vol.1の $L\sim|\omega|$ はscalarである。同じ文字を共有しても
同一objectではなく、このguideは完全なcross-carrier bridgeを与えない。

### 2.2 テンソル化

$$L_{\mu\nu}(x) = \left\langle L_{ab},\, \hat{e}^{(ab)}_\mu \hat{e}^{(ab)}_\nu \right\rangle_U$$

このdisplayed averageはproposed **PARTIAL / OPEN bridge** である。sampling、normalization、
scaling / limit、tensorizationのuniqueness、およびscalar $L$ とのrelationは未構築である。

$$\boxed{L_{\mu\nu} = \text{閉包テンソル}}$$

### 2.3 計量との関係

$$g_{\mu\nu} = g^{(0)}_{\mu\nu} + \alpha_G L_{\mu\nu}$$

この式はproposed continuum description内部のrelationである。network distance $d_{ij}$ から
$g^{(0)}_{\mu\nu}$ へのbridgeは **PARTIAL / OPEN** であり、reconstruction、convergence、
normalization、uniquenessは与えられない。

$$\boxed{\text{閉包密度はproposed effective metricへ寄与する}}$$

### 2.4 有効結合としての G

$$\boxed{G_{\text{eff}} \sim \alpha_G}$$

ここでは $G$ をcoarse-grained closure structureに対応するeffective couplingの候補として扱う。

$$\boxed{\text{Gの普遍性はOPENなcoarse-graining targetである}}$$

$$\boxed{\text{閉包密度はgravity-like behaviorのcandidate sourceである}}$$

$$\boxed{\text{粗視化された閉包幾何はspacetime descriptionの候補である}}$$

ここでのdistance-to-metric connectionはeffective endpointを示す **PARTIAL / OPEN bridge** であり、
reconstruction、convergence、uniqueness、physical interpretationを確立しない。

---

## 第3章　Einstein方程式はどこから来るのか

### 3.1 出発点：固定点方程式

$$C_{ij} = 1 - \exp(-\lambda \rho_i H_{ij}), \qquad \rho_i = \sum_j C_{ij}$$

$$\boxed{\text{自己参照的な固定点方程式}}$$

### 3.2 連続表現と渦

ここで用いるcontinuum $J$ とdiscrete $J_{ij}$ の関係は **INFORMAL / OPEN bridge** である。
averaging、scaling、orientation、vector-field mapは表示されない。

$$\omega = \nabla \times J, \qquad L \sim |\omega|$$

このcontinuum vector-field representationでは、$\omega$ はrepresented flowのcurlによる定義である。
$L\sim|\omega|$ はeffectiveなscalar比例関係であり、magnitude conventionとnormalizationは固定されず、
普遍的identityまたはstability theoremではない。

$$\boxed{\text{閉包密度は流れの渦として現れる}}$$

### 3.3 計量の自己整合条件

$$g_{\mu\nu} = g^{(0)}_{\mu\nu} + \alpha_G L_{\mu\nu}[g]$$

$$\boxed{\text{計量は自分自身で決まる（固定点問題）}}$$

これはeffective continuum representation内のproposed self-consistency targetであり、解の存在・
一意性・iterationの収束・安定性は確立しない。$L_{\mu\nu}[g]$ のconstructionもbridge-dependent
のままである。

### 3.4 線形化と方程式の形

弱重力極限で：

$$\boxed{G_{\mu\nu} = 8\pi G_{\text{eff}} L_{\mu\nu}}$$

$$\boxed{\text{Einstein方程式とのstructural analogy}}$$

これはintended weak-field targetであり、係数を含む完全なlinearization、nonlinear recovery、
observational equivalenceを確立しない。

### 3.5 重要な転換

通常：Einstein方程式 = 基本法則

VED：

$$\boxed{\text{固定点構造のintended weak-field comparison}}$$

比較は古典相にscopeされる。物理的重力のemergenceまたはexact recoveryは確立しない。

$$\boxed{\text{GRは間違っていない}}$$

$$\boxed{\text{それは全てではない}}$$

---

## 第4章　Schwarzschild解 — 閉包密度の外部解

### 4.1 外部真空の解

点状の閉包分布：$L(x) = M\,\delta(x)$

外部領域（$r > R$）では $L(r) = 0$。球対称の解：

$$\boxed{\Psi(r) = -\frac{G_{\text{eff}} M}{r}}$$

$$\boxed{\text{Newtonポテンシャル}}$$

### 4.2 計量の形（弱重力極限）

$$\boxed{ds^2 \approx -\left(1-\frac{2GM}{r}\right)dt^2 + \left(1+\frac{2GM}{r}\right)dr^2 + r^2 d\Omega^2}$$

$$\boxed{\text{Schwarzschild型外部解との一次近似比較}}$$

### 4.3 地平線のVED的読み替え

地平線 $r_s = 2GM$ では $g_{tt} \to 0$。以下は、この比較対象に対するVEDの候補解釈であり、成立済みの物理的説明ではない：

$$\boxed{\text{地平線 = 経路構造の臨界点}}$$

経路コストの発散、伝播の凍結、臨界的閉包密度による相境界という読み替えは提案にとどまる。動的実現、安定性、物理的同定はOPENである。

$$\boxed{\text{GRの外部解はVEDのintended comparison targetである}}$$

完全なnonlinear recovery、係数matching、observational equivalenceはOPENである。

---

## 第5章　ブラックホール内部 — 非平衡閉包相

### 5.1 地平線 = 相の境界

$$\boxed{\text{地平線をcandidate phase boundaryとしてmodel化する}}$$

外部では古典相が成立：

$$\sigma \approx 0, \quad \nabla \cdot J \approx 0, \quad \text{固定点構造が成立}$$

地平線を越えるとこの記述条件が変わる、というmodel interpretationを提案する。

### 5.2 内部のダイナミクス

$$\boxed{\sigma > 0}$$

本modelではpositive-source regimeとし、source-free balance conditionが成立しない。

$$\boxed{\text{time-like accumulationが再びactiveになるmodel regime}}$$

これはphysical-time generationまたはthermodynamic irreversibilityを確立しない。

### 5.3 特異点を閉包極限として読む

$$B(L) = -\kappa_B \log\!\left(1 - \frac{L}{L_{\max}}\right) \to \infty \qquad (L \to L_{\max})$$

$$\boxed{\text{中心を閉包の漸近的極限として読むcandidate interpretation}}$$

### 5.4 重要な転換

通常：ブラックホール = 終点

VED：

$$\boxed{\text{ブラックホールを新しい相の入口として読む候補}}$$

$$\boxed{\text{non-singular interiorはproposed physical interpretationである}}$$

$$\boxed{\text{内部を非平衡閉包相としてmodel化する}}$$

---

## 第6章　宇宙論 — σ > 0 の全体解

### 6.1 基本方程式

連続式 $\partial_t \rho + \nabla \cdot J = \sigma$ において均一・等方近似を用いると：

ここでの $t$ と $\sigma$ はVol.1のderivative parameter / continuum sourceとしての
source-local identityを継承する。IFGTのeffective external $t$ および別途構成される
generation term $\sigma$ とは同一視しない。

$$\boxed{\dot{\rho} + 3H\rho = \sigma}$$

### 6.2 τ時間での方程式

$$\boxed{\frac{d\rho}{d\tau} + 3\gamma \rho^2 = \sigma(\rho)}$$

ここでは $H_\tau\sim\rho$ をadditional effective ansatzとして用いる。

$$H^2 \propto \rho \quad \text{（Friedmann方程式とのstructural analogy）}$$

### 6.3 σの形

$$\boxed{\sigma(\rho) = \xi \rho \left(1 - \frac{\rho}{\rho_{\max}}\right)}$$

### 6.4 de Sitter相

固定点では $H_* = \gamma\rho_* = \text{const}$ となり：

$$a(\tau) \sim e^{H_*\tau} \quad \Rightarrow \quad \boxed{\text{de Sitter型加速膨張}}$$

### 6.5 宇宙定数の起源

$$\Lambda_{\text{eff}} \sim H_*^2 = \gamma^2\rho_*^2$$

$$\boxed{\text{effective }\Lambda\text{を固定点closure scaleと対応づける}}$$

observed cosmological constantとのidentityはOPENである。

### 6.6 重要な転換

通常：宇宙膨張 = 初期条件

VED：

$$\boxed{\text{宇宙膨張を相の選択としてmodel化する}}$$

$$\boxed{\text{初期宇宙とBH内部を類似する}\sigma>0\text{ regimeとして提案する}}$$

$$\boxed{\text{continuous structural generationはcosmological model proposalである}}$$

$$\boxed{\sigma>0\text{はcandidate expansion regimeを示す}}$$

$\sigma>0$ とphysical expansionの必要十分関係は確立しない。

---

## 第7章　総括 — 構造としての世界

### 7.1 role-separated全体構造

次のdisplayはtopic orderを圧縮したhistorical mnemonicであり、各arrowが同じlogical relationを
表すわけではない。

$$\boxed{\text{差} \rightarrow C_{ij} \rightarrow J \rightarrow \omega \rightarrow L \rightarrow g \rightarrow \text{Einstein方程式} \rightarrow \text{宇宙}}$$

| 量 | 意味 |
|---|---|
| $C_{ij}$ | 因果ログ（構造の選択） |
| $J$ | ログの流れ |
| $\omega$ | 渦（回転） |
| $L$ | 閉包密度（構造の蓄積） |
| $g$ | 有効計量 |
| Einstein方程式 | 固定点近似 |
| 宇宙 | $\sigma>0$の全体相 |

| 局所関係 | navigation role | status |
|---|---|---|
| causal-log $C_{ij}\to J_{ij}$ | discrete definition | formal construction |
| $J_{ij}\to\mathbf J(x)$ | discrete / continuum correspondence | INFORMAL / OPEN bridge |
| $\mathbf J(x)\to\omega$ | curl definition | formal construction |
| $\omega\to L$ | effective proportional relation | phenomenological；enclosure mechanismはcandidate |
| $L,L_{ab}\to L_{\mu\nu}$ | carrier / coarse correspondence | PARTIAL / OPEN bridge |
| network / closure quantities $\to g_{\mu\nu}$ | effective metric target | PARTIAL / OPEN bridge |
| $g_{\mu\nu}\to$ Einstein方程式 | weak-field structural comparison | exact recoveryはDOWNGRADED / OPEN |
| Einstein comparison $\to$ 宇宙 | physical / cosmological interpretation | proposed；observational mapはOPEN |

$$\boxed{\text{すべては一つの連鎖である}}$$

ここで「一つの連鎖」は一つのresearch programに属するという意味に限定する。formal
construction、bridge、effective relation、physical interpretationは上表のとおり分離し、
[role-separated navigation record](navigation/generative_sequence.md)をrepository-wide authorityとする。

### 7.2 各Volの対応

- **Vol.1（生成）**：$C_{ij}$ の定義、time-like accumulation、network distance
- **Vol.2（構造）**：三角閉包とparticle / gauge / mass-like candidate comparisons
- **Vol.3（ダイナミクス）**：gravity-like、Einstein weak-field、cosmologyのcandidate comparisons

$$\boxed{\text{生成・構造・ダイナミクスを一つのprogram内で比較する}}$$

### 7.3 最終的な転換

$$\boxed{\text{各model constructionは構造を共通の入力として用いる}}$$

- time-like orderingとnetwork distanceはformalに構成されるが、physical identityはOPENである
- particle-like candidateはclosure minimumとして表される
- gravity-like behaviorはeffective interpretationとして提案される
- 宇宙論的phase identityはcandidate interpretationである

### 7.4 最後の一文

$$\boxed{\text{世界は閉じているのではない}}$$

$$\boxed{\text{閉じきらないことで存在している}}$$

これは本理論の出発点であり、結論でもある。

$$\boxed{\begin{aligned}
\text{time-like quantity} &= \text{ログの量} \\
\text{spatial candidate} &= \text{network log-distance} \\
\text{particle-like candidate} &= \text{閉包minimum} \\
\text{gravity-like candidate} &= \text{effective closure-density potential} \\
\text{cosmological candidate} &= \text{positive-source phase model}
\end{aligned}}$$

$$\boxed{\text{すべてが}C_{ij}\text{という一本の根から出ている}}$$

---

## 付録：記号一覧

| 記号 | 定義 | 出所 |
|---|---|---|
| $C_{ij}$ | 因果ログ行列 | Vol.1 |
| $\rho_i = \sum_j C_{ij}$ | ログ密度 | Vol.1 |
| $S_{ab}$ | $C_{ij}$の対称成分 | Vol.1 |
| $d_{ij}$ | 重み付き最短距離 | Vol.3 §1 |
| $L_{ab} = \sum_k\phi_{abk}$ | 局所閉包テンソル | Vol.2+Vol.3 |
| $J_{ij} = C_{ij}-C_{ji}$ | ログ流（反対称） | Vol.3 |
| $\omega = \nabla\times J$ | 渦度 | Vol.3 |
| $\sigma$ | Vol.1由来のcontinuum log-generation rate | Vol.1+Vol.3 |
| $\Psi$ | 重力ポテンシャル | Vol.3 |
| $\alpha_G$ | 重力結合定数（構造由来） | Vol.3 |
| $G_{\text{eff}}$ | 有効重力定数 | Vol.3 |
| $r_s = 2G_{\text{eff}}M$ | Schwarzschild半径 | Vol.3 §4 |
| $\sigma(\rho)$ | ログ生成率有効モデル | Vol.3 §6 |
| $\rho_*$ | 宇宙論的固定点密度 | Vol.3 §6 |
| $H_*$ | de Sitter膨張率 | Vol.3 §6 |

---

*Vol.3 — 重力・宇宙論の構造比較：閉包密度から宇宙へ　2026*

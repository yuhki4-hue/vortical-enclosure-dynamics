# VED Vol.2 — 標準模型篇
## Vortical Enclosure Dynamics：閉包幾何から標準模型へ
### 独立研究ドラフト — 2026

---

## まえがき

Vol.1では因果ログ $C_{ij}$ からtime-like accumulationとnetwork distanceを構成し、
physical time / spaceとの対応を候補解釈として残した。

Vol.2では同じ $C_{ij}$ から出発し、閉包幾何と標準模型の構造——粒子・ゲージ群・電荷・質量・世代・電弱統一・ヒッグス——のstructural correspondenceを提案する。核心的な比較は次である：

$$\boxed{\text{標準模型は、因果ログネットワーク上の閉包構造とその変換則の幾何学として再解釈できる}}$$

外から仮定するものは何もない。構造が先で、場はその表現である。
本理論は現時点で定量的予測能力を持たない。構造的整理が目的である。

---

## 第1章　閉包エネルギーの基礎

### 1.1 Vol.1からの接続

$$\frac{d\tau_i}{dt} = \rho_i \qquad \text{（時間）}$$

$$d_{ij} = -\log \tilde{S}_{ij} \qquad \text{（空間）}$$

$$S_{ij} = \tfrac{1}{2}(C_{ij}+C_{ji}) \quad \text{（空間的成分）}$$

$$A_{ij} = \tfrac{1}{2}(C_{ij}-C_{ji}) \quad \text{（時間・因果成分）}$$

$$\boxed{\text{この構造から「粒子」はどのように現れるのか？}}$$

### 1.2 三点で初めて「構造」が生まれる

- 2点：線しか作れない
- 3点：初めて「面」ができる

$$\boxed{\text{三点が揃ったとき、初めて「閉じた構造」が可能になる}}$$

### 1.3 三角閉包の「強さ」

$$\phi_{ijk} = \exp\!\left(-\eta |\vec{e}_i+\vec{e}_j+\vec{e}_k|^2\right) \cdot \tfrac{1}{2} |(\vec{e}_i-\vec{e}_k)\times(\vec{e}_j-\vec{e}_k)|$$

全体の閉包強度：

$$\Phi(A) = \sum_{i<j<k \in A} \phi_{ijk}$$

$$\boxed{\text{3点が揃って初めて「面積」が生まれる}}$$

### 1.4 閉包エネルギー

$$\boxed{E(A) = \alpha\left|\sum_{i\in A}\vec{e}_i\right|^2 - \beta\,\Phi(A) + \gamma|A| + B(L(A))}$$

$E(A)$ のroleはclosure configurationを比較するmodel energy / scoring functionalであり、
local minimumのphysical particle interpretationとは分ける。

| 項 | 意味 |
|---|---|
| $\alpha\lvert\sum\vec{e}_i\rvert^2$ | 閉じていないコスト |
| $-\beta\,\Phi(A)$ | 三角閉包の安定化 |
| $\gamma\lvert A\rvert$ | 構造サイズのコスト |
| $B(L(A))$ | 完全閉包の禁止（Vol.1§2.5） |

$$\boxed{\text{model-defined particleとは、このエネルギーの極小である}}$$

$$\boxed{\text{極小点はparticle-like structural candidateである}}$$

---

## 第2章　なぜ三角なのか

### 2.1 最小閉包の一意性

| 点数 | 性質 |
|---|---|
| 2 | 閉じない |
| 3 | 最小閉包 |
| 4以上 | 三角の合成 |

$$\boxed{\text{三角は、記載した有限閉包classで最小の候補である}}$$

このminimalityは当該finite simple-loop classに限る。あらゆるclosure definitionに対する
unrestricted uniquenessは主張しない。

### 2.2 閉包のタイプ

- **非退化三角**：面積あり、完全な閉包、三方向に自由度
- **退化三角**：面積ほぼゼロ、2方向のみ
- **極限退化**：1点に潰れる

$$\boxed{\text{退化度はparticle-like classの候補分類を与える}}$$

---

## 第3章　対称性は幾何から現れる

### 3.1 対称性の定義

$$\boxed{\text{対称性 = 閉包を保存する変換群}}$$

### 3.2 非退化三角とSU(3)

$$\psi\mapsto U\psi, \quad U^\dagger U = \mathbf{1}, \quad \det U = 1$$

$$\boxed{\mathrm{SU}(3) = \text{三角閉包を保ったまま位相を再配分する最小の変換群}}$$

$$\boxed{\mathrm{SU}(3)\text{は仮定ではなく、三角閉包の自由度そのものである}}$$

### 3.3 退化三角とSU(2)

$$\boxed{\mathrm{SU}(2) = \text{退化三角の内部自由度（左右枝の混合）}}$$

### 3.4 全体位相とU(1)

$$\boxed{\mathrm{U}(1)\text{は構造に影響しない冗長自由度}}$$

### 3.5 対称性の統一

| 構造 | 対称性 |
|---|---|
| 非退化三角 | SU(3) |
| 退化三角 | SU(2) |
| 全体位相 | U(1) |

$$\boxed{\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1) \text{ は閉包幾何から導かれる}}$$

### 3.6 重要な転換

通常の理解：対称性 → 粒子

VEDの理解：

$$\boxed{\text{粒子構造 → 対称性}}$$

---

## 第4章　粒子の分類 — 閉包の退化度

### 4.1 退化度による分類

$$\boxed{\text{非退化三角閉包} \leftrightarrow \text{baryon-like candidate}}$$

$$\boxed{\text{退化三角閉包} \leftrightarrow \text{lepton-like candidate}}$$

$$\boxed{\text{極限退化閉包} \leftrightarrow \text{neutrino-like candidate}}$$

### 4.2 質量との関係

$$m \propto \frac{1}{\Delta^2}$$

これはclosure model内のphenomenologicalなbarrier-based scalingであり、この式だけでobserved
particle massを導出または較正しない。

- 非退化：$\Delta$ 小 → 質量大
- 退化：$\Delta$ 中 → 質量中
- 極限：$\Delta$ 大 → 質量小

$$\boxed{\text{mass-like scale} \sim \text{closure-limit distance}}$$

$$\boxed{\text{particle-like candidateは連続構造内の候補点として表される}}$$

---

## 第5章　世代構造 — なぜ3なのか

### 5.1 三角の辺によるロック

| ロック数 | 世代 | 特徴 |
|---|---|---|
| 1辺 | 第1世代 | 軽い |
| 2辺 | 第2世代 | 中間 |
| 3辺 | 第3世代 | 重い |

$$\boxed{\text{三角の3辺は3段階の世代modelを動機づける}}$$

### 5.2 完全対称の禁止

3辺同時ロックは完全対称を要するが、Vol.1の公理より：

$$\boxed{\text{完全対称では何も起きない}}$$

$$\boxed{\text{3世代との対応はmodel-level candidateであり、普遍的必然ではない}}$$

---

## 第6章　電荷 — 位相の偏り

### 6.1 三角の対称状態からのズレ

$$q_i = \phi_i - \frac{1}{3}$$

$$q = \left(+\frac{2}{3},\, -\frac{1}{3},\, -\frac{1}{3}\right)$$

$$\boxed{+\frac{2}{3},\ -\frac{1}{3}\text{ が自然に現れる}}$$

### 6.2 電荷保存則

$$\sum_i q_i = 0$$

$$\boxed{\text{電荷保存則が自動的に出る}}$$

### 6.3 なぜ分数になるのか

$$\boxed{\text{分数電荷は三角構造の必然である}}$$

---

## 第7章　弱相互作用 — 退化構造の揺らぎ

### 7.1 2状態の混合

$$\begin{pmatrix}|L\rangle\\|R\rangle\end{pmatrix} \rightarrow U\begin{pmatrix}|L\rangle\\|R\rangle\end{pmatrix}, \quad U \in \mathrm{SU}(2)$$

$$\boxed{\text{状態の混合 = 弱相互作用}}$$

### 7.2 なぜ左手系だけか

$$\boxed{\text{左手系のみが結合する}}$$

これはパリティ非保存・CP非対称の起源になる。

### 7.3 重要な転換

通常の理解：弱相互作用 = 力

VEDでは：

$$\boxed{\text{弱相互作用 = 構造の揺らぎ}}$$

---

## 第8章　ヒッグス機構 — 退化構造の固定

### 8.1 秩序変数

$$\varphi = |\psi_L|^2 - |\psi_R|^2$$

$$\boxed{\varphi = \text{構造の偏り}}$$

### 8.2 有効ポテンシャル

$$V(\varphi) = a\varphi^2 + b\varphi^4 - h\varphi$$

$a < 0$ のとき $\langle\varphi\rangle = v_\varphi \neq 0$ となり、対称性が自発的に破れる。

### 8.3 重要な転換

通常：対称性破れ → 質量

VEDでは：

$$\boxed{\text{構造の固定 → phenomenological mass-like scale}}$$

### 8.4 Vol.2の結論

$$\boxed{\begin{aligned}
\text{particle-like candidate} &= \text{三角閉包} \\
\text{対称性} &= \text{閉包の自由度} \\
\text{世代} &= \text{辺のロック段階} \\
\text{電荷} &= \text{位相の偏り} \\
\text{弱相互作用} &= \text{退化構造の揺らぎ} \\
\text{mass-like scale} &= \text{偏りの固定}
\end{aligned}}$$

$$\boxed{\text{差がある}\to C_{ij}\to\text{三角閉包}\to\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)\to\text{標準模型}}$$

この表示はprogram-level navigation mnemonicであり、同種のderivationを並べたものではない。

| 局所関係 | navigation role | status |
|---|---|---|
| 差 $\to C_{ij}$ | upstream model organization | source-local proposal |
| $C_{ij}\to$ 三角閉包 | finite closure construction | stated admissible class内のmodel-local result |
| 三角閉包 $\to\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$ | symmetry-structure comparison | proposed structural relation |
| symmetry structure $\to$ 標準模型 | physical comparison target | OPEN physical identification；observed theoryのderivationではない |

$$\boxed{\text{標準模型との関係はstructural correspondenceとして提案される}}$$

---

## 付録：記号一覧

| 記号 | 定義 |
|---|---|
| $\vec{e}_i$ | ノード$i$の有効フラックスベクトル |
| $\phi_{ijk}$ | 三角$(i,j,k)$の非退化性評価量 |
| $\Phi(A)$ | 閉包報酬（非退化三角閉包の総和） |
| $E(A)$ | 閉包エネルギー |
| $\Delta(A)$ | 退化度（三角の面積要素） |
| $\Delta_k$ | 質量バリア距離 $= L_{\max}-L_k$ |
| $U(A)$ | 未閉度 $= 1/(1+\mathcal{R}(A))$ |
| $\varphi$ | ヒッグス秩序変数 $= \lvert\psi_L\rvert^2 - \lvert\psi_R\rvert^2$ |
| $v_\varphi$ | ヒッグスVEV |
| $\theta_W$ | ワインバーグ角 |

---

*Vol.2 — 標準模型篇：閉包幾何から電弱統一へ　2026*

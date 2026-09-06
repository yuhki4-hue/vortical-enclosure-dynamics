# 道具的成功の存在論的非自己証明性 — Case Study 01: Quantum Theory

## Scientific Identifiability Prerequisite Network applied to quantum theory

### 道具的成功・モデル内識別・補助条件・存在論的解釈の分離

- **Status:** working case study / corrigible audit / not a theorem announcement
- **Parent note:** [`tool_truth_absence_working_note_v0.2.md`](./tool_truth_absence_working_note_v0.2.md)
- **Case:** 01 — Quantum theory
- **Date:** 2026-08-16
- **Evaluation target:** Scientific Identifiability Prerequisite Network
- **Non-target:** quantum theory itself
- **Pre-registered outcome space:** positive, negative, or mixed result

---

## 1. Purpose

本ケーススタディの目的は量子論を批判することではない。量子論の不完全性、特定解釈の誤り、隠れ変数理論の優位、または「量子論には真理がない」ことを示そうとしない。

検査対象は、親ノート v0.2 で構成した **Scientific Identifiability Prerequisite Network（科学的識別可能性の前提ネットワーク／監査ネットワーク）**である。量子論は、その検証材料ではなく、ネットワークにとっての adversarial case である。

中心課題は次である。

> 成熟した量子情報・量子基礎論へ前提ネットワークを適用したとき、既存整理とは異なる診断的価値が生じるか。それとも、標準的な区別を別の順序で並べただけか。

この問いへの negative result も成功として記録する。

---

## 2. Pre-registered evaluation criteria

以下の基準は、個別ケースの結論を出す前に固定する。

### 2.1 Network passes a weak usefulness test if

- 少なくとも一つ、通常は異なる文献群で扱われる前提間の依存・代替・循環を明示できる。
- 「観測結果」「モデル内識別」「補助仮定」「存在論的橋」の混同を減らせる。
- ケースの推論構造を既存記述より明瞭にできる。

### 2.2 Network does not pass a methodological-value test if

- 既存教科書・レビューの章立てを別順に並べただけである。
- 既存の区別に新しい監査上の役割を与えない。
- どの主張も変更または明確化されない。
- 何を独立監査すべきかについて追加情報を与えない。

### 2.3 Stronger methodological contribution would require

- 複数ケースで同じネットワークを再利用できる。
- 分野ごとの見落としを実際に発見する。
- 推論または実験設計の変更を促す。
- 既存枠組みでは見えにくかった循環・依存を再現可能に指摘する。

本ケース一件だけでは、第三の基準を満たしたとは判定しない。

---

## 3. Scope, non-goals, and claim tags

### 3.1 Scope

本ノートは四つの限定されたケースを扱う。

1. **Q1:** 有限次元 quantum state tomography。
2. **Q2:** ensemble、fresh preparation、single-copy limit。
3. **Q3:** Bell-type inference の推論構造。
4. **Q4:** 量子形式体系の成功から解釈へ進む bridge。

量子場理論、無限次元 tomography、量子重力、全ての解釈史を包括しない。Q1 の主モデルは既知の有限次元 Hilbert 空間と既知の POVM である。Q2 以降で、その既知性を緩めたときに何が壊れるかを監査する。

### 3.2 Preserved constraints from v0.2

本ケースでも次を変更しない。

- 観測成功と存在論的一意性は同じ命題ではない。
- 観測成功は、存在論的主張への強い証拠になりうる。
- 自己包含だけから普遍的不可能性は出ない。
- `inside/outside` ラベルだけから識別能力差は出ない。
- informational refinement と physical joint realizability は異なる。
- dynamic CIF、preparation / initial independence、EA は異なる。
- candidate-class adequacy と within-model identifiability は異なる。
- 前提ネットワークは一本道ではない。
- 中心原理は新しい数学定理ではない。

### 3.3 Claim tags

- **[MODEL-RELATIVE]** 指定された量子モデル内部で証明・計算される。
- **[EMPIRICALLY SUPPORTED]** 明示された実験・統計手続から支持される。
- **[DESIGN ASSUMPTION]** 装置・配置・プロトコル設計により支えられるが、target success だけからは出ない。
- **[STATISTICALLY CONSTRAINED]** 有限標本モデルと明示された検定・推定手続の下で範囲が制約される。
- **[NOT SELF-CERTIFIED]** target success だけからは導出されない。根拠がないという意味ではない。
- **[SYNTHESIS]** 既存結果を本監査目的に沿って再配置した読み。
- **[OPEN]** 定義、文献監査、または経験的評価が未完である。

量子形式体系内の定理を、量子状態の存在論についての `[ESTABLISHED]` 命題へ読み替えない。

---

## 4. Mapping the v0.2 network to quantum theory

量子ケースでは、ネットワークは少なくとも次の分岐をもつ。

```text
[target: state / channel / behavior / ontology]
                  │
      [dimension and candidate class]
                  │
       ┌──────────┼───────────┐
       ▼          ▼           ▼
 [known POVM] [preparation] [causal/Bell model]
       │       equivalence      │
       │       + independence   ├── dynamic shielding
       │          │             └── setting/source assumptions
       ├──────────┤
       ▼          ▼
 [measurement  [fresh samples / product interface]
  richness]       │
       └──────┬───┘
              ▼
 [recorded frequencies / correlations]
       ┌──────┼───────────┐
       ▼      ▼           ▼
 [ideal ID] [finite-N] [model checks / calibration]
       │      │           │
       └──────┴─────┬─────┘
                    ▼
 [formal or model-class conclusion]
                    │
     [additional ontological bridge]
```

これは論理含意図ではない。fresh preparation は noncommuting measurements の同一試料上での joint realizability を回復するのではなく、**異なる試料の結果を共通状態パラメータへ統合する代替経路**を与える。Bell 型実験では、dynamic shielding と初期 setting independence が別枝になる。

---

## 5. Case Q1 — Quantum state tomography

### 5.1 Fixed finite-dimensional model

候補クラスを

$$
\Omega_d
=
\left\{
\rho\in\mathbb C^{d\times d}
\;\middle|\;
\rho=\rho^\dagger,\ \rho\ge 0,\ \operatorname{Tr}\rho=1
\right\}
$$

とする。測定 setting を $s$、結果を $y$ とし、既知の POVM 族を

$$
\mathcal M
=
\left\{
E^{(s)}_y\ge 0,
\quad
\sum_y E^{(s)}_y=I
\right\}_{s,y}
$$

とする。観測法則は Born rule

$$
p(y\mid s,\rho)
=
\operatorname{Tr}\!\left(\rho E^{(s)}_y\right)
$$

である。ここで既に、$d$、状態空間、POVM の行列表現、setting の意味、Born rule、各 run がどの $\rho$ に属するかが固定されている。これらは観測頻度そのものと同じ対象ではない。

Q1 の target specification は「指定された $d$ 次元モデル内の full density operator」である。選択した期待値だけを予測する target なら full informational completeness は不要になりうる。反対に full-state target を選んでも、必要な POVM が装置上で利用可能か、nominal effects と実現 effects が一致するか、同じ preparation procedure を反復できるかは別の experiment-availability / calibration / preparation 条件である。さらに、

$$
\theta_\star\in\Omega_d
$$

は within-model の単射性からは出ない。

### 5.2 Informational completeness and ideal identifiability

測定写像を

$$
T_{\mathcal M}:\operatorname{Herm}(\mathbb C^d)\to\mathbb R^m,
\qquad
T_{\mathcal M}(X)_{s,y}
=
\operatorname{Tr}\!\left(XE^{(s)}_y\right)
$$

とする。

**Proposition Q1.1 [MODEL-RELATIVE].** 既知の有限次元 $d$ と既知の POVM 族 $\mathcal M$ を固定する。$\{E^{(s)}_y\}_{s,y}$ が Hermitian operator space を線形に張るなら、$T_{\mathcal M}$ は $\Omega_d$ 上で単射である。従って理想的な全確率が既知なら、$\rho$ はこの候補クラス内で一意に識別される。

**Proof sketch.** $T_{\mathcal M}(\rho_1)=T_{\mathcal M}(\rho_2)$ とする。すると $\Delta=\rho_1-\rho_2$ は全ての $E^{(s)}_y$ と Hilbert–Schmidt 内積がゼロである。effects が Hermitian space を張るなら、$\Delta$ は全 Hermitian operator と直交し、特に $\Delta$ 自身と直交するので $\operatorname{Tr}(\Delta^2)=0$、従って $\Delta=0$ である。逆に測定族が状態差を分離しなければ、非零の traceless Hermitian $H$ が kernel に残り、十分小さい $\epsilon$ と full-rank state $\rho_0$ に対して $\rho_0\pm\epsilon H$ が同じ観測確率を与える。informational completeness の標準的な frame 表現については [Scott 2006](https://doi.org/10.1088/0305-4470/39/43/009) および [D’Ariano, Paris & Sacchi 2003](https://doi.org/10.1016/S1076-5670(03)80065-4) を参照。

これは v0.2 の普遍的不可能性を回復しない。むしろ、明示された候補クラスと experiment family の下では完全識別が可能な具体例である。

$$
\boxed{
\text{quantum theory}
\not\Rightarrow
\text{universal observational non-identifiability}
}
$$

### 5.3 Identifiability, estimability, stability, adequacy, ontology

| Question | Object | What can be established | What does not follow |
|---|---|---|---|
| **A. Identifiability** | $T_{\mathcal M}:\rho\mapsto p(\cdot\mid\rho)$ | IC なら理想確率に対して単射 [MODEL-RELATIVE] | 有限データで $\rho$ を誤差ゼロ復元できること |
| **B. Estimability** | counts $n_{s,y}$ からの estimator $\hat\rho_N$ | sampling model、loss、confidence procedure の下で誤差率・信頼領域を評価できる | estimator の一点出力が真値と一致すること |
| **C. Stability** | $T_{\mathcal M}^{-1}$ の conditioning | finite-dimensional IC map は image 上に連続逆をもつが、その条件数は measurement frame に依存 | IC であるだけで数値的・統計的に良条件であること |
| **D. Candidate-class adequacy** | 実過程が一つの $d$ 次元 state と既知 POVM で表されるか | drift、leakage、SPAM、goodness-of-fit を別テストで制約できる | $\Omega_d$ 内の fit が $\theta_\star\in\Omega_d$ を自己証明すること |
| **E. Ontological interpretation** | 識別された $\rho$ が世界の何を表すか | 追加の解釈・理論比較により支持を変えうる | density operator のモデル内一意性から、一意な state ontology が出ること |

従って本ケースの中心区別は

$$
\boxed{
\text{state identifiability}
\neq
\text{state ontology}
}
$$

である。ただしこれは新定理ではなく、統計的対象と解釈対象の区別を圧縮した記法である。

### 5.4 Finite-sample estimation

有限回の測定では経験頻度 $\hat p_N$ は一般に Born probability $p_\rho$ と一致しない。従って tomography は、単射性だけでなく estimator、loss function、sampling model、confidence statement を必要とする。[Christandl & Renner 2012](https://doi.org/10.1103/PhysRevLett.109.120403) は quantum tomography に confidence region を与え、有限標本の一点推定と operational error bound を区別した。

ここでの監査結果は次である。

- **[MODEL-RELATIVE]** IC は理想 law の識別条件である。
- **[STATISTICALLY CONSTRAINED]** finite-$N$ accuracy は confidence region、concentration、likelihood などで評価される。
- **[OPEN unless specified]** iid、exchangeability、adaptive sampling、memory をどの統計モデルで扱うか。
- **[NOT SELF-CERTIFIED]** 良好な fit だけから、全 run が同じ state を共有したことは出ない。

### 5.5 Inverse stability

effects を frame とみると、線形 inversion の誤差増幅は frame operator の最小特異値または condition number に依存する。IC であることは kernel がないことを保証するが、kernel に近い方向がないことまでは保証しない。tight IC measurements は conditioning と reconstruction formula の観点から特別な構造をもつ [Scott 2006](https://doi.org/10.1088/0305-4470/39/43/009)。

従って、

$$
\text{injective}
\not\Rightarrow
\text{well-conditioned}
$$

である。これは量子固有の哲学的限界ではなく、有限次元逆問題の標準的区別である。

### 5.6 Candidate-class adequacy and misspecification

通常の state tomography は、少なくとも次を仮定または別途検証する。

- Hilbert-space dimension $d$ が適切である。
- nominal POVM と実現 POVM の差が制御される。
- source が測定 setting の順序とともに drift していない。
- preparation が一つの固定 $\rho$ または宣言した時間依存モデルで記述される。
- 漏れ準位、選択バイアス、未記録 outcome が無視できるかモデル化される。

[van Enk & Blume-Kohout 2013](https://doi.org/10.1088/1367-2630/15/2/025024) は、異なる測定のデータが単一 state/process で説明できるという標準 tomography model が source drift などで失敗しうることと、alternative-model comparison による診断を論じた。これは candidate-class adequacy が「根拠なし」であることを意味しない。randomized measurement order、calibration、hold-out prediction、time-tagged residual、drift model、leakage test などにより独立に制約できる。

一方、state と POVM を同時に未知とすると probability model は bilinear になり、reference-frame または gauge freedom が現れる。self-consistent process / gate-set tomography は state-preparation-and-measurement error を同時推定するが、全ての gauge をデータだけで消すわけではない [Merkel et al. 2013](https://doi.org/10.1103/PhysRevA.87.062119)。ここでは「校正を不要にした」というより、**校正対象を joint model と gauge quotient へ移した**と読む方が安全である。

### 5.7 Verdict on the provisional Q1 proposition

> 情報完全な測定族と適切な統計条件があれば、指定された有限次元量子状態モデル内で $\rho$ は識別可能になりうる。

**Verdict:成立する。ただし within-model / ideal-law statement として。**

成立条件は少なくとも、固定された有限 $d$、識別対象としての density operator、既知または共同モデル化された measurement effects、informational completeness、run の割当てを正当化する sampling/preparation model である。finite-sample accuracy、conditioning、model adequacy、ontology は別に監査する。

---

## 6. Case Q2 — Ensemble, fresh preparation, and single-copy limits

### 6.1 What ordinary tomography identifies

標準的な fresh-copy tomography は、多くの場合

$$
\rho^{\otimes N}
$$

またはそれに十分近い sampling model を用いる。これは「未知の一個体を複製装置に入れて $N$ コピーを作る」という意味ではない。同じ制御された preparation procedure が $N$ 個の試料を供給し、それらを同じ state parameter $\rho$ で記述するというモデルである。

ここで少なくとも四条件を分ける。

1. **Re-preparability / operational repeatability:** 宣言した preparation procedure を必要回数だけ再実行できる。
2. **Preparation equivalence:** 各 run の marginal state を同じ $\rho$ とみなせる。
3. **Run-to-run independence:** joint state または outcome law が積に因子化する。
4. **Stationarity / no drift:** run index や setting order により state が系統変化しない。

procedure を再実行できても同じ state が出るとは限らず、同じ marginal をもつ相関試料もありうるため、1、2、3 は別条件である。3 を仮定しても、時間とともに異なる $\rho_t$ が現れるなら 4 は失敗する。ここでいう repeatability は source procedure の再実行可能性であって、projective measurement の repeatability や同一 outcome の反復を意味しない。tomography の target success だけで四つを一括して自己証明することはできないが、randomization、time-stamp、interleaving、drift test、source monitor により別々に支持できる。

### 6.2 Single historical system versus repeated preparation

**Question.** 「量子状態 $\rho$ を tomography できる」という事実は、一回限りの個別量子系について、その全状態を一つの履歴から取得できることを意味するか。

**Answer:一般には意味しない。**

候補クラス $\Omega_d$ は互いに非直交な純粋状態を含む。標準量子論では非直交状態を単一試行で誤りなく決定論的に識別できない。従って、任意未知 $\rho\in\Omega_d$ を一コピーから常に正確に同定する POVM は存在しない。これは quantum state discrimination の標準的限界であり、非直交状態の deterministic perfect discrimination が禁止されることは [Mohseni, Steinberg & Bergou 2004](https://doi.org/10.1103/PhysRevLett.93.200403) でも実験的文脈とともに明示されている。

有限個 $N$ の同一試料があっても、連続な全状態空間上の未知 state を有限データから一般に誤差ゼロで決めることはできない。[Massar & Popescu 1995](https://doi.org/10.1103/PhysRevLett.74.1259) は有限 ensemble からの最適状態推定を扱い、collective measurement が separate measurement より有利になりうることを示した。これは多数試料上の physical joint measurement であり、単一の歴史的個体の全状態読出しではない。

この結論から「個別量子状態は存在しない」は出ない。得られるのは、**標準量子測定インターフェースにおける一コピー完全識別の不可能性**であって、state ontology の否定ではない。

### 6.3 Product/preparation interface is not same-token joint realizability

fresh preparation を使う tomography では、全試料を subset $I_s$ に分け、setting $s$ の POVM をそれぞれに実行し、結果を共通の $\rho$ へ統合する。

```text
source procedure
   ├── sample 1 ── measure setting X
   ├── sample 2 ── measure setting Y
   ├── sample 3 ── measure setting Z
   └── ...       ── combine records under common-ρ model
```

これは noncommuting $X,Y,Z$ を同じ token に同時実行することではない。従って、v0.2 の語彙では次のように分類する。

- **Product experiment:** 複数の fresh samples 上で異なる実験結果を結合する。
- **Experimental amalgamation:** common-$\rho$ model、preparation equivalence、記録保存を用いて情報を一つの推定へ統合する。
- **Physical joint realizability:** collective POVM を実際に $\rho^{\otimes N}$ 上で行う場合には $N$-partite system 上で成立するが、一個の元試料上で全測定を共同実行したことにはならない。
- **Informational refinement:** 推定した $\rho$ から未実行 POVM の確率 $\operatorname{Tr}(\rho E)$ を計算できること。未実行の individual outcome を過去へ遡って得たことではない。
- **Blackwell refinement:** 共通の候補クラス上で、一方の experiment の outcome law が他方から stochastic post-processing で得られるという比較である [Blackwell 1953](https://doi.org/10.1214/aoms/1177729032)。IC であることや、推定後に確率を計算できることだけで、有限標本 protocol 間の Blackwell dominance まで自動的に従うわけではない。

physical joint realizability は、どの carrier と resource scope に相対的かも指定しなければならない。複数試料を用いる batch protocol 全体は、source、測定順序、記録を合成できれば一つの物理的 protocol として実現できる。しかし、それは各 noncommuting measurement が同じ carrier 上で共同実現されたことを意味しない。collective POVM はさらに強い、複数 carrier への joint quantum access である。

従って fresh preparation は、same-token physical joint realizability と同じではなく、**preparation/product interface による代替経路**である。

### 6.4 No-cloning and no-broadcasting: exact scope

[Wootters & Zurek 1982](https://doi.org/10.1038/299802a0) の no-cloning theorem は、任意の未知純粋状態を完全にコピーする universal physical process を禁じる。[Barnum et al. 1996](https://doi.org/10.1103/PhysRevLett.76.2818) の no-broadcasting theorem は、一般の非可換混合状態族を、両 marginal に元状態が残る形で broadcast できないことを示す。

これらが直接禁止しないものには、次がある。

- preparation procedure を再実行して同じ nominal state を作ること。
- 既知状態、互いに直交する状態、または可換な特定状態族を複製・broadcast すること。
- approximate cloning、または特定の線形独立な純粋状態族などに限定した probabilistic cloning。
- 既に供給された複数試料へ collective measurement を行うこと。
- restricted candidate class 上で必要な property だけを推定すること。

従って no-cloning は「量子状態は識別できない」という一般命題を与えない。制約するのは、**未知入力から任意に product interface を製造する特定の物理操作**である。

### 6.5 Five distinct quantum constraints

| Constraint | What it says | What it does not say |
|---|---|---|
| **No-cloning** | 任意未知純粋状態を完全コピーする universal channel はない | source の repeated preparation が常に不可能 |
| **Measurement incompatibility** | 指定測定族が一つの parent POVM の marginals として共同実現できない場合がある | 別試料上で各測定を実行できない |
| **Contextuality** | 指定 scenario と仮定の下で noncontextual ontological assignment が不可能 | 全解釈が一意に決まる。Kochen–Specker の原結果は [Kochen & Specker 1967](https://doi.org/10.1512/iumj.1968.17.17004) |
| **Destructive measurement** | 特定 instrument が測定後 state または carrier を不可逆に変える | 全 POVM が destructive、または外部観測者だけは影響を免れる |
| **One-copy limitation** | available resource が一試料に限定される | no-cloning theorem と論理的に同一、または state ontology が否定される |

この五つは相互に関係するが同義ではない。とくに POVM は outcome probabilities を定めても、post-measurement state update を一意に定めない。destructiveness と informational completeness は別軸である。

### 6.6 Q2 network audit

| Network node | Quantum realization | How it is secured | Failure mode | Audit status |
|---|---|---|---|---|
| repeatability / re-preparability | source procedure を必要回数だけ再実行 | source control、throughput test、protocol bookkeeping | procedure exhaustion、history dependence | independently testable / design-certified |
| fresh preparation | 同じ source procedure の再実行 | source control、interleaving、monitoring | drift、setting-dependent preparation | independently supported / design-certified |
| preparation equivalence | 各 sample に共通 $\rho$ を割り当てる | goodness-of-fit、drift model、replication | nominally same procedure が異なる state を出す | statistically constrained / model-relative |
| independence | $\rho^{\otimes N}$ または factorized outcome law | randomization、memory tests、protocol model | correlated noise、memory、batch effect | design-certified / not fully self-certified |
| destructive measurement | instrument-specific state update | detector characterization、control experiments | 後続測定へ情報が残らない | independently testable / model-relative |
| product experiment | multiple samples を一つの推定へ統合 | source throughput、sample bookkeeping | sample identity、drift、correlation | design-certified |
| sequential composability | 同一 sample 上で測定後も次操作可能 | nondemolition/weak instrument、known dynamics | back-action、loss、absorption | independently testable |
| EA | 複数 setting の情報を common target へ統合 | common-$\rho$ model、stable records | domain mismatch、setting-dependent source | model-relative / statistically constrained |
| informational refinement | $\hat\rho$ から他 POVM probability を算出 | Born model と estimator | model misspecification | analytically guaranteed within model |
| physical joint realizability | collective POVM on supplied $N$ systems | joint control hardware | same-token inference との混同 | design-certified / experiment-specific |
| no-cloning / broadcasting | arbitrary unknown input の自由コピー制約 | standard quantum dynamicsからの定理 | product access 全般の禁止へ過剰一般化 | analytically guaranteed / quantum-specific |

---

## 7. Alternative identification paths

前提ネットワークが一本道でないことは、量子 tomography の複数経路に明確に現れる。

| Route | What is reduced or substituted | New or strengthened assumptions | What is actually identified |
|---|---|---|---|
| **Controlled dynamics + repeated incomplete measurement** | 一時点での measurement richness を、既知 dynamics と複数時刻の effective observables で補う | dynamics/calibration/control の正確さ、observability、しばしば repeated ensemble | initial state または選択された parameters |
| **Continuous weak measurement** | 強い destructive measurement を、時間連続 record と controlled evolution で代替 | back-action model、filter model、record bandwidth、known control | conditional/current state または ensemble initial state。Silberfarb et al. の原提案は ensemble average を用いる [Silberfarb, Jessen & Deutsch 2005](https://doi.org/10.1103/PhysRevLett.95.030402) |
| **Ancilla-assisted process tomography** | 多数の probe-state settings の一部を、ancilla correlation と joint measurement で代替 | faithful joint input、ancilla control、larger Hilbert space、joint calibration | quantum operation。単一の未知 state の全読出しではない [D’Ariano & Lo Presti 2001](https://doi.org/10.1103/PhysRevLett.86.4195) |
| **Compressed-sensing tomography** | full $d^2$-scale measurement richness を低 rank / sparsity で代替 | restricted candidate class、incoherence、noise model | low-rank または approximately low-rank state [Gross et al. 2010](https://doi.org/10.1103/PhysRevLett.105.150401) |
| **Randomized measurements / classical shadows** | full-state reconstruction を、多数の target properties の prediction へ弱める | randomized control、independent samples、observable class、error criterion | selected functions of $\rho$。一般の full tomography と同じ target ではない [Huang, Kueng & Preskill 2020](https://doi.org/10.1038/s41567-020-0932-7) |
| **Process tomography** | state target を channel target へ変更 | spanning input states、output tomography、CP/TP model | quantum channel [Chuang & Nielsen 1997](https://doi.org/10.1080/09500349708231894) |
| **Gate-set tomography** | pre-calibrated SPAM への依存を joint self-consistent estimation へ移す | gate-set richness、sequence model、stationarity、gauge quotient | state/preparation/measurement/gates の同値類 [Merkel et al. 2013](https://doi.org/10.1103/PhysRevA.87.062119) |

この表は「reset が不要になった」などの単純な代替を示さない。多くの場合、ある資源を減らすと別の候補制限、制御、ancilla、時間、stationarity、gauge choice が強くなる。

**[SYNTHESIS] Q2 のネットワーク上の利点**は、fresh copies、same-token sequential access、collective measurement、post-processing reconstruction を一語の「tomography」に畳み込まず、どの経路がどの前提を代替したかを表示できる点にある。ただし、これらの区別自体は quantum estimation / information 文献で既知である。

---

## 8. Case Q3 — Bell-type inference

### 8.1 Bell data are conditional behavior, not an interpretation label

Bell 型実験で直接集計される対象は

$$
P(a,b\mid x,y),
$$

すなわち二地点の settings $x,y$ に条件づけた outcomes $a,b$ の頻度または推定確率である。Bell の原論文は、量子予測が特定の局所 hidden-variable 構造と両立しないことを示した [Bell 1964](https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195)。

標準的な local hidden-variable class の一形式は

$$
P(a,b\mid x,y)
=
\int d\lambda\,\mu(\lambda)
P(a\mid x,\lambda)
P(b\mid y,\lambda).
$$

この表示には少なくとも次が含まれる。

- **local factorization / local causality:** local outcome response が remote setting を直接引数にとらない。
- **measurement-setting independence:** source-side latent variable の分布が settings と相関しない。
- **common trial/sample definition:** 観測された event が、Bell bound を導いた trial ensemble に対応する。
- **statistical model:** 有限列から null class をどう棄却するか。

measurement independence を明示するなら

$$
\mu(\lambda\mid x,y)=\mu(\lambda)
$$

である。これは Bell causal structure における特定の初期独立性であり、一般の全ての seed independence と同じではない。

### 8.2 What a violation excludes

Bell functional $\mathcal B$ と local bound $\beta_L$ が

$$
\mathcal B(P)\le \beta_L
$$

を local model class の全要素について満たすとする。実験推定が、有限標本統計と事前指定した解析の下でこの bound を有意に超えるなら、排除されるのは次の conjunction である。

```text
specified local factorization
+ specified setting/source independence
+ specified event/detection/trial model
+ statistical null
```

従って「Bell violation は locality という一語だけを無条件に否定する」より、**明示された local causal model class を排除する**と記す方が正確である。[Brunner et al. 2014](https://doi.org/10.1103/RevModPhys.86.419) は Bell nonlocality のモデル・実験・情報理論上の標準的整理を与える。

これは弱い結論ではない。排除するクラスは広く、量子相関との不整合は数学的に明確である。補助条件の明示は推論の欠陥ではなく、その射程を定める。

### 8.3 Major assumptions and how experiments audit them

| Component | Bell realization | How it is constrained | What success alone does not prove |
|---|---|---|---|
| observed statistics | time-tagged $a,b,x,y$ records | preregistered windows、counting、randomized settings、replication | 記録が全 relevant event を漏れなく表すこと |
| local model class | factorizable response model | theorem and polytope/inequality analysis | その class が全 ontology を尽くすこと |
| setting independence | $\mu(\lambda\mid x,y)=\mu(\lambda)$ | RNG design、spacetime arrangement、cosmic/human setting schemes | 任意に古い common cause が絶対にないこと |
| detector/sampling | detected events が target trials を表す | high-efficiency detection、event-ready protocol、no-postselection analysis | detector model の全正しさ |
| source assumptions | trial structure、pairing、latent source process | heralding、source monitor、timing、memory-robust statistics | source が候補外 dynamics を持たないこと |
| spacetime separation | settings/outcomes の relevant events が spacelike | surveyed distance、clock calibration、fast switching | 採用した event-boundary model の自己証明 |
| statistical rejection | local null の $p$-value / confidence bound | martingale、prediction-based ratio、finite-statistics analysis | 排除した class 外の ontology の順位 |

2015 年の Hensen et al. は 1.3 km 離れた electron-spin system で event-ready Bell test を行い [Hensen et al. 2015](https://doi.org/10.1038/nature15759)、Giustina et al. と Shalm et al. は高効率 photon detection と高速 settings を用いた tests を報告した [Giustina et al. 2015](https://doi.org/10.1103/PhysRevLett.115.250401)、[Shalm et al. 2015](https://doi.org/10.1103/PhysRevLett.115.250402)。これらは locality と detection の主要 loopholes を同一実験で大幅に封鎖したという強い実験的成果である。

`loophole-free` は、無仮定または全 ontology 排除を意味する語として読まない。装置 event の時空境界、random setting の物理モデル、有限標本解析などはなお明示される。一方、残る論理仮定の存在だけを理由に実験を「無意味」と評価することも誤りである。実験は、各 failure route を物理設計・校正・統計解析で狭めている。

### 8.4 Dynamic CIF is not measurement independence

Bell case で v0.2 の分離を維持する。

#### Dynamic CIF

dynamic CIF が問題にするのは、settings が選択された後または trial 中に、宣言チャネルを迂回する情報経路が対象・remote wing・detector へ到達することである。例は、electronic cross-talk、setting signal の unintended leakage、timing protocol 外の subluminal communication、未記録 feedback である。spacelike separation、shielding、timing audit はこの種の経路を制約する。

この CIF 判定は、どの event、device state、channel を causal variables として宣言したかに相対的である。変数分解の外に置いた経路が存在しないことを、Bell violation の値だけが保証するわけではない。

#### Preparation / initial independence

measurement independence が問題にするのは、trial に先立つ source latent variable $\lambda$ と settings $x,y$ の統計的関係である。動的 leakage がなくても共通原因があれば失敗しうる。逆に初期独立性を仮定しても、trial 中の cross-talk があれば dynamic CIF は失敗しうる。

[Hall 2010](https://doi.org/10.1103/PhysRevLett.105.250404) は measurement independence を緩和した local deterministic correlation model を具体的に解析した。これは `measurement dependence` が一つの数学条件の破れを指し、その causal interpretation が一意ではないことを示す材料になる。`measurement dependence = superdeterminism` とは定義しない。superdeterminism、通常の common cause、setting-device memory、retrocausal proposal は異なる causal stories である。

cosmic Bell tests は distant astronomical photons で settings を選び、setting correlation を説明する common cause の許容時刻を遠い過去へ押し戻す設計を採った [Handsteiner et al. 2017](https://doi.org/10.1103/PhysRevLett.118.060401)。これも independence を論理的に自己証明するのではなく、特定の correlation route を設計上さらに制約する。

### 8.5 Bell violation does not select one ontology

Bell violation は、指定仮定を満たす local hidden-variable class を排除する。そこから次は出ない。

- Everett、Bohm、Copenhagen-family、information-centered view の一つが自動的に選ばれる。
- hidden variables 一般が排除される。Bohmian mechanics は非局所構造をもつ。
- measurement dependence を採る全モデルが同一の superdeterministic ontology になる。
- quantum formalism 以外の全 candidate class が排除される。

従って Q3 は、

$$
\text{strong model-class discrimination}
\not\Rightarrow
\text{unique ontological interpretation}
$$

を示すケースである。同時に、補助条件があることと科学的推論が弱いことが同義でないことも示す。Bell research は補助条件を放置せず、loophole ごとに装置・時空配置・統計を改良してきた。

### 8.6 Q3 audit verdict

- **[MODEL-RELATIVE]** Bell inequality は指定 local behavior class の bound である。
- **[EMPIRICALLY SUPPORTED]** 複数の独立実験で量子予測と整合する violation が得られ、主要 loopholes は同一実験内で封鎖されてきた。
- **[DESIGN ASSUMPTION]** spacetime separation、setting generation、event definition は装置設計・校正で支持される。
- **[STATISTICALLY CONSTRAINED]** 有限標本棄却は明示的な null と解析に相対的である。
- **[NOT SELF-CERTIFIED]** violation 自身は measurement independence、全装置モデル、unique ontology を同時に証明しない。

この分類の最後の行は、上の四行を無効化しない。

---

## 9. Case Q4 — From formal success to interpretation

### 9.1 Four different questions

| Layer | Quantum question | Typical evidential object | Possible conclusion |
|---|---|---|---|
| **Formalism identification** | どの state、observable、channel、Hamiltonian がデータを記述するか | tomography、spectroscopy、process characterization | 指定形式モデル内の parameter / equivalence class |
| **Empirical adequacy** | どの domain と精度で Born statistics や dynamics が成功するか | prediction、intervention、replication、error model | target domain での adequacy |
| **Model-class discrimination** | どの competing class が実験に反するか | Bell、contextuality、collapse bounds、PBR-type no-go results | 仮定を明示した class exclusion |
| **Ontological bridge** | $\rho$、$\psi$、branch、particle position、probability を何として読むか | formal success に加え、説明・統合・追加原理 | 解釈的・形而上学的主張。データから自動出力されない |

最初の三つは量子科学の通常の理論・実験課題であり、強い結果をもちうる。第四はそれらから無関係ではないが、同一ではない。

### 9.2 Interpretation families are not one empirical equivalence class

以下は勝敗表ではなく、bridge の型が異なることを示す最小比較である。

| Family / theory | Additional bridge or structure | Relation to standard operational predictions | Audit caution |
|---|---|---|---|
| **Copenhagen-family approaches** | classical description、complementarity、measurement context 等を異なる仕方で重視する。Bohr の一次資料は [Bohr 1928](https://doi.org/10.1038/121580a0) | 通常の quantum formalism の運用と密接だが、「Copenhagen」は単一の公理化モデルではない | family 全体へ一つの collapse ontology を割り当てない |
| **Everett / relative-state approaches** | universal unitary state、relative states、branch/weight の解釈 | Everett の原形式は projection を基本力学に置かない [Everett 1957](https://doi.org/10.1103/RevModPhys.29.454) | branch、probability、preferred structure の扱いを単なる notation と決めつけない |
| **Bohmian mechanics** | particle configuration、guiding dynamics、quantum equilibrium | nonrelativistic quantum equilibrium では Born statistics の導出を目指す [Bohm 1952a](https://doi.org/10.1103/PhysRev.85.166)、[Dürr, Goldstein & Zanghì 1992](https://doi.org/10.1007/BF01049004) | nonlocal structureをもち、「hidden variable 一般が Bell で排除」と書かない。拡張・非平衡 variant まで一括しない |
| **QBism and other information-centered views** | quantum state を agent の確率判断または情報的対象として読むなど、互いに異なる bridge | QBism は Born rule と quantum formalism を独自の規範的・agent-centered 意味で用いる [Fuchs, Mermin & Schack 2014](https://doi.org/10.1119/1.4874855) | QBism、operationalism、relational views、ontological-model の $\psi$-epistemic class を同義にしない |
| **Objective-collapse models** | Schrödinger dynamics 自体を stochastic collapse で修正 | standard quantum theory と近似的一致域をもちつつ、原理的には異なる予測をもちうる [Ghirardi, Rimini & Weber 1986](https://doi.org/10.1103/PhysRevD.34.470) | 「解釈は全て同じ経験予測」の反例。interpretation と modified theory の境界を明記する |

この表は、standard domain で同じ operational probabilities を再現する限定された formulation 同士がありうることを否定しない。しかし、全ての解釈・修正理論・拡張理論が全 domain で経験的同値だとは言わない。

### 9.3 No-go theorems constrain bridges without selecting a unique one

Pusey–Barrett–Rudolph theorem は、独立に準備された systems の ontic states に preparation independence を課す ontological-model framework で、重なりをもつ一群の $\psi$-epistemic models が quantum prediction と両立しないことを示す [Pusey, Barrett & Rudolph 2012](https://doi.org/10.1038/nphys2309)。

ここでの preparation independence は、別々に準備された system の ontic-state distribution に関する条件であり、Bell の setting/source measurement independence や tomography の iid sampling assumption と同一条件ではない。

ここから「wave function の唯一の ontology が証明された」は出ない。

- theorem は特定の ontological-model vocabulary と preparation independence を使う。
- information-centered interpretation 全般が、その $\psi$-epistemic class と同じではない。
- $\psi$-ontic であることは、Everett、Bohm、collapse、その他の間を一意に選ばない。

Bell、Kochen–Specker、PBR は、ontology に無関係なのではない。むしろ広い候補クラスを非自明に削る。しかし、それぞれが異なる target class と補助仮定をもつため、三つを一つの「量子 ontology theorem」へ結合しない。

### 9.4 Formal success neither certifies nor equalizes interpretations

本ケースで確認できるのは、

$$
\text{quantum formalism succeeds}
\not\Rightarrow
\text{therefore ontology }X
$$

である。ただし同時に、

$$
\text{formalism does not self-certify ontology}
\not\Rightarrow
\text{all interpretations are equally good}.
$$

理論統合、内部整合性、相対論・場の理論との接続、説明範囲、単純性、causal structure、measurement analysis、新予測、modified dynamics への実験制約は追加評価基準になりうる。どの基準をどの重みで使うかも、成功スコア一つからは決まらない。

---

## 10. Network audit table

以下は Q1–Q4 を横断した監査表である。`Not fully self-certified` は `unsupported` を意味しない。第三列にある独立支持が重要である。

| Network node | Quantum realization | How it is secured | Failure mode | Audit status |
|---|---|---|---|---|
| **Target specification** | state $\rho$、channel $\mathcal E$、behavior $P(a,b\mid x,y)$、または ontology | protocol と model class を事前指定 | state tomography と interpretation selection を同一 target にする | model-relative / explicitly specifiable |
| **Candidate-class adequacy** | finite $d$、density-operator model、local hidden-variable class、fixed channel family | leakage tests、alternative models、hold-out prediction、cross-platform replication | $d$ 外 leakage、drift、unknown dynamics、unconceived model | only indirectly constrained / open-ended |
| **Experiment availability** | realizable POVM、control pulse、Bell settings、detectors | calibration、control characterization、hardware qualification | nominal POVM と実現 POVM の不一致 | independently supported / design-certified |
| **Dynamic CIF** | undeclared cross-talk や setting leakage が declared channel を迂回しない | shielding、spacelike separation、timing and cross-talk tests | trial 中の unintended causal path | design-certified / model-relative |
| **Preparation / initial independence** | tomography の run correlations、Bell の $\mu(\lambda\mid x,y)=\mu(\lambda)$ | randomization、source monitoring、cosmic settings、memory tests | common cause、batch correlation、setting-dependent source | design-certified / statistically constrained / not fully self-certified |
| **Safe / admissible experiment** | loss・heating・leakageを許容範囲に保つ measurement/control | power budget、nondemolition design、error monitoring | informative measurement が device regime を壊す | independently testable / experiment-specific |
| **Fresh preparation / reset** | source procedure を繰り返し nominal state を作る | control sequence、interleaved verification、reset fidelity | drift、incomplete reset、history dependence | design-certified / statistically constrained |
| **Copy / product availability** | source-supplied samples（しばしば $\rho^{\otimes N}$ とモデル化）、collective measurement | repeated source use、sample bookkeeping | unknown-input cloning と混同、correlated samples | model-relative / design-certified; no-cloning is analytic and quantum-specific |
| **Measurement richness** | effects が Hermitian space または restricted tangent space を張る | IC proof、frame analysis、randomized design | blind operator direction、rank assumption failure | analytically guaranteed within model / calibration-dependent |
| **Experimental amalgamation** | 複数 settings・times・samples の data を common target へ統合 | preparation equivalence、stable logs、joint likelihood | setting-dependent preparation、incompatible domains | model-relative / statistically constrained |
| **Stable recording** | outcome、setting、time tag、trial window、calibration ledger | synchronized clocks、append-only logs、metrology | lost events、time-window bias、postselection | directly testable / design-certified |
| **Statistical identifiability** | IC tomography、channel identifiability、Bell polytope separation | linear algebra、likelihood geometry、inequality theorem | equal observational law、gauge freedom | analytically guaranteed within specified class |
| **Inverse stability** | measurement frame・Fisher information・channel inversion の conditioning | singular-value analysis、optimal design、regularization | near-null directions、boundary bias、ill conditioning | model-relative / numerically and statistically testable |
| **Predictive validation** | held-out POVM outcomes、gate sequences、Bell correlations、cross-lab reproduction | preregistered prediction、confidence bounds、replication | overfit、distribution shift、drift | directly tested / statistically constrained |
| **Ontological bridge** | $\rho$ または $\psi$ を ontic state、relative-state structure、guiding object / law-like structure、agent probability 等として読む | no-go theorems、unification、explanatory comparison、new predictions | formal object と unique ontology の同一視 | interpretation-dependent / only indirectly constrained / open |

### 10.1 Auditability ledger

同じ条件は一つの status に固定されない。例えば POVM availability は装置校正により `independently supported` だが、POVM matrix が完全に正しいことは target frequencies だけから出ない。measurement richness は nominal model 内で `analytically guaranteed` でも、実現 measurement の calibration に依存する。

この二重性は欠陥ではない。**モデル内の数学的保証と、モデルを実験へ接続する保証を別勘定にする**ことが監査の目的である。

---

## 11. What quantum theory secures strongly

本ケースは弱点表ではない。量子論では、ネットワークの多くの部分が数学・工学・統計の別経路で強く支えられている。

1. **Born-law statistical structure.** state と POVM を固定したときの probability law は明確で、幅広い予測・制御・tomography の共通基盤になっている。
2. **Informational completeness.** finite-dimensional state model には IC measurement の明示構成と単射性証明がある [Scott 2006](https://doi.org/10.1088/0305-4470/39/43/009)。
3. **Finite-sample error analysis.** confidence region、likelihood、minimax/sample-complexity 解析により、理想確率と有限 data の差を定量化する [Christandl & Renner 2012](https://doi.org/10.1103/PhysRevLett.109.120403)。
4. **Alternative experimental design.** compressed sensing、continuous measurement、ancilla assistance、randomized measurements は、resource と target class の trade-off を定理と実験で扱う。
5. **Calibration and joint characterization.** process tomography と gate-set tomography は SPAM、gauge、control errors を明示的な推定対象に変える。
6. **Precise impossibility results.** no-cloning、no-broadcasting、state discrimination、Bell、Kochen–Specker、PBR は、それぞれの仮定と model class の下で明確な境界を与える。
7. **Loophole control.** Bell experiments は detection efficiency、spacetime separation、setting generation、finite statistics を工学的・統計的に改善してきた。
8. **Independent replication and error modeling.** platform、measurement、source、analysis の異なる構成で予測が比較され、target success は一装置の自己報告だけに依存しない。

従って、「量子論は前提ネットワークを無視して成功した」という読みは成立しにくい。より適切なのは、**多くの前提を理論・装置設計・校正・統計・独立再現で別々に監査してきたため、高い予測・制御成功を得ている**という読みである。

---

## 12. What target success does not self-certify

### 12.1 Directly tested

同じ target experiment で比較的直接検査されるものには、次がある。

- outcome frequencies と Born/model probabilities の適合。
- held-out settings または gate sequences への予測。
- Bell functional の値と、指定 local bound からの統計的乖離。
- time-tagged data 内の一部の drift、cross-talk、marginal inconsistency。

直接検査でも、finite sample と選択された loss/test に相対的である。

### 12.2 Independently supported

target success とは別の calibration、control experiment、設計資料から支持されるものには、次がある。

- detector efficiency、dark count、timing resolution。
- realized POVM、control pulse、readout confusion matrix。
- source spectrum、leakage level、reset fidelity。
- Bell stations の距離、clock synchronization、setting latency。
- repeated preparation の stationarity と batch effect。

これらは target success に論理的に含まれなくても、独立の強い根拠をもつことができる。

### 12.3 Model-relative

採用した quantum model 内で証明・計算されるものには、次がある。

- POVM span からの informational completeness。
- measurement map の conditioning。
- no-cloning / no-broadcasting bound。
- Bell-local class の inequality。
- compressed sensing の recovery condition。
- PBR theorem の exclusion class。

これらは「主観的仮定」にすぎないわけではない。形式化された前提から厳密に従うが、前提が対象実験を適切に表すかは別の接続問題である。

### 12.4 Design-certified

装置構造から積極的に作られる条件には、次がある。

- fresh preparation と randomized setting allocation。
- shielding と spacelike separation。
- append-only time-tag logging。
- heralding と event-ready trial definition。
- ancilla access、collective measurement、measurement randomization。

design certification は万能ではないが、成功結果と独立した evidence channel である。

### 12.5 Not fully self-certified by target success

次は target success だけからは完全に出ない。

- 選んだ Hilbert dimension と candidate class が全 relevant dynamics を含むこと。
- nominally identical preparations が全 run で同じ operational state を実現したこと。
- Bell settings と全 relevant latent variables の完全な初期独立性。
- calibration model に未記録の gauge、leakage、feedback がないこと。
- fit された $\rho$ または $\psi$ が一つの ontology をもつこと。
- 競合解釈・修正理論が全て同じ evidence を受けること。

ここで `not fully self-certified` は `unsupported` ではない。例えば spacetime separation は Bell violation という数値だけからは出ないが、距離測定、clock calibration、switching-time measurement により強く支持される。tomography の POVM も target frequencies だけからは出ないが、detector tomography と校正で支持されうる。

---

## 13. Does the prerequisite network add diagnostic value here?

### 13.1 Was the existing organization of quantum theory already sufficient?

**Answer: PARTLY.**

quantum estimation、quantum information、Bell nonlocality、quantum foundations の各分野には、本ケースで使った実質的区別が既にある。IC と finite-sample estimation、no-cloning と repeated preparation、Bell inequality と measurement independence、formalism と interpretation は新しくない。量子論固有の新定理または新しい実験判断は、このケーススタディから得られなかった。

一方、これらは通常、別の文献群と目的の下で整理される。単一の ledger に置くと、次の cross-case dependency が明示される。

- tomography の成功が fresh-preparation interface に依存する一方、それは same-token joint access ではない。
- nominal IC は measurement calibration と dimension adequacy を必要とし、finite-$N$ estimation と stability はさらに別である。
- Bell の dynamic shielding と initial measurement independence は異なる監査を受ける。
- formal model discrimination が強くても、candidate-class adequacy と ontology bridge は別に残る。

### 13.2 Did the network reveal new distinctions?

**New to quantum theory: NO. New as a cross-domain audit arrangement: PARTLY.**

| Distinction | Status in existing quantum work | Added role of the network |
|---|---|---|
| tomography identifiability vs ontology | foundations と estimation では既知 | Q1 と Q4 の間の bridge failure として同じ ledger に置く |
| fresh preparation vs single-history access | tomography/state-discrimination では既知 | product access を physical joint realizability の代替として分類する |
| CIF vs preparation independence | Bell causal analysis では区別可能 | v0.2 の二ノードを Bell apparatus audit へ明示対応させる |
| informational refinement vs physical realization | quantum measurement では既知 | 推定後の counterfactual probability と実測 outcome の差として追跡する |
| within-model ID vs candidate-class adequacy | misspecification、drift、dimension audit では既知 | tomography、Bell、interpretation に共通する upstream risk として統合する |
| full-state reconstruction vs property prediction | shadows/compressed sensing で既知 | target specification を resource substitution の前に固定させる |

### 13.3 Is the network merely a reclassification?

**Largely yes at the level of quantum content.**

このケースが行った数学と物理は既存研究に由来する。監査ネットワークの独自部分があるとすれば、発見内容ではなく、条件を

```text
target / model theorem / design support / statistical support /
class adequacy / ontological bridge
```

へ再配列し、`not self-certified` と `unsupported` を別列にしたことである。この再分類が研究上の方法論的貢献になるかは、一ケースでは示せない。

### 13.4 Pre-registered verdict

| Criterion | Verdict | Reason |
|---|---|---|
| **Weak usefulness test** | **PASS, narrowly** | Q1–Q4 を横断し、product/preparation route、CIF/initial independence、model-ID/class adequacy を同一 ledger で分離した |
| **Methodological-value test** | **NOT YET PASSED** | 既存量子文献にない診断、実験変更、推論変更をまだ生んでいない |
| **Stronger methodological contribution** | **NOT ESTABLISHED** | 一ケースだけで、再利用性・見落とし発見・実験設計変更を示していない |

従って本ケースの結果は **mixed** である。ネットワークは説明上の弱い usefulness を示したが、量子情報・量子基礎論の既存整理を超える方法論的価値は未実証である。

---

## 14. Implications for revision of v0.2

以下は量子ケースから実際に生じた改訂候補であり、直ちに v0.2 へ適用する決定ではない。

### 14.1 Separate preparation equivalence from independence

量子 tomography は、各 run の marginal が同じ $\rho$ であることと、joint state が $\rho^{\otimes N}$ に因子化することを分ける必要がある。v0.2 の `Preparation / initial independence` node は、少なくとも

- preparation equivalence / stationarity
- run-to-run independence / initial correlation

へ内部分解した方がよい可能性がある。

### 14.2 Add calibration / reference-frame / gauge as a cross-cutting edge

known POVM を用いる state tomography と joint SPAM estimation の差は、`experiment availability` だけでは目立ちにくい。measurement realization、calibration、reference frame、gauge quotient を、target specification と experiment availability を結ぶ cross-cutting edge として明示する候補がある。

### 14.3 Refine copy/product access

`copy / product availability` は少なくとも次へ分けるべきである。

- source-driven fresh preparation
- cloning of an unknown supplied token
- supplied multi-copy resource
- collective access to multiple systems

量子論ではこの区別が no-cloning の過剰一般化を防ぐ。

### 14.4 Make query-relative identification explicit

compressed sensing と classical shadows は、full state の識別、restricted state class の識別、選択された properties の予測を区別させる。v0.2 の target specification に、`full generator / parameter / equivalence class / query set` の granularity を明示する価値がある。

### 14.5 Preserve the strength of independently supported auxiliaries

Bell case は、「補助条件が target success から自己証明されない」という表現だけでは、実際の設計・校正・loophole closure の強さを過小表示しうることを示した。v0.2 の auditability に

- directly tested
- independently supported
- analytically guaranteed
- statistically constrained

を正式に追加し、`only indirectly constrained` との間を細分する候補がある。

### 14.6 No strengthening of the central theorem claim

量子ケースは、観測成功から ontology への普遍的不可能定理を支持しない。IC tomography は class-relative identifiability の成功例であり、Bell は強い model-class exclusion の成功例である。ケース結果が支持するのは、ネットワークを固定線形鎖とせず、異なる support channel を記録する必要性だけである。

---

## 15. Open questions

1. **[OPEN] Non-iid tomography.** exchangeable、correlated、adversarial、drifting sources のどの範囲まで、同じ audit ledger で finite-sample guarantees を比較できるか。
2. **[OPEN] Dimension adequacy.** leakage test、dimension witness、spectroscopy、device-independent dimension bound を candidate-class adequacy のどの status に置くべきか。
3. **[OPEN] Calibration circularity.** detector tomography が別の calibrated source を必要とし、source tomography が detector を必要とするとき、gate-set tomography の gauge quotient は regress をどこまで解消し、どこへ移すか。
4. **[OPEN] Single-system observability.** known dynamics と continuous records の下で、initial-state observability、current conditional-state tracking、full-state tomography をどう分類するか。
5. **[OPEN] Bell causal models.** dynamic leakage、initial correlation、retrocausal structure、fine-tuning を、CIF と preparation-independence の二分だけで十分に表せるか。
6. **[OPEN] Interpretation comparison.** empirical equivalence domain、modified dynamics、relativistic/QFT extension、新規予測を同じ model-class audit に入れると、単なる哲学一覧を超えられるか。
7. **[OPEN] Practical diagnostic impact.** この ledger を既存の tomography または Bell experiment の preregistration に適用して、実際に missing check を発見できるか。
8. **[OPEN] Cross-case reuse.** cosmological inverse problems、phylogenetics、nonequilibrium experiment で同じ区別が再利用できるか。

---

## 16. Final self-audit

| Check | Result | Note |
|---|---|---|
| 1. 量子論を批判対象として扱っていないか | pass | 評価対象をネットワークに固定した |
| 2. 量子論の成功を十分に記述したか | pass | §11 に IC、tomography、error analysis、Bell engineering 等を記録した |
| 3. state identifiability と state ontology を分けたか | pass | §5.3、§9 |
| 4. finite-sample estimation と ideal identifiability を分けたか | pass | §5.2–5.5 |
| 5. fresh preparation と single-copy access を分けたか | pass | §6.1–6.3 |
| 6. no-cloning を量子特殊条件として限定したか | pass | §6.4–6.5 |
| 7. CIF と preparation independence を分けたか | pass | §8.4 |
| 8. Bell violation と unique ontology を分けたか | pass | §8.5 |
| 9. candidate-class adequacy を監査したか | pass | §5.6、§10 |
| 10. self-certified でないことと unsupported を混同していないか | pass | §10、§12 |
| 11. ネットワークに不利な結果を許したか | pass | methodological-value test を未通過と判定した |
| 12. 既存量子論との差分を正直に評価したか | pass | quantum content は largely reclassification とした |
| 13. v0.2 改訂案がケース結果から導かれたか | pass | preparation、calibration、product、query granularity に限定した |
| 14. VED を持ち込んでいないか | pass | 本文の理論比較に使用していない |

> **このケーススタディは、v0.2の監査ネットワークを検証対象として扱い、量子論をその証明材料として扱わない。**

本ケーススタディは VED とは独立であり、量子論への監査結果は VED への証拠的支持を与えない。

---

## 17. References

以下は本ケースの具体的主張を監査するために確認した一次文献および標準的レビューである。解釈史全体の完全な bibliography ではない。

1. Barnum, H., Caves, C. M., Fuchs, C. A., Jozsa, R., & Schumacher, B. (1996). “Noncommuting Mixed States Cannot Be Broadcast.” *Physical Review Letters*, 76, 2818–2821. [doi:10.1103/PhysRevLett.76.2818](https://doi.org/10.1103/PhysRevLett.76.2818)
2. Bell, J. S. (1964). “On the Einstein Podolsky Rosen Paradox.” *Physics Physique Fizika*, 1, 195–200. [doi:10.1103/PhysicsPhysiqueFizika.1.195](https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195)
3. Bohm, D. (1952a). “A Suggested Interpretation of the Quantum Theory in Terms of ‘Hidden’ Variables. I.” *Physical Review*, 85, 166–179. [doi:10.1103/PhysRev.85.166](https://doi.org/10.1103/PhysRev.85.166)
4. Bohm, D. (1952b). “A Suggested Interpretation of the Quantum Theory in Terms of ‘Hidden’ Variables. II.” *Physical Review*, 85, 180–193. [doi:10.1103/PhysRev.85.180](https://doi.org/10.1103/PhysRev.85.180)
5. Bohr, N. (1928). “The Quantum Postulate and the Recent Development of Atomic Theory.” *Nature*, 121, 580–590. [doi:10.1038/121580a0](https://doi.org/10.1038/121580a0)
6. Brunner, N., Cavalcanti, D., Pironio, S., Scarani, V., & Wehner, S. (2014). “Bell Nonlocality.” *Reviews of Modern Physics*, 86, 419–478. [doi:10.1103/RevModPhys.86.419](https://doi.org/10.1103/RevModPhys.86.419)
7. Chuang, I. L., & Nielsen, M. A. (1997). “Prescription for Experimental Determination of the Dynamics of a Quantum Black Box.” *Journal of Modern Optics*, 44, 2455–2467. [doi:10.1080/09500349708231894](https://doi.org/10.1080/09500349708231894)
8. Christandl, M., & Renner, R. (2012). “Reliable Quantum State Tomography.” *Physical Review Letters*, 109, 120403. [doi:10.1103/PhysRevLett.109.120403](https://doi.org/10.1103/PhysRevLett.109.120403)
9. D’Ariano, G. M., & Lo Presti, P. (2001). “Quantum Tomography for Measuring Experimentally the Matrix Elements of an Arbitrary Quantum Operation.” *Physical Review Letters*, 86, 4195–4198. [doi:10.1103/PhysRevLett.86.4195](https://doi.org/10.1103/PhysRevLett.86.4195)
10. D’Ariano, G. M., Paris, M. G. A., & Sacchi, M. F. (2003). “Quantum Tomography.” *Advances in Imaging and Electron Physics*, 128, 205–308. [doi:10.1016/S1076-5670(03)80065-4](https://doi.org/10.1016/S1076-5670(03)80065-4)
11. Dürr, D., Goldstein, S., & Zanghì, N. (1992). “Quantum Equilibrium and the Origin of Absolute Uncertainty.” *Journal of Statistical Physics*, 67, 843–907. [doi:10.1007/BF01049004](https://doi.org/10.1007/BF01049004)
12. Everett, H. III. (1957). “‘Relative State’ Formulation of Quantum Mechanics.” *Reviews of Modern Physics*, 29, 454–462. [doi:10.1103/RevModPhys.29.454](https://doi.org/10.1103/RevModPhys.29.454)
13. Fuchs, C. A., Mermin, N. D., & Schack, R. (2014). “An Introduction to QBism with an Application to the Locality of Quantum Mechanics.” *American Journal of Physics*, 82, 749–754. [doi:10.1119/1.4874855](https://doi.org/10.1119/1.4874855)
14. Ghirardi, G. C., Rimini, A., & Weber, T. (1986). “Unified Dynamics for Microscopic and Macroscopic Systems.” *Physical Review D*, 34, 470–491. [doi:10.1103/PhysRevD.34.470](https://doi.org/10.1103/PhysRevD.34.470)
15. Giustina, M., et al. (2015). “Significant-Loophole-Free Test of Bell’s Theorem with Entangled Photons.” *Physical Review Letters*, 115, 250401. [doi:10.1103/PhysRevLett.115.250401](https://doi.org/10.1103/PhysRevLett.115.250401)
16. Gross, D., Liu, Y.-K., Flammia, S. T., Becker, S., & Eisert, J. (2010). “Quantum State Tomography via Compressed Sensing.” *Physical Review Letters*, 105, 150401. [doi:10.1103/PhysRevLett.105.150401](https://doi.org/10.1103/PhysRevLett.105.150401)
17. Hall, M. J. W. (2010). “Local Deterministic Model of Singlet State Correlations Based on Relaxing Measurement Independence.” *Physical Review Letters*, 105, 250404; erratum 116, 219902 (2016). [doi:10.1103/PhysRevLett.105.250404](https://doi.org/10.1103/PhysRevLett.105.250404)
18. Handsteiner, J., et al. (2017). “Cosmic Bell Test: Measurement Settings from Milky Way Stars.” *Physical Review Letters*, 118, 060401. [doi:10.1103/PhysRevLett.118.060401](https://doi.org/10.1103/PhysRevLett.118.060401)
19. Hensen, B., et al. (2015). “Loophole-Free Bell Inequality Violation Using Electron Spins Separated by 1.3 Kilometres.” *Nature*, 526, 682–686. [doi:10.1038/nature15759](https://doi.org/10.1038/nature15759)
20. Huang, H.-Y., Kueng, R., & Preskill, J. (2020). “Predicting Many Properties of a Quantum System from Very Few Measurements.” *Nature Physics*, 16, 1050–1057. [doi:10.1038/s41567-020-0932-7](https://doi.org/10.1038/s41567-020-0932-7)
21. Kochen, S., & Specker, E. P. (1967). “The Problem of Hidden Variables in Quantum Mechanics.” *Journal of Mathematics and Mechanics*, 17, 59–87. [doi:10.1512/iumj.1968.17.17004](https://doi.org/10.1512/iumj.1968.17.17004)
22. Massar, S., & Popescu, S. (1995). “Optimal Extraction of Information from Finite Quantum Ensembles.” *Physical Review Letters*, 74, 1259–1263. [doi:10.1103/PhysRevLett.74.1259](https://doi.org/10.1103/PhysRevLett.74.1259)
23. Merkel, S. T., et al. (2013). “Self-Consistent Quantum Process Tomography.” *Physical Review A*, 87, 062119. [doi:10.1103/PhysRevA.87.062119](https://doi.org/10.1103/PhysRevA.87.062119)
24. Mohseni, M., Steinberg, A. M., & Bergou, J. A. (2004). “Optical Realization of Optimal Unambiguous Discrimination for Pure and Mixed Quantum States.” *Physical Review Letters*, 93, 200403. [doi:10.1103/PhysRevLett.93.200403](https://doi.org/10.1103/PhysRevLett.93.200403)
25. Pusey, M. F., Barrett, J., & Rudolph, T. (2012). “On the Reality of the Quantum State.” *Nature Physics*, 8, 475–478. [doi:10.1038/nphys2309](https://doi.org/10.1038/nphys2309)
26. Scott, A. J. (2006). “Tight Informationally Complete Quantum Measurements.” *Journal of Physics A*, 39, 13507–13530. [doi:10.1088/0305-4470/39/43/009](https://doi.org/10.1088/0305-4470/39/43/009)
27. Shalm, L. K., et al. (2015). “Strong Loophole-Free Test of Local Realism.” *Physical Review Letters*, 115, 250402. [doi:10.1103/PhysRevLett.115.250402](https://doi.org/10.1103/PhysRevLett.115.250402)
28. Silberfarb, A., Jessen, P. S., & Deutsch, I. H. (2005). “Quantum State Reconstruction via Continuous Measurement.” *Physical Review Letters*, 95, 030402. [doi:10.1103/PhysRevLett.95.030402](https://doi.org/10.1103/PhysRevLett.95.030402)
29. van Enk, S. J., & Blume-Kohout, R. (2013). “When Quantum Tomography Goes Wrong: Drift of Quantum Sources and Other Errors.” *New Journal of Physics*, 15, 025024. [doi:10.1088/1367-2630/15/2/025024](https://doi.org/10.1088/1367-2630/15/2/025024)
30. Wootters, W. K., & Zurek, W. H. (1982). “A Single Quantum Cannot Be Cloned.” *Nature*, 299, 802–803. [doi:10.1038/299802a0](https://doi.org/10.1038/299802a0)
31. Blackwell, D. (1953). “Equivalent Comparisons of Experiments.” *The Annals of Mathematical Statistics*, 24, 265–272. [doi:10.1214/aoms/1177729032](https://doi.org/10.1214/aoms/1177729032)

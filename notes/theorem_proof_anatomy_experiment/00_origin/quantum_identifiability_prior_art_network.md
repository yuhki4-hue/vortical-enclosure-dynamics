# 量子論における識別と存在論的推論の既存「照明網」

## Prior-Art Reconstruction for Scientific Identifiability and Ontological Inference

- **Status:** working research note / literature reconstruction / corrigible
- **Version:** 0.1
- **Date:** 2026-08-16
- **Primary object of study:** the structure already present in quantum information, quantum measurement, Bell foundations, statistical inference, and philosophy of science
- **Comparison objects only:** [v0.2 working note](./tool_truth_absence_working_note_v0.2.md), [Quantum Case Study 01](./scientific_identifiability_case_01_quantum.md), and the attached adversarial review
- **Novelty claim:** none

---

## 1. Purpose

本ノートの問いは、量子論における

> 観測成功から、状態・装置・モデルの識別、実験的保証、理論比較、存在論的解釈へ進む過程は、既存研究によってどこまで既に分解・接続されているか

である。

出発点は Scientific Identifiability Prerequisite Network ではない。まず、量子状態トモグラフィー、校正、状態識別、Bell 非局所性、文脈性、量子解釈、科学方法論が、それぞれの目的と用語で作ってきた局所的な推論構造を可能な限り強く再構成する。その後にのみ、それらを重ね、既存研究間の接続状態を調べ、最後に v0.2 の監査ネットワークと比較する。

「照明網」は定理名ではなく、既存の保証関係、条件、失敗様式、分野間 handoff を図示するための比喩である。既存研究が扱っていない領域を先に暗部と呼ぶものでもない。

---

## 2. Method

### 2.1 Reconstruction order

調査順序を次のように固定した。

1. 分野ごとに問題、形式対象、明示条件、失敗様式、回避策、残余曖昧性を再構成する。
2. 各分野が合理的に背景化している実験条件と、下流へ渡す結論を記録する。
3. 文献内の edge を分類する。
4. 同じ失敗様式が複数の保証関係を壊す場合、その多重作用を保存する。
5. 分野別グラフを重ね、接続済み、部分接続、handoff、隣接のみ、未確認を分ける。
6. 最後にだけ v0.2 の語彙と比較する。

### 2.2 Source policy

具体的な物理・数学上の主張には、原論文、権威的レビュー、標準的 monograph を優先した。哲学側では原著と Stanford Encyclopedia of Philosophy の概説を併用した。網羅的 systematic review ではないため、「直接接続を確認できなかった」と「接続が存在しない」を同一視しない。

内部ノートと敵対的査読は、検索論点と比較対象を与える資料としてのみ使用した。査読コメントは独立に検証し、採用、限定採用、棄却、文献監査保留に分けた。査読と一次文献が衝突した場合は一次文献を優先する。結果は §18 の検証台帳に残す。

### 2.3 Edge taxonomy

各矢印は、可能な限り次のいずれかとして読む。

| Edge type | Meaning |
|---|---|
| theorem implication | 明示したモデルと仮定の下で証明される含意 |
| modeling assumption | 推論対象を定義するために置かれる仮定 |
| experimental design support | 装置配置、操作、冗長性、校正が条件を支える |
| statistical dependence | 標本モデル、誤差率、収束、信頼領域に依存する |
| calibration dependence | 既知の準備、測定、参照系、標準への依存 |
| causal assumption | 許される因果経路、共通原因、設定との相関に関する仮定 |
| interpretive inference | 形式的・経験的結論に追加の解釈原理を加える推論 |
| historical / methodological association | 直接の含意ではないが、方法論上結び付けられる |
| merely adjacent | 同じ文献群に現れるだけで、保証関係は確認できない |

### 2.4 Illumination status

| Status | Operational meaning in this note |
|---|---|
| **Fully illuminated** | 問題、条件、失敗、回避策が当該分野で明示的に扱われる |
| **Locally illuminated** | ある分野では前景化されるが、別分野では通常背景化される |
| **Cross-domain handoff** | 一方の結論が別分野の出発点として明示または暗黙に渡される |
| **Weakly connected** | 両側の研究はあるが、直接の保証関係または相互参照が弱い |
| **Apparently unconnected** | 今回の範囲では直接接続を確認できない |
| **Unknown due to incomplete audit** | 文献監査不足の可能性が残る |

最後の二つを本ノートでは blind spot と呼ばない。

### 2.5 Falsification criterion for added value

比較対象の監査ネットワークについて、次の反証基準を置く。

> ネットワーク固有の語彙と図を消しても、科学的内容、必要な区別、実験上の指示がすべて既存文献から同じように再現できるなら、量子ケースで確認された価値は提示形式または索引機能に留まる。

異分野の項目を一枚に描けることだけでは、方法論的貢献と判定しない。既存のレビューや教科書との head-to-head comparison なしに usefulness を確定しない。

---

## 3. Non-goals

本ノートは次を行わない。

- 量子論の不完全性を証明しない。
- 特定の量子解釈を選択または排除しない。
- Bell、Kochen–Specker、PBR を一つの「存在論定理」にまとめない。
- no-cloning、測定非可換性、文脈性、破壊的測定、一個体制約を一つの限界にまとめない。
- 既存研究が背景化する条件を、直ちに欠陥または循環と呼ばない。
- 分野横断の再配置を新規性と同一視しない。
- 「観測成功が存在論を自己証明しない」という見方を、真理の不存在または科学の失敗へ拡張しない。

---

## 4. Subnetwork A — Quantum state tomography and quantum estimation

### 4.1 Problem

量子状態トモグラフィーは、指定された状態モデルと測定モデルの下で、実験結果から状態パラメータ、状態の一部、または選択された observables を推定する。full-state reconstruction、低ランク状態の回復、多数の性質の予測は同じ target ではない。

有限次元の標準設定では

$$
\rho\in\mathcal S(\mathbb C^d),\qquad
p(y\mid s,\rho)=\operatorname{Tr}(\rho E_y^{(s)})
$$

と置く。ここで $\rho$ は density operator、$\{E_y^{(s)}\}_y$ は setting $s$ の POVM である。

### 4.2 Formal objects and core implications

測定写像を

$$
\mathcal M:\rho\longmapsto
\left(\operatorname{Tr}(\rho E_y^{(s)})\right)_{s,y}
$$

とする。full density operator に関して informational completeness が成立するのは、POVM effects の実線形 span が Hermitian operator 空間を張る場合であり、その場合に限る。これは Scott の frame-theoretic treatment と標準的 tomography review に含まれる既知のモデル内結果である。[Scott 2006](https://doi.org/10.1088/0305-4470/39/43/009); [D’Ariano, Paris & Sacchi 2003](https://doi.org/10.1016/S1076-5670(03)80065-4)

非 span の場合、測定 kernel に非零 Hermitian 方向 $H$ があり、POVM が identity を含むため $H$ は traceless に取れる。full-rank の $\rho_0$ に対して十分小さい $\epsilon$ なら $\rho_0\pm\epsilon H$ は異なる状態だが同じ確率を与える。したがって IC は単なる十分条件ではなく、この固定モデルでは必要条件でもある。

一方、有限標本からの estimability、confidence region、minimax risk、sample complexity はこの injectivity と別問題である。[Christandl & Renner 2012](https://doi.org/10.1103/PhysRevLett.109.120403) は信頼領域を、[Haah et al. 2017](https://doi.org/10.1109/TIT.2017.2719044) は sample-optimal tomography を扱う。測定 frame の condition number や Fisher information は、同定可能であっても inversion が不安定または非効率になりうることを表す。

### 4.3 Literature flow

~~~text
full state target ──[modeling assumption: known d and state space]──┐
property target / low-rank target ──[different estimand]───────────┤
                                                                  ▼
              known measurement model + available settings
                   │                  │
       [IC/frame condition]      [restricted isometry /
          theorem edge]          shadow norm / query guarantee]
                   │                  │
                   └──────┬───────────┘
                          ▼
                recorded outcome counts
                          │
       ┌──────────────────┼──────────────────┐
       ▼                  ▼                  ▼
 ideal identifiability  finite-N estimator  goodness-of-fit /
                         + confidence        model checks
       │                  │                  │
       └──────────────┬───┴──────────────────┘
                      ▼
        state, property, or confidence set
                      │
          residual: calibration, drift,
          misspecification, interpretation
~~~

### 4.4 Required conditions

当該文献が前景化する条件は、少なくとも次のように分かれる。

- **State-space specification:** Hilbert-space dimension、positivity、trace-one、必要なら rank、symmetry、matrix-product structure。
- **Measurement specification:** 実現 POVM が既知、または別途推定されていること。
- **Informational condition:** full target なら IC、restricted target ならその集合または query に対する分離条件。
- **Sampling condition:** 独立同分布を用いる定理では i.i.d.; 別の定理では permutation symmetry、exchangeability、martingale、adversarially valid protocol など、それぞれ明示された条件。
- **Statistical regularity:** likelihood model、coverage criterion、loss function、significance level、estimator。
- **Stationarity or specified time variation:** 一つの固定状態を target にするなら、run 間 drift を無視できるかモデル化する必要がある。

i.i.d. は全 tomography の論理的必要条件ではない。対称化、quantum de Finetti reduction、postselection technique は、対称な多体系を独立な積状態の混合に近い形へ還元する手段を与える。ただし、データ順序の random permutation は無限 exchangeability や物理的独立性そのものを作らない。[Renner 2007](https://doi.org/10.1038/nphys684); [Christandl, König & Renner 2009](https://doi.org/10.1103/PhysRevLett.102.020504)

### 4.5 Failure modes

- POVM が full target を分離しない。
- frame が ill-conditioned で、頻度誤差が復元誤差へ大きく増幅される。
- finite-sample uncertainty を点推定だけで覆い隠す。
- positivity boundary 付近で通常の漸近近似や likelihood geometry が非正則になる。[Scholten & Blume-Kohout 2018](https://doi.org/10.1088/1367-2630/aaa7e2)
- source drift が「各 run は同じ $\rho$」という target を壊す。[van Enk & Blume-Kohout 2013](https://doi.org/10.1088/1367-2630/15/2/025024)
- nominal POVM と実現 POVM のずれが state estimate に吸収される。
- leakage または誤った dimension が指定状態空間外の挙動を作る。
- restricted-state assumption が外れ、compressed recovery の保証条件が失われる。

### 4.6 Remedies and substitutions

- IC POVM、overcomplete frame、adaptive design、optimal design によって情報量や conditioning を改善する。
- low-rank 仮定が妥当なら compressed sensing を使う。[Gross et al. 2010](https://doi.org/10.1103/PhysRevLett.105.150401)
- full reconstruction が不要なら classical shadows など query-relative な目標へ変更する。[Huang, Kueng & Preskill 2020](https://doi.org/10.1038/s41567-020-0932-7)
- confidence region、likelihood-ratio region、bootstrap または finite-sample bounds を点推定に追加する。
- 時間ブロック、interleaved controls、drift model、randomization により stationarity failure を検出またはモデル化する。
- dimension witnesses、leakage diagnostics、spectroscopy を別検査として使う。[Gallego et al. 2010](https://doi.org/10.1103/PhysRevLett.105.230501); [Wood & Gambetta 2018](https://doi.org/10.1103/PhysRevA.97.032306)
- measurement model が未知なら、次節の detector tomography または self-consistent characterization へ問題を移す。

### 4.7 Residual ambiguity

データが固定された $(d,\mathcal S,\mathcal M)$ 内で $\rho$ を一意に定めても、次は残る。

- 実際の装置が指定した dimension と POVM で十分表現されるか。
- 単一の stationary state と time-averaged state のどちらを推定したか。
- operational density operator をどの存在論的対象として読むか。
- full-state estimate が目的なのか、予測する query set に対する十分な記述が目的なのか。

これらは tomography の IC theorem 自体が解く問題ではない。

### 4.8 Backgrounded assumptions / stabilized interfaces

成熟した tomography 実験では、preparation procedure の反復、time stamping、setting control、calibrated detector model、classical record、データ処理 pipeline が日常的に安定化される。この背景化は合理的であり、理論的に無視されていることを意味しない。装置校正または drift が主問題になれば、これらは直ちに前景化する。

### 4.9 Upstream assumptions and downstream handoff

- **Upstream:** quantum kinematics、Born rule、sample target、measurement implementation、preparation protocol。
- **Downstream:** process characterization、control validation、property certification、基礎論で用いる operational statistics。

### 4.10 Edge register

| From | To | Edge type | Illumination |
|---|---|---|---|
| effect span | ideal state identifiability | theorem implication | Fully illuminated |
| repeated records | finite-sample estimate | statistical dependence | Fully illuminated |
| low-rank restriction | reduced measurement count | theorem implication + modeling assumption | Fully illuminated |
| source stationarity | fixed-state estimand | modeling assumption | Locally illuminated |
| detector calibration | validity of state estimate | calibration dependence | Cross-domain handoff to §5 |
| density operator estimate | ontology of state | no theorem edge in tomography | handoff to §§8–9 |

---

## 5. Subnetwork B — Measurement calibration, SPAM, and self-consistent tomography

### 5.1 Problem

標準の state tomography は measurement を既知とし、detector tomography は probe states を既知とし、process tomography は入力 state と measurement を既知とする。この相互依存は新しい calibration regress ではなく、量子計測で明示的に扱われてきた。問題は、何を reference として固定し、何を同時推定し、どの等価性までしか識別できないかである。

### 5.2 Formal objects

- **Detector tomography:** 未知の POVM effects $\{E_y\}$ と既知 probe states $\{\rho_i\}$。
- **Source tomography:** 未知 states と既知 measurements。
- **Process tomography:** 未知 channel $\mathcal E$ と既知 input states / measurements。
- **Gate-set tomography (GST):** preparation $\rho$, measurement effects $E$, gates $\{G_i\}$ を一つの gate set として同時推定。

GST の予測確率は例えば

$$
p(s)=\langle\!\langle E|G_{i_L}\cdots G_{i_1}|\rho\rangle\!\rangle
$$

である。任意の可逆表現変換 $B$ に対し

$$
|\rho\rangle\!\rangle\mapsto B|\rho\rangle\!\rangle,\quad
\langle\!\langle E|\mapsto\langle\!\langle E|B^{-1},\quad
G_i\mapsto BG_iB^{-1}
$$

は全 sequence probability を不変にする。したがって、十分なデータでも gate-set representation は gauge orbit を越えて一意にならない。これは失敗を隠す言葉ではなく、観測確率が決める同値類の明示である。[Nielsen et al. 2021](https://doi.org/10.22331/q-2021-10-05-557)

### 5.3 Literature flow

~~~text
known probe states ───────────▶ detector tomography ───────▶ POVM estimate
known detector  ──────────────▶ source tomography   ───────▶ state estimate
known inputs + detector ──────▶ process tomography  ───────▶ channel estimate

unknown SPAM + unknown gates
          │
          ├──[sequence design + fiducial completeness]
          ▼
 self-consistent gate-set likelihood
          │
          ├──▶ gauge-invariant predictions / quantities
          ├──▶ gauge fixing by convention or target comparison
          └──▶ model-violation diagnostics

external reference frames / traceability ──▶ meaning of coordinates
device-independent self-testing ───────────▶ equivalence up to local isometry
~~~

### 5.4 Required conditions

- probe states、measurements、または gate sequences のうち、推定対象を励起・読み出すための十分な span。
- device が実験中に同じ model class に従うこと。GST では通常 Markovian gate model が基準となり、non-Markovianity は model violation として診断されうる。
- sequence labels と classical record の対応。
- reference frame または gauge convention の意味を明示すること。
- finite-sample likelihood と uncertainty treatment。

「calibration-free GST」は、pre-calibrated SPAM を不要にして gate set を相対的・自己整合的に推定するという文献内の用語であり、absolute reference や gauge ambiguity が消えるという意味ではない。[Nielsen et al. 2021](https://doi.org/10.22331/q-2021-10-05-557)

### 5.5 Failure modes

- SPAM error を gate error または state error に誤帰属する。
- fiducial または germ が informationally / amplificationally incomplete。
- device drift や history dependence が固定 Markovian gate set を壊す。
- leakage、crosstalk、context dependence が想定 Hilbert space や tensor factorization を壊す。
- gauge-variant metric を物理的に一意な量と誤認する。
- reference frame のずれを object dynamics に誤帰属する。
- calibration chain の一部が未追跡で、絶対量の意味が不明確になる。

### 5.6 Remedies and substitutions

- detector / process tomography は既知 reference へ依存を移す。[D’Ariano, Maccone & Lo Presti 2004](https://doi.org/10.1103/PhysRevLett.93.250407); [Chuang & Nielsen 1997](https://doi.org/10.1080/09500349708231894)
- self-consistent process tomography と GST は SPAM と gates を共同モデル化する。[Merkel et al. 2013](https://doi.org/10.1103/PhysRevA.87.062119)
- gauge-invariant predictions、operational parameterization、または明示的な gauge fixing を用いる。[Di Matteo et al. 2020](https://doi.org/10.22331/q-2020-11-17-364)
- randomization、sequence-length variation、held-out circuits、likelihood-ratio tests で model violation を検査する。
- shared reference frame がない場合、その不在を resource theory として扱う。[Bartlett, Rudolph & Spekkens 2007](https://doi.org/10.1103/RevModPhys.79.555)
- Bell correlations を用いる self-testing は、black-box device の状態・測定を assumptions の下で local isometry まで certify する別経路である。通常の metrological calibration を無仮定で置換するわけではない。[Šupić & Bowles 2020](https://doi.org/10.22331/q-2020-09-30-337)

一般計量学で metrological traceability は、各段階が measurement uncertainty に寄与する documented calibration chain により結果を reference へ関係づける性質として定義される。[JCGM 200:2012](https://doi.org/10.59161/JCGM200-2012) GUM は uncertainty の評価・伝播・報告を標準化する。[JCGM 100:2008](https://doi.org/10.59161/JCGM100-2008E) これは quantum-specific identifiability theorem ではないが、calibration dependency を「無根拠」ではなく追跡可能な evidence chain へ変える既存の方法である。

### 5.7 Residual ambiguity

- gauge orbit 内の表現差は実験確率からは選ばれない。
- gauge fixing は報告・比較を可能にするが、選んだ座標を新たな観測事実にはしない。
- self-consistency は model family が適切であることを単独で保証しない。
- self-testing も因果構造、独立性、量子実現可能性など指定 assumptions に相対的である。
- traceability は reference への連鎖を作るが、無限 regress を数学的に消すのではなく、再現可能な標準と不確かさ budget へ依存を移送する。

### 5.8 Backgrounded assumptions / stabilized interfaces

laboratory timing、control labels、shared phase reference、classical electronics、detector linearity、standard source、environmental isolation は、校正計画により安定化される。GST では既知 SPAM が背景から外される一方、gate-set model、sequence execution、classical labels は背景に残る。self-testing では内部 device model を後退させる一方、spacelike organization や入力選択など別の assumption が前景化する。

### 5.9 Upstream assumptions and downstream handoff

- **Upstream:** reference standards、control semantics、device stability、chosen equivalence relation。
- **Downstream:** state/process estimates の意味、gate performance claims、fault-tolerance model、Bell/contextuality experiment の measurement implementation。

### 5.10 Edge register

| From | To | Edge type | Illumination |
|---|---|---|---|
| known probes | POVM estimate | calibration dependence + theorem implication | Fully illuminated |
| joint SPAM/gate data | gate-set equivalence class | statistical dependence + theorem implication | Fully illuminated |
| gauge choice | coordinate report | modeling convention | Fully illuminated |
| sequence redundancy | model-violation detection | experimental design support | Fully illuminated |
| reference-frame resource | operational meaning of coordinates | calibration dependence | Locally illuminated |
| calibrated operations | downstream tomography/Bell claims | Cross-domain handoff | explicit locally, diffuse globally |

---

## 6. Subnetwork C — Quantum state discrimination and resource constraints

### 6.1 Problem

state discrimination は、通常、既知の候補 ensemble から供給された状態の label を推測する decision problem である。未知状態全体を再構成する tomography と target が異なる。

候補 ensemble を $\{(p_i,\rho_i)\}$、measurement を POVM $\{M_j\}$、decision rule を $\delta(j)$ とすれば、minimum-error discrimination は平均誤りを最小化する。unambiguous discrimination は inconclusive outcome を許して誤同定をゼロにする。perfect discrimination、minimum error、unambiguous discrimination、asymptotic error exponent は別問題である。[Helstrom 1976](#ref-helstrom); [Chefles 2000](https://doi.org/10.1080/00107510010002599)

### 6.2 Formal objects and core results

- 一個の system で pure states を perfect に区別できるのは、候補が相互 orthogonal の場合である。
- nonorthogonal states には一般に zero-error perfect discrimination はないが、prior を与えた minimum-error optimum は Helstrom problem として定義できる。
- linearly independent pure states は、失敗 outcome を許せば unambiguous discrimination が可能である。混合状態には support 条件が加わる。
- $N$ copies と collective measurement は one-copy より誤りを減らし、asymptotic discrimination は quantum Chernoff bound で特徴づけられる。[Audenaert et al. 2007](https://doi.org/10.1103/PhysRevLett.98.160501)
- unknown token を複製する no-cloning task と、source が同じ preparation procedure を再実行して $\rho^{\otimes N}$ を供給する multi-copy resource は同じ操作ではない。

### 6.3 Literature flow

~~~text
known ensemble + prior + loss
            │
            ├──── one supplied system ──▶ POVM decision
            │             │
            │             ├─ orthogonal: perfect possible
            │             ├─ nonorthogonal: minimum error
            │             └─ linearly independent: unambiguous + inconclusive
            │
            └──── N supplied copies ───▶ local/adaptive/collective strategy
                                          │
                                          └─ finite-N risk / asymptotic exponent

unknown supplied token ── no universal cloning ──╳── arbitrary product interface
repeatable source ─────── experimental resource ───▶ supplied multi-copy state

joint measurability ──▶ common POVM marginals
nondisturbance / instruments ──▶ sequential implementation and state update
broadcastability ──▶ distribution of state information to subsystems
~~~

### 6.4 Required conditions

- candidate ensemble、prior、loss function が指定される。
- allowed POVM、collective access、ancilla、adaptive control、copy count が指定される。
- repeated preparation を使うなら、source が同じ ensemble element または同じ preparation law をどのように供給するかが指定される。
- sequential measurement を使うなら effect だけでなく instrument、すなわち outcome と state update が指定される。

### 6.5 Relations that must not be collapsed

1. **No-cloning:** 任意未知 pure state を完全に複製する universal physical map はない。[Wootters & Zurek 1982](https://doi.org/10.1038/299802a0)
2. **No-broadcasting:** 任意の非可換 mixed-state family を、その marginals に同じ状態が現れる形で放送できない。[Barnum et al. 1996](https://doi.org/10.1103/PhysRevLett.76.2818)
3. **Measurement incompatibility / joint measurability:** 複数 POVM が一つの parent POVM の marginals かという effect-level property。
4. **Nondisturbance:** ある measurement instrument の実行が別 observable の statistics を保存するかという sequential property。
5. **Destructiveness:** instrument が input state をどのように更新するか。非可換性そのものと同義ではない。
6. **One-copy limitation:** 実験者に供給された物理 resource 数の制約。

これらには定理的な関係があるが、一般に同値ではない。compatibility、nondisturbance、broadcastability 等が階層をなすことは [Heinosaari 2016](https://doi.org/10.1103/PhysRevA.93.042118) が明示する。したがって「一般確率論ではすべて同値になる」という無限定な整理は採用しない。

### 6.6 Failure modes

- unknown ensemble を known と扱う。
- single-copy risk と asymptotic $N\to\infty$ risk を混同する。
- fresh samples を unknown supplied token の cloning と解釈する。
- outcome statistics だけを指定し、sequential disturbance を決める instrument を省く。
- local measurements と collective measurements の resource difference を消す。
- incompatible observables を「一切同時に情報を得られない」と過剰解釈する。

### 6.7 Remedies and substitutions

- zero-error target を minimum-error、unambiguous、confidence-set target に緩める。
- copies、ancilla、adaptive strategy、collective measurement を明示 resource として増やす。
- tomography ではなく、目的関数に十分な observable/query のみ推定する。
- joint measurability がない場合、異なる fresh preparations を setting 間に配分する。
- known dynamics と continuous/weak measurement により、別の observability problem へ移す。

### 6.8 Residual ambiguity

resource が増えれば operational discrimination は改善しうるが、識別された label または density operator の存在論的意味は discrimination theorem からは決まらない。また no-cloning は unrestricted product interface の不在を示すが、量子状態一般の識別不能や、同じ手順による再準備不能を示さない。

### 6.9 Backgrounded assumptions / stabilized interfaces

candidate labels、source prior、trial boundaries、copy count、allowed laboratory operations は decision problem の一部として固定される。通信・暗号プロトコルではこれらを threat model として前景化するが、教科書的 discrimination theorem では既知入力として背景化される。

### 6.10 Upstream assumptions and downstream handoff

- **Upstream:** known ensemble、resource theory、instrument model、source interface。
- **Downstream:** communication rate、cryptographic security、tomographic sample design、operational no-go claims。

### 6.11 Edge register

| From | To | Edge type | Illumination |
|---|---|---|---|
| orthogonality | one-copy perfect discrimination | theorem implication | Fully illuminated |
| copy number / collective access | attainable error | theorem implication + resource assumption | Fully illuminated |
| no-cloning | inability to manufacture universal copies | theorem implication | Fully illuminated |
| repeatable source | multi-copy experiment | experimental resource | Locally illuminated |
| joint measurability | common measurement implementation | theorem implication | Fully illuminated |
| effect statistics | sequential disturbance | no unique edge without instrument | Fully illuminated warning |

---

## 7. Subnetwork D — Bell nonlocality and Bell experimental methodology

### 7.1 Problem

Bell 研究は、観測 behavior

$$
P(a,b\mid x,y)
$$

が、指定された causal / hidden-variable model class に属しうるかを検査する。Bell inequality violation は、無仮定で世界像を直接読む操作ではない。他方で、補助条件が存在するというだけで推論が弱いわけでもない。Bell 分野は、どの仮定の conjunction が排除され、どの実験設計が loophole を閉じ、有限標本でどの rejection が可能かを高度に明示してきた。[Bell 1964](https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195); [Brunner et al. 2014](https://doi.org/10.1103/RevModPhys.86.419)

### 7.2 Formal objects and assumption decomposition

hidden variable を $\lambda$ とする。標準的な Bell-local factorization は

$$
P(a,b\mid x,y,\lambda)
=
P(a\mid x,\lambda)P(b\mid y,\lambda)
$$

である。さらに観測 behavior を得るために

$$
P(a,b\mid x,y)
=
\int d\lambda\,
P(\lambda\mid x,y)
P(a,b\mid x,y,\lambda)
$$

と書く。measurement independence / setting independence は

$$
P(\lambda\mid x,y)=P(\lambda)
$$

である。

Jarrett に由来し、Shimony が中立的名称を普及させた分解では、factorizability は次の conjunction として表せる。[SEP: Bell’s Theorem](https://plato.stanford.edu/entries/bell-theorem/)

**Parameter independence (PI):**

$$
P(a\mid x,y,\lambda)=P(a\mid x,\lambda),\qquad
P(b\mid x,y,\lambda)=P(b\mid y,\lambda).
$$

**Outcome independence (OI):**

$$
P(a,b\mid x,y,\lambda)
=
P(a\mid x,y,\lambda)P(b\mid x,y,\lambda).
$$

通常の正則性の下で PI と OI の conjunction は factorization と同値である。[Jarrett 1984](https://doi.org/10.2307/2214878) ただし、Bell の local causality という物理概念をこの統計的分解だけと無条件に同一視すべきではない。因果完全性、screening-off、時空的な局所性をどう読むかは別の概念分析を伴う。

operational no-signaling

$$
\sum_bP(a,b\mid x,y)
\ \text{is independent of }y
$$

は観測分布の条件である。PI と measurement independence は operational no-signaling を導く一つの十分な組だが、観測された no-signaling から hidden level の PI は一般には戻らない。標準量子表現で「PI を保ち OI を破る」と言う整理はよく用いられるが、$\lambda$ に何を含めるかと解釈に相対的である。

measurement dependence は $P(\lambda\mid x,y)\ne P(\lambda)$ というモデル特性である。それだけで、設定が未来から過去へ作用する retrocausal model、共通過去による相関、設定生成装置まで含めた決定論的 model、通常 superdeterminism と呼ばれる諸立場を同一にしない。[Hall 2010](https://doi.org/10.1103/PhysRevLett.105.250404)

### 7.3 Literature flow

~~~text
observed time tags + settings + outcomes
          │
          ├── trial definition / coincidence rule
          ├── detection and inclusion rule
          ├── finite-sample test valid under allowed memory
          ▼
       behavior P(a,b|x,y)
          │
          ├───────────────┬────────────────┐
          ▼               ▼                ▼
 Bell inequality     no-signaling      causal-model analysis
          │               │                │
          └─────── statistical rejection ─┘
                          │
          excluded: specified conjunction of
          factorization + setting/source/trial assumptions
                          │
        ┌─────────────────┼────────────────────┐
        ▼                 ▼                    ▼
 relax PI/OI        relax setting       alter causal order /
 or common-cause    independence        retrocausal class
 structure
        │                 │                    │
        └──────────── residual model plurality ┘
                          │
          downstream: device independence,
          causal foundations, interpretation
~~~

### 7.4 Required conditions as the field states them

- **Bell-local model class:** factorization / local causality and specification of $\lambda$.
- **Measurement independence / freedom-of-choice condition:** settings and relevant source variables are appropriately independent.
- **Space-time arrangement:** remote setting and outcome events are separated so that subluminal communication cannot explain the correlations under the chosen event boundaries.
- **Outcome registration and sampling:** detection efficiencies and inclusion rules do not create selection that invalidates the tested inequality.
- **Trial definition:** emissions, detections, windows, and coincidences are defined without settings-dependent selection.
- **Finite-sample analysis:** reported $p$-value、confidence level、prediction-based ratio、martingale bound 等が、実際に許す temporal dependence に対して妥当。
- **Source and device assumptions:** protocol により異なる。event-ready heralding、random number generator、timing model、detector behavior が含まれる。

### 7.5 Experimental loopholes and their remedies

| Issue in Bell literature | What it can invalidate | Standard response |
|---|---|---|
| locality / communication loophole | PI/locality interpretation of factorization | spacelike event organization, fast setting choice, shielding |
| detection / fair-sampling loophole | observed subsample as representative of all trials | high-efficiency detection, inequalities robust to no-click outcomes |
| freedom-of-choice / setting-correlation issue | $P(\lambda\mid x,y)=P(\lambda)$ | physical RNGs, separation of choice events, cosmic setting sources |
| memory loophole | an i.i.d.-based significance analysis | martingale/sequential statistics valid under inter-trial memory |
| coincidence-time loophole | settings-dependent pairing of events | event-ready or pulsed trial definitions, time-tag inequalities |
| trial-definition / stopping issue | sample selection and reported significance | preregistered windows/stopping, complete time-tag analysis |
| source imperfection or background | intended event distribution | heralding, auxiliary characterization, explicit error model |

memory loophole は単なる device drift の別名ではない。devices が過去 trials に依存して応答する local model に対しても統計的 rejection が妥当かという問題である。[Barrett et al. 2002](https://doi.org/10.1103/PhysRevA.66.042111)

coincidence-time loophole は、連続 source などでどの detections を同一 pair の trial とするかに関わる。[Larsson & Gill 2004](https://doi.org/10.1209/epl/i2004-10124-7) time-tag または event-ready design は、その依存を除くか明示する。

2015年の複数実験は、主要な detection と locality loopholes を同時に閉じる設計と有限統計を実現した。[Hensen et al. 2015](https://doi.org/10.1038/nature15759); [Giustina et al. 2015](https://doi.org/10.1103/PhysRevLett.115.250401); [Shalm et al. 2015](https://doi.org/10.1103/PhysRevLett.115.250402) これは「全ての補助条件がデータ自身から証明された」という意味ではない。どの loopholes をどの設計で閉じたかを明示することが、実験の強さである。[Kofler et al. 2016](https://doi.org/10.1103/PhysRevA.93.032115)

cosmic Bell tests は setting source と粒子 source の共通原因がありうる時空領域を過去へ押し戻す。measurement independence を論理的に無仮定へ変えるのではない。[Handsteiner et al. 2017](https://doi.org/10.1103/PhysRevLett.118.060401)

### 7.6 Causal-model formulations

causal graph では、Bell-local classical model を共通原因 $\lambda$ から outcomes への arrows と、settings から各 local outcome への arrows で表す。Bell correlations を classical causal model で再現しながら observed no-signaling independences を保つには fine-tuning が必要になる、という結果がある。[Wood & Spekkens 2015](https://doi.org/10.1088/1367-2630/17/3/033002) quantum causal models は common cause の概念自体を量子化する試みを含む。[Allen et al. 2017](https://doi.org/10.1103/PhysRevX.7.031021)

これらは「因果仮定」という一語へ Bell methodology 全体を畳み込むものではない。graph structure、conditional independences、fine-tuning criterion、quantum common cause の形式体系がそれぞれ必要である。

### 7.7 Remedies and substitutions

- detector、setting generator、event-ready heralding、space-time layout を再設計し、特定 loophole を閉じる。
- i.i.d. を要求しない martingale / sequential test へ統計手法を置換する。
- fair-sampling または fair-coincidence assumption が不要な inequality と event definition を選ぶ。
- measurement independence を弱めるなら、その許容相関量または causal class を明示し、別の inequality / bound を導く。
- device characterization を減らすなら、代わりに device-independent protocol の causal and statistical assumptions を明示する。
- 一つの conjunction が棄却された後は、どの assumption relaxation が残るかを model class ごとに比較する。

### 7.8 Failure modes

- factorization、PI、OI、measurement independence、no-signaling を同じ条件として扱う。
- detector selection、coincidence selection、trial definition を一つの generic leakage にまとめる。
- i.i.d. significance test を memory-allowed experiment に使う。
- Bell violation を quantum theory 全体、または一つの解釈の直接証明と読む。
- loophole の存在可能性だけから実験を無効とする。
- “loophole-free” という慣用名から、全ての causal/ontological assumptions が自己証明されたと読む。

### 7.9 Residual ambiguity

Bell violation が強く排除するのは、明示された statistical and causal assumptions の conjunction に属する model class である。どの conjunct を放棄するか、量子 causal structure をどう読むか、Everett、Bohm、collapse、operational approaches のどれを採るかは violation 単独では一意にならない。しかしこの非一意性は、Bell test の排除力が弱いという意味ではない。

### 7.10 Backgrounded assumptions / stabilized interfaces

Bell 分野では setting independence、locality、detection、trial definition は他分野より前景化している。反対に、各 detector の量子トモグラフィー、laboratory metrology の全 traceability chain、raw voltage から event label への electronics は、実験論文の methods と校正文献へ委ねられやすい。operational behavior を得た後の foundations 論文では、これらが所与として背景化することが多い。

### 7.11 Upstream assumptions and downstream handoff

- **Upstream:** calibration、time synchronization、event construction、randomness source、space-time geometry、finite-sample protocol。
- **Downstream:** local hidden-variable class exclusion、device-independent randomness / cryptography、quantum causal models、interpretation。

### 7.12 Edge register

| From | To | Edge type | Illumination |
|---|---|---|---|
| PI + OI | factorizability | theorem implication | Fully illuminated |
| factorization + measurement independence | Bell polytope constraints | theorem implication | Fully illuminated |
| detector/trial design | valid sampled behavior | experimental design + statistical dependence | Fully illuminated |
| spacelike arrangement | closure of communication explanation | experimental design + causal assumption | Fully illuminated |
| Bell violation | exclusion of specified model conjunction | theorem + statistical rejection | Fully illuminated |
| class exclusion | unique ontology | no theorem edge | explicit residual ambiguity |

---

## 8. Subnetwork E — Contextuality and ontological-model no-go results

### 8.1 Problem

この領域は、operational procedures の同値性を underlying ontological representation がどのように表すべきか、あるいは量子予測がどの hidden-variable / ontological-model class と両立しないかを問う。Kochen–Specker、generalized contextuality、Bell、PBR は target と assumptions が異なる。

### 8.2 Formal objects

形式対象は、projector valuation、operational procedure とその equivalence class、ontic state $\lambda$、preparation distribution $\mu(\lambda\mid P)$、measurement response $\xi(k\mid M,\lambda)$、transformation kernel、observed contextuality behavior である。どの object と equivalence relation を選ぶかが theorem scope を決める。

### 8.3 Kochen–Specker contextuality

original Kochen–Specker theorem は、$d\ge 3$ の Hilbert space で、projectors に measurement context と独立な definite value を割り当て、orthogonal resolution ごとの functional constraints を満たす valuation が存在しないことを示す。[Kochen & Specker 1967](https://doi.org/10.1512/iumj.1968.17.17004)

この original form では outcome-deterministic value assignment が中心にある。ただし、これを generalized contextuality の全結果に必要な独立仮定として投影してはならない。

### 8.4 Generalized contextuality

operational theory では preparations $P$、transformations $T$、measurements $M$ と outcome probabilities $p(k\mid P,T,M)$ を扱う。二つの procedures が全 operational contexts で同じ statistics を与えるとき operationally equivalent とする。ontological model は ontic state $\lambda$、preparation distributions $\mu(\lambda\mid P)$、response functions $\xi(k\mid M,\lambda)$、transition kernels を与える。

generalized noncontextuality は、operationally equivalent な procedures が ontological representation でも同じ表現を持つことを要求する。これは preparation、transformation、unsharp measurement に拡張され、deterministic hidden-variable model に限定されない。[Spekkens 2005](https://doi.org/10.1103/PhysRevA.71.052108)

### 8.5 Ontological models and PBR

Harrigan–Spekkens framework は、異なる pure quantum states に対応する ontic distributions の supports が overlap するかにより $\psi$-ontic / $\psi$-epistemic model を分類する。[Harrigan & Spekkens 2010](https://doi.org/10.1007/s10701-009-9347-0) これはすべての「epistemic interpretation」と同義ではない。とくに QBism の normative state assignment を、この ontological-model taxonomy の $\psi$-epistemic model と無条件に同一視しない。

PBR theorem は、独立に準備された systems の joint ontic state に関する preparation independence を含む assumptions の下で、quantum state distributions が overlap するある種の $\psi$-epistemic model を排除する。[Pusey, Barrett & Rudolph 2012](https://doi.org/10.1038/nphys2309)

PBR preparation independence は、Bell における settings と source variable の measurement independence と同じ式・役割ではない。また tomography の i.i.d. sampling assumption とも同一ではない。

### 8.6 Literature flow

~~~text
operational preparations / transformations / measurements
                       │
                       ├── operational equivalences
                       │          │
                       │          ▼
                       │ generalized noncontextuality assumption
                       │          │
                       │          ▼
                       │ noncontextual inequality / impossibility
                       │
sharp projective structure ── valuation constraints ──▶ KS contradiction

quantum pure-state preparations
          │
 ontological distributions μ_ψ(λ)
          │
 preparation independence for products
          ▼
 PBR exclusion of overlapping-support class

each exclusion ──▶ narrower ontological-model space
                 ──╳──▶ unique interpretation
~~~

### 8.7 Required conditions

- operational equivalences が理論的、実験的、または secondary procedures により十分確立されること。
- tested noncontextuality notion が preparation、measurement、transformation のどれか明示されること。
- sharpness、compatibility、no-disturbance、outcome determinism 等、採用 theorem に固有の条件。
- PBR では ontological-model representation と preparation independence。
- finite experiment では inequality、noise robustness、statistical test。

### 8.8 Failure modes

- Bell locality と noncontextuality を同じ constraint とする。
- original KS の deterministic valuation を generalized contextuality 全体へ要求する。
- operational equivalence の近似誤差を無視する。
- compatibility/no-disturbance assumption を device label だけで保証済みとする。
- PBR の preparation independence を無記載にして「$\psi$ は実在」と一般化する。
- 排除された model class を、量子解釈全体と同一視する。

### 8.9 Remedies and substitutions

- noise-robust noncontextuality inequalities と explicit operational equivalence tests。
- secondary preparations/measurements を用いた exact-equivalence construction。
- theorem の assumption を弱める代わりに exclusion scope を狭める。
- causal and operational frameworks で Bell、contextuality、preparation noncontextuality の関係を限定的に比較する。
- empirical indistinguishability が残る場合、排除ではなく compatible model set を報告する。

### 8.10 Residual ambiguity

no-go theorem は広い model landscape を削るが、残る model のうち一つを選ぶ decision rule を自動的に与えない。さらに theorem が扱う ontological model の形式化に入らない interpretive program もありうる。これは theorem を無効にするのではなく、exclusion domain を限定する。

### 8.11 Backgrounded assumptions / stabilized interfaces

foundations analysis では operational probabilities と equivalence classes が入力として背景化されることが多い。実験ではそれらの近似、compatibility、drift、calibration が前景化する。反対に tomography では同じ density operator を operational target とし、その ontological representation は背景化される。

### 8.12 Upstream assumptions and downstream handoff

- **Upstream:** operational data、procedure equivalences、compatibility、preparation composition。
- **Downstream:** ontological-model exclusion、resource theories of contextuality、interpretation comparison。

### 8.13 Edge register

| From | To | Edge type | Illumination |
|---|---|---|---|
| KS constraints | impossibility of noncontextual valuation | theorem implication | Fully illuminated |
| operational equivalence + generalized noncontextuality | inequality constraints | theorem implication + modeling assumption | Fully illuminated |
| preparation independence | PBR exclusion scope | modeling assumption + theorem implication | Fully illuminated |
| experiment calibration | validity of operational equivalences | calibration dependence | Locally illuminated |
| no-go exclusion | unique quantum interpretation | no theorem edge | explicit residual ambiguity |

---

## 9. Subnetwork F — Quantum interpretation and theory comparison

### 9.1 Problem

この領域の target は、laboratory state parameter の推定ではなく、quantum formalism が何を表すか、measurement、probability、macroscopic facts、relativity との関係をどう理解するかである。「Copenhagen interpretation」は統一された一理論ではなく、Bohr、Heisenberg、後世の textbook instrumentalism を含む family として扱う必要がある。[SEP: Copenhagen Interpretation](https://plato.stanford.edu/entries/qm-copenhagen/)

### 9.2 Formal objects

比較対象には、同じ operational formalism に異なる意味論を与える interpretive program、追加 variables を持つ formulation、標準 dynamics を変更する rival theory、relativistic/QFT extension が混在する。形式対象は wave function、density operator、configuration、branch structure、stochastic law、agent-relative probability assignment、relational fact などであり、一つの共通 parameter space に最初から入るとは限らない。

### 9.3 Comparison dimensions

| Program / theory family | Characteristic structure | Empirical relation to standard operational QM | Residual assessment questions |
|---|---|---|---|
| Copenhagen-family approaches | classical/quantum cut、complementarity、context of measurement について複数の立場 | 標準 laboratory predictions を通常採用 | family 内差、measurement description、realism の読み |
| Everett / relative-state | universal unitary state、relative states / branching | 標準 unitary predictions の回復を目指す | probability、preferred basis、branch ontology、QFT/cosmology |
| Bohmian mechanics | wave function + configuration + guidance law + quantum equilibrium | equilibrium domain で標準 QM statistics を再現 | nonlocality、relativistic/QFT extension、equilibrium status |
| objective-collapse theories | stochastic nonlinear modification、collapse parameters | 標準 QM と原理的に異なる predictions を持ちうる | parameter bounds、energy increase、relativistic models |
| QBism | quantum state and Born rule as an agent’s normative probability calculus | operational predictions と整合することを目指す | agent/system boundary、intersubjective objectivity、ontology |
| relational approaches | facts/states relative to systems or interactions | 多くは標準 formalism を再解釈 | consistency across perspectives、precise dynamics、variants |

Everett の原論文は relative-state formulation を、Bohm は追加 variables と guidance dynamics を、GRW は標準 Schrödinger dynamics の修正を提案した。[Everett 1957](https://doi.org/10.1103/RevModPhys.29.454); [Bohm 1952a](https://doi.org/10.1103/PhysRev.85.166); [Bohm 1952b](https://doi.org/10.1103/PhysRev.85.180); [Ghirardi, Rimini & Weber 1986](https://doi.org/10.1103/PhysRevD.34.470)

objective-collapse models は「解釈の差」に留まらず modified dynamics と追加 predictions を持ち、実験的に parameter space が制約される。[Bassi et al. 2013](https://doi.org/10.1103/RevModPhys.85.471); [Carlesso et al. 2022](https://doi.org/10.1038/s41567-021-01489-5) したがって「量子解釈はすべて経験的に同値」とは書けない。

### 9.4 Literature flow

~~~text
successful operational formalism + laboratory records
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
 empirical-domain comparison   conceptual problems
 standard vs modified dynamics measurement / probability /
          │                    macroscopic facts / relativity
          ▼                     │
 exclusion bounds or           ▼
 new predictions        interpretive constructions
          │                     │
          └──────────┬──────────┘
                     ▼
 comparison by empirical fit, coherence, scope,
 simplicity, causal/explanatory structure, QFT extension
                     │
             plural but non-equal appraisal
~~~

### 9.5 Required conditions for comparison

- 比較する object が mere interpretation、mathematically distinct theory、parameterized modification のどれかを明示する。
- empirical equivalence を主張する domain を限定する。
- equilibrium assumptions、Born-rule derivation、collapse parameter、relativistic extension 等を theory-specific に記載する。
- explanation、simplicity、unification、causal structure を empirical likelihood と混同せず、評価基準として明示する。

### 9.6 Failure modes

- standard operational agreement を全 variants・全 regimes の完全 equivalence とする。
- no-go theorem が採用しない theory family まで自動排除したと読む。
- formalism の経験的成功を一つの interpretation の演繹的証明とする。
- formalism が ontology を一意に選ばないことから、全解釈が同程度に良いとする。
- objective-collapse のような empirically distinguishable modifications を pure interpretation と一括する。
- $\psi$-epistemic ontological model と information-centered interpretation を同義にする。

### 9.7 Remedies and substitutions

- domain-indexed empirical equivalence を記録する。
- standard formalism の再解釈と dynamics modification を別表にする。
- no-go theorem の assumption set と各 interpretation の formal membership を個別に照合する。
- experimental constraints、QFT extension、internal consistency、explanatory criteria を複数軸で比較する。

### 9.8 Residual ambiguity

経験的に同じ domain を共有する複数 program の間では、data likelihood 以外の criteria が残る。他方、追加 predictions がある theory は experiment により区別されうる。したがって残余曖昧性は一様でも永久でもなく、theory pair と domain に相対的である。

### 9.9 Backgrounded assumptions / stabilized interfaces

interpretation literature は、Born-rule frequencies、tomographic state assignments、Bell behavior など operational results を入力として扱い、detector calibration や finite-sample pipeline の詳細を背景化しやすい。これは分業として合理的だが、operational conclusion から metaphysical conclusion への handoff が自動的な theorem edgeになるわけではない。

### 9.10 Upstream assumptions and downstream handoff

- **Upstream:** operational formalism、no-go results、experimental bounds、relativity/QFT requirements。
- **Downstream:** metaphysics of laws/properties、explanation、theory choice、new experimental proposals。

### 9.11 Edge register

| From | To | Edge type | Illumination |
|---|---|---|---|
| modified collapse dynamics | experimental parameter bounds | theorem + statistical/experimental support | Fully illuminated |
| quantum equilibrium | Bohmian recovery of Born statistics | theorem/modeling assumption | Fully illuminated within theory |
| operational equivalence in a domain | empirical tie in that domain | theorem/model comparison | Locally illuminated |
| empirical tie | equal explanatory merit | no implication | explicit methodological warning |
| formal success | unique interpretation | no implication without added criteria | explicit residual ambiguity |

---

## 10. Subnetwork G — Philosophy and methodology of science

### 10.1 Problem families

この領域は量子論の下位理論ではない。実験データ、モデル、仮説、補助仮定、介入、理論選択の関係を別の抽象度で扱う。物理側との exact correspondence を前提にしない。

### 10.2 Formal objects

形式対象は program ごとに異なり、theory–auxiliary package、data model、phenomenon claim、error probability、identified set、causal graph、intervention、model class、theory virtues などを含む。これらを一つの数学的 object に還元せず、どの inferential relation を扱うかで分ける。

### 10.3 Underdetermination and empirical adequacy

Duhem–Quine 系の論点は、仮説が単独で observation consequence を持つのではなく補助仮定と共に tested package を作ること、同じ evidence と整合する代替記述がありうることを区別してきた。[SEP: Underdetermination of Scientific Theory](https://plato.stanford.edu/entries/scientific-underdetermination/)

van Fraassen の constructive empiricism は empirical adequacy を科学の目標として提示し、theory acceptance を unobservable ontology の belief と同一視しない。[van Fraassen 1980](https://doi.org/10.1093/0198244274.001.0001)

Stanford の unconceived alternatives は、現在比較している理論集合が歴史的に不完全でありうることを問題化する。[Stanford 2006](https://global.oup.com/academic/product/exceeding-our-grasp-9780195174080) これは有限の候補内 identification と、比較集合の十分性を区別する強い哲学的先行形であるが、特定の量子モデル検定と exact match ではない。

### 10.4 Data, phenomena, calibration, and intervention

Suppes の models of data は、raw experimental situation と theory の間に構成された data model があることを形式化する先駆的研究である。[Suppes 1962](https://errorstatistics.files.wordpress.com/2016/12/suppes-p-1962-models-of-data.pdf)

Bogen and Woodward は data と phenomena を区別し、個々の detector records から relatively stable phenomena への推論を扱う。[Bogen & Woodward 1988](https://doi.org/10.2307/2185445)

Collins の experimenter’s regress は、装置が正しく働いたかと、現象が正しい結果を与えたかの相互依存を社会学的・実践的問題として分析する。これを GST gauge theorem や calibration equation と同一視はできないが、校正の証拠構造に対する強い先行形である。[SEP: Experiment in Physics](https://plato.stanford.edu/entries/physics-experiment/)

Hacking の intervention-centered realism と Woodward の interventionism は、観察だけでなく操作可能性、安定した因果関係、介入による検査を前景化する。[Hacking 1983](https://doi.org/10.1017/CBO9780511814563); [Woodward 2003](https://doi.org/10.1093/0195155270.001.0001)

### 10.5 Error probing, partial identification, and misspecification

Mayo の severe testing は、結果が仮説を支持する強さを、誤りを高確率で検出できたかという test performance と結びつける。[Mayo 2018](https://doi.org/10.1017/9781107286184) これは Bell loophole closure や tomography confidence と方法論的に近いが、量子実験の全保証構造を既に一つにしたものとは確認していない。

Manski の partial identification は、仮定を弱めたとき point estimate を無理に出さず、データと仮定が許す identified set を報告する。[Manski 2003](https://doi.org/10.1007/b97478)

White の misspecified maximum-likelihood theory は、指定 statistical model が真でなくても estimator がどの pseudo-true target へ収束するかを扱う。[White 1982](https://doi.org/10.2307/1912526) これは tomography の model violation と接続可能だが、M-open theory choice と同じ概念ではない。

causal identifiability / do-calculus は、observational and interventional distributions と causal graph assumptions から causal query が一意に定まる条件を扱う。[Shpitser & Pearl 2006](https://dl.acm.org/doi/10.5555/1597538.1597540) Bell causal models と形式的接点を持つが、量子 ontology 一般の選択原理ではない。

### 10.6 Literature flow

~~~text
worldly interaction / apparatus
        │
        ├──▶ records ──▶ data model ──▶ phenomenon claim
        │                     │                │
        │               calibration /         │
        │               error probing          ▼
        └── intervention ─────────────▶ causal/explanatory model
                                              │
                  ┌───────────────────────────┼──────────────┐
                  ▼                           ▼              ▼
         severe test / error control   partial ID      misspecification
                  │                           │              │
                  └────────── evidence appraisal ────────────┘
                                              │
                      empirical adequacy / theory choice
                                              │
                    underdetermination / unconceived alternatives
~~~

### 10.7 Required conditions

哲学・方法論側は単一の条件集合を共有しない。各 program は、observation consequence を作る補助仮定、data reduction、error probabilities、intervention criterion、model family、theory virtues のいずれかを前景化する。

### 10.8 Failure modes

- empirical adequacy、truth、acceptance を一語で扱う。
- raw data と processed data model と phenomenon を同一視する。
- underdetermination の可能性だけから、全理論が等価または evidence が無力とする。
- auxiliary assumptions があることから severe test が不可能とする。
- partial identification を「何も識別できない」と読む。
- experimenter’s regress を全 calibration の普遍的不可能定理にする。

### 10.9 Remedies and substitutions

- tested package と individual assumptions を分ける。
- data processing、calibration、robustness、replication を明示する。
- point identification が無理なら identified set と sensitivity analysis を報告する。
- error probe、negative control、intervention、independent calibration を組み合わせる。
- 現候補集合外の alternatives を理論史、model expansion、misspecification test により探索する。

### 10.10 Residual ambiguity

これらの方法論は、量子実験に対する一つの完成された assurance graph を共同で提供するわけではない。むしろ、data construction、error control、causal identification、theory choice の異なる層をそれぞれ強く照らす。相互関係には多数の文献があるが、用語と研究目的は統一されていない。

### 10.11 Backgrounded assumptions / stabilized interfaces

哲学文献は、具体的な POVM span、GST sequence、Bell time-tag statistic を背景化する。物理文献は、theory acceptance、unconceived alternatives、data/phenomena distinction を背景化する。この相互背景化は分業の結果であり、それだけで gap ではない。

### 10.12 Upstream assumptions and downstream handoff

- **Upstream:** scientific practice、statistical models、experimental records、causal and explanatory aims。
- **Downstream:** evidence appraisal、realism debate、methodological prescriptions、theory comparison。

### 10.13 Edge register

| From | To | Edge type | Illumination |
|---|---|---|---|
| raw records | data model / phenomenon | methodological association + inferential construction | Fully illuminated in philosophy |
| test design | evidential severity | statistical/methodological dependence | Fully illuminated |
| weakened assumptions | identified set | theorem/methodological implication | Fully illuminated |
| current alternatives | global theory adequacy | no deductive implication | Fully illuminated warning |
| philosophy frameworks | specific quantum protocols | usually historical/methodological association | Weakly connected, case-dependent |

---

## 11. Cross-cutting failure modes

一つの failure mode を一つの node に排他的に割り当てると、実際の因果的多重作用を失う。必要なら発生源または最初に検出する場所を primary site と呼べるが、downstream impact は別に保持すべきである。

### 11.1 Drift and nonstationarity

~~~text
source / device / reference-frame drift
        ├── breaks fixed-preparation interpretation
        ├── changes the estimand from one state to a mixture/time average
        ├── invalidates a fixed calibration transfer
        ├── creates model violation in GST
        └── can induce inter-trial dependence in Bell data
~~~

最後の枝は Bell の memory loophole と重なる場合があるが同義ではない。memory-robust statistics は任意の過去依存を許すことがあり、drift は特定の物理的非定常性である。

### 11.2 SPAM and calibration error

~~~text
unknown preparation + unknown measurement
        ├── biases state tomography
        ├── biases process tomography
        ├── confounds gate errors
        ├── changes realized Bell behavior
        └── perturbs operational equivalences in contextuality tests
~~~

GST は最初の三枝を共同推定へ移すが、gauge と model adequacy の問題を残す。Bell や contextuality では、装置内部の完全記述ではなく、behavior-level robustness または self-testing により一部を回避する別経路がある。

### 11.3 Gauge and reference-frame ambiguity

gauge は単なるノイズではない。観測確率を不変にする representation freedom であり、gate-set parameter の一意性と、一部の gauge-variant performance metric を同時に制限する。reference-frame drift は物理誤差になりうるが、固定 gauge orbit 内の表現自由度とは別である。

### 11.4 Dimension error, leakage, and factorization error

~~~text
actual degrees of freedom exceed assumed model
        ├── invalidates IC claim relative to stated d
        ├── moves data outside state/process model
        ├── creates apparent non-Markovian gate behavior
        ├── undermines subsystem/tensor-factor labels
        └── changes scope of self-testing or dimension certification
~~~

dimension witness や leakage diagnostic はこの risk を制約するが、あらゆる未モデル自由度の不存在を証明する万能 test ではない。

### 11.5 Selection, loss, and event construction

detector loss、postselection、coincidence window、stopping rule は、raw events から analyzed sample への写像を変える。tomography では sampling bias、Bell では detection/coincidence loophole、contextuality では operational-equivalence sample の偏りとして現れる。原因が同じ detector にあっても、壊す theorem edge は異なる。

### 11.6 Dependence and common causes

次は同じ「独立性」ではない。

| Domain | Condition | What is separated |
|---|---|---|
| tomography | i.i.d., exchangeability, or theorem-specific dependence control | trials / prepared systems |
| Bell | measurement independence | settings and relevant hidden/common-cause variables |
| PBR | preparation independence | ontic state of separately prepared systems |
| randomized experiment design | randomization validity | selection mechanism and target quantities |

数式上 conditional independence を用いる点は共通するが、random variables、causal role、violation consequence が違う。統合図は similarity を示せるが、一つの universal independence assumption には置換できない。

### 11.7 Model misspecification

指定 model がデータ生成過程を含まないと、同じ failure は異なる形で現れる。

- tomography: pseudo-state、poor fit、dimension leakage、time average。
- GST: non-Markovian residual、context-dependent gate、gauge-invariant lack of fit。
- Bell: tested inequality と実際の event process の不整合。
- contextuality: intended operational equivalence や compatibility の不成立。
- interpretation: 比較集合が relevant alternatives を含まない。

「model misspecification」はこれらを診断する単一 theorem ではなく、各分野の具体的 checks を束ねる上位語である。

### 11.8 Cross-impact matrix

| Failure mode | Tomography | Calibration/GST | Discrimination | Bell | Contextuality | Interpretation |
|---|---:|---:|---:|---:|---:|---:|
| drift / nonstationarity | fixed target, coverage | fixed gate set | ensemble prior | memory/statistics | operational equivalence | empirical-domain claims |
| SPAM error | state bias | confounding | realized POVM | behavior estimate | equivalence test | usually upstream |
| gauge / reference | coordinates | primary formal issue | labels/cost basis | setting semantics in special cases | procedure identity | representation comparison |
| dimension/leakage | model space | process model | ensemble/resource | device model | compatibility realization | theory scope |
| selection/event rule | sample | likelihood | risk estimate | major loopholes | inequality sample | evidential input |
| initial/dependence assumptions | sample theorem | drift model | multi-copy source | measurement independence | PBR composition | usually upstream |

この表は各 failure の同一性を主張しない。作用先が複数あることを示す索引である。

---

## 12. Prior-art integrated graph

分野別グラフを

$$
G_{\mathrm{T}},\;
G_{\mathrm{Cal}},\;
G_{\mathrm{D}},\;
G_{\mathrm{B}},\;
G_{\mathrm{C}},\;
G_{\mathrm{I}},\;
G_{\mathrm{P}}
$$

と表す。ここで T は tomography、Cal は calibration、D は discrimination、B は Bell、C は contextuality、I は interpretation、P は philosophy/methodology である。重ね合わせた $G_{\text{prior-art}}$ の概略は次のようになる。

~~~text
                         ┌─────────────────────────────┐
                         │ references / calibration   │
                         │ detector, source, SPAM, GST│
                         └───────┬───────────┬─────────┘
                                 │           │
               calibration edge │           │ model/gauge diagnostics
                                 ▼           ▼
┌───────────────────┐     ┌──────────────────────┐
│ state preparation │────▶│ tomography/estimation│
│ and supplied copies│     │ state/property target│
└──────┬────────────┘     └────────┬─────────────┘
       │                            │ operational state / predictions
       ▼                            │
┌────────────────────┐              │
│ discrimination and │              │
│ resource constraints│             │
└──────┬─────────────┘              │
       │                            ▼
       │                  ┌───────────────────────┐
       └─────────────────▶│ operational procedures│
                          │ and behavior records  │
                          └───────┬────────┬──────┘
                                  │        │
                                  ▼        ▼
                         ┌────────────┐  ┌────────────────┐
                         │ Bell tests │  │ contextuality /│
                         │ causal class│  │ ontological    │
                         │ exclusion  │  │ model no-go    │
                         └─────┬──────┘  └──────┬─────────┘
                               │                │
                               └──────┬─────────┘
                                      ▼
                           constrained theory/model space
                                      │
                                      ▼
                         ┌────────────────────────┐
                         │ interpretation and     │
                         │ theory comparison      │
                         └───────────┬────────────┘
                                     │
                ┌────────────────────┴──────────────────┐
                ▼                                       ▼
  philosophy of experiment/statistics       underdetermination/
  data models, severity, intervention        empirical adequacy/
                                             unconceived alternatives
~~~

この図は一方向の証明鎖ではない。

- calibration と tomography は循環的依存を self-consistent estimation や external references へ組み替える。
- Bell correlations は self-testing を通じて device characterization へ逆向きに寄与しうる。
- discrimination resource theory は tomography design と通信課題の双方へ分岐する。
- philosophy は下流の解釈だけでなく、上流の data construction と calibration にも cross-reference を持つ。
- interpretation program は新しい experiment proposal を生み、実験側へ戻りうる。

### 12.1 Cross-domain connection ledger

| Source region | Target region | Prior-art connection | Status |
|---|---|---|---|
| calibration/GST | tomography | unknown SPAM biases inference; joint estimation and gauge | Fully connected |
| tomography | discrimination | different targets; estimation/discrimination bounds and multi-copy resources overlap | Fully connected |
| Bell | self-testing/calibration | behavior certifies state/measurements up to equivalence under assumptions | Fully connected within device-independent literature |
| Bell | causal models | DAG/fine-tuning/quantum common cause | Fully connected |
| contextuality | operational experiments | equivalence and compatibility tests feed inequalities | Fully connected locally |
| Bell | contextuality | shared polytope/resource methods, but distinct assumptions | Partially connected with explicit literature |
| PBR | ontology interpretation | theorem narrows ontological-model classes | Explicit handoff; not a unique-choice edge |
| tomography | interpretation | density operator estimate becomes interpretive input | Cross-domain handoff, usually implicit |
| GST gauge | theory representation | operational equivalence/gauge analogy | Partially connected; exact scope differs |
| experimental methodology | quantum protocol design | severity, calibration, intervention, data construction | Historical/methodological association; uneven direct citation |
| unconceived alternatives | quantum model comparison | warns against closure of current comparison set | Close philosophical analogue; direct technical edge weak |

---

## 13. Strongly connected regions

### 13.1 Tomography–calibration–estimation

この領域は最も強く接続されている。IC、frame conditioning、finite-sample confidence、SPAM、joint estimation、gauge、model violation が同一または密接な文献群で扱われる。既存研究は「測定写像が非単射なら困る」よりはるかに精密で、target、equivalence class、error metric、resource scaling を与える。

### 13.2 Bell experiment–finite statistics–causal assumptions

Bell 分野も強く接続されている。factorization、PI/OI、measurement independence、no-signaling、detector selection、memory、coincidence、finite statistics、space-time design が明示的に分解されている。generic な「因果 interface」語彙より既存 Bell 語彙の方が、このケース内では精密である。

### 13.3 Operational equivalence–contextuality–ontological-model exclusion

Spekkens 型 framework 以後、operational equivalence から noncontextual ontological representation への条件、実験 inequality、no-go conclusion が強く接続される。PBR は別枝であり、preparation composition assumption を持つ。この区別も既存文献側で明示されている。

### 13.4 Modified dynamics–experimental bounds

objective-collapse のように追加 predictions を持つ theory では、interpretation discussion と experiment が直接接続する。これは「ontology は常に observationally underdetermined」という普遍命題への反例でもある。特定 parameter range や dynamics は、データで排除・制約されうる。

---

## 14. Weakly connected and handed-off regions

### 14.1 From laboratory identifiability to interpretation

tomography は density operator を operational model 内で識別し、interpretation literature はその意味を論じる。両者の区別自体は標準的だが、校正 uncertainty、model violation、gauge equivalence が最終 interpretive comparison にどう伝播するかを一つの共通 ledger で追う文献は、今回の監査では中心的伝統として確認できなかった。

これは missing theorem とは限らない。通常、interpretation differences は laboratory estimation error より大きく概念的であり、上流 uncertainty の詳細を持ち込んでも比較が変わらないため、合理的に handoff されている可能性が高い。

### 14.2 From experimental design to philosophical underdetermination

Hacking、Mayo、Collins、Woodward など、介入、error probing、calibration practice を扱う哲学はある。量子側にも active design、loophole closure、self-testing がある。したがって両端は未研究ではない。しかし、同じ formal object と評価尺度で結ばれた一つの量子固有理論ではなく、methodological association と case-by-case handoff が多い。

### 14.3 Across independence assumptions

tomography の exchangeability、Bell の measurement independence、PBR の preparation independence は互いに参照されることがあるが、共通の「independence node」へ統合するより、変数と causal role を保存する方が正確である。接続が弱いことの一部は用語分断ではなく、研究対象が本当に異なるためである。

### 14.4 Metrology and foundations

traceability、reference standards、electronics、uncertainty budgets は laboratory metrology で扱われ、foundations papers は operational behavior を所与にする。この handoff は弱く見えるが、Bell experimental papers の methods、detector calibration、randomness characterization により実務上は接続される。単なる無視とは判定できない。

---

## 15. Candidate apparently-unconnected edges

未接続 edge と呼ぶための四条件、すなわち両端が確立、接続が研究上有意味、直接文献が弱い、接続により推論が変わること、を適用した。

| Candidate | Audit result | Classification |
|---|---|---|
| tomography preparation assumptions ↔ Bell setting independence | いずれも independence だが random variables と causal role が違う。直接接続しても theorem scope は統合されない | merely adjacent unless a specific protocol couples them |
| calibration/gauge ↔ adequacy of the physical model | GST 自身が gauge と model violation を区別する。dimension/leakage diagnostics もある | already partially connected |
| statistical identifiability ↔ quantum interpretation | 区別は既知。uncertainty propagation を解釈比較へ組み込む共通 protocol は弱いが、結論を変える事例未確認 | Weakly connected; added value unproven |
| no-go model-class exclusion ↔ ontology choice | foundations literature が theorem scope と残る解釈を明示的に論じる | already connected; no unique-choice edge by design |
| experiment design ↔ philosophical underdetermination | severe testing、interventionism、experiment philosophy が接続を提供するが、量子技術文献との直接相互参照は uneven | Cross-domain handoff, not established missing edge |
| calibration traceability ↔ theory-comparison evidence weights | 両端は確立しているが、統一された propagation formalism を今回確認できず、実際の decision impact も未実証 | Unknown due to incomplete audit |

したがって、四条件を満たす genuine missing edge は現段階で確定しない。最後の候補は探索価値があるが、「今回見つからなかった」以上の主張はできない。

---

## 16. What is backgrounded where

| Field | Foregrounded | Commonly backgrounded or handed off |
|---|---|---|
| state tomography | IC、estimator、sample complexity、confidence | absolute calibration、interpretation、full source ontology |
| calibration/GST | SPAM、gauge、sequence design、model violation | ultimate external standard、theory choice |
| discrimination | ensemble、loss、POVM、copy resource | source construction、ontology of labels |
| Bell methodology | locality、settings、detection、memory、trial definition | full detector tomography、interpretation winner |
| contextuality/no-go | operational equivalence、ontological-model assumptions | electronics、raw data reduction、global theory choice |
| interpretation | meaning、explanation、dynamics、QFT/cosmology | finite-sample tomography and daily calibration |
| philosophy/methodology | evidence structure、data models、error、underdetermination | protocol-specific quantum algebra and hardware |

背景化は、ある条件が未検討であることを意味しない。多くは別文献、装置設計、standard operating procedure、metrology へ合理的に委譲されている。

---

## 17. Coverage verdict before comparison with v0.2

既存研究だけから、次の構造は自然に再構成できた。

1. 状態または query の形式的 target。
2. measurement span と ideal identifiability。
3. finite-sample estimation、confidence、stability。
4. calibration、SPAM、reference、gauge-equivalence。
5. copy、collective access、joint measurability、instrument disturbance。
6. Bell の causal/statistical assumption decomposition と loophole methodology。
7. operational equivalence と no-go theorem の model-class-relative exclusion。
8. empirical equivalence domain と theory-specific interpretive criteria。
9. data construction、severity、partial identification、misspecification、underdetermination。

個々の nodes と local edges の大半は既に明示的である。弱いのは、これらを一つの assurance case として横断追跡する共通表示と、一部の handoff である。ただし共通表示が推論または実験を改善した事例は、この再構成だけでは示されない。

---

## 18. Adversarial-review verification ledger

添付査読は Case Study 01 の改訂指示ではなく、prior-art reconstruction で見落としやすい箇所を示す検索入力として扱った。次の表は、査読の主要主張を一次文献・権威的レビューと照合した結果である。

| Review claim | Verdict | Literature-based reason / action |
|---|---|---|
| Bell section needs PI/OI and measurement-independence decomposition | **accepted** | Jarrett decomposition と Bell reviews が標準的に区別する。§7.2 に再構成した |
| memory and coincidence-time loopholes were missing | **accepted** | 両者には独立の literature と remedies がある。§7.5 に追加した |
| Bell vocabulary already covers much of the proposed generic causal-interface vocabulary | **partially accepted** | Bell 文脈では locality/communication loophole、setting leakage、shielding、trial structure の方が精密。一般制御系への拡張まで同一とは確認しない |
| usefulness cannot be judged without comparison to prior art | **accepted** | §2.5 の反証基準と §§19–23 の比較を採用した |
| if deleting the network leaves all content intact, value may be presentation only | **accepted as a falsification criterion** | quantum case では実際にこの test を適用する。一般的方法論全体の十分条件とはしない |
| informational completeness proposition should be iff, not one-way | **accepted** | Hermitian span と kernel construction により固定有限次元モデルで必要十分。§4.2 に修正した |
| tomography does not universally require i.i.d. | **accepted with qualification** | de Finetti/postselection 等が weaker structures を扱う。ただし random permutation は物理的独立性を作らず、finite symmetry と infinite exchangeability も別。§4.4 |
| no-signaling, PI, and OI need finer treatment | **accepted with qualification** | operational no-signaling と hidden-level PI は同値でない。標準量子表現の PI/OI attribution は representation-relative。§7.2 |
| every failure mode should have one exclusive primary node | **rejected** | drift、SPAM、selection は複数の保証 edge を因果的に壊す。発生源の指定は可能だが cross-impact を消す排他配属は不適切。§11 |
| in general probabilistic theories, broadcastability and joint measurability are simply equivalent, leaving only destructiveness and one-copy limits independent | **rejected as overgeneralized** | quantum observables だけでも compatibility、nondisturbance、broadcastability 等は階層であり同値でない。[Heinosaari 2016](https://doi.org/10.1103/PhysRevA.93.042118) GPT-level equivalenceには追加構造が必要で、査読は条件を示していない |
| Bell’s “La nouvelle cuisine” is a 1976 source | **rejected: bibliographic error** | “La nouvelle cuisine” は1990年刊行。1970年代の local-beables papers と混同されている。[Bell 1990](https://doi.org/10.1017/CBO9780511815676.026) |
| only one genuine open question remains | **deferred / unsupported** | exhaustive systematic audit がないため、open question 数を確定できない |

この台帳の目的は査読に反論することではなく、査読も含めた correction trail を残すことである。

---

## 19. Comparison with the v0.2 audit network

ここで初めて v0.2 の用語を用いる。比較単位は名称ではなく、既存研究が既に持つ distinction と edge である。

### 19.1 Comparison table

| v0.2 item | Prior-art reconstruction | Assessment |
|---|---|---|
| target specification | state/property/process/behavior/ontological-model target の区別 | **already explicit in prior art** |
| candidate-class adequacy | dimension assumption、restricted-state model、leakage、misspecification、unconceived alternatives | **same distinction under different terminology**; technical treatment is field-specific |
| experiment availability | allowed POVMs、control sequences、copy number、setting implementation | **already explicit in prior art** |
| Experimental Amalgamation (EA) | joint measurability、common POVM、instrumental sequential compatibility、multi-copy allocation、collective measurement、adaptive design | no single exact match; **audit network combines existing but non-equivalent edges** |
| informational vs physical joint realizability | data postprocessing vs joint POVM/instrument/copy protocol | **already explicit under different local vocabularies** |
| dynamic CIF | Bell locality/communication loophole、cross-talk、shielding、declared control dynamics | in Bell, **prior art is more precise**; outside Bell, generic factorization may be a useful abstraction but is unvalidated here |
| preparation / initial independence | tomography sampling assumptions、Bell measurement independence、PBR preparation independence | the v0.2 umbrella is useful only if it preserves these differences; **prior art is more precise** |
| stable recording | time tags、event construction、data models、traceability | **already explicit**, but dispersed |
| statistical identifiability and inverse stability | IC、Fisher/frame conditioning、risk、confidence、sample complexity | **prior art is substantially more precise** |
| ontological bridge | underdetermination、empirical adequacy、ontological models、interpretation criteria | **same concern under established philosophy/foundations vocabularies** |
| auxiliary-condition auditability labels | calibration evidence、design closure、statistical validation、model-relative theorem | **audit network may add a common display**, not new evidential relations |
| prerequisite network as a whole | union of local literatures and handoffs | **possible cross-domain visualization**, methodological value unproven |

### 19.2 Where prior art is more precise

- Bell の CIF-like 問題は、PI/OI、measurement independence、locality、detection、memory、coincidence、trial definition に分解される。
- EA-like 問題は、joint measurability、nondisturbance、instrument、fresh source、collective access へ分かれる。一つの「共同実現可能性」だけでは theorem scope が粗い。
- candidate-class adequacy は、tomography の dimension/leakage、GST の model violation、statistics の misspecification、philosophy の unconceived alternatives で異なる検査を持つ。
- ontological inference は、PBR 型 model-class exclusion、modified-dynamics comparison、empirical-equivalence domain、一般 underdetermination を分ける必要がある。

### 19.3 Where the audit network may combine existing edges

- ある結論が theorem-relative、calibration-supported、design-supported、statistically constrained、interpretive のどれかを一枚で追跡する。
- drift や SPAM のような cross-cutting failure が複数 field のどの edge を壊すかを表示する。
- laboratory identification から foundations への handoff と、そこで backgrounded になる条件を同じ図に置く。

これらは可視化上の候補価値である。既存分野が持たない新しい依存関係を証明したわけではない。

### 19.4 Unsupported novelty claims

次は本調査から支持されない。

- CIF が Bell methodology に新しい区別を与えた。
- EA が joint measurability、instrument theory、experimental design を置換する新しい数学構造である。
- candidate-class adequacy が misspecification または underdetermination と別の新原理である。
- ontological non-self-certification が Duhem–Quine、constructive empiricism、no-go theorem scope を超える新定理である。
- 共通図が作れること自体が methodological contribution である。

### 19.5 Erasure test

v0.2 固有の node names を消しても、§§4–10 の物理・統計・哲学上の内容は成立する。IC、GST gauge、Helstrom discrimination、Bell assumption decomposition、generalized contextuality、collapse-model tests、underdetermination は、それぞれ既存の語彙と theorem で記述できる。

消えるのは、主に

- 同じ failure の横断表示、
- upstream/downstream handoff の共通 ledger、
- evidential support type を一枚で比較する表示

である。したがって量子ケースだけから確認できる追加価値は、現時点では **presentation / indexing / cross-domain visualization** に留まる。実験設計や結論を変更した実例が出るまで、audit procedure の方法論的価値は未実証である。

---

## 20. What is merely reclassification

次は既存研究の再命名または再配列であり、新規内容として数えない。

- state identifiability と state ontology の区別。
- ideal identifiability、finite-sample estimability、stability の区別。
- known-POVM tomography と self-consistent SPAM estimation の区別。
- fresh source と cloning の区別。
- informational postprocessing と physical joint measurement の区別。
- Bell factorization、measurement independence、loophole closure の分解。
- no-go theorem の model-class-relative scope。
- formalism success と unique interpretation の非同一性。
- misspecification、partial identification、underdetermination。

これらは量子情報、量子基礎論、統計学、科学哲学ですでに強く照明されている。

---

## 21. What may gain visibility

限定的に可視性が増す可能性があるのは次である。

1. **Assumption provenance:** ある条件が theorem、device design、independent calibration、statistical model、interpretive criterion のどこから来たかを同一表示にする。
2. **Cross-impact:** 一つの drift、SPAM、selection error が複数の保証関係を壊す様子を保存する。
3. **Backgrounding map:** ある分野で所与とされる output が、上流では何を条件に作られたかを追う。
4. **Scope preservation:** 同じ independence、equivalence、factorization という語でも variables と causal role が異なることを横断図で警告する。
5. **Handoff visibility:** statistical/model-class exclusion と interpretation choice の間に、追加 criteria が置かれる場所を明示する。

しかし、これらの visibility が専門家の誤りを実際に発見するか、protocol を改善するか、既存レビューより速く正確な audit を可能にするかは未検証である。

---

## 22. Open literature checks

1. **Metrological traceability and foundations:** quantum electrical/optical metrology の traceability literature と Bell/contextuality foundations の直接的接続を systematic に監査する。
2. **Non-i.i.d. tomography:** exchangeable、martingale、adversarial、drifting source に対する confidence guarantees を同一 taxonomy で比較する。
3. **Gauge, model selection, and leakage:** GST gauge orbit、non-Markovian model violation、dimension/leakage model selection の formal relations を精査する。
4. **Device-independent certification:** self-testing が calibration dependency をどこまで置換し、local-isometry equivalence と finite robustness に何を残すかを独立節で再構成する。
5. **Bell trial construction:** memory、coincidence、stopping、time-tag analyses の最新 authoritative review を systematic に比較する。
6. **General probabilistic theories:** cloning、broadcasting、compatibility、nondisturbance の equivalence/hierarchy に必要な no-restriction、local tomography 等の assumptions を確認する。
7. **Interpretation comparisons:** standard operational equivalence、nonequilibrium Bohm variants、collapse predictions、relativistic/QFT extensions を pairwise domain table にする。
8. **Philosophy-to-protocol links:** severity、experimenter’s regress、models of data が具体的量子 protocol の design decision に直接使われた事例を探索する。
9. **Head-to-head benchmark:** 本統合図を、標準 tomography review、GST review、Bell RMP、contextuality RMP、量子解釈 review の組み合わせと比較し、retrieval accuracy と missed-assumption detection を測る。

これらは「未解決の暗部」の一覧ではない。多くは本ノートの literature coverage を改善する課題である。

---

## 23. Answers to the four comparison questions

### Q1. 量子論の既存研究だけで、v0.2にかなり近いネットワークは自然に再構成できるか

**Yes, substantially.** 局所 nodes とその保証 edges の大半は、既存研究の方が精密な用語と theorem scope を持つ。特に tomography–calibration と Bell methodology ではそうである。

### Q2. できる場合、v0.2の追加価値は何か

- **Vocabulary:** 一部の分野横断索引としては使えるが、field-native terminology を置換すべきでない。
- **Visualization:** cross-impact、backgrounding、handoff を一枚に置く価値はありうる。
- **Cross-domain mapping:** 現段階で最も擁護可能な価値。
- **Audit procedure:** practical diagnostic impact が示されておらず未実証。
- **Mathematical content:** 本ケースで追加は確認できない。

### Q3. 再構成しにくい部分の原因は何か

主に **literature fragmentation、terminology differences、research-goal differences** の混合である。genuine missing edge は確認できない。metrology から theory comparison への uncertainty propagation などは弱く見えるが、現段階では **audit不足** と分離できない。

### Q4. 「存在論的非自己証明性」は underdetermination 等の再記述だけか

中心的な論理主張、すなわち empirical/formal success 単独から unique ontology が演繹されないという点は、underdetermination、empirical adequacy、ontological-model scope、interpretation literature に強い先行形がある。概念的新規性は主張できない。

実験設計、校正、識別、統計、解釈を同じ guarantee provenance の下で並べることには配置上の価値がありうる。しかし本量子ケースでは、その配置が新しい推論、見落とし、実験変更を生んだことを示せていない。よって追加価値は候補であって確立した contribution ではない。

---

## 24. Final verdict

### Classification

**Type B — Existing nodes, weak cross-domain edges**, with a strong Type A component.

- **Type A component:** 各 subnetwork と主要 local edges は既存研究だけで十分に得られる。監査ネットワークの名称を除いても科学的内容は残る。
- **Type B reason:** laboratory calibration、statistical identification、no-go exclusion、interpretation、philosophy の間の handoff は、分散した文献を跨がないと一望しにくい。
- **Why not Type C yet:** common audit structure が誤り発見、evidence appraisal、experiment design を改善した再現可能な事例がない。
- **Why not Type D:** 既存研究に欠ける重要な依存関係を確定していない。

したがって、量子ケースに関する Scientific Identifiability Prerequisite Network の価値判定は、

> **organizational usefulness is plausible; methodological usefulness remains unproven**

である。既存研究に対する優位性を主張しない。

---

## 25. Final self-audit

| Check | Result | Note |
|---|---|---|
| 1. v0.2 nodesを先に押し付けなかったか | pass | 比較語彙は §19 まで保留した |
| 2. 既存研究を最大限強く再構成したか | pass with scope limit | authoritative reviews と primary results を優先したが systematic review ではない |
| 3. 未接続と調査不足を分けたか | pass | §15、§22 |
| 4. failure mode の多重作用を保存したか | pass | §11 の cross-impact |
| 5. 既存概念を新発見扱いしていないか | pass | §20 |
| 6. node より edge を見たか | pass | edge registers と integrated ledger |
| 7. 分野内既知と分野間弱接続を分けたか | pass | §§13–15 |
| 8. 背景化を批判語にしていないか | pass | §16 |
| 9. 哲学を物理の下位説明にしていないか | pass | 独立 subnetwork とした |
| 10. 監査ネットワーク不要の結論を許したか | pass | erasure test は presentation-only 寄り |
| 11. 「真理不在性」を先取りしていないか | pass | theorem claim として使用していない |
| 12. 最終判定が文献配置から出たか | pass | Type B、C/D不採用理由を明示した |
| 13. Bell assumptions を十分分解したか | pass | PI/OI、MI、no-signaling、loopholes を分離した |
| 14. 査読を権威化しなかったか | pass | §18 に棄却・限定採用を含む |

> **一文での回答:** 現段階で量子論に残って見えるものは、未知の暗部そのものより、十分に発達した既知の照明が分野別に配置され、その相互 handoff と保証の出所が一望しにくいことである。ただし metrology から theory comparison への接続などには文献監査不足が残るため、すべてを単なる配置問題とも断定しない。

---

## 26. References

本 bibliography は各 subnetwork の再構成に用いた主要原論文、標準的レビュー、monograph を分野別に記録する。完全な systematic bibliography ではない。

### Quantum tomography, estimation, and model checking

1. D’Ariano, G. M., Paris, M. G. A., & Sacchi, M. F. (2003). “Quantum Tomography.” *Advances in Imaging and Electron Physics*, 128, 205–308. [doi:10.1016/S1076-5670(03)80065-4](https://doi.org/10.1016/S1076-5670(03)80065-4)
2. Scott, A. J. (2006). “Tight Informationally Complete Quantum Measurements.” *Journal of Physics A*, 39, 13507–13530. [doi:10.1088/0305-4470/39/43/009](https://doi.org/10.1088/0305-4470/39/43/009)
3. Christandl, M., & Renner, R. (2012). “Reliable Quantum State Tomography.” *Physical Review Letters*, 109, 120403. [doi:10.1103/PhysRevLett.109.120403](https://doi.org/10.1103/PhysRevLett.109.120403)
4. Renner, R. (2007). “Symmetry of Large Physical Systems Implies Independence of Subsystems.” *Nature Physics*, 3, 645–649. [doi:10.1038/nphys684](https://doi.org/10.1038/nphys684)
5. Christandl, M., König, R., & Renner, R. (2009). “Postselection Technique for Quantum Channels with Applications to Quantum Cryptography.” *Physical Review Letters*, 102, 020504. [doi:10.1103/PhysRevLett.102.020504](https://doi.org/10.1103/PhysRevLett.102.020504)
6. Gross, D., Liu, Y.-K., Flammia, S. T., Becker, S., & Eisert, J. (2010). “Quantum State Tomography via Compressed Sensing.” *Physical Review Letters*, 105, 150401. [doi:10.1103/PhysRevLett.105.150401](https://doi.org/10.1103/PhysRevLett.105.150401)
7. Huang, H.-Y., Kueng, R., & Preskill, J. (2020). “Predicting Many Properties of a Quantum System from Very Few Measurements.” *Nature Physics*, 16, 1050–1057. [doi:10.1038/s41567-020-0932-7](https://doi.org/10.1038/s41567-020-0932-7)
8. Haah, J., Harrow, A. W., Ji, Z., Wu, X., & Yu, N. (2017). “Sample-Optimal Tomography of Quantum States.” *IEEE Transactions on Information Theory*, 63, 5628–5641. [doi:10.1109/TIT.2017.2719044](https://doi.org/10.1109/TIT.2017.2719044)
9. Wang, J., Scholz, V. B., & Renner, R. (2019). “Confidence Polytopes in Quantum State Tomography.” *Physical Review Letters*, 122, 190401. [doi:10.1103/PhysRevLett.122.190401](https://doi.org/10.1103/PhysRevLett.122.190401)
10. Scholten, T. L., & Blume-Kohout, R. (2018). “Behavior of the Maximum Likelihood in Quantum State Tomography.” *New Journal of Physics*, 20, 023050. [doi:10.1088/1367-2630/aaa7e2](https://doi.org/10.1088/1367-2630/aaa7e2)
11. van Enk, S. J., & Blume-Kohout, R. (2013). “When Quantum Tomography Goes Wrong: Drift of Quantum Sources and Other Errors.” *New Journal of Physics*, 15, 025024. [doi:10.1088/1367-2630/15/2/025024](https://doi.org/10.1088/1367-2630/15/2/025024)
12. Gallego, R., Brunner, N., Hadley, C., & Acín, A. (2010). “Device-Independent Tests of Classical and Quantum Dimensions.” *Physical Review Letters*, 105, 230501. [doi:10.1103/PhysRevLett.105.230501](https://doi.org/10.1103/PhysRevLett.105.230501)
13. Wood, C. J., & Gambetta, J. M. (2018). “Quantification and Characterization of Leakage Errors.” *Physical Review A*, 97, 032306. [doi:10.1103/PhysRevA.97.032306](https://doi.org/10.1103/PhysRevA.97.032306)

### Calibration, SPAM, reference frames, and self-testing

14. D’Ariano, G. M., Maccone, L., & Lo Presti, P. (2004). “Quantum Calibration of Measurement Instrumentation.” *Physical Review Letters*, 93, 250407. [doi:10.1103/PhysRevLett.93.250407](https://doi.org/10.1103/PhysRevLett.93.250407)
15. Chuang, I. L., & Nielsen, M. A. (1997). “Prescription for Experimental Determination of the Dynamics of a Quantum Black Box.” *Journal of Modern Optics*, 44, 2455–2467. [doi:10.1080/09500349708231894](https://doi.org/10.1080/09500349708231894)
16. D’Ariano, G. M., & Lo Presti, P. (2001). “Quantum Tomography for Measuring Experimentally the Matrix Elements of an Arbitrary Quantum Operation.” *Physical Review Letters*, 86, 4195–4198. [doi:10.1103/PhysRevLett.86.4195](https://doi.org/10.1103/PhysRevLett.86.4195)
17. Merkel, S. T., et al. (2013). “Self-Consistent Quantum Process Tomography.” *Physical Review A*, 87, 062119. [doi:10.1103/PhysRevA.87.062119](https://doi.org/10.1103/PhysRevA.87.062119)
18. Blume-Kohout, R., et al. (2017). “Demonstration of Qubit Operations below a Rigorous Fault Tolerance Threshold with Gate Set Tomography.” *Nature Communications*, 8, 14485. [doi:10.1038/ncomms14485](https://doi.org/10.1038/ncomms14485)
19. Nielsen, E., Gamble, J. K., Rudinger, K., Scholten, T., Young, K., & Blume-Kohout, R. (2021). “Gate Set Tomography.” *Quantum*, 5, 557. [doi:10.22331/q-2021-10-05-557](https://doi.org/10.22331/q-2021-10-05-557)
20. Di Matteo, O., et al. (2020). “Operational, Gauge-Free Quantum Tomography.” *Quantum*, 4, 364. [doi:10.22331/q-2020-11-17-364](https://doi.org/10.22331/q-2020-11-17-364)
21. Bartlett, S. D., Rudolph, T., & Spekkens, R. W. (2007). “Reference Frames, Superselection Rules, and Quantum Information.” *Reviews of Modern Physics*, 79, 555–609. [doi:10.1103/RevModPhys.79.555](https://doi.org/10.1103/RevModPhys.79.555)
22. Šupić, I., & Bowles, J. (2020). “Self-Testing of Quantum Systems: A Review.” *Quantum*, 4, 337. [doi:10.22331/q-2020-09-30-337](https://doi.org/10.22331/q-2020-09-30-337)

### State discrimination and quantum resources

<a id="ref-helstrom"></a>

23. Helstrom, C. W. (1976). *Quantum Detection and Estimation Theory*. Academic Press.
24. Chefles, A. (2000). “Quantum State Discrimination.” *Contemporary Physics*, 41, 401–424. [doi:10.1080/00107510010002599](https://doi.org/10.1080/00107510010002599)
25. Audenaert, K. M. R., et al. (2007). “Discriminating States: The Quantum Chernoff Bound.” *Physical Review Letters*, 98, 160501. [doi:10.1103/PhysRevLett.98.160501](https://doi.org/10.1103/PhysRevLett.98.160501)
26. Massar, S., & Popescu, S. (1995). “Optimal Extraction of Information from Finite Quantum Ensembles.” *Physical Review Letters*, 74, 1259–1263. [doi:10.1103/PhysRevLett.74.1259](https://doi.org/10.1103/PhysRevLett.74.1259)
27. Wootters, W. K., & Zurek, W. H. (1982). “A Single Quantum Cannot Be Cloned.” *Nature*, 299, 802–803. [doi:10.1038/299802a0](https://doi.org/10.1038/299802a0)
28. Barnum, H., Caves, C. M., Fuchs, C. A., Jozsa, R., & Schumacher, B. (1996). “Noncommuting Mixed States Cannot Be Broadcast.” *Physical Review Letters*, 76, 2818–2821. [doi:10.1103/PhysRevLett.76.2818](https://doi.org/10.1103/PhysRevLett.76.2818)
29. Heinosaari, T. (2016). “Simultaneous Measurement of Two Quantum Observables: Compatibility, Broadcasting, and In-Between.” *Physical Review A*, 93, 042118. [doi:10.1103/PhysRevA.93.042118](https://doi.org/10.1103/PhysRevA.93.042118)

### Bell nonlocality, causal structure, and experimental methodology

30. Bell, J. S. (1964). “On the Einstein Podolsky Rosen Paradox.” *Physics Physique Fizika*, 1, 195–200. [doi:10.1103/PhysicsPhysiqueFizika.1.195](https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195)
31. Bell, J. S. (1990). “La nouvelle cuisine.” In A. Sarlemijn & P. Kroes (Eds.), *Between Science and Technology*. Elsevier; reprinted in *Speakable and Unspeakable in Quantum Mechanics*. [doi:10.1017/CBO9780511815676.026](https://doi.org/10.1017/CBO9780511815676.026)
32. Jarrett, J. P. (1984). “On the Physical Significance of the Locality Conditions in the Bell Arguments.” *Noûs*, 18, 569–589. [doi:10.2307/2214878](https://doi.org/10.2307/2214878)
33. Brunner, N., Cavalcanti, D., Pironio, S., Scarani, V., & Wehner, S. (2014). “Bell Nonlocality.” *Reviews of Modern Physics*, 86, 419–478. [doi:10.1103/RevModPhys.86.419](https://doi.org/10.1103/RevModPhys.86.419)
34. Larsson, J.-Å. (2014). “Loopholes in Bell Inequality Tests of Local Realism.” *Journal of Physics A*, 47, 424003. [doi:10.1088/1751-8113/47/42/424003](https://doi.org/10.1088/1751-8113/47/42/424003)
35. Barrett, J., Collins, D., Hardy, L., Kent, A., & Popescu, S. (2002). “Quantum Nonlocality, Bell Inequalities, and the Memory Loophole.” *Physical Review A*, 66, 042111. [doi:10.1103/PhysRevA.66.042111](https://doi.org/10.1103/PhysRevA.66.042111)
36. Larsson, J.-Å., & Gill, R. D. (2004). “Bell’s Inequality and the Coincidence-Time Loophole.” *Europhysics Letters*, 67, 707–713. [doi:10.1209/epl/i2004-10124-7](https://doi.org/10.1209/epl/i2004-10124-7)
37. Kofler, J., et al. (2016). “Requirements for a Loophole-Free Photonic Bell Test Using Imperfect Setting Generators.” *Physical Review A*, 93, 032115. [doi:10.1103/PhysRevA.93.032115](https://doi.org/10.1103/PhysRevA.93.032115)
38. Hensen, B., et al. (2015). “Loophole-Free Bell Inequality Violation Using Electron Spins Separated by 1.3 Kilometres.” *Nature*, 526, 682–686. [doi:10.1038/nature15759](https://doi.org/10.1038/nature15759)
39. Giustina, M., et al. (2015). “Significant-Loophole-Free Test of Bell’s Theorem with Entangled Photons.” *Physical Review Letters*, 115, 250401. [doi:10.1103/PhysRevLett.115.250401](https://doi.org/10.1103/PhysRevLett.115.250401)
40. Shalm, L. K., et al. (2015). “Strong Loophole-Free Test of Local Realism.” *Physical Review Letters*, 115, 250402. [doi:10.1103/PhysRevLett.115.250402](https://doi.org/10.1103/PhysRevLett.115.250402)
41. Handsteiner, J., et al. (2017). “Cosmic Bell Test: Measurement Settings from Milky Way Stars.” *Physical Review Letters*, 118, 060401. [doi:10.1103/PhysRevLett.118.060401](https://doi.org/10.1103/PhysRevLett.118.060401)
42. Hall, M. J. W. (2010). “Local Deterministic Model of Singlet State Correlations Based on Relaxing Measurement Independence.” *Physical Review Letters*, 105, 250404. [doi:10.1103/PhysRevLett.105.250404](https://doi.org/10.1103/PhysRevLett.105.250404)
43. Wood, C. J., & Spekkens, R. W. (2015). “The Lesson of Causal Discovery Algorithms for Quantum Correlations: Causal Explanations of Bell-Inequality Violations Require Fine-Tuning.” *New Journal of Physics*, 17, 033002. [doi:10.1088/1367-2630/17/3/033002](https://doi.org/10.1088/1367-2630/17/3/033002)
44. Allen, J.-M. A., Barrett, J., Horsman, D. C., Lee, C. M., & Spekkens, R. W. (2017). “Quantum Common Causes and Quantum Causal Models.” *Physical Review X*, 7, 031021. [doi:10.1103/PhysRevX.7.031021](https://doi.org/10.1103/PhysRevX.7.031021)

Supplementary historical source: Shimony, A. (1986). “Events and Processes in the Quantum World.” In R. Penrose & C. J. Isham (Eds.), *Quantum Concepts in Space and Time*. Oxford University Press.

### Contextuality and ontological models

45. Kochen, S., & Specker, E. P. (1967). “The Problem of Hidden Variables in Quantum Mechanics.” *Journal of Mathematics and Mechanics*, 17, 59–87. [doi:10.1512/iumj.1968.17.17004](https://doi.org/10.1512/iumj.1968.17.17004)
46. Spekkens, R. W. (2005). “Contextuality for Preparations, Transformations, and Unsharp Measurements.” *Physical Review A*, 71, 052108. [doi:10.1103/PhysRevA.71.052108](https://doi.org/10.1103/PhysRevA.71.052108)
47. Budroni, C., Cabello, A., Gühne, O., Kleinmann, M., & Larsson, J.-Å. (2022). “Kochen–Specker Contextuality.” *Reviews of Modern Physics*, 94, 045007. [doi:10.1103/RevModPhys.94.045007](https://doi.org/10.1103/RevModPhys.94.045007)
48. Harrigan, N., & Spekkens, R. W. (2010). “Einstein, Incompleteness, and the Epistemic View of Quantum States.” *Foundations of Physics*, 40, 125–157. [doi:10.1007/s10701-009-9347-0](https://doi.org/10.1007/s10701-009-9347-0)
49. Pusey, M. F., Barrett, J., & Rudolph, T. (2012). “On the Reality of the Quantum State.” *Nature Physics*, 8, 475–478. [doi:10.1038/nphys2309](https://doi.org/10.1038/nphys2309)
50. Klyachko, A. A., Can, M. A., Binicioğlu, S., & Shumovsky, A. S. (2008). “Simple Test for Hidden Variables in Spin-1 Systems.” *Physical Review Letters*, 101, 020403. [doi:10.1103/PhysRevLett.101.020403](https://doi.org/10.1103/PhysRevLett.101.020403)

### Interpretations and empirically modified theories

51. Bohr, N. (1928). “The Quantum Postulate and the Recent Development of Atomic Theory.” *Nature*, 121, 580–590. [doi:10.1038/121580a0](https://doi.org/10.1038/121580a0)
52. Everett, H. III. (1957). “‘Relative State’ Formulation of Quantum Mechanics.” *Reviews of Modern Physics*, 29, 454–462. [doi:10.1103/RevModPhys.29.454](https://doi.org/10.1103/RevModPhys.29.454)
53. Bohm, D. (1952). “A Suggested Interpretation of the Quantum Theory in Terms of ‘Hidden’ Variables. I.” *Physical Review*, 85, 166–179. [doi:10.1103/PhysRev.85.166](https://doi.org/10.1103/PhysRev.85.166)
54. Bohm, D. (1952). “A Suggested Interpretation of the Quantum Theory in Terms of ‘Hidden’ Variables. II.” *Physical Review*, 85, 180–193. [doi:10.1103/PhysRev.85.180](https://doi.org/10.1103/PhysRev.85.180)
55. Dürr, D., Goldstein, S., & Zanghì, N. (1992). “Quantum Equilibrium and the Origin of Absolute Uncertainty.” *Journal of Statistical Physics*, 67, 843–907. [doi:10.1007/BF01049004](https://doi.org/10.1007/BF01049004)
56. Ghirardi, G. C., Rimini, A., & Weber, T. (1986). “Unified Dynamics for Microscopic and Macroscopic Systems.” *Physical Review D*, 34, 470–491. [doi:10.1103/PhysRevD.34.470](https://doi.org/10.1103/PhysRevD.34.470)
57. Bassi, A., Lochan, K., Satin, S., Singh, T. P., & Ulbricht, H. (2013). “Models of Wave-Function Collapse, Underlying Theories, and Experimental Tests.” *Reviews of Modern Physics*, 85, 471–527. [doi:10.1103/RevModPhys.85.471](https://doi.org/10.1103/RevModPhys.85.471)
58. Carlesso, M., et al. (2022). “Present Status and Future Challenges of Non-Interferometric Tests of Collapse Models.” *Nature Physics*, 18, 243–250. [doi:10.1038/s41567-021-01489-5](https://doi.org/10.1038/s41567-021-01489-5)
59. Fuchs, C. A., Mermin, N. D., & Schack, R. (2014). “An Introduction to QBism with an Application to the Locality of Quantum Mechanics.” *American Journal of Physics*, 82, 749–754. [doi:10.1119/1.4874855](https://doi.org/10.1119/1.4874855)
60. Rovelli, C. (1996). “Relational Quantum Mechanics.” *International Journal of Theoretical Physics*, 35, 1637–1678. [doi:10.1007/BF02302261](https://doi.org/10.1007/BF02302261)
61. Faye, J. “Copenhagen Interpretation of Quantum Mechanics.” *Stanford Encyclopedia of Philosophy* (living entry). [SEP entry](https://plato.stanford.edu/entries/qm-copenhagen/)

### Philosophy, statistics, and methodology

62. Stanford, K. “Underdetermination of Scientific Theory.” *Stanford Encyclopedia of Philosophy* (living entry). [SEP entry](https://plato.stanford.edu/entries/scientific-underdetermination/)
63. van Fraassen, B. C. (1980). *The Scientific Image*. Oxford University Press. [doi:10.1093/0198244274.001.0001](https://doi.org/10.1093/0198244274.001.0001)
64. Stanford, P. K. (2006). *Exceeding Our Grasp: Science, History, and the Problem of Unconceived Alternatives*. Oxford University Press. [Publisher page](https://global.oup.com/academic/product/exceeding-our-grasp-9780195174080)
65. Suppes, P. (1962). “Models of Data.” In E. Nagel, P. Suppes, & A. Tarski (Eds.), *Logic, Methodology and Philosophy of Science*, pp. 252–261. [Reprint](https://errorstatistics.files.wordpress.com/2016/12/suppes-p-1962-models-of-data.pdf)
66. Bogen, J., & Woodward, J. (1988). “Saving the Phenomena.” *The Philosophical Review*, 97, 303–352. [doi:10.2307/2185445](https://doi.org/10.2307/2185445)
67. Collins, H. M. (1985/1992). *Changing Order: Replication and Induction in Scientific Practice*. University of Chicago Press.
68. Franklin, A., & Perovic, S. (2023). “Experiment in Physics.” *Stanford Encyclopedia of Philosophy*. [SEP entry](https://plato.stanford.edu/entries/physics-experiment/)
69. Hacking, I. (1983). *Representing and Intervening*. Cambridge University Press. [doi:10.1017/CBO9780511814563](https://doi.org/10.1017/CBO9780511814563)
70. Woodward, J. (2003). *Making Things Happen: A Theory of Causal Explanation*. Oxford University Press. [doi:10.1093/0195155270.001.0001](https://doi.org/10.1093/0195155270.001.0001)
71. Mayo, D. G. (2018). *Statistical Inference as Severe Testing*. Cambridge University Press. [doi:10.1017/9781107286184](https://doi.org/10.1017/9781107286184)
72. Manski, C. F. (2003). *Partial Identification of Probability Distributions*. Springer. [doi:10.1007/b97478](https://doi.org/10.1007/b97478)
73. White, H. (1982). “Maximum Likelihood Estimation of Misspecified Models.” *Econometrica*, 50, 1–25. [doi:10.2307/1912526](https://doi.org/10.2307/1912526)
74. Shpitser, I., & Pearl, J. (2006). “Identification of Joint Interventional Distributions in Recursive Semi-Markovian Causal Models.” *AAAI Proceedings*. [ACM record](https://dl.acm.org/doi/10.5555/1597538.1597540)
75. Joint Committee for Guides in Metrology. (2012). *International Vocabulary of Metrology — Basic and General Concepts and Associated Terms*, 3rd ed. (JCGM 200:2012). [doi:10.59161/JCGM200-2012](https://doi.org/10.59161/JCGM200-2012)
76. Joint Committee for Guides in Metrology. (2008). *Evaluation of Measurement Data — Guide to the Expression of Uncertainty in Measurement* (JCGM 100:2008). [doi:10.59161/JCGM100-2008E](https://doi.org/10.59161/JCGM100-2008E)

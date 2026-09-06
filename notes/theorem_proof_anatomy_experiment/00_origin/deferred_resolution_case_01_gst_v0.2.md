# GST Case 01

## Conditional Inference, Quotient Identifiability, and Model-Scope Revision

### A Negative Test of the Deferred-Resolution Hypothesis

**Version:** v0.2  
**Status:** Frozen negative result  
**Date:** 2026-08-16  
**Parent note:** [deferred_resolution_case_01_gst.md](./deferred_resolution_case_01_gst.md)  
**Audit inputs:** [Claude Code review](./deferred_resolution_case_01_gst_adversarial_review_claudecode.md); [Codex review](./deferred_resolution_case_01_gst_adversarial_review_codex.md); [v0.3 working note](./tool_truth_absence_working_note_v0.3.md); [quantum prior-art reconstruction](./quantum_identifiability_prior_art_network.md)  
**Epistemic posture:** field-native reconstruction first; no claim of a new mechanism

> **GST系列は、仮説した反復的なDeferred Resolution連鎖を支持しなかった。**

標準的 quantum process tomography（QPT）から self-consistent tomography、Gate Set Tomography（GST）、gauge-free / operational formulations、さらに non-Markovian characterization へ至る文献を再監査した結果、この系列を一つの反復機構としてまとめる必要はなかった。技術内容は、conditional inverse problem、reference / nuisance uncertainty、joint estimation、identifiability modulo gauge、quotient parameterization、model checking、model-specific extension という既存語彙で、より正確に再構成できる。

残る有用な結果は肯定的な新概念ではなく、区別の保存である。外見上似た「残余」は一種類ではない。あるものは条件付き推論の model assumption、あるものは observational equivalence による quotient structure、あるものは gauge-sensitive reporting の convention、別のものは独立した model-adequacy failure である。

---

## 1. Changes from v0.1

### 1.1 Downgraded or withdrawn

- ケース全体を支持結果とした旧判定を撤回した。
- Deferred Resolution を独立した機構名から、今回棄却された historical working hypothesis へ降格した。
- frequency、recurrence、formal invariance、diagnostic effect、modal impossibility を一列に並べた旧五段階 taxonomy を削除した。
- 「保証境界の移送」を A→B/C の第一記述とすることを撤回した。
- operational success と存在論的な一意性の完結を対比した旧主張を削除した。このケースが直接扱う model adequacy、representational uniqueness と、直接扱わない interpretive uniqueness を分離した。
- assurance-provenance table は、このケースでは独立した診断を生まなかったため本文の中心から削除した。

### 1.2 Rewritten in field-native terms

- standard QPT → self-consistent QPT/GST は、同一の境界が移る過程ではなく、**reference / nuisance parameters の joint estimation**、または **weaker reference assumptions の下での estimand expansion** と記述する。
- gauge freedom は、observational non-identifiability、representational redundancy、宣言された experiment algebra に相対的な operational indistinguishability、decision-relevant reporting choice、model misspecification に分解する。
- quotient-level identifiability と、gauge-sensitive quantities を報告・比較するときの representative choice を分離する。
- non-Markovianity、drift、leakage、crosstalk、context dependence、memory は直列の最終段階ではなく、固定 Markovian gate-set model から分岐する model-specific extensions として扱う。

### 1.3 Added

- Box、Cox–Reid、Ljung、Gelman–Shalizi に接続する ordinary model-building / model-criticism / nuisance-parameter prior art。
- field-native 語彙だけで書き直す Erasure Test の正式な negative result。
- cross-cutting failure modes に対する primary detection responsibility。
- Li et al. (2024) の一次資料に基づく書誌訂正。
- Merkel et al. (2013) の固定 initial state / measurement と、同論文に成熟した GST の gauge 語彙が明示されているかを分けた一次資料確認。
- ケースを negative baseline として維持する freeze rule。

### 1.4 Preserved

- standard tomography の calibration dependence。
- self-consistent estimation が systematic gate-generated SPAM の誤帰属を減らすこと。
- GST の operational probabilities が gauge orbit 上で不変であること。
- quotient target と gauge optimization / reporting practice の区別。
- fixed Markovian gate-set model に対する model checking と、範囲外に対する extensions の必要。
- 技術進歩を failure、infinite regress、または ontological impossibility と読まない規律。

---

## 2. Purpose and non-goals

本ケースの目的は、次の作業仮説を反証可能に検査することだった。

    local resolution
        ↓
    residual assurance boundary
        ↓
    target reformulation
        ↓
    new adequacy boundary

v0.1 はこの図を弱い意味で支持した。しかし両査読と一次資料の再検証を経ると、同じ技術史はより少ない追加語彙で再構成できた。したがって v0.2 は、この図を科学史・方法論上の一般機構として採用しない。

本稿は以下を主張しない。

- GST が不完全または失敗した方法である。
- calibration dependence や gauge freedom が新発見である。
- gauge freedom が存在論的不確定性を証明する。
- model checking と model extension が無限後退を作る。
- 科学が真理に到達できない。
- operational success と interpretation が無関係である。
- 今回の negative result が、他分野における同種仮説を自動的に棄却する。

このケースが問うのは限定的に、**GST lineage に独立の Deferred Resolution mechanism を置かなければ失われる技術的・診断的内容があるか**である。答えは現時点で否定的である。

---

## 3. Evaluation rule

### 3.1 Positive判定に必要だったもの

独立概念を残すには、少なくとも次が必要だった。

1. 前段の解決と後段の問題の間に、単なる時系列ではない強い dependency がある。
2. 同じ種類の dependency が複数回反復する。
3. field-native vocabulary だけでは見落とされる failure path、scope error、または design decision が得られる。
4. 単なる model refinement、quotienting、model checking、scope extension より説明力が高い。

### 3.2 Negative判定

以下が成立するなら仮説を棄却する。

- 技術的結論が field-native terminology だけで完全に再構成できる。
- purported chain が複数の独立 branch を後から直列化したものにすぎない。
- gauge は quotient によって identifiable target が明確になる一方、後続の model adequacy は別問題である。
- 追加ラベルが図示・索引以上の診断効果を示さない。

今回はこちらに該当した。

---

## 4. Prior-art baseline: ordinary model construction and inference

GST に固有でない一般形は、既存のモデル構築・統計推論の語彙でかなり説明できる。

### 4.1 Iterative model building and criticism

Box は、モデル構築を仮定、演繹、データとの照合、批判、改訂からなる反復過程として論じた（[Box 1976](https://doi.org/10.1080/01621459.1976.10480949)）。Gelman and Shalizi は Bayesian workflow においても model checking と model expansion を推論の外側ではなく中心的実践として扱う（[Gelman & Shalizi 2013](https://doi.org/10.1111/j.2044-8317.2011.02037.x)）。

この観点から見ると、fixed Markovian model の適合度を検査し、drift、memory、crosstalk などに応じて model class を変えることは、特殊な「解決の先送り」ではない。標準的な model criticism → structure revision である。

### 4.2 Nuisance / reference parameters

統計学では、target parameter 以外の未知量を nuisance parameter として扱い、conditioning、profiling、marginalization、orthogonalization、joint estimation などで処理する長い伝統がある（例：[Cox & Reid 1987](https://doi.org/10.1111/j.2517-6161.1987.tb01422.x)）。

SPAM を固定基準として条件づける方法から、SPAM と gates を共同推定する方法への変化は、この一般的な問題族に近い。ただし「nuisance-parameter promotion」は本稿の記述的索引であり、GST 文献が一貫して用いる正式名称ではない。

### 4.3 System identification

Ljung の system identification は、experiment / input design、model-structure choice、identifiability と estimation、validation、必要に応じた structure revision を一つの標準的 workflow に置く（[Ljung 1999](https://rt.isy.liu.se/en/books/sysid/)）。GST は量子操作に固有の gauge、circuit design、physical constraints を持つが、conditional model → estimation → validation → revision という一般構図自体は新しくない。

これらの prior art は GST の詳細を置換しない。しかし本ケースの「一般形」が独自機構であるという読みを弱める。

---

## 5. Historical sequence

時系列は論理的な単線を意味しない。

| Year | Work | Field-native contribution | Relation to this case |
|---:|---|---|---|
| 1997 | Chuang & Nielsen | ancilla-assisted quantum process tomography | known preparation / measurement model の下で process を復元 |
| 2001–2004 | D’Ariano and collaborators | detector, process, calibration relations | unknown target と trusted reference の相補性を明示 |
| 2013 | Merkel et al. | self-consistent QPT | faulty gate-generated SPAM を joint gate estimation に含める |
| 2013 | van Enk & Blume-Kohout | “better tomography” | state–measurement joint uncertainty と gauge-like non-identifiability |
| 2017 | Blume-Kohout et al. | robust self-consistent tomography / GST | gate set、circuit design、gauge、goodness-of-fit |
| 2018 | Pollock et al. | process-tensor framework | multitime / non-Markovian process の一般的 operational framework |
| 2020 | Di Matteo et al. | operational, gauge-free tomography | observable quantities を parameter とする target reformulation |
| 2021 | Nielsen et al. | GST review | gauge、gauge optimization、model testing、実務を体系化 |
| 2021 | Rudinger et al. | simultaneous GST | crosstalk / simultaneous-operation characterization |
| 2022 | White et al. | non-Markovian process tomography | finite time-window の process tensor 推定 |
| 2024 | Li et al. | instrument-set tomography | system–environment correlations を含む gate characterization |

Process-tensor framework が operational gauge-free tomography より先行することは、旧稿の A→B→C→D→E という直線が歴史的事実ではなく、reviewer-generated ordering だったことの強い反証である。

---

## 6. Stage A — Standard tomography and QPT

### Problem

指定された state、POVM、channel / process のパラメータを、既知の実験操作と観測頻度から推定する。

### Target

- state tomography: \(\rho\)
- detector tomography: \(\{E_y\}\)
- process tomography: channel \(\mathcal E\) またはその Choi representation

### Backgrounded or fixed inputs

通常の定式化では target に応じて別側の reference が既知である。

- state tomography は measurement model を条件とする。
- detector tomography は probe states を条件とする。
- standard QPT は input states と output measurements、したがって SPAM characterization を条件とする。

informational completeness、Hilbert-space dimension、repeatability / preparation model、likelihood model も target の可識別性・推定可能性に関与する。

### What is resolved

指定 model class と trusted-reference assumptions の下で、informationally complete design は state / detector / process の within-model identifiability を与えうる。有限標本では estimator、confidence region、bias、conditioning を別途評価する。

### What remains

これは unconditional characterization ではない。reference model の systematic error は target estimate に伝播しうる。oversampling は sampling error を減らしても、reference miscalibration による bias を一般には除去しない。

### Status in this case

これは calibration-conditioned inverse problem である。「保証境界の移送」を要請しない。

---

## 7. Stage B — Self-consistent process tomography

### Problem

Merkel et al. は、input preparation と measurement rotations を生成する gates に coherent systematic errors があると、standard QPT がその誤差を test target に誤帰属しうると指摘した。単なる repeated sampling ではこの bias は消えない（[Merkel et al. 2013](https://doi.org/10.1103/PhysRevA.87.062119)）。

### Target

個別 gate だけでなく、state preparation と measurement を生成する library of operations を相互整合的に推定する。

### Primary-source verification

同論文は fixed initial state \(\rho_0\) と measurement operator \(M_0\) を置き、その上で gates を共同推定する。結論部では \(\rho_0\) / \(M_0\) の誤差と slowly time-varying errors を将来拡張として明示している。

全文確認では、後の GST review で標準化された “gauge” または “similarity transform” という語による独立節は確認できなかった。この事実は、数学的な observational invariance が存在しなかったことを意味しない。2013 年論文に後世の成熟した GST 語彙を遡及投影せず、同時に「gauge が後から発見された」という歴史的主張にも使わない。

### Resolution mechanism

    standard QPT:
    gate-generated SPAM = characterized / conditioned input

    self-consistent QPT:
    gate-generated SPAM = jointly estimated

より弱い reference assumptions の下で、unknown parameter block を拡張して joint fit を行う。

### What is genuinely resolved

gate-generated SPAM errors を target gate に一方的に帰属する特定の systematic error mechanism が、joint inference によって減少または可視化される。

### Residual

- base \(\rho_0\) / \(M_0\) への依存
- parameterization の observational redundancy
- time variation や richer context dependence
- finite-data optimization と conditioning

### Case judgment

ここで起きたことは **nuisance/reference parameter promotion** または **joint estimation under weaker reference assumptions** と呼ぶのが最も正確である。「同じ assurance boundary が別層へ移った」という主張は不要であり、同一性基準も示されていない。

---

## 8. Stage C — Gate Set Tomography

### Problem and target

GST は state preparation、gate operations、measurement を含む gate set 全体を、長い gate sequences の outcome probabilities から self-consistently estimate する。fiducials は effective preparations / measurements を生成し、germs と sequence lengths は error generators を増幅して可識別性と精度を高める。

### Backgrounded model

典型的な long-sequence GST は、指定 Hilbert-space dimension、固定された circuit alphabet、time-independent / Markovian gate set、shot model などを採る。これらは GST の欠陥ではなく、何を推定するかを定義する model scope である。

### What is resolved

- unknown operations の self-consistent joint estimation
- gate-generated SPAM error の explicit treatment
- circuits の設計による感度増幅
- likelihood / goodness-of-fit による model violation diagnostics
- identifiable combinations と gauge directions の分離

### Gauge orbit

gate-set representation に similarity-type transformation を施しても、宣言された circuit experiment algebra 上の全 outcome probabilities が変わらないことがある。したがってデータが識別するのは任意の matrix representative ではなく、operationally indistinguishable representations の orbit / quotient である。

これは、calibration error や model misspecification と同じ問題ではない。

### Model checking

GST の goodness-of-fit は、fixed Markovian gate-set model がデータを十分説明するかを検査する。fit failure は原因を一意に同定しないが、stationarity、Markovianity、dimension、crosstalk などの追加診断へ進む根拠になる。これは diagnostic resolution であって、全 failure mode の除去ではない。

### Case judgment

GST は conditional model の下で joint estimation、quotient identifiability、model checking を結合する成熟した方法である。これらを一つの新しい “deferred” mechanism と読み替える必要はない。

---

## 9. Stage D — Operational and gauge-free formulations

### 9.1 Identifiability layer

Di Matteo et al. は、gauge-dependent matrix representatives ではなく、実験的に observable な quantities を parameter とする operational formulation を与える（[Di Matteo et al. 2020](https://doi.org/10.22331/q-2020-11-17-364)）。

この層では、overparameterized representation の一意性を要求する問題を捨て、宣言された experiment algebra が識別する quotient / operational coordinates を target とする。representational redundancy は identifiable quotient の水準で閉じる。これは **quotient resolution** または **target reparameterization** であり、未解決の物理的曖昧性を自動的に意味しない。

### 9.2 Reporting and decision layer

quotient-level identifiability が閉じても、実務上の報告がすべて自動的に一意になるわけではない。

- 一般の非 unitary gauge transformation は complete positivity を保存しない場合がある。
- fidelity、diamond distance、entropy など、実務上用いられる一部の quantities は gauge-variant である。
- target comparison や、gauge-sensitive metric を用いる threshold report では representative / optimization convention が結論の表現に影響しうる。

したがって安全な要約は次である。

> Gauge freedom is resolved at the level of identifiable quotient structure, but operational reporting may still require a representative or a convention for gauge-sensitive metrics.

ここで残るのは存在論問題でも、Deferred Resolution の証拠でもない。decision-relevant gauge choice と reporting practice の問題である。

---

## 10. Gauge distinctions after revision

旧稿の無限定な equivalence label は、宣言された interface 外を含む存在論的同一性まで示唆しうるため削除する。代わりに次を区別する。

| Distinction | Meaning in this case | Proper treatment |
|---|---|---|
| Observational non-identifiability | 許容 circuits の全確率が同じで representative を分離できない | identifiable object を orbit / quotient として特定 |
| Representational redundancy | 複数の matrix descriptions が同じ observable predictions を表す | gauge-invariant parameterization または gauge fixing |
| Operational indistinguishability under the declared experiment algebra | 宣言された preparation / gate / measurement compositions では区別不能 | interface と experiment algebra を明記 |
| Decision-relevant gauge choice / reporting representative | gauge-sensitive metric や target comparison に representative が必要 | optimization rule、metric、reference を報告 |
| Model misspecification | データ生成過程が採用 gate-set model の外にある | goodness-of-fit、residual diagnostics、model revision |

第三項は interface-relative である。これを、あらゆる物理的介入の下での同一性へ拡張しない。

---

## 11. Related model extensions beyond fixed Markovian gate-set assumptions

以下は operational gauge-free tomography の「次段階」ではない。固定 Markovian gate-set model の異なる scope limitations に応答する並列 branch である。

### 11.1 Drift and time dependence

stationarity を外し、time-tagged residuals、sliding-window estimates、change-point / drift models などで時間変化を扱う。drift は preparation identity、gate stability、calibration transfer、finite-sample model を横断して影響する。

### 11.2 Leakage and dimension mismatch

computational subspace 外への population transfer や assumed dimension の誤りを、leakage-sensitive sequences、population measurements、拡張 Hilbert-space model で扱う（例：[Wood & Gambetta 2018](https://doi.org/10.1103/PhysRevA.97.032306)）。

### 11.3 Crosstalk and simultaneous operations

gate が他 qubit / operation context に依存する場合、single-device gate set では足りない。simultaneous GST などは並列実行時の context-dependent operations を target に含める（[Rudinger et al. 2021](https://doi.org/10.1103/PRXQuantum.2.040338)）。

### 11.4 Memory and multitime processes

process tensor は multitime quantum process を operationally characterize する一般枠組みを与える（[Pollock et al. 2018](https://doi.org/10.1103/PhysRevA.97.012127)）。finite time-window の process-tensor tomography（[White et al. 2022](https://doi.org/10.1103/PRXQuantum.3.020344)）や、system–environment correlations を含む instrument-set tomography（[Li et al. 2024](https://doi.org/10.1088/2058-9565/ad3d80)）は、別の target と resource requirements を持つ。

### 11.5 Context dependence and control nonlinearity

operation label の意味が surrounding circuit、amplitude、history、concurrency に依存するなら、その dependence を covariate、context-indexed operation、または richer dynamical model として foreground に置く必要がある。

### Branch judgment

これらは gauge problem の続きではない。GST が明示した model scope の外側を扱う model checking / model extension の問題である。一部は GST development と相互に影響するが、一つの歴史的・論理的 chain を構成しない。

---

## 12. Field-native reconstruction

Deferred Resolution と boundary relocation という語を使わずに、ケース全体を次のように再構成できる。

    Standard QPT
      conditional inference with characterized SPAM
                |
                | systematic gate-generated SPAM bias
                v
    Self-consistent QPT / GST
      enlarged joint estimand under weaker reference assumptions
      + circuit design
      + likelihood estimation
                |
                +---- observational symmetry ----> quotient identifiability
                |                                  + gauge/reporting conventions
                |
                +---- goodness-of-fit ------------> model validation
                                                   |
                                                   +--> drift model
                                                   +--> leakage model
                                                   +--> crosstalk model
                                                   +--> multitime / memory model
                                                   +--> context-dependent model

この図には三つの異なる operation がある。

1. **Estimand expansion:** fixed reference の一部を joint unknown にする。
2. **Quotienting / reparameterization:** observable predictions が識別する対象へ target を修正する。
3. **Model checking and extension:** adopted scope がデータに合うかを検査し、必要なら別 class を使う。

これらは相互作用するが、同一の mechanism ではない。

---

## 13. Edge ledger

| From | To | Edge type | Evidence | Strength | Does it support a recurrent mechanism? |
|---|---|---|---|---|---|
| Characterized SPAM | Standard QPT estimate | calibration dependence / modeling assumption | standard tomography literature | strong | No |
| Gate-generated SPAM uncertainty | Self-consistent QPT | stated problem–solution relation | Merkel et al. 2013 | strong | Only a local relation |
| Self-consistent circuit probabilities | Gauge orbit | mathematical observational invariance | GST literature | strong | No; quotient structure |
| Gauge orbit | Operational coordinates | target reparameterization | Di Matteo et al. 2020 | strong | No; quotient resolution |
| Gauge orbit | Gauge-sensitive metric report | reporting / decision convention | Nielsen et al. 2021 | strong | No |
| Fixed Markovian GST | Goodness-of-fit result | statistical model checking | GST literature | strong | No |
| Failed Markovian fit | Particular extension | diagnosis plus model-selection judgment | extension-specific literature | medium; cause-dependent | No common next stage |
| Process tensor | Gauge-free tomography | historical sequence | dates only | none as logical edge | Contradicts the old linear story |

一つ目から四つ目までを時系列で並べても、同型の edge が反復しているわけではない。

---

## 14. Cross-cutting failure modes and detection responsibility

failure mode を一つの node に排他的に所属させない。ただし監査実務のため、first-line detection responsibility を明示できる。

| Failure mode | Cross-impact | Primary detection responsibility / responsible test | Notes |
|---|---|---|---|
| Drift / time dependence | preparation stationarity、gate identity、calibration transfer、likelihood assumptions | time-tagged residuals、windowed fits、change-point / sequence-order checks | 単一原因へ自動同定しない |
| Gate-generated SPAM uncertainty | process estimate、gate comparison、confidence coverage | self-consistent circuit fit、independent reference comparison | Stage B の中心問題 |
| Gauge-sensitive reporting | fidelity / distance / entropy report、target comparison | gauge-invariant report or declared gauge optimization / metric convention | model fit failureではない |
| Leakage / dimension error | trace within subspace、gate errors、state-preparation model | leakage-sensitive measurements、population diagnostics、dimension tests | scope violation |
| Crosstalk | simultaneous-gate behavior、local gate estimate、context transfer | simultaneous circuits / simultaneous GST | isolated-gate fitでは見えない場合 |
| Context dependence | fixed-label gate identity、transfer across circuits | context-stratified residual tests | causes can include crosstalk or control nonlinearities |
| Memory / system–environment correlation | iid / Markovian likelihood、sequence prediction、confidence statement | multitime correlation tests、process-tensor or instrument-set protocols | richer target and sample demands |

この “responsibility” は所有権ではない。どの検査が最初に異常を捉える責任を持つかを記すだけで、cross-impact を消さない。

---

## 15. What the quotient closes—and does not close

### 15.1 Closed at the identifiability layer

許容 experiment algebra 上の全 outcome probabilities が gauge-related representatives を分離しないなら、representative 自体を identifiable target とする問題は overparameterized である。orbit / quotient を target にすれば、その representational non-uniqueness は原理的な欠損ではなく正しい target specification に変わる。

### 15.2 Not automatically closed at the reporting layer

実験家が具体的な matrix、target gate、fidelity、diamond distance などを比較・報告する場合、選択した quantity が gauge-invariant か、どの gauge optimization / representative convention を使ったかが必要になる。これは quotient identifiability と矛盾しない。

### 15.3 Independent adequacy questions

Markovianity、stationarity、dimension、leakage、crosstalk、memory は、gauge orbit の quotienting では解決されない。しかしそれは gauge が「先送りされた」からではない。異なる model adequacy conditions だからである。

### 15.4 Interpretive uniqueness

GST の experiment statistics、gauge orbit、model checking は、それだけで量子形式体系の interpretive uniqueness を決めない。一方、このケースは interpretive non-uniqueness を証明もしない。ここで監査できるのは model adequacy と representational uniqueness までである。

---

## 16. Erasure Test

### 16.1 Pass 1: proprietary vocabulary removal

Deferred Resolution、boundary relocation、assurance provenance という固有語を削除した。

### 16.2 Pass 2: reconstruction

残った内容を次だけで再記述した。

- calibration-conditioned inverse problem
- reference / nuisance uncertainty
- joint estimation
- experiment design and informational amplification
- observational equivalence and gauge orbit
- quotient parameterization
- gauge optimization and gauge-sensitive reporting
- goodness-of-fit and model checking
- model misspecification
- model-specific extension

### 16.3 Result

技術的結論、scope 判断、実験的区別はすべて残った。さらに field-native reconstruction は、旧稿より次を明確にした。

- A→B/C は「境界の移動」より reference / nuisance parameter の joint estimation と記述する方が精密である。
- gauge quotient が閉じる identifiability problem と、gauge-sensitive reporting を分ける必要がある。
- non-Markovian extensions は operational gauge-free tomography の後続段階ではなく、異なる adequacy failures への branch である。
- process tensor の先行年代は、旧直線が歴史系列ですらないことを示す。

したがってこの Erasure Test は **negative result** である。固有語彙を消しても情報は失われず、少なくとも二箇所で記述精度が上がった。Deferred Resolution は、このケースでは methodological construct として独立しない。

---

## 17. Adopted null explanations

### Null A — Ordinary model refinement / model-building cycle

最も強い説明は次である。

    conditional model
        → reference uncertaintyをjoint estimandへ含める
        → identifiable quotientを定める
        → model fitを検査する
        → failureに応じたmodel classへ拡張する

これは inverse problems、nuisance-parameter inference、system identification、model criticism の通常の組合せである。

### Null E — Reviewer-generated linear narrative

旧稿の A→B→C→D→E は、異なる研究目的と年代を一つの story に並べた。とくに process-tensor work が operational gauge-free formulation より先行するため、Stage D が Stage E を生み出したという歴史的 inference は成立しない。論理的にも model-memory branch は gauge quotient から導かれない。

### Supporting null: quotient resolution

gauge に関しては quotient / operational target が representational identifiability を閉じる。後に残る reporting convention と adequacy questions は、閉じなかった同一問題ではない。

この三つの説明は、独立の Deferred Resolution mechanism より簡潔で、一次文献の語彙にも近い。

---

## 18. Claims after revision

### 18.1 Supported but standard

1. **Model-relative solutions retain scope assumptions.**  
   standard QPT、GST、process tensor のいずれも、定めた target、experiment algebra、dimension、temporal model、sampling conditions に相対して推論を行う。

2. **An identifiable target may be a quotient or equivalence class.**  
   GST の observable circuit probabilities が gauge-related representatives を分離しないとき、quotient-level target が適切である。

3. **Joint estimation can replace stronger reference assumptions.**  
   gate-generated SPAM を fixed input の一部として扱う代わりに、gate set の中で共同推定できる。

4. **Model checking can motivate, but does not uniquely select, a richer model.**  
   poor fit は scope revision の理由になりうるが、drift、memory、leakage 等を自動的に区別しない。

### 18.2 Unsupported by this case

- 反復する boundary-relocation mechanism。
- model refinement を横断する独立の Deferred Resolution 構造。
- representational gauge から解釈的一意性の不成立を導くこと。
- scientific progress が最終 closure を原理的に回避するという主張。
- Deferred Resolution の方法論的新規性または実験設計上の追加効果。

---

## 19. Assurance-provenance vocabulary in this case

v0.3 の assurance-provenance vocabulary を使えば、standard QPT は calibration-supported and model-relative、GST の gauge statement は theorem/model-supported、fit evaluation は statistically constrained、と索引できる。

しかし本ケースでは、その再分類は次のいずれも変更しなかった。

- target specification
- identifiable object
- responsible experiment
- model-checking decision
- extension choice

したがって詳細な provenance table は v0.2 から削除する。このケースに限っては、同表は indexing / pedagogy 以上の独立した diagnostic effect を示さなかった。これは v0.3 全体の語彙を棄却するものではなく、具体例に対する Erasure Test の結果である。

---

## 20. Implications for the v0.3 working note

このケース単独から v0.3 の中心構造を変更すべきではない。適切な影響は次に限られる。

- “resolution relocation” を open research hypothesis として採用しない。
- ordinary model refinement、quotient resolution、reporting choice、independent model adequacy を混同しない negative baseline として参照する。
- 将来の別ケースでは、field-native reconstruction 後にも残る recurrent dependency、formal invariance、または diagnostic effect を要求する。

したがって推奨は **No substantive revision** である。もし v0.3 に追記するなら、一段落の negative case report で十分である。

> GST Case 01では、仮説した反復的な resolution-relocation chain は支持されなかった。standard tomography、self-consistent estimation、gauge quotient、model checking、model extension の関係は既存語彙でより精密に再構成でき、共通語彙を消しても独立の診断結果は失われなかった。

---

## 21. Limitations and open technical checks

1. **Gauge-sensitive decision rules:** 特定の fault-tolerance or benchmarking threshold が gauge-variant estimate に依存する実例を、protocol-level で追加監査できる。
2. **Implicit invariance in Merkel et al.:** 2013 論文に成熟した gauge 語彙は明示されないが、parameter symmetry の数学的含意を後の形式と厳密に対応づける歴史的・技術的検討は別課題である。
3. **Instrument-set gauge:** system–environment models の identifiability、finite-memory assumptions、representation freedom を個別に監査する必要がある。
4. **Model-checking responsibility:** drift、memory、leakage、crosstalk を区別する診断力を、実データ protocol で比較する余地がある。
5. **Bibliographic completeness:** 本稿は representative primary sources と reviews を用いたケース監査であり、GST / system identification / statistical nuisance theory の網羅的 review ではない。

これらは Deferred Resolution の再生条件ではなく、技術的 precision の改善課題である。

---

## 22. Frozen negative result

このケースを **frozen negative result** とする。

- 新しい独立証拠がない限り、このケースから Deferred Resolution を支持する判定を再生しない。
- 今後の修正は technical correction、bibliography、primary-source provenance verification に限定する。
- 新しい supporting case は、本ケースの用語を流用するだけでなく、field-native Erasure Test 後にも残る dependency と diagnostic effect を示さなければならない。
- 他ケースは、この GST case を negative baseline として比較する。

---

## 23. Final verdict

> **GST Case 01 did not support a distinct Deferred Resolution mechanism. Its technical content is better described using established concepts: conditional inverse problems, nuisance/reference uncertainty, joint estimation, identifiability modulo gauge, quotient parameterization, model checking, and model-specific extension.**

有用な negative result は、似て見える「残る境界」が一つの現象ではないと確認したことである。model assumption、quotient structure、reporting choice、independent model-adequacy problem は、それぞれ別の処理を要する。

### Answers to the original questions

1. **GST 系列では問題が「解決されず残った」のか。**  
   一括した答えはない。standard QPT の特定の SPAM dependency は joint estimation によって扱い方が変わった。gauge redundancy は quotient target で閉じる。model violations は別の validation / extension problem である。

2. **Gauge freedom は未解決問題か。**  
   identifiable quotient の水準では representational redundancy が閉じる。gauge-sensitive reporting には representative / metric convention が残りうるが、これは同じ identifiability problem の未解決残余ではない。

3. **Non-Markovian extensions は GST の失敗か。**  
   一般には違う。fixed Markovian gate-set model の scope を越える別 target / model class である。GST goodness-of-fit が拡張の必要を示唆する場合はあるが、論理的に一意の次段階を決めない。

4. **仮説した反復連鎖はあったか。**  
   支持されなかった。局所的な problem–solution relation はあるが、同型の relocation が反復する証拠も、独立の診断効果も得られなかった。

5. **普通の科学的精密化を越える価値はあったか。**  
   Deferred Resolution という概念にはなかった。negative comparison は、異種の residual を混同しない教育的・索引的価値を持つが、field-native literature を越える方法論的成果ではない。

**GST Case 01はDeferred Resolutionを支持せず、既存のmodel-building / identifiability / quotient / validation語彙でより正確に記述できるnegative caseだった。**

---

## 24. References

### Standard tomography and calibration

- Chuang, I. L., & Nielsen, M. A. (1997). “Prescription for experimental determination of the dynamics of a quantum black box.” *Journal of Modern Optics*, 44(11–12), 2455–2467. [DOI](https://doi.org/10.1080/09500349708231894)
- D’Ariano, G. M., & Lo Presti, P. (2001). “Quantum tomography for measuring experimentally the matrix elements of an arbitrary quantum operation.” *Physical Review Letters*, 86, 4195–4198. [DOI](https://doi.org/10.1103/PhysRevLett.86.4195); [arXiv](https://arxiv.org/abs/quant-ph/0012071)
- D’Ariano, G. M., Paris, M. G. A., & Sacchi, M. F. (2003). “Quantum tomography.” *Advances in Imaging and Electron Physics*, 128, 205–308. [DOI](https://doi.org/10.1016/S1076-5670(03)80065-4)
- D’Ariano, G. M., Maccone, L., & Lo Presti, P. (2004). “Quantum calibration of measurement instrumentation.” *Physical Review Letters*, 93, 250407. [DOI](https://doi.org/10.1103/PhysRevLett.93.250407)

### Self-consistent tomography and GST

- Merkel, S. T., Gambetta, J. M., Smolin, J. A., Poletto, S., Córcoles, A. D., Johnson, B. R., Ryan, C. A., & Steffen, M. (2013). “Self-consistent quantum process tomography.” *Physical Review A*, 87, 062119. [DOI](https://doi.org/10.1103/PhysRevA.87.062119); [arXiv full text](https://arxiv.org/abs/1211.0322)
- van Enk, S. J., & Blume-Kohout, R. (2013). “When quantum tomography goes wrong: drift of quantum sources and other errors.” *New Journal of Physics*, 15, 025024. [DOI](https://doi.org/10.1088/1367-2630/15/2/025024)
- Blume-Kohout, R., Gamble, J. K., Nielsen, E., Rudinger, K., Mizrahi, J., Fortier, K., & Maunz, P. (2017). “Demonstration of qubit operations below a rigorous fault tolerance threshold with gate set tomography.” *Nature Communications*, 8, 14485. [DOI](https://doi.org/10.1038/ncomms14485)
- Nielsen, E., Gamble, J. K., Rudinger, K., Scholten, T., Young, K., & Blume-Kohout, R. (2021). “Gate Set Tomography.” *Quantum*, 5, 557. [DOI](https://doi.org/10.22331/q-2021-10-05-557)

### Operational and gauge-free formulations

- Di Matteo, O., Gamble, J. K., Granade, C., Rudinger, K., & Wiebe, N. (2020). “Operational, gauge-free quantum tomography.” *Quantum*, 4, 364. [DOI](https://doi.org/10.22331/q-2020-11-17-364)

### Model checking and extensions

- Pollock, F. A., Rodríguez-Rosario, C., Frauenheim, T., Paternostro, M., & Modi, K. (2018). “Non-Markovian quantum processes: Complete framework and efficient characterization.” *Physical Review A*, 97, 012127. [DOI](https://doi.org/10.1103/PhysRevA.97.012127)
- Rudinger, K., Hogle, C. W., Naik, R. K., Hashim, A., Lobser, D., Santiago, D. I., Grace, M. D., Nielsen, E., Proctor, T., Seritan, S., Clark, S. M., Blume-Kohout, R., Siddiqi, I., & Young, K. C. (2021). “Experimental characterization of crosstalk errors with simultaneous gate set tomography.” *PRX Quantum*, 2, 040338. [DOI](https://doi.org/10.1103/PRXQuantum.2.040338)
- White, G. A. L., Pollock, F. A., Hollenberg, L. C. L., Modi, K., & Hill, C. D. (2022). “Non-Markovian quantum process tomography.” *PRX Quantum*, 3, 020344. [DOI](https://doi.org/10.1103/PRXQuantum.3.020344)
- Li, Z.-T., Zheng, C.-C., Meng, F.-X., Zeng, H., Luan, T., Zhang, Z.-C., & Yu, X.-T. (2024). “Non-Markovian quantum gate set tomography.” *Quantum Science and Technology*, 9, 035027. [DOI](https://doi.org/10.1088/2058-9565/ad3d80); [arXiv](https://arxiv.org/abs/2307.14696)
- Wood, C. J., & Gambetta, J. M. (2018). “Quantification and characterization of leakage errors.” *Physical Review A*, 97, 032306. [DOI](https://doi.org/10.1103/PhysRevA.97.032306)

### General model building, nuisance parameters, and system identification

- Box, G. E. P. (1976). “Science and statistics.” *Journal of the American Statistical Association*, 71(356), 791–799. [DOI](https://doi.org/10.1080/01621459.1976.10480949)
- Cox, D. R., & Reid, N. (1987). “Parameter orthogonality and approximate conditional inference.” *Journal of the Royal Statistical Society: Series B*, 49(1), 1–18. [DOI](https://doi.org/10.1111/j.2517-6161.1987.tb01422.x)
- Gelman, A., & Shalizi, C. R. (2013). “Philosophy and the practice of Bayesian statistics.” *British Journal of Mathematical and Statistical Psychology*, 66(1), 8–38. [DOI](https://doi.org/10.1111/j.2044-8317.2011.02037.x)
- Ljung, L. (1999). *System Identification: Theory for the User* (2nd ed.). PTR Prentice Hall. [Author’s publication page](https://rt.isy.liu.se/en/books/sysid/)

---

## 25. Revision posture

### Comparatively secure

- standard tomography の trusted-reference dependence。
- Merkel et al. の fixed \(\rho_0\), \(M_0\) と joint gate estimation。
- GST probabilities の gauge invariance と quotient-level identifiability。
- non-unitary gauge transformations と complete positivity の非保存可能性。
- practical error metrics の gauge dependence。
- fixed Markovian GST と non-Markovian / context-sensitive extensions の target difference。
- process tensor が operational gauge-free tomography より年代的に先行すること。

### Interpretive synthesis

- A→B/C を nuisance/reference parameter promotion と整理すること。
- Null A と Null E の組合せを最良説明とすること。
- superficially similar residuals を assumption、quotient、reporting、adequacy に分類すること。

### Withdrawn

- GST lineage が反復的 Deferred Resolution chain を支持するという判定。
- 旧五段階 taxonomy。
- interface を限定しない equivalence 表現。
- 存在論的な一意性の完結をこのケースの outcome とすること。

### Open

- gauge-sensitive reporting が実際の decision threshold に与える protocol-specific effect。
- Merkel et al. の implicit symmetry と後の GST gauge formalism の厳密な歴史的対応。
- instrument-set tomography の quotient identifiability。

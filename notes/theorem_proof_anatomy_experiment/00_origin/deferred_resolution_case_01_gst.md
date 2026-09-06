# Deferred Resolution Case 01

## Quantum Tomography → Self-Consistent Tomography / GST → Gauge → Model Adequacy

- **Status:** working case study / corrigible literature audit / not a theorem announcement
- **Version:** 0.1
- **Date:** 2026-08-16
- **Parent note:** [`tool_truth_absence_working_note_v0.3.md`](./tool_truth_absence_working_note_v0.3.md)
- **Scope:** GST 系列に限定した boundary relocation 仮説の反証的検査

---

## 1. Purpose

本ケーススタディは、quantum tomography から self-consistent tomography、Gate Set Tomography（GST）、gauge-free / operational formulation、非 Markov 拡張へ至る文献群を用いて、次の作業仮説を検査する。

```text
resolution
   ↓
boundary relocation
   ↓
target reformulation
   ↓
new adequacy boundary
```

目的は GST を批判することではない。また gauge freedom や model extension から、無限後退、原理的不可知、存在論的非一意性を導くことでもない。限定された問いは、局所的な解決が、次にどの scope condition を明示するか、何を estimand とするか、どの model family を検査対象とするかを変更する場合があるか、である。

### 1.1 Result preview

一次文献からは、仮説の全系列を一つの recurrent deferred-resolution chain としては再構成できなかった。各遷移の型が異なる。

- known-reference tomography → self-consistent estimation は、明確な problem/solution relation である。
- GST の gauge freedom は、joint representation の厳密な observational invariance であり、単なる残存誤差ではない。
- operational gauge-free tomography は、主として target を quotient / observable coordinates へ変更することで gauge を閉じる。
- Markovianity、drift、leakage、crosstalk、memory は model adequacy の問題であり、gauge problem の未解決部分ではない。
- process-tensor 系は gauge-free tomography より前から展開しており、歴史的にも Stage D の単純な下流ではない。

ケース全体の最適判定は **DR-1 — Weak relocation** である。ただし **Null C（Solved by quotient）** と **Null D/E（historical sequencing / reviewer-imposed narrative）** が全系列の強い読みを制限する。この判定は科学一般の法則を主張しない。

---

## 2. Definition of deferred resolution

本ケースだけの作業定義を次とする。

> **Deferred Resolution** とは、問題 \(P_i\) が指定された target・model・保証条件の下で実質的に解決された後、その解決と論理的または実験的に接続する保証境界または残余同定問題が、下流の問題 \(P_{i+1}\) として明示化され、output の scope を制限するか、target の再定式化を促す構造をいう。

概念的 ledger としてのみ、次を使う。

```text
Problem P_i
   ↓ solved under assumptions A_i
Output O_i
   ↓ used downstream
Residual / scope boundary B_i
   ↓
Problem P_{i+1}
```

これは `unresolved forever`、`infinite regress`、`fundamental unknowability` を意味しない。後続問題が出ただけでも不十分である。判定には最低限、次を要求する。

1. 元問題 \(P_i\) が明確である。
2. 解決機構が明示され、指定 scope 内で \(P_i\) を実質的に閉じる。
3. 残る boundary がその解決構造と論理的・実験的に接続する。
4. boundary が downstream inference の scope を制限する。
5. boundary が新しい target、equivalence、または model-class problem として再定式化される。

### 2.1 「解決」の型

| Type | 本ノートでの意味 |
| --- | --- |
| **Exact resolution** | 指定モデル内で数学的な曖昧性または逆問題を除去する。 |
| **Operational resolution** | 明示した実験目的に必要な精度まで問題を制御する。 |
| **Reparameterization** | 同じ empirical model を別の座標で表す。 |
| **Quotient resolution** | 一意性 target を representative から observational equivalence class へ変更する。 |
| **Diagnostic resolution** | failure を除去せず、model violation として検出可能にする。 |
| **Dependency relocation** | 依存先を別の reference、interface、model promise、calibration step へ移す。 |

これらは同一ではない。とくに quotient resolution は、別個の model-adequacy question を残しても、gauge identification problem 自体を閉じうる。

---

## 3. Null hypotheses

以下を本仮説と同等以上に強く検討する。

### Null A — Ordinary refinement

方法が高精度・高一般性になっただけで、独自の deferred-resolution structure は不要である。

### Null B — Different problem

後続研究は別問題を扱う。たとえば gauge orbit の同定と temporal memory のモデル化は、一方が他方の残余なのではない。

### Null C — Solved by quotient

identifiable target を gauge-equivalence class とすれば gauge problem は閉じる。その後の adequacy problem は独立である。

### Null D — Historical sequencing only

論文の年代順は、提案した論理的依存を意味しない。

### Null E — Reviewer-imposed narrative

「境界移送」は既存研究を後から一列にした物語で、field-native account を越える診断内容を持たない。

本ノートは、一つでも残余があれば deferred resolution とする判定を採らない。

---

## 4. Literature method

一次論文を優先し、分野の自己整理が必要な箇所では 2021 年の GST review を用いた。対象は次である。

- standard state / detector / process tomography;
- 2013 年の self-consistent process tomography;
- experimental GST と GST review;
- 2020 年の operational, gauge-free tomography;
- process tensor、non-Markovian process tomography、instrument-set tomography。

各矢印は次のいずれかに分類する。

- **theorem / model implication**
- **problem/solution relation stated in the literature**
- **model-scope extension**
- **historical influence**
- **merely adjacent**
- **no evidence located**

記述順は field-native terminology first とする。SPAM error、gauge orbit、Markovian gate set、goodness of fit、process tensor を先に再構成し、その後に限って v0.3 の assurance provenance、backgrounding、handoff へ写す。

Claude Code の敵対的査読は検索・反証入力として参照したが、権威として採用していない。とくに calibration regress と GST gauge は既知の問題であるという指摘は一次文献で再確認した。一方、failure mode を一つの primary node へ排他的に配属すべきだという一般指示は採用せず、drift 等の cross-impact を保存する。

本調査は本ケースの判定には足りるが、文献全体の網羅を主張しない。直接接続を確認できない場合は、文献不在ではなく open literature check とする。

---

## 5. Historical sequence

年代順と論理的依存は分ける。

| Year | Work | 本ケースに関係する主な内容 | 仮説系列との関係 |
| --- | --- | --- | --- |
| 1997 | Chuang & Nielsen | characterized inputs と output tomography による quantum process tomography | standard known-reference QPT |
| 2001 | D'Ariano & Lo Presti | ancilla-assisted process tomography | reference/resource 構成の代替。GST ではない |
| 2003 | D'Ariano, Paris & Sacchi | state / process / measurement tomography の review | standard inverse-problem framework の整理 |
| 2004 | D'Ariano, Maccone & Lo Presti | calibrated probe または bipartite reference による detector calibration | calibration dependence の reference scheme への移送 |
| 2013 | Merkel et al. | faulty gate-generated SPAM を含む self-consistent QPT | standard QPT の systematic SPAM problem への直接応答 |
| 2017 | Blume-Kohout et al. | long-sequence GST、gauge、model-violation test の実験提示 | joint gate-set target と scope の明示 |
| 2018 | Pollock et al. | arbitrary multitime process の process-tensor framework | gauge-free 2020 より前に成立した broader temporal target |
| 2020 | Di Matteo et al. | operational, gauge-free parameterization | quotient / observable target による gauge 処理 |
| 2021 | Nielsen et al. | GST の包括的 review | fiducials、germs、gauge、model test、limitations の整理 |
| 2021 | Rudinger et al. | simultaneous GST による crosstalk characterization | 特定 failure に対する model/design extension |
| 2022 | White et al. | process-tensor による non-Markovian process tomography | 指定 time window の multitime correlation reconstruction |
| 2024 | Li et al. | non-Markovian gate characterization の instrument-set tomography | GST と system–environment correlation の直接的拡張 |

ここから二点が分かる。Stage A → B/C は、self-consistent paper 自身が standard QPT の reference-operation dependence に応答しており、歴史的・論理的接続が強い。他方、process-tensor work は operational gauge-free tomography より前であり、GST も 2017 年には model violation を扱っていた。したがって Stage D → E を年代順の一方向系列として正当化できない。

---

## 6. Stage A — Standard state, detector, and process tomography

### Problem

standard task は別々の inverse problem である。

- **state tomography:** characterized measurement の outcome statistics から未知状態を推定する。
- **detector tomography:** characterized probe states または reference arrangement を用いて未知 POVM / instrument を推定する。
- **process tomography:** characterized input preparations と output measurements を用いて未知 channel を推定する。

D'Ariano, Paris & Sacchi は tomography を同様に準備した ensemble への反復測定からの再構成として整理し、Chuang & Nielsen は既知入力を準備し、未知 process を作用させ、出力状態を測る QPT を定式化する（[D'Ariano, Paris & Sacchi 2003](https://arxiv.org/abs/quant-ph/0302028); [Chuang & Nielsen 1997](https://arxiv.org/abs/quant-ph/9610001)）。

### Target

task に応じて、density operator \(\rho\)、POVM / instrument、quantum channel \(\mathcal E\) を、指定 Hilbert-space dimension と表現の下で推定する。

### Backgrounded / fixed inputs

- state tomography では trusted measurement model;
- detector tomography では trusted probe states;
- process tomography では trusted input preparation と output measurement;
- repeated preparation または明示的に供給された multicopy / ancilla resource;
- dimension、acquisition 中の stationarity、sampling model。

ancilla-assisted QPT は resource arrangement を変えるが、characterized measurement/reference structure を消去しない（[D'Ariano & Lo Presti 2001](https://arxiv.org/abs/quant-ph/0012071)）。detector calibration も未知 detector を calibrated probe または別の characterized tomographic arrangement と比較する（[D'Ariano, Maccone & Lo Presti 2004](https://arxiv.org/abs/quant-ph/0408116)）。

### Resolution mechanism

informationally complete experiment が指定 model 上の forward map を injective にし、linear inversion、maximum likelihood、Bayesian estimation 等が有限データから target を復元する。alternative design は使う reference object や resource を変更する。

### What is genuinely resolved

指定有限次元モデルと trusted reference interface の内部では、ideal inverse problem は identifiable になりうる。有限データでは estimator が error bar、confidence region、posterior uncertainty を与えうる。これは実質的な局所解決であり、哲学的な仮置きではない。

### Residual

output は reference operations、sampling model、finite-sample behavior、conditioning、dimension、stationarity の妥当性に依存する。標本数を増やしても、データ生成に使う操作の固定 systematic error は消えない。

### New boundary

本ケースで重要なのは SPAM / reference-operation characterization である。preparation と measurement も同じ実験内の未知量なら、既知だった forward map は所与でなくなる。これとは別に、\(d\)-dimensional stationary model の adequacy boundary がある。

### Target reformulation

この段階では通常ない。個別に表現された state、detector、process が target である。

### Downstream consequence

推定 state / process は device validation、control、foundational experiment に渡る。downstream では、uncertainty propagation を明示しない限り reference calibration が背景化する。

### Literature language

文献は informational completeness、calibration、systematic SPAM error、statistical error、process reconstruction と呼ぶ。GST review は standard state/process/measurement tomography が trusted fiducial operation に依存することと、全操作が imperfect な場合の循環を明示する（[Nielsen et al. 2021](https://doi.org/10.22331/q-2021-10-05-557)）。

### Deferred-resolution status

**PARTIAL.** standard tomography は定義した inverse problem を解く。その trusted-reference dependence が self-consistent method の問題を与えるが、依存は元 task の specification に含まれており、元 task が未解決だった証拠ではない。

---

## 7. Stage B — Self-consistent process tomography

### Problem

Merkel et al. は standard QPT の具体的 failure から始める。input preparation と measurement rotation を生成する gates に coherent systematic error があると、standard QPT はその誤差を test target の gate に誤帰属しうる。oversampling は statistical error を減らしても、この bias を除去しない（[Merkel et al. 2013](https://arxiv.org/abs/1211.0322)）。

### Target

target は trusted auxiliary gates に条件づけた一つの process ではない。target operations の近傍で、gate library 全体を jointly / self-consistently 推定する。

### Backgrounded / fixed inputs

2013 年の方法は全 laboratory component を未知にしない。base initial state \(\rho_0\) と base observable \(M_0\) を固定し、target に近い gate library と acquisition 中の安定性を仮定する。論文自身も、\(\rho_0\)、\(M_0\)、slowly time-varying error を今後の拡張として挙げる。

### Resolution mechanism

faulty gate library を既知 reference とせず、overcomplete circuit family を作り、library 全体を likelihood によって同時 fit する。同じ gates が生成する preparation / measurement error を、test gate へ暗黙に押し込まず joint model 内へ置く。

### What is genuinely resolved

linearized stable-library model の内部で、gate-generated SPAM の systematic misattribution を解く。これは単なる精度向上ではない。target を、known auxiliaries に条件づけた一 gate から coupled gate library へ変える。

### Residual

- base state と base measurement は固定される。
- approximation は target operations の近傍にある。
- slowly varying error は一つの static library で表されない。
- joint circuit probabilities を不変にする similarity transform があれば、matrix representation は一意でない。

最後の点は成熟した GST の中心となるが、2013 年論文は gauge freedom として明示的には展開していない。後世の語彙を無条件に遡及させない。

### New boundary

gate-generated SPAM の calibration boundary は estimand 内へ移る。他方、base SPAM、temporal stability、target-neighborhood approximation、representation の境界が残る。

### Target reformulation

**YES.** estimand は jointly constrained gate library になる。fully developed GST ではないが、同定対象は明確に変わる。

### Downstream consequence

この joint-target idea は GST に接続する。state preparation、measurement、gates を同じ circuit data から推定し、そのどの組合せが observable かを明示する方向である。

### Literature language

論文は self-consistent quantum process tomography、statistical/systematic error、joint reconstruction と呼ぶ。後の GST における calibration-free は、estimated SPAM operation を事前に perfect と宣言しないという意味であり、model、coordinate convention、experiment design、stability condition が不要という意味ではない。

### Deferred-resolution status

**YES, LOCALLY.** 明確な SPAM-induced bias が joint inference で処理され、その解決が target と残る reference/model boundary を変える。一つの局所的な `resolution → relocation` は支持するが、反復系列はまだ支持しない。

---

## 8. Stage C — Gate Set Tomography

### Problem

GST は、利用できる state preparation、measurement、gates がすべて imperfect で、どれも error-free tomographic reference とできない状況を扱う。同時に、小さな gate error への高感度化と、fixed Markovian gate-set model が circuit data に適合するかの統計検査を目指す（[Blume-Kohout et al. 2017](https://doi.org/10.1038/ncomms14485); [Nielsen et al. 2021](https://arxiv.org/abs/2009.07301)）。

### Target

gate set を典型的に

\[
\mathcal G=(\rho,E,G_1,\ldots,G_k)
\]

と表す。\(\rho\) は preparation、\(E\) は measurement effect、\(G_i\) は gates である。data が拘束するのは control-label sequences の circuit probabilities であり、target は全確率を保存する変換を除いた gate set、すなわち gauge orbit である。

### Backgrounded / fixed inputs

- Hilbert / Liouville-space dimension;
- control labels と circuit composition rule;
- base model では各 label に対する time-independent、context-independent、Markovian map;
- gauge-invariant parameters を observable / amplifiable にする fiducials と germs;
- sampling likelihood と明示した trial model;
- optimizer と、採用する場合の physicality constraints。

GST review は、通常の GST が processor 全体の holistic model ではなく、任意の crosstalk、drift、leakage、environment memory を自動的に含まないと明示する。

### Resolution mechanism

fiducials が informationally complete な effective preparation / measurement を生成し、germs が gate parameters を増幅し、長い circuits が感度を高める。global likelihood fit が全 gate-set components を同時推定し、goodness-of-fit statistics が fixed model を data と比較する。

### What is genuinely resolved

- estimated gate set 内の SPAM operation を perfect reference と事前認定する必要を除く。
- gauge-invariant combinations を self-consistently 推定する。
- long-sequence design により coherent error を増幅する。
- fixed Markovian model の fit failure を統計的に検出する。

最後は **diagnostic resolution** である。model incompatibility を検出するが、drift、leakage、crosstalk、memory のどれが原因かを単独では特定しない。

### Residual 1 — Gauge freedom

invertible representation change \(B\) に対して、通常の Liouville representation では

\[
\rho\mapsto B\rho,\qquad
E\mapsto EB^{-1},\qquad
G_i\mapsto BG_iB^{-1}
\]

と変換しても全 circuit probability は不変である。したがって likelihood は unique point でなく gauge orbit を持つ。GST review は、gate set のみから構成される実験では orbit の representatives を区別できないため、global gauge までの reconstruction を成功とする（[Nielsen et al. 2021](https://doi.org/10.22331/q-2021-10-05-557)）。

ここで五つを分ける。

1. **observational non-identifiability:** individual matrix representative は circuit probabilities から決まらない。
2. **representational redundancy:** 複数の座標記述が同じ operational predictions を符号化する。
3. **physical equivalence:** 宣言された experimental interface に相対して gauge-related models は区別不能である。
4. **reporting convention:** gauge optimization は比較・可視化に便利な representative を選ぶ。
5. **model misspecification:** gate-set family 全体が data に適合しない。

1–4 が gauge であり、5 は別問題である。gauge optimization は misspecification を修復せず、model expansion は absolute gauge を選ばない。

### Residual 2 — Model scope

base gate-set model は各 gate label に fixed map を割り当てる。drift、history dependence、persistent environment correlation、context dependence、modeled subspace 外への leakage、crosstalk は、この割当ての異なる部分を壊しうる。2017 年の実験論文は goodness-of-fit failure が assumption violation を示しても、その物理原因を単独では特定しないとする（[Blume-Kohout et al. 2017](https://doi.org/10.1038/ncomms14485)）。

### New boundary

GST は二つの別 boundary を明示する。

- **equivalence boundary:** gate set は gauge modulo で識別される。
- **adequacy boundary:** fixed-dimensional Markovian gate-set model が対象 circuits に適合する必要がある。

前者は representation の厳密な symmetry、後者は empirical modeling question である。一つの「残る未知」へまとめてはならない。

### Target reformulation

**YES.** target は individually absolute な SPAM / gate matrices ではなく、relational gate set / gauge orbit と circuit predictions になる。

### Downstream consequence

一方の下流は gauge-invariant / operational coordinates を求め、他方は fixed Markovian assumption の violation を診断・モデル化する。二つは異なる residual から分岐し、一系列とは限らない。

### Literature language

self-consistent、calibration-free、gauge freedom、gauge optimization、fiducial completeness、amplificational completeness、Markovian gate set、model violation が分野固有語である。ここでは generic な assurance boundary より精密である。

### Deferred-resolution status

**PARTIAL.** GST は trusted-SPAM dependence を joint target への変更によって実質的に処理する。gauge は identifiable-equivalence structure、model adequacy は条件として残る。しかし gauge 自体は未解決 calibration error ではなく、recurrent deferral を示さない。

---

## 9. Stage D — Operational, gauge-free tomography

### Problem

gauge-dependent coordinates は、物理的に区別不能な representatives を matrix norm 上で異なって見せ、reporting、prior、uncertainty quantification、model comparison を難しくする。Di Matteo et al. は operationally accessible quantities からなる self-consistent parameterization を求める（[Di Matteo et al. 2020](https://arxiv.org/abs/2007.01470)）。

### Target

target は gauge orbit の特権的 representative ではない。specified fiducial experiments に結びつく operational model、同値に sequence probabilities を保存する equivalence class である。論文の形式では、button sequences から transformations への homomorphisms の quotient として

\[
G(B,H)=\operatorname{Hom}(S,T(H))/\!\sim
\]

を扱い、\(\sim\) は stated conditions の下で同じ operational statistics を生成する model を同一視する。

### Backgrounded / fixed inputs

- state-space / Hilbert-space structure \(H\) の promise;
- button sequences から transformations への compositional / homomorphic assignment;
- informationally adequate fiducials;
- repeated data と statistical model;
- equivalence を定義する declared operational interface。

homomorphism condition は fixed compositional / Markovian structure を符号化する。arbitrary history-dependent experiment は暗黙に含まれない。

### Resolution mechanism

quotient を gauge-invariant かつ experimentally accessible な値で直接 parameterize する。redundant gate-set representation を fit してから gauge optimize するのでなく、operational parameters 上で Bayesian inference 等を行う。

### What is genuinely resolved

promised model 内で、representational ambiguity を inferential target から除く。prior と posterior を identifiable quantities に置き、unobservable absolute frame を選ばず future experiments を予測できる。

これは **quotient resolution + reparameterization** が最も正確である。論文が gauge problem を solve / address と表現することは妥当だが、unique underlying matrix representative を発見したのではない。

### Residual

finite-data uncertainty、fiducial quality、numerical inference、dimension/model promise、homomorphic composition assumption は残る。対象が model 外の context dependence / non-Markovianity を持つなら、gauge-free coordinates は model を adequate にしない。

### New boundary

quotient は model-scope boundary を明瞭にする。representation redundancy を除いた後、operational model の empirical adequacy が別問題として残る。この boundary は quotient が新しく作ったのではなく、model specification に既に含まれていた。

### Target reformulation

**YES, EXPLICITLY.** target を gauge-dependent representative から equivalence class 上の operational coordinates へ変更する。

### Downstream consequence

gauge-free inference は operational prediction と uncertainty reporting を支える。broader temporal / context-dependent behavior には、別の gauge choice でなく formal object の拡張が必要である。

### Literature language

operational representation、gauge-free quantum tomography、observables as model parameters、gauge equivalence と呼ぶ。absolute hidden gate set へのアクセスを先送りしたとは記述しない。

### Deferred-resolution status

**NO for gauge as a deferred problem; PARTIAL for scope visibility.** Null C を強く支持する。correct target を quotient とすれば gauge identification problem は閉じる。残る model-adequacy question は実在するが、gauge の未解決部分ではない。

---

## 10. Stage E — Beyond fixed Markovian gate sets

### Problem

fixed gate-set model は、dynamics が time、history、neighboring controls、persistent environment、chosen computational subspace 外の degree of freedom に依存すると破れうる。これらを一つの generic non-Markovianity にまとめない。

### Target

extension ごとに target が違う。

- multitime input–output behavior と temporal correlations の **process tensor**;
- interventions と system–environment correlations を共同表現する **instrument set**;
- 特定 crosstalk の simultaneous / context-aware gate sets;
- enlarged Hilbert space / leakage model;
- time-indexed / drift model。

Pollock et al. は general multitime quantum process の operational framework として process tensor を定式化する（[Pollock et al. 2018](https://arxiv.org/abs/1512.00589)）。White et al. は指定 time window 上の non-Markovian process-tensor tomography を示す（[White et al. 2022](https://doi.org/10.1103/PRXQuantum.3.020344)）。Li et al. は gate-set setting で system–environment effect を共同 characterise する instrument-set tomography を提案する（[Li et al. 2024](https://arxiv.org/abs/2307.14696)）。

### Backgrounded / fixed inputs

extension は一部仮定を緩めるが、別の指定を置く。

- finite time window、memory length、bond/environment dimension;
- informationally adequate intervention set;
- stable control labels と system boundary;
- tractable correlation structure;
- finite-sample / numerical conditions。

learnable target を定義する制約であり、残ること自体は欠陥でない。

### Resolution mechanism

中心は model enlargement と target reformulation である。sequence を independent one-step maps の積でなく multitime object として扱い、instrument と latent environment correlation を jointly estimate するか、crosstalk-specific circuits を設計する。simultaneous GST は crosstalk を irreducible residual とせず、GST model/design を拡張して characterise する（[Rudinger et al. 2021](https://arxiv.org/abs/2103.09890)）。

### What is genuinely resolved

指定 horizon と intervention set の内部で、fixed Markovian gate set が表せない temporal correlation、memory structure、context-dependent behavior の一部を再構成する。これは substantive model expansion であり、GST が宣言 scope 内で失敗していた証拠ではない。

### Residual

sample complexity、intervention completeness、system-boundary choice、finite memory/order、leakage dimension、acquisition 中の drift、observed window 外への extrapolation が残りうる。

### New boundary

| Failure / scope issue | 何を壊すか |
| --- | --- |
| Markovianity | history-independent maps からの composition |
| Stationarity / drift | acquisition/use 中の target constancy |
| Leakage | chosen computational state space の closure |
| Crosstalk | local/tensor-product control structure |
| Context dependence | gate label への一 fixed map assignment |
| Memory | earlier intervention/outcome からの conditional independence |
| System–environment correlation | system boundary での preparation/composition assumption |
| Dimension error | reconstruction に使う state-space size |
| Control nonlinearity | control setting と implemented map の対応 |

model adequacy は umbrella にはなるが、これらは異なる model relation を壊し、別の diagnostic を要する。

### Target reformulation

**YES, HETEROGENEOUSLY.** process tensor、instrument set、leakage model、time-dependent gate model は、一 target の別座標ではなく別の extended question に答える。

### Downstream consequence

output は control design、error mitigation、device model、宣言した temporal/contextual range の prediction に使われる。scope condition を output とともに渡す必要がある。

### Literature language

non-Markovian process、process tensor、quantum stochastic process、instrument-set tomography、crosstalk characterization、leakage、drift が分野語彙である。一つの deferred-resolution doctrine の事例とは呼ばれていない。

### Deferred-resolution status

**PARTIAL.** fixed Markovian GST から broader target への論理的 model-scope extension はあり、instrument-set tomography はとくに直接的な接続を与える。しかし process-tensor theory は一部並行して先行した。Stage E は gauge の次の未解決部分でなく、全体は uninterrupted chain ではない。

---

## 11. Stage-by-stage ledger

| Stage | Stated problem | Resolution type | 実際に閉じるもの | 解決後の boundary | Target change | DR status |
| --- | --- | --- | --- | --- | --- | --- |
| A — standard tomography | characterized reference から state / detector / process を推定 | exact/model-relative inversion + statistical estimation | specified forward model 内の identifiability | reference calibration、sampling、stability、dimension/model adequacy | 通常なし | PARTIAL |
| B — self-consistent QPT | gate-generated SPAM が ordinary QPT を bias | joint inference / dependency relocation | 指定 class の systematic SPAM misattribution | base SPAM、local approximation、temporal stability、representation | process → gate library | YES locally |
| C — GST | perfect reference 不在、高感度化、model test | joint estimation、design amplification、diagnostic resolution | relative gate-set prediction、gauge-invariant parameters、bad fit 検出 | gauge orbit と fixed Markovian scope | gate set modulo gauge | PARTIAL |
| D — operational gauge-free | redundant coordinates が inference/reporting を妨げる | quotient resolution + reparameterization | inferential target 内の gauge ambiguity | dimension/composition promise と finite-data adequacy | representative → operational class | NO for gauge deferral |
| E — extended models | fixed maps が temporal/contextual structure を除外 | model expansion + new tomography target | 指定 memory/crosstalk/leakage/multitime behavior | horizon、order、dimension、intervention completeness | gate set → process tensor 等 | PARTIAL |

この ledger は二つの短絡を遮断する。

1. residual があることは、前問題が未解決であることを意味しない。gauge は quotient で閉じても model adequacy は別に残る。
2. broader model があることは、earlier model の failure を意味しない。fixed Markovian gate set は宣言 domain 内で適切かつ predictive でありうる。

---

## 12. Two sequences

### 12.1 Historical sequence

```text
standard QPT (1997 and earlier traditions)
   ├── ancilla-assisted QPT (2001)
   ├── tomography review (2003)
   └── detector calibration (2004)
             │
             └── self-consistent QPT (2013)
                       │
                       └── experimental / long-sequence GST (2017)
                              ├── model-violation analysis (2017までに明示)
                              └── comprehensive GST synthesis (2021)

process-tensor framework (submitted 2015; published 2018)
   └── non-Markovian process-tensor tomography (2022)

operational gauge-free tomography (2020)
simultaneous/crosstalk GST (2021)
instrument-set tomography (2024)
```

この年代配置は、gauge-free tomography が Markovian adequacy を初めて露呈させ、それが process-tensor theory を生んだ、という歴史記述を否定する。

### 12.2 Logical dependency sequence

```text
characterized preparation + characterized measurement
       │  [calibration/modeling dependence]
       ▼
standard state/process tomography
       │  systematic error in gate-generated SPAM
       │  [problem/solution relation: strong]
       ▼
self-consistent joint gate estimation
       │  all estimated operations treated relationally
       │  [model implication: strong]
       ▼
GST gate set identified up to gauge
       ├─────────────────────────────────────┐
       │ exact observational equivalence     │ fixed-map model tested against data
       │ [model symmetry: strong]             │ [statistical/model relation: strong]
       ▼                                     ▼
operational quotient target            model violation detected
       │                                     │
       │ model promise remains               ├── drift model
       │ [scope relation: strong]             ├── leakage/crosstalk model
       ▼                                     └── memory/process-tensor/instrument-set model
model adequacy of operational target

未確認の直接edge:
operational quotient target ──?──▶ non-Markovian extensions
```

これは ontology へ近づく、または遠ざかる staircase ではない。estimand、invariance、model test、alternative expansion の分岐図である。

---

## 13. Edge ledger

| From | To | Edge type | Evidence | Strength |
| --- | --- | --- | --- | --- |
| Known SPAM/reference operations | Standard tomography | calibration/modeling dependence | standard QPT/tomography literature | strong |
| Systematic gate-generated SPAM error | Self-consistent QPT | stated problem/solution relation | Merkel et al. 2013 | strong |
| Self-consistent gate-library inference | GST | methodological/historical development | GST review と shared joint target | medium–strong |
| GST joint representation | Gauge equivalence | exact model symmetry / observational invariance | GST review、operational tomography | strong |
| Gauge equivalence | Gauge optimization | reporting/target-comparison convention | GST literature | strong |
| Gauge equivalence | Operational quotient target | mathematical/conceptual target reformulation | Di Matteo et al. 2020 | strong |
| Fixed Markovian GST model | Goodness-of-fit test | statistical model-check relation | Blume-Kohout et al. 2017; Nielsen et al. 2021 | strong |
| Poor GST fit | Specific cause（drift 等） | diagnostic inference | fit failure は nonspecific | weak without additional tests |
| Fixed Markovian model | Process-tensor target | model-scope enlargement | process-tensor literature | logically strong; direct historical influence weak |
| GST + system–environment memory | Instrument-set tomography | direct model/target extension | Li et al. 2024 | strong |
| Fixed local gate-set model | Simultaneous crosstalk GST | design/model extension | Rudinger et al. 2021 | strong for specified problem |
| Operational gauge-free tomography | Non-Markovian process tomography | proposed sequence relation | direct dependency 未確認 | unclear / apparently adjacent |
| Gauge freedom | Model misspecification | alleged continuation | primary literature では orthogonal | rejected |

仮説系列を圧縮すると次である。

```text
known-SPAM tomography
   ──[strong problem specification]──▶ self-consistent joint estimation
   ──[strong joint-model implication]▶ gauge equivalence
   ──[strong quotient reformulation]─▶ operational target
   ──[no direct historical edge found]▶ non-Markovian extensions
```

最初の三矢印は残るが、edge type は同じでない。第四矢印は直接接続として残らず、valid な最短 edge は **fixed Markovian gate-set adequacy → model-specific extensions** である。

---

## 14. Assurance provenance map

以下は field-native reconstruction 後の比較写像である。categories は非排他的で完全性を主張しない。

| Output | Theorem-supported | Design-supported | Calibration-supported | Statistically constrained | Empirically cross-checked | Model-relative | Interpretive |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Standard tomographic estimate | IC / inversion results | measurement/probe design | trusted reference に明示依存 | estimator、confidence/posterior | repeated data / validation | dimension、state/channel model | reconstruction 自体には不要 |
| Self-consistent gate library | joint forward model | overcomplete circuits | gate-generated calibrated SPAM 依存を低減。early form は fixed inputs を保持 | joint likelihood | circuit behavior との比較 | local error / stability | reconstruction 自体には不要 |
| GST gate-set orbit | gauge invariance / identifiability | fiducials、germs、lengths | gate set 内に perfect operation 不要。lab traceability は残る | likelihood、uncertainty、GOF | independent circuits / device checks | fixed-dimensional Markovian family | orbit の存在論的読みは別問題 |
| Operational gauge-free model | quotient representation | informative fiducials | relative operational references | Bayesian 等の finite-data inference | future-sequence prediction | homomorphic/compositional promise | operational equivalence の存在論的読みは別問題 |
| Process tensor / instrument set | multitime representation | complete interventions | intervention characterization | uncertainty / model selection | held-out histories | time window、memory/order/dimension | reconstruction 自体には不要 |

保証源が異種であることは unsupported を意味しない。target fit が単独で自己証明しない条件も、design、calibration、theorem、independent checks から強く支持されうる。

---

## 15. Backgrounding / handoff map

### 15.1 Foreground/background の変化

| Item | Stage A | Stage B/C | Stage D | Stage E |
| --- | --- | --- | --- | --- |
| SPAM calibration | foreground prerequisite | jointly estimated target（scope あり） | operational relative quantities へ吸収 | intervention characterization が practical input |
| Gauge | fixed reference のため通常前景化しない | joint representation の explicit non-identifiability | quotient/operational coordinates で target から除く | model-specific redundancy はありうるが同じ unresolved physical question ではない |
| Markovianity/composition | one-shot channel では背景化しやすい | explicit model class + GOF | homomorphic operational model に内在 | relaxed / foreground target |
| Drift | fixed state/process target を壊す | static gate-set model violation | static operational target 外 | time-dependent target / cross-cutting failure |
| Dimension/leakage | fixed model choice | scope condition / possible violation | promise \(H\) に残る | enlarged target / leakage-specific model |

backgrounding は neglect ではない。calibrated interface や既に検査した scope を安定入力として扱い、別の inverse problem に集中するのは合理的分業である。監査対象は、scope と uncertainty が handoff を越えて保持されるかである。

### 15.2 Cross-domain handoff

```text
calibrated reference or self-consistent circuit model
        ↓
tomographic / GST estimate + uncertainty + model scope
        ↓
device validation / control / foundational experiment
        ↓
model exclusion or engineering decision
```

downstream が upstream の全 calibration を毎回開き直さないこと自体は欠陥でない。問題候補は、model-relative / gauge-conventional quantity を invariant と扱う、relevant uncertainty を落とす、validated context 外へ外挿する場合である。本ケースは実 protocol でそのような loss を発見していない。

### 15.3 Cross-impact example: drift

```text
drift
 ├─ ordinary tomography の state/process target identity を壊す
 ├─ GST の one-static-gate-set assumption を壊す
 ├─ iid / stationary likelihood を不適切にしうる
 ├─ calibration transfer across time を弱める
 └─ broader process model では temporal correlation として現れうる
```

したがって drift を一つの node に排他的に所属させない。ただし本ケースの主眼は cross-impact 一般でなく problem relocation sequence である。

---

## 16. Boundary relocation analysis

### 16.1 Standard tomography → self-consistent estimation

ここが本ケースで最も強い relocation である。

| Criterion | Assessment |
| --- | --- |
| 元問題が定義済み | YES — characterized operations を用いた unknown process reconstruction |
| 解決が明示 | YES — informationally complete tomography + finite-data estimator |
| 残余が解決と接続 | YES — 同じ reference operations の error が forward model を bias |
| downstream scope を制限 | YES — estimate は reference model の信頼範囲に条件づく |
| 新 target/problem | YES — perfect gate-generated SPAM に条件づけず gate library を jointly estimate |

元 task が偽りの解決だったのではない。条件付きで解かれ、条件を満たせない場合に self-consistent method が target を拡張した。`先送り` より **relocation** が正確である。

### 16.2 Self-consistent estimation / GST → gauge equivalence

absolute trusted reference を外し joint relative model にすると、simultaneous similarity transform に invariant な組合せだけが identifiable になる。この接続は強い model implication である。

しかし、absolute gate matrix が物理的に実在するのに隠れた、とは言えない。data と intervention algebra が equivalence class を定める。gauge を「新しい未解決問題」と呼ぶことは quotient target を不当に退ける。

```text
trusted absolute reference removed
       ↓
joint relative model
       ↓
gauge orbit is the identifiable object
```

これは deferral より **target clarification** である。

### 16.3 Gauge equivalence → operational gauge-free target

operational formulation は gauge の未解決部分を downstream へ持ち越すのではなく、既に identifiable だった equivalence class を直接 parameterize する。したがって Deferred Resolution の criterion 3 は同じ意味では成立せず、**Null C** を支持する。

dimension と composition の model promise は quotient が生成した残余でない。初めからの specification が、redundancy を除いた後に見やすくなっただけである。

### 16.4 Fixed Markovian GST → extended models

```text
one fixed map per control label
       ↓ tested against circuit data
fit acceptable ──▶ use within validated scope
fit rejected / broader target required
       ├── time-dependent/drift model
       ├── crosstalk/leakage model
       └── process-tensor/instrument-set model
```

これは diagnostic resolution に続く model expansion と読める。ただし各 branch は異なる conditional independence、state space、control semantics を変更する。poor GST fit だけから branch は選べない。

### 16.5 Full sequence verdict

全系列は、次の弱い branching form でのみ成立する。

```text
local inverse problem solved
       ↓
reference dependence motivates a joint target
       ↓
joint target has an exact equivalence structure
       ↓
quotient closes that representational ambiguity

independently but alongside:
fixed model is empirically tested
       ↓
specific violations motivate broader targets
```

最後の branch は GST model adequacy から出ており、gauge の未解決残余から出ない。仮説の linear formula は強すぎる。

---

## 17. Strongest mundane interpretation

最も強い通常解釈は次である。

> これは inverse-problem methodology の正常な成熟である。standard tomography は conditional problem を解き、self-consistent method は reference が imperfect な場合に estimand を拡張し、GST は実験が定められる quotient を同定し、operational tomography は redundant coordinates を除き、model checking と process-tensor method は異なる dynamical scope を扱う。特別な deferred-resolution mechanism は不要である。

この解釈は技術史を十分よく説明し、強い deferred-resolution 読解より優先される。既存文献には、reference dependence、joint estimation、identifiability modulo gauge、quotient parameterization、goodness-of-fit、misspecification、model extension が既にある。

その上で deferred-resolution vocabulary が追加しうるのは、次の category error を防ぐ ledger である。

1. conditional local solution を unconditional solution と誤認する。
2. quotient resolution を unresolved physical ambiguity と誤認する。
3. later model-scope extension を earlier method の failure と誤認する。

これは organizational / scope-preservation value の候補である。本ケースは、実験設計を変えた、missing check を発見した、field review より優れた診断をした、とは示していない。現段階では erasure test を通過していない可能性が高い。

---

## 18. Weak Claims A–D verdict

### Weak Claim A

> 局所的な識別問題を解決しても、その解決に必要な model scope または equivalence boundary が残る場合がある。

**SUPPORTED, WITH QUALIFICATION.** standard tomography は reference model に条件づき、GST は gauge modulo かつ gate-set family に条件づく。ただし「残る」は boundary が解決によって新造されたことを意味しない。

### Weak Claim B

> 一部の成熟した実験科学では、problem resolution が保証境界の消去だけでなく、明示化・移送・再定義として進む。

**PARTIALLY SUPPORTED.** GST 系列は reference dependence の joint estimand 化と quotient target の明示を示す。しかし一 domain、一 lineage から成熟した実験科学一般へは一般化できない。

### Weak Claim C

> operational success の増大と ontological closure の増大は同じ尺度ではない。

**PARTIALLY SUPPORTED, AS A SCOPE DISTINCTION.** 文献は operational characterization と model-class discrimination の改善を示すが、ontological closure を定義・測定しない。operational estimate が全 interpretive question に単独回答しないことは確認できても、両者の一般的反比例や独立性は示せない。

### Weak Claim D

> 科学的進歩は「何を一意に決める target とするか」を変更することで成立することがある。

**SUPPORTED IN THIS CASE.** absolute gate-set representative から gauge orbit / operational parameterization への移行は明確な quotient / target reformulation である。これは GST の既知内容であり、本ノートの新定理ではない。

---

## 19. DR-0–DR-4 classification

| Level | Definition | Case assessment |
| --- | --- | --- |
| **DR-0** | 単なる別問題の系列 | A → B/C の直接接続を捉えないため弱すぎる |
| **DR-1** | 一部の保証境界が downstream problem へ移る | **Best fit** |
| **DR-2** | resolution → relocation が複数段階で反復 | 未成立。quotient が gauge を閉じ、Stage E は adequacy から分岐する |
| **DR-3** | 異なる formalism を越えて安定した同型構造が診断に使える | 一ケースでは支持不能 |
| **DR-4** | 最終 closure が原理的に不可能 | theorem/evidence なし。本ケースでは棄却 |

### Case classification: DR-1 — Weak relocation

局所 pattern は実在する。

```text
trusted-reference inverse problem
  → joint estimation
  → equivalence-class target
```

しかし後続は同一 pattern の反復でない。gauge は quotient で閉じ、temporal/contextual adequacy は異なる model-extension problems に分岐する。したがって recurrent / structural deferred resolution は支持しない。

---

## 20. Implications for v0.3

### Recommendation: Minor revision, not yet applied

本ケースだけから deferred resolution を v0.3 assurance graph の中心構造にすべきでない。追加するなら Open Question または短い dynamic-edge note に限る。

> 局所解決は、estimand を変更し、equivalence boundary を明示し、または model-scope check へ依存を移す場合がある。監査では dependency relocation、quotient resolution、diagnostic resolution、independent model expansion を分ける。

Minor に留める理由は次である。

- 一つの technical lineage しか調べていない。
- 最も強い内容は GST / process-tensor literature に既に明示される。
- missing experimental check や incorrect inference を発見していない。
- 仮説の全系列は一 chain として失敗した。
- 固有語彙を消しても主要区別を field-native terminology で再構成でき、Erasure Test をまだ越えない。

Moderate revision には、第二分野で ledger が real handoff を明確化するか scope error を防ぐことが必要である。Major revision には複数 domain での反復的診断成功を要求する。

---

## 21. Open literature checks

以下は特記しない限り literature-audit task であり、未解決科学問題の主張ではない。

1. **Early GST genealogy:** 2012–2014 年の初期 GST 文献を直接追い、self-consistent QPT からの citation/technical changes を 2021 review に頼らず再構成する。
2. **Post-2020 gauge-free work:** quotient target と non-Markovian/context-dependent extension を直接接続する後続研究があるか確認する。
3. **Non-Markovian instrument-set identifiability:** representation gauge、physical equivalence、finite-memory non-identifiability を分ける。
4. **Experimental traceability:** 実 GST protocol で metrological references、uncertainty、drift checks が reported estimate へどう渡るか追う。
5. **Diagnostic specificity:** Markovian gate-set を reject するだけの test と、drift/leakage/crosstalk/memory を識別する protocol を比較する。
6. **Erasure benchmark:** deferred-resolution 語彙を消して最強の GST review と比較し、失われる inference、check、scope judgment があるか測る。
7. **Cross-domain replication — genuine research test:** latent-state realization equivalence を持つ system identification、または metrology の calibration transfer へ同じ resolution-type ledger を適用する。

---

## 22. Final verdict

### Q1 — GST 系列では、問題は残ったのか、解決後に次の境界が見えたのか

主として後者である。standard tomography は conditional inverse problem を解き、self-consistent tomography は trusted-reference condition を満たせない別状況で target を拡張する。元解決が偽だったのではない。

### Q2 — Gauge freedom は未解決問題か、equivalence class への修正か

主として後者である。declared circuit interface に相対して、gauge orbit が正しい identifiable target である。gauge optimization は reporting convention であり、model misspecification は別問題である。

### Q3 — Non-Markovian extensions は GST の failure か

一般には違う。fixed Markovian gate-set scope 外の behavior、または別 failure mode を characterise する broader target である。GST goodness-of-fit failure が拡張を動機づける場合はあるが、model が adequate な domain での GST 成功を取り消さない。

### Q4 — `resolution → boundary relocation → target reformulation → new adequacy boundary` は存在するか

**局所的・分岐的な形では存在する。** reference dependence は joint estimation を動機づけ、joint model は gauge equivalence を明示し、quotient は target を再定式化する。別 branch で fixed-model testing が broader dynamics を動機づける。しかし gauge から non-Markovianity へ続く recurrent linear chain はない。

### Q5 — 「普通の科学的精密化」を越える診断価値はあるか

現時点では限定的である。ledger は conditional solution、quotient resolution、model expansion の混同を防ぐ。しかし新しい experimental decision や missed check を示しておらず、追加価値は organizational / scope-preserving に留まる。

### Q6 — 最も強く言えるものの順位

技術的変化としては：

1. **target は再定義される** — matrix representative から gauge-equivalence class / operational coordinates への変更が最も明確。
2. **保証境界は移動または明示化される** — gate-generated SPAM の joint inference 化と fixed-model scope の検査。
3. **問題は先送りされる** — A → B/C の限定関係にのみ弱く適用でき、全系列には適用できない。

全体の説明としては、**単に科学が正常に精密化している**が第一である。これは上記 1–2 を否定せず、その最も強い mundane explanation である。

### Case conclusion

GST lineage が支持するのは **DR-1 — weak boundary relocation** であり、recurrent / fundamental non-closure ではない。異なる解決は異なる target を閉じる。ある方法は reference に条件づけ、ある方法は reference を joint model に入れ、ある方法は quotient を識別し、別の方法は model class を拡張する。

> **この GST 系列は「真理に辿り着けない」ことを示さず、局所的な解決が、何を解決済みの target とし、どの equivalence を採用し、次の model-scope boundary をどこに置くかを更新することを示している。**

---

## 23. References

### Standard tomography and calibration

1. Chuang, I. L., & Nielsen, M. A. (1997). “Prescription for experimental determination of the dynamics of a quantum black box.” *Journal of Modern Optics*, 44, 2455–2467. [arXiv](https://arxiv.org/abs/quant-ph/9610001) · [DOI](https://doi.org/10.1080/09500349708231894)
2. D'Ariano, G. M., & Lo Presti, P. (2001). “Imprinting Complete Information about a Quantum Channel on its Output State.” *Physical Review Letters*, 86, 4195–4198. [arXiv](https://arxiv.org/abs/quant-ph/0012071) · [DOI](https://doi.org/10.1103/PhysRevLett.86.4195)
3. D'Ariano, G. M., Paris, M. G. A., & Sacchi, M. F. (2003). “Quantum Tomography.” *Advances in Imaging and Electron Physics*, 128, 205–308. [arXiv](https://arxiv.org/abs/quant-ph/0302028) · [DOI](https://doi.org/10.1016/S1076-5670(03)80065-4)
4. D'Ariano, G. M., Maccone, L., & Lo Presti, P. (2004). “Quantum Calibration of Measurement Instrumentation.” *Physical Review Letters*, 93, 250407. [arXiv](https://arxiv.org/abs/quant-ph/0408116) · [DOI](https://doi.org/10.1103/PhysRevLett.93.250407)

### Self-consistent tomography and GST

5. Merkel, S. T., Gambetta, J. M., Smolin, J. A., Poletto, S., Córcoles, A. D., Johnson, B. R., Ryan, C. A., & Steffen, M. (2013). “Self-consistent quantum process tomography.” *Physical Review A*, 87, 062119. [arXiv](https://arxiv.org/abs/1211.0322) · [DOI](https://doi.org/10.1103/PhysRevA.87.062119)
6. Blume-Kohout, R., Gamble, J. K., Nielsen, E., Rudinger, K., Mizrahi, J., Fortier, K., & Maunz, P. (2017). “Demonstration of qubit operations below a rigorous fault tolerance threshold with gate set tomography.” *Nature Communications*, 8, 14485. [Article](https://www.nature.com/articles/ncomms14485) · [DOI](https://doi.org/10.1038/ncomms14485)
7. Nielsen, E., Gamble, J. K., Rudinger, K., Scholten, T., Young, K., & Blume-Kohout, R. (2021). “Gate Set Tomography.” *Quantum*, 5, 557. [arXiv](https://arxiv.org/abs/2009.07301) · [DOI](https://doi.org/10.22331/q-2021-10-05-557)

### Operational / gauge-free formulations

8. Di Matteo, O., Gamble, J. K., Granade, C., Rudinger, K., & Wiebe, N. (2020). “Operational, gauge-free quantum tomography.” *Quantum*, 4, 364. [arXiv](https://arxiv.org/abs/2007.01470) · [DOI](https://doi.org/10.22331/q-2020-11-17-364)

### Beyond fixed Markovian gate sets

9. Pollock, F. A., Rodríguez-Rosario, C., Frauenheim, T., Paternostro, M., & Modi, K. (2018). “Non-Markovian quantum processes: Complete framework and efficient characterization.” *Physical Review A*, 97, 012127. [arXiv](https://arxiv.org/abs/1512.00589) · [DOI](https://doi.org/10.1103/PhysRevA.97.012127)
10. Rudinger, K., et al. (2021). “Experimental Characterization of Crosstalk Errors with Simultaneous Gate Set Tomography.” *PRX Quantum*, 2, 040338. [arXiv](https://arxiv.org/abs/2103.09890) · [DOI](https://doi.org/10.1103/PRXQuantum.2.040338)
11. White, G. A. L., Pollock, F. A., Hollenberg, L. C. L., Modi, K., & Hill, C. D. (2022). “Non-Markovian Quantum Process Tomography.” *PRX Quantum*, 3, 020344. [arXiv](https://arxiv.org/abs/2106.11722) · [DOI](https://doi.org/10.1103/PRXQuantum.3.020344)
12. Li, Z.-Z., Mizera, A., Zou, J., Zhang, X., & Xiang, G.-Y. (2024). “Non-Markovian quantum gate set tomography.” *Quantum Science and Technology*, 9, 025027. [arXiv](https://arxiv.org/abs/2307.14696) · [DOI](https://doi.org/10.1088/2058-9565/ad3d80)

### Cross-cutting model failures

13. van Enk, S. J., & Blume-Kohout, R. (2013). “When quantum tomography goes wrong: drift of quantum sources and other errors.” *New Journal of Physics*, 15, 025024. [DOI](https://doi.org/10.1088/1367-2630/15/2/025024)
14. Wood, C. J., & Gambetta, J. M. (2018). “Quantification and characterization of leakage errors.” *Physical Review A*, 97, 032306. [DOI](https://doi.org/10.1103/PhysRevA.97.032306)

---

## Revision posture

### Comparatively secure

- standard tomography は reference-model dependent である。
- self-consistent/GST は gate set を jointly estimate する。
- GST は gauge modulo で identifiable である。
- gauge と model misspecification は別問題である。
- operational gauge-free tomography は quotient / operational target を採る。
- broader temporal models は異なる scope を持つ。

### Interpretive synthesis

- A → B/C transition を boundary relocation と記述すること。
- resolution types と edge types を一つの ledger に並べること。

### Working hypothesis

- 同じ ledger が別分野または real protocol audit で診断価値を持つこと。

### Rejected in this case

- gauge から non-Markovianity へ至る recurrent linear deferral。
- gauge が unknown unique physical representative の存在を示すという読み。
- DR-4 fundamental non-closure。

### Open

- real protocol audit または第二科学分野で Erasure Test を越え、organizational value 以上を示すか。

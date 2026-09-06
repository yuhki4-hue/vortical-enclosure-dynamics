# Adversarial Review — Deferred Resolution Case 01

## GST lineage: tomography → self-consistency → gauge → model adequacy

- **Review status:** adversarial / correction-first / concept-preservation not assumed
- **Date:** 2026-08-16
- **Primary target:** [`deferred_resolution_case_01_gst.md`](./deferred_resolution_case_01_gst.md)
- **Context checked:** [`tool_truth_absence_working_note_v0.3.md`](./tool_truth_absence_working_note_v0.3.md), [`quantum_identifiability_prior_art_network.md`](./quantum_identifiability_prior_art_network.md), [`tool_truth_absence_v0.2_to_v0.3_diff.md`](./tool_truth_absence_v0.2_to_v0.3_diff.md)
- **Review rule:** field-native literature controls; prior reviews are search inputs, not authorities

---

## 1. Overall verdict

### 1.1 最重要レビュー問い

> Deferred Resolution という新しいラベルを消しても、科学的内容・区別・診断・結論は完全に残るか。

**YES, ENTIRELY.**

standard QPT の trusted-SPAM dependence、Merkel et al. の joint estimation、GST の identifiability modulo gauge、gauge optimization、operational quotient、Markovian gate-set model の goodness-of-fit、process-tensor / instrument-set / crosstalk-specific model extension だけで、Case 01 の全技術的結論を再構成できる。

消えるのは、

- `resolution → relocation → reformulation` という共通図式、
- Stage A–E を一枚に並べる index、
- DR-0–DR-4 という独自 taxonomy、

だけである。新しい empirical distinction、theorem、diagnostic test、experiment-design decision、scope judgment は失われない。したがって本ケースにおける DR-1 は **presentation-level reclassification** であり、独立した methodological construct ではない。

### 1.2 Summary assessment

| Question | Verdict |
| --- | --- |
| **Technically sound?** | **Mostly yes.** 中心的 GST 技術内容は概ね正しい。ただし gauge の “physical equivalence” は強すぎ、Li et al. 2024 の書誌情報は誤っている。 |
| **Conceptually sound?** | **As a descriptive metaphor, yes; as an independent concept, no.** |
| **Overreach risk?** | **High if DR is capitalized, taxonomized, or treated as a methodological finding.** |
| **Publication value?** | **Low as original research.** 内部研究ノートまたは pedagogical synthesis としては有用だが、DR 固有の publishable contribution は示されない。 |

### 1.3 DR-1 を壊す最短ルート

最も強い単独攻撃は **Attack A — Ordinary model refinement** である。

```text
standard QPT with characterized SPAM
   → joint estimation when gate-generated SPAM is uncertain
   → identifiability only modulo gauge
   → quotient parameterization
   → goodness-of-fit and model-specific extensions
```

これは inverse problems、statistical identifiability、nuisance/reference uncertainty、quotient models、model checking、misspecification、model extension の通常語彙で尽くされる。Case の DR 定義がこの通常系列をそのまま DR-1 に含めるなら、DR は現象を識別していない。

第二の決定打は **Attack D — No recurrent pattern** である。A→B/C に一回の “relocation” を比喩的に認めても、gauge は quotient で閉じ、Stage E は gauge ではなく model adequacy から分岐する。一回の局所的 target change から一般 taxonomy を作る根拠はない。

---

## 2. Fatal issues

### 2.1 独立概念としての fatal issue

**Erasure Test に失敗しているのに DR-1 を肯定判定している。**

Case 自身が、

- strongest mundane interpretation が ordinary inverse-problem maturation である、
- field-native terminology で主要内容が既に得られる、
- missing check、protocol change、review advantage を示していない、
- Erasure Test を越えていない、

と認める。それでも DR-1 を “Best fit” とするため、null hypothesis が勝っても DR が残る判定設計になっている。

これは、Case を技術 review として読む場合の fatal error ではない。しかし **DR を独立方法論として保存する主張には fatal** である。構成概念が既存説明に対して排他的予測も追加診断も持たないからである。

### 2.2 技術内容に fatal issue はあるか

ない。GST の core account を無効にする技術的誤りは確認しなかった。修正すべき表現・書誌はあるが、主な技術結論は維持できる。

---

## 3. Major issues

### Major 1 — DR の判定規則が非識別的

現在の定義は、問題を仮定の下で解き、その仮定や scope を明示し、後続研究がより広い target を扱えば成立する。これはほぼ全ての model-based science に当てはまりうる。

「後続問題が出ただけでは不十分」という但し書きも弱い。`論理的・実験的に接続する`、`downstream scope を制限する`、`scope boundary` は、通常の model conditionality に常に見つけられる。DR-1 の positive criterion と ordinary refinement の negative criterion が分離されていない。

### Major 2 — Null A は null になっていない

Case は Ordinary refinement を strongest mundane interpretation としながら、それと両立する DR-1 を採る。Null A が成立した時に本仮説を棄却する規則がないため、Null A は競合仮説ではなく DR の別記述になっている。

公平な判定なら、事前に次を置く必要があった。

> field-native model refinement だけで全 conclusions と decisions が再現されれば DR は棄却する。

この基準なら本ケースは棄却である。

### Major 3 — “Relocation” される同一対象が定義されていない

relocation には、何がどこからどこへ移ったかを同一視する基準が必要である。しかし A→B/C では、

- standard QPT の trusted gate-generated SPAM は joint estimand に入る、
- Merkel et al. の base state / measurement はなお固定される、
- mature GST では target が gate-set orbit に変わる、

ので、同一の boundary が保存されて移動したとは限らない。未知変数集合、reference structure、estimand、equivalence relation が同時に変わっている。

`calibration dependence remains/changes` と `which SPAM components are jointly estimated` と書けば足りる。`assurance boundary is relocated` は、現状では技術情報を追加しない空間比喩である。

### Major 4 — A→B/C の “YES locally” は強すぎる

Merkel et al. は、known-SPAM QPT の解決を引き継いで残余を別位置へ送ったのではなく、gate-generated SPAM が uncertain な **別の statistical model と estimand** を解く。standard QPT と self-consistent QPT の problem/solution relation は実在するが、それは assumption relaxation / joint estimation で十分に表現できる。

したがって A→B/C は DR 固有の positive instance ではない。`YES locally` は少なくとも **descriptive only** へ降格すべきである。ここを降格すると、Case 内に DR 固有の実証例は残らない。

### Major 5 — Gauge の分類に重複と過剰語がある

五分類の中心区別、すなわち gauge と misspecification を分ける点は正しい。しかし、

- observational non-identifiability と representational redundancy は独立な二分類というより、同じ invariance の inferential / representational 記述である。
- **physical equivalence** は強すぎる。data が示すのは、declared circuit family に関する **operational indistinguishability / empirical equivalence** である。
- gauge-related representatives が同一の ontology を表すかは、tomographic likelihood だけでは決まらない。

推奨置換は、`physical equivalence` → `operational equivalence under the declared experiment algebra` である。

### Major 6 — “Gauge problem closes” の scope をさらに限定すべき

Di Matteo et al. は experimental observables を parameters とする operational tomography により representation ambiguity を address / solve する（[Di Matteo et al. 2020](https://doi.org/10.22331/q-2020-11-17-364)）。したがって quotient resolution という読みは妥当である。

ただし閉じるのは、**指定 operational model 内の redundant parameterization problem** である。finite-data uncertainty、choice of experiment algebra、model dimension、composition assumption、gauge-variant target metrics の運用問題、外部 reference の導入可能性まで全て閉じるわけではない。

また「absolute representative は unobservable」と存在論的に言い切るより、「declared circuit data から identifiable でない」と限定すべきである。

### Major 7 — Stage E は “Stage” というより複数の別枝

process tensor、instrument-set tomography、simultaneous GST、leakage/drift models は同一 target の順次改良ではない。変更する system boundary、intervention set、temporal structure、dimension、locality assumption が異なる。

Case はこの点を最終的には認めるが、Stage A→E という表題・構造自体が一 lineage の印象を残す。process-tensor framework は gauge-free tomography より前に展開し、crosstalk GST は別の scope-specific branch である。Stage E は `Related model extensions` へ改称する方が正確である。

### Major 8 — “Ontological closure” は本ケースの object でない

Weak Claim C の `operational success と ontological closure は同じ尺度でない` は、対象文献が ontological closure を定義、推定、測定していない以上、本ケースから支持できない。

少なくとも次へ分解すべきである。

- **model closure:** specified model family が data を十分説明するか。
- **representational uniqueness:** parameter representative が一意か、quotient のみか。
- **interpretive uniqueness:** operational model から一つの ontology が選ばれるか。

GST 文献が直接扱うのは主に前二者である。Weak Claim C は削除するか、`GSTの operational fit と interpretive uniqueness は異なる問いである` という初等的な scope statement に落とすべきである。

### Major 9 — DR taxonomy は ordinal scale でない

DR-0–DR-4 は同一軸の強度段階ではない。

- DR-1 は一回の existential relation。
- DR-2 は recurrence の回数・分布。
- DR-3 は cross-formalism structural stability と diagnostic utility。
- DR-4 は modal impossibility theorem。

frequency、structural generality、practical utility、logical impossibility を一列にしている。DR-4 はとくに別種類の claim であり、DR-3 の強い版ではない。この taxonomy は弱い DR-1 を大きな理論の第一段階に見せる装置になりうる。

本ケースで DR-1 しか残らないなら taxonomy は不要である。将来残す場合も、`recurrence`、`formal invariance`、`diagnostic effect`、`impossibility` を独立軸に分けるべきである。

### Major 10 — Category-error prevention は独自方法論でない

Case が防ぐとする三つの誤りは、既存 literature が既に明示する。

1. conditional QPT を unconditional と読まない。
2. GST gauge を physical error / misspecification と混同しない。
3. non-Markovian extension を Markovian GST の全面的失敗と読まない。

これらを一枚に並べる価値は **indexing / pedagogy** にはある。しかし、チェックを新設せず、判定を変えず、実験を変えない限り methodology ではない。

---

## 4. Minor issues

1. **Li et al. 2024 の書誌が誤り。** 正しい著者は Ze-Tong Li, Cong-Cong Zheng, Fan-Xu Meng, Han Zeng, Tian Luan, Zai-Chen Zhang, Xu-Tao Yu、掲載は *Quantum Science and Technology* **9, 035027** (2024) である。Case の `Li, Z.-Z., Mizera, Zou, Zhang, Xiang` と `025027` は修正が必要（[arXiv:2307.14696](https://arxiv.org/abs/2307.14696)）。
2. **“calibration-free” の限定は概ね適切。** ただし `no pre-calibrated SPAM within the modeled gate set` と書くのが最も安全で、laboratory traceability や control-label semantics まで calibration-free と読ませない方がよい。
3. **GST goodness-of-fit。** `model violation を検出する` は finite-sample statistic と regularity / reference model に条件づく。Case は概ね限定しているが、「検出」を無条件の原因診断と読ませない注意を維持すべきである。
4. **Operational homomorphism と Markovianity。** Di Matteo et al. の compositional homomorphism assumption は history-independent composition を制限するが、一般的な non-Markovianity 全分類との同一視は避け、論文の exact model promise として記述する方がよい。
5. **Historical influence。** self-consistent QPT から mature GST への genealogy は review に依存する部分がある。Case 自身が Open literature check として残したのは適切である。
6. **Stage E の “complete”。** process-tensor tomography の completeness は指定 time frame と adequate interventions に相対する。Case はこの限定を置いており、維持すべきである。

---

## 5. Technical GST audit

### Stage A — Standard tomography

**Verdict: technically sound.**

- state tomography が characterized measurement model、detector tomography が characterized probes、standard QPT が characterized preparation/measurement に依存するという整理は妥当である。
- informational completeness を specified candidate/model class 上の injectivity とする点も妥当である。
- repeated data は sampling error を減らせても fixed SPAM systematic error を除かない、という区別も正しい。
- standard QPT の scope を「条件付き inverse problem」と明示しており、GST の必要性を誇張していない。

修正は不要だが、`trusted` は metaphysical certainty でなく calibrated/characterized within uncertainty という operational meaning だと一度明記するとよい。

### Stage B — Self-consistent process tomography

**Verdict: technically sound; DR interpretation not established.**

Merkel et al. は、preparation / measurement に使う gates の systematic error が standard QPT を bias し、oversampling では修正できないことを問題にし、gate library 全体の self-consistent likelihood fit を提案する。また target 周りで linearize する（[Merkel et al. 2013](https://arxiv.org/abs/1211.0322)）。

Case が base \(\rho_0\) と \(M_0\)、local linearization、time stability を residual とすることは妥当である。2013 paper が gauge を成熟 GST と同じ形で前景化していないことも明記しており、後世語彙の遡及投影を概ね避けている。

問題は技術でなく `YES locally` という DR 判定である。field-native には `different estimand under weaker reference assumptions` で尽くされる。

### Stage C — GST

**Verdict: technically sound with terminology correction.**

GST が state preparation、measurement、gates を simultaneous / self-consistent に characterize し、pre-calibrated SPAM に依存しないことは review の中心記述である（[Nielsen et al. 2021](https://doi.org/10.22331/q-2021-10-05-557)）。fiducials、germs、long sequences、likelihood fit の概要も妥当である。

gauge transform が全 circuit probabilities を保存し、estimate が gauge orbit までであること、gauge optimization が target-relative reporting に使われることも正しい。実験 GST 文献も gauge-related gate sets が同じ probabilities を与え、多くの metrics が gauge-variant であることを明示する（[Blume-Kohout et al. 2017](https://doi.org/10.1038/ncomms14485)）。

fixed-dimensional Markovian gate-set model と goodness-of-fit、fit failure が特定物理原因を一意診断しないという記述も適切である。修正点は `physical equivalence` を `operational indistinguishability under the modeled circuit family` に落とすことだけである。

### Stage D — Operational, gauge-free tomography

**Verdict: core interpretation correct.**

Di Matteo et al. は experimental observables を model parameters とすることで ambiguity in representation、すなわち gauge problem を扱う。Case の quotient / operational target という理解は正しい。

`gauge problem closes` は、

> specified operational model の inferential parameter redundancy が quotient parameterization で除かれる

という限定ならよい。absolute representative の ontology が存在しないことまでは示さない。示すのは declared data からそれを選べないことである。

### Stage E — Non-Markovian and contextual extensions

**Verdict: individual descriptions are sound; a single Stage is conceptually misleading.**

- process tensor は multitime interventions と memory-bearing process の operational target を与える（[Pollock et al. 2018](https://doi.org/10.1103/PhysRevA.97.012127)）。
- process-tensor tomography は指定 time frame の non-Markovian dynamics を characterize する（[White et al. 2022](https://doi.org/10.1103/PRXQuantum.3.020344)）。
- simultaneous GST は crosstalk-specific characterization を行う（[Rudinger et al. 2021](https://doi.org/10.1103/PRXQuantum.2.040338)）。
- IST は imperfect instruments と system–environment correlations を self-consistently扱う non-Markovian GST extension として提示される。

よって individual content は妥当である。しかしこれらは gauge-free target の次に同じ residual を解く一 Stage ではない。`Related extensions beyond a fixed Markovian gate-set model` として並列配置すべきである。

---

## 6. DR concept audit

### 6.1 Definition audit

| Question | Verdict | Reason |
| --- | --- | --- |
| 1. 定義は広すぎるか | **YES** | model-relative solution の後に scope condition が残るだけで適用できる。 |
| 2. ordinary scientific progress の大半を含むか | **YES, potentially** | assumption relaxation、new nuisance parameters、model selection、domain extension がほぼ全て該当しうる。 |
| 3. 「後続問題だけでは不十分」は十分強いか | **NO** | “connected” と “scope-limiting” の operational test がない。 |
| 4. scope boundary で何でも該当しないか | **Nearly yes** | 全有限モデルには domain、parameterization、sampling、instrumentation の scope がある。 |
| 5. falsifiable concept か | **Not in its current form** | Null A が成立しても DR-1 が残るため、negative outcome の判定規則がない。 |

概念を将来再検査するなら、少なくとも次を事前登録する必要がある。

1. 移送される dependency \(D\) と、前後での同一性 criterion。
2. \(D\) がどの variable / equation / experimental obligation からどこへ移るか。
3. ordinary refinement と異なる予測または audit decision。
4. DR 語彙を使わない control reconstruction。
5. DR 判定を棄却する observable condition。

これがない限り、Deferred Resolution は falsifiable classification でなく retrospective narrative である。

### 6.2 Is “relocation” necessary?

比較対象は次である。

**A:** `calibration dependence remains`  
**B:** `the assurance boundary is relocated`

B が A に追加しうる最良の内容は、unknown/reference の区切りが estimand の変更に伴って再配置される、という視覚化である。しかし Case 01 では、どの calibration dependence が保存され、どれが除去され、どれが別の base reference として残るかを説明するには、結局 field-native description が必要になる。

```text
standard QPT:
  gate-generated SPAM = treated as characterized input

self-consistent QPT/GST:
  gate-generated SPAM = jointly estimated
  base/model/design assumptions = retained or changed
```

この二行が全技術内容を持つ。`boundary relocated` は追加 theorem、error term、uncertainty propagation rule を与えない。現状では **比喩 / index** である。

### 6.3 Null-hypothesis fairness

| Null | Case での扱い | Adversarial verdict | Explanatory power |
| --- | --- | --- | --- |
| **A Ordinary refinement** | strongest mundane interpretation と認めるが DR-1 と両立させる | 不公平。成立時に DR を棄却しないため null でない | **Overall strongest** |
| **B Different problem** | Stage E と gauge の分離に採用 | 概ね公平。ただし A→B/C にもより強く適用可能 | Strong for cross-stage chain |
| **C Solved by quotient** | gauge について強く採用 | 公平かつ決定的 | **Decisive for gauge branch** |
| **D Historical sequencing only** | D→E の単純系列を棄却 | 公平 | Strong against A→E lineage |
| **E Reviewer-imposed narrative** | risk を認めるが DR-1 は残す | 十分に帰結へ反映されていない | Strong meta-explanation |

単一の best null は **Null A**。ただし full chain に対する最強説明は A+B+C+D/E の複合である。

### 6.4 DR taxonomy audit

1. **Ordinal scale として不適切。** 異なる次元の claims を一列にする。
2. **DR-1→2→3 は単純な強度増加でない。** recurrence と structural invariance と utility は別軸である。
3. **DR-4 は category error。** fundamental non-closure は一般不可能性定理であり、descriptive relocation の最大値ではない。
4. **theorem-like appearance の risk がある。** DR-4 を頂点に置くことで DR-1 が未成熟な大理論の初段に見える。
5. **本ケースだけなら taxonomy は不要。** `one descriptive change in estimand/reference structure` で足りる。

推奨は DR-0–4 を削除し、必要なら独立評価軸へ分解することである。

| Axis | Question |
| --- | --- |
| Dependency persistence | 同じ dependency が前後に実在するか |
| Recurrence | 同じ形式の transition が複数回生じるか |
| Formal invariance | model family を越えた structure-preserving map があるか |
| Diagnostic effect | test、decision、design を変えるか |
| Modal claim | closure impossibility theorem があるか |

Case 01 が満たすのは、せいぜい最初の軸の弱い記述だけである。

---

## 7. Weak Claims A–D verdict

| Claim | Verdict | Review |
| --- | --- | --- |
| **A. 局所識別を解いても model scope / equivalence boundary が残る場合がある** | **SUPPORTED + TOO TRIVIAL** | model-relative inference と quotient identifiability の標準的事実。DR を支持しない。 |
| **B. 科学的解決は境界の消去だけでなく明示化・移送・再定義として進む** | **TOO BROAD + MISLEADING** | `明示化` と `target redefinition` は本ケースにあるが、`移送` の identity criterion がない。科学一般への拡張も未支持。 |
| **C. operational success と ontological closure は同じ尺度でない** | **UNSUPPORTED + MISLEADING** | ontological closure が未定義・未測定。GST literature の object ではない。 |
| **D. 何を一意 target とするかの変更で科学的進歩が成立する場合がある** | **SUPPORTED + TOO TRIVIAL** | gauge orbit / quotient model の標準的 target correction。独自診断ではない。 |

### 7.1 “Ontological closure” recommendation

**削除を推奨する。** 少なくとも本ケースの evidential vocabulary に置くべきでない。

代替は次の三分解である。

| Term | GST case で問えること |
| --- | --- |
| **Model adequacy / closure** | fixed gate-set family が observed circuit behavior を十分表すか |
| **Representational uniqueness** | parameter point が一意か、gauge orbit までか |
| **Interpretive uniqueness** | operational model が一つの ontology を選ぶか |

第一・第二は GST / tomography 文献で扱える。第三は別の foundations / philosophy question であり、本ケースの data analysis から直接導かれない。

---

## 8. Erasure Test result

### Pass 1 — 固有語の消去

次を全て削除する。

- Deferred Resolution / DR-0–DR-4
- boundary relocation
- assurance provenance
- backgrounding / handoff（固有 audit label として）
- resolution ledger

### Pass 2 — GST field-native vocabulary のみで再構成

> Standard quantum process tomography estimates a channel conditional on characterized state preparation and measurement. Systematic errors in gates used to generate those preparations and measurements bias the inferred channel and are not removed by oversampling. Self-consistent process tomography therefore fits a gate library jointly, under its own fixed base-SPAM, stability, and local-model assumptions. Mature GST estimates state preparation, measurement, and gates together from structured circuit data; the gate set is identifiable only up to similarity transformations that preserve all circuit probabilities. Gauge optimization chooses a convenient representative for reporting and target-relative metrics, while operational gauge-free tomography parameterizes identifiable experimental quantities or the quotient directly. Separately, GST goodness-of-fit assesses whether a fixed-dimensional Markovian gate-set model fits the data. Rejection does not identify a unique physical cause. Drift, leakage, crosstalk, context dependence, and memory require cause-specific diagnostics or enlarged model classes such as simultaneous GST, process tensors, or instrument-set tomography. These extensions do not make gauge an unresolved physical error and do not retroactively invalidate GST within its stated scope.

### Pass 3 — 何が失われたか

| Lost item | Scientific loss? |
| --- | --- |
| A→E の一枚図 | No; visualization only |
| “Relocation” という共通動詞 | No; metaphor/index only |
| DR-0–DR-4 labels | No;むしろ異種 claims の混線が減る |
| Stage間の比較表 | Partly pedagogical, but field terms で再作成可能 |
| Technical distinction | None |
| Diagnostic test | None |
| Experiment-design recommendation | None |
| Changed inference or conclusion | None |

### Erasure verdict

> **DR is not yet a methodological construct.**

本ケースで確認できる価値は diagram、indexing、pedagogical summary に限られる。

---

## 9. Strongest mundane reconstruction

DR 語彙を用いない最も強い再構成は次である。

### 9.1 Standard model conditionality

ordinary QPT は characterized preparation / measurement を forward model の一部として固定し、その条件下で unknown process を推定する。systematic SPAM error は statistical noise でなく model error を生む。

### 9.2 Self-consistent estimation

gate-generated SPAM を固定 reference とみなせない場合、推定対象を gate library 全体へ拡張し、circuit probabilities に対して joint likelihood を fit する。これは unknown nuisance/reference operations を estimand へ含める model change である。

### 9.3 Quotient identifiability

state、measurement、gates を相対的に推定すると、simultaneous similarity transformations が全 accessible probabilities を保存する。したがって identifiable object は parameter point でなく gauge orbit である。

### 9.4 Gauge handling

gauge optimization は target comparison と reporting のため representative を選ぶ。operational gauge-free tomography は gauge-invariant observables / quotient coordinates を直接 parameterize し、redundant inference を避ける。

### 9.5 Model checking

gauge と独立に、likelihood / goodness-of-fit は fixed-dimensional Markovian gate-set family が data に適合するかを検査する。fit failure は model inadequacy を示唆するが、drift、leakage、crosstalk、memory の原因同定ではない。

### 9.6 Model extension

各 failure mode に応じて、time dependence、larger Hilbert space、simultaneous crosstalk model、process tensor、instrument set 等へ model/target を拡張する。これは earlier model の domain extension であり、gauge problem の継続ではない。

この再構成で Case 01 の科学的内容は全て残る。

---

## 10. Does DR-1 survive?

### Verdict: YES, BUT PRESENTATION-ONLY

`DR-1` を、

> ある conditional method から、assumptions の一部を estimand に含む別 method へ移ることを一枚に表示する非公式ラベル

とだけ定義すれば、A→B/C の記述として残せる。

しかし、

- field-native reconstruction を越えない、
- null を識別しない、
- prediction/test/decision を追加しない、
- recurrence を示さない、

ため、**研究概念としては survive しない**。保存するとしても glossary の作業語または comparison-case 用の provisional search label に限る。現段階で名詞を大文字化し taxonomy を与えるべきでない。

結論を二値化すれば、

> **DR-1 as description: survives. DR-1 as methodology: no.**

---

## 11. Recommended v0.3 impact

### Verdict: Minor revision

新概念を加えるためでなく、negative case result を correction trail に残すための最小改訂を推奨する。

### v0.3 に追加する最小の一段落

> **[NEGATIVE CASE RESULT — GST]** GST 系列では、standard tomography の reference dependence、self-consistent joint estimation、identifiability modulo gauge、quotient parameterization、goodness-of-fit、model-specific extension という field-native 語彙だけで全技術的結論を再構成できた。`Deferred Resolution / boundary relocation` は新しい check、推論、実験設計を与えず、DR-1 は presentation-level label に留まった。したがって現段階では独立方法論として採用せず、事前登録した対照ケースで field-native reconstruction と異なる診断結果を示すまで作業仮説に限定する。

これ以上の追加は不要である。v0.3 の assurance-provenance framework 自体もすでに Erasure Test と `methodological usefulness unproven` を持つため、DR taxonomy を導入してはならない。

---

## 12. Best next comparison case

### Choice: Metrological traceability

三候補のうち最も diagnostic なのは **metrological traceability** である。

| Criterion | Why metrology is strongest |
| --- | --- |
| DR-0 / closure の対照 | SI realization、traceability chain、uncertainty budget により、依存が明示的に閉じられる事例を持ちうる。 |
| DR-2 候補 | calibration hierarchy が複数段で現れるため、もし recurrent relocation が実在するなら捕捉しやすい。 |
| Field-native literature | VIM、GUM、BIPM/JCGM、NMI literature が強く、generic metaphor と厳密比較できる。 |
| Storytelling resistance | calibration chain、reference standard、uncertainty propagation、comparability という operational records がある。 |
| Erasure power | DR を消して traceability/uncertainty だけで全て残れば、DR を強く棄却できる。 |

system identification は GST と同じ realization/quotient structure に近すぎ、同じ再分類を繰り返す可能性が高い。cosmology は model misspecification と underdetermination の哲学的物語へ逃げやすい。

次ケースは、結果が DR-0 でも DR-2 でもよいよう、次を事前登録すべきである。

1. traceability literature だけで得られる baseline map;
2. “同じ dependency が移送された”と数える identity criterion;
3. DR によって変わる audit decision;
4. DR を棄却する条件;
5. standard uncertainty budget / assurance case との head-to-head comparison。

---

## 13. Final one-sentence judgment

> **GST Case Study は、inverse problems・self-consistent tomography・gauge quotient・model checking・model extension の既存語彙では見えなかった科学的内容を発見しておらず、Deferred Resolution は現段階では ordinary scientific refinement の presentation-level 再命名として独立概念から外し、せいぜい次の対照試験までの暫定検索ラベルとしてのみ残すべきである。**

---

## Reviewer correction ledger

| Item | Status | Required action |
| --- | --- | --- |
| Standard tomography characterization | Sound | None |
| Merkel et al. target / fixed base SPAM / linearization | Sound | Keep field-native description; downgrade DR inference |
| GST gauge orbit and gauge optimization | Sound | Replace “physical equivalence” with operational indistinguishability |
| Gauge vs misspecification | Sound and important | Keep |
| Operational quotient reading | Sound within specified model | Limit “closes” and “unobservable” claims to declared experiment/model |
| Stage E individual literature | Sound | Recast as parallel related extensions, not one stage |
| Li et al. 2024 bibliography | Incorrect | Correct authors and page 035027 |
| DR-1 classification | Descriptively possible, methodologically unsupported | Downgrade to presentation-only |
| DR-0–DR-4 taxonomy | Unsupported | Remove from methodological claims |
| Weak Claim C / ontological closure | Unsupported by case literature | Delete or decompose |

## Primary literature checked

1. Merkel, S. T., et al. (2013). “Self-Consistent Quantum Process Tomography.” *Physical Review A* 87, 062119. [arXiv](https://arxiv.org/abs/1211.0322) · [DOI](https://doi.org/10.1103/PhysRevA.87.062119)
2. Blume-Kohout, R., et al. (2017). “Demonstration of qubit operations below a rigorous fault tolerance threshold with gate set tomography.” *Nature Communications* 8, 14485. [Article](https://www.nature.com/articles/ncomms14485) · [DOI](https://doi.org/10.1038/ncomms14485)
3. Nielsen, E., et al. (2021). “Gate Set Tomography.” *Quantum* 5, 557. [Article](https://quantum-journal.org/papers/q-2021-10-05-557/) · [DOI](https://doi.org/10.22331/q-2021-10-05-557)
4. Di Matteo, O., et al. (2020). “Operational, gauge-free quantum tomography.” *Quantum* 4, 364. [Article](https://quantum-journal.org/papers/q-2020-11-17-364/) · [DOI](https://doi.org/10.22331/q-2020-11-17-364)
5. Pollock, F. A., et al. (2018). “Non-Markovian quantum processes: Complete framework and efficient characterisation.” *Physical Review A* 97, 012127. [arXiv](https://arxiv.org/abs/1512.00589) · [DOI](https://doi.org/10.1103/PhysRevA.97.012127)
6. Rudinger, K., et al. (2021). “Experimental Characterization of Crosstalk Errors with Simultaneous Gate Set Tomography.” *PRX Quantum* 2, 040338. [Article](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.2.040338) · [DOI](https://doi.org/10.1103/PRXQuantum.2.040338)
7. White, G. A. L., et al. (2022). “Non-Markovian Quantum Process Tomography.” *PRX Quantum* 3, 020344. [Article](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.3.020344) · [DOI](https://doi.org/10.1103/PRXQuantum.3.020344)
8. Li, Z.-T., Zheng, C.-C., Meng, F.-X., Zeng, H., Luan, T., Zhang, Z.-C., & Yu, X.-T. (2024). “Non-Markovian quantum gate set tomography.” *Quantum Science and Technology* 9, 035027. [arXiv](https://arxiv.org/abs/2307.14696) · [DOI](https://doi.org/10.1088/2058-9565/ad3d80)

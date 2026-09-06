# Adversarial Review (Claude Code) — Deferred Resolution Case 01

## GST lineage: tomography → self-consistency → gauge → model adequacy

- **Review status:** adversarial / concept-elimination-first / concept preservation not assumed
- **Reviewer:** Claude Code (Fable 5)
- **Date:** 2026-08-16
- **Primary target:** [`deferred_resolution_case_01_gst.md`](./deferred_resolution_case_01_gst.md)
- **Context checked:** [`tool_truth_absence_working_note_v0.3.md`](./tool_truth_absence_working_note_v0.3.md), [`quantum_identifiability_prior_art_network.md`](./quantum_identifiability_prior_art_network.md), [`tool_truth_absence_v0.2_to_v0.3_diff.md`](./tool_truth_absence_v0.2_to_v0.3_diff.md), [`scientific_identifiability_case_01_quantum.md`](./scientific_identifiability_case_01_quantum.md)
- **Review rule:** field-native literature controls; prior reviews (including the existing `deferred_resolution_case_01_gst_adversarial_review.md`) are search inputs, not authorities
- **Independent verification performed:** two primary-source checks (arXiv:2307.14696, arXiv:1211.0322); one confirmed a citation error, one remained inconclusive and is flagged as such

---

## 1. Overall verdict

### 1.1 最重要レビュー問い

> Deferred Resolution というラベルを消しても、科学的内容・区別・診断・結論は完全に残るか。

**YES, ALMOST ENTIRELY.**（完全 YES にしない理由は下記一点のみ）

Stage A–E の技術的結論は、既存語彙 — reference-conditional inversion、nuisance parameter の joint estimation、identifiability up to similarity transformation、quotient parameterization、goodness-of-fit による model checking、model expansion — で残らず再構成できる（§9 で実演）。消えるのは図式、索引、DR-0–DR-4 の梯子だけである。

「完全 YES」にしない唯一の理由は、消すと失われる**判断が一つある**からだ：Stage D→E に直接 edge が無いという発見（L598, L611）。ただしこれは DR 概念が生んだのではなく、**出版年を並べたことが生んだ**。年表は概念を必要としない。したがって残るのは概念の価値ではなく、書誌調査の価値である。

### 1.2 Summary assessment

| 問い | 判定 |
| --- | --- |
| **Technically sound?** | **概ね yes、二点の実質的欠陥あり**。gauge を「reporting convention」に格下げした点（§5-C）と、Li et al. の著者名が完全な誤り（検証済み） |
| **Conceptually sound?** | **記述的比喩としては yes、独立概念としては no**。定義が Box の反復モデル構築ループと外延的に一致し、識別力がない |
| **Overreach risk?** | **中〜高**。本文の自制は高水準だが、taxonomy の存在自体と「DR-1」という肯定形ラベルが、否定的結果を段階的成果に見せる |
| **Publication value?** | **原著研究としては低**。ただし GST lineage の assumption ledger としては、二つの修正後に内部教材の価値がある |

### 1.3 最も強い攻撃（Attack A′）

候補 A–E のうち最強は **Attack A の鋭化版**であり、これを **A′** と呼ぶ。

> **境界は解決によって生成されていない。解決前から仕様に含まれていた。**

根拠は本文自身の二つの自認である。

- Stage A について L218「依存は元 task の specification に含まれており、元 task が未解決だった証拠ではない」
- Stage D について L710「この boundary は quotient が新しく作ったのではなく、model specification に既に含まれていた」

**系列の最初の遷移と最後の遷移の両方で、境界が先在していたと本文が認めている。** 両端で先在するなら、中間だけが「移送」であるという主張は支えを失う。移動したのは境界ではなく**注意**であり、より正確には技術水準が「trusted reference の誤差 ≪ 被測定 gate の誤差」という前提が成り立たない領域へ入った、という regime の移動である。

これは Attack A（通常の refinement）より強い。A は「別の説明でも足りる」という代替説明の提示にとどまるが、A′ は「relocation という語に指示対象が無い」という**内部矛盾の指摘**である。第二に強いのは Attack D（反復なし）、第三が Attack E（narrative artifact、後述の通り本文で審理されていない）。

### 1.4 「relocation」という語は必要か

A「calibration dependence remains」と B「the assurance boundary is relocated」を比較すると、B が A に加えているのは (i) 空間的比喩、(ii) before/after の暗黙比較、の二つである。

(i) は装飾。(ii) には実質がある — Stage B では条件集合が実際に**交換**された（trusted-SPAM を落とし、stability・linearization・base-SPAM を加えた）。しかしこの交換には既存名がある：**nuisance parameter の promotion**（既知定数として条件づけていた量を、推定対象へ格上げする）。統計学は profile likelihood、marginal likelihood、Neyman–Scott 問題として一世紀近く扱っている。

したがって：**B は A に対して、比喩一つと、既に名前のある操作一つを加えているだけである。**「relocation」は「条件集合の交換」と書けば済み、書き換えた方が何が起きたかが明確になる。

---

## 2. Fatal issues

### 2.1 概念としての存立に関わる

```text
[Lines 47, 61–67]
Severity: FATAL
Category: Definition / Falsifiability

Issue:
DR の定義+5 条件は、Box (1976) の反復的モデル構築ループの各周回を
すべて満たす。条件 5「新しい target、equivalence、または model-class
problem として再定式化される」は選言が広すぎ、あらゆる model expansion が
第三項で自動的に該当する。反例を作ろうとしても、条件 3（残余が解決構造と
接続する）が同一実験内のほぼ全ての残余について自明に成立するため、
DR-0 に落ちる事例をこの定義から構成できない。

Why it matters:
本文が実際に DR-0 的判定（D→E の edge 不在）を下したとき、その判定は
定義からではなく出版年から得られた（L158, L539–547）。すなわち定義は
一度も識別作業をしていない。反証条件を持たない概念は研究仮説ではない。

Recommended action:
定義を捨てるか、条件 5 を「新 target が旧 target の quotient または
strict extension として構成でき、かつ旧解決の妥当性を取り消さない」等の
非選言的形へ絞る。絞った定義で Box ループの通常周回が除外されるかを
先に検査し、除外されないなら概念を破棄する。
```

### 2.2 文献整合性

```text
[Line 917]
Severity: FATAL
Category: Citation integrity
Verification: 独立確認済み（arXiv:2307.14696）

Issue:
Li et al. 2024 の著者名が完全に誤っている。本文は
「Li, Z.-Z., Mizera, A., Zou, J., Zhang, X., & Xiang, G.-Y.」と記すが、
arXiv:2307.14696 / QST 9, 025027 の実際の著者は
Ze-Tong Li, Cong-Cong Zheng, Fan-Xu Meng, Han Zeng, Tian Luan,
Zai-Chen Zhang, Xu-Tao Yu である。第一著者のイニシャルも Z.-T. が正しい。
第二著者以降は一人も一致しない。タイトル・誌名・DOI は正しい。

なお本文 L156/L446 の「instrument-set tomography」という記述は
**正しい** — 当該論文はタイトルが "Non-Markovian Quantum Gate Set
Tomography" だが、本文中で instrument set tomography (IST) を提案しており、
LIST / MLE-IST の二手法を与える。ここは本文に非がない。

Why it matters:
本ノートの唯一の主張価値は一次文献の正確な再構成である。著者名の
全面誤りは、他の 13 件の書誌についても独立検証を要求させる。

Recommended action:
L917 を訂正し、全書誌を再検証する。
```

---

## 3. Major issues

```text
[Lines 327–335, 591, 861]
Severity: MAJOR
Category: Quantum fact / Overclaim

Issue:
(a) 五分類の第 3 項を「physical equivalence」と命名しているが、これは強すぎる。
gauge 関連モデルが区別不能なのは「宣言された実験インターフェースに相対して」で
あり、本文自身が L331 でそう書いている。ならば名称は operational equivalence
または interface-relative empirical equivalence であるべきで、"physical" は
本ノートが他所で拒否している存在論的断定を名称に密輸入している。

(b) より重い問題として、gauge optimization を「reporting/target-comparison
convention」（L332, L591, L861）と分類するのは技術的に不正確である。gauge 変換は
完全正値性を保存しない。したがって GST の推定 gate set が張る「orbit」は、物理
モデル（CPTP 集合）の内部では自由な GL 軌道ではなく、その交わりを取ったものになる。
さらに現場が実際に報告し fault-tolerance 閾値と比較する量（diamond norm、
average gate fidelity）は gauge 変位量であり、gauge の選び方が閾値判定を動かす。

Why it matters:
(b) は本ケースの Stage D 判定を直撃する。quotient は identifiability 問題を
閉じるが、**現場が意思決定に使う量は gauge 不変ではない**ため、実務上の問題は
閉じていない。皮肉なことに、これは本ケースが探していた「解決に接続し、下流推論の
scope を制限する残余」の最良の候補であり、本文は自ら "convention" と呼んで
切り捨てた。DR を救う材料ではない（この論点も Nielsen et al. 2021 の gauge 節と
後続の gauge-invariant error metric 研究で field-native に扱われている）が、
技術監査の完全性を損なう。

Recommended action:
第 3 項を operational equivalence へ改称。gauge optimization の分類に
「decision-relevant reporting choice（CP 非保存と gauge-variant error metric の
ため、単なる可視化ではない）」を追加。Stage D の判定を「identifiability として
閉じる。報告・閾値判定の問題としては閉じない」と二分する。
```

```text
[全体、特に Lines 749–763, 893–923]
Severity: MAJOR
Category: Prior art

Issue:
本ケースの中心パターン — 「条件付きで解く → 適合を検査する → 不適合を診断する
→ モデルを拡張する → 新しい scope 境界が見える」 — には既に名前がある。

1. Box (1976) "Science and Statistics" の反復的モデル構築ループ。
   "all models are wrong" は、境界が消去されず明示・更新され続けることの
   元祖定式化である。Box–Hunter の学習ループも同じ。
2. Gelman & Shalizi (2013) の model checking → expansion サイクル。
3. Nuisance parameter theory（既知として条件づける vs 同時推定する）。
   Stage A→B は教科書的な nuisance promotion である。
4. Ljung の system identification 教科書の構成：model structure →
   identifiability（相似変換を除く一意性）→ estimation → validation →
   structure revision。**Stage A–E は一冊の教科書の章順に一致する。**
5. 計量学の traceability chain / GUM：保証を上位標準へ委譲する構造が
   制度化されている。

参照文献 14 件のうち、これらは一件も含まれない。

Why it matters:
DR-2（反復）と DR-3（分野横断の同型構造）が仮に達成されたとしても、
その到達点には既に Ljung Ch.4+Ch.16 と Box ループという先行統合がある。
すなわち DR の研究プログラムは、成功した場合の帰結も既知である。これは
DR-1 の弱さより重い — 上限が既に占有されている。

Recommended action:
§17 の strongest mundane interpretation に、Box ループ・nuisance parameter・
Ljung の章構成を名指しで加える。これらを加えた上で DR に残余価値があるかを
再判定する。
```

```text
[Lines 104–108, 39]
Severity: MAJOR
Category: Logic / Null testing

Issue:
Null E（reviewer-imposed narrative）が列挙されるだけで一度も審理されていない。
L39 と L106 に言及があるが、「GST の専門家はこれを一つの chain と見るか」を
検査する節が無い。しかも本文の §5・§12.1 が集めた証拠（process tensor が
gauge-free より先行、Stage E は adequacy から分岐）は、**Null E を支持する
方向の証拠**であり、本文はそれを Null D（historical sequencing）の下でのみ
処理している。

Why it matters:
Null E は概念全体を消す唯一の null である。それだけが審理されないのは、
null 設定の公平性を損なう。最も説明力が高い null は、本査読の判定では
**Null A（各遷移の説明）+ Null E（一系列に見える理由の説明）の連言**であり、
本文は A を部分的に、E を全く審理していない。

Recommended action:
Null E を独立節で審理する。最小の検査は、Nielsen et al. 2021 の
"Limitations"/"Related work" 節と Di Matteo et al. 2020 の導入部が、
本ケースと同じ連鎖を提示しているかの直接比較である（§21-6 の
Erasure benchmark を本文内で先に実行する）。
```

```text
[Lines 795–815]
Severity: MAJOR
Category: Taxonomy / Overclaim

Issue:
DR-0–DR-4 は単一の順序尺度ではない。
- DR-1 → DR-2 は**頻度**の増分（1 回 → 複数回）。
- DR-2 → DR-3 は**種類**の飛躍（分野横断の同型構造という構造的主張）。
- DR-3 → DR-4 は**様相**の飛躍（原理的不可能性という modal claim）。
三種の異なる量を一列の梯子に並べており、DR-4 は他の四つと同じ軸上にない。
加えて、データ点が一つしかない段階で五段階尺度を先に置くことは、概念に
研究プログラムの外観を与える足場としてはたらく。

Why it matters:
実質的な発見は「仮説した連鎖は成立しなかった」という否定的結果である。
それを「DR-1」という肯定形のラベルで報告すると、否定的結果が
「五段階中の第一段階を達成」と読める。ラベルが結果の符号を反転させる。

Recommended action:
taxonomy を削除する。DR-1 だけが残るなら梯子は不要であり（§13-5 の
指摘は正しい）、結果は「hypothesized chain not supported; one transition is
describable as a nuisance-parameter promotion」と符号どおりに書くべきである。
```

```text
[Lines 234, 249–251]
Severity: MAJOR（条件付き）
Category: Prior art / Logic — 未検証

Issue:
本文は Merkel et al. 2013 について「base ρ₀ と M₀ を固定」（L234）、
「gauge freedom として明示的には展開していない」（L251）とする。これが
DR-1 の時間構造を支えている：SPAM 問題を解いた段階では gauge がまだ
現れておらず、後に境界として現れた、という筋である。

本査読では原論文の該当箇所を確認できなかった（arXiv PDF・OSTI 文書とも
テキスト抽出に失敗）。abstract は "assumes nothing about the gates used for
preparation and measurement" および "linearize about the target" のみを述べる。
一方、GST 系の二次資料は「self-consistent な gate set 記述は本質的に gauge
自由度を導入する」と述べており、これが 2013 年時点で自覚されていたかは
本文の主張の成否を分ける。

Why it matters:
**もし Merkel et al. が同論文内で相似変換不変性に言及していたなら、
Stage B の「新 boundary」は同じ著者が同じ論文で述べた scope statement で
あり、時間をまたぐ relocation は存在しない。** その場合 DR-1 の最良事例が
消え、A′ 攻撃が全遷移に及ぶ。逆に言及が無ければ、本文の記述は正しい。

Recommended action:
PRA 87, 062119 の本文（特に likelihood 構成と再構成の一意性を論じる箇所）を
直接確認する。本ケースの中心判定が単一の未検証事実に依存している以上、
§21-1 の open check ではなく、判定の前提条件として明示すべきである。
```

```text
[Lines 39, 805–815, 853–889]
Severity: MODERATE
Category: Reporting / Overclaim

Issue:
§1.1 Result preview は「仮説の全系列を再構成できなかった」と正しく始まるが、
最終判定は「DR-1 — Weak relocation」という肯定的ラベルで閉じる。読者が
abstract と verdict だけを読むと、否定的結果が弱い肯定として伝わる。

Recommended action:
Case conclusion の第一文を「本ケースは仮説した連鎖を支持しなかった」に置き、
DR-1 の言及はその後に限定句付きで置く。
```

```text
[Lines 616–627]
Severity: MODERATE
Category: Redundancy

Issue:
§14 assurance provenance map の 7 列は、v0.3 の auditability 語彙を GST へ
写したものだが、行の内容はすべて §11 ledger と §13 edge ledger の再掲であり、
新しい判断を一つも生んでいない。「Interpretive」列は 5 行中 3 行が
「reconstruction 自体には不要」、2 行が「存在論的読みは別問題」で、
情報量がほぼゼロである。

Recommended action:
§14 を削除するか、Interpretive 列を落として §11 へ統合する。表の存在自体が
語彙の適用可能性の証拠に見えるが、適用しても判断が変わらないことは
むしろ Erasure Test の失敗証拠である。
```

```text
[Lines 300, 337–348]
Severity: MODERATE
Category: Scope

Issue:
Residual 2（model scope）で列挙される drift・leakage・crosstalk・memory・
context dependence は、GST の base model の異なる公理を壊す。本文は L486 で
「異なる model relation を壊し、別の diagnostic を要する」と正しく述べるが、
どの公理をどれが壊すかの対応が §10 の表（L474–485）にしかなく、Stage C の
Residual 2 では一括されている。

Recommended action:
Stage C の Residual 2 から §10 の表へ明示的に前方参照する。
```

```text
[Line 133]
Severity: MODERATE
Category: Method

Issue:
前回査読の「failure mode を一つの primary node へ排他配属せよ」という指摘を
採用せず cross-impact を保存する、と宣言している。この判断自体は擁護可能
（drift は実際に複数ノードを壊す）だが、その結果、監査台帳が「どこを見れば
よいか」を一意に指示しない状態が維持されている。§15.3 が cross-impact を
図示するのは良いが、**監査手順としては「drift は A/B/C/E のどこで検出されるか」
ではなく「drift を検出する責任はどの検査が負うか」を書かないと使えない。**

Recommended action:
cross-impact の保存は維持しつつ、各 failure mode に「検出責任を負う検査」を
一つ指定する列を §15.3 に追加する（所属ノードではなく検出責任の割当）。
```

---

## 4. Minor issues

- **L146**：D'Ariano & Lo Presti 2001 を「ancilla-assisted process tomography」と要約しているが、原題は "Imprinting Complete Information about a Quantum Channel on its Output State" で、faithful state を用いる定式化。参考文献欄（L898）は正しい原題を挙げており、本文要約との齟齬は軽微だが、本文側も原語に寄せる方が安全。
- **L317–323**：gauge 変換の式は正しい（ρ↦Bρ, E↦EB⁻¹, G↦BGB⁻¹ で回路確率 E G_k…G_1 ρ が不変）。検算済み。
- **L539**：process tensor を「submitted 2015; published 2018」と注記しているのは良い書誌姿勢（arXiv:1512.00589 → PRA 97, 012127）。Stage D→E の時系列反論はこの一点で成立しており、本ケース最良の実証部分。
- **L376–382**：Di Matteo et al. の G(B,H)=Hom(S,T(H))/∼ という記法は原論文の形式に沿うと思われるが、B（button set）の記号が式の左辺に現れて右辺に現れない。記法の説明不足。
- **L785**：Weak Claim C の評価で「文献は ontological closure を定義・測定しない」と自認しながら判定を PARTIALLY SUPPORTED としている。未定義項を含む命題は部分的にも支持されない（§7）。
- **L843–849**：Open literature checks はすべて literature-audit task と正しくラベルされている。7 番のみ「genuine research test」とされ、これは妥当。

---

## 5. Technical GST audit（Stage A–E）

### Stage A — 正確

state/detector/process tomography を別々の逆問題として立て、それぞれの trusted reference を明示する構成は正しい。ancilla-assisted が reference structure を消さない（L186）、detector calibration が別の characterized arrangement を要する（L186）という指摘はいずれも正確で、循環の所在を正しく特定している。IC・推定・有限標本の分離も正しい。

**DR 判定 PARTIAL は妥当だが、L218 の自認が A′ 攻撃の材料になっている。**

### Stage B — 概ね正確、一点未検証

standard QPT の bias が「oversampling では消えない systematic error」であるという記述（L226）は原論文の主張と一致する（abstract の "grossly inaccurate ... systematic error" と整合）。「linearize about the target」の制約も原論文どおり（abstract で確認）。base ρ₀/M₀ 固定と gauge 非展開の二点は未検証（§3 の条件付き MAJOR 参照）。

**後世語彙の遡及投影を避けようとする姿勢（L251）は方法論的に正しく、本ケースの美点。**

### Stage C — 正確だが gauge の性格づけに欠陥

gauge 変換式は正しい。fiducials/germs による informational + amplificational completeness、long-sequence による感度向上、GOF による model violation 検出の三点整理は GST review に忠実。**diagnostic resolution が原因を特定しない（L313, L339）という指摘は正しく重要。**

欠陥は §3 に挙げた二点（physical equivalence の命名、gauge optimization を convention に格下げ）。equivalence boundary と adequacy boundary を「一つの残る未知へまとめてはならない」（L348）は本ケース最良の技術的判断。

### Stage D — 判定が clean すぎる

quotient resolution + reparameterization という性格づけは正しく、「unique underlying matrix representative を発見したのではない」（L402）は正確。しかし「NO for gauge as a deferred problem」は、identifiability の層では正しく、**報告・閾値判定の層では成立しない**（§3 参照）。Null C を支持する結論自体は維持されるが、「gauge problem closes」と無条件に言うのは避けるべきである。

### Stage E — 整理は妥当、ただし Stage 名が誤解を招く

process tensor（Pollock）、instrument set（Li）、simultaneous GST（Rudinger）、leakage、drift を「一つの generic non-Markovianity にまとめない」（L434）、それぞれ異なる model relation を壊す（L486）という扱いは正確で、この節が本ケースで最も丁寧である。

**ただし「Stage E」という連番自体が、本文が否定した線形性（L502, L611）を版面上で再導入している。** Stage D と Stage E は同じ列に並べるべきではなく、§12.2 の分岐図の形が正しい。

---

## 6. DR concept audit

### 6.1 定義

§2.1 の Fatal issue のとおり、Box ループと外延一致。5 条件のうち実際に働くのは条件 3 のみで、それも同一実験内の残余にはほぼ自明に成立する。**反証不能。**

### 6.2 Taxonomy

§3 の MAJOR のとおり、頻度・構造・様相という三種の量を一列に並べており順序尺度として不成立。DR-1 だけが残るなら不要。

### 6.3 Nulls

| Null | 審理状況 | 判定 |
| --- | --- | --- |
| **A** Ordinary refinement | 部分審理 | strongest mundane interpretation として認めるが、category-error prevention の残余価値が A の下で再検査されていない。「条件を明示せよ」は A に完全に含まれる |
| **B** Different problem | 公平に審理 | D→E の拒否に反映済み |
| **C** Solved by quotient | 公平に審理 | Stage D で強く支持、判定に反映済み |
| **D** Historical sequencing | 公平に審理 | 年表により実際に機能した |
| **E** Reviewer-imposed narrative | **未審理** | 概念全体を消す唯一の null が一行言及のみ |

**最も説明力が高いのは A+E の連言。** A が各遷移を説明し、E が「一系列に見える理由」を説明する。

### 6.4 概念が実際に行った識別作業の総量

**一件**（D→E の edge 不在）。その一件は出版年の比較で得られた。

---

## 7. Weak Claims A–D verdict

| Claim | 判定 | 理由 |
| --- | --- | --- |
| **A** 局所識別を解決しても model scope / equivalence boundary が残る | **SUPPORTED + TOO TRIVIAL** | 「モデルには仮定がある」以上の内容がない。本文自身の但し書き（L773「残るは新造を意味しない」）が残った内容をさらに空にする。この形では監査指針として機能しない |
| **B** 解決は消去だけでなく明示化・移送・再定義として進む | **TOO BROAD + 部分的に UNSUPPORTED** | 「明示化」「再定義」は支持され、かつ Box ループの再記述。「移送」は A′ 攻撃により未支持 — 本文が両端で境界の先在を認めている。三つの動詞のうち一つが未支持のまま連言で提示されている |
| **C** operational success と ontological closure は同じ尺度ではない | **MISLEADING** | 「ontological closure」は本ケースの文献が定義も測定もしない語であり（本文 L785 が自認）、未定義項を含む命題は PARTIALLY SUPPORTED になり得ない。削除を推奨 |
| **D** 進歩は target 変更で成立することがある | **SUPPORTED + TOO TRIVIAL** | 正しいが、realization theory（相似変換を除く一意性）、因子分析（回転の不定性）、GST（gauge）で標準。本文も L791 で GST の既知内容と認める |

### 7.1 「ontological closure」の扱い

**削除を推奨する。** 分解すると三層になり、分解した瞬間に主張が消える。

1. **representational uniqueness** — gauge の問題であり、**定理により決着済み**（一意な representative は存在しない）。
2. **model-class uniqueness** — 経験的に未決だが、これは model adequacy であって closure ではない。
3. **interpretive uniqueness** — 本ケースの文献が扱っていない。

Weak Claim C を維持するなら (1) について書くべきで、その場合「operational success が増しても representational uniqueness は増さない」となり、gauge 文献がすでに述べていることの反復になる。**未定義語を残すことによってのみ、この claim は非自明に見えている。**

---

## 8. Erasure Test result

**Pass 1（固有語削除）**：Deferred Resolution、boundary relocation、assurance provenance、backgrounding、handoff、DR-0–DR-4 を削除。

**Pass 2（field-native 再構成）**：§9 に全文。

**Pass 3（失われたもの）**：

| 項目 | 失われるか |
| --- | --- |
| 図式 `resolution → relocation → reformulation` | 失われる |
| Stage A–E を一枚に並べる索引 | 失われる |
| DR-0–DR-4 ラベル | 失われる |
| §14 assurance provenance 表 | 失われる（ただし判断を生んでいないので損失ゼロ） |
| empirical distinction | **失われない** |
| theorem / 数学的結果 | **失われない** |
| diagnostic test | **失われない** |
| experiment-design decision | **失われない** |
| scope judgment | **失われない** |
| D→E edge 不在の発見 | **失われない**（年表由来） |

**判定：DR is not yet a methodological construct.** 失われるのは diagram、indexing、pedagogical summary の三つのみで、これは本文の §14 が予告した失敗条件そのものである。

---

## 9. Strongest mundane reconstruction（DR 語彙なし）

> 量子過程トモグラフィは、特性づけ済みの状態準備と測定を条件として、チャネルを推定する逆問題である。準備・測定に用いる操作の誤差が被測定過程の誤差と同程度になる領域では、この条件づけが成り立たず、SPAM 誤差が推定チャネルへ誤帰属される（Merkel et al. 2013）。self-consistent tomography と GST はこれに対し、準備・測定・ゲートを同時推定パラメータとして扱う — 統計学の語彙では、既知定数として条件づけていた撹乱母数を推定対象へ格上げする操作である。回路確率は gauge 不変な組合せにしか依存しないため、この同時モデルは相似変換を除いてのみ識別可能であり、識別対象は gauge 軌道になる。これは状態空間実現が相似変換を除いてのみ一意である（Kalman）のと同じ構造である。実務では gauge 最適化により代表元を固定するが、完全正値性は gauge 変換で保存されず、報告される誤差量（diamond norm など）も gauge 変位量であるため、代表元の選択は報告上の決定を含む。Di Matteo et al. (2020) はこれに対し、商を作用素的に接近可能な量で直接パラメータ化し、冗長性を推論対象から除く。これとは独立に、GST の固定・Markov 的・文脈非依存な gate-set モデルは検査可能なモデルであり、適合度検定がモデル違反を検出する — ただし原因は特定しない（Blume-Kohout et al. 2017）。検出された違反は、drift モデル、leakage モデル、simultaneous/crosstalk GST、process tensor、instrument set といった、それぞれ別の軸に沿ったモデル拡張を動機づける。これは identifiability → estimation → model checking → model expansion という標準的な循環であり、Box (1976) の反復的モデル構築ループ、および Ljung の system identification 教科書の章構成と同型である。

**この再構成で失われたもの：ない。** 加えて、DR 版では見えなかったものが二つ**得られている** — nuisance parameter promotion という Stage A→B の正確な名前と、gauge 最適化が単なる規約ではないという技術的事実である。すなわち field-native 語彙への翻訳は、情報を保存しただけでなく増やした。

---

## 10. Does DR-1 survive?

**YES but presentation-only.**

局所パターン（trusted-reference inverse problem → joint estimation → equivalence-class target）は実在する。しかしその実在は、既存の三語 — nuisance promotion、identifiability up to similarity、quotient parameterization — で完全に記述され、DR という語を追加しても新しい判断は一つも生じない。さらに A′ 攻撃により、「relocation」の指示対象（解決が生成した境界）は本文の自認二箇所によって否定されている。生き残るのは記述の便宜であり、方法論的構成物ではない。

---

## 11. Recommended v0.3 impact

**Minor revision。ただし追加すべき内容を変更する。**

本文 §20 は DR 的 note の追加を提案しているが、v0.3 へ入れるべきは概念ではなく**否定的結果と先行名称**である。DR 語彙・DR-0–DR-4 は v0.3 に入れない。

### 11.1 v0.3 に追加すべき最小の一段落（提案）

> GST lineage を一次文献で検査した結果、`resolution → boundary relocation → target reformulation` を反復構造として支持する証拠は得られなかった。gauge は quotient target により閉じ、非 Markov 拡張は gauge の残余ではなく model adequacy から分岐し、process-tensor 理論は gauge-free 定式化に先行する。局所的に観察されたのは、(i) 既知として条件づけていた参照操作を同時推定へ格上げする操作（統計学の nuisance parameter promotion）、(ii) 相似変換を除く識別可能性とその商による target 再定義（実現理論と同型）、(iii) 適合度検定によるモデル違反の検出と、それに続く方向別のモデル拡張、の三つである。これらは Box (1976) の反復的モデル構築ループ、および system identification の標準的な model structure → identifiability → validation → structure revision の循環として既に統合されている。したがって本ノートは、この構造に固有名を与えず、既存名称で参照する。監査上保持するのは、条件付き解決を無条件解決と読まないこと、商による解決を未解決の物理的曖昧性と読まないこと、後続の model 拡張を先行手法の失敗と読まないことの三点のみであり、これらもいずれも GST review と gauge-free tomography の一次文献に明示されている。

---

## 12. Best next comparison case

**計量学 / SI traceability を選ぶ。** system identification と cosmology は退ける。

理由は四基準すべてで最良だからである。

**(a) DR-0/closure が出そうな対照がある** — これが決定的。2019 年の SI 改定で、キログラムは国際キログラム原器という**人工物への依存を関係づけ直したのではなく消去した**（h を定義値に固定）。定義上の不確かさはゼロになった。これは「境界は移送されるのであって消去されない」という DR の中心主張に対する、**事前に指定できる反証事例**である。DR を検査する次のケースは、DR が負けうる場所で行わなければならない。

**(b) DR-2 が出そうな候補も同じ分野にある** — traceability chain は、保証を上位標準へ委譲する構造が制度として明文化されており（VIM、GUM、BIPM の相互承認取決め）、反復的委譲の実例として設計上存在する。同一分野内に反証事例と支持事例の両方があるのは、この分野だけである。

**(c) field-native literature が強い** — VIM の用語定義、GUM の不確かさ伝播、校正証明書という文書形式まで標準化されており、比喩へ逃げる余地が構造的に小さい。

**(d) philosophical storytelling に逃げにくい** — 計量学は「何を一意に決めるか」を法的・制度的に決着させる分野であり、存在論的読解の入り込む隙が最も少ない。

### 12.1 退ける理由

- **system identification**：そこでの Stage A–E 相当はすでに一冊の教科書（Ljung）が統合しており、実施すれば「DR が目指す統合は既存」という結論が高確率で出る。予見可能な否定的結果に第二ケースを費やす価値は低い。
- **cosmology**：(d) の基準で最悪であり、DR-4 的な語りへの誘引が最も強い。

### 12.2 次ケースの事前登録すべき反証条件

> 「SI 改定においてキログラムの人工物依存が消去された事例が、DR の定義下で `closure`（DR-0）と判定できるなら、DR は普遍的パターンではない。判定できないなら、DR の定義は closure を認識できず、反証不能である。」

どちらに転んでも概念について決着がつく。

---

## 13. Final one-sentence judgment

**GST lineage は、条件付き逆問題・撹乱母数の格上げ・相似変換を除く識別可能性・商によるパラメータ化・適合度検定・モデル拡張という既存語彙で余さず記述でき、Deferred Resolution は本ケースにおいて新しい区別も診断も生まず、その最良の事例ですら本文自身が「境界は解決以前から仕様に含まれていた」と二度認めているため、概念としては破棄し、記述は既存名称へ戻すべきである。**

---

## 14. 核心への回答

### 14.1 GST Case Study は、既存語彙では見えにくかった何かを発見・診断しているか

**NO。**

本ケースが引く区別 — 条件付き解決と無条件解決、gauge と model misspecification、後続拡張と先行失敗 — は、本ケースが最も依拠する二つの文献、**Nielsen et al. 2021 の GST review と Di Matteo et al. 2020 の導入部に、いずれも明示されている**。すなわち区別の出所は本ケースではなく、本ケースが読んだ文献である。一般パターンの側は 1976 年に Box が命名し、Ljung の教科書が一分野内で統合済みである。本ケースは新しい実験判断も、見落とされた検査も、既存レビューより優れた診断も示していない — この点は本文 §17（L763）と §20（L831）が自ら認めている。

さらに、本ケースが実際に生んだ唯一の非自明な判定（operational gauge-free → non-Markovian の直接 edge は存在しない）は、**出版年を並べたことで得られた**。概念は一度も識別作業をしていない。

### 14.2 Deferred Resolution は保存すべき研究仮説か、捨てるべき再命名か

**捨てるべき再命名である。** 名称・定義・DR-0–DR-4 の梯子をすべて破棄することを推奨する。理由は三つ：

1. 定義が Box ループと外延一致し反証不能であること（§2.1）。
2. 最良事例で「境界の先在」を本文自身が認めており relocation に指示対象がないこと（A′）。
3. 達成された場合の到達点（分野横断の統合）が既に占有されていること（§3 prior art）。

### 14.3 ただし捨てずに残すべきものが一つある

それは概念ではなく、本文 §15.2 が提起した経験的問いである。

> **上流の scope と不確かさは、handoff を越えて実際に保持されるか。**

これは DR とは別種の問いである。DR は「境界が移送されるという構造があるか」を問い、答えは「ない、それは通常のモデル構築である」だった。handoff の問いは「実際のプロトコル文書・報告書・下流利用において、上流の条件と不確かさが失われる事例があるか」を問う**監査可能な経験的問い**であり、失敗事例の発見によって決着する。この問いは Deferred Resolution という語を必要とせず、既に safety engineering の assurance case、計量学の traceability、統計学の model-transfer 問題という三つの隣接領域を持つ。

**本ケースが §15.2 で「本ケースは実 protocol でそのような loss を発見していない」（L657）と書いた一行が、実は次に追うべき唯一の生きた研究線であり、DR という概念はその線に不要である。**

---

## 15. Verification log

本査読で独立に確認した事項。

| 対象 | 方法 | 結果 |
| --- | --- | --- |
| Li et al. 2024 の書誌 | arXiv:2307.14696 を直接取得 | **著者名が全面的に誤り**（実際の著者：Ze-Tong Li, Cong-Cong Zheng, Fan-Xu Meng, Han Zeng, Tian Luan, Zai-Chen Zhang, Xu-Tao Yu）。タイトル・誌名・DOI は正しい。本文の「instrument-set tomography」という記述は正しい（論文が IST / LIST / MLE-IST を提案） |
| Merkel et al. 2013 の gauge 言及 | arXiv:1211.0322 の abstract 取得、full PDF 抽出試行、OSTI QCVV 文書取得試行、Web 検索 | **未確認**。abstract は "assumes nothing about the gates used for preparation and measurement"、"linearize about the target" のみ。PDF テキスト抽出は二件とも失敗。判定の前提条件として本文に明記すべき |
| gauge 変換式の正しさ | 手計算 | **正しい**。(EB⁻¹)(BG_kB⁻¹)…(BG_1B⁻¹)(Bρ) = E G_k…G_1 ρ |
| Pollock et al. の投稿・出版年 | arXiv:1512.00589 / PRA 97, 012127 | **本文の記述どおり**（submitted 2015, published 2018）。Stage D→E の時系列反論はこの一点で成立 |

### Sources

- [arXiv:2307.14696 — Non-Markovian Quantum Gate Set Tomography](https://arxiv.org/abs/2307.14696)
- [arXiv:1211.0322 — Self-Consistent Quantum Process Tomography](https://arxiv.org/abs/1211.0322)
- [Physical Review A 87, 062119](https://link.aps.org/doi/10.1103/PhysRevA.87.062119)
- [Sandia QCVV report (OSTI 1345895)](https://www.osti.gov/servlets/purl/1345895)

---

## 16. Review posture

### 本査読が確信をもって主張するもの

- Deferred Resolution の定義は反証不能であり、Box ループと外延一致する。
- 本文は境界の先在を両端（L218, L710）で自認しており、relocation に指示対象がない。
- Li et al. 2024 の著者名は誤りである（検証済み）。
- gauge 変換は完全正値性を保存せず、報告される誤差量は gauge 変位量であるため、gauge optimization は単なる reporting convention ではない。
- Erasure Test は通過していない。

### 本査読が確信をもたないもの

- Merkel et al. 2013 が gauge / 相似変換不変性に言及しているか（未検証。DR-1 の最良事例の成否を左右する）。
- Di Matteo et al. 2020 の記法 G(B,H)=Hom(S,T(H))/∼ が原論文の形式に忠実か（未検証）。

### 本査読が擁護しなかったもの

- Deferred Resolution という概念の保存。
- 監査ネットワークの新規性。
- 本文の DR-1 という肯定形ラベル。

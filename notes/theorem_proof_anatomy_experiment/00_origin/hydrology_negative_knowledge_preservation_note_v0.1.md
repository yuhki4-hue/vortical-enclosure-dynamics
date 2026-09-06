# Hydrology Negative-Knowledge Preservation Note v0.1

## How US flood-frequency guidance recorded, carried, and retired what it could not do

- **バージョン:** 0.1
- **日付:** 2026-08-21
- **種別:** exploratory historical / methodological reconstruction
- **主対象:** Bulletin 15 → 17 → 17A → 17B → 17C の系列と、FEMA 側の下流利用
- **姉妹ノート:** [`case_01_hydro_target_artifact_discovery_v0.1.md`](./case_01_hydro_target_artifact_discovery_v0.1.md)（omission search。本ノートとは目的が異なる）

---

## 0. Status

このノートが**主張しないこと**を先に固定する。

- 新しい理論・方法論・framework ではない。
- 水文学が他分野より成熟しているという主張ではない。
- Validation Basis Transition（VBT）の成功証拠ではない。omission が見つからないことを VBT の支持として扱わない。
- 「negative knowledge preservation」を新概念として提示しない。以下で扱う保存形態はすべて、水文学の文書が自分の語彙で名指ししているものである。
- 「古い分野だから成熟している」という論証はしない。年数は根拠に数えない。

このノートが**やること**は一つだけである。米国の洪水頻度解析ガイダンス系列において、認識された限界・偏り・未解決問題が、実際にどの文書のどの節に、どの形式で書き残されたかを、一次資料の本文から復元する。

**確度ラベル**を全体で使用する。

| ラベル | 意味 |
|---|---|
| `documented` | 一次資料の本文に明示されている。引用可能。 |
| `strongly suggested` | 複数の一次資料の記述から強く示唆されるが、直接の因果記述はない。 |
| `plausible` | 整合的だが、文献上の裏付けを本調査では確認していない。 |
| `unknown` | 本調査では確認できなかった。存在しないという意味ではない。 |

---

## 1. Motivation

水文学を教材として見る理由は「成熟しているから」ではない。次の三つが交差する場所で、**保証の担当区分が明示的に文書化されざるを得なかった**からである。

1. **empirical / statistical inference** — 有限標本、極値、tail、skew 推定。
2. **physical / process understanding** — 流域改変、都市化、混合母集団、融雪と降雨。
3. **practical / institutional decision use** — 保険料率、氾濫原規制、設計、地図の法的効力。

この三層が同一文書系列の中で衝突するため、「統計手法の限界」「物理過程の変化」「制度上の判断」のどれがどこまで担当するかを、標準文書自身が書き分ける必要が生じた。その書き分けの痕跡が、本ノートの探索対象である。

なお本ノートは、水文学を「統計科学」として読まない。同時に「物理は法則、水文学は統計」という二分法も作らない。Bulletin 17C 自身が、統計的推論と物理過程知識を並置して扱うことを繰り返し要求している（後述 §7-E）。

---

## 2. Research Question

> 水文学における認識された failure・bias・uncertainty・limitation は、どのような qualification・procedure・standard・revision mechanism へ変換され、保存されてきたか。そして、その保存はどこで弱まるか。

補助問い。

- **Q-a** その negative knowledge はどこから来たか（失敗事例／統計的 bias の発見／simulation 研究／理論的限界／実務経験／破局的事象／事後解析／規制上の懸念）。
- **Q-b** 何に変換されたか（mandatory procedure／warning／applicability condition／update trigger／unresolved issue 等）。
- **Q-c** 背景化されたものは、必要なときに再前景化できる形で残っているか。
- **Q-d** 統計的規則性の有効期間と、対象系の process change は、文書上どう区別されているか。
- **Q-e** 反復的な成功使用によって条件が暗黙化し、claim が安定した規則のように振る舞うようになるか。それとも、それを防ぐ制度が発達しているか。

---

## 3. Scope

### 見る範囲

- Bulletin 17B 全文（IACWD 1982、194 頁 PDF）— 本文取得・全文検索済み。
- Bulletin 17C 全文（USGS TM 4-B5、ver. 1.1、2019 年 5 月、168 頁 PDF）— 本文取得・全文検索済み。
- FEMA *General Hydrologic Considerations*, Guidance Document 71, February 2019 — 本文取得・全文検索済み。
- Bulletin 15（1967）、Bulletin 17（1976）、17A（1977）— **原文未取得**。17B と 17C 内の記述を通じてのみ参照。

### 見ない範囲

- 米国外の洪水頻度解析（英国 FEH、豪州 ARR 等）。
- 個別事故・災害の事後調査報告（後述のとおり、本調査では Bulletin 改訂との直接的因果を確認できなかった）。
- HYD-A01 の監査。§10 で読み替えの可能性のみ述べ、verdict は出さない。
- 降雨頻度（NOAA Atlas 14 系列）、ダム安全、河川水理モデルの検証体系。

### 本調査の限界

Bulletin 15・17・17A の原文を読んでいない。したがって「Bulletin 17 が outlier 処理を導入した」等の記述は、すべて 17B/17C の二次的記述に依存する（`documented` ではなく、**17C の記述としては** `documented`、原典に対しては未検証）。

---

## 4. Analytical Distinctions

語を混同しないための最小区別。本ノート内でのみ有効な作業定義であり、水文学の用語法を規定するものではない。

| 語 | 本ノートでの意味 | 水文学側の典型的な現れ方 |
|---|---|---|
| **failure** | ある手法が適用され、結果が誤っていたと事後に判明した事象 | 本調査では Bulletin 改訂の直接原因として確認できなかった（§12） |
| **limitation** | 手法が原理的または実際的に扱えない範囲 | 「これらのガイドラインは〜を扱わない」型の記述 |
| **uncertainty** | 推定量に付随する定量化された散らばり | confidence interval、MSE、effective record length |
| **bias** | 推定量の系統的な偏り | 低外れ値による当てはめの歪み、skew 推定の偏り |
| **unresolved issue** | 問題として認識されているが解法が確定していないもの | Future Studies リスト、"unresolved problem" の明記 |
| **non-evaluation** | 作業部会が**評価しなかった**と明示したもの | "The Work Group did not evaluate..."（§7-C） |
| **qualification** | 結果の適用範囲を限定する記述 | Applicability 節、scope 条件 |
| **correction** | 問題を消す手続き | MGBT、EMA、effective record length 補正 |
| **preservation** | 後から取り出せる形で残すこと | 版をまたぐ Future Studies の継承、参照連鎖 |
| **omission** | 下流アーティファクトで落ちること | 本ノートの主題ではない（Case 01 の主題） |

**重要な区別:** `limitation` と `non-evaluation` は別物である。前者は「できないと分かっている」、後者は「調べていないので分からない」。水文学のガイダンスはこの二つを書き分けている（§7-C）。本ノートで最も注目すべき発見の一つがこれである。

---

## 5. Historical Reconstruction

### 5.1 版の系譜（`documented`）

| 年 | 文書 | 発行主体 | 17C が記述する変更内容 |
|---|---|---|---|
| 1967-12 | Bulletin 15 *A Uniform Technique for Determining Flood Flow Frequencies* | Hydrology Committee, US Water Resources Council | log-Pearson Type III をモーメント法で当てはめる方式を推奨。報告書自身が「さらなる研究が必要」と明記 |
| 1976-03 | Bulletin 17 *Guidelines for Determining Flood Flow Frequency* | US Water Resources Council | Bulletin 15 の拡張。outlier、historical flood information、regional skew の扱いを導入 |
| 1977-06 | Bulletin 17A | 同上 | weighted skew の計算手順の明確化のみ |
| 1981-09 / 1982-03 | Bulletin 17B | Hydrology Subcommittee, IACWD | generalized skew の推定と重み付け、outlier の検出、two-station comparison、confidence limits、conditional probability adjustment (CPA) |
| 2018 / 2019-05 (ver. 1.1) | Bulletin 17C（USGS TM 4-B5） | HFAWG / Subcommittee on Hydrology | interval・censored データ枠組、EMA、MGBT、改良 confidence interval、Bayesian GLS regional skew |

Bulletin 17C 本文（Background 節）:

> "This document is an update to the guidelines published earlier in Bulletins 17, 17A, and 17B. Revisions incorporated in this document address major limitations of Bulletin 17B. **Most of these limitations were well known and are listed in Bulletin 17B (IACWD, 1982) on p. 27–28 as topics needing future study.**"

この一文が本ノートの中心的発見の入口である。**17C は自らの改訂項目を、17B が 36 年前に自分で書いた未解決問題リストに紐付けている。**

### 5.2 Bulletin 17B の Future Studies リスト（原文、pp. 27–28）

17B §VII.C "Future Studies" の全 8 項目（`documented`、原文からの転記）:

> 1. Selection of distribution and fitting procedures
>    - (a) Continued study of alternative distributions and fitting procedures is believed warranted.
>    - (b) Initially the Work Group had expected to find that the proper distribution for a watershed would vary depending upon watershed and hydrometeorological conditions. **Time did not permit exploration of this idea.**
>    - (c) More adequate criteria are needed for selection of a distribution.
>    - (d) Development of techniques for evaluating homogeneity of series is needed.
> 2. The identification and treatment of mixed distributions.
> 3. The treatment of outliers both as to identification and computational procedures.
> 4. Alternative procedures for treating historic data.
> 5. More adequate computation procedures for confidence limits to the Pearson III distribution.
> 6. Procedures to incorporate flood estimates from precipitation into frequency analysis.
> 7. Guides for defining flood potentials for ungaged watersheds and watersheds with limited gaging records.
> 8. Guides for defining flood potentials for watersheds altered by urbanization and by reservoirs.

項目 1(b) は特筆に値する。作業部会が**持っていた仮説と、それを検証しなかった理由（時間不足）**を、標準文書の本文に残している。これは結果でも限界でもなく、**未実行の探索の記録**である。

### 5.3 36 年後の対応関係

Bulletin 17C の Future Studies 節（p. 35）と 17B のリストを突き合わせる。

| 17B の項目 | 17C での状態 | 確度 |
|---|---|---|
| 1(a)(c) 分布選択の代替と基準 | 明示的な解決なし。LP-III を維持 | `documented`（17C が LP-III を推奨として維持） |
| 1(b) 流域条件による分布の変動 | 17C Future Studies 項目 3「流域の水文過程・物理的考慮を解析に取り込む方法」に部分的に継承 | `strongly suggested`（文言は異なるが主題は連続） |
| 1(d) 系列の均質性評価 | appendix 4 の exploratory data analysis（trend・changepoint 検査）として手続化 | `documented` |
| **2. 混合母集団** | **未解決のまま 17C Future Studies 項目 1 として再掲** | `documented` |
| 3. outlier の識別と計算手順 | **解決。MGBT による PILF 識別（Cohn et al. 2013）** | `documented` |
| 4. historic data の代替手順 | **解決。interval データ枠組 + EMA（Cohn et al. 1997, 2001）** | `documented` |
| 5. Pearson III の confidence limits | **解決。改良 CI（Cohn et al. 2001）** | `documented` |
| **6. 降水からの洪水推定の統合** | **未解決のまま 17C Future Studies 項目 4 として再掲** | `documented` |
| **7. 無観測・短記録流域** | **未解決のまま 17C Future Studies 項目 2 として再掲。独立小節を新設** | `documented` |
| **8. 都市化・貯水池による改変流域** | **未解決のまま 17C Future Studies 項目 5 として再掲。独立小節を新設** | `documented` |

**36 年間で解決されたのは 3 項目、未解決のまま明示的に繰り越されたのが 4 項目である。**

17C 自身の記述は「four of the items listed as 'Future Work' in Bulletin 17B」に対応したとするが、上の突合せで明確に解決と対応づけられるのは項目 3・4・5 の三つで、四つ目は interval 枠組が項目 4 の一部を超えて拡張した分を別建てにしたものと読める（`plausible`。17C は四項目の内訳を明示していない）。

### 5.4 17C が新規に追加した未解決問題

17B のリストになく 17C で新設された Future Studies 項目（`documented`）:

> 6. Guides for estimating dynamic flood frequency curves that vary with time, incorporating climate indices, changing basin characteristics, and addressing potential nonstationary climate conditions;
> 7. Frequency estimation in cases where long-term trends are evident in the data but are not readily explainable by the history of land use, land use practices, or engineering modifications of the river or flood plain; and
> 8. **An examination and redefinition of risk, reliability, and return periods under nonstationary conditions.**

項目 8 は、非定常条件下では「リスク」「信頼性」「再現期間」という**概念そのものの再定義**が必要だという認識を、未解決問題として登録している。

---

## 6. Negative-Knowledge Ledger

`Mandatory?` 欄は文書の助動詞（shall / should / recommended / may）に基づく。ガイダンス自体の法的拘束力は別問題であり、ここでは判定しない。

| ID | Problem / negative knowledge | Evidence / source of concern | Earlier treatment | Revised treatment | Preservation form | Mandatory? | Downstream relevance | Confidence |
|---|---|---|---|---|---|---|---|---|
| NK-01 | 低い方の外れ値が当てはめに過大な影響を与える | 統計手法研究（Cohn et al. 2013）。17B は問題を認識し未解決として登録 | 17B: Grubbs-Beck による単一低外れ値検出 + conditional probability adjustment | 17C: Multiple Grubbs-Beck Test による PILF 識別 | mandatory procedure（17C 本体手順） | recommended（"should"） | 低頻度洪水量の推定値が変わりうる | `documented` |
| NK-02 | historic / paleoflood 情報を点値としてしか扱えない | 17B Future Studies #4。EMA 研究（Cohn et al. 1997） | 17B: pp. 12-2〜12-4 の逐次調整手順 | 17C: interval 表現 + perception threshold + EMA | mandatory procedure + 新データ表現規約 | recommended | 長期記録を持つ地点で推定が変わる | `documented` |
| NK-03 | 17B の confidence limits が skew の不確かさを無視していた | 17C 本文が明記 | 17B: Appendix 9 の手順 | 17C: skew 不確かさと historic 情報を反映した CI | uncertainty interval の再定義 + 差異の明示的警告 | recommended | **17B 由来の CI は過小である可能性を 17C が明言** | `documented` |
| NK-04 | 17B の調整手順の適用順序が恣意的だった | 17C 本文が "arbitrary selection of a sequence of such adjustments" と明記 | 17B: 調整アルゴリズムの逐次適用 | 17C: EMA による単一枠組への統合 | 手法統合による恣意性の除去 | mandatory（EMA が本体手順） | 同一データでも解析者により結果が異なりえた | `documented` |
| NK-05 | 一般化 skew マップ（17B Plate 1）の精度不足 | 17B 自身が「generalized estimate」と留保。後の Bayesian GLS 研究 | 17B: Plate 1 を全国標準として提供、詳細研究を推奨 | 17C: **「IACWD (1982, plate 1) の regional skew 推定値は洪水頻度解析での使用を推奨しない」** | **explicit obsolescence declaration**（本文中 2 箇所） | 明示的な不使用勧告 | **17B Plate 1 に依拠した既存推定値が下流に残存** | `documented` |
| NK-06 | 混合母集団（融雪／降雨／熱帯低気圧／アイスジャム）を単一分布で扱う誤り | 17B Future Studies #2。地域研究群（Crippen 1978, Jarrett & Costa 1988, Murphy 2001 ほか） | 17B: 未解決として登録 | 17C: 事例を列挙し分離解析を許容。ただし**「作業部会はこれらの手順を評価していない」と明記** | applicability condition + **mandatory default rule** + non-evaluation 宣言 | **"shall"**（客観的基準で分離できない場合は単一母集団として扱う） | 分離判断が推定値を大きく動かしうる | `documented` |
| NK-07 | 暦期間による系列分割の誤用 | 17C 本文 | 17B: 明示的規定を本調査では未確認 | 17C: 「異なる水文気象条件による事象でない限り、暦期間による分離は水文学的に妥当と見なさない」 | **explicit prohibition** | 禁止 | 解析者による恣意的分割の防止 | `documented` |
| NK-08 | 見かけのトレンドから非定常性を推論する誤り | 方法論研究（Cohn & Lins 2005; Villarini et al. 2009a; Koutsoyiannis 2011） | 17B: 該当記述を本調査では未確認 | 17C: **「定常性は基礎となる確率過程の性質であり、観測データの性質ではない。定常過程の実現値も数十年〜数世紀持続する変動やトレンドを示しうる」** | **conceptual warning**（推論誤りの名指し） | 記述的（強い断定） | トレンド検出＝非定常性という下流での短絡を抑止 | `documented` |
| NK-09 | 土地利用・気候で説明できない多十年トレンド | 17C 本文 | 17B: 未確認 | 17C: 「最も厄介な問題の一つ」「作業部会は評価していない」「**そのような記録をどう調整するかは未解決問題である**」 | **explicit unresolved issue** | 物理機構の調査を推奨 | 該当地点では手順が存在しない | `documented` |
| NK-10 | 系列相関により不確かさ推定が誤る | Tasker 1983; Vogel & Kroll 1991 | 17B: 未確認 | 17C: effective record length による不確かさ補正を推奨 | correction procedure | recommended（"should"） | CI 幅に影響 | `documented` |
| NK-11 | 漸進的流域変化は記録に残らない | 17C 本文 | 17B: 未確認 | 17C: **「都市化や多数の小貯水池の建設の影響は文書化されない可能性が高い。年々では流況を目立って変えないが累積効果は大きくなりうる」** | **warning + documentation-failure の名指し** | 記述的 | **記録に無いこと＝変化が無いこと、ではないと明言** | `documented` |
| NK-12 | 流域改変記録の非均質性 | 17B Future Studies #8 の系譜 | 17B: 未解決として登録 | 17C: 「比較的一定の流域条件を表す記録のみを頻度解析に使用すべき」+ **「作業部会は流域変化を扱う手法を評価しておらず、特段の推奨を行わない」** | applicability condition + non-evaluation 宣言 | recommended（"should"） | 都市化流域での適用可否に直結 | `documented` |
| NK-13 | 気候変動・気候変動性 | 17C 本文 | 17B: 該当記述なし（時代的に当然） | 17C: **「これらのガイドラインの策定において時間不変性が仮定された」**。定量化の科学的根拠がある場合は時変パラメータ等を使用し、**十分に文書化し正当化すること**を要求 | **explicit assumption declaration** + 条件付き逸脱許可 + 文書化要求 | 逸脱時の文書化・正当化は要求 | **標準自身が自らの仮定を明示** | `documented` |
| NK-14 | 推定値の陳腐化 | 17C 本文 | 17B: 未確認 | 17C: 「**推定値は作成の数年後には古くなっている可能性がある**」「追加データだけでも再評価の十分な理由になりうる」「新たな評価の際、解析者は過去の推定値のレビューを自分の研究に含めるべきである。**差異が現れた場合は、それを認識し説明すべきである**」 | **update trigger + reconciliation requirement** | recommended（"should"） | **過去推定値との差異の説明義務。Case 01 の主題に直接対応** | `documented` |
| NK-15 | 年超過確率の誤読（供用期間リスクの見落とし） | 17B §VI.B "Risk" + Appendix 10 の系譜 | 17B: Risk 節と付録 | 17C: **独立節 "Risk Accumulates"** を設置。25 年で 22% 等の具体例を提示 | dedicated warning section | 記述的 | 一般利用者・意思決定者向けの誤読防止 | `documented` |
| NK-16 | 記録長不足での適用 | 17B・17C 双方 | 17B: 最小記録長の規定 | 17C: 「一般に 10 年未満の記録では信頼できない」「AEP 0.005 未満は地域情報・降水情報・paleoflood 情報による補強を一般に要する」 | applicability condition（数値閾値付き） | 記述的だが具体的 | 短記録地点の推定値の信頼範囲 | `documented` |
| NK-17 | 記録外への外挿 | 17C 本文 | 17B: §VII.A で「相当の裁量を許す」と記述 | 17C: 「利用可能な記録で定義される確率より稀な確率では、推定精度が劣化する」。理由として標本誤差・基礎分布の未知性・**大規模時の物理過程の変化**を列挙 | warning + 理由の明示 | 記述的 | 0.2% AEP 等の下流利用に直接関係 | `documented` |
| NK-18 | 特異事象データの混入 | 17C Applicability | 17B: 未確認 | 17C: ダム決壊、アイスジャム、導水・分水などの特異事象は、自然流域条件を表すよう適切に調整しない限り使用すべきでない | data exclusion rule | 記述的（"should not"） | 記録の前処理判断 | `documented` |
| NK-19 | 標準からの逸脱の無管理 | 17B §VII.A、17C Applicability（**ほぼ同文で 36 年間継承**） | 17B: 「逸脱は適切な研究により裏付け、推奨手順による結果との比較を伴わなければならない」 | 17C: ほぼ同文を維持。さらに「Subcommittee on Hydrology は、そのような状況を将来の改訂の検討のため報告するよう要請する」 | **deviation control + institutional feedback channel** | **"must"**（逸脱の裏付けと比較） | **逸脱事例が標準改訂へ還流する経路** | `documented` |
| NK-20 | 評価していない事項を「問題なし」と読まれること | 17B §VII.B、17C 複数箇所 | 17B: 「代替 plotting position 公式の優劣は研究しておらず、推奨は行わない」 | 17C: **"The Work Group did not evaluate..."** が混合母集団・流域変化・気候変動性・多十年トレンドの 4 箇所に出現 | **non-evaluation disclaimer** | 記述的 | **「未評価」と「不要」の区別を下流に伝える** | `documented` |

---

## 7. Preservation Mechanisms

一次資料から確認できた保存機構を、水文学側の文書構造に即して整理する。

### A. 版をまたぐ未解決問題リストの継承（最も強い機構）

Future Studies 節が Bulletin 17B と 17C の双方に存在し、**未解決項目が次版へ明示的に持ち越される**（§5.3）。保存されるのは解法ではなく**問題の同一性**である。36 年間で 4 項目が生き延びた。

これは注釈でも警告でもない。**標準文書に付属する常設の未解決問題台帳**であり、改訂時に照合される。17C が自らの変更を 17B の p.27–28 に紐付けたことが、この台帳が実際に参照されたことの証拠である（`documented`）。

### B. 明示的な陳腐化宣言

NK-05。17C は 17B Plate 1 の regional skew 推定値について「洪水頻度解析での使用を推奨しない」と本文中 2 箇所で述べる。**先行版の特定の成果物を名指しで退役させる**形式であり、暗黙の置き換えではない。

### C. Non-evaluation disclaimer（本調査で最も注目すべき形式）

NK-20。「作業部会は〜を評価しなかった」という定型句が、17B（plotting position）と 17C（混合母集団・流域変化・気候変動性・多十年トレンド）の双方に現れる。

この形式は `limitation`（できないと分かっている）とも `warning`（危険だと分かっている）とも異なる。**「調べていないので分からない」という状態を、第一級の記載事項として残す**ものである。これにより、下流の読者は「記載がない＝問題がない」と読めなくなる。

### D. 逸脱制御と制度的還流経路

NK-19。17B §VII.A と 17C Applicability がほぼ同文で以下を要求する。

- 逸脱は適切な研究で裏付けること。
- **推奨手順で得られる結果との比較を添えること。**
- 逸脱事例を Subcommittee へ報告すること。

第二項が重要である。逸脱時に標準手順の結果を併記させることで、**逸脱の効果が定量的に可視化される**。第三項は、実務で生じた非適合事例が次の改訂へ還流する経路を、標準自身が指定している。

### E. 統計的検査と物理的理解の対の要求

17C は、統計的手順の結果を物理過程の理解と照合することを繰り返し要求する。多十年トレンドが検出された場合は「基礎となる物理機構を調査すること」を推奨し、混合母集団の分離には「客観的かつ**水文学的に意味のある**基準」を要求する（NK-06、NK-07）。統計的分離可能性だけでは不十分、という条件が明文化されている。

### F. 仮定の明示宣言

NK-13。「これらのガイドラインの策定において時間不変性が仮定された」。**標準が自らの前提を一文で名指しする**形式。これがあることで、非定常性が問題になったときに「どこが破れるか」を下流が特定できる。

### G. 更新契機と過去推定値との照合義務

NK-14。追加データだけでも再評価の理由になること、および新推定が過去推定と異なる場合に**差異を認識し説明すること**を要求する。これは推定値の transport に対する照合要求そのものである。

### H. 下流側の参照更新規約

FEMA *General Hydrologic Considerations*（Feb 2019）は「Mapping Partner は **Bulletin 17C およびその後続の修正**に従って peak flow データを解析すべきである」と記す（`documented`）。「and subsequent modifications」という前方参照により、参照先が固定版ではなく生きた標準に接続される。

同文書には **Table of Revisions**（改訂表）が付されており、2019 年 2 月改訂の内容として「USGS Bulletin 17C への参照を改訂した」と記録されている（`documented`）。下流ガイダンス側にも版管理の痕跡が保存されている。

さらに「Bulletin 17C に記載された以外の解析手法を使う場合は Regional Project Officer と調整すべきである」として、**逸脱に制度的承認ゲートを課している**（`documented`）。§7-D の逸脱制御が、規制実務側では承認手続として実装されている。

---

## 8. Known Failure / Limitation of Preservation

保存機構が弱い、または本調査で確認できなかった箇所。**これらは水文学の欠陥の告発ではなく、保存の限界の記録である。**

### L-01 — 17B の expected probability が 17C に見当たらない（`documented`（不在の事実）／ `unknown`（理由））

Bulletin 17B は §VI.C "Expected Probability"（p. 24）と Appendix 11 を持つ。Bulletin 17C 全文を検索したところ、"expected probability" という語は**一度も出現しない**（"Expected Moments Algorithm" は別概念）。conditional probability adjustment も、導入部で 17B の特徴として一度言及されるのみで、手順としては継承されていない。

17C は EMA が「17B の恣意的な調整手順の逐次適用を不要にする」と述べており（NK-04）、CPA についてはこれが実質的な退役理由と読める（`strongly suggested`）。一方、expected probability については、**退役を明示する記述を本調査では発見できなかった**。

§7-B の Plate 1 が明示的に退役宣言されたのと対照的である。**同一文書内で、明示的退役と無言の消滅が併存している。**

### L-02 — 下流ガイダンスにおける語彙の減衰（`documented`（当該文書について））

FEMA *General Hydrologic Considerations*（Feb 2019、25 頁）の全文検索結果:

| 語 | 出現回数 |
|---|---|
| `17C` | 16 |
| `17B` | 0 |
| `uncertaint`（uncertainty 等） | **0** |
| `nonstation`（nonstationarity 等） | **0** |
| `climate` | 1（閉鎖流域湖の水位変動の文脈のみ） |
| `urbaniz` | 3 |
| `document` | 41 |

Bulletin 17C は confidence interval を主要成果の一つとし、非定常性に独立節と 3 つの Future Studies 項目を割いている。それを採用する FEMA の一般水文考慮事項ガイダンスには、当該語が現れない。

**この所見の射程を限定する。** FEMA のガイダンス体系は複数文書に分かれており、不確かさが他文書（例えば riverine mapping guidance、MT-2 手続）で扱われている可能性は排除していない。本調査が確認したのは、**この一文書について**の語の不在のみである。「FEMA が不確かさを扱っていない」とは述べない。

### L-03 — 未解決問題の長期滞留（`documented`）

混合母集団・無観測地点・都市化／貯水池・降水情報の統合は、1982 年から 2018 年まで未解決のまま繰り越された（§5.3）。保存機構が働いていることと、問題が解決することは別である。**この分野の Future Studies 台帳は、解決を保証せず、忘却だけを防いでいる。**

### L-04 — 適用範囲外の地点に対する手順の不在（`documented`）

17C の Introduction は明言する。

> "The procedures do not cover watersheds where flood flows are appreciably altered by reservoir regulation, watershed changes, or hydrologic nonstationarities, or where the possibility of unusual events, such as dam failures, must be considered."

**標準が適用されない地点が存在することは明示されているが、その地点でどうすべきかの国家的手引きは存在しない。** 17C は Regulated Flow Frequency と Urbanization の小節で既存手法を列挙するが、「それらは本ガイドラインで企図するような広範・体系的適用に向けた評価をまだ受けていない」と述べる。保存されているのは**空白の所在**であり、埋め方ではない。

### L-05 — Bulletin 15・17・17A 原文の未確認（本調査の限界）

初期二版の改訂理由は 17B/17C の要約を通してしか見ていない。改訂の一次的動機（何が問題として提起されたか）を原典で確認していない。

---

## 9. Nonstationarity as a Stress Test

非定常性を特別扱いしない。ただし、保存機構が最も強く試される箇所として観察する。

### 9.1 17C の姿勢は「保存」であって「解決」ではない（`documented`）

17C は以下を同時に行っている。

1. **時間不変性を仮定したと明示する**（NK-13）。
2. 気候変動性を扱う手法を**評価していないと明示する**（NK-20）。
3. 科学的根拠がある場合の時変パラメータ使用を**許可し、文書化と正当化を要求する**。
4. 参考となりうる情報源を 5 つ列挙する（synoptic weather pattern、paleoclimate、気候予測、経年・十年規模変動、時変分布パラメータ）。
5. 非定常性関連の未解決問題を Future Studies に**3 項目登録する**。

つまり、手法を採用せずに問題を登録した。これは §5 で見た Future Studies 機構の、現在進行形の使用例である。

### 9.2 「トレンドが検出されない」と「将来の定常性が保証される」の区別（`documented`）

17C の記述はこの区別に対して**両方向に**注意を向けている。

- **一方向:** 「定常性は基礎となる確率過程の性質であり、観測データの性質ではない。定常過程の実現値も数十年〜数世紀持続する変動やトレンドを示しうる」（NK-08）。すなわち**トレンドが見えても非定常とは限らない**。
- **他方向:** 「記録に現れない漸進的変化」の警告（NK-11）。すなわち**変化が見えなくても変化がないとは限らない**。

**両方向の誤推論に対する注意が同一文書内に併存している。** これは片側だけの警告より強い保存形態である。ただし、これらは検出の限界についての注意であり、「検出されなかった場合に将来の定常性をどう扱うか」という規範的手順を与えるものではない。

### 9.3 「統計に消費期限がある」という直感の文書上の対応物（`documented`、ただし用語ではない）

ユーザ提示の探索仮説に対応する記述は存在するが、**「有効期限」という概念としてではなく、二つの別々の条項として**現れる。

| 直感的表現 | 文書上の対応物 | 性格 |
|---|---|---|
| 統計には有効期間がある | NK-14「推定値は作成の数年後には古くなっている可能性がある」+ 追加データによる再評価契機 | **標本情報の増加**による更新。時間経過そのものではない |
| 対象系が変わる | NK-12 流域変化、NK-13 気候、L-04 適用範囲外 | **母集団の変化**。統計的不確かさでは扱えないと明示 |

**この二つは文書上で明確に分離されている。** 前者は「データが増えたので推定を更新せよ」、後者は「対象が変わったので手順の前提が崩れる」であり、後者に対しては 17C は手順を与えず、適用範囲外と宣言している（L-04）。

したがって「統計の消費期限」は単一概念としては水文学の語彙に存在しない。**存在するのは、標本の更新契機と、母集団同一性の適用条件という二つの別条項である。** これは専門用語として扱うべきでないというユーザの注意と整合する。

---

## 10. Relation to HYD-A01

**audit verdict は出さない。** 本ノートの知見が HYD-A01 の読み方に与える影響のみを記す。

### 10.1 2020 FIS の qualification は制度的起源を持ちうる（`plausible`）

HYD-A01 で確認された FIS の記述 — 調査完了時点の community conditions への限定、将来変化時の amendment、都市化の影響、1%+ の追加 discharge uncertainty、短い gage record、回帰式の適用範囲 — は、本ノートで復元した保存機構（§7-A, D, F, G, H）と主題的に対応する。

ただし、**個別の FIS 文言を Bulletin 系列の特定条項の帰結として結び付ける証拠は本調査では得ていない。** FEMA の FIS テンプレートがこれらの文言をどこから継承したかは未追跡である。§7-H で確認した FEMA 側の参照更新規約と Table of Revisions は、その追跡の入口にはなる。

### 10.2 Case 01 の false-positive control として使える論点

Case 01 が「落ちている」と判定しかけたものが、実は保存機構により**別の場所に保存されている**可能性を、以下の形で検査できる。

| Case 01 で「落ちた」と見えうるもの | 本ノートが示す代替所在 |
|---|---|
| FIS に不確かさの完全な記述がない | source（USGS SIR）側の confidence limits、および Bulletin 17C 本体の CI 手順（reference chain により recoverable） |
| FIS に非定常性の議論がない | 17C が時間不変性を仮定したことを明示（NK-13）。FIS はその仮定の下の成果物であり、仮定は標準側に保存されている |
| FIS に手法の限界記述がない | 17C Applicability 節と Future Studies 節（standard 内保存） |
| FIS に将来変化の扱いがない | FIS 自身の amendment 条項 + 17C の更新契機条項（NK-14） |

**したがって Case 01 では、「target artifact に書かれていない」ことを omission と判定する前に、reference chain 上の保存所在を最低限 3 段（source report / Bulletin / FEMA guidance）まで確認する必要がある。** これは Case 01 §3 の「背景化されても再前景化できるか」という区別の、具体的な検査手順になる。

### 10.3 逆に、Case 01 で本当に検査すべき候補

本ノートが示唆する、より鋭い検査点は「不確かさの記述の有無」ではない。

- **NK-05（Plate 1 退役）:** 17B Plate 1 の regional skew に依拠した推定値が、17C の明示的不使用勧告の後も有効な FIS/FIRM に残存しているか。残存している場合、その事実が下流でどう扱われているか。
- **NK-14（照合義務）:** 推定値が更新された地点で、過去推定値との差異が「認識され説明された」記録が実際に存在するか。
- **NK-03（CI 過小）:** 17B 由来の confidence interval を引用する下流文書が、17C の「17B の CI は skew の不確かさを無視していた」という指摘を反映しているか。

これらはいずれも「注釈が落ちたか」ではなく、**「上流が明示的に退役・訂正したものが下流に残っているか」**という問いであり、証拠として扱いやすい。

---

## 11. Lessons for Later Comparative Cases

一般法則化しない。**他分野で同型の機構が存在するかを問う質問形式**としてのみ持ち出す。

1. その分野の標準文書は、**常設の未解決問題リスト**を持ち、改訂時にそれを参照するか。
2. 「評価していない」と「問題がない」を**書き分ける定型表現**を持つか。
3. 先行版の特定成果物を**名指しで退役させる**慣行があるか。それとも暗黙に置き換えるか。
4. 標準からの逸脱時に、**標準手順の結果との比較を併記させる**要求があるか。
5. 逸脱事例が**改訂へ還流する経路**が文書化されているか。
6. 標準が**自らの前提を一文で名指しする**か。
7. 推定値の更新時に、**過去推定との差異の説明**を要求するか。
8. 検出限界について、**両方向の誤推論**（見えた＝ある／見えない＝ない）に注意を向けているか。
9. 標準が適用されない領域について、**空白の所在**が明示されているか。
10. 下流ガイダンスが上流標準を**固定版参照か、前方参照（"and subsequent modifications"）か**。

これらはすべて、水文学の文書から帰納した検査項目であり、他分野で満たされるべき規範ではない。**満たされない分野が劣っているという推論をしない。** 分野によっては別の機構が同じ機能を果たしている可能性がある。

---

## 12. Negative / Null Findings

**見つからなかったものを明記する。これらは本ノートの主要な成果である。**

### N-01 — 破局的事象と Bulletin 改訂を結ぶ documented な因果を発見できなかった

本調査の範囲では、特定の洪水災害が特定の Bulletin 改訂を直接引き起こしたという記述を、17B・17C の本文中に**発見できなかった**。

17C が改訂の根拠として挙げるのは以下である（`documented`）。

- 文献レビュー
- 作業部会メンバーの実務経験
- 選定を助けるために実施された特別研究
- Monte Carlo シミュレーションによる検証（Cohn et al.）
- 観測所データを用いた手法試験

17B も同様に、Beard (1974) の比較研究（University of Texas at Austin, Center for Research in Water Resources）を選定根拠とし、その要約を Appendix 14 に収録している。

**したがって「水文学は失敗から学んだ」という物語は、少なくとも Bulletin 系列の改訂史については本調査で裏付けられなかった。** 復元できたのは、**統計的手法の欠陥が方法論研究によって発見され、標準へ反映された**という経路である。これは失敗ではなく、系統的な自己検査である。

ユーザの指示（「各改訂を失敗由来だと推測だけでつなぐ」ことの禁止）に照らし、この点は明確な null finding として記録する。

### N-02 — negative knowledge の「注釈」化は主要形態ではなかった

事前に想定された保存形態は「注釈（qualification）」だったが、実際に確認できた主要形態は**構造的なもの**だった。

- 常設リスト（Future Studies）
- 定型句（non-evaluation disclaimer）
- 手続的ゲート（逸脱時の比較併記、RPO 調整）
- 明示的退役宣言
- 節そのものの新設（Risk Accumulates、Applicability）

「注釈」という語を広く使いすぎないというユーザの注意は妥当だった。

### N-03 — 法則化・透明背景化を示す証拠を発見できなかった（control finding）

「反復的な成功使用により条件が暗黙化し、claim が安定した規則のように振る舞う」という探索仮説について、**Bulletin 系列の文書内では逆向きの証拠のみを発見した。**

- 標準が自らの仮定を明示する（NK-13）
- 推定値の陳腐化を明言する（NK-14）
- 逸脱に比較併記を要求する（NK-19）
- 年超過確率の誤読に独立節を割く（NK-15）

これらはいずれも暗黙化に抗する方向に働く。**ユーザが予期したとおり、この分野では法則化を防ぐ制度が発達している側の証拠が優勢である。**

ただし、これは標準文書内の話である。標準を使う実務、下流アーティファクト、一般利用者の理解において暗黙化が起きていないことは、本調査では**示していない**。L-02 の語彙減衰は、その方向の弱い手掛かりではあるが、単一文書の語彙統計にすぎない。

### N-04 — 保存機構の有効性を示す証拠を発見していない

機構が**存在する**ことは示した。それが**機能している**こと — たとえば逸脱報告が実際に改訂へ還流した事例、Future Studies 台帳が改訂作業で実際に参照された記録 — は、17C が 17B の p.27–28 を名指ししたという一点を除いて確認していない。HFAWG の議事録（acwi.gov に所在）が未調査である。

---

## 13. Open Questions

1. **Bulletin 15・17・17A の原文**を取得し、各改訂の一次的動機を確認する。特に Bulletin 17（1976）が outlier・historical information・regional skew を導入した理由。
2. **HFAWG 議事録**（2005–2013、acwi.gov）を追い、17B の Future Studies 台帳が改訂作業で実際に参照された経緯を確認する。§12 N-04 の空白を埋める。
3. **expected probability の退役理由**（L-01）。17C 策定過程の文書に記録があるか。
4. **PSIAC 1966**, *Limitations in Hydrologic Data as Applied to Studies in Water Control Management*（17B 参考文献 7）。表題からして本ノートの主題に直接該当する可能性があるが未取得。
5. **FEMA の不確かさ扱い**（L-02 の射程確定）。riverine mapping guidance、MT-2 手続、CNMS の各文書で uncertainty と nonstationarity がどう扱われているか。
6. **17B Plate 1 の残存**（§10.3）。17C の不使用勧告後、17B skew に依拠する有効な FIS/FIRM がどれだけ残っているか、また FEMA 側にそれを識別する機構があるか。
7. **他国標準との比較**。英国 FEH、豪州 ARR に同型の Future Studies 継承機構があるか。あれば米国固有ではないことになり、比較の基準線になる。
8. **USACE の 17B→17C 移行ガイダンス**（検索で所在確認済み、未取得）。同一標準変更に対する二機関の対応差は、下流保存の比較材料になる。

---

## 14. Sources

### 一次資料（全文取得・検索済み）

1. Interagency Advisory Committee on Water Data, Hydrology Subcommittee, 1982, *Guidelines for Determining Flood Flow Frequency*, Bulletin 17B（Revised September 1981, Editorial Corrections March 1982）: U.S. Department of the Interior, Geological Survey, Office of Water Data Coordination, Reston, Va. — [PDF](https://pubs.usgs.gov/unnumbered/70275162/report.pdf) ／ [publication page](https://pubs.usgs.gov/publication/70275162)
   - 本ノートで参照した箇所: §VI.B Risk（p. 24）、§VI.C Expected Probability（p. 24）、§VII.A Non-conforming Special Situations（p. 25）、§VII.B Plotting Position（p. 26）、**§VII.C Future Studies（pp. 27–28）**、Appendix 5 Conditional Probability Adjustment、Appendix 11 Expected Probability、Appendix 14 Beard 研究要約。

2. England, J.F., Jr., Cohn, T.A., Faber, B.A., Stedinger, J.R., Thomas, W.O., Jr., Veilleux, A.G., Kiang, J.E., and Mason, R.R., Jr., 2018, *Guidelines for determining flood flow frequency—Bulletin 17C*（ver. 1.1, May 2019）: U.S. Geological Survey Techniques and Methods, book 4, chap. B5, 148 p. — [doi:10.3133/tm4B5](https://doi.org/10.3133/tm4B5)
   - 本ノートで参照した箇所: Abstract、Introduction / Background、Purpose and Scope、Risk Accumulates（p. 4–5）、Common Issues with At-Site Data Records、Data Assumptions and Specific Concerns（Randomness of Events / Mixed Populations / Watershed Changes / Climate Variability and Change, pp. 20–23）、Estimating Regional Skew、Frequency Curve Extrapolation、**Future Studies（p. 35–36）**、**Applicability of These Guidelines（p. 36–37）**、Appendix 3、Appendix 4。

3. Federal Emergency Management Agency, 2019, *General Hydrologic Considerations*, Guidance for Flood Risk Analysis and Mapping, Guidance Document 71, February 2019, 25 p. — 取得経路: [Kentucky Transportation Cabinet mirror](https://transportation.ky.gov/Highway-Design/Drainage%20Manual/FEMA%20-%20General%20Hydrologic%20Considerations%20Guidance%20-%20Feb%202019.pdf)。FEMA 直リンク（[2022 年版](https://www.fema.gov/sites/default/files/documents/fema_general-hydrologic-considerations_112022.pdf)）は本調査時点で取得不可。
   - 本ノートで参照した箇所: Table of Revisions（p. ii）、§4 Hydrologic Analysis Methods（gage 解析と Bulletin 17C 参照、RPO 調整規定）。

### 17B / 17C を通じてのみ参照した文書（原文未取得）

4. U.S. Water Resources Council, Hydrology Committee, 1967, *A Uniform Technique for Determining Flood Flow Frequencies*, Bulletin 15.
5. U.S. Water Resources Council, 1976, *Guidelines for Determining Flood Flow Frequency*, Bulletin 17.
6. U.S. Water Resources Council, 1977, Bulletin 17A.
7. Beard, L.R., 1974, *Flood Flow Frequency Techniques*, Center for Research in Water Resources, University of Texas at Austin.（17B Appendix 14 に要約）
8. Cohn, T.A., Lane, W.L., and Baier, W.G., 1997; Cohn et al., 2001; Cohn et al., 2013（EMA・MGBT の基礎研究。17C が改訂根拠として引用）
9. Cohn, T.A., and Lins, H.F., 2005（"定常過程の実現値もトレンドを示しうる" の典拠として 17C が引用）
10. Pacific Southwest Interagency Commission, Hydrology Subcommittee, 1966, *Limitations in Hydrologic Data as Applied to Studies in Water Control Management*.（17B 参考文献 7。未取得、§13-4）

### 検索のみで所在確認（未取得）

11. U.S. Army Corps of Engineers, *Update of Bulletin 17B to 17C: Guidance for Flood...*（§13-8）
12. HFAWG 議事録アーカイブ — https://acwi.gov/hydrology/Frequency/minutes/index.html （§13-2）

---

## Current verdict

### **B. Partial preservation history identified**

ただし、この判定には**主題の訂正**を伴う。

**確認できたこと。** 米国の洪水頻度解析ガイダンス系列には、認識された限界・未解決問題・未評価事項を、版をまたいで保存する複数の documented な機構が存在する。最も強いのは、Bulletin 17B（1982）の未解決問題リストが Bulletin 17C（2018）で明示的に参照され、うち 3 項目が解決、4 項目が未解決のまま再掲されたという事実である。これは推測ではなく、17C が 17B の p.27–28 を名指しして述べている。加えて、明示的退役宣言、non-evaluation disclaimer、逸脱制御と還流経路、仮定の明示宣言、更新契機と照合義務が、いずれも一次資料の本文から確認できた。

**主題の訂正。** 保存されているのは主として**失敗の教訓ではなく、方法論的限界と未評価領域の知識**である。本調査の範囲では、特定の災害が特定の改訂を引き起こしたという documented な因果を一件も発見できなかった（N-01）。改訂の documented な起源は、比較研究・Monte Carlo 検証・文献レビュー・作業部会の実務経験である。したがって副題は "lessons from failure" ではなく、**"what it could not do"** の保存として書くのが正確である。

**A を選ばない理由。** (i) 保存機構の**有効性**を示す証拠が、17C→17B の一回の参照を除いてほとんどない（N-04）。(ii) 明示的退役と無言の消滅が同一文書内に併存する（L-01）。(iii) 下流ガイダンス一文書で不確かさ・非定常性の語が消える（L-02）。(iv) 未解決問題は 36 年間解決されないまま残った（L-03）。**保存機構は忘却を防いだが、解決も、下流への完全な伝達も保証していない。**

**C を選ばない理由。** 「通常の標準改訂」では説明しにくい形式が二つある。第一に、未解決問題リストの**版をまたぐ継承と改訂時の名指し参照**。第二に、"The Work Group did not evaluate..." という**非評価の明示宣言**。後者は「限界」でも「警告」でもなく、認識状態そのものの記録であり、通常の改訂履歴には現れない形式である。

**D・E を選ばない理由。** 一次資料本文から直接引用可能な形で、20 件の保存事例を特定できた。証拠不足でも仮説棄却でもない。

---

## What did this analysis teach us that we did not know before the analysis?

1. **保存の主要な担い手は注釈ではなく、常設の未解決問題台帳だった。** Bulletin 17B の Future Studies 8 項目が 36 年後に 17C から名指しで参照され、4 項目が未解決のまま再掲された。個々の結果に付随する qualification ではなく、標準文書に付属する独立した台帳が、版をまたぐ記憶の担体になっている。

2. **"The Work Group did not evaluate..." という定型句が、限界とも警告とも別の第三のカテゴリを構成している。** これは「調べていないので分からない」という認識状態を第一級の記載事項として残す形式であり、17B（plotting position）と 17C（4 箇所）の双方に現れる。分野の実務が、`unknown-unassessed` を独立の値として扱う必要に自力で到達していたことになる。

3. **改訂の起源は災害ではなく方法論研究だった。** これは分析前の予想と反する。「水文学は洪水被害から学んで標準を厚くした」という自然な物語を、本調査の範囲では一件も裏付けられなかった。裏付けられたのは、比較研究と Monte Carlo 検証による自己検査の経路である。

4. **退役は可能であり、実際に行使されている。** 17C は 17B Plate 1 の regional skew マップを名指しで「使用を推奨しない」と宣言した。標準は積み増すだけでなく、先行版の特定成果物を退役させうる。同時に、expected probability のように**無言で消えたもの**も同じ文書内に存在し、二つの様式が併存している。

5. **「統計の消費期限」は単一概念としては存在せず、二つの別条項に分離されていた。** 標本情報の増加による更新契機（NK-14）と、母集団同一性の適用条件（NK-12, NK-13, L-04）である。後者について 17C は手順を与えず、適用範囲外と宣言する。直感的表現が一語で捉えていたものが、文書上は担当区分の異なる二条項だったことになる。

6. **検出限界について両方向の誤推論に注意が向けられている。** 「トレンドが見えても非定常とは限らない」（Cohn & Lins）と「変化が見えなくても変化がないとは限らない」（漸進的流域変化）が同一文書内に併存する。片側だけの警告より強い形式であり、非定常性論争の両陣営の主張が標準の中で共存している。

7. **法則化仮説については逆向きの証拠が優勢だった。** 仮定の明示、陳腐化の明言、逸脱時の比較併記要求、年超過確率の誤読に対する独立節 — いずれも暗黙化に抗する方向に働く。ただしこれは標準文書内の話であり、実務・下流・一般理解における暗黙化については何も示していない。

---

## v0.1 で確立するもの

- Bulletin 15→17→17A→17B→17C の版系譜と、17B Future Studies 8 項目の 17C における状態（解決 3 / 未解決繰越 4 / 部分継承 1）。
- 一次資料本文から引用可能な 20 件の negative-knowledge 保存事例（NK-01〜NK-20）。
- 8 種の保存機構（§7-A〜H）。
- 5 件の保存の限界・空白（L-01〜L-05）。
- 4 件の null finding（N-01〜N-04）。特に災害由来因果の不在。
- Case 01 に対する false-positive control の具体的検査手順（§10.2）と、より鋭い検査候補 3 件（§10.3）。

## v0.1 で確立しないもの

- 保存機構が実際に機能していること（N-04）。
- 水文学が他分野より優れていること。
- FIS の個別文言が Bulletin の特定条項に由来すること（§10.1）。
- FEMA が不確かさを扱っていないこと（L-02 の射程は一文書の語彙統計のみ）。
- 実務・下流・一般理解における法則化の有無（N-03 の但し書き）。
- Case 01 の positive / negative 判定への含意。

## 次の作業

§13 の open question のうち 2（HFAWG 議事録）と 4（PSIAC 1966）を優先する。前者は保存機構の**有効性**という最大の空白（N-04）を直接埋める。後者は表題からして本ノートの主題に該当する可能性が高く、1966 年時点で「水文データの限界」がどう定式化されていたかを示しうる。この二件を得るまで、保存機構の強さについての判定を上方修正しない。

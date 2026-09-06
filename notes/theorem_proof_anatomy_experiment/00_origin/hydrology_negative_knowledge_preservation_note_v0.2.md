# Qualification, Open Problems, and Revision in U.S. Flood-Frequency Guidance

## A Documentary Reconstruction of Bulletin 17B → 17C → FEMA Guidance

- **バージョン:** 0.2
- **日付:** 2026-08-21
- **旧作業名:** *Hydrology Negative-Knowledge Preservation Note*（v0.1。historical working title として保持。以後この名称は使用しない）
- **種別:** exploratory documentary working note / historical-methodological case reconstruction
- **前版:** [`hydrology_negative_knowledge_preservation_note_v0.1.md`](./hydrology_negative_knowledge_preservation_note_v0.1.md)
- **設計文書:** [`qualification_practices_comparative_study_design_v0.1.md`](./qualification_practices_comparative_study_design_v0.1.md)
- **姉妹ノート:** [`case_01_hydro_target_artifact_discovery_v0.1.md`](./case_01_hydro_target_artifact_discovery_v0.1.md)

---

## Changes from v0.1

v0.1 に対する Codex adversarial review を受け、二つの事実主張を独立検証した。**いずれも Codex が正しく、v0.1 に事実誤りが二件、内部矛盾が一件あった。**

### 事実訂正

| # | v0.1 の記述 | 検証結果 | v0.2 での扱い |
|---|---|---|---|
| **C-1** | L-01「expected probability は退役宣言なく消えた」 | **誤り。** FEMA GD 71（2019, p.8）が当該調整を "must not" として明示的に禁止し、National Academy of Sciences (1978) を典拠に挙げる | L-01 を全面改稿（§8）。新規観察 `RET-DOWN` を導出 |
| **C-2** | L-04「適用範囲外に国家的手引きは存在しない」 | **誤り。** USACE EM 1110-2-1415 (1993) が存在し、FEMA GD 71 が名指しで参照している。しかも当該記述は v0.1 が抽出済みのテキスト内にあり、読み落としだった | L-04 を全面改稿（§8）。新規観察 `DELEG` を導出 |
| **C-3** | Current verdict「保存機構は忘却を防いだ」 | **N-04（有効性は未確認）と内部矛盾。** Codex の指摘は正当 | 当該表現を削除（§Verdict） |

### 追加された一次資料

Codex が本調査の見落とした一次資料を挙げた。実在を確認した。

> Cohn, T.A., England, J.F., Jr., and others, 2017, *Evaluation of Recommended Revisions to Bulletin 17B*: USGS Open-File Report 2017–1064.

改訂案が採択前に Monte Carlo 評価を経たことが documented になる。N-04 を部分的に縮小する（消滅はさせない）。

### 用語の中立化

| v0.1 | v0.2 |
|---|---|
| negative knowledge preservation | qualification and open-problem recording |
| preservation mechanism | documentary form / revision practice |
| 常設の未解決問題台帳 | cross-edition future-work list |
| 忘却を防いだ | 文書上の再発見可能性は残った（効果は未測定） |
| 解決 | addressed within the stated scope |
| 20 件の保存事例 | 20 件の coded documentary items |
| 「水文学は」 | 「本調査が検討した米国連邦洪水頻度ガイダンス系列は」 |

### 追加された Null

**N-05**（技術ガイダンス一般の通常運用である可能性）を正式な null として追加。**これは v0.2 公開後に実施した P0 検査により、部分的に確証された**（§12、および [`p0_generic_standards_baseline_v0.1.md`](./p0_generic_standards_baseline_v0.1.md)）。

### 判定の変更

| v0.1 | v0.2 |
|---|---|
| B. Partial preservation history identified | **Documentary continuity identified; preservation effectiveness untested** |

---

## 0. Status

このノートが**主張しないこと**。

- 新しい理論・方法論・framework ではない。
- 水文学が他分野より成熟しているという主張ではない。
- Validation Basis Transition（VBT）の成功証拠ではない。omission が見つからないことを VBT の支持として扱わない。
- 「保存機構」の存在を主張しない。確認できたのは文書上の連続性のみである。
- 「古い分野だから成熟している」という論証はしない。年数は根拠に数えない。

このノートが**やること**。米国の洪水頻度解析ガイダンス系列において、認識された限界・未解決問題・未評価事項が、実際にどの文書のどの節に、どの形式・どの法助動詞で記載され、後続版でどう変更・削除・参照されたかを、一次資料の本文から復元する。

**確度ラベル。**

| ラベル | 意味 |
|---|---|
| `documented` | 一次資料の本文に明示されている。引用可能。 |
| `strongly suggested` | 複数の一次資料の記述から強く示唆されるが、直接の因果記述はない。 |
| `plausible` | 整合的だが、文献上の裏付けを本調査では確認していない。 |
| `unknown` | 本調査では確認できなかった。存在しないという意味ではない。 |

**記述層のラベル**（v0.2 で追加）。

| ラベル | 意味 |
|---|---|
| `[DOCUMENTED]` | 文書に直接あるもの |
| `[ANALYTIC CODING]` | 本ノートが分類したもの |
| `[HYPOTHESIS]` | 保存・再検討支援・比較研究上の意味づけ |

---

## 1. Motivation

本調査が検討する連邦洪水頻度ガイダンス系列には、次の三種の条件が併記されている。

1. **empirical / statistical inference** — 有限標本、極値、tail、skew 推定。
2. **physical / process understanding** — 流域改変、都市化、混合母集団、融雪と降雨。
3. **practical / institutional decision use** — 保険料率、氾濫原規制、設計、地図の法的効力。

本ノートはこの担当区分を復元する。**v0.1 は「三層が衝突したため標準文書が書き分けざるを得なかった」と因果史を書いたが、これは議事録・作業部会史を持たない推測だった。削除する。** 確認できるのは併記の事実のみである。

---

## 2. Research Question

> 認識された限界・偏り・不確かさ・未評価事項は、後続版でどのように記載・変更・削除・参照されたか。

v0.1 の「どう保存されてきたか」は、保存されたことを前提に含んでいた。中立化する。

補助問い。

- **Q-a** その記述はどこから来たか（失敗事例／統計的 bias の発見／simulation 研究／理論的限界／実務経験／破局的事象／事後解析／規制上の懸念）。
- **Q-b** 何として記載されたか（mandatory procedure／warning／applicability condition／update trigger／unresolved issue 等）。
- **Q-c** 記載の所在はどこか（同一文書内／上流文書／下流文書／別機関文書）。
- **Q-d** 統計的規則性の有効期間と対象系の process change は、文書上どう区別されているか。
- **Q-e** 反復的な成功使用によって条件が暗黙化する徴候はあるか。それを抑制する記述はあるか。

---

## 3. Scope

### 見た範囲

- Bulletin 17B 全文（IACWD 1982、194 頁 PDF）— 本文取得・全文検索済み。
- Bulletin 17C 全文（USGS TM 4-B5、ver. 1.1、2019 年 5 月、168 頁 PDF）— 本文取得・全文検索済み。
- FEMA *General Hydrologic Considerations*, Guidance Document 71, February 2019 — 本文取得・全文検索済み。
- Bulletin 15（1967）、Bulletin 17（1976）、17A（1977）— **原文未取得**。17B と 17C 内の記述を通じてのみ参照。
- USGS OFR 2017–1064 — **未取得**（v0.2 で必要性が判明）。
- USACE EM 1110-2-1415（1993）— **未取得**（C-2 により必要性が判明）。

### 見ない範囲

- 米国外の洪水頻度解析。
- 個別災害の事後調査報告。
- HYD-A01 の監査。§10 で読み替え可能性のみ述べ、verdict は出さない。
- 降雨頻度、ダム安全、河川水理モデルの検証体系。

### 本調査の限界

Bulletin 15・17・17A の原文を読んでいない。したがって「Bulletin 17 が outlier 処理を導入した」等は、**17B/17C の記述としては** `documented` だが、原典に対しては未検証である。

---

## 4. Analytical Distinctions

`[ANALYTIC CODING]`。本ノート内でのみ有効な作業定義であり、水文学の用語法を規定しない。

| 語 | 本ノートでの意味 |
|---|---|
| **failure** | ある手法が適用され、結果が誤っていたと事後に判明した事象 |
| **limitation** | 手法が原理的または実際的に扱えない範囲 |
| **uncertainty** | 推定量に付随する定量化された散らばり |
| **bias** | 推定量の系統的な偏り |
| **unresolved issue** | 問題として認識されているが解法が確定していないもの |
| **non-evaluation** | 作業部会が**評価しなかった**と明示したもの |
| **qualification** | 結果の適用範囲を限定する記述 |
| **correction** | 問題を消す手続き |
| **documentary continuity** | 後続版から先行版の記述が参照可能であること（効果は含意しない） |
| **omission** | 下流アーティファクトで落ちること（Case 01 の主題。本ノートの主題ではない） |

**重要な区別。** `limitation`（できないと分かっている）と `non-evaluation`（調べていないので分からない）は別物である。本調査が検討したガイダンス系列はこの二つを書き分けている（§7-C）。**ただし、この書き分けが当該系列に固有かどうかは、v0.2 時点では P0 検査により否定的な見通しが立っている（§12 N-05）。**

---

## 5. Historical Reconstruction

### 5.1 版の系譜（`documented`）

| 年 | 文書 | 発行主体 | 17C が記述する変更内容 |
|---|---|---|---|
| 1967-12 | Bulletin 15 | Hydrology Committee, US Water Resources Council | log-Pearson Type III をモーメント法で当てはめる方式を推奨 |
| 1976-03 | Bulletin 17 | US Water Resources Council | outlier、historical flood information、regional skew の扱いを導入 |
| 1977-06 | Bulletin 17A | 同上 | weighted skew の計算手順の明確化のみ |
| 1981-09 / 1982-03 | Bulletin 17B | Hydrology Subcommittee, IACWD | generalized skew、outlier 検出、two-station comparison、confidence limits、conditional probability adjustment |
| 2017 | **USGS OFR 2017–1064** | Cohn et al. | **改訂案の統計的性能の Monte Carlo 評価**（v0.2 で追加。未取得） |
| 2018 / 2019-05 (ver. 1.1) | Bulletin 17C（USGS TM 4-B5） | HFAWG / Subcommittee on Hydrology | interval・censored データ枠組、EMA、MGBT、改良 confidence interval、Bayesian GLS regional skew |

Bulletin 17C 本文（Background 節）:

> "This document is an update to the guidelines published earlier in Bulletins 17, 17A, and 17B. Revisions incorporated in this document address major limitations of Bulletin 17B. **Most of these limitations were well known and are listed in Bulletin 17B (IACWD, 1982) on p. 27–28 as topics needing future study.**"

**17C は自らの改訂項目を、17B が 36 年前に書いた future-work list に紐付けている。** `documented`

### 5.2 Bulletin 17B の Future Studies リスト（原文、pp. 27–28）

17B §VII.C の全 8 項目（`documented`）:

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

項目 1(b) は、作業部会が持っていた仮説と、それを検証しなかった理由（時間不足）を本文に残している。

### 5.3 36 年後の対応関係

| 17B の項目 | 17C での状態 | 確度 |
|---|---|---|
| 1(a)(c) 分布選択の代替と基準 | 明示的対応なし。LP-III を維持 | `documented` |
| 1(b) 流域条件による分布の変動 | 17C Future Studies 項目 3 に部分的に継承 | `strongly suggested` |
| 1(d) 系列の均質性評価 | appendix 4 の exploratory data analysis として手続化 | `documented` |
| **2. 混合母集団** | **carried forward。17C Future Studies 項目 1** | `documented` |
| 3. outlier の識別と計算手順 | **addressed within 17C。** MGBT による PILF 識別 | `documented` |
| 4. historic data の代替手順 | **addressed within 17C。** interval データ枠組 + EMA | `documented` |
| 5. Pearson III の confidence limits | **addressed within 17C。** 改良 CI | `documented` |
| **6. 降水からの洪水推定の統合** | **carried forward。17C Future Studies 項目 4** | `documented` |
| **7. 無観測・短記録流域** | **carried forward。17C Future Studies 項目 2。独立小節を新設** | `documented` |
| **8. 都市化・貯水池による改変流域** | **carried forward。17C Future Studies 項目 5。独立小節を新設** | `documented` |

**36 年間で addressed within scope となったのは 3 項目、carried forward が 4 項目である。**

17C 自身は「four of the items」に対応したとするが、上の突合せで明確に対応づけられるのは項目 3・4・5 の三つである。**17C は四項目の内訳を明示していない。3+4+1 という配分は本ノートの `[ANALYTIC CODING]` であり、確立事項ではない。**

### 5.4 17C が新規に追加した未解決問題（`documented`）

> 6. Guides for estimating dynamic flood frequency curves that vary with time, incorporating climate indices, changing basin characteristics, and addressing potential nonstationary climate conditions;
> 7. Frequency estimation in cases where long-term trends are evident in the data but are not readily explainable by the history of land use, land use practices, or engineering modifications of the river or flood plain; and
> 8. **An examination and redefinition of risk, reliability, and return periods under nonstationary conditions.**

---

## 6. Coded Documentary Items

**この表は 20 件の独立事例ではない。** 同一本文箇所が複数行に符号化されている場合がある。分類は分析者側の coding scheme である `[ANALYTIC CODING]`。

**v0.2 での変更:** `Documentary form` 欄と `Modality` 欄を分離した。v0.1 は前者に "mandatory procedure"、後者に "recommended" を書いて矛盾していた。Modality 欄には文書の法助動詞のみを転記する。

| ID | 記述内容 | 記述の出所 | 17B での扱い | 17C での扱い | Documentary form | Modality | 下流への関係 | 確度 |
|---|---|---|---|---|---|---|---|---|
| NK-01 | 低い方の外れ値が当てはめに影響 | 統計手法研究（Cohn et al. 2013） | Grubbs-Beck + CPA | MGBT による PILF 識別 | recommended default procedure | should | 低頻度洪水量の推定値が変わりうる | `documented` |
| NK-02 | historic / paleoflood 情報の点値表現の制約 | 17B Future Studies #4、EMA 研究 | pp.12-2〜12-4 の逐次調整 | interval 表現 + perception threshold + EMA | recommended default procedure + データ表現規約 | should | 長期記録地点で推定が変わる | `documented` |
| NK-03 | 17B の CI が skew の不確かさを無視 | 17C 本文が明記 | Appendix 9 | skew 不確かさと historic 情報を反映 | uncertainty statement + 差異の警告 | 記述的 | 17B 由来 CI は過小の可能性を 17C が明言 | `documented` |
| NK-04 | 17B 調整手順の適用順序が恣意的 | 17C 本文 "arbitrary selection of a sequence" | 逐次適用 | EMA による統合 | 手法統合 | should（EMA が本体手順） | 同一データで解析者差が生じえた | `documented` |
| NK-05 | Plate 1 の精度不足 | 17B 自身の留保、後の Bayesian GLS 研究 | Plate 1 を提供、詳細研究を推奨 | **「IACWD (1982, plate 1) の推定値は使用を推奨しない」**（2 箇所） | explicit obsolescence declaration | not recommended | **17B Plate 1 依拠の推定値が下流に残存** | `documented` |
| NK-06 | 混合母集団を単一分布で扱う誤り | 17B #2、地域研究群 | 未解決として登録 | 事例列挙 + 分離解析を許容 + **「作業部会は評価していない」** | applicability condition + default rule + non-evaluation | **shall**（客観基準で分離不能なら単一母集団） | 分離判断が推定値を動かす | `documented` |
| NK-07 | 暦期間による系列分割 | 17C 本文 | 未確認 | 「水文学的に妥当と見なさない」 | explicit prohibition | 禁止 | 恣意的分割の防止 | `documented` |
| NK-08 | 見かけのトレンドからの非定常性推論 | Cohn & Lins 2005 ほか | 未確認 | 「定常性は確率過程の性質であり観測データの性質ではない」 | conceptual statement | 記述的 | トレンド検出＝非定常性の短絡を抑止 | `documented` |
| NK-09 | 説明できない多十年トレンド | 17C 本文 | 未確認 | 「最も厄介な問題の一つ」「評価していない」「**未解決問題である**」 | explicit unresolved issue | 物理機構調査を推奨 | 該当地点に手順がない | `documented` |
| NK-10 | 系列相関による不確かさ推定の誤り | Tasker 1983 ほか | 未確認 | effective record length 補正 | correction procedure | should | CI 幅に影響 | `documented` |
| NK-11 | 漸進的流域変化は記録に残らない | 17C 本文 | 未確認 | 「文書化されない可能性が高い」「累積効果は大きくなりうる」 | warning | 記述的 | 記録に無いこと≠変化が無いこと | `documented` |
| NK-12 | 流域改変記録の非均質性 | 17B #8 の系譜 | 未解決として登録 | 「一定の流域条件を表す記録のみ使用すべき」+ **「評価しておらず特段の推奨を行わない」** | applicability condition + non-evaluation | should | 都市化流域での適用可否 | `documented` |
| NK-13 | 気候変動・気候変動性 | 17C 本文 | 該当なし | **「時間不変性が仮定された」**。逸脱時は文書化と正当化を要求 | explicit assumption declaration + 条件付き逸脱許可 | 逸脱時の文書化を要求 | 標準が自らの仮定を明示 | `documented` |
| NK-14 | 推定値の陳腐化 | 17C 本文 | 未確認 | 「数年後には古くなっている可能性」「差異が現れた場合は認識し説明すべき」 | update trigger + reconciliation requirement | should | **過去推定との差異の説明。Case 01 に直接対応** | `documented` |
| NK-15 | 年超過確率の誤読 | 17B §VI.B の系譜 | Risk 節 + Appendix 10 | 独立節 "Risk Accumulates" | dedicated warning section | 記述的 | 意思決定者向けの誤読防止 | `documented` |
| NK-16 | 記録長不足での適用 | 17B・17C 双方 | 最小記録長規定 | 「10 年未満は信頼できない」「AEP 0.005 未満は補強を要する」 | applicability condition（数値閾値） | 記述的 | 短記録地点の信頼範囲 | `documented` |
| NK-17 | 記録外への外挿 | 17C 本文 | 「相当の裁量を許す」 | 精度劣化と三つの理由を明示 | warning + 理由の明示 | 記述的 | 0.2% AEP 等の下流利用 | `documented` |
| NK-18 | 特異事象データの混入 | 17C Applicability | 未確認 | ダム決壊・アイスジャム・導水は調整なしに使用すべきでない | data exclusion rule | should not | 記録の前処理判断 | `documented` |
| NK-19 | 標準からの逸脱の無管理 | 17B §VII.A、17C Applicability（ほぼ同文で継承） | 逸脱は研究で裏付け、推奨手順との比較を伴う | 同文 + Subcommittee への報告要請 | deviation control + feedback channel | **must**（裏付けと比較） | 逸脱事例が改訂へ還流する経路 | `documented` |
| NK-20 | 未評価事項を「問題なし」と読まれること | 17B §VII.B、17C 複数箇所 | 「plotting position の優劣は研究しておらず推奨は行わない」 | "The Work Group did not evaluate..." が 4 箇所 | non-evaluation declaration | 記述的 | 「未評価」と「不要」の区別 | `documented` |

---

## 7. Documentary Forms Observed

`[ANALYTIC CODING]`。**v0.2 では「保存機構」と呼ばない。** 観察されたのは文書形式であり、その機能的効果は測定していない。

### A. 後続版から先行版 future-work list への参照

17C が 17B の p.27–28 を名指しで参照した（§5.1）。**確認できるのは二時点・一件の参照である。** v0.1 の「常設の未解決問題台帳」「改訂時に照合される」は、議事録なしには言えない。削除。

**P0 検査の結果、これは技術標準運用の一般形式である公算が高い**（§12 N-05）。

### B. 明示的な陳腐化宣言

NK-05。17C は 17B Plate 1 について「使用を推奨しない」と本文中 2 箇所で述べる。先行版の特定成果物を名指しで退役させる形式。

### C. Non-evaluation declaration

NK-20。「作業部会は〜を評価しなかった」が 17B（plotting position）と 17C（混合母集団・流域変化・気候変動性・多十年トレンド）に現れる。

`limitation`（できないと分かっている）とも `warning`（危険だと分かっている）とも異なり、**推奨しない理由が「否定的評価」ではなく「未評価」であることを明示する**形式である。

**v0.1 は「下流の読者は『記載がない＝問題がない』と読めなくなる」と書いたが、これは効果の主張である。削除。** 言えるのは文書が書き分けていることまで。**なお P0 検査では、この形式は generic baseline に見つからなかった**（§12 N-05）。現時点で当該系列に固有である可能性が最も高い形式である。

### D. 逸脱制御と報告要請

NK-19。17B §VII.A と 17C Applicability がほぼ同文で、逸脱の裏付け・**推奨手順の結果との比較併記**・Subcommittee への報告を求める。第二項により逸脱の効果が定量的に可視化される。

### E. 統計的検査と物理的理解の対の要求

17C は多十年トレンド検出時に物理機構の調査を推奨し、混合母集団の分離に「客観的かつ**水文学的に意味のある**基準」を要求する（NK-06, NK-09）。統計的分離可能性だけでは不十分と明文化されている。

### F. 仮定の明示宣言

NK-13。「これらのガイドラインの策定において時間不変性が仮定された」。

### G. 更新契機と過去推定値との照合要求

NK-14。追加データだけでも再評価の理由になること、新推定が過去と異なる場合に差異を認識し説明することを要求する。

### H. 下流側の参照更新規約

FEMA GD 71 は「Mapping Partner は **Bulletin 17C およびその後続の修正**に従って解析すべきである」と記す（`documented`）。前方参照により参照先が生きた標準に接続される。同文書には **Table of Revisions** があり、2019 年 2 月改訂として「Bulletin 17C への参照を改訂した」と記録されている。逸脱には Regional Project Officer との調整を求める。

### I. 下流文書による上流標準の制限（v0.2 新設。C-1 由来）

FEMA GD 71（p.8）:

> "The Mapping Partner **must not** make expected probability adjustments to the Bulletin 17C frequency curve or alternative analysis if performed (National Academy of Sciences, 1978)."

**上流標準に含まれない制限を、下流の規制ガイダンスが外部典拠つきで課す形式。** 当該文書で数少ない "must not" の一つである。`documented`

### J. 適用範囲外の他機関委譲（v0.2 新設。C-2 由来）

FEMA GD 71（pp.7–8）は、混合母集団と規制流量について 17C の該当節に加え、**USACE EM 1110-2-1415 (1993)** を名指しで参照する。適用範囲外の担当が別機関・別文書形式へ委譲されている。`documented`（配置）／`unknown`（委譲先の評価状況）

---

## 8. Limits and Gaps in the Documentary Record

### L-01（訂正版）— expected probability の記録位置

Bulletin 17B §VI.C および Appendix 11 の expected probability は、Bulletin 17C 本文に出現しない。**17C 内に退役理由の記述を発見できなかった。**

一方、FEMA GD 71（2019, p.8）は当該調整を "must not" として明示的に禁止し、National Academy of Sciences (1978) を典拠に挙げる。

したがって観察されるのは消滅ではなく、**退役の記録位置が上流標準ではなく下流ガイダンスにあり、典拠が Bulletin 系列外の外部レビュー機関である**という配置である。`documented`

**v0.1 の「明示的退役と無言の消滅が併存」は誤りだった。** 正しくは、退役の記録位置が上流・下流の二層に分かれている。

### L-02 — 下流ガイダンスにおける語彙分布（射程を限定）

FEMA GD 71（Feb 2019、25 頁）の全文検索:

| 語 | 出現回数 |
|---|---|
| `17C` | 16 |
| `17B` | 0 |
| `uncertaint` | **0** |
| `nonstation` | **0** |
| `climate` | 1（閉鎖流域湖の水位変動の文脈のみ） |
| `urbaniz` | 3 |
| `must not` | ≥1（expected probability 禁止） |

**v0.2 での重要な但し書き。** v0.1 はこれを「語彙の減衰」と読んだが、C-1 の発見により修正が必要である。同文書は uncertainty の語を持たない一方で、**手法レベルの実質的な禁止（"must not"）を課している**。したがって「不確かさに無関心」とは読めない。

確認できるのは、**この一文書において不確かさが語彙として現れないこと**のみである。FEMA のガイダンス体系は複数文書に分かれており、他文書での扱いは未確認。**「FEMA が不確かさを扱っていない」とは述べない。**

### L-03 — 未解決課題の長期滞留（`documented`）

混合母集団・無観測地点・都市化／貯水池・降水情報の統合は、1982 年から 2018 年まで carried forward された。**文書上の連続性があることと、問題が解決することは別である。**

### L-04（訂正版）— 適用範囲外の担当配置

Bulletin 17C は自らの適用範囲外を明示する。

> "The procedures do not cover watersheds where flood flows are appreciably altered by reservoir regulation, watershed changes, or hydrologic nonstationarities, or where the possibility of unusual events, such as dam failures, must be considered."

**同一文書形式の中では**代替手順を標準化していない。しかし連邦全体としては USACE EM 1110-2-1415（1993）等が存在し、FEMA GD 71 がこれを名指しで参照する。

したがって観察されるのは手引きの不在ではなく、**適用範囲外の担当が別機関・別文書形式へ委譲されている**という配置である。`documented`（配置）／`unknown`（委譲先が Bulletin と同等の評価を受けているか）

**v0.1 の「国家的手引きは存在しない」は範囲超過であり、かつ v0.1 自身が抽出したテキスト内に反証があった。**

### L-05 — 未取得資料（本調査の限界）

Bulletin 15・17・17A 原文、USGS OFR 2017–1064、USACE EM 1110-2-1415、HFAWG 議事録。

---

## 9. Nonstationarity as a Stress Test

### 9.1 17C の姿勢は課題登録であって解決ではない（`documented`）

17C は同時に次を行う。

1. 時間不変性を仮定したと明示（NK-13）。
2. 気候変動性を扱う手法を評価していないと明示（NK-20）。
3. 科学的根拠がある場合の時変パラメータ使用を許可し、文書化と正当化を要求。
4. 参考情報源を 5 つ列挙。
5. 非定常性関連の未解決問題を Future Studies に 3 項目登録。

### 9.2 両方向の誤推論への注意（`documented`）

- **「トレンドが見えても非定常とは限らない」** — 定常性は確率過程の性質であり観測データの性質ではない（NK-08）。
- **「変化が見えなくても変化がないとは限らない」** — 漸進的流域変化は記録に残らない（NK-11）。

**両方向の注意が同一文書内に併存している。** ただしこれは検出限界についての注意であり、検出されなかった場合の規範的手順は与えていない。

### 9.3 「統計の消費期限」に対応する文書上の記述（`documented`、ただし単一概念ではない）

| 直感的表現 | 文書上の対応物 | 性格 |
|---|---|---|
| 統計には有効期間がある | NK-14。追加データによる再評価契機 | **標本情報の増加**による更新 |
| 対象系が変わる | NK-12, NK-13, L-04 | **母集団の変化**。統計的不確かさでは扱えないと明示 |

**この二つは文書上で明確に分離されている。** 後者に対して 17C は手順を与えず、適用範囲外と宣言し、担当を他機関へ委譲する（L-04 訂正版）。

「統計の消費期限」は単一概念としては当該系列の語彙に存在しない。存在するのは、標本の更新契機と母集団同一性の適用条件という二つの別条項である。

---

## 10. Relation to HYD-A01

**audit verdict は出さない。**

### 10.1 2020 FIS の qualification の起源（`plausible`）

HYD-A01 で確認された FIS の記述は、§7 の文書形式と主題的に対応する。**ただし個別 FIS 文言を Bulletin 系列の特定条項の帰結として結び付ける証拠は得ていない。**

### 10.2 Case 01 の false-positive control

| Case 01 で「落ちた」と見えうるもの | 参照連鎖上の所在 |
|---|---|
| FIS に不確かさの完全な記述がない | source（USGS SIR）側の confidence limits、17C 本体の CI 手順 |
| FIS に非定常性の議論がない | 17C が時間不変性を仮定したことを明示（NK-13） |
| FIS に手法の限界記述がない | 17C Applicability 節と Future Studies 節 |
| FIS に将来変化の扱いがない | FIS 自身の amendment 条項 + 17C の更新契機（NK-14） |
| **FIS に expected probability の扱いがない** | **FEMA GD 71 が "must not" で禁止（L-01 訂正版）** |

**Case 01 では、target artifact に書かれていないことを omission と判定する前に、参照連鎖上の所在を最低 3 段（source report / Bulletin / FEMA guidance）確認する必要がある。** v0.2 では、下流ガイダンス層に上流標準への制限が置かれうること（§7-I）が加わったため、**FEMA guidance 層の確認は省略できない**。

### 10.3 Case 01 で検査すべき候補（優先順）

1. **NK-05（Plate 1 退役）:** 17B Plate 1 の regional skew に依拠した推定値が、17C の不使用勧告後も有効な FIS/FIRM に残存しているか。
2. **L-01 訂正版（expected probability）:** FEMA の "must not" 以前に作成された FIS に、当該調整を適用した推定値が残っているか。**v0.2 で新規に浮上した、最も証拠として扱いやすい候補。**
3. **NK-14（照合義務）:** 推定値が更新された地点で、過去推定値との差異が「認識され説明された」記録が存在するか。
4. **NK-03（CI 過小）:** 17B 由来 CI を引用する下流文書が、17C の指摘を反映しているか。

---

## 11. Questions for Later Comparative Cases

一般法則化しない。**他分野で同型が存在するかを問う質問形式**としてのみ持ち出す。

1. 後続版が先行版の future-work list を参照する慣行があるか。
2. 「評価していない」と「問題がない」を書き分ける定型表現があるか。
3. 先行版の特定成果物を名指しで退役させる慣行があるか。
4. 逸脱時に標準手順との比較併記を求めるか。
5. 標準が自らの前提を一文で名指しするか。
6. 推定値の更新時に過去推定との差異の説明を求めるか。
7. 検出限界について両方向の誤推論に注意を向けているか。
8. 適用範囲外の空白の所在が明示されているか。
9. 下流ガイダンスが上流標準を固定版参照か前方参照か。
10. **下流文書が上流標準の一部を制限・禁止する形式があるか**（v0.2 追加）。
11. **適用範囲外の担当を他機関へ委譲する形式があるか**（v0.2 追加）。

**満たされない分野が劣っているという推論をしない。**

---

## 12. Negative / Null Findings

### N-01 — 破局的事象と改訂を結ぶ documented な因果を発見できなかった

17B・17C の本文中に、特定の洪水災害が特定の改訂を引き起こしたという記述を**発見できなかった**。documented な起源は、文献レビュー、作業部会メンバーの実務経験、選定を助ける特別研究（Beard 1974）、Monte Carlo 検証（Cohn et al.、OFR 2017–1064）、観測所データによる試験である。

**「失敗から学んだ」という物語は本調査で裏付けられなかった。**

### N-02 — 記述形式は「注釈」が主ではなかった

主要形態は構造的なものだった。常設リスト、定型句、手続的ゲート、明示的退役宣言、節の新設。

### N-03 — 暗黙化を示す証拠を発見できなかった（control finding）

Bulletin 系列の文書内では逆向きの証拠のみを発見した（仮定の明示、陳腐化の明言、逸脱時の比較併記、誤読への独立節）。

**ただしこれは標準文書内の話である。** 標準を使う実務、下流アーティファクト、一般利用者の理解において暗黙化が起きていないことは示していない。

### N-04 — 記述形式の有効性を示す証拠をほとんど発見していない

形式が**存在する**ことは示した。それが**機能している**ことは、17C が 17B の p.27–28 を名指しした一点を除いて確認していない。HFAWG 議事録が未調査。

**v0.2 での縮小:** OFR 2017–1064 の存在により、改訂案が採択前に評価工程を経たことは documented になる。ただしこれは改訂手続に評価工程があることの証拠であって、過去の記述が忘却を防いだことの証拠ではない。

### N-05 — 技術ガイダンス一般の通常運用である可能性（v0.2 新設、**かつ部分的に確証済み**）

観察された特徴が、洪水頻度解析に固有ではなく技術ガイダンス一般の運用である可能性。

**v0.2 公開時点で、この null は P0 検査により部分的に確証された。** 詳細は [`p0_generic_standards_baseline_v0.1.md`](./p0_generic_standards_baseline_v0.1.md)。要点のみ:

- ISO/IEC Directives + IEC Supplement には、**未処理コメントを次回 systematic review のために公式カテゴリ（"Non-actionable – Comments preserved for historical record only"）として保存し、archive を義務づける規定がある。** すなわち §7-A（future-work list の継承）に相当する機構は、技術標準運用の一般形式として制度化されている。
- 版管理、退役、更新契機、逸脱手続、文書化要求、他機関委譲は、いずれも generic baseline で再現された。
- **再現されなかったのは non-evaluation declaration（§7-C）と、下流からの上流制限（§7-I）のみである。**

したがって §7 の 10 形式のうち、当該ガイダンス系列に固有である可能性が残るのは 2 形式である。

---

## 13. Open Questions

1. Bulletin 15・17・17A 原文の取得。
2. HFAWG 議事録。N-04 の空白を直接埋める。
3. expected probability の退役理由（NAS 1978 報告の内容）。
4. PSIAC 1966 *Limitations in Hydrologic Data as Applied to Studies in Water Control Management*。
5. FEMA の不確かさ扱い（L-02 の射程確定）。riverine mapping guidance、MT-2、CNMS。
6. 17B Plate 1 依拠推定値の残存（§10.3-1）。
7. **FEMA "must not" 以前の FIS における expected probability 適用の残存**（§10.3-2、v0.2 新設）。
8. USACE EM 1110-2-1415 の取得（L-04 訂正版）。
9. 他国標準との比較（英国 FEH、豪州 ARR）。
10. USGS OFR 2017–1064 の取得。

---

## 14. Sources

### 一次資料（全文取得・検索済み）

1. Interagency Advisory Committee on Water Data, Hydrology Subcommittee, 1982, *Guidelines for Determining Flood Flow Frequency*, Bulletin 17B（Revised September 1981, Editorial Corrections March 1982）— [PDF](https://pubs.usgs.gov/unnumbered/70275162/report.pdf)
   - 参照箇所: §VI.B Risk（p.24）、§VI.C Expected Probability（p.24）、§VII.A Non-conforming Special Situations（p.25）、§VII.B Plotting Position（p.26）、**§VII.C Future Studies（pp.27–28）**、Appendix 5、Appendix 11、Appendix 14。

2. England, J.F., Jr., Cohn, T.A., Faber, B.A., Stedinger, J.R., Thomas, W.O., Jr., Veilleux, A.G., Kiang, J.E., and Mason, R.R., Jr., 2018, *Guidelines for determining flood flow frequency—Bulletin 17C*（ver. 1.1, May 2019）: USGS Techniques and Methods, book 4, chap. B5, 148 p. — [doi:10.3133/tm4B5](https://doi.org/10.3133/tm4B5)
   - 参照箇所: Abstract、Introduction / Background、Purpose and Scope、Risk Accumulates、Common Issues with At-Site Data Records、Data Assumptions and Specific Concerns（pp.20–23）、Estimating Regional Skew、Frequency Curve Extrapolation、**Future Studies（pp.35–36）**、**Applicability of These Guidelines（pp.36–37）**、Appendix 3、Appendix 4。

3. Federal Emergency Management Agency, 2019, *General Hydrologic Considerations*, Guidance for Flood Risk Analysis and Mapping, Guidance Document 71, February 2019, 25 p. — 取得経路: [Kentucky Transportation Cabinet mirror](https://transportation.ky.gov/Highway-Design/Drainage%20Manual/FEMA%20-%20General%20Hydrologic%20Considerations%20Guidance%20-%20Feb%202019.pdf)
   - 参照箇所: Table of Revisions（p.ii）、§4 Hydrologic Analysis Methods（pp.7–8。gage 解析、Bulletin 17C 参照、**expected probability の禁止**、**USACE EM 1110-2-1415 への参照**、RPO 調整規定）。

### 17B / 17C を通じてのみ参照（原文未取得）

4. USWRC, 1967, Bulletin 15. ／ 5. USWRC, 1976, Bulletin 17. ／ 6. USWRC, 1977, Bulletin 17A.
7. Beard, L.R., 1974, *Flood Flow Frequency Techniques*, Univ. of Texas at Austin.（17B Appendix 14 に要約）
8. Cohn, T.A., and others, 1997, 2001, 2013（EMA・MGBT の基礎研究）
9. Cohn, T.A., and Lins, H.F., 2005（NK-08 の典拠）
10. National Academy of Sciences, 1978（FEMA GD 71 が expected probability 禁止の典拠として引用。**v0.2 新規**）

### 所在確認済み・未取得

11. Cohn, T.A., England, J.F., Jr., and others, 2017, *Evaluation of Recommended Revisions to Bulletin 17B*: USGS Open-File Report 2017–1064. — [PDF](https://pubs.usgs.gov/of/2017/1064/ofr20171064.pdf) **（Codex review により発見。v0.2 新規）**
12. USACE, 1993, *Hydrologic Frequency Analysis*, EM 1110-2-1415.（**C-2 により必要性判明。v0.2 新規**）
13. PSIAC Hydrology Subcommittee, 1966, *Limitations in Hydrologic Data as Applied to Studies in Water Control Management*.
14. HFAWG 議事録 — https://acwi.gov/hydrology/Frequency/minutes/index.html

---

## Current verdict

### **Documentary continuity identified; preservation effectiveness untested**

**確認できたこと。** 本調査が検討した米国連邦洪水頻度ガイダンス系列には、認識された限界・未解決課題・未評価事項を記載し、後続版から参照可能にする複数の documented な文書形式が存在する。最も直接的なのは、Bulletin 17B（1982）の future-work list が Bulletin 17C（2018）で明示的に参照され、3 項目が addressed、4 項目が carried forward されたことである。加えて、明示的退役宣言、non-evaluation declaration、逸脱制御と報告要請、仮定の明示宣言、更新契機と照合要求、下流文書による上流標準の制限、他機関への委譲が、いずれも一次資料の本文から確認できた。

**確認できていないこと。** 実際の参照・利用・下流伝達・忘却防止効果は、いずれも測定していない。**文書上の再発見可能性は残ったが、それ以上は言えない。**

**主題の訂正。** 記載されているのは主として方法論的限界と未評価領域の知識である。本調査の範囲では、特定の災害が特定の改訂を引き起こしたという documented な因果を一件も発見できなかった（N-01）。改訂の documented な起源は、比較研究・Monte Carlo 検証・文献レビュー・作業部会の実務経験である。

**固有性の主張を撤回する。** v0.1 は「通常の標準改訂では説明しにくい形式が二つある」として future-work list の継承と non-evaluation declaration を挙げた。**P0 検査により、前者は技術標準運用の一般形式であることが確認された**（N-05）。ISO/IEC の枠組は、未処理コメントを次回 systematic review のために公式カテゴリとして保存し archive を義務づけており、Bulletin 17B の Future Studies リストより形式化されている。

**現時点で当該系列に固有である可能性が残るのは、non-evaluation declaration（§7-C）と、下流文書による上流標準の制限（§7-I）の二形式のみである。** いずれも比較検査は未完了である。

---

## What this analysis established

1. **後続版が先行版の future-work list を参照した事例が documented である。** 17B の 8 項目のうち 3 項目が addressed、4 項目が carried forward された。**ただしこの形式は技術標準一般に存在する**（N-05）。

2. **"The Work Group did not evaluate..." という定型句が、限界とも警告とも別の記述カテゴリを構成している。** P0 検査の generic baseline には見つからなかった。**現時点で最も固有性の見込みが高い形式である。**

3. **改訂の documented な起源は災害ではなく方法論研究だった。** 分析前の予想と反する。

4. **退役の記録位置は上流標準と下流ガイダンスの二層に分かれている。** Plate 1 は 17C 本文が退役させ、expected probability は FEMA が外部典拠つきで禁止した。**v0.1 の「無言の消滅」は誤りだった。**

5. **適用範囲外の担当は空白ではなく他機関へ委譲されている。** USACE EM 1110-2-1415。**v0.1 の「国家的手引きは存在しない」は誤りだった。**

6. **「統計の消費期限」は単一概念としては存在せず、標本更新契機と母集団同一性条件の二条項に分離されていた。**

7. **検出限界について両方向の誤推論に注意が向けられている。**

---

## v0.2 で確立するもの

- 版系譜と 17B future-work 8 項目の 17C における状態。
- 一次資料本文から引用可能な 20 件の coded documentary items。
- 10 種の documentary form（うち 2 種は v0.2 新設）。
- 5 件の限界・空白（うち 2 件は v0.1 の事実誤りの訂正）。
- 5 件の null finding（うち N-05 は P0 により部分的に確証）。
- Case 01 に対する検査候補 4 件（優先順位つき）。

## v0.2 で確立しないもの

- 記述形式が機能していること。
- 当該系列に固有の形式が存在すること（残り候補 2 形式は未検査）。
- 文書構造が検索・利用・判断を改善すること。
- 水文学が他分野より優れていること。
- Case 01 の positive / negative 判定への含意。

## 次の作業

§13 の open question のうち 2（HFAWG 議事録）と 7（expected probability 適用の残存）を優先する。前者は N-04 の空白を直接埋める。後者は v0.2 で新規に浮上した、Case 01 にとって最も証拠として扱いやすい検査候補である。

# Comparative Study Design v0.1 — Operational Fixing and Retained Qualification in Technical Guidance

## 権威ある科学・技術ガイダンスが、推定・手順・推奨を運用上固定する際に、何を同時に固定せず記録しているか

- **バージョン:** 0.1
- **日付:** 2026-08-21
- **種別:** study-design proposal / working note（完成論文ではない）
- **前提資料:** [`hydrology_negative_knowledge_preservation_note_v0.1.md`](./hydrology_negative_knowledge_preservation_note_v0.1.md) および同ノートに対する Codex adversarial review
- **姉妹ノート:** [`case_01_hydro_target_artifact_discovery_v0.1.md`](./case_01_hydro_target_artifact_discovery_v0.1.md)

---

## 0. 本設計が採用した制約

Codex review の制約をすべて採用する。加えて、**本設計の作成中に Codex の二つの事実主張を独立検証し、いずれも正しいことを確認した。** その結果、前提資料である水文学ノートに**事実誤り二件と内部矛盾一件**が見つかった。Part I はその訂正から始める。

以後、次の語は観測事実として使わない。

| 使わない語 | 代わりに使う語 |
|---|---|
| negative knowledge preservation | qualification and open-problem recording |
| preservation mechanism | documentary form / revision practice |
| permanent ledger | cross-edition future-work list |
| prevented forgetting | remained documentarily available |
| re-foregrounding cost management | later retrieval or reconsideration（効果は未測定） |
| solved | addressed within the stated scope |
| 20 preservation cases | 20 coded documentary items |

`prediction demand ↔ epistemic restraint` は一次コードにしない。分析後にのみ解釈語として検討する。

---

# Part I — Hydrology revision proposal

## I-1. 事実訂正（最優先。中立化より前に行う）

### 訂正 1 — L-01「expected probability の無言の消滅」は誤り

**現在の記述:** Bulletin 17C 本文に "expected probability" が出現しないことをもって「無言の消滅」とし、Plate 1 の明示的退役と対比させた。

**検証結果:** FEMA *General Hydrologic Considerations*, Guidance Document 71（February 2019）p. 8 に次の記述がある。

> "The Mapping Partner **must not** make expected probability adjustments to the Bulletin 17C frequency curve or alternative analysis if performed (National Academy of Sciences, 1978)."

したがって当該手法は体系から無言で消えたのではなく、**下流の規制ガイダンス層で、外部典拠（NAS 1978）を伴う明示的な禁止として退役している。** しかも FEMA 文書中で数少ない "must not" の一つである。

**訂正後の記述案:**

> **L-01（訂正版）** Bulletin 17B §VI.C および Appendix 11 の expected probability は、Bulletin 17C 本文には出現しない。17C 内に退役理由の記述を発見できなかった。一方、FEMA Guidance Document 71（2019, p. 8）は当該調整を "must not" として明示的に禁止し、National Academy of Sciences (1978) を典拠として挙げる。したがって観察されるのは「消滅」ではなく、**退役の記録位置が上流標準ではなく下流ガイダンスにあり、かつ典拠が Bulletin 系列外の外部レビュー機関である**という配置である。`documented`

**この訂正は元の所見より重要な観察を生む。** 退役は上流標準の中だけで起きるとは限らず、下流の規制文書が上流標準に対する制限として実装する経路が存在する。これは Part V の抽出スキーマに独立コードとして追加すべき現象である（`downstream-imposed restriction on upstream standard`）。

### 訂正 2 — L-04「国家的手引きは存在しない」は範囲超過

**現在の記述:** 「標準が適用されない地点が存在することは明示されているが、その地点でどうすべきかの国家的手引きは存在しない。」

**検証結果:** 誤り。FEMA GD 71（2019, p. 7–8）は、混合母集団および規制流量について次を指示している。

> "the Mapping Partner should refer to the mixed population section of Bulletin 17C, Guidance: Ice Jams, or **USACE Hydrologic Frequency Analysis EM No. 1110-2-1415 (USACE, 1993)**."
> "USACE EM No. 1110-2-1415 (USACE, 1993) describes techniques for several situations in which the analyses may require adjustments to gage data to make a homogenous dataset. For example, guidance is available for analyzing gage records containing regulated and unregulated flow values."

すなわち規制流量・混合母集団については、別の連邦機関の技術マニュアルが存在し、FEMA がそれを名指しで参照している。

**訂正後の記述案:**

> **L-04（訂正版）** Bulletin 17C は自らの適用範囲外を明示するが、**同一文書形式の中では**代替手順を標準化していない。連邦全体としては USACE EM 1110-2-1415（1993）等が存在し、FEMA GD 71 はこれを名指しで参照する。したがって観察されるのは手引きの不在ではなく、**適用範囲外の担当が別機関・別文書形式へ委譲されている**という配置である。委譲先の手順が Bulletin と同等の評価を受けているかは未確認。`documented`（配置について）／`unknown`（委譲先の評価状況）

**この訂正も所見を改善する。** 「空白」ではなく「機関間の担当委譲」であり、比較研究にとってはこちらの方が観察可能な対象である。

### 訂正 3 — 内部矛盾の削除

Current verdict の「保存機構は忘却を防いだが、解決も、下流への完全な伝達も保証していない」は、N-04（有効性は未確認）と矛盾する。Codex の指摘は正しい。

**訂正後:**

> 文書上の再発見可能性は残った。実際の参照・利用・下流伝達・忘却防止効果は、いずれも本調査で測定していない。

### 追加 4 — N-04 の部分的充填（Codex が発見した一次資料）

Codex は本調査が見落とした一次資料を挙げている。

> Cohn, T.A., England, J.F., Jr., and others, 2017, *Evaluation of Recommended Revisions to Bulletin 17B*: U.S. Geological Survey Open-File Report 2017–1064. — [PDF](https://pubs.usgs.gov/of/2017/1064/ofr20171064.pdf)

これは 17B からの提案改訂の統計的性能を Monte Carlo で評価した正式報告である。**改訂案が採択前に評価段階を経たことは、これにより documented になる。** ただしこれは「改訂手続に評価工程がある」ことの証拠であって、「過去の qualification 記録が忘却を防いだ」ことの証拠ではない。N-04 の空白は縮小するが消えない。

## I-2. 中立化（Codex 提案を採用）

| 箇所 | 現在 | 訂正案 |
|---|---|---|
| タイトル | Hydrology Negative-Knowledge Preservation Note | **Qualification, Open Problems, and Revision in U.S. Flood-Frequency Guidance — A Documentary Reconstruction of Bulletin 17B→17C**（旧題は historical working title として脚注に残す） |
| 主語 | 「水文学は」 | 「本調査が検討した米国連邦洪水頻度ガイダンス系列は」 |
| §1 動機 | 「三層が衝突するため標準文書自身が書き分ける必要が生じた」 | 「ガイダンスには統計的推定・物理過程・制度的利用に関する異なる条件が併記されている。本ノートはその担当区分を復元する」（因果史を主張しない） |
| §2 研究質問 | 「どう保存されてきたか」 | 「認識された限界・偏り・不確かさ・未評価事項は、後続版でどのように記載・変更・削除・参照されたか」 |
| §5.3「解決」 | 解決 3 / 未解決繰越 4 | **addressed within Bulletin 17C** 3 / carried forward 4。「3+4+1」を確定事項として扱わず、17C 自身の "four items" と一致しないことを明記 |
| §6 台帳 | 「20 件の保存事例」 | 「20 件の coded documentary items（同一本文箇所が複数行に符号化されている場合がある。分類は分析者側の coding scheme である）」 |
| §6 mandatory 欄 | Preservation form に `mandatory procedure`、Mandatory? に `recommended` | 二欄を分離。Documentary form は `recommended default procedure` 等に統一。Modality 欄は文書の助動詞のみを転記（must / must not / shall / should / may / 記述的） |
| §7-A | 「常設の未解決問題台帳」 | 「後続版が先行版の future-work list を明示的に参照した事例（二時点、一件）」 |
| §7-C | 「下流の読者は『記載がない＝問題がない』と読めなくなる」 | 「文書が、推奨しない理由を『否定的評価』ではなく『未評価』として明示している」（効果は主張しない） |
| §7-C 評価 | 「第三のカテゴリ」「第一級の記載事項」 | 同左を維持してよいが、`[ANALYTIC CODING]` として明示し、他の技術標準との比較なしに固有性を主張しない |
| Current verdict | B. Partial preservation history identified | **Documentary continuity identified; preservation effectiveness untested** |
| verdict の C 却下理由 | 「通常の標準改訂では説明しにくい」 | **削除。** ISO/IEC Directives の systematic review・改訂・確認・廃止・コメント繰越が制度化されている以上、比較基準線なしにこの主張はできない（Part VII Null D） |

## I-3. 必須 Null の追加

§12 に次を正式な null として追加する。

> **N-05** 観察された特徴（scope specification、research agenda、revision、withdrawal、version control、非評価の明示）は、洪水頻度解析に固有の形式ではなく、**技術ガイダンス一般の通常の運用**である可能性がある。本調査は他分野・他標準との比較基準線を持たないため、この可能性を排除できていない。`documented`（比較を行っていないという事実）

## I-4. 学習項目の訂正

現行の「What did this analysis teach us」7 項目のうち、次を訂正する。

- **項目 4（退役は可能であり行使されている）** — 訂正 1 により補強される。ただし「無言の消滅も併存」は削除し、「退役の記録位置が上流標準・下流ガイダンスの二層に分かれている」に置き換える。
- **項目 2（non-evaluation が第三のカテゴリ）** — 「分野の実務が自力で到達した」を削除。比較基準線がない。`[ANALYTIC CODING]` として保持。
- **項目 3（起源は災害でなく方法論研究）** — 維持。OFR 2017-1064 の発見により補強される。

---

# Part II — Comparative research question

## II-1. 中心問い

> **How do authoritative scientific or technical guidance systems operationally fix estimates, procedures, or recommendations, while separately recording uncertainty, scope, non-evaluated cases, deviation conditions, update triggers, and retirement or supersession status — and in which document, in which form, under which modality?**

ユーザ提示案からの変更点は末尾の三つである。**どの文書に／どの形式で／どの法助動詞で**を明示的に問う。訂正 1（退役が下流文書にあった）と訂正 2（担当が別機関へ委譲されていた）が示すとおり、記録の**所在**が最も観察しやすく、かつ分野差が出うる変数だからである。

## II-2. 一次的な下位問い（すべて文書観察で答えられる形）

| コード | 問い |
|---|---|
| **RQ-1** | 運用上固定されているのは何か（量／手順／推奨／閾値）。その固定を述べる文の法助動詞は何か。 |
| **RQ-2** | 同時に固定されていない条件は、同一文書内・上流文書・下流文書・別機関文書のどこに記録されているか。 |
| **RQ-3** | 「評価していない」と「評価した結果推奨しない」は書き分けられているか。書き分けの定型表現は何か。 |
| **RQ-4** | 固定からの逸脱が許される条件と、その際の要求（文書化／比較併記／承認）は何か。 |
| **RQ-5** | 再検討・更新の契機は何として記述されているか（時間／新データ／外部事象／定期レビュー）。 |
| **RQ-6** | 先行版・先行手法の退役は、どの文書が、どの語で、どの典拠で宣言しているか。 |
| **RQ-7** | 下流の意思決定規則は、推定の不確かさをどう受け取っているか（伝播／閾値調整／無視／言及なし）。 |

## II-3. 問わないこと

- 忘却が防止されたか。
- 実務者の検索コスト。
- どの分野が優れているか。
- `prediction demand ↔ epistemic restraint` が存在するか。

これらはいずれも本設計の観察範囲外である。H3（Part VII）として仮説にとどめる。

---

# Part III — Field-native case selection

## III-1. 三分野の選定理由

| ケース | 役割 | 選定理由 | 予想される結果 |
|---|---|---|---|
| **A. Hydrology**（Bulletin 17B→17C→FEMA GD 71） | 候補コードの供給源 | すでに一次資料で復元済み。**ただしテンプレートとしては使わない。** 他二分野のコードがここから逸脱することを想定する | — |
| **B. Metrology**（VIM / GUM / JCGM 106 / 校正機関認定要件） | **最強の negative control** | 測定結果・不確かさ・トレーサビリティ・目的適合性・判定規則がすでに別語彙として制度的に分離済み。水文学で見えた分類が既存の計量学語彙へ完全吸収されるなら、共通語彙は不要という強い証拠になる | **吸収される可能性が高い。それが重要な negative finding** |
| **C. Clinical medicine / epidemiology**（GRADE handbook / EtD framework / 個別診療ガイドライン） | **推定と判断の分離の最強対照** | GRADE は evidence certainty と recommendation strength を明示的に分離する。水文学ノートが最も混線させた「推定」と「意思決定」を、制度として分離している唯一の候補 | 分離が明示的なぶん、hydrology の混線が**分野差ではなく文書型差**であることが露見しうる（Null A） |

## III-2. 追加すべき第四ケース — 一般技術標準ベースライン（本設計の主要な追加提案）

**Codex の Null D（ordinary guidance development で説明可能）は、仮説として保持するのではなく、ケースとして走らせるべきである。**

| ケース | 内容 |
|---|---|
| **D. Generic standards baseline** | ISO/IEC Directives Part 1（systematic review、confirmation / revision / withdrawal / stabilization の段階規定）＋ **科学とは無関係な技術標準を 1 件**（例：材料試験規格または建築関連規格を任意抽出） |

**理由。** 三つの科学分野だけを比較すると、共通して見えるものが「科学の特徴」なのか「標準文書の特徴」なのか区別できない。非科学的技術標準を同じ抽出スキーマにかけて同じコードが立つなら、本研究の対象は科学の認識論ではなく**標準文書の書式**であり、その時点で終了できる。

**これは最も安価な kill test であり、他の三ケースより先に走らせるべきである。**

## III-3. 第二段階（保留）

Climate science / IPCC は第四ケースではなく**第五ケース**とし、A–D の結果が出るまで着手しない。理由は、IPCC の calibrated language が最も「共通語彙」に近い見た目を持つため、早期に投入すると分析者側の枠組みを補強する方向のバイアスがかかるからである。

Machine learning と physics は当面除外する（Codex の指摘に同意。artifact type の混在が分野差を汚染する）。

---

# Part IV — Artifact-chain specification

## IV-1. 共通の連鎖テンプレート

```text
[L1] evidence / empirical data / model
        ↓
[L2] authoritative assessment or standard
        ↓
[L3] operational guidance / procedure specification
        ↓
[L4] decision artifact / downstream use
        ↓
[L5] revision / reassessment / withdrawal record
```

**厳守事項:** 比較は**同一 L 層どうしでのみ**行う。L2 ↔ L2、L3 ↔ L3。Bulletin 17C（L2）を個別診療ガイドラインの推奨文（L4）と比較しない。

## IV-2. 各ケースの具体的連鎖

### Case A — Hydrology

| 層 | 文書 | 取得状況 |
|---|---|---|
| L1 | Cohn et al., *Evaluation of Recommended Revisions to Bulletin 17B*, USGS OFR 2017–1064 | **未取得**（Codex が発見。最優先） |
| L2 | Bulletin 17C（USGS TM 4-B5, ver. 1.1, 2019） | 取得済・全文検索済 |
| L2′ | Bulletin 17B（IACWD 1982） | 取得済・全文検索済 |
| L3 | FEMA *General Hydrologic Considerations*, GD 71（Feb 2019） | 取得済・全文検索済 |
| L3′ | USACE EM 1110-2-1415（1993） | **未取得**（訂正 2 で必要性が判明） |
| L4 | Juneau FIS 02110CV000B（2020） | Case 01 で取得済 |
| L5 | 17B→17C 改訂記録、FEMA GD 71 Table of Revisions | 部分取得 |

### Case B — Metrology

| 層 | 文書（候補） |
|---|---|
| L1 | 個別の校正・比較測定報告 |
| L2 | JCGM 100 (GUM)、JCGM 200 (VIM) |
| L3 | JCGM 106（適合性評価における測定不確かさの役割、decision rule と guard band）、ISO/IEC 17025 |
| L4 | 校正証明書 1 件（実物） |
| L5 | GUM の改訂経緯、VIM 版管理 |

**注目点:** L3（JCGM 106）が L4（校正証明書）へ不確かさをどう伝播させることを要求するか。水文学 L3（FEMA GD 71）には uncertainty の語が 0 回だった（要再確認、L-02 の射程限定つき）。**この一点だけでも L3 層の直接比較になる。**

### Case C — Clinical

| 層 | 文書（候補） |
|---|---|
| L1 | 系統的レビュー 1 件 |
| L2 | GRADE handbook |
| L3 | GRADE EtD framework、特定学会のガイドライン作成マニュアル |
| L4 | 個別診療ガイドラインの推奨文 1 件（strength と certainty が併記されたもの） |
| L5 | living guideline の更新記録、推奨の撤回・変更事例 |

### Case D — Generic baseline

| 層 | 文書 |
|---|---|
| L2 | ISO/IEC Directives Part 1（systematic review 規定） |
| L2′ | 任意抽出した非科学的技術標準 1 件 |
| L5 | 当該標準の confirmed / revised / withdrawn 履歴 |

L1・L3・L4 は当該標準に存在する範囲で。

---

# Part V — Extraction schema

## V-1. 一次コード（分析者側の coding scheme であることを明示）

各文書について、**該当箇所の原文・文書内位置・法助動詞**を記録する。解釈は書かない。

| コード | 抽出対象 | 記録項目 |
|---|---|---|
| `FIX` | 運用上固定された量・手順・推奨 | 原文、位置、法助動詞 |
| `UNC` | 不確かさの限定 | 種類、定量／記述の別、位置 |
| `SCOPE` | 適用条件・適用範囲 | 原文、境界の指定方法（数値／記述） |
| `NONEVAL` | 未評価の明示 | 定型表現、対象、位置 |
| `OPEN` | 未解決課題 | 原文、リスト形式か散在か |
| `DEV` | 逸脱条件と逸脱時の要求 | 許可条件、要求（文書化／比較／承認） |
| `TRIG` | 更新・再検討の契機 | 契機の種類（時間／新データ／外部事象／定期） |
| `DOWN` | 下流の意思決定規則 | 不確かさの受け取り方 |
| `VER` | 版関係 | 参照が固定版か前方参照か |
| `RET` | 退役・撤回・置換 | 宣言文書、語、典拠 |
| `REF` | 参照連鎖 | 参照先、参照の向き |
| `DOC` | 文書化要求 | 何を記録させるか |

## V-2. 本設計で追加した二コード（訂正 1・2 に由来）

| コード | 抽出対象 | 由来 |
|---|---|---|
| **`RET-DOWN`** | **下流文書が上流標準の一部を制限・禁止する記述** | 訂正 1。FEMA が Bulletin 17C 曲線への expected probability adjustment を "must not" とした事例 |
| **`DELEG`** | **適用範囲外の担当を別機関・別文書へ委譲する記述** | 訂正 2。FEMA が規制流量・混合母集団について USACE EM 1110-2-1415 を参照した事例 |

この二つは、水文学ノートの初版では「消滅」「空白」として誤って記録されていた。**訂正によって初めて観察可能なコードになった。** 他分野で同型が見つかるかは未知であり、これが本比較研究で最も検証価値のある候補である。

## V-3. 記録しないもの

- 「保存されている」「再前景化できる」「抑制的である」といった機能判定。
- `prediction demand`／`epistemic restraint`。
- 分野間の優劣。

これらは Part VI-4 以降でのみ、二次的解釈として検討する。

## V-4. 分野固有コード

各ケースの field-native reconstruction 段階で、上記に収まらない項目が出た場合は**分野固有コードとして別枠に追加し、共通コードへ無理に写像しない**。写像できないことは結果である。

---

# Part VI — Comparison protocol

## VI-1. 手順

```text
Step 0  Generic baseline (Case D) を先に走らせる
          → 全コードが立つなら Part IX-1 で終了判定
Step 1  各ケースを field-native vocabulary のみで復元
          共通語彙・共通コードを一切使わない
          成果物：分野ごとの用語表と文書構造の記述
Step 2  第一分析者が V-1/V-2 スキーマで符号化（封印）
Step 3  第二分析者が独立に符号化（第一の結果を見ない）
Step 4  一致率と不一致理由を記録（不一致は削除せず保存）
Step 5  同一 L 層どうしでのみ機能対応を検討
Step 6  事前登録した 5 問への回答を各ケースで作成
Step 7  成果判定（Part XI）
```

## VI-2. Step 1 の厳格化

**共通語彙を当てる前に、各分野の文書が自分で使っている語だけで記述を完成させる。** 完成した記述を封印してから Step 2 に進む。Step 1 の記述に共通語彙が混入していた場合、その記述は破棄して書き直す。

これは Codex の Null C（構造は分析者の物語）への直接の対抗手段である。field-native 記述だけで各分野の運用が説明でき、比較表を作っても記述が改善しないなら、Null C が成立する。

## VI-3. 独立符号化の現実的制約（明記すべき限界）

独立分析者を二名確保できない場合、この設計は**再現性を測定できない**。その場合の代替は次の順で劣化する。

1. **最良:** 分野を知る第二分析者。
2. **次善:** 同一分析者の時間差二回符号化（第一回を封印、最低 1 週間空ける）。再現性ではなく**安定性**しか測れないと明記する。
3. **最低:** 単一符号化。この場合、Part XI の成功基準のうち「独立 reviewer 間の検索再現性」は**判定不能**とし、成果判定の上限を organizational value に固定する。

**単一分析者しかいない状態で方法論的価値を主張してはならない。**

## VI-4. 事前登録する 5 問（Step 6）

各ケースの L4 artifact 一件に対して、以下を **Step 0 の前に**登録する。

1. この artifact が用いた推定値は、現行の上流標準で退役・非推奨とされた手法に依拠しているか。
2. この artifact の適用範囲外条件は、artifact 自身から特定できるか。何 hop の参照が必要か。
3. この artifact が引用する不確かさは、下流の判定規則にどう入っているか。
4. この artifact の再評価契機は明示されているか。
5. この artifact の推定層と判断層は分離して記述されているか。

**各問について、field-native reviewer の回答（Group A）と、スキーマ利用者の回答（Group B）を比較する。** 回答が一致するなら、スキーマは診断を変えていない。

---

# Part VII — Null hypotheses

強い順に並べる。**Null D を最上位に置く。**

### Null D（最強）— ordinary guidance development

観察される特徴は、技術標準運用の通常形式である。ISO/IEC Directives は systematic review、確認・改訂・廃止、コメントの次回改訂への繰越を制度化している。Future Studies も non-evaluation declaration も、その一変種にすぎない。

**検査:** Case D を先に走らせ、全コードが立つかを見る。立つなら本研究は科学の認識論ではなく標準文書の書式を扱っていることになる。

### Null A — artifact type の差

分野差に見えるものは、文書型の差である。Bulletin 17C は L2、GRADE handbook も L2 だが、FEMA GD 71 と診療ガイドラインは制度上の役割が異なる。

**検査:** L 層を厳密に揃えて比較する。層を揃えると差が消えるなら Null A。

### Null B — 既存語彙による完全再構成

standards lifecycle、V&V、UQ、evidence grading、metrological traceability の既存語彙で全体が説明できる。

**検査:** Case B（metrology）で水文学のコードが完全吸収されるかを見る。吸収されるなら共通語彙は不要。

### Null C — 分析者の物語

`prediction demand ↔ epistemic restraint` は field-native reconstruction に不要である。

**検査:** Step 1 の field-native 記述だけで Part VI-4 の 5 問に答えられるかを見る。答えられるなら Null C。

### Null E — coding artifact

分野間の共通機能は存在せず、似て見えるのは符号化の産物である。

**検査:** Step 3–4 の独立符号化一致率。低いなら Null E。

### Null F（本設計で追加）— governance が説明変数

分野差は認識論の差ではなく、規制権限・法的効力・意思決定の賭け金の差である。

**検査:** 各ケースについて、文書の法的地位（強制／推奨／任意）と賭け金（人命／財産／通商）を独立変数として記録し、コードの分布と対照する。この変数だけで差が説明できるなら Null F。

**Null F は Codex の H4 に対応し、本研究で最も棄却しにくい対抗仮説である。** 三ケースは規制権限が大きく異なる（FEMA は保険料率と建築規制、計量学は通商と法定計量、臨床は診療責任）。差が出た場合、それを分野の認識論に帰属させる根拠はほぼない。

---

# Part VIII — Pilot design

**大規模調査にしない。** 各ケース 3–5 文書、合計 15 文書以内。

## VIII-1. 実行順序と停止条件

| 段階 | 作業 | 停止条件 |
|---|---|---|
| **P0** | Case D（generic baseline）。ISO/IEC Directives Part 1 + 非科学的標準 1 件をスキーマで符号化 | **全 12 コードが立つなら P1 へ進まず、Part X を D に確定** |
| **P1** | Case A の未取得資料を取得（OFR 2017-1064、USACE EM 1110-2-1415）。水文学ノートを Part I で訂正 | 訂正により所見が崩れるなら再設計 |
| **P2** | Case B（metrology）を field-native で復元。L2/L3 のみ | **水文学の全コードが計量学語彙へ吸収されるなら Part X を D 寄りに更新** |
| **P3** | Case C（clinical）を field-native で復元。L2/L3 のみ | — |
| **P4** | 独立符号化（VI-3 の制約を明記して実施） | 一致率が低いなら Null E |
| **P5** | 事前登録 5 問を各ケースの L4 一件に適用 | Group A と B の回答が一致するなら organizational value に確定 |

## VIII-2. P0 の詳細（最優先・最安価）

必要資料は 2 件のみ。所要は短い。**この段階で研究の生死が決まる。**

具体的な問い:

> ISO/IEC Directives Part 1 の systematic review 規定と、任意の非科学的技術標準 1 件に、`NONEVAL`（未評価の明示）、`OPEN`（未解決課題リスト）、`RET-DOWN`（下流からの上流制限）、`DELEG`（他機関への委譲）は現れるか。

**予想:** `VER`、`RET`、`TRIG`、`DEV`、`DOC` は確実に立つ。`NONEVAL` と `OPEN` は立たない可能性がある(標準は通常、未解決課題リストを本文に持たない)。`RET-DOWN` と `DELEG` は不明。

したがって P0 の後に残りうるのは、**12 コード中せいぜい 4 コード**である。それを前提に期待値を設定する。

## VIII-3. やらないこと

- 4 分野以上への同時拡張。
- IPCC の早期投入。
- 実務者インタビュー(効果測定は本パイロットの範囲外)。
- 完成論文の執筆。

---

# Part IX — Kill criteria

Codex の 12 項目を採用し、実行可能な検査に対応づける。**発火が早い順に並べる。**

| # | 条件 | 検査 | 発火段階 |
|---|---|---|---|
| 1 | Case D で全コードが立つ | P0 | **最速** |
| 2 | metrology 語彙で水文学のコードが完全再構成できる | P2 | 早い |
| 3 | field-native 記述だけで事前登録 5 問に答えられる | P5 | 中 |
| 4 | 独立符号化の一致率が低い | P4 | 中 |
| 5 | Group A と Group B の回答が一致する | P5 | 中 |
| 6 | 分野差が法的地位・賭け金で説明できる（Null F） | P2–P3 | 中 |
| 7 | 共通語彙を消しても各分野の診断が変わらない | P5 | 中 |
| 8 | コードの単位・件数が符号化方法で大きく変わる | P4 | 中 |
| 9 | 文書に残ることと実際の検索・利用・判断への影響を区別できない | 全段階 | 恒常 |
| 10 | 効果測定なしに retrieval cost を主張する必要が生じる | 全段階 | 恒常 |
| 11 | positive case が単なる標準不遵守・implementation failure に帰着 | P5 | 遅い |
| 12 | 比較のために推定・規範判断・科学法則を同一軸へ押し込む必要が生じる | 全段階 | 恒常 |

**いずれかが発火した場合の最終成果:**

> comparative review of qualification practices in scientific and technical guidance

これで問題ない。むしろ P0 で 1 が発火するのが最も安価な結末である。

---

# Part X — Current status

## **B. viable comparative review, methodological value unproven**

ただし **D への降格リスクが高い**。判定の内訳を示す。

**B とする理由。**

1. 同一 L 層で揃えた artifact chain の突き合わせは、私の知る限り hydrology / metrology / clinical の三者で行われていない。各分野内の整理(GUM、GRADE、standards lifecycle)は完成しているが、層を揃えた対照はない。
2. 訂正 1・2 から生じた二コード(`RET-DOWN`、`DELEG`)は、単一分野の記述からは出にくく、**比較によってのみ観察可能になった**候補である。これは本研究の唯一の内在的動機である。
3. 事前登録 5 問と Group A/B 比較は、organizational value を超えるか否かを実際に判定できる設計になっている。

**A としない理由。** 効果測定(retrieval、利用、下流判断)が一切ない。実務者を含まない設計では A に到達しない。

**D のリスクが高い理由。** Part VIII-2 の予想どおりなら、P0 の後に残るコードは 12 中 4 程度である。さらに Case B で水文学のコードが計量学語彙へ吸収されれば、残りはほぼ消える。**P0 と P2 の二段階を通過する確率を高く見積もる根拠はない。**

**C(organizational synthesis only)としない理由。** まだ P0 を走らせていないため、C と B の区別がついていない。P0 の結果で C か B か D が確定する。

**E(terminate / redesign)としない理由。** P0 が安価であり、走らせる前に終了する理由がない。

---

# Part XI — What would genuinely change our mind?

## XI-1. 仮説を強める証拠

| # | 証拠 | 強さ | 取得段階 |
|---|---|---|---|
| 1 | Case D で `NONEVAL` と `OPEN` が立たない | 中 | P0 |
| 2 | `RET-DOWN`(下流からの上流制限)が三分野すべてに、異なる形式で存在する | **強** | P2–P3 |
| 3 | `DELEG`(他機関委譲)の扱いが分野間で明確に異なり、その差が法的地位で説明できない | **強** | P2–P3 |
| 4 | Group B が Group A の見落とした退役・非推奨手法への依拠を検出する | **最強** | P5 |
| 5 | 独立符号化の一致率が高く、不一致が分野固有項目に集中する | 中 | P4 |
| 6 | L3 層(運用ガイダンス)における不確かさの伝播記述が、分野間で構造的に異なる | 中 | P2–P3 |

**証拠 4 が唯一、organizational value を超える。** 他はすべて「整理がうまくいった」の範囲に留まりうる。

## XI-2. 仮説を弱める証拠

| # | 証拠 | 強さ | 取得段階 |
|---|---|---|---|
| 1 | Case D の非科学的標準に `NONEVAL` と `OPEN` が現れる | **致命的** | P0 |
| 2 | 水文学の全コードが VIM/GUM/JCGM 106 の語彙へ写像できる | **致命的** | P2 |
| 3 | field-native 記述のみで 5 問すべてに答えられる | **致命的** | P5 |
| 4 | Group A と Group B の回答が一致する | **致命的** | P5 |
| 5 | 分野差の分布が、法的地位・賭け金の分布と一致する | 強 | P2–P3 |
| 6 | 独立符号化で件数が 2 倍以上ずれる | 強 | P4 |
| 7 | GRADE の EtD が本研究の 12 コードをすでに包含している | 強 | P3 |

## XI-3. 現時点で予想される最尤の結末

正直に書く。**弱める証拠 1・2 のいずれかが発火する確率が、強める証拠 4 が得られる確率より高いと見積もる。**

根拠は三つ。第一に、標準文書の書式は業界横断で相互模倣されており、Future Studies 型のリストは学協会標準に広く見られる可能性がある。第二に、計量学は不確かさ・適用条件・判定規則の分離を目的として語彙を構築した分野であり、後発の分類が吸収されやすい。第三に、水文学ノートの初版で私が「固有」と見た二つの特徴(non-evaluation declaration、future-work 継承)は、いずれも比較基準線なしの判断だった。

したがって本設計の最も現実的な貢献は、**「共通語彙は不要である」ことを安価に確定させること**である可能性が高い。それは失敗ではない。Part IX の kill criteria はそのために設計されている。

---

## 本設計が確立するもの

- 水文学ノートの事実誤り二件と内部矛盾一件の特定と訂正案(Part I)。
- 訂正から派生した二つの新規観察コード(`RET-DOWN`、`DELEG`)。
- 同一 artifact 層でのみ比較する規律(Part IV)。
- Null D をケースとして先行実行する設計(Part III-2、VIII-2)。
- 効果測定を伴わない主張の禁止と、単一分析者時の成果上限の固定(Part VI-3)。

## 本設計が確立しないもの

- 分野間に共通機能が存在すること。
- 水文学に固有の形式が存在すること。
- 文書構造が検索・利用・判断を改善すること。
- `prediction demand ↔ epistemic restraint` が有用な構造であること。

## 次の作業

**P0 のみ。** ISO/IEC Directives Part 1 と非科学的技術標準 1 件を V-1/V-2 スキーマで符号化する。全コードが立つなら Part X を D に確定し、比較研究は comparative review へ降格して終了する。立たないコードがあれば、その範囲に限定して P1 へ進む。

P0 の前に、Part I の訂正を水文学ノート v0.2 として適用する。**事実誤りを含む前提資料の上に比較研究を積まない。**

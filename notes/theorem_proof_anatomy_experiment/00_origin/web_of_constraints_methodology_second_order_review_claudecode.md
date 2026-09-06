# Second-Order Adversarial Review (Claude Code) — Web of Constraints methodology proposal

## Codex の adversarial review そのものに対する監査

- **Review status:** second-order adversarial review / concept rescue not attempted
- **Reviewer:** Claude Code (Fable 5)
- **Date:** 2026-08-17
- **Primary target:** [`web_of_constraints_methodology_adversarial_review.md`](./web_of_constraints_methodology_adversarial_review.md) に記録された Codex の adversarial review
- **Secondary target:** 同記録に含まれる元構想（仮題 *From Successful Theories to a Web of Constraints*）
- **Related:** [`deferred_resolution_case_01_gst_adversarial_review_claudecode.md`](./deferred_resolution_case_01_gst_adversarial_review_claudecode.md), [`scientific_identifiability_case_01_quantum.md`](./scientific_identifiability_case_01_quantum.md), [`tool_truth_absence_working_note_v0.3.md`](./tool_truth_absence_working_note_v0.3.md)
- **Review rule:** 新規性の救済を目的にしない。ただし「各部品が既存である」と「横断的構成も既存 framework で吸収される」を同一の主張として扱わない
- **Relation to VED:** independent; VED への証拠的支持は一切主張しない
- **Independent verification performed:** 先行研究側の実地確認 4 件（うち 3 件は論文にとって不利な発見）

---

## 0. 要旨

検証の結果、**Codex の還元判断は結論として正しく、論証として不十分**であった。Codex が挙げていない先行研究が四件見つかり、うち三件は論文にとって不利に働く。特に boundary objects / trading zones（概念層）と ASME V&V 40 の context of use（制度層）は、Codex が「まだ横断配置は残るかもしれない」と留保した領域を、すでに占有している。

一方で Codex には二つの過剰・一つの見落としがある。SACM/SEPIO/PROV による吸収論証は**表現スキーマと方法の混同**であり形式として誤っている（ただし結論はほぼ変わらない）。実証ハードルは **B（方法論論文）と C（実証済み手法）を混同**している。そして二つの negative calibration が**いずれも単一分野内の検査**であり、framework の主張対象（分野間連鎖）を検査していないという仕様不一致を見落としている。

最終的に残るのは二つだけである。六つの transport license の対照表（review 相当、実証不要）と、分野間境界での license 欠落仮説（検証可能な経験的仮説）。

---

## 1. Codex review の監査

| # | Codex の批判 | 判定 | 理由 |
|---|---|---|---|
| 1 | 主要部品に強い先行形がある | **correct but incomplete** | 挙げた 16 領域はすべて妥当。ただし最も痛い四件を落としている（§3）。落とした四件はいずれも還元を**強める**方向であり、Codex は自分の結論を過小に論証している |
| 2 | `web of constraints` は比喩に留まる | **correct** | typed edge を導入しなければ argument/evidence/provenance graph の再記述。導入すれば SACM に接近する。この二択の指摘は正確 |
| 3 | claim transport を単一 relation にするな | **correct、かつ本レビュー中で最も建設的** | ただし Codex は「型を分ければ索引になる」で止めた。型分けの非自明な帰結（§3-f）を追っていない |
| 4 | observability map が異種軸を混ぜる | **correct** | Kalman observability（モデル相対）と統計的 identifiability（確率法則の単射性）を一つの順序尺度に載せる根拠がないという指摘は正しい。D1–D4 の降格は妥当 |
| 5 | 各分野が自由に map 形式を選べると反証不能 | **correct — 単独で最強の批判** | ただし Codex は解決策を「固定項目を増やす」方向でしか示していない。反証可能性は項目数ではなく**事前予測の要求**で回復する（§6） |
| 6 | negative calibration は反証側にある | **mostly correct but incomplete** | 「framework の限界を示すが有用性は示さない」は正しい。しかし二件とも**単一分野内**の検査であり、framework の主張対象（分野間連鎖）を検査していない。この仕様不一致を Codex は指摘していない（§3-f） |
| 7 | "cross-domain transport requires additional work" は自明に近い | **correct** | 何が追加されるかを型別に特定できなければ一般論。この点は維持されるべき |
| 8 | SACM + SEPIO/PROV + field modules で大部分を再現できる | **overstated（推論として）、結論としては概ね正しい** | §3-g で詳述。これらは**表現スキーマ**であって方法ではない。「符号化可能」は「同等以上に遂行できる」を含意しない。ただし提案側も大部分がスキーマであるため、結論はほぼ変わらない。**変わるのは残余の同定**であり、Codex の残余（Erasure Test）は誤りで、正しい残余は別にある |
| 9 | 実証ハードル（盲検比較、precision/recall、inter-rater agreement） | **overstated — B と C の混同** | §9 で詳述。PRISMA・CONSORT・TRIPOD・GRADE・ASME V&V 40 はいずれも盲検対照比較なしに公刊された。Codex の要求は C（実証済み手法）の基準であり、B（方法論論文）に適用するのは categorical error |
| 10 | materials chain を positive case 候補に | **correct but incomplete** | 良い候補だが、何が positive で何が再発見かの境界を Codex は与えていない。境界を与えないと、この case も第三の negative calibration になるだけ（§8 で設計） |

---

## 2. Prior-art absorption matrix

| 提案要素 | 最強の先行形 | 完全吸収か | 部分吸収か | 残るもの | 必要な証拠 |
|---|---|---|---|---|---|
| claim を分析単位に | Toulmin / micropublications / SEPIO / nanopublications / **ICH E9(R1) estimand framework** | **YES** | — | なし。estimand 枠組みは claim individuation の作業規則まで与えている | — |
| `C\|(E,M,A,U,S,R)` 記法 | SACM（Claim/Context/Assumption/Justification）、PROV | **YES** | — | なし。SACM の方が型が豊富 | — |
| web of constraints | argument graph / assurance case / evidence graph | **YES** | — | なし | — |
| constraint provenance | W3C PROV、Research Objects、metrological traceability | **YES** | — | なし | — |
| observability map | Kalman observability、statistical identifiability、partial identification、applicability domain、measurement capability | **YES**（各軸ごとに） | — | 統合軸としては未存在だが、Codex 指摘のとおり統合する根拠自体が無い | 統合を正当化する理論（現状なし） |
| claim transport（概念） | external validity、transportability、**Cartwright & Hardie 2012**、GRADE indirectness、model transfer | **YES** | — | なし | — |
| claim transport（**型の比較表**） | 各型が個別に形式化済み。**型間比較は未発見** | NO | **YES** | **型ごとの license 要件の対照表**。causal transport は selection diagram、EFT は matching、metrology は traceability + guard band、GRADE は indirectness — 各々完成しているが、同一面上での対照は見当たらない | 系統的 prior-art audit（review として成立） |
| interdisciplinary hub / typed crosswalk | **boundary objects (Star & Griesemer 1989)**、**trading zones (Galison)**、ontology alignment、metadata crosswalk | **YES**（概念として） | — | 概念的新規性ゼロ。boundary object は「各世界で異なる意味を持ちつつ同一性を保つ」という、本構想の hub 要件そのもの | — |
| claim + scope + fitness-for-purpose の標準化 | **ASME V&V 40-2018 の context of use + risk-informed credibility**、FDA DDT qualification | **YES** | — | V&V 40 は「他分野へも適用可能な一般性を持つ」と規格自身が明言しており、分野横断性まで先取りしている | — |
| minimum ledger / checklist | **EQUATOR Network（CONSORT/PRISMA/TRIPOD/PROBAST）**、GRADE EtD、model cards、datasheets | **YES**（形式として） | — | 形式は既存。ただし「transport 型を明示する checklist」は EQUATOR 群にない | 既存 checklist に transport 型欄が無いことの確認 |
| negative calibration / Erasure Test | ablation study、incremental validity、comparative usability testing | **YES**（評価設計として） | — | Codex はここを残余としたが、これは統計・HCI で確立した評価設計であり、残余にならない | — |
| **事前予測付き protocol** | 見当たらない | NO | — | **反証可能性を protocol 自体に埋め込む設計**（§6） | 設計提示 + 1 事例 |
| **分野間境界での license 欠落仮説** | 見当たらない | NO | — | **§3-f。検証可能な経験的仮説** | 1 件の positive case |

**要約:** 13 要素中 10 が完全吸収、1 が正当化不能、**残るのは 2 つだけ** — 型別 license の対照表（review 相当）と、分野間境界での license 欠落仮説（検証可能な研究仮説）。

---

## 3. Codex が見落としている論点

**見落としはある。八件。うち五件は論文に不利、二件は有利、一件は中立。**

### (a) Boundary objects と trading zones — 不利、かつ最も痛い

「意味を平坦化せずに分野横断で協働する」という hub の中心要件は、Star & Griesemer (1989) の boundary object と Galison の trading zone / interactional expertise がまさに定式化した対象である。boundary object の定義的性質は「各共同体の内部では別々の意味を持ちながら、共通の同一性を保つ」であり、これは提案の typed crosswalk が達成しようとしているものと同一である。Codex は Cartwright/Giere/pluralism を挙げたが、この最も直接的な系譜を落とした。**typed crosswalk の概念的新規性はここでゼロになる。**

### (b) ASME V&V 40 の context of use — 不利

claim（モデル出力）+ context of use + リスク段階づけした credibility 要件、という構造がすでに国際規格として存在し、**規格自身が他分野への適用可能性を明言している**。FDA の Drug Development Tool qualification も同型（バイオマーカーを COU 単位で資格認定する）。これは「claim + scope + 追加 license」の制度化された先行形であり、Codex の metrology への言及より近い。

### (c) Cartwright & Hardie 2012 — 不利

Codex は Cartwright を「domain-limited law / pluralism」でのみ引いたが、*Evidence-Based Policy: A Practical Guide to Doing It Better* は claim を別文脈へ運ぶ際に何が追加で必要か（support factors、vertical/horizontal search）を実務手順として書いた一冊であり、本構想の核と正面から重なる。

### (d) EQUATOR / reporting guidelines — 不利（新規性）、有利（公刊経路）

CONSORT・PRISMA・TRIPOD・PROBAST・STARD は、claim の scope と支持条件を分野内で明示させる checklist 群であり、「最小 ledger」の形式的先行形。ただしこれらは**盲検比較なしに Delphi 合意と worked example で公刊された**という事実が、Codex の評価基準への反論材料になる（§9）。

### (e) ISO/IEC Guide 98-4 / JCGM 106 の guard band — 有利、positive case の材料

測定不確かさ下の適合性判定（decision rule、guard band）は計量学が完成させた「不確かさを判定へ運ぶ license」である。この license は、同じ数値が機械学習の閾値判定へ渡るとき**ほぼ適用されない**。ここに、片方の分野が機構を持ち、受け取る分野が適用していない具体的な境界がある。§8 の positive case はここに賭ける。

### (f) negative calibration 二件の仕様不一致 — 有利、ただし限定的

GST も metrology も**単一分野内**の検査である。framework の主張対象は分野間連鎖であり、分野内は各分野が native 機構を最も強く持つ領域、すなわち framework が最も負けやすい場所である。したがって二件は「分野内では価値なし」という**上限を確定**したのであって、主張対象を検査していない。

ただし過剰救済しないため即座に制約する。分野間境界も部分的に制度化されている（モデル→意思決定は ASME V&V 40、測定→適合判定は ILAC/JCGM 106、モデル→臨床使用は TRIPOD/PROBAST）。したがって「境界には所有者がいない」という前提自体が一般には成り立たず、**所有者不在の境界を特定できたときにのみ**この方向は生きる。

### (g) スキーマと方法の区別 — 中立、ただし Codex の推論を訂正する

SACM・SEPIO・PROV は表現形式であって、(i) transport 操作の類型、(ii) 型ごとに要求される license、(iii) 意味保存の判定基準、のいずれも供給しない。「SACM に符号化できる」は「同等以上に遂行できる」を含意しない — XML に符号化できることが方法論的吸収でないのと同じである。したがって Codex の吸収論証は形式として誤っている。

**ただし結論はほぼ変わらない。** 提案側も大部分がスキーマだからである。変わるのは残余の同定で、Codex が残余とした Erasure Test は既存の ablation / incremental validity 設計に吸収され、残余にならない。

### (h) B と C の証拠基準の混同 — 有利

§9 で扱う。

---

## 4. Strongest surviving central claim（三段階）

### Level 0 — 現時点で安全に言えるもの

> Scientific claims are reused across contexts under domain-specific qualifications — evidential support, model class, uncertainty, equivalence, calibration, and validated scope. Several communities have independently formalized the license required for a *particular* kind of reuse: causal transportability for population transfer, EFT matching for scale transfer, metrological traceability and decision rules for measurement-to-conformity transfer, GRADE indirectness for evidence-to-recommendation transfer, applicability domains for model-to-prediction transfer, and context-of-use qualification for model-to-decision transfer. **These licenses have not been placed on a common comparison surface, and their differences are consequential.**

これは review としてそのまま成立し、実証を必要としない。

### Level 1 — 論文内の case study で示せれば言えるもの

> In at least one cross-field chain, a claim is transported across a boundary by an operation whose license is formalized in the source field but not applied in the target field, and a claim-level reconstruction identifies this gap where independent field-native review of the same corpus does not.

要件は「二名以上の独立分析者による再構成一致」+「分野専門家による field-native control」+「**事前登録した予測**」。

### Level 2 — controlled validation まで成功して初めて言えるもの

> Across independent cross-field chains, claim-level transport reconstruction identifies unlicensed transports at a higher rate than field-native review at comparable false-positive rate, and at least one identification changes a measurement requirement, validation target, or scope statement.

**Level 2 に到達しても、これは「新しい観測可能性理論」ではなく「境界審査の手順」である。** 元の central claim（`allowing observability, applicability, and cross-domain transport to be mapped and audited`）は、Level 2 でも `observability` の部分が支持されない。

---

## 5. Framework / protocol / review のどれとして出すべきか

**単一ラベルを選ぶなら:comparative protocol（cross-domain claim-transport audit protocol）。ただし条件付き。**

- 論文が **inter-field の positive case を一件も含まないなら → review/synthesis** へ降格すべきである。二つの negative calibration だけを持つ protocol paper は、自分の手順が機能した例を一つも持たない protocol であり、査読で通らない。
- `framework` と `methodological scaffold` は却下。framework は SACM / ASME V&V 40 と正面衝突し、incremental difference を示せない。
- `position paper` も却下。position を取るには、既存 license 群の対照という実務的中身がもったいない。

**理由:** 残余二つ（型別 license 対照表、境界での license 欠落仮説）のうち、前者は review、後者は protocol でしか検証できない。両方を一本に載せる最小のラベルが comparative protocol である。

---

## 6. Minimum invariant core

反証不能化を防ぐ鍵は**項目数ではなく事前予測の要求**である。Codex は固定項目を増やす方向でしか答えていないが、項目を増やしても分析者が事後的に埋められる限り反証不能性は残る。

### 6.1 全分野で固定する 8 スロット

| # | スロット | 固定する理由 | 記入規則 |
|---|---|---|---|
| 1 | **Claim identity** | これが崩れると全体が崩れる（§12 の最大脅威） | ICH E9(R1) estimand 方式で 5 属性を必須化：命題 / 測定量・推定量 / 対象母集団または系 / 条件 / 意思決定用途。**うち一つでも異なれば別 claim であり、その差分が transport である** |
| 2 | **Source context** | scope の起点 | 実際に検証された範囲のみ。「一般に成り立つ」は記入不可 |
| 3 | **Support type** | 支持の異種性を潰さない | data / measurement / model / calibration / theorem / decision rule / convention の 7 択（複数可） |
| 4 | **Uncertainty & equivalence** | 二つは別物なので同一スロット内で別欄 | 不確かさの種類と、同定できない同値類（gauge、identified set、observational equivalence） |
| 5 | **Transport type** | 型の混同を防ぐ中核 | §7 の閉じた型リストから選択。**新型の追加は明示的な拡張手続きを要する** |
| 6 | **Source–target difference** | 何が変わったか | claim identity の 5 属性のどれが変わったかを機械的に照合 |
| 7 | **Added license** | 追加された仮定・証拠・校正・橋渡し原理 | 「なし」と記入した場合、それ自体が監査対象 |
| 8 | **Target check status** | 結論 | verified / conditional / unsupported / **unknown-unassessed** の 4 値。第 4 値を一級市民として必須化する |

### 6.2 反証可能性を回復する三つの手続き要件

固定スロットより重要なのはこちらである。

1. **事前予測の登録** — 再構成に着手する前に、「field-native review が見落とすと予測する境界」を書き、封をする。事後に見つけたものを成果と数えない。
2. **field-native control の必須化** — 同一資料に対する分野専門家の独立レビューを常に併走させる。control を持たない適用は事例と数えない。
3. **失敗条件の事前宣言** — 「この case で control が同等以上なら negative と記録する」を protocol 本文に書く。GST・metrology の二件はこの形式で記録されており、この点は既に正しく運用されている。

**この三点があれば、各分野が map 形式を自由に選んでも framework は case ごとに反証可能になる。** Codex の最強批判への回答はここにある。

---

## 7. Generic 化してはいけない部分

| 対象 | 理由 |
|---|---|
| **`observable` `identifiable` `valid` `uncertain` `scope` の定義** | 分野ごとに数学的対象も実験的対象も異なる。共通定義を置いた瞬間に boundary object としての機能を失う。保持するのは定義ではなく**対応表の行**（原語・分野内定義・典拠・数学的対象・実験的対象・翻訳で失われるもの） |
| **判定基準と閾値** | 何をもって identifiable とするか、どの不確かさを無視可能とするかは分野の合意事項。generic 側は基準を持たず、基準が**明示されているか**だけを問う |
| **map の形状** | category / continuous / partial order / 多軸は分野が決める。generic 側が固定してよいのは「不明」を表示できることのみ |
| **transport license の中身** | selection diagram、matching、guard band、indirectness の実質はすべて分野固有。generic 側は「どの型か」「license が明示されたか」までしか言わない |
| **claim の重要性判断** | どの claim が中心的かは分野の価値判断。generic 側が代行してはならない |
| **専門家判断の最終権限** | adjudication は常に分野側にある。protocol は候補を出すだけで判定しない |

一行で言えば：**generic 側は述語を持たず、述語の有無だけを問う。**

---

## 8. Positive-case design（materials chain）

Codex の chain を採るが、**何が positive で何が再発見かの線を事前に引く**。

### 8.1 対象境界（一箇所に絞る）

```text
calibrated characterization  →  property database  →  ML model  →  screening decision
   [measurement uncertainty      [label becomes        [prediction     [threshold applied
    + traceability + CMC]         a point value]        interval?]      without guard band?]
```

四段すべてではなく、**「測定不確かさ → 判定閾値」の一本**に絞る。理由：計量学側に完成した license（JCGM 106 の decision rule と guard band）が存在し、受け取り側での適用有無が客観的に確認できるためである。

### 8.2 事前登録する予測

> 対象コーパスにおいて、特性評価段階で報告された測定不確かさは、データベース収載時に点推定へ縮約され、ML 予測区間にも意思決定閾値にも伝播していない。すなわち、計量学が形式化した decision-rule license が境界で失われている。**field-native review（材料インフォマティクス側）はこれを model の予測精度問題として扱い、測定不確かさの伝播欠落としては指摘しない。**

これは**現時点では仮説である**。実際に確認するまで成果として扱ってはならない。

### 8.3 field-native control

| Group | 構成 | 資料 |
|---|---|---|
| **A（control 1）** | 材料インフォマティクス研究者 2 名の通常レビュー | 同一コーパス |
| **B（control 2）** | 計量学者 2 名の通常レビュー | 同一コーパス |
| **C（framework）** | protocol を用いた分析者 2 名 | 同一コーパス |
| **Adjudication** | 両分野の第三者専門家、群の出所を伏せる | C の出力を A/B の出力と混ぜて提示 |

**control を A だけにしないことが決定的である。** 計量学者単独レビューが同じ指摘をするなら、framework の寄与は「計量学者を呼ぶこと」であり、これは negative である。

### 8.4 判定表

| 結果 | 判定 |
|---|---|
| C だけが license 欠落を指摘し、adjudicator が妥当と認め、**測定要求・検証対象・scope 記述のいずれかが変わる** | **positive** |
| C が指摘するが B（計量学者）も同等に指摘する | **negative** — 寄与は分野横断配置ではなく人員配置 |
| C が指摘するが、どの決定も変わらない | **weak positive**（可視化のみ）。方法論的価値の主張には不足 |
| C が指摘した項目の多くを adjudicator が却下する | **negative + false-positive 問題** |
| C が DFT 対実験のギャップ等、既に広く議論されている問題を再発見しただけ | **negative** — 第三の negative calibration として記録 |

### 8.5 より良い case はあるか

**ある。** 二番目の候補として、生態学・疫学の種分布モデル → 政策判断、あるいは気候モデル出力 → 適応計画が挙がる。境界の所有者が明確に不在で、transport 型が複数（外挿・因果 transport・decision transport）重なるためである。ただし materials chain の方が測定量が定量的で、license の有無が二値で判定できる分、**第一 case としては materials が優る**。

---

## 9. Methodological value — 証拠基準の三分割

Codex の実証ハードルは高すぎる。区別すべき三段階を分ける。

| 段階 | 必要な証拠 | 先例 |
|---|---|---|
| **A. conceptual framework paper** | 明示された動機、先行研究の系統的位置づけ、worked example 1 件 | 大半の哲学・方法論提案 |
| **B. methodology paper** | 文書化された protocol、独立分析者 2 名以上による再構成、失敗条件の事前宣言、negative 結果の報告、worked example 2 件以上 | **PRISMA・CONSORT・TRIPOD・GRADE・ASME V&V 40 はいずれもこの水準で公刊された。盲検対照比較は行われていない** |
| **C. empirically validated method** | 盲検 field-native control との比較、precision/recall、false-positive 率、inter-rater agreement、実際の設計変更 | GRADE の後続検証研究群、reporting guideline の adherence 研究 |

**Codex が提示した基準は C のものであり、B に適用するのは categorical error である。**

ただし B の水準で公刊された先行例には、本構想が現時点で持たないものが一つある — **共有された問題を持つ実務者共同体と、そこでの合意手続き（Delphi 等）** である。PRISMA も GRADE も、すでに困っている人々が存在する場所に投入された。本構想にはまだその共同体が特定されていない。したがって B を狙うなら、**誰がこの手順を必要としているのかを論文内で特定する**ことが、方法論的価値の主張と同等に重要である。

---

## 10. Publication path

| 案 | 利点 | 欠点 | 作業量 | 査読上の弱点 |
|---|---|---|---|---|
| **A. conceptual/reconstruction paper を先に** | 早い。優先権を確保 | **positive case ゼロで方法を提案する形になり、二件の negative だけを持つ**。V&V 40・SACM・boundary object との差分を問われて答えられない | 小 | 「既存の組合せで足りるのでは」に反論材料が無い。**却下推奨** |
| **B. positive case まで含めて一本** | 主張と証拠が一致。protocol paper として最も強い | case が negative なら一本が消える（ただしその場合も C へ転用可） | 大 | positive が一件では一般化を問われる。ただし PRISMA も TRIPOD も worked example から始まった。許容範囲 |
| **C. review/synthesis を先、validation は別論文** | 最も安全。Level 0 は今日書ける。型別 license 対照表は独立に価値がある | 「方法論」の主張は次論文まで持ち越し。review は引用されるが方法として定着しない | 中 | 弱点が少ない。ただし review 単独では研究プログラムが始まらない |

**推奨:C → B の順。** 理由は三つ。

1. Level 0（型別 license の対照）は実証を要さず、現時点で最も確実な貢献であり、これを先に確定させれば B の prior-art 節が完成する。
2. B の case が negative でも、C が既に出ていれば損失が限定される。
3. A は二件の negative だけを持って方法を提案する形になり、査読で最も脆い。

---

## 11. Revised outline

Codex 案（13 章）を採らない。**map と framework を主役から降ろし、transport license の対照を主役に据える。** 9 章構成。

```text
1. The problem: claims are reused; licenses are not
   - 分野横断連鎖で claim が運ばれる実例を三つ
   - 「観測可能性の一般理論ではない」を最初に明示
   - negative results を含む評価方針を先に宣言

2. Prior art: six formalized transport licenses
   - causal transportability（母集団間）
   - EFT matching / domain of validity（スケール間）
   - metrological traceability + decision rules（測定→適合判定）
   - GRADE indirectness / EtD（証拠→推奨）
   - applicability domain（モデル→予測）
   - context of use / V&V 40 / DDT qualification（モデル→意思決定）
   ★ この章が論文の主要貢献。Codex 案では §2 に埋もれていた

3. A comparative table of transport types and their licenses
   - 型ごとに：何が変わるか / 何を追加で要求するか / 誰が所有者か / 所有者不在の境界はどこか
   - ★ Level 0 claim はここで完結する

4. Claim individuation and the minimum ledger
   - estimand 5 属性による claim 同一性
   - 8 スロット ledger
   - unknown-unassessed を一級市民として扱う理由

5. Making the protocol falsifiable
   - 事前予測の登録
   - field-native control の必須化（control を二分野置く理由）
   - 失敗条件の事前宣言

6. Two negative calibrations, and what they bound
   - GST / metrology
   - 「分野内では価値なし」という上限の確定
   - 分野間仮説が未検査であることの明示
   ★ 失敗として捨てず、主張の境界確定として位置づける

7. One cross-field case: measurement uncertainty to decision threshold
   - 事前登録した予測
   - A/B/C 群比較と adjudication
   - 結果（positive / weak / negative のいずれでも報告）

8. What must remain field-native
   - boundary object としての crosswalk
   - semantic flattening の失敗様式
   - generic 側は述語を持たない

9. Limitations and kill criteria
   - claim individuation の分析者依存
   - 文書化コスト
   - 既存標準との incremental difference
   - 撤回条件の明示
```

**削除した Codex 案の章:** "From theories to scoped claims"（§3。Level 0 に吸収）、"Provisional domain-specific map"（§7。派生表示へ降格し appendix）、"Interdisciplinary hub"（§10。新 §8 に統合）、"From map to research requirements"（§11。case study 内へ）。**D1–D4 は appendix にも置かない** — 統合軸を正当化できない以上、掲載すること自体が主張になる。

---

## 12. Revised abstract / title

### 12.1 タイトルは維持できない

三つの理由による。

1. `Web of Constraints` は §3-a により概念的先行形が確立しており、比喩として提示すると relabeling 批判を正面から受ける。
2. `Framework` は SACM / ASME V&V 40 と衝突し、incremental difference を示せない。
3. `Observability` は主役から降ろす方針と矛盾し、かつ Codex の軸混在批判が正しい以上、タイトルに残すと最も弱い部分を看板にすることになる。

### 12.2 代替タイトル 3 案

1. **Transport Licenses for Scientific Claims: A Comparative Protocol for Auditing Cross-Field Reuse**
2. **What Travels and What Does Not: Comparing the Licenses Required to Reuse Scientific Claims Across Fields**
3. **Auditing Claim Reuse at Field Boundaries: A Reconstruction Protocol with Two Negative and One Positive Calibration**

第 3 案が内容に最も忠実である（negative を看板に載せる点で誠実、かつ査読者に評価方針が即座に伝わる）。第 1 案が最も引用されやすい。

### 12.3 Abstract draft（第 1 案のタイトルに対応）

> Scientific claims are routinely reused outside the setting that established them: across populations, scales, instruments, model classes, and decision contexts. Several research communities have independently formalized the license such reuse requires — selection diagrams and transport formulas for causal effects, matching and truncation for effective theories, traceability chains and decision rules with guard bands for measurement results, indirectness assessment for evidence-to-recommendation transfer, applicability domains for model predictions, and context-of-use qualification for models informing decisions. These licenses are mature within their fields but have not been compared on a common surface, and they differ in what they require, what they leave unstated, and who is responsible for checking them.
>
> We do three things. First, we place six formalized transport licenses side by side and identify which source–target boundaries have an established owner and which do not. Second, we specify a minimal, field-adaptable ledger for reconstructing a claim together with its source scope, support type, uncertainty and equivalence structure, transport type, added license, and target check status, with an explicit *unknown-unassessed* value; claim identity is fixed using estimand-style attributes so that a change in any attribute is recorded as a transport rather than absorbed silently. Third, and central to the paper's evidential standing, we make the procedure falsifiable case by case: every application registers, before reconstruction, what it predicts field-native review will miss, and runs against independent field-native controls drawn from *both* adjoining fields.
>
> We report two negative calibrations. In quantum gate set tomography and in metrology, claim-level reconstruction added no diagnosis beyond field-native language. We argue these results bound rather than refute the procedure: both are within-field tests, and both fields possess strong native machinery for the transports they routinely perform. We then report one inter-field test at the boundary from calibrated materials characterization to machine-learning screening thresholds, where the metrological decision-rule license is formalized on the source side and, we predicted in advance, not applied on the target side.
>
> We claim no new theory of observability, no new formalism, and no general partition of what is observable. The generic layer carries no domain predicates; it records only whether a field's own predicates were stated. Whether the procedure constitutes a methodological contribution rather than an indexing convenience is decided by the controlled comparison reported here and by replication, and we state in advance the results that would retire the claim.

---

## 13. Final verdict

### Is the paper idea alive?

**部分的に。framework としては死んでいる。**

- `web of constraints` は boundary object と assurance case に完全に吸収される。
- `observability map` は統合軸を正当化できず、D1–D4 は撤去すべきである。
- `claim + qualifications` の記法は SACM と ASME V&V 40 の context of use に完全に吸収される。
- `interdisciplinary hub` は trading zone / boundary object の再命名である。

### If yes, in what reduced form?

二つだけ残る。

1. **六つの transport license の対照表**（review 相当、実証不要、今日書ける）。
2. **分野間境界での license 欠落仮説**（検証可能な経験的仮説、protocol が必要）。

### What is genuinely worth testing?

> ある分野が形式化した transport license が、隣接分野との境界で適用されずに失われる事例が存在し、それを claim 単位の再構成が、隣接**両**分野の native review が見落とす形で検出できるか。

この仮説は真偽が定まり、事前予測で運用でき、materials chain で一回の試験にかけられる。

### What is probably already known?

提案の 13 要素中 10。claim 単位化、scope 記述、provenance、証拠グラフ、意味を平坦化しない横断配置、型ごとの transport 形式化、checklist 形式、消去試験による評価設計 — すべて既存である。**「部品が既存」だけでなく「横断配置の発想自体」も、boundary object と trading zone が 1989 年と 1997 年に占有している。** ここは救済しない。

### What is the single biggest threat?

**claim individuation の分析者依存。** 先行研究の厚さではない。先行研究は引用で回避できるが、二人の分析者が同じ資料から異なる claim 分割を作れば、ledger は再現不能になり、protocol paper として成立しない。estimand の 5 属性による固定はこれに対する最善手だが、それでも「どの粒度で命題を切るか」は残る。**この一点が解けなければ、他がすべて解けても方法論にならない。**

### What result would make you abandon the framework claim?

以下のいずれか一つ。

- materials case で計量学者の control 群（B）が同じ license 欠落を指摘する（寄与が人員配置に還元される）。
- 独立分析者二名の claim 分割一致率が低く、decision-relevant edge が再現しない。
- adjudicator が C 群の指摘の過半を却下する（false positive 問題）。
- ASME V&V 40 の context-of-use 手続きを対象境界にそのまま適用して同じ指摘が出る（既存標準で足りる）。
- 指摘が正しくても、測定要求・検証対象・scope 記述のいずれも変わらない。

### What result would justify calling it a methodology?

以下の**全部**。

- 二つ以上の独立した分野間連鎖での positive case。
- 隣接両分野の native control が見落とした license 欠落の検出。
- 専門家 adjudication での妥当性承認。
- false positive 率が control 以下。
- 独立分析者による再構成の一致。
- 少なくとも一件の実際の設計・検証・scope 決定の変更。

---

## 14. 依頼された区別への直接回答

「各部品が既存である」と「横断的構成も既存 framework で吸収される」は確かに別の主張であり、本レビューはこれを分けて検査した。結果は次のとおりである。

**横断的構成そのものは、Codex が挙げた SACM + SEPIO + PROV では吸収されない** — それらはスキーマであって方法ではないからだ。しかし Codex が見落とした boundary object / trading zone（概念層）と ASME V&V 40 の context of use（制度層）によって、**横断的構成の発想も、その標準化された実装も、すでに占有されている。**

すなわち Codex の結論は正しく、論証は不十分だった。残るのは横断的構成の新規性ではなく、**その構成を使って特定の境界に license 欠落があるかを実際に検査するという、一件の経験的仕事**だけである。

---

## 15. Verification log

本レビューで独立に確認した事項。

| 対象 | 方法 | 結果 |
| --- | --- | --- |
| 分野横断の「typed claim transport framework」が既存かどうか | Web 検索 | **単一の統合 framework は確認できず。** ただし causal transportability / external validity 側は完全に形式化済み。Codex の判断と一致 |
| ASME V&V 40 の内容と適用範囲 | Web 検索・規格解説の確認 | **確認。** risk-informed credibility、context of use (COU) が中核。V&V 40 小委員会自身が「他分野へ適用可能な一般性を持つ」としている。**Codex の見落とし** |
| boundary objects / trading zones | Web 検索 | **確認。** Star & Griesemer 1989、Galison。「異なる認識文化間で意味を共有せずに協働する」概念として STS で確立。**Codex の見落とし、最も痛い** |
| 2026 年の近接研究（"evidence-licensed claims"） | arXiv:2606.31273 を直接取得 | **残余を殺さない。** Hongmin Li, "The Calibration Turn in AI-Assisted Research"（2026-06-30）は AI 支援研究に限定されており、分野横断の claim transport を扱わない。ただし "no claim without license" の発想が同時期に出ていることは記録に値する |

### Sources

- [Transportability / external validity (Pearl & Bareinboim)](https://arxiv.org/abs/1503.01603)
- [ASME V&V 40-2018 overview](https://link.springer.com/chapter/10.1007/978-3-032-09180-2_5)
- [ASME V&V 40 standard page](https://www.asme.org/codes-standards/find-codes-standards/assessing-credibility-of-computational-modeling-through-verification-and-validation-application-to-medical-devices)
- [Trading zones and boundary objects in cross-disciplinary collaboration](https://www.nature.com/articles/s41599-024-03135-w)
- [The Calibration Turn in AI-Assisted Research](https://arxiv.org/pdf/2606.31273)

---

## 16. Review posture

### 本レビューが確信をもって主張するもの

- `web of constraints`、`typed crosswalk`、`observability map` はいずれも概念的新規性を持たない。
- Codex の還元判断は結論として正しい。
- Codex の SACM 吸収論証は形式として誤っている（スキーマと方法の混同）が、結論はほぼ変わらない。
- Codex の実証ハードルは B と C を混同している。
- 二つの negative calibration は単一分野内の検査であり、主張対象を検査していない。
- 元のタイトルは維持できない。

### 本レビューが確信をもたないもの

- materials chain において実際に measurement uncertainty の伝播欠落が起きているか（**仮説であり未確認**。§8.2 の予測は検証前である）。
- 「所有者不在の分野間境界」が実在するか（部分的に制度化されていることは確認したが、網羅的調査はしていない）。
- claim individuation が estimand 5 属性で十分に固定できるか。

### 本レビューが擁護しなかったもの

- 元構想の新規性。
- `web of constraints` という名称。
- framework というラベル。
- Codex の批判のうち、過剰と判断した二点（SACM 吸収論証の形式、実証ハードル）についても、それが元構想を救うとは主張しない。

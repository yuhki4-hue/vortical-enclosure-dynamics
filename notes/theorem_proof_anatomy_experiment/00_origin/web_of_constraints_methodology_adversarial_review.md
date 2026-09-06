# From Successful Theories to a Web of Constraints — Adversarial Review Record

**Status:** prompt-and-response research record  
**Date:** 2026-08-17  
**Relation to VED:** independent; no evidential support for VED is claimed

---

## User prompt

```text
# Context from my IDE setup:

## Active file: vortical-enclosure-dynamics/notes/theorem_proof_anatomy_experiment/00_origin/deferred_resolution_case_01_gst_adversarial_review_claudecode.md

## Open tabs:
- deferred_resolution_case_01_gst_adversarial_review_claudecode.md: vortical-enclosure-dynamics/notes/theorem_proof_anatomy_experiment/00_origin/deferred_resolution_case_01_gst_adversarial_review_claudecode.md
- tool_truth_absence_working_note.md: vortical-enclosure-dynamics/notes/theorem_proof_anatomy_experiment/00_origin/tool_truth_absence_working_note.md

## My request:
新しい方法論論文の構想を検討しています。以下の仮タイトル・central claim・設計方針を前提に、論文として成立する骨格を adversarial に検討してください。

仮タイトル：

From Successful Theories to a Web of Constraints
A Reconstructible Framework for Mapping Observability, Applicability, and Scientific Claim Transport

この論文は、新しい物理理論、新しい観測可能性の形式理論、新しい普遍的方法論そのものを提案するものではありません。

中心的な目的は、既存の科学理論・数学的手法・計算論的手法が作っている局所的な拘束を、「一意な世界像へ収束する理論階層」としてではなく、異なる観測可能性・適用範囲を持つ “web of constraints” として再構成することです。

central claim の暫定形：

We propose a reconstructible framework in which successful scientific theories are represented as a web of scoped constraints, allowing the observability, applicability, and cross-domain transport of individual claims to be mapped and audited without presupposing a single universal partition or method.

重要な設計思想は以下です。

1. 分析単位は「理論」や「対象」ではなく scientific claim とする。

2. 各 claim は、それが成立する観測・実験・モデル・校正・推論・不確かさ・適用範囲などの拘束網の中にあると考える。

概念的には例えば、

C | (E, M, A, U, S, R, ...)

のように考える。

C = scientific claim
E = experimental / observational conditions
M = model class
A = assumptions
U = uncertainty
S = validated scope
R = reference / calibration / traceability structure

ただし、この表記自体を新しいformalismとして売り出すつもりはない。

3. 論文の中核問題は「claim transport」とする。

ある領域で成立した claim が、

C|D_i -> C'|D_j

のように別の領域へ拡張・再利用・存在論化される際に、

- empirical support
- identifiability
- uncertainty
- model adequacy
- equivalence relations
- calibration / traceability
- scope conditions
- interpretive assumptions

などがどこまで保持され、変形され、背景化され、新たに追加されるかを追跡する。

重要なのは「越境を禁止する」ことではなく、

“cross-domain transport requires additional work”

という点である。

4. observability map を作る。

ただし地図そのものや特定の分類体系を論文の主要成果にはしない。

暫定例として、

D1: clearly observable
D2: quasi-observable
D3: observationally undetermined
D4: completely / in-principle unobservable

という区分を検討しているが、D4はoptional limiting categoryとする。

フレームワークはD4なしでも成立する。

さらに、各分野は3領域、5領域、continuous scale、partial orderなど、自分たちのfield-native criteriaに基づいて地図そのものを再構成できる設計にする。

つまり、

generic scaffold
+
field-native constraints
->
domain-specific observability map

という構造を目指す。

5. この論文は「地図を配る」のではなく「地図の描き方を配る」ことを目標にする。

読者が最終的にこちらの四領域分類を捨てても構わない。

むしろ各専門分野が、

- 何を観測可能と呼ぶか
- 何を識別可能とするか
- どのモデル依存性を許容するか
- uncertainty をどう扱うか
- scope をどう定義するか
- observational equivalence をどう扱うか

を自分たちの基準でマップに乗せ直せることを成功条件とする。

6. この observability map は学際横断のハブとして使える可能性がある。

中央に万能理論を置くのではなく、

observability
applicability
claim transport
constraint provenance

の共通作業面だけを置き、各分野の精密なfield-native conceptsを失わずに比較・接続できるようにする。

7. uniquenessについては主題にしない。

この論文は理論統一や一意性探索を否定しない。

区別したいのは、

- uniqueness obtained as a result
- uniqueness imposed as a methodological preference or transport assumption

である。

一意性への志向が、ある領域で成立した道具や結論を観測可能性・適用範囲を越えて運ぶ際の追加仮定を背景化する場合だけを問題にする。

8. 新しい道具そのものは提示しない。

フレームワークの役割は、

map
-> unresolved boundary
-> required capability
-> future tool design

という前段階を作ること。

つまり、新しい実験装置、計算法、理論形式を与えるのではなく、

「どこに新しい能力が必要なのか」
「何を観測可能にしなければならないのか」

を要求仕様として見えやすくする。

9. 既存理論を大量に引用して構成する。

候補には、

- identifiability
- inverse problems
- observational equivalence
- model adequacy / model misspecification
- uncertainty quantification
- statistical decision theory
- metrological traceability
- calibration
- quotient / gauge structures
- effective theories / domain of validity
- causal inference
- experimental design

などがある。

ただし、「既存概念を新しい名前で言い換えただけ」という批判を最重要視する。

10. 過去に行った二つのnegative calibrationがある。

Case 1: quantum tomography / GST
- identifiability
- gauge redundancy
- quotient structure
- model adequacy
などで、field-native languageがすでにかなり精密だった。
一般用語で再記述しても新しい科学的診断はほぼ得られなかった。

Case 2: metrology
- measurement uncertainty
- traceability
- calibration
- validated scope
- conformity assessment
などにより、科学的結論の安全なtransportがすでに高度に制度化されていた。
generic handoff auditは新しい診断をほぼ与えなかった。

この二例は失敗として捨てず、

「field-native reconstructionで十分ならgeneric vocabularyは降格させる」

というErasure Test / calibrationとして利用したい。

重要：
この論文の価値を守るため、以下を絶対に仮定しないでください。

- このframeworkが新規である
- 四領域分類が妥当である
- “web of constraints”が新概念である
- claim transportが新概念である
- 学際ハブとして実際に有効である
- 方法論的価値がすでに証明されている
- VEDその他の独自理論をこの論文の根拠に使える

この論文はVEDから独立させます。

あなたにやってほしいこと：

A. まず、この構想をできるだけfield-nativeな既存概念だけで再構成してください。
新しい用語を全部消しても何が残るか確認してください。

B. この論文のcentral claimを最も弱く、しかし論文として意味が残る形に書き直してください。

C. 「既存理論の再ラベル」「単なる概念地図」「哲学的整理」「review paper以上ではない」という批判を最大限強くしてください。

D. それでも残りうるmethodological contributionがあるなら、
- conceptual novelty
- organizational novelty
- methodological novelty
- practical research-design value
を分けて評価してください。

E. この論文が本当に成立するために最低限必要なdemonstrationを提案してください。
特に、
「field-native reconstructionだけでは得にくいが、このframeworkを使うことで診断・比較・研究設計が変わる」
ことを示すには何が必要か考えてください。

F. observability mapを作るためのconstruction questionsを設計してください。
特定の4分類に依存しないものにしてください。

G. claim transportを監査するための最小ledger / checklistを提案してください。
ただし新formalismを発明する方向には走らないでください。

H. 学際横断ハブとして成立させる場合、どこで用語の意味が崩れるかを検討してください。
物理、統計、計量、材料科学などで “observable”, “identifiable”, “valid”, “uncertain”, “scope” が同じ意味ではない点を重視してください。

I. この構想に近い既存研究領域・論文・哲学的系譜を列挙し、
「どこまで既にやられている可能性が高いか」を厳しく評価してください。
可能なら検索・文献調査を前提に、一次文献を優先してください。

J. 最後に、現時点で妥当と思われる章構成を提案してください。
章構成は以下の思想を反映してください：

- 理論 -> scoped constraints
- constraintsがなぜ無制限transportに抵抗するか
- claim transport
- なぜmapが必要になるか
- mapの描き方
- provisional example map
- field-native reconstruction
- negative calibration
- interdisciplinary hub
- research design
- limitations

出力では「このアイデアを育てる」よりも「どこで壊れるか」を優先してください。

もし既存研究でほぼ同等の枠組みが存在するなら、遠慮なくそう結論してください。

逆に、新規数学や新定理がなくても、
「既知の事実の新しい可視性」
「分野横断で再構成可能な作業面」
「研究設計上の有用性」
だけが残る場合も、その価値を過大評価せずに具体的に評価してください。

最後に以下の形式で総評してください：

1. Theorem-level novelty:
2. Formal novelty:
3. Conceptual novelty:
4. Organizational novelty:
5. Methodological novelty:
6. Cross-disciplinary usefulness:
7. Risk of relabeling:
8. Minimum evidence needed before publication:
9. Strongest surviving central claim:
10. Kill criterion — 何が判明したらこの論文構想を撤回または大幅降格すべきか:
```

---

## Assistant response

# 総合判定

現状の構想は、まだ「新しい方法論論文」としては成立していません。最も正確な位置づけは、

> claim・evidence・provenance・scope・transportに関する既存研究を横断的に再配置し、その再配置に本当に診断力があるかをcontrol comparisonで検査する研究計画

です。

`web of constraints`、claim単位、provenance、scope、transport、field-native reconstructionの各部品には強い先行形があります。特にSACM、Toulmin、micropublications、SEPIO、W3C PROV、因果的transportability、GRADEは、この構想の相当部分をすでに個別に実装・形式化しています。

したがって、現在のcentral claimにある “allowing ... to be mapped and audited” は、まだ実証されていません。GSTとmetrologyのnegative calibrationは、むしろgeneric frameworkがfield-native reconstructionを上回らなかった証拠です。

論文として残り得る核は、

> 一般語彙を提案することではなく、field-native controlとの比較によって、cross-domain claim reconstructionの追加価値を反証可能に評価する手順

です。

タイトルも、現段階では次の方が内容に忠実です。

> **Mapping the Scope and Reuse of Scientific Claims: A Field-Native Reconstruction Protocol with Two Negative Calibrations**

---

## A. 固有語彙を消したcontrol reconstruction

| 提案中の語彙 | 既存のfield-native reconstruction |
|---|---|
| scientific claim | proposition、assertion、estimand、hypothesis、model prediction、conformity statement |
| \(C\mid(E,M,A,U,S,R)\) | claim–data–warrant–qualifier、assurance case、evidence/provenance record、measurement model |
| web of constraints | argument graph、evidence graph、provenance graph、model dependency graph |
| claim transport | generalization、external validity、causal transportability、extrapolation、model transfer、evidence reuse |
| observability map | observability、identifiability、estimability、detectability、applicability domain、measurement capability |
| constraint provenance | evidence provenance、workflow provenance、traceability、derivation history |
| field-native reconstruction | domain ontology、assurance case、structured review、knowledge-graph comparison |
| unresolved boundary | identified set、model inadequacy、out-of-domain case、unvalidated regime、open requirement |
| required capability | experimental-design requirement、measurement capability、identification condition、validation requirement |

これだけで、現在の技術的内容のほぼすべては再構成できます。

特に近いものは以下です。

- Toulminはclaim、data、warrant、backing、qualifier、rebuttalを区別し、推論規準のfield dependenceを扱っています。[The Uses of Argument](https://www.cambridge.org/core/books/abs/uses-of-argument/fields-of-argument-and-modals/EFBE9FE0D5073226831DF4580D3CE3A5)
- OMGのSACMはclaim、argument、evidenceを交換可能な構造として表現する標準です。[SACM 2.3](https://www.omg.org/spec/SACM/About-SACM)
- micropublicationsは、科学的claim、support、challenge、data、method、citation chainをclaim単位で表現します。[Micropublications](https://pmc.ncbi.nlm.nih.gov/articles/PMC4530550/)
- SEPIOはclaim、evidence line、data、method、tool、agentの関係を、domain-independentで拡張可能なcore modelとして扱っています。[SEPIO](https://ohsu.elsevierpure.com/en/publications/sepio-a-semantic-model-for-the-integration-and-analysis-of-scient/)
- W3C PROVはderivation、attribution、activity、version、procedure、provenance-of-provenanceを標準化しています。ただし、それ自体はclaimの科学的妥当性を保証しません。[W3C PROV](https://www.w3.org/TR/prov-overview/)
- ORKGは研究成果を構造化し、異なる論文のproblem、method、result等を比較・可視化します。[ORKG](https://arxiv.org/abs/1901.10816)

Erasure Test後に残るのは、

> claim-level argument/evidence/provenance structuresと、分野固有のscope・transport・identifiability評価を組み合わせる比較手順

です。これは新概念ではなく、既存構造の統合候補です。

---

## B. 最弱だが意味の残るcentral claim

現在の証拠に合う形は次です。

> **We specify a field-adaptable procedure for reconstructing selected scientific claims together with their domain-specific evidential, model, uncertainty, equivalence, and scope qualifications, and for comparing how those qualifications change when the claims are reused in a specified target context. The procedure is not a universal theory of observability or validity, and its methodological value is credited only when controlled case studies show reproducible diagnostic or research-design differences relative to field-native review.**

さらに弱く、現時点ですでに言える形なら：

> **Scientific claims are reused under domain-specific qualifications. A cross-domain reconstruction may improve their visibility, but its value must be tested against field-native controls rather than inferred from the coherence of the resulting map.**

後者は論文のmotivationとしては成立しますが、単独では研究成果として弱いです。

---

## C. 最も強い反論

### 1. 既存理論の再ラベルにすぎない

SACM + SEPIO/micropublications + W3C PROVに、各分野のidentifiability、uncertainty、applicability、transportabilityを接続すれば、提案中の大部分を再構成できます。

「一つの文献が全部扱っていない」ことは、新しいframeworkの証拠ではありません。既存のmodular frameworksを組み合わせれば足りる可能性があります。

### 2. `web of constraints` が比喩に留まる

constraintには少なくとも次が混在します。

- 数学的制約
- モデル仮定
- 実験可能性
- 校正関係
- 統計的不確かさ
- applicability condition
- 因果仮定
- 解釈上のwarrant
- 規制上のdecision rule

これらをすべて同じedgeとして描くと、意味の違いを消します。typed edgeを導入すればSACMやknowledge graphへ近づき、導入しなければ単なる図になります。

### 3. claimの同一性が定義されていない

\[
C\mid D_i\to C'\mid D_j
\]

において、\(C'\)が本当に同じclaimなのかが不明です。

例えば、

- 同じ命題の別条件への適用
- 別母集団への一般化
- 推定対象の変更
- 近似モデルへの翻訳
- 操作的claimから存在論的claimへの拡張

は異なる操作です。これらを一つのtransport relationにまとめると、肝心の推論差が消えます。

### 4. observability mapが異種軸を混ぜる

D1–D4は、

- 観測装置によるaccess
- モデル内identifiability
- finite-data estimability
- 実際の資源制約
- 原理的不可能性
- ontological observability

を一列に並べる危険があります。

制御理論のobservabilityは、出力履歴から状態を再構成できるというモデル相対的性質です。[Kalman](https://maxim.ece.illinois.edu/pubs/Kalman_1960_Raginsky.pdf)  
統計的identifiabilityは、異なるパラメータが異なる確率法則を定めるかという性質です。[Rothenberg 1971](https://pages.stern.nyu.edu/~dbackus/Identification/Rothenberg_id_Econometrica_71.pdf)

両者を「観測しやすさ」の共通尺度へ載せる根拠はありません。

また、すでに別内容の四段階observability分類も提案されています。[A Case for Observability](https://pmc.ncbi.nlm.nih.gov/articles/PMC9458833/) 四分類それ自体に新規性は期待できません。

### 5. frameworkが反証不能になる

「各分野が自由に3領域、5領域、連続尺度、partial orderを採用できる」とすると、柔軟性が高すぎて、どんな結果もframeworkの成功例として回収できます。

少なくとも次を固定しないと、reconstructibleではありません。

- 必須質問
- 必須edge type
- map間の比較規則
- reconstruction agreementの評価
- failure判定
- mapを作らない方がよい条件

### 6. negative calibrationが現状では反証側にある

GSTとmetrologyは、

> generic mapを追加しても診断・判断・設計が変わらなかった

という結果です。

これはframeworkの慎重さを示しますが、frameworkの有用性は示しません。二例を「方法の成功」に数えると循環します。

### 7. “cross-domain transport requires additional work” は自明に近い

何が追加されるかを具体的に識別できなければ、

> 別条件へ適用するには別条件の検討が必要

という一般論に留まります。因果推論ではtransportabilityが必要十分条件やalgorithmとして定式化されています。[Bareinboim & Pearl](https://ojs.aaai.org/index.php/AAAI/article/view/8232) 一般frameworkがそれより粗い場合、比較用index以上の価値はありません。

---

## D. 残り得る貢献の種類

| 種類 | 現時点の評価 | 理由 |
|---|---|---|
| Conceptual novelty | **低い** | claim、scope、provenance、transport、pluralismはいずれも強い先行形がある |
| Organizational novelty | **低〜中の可能性** | 複数分野を同じ作業面で比較する配置には限定的価値がありうる |
| Methodological novelty | **未実証** | controlより診断・判断を改善したケースがない |
| Practical research-design value | **未実証だが試験可能** | mapから新しいmeasurement、experiment、validation requirementが実際に導かれれば成立しうる |
| Philosophical synthesis | **成立可能** | semantic/pragmatic view、underdetermination、pluralism、models-as-mediatorsの再配置としては書ける |
| Review-paper value | **比較的高い** | 分散した文献の関係を慎重に整理するreviewなら成立可能 |
| Frameworkとしての独自性 | **現状では支持なし** | SACM、SEPIO、PROV、GRADE等とのincremental differenceが示されていない |

GST/metrologyから得られた独自性候補は、内容的概念ではなく、

> generic vocabularyをfield-native controlと比較し、消去後に精度が上がるなら積極的に降格する

という評価規律です。ただし、これもablation、incremental validity、comparative usability testingの一種として先行研究監査が必要です。

---

## E. 論文成立に最低限必要なdemonstration

### 1. “reconstructible” を測定可能にする

独立した複数の分析者が同じ資料からmapを作り、次について一致する必要があります。

- claimの同定
- source scope
- support relation
- uncertainty
- transport operation
- targetで追加された仮定
- unsupported transferの判定

単なる図の外観ではなく、decision-relevant edgeの一致率を測るべきです。

### 2. field-native controlとの盲検比較

同じ資料を使い、

- Group A: field-native reviewのみ
- Group B: proposed framework
- adjudicator:対象分野の専門家

で比較します。

最低評価項目は：

- missed-condition precision / recall
- false-positive rate
- scope judgmentの差
- downstream decisionの差
- literature/evidence retrieval completeness
- 所要時間
- inter-rater agreement
- 新しい実験・測定・validation requirementの生成

### 3. 少なくとも一つのpositive caseが必要

二つのnegative calibrationだけでは方法論的価値を主張できません。

最も診断的な候補は、例えば：

```text
calibrated materials characterization
  → property database
  → machine-learning model
  → candidate screening
  → synthesis experiment
  → engineering decision
```

です。

この連鎖なら、

- metrological uncertainty
- materials characterization
- dataset provenance
- model applicability domain
- out-of-distribution prediction
- experimental validation
- decision threshold

が異なる専門分野へ分散しています。

材料MLではapplicability domain自体が既に研究されています。[materials applicability-domain study](https://www.nature.com/articles/s41467-020-17112-9) したがって、frameworkがそれを再発見するだけなら失敗です。

### 4. 成功閾値

方法論的価値を認める最低条件としては、

- 2つ以上の独立したcross-domain chain
- 少なくとも1つの実際のscopeまたはdesign decision変更
- field-native controlが見落とした問題
- 専門家adjudicationで妥当
- false positiveがcontrol以下
- 独立分析者が再構成可能

が必要です。

一つの「見やすい図」では不十分です。

---

## F. observability mapのconstruction questions

四分類を先に置かず、次の質問からmap形状を決めるべきです。

### Claim specification

1. 何がclaimされているか。命題、estimand、予測、因果効果、モデル、存在論的解釈のどれか。
2. 対象、時間、スケール、母集団、比較対象、単位は何か。
3. claimの否定または競合claimは何か。

### Empirical access

4. 何が実際に記録されるか。
5. 何が記録から推論されるか。
6. 装置、校正、intervention、sampling、preparationは何か。
7. どのprotocolとresourceに相対してaccess可能なのか。

### Identification and inference

8. 候補モデルまたは候補状態は何か。
9. どのequivalence relationまでしか区別できないか。
10. ideal identifiability、finite-sample estimability、inverse stabilityを区別したか。
11. model misspecificationを検査する手段は何か。

### Uncertainty and robustness

12. 不確かさはsampling、measurement、parameter、model discrepancy、approximation、ambiguityのどれか。
13. alternative specificationsでclaimは保持されるか。
14. failureまたはrebuttal条件は何か。

### Applicability

15. validated population、scale、range、environment、material class、taskは何か。
16. boundaryは理論、実験、統計、規制のどれから得られたか。
17. boundary外では「未検証」「不正確」「識別不能」「原理的不可能」のどれか。

### Map construction

18. この分野ではcategory、continuous measure、partial order、複数軸のどれが適切か。
19. map上の順序は本当に単調か。
20. 不明・未監査を独立statusとして残したか。
21. 独立した専門家が同じ配置を再構成できるか。

D1–D4は、この質問への回答後に必要なら作る派生表示に留めるべきです。特にD4には、resource modelまたは不可能性定理級の根拠が必要です。

---

## G. claim transportの最小ledger

新formalismではなく、既存記録を比較するchecklistとして次で十分です。

| 項目 | 最小質問 |
|---|---|
| 1. Source claim | 元のclaim・estimand・claim typeは何か |
| 2. Source scope | population、system、scale、time、task、conditionsは何か |
| 3. Native support | data、measurement、model、calibration、theorem、decision ruleのどれが支えるか |
| 4. Uncertainty / equivalence | uncertainty、identified set、gauge、observational equivalence、limitationsは何か |
| 5. Transport operation | replication、generalization、extrapolation、reparameterization、analogy、causal transport、interpretationのどれか |
| 6. Target claim | targetでclaimの意味・estimand・decision useは変わったか |
| 7. Source–target differences | population、interface、model class、scale、instrument、loss functionの差は何か |
| 8. Additional license | 新しい仮定、evidence、calibration、validation、bridge principleは何か |
| 9. Target check | targetで独立に検査されたか。conditional / supported / unsupported / unknownのどれか |

重要なのは、transportを一種類のedgeにしないことです。

因果効果の母集団間transport、EFT間のmatching、校正結果のtraceability、材料モデルのout-of-domain prediction、操作的成功からontologyへの推論は、別のlicenseを必要とします。

---

## H. 学際ハブで用語が崩れる場所

| 語 | 物理 | 統計・制御 | 計量 | 材料科学 |
|---|---|---|---|---|
| observable | 演算子、gauge-invariant quantity、instrumental outcome等 | 状態が出力履歴から再構成可能 | 通常はmeasurand/resultの語彙を優先 | characterizationで検出・推定される特徴 |
| identifiable | 状態・parameter・modelの区別可能性 | 確率法則のinjectivity、system identification | 主要標準語ではない場合がある | phase/model/property parameterの識別 |
| valid | 理論のregime、近似の正当性 | internal/external/construct/model validity | procedure validation、fit for intended use | protocol validity、model validation、property regime |
| uncertain | experimental/systematic/theory/truncation | sampling、posterior、confidence、model uncertainty | measurement uncertainty | heterogeneity、measurement、simulation、ML epistemic/aleatoric uncertainty |
| scope | energy・length scale・boundary conditions | population、estimand、distribution、task | measurand、range、conditions、CMC | composition、process、structure、representation、property range |

したがって、ハブが保持すべきなのは共通定義ではなく、

- 原語
- field-native definition
- authority/source
- 数学的対象
- 実験的対象
- source task
- target task
- 翻訳で失われる意味

です。

`observable`を全分野共通の最上位nodeにすると、意味崩壊が起きます。ハブは共通ontologyではなく、**typed crosswalk**に限定すべきです。

---

## I. 近い既存研究と吸収範囲

| 先行領域 | 吸収する部分 | 脅威 |
|---|---|---|
| Toulmin argumentation | claim、data、warrant、qualifier、rebuttal、field dependence | central scaffoldの強い先行形 |
| SACM / GSN / CAE | structured claim、argument、evidence、context、assumption | framework構造の最大の重複候補 |
| micropublications / SEPIO / ECO | scientific claim、support/challenge、method、evidence、provenance | claim単位のwebはほぼ既存 |
| W3C PROV / Research Objects | activity、agent、derivation、version、workflow | constraint provenanceの多くを吸収 |
| ORKG / scholarly knowledge graphs | research contributionの比較・可視化 | mapとしての新規性を弱める |
| causal transportability | source/target difference、追加仮定、transport formula | claim transportの一部を厳密に形式化済み |
| GRADE / Evidence-to-Decision | risk of bias、indirectness、imprecision、decision transport | 実務的frameworkとして非常に強い対照 |
| metrological traceability | result、uncertainty、scope、reference chain | safe transportの成熟例 |
| identifiability / inverse problems | 観測からモデル・parameterを区別する条件 | observability mapの局所部分を吸収 |
| partial identification | 強い仮定を避けたidentified set | non-uniquenessの扱いを吸収 |
| sensitivity / specification curve | claimの分析選択依存性 | constraint variationの実装例 |
| EFT / domain of validity | scale別の有効性、matching、truncation | scoped theory像の物理的先行形 |
| OECD applicability domain | endpoint、algorithm、applicability、robustness、predictivity | map-construction questionの実務的先行形。[OECD guidance](https://www.oecd.org/content/dam/oecd/en/publications/reports/2014/09/guidance-document-on-the-validation-of-quantitative-structure-activity-relationship-q-sar-models_g1ghcc68/9789264085442-en.pdf) |
| semantic/pragmatic views of theory | theoryをmodels/practice/applicationとみる | 「理論から局所constraintsへ」の概念的新規性を弱める |
| models as mediators | theory–model–worldの媒介 | 道具・モデルの独立した役割を既に扱う |
| Cartwright / Giere / pluralism | domain-limited law、perspective、model plurality | single hierarchy拒否の哲学的先行形 |
| evidence and gap maps | 既存研究の配置と不足の可視化 | 「地図の描き方」の先行方法論 |

厳しい結論は、

> 個々のnodeだけでなく、主要edgeの多くも既存である

です。

現時点のscoping searchでは「これら全部を同一の科学方法論として統合した単一framework」は確認できませんでした。しかし、単一frameworkが存在しないことは新規性ではありません。SACM/SEPIO/PROVへfield-specific modulesを接続すれば足りるかを、実装レベルで比較する必要があります。

---

## J. 推奨章構成

### 1. Introduction: the problem and the non-claim

- successful theoryではなくscoped claimを対象とする理由
- universal observability theoryではない
- method valueは未実証
- negative resultsを含む評価方針

### 2. Prior-art reconstruction

- Toulmin
- SACM/GSN/CAE
- micropublications/SEPIO/PROV
- transportability/GRADE/metrology
- applicability domains
- semantic/pragmatic philosophy of science

ここをframework提示より先に置くべきです。

### 3. From theories to scoped claims

- theory全体をclaimへ単純分解できない問題
- claim type
- support relations
- field-native terminology first

### 4. Why claims resist unrestricted reuse

- estimand change
- population/scale change
- model-class change
- equivalence relation
- uncertainty
- calibration
- interpretive extension

### 5. A taxonomy of transport operations

- replication
- within-scope reuse
- generalization
- extrapolation
- representation change
- causal transport
- decision transport
- ontological interpretation

### 6. Construction protocol

- construction questions
- typed relations
- unknown/unassessed status
- reconstructibility criteria
- no universal observability partition

### 7. Provisional domain-specific map

- 一分野だけでfield-nativeに作る
- D1–D4はillustrative appendixへ降格
- mapを捨てても分析が残ることを示す

### 8. Negative calibration

- GST Case 01
- Metrology Case 02
- generic vocabularyが診断を改善しなかったこと
- false positives
- Erasure Test

### 9. Controlled cross-domain demonstration

- control vs framework
- same corpus
- blinded adjudication
- reconstruction agreement
- diagnostic/design differences

この章がなければ、論文はmethodology paperではなくposition/review paperです。

### 10. Interdisciplinary hub without semantic flattening

- typed crosswalk
- field-native definitions
- translation loss
- responsibility and authority

### 11. From map to research requirements

- unresolved claim condition
- missing measurement capability
- required experiment
- validation target
- design change

### 12. Limitations and failure conditions

- open-world incompleteness
- claim-individuation problem
- documentation burden
- analyst dependence
- semantic drift
- inability to outperform native review

### 13. Conclusion

- no universal map
- no new theory of observability
- contribution level determined by controlled evidence

---

# 最終総評

1. **Theorem-level novelty:**  
   **なし。** 新しい定理や一般不可能性結果は含まれていません。

2. **Formal novelty:**  
   **現状なし。** \(C\mid(E,M,A,U,S,R)\) は索引記法であり、SACM、SEPIO、PROV等より形式的に弱いです。

3. **Conceptual novelty:**  
   **低い。** claim、scope、provenance、transport、pluralismには強い先行形があります。

4. **Organizational novelty:**  
   **限定的な可能性あり。** field-native conceptsを失わずに複数分野のsource–target関係を一枚に置く配置は、まだ実証されていないものの候補価値があります。

5. **Methodological novelty:**  
   **未実証。** GSTとmetrologyでは追加診断が得られていません。現時点ではmethodological frameworkと呼ぶべきではありません。

6. **Cross-disciplinary usefulness:**  
   **plausible but unproven。** typed crosswalkとしては可能性がありますが、共通語彙によるsemantic flatteningの危険が高いです。

7. **Risk of relabeling:**  
   **非常に高い。** 特にSACM + SEPIO/micropublications + PROV + domain-specific transport/applicability theoryで再構成できる可能性が高いです。

8. **Minimum evidence needed before publication:**  
   systematic prior-art audit、固定protocol、独立再構成可能性、field-native controlとの盲検比較、少なくとも二つのcross-domain chain、少なくとも一つの実際のdiagnosisまたはresearch-design変更、false-positive評価。

9. **Strongest surviving central claim:**  
   > A field-adaptable, claim-centered reconstruction may provide a common indexing surface for comparing how domain-specific support and scope qualifications change across specified source and target uses; its methodological value must be established through reproducible comparison with field-native controls.

10. **Kill criterion — 撤回または大幅降格条件:**  
    次のいずれかが確認された場合、methodology claimを撤回し、review/visualization/pedagogyへ降格すべきです。

    - SACM、SEPIO、PROV、GRADE等の既存組合せで全機能を同等以上に再現できる。
    - 3件以上の比較ケースでfield-native controlと診断・判断・設計結果が変わらない。
    - generic mapのfalse positiveがfield-native review以上になる。
    - 独立分析者がdecision-relevant mapを再構成できない。
    - claim同一性やedge semanticsをfield-native概念なしでは確定できない。
    - mapを消しても研究設計上の判断が一切変わらない。

現時点では、この構想は「既存科学が照らしていない領域を発見したframework」ではありません。成立し得るのは、**既存の照明を意味を壊さず横断配置できるか、その配置が実際の判断を変えるかを、自身も反証対象として検査する論文**です。

# Post-audit implementation 15 — Formal Remediation Specification Plan after impl14

## 1. Status / authority / preservation

```text
Post-audit implementation 15: COMPLETE — FORMAL SPECIFICATION PLANNING ONLY
Verdict: FORMAL REMEDIATION PLAN READY WITH MATERIAL OPEN CHOICES
Formalism adopted / formal specification executed: NONE / NO
Equation / theorem / proof / source / figure editing: NO
Build / distribution: NO / NO
Priority gates A–E: CONDITIONAL retained, not discharged
```

2026-09-21。完成したのは仕様質問、依存関係、移行単位、解除条件の**計画**であり、formal objectsの定義ではない。候補の列挙は採用・推奨順位ではない。author choiceで定理の真偽を選ばず、proofを保存するためにstateやhistoryを都合よく増設しない。

Primary: [impl14](impl14_independent_consistency_audit_author_decisions_v0.1_ja.md) §3–15。Supporting: [impl13](impl13_author_decision_record_d001_d018_v0.1_ja.md) D001–018、[impl12](impl12_formal_remediation_decision_synthesis_v0.1_ja.md) §5–12、[impl11](impl11_proof_theorem_review_v0.1_ja.md) §4–13、[impl10](impl10_formal_equation_review_v0.1_ja.md) §4–14、[impl09](impl09_authority_adoption_decision_review_v0.1_ja.md) §8–13、[Phase07](07_final_audit_and_frozen_dispositions_v1.0_ja.md) §14–17、[README](README_ja.md)。

current sourceの再確認点: P2 `sections/02_inference_operator.tex:11–49`、`03_nonclosure_theorem_ja.tex:28–100`、`05_emergent_stopping_layer_ja.tex:50–104,265–306`。F/Jの旧signature、strict-Jの量化、LRのfeedback、LEのrole/attractor混在、Eのoperator/value混在を計画の入力とした。その他のEQF/FIG locatorはimpl10の63行ledger、Phase07 FIGFINAL14行を参照。全sourceの新たな独立受入監査・証明レビューは実施していない。

保持: Phase07 KEEP23 / REVISE8 / DOWNGRADE21 / SPLIT41 / RETIRE0 / OPEN2 =95 FROZEN。SERIOUS001–005 RETAIN、research OPEN24/24、uncertainties236、blockers13のglobal statusは変更なし。impl08 prose PASS/CLOSED、impl13 decisions18/18 COMPLETE、impl14 PASS WITH MATERIAL ADVISORIESを保持。
Evidence FE2/CE2/SE2/BE3(citation-background-only)/PE1/XE2/PRE2/OE0、correspondence COR3（formal/cognitive/behavioral/biological/social/AI）、phenomenal COR1、cross-domain X3、OP2、maps/data/sims/tested/validated0は不変。

P1 JAはcurrent distributed build authority、P1 ENはparallelでprimary/authorized translation未決。P2 JAはprimary、ENはworking draft。D001の選択は言語優先から導いたものではない。差異を自動翻訳・同期せず、historical HOLDも削除しない。

## 2. Gate A–E specification matrix / release contract

全gateの共通deliverableは、対象identity・入出力・適用域・parameter/time依存・保持する旧読解・非採用読解・必要なproofとresearchを分離した仕様書。**仕様書承認→依存照合→個別edit packet承認**の順を経るまで、下表のrelease conditionは満たされない。

| Gate / repair unit | Exact object to specify | Keep separate | Current survivor | Equation direction | Proof direction | Before editing: minimum release evidence |
|---|---|---|---|---|---|---|
| A / RU-A | generated transitionの入力identityとFの適用単位、履歴/alternativeとのinterface | state/history/rule/realization/possibility | single-state記述の意図、旧S-variantの条件付き読解 | EQF025/026/048のactive/historical切分け、型待ち | local T3.1 candidateのみ | AR001の意味選択、入力の同一性、definedness、反復可能域、realization前後の区別 |
| B / RU-B | 新Jの対象・比較関係・strict条件・admissibility | 区別/拘束/生成履歴/利用可能履歴/圧縮後保持 | 旧real Jとstrict-J kernelは旧scopeで保持 | EQF026/047の再設計待ち、旧量と新量を混ぜない | local order-kernel candidate、転用未認証 | AR002、Aとの合成、同じ評価context、strict性の根拠と適用域を明記 |
| C / RU-C | Eのaction/effect identityとF-iterationの比較対象 | structure/action/value/output/iteration | LE経由作用というD008、非導出/非計算可能は非採用 | EQF033は型待ち、旧type注記候補を即採用しない | typed非同一かnon-theoremか未決 | AR006、A/D interface、比較の意味・量化、必要なら非同一の根拠 |
| D / RU-D | LR/LE'/LEの役割・同一性・保持/帰還・owner条件 | duration/persistence/access/ownership/feedback/hardness | LR再参照role、LE仮説、D017三境界 | EQF031/032/054/055はschema保持と仕様待ち | emergenceはfuture research、存在証明を要求しないconcept laneも可 | AR003/004、6対象の判別表、非自動promotion、owner別帰還経路 |
| E / RU-E | state/parameter/domain/rule/geometry/historyの変更interface | rule塑性とθ可動性、local/global時間 | fixedθ/Aの局所scope、μは一側面 | EQF030/046/052と新rule解釈の非同一を仕様化 | 局所kernelをrule-changing全過程へliftしない | AR005、Aとの整合、rule identity、変更eventと局所前提の寿命 |

Gate D/Eの「仕様検討に入れる」はPARTIAL。未決概念のalternativesとinterfaceまでは検討できるが、完成した新型・promotion・meta-ruleを今採用できる意味ではない。

## 3. Formal object inventory — current / proposed / future / historical

currentは「記載あり」であってsound認証ではない。表の名前はnavigation用で、新しい理論記号・定義・metricではない。

| Object | Current source status | Author-proposed direction | Future specification / historical separation |
|---|---|---|---|
| state / X | P2推論状態、exact identity未完 | generated transitionの担い手 | historyを含むか、同一状態の意味はRU-A |
| F | single-stateとset-valued併記 | generated single-state方向 | active signatureはRU-A、集合値版はhistorical/alternative |
| pre-transition alternatives | EN候補集合 | 実現transitionと別 | 表現自体を採用するか未決、確率を新設しない |
| history | log/trace role | generated historyと再参照 | event履歴/可アクセス表現を分離 |
| update rule | fixed-rule局所議論 | 履歴による変更の可能性 | RU-E、Fと同一視する範囲を明示 |
| admissible domain | strict-Jの許容状態 | noFP scopeを限定 | 独立criterionか条件集合かを表示、経験的適用は別 |
| J | real justification measure | distinction/constraint/history再解釈 | RU-B、新Jへ旧proof未移行 |
| F^k | 反復族表記 | simple iterationとの比較 | 合成閉性・k・path/rule依存未仕様 |
| S / T | binary仮想停止 / P1completion role | surface stopping/residence | 旧fixedpoint表現をconceptual停止と同一視しない |
| LR | traceと再帰参照layer/motion | temporal architectureのhistory側 | LE'境界RU-D |
| LE' | current equationに存在しない | temporary retention候補 | 新typeかregimeか未決、primeをTeXへ挿入しない |
| LE | role/schema、attractor旧語 | quasi-stable保持仮説 | 存在/収束未確立、fixed attractorはhistorical |
| own/given/shared LE | profile境界未解決 | access/生成/所有を分離 | 同じLEの属性なのか別型かも未仕様 |
| E | operatorと作用値が混在 | reference/action effect via LE | RU-C、超越性/非計算可能性はhistorical |
| reference action / stopping effect / output | 停止演算子読解に混在 | 作用と結果を分ける | 型と因果を別管理、作用が必ず停止するとはしない |
| θ / μ | 領域parameter / mobility命名 | rule-plasticityの一側面 | RU-E、μと全rule変更の同一化禁止 |
| error tolerance | 旧許容性と↔sketch | delay/inertiaという別軸 | 独立対象の仕様、↔はhistorical |
| C / Cmax / f | range、PDE template、f例 | generative horizon読解 | 新cost量は未定義、barrier proof非採用 |
| Φ emergence | layer生成schema | 仮説のまま | P1 scalar Φと別、existence operator未指定 |
| Φext / Φnet | 二視点＋保存≡ | asymmetric co-formation | window/network interface未指定、≡historical |
| Ωintel / Ωlife | 保存subset proposal | temporal thickening | literal subsetはhistorical、共通carrier新設なし |
| stopping functional | future/non-adopted | tool-layerのみ | functional/minimum未定、ontologyへ戻さない |
| graph counts / compression | 条件付きcount例 / 新cycle未実装 | 圧縮・再生成・差分再取得 | loss/回復経路はresearch、universal law非採用 |
| hardness/viscosity/fluidity/slack/residence | current formal variablesではない | conceptual factors | unit/order/criterion未定、V/D等新記号なし |
| window diversity / rule-plasticity / mobility range | author conceptual directions | 集団・個体のscope分離 | measure/empirical endpoint/theorem objectへ昇格しない |
| Master v2.1 artifact | exact source NOT LOCATED | provenance-gapのみ | current row検証と歴史継承検証を分離 |

## 4. Gate A — generated transition / F specification plan

### 4.1 Minimum separations

realized transitionは既に生じた前後関係、pre-transition alternativesは起こりえた候補、stateはある記述単位、historyは過去関係/その保持表現、ruleは更新を記述する規則、admissibilityは適用許容性、path dependenceは同じ局所stateでも履歴が結果へ関わる可能性。これらを一つのF引数へ黙って押し込まない。D001は実現後の単値性を採用したのであって、counterfactual全入力のlawを確定していない。

### 4.2 Candidate families — no adoption

| Candidate | Solves / fails to solve | D001 preservation | T3.1 effect | F^k effect | D015 effect |
|---|---|---|---|---|---|
| state-only partial map | 未定義入力を除外可。同一入力から履歴別に別結果となる問題は未解決 | stateの情報範囲と局所単値性が成立する場合のみ | defined/admissible点のkernel候補。partialだけでstrict性は出ない | 各compositionのdefinednessが必要、全k保証なし | rule可変性は別構造が必要 |
| history-indexed map | 履歴contextを区別可。どのhistoryが同じか、生成と保持の区別は別 | 実現contextを明示するなら候補 | context固定のkernelとhistory更新を分離要 | 異なるcontextの合成は固定F反復と異なる | rule変更とhistory入力増加を区別要 |
| path-conditioned map | realized path上のnextを明示可。未実現入力へ一般化不可 | retrospective記述として整合可能 | 同じstate再訪/異なるpathを潰さず、全域noFPへ移さない | path順compositionであり同一operator反復とは限らない | 規則自体の変化を記述したか不明 |
| transition relation + realized path | alternativesと実現を分離可。実現選択の説明は与えない | active Fを候補集合と同一視しないinterfaceが必要 | relationのfixedpointと単値kernelは別、移植不可 | relation合成/realized列/単値反復を分離 | rule-changeをrelation変更にするか別問 |
| stochastic kernel | 分岐の確率的記述が可能。確率law・測度・samplingは新負担 | 実現Fと確率lawを分ける場合のみ | pathwise/期待値/almost-sure strict性は別で旧kernel未転用 | kernelの反復とsample pathを混同不可 | kernel更新自体の仕様が別途必要 |
| selector / resolution operation | alternativeから実現へのinterface候補。選択理由・domainが追加負担 | possibility representationをactive Fにしないなら候補 | 選択結果にstrict条件が成立する根拠が別 | selector変化でfixed iterateではなくなる | rule/selector/input更新の区別を増やす |
| enlarged state containing history | 履歴依存をstate記述へ含めうる。何を保持するか・irreversible記録か未決 | 実現記述と整合しうるがpredeterminationは証明しない | history成分の増加によるnoFPは元の認知state noFPでない | 拡大spaceで閉じるか、元stateへのprojectionは別 | rule成分を保存すれば区別可能、消せばD015を曖昧化 |

これらは排他的7択ではなく、組合せ可能なformal families。組合せも未採用。stochasticity、selector、全履歴記録を「当然の実装」として補わない。

### 4.3 Questions / release evidence

1. 同じxと見なす範囲は、現在利用可能な表現までか、生成履歴までか。理論的identityの選択はAR001。
2. Fは実現済みtransitionだけを記述するか、未実現入力にも適用するlawを今主張したいか。後者でも未来の事前実在を含意するとは限らない。
3. history差・外部入力差・rule差をどこに明示し、どれを現在対象外とするか。
4. Fのdefinedness、codomain、次段admissibility、固定するcontextを仕様で示せるか。single-stepの定理に全反復閉性を過剰要求しない。
5. pre-transition alternativeを別表現する場合、その存在をFのsignatureに混入させずに区別できるか。
6. J入力と反復族へのinterfaceを同じscopeで接続できるか。これは数学者/仕様担当の検査で、authorに合成の真偽を選ばせない。

最低成果物はstate identity、context依存、definedness、realization/alternative分離、反復の対象の仕様。**Fを今編集可能?: NO。**

## 5. Gate B — new J / T3.1 specification plan

### 5.1 Do not identify the five quantities

| Meaning | Must distinguish / compression consequence |
|---|---|
| generated distinction | 新しい差の発生と、後で識別・回収できる差は別 |
| accumulated constraint | 生成された拘束履歴と、現在有効な制約の強さは別。増加≠自由度の単純減少 |
| accumulated generative history | 発生eventの累積と保存された記録量は別。全event保存を仮定しない |
| currently reusable / accessible history | window/access/再参照に依存。erosionやアクセス喪失で減りうる |
| retained history after compression | 表現の縮約と再生成可能性は別。圧縮を「情報が必ず全回復」と読まない |

### 5.2 Candidate representation families — no adoption

| Candidate | Strict increase / kernel consequence | Compression / erosion / D014 | Admissibility requirement |
|---|---|---|---|
| scalar | 比較は簡単だが5概念のaggregation根拠・単位を要す。scalarだけでstrictにはならない | 量が減る処理と累積対象を分離要 | scalar最大化を許容性の実証に使わない |
| vector | 成分trade-offがある。比較関係を選ばず「>」を流用不可 | 各成分の増減を保存できるが重み/順序未指定 | 比較不能点を除く場合、その除外理由とscopeを明示 |
| preorder / partial order | 弱い順序そのものの反射性とstrict部分を区別。strict比較不能もありうる | 縮約・忘却をstrict増加と自動比較しない | 順序とadmissibilityを独立に記載、部分順序を全順序化しない |
| measure on history | 可測対象・additivity等が新負担。「measure」という旧語だけで採用しない | event集合と保存表現で別measureが必要になりうる | 全履歴を同定/観測可能と仮定しない |
| monotone functional | domainとorderを先に要す。非減少だけではnoFP kernel条件に足りない | 圧縮/再生成を含むallowed transitionごとのstrict性が問題 | monotoneな操作だけを選ぶ模型と全認知適用を分離 |
| family of quantities | 5概念の混同を避けうるが同じ量で前後を比べる規則が必要 | 量ごとに保持/侵食を記述可、統合lawは得ない | transitionごとに別量へすり替えてstrict性を確保しない |

### 5.3 Order-theoretic kernel question — specification requirements only

**Can T3.1 survive as a purely order-theoretic kernel without scalar J?: YES, conditional candidate。** impl11 §5.1の局所kernelが使うstrict比較の非反射性を、将来の仕様が維持する場合に限る。ここで新定理を立てたり証明したりしない。

必要最小構造として検査する事項:

- 比較対象に同じidentityを適用でき、Jに相当する評価が当該state/contextでwell-definedであること。
- 前後の評価を同じcarrier・同じcontext・同じ比較関係へ置くこと。
- strict比較が自己比較を許さないこと。scalar実数・metric・連続性・全順序は局所kernelの必須条件とはしない。transitivityは一般のorderとして採用するなら別条件で、単一fixedpoint排除のために無断追加しない。
- 当該許容点でFと評価合成が定義され、必要なstrict stepが明示前提であること。新Jが実際にこの条件を満たす根拠は未供給。
- history/contextが変化する評価を、元stateが同じなのに同じ評価と見なさないこと。拡大history-stateのnoFPは、元stateの停止や再訪の否定ではない。

admissibilityをstrict条件の成立点と定義する模型自体と、その域が実際の認知を含むという独立主張を分ける。後者の実証・生成mechanismを定理へpreloadしない。AR002は何を表したいかを尋ねるのみで、strict性を著者判断として採用しない。

旧kernel: 保持可能な局所結果。新Jへのproof transfer: **NOT TRANSFERRED**。new-J theorem: **NOT FORMALIZED**。J再定義・T3.1書換えは今NO。

## 6. Gate C — E / F iteration type-separation ledger

| Item | Current / intended role | Alternatives to specify, not adopt | Comparison obligation |
|---|---|---|---|
| F | state update / generated transition | fixed local map、context-dependent family、realized trace記述 | RU-Aのinput identityと合成域 |
| F^k | repeated Fという表記 | operator iterate、path composition、output列は互いに別 | k範囲、同じFか、definedness。勝手にoutput族へ読み替えない |
| E | operator旧名 / reference action-effect新方向 | action自体、作用rule、contextから作用を作るfamily、結果value | 何を同一/非同一と比較するのかAR006 |
| LE | 保持structure | substrate/record/role objectの区別未定 | Eの引数・作用先・存在条件を混同しない |
| reference action | referring/placing/using | eventとそれを記述するoperationを分ける | action identity、recipientとscope |
| stopping effect | action後の帰結候補 | residence/output closure等 | E存在から停止成功を定義的に保証しない |
| state | 更新される対象 | 局所stateと拡大history-state | outputと同じ型か未確定 |
| history | generated/retained record | event系列/アクセス可能表現 | LEやactionと同型にしない |
| output | provisional結果 | state/記号/外部記録等 | output等値はoperator等値より弱い |

| Future treatment of E∉{F^k} | Minimum burden | What it cannot establish |
|---|---|---|
| meaningful after typing | Eと反復族が同じ比較可能な対象で、非所属の意味・量化・根拠を明示 | internal nonderivability、noncomputability、絶対外部性 |
| typed non-equivalence statement | 何の同値（作用rule/結果/trace等）か、比較対象、context、反例または論証の負担を定める | relationを新記号に置換するだけで非同値の証明は得ない |
| prose-only semantic distinction | architecture上の役割差に限りformal exclusionを主張しない | 単なるrole名の差から数学的不一致を導かない |
| historical-only notation | 旧式の所在と非採用の理由を保持し、activeな数学命題として引用しない | old sketchが消えた/反証済みという主張 |

最小typed relationに必要なのは**同じ種類の比較対象、identity/equivalenceの意味、適用context、比較範囲**。同じoperatorを比べる案ならdomain/codomainと入力依存、action/outputを比べる案なら対応するiterated action/outputの指定が要る。異なる型だから非所属、という自明な読みでD008の役割差を証明したことにしない。どのrelationを採るか・式を残すかは未選択。A/Dの仕様が先で、停止定理の証明はこの比較の必要条件ではない。

## 7. Gate D — LR / LE' / LE architecture plan

### 7.1 Distinction matrix (two views of the same six objects)

各セルは仕様質問/保持する方向であり、新定義ではない。durationの長短からtype・ownへの昇格を判断しない。numeric thresholdsなし。

| Object | Duration | Persistence | Re-referenceability | First-order feedback | Hardness | Mutability / erosion |
|---|---|---|---|---|---|---|
| LR | 揮発/凍結双方がcurrentにある | uniform要求なし | recursive referenceというcurrent role | current updateへの反映が既に記述される | 専用criterionなし | 記録と参照運動の変更を分離要 |
| LE' | temporary/local方向 | 期間・存続条件未指定 | subsequent LFへのreuse候補 | 可能性のみ、十分なLE判定でない | 未指定 | runtime/contextで変動しうる |
| LE | quasi-stable、permanentではない | 何を保つか未指定 | 個体への参照可能性を要求する方向 | 概念上の必要条件方向 | 独立criterion未定 | erosion/再解釈を許容 |
| own LE | durationだけでは判定不可 | 自主管理/形成との関係未決 | accessだけではownでない | recipient特定が必要 | self-hardeningを自動認定しない | 誰が変更/維持できるか要指定 |
| given LE | 提供元/受け手で異なる | 供給が止まる場合のscope未定 | window/accessに依存 | 使用者ごとに異なる | 外部保持の強さと内発μは別 | 供給者変更と使用者更新を分離 |
| shared/network LE | 集団の保持と個人の保持を別記 | 共有維持の条件未定 | 全員のaccessを仮定しない | network存在だけで各人に成立しない | collective仮説、個体量ではない | resharing/侵食/偏りの経路未定 |

| Object | Origin | Ownership | Accessibility | Promotion | System boundary |
|---|---|---|---|---|---|
| LR | LF trace/外部/凍結ログ | 記録所有と参照主体を分離 | current sourceでも複数経路 | LE'やLEへの自動変換なし | 内部/環境/weights/context |
| LE' | given LEを運用中に生成する仮説 | model/runtime/humanを未統合 | 次回LFへ戻る経路の候補 | new type操作かregime変化か未決 | D017三境界を別々に記述 |
| LE | history/外在化/共有等の仮説 | 個体内またはenvironmental side | first-order availabilityの意味未完 | 複数経路・昇格不要の案も残る | 「どの個体のLEか」が必要 |
| own LE | 自己形成必須かはAR004 | origin/control/maintenanceをどれで判定するか | owned but inaccessibleな場合を区別要 | ownへの変更はdurationで決めない | native/whole-system混同禁止 |
| given LE | 外から供給 | supplierとrecipientを別記 | read/rewrite可能性を分離要 | 取得しただけでownにはしない | externalは相対語 |
| shared/network LE | 複数windowの関与 | collectiveとindividualの意味未定 | heterogeneous accessを許容 | shared→individual LEはrecipient別条件 | aggregationと個体を分離 |

### 7.2 Alternatives and burdens

| Question | Live conceptual/formal alternatives | Burden / unresolved choice |
|---|---|---|
| A: LE' new type or regime? | 独立の中間type / LR保持のtemporary regime / LEの未成熟regime / role記述を重ねる属性方式 | 独立typeならLR/LEと区別する性質、regimeなら同じobjectの何が変わるか、属性なら重なりの許容を示す。AR003、名前だけでは決定不可 |
| B: first-order feedback? | D009では概念上necessary方向。formal predicate化は未済 | sufficientとは採用されていない。判定規則としてはneither necessary nor sufficientが形式証明された状態ではない。両レベルを明示 |
| C: trace vs quasi-stable LE? | 保持される内容・参照条件・更新への役割・erosion下の存続を区別候補にする | 長さのみ/feedbackのみではLRも該当。独立discriminantsが必要。thresholdを今作らない |
| D: accessible external vs own? | 生成起源 / 保持管理 / 改変権限 / 再参照支配、または複合条件 | access≠ownership。AR004でtheoretical ownershipの意味を限定し、具体systemへは別適用 |
| E: promotion? | 別type間の操作 / 同一objectのregime変化 / 複数属性の変化でpromotion操作なし | 最初はoperation/domain/codomain、次はregime criterion、最後は属性関係が必要。どれも未採用 |

最低discriminants: 対象identity（記録/運動/構造）、recipient、system boundary、何の保持か、参照可能な経路、first-orderの意味、origin/control/accessの差、変更/侵食後に何を同じobjectとみなすか。first-orderを「即時」「一tick」「測定済み一段因果」に置換しない。

AR003/004後は、type/regime候補を仕様化してRU-C・Φ・Transformer profileへのinterface照合へ進める。存在/収束/自律性の実証は別research。**現在のformalization readiness: PARTIAL、完成typeの採用・equation migrationはNO。**

## 8. Gate E — state / rule / θ plan

| Change kind | Distinction required |
|---|---|
| state update | 固定rule内の値の変化と、ruleそのものの変更を分離 |
| parameter update | parameter値変更で表現できるfamilyに属するかを確認。全rule変更と同一視しない |
| domain update | admissible inputsの変更、旧domainとのelement同定が必要 |
| rule update | 入力から更新への対応/方策の何を同じruleとするかが先 |
| geometry update | metric/topology等がそもそも採用される場合のみ。domain変更から自動導入しない |
| history update | generated historyと保持/アクセス表現の変更、state/ruleへの作用を分離 |

| Alternative | State/rule distinction | Local T3.1 | μ as one aspect | Meta-regress / second index | D001 effect |
|---|---|---|---|---|---|
| enlarged state | rule成分/投影を保存するなら区別可、単一state名だけでは消える | 拡大state kernelと元state kernelは別 | 成分全てをμにしなければ可 | 固定super-ruleを仮定するなら追加commitment。第二indexは必須でない | history拡大と整合要、実現pathからlawを捏造しない |
| two-level dynamics | object/updateとrule-updateを別役割にできる | 下位rule固定の局面のみ | 上位変更全体との同一化禁止 | 有限二層のscopeで止めるか未決。同期/順序を要すが第二clock強制ではない | 下位Fと実現順を明示要 |
| time-indexed rule family | 時間別ruleの差は記述可、変更理由は与えない | 同じrule/contextの局所条件だけ | θ familyより広いか要明示 | indexを設けただけでmeta-regress解決ではない。単一event順も候補 | 固定F^kとは異なるcompositionを検査 |
| meta-update operator | ruleを対象とする作用を明示する候補 | ruleを変える作用には旧proof未適用 | meta作用=μとしない | meta-ruleも変わるかはscope判断。無限towerは要求しない | meta作用をactiveFへ混入しない |
| θ-only representation | 選択したrule familyがθで表現できる範囲に限る | fixedθ/A sliceのみ | 全rule塑性をθ/μへ還元するとD015方向を狭める | 第二index不要の場合あり、変更則は別 | F(x;θ)の借用continuous版と同じにしない |
| hybrid structure | 複数変更kindを分けられるがinterface負担増 | 局所modeごとの前提寿命を検査 | μを部分作用として区別可能 | mode切替/上位則のscope明示要、第二time必須とはしない | path依存とmode依存を二重計上しない |

最小extensionは特定の形式ではなく、**rule identity、stateとの区分、historyがどちらを変えるか、変更の順序、局所定理前提の有効範囲、旧/新domain間の比較**を記述できるinterface。AR005のtheoretical rule変更の範囲を先に確認する。second-order time index、metaoperator、common geometryを今導入しない。

D015を無拡張fixedθへ当てはめることはNO。仕様探索はPARTIAL、local kernelは保存対象、全rule-changing過程のnoFP/安定性へはliftしない。

## 9. Secondary specification clusters

「now」は当該active formal migrationを開始する前、「wait」はconceptual/future guardのまま保留できる範囲。研究成果を待たないとstatus表示さえ出来ないというgateは作らない。

| Unit / decision | Formal object required now / can wait | Equation impact | Proof impact | Figure impact | Research dependency |
|---|---|---|---|---|---|
| RU-S / D003 residence | foreground/background、保持対象、観察windowをformal停止にする前に必要。continuous評価/閾値はwait | EQF028/044の旧模型と分離、binaryを連続量へ勝手に置換しない | noFPからsurface stopの不存在を導かない。旧局所不両立だけ別保持 | 007/009/012/013の停止語をscope分離 | independent stopping/retention criterion、OPEN保持 |
| RU-H / D005 horizon | 既存C range/f domain/normalizationの整合は必要。新cost量・到達定理はwait | 017–024/059/060、templateをlawへ変えない | 非到達/invariance未証明。dynamical theoremを復活させる計画でない | 006のboundary illustrationと証明済みbarrierを分離 | C観測・costと知性の対応 |
| RU-PHI / D010 co-formation | window、network、個体側reference、相互作用の対象/順序はtyped表示前に必要。強さlawはwait | 034の≡非採用、053のidentity前提を除く設計 | identity証明を修理するのでなくactive proof burdenを非同一方向へ変更する計画 | FIG011 HOLD、関係仕様後に再設計packet | diversity/bias/hardeningの観測、独立同定 |
| RU-MU / D011別軸 | μの変更対象、delay/inertiaの対象/時間とscope必要。尺度/response法則はwait | 037↔はhistorical、052/054の機構schemaを保証にしない | 必要十分の両方向を復活させない | 008/013のphase/profileはtyped/calibratedと見せない | 各軸の独立操作化、general/sapiens識別 |
| RU-LIFE / D012 temporal thickening | literal subsetをactive非採用と表示するだけなら新object不要。formal extensionのcarrier/time層はwait | 036の記号移行設計、embedding新設なし | inclusion証明を新たに要求・実施しない | 005/014はrole比較、common carrier禁止 | life/Int境界、跨scale map |
| RU-COMP / D014 cycle | countsの対象条件は例を保持する前に明示必要。圧縮/再生成のformal modelはwait | 014/015のcount scope、012のp→fieldは別問題 | elementary countと認知帰結を分離 | 004の必然branchingを除く計画 | 失われた差分の再取得経路、window diversity |
| RU-ARCH / D016非1:1 | 概念区分と旧表のstatusのみnow。typed P1→P2 map不要 | 同字F/Φ等を統合しない。既存P1局所宣言保持 | refinement/derivation theoremを立てない | 001のsurface役割、009のtemporal役割を非同一化 | typed bridgeを望む将来のみ研究 |
| RU-PROV / D018 | 現在検証可能node/欠落linkの台帳now。exact artifactはwait | Master rowの数学を来歴選択で置換しない | historical inheritanceとcurrent row validityは別 | 引用注記のみ、理論図への導出矢印なし | documentary探索でありempirical theory route閉鎖ではない |

Additional isolated checks: RU-RATE（EQF038/040、clock・計数単位・差の意味）、RU-GRAPH（014/015のpossible/actual・exact/cumulative区別）、RU-SOC（056/057のsocial schema）、RU-DOC（HOLD/active status、EN/JA文書role）。これらをGate Aの完成まで一律待たせる必要はないが、edit許可を今与えるものではない。

## 10. Dependency ordering — specification DAG, not generative law

### 10.1 Test the proposed chains

| Proposed chain | Audit result / actual prerequisite |
|---|---|
| A → B → T3.1 → stopping → C | Aの入力interfaceはB合成の前提、A/BはT3.1 restatementの前提。ただしJ意味の探索はAと並行可。surface stoppingの概念はT3.1から導かれず、Cの型比較も停止定理を必要としない。CはAとDに直接依存 |
| D → Φ → Transformer figure | ΦnetをLE間構造として具体化する部分はDに依存。Transformer境界仕様はDに依存するがΦ仕様を常に必要としない。DからΦ/Transformerへ分岐、FIG011/009へ別々に進む |
| E → sapiens → μ/error → phase figures | sapiens rule読解はEに依存。μとdelayの別軸方針はsapiens定理を待たず整理可能。μをrule塑性へ接続するinterfaceはE/Dが必要。phase図にはrate尺度/qualitative mode条件も別入力 |

「iterationの合成域」「new Jの意味」「rule identity」は相互に検討するが、その検討feedbackを循環的な証明依存にしない。共有interfaceをR0として先に合意し、local specとglobal integrationを別nodeへ分ける。R0が変更された場合は依存成果を未承認へ戻す計画であり、変更前の証明を使い回さない。

### 10.2 Nodes / repair units

| Node | Deliverable (not yet produced) |
|---|---|
| AUTH | 既存impl13 D001–018 authority（このnodeのみ既にある入力で、新deliverableではない） |
| Q | AR001–006の理論的意味の回答、未回答scopeの明示 |
| R0 | recipient/system boundary、state/history identity、local contextの共有interface contract |
| A | generated-transition Fの局所signature specification |
| B | J対象/比較/strict premise/admissibility specification（local） |
| D | LR/LE'/LE discriminants・ownership/feedback specification |
| E | state/rule/θ変更interface specification |
| T | A/Bに限定されたT3.1 statement/proof obligation案 |
| STOP | foreground/residenceの概念・対象scope specification（noFPに非依存） |
| STOPCHECK | Tの排除する固定点模型とSTOPの非同一の照合 |
| C | E作用とF反復の比較対象・relation specification |
| PHI | window/network/LE interfaceとco-formation表示仕様 |
| TR | Transformer-only/runtime/human-toolのowner別profile仕様 |
| SAP | D015 state/rule区分のprofile適用scope |
| MU | μ塑性とdelayを別軸とするinterface仕様 |
| RATE | rateの比較可能性・qualitative phaseのscope仕様 |
| MODE | 非網羅・非収束のcollapse taxonomy表示仕様 |
| GRAPH | conditional graph-count例の対象仕様 |
| HORIZON | C/f/domain整合とtemplate/future boundaryの区分 |
| ARCH | P1/P2非1:1の表示/Appendix status仕様 |
| PROV | Master欠落linkとcurrent row検証の分離台帳 |
| INTEGRATE | 選択したrepair sliceの型・scope・proof burden相互照合 |
| EQPACK | 承認済み仕様に対応する個別equation migration packet |
| PROOFPACK | 承認済みstatement/前提に対応する個別proof packet |
| FIG009 | architecture図packet、type/owner解除後のみ |
| FIG011 | co-formation図packet、Φ仕様解除後のみ |
| PHASEFIG | 008/013等の新profile/phase図packet |
| ACCEPT | 将来の独立source/formal/presentation consistency acceptance |
| RELEASE | build/bilingual/distribution許可gate |

### 10.3 Edge ledger

複数source欄は**各sourceが必要**というAND依存。すべてplanning requirementであり、実在する理論上の生成矢印ではない。局所単位を選ぶ場合、Q/R0/INTEGRATEはそのunitと直接依存だけを対象にし、無関係なAR全回答やOPEN24全閉鎖を要求しない。既決AUTHから進められる文書整理はQ待ちではない。

| Edge | From | To | Kind / reason |
|---|---|---|---|
| DEP15-001 | Q | R0 | AUTHOR/SCOPE：意味を数学的都合で決めない |
| DEP15-002 | R0 | A | TYPE：state/history/context |
| DEP15-003 | R0 | D | TYPE：recipientと保持対象 |
| DEP15-004 | R0 | E | TYPE：state/rule identity |
| DEP15-005 | A | B | TYPE：評価合成と同じcontext |
| DEP15-006 | A,B | T | TYPE/PREMISE：local strict kernelのみ |
| DEP15-007 | R0 | STOP | SCOPE：foreground/background |
| DEP15-008 | T,STOP,D | STOPCHECK | SCOPE：noFP≠residence、LE naming≠存在 |
| DEP15-009 | A,D | C | TYPE：iterationと作用対象。Tからの導出ではない |
| DEP15-010 | D | PHI | TYPE：LE/networkに言及するinterface部分 |
| DEP15-011 | D,A | TR | TYPE/BOUNDARY：temporary保持とupdate主体 |
| DEP15-012 | E,A | SAP | SCOPE：local Fとrule-changing profile |
| DEP15-013 | E,D | MU | TYPE：塑性の対象とdelay対象、全rule変更への還元禁止 |
| DEP15-014 | R0 | RATE | TYPE：rate対象と時間scope |
| DEP15-015 | R0 | MODE | SCOPE：固定attractorではないmode |
| DEP15-016 | R0 | GRAPH | TYPE：graph/countと認知対象を分離 |
| DEP15-017 | R0 | HORIZON | TYPE/SCOPE：C/fと新costの分離 |
| DEP15-018 | AUTH | ARCH | AUTHOR：D016は既採用、未回答ARをこの文書整理の前提にしない |
| DEP15-019 | AUTH | PROV | DOCUMENTARY：D018方針を使用、exact artifact発見や新AR回答を前提にしない |
| DEP15-020 | T,STOPCHECK,C,PHI,TR,SAP,MU,RATE,MODE,GRAPH,HORIZON,ARCH,PROV | INTEGRATE | REVIEW：global時の全入力。局所sliceでは関連subsetのみ |
| DEP15-021 | INTEGRATE | EQPACK | AUTHORIZATION：型/active-HOLD/差分範囲を承認 |
| DEP15-022 | INTEGRATE | PROOFPACK | PROOF：statementを先に固定。証明から仕様を逆定義しない |
| DEP15-023 | D,TR,SAP,ARCH | FIG009 | TYPE/SCOPE：図に含めるprofileの境界確認 |
| DEP15-024 | PHI | FIG011 | TYPE：co-formation関係仕様 |
| DEP15-025 | MU,SAP,RATE,MODE | PHASEFIG | SCOPE：非測定・非同値・非網羅 |
| DEP15-026 | EQPACK,PROOFPACK,FIG009,FIG011,PHASEFIG | ACCEPT | REVIEW：採用release sliceの実装後。未実装はHOLD表示して範囲を明示 |
| DEP15-027 | ACCEPT,PROV | RELEASE | RELEASE：EN/JA・asset/PDF・歴史/active分離、別build許可 |

R0→A/D/E/STOP/RATE/MODE/GRAPH/HORIZON、A→B→Tを並行laneとして扱う。ARCH/PROVはdocumentary-only作業を先行検討できる。図のsafe relabel/captionのみの既存laneはこの新architecture DAGと別で、FIG009/011を迂回して解禁しない。

Topological check対象は上の29nodes/27 edge rows（複数sourceを展開して57edges）。数値順は重要度ではない。model上のfeedback cycleをこの作業依存DAGへ証明として写し込んでいない。

## 11. Equation-family migration plan

全63familyをscope確認し、影響の小さい宣言・引用例も保全対象として1行ずつ記載。再proof auditではない。Primary migration classは1つ。RETAINは**表記・scopeを保存する計画**であってnew formal modelへの移植認証ではない。変更候補はimplementation仕様待ちで、今edit-readyな式は0。

Status key: RI=RETAIN AS IS / TA=RETAIN WITH TYPE ANNOTATION / SG=RETAIN WITH SCOPE GUARD / RD=REPLACEMENT DESIGN NEEDED / SC=SYMBOL/RELATION CHANGE LIKELY / HO=HISTORICAL ONLY / FS=WAIT FOR FORMAL SPECIFICATION / PR=WAIT FOR PROOF / RS=WAIT FOR RESEARCH。

| EQF | Current object (impl10 §4 locator) | Class | Migration / survivor | Direct prerequisite / repair unit |
|---|---|---|---|---|
| INT-EQF-001 | P1 discrete update | SG | P1 local schemaを保持、P2 active Fと統合しない | ARCH、P1 state/time scope |
| INT-EQF-002 | P1 scalar Φ | RI | map宣言保持、安定化/非還元証明ではない | 追加移行不要、他Φへ移植不可 |
| INT-EQF-003 | Φbio scalar role | RI | 引用対応の宣言保持 | 生物実証/Int mapを同一化しない |
| INT-EQF-004 | Φtr scalar role | RI | 同上、weightsからの算出mapではない | Transformer所有境界とは別 |
| INT-EQF-005 | edge flow Q | SG | biological引用template、physical条件保持 | source-local units/edge scope、認知へ移植しない |
| INT-EQF-006 | adaptation ODE | SG | 引用templateのまま | 離散Fとの同一性なし、解存在の認証なし |
| INT-EQF-007 | absolute-flow power example | RI | 明示μ>0の例を保持 | P2 μと別glyph role |
| INT-EQF-008 | Transformer hidden-state collection | FS | token/layer/state identity確定待ち | A/TR、同じSの自動継承禁止 |
| INT-EQF-009 | layerwise Ftr update | FS | context/weights/shapeと層別署名待ち | 008/TR、実現transitionとの比較 |
| INT-EQF-010 | I increase schema | SG | direction仮説のみ | GRAPH/COMP、単調性定理なし |
| INT-EQF-011 | div J increase | FS | field/graph geometry未指定 | GRAPH、scalar Jと別 |
| INT-EQF-012 | correctness(p)⇒div J | RS | guard付き候補。typingだけで含意は成立しない | p/field/graph mappingと独立含意、OPEN維持 |
| INT-EQF-013 | indexed I increase | SG | qualitative schema保持 | cognitive instability law非採用 |
| INT-EQF-014 | edge ∼ vertex² | FS | conditional countは保持方向、actual/possible/asymptotic対象待ち | GRAPH。必要なら例の表記設計を別承認 |
| INT-EQF-015 | b^d | FS | exact-depth/cumulativeの対象を選ぶ前に修正しない | GRAPH、merge/branch条件明示 |
| INT-EQF-016 | T∈External(R) | FS | P1外部性のscopeとD003residenceを分離 | STOP/C/ARCH、Internalとの補集合を仮定しない |
| INT-EQF-017 | closure PDE | FS | formal templateとして保存、law採用しない | HORIZON、domain/coefficients/ICBC/Δの意味 |
| INT-EQF-018 | range/barrier | PR | 定義的range保持、動的invarianceへは進めない | HORIZON、先に型、その後必要な場合だけproof |
| INT-EQF-019 | I=f(1−C) | FS | scalar合成/normalization整合待ち | HORIZON、020/021/059と連動 |
| INT-EQF-020 | identity f example | RI | 例の関数形自体は保存 | 全closureでの正値性/極限を認証しない |
| INT-EQF-021 | log f example | FS | 旧type-annotation候補は未解除、C=0を黙って除かない | HORIZON、real domainと018/024の整合方針 |
| INT-EQF-022 | closure gradient drive | FS | geometry/type未仕様、Fと同一operatorでない | HORIZON/Aとの役割区分 |
| INT-EQF-023 | closure flux | FS | scalar/tensor係数・domain未確定 | HORIZON、017との合成 |
| INT-EQF-024 | C range map | RI | 宣言自体保持、非到達証明ではない | 017等にgeometryを自動供給しない |
| INT-EQF-025 | single-state F update | FS | active direction保持、実現pathとmap未接続 | RU-A / AR001 |
| INT-EQF-026 | strict-J step | FS | 旧J局所前提を保持、新J式は未設計 | A/B、same-context/order、strict根拠 |
| INT-EQF-027 | noFP / contradiction | FS | 局所kernel保持、admissible量化へのrestatement待ち | A/B/T、old proofを新Jへ移さない |
| INT-EQF-028 | S / fixedpoint stopping | SG | 仮想模型としてのみ保持、strong cor3.2はhistorical | T/STOPCHECK、surface stopping classifierでない |
| INT-EQF-029 | Cij exponential candidate | FS | product dimension/sign、H境界未仕様 | HORIZON/D/PHI、measurementと混同しない |
| INT-EQF-030 | Ωθ / A,B | SG | fixed-region/mobility区別保持、rule塑性全体ではない | RU-E、強い拡張はFS待ち |
| INT-EQF-031 | general emergence Φ schema | SG | hypothesis schema保持、存在operatorでない | D、他branchとのtyped mapはRS |
| INT-EQF-032 | LE=Φ(LR motion,H) | SG | D009がschemaとして保持。新formal objectの定義にしない | D、existence/feedback同定はresearch |
| INT-EQF-033 | E action / non-iterate | FS | action/effectとoperator比較未型付け、TA断定不可 | A/D/C/AR006。semantic-only/historical案も残す |
| INT-EQF-034 | Φext≡Φnet | SC | literal≡非採用、旧式historical。active relationの表示設計待ち | PHI、new式を必ず作る必要はない、FIG011 HOLD |
| INT-EQF-035 | response Hji near zero | FS | response対象/尺度/閾値未仕様 | D/PHI/RATE、nonontology guard保持 |
| INT-EQF-036 | Ωintel⊂Ωlife | SC | literal subset非採用、旧式historical、conceptual extension | LIFE、共通ambient/embeddingを捏造しない |
| INT-EQF-037 | error tolerance↔μ | SC | ↔非採用、別軸への表示設計待ち | MU/E、delay定義・新相関式は未設計 |
| INT-EQF-038 | Δvintel difference | FS | type-annotation候補継続、共通時計だけでは不足 | RATE、計数尺度/換算を勝手に追加しない |
| INT-EQF-039 | Σ development/activity | RS | future quantificationを保持 | estimator/criterion研究、定量化しない |
| INT-EQF-040 | phase-region schema | SG | qualitative / uncalibrated、zero-motion局所定義保持 | RATE/MODE/MU、新phase criterion不要 |
| INT-EQF-041 | stopping functional minimum | SG | future tool-layerのみ。physical比較式を歴史化して消さない | D013、functional仕様はwait、存在証明対象未定 |
| INT-EQF-042 | continuity equation analogy | SG | fluidの比較に留め保持 | cognitive conservationを主張しない |
| INT-EQF-043 | P1 state set | RI | 集合命名保持 | P2/history stateの構築に流用しない |
| INT-EQF-044 | T∉Internal(R) | FS | local停止とinternalのcriterion未指定 | STOP/C、一般認知不可能性へ戻さない |
| INT-EQF-045 | Fbio discrete update | SG | 生物の形式例として保持 | 006ODE/P2Fと同一化不可 |
| INT-EQF-046 | continuous F(x;θ) | SG | 借用continuous template保持 | RU-E、next-state Fとvector field別署名 |
| INT-EQF-047 | J:X→R | FS | 旧scalar J宣言は旧kernel内保存、新Jへ変更未許可 | RU-B/AR002、same glyph衝突を防ぐ |
| INT-EQF-048 | set-valued F | HO | active非採用、historical/alternativeとして保存計画 | D001、A/DOC、source物理削除ではない |
| INT-EQF-049 | C definition / not truth | RI | local definitionと否定guard保持 | 変更不要、保持量≠truth |
| INT-EQF-050 | LF→traces/LR→LE | SG | retained trace/role/emergenceを仮説の別burdenに | D/COMP、nonclosureから生成自動導出なし |
| INT-EQF-051 | difference→noFP→external stop | RD | 条件省略の導出chainを分離する設計が必要 | A/B/T/STOPCHECK、最終表記未選択、newlawなし |
| INT-EQF-052 | H→threshold→μ→sapiens | RD | 定義/変更能力/profile/加速仮説を別表示へ | E/MU/SAP、μuniversal必要性なし |
| INT-EQF-053 | LE→Φnet→external dependence | SG | conceptual role chain、identity/aggregation theoremでない | D/PHI、diagramの新実装はspec待ち |
| INT-EQF-054 | μ→B→E-site→LR→LE | SG | D009schema保持、convergence/自動生成を含意させない | D/E/C、fixed-attractorの旧readingはHOLD |
| INT-EQF-055 | environmental locus→E-site | FS | role assignmentの対象型/owner未指定 | D/C/TR、locusをoperatorにしない |
| INT-EQF-056 | distributed→centralized | SG | social/historical hypothesisのみ | PHI/SOC、必然的中心化law非採用 |
| INT-EQF-057 | centralized→maintained stop | SG | institutional役割比較 | SOC/STOP、維持の因果保証なし |
| INT-EQF-058 | God≠truth/entity/completion | RI | negative-scope guard保持 | 数学的不等式として修理しない |
| INT-EQF-059 | completeclosure ⇒ I→0 | PR | f/rangeに依存する強い帰結は保留 | HORIZON/019/021、monotonicityだけで極限値なし |
| INT-EQF-060 | ∇C≈0 / residual motion | FS | gradient/time/noFPを同一化しない | HORIZON/A、norm/toleranceを発明しない |
| INT-EQF-061 | triangle closure vector sum | SG | physical comparisonとして保存 | commonvector/tolerance未採用、LE存在へ移植しない |
| INT-EQF-062 | nonclosure→attractor→motion | SG | role-kernel比較、D006/007の非同型/非固定scope | ARCH/MODE、cross-scale lawへ昇格なし |
| INT-EQF-063 | Physarum graph naming | RI | nodes/edges命名保持 | 014の密度条件は自動に与えない |

TAを今確定したfamilyは0。impl10の「type annotation MAY suffice」021/033/038は、domainを制限する理論的影響、actionの型、rateの比較基盤が未決なのでFSに置く。これはimpl10の記録変更ではなく、新しいplanning軸での分類。SC3（034/036/037）、RD2（051/052）はdesign対象であり、新式・必須編集件数・採用formを確定しない。旧required equation changes0というreview結果を遡及改変しない。

Migration counts: RI10 / TA0 / SG21 / RD2 / SC3 / HO1 / FS22 / PR2 / RS2 =63。

## 12. Theorem / proof migration plan

Primaryはchild別。old statementの保存とactive scopeの区分を行う計画で、数学的命題を「proposition」と改名するだけではproof gapは直らないため、今回DOWNGRADE TO PROPOSITIONを機械的に割り当てない。

| Unit | Item / source | Primary migration | Surviving ceiling / exact prerequisite |
|---|---|---|---|
| PM15-001 | T3.1 old single-state strict-J kernel / impl11-001 | KEEP LOCAL KERNEL | 旧J/contextと許容点の範囲。newJやrule-changingへの証明移行なし |
| PM15-002 | T3.1 active statement/new-J読解 | RESTATEMENT NEEDED | A/B/T仕様後。全X→admissibleの量化と対象identityを確定してから |
| PM15-003 | cor3.2 fixedpoint表現の局所不両立 | DOWNGRADE TO CONDITIONAL STATEMENT | S=1⇒FPを模型条件として分離。surface stoppingを排除しない |
| PM15-004 | strong no-stopping / all-X historical sketch | HISTORICAL APPENDIX ONLY | D002/003による非採用を表示。現在のmain/Appendixを今移動しない |
| PM15-005 | cor3.3 active relation | MOVE TO CONCEPTUAL DISCUSSION | D006役割類比。isomorphism証明を新造しない、旧強語はhistorical |
| PM15-006 | Fprime / three/four collapse modes | MOVE TO CONCEPTUAL DISCUSSION | D004/007、非網羅・非収束。旧infinite-regress theoremはhistorical |
| PM15-007 | barrier / dynamical non-attainment | WAIT FOR TYPE SPECIFICATION | template保持、solution/domain/ICBCの後もproof未了。新costで代用しない |
| PM15-008 | E outside iterations | WAIT FOR TYPE SPECIFICATION | RU-C/AR006、role非同一と数学的非同値を区別 |
| PM15-009 | LE existence / convergence | WAIT FOR TYPE SPECIFICATION | hypothesisとして継続可。Dのobject/dynamics未定、現attractor proofを修理しない |
| PM15-010 | Φ identity historical proof | HISTORICAL APPENDIX ONLY | D010非採用、co-formationが旧identityの弱い証明という扱いは不可 |
| PM15-011 | μ/error equivalence historical proof | HISTORICAL APPENDIX ONLY | D011別軸。必要/十分のproofを書き直す作業ではない |
| PM15-012 | Ω inclusion proof-like reading | HISTORICAL APPENDIX ONLY | D012literal非採用、temporal extensionはconceptual。実際の所在はP2§1、後日のarchive先未決 |
| PM15-013 | stopping functional/minimum | WAIT FOR RESEARCH | D013future tool。formal object/domain specificationも前提、現在の定理にしない |
| PM15-014 | graph counting examples | DOWNGRADE TO CONDITIONAL STATEMENT | GRAPHのexact/possible/cumulative等のscopeを明記。認知結果は別 |
| PM15-015 | graph→cognitive instability / regeneration | WAIT FOR RESEARCH | p/field/graph/behaviorのbridge未提供、Gettierをproof根拠にしない |

HISTORICAL APPENDIX ONLYはactive theoremからの非採用方針を表すmigration class。現物が既にAppendixに移動済みという主張ではない。保管先、labels/refs/numberingの継承は後続packetで監査し、今変更しない。

Migration counts: KEEP LOCAL KERNEL1 / RESTATEMENT NEEDED1 / DOWNGRADE TO PROPOSITION0 / DOWNGRADE TO CONDITIONAL STATEMENT2 / MOVE TO CONCEPTUAL DISCUSSION2 / HISTORICAL APPENDIX ONLY4 / WAIT FOR TYPE SPECIFICATION3 / WAIT FOR RESEARCH2 =15。

## 13. Figure migration plan — FIG001–014

Phase07 FIGFINALを保全し、impl14のsource/type debtと合わせて再評価。render/asset編集は0。新architecture図を作る計画と、既に凍結された安全なlabel/caption修正を区別する。

| Figure | Content / Phase07 witness | Migration class | Safe scope / prerequisite for more |
|---|---|---|---|
| FIG001 | P1 four-role decomposition | RELABEL | 表層concept、Gettier確認/機構を分離。D016を1:1moduleへしない |
| FIG002 | three axioms | RELABEL | local proposed lower bound、joint十分性の一般認証なし |
| FIG003 | cross-domain examples | RELABEL | role correspondence、独立収束validation非主張 |
| FIG004 | branching explosion | RELABEL | conditional counting / cognitive仮説を分離。具体graph更新はGRAPH待ち |
| FIG005 | four-layer correspondence | CAPTION ONLY | role比較と非typed bridge。D012新extension図は別仕様 |
| FIG006 | C landscape / noFP | CAPTION ONLY | fixedθ/strict条件と未証明barrierを分離。新J/horizon geometryはA/B/HORIZON後 |
| FIG007 | responsive/silent threshold | CAPTION ONLY | nonontology・未較正のlocal scope。residenceの新diagramはSTOP待ち |
| FIG008 | mutual constraint / μ | RELABEL | proposed schema、生成/収束/freedom保証を除くsafe範囲。新type構成はD/E/MU後 |
| FIG009 | LF/LR/LE profiles | HOLD | RU-D＋TR ownership＋必要なSAP/ARCH scope完了、独立type照合後に限る。LE'追加を先行しない |
| FIG010 | emergence comparisons | NO CHANGE | guarded formal-role comparison保持。D009新objectを例から実証しない |
| FIG011 | Φext/Φnet | HOLD | PHI window/network/co-formation relation仕様後。≡の削除だけで新図を完成としない |
| FIG012 | historical stopping sequence | CAPTION ONLY | historical hypothesis / nonprogress、D003residenceをlawにしない |
| FIG013 | phase diagram | RELABEL | qualitative/uncalibrated/modes、narrow stable band保証を除くsafe範囲。新axesはMU/RATE/MODE後 |
| FIG014 | cross-domain homology | NO CHANGE | no shared carrier/mechanism/identity/typed mapのguard保持 |

NO CHANGE2 / CAPTION ONLY4 / RELABEL6 / REDESIGN READY0 / REDESIGN AFTER TYPE SPEC0 / HOLD2 / HISTORICAL ONLY0。新architectureを必要とする二図を安易にREDESIGN READYにしない。その他の新図案もこの表のsafe scopeを超える場合は別type/spec packetを要す。

## 14. Author decision requests — conceptual commitments only

この表は未回答requestの抽出であり、今回回答を推定しない。impl13の18判断を再び未完了に戻すものではない。AR001–006はそこで残った意味・ontology・scopeの細部、AR007は既存documentary未決の再掲。数学的に正しいか、順序の公理、notationの見栄え、証明を救えるかを著者に選ばせない。形式候補7/6/6からの選択は、意味回答後にformal担当が適合性を検査する。

| Request | Question / why necessary | Conceptual options (no recommendation) | Consequences / affected units | Guarded if unanswered? |
|---|---|---|---|---|
| AR15-001 | Fが区別する「同じstate」は現在利用可能な記述か生成履歴込みか。今のFに未実現入力の更新lawまで求めるか | 利用可能state上の実現記述のみ / history-context付き実現記述 / lawも将来対象にするが実現記述と別layer | 同じ局所stateの再訪、F/J入力、iteration scopeが変わる。D001single-state採用は維持、active候補集合には戻さない | YES、generated transitionという概念に留める。RU-Aのactive仕様確定は待つ |
| AR15-002 | 新Jの主対象は生成eventの累積か、有効constraintか、利用可能distinctionか。統合せず複数対象を維持するか | 消失しない生成履歴という理論対象 / 忘却・再配置される有効/利用可能対象 / 複数対象を別に保持 | strict性が失われる可能性を受容し、proofを移植しない。どれがscalarかは後の検査で、strictを著者の選択で保証しない | YES、旧J局所kernelを保存し新Jはfuture |
| AR15-003 | LE'はLE/LRと質的に異なる保持の種類を意図するか、同じ保持の一時的regime/roleか | distinct intermediate / LRまたはLEのregime / 同じobjectに重なるrole属性 | 独立discriminantが必要か、regime/promotion条件が必要かが変わる。使いやすい記号を理由に選ばない | YES、temporary候補として保持、FIG009未解禁 |
| AR15-004 | own LEのownは生成、保持管理、改変可能性、再参照の支配のどれを指すか | endogenous formation / autonomous maintenance/control / 複合条件。accessのみという選択はD017の非自動own方針と再照合が必要 | model-only/runtime/human-toolへの帰属が変わる。境界を広げただけでmodel能力にしない | YES、own認定せずgiven/temporaryを分離 |
| AR15-005 | sapiens-likeの「rule変更」は固定family内の調整も含むか、family/domainの再構成を区別するか | 調整を含む広い塑性だがkindを区分 / parameter調整とrule再構成を別に限定 / 両profileを未統合で保持 | μの部分性、θ-only案の限界、N/R条項の配置が変わる。generalの普遍必要条件へ戻さない | YES、概念profileのまま、RU-E完成仕様は待つ |
| AR15-006 | 「Eはsimple iterationと同一でない」はarchitecture上の役割区別までか、同じ対象で比較可能な数学的非同一まで将来主張したいか | role distinctionのみ / actionの形成過程の区別 / 比較可能な作用ruleの非同一を将来命題とする | typeとquantifierの仕様・proof負担が変わる。outcomeの常時相違や非計算可能性を著者選択から導入しない | YES、semantic directionと旧式HOLDを保持、RU-C比較式は待つ |
| AR15-007 | P1 ENのprimary/authorized-translation statusをどう表示するか（impl09から継承） | parallel未確定を維持 / 明示された著者authorityとして関係を指定 | 数学の真偽は変えない。release metadata/bilingual移行へ影響、P2JA優先で代替不可 | YES、formal検討前は不要。releaseで未確定statusを扱う方針が必要 |

New conceptual clarification requests6、carried documentary request1。いずれも未回答、author decisions made in impl15=0。AR001–006はimpl16の該当仕様採用前に必要だが、全てのalternative整理を停止させるものではない。AR007を数学上のblockerとして全formal taskへ伝播しない。

Authorに問わずformal disciplineで処理するもの: typed compositionの可否、同じcomparison carrier、strict関係の条件、domain境界、rate比較可能性、exact/cumulative count区別、fixedpointと停止の非同一。p→field対応やLE独立同定など新evidenceが必要なものはresearchへ送り、author voteで成立させない。

## 15. Later implementation packages — proposed task boundaries

task番号は提案であり作成/実行を意味しない。packageはunitごとに停止でき、globalな未解決を一つの完了statusへ隠さない。実装前にはその時点のtask-start snapshotと承認済みtarget listを取り直す。

| Package | Exact proposed scope | Entry prerequisites | Exit / stop boundary |
|---|---|---|---|
| impl16 — formal specification decisions | 16a: AR回答記録、16b: A–E/secondaryの選択済み意味に沿う仕様、16c: signature/scope/依存の独立検査。source編集なし | impl15 plan受入、該当AR回答。未回答sliceはalternativeのまま | 仕様contract・old/new/historicalのcrosswalk・statement obligations。解決済みsliceとHOLDを個別表示、equationをまだ編集しない |
| impl17 — equation migration / type repair | 承認済みEQPACKのみ、active/historical配置と型注記/記号移行。変更対象ごとEN/JA差、labels/refs/cites影響を管理 | impl16の対象slice合格、明示されたedit許可。proofに依存する式は証明射程の事前確認までHOLD | math差分の意図照合、prose/Appendix/summaryの逆流検査。非対象式と図は不変、buildしない |
| impl18 — theorem / proof restatement | PM15の採用対象のみ。旧local kernelのscope、新statement、historical非採用を区分。新Jの存在や認知一般を証明したことにしない | 仕様/statement承認、使用する式の型整合。impl17の全63完了は必須でないが対象式との整合は必要 | 独立proof reviewで前提/量化/結論を確認。未証明はfuture/HOLD、式を無断変更しない |
| impl19 — figure / architecture revision | safe presentationとtype-dependent新図を別subpacket。FIG009/011は専用解除条件 | 既存safe laneはPhase07内の個別許可。新図はD/TR/PHI等の承認済みspecと実装scope | EN/JA/format間のlabel・caption・body整合、必要な視覚QA。diagramをproofや測定結果へ昇格しない |
| impl20 — independent consistency re-audit | 実装したsliceのcurrent sourceを独立確認。source/math/proof/figure/summary/authority・frozen scope crosswalk | 各実装record、差分、残存HOLDが揃うこと | PASS/HOLDを別判定。impl08旧prosePASSで新formal実装を自動受入しない |
| impl21 — build / bilingual / distribution audit | 許可されたrelease scopeのbuildとformat/翻訳/配布parity検証。理論修理は含めない | impl20受入、未実装の表示方針とmetadata確認、明示的build/distribution許可 | distributionにcurrent source scopeが反映、未解決研究を消さず記録。今はNO |

impl17→18は便宜的順で、proofを救うよう式を先に変更する指示ではない。依存するstatementの事前設計はimpl16で行い、proof-gated familyはimpl18相当の確認を先に要求しうる。式/証明/図の小packetは整合させるが、gate未了を順序変更で迂回しない。

**Ready-for-edit packetの必須項目:** 対象file/locatorとEQF/claim、採用authority、仕様version、surviving/history/future区分、変更範囲（式/型注記/statement/図のどれか）、依存の充足証拠、未解決proof/research、EN/JA非対称の扱い、検証方法、stop condition。現時点では該当packet承認0。

## 16. Blocker transition table — no global closure

下表のreleaseは**該当実装成分を許可する条件**。旧13blockerのstatus変更、researchの閉鎖、旧uncertainty削除を行わない。概念的非採用を選んだ強い主張についてはproofを完成させるのでなく、active burdenを除いたことの文書/実装確認を必要とする。

| Old blocker | Current owner / decision now available | Prerequisite | Release condition for affected implementation |
|---|---|---|---|
| INT-BLOCKER-001 | formal A/B、AR001/002。single-state/admissible方向は既決 | input/history identity、J/order/context、量化 | A/B仕様受入＋T statement obligation整合。M→historicalの表示承認。旧kernel以外の証明は別 |
| INT-BLOCKER-002 | STOP/T scope、formal C、research | fixedpoint模型とresidence分離、Fprime非定理の表示 | strong no-stopping/infinite regressをactive根拠にしないscope migration受入。全認知停止criterionはOPEN |
| INT-BLOCKER-003 | HORIZON type/proof/research | C/f/domain/ICBC等、barrier非採用のscope | templateの対象版とf例整合が承認されたsliceのみ。invariance proof未了のまま不達定理を再採用しない |
| INT-BLOCKER-004 | GRAPH type、p/field/cognition research | count対象の明示、012のbridge | 014/015条件付き例は独立承認可。012の含意を修理済みにしない |
| INT-BLOCKER-005 | D/AR003/004、research | LR/LE'/LE discriminants、Φschemaのstatus | role/schema実装と存在命題の隔離が受入。存在/収束/検出のresearchは継続 |
| INT-BLOCKER-006 | C/A/D、AR006 | effect/operator/outputとiterate比較の対象 | typed比較またはsemantic-only/historical方針を承認、必要な場合のみ非同一根拠確認 |
| INT-BLOCKER-007 | PHI formal、presentation | window/net/LEの境界・co-formation、≡非採用既決 | active relation仕様とhistorical式の表示を受入。FIG011は専用packet後、identity証明完了とはしない |
| INT-BLOCKER-008 | MU/E type、research | plasticity/delay別軸、量化/system scope | ↔をactiveにしない実装を受入。別軸の実証や必要十分は未成立 |
| INT-BLOCKER-009 | PROV documentary/source missing | exact v2.1未同定のままnode/row検証を分離 | gap表示は承認可能だがverified inheritanceはartifact/row照合まで解除不可 |
| INT-BLOCKER-010 | future research/tool specification | D013future-only、ontology非採用 | future表示の整合のみ可能。functional/minimumのcurrent採用は本計画の対象外 |
| INT-BLOCKER-011 | LIFE conceptual / future formal | literal subset非採用既決、extensionのscope | ⊂historicalとconceptual読解のmigration受入。typed bridgeが完成した扱いにしない |
| INT-BLOCKER-012 | ARCH/D/TR、AR003/004/007 | 非1:1、三system、owner、language metadata | 各architecture成分受入、FIG009専用解除、P1EN metadataは独立処理。言語優先でtype解決しない |
| INT-BLOCKER-013 | E/SAP/MU、AR005 | state/rule/μとgeneral/sapiens、N/R配置 | 条項のscopeと列挙crosswalk承認。六/七・N1/R4を新profileだけで黙って統合しない |

Global blocker closure0、INT-U新設0、SERIOUS変更0、OPEN route閉鎖0。hardness→retention→hardness、LE→feedback→LE、μ→sapiens→μ、window→network→window、horizon→difference→horizonというimpl14のbackedge注意を各仕様のreview checklistへ引き継ぐ。

## 17. Verdict / explicit readiness answers

**FORMAL REMEDIATION PLAN READY WITH MATERIAL OPEN CHOICES。** 全repair対象の仕様質問・移行先・依存・解除条件・ownerを記載した。AR001–006の意味選択と実装前の型仕様が未完でも、その未完を明示した計画は完成できる。これはFORMAL SPECIFICATION COMPLETEではない。

| # | Question | Answer / boundary |
|---|---|---|
| 1 | Formal remediation plan complete? | YES — planning only |
| 2 | Can F be edited now? | NO |
| 3 | Can J be redefined now? | NO |
| 4 | Can theorem3.1 be rewritten now? | NO |
| 5 | Can E∉{F^k} be edited now? | NO |
| 6 | Can LR/LE'/LE be formalized now? | PARTIAL — alternatives/interface検討可、AR003/004未回答の新type採用は不可 |
| 7 | Can rule-plasticity be formalized now? | PARTIAL — scope/interface検討可、AR005とrule identity未決の完成仕様採用は不可 |
| 8 | New author decisions required before impl16? | YES — 正式仕様採用前にAR001–006。impl16冒頭で逐次確認可能、準備を妨げない。AR007は既存release metadata |
| 9 | Direct equation editing allowed? | NO |
| 10 | Proof rewriting allowed? | NO |
| 11 | FIG009 ready? | NO — Gate D/owner/profile未完 |
| 12 | FIG011 ready? | NO — PHI relation未仕様 |
| 13 | Build/distribution ready? | NO |

impl08 source prose acceptance PASS/CLOSEDを保持し、新しいmandatory prose cleanupが再発したという判定をしていない。new author directionsのsourceへの未実装は別のmigration需要。safe presentationの既存PARTIALは維持するが、今回figure作業の許可/実行はない。

## 18. Validation / task-start state

Task-start git status: `${TEMP_EVIDENCE_ROOT}/int_impl15.WZcir8/task_start_git_status.txt`
Full repository SHA-256 snapshot: `${TEMP_EVIDENCE_ROOT}/int_impl15.WZcir8/baseline.json`
Snapshot SHA-256: `11a7e0d38b74c9be3a864be05e1344f1594ec340e8402931c8f4e25d54734a50`

- baseline1,512 regular files（.git内部除外、ignored/untrackedを含む）。既存dirty stateを保全。
- 許可差分は本impl15新規recordとREADME末尾追記のみ。README旧bytesをprefixとして保持。
- Phase00–07 / impl01–14の22records byte-identical。
- Intelligence TeX66の全文hash不変。display98 / inline2199不変。theorem/proof/equation/caption/labels/refs/cites/macros/countersは全文一致により変更なし。
- figures/PDF/BibTeX/source_md/既存working Markdown不変。repository内にnew code/dataなし。
- coverage: Gates5、A候補7、B候補6、E候補6、LE境界6対象、secondary8、EQF63一意、proof migration15、FIG14一意、author requests7、packages6、blockers13一意、explicit answers13。
- DAG29nodes/27edge rows（57expanded edges）、各source→targetが定義済みでacyclic。提出された3chainを検査し、不要なserial依存を除いた。
- `git diff --check` PASS。untracked新recordも末尾空白を検査。
- `git status --short`は開始時と同じ既存M289 / ??9、298行。notes directoryがuntrackedのため今回差分限定はSHA比較で確認。
- source/equation/theorem/proof/figure/caption編集、formal specification実行、build/distribution、simulation/web、commit/pushは全て0。

## 19. Stop boundary

仕様計画・依存順序・migration planning・author request抽出・validationで停止。formalism、new J、LR/LE'判別基準、promotion、rule/meta-rule、typed Φ relation、閾値・metric・estimator・共通carrierを新たに定義/採用していない。impl16以降は別task・必要な回答・scope承認の後でのみ開始する。

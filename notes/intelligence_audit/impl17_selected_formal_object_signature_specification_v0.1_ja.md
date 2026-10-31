# Post-audit implementation 17 — Selected Formal Object / Signature Specification

## 1. Status / authority / method

```text
Post-audit implementation 17: COMPLETE — specification record only
Selected slice: OBS / RU-A / RU-B / RU-D / RU-C(CG interface only)
Verdict: SELECTED FORMAL SPECIFICATION READY WITH MATERIAL ALTERNATIVES
Active-source signature adoption / equation migration: NOT PERFORMED
New-J proof transfer: NOT TRANSFERRED
E operator / full rule-plasticity / Φ / μ-error model: NOT SPECIFIED
Equation migration / proof restatement permission: NO / NO
FIG009 / FIG011: HOLD / HOLD
Build / distribution: NO / NO
```

2026-09-23。本記録はdescriptive metavariablesを用いた**provisional interface/signature specification**である。実在のcarrierや測定可能量、唯一のformalismを採用した記録ではない。仕様のport、入力・出力の型条件、同一性、候補の互換条件を具体化するが、未確定のrelationを成立済みpredicateへ変えない。以下の`StateView`等はこの文書内の型スロット名であって、新しいTeX macro・理論記号・データ構造実装ではない。

Primary: [impl16](impl16_author_clarification_and_formal_specification_contract_v0.1_ja.md) §2–10。Supporting: [impl15](impl15_formal_remediation_specification_plan_v0.1_ja.md) §4–10/14–16、[impl14](impl14_independent_consistency_audit_author_decisions_v0.1_ja.md) §5 gates/§6–10、[impl13](impl13_author_decision_record_d001_d018_v0.1_ja.md) D001–003/008–017、[impl11](impl11_proof_theorem_review_v0.1_ja.md) §5.1/5.2/5.6/5.7、[impl10](impl10_formal_equation_review_v0.1_ja.md) EQF ledger/cluster A/E、[impl09](impl09_authority_adoption_decision_review_v0.1_ja.md)、[Phase07](07_final_audit_and_frozen_dispositions_v1.0_ja.md)、[README](README_ja.md)。

照合したcurrent source: `intelligence-part2/sections/02_inference_operator.tex:11–39`（single-state/scalar Jと集合値版）、`03_nonclosure_theorem_ja.tex:28–100`（許容状態strict-J、fixed θ/A、全X表示と局所proof）、`05_emergent_stopping_layer_ja.tex:49–110`（LR/LEの命名と仮説）、同`:265–279`（E/action/iterationの混在）。これらは旧sourceを今回改訂したことを意味しない。全95claim・63EQFの再監査は行わず、指定sliceと直接依存のみを扱う。

保存値: Phase07 KEEP23/REVISE8/DOWNGRADE21/SPLIT41/RETIRE0/OPEN2=95 FROZEN、SERIOUS001–005 RETAIN、research OPEN24/24、uncertainties236、global blockers13。不変。impl08 PASS/CLOSED、impl13 COMPLETE、impl14 PASS WITH MATERIAL ADVISORIES、impl15 PLAN READY WITH MATERIAL OPEN CHOICES、impl16 INPUTS COMPLETE WITH TYPE WORK REMAININGはtask-time historyとして保存する。

Evidence FE2/CE2/SE2/BE3(citation-background-only)/PE1/XE2/PRE2/OE0、correspondence formal/cognitive/behavioral/biological/social/AI COR3、phenomenal COR1、cross-domain X3、OP2、operational maps/data/sims/tested/validated0不変。以下の数学的placeholderはoperational mapの作成/検証件数へ数えない。新AR・INT-U・SERIOUS発行0。

方法: snapshot→author constraintsと旧type/proof所見照合→candidate signatures→identity/composition/scope検査→readiness→hash検証。candidateの論理条件を明記することと、その条件がIntelligenceについて成立することを別にする。無条件の単一modelは選ばず、反例を隠すためにcontextへ未来結果を埋め込まない。

## 2. OBS analytical interface

### 2.1 Minimal object / scope table

| ID | Object / candidate formal role | Identity condition | Scope / remaining relativity |
|---|---|---|---|
| OBS17-001 | `Scope`: analytical sides、recipient labels、window、timescale、representation conventionの宣言 | 同じ宣言versionと比較規約を持つ場合にのみ同一scopeとして比較 | ontology/legal owner/永久partitionでない。側の再設定はscope変更として記録 |
| OBS17-002 | `StateView(scope)`: system-side current stateの表現carrier | 観察・表現規約の下で同じ値。時点IDの一致とは別 | current input/environment coupling/surfaced historyを扱うportが必要。全archiveを含めない |
| OBS17-003 | `EnvironmentView(scope)`: environment-side stateの表現carrier | 同じ外部観察規約による同一性 | system-sideと同じcarrierとは仮定しない。環境が無限/完全観測可能とはしない |
| OBS17-004 | `SurfacedHistory(scope)`: 現在浮上した圧縮/再構成表現 | 現在の表現の同一性。過去eventの同一性を保証しない | state成分かcontext側portか未選択。沈降/再構成/再浮上で変化可 |
| OBS17-005 | `Context`: input接続・attention条件・環境参照・規則version等を区分して記載するcontext | 必要項目を列挙した範囲での同一性。省略項目の一致を推定しない | state/context/rule別。未来結果そのものを単値化用の隠しcontextにしない |
| OBS17-006 | `Occurrence`: 実現transitionの前後を指す分析上の位置/occurrence handle | 表面値が同じでも同一occurrenceとは限らない | 完全履歴archiveでもsubjectの内部記憶でもない。indexの採番は生成機構の説明でない |
| OBS17-007 | `ObservationWindow / Timescale`: 評価区間と解像度の指定 | 重なるwindowや異なるscaleを同一と扱わない | wall-clock、event順、認知時間を同一視しない。共通数値単位未採用 |
| OBS17-008 | `RetentionSupport`: trace/記録/支持構造を追跡する対象carrier | 下記LR identity contractによる。変形後の同一性は要明示 | 物質/内部表現/networkの共通substrateを仮定しない |
| OBS17-009 | `FeedbackRecipient`: state/history/update条件/external structureへの分析上の帰還先 | side labelとtarget kind、scopeが一致すること | 固定したsubject/ownnessを先に必要としない。帰還先からownerを自動認定しない |
| OBS17-010 | `RealizedTransitionRecord`: before/after/context/realization statusを結ぶ記述 | 同じ実現eventの記述かを表面値とは別に追跡 | 記録の欠落はevent不存在を意味しない。counterfactual completed statesの集合ではない |

### 2.2 Provisional port contract

以下はanalytical interfaceの型スキーマ。`partial`は観察欠落・非定義域を許すことを示し、欠落を0やfalseへ変換しない。

```text
stateView: (Scope, Occurrence) -> partial StateView(scope)
environmentView: (Scope, Occurrence) -> partial EnvironmentView(scope)
surfacedView: (Scope, Occurrence) -> partial SurfacedHistory(scope)
contextAt: (Scope, Occurrence) -> partial Context
endpoints: RealizedTransitionRecord -> (Occurrence_before, Occurrence_after)
recipientOf: FeedbackRecord -> (Scope, AnalyticalSide, TargetKind)
```

`StateView`に`SurfacedHistory`を内包するD案でも、別context portとするA/B案でもよい。同じ情報を二つの独立原因として二重計上しない。port間に完全再構成map、注入性、Markov性、unit、距離は要求しない。`stateView`は非単射でよく、surface recurrenceを許す。viewへの投影が等しいことからoccurrence同一を推定しない。

scope横断には別のcomparison/interface宣言が要る。同一artifactのstatusを人間側/AI側で別に評価できるが、その評価を同じ観察命題として混ぜない。固定θ/Aの局所scopeは明示的tagとして保持できるが、新scopeへの永続適用を保証しない。OBS interfaceは**YES（抽象port contract）**、具体carrier/観測mappingの完全指定はNO。

## 3. RU-A — candidate F signatures

`localTransition`等はFの将来候補を説明するmetaname。partial arrowも未実現入力への予測lawを自動採用しない。実現後の単一出力と、同一入力から全situationsで一意な出力を持つ関数性は別である。

### 3.1 Candidate signature table

| Candidate | Domain → codomain / context | Realized vs unrealized / AR001 | Iteration meaning | Local kernel effect | AR005 / residual burden |
|---|---|---|---|---|---|
| A1 context-indexed partial map | `localTransition(context): DefinedState(context) ⇀ StateView(scope)`。同一context内のinput identityを先に宣言 | 実現したgraph fragmentのみをまず記述。未観測入力の値を補わない。同一input/contextに異なる実現出力があればこのmapの適用単位を再検査 | 同じmapでdefinedness/closureが確認された範囲のみF^k。context変化時は別map列 | state-domain Jでsurface再訪を禁じる採用は不可。occurrence接続が必要 | parameter/context差とrule差を別metadataへ。contextは結果から逆算して決定しない |
| A2 history-conditioned local map | `localTransition(historyContext, context): DefinedState ⇀ StateView`。historyContextは関連する生成positionへの参照/条件で、全履歴archiveでない | surfaced historyの値だけとは限らない条件付けを明記。author方向を保つがhistoryContextの可用性・主体内保持を仮定しない | historyContext列に沿う合成、一般に同じFのpowerでない | history更新まで含むoccurrence側比較なら候補、history固定mapのsurface noFPは別 | history条件の変更とrule再構成は非同一。history情報の選択範囲はOPEN |
| A3 transition relation + realized path | `TransitionDescription ⊆ BeforeDescription × Context × AfterDescription`、そこから**記述済み実現record**を指定。active Fの出力は候補集合にしない | relationは記述上の許容/記録関係であり、未来完成stateの存在論でない。実現path指定は生成前selectorの説明ではない | record列の連接。relation power、選んだpath、同一function powerは区別 | bare relationへ旧single-map proofを適用不可。realized occurrence successionの比較だけ別候補 | rule変更をrelationの変更と断定しない。relation全体のlawは未採用 |
| A4 enlarged state with surfaced-history component | `LocalCarrier`にcurrent state/surfaced-history/coupling等の明示port、`localTransition: DefinedLocalCarrier ⇀ LocalCarrier` | full archiveではない。surfaced成分を内包する構成候補で、現在の表現配置の最終採用でない | 合成closureを確認する場合のみ局所power。表面拡大だけでcontext依存は消えない | surfaced複合値は再訪しうるため、これだけでは新Jのposition carrierにならない | ruleをstateへ隠して三plasticity regimeを同一化しない |
| A5 family of local transition maps | `localTransition[scope, context, ruleVersion]: DefinedState ⇀ StateView`。indexは意味別に区分 | 実現局所mapのfamilyは候補。全入力への予測familyや固定された全未来列は仮定しない | 適切なdomain/codomainを持つ順序付き合成。ruleVersion変更なら同じF^kでない | scope/indexを固定したlocal kernelか、occurrence上の別kernelに限定 | family membershipの変更とparameter変更を識別する作業は将来RU-Eへ |

これらは排他的五択でなく表現family。A2/A5も「単値化できるまで未知の全条件を入れる」という決定論的完成を認定しない。local functionを主張するなら、指定input/context粒度での関数性は追加の仕様義務。実現recordにevent IDを付すだけの単値性は、全入力lawの独立根拠にならない。

### 3.2 Minimum viable signature family — common interface, not winner selection

**MVS-A:** scope、before/after occurrence、before/after view、context参照を持つrealized-transition interfaceと、それをF表記へ渡す**局所single-output adapter**を分離する。adapterは今回の唯一のF定義でなく、A1–A5が満たす共通受入契約である。

```text
realizedSuccessor[recordScope]: EligibleOccurrence ⇀ Occurrence
stateView(scope, before), stateView(scope, after): partial StateView(scope)
```

`EligibleOccurrence`はendpointsとscopeが記載され、記述対象のtransitionが同定された入力。複数の記録が同一入力から別出力を示すなら、単一map adapterは不適合としてrelation側へ差し戻す。後付けで全てを同一mapと宣言しない。occurrenceは「その時点の主体stateの正式拡大」を採用するものでなく、現象と記述の混同を避ける分析port。

実現前の揺らぎ/route readabilityはContext/SurfacedHistoryの候補portに留め、未実現完成stateのenumerationをMVS-Aの要件にしない。realizedSuccessorのdefinednessは全時間で保証しない。record scopeが変わる列では比較接続を明示し、sourceの`F^k`と同一視しない。

minimum remaining checks: input identity、局所関数性の根拠/宣言scope、context/history配置、codomainの接続、同じruleの判定、J評価carrierへの接続。数学的候補の選定・検査事項であり、現時点で新著者clarificationを要求する理由にはしない。F signature fixed: **PARTIAL、source-ready NO**。

## 4. RU-B — generative order / J

### 4.1 Five separate roles

| Role | Candidate target | Allowed change / nonidentity |
|---|---|---|
| generative order | 実現occurrenceの生成上のposition | 新Jの対象方向。scalar量・memory archiveではない |
| accessible / surfaced history | SurfacedHistoryとaccess context | 沈降/再浮上/再構成可。Jへ同一化しない |
| retained history | RetentionSupportと保持状態 | erosion/compression可。全generated eventを保存する必要なし |
| effective constraint | 現在updateへ効くconstraintの記述 | 強弱/適用域が変わりうる。生成順序の増加とは別 |
| distinction visibility | 観察scopeで識別可能な差の記述 | attention/windowに依存。生成されたことと見えることは別 |

### 4.2 Candidate order table

| Candidate | Carrier / evaluation candidate | Relation requirement / what is not implied | Compression / admissibility / debt |
|---|---|---|---|
| B1 scalar order parameter | `orderPosition: Occurrence → OrderedScalar`、partial evaluation可 | 数値単位/間隔/速度に意味を与えない。strict stepは別前提 | scalarはmemory量でない。全eventへ埋込み可能・測定可能と仮定しない |
| B2 ordinal-like index | `orderPosition: Occurrence → OrdinalLikePositions` | sequence順位の候補。well-order/全順序を採用する負担が増える | 同時/比較不能eventの扱い未定。序数への列挙だけで認知noFPを示さない |
| B3 preorder | `orderPosition: Occurrence → PositionCarrier`とreflexive/transitive比較候補 | preorder自体ではself comparison可。strict partを使うなら別宣言、同値class内stepはstrictでない | 圧縮の同値と生成position同値を混同しない。strict性の追加が必要 |
| B4 partial order | 同carrierとreflexive/antisymmetric/transitive比較候補 | comparableな厳密前進が当該stepにあるか別。非同一だけでは比較可能性を保証しない | 全系/全stepのlinearizationを要求しない |
| B5 strict relation | 同carrierと`strictlyBefore`候補 | local kernel最低条件はirreflexive、各対象stepの比較。transitivityはorder/周期排除を扱う際に別必要 | 単なるirreflexive graphを全履歴のorderと呼ばない |
| B6 history-indexed order position | `(recordScope, occurrence) → GenerativePosition` | 表面値と分離したpositionを同じcontextで評価。index差だけを観測的生成証拠にしない | 保存されたhistory imageが消えてもposition記述の意味と区別可。strict/order structure未選択 |
| B7 event-order structure | 実現event/occurrenceと前後incidenceのcarrier、Jをpositionの参照として読む候補 | 順序を既知として置くならorder axioms/範囲を明記。有限記録から全生成史の非循環性を認定しない | path内順と複数経路間の比較を分離。生成objectを実在的event ontologyへ固定しない |
| B8 family of order observables | 固定したfamilyの各`orderObservable: Occurrence → DeclaredCarrier` | aggregation/比較ruleなしでは「>」を付けない。前後で都合よく別observableへ交換不可 | accessibility等を含むdiagnostic familyと新Jの生成order familyを区別。strict component/共通関係未決 |

### 4.3 Candidate minimum carrier / kernel obligations

**MVS-B:** 同じanalytical scopeで実現前後を指す`Occurrence`と、その`GenerativePosition`へのwell-definedな評価portを候補最小carrierとする。Occurrenceが主体内に保存される全履歴を含む必要はない。位置の異なりを採番で表せても、その記述規則が現実の生成原理であるとは認定しない。B1–B8のどれでposition/relationを実現するかはOPEN。

kernel検査条件（K1–K6、採用済み理論axiomではない）:

1. K1: compared objectのidentityとcarrierが同じで、fixed-point等式を意味づけられること。
2. K2: 前後の評価が同じevaluation/context/comparison carrierに属すること。
3. K3: 採用するstrict関係が自己比較を許さないこと。scalar性・metricは必須でない。
4. K4: 対象transitionのendpointにF/J相当の合成が定義されること。
5. K5: definedness、入力scope、固定θ/A、rule/context version等によりcandidate admissibilityを先に記載し、strict stepは別の明示premiseとして確認すること。
6. K6: 結論を同じcarrierとadmissible domainの局所範囲に留めること。surface viewの同一性からoccurrence同一を推定しないこと。

admissibilityは「noFPになる点」や「進歩する認知」の言換えにしない。strict成立点だけを選ぶ条件模型を作る場合も、独立な認知適用の証拠を得たとしない。新Jについてのstrict stepはauthorの不可逆蓄積方向から証明なく転用できない。

**Kernel status:** scalar以外でも構造的候補はあるがNOT TRANSFERRED / NOT PROVED FOR NEW J。Occurrence上の非自己移行をposition labelで保証する構成は記述上のkernelとなりうるだけで、surface state noFP、停止不能、無限推論、rule-changing系へ何もliftしない。transitivity/無限列の存在/全反復admissibilityはこの一段の検査と別。

## 5. RU-A × RU-B typed compatibility matrix

40 combinations。ここは**型接続の候補互換性**でありproof validityではない。P=`POSITION PORT COMPATIBLE`（MVS-A/Bのoccurrence portを介する限り型接続可能）、R=`REPRESENTATION CONTRACT REQUIRED`（厳密関係、index/scope、aggregation等の追加指定が要る）、U=`SURFACE-ONLY IS INSUFFICIENT`（元のstate複合値だけでは新J評価を供給しない）。Pでもconcrete carrier/orderとstrict性は未確定。

| F candidate | B1 scalar | B2 ordinal-like | B3 preorder | B4 partial order | B5 strict relation | B6 history-position | B7 event-order | B8 family |
|---|---|---|---|---|---|---|---|---|
| A1 | R | R | R | R | R | P | P | R |
| A2 | R | R | R | R | R | P | P | R |
| A3 | R | R | R | R | R | P | P | R |
| A4 | R | R | R | R | R | U | U | R |
| A5 | R | R | R | R | R | P | P | R |

A1/A2/A5のPは**候補mapをMVS-Aの実現recordへ接続した場合**であり、bare surface-mapからJを計算できる意味でない。A3のPもchosen realized recordのpositionだけを比較し、relation全体へ関数proofを適用しない。A4のUはsurfaced-historyをstateへ足すだけでは生成positionを復元できないこと。別occurrence portを併置すれば検討可能だが、その追加を既存enlargementに内在するとしない。

同一`StateView`かつ異なるgenerative positionを許容する仕様では、`J: StateView → position`というcontext-free関数に両方を載せることはできない。この**禁止する合成**を新しい採用signatureに混入させない。候補群そのもののmaterial contradictionではなく、rejected combinationの明示である。

## 6. RU-D — substrate identity and reversible regime architecture

### 6.1 Candidate representations

| Candidate | Formal representation candidate | Preserves AR003 | Remaining burden / failure |
|---|---|---|---|
| D-A same LR object + regime label | `regimeDescription(support, scope, window)`のlabel/role属性 | LE'をsupportと別typeにせずroleへ置ける | label付与基準がなければ再命名だけ。排他的・網羅的3値partitionは仮定しない |
| D-B continuous retention variables | 同support上の複数retention/persistence attributes | 漸次変化を表しうる | 数値尺度/単位/閾値・連続性は未提供、現在採用不可。hardnessを万能scalarにしない |
| D-C partial-order regime relation | scope固定のretention configurations間の比較候補 | 同supportの異なる状態を比較しうる | 比較不能を許す。時間遷移がorder増加だけとはしない。orderをpromotion/dynamicsと混同しない |
| D-D hybrid role/state representation | support identity、observed configuration、reference/scaffold/retention roleを別port | LR/LE'/LEの重なりとreversible role変化を表せる | 役割の必要条件/充分条件、configurationの同一性は個別指定要 |

最低contractは全候補共通の「追跡するsupportの同一性」と「scope/window相対のrole/configuration記述」の分離。D-Dを唯一本体として選ぶのではなく、他候補もこれらを区別できるよう要求する。

### 6.2 LR / LE' / LE regime table

| Role / regime | Substrate identity | Re-reference / persistence / hardness | Feedback and reversibility | Formal status / remaining empirical work |
|---|---|---|---|---|
| LR | registered trace/history supportのcarrier。current sourceのlayer/motionそのものと単一物体を同定しない | accessを失ってもtrace supportの追跡identityは別。消失すれば同一objectが残るとは言わない | recursive参照のsubstrate role。feedback可能性だけでLEにしない | PROVISIONAL FORMAL SPEC：object/role分離。trace continuityのmappingは未検証 |
| LE' | LR supportがtemporary scaffoldとして働くregime。同じsupport IDを再利用し、新typeへcastしない | temporal layers間の再利用role。短さだけで定義しない。hardness/persistenceは別attribute | reuse/attention/externalizationで働きが変わり、沈降・support喪失も許す | PROVISIONAL FORMAL SPEC：regime schema。具体判別基準はOPEN |
| LE | LRに関係するretention support/組織化構造のquasi-stable role。単一traceとの1:1を要求しない | 特定windowで参照/保持roleが継続することを別に記述。permanent storeでない | recipientへのfirst-order feedback availabilityはauthor方向の必要条件、十分条件ではない。erosion/再編を許す | PROVISIONAL FORMAL SPEC：必要なportまで。quasi-stabilityのcriterion・存在/収束はOPEN |
| own LE | LE roleとownness interfaceの組合せ、別substrate typeでない | accessibility/control/originだけでownとしない | 持続的帰還の方向・標的をscope相対で評価 | graded interpretation、scoreなし、own認定は未実施 |
| given/external LE | recipientに与えられるretention role、出自とaccessを別記 | givenであることは受け手側で永続することを保証しない | reference後の変化がどこへ返るかを追跡。自動own化しない | scope-relative descriptionのみ |
| shared/network LE | 複数recipientが接続するretention role/組織 | shared breadthとwindow diversity、hardnessを同一化しない | 双方向feedbackでも単一ownerを捏造しない。各scopeでLE'等との併存可 | network dynamics/Φ relationは本slice外、未検証 |

### 6.3 Identity and regime acceptance contract

`supportAt`/`configurationAt`/`referenceRole`は同じsupportを異なるwindowで記述するport。物質的コピー・traceの再構成・network統合を「同じobject」と認める規約は対象ごとに明記する。regimeが変わっても、追跡identityを維持する限りLR supportである。支持物が破壊されたのに名前だけで同一性を保存しない。newly formed composite LEに単一LR IDを無理に引き継がせない。

LE'をregimeにするのは、scaffoldとしての**作用roleの変化**を既存supportへ付すためで、新carrier/new layerへ移すためでない。LEのより安定という方向は、宣言したwindow/perturbation記述に対するretention roleの維持を対象とするが、topology、摂動分布、許容時間、数値閾値は今回定義しない。したがってLE'とLEを現在機械的に全例分類できるとはしない。

reversibilityは、同supportのwindow別role記述で後のLE-like→LE'-like/弱参照/アクセス喪失を禁止しないことで表す。逆写像や可逆力学、一方向promotion operatorを導入しない。same artifactが異なるsystem/timescaleでgiven LE/LE'/shared retentionであってもよい。ownnessは分類軸に混ぜない。

回答: LR identity維持=追跡規約の維持、LE'=role/regime、LE=scope付き準安定で非永久、複数scopeの異regime=YES、promotion不要=YES（記述architectureとして）。**Formal distinguishability: PARTIAL**、独立discriminants・実証は未了。

## 7. Ownness interface — no score

| ID | Port / candidate relation | Minimum arguments / target | Limit / independent criterion |
|---|---|---|---|
| OWN17-001 | directed feedback relation | reference/use occurrence、support、from-side、recipient、Scope | directionをlegal/origin ownerから推定しない |
| OWN17-002 | persistence-indexed relation | 同feedbackの観察window/再利用機会、retention description | 「強い」「持続的」の数値weight/普遍尺度なし。期間だけでownerを決めない |
| OWN17-003 | target-of-change descriptor | state / surfaced history / update conditions / external structureを別kind | update条件変化の記述からrule reconstructionを認証しない |
| OWN17-004 | re-reference/control interface | access、実行されたreference、reference制御可能性、reuseを別記 | access/利用/制御は別、存在しないcontrolを補わない |
| OWN17-005 | relational predicate family | support、recipient、scope/window、direction/persistence/target descriptors | ownness interpretationの候補。全例のbinary own判定やtotal rankingを要求しない |
| OWN17-006 | weighted relation alternative | 上記relation＋重み候補（未採用） | scale/normalization/比較根拠なし、current contractでは数値を使わない |

provisional minimumはqualitativeなdirected/persistence-indexed descriptorsのfamily。`FeedbackRecord`は帰還の記述単位、`feedbackEvidenceStatus`はproposed / observed-description / causally-supported等を混同しない注記portであり、本taskでobserved/causally-supported事例を認定しない。predicateを真にする物理/認知criterionは独立mapping待ち。

`ownnessDescription(support, recipient, scope, window)`の出力はこれらの帰還記述の束/比較未了statusであり、実数scoreではない。二recipientの比較不能、双方へのco-maintained interpretation、情報不足を保持できなければcontract不適合。ownnessの強弱を表す最終順序/集約ruleは未選択。

OBSのanalytical sidesは観察の便宜、ownness/subject-like境界は帰還から解釈する対象。後者を先に仮定して帰還先を切り出す循環を避ける。**Interface PARTIAL**：argument/target分離はspecified、dominance/persistence/比較の具体意味とmappingは未了。

## 8. RU-C(CG only) — interaction-preserving coarse-graining

### 8.1 Candidate comparison

| Candidate | Preserved / discarded | Failure condition | Circularity / future-outcome risk | Empirical obligation |
|---|---|---|---|---|
| CG-A feedback-relation-preserving map | typed interaction recordsと指定feedback relationを保存。無関係な細部を縮約可 | path/recipient/typeを潰す、未支持の帰還を作る | Eの有無でrelationを定義しない。後続effectは観測済みprefixか明示モデル内に限定 | feedback relationの独立同定、細部を捨ててよい根拠 |
| CG-B quotient of interaction classes | 指定したinteraction queriesで同等なdescriptionを同classへ | 同class内で必須queryが相違、pathをspliceして偽loop生成 | downstream outcomeだけでclassを作ってeffectを「証明」しない | class基準と異なるcontextへの安定性を確認 |
| CG-C sufficient-statistic-like interface | 事前に指定したfeedback-relevant queryの回答に必要な情報を保持 | omitted情報によりquery結果が変わる | probability/modelなしで統計的十分性と呼ばない。将来の答を入力に埋め込まない | 対象queryと分布を選ぶなら別empirical/probability仕様 |
| CG-D path-equivalence by downstream effect | 独立指定したpath descriptor/effect comparisonを保存する候補 | outcome同じでも帰還path/recipientが異なるのに同一化 | 最大のcircularity risk。same outcome≠same interaction、future outcomeoracle不可 | effect criterion・path由来・比較条件の独立証拠 |
| CG-E relation-preserving projection | system/environment/retention/feedbackのportと指定relationを投影 | 忘却した成分で必要な帰還区別が変わる | projectionが存在することをE形成証明にしない | retained relationと実系のmapping、scope外への一般化不可 |

### 8.2 Provisional preservation contract / typed placeholders

E自体を定義せず、`FineInteractionDescription`と`CoarseInteractionDescription`は同じOBS scopeでの**分析記述**のcarrierとする。完全microstate空間を持つとは仮定しない。required-query familyはcoarse-graining選択より先に、E判定や目的の結論に依存せず宣言する。

```text
coarsen[scope]: AdmissibleFineDescriptions -> CoarseInteractionDescription
fineQuery[queryKind]: AdmissibleFineDescriptions -> DeclaredDescriptor
coarseQuery[queryKind]: CoarseInteractionDescription -> DeclaredDescriptor
```

これはmap-familyのcandidate interface。quotient/projection等の具体採用ではない。`DeclaredDescriptor`はrelation/有無/未観測/比較不能等を型別に扱うportであり、一律Boolean・scalarにしない。

preservationの**formal acceptance obligation**は、指定されたqueryについて`coarseQuery(coarsen(description))`が`fineQuery(description)`と同じ宣言済み比較規約で一致すること。従ってcoarsenが同一視する二descriptionでrequired answerが異なるなら不適合。まだそのようなmapの構成・存在・非自明な縮約を証明していない。identity mapはこのobligationを空虚に満たしうるが、有用なcoarse-grainingやE説明を得たとはしない。

| CG contract | Required query / relation | Failure / prohibition |
|---|---|---|
| CG17-001 boundary interface | analytical sidesとrecipient/target kindを区別 | coarse側で双方を融合して帰還先が消える、ownerを新たに固定 |
| CG17-002 externalization | supportの外在化に関するorigin/path/reference port | object copy/transformと単純同一を取り違える |
| CG17-003 external persistence/transformation | outsideでの継続/変形の記述とwindow、unknownの保持 | 途中の喪失を無視して恒久retentionを捏造 |
| CG17-004 feedback path | 対象pathと順序/incidence/recipientの区別 | fineでないpath/loopをquotient上のvertex同一化で生成。必要なpathにはfine witness/lifting又はspurious-path禁止を別検査 |
| CG17-005 later influence | 対象transition/target kindと、独立指定したeffect/evidence descriptor | 「後で変わったもの」を帰還と定義し同じ変化を帰還因果の証明に使用 |

関係をforward-preserveするだけでは余分なcoarse edge/pathを認める場合がある。required queriesに関するreflection又はpath-liftingの検査も必要で、全microstructureのisomorphismは要求しない。CG17-005のeffective influenceは、後続変化との相関記述と因果的影響の認定を区別する。causal criterion未供給ならそのqueryはunknown/proposedのままであり、保存contractを満たしても因果性の証明ではない。

### 8.3 Circularity and temporal boundary

記録済みの有限prefixに含まれるlater transitionを記述することは、未実現future-state ontologyの採用ではない。未発生のeffectについては、明示モデルでのconditional queryかunknownとし、未来結果をcoarsenの隠れ入力にしない。データ駆動でqueryを選ぶ将来作業では、同じ観測を選択理由と独立検証に二重使用しない。

purely formalに指定できるのはtype ports、query先行宣言、同一視に関する整合条件、path保存/偽path排除、unknown扱い、scope限定。実際のinteraction/feedback/effective influence、独立なquery criterion、relevance、縮約が観測に耐えるかはresearch work。研究24は閉鎖しない。

**CG contract specified: YES、concrete coarsening/map/model: NO。** relation/cardinality/probability/metric/causal operatorは採用しない。Eの型・E対F^kの式・rule塑性・Φへの変換はここで定義しない。

## 9. Cross-spec consistency

| Check | Pair | Status | Result / residual obligation |
|---|---|---|---|
| CROSS17-001 | OBS ↔ F | CONSISTENT WITH GUARD | realized recordとviewを別にし、context/side/timeのscope変更を隠さない。actual関数性の適用範囲は別確認 |
| CROSS17-002 | F ↔ J | CONDITIONAL | MVSのoccurrence portで合成候補は得たが、J carrier/order/strict性は未採用。bare surface-domain Jへの帰還禁止 |
| CROSS17-003 | F ↔ LR regime | CONDITIONAL | transitionとtrace登録/保持は別relation。全F作用が持続traceを残すとのpremiseを追加しない |
| CROSS17-004 | J ↔ LR regime | CONSISTENT WITH GUARD | 生成positionと保持/表現を分離。erosionでJを減らす/生成historyを消す同一化をしない |
| CROSS17-005 | LR regime ↔ ownness | CONDITIONAL | support/regimeと方向/持続/標的の帰還descriptorは別。hardnessや長さだけでown認定不可 |
| CROSS17-006 | LR regime ↔ coarse-graining | CONDITIONAL | queryがscaffold/retention/erosionの必要差を失わない条件が必要。regime識別基準そのものをCGから逆定義しない |
| CROSS17-007 | ownness ↔ coarse-graining | CONDITIONAL | recipient/direction/windowとunknownを保持。coarse loopだけで共同ownershipを生成しない |
| CROSS17-008 | J ↔ coarse-graining | CONSISTENT WITH GUARD | CGが同じviewへ潰すことと生成position同一を分離。CGにglobal J保存を追加せず、必要なら将来queryとして別負担 |

Counts: CONSISTENT0 / CONSISTENT WITH GUARD3 / CONDITIONAL5 / TENSION0 / CONFLICT0 / INSUFFICIENT SPECIFICATION0 =8。これはprovisional port contractの照合結果。impl16のF/J TENSIONを旧式内で解消したわけではなく、surface/occurrence分離によって候補仕様内の接続条件として隔離した。formal/specification completionや実証合格の件数ではない。

Rejected formal conflicts: surface値だけに依存するJが同じsurfaceへ異なるorder値を与える指定、event/effectとfunction familyの無型non-membership、regime labelを独立typeへpromotionする指定、feedbackを捨てたquotientで帰還因果を証明する指定。本specはこれらを同時採用しない。選んだ条件付きcontract間にmaterial conflictを確認しないが、具体modelのglobal consistencyを証明したのではない。

SERIOUS001–005 RETAIN。noFP→停止不能、LE命名→形成/停止存在、Φ naming→identity、μ塑性→error equivalence、Gettier→確認のいずれも再導入しない。新circularity認定なし。independent predicates/queriesの未指定を独立証拠で埋めたとしない。

## 10. Provisional signature contract table

StatusはPROVISIONAL FORMAL SPEC / ALTERNATIVE / FUTURE RESEARCH DEPENDENT / HISTORICAL ONLYのいずれか一つ。具体modelの採用statusとは別。コードは文書内IDで理論記号でない。

| Contract | Object | Candidate signature / relation | Status | Remaining boundary |
|---|---|---|---|---|
| SIG17-001 | State/context | OBS partial view ports、入力/環境/surfaced history/rule versionを別記 | PROVISIONAL FORMAL SPEC | carrier/context配置・input identityの具体化 |
| SIG17-002 | F common adapter | `realizedSuccessor[recordScope]: EligibleOccurrence ⇀ Occurrence`、stateViewとの接続 | PROVISIONAL FORMAL SPEC | active source Fの最終型でない。A1–A5と関数性の検査 |
| SIG17-003 | F family realization | context/history/map-family/relation-path/enlarged surfaced-state | ALTERNATIVE | 未実現futureを全域定義しない |
| SIG17-004 | J/order structure | `orderPosition: Occurrence → partial GenerativePosition`、同一scopeのcomparison port | PROVISIONAL FORMAL SPEC | B1–B8未選択、strict premise未認証 |
| SIG17-005 | order representation | scalar / ordinal-like / preorder / partial / strict / history-position / event / observables | ALTERNATIVE | comparison/aggregation/評価domainの追加指定 |
| SIG17-006 | LR substrate | `supportAt(scope, window): RetentionSupport`の追跡記述、欠落可 | PROVISIONAL FORMAL SPEC | sourceのlayer/motionとのobject-role crosswalk、同一性継続 |
| SIG17-007 | LE' regime | `scaffoldRole(support, scope, window)`のrole descriptor | PROVISIONAL FORMAL SPEC | binary判定/新type/数値thresholdなし、discriminants待ち |
| SIG17-008 | LE regime | `retentionRole(support, recipient, scope, window)`の準安定/参照/feedback descriptor | PROVISIONAL FORMAL SPEC | 固有attractor・存在・充分条件なし |
| SIG17-009 | feedback relation | record/support→recipient/targetを結ぶscope/window付き関係 | PROVISIONAL FORMAL SPEC | 実際の因果的feedback認証はしていない |
| SIG17-010 | ownness relation family | support/recipient/scope/windowにdirection/persistence/target descriptorsを付す | PROVISIONAL FORMAL SPEC | graded比較・dominance未定、scoreなし |
| SIG17-011 | coarse-graining interface | coarsen、fine/coarse required-query portsとpreservation obligation | PROVISIONAL FORMAL SPEC | map構成/非自明縮約/実測mapping未実施 |
| SIG17-012 | feedback / influence mapping | descriptive recordを観測/因果criterionへ対応づける課題 | FUTURE RESEARCH DEPENDENT | E存在と同じ定義で検証しない |
| SIG17-013 | set-valued active F | current EN候補集合式の強いactive読解 | HISTORICAL ONLY | sourceに現存、削除/同期しない。relation候補で再採用しない |
| SIG17-014 | active E∉{F^k} theorem | current保存式、E/actionとiterateの型未定 | HISTORICAL ONLY | D008/AR006により現在well-typed theoremとして非採用。replacement未指定 |

Counts: PROVISIONAL FORMAL SPEC9 / ALTERNATIVE2 / FUTURE RESEARCH DEPENDENT1 / HISTORICAL ONLY2 =14。port仕様の件数とsource equation familyの件数は別である。

## 11. Theorem3.1 kernel compatibility — no proof rewrite

§5の40 typed combinationsについて、kernel観点を別に示す。K=`KERNEL COMPATIBLE IN PRINCIPLE`、R=`REQUIRES NEW PREMISE`、N=`NOT COMPATIBLE`、U=`UNDECIDED`。全セルはK1–K6を対象とする**occurrence/local candidate kernel**に限り、old state-domain theoremとの同一視を禁止する。

Kは必要portが接続する候補でありstrict性が実証/証明済みという意味でない。Rは追加の比較/評価規約またはoccurrence接続が必要。bare relation、context-varying evaluation、surface-only Jをそのまま使う場合は下のrejected tableでNとする。

| F candidate | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 |
|---|---|---|---|---|---|---|---|---|
| A1 | R | R | R | R | R | K | K | R |
| A2 | R | R | R | R | R | K | K | R |
| A3 | R | R | R | R | R | K | K | R |
| A4 | R | R | R | R | R | R | R | R |
| A5 | R | R | R | R | R | K | K | R |

K8 / R32 / N0 / U0 =40 candidate combinations。N0は現式が全てcompatibleという意味でなく、表がguard付きcandidateを対象とするため。B6/B7でもorderの非反射性・step比較はK1–K6として将来必要。B1–B5の追加指定はscalar/順序型を使うだけでは何を評価し、どのstepがstrictか決まらないため。B8は同じ評価関係を前後に維持するaggregation/選択規約を追加要。

| Rejected or deferred reading | Kernel status | Why |
|---|---|---|
| bare A3 relationへ旧function proof | NOT COMPATIBLE | relation fixedpointと実現successorのidentityを区別していない |
| A4 surface-compositeのみ＋異なるJ位置を同一入力へ付与 | NOT COMPATIBLE | 評価がfunctionでなくなる。occurrence/context追加は別仕様 |
| preorderの非減少のみでstrict noFP | NOT COMPATIBLE | self comparisonを排除しない |
| 前後で違うJ/contextの値を比較して旧F(x)=xを否定 | NOT COMPATIBLE | 同一評価に対する自己比較のkernelではない |
| indexを毎回増やすだけで認知state noFPを主張 | NOT COMPATIBLE | bookkeepingの非自己同一と認知stateの同一性は別 |
| rule-changing family全体への局所proof移植 | UNDECIDED | RU-E/full model対象外、新たなpremise/reapplication未指定 |

single-step kernelにはglobal iteration closureは不要だが、そのstepでbefore/afterが同じ比較carrierに置けることが必要。複数step、finite cycle、無限regress、変動ruleへの推論は別。surface recurrenceを保持し、Jのconceptual nonreturnはその表面再訪の否定に使わない。

**Local kernel structurally preservable?: PARTIAL（条件付きcandidateあり）。Proof transfer/restatement now?: NO。** theorem3.1のstatement designは比較するcarrier/量化/前提の候補表を作る範囲でPARTIAL、最終restatementやproof本文作成へは進めない。

## 12. Affected blocker impact

| Blocker | Conceptual part resolved? | Type part resolved? | Proof part resolved? | Research part resolved? | Source-edit readiness / next condition |
|---|---|---|---|---|---|
| INT-BLOCKER-001 | YES、single-state実現方向とgenerative J、全域law非採用 | PARTIAL、OBS/occurrence portsを設計。carrier/order/context/関数性は未採用 | NO、新J kernelへ未転用。旧local kernelは旧scopeのまま | NO | NO。A/B具体contract選定・適用域/合成の独立検査が必要 |
| INT-BLOCKER-005 | YES、LE'はLR regime、LE hypothesis | PARTIAL、support/role分離。Φ入力出力・regime discriminants未完 | NO、存在/一意/収束は未成立 | NO | NO。regime/specとgeneric emergence operatorは別。名前だけで生成proofを作らない |
| INT-BLOCKER-006 | YES、Eはfeedback interaction方向、反復回数でない | PARTIAL、CG受入contractまで。E自体のtypeとF^k比較は未指定 | NO、non-derivability等を復活させない | NO | NO。CGの具体model/independent criterionとEの将来scope指定が先 |
| INT-BLOCKER-012 | YES、非1:1 architecture、三system scope、AR007二authority | PARTIAL、regime/ownness portのみ。profile/Transformer/P1-P2表示未実装 | NO、新architecture存在・能力のproofは供給しない | NO | NO。独立interface受入・TR/ARCH scopeとbilingual plan、FIG009 HOLD |

対象4のtype完全解消0、proof解消0、research解消0、global blocker closure0。BLOCKER012のproof欄は新たにproof義務を作るのでなく、profileの能力/存在を本仕様から証明したとしないという境界。残り9blockersは今回再判定せず不変。

## 13. Affected EQF readiness / impl18 planning boundary

Primary statusは指定11familyごと1件。FORMAL SPEC READY=source移行用の型・scopeが固定済み、PARTIAL SPEC=typed interfaceはあるが具体署名/条件未確定、HISTORICAL ONLY=現author方向でactiveから区別すべき保存読解。旧Phase07/impl10 ledgerは更新しない。

| EQF | Current object / impl17 impact | Primary status | May enter impl18 planning? / blocked action |
|---|---|---|---|
| INT-EQF-025 | x_next=F(x)、realized adapter/候補A1–A5 | PARTIAL SPEC | YES、候補差分・scope計画のみ。F replacement未決でmigration NO |
| INT-EQF-026 | J(F(x))>J(x)、occurrence/order port | PARTIAL SPEC | YES、評価carrier/strict premise一覧まで。新不等式採用NO |
| INT-EQF-027 | noFPと背理法 | PARTIAL SPEC | YES、量化/identityのstatement-design依存表まで。proof/式書換NO |
| INT-EQF-031 | generic U=Φ(layer motion,H) | NOT READY | NO、generic emergence object/Φはselected slice外。LR仕様で全layerに型を与えない |
| INT-EQF-032 | LE=Φ(LR motion,H) | PARTIAL SPEC | YES、output roleとsubstrate/regimeのcrosswalkまで。Φ map/存在は未指定 |
| INT-EQF-033 | E[LE,x] / E∉{F^k} | NOT READY | NO、CG-only仕様ではE/actionの型や比較を決めない。historical読解を注記する計画は別 |
| INT-EQF-047 | 旧J:X→R | PARTIAL SPEC | YES、old scalar Jとnew position評価の分離案まで。新J型の確定NO |
| INT-EQF-048 | EN集合値F | HISTORICAL ONLY | YES、active/history status移行の文書計画のみ。source削除/別式への置換許可ではない |
| INT-EQF-050 | LF→trace/LR→LE arrows | PARTIAL SPEC | YES、transition/registration/retentionの別burden計画まで。連鎖をtyped causal lawにしない |
| INT-EQF-054 | μ→B→E-site→LR convergence→LE | NOT READY | NO、μ/RU-E/E/Φ/convergenceの多重依存はslice外。LRのregimeだけで連鎖を閉じない |
| INT-EQF-055 | environment locus↦E-site | PARTIAL SPEC | YES、environment/recipient/feedback portのscope計画まで。E-site assignmentや全域map未定 |

Counts: FORMAL SPEC READY0 / PARTIAL SPEC7 / WAIT FOR RESEARCH0 / HISTORICAL ONLY1 / NOT READY3 =11。WAIT FOR RESEARCH0は研究不要という意味でなく、型/範囲がprimary未了でresearchがsecondaryに残る。

impl18 **planning eligible8**: 025/026/027/032/047/048/050/055。031/033/054のreplacement計画は追加spec待ち。**migration eligible0**、isolated-family editingもNO。048のstatusは著者方向として確定済みでも、EN/JA本文・proofとの参照移行設計・独立確認を終えた意味でない。

## 14. Handoff / remaining work

次に必要なのは本specのcandidateから、対象sliceに限ったcarrier、evaluation、local transition adapter、LR判別条件、required-query semanticsを明示する仕様選定と独立type/scope確認。新たなauthor requestではなくformal実務の候補比較を続けられる。選択が今回のauthor commitmentsを変える場合だけ、その時点で確認する。

```text
OBS scope / identity ports
  -> A candidate + actual/local function criterion
  -> B carrier / relation / admissibility -> local kernel statement design only
OBS + LR support/regime discriminants -> ownness descriptor interface
OBS + A + LR + independently declared feedback queries -> CG contract realization
CG realization -> future E type/comparison specification (NOT this pass)
LR/ownness + future TR/ARCH scope -> FIG009 gate (still HOLD)
future Φ relation specification -> FIG011 gate (still HOLD)
selected concrete spec + independent type/proof-scope check
  -> individually authorized migration/proof/figure task
```

研究handoffは既存OPEN24へ保持: surfaced historyとgenerated orderの観測mapping、LR/LE'判別、quasi-stability/first-order feedback、graded帰還/ownness、independent influence criterion、coarse-graining relevance。metrics/thresholds/experimentsは設計しない。

impl08受入済みproseを今回の未実装formal候補で再度HOLDに変更しない。現在sourceにold equation/attractor語/集合Fが残ることはauthor adoption migration debtとして記録し、今回全prose acceptanceを再監査した扱いにしない。P1 JA semantic priority / EN stabilization、P2 JA primary / EN working draftは維持、自動同期しない。

## 15. Verdict / explicit answers

**SELECTED FORMAL SPECIFICATION READY WITH MATERIAL ALTERNATIVES**。READYはcandidate interfacesと互換条件を次のspecification受入の入力にできるという限定。actual signatures/scopesの全固定、operational realization、proof移行、source edit解禁ではない。

| # | Question | Answer |
|---|---|---|
| 1 | OBS interface specified? | YES、minimal abstract ports/scope/identity contract。具体mappingは未指定 |
| 2 | F formal signature fixed? | PARTIAL、common realized adapterまで。A1–A5のactive採用未決 |
| 3 | J formal carrier/order fixed? | PARTIAL、occurrence/position分離まで。B1–B8/strict性未採用 |
| 4 | LR/LE'/LE formally distinguishable? | PARTIAL、support/regime区分あり、classification discriminants未完 |
| 5 | Ownness interface formally specified? | PARTIAL、relation arguments/targetsのみ、graded比較未完 |
| 6 | Interaction-preserving CG contract specified? | YES、query/path/type保存obligations。具体map/empirical criterionはNO |
| 7 | T3.1 local kernel structurally preservable? | PARTIAL、条件付き候補。新J proof transferはNO |
| 8 | Any new author clarification required? | NO |
| 9 | Any material conceptual conflict? | NO、selected conditional contracts内。global consistency証明でない |
| 10 | Any formal conflict? | NO、新candidateの採用contract間。§5/§11の不適合合成は明示的に除外、旧source欠陥未修理 |
| 11 | Equation migration may begin for selected slice? | NO、planning8familyとmigration0を分離 |
| 12 | Proof restatement may begin? | NO、conditional statement designのみPARTIAL |
| 13 | FIG009 ready? | NO |
| 14 | FIG011 ready? | NO |
| 15 | Build/distribution ready? | NO |

## 16. Validation / task-start state

Task-start status: `${TEMP_EVIDENCE_ROOT}/int_impl17.qoha68/task_start_git_status.txt`。
Full repository SHA-256 snapshot: `${TEMP_EVIDENCE_ROOT}/int_impl17.qoha68/baseline.json`。
Snapshot SHA-256: `eca7ca0367d6340f8e3c7c7fb1be52243e95844749e5be9c1d08d15fd9b4563e`。

- Baseline1,514 regular files（.git内部を除きignored/untrackedを含む）。開始時既存dirty状態を比較基準とする。
- 許可差分: impl17新設＋README末尾追記のみ。既存README bytesをprefixとして保持。
- Phase00–07/impl01–16の24records byte-identical。Intelligence TeX66全文hash不変、display98/inline2199不変。全文一致によりtheorem/proof/equation/caption/labels/refs/cites/macros/counters不変。
- figures/PDF/BibTeX/source_md/既存working Markdown不変。新code/dataなし。
- Coverage: OBS10、F candidates5、J candidates8、compatibility40＋kernel40、regime候補4/role6、ownness ports6、CG candidates5/targets5、cross-spec8、signature contracts14、blockers4、affected EQFs11、explicit answers15。
- `git diff --check` PASS、new recordの末尾空白・表の列数・ID/分母を検査。
- `git status --short`: task-startと同じ既存M289 / ??9（298行）。notes directoryがuntrackedのため、git表示だけでなく全file hashで今回差分を検査。
- source/equation/theorem/proof/figure/caption edit、build/distribution、simulation/web、commit/pushは未実施。

## 17. Stop boundary

selected formal object/signature candidate specification、compatibility、readiness、validationで停止。E operator、rule-plasticity full model、Φ、μ/error relationを形式化していない。型候補をcurrent theoryへ採用せず、新Jの証明を記述していない。equation migration、proof restatement、figure redesign、build/distributionは別途の後続taskを要する。

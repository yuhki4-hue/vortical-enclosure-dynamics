# Validation Basis Transition Working Note v0.1

## A Research Program on Unstated Material Changes During Scientific Claim Extension

- **Version:** 0.1
- **Date:** 2026-08-21
- **Status:** research program only / working note / corrigible / framework・methodology の発表ではない
- **Primary test object:** 指定された source–target claim extension における artifact-level omission
- **Comparison standard:** 同一の時点固定資料を用いる独立した field-native review
- **Current evidence:** negative control 2件、positive diagnostic case 0件
- **Novelty posture:** 概念的部品の大半は prior art。増分的な診断価値は未検証
- **Relation to VED:** 独立。VEDへの証拠的支持を与えない

---

## Project Status

1. 普遍的な観測非一意性定理・内部観測者不可能性定理の探索は失敗し、撤回済みである。
2. `validation basis` は field-native な warrant 条件を比較するための作業語にすぎず、新しい科学的対象ではない。
3. adequacy-for-purpose、context of use、external validity、transportability、applicability domain、model credibility、robustness、uncertainty qualification が概念領域の大半を既に扱う。
4. GST と metrology は negative control であり、generic vocabulary は field-native reconstruction を上回る技術的診断を与えなかった。
5. 本protocolだけが一意に、またはfield-native reviewより再現可能に検出した materialかつunstatedなsource–target changeはまだない。早期検出はsecondary outcomeとする。
6. v0.1が直接検査するのは指定文書での omission のみであり、institutional under-enforcement と field-level conceptual absence は射程外である。
7. 次に許される作業は、preregistered / time-sliced / head-to-head comparison である。
8. 読みやすい表や一覧を作っただけでは成功としない。
9. 再現可能で decision-relevant な差が出なければ、本programはreview/synthesisへ降格または終了する。

---

## 1. Status and non-claims

本ノートは、主張を繰り返し縮小した後の再スタート地点である。定理発表、普遍的observability theory、科学的validationの新formal theory、確立したmethodologyではない。現時点の位置づけは **research program only** である。

検査対象は経験的かつ比較的である。scientific claimがassumptionやdomain of validityを持つ、という既知の一般論を再主張するのではない。問うのは、明示的なsource–target comparisonが、同じ資料を読む独立field-native reviewerに比べ、materialに変化したが明記されていないwarrant条件を一意に、またはより再現可能に検出できるかである。早期検出は、測定方法を事前固定できた場合に限るsecondary outcomeとする。

本ノートは以下を主張しない。

- `validation basis` が新概念である。
- validation条件の変化が新発見である。
- claim extensionに一つの一般理論が必要である。
- same-field changeが一般に見落とされる。
- 学問分野の境界が本質的に危険である。
- 記法、形式、理論名、研究共同体の連続性が必ずvalidation changeを隠す。
- 普遍的なobservability mapを構成できる。
- D1–D4分類が必要または妥当である。
- `transport license` がfield-native terminologyより優れる。
- generic auditが既存のreview、validation、quality practiceより優れる。
- Lagrangian formalismにこの種の固有欠陥がある。
- 一つの文書でのomissionがinstitutional failureまたはfield-level absenceを示す。
- extension後の失敗が、当時その条件を検出可能だったことを示す。
- 本programがVEDその他の独自理論を支持する。

`scientific claim extension` も暫定語である。extrapolation、generalization、transportability、matching、calibration range外への適用、新populationへの移送、新しいcontext of useなど、分野により精密な語があれば常にそちらを優先する。

### Claim-status tags

- **[ESTABLISHED]**: 引用可能な結果、一次資料、または完了済みnegative controlに支持される。
- **[PRIOR ART]**: 比較対象となる既存のfield-native概念・実務。
- **[WORKING DEFINITION]**: 局所的な索引規約であり、新規性を主張しない。
- **[HYPOTHESIS]**: 本programが今後検査する。
- **[UNTESTED]**: preregistered comparisonをまだ受けていない。
- **[WITHDRAWN]**: 反例、prior-art reconstruction、Erasure Testにより撤回・降格した。
- **[OPEN]**: 未解決。可能な場合は必要な次の検査を併記する。

---

## 2. Why this project was restarted

出発点は、観測・予測成功が生成構造の一意的同定を与えるか、という問いだった。その懸念を普遍定理へする試みは順次失敗した。その後、prerequisite、assurance relation、observability、claim transportを広く図示する案へ移ったが、成熟分野との比較では一般語彙の側が精度で劣った。

残ったのは新frameworkではなく、次の棄却規律である。

> field-nativeな枠組みがtarget、scope、equivalence relation、uncertainty、calibration dependence、validation ruleを既に精密に記述するなら、generic vocabularyがdiagnosis、design、scope judgment、evidence retrieval、decisionのいずれも変えない限り、それを消去または降格する。

この再スタートでは野心の単位を変える。scientific successの背後にある普遍構造を探さず、選定したclaim extensionについて一つの狭いcomparison procedureが測定可能な増分価値を持つかだけを問う。

### Why the question is not terminated immediately

概念的中心は、adequacy-for-purpose、context of use、external validity、causal transportability、applicability domain、distribution shift、robustness、uncertainty quantification、model validationに大部分が吸収される。このためconceptual noveltyは現時点で支持されない。

ただし、本project内で未実施の経験的比較が一つ残る。outcome情報を隠して固定したsource–target inventoryを、独立したfield-native reviewとhead-to-headで比較したとき、material judgmentに差が生じるかである。語彙ではなく、この **diagnostic delta** だけがreview paperを超えて調査を続ける理由である。

---

## 3. Historical demotion log

失敗は成果の一部であり、静かに削除しない。

| Earlier hypothesis / vocabulary | 魅力 | 壊れた理由 | 現在の扱い |
|---|---|---|---|
| Observation-map nonuniqueness theorem | 異なる候補が同じlogを持てばontological uniquenessが阻まれるように見えた | 非単射なら逆像が一意でないのは定義的で、inverse problems / identifiabilityが既に扱う | **[WITHDRAWN]** 新定理ではない。初等的背景のみ保持 |
| Internal observer / self-containment impossibility | observerとその計算も系内に含めると完全自己記述を妨げるように見えた | self-containment単独ではnonidentifiabilityは出ない。自己記述可能な構成があり、不可能性には追加資源・device条件が要る | **[WITHDRAWN]** 普遍含意を撤回 |
| Generation–log non-isomorphism | stabilization / loggingが情報損失を強制するように見えた | lossやnon-isomorphismを定義に入れれば結論を仮定している。coarse graining等はclass-dependent | **[WITHDRAWN]** 一般定理ではない |
| Resource hierarchy / persistent ontological fiber | 各有限観測ではcandidate fiberが残る | 無限候補は極限で一点化しうる。有限候補は有限段階で分離されうる。model classとresourceに依存 | **[WITHDRAWN]** class-independentではない |
| Deferred Resolution | calibrated tomographyからGST、quotient、拡張modelへの流れが反復的boundary relocationに見えた | conditional inference、nuisance/reference parameter promotion、joint estimation、identifiability modulo gauge、model checking / extensionでより精密に再構成できた | **[WITHDRAWN]** 独立mechanismではない。GSTをfrozen negative caseとする |
| Assurance provenance | 異種support relationを一枚で見たかった | assurance case、traceability、evidence、calibration、validationが既に扱う可能性が高く、優越診断を示していない | **[UNTESTED]** indexing aid以下 |
| Claim transport / transport license | 異分野のreuseを共通化できるように見えた | causal transport、EFT matching、measurement→decision、evidence→recommendation等はobjectとvalidity criterionが異なる | field-native relationを優先し、generic labelを降格 |
| Observability map / D1–D4 | 学際的な共有partitionを作れそうだった | instrumental access、structural identifiability、finite-sample estimability、resource bound、in-principle impossibilityは一軸でない | **[WITHDRAWN]** universal partitionではない |
| Web of constraints | 異種のscientific supportを可視化した | metaphorだけではedgeを定義せず推論も変えない。nodeとlocal edgeの大半はprior art | organizational vocabulary以下 |
| Cross-field boundary | 分野差がassumptionを見えにくくするように思われた | 学際越境は必要条件でも十分条件でもない。same-field extrapolationもあり、cross-field transferが明示的に管理される場合もある | explanatory variableではなくproxy候補へ降格 |
| Validation-regime transition | disciplineでなくvalidation conditionの変化へ焦点を移した | regime/domain/scope/context of use/transportは既存文献が広く扱い、単なるextrapolation再記述になりうる | より弱い比較語`validation basis`へ置換 |

次の訂正も維持する。

- `inside/outside`ラベルは数学的差の十分条件ではなく、具体的なcausal/resource interfaceを要する。
- observational / predictive successとontological interpretationは同じ主張ではないが、この論理的区別は新定理ではなく、scienceの独立した強い支持を否定しない。

---

## 4. Prior art first, then a minimal working definition

### 4.1 Existing concepts take precedence

以下の部品は既存分野で、しばしば本ノートより精密に扱われる。

- **adequacy-for-purpose / fitness for purpose:** modelが無条件に正しいかではなく、指定purposeにadequateか。
- **context of use / model credibility:** computational modelが指定decisionで担うroleと、そのriskに対応するcredibility evidence。
- **validation domain / application domain:** validation evidenceがintended applicationを支持する範囲と、そこからのextrapolation。
- **applicability domain:** predictive modelが適用可能とみなされる範囲。
- **external validity / generalizability / transportability:** sample、population、environment間で結果をtarget claimへ移す条件。
- **distribution shift / out-of-distribution performance:** developmentとdeploymentの分布差とpredictionへの影響。
- **robustness / sensitivity analysis:** assumption、parameter、perturbationの指定変化に結論が耐えるか。
- **uncertainty quantification / metrological traceability:** uncertaintyとreference relationの評価・伝播・報告。
- **model checking / misspecification / iterative revision:** model classのadequacyとfailure後のexpansion・revision。
- **matching / running / approximation control:** scale間でeffective descriptionを用いるfield-specific条件。
- **conformity assessment / decision rule:** measurement resultとuncertaintyをactionへ接続する規則。

**[PRIOR ART]** Parkerのadequacy-for-purposeはmodel qualityをparticular purposeに相対化し、一つのcontextでのperformanceを別のcontextのevidenceにする難しさを明示する。FDAのcomputational-model credibility guidanceはcontext of useとrisk-informed credibilityを中心に置く。PearlとBareinboimはselection diagramによりsource–target differenceとcausal transportを形式化する。OECDの(Q)SAR guidanceはregulatory modelにdefined applicability domainを要求する。これらは弱い類似ではなく、旧構想の概念内容を相当程度吸収する。

### 4.2 Validation basis

> **[WORKING DEFINITION] Validation basis:** The set of evidence, assumptions, scope conditions, uncertainty treatments, and acceptance criteria actually used within a field to warrant a specified claim for a specified target and use.

日本語では、指定されたclaimを、指定されたtargetとuseについて受容するために、その分野で実際に使われている証拠、仮定、適用範囲、不確かさ処理、判定基準の組、とする。

これは比較用indexである。field-native termを置換せず、全分野が同じ仕方でclaimをvalidateするとも仮定しない。各caseの実質分析では、この語を分解して分野固有の概念へ戻す。

定義はclaim-relativeかつuse-relativeである。同じmodelでも、記述、screening、高consequence decisionではacceptance criterionが異なりうる。

### 4.3 Minimal inventory

source warrantについて、少なくとも次を確認する。

1. empirical / experimental access;
2. identifiable estimand、target、またはequivalence class;
3. model class、approximation、structural assumption;
4. uncertainty / error treatment;
5. validation / application domain;
6. intervention、preparation、calibration、sampling、measurement conditions;
7. acceptance、falsification、credibility、decision criterion.

この一覧は完全でも普遍的でもない。field-native reviewは項目を統合、分割、置換、または不採用にできる。

---

## 5. The remaining research question

> **[HYPOTHESIS / UNTESTED] Can a structured source–target comparison detect material, unstated changes in the validation basis of a scientific claim during extension, when those changes are not already covered by field-native invariance, robustness, transport, applicability, or target-validation machinery?**

実用上はさらに強い比較を要求する。

> 同じfrozen corpusを用いたとき、structured comparisonは独立field-native reviewが検出しない変化を検出するか、またはその検出をより再現可能にし、acceptableなfalse-positive rateの下でdecision-relevantな差を生むか。

早期検出はprimary outcomeに含めない。secondary outcomeとして使う場合は、elapsed time、documents read、retrieval回数、または最初のjustified flagが固定記録された時点のどれで測るかをpreregistrationで指定する。

### 5.1 Null and alternative

- **Null:** field-native review、validation guidance、通常のexpert practiceが同じmaterial differenceを見つけ、同じscope、uncertainty、model、experiment、decisionの判定へ至る。generic comparisonにはmethodological added valueがない。
- **Alternative:** structured comparisonだけが、またはfield-native controlより再現可能に、prospectively justifiedなartifact-level omissionを検出し、独立expert adjudication後にscientific judgmentまたはdecisionが変わる。

### 5.2 Unit of analysis

分析単位は「theory」「discipline」「object」ではない。固定時点で利用可能な文書と結びついた、指定source claimと指定target reuseである。

したがって「classical mechanics→quantum gravity」「laboratory→nature」のような例は、claim、target、use、evidence set、decision consequenceを特定しない限り検査対象にならない。

---

## 6. Claim identity

changed warrantを探す前に、**何が同じだからsourceからtargetへの「延長」と呼ぶのか**を明示する。population、conditions、scale、useの変化はcandidateを除外する理由ではなく、多くの場合まさに検査対象である。

作業上、claimを次の二部分に分けて記録してよい。

\[
C=(P,Q)
\]

- \(P\): assertionのcore content。主張されるproposition、relation、quantity、またはphenomenon。
- \(Q\): application qualifiers。population / system、conditions、scale、use、accuracy、uncertainty、decision contextなど。

これは新formalismでも、全分野に共通するclaim ontologyでもない。何を \(P\) と \(Q\) に置くか、また両者を分けられるかはfield-native analysisに委ねる。

典型的なextension candidateは、core contentを追跡可能な意味で維持しながらqualifiersを変える場合である。

\[
(P,Q_s)\longrightarrow(P,Q_t)
\]

このとき、\(Q_s\) と \(Q_t\) の差がsource warrantへmaterialかを検査する。たとえばsame measured relationをdifferent populationへ、same model outputをdifferent decision useへ、same approximationをdifferent scaleへ用いる場合である。

一方、\(P\) 自体がmaterialに変わり、source warrantもtarget claimの支持として使われていないなら、原則として **new claim** として除外する。\(P_s\neq P_t\) でもsource resultからtarget resultへのfield-nativeな導出・近似・transport relationが明示される場合は、自動除外せず、その継承関係自体を固定する。

| Working role | Claim component | Source | Target | Same / changed / unclear |
|---|---|---|---|---|
| \(P\) candidate | Proposition / relation / quantity / phenomenon |  |  |  |
| \(Q\) candidate | Population / material / system / process |  |  |  |
| \(Q\) candidate | Experimental / environmental / operating conditions |  |  |  |
| \(Q\) candidate | Intended descriptive / predictive / explanatory / decision use |  |  |  |
| \(Q\) candidate | Accuracy / uncertainty / loss / decision threshold |  |  |  |
| \(Q\) candidate | Time horizon / scale（relevantな場合） |  |  |  |

同じ文言・数式・表示量だけでは \(P\) の実質的同一性もextension関係も保証しない。逆に \(Q\) が変わることだけで別claimとして棄却してはならない。claim identityは本protocolの最も壊れやすい箇所であり、preregistrationとexpert adjudicationの対象に残す。

---

## 7. What counts as a material source–target change

transition candidateに入れるには、以下6条件をすべて満たす。

1. source claimのwarrantが条件 `q` にmaterialに依存する。
2. targetでは `q` が変化、不成立、または未確認である。
3. targetでsource claimが比較可能なconfidence、scope、accuracy、decision significanceの下で再利用される。
4. `q` の変化を被覆するfield-nativeなtheorem、invariance result、robustness result、error bound、transport formula、matching condition、applicability rule、direct target validationが確認できない。
5. 差を考慮すればscope、uncertainty、experiment / measurement design、model choice、acceptance decisionの少なくとも一つが変わりうる。
6. 選定した歴史時点の対象文書で、material changeとbridgeの有無が明示されていない。

### 7.1 Materiality test

差がmaterialであるには、field-native argumentが次の少なくとも一つを支持する必要がある。

- validation argumentが同じ形では成立しない。
- error / uncertainty boundが変わる。
- identifiability、calibration、approximation control、transportabilityが変わる。
- 新しいtarget experiment、measurement、sensitivity analysis、robustness checkが要る。
- accepted domainまたはconfidenceを狭めるべきである。
- downstream decision ruleまたはactionが変わりうる。

analystの直観だけでは足りない。field-native result、guidance、empirical study、expert adjudicationへ結びつける。全materiality判断をexpertが事後供給し、structured comparisonがretrievalやconsistencyにも寄与しないなら、本programへの反証と数える。

### 7.2 No outcome-based shortcut

後のfailureはhistorical benchmark選定には使えても、prospective detectabilityを証明しない。後のoutcomeを知らず、当時利用可能な情報だけで差とconsequenceを構成できた場合に限りaudit evidenceとなる。

---

## 8. Three meanings of “silent”

`silent`は誤解を招くため、次の三層を分ける。

### A. Artifact-level omission

指定paper、protocol、model report、submission、decision documentに、materialなsource–target differenceまたはbridge statusが書かれていない。

v0.1の直接対象はこれだけである。結論は「cutoff (t) におけるcorpus (D)で未開示」と文書相対的に書き、「fieldが知らなかった」としない。

### B. Institutional under-enforcement

relevant concept、standard、validation practiceは存在するが、peer review、regulation、procurement、implementation、routine practiceで十分に運用されない。

これを示すにはreview record、compliance data、workflow observation、interview、implementation audit等の組織的証拠が要る。文書比較だけでは示せない。

### C. Field-level conceptual absence

fieldにmaterial differenceを表現・検査する概念や方法が存在しない。

最も強い主張でありv0.1の射程外である。terminology difference、literature fragmentation、retrieval failureと区別できる大規模systematic prior-art auditを要する。

AからB、BからCを推論してはならない。

---

## 9. Minimal source–target comparison protocol

これはcandidate procedureであり、validated methodではない。

### Step 1 — Claim identity

sourceとtargetで同じもの・変わるものを、core content \(P\) とapplication qualifiers \(Q\) に分けて固定する。population / system、conditions、scale、intended use、accuracy、uncertainty、decision thresholdの変化は自動除外しない。追跡可能な \(P\) またはfield-nativeな継承関係がなく、source warrantもtarget supportとして使われていなければnew claimとして終了する。

### Step 2 — Source validation basis

field-native literatureだけでsource claimのwarrantを再構成する。evidence、structural/statistical assumption、calibration/preparation conditions、uncertainty treatment、validated domain、acceptance criterionを記録する。generic headingでnative conceptを置換しない。

### Step 3 — Target difference inventory

source–target差をfield-native languageで列挙する。frozen corpusに支持される差だけを含め、later failureだけから変化を推測しない。

### Step 4 — Materiality test

各差がsource validation argument、error bound、identifiability result、calibration relation、approximation control、applicability condition、acceptance criterionを変えるか問う。根拠sourceを記録する。

### Step 5 — Existing bridge search

invariance、matching、robustness、sensitivity、transportability、uncertainty expansion、applicability rule、direct target validation、explicit scope restrictionを探す。十分なbridgeがあればgeneric concernを解消または降格する。

### Step 6 — Disclosure test

material differenceとbridge statusがcontemporaneous paper、protocol、model report、decision documentに明示されたか確認し、可能なら正確な箇所を記録する。

### Step 7 — Field-native control

独立field-native reviewerが同じfrozen corpusを、`validation basis`語彙やsource–target checklistなしで分析する。比較前にcontrol reportを固定する。structured armへ広い資料を与えない。

### Step 8 — Disposition

少なくとも以下から判定する。

- no material change;
- change covered by existing field-native bridge;
- direct target evidence required;
- claim scope should be narrowed;
- uncertainty should be widened / recomputed;
- model / estimand / decision role should be revised;
- currently unsupported for the stated target/use;
- unknown / unassessed.

結果は一つのclaim useに対する判定であり、theoryやfield全体の評価ではない。

---

## 10. Existing-bridge search and Erasure Test

### 10.1 Field-native bridge search order

最もspecificなnative resultから外側へ探す。

1. direct target validation / target data;
2. theorem / exact invariance;
3. field-specific matching / transport / equivalence result;
4. validated robustness / sensitivity / error bound;
5. applicability-domain / context-of-use argument;
6. explicit uncertainty expansion / conservative decision rule;
7. unsupported reuseを防ぐdeclared scope restriction.

field間のepistemic strengthを順位づけるものではなく、retrieval順序にすぎない。

### 10.2 Erasure Test

分析後に`validation basis`、`transition`、`silent`等のproject vocabularyを消し、field-native termsだけで結果を書き直す。

- 同じfact、scope judgment、decisionが回復すれば、generic layerの価値はorganization / pedagogy以下である。
- field-native rewriteの方が精密なら、そのcaseでgeneric vocabularyを積極的に降格する。
- diagnostic differenceが残るなら、labelでなく、どのoperationが差を生んだか特定する。

### 10.3 Control comparison

methodological valueには、次のpreregistered outcomeの少なくとも一つでcontrolとの差が必要である。

- material omissionの検出;
- justified detectionまでの時間（secondary。測定単位を事前固定した場合のみ）;
- scope / uncertainty judgment;
- 要求されるmeasurement / experiment / validation activity;
- model / estimand revision;
- downstream decision;
- relevant-source retrieval completeness;
- false-positive rate.

読みやすい表を作っただけでは成功としない。

---

## 11. False-positive exclusions

次はcase-specificな反証がない限りcandidateから除外する。

1. **Ordinary parameter variation:** validation / sensitivity analysis済みdomain内の変化。
2. **Declared extrapolation with control:** extrapolationが明示され、適用可能なerror / robustness / transport resultがある。
3. **Representation change only:** observable content、target、decisionを変えない記法・parameterization変更。
4. **Explicitly handled decision-context change:** 新decision roleが明示され、適切なdecision rule / credibility assessmentがある。
5. **Model refinement with new validation:** target modelが変更され、新useについて独立validateされている。
6. **Genuinely new scientific question:** source warrantをtarget supportとして再利用していない。
7. **Already documented limitation:** source / target資料がscope restrictionまたは未解決statusを明示する。
8. **Pure implementation failure:** standard / procedureがmissing checkを明示要求するがlocal implementationが従わない。
9. **Known-standard noncompliance:** missing comparison conceptでなくenforcementの問題。
10. **Field-native scope restriction:** literatureがsource claimを既に限定し、alleged extensionをlicenseしていない。
11. **Different claims:** quantity、equation、theory nameの表面的連続性に反してestimand/useが変わる。
12. **Decision-irrelevant omission:** downstream decisionに不要で、正当に要約・委譲された情報。

`backgrounded`、`referenced elsewhere`、`transformed but recoverable`、`omitted`を`lost`にまとめない。downstream文書がupstream detailを全て反復しないことは、それ自体で欠陥ではない。

---

## 12. Negative controls

### 12.1 GST Case 01

**[ESTABLISHED FOR THIS CASE]** 仮説した反復的Deferred Resolution chainは支持されなかった。standard QPT、self-consistent estimation、GST gauge、operational quotient target、model checking、fixed Markovian gate-set外へのextensionは、conditional inverse problem、nuisance/reference parameter promotion、joint estimation、identifiability modulo gauge、reporting convention、misspecification、model-specific extensionでより精密に再構成できた。

generic languageを消してtechnical conclusionは失われず、一部で精度が上がった。したがってGSTはpositive evidenceでなくfrozen negative controlである。詳細は [GST Case 01 v0.2](./deferred_resolution_case_01_gst_v0.2.md)。

### 12.2 Metrology Case 02

**[ESTABLISHED FOR THE STUDIED CORPUS]** metrological traceability、calibration、measurement uncertainty、stated scope、conformity decision ruleが、measurement resultをdownstream useへ運ぶ強いfield-native architectureを既に与えていた。generic handoff auditだけが見つけたmissing condition、scope error、decision difference、retrieval improvementはなかった。

判定はorganizational valueのみで、より厳しいno-added-value判定も可能だった。また、supportはtransferで必ず失われるという見方への反例として、preservationを制度的に設計できることを示した。詳細は [Metrology Case 02 comparison](./scientific_assurance_case_02_metrology_comparison.md)。

### 12.3 Controlsから言えること／言えないこと

保持するのは次の棄却規則だけである。

> field-native machineryがsource–target difference、equivalence、uncertainty、scope、decision criterionを既に表現するなら、generic comparisonを降格する。

全scientific extensionが適切に管理されることも、generic omission theoryも示さない。本programはfailure 2件、positive diagnostic case 0件から始まる。

---

## 13. Candidate historical and contemporary cases

以下はいずれもpositive evidenceではない。source由来のfact、prior-art interpretation、project hypothesisを分ける。

### 13.1 Hydroclimatic stationarity

- **[ESTABLISHED]** Milly et al. (2008)は、水資源計画で用いられてきたstationarity assumptionがchanging climateと整合しないと論じた。
- **[PRIOR-ART INTERPRETATION]** 現在のhydrology / climate-risk literatureはnonstationarity、robustness、scenario uncertainty、adaptationを明示的に扱う。current conceptual absenceではない。
- **[HYPOTHESIS]** broad recognition以前のtime-sliced corpusなら、historical-distribution assumptionを長寿命のfuture planningへ使う際の差を、contemporaneous ordinary reviewより再現可能に検出できるかもしれない。早期性を測る場合はsecondary outcomeとする。
- **[UNTESTED / RISK]** 以前のhydrological literatureが既にlimitを明示していた可能性がある。その場合はnegative controlまたはunder-enforcement候補となる。

### 13.2 Google Flu Trends

- **[ESTABLISHED]** systemはsearch behaviorとinfluenza surveillanceのhistorical relationをnear-real-time estimationへ使い、後の分析は大きなprediction failure、search behavior、algorithm dynamics、model updatingを論じた。
- **[PRIOR-ART INTERPRETATION]** concept drift、measurement-process change、distribution shift、dynamic recalibrationが自然な記述を与える。
- **[HYPOTHESIS]** contemporaneous source–target comparisonなら、platform-mediated data-generating process changeへのexplicit validationを要求できた可能性がある。
- **[UNTESTED / RISK]** proprietary predictorとhistorical corpusが不十分で、source/target claimを再現可能に固定できない可能性がある。通常のtime-series / surveillance validation以上を与えないかもしれない。

### 13.3 Pulse oximetry across populations and clinical uses

- **[ESTABLISHED]** controlled studyは大規模な2020年のoccult hypoxemia研究以前からskin-pigmentation-related performance differenceを報告し、2020年研究はmeasurement disparityをclinically relevant thresholdへ接続した。
- **[PRIOR-ART INTERPRETATION]** field-level conceptual absenceは考えにくい。artifact-level disclosure、target-population evidence、device testing requirement、institutional under-enforcementの区別が中心となる。
- **[HYPOTHESIS]** time-sliced document auditは、指定device claim / clinical protocolが既知のlimitationを明示せずaccuracy evidenceを別populationまたはthreshold useへ持ち込んだか検査できる。
- **[UNTESTED / SCOPE LIMIT]** under-enforcementの立証にはv0.1を超えるregulatory / organizational evidenceが要る。

### 13.4 Materials machine learning

- **[ESTABLISHED]** materials database間のdistribution shiftで大きなperformance degradationが生じうることが報告され、robustness / generalizabilityが分析されている。
- **[PRIOR-ART INTERPRETATION]** applicability domain、OOD generalization、uncertainty、dataset shiftは既存のnative/adjacent conceptsである。
- **[HYPOTHESIS]** 具体的screening claimがnative domain checkなしにsource-domain performanceを新materials regionへ使う場合に限り、structured comparisonが役立つ可能性がある。
- **[UNTESTED / EXPECTED CONTROL]** 現在のliteratureは差を明示するため、positive caseよりnegative control候補である。

### 13.5 Lagrangian candidate

- **[ESTABLISHED]** 本projectは具体的positive caseをまだ特定していない。
- **[WITHDRAWN]** 「Lagrangian formalismがvalidation changeを隠す」は粗すぎ、現時点のclaimではない。
- **[ENTRY REQUIREMENT]** specific Lagrangian / effective action、source claim、target claim/use、source validation basis、changed target condition、contemporaneous literature、missing bridge、calculation / experiment / uncertainty / interpretationへのeffectが必要である。
- **[DISPOSITION]** これらが揃うまでaudit caseにしない。

### 13.6 Candidate triage

| Case | Likely field-native description | Artifact omissionを直接検査可能か | Main confound | Current role |
|---|---|---:|---|---|
| Hydroclimatic stationarity | nonstationarity、extrapolation、scenario / robust planning | Potentially | hindsight、earlier recognition | Preferred historical benchmark |
| Google Flu Trends | concept drift、algorithm dynamics、surveillance-model validation | Potentially | proprietary / changing data process | Secondary benchmark |
| Pulse oximetry | subgroup measurement performance、clinical-threshold validity | 指定文書ならYes | known prior evidence / under-enforcement | Artifact–institution discriminator |
| Materials ML | distribution shift、applicability domain、OOD generalization | Yes | native literatureが既に明示 | Likely negative control |
| Lagrangian use | case-specific EFT / approximation / canonical or path-integral validity | Not yet | claim未特定 | Suspended |

---

## 14. Time-sliced audit design

historical benchmarkはhindsight biasに弱い。extension時点で利用可能だったinformation setを固定する。

### 14.1 Required design

1. post-outcome analysisを読む前にsource claim、target use、extension dateを定義する。
2. objectiveなbibliographic cutoffとcorpus construction ruleを事前に固定する。
3. later terminology、postmortem、outcome dataを両review armから除く。
4. contemporaneous standard、review、negative evidenceを含め、focal paperだけに絞らない。
5. field-native controlとstructured armが同じcorpusを独立に読む。
6. outcome開示・arm比較前に両reportをfreezeする。
7. claim identity、materiality、bridge adequacy、decision relevanceを独立field expertがadjudicateする。
8. adjudication後にlater historyを開示し、flagが後に認識されたissueへ対応したかscoreする。

### 14.2 Historical benchmarkが示せる範囲

then-available evidenceからprospectively expressibleなconcernを回復できたか、structured procedureがcontemporaneous-style judgmentを変えたかは検査できる。

未知caseへのprospective utilityは単独では示せない。historical caseはlater outcomeが既知だから選ばれやすい。Level 1を超えるには、少なくとも一つのgenuinely prospectiveまたはoutcome-blinded caseが要る。

### 14.3 Leakage controls

- cutoff後の語なら、“stationarity is dead”、“algorithm dynamics”、“racial bias”等のlabelをreviewerへ見せない。
- caseへのprior familiarityを記録する。
- 可能ならpost-cutoff outcomeを詳しく知らないreviewerを用い、またはoutcome knowledgeの効果を測る。
- search queryとeligible databaseを可能な範囲でfreezeする。
- excluded documentsと理由を記録する。

---

## 15. Preregistration template

実質分析前に以下を完成・freezeする。

### 15.1 Case identity

- Case title / domain:
- Source claim（可能ならexact wording）:
- Target claim / use:
- Source–target間で主張されるrelation:
- Extension date / documentary cutoff:
- New claimでなくextensionとする理由:

### 15.2 Corpus

- Eligible document types:
- Databases / search strings:
- Date range:
- Inclusion / exclusion criteria:
- 必須のfield-native standards / reviews / guidance:
- Inaccessible / proprietary documentの扱い:

### 15.3 Prespecified conditions and differences

- Candidate source warrant conditions（field-native terms）:
- Prespecified source–target differences:
- 各differenceのmateriality criterion:
- No material changeを示すevidence:
- Eligible field-native bridges:

### 15.4 Comparison design

- Field-native control reviewer qualifications:
- Structured reviewer qualifications:
- Blinding / information-symmetry plan:
- Freeze order:
- Expert adjudication procedure:
- Conflict of interest / prior familiarity:

### 15.5 Outcomes

- Primary diagnostic-difference outcome（uniqueまたはmore reproducible detectionを優先）:
- Scope / uncertainty / model / experiment / decision outcomes:
- Secondary time-to-detection measure（使用する場合）：elapsed time / documents read / retrieval count / first justified flag timestampのどれを使うか:
- Retrieval-completeness measure:
- False-positive definition:
- Inter-rater agreement measure:
- `unknown / unassessed`の扱い:

### 15.6 Fixed success and rejection rules

- Organizational valueに留まるresult:
- Provisional diagnostic procedureを支持するresult:
- Field-native sufficiencyを支持するresult:
- Termination / demotionを発動するresult:
- 許容するpost hoc analysis:

> **Freeze statement:** This preregistration must be timestamped and frozen before the substantive source–target analysis and before post-cutoff outcomes are disclosed to reviewers.

---

## 16. Kill criteria

決定的criterionを満たすか、累積証拠がthresholdへ達した場合、本programを終了またはreview/synthesisへ大幅降格する。

1. Parker型adequacy-for-purpose、VVUQ / context-of-use、applicability-domain、external-validity、distribution-shift等の既存方法がprotocol全体を同等以上の精度で再現する。
2. 3件以上のpreregistered caseでfield-native controlとの差がdiagnosis、scope、uncertainty、design、retrieval、decisionのいずれにも出ない。
3. candidate changeが当時のfield-native literatureですでに明示されていた。
4. artifact-level `silent`判定がfrozen corpusを読むanalyst間で再現しない。
5. source–target claim identityが恣意的なredescriptionに依存し、expert adjudicationに耐えない。
6. later outcome failureをreviewerへ知らせなければcandidateを検出できない。
7. ordinary parameter changeとmaterial changeをprospectivelyかつacceptable agreementで区別できない。
8. structured comparisonのfalse positiveがfield-native reviewより多く、preregistered benefitで相殺されない。
9. auditが追加measurement、experiment、uncertainty statement、scope restriction、model choice、decisionを一切変えない。
10. GST Case 01と同様、generic vocabularyを消す方が精密で、全judgmentが変わらない。
11. field-native expertが全materiality / bridge judgmentを与えなければ機能せず、checklist自体がretrieval、consistency、comparisonへ独立寄与しない。
12. positive-looking caseがすべてimplementation failure、known-standard noncompliance、already documented limitationへ還元される。
13. later failureの知識なしにcorpus selection / cutoffを規定できない。
14. 独立teamがpreregistered instructionからsource validation basis / target difference inventoryを再現できない。
15. 両armに同じcorpus、time budget、field-native guidanceを与えると見かけのbenefitが消える。

主要な累積停止規則は2と15である。suggestiveなhistorical example 1件ではnegative control 2件を覆せない。

---

## 17. Promotion criteria

### Level 0 — Review / synthesis only

現在地。prior art、failed hypotheses、candidate cases、empirical comparison planの整理に限る。diagnostic methodを主張しない。

### Level 1 — Provisional diagnostic procedure

少なくとも1件のpreregistered caseで、以下を全て満たす。

- frozen corpusからmaterialかつunstatedなsource–target changeを検出する。
- independent field-native controlと具体的差がある。
- claim identity、materiality、bridge absenceをindependent expertが支持する。
- measurement、experiment、scope、uncertainty、model、actionにdecision-relevant effectがある。
- unacceptableなfalse-positive増加がない。

historical benchmark単独ならprovisional evidence以下と明記する。

### Level 2 — Comparative diagnostic protocol

複数の独立領域で次を再現する。

- reproducible detection;
- acceptableかつprespecifiedなfalse-positive rate;
- field-native controlを上回るdiagnostic value;
- research design、scope、uncertainty、model choice、decisionの実変更;
- 別teamが実施できるprocedural stability.

Level 2でもgeneral framework / methodologyの主張は自動的に従わない。追加prior-art比較、external replication、既存validation / assurance practiceに対する優位性が必要である。

---

## 18. Open questions

1. **[OPEN: prior-art audit]** adequacy-for-purpose、validation-domain、transfer-learning、model-risk、evidence-auditに同じsource–target stepsとcontrol comparisonはないか。
2. **[OPEN: measurement]** primary performance metricはuniqueまたはmore reproducibleなmaterial findingを中心に固定できるか。time-to-detectionはsecondaryとし、elapsed time、documents read、retrieval count、first justified flagのどれが妥当かをcaseごとに事前指定する。compositeはpost hoc flexibilityを招く。
3. **[OPEN: claim identity]** cross-disciplinary claim ontologyを押しつけずsource/targetを比較できるか。
4. **[OPEN: materiality]** outcomeを知らずmaterialityを再現可能に判定できるか。
5. **[OPEN: bridge sufficiency]** robustness result、error bound、direct target validationが差を被覆する十分条件は何か。
6. **[OPEN: disclosure]** conditionが別文書参照で組み込まれる場合、adequate disclosureとは何か。
7. **[OPEN: institutions]** explicit standardがあるのにartifact omissionが反復する場合、workload、incentive、review、regulation、implementationをどう分けるか。
8. **[OPEN: sampling]** famous failureや都合のよいnarrativeだけを選ばないcase samplingは可能か。
9. **[OPEN: prospective test]** outcome未知のまま、安全上のdecisionへ介入せずauditできるcontemporary extensionは何か。
10. **[OPEN: expert dependence]** structured armの効果は、別専門性を持つsecond expertを追加した効果にすぎないのではないか。
11. **[OPEN: negative controls]** false-positive behavior測定のため、どのexplicitly licensed transitionを含めるか。
12. **[OPEN: Lagrangian candidate]** §13.5のentry requirementsを満たすspecific paper / target calculationはあるか。

---

## 19. Current ledger and immediate next experiment

### 19.1 Current ledger

| Item | Status | Evidence | Next action |
|---|---|---|---|
| `validation basis`のconceptual novelty | Not supported | adequacy-for-purpose、context of use、applicability、transportability、robustness、UQと強く重複 | New conceptとして売らない |
| Universal method / formalism | Withdrawn / not proposed | 旧theorem / map探索が失敗 | Scope外を維持 |
| Artifact-level omission | Coherent but untested | document/time-relativeに定義可能 | Preregistered comparisonで検査 |
| Institutional under-enforcement | Outside v0.1 | implementation / organizational evidenceが要る | A確立後に別design |
| Field-level conceptual absence | Unsupported | systematic field-wide auditなし | Caseから推論しない |
| GST generic audit | Frozen negative | field-native reconstructionが結論を保持し精密化 | Negative baseline |
| Metrology generic audit | Negative / organizational only | unique diagnosis / decision effectなし | Explicit-preservation control |
| Hydroclimatic stationarity | Candidate | later articulationは明確、prospective detectability不明 | Prior-art screen後にtime-slice preregistration |
| Google Flu Trends | Secondary candidate | later failure analysis、source model opacity | Corpus feasibility確認 |
| Pulse oximetry | A/B分離候補 | prior evidenceによりconceptual absenceは考えにくい | Specific document chain / cutoff特定 |
| Materials ML | Likely negative control | distribution-shift literatureが明示的 | Native-coverage control候補 |
| Lagrangian example | Not a case | specific claim sequenceなし | Entry requirementsまでsuspend |

### 19.2 Immediate next experiment

次は、preliminary prior-art feasibility screenを条件とする **preregistered, time-sliced hydroclimatic-stationarity benchmark** とする。

1. cutoffを決める前に、hydrology / water-planning literatureでnonstationarity concernがいつ明示化したかを調べる。有名な2008年論文の前年を機械的に“pre-recognition”としない。
2. “stationarity一般”でなく、長寿命infrastructure decisionでhistorical flow-frequency estimateを使う等、一つの具体的planning claimを選ぶ。
3. contemporaneous source corpus、target-use documents、standards/guidance、search protocolをfreezeする。
4. independent field-native reviewとstructured comparisonに同じevidence / time budgetを与える。
5. 追加findingがmaterial、unstated、existing bridgeで未被覆、decision-relevantかadjudicateする。
6. 先行field-native recognitionが見つかればgeneric procedureの確認でなくnegative resultと数える。

feasibility screenで差が既に明示されroutine reviewで検出可能ならnegative controlとする。head-to-headでdiagnostic deltaがなければ語彙を追加せず、failureを言い換えずにstopping ruleへ進む。

---

## 20. Termination status

### TERMINATION NOT YET RECOMMENDED — one narrow empirical question remains

conceptual programは既存研究に大部分が吸収される。継続理由はfield-native controlに対するincremental detectionの限定的経験テストだけである。null resultを避けるためにvocabularyやcaseを増やしてはならない。

preregistered benchmarkとconfirmatory casesがkill criteriaを満たせば、残すべき成果はexisting source–target validation practiceのreviewとnegative calibrationの履歴である。それは正当な成果だがmethodologyではない。

---

## 21. Relation to VED

本ノートはVEDから独立する。comparison rules、Erasure Test、negative controls、kill criteria、evidential standardsはVEDを含む任意のtheory/modelへ対称的に適用する。「より基礎的」「観測以前」を扱うという自己記述は、target、source warrant、scope、uncertainty、bridge、target evidenceを示す負担を軽減しない。

本working noteはVEDへの証拠的支持を一切与えない。

---

## 22. Selected prior art and case sources

以下はrouting bibliographyであり、systematic reviewではない。

### Purpose-, use-, and domain-relative validation

- Parker, W. S. (2020), [“Model Evaluation: An Adequacy-for-Purpose View”](https://www.cambridge.org/core/journals/philosophy-of-science/article/model-evaluation-an-adequacyforpurpose-view/CA91669E7CAC8BE4332A2B6D99BC9DB0), *Philosophy of Science* 87(3), 457–477.
- U.S. Food and Drug Administration (2023), [“Assessing the Credibility of Computational Modeling and Simulation in Medical Device Submissions”](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/assessing-credibility-computational-modeling-and-simulation-medical-device-submissions).
- National Research Council (2012), [*Assessing the Reliability of Complex Models: Mathematical and Statistical Foundations of Verification, Validation, and Uncertainty Quantification*](https://nap.nationalacademies.org/catalog/13395/assessing-the-reliability-of-complex-models-mathematical-and-statistical-foundations).
- Scovel, C. and Steinwart, I. (2013), [“Extrapolative Validation of Models”](https://arxiv.org/abs/1302.6427).
- OECD (2014), [*Guidance Document on the Validation of (Quantitative) Structure–Activity Relationship Models*](https://www.oecd.org/content/dam/oecd/en/publications/reports/2014/09/guidance-document-on-the-validation-of-quantitative-structure-activity-relationship-q-sar-models_g1ghcc68/9789264085442-en.pdf).

### External validity and transportability

- Pearl, J. and Bareinboim, E. (2011), [“Transportability of Causal and Statistical Relations: A Formal Approach”](https://ojs.aaai.org/index.php/AAAI/article/view/7861), *Proceedings of AAAI* 25(1), 247–254.
- Pearl, J. and Bareinboim, E. (2014), [“External Validity: From Do-Calculus to Transportability Across Populations”](https://arxiv.org/abs/1503.01603), *Statistical Science* 29(4), 579–595.

### Measurement uncertainty and traceability

- Joint Committee for Guides in Metrology, [JCGM publications: GUM and VIM](https://www.bipm.org/en/committees/jc/jcgm/publications).
- Completed control: [Metrology Case 02 comparison](./scientific_assurance_case_02_metrology_comparison.md).

### Historical and contemporary benchmark sources

- Milly, P. C. D. et al. (2008), [“Stationarity Is Dead: Whither Water Management?”](https://pubmed.ncbi.nlm.nih.gov/18239110/), *Science* 319(5863), 573–574.
- Ginsberg, J. et al. (2009), [“Detecting Influenza Epidemics Using Search Engine Query Data”](https://www.nature.com/articles/nature07634), *Nature* 457, 1012–1014.
- Lazer, D. et al. (2014), [“The Parable of Google Flu: Traps in Big Data Analysis”](https://www.networkscienceinstitute.org/publications/the-parable-of-google-flu-traps-in-big-data-analysis-2), *Science* 343, 1203–1205.
- Bickler, P. E., Feiner, J. R., and Severinghaus, J. W. (2005), [“Effects of Skin Pigmentation on Pulse Oximeter Accuracy at Low Saturation”](https://pubmed.ncbi.nlm.nih.gov/15791098/), *Anesthesiology* 102(4), 715–719.
- Sjoding, M. W. et al. (2020), [“Racial Bias in Pulse Oximetry Measurement”](https://pmc.ncbi.nlm.nih.gov/articles/PMC7808260/), *New England Journal of Medicine* 383, 2477–2478.
- Li, K., DeCost, B., Choudhary, K., Greenwood, M., and Hattrick-Simpers, J. (2023), [“A Critical Examination of Robustness and Generalizability of Machine Learning Prediction of Materials Properties”](https://www.nist.gov/publications/critical-examination-robustness-and-generalizability-machine-learning-prediction), *npj Computational Materials* 9.

### Internal correction trail

- [Tool-truth-absence working note v0.4](./tool_truth_absence_working_note_v0.4.md)
- [GST Case 01 v0.2 — frozen negative result](./deferred_resolution_case_01_gst_v0.2.md)
- [Metrology Case 02 — head-to-head comparison](./scientific_assurance_case_02_metrology_comparison.md)
- [Web of constraints — adversarial review record](./web_of_constraints_methodology_adversarial_review.md)

---

## v0.1 establishes

- **research program only**として、訂正履歴を保存した再スタート地点。
- artifact omission、institutional under-enforcement、field-level conceptual absenceのdocument-relativeな分離。
- 将来caseのためのfalsifiable entry rule、control comparison、Erasure Test、preregistration template、stopping criteria。
- GSTとmetrologyをsupportでなくnegative controlsとして保持すること。
- null resultを成功として受け入れ、終了可能な具体的next experiment。

## v0.1 does not establish

- 新概念、formalism、framework、methodology、universal classification。
- claim extensionにmaterialかつunstatedなchangeが存在または頻発すること。
- field-native reviewへの優位性。
- field-level blind spot、institutional failure、科学知識の一般限界、ontological nonuniqueness。
- Lagrangian formalism一般についてのclaim、またはVEDへの証拠的支持。

## next revision requires

- 一つのspecific source claim / target useについてfrozen preregistrationを作る。
- contemporaneous corpusとobjective cutoffを文書化する。
- 同じevidence/resourceを用いるindependent field-native reportとstructured-comparison reportを作る。
- claim identity、materiality、bridge adequacy、disclosure、decision relevanceをexpert adjudicateする。
- diagnostic differenceとfalse positiveを明示し、incremental valueがなければprogramを終了・降格する。

# Proof-Formation Independent Reader 01 — Coding v0.1

- **Reader:** 01
- **Status:** independent qualitative reconstruction
- **Read material:** `notes/theorem_proof_anatomy_experiment/02_proof_formation/proof_formation_coder_instructions_v0.1.md`; `notes/theorem_proof_anatomy_experiment/02_proof_formation/proof_formation_frozen_toy_corpus_v0.1.md`
- **Original-source access:** none; frozen corpusのexcerptだけを使用
- **Not consulted:** adjudication rules、meta-experiment、trajectory summary、answer key、他reader出力

## Coding convention under the supplied packet

coder instructionsから直接確認できたformation codeは、M1 = assumption strengthening、M2 = conclusion weakening、M3/M4 = scope restrictionである。ただしM3とM4の厳密な分担、およびその他のM-codeの定義は、許可された2ファイルには収録されていない。したがって、source wordingからmoveをplain-languageで再構成できても、番号を決められない場合は`M-code UNKNOWN`とした。source固有のMetrology `M1`、`S2*`、`A2`等はformation move codeとして扱わない。

# Episode coding

## E01 — Observation-map noninjectivity

```text
episode_id: E01
episode_boundary: [INFERENCE] 「存在論的非一意性定理」候補の提示から、prior-art/identity counterexample、撤回、model-relative remnantまでを一episodeとする。excerpt内にbefore/witness/afterが連続している。
claim_identity: AMBIGUOUS。revision episodeとしては連続するが、一般的新定理と、変更後の「識別可能性はモデルクラスと実験族に相対的」という区別は、同一結論の保持ではない。
claim_before: [SOURCE-DERIVED] 非単射な観測写像 O:W→L ではログから世界を一意復元できず、これを「観測写像の存在論的非一意性定理」として一般化できるのではないか。
target_and_scope: [SOURCE-DERIVED] 候補世界集合W、ログ空間L、観測写像O。初期targetは一般的な存在論的非一意性。変更後はmodel classとexperiment familyに相対的なidentifiability。
obligation_type: [INFERENCE] formal generalization、counterexample exclusion、既存identifiability/inverse-problemとの差。
assumptions: [SOURCE-DERIVED] O(w1)=O(w2)かつw1≠w2という非単射性。Oが非単射でなければならない条件は未提示。その他はUNKNOWN。
proof_or_evidence_resources: [SOURCE-DERIVED] O=id_Wという反例、inverse problems・identifiability・observational equivalence・quotient/fiberという既存設定への照合。個別文献とproof routeはUNKNOWN。
failure_witness: [SOURCE-DERIVED] O=id_Wが即時反例。非単射なら左逆がないという内容を越えず、既存設定に吸収される。
available_branches: [SOURCE-DERIVED] Oが非単射になる追加条件を別途示すこと。model classとexperiment familyを固定したidentifiability問題へ移ること。
move_taken: [SOURCE-DERIVED] 新しい一般定理としての主張を撤回し、model/experiment-relativeな区別だけを保持。[INFERENCE] M2とM3/M4の複数候補。withdrawalおよびprior-art absorptionのM-codeはUNKNOWN。
claim_after: [SOURCE-DERIVED] 観測同値類と採用した構造同型類を区別し、識別可能性をmodel classとexperiment familyに相対化する。
terminal_status: [SOURCE-DERIVED] 一般的新定理はwithdrawn。相対性の区別はestablished。
provenance_label: SOURCE-DERIVED = claim/witness/status/remnant。INFERENCE = episode grouping、obligation type、M-code assignment。OPEN HYPOTHESIS = Oを非単射にする条件の探索と読む場合のみ。
degenerate_or_target_leakage: 該当なし。[INFERENCE] 非単射性を結論として仮定するだけならcircularity riskがあるが、sourceはそれを成功扱いしていない。
uncertainties: M2とM3/M4のどちらをprimaryにするか。撤回・prior-art absorptionのcode定義がpacket内にない。
source_excerpts_used: E01 Excerpts 1–3。
```

## E02 — Self-containment impossibility and conditional capacity

```text
episode_id: E02
episode_boundary: AMBIGUOUS。(a) self-containment単独の普遍claimの撤回と、(b) 追加条件つき有限容量命題を別episodeに分けられる。ここでは一つの主episodeと一つのside branchとして記録する。
claim_identity: [SOURCE-DERIVED] sourceは条件付き容量命題を「自己包含定理」ではないと明記する。したがって普遍claimと条件付きclaimを同一claimとして扱わない。
claim_before: [SOURCE-DERIVED] 世界内部の観測者による、自己を含む世界の完全記述は一般に不可能ではないか。明示式では self-containment ⇒ universal non-identifiability。
target_and_scope: [SOURCE-DERIVED] 初期scopeは内部観測者一般。条件付きside claimは有限世界X=A×E、候補Ω=X、最終記録が真部分系Aに収まり、|E|>1である場合。
obligation_type: [INFERENCE] universal impossibility proof、counterexample exclusion。side claimではfinite-capacity conditional proof。
assumptions: [SOURCE-DERIVED] 初期claimではself-containment。side claimでは有限性、全初期状態を候補とすること、記録場所A、|E|>1。Breuer/Wolpert型結果には別の追加条件がある。
proof_or_evidence_resources: [SOURCE-DERIVED] finite internal encoder、無限集合の濃度、quine、Kleene recursion theoremがfailure evidence。容量命題のproof routeはexcerptに明示されずUNKNOWN。
failure_witness: [SOURCE-DERIVED] 十分な内部記憶を持つ有限encoderが自己状態を一意記録できる。無限集合と自己記述可能性もself-containment単独の含意を壊す。
available_branches: [SOURCE-DERIVED] 真部分系制限、全状態識別、固定出力意味論、query closure等を加える。有限容量命題を別claimとして保持する。候補縮小、環境記憶、外部ログ、無限集合は単純容量議論から外れる。
move_taken: [SOURCE-DERIVED] universal implicationをwithdrawnとし、self-containment単独では不可能性を生まないと固定。別の条件付き命題を保持。[INFERENCE] side claimにはM1とM3/M4。universal withdrawalのM-codeはUNKNOWN。
claim_after: [SOURCE-DERIVED] self-containmentは容量制約や対角化の前提を成立させることがあるが、それ単独では不可能性を生まない。有限・記録場所・候補範囲・容量を加えた別命題は残る。
terminal_status: [SOURCE-DERIVED] universal claim = withdrawn。否定的区別 = established。side claim = conditionally retained/provedと読めるが、excerptだけでproof statusの語は明示されずAMBIGUOUS。
provenance_label: SOURCE-DERIVED = explicit withdrawal、counterexamples、conditional statement。INFERENCE = 二episode構成、M1/M3/M4、side claimのproved判定。OPEN HYPOTHESIS = 追加条件一般の必要十分性は記載なし。
degenerate_or_target_leakage: actual sourceでは該当なし。side claimを元の「self-containment theorem」と再表示するならtarget leakage candidateだが、sourceは明示的に避けている。
uncertainties: conditional capacityをavailable branchとするか、実際に採用された独立claimとするかは両方読める。proof resourceがexcerptから確定しない。
source_excerpts_used: E02 Excerpts 1–4。
```

## E03 — Generation–log non-isomorphism

```text
episode_id: E03
episode_boundary: [INFERENCE] generic non-isomorphism claim、definitional/counterexample failure、withdrawal、specified-channel remnantを一episodeとする。
claim_identity: AMBIGUOUS。変更後は一般的non-isomorphism theoremではなく、個別channel/statisticについてlossを証明するobligationであり、同じclaimの単純な保存ではない。
claim_before: [SOURCE-DERIVED] generation→constraint formation→stabilization→logという段階があるため、生成構造と安定ログ空間の同型は一般に失われる。
target_and_scope: [SOURCE-DERIVED] generation structure、stable log space、一般のstabilization/recording process。変更後は具体的channel、statistic、dynamics、equivalence relation。
obligation_type: [INFERENCE] universal non-isomorphism/information-loss proof、定義からの独立性、reversible counterexample exclusion。
assumptions: [SOURCE-DERIVED] 初期claimの独立なassumptionsはUNKNOWN。「安定化=多対一」「記録=粗視化」と定義する案は結論を埋め込む。
proof_or_evidence_resources: [SOURCE-DERIVED] reversible process、complete encodingというcounterexamples。coarse graining、Blackwell comparison、sufficient statistics、bisimulation、minimal realizationによる既存の精密化。
failure_witness: [SOURCE-DERIVED] lossをdefinitionへ埋めるcircularity、可逆・完全符号化例、prior-art coverage。
available_branches: [SOURCE-DERIVED] 個別channel/statistic/dynamics/equivalence relationについてinformation lossを証明する。
move_taken: [SOURCE-DERIVED] generic claimをwithdrawnし、具体的対象ごとのproof obligationへ変更。[INFERENCE] scope restrictionとしてM3/M4、一般性の弱化と読むならM2。withdrawal/prior-art absorptionのM-codeはUNKNOWN。
claim_after: [SOURCE-DERIVED] information lossは仮定せず、具体的channel等について証明しなければならない。informational postprocessingとphysical joint measurementを区別する。
terminal_status: [SOURCE-DERIVED] universal claim = withdrawn。個別問題を立てる規則/区別 = established。個別loss theorem自体はopen/UNKNOWN。
provenance_label: SOURCE-DERIVED = before、failure、withdrawal、remnant。INFERENCE = M2/M3/M4とclaim identity。OPEN HYPOTHESIS = 個別channelで実際にloss theoremが得られるか。
degenerate_or_target_leakage: YES — 「stabilization」をmany-to-one、「recording」をcoarse grainingと定義してnon-isomorphismを得る案は、sourceが結論埋込みとして退ける。
uncertainties: afterをconclusion weakeningとするか、theorem questionからproof requirementへのnew claimとするか。
source_excerpts_used: E03 Excerpts 1–3。
```

## E04 — Pairwise separation versus a global adaptive separator

```text
episode_id: E04
episode_boundary: AMBIGUOUS。少なくとも(a) quantifier-order distinctionと、(b)その障害をinternality固有とする解釈の撤回がある。fresh preparation branchも同じepisode内にあるがactual moveとは分ける。
claim_identity: [SOURCE-DERIVED] pairwise/globalの差は残るが、二ビット例のinternality固有性は撤回される。したがって初期claimのどの部分をidentityとするかで結果が変わる。
claim_before: [SOURCE-DERIVED] 固定Ωで、各pairにseparatorがあることと、一つのadaptive historyで全pairを分離することは異なり、統合不能な系がありうる。
target_and_scope: [SOURCE-DERIVED] fixed candidate class Ω、pairwise experiments、一つのadaptive observation history。具体例は二ビット、単一copy、destructive operations。
obligation_type: [INFERENCE] quantifier-order separationのcounterexample、internal-observer specificity、既存adaptive-design prior artとの差。
assumptions: [SOURCE-DERIVED] fixed Ω。二ビット例ではsingle copy、destructive A/B、reset不能等。fresh preparationを許す場合は別interface condition。
proof_or_evidence_resources: [SOURCE-DERIVED] 二ビットdestructive example、同条件をexternal observerにも課すcounterexample、adaptive distinguishing sequence等の既存分野との照合。
failure_witness: [SOURCE-DERIVED] 障害はinternal observerに固有でなくexternalでも再現する。fresh preparationを許すと反例は消える。prior artも存在する。
available_branches: [SOURCE-DERIVED] fresh preparationを有限回許す。逐次合成、記録保存、common refinement、uniformity、error controlを設定ごとに調べる。
move_taken: [SOURCE-DERIVED] 二ビット例をinternalityそのものの不可能性例として使うことをwithdrawn。quantifier-order differenceをestablishedとして保持。[INFERENCE] internal-specific conclusionのM2、scope/type correctionのM3/M4も候補。withdrawal/prior-art moveの番号はUNKNOWN。fresh preparationはactual moveに数えない。
claim_after: [SOURCE-DERIVED] pairwise experimentabilityとsingle-policy global separationにはquantifier-order differenceがある。接続条件は「internality」でなくmodel-specific composition等に求める。
terminal_status: [SOURCE-DERIVED] internality-specific reading = withdrawn。quantifier distinction = established。必要十分条件 = synthesis/open。
provenance_label: SOURCE-DERIVED = example、failure、withdrawal、remnant、fresh-preparation possibility。INFERENCE = episode splitとM-code。OPEN HYPOTHESIS = 設定別必要十分条件。
degenerate_or_target_leakage: 該当なし。fresh preparationでinterfaceを変えて元のsingle-copy問題を「解決」と呼ぶならtarget changeだが、sourceは成功原因をfresh preparation/product条件に帰している。
uncertainties: initial hypothesisが量化差だけか、internality explanationまで含むか。M2とM3/M4の分担。
source_excerpts_used: E04 Excerpts 1–4。
```

## E05 — Internal/external interface correction

```text
episode_id: E05
episode_boundary: AMBIGUOUS。revision ledger上は一つのPhase 7 correctionだが、afterは(a) definitional/conventional equivalenceと、(b) conditional implementation lemmaの二branch。別episode化も可能。
claim_identity: [SOURCE-DERIVED] general established interface-equivalence claimはwithdrawn。二つのafter statementsは元の一般existence/equivalence claimと同一ではない。
claim_before: [SOURCE-DERIVED] internal/external controllersに同じinputs、outputs、memory、copies、reset、adversariality、causal interfaceを与えれば、generable history setsは一般に同じになるというestablished claim。
target_and_scope: [SOURCE-DERIVED] general internal/external observers。after(a)は完全なfeasibility interface Iを定義上同一にしたcontrollers。after(b)はdiscrete-time turn-based controlled transition systemとcommuting state mapを持つspecified model。
obligation_type: [INFERENCE] general equivalence/existence proof、definitionとimplementation theoremの分離。
assumptions: [SOURCE-DERIVED] beforeの「same interface」は内容不足。after(a)はtiming、concurrency、memory access/vulnerability、cost、self-readout、stochasticity、causal channels、reset/copy/fresh preparation、adversarial accessをIに含める。after(b)はturn-based dynamics、declared transitions/memory、explicit costs、action/transition/observationを保つstate map。
proof_or_evidence_resources: [SOURCE-DERIVED] after(b)のhistory-length induction。state mapはassumptionであってproof resourceではない。
failure_witness: [SOURCE-DERIVED] actual internal observerからexternal controllerへのexistence claimと、same history capacityを定義で与えるconventionの混同。
available_branches: [SOURCE-DERIVED] full interfaceを同一と定義するconventional result。specified transition modelでstate mapを仮定するconditional lemma。
move_taken: [SOURCE-DERIVED] general `[ESTABLISHED]`をwithdrawnし、二つのlimited statementsへ分離。[INFERENCE] conditional branchにはM1、model restrictionにはM3/M4、generalityのweakeningにはM2。withdrawal/type-splittingの番号はUNKNOWN。
claim_after: [SOURCE-DERIVED] definitional identityからhistory-set equalityは得られるがphysical implementation theoremではない。specified model内のconditional correspondenceも、現実のobserverにstate mapが存在することを保証しない。
terminal_status: [SOURCE-DERIVED] general claim = withdrawn。conventional result = definitional consequence。conditional model correspondence = conditional lemma。現実的implementation existence = not established。
provenance_label: SOURCE-DERIVED = diffのaccepted status、withdrawal、two branches、conditions。INFERENCE = episode splitting、M1/M2/M3/M4。OPEN HYPOTHESIS = 現実のobserverについてstate mapが存在するか。
degenerate_or_target_leakage: YES, candidate only — same transcript relationを定義に入れてhistory equalityを物理的同値定理として扱うならtarget leakage。sourceはこれを規約的帰結として明示し、一般theoremの救済にはしていない。
uncertainties: 二branchを`available_branches`とするか`move_taken`後のactual outputsとするか。規約的結果のterminal status用語。
source_excerpts_used: E05 Excerpts 1–4。
```

## E06 — GST Deferred Resolution revision

```text
episode_id: E06
episode_boundary: [SOURCE-DERIVED] v0.1 working positive caseからv0.2 frozen negative baselineへの明示的revision。個別GST technical stagesはこのpacketでは独立codingしない。
claim_identity: [SOURCE-DERIVED] Deferred Resolutionを独立mechanismとするclaimは撤回され、field-native reconstructionはその同一mechanism claimではない。
claim_before: [SOURCE-DERIVED] GST lineageのbest classificationはDR-1 weak relocationである。ただしquotient解決、historical sequencing、reviewer-imposed narrativeが強い読みを制限する。
target_and_scope: [SOURCE-DERIVED] standard QPTからself-consistent tomography/GST、gauge-free formulations、model extensionsへ至るlineageの共通mechanism。
obligation_type: [INFERENCE] recurrent mechanismのempirical/historical support、既存field-native terminologyを越える独立性・diagnostic contribution。
assumptions: [SOURCE-DERIVED] v0.1判定はNull C、Null D/Eにより制限される。詳細なmechanism assumptionsはexcerptからUNKNOWN。
proof_or_evidence_resources: [SOURCE-DERIVED] field-native reconstructionとrevision ledger。具体的review procedure、文献corpus、Erasure手順はexcerptからUNKNOWN。
failure_witness: [SOURCE-DERIVED] technical contentをconditional inverse problem、nuisance uncertainty、joint estimation、gauge quotient、model checking、model-specific extensionでより正確に再構成でき、独立mechanismを要しなかった。
available_branches: [SOURCE-DERIVED] actual revisionではDRをrejected historical working hypothesisへ降格し、field-native termsへrewriteした。[INFERENCE] DRを表示語として残す別branchがsourceに明示されたかはUNKNOWN。
move_taken: [SOURCE-DERIVED] positive case verdictをwithdrawn、DRをrejected historical working hypothesisへ降格、taxonomyを削除し、field-native termsへrewrite、frozen negative化。[INFERENCE] 対応するwithdrawal/prior-art/type-correction M-codeはpacket内でUNKNOWN。
claim_after: [SOURCE-DERIVED] hypothesized recurrent Deferred Resolution chainは支持されず、新mechanismを主張しない。technical distinctionsはfield-native termsで保持する。
terminal_status: [SOURCE-DERIVED] Frozen negative result / frozen negative baseline。
provenance_label: SOURCE-DERIVED = version relation、status、withdrawals、rewrite。INFERENCE = obligation typeとM-code欠如の評価。OPEN HYPOTHESIS = none in supplied excerpts。
degenerate_or_target_leakage: 該当なし。negative resultをvocabularyの成功に変換していない。
uncertainties: field-native reconstructionをprior-art absorptionと呼べるが、そのcodeとexact/partial strengthは許可資料だけでは決められない。
source_excerpts_used: E06 Excerpts 1–5。
```

## E07 — Metrology H1 to source-verdict M1

```text
episode_id: E07
episode_boundary: [SOURCE-DERIVED] preregistered H1からgeneric auditのhead-to-head resultとfinal M0–M3 source verdictまでを一episodeとする。
claim_identity: [SOURCE-DERIVED] H1「generic auditがnative controlより追加diagnosisを出す」と、source-local M1「organizational value only」は同一claimではない。後者はH1不支持後に残った別水準のvalue verdict。
claim_before: [SOURCE-DERIVED] generic transfer auditが、upstream scope/uncertainty/assumptions/referenceのloss/distortionを少なくとも一pathで発見し、field-native controlより明確または早期に見つける。
target_and_scope: [SOURCE-DERIVED] field-native metrology documentsとgeneric transfer auditの比較。具体的chain/corpusの範囲はsupplied excerptsからUNKNOWN。
obligation_type: [SOURCE-DERIVED/INFERENCE] preregistered empirical comparison。少なくとも一つのsuccess conditionが全applicable falsification conditionsを通過すること。
assumptions: [SOURCE-DERIVED] preregistered success/falsification conditionsとfield-native controlを比較基準にする。これらをclaim assumptionとevaluation ruleのどちらに置くかはAMBIGUOUS。
proof_or_evidence_resources: [SOURCE-DERIVED] frozen control corpus、generic audit、cross-chain display、head-to-head questions。個別documentsとprocedure detailsはUNKNOWN。
failure_witness: [SOURCE-DERIVED] new missing assumption、uncertainty component、scope judgment、decision、traceability break、source、remedyのいずれも得られず、judgmentは変わらなかった。
available_branches: [SOURCE-DERIVED] source-local M0というstricter classificationはdefensible。source-local M2/M3はcriteriaによりrejected。その他のnext experimentはexcerptにない。
move_taken: [SOURCE-DERIVED] H1をsupportせず、presentation/cross-chain visibilityだけをsource-local `M1 — Organizational value`として残す。[INFERENCE] conclusion weakening M2とも読めるが、H1 failureと別value claimへの移動なのでAMBIGUOUS。rejection/demotionのM-codeはUNKNOWN。formation M1は使わない。
claim_after: [SOURCE-DERIVED] generic auditはjudgmentを変えず、diagnostic/methodological added valueはdemonstratedされない。organizational valueのみ。
terminal_status: [SOURCE-DERIVED] H1 = not supported。source verdict = M1 organizational value; M0もdefensible、source-local M2/M3 rejected。
provenance_label: SOURCE-DERIVED = preregistered criterion、negative comparison、source-local verdict。INFERENCE = H1とorganizational claimのepisode relation、formation M2候補。OPEN HYPOTHESIS = none in excerpts。
degenerate_or_target_leakage: 該当なし。source-local `M1`をformation M1と読むことはlabel errorだがtarget leakageではない。
uncertainties: controlがassumptionかevidence resourceか。H1をM2で弱めたのか、failed H1の後に別value verdictを立てたのか。
source_excerpts_used: E07 Excerpts 1–4。
```

## E08 — Hydrology preservation to documentary continuity

```text
episode_id: E08
episode_boundary: [SOURCE-DERIVED] v0.1 current verdictからC-3 internal contradictionを経てv0.2 current verdictへ至るrevision episode。C-1/C-2はpacketにないため含めない。
claim_identity: [SOURCE-DERIVED] same documentary studyのrevisionだが、「保存機構は忘却を防いだ」というeffectiveness claimと「documentary continuity identified」は同一結論ではない。
claim_before: [SOURCE-DERIVED] B. Partial preservation history identified。保存機構は忘却を防いだが、解決やdownstreamへの完全伝達は保証しない。
target_and_scope: [SOURCE-DERIVED] 17B/17C等のdocumentary relationと、実際のreference/use/downstream transmission/forgetting prevention effect。詳細corpusはexcerptからUNKNOWN。
obligation_type: [INFERENCE] documentary evidenceからpreservation effectivenessを支持できるか、internal consistency、empirical effectiveness。
assumptions: UNKNOWN。document accessibilityからforgetting preventionへ進むbridgeはsource excerptでassumptionとして固定されていない。
proof_or_evidence_resources: [SOURCE-DERIVED] N-04「effectiveness unconfirmed」とv0.1/v0.2 verdict comparison。実際のsource documentsとreview procedureはUNKNOWN。
failure_witness: [SOURCE-DERIVED] 「保存機構は忘却を防いだ」がN-04「有効性は未確認」と内部矛盾。actual reference/use/effectを測定していない。
available_branches: [SOURCE-DERIVED] documentary rediscoverabilityだけを残す。effectivenessを将来測るbranchは推測になるためUNKNOWN。
move_taken: [SOURCE-DERIVED] contradictory effectiveness sentenceを削除し、verdictをdocumentary continuity identified / effectiveness untestedへ変更。[INFERENCE] M2。用語訂正に別codeがある可能性はあるがUNKNOWN。scope restriction M3/M4は主要moveではない。
claim_after: [SOURCE-DERIVED] documentary continuityはidentified。実際のuse、transmission、forgetting-prevention effectivenessはuntestedで、それ以上は言えない。
terminal_status: [SOURCE-DERIVED] corrected documentary result / comparative finding。effectiveness claim = withdrawn/untested。
provenance_label: SOURCE-DERIVED = before/after table、C-3、unmeasured effect。INFERENCE = M2とepisode grouping。OPEN HYPOTHESIS = effectivenessの将来testはsource excerptにないため付さない。
degenerate_or_target_leakage: 該当なし。documentary continuityをeffectivenessのproxyとして扱うとtarget leakageになりうるが、sourceは明示的に分離している。
uncertainties: “partial preservation history”自体のどの部分がwithdrawnでどの部分がcontinuityとして保持されたかはexact formal statementがない。
source_excerpts_used: E08 Excerpts 1–5。
```

## E09 — P0 to P1-reduced termination

```text
episode_id: E09
episode_boundary: AMBIGUOUS。少なくとも(a) P0で14-code programをNONEVAL one-code testへ縮小したtransitionと、(b) P1-reduced後にcomparative methodologyをterminateしたtransitionがある。明示dependencyがあるため二段episodeとして記録する。
claim_identity: [SOURCE-DERIVED] 14-code/full artifact-chain program、one-code search、terminated methodology/comparative reviewは同一claimのままではない。program lineageは連続する。
claim_before: [SOURCE-DERIVED] 14 codesを対象とするcomparative research programと、三分野の完全なartifact-chain reconstructionを進める計画。
target_and_scope: [SOURCE-DERIVED] 初期は14 codes/full P1–P5。P0後はNONEVALのみのGUM/VIM/GRADE search。最終はcomparative methodologyを終了しcomparative reviewへ。
obligation_type: [INFERENCE] comparative empirical discrimination、program viability、stop-rule application。
assumptions: [SOURCE-DERIVED] full programには比較すべきcodesが十分残るという前提があったが、P0が否定したとsourceが明記。その他はUNKNOWN。
proof_or_evidence_resources: [SOURCE-DERIVED] P0 result、NONEVAL search/P1-reduced result、predefined Part IX rule。具体的coding/dataはexcerptからUNKNOWN。
failure_witness: [SOURCE-DERIVED] 14 codes中、実質一codeのみが比較対象として残り一codeは保留。P0とP1-reducedによりfull planの前提が二段階で否定された。P1-reducedの個別negative evidenceはexcerptにない。
available_branches: [SOURCE-DERIVED] (i) NONEVAL-only search、(ii) RET-DOWN test、(iii) full P1–P5、(iv) termination。P0時点で(i) recommended、(iii) explicitly not chosen。
move_taken: [SOURCE-DERIVED] (i)へ縮小し、P1-reduced後はmethodologyをterminate、comparative reviewへdowngrade、full P1–P5へ進まない。[INFERENCE] one-code restrictionはM3/M4。program status weakeningにM2も候補。termination/downgradeのM-codeはUNKNOWN。
claim_after: [SOURCE-DERIVED] comparative methodologyとして終了し、comparative reviewへ降格。full three-field chain reconstructionは実施しない。
terminal_status: [SOURCE-DERIVED] terminate as comparative methodology / comparative review。
provenance_label: SOURCE-DERIVED = choices、selection、non-selection、final status。INFERENCE = two-stage episode、M2/M3/M4。OPEN HYPOTHESIS = RET-DOWN branchはavailableだったがactualではない。
degenerate_or_target_leakage: 該当なし。full planを惰性的に続けてsuccessを作ることをsourceが拒否している。
uncertainties: P1-reducedで何がsecond failure witnessだったかはexcerptだけではUNKNOWN。P0→P1rとP1r→terminationの境界。
source_excerpts_used: E09 Excerpts 1–6。
```

## E10 — Gödel “closure reversal” to C1

```text
episode_id: E10
episode_boundary: AMBIGUOUS。packetは(a) Gödel–Rosser Iのadopted theorem、(b) Gödel IIのmetatheoretic conclusion、(c) “closure reversal” vocabulary verdictを含む。少なくとも数学的theorem episodesとmeta-label evaluationを分けられる。
claim_identity: AMBIGUOUS。“closure reversal”のinitial exact claimはexcerptで完全に固定されていない。Gödel I/IIのstandard statementsとC1 label verdictは同一claimではない。
claim_before: [SOURCE-DERIVED] theorem-anatomy comparison vocabularyをGödel I/IIへ適用する。より強いcandidateとして何をC2/C3とする予定だったかはUNKNOWN。[INFERENCE] “closure reversal”が独立した分類として有効かを問うstress testと読む。
target_and_scope: [SOURCE-DERIVED] Gödel–Rosser I: Qを含むcomputably axiomatized classical first-order Tで、Tがconsistent。Gödel IIについてはexternal consistency assumptionからinternal sentenceのunprovabilityを導くmetatheoremというlevel distinction。meta targetは“closure reversal” vocabulary。
obligation_type: [INFERENCE] formal theorem statementのtyping、object/internal/metatheory distinction、独自classificationのdiagnostic adequacy。
assumptions: [SOURCE-DERIVED] Gödel–Rosser excerptではQ inclusion、computable axiomatization、classical first-order theory、consistency。Gödel IIの完全なassumption setはexcerptからUNKNOWN。
proof_or_evidence_resources: UNKNOWN。packetはtheorem statementsとverdictを示すが、diagonal lemma等のproof routeを示していない。
failure_witness: [SOURCE-DERIVED] “closure reversal”は標準概念よりdiagnostic resolutionが低く、Gödel mechanismのdiscovery/distinctionに使えず、standard analysis後のsummaryにしかならない。
available_branches: [SOURCE-DERIVED] C1 explanatory metaphorとしてのみ保持。C2/C3へは上げない。standard proof-theoretic terminologyで分析する。
move_taken: [SOURCE-DERIVED] 独立classificationとして昇格せずC1へ限定。[INFERENCE] label conclusionのweakeningとしてM2。scope correctionにM3/M4も候補。metalevel shift、prior-art/standard-vocabulary absorption、demotionのM-codeはUNKNOWN。
claim_after: [SOURCE-DERIVED] “closure reversal”は比較上の短いexplanatory labelに限り有効で、新しいproof-theoretic classificationではない。
terminal_status: [SOURCE-DERIVED] source verdict C1 — explanatory metaphor only。Gödel theorem statements自体はこのnegative verdictの対象ではない。
provenance_label: SOURCE-DERIVED = theorem statements、level statement、C1 verdict。INFERENCE = initial meta-claim reconstruction、three-way episode split、M2/M3/M4。OPEN HYPOTHESIS = none。
degenerate_or_target_leakage: 該当なし。
uncertainties: claim_beforeのexact strength、Gödel IとIIを同じepisodeへ含めるか、metalevel distinctionに割り当てるM-code、proof resources。
source_excerpts_used: E10 Excerpts 1–5。
```

## E11 — Reflection S2 to S2*

```text
episode_id: E11
episode_boundary: AMBIGUOUS。(a) “self-guarantee” labelのkill testと、(b) external reflection extension T→T+reflection、(c) same-T Löb comparisonが同じpacketにある。meta-label episodeを主とし、数学的extensionをembedded sub-transitionとする。
claim_identity: [SOURCE-DERIVED] broad self-guarantee across local/uniform/global/soundnessと、local-only S2*は同一scopeのclaimではない。same-T theoremhoodとexternal stronger theory constructionも別。
claim_before: [SOURCE-DERIVED] “self-guarantee”がsingle local reflectionで働いても、uniform/global/semantic soundnessまで含めるとtype/level differencesを隠すのではないか、というkill-test hypothesis。positive S2のexact prior statementはUNKNOWN。
target_and_scope: [SOURCE-DERIVED] theory T、formula class Γ、local/uniform/global reflection、semantic soundness、same-T Löb case、external extension T+Rfn/RFN/GRP。
obligation_type: [INFERENCE] scope/type comparison、same theoryとextensionの区別、meta-labelのrobustness。
assumptions: [SOURCE-DERIVED] Γはscope definition。extension strengthはscope、Γ、base、truth axiomsに依存する。各principleの完全なformal assumptionsはexcerptからUNKNOWN。
proof_or_evidence_resources: [SOURCE-DERIVED] Löbとのcomparisonがfailure/type evidenceとして使われる。extension construction自体のproof resourcesはUNKNOWN。
failure_witness: [SOURCE-DERIVED] broad labelがtype、language、metalevelの差を隠す。same Tがlocal reflectionをtheoremにする場合と、externalにold Tのreflectionを加える場合は異なる。
available_branches: [SOURCE-DERIVED] local reflectionに限りS2*を保持。各Γ/scopeごとにstronger theoryを明示して扱う。broad self-guaranteeは維持しない。
move_taken: [SOURCE-DERIVED] S2をfamily-wideに維持せず、local reflection限定のS2*へ。mathematical sub-transitionとしてexternal theory extensionを明示し、same-T caseと分離。[INFERENCE] M2とscope restriction M3/M4。theory extension/type correction/metalevel shiftのM-codeはpacket内でUNKNOWN。
claim_after: [SOURCE-DERIVED] self-guarantee labelはlocal reflectionでのみlimited use。uniform/global/soundnessまで広げると破綻。external additionはstronger theoryを作るがsame-T theoremではない。
terminal_status: [SOURCE-DERIVED] source verdict S2* — limited S2。broad family-wide readingはfailed/demoted。external extensionsはdefined constructionであり、このmeta verdictと同じterminal statusではない。
provenance_label: SOURCE-DERIVED = central hypothesis、Γ role、extension form、Löb distinction、S2*。INFERENCE = episode hierarchy、M2/M3/M4。OPEN HYPOTHESIS = none stated。
degenerate_or_target_leakage: 該当なし。T+reflectionがreflectionを証明することをsame-T self-proofと表示すればdegenerate riskだが、sourceは明示的に区別する。
uncertainties: external theory extensionをactual move_takenとするか、meta-label stress testのanalysis objectとするか。M3/M4の分担。positive S2 before-stateのexact statement。
source_excerpts_used: E11 Excerpts 1–5。
```

## E12 — Proof-theoretic ordinal scalar to fixed-package calibration

```text
episode_id: E12
episode_boundary: AMBIGUOUS。packetはuniversal-scalar否定、same-ordinal inference limits、S2* verdict、subject/metatheory A2 verdictを含む。scalar episodeとmetatheory episodeを分けることもできる。
claim_identity: AMBIGUOUS。universal scalar candidateのexact positive before-stateはexcerptに示されず、中心結論はすでに限定形で書かれている。limited fixed-package calibrationはuniversal strength claimと同一ではない。
claim_before: [INFERENCE] proof-theoretic ordinalがtheoryの全strengthを表すuniversal scalarである、またはsame ordinalから複数strength relationsが従う、というcandidateをstress-testしたと読む。[SOURCE-DERIVED] positive before wording自体はUNKNOWN。
target_and_scope: [SOURCE-DERIVED] theory T/U、ordinal notation、base/metatheory、formula class、reduction notion、natural theory familiesとstandard analysis package。比較対象としてtheorem set、interpretability、consistency、Π1 consequences、induction、reflection rank。
obligation_type: [INFERENCE] comparison/calibration claim、bridge theorem requirement、metatheoretic level distinction。
assumptions: [SOURCE-DERIVED] notation、base/metatheory、formula class、reduction notionの固定。natural theories/standard packageであること。個別bridge theoremのassumptionsはUNKNOWN。
proof_or_evidence_resources: [SOURCE-DERIVED] cut elimination、TI/WO、reflection、worm orderingを結ぶbridge theorems。calculus、ordinal notation、reduction theorem、well-foundednessを証明するmetatheoryは型が異なる。
failure_witness: [SOURCE-DERIVED] |T|=|U|からtheorem-set equality、mutual interpretability、same consistency、same Π1 consequences、same induction、same reflection rankはいずれも自動でない。additional conclusionsにはbridge theoremが必要。
available_branches: [SOURCE-DERIVED] natural theoriesとstandard analysis packageにscopeを限定し、bridge theoremsが結ぶcalibrationとして保持。additional relationを得るには個別bridge theoremが必要だが、実際に採用・証明したとは書かれていない。
move_taken: [SOURCE-DERIVED] universal scalarを否定し、fixed-package/natural-familyのrobust coordinateとしてS2*に限定。analyzed theoryとjustifying metatheoryをA2として分離。[INFERENCE] M2およびM3/M4。comparison/calibrationとmetalevel distinctionのM-codeはUNKNOWN。
claim_after: [SOURCE-DERIVED] proof-theoretic ordinalは比較方法を固定したnatural familyでは強いcalibrationだが、theoryの全strengthのuniversal scalarではない。same ordinalは採用calibration上のsame coordinateまでを直接述べる。
terminal_status: [SOURCE-DERIVED] source verdict S2* for ordinal scalar、A2 for subject/metatheory asymmetry。いずれもsource-local labels。
provenance_label: SOURCE-DERIVED = limited conclusion、negative entailments、S2* and A2 verdicts、dependencies。INFERENCE = positive before-claim reconstruction、episode split、M2/M3/M4。OPEN HYPOTHESIS = unspecified bridge theoremの存在/適用は確立済みとしない。
degenerate_or_target_leakage: 該当なし。同じordinalをsame theoryと再表示するならtarget conflationだが、sourceはそれを否定する。
uncertainties: exact claim_beforeがない。scope restrictionとconclusion weakeningのprimary relation。A2を別episodeにするか。comparison/metalevel moveの番号。
source_excerpts_used: E12 Excerpts 1–4。
```

# Reader 01 post-coding report

## 1. 最もcodingしやすかったepisode

**E08**。before verdict、内部矛盾C-3、after verdictが同じpacket内で明示され、主moveをM2として再構成しやすかった。documentary continuityとeffectivenessを同一視しないこともsource wordingだけで決められた。次点は、final statusが明示されたE06である。

## 2. 最も曖昧だったepisode

**E10**。Gödel Iのtheorem statement、Gödel IIのmetatheorem-level statement、“closure reversal”というmeta-vocabularyのC1 verdictが一つのpacketに入り、どれを`claim_before + witness + after`の中心とするかが一意でない。さらに“closure reversal”のexact positive before-claimがexcerptに固定されていない。E11とE12も、数学的operationとmeta-label evaluationが同居するため近い難しさがあった。

## 3. 既存M1–M17で表現しにくかった箇所

許可されたcoder instructionsはM1、M2、M3/M4の用途は示すが、M5–M17の定義とM3/M4の厳密な分担を掲載していない。そのため、次のplain-language movesは再構成できても番号をsourceだけから決定できなかった。

- withdrawal / frozen negative fixation
- prior-artまたはfield-native terminologyへのabsorption
- claim/typeのdisambiguation
- theory extension
- internal statementとmetalevel evaluationの分離
- empirical/comparative questionへの移行
- comparison/calibration

これは既存codesで本質的に表現不能という判定ではなく、**指定されたreader packetだけではcodebookを利用できない**という判定である。推測による番号付けはしなかった。

## 4. Sourceだけでは決められなかった境界

- E02: universal self-containment claimのwithdrawalとfinite-capacity side claimを一episodeにするか。
- E04: quantifier-order claimとinternality-specific interpretationを一つのclaim identityに含めるか。
- E05: conventional equivalenceとconditional implementation lemmaを二episodeに分けるか。
- E07: H1 failureとorganizational-value claimをconclusion weakeningで結ぶか、別claimとするか。
- E09: P0 narrowingとP1-reduced terminationを一episodeの二段階とするか。
- E10: Gödel I、Gödel II、meta-vocabulary verdictをどこで切るか。
- E11: external theory extensionをactual formation moveとするか、S2 label testのanalysis objectとするか。
- E12: universal scalarのpositive `claim_before`がsource excerptに存在しないため、stress-test targetをどこまで復元してよいか。

## 5. Coder instructions自体で分かりにくかった規則

1. M1–M17を使うよう要求する一方、許可された2ファイル内にfull codebookがない。
2. M3とM4のどちらがformula-class、object/model/corpus restrictionに対応するかが明示されていない。
3. 一つのfrozen episodeに複数のlogical episodeがある場合、submission blockを分割するか、一block内にsub-episodeを置くかが固定されていない。
4. explicitに“残った”conditional claimを`available_branches`へ置くか、実際の`claim_after`へ置くかの規則が弱い。
5. withdrawn main claimとestablished remnantが同居する場合、`terminal_status`を一つにするか複数にするかが未指定。
6. obligation type、assumption、evaluation ruleの境界が、formal theorem以外のempirical protocolでは十分に定義されていない。

## Closing note

本codingでは数値的な一致評価、ranking、新move、一般法則を導入していない。UNKNOWN/AMBIGUOUSは資料または境界規則の不足として保持し、source-local labelsをformation codesへ変換していない。

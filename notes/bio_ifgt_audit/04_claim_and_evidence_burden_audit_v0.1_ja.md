# Bio-IFGT claim / evidence burden audit v0.1

## 0. Status

- Bio-IFGT audit: **IN PROGRESS**
- Phase 00 dependency / inheritance: **COMPLETE**
- Phase 01 equation / symbol inventory: **COMPLETE**
- Phase 02 equation role / biological-role audit: **COMPLETE**
- Phase 03 preload / boundary / circularity audit: **COMPLETE**
- Phase 04 claim / evidence burden audit: **COMPLETE**
- Phase 05 simulation / empirical correspondence audit: **NOT STARTED**
- Upstream VED equation audit / core revision: **CLOSED / CLOSED**

Authorityは[README](README_ja.md)、[Phase 00](00_dependency_and_inheritance_record_v0.1_ja.md)、
[Phase 01](01_equation_and_symbol_inventory_v0.1_ja.md)、
[Phase 02](02_equation_role_and_biological_role_audit_v0.1_ja.md)、
[Phase 03](03_preload_boundary_and_circularity_audit_v0.1_ja.md)。
source identities、48 BIO-EQ、source/working/code差、preload、boundary、circularity分類を保持する。
本稿はclaim type・burdenと既存supportの照合であり、sourceのclaim強度の変更、revision disposition、
総合validity / empirical-validation verdictではない。

新規simulation、empirical comparison、外部web/literature本文の研究、source/PDF/figureの改訂なし。
既存PNGの目視は既存supportの確認であり新しいempirical evidenceではない。
PDFの式版はPhase 01 spot-checkを参照し、今回はdistribution全体の再監査を行わない。
CLM/EV/NG/GAPは監査索引であり理論notationではない。

### Source locators

S IDsはPhase 00を維持する。EN/JA manuscriptとworking MDを統合しない。

| ID | Source / locator |
|---|---|
| S02 | [self-contained JA manuscript](../../bio-ifgt/main_ja.tex) |
| S03–05 | [abstract](../../bio-ifgt/sections/abstract.tex)、[introduction](../../bio-ifgt/sections/introduction.tex)、[intuitive picture](../../bio-ifgt/sections/intuitive_picture.tex) |
| S06–07 | [formal mapping](../../bio-ifgt/sections/formal_mapping.tex)、[core equations](../../bio-ifgt/sections/core_equations.tex) |
| S08–09 | [gene events / DNA](../../bio-ifgt/sections/gene_information_flow.tex)、[morphogenesis](../../bio-ifgt/sections/development_morphogenesis.tex) |
| S10 | [life attractor](../../bio-ifgt/sections/life_attractor.tex) |
| S11–12 | [probability](../../bio-ifgt/sections/probability_revision.tex)、[second attractor](../../bio-ifgt/sections/intelligence_second_attractor.tex) |
| S13 | [relation to note](../../bio-ifgt/sections/relation_to_note.tex) |
| S14–15 | [toy model](../../bio-ifgt/sections/minimal_developmental_simulation.tex)、[results / captions](../../bio-ifgt/sections/simulation_results_visualization.tex) |
| S16–18 | [discussion](../../bio-ifgt/sections/discussion.tex)、[conclusion](../../bio-ifgt/sections/conclusion.tex)、[Bio README](../../bio-ifgt/README.md) |
| S19–20 | [JA working sections](../../bio-ifgt/sections_ja/)、[handoff](../../bio-ifgt/notes/handoff.md) |
| S21–22 | [simulate.py](../../bio-ifgt/simulations/minimal_neural_field/simulate.py)、[simulation README](../../bio-ifgt/simulations/minimal_neural_field/README.md) |
| S24/S26 | [tracked output directory](../../bio-ifgt/simulations/minimal_neural_field/outputs/)、[bibliography](../../bio-ifgt/refs.bib) |

## 1. Claim/evidence guards

以下はaudit guardsであり、個々のclaimへの肯定・否定の結論ではない。

\[
\text{definition}\neq\text{mechanism}
\]
\[
\text{formal construction}\neq\text{biological emergence}
\]
\[
\text{simulation witness}\neq\text{empirical validation}
\]
\[
\text{structural resemblance}\neq\text{mechanistic correspondence}
\]
\[
\text{model robustness}\neq\text{biological robustness}
\]
\[
\text{region definition}\neq\text{life identification evidence}
\]
\[
\text{preload-compatible output}\neq\text{spontaneous emergence}
\]
\[
\text{cross-layer analogy}\neq\text{cross-layer identity}
\]
\[
\text{source-local support}\neq\text{universal claim support}
\]

definitionのburdenが満たされてもbiological identityのburdenまで満たしたとはしない。
逆に、stronger burdenを満たすmap/testが見つからないことは、定義・代数・finite witnessを消さない。
Phase 03のpreloadやinterpretive loopからevidence不足/falseを自動推論せず、sourceとsupportを改めて照合する。
上流8 bridge relationsのOPENを成立済みのBio supportへ変更しない。

## 2. Claim vocabulary / evidence vocabulary

### Claim types

DEFINITION CLAIM; FORMAL CONSTRUCTION CLAIM; MODEL-LOCAL DYNAMICAL CLAIM; MECHANISM CLAIM; BIOLOGICAL IDENTIFICATION CLAIM; EMERGENCE CLAIM; ROBUSTNESS / STABILITY CLAIM; OBSERVATIONAL CLAIM; EMPIRICAL CLAIM; UNIVERSALITY CLAIM; CROSS-SCALE CLAIM; CORRESPONDENCE CLAIM; CAUSAL CLAIM; PROBABILITY CLAIM; NECESSITY CLAIM; SUFFICIENCY CLAIM; FORWARD / RESEARCH-TARGET CLAIM; CLAIM TYPE UNRESOLVED.

複数typeは併記する。MECHANISM / CAUSALはsourceの説明文法であり、機構成立の承認ではない。
OBSERVATIONALには数値出力と生物学的観測対象への言及を含み、scopeで区別する。
EMPIRICAL CLAIMは、この監査では外部生物データ・実験・測定との一致/検証を実績として述べるclaimを数える。
一般的生物学的背景やtestableな解釈をすべてempirical-validation claimとして数えない。
この狭い集計では0件だが、observed morphologyや生物学的robustnessの主張が無いという意味ではない。

### Evidence categories

DEFINITIONAL SUPPORT; ALGEBRAIC SUPPORT; SOURCE-LOCAL FORMAL SUPPORT; FINITE SIMULATION WITNESS; PARAMETERIZED TOY-MODEL WITNESS; VISUAL / DIAGNOSTIC OUTPUT; INTERNAL CONSISTENCY / ROLE SUPPORT; STRUCTURAL ANALOGY; LITERATURE BACKGROUND ONLY; EXTERNAL EMPIRICAL DATA; DIRECT BIOLOGICAL MEASUREMENT; CROSS-MODEL REPLICATION; PARAMETER ROBUSTNESS TEST; INTERVENTION / ABLATION; PREDICTION / HELD-OUT TEST; OPERATIONAL MAPPING; STABILITY / EXISTENCE PROOF; CONTINUUM / COARSE-GRAINING BRIDGE; EVIDENCE NOT LOCATED.

以下のEV索引は**今回locateしたsupportだけ**を指す。
既存finite run reportと図は今回再現したrunではなく、source-reported witnessとして扱う。

| Evidence ID | Located support category | Actual repository item | Scope / provenance limit |
|---|---|---|---|
| EV-01 | DEFINITIONAL SUPPORT | S06/S07/S08/S10/S11/S12のsource-local定義、命名、subset/event設定 | definitionが書かれていること。実体の同定ではない |
| EV-02 | ALGEBRAIC SUPPORT | S07 sign example / gradient relation、S21 gradient/normalizationの明示処理 | 指定形式内の関係のみ。新proofは作らない |
| EV-03 | SOURCE-LOCAL FORMAL SUPPORT | BIO-EQ-01–35、paper equations / signatures / constraints | generic functional未指定、working差を保持 |
| EV-04 | SOURCE-LOCAL FORMAL SUPPORT | S21 executable update / source / gate / boundary / diagnostics | read-only code確認。実行結果やpaperとの完全同値性そのものではない |
| EV-05 | FINITE SIMULATION WITNESS; PARAMETERIZED TOY-MODEL WITNESS | S15 numerical run report + tracked7PNGに対応するtoy model | 一つのmodel familyの既存報告。run manifest / 再現性全般はPhase 05の問い |
| EV-06 | VISUAL / DIAGNOSTIC OUTPUT | tracked7PNG、S21 mean/max/mask/plot処理 | N/B/Eのcurrent PNGを今回目視、他4件の所在/用途は00–01。生物測定ではない |
| EV-07 | STRUCTURAL ANALOGY | S04/S08/S10/S12/S13/S14とdownstreamのcorrespondence prose | resemblance / role再使用。typed translationや機構実証ではない |
| EV-08 | INTERNAL CONSISTENCY / ROLE SUPPORT | 非同一注記、toy限定、future-work表明、source/input関係、Phase 01–03のrole/identity trace | 該当scopeの文言/構成のみ。全Bio整合の承認ではない |
| EV-09 | LITERATURE BACKGROUND ONLY | S04/S09の一般的生物背景、S26の8 bibliography metadata | 個別claimへの文献本文照合はしていない。mainにbibliography呼出未locate、外部文献の支持を認定しない |

EXTERNAL EMPIRICAL DATA / DIRECT BIOLOGICAL MEASUREMENT / CROSS-MODEL REPLICATION /
PARAMETER ROBUSTNESS TEST / INTERVENTION / ABLATION / PREDICTION / HELD-OUT TEST /
OPERATIONAL MAPPING（生物的測定map）/ STABILITY / EXISTENCE PROOF /
CONTINUUM / COARSE-GRAINING BRIDGEを該当claimのsupportとしてlocateしなかった。
これらはEVとして加算しない。CLI modeやno-eye switchの存在だけではablation実績ではなく、
initial random perturbationはpost-formation robustness protocolではない。
codeからarrayへの操作定義はあるがbiological OPERATIONAL MAPPINGには分類しない。

### Burden status and granularity

YES = 表のscopeに限定したburdenを現在のsource/supportが満たす。
PARTIAL = そのreadingに必要な部品の一部があるが、記載した追加burdenが残る。
NO = 表で判定対象としたstronger readingの必須map/test/resultがlocateされない。
NOでも同じ対象の定義・類比等はsupport欄に残す。
UNRESOLVED = version / target / relationの意味が固定できずburdenを一意判定できない。
NOT APPLICABLE = future work / scope exclusionであり、現在の達成claimへのburden判定ではない。
いずれもBio全体のvalidity、empirical-validation判定、revision actionではない。

burdenはclaimに応じて選ぶ。定義に外部datasetを要求せず、有限patternに普遍定理を要求しない。
mechanismには対応量/介入、biological identityには独立同定、universalityにはscope/scale条件を問う。
安定性の検証経路もclaim次第でproofまたはspecified model testを区別し、全burdenを一律に課さない。

## 3. Claim inventory

56families。definition / model / biological読みを別行にし、重複repriseはsource traceへ束ねた。
supportのEVは§2の実物・categoryを参照する。未実施の新実験を存在するsupportとして加えない。
tableのscopeは判定対象の切り出しであり、source文を修正・弱化したものではない。

| Claim ID | Source | Current wording / paraphrase | Claim type | Scope | Current support | Required burden | Burden currently met? |
|---|---|---|---|---|---|---|---|
| CLM-01 | S03/S16:7–15,41; S17 | minimal common description、new biological mechanismを導入しない | FORMAL CONSTRUCTION CLAIM | 共通記述の提示。全biology説明の十分性でない | EV-03, EV-08 | 変数・式・source scopeの明示 | YES |
| CLM-02 | S04:15; S06:11–15 | Iはwindow-local structure / constraint / retained bias | DEFINITION CLAIM | 用語・state variableの定義 | EV-01 | explicit definition、source-local domain | YES |
| CLM-03 | S09:13–17; S06; BI-01 | morphogen profile / differentiationをIとして表す | BIOLOGICAL IDENTIFICATION CLAIM; CORRESPONDENCE CLAIM | 生物量との対応。単一observableのidentityは別 | EV-01, EV-07 | property選択・typed measurement map・units/scale calibration | PARTIAL |
| CLM-04 | S06:19–43; S07:28–33 | Jはstate-change current、diffusion+induced成分 | DEFINITION CLAIM; FORMAL CONSTRUCTION CLAIM | 与えたfield表現内のcurrent構成 | EV-01, EV-03 | domain/signature・constituent relation | YES |
| CLM-05 | S08:21–33; ML-07 | gene eventsのaggregateがcontinuous Jを生成 | MECHANISM CLAIM; CROSS-SCALE CLAIM; CAUSAL CLAIM | 離散gene event→biological currentという機構読み | EV-03, EV-07 | event-to-current averaging/typing・flux calibration・event intervention | NO |
| CLM-06 | S07:37–53 | Phi[I]を選ぶとgradient bias、Phi例の方向が決まる | FORMAL CONSTRUCTION CLAIM | sign/functionalを選んだ条件内のみ | EV-01, EV-02, EV-03 | functional choice・differentiable representation・指定例のalgebra | YES |
| CLM-07 | S08:45; S09:40; S14:110–113 | potentialがstable regionへのreturn / differentiation biasを説明 | MECHANISM CLAIM; CAUSAL CLAIM | biological response解釈。codeの独立Phi/Jとはしない | EV-03, EV-07 | 具体Phi/response・basinとの関係・mechanism-specific intervention | PARTIAL |
| CLM-08 | S07:19–24; BIO-EQ-08 | sigmaはbalanceのlocal generation source | DEFINITION CLAIM; FORMAL CONSTRUCTION CLAIM | source-term role、unconditional conservationでない | EV-01, EV-03 | balance/domain/source slotの明示 | YES |
| CLM-09 | S08:33; S09:26 | sigmaはgene-related production / theta依存source | BIOLOGICAL IDENTIFICATION CLAIM; MECHANISM CLAIM | 生物的生成との対応を読んだ場合 | EV-01, EV-03, EV-07 | independent source function・measurement / gene-event map | NO |
| CLM-10 | S06:47–51; S10:21–25 | tauはtに対する内部progressのaccumulation | DEFINITION CLAIM | interpretive definition relative to t | EV-01 | source-local rho signatureとt/tauの区別 | YES |
| CLM-11 | S16:27 | precise operational tau definitionは本稿範囲外 | FORWARD / RESEARCH-TARGET CLAIM | 将来のbiological clock同定、現在の成功claimでない | EV-08 | 実現claimならtemporal calibration・observable map。今回は未主張 | NOT APPLICABLE |
| CLM-12 | S08:7–23,49–53 | DNAをsequence / theta(s)、eventsをDelta I、反応をthresholdで表す | DEFINITION CLAIM; FORMAL CONSTRUCTION CLAIM | representationとparameter/threshold slotの提示 | EV-01, EV-03 | alphabet・signature・threshold relationの明示 | YES |
| CLM-13 | S08:53,57; S16:31 | DNA parametersがdevelopmental thresholds / branchingを拘束 | MECHANISM CLAIM; CAUSAL CLAIM | 具体genotype→parameter→outcomeの機構読み | EV-03, EV-07 | explicit theta(s)・parameter provenance・gene perturbation/prediction | NO |
| CLM-14 | S08:69 | theta/DNAはhistorically stabilized quasi-closure constraints | CORRESPONDENCE CLAIM; CROSS-SCALE CLAIM | originのinterpretation、具体起源をderiveしないと併記 | EV-07 | history/selection process・cross-layer map、organism-specific provenance | PARTIAL |
| CLM-15 | S09:21–28 | morphogen dynamicsのstandard coarse reaction–diffusion component | FORMAL CONSTRUCTION CLAIM | PDE形式の採用、empirical species identityでない | EV-03 | state/domain/source/coefficientsのsymbolic指定 | YES |
| CLM-16 | S09:44–53 | Iのinterval thresholdsでA/B/Cに分類 | FORMAL CONSTRUCTION CLAIM | model classification ruleのみ | EV-01, EV-03 | ordered intervals / labels | YES |
| CLM-17 | S08:57; S09:53–57 | stable configurationsがobserved cell fate / morphology | BIOLOGICAL IDENTIFICATION CLAIM; OBSERVATIONAL CLAIM | 観測対象との同定。単なるA/B/C定義とは分離 | EV-01, EV-03, EV-07 | independent morphology criterion・measurement map・matched biological data | NO |
| CLM-18 | S09:57,65; S04:9 | morphogenesisはdynamical convergenceの結果として説明 | MECHANISM CLAIM; EMERGENCE CLAIM; CAUSAL CLAIM | 生物学的説明。formal/toy subclaimsと分離 | EV-03, EV-07 | 具体dynamics・convergence・observable mapping・mechanism intervention / alternative comparison | PARTIAL |
| CLM-19 | S07:69; S10:37 | remain / returnするregionをstable / attractorと呼ぶ | DEFINITION CLAIM; ROBUSTNESS / STABILITY CLAIM | propertyの条件付命名、特定系の安定性証明でない | EV-01 | return条件と命名の明示 | YES |
| CLM-20 | S09:61; S10:47,55; S19 life §7.8 | biological robustness / reproducibility follows from attractor structure | MECHANISM CLAIM; ROBUSTNESS / STABILITY CLAIM; CAUSAL CLAIM | 生物学的return説明、generic criterionから分離 | EV-01, EV-07 | independent region criterion・perturbation protocol・convergence/robustness test・biological mapping | NO |
| CLM-21 | S10:55; S19 life §7.8 | regenerationはlarger disturbance後のattractor reconstruction | CORRESPONDENCE CLAIM; ROBUSTNESS / STABILITY CLAIM | conceptual biological interpretation、独立recovery runとは別 | EV-07 | reconstruction rule・disturbance protocol・recovery criterion、mechanismならintervention/data | PARTIAL |
| CLM-22 | S10:27–37 | lifeをbounded sustained viable / returning regionとして定義 | DEFINITION CLAIM | lifeというmodel terminologyの定義のみ | EV-01 | criteriaと命名の明示 | YES |
| CLM-23 | S10:29,43,59 | そのsustained regionをbiological lifeと同定 | BIOLOGICAL IDENTIFICATION CLAIM | definitionから独立のlife identification | EV-01, EV-07 | independent life/viability criterion・boundary/observable mapping | NO |
| CLM-24 | S07:57,80; S10:39 | sustained / life regionは相互作用からformed、not externally imposed | MODEL-LOCAL DYNAMICAL CLAIM; EMERGENCE CLAIM; ROBUSTNESS / STABILITY CLAIM | generic field/state dynamicsでのregion成立。toy gridと別 | EV-03, EV-07 | explicit functional/dynamics・region construction・existence/convergence・imposed inputsとの区別 | PARTIAL |
| CLM-25 | S10:43; S16:19–23 | matter/energy exchangeとupdateの下でorganizationが維持 | MECHANISM CLAIM; CORRESPONDENCE CLAIM | biological non-equilibrium maintenanceの説明 | EV-07 | exchange/state/boundary specification・maintenance criterion・mechanism/data対応 | PARTIAL |
| CLM-26 | S11:19–37 | life probabilityをregion-entry / persistenceというtargetへ再定義 | DEFINITION CLAIM; PROBABILITY CLAIM | event reformulation、no numerical reassessment | EV-01 | 数えるtargetの明示・quantitative claimとの分離 | YES |
| CLM-27 | S11:29–31 | fewer effective variablesによりprobability問題のdimensional structureが変化 | FORMAL CONSTRUCTION CLAIM; PROBABILITY CLAIM | formal reductionの説明、数値確率推定ではない | EV-01, EV-07 | original/reduced domains・projection・preserved event/measureの指定 | PARTIAL |
| CLM-28 | S12:17–21 | Omega_intel subset Omega_life + additional constraints | FORMAL CONSTRUCTION CLAIM | 宣言されたset relation / conceptual architecture | EV-01, EV-03 | subset relationと追加条件の記載 | YES |
| CLM-29 | S12:11–13,21,33–45; S19 intelligence §9.3 | history retention/reference/reuse/shareからsecond attractorとしてintelligenceを解釈 | EMERGENCE CLAIM; CORRESPONDENCE CLAIM; FORWARD / RESEARCH-TARGET CLAIM; NECESSITY CLAIM | Bio-local forward model。inevitableとはしない | EV-01, EV-07 | history dynamics・membership / cognitive map・stability、必要十分ならcounterexample/ablation | PARTIAL |
| CLM-30 | S12:25–29; S02 probability | P_intelのconditional two-stage factorization | FORMAL CONSTRUCTION CLAIM; PROBABILITY CLAIM | schematic、not numerical estimate | EV-01, EV-03 | conditioning targetとtwo-stage readingの表示 | YES |
| CLM-31 | S19 intelligence §9.4; Phase 01 CF-01 | working P_life×P_lifeとmanuscript conditional factorの異同 | PROBABILITY CLAIM; CLAIM TYPE UNRESOLVED | working-sourceの意図未固定 | EV-03 | source/version intent、second factorのevent identity | UNRESOLVED |
| CLM-32 | S14:101,119; S15:99–113; S24 | constrained toyでstructured spatial patternsの可能性をillustrate | MODEL-LOCAL DYNAMICAL CLAIM; EMERGENCE CLAIM | 有限報告runのstructural possibility、biology機構でない | EV-04, EV-05, EV-06 | 既存constructionと有限出力。再現性/parameter-generalizationは追加burden | YES |
| CLM-33 | S14:25–30; S21 run_simulation | source/diffusion/decayを与えMを更新 | FORMAL CONSTRUCTION CLAIM; MODEL-LOCAL DYNAMICAL CLAIM | finite implementation、continuous exact solutionでない | EV-03, EV-04 | source profile・initial/boundary・updateの表示 | YES |
| CLM-34 | S14:33–38; S21 run_simulation | MからIがaccumulate/diffuse/decay | FORMAL CONSTRUCTION CLAIM; MODEL-LOCAL DYNAMICAL CLAIM | new M入力のcode依存に限定 | EV-03, EV-04 | coupling / update order / coefficients | YES |
| CLM-35 | S14:41–46; S22; S24 N | I thresholdでcentral neural-plate-like Nが現れる | MODEL-LOCAL DYNAMICAL CLAIM; EMERGENCE CLAIM | neuralというtoy label、observed neural tissueでない | EV-03, EV-04, EV-05, EV-06 | source/threshold/ruleと有限pattern、biological同定には別map | YES |
| CLM-36 | S14:49–53; S21 gradient_magnitude | raw Gとnormalized G_normを構成 | FORMAL CONSTRUCTION CLAIM | code返値とpaper raw quantityを区別 | EV-02, EV-03, EV-04 | gradient / normalization / denominatorの表示 | YES |
| CLM-37 | S14:54–59; S21 run_simulation | G_norm入力のthresholded B accumulation | FORMAL CONSTRUCTION CLAIM; MODEL-LOCAL DYNAMICAL CLAIM | finite model operation、Nが直接入力ではない | EV-03, EV-04 | actual input・rates・clipping・update | YES |
| CLM-38 | S14:53; S15:18,57 | Bをboundary-like / boundary stabilizationと読む | CORRESPONDENCE CLAIM; BIOLOGICAL IDENTIFICATION CLAIM | gradient-sensitive model interpretation、membraneは未主張 | EV-04, EV-06, EV-07 | boundaryのoperational criterion・raw/normalized/accumulated区別、biologyならindependent boundary map | PARTIAL |
| CLM-39 | S14:62–68; S21 make_eye_window/run_simulation | N/B/positional gateがE localizationを制約 | FORMAL CONSTRUCTION CLAIM; MODEL-LOCAL DYNAMICAL CLAIM | smooth weight下のfinite E update | EV-03, EV-04 | gate / prior positional preference / updated inputs | YES |
| CLM-40 | S22 Toy Eye; S15:25,64; S24 E | 中央windowとboundary入力からpaired eye-spot-like pattern | MODEL-LOCAL DYNAMICAL CLAIM; OBSERVATIONAL CLAIM | reported outputの左右二つのlobe、real eye identityでない | EV-04, EV-05, EV-06 | 有限patternの所在とimposed windowの明示 | YES |
| CLM-41 | S14:5,76,101; S15:9,21,104; S02:473 | completed final shapeはencodeしない / geometryを明示しない | FORMAL CONSTRUCTION CLAIM; EMERGENCE CLAIM | completed drawing非入力とspatial information非入力を区別 | EV-04, EV-08 | input/output information separation、location-free読みにはwindow/source sensitivity・counterfactual | PARTIAL |
| CLM-42 | S14:87–96; S15:92–95 | M→I→N→B→E generation path / ordering | EMERGENCE CLAIM; CLAIM TYPE UNRESOLVED | paper summary。11edge roles / code branchと照合 | EV-03, EV-04, EV-06 | edge typing、orderとcausal dependencyの区別、VR-11/12の対象確定 | UNRESOLVED |
| CLM-43 | S14:107–115 | toy field / stagesをPhi/J・successive quasi-closure・sub-attractorへ対応 | CORRESPONDENCE CLAIM; CROSS-SCALE CLAIM | interpretation、code直接Phi/J integrationでない | EV-07 | field/state map・quasi-closure/attractor criterion・dependency translation | PARTIAL |
| CLM-44 | S15 Observations; S21 print_summary/plotting | simulation observations / mean/max/fraction / contours | OBSERVATIONAL CLAIM; MODEL-LOCAL DYNAMICAL CLAIM | numerical observation。empirical measurementでない | EV-04, EV-05, EV-06 | array/diagnostic/plot ruleの所在 | YES |
| CLM-45 | S14:101,113; S15:25,107 | final toy patternはstable solution / attractor-like | ROBUSTNESS / STABILITY CLAIM; MODEL-LOCAL DYNAMICAL CLAIM | finite final imageから長時間安定性へ拡張する読みを区別 | EV-04, EV-05, EV-06 | time-series criterion・post-formation perturbation・longer-run / stability test | PARTIAL |
| CLM-46 | S08:59–61; S17:5 | molecular/cellular/tissue scalesでsame formal structure / roles | UNIVERSALITY CLAIM; CROSS-SCALE CLAIM | 形式の再使用とscale-invariant biological relationを区別 | EV-03, EV-07 | scale-translation map / invariance条件、複数level/modelでの対応 | PARTIAL |
| CLM-47 | S04:15; S11:37; S16:23 | BioはIFGTのquasi-closure / non-closureにcorrespond | CORRESPONDENCE CLAIM; CROSS-SCALE CLAIM | source-local Bio I非同一注記を保持 | EV-07, EV-08 | cross-layer bridge / carrier & observable translation | PARTIAL |
| CLM-48 | S13:14–20,44; U15 | L3 paperとL1 noteはsame structure、direct translationではない | CORRESPONDENCE CLAIM | 具体note targetの版/path未固定 | EV-07 | paired source locatorと対応scope、typed identityなら別map | UNRESOLVED |
| CLM-49 | S16:31–37; S17:9; AT-15 | concrete I/J/Phi、theta、attractor / intelligence実装はfuture work | FORWARD / RESEARCH-TARGET CLAIM | 完了claimではない | EV-08 | 将来resultに応じてburdenを指定。現在の達成判定対象でない | NOT APPLICABLE |
| CLM-50 | DOWN-01 / S31 SSO:9–23 | Bio simulationでfast/slow spontaneous differentiation confirmed、necessarily | OBSERVATIONAL CLAIM; NECESSITY CLAIM; UNIVERSALITY CLAIM; CAUSAL CLAIM | 下流によるBioへのattribution、下流理論自体は未監査 | EV-05, EV-07 | 専用fast/slow criterion / output・necessity argument・alternative/rate analysis | NO |
| CLM-51 | DOWN-05 / II inference:21–29 | same F glyphはsame dynamics / cross-layer continuityの証拠 | CORRESPONDENCE CLAIM; CROSS-SCALE CLAIM; UNIVERSALITY CLAIM | Bioから下流へ継承したidentityという読み | EV-07 | typed map / preserved dynamics、同notationとは独立の対応 | NO |
| CLM-52 | DOWN-06 / II stopping:67,106 | L_R / L_EはBio second-attractorの内部記述 / same structure | CORRESPONDENCE CLAIM; CROSS-SCALE CLAIM | additional conditions引用とidentity assertionを分離 | EV-01, EV-07 | Bio membership / dynamicsと下流targetを結ぶmap | PARTIAL |
| CLM-53 | DOWN-07 / II social:134,165 | Bioが個体間相互拘束による準閉包維持をshowed | CORRESPONDENCE CLAIM; MECHANISM CLAIM; CROSS-SCALE CLAIM | Bioへの成果attributionのみを監査 | EV-07 | 該当Bio-local construction/result locator・inter-individual maintenance map | NO |
| CLM-54 | DOWN-04 / Intelligence I Introduction:15 | Bio supplies biological vocabulary for four-layer correspondence | CORRESPONDENCE CLAIM | 引用する語彙の所在のみ | EV-01, EV-08 | Bio vocabularyと参照先の確認 | YES |
| CLM-55 | S05:13–27; S04:9 | asymmetries give direction、stable formがstate changeから現れる | MECHANISM CLAIM; EMERGENCE CLAIM | intuitive biological picture、universal necessityとは未記載 | EV-03, EV-07 | concrete relation/conditions・persistence analysis、biologyにはmap | PARTIAL |
| CLM-56 | S04:5; Phase 00 EMP-01 | same DNAのcellsが異なるstateへdifferentiateしうる | OBSERVATIONAL CLAIM | 一般生物学的background、Bioの新規実験resultではない | EV-09 | backgroundの具体文献箇所。Bio mappingを支持するには別burden | PARTIAL |

### Source-family coverage

以下は重複統合の逆引き。古いGEN等を消さず、強い文と限定文を同じsource traceで併記する。
MLは32、BIは10、ATは15、EMは9、GENは17を全件保持。
同じCLMを複数回参照してもclaim数へ再加算しない。

| Original ID | Phase-04 claim families |
|---|---|
| GEN-01 | CLM-01, CLM-12 |
| GEN-02 | CLM-55 |
| GEN-03 | CLM-07, CLM-24 |
| GEN-04 | CLM-05 |
| GEN-05 | CLM-13, CLM-17 |
| GEN-06 | CLM-46 |
| GEN-07 | CLM-14 |
| GEN-08 | CLM-18 |
| GEN-09 | CLM-19, CLM-20, CLM-21 |
| GEN-10 | CLM-22, CLM-23, CLM-24, CLM-25 |
| GEN-11 | CLM-26, CLM-27 |
| GEN-12 | CLM-28, CLM-29, CLM-30 |
| GEN-13 | CLM-48 |
| GEN-14 | CLM-32, CLM-35, CLM-37, CLM-39, CLM-40, CLM-41, CLM-45 |
| GEN-15 | CLM-43 |
| GEN-16 | CLM-32, CLM-44 |
| GEN-17 | CLM-50 |
| ML-01 | CLM-55 |
| ML-02 | CLM-19, CLM-23 |
| ML-03 | CLM-06, CLM-07 |
| ML-04 | CLM-06 |
| ML-05 | CLM-24 |
| ML-06 | CLM-19 |
| ML-07 | CLM-05 |
| ML-08 | CLM-09 |
| ML-09 | CLM-07 |
| ML-10 | CLM-12, CLM-13 |
| ML-11 | CLM-13, CLM-17 |
| ML-12 | CLM-14 |
| ML-13 | CLM-15, CLM-18, CLM-33 |
| ML-14 | CLM-07 |
| ML-15 | CLM-17, CLM-18 |
| ML-16 | CLM-20 |
| ML-17 | CLM-23, CLM-24, CLM-25 |
| ML-18 | CLM-18, CLM-20 |
| ML-19 | CLM-17, CLM-23 |
| ML-20 | CLM-20, CLM-21 |
| ML-21 | CLM-25, CLM-26, CLM-27 |
| ML-22 | CLM-29 |
| ML-23 | CLM-33, CLM-34, CLM-35, CLM-37, CLM-39 |
| ML-24 | CLM-32, CLM-41, CLM-42 |
| ML-25 | CLM-07, CLM-43 |
| ML-26 | CLM-43 |
| ML-27 | CLM-35, CLM-37, CLM-39, CLM-40, CLM-45 |
| ML-28 | CLM-32, CLM-44 |
| ML-29 | CLM-10, CLM-11, CLM-25, CLM-49 |
| ML-30 | CLM-01, CLM-22, CLM-29 |
| ML-31 | CLM-48, CLM-55 |
| ML-32 | CLM-32, CLM-39, CLM-40, CLM-41 |
| BI-01 | CLM-02, CLM-03 |
| BI-02 | CLM-04, CLM-05, CLM-08, CLM-09 |
| BI-03 | CLM-06, CLM-07 |
| BI-04 | CLM-12, CLM-13, CLM-16 |
| BI-05 | CLM-17, CLM-18 |
| BI-06 | CLM-22, CLM-23 |
| BI-07 | CLM-20, CLM-21 |
| BI-08 | CLM-28, CLM-29, CLM-30 |
| BI-09 | CLM-32, CLM-35, CLM-38, CLM-40 |
| BI-10 | CLM-44 |
| AT-01 | CLM-19, CLM-55 |
| AT-02 | CLM-19 |
| AT-03 | CLM-13, CLM-17 |
| AT-04 | CLM-17, CLM-18, CLM-20 |
| AT-05 | CLM-22, CLM-23, CLM-24 |
| AT-06 | CLM-10, CLM-22, CLM-23 |
| AT-07 | CLM-25 |
| AT-08 | CLM-18, CLM-20 |
| AT-09 | CLM-17, CLM-23 |
| AT-10 | CLM-21 |
| AT-11 | CLM-26, CLM-27 |
| AT-12 | CLM-28, CLM-29, CLM-30 |
| AT-13 | CLM-48 |
| AT-14 | CLM-43, CLM-45 |
| AT-15 | CLM-49 |
| EM-01 | CLM-18, CLM-32 |
| EM-02 | CLM-37, CLM-38 |
| EM-03 | CLM-35 |
| EM-04 | CLM-39, CLM-41 |
| EM-05 | CLM-40, CLM-41 |
| EM-06 | CLM-22, CLM-23, CLM-24 |
| EM-07 | CLM-21 |
| EM-08 | CLM-29 |
| EM-09 | CLM-16, CLM-17 |

### Phase-03 interpretive / unresolved handoff

| CIR ID | Claim question carried forward | Phase-04 locator |
|---|---|---|
| CIR-03 | observation window / proxy selector | CLM-03; GAP-01 |
| CIR-04 | I naming→biological identity | CLM-02/03 |
| CIR-05 | event-to-current aggregation | CLM-05; GAP-02 |
| CIR-07 | Phi interpretation / stable region | CLM-07/43 |
| CIR-09 | theta selection / fitting provenance | CLM-13/14; GAP-04 |
| CIR-10 | threshold label→morphology | CLM-16/17 |
| CIR-12 | return definition→robustness | CLM-19/20 |
| CIR-13 | return→regeneration | CLM-21 |
| CIR-14 | history conditions→intelligence | CLM-29 |
| CIR-17 | positional cue→eye-like interpretation | CLM-39/40/41 |
| CIR-18 | G / G_norm / B→boundary | CLM-36/37/38 |
| CIR-21 | shared glyph→cross-layer identity | CLM-51 |

Phase 03のserious circularity 0 / unresolved 3という分類を変更しない。
この表はloopを再判定するものではなく、そのclaimで何を追加に問うかを示す。

## 4. Core field claims

### I / J

Iのlocal structure・constraint・retained biasという定義のburdenはCLM-02でYES。
CLM-03ではmorphogen concentrationやdifferentiationを同じIで表す対応が記述される一方、
window/observable選択、units、測定map、複数observableを共通carrierへ写す規則は未固定。
そのため対応の記述はsupportとして残し、operational biological identityまで満たしたとはしない。
Bio IとIFGT Iの直接非同一はS04/S21/S22に明記されている。

Jのformal current / constitutive expressionはCLM-04。
gene eventsのaggregateがvector currentになるCLM-05は、event class・Delta Iという枠はあるが、
averaging/space-time units/typingのmapと生物的fluxの校正をlocateしない。
formal currentの構成とbiological mechanism burdenを別判定にする。
simulationがJを直接integrateしないことだけでNOとしたのではない。

### Phi/F / sigma

CLM-06のYESは指定したpotential/signの例とgradient操作に限定する。
Phi[I]という記法だけでstable basin、biological return、differentiationを定量説明できるという
CLM-07のburdenは満たさない。具体functionalと独立response/region criterionが必要になる。
コードにPhi/Jを追加したり、新しいstability proofを作ったりしない。

CLM-08はsource slot / balanceを表示するburdenに対するYES。
CLM-09のgene productionには別のsource identificationが必要で、
generic sigmaにgeneという名前が付くことは独立production measurementではない。
toy sigma_Mは具体的profileを持つが、別対象Mのmodel sourceであり、
generic Bio sigmaやupstream sigmaを測定したsupportとして流用しない。
sourceがsigmaを実際に残差推定したとはPhase 03と同様に断定しない。

### Time

CLM-10はrhoの意味とtに対するaccumulationのdefinition。
CLM-11はS16のscope exclusionであり、biological clockを生成したというclaimはlocateしない。
temporal calibration、rho(I,J)/rho(x)の具体化、clock/observable mapは
将来その読みを実現する際のburden。NOT APPLICABLEは完成を意味しない。

## 5. DNA / parameter claims

CLM-12ではsequence、theta(s)、event increment、thresholdを記述するformal supportを保持する。
CLM-13では具体genotype→parameter→reaction/differentiationの説明を判定対象にする。
そのmap、organism-specific calibration、gene intervention / held-out mappingをlocateしない。
コードのDNA-like constantsはparameterized modelを構成するが、sequenceから算出された値ではない。

CLM-14のhistorically stabilized constraintsはsourceが自ら具体起源を導かないと限定するinterpretation。
correspondenceの存在とhistorical mechanism/provenanceは別である。
Phase 03のparameter fitting履歴UNRESOLVEDから、tuningが行われたとも行われなかったとも推定しない。

CLM-56のsame-DNA differentiationは一般的生物背景の言及として保持する。
このtaskでは外部文献本文を検証していないので、それをBio theta(s)の実験的支持には数えない。
文献backgroundとBio固有mechanism burdenを混ぜない。

## 6. Morphogenesis claims

要求された4読みを別々に照合する。主張されていない強い読みを新たなCLMとして捏造しない。

| Reading | Actual source position | Claim / support | Burden result |
|---|---|---|---|
| A: toy produces structured spatial patterns | S14/S15はfinite toy structural possibilityを述べる | CLM-32; EV-04/05/06 | YES、既存reported finite witnessの範囲 |
| B: toy supplies biological developmental mechanism | S15:113 / S22は明示的にそのclaimをしない | 陽性claim未locate、CLM-01/32のscope | NOT APPLICABLE。仮に主張するならobservable map/interventionが必要 |
| C: proposed dynamics explain morphogenesis | S09:57,65のconvergence説明 | CLM-18; source equations + interpretation | PARTIAL、concrete convergence/biological mechanism burdenは別 |
| D: observed morphology is stable configurations | S08:57 / S09:53–57 | CLM-17; classification + identification prose | NO、independent observation/identification map未locate |

Aの有限patternとC/Dのbiological explanationを一つの「示された」にまとめない。
S09のreaction–diffusion component（CLM-15）とthreshold classification（CLM-16）は
各formal scopeでYES。これらをDのbiological mappingの代わりにしない。

## 7. Robustness / regeneration claims

CLM-19のattractor naming/conditional returnには定義的supportがある。
CLM-20のbiological reproducibility / robustnessには独立region criterion、
perturbationの強さ・時点・回復判定、convergence/model sensitivity、biological mappingが必要になる。

現行modelのsmall initial I noiseはpost-formation disturbanceではない。
mode switches、editable rates、no-eye optionの存在も、結果の揃ったrobustness sweep / ablationと同じではない。
調べたBioのcurrent manuscripts/code/reportに、その専用protocol/resultやstability/existence proofをlocateしない。
個々のtestの精度・統計的十分性を採点したのでなく、claimに対応するsupport型の所在を分類した。

| Regeneration reading | Current repository support | Additional burden / scope |
|---|---|---|
| conceptual reconstruction interpretation | S10:55 / working JA §7.8、CLM-21 / EV-07 | interpretationとして記述あり |
| model-local recovery after large disturbance | regeneration-specific run/interventionをlocateせず | reconstructed object、disturbance、recovery criterion、time-series |
| biological regeneration mechanism | reconstructive interpretationのみ | operational target・mechanism-specific intervention / alternative model |
| empirical regenerative behavior | corresponding dataset / direct measurement未locate | biological dataとmodelのpaired mapping |

後3行をBioが達成済みと明言した新claimとして数えない。
CLM-21 PARTIALはinterpretationからregeneration-specific readingを支えるburdenまでの距離を表す。
JA TeXのsubsection省略とworkingの「導かれる」の差（VR-08）を保持し、sourceを統合しない。

## 8. Life-attractor claims

| Required life sub-target | CLM | Current support ceiling | Remaining stronger burden |
|---|---|---|---|
| life-def: bounded viable regionという定義 | CLM-22 | terminological definition、YES | empirical life identityとは別 |
| life identification | CLM-23 | criteria + interpretation、biological burden NO | independent life/viability criterion、observable/boundary map |
| life-dyn: region arises from interactions | CLM-24 | generic equations / feedback description、PARTIAL | concrete dynamics、region construction、existence/convergence |
| life-maint: exchange/update maintains organization | CLM-25 | non-equilibrium structural interpretation、PARTIAL | flux/state/boundaryの具体化、maintenance criterion |
| life-return: robustness from return property | CLM-19/20 | definition YES / biological explanation NO | independent perturbation/return identification |
| life-prob: region-entry target | CLM-26 | event reformulation、YES | numerical probabilityには別のmeasure/trial model |

boundedness、viable range、return、continued exchange、tau progressionがpreloadされることはPhase 03のまま。
life-defを満たすだけで「lifeを観測的に同定した」としない。
“not externally imposed”のregionと、model grid/eye_window/clip boundaryも別object。
toyのB/N/E画像をOmega_lifeの具体的membership plotへ読み替えない。

## 9. Probability claims

CLM-26はpoint targetからregion-entry/persistenceへ、何を数えるかを再定義するclaim。
S11はno numerical reassessment、not automatic necessityと明記する。
そのtarget reformulationはYESであり、算出されたbiological emergence probabilityはlocateしていない。

CLM-27のfewer effective variables / dimensional reductionには、
original/reduced state space、projection、eventやmeasureを何の意味で保つかの表示が必要。
dimensionality branchの有限結果をBioの確率計算へ継承しない。

CLM-30はtwo-stage conditional factorのschematic記述である。YESはこの表示scopeだけで、
独立性の証明・数値確率・統計的uncertaintyを得たという意味ではない。
CLM-31のworking P_life反復は別版としてUNRESOLVED。
source hierarchyから配布manuscriptの式は分かるが、省略/typo/alternativeという意図は決めない。

quantitative estimate / empirical probabilityという陽性claimは現在locateせず、
それらの達成burdenはNOT APPLICABLE。
将来主張するならprobability measure、trial/selection rule、temporal horizon、uncertainty/calibrationが必要になる。

## 10. Second-attractor / intelligence forward claims

CLM-28のsubset/追加条件はformal declarationとしてYES。
CLM-29のhistory/reference/reuse/shareによるintelligenceはforward interpretation。
working JA §9.3の「必要な条件」という語も含め、十分条件と自動的に同一視しない。
S12はinevitableではないと明記する。

set relationだけではregionが実在し安定すること、historyを備えるすべての系が知性であること、
それらが生物的/認知的observableに対応することは確定しない。
history dynamics、membership、stability、operational cognitive criterionが別のburden。
necessityを主張する部分には条件を欠く比較・counterexample / ablationの検討も必要になる。
この照合はBio-local forward claimだけで、intelligence theory内部の定理や認知実装を監査しない。

## 11. Toy-model chain claims

Phase 02の11relationsを全件継承する。各edgeは同じ種類の「生成」ではない。
YESは表示したlocal constructionについてで、whole chain / biological mechanismへ自動伝播しない。

| Edge ID | Relation from Phase 02 | Actual support / code dependence | CLM | Burden / ceiling |
|---|---|---|---|---|
| EDGE-01 | source / diffusion / decay→M | prescribed sigma_MとPDE/finite update | CLM-33 | finite construction。biological source同定とは別 |
| EDGE-02 | M→I | alpha coupling、codeはnew Mを使用 | CLM-34 | executable dependence。情報の実体生成ではない |
| EDGE-03 | I→N | soft threshold update / clip、trackedN | CLM-35 | finite neural-like model pattern |
| EDGE-04 | I→G | gradient magnitude | CLM-36 | formal/array construction |
| EDGE-05 | G→G_norm | max+epsilon normalization | CLM-36 | normalized update input、raw Gと別 |
| EDGE-06 | G/G_norm→B | thresholded accumulation、trackedB | CLM-37/38 | model B構成とboundary interpretationを分離 |
| EDGE-07 | N→B in compact chain | code直接inputなし、I gradient→B | CLM-42 | sequence meaning未固定。NがBを生成したsupportとしない |
| EDGE-08 | N+B+window→E | combined smooth gate + current state | CLM-39/40 | imposed positional preference下のfinite outcome |
| EDGE-09 | A(x,y)/mode→gate | prescribed Gaussian windows | CLM-39/41 | positional construction、位置の自発的生成ではない |
| EDGE-10 | fields→hierarchy | paper summary + report / code分岐 | CLM-42 | typed dependencyとtime-orderを一つにしない |
| EDGE-11 | hierarchy→quasi-closure/sub-attractor | S14:115 structural interpretation | CLM-43 | correspondenceのみ、直接criterion/field mapは未固定 |

paper Gとcode G_norm、paper one-k Sとcode two sigmoids、DTの適用差、sequential update、
clipping、source/eye modesをPhase 01のまま保存する。
これらの違いが存在することから計算誤りを判定しない。
一方、その違いを無視したpaper/code exact correspondenceはsupportに加えない。
CLM-42はclaim type/edge対象のUNRESOLVEDであり、equationを改訂する指示ではない。

## 12. Boundary / neural / eye-like claims

### Boundary

CLM-36/37はgradient-sensitive quantityとB updateのconstruction。
CLM-38はboundary-likeというbiological interpretationで、actual membrane / organism boundary同定は別。
sourceに「Bがmembraneそのものである」という独立した陽性claimはlocateしない。
生物的膜生成を新しいclaimとして追加してNO判定することはしない。

Phase 03のPARTIAL STRUCTURE PRELOADEDは、spatial variationを選ぶruleの先置きを示す。
同じruleでBを得ることはmodel内の意味があるが、独立biological boundary criterionには代えられない。
VR-11のB/magnitude圧縮はそのままclaim対象を分ける材料として保持する。

### Neural

CLM-35のfinite patternは、central source、Iのcoupling、neuralというlabel、threshold/updateという
条件の下で報告されている。tracked Nは中央の高値regionを示す。
finite modelにはYES、observed neural-plate formation mechanismへのmapはこのsupportに含まれない。
「neural-like」という限定を消してempirical claimに拡張しない。

### Eye

| Eye sub-reading | Current support | Burden ceiling |
|---|---|---|
| E is updated under positional gate | S21 / CLM-39 | explicit finite construction |
| two eye-spot-like lobes in reported output | current tracked E / CLM-40 | finite visual witness、not biological eyes |
| position is spontaneous without prior location information | positive claimとしてS22は採らず、windowを明記 | source/windowがimposedであり、その強い読みをwitnessだけでは支えない |
| no completed final drawing encoded | code source/initialization / CLM-41 | final pattern arrayをinputする処理なし |
| no geometric information supplied at all | S14のgeometry文をこう読む場合 | width/center/gateがあり、この読みのburdenは満たさない |
| real biological eye mechanism | S22はnot realistic eye-development modelと限定 | current completed mechanism claimは未locate |

current E PNGには中央付近の左右二つの高値lobe、Nには中央band、Bにはgradient-sensitive bandsが表示される。
これは図の既存内容の確認であり、特定parameter/runとの完全一致、stable attractor判定、
実際の眼・神経・膜との比較を実施したものではない。

Gaussian windowもsigmoidもsoft weightであり、hard binary inside/outsideではない。
location preloadを含むconstrained localizationとspontaneous spatial emergenceを分離する。
locationがpreloadedであることから結果をinvalidとはしない。
window/source sensitivityやcounterfactualは、location-free / causal necessityへ進む場合のburdenであり、
finite constrained witnessの存在そのものに一律要求するものではない。

## 13. Simulation-observation claims

CLM-44は数値配列のsummary / figureとしてのobservation。
sourceとcodeに対応するmean/max/fraction>.5、contour、RGB normalizationをlocateした。
これはbiological direct measurementではないが、numerical outputとしてのsupportを失わない。

CLM-45のstable / attractor-likeにはfinite final imageとsourceのrun記述がある。
それだけで長時間stability、perturbation後のreturn、parameter robustness、continuum convergenceを
全て満たしたとは扱わない。test/proofの所在を確認するburdenをPARTIALとして残す。

| Support check | Located result | What is not counted |
|---|---|---|
| executable finite construction | S21のone model family | 独立cross-model replicationではない |
| existing reported finite output | S15、tracked7PNG | 今回実行した新witnessではない |
| N/B/E visual content | current3PNGを目視 | observational biological identificationではない |
| robustness / regeneration run | dedicated protocol/result未locate | initial noiseをperturbation studyに数えない |
| ablation / alternate modes | switches/code pathsは存在 | controlled comparison実績を推定しない |
| external biological data | loader/dataset/paired measurement未locate | bibliographyやfield名をdataと数えない |
| artifact/run provenance | Phase 00 U11/U16を維持 | ignored alternate images/GIFをindependent replicationに数えない |

Bio sourceはtoy / structural possibilityと明示している。
“confirmed”が下流にある場合、同じword familyでもCLM-50として別のburdenを照合する。
source already limits itselfという事実と、後続mechanistic interpretationのburden未達は両立する。

## 14. Universality / cross-scale claims

CLM-46のS08:61はmolecule/cell/tissue scaleで同じformal structure / rolesを使えるという文。
field vocabularyの再使用はlocateするが、scale translation、coarse operator、
invariant quantity、各levelのcalibration、cross-organism / multi-model結果はlocateしない。
一つのfinite 2D modelはこのcross-scale burdenを単独で満たさない。

CLM-47はIFGT→Bio correspondenceであり、source-local Iの非同一を明記したscopeを保持する。
RC-005–010 / RC-040 / RC-041の8 bridge relationsは上流OPENのまま。
Bio-local I/J/sigma/tauやmodel Bを、それらの完成したmappingとしない。
上流auditのCLOSEDはBioへのempirical support・universality certificateではない。

CLM-48のL3/L1対応はliteral translationでないとsourceが限定する。
noteの具体path/versionというU15が残るので、双方向source correspondenceの照合はUNRESOLVED。
下流のsame-role / same-structureは次節でsource継承の強さだけを比較する。

## 15. Downstream attribution audit

Bioの何を引用しているか、引用先のclaimが元のsupport ceilingを越えていないかだけを対象とする。
consciousness / intelligence / CTの内部理論の成立判定はしない。
以下のstatusはattributionの比較結果であり、revision dispositionではない。

| Downstream claim | What Bio actually supplies | Stronger wording? | Evidence inherited correctly? | Handoff |
|---|---|---|---|---|
| DOWN-01: [SSO EN](../../consciousness/sections/sso.tex):9–23 / [JA](../../consciousness/sections_ja/sso_ja.tex):10–18、fast/slow necessarily / confirmed | source-local life interpretation + finite M/I/N/B/E report、専用fast/slow criterion/result未locate | YES、CLM-50 | STRONGER THAN BIO SOURCE。finite hierarchyを必要性/専用確認へ昇格できない | 専用診断・元結果・rate対照の所在をPhase 05 / downstream auditへ |
| DOWN-02: [projected windows](../../consciousness/sections/formal_mapping.tex):55–65、[correspondence map](../../consciousness/sections/correspondence_map.tex) | window-local quantities / nonidentity注記 | correspondenceとしては強化しない。same underlying structureの射程は別 | CONSISTENT WITH BIO SCOPE（非同一/非還元の部分のみ） | 下流projection理論自体はDOWNSTREAM AUDIT REQUIRED |
| DOWN-03: [CT mapping](../../conceptual-topography/sections/formal_mapping.tex) / [intro](../../conceptual-topography/sections/introduction.tex) | direct Bio inheritanceは未locate | direct Bio claimなし | ATTRIBUTION UNCLEAR、Bio direct edgeを作らない | IFGT/CT比較は本task範囲外 |
| DOWN-04: [Intelligence I intro](../../intelligence-part1/sections/01_introduction.tex):15 / [four-layer horizon](../../intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex) | biological vocabulary / quasi-closure interpretation、CLM-54 | vocabulary引用の範囲ではNO | CONSISTENT WITH BIO SCOPE（語彙供給のみ） | 各layerのphysical/cognitive identityは別 |
| DOWN-05: [II preliminaries](../../intelligence-part2/sections/01_preliminaries_ja.tex):121 / [inference](../../intelligence-part2/sections/02_inference_operator_ja.tex):21–29 | theta/Fのsource-local role、Bio-local state evolution | YES、same dynamics / glyph as evidence、CLM-51 | STRONGER THAN BIO SOURCE。role同形はtyped dynamics identityではない | translation / preserved structureをdownstream reviewへ |
| DOWN-06: [II stopping](../../intelligence-part2/sections/05_emergent_stopping_layer_ja.tex):67,106 / preliminaries:251–260 | history/reference/sharing条件、実装をfuture workへ残す | YES、L_Eとのsame structure identity部分、CLM-52 | STRONGER THAN BIO SOURCE（追加条件の引用自体は対応） | 条件再使用とequivalenceを分離して次の監査へ |
| DOWN-07: [II social](../../intelligence-part2/sections/09_social_blockchain_ja.tex):134,165 | system/environment exchangeとfuture inter-individual work | YES、Bioがinter-individual maintenanceを“示した”、CLM-53 | STRONGER THAN BIO SOURCE。該当Bio construction/resultは未locate | attribution exact target U14 / source locator |
| DOWN-08: [four layers](../../intelligence-part1/figures/fig5_four_layer_correspondence.svg)、[three emergence examples JA](../../intelligence-part2/figures/fig5_three_examples_of_emergence_ja.svg)、[homology JA](../../intelligence-part2/figures/fig9_cross_domain_homology_ja.svg)、draft reprises S36 | life/second-attractorのconcept names、finite toyではない | 図/summaryの同型・創発圧縮あり、独立なBio evidenceではない | DOWNSTREAM AUDIT REQUIRED。上記identity familyの再掲を新証拠へ数えない | full figure/branch auditは未開始、CLM-46/50–53と区別して保持 |

stronger-than-source attributionはDOWN-01/05/06/07の4受け取り方。
DOWN-08のduplicateを同じclaimの追加実績や独立evidenceとして再加算しない。
図そのもののcomprehensive視覚監査はこのphaseで行わず、source labelsと引用方向の確認に限定した。
Phase 03と同様、Bioへ戻るreverse proof citationを追加しない。source-level vicious circularityの新判定も行わない。

## 16. Necessity / sufficiency language ledger

necessary / necessarily / sufficient / follows / must / inevitable / determines / proves /
confirmed / shown / demonstrates / explains / generates / emergence、および語形・日本語対応を
current Bio TeX、working MD、code/README、直接Bioを引用する下流sourceで検索し文脈を確認した。
以下はstatement familyでありkeyword hit数ではない。code returnやfile generationは除外する。

| Language ID | Source / wording context | Claim locator | Reading / burden distinction |
|---|---|---|---|
| NG-01 | S05 asymmetries give direction / form | CLM-55 | intuitive mechanism、universal necessity定理ではない |
| NG-02 | S07 specified sign points toward increasing I | CLM-06 | conditional formal consequence |
| NG-03 | S07 loop can produce sustained structure | CLM-24 | model-local possibility / existence burden |
| NG-04 | S08 gene network generates J | CLM-05 | biological aggregation mechanism / map burden |
| NG-05 | S08 thresholds induced by DNA | CLM-13 | genotype-to-parameter mechanism、nameだけで十分でない |
| NG-06 | S09 stable state is observed morphology / result | CLM-17/18 | biological identification / causal reading |
| NG-07 | S09/S10 robustness follows; working life「導かれる」 | CLM-19/20 | conditional definitionとbiological returnを分離 |
| NG-08 | S10 region not externally imposed / formed | CLM-24 | endogenous region construction、grid/windowと別 |
| NG-09 | S11 not numerical / neither miraculous nor automatic | CLM-26/27 | event再定義、必要性や定量成立確率ではない |
| NG-10 | S12 intelligence appears when; working「必要な条件」 | CLM-29 | emergence/必要条件の言葉、十分条件とは未同定 |
| NG-11 | S12 neither inevitable nor final form | CLM-29 | source自身の非必然scope、necessity theoremの反証を作らない |
| NG-12 | S14 demonstrate structural principle / stable solution | CLM-32/45 | finite witnessとlong-term stabilityを分離 |
| NG-13 | S14 geometry not explicitly encoded / S15 final shape unspecified | CLM-41 | completed drawingとlocation preloadを分離 |
| NG-14 | S15 dynamics determine where / paired patterns | CLM-39/40 | imposed cue下のmodel outcome |
| NG-15 | S15 observations / does not demonstrate biological mechanism | CLM-44/32 | numerical observation、限定文を保存 |
| NG-16 | S16 existing models remain necessary; S17 must identify empirical forms | CLM-01/49 | 他modelを置換しないscope / future requirement、結果の証明ではない |
| NG-17 | S31 SSO necessarily / required / confirmed | CLM-50 | biological necessity / specialized numerical confirmationのattribution |
| NG-18 | II F glyph as evidence / same dynamics | CLM-51 | cross-layer identity、同記号だけではmapを供給しない |
| NG-19 | II L_E same structure / Bio showed maintenance | CLM-52/53 | correspondence強化 / attributionのburden |
| NG-20 | S04 same DNA cells / S09 reproducible background | CLM-56/20 | general biological observationへの参照、新しい実験報告ではない |

explicitなuniversal biological sufficiency theoremや“proves”を用いたBio-local完成証明はlocateしない。
“when”を機械的にiffへ変換せず、codeのsmooth gatesを必要十分な生物学的条件としない。
unqualified wordingと限定文を両方記録しているので、検索hitをそのままevidenceやfailureの数にしない。

## 17. Claim-strength ladder

levelはsourceの現在のclaim対象を記述する索引であり、evidence grade、許可する書換え案、revision dispositionではない。
L3はmechanismを説明しようとする対象の分類で、sourceの断定文をcandidate文へ書き換えたことを意味しない。
L6に分類してburdenがNO/PARTIALとなる場合も、そのsourceが普遍的な主張を置くことと、それを支えるsupportを区別する。
L5=0は本inventory内で実績として外部生物データ検証を述べるclaimをlocateしないという集計であり、Bioのempirical validity verdictではない。

| Claim ID | Current level | Source claim対象 / scope | Burden status |
|---|---|---|---|
| CLM-01 | L1 FORMAL / CONSTRUCTION | 共通記述の提示。全biology説明の十分性でない | YES |
| CLM-02 | L0 TERMINOLOGICAL / DEFINITIONAL | 用語・state variableの定義 | YES |
| CLM-03 | L4 BIOLOGICAL CORRESPONDENCE | 生物量との対応。単一observableのidentityは別 | PARTIAL |
| CLM-04 | L1 FORMAL / CONSTRUCTION | 与えたfield表現内のcurrent構成 | YES |
| CLM-05 | L3 MECHANISTIC CANDIDATE | 離散gene event→biological currentという機構読み | NO |
| CLM-06 | L1 FORMAL / CONSTRUCTION | sign/functionalを選んだ条件内のみ | YES |
| CLM-07 | L3 MECHANISTIC CANDIDATE | biological response解釈。codeの独立Phi/Jとはしない | PARTIAL |
| CLM-08 | L1 FORMAL / CONSTRUCTION | source-term role、unconditional conservationでない | YES |
| CLM-09 | L4 BIOLOGICAL CORRESPONDENCE | 生物的生成との対応を読んだ場合 | NO |
| CLM-10 | L0 TERMINOLOGICAL / DEFINITIONAL | interpretive definition relative to t | YES |
| CLM-11 | LEVEL UNRESOLVED  | 将来のbiological clock同定、現在の成功claimでない | NOT APPLICABLE |
| CLM-12 | L1 FORMAL / CONSTRUCTION | representationとparameter/threshold slotの提示 | YES |
| CLM-13 | L3 MECHANISTIC CANDIDATE | 具体genotype→parameter→outcomeの機構読み | NO |
| CLM-14 | L4 BIOLOGICAL CORRESPONDENCE | originのinterpretation、具体起源をderiveしないと併記 | PARTIAL |
| CLM-15 | L1 FORMAL / CONSTRUCTION | PDE形式の採用、empirical species identityでない | YES |
| CLM-16 | L1 FORMAL / CONSTRUCTION | model classification ruleのみ | YES |
| CLM-17 | L4 BIOLOGICAL CORRESPONDENCE | 観測対象との同定。単なるA/B/C定義とは分離 | NO |
| CLM-18 | L3 MECHANISTIC CANDIDATE | 生物学的説明。formal/toy subclaimsと分離 | PARTIAL |
| CLM-19 | L0 TERMINOLOGICAL / DEFINITIONAL | propertyの条件付命名、特定系の安定性証明でない | YES |
| CLM-20 | L3 MECHANISTIC CANDIDATE | 生物学的return説明、generic criterionから分離 | NO |
| CLM-21 | L4 BIOLOGICAL CORRESPONDENCE | conceptual biological interpretation、独立recovery runとは別 | PARTIAL |
| CLM-22 | L0 TERMINOLOGICAL / DEFINITIONAL | lifeというmodel terminologyの定義のみ | YES |
| CLM-23 | L4 BIOLOGICAL CORRESPONDENCE | definitionから独立のlife identification | NO |
| CLM-24 | L3 MECHANISTIC CANDIDATE | generic field/state dynamicsでのregion成立。toy gridと別 | PARTIAL |
| CLM-25 | L3 MECHANISTIC CANDIDATE | biological non-equilibrium maintenanceの説明 | PARTIAL |
| CLM-26 | L0 TERMINOLOGICAL / DEFINITIONAL | event reformulation、no numerical reassessment | YES |
| CLM-27 | L1 FORMAL / CONSTRUCTION | formal reductionの説明、数値確率推定ではない | PARTIAL |
| CLM-28 | L1 FORMAL / CONSTRUCTION | 宣言されたset relation / conceptual architecture | YES |
| CLM-29 | L4 BIOLOGICAL CORRESPONDENCE | Bio-local forward model。inevitableとはしない | PARTIAL |
| CLM-30 | L1 FORMAL / CONSTRUCTION | schematic、not numerical estimate | YES |
| CLM-31 | LEVEL UNRESOLVED  | working-sourceの意図未固定 | UNRESOLVED |
| CLM-32 | L2 MODEL-LOCAL | 有限報告runのstructural possibility、biology機構でない | YES |
| CLM-33 | L2 MODEL-LOCAL | finite implementation、continuous exact solutionでない | YES |
| CLM-34 | L2 MODEL-LOCAL | new M入力のcode依存に限定 | YES |
| CLM-35 | L2 MODEL-LOCAL | neuralというtoy label、observed neural tissueでない | YES |
| CLM-36 | L1 FORMAL / CONSTRUCTION | code返値とpaper raw quantityを区別 | YES |
| CLM-37 | L2 MODEL-LOCAL | finite model operation、Nが直接入力ではない | YES |
| CLM-38 | L4 BIOLOGICAL CORRESPONDENCE | gradient-sensitive model interpretation、membraneは未主張 | PARTIAL |
| CLM-39 | L2 MODEL-LOCAL | smooth weight下のfinite E update | YES |
| CLM-40 | L2 MODEL-LOCAL | reported outputの左右二つのlobe、real eye identityでない | YES |
| CLM-41 | L2 MODEL-LOCAL | completed drawing非入力とspatial information非入力を区別 | PARTIAL |
| CLM-42 | LEVEL UNRESOLVED  | paper summary。11edge roles / code branchと照合 | UNRESOLVED |
| CLM-43 | L4 BIOLOGICAL CORRESPONDENCE | interpretation、code直接Phi/J integrationでない | PARTIAL |
| CLM-44 | L2 MODEL-LOCAL | numerical observation。empirical measurementでない | YES |
| CLM-45 | L2 MODEL-LOCAL | finite final imageから長時間安定性へ拡張する読みを区別 | PARTIAL |
| CLM-46 | L6 CROSS-SCALE / UNIVERSAL | 形式の再使用とscale-invariant biological relationを区別 | PARTIAL |
| CLM-47 | L4 BIOLOGICAL CORRESPONDENCE | source-local Bio I非同一注記を保持 | PARTIAL |
| CLM-48 | LEVEL UNRESOLVED  | 具体note targetの版/path未固定 | UNRESOLVED |
| CLM-49 | LEVEL UNRESOLVED  | 完了claimではない | NOT APPLICABLE |
| CLM-50 | L6 CROSS-SCALE / UNIVERSAL | 下流によるBioへのattribution、下流理論自体は未監査 | NO |
| CLM-51 | L6 CROSS-SCALE / UNIVERSAL | Bioから下流へ継承したidentityという読み | NO |
| CLM-52 | L4 BIOLOGICAL CORRESPONDENCE | additional conditions引用とidentity assertionを分離 | PARTIAL |
| CLM-53 | L6 CROSS-SCALE / UNIVERSAL | Bioへの成果attributionのみを監査 | NO |
| CLM-54 | L0 TERMINOLOGICAL / DEFINITIONAL | 引用する語彙の所在のみ | YES |
| CLM-55 | L3 MECHANISTIC CANDIDATE | intuitive biological picture、universal necessityとは未記載 | PARTIAL |
| CLM-56 | L4 BIOLOGICAL CORRESPONDENCE | 一般生物学的background、Bioの新規実験resultではない | PARTIAL |

## 18. Evidence ceiling matrix

以下は追加map/testを置かずに現在のsupportから言える範囲である。
「単独では成立させない」は不可能性を意味しない。弱いsupportを保持しながら、異なる種類のclaimへ移る際のburdenを可視化する。

| Evidence item | Strongest claim it can support without extra bridge | Claims it cannot establish alone |
|---|---|---|
| Bio equations / EV-01–03 | source-local定義、指定functional/domain内のformal construction・conditional algebra | biological observable identity、genotype-to-phenotype mechanism、全生物への普遍性 |
| finite simulation / EV-04–05 | 指定source・grid・gate・updateを持つmodel-local constructionと報告されたfinite patternの可能性 | 生物的発生の機構、必然性、全parameterでの安定性・再生、cross-organism普遍性 |
| tracked figures / EV-06 | 表示されたN/B/E等のmodel patternの視覚的所在 | actual neural plate/eye/membraneの同定、観測との一致、独立の実験確認 |
| toy output diagnostics / EV-04–06 | arrayのmean/max/mask、finite numerical observation、表示手続 | fraction>.5を生物的測定として扱うこと、長時間attractor判定 |
| observation-window interpretation / EV-01/07/08 | coarse scopeを選んだsource-local変数の意味づけ | window間/生物間の同一量、測定不変性、observer-independent identity |
| attractor / region definitions / EV-01 | returnを含む定義、life/intelligenceというmodel targetの指定 | その領域の存在・到達・安定性、生物学的life identification、再生の因果説明 |
| literature citations / EV-09 | repositoryが背景文献を列挙する事実、一般背景としての位置づけ | 未読外部本文の個別claim支持、Bio固有mechanismの検証、実験datasetの代替 |
| upstream IFGT correspondence / EV-07/08 | source identitiesを分けたformal/interpretive comparison | VED/IFGTの8 OPEN bridges完成、Bio biological mechanismの継承証明 |
| downstream reuse / EV-07 | Bio概念が引用・再使用される事実 | 元のBio claimへの独立support、同glyphを根拠とするsame dynamics、必要性の確認 |
| code switches / initialization / EV-04 | modes、initial noise、window、thresholdを選べる実装 | 実施済みablation、sensitivity study、post-formation intervention、独立replication |
| explicit toy / future-work limitation / EV-08 | source自身の主張範囲と研究targetの確認 | 将来のmechanismや測定mapを現在の達成結果として数えること |

## 19. Evidence-gap ledger

各gapはclaimを棄却する判定でなく、そのstronger readingへ進む場合のburdenの所在を示す。
Phase 05は既存simulation / empirical correspondenceの次段監査先であり、本taskで実験を実施・設計する指示ではない。
後日のrevision decisionに先行してaction dispositionを付けない。

| Gap ID | Claim | Missing burden | Is current weaker support still valid? | Later phase |
|---|---|---|---|---|
| GAP-01 | CLM-03 | Iのproperty/proxy選択、typed observable map、単位・scale calibration | YES：CLM-02のwindow-local定義は残る | Phase 05 observation correspondence |
| GAP-02 | CLM-05 | discrete gene event→current aggregation、flux calibration、mechanism intervention | YES：CLM-04のfield current構成は残る | Phase 05 cross-domain correspondence |
| GAP-03 | CLM-07 | concrete Phi/response functional、return basinとの独立関係、causal specificity | YES：CLM-06の選択されたsign/gradient関係は残る | Phase 05 model-specific correspondence |
| GAP-04 | CLM-13/14 | actual sequence→theta map、parameter provenance・organism mapping、historical stabilizationの対応 | YES：CLM-12のsequence/parameter/threshold表現と類比は残る | Phase 05 parameter correspondence |
| GAP-05 | CLM-09 | independent sigma function / gene-event measurement map | YES：CLM-08のbalance/source-term slotは残る | Phase 05 source correspondence |
| GAP-06 | CLM-11/49 | future targetならclock/duration、I/J/Phi等の操作的同定 | YES：CLM-10定義、future workというscope。現在の達成burdenはN/A | Phase 05 scope handoff |
| GAP-07 | CLM-17/18/55/56 | morphologyの独立criterion、具体機構・背景文献箇所、観測とmodelの対応 | YES：threshold分類、RD formalism、intuitive picture、背景への言及は残る | Phase 05 biological correspondence |
| GAP-08 | CLM-20/45 | 指定systemのreturn/long-time stability、perturbation protocol、parameter/rate dependence、biologyには別map | YES：CLM-19のconditional attractor定義、finite outputは残る | Phase 05 robustness support inventory |
| GAP-09 | CLM-21 | regeneration固有のdisturbance/reconstruction protocol/result、biological mechanism map | YES：再構成としてのconceptual interpretationは残る | Phase 05 intervention correspondence |
| GAP-10 | CLM-23 | life membershipと独立したoperational life/boundary criterion | YES：CLM-22のnamed region定義は残る | Phase 05 identification correspondence |
| GAP-11 | CLM-24/25 | concrete dynamics・endogenous region条件、exchange→maintenance関係、到達/維持のmodel result | YES：generic evolution/viability条件とinterpretationは残る | Phase 05 model / system correspondence |
| GAP-12 | CLM-27 | probability measure、sampling/event条件、effective-variable reduction map / uncertainty | YES：CLM-26のregion-entry target reformulationは残る | Phase 05 probability correspondence |
| GAP-13 | CLM-29 | history/reference/sharingの実装・subset membership、必要条件のscope、cognitive translation | YES：CLM-28のsubset設定、CLM-30のschematic factorizationは残る | Phase 05 Bio-local handoff、downstream audit |
| GAP-14 | CLM-31 | conditional factorとworking squared formのversion/meaning特定 | YES：両source式が存在する事実。数値probabilityの支持とは別 | Phase 05 source correspondence |
| GAP-15 | CLM-42 | paper sequenceとactual I→G_norm→B dependencyのrelation対象固定 | YES：individual updates / finite outputを消さない | Phase 05 paper/code correspondence |
| GAP-16 | CLM-38 | gradient-sensitive Bとbiological boundaryの独立criterion/map | YES：CLM-36/37のderived quantityとfinite updateは残る。膜同定claimを新設しない | Phase 05 boundary correspondence |
| GAP-17 | CLM-41 | completed drawing不使用とlocation-freeのreading区別、後者ならsource/window dependenceの対応 | YES：CLM-39/40のpositional constraint下のfinite localizationは残る | Phase 05 preload / output correspondence |
| GAP-18 | CLM-32/35/40/44/45 | outputとrun/config/code versionの詳細provenance、強い再現性claimなら独立再現情報 | YES：現存図とsource-reported finite witness。今回は再現実行していない | Phase 05 artifact / run correspondence |
| GAP-19 | CLM-43/46/47 | quasi-closure criteria、scale/cross-layer typed maps、preserved quantitiesとlevel別対応 | YES：structural analogy、formal vocabulary、upstream非同一scopeは残る | Phase 05 cross-layer correspondence |
| GAP-20 | CLM-48 | L1 noteのexact path/versionとL3 counterpart | YES：S13の限定されたcorrespondence proseは残る | Phase 05 source locator handoff |
| GAP-21 | CLM-50/51/52 | fast/slow確認への専用結果、necessity scope、same dynamics / L_R/L_E translation | YES：Bio finite model、history条件、下流引用の存在は残る | Phase 05 attribution handoff、downstream audit |
| GAP-22 | CLM-53 | Bioがinter-individual quasi-closure維持を示したとする原resultと機構map | YES：exchange/maintenanceのBio解釈と将来targetは残る | Phase 05 attribution handoff、downstream audit |

PARTIAL/NO/UNRESOLVEDの全30familiesはこのgap tableへ対応する。
GAP-06はN/A targetの将来burden、GAP-18はYES finite witnessを独立再現へ拡張する場合の追加burdenも含む。
したがってgap数とburden未達件数は一致させない。

## 20. Phase-04 outcome

### Counts and interpretation

集計母数はCLM-01–56の56families。typeはmulti-labelなので合計を56に合わせない。
burdenとlevelは各familyに1つを割り当てる。NO/PARTIALはtableで指定したreadingのburdenについてであり、source claimを改訂する判定ではない。

| Claim type | Count |
|---|---|
| DEFINITION CLAIM | 8 |
| FORMAL CONSTRUCTION CLAIM | 16 |
| MODEL-LOCAL DYNAMICAL CLAIM | 10 |
| MECHANISM CLAIM | 9 |
| BIOLOGICAL IDENTIFICATION CLAIM | 5 |
| EMERGENCE CLAIM | 8 |
| ROBUSTNESS / STABILITY CLAIM | 5 |
| OBSERVATIONAL CLAIM | 5 |
| EMPIRICAL CLAIM | 0 |
| UNIVERSALITY CLAIM | 3 |
| CROSS-SCALE CLAIM | 8 |
| CORRESPONDENCE CLAIM | 13 |
| CAUSAL CLAIM | 6 |
| PROBABILITY CLAIM | 4 |
| NECESSITY CLAIM | 2 |
| SUFFICIENCY CLAIM | 0 |
| FORWARD / RESEARCH-TARGET CLAIM | 3 |
| CLAIM TYPE UNRESOLVED | 2 |

| Burden status | Count |
|---|---|
| YES | 24 |
| PARTIAL | 18 |
| NO | 9 |
| UNRESOLVED | 3 |
| NOT APPLICABLE | 2 |

| Current level | Count |
|---|---|
| L0 | 6 |
| L1 | 11 |
| L2 | 10 |
| L3 | 8 |
| L4 | 12 |
| L5 | 0 |
| L6 | 4 |
| LEVEL UNRESOLVED | 5 |

| Other requested metric | Count / counting rule |
|---|---|
| Claim families | 56 |
| Evidence support items | EV-01–09: 9（categoryとは別） |
| Empirical claims actually made | 0：外部生物data/measurementとの検証を達成実績とするBio claimという§2の定義。一般生物観測への言及はCLM-56等に残す |
| Model-local claims | 10：MODEL-LOCAL DYNAMICAL CLAIMのfamilies。L2の10とは集合が異なる |
| Biological mechanism claims | 9：MECHANISM CLAIMの説明対象。Bio-local8 + downstream attribution CLM-53の1 |
| Universality claims | 3：CLM-46/50/51。CROSS-SCALE CLAIMは別に8 |
| Downstream stronger-than-source attributions | 4：DOWN-01/05/06/07。DOWN-08のrepriseは重複加算しない |
| Evidence-gap entries | 22：GAP-01–22 |
| Finite-simulation-only support（排他的） | 0：EV-05/06だけで、formal/code等を全く伴わないfamilyはない |
| 実績型supportがfinite simulation / outputに限られるfamily | 5：CLM-32/35/40/44/45。付随する定義/codeはあるが独立biological measurementではない |
| Definition/terminology-only support | 5：EV-01のみのCLM-02/10/19/22/26。L0はEV-08も持つCLM-54を含むので6 |
| Necessity / sufficiency language ledger | NG-01–20: 20 contexts、sourceのconditional/negative/futureも含む |
| Toy relation coverage | EDGE-01–11: 11、paper sequenceとcode dependencyを混同しない |
| Required prior claim coverage | GEN17/17、ML32/32、BI10/10、AT15/15、EM9/9 |
| Downstream coverage | DOWN8/8、重複repriseとdirect-dependency未特定を明記 |
| Circularity handoffs | CIR12件：Phase 03のinterpretive/unresolvedを§3でtrace、循環性判定は変更しない |

### Scope-sensitive result

定義とformal constructionのburdenが満たされる項目、有限toy witnessがmodel-localな可能性を示す項目、
その上でbiological identification / mechanism / universalityへ進むための別burdenが残る項目を分けた。
I/J/sigmaの量的同定、DNA→theta、lifeとmembershipの独立対応、physical clock / boundary、
robustness/regeneration、cross-scale mapsを、式の存在や生物名から成立済みとしない。
S15/S22のtoy限定とsource自身のfuture workを消さず、必要以上の強いclaimをBioに新設しない。

Phase 03のsource-level vicious circularity未確立という結果を保持する。
上流RC-005/006/007/008/009/010/040/041のOPENおよびsource-local identityを保持し、
Bio definitionやdownstream再使用によってmissing bridgeが完成したと扱わない。
本稿はrevision候補・action disposition・empirical-validation verdict・biological invalidity verdictを作成していない。
source claim/equation、simulation、source版本、figure/PDF、upstream recordの変更なし。
新equation・notation・theory・bridge・evidenceなし。commit/pushなし。

### Validation / write scope

- Local links / source paths: PASS。新record43 + README8 = 51 relative linksのtargetが存在する。
- Markdown fences / display math: PASS。未閉鎖fenceなし、display delimitersは新record9組 / README6組、inline delimitersも釣り合う。
- Tables: PASS。新record20表 / README1表、各tableのcolumn数整合。
- CLM inventory / ladder: PASS。各56/56、主table内のID重複なし、両tableのburden一致。参照IDも範囲内。
- Counts: PASS。burden 24+18+9+3+2=56、level 6+11+10+8+12+0+4+5=56、multi-label type集計を本文表と再照合。
- Coverage: PASS。GEN17、ML32、BI10、AT15、EM9を元recordと照合。DOWN8、EDGE11、CIR handoff12もtrace。
- Ledgers: PASS。GAP22 / NG20 / EV9のIDは各一意。PARTIAL/NO/UNRESOLVED全30familiesのgap参照を確認。
- Write scope: PASS。作業開始時1431既存filesのSHA-256と照合し、変更は本枝READMEのみ、新規は本recordのみ。既存fileの削除なし。
- git diff --check: PASS。既存working-tree変更を保持。新recordはuntrackedのため上記Markdownチェックを別途実施。
- Source/simulation/web: sourceの編集・simulation実行・外部web researchなし。Phase 05の実行・再現性/empirical correspondence監査は開始していない。

Phase 04はここで完了。Phase 05 simulation / empirical correspondence auditは**NOT STARTED**のまま停止する。

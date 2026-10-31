# Bio-IFGT preload / boundary / circularity audit v0.1

## 0. Status

- Bio-IFGT audit: **IN PROGRESS**
- Phase 00 dependency / inheritance: **COMPLETE**
- Phase 01 equation / symbol inventory: **COMPLETE**
- Phase 02 equation role / biological-role audit: **COMPLETE**
- Phase 03 preload / boundary / circularity audit: **COMPLETE**
- Phase 04 claim / evidence burden audit: **NOT STARTED**
- Upstream VED equation audit / core revision: **CLOSED / CLOSED**

最初に[README](README_ja.md)、[Phase 00](00_dependency_and_inheritance_record_v0.1_ja.md)、
[Phase 01](01_equation_and_symbol_inventory_v0.1_ja.md)、
[Phase 02](02_equation_role_and_biological_role_audit_v0.1_ja.md)を読む。
本稿はそのsource identity・role・版差を維持したpreload / boundary / circularity分類である。
生物学的妥当性、empirical adequacy、evidence sufficiency、claim strengthの変更は扱わない。
source・式・code・図・PDF・上流記録は変更せず、simulationも再実行しない。

S番号はPhase 00、BIO-EQはPhase 01、CON/VR/ATはPhase 02のIDを維持する。
U01–U16は**Phase 00 uncertainty ledger**を指し、Phase 01の同名unit行ではない。
以下のPL/CIR/EMは監査索引であり新しい数学的notationではない。

### Source locator key

行番号は今回読んだsourceの位置。function/section名も併記して再追跡可能にする。
EN TeX、self-contained JA TeX、JA working Markdown、実行codeは別authorityである。

| Source | Direct path / locator |
|---|---|
| S02 | [JA manuscript](../../bio-ifgt/main_ja.tex) |
| S04–05 | [Introduction](../../bio-ifgt/sections/introduction.tex):15、[Intuitive Picture](../../bio-ifgt/sections/intuitive_picture.tex) |
| S06 | [Formal Mapping](../../bio-ifgt/sections/formal_mapping.tex):7–60 |
| S07 | [Core Equations](../../bio-ifgt/sections/core_equations.tex):15–80 |
| S08 | [Gene / information flow](../../bio-ifgt/sections/gene_information_flow.tex):7–69 |
| S09 | [Development / morphogenesis](../../bio-ifgt/sections/development_morphogenesis.tex):7–65 |
| S10 | [Life as Attractor](../../bio-ifgt/sections/life_attractor.tex):7–59 |
| S11–12 | [Probability](../../bio-ifgt/sections/probability_revision.tex)、[Second Attractor](../../bio-ifgt/sections/intelligence_second_attractor.tex) |
| S13 | [Relation to note](../../bio-ifgt/sections/relation_to_note.tex) |
| S14–15 | [Toy model](../../bio-ifgt/sections/minimal_developmental_simulation.tex)、[Results](../../bio-ifgt/sections/simulation_results_visualization.tex) |
| S16 | [Discussion](../../bio-ifgt/sections/discussion.tex):13,27–37 |
| S19 | [working life](../../bio-ifgt/sections_ja/life_attractor_ja.md)、[working development](../../bio-ifgt/sections_ja/development_morphogenesis_ja.md)、[working intelligence](../../bio-ifgt/sections_ja/intelligence_second_attractor_ja.md)、[working core](../../bio-ifgt/sections_ja/core_equations_ja.md) |
| S21–22 | [simulate.py](../../bio-ifgt/simulations/minimal_neural_field/simulate.py)、[simulation README](../../bio-ifgt/simulations/minimal_neural_field/README.md) |

## 1. Audit guards / vocabulary

以下は結論ではなく、異なる依存を混同しないためのhard guards。

\[
\text{representation preload}\neq\text{biological ontology}
\]
\[
\text{coordinate choice}\neq\text{physical organism geometry}
\]
\[
\text{simulation boundary}\neq\text{biological boundary}
\]
\[
\text{observation window}\neq\text{observed system itself}
\]
\[
\text{definition dependence}\neq\text{vicious circularity}
\]
\[
\text{self-reference}\neq\text{circular invalidity}
\]
\[
\text{selection rule}\neq\text{empirical discovery}
\]
\[
\text{model viability criterion}\neq\text{biological life criterion}
\]

READMEの6 inheritance guardsも保持する。上流OPENをBio-local definitionで閉じない。

Preload vocabulary: REPRESENTATION PRELOAD; DOMAIN PRELOAD; GEOMETRIC PRELOAD; TEMPORAL PRELOAD; BOUNDARY PRELOAD; OBSERVATION-WINDOW PRELOAD; PARAMETER PRELOAD; INITIAL-CONDITION PRELOAD; SOURCE / FORCING PRELOAD; THRESHOLD PRELOAD; LABEL / CLASS PRELOAD; FUNCTIONAL-FORM PRELOAD; BIOLOGICAL-INTERPRETATION PRELOAD; DOWNSTREAM-CONCEPT PRELOAD; PRELOAD UNRESOLVED.

Circularity vocabulary: NO CIRCULARITY LOCATED; DEFINITIONAL SELF-REFERENCE; FIXED-POINT / SELF-CONSISTENCY STRUCTURE; ITERATIVE FEEDBACK; MUTUAL DEPENDENCE; LABEL-SELECTION LOOP; OBSERVATION-SELECTION LOOP; INTERPRETATION LOOP; CLAIM-THREATENING CIRCULARITY CANDIDATE; CIRCULARITY STATUS UNRESOLVED.

§15のstatusはNOT CIRCULAR / BENIGN / DEFINitional / FEEDBACK, NOT CIRCULAR / INTERPRETIVE LOOP / CIRCULARITY CANDIDATE / UNRESOLVED。
「BENIGN / DEFINitional」は一つのstatus名。NOT CIRCULARは当該source依存経路についての分類であり、
全理論に循環が存在しないという証明ではない。INTERPRETIVE LOOPは命名・解釈の再使用であり、論証の循環を認定しない。
内生性は対象別に記録する。入力された関数形の下でstateが更新されることと、その関数形自体が生成されることは別である。

## 2. Global preload map

### Preload matrix

表の「prior」は表現・実行・解釈の依存順序であり、物理的起源の順序ではない。
imposedはモデルの入力・選択という意味で、研究者の意図やparameter fittingの履歴を推測しない。

| Preload ID | Target | Required prior structure | Source | Type | Endogenous / imposed / interpretive | Later claim depending on it |
|---|---|---|---|---|---|---|
| PL-01 | continuum fields | R3、位置・近傍、coarse scalar/vector表現 | S06:7–23 | REPRESENTATION PRELOAD; DOMAIN PRELOAD; GEOMETRIC PRELOAD | imposed representation | spatial biological description |
| PL-02 | toy domain | 2D square、size、coordinate mesh | S14:9; S21 run_simulation | DOMAIN PRELOAD; GEOMETRIC PRELOAD; BOUNDARY PRELOAD | imposed | embryo-like field / location |
| PL-03 | gradients / Laplacian | differential structure、stencil、spacing convention | S06–09; S21 laplacian/gradient_magnitude | GEOMETRIC PRELOAD; FUNCTIONAL-FORM PRELOAD; BOUNDARY PRELOAD | imposed operator; field values dynamic | direction / boundary-like pattern |
| PL-04 | external t | recording/evolution parameter | S06:47–51; S10:21–25 | TEMPORAL PRELOAD | source-declared external | internal progression description |
| PL-05 | tau / rho | t、selected state/fields、progression function | S07:61–65; S10:23–29 | TEMPORAL PRELOAD; FUNCTIONAL-FORM PRELOAD; PRELOAD UNRESOLVED | definition; concrete rho unspecified | life regime / history of tau |
| PL-06 | numerical time | step count、DT、ordered old/new arrays | S21 run_simulation | TEMPORAL PRELOAD; PARAMETER PRELOAD | imposed schedule | staged development / GIF time |
| PL-07 | observation window | scale、coarse-graining、variable/proxy selection | S04:15; S06:7; S16:31–37 | OBSERVATION-WINDOW PRELOAD; REPRESENTATION PRELOAD; PRELOAD UNRESOLVED | selected concept; procedure unspecified | information as biological quantity |
| PL-08 | Bio I | local constraint/retained-bias meaning、window | S04:15; S06:11–15; S21 docstring | BIOLOGICAL-INTERPRETATION PRELOAD; LABEL / CLASS PRELOAD | interpretive proxy | structure / information density |
| PL-09 | morphogen I / M | concentration profile as represented property | S09:13–28; S14:11,25 | REPRESENTATION PRELOAD; BIOLOGICAL-INTERPRETATION PRELOAD | selected process/label | morphogenesis description |
| PL-10 | J / gene events | chosen I、event categories、aggregation convention | S06:23; S08:21–33 | REPRESENTATION PRELOAD; FUNCTIONAL-FORM PRELOAD; PRELOAD UNRESOLVED | interpretation; concrete aggregation unspecified | gene network as flow |
| PL-11 | Phi / F | functional choice、sign、response coefficients | S07:37–53; S08:45 | FUNCTIONAL-FORM PRELOAD; PARAMETER PRELOAD | system-dependent choice; response interpretation | stable-region / restoring explanation |
| PL-12 | sigma | source slot、production meaning、source function | S07:24; S08:33; S09:26 | SOURCE / FORCING PRELOAD; BIOLOGICAL-INTERPRETATION PRELOAD; PRELOAD UNRESOLVED | generic function unspecified; toy source imposed | gene-event production |
| PL-13 | DNA / theta | nucleotide alphabet、sequence length、parameter set/map | S08:7–17,69 | DOMAIN PRELOAD; PARAMETER PRELOAD; FUNCTIONAL-FORM PRELOAD | representation; concrete map unspecified | DNA-conditioned development |
| PL-14 | Fk / fate thresholds | response signature、threshold values/order | S08:49–53; S09:44–53 | THRESHOLD PRELOAD; FUNCTIONAL-FORM PRELOAD | model-selected | reaction / differentiation switching |
| PL-15 | A/B/C; N/B/E names | state categories、neural/boundary/eye-like labels | S09:45–57; S14:10–19 | LABEL / CLASS PRELOAD; BIOLOGICAL-INTERPRETATION PRELOAD | interpretive labels preassigned | morphology / neural / eye identification |
| PL-16 | x / Omega | state components、environmental variables、F/constraints | S10:7–17,33 | DOMAIN PRELOAD; REPRESENTATION PRELOAD; FUNCTIONAL-FORM PRELOAD | component choice supplied; trajectory dynamic | life-region description |
| PL-17 | Omega_life | viable range、boundedness、continued update/exchange、return criterion | S10:29–43 | BOUNDARY PRELOAD; BIOLOGICAL-INTERPRETATION PRELOAD; PRELOAD UNRESOLVED | criteria stated; region claimed endogenous | life identification / region entry |
| PL-18 | attractor / return | selected stable region、perturbation/return meaning | S07:69; S09:61; S10:37,55 | LABEL / CLASS PRELOAD; BOUNDARY PRELOAD | definition + interpretation | robustness / regeneration |
| PL-19 | second attractor | life region、history/reference/reuse/sharing conditions | S12:11–21,37–45 | DOWNSTREAM-CONCEPT PRELOAD; DOMAIN PRELOAD; BIOLOGICAL-INTERPRETATION PRELOAD | additional conceptual conditions | intelligence forward interpretation |
| PL-20 | probability target | life / second event definitions、conditioning target | S11:19–37; S12:25–29; S19 | DOMAIN PRELOAD; LABEL / CLASS PRELOAD; PRELOAD UNRESOLVED | schematic event selection | region-entry probability wording |
| PL-21 | sigma_M profile | selected mode、centers、widths、amplitude / band | S21 make_sigma_m; S22 Source Modes | SOURCE / FORCING PRELOAD; GEOMETRIC PRELOAD; PARAMETER PRELOAD | fixed before loop | central / edge pattern |
| PL-22 | eye_window | Gaussian positional preference、mode、width | S21 make_eye_window; S22 Toy Eye | GEOMETRIC PRELOAD; PARAMETER PRELOAD; SOURCE / FORCING PRELOAD | imposed gate, not evolving field | eye-like localization |
| PL-23 | initial state | zeros、random generator、seed、noise amplitude | S21 run_simulation | INITIAL-CONDITION PRELOAD; PARAMETER PRELOAD | imposed values; no final pattern loaded | formation from near-uniform state |
| PL-24 | finite responses | diffusion/decay/rates、logistic forms、clipping bounds | S21 constants/sigmoid/run_simulation | PARAMETER PRELOAD; THRESHOLD PRELOAD; FUNCTIONAL-FORM PRELOAD | fixed rules; states dynamic | commitment / bounded arrays |
| PL-25 | B construction | I gradient、whole-grid max normalization、threshold/rate | S14:49–59; S21 gradient_magnitude | FUNCTIONAL-FORM PRELOAD; THRESHOLD PRELOAD; LABEL / CLASS PRELOAD | G/B derived/updated; extraction rule imposed | boundary stabilization |
| PL-26 | observation / plots | summary choice、.5 masks、contours、RGB scaling、frame schedule | S21 print_summary/plotting; S15 | OBSERVATION-WINDOW PRELOAD; THRESHOLD PRELOAD; LABEL / CLASS PRELOAD | diagnostics imposed; measured arrays internal | numerical observation / downstream attribution |

### BIO-EQ universe trace

48個の元IDを以下で全件対応付ける。Expression/source/roleの再分類はPhase 01–02へリンクし、
今回追加するのはpreloadと依存の読みだけ。compact arrowを新しい数式へ置換しない。

| BIO-EQ ID | Target | Preload IDs | Circularity locator | Phase-03 reading |
|---|---|---|---|---|
| BIO-EQ-01 | domain | PL-01, PL-04 | CIR-01 | continuum/timeは記述の前提 |
| BIO-EQ-02 | I | PL-07, PL-08, PL-09 | CIR-03, CIR-04 | window-local proxyとobservableは別 |
| BIO-EQ-03 | J | PL-01, PL-10 | CIR-05 | aggregate currentの定義先を分離 |
| BIO-EQ-04 | Phi[I] | PL-03, PL-11 | CIR-06, CIR-07 | functional choiceとreturn解釈は別 |
| BIO-EQ-05 | F gradient | PL-03, PL-11 | CIR-06, CIR-07 | 指定potentialからの構成 |
| BIO-EQ-06 | J relation | PL-03, PL-10, PL-11, PL-24 | CIR-06 | constitutive feedback、論証循環でない |
| BIO-EQ-07 | tau fields | PL-04, PL-05 | CIR-02 | tとrhoを先に用いる |
| BIO-EQ-08 | balance | PL-04, PL-10, PL-12 | CIR-08 | source slotとgene mechanismを分離 |
| BIO-EQ-09 | Phi example | PL-11 | CIR-07 | sign example、attractor選定法ではない |
| BIO-EQ-10 | sequence | PL-13 | CIR-09 | alphabet/lengthを置く |
| BIO-EQ-11 | theta(s) | PL-13, PL-24 | CIR-09 | 具体parameter fitting経路は未表示 |
| BIO-EQ-12 | gene increment | PL-08, PL-10, PL-13 | CIR-05 | local eventと集約規則を分離 |
| BIO-EQ-13 | Fk threshold | PL-13, PL-14 | CIR-09, CIR-10 | threshold/signature preload |
| BIO-EQ-14 | RD evolution | PL-01, PL-03, PL-04, PL-12, PL-24 | CIR-08 | source/diffusion/decayを与える |
| BIO-EQ-15 | A/B/C | PL-14, PL-15 | CIR-10 | 分類規則とmorphology命名 |
| BIO-EQ-16 | x(t) | PL-04, PL-16 | CIR-11 | state component選択 |
| BIO-EQ-17 | state F | PL-13, PL-16 | CIR-11, CIR-12 | flowと選定regionを別に読む |
| BIO-EQ-18 | tau state | PL-04, PL-05, PL-16 | CIR-02 | rho(x)をtauから定義した箇所なし |
| BIO-EQ-19 | life subset | PL-16, PL-17, PL-18 | CIR-11, CIR-12 | region命名とlife説明を分離 |
| BIO-EQ-20 | intelligence subset | PL-17, PL-19 | CIR-14 | 追加条件を先に置く |
| BIO-EQ-21 | conditional probability | PL-19, PL-20 | CIR-15 | eventの再定義、数値導出でない |
| BIO-EQ-22 | descriptive mapping | PL-07, PL-08, PL-10, PL-11 | CIR-03, CIR-04 | representation対応 |
| BIO-EQ-23 | note correspondence | PL-07, PL-18 | CIR-07 | return analogy、direct translationでない |
| BIO-EQ-24 | M PDE | PL-02, PL-03, PL-04, PL-21, PL-24 | CIR-16 | prescribed source下の更新 |
| BIO-EQ-25 | I PDE | PL-02, PL-03, PL-04, PL-09, PL-24 | CIR-16 | Mを入力とする更新 |
| BIO-EQ-26 | N update | PL-14, PL-15, PL-24 | CIR-16 | gateとneural labelを分離 |
| BIO-EQ-27 | G magnitude | PL-03, PL-25 | CIR-18 | edge敏感なquantityの構成 |
| BIO-EQ-28 | B update | PL-14, PL-15, PL-25 | CIR-18 | gradient入力の蓄積、膜でない |
| BIO-EQ-29 | E update | PL-14, PL-15, PL-22, PL-24 | CIR-17 | positional cueとpatternを分離 |
| BIO-EQ-30 | logistic S | PL-14, PL-24 | CIR-16 | response shapeを先に指定 |
| BIO-EQ-31 | toy chain | PL-15, PL-25 | CIR-19 | N→Bはcode直接依存でない |
| BIO-EQ-32 | toy J/Phi | PL-11, PL-15 | CIR-07 | code独立J/Phiなし、解釈対応 |
| BIO-EQ-33 | working probability | PL-19, PL-20 | CIR-15 | 別版の意図未固定を保存 |
| BIO-EQ-34 | working RD | PL-12, PL-24 | CIR-08 | theta省略を補完しない |
| BIO-EQ-35 | working threshold | PL-13, PL-14 | CIR-09 | signature variantを保存 |
| BIO-EQ-36 | Laplacian | PL-02, PL-03 | CIR-01 | edge-copy境界はimposed |
| BIO-EQ-37 | two sigmoids | PL-14, PL-24 | CIR-16 | smooth gate、二つのsteepness |
| BIO-EQ-38 | central source | PL-02, PL-21 | CIR-17 | 中心位置/幅を与える |
| BIO-EQ-39 | left source | PL-02, PL-21 | CIR-17 | 左8columns支持を与える |
| BIO-EQ-40 | eye window | PL-02, PL-22 | CIR-17 | 位置選好を与える、final eye描画でない |
| BIO-EQ-41 | G_norm | PL-03, PL-25 | CIR-18 | global max依存のnormalized input |
| BIO-EQ-42 | initialization | PL-23 | CIR-16 | zeros/noise、結果から初期値を定義しない |
| BIO-EQ-43 | M/I numerical | PL-06, PL-21, PL-24 | CIR-16 | new MをIへ渡す |
| BIO-EQ-44 | N/B numerical | PL-06, PL-14, PL-24, PL-25 | CIR-16, CIR-18 | N後BだがBのinputはI由来 |
| BIO-EQ-45 | E numerical | PL-06, PL-22, PL-24 | CIR-17 | new N/Bと固定window |
| BIO-EQ-46 | clip/schedule | PL-06, PL-24, PL-26 | CIR-16, CIR-20 | boundsと観測時点を与える |
| BIO-EQ-47 | stats/masks | PL-15, PL-26 | CIR-20 | model selection、empirical測定でない |
| BIO-EQ-48 | RGB transform | PL-26 | CIR-20 | display変換はupdateへ戻らない |

## 3. Spatial / temporal preload

### Spatial

S06は生物系を既存のR3とt上のcoarse fieldsで表す。S14は2D embryo-like domain、
S21はdefault128×128のsquare gridを置く。これはgeometryを生成する規則ではなく、
生物的構造を**その上で**記述するためのrepresentationである。
Bio primaryのここでbiological spaceそのものの生成を独立に主張する箇所はlocateしていない。
VEDのphysical-space claimやnetwork metricをBioへ輸入しない。

source中心・eye window・gradient operatorは別のgeometric input。
central_bandは0..1座標上の中心band、left_edgeは左8columnsのsource。
laplacianはedge-copy zero-fluxとsourceが呼ぶstencil、gradient_magnitudeは別のnp.gradient処理。
両者へ生物学的距離・grid spacingを補わない。
toy grid端に膜・organism boundaryという独立同定は表示されない。
「geometryを明示的にencodeしない」というS14/S02の文は、completed final drawingと
位置・width等の幾何条件を分けて§10/16に残す。ここでsourceを訂正しない。

### Temporal

BIO-EQ-07/18はexternal tとstate-dependent rhoを用いてtauを導入する。
S06:51 / S07:65 / S10:25はtで運動を記述しtauをinterpretiveに用いると述べる。
表示されたrhoの引数はI/Jまたはxであり、tauを先に用いてrhoを定義する逆方向はlocateしない。
ただし具体的rhoは未指定なので、将来の全具体化について循環なしとは保証しない。
S16:27はtauのoperational definitionを範囲外としている。

step/DT/更新順は別のtemporal preload。M/IだけにDTが掛かり、N/B/Eにはstepあたりのrate、
さらにnew M、new N/Bを使う順序がある。GIFのt=step表示はmodel indexであり、
biological clock機構を実装した箇所ではない。life regimeでtauが進むという命名条件と、
その時間の生物学的測定・生成は同じ主張ではない。
下流SSOのfast/slow attributionも、code rateの違いだけから認定しない（§12–13）。

## 4. Observation-window preload

BND-01 / U05は、単に画面のcropではない。
どの生物学的scale・property・時間空間範囲を採り、何をlocal constraint densityとして表すかの選択である。
S04:15はparticular observational windowを先に置き、その中のproxyとしてIを説明する。
S06:7はmicroscopic detailをすべて追わないcoarse descriptionを宣言するが、
window選択・averaging kernel・observable selectionの具体手順は表示しない。

したがって現在locateできるのはrepresentation dependence。
同じI/J/Phiというroleを複数scaleで使うS08:61はあるが、
observer-independentな単一測定量へ変換するmapをそこから推定しない。
また「都合のよいwindowを結果から選び直して確認した」という実際のselection手順もlocateしない。
その往復をCIR-03のUNRESOLVEDに置く理由は、手順の未指定であってcircularityの肯定ではない。

計算全grid、表示mask、GIF samplingは別の観測選択。
G_normのmaxは全gridを参照するため、Bの入力には選んだcomputational domainも関わる。
RGB normalizationはfieldごとの表示変換であり、これを生物系自身の境界としない。

## 5. Core-field preload

### I use

| I use | Required preload | Endogenous / imposed / interpretive | Circularity candidate? |
|---|---|---|---|
| generic Bio I (02) | selected biological window、constraint/differentiationという意味 | representation / interpretive | CIR-03/04。proxy命名と実体説明の再使用、必須論証loop未確認 |
| morphogen profiles as I (S09) | concentration profileを対象として選ぶ、geometry/time | selected process / interpretive | Iからmorphogen identityを独立導出したとはしない |
| toy I (25) | M、coupling、diffusion/decay、initial noise | parameters imposed、array dynamic | numerical updateに結果からの定義loopなし |
| code I / RGB / downstream I | array type、window label、display rule / 別window | model / display / downstream interpretation | array・normalized color・biological observableを分離 |

Iが使える前にproperty/proxyを選ぶことと、Iの値がその後のupdateで変わることは両立する。
sourceはmorphogen、constraint、retained biasを同じ測定手順で同定してはいないが、
この所在情報をbiological invalidityへ変換しない（CON-01）。

### J / events

S06:23はreaction/diffusion/transport/interactionsをまとめたstate updateをJとする。
S08:21–33は既に選んだIへのlocal gene eventの変化を集約してcontinuous Jと読む。
event種類とIの意味はpreload、離散eventからvector currentへの集約法はU04のまま。
Jを独立測定fluxとして固定した経路も、必ずsigmaの残差から定義する経路も表示されない。
従ってCIR-05は具体的同定手順UNRESOLVEDであり、「定義が相互に循環する」とは断定しない。
codeはJを直接integrateしない（CON-02/15）。

### Phi / F

S07:47–53はfunctionalの具体形とsignをsystem-dependentとし、Phiの一例を提示する。
functional choice・differentiability・response coefficientが事前に必要。
S07:57のI→Phi→J→Iはstateを更新するdynamical feedbackであり、命題の証明loopではない。

S08:45のstable-state basin説明、S13のreturn tendency対応、S14:110–113のtoy interpretationは
potential/returnの解釈を再使用する。しかし「observed stable regionを先に選び、それに合うPhiを逆算し、
そのPhiで同じregionの存在を導いた」とするprocedureはlocateしない。
CIR-07はINTERPRETIVE LOOPに留め、functionが未指定という理由だけで
claim-threatening circularityを作らない。codeにPhi/F fieldがないことも無効性の根拠にしない。

### sigma

S07:24はlocal generation rate、S08:33はgene-related generation、S09:26はtheta-constrained sourceと記述する。
generic balanceにはsource-term slotがあり、Bio specific productionという意味が付く。
balanceを代数的に読み替えれば残差として扱えることと、sourceが実際に残差推定でsigmaを
定義・検証したことは別である。後者の手順はlocateしない。
具体gene-event function/measurementは未指定、toy sigma_Mだけは事前に作る独立source array。
productionを表すslotをproductionと呼ぶCIR-08はdefinitionであり、
その命名がproduction mechanismの発見となったとは認定しない（CON-04）。

## 6. DNA / threshold preload

sのalphabet/length、thetaのparameter space、gene-event categories、response signature、
theta_kおよびA/B/Cという分類名が先に置かれる。
S08:69はthetaをhistorically stabilized constraintと読むが、
具体organismのthetaの起源をderiveしないとも明記する。
codeにsequence inputやtheta(s)を算出する処理はなく、editable constantsをDNA-likeと呼ぶ。

「desired outcome→parameter fitting→再現→DNA説明」という経路は、
定数が手設定であることだけでは確定しない。
調べたsource/code/READMEにはそのfitting・selection手順が表示されないのでCIR-09はUNRESOLVED。
選択履歴が不明なことを、意図的tuningや未調整の証拠のどちらにもしない。

BIO-EQ-15はfield値をthresholdでA/B/Cへ分類する。生物学的cell fateという名前を付ける部分と、
independent morphology同定を分ける。S09:53–57にはobserved morphologyとの接続文があるが、
同じlabelを独立confirmationとして再投入する実際の測定手順は表示されない。
CIR-10はLABEL-SELECTION LOOP / INTERPRETIVE LOOP。
thresholdの形式的分類を、経験的なcell-fate discoveryとも、その不可能性とも判定しない。

working signature省略（34/35）とprobability版差（33）はPhase 01のまま維持する。
省略を使ってtheta依存が消えた、または新しいloopが増えたと推定しない。

## 7. Life-attractor preload

### Conditions defining / characterizing the life region

| Condition | Source | Prior criterion or claimed dynamics? | Boundary / identity distinction |
|---|---|---|---|
| state components include biology/environment | S10:7–17 | representation selected before F trajectory | variable selection≠endogenous region boundary |
| boundedness / viable range | S10:29; S19 life §7.3 | life descriptionのcriterion | numerical bounds / membership未指定 |
| nonstatic / non-divergence | S10:29 | admitted motionのcharacterization | label criterionをstability resultとしない |
| internal progression | S10:25,29 | rho/tauを使うinterpretation | physical clock criterionではない |
| return after moderate perturbation | S10:37 | regionを名付けるproperty | perturbation scale、return test、region選定法は未具体化 |
| system/environment interaction | S10:39 | region “not externally imposed”というsource claim | actual region boundaryかrepresentation selectionかは別問い |
| matter/energy exchange | S10:43 | non-equilibrium persistenceのdescription | flux/organism boundaryのoperational ruleではない |
| developmental convergence / sub-regions | S10:47,51 | interpretation / may exist | subset命名と具体region構成を分離 |
| robustness / regeneration | S10:55 | return / reconstructionのexplanatory usage | small-return conditionとlarge-disturbance reconstructionは別 |

boundednessやreturnは「life」という語なしでも述べられる条件だが、
どのrangeが生物学的viableなのかを独立に決めるprocedureは未表示。
従ってlife-like条件→Omega_life命名→lifeの記述という再使用はlocateする。
S10のDefinition of Lifeという明示的立場ではCIR-11はBENIGN / DEFINitional。
これを独立した生命生成の証明として扱う必須推論経路は確定しない。

“not externally imposed”はsourceがregion formationへ付けた述語であり、
今回その成立を判定しない。少なくともstate coordinates、選んだproperty、model parametersは既に置かれる。
それらとregionの形状が力学的に形成されるというclaimは、対象が違うので直ちに矛盾しない。
toy clipping境界・eye windowをそのままOmega_life境界とするmapもlocateしない。

### All attractor usage families carried forward

Phase 02 §11のAT-01–15 / 28files・113 matching-line locatorを母集団として保持する。
build入力名やsummary repriseを新しいattractor objectとして増やさない。
以下は全15familiesのpreload / explanatory-use check。JA workingを本稿へ統合しない。

| AT family | Prior object / condition | Use checked / source | Circularity handoff |
|---|---|---|---|
| AT-01 intuitive stable region | repeated return / recognizable form | S05、JA intuitive | CIR-11/12、直観的命名 |
| AT-02 core attractor | remain / return criterion | S07:69、JA/working core | CIR-11、定義条件 |
| AT-03 gene stable configuration | theta/threshold/dynamics | S08:57、JA/working gene | CIR-10、labelから同定への移行 |
| AT-04 morphology | stable configuration / convergence | S09:55–61、JA/working development | CIR-10/12、説明再使用 |
| AT-05 life attractor | bounded returning region | S10:33–39、JA/working life | CIR-11、命名と内生claim別 |
| AT-06 viable range | constrained motion / tau progression | S10:29、JA/working life | CIR-02/11 |
| AT-07 non-equilibrium | exchange / sustained organization | S10:43、JA/working life | CIR-11、life解釈 |
| AT-08 developmental convergence | initial conditions / target region | S10:47、working life §7.6 | CIR-12 |
| AT-09 sub-attractors | containing life region / smaller stable region | S10:51; VR-07 | CIR-11/13、mayとworking直述は別 |
| AT-10 regeneration | return / reconstruction after larger disturbance | S10:55; S19 §7.8; VR-08 | CIR-13、再構成を定義済みreturnと同一視しない |
| AT-11 probability target | region/event selection | S11、JA/working probability | CIR-15 |
| AT-12 second attractor | history/reference/reuse/sharing | S12、JA/working intelligence | CIR-14/15 |
| AT-13 note analogy | return/preserving formという対応 | S13、working note | CIR-07、literal translationでない |
| AT-14 toy attractor-like | field patterns / model labels | S14:113–115、S22、JA toy | CIR-17/18/19 |
| AT-15 future region | concrete I/J/Phi/regionを今後特定 | S16:37、working discussion | CIR-03/07、現在の構成としない |

abstract/conclusion/README/handoffのlife/second-attractor repriseは上記05/12/14のsummary。
このmanifestは源泉のusage coverageであって、新しいPDF distribution照合ではない。

## 8. Attractor / robustness / regeneration circularity

S07:69とS10:37はreturn性を用いてregionをattractorと呼ぶ。
S09:61とS10:55はattractor propertyからrobustnessを説明する。
戻るという性質を仮定した条件文「その性質があれば戻る」はdefinitionの展開として読め、
それだけではvicious circularityではない。

注意すべき往復は「生物的robustnessを見てattractorを同定した後、
同じrobustnessをattractorだけで独立に導出したと扱う」場合である。
sourceには前者を実行したregion-selection / fitting手順が表示されず、
generic property statementとbiological interpretationがある。
本phaseはCIR-12をINTERPRETIVE LOOPとし、独立性・proof/stabilityのevidence採点は行わない。

regenerationはS10:55でlarger disturbance後のattractor reconstructionと読む。
moderate perturbationからのreturnを定義しただけで、region再構築まで
定義上含まれると読み足さない。CIR-13はinterpretive extension。
JA self-contained manuscriptには同独立subsectionがなく、working JA §7.8は「導かれる」と書く。
VR-08のscope差を保存し、弱い版を強い版へ自動適用しない。

## 9. Toy-model forcing / initial-condition preload

| Construct | Imposed? | Dynamically generated? | Biological interpretation attached? | Circularity risk |
|---|---|---|---|---|
| square grid / edge-copy boundary | YES | grid/boundary自身はNO | embryo-like domain | computational boundaryとorganism境界を混同しない |
| sigma_M central_band | YES、center .5 / width .035、vertical taper .35 | sourceは固定、Mはupdate | localized morphogen production | source位置をoutput発見としない |
| sigma_M left_edge | YES、band8 / strength .20 | sourceは固定 | alternative morphogen source | boundary flux条件とsource支持を分離 |
| eye_window modes | YES、selected Gaussian preference | windowは固定、Eはupdate | coarse positional cue / eye-like | CIR-17、§10 |
| zeros M/N/B/E | YES | initial値はNO、以後update | initial undifferentiated toy state | no completed output array読み込み |
| random I | YES、seed7 / scale1e-4 | RNG sample、biological fluctuation測定ではない | small perturbation | selection履歴は未指定、tuningと推定しない |
| D / decay / coupling / eta | YES、fixed numerical values | constantsの学習なし | DNA-like parameters | theta(s)からの生成としない |
| threshold / sigmoid slopes | YES、N/B slope8、E slope20 | gate値はcurrent inputsから計算 | commitment labels | label/threshold選択≠生物的発見 |
| clip N/B/E | YES、0..1 | arraysはupdate、bounds固定 | bounded commitment | viability / return theoremでない |
| enable_eye / source / eye modes | YES、switch/CLI | experiment configuration | alternative toy conditions | independent interventionの実行を本phaseで推定しない |
| G / G_norm / B | extraction/normalization/rateはYES | G再計算、B蓄積 | boundary stabilization | §11、CIR-18 |
| observation masks / frames | YES、.5 threshold / scheduling | displayed values依存 | numerical observations | §12、CIR-20 |

更新はsource→M→I→N、およびI→G_norm→B、N/B/window→Eの依存を持つ。
同時に各fieldのold stateを次stepへ渡す。これはfinite iterative feedbackであり、
未来のoutputを前提に同じoutputを論証する構造ではない。
codeにはfinal N/E描画を初期値としてloadする処理はlocateしない。
ただしこの事実から「幾何学的inputが全くない」とは結論しない。

## 10. Eye-window audit

S21 make_eye_windowはloopの前にpositional arrayを作る。
default central_band_window（central_pairはalias）はvertical middleを好むGaussian、
edge_pairは二つのvertical centers、single_pairは追加horizontal preferenceを持つ。
中心・width・modeはoutputから計算するものではない。

S22はwindowがpaired eye shapeそのものではなく、central windowとboundary fieldの組合せによる
toy commitmentだと明記する。従ってsourceのscopeを「完全にspontaneousな位置形成」へ強めない。
反対に、window単体に最終Eの全構造が書かれているとも言わない。
EはN/Bとwindowを入力に継続updateされる。

厳密にはGaussianとlogisticはsmooth weightであり、hard binary supportではない。
S14:62の“only where ... active”という説明を、window外ではEが必ず厳密にゼロという数学的主張に読み替えない。
.5 contourは後段のdiagnosticである。
位置選好はOUTPUT-LOCATION PRELOADED、最終細部やpaired pattern全体とは別。
S14:5,76とS02:473の“geometry not explicitly encoded”はcompleted drawingについての読みと、
位置条件も無いという読みを区別すべきsource文脈として記録する。

CIR-17はimposed positional cue→localized update→eye-likeという解釈の再使用。
sourceはconstrained toy / structural possibilityを併記し、window位置そのものを
独立に発見したとする必要な論証はlocateしない。
したがってserious circularity candidateに固定せずINTERPRETIVE LOOP。
position preloadingの記録はempirical adequacyやclaim downgradeではない。

## 11. Boundary-field audit

Bはgrid edge、膜、cell fate label B、life-region boundaryと別object。
paperはraw gradient G、codeはG_normを入力にBをupdateする。
gradient-sensitive extractionとthreshold/rateは先に設計されたconstructionなので、
境界らしさの一部（空間変化を選ぶという情報）はpreloadされる。
B配列の値・時間経過・細かなshapeまで事前指定されたとはしない。

| Phase-02 role conflict | Current source contrast | Phase-03 classification | What is not concluded |
|---|---|---|---|
| VR-11 | S15:18 gradient magnitude “defines ... B”; S14:49–59 / S21はGからBを更新 | diagnostic / accumulated state / boundary labelの解釈圧縮、CIR-18 | B=Gというidentity、膜生成、数学的無効性は認定しない |
| VR-12 | S14:89 / S15:94 compact N→B; S21はI→G_norm→B | order / dependencyの混同可能性、CIR-19 | NをBの入力へ補わず、feedback loopを捏造しない |

S14:81 / S15:18,57にはboundary structure / boundary-like regionという形成の語がある。
数理的boundary-sensitive constructionとbiological membrane形成を同じclaimへ拡張しない。
code Bが既存Nの境界を直接detectする処理でもない（共通のIがある）。
CIR-18のlabel-selectionはinterpretive、N→Bの問題自体はdirected dependencyの所在差で
circularityではない。source修正・simulation再設計は行わない。

## 12. Simulation-observation audit

S15はnumerical run、not specific biological process、not biological mechanism / structural possibilityと限定する。
S21のmean/max/fraction、mask、RGBはmodel arrayを入力とし、生物学的観測データを入力していない。
ここでの「observation」はnumerical observationとしてsource-localに読む。

preassigned biological label→array pattern→plot labelの繰返しはあるが、
plotを別の生物測定としてモデルへ戻す経路はlocateしない。
fraction>.5は選択規則、raw arraysはmodel state、RGBはdisplay transform。
G_normだけはB updateへ渡るのでdisplay-onlyとは扱わない。

「model verification」「structural witness」という用途の記述とempirical confirmationは別。
本phaseでは実行検証もempirical evidence gradingも行わない。
下流の“confirmed in Bio simulation”は§13のattributionとして別記し、
Bioの限定文を消したり、その限定だけで下流をfalseと判定したりしない。

## 13. Upstream / downstream dependency loops

### Upstream OPEN inheritance

上流[frozen 06](../ved_equation_audit/06_final_audit_record_v1.0_ja.md)の8 OPENを保持する。
「間接関連」はPhase 00 §7の5件であり、Bioが上流bridgeを直接実行しているという意味ではない。
分類語はBIO-LOCAL REDEFINITION / PROPOSED CORRESPONDENCE / SILENT INHERITANCE / DEPENDENCY UNRESOLVED。
今回SILENT INHERITANCEを確定する例はlocateしない。

| Upstream OPEN | Bio relevance / source | Classification | Completion assumed / new bridge? |
|---|---|---|---|
| RC-005 Cij→C field | S04:15のIFGT CとBio Iの対応 | BIO-LOCAL REDEFINITION; PROPOSED CORRESPONDENCE | 非同一明記、matrix-to-field mapなし |
| RC-006 Jij→vector J | S06/S08のBio-local current / events集約 | BIO-LOCAL REDEFINITION; DEPENDENCY UNRESOLVED | VED matrix使用をlocateせず、Bio event集約を上流bridgeとしない |
| RC-007 rhoi→rho field | Bio rhoはprogression、上流densityと別signature | DEPENDENCY UNRESOLVED（直接使用locateせず） | 同glyphから使用・完成を推定しない |
| RC-008 distance→metric | Bio R3 / gridはsupplied representation | DEPENDENCY UNRESOLVED（直接使用locateせず） | metric再構成をBioが実行したとしない |
| RC-009 microscopic rate→sigma | S07/S08 Bio source、toy sigma_M | BIO-LOCAL REDEFINITION | gene-source slotはupstream projectionでない |
| RC-010 L carriers→tensor | Bio boundary / quasi-closure prose | DEPENDENCY UNRESOLVED（直接使用locateせず） | Bをclosure tensorとしない |
| RC-040 tau / VED time | S06/S10/S12 internal progression | BIO-LOCAL REDEFINITION; PROPOSED CORRESPONDENCE | source-local t/rho導入はtime translationを閉じない |
| RC-041 VED / IFGT sigma | S04/S16 IFGT correspondenceとBio source | BIO-LOCAL REDEFINITION; PROPOSED CORRESPONDENCE | same-process identityを自動継承しない |

Bioでsource-localに再定義することは、未完成bridgeの正当/不当な回避と直ちに判定しない。
継承しているのが語彙・role・形式か、carrier identityかを分離する。

### Downstream direction check

以下の全DOWN-01–08はPhase 00から引継ぎ、受け取りの方向だけを監査する。
引用語をこのrecordの生物学的結論として採用しない。

| Dependency | Current locator | Direction / interpretation found | Return to Bio as independent support? |
|---|---|---|---|
| DOWN-01 consciousness | [EN SSO](../../consciousness/sections/sso.tex):9–23、[JA SSO](../../consciousness/sections_ja/sso_ja.tex):10–18 | Bio life / toy chain→fast/slow necessary / confirmed→SSO grounding | Bio sourceがSSOを使い元claimを証明する帰路はlocateせず |
| DOWN-02 projected windows | [formal mapping](../../consciousness/sections/formal_mapping.tex):55–65、[correspondence map](../../consciousness/sections/correspondence_map.tex) | Bio/consciousness/CTは別projected windows、no paper grounds another | groundというDOWN-01の語とのscope差を保持、循環へ統合しない |
| DOWN-03 CT | [CT introduction](../../conceptual-topography/sections/introduction.tex)、[formal mapping](../../conceptual-topography/sections/formal_mapping.tex) | direct Bio継承は未locate、IFGT/関連window比較 | 直接edgeも帰路も推定しない |
| DOWN-04 Intelligence I | [Introduction](../../intelligence-part1/sections/01_introduction.tex):15 | Bio supplies biological vocabulary / four-layer correspondence | reverse proof citation未locate |
| DOWN-05 theta / F | [II preliminaries](../../intelligence-part2/sections/01_preliminaries_ja.tex):121、[inference](../../intelligence-part2/sections/02_inference_operator_ja.tex):21–29 | Bio Fのspecial caseとして下流Fを配置→same glyphをcontinuityの証拠と呼ぶ | CIR-21の局所解釈再使用。Bioが逆引用する経路とは別 |
| DOWN-06 second attractor | II preliminaries:251–260、[stopping](../../intelligence-part2/sections/05_emergent_stopping_layer_ja.tex):67,106 | Bioのhistory/reference条件→L_R / L_E内部記述、same structure | Bioは実装をfuture workへ開く。下流結果からBioへ戻る証明は未locate |
| DOWN-07 inter-individual | [social](../../intelligence-part2/sections/09_social_blockchain_ja.tex):134,165 | Bioが準閉包維持を“示した”→social homology | 元Bio construction所在U14とattributionを分離。帰路未locate |
| DOWN-08 figures / summaries | stopping:100–111のBio emergence例、Phase 00 S36/S37 | upper-attractor / layer examplesとして再掲 | representation再掲だけで相互証明とはしない |

BioのEN/JA本文・working・README/codeでconsciousness/SSO/CT/Intelligence-part、
下流L_F/L_R/L_Eの結果を根拠として戻す引用を検索した。
Bio-local second-attractorのforward referenceはあるが、下流結果を用いた帰路はlocateしない。
ゆえに要求された「Bioを仮定→下流構成→Bioを逆に支持」という全3段のsource-level loopは0。

ただしDOWN-05には、既に対応として選んだFの記号を、対応の根拠として再使用する文章がある。
これはcross-layer inheritanceの**interpretive dependency-loop candidate 1件**（CIR-21）。
数学的Fの同一性を解決したとも、下流理論全体が循環するとも判定しない。
DOWN-01のconfirmed/necessarily、DOWN-07の示したはlater claim/attribution auditへ渡す。

### Phase-00 uncertainty carry-forward

| Phase-00 Open ID | Phase-03 target / classification | Handoff retained |
|---|---|---|
| U01 | PL-07/08; CIR-03/04 | proxy/windowとbiological quantityのmap |
| U02 | PL-04/05; CIR-02 | rho signaturesとclock map |
| U03 | PL-12; CIR-08 | upstream / Bio source identity |
| U04 | PL-10; CIR-05 | event-to-current aggregation |
| U05 | PL-07; CIR-03 | observation / coarse-graining selection |
| U06 | PL-11; CIR-07 | functional/sign specification |
| U07 | PL-13/24; CIR-09 | parameter origin / fitting procedure未表示 |
| U08 | PL-16/17; CIR-11/12 | life membership / viable criterion |
| U09 | PL-25; CIR-18 | Bと膜 / organism boundary |
| U10 | PL-26; CIR-20 | model diagnosticとobservable |
| U11 | PL-06/24/25; CIR-16/18/19 | paper/code / figure-run differences |
| U12 | PL-14/20; CIR-09/15 | working signature/probability意図未固定 |
| U13 | PL-19/26; CIR-22 | fast/slow attributionの元diagnostic所在 |
| U14 | PL-19; CIR-21/22 | second-attractor / inter-individual claim attribution |
| U15 | PL-07/18; CIR-07 | L1 noteの具体source identity |
| U16 | PL-26; CIR-20 | GIF/alternate output lineage、今回再実行・再検査なし |

## 14. Boundary matrix

BND IDsはPhase 00の9対象を維持する。Status列はboundaryの置かれ方でありpass/failではない。

| Boundary ID | Boundary object | How defined | Who/what selects it? | Dynamic? | Biological identity claimed? | Status |
|---|---|---|---|---|---|---|
| BND-01 | observational window | biological coarse description、filter/scale具体法未表示 | describing/observing choice、主体手順未指定 | changing window procedure未表示 | Bio proxy内のwindowと記載 | REPRESENTATION DEPENDENCE / selection unresolved |
| BND-02 | R3 / external t | coordinate domain declaration S06:7,47 | formulation | field動的、domain生成なし | biological representation、organism shapeではない | SUPPLIED REPRESENTATION |
| BND-03 | Omega_life region | bounded/viable/return criterion S10:29–39 | criteriaは本文、regionはinteractionからformedと主張 | source claims YES | lifeと命名 | DEFINITION / claimed endogenous region; selector unresolved |
| BND-04 | system/environment | matter/energy exchange S10:11,39,43 | state component / system切出し | coupling継続と記述 | biological system/environment | INTERPRETIVE INTERFACE / operational boundary unresolved |
| BND-05 | complete / quasi-closure | IFGT vocabulary S04/S11/S16 | cross-layer interpretation | persistence/updateと記述 | life correspondsと記載 | PROPOSED CORRESPONDENCE / no membrane map |
| BND-06 | grid exterior | finite square + edge-copy padding | code/domain choice | boundary固定 | embryo-like labelのみ | IMPOSED COMPUTATIONAL BOUNDARY |
| BND-07 | source support / window | modes、coordinates、bands/Gaussians | parameter/CLI selection | profile固定、response動的 | morphogen / eye-like cue | IMPOSED FORCING / POSITIONAL PREFERENCE |
| BND-08 | B boundary-like field | gradient / normalization / thresholded accumulation | extraction/rate固定、I/B値更新 | YES as model field | boundary stabilization、membrane identity未表示 | DERIVED / UPDATED FIELD + INTERPRETIVE LABEL |
| BND-09 | commitment/display cut | clipping0..1、mask>.5、contour/RGB | code/display choices | selected area随state変化、rule固定 | neural/eye model labels | IMPOSED RULE / STATE-DEPENDENT DISPLAY |

Gaussianの「window boundary」はcompact supportの硬い境界でなく、位置選好の幅。
BND-06のzero-flux stencil、BND-07のsource位置、BND-08のinternal field、
BND-09の表示cutを同じboundaryとして扱わない。

## 15. Circularity ledger

「候補」は検査に投入した可能なloopを意味する。疑問符付きの帰路は監査仮説であり、
sourceにその手順があるという主張ではない。22検査項目のうち最終statusを
CIRCULARITY CANDIDATEとして残すものは0。INTERPRETIVE LOOPはsource上の意味再使用を保存する分類。
将来、独立導出としての使用経路が確定すれば、後続claim auditで再検討する。

| Circularity ID | Candidate loop | Source | Type | Is loop actually required by source? | Current status |
|---|---|---|---|---|---|
| CIR-01 | geometry / operator→field description | S06:7; S21 laplacian | NO CIRCULARITY LOCATED | 生物形状からdomainを逆導出する経路なし | NOT CIRCULAR |
| CIR-02 | t/state/rho→tau→internal progressionという命名 | S06:47–51; S10:21–29 | DEFINITIONAL SELF-REFERENCE | 定義relative to t。tau→rhoの逆定義は表示なし | BENIGN / DEFINitional |
| CIR-03 | chosen window→I/proxy→同じwindow選択を正当化? | S04:15; S16:31–37; U05 | CIRCULARITY STATUS UNRESOLVED | window selection手順と結果による再選択は未表示 | UNRESOLVED |
| CIR-04 | constraint/concentrationをIと呼ぶ→Iでbiologyを記述 | S06:15; S09:13–17; CON-01 | INTERPRETATION LOOP | descriptionの再使用はある、独立同定の証明loopは必須でない | INTERPRETIVE LOOP |
| CIR-05 | events→Delta I/J→eventsを逆同定? | S08:21–33; U04 | CIRCULARITY STATUS UNRESOLVED | aggregation/measurement procedure未指定、逆同定経路未固定 | UNRESOLVED |
| CIR-06 | I→Phi→J→redistributed I | S07:55–57 | ITERATIVE FEEDBACK | sourceがdynamical loopを明記、命題の相互証明ではない | FEEDBACK, NOT CIRCULAR |
| CIR-07 | stable region→restoring Phiという読み→stable region説明 | S08:45; S13; S14:110–113 | INTERPRETATION LOOP | return interpretationの往復はある、Phiを結果からfitする手順なし | INTERPRETIVE LOOP |
| CIR-08 | production slot sigma→local generationという命名 | S07:24; S08:33 | DEFINITIONAL SELF-REFERENCE | 意味付けの反復、independent production mechanismを定義だけで証明したとは固定しない | BENIGN / DEFINitional |
| CIR-09 | desired morphology→theta tuning→morphology説明? | S08:69; S21 constants; U07 | CIRCULARITY STATUS UNRESOLVED | 選択/fit手順未表示。手設定だけから望む結果への調整を推定しない | UNRESOLVED |
| CIR-10 | threshold regions→A/B/C→cell fate / morphology | S09:44–57 | LABEL-SELECTION LOOP | label選択とbiological namingはある、独立confirmationとして戻す手順なし | INTERPRETIVE LOOP |
| CIR-11 | bounded viable returning motion→Omega_life→life記述 | S10:27–43 | DEFINITIONAL SELF-REFERENCE | Definition of Life / We callと明示、independent discoveryの論証とは別 | BENIGN / DEFINitional |
| CIR-12 | returning region→attractor→robustness follows | S07:69; S09:61; S10:37,55 | INTERPRETATION LOOP | returnについてのconditional rephrasingあり、biological独立導出の帰路未固定 | INTERPRETIVE LOOP |
| CIR-13 | return / region reconstruction→regenerationと読む→attractor説明 | S10:55; S19 life §7.8; VR-08 | INTERPRETATION LOOP | large-disturbance reconstructionは解釈、return定義の自動結果としない | INTERPRETIVE LOOP |
| CIR-14 | history/reference/sharing条件→second attractor→intelligence | S12:11–21,37–45 | INTERPRETATION LOOP | 追加条件のconcept再使用、Bio内部で認知実装の証明はしない | INTERPRETIVE LOOP |
| CIR-15 | life/second targetを選ぶ→そのtargetの確率を名付ける | S11:19–37; S12:25–29; EQ21/33 | DEFINITIONAL SELF-REFERENCE | 対象再定義とschematic factor、numerical discoveryではない | BENIGN / DEFINitional |
| CIR-16 | old array→next array→next iteration | S21 run_simulation / EQ24–46 | ITERATIVE FEEDBACK | actual finite recurrence、結果を論証の前提へ戻す構造でない | FEEDBACK, NOT CIRCULAR |
| CIR-17 | eye-specific cue→E localization→eye-like interpretation | S21 make_eye_window; S14:62–82; S22 Toy Eye | INTERPRETATION LOOP | 位置選好あり、completed eye全体・independent positional discoveryはsourceも同じとしない | INTERPRETIVE LOOP |
| CIR-18 | gradient-sensitive rule→B→boundary-likeという読解 | S14:49–59; S15:18; VR-11 | LABEL-SELECTION LOOP | edge-sensitive constructionをboundary labelで再記述 | INTERPRETIVE LOOP |
| CIR-19 | compact N→B vs I→G_norm→B | S14:89; S21; S22; VR-12 | NO CIRCULARITY LOCATED | 依存/sequenceの相違であり帰路ではない | NOT CIRCULAR |
| CIR-20 | arrays→mask/plot/statistic→numerical observation | S21 plotting/print_summary; S15:111–113 | NO CIRCULARITY LOCATED | 表示をempirical dataとして更新に戻す経路なし | NOT CIRCULAR |
| CIR-21 | Bio Fの対応として下流Fを置く→same glyphをcontinuityの根拠と読む | DOWN-05; II inference:21–29 | INTERPRETATION LOOP | 下流局所の解釈再使用あり、Bioへ戻る実証/証明ではない | INTERPRETIVE LOOP |
| CIR-22 | Bio attribution→SSO / intelligence→Bioを逆支持? | DOWN-01/02/04/06/07/08 | NO CIRCULARITY LOCATED | 前半の引用はあるがBioで逆引用する帰路はlocateせず | NOT CIRCULAR |

### Vicious-circularity test

各候補を(1) Xの定義がYに依存、(2) Yが独立に利用可能、
(3) Yを後にXから導出したと主張、(4) Yのpreloadでその導出が空になる、
(5)単なる相互力学、(6)定義か説明か、(7)独立criterion/intervention/observationの所在、
の順に確認した。1+3+4が**同じclaim targetで**materialに成立する場合だけserious candidateに残す。
「具体化なし」は(2)/(7)の未指定であって、(3)/(4)を肯定する根拠ではない。
特に混同しやすい3群を次に展開する。証拠の十分性を採点する表ではない。

| Test | CIR-11/12 life / return | CIR-17 eye location | CIR-21 downstream glyph |
|---|---|---|---|
| 1: X defined using Y? | YES、life/attractor命名にboundedness/returnを使う | YES、E ruleにpositional cueを使う | YES、FをBioのspecial caseとして記述 |
| 2: Y independent? | criterionはproseで先に表示、具体life判別法は未指定 | code入力としてwindowは独立に表示、biological cue同定は別 | glyph選択は表示、cross-layer identity mapは別 |
| 3: Y later derived from X? | returnのconditional言い換えあり、独立life導出とは固定できない | localized patternの形成記述あり、入力位置そのものの独立導出とは固定できない | continuityの根拠という文はあるが、数学的identity導出とは分離が必要 |
| 4: derivation empty if preloaded? | returnの言い換え部分のみ、life/regeneration全体とは異なる | 位置選好の部分のみ、E全patternはinputではない | glyph同一の部分は選択の反復、theory continuity全体の成立判定は範囲外 |
| 5: mutual dynamics only? | region propertyは命名、I/Phi/J feedbackは別CIR-06 | finite E updateはあるがwindow自体は固定 | dynamicsのfeedbackではない |
| 6: definitional or explanatory? | definitionとbiological interpretationを分離 | constrained formationとeye-like命名を分離 | local interpretive supportの再使用 |
| 7: independent loop-breaking procedure located? | operational membership/perturbation selector未指定 | mode switchesはあるが独立生物criterion/intervention結果はここでlocateせず | Bioへの逆引用・independent translationはlocateせず |
| Retained result | BENIGN definition / INTERPRETIVE LOOP、serious0 | INTERPRETIVE LOOP、location preloadを保存、serious0 | INTERPRETIVE LOOP、downstream handoff、serious0 |

CIR-07のpotential逆算、CIR-09のdesired-outcome fitting、
CIR-22のBioへの逆引用も、sourceにない帰路を追加しないためserious candidateにしない。
独立criterionの有無をここで問うのは循環の経路確認であって、empirical adequacy判定ではない。
**no source-level vicious circularity established**。
これはBioが正しい・完全・非循環と証明されたという結論ではない。

### CON coverage / later-audit handoff

| Phase-02 Conflation ID | Preload / circularity result | Later inquiry retained |
|---|---|---|
| CON-01 | PL-07/08/09; CIR-03/04 | window/proxy/biological identity |
| CON-02 | PL-10; CIR-05 | events / currentの同定手順 |
| CON-03 | PL-11; CIR-06/07 | functionalとrestoring interpretation |
| CON-04 | PL-12; CIR-08 | source slotとproduction mechanism |
| CON-05 | PL-04/05/06; CIR-02 | recording / progression / biological clock |
| CON-06 | PL-13/14/24; CIR-09 | DNA mapとnumeric parameter provenance |
| CON-07 | PL-14/15; CIR-10 | thresholds / cell fate / morphology |
| CON-08 | PL-16/17; CIR-11 | life-region criterionと同定 |
| CON-09 | PL-18; CIR-12/13 | definition / robustness / regeneration |
| CON-10 | PL-19/20; CIR-14/15 | second-attractor conditions / probability target |
| CON-11 | PL-15/25; CIR-19 | stage order / actual dependence |
| CON-12 | PL-03/25; CIR-18 | G / G_norm / B / membrane |
| CON-13 | PL-26; CIR-20/22 | numerical observations / downstream confirmation |
| CON-14 | PL-02/21/22/23; CIR-16/17 | forcing / initial / positional constraints |
| CON-15 | PL-11; CIR-07 | interpretive J/Phiとactual finite model |

## 16. Preload-vs-emergence matrix

分類はpreloadの内容比較であり、emergenceの成立・不成立やevidence gradeではない。
主statusは各行1つ。PARTIAL STRUCTURE PRELOADEDの件数とOUTPUT-LOCATION PRELOADEDの件数を別に数える。
「完成形が入力されていない」と「output-defining informationが部分的に入力されている」は両立する。

| Claim | Output claimed | Relevant preloaded structure | Does preload already contain output-defining information? | Status |
|---|---|---|---|---|
| EM-01 morphogenesis (S09/S14) | stable differentiated pattern | field geometry、RD form、sources、threshold categories | spatial/response条件の一部。completed patternとは別 | PARTIAL STRUCTURE PRELOADED |
| EM-02 boundary formation (S14/S15) | boundary-like B | gradient extraction、G_norm、threshold/rate | spatial variationを選ぶ条件が含まれる、膜の全構造ではない | PARTIAL STRUCTURE PRELOADED |
| EM-03 neural-like structure (S14/S22) | N region | central source / I coupling / threshold / neural label | spatial biasとclassification rule、最終N配列ではない | PARTIAL STRUCTURE PRELOADED |
| EM-04 eye-like location (S14/S22) | E localized preference | eye_window centers/width/mode | YES、coarse positional information。smooth weightでありhard supportとは別 | OUTPUT-LOCATION PRELOADED |
| EM-05 eye-like pattern (S14/S22) | finer / paired E organization | N/B gates、position cue、source、rates | 条件の組合せの一部、completed eye形状ではない | PARTIAL STRUCTURE PRELOADED |
| EM-06 life attractor (S10) | life as bounded sustained region | viable/return/continued-update criteria、state choice | outputをlifeと呼ぶ基準が先にある、具体region constructionは別 | CLAIM DEPENDS ON PRELOAD |
| EM-07 regeneration (S10:55) | reconstruction after larger disturbance | return-region vocabulary、disturbance / reconstruction meaning | 小摂動returnと大擾乱再構築は同一でなく、後者の具体操作は未固定 | UNRESOLVED |
| EM-08 second attractor (S12) | history-based intelligence | history/reference/reuse/sharing、life region | 概念条件の一部、implementation全体ではない | PARTIAL STRUCTURE PRELOADED |
| EM-09 fate identification (S09) | A/B/C as cell fate | interval labelsとbiological naming | YES、分類名。observed biological fate mapとは別 | OUTPUT-LABEL PRELOADED |

EM-04と05は同じeye claimのlocation/pattern sub-targetであり、二つの独立実験ではない。
partial5、location1、claim-depends1、unresolved1、label1、計9sub-target。
OUTPUT NOT PRELOADEDを0とするのは、いずれかのdomain/rule/criterionが関わるこの母集団での分類であり、
すべての完成outputが入力済みだという意味ではない。

## 17. Phase-03 outcome

### Counts and denominator

| Count unit | Count / result |
|---|---|
| Preload entries | 26 (PL-01–26)、typeは複数可 |
| Boundary entries | 9 (BND-01–09)、全件継承 |
| Circularity inspection candidates | 22 (CIR-01–22)、疑問形の仮説を含む検査母集団 |
| Retained CIRCULARITY CANDIDATE status | 0 |
| Benign definitional loops | 4 (CIR-02/08/11/15) |
| Feedback-only cases | 2 (CIR-06/16) |
| Interpretive loops | 9 (CIR-04/07/10/12/13/14/17/18/21) |
| NOT CIRCULAR cases | 4 (CIR-01/19/20/22) |
| Unresolved circularity | 3 (CIR-03/05/09) |
| Serious claim-threatening candidates | 0; source-level vicious circularity established 0 |
| Preload / emergence sub-targets | 9; PARTIAL STRUCTURE PRELOADED 5 |
| Output-location preload | 1 (EM-04)、whole output encodingという意味ではない |
| Output-label preload | 1 (EM-09) |
| Upstream OPEN reviewed / implicated | 8 preserved / 5 indirect (RC-005/006/009/040/041) |
| Downstream dependency-loop candidates | 1 interpretive (CIR-21); complete cross-branch return-proof loop located 0 |
| Coverage | BIO-EQ 48/48; CON 15/15; BND 9/9; Phase-00 U 16/16; VR-11/12 2/2; AT 15/15; DOWN 8/8 |

NOT CIRCULAR 4 + BENIGN 4 + FEEDBACK 2 + INTERPRETIVE 9 + UNRESOLVED 3 = 22。
“circularity candidates 22”という検査母集団と、serious / retained candidate 0という分類結果を混同しない。

### Retained findings / non-results

representation・observation window・threshold・source/window・labelは、各constructionの前に置かれる。
region命名、returnの条件説明、数値feedback、biological interpretationの再使用は別の依存である。
特にeye位置情報、gradient-sensitive B、lifeのviability/return criterionを記録した。
これらから「生命が生成された / 生成されない」「Bioはvalid / invalid」「実証された / 不十分」
という判定へ進まない。wrong/cheating等の評価語もsourceへ付与しない。

未固定のselector・aggregation・parameter選択履歴、life/observable mapping、下流attributionは
後続Phase 04–05への問いとして残す。revision actionを選ばず、claimをdowngradeしない。
VR-11/12、working probability/signature differences、上流OPENも解消しない。

### Validation / write boundary

新規record / READMEのlocal links 37 / 7件、source paths、fences、display math、
17 / 1 tablesの列数、PL/CIR IDsの一意性、48 BIO-EQ / 15 CON / 9 BND / 16 U / 15 AT / 8 DOWN coverage、
参照先IDと集計整合を検査し、error 0。git diff --checkはPASS。
task開始時の既存1,430 filesのSHA-256 snapshotと比較し、既存変更は本枝READMEだけ、
新規は本recordだけ、source変更・削除0を確認した。
既存tracked modifications 96件、untracked research directories 3件を保持。
git diff --statの96 files / +3054 / -1268は今回以前のtracked変更であり、本taskのsource変更ではない。

Phase 03 COMPLETE。Phase 04 claim / evidence burden auditはNOT STARTED。
上流監査 / core revision CLOSED、Bio audit IN PROGRESSを維持。
simulation / source build / web research / commit / pushなし。Phase 04へ進まず停止する。

[Bio audit README](README_ja.md)

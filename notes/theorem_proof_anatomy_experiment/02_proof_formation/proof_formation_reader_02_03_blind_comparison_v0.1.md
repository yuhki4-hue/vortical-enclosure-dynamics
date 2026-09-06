# Reader 02 / Reader 03 Blind Comparison v0.1

**Purpose:** 同一blind packetから独立に作られたReader 02とReader 03のqualitative reconstructionを、parent corpus item E01–E12単位で比較する。  
**Not performed:** adjudication、winner selection、answer-key comparison、framework revision、score、percentage、kappa、ranking、generalization。  
**Files used:** `proof_formation_coder_instructions_v0.1.1.md`、`proof_formation_frozen_toy_corpus_v0.1.md`、`proof_formation_reader_02_claudecode_v0.1.1.md`、`proof_formation_reader_03_v0.1.1.md`のみ。原sourceには戻っていない。

この文書の「一致」は、二つのreader記録が同じtransitionを再構成したという記述であり、そのtransitionまたはcodeが正しいという判定ではない。「差」はreader errorを意味しない。

## 1. Comparison unit

比較単位はparent corpus item E01–E12とする。subepisode数が異なる場合は、次の三関係を区別する。

| Parent | Reader 02 | Reader 03 | Subepisode relation |
|---|---|---|---|
| E01 | E01 | E01 | same transition, same segmentation |
| E02 | E02-a / E02-b。単一episode案もAMBIGUOUSとして保持 | E02-a / E02-b。境界はSOURCE-DERIVED扱い | same transition, same primary segmentation。境界ambiguityだけreader-specific |
| E03 | E03 | E03 | same transition, same segmentation |
| E04 | E04。量化順序確立と内部性撤回への二分案を保持 | E04 | same transition, same primary segmentation。Reader 02のみdifferent-segmentation案を保持 |
| E05 | E05-a＝一般同値撤回＋規約的／条件付き置換、E05-b＝空間的位置の第一義性撤回 | E05-a＝一般同値撤回、E05-b＝規約的同値、E05-c＝条件付きモデル対応 | same transition, different segmentation（一般同値と二置換）。加えてReader 02のE05-bはgenuinely different reconstructed transitionで、Reader 03には独立対応blockがない |
| E06 | E06-a＝case verdict、E06-b＝mechanism名、E06-c＝taxonomy | E06-a＝case verdict、E06-b＝mechanism/taxonomy＋field-native reconstruction | same parent, partially overlapping subepisodes。Reader 02のb/cをReader 03が一blockにまとめる |
| E07 | E07 | E07 | same transition, same segmentation |
| E08 | E08。表現削除／verdict改称への二分案を保持 | E08 | same transition, same primary segmentation。Reader 02のみdifferent-segmentation案を保持 |
| E09 | E09-a / E09-b | E09-a / E09-b | same two-stage transition, same segmentation |
| E10 | E10 | E10 | same transition, same segmentation |
| E11 | E11。technical materialはS2→S2*のresource/witness | E11-a＝S2→S2*、E11-b＝reflection type/subject shift。統合案も保持 | same parent, partially overlapping subepisodes。main label transitionは同じだが、Reader 03だけがtechnical reconstructionを別transitionとして立てる |
| E12 | E12-a＝scalar/S judgment、E12-b＝architecture/A judgment | E12-a / E12-b | same two target claims and same segmentation。E12-bのbefore確定度とmove interpretationが異なる |

一対一対応が成立しないのは主にE05、E06、E11である。以下では、共有テキストを複数の独立結果として扱わず、parent内のoverlapとして比較する。

## 2. Transition-core comparison

判定語は指定された四語に限定する。ここでのcoreは、`claim_before`、principal failure witness、principal withdrawal/demotion、retained side claim/remnant、terminal statusの組合せである。

| Parent | Claim-before core | Principal failure witness | Principal withdrawal/demotion | Retained remnant and terminal status | Qualitative judgment |
|---|---|---|---|---|---|
| E01 | 両者とも、非単射観測写像から新しい一般的「存在論的非一意性定理」を作るclaim | 両者とも、既存のinverse-problem等の基本設定であることと、`O=id_W` | 新しい一般定理／novelty claimをwithdraw | 観測同値と構造同型の区別、model class・experiment family相対のidentifiabilityをestablishedとして保持 | **CORE CONVERGENCE** |
| E02 | 両者とも、self-containment単独からuniversal non-identifiabilityを導くclaim | 十分な内部記憶による有限符号化、無限濃度、quine/Kleene、既存不可能性結果の追加条件 | universal implicationをwithdraw | self-containmentは追加前提を成立させうるというremnantと、有限`X=A×E`のconditional capacity propositionを保持 | **CORE CONVERGENCE** |
| E03 | 両者とも、generation→stabilization→logという段階だけから一般的non-isomorphismを導くclaim | lossを定義に埋め込むこと、可逆／完全符号化countercase、既存の情報比較概念 | stage-existence implicationをwithdraw | concrete channel等についてlossを証明する必要と、Blackwell post-processing対joint physical measurementの区別をestablishedとして保持 | **CORE CONVERGENCE** |
| E04 | 両者とも、二ビット破壊例をinternality自体が生むglobal-separation impossibilityとして使うclaim | matched external observerでも同じ反例、fresh preparationで反例消失、既存adaptive-identification literature | internality-specific useをwithdraw | pairwise `∀∃`とglobal `∃∀`の差をestablished、bridge条件をsetting-dependent/openとして保持 | **CORE CONVERGENCE** |
| E05 | 両者とも、informalな“same interface”から一般internal/external history equivalenceを導くclaim | 規約的同一性と実装存在命題の混線、interface specification不足 | general equivalenceをwithdraw | 完全interfaceを定義した規約的同値と、controlled-transition model＋state mapの条件付き補題を保持 | **PARTIAL CONVERGENCE**。このcoreは一致するが、Reader 02だけがspatial `inside vs outside`の第一義性撤回を別coreとして再構成 |
| E06 | 両者とも、GSTをDeferred Resolutionのpositive case／independent mechanismとして扱う旧claim群 | 系列が反復連鎖をsupportしないこと、Null C/D/E、既存field-native vocabularyでのより正確な再構成 | positive verdictをfrozen negativeへ、mechanism名をrejected historical hypothesisへ、taxonomyをdelete | field-native reconstructionを保持 | **PARTIAL CONVERGENCE**。outcomeは重なるが、taxonomy固有witnessの有無とclaim groupingが異なる |
| E07 | 両者とも、generic auditがfield-native controlより早く／明確にtransfer-lossを診断するH1 | new assumption等を一つも産出せず、judgmentを変えず、presentationだけを変更 | diagnostic/methodological added-value claimをnot supportedとして固定 | organizational/cross-chain visibility valueのみ保持。source-local M0はdefensible、M2/M3はrejected | **CORE CONVERGENCE** |
| E08 | 両者とも、partial preservation／忘却防止というeffectiveness claim | N-04との内部矛盾、reference/use/transmission/forgetting-preventionが未測定 | forgetting-prevention/effectiveness表現をwithdrawまたはuntestedへ | documentary continuity／rediscoverabilityのみ保持 | **CORE CONVERGENCE** |
| E09 | 両者とも、full P1–P5が十分なcodeを前提とするdesign claimと、その後のreduced methodology viability | P0で実質一codeのみ、次にreduced checkを含む二段階でpremise否定 | full designをabandonし、後にcomparative methodologyをterminate | NONEVAL-only reduced checkを一時採用し、最終的にcomparative reviewへdowngrade | **CORE CONVERGENCE** |
| E10 | 両者とも、“closure reversal”がGödel分析の独立分類／diagnostic toolになりうるclaimを判定文から再構成 | standard conceptsよりdiagnostic resolutionが低く、mechanismの発見・区別に使えない | C2/C3への昇格を否定しnegative resultをfix | standard analysis後のcomparative explanatory metaphorとしてC1を保持 | **CORE CONVERGENCE** |
| E11 | main coreでは両者とも、broad S2 “self-assurance” labelをlocal/uniform/global/soundness全域へ広げるclaim | type・language・metalevel差、scope/Γ/base/truth-axiom依存、subject shift | broad S2をS2*へdemote | local reflectionでのみlimited retention | **PARTIAL CONVERGENCE**。main terminal coreは一致するが、Reader 03はtechnical correction自体を追加transitionとして再構成 |
| E12 | scalar coreでは、universal strength scalarをfixed-package calibrationへ限定。architecture coreではevaluated/evaluating theoryを区別しA2とする | equal ordinalがtheorem set等の同一性を含意しないこと、standard metamathematical distinctionでA3に足りること | universal readingをrejectし、A3へ上げない | natural theory family＋fixed packageのS2* calibrationと、stable but standardなA2 architecture featureを保持 | **PARTIAL CONVERGENCE**。after/statusは近いが、E12-bのclaim-beforeはReader 02がUNKNOWN、Reader 03がINFERENCEで補い、moveも異なる |

この比較では、parent-level coreが完全に反対方向へ再構成された`CORE DIVERGENCE`は確認されない。segmentationのためcore自体を比較不能とする`NOT COMPARABLE DUE TO SEGMENTATION`もないが、E05・E06・E11ではsubepisode単位の一対一比較はできない。

## 3. Segmentation comparison

### 3.1 E01–E12 overview

| Parent | Reader 02 segmentation | Reader 03 segmentation | Shared ambiguity | Reader-specific ambiguity | Move codingへの影響 | Terminal statusへの影響 |
|---|---|---|---|---|---|---|
| E01 | single | single | none | Reader 02はsplit案を検討後、非compatibleとして却下 | none | none |
| E02 | two; one-episode alternative retained | two; no alternative | none | Reader 02のみa/b境界をAMBIGUOUS | main codesの配置は同じ。aのM14対M2はboundaryよりoperation interpretationの差 | parent-level statusは同じ。統合案ならwithdrawal、side claim、conditional theoremが一blockに並ぶだけ |
| E03 | single | single | none | none | none except optional M14 | none |
| E04 | single; two-episode alternative retained | single; no alternative | none | Reader 02のみ「quantifier distinction確立」と「internality attribution撤回」のsplitを保持 | primaryでは同じM14/M15/M17。alternativeではmoveが二blockへ分散 | parent-level status不変。alternativeではestablished resultとwithdrawalが別terminal recordになる |
| E05 | two; E05-a内部の二置換split案あり | three; integrated/two-part alternativesあり | general withdrawalと二replacementを一つか複数かは両者ともambiguous | Reader 02のみspatial-location withdrawalを独立E05-b化 | 大きい。M1/M4/M8を一blockへまとめるReader 02に対し、Reader 03はM1/M2/M14とM1/M7/M8/M10へ分配 | general withdrawal、convention、conditional lemmaのstatusは同じ。spatial-location withdrawal statusはReader 02だけに存在 |
| E06 | three; single integrated alternative | two; integratedまたはb再分割alternative | case verdictとmechanism/taxonomy groupingが非一意というambiguityは共有 | Reader 02はtaxonomyを必ず独立primary、Reader 03はmechanismと同一primary | Reader 02はtaxonomyにM17のみ、Reader 03はcombined blockにM15+M17 | negative verdict、mechanism demotion、taxonomy deletionはparent-levelで一致。field-native remnantの付け先が異なる |
| E07 | single | single | none | none | none | none |
| E08 | single; deletion/relabel split alternative | single; no alternative | none | Reader 02のみ二変更案をAMBIGUOUS | primaryでは両者ともM2/M14/M17 | parent-levelは同じ。Reader 02はcontinuity retained/effectiveness open、Reader 03はoriginal claim withdrawn/untested＋continuity retainedとidentityを付け替える |
| E09 | two | two | none | none | same M4/M17 then M17 | same reduced-adopted then methodology-terminated sequence |
| E10 | single | single | none | Reader 02はGödel II metatheoremを別episodeにする案を非compatibleとして却下 | 両者ともM12をmoveにしない。M14対M2のoptional co-code差のみ | none |
| E11 | single | two; integrated alternative retained | none | Reader 03のみtechnical block境界をAMBIGUOUSとして採用 | decisive。Reader 03 E11-bのM6/M12/(M3)は、Reader 02ではresource/analysis object | S2* statusは不変。Reader 03だけがΓ-scopeとexternal stronger-theory claimsへ独立terminal statusを付す |
| E12 | two | two | none | none | E12-aはM13のみ差。E12-bはM15対M12 | scalar S2*とarchitecture A2は同じ。claim-before確定度だけ異なる |

### 3.2 Focused segmentation notes

#### E02

primary segmentationは一致する。Reader 02はExcerpt 4の「残る」をExcerpt 3のremnantと連続させる単一episode案を保持し、Reader 03はconditional propositionの独立assumption setを優先して境界をSOURCE-DERIVEDとした。差はconditional propositionのstatusではなく、`claim_before`の置き方に現れる。Reader 02はwithdrawn universal claimをbeforeとして再利用し、Reader 03は条件付き後継を`OPEN HYPOTHESIS`として立てる。

#### E04

両者のprimary blockは同じ。Reader 02だけが、二ビット例によるquantifier-order differenceの確立と、その例へのinternality attributionの撤回を別transitionにできるとした。Reader 03は同じ例を一つのbefore/witness/after sequenceとして保持した。parent terminal resultは変わらない。

#### E05

一般equivalence、definitional branch、conditional implementation branchについては`same transition, different segmentation`である。Reader 02は一つのE05-aに三つのafterを置き、Reader 03はwithdrawal、convention、conditional lemmaを三blockへ分けた。これに対し、Reader 02 E05-bの「spatial inside/outsideを第一義的数学条件とすることの撤回」はReader 03に独立blockがなく、`genuinely different reconstructed transition`である。

#### E06

Reader 02 E06-aとReader 03 E06-aは直接対応する。Reader 02 E06-b/cはReader 03 E06-bに部分的に重なる。taxonomy deletionをmechanism/prior-art absorptionと同じfailure sequenceに置くReader 03に対し、Reader 02はtaxonomy固有のwitnessをUNKNOWNのまま切り離す。このsegmentation差がM15の適用範囲を変える。

#### E08

両者とも単一blockを採用し、同じwitnessとafter verdictを得る。Reader 02だけが、表現削除とverdict relabelを二transitionにできるとした。差はsource上の二つの変更表をepisode境界と見るか、同一N-04 witnessを共有する一改訂と見るかにある。

#### E10

両者ともGödel I/IIのmathematical contentをframework claimの分析resourceとし、独立subepisodeにしない。Reader 02はこの代替を明示的に検討・却下し、Reader 03は単一episodeのみを記録した。したがってE10のM12不採用はsegmentation上も収束している。

#### E11

最大のboundary-dependent caseである。Reader 02はT+ construction、Löb、subject shiftをS2→S2*を判断するresource/witnessに置く。Reader 03は同じmain blockに加え、untyped self-assuranceからΓ-scoped external reflection theoryへのtechnical correctionをE11-bとして立てる。この追加境界がM6/M12をmoveへ変え、独立after/statusを作る。

#### E12

両者ともS-axisとA-axisを分離するため、segmentationは一致する。差はsegmentationではなくE12-bのbefore reconstructionとoperation identityである。Reader 02はA-ladder欠落のためbeforeをUNKNOWN/AMBIGUOUSとし、Reader 03はA3-worthinessを問うclassification obligationとしてINFERENCEした。

## 4. Move comparison

### 4.1 M1–M17 comparison by operation

この表はcode setの一致数を示すものではない。同じcodeでもepisode boundaryと役割が同じかを区別する。

| Code | Cross-reader relation |
|---|---|
| M1 | **same move under same episode boundary**: E02-bの記録場所・candidate range・finite capacity条件、E12-aのfixed analysis package。E05でも両者がinterface/model条件の強化を認めるが、Reader 02は一般withdrawalと二置換を一blockにまとめ、Reader 03はdefinitional E05-bとconditional E05-cへ分けるため、ここは**different move because boundary differs**を含む。 |
| M2 | **same move under same episode boundary**: E08のeffectiveness→continuity、E11 mainのbroad S2→S2*、E12-aのuniversal scalar→limited calibration。**optional co-code difference**: E02-aはReader 03がM2、Reader 02がM14。E05 definitional branchはReader 03のみM2。E10はReader 03がM2、Reader 02がM14。E07は両者ともM2を最終codingせず、Reader 02だけがAMBIGUOUS候補として明示した。 |
| M3 | **same move under same episode boundary**: E12-aで両者ともformula classの固定をcoding。E11は両者ともM3/M14境界を検出するが、Reader 02はM3をcodingせず、Reader 03はE11-bに`AMBIGUOUS M3`を置く。これは**different move because boundary differs**かつoptional co-code difference。 |
| M4 | **same move under same episode boundary**: E02-bのfinite object/domain、E09-aのNONEVAL限定、E12-aのnatural theory family。E05 conditional branchではReader 02がM4、Reader 03がM7を使い、同じcontrolled-transition restrictionをdomain restrictionとmodel revisionのどちらとして表すかが異なる。 |
| M5 | 両者ともcodingしない。E01のequivalence-class言明について、Reader 02はtarget reformulationではないためM5を明示的に除外し、Reader 03もside-claim distinctionとして扱う。 |
| M6 | Reader 03のみE11-bでexternal reflection extension `T→T+`をcoding。Reader 02は同じ構成をS2* judgmentのproof/evidence resource・analysis objectに置く。**code-versus-resource difference**および**different move because boundary differs**。 |
| M7 | Reader 03のみE05-cでspecified controlled-transition modelへのrevisionをcoding。Reader 02は同じ箇所をM4でmodel-class restrictionとする。**optional co-code difference**だが、M7対M4というoperation typingの差でもある。 |
| M8 | E05 conditional correspondenceで両者ともhistory-length inductionをroute additionとしてcoding。Reader 02ではintegrated E05-a、Reader 03ではE05-cなので、semantic moveは同じだがepisode boundaryが異なる。 |
| M9 | 両者ともcodingしない。Reader 02はE05のpolicy transferがspecified consequence-class reductionではないとしてM9を除外し、Reader 03はstate mapをM10寄りに読む。 |
| M10 | Reader 03のみE05-cのstate mapをexplicit translationとしてcodingし、INFERENCEと明記。Reader 02は同じmapをassumption/resourceとして扱い、M9も採らない。**code-versus-resource difference**。 |
| M11 | 両者ともcodingしない。internal syntax/proof representationをformation moveとするepisodeは両記録にない。 |
| M12 | E10では両者ともcodingせず、Gödel IIのexternal-consistency/metatheorem構造をanalysis object/resourceとするため、**same code-versus-analysis-object resolution**。E11ではReader 03が独立E11-bを作ったためM12をcodingし、Reader 02はmain claimのresourceとして非coding。E12-bでもReader 03はmetatheoryへのevaluation placementをM12、Reader 02はordinal analysisの既存構造というanalysis objectとして非coding。後二者は**code-versus-analysis-object difference**。 |
| M13 | Reader 03のみE12-aでtotal-strength questionをordinal calibrationへreformulateしたmoveとしてcoding。Reader 02はepisode開始時点ですでにordinal calibrationがanalysis objectであり、bridge theorem要求はavailable branchだとして非coding。**code-versus-analysis-object difference**。 |
| M14 | **same move under same episode boundary**: E04のpairwise/globalおよびinternality/resource separation、E05のconvention/existence分離、E08のcontinuity/effectiveness、E11 mainのlocal/uniform/global/soundness、E12-aのcoordinate/equivalence separation。Reader 02だけがE01、E02-a、E03、E10、E12-bの追加disambiguationをcodingし、Reader 03は一部をM2またはside-claim contentに置く。主に**optional co-code difference**。 |
| M15 | **same move under same episode boundaryまたは同じoverlap**: E01、E03、E04、E06 mechanism、E10で既存語彙／標準概念へのabsorptionを両者がcoding。E12-bはReader 02のみstandard metamathematical level distinctionへのabsorptionをM15とし、Reader 03はM12/M14とする。E06 taxonomyではReader 02が固有witness不明のためM17のみ、Reader 03はmechanism blockと統合したためM15がtaxonomyを含むblock全体に及ぶ。 |
| M16 | 両者ともcodingしない。E04、E06、E07、E09、E10等でcomparison/empirical materialはあるが、両者とも当該subepisode内のtheorem/framework targetからのconversionではないと扱う。 |
| M17 | E01–E10の主要withdrawal/demotion/termination、E12-aのuniversal reading rejectionで広く**same move under same episode boundary**。差はE05のspatial-location withdrawalがReader 02だけにあること、E06 taxonomy deletionがReader 02では独立block、Reader 03ではmechanism blockに統合されること。後者は**different move because boundary differs**。 |

### 4.2 Required focus cases

#### E05 definitional branch

両者は、完全interfaceのprotocol/transcript relationを同一と定義した場合のhistory-set equalityを、物理的なequivalence theoremではなくstipulative/definitional resultとして読む点で一致する。違いはoperationの切り出し方である。

- Reader 02: integrated E05-a内でM1を付し、M14はgeneral claimをconventionとexistence theoremへ分けるmove。M2は非coding。
- Reader 03: E05-bを独立化し、M1＋M2＋M14。M2はgeneral physical-sounding claimからconventional conditionalへの弱化を表す。

これは`same transition, different segmentation`と`optional co-code difference`であり、terminal statusは両者とも「definitional/conventional、physical existence theoremではない」。

#### E07 M2

両者ともformation M2を最終codeに含めない。diagnostic valueが失われ、organizational valueだけが残ることは同じだが、これを同一claimのweakened conclusionではなく、失敗したH1と別のretained value claimとして扱う点が一致する。Reader 02はM2をAMBIGUOUS候補として明示し、Reader 03はside-claim identityの違いを理由に採らない。source-local “M2”のrejectionとも混同していない。

#### E10 M12

両者ともM12をcodingしない。Gödel IIが外部整合性仮定から内部文のnon-provabilityを導くmetatheoremであることは、framework claimのformation moveではなくanalysis object／resourceとされる。これはcode-versus-analysis-object境界についての強い収束である。

#### E11 M6 / M12

同じT+ constructionとsubject shiftを読んでいるが、boundaryが異なる。

- Reader 02: S2→S2*のsingle episode。M6/M12はreflection theory側のmathematical operation／resourceであり、formation moveではない。
- Reader 03: E11-bを独立technical correctionとして立てる。そのbeforeをuntyped “same theory assures itself” reading、afterをexternal Γ-scoped stronger theoryとしたためM6/M12をformation moveとしてcoding。

これは`code-versus-resource difference`、`code-versus-analysis-object difference`、`different move because boundary differs`が重なる例である。main S2* statusは変わらない。

#### E12 M1 / M3 / M13 / M12

- M1とM3: E12-aで両者がcoding。notation/base/reduction notionの固定をM1、formula classの固定をM3とする。M4との多重化粒度が難しいという自己記録も共有する。
- M13: Reader 03のみcoding。Reader 02はordinal calibrationを既存のanalysis targetとし、追加のbridge theoremをavailable branchに置く。
- M12: E12-bでReader 03のみcoding。Reader 02はwell-foundednessをmetatheoryで証明する構造をanalysis objectとし、代わりにM15でstandard metamathematical distinctionへのabsorptionを表す。

E12の差はscalar/architecture terminal statusを変えず、formation moveと分析対象の数学的構造をどこで分けるかに依存する。

### 4.3 Difference categories summary

- **same move under same episode boundary:** E02-b M1/M4、E04 M14/M15/M17、E07 M17、E08 M2/M14/M17、E09 M4/M17、E11 main M2/M14、E12-a M1/M2/M3/M4/M14など。
- **different move because boundary differs:** E05 replacement package、E06 taxonomy、E11 technical correction。
- **optional co-code difference:** E01/E03のM14、E02-aのM2対M14、E05 definitional M2、E10のM2対M14、E12-aのM13。
- **code-versus-resource difference:** E05 state mapのM10、E11のM6/M12。
- **code-versus-analysis-object difference:** E10 M12では同じ非coding、E11/E12-b M12とE12-a M13ではreader間で異なる解決。
- **unsupported difference:** blind comparisonだけから、一方のcodeをsource-unsupportedと確定できる差はない。Reader 03のE05 M10、E11-b before/M3、E12 M13は本人がINFERENCEまたはAMBIGUOUSを付し、Reader 02も対応内容自体は認識している。相違はsource内容の見落としと断定できず、boundaryまたはoperation-roleの非一意性として残る。

## 5. Role comparison

### 5.1 Assumptions

広い一致は、claimのadmissible casesをassumptionsに置き、counterexample・audit・bridge theoremをそこから分けたことである。E01のnoninjectivity antecedent、E04のsingle-copy/destructive-operation条件、E07のfrozen control、E09の「十分なcodeがある」というdesign premise、E12のfixed package parametersは両者で同じ役割を持つ。

主な差は次のとおり。

- **E02-b:** Reader 02はpositive assumptionsに加え、candidate縮小、environment memory、external log、infinite cardinalityという失効条件もassumption境界に置き、available branchとのAMBIGUITYを明記する。Reader 03はpositive four conditionsだけをassumptionsに置き、失効条件をavailable branchesとする。
- **E05 definitional branch:** 両者ともcomplete interface specificationをassumptionとする。Reader 02は同一protocol/transcript relationを同じintegrated blockのassumption／conventionに置き、Reader 03はE05-bのassumptionとし、physical theoremとして数えないことをevaluation ruleへ分ける。
- **E05 conditional branch:** 両者ともcontrolled-transition条件とcommuting state mapをclaim conditionとする。Reader 03はstate mapがproof resourceでもありうると明示し、Reader 02もinterface assumptionとresourceの二重性をframework-boundary problemとして記録する。
- **E11:** Reader 02はT+ constructionsとΓ scopeをmain S2 judgmentのassumptions/resourcesに置く。Reader 03はE11-bを立て、chosen base/schema/Γ/truth axiomsをそのtechnical claimのassumptionsにする。
- **E12-b:** Reader 02は五構成要素を含むordinal analysisをassumption、Reader 03は各componentが記載roleを占めることとTuring–Fefermanとの非同一をassumptionとする。差は主にbeforeの確定度に由来する。

### 5.2 Proof/evidence resources

- **E01/E02-a:** Reader 02はprior artやcounterconstructionをfailure witnessへ集中させ、元claim側のproof resourceを「elementary fact only」またはUNKNOWNとする。Reader 03は同じmaterialsをobligationをinvestigateしたevidence resourcesにも置く。これは内容差ではなく、failure evidenceをresource欄にも含めるかのrole assignment差である。
- **E03/E04:** 両者ともcountermodels/constructionsと既存technical vocabularyをresourcesとして認識するが、Reader 02は一部をfailure witnessに限定し、Reader 03はresource listを広く取る。
- **E05-c:** history-length inductionは両者一致してresource。state mapは両者ともclaim conditionだが、Reader 03はM10 moveにも分類し、Reader 02はmoveにしない。
- **E06:** 両者ともcase-level evidential detailsの欠落を認識する。Reader 02はresourcesをUNKNOWNと明記し、Reader 03はavailable summary materialsを列挙しつつfine-grained mappingをUNKNOWNとする。
- **E10–E12:** standard theorem statements、reflection constructions、ordinal bridge theoremsをanalysis resourcesとして読む点は一致する。E11/E12でそれを別formation transitionへ昇格させるかが分かれる。

### 5.3 Evaluation or decision rules

両者とも、counterexample自体と「何をもってclaimをretain/demoteするか」を区別している。特にE07のpreregistered success/falsification conditions、E09のdesign termination rule、E10–E12のsource-local laddersをevaluation ruleとして扱う点は一致する。

相違は、packetに完全なrule definitionがない場合の記述強度である。

- Reader 02はE06 Null labels、E07 §5/§6、E09 Part IX、E10–E12 laddersについて「ruleの存在はSOURCE-DERIVED、内容はUNKNOWN」を反復する。
- Reader 03も欠落を記録するが、各afterから「一般定理にはnoninjectivityを強制する条件が必要」「A3はstandard distinctionを越える必要がある」等のlocal ruleをより積極的にINFERENCEする。
- E03の「具体的に証明すべき」は、Reader 02ではadopted side claimとevaluation ruleの役割重複としてAMBIGUOUS、Reader 03ではevaluation ruleとside claimの両面を別表現で記録する。
- E08のN-04は、Reader 02がevidence resourceに実体を置きつつinternal-consistency ruleをevaluation欄に置く。Reader 03も「unmeasured effectをassertしない」というdecision ruleを再構成する。

### 5.4 Available branches

- **Shared treatment:** E01の「noninjectivityを強制する条件」、E04のfresh preparation、E07のsource-local M0/M2/M3 alternatives、E09-aのRET-DOWN/full design/immediate termination、E10のC2/C3、E12-bのA3を、採用結果とは分ける。
- **E02-b difference:** Reader 02は失効条件をassumption boundaryに置いたためavailable branchesをUNKNOWNとする。Reader 03はcandidate restriction、environment memory、external log、infinite settingsを明示的branchesにする。
- **E05 difference:** Reader 02は二replacementをintegrated after-claimsとしてNOT APPLICABLE/UNKNOWNとし、Reader 03は別subepisodesにするためE05-aでもmerely availableとは扱わない。分離方法は違うが、両者とも実際に採用されたreplacementを「未採用branch」へ落とさない。
- **E08 difference:** Reader 02は内容不明のverdict Aをavailable/rejected branchとして保持する。Reader 03はAを記録せず、将来のeffect measurementをOPEN HYPOTHESIS的branchとする。
- **E09-b difference:** Reader 02はこの段階のunadopted branchをUNKNOWNとし、Reader 03はfull P1–P5を明示的rejected branchとして再掲する。
- **E11 difference:** Reader 02はS2救済branchをUNKNOWNとする。Reader 03はunqualified S2 retentionをexplicit not-taken branchとし、E11-bではlocal/uniform/global extensionsをalternative branchesとして列挙する。
- **E12-a difference:** Reader 02はadditional bridge theoremをavailable routeとする。Reader 03はuniversal scalarをrejected branch、single characterizationとPA-like convergenceをrestricted branchesとして分ける。

### 5.5 Adopted side claims

元claimの失敗とremnantを同一successにしない点は全体として収束する。E01、E02、E03、E04、E07、E08、E09、E12で、両者はwithdrawn/unsupported main claimとretained remnantへ別statusを与える。

identityの粒度には差がある。

- E01: Reader 02はequivalence distinctionとrelative identifiabilityを一つのS01にまとめ、Reader 03は二つのclaim IDに分ける。
- E05: Reader 02はdefinitional/conditional replacementsをmain claimのsuccessではないsuccessor after-claimsとし、`adopted_side_claims`をNOT APPLICABLEとする。Reader 03はそれぞれ独立claim/subepisodeとする。
- E06: 両者ともfield-native reconstructionをretainするが、Reader 02はrejected working hypothesisの「retained as rejected record」という中間statusもside claim化する。Reader 03はcombined block内でdemoted hypothesisとfield-native remnantを分ける。
- E10: Reader 02はC1 metaphorをS10 side claim、Reader 03は同じlabel claimのweakened continuationとする。terminal meaningは同じで、claim identityのみ異なる。
- E11: Reader 02はS2*をS11 side claim、Reader 03はE11-aではsame identityのqualified continuationとし、E11-bでΓ scope／external stronger-theory claimsを別side claimsにする。

### 5.6 OPEN HYPOTHESIS

- Reader 03はE02-bのconditional-capacity successorを明示的`OPEN HYPOTHESIS`から始める。Reader 02はwithdrawn B02を直接beforeに再利用し、open-hypothesis段階を作らない。
- Reader 03はE05-cでreal observerにpreserving state mapが存在することをOPEN HYPOTHESISとして残す。Reader 02も「existence guaranteeなし」と同じ内容をterminal limitationに置くが、OPEN HYPOTHESIS labelは使わない。
- E04の必要十分bridge conditionsは両者ともopen/synthesis。
- E08ではReader 03だけが将来のactual-use/effect measurementをprospective open branchとして明示する。Reader 02はeffectiveness statusをuntested/openとするが、future claimを別に立てない。

### 5.7 Degenerate or target leakage

semantic coreは広く一致する。

- E01: noninjectivity premiseにnon-recovery conclusionが埋め込まれる。
- E03: many-to-one/coarse-grainingをdefinitionに入れる。
- E04: destructive single-copy interfaceの効果をinternalityへ帰属する。
- E05: history capability equalityをinterface definitionへ入れる。
- E08: documentary persistenceからpreservation effectivenessへ越境する。
- E10: Gödelの標準的成果をnew framework vocabularyの成果として取り込まない。
- E11: local reflectionの説明力をuniform/global/soundnessへ持ち越さない。
- E12-a: calibration coordinateをtotal strengthへ持ち越さない。

reader-specificな適用もある。E02ではReader 02が「conditional theoremにself-containmentの功績を帰属させない遮断」とし、Reader 03はuniversal claim側のpremise conflationとして記録する。E07はReader 02がpresentation valueをdiagnostic valueへ数えない明示的leakage遮断、Reader 03は「直接targetをtestしたnegative resultなのでleakageなし」とする。E09-aはReader 02がdesign execution自体の成果化を遮断したと読み、Reader 03はscope decisionでleakageなしとする。E12-bはReader 02がstandard distinctionをA3 noveltyへ計上しない遮断、Reader 03がobject/metatheory type leakageの訂正として表す。

## 6. Packet-gap convergence

以下は、両readerが独立にmissing/UNKNOWNとして検出した事項である。

| Parent / topic | Shared missing information | Comparison status |
|---|---|---|
| E06 witness | GST seriesが反復Deferred Resolution chainをsupportしなかった具体的観察、Null C/D/Eの実質、field-native vocabularyへのitem-by-item対応 | **SHARED PACKET GAP** |
| E07 preregistration | §5 falsification conditionsと§6 success conditionsの全文・個別適用内容 | **SHARED PACKET GAP** |
| E09 reduced check | P1-reduced/NONEVAL two-field checkが具体的に何を観察し、なぜ第二段階のpremise failureになったか | **SHARED PACKET GAP** |
| E10 comparison | 「既存21定理」の内容と比較実体 | **SHARED PACKET GAP** |
| E10 source-local ladder | C1/C2/C3の完全な昇格・降格基準 | **SHARED PACKET GAP** |
| E11 source-local ladder | S2の元claim全文、S1/S2/S2*の完全な定義 | **SHARED PACKET GAP** |
| E12 source-local ladders | S1/S2/S2*とA2/A3を含む判定ラダーの完全な定義 | **SHARED PACKET GAP** |
| E12 calibration package | 固定すべきnotation、base/metatheory、formula class、reduction notionの具体値／標準package | **SHARED PACKET GAP** |
| E05/E06/E11 segmentation | 唯一のanalytic episode boundary | **SHARED PACKET GAP** |

source-local ladders一般についてはsemantic overlapがあるが、検出範囲は完全同一ではない。Reader 02はE07のM0–M3、E09の`D相当`、E12のA0–A3まで明示的gapとし、Reader 03は主にE10–E12のC/S/A laddersをまとめてgapとする。したがって「source-local ladder不足」という上位問題は共有される一方、個別labelの網羅性はreader-specificである。

## 7. Framework-boundary convergence

ここでいうconvergenceは、両readerが同じ表現困難性を独立に記録したことを指す。解決策の選択やframework revisionは行わない。

| Boundary problem | Reader 02 expression | Reader 03 expression | Semantic overlap / remaining difference |
|---|---|---|---|
| Definitional/stipulative transition | E05のA2は「同一性を定義した帰結」で、M1は近似にすぎない | E05-bはconventionでありM1/M2/M14のいずれも完全には一致しない | 強いsemantic overlap。Reader 02はintegrated after、Reader 03は独立episodeにしたためco-codeだけ異なる |
| Taxonomy deletion | E06-cはclaimでなくclassification apparatusの削除で、M17は近似。理由もUNKNOWN | E06-bでtaxonomy廃止とcase/mechanism demotionが同じM17に集約される | 両者ともM17の粗さを検出。Reader 02はreason不明を分離、Reader 03は共通revision contextを優先 |
| Verdict relabeling | E08の`Partial preservation`→`Documentary continuity`はM2＋M14による近似 | source-local status relabel自体にformation moveがないと記録し、E08をM2/M14/M17で表現 | 強いsemantic overlap |
| State-map simulation | E05のpolicy transferはM9に十分合わず、M4/M8で表す | M10に近いがcontroller implementation simulationはcodebook例外縁。M7/M8/M10で表す | 同じfit問題を検出。M4対M7、M10の有無が残る |
| Branch-state changes | E02追加条件とE09 terminationがavailableからlater adoptedへ変わるがcross-subepisode link欄がない | E09-aのimmediate terminationは当時unadopted、E09-bでlater adoptedになると区別 | semantic overlap。Reader 02はsubmission-block構造の問題、Reader 03はtemporal role assignmentとして記録 |
| Object-level mathematical operation vs formation move | E10 M12、E11 M6/M12、E12-b M12をanalysis object/resourceとして非coding | E10では同じ非coding。E11-bとE12-bでは独立formation transitionを立てM6/M12をcoding | boundary problemの認識は共有、解決はE11/E12で分岐 |
| Multiple-axis restriction | E12 fixed packageをM1/M3/M4へ分解する粒度が未指定 | M1/M3/M4重複が不安定と記録 | 強いsemantic overlap。E12-aの三code自体は一致 |
| Kill-test with limited survival | E11のS2→S2*をM2で近似し、過程はstatusにしか残らない | source-local classificationをterminal statusに移せるがclassification operation自体をcode化しにくい | 表現は異なるが、verdict processとformation moveの不一致を同じく検出 |
| Multiple after-claims | `move_taken`がafter別でなくE05の異なるmovesを対応づけにくい | 一withdrawalから複数conditional replacementsをsubepisode化するとshared beforeの反復規則がない | 同じ構造を、Reader 02はone-block mapping問題、Reader 03はsegmentation/link problemとして表現 |
| `degenerate_or_target_leakage` | 定義・例・provenance指針がない | 定義への埋め込み、条件取違え、target消失を一欄で扱うことになる | 強いsemantic overlap |

両者の語彙が一致しない場合でも、例えば「分類体系の削除」と「source-local verdictの固定」、「state-map translation」と「implementation simulation」は、同じboundary pressureの別表現として扱える。ただし同義と断定せず、上表のremaining differenceを保持する。

## 8. Reader-specific findings

以下は片方の記録だけに現れる、または片方だけが明示的に問題化した事項である。reader errorとは扱わない。

### 8.1 Reader 02-specific findings

#### Reconstructed transitions and ambiguities

- E04で、quantifier-order differenceの確立とinternality attributionの撤回を二subepisodeにできるというalternative segmentationを保持した。
- E05で、`inside vs outside`というspatial locationを第一義的数学条件とすることの撤回を、general equivalence correctionとは別のtransitionとして立てた。Reader 03にはこの独立claim/statusがない。
- E06でtaxonomy deletionを独立E06-cとし、固有failure witness、evaluation rule、deletion reasonをUNKNOWNとした。
- E08で、verdict文の削除とverdict labelの改称を別transitionにできるというalternative segmentationを保持した。
- E12-bのclaim-beforeを、A-ladder欠落のためUNKNOWN/AMBIGUOUSのまま残した。Reader 03は同じ不足を認めつつclassification obligationをINFERENCEした。

#### Move and role findings

- E01、E02-a、E03、E10で、retained distinctionをM14として追加codingした。Reader 03は同じ内容をside claimまたはM2に置く。
- E12-bでstandard metamathematical level distinctionへのM15をcodingし、M12はanalysis objectとして留保した。
- E07ではM2とM15、E09-bではM15をexplicitly considered but not codedとして残した。
- E02-bの失効条件をassumptionsとavailable branchesの境界問題として扱い、重複を避けてassumptionsへ置いた。
- E08で内容不明のverdict Aをavailable branchとして残した。

#### Packet and protocol findings

- E06 Source path Aの版が不明で、DR-1がv0.2で維持／撤回／再定義のいずれかを決められないとした。
- E08の“Codex”が人か自動reviewerか、外部指摘か自己発見かを決められないとした。
- E09の14 codes、NONEVAL、RET-DOWN、L2/L3、`D相当`、Part IX ruleの定義欠落を個別に列挙した。
- E11とE12の`S2*`が同じladder上の同じlabelかを決められないとした。
- E01–E04が一つのrunning claimのphase sequenceか、独立itemsかをpacketだけでは決められないとした。
- Submission blockについて、`move_taken`がafter-claim別でないこと、A1/A2 labelsとsource-local A2の衝突、`claim_identity`欄の意味、dependencies provenanceの粒度、alternative segmentationのcoding方法、cross-subepisode link、cross-item beforeの可否を明示的problemとして挙げた。
- Original-source return permissionと、diff文書／trajectory material禁止の境界、構造的に薄いexcerptへの対応をisolation-level問題として記録した。

### 8.2 Reader 03-specific findings

#### Reconstructed transitions and ambiguities

- E01のretained statementを、equivalence-class distinctionとrelative identifiabilityの二つのside-claim IDへ分けた。
- E02-bをwithdrawn universal claimの直接afterではなく、追加条件下のsuccessorを問う`OPEN HYPOTHESIS`から始めた。
- E05をwithdrawal／definitional convention／conditional model correspondenceの三つへprimary segmentationし、二replacementのobligationを別blockで完結させた。
- E06ではmechanism demotionとtaxonomy deletionを一blockに置き、field-native absorptionと同じrevision contextを共有させた。
- E11-bを独立technical correctionとして立て、Γ scopeとexternal stronger-theory subject shiftへ独立claim IDとterminal statusを与えた。

#### Move and role findings

- E02-aでM14ではなくM2を使い、self-containmentの役割を“sufficient cause”から“premise enabler”へweakeningした。
- E05 definitional branchにM2を追加し、conditional correspondenceにはM7/M8/M10を付した。state-map simulationへのM10はINFERENCEとして留保した。
- E10ではReader 02のM14に対しM2を用い、independent classificationからexplanatory metaphorへのweakeningを中心にした。
- E11-bでM6/M12をcodingし、M3はAMBIGUOUS co-codeとして残した。
- E12-aでM13、E12-bでM12をcodingし、standard-level absorptionのM15は採らなかった。
- E02-bのcountersettings、E08のfuture effectiveness measurement、E11-bのreflection variantsをavailable/open branchesとして広く記録した。
- E02-bでAまたはEがemptyかという有限cardinality argumentのlocal uncertaintyを挙げた。

#### Packet and protocol findings

- M9/M10がgeneral implementation simulationをどこまで含むかを、Reader 02より直接的にcodebook coverage problemとして挙げた。
- Source-local classificationをterminal statusとして移せても、classification decision自体に対応するformation moveがないという形で問題を記録した。
- Multiple conditional replacementsをsubepisode化したとき、shared claim-beforeをどこまで反復できるかを明示的problemとした。

## 9. Final qualitative result

### A. Strong cross-reader convergence

両readerは、E01–E04、E07–E10、およびE12-aのprincipal transitionについて、ほぼ同じclaim-before、failure witness、withdrawal/demotion、retained remnant、terminal directionを再構成した。特に次の骨格は安定している。

- 条件や定義に結論を埋め込んだ一般化はwithdrawされ、具体的条件または既存technical vocabularyだけが残る。
- Internal/external、preservation/effectiveness、diagnostic/organizational value、universal scalar/fixed calibrationの区別がafter-claimに反映される。
- Adopted side claimは元claimの成功として扱われず、別statusを持つ。
- E07のsource-local M labelsをformation codesと混同しない。
- E10のGödel metatheorem structureをM12 formation moveにしない。

### B. Stable ambiguity hotspots

E05、E06、E11では、二readerが異なるprimary segmentationを採用しつつ、少なくとも一方または両方がalternativeを明示した。E02、E04、E08ではprimary結果は一致するが、Reader 02だけがadditional segmentation ambiguityを残す。E12-bはsegmentationではなくclaim-beforeの存在とclassification transition性が安定したambiguity hotspotである。

### C. Boundary-dependent coding

Move差の中心はsource内容の違いではなく、何をanalytic transitionとして切り出すかである。

- E05を統合するとM1/M4/M8が一つのrevisionに集まり、分割するとM2/M7/M10が個別branchに現れる。
- E06でtaxonomyを独立させると固有witnessはUNKNOWNになり、mechanismと統合するとM15のcontextが及ぶ。
- E11でT+ constructionをresourceに置けばM6/M12は非coding、technical correctionを独立化すればcoding対象になる。
- E12-bでもmetatheoryはanalysis objectにもM12 moveにもなりうる。E12-aのM13も、calibrationをbeforeからのreformulationと見るか、当初からのanalysis objectと見るかに依存する。

### D. Shared packet limitations

E06 witness details、E07 preregistered criteria、E09 reduced-check observations、E10の21-theorem comparison、E10–E12のsource-local ladders、E11の元S2、E12の具体的calibration packageは、両readerが独立に不足と認識した。これらは**SHARED PACKET GAP**であり、blind comparison内で埋められない。

### E. Reader-specific reconstructions

Reader 02はadditional ambiguity、UNKNOWN、source-local label definitionの欠落を細かく保持し、spatial `inside vs outside` withdrawalとtaxonomy deletionを独立transitionにした。Reader 03はconditional successorsとtechnical correctionsをより細かくsubepisode化し、state-map translation、reflection extension/metalevel shift、ordinal calibration reformulationへM10/M6/M12/M13を割り当てた。これはreader-specific reconstruction styleの差として記録され、優劣や正誤には変換しない。

### F. What remains genuinely undecidable from this blind comparison

- E05の最小episode boundaryと、spatial-location withdrawalを独立transitionとして必ず立てるべきか。
- E06 taxonomy deletionがmechanism failureと同じwitnessを持つか、理由不明の独立編集decisionか。
- E08の表現削除とverdict relabelが一transitionか二transitionか。
- E11のreflection-theory constructionがS2* judgmentのresourceに留まるか、独立technical claim transitionか。
- E12-aのM13、E12-bのM12/M15のうち、どのoperation identityがsourceによって一意に要求されるか。
- E05 state mapをM10、M7、M4、またはresourceのみとして扱う境界。
- Missing ladder definitionsの下で、C1、S2*、A2等がdemotionなのか初回classificationなのか。
- Packetに欠けるwitness/detailsを補った場合に、現在のsegmentation、role assignment、terminal statusが維持されるか。

これらは、二readerの記録だけからは決定できない。したがって本比較は、共有transition core、stable ambiguity、boundary-dependent coding、shared packet gap、reader-specific reconstructionを並置するところで終了する。

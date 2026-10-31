# Consciousness Phase 00 — dependency / inheritance / source authority record v0.1

## 0. Status

- Consciousness audit: **IN PROGRESS**
- Phase 00 dependency / inheritance / source authority: **COMPLETE**
- Phase 01 equation / symbol / object inventory: **NOT STARTED**
- 作業日: 2026-09-09。対象は `consciousness/` の現物および直接の参照元・参照先。
- 本記録はinventoryのみ。sourceの主張を記載することと、監査者がその主張を採用することを区別する。validity、circularity、empirical adequacy、phenomenal explanationの成否、claim dispositionは判定しない。
- 上流VED equation audit / core revision、Bio-IFGT audit / core revisionはCLOSED。closureは各々の監査・実装整合の状態であり、Consciousnessの導出・神経機構・現象的同定の成立を継承しない。
- 原文・式・図・PDF・code・過去の監査は変更せず、simulation / build / web researchも行わない。

本記録のID、L0–L3列、集計区分は監査用索引であり、新しい理論記号ではない。以下のS00–S20は§2のEN/JA source pairを指す。`S06:319`はEN sourceの行番号、`JA`を付した場合は対応JA sourceの行番号。section名を併記するので行移動後も追跡可能である。「first」はcurrent buildの読書順での最初の導入・最初の定義を区別し、発明・歴史的初出は意味しない。

## 1. Authority / source tree

### 1.1 上流authorityと適用境界

| Authority | 確認した状態 / 用途 | 本監査へ自動継承しないもの |
| --- | --- | --- |
| [VED final audit](../ved_equation_audit/06_final_audit_record_v1.0_ja.md)、[closure recheck](../ved_equation_audit/implementation_final_closure_recheck_v1.1_ja.md)、[README](../ved_equation_audit/README_ja.md) | frozen dispositions、CLOSED、source-local objectと未解決bridgeの区別 | ConsciousnessがVEDから導出済みという地位 |
| [Bio final audit](../bio_ifgt_audit/07_final_audit_record_v1.0_ja.md)、[final recheck v1.1](../bio_ifgt_audit/implementation_final_consistency_recheck_v1.1_ja.md)、[README](../bio_ifgt_audit/README_ja.md) | audit/core CLOSED。v1.0 FAIL履歴を維持してclosure。BIO-OPEN-01–26は研究上未解決 | fast/slow確認、神経機構、phenomenal explanation |
| [Bio execution audit](../bio_ifgt_audit/05_simulation_and_empirical_correspondence_audit_v0.1_ja.md)、[current Bio README](../../bio-ifgt/README.md) | finite toy witnessと生物対応を分離。専用fast/slow結果の所在なしというhandoff | toy hierarchyを神経・意識の生成順序とする推論 |
| [IFGT entry](../../Information-Field-Geometry-Theory/main.tex)、[fundamental dynamics](../../Information-Field-Geometry-Theory/sections/fundamental_dynamics.tex)、[VED relation](../../Information-Field-Geometry-Theory/sections/ved_relation.tex) | current upstream source-local field、informational tau、source sigma、OPEN translationの照合 | 同じglyphからの同一carrier / time / equation identity |
| [Bio life region](../../bio-ifgt/sections/life_attractor.tex)、[second attractor](../../bio-ifgt/sections/intelligence_second_attractor.tex)、[toy source](../../bio-ifgt/sections/minimal_developmental_simulation.tex) | Consciousnessが参照する語彙の所在 | biological / phenomenal identification |
| [root EN](../../README.md)、[root JA](../../README_ja.md)、[concept map](../../docs/navigation/concept_map.md) | entry/navigation、application-layer accountの位置づけ | navigation順をproof/generation順とすること |

### 1.2 実際のbranch treeとauthority

| File / group | Role | Current-facing? | Build authority? | Historical / working? | Notes |
| --- | --- | --- | --- | --- | --- |
| [main.tex](../../consciousness/main.tex) | canonical EN entry、preamble、macros | YES | YES | NO | article + fontspec。21 input、abstract + numbered sections 20 |
| [main_ja.tex](../../consciousness/main_ja.tex) | canonical JA entry | YES | YES | NO | ltjsarticle / luatexja。self-containedではなく21 input |
| `consciousness/sections/*.tex` | EN本文21 files | YES | YES | NO | §2に全件列挙 |
| `consciousness/sections_ja/*_ja.tex` | JA本文21 files | YES | YES | NO | working Markdownではない。ENと同じsection順 |
| [refs.bib](../../consciousness/refs.bib) | shared bibliography | YES | YES | NO | entryはIntelligence 1件、plainnatで両entryに接続 |
| [main.pdf](../../consciousness/main.pdf)、[main_ja.pdf](../../consciousness/main_ja.pdf) | distributed manuscripts | YES | build output | NO | tracked。ignore ruleが存在しても現在trackedであることは別 |
| `figures/*.pdf` / `figures_ja/*_jp.pdf` | included schematic figures 各6 | YES | TeXが直接参照する図asset | NO | 12 PDFs、6 figure families |
| draft_en.md（公開版未収録: `../../consciousness/draft_en.md`）、draft_ja.md（公開版未収録: `../../consciousness/draft_ja.md`） | flattened old drafts | NO（canonicalとしては） | NO | working/historical 2 | ignored/local。両方にSource status注記。旧Bio fast/slow帰属を保存 |
| `figures/*.svg` / `figures_ja/*_jp.svg` / `figures_ja/*_jp.png` | local figure-generation/export assets | NO（直接build入力ではない） | NO | local derivative 18 | SVG 12、JA PNG 6。元図とのprovenanceをファイル名だけから確定しない |
| [branch .gitignore](../../consciousness/.gitignore) | tracking/working-status policy | policy | NO | NO | old flattened draftsよりmodular TeXをmaintained sourceと明記 |
| `.texmf-var/`、aux/log/bbl/toc/out/blg、`.DS_Store`等 | build cache / generated bookkeeping | NO | NO | research sourceではない | 上記以外157 files。logはbuild経路の補助情報であり理論authorityではない |
| branch README / notes / handoff / appendix / simulation / code | 対象候補 | NOT LOCATED | NOT LOCATED | NOT LOCATED | branch内に専用README・appendix input・simulation実装・datasetは所在せず。§17はnote系列についての本文であって別appendixではない |

全local treeは237 files。current-facing **text sourceは45**（44 TeX + 1 bib）、distributionは14 PDFs（main 2 + figure 12）、working/historical textは2、local figure derivativesは18、policyは1、その他157。current-facing text + distributionは59 files。これらの集合を混ぜて「source数」としない。historical-onlyとworkingを厳密に分ける年代authorityはなく、2 draftsは両ラベル、historical-onlyと一意に決まる別textは0。

## 2. Current-facing source map

EN/JA双方のbuild経路はentry → 21 input → shared bibliography。ENはfontspec対応engine、JAはLuaLaTeX構成。local build logもLuaHBTeXを示す。本phaseではbuild commandを実行していない。`\appendix`、独立appendix input、branch内codeは所在しない。

| Source ID / order | EN source | JA source | 主なinventory対象 |
| --- | --- | --- | --- |
| S00 abstract | [abstract](../../consciousness/sections/abstract.tex) | [abstract JA](../../consciousness/sections_ja/abstract_ja.tex) | log-referenceable relation、非生成記述 |
| S01 §1 | [introduction](../../consciousness/sections/introduction.tex) | [introduction JA](../../consciousness/sections_ja/introduction_ja.tex) | 4 declarations、upstream / CT位置 |
| S02 §2 | [intuitive picture](../../consciousness/sections/intuitive_picture.tex) | [intuitive picture JA](../../consciousness/sections_ja/intuitive_picture_ja.tex) | fast/slow境界 |
| S03 §3 | [notation](../../consciousness/sections/notation.tex) | [notation JA](../../consciousness/sections_ja/notation_ja.tex) | local notation、t/tau/T区別 |
| S04 §4 | [SSO](../../consciousness/sections/sso.tex) | [SSO JA](../../consciousness/sections_ja/sso_ja.tex) | Bio motivation、2展開名、gate |
| S05 §5 | [TCA](../../consciousness/sections/torque_converter_attention.tex) | [TCA JA](../../consciousness/sections_ja/torque_converter_attention_ja.tex) | torque analogy、attention、ego |
| S06 §6 | [formal mapping](../../consciousness/sections/formal_mapping.tex) | [formal mapping JA](../../consciousness/sections_ja/formal_mapping_ja.tex) | projection、IFGT/VED template、closure degree |
| S07 §7 | [core equations](../../consciousness/sections/core_equations.tex) | [core equations JA](../../consciousness/sections_ja/core_equations_ja.tex) | window、nonclosure conditions |
| S08 §8 | [structural interpretation](../../consciousness/sections/structural_interpretation.tex) | [structural interpretation JA](../../consciousness/sections_ja/structural_interpretation_ja.tex) | conscious regime、ego、qualia |
| S09 §9 | [log dynamics](../../consciousness/sections/dynamics_log_referencing.tex) | [log dynamics JA](../../consciousness/sections_ja/dynamics_log_referencing_ja.tex) | six-step referencing loop、report |
| S10 §10 | [experiments](../../consciousness/sections/experimental_reinterpretation.tex) | [experiments JA](../../consciousness/sections_ja/experimental_reinterpretation_ja.tex) | Libet、split-brain、rationalization |
| S11 §11 | [qualia](../../consciousness/sections/qualia_boundary.tex) | [qualia JA](../../consciousness/sections_ja/qualia_boundary_ja.tex) | sedimentation frontier、hard problem |
| S12 §12 | [opening model](../../consciousness/sections/opening_model.tex) | [opening model JA](../../consciousness/sections_ja/opening_model_ja.tex) | self terrain、storage/copy |
| S13 §13 | [measurement](../../consciousness/sections/measurement_collapse.tex) | [measurement JA](../../consciousness/sections_ja/measurement_collapse_ja.tex) | residue、introspection、collapse |
| S14 §14 | [non-localization](../../consciousness/sections/non_localization.tex) | [non-localization JA](../../consciousness/sections_ja/non_localization_ja.tex) | local substrateとregime |
| S15 §15 | [predictions](../../consciousness/sections/qualitative_predictions.tex) | [predictions JA](../../consciousness/sections_ja/qualitative_predictions_ja.tex) | qualitative directions、testable directions |
| S16 §16 | [pathologies/limits](../../consciousness/sections/pathologies_limits.tex) | [pathologies/limits JA](../../consciousness/sections_ja/pathologies_limits_ja.tex) | regime deviations、明示未完成mapping |
| S17 §17 | [relation to note](../../consciousness/sections/relation_to_note.tex) | [relation to note JA](../../consciousness/sections_ja/relation_to_note_ja.tex) | note / L1–L3説明層 |
| S18 §18 | [discussion](../../consciousness/sections/discussion.tex) | [discussion JA](../../consciousness/sections_ja/discussion_ja.tex) | theory comparisons、remaining questions |
| S19 §19 | [conclusion](../../consciousness/sections/conclusion.tex) | [conclusion JA](../../consciousness/sections_ja/conclusion_ja.tex) | proposed result、futurework |
| S20 §20 | [correspondence map](../../consciousness/sections/correspondence_map.tex) | [correspondence map JA](../../consciousness/sections_ja/correspondence_map_ja.tex) | CT correspondence table、4-layer reprise |

root EN:167–168 / JA:119–120はmain PDFへリンクしarXiv ID未確定と記載。concept mapはConsciousness directory、S04、S05、S09へリンクする。rootの説明はapplication-layer / temporal nonclosure / log referencing。参照元の列挙はauthorityの格上げではない。

## 3. Upstream dependency inventory

主たるcurrent dependency familyを28件で固定する。Explicitはsourceがbranch/object/対応を記載する意味であり、exact upstream equation locatorや導出が明示されるという意味ではない。claimed identityは「same structure / quantity / coordinates」という原文上の同一性主張を含むが、同じphysical carrierを主張するとの読みは自動付与しない。分類は排他的主分類で集計する。

| DEP-ID | Upstream source/object | Consciousness location | Relation type | Explicit or implied? | Current claim wording / paraphrase |
| --- | --- | --- | --- | --- | --- |
| DEP-01 | IFGT I/J/Phi | S00末、S01:35–43 | vocabulary reuse | explicit | projected effective coordinates、general fieldと直接同定しない |
| DEP-02 | Bio life attractor | S01:43、S04:9–11 | background motivation | explicit | biological comparisonを動機づける語彙 |
| DEP-03 | Bio finite M/I/N/B/E | S04:17–23 | formal analogy | explicit | staged model rolesからfast/slowを本稿が提案。confirmed Bio resultではない |
| DEP-04 | fast/slow biological reading | S04:9–25 | premise | explicit | own downstream premise、candidate biological realization |
| DEP-05 | IFGT I | S06:151–182 | symbol reuse | explicit | slow-layer re-referenceable log density |
| DEP-06 | IFGT J / local J_log | S06:151–213、S07 IFGT Coupling | symbol reuse | explicit | general currentとwindow-local referencing flow |
| DEP-07 | IFGT Phi / gradient | S06 IFGT Mapping | symbol reuse | explicit | log configurationからmeaning field、referencing bias |
| DEP-08 | IFGT balance / flow / force / convolution | S06:184–213、S07 | equation reuse | explicit | 「minimal relations of IFGT」。current upstreamはtau/J/F_I等を使用し、本文はt/J_I/F/Kを使用。exact version未固定 |
| DEP-09 | VED nonclosure | S06:215–250、S07 Non-Closure | vocabulary reuse | explicit | difference、gradient、flow、closure tendency |
| DEP-10 | older VED persistence PDE | S06:300–321、JA S06:243–261 | claimed derivation | explicit | 「Through this three-term structure ... maintains」「VED-grounded basis」。phenomenological approximationとも記載。成立を本監査は判定しない |
| DEP-11 | VED closure degree C | S06 VED Closure Degree | symbol reuse | explicit | C_f / C_sをlayerのeffective closure degreeとして導入 |
| DEP-12 | Delta v / Delta C | S06:275–333、S07末、figure6 | claimed identity | explicit | same non-closure condition in different coordinates。neither grounds the otherも併記 |
| DEP-13 | VED temporal nonclosure → SSO | S04 Temporal Non-Closure、S06 SSO as Local | claimed correspondence | explicit | SSOをlocal temporal structure in the brainと読む |
| DEP-14 | IFGT/VED → TCA | S05末、S06 Coupler | claimed correspondence | explicit | VED-type transmission mechanism / IFGT-type direction mechanism |
| DEP-15 | IFGT/VED interface → consciousness | S06 Interface | claimed correspondence | explicit | local projected regime、log referencingのschematic expression |
| DEP-16 | projection / fourth IFGT primitive | S06:66–101 | vocabulary reuse | explicit | mass assignmentとして本稿がstructural definitionを供給。upstream既存定義の所在は別問題 |
| DEP-17 | Intelligence projected uses | S06:46–62、S18 | claimed correspondence | explicit | parallel paperとcommon epistemological foundation。片方向upstreamだけではない |
| DEP-18 | CT invisible GPU / landscape | S04:196 | claimed identity | explicit | SSO条件とconceptual landscape形成条件がsame structure |
| DEP-19 | CT token coupling | S05 Attention as Temporal Transformation内CT quote | claimed identity | explicit | temporal/spatial axesのsame transformation structure。S20はisomorphic structures |
| DEP-20 | CT meaning gradient | S09:129 | claimed identity | explicit | 「same quantity」governs conscious bias / concept depth,width,robustness |
| DEP-21 | CT qualia / insight | S20 table | claimed identity | explicit | same boundary phenomenon at different temporal granularities |
| DEP-22 | CT sedimentation / Phi* | S09:61、S20 table | claimed correspondence | explicit | CTでformally specified、long-time attractor / geometric deformationとして対応 |
| DEP-23 | CT positivity / complete closure exclusion | S20 table | equation reuse | explicit | I(x,tau)>0を両windowに列記。positivity自体によるentity identityを否定 |
| DEP-24 | VED/Bio/Consciousness/Intelligence four layers | S06:421–432、S18:223、S20末 | claimed identity | explicit | same differential-development structure / generative grammar、nonreductionとも記載 |
| DEP-25 | Bio quasi-closure → intra-individual precursor | S18:223 | premise | explicit | consciousness window obtains on biological quasi-closure basis |
| DEP-26 | VED barrier / revised Vol.4 | S06:300–317 | historical citation | explicit | older PDE、effective projected resistance、fundamental external prohibitionではない |
| DEP-27 | VED nonclosure → opening/persistence | S09 Non-Closure、S12 Opening and Non-Closure | claimed correspondence | explicit | referencing loopのpersistence conditionとの対応 |
| DEP-28 | note series / L1,L2,L2.5,L3 | S17 Layered Translation / Relation to Appendices | claimed correspondence | explicit | 同じstructureの解像度別記述。本監査L0–L3列とは別のsource-local分類 |

集計: explicit 28、claimed derivation 1（DEP-10）、claimed identity 6（DEP-12/18/19/20/21/24）。これは主張文のinventoryであってderivation/identityの認定数ではない。historical citation 1はcurrent本文が歴史式を引用するためcurrent dependencyとして含めた。

`life attractor`は明示されるが、current ConsciousnessにBioの`second attractor` subsetを直接継承する記述は検索で所在しない。Intelligence IIのsecond-attractor参照はBioを直接参照するものとして§15で分離する。node rho、sigma、tau等の厳密同一性は本phaseで解決しない。IFGT current sourceではbalanceのtimeがtau、Consciousness templateではtであることもsource-version inventoryに留める。

## 4. Upstream closure inheritance

| Attribution target | Source | Inventory label | 継承されると書かれているもの / 留保 |
| --- | --- | --- | --- |
| fast/slow split | S01:43、S04:9–23、JA対応節 | PROPOSED ANALOGY | Bioがnecessityを確立したのではなく本稿のpremise |
| neural-like hierarchy | S04 Bio quote | PROPOSED ANALOGY | Bio toy staged roles。neural carrierや専用timescale結果を継承しないと明記 |
| life quasi-closure basis | S18 four-layer paragraph | INHERITED AS GIVEN | biological quasi-closure basis上にwindowがobtainsというsource wording |
| nonclosure / persistence | S06:215–250、S07 | REUSED AS VOCABULARY | VED観点を適用。proofの継承かはこの語だけでは決めない |
| SSO self-maintenance | S06:300–321 | CLAIMED DERIVATION | older PDE三項からmaintains、VED-grounded basisという言い方を保存 |
| Delta C window | S06 / figure6 | INHERITED AS GIVEN | same structural condition / correspondence。no groundingの限定も保存 |
| internal tau | S03 / S04 Internal Delay | UNSPECIFIED | local buffer、subjective timeではない。VED/IFGTとのtyped time mapは所在未固定 |
| information field | S06 Projected Uses | REUSED AS VOCABULARY | direct general-field identityを明示否定 |
| CT attractor Phi* / meaning wells | S09 CT quotes、S20 | INHERITED AS GIVEN | CT formally specified / same quantityという帰属 |
| boundary / observer | S04 Observer、S11、S14 | UNSPECIFIED | 本稿のtemporal boundary / self-maintaining reading。Bio膜からの明示継承ではない |
| generation sequence / four layers | S18:223、S20 | INHERITED AS GIVEN | proposed nonreductionとsame grammarの語を併記。監査closureからの成立推論とは記さない |
| second attractor | current Consciousness全TeX検索 | UNSPECIFIED | 直接のsubset継承はNOT LOCATED |

current本文が「上流監査CLOSEDなのでConsciousnessもvalid」と明示する文は所在しない。この不在と、上表の構造・basis帰属が存在することは別々に記録する。Bio帰属修復済みであることから、VED/CT/phenomenal関係まで修復・評価済みと推論しない。

## 5. Consciousness-specific object inventory

「specific」は本枝のlocal use / constructionであり、語そのものの歴史的独創性ではない。Formal欄の「記号/条件」はtyped realizationを意味せず、Operational欄の「未提示」は独立測定手順の所在についてのみ述べる。

| CON-OBJ | Object / term | First authoritative occurrence | Formal definition? | Operational definition? | Interpretive role | Upstream dependency |
| --- | --- | --- | --- | --- | --- | --- |
| CON-OBJ-01 | consciousness / opening / regime | S00、定式化S07/S12 | schematic関係・window | S16/S18で今後の課題 | 関係が開く状態 | VED/IFGT、fast/slow premise |
| CON-OBJ-02 | fast predictive layer / v_f | S00/S02、定義S03/S04 | 記号・役割 | neural rate対応未提示 | prediction/reaction | Bio analogy |
| CON-OBJ-03 | slow sedimentary layer / v_s | S00/S02、S03/S04 | 記号・役割 | 同上 | memory/integration | Bio / CT |
| CON-OBJ-04 | Delta v | S00、S03/S04 | difference式 | rate単位/推定未提示 | 非同期差 | closure差との対応 |
| CON-OBJ-05 | mu coupling viscosity | S00/S03 | 範囲・ratio内使用 | 測定未提示 | slip/adhesion | TCA analogy; IFGT mu_Iとは別表記 |
| CON-OBJ-06 | tau delay/buffer | S00/S03 | ratio・window | calibration未提示 | referencing thickness | upstream tauとの関係未固定 |
| CON-OBJ-07 | effective T / T_Phi | S00/S03、S05 | index式 | S18で未完成と明記 | transformation load | TCA、gradient |
| CON-OBJ-08 | I log density | S00/S03、local定義S06 | field記号・balance | brain/behavior map今後 | referenceable sedimented logs | IFGT I |
| CON-OBJ-09 | J_I / J_log | S00/S03、S06 | field/flow記号 | event/log測定map未提示 | local referencing flow | IFGT J |
| CON-OBJ-10 | Phi / meaning gradient / well | S00/S03、S06 | potential・gradient | meaning calibration今後 | selective referencing | IFGT / CT |
| CON-OBJ-11 | SSO orchestration | S04:27–37 | 文章定義、6条件 | specific anatomyを否定 | noncentral coordination | Bio motivation / VED |
| CON-OBJ-12 | SSO Self-Sustaining Observer | S04:199–222 | 同構造のreading | observer判別手順未提示 | own-log referencing loop | SSO / nonclosure |
| CON-OBJ-13 | plasticity gate | S04:126以降 | 文章passage condition | gate測定未提示 | partial writing / later constraint | fast/slow |
| CON-OBJ-14 | TCA | S05導入 | analogy + index | neural実装未提示 | temporal transformation mechanismとのsource主張 | converter / IFGT / VED |
| CON-OBJ-15 | log / retained trace / memory | S00/S04、定義S09 Slow Dynamics | re-referenceable structure | trace extraction未提示 | sedimentation / reuse | IFGT history / CT |
| CON-OBJ-16 | log-referencing feedback loop | S04、6-step記述S09 | 手順列・figure4 | 実装/観測protocol未提示 | fast→slow→potential→fast | SSO / IFGT |
| CON-OBJ-17 | ego | S05 From Attention to Ego | transformation position | phenomenological対応未提示 | experienced thinking/choosing locus | TCA |
| CON-OBJ-18 | self / self-model / narrative terrain | S01否定的導入、S12 Opening and Self | slow terrainという記述 | 判別未提示 | self-continuity / stable referencing pattern | loop / CT |
| CON-OBJ-19 | qualia / live foreground | S00、local同定S08/S11 | boundaryという記述 | direct storage/measurementを否定する立場 | phenomenal frontier | gate / fastslow |
| CON-OBJ-20 | sedimentation / closure frontier | S02、命名S11 | transitional boundary記述 | boundary判別未提示 | fastとlog間 | nonclosure |
| CON-OBJ-21 | conscious access / reportability | S01/S04、区別S09 | passage/report条件 | S10実験の解釈、独立mapなし | accessとreportはnot identical | logs/pathways |
| CON-OBJ-22 | measurement / residue / collapse | S00、S11/S13 | schematic変換 | 実験計画はfuture directions | live→report/log、quantum collapseと非同定 | frontier |
| CON-OBJ-23 | introspection | S13 Introspection | internal measurementという定義 | protocol未提示 | own-state verbalization | measurement/log |
| CON-OBJ-24 | consciousness stability window | S07 Internal Delay / Window | finite inequalities | empirical boundary今後 | regime / phase diagram | speed,viscosity,delay,index |
| CON-OBJ-25 | C_f / C_s / Delta C | S06 VED Closure Degree | local effective closure/difference | neural closure map未提示 | SSO window別座標とのsource主張 | VED C |
| CON-OBJ-26 | projection / mass assignment | S01予告、S06定義 | disproportionate influenceの文章定義 | weighting測定未提示 | attention/selection/prioritization | IFGT primitiveと呼称 / Intelligence共通stance |
| CON-OBJ-27 | action candidate / forward prediction | S04 fast layer、S09/S10 | dynamical役割 | Libetを再解釈 | action preparation precedes log reference | fastlayer |
| CON-OBJ-28 | reporting pathway / bottleneck | S09/S10 | 3条件の文章記述 | split-brain例、独立実装なし | verbal/behavioral access asymmetry | neural substrate |
| CON-OBJ-29 | rationalization / log completion | S10 Rationalization | coherence補完という記述 | 固有datasetなし | inaccessible log gap / self-continuity | slow logs |
| CON-OBJ-30 | regime deviations | S15/S16 | qualitative limits/phase labels | diagnostic theoryでないと明記 | synchrony,dissociation,fixation等 | consciousness window |
| CON-OBJ-31 | neural / bodily local substrate | S01、S14 Local Substrates | generic carrier記述 | region/rate対応はfuture | neural correlatesとconsciousnessの区別 | biological motivation |
| CON-OBJ-32 | conceptual attractor / action attractor | S09 CT quote、S10 Libet | Phi* / action-attractor wording | 本枝のtrajectory実装なし | memory landscape / action preparation | CT、fastlayer |

salienceは独立変数/定義として所在せず、意味勾配・情動重み・prioritizationの語で関連内容を記述。`access consciousness` / `phenomenal consciousness`を別のtyped objectsとして定義する表は所在せず、conscious access / explicit consciousness / qualia / subjective experienceの区別が散在する。prediction horizon、memory depth、global-state固有変数、数学的recursion operatorも本phaseでは所在しない。これらを既存概念の同義語として追加しない。

S06/S07のformal templateにはさらにD、mu_I、F、K、sigma、Tのscale factor kappaが現れる。これらはCON-OBJ-07–10の式の構成要素として所在を保存し、32のrole familiesとは別の独立biological objectsに数えない。全symbol/signatureの採番はPhase01に残す。

## 6. Formal / neural / cognitive / phenomenal layer map

Yはsourceがその層の役割・解釈を与えること、—は本表で付与しないこと。神経解釈があるだけでneural mechanismは認定しない。L0–L3は監査列であり、S17のL1=note / L3=formalとの取り違えを禁止する。

| Object / claim (CON-OBJ) | L0 | L1 | L2 | L3 | Explicit bridge? | Bridge source |
| --- | --- | --- | --- | --- | --- | --- |
| 01 opening regime | Y | — | Y | Y | 言語的同定/条件claim | PH-01/02 |
| 02 fast | Y | Y | Y | — | carrier対応をgenericに記載 | S14、rate mapは未固定 |
| 03 slow | Y | Y | Y | — | neural/bodily substrate記述 | S14 |
| 04 Delta v | Y | — | Y | — | closure差の対応claim | DEP-12 |
| 05 mu | Y | — | Y | — | transformation interpretation | S05/S07 |
| 06 tau | Y | — | Y | — | subjective timeそのものを否定 | S03/S04 |
| 07 T/T_Phi | Y | — | Y | Y | qualia clarityとの関係claim | PH-07 |
| 08 I | Y | — | Y | — | log densityのlocal map | S06 |
| 09 J | Y | — | Y | — | window-local flow | S06 |
| 10 Phi | Y | — | Y | Y | appearance biasの記述 | PH-06 |
| 11 SSO | Y | — | Y | — | consciousnessの必要条件として言及 | PH-02 |
| 12 observer | — | — | Y | — | subjectとの非同定 | S04 |
| 13 gate | Y | — | Y | Y | phenomenal surfaceというclaim | PH-05 |
| 14 TCA | Y | — | Y | Y | egoのexperienced position | PH-03 |
| 15 logs | — | Y | Y | — | slow biological substrateとの関係 | S09/S14 |
| 16 loop | Y | Y | Y | Y | neural participation / conscious state | PH-09、S14 |
| 17 ego | — | — | Y | Y | experienced location | PH-03 |
| 18 self | — | — | Y | Y | self-likeness / continuity | PH-10 |
| 19 qualia | — | — | — | Y | boundaryとの同定claim | PH-04/05 |
| 20 frontier | Y | — | Y | Y | transitional state experienced as qualia | PH-04 |
| 21 access/report | — | Y | Y | Y | explicit consciousnessとreportの接続 | PH-08 |
| 22 measurement/residue | Y | Y | Y | Y | live→residueとの変換claim | PH-11 |
| 23 introspection | — | — | Y | Y | own conscious-state measurement | PH-12 |
| 24 window | Y | — | Y | Y | regime条件とconsciousness | PH-01/13 |
| 25 closure difference | Y | — | Y | — | SSOとのstructural equivalence | DEP-12 |
| 26 projection | Y | Y | Y | — | physical/biological/artificial weightingを列挙 | S06 |
| 27 prediction/action | — | Y | Y | — | readiness potentialの解釈 | S10 |
| 28 report pathway | — | Y | Y | — | hemisphere/pathwayの解釈 | S10 |
| 29 rationalization | — | Y | Y | — | left-hemisphere例 / logs | S10 |
| 30 deviations | Y | — | Y | Y | dream-like等のqualitative claim | S15/S16 |
| 31 local substrate | — | Y | — | — | neural correlatesとconsciousnessを区別 | S14 |
| 32 attractors | Y | — | Y | — | CT / action analogy | S09/S10 |

層別集計は重複可: L0=21、L1=11、L2=30、L3=15。explicit phenomenal bridgeは§7の**13言語的claim families**。typed/operational bridgeを13件発見したという意味ではない。source自体がformal/cognitive条件からphenomenalな言い方へ接続する所在を数える。

## 7. Phenomenal identification inventory

引用符内は短い原文、残りはsourceのparaphrase。否定・留保も同じ行に残す。「opening」であることからphenomenal identification claimが存在しないとは推論しない。

| PH-ID | Current wording / claim | Exact location / heading | Wording class |
| --- | --- | --- | --- |
| PH-01 | consciousness = log-referenceable relation / regime。final definitionを目指すのではないとも記述 | S00:1、S01:4–6、S07 Window / Summary | DEFINITION; IDENTITY |
| PH-02 | finite differenceはconscious stateのnecessary condition。SSO itself is not yet consciousness | S04 Speed Differential / Minimal Conditions、S07 Non-Closure | NECESSITY |
| PH-03 | TCA corresponds to position experienced as ego。egoはsubject/causal controllerではない | S05 From Attention to Ego、S08 Ego as a Derived Position | CORRESPONDENCE |
| PH-04 | 「This transitional state is what is experienced as qualia」 | S11 Sedimentation Frontier:37–65 | IDENTITY |
| PH-05 | qualiaはgate通過のphenomenal surface、gate productsではない | S11 Qualia and the Plasticity Gate:101–124、S12 Consciousness Opens | CORRESPONDENCE; MECHANISM |
| PH-06 | meaning gradientがwhat appears in consciousnessをbiasする | S08 Meaning Gradient / S09 Meaning Gradient:107–129 | MECHANISM |
| PH-07 | T_Phiのintermediate rangeとqualia clarity、強さと自由を区別 | S11 Qualia and Effective Torque:126–143 | CORRESPONDENCE; MECHANISM |
| PH-08 | processingがexplicit consciousnessになるにはsedimentation / referenceability / reporting connection | S10 Experimental Correspondence:175–211、Summary:234以降 | NECESSITY; CORRESPONDENCE |
| PH-09 | fast→logs→potential→fastのnonclosed loopをconscious stateと記述 | S09冒頭:9–11、Referencing Loop:162–206 | IDENTITY; MECHANISM |
| PH-10 | selfはopening反復後に形成するslow terrain、self-likenessがsediment | S12 Opening and Self | DEFINITION; CORRESPONDENCE |
| PH-11 | measurement transforms live boundary into residue、qualia自体ではない | S11 Measurement:145–170、S13:31–73 | MECHANISM |
| PH-12 | introspectionはown-state internal measurement、captures residue | S13 Introspection:146–167 | CORRESPONDENCE; MECHANISM |
| PH-13 | 「stable consciousness」↔ window条件、qualitative/testable directions | S15 Summary、S12 From Product to Relation | SUFFICIENCY; NECESSITY; FORWARD CLAIM |

S11 Relation to the Hard Problemは「solved」を否定し、問いをboundary conditionsへ移すとする。S16 Limitsはqualia boundary記述がall subjective experienceを説明するものではないと述べる。この自己限定もinventoryに含め、成功/失敗判定はしない。

## 8. Fast / slow inventory

| FASTSLOW-ID | Claim | Source | Role | Evidence/source cited | Upstream dependence | Status wording |
| --- | --- | --- | --- | --- | --- | --- |
| FASTSLOW-01 | fast=prediction/reaction/error correction | S02、S04:13,43–47 | functional definition | source-local prose | Bio motivation | premise |
| FASTSLOW-02 | slow=memory/sedimentation/long-term structure | S04:15,49–54 | functional definition | source-local prose | Bio / CT | premise |
| FASTSLOW-03 | v_f-v_s、finite nonzero difference | S04:64–93、S07 | mathematical timescale variable / condition | displayed relations | VED correspondence later | necessaryと記述 |
| FASTSLOW-04 | no central control、local interference | S04 Orchestration | organization assumption | SSO definition | temporal nonclosure | adopted structure |
| FASTSLOW-05 | gate、mu、tau permit partial passage | S04 Gate / Internal Delay | coupling / delay condition | ratio and prose | local construction | appropriate range |
| FASTSLOW-06 | Bio toy does not confirm split | S01:43、S04:9–23、JA同節 | provenance / premise declaration | Bio source and audited handoff | explicit analogy | not confirmed / no dedicated diagnostic |
| FASTSLOW-07 | C_s-C_f corresponds to speed difference | S06:252–321、figure6 | structural correspondence | older VED PDE / figure | VED | same condition / grounded basisという別文も所在 |
| FASTSLOW-08 | Libet delay / split-brain pathway | S10 | experiment reinterpretation | named experiment types、個別bib keyなし | local log model | measured / showedというsource語 |
| FASTSLOW-09 | fast/slow neural activity / substrate | S14 Local Substrates、S18 Remaining Questions | biological interpretation / future map | generic neural activity、固有rateなし | model→neural | mapping future |
| FASTSLOW-10 | sleep/dream/anesthesia等でwindow changes | S15 Testable Directions、S16 | qualitative research target | proposed directions、datasetなし | local window | testable、not diagnostic theory |

速度変数と不等式はあるが、秒単位のrate specification、carrier-specific timescale推定、専用実験引用はこのbranchに所在しない。これは所在の記録であってadequacy判定ではない。SSOはFASTSLOW-01–05を必要条件として使用する。報告timestamp・external t・internal tau・experienced timeは別扱い。

## 9. SSO inventory

正式導入: **Speed-Scale Orchestration**（S04:27、JA S04:26）。同節後半に **Self-Sustaining Observer**（S04:204、JA:196）という「same structure can be read as」の読み替えがある。略称から片方を削除・統合しない。

| Component | Source-local object | Dependence / role | 記述上の接続先 |
| --- | --- | --- | --- |
| SSO-C01 | fast layer | prediction、reaction、current updating | C02/C04へのpartial sedimentation |
| SSO-C02 | slow layer / logs | retention、future fastへのconstraint | C01へfeedback |
| SSO-C03 | finite speed difference | complete synchrony/separationの間 | boundary/referenceability |
| SSO-C04 | plasticity gate | what sediments / what flows away | fastとslowのpassage |
| SSO-C05 | coupling viscosity | partial coupling / slip | C03/C06との関係 |
| SSO-C06 | internal delay/buffer | referenceable thickness | log formation |
| SSO-C07 | nonclosed self-maintaining loop | central controllerなしでown logsをreference | Observer reading |

7 componentsはS04のminimal conditionsをobject単位に分けた索引で、新modelではない。S04のenumerated条件は6件、S06のSSO conditionsは3件であり、同じ数の公理と仮定しない。S05のTCA、S06のI/J/Phi/projectionは後続のcoupler / formal extensionであって上表へ黙って同一化しない。図はfigure1、関連図figure2/4/6。式所在はS04 Speed Differential / Internal Delay、S07。observerはcontemplating subjectではないとsourceが明記し、consciousness自体でもないが必要構造とする。下流の明示SSO repriseはIntelligence I JA summary（DOWN-05）。

## 10. Self-reference inventory

recursion/self-referenceという語だけを数えるとown-log loopを落とすため、本文の関係familyとliteral occurrence indexを分ける。以下はcircularity分類ではない。

| SELF-ID | Use / location | Source treatment | Phenomenal relation |
| --- | --- | --- | --- |
| SELF-01 | S04 Observer:199–235 | informational own-log loop、self-sustaining organization | subjectを追加したのではないと記述 |
| SELF-02 | S09 Referencing Loop:162–206 | informational feedbackの6手順 | loopによりconscious stateが継続するclaim |
| SELF-03 | S09 Slow Dynamics / CT quote:61 | log re-reference、landscape sedimentation | stored logsとcurrent consciousnessの区別 |
| SELF-04 | S12 Opening and Self | cognitive self-model / terrain formation | self-likenessの解釈 |
| SELF-05 | S13 Introspection:146–167 | own-state observation / internal measurement | direct qualiaとresidueを区別するclaim |
| SELF-06 | S18 Higher-Order:58–75 | 他説のmeta-representationを紹介、本稿self-referenceを区別 | self-modelによる生成を採用しない |
| SELF-07 | S10 Rationalization:148–173 | cognitive coherence / inaccessible logs補完 | self-continuity / ego |
| SELF-08 | S06:319 | VED PDEからSSO自己維持への説明 | consciousness persistenceとの帰属 |
| SELF-09 | S14 neural-loop passages | neural feedback participationという解釈 | local correlateとconsciousnessの区別 |
| SELF-10 | S18:223、S19 Why Model Remains Open | theoryのnonclosureとobjectのnonclosureの類比 | theory resembles its objectというsource文 |

literal scan（case-insensitive `self.reference|self.model|recurs|own logs|self.sustaining|referencing loop|自己参照|自己モデル|再帰|自身のログ|自己持続|参照ループ`）は47 source lines。見出し・summary反復も含むので独立mechanismsの数ではない。全literal occurrenceを次表で所在固定する。

| Source | EN matching line numbers | JA matching line numbers | 主な分類 |
| --- | --- | --- | --- |
| S01 | 29 | 28 | neural-loop interpretation |
| S04 | 199,204,208,216,222,235 | 192,196 | informational loop / observer |
| S06 | 319 | — | self-maintenance wording |
| S09 | 61,162,180,202,228 | 184,201,223,247 | informational feedback / CT analogy |
| S14 | 79,123,153,171 | 82,148,186,215 | neural-loop participation |
| S16 | 191 | 303 | reference-loop vocabulary |
| S18 | 58,61,63,67,75,138,174,223,234 | 60,62,64,68,76,140,180,241 | self-model comparison / neural / cross-layer |

数学的recursion operatorまたはrecurrence algorithmを定義する実装は所在しない。図のloopをそのまま数学的再帰やneural feedback実測へ格上げしない。

## 11. Observer / boundary inventory

| BND-ID | Boundary / assumption | Source | Selected / defined / generated wording | Inventory status |
| --- | --- | --- | --- | --- |
| CON-BND-01 | biological-cognitive observation window | S01/S06 Projected Uses | local windowを先に指定 | preloaded / defined。coarse-graining ruleは未固定 |
| CON-BND-02 | fast/slow layer distinction | S02/S04 | two layersをconsider | preloaded、動的相互作用を記述 |
| CON-BND-03 | synchrony/disconnection limits | S04/S07 | finite inequalities | defined symbolic boundary |
| CON-BND-04 | plasticity gate | S04/S12 | passage boundary condition | defined / interpretive、specific anatomyではない |
| CON-BND-05 | sedimentation / closure frontier | S11 | transient relationと呼ぶ | dynamically described / phenomenal interpretation |
| CON-BND-06 | observer vs observing subject | S04 Observer | loopがstabilizeするとobserver-like | dynamically generated reading、subject非追加 |
| CON-BND-07 | self/world / internal/external | S12 Self、S19末 | self terrain / world relation | interpretive。独立system-boundary抽出なし |
| CON-BND-08 | processing vs report pathway | S09/S10 | verbal/behavioral pathway connection | biological example + functional boundary |
| CON-BND-09 | subject/object of measurement | S13 | measurement stabilizes and logs | interpretive、external non-disturbing observerを否定 |
| CON-BND-10 | consciousness vs local substrate | S14 | multi-local temporal relation | interpretive nonidentity |
| CON-BND-11 | VED observation regime vs conscious window | S06 / figure6 | Delta C側との対応 | inherited vocabulary / claimed correspondence |
| CON-BND-12 | within-individual vs externalized stopping | S18、Intelligence I §9 | transitional consciousness layer | downstream comparison。generated biological boundaryとしない |

system/environmentの厳密partition、reporting/access boundary、self/world boundary、計算grid境界は同一ではない。branch内にtoy gridは所在しない。observer-selection dependenceの是非、generated subjectの成否はここでは扱わない。

## 12. Time / ordering inventory

| TIME-ID | Object | Formal status | Biological status | Cognitive status | Phenomenal status | Upstream relation |
| --- | --- | --- | --- | --- | --- | --- |
| TIME-01 | t | physical externally measurable、field derivatives | generic recording time | update coordinate | experienced timeと同定なし | IFGT current tauと別 |
| TIME-02 | tau | proportional delay / range | calibration未固定 | buffering / retention | not subjective time itself | VED/IFGT tauとのmap未固定 |
| TIME-03 | v_f | fast rate symbol | neural activityのgeneric対応 | future prediction/reaction | consciousness自体ではない | Bio analogy |
| TIME-04 | v_s | slow rate symbol | neural/bodily substrate記述 | past memory / sedimentation | consciousness自体ではない | Bio / CT |
| TIME-05 | Delta v | difference + bounds | timescale実測なし | coupling asymmetry | consciousness necessary conditionというclaim | Delta C correspondence |
| TIME-06 | tau window / thickness | symbolic min/max | neural推定future | integration / reference window | time-sense fragmentationとの記述 | local |
| TIME-07 | preparation→sedimentation→timestamp | schematic order | Libet reinterpretation | report delay | reportable intention | experiment-type prose |
| TIME-08 | loop recurrence / subsequent prediction | six-step explanatory loop | neural carrier generic | repeated log update | conscious continuity | IFGT / CT |
| TIME-09 | long-time Phi* / tau→infinity | CT correspondence expression | local biological実装なし | stabilized concept/memory terrain | consciousnessそのものとの同定なし | CT |
| TIME-10 | experiential time / self-continuity | 独立symbolなし | — | report/contextに関与 | experienced lag / time sense | tauから自動同定しない |
| TIME-11 | note L1→L3 / four-layer sequence | explanatory/navigation order | biological layerという位置づけ | consciousness→self→intelligence | phenomenal emergence order未固定 | S17/S18/S19 |

simulation step/DT、具体memory-depth、prediction-horizon値はConsciousness固有実装として所在しない。S09 six-step orderはsourceのclaimとして保存し、因果同定や生物生成順の証明とは数えない。

## 13. Evidence / artifact inventory

| EVID-ID | Evidence type | Location | Direct / illustrative | External data? | Consciousness-specific? |
| --- | --- | --- | --- | --- | --- |
| EVID-01 | formal equations / effective constraints | S04–S07、S09、S15等 | source-local formal | NO | YES |
| EVID-02 | definitions / assumptions | S03/S04/S06/S07 | direct definitional | NO | YES |
| EVID-03 | conceptual figures | 6 families、§16 | schematic / illustrative | NO | YES |
| EVID-04 | Bio finite toy reference | S04 quote | upstream model reference、local runではない | NO biological dataset | NO（upstream） |
| EVID-05 | Libet-type observations | S10:22–67 | existing-experiment reinterpretation | named empirical topic、data fileなし | interpretation YES |
| EVID-06 | split-brain / rationalization | S10:90–173 | existing-experiment reinterpretation | named empirical topic、data fileなし | interpretation YES |
| EVID-07 | neuroscience substrates / correlates | S01/S14/S18 | generic substrate/correlation discussion | 固有neural datasetなし | YES |
| EVID-08 | psychology / theory comparisons | S06 psychological projection、S18 GW/IIT/HOT/PP | literature-type background prose | branch refsに対応entryなし | YES |
| EVID-09 | phenomenological examples | S11 red/pain/sound/here-now、S05 ego | illustrative lived examples | subject recordsなし | YES |
| EVID-10 | storage/copy / measurement thought cases | S12/S13 | conceptual reasoning | NO | YES |
| EVID-11 | clinical / altered-state examples | S15/S16 | qualitative regime analogies、diagnosisではない | clinical datasetなし | YES |
| EVID-12 | testable directions | S13 Experimental Implication、S15 | proposed measurements / predictions | completed testではない | YES |
| EVID-13 | bibliography citation | refs.bib、S06/S18/S20 | Intelligenceを参照 | repository manuscript | cross-branch |
| EVID-14 | CT correspondence | S04/S05/S09/S20 | source prose/table、formal comparisons | external datasetではない | cross-branch |

存在しない型をevidence entryとして水増ししない。Consciousness-local executable simulation、model-data comparison、CSV/TSV/measurement JSON、accession ID、downloaded neuroscience dataset、empirical protocol/result fileはbranchの全local tree検索で所在しない。refs.bibの唯一のentryはIntelligence（2026、Endoh）。両entryにbibliography接続、本文に`cite{Intelligence}`あり。Libet / split-brain / neuroscience / psychologyの個別出典keyはこのbibにない。本文の実験言及があることと、対応dataがrepositoryにあることを分離する。文献を外部で取得して補わない。

## 14. Empirical / phenomenological wording inventory

広い語検索はEN/JA42 section filesで1,444 matching lines（大文字小文字非区別、consciousness/意識も含む）。これはclaimsの数ではない。以下は内容別の**28 claim-location families**。同じ節のEN/JA対応とsummary反復を独立証拠として重複計上しない。

| WORD-ID | Current-facing location | Wording / content class（評価ではない） |
| --- | --- | --- |
| WORD-01 | S00:1 | consciousness as relation、subject matter |
| WORD-02 | S01 Four Declarations | neural correlate / generated object / projectionを区別するposition |
| WORD-03 | S02 boundary paragraph | consciousness opens before full sedimentation |
| WORD-04 | S04 Bio motivation | 「not a confirmed Bio-IFGT result」 |
| WORD-05 | S04 Minimal Conditions | necessary temporal structure、not yet consciousness |
| WORD-06 | S05 From Attention to Ego | humans experience thinking/choosing位置 |
| WORD-07 | S06 Projected Uses | observation-window coordinates、nonidentity |
| WORD-08 | S06 VED Closure Degree | self-maintenance / grounded basis / structural equivalence |
| WORD-09 | S07 Window / Summary | conditions for consciousness、not measurement equation |
| WORD-10 | S08 Meaning Gradient | memory/emotion/narrative enters conscious referencing |
| WORD-11 | S09 Referencing Loop | loop persistence / conscious state |
| WORD-12 | S09 Conscious Access and Report | reportability not identical to conscious state |
| WORD-13 | S10 Libet-Type:22–67 | recorded brain activity / measured delay / interpretation |
| WORD-14 | S10 Split-Brain:90–121 | behavioral response / no verbal report / what experiments show |
| WORD-15 | S10 Rationalization:148–173 | observed confabulation interpreted as log completion |
| WORD-16 | S10 Experimental Correspondence:175–211 | evidence / explicit consciousness / same structure |
| WORD-17 | S11 Qualia Problem:14–35 | redness/pain/sound/here-now、genuinely experienced |
| WORD-18 | S11 Frontier/Gate:37–124 | experienced as qualia、phenomenal surface |
| WORD-19 | S11 Effective Torque:126–143 | qualia clarity and vividness |
| WORD-20 | S11 Measurement / Hard Problem | observable traces、does not claim solved |
| WORD-21 | S12 Storage / Copy / Self | consciousness not stored、self sediments |
| WORD-22 | S13 Precision / Measurement Window | measurement succeeds / changes regimeというsource解釈 |
| WORD-23 | S13 Introspection / Experimental Implication | subjective report、own-state observation、futuremeasurements |
| WORD-24 | S14 Neural Correlates | correspondence important but not identity |
| WORD-25 | S15 Predictions / Testable Directions | subjective report / sleep / anesthesia等のqualitative予測 |
| WORD-26 | S16 Limits | map incomplete、not all subjective experience、not diagnostic |
| WORD-27 | S18 Remaining Questions / comparisons | measurable definition incomplete、empirical window undetermined |
| WORD-28 | S19 futurework / S20 correspondence | proposed structure、data mapfuture、qualia/insight same-boundary wording |

検索語: `observed / measured / confirmed / demonstrated / validated / consistent with / explains / predicts / accounts for / phenomenology / subjective / qualia / experience / awareness / consciousness` および `観測 / 測定 / 実証 / 確認 / 検証 / 再現 / 説明 / 予測 / 主観 / クオリア / 体験 / 意識`。sourceの「shows」「measured」を本監査のempirical confirmationに置換しない。

## 15. Downstream Intelligence dependency inventory

Intelligence IIのJAは`sections/*_ja.tex`であり`sections_ja/`ではない。ConsciousnessがIntelligenceを引用する逆向きもDEP-17/24に残す。相互引用を直ちにcircularityとしない。

| DOWN-ID | Consciousness object | Intelligence location | Claimed relation | Identity / analogy / reuse / derivation |
| --- | --- | --- | --- | --- |
| DOWN-01 | fast/slow log referencing / window | [I EN introduction](../../intelligence-part1/sections/01_introduction.tex):15、[JA introduction](../../intelligence-part1/sections_ja/01_introduction_ja.tex) | individual windowとlocal horizon-form | same differential-development structureのprojectionというclaimed correspondence |
| DOWN-02 | projected uses / I,J,Phi | [I JA IFGT vocabulary](../../intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex):92 | Consciousnessと同様のeffective-coordinate stance | vocabulary/method reuse |
| DOWN-03 | fast/slow gap、synchrony/dissociation | [I EN §9](../../intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex):67–83、[I JA §9](../../intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex) | four-layer table / figure comparison | proposed structural comparison、no common carrier/mechanismを記載 |
| DOWN-04 | log referencing / transitional layer | [I JA §8](../../intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex):373–375、I JA §9 | lifeとintelligenceの間のintra-individual precursor | claimed correspondence、stoppingそのものと分離 |
| DOWN-05 | SSO / TCA / window / variables | [I JA summary](../../intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex):141–161 | Consciousness対象を列挙、SSO minimal conditions | explicit reuse / attribution |
| DOWN-06 | temporal nonclosure inside individual | [I EN summary](../../intelligence-part1/sections/10_summary_convergence_and_outlook.tex):55–67 | externalized stoppingにcomplementary | analogy / division of roles |
| DOWN-07 | projection / projected uses | [II EN preliminaries](../../intelligence-part2/sections/01_preliminaries.tex):6、[II JA preliminaries](../../intelligence-part2/sections/01_preliminaries_ja.tex):33 | consciousness stanceをfollows | explicit reuse |
| DOWN-08 | projection primitive | [II JA inference](../../intelligence-part2/sections/02_inference_operator_ja.tex):156 | stopping operatorを設置できる領域のprojection | intelligence-layer action / claimed correspondence |
| DOWN-09 | projection as unequal influence | [II EN stopping](../../intelligence-part2/sections/05_emergent_stopping_layer.tex):80、[II JA stopping](../../intelligence-part2/sections/05_emergent_stopping_layer_ja.tex):236–245 | consciousness definitionをstopping contextへ適用 | definition reuse / realization claim |
| DOWN-10 | structural vs psychological projection | II JA stopping:245、[II JA animism](../../intelligence-part2/sections/06_animism_ja.tex):40 | 応答性の投影にもsame definition / disclaimer | vocabulary reuse / claimed application |
| DOWN-11 | consciousness/window scope exclusion | I EN introduction:58、I JA §3/§5、I JA §9:288 | intelligenceからsubjective experienceを直接同定しない | scope relation / distinction |
| DOWN-12 | future prediction / language / social logs | S18 Toward Consciousness,Self,Intelligence、S19; I summaries | Consciousness側から後続Intelligenceへhandoff | forward dependency、completed derivationではない |

SSOの直接引用はDOWN-05、fast/slowはDOWN-01/03、closure/windowはDOWN-01/04/06、projectionはDOWN-02/07–10。IIのL_R recursive logs / L_E second attractorを、ConsciousnessのloopまたはSSOと直接同一視するlocatorは今回の直接引用検索では所在しない。II JA preliminaries:251のsecond-attractor antecedentはBioであり、Consciousness経由と推定しない。memory/prediction/recursionの共有語だけで新しいDOWN行を作らない。

## 16. Figure / PDF / distribution inventory

### 16.1 Figure families

全図はschematic/conceptual。empirical image / model-generated simulation outputのsource表示はない。SVG/PNGを原生成codeの代用にはしない。図内の矢印・等価語は関係claimとして記録し、導出の証拠とは扱わない。

| FIG-ID | File EN / JA | Caption / section | 概念関係 / visual claim | PDF掲載番号、物理page EN / JA |
| --- | --- | --- | --- | --- |
| FIG-01 | [figure1](../../consciousness/figures/figure1_sso_density.pdf) / [JP](../../consciousness/figures_ja/figure1_sso_density_jp.pdf) | Minimal SSO / S04 | fast/slow間のconscious access、finite gap/delay/viscosity | Figure 1、8 / 8 |
| FIG-02 | [figure2](../../consciousness/figures/figure2_tca.pdf) / [JP](../../consciousness/figures_ja/figure2_tca_jp.pdf) | TCA / S05 | rotating coupling、logs/gradient/prediction feedback | Figure 2、13 / 13 |
| FIG-03 | [figure3](../../consciousness/figures/figure3_nonclosure_window.pdf) / [JP](../../consciousness/figures_ja/figure3_nonclosure_window_jp.pdf) | two-axis nonclosure phase diagram / S07 | conscious access領域とsynchrony,dissociation,fragmentation,fixation | Figure 4、28 / 31 |
| FIG-04 | [figure4](../../consciousness/figures/figure4_log_referencing_loop.pdf) / [JP](../../consciousness/figures_ja/figure4_log_referencing_loop_jp.pdf) | log-referencing nonclosure loop / S09 | fast→gate→slow→I/Phi→gradient→fast、open gap | Figure 5、37 / 42 |
| FIG-05 | [figure5](../../consciousness/figures/figure5_qualia_boundary.pdf) / [JP](../../consciousness/figures_ja/figure5_qualia_boundary_jp.pdf) | qualia boundary / S11 | live frontierからmeasurementによるresidue、phenomenal同定の図示 | Figure 6、45 / 51 |
| FIG-06 | [figure6](../../consciousness/figures/figure6_observation_regime.pdf) / [JP](../../consciousness/figures_ja/figure6_observation_regime_jp.pdf) | SSO/VED mapping / S06 | structural equivalence、same condition、neither grounds other; causal identityではないとの図内限定 | Figure 3、21 / 23 |

図ファイルの番号とpaperの連番は別。S06でfigure6を先にinputするのでこの順になる。figure3内のDelta v_minを含む表示と本文window、diagramの温度/密度/速度の語の関係はPhase01へ保留し、図や式を修正しない。

### 16.2 Distribution

| Artifact | Current-facing / build relation | Inventory result |
| --- | --- | --- |
| EN main.pdf | canonical ENの配布 | 83 pages、abstract +20 sections + bibliography、6 figures。projected uses、修復済みBio fast/slow premise、VED closure対応、qualia boundaryをtext確認 |
| JA main_ja.pdf | modular JAの配布 | 97 pages、同じ20 sections、6 figures。SSO定義、Bio premise、qualia/measurement/current captionsをtext確認 |
| figure PDFs | 12 tracked inputs | 全source参照先が存在、全EN図6枚、EN本文page21、JA本文page42をrenderして視認 |
| SVG / PNG | ignored local derivatives | 18 files、buildで直接使用されない。source-of-truthに昇格しない |
| drafts | ignored working/historical | 2 local files、status annotationがある。PDFのauthorityではない |
| branch README / GIF / simulation artifacts | dedicated current artifacts | NOT LOCATED |

PDF SHA-256: EN `1c0aa1b06a0323582ae20aef4bd95aa9ee297116742bccef9d66070835245ee3`、JA `dcadebf39d11013eabf3d936d396fb73fbc86be5c1028152b7c0e2244b0faed3`。

Freshnessは**section/figure inclusionと主要current wordingのspot-check対応**。再build比較・全数式のPDF/source同一性・全翻訳parityを認定する最終distribution auditではない。EN titleはNon-Generative Account / Cross-Scale Log Referencing、JA subtitleはSSO/TCAを含みauthorもEN=Yuhki Endoh / JA=IFGT Project。差を消さずversion metadataとして記録する。

PDF skillを使用。Popplerが所在しなかったため、既存pypdfでtext/pages、Ghostscriptで一時PNG renderを確認した。理論figureは再生成していない。一時資料は `${TEMP_EVIDENCE_ROOT}/consciousness_phase00.fm3cHT/`、repositoryへ追加しない。

## 17. Open uncertainties from Phase 00

OPENはinventory上の未固定事項であり、source claimがfalse/invalidというdispositionではない。

| CON-U | Unresolved identity / dependency | Why unresolved / source trace | Later inventoryへのhandoff |
| --- | --- | --- | --- |
| CON-U-001 | current IFGT vs Consciousness template version | t/tau、J/J_I/J_log、F/F_I、K*Iのsource別表現。DEP-08 | equation/source locator |
| CON-U-002 | VED C / C_f,C_s / Delta v | same coordinates/conditionとlocal definitionsの関係。DEP-11/12 | symbol/domain/signature |
| CON-U-003 | older VED PDEのexact authority | S06がolder / phenomenological / Vol.4と記載、current equation/role locatorをさらに固定する必要 | upstream dispositionを再判定せず引用同定 |
| CON-U-004 | no groundingとVED-grounded basis | S06:319–333内の別文言を両方保存 | relation wording / later role |
| CON-U-005 | SSO二展開名と条件集合 | 6 minimal conditions、S06の3 conditions、Observer reading | object identity、必要十分表現 |
| CON-U-006 | fast/slow rate / neural carrier | premiseは明示、neural measurement specificationは未固定 | rates/units/carrier map |
| CON-U-007 | t / tau / experienced time | source-local delayは定義、体験時間そのものを否定 | temporal signatures |
| CON-U-008 | observation/coarse-graining window | projected usesは明示、選択手順・尺度・boundary extractionは未固定 | observer/domain inventory |
| CON-U-009 | I/J/Phi/projection operational map | S16/S18がneural/behavioral/report対応をfutureと記載 | variable vs observable |
| CON-U-010 | functional conditions→phenomenal identification | PH-01–13に文章接続、typed/operational bridgeの所在別問題 | bridge-claim identity、説明成否は未判定 |
| CON-U-011 | qualia / access / report / explicit consciousness | S09区別とS10接続、S11境界同定 | object/signature |
| CON-U-012 | self / ego / Observer roles | S04/S05/S12/S18の各local description | 同じselfを推定しない |
| CON-U-013 | Libet / split-brain empirical provenance | named experiment typesはあるが個別bib/data locatorはない | evidence inventoryの後続詳細 |
| CON-U-014 | CT exact correspondence | CT §2.4/4.2/4.4/6.1参照、same quantity/isomorphic/positivity | source-specific map。CTを独立監査しない |
| CON-U-015 | note series / L1–L3 locator | S17説明はあるが別note/appendixのexact path/version未固定 | authority。監査L0–L3と非同一 |
| CON-U-016 | 4-layer / Intelligence bidirectional reference | DEP-17/24、DOWN-01–12 | direction / premise / identity claimを分離 |
| CON-U-017 | figure formula/label vs body | diagram phase bounds、density/speed/temperature labels、numbering | figure-symbol inventory |
| CON-U-018 | distribution exact lineage / full EN-JA correspondence | pages/major sectionsのspot-checkのみ、local figure exportsの生成履歴なし | 後続distribution/version確認 |

## 18. Hard gates for Phase 01

以下はinventory guardであり結論ではない。sourceがそれらを同定・導出する場合はclaimとして保存し、監査者がbridgeを補わない。

- upstream vocabulary reuse ≠ upstream derivation
- Bio analogy ≠ neural mechanism
- formal object ≠ neural carrier
- neural carrier ≠ cognitive function
- neural / cognitive dynamics ≠ phenomenal consciousness
- cognitive function / functional organization ≠ phenomenal experience / subjective experience
- formal correspondence ≠ phenomenal identification
- self-reference ≠ vicious circularity
- observer boundary ≠ generated subject
- fast/slow ordering ≠ experienced time
- downstream reuse ≠ Consciousness established result
- upstream audit/core closure ≠ Consciousness validity / phenomenal explanation

監査L0–L3、S17説明層L1–L3、physical/biological/consciousness/intelligence四層は別の分類。section order、explanatory order、dependency order、formal derivation order、biological generation order、phenomenal emergence orderを同一と仮定しない。S09 six-step loop、S18/S19 consciousness→self→intelligence、S20 correspondenceの順序はsourceが述べる関係としてのみ保持する。

## 19. Stop boundary

### Counts（集計単位を固定）

| Metric | Count / scope |
| --- | --- |
| current-facing text sources | 45 = entries 2 + included sections 42 + bib 1 |
| working/historical text | 2 combined、historical-only separate 0 |
| section order | abstract +20 numbered sections、21 includes per language |
| current figures | 6 families /12 EN-JA figure PDF files |
| PDFs | main distribution 2、figure含むtotal14 |
| explicit upstream dependencies | 28 DEP families |
| claimed derivations / claimed identities | 1 /6（primary wording classes） |
| Consciousness-specific object families | 32 |
| L0 / L1 / L2 / L3 objects | 21 /11 /30 /15（overlapping） |
| explicit phenomenal bridge claims | 13 language-level families、operational bridge認定ではない |
| fast/slow claim families | 10 |
| SSO components | 7（sourceのenumerated conditionsは6） |
| self-reference usages | 47 matching lines、10 documentary relation families |
| observer/boundary assumptions | 12 |
| time/order objects | 11 |
| evidence-type entries | 14 |
| empirical/phenomenological locations | 28 claim-location families、raw search1444 lines |
| downstream Intelligence dependencies | 12 |
| unresolved inventory items | 18 |

Validation: source/relative-link existence、42 include targets、20 section order EN/JA、12 figure paths/labels、14 PDF existence、current/working separation、Markdown tables/fences/display delimiters、各ID一意性とcounts、`git diff --check`を確認。branch全237 filesと既存repository snapshotを照合し、source/式/code/図/PDF/upstream/downstreamの変更0。新規作成は本recordと[README](README_ja.md)のみ。

このPhaseでは個々の式の全件ID採番・role/evidence grading・circularity/phenomenal success判定・revision dispositionを開始していない。**Phase 00 COMPLETE。Phase 01 equation / symbol / object inventoryには進まず停止する。**

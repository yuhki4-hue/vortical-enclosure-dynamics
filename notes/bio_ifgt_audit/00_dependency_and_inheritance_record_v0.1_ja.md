# Bio-IFGT dependency / inheritance record v0.1

## 0. Status and non-results

- date: 2026-09-08
- Bio-IFGT audit: **IN PROGRESS**
- Phase 00 dependency / inheritance: **COMPLETE**
- Phase 01 equation / symbol inventory: **NOT STARTED**
- upstream VED equation audit / core revision: **CLOSED / CLOSED**
- inventory / dependency mapping only
- source / equation / code / generated artifactの変更: **NO**
- new equation / notation / theory / bridge: **NO**
- evidence grading / empirical-validation verdict / emergence verdict: **NOT PERFORMED**

本記録は「何がどこに書かれ、何を参照しているか」を固定する。引用されたclaimはsourceの発言であり、
監査者の結論ではない。「mapをlocateしていない」は不存在・不可能性の証明ではない。
working source間の表記差も保持する。以下のIDは監査索引であり理論notationではない。
00の予備的equation所在表は01のsymbol/domain同定を先取りしない。

## 1. Upstream authority and inheritance gates

最初に読んだauthority:

1. [frozen final dispositions 06](../ved_equation_audit/06_final_audit_record_v1.0_ja.md)
2. [final closure recheck v1.1](../ved_equation_audit/implementation_final_closure_recheck_v1.1_ja.md)
3. [upstream audit README](../ved_equation_audit/README_ja.md)

06の「implementation未開始」は当時の状態であり、現在のclosureはv1.1に従う。
v1.1は **PASS WITH CLERICAL ADVISORIES — CLOSE**、44 dispositionsの実装closureである。
Bio-IFGTの生物学的claimを承認した結果として輸入しない。
KEEP 11 / REVISE 4 / DOWNGRADE 13 / SPLIT 6 / OPEN 10 / RETIRE 0を変更しない。

補助的に現行[IFGT fundamental dynamics](../../Information-Field-Geometry-Theory/sections/fundamental_dynamics.tex)
と[IFGT internal unified equation](../../Information-Field-Geometry-Theory/sections/unified_equation.tex)を再読した。
IFGT内部のbalance/evolutionはRC-038のdeclared scope、VEDとのidentityは別問題である。
non-closureの語彙を持つことだけで、Bioの実体・機構・測定へのmapが継承されるとはしない。

以下を最初のhard gatesとして固定する。いずれも評価結果ではなく、後続監査のguardである。

\[
\text{source-local definition}\neq\text{cross-layer identity}
\]
\[
\text{formal field dynamics}\neq\text{biological mechanism}
\]
\[
\text{cross-layer correspondence}\neq\text{mechanistic derivation}
\]
\[
\text{simulation witness}\neq\text{empirical validation}
\]
\[
\text{model state variable}\neq\text{biological observable}
\]
\[
\text{VED / IFGT OPEN bridge}\neq\text{Bio-IFGT inherited established result}
\]

さらにsimulation outputとempirical observationを区別する。
source-localな同じglyph、類似した式形、引用、同じ階層図だけでcross-source identityを推定しない。

## 2. Discovery scope and source selection

repository全体の通常検索対象textに対して、Bio-IFGT、biological、metabolism、membrane、
homeostasis、self-maintenance、cell、organism、viability、dissipation、closure、
information field、IFGT、VED、emergence、simulation、observable、experiment、validation、
consciousness、cognitionをcase-insensitive検索した。生物学的対応箇所では日本語の生命・準閉包・観測・
環境・同一・対応・実験も確認した。外部web、外部bibliography本文、外部datasetにはアクセスしていない。

直接Bio参照のあるfileを抽出し、main entryのinput、README/navのincoming link、simulationの
read/write経路を確認した。広いVED/closure hitをすべてBio authorityとはしない。
Bio directoryではgit-tracked 47 filesを確認した。内訳はTeX 17、working Markdown 13、
README 2、handoff 1、bibliography 1、code 1、requirements 1、figure PNG 7、
PDF 2、LICENSE 1、outputs/.gitignore 1。

### Source hierarchy and versions

- ENはS01が15 section TeXを直接inputする。
- JAはS02のself-contained TeX。13 working Markdownを直接inputする構造ではない。
  したがってworking notesとJA配布本文を同じ版として合算しない。
- PDF 2件はtop-levelから現行配布としてリンクされる。00では配布経路をinventoryし、
  PDF build freshness、描画、本文との完全一致は試験していない。
- 7 tracked PNGはpaperからincludeされるmodel-generated図。photograph/measurementとは分類しない。
- outputsには別名PNG/GIFなどignored local artifactsも存在する。存在と由来の確定を分ける。
- handoffはREADMEから現行参照される設計memoだが「paper skeleton only」とも書く。
  historical-onlyと断定せず、publication proseとは別authorityにする。
- CHANGELOGはhistorical record。downstream draftもREADMEがsourceと指定する場合は、
  古い表現があるという理由だけでhistorical-onlyにしない。

## 3. Source inventory

表のS-IDはsource単位／明示したsource群。個別file数とは異なる。
「current-facing」は現在のentry/input/linkからの到達性を表し、妥当性や版一致の評価ではない。

| Source ID | File | Role | Current-facing? | Upstream dependency stated? | Bio-specific content? |
|---|---|---|---|---|---|
| S01 | [main.tex](../../bio-ifgt/main.tex) | EN manuscript entry、15 sectionsをinput | YES | title/sections経由 | YES |
| S02 | [main_ja.tex](../../bio-ifgt/main_ja.tex) | JA manuscript、本文内蔵 | YES | IntroductionでIFGT | YES |
| S03 | [abstract](../../bio-ifgt/sections/abstract.tex) | paper scope | YES/S01 | minimal field description | DNA、life、second attractor |
| S04 | [introduction](../../bio-ifgt/sections/introduction.tex) | primary inheritance declaration | YES/S01 | IFGT明示、I非同一 | biological observation window |
| S05 | [intuitive picture](../../bio-ifgt/sections/intuitive_picture.tex) | informal picture | YES/S01 | field vocabulary | molecule/cell/form |
| S06 | [formal mapping](../../bio-ifgt/sections/formal_mapping.tex) | field/state/time source definitions | YES/S01 | I/J/Phi field形式 | coarse biological variables |
| S07 | [core equations](../../bio-ifgt/sections/core_equations.tex) | primary equation source | YES/S01 | balance/flow形 | system-dependent potential |
| S08 | [gene information flow](../../bio-ifgt/sections/gene_information_flow.tex) | DNA/events/thresholds | YES/S01 | quasi-closure解釈 | theta、gene events |
| S09 | [development](../../bio-ifgt/sections/development_morphogenesis.tex) | morphogenesis application | YES/S01 | field description | morphogen/cell fate |
| S10 | [life attractor](../../bio-ifgt/sections/life_attractor.tex) | life/state-space definitions | YES/S01 | sustained dynamics | viable region、regeneration |
| S11 | [probability revision](../../bio-ifgt/sections/probability_revision.tex) | region-entry interpretation | YES/S01 | IFGT quasi-closure明示 | life-emergence probability |
| S12 | [intelligence second attractor](../../bio-ifgt/sections/intelligence_second_attractor.tex) | downstream forward reference | YES/S01 | life attractor基盤 | retained/reused history |
| S13 | [relation to note](../../bio-ifgt/sections/relation_to_note.tex) | L3/L1 correspondence | YES/S01 | descriptive-layer relation | life/intelligence exposition |
| S14 | [minimal developmental simulation](../../bio-ifgt/sections/minimal_developmental_simulation.tex) | toy model manuscript | YES/S01 | quasi-closure interpretation | M/I/N/B/E |
| S15 | [simulation results](../../bio-ifgt/sections/simulation_results_visualization.tex) | numerical-run / figure report | YES/S01 | Bio interpretation | model output observations |
| S16 | [discussion](../../bio-ifgt/sections/discussion.tex) | limitations / future work | YES/S01 | IFGT correspondence | empirical forms/time未指定 |
| S17 | [conclusion](../../bio-ifgt/sections/conclusion.tex) | scope summary | YES/S01 | field vocabulary | future applications |
| S18 | [Bio README](../../bio-ifgt/README.md) | project entry/guide | YES | biological coarse-graining of IFGT/VED | YES |
| S19 | [sections_ja](../../bio-ifgt/sections_ja/)（13 files、下表） | Japanese working sections | READMEに所在案内、build inputではない | Introduction明示 | YES、別表記あり |
| S20 | [handoff](../../bio-ifgt/notes/handoff.md) | design/terminology memo | READMEから参照 | VEDをforegroundしない方針 | DNA parameter、life、second attractor |
| S21 | [simulate.py](../../bio-ifgt/simulations/minimal_neural_field/simulate.py) | executable finite model | YES | docstringでBio IとIFGT Iを分離 | YES |
| S22 | [simulation README](../../bio-ifgt/simulations/minimal_neural_field/README.md) | model/run documentation | YES | I非同一明示 | toy/not realistic embryogenesis |
| S23 | [requirements](../../bio-ifgt/simulations/minimal_neural_field/requirements.txt) | runtime dependencies | YES/model | NO | NumPy/Matplotlib/imageio/Pillow |
| S24 | [outputs](../../bio-ifgt/simulations/minimal_neural_field/outputs/) 7 tracked PNG | generated figures | YES/paper include | model-mediated | YES/model-generated |
| S25 | [main.pdf](../../bio-ifgt/main.pdf) / [main_ja.pdf](../../bio-ifgt/main_ja.pdf) | distributed manuscripts | YES/top README | source由来、freshness未試験 | YES |
| S26 | [refs.bib](../../bio-ifgt/refs.bib) | bibliography 8 entries | available、entryにbibliography呼出なし | external literature metadata | development/RD/attractor/FEP等 |
| S27 | [root EN](../../README.md) / [root JA](../../README_ja.md) | overview / PDF navigation | YES | IFGT/VED biological coarse-graining | life/development/gene constraints |
| S28 | [concept map](../../docs/navigation/concept_map.md) / [reading paths](../../docs/navigation/reading_paths.md) | current navigation | YES | IFGT→Bio reading order | branch定位 |
| S29 | [enactivism](../../docs/navigation/enactivism_comparison.md) / [FEP](../../docs/navigation/fep_comparison.md) / [neighbors](../../docs/navigation/conceptual_neighbors.md) / [relationships](../../docs/navigation/theory_relationships.md) / [misreadings](../../docs/navigation/common_misreadings.md) | cross-reference guides | YES | comparison語彙 | maintenance、organism/environment |
| S30 | [CHANGELOG](../../CHANGELOG.md) 133–139,177付近 | historical change record | historical-only | Bio追加/非同一注記の履歴 | YES |
| S31 | [consciousness introduction](../../consciousness/sections/introduction.tex) / [SSO](../../consciousness/sections/sso.tex) | downstream current manuscript | YES | Bio as biological grounding | fast/slow、simulation引用 |
| S32 | [consciousness formal mapping](../../consciousness/sections/formal_mapping.tex) / [correspondence map](../../consciousness/sections/correspondence_map.tex) | downstream scope/cross-window relation | YES | Bio/IFGTを明示 | projected windows |
| S33 | [CT README](../../conceptual-topography/README.md) / [CT introduction](../../conceptual-topography/sections/introduction.tex) / [CT mapping](../../conceptual-topography/sections/formal_mapping.tex) | related application manuscript | YES | IFGT/VED直接; Bio名の直接参照locateせず | cognitive/social projection、Bioとは区別 |
| S34 | [Intelligence I introduction](../../intelligence-part1/sections/01_introduction.tex) / [horizon](../../intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex) / [JA horizon](../../intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex) | downstream manuscript | YES | Bio biological vocabulary明示 | metabolic/reproductive cyclesのcross-reference |
| S35 | [Intelligence II README](../../intelligence-part2/README.md) / [JA preliminaries](../../intelligence-part2/sections/01_preliminaries_ja.tex) / [JA inference](../../intelligence-part2/sections/02_inference_operator_ja.tex) / [JA stopping](../../intelligence-part2/sections/05_emergent_stopping_layer_ja.tex) / [JA social](../../intelligence-part2/sections/09_social_blockchain_ja.tex) | downstream primary JA / EN draft系 | YES | Bioのtheta/F/second attractor明示 | layer-to-layer continuation |
| S36 | [Intelligence I draft](../../intelligence-part1/draft_ja.md) / [Intelligence II combined](../../intelligence-part2/source_md/intelligence_part2_combined_ja.md) / [appendices](../../intelligence-part2/source_md/intelligence_part2_appendices_ja.md) | downstream draft/source duplicates | working、historical-onlyとはしない | Bio直接引用 | same-role/homology文言 |
| S37 | [Intelligence I four layers](../../intelligence-part1/figures/fig5_four_layer_correspondence.svg) / [JA](../../intelligence-part1/figures/fig5_four_layer_correspondence_ja.svg) / [Intelligence II emergence](../../intelligence-part2/figures/fig5_three_examples_of_emergence.svg) / [JA](../../intelligence-part2/figures/fig5_three_examples_of_emergence_ja.svg) / [homology](../../intelligence-part2/figures/fig9_cross_domain_homology.svg) / [JA](../../intelligence-part2/figures/fig9_cross_domain_homology_ja.svg) | downstream figure cross-references | current figure sources | Bio生命層label | dependency表示、内容評価は後続 |

### S19 working-source manifest

| File | 対応するprimary section / 所在上の差 |
|---|---|
| [abstract_ja](../../bio-ifgt/sections_ja/abstract_ja.md) | S03 |
| [introduction_ja](../../bio-ifgt/sections_ja/introduction_ja.md) | S04、I非同一明記 |
| [intuitive_picture_ja](../../bio-ifgt/sections_ja/intuitive_picture_ja.md) | S05 |
| [formal_mapping_ja](../../bio-ifgt/sections_ja/formal_mapping_ja.md) | S06、plain r/J/F表記 |
| [core_equations_ja](../../bio-ifgt/sections_ja/core_equations_ja.md) | S07 |
| [gene_information_flow_ja](../../bio-ifgt/sections_ja/gene_information_flow_ja.md) | S08、threshold signatureの別表記 |
| [development_morphogenesis_ja](../../bio-ifgt/sections_ja/development_morphogenesis_ja.md) | S09、sigma signatureの別表記 |
| [life_attractor_ja](../../bio-ifgt/sections_ja/life_attractor_ja.md) | S10 |
| [probability_revision_ja](../../bio-ifgt/sections_ja/probability_revision_ja.md) | S11 |
| [intelligence_second_attractor_ja](../../bio-ifgt/sections_ja/intelligence_second_attractor_ja.md) | S12、確率式の別表記 |
| [relation_to_note_ja](../../bio-ifgt/sections_ja/relation_to_note_ja.md) | S13 |
| [discussion_ja](../../bio-ifgt/sections_ja/discussion_ja.md) | S16 |
| [conclusion_ja](../../bio-ifgt/sections_ja/conclusion_ja.md) | S17、実験的対応は今後の課題 |

Bioの独立experiment/validation record、外部datasetを読み込む別executableはlocateしていない。
S15の“observations”はnumerical runについてのsection名である。
AI Spine machine/generatedの直接Bio名hitはなく、独立Bio machine modelをlocateしなかった。
LICENSEは権利情報、既存aux/log/toc・font cache・DS_Storeはbuild/editor artifactとして除外し、変更しない。

## 4. Inherited upstream objects

「継承」はsourceが参照・再利用・比較していること。identity mapを認定する語ではない。
IFGT source identityは§1リンクとfrozen06、Bio用法はS04–S16で確認した。

| Upstream object | Upstream source identity | Bio-IFGT usage | Same symbol? | Explicit map? | Status inherited |
|---|---|---|---|---|---|
| INH-01: I | IFGT retained trace density、I=f(1-C) | S04: biological coarse-grained constraint density | YES/glyph; Bio macro I | direct identityを明示的に否定、field-to-Bio map未表示 | source-local IFGT定義のみ、Bio測定identityなし |
| INH-02: J | IFGT vector information flow / VED discrete log-flowは別 | S06: reaction/diffusion/transport/updateの総合 | YES/arrow-bold差あり | aggregate wording、carrier map未表示 | RC-006 OPENを維持 |
| INH-03: Phi | IFGT scalar constraint potential、-alpha C+Phi0 | S06–07: Phi[I]、具体形system-dependent | YES | 上流Cとのmap未表示 | source-local/effective potential vocabulary |
| INH-04: gradient-driven bias F | IFGT F_I=-grad Phi | S06: F=-grad Phi、new fundamental forceでない | FとF_Iは別表記 | 類似式形、identity map未表示 | effective relation scopeを輸入、物理力認定なし |
| INH-05: sigma | IFGT mismatch、drive/dissipation/barrier; Vol.1別source | S07 local generation; S08 gene-event generation | YES | 三項分解とのtranslation未表示 | RC-003分離、RC-041 OPEN |
| INH-06: balance equation | IFGT tau balance / Vol.1 rho balanceは別 | S07 t-based I balance | 類似形、変数/parameter異なる | source-local式を表示、上流変換は未表示 | RC-038 internal formal scopeのみ |
| INH-07: t | IFGT fixed-background external parameter / Vol.1 derivative parameter | S06 external recording time、S16 observed timeとの区別 | YES | clock/source間map未表示 | RC-002分離のguard |
| INH-08: tau | IFGT informational ordering、Vol.1 node-local accumulation | S06/S10 interpretive internal progression | YES; node indexなし | d tau/dtをBio側で導入、上流tauとのmapなし | RC-040 OPEN |
| INH-09: rho | VED node log density、continuum densityは別 | S06 rho(I,J)、S10 rho(x) = progression rate | YES/glyphのみ | 上流densityとのmap未表示 | RC-007/009 OPEN; Bio-local function別記 |
| INH-10: C / quasi-closure | IFGT scalar closure degree; Vol.1 Cij causal-log matrixと別 | S04 life quasi-closure解釈、I=f(1-C)を比較対象に引用 | Cはupstream説明、Bio stateとして未導入 | 非同一注記あり、Cij→field mapなし | RC-001/005/039を保持 |
| INH-11: non-closure / complete-closure boundary | IFGT constraintとeffective barrier | S04/S11/S16 sustained non-equilibrium regime | 語彙共有; L-family式なし | biological境界とのmap未表示 | conceptual correspondence、barrier式の直接継承なし |
| INH-12: difference / asymmetry | upstream represented gradient/effective flow、necessity限定 | S05/S09 initial asymmetry、S08 historically retained theta | 語彙共有 | cross-layer mechanism map未表示 | RC-016–018のscope/OPENは保持 |
| INH-13: attractor / persistence | upstream formal targetとphysical persistenceを分離 | S10 life region、S12 second attractor | 概念語彙共有; upstream fixed-point式未転載 | stable-structure同定はBio文章、上流solution mapなし | RC-020/021/024の研究OPENを結果扱いしない |
| INH-14: diffusion / dissipation | IFGT transport/D、sigma dissipative term | S09/14 D、lambda decay、source terms | D等共有、lambdaはBio source-local | coefficient/units translation未表示 | field-description形式の参照 |
| INH-15: “unified” / VED–IFGT relation | RC-038 internal equation、RC-039 proposed correspondence | S03/S18 unified biological description / coarse-graining | label共有、C evolutionそのものは未転載 | cross-theory map未表示 | upstream unificationが成立済みとは継承しない |

network distance、metric tensor、L、L_ab、L_mn、VED causal-log fixed-point系、
IFGT三項sigmaやbarrier式はBioの直接equation入力としてlocateしていない。
Phiを重力と同定することもS20では避ける方針。類似したpotentialという語だけでgravity継承を追加しない。

## 5. Bio-specific additions

“First source”はEN論文の読書順での初出／最初の明示位置であり、git年代順の発明者判定ではない。
Formal role欄はsourceの説明の転記・要約のみ。

| Bio object / assumption | First source | Formal role | Biological interpretation | Upstream dependency |
|---|---|---|---|---|
| BIO-01: biological I | S04:15、S06:11–15 | constraint-density field | local structure/differentiation/retained bias | IFGT Iと非同一の対応 |
| BIO-02: biological J | S06:19–23 | state-update direction/rate | reactions、transport、interactions | IFGT flow形式 |
| BIO-03: Phi[I] / response | S06:27–43、S07:47–53 | system-dependent effective potential、D/mu | gradient-driven bias | IFGT potential語彙 |
| BIO-04: observation window / r,t | S04:15、S06:7 | coarse fields on R3、external t | organism detailsの粗視化 | field representation |
| BIO-05: s / theta(s) | S04:5、S08:7–17 | sequence / parameter set | DNA-dependent reaction propensities | quasi-closure origin readingはS08:69 |
| BIO-06: gene events / Delta I | S08:21–33 | local operations / local generation | transcription/translation/binding/modification | I/J/sigma |
| BIO-07: F_k / theta_k | S08:49–53 | reaction threshold | conditional differentiation | theta / continuous fields |
| BIO-08: morphogen / decay | S09:13–28 | reaction–diffusion component | concentration profiles、production/degradation | density/flow description |
| BIO-09: state x / F(x;theta) | S10:7–17 | state vector / evolution | concentration/expression/reaction/environment | general dynamics vocabulary |
| BIO-10: internal progression rho/tau | S06:47–51、S10:21–25 | optional interpretive time | accumulated state update | upstream orderingとの対応未固定 |
| BIO-11: Omega_life / viable range | S10:29–39 | bounded return region called life attractor | life maintenance | quasi-closure/persistence vocabulary |
| BIO-12: matter/energy exchange | S10:43 | non-equilibrium description、専用resource式未表示 | matter replacement、energy consumption | non-closure |
| BIO-13: sub-attractor / regeneration | S10:51–55 | differentiation/return/reconstruction interpretation | cell fate、robustness、regeneration | attractor interpretation |
| BIO-14: life-entry probability | S11:19–37 | object of probabilityの再定式化、数値なし | life emergence as region entry/persistence | quasi-closure interpretation |
| BIO-15: Omega_intel / history reuse | S12:11–29 | second-attractor subset、schematic factorization | memory/reference/sharing forwardref | life attractor |
| BIO-16: M/I/N/B/E toy fields | S14:9–19 | finite developmental model variables | embryo-like/neural-like/eye-like | Bio field vocabulary |
| BIO-17: source / positional window / initial noise | S14:62–76、S21 make functions | imposed runtime input / gate | DNA-like conditions、coarse eye window | theta analogy |
| BIO-18: gradient-derived B / threshold masks | S14:49–59、S21 gradient/update | boundary stabilization and diagnostics | boundary-like region、not specified cell membrane | Bio I gradient |

membrane、homeostasis、self-maintenance、metabolism、replicationに対応する独立変数/専用法則は
Bio primary sourceにlocateしていない。maintenance、matter/energy exchange、regenerationは文章にある。
下流のmetabolic/reproductive cyclesという言い換えを、Bio本文に存在する代謝・複製モデルとして補わない。
fitness scalar、resource-budget equationも追加しない。

## 6. Cross-layer identity / correspondence inventory

Explicit map欄はsource-localな式の存在とcross-layer変換の存在を区別する。
Current claim formは文章形式の分類でありsupport判定ではない。

| Relation ID | From | To | Source wording | Explicit map? | Representation change? | Current claim form |
|---|---|---|---|---|---|---|
| REL-01 | IFGT I=f(1-C) | biological I | S04:15 “correspondence between descriptive layers, not an identity” | NO cross-layer map、非同一を明記 | general field→biological window | CORRESPONDENCE CLAIM |
| REL-02 | IFGT quasi-closure | life sustained non-equilibrium | S04:15 “corresponds, in IFGT terms, to quasi-closure” | proseのみ | closure regime→life | CORRESPONDENCE CLAIM |
| REL-03 | prior difference / closure patterns | theta/DNA | S08:69 “historically stabilized constraint patterns”; concrete originはderiveしない | theta(s) source-localのみ | dynamical history→biological constraints | CORRESPONDENCE CLAIM |
| REL-04 | gene events | I change / sigma / J | S08:21–33 local operations、aggregate continuous flow、source represents gene events | Delta Iの記述式、aggregation map未表示 | discrete events→continuum | PHYSICAL / BIOLOGICAL IDENTIFICATION CLAIM |
| REL-05 | morphogen concentration | I | S09:13 “such profiles are represented as information density” | proportionality/calibration未表示 | molecular concentration→constraint proxy | PHYSICAL / BIOLOGICAL IDENTIFICATION CLAIM |
| REL-06 | I bias | Phi / F / flow | S06:27–43 effective potential / gradient bias | Bio式あり、Phiの具体形未固定 | source-local field relations | FORMAL CONSTRUCTION CLAIM |
| REL-07 | thresholded continuous I | cell fate / morphology | S09:44–57 “stable state is the morphology observed” | threshold examplesあり、observable map未表示 | continuous state→discrete biological label | PHYSICAL / BIOLOGICAL IDENTIFICATION CLAIM |
| REL-08 | bounded return dynamics | life / regeneration | S10:29–55 life attractor、return/reconstruction | Omega_life命名、operational membership未表示 | model state space→life | PHYSICAL / BIOLOGICAL IDENTIFICATION CLAIM |
| REL-09 | rho(I,J) / rho(x) | tau / internal progress | S06:47–51、S16:27 “interpretive variable” | d tau/dt式あり、clock mapなし | update→internal time reading | CORRESPONDENCE CLAIM |
| REL-10 | quasi-closure entry/persistence | probability of life | S11:37 “precise interpretation” | event description、measure/数値未表示 | regime→probability target | CORRESPONDENCE CLAIM |
| REL-11 | life + retained/reused history | intelligence | S12:11–29 second attractor / subset | subset/factorization、implementation未表示 | biological→cognitive | EMERGENCE CLAIM |
| REL-12 | toy I/N/B/E | quasi-closure hierarchy | S14:115 “successive localization of quasi-closure” | simulation rulesあり、C carrier map未表示 | model fields→IFGT interpretation | CORRESPONDENCE CLAIM |
| REL-13 | toy N/E configurations | neural-plate-like / eye-like structures | S14:76–83、S15:25,111–113 | label/threshold rules、not specific biologyと明記 | numerical fields→biological-like label | PHYSICAL / BIOLOGICAL IDENTIFICATION CLAIM |
| REL-14 | L3 formal variables | L1 note expressions | S13:7–20 structural correspondence、not direct translations | listed analogiesのみ | formal→intuitive | CORRESPONDENCE CLAIM |
| REL-15 | common field structure | molecule/cell/tissue scales | S08:61 “same formal structure ... retain the same roles” | scale map未表示 | cross-scale | UNIVERSALITY CLAIM |
| REL-16 | I/Phi/J loop | sustained structures | S07:57,80 “can produce non-equilibrium structures” | source-local loop、concrete organism map未表示 | dynamical description→organization | MECHANISM CLAIM |

REL-08はsourceのlife terminologyのinventoryであり、生活現象と数学領域の同一性を認定したものではない。
REL-12のpaper chainとcode dependencyは§8/9に別記する。矢印のrole判定は02へ渡す。

## 7. Upstream OPEN inheritance

8件すべてを照合した。「間接」は語彙・類似式・parameterの依存候補であり、そのbridgeを実際に
前提化したと確定する意味ではない。最後の列も評価ではなく、completionを述べる文の所在確認である。

| Upstream OPEN | Used by Bio-IFGT? | How | Does Bio-IFGT add a bridge? | Does it silently assume completion? |
|---|---|---|---|---|
| RC-005 Cij→C(x,tau) | 間接関連、直接行列入力なし | S04 C/I、S14 quasi-closure | matrix-to-field mapなし、I非同一注記あり | 完成assertionはlocateせず。quasi-closure解釈の依存範囲は後続確認 |
| RC-006 Jij→J(x) | 間接関連 | S06/S08 aggregate biological flow | biological events→J proseはあるがVED Jij mapなし | 完成assertionはlocateせず。Bio-local aggregationはREL-04 |
| RC-007 rhoi→rho(x,t) | 直接使用locateせず; glyph比較は関連 | Bio rhoはprogression rateであってdensity入力と記載されない | mapなし | glyphから完成を推定しない |
| RC-008 dij→g_mn | 直接使用locateせず | R3/2Dをsource-localに置く、graph metric式なし | mapなし | metric completionを述べる箇所locateせず |
| RC-009 dot-rhoi→sigma | 間接関連 | Bio sigmaはgene-event/source rate、upstreamと同glyph | projection/unit mapなし | dot-rhoiとの同一assertionはlocateせず |
| RC-010 scalar/edge L→L_mn | 直接使用locateせず | quasi-closure語彙はあるがL-family未導入 | tensor mapなし | tensor completionを述べる箇所locateせず |
| RC-040 tau↔tau_VED | 間接関連 | Bio内部tauを導入、S16 operational definition scope外 | Bio d tau/dtはあり、上流間translationでない | completed temporal identityはlocateせず |
| RC-041 VEDsigma↔IFGTsigma | 間接関連 | Bio continuity/gene source、IFGT attribution | cross-theory sigma mapなし | exact same-process assertionはlocateせず |

直接completed bridgeとしての使用確認0、間接関連5（005/006/009/040/041）。
007は同glyph比較対象として別途保留する。関連なしの断定ではなく、今回のsourceで直接利用をlocateしない。
upstream OPENを閉じる判定やBio側のFAIL判定は行っていない。

## 8. Equation / update / constraint location inventory

すべて既存expressionの転記／code抜粋で、新しい式を提案していない。
ENの \I / \J / \PhiI / \dd はS01でそれぞれI / bold J / Phi / roman dへ展開されるmacro。
表では可読な既存glyphへ展開する。JA workingのplain J/F/rはその版のまま残す。
同一式のrepriseはまとめ、別signature・working variant・コードでの実装差は別行とした。
係数、operator/domainの妥当性はまだ監査しない。

| BIO-EQ ID | Expression | Source | Variables | Upstream inherited? | Bio-specific? | Stated role |
|---|---|---|---|---|---|---|
| BIO-EQ-01 | \(\mathbf r\in\mathbb R^3,\ t\in\mathbb R\) | S06:7; S02 Formal Mapping | r,t | field settingの使用 | biological coarse state | State Description |
| BIO-EQ-02 | \(I(\mathbf r,t)\) | S06:12–14; S07:8–10; S09; S19 | I,r,t | IFGT Iと非同一 | constraint density | Information Density |
| BIO-EQ-03 | \(\mathbf J(\mathbf r,t)\) | S06:20–22; S07:12–14; S19 plain J | J,r,t | flow語彙 | biological update | Information Flow |
| BIO-EQ-04 | \(\Phi=\Phi[I]\) | S06:28–30; S07:43–46; S08/09; S19 | Phi,I | potential形 | system-dependent | induced effective potential、具体形未指定 |
| BIO-EQ-05 | \(\mathbf F=-\nabla\Phi\) | S06:33–35; S07:38–41; S08/09; S19 plain F | F,Phi | gradient bias形 | response | gradient-driven bias |
| BIO-EQ-06 | \(\mathbf J=-D\nabla I+\mu\mathbf F\) | S06:40–43; S07:29–33; S19 | J,D,I,mu,F | IFGT流れの類似形 | source-local | diffusive + induced components |
| BIO-EQ-07 | \(d\tau/dt=\rho(I,\mathbf J)\) | S06:48–51; S07:62–65; S19 | tau,t,rho,I,J | time vocabulary、mapなし | progression function | interpretive internal time |
| BIO-EQ-08 | \(\partial_t I+\nabla\cdot\mathbf J=\sigma\) | S07:20–24,74–79; S08:30–33; S19 | I,J,t,sigma | balance形、tauでなくt | gene source use | continuity equation |
| BIO-EQ-09 | \(\Phi\sim-I\) | S07:50–51; S14:110; S19 core:95 | Phi,I | identity継承せず | example potential | example sign convention |
| BIO-EQ-10 | \(s\in\{A,T,G,C\}^{N}\) | S08:8–10; S02/S19 | s,N,nucleotide labels | NO | DNA | sequence representation |
| BIO-EQ-11 | \(\theta=\theta(s)\) | S08:14–17; S02:238 | theta,s | NO map from upstream | DNA parameters | parameter set |
| BIO-EQ-12 | \(I(\mathbf r,t)\mapsto I(\mathbf r,t)+\Delta I\) | S08:22–25; S02:246 | I,DeltaI | NO event map | gene operations | local state change |
| BIO-EQ-13 | \(F_k(I,\mathbf J,\mathbf r,t;\theta)>\theta_k\) | S08:50–53; S02:273 | F_k,I,J,r,t,theta | NO | reaction switching | threshold condition |
| BIO-EQ-14 | \(\partial_t I=D\nabla^2I-\lambda I+\sigma(\mathbf r,t;\theta)\) | S09:22–28; S02:313 | D,lambda,sigma,theta | generic RD component、source明記 | morphogen description | standard reaction–diffusion form |
| BIO-EQ-15 | \(I(\mathbf r)<\theta_1\Rightarrow A;\ \theta_1\le I(\mathbf r)<\theta_2\Rightarrow B;\ I(\mathbf r)\ge\theta_2\Rightarrow C\) | S09:45–53; S02:334; S19矢印はright-arrow | I,theta1/2,A/B/C state labels | NO | cell fate examples | threshold response |
| BIO-EQ-16 | \(x(t)=(x_1(t),\ldots,x_n(t))\) | S10:8–11; S02/S19 | x,t | general state representation | molecular/environment components | state vector |
| BIO-EQ-17 | \(dx/dt=F(x;\theta)\) | S10:14–17; S02/S19 | x,F,theta | VED fixed-point式ではない | biological dynamics | system evolution |
| BIO-EQ-18 | \(d\tau/dt=\rho(x)\) | S10:22–25; S02/S19 | tau,t,rho,x | identity mapなし | state progression | internal time |
| BIO-EQ-19 | \(\Omega_{\mathrm{life}}\subset\Omega\) | S10:34–39; S11:20–23; S02/S19 | Omega/life | upstream fixed pointと別 | viable return region | life attractor / region-entry target |
| BIO-EQ-20 | \(\Omega_{\mathrm{intel}}\subset\Omega_{\mathrm{life}}\) | S12:18–21; S02/S19 | Omega/intel/life | NO | second attractor | additional-constraint subset |
| BIO-EQ-21 | \(P_{\mathrm{intel}}\approx P_{\mathrm{life}}P_{\mathrm{second}\mid\mathrm{life}}\) | S12:26–29; S02:450 | probabilities | NO | two-stage emergence | schematic factorization、not numerical estimate |
| BIO-EQ-22 | bias/constraint \(\mapsto I\); state update \(\mapsto\mathbf J\); asymmetry in update \(\mapsto\Phi\) | S06:56–60; S19 summary prose | three descriptions | source-local mapping | biological picture | correspondence to formal quantities |
| BIO-EQ-23 | \(I\leftrightarrow\) local bias; \(\mathbf J\leftrightarrow\) flow; \(\Phi\leftrightarrow\) return tendency; attractor \(\leftrightarrow\) preserving form | S13:14–20; S19 relation note | formal/intuitive labels | NO | L3/L1 comparison | not direct translations |
| BIO-EQ-24 | \(\partial_t M=D_M\nabla^2M-\lambda_M M+\sigma_M(x,y)\) | S14:26–30; S02:482 | M,D_M,lambda_M,sigma_M | RD形式 | toy morphogen | diffusion/decay/local production |
| BIO-EQ-25 | \(\partial_t I=D_I\nabla^2I-\lambda_I I+\alpha M\) | S14:34–38; S02:486 | I,M,D_I,lambda_I,alpha | density形式 | toy accumulation | diffusion/decay/accumulation |
| BIO-EQ-26 | \(N_{t+1}=N_t+\eta_N S(I-\theta_N)(1-N_t)\) | S14:42–46; S02:490 | N,eta_N,S,I,theta_N | NO | neural commitment | threshold update |
| BIO-EQ-27 | \(G=\lvert\nabla I\rvert\) | S14:50–53; S02:496 | G,I | gradient形式 | boundary field input | gradient structure |
| BIO-EQ-28 | \(B_{t+1}=B_t+\eta_B S(G-\theta_B)(1-B_t)\) | S14:55–59; S02:500 | B,eta_B,G,theta_B | NO | boundary stabilization | thresholded update |
| BIO-EQ-29 | \(E_{t+1}=E_t+\eta_E S(N-\theta_{EN})S(B-\theta_{EB})A(x,y)(1-E_t)\) | S14:63–68; S02:506 | E,N,B,A,eta_E,thresholds | NO | eye-like commitment | combined threshold/window |
| BIO-EQ-30 | \(S(z)=1/(1+e^{-kz})\) | S14:70–72; S02:510 | S,z,k | NO stated lineage | thresholding | thresholding function |
| BIO-EQ-31 | \(M\to I\to N\to B\to E\) | S14:88–96; S15:93–95; S02:522,613 | M,I,N,B,E | quasi-closure interpretation近接 | toy hierarchy | generation path / successive constraints（source wording） |
| BIO-EQ-32 | \(\mathbf J\sim-\nabla\Phi\) | S14:111; S02:533 | J,Phi | effective flow類似形 | toy interpretation | induces flows toward stable regions（source wording） |
| BIO-EQ-33 | \(P_{\mathrm{intel}}\approx P_{\mathrm{life}}\times P_{\mathrm{life}}\) | S19 intelligence:105–112 | P_intel,P_life | NO | working variant | 数値評価ではないとの説明; BIO-EQ-21と別版のまま記録 |
| BIO-EQ-34 | \(\partial_t I=D\nabla^2 I-\lambda I+\sigma(r,t)\) | S19 development:49–50 | I,D,lambda,sigma,r,t | RD形式 | working signature | ダイナミクス |
| BIO-EQ-35 | \(F_k(I,J,r,t)>\theta_k\) | S19 gene:112–118 | F_k,I,J,r,t,theta_k | NO | working signature | 閾値としてのif/then |
| BIO-EQ-36 | `padded[2:,1:-1]+padded[:-2,1:-1]+padded[1:-1,2:]+padded[1:-1,:-2]-4.0*field` | S21 laplacian | field,padded | no upstream map | 2D stencil | edge-copy zero-flux Laplacian |
| BIO-EQ-37 | `1.0/(1.0+np.exp(clipped))`; `clipped=np.clip(-SIGMOID_K*z,-60.0,60.0)` / `-K_EYE*z` | S21 sigmoid / eye_sigmoid | z,k,clip | NO | two threshold functions | stable logistic threshold |
| BIO-EQ-38 | `SOURCE_STRENGTH*np.exp(-((X-0.5)**2)/(2.0*SOURCE_WIDTH**2))` times `np.exp(-((Y-0.5)**2)/(2.0*Y_WIDTH**2))` | S21 make_sigma_m central_band | X,Y,width,strength | NO | source profile | morphogen source |
| BIO-EQ-39 | `sigma[:,:SIGMA_M_BAND_WIDTH]=SIGMA_M_STRENGTH*vertical_profile[:,None]`; `vertical_profile=np.exp(-(y/0.65)**2)` | S21 make_sigma_m left_edge | y,sigma,band | NO | alternative source | source mode |
| BIO-EQ-40 | `exp(-((Y-.5)**2)/(2*EYE_Y_WIDTH**2))`; edge_pairはcenters .35/.65の和; single_pairは追加 `exp(-((X-.35)**2)/(2*.18**2))` | S21 make_eye_window（np.expの要約転記） | X,Y,window,mode | NO | positional gates | positional window; central_pairはalias |
| BIO-EQ-41 | `G=np.sqrt(grad_x**2+grad_y**2)`; `G/(float(np.max(G))+1.0e-8)` | S21 gradient_magnitude | I,G,grad | NO cross-layer map | normalized boundary input | normalized gradient magnitude |
| BIO-EQ-42 | `M,N,B,E=np.zeros(...)`（各field個別初期化）; `I=PERTURBATION_SCALE*rng.standard_normal((size,size))` | S21 run_simulation | size,SEED=7,noise=1e-4 | NO | initial conditions | initialization（code位置; ROLE NOT YET AUDITED） |
| BIO-EQ-43 | `M += DT*(D_M*laplacian(M)-LAMBDA_M*M+sigma_M)`; `I += DT*(D_I*laplacian(I)-LAMBDA_I*I+ALPHA*M)` | S21 run_simulation | M,I,DT,parameters | local discretizationのみ | finite update | explicit finite-difference simulation |
| BIO-EQ-44 | `N += ETA_N*sigmoid(I-THETA_N)*(1.0-N)`; `B += ETA_B*sigmoid(G_norm-THETA_B)*(1.0-B)`（signal変数展開） | S21 run_simulation | N,B,I,G_norm | NO | commitment/stabilization | threshold updates |
| BIO-EQ-45 | `E += ETA_E*eye_signal*(1.0-E)`; `eye_signal=eye_sigmoid(N-THETA_EN)*eye_sigmoid(B-THETA_EB)*eye_window` | S21 run_simulation | E,N,B,window | NO | secondary commitment | conditional eye update |
| BIO-EQ-46 | `np.clip(N,0.0,1.0)`, B/E同様; `range(steps+1)`, last stepではbreak | S21 run_simulation | N,B,E,steps | NO | bounds/schedule | executable constraints（ROLE NOT YET AUDITED） |
| BIO-EQ-47 | `np.mean(N>0.5)`, B/E同様; means/maxima、E>.5 contour/overlay | S21 print_summary / plotting | field masks/statistics | NO | model diagnostics | numerical summary / visualization |
| BIO-EQ-48 | `(field-minimum)/(maximum-minimum)`; maximum<=minimumならzeros | S21 normalize_for_plot | field,min,max | NO | RGB composition | plot normalization、biological observableではない |

BIO-EQ-40/42/44はcode場所を読みやすく要約した抜粋であり、新update lawではない。
完全な実行順序・定数はS21がauthority。codeはM更新後I、次にN、G_norm/B、Eを実行する。
Phi/J/tauを直接積分するroutineはS21にlocateしない。
論文Gとcode G_norm、論文共通SとcodeのSIGMOID_K=8/K_EYE=20、paper chainとREADMEの分岐図を、
同じ実装だと先に断定しない。相互対応は後続01/02/05で検討する。

S19のtuple一覧 `I,J,Phi,thresholds,stable solutions` は§5のsource role列へ収録。
S04引用のIFGT I=f(1-C)はINH-01/10で収録し、Bio equationとして二重計上しない。
Phiに特定kernelやclosure barrierを補っていない。

## 9. Simulation / executable inventory

新しいrun、checker、finite experimentを行っていない。以下はcodeと既存outputの所在確認である。

| SIM ID | File | Model family | Inputs | Outputs | Finite? | Empirical data used? | Current claim attached |
|---|---|---|---|---|---|---|---|
| SIM-01 | S21 / S22 / S23 | minimal_neural_field v2_hierarchical、explicit finite difference | default 128x128、800 steps、DT .08、seed7、source/eye modes、thresholds/decay/diffusion/response、CLI | M/I/N/B/E arrays、PNG、optional GIF、stdout stats | YES/configured grid+steps | file/network measurement loaderなし、synthetic sources/noise | illustrative toy、not realistic embryogenesis |
| SIM-02 | S24 7 tracked PNG、S15 captions | SIM-01 figure distribution | saved model arrays（個別run metadata未付属） | M,I,N,B,E,overlay,combined | finite render | model-generatedとsource記載 | structural possibility、not biological mechanism |
| SIM-03 | S15:84–90、S22:145、local outputs | time-evolution supplement | saved frames | claimed development_v2_hierarchical.gif; local fig8-prefixed GIFあり | finite frames | simulation | staged formation visualization |
| SIM-04 | S21 print_summary / normalize_for_plot | diagnostics / display | field arrays | mean/max、fraction>.5、normalized RGB | YES | simulation | numerical summary; empirical markerとは記載されない |

実行可能model familyは**1**。4行はartifact/function側面を分けたもので、4実験を意味しない。
S21 default定数はD_M=.45、LAMBDA_M=.030、D_I=.16、LAMBDA_I=.020、ALPHA=.09、
THETA_N=1.15、ETA_N=.030、ETA_B=.020、THETA_B=.55、ETA_E=.020、
THETA_EN/EB=.50、EYE_Y_WIDTH=.08。これは既存inputの転記でありcalibrationではない。

### Current figure manifest

| Field / purpose | Tracked paper artifact |
|---|---|
| M | [morphogen_final_v2.png](../../bio-ifgt/simulations/minimal_neural_field/outputs/morphogen_final_v2.png) |
| I | [information_density_final_v2.png](../../bio-ifgt/simulations/minimal_neural_field/outputs/information_density_final_v2.png) |
| N | [neural_commitment_final_v2.png](../../bio-ifgt/simulations/minimal_neural_field/outputs/neural_commitment_final_v2.png) |
| B | [boundary_field_final_v2.png](../../bio-ifgt/simulations/minimal_neural_field/outputs/boundary_field_final_v2.png) |
| E | [eye_commitment_final_v2.png](../../bio-ifgt/simulations/minimal_neural_field/outputs/eye_commitment_final_v2.png) |
| N/E overlay | [neural_eye_overlay_v2.png](../../bio-ifgt/simulations/minimal_neural_field/outputs/neural_eye_overlay_v2.png) |
| combined | [combined_fields_with_eye_v2.png](../../bio-ifgt/simulations/minimal_neural_field/outputs/combined_fields_with_eye_v2.png) |

[output policy](../../bio-ifgt/simulations/minimal_neural_field/outputs/.gitignore)はこの7PNGと.gitignoreのみを例外にする。
paperが記す `development_v2_hierarchical.gif` は今回localではlocateせず、
`fig8_development_v2_hierarchical.gif` はignored local artifactとして存在する。
別名fig1–7、central_band、unsuffixed PNGもlocalにある。tracked/current sevenとのbyte一致・
run provenanceは本phase未試験。local別名を独立experimentとして数えない。
これはartifact所在の未確定事項で、simulation結果への評価ではない。

## 10. Empirical / observational inventory

「data sourceなし」は今回調べたsourceに個別dataset/measurement protocolが表示されないという意味。
source自体が限定する文も、肯定的なobservational wordingも併記する。

| EMP ID | Claim | Source | Data source | Direct measurement? | Model-generated? | External dataset? |
|---|---|---|---|---|---|---|
| EMP-01 | same DNA cells can differentiate | S04:5、S02 Introduction | biological background prose、個別実験指定なし | recorded measurementなし | NO/model結果の記述でない | not located |
| EMP-02 | morphogen profiles represented as I | S09:13–17 | concentrationという観測対象、protocol未表示 | not recorded here | field description | not located |
| EMP-03 | cell fate/morphology observed as stable configurations | S08:57、S09:53–57 | phenomenon-to-model wording | paired measurementなし | interpretationあり | not located |
| EMP-04 | developmental reproducibility/robustness、regeneration | S09:61、S10:55 | general biological discussion | dataset/perturbation trial記録なし | attractor reading | not located |
| EMP-05 | stable central neural/eye-like final state、“Observations” | S15:25,97–113 | numerical run / 7PNG | biological measurementではないとsource限定 | YES | NO located loader |
| EMP-06 | other biological observables may need other response conventions | S07:47–53 | prospective observable specification | not supplied | example Phi choice | not located |
| EMP-07 | empirical forms of I/J/Phi must be identified、no numerical predictions | S16:27–37、S17:9、S19 conclusion | future work declaration | not supplied | not an empirical result | not located |
| EMP-08 | fast/slow differentiation “confirmed” in Bio simulation experiments | S31 SSO:17–21 | downstreamがBio toy pathを引用 | biological measurement citationなし | simulationを指す文章 | not located in cited Bio artifacts |

8 bibliography entriesはliterature metadataでありdatasetではない。S01/S02にbibliography呼出をlocateせず、
それら外部文献の内容や支持範囲を読んだとはしない。
Bio独立empirical-validation record、observation CSV、external-data loaderはlocateしていない。
本記録は“validated/unvalidated”という総合判定を行わない。

## 11. Boundary / observer inventory

| Boundary ID | Boundary type | Source | Endogenous / imposed | Operationally identifiable? |
|---|---|---|---|---|
| BND-01 | biological observation window | S04:15、S21 docstring | selected coarse window、selection algorithm未記載 | observable/filter/scale procedure未表示 |
| BND-02 | spatial continuum R3 and external t | S06:7,47 | representationとして置く | coordinatesは表示、organismとのcalibration未表示 |
| BND-03 | Omega_life viable bounded region | S10:29–39 | source says “not externally imposed”、system/environment interactionでformed | membership/range/perturbation scale未数値化 |
| BND-04 | system/environment material exchange | S10:11,39,43 | coupled environmentと記載 | exchange flux・物理boundary detector未表示 |
| BND-05 | complete-closure / quasi-closure boundary | S04:15、S11:37、S16:23 | IFGT vocabularyによる記述 | biological C測定・membrane identification未表示 |
| BND-06 | computational grid outer boundary | S21 laplacian/run | imposed 2D square、edge-copy zero-flux | padding操作として明示 |
| BND-07 | source support / eye positional window | S21 make_sigma_m/make_eye_window | imposed Gaussian/band/mode parameters | code coordinates/widthsあり、biological calibration未表示 |
| BND-08 | B boundary stabilization | S14:49–59、S21 gradient_magnitude | I gradientからupdate、threshold/rateはinput | code field/mask定義あり、membraneとしての観測手順なし |
| BND-09 | commitment/display boundary | S21 clip/print/overlay | threshold .5、clip、display normalization | finite arrayで判別可能、physical boundary同定とは別 |

S10のendogenous-region wordingとS21のimposed grid/windowは異なる対象として残す。
膜・細胞内外・observerを解決したという判定は行わない。

## 12. Generation-claim inventory

Wordingだけを分類する。sourceの“does not introduce a new biological mechanism”と
“emergence”記述をどちらも保存し、ここで優先する読みを決めない。

| Claim ID | Source / wording | Wording class | 対象 / scope note in source |
|---|---|---|---|
| GEN-01 | S03:1,5 minimal unified description、no new biological mechanism | FORMAL CONSTRUCTION CLAIM | biological phenomenaの共通description |
| GEN-02 | S05:13–21 asymmetries give direction、stable regions appear | MECHANISM CLAIM | intuitive picture、rigorous definitionではない |
| GEN-03 | S07:57,80 loop can produce sustained structures | MECHANISM CLAIM | general source-local dynamics |
| GEN-04 | S08:25 gene network generates information flow | MECHANISM CLAIM | discrete events aggregate continuous flow |
| GEN-05 | S08:57 cell fate/morphology observed as stable configurations | PHYSICAL / BIOLOGICAL IDENTIFICATION CLAIM | theta/field/threshold sequence |
| GEN-06 | S08:61 same structure at molecule/cell/tissue scales | UNIVERSALITY CLAIM | roles retained under different coarse levels |
| GEN-07 | S08:69 theta as historically stabilized quasi-closure | CORRESPONDENCE CLAIM | concrete origin not derived |
| GEN-08 | S09:57 morphology is result of dynamical convergence | EMERGENCE CLAIM | morphogenesis interpretation |
| GEN-09 | S09:61、S10:55 robustness follows from attractor property | MECHANISM CLAIM | return/perturbation/regeneration |
| GEN-10 | S10:29–43 life as bounded sustained non-equilibrium motion | PHYSICAL / BIOLOGICAL IDENTIFICATION CLAIM | life attractor source definition |
| GEN-11 | S11:23,35–37 life probability = region-entry target | CORRESPONDENCE CLAIM | no numerical reassessment、not automatic necessity |
| GEN-12 | S12:11–29 intelligence appears with retained/reused history | EMERGENCE CLAIM | second attractor、additional constraints |
| GEN-13 | S13:7–20 same target/structure across L3/L1 | CORRESPONDENCE CLAIM | not literal translation |
| GEN-14 | S14:5,76–103 parameters generate biological-like stable structures | EMERGENCE CLAIM | toy model、no explicit completed geometryというsource claim |
| GEN-15 | S14:115 E as secondary quasi-closure | CORRESPONDENCE CLAIM | supports attractor-within-attractor reading |
| GEN-16 | S15:99–113 structural possibility、not biological mechanism | FORMAL CONSTRUCTION CLAIM | simulation-only scope |
| GEN-17 | S31 SSO:9–23 two layers emerge necessarily; confirmed in Bio simulation | UNIVERSALITY CLAIM | downstream attribution、今回その枝の判定なし |

biological timeそのものの生成、agencyの独立生成、metabolismの専用生成則はBio primaryに
直接claimとしてlocateしていない。tauのinterpretive usage、life maintenance、intelligenceの
forward referenceを、それらのclaimへ膨らませない。

## 13. Downstream inheritance

以下は依存の受け取り方を記録するだけで、consciousness/CT/intelligenceの監査は開始しない。
“same”“necessarily”“shown”は引用元のclaim formであり、このrecordが承認した述語ではない。

| Downstream branch | Bio-IFGT object inherited | Source | Explicit dependency? | Identity / analogy / mechanism wording |
|---|---|---|---|---|
| DOWN-01: consciousness | life quasi-closure、M/I/N/B/E hierarchy | S31 introduction:43、SSO:9–23; [JA SSO](../../consciousness/sections_ja/sso_ja.tex) | YES | biological grounding、fast/slow necessary differentiation、simulation confirmedという文言 |
| DOWN-02: consciousness / CT comparison | window-local density/flow、biological substrate | S32 formal_mapping:35–65、correspondence_map:31 | YES/Bio名あり | projected uses、no paper grounds another、structural isomorphismの語彙。DOWN-01と別に保存 |
| DOWN-03: conceptual topography | 直接Bio object継承はlocateせず | S33、[CT refs](../../conceptual-topography/refs.bib); S32経由の比較 | IFGT/VEDはYES、Bio直接は未確認 | cognitive-window projection。Bio→CT機構を推定しない |
| DOWN-04: Intelligence I | life quasi-closure regime / biological vocabulary | S34 introduction:15、horizon四層表; [summary](../../intelligence-part1/sections/10_summary_convergence_and_outlook.tex):55,67 | YES | substrate / metabolic and reproductive cycles / layered correspondence |
| DOWN-05: Intelligence II theta / F | theta、dx/dt=F(x;theta) | S35 JA preliminaries:121、JA inference:21以降 | YES | “同一の役割”、Fの知性層特殊形、時間scale差 |
| DOWN-06: Intelligence II second attractor | Omega_intel、history/reference/shared information | S35 JA preliminaries:251–260、JA stopping:67,106 | YES | L_Rを内部記述、L_Eをsecond-attractorの同一構造として記載 |
| DOWN-07: Intelligence II social | inter-individual quasi-closure maintenance | S35 JA social:134,165 | YES/attribution | Bioが“示した”、相同・同一構造という文言; 対応するBio-local construction所在未固定 |
| DOWN-08: downstream figures / summaries | life attractor、four-layer/emergence examples | S36/S37、EN II stopping figure note | YES | cross-domain homology / upper-attractor substitutionという図解上の接続 |

S35 READMEはJA manuscript/Markdown sourceとEN draftを区別する。Bioに関する詳細文がJAにあり、
EN draftで短縮されている箇所も同じ引用量とみなさない。
S31の“simulation experiments”に対するBio側直接入力はSIM-01/02。
専用fast/slow metric、two-layer identification protocolの所在は本inventoryでは未固定。

## 14. Documentary dependency graph

各行は参照・定義・実装・解釈・引用の関係であって、全段が因果生成であるという図ではない。

| From | To | Documented relation type | Trace |
|---|---|---|---|
| frozen VED/IFGT scope | Bio inherited vocabulary | authority guard / correspondence、identity自動継承なし | §1、INH-01–15 |
| IFGT density/flow/potential/quasi-closure | Bio I/J/Phi/time / life description | source-local definition + cross-layer correspondence | S04/06/16、REL-01/02/09 |
| Bio field description | theta / events / viable region / environment | Bio-specific assumptions and interpretations | BIO-05–15 |
| fields / thresholds / source windows | finite M/I/N/B/E update | executable construction | S14/S21、BIO-EQ-24–48 |
| model arrays | figures / numerical “observations” | generated visualization | SIM-02–04 |
| sustained / attractor-like model states | life / morphogenesis / intelligence | biological interpretation / claim wording | GEN-05–17 |
| Bio claims / toy hierarchy | consciousness / intelligence | explicit downstream attribution | DOWN-01/04–08 |
| Bio / consciousness comparison | CT cognitive window | related-window correspondence、Bio direct edge未確認 | DOWN-02/03 |

これによって「上流で固定されたもの」「Bioが置くもの」「下流がBioから受け取ると書くもの」を分ける。
dependency order ≠ proof order ≠ biological causal order。

## 15. Uncertainty / handoff ledger

Open IDは今回の未確定な所在・identity・mappingの索引であり、上流RC final dispositionを新規設定しない。
“Blocks later audit?”は、その監査問いを確定する前に必要な確認を意味し、00完了のFAILではない。

| Open ID | Unresolved identity / dependency | Why unresolved | Upstream or Bio-local? | Blocks later audit? |
|---|---|---|---|---|
| U01 | IFGT I / Bio I / observed biological quantity | 非同一を明記、coarse operator/measurement未表示 | upstream↔Bio | 01/04/05の同定比較前に必要 |
| U02 | Bio rho(I,J) / rho(x) / upstream rho | glyphは共有、state-field/clock mapなし | upstream↔Bio | 01/03 time identity |
| U03 | Bio sigma gene production / IFGT mismatch / Vol.1 source | source-local definitions、translation未表示 | upstream↔Bio | 01/04 source meaning |
| U04 | gene events→continuous J | aggregate prose、averaging/units/carrier map未表示 | Bio-local | 02/03 bridge/dependency |
| U05 | r,t / biological window / chosen observables | geometryとwindowは記述、measurement selection未表示 | Bio-local | 03/05 boundary/measurement |
| U06 | Phi functional / sign / response | S07 explicitly system-dependent、exampleのみ | Bio-local | 01/02 concrete role |
| U07 | theta(s) / DNA-like numerical parameters | organism-specific theta originをderiveしないとsource明記 | Bio-local | 04/05 parameter-to-biology |
| U08 | Omega_life / viable criterion / boundedness / perturbation | region命名、membershipと具体基準未表示 | Bio-local | 03/04/05 life identification |
| U09 | B / membrane / organism boundary | Bはgradient field、membrane variableをlocateせず | Bio-local | 03/05 boundary interpretation |
| U10 | toy simulation state→biological observable | sourceはtoy/not specific organism、paired dataset未表示 | Bio-local | 04/05 empirical correspondence |
| U11 | paper equations / implementation update / figure run | G vs normalized G、S vs k_eye、sequential updates、run manifest未付属 | Bio-local | 01/02/05 version correspondence |
| U12 | S19 probability/signatures vs EN/JA TeX | BIO-EQ-21/33/34/35は別表記。S19は直接build inputでない | Bio-local | 01 source identityを選ぶ前に必要 |
| U13 | quasi-closure→life→fast/slow / SSO | downstream“confirmed”の専用diagnostic所在未固定 | Bio→consciousness | downstream review前、04/05に引渡し |
| U14 | second attractor / L_E / inter-individual maintenance | S12 forwardref、downstream same-structure/shown attributionの対応箇所未固定 | Bio→intelligence | downstream inheritance review前 |
| U15 | note essay L1 target / intermediate appendix | S13に対応記述、具体local essay path/版未固定 | Bio↔expository | provenanceの照合時に必要 |
| U16 | animation / local alternate output lineage | unprefixed GIF未locate、ignored fig8 GIF等は存在、run/hash未照合 | Bio-local artifacts | 05 artifact provenance |

mapping/bridge所在の未確定項目はU01–05、U07–10、U13–14（11行）、
source/local identity・form・versionの確認項目はU01–03、U06、U11–12、U15–16（8行）。
分類は重複あり。これらを新たなevidence insufficiency verdictとして扱わない。
upstream8 OPENは別ledger§7のまま保持する。

## 16. Phase-00 outcome and next boundary

| Inventory | Count / unit |
|---|---|
| Source inventory | 37 source units / explicitly grouped sources |
| Primary Bio TeX | 17 files = EN entry + 15 sections + self-contained JA entry |
| Bio tracked scope | 47 files、うちworking JA 13 / distributed PDF 2 / tracked PNG 7 |
| current-facing source units | 32（S01–18、S21–25、S27–29、S31–35、S37） |
| working / design / bibliography units | 4（S19/S20/S26/S36） |
| historical-only source units | 1（S30 CHANGELOG） |
| inherited object families | 15 |
| Bio-specific additions | 18 |
| cross-layer relations | 16 |
| upstream OPEN review | 8、間接関連5、完成した継承bridgeの確認0 |
| equation / update location entries | 48、reprises統合・variants分離 |
| simulation inventory | 4 artifact/function rows、executable model family 1 |
| empirical / observational wording entries | 8、外部dataset使用はlocateせず |
| boundary entries | 9 |
| generation-claim wording entries | 17 |
| downstream dependency entries | 8、CT direct Bio dependencyは未確認 |
| uncertainty ledger | 16、評価結果ではなく後続確認事項 |

同じ“closure”“information”“observation”を使う文章を区別し、直接のBio定義・比喩・
simulation result・downstream attributionをsourceごとに辿れる状態にした。
ここからwrong/invalid/circular、claim downgrade、empirical validation、生命生成の
肯定・否定へ進まない。Phase01のequation/symbol同定は次taskであり未開始。

## 17. Validation and write boundary

- 新規2 Markdownのrelative links / source paths 95件、17 tables、fences、display-math delimitersを検査し、error 0。
- source IDs / inventory counts / equation IDsは本record内で確認。
- 開始時の既存1,426 filesのSHA-256比較で変更・削除0。新規は本recordとREADMEの2件のみ。
- `git diff --check`: PASS。既存96 tracked modificationsは本task以前の作業としてそのまま保持。
- source、working notes、PDF、PNG/GIF、simulation code、upstream frozen/implementation recordsは無変更。
- 新規simulation / compile / regeneration / empirical comparisonなし。source inventoryのためのread-only code読解のみ。
- 既存tracked modificationsとuntracked methodology / VED auditを保持し、本taskの新規はBio監査READMEと00のみ。
- 上流監査とcore revisionはCLOSEDを維持。Bio auditはIN PROGRESS。
- commit / pushなし。Phase01を開始せず停止。

[Bio audit README](README_ja.md)

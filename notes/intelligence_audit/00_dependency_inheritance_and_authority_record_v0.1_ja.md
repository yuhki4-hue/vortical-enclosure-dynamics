# Intelligence Phase 00 — dependency / inheritance / source authority inventory v0.1

## 0. Status / stop boundary

```text
Intelligence audit: IN PROGRESS
Phase00 dependency / inheritance / source authority: COMPLETE
Phase01–07: NOT STARTED
Source / equation / distribution revision: NOT STARTED
```

本記録は2026-09-11のworkspaceを対象とする独立inventoryである。過去のCT作業依頼ではなく、今回のIntelligence Phase00のみを実施した。本文にある「定理」「証明」「必然」「実証」「同型」は**sourceの主張種別・強度の記録**であり、本監査による承認ではない。claim truth、数学的正しさ、経験的妥当性、循環性、evidence sufficiency、dispositionは判定していない。

監査層 I0=formal/mathematical、I1=representational/computational、I2=cognitive/functional、I3=social/collective、I4=phenomenal/subjective。これは監査用であって、sourceの四層、L_F/L_R/L_E、VEDの層、CTの層と同一ではない。

## 1. Authority boundary / method

source reuse ≠ derivation、same notation ≠ same object、same formula shape ≠ same signature、same vocabulary ≠ typed inheritance、downstream reuse ≠ upstream validation、upstream closure ≠ Intelligence validity。appendix homology / correspondence table ≠ proof、navigation / exposition order ≠ proof / generation order、formal analogy ≠ ontology、model role ≠ empirical mechanism。CT / Consciousness / Bio-IFGTの結果をIntelligenceの結果へ移送しない。社会的なintelligence命名をgeneral intelligenceへ統合しない。emergent stopping layerという名称から経験的cognitive moduleを認定しない。

直接確認したauthority根拠は各PartのREADME、entryのinput構造、本文、補遺、MD status banner、caption/asset、配布PDFである。CTの「EN canonical」という方針はIntelligenceへ転用しない。

| 対象 | entry / artifact | 分類・今回固定するauthority |
|---|---|---|
| Part I JA | `intelligence-part1/main_ja.tex` + `sections_ja/` | CANONICAL（current distributed build authorityというREADMEの明示に限定。最終理論freezeを意味しない） |
| Part I EN | `intelligence-part1/main.tex` + `sections/` | current EN TeX source。primary CANONICAL / AUTHORIZED TRANSLATIONの明示はUNKNOWN。言語別sourceとして保持し、JAを上書きしない |
| Part I MD | `intelligence-part1/draft_ja.md` | WORKING / HISTORICAL。status bannerがTeXをcurrent authorityに指定 |
| Part II JA | `intelligence-part2/main_ja.tex` + `preamble_ja.tex` + JA sections/appendices | CANONICAL（READMEの「primary source for now」、移行中のmanuscript authority） |
| Part II EN | `intelligence-part2/main.tex` + `preamble.tex` + EN sections/appendices | WORKING English draft。canonical EN / authorized faithful translationとは未確定 |
| Part II MD | `source_md/intelligence_part2_combined_ja.md`, `intelligence_part2_appendices_ja.md` | WORKING / HISTORICAL。各bannerはcurrent TeXをauthorityに指定 |
| Part II revision notes | `source_md/intelligence_part2_revision_notes_ja.md` | WORKING editorial instruction/history。本文・証明を上書きしない |
| 両Part root PDF | `main.pdf`, `main_ja.pdf` | DERIVED DISTRIBUTION。PDFの存在はcanonicality/validityの根拠ではない |
| 両Part README | 各 `README.md` | NAVIGATION + editorial/build authority。論証authorityではない |
| Part II appendices A–E | 言語別10 TeX files | APPENDIX AUTHORITY、JA primary / EN draftを継承。mainの確立結果へ自動昇格しない |
| figures / caption MD | 下記全assets、Part II `figure_captions*.md` | FIGURE/PRESENTATION。caption MDは詳細版、TeX noteは短縮版というREADME方針 |
| bib / preamble / Makefile | 各source support | bibliography / build-support。理論の独立supportとは区別 |
| Part II CFF / CHANGELOG / LICENSE | directory metadata | NAVIGATION / HISTORICAL / license。CFF v0.1.0、2026、CC-BY-4.0。Unreleased migration履歴はsource completionの保証ではない |
| root docs / upstream/downstream | 後掲locator | NAVIGATIONまたは各branch-local source。Intelligence content authorityの代替ではない |

AUTHORIZED TRANSLATIONと明示されたIntelligence EN entryは今回未確認。JAとENの章境界の一致を翻訳同値の根拠にしない。

### 1.1 Entry metadata / declared purpose

| Part | title / subtitle | author / date / series | declared purpose / scope |
|---|---|---|---|
| I | Structural Constraints on Intelligence as a Dynamical Phenomenon; JA「知性を力学的現象として制約する構造条件」 | Yuhki Endoh; Independent Researcher; 2026; Intelligence Section, Part I | stopping structureの所有でなくdynamical phenomenon、3 axioms、Physarum/Transformer比較、Gettier、nonclosure、differential horizon。VED/IFGT記述語彙、Bio/Con比較。complete theory、経験内容、工学/規範を除外 |
| II | Non-Closure of Inference, Externalization of Stopping, and Emergent Stopping Layers; JA「推論の非閉包性、停止の外部化、創発的停止層」 | Yuhki Endoh; Independent Researcher; 2026; Intelligence Section, Part II | Part Iから三層、externalized stopping、history/social/networkへ。JAはVED基底からの構造的導出を宣言。宗教真理の序列、AGI設計処方、経験/倫理判断は除外 |

MDの旧英語subtitleは “Externalized Stopping” / “A VED-Theoretic Derivation” / “Three-Layer Architecture of Sapient Cognition”。current TeX titleとの差をhistoricalとして保存する。Part I abstract JAは「知覚・知識・知性」の三つを挙げ、本文の四層（認識を含む）と項目数が異なる。Part II EN abstractは本文あり、JA entryの概要は未移植placeholder（配布PDFも空欄）。

## 2. Complete source / section map

locator略記: P1:E/J §n = 下記INT1-SnnのEN/JA file。P2:E/J §n = INT2-Snn。P2:E/J A–E = 補遺表。E/Jは言語を示すだけでauthorityは§1に従う。abstractはINT1-S00、Part II entry内abstractはINT2-FRONT。後掲claim表のこれらlocatorはsourceファイル＋section titleへ一意に展開できる。

Part I: abstract + 本文§1–10 = 11 included content files/言語、計22。Part II: 本文§0–13 = 14 files/言語、計28; preamble 1/言語; appendix5/言語。本文の数とinput総数を混同しない。両entryのinput順を確認した。subsection/subsubsection全見出しも次のsource mapに記録する（空欄はなし）。数式欄はPhase00のdisplay block検出数でありequation-family数ではない。


### 2.1 Part 1 included sources

| ID | EN path / title | JA path / title | 主role / figures / displayed blocks E:J |
|---|---|---|---|
| INT1-S00 | `intelligence-part1/sections/abstract.tex` — Abstract | `intelligence-part1/sections_ja/abstract_ja.tex` — 概要 | 要約; figs なし; 0:0 |
| INT1-S01 | `intelligence-part1/sections/01_introduction.tex` — Introduction | `intelligence-part1/sections_ja/01_introduction_ja.tex` — Introduction | Introduction; figs なし; 0:0 |
| INT1-S02 | `intelligence-part1/sections/02_the_decomposition_perception_recognition_knowledge_and_intelligence.tex` — The Decomposition: Perception, Recognition, Knowledge, and Intelligence | `intelligence-part1/sections_ja/02_the_decomposition_perception_recognition_knowledge_and_intelligence_ja.tex` — The Decomposition: Perception, Recognition, Knowledge, and Intelligence | The Decomposition: Perception, Recognition, Knowledge, and Intelligence; figs `figures/fig1_four_layer_decomposition.png`; 0:0 |
| INT1-S03 | `intelligence-part1/sections/03_minimal_axioms_of_intelligence.tex` — Minimal Axioms of Intelligence | `intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex` — Minimal Axioms of Intelligence | Minimal Axioms of Intelligence; figs `figures/fig2_three_axioms.png`; 3:3 |
| INT1-S04 | `intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex` — IFGT as Vocabulary, with Lexical Correspondence to the Physarum Solver | `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex` — IFGT as Vocabulary, with Lexical Correspondence to the Physarum Solver | IFGT as Vocabulary, with Lexical Correspondence to the Physarum Solver; figs なし; 2:2 |
| INT1-S05 | `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex` — Cross-Domain Instantiation: Slime Mold and Transformer | `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex` — Cross-Domain Instantiation: Slime Mold and Transformer | Cross-Domain Instantiation: Slime Mold and Transformer; figs `figures/fig3_cross_domain_homology.png`; 4:5 |
| INT1-S06 | `intelligence-part1/sections/06_the_gettier_problem_as_a_structural_diagnostic.tex` — The Gettier Problem as a Structural Diagnostic | `intelligence-part1/sections_ja/06_the_gettier_problem_as_a_structural_diagnostic_ja.tex` — The Gettier Problem as a Structural Diagnostic | The Gettier Problem as a Structural Diagnostic; figs なし; 0:0 |
| INT1-S07 | `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex` — The Dynamical Instability of Accumulated Correctness | `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex` — The Dynamical Instability of Accumulated Correctness | The Dynamical Instability of Accumulated Correctness; figs `figures/fig4_branching_explosion.png`; 3:4 |
| INT1-S08 | `intelligence-part1/sections/08_the_non_closure_of_individual_intelligence.tex` — The Non-Closure of Individual Intelligence | `intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex` — The Non-Closure of Individual Intelligence | The Non-Closure of Individual Intelligence; figs なし; 1:0 |
| INT1-S09 | `intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex` — The Differential Horizon of Intelligence | `intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex` — The Differential Horizon of Intelligence | The Differential Horizon of Intelligence; figs `figures/fig5_four_layer_correspondence.png`; 2:1 |
| INT1-S10 | `intelligence-part1/sections/10_summary_convergence_and_outlook.tex` — Summary, Convergence, and Outlook | `intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex` — Summary, Convergence, and Outlook | Summary, Convergence, and Outlook; figs なし; 0:0 |

#### Subsection / subsubsection locator inventory

- `intelligence-part1/sections/abstract.tex`: なし
- `intelligence-part1/sections_ja/abstract_ja.tex`: なし
- `intelligence-part1/sections/01_introduction.tex`: Background: VED and IFGT as theoretical infrastructure / The intelligence question: why neither ability nor knowledge suffices / Contributions and scope
- `intelligence-part1/sections_ja/01_introduction_ja.tex`: Background: VED and IFGT as theoretical infrastructure / The intelligence question: why neither ability nor knowledge suffices / Contributions and scope
- `intelligence-part1/sections/02_the_decomposition_perception_recognition_knowledge_and_intelligence.tex`: Overview / Perception / Recognition / Knowledge / Intelligence / Why the distinction matters
- `intelligence-part1/sections_ja/02_the_decomposition_perception_recognition_knowledge_and_intelligence_ja.tex`: Overview / The structural distinction: stopping versus ongoing / Perception as input-state formation / Recognition as mapping into an existing representational structure / Knowledge as stabilized stopping (log) / Intelligence as ongoing, revisable dynamics / Why conflation occurs: the operational coupling of layers / Summary of the decomposition
- `intelligence-part1/sections/03_minimal_axioms_of_intelligence.tex`: Overview / Axiom I: Connected state space / Axiom II: Temporal ordering / Axiom III: Global constraint $\Phi$ / The joint necessity of the three axioms / Semantic neutrality of the axioms / Summary
- `intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex`: Overview / Axiom I: Connected state space / Axiom II: Temporal ordering / Axiom III: Global constraint $\Phi$ / The joint necessity of the three axioms / Semantic neutrality of the axioms / Summary
- `intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex`: Overview / Why a vocabulary, not a theory / The IFGT vocabulary / Lexical correspondence with the Physarum solver / What IFGT vocabulary does not do / Summary
- `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex`: Overview / Why a vocabulary, not a theory / Why existing vocabularies fail / The IFGT vocabulary / Lexical correspondence with the Physarum solver / The Physarum solver model / Lexical correspondence / The emergence of $\Phi$ in independent confirmation / What IFGT vocabulary does not do / Summary
- `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex`: Overview / The slime mold as an externally validated instantiation / The Transformer as an artificial instantiation / Structural homology and its limits / The structural meaning of cross-domain convergence
- `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex`: Overview / The slime mold as an externally validated instantiation / Independent biological grounding / Mapping to the three axioms / The structural status of the slime mold case / The transformer as an artificial instantiation / Why the transformer / Mapping to the three axioms / What this mapping does not assert / Structural homology and its limits / What the homology asserts / What the homology does not assert / Why the homology nonetheless matters / The structural meaning of cross-domain convergence / Summary
- `intelligence-part1/sections/06_the_gettier_problem_as_a_structural_diagnostic.tex`: Overview / Knowledge as stopping structure / Why Gettier cases recur / Relation to the four-layer decomposition / Implications for later sections / Summary
- `intelligence-part1/sections_ja/06_the_gettier_problem_as_a_structural_diagnostic_ja.tex`: Overview / The Gettier problem and its persistence / The classical formulation / The series of repair attempts / Why the problem is structurally insoluble / The structural diagnosis / Why every repair attempt fails in the same way / Repositioning Gettier through the layer decomposition / Layer-by-layer analysis of Gettier cases / What the intuition is actually tracking / The Gettier problem as a structural diagnostic / Diagnostic function / What Gettier cases demonstrate / Implications for the broader argument / Implications for \S{}7 (the instability of accumulated correctness) / Implications for \S{}8 (the non-closure of individual intelligence) / Implications for \S{}9 (the differential horizon of intelligence) / Summary
- `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex`: Overview / Why correctness increases connectivity / Why correctness contains no stopping condition / Branching explosion / Why ``more intelligence'' does not solve the problem / Summary
- `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex`: Overview / Why correctness increases connectivity / The reusability of correctness / Formalization in IFGT vocabulary / Why correctness contains no stopping condition / Correctness generates further inference / The self-generating nature of inference / The dynamics of branching explosion / The structural chain / The structural meaning of branching explosion / The regime of instability / Consequences for individual systems / The signature symptoms / These are not failures of ability / Why "more intelligence" does not solve the problem / The intuitive proposal / Why the proposal fails / The implication for the broader argument / Summary
- `intelligence-part1/sections/08_the_non_closure_of_individual_intelligence.tex`: Overview / The stopping operator problem / Interruption is not stopping / The paperclip problem as a structural example / Transition to \S{}9 / Summary
- `intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex`: Overview / The recursive structure of causal reasoning / The form of why-regress / The regress contains no intrinsic stopping point / Conditions required for stable stopping / External response / Shared agreement / Externalization as log / Temporal delay / The structural commonality / The absence of an internal stopping operator / What the individual system can do / What the individual system cannot do / The structural absence / Failure modes of the individual node / The structural relation to \S{}7.4 / The structural reading of the symptoms / Not pathologies in the medical sense / Anticipated objection: stopping versus interruption / The objection / The structural distinction: stopping versus interruption / Energy, reward gradients, and biological constraints / Why this distinction is decisive: the paperclip problem / What the objection does not refute / Implications for the broader argument / The transition to \S{}9 / Connection to the layered correspondence (\S{}9.4) / Summary
- `intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex`: Overview / The structural necessity of crossing / What is externalized / Naming the boundary / Layered correspondence / Connection to subsequent work / Summary
- `intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex`: Overview / The structural necessity of crossing / Deriving the boundary from the absence / What makes the crossing inevitable / What is externalized / Stopping judgments / Records (logs) / Temporal delay / Distribution of responsibility / What is NOT externalized / What externalization does NOT guarantee / Naming the boundary / The naming / Why this name / What the name does and does not claim / Layered correspondence with Bio-IFGT and the consciousness paper / The four-layer system / The four common structural features / The transitional position of the consciousness layer / The peculiar position of the biological layer / What the layered correspondence implies / What is not claimed in this layered correspondence / Connection to subsequent work / What this paper establishes / What this paper does not establish / The transition to Part II / Connection to other parts of the series / Summary
- `intelligence-part1/sections/10_summary_convergence_and_outlook.tex`: Overview / Summary of constraints / The convergence of independent research lines / Outlook / Concluding remarks
- `intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex`: Overview / Summary of constraints / Constraint 1: Intelligence is not a stopping structure / Constraint 2: Intelligence is not preserved, only generated / Constraint 3: Intelligence requires three simultaneous axiomatic conditions / Constraint 4: Correctness does not stabilize intelligence / Constraint 5: Individual closure is structurally impossible / Constraint 6: Crossing the local horizon-form is structurally necessary / The status of these constraints / The convergence of independent research lines / The pattern of convergence / The Physarum research lineage / The transformer architecture as parallel convergence / The structural meaning of convergence / An important qualification / Outlook / The structural status of this paper / Subsequent work in the series / Branch connections beyond this paper's scope / The structural status of branch connections / Concluding remarks / What this paper is / What this paper is not / The minimal statement / The position of this paper in the series

### 2.2 Part 2 included sources

| ID | EN path / title | JA path / title | 主role / figures / displayed blocks E:J |
|---|---|---|---|
| INT2-S00 | `intelligence-part2/sections/00_introduction.tex` — Introduction: Why Intelligence Requires Stopping | `intelligence-part2/sections/00_introduction_ja.tex` — 序論 — VED理論ツリーにおける本論文の位置 | Introduction: Why Intelligence Requires Stopping; figs なし; 1:6 |
| INT2-S01 | `intelligence-part2/sections/01_preliminaries.tex` — Preliminaries: VED Vocabulary in the Intelligence Layer | `intelligence-part2/sections/01_preliminaries_ja.tex` — 準備 — VED・IFGT・推論の C-幾何学 | Preliminaries: VED Vocabulary in the Intelligence Layer; figs なし; 4:5 |
| INT2-S02 | `intelligence-part2/sections/02_inference_operator.tex` — The Inference Operator $F$ | `intelligence-part2/sections/02_inference_operator_ja.tex` — 推論演算子 $F$ と推論層 $L_F$ — 相互拘束・閾値・開放窓 | The Inference Operator $F$; figs なし; 5:4 |
| INT2-S03 | `intelligence-part2/sections/03_nonclosure_theorem.tex` — The Non-Closure Theorem: No Internal Fixed Point in $L_F$ | `intelligence-part2/sections/03_nonclosure_theorem_ja.tex` — 非閉包定理 — 推論層 $L_F$ に内部不動点が存在しないこと | The Non-Closure Theorem: No Internal Fixed Point in $L_F$; figs `fig1_c_landscape.pdf`; 5:6 |
| INT2-S04 | `intelligence-part2/sections/04_response_channels.tex` — Response Channels and Silent Worlds | `intelligence-part2/sections/04_response_channels_ja.tex` — 応答チャネルと沈黙世界 — 閾値現象としての C-幾何学 | Response Channels and Silent Worlds; figs `fig2_responsive_silent_threshold.pdf`; 0:1 |
| INT2-S05 | `intelligence-part2/sections/05_emergent_stopping_layer.tex` — The Emergent Stopping Layer $L_E$ | `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex` — 創発停止層 $L_E$ — 外部依存型停止の動力学 | The Emergent Stopping Layer $L_E$; figs `fig3_mutual_constraint_mu_theta.pdf`, `fig4_three_layer_architecture.pdf`, `fig5_three_examples_of_emergence.pdf`, `fig6_phi_ext_phi_net.pdf`; 4:1 |
| INT2-S06 | `intelligence-part2/sections/06_animism.tex` — Animism: Installation of Stopping in the Environment | `intelligence-part2/sections/06_animism_ja.tex` — アニミズム — $L_E$ を環境直接相互干渉で維持する | Animism: Installation of Stopping in the Environment; figs なし; 1:0 |
| INT2-S07 | `intelligence-part2/sections/07_god.tex` — God: Compression of Distributed Stopping | `intelligence-part2/sections/07_god_ja.tex` — 神 — $L_E$ の中心化された懸架軌跡 | God: Compression of Distributed Stopping; figs なし; 1:2 |
| INT2-S08 | `intelligence-part2/sections/08_religion.tex` — Religion: Long-Term Maintenance of Stopping Structures | `intelligence-part2/sections/08_religion_ja.tex` — 宗教 — $L_E$ の世代横断的維持と混合相 | Religion: Long-Term Maintenance of Stopping Structures; figs なし; 1:0 |
| INT2-S09 | `intelligence-part2/sections/09_social_blockchain.tex` — Social Blockchain: Distributed $L_E$ as $\Phi_{\text{net}}$ | `intelligence-part2/sections/09_social_blockchain_ja.tex` — 社会的ブロックチェーン — $\Phi_{\text{net}}$ としての分散 $L_E$ | Social Blockchain: Distributed $L_E$ as $\Phi_{\text{net$; figs `fig7_evolution_of_stopping_structures.pdf`; 0:0 |
| INT2-S10 | `intelligence-part2/sections/10_gettier_problem.tex` — The Gettier Problem: Stability Is Not Truth | `intelligence-part2/sections/10_gettier_problem_ja.tex` — ゲティア問題 — $C \neq$ 真理の証拠、$L_E$ の操作的安定性 | The Gettier Problem: Stability Is Not Truth; figs なし; 2:0 |
| INT2-S11 | `intelligence-part2/sections/11_instability_region.tex` — The Instability Region: A Three-Axis Phase Diagram | `intelligence-part2/sections/11_instability_region_ja.tex` — 不安定領域 — 速度・解像度・停止硬度の三軸相図 | The Instability Region: A Three-Axis Phase Diagram; figs `fig8_phase_diagram.pdf`; 1:1 |
| INT2-S12 | `intelligence-part2/sections/12_constructive_clauses.tex` — Constructive Clauses | `intelligence-part2/sections/12_constructive_clauses_ja.tex` — 構成的条項 — 知性の構造的制約 | Constructive Clauses; figs なし; 1:0 |
| INT2-S13 | `intelligence-part2/sections/13_conclusion.tex` — Conclusion: What Remains Open | `intelligence-part2/sections/13_conclusion_ja.tex` — 結論 — 意図的に開いておくもの | Conclusion: What Remains Open; figs `fig9_cross_domain_homology.pdf`; 0:0 |

#### Subsection / subsubsection locator inventory

- `intelligence-part2/sections/00_introduction.tex`: Four Declarations of Position / What This Paper Does Not Claim / How to Read the History of Intelligence / Outline
- `intelligence-part2/sections/00_introduction_ja.tex`: 本論文の課題 / 本論文の立場：四つの宣言 / Part I からの接続 / 四層分解 / 三公理 / 領域横断ホモロジー / 分岐爆発 / 個体知性の非閉包 / 本論文の双中心構造 / 本論文が課題としないこと / 知性の歴史をどう読むか / VED理論ツリーにおける位置 / 本論文の構造 / 形式と表記 / 本論文を読む順序について / 三本論理線の予告 / 要約
- `intelligence-part2/sections/01_preliminaries.tex`: Methodological Fixing: Stopping, Projection, and Consensus / VED Basic Form / Movement Region and Threshold Mobility / Emergence / Variables
- `intelligence-part2/sections/01_preliminaries_ja.tex`: 方法論的固定：停止・投影・合意 / VED 基本式の知性層への再定式化 / 情報場と情報力 / 準閉包 $\Omega_\theta$ / C-landscape と推論軌道 / $C_{max}$ 境界の構造的意味 / 創発の VED 内定義 / 三層動力学の予告 / 本論文で新規導入する変数 / 本章で確立した枠組み / 次章への橋渡し
- `intelligence-part2/sections/02_inference_operator.tex`: Definition / Relation to VED / Branching / Internal Stopping Predicate
- `intelligence-part2/sections/02_inference_operator_ja.tex`: 推論演算子 $F$ の定義 / 推論演算子の四性質 / 推論層 $L_F$ の定義 / Part I との整合 — Physarum・Transformer / 相互拘束 $H_{ij}$ と推論環境 / 応答的/沈黙的は閾値現象である / 閾値移動能力 $\mu_\theta$ / $\theta$ 可変性の時間スケール / 持続可能な因果推論運用との関係 / 開放窓としての $\mu_\theta$ — 第5節への橋渡し / 要約
- `intelligence-part2/sections/03_nonclosure_theorem.tex`: Assumptions / Theorem / Proof Sketch / Branching Explosion / Consequence
- `intelligence-part2/sections/03_nonclosure_theorem_ja.tex`: 推論演算子の前提と正当化測度 / 主定理 — 内部不動点の不在 / 証明スケッチ / 失敗ではなく構造的性質 / 内部停止述語の不可能性 / VED対応 — $C_{max}$ 境界との同型 / 動力学的解釈と分岐爆発との接続 / 系 — 知性が個体内で閉じることの不可能性 / 次章への橋渡し / 要約
- `intelligence-part2/sections/04_response_channels.tex`: Responsive and Silent Regimes / Silence Is Not Defect / Threshold Phenomenon / Infinite Regress in Silent Worlds / The Preview of $L_R$
- `intelligence-part2/sections/04_response_channels_ja.tex`: 応答的世界と沈黙的世界 / 沈黙性は欠陥ではない / 応答的/沈黙的は閾値現象である / 沈黙世界における無限後退 / 無限後退と分岐爆発の相同 / ログ層 $L_R$ の予兆 / 次章への橋渡し / 要約
- `intelligence-part2/sections/05_emergent_stopping_layer.tex`: Problem Setting / The Log Layer $L_R$ / Definition of $L_E$ / Three Profiles / Emergence Mechanism / Projection / External Stopping Operator / $\Phi_{\text{ext}}\equiv\Phi_{\text{net}}$ / Summary
- `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex`: 問題設定 / ログ層 $L_R$ の定義 / 創発停止層 $L_E$ の定義 / アトラクターとしての $L_E$ / 三層プロファイル比較 — 粘菌 / Transformer / サピエンス / 粘菌(Physarum) / Transformer / サピエンス / 二軸による整理 / 「停止構造の場」の連続変分 / 創発機構 — 領域組み替えと停止演算子設置領域の投影 / 投影の位置づけ — 意識編 projection との接続 / 外部停止演算子 $E$ の構造 / $\Phi_{\text{ext}} \equiv \Phi_{\text{net}}$ — 外部参照場と $L_E$ ネットワークの同型 / 回復可能性と改訂可能性 / 系 — 知性の構造的特徴 / 要約
- `intelligence-part2/sections/06_animism.tex`: なし
- `intelligence-part2/sections/06_animism_ja.tex`: アニミズムの構造的定義 / 事実性ではなく構造的変換 / 因果推論の否定ではなく保留 / 低コスト停止装置 / 責任の所在と行動可能性 / 三層動力学における位置 — 環境直接相互干渉型 $L_E$ / 粘菌との構造的同位について / 次章への橋渡し / 要約
- `intelligence-part2/sections/07_god.tex`: なし
- `intelligence-part2/sections/07_god_ja.tex`: 神は説明的実体ではない / 神の機能 — 未解決を保留に変換する状態変化演算子 / 未決定性の委任 / アニミズムとの動力学的差異 — 分散から中心化へ / 中心化の動力学的安定性 / $\Phi_{\text{net}}$ の単一極限としての神 / 単一極限は時間的終着点ではない / 次章への橋渡し / 要約
- `intelligence-part2/sections/08_religion.tex`: なし
- `intelligence-part2/sections/08_religion_ja.tex`: 宗教は科学の対立物ではない / 混合相 — 応答的領域と沈黙的領域の境界管理 / 宗教の三機能 / 純粋因果推論が人間にとって不安定な理由 / 病的引力子 / 遷移的アーキテクチャとしての宗教 / 三層動力学における位置 / 次章への橋渡し / 要約
- `intelligence-part2/sections/09_social_blockchain.tex`: Structure / Legitimacy Rather Than Consistency / Creation and Stabilization / Position in the Three-Layer Dynamics / Bridge to the Gettier Problem
- `intelligence-part2/sections/09_social_blockchain_ja.tex`: 社会的ブロックチェーンの構造的特徴 / 構成要素 / バージョン管理システムとの対比 / 一貫性ではなく正統性 / 創造は社会で起こらない / 三層動力学における位置 — $\Phi_{\text{net}}$ そのものの一形態 / 次章への橋渡し / 要約
- `intelligence-part2/sections/10_gettier_problem.tex`: Structural Diagnosis / $C$ as Stability Measure / Error Tolerance and $\mu_\theta$ / Consequence
- `intelligence-part2/sections/10_gettier_problem_ja.tex`: ゲティア問題は構造的事実の暴露である / ゲティア問題は原理的に解決不可能である / 社会はゲティア問題を解決しない / 知識の再定義 — 行動可能化のための暫定ブロック / 真理に依存しない操作的安定性 / プラグマティズムとの区別 / 誤り許容性の必然と $\mu_\theta$ との同値 / ゲティア問題の最終的役割 / 次章への橋渡し / 要約
- `intelligence-part2/sections/11_instability_region.tex`: Three Axes / Three Regions / Four-Fold Collapse / Rigidity / Instability as Constitutive
- `intelligence-part2/sections/11_instability_region_ja.tex`: 直観的命題の形式化 / 三軸 / 三領域 / 発散域の四重崩壊 / 硬直域の $L_E$ 固着 / (0,0,·)点は知性ではない / 不安定性は構成的特徴である / 個別ノードと高度自律システムへの適用 / 三本論理線の統合 / 次章への橋渡し / 要約
- `intelligence-part2/sections/12_constructive_clauses.tex`: Clause 1: Inference Alone Does Not Close / Clause 2: Logs Are Required / Clause 3: Stopping Is Externally Dependent / Clause 4: Sapiens-Like Intelligence Requires $\mu_\theta$ / Clause 5: Stability Is Revisability / Clause 6: Social Stopping Is Networked / Clause 7: Open Intelligence Requires Movable Stops
- `intelligence-part2/sections/12_constructive_clauses_ja.tex`: 本章の位置づけ / 知性がありえない形態 / 知性一般が必要とするもの / サピエンス的知性を特徴づけるもの / 最終条項 / 制約違反の帰結 / 要約
- `intelligence-part2/sections/13_conclusion.tex`: Three Logical Lines / VED Principle in the Intelligence Layer / Open Questions / Final Statement
- `intelligence-part2/sections/13_conclusion_ja.tex`: 非介入の表明 / 動力学の説明と使用法の決定 / 三本の論理線の総括 / VED の基底原理の知性層における現れ / 残された開放性 / Part I 微修正への引き渡し / 知性は閉じない、しかし持続する / 理論の境界 / 要約

### 2.3 Entries / preambles / abstract

Part I EN/JA entryはtitle、abstract、目次、§1–10、shared refs.bibを組む。Part II EN/JAは各preamble、entry内abstract、目次、§0–13、\\appendix後A–E、refs.bibを組む。Part II EN/JAのpreambleはtheorem/definition/figure-note等のpresentation定義であり、別の証明sourceではない。JA abstractの空欄を本文未存在と混同しない。

## 3. Appendix authority inventory

| ID | paths / titles E ; J | 内容・main relation・新規性 |
|---|---|---|
| INT-APP-001 | `intelligence-part2/appendices/appendix_a_master_table.tex` Master Table of Variables; `intelligence-part2/appendices/appendix_a_master_table_ja.tex` 変数表 Master Table v2.2 | 変数辞書、JA Master Table v2.2 / v2.1再掲宣言。既存と新規の区分、parameter/operatorを追加。§1から参照。exact v2.1 artifact未同定 |
| INT-APP-002 | `intelligence-part2/appendices/appendix_b_homology.tex` Cross-Domain Homology; `intelligence-part2/appendices/appendix_b_homology_ja.tex` 領域横断ホモロジー表 | main cross-domainを表で拡張。JAにCT列、emergence/projection/θ/F/history/P1P2計7table群。ENは短い5-domain表。mapsはrole comparison、typed inverseは未記載 |
| INT-APP-003 | `intelligence-part2/appendices/appendix_c_part1_mapping.tex` Mapping to Intelligence Part I; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex` Part I 各章との対応表・微修正提案リスト | mainでPart Iを参照し補遺へ誘導。EN4対応、JA§1–10と§5/6/8/9微修正提案。提案はP1への実装済み変更ではない |
| INT-APP-004 | `intelligence-part2/appendices/appendix_d_optional_notes.tex` Optional Notes; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex` 主要定理の証明スケッチ集 | EN Optional Notes（psychological projection/science/AI cost/freedom）；JA主要定理の証明スケッチ集（3.1/3.2/3.3/3.4/emergence/5.4/error–μ同値）。同名系列の同内容ではない |
| INT-APP-005 | `intelligence-part2/appendices/appendix_e_emergence_homology.tex` Emergence Homology; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex` 創発の VED 内位置づけ | EN emergence grammar4domain、JA VED定義の創発・weak/strong/holistic/functional比較、物理/Bio/LE。bodyでfutureのstopping functionalを補遺がlocal minimumとして記述する箇所を分離 |

Part I appendix: 0。Part II appendix: 5 families / 10 files。A–Eは両entryからすべてincludeされる。JA Dのproof-sketch存在とその数学的成立は別である。

## 4. Figure / presentation inventory

| ID | family / assets | main placement | symbols / visually asserted claim |
|---|---|---|---|
| INT-FIG-001 | `intelligence-part1/figures/fig1_four_layer_decomposition{,_ja}.{png,svg}` | §2 | 知覚→認識→知識↔知性；stopping vs ongoing。図中intelligence is not stored、Gettier混同。 |
| INT-FIG-002 | `intelligence-part1/figures/fig2_three_axioms{,_ja}.{png,svg}` | §3 | S, s(t+1)=F(s(t)), Φ:S→R、3公理Venn、joint necessity/下限、保証しないguard。 |
| INT-FIG-003 | `intelligence-part1/figures/fig3_cross_domain_homology{,_ja}.{png,svg}` | §5 | Physarum Q/D/network、Transformer h/layers、Φbio/Φtr。same structural conditions；cognitive/phenomenal/ethical identity否定。 |
| INT-FIG-004 | `intelligence-part1/figures/fig4_branching_explosion{,_ja}.{png,svg}` | §7 | N, V, E, b^d, Φ-minimum、growth curves。structural not contingent / no internal stoppingの視覚主張。データplotとは表示されていない。 |
| INT-FIG-005 | `intelligence-part1/figures/fig5_four_layer_correspondence{,_ja}.{png,svg}` | §9 | physical/Bio/Con/Intelligence、DH、renormalization/window/external stop。提案比較guard、substrate矢印。 |
| INT-FIG-006 | `intelligence-part2/figures/fig1_c_landscape{,_ja}.{pdf,svg}` | §3 | C,Cmax,∇C,F,J(x)、no internal fixed point proof box、unreachable boundary、C-landscape trajectory。 |
| INT-FIG-007 | `intelligence-part2/figures/fig2_responsive_silent_threshold{,_ja}.{pdf,svg}` | §4 | observer/world,H,μθ,ρresp、応答/沈黙閾値、閉/開feedback、local stopping。 |
| INT-FIG-008 | `intelligence-part2/figures/fig3_mutual_constraint_mu_theta{,_ja}.{pdf,svg}` | §5 | agent i/j,LR,Hij,μθ,LE、projected stopping region、freedom requires movable stops。 |
| INT-FIG-009 | `intelligence-part2/figures/fig4_three_layer_architecture{,_ja}.{pdf,svg}` | §5 | LF→LR→LE, E,μθ(B)、projection→convergence、sapiens特有guard。 |
| INT-FIG-010 | `intelligence-part2/figures/fig5_three_examples_of_emergence{,_ja}.{pdf,svg}` | §5 | VEDparticle/BioLife/IntLE、U=Φ(L,H)、formal-role comparison not derivation/shared mechanism。 |
| INT-FIG-011 | `intelligence-part2/figures/fig6_phi_ext_phi_net{,_ja}.{pdf,svg}` | §5 | Φext≡Φnet、LEnetwork、external/internal view、same stopping relation、no transcendent field。 |
| INT-FIG-012 | `intelligence-part2/figures/fig7_evolution_of_stopping_structures{,_ja}.{pdf,svg}` | §9 | animism/God/religion/science/social blockchain、installation/compression/maintenance/revision/synchronization；progress story否定。 |
| INT-FIG-013 | `intelligence-part2/figures/fig8_phase_diagram{,_ja}.{pdf,svg}` | §11 | vinf,rres,η,Δvintel,μθ、stable narrow band、divergent/rigid、fourfoldcollapse、notnormative。 |
| INT-FIG-014 | `intelligence-part2/figures/fig9_cross_domain_homology{,_ja}.{pdf,svg}` | §13 | physics/Bio/Con/Int/social、incomplete closure→emergent attractor→sustainable dynamics、no typed-map guard。 |

各brace表記はEN/JA×2formatの実在4filesを表す。14families、28language variants、56assets（P1 20、P2 36）。全28 compiled-format variantsをcontact sheetで視認、SVGの存在をeditable-source locatorとして確認。PNG/SVGまたはPDF/SVGの厳密pixel同値は未認定。editable SVGあり、独立生成コードは未確認。P1はPNG、P2はPDFをTeXがinclude。P2 PDFのimage object数17をfigure family数9と混同しない。図はpresentationであり実験結果とは数えない。

### 4.1 Exact caption locators and current wording


- `intelligence-part1/sections_ja/02_the_decomposition_perception_recognition_knowledge_and_intelligence_ja.tex`: 四層分離の構造図(知覚 → 認識 → 知識 ⇄ 知性、知性は四層全体を運用するが、知性自身は格納されない)

- `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex`: Cross-domain homology(粘菌の管網と Transformer の層構造を、三公理のもとで並列配置する構造図)

- `intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex`: 三公理の同時必要性(三条件のベン図的配置と、各公理を欠いた場合の退化様式)

- `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex`: Branching explosion under accumulated correctness(正しさの累積がノード数線形・エッジ数二次的増大を経て、分岐次数指数的増大に至り、停止点が喪失するまでの動力学的連鎖)

- `intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex`: 差分地平線formsの提案的な四層比較。類似する役割を比較するが、共通carrier・同一mechanism・typed translationは主張しない。

- `intelligence-part1/sections/03_minimal_axioms_of_intelligence.tex`: Joint necessity of the three axioms. Intelligence-like dynamics appears only where connected state space, temporal ordering, and a global constraint hold together.

- `intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex`: A proposed four-layer comparison of Differential Horizon forms. It compares analogous roles without asserting a common carrier, mechanism, or typed translation.

- `intelligence-part1/sections/02_the_decomposition_perception_recognition_knowledge_and_intelligence.tex`: Four-layer decomposition of intelligence. Perception and recognition are precursor layers, knowledge is a stopping structure, and intelligence is ongoing revisable motion across all of them.

- `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex`: Branching explosion under accumulated correctness. Correctness increases reuse, reuse increases connectivity, and connectivity dissolves internal stopping points.

- `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex`: Cross-domain homology under the three axioms. Slime mold and Transformer systems differ radically in substrate but satisfy the same minimal structural conditions.

- `intelligence-part2/sections/09_social_blockchain.tex`: Evolution of stopping structures. Animism, God, religion, science, and social blockchain are different operations for stabilizing, moving, revising, and synchronizing the same emergent stopping layer $L_E$.

- `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex`: 相互拘束 $H_{ij}$ と閾値移動能力 $\mu_\theta$。停止領域は孤立した推論層が生成するものではなく、相互拘束を通して投影される。 / 知性の三層構造。知性は推論層 $L_F$・ログ層 $L_R$・創発停止層 $L_E$ からなり、$\mu_\theta$ はこの創発への開放窓である。 / 異なる領域の創発を、提案的なVED比較に配置した三例。 / $\Phi_{\text{ext}} \equiv \Phi_{\text{net}}$。個体から外部参照場として現れるものは、個々の $L_E$ が相互同期してできたネットワークである。

- `intelligence-part2/sections/09_social_blockchain_ja.tex`: 停止構造の進化。アニミズム・神・宗教・科学・社会的ブロックチェーンは、同一の創発停止層 $L_E$ を安定化・移動・共有するための異なる操作である。

- `intelligence-part2/sections/03_nonclosure_theorem.tex`: The C-landscape and the inference trajectory. Inference moves along the gradient $\nabla C$ on the closure landscape, but structurally it cannot settle at an internal stopping point.

- `intelligence-part2/sections/11_instability_region_ja.tex`: 知性の三軸相図。知性の安定動作は、推論速度 $v_{\text{inf}}$・解像度 $r_{\text{res}}$・停止硬度 $\eta$ の三軸空間で、発散と硬直に挟まれた狭い帯に成立する。

- `intelligence-part2/sections/05_emergent_stopping_layer.tex`: Mutual constraint $H_{ij}$ and threshold mobility $\mu_\theta$. Stopping regions are not generated by an isolated inference layer; they are projected through mutual constraint. / The three-layer architecture of intelligence. Intelligence consists of $L_F$, $L_R$, and $L_E$; $\mu_\theta$ is the opening window through which stopping regions can be reconfigured. / Three examples placed in a proposed VED comparison of emergence across distinct domains. / $\Phi_{\text{ext}} \equiv \Phi_{\text{net}}$. What appears to an individual as an external reference field is the network formed by mutual synchronization among individual $L_E$ layers.

- `intelligence-part2/sections/13_conclusion_ja.tex`: 不完全閉包、アトラクター的組織化、持続的動態をめぐる提案的な領域横断比較。

- `intelligence-part2/sections/03_nonclosure_theorem_ja.tex`: C-地景と推論軌道。推論は閉包度の地形の上を勾配 $\nabla C$ に沿って動き続けるが、構造的にどこにも止まれない。

- `intelligence-part2/sections/13_conclusion.tex`: A proposed cross-domain comparison of incomplete closure, attractor-like organization, and sustained dynamics.

- `intelligence-part2/sections/04_response_channels_ja.tex`: 応答的世界と沈黙的世界。両者は世界の存在論的な種別ではなく、$\mu_\theta$ が動かす閾値境界の左右にどちらが落ちるかで決まる相である。

- `intelligence-part2/sections/11_instability_region.tex`: The three-axis phase diagram of intelligence. Stable operation exists only in a narrow band between divergence and rigidity in the space of $v_{\text{inf}}$, $r_{\text{res}}$, and $\eta$.

- `intelligence-part2/sections/04_response_channels.tex`: Responsive and silent regimes. These are not two ontological kinds of world, but threshold-dependent phases determined by the boundary moved by $\mu_\theta$.

P2の詳細説明は `intelligence-part2/figures/figure_captions.md` / `figure_captions_ja.md`、短縮reading/takeawayは同じfigure環境の `\\figurenote`。これらは別presentation authorityとして保持する。

## 5. Formal object inventory (Phase00)

| ID | object family | source | source role / phase boundary |
|---|---|---|---|
| INT-OBJ-001 | S / X / x / s | P1 §3,5; P2 §1–3 | connected state space, inference state。shared spaceの同定は未実施 |
| INT-OBJ-002 | F / Ftr / F(x;θ) | P1 §3,5; P2 §2,B | temporal/Transformer/inference/Bio flow。same glyphは同じoperatorでない |
| INT-OBJ-003 | Φ global constraint | P1 §3–5 | S→R、local ruleに還元されないbias |
| INT-OBJ-004 | I | P1 §4,7; P2 §1,A | accumulation density vs unresolved degree f(1−C) |
| INT-OBJ-005 | J / Jint / JC | P1 §4,7; P2 §1,A | flow/direction/divergence vs closure flux |
| INT-OBJ-006 | J(x) justification | P2 §2–3,D | strictly increasing justification function；flow Jと別role |
| INT-OBJ-007 | Physarum Qij/Dij/Lij/pi | P1 §4–5 | flow/conductance/length/pressure、literature model |
| INT-OBJ-008 | Transformer h / layers / attention | P1 §5 | state transitions, trained parameters, Φtr |
| INT-OBJ-009 | graph V/E/b/d | P1 §7 | nodes/edges/branching/depth vs stopping E inP2 |
| INT-OBJ-010 | T / R / External(R) | P1 §8–9 | internal/external stopping boundary |
| INT-OBJ-011 | DH / local horizon-form | P1 §9; P2 §3,C | VED4との差別・共通境界というsource読み |
| INT-OBJ-012 | C / Cij | P2 §1–2,A | scalar closure vs causal log/mutual constraint relation |
| INT-OBJ-013 | C* / Cmax / Δ / Γ / κB / a / ξ / α | P2 §1,A | closure PDE parameters/source/barrier/force |
| INT-OBJ-014 | τ | P2 §1,A | internaldevelopmentparameter。physicalunits継承未確定 |
| INT-OBJ-015 | f | P2 §1 | closure→unresolved quantity relation |
| INT-OBJ-016 | Ωθ / θ | P2 §1–2 | admissible movement region / constraint parameter |
| INT-OBJ-017 | Hij / ρi / λ | P2 §2,A | mutual constraint and causal-log relation |
| INT-OBJ-018 | LF | P2 §2 | inference operation domain / trajectories |
| INT-OBJ-019 | LR | P2 §5 | logs and recursive referencing motion |
| INT-OBJ-020 | LE | P2 §5 | externally dependent emergent stopping layer/attractor |
| INT-OBJ-021 | E | P2 §5 | external stopping operator, not F iteration |
| INT-OBJ-022 | μθ / (A)/(B) movement | P2 §2,5 | thresholdmobility / domainreconfiguration |
| INT-OBJ-023 | Φext / Φnet | P2 §5,9 | external reference field / LE network |
| INT-OBJ-024 | ρresp / responsive-silent threshold | P2 §4,A | response density、threshold not ontological kind |
| INT-OBJ-025 | U / L / Φ(L,H) | P2 §1,E | emergence schema；Φglobalfieldとは別signature候補 |
| INT-OBJ-026 | Ωlife / Ωintel / Jlife | P2 §1,B,E | Bio vocabulary forward comparison |
| INT-OBJ-027 | E(A) particle closure energy / internal vectors | P2 E | VED2引用的再使用、stopping Eとは別 |
| INT-OBJ-028 | Σ / vinf / rres / η | P2 §11,A | 3-axis instability region, no numeric phase boundaries |
| INT-OBJ-029 | vLR / Δvintel | P2 §11 | log speed and speed-scale gap |
| INT-OBJ-030 | knowledge block / consensus / legitimacy | P2 §9–10 | social provisional stopping unit、formalnumerictypingではない |
| INT-OBJ-031 | projection / opening window / TΦ / ∇Φ / Δv / μ | P1 §9; P2 §2,5,B | Con comparison vocabulary; shared operator未確定 |
| INT-OBJ-032 | history / token / log / re-entry | P1 §2,8–9; P2 §4–5,9 | storage/control/reference/social roles distinct |

## 6. Draft equation / formal relation families

| ID | relation family (source notation summary) | locator | inventory only |
|---|---|---|---|
| INT-EQF-DRAFT-001 | s(t+1)=F(s(t)) | P1 §3 | temporal ordering |
| INT-EQF-DRAFT-002 | Φ:S→R | P1 §3 | global constraint signature |
| INT-EQF-DRAFT-003 | Φbio / Φtr:S→R | P1 §5 | substrate-specific bias |
| INT-EQF-DRAFT-004 | Qij=(Dij/Lij)Δpij | P1 §4 | Physarum flow relation |
| INT-EQF-DRAFT-005 | dDij/dt=f(abs(Qij))−Dij | P1 §4 | reinforcement/decay; literal abs notation differs in source |
| INT-EQF-DRAFT-006 | f(Q)=abs(Q)^μ; μ>0 | P1 J §4 | inline source-local nonlinear response |
| INT-EQF-DRAFT-007 | Transformer hidden-state set and layer update | P1 §5 | h_i^(ell), Ftr |
| INT-EQF-DRAFT-008 | I↑ ⇒ ∇·J↑ / correctness⇒divergence | P1 §7 | prose/formal implication family; EN/JA text differences |
| INT-EQF-DRAFT-009 | I(si)↑ | P1 §7 | accumulation shorthand |
| INT-EQF-DRAFT-010 | edge count ∼ node count² | P1 §7 | qualitative combinatorics |
| INT-EQF-DRAFT-011 | paths ∼ b^d | P1 §7 | branching expression |
| INT-EQF-DRAFT-012 | T∈External(R) | P1 §9 | external stopping shorthand |
| INT-EQF-DRAFT-013 | closure balance PDE | P2 J §1 | ∂τC+divJC = drive−ΓC−κB/(Cmax−C) |
| INT-EQF-DRAFT-014 | 0≤C<Cmax; C approaches Cmax | P2 §1,3,A | range/barrier claim |
| INT-EQF-DRAFT-015 | I=f(1−C) and example f | P2 §1 | JA monotonic/examples; full scope Phase01 |
| INT-EQF-DRAFT-016 | FI=α∇C | P2 J §1,A | force-gradient relation |
| INT-EQF-DRAFT-017 | JC=−ξ∇C | P2 J §1,A | closure flux |
| INT-EQF-DRAFT-018 | C:X→[0,Cmax) / C-landscape | P2 §1 | geometric representation |
| INT-EQF-DRAFT-019 | xn+1=F(xn) | P2 §2 | inference iteration |
| INT-EQF-DRAFT-020 | J(F(x))>J(x) | P2 §2–3,D | justification monotonicity premise |
| INT-EQF-DRAFT-021 | F(x*)=x* absence / contradiction proof route | P2 §3,D | theorem source claim; no correctness audit |
| INT-EQF-DRAFT-022 | internal S(x)/stop regress | P2 §3,D | corollary claim |
| INT-EQF-DRAFT-023 | Cij=1−exp(−λρiHij) | P2 J §2 | causal-log/response threshold relation |
| INT-EQF-DRAFT-024 | Ωθ and endogenous θ reconfiguration | P2 §1–2 | movement A/B |
| INT-EQF-DRAFT-025 | U=Φ(L motion,Hij) | P2 §1,E | emergence schema |
| INT-EQF-DRAFT-026 | LE=Φ(LR motion,Hij) | P2 §5 | specific schema; no adoptedcommonΦtype |
| INT-EQF-DRAFT-027 | E=E[LE,xn]; E∉{F^k} | P2 §5 | stopping operator vs inference |
| INT-EQF-DRAFT-028 | Φext≡Φnet | P2 §5,D | isomorphism/identity wording family |
| INT-EQF-DRAFT-029 | Hji≈0 vs positive return | P2 §4,6 | responsive/silent and animism interpretation |
| INT-EQF-DRAFT-030 | Ωintel⊂Ωlife | P2 J §1 | Bio future/domain relation |
| INT-EQF-DRAFT-031 | error tolerance ↔ μθ | P2 J §10,D | claimed equivalence |
| INT-EQF-DRAFT-032 | Δvintel=vinf−vLR | P2 §11 | speed gap |
| INT-EQF-DRAFT-033 | Σ in (vinf,rres,η) | P2 §11,A | qualitative phase region |
| INT-EQF-DRAFT-034 | VED2 E(A) local minima / closure-condition family | P2 J E | imported particle analogy, not stopping-functional derivation |
| INT-EQF-DRAFT-035 | fluid continuity relation ∂ρ/∂t + div(ρv)=0 | P2 J §3 | explicit analogy; no fluid proof of intelligence inferred |

## 7. Primary claim-family inventory

| ID | distinct claim concept | source / language | tags | audit layer | source strength marker |
|---|---|---|---|---|---|
| INT-CLM-001 | 知性は所有能力でなく持続する動態 | P1 E/J abstract,§1–2 | DEF COG FUNC | I2 | is / 定式化 |
| INT-CLM-002 | 知覚・認識・知識・知性の四層区別 | P1 E/J §2 | DEF REP COG | I1/I2 | different structural kinds |
| INT-CLM-003 | 知識は安定した停止構造で真理そのものではない | P1 E/J §2,6 | DEF REP NEG | I1/I2 | is / not truth |
| INT-CLM-004 | 知性は全層を横断し知識を産出・改訂、保存されない | P1 E/J §2 | COG MECH NEC | I1/I2 | continually produces / not stored |
| INT-CLM-005 | 3公理は同時必要な下限、完全理論でない | P1 E/J §3,10 | FORM NEC NEG | I0/I2 | necessary / lower bound |
| INT-CLM-006 | connected state spaceは連続空間に限定しない | P1 E/J §3 | FORM DEF NEG | I0 | connected, not necessarily continuous |
| INT-CLM-007 | temporal orderingで履歴変化が蓄積する | P1 E/J §3 | FORM REP | I0/I1 | requires / update |
| INT-CLM-008 | global Φは局所更新に非還元 | P1 E/J §3–4 | FORM NEC MECH | I0/I1 | irreducible |
| INT-CLM-009 | 3公理はVED/IFGTから論理的独立・意味中立 | P1 E/J §3 | META NEG | I0/I1 | logically independent |
| INT-CLM-010 | I/J/Φは投影的語彙、IFGT一般量の直接同定でない | P1 E/J §4 | REP XSC NEG | I0/I1 | projected uses |
| INT-CLM-011 | Physarum solverと語彙的/構造的対応 | P1 E/J §4 | HOMOLOGY CORR XSC | I0/I1 | same structure / not strict mathematical isomorphism |
| INT-CLM-012 | Physarum研究はglobal Φ非還元性への独立実証的収束 | P1 E/J abstract,§4–5,10 | HOMOLOGY META | I0/I1 | independent empirical line / 示す |
| INT-CLM-013 | PhysarumとTransformerは同じ三条件を満たす | P1 E/J §5 | HOMOLOGY COMP XSC | I1/I2 | both satisfy |
| INT-CLM-014 | 同一cognition/experience/functionalethicalstatusを主張しない | P1 E/J §5 | NEG | I2/I4 | does not claim |
| INT-CLM-015 | Gettierはstopping状態と動的性質の層間不一致 | P1 E/J §6 | COG CORR | I1/I2 | structural diagnostic |
| INT-CLM-016 | JTBへの静的条件追加では動的保証にならない | P1 E/J §6 | NEC NEG FORM | I0/I2 | cannot guarantee |
| INT-CLM-017 | 正しさ蓄積はconnectivity/divergenceを増やす | P1 E/J §7 | MECH FORM COG | I0/I2 | increases / generates |
| INT-CLM-018 | 結合数二乗・経路指数の分岐爆発 | P1 E/J §7 | FORM MECH | I0/I1 | structural not contingent |
| INT-CLM-019 | 知識量/推論速度/専門化/能力強化だけでは止まらない | P1 E/J §7 | NEC COG COMP | I1/I2 | does not solve |
| INT-CLM-020 | overexplanation等は不安定性の4症状という読み | P1 J §7 | COG CORR | I2 | structural symptoms |
| INT-CLM-021 | 個体内推論には停止演算子がない | P1 E/J §8 | FORM NEC COG | I0/I2 | no stopping operator |
| INT-CLM-022 | 疲労/注意/報酬/生理終了は停止でなく中断 | P1 E/J §8（J詳細） | COG MECH NEC | I2 | all / すべて中断 |
| INT-CLM-023 | paperclip/alignment問題は同じ停止不在の構造 | P1 E/J §8（J強化） | COMP COG XSC NEC | I1/I2 | structural root / 誤っている |
| INT-CLM-024 | 停止はログ・応答・合意・遅延への越境を必要とする | P1 E/J §8–9 | NEC SOCIAL | I2/I3 | requires / 必然 |
| INT-CLM-025 | DHIは外部停止へのlocal horizon-form | P1 E/J §9 | DEF XSC | I0/I2/I3 | named / same boundary |
| INT-CLM-026 | DHIはVED4とは別の第二絶対境界でない | P1 E/J §1,9 | NEG XSC | I0/I2 | not a second horizon |
| INT-CLM-027 | 外化は真理を保証せず持続/改訂可能停止を保証 | P1 E/J §9 | SUFF NEG SOCIAL | I2/I3 | does not guarantee truth / guarantees |
| INT-CLM-028 | 推論能力/個体理解/責任の全面外化はしない | P1 E/J §9 | NEG COG SOCIAL PHEN | I2/I3/I4 | not externalized |
| INT-CLM-029 | 物理/Bio/Con/Int四層はproposed comparison、型付け移送でない | P1 E/J §9 | HOMOLOGY XSC NEG | I0/I2/I3 | proposed / no typed translation |
| INT-CLM-030 | 生命層はCon/Intを支える必要基盤というJA記述 | P1 J §9 | NEC XSC COG | I2/I4 | 構造的事実 |
| INT-CLM-031 | Conのfast/slow log/windowとIntの越境の相補性 | P1 E/J §1,9 | CORR XSC | I0/I2/I4 | different projections / same structure |
| INT-CLM-032 | selfを経て未来予測・言語・社会へflowback | P1 J §9; Con参照 | COG SOCIAL XSC | I2/I3/I4 | Consciousness opens → Self sediments → Intelligence |
| INT-CLM-033 | 六制約は必要で十分でない、complete/engineering/norm theoryでない | P1 E/J §10 | NEC NEG FUTURE | I0/I2 | necessary not sufficient |
| INT-CLM-034 | 3条件の収束は恣意性でないことの支持 | P1 E/J §10 | META HOMOLOGY | I0/I1 | convergence / 収束 |
| INT-CLM-035 | 外部停止・生命意識移行・社会制度・AI設計を後続へ | P1 E/J §10 | FUTURE SOCIAL COMP | I2/I3 | future Part II |
| INT-CLM-036 | PartIIはVED差分原理から三層構造を導出すると宣言 | P2 J §0; E abstract | FORM XSC META | I0/I2 | 構造的に導出 / develops |
| INT-CLM-037 | LF/LR/LEの同時動態が個体内外部依存停止を生む | P2 E/J §0,5,12 | MECH COG NEC | I0/I2 | emerges / 同時 |
| INT-CLM-038 | 知性史は推論能力だけでなく停止構造の発達史 | P2 E/J §0 | SOCIAL CORR | I2/I3 | read history as |
| INT-CLM-039 | PartI四層の継承説明（JA別表physical/relational/symbolic/cognitive） | P2 J §0.2 | META REP | I1/I2 | Part I established / 表再述 |
| INT-CLM-040 | Cは操作的安定性で真理でない | P2 E/J §1,10 | DEF NEG | I0/I2 | C is not truth |
| INT-CLM-041 | closure PDE/basic VED formをIntで使用 | P2 J §1,A; E簡略 | FORM XSC | I0 | VED基本式 |
| INT-CLM-042 | Cmax非到達と究極理解/最終判断の非到達 | P2 E/J §1,3 | FORM NEC COG XSC | I0/I2 | unreachable / 構造的禁止 |
| INT-CLM-043 | Ωθ内(A)とθ再編(B)、領域外は発散/停止 | P2 E/J §1–2 | FORM COMP | I0/I1 | movement region |
| INT-CLM-044 | VED-defined emergenceは下位運動+外部Hから上位動態 | P2 E/J §1,E | DEF MECH XSC | I0/I2 | not deduced from lower alone |
| INT-CLM-045 | Bio second-attractor予告に対するInt独自下流構成 | P2 E/J §1,B,E | XSC CORR FUTURE NEG | I0/I2 | proposed / no Bio-established implementation |
| INT-CLM-046 | 推論Fは既存概念地形内、確率的/反復/局所正当化 | P2 E/J §2 | DEF COMP REP | I0/I1 | Definition / F1–F4 |
| INT-CLM-047 | Physarum/TransformerをF actionとして読む | P2 E/J §2,5 | COMP HOMOLOGY | I1/I2 | is action itself / instantiates |
| INT-CLM-048 | Hij応答閾値をCij指数関係で記述 | P2 J §2 | FORM MECH | I0/I1 | 式 / threshold |
| INT-CLM-049 | μθは内生的閾値移動・E設置領域を組み替える | P2 E/J §2,5 | DEF MECH COG | I0/I2 | not mere flexibility |
| INT-CLM-050 | BioDNA長期とsapiens対話短期のθ可変性を同一原理で比較 | P2 J §2,B | HOMOLOGY XSC | I0/I2 | 同じ原理 / local-type guard |
| INT-CLM-051 | P1/P2仮定下Fに内部不動点なし（定理3.1） | P2 E/J §3,D | FORM NEC | I0 | Theorem / proof sketch |
| INT-CLM-052 | 任意内部停止条件Sは推論要求へ戻る（系3.2） | P2 E/J §3; J D | FORM NEC | I0/I1 | no internal S |
| INT-CLM-053 | 非閉包とCmax/VED4horizonは同型（系3.3） | P2 E/J §3; J D | HOMOLOGY ID XSC | I0/I2 | isomorphism / 同型 |
| INT-CLM-054 | 個体内知性完結不能、3collapse attractorsへ | P2 E/J §3; J D | NEC COG | I2 | cannot / inevitable |
| INT-CLM-055 | 応答的/沈黙的世界は閾値regimeでontologyでない | P2 E/J §4 | DEF REP NEG | I0/I1 | threshold phenomena |
| INT-CLM-056 | 沈黙世界でregress持続、branch explosionと同じ構造 | P2 E/J §4 | FORM HOMOLOGY COG | I0/I2 | continues indefinitely |
| INT-CLM-057 | nonclosureはtraceを残しLR/LE創発へproductive | P2 E/J §4–5 | MECH | I1/I2 | because / generates |
| INT-CLM-058 | LRは推論痕跡とその再帰参照、3保存様式 | P2 E/J §5 | DEF REP | I1 | log layer definition |
| INT-CLM-059 | LEは個体内だが外部H依存の動的stopping attractor | P2 E/J §5 | DEF MECH COG | I0/I2 | Definition / arises |
| INT-CLM-060 | μθ→B→E-site projection→LRconvergence→LEの機構 | P2 E/J §5 | MECH COG | I0/I2 | emergence mechanism |
| INT-CLM-061 | Physarum autonomousenvironmentstop / Transformer injectedstop / sapiensμendo | P2 E/J §5 | COMP COG HOMOLOGY | I1/I2 | profile comparison |
| INT-CLM-062 | projectionはConの第四原語を適用、心理防衛でない | P2 E/J §5; J B | XSC ID NEG | I1/I2/I4 | definition itself / not psychological |
| INT-CLM-063 | EはF反復から導出できずLEと現在stateに依存 | P2 E/J §5 | FORM NEC | I0/I1 | E not F^k |
| INT-CLM-064 | Φext≡Φnet、外部性はLEnetworkの見え方 | P2 E/J §5,D | ID FORM SOCIAL | I0/I3 | equivalent / 同型命題5.4 |
| INT-CLM-065 | P1globalΦはΦnetで具体化される | P2 E/J §5,C | XSC META | I0/I3 | refines / implementation |
| INT-CLM-066 | stabilityはtruthでなくrecoverability/revisability | P2 E/J §5,10 | DEF NEG FUNC | I2/I3 | not truth |
| INT-CLM-067 | animismは沈黙世界を応答的として扱う停止設置 | P2 E/J §6 | DEF SOCIAL MECH | I2/I3 | installation / 状態変換 |
| INT-CLM-068 | animism低停止コストが普遍性を説明 | P2 J §6 | MECH SOCIAL | I3 | 低コスト / 普遍性 |
| INT-CLM-069 | Godは未解決→保留演算子、中心化Φext | P2 E/J §7 | DEF SOCIAL MECH | I2/I3 | is / Definition7.1 |
| INT-CLM-070 | 中心化は曖昧性を減らし安定化、単一極限は歴史終点でない | P2 E/J §7 | SOCIAL MECH NEG | I3 | reduces / not progress |
| INT-CLM-071 | religionはLE世代維持・mixed responsive/silent境界管理 | P2 E/J §8 | DEF SOCIAL MECH | I3 | three functions |
| INT-CLM-072 | scienceは停止改訂制度化、religionと真理序列でない | P2 E/J §8–9,D | SOCIAL CORR NEG | I3 | revision / not immature science |
| INT-CLM-073 | 純粋因果推論は有限sapiensに不安定、病的引力子分類 | P2 E/J §8 | COG MECH | I2 | unstable / prevents・buffer |
| INT-CLM-074 | social blockchainは分散LE consensusでtechnicalcryptoでない | P2 E/J §9 | DEF SOCIAL CORR NEG | I3 | not Version Control but Consensus |
| INT-CLM-075 | Gitとsocialの分岐/merge/rollback costは対称/逆 | P2 E/J §9 | COMP SOCIAL HOMOLOGY | I1/I3 | opposite cost structure |
| INT-CLM-076 | legitimacyは原理的非計算可能、継続改訂条件 | P2 E/J §9 | FORM SOCIAL NEC | I0/I3 | cannot be computed |
| INT-CLM-077 | 創造は個体でのみ、社会は事後安定化 | P2 E/J §9 | NEC SOCIAL COG | I2/I3 | only / 社会では起こらない |
| INT-CLM-078 | GettierはC≠truthのevidence、原理的解決不能というJA主張 | P2 E/J §10 | META FORM NEC | I0/I2 | confirms / 原理的に不可能 |
| INT-CLM-079 | knowledgeはaction可能なΦnet暫定block | P2 J §10（EN簡略） | DEF SOCIAL | I2/I3 | Definition10.1 |
| INT-CLM-080 | error toleranceとμθは構造的同値 | P2 J §10,D; E弱いcoupling | FORM ID NEC | I0/I2 | equivalent / 双方向sketch |
| INT-CLM-081 | Σ相図はvinf/rres/η、安定は狭いbandのみ | P2 E/J §11 | FORM COG PRED | I0/I2 | only narrow band |
| INT-CLM-082 | Δvintel増大はLR/LE/μ失敗のfourfoldcollapse | P2 E/J §11 | MECH COG PRED | I0/I2 | collapse / 連鎖 |
| INT-CLM-083 | zero motionは知性でなく不安定性は構成的 | P2 E/J §11 | DEF NEC | I0/I2 | not intelligence / constitutive |
| INT-CLM-084 | highspeedautonomous human/AIは同じphase制約 | P2 E/J §11 | XSC COMP PRED | I1/I2 | same consequence |
| INT-CLM-085 | N1–6 impossibilities/R1–6 necessities/S1sapiens条件 | P2 J §12; E7clauses | NEC COG | I0/I2 | cannot / requires |
| INT-CLM-086 | 一般知性はLF+LR+LE、sapiensはμ移動性追加 | P2 J §12; E §12 | DEF NEC COG | I2 | final constructive statement |
| INT-CLM-087 | 停止と可動性が自由な推論を可能にする | P2 E/J §0,5,12 | NEC FUNC | I2/I3 | free inference requires movable stopping |
| INT-CLM-088 | 理論は使用法/制度正統性/倫理/AGI設計を決定しない | P2 E/J §0,13 | NEG FUTURE | I2/I3 | does not decide |
| INT-CLM-089 | Σ定量化・stoppingfunctional・哲学/AI実践はfuture | P2 E/J §5,13,D,E | FUTURE FORM | I0/I2 | future work |
| INT-CLM-090 | Masterv2.2はv2.1継承+Int追加と宣言 | P2 J A; E A辞書 | META XSC | I0 | 再掲 / inherited |
| INT-CLM-091 | appendixBはCTを含むnonclosure/attractor/horizon対応を拡張 | P2 J B; E B短縮 | HOMOLOGY XSC | I0/I1/I2/I3/I4 | 同じ構造 / proposedguard |
| INT-CLM-092 | appendixCはPartIへの4微修正を提案 | P2 J C; §13 | META FUTURE | I1/I2 | proposal, not implemented |
| INT-CLM-093 | appendixEはemergence比較とLElocalminの記述を追加 | P2 E/J E | HOMOLOGY FORM XSC | I0/I2 | same grammar / proposedtypedOPEN |
| INT-CLM-094 | AI costをstoppingcostとして読む | P2 E D; revision_notes | COMP CORR FUTURE | I1/I3 | can be read / design question |
| INT-CLM-095 | NGs：religion/culture/truthhierarchy/clinicalanthropomorphism除外 | P2 E/J §0,8,D | NEG META | I2/I3/I4 | not / NG1–6 |

同一familyの複数section反復は1件、JAだけの追加命題・言語強度差は同じ行内で明示または独立family化した。WORKING MDの追加候補は後掲historical/AI ledgerへ分離。番号は将来監査の参照用で、truth/dispositionではない。

## 8. Definitions inventory

| ID | term / local definition | locator | definition class |
|---|---|---|---|
| INT-DEF-001 | perception=input availability | P1 §2 | model-local definition |
| INT-DEF-002 | recognition=existing structureへのmapping | P1 §2 | model-local definition |
| INT-DEF-003 | knowledge=stopping structure | P1 §2 | explanatory naming |
| INT-DEF-004 | intelligence=ongoing revisable motion | P1 §1–2 | model-local / explanatory definition |
| INT-DEF-005 | connected S | P1 §3 | formal condition |
| INT-DEF-006 | temporal ordering | P1 §3 | formal condition |
| INT-DEF-007 | global Φ:S→R | P1 §3 | formal signature + global-role definition |
| INT-DEF-008 | I accumulation density | P1 §4 | model-local projected naming |
| INT-DEF-009 | J direction/flow | P1 §4 | model-local projected naming |
| INT-DEF-010 | Φ normative-neutral bias | P1 §4 | model-local naming |
| INT-DEF-011 | interruption vs stopping | P1 §8 | explanatory distinction, not operational test |
| INT-DEF-012 | differential horizon of intelligence | P1 §9 | explanatory boundary naming |
| INT-DEF-013 | C operational stability not truth | P2 §1 | model-local; word operational≠observable calibration |
| INT-DEF-014 | C-landscape (X,C) | P2 §1 | formal representation |
| INT-DEF-015 | Ωθ / θ | P2 §1 | formal/model-local region |
| INT-DEF-016 | emergence U=Φ(L,H) | P2 J definition1.1; E§1 | model-local definition; crossdomainanalogy |
| INT-DEF-017 | inference F / LF | P2 §2 | formal/operator and model-local layer; JA2.1 |
| INT-DEF-018 | justification J:X→R | P2 E §2; J §3 | formal premise |
| INT-DEF-019 | μθ threshold mobility | P2 J2.3; E§1,2 | model-local ability definition |
| INT-DEF-020 | movement A/B | P2 §2 | model-local classification |
| INT-DEF-021 | responsive/silent worlds | P2 §4 | model-local regimes |
| INT-DEF-022 | LR=trace + recursive reference | P2 J5.1; E§5 | model-local definition |
| INT-DEF-023 | LE=externally dependent stopping attractor | P2 J5.2 / E5.1 | model-local definition; numbering differs |
| INT-DEF-024 | external E | P2 J5.3; E§5 | formal schematic operator |
| INT-DEF-025 | Φext / Φnet | P2 §5 | representational identification / network naming |
| INT-DEF-026 | animism | P2 J6.1; E§6 | explanatory naming |
| INT-DEF-027 | God: unresolved→suspended | P2 J7.1; E§7 | explanatory operator naming |
| INT-DEF-028 | religion | P2 §8 | social maintenance naming |
| INT-DEF-029 | social blockchain | P2 §9 | conceptual analogy / consensus naming |
| INT-DEF-030 | knowledge provisional block | P2 J10.1 | social model-local redefinition |
| INT-DEF-031 | Σ / speed-resolution-stiffness | P2 §11,A | qualitative model region |
| INT-DEF-032 | general vs sapiens intelligence | P2 §12 | necessary-condition / functional definition |

## 9. Intelligence-definition variants

| ID | variant | locator | do not merge |
|---|---|---|---|
| INT-IDEF-001 | stopping structureを生成・横断する動態 | P1 §1–2 | 知識所有と区別 |
| INT-IDEF-002 | 3axiomsで特徴づけるintelligence-like lower bound | P1 §3–5 | 必要条件と定義同定を区別 |
| INT-IDEF-003 | 個体内非閉包・external horizonを持つ動態 | P1 §8–10 | 条件と一般知性の同値を未判定 |
| INT-IDEF-004 | LFの推論能力は必要だが単独では知性でない | P2 §2 | 3層との差 |
| INT-IDEF-005 | LF/LR/LE外部H同時運動 | P2 §5,12 | general architecture |
| INT-IDEF-006 | μθ内生移動を伴うsapiens profile | P2 §2,5,12 | general条件へ自動転用しない |
| INT-IDEF-007 | 社会的分散LE/Φnet maintenance | P2 §9 | 個体創造/general intelligenceと同一視しない |
| INT-IDEF-008 | Bio second-attractor / recursive information flow | P2 §1,E; Bio §9 | 外部branch-local forward proposal |
| INT-IDEF-009 | CT social landscape maintenance | CT multiscale; P2 J B | CT-local naming≠Int general definition |
| INT-IDEF-010 | AI/Transformer local LF + suppliedstopping | P1 §5; P2 §5 | P1三公理profileとP2三層profileは別 |

## 10. Strong-language families (contextual inventory)

| ID | claim crosswalk | source | wording / target; no verdict |
|---|---|---|---|
| INT-STRONG-001 | INT-CLM-004 | P1 E/J §2 | continually produces / not stored — 知性は全層を横断し知識を産出・改訂、保存されない |
| INT-STRONG-002 | INT-CLM-005 | P1 E/J §3,10 | necessary / lower bound — 3公理は同時必要な下限、完全理論でない |
| INT-STRONG-003 | INT-CLM-006 | P1 E/J §3 | connected, not necessarily continuous — connected state spaceは連続空間に限定しない |
| INT-STRONG-004 | INT-CLM-007 | P1 E/J §3 | requires / update — temporal orderingで履歴変化が蓄積する |
| INT-STRONG-005 | INT-CLM-008 | P1 E/J §3–4 | irreducible — global Φは局所更新に非還元 |
| INT-STRONG-006 | INT-CLM-016 | P1 E/J §6 | cannot guarantee — JTBへの静的条件追加では動的保証にならない |
| INT-STRONG-007 | INT-CLM-017 | P1 E/J §7 | increases / generates — 正しさ蓄積はconnectivity/divergenceを増やす |
| INT-STRONG-008 | INT-CLM-018 | P1 E/J §7 | structural not contingent — 結合数二乗・経路指数の分岐爆発 |
| INT-STRONG-009 | INT-CLM-019 | P1 E/J §7 | does not solve — 知識量/推論速度/専門化/能力強化だけでは止まらない |
| INT-STRONG-010 | INT-CLM-021 | P1 E/J §8 | no stopping operator — 個体内推論には停止演算子がない |
| INT-STRONG-011 | INT-CLM-022 | P1 E/J §8（J詳細） | all / すべて中断 — 疲労/注意/報酬/生理終了は停止でなく中断 |
| INT-STRONG-012 | INT-CLM-023 | P1 E/J §8（J強化） | structural root / 誤っている — paperclip/alignment問題は同じ停止不在の構造 |
| INT-STRONG-013 | INT-CLM-024 | P1 E/J §8–9 | requires / 必然 — 停止はログ・応答・合意・遅延への越境を必要とする |
| INT-STRONG-014 | INT-CLM-027 | P1 E/J §9 | does not guarantee truth / guarantees — 外化は真理を保証せず持続/改訂可能停止を保証 |
| INT-STRONG-015 | INT-CLM-030 | P1 J §9 | 構造的事実 — 生命層はCon/Intを支える必要基盤というJA記述 |
| INT-STRONG-016 | INT-CLM-033 | P1 E/J §10 | necessary not sufficient — 六制約は必要で十分でない、complete/engineering/norm theoryでない |
| INT-STRONG-017 | INT-CLM-036 | P2 J §0; E abstract | 構造的に導出 / develops — PartIIはVED差分原理から三層構造を導出すると宣言 |
| INT-STRONG-018 | INT-CLM-037 | P2 E/J §0,5,12 | emerges / 同時 — LF/LR/LEの同時動態が個体内外部依存停止を生む |
| INT-STRONG-019 | INT-CLM-041 | P2 J §1,A; E簡略 | VED基本式 — closure PDE/basic VED formをIntで使用 |
| INT-STRONG-020 | INT-CLM-042 | P2 E/J §1,3 | unreachable / 構造的禁止 — Cmax非到達と究極理解/最終判断の非到達 |
| INT-STRONG-021 | INT-CLM-043 | P2 E/J §1–2 | movement region — Ωθ内(A)とθ再編(B)、領域外は発散/停止 |
| INT-STRONG-022 | INT-CLM-044 | P2 E/J §1,E | not deduced from lower alone — VED-defined emergenceは下位運動+外部Hから上位動態 |
| INT-STRONG-023 | INT-CLM-048 | P2 J §2 | 式 / threshold — Hij応答閾値をCij指数関係で記述 |
| INT-STRONG-024 | INT-CLM-049 | P2 E/J §2,5 | not mere flexibility — μθは内生的閾値移動・E設置領域を組み替える |
| INT-STRONG-025 | INT-CLM-051 | P2 E/J §3,D | Theorem / proof sketch — P1/P2仮定下Fに内部不動点なし（定理3.1） |
| INT-STRONG-026 | INT-CLM-052 | P2 E/J §3; J D | no internal S — 任意内部停止条件Sは推論要求へ戻る（系3.2） |
| INT-STRONG-027 | INT-CLM-053 | P2 E/J §3; J D | isomorphism / 同型 — 非閉包とCmax/VED4horizonは同型（系3.3） |
| INT-STRONG-028 | INT-CLM-054 | P2 E/J §3; J D | cannot / inevitable — 個体内知性完結不能、3collapse attractorsへ |
| INT-STRONG-029 | INT-CLM-056 | P2 E/J §4 | continues indefinitely — 沈黙世界でregress持続、branch explosionと同じ構造 |
| INT-STRONG-030 | INT-CLM-057 | P2 E/J §4–5 | because / generates — nonclosureはtraceを残しLR/LE創発へproductive |
| INT-STRONG-031 | INT-CLM-059 | P2 E/J §5 | Definition / arises — LEは個体内だが外部H依存の動的stopping attractor |
| INT-STRONG-032 | INT-CLM-060 | P2 E/J §5 | emergence mechanism — μθ→B→E-site projection→LRconvergence→LEの機構 |
| INT-STRONG-033 | INT-CLM-062 | P2 E/J §5; J B | definition itself / not psychological — projectionはConの第四原語を適用、心理防衛でない |
| INT-STRONG-034 | INT-CLM-063 | P2 E/J §5 | E not F^k — EはF反復から導出できずLEと現在stateに依存 |
| INT-STRONG-035 | INT-CLM-064 | P2 E/J §5,D | equivalent / 同型命題5.4 — Φext≡Φnet、外部性はLEnetworkの見え方 |
| INT-STRONG-036 | INT-CLM-067 | P2 E/J §6 | installation / 状態変換 — animismは沈黙世界を応答的として扱う停止設置 |
| INT-STRONG-037 | INT-CLM-068 | P2 J §6 | 低コスト / 普遍性 — animism低停止コストが普遍性を説明 |
| INT-STRONG-038 | INT-CLM-069 | P2 E/J §7 | is / Definition7.1 — Godは未解決→保留演算子、中心化Φext |
| INT-STRONG-039 | INT-CLM-070 | P2 E/J §7 | reduces / not progress — 中心化は曖昧性を減らし安定化、単一極限は歴史終点でない |
| INT-STRONG-040 | INT-CLM-071 | P2 E/J §8 | three functions — religionはLE世代維持・mixed responsive/silent境界管理 |
| INT-STRONG-041 | INT-CLM-073 | P2 E/J §8 | unstable / prevents・buffer — 純粋因果推論は有限sapiensに不安定、病的引力子分類 |
| INT-STRONG-042 | INT-CLM-076 | P2 E/J §9 | cannot be computed — legitimacyは原理的非計算可能、継続改訂条件 |
| INT-STRONG-043 | INT-CLM-077 | P2 E/J §9 | only / 社会では起こらない — 創造は個体でのみ、社会は事後安定化 |
| INT-STRONG-044 | INT-CLM-078 | P2 E/J §10 | confirms / 原理的に不可能 — GettierはC≠truthのevidence、原理的解決不能というJA主張 |
| INT-STRONG-045 | INT-CLM-080 | P2 J §10,D; E弱いcoupling | equivalent / 双方向sketch — error toleranceとμθは構造的同値 |
| INT-STRONG-046 | INT-CLM-081 | P2 E/J §11 | only narrow band — Σ相図はvinf/rres/η、安定は狭いbandのみ |
| INT-STRONG-047 | INT-CLM-082 | P2 E/J §11 | collapse / 連鎖 — Δvintel増大はLR/LE/μ失敗のfourfoldcollapse |
| INT-STRONG-048 | INT-CLM-083 | P2 E/J §11 | not intelligence / constitutive — zero motionは知性でなく不安定性は構成的 |
| INT-STRONG-049 | INT-CLM-085 | P2 J §12; E7clauses | cannot / requires — N1–6 impossibilities/R1–6 necessities/S1sapiens条件 |
| INT-STRONG-050 | INT-CLM-086 | P2 J §12; E §12 | final constructive statement — 一般知性はLF+LR+LE、sapiensはμ移動性追加 |
| INT-STRONG-051 | INT-CLM-087 | P2 E/J §0,5,12 | free inference requires movable stopping — 停止と可動性が自由な推論を可能にする |
| INT-STRONG-052 | INT-CLM-089 | P2 E/J §5,13,D,E | future work — Σ定量化・stoppingfunctional・哲学/AI実践はfuture |
| INT-STRONG-053 | INT-CLM-093 | P2 E/J E | same grammar / proposedtypedOPEN — appendixEはemergence比較とLElocalminの記述を追加 |
| INT-STRONG-054 | INT-CLM-011 | P1 §4 | same structure / not strict mathematical isomorphism |
| INT-STRONG-055 | INT-CLM-012 | P1 abstract,§4–5,10 | independent empirical line / 独立な実証 |
| INT-STRONG-056 | INT-CLM-013 | P1 §5 | both satisfy / 同一条件 |
| INT-STRONG-057 | INT-CLM-031 | P1 §1,9 | different projections of the same structure |
| INT-STRONG-058 | INT-CLM-034 | P1 §10 | convergence supports non-arbitrary conditions |
| INT-STRONG-059 | INT-CLM-047 | P2 §2,5 | Physarum flow as F action itself |
| INT-STRONG-060 | INT-CLM-050 | P2 J §2,B | 同じ原理でDNAと知性のθ可変性を統一 |
| INT-STRONG-061 | INT-CLM-065 | P2 §5,C | P1 global Φ refined / concretized as network |
| INT-STRONG-062 | INT-CLM-091 | P2 J B | same structures across domains / guarded homology |

## 11. Negative-scope ledger

| ID | negative claim / explicit guard | locator | scope |
|---|---|---|---|
| INT-NEG-001 | complete theory/engineering/normative theoryを提示しない | P1 §1,10 | purpose |
| INT-NEG-002 | 3axiomsはhigh intelligenceの十分条件でない | P1 §3,10 | necessary lower bound |
| INT-NEG-003 | connected≠continuous; ordering≠physicalclock | P1 §3 | formal interpretation |
| INT-NEG-004 | no meaning/optimization/subject presupposition | P1 §3 | primitive scope |
| INT-NEG-005 | projected I/J/Φ not general IFGT identification | P1 §4 | typed inheritance |
| INT-NEG-006 | Physarum/Transformer cognitive/phenomenal/ethicalidentityを主張しない | P1 §5 | crossdomain |
| INT-NEG-007 | Gettierへの新JTB条件追加が目的でない | P1 §6 | method |
| INT-NEG-008 | externalized stopping≠truth guarantee | P1 §9 | semantic truth |
| INT-NEG-009 | 新たな第二絶対DH/4layerphysicalidentity/reduction/transitiontheoryでない | P1 §9 | crossscale |
| INT-NEG-010 | 個体推論能力・feltunderstanding・責任全面外化でない | P1 §9 | individual/social |
| INT-NEG-011 | religionculture/scienceの真理優劣・護教/批判でない | P2 §0,6–8 | NG1 |
| INT-NEG-012 | ethics/normative prescriptions/AGIdesign支持否定しない | P2 §0,11,13 | NG2/3 |
| INT-NEG-013 | epistemologyhistory網羅/個別歴史心理解釈でない | P2 J §0 | NG4/5 |
| INT-NEG-014 | continuousstoppingfieldはanthropomorphism/eliminativismでない | P2 J §0,5 | NG6 |
| INT-NEG-015 | stoppingは自由否定/completeclosureでない | P2 §0,5,12 | functional scope |
| INT-NEG-016 | projection≠psychologicaldefense/subjectiveimage | P2 §1,5,D | Con correspondence scope |
| INT-NEG-017 | responsive/silent≠ontological kinds | P2 §4 | threshold scope |
| INT-NEG-018 | animism/Godのspirits/explanatoryentityの事実性を主張しない | P2 §6–7 | socialinterpretation |
| INT-NEG-019 | historyschema≠linearprogress/singlepolefinalendpoint | P2 §7–9 | historical scope |
| INT-NEG-020 | socialblockchain≠technicalblockchain/versioncontrol | P2 §9 | analogy |
| INT-NEG-021 | pathologylabels≠clinicaldiagnosis | P2 §8,11 | cognitive scope |
| INT-NEG-022 | Φext≠transcendent independent field | P2 §5 | ontological scope |
| INT-NEG-023 | Bio/physics homology≠commoncarrier/mechanism/typedtranslation | P2 §1,2,9,B,E; fig5/9 | crossbranch |
| INT-NEG-024 | C≠truth / operational stability≠correctness | P2 §1,5,10 | epistemic scope |

## 12. CT dependency ledger

| ID | Intelligence locator → CT target | relation | mapping / validation boundary |
|---|---|---|---|
| INT-CTDEP-001 | P2 J §0.2 theory-tree/representation row, §0.6–0.7; B.1 → CT concept/terrain/closure | homology table | CT column explicit; carrier/units/map inverse not supplied |
| INT-CTDEP-002 | P2 J B.1 → CT概念準安定/attractor/境界/分岐 | vocabulary + structural comparison | multiple rolesをshared theoremにしない |
| INT-CTDEP-003 | P2 §2 F acts within existing conceptual landscape → CT-like landscape vocabulary | representation; CT-specific attribution未確定 | 具体的CTversion/eq pointer未記載 |
| INT-CTDEP-004 | P2 §5 LR/sedimented terrain/reentry → CT-like vocabulary | vocabulary reuse candidate | 全てのlog用語をCT由来と推定しない |
| INT-CTDEP-005 | CT sections/multiscale.tex Intelligence as Landscape Maintenance → Int papers | documentary / conceptual handoff | currentCTexplicitlyno validationtransfer/generaldefinition |
| INT-CTDEP-006 | CT sections/introduction.tex table; conclusion.tex; core_equations.tex → Intelligence | navigation / conceptual comparison | downstream applicationラベルはprooforderでない |

## 13. Consciousness dependency ledger

| ID | locator / target | relation | boundary |
|---|---|---|---|
| INT-CONDEP-001 | P1 §1,9 → consciousness fast/slow log referencing | architecture / vocabulary | 個体内temporalnonclosure vs個体外horizon |
| INT-CONDEP-002 | P1 J §9 → Con §4.1 Bio, §7 SSO | architecture / documentary | exactcitedversionnotpinned |
| INT-CONDEP-003 | P1 J §9 → Con §18.10 selfsediments/Intflowback | documentary / sequence | 現行Conはhandoff非generationproof |
| INT-CONDEP-004 | P1 §9 window Δv,μ,τ,TΦ,∇Φ | notation / proposed comparison | units/windowmappingnotinherited |
| INT-CONDEP-005 | P2 §2,5 → Consciousness projection/fourthprimitive | formal-role reuse / identity-strength wording | sameprojector型変換未提示 |
| INT-CONDEP-006 | P2 B → projection vspsychologicalprojection | homology / analogy | psychdefense否定 |
| INT-CONDEP-007 | P2 B,fig9 → SSO/TCA/temporalnonclosure | homology | sharedcarrierproofなし |
| INT-CONDEP-008 | P2 §11 Δvintel speedgap → Confastslowcomparison | structural analogy | vLRとConτ同一でない |
| INT-CONDEP-009 | Con sections/formal_mapping.tex → Intelligence projecteduses/§9.4 | reciprocal methodological comparison | currentCon明示no commonlaw/typedtranslation/validationtransfer |
| INT-CONDEP-010 | Con sections/discussion.tex,conclusion.tex,correspondence_map.tex → Intelligence | handoff / documentary | self/futurelanguage/sociallog順序、empiricalauthority移送なし |

## 14. Bio / ecological dependency ledger

| ID | locator / target | relation | boundary |
|---|---|---|---|
| INT-BIODEP-001 | P1 §4 → Tero2007Physarum solver | formal vocabulary homology / source claims empirical convergence | externalpaper内容はweb検証しない |
| INT-BIODEP-002 | P1 §5 → Nakagaki2000/Kobayashi2006/Vaswani2017 | crosssubstrate examples | source報告とrepo-local dataを区別 |
| INT-BIODEP-003 | P1 J §2 → Gibson1986/ecologicalperception | conceptual precedent | JA-onlycite; operationalintcriterionでない |
| INT-BIODEP-004 | P1 §8 → fatigue/reward/attention/energy/homeostasis | biological/cognitive explanation | Bio-specificresult引用と一般言及を区別 |
| INT-BIODEP-005 | P1 J §9 → life必要基盤/Conbuffer | structural continuity/necessity | Transformerとのrole差を後続へ |
| INT-BIODEP-006 | P1 §9 → Bioquasiclosure/metabolic/reproductivecycles | proposed crossdomain analogy | currentguard commoncarrier/mechanism否定 |
| INT-BIODEP-007 | P2 §1,E → Bio Ωlife/Ωintel第二attractor | forward conceptual proposal | currentBio §9は実装未確立と明示 |
| INT-BIODEP-008 | P2 §2,B → Bio F(x;θ), DNA-likeθ | notationreuse/analogy | inferenceFとBioflow別signatureguard |
| INT-BIODEP-009 | P2 §2,B → evolutionlongtime/sapiensshorttimeθmobility | generalization / sameprinciple wording | typedbridgeなし |
| INT-BIODEP-010 | P2 §5 → Physarum externaltrail/networkstopping | biological/computational profile | μfixedとautonomousstoppingを別々に記録 |
| INT-BIODEP-011 | P2 §9,E → Bio memory/language/interactionfuture | downstream proposed construction | BioalreadydemonstratedsharedLEとはしない |
| INT-BIODEP-012 | bio-ifgt sections/intelligence_second_attractor.tex,relation_to_note.tex,discussion.tex | reverse conceptual handoff | second-attractor stableimplementation/cognitivetranslationOPEN |

## 15. VED / IFGT inheritance ledger

| ID | Intelligence locator | reused source/object | declared relation / exact authority limit |
|---|---|---|---|
| INT-UPSTREAM-001 | P1 §1 | VEDVol1–4 bibliography / paper/vol1–4 | differential-development syntax、selfcontainedargument。generic2026preprintでcommit/page未指定 |
| INT-UPSTREAM-002 | P1 §3 | VED/IFGT | axioms logicallyindependent宣言。derivedと同一にしない |
| INT-UPSTREAM-003 | P1 §4 | IFGT I/J/Φ | projected uses・no directgeneralquantityidentification。units/types自動継承なし |
| INT-UPSTREAM-004 | P1 §9 | VEDVol4 Differential Horizon | local horizon-form/sameboundary、notsecondabsolute。typedmap未提示 |
| INT-UPSTREAM-005 | P1 §9 | VED4 renormalization/finiteinternalabsorption | formal-role comparison; physicscognitionidentity否定 |
| INT-UPSTREAM-006 | P2 J §0,13 | VED basicaxiom differenceexists | structuralderivation宣言；exactproofdependencychain未確定 |
| INT-UPSTREAM-007 | P2 J §1 | VED closure PDE C/JC/Δ/Γ/barrier | basicform提示。現行upstreamのどの版か固定pointerなし |
| INT-UPSTREAM-008 | P2 §1 | IFGT I=f(1−C), FI=α∇C | source-local specialization。kernel/space/range継承未確定 |
| INT-UPSTREAM-009 | P2 J §2 | Cij=1−exp(−λρiHij) | mutualconstraint thresholdへreuse。Vol1causallogと同glyphで自動同定しない |
| INT-UPSTREAM-010 | P2 §3,D | Cmax nonclosure / VED4horizon | isomorphism/corollary wording；map/inverse/invariant未指定 |
| INT-UPSTREAM-011 | P2 J A | MasterTablev2.1→v2.2 | v2.2はlocalappendixに存在。v2.1exactartifactNOT LOCATED |
| INT-UPSTREAM-012 | P2 J E | VEDVol2 causalCij/internalvectors/E(A) | particleclosure/localminimum↔LEemergencecomparison；currentguardnottypedproof |
| INT-UPSTREAM-013 | P2 §1,E | U=Φ(L,H) | sameemergencegrammar宣言とproposedguard共存 |
| INT-UPSTREAM-014 | root README/docs/navigation/claim_status.md | application-layerlevel4 / VED tree | navigation≠proof。root claims/open_problemsはInt専用結果でない |

## 16. Part I ↔ Part II dependency ledger

| ID | Part I source → Part II use | class | proof / strengthening / language |
|---|---|---|---|
| INT-P1P2-001 | P1 §2四層 → P2 §0,C | exposition continuation | JA§0別四層tableを併記。独立derivationでない |
| INT-P1P2-002 | P1 §3axioms → P2 §1–2 | reuse / reinterpretation | P1independenceとP2VEDderivation宣言差 |
| INT-P1P2-003 | P1 §4–5Physarum/Transformer → P2 §2,5 | profileextension | 3axioms vs3layers; TransformerLE否定、sapiens追加 |
| INT-P1P2-004 | P1 §6Gettier → P2 §10,D | structuralformalizationclaim | JAprincipallyunsolvable/μequivalenceで強化 |
| INT-P1P2-005 | P1 §7branching → P2 §3,4,11 | formalization / phaseextension | Jmonotonicity/Theorem3.1 added, quantitativevalidationとは未認定 |
| INT-P1P2-006 | P1 §8individualnonclosure → P2 §3 | purported formalization | Theorem3.1proofsketchexists; P1wholeclaimproofか未判定 |
| INT-P1P2-007 | P1 §8externalstopfuture → P2 §5LE | extension / qualification | insideindividualbutexternaldependency; P1 nointernaloperatorとの語義境界 |
| INT-P1P2-008 | P1 §9globalΦ/externalstopping → P2 Φext≡Φnet | socialinstantiationclaim | sameΦtypedinheritance未提示 |
| INT-P1P2-009 | P1 §9fourlayerhorizon → P2 B/E | appendixhomologyexpansion | CT/socialcolumns/secondattractors追加 |
| INT-P1P2-010 | P1 §10futurePartII → currentPartII | documentarychronology | P1futurewording残存 |
| INT-P1P2-011 | P2 J §13,C → P1§5/6/8/9微修正 | reverseeditorialproposal | 4修正は提案、Phase00で実装しない |
| INT-P1P2-012 | P2 EN C / JA C,D | versionasymmetricformalization | ENmapping4items; JAfullsectionmapping+proofsketches |

## 17. Homology / cross-domain correspondence ledger

| ID | source → target / locator | asserted preserved role / layer | mapping / inverse / invariant / source evidence / authority |
|---|---|---|---|
| INT-HOMO-001 | P1 §4 Tero Q,D,reinforcement,BC → J,I,projection,Φ | flow/log/bias; I0/I1 | lexicaltable explicit; invertibletypedmap未提示; citesTero2007; currentJA+EN |
| INT-HOMO-002 | P1 §5 Physarum ↔ Transformer | S/order/Φ三公理; I1/I2 | 3propertycomparison; inverse未提示; namedliterature; no cognitiveidentityguard |
| INT-HOMO-003 | P1 §9 VED4DH ↔ Int localhorizon | unreachability/divergence/finiteabsorption; I0/I2 | descriptiverole; inverse/invariant未指定; VEDVol4cite |
| INT-HOMO-004 | P1 §9 physical ↔ Bio ↔ Con ↔ Int | fourlayerroles; I0/I2/I4/I3 | table/fig5; no sharedcarrier/mechanism/typedmapguard |
| INT-HOMO-005 | P1 J §8 paperclip ↔ individual nonclosure | nointernalstop; I1/I2 | structuralanalogy strongrootlanguage; no commonstate mapping |
| INT-HOMO-006 | P2 §3,D nonfixedF ↔ Cmax ↔ DH | nonclosure; I0/I2 | same structure/isomorphism, proofsketchcrosswalk nottypedbijective map |
| INT-HOMO-007 | P2 §4 regress ↔ branching | sameinferenceextension; I0/I2 | qualitativestructure; invariant未指定 |
| INT-HOMO-008 | P2 §1,E physicalparticle ↔ life ↔ LE | lower motion+H→upperattractor; I0/I2 | U=Φ(L,H)schematic; no typedinverse; appendixevidenceはsource-localcomparison |
| INT-HOMO-009 | P2 J B.1 CT ↔ physical/Bio/Con/Int | closure/attractor/horizon/branching; I0/I1/I2/I4 | CTcolumnJAonly; no CTversion/operationalmap |
| INT-HOMO-010 | P2 J B.2 / fig5 threeemergencecases | particle/life/stopping; I0/I2 | guardedformalroles; no mechanismidentity |
| INT-HOMO-011 | P2 §5,B.3 Conprojection ↔ IntE-siteprojection ↔ psychprojection | projection role; I1/I2/I4 | definitionapplicationlanguage、psych用語guard; commonoperator未定義 |
| INT-HOMO-012 | P2 J §2,B.4 DNAθ ↔ Intθ ↔ sapiensμ | constraintmobility; I0/I2 | time-scalecomparison; sameprinciplewording; no domain/codomainmap |
| INT-HOMO-013 | P2 §2,B.5 BioF ↔ inferenceF | localstateevolution role; I0/I1 | explicitsource-localtypingguard; sameglyphnotsharedvectorfield |
| INT-HOMO-014 | P2 §5,B.6 Physarum/Transformer/sapiens | LF/LR/LEstorage/μprofiles; I1/I2 | tablecomparisons; empiricaldatasetnotlocatedinbranch |
| INT-HOMO-015 | P2 §6–9,B.6 animism/God/religion/socialBC | LEinstallation/compression/maintenance/sync; I2/I3 | historicaloperatingforms; notlinearprogressguard |
| INT-HOMO-016 | P2 §9 Git ↔ socialBC | branch/merge/rollback vsconsensus; I1/I3 | costcontrast ratherthan literalprotocolisomorphism |
| INT-HOMO-017 | P2 §5,D Φext ↔ Φnet | same stopping relation external/internalview; I0/I3 | equivalence sign/proofsketch; no explicitinverse/map signature |
| INT-HOMO-018 | P2 J §10,D error tolerance ↔ μθ | revisability/endogenousmovement; I0/I2 | bidirectionalsketchpresent; independentcriterionnotfixedhere |
| INT-HOMO-019 | P2 §11 ConΔv ↔ IntΔvintel | speedgap/logtracking; I0/I2/I4 | analogousdifference; sameclock/unitnotstated |
| INT-HOMO-020 | P2 B/E/fig9 physics/Bio/Con/Int/social | nonclosure→attractor→sustaineddynamics; I0–I4 | proposedcomparison guards; ENE samegrammarwordingretained |
| INT-HOMO-021 | P2 J E VEDemergence ↔ weak/strong/holistic/functional emergence | dynamicrelationalposition; I0/I2 | conceptcomparison; notnewexternalempiricalsupport |

## 18. Emergence / stopping inventory

| ID | source claim / source layer | locator | classification without verdict |
|---|---|---|---|
| INT-EMERG-001 | knowledge停止 vs intelligence運動 | P1 §2 | cognitive/representational |
| INT-EMERG-002 | globalΦemergence nonlocal constraint | P1 §3–4 | formal/computational |
| INT-EMERG-003 | individualnoT/regress | P1 §8 | formal/cognitive |
| INT-EMERG-004 | externalDH/logconsensus | P1 §9 | cognitive/socialboundary |
| INT-EMERG-005 | nonfixedpoint theorem | P2 §3,D | formal source theorem |
| INT-EMERG-006 | LRfromnonclosuretraces | P2 §4 | computational/functional emergence |
| INT-EMERG-007 | LEfromLRmotion+H | P2 §5 | formal-schema/cognitive stopping |
| INT-EMERG-008 | μ/B/Einstallation/convergence | P2 §5 | mechanism-language/schema |
| INT-EMERG-009 | Physarum autonomous vs Transformer injected stop | P2 §5 | biological/computationalprofile |
| INT-EMERG-010 | Biosecondattractor | P2 §1,E | forwardbiological/intelligencecomparison |
| INT-EMERG-011 | VEDparticleclosure/life/stopping emergent U | P2 E | crossdomainformalrole |
| INT-EMERG-012 | Φnet synchronization | P2 §5,9 | social emergence |
| INT-EMERG-013 | religion/stopping historicalmaintenance | P2 §6–9 | social/history |
| INT-EMERG-014 | Σ narrow stableLE vs rigid/divergent | P2 §11 | qualitativephase/cognitive |

## 19. Landscape / language / log roles

| ID | object/use | locator | storage / control / communication / social role |
|---|---|---|---|
| INT-LOG-001 | knowledge sediment / stablelog | P1 §2 | storage; intelligenceoperatesnotstored |
| INT-LOG-002 | I accumulatedcorrectness and J branching | P1 §4,7 | representation/control |
| INT-LOG-003 | records,response,agreement,delay | P1 §8–9 | external stopping/socialcoordination |
| INT-LOG-004 | Conpastlog/futureflow | P1 J §9 | temporalreference/handoff |
| INT-LOG-005 | existing conceptual landscape | P2 §2 | inference stayswithincategories; no automaticCTtheorem |
| INT-LOG-006 | LFtrajectoryleavestrace | P2 §4 | historygeneration |
| INT-LOG-007 | environmental/individual/frozenLR | P2 §5 | three storage locations distinct |
| INT-LOG-008 | LRrecursive reference / re-entry | P2 §5 | control/feedback, notviciousnessverdict |
| INT-LOG-009 | Transformerweights/context/tokens/EOS | P2 §5 | frozen/volatilelog; suppliedstop |
| INT-LOG-010 | E-siteprojection | P2 §5 | control notsemantictruth |
| INT-LOG-011 | ritual/text/institution | P2 §8 | crossgenerationcommunication/stoppingmaintenance |
| INT-LOG-012 | socialblock/fork/consensus/historyresponsibility | P2 §9 | socialstabilization notcryptodata |
| INT-LOG-013 | knowledgeasactionableprovisionalblock | P2 §10 | storage/socialaction |
| INT-LOG-014 | newconcept/dimensioncreationvsinference | P2 §2,9 | individualcreativechange vs socialafterward |
| INT-LOG-015 | CTsharedlandscape/languagehandoff | CT multiscale; P2 J B | relatedlocalvocabulary not validatedsemanticmap |

## 20. AI / LLM inventory

| ID | source / target | claim strength / role | boundary |
|---|---|---|---|
| INT-AI-001 | P1 §5 Transformer hidden layers/attention/trainingloss | 3axiomssatisfied; computationalhomology | not literalcognition/experience |
| INT-AI-002 | P1 §7 moreknowledge/reasoning/speed/specialization | categorical nonremedy forstopping | notempiricalbenchmarkinventory |
| INT-AI-003 | P1 §8 paperclip/Bostrom/alignment | structuralroot; JA六十年/誤った応答のstrongclaim | Bostrom bibkeynotlocated; externalfactnotverified |
| INT-AI-004 | P1 J §8 artificialsystemswithoutBiointerruptions | inferencecontinuesresourcespermitting | sourceclaimnotmodernAIknowledge |
| INT-AI-005 | P1 §10 externalstopdesign futurePartII | futureengineeringdirection | noimplementation authorized |
| INT-AI-006 | P2 §2,5 Transformer LF/weights/context/EOS | no ownLE; stopinjectedtask/decoding | architectureprofile vs P1lowerbound |
| INT-AI-007 | P2 §11 highspeedautonomoussystem | qualitativeinstabilitysamephasehuman/AI | no AGIdesignendorsement |
| INT-AI-008 | P2 E D; source_md/revision_notes AIcost | stoppingdesigncost beyondcompute/electricity | conceptualfuturecomparison |
| INT-AI-009 | P2 §0,13 AI implementation/ethicsnonintervention | negative scope | no AGI blueprint / normative decision |

Intelligence TeX/MD内のliteral RSI / ERI / LLM は単語境界検索で未検出（Transformer/AI/AGIは上表）。agentは一般モデル主体として現れるが、agent-systemコード・RSI/ERI理論を追加していない。root docs/ai_spineは別navigation scopeでありIntelligence主張集合を自動拡張しない。

## 21. Social-intelligence families

| ID | distinct social role | locator | relation class |
|---|---|---|---|
| INT-SOC-001 | individualnonclosure→externalrecordsagreementdelay | P1 §8–9 | necessityclaim |
| INT-SOC-002 | truthnotguaranteedbutrevisablestops | P1 §9 | functionalclaim |
| INT-SOC-003 | self/terrain→language/sociallogs | P1 J §9 | Conhandoff |
| INT-SOC-004 | LEnetworkΦnet | P2 §5 | sharednetwork/aggregation-likepresentation; typedaggregationrule未特定 |
| INT-SOC-005 | externalΦappearance | P2 §5 | identity/isomorphismwording |
| INT-SOC-006 | animismresponseinstallation | P2 §6 | historicalsocialmodel |
| INT-SOC-007 | Godcentralization | P2 §7 | stoppingreferencecompression |
| INT-SOC-008 | religiongenerationmaintenance | P2 §8 | institutionalcontinuity |
| INT-SOC-009 | scienceinstitutionalrevision | P2 §8–9 | comparativestoppingoperation |
| INT-SOC-010 | socialBCconsensus | P2 §9 | distributedstoppingnottechnicalprotocol |
| INT-SOC-011 | legitimacy/history/responsibilitynoncomputability | P2 §9 | socialformal-strengthclaim |
| INT-SOC-012 | individualcreation vs socialafterward | P2 §9 | scale-separationclaim |
| INT-SOC-013 | knowledgeprovisionalcollectiveblock | P2 §10 | localfunctiondefinition |
| INT-SOC-014 | stableΣ / collectiveoperatingforms | P2 §11–13 | qualitativeextension |
| INT-SOC-015 | CTsociallandscapemaintenance | CT multiscale; P2 J B | externalbranchlocaldefinition; not generalInt |

## 22. Prediction / empirical / future task draft inventory

| ID | source-named direction / target | locator | status as written, not execution |
|---|---|---|---|
| INT-PRED-DRAFT-001 | Physarumnetwork/maze/rhythmexample | P1 §4–5 | namedexternalobservational/modelreference; notnewprediction |
| INT-PRED-DRAFT-002 | Transformerlayertransition/attentionunderaxioms | P1 §5 | comparativeexample |
| INT-PRED-DRAFT-003 | accumulatedcorrectness→morebranching | P1 §7 | qualitativedirection |
| INT-PRED-DRAFT-004 | speed/knowledge/capabilityincreasewillnotselfstop | P1 §7–8 | directionalclaim |
| INT-PRED-DRAFT-005 | fatiguedinferencecanresume | P1 J §8 | behavioralexample |
| INT-PRED-DRAFT-006 | externalizedstop/AI safetyarchitecture | P1 §9–10 | futuredesignquestion; no design performed |
| INT-PRED-DRAFT-007 | Bio-Con-Inttransitiondynamics | P1 §9–10 | explicitfuturework |
| INT-PRED-DRAFT-008 | otherbiologicalsystems / convergence extensions | P1 §10 | futurecomparison |
| INT-PRED-DRAFT-009 | changingthresholdresponse/silentregime | P2 §2,4 | qualitativecomparativedirection |
| INT-PRED-DRAFT-010 | Physarum/Transformer/sapienslog-stopprofiles | P2 §5 | namedarchitecturecomparison |
| INT-PRED-DRAFT-011 | stoppingfunctional localmin formalization | P2 §5,13,E | futureformalization vs appendixpresenttense |
| INT-PRED-DRAFT-012 | animismcost / centralizationambiguity | P2 §6–7 | qualitativesocialdirection |
| INT-PRED-DRAFT-013 | religion/science/BCmaintenance/revision | P2 §8–9 | historicalcomparisons, notexecutedstudy |
| INT-PRED-DRAFT-014 | branch/merge/rollbackcostsocialvsGit | P2 §9 | comparativeclaim |
| INT-PRED-DRAFT-015 | vinf/rres/η and speedgapcollapse | P2 §11 | qualitativephaseprediction; quantitativeΣfuture |
| INT-PRED-DRAFT-016 | clinical/pathologicalattractorapplication | P2 §8,11,13 | future/caution; notclinicaltest |
| INT-PRED-DRAFT-017 | μθ relocation / error tolerance | P2 §10–12 | qualitativestructuraldirection |
| INT-PRED-DRAFT-018 | philosophymeaning/understanding/subjectivity | P2 §13 | futurework |
| INT-PRED-DRAFT-019 | AIcost/stoppingengineeringpracticalproblems | P2 E D; J §13; revision_notes | futurework, no protocol |
| INT-PRED-DRAFT-020 | P1§5/6/8/9微修正 | P2 J §13,C | futureeditorialtask, notempiricalprediction |

## 23. EN/JA structure, bibliography, code and distribution

### 23.1 Language alignment

| Item | Part I | Part II |
|---|---|---|
| body section boundary | §1–10 aligned, abstract各1 | §0–13 aligned、JA abstract空欄、ENabstract本文あり |
| included content | 11 E + 11 J | 14 E + 14 J + appendices5 E +5 J |
| displayed bracket blocks | E15 / J15 | E28 / J32（本文+補遺、entry含む） |
| same mathematical content? | count一致のみ。JA日本語text付き関係/inline追加があり完全parity未認定 | countも異なる。JAPDE、追加関係/証明sketchがある |
| figures | 同じ5families、言語別PNG/SVG | 同じ9families、言語別PDF/SVG |
| translation authority | JAcurrentbuild; ENprimary/translation認定UNKNOWN | JAprimary; ENdraft |
| appendices | none | A–E言語非対称、Dは別内容 |

上記display countは `\\[` をbeginとしてsource集合に数えたartifact-level inventory。式family数35とは別。Phase01でinline/grouping/signatureを固定する。これをfull equation auditとはしない。

### 23.2 Bibliography

| Part / file | entries | EN cited keys | JA cited keys | unresolved cited keys | appendix-only |
|---|---:|---:|---:|---:|---|
| I refs.bib | 13 | 12 | 13 | 0 | appendicesなし |
| II refs.bib | 0 | 0 | 0 | 0 | 0（無citationで内容参照は多数） |

Part I keys: `VEDVol1`, `VEDVol2`, `VEDVol3`, `VEDVol4`, `IFGT`, `BioIFGT`, `Consciousness`, `Gettier1963`, `Gibson1986`, `Nakagaki2000`, `Kobayashi2006`, `Tero2007`, `Vaswani2017`。JA-only keyは `Gibson1986`、EN-only0。VED/IFGT/Bio/Con各entryは2026 GitHub preprintというgeneric書誌で版固定が弱い。外部文献役割はGettier問題、ecologicalperception、Physarummaze/rhythm/solver、Transformerarchitectureというsource上の参照先として記録する。Part I JA§10のliteral角括弧key列と実際のcite commandは区別した。

Part II refs.bibは移植時に追加予定というcommentだけ。引用key未解決0は文献provenance完備を意味しない。Gettier、James/Dewey、Git、VED/Bio/Con/CT、historicalreligion等のnamedreferencesにdedicated citeがない。Bostrom/paperclip等もPart Iの13keyにない。外部文献本文の検証・質評価はしていない。

### 23.3 Code / simulation / data artifact inventory

`rg --files`に加えignoredファイルを含め両branchを列挙した。Part I 156 files、Part II 199 files（TeX/fontcache/OSmetadata含むtask-start filesystem数）。scientific code/notebook/data pipeline/estimator/model-output dataset/simulation logは両branchでNOT LOCATED。図4growth curvesや図8phase diagramを生成結果と認定しない。

存在する実行関連artifactはPart II `Makefile`（LuaLaTeX/bibtex/clean、defaultJA、build/出力）、P1 READMEのLuaLaTeX/bibtex手順、SVGeditablepresentation、TeX preamble/macros、`.texmf-var/`のLua/LUC/fontcache。これらは研究simulation/codeと区別。`.aux/.toc/.out/.log/.bbl/.blg`はTeX由来buildoutputs、`.DS_Store`はOSmetadata。Part II `build/.gitkeep`とignored `build/main*.pdf`も保持。codeを実行せず、buildを実行せず、cacheを消去していない。実施したPythonはread-only metadata/hash/PDF抽出・audit用一時renderのみ。

### 23.4 Distribution inventory / freshness


| Distribution | pages | relation / freshness | SHA-256 |
|---|---:|---|---|
| `intelligence-part1/main.pdf` | 26 | EN parallel source/draft distribution; full freshness UNRESOLVED（再buildしていない） | `0f5c86a8615537fd09536249ae223f33c4903249df710aee1dd0937d263802be` |
| `intelligence-part1/main_ja.pdf` | 73 | JA current manuscript distribution; full freshness UNRESOLVED（再buildしていない） | `0b9344a0dd096f068ab245db0c555f31ec222ac83b4fb89f9271af4b46d8dfcb` |
| `intelligence-part2/main.pdf` | 30 | EN parallel source/draft distribution; full freshness UNRESOLVED（再buildしていない） | `226f68349d6cd3b1eca07861f084adbea281c7cadd385f09c2f9ac3168b39fa0` |
| `intelligence-part2/main_ja.pdf` | 123 | JA current manuscript distribution; full freshness UNRESOLVED（再buildしていない） | `c589361e3b35b040cbd61d0fd2cd11ac13d8672d14bba9b6ca312588dc2c0aba` |

PDFmetadataはいずれもLuaTeX1.21.0 / TeXLive2025、CreationDateはP1 2026-09-09 06:41:17 / 06:43:03 JST、P2 05:41:09 / 05:41:24 JST。timestamp単独ではfreshnessを証明しない。タイトル/目次/末尾/文献とscope passageをPDF textで確認し、全4rootPDFのfirst/lastを視認した。図assets28variantsを別に視認。全252頁のlayout auditは行っておらず、完全なvisual QAの合格を主張しない。

P1 rootPDFは画像5件ずつ、P2 rootPDFにはraster image objects17件ずつがあり、sourceのfigure family数9とは別。P2 root ENのappendixEはsamegrammarの文、JA末尾はtypedtranslationOPENの文を含む。JA概要空欄、EN文献12/JA13、P2空Referencesはsource構造と対応する。

P2 ignored build/main.pdfは30頁、build/main_ja.pdfは122頁（rootJAは123頁）。いずれもrootとSHA不一致、古いlog/mtimeはJune4由来。Makefileはbuild/へ出力するがrootへcopyする規則を持たない。従って「make出力=root配布」を仮定しない。P1 log26/73頁、P2旧log30/122頁。旧logにoverfull/hyperrefPDF-string/font警告があるがrootの現行layout defectと同定しない。

### 23.5 Historical Markdown coverage

Part I draft_ja.md、Part II combined/appendices/revision_notesを別artifactとしてinventory。status banner、章/補遺構造、Bio旧同一性表現、source-specificAI/future/strong文言を照合した。MD全行をcurrent primary claimsへ昇格せず、TeXに対応する内容はsource tableをprimary locatorとした。MDの強い旧表現・revision instructionはhistory/provenance候補。Part II revision_notesは元MD非改変、橋渡し追加、自由/停止、宗教・科学、VersionControl/Consensus、AI停止コストを指示する補助資料である。

### 23.6 Appendix subordinate headings (all source locators)


- `intelligence-part2/appendices/appendix_a_master_table.tex`: なし

- `intelligence-part2/appendices/appendix_a_master_table_ja.tex`: VED 基本変数(Master Table v2.1 より再掲・知性層解釈付) / 知性編 Part II 新規導入変数(Master Table v2.2 追加分) / 推論演算子と三層動力学 / 停止演算子と外部参照場 / 閾値移動と応答性 / 三軸相図変数 / 概念的量(量化は後続研究) / (A)/(B) 区別の正式定義 / 変数間の主要な関係式 / $\theta$ の時間スケール比較表

- `intelligence-part2/appendices/appendix_b_homology.tex`: なし

- `intelligence-part2/appendices/appendix_b_homology_ja.tex`: 停止・閉包・アトラクターのホモロジー / 創発構造のホモロジー($\mathcal{U} = \Phi(\mathcal{L}, H_{ij})$) / projection(投影)のホモロジー / $\theta$(拘束パラメータ)のホモロジー / F(状態発展演算子)のホモロジー / 停止構造の歴史的形態ホモロジー / Part I との構造対応表

- `intelligence-part2/appendices/appendix_c_part1_mapping.tex`: Individual Non-Closure / Branching Explosion / Physarum and Transformer / Gettier

- `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex`: Part I × Part II 対応表 / Part I 各章が Part II で受ける継承・拡張・精密化 / Part I への微修正提案リスト / Part I 第8節(個体知性の非閉包)への精密化 / Part I 第9節(知性の差分の地平線)への三層解釈追加 / Part I 第6節(ゲティア問題)への $\mu_\theta$ 補強 / Part I 第5節(Physarum・Transformer)の三層プロファイル再記述 / Part I 微修正の優先順位

- `intelligence-part2/appendices/appendix_d_optional_notes.tex`: Psychological Projection / Science / AI Cost / Freedom

- `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex`: 定理 3.1(非閉包定理 / Non-Closure Theorem) / 系 3.2(内部停止述語の不可能性) / 系 3.3($C_{max}$ 不到達性との同型) / 系 3.4(個体閉包不可能性) / 定義 1.1(VED 的創発)の三例検証 / 主張 5.4($\Phi_{\text{ext}} \equiv \Phi_{\text{net}}$)のスケッチ / 同値命題(誤り許容性 $\Leftrightarrow$ $\mu_\theta$)のスケッチ

- `intelligence-part2/appendices/appendix_e_emergence_homology.tex`: なし

- `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex`: 創発概念の扱いの難しさ / VED 的創発の定義(定義 1.1 の再掲) / VED 内の三例の詳細比較 / Vol.2: 標準模型構造の創発 / Bio-IFGT: 生命の創発 / 知性編 Part II: 創発停止層 $L_E$ / VED 的創発と既存創発概念の比較 / VED 的創発の理論的意義

## 24. Documentary reciprocal cycles

| ID | outbound / return locators | documentary class | non-inference boundary |
|---|---|---|---|
| INT-DCYCLE-001 | P1 §10→futureP2; P2 §0/C→P1 | series continuation | futurechronology≠mutualproof |
| INT-DCYCLE-002 | P2 J C/§13→P1revisionproposal→P2foundation | editorialbackreference | proposal未実装 |
| INT-DCYCLE-003 | P2 J §0/B→CT; CT multiscale/introduction→Intelligence | crossbranchnavigation/homology | CTlocalclaimnotIntvalidation |
| INT-DCYCLE-004 | P1 §1/9,P2 §5→Con; Conformal_mapping/discussion→Intelligence | reciprocalarchitecturecomparison | currentConnonvalidationguard |
| INT-DCYCLE-005 | P1/P2→Bio; Bio§9/discussion→Intelligencefuture | conceptualhandoff | Biosecondattractor未実装 |
| INT-DCYCLE-006 | P2main§1/13→A/B/C/D/E; appendices→main定義/定理 | main/appendixreference | proofsketch存在だけで成立認定しない |
| INT-DCYCLE-007 | branchREADME→main/PDF; sourceentrytreeposition→branchseries | source/navigationcycle | canonicalityはREADMEpolicy以上に拡張しない |
| INT-DCYCLE-008 | rootreading_paths/claim_status→Int; Intintro→VEDtree | navigationcycle | readingorder≠derivationorder |
| INT-DCYCLE-009 | source_md→TeXcurrentauthority; README→source_md移植origin | migration/provenancecycle | historicalMDstrongclaimを逆流させない |

## 25. Authority conflicts / version asymmetries

| ID | source pair / fact | kind | Phase00 handling |
|---|---|---|---|
| INT-AUTHCONFLICT-001 | P1READMEはJAcurrentbuild、ENprimary明示なし | canonical EN authority | EN sourceは保持、canonical断定hold |
| INT-AUTHCONFLICT-002 | P2README JAprimary/ENdraft vs rootEnglishfirstlink | navigation/authority | リンク順でENprimaryへ昇格しない |
| INT-AUTHCONFLICT-003 | P1EN26頁/JA73頁、同じsection数 | translationasymmetry | faithfultranslationauthority未認定 |
| INT-AUTHCONFLICT-004 | P1JAabstract三つの層 vs本文四層 | summary/definition | 認識omissionをinventory |
| INT-AUTHCONFLICT-005 | P2JAabstract空欄/EN本文 | translationcompletion | placeholder保持、修正しない |
| INT-AUTHCONFLICT-006 | P2J§0PartIrecap physical/relational/symbolic/cognitive vsP1perception/recognition/knowledge/intelligence | cross-part attribution | 同じ四層でないdocumentaryfact |
| INT-AUTHCONFLICT-007 | P1logicalindependence vsP2VEDaxiomderivation | inheritancestrength | 源流の違いを後続へ |
| INT-AUTHCONFLICT-008 | P2EN/J P3 fixedregion vsVEDgrounding | formalpremiseversion | 共通定理番号でもpremise同一としない |
| INT-AUTHCONFLICT-009 | P2ENLEdefinition5.1 vsJALR5.1/LE5.2 | definitionnumber | 言語必須locator |
| INT-AUTHCONFLICT-010 | P2JfullclosurePDE vsENshortbasicform | equationcoverage | JAmathをENimplicit前提にしない |
| INT-AUTHCONFLICT-011 | P2D ENOptionalNotes vsJAproofsketches | appendixauthority | 別contentsとして固定 |
| INT-AUTHCONFLICT-012 | P2B JACTcolumn/multitable vsENshorttable | homologycoverage | JA-onlyCTrelations保持 |
| INT-AUTHCONFLICT-013 | P2A JAv2.2/v2.1 vsENgenericvariables | Masterprovenance | exactv2.1未同定 |
| INT-AUTHCONFLICT-014 | P2A tableとbodyΔvintel/vLR等の掲載範囲 | formalobjectcoverage | tableを全objectauthorityと仮定しない |
| INT-AUTHCONFLICT-015 | P1futurePartII vsalreadyexistingP2 | chronology | documentaryissue; no edit |
| INT-AUTHCONFLICT-016 | P2C微修正提案 vscurrentP1 | implementationauthority | 実装済みとしない |
| INT-AUTHCONFLICT-017 | P1nointernalstop vsP2insideindividualexternallydependentLE | stoppingterm/scale | 定義scope差候補、矛盾判定はしない |
| INT-AUTHCONFLICT-018 | P2genericnecessities vsμsapiens追加・sevenclauses残存 | general/specialscope | 必要条件集合を未統合 |
| INT-AUTHCONFLICT-019 | P2EonlyB/μneeded vsPhysarumμfixed/autonomousstop | profile/role | どのE/LE種別か後続へ |
| INT-AUTHCONFLICT-020 | P2§5TransformerownLEなし vsgenericR3LEnecessary | definition/profile | P1axiomprofileとは別集合 |
| INT-AUTHCONFLICT-021 | P2§5stoppingfunctional future vsJAElocalminimum | main/appendixformalstatus | proposition既成事実化を避ける |
| INT-AUTHCONFLICT-022 | P1J§9fourwindowvariables wordingと列挙数 | notation/documentary | 列挙をそのままPhase01へ |
| INT-AUTHCONFLICT-023 | P2root/buildPDF hash差、JA123/122頁 | distributionauthority | 旧build/root別artifact |
| INT-AUTHCONFLICT-024 | P1/P2workingMD旧Bio同一表現 vsTeXguard | historical/current | bannerがTeX優先を明示 |
| INT-AUTHCONFLICT-025 | P1/P2strongsameboundary/grammar/projection vslocalnontypedguards | role/versionstrength | guardは近隣強主張を自動消去しない |
| INT-AUTHCONFLICT-026 | P2refs0/emptyReferences vsnamedtheories/proofclaims | citationprovenance | missinganchor≠false/evidenceverdict |
| INT-AUTHCONFLICT-027 | P2fig1captionunqualifiednostop vsfixedθ(A)note | figure/bodycompression | presentationとformalpremiseを分離 |
| INT-AUTHCONFLICT-028 | P2fig7staircase/evolution vsnotprogressstory | visual/textchronology | 歴史順序proofとしない |

## 26. Glyph / term collision ledger

| ID | glyph / term | different local roles / locators | same object explicitly established? |
|---|---|---|---|
| INT-GLYPH-001 | I | P1accumulationdensity; P2f(1−C); CTtension; IFGTdensity; BioI | NO（共通型の明示なし） |
| INT-GLYPH-002 | C / Cij | P2closure/Cijinteraction; VEDVol1causallogmatrix; IFGTclosure; CTfixation | NO |
| INT-GLYPH-003 | Φ | P1globalconstraint; CTconvolutionpotential; P2Φ(L,H)schema/Φext-net | NO |
| INT-GLYPH-004 | J | P1flow; P2Jjustification; JCclosureflux; CTJI; Bioflow | NO |
| INT-GLYPH-005 | τ | P2internaldevelopment; CTordering; Conwindow; Biotime | UNRESOLVED |
| INT-GLYPH-006 | F | P1update/Ftr; P2inference; BioF(x;θ)vectorfield | NO（localguardあり） |
| INT-GLYPH-007 | E / E(A) | P1graphedges; P2stopoperator; VED2energyfunctional | NO |
| INT-GLYPH-008 | S | P1statespace; P2stoppingpredicateS | NO |
| INT-GLYPH-009 | θ / μ | BioDNA-likeθ; P2region/thresholdmobility; Conwindowparameters | NO |
| INT-GLYPH-010 | H / Cij | P2agent/environmentmutualconstraint; VEDphysicalrelationaldata | UNRESOLVED |
| INT-GLYPH-011 | Φext / Φnet | P2samefield/networkappearanceというsourceexplicitidentity | YES（source主張のみ。typed成立未判定） |
| INT-GLYPH-012 | intelligence | P1lowerbounddynamics; P2general3layers/sapiens; CTsocialnaming; Biosecondattractor | NO |
| INT-GLYPH-013 | landscape | P2C-landscape; CTΦlandscape; Consedimentedterrain | NO |
| INT-GLYPH-014 | attractor / secondattractor | physicalparticle/Biolife/intelligence/P2LE/CTconcept | NO |
| INT-GLYPH-015 | boundary / horizon | VED4DH; P1externalstopping; P2Cmax/Ωθ; CTconceptboundary | UNRESOLVED |
| INT-GLYPH-016 | closure / nonclosure | P1individualstop; P2fixedF/Cmax; VEDphysical; Contemporal; Bioselfmaintenance | NO |
| INT-GLYPH-017 | token / log / memory | CTdiscretetoken; P1knowledge; P2LR/weight/socialblock; VEDcausallog | NO |
| INT-GLYPH-018 | stopping | knowledgefixation/interruption/E/LE/consensus/EOS | NO |
| INT-GLYPH-019 | emergence | P1Φglobal; P2U/LE; Bioattractor; VEDparticle | NO |
| INT-GLYPH-020 | homology / isomorphism | P1axiomcomparison; P2Cmax/nonfixedF/Φext-net/projection | UNRESOLVED |
| INT-GLYPH-021 | layers | P1fourcategories; P2LF/LR/LE; JArep/table; auditI0–I4 | NO |
| INT-GLYPH-022 | projection | IFGTprimitive; Conwindow; P2E-site; psychologicalprojection | NO |

## 27. Preload candidates (not a circularity verdict)

| ID | initial property / locator | later reuse | why retained for later audit |
|---|---|---|---|
| INT-PRELOAD-001 | intelligence=ongoingrevisablemotion P1§2 | motion/revision then characterizesintelligence | localdefinition vs explanation要分離 |
| INT-PRELOAD-002 | knowledge=stopping P1§2 | Gettier mismatch P1§6 | definitionとdiagnostic再使用 |
| INT-PRELOAD-003 | Φglobalirreducible P1§3 | Physarumglobalconstraints support P1§4 | 定義propertyとexternalcomparison |
| INT-PRELOAD-004 | correctness=reusable/connective P1§7 | correctness→branchingexplosion | consequenceの導出前提位置 |
| INT-PRELOAD-005 | stop=completionnotinterruption P1§8 | allobservedendinterruption | criterion独立性を後続inventoryへ |
| INT-PRELOAD-006 | DHI=unreachableinternalstop P1§9 | horizonexplainsneedexternalstop | naming vs explanatory reuse |
| INT-PRELOAD-007 | F=justificationadvancing P2§2–3 | no fixedpoint theorem | source自身が定義時点で排除と述べる；viciousとは判定しない |
| INT-PRELOAD-008 | C=operationalstability P2§1 | GettierconfirmsCnottruth §10 | interpretation/evidence方向 |
| INT-PRELOAD-009 | LE=stableexternallydependentattractor P2§5 | LEexplainsstopping/sustainablefreedom | stabilitypreload候補 |
| INT-PRELOAD-010 | μ=E-site relocation P2§2 | movabilitygeneratesLE §5 | definition/architecture連結 |
| INT-PRELOAD-011 | Φext=functionalreference and Φnet=network P2§5,D | same stopping relation proof | functionalnaming/identityrelation |
| INT-PRELOAD-012 | animism=responsiveinstallation P2§6 | lowcost/universality説明 | socialpropertypreload |
| INT-PRELOAD-013 | God=centralstopping P2§7 | centralizationstability説明 | definition vs causalclaim |
| INT-PRELOAD-014 | religion=maintenance P2§8 | generationcontinuity説明 | historicalindependentcriterion未固定 |
| INT-PRELOAD-015 | socialBC=consensus P2§9 | legitimacy/sync/function説明 | technicalanalogyとの切分け |
| INT-PRELOAD-016 | Σstablebetweenrigid/divergent P2§11 | intelligenceonlynarrowband | regiondefinition vs predictedlimit |
| INT-PRELOAD-017 | homology=sharedroles P2B/E | sharedpatternasgeneralitysupport | table再使用、proof化未判定 |
| INT-PRELOAD-018 | error tolerance/revisability and μ P2§10,D | bidirectionalequivalence | 定義成分と同値主張を分離 |

## 28. Initial uncertainty ledger

| ID | unresolved question | source / continuation boundary |
|---|---|---|
| INT-U-001 | Part I ENをprimarycanonical/authorizedtranslationとする明示記録はあるか | P1README/main; authority |
| INT-U-002 | Part II ENdraftの完成範囲・JAとの差をどう固定するか | P2README/main/appendices |
| INT-U-003 | JAprimarymanuscriptは理論freezeでなくcurrentbuildという理解でよいか | 両README; futureauthority |
| INT-U-004 | P1abstract三層 vs本文四層の意図 | P1JAabstract/§2 |
| INT-U-005 | P2J§0のPartI四層再述が別分類である意図 | P2§0.2/C |
| INT-U-006 | P2JAabstract未移植のversionstatus | P2main_ja |
| INT-U-007 | EN/JAtheoremP3差の採用意図 | P2§3 |
| INT-U-008 | definition5.1/5.2の言語別同定 | P2§5 |
| INT-U-009 | P1axiomindependenceとP2VEDderivationの関係 | P1§3/P2§0 |
| INT-U-010 | exactMasterTablev2.1 artifact/version | P2JA A; CT旧帰属を代用しない |
| INT-U-011 | v2.2のbody全objectcoverage | P2A/§11vLR/Δv |
| INT-U-012 | reusedclosurePDEのexactupstreamrevision | P2JA§1; VED/IFGT |
| INT-U-013 | I=f(1−C)のdomain/range/Cnormalization関係 | P2§1; 正否はPhase01以降 |
| INT-U-014 | F/JC/Jjustification/Φのsignature分離 | P1§4/P2§2–5 |
| INT-U-015 | fixedpointabsenceからarbitrarySへのsource論証範囲 | P2§3,D; Phase03前に判定しない |
| INT-U-016 | Cmax/barrier↔nonclosure/horizonのmap | P2§3,D |
| INT-U-017 | internalindividualstopとexternallydependentinsideLEの語義 | P1§8/P2§5 |
| INT-U-018 | LEemergence式のΦの数学的kind | P2§1,5,E |
| INT-U-019 | LRtraceからrecursivereferenceへのformaldependency | P2§4–5 |
| INT-U-020 | μ/B/E必要性とPhysarumfixedμautonomousstopの関係 | P2§5 |
| INT-U-021 | Transformer3axiomsprofileとownLEabsence/R3necessityの関係 | P1§5/P2§5,12 |
| INT-U-022 | 一般知性条件とsapiens追加条件の条項数 | P2§12 |
| INT-U-023 | stoppingfunctionalfuture vsappendixlocalminのauthority | P2§5,13,E |
| INT-U-024 | Φext≡Φnetのtypedmap/inverse/state-space | P2§5,D |
| INT-U-025 | P1ΦとP2Φnetのrefinementの意味 | P2§5,C |
| INT-U-026 | exactCTversion used in appendixB/tree | P2J§0,B |
| INT-U-027 | CTC-landscapeとCTΦlandscapeの関係 | P2§1–2; CTformal_mapping |
| INT-U-028 | Con投影定義/CPU-GPU/fast-slow/SSO/TCAのexactversion | P1§9/P2§5/B; currentConと歴史引用を分離 |
| INT-U-029 | Conwindow列挙数のdocumentary差 | P1J§9 |
| INT-U-030 | Bioθ/F/Ωlife/ΩintelとIntのtypedtranslation | P2§1–2,B,E |
| INT-U-031 | 生命必要基盤主張と人工substrateの役割 | P1J§9/P1§5 |
| INT-U-032 | historicalMDとcurrentTeX間の全差分の適用履歴 | draft_ja/source_md; 全差分source修正は対象外 |
| INT-U-033 | PartII微修正提案がP1へどこまで実装済みか | P2C/§13; 本taskは実装しない |
| INT-U-034 | AppendixD EN/JA異内容の同期予定 | P2D |
| INT-U-035 | BhomologyJA追加CT列/7tablesのEN移植範囲 | P2B |
| INT-U-036 | source-derivedrootPDF完全freshnessの証拠 | 4rootPDF; timestampだけでは未確定 |
| INT-U-037 | P2buildroot異版の配布copy/provenance | Makefile/build/root PDFs |
| INT-U-038 | SVGとcompiledPNG/PDFの完全同期 | 56assets; pixel同値未認定 |
| INT-U-039 | figurecaption強度とbody限定fixedθ等の関係 | P2fig1/3/4/8 |
| INT-U-040 | historyevolutionstaircaseとnonprogressguardの読み | P2fig7/§7–9 |
| INT-U-041 | P2refs空欄とnamedtheoriesの専用anchors | refs.bib; bib追加禁止 |
| INT-U-042 | P1JA-onlyGibson/uncitedBostrom等のprovenance | P1bib/§2/§8 |
| INT-U-043 | error tolerance↔μθ同値のdefinedproperty/independentcriterion区別 | P2§10,D |
| INT-U-044 | legitimacy非計算可能のformal/社会的意味 | P2§9 |
| INT-U-045 | Σ/速度/解像度/硬度/μの観測対応とparameter範囲 | P2§11; evidence評価前のobjectquestion |
| INT-U-046 | historicalreligion/clinicalattractor/AI claimsのstatus | P2§6–13; truth評価しない |
| INT-U-047 | homology/identity強語とnontypedguardのlocalreach | P1§9/P2B/E/figs |
| INT-U-048 | formal/semantic/social同語再使用preloadの後続役割 | INT-PRELOAD全件; circularity未判定 |

## 29. Phase00 authority handoff

後続監査のprimary materialは、Part I current JA distributed sourceとPart II current primary JA manuscript。EN sourceは言語別に全件保持するが、EN優先は固定しない。EN/JAを同一命題集合とせず、JA-only equations/definitions/proof sketches/CTtable、EN-only Optional Notes等を別authorityで追跡する。source-native theorem/definition番号には必ずPart・言語・ファイルを添える。

root/navigationのcurrent weaker guardはIntelligenceのstrong wordingを修正したことにならない。currentCT/Con/Bioの閉監査・改訂も、歴史的Int引用のexactversion・typedinheritanceを補わない。AppendixAはInt-local辞書として存在するが、v2.1の出典を確定したことにはならない。

Intelligence研究のdata/testを認定していない。code/data NOT LOCATEDはclaimfalseでもevidencesufficiency判定でもない。feedback/documentarycycles/preloadの列挙はcircularity判定ではない。

## 30. Validation / immutable baseline

task-start snapshot: 1489 regular files、SHA-256、.git除外・ignored filesを含む。監査用一時manifest: ${TEMP_EVIDENCE_ROOT}/int_phase00.YBkrdv/baseline.json。
既存dirty worktree: 249 status lines（M 241 / ?? 8）。CT等の先行変更はユーザーの既存状態として保持し、本監査の変更と混同しない。

- main entry 4、本文included content 22+28=50 files、P2preamble2、appendix10 filesの存在・inputを確認。
- P1 §1–10 + abstract、P2 §0–13 + entryabstract、appendixA–Eを言語別にinventory。
- figure14families/28variants/56assets、caption、editableSVG、compiledformatを確認。
- 全primaryclaim/definition/homology/negative/dependency IDsを個別ledger化。
- bibliography13+0、cited keys E/J=12/13,0/0、rootPDF26/73/30/123頁、旧buildPDFを分離。
- 科学code/simulation/dataとMakefile/TeX/fontcacheを区別。実行はhash/metadata/text抽出/一時PDFrenderだけ。
- PDF skillの指示に従い配布PDFの抽出だけでなくfirst/lastと図assetのvisual inventoryを実施。全頁quality certificationではない。
- 外部研究、web、build、simulation、source/式/図/PDF/Bib変更、theory/bridge導入、commit/pushなし。
- 最終hash差分・ID検査・git diff --check結果は末尾のvalidation resultに記録する。


### Summary counts (family単位)

| Ledger | Count |
|---|---:|
| INT-FIG | 14 |
| INT-OBJ | 32 |
| INT-EQF-DRAFT | 35 |
| INT-CLM | 95 |
| INT-DEF | 32 |
| INT-IDEF | 10 |
| INT-STRONG | 62 |
| INT-NEG | 24 |
| INT-CTDEP | 6 |
| INT-CONDEP | 10 |
| INT-BIODEP | 12 |
| INT-UPSTREAM | 14 |
| INT-P1P2 | 12 |
| INT-HOMO | 21 |
| INT-EMERG | 14 |
| INT-LOG | 15 |
| INT-AI | 9 |
| INT-SOC | 15 |
| INT-PRED-DRAFT | 20 |
| INT-DCYCLE | 9 |
| INT-AUTHCONFLICT | 28 |
| INT-GLYPH | 22 |
| INT-PRELOAD | 18 |
| INT-U | 48 |

Figure14はunique論点family、languagevariants28、physicalassets56。dependency ledgerは相互に重なりうるcrosswalkであり、独立evidence件数ではない。draftprediction20にはsource example・editorialfutureも含み、testedprediction件数として使用しない。

### Final validation result

開始時1489filesのSHA-256は全件一致、変更/削除0。新規は本記録とIntelligence audit READMEの2filesのみ。旧Phase00–07/CT implementation recordsを含め既存監査記録、全source、式、figure、PDF、BibTeX、JAは不変。

ID ledgerの重複0、数値IDは各prefixで001から連続。INT-CLM95/95、INT-DEF32/32、INT-U48/48を確認。INT1-S00–S10、INT2-S00–S13を別に確認。claim/definitionのlanguage-qualified locatorとsection mapを対応させた。frozen dispositionは付与していない。

git diff --check: PASS (exit 0)。新規untracked2filesはgit diff --no-index --checkでも別途検査（Markdown statusの末尾空白を除去後PASS）。
git status --short: 開始時249行をすべて保持、終了時250行。追加は `?? notes/intelligence_audit/` の1行（内訳2files）。既存M241/??8を今回変更と報告しない。commit/pushなし。

## 31. Stop boundary

Phase00 COMPLETEで停止する。Phase01 equation / symbol / object inventory、数学的正しさ、循環性、evidence burden判定、disposition、source/equation/distribution revisionへ進まない。

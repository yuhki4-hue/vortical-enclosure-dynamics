# Intelligence Phase01 — equation / symbol / object / signature inventory v0.1

## 0. Status

```text
Intelligence audit: IN PROGRESS
Phase00: COMPLETE
Phase01: COMPLETE
Phase02–07: NOT STARTED
Claim truth / mathematical correctness / proof validity: NOT AUDITED
Circularity / evidence sufficiency: NOT AUDITED
Final dispositions: NOT ASSIGNED
Source / equation / distribution revision: NOT STARTED
```

## 1. Authority inheritance / extraction boundary

最上位authorityは[Phase00](00_dependency_inheritance_and_authority_record_v0.1_ja.md)と[README](README_ja.md)。Part I JAはcurrent distributed build authority、ENはcurrent parallel source（primary unresolved）。Part II JAはprimary manuscript、ENはworking draft。補遺は言語別APPENDIX AUTHORITY。MD/PDF/figuresは本文のauthorityを上書きしない。

P1E/P1J/P2E/P2J/P2AE/P2AJを分離して抽出した。main4、preamble2、本文/abstract50、補遺10の計66 TeX filesをentryのinput順に走査。コメントを位置保存して除外し、\\[...\\]、$$...$$、equation/align/gather/multline/displaymath/eqnarray/alignat（star含む）を検出。inlineは$...$および\\(...\\)。図caption・table内のinlineも含む。SVG/PNGの図内数学は別figure ledgerとしTeX occurrence数へ混入しない。raw expressionはsourceのdelimiter込みで保存、lineはtask-start fileの1-based位置。

same glyph ≠ same object、same equation form ≠ same signature、same Φ/F/J/C/E/θ ≠ same object、homology ≠ typed map。sourceのtheorem/proof sketch/同型という語をinventoryするだけでvalidityを判定しない。CONFLICTINGは**signatureの複数契約が競合する候補**であり、形式的不可能性の判定ではない。提案・否定・反証仮定内の数式も記録するが、採用された前提と取り違えない。

### 1.1 Phase00への補足（旧記録を変更しない）

- Phase00 display集計は主に\\[を数えた簡易値だった。今回は$$内のP1JA 2blocks、P2JA/appendix 6blocksも抽出し、合計98。source追加ではなくdelimiter coverageの補足。
- Phase00のΣ/phase-region groupingを分解する。P2 JA §1:325、A:133、§13:90–91のΣは「創発停止層発達度・活性度」、量化はfuture。三軸相図の領域集合としてΣを定義したsourceは未確認。
- P2JA P3には「VED接地」という見出しだけでなく、fixed θ / movement(A) / (B)除外も明記される。ENのfixed-region premiseと共有する部分と、JA追加のupstream対応を分ける。
- P1JのF_bio離散update、P2のset-valued F、C=truthという**否定対象のdisplay**、causal-vector sums等を補足。旧35familiesを無条件に最終数へ固定しない。

## 2. Display occurrence inventory

環境は各raw blockに保存。全98にequation labelは未検出（近隣figure labelとは別）。同family内反復は以下のEQF crosswalkで列挙し、rawの語順・text annotation・delimiter差は消さない。各displayのsignature/unit/dependencyは参照EQF行に付属する。

| Stream | Authority | Occurrences |
|---|---|---:|
| P1E | parallel EN / primary unresolved | 15 |
| P1J | current distributed build authority | 17 |
| P2E | working EN main | 26 |
| P2J | primary JA main | 31 |
| P2AE | EN draft appendix | 2 |
| P2AJ | JA primary appendix | 7 |


### INT-MATH-P1E-001

Source: `intelligence-part1/sections/03_minimal_axioms_of_intelligence.tex:16–18` / P1E。Context: Axiom I: Connected state space。Family: INT-EQF-043。Label: NONE。source-local relation / annotation。

```tex
\[
\mathcal{S}=\{s_1,s_2,\dots\}.
\]
```

### INT-MATH-P1E-002

Source: `intelligence-part1/sections/03_minimal_axioms_of_intelligence.tex:26–28` / P1E。Context: Axiom II: Temporal ordering。Family: INT-EQF-001。Label: NONE。source-local relation / annotation。

```tex
\[
s(t+1)=F(s(t)).
\]
```

### INT-MATH-P1E-003

Source: `intelligence-part1/sections/03_minimal_axioms_of_intelligence.tex:38–40` / P1E。Context: Axiom III: Global constraint $\Phi$。Family: INT-EQF-002。Label: NONE。source-local relation / annotation。

```tex
\[
\Phi:\mathcal{S}\rightarrow\mathbb{R}.
\]
```

### INT-MATH-P1E-004

Source: `intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex:42–44` / P1E。Context: Lexical correspondence with the Physarum solver。Family: INT-EQF-005。Label: NONE。source-local relation / annotation。

```tex
\[
Q_{ij}=\frac{D_{ij}}{L_{ij}}\Delta p_{ij},
\]
```

### INT-MATH-P1E-005

Source: `intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex:46–48` / P1E。Context: Lexical correspondence with the Physarum solver。Family: INT-EQF-006。Label: NONE。source-local relation / annotation。

```tex
\[
\frac{dD_{ij}}{dt}=f(|Q_{ij}|)-D_{ij}.
\]
```

### INT-MATH-P1E-006

Source: `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex:20–22` / P1E。Context: The slime mold as an externally validated instantiation。Family: INT-EQF-006。Label: NONE。source-local relation / annotation。

```tex
\[
\frac{dD_{ij}}{dt}=f(|Q_{ij}|)-D_{ij}.
\]
```

### INT-MATH-P1E-007

Source: `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex:34–36` / P1E。Context: The Transformer as an artificial instantiation。Family: INT-EQF-008。Label: NONE。source-local relation / annotation。

```tex
\[
\mathcal{S}=\{h_i^{(\ell)}\}.
\]
```

### INT-MATH-P1E-008

Source: `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex:41–43` / P1E。Context: The Transformer as an artificial instantiation。Family: INT-EQF-009。Label: NONE。source-local relation / annotation。

```tex
\[
h^{(\ell+1)}=F_{\mathrm{tr}}\!\left(h^{(\ell)}\right).
\]
```

### INT-MATH-P1E-009

Source: `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex:48–50` / P1E。Context: The Transformer as an artificial instantiation。Family: INT-EQF-004。Label: NONE。source-local relation / annotation。

```tex
\[
\Phi_{\mathrm{tr}}:\mathcal{S}\rightarrow\mathbb{R}.
\]
```

### INT-MATH-P1E-010

Source: `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex:18–20` / P1E。Context: Why correctness increases connectivity。Family: INT-EQF-010。Label: NONE。source-local relation / annotation。

```tex
\[
I(s)\uparrow.
\]
```

### INT-MATH-P1E-011

Source: `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex:22–24` / P1E。Context: Why correctness increases connectivity。Family: INT-EQF-011。Label: NONE。source-local relation / annotation。

```tex
\[
\nabla\cdot J \uparrow.
\]
```

### INT-MATH-P1E-012

Source: `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex:35–37` / P1E。Context: Why correctness contains no stopping condition。Family: INT-EQF-012。Label: NONE。source-local relation / annotation。

```tex
\[
\mathrm{correctness}(p)\Rightarrow \nabla\cdot J|_p\neq 0.
\]
```

### INT-MATH-P1E-013

Source: `intelligence-part1/sections/08_the_non_closure_of_individual_intelligence.tex:14–16` / P1E。Context: The stopping operator problem。Family: INT-EQF-044。Label: NONE。source-local relation / annotation。

```tex
\[
\mathcal{T}\notin \mathrm{Internal}(\mathcal{R}).
\]
```

### INT-MATH-P1E-014

Source: `intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex:12–14` / P1E。Context: The structural necessity of crossing。Family: INT-EQF-044。Label: NONE。source-local relation / annotation。

```tex
\[
\mathcal{T}\notin \mathrm{Internal}(\mathcal{R}).
\]
```

### INT-MATH-P1E-015

Source: `intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex:16–18` / P1E。Context: The structural necessity of crossing。Family: INT-EQF-016。Label: NONE。source-local relation / annotation。

```tex
\[
\mathcal{T}\in \mathrm{External}(\mathcal{R}).
\]
```

### INT-MATH-P1J-001

Source: `intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex:20–22` / P1J。Context: Axiom I: Connected state space。Family: INT-EQF-043。Label: NONE。source-local relation / annotation。

```tex
\[
\mathcal{S} = \{ s_1, s_2, \dots \}
\]
```

### INT-MATH-P1J-002

Source: `intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex:45–47` / P1J。Context: Axiom II: Temporal ordering。Family: INT-EQF-001。Label: NONE。source-local relation / annotation。

```tex
\[
s(t+1) = F(s(t))
\]
```

### INT-MATH-P1J-003

Source: `intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex:76–78` / P1J。Context: Axiom III: Global constraint $\Phi$。Family: INT-EQF-002。Label: NONE。source-local relation / annotation。

```tex
\[
\Phi : \mathcal{S} \rightarrow \mathbb{R}.
\]
```

### INT-MATH-P1J-004

Source: `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:118–120` / P1J。Context: The Physarum solver model。Family: INT-EQF-005。Label: NONE。source-local relation / annotation。

```tex
\[
Q_{ij} = \frac{D_{ij}}{L_{ij}} \Delta p_{ij}
\]
```

### INT-MATH-P1J-005

Source: `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:126–128` / P1J。Context: The Physarum solver model。Family: INT-EQF-006。Label: NONE。source-local relation / annotation。

```tex
\[
\frac{dD_{ij}}{dt} = f(|Q_{ij}|) - D_{ij}
\]
```

### INT-MATH-P1J-006

Source: `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:42–44` / P1J。Context: Mapping to the three axioms。Family: INT-EQF-006。Label: NONE。source-local relation / annotation。

```tex
\[
\frac{dD_{ij}}{dt} = f(|Q_{ij}|) - D_{ij}
\]
```

### INT-MATH-P1J-007

Source: `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:51–53` / P1J。Context: Mapping to the three axioms。Family: INT-EQF-003。Label: NONE。source-local relation / annotation。

```tex
\[
\Phi_\text{bio} : \mathcal{S} \to \mathbb{R}
\]
```

### INT-MATH-P1J-008

Source: `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:94–96` / P1J。Context: Mapping to the three axioms。Family: INT-EQF-008。Label: NONE。source-local relation / annotation。

```tex
\[
\mathcal{S} = \{ h^{(\ell)}_i \}
\]
```

### INT-MATH-P1J-009

Source: `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:103–105` / P1J。Context: Mapping to the three axioms。Family: INT-EQF-009。Label: NONE。source-local relation / annotation。

```tex
\[
h^{(\ell+1)} = F_\text{tr}\!\left( h^{(\ell)} \right)
\]
```

### INT-MATH-P1J-010

Source: `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:112–114` / P1J。Context: Mapping to the three axioms。Family: INT-EQF-004。Label: NONE。source-local relation / annotation。

```tex
\[
\Phi_\text{tr} : \mathcal{S} \to \mathbb{R}
\]
```

### INT-MATH-P1J-011

Source: `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:46–48` / P1J。Context: Formalization in IFGT vocabulary。Family: INT-EQF-010。Label: NONE。source-local relation / annotation。

```tex
\[
I(s) \uparrow \quad \text{(局所的情報密度の増大)}
\]
```

### INT-MATH-P1J-012

Source: `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:52–54` / P1J。Context: Formalization in IFGT vocabulary。Family: INT-EQF-011。Label: NONE。source-local relation / annotation。

```tex
\[
\nabla \cdot J \uparrow \quad \text{(局所的な情報流の分岐)}
\]
```

### INT-MATH-P1J-013

Source: `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:87–89` / P1J。Context: The self-generating nature of inference。Family: INT-EQF-012。Label: NONE。source-local relation / annotation。

```tex
\[
\text{正しさ}(p) \implies \nabla \cdot J|_p \neq 0
\]
```

### INT-MATH-P1J-014

Source: `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:104–106` / P1J。Context: The structural chain。Family: INT-EQF-013。Label: NONE。source-local relation / annotation。

```tex
\[
I(s_i) \uparrow \quad \text{for } i = 1, 2, 3, \dots
\]
```

### INT-MATH-P1J-015

Source: `intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex:189–191` / P1J。Context: The structural absence。Family: INT-EQF-044。Label: NONE。source-local relation / annotation。

```tex
$$
\mathcal{T} \notin \text{Internal}(\mathcal{R})
$$
```

### INT-MATH-P1J-016

Source: `intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex:23–23` / P1J。Context: Deriving the boundary from the absence。Family: INT-EQF-044。Label: NONE。source-local relation / annotation。

```tex
$$\mathcal{T} \notin \text{Internal}(\mathcal{R})$$
```

### INT-MATH-P1J-017

Source: `intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex:28–30` / P1J。Context: Deriving the boundary from the absence。Family: INT-EQF-016。Label: NONE。source-local relation / annotation。

```tex
\[
\mathcal{T} \in \text{External}(\mathcal{R})
\]
```

### INT-MATH-P2E-001

Source: `intelligence-part2/sections/00_introduction.tex:9–11` / P2E。Context: Introduction: Why Intelligence Requires Stopping。Family: INT-EQF-050。Label: NONE。source-local relation / annotation。

```tex
\[
L_F \;\longrightarrow\; L_R \;\longrightarrow\; L_E .
\]
```

### INT-MATH-P2E-002

Source: `intelligence-part2/sections/01_preliminaries.tex:23–25` / P2E。Context: VED Basic Form。Family: INT-EQF-051。Label: NONE。source-local relation / annotation。

```tex
\[
\text{difference} \;\longrightarrow\; F(L_F) \;\longrightarrow\; \text{non-closure} \;\longrightarrow\; \text{externalized stopping}.
\]
```

### INT-MATH-P2E-003

Source: `intelligence-part2/sections/01_preliminaries.tex:28–30` / P2E。Context: VED Basic Form。Family: INT-EQF-019。Label: NONE。source-local relation / annotation。

```tex
\[
I = f(1-C).
\]
```

### INT-MATH-P2E-004

Source: `intelligence-part2/sections/01_preliminaries.tex:46–48` / P2E。Context: Emergence。Family: INT-EQF-031。Label: NONE。source-local relation / annotation。

```tex
\[
U = \Phi(L,H_{ij}),
\]
```

### INT-MATH-P2E-005

Source: `intelligence-part2/sections/01_preliminaries.tex:52–54` / P2E。Context: Emergence。Family: INT-EQF-032。Label: NONE。source-local relation / annotation。

```tex
\[
L_E = \Phi(L_R,H_{ij}).
\]
```

### INT-MATH-P2E-006

Source: `intelligence-part2/sections/02_inference_operator.tex:9–11` / P2E。Context: Definition。Family: INT-EQF-025。Label: NONE。source-local relation / annotation。

```tex
\[
x_{n+1}=F(x_n),
\]
```

### INT-MATH-P2E-007

Source: `intelligence-part2/sections/02_inference_operator.tex:15–17` / P2E。Context: Definition。Family: INT-EQF-047。Label: NONE。source-local relation / annotation。

```tex
\[
J:\mathcal{X}\to\mathbb{R}
\]
```

### INT-MATH-P2E-008

Source: `intelligence-part2/sections/02_inference_operator.tex:19–21` / P2E。Context: Definition。Family: INT-EQF-026。Label: NONE。source-local relation / annotation。

```tex
\[
J(F(x))>J(x).
\]
```

### INT-MATH-P2E-009

Source: `intelligence-part2/sections/02_inference_operator.tex:33–35` / P2E。Context: Branching。Family: INT-EQF-048。Label: NONE。source-local relation / annotation。

```tex
\[
F(x_n)=\{x_{n+1}^{(1)},x_{n+1}^{(2)},\ldots\}
\]
```

### INT-MATH-P2E-010

Source: `intelligence-part2/sections/02_inference_operator.tex:43–45` / P2E。Context: Internal Stopping Predicate。Family: INT-EQF-028。Label: NONE。source-local relation / annotation。

```tex
\[
S(x)=1 \quad \text{if inference should stop at } x.
\]
```

### INT-MATH-P2E-011

Source: `intelligence-part2/sections/03_nonclosure_theorem.tex:21–23` / P2E。Context: Assumptions。Family: INT-EQF-026。Label: NONE。source-local relation / annotation。

```tex
\[
J(F(x))>J(x)
\]
```

### INT-MATH-P2E-012

Source: `intelligence-part2/sections/03_nonclosure_theorem.tex:32–34` / P2E。Context: Theorem。Family: INT-EQF-027。Label: NONE。不動点条件を否定するtheoremの内包式。

```tex
\[
F(x^*)=x^*.
\]
```

### INT-MATH-P2E-013

Source: `intelligence-part2/sections/03_nonclosure_theorem.tex:36–38` / P2E。Context: Theorem。Family: INT-EQF-027。Label: NONE。source-local relation / annotation。

```tex
\[
\forall x\in\mathcal{X},\quad F(x)\neq x
\]
```

### INT-MATH-P2E-014

Source: `intelligence-part2/sections/03_nonclosure_theorem.tex:44–46` / P2E。Context: Proof Sketch。Family: INT-EQF-027。Label: NONE。反証仮定下のproof-step；sourceが矛盾標的として使用。

```tex
\[
J(F(x^*))>J(x^*).
\]
```

### INT-MATH-P2E-015

Source: `intelligence-part2/sections/03_nonclosure_theorem.tex:48–50` / P2E。Context: Proof Sketch。Family: INT-EQF-027。Label: NONE。反証仮定下のproof-step；sourceが矛盾標的として使用。

```tex
\[
J(x^*)>J(x^*),
\]
```

### INT-MATH-P2E-016

Source: `intelligence-part2/sections/05_emergent_stopping_layer.tex:38–40` / P2E。Context: Definition of $L_E$。Family: INT-EQF-032。Label: NONE。source-local relation / annotation。

```tex
\[
L_E=\Phi(L_R\text{ motion},H_{ij}).
\]
```

### INT-MATH-P2E-017

Source: `intelligence-part2/sections/05_emergent_stopping_layer.tex:72–74` / P2E。Context: Emergence Mechanism。Family: INT-EQF-054。Label: NONE。source-local relation / annotation。

```tex
\[
\mu_\theta \to (B)\text{ reconfiguration} \to E\text{-region projection} \to L_R\text{ convergence} \to L_E .
\]
```

### INT-MATH-P2E-018

Source: `intelligence-part2/sections/05_emergent_stopping_layer.tex:85–87` / P2E。Context: External Stopping Operator。Family: INT-EQF-033。Label: NONE。source-local relation / annotation。

```tex
\[
E=E[L_E,x_n],\qquad E\notin\{F^k\}.
\]
```

### INT-MATH-P2E-019

Source: `intelligence-part2/sections/05_emergent_stopping_layer.tex:93–95` / P2E。Context: $\Phi_{\text{ext}}\equiv\Phi_{\text{net}}$。Family: INT-EQF-034。Label: NONE。source-local relation / annotation。

```tex
\[
\Phi_{\text{ext}}\equiv\Phi_{\text{net}}.
\]
```

### INT-MATH-P2E-020

Source: `intelligence-part2/sections/06_animism.tex:11–13` / P2E。Context: Animism: Installation of Stopping in the Environment。Family: INT-EQF-055。Label: NONE。source-local relation / annotation。

```tex
\[
\text{environmental locus} \;\mapsto\; E\text{-installation site}.
\]
```

### INT-MATH-P2E-021

Source: `intelligence-part2/sections/07_god.tex:15–17` / P2E。Context: God: Compression of Distributed Stopping。Family: INT-EQF-056。Label: NONE。source-local relation / annotation。

```tex
\[
\text{distributed stopping} \;\longrightarrow\; \text{centralized stopping}.
\]
```

### INT-MATH-P2E-022

Source: `intelligence-part2/sections/08_religion.tex:13–15` / P2E。Context: Religion: Long-Term Maintenance of Stopping Structures。Family: INT-EQF-057。Label: NONE。source-local relation / annotation。

```tex
\[
\text{centralized stopping} \;\longrightarrow\; \text{maintained stopping}.
\]
```

### INT-MATH-P2E-023

Source: `intelligence-part2/sections/10_gettier_problem.tex:17–19` / P2E。Context: $C$ as Stability Measure。Family: INT-EQF-049。Label: NONE。source-local relation / annotation。

```tex
\[
C = \text{degree of operational closure/stability},
\]
```

### INT-MATH-P2E-024

Source: `intelligence-part2/sections/10_gettier_problem.tex:21–23` / P2E。Context: $C$ as Stability Measure。Family: INT-EQF-049。Label: NONE。**否定される同定**（直前not）；採用式ではない。

```tex
\[
C = \text{truth}.
\]
```

### INT-MATH-P2E-025

Source: `intelligence-part2/sections/11_instability_region.tex:18–20` / P2E。Context: Three Axes。Family: INT-EQF-038。Label: NONE。source-local relation / annotation。

```tex
\[
\Delta v_{\text{intel}} = v_{\text{inf}} - v_{LR}
\]
```

### INT-MATH-P2E-026

Source: `intelligence-part2/sections/12_constructive_clauses.tex:29–31` / P2E。Context: Clause 6: Social Stopping Is Networked。Family: INT-EQF-034。Label: NONE。source-local relation / annotation。

```tex
\[
\Phi_{\text{ext}}\equiv\Phi_{\text{net}}.
\]
```

### INT-MATH-P2AE-001

Source: `intelligence-part2/appendices/appendix_b_homology.tex:6–12` / P2AE。Context: Cross-Domain Homology。Family: INT-EQF-062。Label: NONE。source-local relation / annotation。

```tex
\[
\text{incomplete closure}
\;\longrightarrow\;
\text{emergent attractor}
\;\longrightarrow\;
\text{sustainable dynamics}.
\]
```

### INT-MATH-P2AE-002

Source: `intelligence-part2/appendices/appendix_e_emergence_homology.tex:5–7` / P2AE。Context: Emergence Homology。Family: INT-EQF-031。Label: NONE。source-local relation / annotation。

```tex
\[
U=\Phi(L,H_{ij}).
\]
```

### INT-MATH-P2J-001

Source: `intelligence-part2/sections/00_introduction_ja.tex:27–29` / P2J。Context: 本論文の課題。Family: INT-EQF-051。Label: NONE。source-local relation / annotation。

```tex
\[
\text{差がある} \;\longrightarrow\; F(L_F) \;\longrightarrow\; \text{内部不動点不在} \;\longrightarrow\; \text{無限後退}
\]
```

### INT-MATH-P2J-002

Source: `intelligence-part2/sections/00_introduction_ja.tex:31–33` / P2J。Context: 本論文の課題。Family: INT-EQF-051。Label: NONE。source-local relation / annotation。

```tex
\[
\longrightarrow\; E(\text{外部停止演算子})\text{の必然性} \;\longrightarrow\; \Phi_{\text{ext}}\text{の歴史的諸形態}
\]
```

### INT-MATH-P2J-003

Source: `intelligence-part2/sections/00_introduction_ja.tex:37–39` / P2J。Context: 本論文の課題。Family: INT-EQF-052。Label: NONE。source-local relation / annotation。

```tex
\[
H_{ij}\text{パラメータ} \;\longrightarrow\; \text{応答性閾値} \;\longrightarrow\; \mu_\theta(\text{閾値移動能力})
\]
```

### INT-MATH-P2J-004

Source: `intelligence-part2/sections/00_introduction_ja.tex:41–43` / P2J。Context: 本論文の課題。Family: INT-EQF-052。Label: NONE。source-local relation / annotation。

```tex
\[
\longrightarrow\; \text{持続可能な因果推論運用} \;\longrightarrow\; \text{サピエンス的知性}
\]
```

### INT-MATH-P2J-005

Source: `intelligence-part2/sections/00_introduction_ja.tex:47–49` / P2J。Context: 本論文の課題。Family: INT-EQF-050。Label: NONE。source-local relation / annotation。

```tex
\[
L_F \;\longrightarrow\; L_R(\text{ログ・再帰運動}) \;\longrightarrow\; L_E(\text{創発停止層})
\]
```

### INT-MATH-P2J-006

Source: `intelligence-part2/sections/00_introduction_ja.tex:51–53` / P2J。Context: 本論文の課題。Family: INT-EQF-053。Label: NONE。source-local relation / annotation。

```tex
\[
\longrightarrow\; \Phi_{\text{net}}(L_E\text{ネットワーク}) \;\longrightarrow\; \text{外部依存型停止を持つ動力学的存在}
\]
```

### INT-MATH-P2J-007

Source: `intelligence-part2/sections/01_preliminaries_ja.tex:47–49` / P2J。Context: VED 基本式の知性層への再定式化。Family: INT-EQF-017。Label: NONE。source-local relation / annotation。

```tex
\[
\frac{\partial C}{\partial \tau} + \nabla \cdot J_C = a\Delta\left(1 - \frac{C}{C_*}\right) - \Gamma C - \frac{\kappa_B}{C_{max} - C}
\]
```

### INT-MATH-P2J-008

Source: `intelligence-part2/sections/01_preliminaries_ja.tex:76–78` / P2J。Context: 情報場と情報力。Family: INT-EQF-019。Label: NONE。source-local relation / annotation。

```tex
\[
I = f(1 - C)
\]
```

### INT-MATH-P2J-009

Source: `intelligence-part2/sections/01_preliminaries_ja.tex:86–88` / P2J。Context: 情報場と情報力。Family: INT-EQF-022。Label: NONE。source-local relation / annotation。

```tex
\[
F_I = \alpha \nabla C
\]
```

### INT-MATH-P2J-010

Source: `intelligence-part2/sections/01_preliminaries_ja.tex:162–164` / P2J。Context: C-landscape と推論軌道。Family: INT-EQF-025。Label: NONE。source-local relation / annotation。

```tex
\[
x_0 \xrightarrow{F} x_1 \xrightarrow{F} x_2 \xrightarrow{F} \cdots
\]
```

### INT-MATH-P2J-011

Source: `intelligence-part2/sections/01_preliminaries_ja.tex:214–216` / P2J。Context: 創発の VED 内定義。Family: INT-EQF-031。Label: NONE。source-local relation / annotation。

```tex
$$
\mathcal{U} = \Phi(\mathcal{L}\text{の運動}, \; H_{ij})
$$
```

### INT-MATH-P2J-012

Source: `intelligence-part2/sections/01_preliminaries_ja.tex:283–285` / P2J。Context: 三層動力学の予告。Family: INT-EQF-050。Label: NONE。source-local relation / annotation。

```tex
\[
L_F \xrightarrow{\text{運動の痕跡}} L_R \xrightarrow{\;\Phi(\cdot, H_{ij})\;} L_E
\]
```

### INT-MATH-P2J-013

Source: `intelligence-part2/sections/02_inference_operator_ja.tex:15–17` / P2J。Context: 推論演算子 $F$ の定義。Family: INT-EQF-025。Label: NONE。source-local relation / annotation。

```tex
\[
x_{n+1} = F(x_n)
\]
```

### INT-MATH-P2J-014

Source: `intelligence-part2/sections/02_inference_operator_ja.tex:23–25` / P2J。Context: 推論演算子 $F$ の定義。Family: INT-EQF-046。Label: NONE。source-local relation / annotation。

```tex
\[
\frac{dx}{dt} = F(x;\theta)
\]
```

### INT-MATH-P2J-015

Source: `intelligence-part2/sections/02_inference_operator_ja.tex:100–102` / P2J。Context: 相互拘束 $H_{ij}$ と推論環境。Family: INT-EQF-029。Label: NONE。source-local relation / annotation。

```tex
\[
C_{ij} = 1 - \exp(-\lambda \rho_i H_{ij})
\]
```

### INT-MATH-P2J-016

Source: `intelligence-part2/sections/02_inference_operator_ja.tex:203–205` / P2J。Context: 開放窓としての $\mu_\theta$ — 第5節への橋渡し。Family: INT-EQF-050。Label: NONE。source-local relation / annotation。

```tex
\[
L_F \xrightarrow{\;\text{運動の痕跡}\;} L_R \xrightarrow{\;\mu_\theta \text{による開放}\;} L_E
\]
```

### INT-MATH-P2J-017

Source: `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:28–30` / P2J。Context: 推論演算子の前提と正当化測度。Family: INT-EQF-025。Label: NONE。source-local relation / annotation。

```tex
\[
x_{n+1} = F(x_n)
\]
```

### INT-MATH-P2J-018

Source: `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:37–39` / P2J。Context: 推論演算子の前提と正当化測度。Family: INT-EQF-026。Label: NONE。source-local relation / annotation。

```tex
\[
J(F(x)) > J(x)
\]
```

### INT-MATH-P2J-019

Source: `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:59–61` / P2J。Context: 主定理 — 内部不動点の不在。Family: INT-EQF-027。Label: NONE。source-local relation / annotation。

```tex
$$
\forall x \in \mathcal{X}, \quad F(x) \neq x
$$
```

### INT-MATH-P2J-020

Source: `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:79–81` / P2J。Context: 証明スケッチ。Family: INT-EQF-026。Label: NONE。source-local relation / annotation。

```tex
\[
J(F(x)) > J(x)
\]
```

### INT-MATH-P2J-021

Source: `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:85–87` / P2J。Context: 証明スケッチ。Family: INT-EQF-027。Label: NONE。反証仮定下のproof-step；sourceが矛盾標的として使用。

```tex
\[
J(F(x^*)) > J(x^*)
\]
```

### INT-MATH-P2J-022

Source: `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:91–93` / P2J。Context: 証明スケッチ。Family: INT-EQF-027。Label: NONE。反証仮定下のproof-step；sourceが矛盾標的として使用。

```tex
\[
J(x^*) > J(x^*)
\]
```

### INT-MATH-P2J-023

Source: `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:149–151` / P2J。Context: VED対応 — $C_{max}$ 境界との同型。Family: INT-EQF-017。Label: NONE。source-local relation / annotation。

```tex
\[
\frac{\partial C}{\partial \tau} + \nabla \cdot J_C = a\Delta\left(1 - \frac{C}{C_*}\right) - \Gamma C - \frac{\kappa_B}{C_{max} - C}
\]
```

### INT-MATH-P2J-024

Source: `intelligence-part2/sections/04_response_channels_ja.tex:127–129` / P2J。Context: 次章への橋渡し。Family: INT-EQF-050。Label: NONE。source-local relation / annotation。

```tex
\[
L_F \text{の非閉包(§3)} \;\longrightarrow\; \text{沈黙世界での無限後退(§4.4)} \;\longrightarrow\; \text{ログの堆積} \;\longrightarrow\; L_R \text{の予兆(§4.6)}
\]
```

### INT-MATH-P2J-025

Source: `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:82–84` / P2J。Context: 創発停止層 $L_E$ の定義。Family: INT-EQF-032。Label: NONE。source-local relation / annotation。

```tex
$$
L_E = \Phi(L_R \text{の運動}, \; H_{ij})
$$
```

### INT-MATH-P2J-026

Source: `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:223–225` / P2J。Context: 創発機構 — 領域組み替えと停止演算子設置領域の投影。Family: INT-EQF-054。Label: NONE。source-local relation / annotation。

```tex
\[
\mu_\theta \;\xrightarrow{\text{起こす}}\; (B)\text{組み替え} \;\xrightarrow{H_{ij}\text{に沿って}}\; E\text{設置領域の投影} \;\xrightarrow{L_R\text{収束}}\; L_E
\]
```

### INT-MATH-P2J-027

Source: `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:260–262` / P2J。Context: 外部停止演算子 $E$ の構造。Family: INT-EQF-033。Label: NONE。source-local relation / annotation。

```tex
$$
E = E[L_E, x_n], \qquad E \notin \{F^k\}
$$
```

### INT-MATH-P2J-028

Source: `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:287–289` / P2J。Context: $\Phi_{\text{ext}} \equiv \Phi_{\text{net}}$ — 外部参照場と $L_E$ ネットワークの同型。Family: INT-EQF-034。Label: NONE。source-local relation / annotation。

```tex
$$
\Phi_{\text{ext}} \equiv \Phi_{\text{net}}
$$
```

### INT-MATH-P2J-029

Source: `intelligence-part2/sections/07_god_ja.tex:21–23` / P2J。Context: 神は説明的実体ではない。Family: INT-EQF-058。Label: NONE。source-local relation / annotation。

```tex
\[
\text{神} \neq \text{因果完結}, \qquad \text{神} \neq \text{真理保証機構}, \qquad \text{神} \neq \text{説明的実体}
\]
```

### INT-MATH-P2J-030

Source: `intelligence-part2/sections/07_god_ja.tex:112–114` / P2J。Context: $\Phi_{\text{net}}$ の単一極限としての神。Family: INT-EQF-056。Label: NONE。source-local relation / annotation。

```tex
\[
\Phi_{\text{net}}^{\text{分散}} \;\xrightarrow{\text{統合}}\; \Phi_{\text{net}}^{\text{中心化}} \;\xrightarrow{\text{極限}}\; \text{単一懸架軌跡(神)}
\]
```

### INT-MATH-P2J-031

Source: `intelligence-part2/sections/11_instability_region_ja.tex:46–48` / P2J。Context: 三軸。Family: INT-EQF-038。Label: NONE。source-local relation / annotation。

```tex
\[
\Delta v_{\text{intel}} = v_{\text{inf}} - v_{LR}
\]
```

### INT-MATH-P2AJ-001

Source: `intelligence-part2/appendices/appendix_a_master_table_ja.tex:162–164` / P2AJ。Context: 変数間の主要な関係式。Family: INT-EQF-032。Label: NONE。source-local relation / annotation。

```tex
\[
L_E = \Phi(L_R \text{の運動}, \; H_{ij}) \qquad \text{(創発の定義 1.1 の知性層適用)}
\]
```

### INT-MATH-P2AJ-002

Source: `intelligence-part2/appendices/appendix_a_master_table_ja.tex:166–168` / P2AJ。Context: 変数間の主要な関係式。Family: INT-EQF-033。Label: NONE。source-local relation / annotation。

```tex
\[
E = E[L_E, x_n], \quad E \notin \{F^k\} \qquad \text{(外部停止演算子の定義 5.3)}
\]
```

### INT-MATH-P2AJ-003

Source: `intelligence-part2/appendices/appendix_a_master_table_ja.tex:170–172` / P2AJ。Context: 変数間の主要な関係式。Family: INT-EQF-034。Label: NONE。source-local relation / annotation。

```tex
\[
\Phi_{\text{ext}} \equiv \Phi_{\text{net}} \qquad \text{(主張 5.4 の同型)}
\]
```

### INT-MATH-P2AJ-004

Source: `intelligence-part2/appendices/appendix_a_master_table_ja.tex:174–176` / P2AJ。Context: 変数間の主要な関係式。Family: INT-EQF-054。Label: NONE。source-local relation / annotation。

```tex
\[
\mu_\theta \;\xrightarrow{\text{起こす}}\; (B)\text{組み替え} \;\xrightarrow{H_{ij}\text{に沿って}}\; E\text{設置領域の投影} \;\xrightarrow{L_R\text{収束}}\; L_E \qquad \text{(§5.5 創発機構)}
\]
```

### INT-MATH-P2AJ-005

Source: `intelligence-part2/appendices/appendix_a_master_table_ja.tex:178–180` / P2AJ。Context: 変数間の主要な関係式。Family: INT-EQF-019, INT-EQF-022, INT-EQF-029。Label: NONE。source-local relation / annotation。

```tex
\[
I = f(1-C), \quad F_I = \alpha \nabla C, \quad C_{ij} = 1 - \exp(-\lambda \rho_i H_{ij}) \qquad \text{(VED/IFGT 基本式)}
\]
```

### INT-MATH-P2AJ-006

Source: `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:15–17` / P2AJ。Context: 定理 3.1(非閉包定理 / Non-Closure Theorem)。Family: INT-EQF-027。Label: NONE。source-local relation / annotation。

```tex
\[
\forall x \in \mathcal{X}, \quad F(x) \neq x
\]
```

### INT-MATH-P2AJ-007

Source: `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:45–47` / P2AJ。Context: VED 的創発の定義(定義 1.1 の再掲)。Family: INT-EQF-031。Label: NONE。source-local relation / annotation。

```tex
$$
\mathcal{U} = \Phi(\mathcal{L}\text{の運動}, \; H_{ij})
$$
```

## 3. Inline inventory

source全inline mathは2199 occurrence。関係記号に加えb^d・graph set/cardinality・三軸tuple等のrole-sensitive表現を含め131 occurrence、94 lexical familiesを下表に記録。同一stream内の空白のみを除いた一致でgroupし、異言語/本文補遺の一致を自動同一object化しない。isolated arrows/C≠は文外の項を周辺proseで補う構文であり、完全なbinary mapと認定しない。全残余lexemeは末尾symbol occurrence indexに保持。

| INLINE | Raw variants | Occurrences / locator | EQF |
|---|---|---|---|
| INT-INLINE-001 | `\(\{N_i,e_{ij}\}\)` | 2: `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex:16`; `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex:62` | 063 |
| INT-INLINE-002 | `\(dD_{ij}/dt=f(&#124;Q&#124;)-D_{ij}\)` | 1: `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex:63` | 006 |
| INT-INLINE-003 | `\(h^{(\ell+1)}=F_{\mathrm{tr}}(h^{(\ell)})\)` | 1: `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex:63` | 009 |
| INT-INLINE-004 | `\(\nabla\cdot J=0\)` | 1: `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex:38` | 011 |
| INT-INLINE-005 | `\(&#124;V&#124;\)` | 1: `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex:51` | 014 |
| INT-INLINE-006 | `\(&#124;E&#124;\sim &#124;V&#124;^2\)` | 1: `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex:51` | 014 |
| INT-INLINE-007 | `\(b^d\)` | 1: `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex:51` | 015 |
| INT-INLINE-008 | `$s(t+1) = F(s(t))$` | 1: `intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex:55` | 001 |
| INT-INLINE-009 | `$\{N_i\}$` | 1: `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:109` | 063 |
| INT-INLINE-010 | `$\{e_{ij}\}$` | 1: `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:110` | 063 |
| INT-INLINE-011 | `$f(Q) = &#124;Q&#124;^{\mu}$` | 1: `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:130` | 007 |
| INT-INLINE-012 | `$\mu > 0$` | 1: `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:130` | 007 |
| INT-INLINE-013 | `$\{N_i, e_{ij}\}$` | 2: `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:37`; `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:147` | 063 |
| INT-INLINE-014 | `$s_{t+1} = F_\text{bio}(s_t)$` | 1: `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:46` | 045 |
| INT-INLINE-015 | `$dD_{ij}/dt = f(\lvert Q\rvert) - D_{ij}$` | 1: `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:148` | 006 |
| INT-INLINE-016 | `$h^{(\ell+1)} = F_\text{tr}(h^{(\ell)})$` | 1: `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:148` | 009 |
| INT-INLINE-017 | `$\nabla \cdot J = 0$` | 1: `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:91` | 011 |
| INT-INLINE-018 | `$&#124;E&#124;$` | 1: `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:109` | 014 |
| INT-INLINE-019 | `$&#124;V&#124;$` | 1: `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:109` | 014 |
| INT-INLINE-020 | `$&#124;E&#124; \sim &#124;V&#124;^2$` | 1: `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:109` | 014 |
| INT-INLINE-021 | `$b^d$` | 1: `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:112` | 015 |
| INT-INLINE-022 | `$x_n\in\mathcal{X}$` | 1: `intelligence-part2/sections/02_inference_operator.tex:12` | 025 |
| INT-INLINE-023 | `$x_{n+1}=F(x_n)$` | 1: `intelligence-part2/sections/03_nonclosure_theorem.tex:18` | 025 |
| INT-INLINE-024 | `$F(x^*)=x^*$` | 2: `intelligence-part2/sections/03_nonclosure_theorem.tex:43`; `intelligence-part2/sections/03_nonclosure_theorem.tex:47` | 027 |
| INT-INLINE-025 | `$H_{ji}\approx 0$` | 1: `intelligence-part2/sections/04_response_channels.tex:12` | 035 |
| INT-INLINE-026 | `$U=\Phi(L,H_{ij})$` | 1: `intelligence-part2/sections/05_emergent_stopping_layer.tex:48` | 031 |
| INT-INLINE-027 | `$\Phi_{\text{ext}}\equiv\Phi_{\text{net}}$`<br>`$\Phi_{\text{ext}} \equiv \Phi_{\text{net}}$` | 2: `intelligence-part2/sections/05_emergent_stopping_layer.tex:90`; `intelligence-part2/sections/05_emergent_stopping_layer.tex:101` | 034 |
| INT-INLINE-028 | `$\Delta v_{\text{intel}} = v_{\text{inf}} - v_{LR}$` | 1: `intelligence-part2/sections/11_instability_region.tex:46` | 038 |
| INT-INLINE-029 | `$\Phi_{\text{ext}} \equiv \Phi_{\text{net}}$` | 5: `intelligence-part2/sections/00_introduction_ja.tex:124`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:277`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:297`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:304`; `intelligence-part2/sections/07_god_ja.tex:62` | 034 |
| INT-INLINE-030 | `$\to$` | 1: `intelligence-part2/sections/00_introduction_ja.tex:221` | 051 |
| INT-INLINE-031 | `$L_R \to L_E$` | 1: `intelligence-part2/sections/00_introduction_ja.tex:232` | 050 |
| INT-INLINE-032 | `$C \neq$` | 2: `intelligence-part2/sections/00_introduction_ja.tex:275`; `intelligence-part2/sections/10_gettier_problem_ja.tex:2` | 049 |
| INT-INLINE-033 | `$0 \le C < C_{max}$` | 1: `intelligence-part2/sections/01_preliminaries_ja.tex:53` | 018 |
| INT-INLINE-034 | `$f(u) = u$` | 1: `intelligence-part2/sections/01_preliminaries_ja.tex:80` | 020 |
| INT-INLINE-035 | `$f(u) = -\ln(1-u)$` | 1: `intelligence-part2/sections/01_preliminaries_ja.tex:80` | 021 |
| INT-INLINE-036 | `$I \to 0$` | 1: `intelligence-part2/sections/01_preliminaries_ja.tex:82` | 059 |
| INT-INLINE-037 | `$\nabla C \approx 0$` | 1: `intelligence-part2/sections/01_preliminaries_ja.tex:94` | 060 |
| INT-INLINE-038 | `$\dot{x} = F(x;\theta)$`<br>`$\dot{x}=F(x;\theta)$` | 2: `intelligence-part2/sections/01_preliminaries_ja.tex:121`; `intelligence-part2/sections/01_preliminaries_ja.tex:243` | 046 |
| INT-INLINE-039 | `$C: \mathcal{X} \to [0, C_{max})$` | 1: `intelligence-part2/sections/01_preliminaries_ja.tex:139` | 024 |
| INT-INLINE-040 | `$C \to C_{max}$` | 5: `intelligence-part2/sections/01_preliminaries_ja.tex:155`; `intelligence-part2/sections/01_preliminaries_ja.tex:184`; `intelligence-part2/sections/01_preliminaries_ja.tex:349`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:153`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:166` | 018 |
| INT-INLINE-041 | `$C = C_{max}$` | 1: `intelligence-part2/sections/01_preliminaries_ja.tex:186` | 018 |
| INT-INLINE-042 | `$\sum \vec{e} \approx 0$` | 1: `intelligence-part2/sections/01_preliminaries_ja.tex:242` | 061 |
| INT-INLINE-043 | `$\mathcal{U} = \Phi(\mathcal{L}, H_{ij})$` | 1: `intelligence-part2/sections/01_preliminaries_ja.tex:249` | 031 |
| INT-INLINE-044 | `$\Omega_{\text{intel}} \subset \Omega_{\text{life}}$` | 1: `intelligence-part2/sections/01_preliminaries_ja.tex:251` | 036 |
| INT-INLINE-045 | `$I = f(1-C)$` | 2: `intelligence-part2/sections/01_preliminaries_ja.tex:345`; `intelligence-part2/sections/11_instability_region_ja.tex:126` | 019 |
| INT-INLINE-046 | `$F_I = \alpha \nabla C$` | 1: `intelligence-part2/sections/01_preliminaries_ja.tex:346` | 022 |
| INT-INLINE-047 | `$J_C = -\xi \nabla C$` | 2: `intelligence-part2/sections/01_preliminaries_ja.tex:362`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:44` | 023 |
| INT-INLINE-048 | `$x_0 \to x_1 \to x_2 \to \cdots$` | 1: `intelligence-part2/sections/02_inference_operator_ja.tex:46` | 025 |
| INT-INLINE-049 | `$x_n \to x_{n+1}$` | 1: `intelligence-part2/sections/02_inference_operator_ja.tex:49` | 025 |
| INT-INLINE-050 | `$(v_{\text{inf}}, r_{\text{res}}, \eta)$` | 3: `intelligence-part2/sections/02_inference_operator_ja.tex:121`; `intelligence-part2/sections/04_response_channels_ja.tex:45`; `intelligence-part2/sections/11_instability_region_ja.tex:43` | 040 |
| INT-INLINE-051 | `$J: \mathcal{X} \to \mathbb{R}$` | 1: `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:35` | 047 |
| INT-INLINE-052 | `$x \in \mathcal{X}$` | 1: `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:35` | 025 |
| INT-INLINE-053 | `$F(x^*) = x^*$` | 3: `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:65`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:75`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:89` | 027 |
| INT-INLINE-054 | `$x^* \in \mathcal{X}$` | 1: `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:75` | 027 |
| INT-INLINE-055 | `$x = x^*$` | 1: `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:83` | 027 |
| INT-INLINE-056 | `$\partial \rho / \partial t + \nabla \cdot (\rho \mathbf{v}) = 0$` | 1: `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:109` | 042 |
| INT-INLINE-057 | `$S: \mathcal{X} \to \{0, 1\}$` | 1: `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:124` | 028 |
| INT-INLINE-058 | `$S(x) = 1$` | 1: `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:128` | 028 |
| INT-INLINE-059 | `$H_{ji} \approx 0$` | 3: `intelligence-part2/sections/04_response_channels_ja.tex:21`; `intelligence-part2/sections/04_response_channels_ja.tex:69`; `intelligence-part2/sections/06_animism_ja.tex:26` | 035 |
| INT-INLINE-060 | `$U=\Phi(L,H_{ij})$` | 1: `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:113` | 031 |
| INT-INLINE-061 | `$E \notin \{F^k\}$` | 1: `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:268` | 033 |
| INT-INLINE-062 | `$H_{ji} > 0$` | 1: `intelligence-part2/sections/06_animism_ja.tex:26` | 035 |
| INT-INLINE-063 | `$L_E = \Phi(L_R, H_{ij})$` | 1: `intelligence-part2/sections/07_god_ja.tex:125` | 032 |
| INT-INLINE-064 | `$\Delta v_{\text{intel}} = v_{\text{inf}} - v_{LR}$` | 1: `intelligence-part2/sections/11_instability_region_ja.tex:90` | 038 |
| INT-INLINE-065 | `$v_{\text{inf}} = 0$` | 2: `intelligence-part2/sections/11_instability_region_ja.tex:122`; `intelligence-part2/sections/11_instability_region_ja.tex:124` | 040 |
| INT-INLINE-066 | `$r_{\text{res}} = 0$` | 1: `intelligence-part2/sections/11_instability_region_ja.tex:122` | 040 |
| INT-INLINE-067 | `$J_C = -\xi \nabla C$` | 1: `intelligence-part2/appendices/appendix_a_master_table_ja.tex:27` | 023 |
| INT-INLINE-068 | `$I = f(1-C)$` | 1: `intelligence-part2/appendices/appendix_a_master_table_ja.tex:28` | 019 |
| INT-INLINE-069 | `$F_I = \alpha \nabla C$` | 1: `intelligence-part2/appendices/appendix_a_master_table_ja.tex:29` | 022 |
| INT-INLINE-070 | `$C_{ij} = 1-\exp(-\lambda \rho_i H_{ij})$` | 1: `intelligence-part2/appendices/appendix_a_master_table_ja.tex:32` | 029 |
| INT-INLINE-071 | `$x_{n+1} = F(x_n)$` | 2: `intelligence-part2/appendices/appendix_a_master_table_ja.tex:56`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:119` | 025 |
| INT-INLINE-072 | `$J(F(x)) > J(x)$` | 3: `intelligence-part2/appendices/appendix_a_master_table_ja.tex:57`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:22`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:30` | 026 |
| INT-INLINE-073 | `$L_E = \Phi(L_R, H_{ij})$` | 1: `intelligence-part2/appendices/appendix_a_master_table_ja.tex:60` | 032 |
| INT-INLINE-074 | `$E = E[L_E, x_n]$` | 1: `intelligence-part2/appendices/appendix_a_master_table_ja.tex:77` | 033 |
| INT-INLINE-075 | `$E \notin \{F^k\}$` | 1: `intelligence-part2/appendices/appendix_a_master_table_ja.tex:77` | 033 |
| INT-INLINE-076 | `$\Phi_{\text{ext}} \equiv \Phi_{\text{net}}$` | 4: `intelligence-part2/appendices/appendix_a_master_table_ja.tex:78`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:27`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:152`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:165` | 034 |
| INT-INLINE-077 | `$\mathcal{U} = \Phi(\mathcal{L}, H_{ij})$` | 3: `intelligence-part2/appendices/appendix_b_homology_ja.tex:34`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:53`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:158` | 031 |
| INT-INLINE-078 | `$\dot{x}=F(x;\theta)$`<br>`$\dot{x} = F(x;\theta)$` | 4: `intelligence-part2/appendices/appendix_b_homology_ja.tex:47`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:118`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:129`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:94` | 046 |
| INT-INLINE-079 | `$J: \mathcal{X} \to \mathbb{R}$` | 1: `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:22` | 047 |
| INT-INLINE-080 | `$F(x^*) = x^*$` | 3: `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:28`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:34`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:68` | 027 |
| INT-INLINE-081 | `$x^* \in \mathcal{X}$` | 1: `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:28` | 027 |
| INT-INLINE-082 | `$x = x^*$` | 1: `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:32` | 027 |
| INT-INLINE-083 | `$J(F(x^*)) > J(x^*)$` | 1: `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:32` | 027 |
| INT-INLINE-084 | `$J(x^*) > J(x^*)$` | 1: `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:34` | 027 |
| INT-INLINE-085 | `$S: \mathcal{X} \to \{0, 1\}$` | 1: `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:46` | 028 |
| INT-INLINE-086 | `$S(x) = 1$` | 1: `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:50` | 028 |
| INT-INLINE-087 | `$F(x) = x$` | 1: `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:50` | 027 |
| INT-INLINE-088 | `$C \to C_{max}$` | 2: `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:64`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:84` | 018 |
| INT-INLINE-089 | `$\mathcal{U} = \Phi(\mathcal{L}\text{の運動}, H_{ij})$` | 1: `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:113` | 031 |
| INT-INLINE-090 | `$\sum \vec{e} \approx 0$` | 1: `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:121` | 061 |
| INT-INLINE-091 | `$\Leftrightarrow$` | 1: `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:170` | 037 |
| INT-INLINE-092 | `$\Rightarrow$` | 1: `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:175` | 037 |
| INT-INLINE-093 | `$\Leftarrow$` | 1: `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:179` | 037 |
| INT-INLINE-094 | `$\vec{e}_i + \vec{e}_j + \vec{e}_k \approx 0$` | 1: `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:76` | 061 |

## 4. Final equation families / signature / unit / dependency crosswalk

| ID | Family | Signature | Signature scope | Phase00 draft | Claim families | Source / all occurrences | Units / dependence |
|---|---|---|---|---|---|---|---|
| INT-EQF-001 | P1 ordered update | PARTIAL | S上の状態遷移; Fの具体形・codomainの完全宣言なし | 001 | INT-CLM-005–009 | P1 §3; INT-MATH-P1E-002, INT-MATH-P1J-002, INT-INLINE-008 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-002 | P1 global Φ map | EXPLICIT | Φ: S→R; scalar fieldと明示、Sの幾何は別問題 | 002 | INT-CLM-007–010 | P1 §3; INT-MATH-P1E-003, INT-MATH-P1J-003 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-003 | P1 Φbio map | EXPLICIT | S→Rの表示、biological biasの解釈別 | 003 | INT-CLM-011–014 | P1 §5; INT-MATH-P1J-007 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-004 | P1 Φtr map | EXPLICIT | S→Rの表示、training/inference役割別 | 003 | INT-CLM-011–014 | P1 §5; INT-MATH-P1E-009, INT-MATH-P1J-010 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-005 | Physarum Q relation | PARTIAL | edge flow/conductance/length/pressure roles; graph/units not complete | 004 | INT-CLM-011–013 | P1 §4; INT-MATH-P1E-004, INT-MATH-P1J-004 | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-006 | Physarum conductance update | PARTIAL | continuous t derivative; f response form optional | 005 | INT-CLM-011–013 | P1 §4–5; INT-MATH-P1E-005, INT-MATH-P1E-006, INT-MATH-P1J-005, INT-MATH-P1J-006, INT-INLINE-002, INT-INLINE-015 | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-007 | Physarum power response and μ>0 | PARTIAL | f(Q)=abs(Q)^μ example; range/domain not fully fixed | 006 | INT-CLM-011–013 | P1 J §4; INT-INLINE-011, INT-INLINE-012 | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-008 | Transformer state set | PARTIAL | hidden states indexed i,ell; tensor dimensions not specified | 007 | INT-CLM-013–014 | P1 §5; INT-MATH-P1E-007, INT-MATH-P1J-008 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-009 | Transformer layer update | PARTIAL | Ftr input/output hidden-state roles; layer dependence not typed | 007 | INT-CLM-013–014 | P1 §5; INT-MATH-P1E-008, INT-MATH-P1J-009, INT-INLINE-003, INT-INLINE-016 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-010 | I(s) increase | PARTIAL | accumulation scalar/density role; ↑ no parameter derivative | 008 | INT-CLM-017 | P1 §7; INT-MATH-P1E-010, INT-MATH-P1J-011 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-011 | div J increase / zero comparison | PARTIAL | vector-like flow/divergence; geometry not specified | 008 | INT-CLM-017–019 | P1 §7; INT-MATH-P1E-011, INT-MATH-P1J-012, INT-INLINE-004, INT-INLINE-017 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-012 | correctness(p) implies nonzero divergence | UNRESOLVED | proposition p→field evaluation at p mapping untyped | 008 | INT-CLM-017–018 | P1 §7; INT-MATH-P1E-012, INT-MATH-P1J-013 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-013 | I(si) increase for indexed states | PARTIAL | states i=1,2,... given; ↑ qualitative | 009 | INT-CLM-017–018 | P1 J §7; INT-MATH-P1J-014 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-014 | graph edge-square growth | PARTIAL | &#124;E&#124;∼&#124;V&#124;²; graph conditions/asymptotic variable incomplete | 010 | INT-CLM-018 | P1 §7; INT-INLINE-005, INT-INLINE-006, INT-INLINE-018, INT-INLINE-019, INT-INLINE-020 | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-015 | branch count b^d | PARTIAL | b branching/depth d; path counting conditions incomplete | 011 | INT-CLM-018–019 | P1 §7; INT-INLINE-007, INT-INLINE-021 | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-016 | external T membership | UNRESOLVED | External(R) symbolic membership; operator collection not typed | 012 | INT-CLM-024–028 | P1 §9; INT-MATH-P1E-015, INT-MATH-P1J-017 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-017 | closure PDE | PARTIAL | C scalar/JC flux/tau order/parameters named; domain/IC/BC not supplied | 013 | INT-CLM-041–042 | P2 J §1,3; INT-MATH-P2J-007, INT-MATH-P2J-023 | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-018 | C range / endpoint barrier | PARTIAL | 0≤C<Cmax explicit; parameter scale and dynamical boundary status separate | 014 | INT-CLM-042 | P2 J §1,3; INT-INLINE-033, INT-INLINE-040, INT-INLINE-041, INT-INLINE-088 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-019 | I=f(1−C) | PARTIAL | scalar function f monotonicity in JA; range/normalization not fixed | 015 | INT-CLM-040–042 | P2 §1,A; INT-MATH-P2E-003, INT-MATH-P2J-008, INT-MATH-P2AJ-005, INT-INLINE-045, INT-INLINE-068 | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-020 | f(u)=u example | PARTIAL | example only; domain not fixed | 015 | INT-CLM-041 | P2 J §1; INT-INLINE-034 | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-021 | f(u)=−ln(1−u) example | PARTIAL | example only; admissible argument domain not stated | 015 | INT-CLM-041 | P2 J §1; INT-INLINE-035 | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-022 | FI=α∇C | PARTIAL | α coupling constant; vector geometry/units unspecified | 016 | INT-CLM-041,046 | P2 J §1,A; INT-MATH-P2J-009, INT-MATH-P2AJ-005, INT-INLINE-046, INT-INLINE-069 | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-023 | JC=−ξ∇C | PARTIAL | closure flux template; ξ/geometry/unit scope incomplete | 017 | INT-CLM-041,046 | P2 J §1,3,A; INT-INLINE-047, INT-INLINE-067 | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-024 | C:X→[0,Cmax) | EXPLICIT | source map domain/codomain explicit; X geometry not thereby fixed | 018 | INT-CLM-040,043 | P2 J §1; INT-INLINE-039 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-025 | P2 inference update | CONFLICTING | single next state vs explicitly set-valued F branch; source offers alternatives, compatibility undecided | 019 | INT-CLM-046,051 | P2 §2–3; INT-MATH-P2E-006, INT-MATH-P2J-010, INT-MATH-P2J-013, INT-MATH-P2J-017, INT-INLINE-022, INT-INLINE-023, INT-INLINE-048, INT-INLINE-049, INT-INLINE-052, INT-INLINE-071 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-026 | strict justification increase | PARTIAL | J:X→R elsewhere explicit; admissibility/F composition scope incomplete | 020 | INT-CLM-051 | P2 §2–3,D; INT-MATH-P2E-008, INT-MATH-P2E-011, INT-MATH-P2J-018, INT-MATH-P2J-020, INT-INLINE-072 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-027 | nonfixed-point theorem / contradiction sequence | PARTIAL | quantified X, strict J and assumed x*; not proof validation | 021 | INT-CLM-051–054 | P2 §3,D; INT-MATH-P2E-012, INT-MATH-P2E-013, INT-MATH-P2E-014, INT-MATH-P2E-015, INT-MATH-P2J-019, INT-MATH-P2J-021, INT-MATH-P2J-022, INT-MATH-P2AJ-006, INT-INLINE-024, INT-INLINE-053, INT-INLINE-054, INT-INLINE-055, INT-INLINE-080, INT-INLINE-081, INT-INLINE-082, INT-INLINE-083, INT-INLINE-084, INT-INLINE-087 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-028 | internal stopping predicate | EXPLICIT | S:X→{0,1} appears as hypothetical rejected construction, not adopted operator | 022 | INT-CLM-052 | P2 §2–3,D; INT-MATH-P2E-010, INT-INLINE-057, INT-INLINE-058, INT-INLINE-085, INT-INLINE-086 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-029 | Cij exponential relation | PARTIAL | i agent/jenvironment; λρH compatibility/ranges not specified | 023 | INT-CLM-048 | P2 J §2,A; INT-MATH-P2J-015, INT-MATH-P2AJ-005, INT-INLINE-070 | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-030 | Ωθ and A/B reconfiguration | PARTIAL | region/parameter collection; no explicit domain-reconfiguration operator | 024 | INT-CLM-043,049 | P2 §1–2,A; prose-only; dedicated ledgers below | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-031 | emergence U=Φ(L,H) | UNRESOLVED | Φ operator kind/domain/codomain not supplied; U vs calU variants | 025 | INT-CLM-044,093 | P2 §1,E; INT-MATH-P2E-004, INT-MATH-P2AE-002, INT-MATH-P2J-011, INT-MATH-P2AJ-007, INT-INLINE-026, INT-INLINE-043, INT-INLINE-060, INT-INLINE-077, INT-INLINE-089 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-032 | LE=Φ(LR motion,H) | UNRESOLVED | log motion / mutual constraint inputs named, layer output type missing | 026 | INT-CLM-037,059–060 | P2 §5,A; INT-MATH-P2E-005, INT-MATH-P2E-016, INT-MATH-P2J-025, INT-MATH-P2AJ-001, INT-INLINE-063, INT-INLINE-073 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-033 | E[LE,xn] and E not in F^k | UNRESOLVED | left operator vs RHS construction; k index/codomain/update missing | 027 | INT-CLM-063 | P2 §5,A; INT-MATH-P2E-018, INT-MATH-P2J-027, INT-MATH-P2AJ-002, INT-INLINE-061, INT-INLINE-074, INT-INLINE-075 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-034 | Φext≡Φnet | UNRESOLVED | functional field vs network; same-structure assertion without typed map | 028 | INT-CLM-064–065 | P2 §5,D; INT-MATH-P2E-019, INT-MATH-P2E-026, INT-MATH-P2J-028, INT-MATH-P2AJ-003, INT-INLINE-027, INT-INLINE-029, INT-INLINE-076 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-035 | response/silence Hji≈0 and Hji>0 | PARTIAL | threshold role, effective normalization not fixed | 029 | INT-CLM-055,067 | P2 §4,6; INT-INLINE-025, INT-INLINE-059, INT-INLINE-062 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-036 | Ωintel subset Ωlife | UNRESOLVED | sets named; common ambient space across Bio/Int not supplied | 030 | INT-CLM-045 | P2 J §1; INT-INLINE-044 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-037 | error tolerance ↔ μθ | UNRESOLVED | prose equivalence; propositions/predicates not independently formalized | 031 | INT-CLM-080 | P2 J §10,D; INT-INLINE-091, INT-INLINE-092, INT-INLINE-093 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-038 | Δvintel=vinf−vLR | PARTIAL | two speeds, subtraction; common time/counting convention incomplete | 032 | INT-CLM-082 | P2 §11; INT-MATH-P2E-025, INT-MATH-P2J-031, INT-INLINE-028, INT-INLINE-064 | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-039 | Σ development/activity quantity | PARTIAL | JA A defines quantity not quantified; not defined as phase-region set | 033 | INT-CLM-089 | P2 J §1,A; prose-only; dedicated ledgers below | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-040 | three-axis regions / zero-motion condition | PARTIAL | vinf/rres/η coordinates qualitatively named; numeric region predicates not supplied | 033 | INT-CLM-081–085 | P2 §11; INT-INLINE-050, INT-INLINE-065, INT-INLINE-066 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-041 | VED E(A) / stopping functional minimum comparison | UNRESOLVED | energy functional imported by name; stopping functional not written | 034 | INT-CLM-089,093 | P2 J E; prose-only; dedicated ledgers below | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-042 | fluid continuity analogy | PARTIAL | ρ,v,t as fluid roles; illustrative not P2 adopted evolution | 035 | INT-CLM-051 | P2 J §3; INT-INLINE-056 | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-043 | P1 S={si,...} | INFERRED | set of states explicit enumeration; cardinality/topology not fixed | NEW | INT-CLM-005–006 | P1 §3; INT-MATH-P1E-001, INT-MATH-P1J-001 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-044 | T not in Internal(R) | UNRESOLVED | internal/external notation scope; not a typed existence theorem here | NEW | INT-CLM-021,025 | P1 §8–9; INT-MATH-P1E-013, INT-MATH-P1E-014, INT-MATH-P1J-015, INT-MATH-P1J-016 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-045 | P1 Fbio discrete update | PARTIAL | s_t→s_t+1 biological time reading; relation to conductance ODE not typed | NEW | INT-CLM-013 | P1 J §5; INT-INLINE-014 | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-046 | P2 Bio continuous F(x;θ) | PARTIAL | dx/dt Bio state-evolution comparison; not inference F identity | NEW | INT-CLM-045–050 | P2 J §1–2; INT-MATH-P2J-014, INT-INLINE-038, INT-INLINE-078 | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-047 | J:X→R justification | EXPLICIT | real-valued function called measure; measure-theoretic structure not declared | NEW | INT-CLM-046,051 | P2 §2–3; INT-MATH-P2E-007, INT-INLINE-051, INT-INLINE-079 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-048 | set-valued F continuation | CONFLICTING | set of next states vs single-state F; no powerset signature/adaptation of J supplied | NEW | INT-CLM-046,051 | P2 E §2; INT-MATH-P2E-009 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-049 | C operational stability / denied C=truth | PARTIAL | two displayed equalities under positive vs negating prose; do not assert denied equality | NEW | INT-CLM-040,078 | P2 E §10; INT-MATH-P2E-023, INT-MATH-P2E-024, INT-INLINE-032 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-050 | LF→LR→LE architecture sequence | UNRESOLVED | arrows include trace/Φ/μ labels; sequence not composable maps | NEW | INT-CLM-037,057–060 | P2 §0–2; INT-MATH-P2E-001, INT-MATH-P2J-005, INT-MATH-P2J-012, INT-MATH-P2J-016, INT-MATH-P2J-024, INT-INLINE-031 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-051 | difference→F→nonclosure→externalstop chain | UNRESOLVED | expository/formal-strength schematic sequence | NEW | INT-CLM-036,051–054 | P2 §0–1; INT-MATH-P2E-002, INT-MATH-P2J-001, INT-MATH-P2J-002, INT-INLINE-030 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-052 | H→response threshold→μ→sapiens chain | UNRESOLVED | schematic stages, no typed composition | NEW | INT-CLM-048–049 | P2 J §0; INT-MATH-P2J-003, INT-MATH-P2J-004 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-053 | LE→Φnet→externally dependent existence | UNRESOLVED | architectural/social consequence chain | NEW | INT-CLM-037,064 | P2 J §0; INT-MATH-P2J-006 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-054 | μ→B→E-site→LRconvergence→LE | UNRESOLVED | proposed mechanism arrows, no update/convergence specification | NEW | INT-CLM-060 | P2 §5,A; INT-MATH-P2E-017, INT-MATH-P2J-026, INT-MATH-P2AJ-004 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-055 | environmental locus ↦ E site | UNRESOLVED | animism operation prose map, no formal input/output spaces | NEW | INT-CLM-067 | P2 E §6; INT-MATH-P2E-020 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-056 | distributed→centralized stopping / singlepole | UNRESOLVED | historical-structural schema, no network limit topology | NEW | INT-CLM-069–070 | P2 §7; INT-MATH-P2E-021, INT-MATH-P2J-030 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-057 | centralized→maintained stopping | UNRESOLVED | religion maintenance schema | NEW | INT-CLM-071 | P2 E §8; INT-MATH-P2E-022 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-058 | God negative identities | UNRESOLVED | negative-scope text equations, not numeric quantities | NEW | INT-CLM-069 | P2 J §7; INT-MATH-P2J-029 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-059 | complete closure implies I→0 | PARTIAL | conditional prose/formal limit; f/range premise distinct | NEW | INT-CLM-042 | P2 J §1; INT-INLINE-036 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-060 | ∇C≈0 / remaining motion | PARTIAL | local gradient quiescence contextual condition; no full dynamics implied | NEW | INT-CLM-042,046 | P2 J §1; INT-INLINE-037 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-061 | causal vector closure sums | PARTIAL | sum e≈0 / ei+ej+ek≈0 imported illustration; space/index set incomplete | NEW | INT-CLM-044,093 | P2 J §1,E; INT-INLINE-042, INT-INLINE-090, INT-INLINE-094 | implicit compatibility required; source numerical units not specified; dependencies below |
| INT-EQF-062 | homology kernel incompleteclosure→attractor→sustaineddynamics | UNRESOLVED | cross-domain arrow summary, not LF/LR/LE map | NEW | INT-CLM-091,093 | P2 E B; INT-MATH-P2AE-001 | not specified (map/order roles only; no automatic dimensionless declaration) |
| INT-EQF-063 | Physarum graph nodes/edges | PARTIAL | Ni/eij network representation; graph orientation/cardinality not fully specified | NEW | INT-CLM-011–013 | P1 §4–5; INT-INLINE-001, INT-INLINE-009, INT-INLINE-010, INT-INLINE-013 | not specified (map/order roles only; no automatic dimensionless declaration) |

## 5. Phase00 draft reconciliation

| ID | Phase00 | Phase01 | Action |
|---|---|---|---|
| INT-DRAFTMAP-001 | INT-EQF-DRAFT-001 | EQF001 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-002 | INT-EQF-DRAFT-002 | EQF002 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-003 | INT-EQF-DRAFT-003 | EQF003, EQF004 | SPLIT: distinct formula/type/role occurrences separated |
| INT-DRAFTMAP-004 | INT-EQF-DRAFT-004 | EQF005 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-005 | INT-EQF-DRAFT-005 | EQF006 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-006 | INT-EQF-DRAFT-006 | EQF007 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-007 | INT-EQF-DRAFT-007 | EQF008, EQF009 | SPLIT: distinct formula/type/role occurrences separated |
| INT-DRAFTMAP-008 | INT-EQF-DRAFT-008 | EQF010, EQF011, EQF012 | SPLIT: distinct formula/type/role occurrences separated |
| INT-DRAFTMAP-009 | INT-EQF-DRAFT-009 | EQF013 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-010 | INT-EQF-DRAFT-010 | EQF014 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-011 | INT-EQF-DRAFT-011 | EQF015 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-012 | INT-EQF-DRAFT-012 | EQF016 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-013 | INT-EQF-DRAFT-013 | EQF017 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-014 | INT-EQF-DRAFT-014 | EQF018 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-015 | INT-EQF-DRAFT-015 | EQF019, EQF020, EQF021 | SPLIT: distinct formula/type/role occurrences separated |
| INT-DRAFTMAP-016 | INT-EQF-DRAFT-016 | EQF022 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-017 | INT-EQF-DRAFT-017 | EQF023 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-018 | INT-EQF-DRAFT-018 | EQF024 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-019 | INT-EQF-DRAFT-019 | EQF025 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-020 | INT-EQF-DRAFT-020 | EQF026 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-021 | INT-EQF-DRAFT-021 | EQF027 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-022 | INT-EQF-DRAFT-022 | EQF028 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-023 | INT-EQF-DRAFT-023 | EQF029 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-024 | INT-EQF-DRAFT-024 | EQF030 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-025 | INT-EQF-DRAFT-025 | EQF031 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-026 | INT-EQF-DRAFT-026 | EQF032 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-027 | INT-EQF-DRAFT-027 | EQF033 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-028 | INT-EQF-DRAFT-028 | EQF034 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-029 | INT-EQF-DRAFT-029 | EQF035 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-030 | INT-EQF-DRAFT-030 | EQF036 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-031 | INT-EQF-DRAFT-031 | EQF037 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-032 | INT-EQF-DRAFT-032 | EQF038 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-033 | INT-EQF-DRAFT-033 | EQF039, EQF040 | SPLIT: distinct formula/type/role occurrences separated |
| INT-DRAFTMAP-034 | INT-EQF-DRAFT-034 | EQF041 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |
| INT-DRAFTMAP-035 | INT-EQF-DRAFT-035 | EQF042 | RETAIN FAMILY: occurrence coverage expanded; no correctness conclusion |

Draft merge 0 / split 5 (003,007,008,015,033) / retained unsplit 30。既存35から42descendants、追加21（EQF043–063）、計63。追加は見落とし補足・prose/inline関係の独立化でありsource追加ではない。

## 6. Signature taxonomy

EXPLICIT=当該mapのdomain/codomain/typeがsourceに明記（well-posednessまで意味しない）。INFERRED=文法的に読み取れる最小限のtype、未宣言部分は補わない。PARTIAL=role/input/outputの一部明記。UNRESOLVED=signatureを固定できない。CONFLICTING=複数のtype契約の整合方法が未記載。主要集計母数はEQF63：EXPLICIT6 / INFERRED1 / PARTIAL34 / UNRESOLVED20 / CONFLICTING2。

単位は「式中で整合が必要」と「実際に単位が定義された」を分けた。real-valued mapだけでは無次元にならない。vinfはJA本文§11およびAで単位時間あたり推論stepというrelative rateの記述があるが、clock/step calibrationはない。図の長さ・速度・時刻例を理論変数の単位宣言に移さない。

## 7. Symbol families / collision risk

| ID | Glyph/local family | Locator | Local type/role | Signature | Risk | Same object / separation |
|---|---|---|---|---|---|---|
| INT-SYM-001 | S,\mathcal S; s_i | P1 §3; EQF043 | state set/member; enumeration | PARTIAL | C3 | P2 Xとの同定NO |
| INT-SYM-002 | s(t),s_t | P1 §3,5; EQF001,045 | state, ordered argument | PARTIAL | C1 | discrete/continuousreading分離 |
| INT-SYM-003 | \mathcal X,x,x_n,x* | P2 §1–3; EQF024–028 | inference state/domain/fixedpoint hypothesis | PARTIAL | C3 | P1 S/Bio x同定NO |
| INT-SYM-004 | \Phi (P1) | P1 §3; EQF002 | scalar map S→R | EXPLICIT | C4 | emergence Phiとは同定NO |
| INT-SYM-005 | \Phi_bio | P1 §5; EQF003 | biological bias scalar map | EXPLICIT | C3 | P2 Biofield同定UNRESOLVED |
| INT-SYM-006 | \Phi_tr | P1 §5; EQF004 | training/global bias scalar map | EXPLICIT | C1 | P1Phiのdomain-specificexample |
| INT-SYM-007 | \Phi (CT) | P2 J B.1; INT-HOMO009 | concept-landscape potential by comparison | PARTIAL | C4 | CT→InttypedmapNO |
| INT-SYM-008 | \Phi(L,H) | P2 §1,5,E; EQF031–032 | emergence map/operator, no signature | UNRESOLVED | C6 | P1scalarfieldとのtypecompatibility未指定 |
| INT-SYM-009 | \Phi_ext | P2 §5,A,D; EQF034 | external reference field, functional view | UNRESOLVED | C5 | PhiNet同一/同型主張YES;typedmapNO |
| INT-SYM-010 | \Phi_net | P2 §5,A,D; EQF034 | interacting LE network | UNRESOLVED | C5 | PhiExt同一/同型主張YES;P1Phi精密化主張 |
| INT-SYM-011 | I (P1) | P1 §4,7; EQF010,013 | information accumulation/density | PARTIAL | C3 | P2f(1-C)typedinheritanceNO |
| INT-SYM-012 | I (P2) | P2 §1,A; EQF019 | unresolved/unclosed field | PARTIAL | C4 | upstreamsameglyph≠typedidentity |
| INT-SYM-013 | J (P1) | P1 §4,7; EQF011 | information flow/divergence | PARTIAL | C3 | P2justification別対象 |
| INT-SYM-014 | J_int | P1 §4 lexical table | internal/information flow naming | PARTIAL | C2 | Jとのvocabularyreuse;signature未固定 |
| INT-SYM-015 | J_I | P2 J B.1 CT/Bio comparison | branch-local information flow | PARTIAL | C4 | Jjustification同定NO |
| INT-SYM-016 | J_C | P2 J §1,3,A; EQF023 | closure flux | PARTIAL | C4 | JflowとのconversionNO |
| INT-SYM-017 | J(x) | P2 §2,3; EQF047 | real-valued justification function | EXPLICIT | C3 | measure-theorymeasureとは未指定 |
| INT-SYM-018 | C | P2 §1,10; EQF024,049 | closure/stability real-valued map | EXPLICIT | C4 | truthidentity明示否定 |
| INT-SYM-019 | C_ij | P2 J §2,A; EQF029 | indexed causal-log/mutual-constraint relation | PARTIAL | C2 | scalarCへのaggregation未記載 |
| INT-SYM-020 | C_max,C_{max} | P2 §1,3,A; EQF018 | closure upper bound, twoTeXspellings | PARTIAL | C4 | upstreamboundnormalization未継承 |
| INT-SYM-021 | C_* | P2 J §1; EQF017 | source-relaxation reference parameter | PARTIAL | C1 | Cmaxとは別 |
| INT-SYM-022 | \nabla C | P2 §1,A | closure gradient | PARTIAL | C4 | geometry未指定 |
| INT-SYM-023 | \nabla\Phi | P1 §9 Concomparison | potential gradient | PARTIAL | C4 | closuregradientとのtypedrelation未指定 |
| INT-SYM-024 | F (P1) | P1 §3; EQF001 | ordered state update | PARTIAL | C3 | P2Fと同型未提示 |
| INT-SYM-025 | F_bio (P1) | P1 J §5; EQF045 | biological discrete update | PARTIAL | C3 | P2ODEとの変換NO |
| INT-SYM-026 | F_tr | P1 §5; EQF009 | Transformer hidden-state/layer update | PARTIAL | C3 | inferenceF同定NO |
| INT-SYM-027 | F (P2 single) | P2 §2,3; EQF025 | inference next-state operator | CONFLICTING | C6 | set-valuedalternativeとのJcomposition未固定 |
| INT-SYM-028 | F (P2 set) | P2 E §2; EQF048 | set of possible continuations | CONFLICTING | C6 | single-outputsignatureと区別 |
| INT-SYM-029 | F(x;\theta) (Bio) | P2 J §1,2; EQF046 | continuous state-rate field comparison | PARTIAL | C4 | source-localguardあり |
| INT-SYM-030 | F_I | P2 J §1,A; EQF022 | constraint/information force | PARTIAL | C4 | Fupdateとは別 |
| INT-SYM-031 | F',F^k | P2 J §3,D; EQF028,033 | repackagedinference/iteratefamily | PARTIAL | C2 | kcollection未定義 |
| INT-SYM-032 | f (Physarum) | P1 §4; EQF006–007 | nonlinear flow response | PARTIAL | C3 | P2fとは別 |
| INT-SYM-033 | f (closure) | P2 §1; EQF019–021 | monotone response/examplefunctions | PARTIAL | C3 | domain/range全指定NO |
| INT-SYM-034 | u | P2 J §1; EQF020–021 | example function argument | INFERRED | C0 | statexとは別 |
| INT-SYM-035 | Q_ij,Q | P1 §4; EQF005–007 | edge flow | PARTIAL | C4 | CTcalQtokenextractionとは別 |
| INT-SYM-036 | \mathcal Q (CT comparison) | CTauthority/INT-HOMO009 | token extraction comparator; Intlocaloperator未定義 | UNRESOLVED | C4 | sameobjectNO;IntadoptedQ未確認 |
| INT-SYM-037 | D_ij | P1 §4; EQF005–006 | conductance | PARTIAL | C0 | localrole |
| INT-SYM-038 | L_ij | P1 §4; EQF005 | edge length | PARTIAL | C3 | P2layerL別 |
| INT-SYM-039 | \Delta p_ij | P1 §4; EQF005 | pressure difference | PARTIAL | C0 | p_i単独定義/独立occurrenceNOTLOCATED |
| INT-SYM-040 | p | P1 §6–7; EQF012 | proposition/correctness argument | PARTIAL | C1 | pressurepと別 |
| INT-SYM-041 | N_i,e_ij | P1 §4–5; EQF063 | network nodes/edges | PARTIAL | C3 | P2causalvectors別 |
| INT-SYM-042 | h_i^(ell) | P1 §5; EQF008–009 | hidden state withtoken/layerindices | PARTIAL | C1 | dimensionnotgiven |
| INT-SYM-043 | \ell | P1 §5 | Transformer layer index | PARTIAL | C4 | CTtokenell_i別 |
| INT-SYM-044 | i,j (P1) | P1 §4–5 | node/hiddenstate indices | PARTIAL | C1 | contextseparated |
| INT-SYM-045 | V,E (graph) | P1 §7; EQF014 | vertex/edge sets,cardinality | PARTIAL | C3 | stopping/energyE別 |
| INT-SYM-046 | b | P1 §7; EQF015 | branching factor | PARTIAL | C0 | range/constantassumption未固定 |
| INT-SYM-047 | d | P1 §7; EQF015 | path depth | PARTIAL | C0 | exactdepthvsuptodepth文脈差 |
| INT-SYM-048 | \mathcal R | P1 §8–9; EQF016,044 | individual/reasoning system | UNRESOLVED | C2 | typedoperatorcollectionNO |
| INT-SYM-049 | \mathcal T | P1 §8–9; EQF016,044 | stopping condition/operator | UNRESOLVED | C3 | P2EとのformalmapNO |
| INT-SYM-050 | Internal,External | P1 §8–9 | system-internal/external membership domains | UNRESOLVED | C2 | sets/operatorsとして未定義 |
| INT-SYM-051 | t,t_n (P1) | P1 §3,9 | order/update/Concomparison | PARTIAL | C3 | clockidentityNO |
| INT-SYM-052 | t (Physarum/fluid/Bio) | P1 §4; P2 §1,3 | continuous-time derivative parameter | PARTIAL | C4 | sharedunitNO |
| INT-SYM-053 | n | P2 §1–3 | inference iteration | PARTIAL | C1 | n→tau/clockmapNO |
| INT-SYM-054 | \tau | P2 §1,A; P1§9comparison | internal order | PARTIAL | C4 | Con/PDE/sharedclockNO |
| INT-SYM-055 | T_\Phi | P1 §9 | Con processing-time/window comparison | PARTIAL | C4 | Tstop別 |
| INT-SYM-056 | \Delta v (Con) | P1 §9; P2 §11 | speed-gap comparison | PARTIAL | C4 | IntDelta v別 |
| INT-SYM-057 | \mu (Con) | P1 §9 | Concomparisonparameter | PARTIAL | C4 | mu_theta/powerexponent別 |
| INT-SYM-058 | \mu (Physarum) | P1 J §4; EQF007 | positive power exponent | PARTIAL | C3 | mu_theta別 |
| INT-SYM-059 | \theta | P2 §1,2,A | constraint parameter collection | PARTIAL | C4 | scalarthresholdに自動縮約しない |
| INT-SYM-060 | \mu_\theta | P2 §2,5,11,A | endogenous threshold-movement capacity | PARTIAL | C3 | numericalrate/operator未定義 |
| INT-SYM-061 | \Omega_\theta | P2 §1,2,A | maintainable/admissible region | PARTIAL | C4 | ambientspace未完全 |
| INT-SYM-062 | \Omega_life | P2 J §1,B | Bio quasi-closure region | PARTIAL | C4 | Intとの共通spaceNO |
| INT-SYM-063 | \Omega_intel | P2 J §1; EQF036 | intelligence region | PARTIAL | C4 | subsetは主張;typedembeddingNO |
| INT-SYM-064 | A,B (movement) | P2 §1–3,A | intra-domain/reconfiguration modes | PARTIAL | C1 | energyE(A)A別 |
| INT-SYM-065 | L_F | P2 §2 | inference layer/domain includingtrajectories | PARTIAL | C2 | space/processmixed |
| INT-SYM-066 | L_R | P2 §5 | recursive log-reference motion/layer | PARTIAL | C2 | storage≠motion;domain未固定 |
| INT-SYM-067 | L_E | P2 §5 | externallydependent stopping layer/attractor | PARTIAL | C2 | layer/attractor/outputkind未統一 |
| INT-SYM-068 | L,\mathcal L | P2 §1,E | lower-layer motion inemergenceschema | UNRESOLVED | C3 | PhysarumLij/CTcalL別 |
| INT-SYM-069 | U,\mathcal U | P2 §1,E; EQF031 | upper emergent attractor/schemaoutput | UNRESOLVED | C2 | glyphvariant;noformalidentificationmap |
| INT-SYM-070 | H,H_ij | P2 §1,2,5,A,E | mutual constraints | PARTIAL | C4 | operator/scalar/matrix统一NO |
| INT-SYM-071 | H_ji | P2 §4,6 | reverse response effective value | PARTIAL | C1 | symmetrynotassumed |
| INT-SYM-072 | \rho_i | P2 J §2,A | density factor | PARTIAL | C1 | rhorespidentityNO |
| INT-SYM-073 | \rho_resp | P2 §4,A | local response-channel density | PARTIAL | C2 | Hijcorrespondence;estimator未定義 |
| INT-SYM-074 | \lambda | P2 J §2,A | coupling coefficient | PARTIAL | C4 | CTlambda別 |
| INT-SYM-075 | a | P2 J §1; EQF017 | closure generation coefficient | PARTIAL | C0 | range/unit未指定 |
| INT-SYM-076 | \Gamma | P2 J §1; EQF017 | dissipation/relaxation coefficient | PARTIAL | C0 | range/unit未指定 |
| INT-SYM-077 | \kappa_B | P2 J §1; EQF017 | barrier coefficient | PARTIAL | C4 | sign/range未宣言 |
| INT-SYM-078 | \Delta | P2 J §1; EQF017 | generation/difference source | PARTIAL | C2 | Delta v別 |
| INT-SYM-079 | \xi | P2 J §1,3; EQF023 | closure-flux coefficient | PARTIAL | C4 | unit/range未指定 |
| INT-SYM-080 | \alpha | P2 J §1; EQF022 | coupling constant calledconstant | PARTIAL | C4 | globalregime constancy未詳述 |
| INT-SYM-081 | E (stopping) | P2 §5,A; EQF033 | externallydependent stoppingoperator | UNRESOLVED | C3 | graphE/energyE別 |
| INT-SYM-082 | E(A) | P2 J §1,E; EQF041 | VED particle energy functional byreference | PARTIAL | C4 | AconfigurationnotmovementA |
| INT-SYM-083 | \vec e_i | P2 J §1,E; EQF061 | causal vector | PARTIAL | C3 | graph eij別 |
| INT-SYM-084 | \Sigma | P2 J §1,A,13; EQF039 | LEdevelopment/activity conceptualquantity | PARTIAL | C2 | phase-regionsetではない |
| INT-SYM-085 | v_inf | P2 §11,A; EQF038,040 | inference steps/frequency | PARTIAL | C3 | relative rate;clock未較正 |
| INT-SYM-086 | v_LR | P2 §11; EQF038 | log-reference/assimilation speed | PARTIAL | C2 | commonunitnotexplicit |
| INT-SYM-087 | \Delta v_intel | P2 §11; EQF038 | difference of speeds | PARTIAL | C4 | ConDelta vと同じ量NO |
| INT-SYM-088 | r_res | P2 §11,A | granularity/resolution | PARTIAL | C2 | spatialresolution単位NO |
| INT-SYM-089 | \eta | P2 §11,A | stopping rigidity | PARTIAL | C4 | upstreameta別 |
| INT-SYM-090 | S,S' (predicate) | P2 §2,3,D; EQF028 | hypothetical binary stop/revisedstop | EXPLICIT | C3 | P1stateS別 |
| INT-SYM-091 | \rho,\mathbf v (fluid) | P2 J §3; EQF042 | density/velocity analogy | PARTIAL | C4 | rhoi/Intspeed別 |
| INT-SYM-092 | j,k,... (network) | P2 §5,D | other-agent / iterate indices | PARTIAL | C2 | kiterateと区別 |
| INT-SYM-093 | DH / horizon | P1 §9; P2 §3,C | limit/unreachability vocabulary | UNRESOLVED | C4 | physicalhorizontypedmapNO |
| INT-SYM-094 | knowledge block/log/token | P2 §9,10; P1 §2 | social stopping/storage representations | UNRESOLVED | C4 | CTtokenformalobjectと同定NO |
| INT-SYM-095 | responsive/silent | P2 §4 | effective-channel classification | PARTIAL | C1 | ontologicalcategory否定 |
| INT-SYM-096 | homology/isomorphism | P2 §3,5,B,D,E | cross-domain role relation | UNRESOLVED | C5 | claimed≠definedbijection |
| INT-SYM-097 | \blacksquare | P2 J §3 | proof-end marker,notmodelvariable | EXPLICIT | C0 | not a theorem-validityflag |

Collision C0 harmless / C1 locally separated overload / C2 section ambiguity / C3 cross-Part / C4 cross-branch / C5 identity wording / C6 direct type-conflict candidate。これはnotation-risk分類であって循環性分類ではない。SYM036のCT Qは依存比較のboundary entryでありIntelligenceに新しいQoperatorを定義しない。p_iは圧力差の表記から独立定義を作らずNOT LOCATEDとした。

## 8. Operator/function inventory

| ID | Operator | EQF/reference | Definition status | Composition / inverse / iteration |
|---|---|---|---|---|
| INT-OP-001 | F P1 | 001 | ordered state update; concretefunctionnotgiven | iteration by order; inverseNO/composabilitypartial |
| INT-OP-002 | Fbio P1 | 045 | biological discreteupdate | P1Fexample; ODEtranslationNO |
| INT-OP-003 | Ftr | 009 | hidden-state layertransition | iteration layers; dimensions/weightsnotfullytyped |
| INT-OP-004 | F P2 | 025 | next inference; F1–4properties | xnrecurrence; Jcompositionpremise; inverseNO |
| INT-OP-005 | F set-valued | 048 | possiblecontinuations EN§2 | J(set)ruleNOTLOCATED |
| INT-OP-006 | Bio F(x;θ) | 046 | state-rate field comparison | ODEspelling; inferenceidentityguard |
| INT-OP-007 | F',F^k | 028/033 | internal-predicate repackaging / iterate notation | kdomain/compositionclosureNOTLOCATED |
| INT-OP-008 | Φ:S→R | 002 | explicitscalarfield | inverseNO; notemergenceoperator |
| INT-OP-009 | Φbio | 003 | explicitmap | noinverse/transfermap |
| INT-OP-010 | Φtr | 004 | explicitmap | noinverse/optimizationroutine |
| INT-OP-011 | f Physarum | 006/007 | responsefunction, JA powerexample | f&#124;Q&#124; input; noinverse |
| INT-OP-012 | f closure | 019–021 | JAmonotonic function/twoexamples | domain/rangeincomplete; notPhysarumf |
| INT-OP-013 | divergence | 011/017/042 | differentialoperator symbol | geometry/BCnotdeclared; threecontextsseparate |
| INT-OP-014 | gradient | 022/023/060 | differentialoperator symbol | geometry/metricnotdeclared |
| INT-OP-015 | F_I | 022 | effectiveforce relation, notupdateoperator | alpha∇C; noiteration |
| INT-OP-016 | C:X→[0,Cmax) | 024 | closure evaluationmap | noinverse/calibration |
| INT-OP-017 | Cij(H,ρ,λ) | 029 | explicitexponentialrelation | indexedscalar-like; range/parametersunfixed |
| INT-OP-018 | J:X→R | 047 | justificationfunction | strictincreasepremise; noinverse |
| INT-OP-019 | S:X→{0,1} | 028 | hypothetical internalpredicate | rejected-sourceargument; notadoptedstop |
| INT-OP-020 | Internal/External | 016/044 | prose boundary labels withmembership | operatorclassesnotdefined |
| INT-OP-021 | T | 016/044 | stoppingcondition/operator | signature/iteration/inversenotgiven |
| INT-OP-022 | U=Φ(L,H) | 031 | emergence schema | argumentrolesonly; nooperatorconstruction |
| INT-OP-023 | LE=Φ(LR,H) | 032 | intelligenceapplicationofschema | sameΦsignatureunestablished |
| INT-OP-024 | E[LE,xn] | 033 | external stoppingoperator constructionnotation | input/output/codomainnotfixed; E∉F^kclaim |
| INT-OP-025 | projection E-site | 054 | prose operation at H/θ | no projectionmap/idempotence/inverse |
| INT-OP-026 | Ωθ reconfiguration | 030 | (B)changesregion byθ | no transformationmap onspaces |
| INT-OP-027 | μθ | 037/054 | capacitynamed; notformalfunction | no updaterate/derivative |
| INT-OP-028 | Φext/Φnet identification | 034 | functional/structural equalityclaim | no forward/inverse typedmap |
| INT-OP-029 | E(A)/stoppingfunctionalminimum | 041 | importedenergyname / proposedstoppingfunctional | no Intfunctionalexpression,minimizerdomain |
| INT-OP-030 | Q token extraction | INT-HOMO009 | CTcomparison only | no IntlocalQdefinition |
| INT-OP-031 | graph growth | 014/015 | cardinality/branch expression | no graphgrowthoperator/rule |
| INT-OP-032 | environment↦E-site | 055 | operationaldescription ofanimism | not definedinput/outputmap |

## 9. Index / summation / graph structures

| ID | Index/structure | Source | Explicit / absent boundary |
|---|---|---|---|
| INT-INDEX-001 | i,j Physarum | P1§4–5 | node/edge indices named; cardinality,directedness notfixed; noEinsteinsummation |
| INT-INDEX-002 | i,ell Transformer | P1§5 | hidden-state/token andlayerlabels; dimensions/indexsetsunspecified |
| INT-INDEX-003 | i in I(si) | P1J§7 | i=1,2,... explicit; no commonmeasurable-stateindex |
| INT-INDEX-004 | V,E | P1§7 | vertex/edgecounts; simple/directed/dense assumptionsnotdeclared |
| INT-INDEX-005 | b,d | P1§7 | branchingfactor/depth; exact-vs-up-to-depth route countingunspecified |
| INT-INDEX-006 | t/t+1 | P1§3 | order recurrence; prose allowsdiscrete/continuous; no universalclock |
| INT-INDEX-007 | n,n+1 | P2§1–3 | inferenceiteration; initialx0shown notspecified data |
| INT-INDEX-008 | x∈X,x* | P2§3 | theoremquantification/fixedpointhypothesis; admissibilitynotindependentlyspecified |
| INT-INDEX-009 | i,j H/C/ρ | P2J§2,4,A | agent/environmentroles; no matrixdimensions,symmetryorsummationconvention |
| INT-INDEX-010 | j,k,... network | P2J§5,D | otheragents; graphupdate/edgeweightsnotfullyspecified |
| INT-INDEX-011 | k in {F^k} | P2§5,A | iterationpower; indexset/start/closureundercompositionnotgiven |
| INT-INDEX-012 | vector sum e | P2J§1,E | causalvectorclosure; trianglethreeindices; no generalindexset |
| INT-INDEX-013 | A/B | P2§2,3,A | movementclasses, not numericalindex |
| INT-INDEX-014 | LF/LR/LE | P2§2,5 | role/layernames, not sourceseriesindex or auditI0–I4 |

## 10. Domain/range ledger

| ID | Object/domain | Source/EQF | Status | Declared vs missing |
|---|---|---|---|---|
| INT-DOM-001 | P1 S | 043 | PARTIAL | connected states; discreteness allowed; cardinality/topology unspecified |
| INT-DOM-002 | P2 X | 024/047 | PARTIAL | inference-state domain; geometriclandscape language; metric未固定 |
| INT-DOM-003 | C | 024 | EXPLICIT | X→[0,Cmax) given; implementation/calibration別 |
| INT-DOM-004 | Cij | 029 | PARTIAL | agent/environmentindices, domain/rangeparametersnotfixed |
| INT-DOM-005 | I P1 | 010/013 | PARTIAL | I(s), accumulationrole; codomainnotgiven |
| INT-DOM-006 | I P2 | 019 | PARTIAL | f(1−C); fdomain/range andnormalizationnotfixed |
| INT-DOM-007 | Φ P1 | 002 | EXPLICIT | S→R |
| INT-DOM-008 | Φbio/Φtr | 003/004 | EXPLICIT | bothS→R, physicalcarriersdifferent |
| INT-DOM-009 | Φ emergence | 031/032 | UNRESOLVED | L,H inputs; U/LEoutputroles; no sharedspaces |
| INT-DOM-010 | F P1 | 001 | PARTIAL | state→state suggested notcomplete typedfunction |
| INT-DOM-011 | F P2 single/set | 025/048 | CONFLICTING | X states vs setcontinuations; no source powersetsignature |
| INT-DOM-012 | J flow | 011 | PARTIAL | divergenceimplies differentialflowrole; manifold/dimensionnotset |
| INT-DOM-013 | JC | 023 | PARTIAL | closuregradientflux; base/spacesnotset |
| INT-DOM-014 | J justification | 047 | EXPLICIT | X→R; notsameJflow |
| INT-DOM-015 | S predicate | 028 | EXPLICIT | X→{0,1}, counterfactualargument |
| INT-DOM-016 | Ωθ | 030 | PARTIAL | maintainableregion; embeddinginX notfullyformalized |
| INT-DOM-017 | Ωlife/Ωintel | 036 | UNRESOLVED | subsetclaimed; cross-domainambientspace/mapabsent |
| INT-DOM-018 | LF/LR/LE | 032/050 | PARTIAL | domain/motion/attractorroles; unifiedcategorynotgiven |
| INT-DOM-019 | E | 033 | UNRESOLVED | LE,xn construction; result/operatorcodomainunclear |
| INT-DOM-020 | μθ | 037/054 | PARTIAL | capacityforθmovement; interval/unitnotdefined |
| INT-DOM-021 | Φext/Φnet | 034 | UNRESOLVED | fieldvsnetwork; bijectionorcarrierabsent |
| INT-DOM-022 | Σ | 039 | PARTIAL | development/activityquantity; quantificationexplicitfuture |
| INT-DOM-023 | vinf,vLR,rres,η | 038/040 | PARTIAL | axes/ratesroles; numericdomains/bandsnotfixed |

## 11. Time/order ledger

| ID | Parameter | Source | Role / units / identity |
|---|---|---|---|
| INT-TIME-001 | t P1axiom | P1§3 | ordering; notnecessarilyexternalclock; t+1 recurrence |
| INT-TIME-002 | t Physarum | P1§4 | continuousconductance-time derivative; unitsnotformalized |
| INT-TIME-003 | t Transformer vs ell | P1§5 | layer/order; notphysarumclock |
| INT-TIME-004 | n P2 | P2§1–3 | discreteinferenceiteration; n→t/tau calibrationnotprovided |
| INT-TIME-005 | τ P2 | P2J§1,A | internalorderindependentofobservationtime; no commonclock |
| INT-TIME-006 | t BioODE | P2J§1–2 | biologicalstate-evolutioncomparison; no inference-clocktranslation |
| INT-TIME-007 | t fluid | P2J§3 | continuityanalogyonly |
| INT-TIME-008 | TΦ,tn,Δv Con | P1§9; P2§11 | comparativetimescale/window; Intidentitynotdeclared |
| INT-TIME-009 | vinf/vLR timescale | P2§11,A | stepfrequency/lograte; commoncount/timeconventionnotcomplete |
| INT-TIME-010 | θ evolutionary timescale | P2JA A | generation-spanning qualitativecomparison |
| INT-TIME-011 | θ environmental timescale | P2JA A | passiveenvironmentalchange; numericclockabsent |
| INT-TIME-012 | θ endogenous timescale | P2JA A | individual/dialoguehistory; no adoptedtimeconstant |

## 12. Units / dimensional status

EQF001–063のunit欄をfamily-level inventoryとする（63/63）。explicit physical unit付きのcomplete equation signatureは未確認。dimensionless宣言も未確認。以下は必要なcompatibilityの所在を示すだけで、単位を割り当てない。

- Q/D/L/Δpとconductance derivative/f responseの単位整合、powerμは指数で正値例だがnormalizationは未記載。
- closure PDEではtime derivative、divergence、aΔ、ΓC、barrierの加算整合が必要。C/Cmaxの数字上限を1と補わない。
- expのλρH argument、α∇C、ξ∇Cのcompatibilityが必要。係数の単位・sign・rangeを外から補わない。
- Φ:S→Rはreal-valued宣言であり無次元宣言でない。U=Φ(L,H)はmapのkindが未固定なのでunitcheck以前のsignature境界。
- vinfのstep/timeというrelative rate roleとvLRの速度差式は共通較正を意味しない。rres/η/μθ/Σは概念的・effective役割、数値単位未指定。
- E(A)はupstream functional名、Int停止functionalはfuture/proposalとappendixpresent-tenseを分け、energyunitsをIntへ移さない。

## 13. Definition-to-equation crosswalk

| ID | Phase00 definition | Term | Source | Support form | EQF / limit |
|---|---|---|---|---|---|
| INT-DEFEQ-001 | INT-DEF-001 | perception=input availability | P1 §2 | prose only | — |
| INT-DEFEQ-002 | INT-DEF-002 | recognition=existing structureへのmapping | P1 §2 | prose only | — |
| INT-DEFEQ-003 | INT-DEF-003 | knowledge=stopping structure | P1 §2 | prose only | — |
| INT-DEFEQ-004 | INT-DEF-004 | intelligence=ongoing revisable motion | P1 §1–2 | prose only | 001–002 not definition-equivalence |
| INT-DEFEQ-005 | INT-DEF-005 | connected S | P1 §3 | mixed | 043; connectivityprose |
| INT-DEFEQ-006 | INT-DEF-006 | temporal ordering | P1 §3 | mixed | 001; time/orderprose |
| INT-DEFEQ-007 | INT-DEF-007 | global Φ:S→R | P1 §3 | explicit equation | 002 |
| INT-DEFEQ-008 | INT-DEF-008 | I accumulation density | P1 §4 | mixed | 010,013 |
| INT-DEFEQ-009 | INT-DEF-009 | J direction/flow | P1 §4 | mixed | 011 |
| INT-DEFEQ-010 | INT-DEF-010 | Φ normative-neutral bias | P1 §4 | mixed | 002 |
| INT-DEFEQ-011 | INT-DEF-011 | interruption vs stopping | P1 §8 | prose only | 044 boundarynotation別 |
| INT-DEFEQ-012 | INT-DEF-012 | differential horizon of intelligence | P1 §9 | mixed | 016/044 |
| INT-DEFEQ-013 | INT-DEF-013 | C operational stability not truth | P2 §1 | mixed | 024/049 |
| INT-DEFEQ-014 | INT-DEF-014 | C-landscape (X,C) | P2 §1 | explicit equation | 024 |
| INT-DEFEQ-015 | INT-DEF-015 | Ωθ / θ | P2 §1 | mixed | 030 |
| INT-DEFEQ-016 | INT-DEF-016 | emergence U=Φ(L,H) | P2 J definition1.1; E§1 | explicit equation | 031 |
| INT-DEFEQ-017 | INT-DEF-017 | inference F / LF | P2 §2 | mixed | 025/048/050 |
| INT-DEFEQ-018 | INT-DEF-018 | justification J:X→R | P2 E §2; J §3 | explicit equation | 026/047 |
| INT-DEFEQ-019 | INT-DEF-019 | μθ threshold mobility | P2 J2.3; E§1,2 | prose only | 037/054 linksnotcapacityformula |
| INT-DEFEQ-020 | INT-DEF-020 | movement A/B | P2 §2 | prose only | 030; Aformaldefinitions |
| INT-DEFEQ-021 | INT-DEF-021 | responsive/silent worlds | P2 §4 | mixed | 035 |
| INT-DEFEQ-022 | INT-DEF-022 | LR=trace + recursive reference | P2 J5.1; E§5 | prose only | 032inputrole |
| INT-DEFEQ-023 | INT-DEF-023 | LE=externally dependent stopping attractor | P2 J5.2 / E5.1 | mixed | 032 |
| INT-DEFEQ-024 | INT-DEF-024 | external E | P2 J5.3; E§5 | explicit equation | 033 |
| INT-DEFEQ-025 | INT-DEF-025 | Φext / Φnet | P2 §5 | mixed | 034 |
| INT-DEFEQ-026 | INT-DEF-026 | animism | P2 J6.1; E§6 | mixed | 055 |
| INT-DEFEQ-027 | INT-DEF-027 | God: unresolved→suspended | P2 J7.1; E§7 | mixed | 056/058; negativeidentitiesnotpositiveoperator |
| INT-DEFEQ-028 | INT-DEF-028 | religion | P2 §8 | mixed | 057 |
| INT-DEFEQ-029 | INT-DEF-029 | social blockchain | P2 §9 | prose only | noledgerconsensusalgorithm |
| INT-DEFEQ-030 | INT-DEF-030 | knowledge provisional block | P2 J10.1 | prose only | no empiricalcriterion |
| INT-DEFEQ-031 | INT-DEF-031 | Σ / speed-resolution-stiffness | P2 §11,A | mixed | 039 separateddevelopment;040axisroles |
| INT-DEFEQ-032 | INT-DEF-032 | general vs sapiens intelligence | P2 §12 | prose only | N/R/Sclauses notnumericalcriterion |

## 14. Theorem / proposition / theorem-like claims

| ID | Statement family | Source | Premises named | Conclusion | Source proof type | Language/scope |
|---|---|---|---|---|---|---|
| INT-THM-001 | Non-Closure Theorem3.1 | P2 EN/JA§3; J D.1 | P1 justificationextension;P2 strictJ; scopeP3fixedθ/A | noFfixedpoint | contradiction sketch | EN/JAformula shared;J D repeats; no proof-validityjudgment |
| INT-THM-002 | internal stoppingpredicate cor3.2 | P2 J§3,D.2; EN§3Consequence | T3.1; hypotheticalS; stopjudgment→fixedpoint; S-as-F' | internalS cannotbecompleted; regress | prose argument / contradiction sketch | JAexplicitcorollary;ENshortconsequence |
| INT-THM-003 | Cmax/horizonisomorphism cor3.3 | P2 J§3,D.3 | barrierdivergence+claimedunreachability;T3.1;cor3.2 | same structural/dynamical proposition | table + prose argument | JAexplicit;ENtheorembodydoesnotincludePDEproof |
| INT-THM-004 | individualclosure cor3.4 | P2 J§3,D.4; EN§3 | T3.1+cor3.2; LF-onlyscope | individualLFalonecannotclose | prose argument | LR/LEwhole stopnotexcluded |
| INT-THM-005 | VEDemergence definition1.1 three-caseverification | P2 J§1,D.5,E | lowerLmotion+H; particle/Bio/Intcases | threeexamples satisfyU=Phi(L,H) | appendix-only comparison sketch | calleddefinition/verification; notnewformaltheorem |
| INT-THM-006 | Φext≡Φnet claim5.4 | P2§5; JA D.6,A | functionalexternalview;networkofindividualLE | same structure/isomorphism | prose argument / appendix sketch | ENpresentclaim;JAexpandsdefinitions |
| INT-THM-007 | three-layer architecture cor5.5 | P2 J§5; EN§5summary | LFnonclosure; LRtrace; LEexternallydependent | intelligence architectureLF/LR/LE | prose argument | numberedJA; noindependentformalproofblock |
| INT-THM-008 | error tolerance↔μθ equivalence | P2 J§10,D.7 | μ=endogenousθchange; revisable stop | bidirectionalstructuralequivalence | two-direction prose sketch | ENhasfallibilitydiscussionnotfullJAsketch |
| INT-THM-009 | LElocalminimum stoppingfunctional | P2 JA E; §13future | energy/attractorcomparison; functionalnotexplicit | LEaslocalminimum | appendix-only assertion | bodyfutureformulation/appendixpresenttense |
| INT-THM-010 | Σ/speed phase-regime necessity | P2§11–12 | vinf,rres,eta; internal/externalstop; μroles | qualitativeregion andnecessaryconditions | prose argument | notlabeledtheorem; Σnotphaseregionset |
| INT-THM-011 | P1nointernalstop/differentialhorizon | P1§8–9 | inference/correctness expansion; Rboundary | T notInternal(R), T inExternal(R) | prose argument | P2formalizationclaimed; noP1theoremenvironment |
| INT-THM-012 | threshold-dependent dichotomy claim2.2 | P2J§2.6:118;§4.3;EN§4prose | Hparameter + (vinf,rres,eta), same environment | responsive/silent arecontinuous thresholdregimes notontologicalkinds | prose argument | explicitJAclaimnumber; numericthresholdnotgiven |
| INT-THM-013 | silent-world regress conditional | P2J§4.4:65–79;EN§4 | no response; justificationonlyinference; noinferredstop | regress forsubjectfixedinsilentregime | prose argument | three numberedconditions JA; notuniversalall-environmentsclaim |

## 15. Theorem-premise inventory

| ID | Theorem family | Locator | Source premise/excerpt | Status |
|---|---|---|---|---|
| INT-PREM-001 | THM001 | P2E§3P1 | The inference operator $F$ sends a state $x_n$ to a more justified state $x_{n+1}=F(x_n)$. | EXPLICIT |
| INT-PREM-002 | THM001 | P2J§3P1 | $F$ は状態 $x_n$ から、より正当化された状態 $x_{n+1}$ への遷移を生成する。 | EXPLICIT |
| INT-PREM-003 | THM001 | P2J§3P2 | ある測度 $J: \mathcal{X} \to \mathbb{R}$ が存在し、$F$ の作用によって単調に増大する。 | EXPLICIT |
| INT-PREM-004 | THM001 | P2EN/JA§3P2; JD.1 | J(F(x)) > J(x); any/admissible states | EXPLICIT; exact rawoccurrence§2 |
| INT-PREM-005 | THM001 | P2E§3P3 | The argument is made within a fixed movement region $\Omega_\theta$. It concerns movement type (A), not reconfiguration type (B). | EXPLICIT |
| INT-PREM-006 | THM001 | P2J§3P3 | $\theta$ 自体の組み替え (B) は本章の射程外であり、\S{}5 で扱われる。 | EXPLICIT |
| INT-PREM-007 | THM001 | P2J§3P3 | same dynamicsやtyped translationは導かれない | EXPLICIT guard; upstreamcorrespondencealsoinP3 |
| INT-PREM-008 | THM001 | P2§3; JD.1 | F(x*)=x*, x*∈X | EXPLICIT counterfactual; notadoptedexistence |
| INT-PREM-009 | THM002 | P2J§3; D.2 | $S(x) = 1$ となる状態 $x$ は、これ以上推論を進める必要がない | EXPLICIT |
| INT-PREM-010 | THM002 | P2JD.2 | これは $F(x) = x$ を意味し、定理 3.1 に矛盾する。 | EXPLICIT source transition; independentrelationnotadded |
| INT-PREM-011 | THM002 | P2JD.2 | $F'$ 自体が推論演算子であり、定理 3.1 が適用される。 | EXPLICIT assertion; P1/P2forF'notseparatelylisted |
| INT-PREM-012 | THM003 | P2JD.3 | $-\kappa_B/(C_{max} - C)$ は $C \to C_{max}$ で発散し、完全閉包への到達を動力学的に禁じる。 | EXPLICIT source assertion; no auditendorsement |
| INT-PREM-013 | THM003 | P2JD.3 | 両者は別領域の現象だが、同一の動力学的命題の層別表現である。 | EXPLICIT tableconclusion; typedmapNOTLOCATED |
| INT-PREM-014 | THM004 | P2JD.4 | 定理 3.1 により $L_F$ に内部不動点はない。系 3.2 により内部停止述語も定義できない。 | EXPLICIT |
| INT-PREM-015 | THM004 | P2JD.4 | ただし $L_R$ と $L_E$ を含む三層全体では外部依存的に閉じうる | EXPLICIT qualification |
| INT-PREM-016 | THM005 | P2JD.5 | \mathcal{U} = \Phi(\mathcal{L}\text{の運動}, H_{ij}) | EXPLICIT source schema |
| INT-PREM-017 | THM005 | P2JD.5 particle | 閉包条件 $\sum \vec{e} \approx 0$、閉包エネルギー汎関数 $E(A)$ | EXPLICIT citedinput; nofunctionaldefinitionhere |
| INT-PREM-018 | THM005 | P2JD.5 Bio | 生命のoperational criterionとtyped mappingはOPENである。 | EXPLICIT guard |
| INT-PREM-019 | THM005 | P2JD.5 Int | $L_R$ の運動は $L_E$ を論理的には含意しない | EXPLICIT non-deductionguard |
| INT-PREM-020 | THM006 | P2JD.6 | 個体が停止を委ねる外部の共通参照基盤 | EXPLICIT functionaldefinition |
| INT-PREM-021 | THM006 | P2JD.6 | 複数の個体が各自の内部に持つ $L_E$ が、相互干渉によって形成するネットワーク | EXPLICIT structuraldefinition |
| INT-PREM-022 | THM007 | P2J§5 | LF/LR/LE three-layer definitions and externaldependence | EXPLICIT prose prerequisites; no extraequationpremise |
| INT-PREM-023 | THM008 | P2JD.7 forward | $\mu_\theta$ は $\theta$ を動かす能力(領域組み替え (B))。 | EXPLICIT |
| INT-PREM-024 | THM008 | P2JD.7 reverse | 誤り許容性は「停止が後に改訂されうること」を前提とする。 | EXPLICIT |
| INT-PREM-025 | THM008 | P2JD.7 reverse | これは $\theta$ の変化(新しい停止条件の下での再評価)を要求する。 | EXPLICIT assertedtransition |
| INT-PREM-026 | THM009 | P2J E; §13 | stopping functional/local minimum; future explicit formalization | NOT LOCATED explicitfunctional/domain/minimumcriterion |
| INT-PREM-027 | THM010 | P2§11 | v_inf,vLR,rres,eta axes andstoppingroles | EXPLICIT qualitativepremises; numericbandboundsNOTLOCATED |
| INT-PREM-028 | THM011 | P1§8–9 | internal justification continues; interruption ≠ stopping | EXPLICIT prose; formalInternal/ExternalclassNOTLOCATED |
| INT-PREM-029 | THM012 | P2J§2.6:121 | 同一の環境が、相互拘束 $H_{ij}$ のパラメータ位置と、推論主体の $(v_{\text{inf}}, r_{\text{res}}, \eta)$ の組によって、応答的にも沈黙的にも現れる。 | EXPLICIT |
| INT-PREM-030 | THM013 | P2J§4.4:69 | 環境が応答を返さない(沈黙性、$H_{ji} \approx 0$)。 | EXPLICIT condition1 |
| INT-PREM-031 | THM013 | P2J§4.4:71 | 正当化は推論によってのみ生成される(\S{}3 の前提 P2)。 | EXPLICIT condition2; sourceattributesP2; exactstrengthcomparelater |
| INT-PREM-032 | THM013 | P2J§4.4:73 | 停止は推論から導出できない(\S{}3 の定理 3.1、系 3.2)。 | EXPLICIT condition3 |
| INT-PREM-033 | F definition | P2J§2.1 F1–F4 | 既存概念地景内操作 / 確率的 / 反復可能 / 局所的に正当化 | EXPLICIT propertyfamily; these do notautomaticallysupplyT3.1strictJ |
| INT-PREM-034 | THM012 | P2J§2.6:128 | VED は静的な範疇ではなく運動を基底に置く。 | EXPLICIT groundingprose; notnewnumericthreshold |

## 16. Proof-step inventory (no proof evaluation)

| ID | THM | Source | Step/transition | Presence |
|---|---|---|---|---|
| INT-PROOFSTEP-001 | 001 | EN/JA§3,D.1 | assume x*∈X and F(x*)=x* | EXPLICIT |
| INT-PROOFSTEP-002 | 001 | EN/JA§3,D.1 | invoke strictJ on admissiblex | EXPLICIT |
| INT-PROOFSTEP-003 | 001 | EN/JA§3,D.1 | substitute x=x* | EXPLICIT |
| INT-PROOFSTEP-004 | 001 | EN/JA§3,D.1 | replace F(x*) byx* to J(x*)>J(x*) | EXPLICIT |
| INT-PROOFSTEP-005 | 001 | EN/JA§3,D.1 | state contradiction and nofixedpoint | EXPLICIT |
| INT-PROOFSTEP-006 | 001 | EN§2→§3 | set-valuedcontinuation contract→J(Fx) scalar argument | NOT LOCATED bridgingrule; notfilled |
| INT-PROOFSTEP-007 | 002 | JA§3,D.2 | suppose internalS:X→{0,1} | EXPLICIT |
| INT-PROOFSTEP-008 | 002 | JA§3,D.2 | Sx=1 interpreted nofurtherinference→Fx=x | EXPLICIT assertion; separateequivalenceformalizationNOTLOCATED |
| INT-PROOFSTEP-009 | 002 | JA§3,D.2 | invokeT3.1 contradiction | EXPLICIT |
| INT-PROOFSTEP-010 | 002 | JA§3,D.2 | recastS asF' and invokeT3.1again | EXPLICIT; F'premiseverificationNOTLOCATED |
| INT-PROOFSTEP-011 | 002 | JA§3,D.2 | newS' required andchainnontermination | EXPLICIT conclusion |
| INT-PROOFSTEP-012 | 003 | JA§3,D.3 | reciprocalbarrierdiverges atbound | EXPLICIT |
| INT-PROOFSTEP-013 | 003 | JA§3,D.3 | divergence→dynamicinaccessibility | EXPLICIT assertion; evolution/BCproofNOTLOCATED |
| INT-PROOFSTEP-014 | 003 | JA§3,D.3 | pairbarrier/regress,Ω/operationregion,Cmax/nofixedpoint | EXPLICIT table |
| INT-PROOFSTEP-015 | 003 | JA§3,D.3 | conclude same dynamicalproposition/isomorphism | EXPLICIT; typedmap/inverseNOTLOCATED |
| INT-PROOFSTEP-016 | 004 | JA§3,D.4 | combineT3.1andC3.2 | EXPLICIT |
| INT-PROOFSTEP-017 | 004 | JA§3,D.4 | stopmustoutsideLF; identifyouterstructureLE | EXPLICIT prose; uniqueexhaustionargumentNOTLOCATED |
| INT-PROOFSTEP-018 | 004 | JA§3,D.4 | qualifyLFalone vs three-layerwhole | EXPLICIT |
| INT-PROOFSTEP-019 | 005 | JA D.5/E | instantiateL,H,U particlecase | EXPLICIT roleassignment |
| INT-PROOFSTEP-020 | 005 | JA D.5/E | instantiateBio case withoperational/typedOPENguard | EXPLICIT |
| INT-PROOFSTEP-021 | 005 | JA D.5/E | instantiateInt LR/H/LE case; μ/B emergence | EXPLICIT; updatedynamicsNOTLOCATED |
| INT-PROOFSTEP-022 | 005 | JA D.5/E | claimallthree shareform | EXPLICIT; commontypedoperatorNOTLOCATED |
| INT-PROOFSTEP-023 | 006 | JA§5,D.6 | defineexternalfunctionalview | EXPLICIT |
| INT-PROOFSTEP-024 | 006 | JA§5,D.6 | definenetwork structuralview | EXPLICIT |
| INT-PROOFSTEP-025 | 006 | JA§5,D.6 | observeri referencesotherj,k LEinteractions | EXPLICIT |
| INT-PROOFSTEP-026 | 006 | JA§5,D.6 | identifyviews as same structure | EXPLICIT; mapping/inverseconstructionNOTLOCATED |
| INT-PROOFSTEP-027 | 007 | JA§5 | assemble LFmotion LRrecursion LEexternalstop | EXPLICIT |
| INT-PROOFSTEP-028 | 007 | JA§5 | statearchitecturecorollary | EXPLICIT prose; independentproofblockNOTLOCATED |
| INT-PROOFSTEP-029 | 008 | JA D.7 forward | μ→θmovement→nonfinalstop→revisability→fallibility | EXPLICIT chain |
| INT-PROOFSTEP-030 | 008 | JA D.7 reverse | errortolerance→revisablestop→reassessment→θchange→μ | EXPLICIT chain |
| INT-PROOFSTEP-031 | 008 | JA D.7 | endwith structural equivalence | EXPLICIT; independentpredicatetypingNOTLOCATED |
| INT-PROOFSTEP-032 | 009 | JA E | compareVEDenergyminimum/LEstoppingminimum | EXPLICIT prose; functionalconstructionNOTLOCATED |
| INT-PROOFSTEP-033 | 010 | EN/JA§11–12 | classify threequalitativebands +zero-motion | EXPLICIT |
| INT-PROOFSTEP-034 | 010 | EN/JA§11–12 | necessary/failure-regime conclusions | EXPLICIT prose; numericalphaseboundary derivationNOTLOCATED |
| INT-PROOFSTEP-035 | 011 | P1§8–9 | internalextension→nointernalT→externalT | EXPLICIT prose/notation |
| INT-PROOFSTEP-036 | 011 | P1→P2 | P1T/R identificationwithP2S/E/X | NOT LOCATED typedtranslation |
| INT-PROOFSTEP-037 | 012 | JA§2.6/§4.3 | same environment/H+axes settings→differentresponse→movingthreshold | EXPLICIT qualitativeargument; thresholdfunctionNOTLOCATED |
| INT-PROOFSTEP-038 | 013 | JA§4.4 | condition1 removesexternalresponse | EXPLICIT |
| INT-PROOFSTEP-039 | 013 | JA§4.4 | condition2requirescontinuedinference;condition3excludesinternalstop | EXPLICIT |
| INT-PROOFSTEP-040 | 013 | JA§4.4 | no stoppingmeans→infinite regress | EXPLICIT proseconclusion; no additionaldynamics supplied |

## 17. EN/JA formal variants

| ID | Family | Classification | Locator | Difference |
|---|---|---|---|---|
| INT-FVAR-001 | P1 state S/Φ axiom | SAME | §3 | sameenumeration/map; Japaneseprosenotnewtype |
| INT-FVAR-002 | P1 update/order | SAME | §3 | same s(t+1)=F(s(t)); tinterpretationpreserved |
| INT-FVAR-003 | P1 PhysarumQ,D | SAME | §4 | sameflow/conductanceformula |
| INT-FVAR-004 | P1 powerresponse | JA ONLY | J§4 | f(Q)=absQ^μ μ>0extraexample |
| INT-FVAR-005 | P1 Transformerhiddenstates | SAME | §5 | same indexedstatefamily |
| INT-FVAR-006 | P1 biologicalFbio | JA ONLY | J§5 | discreteFbioinline; ENprose lessformal |
| INT-FVAR-007 | P1 I/divJ/correctness | DIFFERENT FORMULATION | §7 | bothlanguagescarrythreecoredisplays; JAaddsindexedI(si) andtextannotations |
| INT-FVAR-008 | P1 branch counts | DIFFERENT FORMULATION | §7 | sameedge/b^d motif; sourceexplanation anddisplayplacementdiffer |
| INT-FVAR-009 | P1 internalT | SAME | §8–9 | bothlanguageshaveTnotInternaldisplays; JAuses$$ inadditionaldelimiterpositions; no semanticJA-onlyclaim |
| INT-FVAR-010 | P1 externalT | SAME | §9 | sameexternalmembership; Internal/External typography/delimitersdiffer |
| INT-FVAR-011 | P1 horizon/Consymbols | DIFFERENT FORMULATION | §9 | JAexpandedparameterroles; no commonclock |
| INT-FVAR-012 | P2 closure PDE | JA ONLY | J§1,3 | ENsummary/table retainsrelations notfullPDEdisplay |
| INT-FVAR-013 | P2 C-range mapping | JA ONLY | J§1 | explicitC:X→range; ENroleprose |
| INT-FVAR-014 | P2 f examples | JA ONLY | J§1 | linear/log examples absentENformula |
| INT-FVAR-015 | P2 FI/JC | JA ONLY | J§1,3,A | closuregradient/fluxexplicitrelationsmoreextensive |
| INT-FVAR-016 | P2 Fsingle/set | EN ONLY | E§2 | explicitset-valuedalternative; JAupdatedisplay single |
| INT-FVAR-017 | P2 Jsignature | SAME | E§2/J§3 | X→R explicitlyboth; placementdifferent |
| INT-FVAR-018 | P2 T3.1statement | SAME | §3 | strictincrease/no-fixedpoint; delimiter/quantifierformat retained |
| INT-FVAR-019 | P2 P3 | DIFFERENT FORMULATION | §3 | bothfixedθ/A; JAupstreamgroundingadditionalguardedrole |
| INT-FVAR-020 | P2 internalS corollary | JA STRONGER | J§3,D | namedcor3.2withregresssketch; ENconsequenceprose |
| INT-FVAR-021 | P2 Cmaxisomorphism | JA STRONGER | J§3,D | namedcor3.3plusPDE/inaccessibilitysameproposition |
| INT-FVAR-022 | P2 individualclosure | JA STRONGER | J§3,D | namedcor3.4plusnecessaryattractorwording |
| INT-FVAR-023 | P2 Cij relation | JA ONLY | J§2,A | exponentialindexedrelation |
| INT-FVAR-024 | P2 Ω subset | JA ONLY | J§1 | Ωintel⊂Ωlife |
| INT-FVAR-025 | P2 U/LE schema | DIFFERENT FORMULATION | §1,5,E | U/calU L/calL textmotion variants; no forcednormalization |
| INT-FVAR-026 | P2 E andPhiidentity | SAME | §5 | samecoreexpressions; JAadditionalDsketch |
| INT-FVAR-027 | P2 μ/errortolerance | JA STRONGER | J§10,D | explicitbidirectionalequivalence vsENrevisabilitydiscussion |
| INT-FVAR-028 | AppendixD | DIFFERENT FORMULATION | D | ENoptionalnotes;JAsevenproofsketches nottranslationparity |
| INT-FVAR-029 | AppendixB | JA ONLY | B | extraCTcolumn/θtimescale/Fcomparison tables |
| INT-FVAR-030 | AppendixE | DIFFERENT FORMULATION | E | JAcausalvectors/energy/stoppingminimum;ENshortemergencehomology |
| INT-FVAR-031 | MasterΣ | JA ONLY | A | development/activityquantity; notENtableentry |
| INT-FVAR-032 | phase speedgap | SAME | §11 | Delta vintel subtractionshared; clocksnotfixed |
| INT-FVAR-033 | masterprincipalrelations | JA ONLY | A | fiveextraformula-summarydisplays |
| INT-FVAR-034 | fluidcontinuityanalogy | JA ONLY | J§3 | inlineρ,v,tcomparison notadoptedPDE |
| INT-FVAR-035 | C=truthnegation | EN ONLY | E§10 | negateddisplay representation; JAdenialinprose |
| INT-FVAR-036 | P1 Φbio mapdisplay | JA ONLY | J§5 | explicitΦbio:S→R displayJA; ENbiologicalglobalbiasprose, no matchingdisplay |

## 18. Body / appendix formal relation

| ID | Appendix/role | Body relation | Formal content / boundary |
|---|---|---|---|
| INT-APPFORM-001 | A ENsymboltable | §1–13names | 17rows; primaryJAstatusnottransfer; source-mapnotproof |
| INT-APPFORM-002 | A JA v2.1rows | §1–3 | 10reprinted-attributionrows; exactv2.1artifactnotfixed |
| INT-APPFORM-003 | A JA v2.2rows | §2,4,5,11 | 14additionalrows; Σfuturequantity included |
| INT-APPFORM-004 | A JA A/Bdefinitions | §2.7,3P3,5 | formalproseclassification, nottypedregionoperator |
| INT-APPFORM-005 | A JA fiveformula summaries | §1,2,5 | LE/E/Phiidentity/mechanismarrow/basicrelations; presentestablishedwording |
| INT-APPFORM-006 | A JA timescaletable | §2/B.4 | θsameprincipleclaim across3timescales; no timeconversion |
| INT-APPFORM-007 | B homologytables | §1–5,9 | JAextraCT/θ/F/profiles; no newtypedinverse |
| INT-APPFORM-008 | B ENkernelarrow | §13/E | incompleteclosure→attractor→sustaineddynamicsdisplay; crossdomainnotupdate |
| INT-APPFORM-009 | C PartI mapping | P1axioms/stop/DH | re-descriptionalignment; no formalP1T→P2Econversion |
| INT-APPFORM-010 | D JA T3.1/cor3.2–4 | §3 | 4dedicatedsketches, nofullformalproofsystemclaimed |
| INT-APPFORM-011 | D JA emergence/identity/equivalence | §1,5,10 | 3additionalsketches; typingboundaryseparate |
| INT-APPFORM-012 | D ENoptionalnotes | §5,11–13 | differentcontentfromJAproofcollection; no automaticEnglishproofauthority |
| INT-APPFORM-013 | E emergence/energy | §1,5,13 | U/calU, causaltriangle, E(A)localminimum, LEstoppingfunctionalminimum |
| INT-APPFORM-014 | E present vsfuture | §13 | stoppingfunctionalfutureinbody vsminimumdescriptionappendix; recordAUTH/TYPEuncertainty |

## 19. Master Table row-by-row inventory

| ID | Language | Exact locator | Raw row (cells separated by &) | Claimed origin | Type/unit/signature | Provenance |
|---|---|---|---|---|---|---|
| INT-MASTER-001 | P2AE | intelligence-part2/appendices/appendix_a_master_table.tex:15 | $C$ & closure degree & operational stability, not truth | Masterv2.2summary | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-002 | P2AE | intelligence-part2/appendices/appendix_a_master_table.tex:16 | $C_{\max}$ & complete closure limit & unattainable boundary of closure | Masterv2.2summary | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-003 | P2AE | intelligence-part2/appendices/appendix_a_master_table.tex:17 | $I$ & information-field drive & drive generated by non-closure | Masterv2.2summary | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-004 | P2AE | intelligence-part2/appendices/appendix_a_master_table.tex:18 | $F$ & inference operator & advances inferential states | Masterv2.2summary | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-005 | P2AE | intelligence-part2/appendices/appendix_a_master_table.tex:19 | $L_F$ & inference layer & layer on which $F$ operates | Masterv2.2summary | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-006 | P2AE | intelligence-part2/appendices/appendix_a_master_table.tex:20 | $L_R$ & log layer & recursive reference to traces of inference | Masterv2.2summary | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-007 | P2AE | intelligence-part2/appendices/appendix_a_master_table.tex:21 | $L_E$ & emergent stopping layer & externally dependent stopping attractor | Masterv2.2summary | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-008 | P2AE | intelligence-part2/appendices/appendix_a_master_table.tex:22 | $E$ & external stopping operator & stopping action supplied through $L_E$ | Masterv2.2summary | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-009 | P2AE | intelligence-part2/appendices/appendix_a_master_table.tex:23 | $H_{ij}$ & mutual constraint & coupling between agents or agent and environment | Masterv2.2summary | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-010 | P2AE | intelligence-part2/appendices/appendix_a_master_table.tex:24 | $\theta$ & constraint parameter & parameter defining $\Omega_\theta$ | Masterv2.2summary | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-011 | P2AE | intelligence-part2/appendices/appendix_a_master_table.tex:25 | $\Omega_\theta$ & movement region & region in which inference can move | Masterv2.2summary | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-012 | P2AE | intelligence-part2/appendices/appendix_a_master_table.tex:26 | $\mu_\theta$ & threshold mobility & ability to reorganize $\Omega_\theta$ and stopping loci | Masterv2.2summary | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-013 | P2AE | intelligence-part2/appendices/appendix_a_master_table.tex:27 | $\Phi_{\text{ext}}$ & external reference field & field as it appears to an individual | Masterv2.2summary | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-014 | P2AE | intelligence-part2/appendices/appendix_a_master_table.tex:28 | $\Phi_{\text{net}}$ & stopping network & inter-individual network of $L_E$ layers | Masterv2.2summary | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-015 | P2AE | intelligence-part2/appendices/appendix_a_master_table.tex:29 | $v_{\text{inf}}$ & inference velocity & speed of inferential generation | Masterv2.2summary | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-016 | P2AE | intelligence-part2/appendices/appendix_a_master_table.tex:30 | $r_{\text{res}}$ & resolution & fineness of distinctions | Masterv2.2summary | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-017 | P2AE | intelligence-part2/appendices/appendix_a_master_table.tex:31 | $\eta$ & stopping hardness & rigidity or revisability of stopping | Masterv2.2summary | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-018 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:24 | $C$ & 閉包度 & 因果ログの閉包度 & 推論状態の安定化度(真理測度ではない) | v2.1 reprint claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-019 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:25 | $C_{max}$ & 完全閉包 & 到達不能な上限 & 「完全な理解/最終的判断」の構造的不到達性 | v2.1 reprint claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-020 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:26 | $\nabla C$ & 閉包度勾配 & 空間的閉包度差 & 推論の駆動力の方向と強度 | v2.1 reprint claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-021 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:27 | $J_C$ & 閉包度流れ場 & $J_C = -\xi \nabla C$ & 推論の流れ方向 | v2.1 reprint claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-022 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:28 | $I$ & 情報場 & $I = f(1-C)$ & 未閉包性の場。閉包が進むほど減少 | v2.1 reprint claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-023 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:29 | $F_I$ & 情報力 & $F_I = \alpha \nabla C$ & 推論駆動力。$\nabla C$ に沿った推論の押し出し力 | v2.1 reprint claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-024 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:30 | $\Omega_\theta$ & 準閉包 & $\theta$ で特徴づけられる安定維持可能領域 & 操作可能推論領域 | v2.1 reprint claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-025 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:31 | $\theta$ & 拘束パラメータ & 準閉包 $\Omega_\theta$ を特徴づけるパラメータ集合 & 運動可能領域を画定し生成に構造を与える拘束。生命層では DNA・知性層では推論操作の拘束 | v2.1 reprint claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-026 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:32 | $H_{ij}$ & 相互拘束 & $C_{ij} = 1-\exp(-\lambda \rho_i H_{ij})$ & 推論主体と環境の相互拘束。応答性閾値を決める | v2.1 reprint claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-027 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:33 | $\tau$ & 内的時間 & 観測時間とは独立な内的順序パラメータ & 推論の進行を測る内的時間 | v2.1 reprint claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-028 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:56 | $F$ & 推論演算子 & \S{}2.1 & 正当化拡張作用素。$x_{n+1} = F(x_n)$。VED/Bio-IFGT の流れ・状態発展演算子と類似した形式的役割を持つが、source-localでありsame dynamicsやtyped identityを意味しない | v2.2 addition claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-029 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:57 | $J$ & 正当化測度 & \S{}3.1 & $F$ の作用による正当化の進行を測る測度。$J(F(x)) > J(x)$ が成立(前提 P2) | v2.2 addition claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-030 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:58 | $L_F$ & 推論層 & \S{}2.3 & $F$ の作用域全体。推論軌道を含む。内部停止条件を持たない(定理 3.1) | v2.2 addition claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-031 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:59 | $L_R$ & ログ層 & \S{}5.2 & $L_F$ の運動の痕跡(ログ)への再帰参照運動の層。$L_E$ 創発の基盤。所在は系によって異なる(個体内・環境外部化・凍結) | v2.2 addition claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-032 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:60 | $L_E$ & 創発停止層 & \S{}5.3 & $L_R$ の再帰運動と外部相互拘束 $H_{ij}$ の関数として創発する停止層。$L_E = \Phi(L_R, H_{ij})$。個体内にありながら外部依存的 | v2.2 addition claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-033 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:77 | $E$ & 外部停止演算子 & \S{}5.7 & $L_E$ の作用として実装される停止演算子。$E = E[L_E, x_n]$、$E \notin \{F^k\}$。$F$ の関数列の外側に位置する | v2.2 addition claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-034 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:78 | $\Phi_{\text{ext}}$ & 外部参照場 & \S{}5.8 & 個体外部の共通参照基盤として外から見える量。$\Phi_{\text{net}}$ と同型($\Phi_{\text{ext}} \equiv \Phi_{\text{net}}$) | v2.2 addition claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-035 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:79 | $\Phi_{\text{net}}$ & $L_E$ ネットワーク & \S{}5.8 & 個体間 $L_E$ の相互干渉ネットワーク。$\Phi_{\text{ext}}$ の構造的実体。Part I の大域的拘束 $\Phi$(公理 III)の精密化 | v2.2 addition claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-036 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:96 | $\mu_\theta$ & 閾値移動能力 & \S{}2.7 & 運動可能領域の拘束パラメータ $\theta$ を内発的に動かす能力。領域組み替え (B) を内発的に起こす能力。サピエンス的知性の特徴的能力(知性一般の必要条件ではない) | v2.2 addition claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-037 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:97 | $\rho_{\text{resp}}$ & 応答チャネル密度 & \S{}4, \S{}6 & 環境の応答性の局所測度。$H_{ji}$ の有効値に対応。アニミズムは沈黙領域での $\rho_{\text{resp}}$ の局所的増大として記述される | v2.2 addition claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-038 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:114 | $v_{\text{inf}}$ & 推論速度 & \S{}11.2 & 推論・判断・仮説更新の頻度。単位時間あたりの $L_F$ の推論ステップ数 | v2.2 addition claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-039 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:115 | $r_{\text{res}}$ & 解像度 & \S{}11.2 & 区別・因果関係・構造表現の粒度。$L_F$ が状態空間をどれだけ細かく分節するか | v2.2 addition claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-040 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:116 | $\eta$ & 停止硬度 & \S{}11.2 & 停止点の固定度・判断の改訂耐性。$L_E$ が供給する停止の固定性。$\eta$ 過大 → 硬直域 | v2.2 addition claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-041 | P2AJ | intelligence-part2/appendices/appendix_a_master_table_ja.tex:133 | $\Sigma$ & 創発停止層発達度 & \S{}1.8 & $L_E$ の発達度・活性度を測る量。概念的に存在するが本論文では量化しない。臨床的・実証的研究へ開く | v2.2 addition claimed | role/type as rawrow; no unit/domain beyond row; INT-SYM localobject takes precedence | v2.1 exactartifact NOT LOCATED; relatedupstreamsource≠verifiedreprint |
| INT-MASTER-042 | P2AJ timescale | intelligence-part2/appendices/appendix_a_master_table_ja.tex:197 | 生命層(Bio-IFGT) & DNA・反応傾向・閾値 & 可変だが超長期 & 世代を跨ぐ & 進化・選択・遺伝 | v2.2 θcomparisontable | relative timescale only; no commonclock | cross-branchrolecomparison; no typedtranslation |
| INT-MASTER-043 | P2AJ timescale | intelligence-part2/appendices/appendix_a_master_table_ja.tex:198 | 知性層・一般 & 外部条件・環境設定 & 受動的可変 & 環境変化に従属 & 環境フィードバック・外部設定 | v2.2 θcomparisontable | relative timescale only; no commonclock | cross-branchrolecomparison; no typedtranslation |
| INT-MASTER-044 | P2AJ timescale | intelligence-part2/appendices/appendix_a_master_table_ja.tex:199 | 知性層・サピエンス & 推論操作の拘束・履歴的閾値 & 能動的可変($\mu_\theta$) & 個体内・対話内 & 閾値移動能力 $\mu_\theta$ | v2.2 θcomparisontable | relative timescale only; no commonclock | cross-branchrolecomparison; no typedtranslation |

## 20. Homology formalization crosswalk

| ID | Phase00 | Source/domainpair | Formalization present | Map/type status | Inverse/invariant |
|---|---|---|---|---|---|
| INT-HOMOFORM-001 | INT-HOMO-001 | P1 §4 Tero Q,D,reinforcement,BC → J,I,projection,Φ | table correspondence | Q/D⇒J/I names; nofunctionmap | noinverse/invariant |
| INT-HOMOFORM-002 | INT-HOMO-002 | P1 §5 Physarum ↔ Transformer | table correspondence | threeconditionsidentified; scalarΦmapsindomain | no crossdomainmap/inverse |
| INT-HOMOFORM-003 | INT-HOMO-003 | P1 §9 VED4DH ↔ Int localhorizon | purely verbal/table | unreachability/divergence/absorption aspreservedroles | no formalinvariant |
| INT-HOMOFORM-004 | INT-HOMO-004 | P1 §9 physical ↔ Bio ↔ Con ↔ Int | table correspondence | fourbranchroles; explicittypedmapguard | none |
| INT-HOMOFORM-005 | INT-HOMO-005 | P1 J §8 paperclip ↔ individual nonclosure | purely verbal | stopabsencecomparison | none |
| INT-HOMOFORM-006 | INT-HOMO-006 | P2 §3,D nonfixedF ↔ Cmax ↔ DH | isomorphism claimed / theorem linked | T3.1/C3.3/D.3 pairroles | no typedmap, inverse or invariantdefinition |
| INT-HOMOFORM-007 | INT-HOMO-007 | P2 §4 regress ↔ branching | purely verbal | regress vsbranching | none |
| INT-HOMOFORM-008 | INT-HOMO-008 | P2 §1,E physicalparticle ↔ life ↔ LE | same schema-variable reuse | U=Φ(L,H), nooperatortype | none |
| INT-HOMOFORM-009 | INT-HOMO-009 | P2 J B.1 CT ↔ physical/Bio/Con/Int | table correspondence | CTcolumn JA, no commonspace | none |
| INT-HOMOFORM-010 | INT-HOMO-010 | P2 J B.2 / fig5 threeemergencecases | table/diagram correspondence | threeL/H/Uroles | none |
| INT-HOMOFORM-011 | INT-HOMO-011 | P2 §5,B.3 Conprojection ↔ IntE-siteprojection ↔ psychprojection | same operator vocabulary | projectionnamed; actualmapnotdefined | none |
| INT-HOMOFORM-012 | INT-HOMO-012 | P2 J §2,B.4 DNAθ ↔ Intθ ↔ sapiensμ | table correspondence | θmobility timescales | no timeconversion/invariant |
| INT-HOMOFORM-013 | INT-HOMO-013 | P2 §2,B.5 BioF ↔ inferenceF | same-variable reuse | BioODE vsinferenceupdate; nonidentityguard | no sameoperator |
| INT-HOMOFORM-014 | INT-HOMO-014 | P2 §5,B.6 Physarum/Transformer/sapiens | table correspondence | LF/LR/LEprofiles | no model-linkedmap |
| INT-HOMOFORM-015 | INT-HOMO-015 | P2 §6–9,B.6 animism/God/religion/socialBC | purely verbal/table | historicaloperations ofLE | no relationoncommonstates |
| INT-HOMOFORM-016 | INT-HOMO-016 | P2 §9 Git ↔ socialBC | conceptual analogy | branch/merge/rollback vsconsensus | no protocolisomorphism |
| INT-HOMOFORM-017 | INT-HOMO-017 | P2 §5,D Φext ↔ Φnet | isomorphism/equivalence claimed | Φext≡Φnet; D.6 viewargument | no mapdomain/codomain/inverse |
| INT-HOMOFORM-018 | INT-HOMO-018 | P2 J §10,D error tolerance ↔ μθ | equivalence claimed / sketch linked | fallibility↔μ D.7 | no explicitpredicates/domain equivalencerelation |
| INT-HOMOFORM-019 | INT-HOMO-019 | P2 §11 ConΔv ↔ IntΔvintel | same formula-role comparison | speed differences; EQF038 | no sameclock/units |
| INT-HOMOFORM-020 | INT-HOMO-020 | P2 B/E/fig9 physics/Bio/Con/Int/social | table/diagram + schemaarrow | incompleteclosure→attractor→sustained | no typedcrosslayermap; guard |
| INT-HOMOFORM-021 | INT-HOMO-021 | P2 J E VEDemergence ↔ weak/strong/holistic/functional emergence | purely verbal taxonomy | weak/strong/holistic/functionalemergence | no formalmap |

## 21. Figure formal roles (14 families, EN/JA separate variants retained)

| ID | Phase00/assetfamily | Placement | Role | Formal expressions | Presentation-strength flag |
|---|---|---|---|---|---|
| INT-FIGFORM-001 | INT-FIG-001 `intelligence-part1/figures/fig1_four_layer_decomposition{,_ja}.{png,svg}` | §2 | illustration / role diagram | knowledge/intelligencearrowsnotupdateequations | no independentproof; arrows rolecompression |
| INT-FIGFORM-002 | INT-FIG-002 `intelligence-part1/figures/fig2_three_axioms{,_ja}.{png,svg}` | §3 | equation summary / Venn schematic | F/ΦandI∧II∧III; jointnecessity/sufficiencylanguage | Only joint satisfaction does isstrongerthanlower-boundreading; flagnotverdict |
| INT-FIGFORM-003 | INT-FIG-003 `intelligence-part1/figures/fig3_cross_domain_homology{,_ja}.{png,svg}` | §5 | cross-domain table/diagram | PhysarumODE/Ftr/graph; scaleexamples | identical structural conditions; formal-roleidentity guard; no typedtranslation |
| INT-FIGFORM-004 | INT-FIG-004 `intelligence-part1/figures/fig4_branching_explosion{,_ja}.{png,svg}` | §7 | empirical-looking schematic growth plot | V∝N,E∼V²,paths∼b^d; no stableΦminimum | eachstepnecessarily vsbodyconditionalgrowth; visualconsequencechainflag |
| INT-FIGFORM-005 | INT-FIG-005 `intelligence-part1/figures/fig5_four_layer_correspondence{,_ja}.{png,svg}` | §9 | cross-domain table/diagram | DH andConΔv>0; Tinternal | substratearrows/necessarylocalclaims coexist proposalguard |
| INT-FIGFORM-006 | INT-FIG-006 `intelligence-part2/figures/fig1_c_landscape{,_ja}.{pdf,svg}` | §3 | proof-sketch visual / landscape | fixedpointcontradictionbox,Cmaxbarrier | gradientpath/nonclosure/endpointvisuallycombined; transitionnotnewproof |
| INT-FIGFORM-007 | INT-FIG-007 `intelligence-part2/figures/fig2_responsive_silent_threshold{,_ja}.{pdf,svg}` | §4 | threshold schematic | H/ρ/μ feedback/openloop | localstopcontrast; no numericthreshold |
| INT-FIGFORM-008 | INT-FIG-008 `intelligence-part2/figures/fig3_mutual_constraint_mu_theta{,_ja}.{pdf,svg}` | §5 | projection schematic | LR(i),LR(j),H,μ,LE | projectionasimplemented-lookingprocess; no typedmap |
| INT-FIGFORM-009 | INT-FIG-009 `intelligence-part2/figures/fig4_three_layer_architecture{,_ja}.{pdf,svg}` | §5 | equation-summary / architecture | LF→LR→LE; μ/B/project/converge | convergencearrow noformalupdate; figureENhave vsJAmayhaveprofiles |
| INT-FIGFORM-010 | INT-FIG-010 `intelligence-part2/figures/fig5_three_examples_of_emergence{,_ja}.{pdf,svg}` | §5 | cross-domain schema | U=Φ(L,H),E(A),Ωlife | explicitformal-rolecomparison guard |
| INT-FIGFORM-011 | INT-FIG-011 `intelligence-part2/figures/fig6_phi_ext_phi_net{,_ja}.{pdf,svg}` | §5 | identity diagram | Φext≡Φnet | two-viewidentitypictured; no definedbijection |
| INT-FIGFORM-012 | INT-FIG-012 `intelligence-part2/figures/fig7_evolution_of_stopping_structures{,_ja}.{pdf,svg}` | §9 | social-history schematic | LEinstallation→compression→maintenance→revision→sync | progressguard; arrowsnotgenerativeproof |
| INT-FIGFORM-013 | INT-FIG-013 `intelligence-part2/figures/fig8_phase_diagram{,_ja}.{pdf,svg}` | §11 | qualitative phase diagram | vinf,rres,η,Δv; origin(0,0,0) | narrowband/necessaryzone visuallyquantitative; no numericphaseboundaries |
| INT-FIGFORM-014 | INT-FIG-014 `intelligence-part2/figures/fig9_cross_domain_homology{,_ja}.{pdf,svg}` | §13 | homology diagram | Δ→∇Δ;F;Conwindow;Φnet | explicit no sharedcarrier/mechanism/typedmap guard |

図の現行SVG textを28variants全件から抽出してcaption/figurenoteと照合。compiledPNG/PDFとのpixel同値やPDFfreshness再判定はこのformal inventoryでは行わない（Phase00のpresentation inventoryを継承）。図中のみの `|V|∝N`, `paths∼b^d`, `(I∧II∧III)`, `(0,0,0)`, `Δv>0`, `Δ→∇Δ`, `LR(i)` はFIGFORMのraw-role対象でありTeX98display数に足さない。Nは正しい知識の蓄積量、RomanI/II/IIIはaxiom番号でinformationIとは別、agent A…Gは図のノード名でEoperatorとは別。これらを以下supplement symbol ledgerへ分離する。

### Symbol supplement (figure-only roles)

| ID | Glyph | Source | Role | Signature | Risk | Separation |
|---|---|---|---|---|---|---|
| INT-SYM-098 | N (figure only) | P1fig4 EN/JA | accumulated correctknowledge count | PARTIAL | C1 | Ni graphnodeとは別 |
| INT-SYM-099 | ∇Δ (figure only) | P2fig9 EN/JA | physicaldifferencegradientcomparison | PARTIAL | C4 | closure/potentialgradient同定NO |
| INT-SYM-100 | SSO/TCA (figure terms) | P2fig9 EN/JA | Concondition/window comparison | UNRESOLVED | C4 | Intobjectとしてtype未定義 |
| INT-SYM-101 | I/II/III (Roman axioms) | P1fig2/3;§3 | axiomlabels, conjunction schematic | EXPLICIT | C1 | informationIとは別 |
| INT-SYM-102 | A…G (agent labels) | P2fig6 EN/JA | networknode labels | INFERRED | C1 | movementA/B,energyA,operatorE別 |

## 22. Branching explosion — four separate inventories

1. **Graph combinatorics**：P1§7, EQF014–015, FIGFORM004。bodyはedge数がnode数の二乗程度に増え得るという記述、branching factor/depthのb^d表現。FIG004はN→V→E→pathsの線形/二次/指数を同一画面へ置く。Nの生成則、graphのsimple/directed/dense条件、exactdepthかuptodepthかは固定されない。
2. **Inference dynamics**：P1§7のI↑、divJ↑、correctness(p)⇒divJ|p≠0（EQF010–013）をgraph数え上げと別familyにした。graph→flowfield/pへの評価map、divergenceのgeometryは未提示。
3. **Cognitive interpretation**：correctness accumulation→reuse/connectivity→branchingというprose。cognitiveperformance/正しさのobservableをgraphから作らない。
4. **Stopping claim**：no stable Φ-minimum / internalTabsenceはEQF044, THM011。P2はnonfixedpointをregress/branchingへ結び直す。countingrelationからstopabsenceへのformalbridgeはsourceの主張として記録し、監査で導出しない。

## 23. Non-closure theorem dependency inventory

P2EN/JA§2–3のF, X, JをP1flow/graphから独立に扱う。sourceが明記する順序は、P1/P2前提、P3fixedθ/Aのscope、counterfactual fixedpoint、strictJの代入、矛盾というsketchである。P3のgroundingはJAの追加記述で、定理本文はP1/P2を列挙する。P3が代数ステップでどう用いられるかは別に追跡し、追加前提を作らない。

内部Sのcorollaryは「停止判断→F-fixedpoint」「補助判断S→F'」「F'にも同じ前提」というsource内遷移を含む。これらはTHM001の式そのものと別route。Cmax/horizon対応はさらにclosurePDE/barrierとisomorphism tableを要する。P1 Internal(R)/External(R)との関係はexposition/re-descriptionとして明示されるが、R/X/T/Eのtypedtranslationは未提示。proofvalidity・theoremtruth・circularityはいずれも未判定。

## 24. LF / LR / LE object-role inventory

| Layer | Definition/source | State/input/output | Update/dependency | Stop / internal-external boundary |
|---|---|---|---|---|
| LF | P2JA2.1 / EN§2; inference action domain incl trajectories | X/x,F; domain/process両語、single/setF別 | xnrecurrence; no complete state-space evolution contract | LF単独内部stopなしというtheorem-linkedclaim |
| LR | P2JA5.1 / EN§5 | LFmotion traces + recursive reference; record≠reference motion | recurrenceprose、explicitupdate/mapなし | storageはindividual/internal、environmentexternalized、frozen variants; currentFの外≠必ず個体外 |
| LE | P2JA5.2 / ENdefinition5.1 | LRmotion/H inputs; layer/attractor output named | EQF032schema, μ/B/projection/convergence chain | individualinternal butexternallydependent; suppliesE; empiricalmoduleとは同定しない |

三層を一つのset/space/processontologyに統一しない。LF/LR/LEのaddition/arrow表記はarchitecture summaryとしてraw保持し、vector-space直和や関数合成へ読み替えない。

## 25. μθ dedicated inventory

| ID | Role | Source | Formal status / unresolved boundary |
|---|---|---|---|
| INT-MUTHETA-001 | definition2.3 | P2J§2; EN§1,2 | capacityendogenouslymoveθ; no ratefunction |
| INT-MUTHETA-002 | Ωθ A/B | P2§2/A | regionreconfiguration role, no reconfigurationmap |
| INT-MUTHETA-003 | responsive/silent | P2§4 | effectiveboundarymoves; no scalarthresholdcriterion |
| INT-MUTHETA-004 | E-siteprojection | P2§5/fig3/4 | μ→B→site; no projectionoperator |
| INT-MUTHETA-005 | LEemergence | P2§5 | LR/H convergencerole, no dynamicalcondition |
| INT-MUTHETA-006 | error tolerance | P2J§10,D.7 | bidirectionalsketch; μpredicateformalizationabsent |
| INT-MUTHETA-007 | sapiens/general | P2§12/fig4 | sapiens-specific; notgeneralnecessarycondition |
| INT-MUTHETA-008 | Bioθtimescale | P2A/B | DNA/generation vs individualdialoguecomparison |
| INT-MUTHETA-009 | phase diagram | P2§11/fig8 | active return/revisableLErole; not calibratedcontrol |
| INT-MUTHETA-010 | Conμ separation | P1§9; P2B | sameglyph/projectivecomparison≠sameparameter |

## 26. Φ / F / J / E / C separation

Family counts here are semantic-role splits, not occurrence totals.

| Glyph | Distinct families retained | Formal relation / identity boundary |
|---|---|---|
| Φ (8) | P1global; Φbio; Φtr; CTΦ; ConΦ/gradient-window comparator; emergenceΦ(L,H); Φext; Φnet | P1 firstthree explicitS→R; emergenceoperatoruntyped; ext≡net asserted; P1→net refinement language ≠ typedmap |
| F (6 principal) | P1update; P1Fbio; Ftr; P2singleinference; P2setcontinuation; BioF(x;θ) | F' andF^k arederivednotation underP2, notseventhindependentlaw; single/setcontractunresolved |
| J (5) | P1J; Jint; JIbranchcomparison; JCclosureflux; J(x)justification | firstfourflowroles; J:X→R justificationseparate; noautomaticconversion |
| E (3) | P1graphedge set; P2stoppingoperator; VEDE(A)energyfunctional | diagramagentE islabelonly; neitheractionsemanticsnorgraphedgefromglyph |
| C (5) | scalarclosuremap; Cij; Cmax; C*; C-landscape/stabilityrole | lastrole belongsCmapbutinterpretivenotnewnumericalquantity; truthidentitynegated; cognitiveclosure/horizonrelationnotderivedhere |

ΦfamilyCon comparator iscoveredbySYM023/055, CT bySYM007; the8countincludescomparatorsnotlocaladoptedfields. F_I isforce(SYM030), notmemberofthe6update/operatorFfamilies. C0–C6notationrisksmustnotbeconfusedwithclosureCorthephase03circularitytaxonomy.

## 27. Formal subsystem completeness markers

| ID | Subsystem | State space | Variables | Update/evolution | IC | BC/scope | Parameters | Stop | Observable | Proof item located | Validation artifact located |
|---|---|---|---|---|---|---|---|---|---|---|---|
| INT-FCOMP-001 | P1 threeaxioms | Senumerated/connected | s,F,Φ | orderedupdate | none | none | concreteF/Φfuture | nointernalstopprose | noextractionrule | axiomstatements | notmodel-linkedhere |
| INT-FCOMP-002 | Physarum mapping | graphnodes/edges | Q,D,L,Δp | conductanceODE | none | nutrientsource/sink/Kirchhoffprose | μ>0JAexample | notstoppingcriterion | flow/conductancenamed | literaturerelation imported | branch-localvalidationnotlocated |
| INT-FCOMP-003 | Transformer mapping | hiddenstates | h,ell,Ftr,Φtr | layerupdate | none | notexplicitBC | trainingroles;weightsnotdefined | externaloutput/terminationprose | hiddenstatesnamed | analogy/table | noexecutedtesthere |
| INT-FCOMP-004 | branching explosion | V/Egraph | b,d,N,I,J | growthrelations notoperator | none | none | b/droles | nointernalstopclaim | counts named, extractionnotgiven | prosechain | noquantitativevalidationhere |
| INT-FCOMP-005 | P1 nonclosure | Rboundary | T/Internal/External | inferenceprose | none | boundarynotformalBC | none | externalmembership | none | proseargument | none |
| INT-FCOMP-006 | P2 closure dynamics | X/C-landscape | C,JC,τ,parameters | JAclosurePDE | none | upperboundclaim notBCproblem | names notranges/units | nonclosureclaim | none | barrierprose | none |
| INT-FCOMP-007 | P2 inference F | X | F,J | single/setvariants | x0symbol notinitialdata | fixedΩscope | admissibilitypartial | hypotheticalS | none | F1–4properties | none |
| INT-FCOMP-008 | nonclosure theorem | X | F,J,x* | Fiteration premise | none | fixedθ/A scope | P1/P2/P3 | nointernalfixedpoint | none | contradictionsketch | notempiricaltest |
| INT-FCOMP-009 | LR/LE emergence | layerrolesonly | LR,H,Φ,LE,E | schemaarrows | none | externalconstraintrole | μ/θuntyped | externallydependentE | logs/sitesnamed | definition/casesketch | none |
| INT-FCOMP-010 | μθ | Ωregionroles | θ/μ/A/B | reconfigurationprose | none | regionboundarynotBC | capacityunquantified | Esite | nocalibration | equivalenceprose | none |
| INT-FCOMP-011 | Φext/Φnet | field/networkroles | LE/H/nodes | syncprose | none | individualexternality | noedge-weightdomain | sharedstop | none | two-viewsketch | none |
| INT-FCOMP-012 | Σ andphaseaxes | conceptualΣ;3axisdisplay | v,r,η,μ,Δv | noevolutionlaw | none | bandsnotnumericBC | qualitativeroles | zero-motion/rigidityprose | candidategrain/rateonly | regimeargument | none |
| INT-FCOMP-013 | social blockchain | network/logroles | knowledgeblocks/consensus | noalgorithm | none | socialscope | cost/trustqualitative | provisionalconsensus | socialbehaviournamed | Gitcomparison | none |

## 28. Phase00 object crosswalk

| ID | Phase00 | Object | Current source | Phase01 destination |
|---|---|---|---|---|
| INT-OBJMAP-001 | INT-OBJ-001 | S / X / x / s | P1 §3,5; P2 §1–3 | 001,024,043,047 |
| INT-OBJMAP-002 | INT-OBJ-002 | F / Ftr / F(x;θ) | P1 §3,5; P2 §2,B | 001,009,025,045,046,048 |
| INT-OBJMAP-003 | INT-OBJ-003 | Φ global constraint | P1 §3–5 | 002–004 |
| INT-OBJMAP-004 | INT-OBJ-004 | I | P1 §4,7; P2 §1,A | 010,013,019 |
| INT-OBJMAP-005 | INT-OBJ-005 | J / Jint / JC | P1 §4,7; P2 §1,A | 011,023 |
| INT-OBJMAP-006 | INT-OBJ-006 | J(x) justification | P2 §2–3,D | 026,047 |
| INT-OBJMAP-007 | INT-OBJ-007 | Physarum Qij/Dij/Lij/pi | P1 §4–5 | 005–007,063; p_i独立未確認 |
| INT-OBJMAP-008 | INT-OBJ-008 | Transformer h / layers / attention | P1 §5 | 008–009 |
| INT-OBJMAP-009 | INT-OBJ-009 | graph V/E/b/d | P1 §7 | 014–015 |
| INT-OBJMAP-010 | INT-OBJ-010 | T / R / External(R) | P1 §8–9 | 016,044 |
| INT-OBJMAP-011 | INT-OBJ-011 | DH / local horizon-form | P1 §9; P2 §3,C | 016,027/THM003 |
| INT-OBJMAP-012 | INT-OBJ-012 | C / Cij | P2 §1–2,A | 018,024,029,049 |
| INT-OBJMAP-013 | INT-OBJ-013 | C* / Cmax / Δ / Γ / κB / a / ξ / α | P2 §1,A | 017,018,022,023 |
| INT-OBJMAP-014 | INT-OBJ-014 | τ | P2 §1,A | 017,TIME005 |
| INT-OBJMAP-015 | INT-OBJ-015 | f | P2 §1 | 019–021 |
| INT-OBJMAP-016 | INT-OBJ-016 | Ωθ / θ | P2 §1–2 | 030 |
| INT-OBJMAP-017 | INT-OBJ-017 | Hij / ρi / λ | P2 §2,A | 029,035 |
| INT-OBJMAP-018 | INT-OBJ-018 | LF | P2 §2 | 025,050 |
| INT-OBJMAP-019 | INT-OBJ-019 | LR | P2 §5 | 032,050 |
| INT-OBJMAP-020 | INT-OBJ-020 | LE | P2 §5 | 032,054 |
| INT-OBJMAP-021 | INT-OBJ-021 | E | P2 §5 | 033 |
| INT-OBJMAP-022 | INT-OBJ-022 | μθ / (A)/(B) movement | P2 §2,5 | 030,037,054 |
| INT-OBJMAP-023 | INT-OBJ-023 | Φext / Φnet | P2 §5,9 | 034 |
| INT-OBJMAP-024 | INT-OBJ-024 | ρresp / responsive-silent threshold | P2 §4,A | 035/SYM073 |
| INT-OBJMAP-025 | INT-OBJ-025 | U / L / Φ(L,H) | P2 §1,E | 031 |
| INT-OBJMAP-026 | INT-OBJ-026 | Ωlife / Ωintel / Jlife | P2 §1,B,E | 036,046 |
| INT-OBJMAP-027 | INT-OBJ-027 | E(A) particle closure energy / internal vectors | P2 E | 041,061 |
| INT-OBJMAP-028 | INT-OBJ-028 | Σ / vinf / rres / η | P2 §11,A | 039/040分離;Σは発達量 |
| INT-OBJMAP-029 | INT-OBJ-029 | vLR / Δvintel | P2 §11 | 038 |
| INT-OBJMAP-030 | INT-OBJ-030 | knowledge block / consensus / legitimacy | P2 §9–10 | DEF029–030prose |
| INT-OBJMAP-031 | INT-OBJ-031 | projection / opening window / TΦ / ∇Φ / Δv / μ | P1 §9; P2 §2,5,B | TIME008/Φcomparison |
| INT-OBJMAP-032 | INT-OBJ-032 | history / token / log / re-entry | P1 §2,8–9; P2 §4–5,9 | DEF022/logrole; noexecutionupdate |

## 29. Equation dependency index

| ID | EQF | Dependencies explicitly named / interpretive boundaries |
|---|---|---|
| INT-EQDEP-001 | INT-EQF-001 | 043 state;002 bias interpretation, not Fconstruction |
| INT-EQDEP-002 | INT-EQF-002 | 043domain |
| INT-EQDEP-003 | INT-EQF-003 | 002exemplification |
| INT-EQDEP-004 | INT-EQF-004 | 002exemplification |
| INT-EQDEP-005 | INT-EQF-005 | 063graph; Δp/D/L roles |
| INT-EQDEP-006 | INT-EQF-006 | 005Q;007optional response |
| INT-EQDEP-007 | INT-EQF-007 | 006example notmandatory |
| INT-EQDEP-008 | INT-EQF-008 | 043analogy; token/layerindices |
| INT-EQDEP-009 | INT-EQF-009 | 008hiddenstates;004globalbiasrole |
| INT-EQDEP-010 | INT-EQF-010 | P1accumulationdefinition |
| INT-EQDEP-011 | INT-EQF-011 | 010prose direction; no differentialderivation |
| INT-EQDEP-012 | INT-EQF-012 | 010/011correctness→flowclaim |
| INT-EQDEP-013 | INT-EQF-013 | 010indexedvariant |
| INT-EQDEP-014 | INT-EQF-014 | 063graph analogy; no densegraphassumption |
| INT-EQDEP-015 | INT-EQF-015 | 014branchinterpretation; growthrouteprose |
| INT-EQDEP-016 | INT-EQF-016 | 044negativeinternalrelation |
| INT-EQDEP-017 | INT-EQF-017 | 018range,023flux,parameter/source-termroles |
| INT-EQDEP-018 | INT-EQF-018 | 017barrierunreachabilityclaim |
| INT-EQDEP-019 | INT-EQF-019 | 018C;20/21examples optional |
| INT-EQDEP-020 | INT-EQF-020 | 019example |
| INT-EQDEP-021 | INT-EQF-021 | 019example |
| INT-EQDEP-022 | INT-EQF-022 | Cgradientrole;019upstreamvocabulary |
| INT-EQDEP-023 | INT-EQF-023 | Cgradientrole;017balanceflux |
| INT-EQDEP-024 | INT-EQF-024 | 018codomain |
| INT-EQDEP-025 | INT-EQF-025 | 047/026justification;048alternativecontract |
| INT-EQDEP-026 | INT-EQF-026 | 025+047compositionpremise |
| INT-EQDEP-027 | INT-EQF-027 | 026+fixedpointcounterfactual;THM001 |
| INT-EQDEP-028 | INT-EQF-028 | 027+stop→fixedpointtransition;THM002 |
| INT-EQDEP-029 | INT-EQF-029 | H/rho/lambda roles; noCaggregation |
| INT-EQDEP-030 | INT-EQF-030 | 024C-landscape;θroles |
| INT-EQDEP-031 | INT-EQF-031 | Lmotion,H→Urole schema |
| INT-EQDEP-032 | INT-EQF-032 | 031application;LR,H;054mechanismprose |
| INT-EQDEP-033 | INT-EQF-033 | 032LE;025Fiterations separated |
| INT-EQDEP-034 | INT-EQF-034 | 032LEnetwork;functionalviewdefinitions |
| INT-EQDEP-035 | INT-EQF-035 | Hji/rhoresp thresholdprose |
| INT-EQDEP-036 | INT-EQF-036 | 030domains;Bio/Intcrossdomainclaim |
| INT-EQDEP-037 | INT-EQF-037 | μdefinition;stoppingrevisability;THM008 |
| INT-EQDEP-038 | INT-EQF-038 | speedroles;notConclockinheritance |
| INT-EQDEP-039 | INT-EQF-039 | LEconceptualdevelopment, noquantification |
| INT-EQDEP-040 | INT-EQF-040 | 038speed/eta/res roles;Σnotregionset |
| INT-EQDEP-041 | INT-EQF-041 | VEDenergycomparison;031emergence; noexplicitstopfunctional |
| INT-EQDEP-042 | INT-EQF-042 | fluidanalogy not017proof |
| INT-EQDEP-043 | INT-EQF-043 | P1connectednessprose |
| INT-EQDEP-044 | INT-EQF-044 | P1nonclosureprose;016positiveexternalmembership |
| INT-EQDEP-045 | INT-EQF-045 | 001example;006nottypedconversion |
| INT-EQDEP-046 | INT-EQF-046 | Biocomparison;025nonidentityguard |
| INT-EQDEP-047 | INT-EQF-047 | 025justificationinput |
| INT-EQDEP-048 | INT-EQF-048 | 025alternative;026Jsetextensionmissing |
| INT-EQDEP-049 | INT-EQF-049 | 024closureinterpretation andnegation |
| INT-EQDEP-050 | INT-EQF-050 | 025/032LRLErole chain |
| INT-EQDEP-051 | INT-EQF-051 | 027/033expositorychain |
| INT-EQDEP-052 | INT-EQF-052 | 029/030/037rolechain |
| INT-EQDEP-053 | INT-EQF-053 | 032/034networkinterpretation |
| INT-EQDEP-054 | INT-EQF-054 | 030/032/033/037claimedprocess |
| INT-EQDEP-055 | INT-EQF-055 | 035/033animismrole |
| INT-EQDEP-056 | INT-EQF-056 | 033socialcompression |
| INT-EQDEP-057 | INT-EQF-057 | 056maintenancerole |
| INT-EQDEP-058 | INT-EQF-058 | 056negativeclaimscope |
| INT-EQDEP-059 | INT-EQF-059 | 019conditionalcompleteclosureprose |
| INT-EQDEP-060 | INT-EQF-060 | 022/023localgradientcontext |
| INT-EQDEP-061 | INT-EQF-061 | 041physicalclosurecomparison |
| INT-EQDEP-062 | INT-EQF-062 | 031homologyschema |
| INT-EQDEP-063 | INT-EQF-063 | 005graphroles |

## 30. Phase00 collision crosswalk

| ID | Phase00 | Glyph/term | Formal inventory destination | Phase boundary |
|---|---|---|---|---|
| INT-GLYPHMAP-001 | INT-GLYPH-001 | I | SYM011–012; EQF010/019 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-002 | INT-GLYPH-002 | C / Cij | SYM018–021; EQF024/029 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-003 | INT-GLYPH-003 | Φ | SYM004–010; §26 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-004 | INT-GLYPH-004 | J | SYM013–017; §26 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-005 | INT-GLYPH-005 | τ | SYM054; TIME005/008 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-006 | INT-GLYPH-006 | F | SYM024–031; §26 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-007 | INT-GLYPH-007 | E / E(A) | SYM045/081/082; §26 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-008 | INT-GLYPH-008 | S | SYM001/090 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-009 | INT-GLYPH-009 | θ / μ | SYM057–060; MUTHETA | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-010 | INT-GLYPH-010 | H / Cij | SYM019/070–074 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-011 | INT-GLYPH-011 | Φext / Φnet | SYM009–010; EQF034 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-012 | INT-GLYPH-012 | intelligence | DEF004/032; HOMOFORM014 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-013 | INT-GLYPH-013 | landscape | EQF024; SYM007/023 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-014 | INT-GLYPH-014 | attractor / secondattractor | EQF031–032/036/041 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-015 | INT-GLYPH-015 | boundary / horizon | SYM093; EQF016/018/027 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-016 | INT-GLYPH-016 | closure / nonclosure | THM001–004/011 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-017 | INT-GLYPH-017 | token / log / memory | SYM094; DEF022/029/030 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-018 | INT-GLYPH-018 | stopping | DEF003/011/024/027; Efamilies | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-019 | INT-GLYPH-019 | emergence | EQF031/032; THM005 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-020 | INT-GLYPH-020 | homology / isomorphism | SYM homology/isomorphism row; HOMOFORM001–021 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-021 | INT-GLYPH-021 | layers | INDEX014; §24 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |
| INT-GLYPHMAP-022 | INT-GLYPH-022 | projection | OP025; HOMOFORM011 | same-object claim and actualtypedmapping remain distinct; C0–C6 notationrisk only |

## 31. Residual inline symbol/lexeme occurrence index

| ID | Stream | Raw inner expression | Occurrences | Exact locations (repeated line numbers retained) |
|---|---|---|---|---|
| INT-LEX-001 | P1E | `\Phi` | 23 | `intelligence-part1/sections/abstract.tex:3,3`; `intelligence-part1/sections/01_introduction.tex:9,9,43`; `intelligence-part1/sections/03_minimal_axioms_of_intelligence.tex:35,37,41,43,45,45,47,80`; `intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex:5,29,30,35,61,62,78,81`; `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex:64`; `intelligence-part1/sections/10_summary_convergence_and_outlook.tex:16` |
| INT-LEX-002 | P1E | `C` | 1 | `intelligence-part1/sections/01_introduction.tex:9` |
| INT-LEX-003 | P1E | `I` | 9 | `intelligence-part1/sections/01_introduction.tex:9,9`; `intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex:23,24,35,59,78`; `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex:21,57` |
| INT-LEX-004 | P1E | `J` | 8 | `intelligence-part1/sections/01_introduction.tex:9,9`; `intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex:26,27,35,35,58,78` |
| INT-LEX-005 | P1E | `F` | 1 | `intelligence-part1/sections/03_minimal_axioms_of_intelligence.tex:29` |
| INT-LEX-006 | P1E | `J_{\mathrm{int}}` | 1 | `intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex:35` |
| INT-LEX-007 | P1E | `Q_{ij}` | 2 | `intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex:41,58` |
| INT-LEX-008 | P1E | `e_{ij}` | 1 | `intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex:41` |
| INT-LEX-009 | P1E | `D_{ij}` | 2 | `intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex:41,59` |
| INT-LEX-010 | P1E | `L_{ij}` | 1 | `intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex:41` |
| INT-LEX-011 | P1E | `\Delta p_{ij}` | 1 | `intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex:45` |
| INT-LEX-012 | P1E | `f(&#124;Q&#124;)` | 1 | `intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex:60` |
| INT-LEX-013 | P1E | `\Phi_{\mathrm{bio}}` | 1 | `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex:26` |
| INT-LEX-014 | P1E | `\Phi_{\mathrm{tr}}` | 1 | `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex:47` |
| INT-LEX-015 | P1E | `\{h_i^{(\ell)}\}` | 1 | `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex:62` |
| INT-LEX-016 | P1E | `p` | 2 | `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex:32,32` |
| INT-LEX-017 | P1E | `b` | 1 | `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex:51` |
| INT-LEX-018 | P1E | `d` | 1 | `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex:51` |
| INT-LEX-019 | P1E | `\mathcal{R}` | 3 | `intelligence-part1/sections/08_the_non_closure_of_individual_intelligence.tex:11,11`; `intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex:11` |
| INT-LEX-020 | P1E | `\mathcal{T}` | 1 | `intelligence-part1/sections/08_the_non_closure_of_individual_intelligence.tex:11` |
| INT-LEX-021 | P1E | `\mathrm{External}` | 1 | `intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex:20` |
| INT-LEX-022 | P1J | `\Phi` | 58 | `intelligence-part1/sections_ja/abstract_ja.tex:3,3`; `intelligence-part1/sections_ja/01_introduction_ja.tex:11,11,47`; `intelligence-part1/sections_ja/02_the_decomposition_perception_recognition_knowledge_and_intelligence_ja.tex:106`; `intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex:69,72,72,74,80,80,82,82,84,84,86,89,90,91,96,104,111,114,117,179,188`; `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:7,7,9,11,71,75,75,76,77,77,86,92,92,149,150,158,161,165,165,167,189,196`; `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:149,196`; `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:56,56,141,145,145`; `intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex:29,75` |
| INT-LEX-023 | P1J | `C` | 4 | `intelligence-part1/sections_ja/01_introduction_ja.tex:11`; `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:150`; `intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex:31,32` |
| INT-LEX-024 | P1J | `I` | 16 | `intelligence-part1/sections_ja/01_introduction_ja.tex:11,11`; `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:52,56,57,58,92,92,147,189,205`; `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:44,50,139,204`; `intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex:74` |
| INT-LEX-025 | P1J | `J` | 17 | `intelligence-part1/sections_ja/01_introduction_ja.tex:11,11`; `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:62,66,67,68,68,86,92,92,146,189,205`; `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:50,140`; `intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex:41`; `intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex:74` |
| INT-LEX-026 | P1J | `F` | 1 | `intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex:49` |
| INT-LEX-027 | P1J | `J_{\mathrm{int}}` | 1 | `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:92` |
| INT-LEX-028 | P1J | `Q_{ij}` | 2 | `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:111,146` |
| INT-LEX-029 | P1J | `e_{ij}` | 2 | `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:111,112` |
| INT-LEX-030 | P1J | `D_{ij}` | 6 | `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:112,124,130,130,147`; `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:40` |
| INT-LEX-031 | P1J | `\Delta p_{ij}` | 1 | `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:116` |
| INT-LEX-032 | P1J | `L_{ij}` | 1 | `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:122` |
| INT-LEX-033 | P1J | `f` | 1 | `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:130` |
| INT-LEX-034 | P1J | `f(\lvert Q\rvert)` | 1 | `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:148` |
| INT-LEX-035 | P1J | `\Phi_\text{bio}` | 4 | `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:48,55,116,149` |
| INT-LEX-036 | P1J | `\ell` | 1 | `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:98` |
| INT-LEX-037 | P1J | `i` | 2 | `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:98,98` |
| INT-LEX-038 | P1J | `j` | 1 | `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:98` |
| INT-LEX-039 | P1J | `F_\text{tr}` | 1 | `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:107` |
| INT-LEX-040 | P1J | `\Phi_\text{tr}` | 4 | `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:109,116,116,149` |
| INT-LEX-041 | P1J | `\{h^{(\ell)}_i\}` | 1 | `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:147` |
| INT-LEX-042 | P1J | `p` | 17 | `intelligence-part1/sections_ja/06_the_gettier_problem_as_a_structural_diagnostic_ja.tex:19,19,22,23,24,45,45,46,46`; `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:66,69,70,71,72,73,76,76` |
| INT-LEX-043 | P1J | `S` | 6 | `intelligence-part1/sections_ja/06_the_gettier_problem_as_a_structural_diagnostic_ja.tex:19,19,23,24,45,46` |
| INT-LEX-044 | P1J | `\mathcal{S}` | 1 | `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:44` |
| INT-LEX-045 | P1J | `s_i` | 1 | `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:109` |
| INT-LEX-046 | P1J | `b` | 3 | `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:112,112,205` |
| INT-LEX-047 | P1J | `d` | 1 | `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:112` |
| INT-LEX-048 | P1J | `A` | 4 | `intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex:28,29,37,41` |
| INT-LEX-049 | P1J | `B` | 8 | `intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex:29,30,31,37,40,41,42,62` |
| INT-LEX-050 | P1J | `t_n` | 2 | `intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex:52,52` |
| INT-LEX-051 | P1J | `\mathcal{R}` | 11 | `intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex:187,187,188,194,194,196,196`; `intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex:22,26,32,51` |
| INT-LEX-052 | P1J | `\mathcal{T}` | 7 | `intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex:187,188,194,196,196`; `intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex:22,26` |
| INT-LEX-053 | P1J | `\Delta v` | 1 | `intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex:148` |
| INT-LEX-054 | P1J | `\mu` | 1 | `intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex:148` |
| INT-LEX-055 | P1J | `\tau` | 1 | `intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex:148` |
| INT-LEX-056 | P1J | `T_\Phi` | 1 | `intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex:148` |
| INT-LEX-057 | P1J | `\nabla\Phi` | 1 | `intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex:148` |
| INT-LEX-058 | P2E | `L_F` | 27 | `intelligence-part2/main.tex:15`; `intelligence-part2/sections/00_introduction.tex:6,12`; `intelligence-part2/sections/01_preliminaries.tex:68`; `intelligence-part2/sections/03_nonclosure_theorem.tex:2,4,11,63`; `intelligence-part2/sections/04_response_channels.tex:4,40`; `intelligence-part2/sections/05_emergent_stopping_layer.tex:4,11,17,19,19,24,108`; `intelligence-part2/sections/09_social_blockchain.tex:24`; `intelligence-part2/sections/11_instability_region.tex:17,29,31,38,45`; `intelligence-part2/sections/12_constructive_clauses.tex:8`; `intelligence-part2/sections/13_conclusion.tex:8,12,12` |
| INT-LEX-059 | P2E | `L_F/L_R/L_E` | 3 | `intelligence-part2/main.tex:15`; `intelligence-part2/sections/00_introduction.tex:43`; `intelligence-part2/sections/11_instability_region.tex:4` |
| INT-LEX-060 | P2E | `L_E` | 58 | `intelligence-part2/main.tex:15`; `intelligence-part2/sections/00_introduction.tex:12,18,24,39`; `intelligence-part2/sections/01_preliminaries.tex:55,70,73,75`; `intelligence-part2/sections/03_nonclosure_theorem.tex:11,63`; `intelligence-part2/sections/04_response_channels.tex:40`; `intelligence-part2/sections/05_emergent_stopping_layer.tex:2,4,11,17,19,26,34,37,48,53,57,59,63,68,76,84,88,101,103,103,108`; `intelligence-part2/sections/06_animism.tex:8`; `intelligence-part2/sections/08_religion.tex:8`; `intelligence-part2/sections/09_social_blockchain.tex:2,30,32,32,32,32,37,39`; `intelligence-part2/sections/10_gettier_problem.tex:10`; `intelligence-part2/sections/11_instability_region.tex:21,27,29,31,31,38,38,47,55`; `intelligence-part2/sections/12_constructive_clauses.tex:16,28`; `intelligence-part2/sections/13_conclusion.tex:12,12,28` |
| INT-LEX-061 | P2E | `L_R` | 29 | `intelligence-part2/sections/00_introduction.tex:12,12`; `intelligence-part2/sections/01_preliminaries.tex:55,69,70`; `intelligence-part2/sections/03_nonclosure_theorem.tex:63`; `intelligence-part2/sections/04_response_channels.tex:36,38`; `intelligence-part2/sections/05_emergent_stopping_layer.tex:4,11,17,19,28,30,30,32,37,53,67,108`; `intelligence-part2/sections/11_instability_region.tex:17,29,46,47`; `intelligence-part2/sections/12_constructive_clauses.tex:12,16`; `intelligence-part2/sections/13_conclusion.tex:12,12,12` |
| INT-LEX-062 | P2E | `H_{ij}` | 12 | `intelligence-part2/sections/00_introduction.tex:12`; `intelligence-part2/sections/01_preliminaries.tex:49,70,71`; `intelligence-part2/sections/04_response_channels.tex:12`; `intelligence-part2/sections/05_emergent_stopping_layer.tex:9,11,11,19,37`; `intelligence-part2/sections/12_constructive_clauses.tex:16`; `intelligence-part2/sections/13_conclusion.tex:12` |
| INT-LEX-063 | P2E | `F` | 16 | `intelligence-part2/sections/00_introduction.tex:35,43`; `intelligence-part2/sections/01_preliminaries.tex:68`; `intelligence-part2/sections/02_inference_operator.tex:2,4,14,26,28,46`; `intelligence-part2/sections/03_nonclosure_theorem.tex:11,18,31,63`; `intelligence-part2/sections/05_emergent_stopping_layer.tex:30`; `intelligence-part2/sections/12_constructive_clauses.tex:8`; `intelligence-part2/sections/13_conclusion.tex:8` |
| INT-LEX-064 | P2E | `I` | 1 | `intelligence-part2/sections/01_preliminaries.tex:6` |
| INT-LEX-065 | P2E | `J` | 2 | `intelligence-part2/sections/01_preliminaries.tex:6`; `intelligence-part2/sections/03_nonclosure_theorem.tex:20` |
| INT-LEX-066 | P2E | `\Phi` | 1 | `intelligence-part2/sections/01_preliminaries.tex:6` |
| INT-LEX-067 | P2E | `C` | 8 | `intelligence-part2/sections/01_preliminaries.tex:10,27,31`; `intelligence-part2/sections/03_nonclosure_theorem.tex:11`; `intelligence-part2/sections/10_gettier_problem.tex:4,12,14,14` |
| INT-LEX-068 | P2E | `\mu_\theta` | 24 | `intelligence-part2/sections/01_preliminaries.tex:12,72`; `intelligence-part2/sections/03_nonclosure_theorem.tex:11`; `intelligence-part2/sections/04_response_channels.tex:20,25`; `intelligence-part2/sections/05_emergent_stopping_layer.tex:9,11,17,53,55,59,65,108`; `intelligence-part2/sections/10_gettier_problem.tex:25,29`; `intelligence-part2/sections/11_instability_region.tex:27,29,31,38,48`; `intelligence-part2/sections/12_constructive_clauses.tex:18,20`; `intelligence-part2/sections/13_conclusion.tex:10,34` |
| INT-LEX-069 | P2E | `E` | 6 | `intelligence-part2/sections/01_preliminaries.tex:12,72,73`; `intelligence-part2/sections/05_emergent_stopping_layer.tex:11,66,84` |
| INT-LEX-070 | P2E | `C_{\max}` | 2 | `intelligence-part2/sections/01_preliminaries.tex:31`; `intelligence-part2/sections/03_nonclosure_theorem.tex:11` |
| INT-LEX-071 | P2E | `\Omega_\theta` | 4 | `intelligence-part2/sections/01_preliminaries.tex:35,37,38`; `intelligence-part2/sections/03_nonclosure_theorem.tex:26` |
| INT-LEX-072 | P2E | `\theta` | 5 | `intelligence-part2/sections/01_preliminaries.tex:35,38,41`; `intelligence-part2/sections/03_nonclosure_theorem.tex:11,39` |
| INT-LEX-073 | P2E | `L` | 1 | `intelligence-part2/sections/01_preliminaries.tex:49` |
| INT-LEX-074 | P2E | `U` | 1 | `intelligence-part2/sections/01_preliminaries.tex:49` |
| INT-LEX-075 | P2E | `\Phi_{\text{ext}}` | 5 | `intelligence-part2/sections/01_preliminaries.tex:74`; `intelligence-part2/sections/05_emergent_stopping_layer.tex:92,96,103`; `intelligence-part2/sections/07_god.tex:6` |
| INT-LEX-076 | P2E | `\Phi_{\text{net}}` | 6 | `intelligence-part2/sections/01_preliminaries.tex:75`; `intelligence-part2/sections/05_emergent_stopping_layer.tex:92,103`; `intelligence-part2/sections/09_social_blockchain.tex:2,26,30` |
| INT-LEX-077 | P2E | `\mathcal{X}` | 1 | `intelligence-part2/sections/02_inference_operator.tex:8` |
| INT-LEX-078 | P2E | `F(x_n)` | 1 | `intelligence-part2/sections/02_inference_operator.tex:12` |
| INT-LEX-079 | P2E | `S` | 2 | `intelligence-part2/sections/02_inference_operator.tex:46,46` |
| INT-LEX-080 | P2E | `\nabla C` | 1 | `intelligence-part2/sections/03_nonclosure_theorem.tex:9` |
| INT-LEX-081 | P2E | `x_n` | 1 | `intelligence-part2/sections/03_nonclosure_theorem.tex:18` |
| INT-LEX-082 | P2E | `x^*` | 2 | `intelligence-part2/sections/03_nonclosure_theorem.tex:31,43` |
| INT-LEX-083 | P2E | `H_{ji}` | 1 | `intelligence-part2/sections/04_response_channels.tex:12` |
| INT-LEX-084 | P2E | `\Omega_{\text{life}}` | 1 | `intelligence-part2/sections/05_emergent_stopping_layer.tex:48` |
| INT-LEX-085 | P2E | `v_{\text{inf}}` | 2 | `intelligence-part2/sections/11_instability_region.tex:10,36` |
| INT-LEX-086 | P2E | `r_{\text{res}}` | 2 | `intelligence-part2/sections/11_instability_region.tex:11,36` |
| INT-LEX-087 | P2E | `\eta` | 2 | `intelligence-part2/sections/11_instability_region.tex:12,36` |
| INT-LEX-088 | P2E | `v_{LR}` | 1 | `intelligence-part2/sections/11_instability_region.tex:17` |
| INT-LEX-089 | P2AE | `C` | 1 | `intelligence-part2/appendices/appendix_a_master_table.tex:15` |
| INT-LEX-090 | P2AE | `C_{\max}` | 1 | `intelligence-part2/appendices/appendix_a_master_table.tex:16` |
| INT-LEX-091 | P2AE | `I` | 1 | `intelligence-part2/appendices/appendix_a_master_table.tex:17` |
| INT-LEX-092 | P2AE | `F` | 2 | `intelligence-part2/appendices/appendix_a_master_table.tex:18,19` |
| INT-LEX-093 | P2AE | `L_F` | 3 | `intelligence-part2/appendices/appendix_a_master_table.tex:19`; `intelligence-part2/appendices/appendix_b_homology.tex:26`; `intelligence-part2/appendices/appendix_c_part1_mapping.tex:8` |
| INT-LEX-094 | P2AE | `L_R` | 2 | `intelligence-part2/appendices/appendix_a_master_table.tex:20`; `intelligence-part2/appendices/appendix_e_emergence_homology.tex:21` |
| INT-LEX-095 | P2AE | `L_E` | 6 | `intelligence-part2/appendices/appendix_a_master_table.tex:21,22,28`; `intelligence-part2/appendices/appendix_b_homology.tex:26`; `intelligence-part2/appendices/appendix_e_emergence_homology.tex:21,22` |
| INT-LEX-096 | P2AE | `E` | 1 | `intelligence-part2/appendices/appendix_a_master_table.tex:22` |
| INT-LEX-097 | P2AE | `H_{ij}` | 2 | `intelligence-part2/appendices/appendix_a_master_table.tex:23`; `intelligence-part2/appendices/appendix_e_emergence_homology.tex:8` |
| INT-LEX-098 | P2AE | `\theta` | 2 | `intelligence-part2/appendices/appendix_a_master_table.tex:24`; `intelligence-part2/appendices/appendix_c_part1_mapping.tex:8` |
| INT-LEX-099 | P2AE | `\Omega_\theta` | 3 | `intelligence-part2/appendices/appendix_a_master_table.tex:24,25,26` |
| INT-LEX-100 | P2AE | `\mu_\theta` | 2 | `intelligence-part2/appendices/appendix_a_master_table.tex:26`; `intelligence-part2/appendices/appendix_c_part1_mapping.tex:20` |
| INT-LEX-101 | P2AE | `\Phi_{\text{ext}}` | 1 | `intelligence-part2/appendices/appendix_a_master_table.tex:27` |
| INT-LEX-102 | P2AE | `\Phi_{\text{net}}` | 3 | `intelligence-part2/appendices/appendix_a_master_table.tex:28`; `intelligence-part2/appendices/appendix_b_homology.tex:27`; `intelligence-part2/appendices/appendix_e_emergence_homology.tex:22` |
| INT-LEX-103 | P2AE | `v_{\text{inf}}` | 1 | `intelligence-part2/appendices/appendix_a_master_table.tex:29` |
| INT-LEX-104 | P2AE | `r_{\text{res}}` | 1 | `intelligence-part2/appendices/appendix_a_master_table.tex:30` |
| INT-LEX-105 | P2AE | `\eta` | 1 | `intelligence-part2/appendices/appendix_a_master_table.tex:31` |
| INT-LEX-106 | P2AE | `\Omega_{\text{life}}` | 2 | `intelligence-part2/appendices/appendix_b_homology.tex:24`; `intelligence-part2/appendices/appendix_e_emergence_homology.tex:20` |
| INT-LEX-107 | P2AE | `L` | 3 | `intelligence-part2/appendices/appendix_e_emergence_homology.tex:8,12,16` |
| INT-LEX-108 | P2AE | `U` | 3 | `intelligence-part2/appendices/appendix_e_emergence_homology.tex:8,12,16` |
| INT-LEX-109 | P2J | `L_F` | 174 | `intelligence-part2/sections/00_introduction_ja.tex:10,15,16,21,21,67,73,110,134,158,158,232,267,267,268,283,295,324,338`; `intelligence-part2/sections/01_preliminaries_ja.tex:260,272,276,276,287,309,310,362,362,364`; `intelligence-part2/sections/02_inference_operator_ja.tex:2,5,56,59,61,64,68,68,70,70,70,78,86,86,86,88,88,149,156,195,197,199,209,222,222,223,223,227,231`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:2,5,7,7,14,219,223,228,235,235,237,257,259,270,273,277,279`; `intelligence-part2/sections/04_response_channels_ja.tex:5,99,113,113,113,115,115,115,133,150`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:5,14,20,22,31,31,35,35,35,37,50,54,54,92,130,143,158,210,213,229,245,312,329,333,335,349,360`; `intelligence-part2/sections/09_social_blockchain_ja.tex:32,104,106`; `intelligence-part2/sections/10_gettier_problem_ja.tex:19,29,29,29,31,31,31,57,91,125,125,151`; `intelligence-part2/sections/11_instability_region_ja.tex:22,35,38,45,60,75,86,87,87,87,90,96,96,98,98,112,112,124,140,170,174,176,202,203`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:17,30,36,42,47,59,60,63,66,77,98,111,157,158`; `intelligence-part2/sections/13_conclusion_ja.tex:13,44,50,62,105,108,114,126,140` |
| INT-LEX-110 | P2J | `L_R` | 124 | `intelligence-part2/sections/00_introduction_ja.tex:10,16,17,110,129,129,232,269,270,295,324,338`; `intelligence-part2/sections/01_preliminaries_ja.tex:244,254,260,262,262,262,262,275,279,287,289,310,311,362,364`; `intelligence-part2/sections/02_inference_operator_ja.tex:70,70,86,199,207,227`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:7,223,237,257,259,277,279`; `intelligence-part2/sections/04_response_channels_ja.tex:5,104,111,113,113,115,115,117,117,131,131,133,149,150`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:5,7,14,20,22,22,22,37,42,47,50,54,54,54,56,67,67,67,75,80,90,90,90,102,124,131,144,159,174,178,193,215,216,216,219,314,329,333,349,360,361,364`; `intelligence-part2/sections/09_social_blockchain_ja.tex:33,136`; `intelligence-part2/sections/11_instability_region_ja.tex:45,60,89,90,90,90,93,93,98,98,124,174,202`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:17,33,62,66,77,98,111,158`; `intelligence-part2/sections/13_conclusion_ja.tex:50,50,62,105,140` |
| INT-LEX-111 | P2J | `L_E` | 294 | `intelligence-part2/sections/00_introduction_ja.tex:10,17,67,73,73,110,129,129,139,147,159,177,204,232,270,270,271,272,273,274,275,276,295,324,324,338`; `intelligence-part2/sections/01_preliminaries_ja.tex:35,244,255,256,260,262,262,278,287,311,312,314,314,316,362,364`; `intelligence-part2/sections/02_inference_operator_ja.tex:70,70,86,185,199,207,207,227`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:7,14,223,235,235,237,237,259,259,259,277,279`; `intelligence-part2/sections/04_response_channels_ja.tex:99,115,115,117,131,131,131,133,150,154`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:2,5,7,7,7,14,20,22,22,37,37,72,75,77,80,86,90,90,92,92,92,94,97,102,106,106,113,116,116,124,124,132,145,145,145,152,160,165,174,178,197,197,205,205,205,218,219,227,229,229,231,253,258,268,270,270,270,277,285,293,293,293,295,297,297,299,304,306,306,312,314,314,316,329,333,349,361,362,364,366,367`; `intelligence-part2/sections/06_animism_ja.tex:2,5,5,85,90,90,92,99,99,101,111,113,131,132`; `intelligence-part2/sections/07_god_ja.tex:2,5,62,62,62,64,74,79,80,94,116,125,125,141,162`; `intelligence-part2/sections/08_religion_ja.tex:2,5,54,115,115,129,129,129,141,145`; `intelligence-part2/sections/09_social_blockchain_ja.tex:2,5,32,90,118,120,120,120,120,125,127,132,136,136,144,148`; `intelligence-part2/sections/10_gettier_problem_ja.tex:2,19,19,19,31,66,68,80,91,91,103,125,125,127,139`; `intelligence-part2/sections/11_instability_region_ja.tex:22,41,49,60,60,63,75,75,92,93,93,93,96,96,98,98,105,108,110,110,110,110,112,112,112,112,112,124,140,144,154,158,170,174,174,202,203,203`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:17,30,36,42,44,45,45,47,63,65,66,69,69,77,90,98,111,118,137,138,157,158,161`; `intelligence-part2/sections/13_conclusion_ja.tex:13,50,50,50,62,91,94,105,128,140` |
| INT-LEX-112 | P2J | `\Phi` | 7 | `intelligence-part2/sections/00_introduction_ja.tex:12,120,124`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:241,299,299,299` |
| INT-LEX-113 | P2J | `F` | 72 | `intelligence-part2/sections/00_introduction_ja.tex:15,200,267,318`; `intelligence-part2/sections/01_preliminaries_ja.tex:90,119,119,125,160,197,273,276,308,309,312,362,362,364,366`; `intelligence-part2/sections/02_inference_operator_ja.tex:2,5,10,19,21,27,27,37,37,40,40,40,43,46,49,59,64,64,81,82,96,96,149,154,220,221,222,225`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:14,23,26,32,32,35,44,44,57,65,97,107,111,128,143,166,184`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:54,264,268,268,268,366`; `intelligence-part2/sections/13_conclusion_ja.tex:44,44` |
| INT-LEX-114 | P2J | `H_{ij}` | 46 | `intelligence-part2/sections/00_introduction_ja.tex:17,76,321`; `intelligence-part2/sections/01_preliminaries_ja.tex:212,226,226,235,239,279,311,315,364`; `intelligence-part2/sections/02_inference_operator_ja.tex:5,93,96,104,104,106,121,156,224`; `intelligence-part2/sections/04_response_channels_ja.tex:45,115,131`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:12,14,14,22,37,80,92,132,213,243,270,361,364`; `intelligence-part2/sections/07_god_ja.tex:125,125,125,127,129,157`; `intelligence-part2/sections/11_instability_region_ja.tex:93`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:66`; `intelligence-part2/sections/13_conclusion_ja.tex:47` |
| INT-LEX-115 | P2J | `L_F + L_R + L_E` | 3 | `intelligence-part2/sections/00_introduction_ja.tex:21`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:368`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:160` |
| INT-LEX-116 | P2J | `\Phi_{\text{net}}` | 80 | `intelligence-part2/sections/00_introduction_ja.tex:21,270,274,324`; `intelligence-part2/sections/01_preliminaries_ja.tex:256,314`; `intelligence-part2/sections/02_inference_operator_ja.tex:207`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:259`; `intelligence-part2/sections/04_response_channels_ja.tex:131`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:160,285,293,295,306,312,314,340,349,367`; `intelligence-part2/sections/06_animism_ja.tex:5,5,92,92,111,115,131,137`; `intelligence-part2/sections/07_god_ja.tex:5,62,64,72,74,74,96,96,105,108,110,116,116,118,123,129,137,154,155,157`; `intelligence-part2/sections/08_religion_ja.tex:5,54,97,129,133,145,162`; `intelligence-part2/sections/09_social_blockchain_ja.tex:2,90,106,113,118,118,144,165`; `intelligence-part2/sections/10_gettier_problem_ja.tex:41,62,66,78,103,153`; `intelligence-part2/sections/11_instability_region_ja.tex:60,144,158,158,170`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:17,30,44,69,75,98`; `intelligence-part2/sections/13_conclusion_ja.tex:50` |
| INT-LEX-117 | P2J | `E` | 32 | `intelligence-part2/sections/00_introduction_ja.tex:76,270,318`; `intelligence-part2/sections/01_preliminaries_ja.tex:30,287,312,313,316`; `intelligence-part2/sections/02_inference_operator_ja.tex:156,207`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:259`; `intelligence-part2/sections/04_response_channels_ja.tex:131`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:7,14,213,250,253,255,258,264,268,268,270,270,272,272,272,272,272,272,366`; `intelligence-part2/sections/13_conclusion_ja.tex:44` |
| INT-LEX-118 | P2J | `C, \nabla C` | 1 | `intelligence-part2/sections/00_introduction_ja.tex:102` |
| INT-LEX-119 | P2J | `J_C` | 2 | `intelligence-part2/sections/00_introduction_ja.tex:103`; `intelligence-part2/sections/01_preliminaries_ja.tex:55` |
| INT-LEX-120 | P2J | `\mu_\theta` | 146 | `intelligence-part2/sections/00_introduction_ja.tex:129,192,267,321`; `intelligence-part2/sections/01_preliminaries_ja.tex:29,30,30,100,287,287,289,316,364,364`; `intelligence-part2/sections/02_inference_operator_ja.tex:5,5,132,137,140,140,144,144,154,156,173,185,185,185,187,187,187,187,192,195,199,199,225,227`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:14`; `intelligence-part2/sections/04_response_channels_ja.tex:49,56,131`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:7,12,14,20,124,133,146,161,165,174,178,193,195,195,209,210,210,227,227,272,272,329,333,364,368`; `intelligence-part2/sections/06_animism_ja.tex:94,94,94,101,101,101,101,103,132`; `intelligence-part2/sections/08_religion_ja.tex:131,133,162`; `intelligence-part2/sections/10_gettier_problem_ja.tex:98,107,109,109,111,111,113,135,137,137,137,139,155`; `intelligence-part2/sections/11_instability_region_ja.tex:22,43,43,60,75,95,96,98,98,112,124,144,172,172,172,172,176,200,202,203`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:17,49,72,85,87,87,87,87,87,89,92,92,92,94,96,96,98,118,124,138,159,161`; `intelligence-part2/sections/13_conclusion_ja.tex:47,47,47,64,64,110,111,111,114,130,140,158` |
| INT-LEX-121 | P2J | `L_F + L_R + L_E + \Phi_{\text{net}}` | 1 | `intelligence-part2/sections/00_introduction_ja.tex:159` |
| INT-LEX-122 | P2J | `C, \nabla C, F_I, I, \Omega_\theta` | 1 | `intelligence-part2/sections/00_introduction_ja.tex:293` |
| INT-LEX-123 | P2J | `F, E, L_F, L_R, L_E, \Phi_{\text{ext}}, \Phi_{\text{net}}, H_{ij}, \mu_\theta, \eta, v_{\text{inf}}, r_{\text{res}}, \rho_{\text{resp}}` | 1 | `intelligence-part2/sections/00_introduction_ja.tex:293` |
| INT-LEX-124 | P2J | `\Phi_{\text{ext}}` | 18 | `intelligence-part2/sections/00_introduction_ja.tex:318,324`; `intelligence-part2/sections/01_preliminaries_ja.tex:313,314`; `intelligence-part2/sections/02_inference_operator_ja.tex:207`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:259`; `intelligence-part2/sections/04_response_channels_ja.tex:131`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:280,285,293,293,295,297,306,367`; `intelligence-part2/sections/13_conclusion_ja.tex:44,44,50` |
| INT-LEX-125 | P2J | `I` | 3 | `intelligence-part2/sections/01_preliminaries_ja.tex:11,74,80` |
| INT-LEX-126 | P2J | `F_I` | 3 | `intelligence-part2/sections/01_preliminaries_ja.tex:11,84,90` |
| INT-LEX-127 | P2J | `\Omega_\theta` | 18 | `intelligence-part2/sections/01_preliminaries_ja.tex:12,105,108,110,125,125,127,127,129,347`; `intelligence-part2/sections/02_inference_operator_ja.tex:149,152`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:44,168,277`; `intelligence-part2/sections/09_social_blockchain_ja.tex:104`; `intelligence-part2/sections/10_gettier_problem_ja.tex:109`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:90` |
| INT-LEX-128 | P2J | `C_{max}` | 14 | `intelligence-part2/sections/01_preliminaries_ja.tex:14,113,181,188,191`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:137,140,143,272`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:342`; `intelligence-part2/sections/11_instability_region_ja.tex:126`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:39`; `intelligence-part2/sections/13_conclusion_ja.tex:108,126` |
| INT-LEX-129 | P2J | `C` | 23 | `intelligence-part2/sections/01_preliminaries_ja.tex:27,53,60,62,62,62,72,137,344`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:14`; `intelligence-part2/sections/04_response_channels_ja.tex:58`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:316`; `intelligence-part2/sections/09_social_blockchain_ja.tex:148,170`; `intelligence-part2/sections/10_gettier_problem_ja.tex:5,80,80,80,91,91,111,135,154` |
| INT-LEX-130 | P2J | `\tau` | 1 | `intelligence-part2/sections/01_preliminaries_ja.tex:54` |
| INT-LEX-131 | P2J | `a, \Gamma, \kappa_B, C_*, C_{max}` | 1 | `intelligence-part2/sections/01_preliminaries_ja.tex:56` |
| INT-LEX-132 | P2J | `x` | 3 | `intelligence-part2/sections/01_preliminaries_ja.tex:60`; `intelligence-part2/sections/02_inference_operator_ja.tex:149`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:128` |
| INT-LEX-133 | P2J | `C(x)` | 1 | `intelligence-part2/sections/01_preliminaries_ja.tex:60` |
| INT-LEX-134 | P2J | `f` | 1 | `intelligence-part2/sections/01_preliminaries_ja.tex:80` |
| INT-LEX-135 | P2J | `\alpha` | 1 | `intelligence-part2/sections/01_preliminaries_ja.tex:90` |
| INT-LEX-136 | P2J | `\nabla C` | 13 | `intelligence-part2/sections/01_preliminaries_ja.tex:93,98,273`; `intelligence-part2/sections/02_inference_operator_ja.tex:81`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:12,111`; `intelligence-part2/sections/04_response_channels_ja.tex:16,19,144,144`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:130`; `intelligence-part2/sections/06_animism_ja.tex:20`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:60` |
| INT-LEX-137 | P2J | `\theta` | 40 | `intelligence-part2/sections/01_preliminaries_ja.tex:115,119,119,119,121,121,121,121,243`; `intelligence-part2/sections/02_inference_operator_ja.tex:27,144,144,144,149,152,154,158,161,161,165,169,178,178,178,225,226`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:14,44,44,277,277`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:210,210,229,229`; `intelligence-part2/sections/10_gettier_problem_ja.tex:109`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:87`; `intelligence-part2/sections/13_conclusion_ja.tex:47,105,105` |
| INT-LEX-138 | P2J | `\mathcal{X}` | 4 | `intelligence-part2/sections/01_preliminaries_ja.tex:137,139`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:184,184` |
| INT-LEX-139 | P2J | `x_i` | 1 | `intelligence-part2/sections/01_preliminaries_ja.tex:166` |
| INT-LEX-140 | P2J | `-\kappa_B/(C_{max} - C)` | 2 | `intelligence-part2/sections/01_preliminaries_ja.tex:184`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:153` |
| INT-LEX-141 | P2J | `\mathcal{U}` | 10 | `intelligence-part2/sections/01_preliminaries_ja.tex:212,212,223,223,226,226,229,229,235,239` |
| INT-LEX-142 | P2J | `\mathcal{L}` | 9 | `intelligence-part2/sections/01_preliminaries_ja.tex:212,212,223,223,226,226,229,235,239` |
| INT-LEX-143 | P2J | `C_{ij}` | 5 | `intelligence-part2/sections/01_preliminaries_ja.tex:242`; `intelligence-part2/sections/02_inference_operator_ja.tex:104,106`; `intelligence-part2/sections/04_response_channels_ja.tex:21,21` |
| INT-LEX-144 | P2J | `\vec{e}_i` | 1 | `intelligence-part2/sections/01_preliminaries_ja.tex:242` |
| INT-LEX-145 | P2J | `E(A)` | 5 | `intelligence-part2/sections/01_preliminaries_ja.tex:242,242`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:100,116`; `intelligence-part2/sections/13_conclusion_ja.tex:94` |
| INT-LEX-146 | P2J | `J` | 8 | `intelligence-part2/sections/01_preliminaries_ja.tex:243`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:41,41,184,184,188`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:241`; `intelligence-part2/sections/10_gettier_problem_ja.tex:19` |
| INT-LEX-147 | P2J | `\Omega_{\text{life}}` | 4 | `intelligence-part2/sections/01_preliminaries_ja.tex:243,251`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:101,113` |
| INT-LEX-148 | P2J | `\Omega_{\text{intel}}` | 3 | `intelligence-part2/sections/01_preliminaries_ja.tex:255`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:101,106` |
| INT-LEX-149 | P2J | `\rho_{\text{resp}}` | 3 | `intelligence-part2/sections/01_preliminaries_ja.tex:317`; `intelligence-part2/sections/06_animism_ja.tex:26,126` |
| INT-LEX-150 | P2J | `\eta` | 10 | `intelligence-part2/sections/01_preliminaries_ja.tex:318`; `intelligence-part2/sections/08_religion_ja.tex:103`; `intelligence-part2/sections/10_gettier_problem_ja.tex:139`; `intelligence-part2/sections/11_instability_region_ja.tex:40,41,41,66,73,110,200` |
| INT-LEX-151 | P2J | `v_{\text{inf}}` | 10 | `intelligence-part2/sections/01_preliminaries_ja.tex:319`; `intelligence-part2/sections/10_gettier_problem_ja.tex:139`; `intelligence-part2/sections/11_instability_region_ja.tex:34,35,63,73,87,154,158,200` |
| INT-LEX-152 | P2J | `r_{\text{res}}` | 10 | `intelligence-part2/sections/01_preliminaries_ja.tex:320`; `intelligence-part2/sections/10_gettier_problem_ja.tex:139`; `intelligence-part2/sections/11_instability_region_ja.tex:37,38,63,73,87,154,158,200` |
| INT-LEX-153 | P2J | `C, \nabla C, J_C, I, F_I, \Omega_\theta, C_{max}` | 1 | `intelligence-part2/sections/01_preliminaries_ja.tex:325` |
| INT-LEX-154 | P2J | `\Sigma` | 8 | `intelligence-part2/sections/01_preliminaries_ja.tex:325`; `intelligence-part2/sections/08_religion_ja.tex:88`; `intelligence-part2/sections/13_conclusion_ja.tex:90,91,91,91,142,159` |
| INT-LEX-155 | P2J | `(\mathcal{X}, C)` | 1 | `intelligence-part2/sections/01_preliminaries_ja.tex:348` |
| INT-LEX-156 | P2J | `x_n` | 4 | `intelligence-part2/sections/02_inference_operator_ja.tex:19,43`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:26,32` |
| INT-LEX-157 | P2J | `x_{n+1}` | 2 | `intelligence-part2/sections/02_inference_operator_ja.tex:43`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:26` |
| INT-LEX-158 | P2J | `i` | 3 | `intelligence-part2/sections/02_inference_operator_ja.tex:104,106`; `intelligence-part2/sections/04_response_channels_ja.tex:21` |
| INT-LEX-159 | P2J | `j` | 3 | `intelligence-part2/sections/02_inference_operator_ja.tex:104,106`; `intelligence-part2/sections/04_response_channels_ja.tex:21` |
| INT-LEX-160 | P2J | `\rho_i` | 1 | `intelligence-part2/sections/02_inference_operator_ja.tex:104` |
| INT-LEX-161 | P2J | `\lambda` | 1 | `intelligence-part2/sections/02_inference_operator_ja.tex:104` |
| INT-LEX-162 | P2J | `F(x;\theta)` | 2 | `intelligence-part2/sections/02_inference_operator_ja.tex:220`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:44` |
| INT-LEX-163 | P2J | `C_{\max}` | 1 | `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:14` |
| INT-LEX-164 | P2J | `x^*` | 2 | `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:57,95` |
| INT-LEX-165 | P2J | `\blacksquare` | 1 | `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:95` |
| INT-LEX-166 | P2J | `S` | 4 | `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:128,130,130,130` |
| INT-LEX-167 | P2J | `F'` | 3 | `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:130,130,130` |
| INT-LEX-168 | P2J | `S'` | 1 | `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:130` |
| INT-LEX-169 | P2J | `\kappa_B/(C_{max}-C)` | 1 | `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:167` |
| INT-LEX-170 | P2J | `H_{ij}, H_{ji}` | 1 | `intelligence-part2/sections/04_response_channels_ja.tex:21` |
| INT-LEX-171 | P2J | `v_{LR}` | 2 | `intelligence-part2/sections/11_instability_region_ja.tex:45,45` |
| INT-LEX-172 | P2AJ | `C` | 2 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:24`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:92` |
| INT-LEX-173 | P2AJ | `C_{max}` | 9 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:25`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:22,25`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:33,75,75`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:57,60,69` |
| INT-LEX-174 | P2AJ | `\nabla C` | 2 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:26,29` |
| INT-LEX-175 | P2AJ | `J_C` | 1 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:27` |
| INT-LEX-176 | P2AJ | `I` | 1 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:28` |
| INT-LEX-177 | P2AJ | `F_I` | 1 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:29` |
| INT-LEX-178 | P2AJ | `\Omega_\theta` | 6 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:30,31,147,150`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:58`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:86` |
| INT-LEX-179 | P2AJ | `\theta` | 23 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:30,31,96,147,150,185,190,194,204`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:47,82,87,91`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:58,58`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:131,135,177,177,181,181`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:95,101` |
| INT-LEX-180 | P2AJ | `H_{ij}` | 21 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:32,60,150`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:39,43,48`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:121,125,131,141,145`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:43,57,57,60,76,95,114,120,140,141` |
| INT-LEX-181 | P2AJ | `\tau` | 1 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:33` |
| INT-LEX-182 | P2AJ | `F` | 14 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:56,57,58,77,147`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:111,115,124`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:75`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:13,21,38,50,84` |
| INT-LEX-183 | P2AJ | `J` | 4 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:57`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:47`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:129`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:94` |
| INT-LEX-184 | P2AJ | `L_F` | 17 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:58,59,114,115`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:22`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:29,32,58,58,109,136`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:99,103,103,105,105`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:109` |
| INT-LEX-185 | P2AJ | `L_R` | 14 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:59,60`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:48`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:58,111,112,113`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:105,139,145`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:109,113,120,120` |
| INT-LEX-186 | P2AJ | `L_E` | 38 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:59,60,77,79,79,116,133,152`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:23,24,48,136,140,147,175`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:32,58,58,111,112,113`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:105,105,137,143,145,145,155,161,163`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:104,106,109,115,120,120,123,162` |
| INT-LEX-187 | P2AJ | `E` | 2 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:77,150` |
| INT-LEX-188 | P2AJ | `\Phi_{\text{ext}}` | 5 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:78,79`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:155,159,163` |
| INT-LEX-189 | P2AJ | `\Phi_{\text{net}}` | 9 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:78,79`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:136,140`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:113`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:155,161,163`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:104` |
| INT-LEX-190 | P2AJ | `\Phi` | 4 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:79`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:70`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:27,27` |
| INT-LEX-191 | P2AJ | `\mu_\theta` | 29 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:96,150,199,199`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:136,140,172,172`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:30,84,89,92,92,111,112,113,115,138`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:145,170,173,175,177,177,179,181,181`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:114,120` |
| INT-LEX-192 | P2AJ | `\rho_{\text{resp}}` | 2 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:97,97` |
| INT-LEX-193 | P2AJ | `H_{ji}` | 1 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:97` |
| INT-LEX-194 | P2AJ | `v_{\text{inf}}` | 1 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:114` |
| INT-LEX-195 | P2AJ | `r_{\text{res}}` | 1 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:115` |
| INT-LEX-196 | P2AJ | `\eta` | 2 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:116,116` |
| INT-LEX-197 | P2AJ | `\Sigma` | 1 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:133` |
| INT-LEX-198 | P2AJ | `x` | 3 | `intelligence-part2/appendices/appendix_a_master_table_ja.tex:147`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:30,50` |
| INT-LEX-199 | P2AJ | `E(A)` | 9 | `intelligence-part2/appendices/appendix_b_homology_ja.tex:23,46`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:121,123`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:71,76,77,85,123` |
| INT-LEX-200 | P2AJ | `\Omega_{\text{life}}` | 4 | `intelligence-part2/appendices/appendix_b_homology_ja.tex:23,47`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:133`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:96` |
| INT-LEX-201 | P2AJ | `\Omega_{\text{intel}}` | 2 | `intelligence-part2/appendices/appendix_b_homology_ja.tex:24`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:104` |
| INT-LEX-202 | P2AJ | `\mathcal{L}` | 16 | `intelligence-part2/appendices/appendix_b_homology_ja.tex:39,43`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:119,125,125,129,139`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:43,43,54,54,57,60,75,94,113` |
| INT-LEX-203 | P2AJ | `\mathcal{U}` | 16 | `intelligence-part2/appendices/appendix_b_homology_ja.tex:39,43`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:123,125,133,143`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:43,43,54,54,57,60,60,77,96,115` |
| INT-LEX-204 | P2AJ | `C_{ij}` | 4 | `intelligence-part2/appendices/appendix_b_homology_ja.tex:46`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:119`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:71,75` |
| INT-LEX-205 | P2AJ | `\vec{e}_i` | 3 | `intelligence-part2/appendices/appendix_b_homology_ja.tex:46`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:119`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:75` |
| INT-LEX-206 | P2AJ | `J_I` | 1 | `intelligence-part2/appendices/appendix_b_homology_ja.tex:70` |
| INT-LEX-207 | P2AJ | `F(x;\theta)` | 2 | `intelligence-part2/appendices/appendix_b_homology_ja.tex:119`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:28` |
| INT-LEX-208 | P2AJ | `x^*` | 2 | `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:13,36` |
| INT-LEX-209 | P2AJ | `x_n` | 1 | `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:21` |
| INT-LEX-210 | P2AJ | `x_{n+1}` | 1 | `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:21` |
| INT-LEX-211 | P2AJ | `\blacksquare` | 7 | `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:36,52,91,105,147,165,181` |
| INT-LEX-212 | P2AJ | `S` | 3 | `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:50,52,52` |
| INT-LEX-213 | P2AJ | `F'` | 3 | `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:52,52,52` |
| INT-LEX-214 | P2AJ | `S'` | 1 | `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:52` |
| INT-LEX-215 | P2AJ | `-\kappa_B/(C_{max} - C)` | 1 | `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:64` |
| INT-LEX-216 | P2AJ | `\kappa_B/(C_{max}-C)` | 1 | `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:85` |
| INT-LEX-217 | P2AJ | `i` | 2 | `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:163,163` |
| INT-LEX-218 | P2AJ | `j, k, \ldots` | 1 | `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:163` |

## 32. Prose mathematical-relation index

以下16familiesはTeX delimiter外の関係語を、本文・heading・table・captionのsource-context付きで追跡する。これは新しい式/主張数ではない。matched line countsは重複family間で重なる検索出現数で、headingや否定・反証仮定を除外して正の命題へ変換しない。直前の98 rawdisplays/131 substantiveinlineと一部文脈を共有し、別母数。premise/proof/HOMOFORMでactualassertionとguardを区分した。全inlinefamiliesは94mathlexical+16proserelation=110。

| ID | Relation family | Matched source lines | Exact representative line | All source line locators | Tracking boundary |
|---|---|---:|---|---|---|
| INT-INLINE-095 | monotonicity / strict advancement | 18 | \textbf{P2: Monotonic justification measure.} There exists a measure $J$ such that | `intelligence-part2/sections/03_nonclosure_theorem.tex:20`; `intelligence-part2/sections/10_gettier_problem.tex:14`; `intelligence-part2/sections/01_preliminaries_ja.tex:80,308`; `intelligence-part2/sections/02_inference_operator_ja.tex:51`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:25,32,35,97,184,188,270`; `intelligence-part2/sections/04_response_channels_ja.tex:77`; `intelligence-part2/sections/11_instability_region_ja.tex:18,199`; `intelligence-part2/appendices/appendix_a_master_table_ja.tex:56`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:21,38` | EQF026/THM001; admissibility qualifier preserved |
| INT-INLINE-096 | fixed-point absence / counterfactual | 59 | This paper develops Intelligence Part II of the VED/IFGT theory tree. Its central claim is that inference does not contain an internal fixed point: the inference layer $L_F$ cannot close itself by inference alone. Stable intelligence therefore requires stopping structures that are externalized, projected, maintained, revised, and synchronized through emergent stopping layers. The paper introduces the three-layer dynamics $L_F/L_R/L_E$, defines the emergent stopping layer $L_E$, analyzes historical stopping operations such as animism, God, religion, science, institutions, and social blockchain, and derives a phase diagram in which intelligence persists only between divergence and rigidity. Stopping is not treated as the negation of freedom. Rather, movable and revisable stopping is the condition under which finite intelligence can sustain open-ended inference. | `intelligence-part2/main.tex:15`; `intelligence-part2/sections/00_introduction.tex:6`; `intelligence-part2/sections/03_nonclosure_theorem.tex:2,11,31,43,51,57`; `intelligence-part2/sections/12_constructive_clauses.tex:8`; `intelligence-part2/sections/13_conclusion.tex:8`; `intelligence-part2/appendices/appendix_b_homology.tex:26`; `intelligence-part2/appendices/appendix_c_part1_mapping.tex:8`; `intelligence-part2/sections/00_introduction_ja.tex:28,268`; `intelligence-part2/sections/01_preliminaries_ja.tex:172,197,366`; `intelligence-part2/sections/02_inference_operator_ja.tex:231`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:2,5,14,51,57,65,75,89,95,97,128,130,143,166,184,199,201,247,250,270`; `intelligence-part2/sections/04_response_channels_ja.tex:89,92,93`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:31`; `intelligence-part2/sections/13_conclusion_ja.tex:44,108,126`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:22,174`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:31,75`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:13,28,34,36,52,60,68,69,84,103` | EQF027; hypotheticalexistence vsconclusion distinguished |
| INT-INLINE-097 | internal stopping absence | 94 | From this structure, the Gettier problem is reinterpreted not as a defect in the definition of knowledge, but as a mismatch between a stopping structure and the dynamical property it is asked to guarantee. Accumulated correctness does not stabilize intelligence. Instead, it increases inferential connectivity and generates a branching explosion. Therefore intelligence cannot be stabilized within an individual system alone: no stopping operator exists internally. | `intelligence-part1/sections/abstract.tex:5`; `intelligence-part1/sections/06_the_gettier_problem_as_a_structural_diagnostic.tex:37`; `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex:59,64`; `intelligence-part1/sections/08_the_non_closure_of_individual_intelligence.tex:7,20,24,32,40,47`; `intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex:7,15,52,77`; `intelligence-part1/sections_ja/02_the_decomposition_perception_recognition_knowledge_and_intelligence_ja.tex:20`; `intelligence-part1/sections_ja/06_the_gettier_problem_as_a_structural_diagnostic_ja.tex:114`; `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:245`; `intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex:85,149`; `intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex:159,228`; `intelligence-part2/main.tex:15`; `intelligence-part2/sections/00_introduction.tex:6,12`; `intelligence-part2/sections/02_inference_operator.tex:40`; `intelligence-part2/sections/03_nonclosure_theorem.tex:9,53,59,63`; `intelligence-part2/sections/04_response_channels.tex:4`; `intelligence-part2/sections/05_emergent_stopping_layer.tex:26,57`; `intelligence-part2/sections/11_instability_region.tex:29`; `intelligence-part2/sections/12_constructive_clauses.tex:8`; `intelligence-part2/sections/13_conclusion.tex:8`; `intelligence-part2/appendices/appendix_b_homology.tex:26`; `intelligence-part2/appendices/appendix_c_part1_mapping.tex:12,16`; `intelligence-part2/appendices/appendix_d_optional_notes.tex:8`; `intelligence-part2/sections/00_introduction_ja.tex:15,134,158,183`; `intelligence-part2/sections/01_preliminaries_ja.tex:273,309`; `intelligence-part2/sections/02_inference_operator_ja.tex:68,197,209,222`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:116,121,124,128,130,169,195,237,250,271,277`; `intelligence-part2/sections/04_response_channels_ja.tex:5,77,79,89`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:14,31,35,245,268,270`; `intelligence-part2/sections/07_god_ja.tex:58`; `intelligence-part2/sections/10_gettier_problem_ja.tex:29,31,125,151`; `intelligence-part2/sections/11_instability_region_ja.tex:7,63,87,100,154,156,158,170,206`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:36,42`; `intelligence-part2/sections/13_conclusion_ja.tex:31,44`; `intelligence-part2/appendices/appendix_a_master_table_ja.tex:58`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:43,46,50,52,103` | EQF028/044; predicate vsmotion vsjudgment |
| INT-INLINE-098 | closure bound / unreachable | 25 | \item 個体内推論からは外化された停止構造を内部状態として直接生成できない(到達不可能性) | `intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex:159,227,379`; `intelligence-part2/sections/01_preliminaries_ja.tex:186,192`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:14,140,143,153,223,272`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:342`; `intelligence-part2/sections/10_gettier_problem_ja.tex:45,105`; `intelligence-part2/sections/11_instability_region_ja.tex:126`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:39`; `intelligence-part2/sections/13_conclusion_ja.tex:108,126`; `intelligence-part2/appendices/appendix_a_master_table_ja.tex:25`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:22`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:33,75`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:57,60,69` | EQF018; reciprocalterm andclaimedconsequence distinct |
| INT-INLINE-099 | state connectivity | 32 | The paper proposes three minimal axiomatic conditions: a connected state space, temporal ordering, and a global constraint $\Phi$. These conditions are not presented as a complete theory of intelligence, but as a lower bound on the kind of dynamics required for intelligence-like motion. They distinguish perception, recognition, knowledge, and intelligence as different structural layers. The paper then compares two radically different substrates, the reticulate dynamics of \emph{Physarum polycephalum} and the layer transitions of Transformer architectures, and reads both through the same structural conditions. In particular, the flow-reinforcement dynamics of the Physarum solver formulated by Tero, Kobayashi, and Nakagaki (2007) already exhibits a structure homologous to the emergence of $\Phi$ as a global constraint irreducible to local update rules. | `intelligence-part1/sections/abstract.tex:3`; `intelligence-part1/sections/01_introduction.tex:43`; `intelligence-part1/sections/03_minimal_axioms_of_intelligence.tex:11,13,33,80,88`; `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex:15,32,62`; `intelligence-part1/sections/10_summary_convergence_and_outlook.tex:16,35`; `intelligence-part1/sections_ja/abstract_ja.tex:3`; `intelligence-part1/sections_ja/01_introduction_ja.tex:47`; `intelligence-part1/sections_ja/02_the_decomposition_perception_recognition_knowledge_and_intelligence_ja.tex:106`; `intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex:13,16,24,26,115,179`; `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:67`; `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:36,37,91,98,147`; `intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex:40`; `intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex:29`; `intelligence-part2/sections/00_introduction_ja.tex:12,118`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:27` | EQF043; topology notinvented |
| INT-INLINE-100 | global irreducibility | 9 | The paper proposes three minimal axiomatic conditions: a connected state space, temporal ordering, and a global constraint $\Phi$. These conditions are not presented as a complete theory of intelligence, but as a lower bound on the kind of dynamics required for intelligence-like motion. They distinguish perception, recognition, knowledge, and intelligence as different structural layers. The paper then compares two radically different substrates, the reticulate dynamics of \emph{Physarum polycephalum} and the layer transitions of Transformer architectures, and reads both through the same structural conditions. In particular, the flow-reinforcement dynamics of the Physarum solver formulated by Tero, Kobayashi, and Nakagaki (2007) already exhibits a structure homologous to the emergence of $\Phi$ as a global constraint irreducible to local update rules. | `intelligence-part1/sections/abstract.tex:3`; `intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex:84`; `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:77,165`; `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:116`; `intelligence-part2/sections/09_social_blockchain_ja.tex:88,90`; `intelligence-part2/sections/13_conclusion_ja.tex:17`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:24` | EQF002; scalar map vs globalrole |
| INT-INLINE-101 | homology / same formal structure | 91 | The paper proposes three minimal axiomatic conditions: a connected state space, temporal ordering, and a global constraint $\Phi$. These conditions are not presented as a complete theory of intelligence, but as a lower bound on the kind of dynamics required for intelligence-like motion. They distinguish perception, recognition, knowledge, and intelligence as different structural layers. The paper then compares two radically different substrates, the reticulate dynamics of \emph{Physarum polycephalum} and the layer transitions of Transformer architectures, and reads both through the same structural conditions. In particular, the flow-reinforcement dynamics of the Physarum solver formulated by Tero, Kobayashi, and Nakagaki (2007) already exhibits a structure homologous to the emergence of $\Phi$ as a global constraint irreducible to local update rules. | `intelligence-part1/sections/abstract.tex:3`; `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex:7,53,78,84`; `intelligence-part1/sections/08_the_non_closure_of_individual_intelligence.tex:32`; `intelligence-part1/sections_ja/abstract_ja.tex:3`; `intelligence-part1/sections_ja/01_introduction_ja.tex:17`; `intelligence-part1/sections_ja/02_the_decomposition_perception_recognition_knowledge_and_intelligence_ja.tex:9`; `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:11,75,156,165,167`; `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:11,126,132,135,158,160,163,172,174,177,180,183,186,211,215,229,238`; `intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex:156,164,180,191,228,285,288,367`; `intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex:151`; `intelligence-part2/sections/05_emergent_stopping_layer.tex:92`; `intelligence-part2/sections/13_conclusion.tex:22`; `intelligence-part2/appendices/appendix_b_homology.tex:2,4,31`; `intelligence-part2/appendices/appendix_e_emergence_homology.tex:2`; `intelligence-part2/sections/00_introduction_ja.tex:324`; `intelligence-part2/sections/01_preliminaries_ja.tex:100,199,231,314`; `intelligence-part2/sections/02_inference_operator_ja.tex:207`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:137,140,143,174,259,272`; `intelligence-part2/sections/04_response_channels_ja.tex:131`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:7,243,277,282,285,295,297,299,367`; `intelligence-part2/sections/07_god_ja.tex:62,64,116,154`; `intelligence-part2/sections/09_social_blockchain_ja.tex:35`; `intelligence-part2/sections/10_gettier_problem_ja.tex:111`; `intelligence-part2/sections/13_conclusion_ja.tex:50,72,108`; `intelligence-part2/appendices/appendix_a_master_table_ja.tex:78,171`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:101,171`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:33,75`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:57,60,91,147,155,165`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:123,162` | HOMOFORM; no implicit map |
| INT-INLINE-102 | equivalence / fallibility | 29 | The two systems differ in substrate, scale, and implementation. Nonetheless, both can be described as satisfying the same minimal structural conditions. This does not imply cognitive identity, experiential identity, functional identity, or ethical equivalence. | `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex:71`; `intelligence-part2/sections/03_nonclosure_theorem.tex:35`; `intelligence-part2/sections/10_gettier_problem_ja.tex:98,101,103,105,107,135,137,155`; `intelligence-part2/sections/11_instability_region_ja.tex:22`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:71,72,77,98,111,158,160`; `intelligence-part2/sections/13_conclusion_ja.tex:47,111`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:172`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:89,92`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:170,173,175,177,179,181` | EQF034/037; bidirectionalclaimsnotproofjudgment |
| INT-INLINE-103 | gradient and motion | 14 | として表現されるスカラー場である。$\Phi_\text{bio}$ は栄養源勾配・エネルギーコスト・物理的境界条件を統合した大域的制約であり、\S{}3.3 で要請した \textbf{局所更新規則の単純集約への非還元性} を満たす。局所的に well-defined な flow-reinforcement だけでは shortest path は現れない ── 大域条件が局所動態を制約することで、初めて大域構造が動的に創発する(\S{}4.4.3 を参照)。 | `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:55,116`; `intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex:254,285,291`; `intelligence-part2/sections/00_introduction.tex:6`; `intelligence-part2/sections/01_preliminaries.tex:22`; `intelligence-part2/sections/02_inference_operator.tex:26`; `intelligence-part2/sections/01_preliminaries_ja.tex:90`; `intelligence-part2/sections/02_inference_operator_ja.tex:81`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:12,111`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:130`; `intelligence-part2/appendices/appendix_a_master_table_ja.tex:26` | EQF011/022/023; no complete trajectoryderivation |
| INT-INLINE-104 | branch/node/edge growth | 40 | From this structure, the Gettier problem is reinterpreted not as a defect in the definition of knowledge, but as a mismatch between a stopping structure and the dynamical property it is asked to guarantee. Accumulated correctness does not stabilize intelligence. Instead, it increases inferential connectivity and generates a branching explosion. Therefore intelligence cannot be stabilized within an individual system alone: no stopping operator exists internally. | `intelligence-part1/sections/abstract.tex:5`; `intelligence-part1/sections/01_introduction.tex:47`; `intelligence-part1/sections/06_the_gettier_problem_as_a_structural_diagnostic.tex:37`; `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex:40,51,55,57,64,71`; `intelligence-part1/sections/08_the_non_closure_of_individual_intelligence.tex:5`; `intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex:5,52,77`; `intelligence-part1/sections/10_summary_convergence_and_outlook.tex:19`; `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:130`; `intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex:37,50,56,95,111,112,117,140,205,210,259`; `intelligence-part2/sections/00_introduction.tex:6,35`; `intelligence-part2/sections/02_inference_operator.tex:36`; `intelligence-part2/sections/03_nonclosure_theorem.tex:55,59`; `intelligence-part2/sections/04_response_channels.tex:34`; `intelligence-part2/sections/05_emergent_stopping_layer.tex:76`; `intelligence-part2/appendices/appendix_c_part1_mapping.tex:10,12`; `intelligence-part2/sections/00_introduction_ja.tex:200`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:195,197`; `intelligence-part2/sections/04_response_channels_ja.tex:89`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:26` | EQF014/015; comparator/countmeaning |
| INT-INLINE-105 | convergence / minimum / stable attractor | 56 | This position has also been reached independently in biophysics. Research on \emph{Physarum polycephalum} since Nakagaki et al. (2000) has described intelligent behavior without attributing intelligence as a possessed property \citep{Nakagaki2000,Tero2007}. Nakagaki's formulation, that slime mold does not possess intelligence but behaves intelligently, converges with the present paper's central position from a very different research path. | `intelligence-part1/sections/01_introduction.tex:35`; `intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex:62`; `intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex:73,75`; `intelligence-part1/sections/10_summary_convergence_and_outlook.tex:1,5,29,31,37`; `intelligence-part1/sections_ja/01_introduction_ja.tex:38`; `intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex:115,128`; `intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex:65,188,193,201,222`; `intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex:11,388`; `intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex:1,7,9,58,61,64,81,88,110,181`; `intelligence-part2/sections/05_emergent_stopping_layer.tex:67,73`; `intelligence-part2/sections/01_preliminaries_ja.tex:242`; `intelligence-part2/sections/04_response_channels_ja.tex:97`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:97,100,102,116,215,216,219,224,364`; `intelligence-part2/sections/08_religion_ja.tex:88`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:39`; `intelligence-part2/sections/13_conclusion_ja.tex:94`; `intelligence-part2/appendices/appendix_a_master_table_ja.tex:175`; `intelligence-part2/appendices/appendix_b_homology_ja.tex:23,24,46`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:34`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:123`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:77,82,85,120,123` | EQF032/041/054; no limitmode |
| INT-INLINE-106 | threshold / domain reconfiguration | 93 | Let $\Omega_\theta$ denote the movement region available under a constraint parameter $\theta$. We distinguish two movement types: | `intelligence-part2/sections/01_preliminaries.tex:35,38,41`; `intelligence-part2/sections/03_nonclosure_theorem.tex:11,26`; `intelligence-part2/sections/04_response_channels.tex:20`; `intelligence-part2/sections/05_emergent_stopping_layer.tex:17,59,65,66,73`; `intelligence-part2/sections/11_instability_region.tex:48`; `intelligence-part2/sections/12_constructive_clauses.tex:20`; `intelligence-part2/sections/13_conclusion.tex:10,34`; `intelligence-part2/appendices/appendix_a_master_table.tex:25`; `intelligence-part2/appendices/appendix_c_part1_mapping.tex:20`; `intelligence-part2/sections/00_introduction_ja.tex:35,38,129,192,321`; `intelligence-part2/sections/01_preliminaries_ja.tex:30,100,287,316,364`; `intelligence-part2/sections/02_inference_operator_ja.tex:5,132,137,140,151,152,156,173,185,187,195,199,225`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:14,44,277`; `intelligence-part2/sections/04_response_channels_ja.tex:49,131`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:7,12,133,161,202,209,210,227,229,272,329,364`; `intelligence-part2/sections/06_animism_ja.tex:94`; `intelligence-part2/sections/08_religion_ja.tex:131,133`; `intelligence-part2/sections/10_gettier_problem_ja.tex:107,109,111,137,155`; `intelligence-part2/sections/11_instability_region_ja.tex:5,43,96,112,172,186`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:17,85,89,90,92,96,118,159,161`; `intelligence-part2/sections/13_conclusion_ja.tex:46,47,111,130,157`; `intelligence-part2/appendices/appendix_a_master_table_ja.tex:84,96,149,199`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:58,92`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:173,177` | EQF030/037; operationrole notoperator |
| INT-INLINE-107 | necessity / exclusion formal prose | 150 | From this structure, the Gettier problem is reinterpreted not as a defect in the definition of knowledge, but as a mismatch between a stopping structure and the dynamical property it is asked to guarantee. Accumulated correctness does not stabilize intelligence. Instead, it increases inferential connectivity and generates a branching explosion. Therefore intelligence cannot be stabilized within an individual system alone: no stopping operator exists internally. | `intelligence-part1/sections/abstract.tex:5`; `intelligence-part1/sections/01_introduction.tex:21,43,55,62`; `intelligence-part1/sections/02_the_decomposition_perception_recognition_knowledge_and_intelligence.tex:5,34`; `intelligence-part1/sections/03_minimal_axioms_of_intelligence.tex:19,21,25,45,83`; `intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex:67`; `intelligence-part1/sections/06_the_gettier_problem_as_a_structural_diagnostic.tex:5,15,33,37`; `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex:5,38`; `intelligence-part1/sections/08_the_non_closure_of_individual_intelligence.tex:40`; `intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex:5,7,15,38,44,52,74,88,93`; `intelligence-part1/sections/10_summary_convergence_and_outlook.tex:13,16,24,27,43,55,64`; `intelligence-part1/sections_ja/01_introduction_ja.tex:36,66`; `intelligence-part1/sections_ja/02_the_decomposition_perception_recognition_knowledge_and_intelligence_ja.tex:22`; `intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex:63`; `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:9`; `intelligence-part1/sections_ja/06_the_gettier_problem_as_a_structural_diagnostic_ja.tex:76,163,183,190`; `intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex:15,83,167,373,409`; `intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex:34,53,55,159,227,228,341,379`; `intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex:41,44,49,139,188,231`; `intelligence-part2/main.tex:15`; `intelligence-part2/sections/01_preliminaries.tex:41`; `intelligence-part2/sections/02_inference_operator.tex:28,32`; `intelligence-part2/sections/03_nonclosure_theorem.tex:4,9,11,63`; `intelligence-part2/sections/04_response_channels.tex:32`; `intelligence-part2/sections/05_emergent_stopping_layer.tex:19,24`; `intelligence-part2/sections/06_animism.tex:6`; `intelligence-part2/sections/09_social_blockchain.tex:26`; `intelligence-part2/sections/11_instability_region.tex:29,46,47,48,59`; `intelligence-part2/sections/12_constructive_clauses.tex:8,12,24`; `intelligence-part2/sections/13_conclusion.tex:8`; `intelligence-part2/appendices/appendix_d_optional_notes.tex:4`; `intelligence-part2/sections/00_introduction_ja.tex:32,158,183,303,318`; `intelligence-part2/sections/02_inference_operator_ja.tex:88`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:7,116,121,153,169,211,216,223,228,235,237,259`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:245,268,333,335`; `intelligence-part2/sections/06_animism_ja.tex:52`; `intelligence-part2/sections/09_social_blockchain_ja.tex:90,92,108,163`; `intelligence-part2/sections/10_gettier_problem_ja.tex:24,31,33,43,45,47,82,98,101,105,111,113,125,151,152,155`; `intelligence-part2/sections/11_instability_region_ja.tex:96,114,140,178,188`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:5,42,87,134,159`; `intelligence-part2/sections/13_conclusion_ja.tex:17,44,47,155`; `intelligence-part2/appendices/appendix_a_master_table_ja.tex:96`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:75,92`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:43,96`; `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex:25` | source-strengthindex; scope/negative/counterfactualcontextretained |
| INT-INLINE-108 | sufficiency / lower bound | 19 | The paper proposes three minimal axiomatic conditions: a connected state space, temporal ordering, and a global constraint $\Phi$. These conditions are not presented as a complete theory of intelligence, but as a lower bound on the kind of dynamics required for intelligence-like motion. They distinguish perception, recognition, knowledge, and intelligence as different structural layers. The paper then compares two radically different substrates, the reticulate dynamics of \emph{Physarum polycephalum} and the layer transitions of Transformer architectures, and reads both through the same structural conditions. In particular, the flow-reinforcement dynamics of the Physarum solver formulated by Tero, Kobayashi, and Nakagaki (2007) already exhibits a structure homologous to the emergence of $\Phi$ as a global constraint irreducible to local update rules. | `intelligence-part1/sections/abstract.tex:3`; `intelligence-part1/sections/03_minimal_axioms_of_intelligence.tex:7,21,51,83`; `intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex:81`; `intelligence-part1/sections/06_the_gettier_problem_as_a_structural_diagnostic.tex:11,33`; `intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex:59`; `intelligence-part1/sections/08_the_non_closure_of_individual_intelligence.tex:32`; `intelligence-part1/sections/10_summary_convergence_and_outlook.tex:27`; `intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex:143,179,183`; `intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex:29,49,212`; `intelligence-part2/sections/06_animism.tex:6`; `intelligence-part2/sections/02_inference_operator_ja.tex:88` | P1axiom/definitionboundary |
| INT-INLINE-109 | frequency / quantification / time units | 14 | \item $I$ は「情報量」の量化ではなく、\textbf{累積度の構造的尺度} である | `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:56`; `intelligence-part2/sections/11_instability_region.tex:15`; `intelligence-part2/sections/13_conclusion.tex:28`; `intelligence-part2/sections/01_preliminaries_ja.tex:325`; `intelligence-part2/sections/02_inference_operator_ja.tex:178`; `intelligence-part2/sections/11_instability_region_ja.tex:35`; `intelligence-part2/sections/13_conclusion_ja.tex:90,91,142,159`; `intelligence-part2/appendices/appendix_a_master_table_ja.tex:114,121,133,204` | UNIT/TIME; futurequantification notcurrentdefinition |
| INT-INLINE-110 | region / containment / fixed-domain scope | 31 | 本論文の \textbf{射程外} は明示的に以下を含む: | `intelligence-part1/sections_ja/01_introduction_ja.tex:56`; `intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex:180`; `intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex:85`; `intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex:173`; `intelligence-part2/sections/01_preliminaries.tex:37,41`; `intelligence-part2/sections/03_nonclosure_theorem.tex:11,26,39`; `intelligence-part2/appendices/appendix_c_part1_mapping.tex:8`; `intelligence-part2/sections/01_preliminaries_ja.tex:251,260`; `intelligence-part2/sections/02_inference_operator_ja.tex:149`; `intelligence-part2/sections/03_nonclosure_theorem_ja.tex:14,44,223,277`; `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex:229`; `intelligence-part2/sections/07_god_ja.tex:62`; `intelligence-part2/sections/11_instability_region_ja.tex:96`; `intelligence-part2/sections/12_constructive_clauses_ja.tex:30,49,57,96,122`; `intelligence-part2/sections/13_conclusion_ja.tex:33`; `intelligence-part2/appendices/appendix_a_master_table_ja.tex:58,147,152`; `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex:58`; `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex:105` | EQF030/036; scopeclausesnotimplicitsharedspace |

## 33. Phase01 uncertainty continuation

INT-U-001–048は変更・解決扱いにしない。以下はformal/object/signature面の新規46entries、INT-U-049–094。総数94。既存authorityuncertaintyへのリンクは解決ではなく細分化である。

| ID | Issue | Reference | Unresolved formal boundary |
|---|---|---|---|
| INT-U-049 | P1 S topology/cardinality | EQF043 / SYM001 | 連結性とdiscretegraph許容の下で、後続gradient/flowに用いるspaceが同じか未確定 |
| INT-U-050 | P1 F update contract | EQF001 | discrete recurrenceとcontinuous-order許容を結ぶsignature未指定 |
| INT-U-051 | global Φ and emergence Φ | EQF002/031 | scalarfieldとtwo-inputemergenceoperatorの共通typeは未提示 |
| INT-U-052 | Φbio / Φtr state domains | EQF003/004 | 同じS記号が生物networkとhiddenstatesでどのspaceを表すか未統一 |
| INT-U-053 | Physarum graph specification | EQF063 | directedness/cardinality/edgeconditionsがformalizedbranchinggraphへ継承されるか不明 |
| INT-U-054 | Q/D/L/pressure unit relation | EQF005/006 | quantityroles以外のunit/normalization未指定; p_i独立定義未確認 |
| INT-U-055 | nonlinear response example | EQF007 | JApowerμ>0が例か全instantiation条件か、normalization範囲未固定 |
| INT-U-056 | Bio discrete vscontinuous | EQF045/046 | P1FbioとP2F(x;θ)のupdate/ordertranslation未提示 |
| INT-U-057 | Transformer signature | EQF008/009 | hidden-state dimensions/layerparameterdependenceの完全contract未指定 |
| INT-U-058 | edge growth assumptions | EQF014 | 二次edgegrowthのgraphclass/密度/limit条件未指定 |
| INT-U-059 | branch depth counting | EQF015 | b^dがexactdepthかdepthまでか、b可変の場合の範囲未指定 |
| INT-U-060 | correctness-to-flow evaluation | EQF012 | propositionpへのdivergenceevaluationmap未指定 |
| INT-U-061 | I increase relation | EQF010/013/019 | accumulation↑とf(1−C)のorder/range対応未指定 |
| INT-U-062 | Internal/External operator domains | EQF016/044 | R/Tのtype、internalcollection、externalmembershipcriterion未定義 |
| INT-U-063 | closure PDE domain | EQF017 | Xdimension/geometry/regularityとdifferentialoperatorsの適用domain未固定 |
| INT-U-064 | closure PDE IC/BC | EQF017/018 | initialdata/BC/invariantdomainの設定はsourceでは未提示 |
| INT-U-065 | C/f normalization | EQF018/019 | Cmax/C*/1−Cのscale/range関係未指定 |
| INT-U-066 | f example domains | EQF020/021 | linear/logexampleのargument admissibility/rangeおよびintendeduse未指定 |
| INT-U-067 | PDE parameter units/signs | EQF017 | a/Γ/κB/Δとtime/fluxの整合条件を実際に採用しているか未固定 |
| INT-U-068 | force/flux/update linkage | EQF022/023/025 | FI/JCgradientrelationからinferenceFへのtypedconversion未提示 |
| INT-U-069 | Cij vs C | EQF029/024 | indexedrelationからscalarlandscapeへのaggregation/identification未指定 |
| INT-U-070 | admissible states for strictJ | EQF026/047 | X全体とadmissiblestate subsetの量化範囲未完全 |
| INT-U-071 | single-valued vs set-valued F | EQF025/048 | Jへの集合引数の扱い/継続候補選択と定理域の関係未指定 |
| INT-U-072 | probabilistic F and strictincrease | EQF025/026 | pathwise/expected/selectedcontinuationのどの読みかsource明示なし |
| INT-U-073 | P3 role in theorem | THM001/PREM005–007 | fixedθscopeとJAgrounding記述の代数的前提上の位置未完全 |
| INT-U-074 | stopping predicate bridge | THM002 | S=1→Ffixedpointのformal条件は独立列挙されていない |
| INT-U-075 | F-prime theorem applicability | THM002 | 補助推論F'についてP1/P2がどのように再成立するか個別premise未提示 |
| INT-U-076 | barrier-to-inaccessibility transition | THM003 | reciprocaldivergenceとfull-evolution noncrossingの関係を指定するdomain/BC未提示 |
| INT-U-077 | Cmax/F/DH isomorphism | THM003 | objects/map/inverse/invariantの署名未提示 |
| INT-U-078 | Ωintel subset Ωlife | EQF036 | cross-domainambientspace/embedding未提示 |
| INT-U-079 | U/L script variants | EQF031 | U/calU,L/calLの対象同一性とemergenceoperatorcontract未確定 |
| INT-U-080 | LE layer vsattractor | EQF032 / §24 | input/output/attractorstatespaceとLRreferenceprocessのtype未統一 |
| INT-U-081 | external E typing | EQF033 | operatorEとE[LE,xn]出力のtype、{F^k}index/composition範囲未指定 |
| INT-U-082 | E-site projection | EQF054/OP025 | projectiondomain/codomain/operatorと単なるplaceassignmentの関係未指定 |
| INT-U-083 | Con window symbols | TIME008/MUTHETA010 | TΦ/Δv/μ/τとIntcapacity/timeへのtypedtranslation未提示 |
| INT-U-084 | LR convergence toLE | EQF054 | convergence mode/conditions/limitobjectのformal指定未提示 |
| INT-U-085 | Φext/Φnet identity contract | EQF034 | functionalfield/networkview間のmap/inverse・sameobjectcriteria未指定 |
| INT-U-086 | error-tolerance equivalence predicates | EQF037 | fallibility/revisability/μcapacityの個別predicateと量化範囲未指定 |
| INT-U-087 | μθ numerical status | MUTHETA001–010 | capacity/shift/rate/controlのどのtypeか未固定; units未指定 |
| INT-U-088 | speed difference calibration | EQF038 | vinfとvLRのstep/time/counting compatibility未指定 |
| INT-U-089 | Σ distinct fromphase space | EQF039/040 | Σは発達度・活性度、phase-regionsetではない。量化はfutureで対象の測り方未固定 |
| INT-U-090 | Master v2.1 exact formal provenance | MASTER018–027 | reprintedrelationの原artifact/version/当時signature対応未確定 |
| INT-U-091 | appendixD language contracts | APPFORM010–012 | JAproofcollectionとENoptionalnotesのformalcoverage差・共有claimscope未統一 |
| INT-U-092 | stopping functional tense/type | EQF041/APPFORM013–014 | bodyfuture vsappendixlocalminimumpresent; functionalexpression/domain未提示 |
| INT-U-093 | figure-only formal additions | FIGFORM004/013 | Ncounts/common-growth-scale/phaseband境界をbodyvariablesへ戻すformalrule未提示 |
| INT-U-094 | responsive threshold relation | THM012/013 | H/axesからresponseclassificationへのthresholdfunction未指定; structuralsilence/continuousboundaryのscope差 |

## 34. Included-source SHA-256 / coverage manifest

| ID | Source file | Task-start SHA-256 | Displays | All inline |
|---|---|---|---|---|
| INT-SOURCE-001 | intelligence-part1/main.tex | b379d762a9b70a2388f764573563e0faf07aa2451adc74c8e9effce17a390eb5 | 0 | 0 |
| INT-SOURCE-002 | intelligence-part1/sections/abstract.tex | 2aea790ea2bb5b48feec6420dcaadb8394201efb2f0405950d838c83253803e6 | 0 | 2 |
| INT-SOURCE-003 | intelligence-part1/sections/01_introduction.tex | fce9e87ce405d4401dd9d3800e7b760e7d754c39c20b5c23ce6969c312a488df | 0 | 8 |
| INT-SOURCE-004 | intelligence-part1/sections/02_the_decomposition_perception_recognition_knowledge_and_intelligence.tex | f51159e1a73679be2134d685dfe7e66ee2af6410f0c9770d15e90b78dbe238f4 | 0 | 0 |
| INT-SOURCE-005 | intelligence-part1/sections/03_minimal_axioms_of_intelligence.tex | 19b62e0dce76b1b78aa3728878addd89b92fe1714177fc616cde244bceb158fa | 3 | 9 |
| INT-SOURCE-006 | intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex | 6831b761736d6eb6b53976dae2808a0582166cffe03d34bb024764e978149f44 | 2 | 28 |
| INT-SOURCE-007 | intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex | 749192dfa136931342cf1e923129d3e895358c437083d066151835a95f7d4189 | 4 | 8 |
| INT-SOURCE-008 | intelligence-part1/sections/06_the_gettier_problem_as_a_structural_diagnostic.tex | 9780738104625b2adf91fea9e09c666279a135f688738f3409f1bc92de32dc10 | 0 | 0 |
| INT-SOURCE-009 | intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex | b258af49381ecdddd922642903648efad5605e8c9cc2cbf3df9a3e6c3b5fd201 | 3 | 10 |
| INT-SOURCE-010 | intelligence-part1/sections/08_the_non_closure_of_individual_intelligence.tex | 6f1d10fad999d59b8c7ef8a5a327ffd5622e7bdffb48307cc38f9d150a8bf1bf | 1 | 3 |
| INT-SOURCE-011 | intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex | 64739052c34b31677c943603967b15f1cd89edadea3a0ff98e3bbeeb6ec7fd5b | 2 | 2 |
| INT-SOURCE-012 | intelligence-part1/sections/10_summary_convergence_and_outlook.tex | 642823265843d5a357e1060ce5b1e17ba415158ce17463c7fe6dce682359c0fe | 0 | 1 |
| INT-SOURCE-013 | intelligence-part1/main_ja.tex | 29791c11407a84ee9659d8ca2040e1731613e502bf52f7a8392ed49ef5875e94 | 0 | 0 |
| INT-SOURCE-014 | intelligence-part1/sections_ja/abstract_ja.tex | d4c4c29987b67de82a7872d1e8848d5499c4c3147f9388ec49c3d4fcfe50c3d4 | 0 | 2 |
| INT-SOURCE-015 | intelligence-part1/sections_ja/01_introduction_ja.tex | d0ac607901cc7cb35b58aa261f370377f504caa187e6cccf24da9ccb5a7d7938 | 0 | 8 |
| INT-SOURCE-016 | intelligence-part1/sections_ja/02_the_decomposition_perception_recognition_knowledge_and_intelligence_ja.tex | 450abf27584fb2026e0093e91eacf4f3a8587a2d30e41e4d7fc08610332189ba | 0 | 1 |
| INT-SOURCE-017 | intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex | c70bee06ce91223cc34f0514b17c8d4f3be395733e41961a50f74af3f736c990 | 3 | 23 |
| INT-SOURCE-018 | intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex | 904621d6cd46f38bf3009db0b4218c504b04b4f4bbf08e6d20dfa94543f2365b | 2 | 61 |
| INT-SOURCE-019 | intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex | 7fc5ae659598710a58a397c09aadf6cc735fabd19e8b1d9ebc71ec1214e121e0 | 5 | 22 |
| INT-SOURCE-020 | intelligence-part1/sections_ja/06_the_gettier_problem_as_a_structural_diagnostic_ja.tex | 9970c15afaa031451e5a3504ca91a4b8ff9d38ec82ea1ffde74e249303221927 | 0 | 15 |
| INT-SOURCE-021 | intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex | 255b84c6e25cfa758e1b2105c759e79b4b2a6e7272d62897842490e97678d2dc | 4 | 30 |
| INT-SOURCE-022 | intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex | 54276e1e0e73d68968347d1b36b04521b357e5ca7309c1cea3f119bf4eb0701f | 1 | 29 |
| INT-SOURCE-023 | intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex | b75818a137e8c2a4a9bb822dab89a25f82149a8c27dd69fd0e90060e524da3d5 | 2 | 6 |
| INT-SOURCE-024 | intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex | a4d541fe41c0f43494a6a198f44d7f9c76d4aa4f96ef772e1e5ba2f5f8318b08 | 0 | 9 |
| INT-SOURCE-025 | intelligence-part2/main.tex | a04533374c7b78cf10d07483203cbf87d9624f25a5416c67b2fad0c1e1555009 | 0 | 3 |
| INT-SOURCE-026 | intelligence-part2/preamble.tex | 7ad544b5851a1486f94e633eda03a73fa0ff1857aff146f1bbb4c843f5aaa66c | 0 | 0 |
| INT-SOURCE-027 | intelligence-part2/sections/00_introduction.tex | 1f57408a0f5bcc14b8694ba25c73aa09d34d2ef300564c246091ed67768eaa4a | 1 | 12 |
| INT-SOURCE-028 | intelligence-part2/sections/01_preliminaries.tex | 847e52dfa72ef31c351e1a77fc8617ff226a2bd9b7940be1fc50ccc99bb4c389 | 4 | 34 |
| INT-SOURCE-029 | intelligence-part2/sections/02_inference_operator.tex | 9064f86751cefe477403e471b2ebe0462d6c67f8a6cd1c48b90b30a9c0e332b7 | 5 | 11 |
| INT-SOURCE-030 | intelligence-part2/sections/03_nonclosure_theorem.tex | 411df8cdf89904c628b395b9183d4593409f47cf3d929fd8aa72e0c10e1432f0 | 5 | 25 |
| INT-SOURCE-031 | intelligence-part2/sections/04_response_channels.tex | 28fe3ba7e74d3b294b4cd0c48ab941ac5bb1681fdf33aae44764646ad07bf6ad | 0 | 10 |
| INT-SOURCE-032 | intelligence-part2/sections/05_emergent_stopping_layer.tex | 1f9926d30db3abc008327e38d409b5ba2d746a0789b4737fd90e53654882511a | 4 | 66 |
| INT-SOURCE-033 | intelligence-part2/sections/06_animism.tex | 7cd29f4f546b9f8a4a6eebba5a5e4be9b1f9c7c07df43233531ba215c0fcdc4f | 1 | 1 |
| INT-SOURCE-034 | intelligence-part2/sections/07_god.tex | a4bef4d5297ac48c0a3c546365f99d84b6f22d2b92b88f10f0197ee1778146e5 | 1 | 1 |
| INT-SOURCE-035 | intelligence-part2/sections/08_religion.tex | 3c34e62c40de7e3a32e17b5e570d93425f9f7bc0faaddb0cf501a2c78140ebfd | 1 | 1 |
| INT-SOURCE-036 | intelligence-part2/sections/09_social_blockchain.tex | 75ea660e6dc1b5c1bd8b33db0def9b24d20077455b15a6c25e27c1a68834f369 | 0 | 12 |
| INT-SOURCE-037 | intelligence-part2/sections/10_gettier_problem.tex | 04b04412708c896d55d93406a28ff3f076797c4ff232f0807303c7ae0eb4b3b8 | 2 | 7 |
| INT-SOURCE-038 | intelligence-part2/sections/11_instability_region.tex | b9a24b3a4ef3d7ce650c55d7fd9dfe8708f9e9800163982aacc92725f8add1f6 | 1 | 32 |
| INT-SOURCE-039 | intelligence-part2/sections/12_constructive_clauses.tex | 23b5d759b08b5a844df71b638a2b6eeaaaa6e8436b26e50291eed3e7fa2967d7 | 1 | 9 |
| INT-SOURCE-040 | intelligence-part2/sections/13_conclusion.tex | d6577f6c9c471a8cca1a2bfc06e7acfe1e16cb4436ceadb3bc6aa36bef2cc39f | 0 | 13 |
| INT-SOURCE-041 | intelligence-part2/appendices/appendix_a_master_table.tex | 22ed8b2e49283129637e35845e427a55cbeb4b9e4e8af943df58882689df0d2e | 0 | 22 |
| INT-SOURCE-042 | intelligence-part2/appendices/appendix_b_homology.tex | 2ea76b46b95ec3a702e8ce2146b2999075de2b05ce6846d11679c6a50b0ceeba | 1 | 4 |
| INT-SOURCE-043 | intelligence-part2/appendices/appendix_c_part1_mapping.tex | 0b3be4305ff1720110b8db690e4b190f976ac8aba9afe947aaeab9823069c743 | 0 | 3 |
| INT-SOURCE-044 | intelligence-part2/appendices/appendix_d_optional_notes.tex | 0442614f780af1e72a4c6fd6e1d7ca8bb9c52732828dcce01d0d7437edd7441b | 0 | 0 |
| INT-SOURCE-045 | intelligence-part2/appendices/appendix_e_emergence_homology.tex | 56e1dd3ed93603b01ddee642db5621a7983542c00d63475fbfaccfa0edeca83e | 1 | 12 |
| INT-SOURCE-046 | intelligence-part2/main_ja.tex | 682cd3c52f4d57787dcffa46a31150e3218f71015a64177f8a50bac5ae131a18 | 0 | 0 |
| INT-SOURCE-047 | intelligence-part2/preamble_ja.tex | 8b6dcc74ff465fb7554b3e460f7b3d13a88000d5726138fdc830152ee6df6b4b | 0 | 0 |
| INT-SOURCE-048 | intelligence-part2/sections/00_introduction_ja.tex | a88d12931e94d8ef1b73e5732b88c591d9e39e93545f05fd88cf06df13ce8eac | 6 | 90 |
| INT-SOURCE-049 | intelligence-part2/sections/01_preliminaries_ja.tex | b3e741b48e172cf12d1d128bd7dd57c888093f3e1e028053ba13614b64659570 | 6 | 189 |
| INT-SOURCE-050 | intelligence-part2/sections/02_inference_operator_ja.tex | d59df3d7f753b3d9443174dea2dc2989a223ac192f4bf3e6ec8f0a454b35b47a | 4 | 144 |
| INT-SOURCE-051 | intelligence-part2/sections/03_nonclosure_theorem_ja.tex | 6129d0497f9a3bd8d52bf3b7537f455607613783f25de2a946396a05acb9cb30 | 7 | 111 |
| INT-SOURCE-052 | intelligence-part2/sections/04_response_channels_ja.tex | 8537110058a546e97a736d38d1d0ec55721e4499423d2cae46f6252879eaeb9f | 1 | 56 |
| INT-SOURCE-053 | intelligence-part2/sections/05_emergent_stopping_layer_ja.tex | 20458d301121f2281375a3d6912500d770d0d087a77e5ec3c60f18ae891691cc | 4 | 255 |
| INT-SOURCE-054 | intelligence-part2/sections/06_animism_ja.tex | c71bfdbc777278a12010d1961d76feb1648e67f0c4cd9e82550808e7a81b2b84 | 0 | 36 |
| INT-SOURCE-055 | intelligence-part2/sections/07_god_ja.tex | 57a492d897ad0d501076a7c5563ca2e7ffd876f7a6d01f06fd144e1e7d42275b | 2 | 43 |
| INT-SOURCE-056 | intelligence-part2/sections/08_religion_ja.tex | fc77ea33ee6d194a6c080a822a2b91d5e8421c6058646a764a32fa57525bdc6d | 0 | 22 |
| INT-SOURCE-057 | intelligence-part2/sections/09_social_blockchain_ja.tex | c5c4356ca105a264bbbf976c88c994a965802a7a6f67e5bf2240c6b10dcf49ad | 0 | 32 |
| INT-SOURCE-058 | intelligence-part2/sections/10_gettier_problem_ja.tex | 4bb1419f9617f9077dff8fe3e438a4a7f47f6974c6817f7e5511a2c7d233209f | 0 | 62 |
| INT-SOURCE-059 | intelligence-part2/sections/11_instability_region_ja.tex | bf61aee0613d53a955425ee356a6eabd58e9d321ddc291bff1b84aee93f4b290 | 1 | 133 |
| INT-SOURCE-060 | intelligence-part2/sections/12_constructive_clauses_ja.tex | b75c5c809bbbcbdde9abde01f14ee569bd8cc7e49ff579e0195fd64ef218dcce | 0 | 79 |
| INT-SOURCE-061 | intelligence-part2/sections/13_conclusion_ja.tex | cc2aa0e7c319170c68685d6d5418f7924804a9fd131a6df3edce863393797606 | 0 | 56 |
| INT-SOURCE-062 | intelligence-part2/appendices/appendix_a_master_table_ja.tex | 4e1154ffb4b6851e16495e5dc0af8fe34a590f05592b0539ca4fd81a73223e17 | 5 | 74 |
| INT-SOURCE-063 | intelligence-part2/appendices/appendix_b_homology_ja.tex | 59adc70ebaa16d6784c600bc4f4bfee3685dbd4cedbacee38c48a6025305816e | 0 | 47 |
| INT-SOURCE-064 | intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex | 1c69f380873fa966f018a71b463d7e0ff72bd200d42eb3722bb2a9c81b3a4ee6 | 0 | 39 |
| INT-SOURCE-065 | intelligence-part2/appendices/appendix_d_optional_notes_ja.tex | bd9f007ef751498d494573e956e19909d4f14c578df2cfbc130e60a9f0818ee2 | 1 | 115 |
| INT-SOURCE-066 | intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex | 26a4258a8a33094132cf9f01aff6362ad771d84e17aafefd17c434daa363a098 | 1 | 61 |

## 35. Validation

### 35.1 Coverage and count reconciliation

| Check | Result / denominator |
|---|---|
| Input graph | 66/66 TeXfiles; main4 + preamble2 + body/abstract50 + appendix10 |
| Display raw occurrences | 98/98; P1E15/P1J17/P2E26/P2J31/P2AE2/P2AJ7 |
| Display environments | 90 bracket displays + 8 dollar-dollar; no numbered-equation label located |
| All inline math | 2199 occurrences = 131 substantive math + 2068 residual symbol/lexeme occurrences |
| Inline grouping | 94 math lexical families + 16 prose-relation families = 110; proseindex774 matched lines / 622 distinct source lines (overlap not independentclaims) |
| Residual lexical coverage | 218 stream-specific groups cover2068 occurrences; exactfile/lineindex retained |
| Phase00 EQF draft | 35/35; merge0, split5, retainedunsplit30; descendants42 + newlyseparated21 = final63 |
| Signature counts (EQF63 denominator) | EXPLICIT6 / INFERRED1 / PARTIAL34 / UNRESOLVED20 / CONFLICTING2 |
| Symbols/operators | 102symbolfamilies (97text/comparison +5figure-only supplements); 32operatorfamilies |
| Indices/domains/time/units | 14index / 23domain / 12time; unitstatus63/63EQF rows |
| Definitions / objects | 32/32 INT-DEF and32/32 INT-OBJ crosswalked |
| Phase00 glyph collisions | 22/22 crosswalked; notationrisks notcircularity |
| Theorem-like families | 13; 34premisefamilies;40proof-stepfamilies; no validityassessment |
| EN/JA formal variants | 36: SAME10 / JA STRONGER4 / EN STRONGER0 / DIFFERENT7 / JA ONLY13 / EN ONLY2 / CONFLICTING0 / UNKNOWN0 |
| Appendices | 10files / 5language-pairedfamilies;14formalrelationfamilies; rawdisplays9 |
| Master table | EN17symbolrows + JA24symbolrows + JA3timescalecomparisonrows =44; combinedformula displays counted separately |
| Homology | 21/21 formalizationstatuses |
| Figures | 14/14 families, bothlanguages; currentSVGtext/captionformalinventory; no figure/PDF rebuild |
| Dedicated subsystems | branching4layers, nonclosuredependencyroute, LF/LR/LE, μθ10entries, Φ8/F6/J5/E3/C5roles separated |
| Completeness markers | 13subsystems; sourcepresence only, not evidence sufficiency |
| New uncertainty IDs | INT-U-049–094,46new; old001–048unchanged; total94 |

### 35.2 Task-start SHA-256 / unchanged-source validation

開始時snapshotは既存1491files（ignored含む、.git除外）。開始時からdirtyworktreeであり、既存変更を本監査の変更と誤認しない。snapshot JSONは `${TEMP_EVIDENCE_ROOT}/int_phase01.FQ1Sb9/baseline.json`、SHA-256 `a0e15b7c7cf678bee702be8390012cd05bd8df1a1aa63adfd6c853f1a423dda2`。path→hash mapのsortedcompactJSON digestは `8e56bff17e3f84c04086052d6d1e5d21bf97e28c72b8f53ca846118949c8dae3`。全includedsource66のindividualhashは§34に永続記録した。

Phase00recordのtask-start/final SHA-256は `ffb891b9039a71a2173574652f72776a307be6618070a74f2fcc64bc0a312d64`。extract JSON SHA-256 `68ce050f2e046dd16a0076b073f58e5db3f914126cd6c180f0b3fc42eae8bb2e` はrawextractionの参照用であり、後のfamilyclassificationを含むファイルではない。snapshot/extraction/validation用scriptはtemp内の監査補助で、理論simulation/codeexecutionではない。

最終比較の許可集合は本recordとREADMEのみ。source/equations/figures/PDF/BibTeX/MD/他branch/Phase00recordをbyte単位で保持する。README以外の既存1490files不変、新規repositoryfileは本record1のみを検証する。既存1491filesに削除なし。raw98blocksはsource該当line範囲とcodefence内容を個別照合し、locator/id欠落なしを確認する。

`git diff --check`に加え、untrackedrecordを `git diff --no-index --check /dev/null <record>` で検査する。完全gitstatusは開始時snapshotとの比較対象とし、既存約250行のdirty状態を消さない。

実測結果: SHA-256比較PASS（既存1490files不変、README1変更、新規record1、削除0）。raw98blocks・全ledger連番・uncertainty049–094の照合PASS。`git diff --check`はexit0・出力なし。untrackedrecordのno-index checkもwhitespace diagnosticなし（exit1は新規file差分ありの通常結果）。`git status --short`は250行でtask-start表示と同一。監査directory全体が既にuntracked表示のため新規recordはstatus行数に現れないが、全filehash比較で上記2fileのみの変更を確認した。

### 35.3 Non-actions / limitations

数学・定理・証明の正否、解釈truth、循環性、evidence sufficiency、final dispositionは判定しない。completeはinventorycoverageに限る。図の形式的roleはSVG/source textから確認し、compiledassetの再render・PDFfreshness再判定は行わない。外部research、simulation、build、source/notation修正、新規theory/bridge、commit/pushは未実施。

## 36. Stop boundary

Phase01 inventory COMPLETE。Phase02 role / definition / homology auditへ進まない。形式的不足や署名競合候補はINT-Uへ保持し、式・証明・主張を修復しない。

# Consciousness Phase 01 — equation / symbol / object / signature inventory v0.1

## 0. Status

Consciousness audit: **IN PROGRESS**。Phase 00: COMPLETE。Phase 01: **COMPLETE**。Phase 02 formal / neural / cognitive / phenomenal role audit: **NOT STARTED**。

2026-09-09、current local repositoryを対象とするidentity inventory。式の役割の最終分類、神経・認知機構、現象的説明、循環性、実証適合、妥当性、claim dispositionは判定しない。以下のIDと分類表は監査索引であり新しい理論notationではない。式の掲載は原文引用であり、新式の提案ではない。

上流VED equation audit / core revision、Bio-IFGT audit / core revisionはCLOSEDのまま。source・式・図・PDF・simulation・過去の監査は変更しない。Phase 00 uncertaintyを上書きしない。

## 1. Authority

最初に[Phase 00](00_dependency_inheritance_and_authority_record_v0.1_ja.md)と[監査README](README_ja.md)を読み、実際のentry/inputを再確認した。S00–S20はPhase 00 §2のsource pairをそのまま使用する。`S06:301`はENの行、`JA S06:245`はJAの行。省略したsource名の逆引きは次表による。EN/JAはともにmodular buildであり、JA working Markdownをcanonicalとは扱わない。

| Source ID | EN current input | JA current input | Display EN / JA |
| --- | --- | --- | --- |
| S00 | [abstract](../../consciousness/sections/abstract.tex) | [abstract JA](../../consciousness/sections_ja/abstract_ja.tex) | 0 / 0 |
| S01 | [introduction](../../consciousness/sections/introduction.tex) | [introduction JA](../../consciousness/sections_ja/introduction_ja.tex) | 0 / 0 |
| S02 | [intuitive_picture](../../consciousness/sections/intuitive_picture.tex) | [intuitive_picture JA](../../consciousness/sections_ja/intuitive_picture_ja.tex) | 0 / 0 |
| S03 | [notation](../../consciousness/sections/notation.tex) | [notation JA](../../consciousness/sections_ja/notation_ja.tex) | 0 / 0 |
| S04 | [sso](../../consciousness/sections/sso.tex) | [sso JA](../../consciousness/sections_ja/sso_ja.tex) | 3 / 3 |
| S05 | [torque_converter_attention](../../consciousness/sections/torque_converter_attention.tex) | [torque_converter_attention JA](../../consciousness/sections_ja/torque_converter_attention_ja.tex) | 5 / 8 |
| S06 | [formal_mapping](../../consciousness/sections/formal_mapping.tex) | [formal_mapping JA](../../consciousness/sections_ja/formal_mapping_ja.tex) | 14 / 14 |
| S07 | [core_equations](../../consciousness/sections/core_equations.tex) | [core_equations JA](../../consciousness/sections_ja/core_equations_ja.tex) | 17 / 18 |
| S08 | [structural_interpretation](../../consciousness/sections/structural_interpretation.tex) | [structural_interpretation JA](../../consciousness/sections_ja/structural_interpretation_ja.tex) | 2 / 7 |
| S09 | [dynamics_log_referencing](../../consciousness/sections/dynamics_log_referencing.tex) | [dynamics_log_referencing JA](../../consciousness/sections_ja/dynamics_log_referencing_ja.tex) | 4 / 4 |
| S10 | [experimental_reinterpretation](../../consciousness/sections/experimental_reinterpretation.tex) | [experimental_reinterpretation JA](../../consciousness/sections_ja/experimental_reinterpretation_ja.tex) | 4 / 4 |
| S11 | [qualia_boundary](../../consciousness/sections/qualia_boundary.tex) | [qualia_boundary JA](../../consciousness/sections_ja/qualia_boundary_ja.tex) | 2 / 2 |
| S12 | [opening_model](../../consciousness/sections/opening_model.tex) | [opening_model JA](../../consciousness/sections_ja/opening_model_ja.tex) | 1 / 1 |
| S13 | [measurement_collapse](../../consciousness/sections/measurement_collapse.tex) | [measurement_collapse JA](../../consciousness/sections_ja/measurement_collapse_ja.tex) | 2 / 6 |
| S14 | [non_localization](../../consciousness/sections/non_localization.tex) | [non_localization JA](../../consciousness/sections_ja/non_localization_ja.tex) | 1 / 4 |
| S15 | [qualitative_predictions](../../consciousness/sections/qualitative_predictions.tex) | [qualitative_predictions JA](../../consciousness/sections_ja/qualitative_predictions_ja.tex) | 12 / 17 |
| S16 | [pathologies_limits](../../consciousness/sections/pathologies_limits.tex) | [pathologies_limits JA](../../consciousness/sections_ja/pathologies_limits_ja.tex) | 0 / 11 |
| S17 | [relation_to_note](../../consciousness/sections/relation_to_note.tex) | [relation_to_note JA](../../consciousness/sections_ja/relation_to_note_ja.tex) | 1 / 1 |
| S18 | [discussion](../../consciousness/sections/discussion.tex) | [discussion JA](../../consciousness/sections_ja/discussion_ja.tex) | 0 / 0 |
| S19 | [conclusion](../../consciousness/sections/conclusion.tex) | [conclusion JA](../../consciousness/sections_ja/conclusion_ja.tex) | 5 / 5 |
| S20 | [correspondence_map](../../consciousness/sections/correspondence_map.tex) | [correspondence_map JA](../../consciousness/sections_ja/correspondence_map_ja.tex) | 0 / 0 |

Current-facing textは44 TeX（entry 2 + inputs 42）とshared [refs.bib](../../consciousness/refs.bib)。全44 TeXを表示式抽出対象にした。2つのdraft EN（公開版未収録: `../../consciousness/draft_en.md`） / draft JA（公開版未収録: `../../consciousness/draft_ja.md`）はSource status付きworking/historicalであり、旧式・旧名称をcurrent equation件数へ加算しない。branch専用READMEはない。root [EN](../../README.md) / [JA](../../README_ja.md)と[concept map](../../docs/navigation/concept_map.md)はnavigation authorityである。

Upstream照合先は[VED equation inventory](../ved_equation_audit/01_equation_inventory_v0.1_ja.md)、[VED final record](../ved_equation_audit/06_final_audit_record_v1.0_ja.md)、[Bio identity inventory](../bio_ifgt_audit/01_equation_and_symbol_inventory_v0.1_ja.md)、[Bio final record](../bio_ifgt_audit/07_final_audit_record_v1.0_ja.md)、[Bio closure recheck](../bio_ifgt_audit/implementation_final_consistency_recheck_v1.1_ja.md)。現在の式のlocatorは§13–14を優先し、過去のinventoryによる引用同定とcurrent sourceそのものを区別する。

Guard（結論ではない）: upstream vocabulary reuse ≠ upstream derivation、formal object ≠ neural carrier、neural carrier ≠ cognitive function、cognitive function ≠ phenomenal experience、same glyph ≠ same object、same phrase ≠ same signature、same structure ≠ identity。sourceがidentityを述べる場合もSOURCE CLAIMSとして記録する。

## 2. Full equation inventory

抽出単位はdisplay environment一個。`equation/align/gather/multline`のstar variants、`displaymath`、bracket display、double-dollarを検索し、commentを除外した。結果はequation 176、bracket 2、その他0。inline math、table内inline math、図中数式はこの178件に混入させず、§4以降に別記する。句読点・演算子・添字・空白を含むraw blockを保存し、式の正規化によるsource統合はしない。

出現順はEN entry順の001–073、JA entry順の074–178。各式は独立IDを持つ。F番号は空白列を1個にした**文字列表現family**（52種）であり、object/roleの同一性を認定するものではない。元式の改行・delimiterを含むexact raw blockを各行直後に保存する。数式はsourceからの引用で、新しい理論式ではない。

### CON-EQ-001

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN sso.tex](../../consciousness/sections/sso.tex):71 | F01; raw block below | Delta v,v_f,v_s | rate parameters; scalar-like, units unspecified | CON-EQ-074; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
\Delta v = v_f - v_s
\end{equation}
```

### CON-EQ-002

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN sso.tex](../../consciousness/sections/sso.tex):85 | F02; raw block below | Delta v | nonzero condition | CON-EQ-075; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
\Delta v \neq 0
\end{equation}
```

### CON-EQ-003

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN sso.tex](../../consciousness/sections/sso.tex):152 | F03; raw block below | tau,Delta v,mu | ratio/proportionality; constants unspecified | CON-EQ-076; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 3 |

```tex
\begin{equation}
\tau \propto \frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-004

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN torque_converter_attention.tex](../../consciousness/sections/torque_converter_attention.tex):60 | F01; raw block below | Delta v,v_f,v_s | rate parameters; scalar-like, units unspecified | CON-EQ-077; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
\Delta v = v_f - v_s
\end{equation}
```

### CON-EQ-005

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN torque_converter_attention.tex](../../consciousness/sections/torque_converter_attention.tex):77 | F04; raw block below | T,kappa,Delta v,mu | effective index / parameter ratio | CON-EQ-078; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
\mathcal{T} = \kappa \frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-006

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN torque_converter_attention.tex](../../consciousness/sections/torque_converter_attention.tex):125 | F03; raw block below | tau,Delta v,mu | ratio/proportionality; constants unspecified | CON-EQ-082; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 3 |

```tex
\begin{equation}
\tau \propto \frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-007

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN torque_converter_attention.tex](../../consciousness/sections/torque_converter_attention.tex):139 | F05; raw block below | lambda,i,ell_i,Phi,nabla | token coupling; index/gradient domains unspecified | CON-EQ-083; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | CT token coupling; §14 | CT-REUSED; source-local occurrence 4 |

```tex
\[
\lambda \sum_i \ell_i \cdot \nabla\Phi
\]
```

### CON-EQ-008

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN torque_converter_attention.tex](../../consciousness/sections/torque_converter_attention.tex):202 | F06; raw block below | T_Phi,kappa,Delta v,mu,Phi,nabla | effective index; gradient norm convention unspecified | CON-EQ-084; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 5 |

```tex
\begin{equation}
\mathcal{T}_{\Phi} \sim \kappa \frac{\Delta v}{\mu} |\nabla \Phi|
\end{equation}
```

### CON-EQ-009

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN formal_mapping.tex](../../consciousness/sections/formal_mapping.tex):189 | F07; raw block below | I,t,J_I,sigma,nabla | window-local continuum template; spatial domain unspecified | CON-EQ-085; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 1 |

```tex
\begin{equation}
\frac{\partial I}{\partial t} + \nabla \cdot J_I = \sigma
\end{equation}
```

### CON-EQ-010

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN formal_mapping.tex](../../consciousness/sections/formal_mapping.tex):193 | F08; raw block below | J_I,D,I,mu_I,F,nabla | flow template; carrier/dimension unspecified | CON-EQ-086; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 2 |

```tex
\begin{equation}
J_I = -D \nabla I + \mu_I F
\end{equation}
```

### CON-EQ-011

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN formal_mapping.tex](../../consciousness/sections/formal_mapping.tex):197 | F09; raw block below | F,Phi,nabla | gradient template; coordinate domain unspecified | CON-EQ-087; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 3 |

```tex
\begin{equation}
F = -\nabla \Phi
\end{equation}
```

### CON-EQ-012

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN formal_mapping.tex](../../consciousness/sections/formal_mapping.tex):201 | F10; raw block below | Phi,K,I,* | kernel/convolution template; kernel signature unspecified | CON-EQ-088; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 4 |

```tex
\begin{equation}
\Phi = K * I
\end{equation}
```

### CON-EQ-013

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN formal_mapping.tex](../../consciousness/sections/formal_mapping.tex):228 | F11; raw block below | Delta v | limit toward synchrony | CON-EQ-089; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 5 |

```tex
\begin{equation}
\Delta v \rightarrow 0
\end{equation}
```

### CON-EQ-014

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN formal_mapping.tex](../../consciousness/sections/formal_mapping.tex):242 | F02; raw block below | Delta v | nonzero condition | CON-EQ-090; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 6 |

```tex
\begin{equation}
\Delta v \neq 0
\end{equation}
```

### CON-EQ-015

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN formal_mapping.tex](../../consciousness/sections/formal_mapping.tex):261 | F12; raw block below | C_ij,lambda,rho_i,H_ij,i,j | node-pair relation; node set unspecified | CON-EQ-091; EXACT | Vol.1 causal_logs_time eq:Cij | VED-REUSED; source-local occurrence 7 |

```tex
\begin{equation}
C_{ij} = 1 - \exp\!\left(-\lambda \rho_i H_{ij}\right)
\end{equation}
```

### CON-EQ-016

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN formal_mapping.tex](../../consciousness/sections/formal_mapping.tex):281 | F13; raw block below | Delta C,C_s,C_f | effective layer closure difference | CON-EQ-092; EXACT | VED closure difference comparison; §12 | CONSCIOUSNESS-LOCAL; source-local occurrence 8 |

```tex
\begin{equation}
\Delta C = C_s - C_f
\end{equation}
```

### CON-EQ-017

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN formal_mapping.tex](../../consciousness/sections/formal_mapping.tex):287 | F14; raw block below | Delta v,Delta C | correspondence; no coordinate transformation function | CON-EQ-093; EXACT | VED closure difference comparison; §12 | SCHEMATIC; source-local occurrence 9 |

```tex
\begin{equation}
\Delta v \;\leftrightarrow\; \Delta C
\end{equation}
```

### CON-EQ-018

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN formal_mapping.tex](../../consciousness/sections/formal_mapping.tex):295 | F15; raw block below | Delta C,Delta C_max | bounded difference interval | CON-EQ-094; EXACT | VED closure difference comparison; §12 | CONSCIOUSNESS-LOCAL; source-local occurrence 10 |

```tex
\begin{equation}
0 < \Delta C < \Delta C_{\max}
\end{equation}
```

### CON-EQ-019

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN formal_mapping.tex](../../consciousness/sections/formal_mapping.tex):307 | F16; raw block below | C,t,J_C,a,Delta,C_*,Gamma,kappa_B,C_max,nabla | older field PDE; spatial domain unspecified | CON-EQ-095; EXACT | IFGT unified_equation eq:unified / eq:unified_external; §13 | HISTORICAL / OLDER-VERSION; source-local occurrence 11 |

```tex
\begin{equation}
\frac{\partial C}{\partial t} + \nabla \cdot J_C = a\Delta\!\left(1 - C/C_*\right) - \Gamma C - \frac{\kappa_B}{C_{\max} - C}
\end{equation}
```

### CON-EQ-020

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN formal_mapping.tex](../../consciousness/sections/formal_mapping.tex):374 | F04; raw block below | T,kappa,Delta v,mu | effective index / parameter ratio | CON-EQ-096; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 12 |

```tex
\begin{equation}
\mathcal{T} = \kappa \frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-021

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN formal_mapping.tex](../../consciousness/sections/formal_mapping.tex):384 | F06; raw block below | T_Phi,kappa,Delta v,mu,Phi,nabla | effective index; gradient norm convention unspecified | CON-EQ-097; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 13 |

```tex
\begin{equation}
\mathcal{T}_{\Phi} \sim \kappa \frac{\Delta v}{\mu} |\nabla \Phi|
\end{equation}
```

### CON-EQ-022

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN formal_mapping.tex](../../consciousness/sections/formal_mapping.tex):409 | F17; raw block below | I,J_log,Phi,Delta v,mu,tau,T_Phi; Log Referencing | schematic argument list; codomain unspecified | CON-EQ-098; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | SCHEMATIC; source-local occurrence 14 |

```tex
\begin{equation}
\text{Consciousness} \sim \text{Log Referencing}\!\left(I, J_{\log}, \Phi, \Delta v, \mu, \tau, \mathcal{T}_{\Phi}\right)
\end{equation}
```

### CON-EQ-023

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN core_equations.tex](../../consciousness/sections/core_equations.tex):17 | F01; raw block below | Delta v,v_f,v_s | rate parameters; scalar-like, units unspecified | CON-EQ-099; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
\Delta v = v_f - v_s
\end{equation}
```

### CON-EQ-024

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN core_equations.tex](../../consciousness/sections/core_equations.tex):33 | F02; raw block below | Delta v | nonzero condition | CON-EQ-100; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
\Delta v \neq 0
\end{equation}
```

### CON-EQ-025

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN core_equations.tex](../../consciousness/sections/core_equations.tex):50 | F18; raw block below | mu | positive parameter | CON-EQ-102; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 3 |

```tex
\begin{equation}
\mu > 0
\end{equation}
```

### CON-EQ-026

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN core_equations.tex](../../consciousness/sections/core_equations.tex):67 | F03; raw block below | tau,Delta v,mu | ratio/proportionality; constants unspecified | CON-EQ-103; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 4 |

```tex
\begin{equation}
\tau \propto \frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-027

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN core_equations.tex](../../consciousness/sections/core_equations.tex):83 | F19; raw block below | tau,tau_min,tau_max | open interval; numerical bounds unspecified | CON-EQ-104; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 5 |

```tex
\begin{equation}
\tau_{\min} < \tau < \tau_{\max}
\end{equation}
```

### CON-EQ-028

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN core_equations.tex](../../consciousness/sections/core_equations.tex):96 | F04; raw block below | T,kappa,Delta v,mu | effective index / parameter ratio | CON-EQ-105; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 6 |

```tex
\begin{equation}
\mathcal{T} = \kappa \frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-029

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN core_equations.tex](../../consciousness/sections/core_equations.tex):125 | F07; raw block below | I,t,J_I,sigma,nabla | window-local continuum template; spatial domain unspecified | CON-EQ-106; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 7 |

```tex
\begin{equation}
\frac{\partial I}{\partial t} + \nabla \cdot J_I = \sigma
\end{equation}
```

### CON-EQ-030

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN core_equations.tex](../../consciousness/sections/core_equations.tex):129 | F08; raw block below | J_I,D,I,mu_I,F,nabla | flow template; carrier/dimension unspecified | CON-EQ-107; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 8 |

```tex
\begin{equation}
J_I = -D \nabla I + \mu_I F
\end{equation}
```

### CON-EQ-031

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN core_equations.tex](../../consciousness/sections/core_equations.tex):133 | F09; raw block below | F,Phi,nabla | gradient template; coordinate domain unspecified | CON-EQ-108; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 9 |

```tex
\begin{equation}
F = -\nabla \Phi
\end{equation}
```

### CON-EQ-032

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN core_equations.tex](../../consciousness/sections/core_equations.tex):137 | F10; raw block below | Phi,K,I,* | kernel/convolution template; kernel signature unspecified | CON-EQ-109; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 10 |

```tex
\begin{equation}
\Phi = K * I
\end{equation}
```

### CON-EQ-033

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN core_equations.tex](../../consciousness/sections/core_equations.tex):149 | F20; raw block below | T_Phi,kappa,Delta v,mu,Phi,nabla | effective index; explicit left/right norm delimiters | CON-EQ-110; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 11 |

```tex
\begin{equation}
\mathcal{T}_{\Phi} \sim \kappa \frac{\Delta v}{\mu} \left|\nabla \Phi\right|
\end{equation}
```

### CON-EQ-034

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN core_equations.tex](../../consciousness/sections/core_equations.tex):166 | F21; raw block below | Delta v,Delta v_max | absolute-gap interval | CON-EQ-111; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 12 |

```tex
\begin{equation}
0 < |\Delta v| < \Delta v_{\max}
\end{equation}
```

### CON-EQ-035

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN core_equations.tex](../../consciousness/sections/core_equations.tex):170 | F22; raw block below | mu,mu_min,mu_max | open parameter interval | CON-EQ-112; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 13 |

```tex
\begin{equation}
\mu_{\min} < \mu < \mu_{\max}
\end{equation}
```

### CON-EQ-036

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN core_equations.tex](../../consciousness/sections/core_equations.tex):174 | F19; raw block below | tau,tau_min,tau_max | open interval; numerical bounds unspecified | CON-EQ-113; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 14 |

```tex
\begin{equation}
\tau_{\min} < \tau < \tau_{\max}
\end{equation}
```

### CON-EQ-037

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN core_equations.tex](../../consciousness/sections/core_equations.tex):178 | F23; raw block below | T_Phi,T_min,T_max | index interval; no T_Phi_min symbol defined | CON-EQ-114; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 15 |

```tex
\begin{equation}
\mathcal{T}_{\min} < \mathcal{T}_{\Phi} < \mathcal{T}_{\max}
\end{equation}
```

### CON-EQ-038

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN core_equations.tex](../../consciousness/sections/core_equations.tex):228 | F24; raw block below | Delta v,Phi,I,t,nabla | three nonzero conditions | CON-EQ-115; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 16 |

```tex
\begin{equation}
\Delta v \neq 0, \qquad \nabla \Phi \neq 0, \qquad \frac{\partial I}{\partial t} \neq 0
\end{equation}
```

### CON-EQ-039

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN core_equations.tex](../../consciousness/sections/core_equations.tex):249 | F25; raw block below | Delta v,mu,tau,T_Phi,nabla Phi; Log Referencing | schematic argument list | CON-EQ-116; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | SCHEMATIC; source-local occurrence 17 |

```tex
\begin{equation}
\text{Consciousness} \;\sim\; \text{Log Referencing}\!\left(\Delta v, \mu, \tau, \mathcal{T}_{\Phi}, \nabla \Phi\right)
\end{equation}
```

### CON-EQ-040

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN structural_interpretation.tex](../../consciousness/sections/structural_interpretation.tex):115 | F26; raw block below | Phi,nabla; referencing bias | qualitative increase correspondence | CON-EQ-122; EXACT | not assigned from shared wording | SCHEMATIC; source-local occurrence 1 |

```tex
\begin{equation}
|\nabla \Phi| \uparrow \quad \Rightarrow \quad \text{referencing bias} \uparrow
\end{equation}
```

### CON-EQ-041

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN structural_interpretation.tex](../../consciousness/sections/structural_interpretation.tex):133 | F06; raw block below | T_Phi,kappa,Delta v,mu,Phi,nabla | effective index; gradient norm convention unspecified | CON-EQ-123; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
\mathcal{T}_{\Phi} \sim \kappa \frac{\Delta v}{\mu} |\nabla \Phi|
\end{equation}
```

### CON-EQ-042

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN dynamics_log_referencing.tex](../../consciousness/sections/dynamics_log_referencing.tex):90 | F03; raw block below | tau,Delta v,mu | ratio/proportionality; constants unspecified | CON-EQ-124; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
\tau \propto \frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-043

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN dynamics_log_referencing.tex](../../consciousness/sections/dynamics_log_referencing.tex):113 | F09; raw block below | F,Phi,nabla | gradient template; coordinate domain unspecified | CON-EQ-125; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 2 |

```tex
\begin{equation}
F = -\nabla \Phi
\end{equation}
```

### CON-EQ-044

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN dynamics_log_referencing.tex](../../consciousness/sections/dynamics_log_referencing.tex):142 | F06; raw block below | T_Phi,kappa,Delta v,mu,Phi,nabla | effective index; gradient norm convention unspecified | CON-EQ-126; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 3 |

```tex
\begin{equation}
\mathcal{T}_{\Phi} \sim \kappa \frac{\Delta v}{\mu} |\nabla \Phi|
\end{equation}
```

### CON-EQ-045

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN dynamics_log_referencing.tex](../../consciousness/sections/dynamics_log_referencing.tex):156 | F23; raw block below | T_Phi,T_min,T_max | index interval; no T_Phi_min symbol defined | CON-EQ-127; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 4 |

```tex
\begin{equation}
\mathcal{T}_{\min} < \mathcal{T}_{\Phi} < \mathcal{T}_{\max}
\end{equation}
```

### CON-EQ-046

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN experimental_reinterpretation.tex](../../consciousness/sections/experimental_reinterpretation.tex):45 | F01; raw block below | Delta v,v_f,v_s | rate parameters; scalar-like, units unspecified | CON-EQ-128; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
\Delta v = v_f - v_s
\end{equation}
```

### CON-EQ-047

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN experimental_reinterpretation.tex](../../consciousness/sections/experimental_reinterpretation.tex):51 | F03; raw block below | tau,Delta v,mu | ratio/proportionality; constants unspecified | CON-EQ-129; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
\tau \propto \frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-048

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN experimental_reinterpretation.tex](../../consciousness/sections/experimental_reinterpretation.tex):186 | F27; raw block below | fast preparation; delayed sedimentation; reportable timestamp | schematic temporal sequence | CON-EQ-130; EXACT | not assigned from shared wording | SCHEMATIC; source-local occurrence 3 |

```tex
\begin{equation}
\text{fast preparation} \rightarrow \text{delayed sedimentation} \rightarrow \text{reportable timestamp}
\end{equation}
```

### CON-EQ-049

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN experimental_reinterpretation.tex](../../consciousness/sections/experimental_reinterpretation.tex):192 | F28; raw block below | localized processing; blocked transmission; asymmetric reportability | schematic pathway sequence | CON-EQ-131; EXACT | not assigned from shared wording | SCHEMATIC; source-local occurrence 4 |

```tex
\begin{equation}
\text{localized processing} \rightarrow \text{blocked transmission} \rightarrow \text{asymmetric reportability}
\end{equation}
```

### CON-EQ-050

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN qualia_boundary.tex](../../consciousness/sections/qualia_boundary.tex):133 | F06; raw block below | T_Phi,kappa,Delta v,mu,Phi,nabla | effective index; gradient norm convention unspecified | CON-EQ-132; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
\mathcal{T}_{\Phi} \sim \kappa \frac{\Delta v}{\mu} |\nabla \Phi|
\end{equation}
```

### CON-EQ-051

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN qualia_boundary.tex](../../consciousness/sections/qualia_boundary.tex):164 | F29; raw block below | qualia live; measurement; sedimented residue | schematic transformation | CON-EQ-133; EXACT | not assigned from shared wording | SCHEMATIC; source-local occurrence 2 |

```tex
\begin{equation}
\text{qualia live} \rightarrow \text{measurement} \rightarrow \text{sedimented residue}
\end{equation}
```

### CON-EQ-052

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN opening_model.tex](../../consciousness/sections/opening_model.tex):79 | F06; raw block below | T_Phi,kappa,Delta v,mu,Phi,nabla | effective index; gradient norm convention unspecified | CON-EQ-134; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
\mathcal{T}_{\Phi} \sim \kappa \frac{\Delta v}{\mu} |\nabla \Phi|
\end{equation}
```

### CON-EQ-053

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN measurement_collapse.tex](../../consciousness/sections/measurement_collapse.tex):57 | F29; raw block below | qualia live; measurement; sedimented residue | schematic transformation | CON-EQ-135; EXACT | not assigned from shared wording | SCHEMATIC; source-local occurrence 1 |

```tex
\begin{equation}
\text{qualia live} \rightarrow \text{measurement} \rightarrow \text{sedimented residue}
\end{equation}
```

### CON-EQ-054

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN measurement_collapse.tex](../../consciousness/sections/measurement_collapse.tex):105 | F30; raw block below | Delta v,Delta v_max,mu,mu_min,mu_max,tau,tau_min,tau_max,T_min,T_Phi,T_max | four inequalities in one display | CON-EQ-136, CON-EQ-137, CON-EQ-138, CON-EQ-139; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
0 < |\Delta v| < \Delta v_{\max}, \quad \mu_{\min} < \mu < \mu_{\max}, \quad \tau_{\min} < \tau < \tau_{\max}, \quad \mathcal{T}_{\min} < \mathcal{T}_{\Phi} < \mathcal{T}_{\max}
\end{equation}
```

### CON-EQ-055

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN non_localization.tex](../../consciousness/sections/non_localization.tex):98 | F30; raw block below | Delta v,Delta v_max,mu,mu_min,mu_max,tau,tau_min,tau_max,T_min,T_Phi,T_max | four inequalities in one display | CON-EQ-141, CON-EQ-142, CON-EQ-143, CON-EQ-144; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
0 < |\Delta v| < \Delta v_{\max}, \quad \mu_{\min} < \mu < \mu_{\max}, \quad \tau_{\min} < \tau < \tau_{\max}, \quad \mathcal{T}_{\min} < \mathcal{T}_{\Phi} < \mathcal{T}_{\max}
\end{equation}
```

### CON-EQ-056

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN qualitative_predictions.tex](../../consciousness/sections/qualitative_predictions.tex):10 | F20; raw block below | T_Phi,kappa,Delta v,mu,Phi,nabla | effective index; explicit left/right norm delimiters | CON-EQ-145; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
\mathcal{T}_{\Phi} \sim \kappa \frac{\Delta v}{\mu} \left|\nabla \Phi\right|
\end{equation}
```

### CON-EQ-057

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN qualitative_predictions.tex](../../consciousness/sections/qualitative_predictions.tex):21 | F11; raw block below | Delta v | limit toward synchrony | CON-EQ-146; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
\Delta v \rightarrow 0
\end{equation}
```

### CON-EQ-058

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN qualitative_predictions.tex](../../consciousness/sections/qualitative_predictions.tex):36 | F31; raw block below | Delta v | qualitative large-gap condition; numerical scale unspecified | CON-EQ-147; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 3 |

```tex
\begin{equation}
|\Delta v| \gg 0
\end{equation}
```

### CON-EQ-059

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN qualitative_predictions.tex](../../consciousness/sections/qualitative_predictions.tex):51 | F32; raw block below | mu | limit toward zero | CON-EQ-148; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 4 |

```tex
\begin{equation}
\mu \rightarrow 0
\end{equation}
```

### CON-EQ-060

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN qualitative_predictions.tex](../../consciousness/sections/qualitative_predictions.tex):59 | F33; raw block below | mu | limit toward infinity | CON-EQ-149; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 5 |

```tex
\begin{equation}
\mu \rightarrow \infty
\end{equation}
```

### CON-EQ-061

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN qualitative_predictions.tex](../../consciousness/sections/qualitative_predictions.tex):67 | F22; raw block below | mu,mu_min,mu_max | open parameter interval | CON-EQ-150; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 6 |

```tex
\begin{equation}
\mu_{\min} < \mu < \mu_{\max}
\end{equation}
```

### CON-EQ-062

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN qualitative_predictions.tex](../../consciousness/sections/qualitative_predictions.tex):78 | F03; raw block below | tau,Delta v,mu | ratio/proportionality; constants unspecified | CON-EQ-151; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 7 |

```tex
\begin{equation}
\tau \propto \frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-063

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN qualitative_predictions.tex](../../consciousness/sections/qualitative_predictions.tex):88 | F19; raw block below | tau,tau_min,tau_max | open interval; numerical bounds unspecified | CON-EQ-154; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 8 |

```tex
\begin{equation}
\tau_{\min} < \tau < \tau_{\max}
\end{equation}
```

### CON-EQ-064

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN qualitative_predictions.tex](../../consciousness/sections/qualitative_predictions.tex):99 | F26; raw block below | Phi,nabla; referencing bias | qualitative increase correspondence | CON-EQ-155; EXACT | not assigned from shared wording | SCHEMATIC; source-local occurrence 9 |

```tex
\begin{equation}
|\nabla \Phi| \uparrow \quad \Rightarrow \quad \text{referencing bias} \uparrow
\end{equation}
```

### CON-EQ-065

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN qualitative_predictions.tex](../../consciousness/sections/qualitative_predictions.tex):118 | F34; raw block below | measurement; boundary closure; sedimented residue | schematic implication chain | CON-EQ-156; EXACT | not assigned from shared wording | SCHEMATIC; source-local occurrence 10 |

```tex
\begin{equation}
\text{measurement} \quad \Rightarrow \quad \text{boundary closure} \quad \Rightarrow \quad \text{sedimented residue}
\end{equation}
```

### CON-EQ-066

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN qualitative_predictions.tex](../../consciousness/sections/qualitative_predictions.tex):170 | F30; raw block below | Delta v,Delta v_max,mu,mu_min,mu_max,tau,tau_min,tau_max,T_min,T_Phi,T_max | four inequalities in one display | CON-EQ-157, CON-EQ-158, CON-EQ-159, CON-EQ-160; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 11 |

```tex
\begin{equation}
0 < |\Delta v| < \Delta v_{\max}, \quad \mu_{\min} < \mu < \mu_{\max}, \quad \tau_{\min} < \tau < \tau_{\max}, \quad \mathcal{T}_{\min} < \mathcal{T}_{\Phi} < \mathcal{T}_{\max}
\end{equation}
```

### CON-EQ-067

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN qualitative_predictions.tex](../../consciousness/sections/qualitative_predictions.tex):225 | F35; raw block below | Delta v,mu,tau,T_Phi,nabla Phi; consciousness window | tuple membership; set not separately typed | CON-EQ-161; EXACT | not assigned from shared wording | SCHEMATIC; source-local occurrence 12 |

```tex
\begin{equation}
\text{stable consciousness} \quad \Leftrightarrow \quad (\Delta v, \mu, \tau, \mathcal{T}_{\Phi}, \nabla\Phi) \in \text{consciousness window}
\end{equation}
```

### CON-EQ-068

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN relation_to_note.tex](../../consciousness/sections/relation_to_note.tex):92 | F36; raw block below | Delta v,mu,tau,T_Phi,nabla Phi; Log Referencing | schematic argument list | CON-EQ-173; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | SCHEMATIC; source-local occurrence 1 |

```tex
\begin{equation}
\text{Consciousness} \sim \text{Log Referencing}\!\left(\Delta v, \mu, \tau, \mathcal{T}_{\Phi}, \nabla\Phi\right)
\end{equation}
```

### CON-EQ-069

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN conclusion.tex](../../consciousness/sections/conclusion.tex):86 | F36; raw block below | Delta v,mu,tau,T_Phi,nabla Phi; Log Referencing | schematic argument list | CON-EQ-174; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | SCHEMATIC; source-local occurrence 1 |

```tex
\begin{equation}
\text{Consciousness} \sim \text{Log Referencing}\!\left(\Delta v, \mu, \tau, \mathcal{T}_{\Phi}, \nabla\Phi\right)
\end{equation}
```

### CON-EQ-070

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN conclusion.tex](../../consciousness/sections/conclusion.tex):96 | F21; raw block below | Delta v,Delta v_max | absolute-gap interval | CON-EQ-175; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
0 < |\Delta v| < \Delta v_{\max}
\end{equation}
```

### CON-EQ-071

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN conclusion.tex](../../consciousness/sections/conclusion.tex):100 | F22; raw block below | mu,mu_min,mu_max | open parameter interval | CON-EQ-176; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 3 |

```tex
\begin{equation}
\mu_{\min} < \mu < \mu_{\max}
\end{equation}
```

### CON-EQ-072

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN conclusion.tex](../../consciousness/sections/conclusion.tex):104 | F19; raw block below | tau,tau_min,tau_max | open interval; numerical bounds unspecified | CON-EQ-177; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 4 |

```tex
\begin{equation}
\tau_{\min} < \tau < \tau_{\max}
\end{equation}
```

### CON-EQ-073

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [EN conclusion.tex](../../consciousness/sections/conclusion.tex):108 | F23; raw block below | T_Phi,T_min,T_max | index interval; no T_Phi_min symbol defined | CON-EQ-178; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 5 |

```tex
\begin{equation}
\mathcal{T}_{\min} < \mathcal{T}_{\Phi} < \mathcal{T}_{\max}
\end{equation}
```

### CON-EQ-074

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA sso_ja.tex](../../consciousness/sections_ja/sso_ja.tex):68 | F01; raw block below | Delta v,v_f,v_s | rate parameters; scalar-like, units unspecified | CON-EQ-001; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
\Delta v = v_f - v_s
\end{equation}
```

### CON-EQ-075

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA sso_ja.tex](../../consciousness/sections_ja/sso_ja.tex):82 | F02; raw block below | Delta v | nonzero condition | CON-EQ-002; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
\Delta v \neq 0
\end{equation}
```

### CON-EQ-076

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA sso_ja.tex](../../consciousness/sections_ja/sso_ja.tex):146 | F03; raw block below | tau,Delta v,mu | ratio/proportionality; constants unspecified | CON-EQ-003; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 3 |

```tex
\begin{equation}
\tau \propto \frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-077

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA torque_converter_attention_ja.tex](../../consciousness/sections_ja/torque_converter_attention_ja.tex):60 | F01; raw block below | Delta v,v_f,v_s | rate parameters; scalar-like, units unspecified | CON-EQ-004; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
\Delta v = v_f - v_s
\end{equation}
```

### CON-EQ-078

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA torque_converter_attention_ja.tex](../../consciousness/sections_ja/torque_converter_attention_ja.tex):76 | F04; raw block below | T,kappa,Delta v,mu | effective index / parameter ratio | CON-EQ-005; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
\mathcal{T}
=
\kappa
\frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-079

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA torque_converter_attention_ja.tex](../../consciousness/sections_ja/torque_converter_attention_ja.tex):116 | F37; raw block below | A_i,m_i,T_i,i | JA local attention/log-index relation | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 3 |

```tex
\begin{equation}
A_i \propto m_i \cdot \mathcal{T}_i
\end{equation}
```

### CON-EQ-080

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA torque_converter_attention_ja.tex](../../consciousness/sections_ja/torque_converter_attention_ja.tex):122 | F38; raw block below | T_i,Delta v_i,i | JA local proportionality | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 4 |

```tex
\begin{equation}
\mathcal{T}_i \propto \Delta v_i
\end{equation}
```

### CON-EQ-081

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA torque_converter_attention_ja.tex](../../consciousness/sections_ja/torque_converter_attention_ja.tex):128 | F39; raw block below | A_i,m_i,Delta v_i,i | JA minimal approximation | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 5 |

```tex
\begin{equation}
A_i \propto m_i \cdot \Delta v_i
\end{equation}
```

### CON-EQ-082

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA torque_converter_attention_ja.tex](../../consciousness/sections_ja/torque_converter_attention_ja.tex):148 | F03; raw block below | tau,Delta v,mu | ratio/proportionality; constants unspecified | CON-EQ-006; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 6 |

```tex
\begin{equation}
\tau \propto \frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-083

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA torque_converter_attention_ja.tex](../../consciousness/sections_ja/torque_converter_attention_ja.tex):162 | F40; raw block below | lambda,i,ell_{i},Phi,nabla | CT token coupling; subscript-brace variant | CON-EQ-007; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | CT token coupling; §14 | CT-REUSED; source-local occurrence 7 |

```tex
\[
\lambda \sum_i \ell_{i} \cdot \nabla\Phi
\]
```

### CON-EQ-084

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA torque_converter_attention_ja.tex](../../consciousness/sections_ja/torque_converter_attention_ja.tex):222 | F06; raw block below | T_Phi,kappa,Delta v,mu,Phi,nabla | effective index; gradient norm convention unspecified | CON-EQ-008; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 8 |

```tex
\begin{equation}
\mathcal{T}_{\Phi}
\sim
\kappa
\frac{\Delta v}{\mu}
|\nabla \Phi|
\end{equation}
```

### CON-EQ-085

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA formal_mapping_ja.tex](../../consciousness/sections_ja/formal_mapping_ja.tex):113 | F07; raw block below | I,t,J_I,sigma,nabla | window-local continuum template; spatial domain unspecified | CON-EQ-009; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 1 |

```tex
\begin{equation}
\frac{\partial I}{\partial t} + \nabla \cdot J_I = \sigma
\end{equation}
```

### CON-EQ-086

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA formal_mapping_ja.tex](../../consciousness/sections_ja/formal_mapping_ja.tex):117 | F08; raw block below | J_I,D,I,mu_I,F,nabla | flow template; carrier/dimension unspecified | CON-EQ-010; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 2 |

```tex
\begin{equation}
J_I = -D \nabla I + \mu_I F
\end{equation}
```

### CON-EQ-087

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA formal_mapping_ja.tex](../../consciousness/sections_ja/formal_mapping_ja.tex):121 | F09; raw block below | F,Phi,nabla | gradient template; coordinate domain unspecified | CON-EQ-011; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 3 |

```tex
\begin{equation}
F = -\nabla \Phi
\end{equation}
```

### CON-EQ-088

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA formal_mapping_ja.tex](../../consciousness/sections_ja/formal_mapping_ja.tex):125 | F10; raw block below | Phi,K,I,* | kernel/convolution template; kernel signature unspecified | CON-EQ-012; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 4 |

```tex
\begin{equation}
\Phi = K * I
\end{equation}
```

### CON-EQ-089

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA formal_mapping_ja.tex](../../consciousness/sections_ja/formal_mapping_ja.tex):155 | F11; raw block below | Delta v | limit toward synchrony | CON-EQ-013; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 5 |

```tex
\begin{equation}
\Delta v \rightarrow 0
\end{equation}
```

### CON-EQ-090

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA formal_mapping_ja.tex](../../consciousness/sections_ja/formal_mapping_ja.tex):171 | F02; raw block below | Delta v | nonzero condition | CON-EQ-014; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 6 |

```tex
\begin{equation}
\Delta v \neq 0
\end{equation}
```

### CON-EQ-091

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA formal_mapping_ja.tex](../../consciousness/sections_ja/formal_mapping_ja.tex):188 | F12; raw block below | C_ij,lambda,rho_i,H_ij,i,j | node-pair relation; node set unspecified | CON-EQ-015; EXACT | Vol.1 causal_logs_time eq:Cij | VED-REUSED; source-local occurrence 7 |

```tex
\begin{equation}
C_{ij} = 1 - \exp\!\left(-\lambda \rho_i H_{ij}\right)
\end{equation}
```

### CON-EQ-092

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA formal_mapping_ja.tex](../../consciousness/sections_ja/formal_mapping_ja.tex):208 | F13; raw block below | Delta C,C_s,C_f | effective layer closure difference | CON-EQ-016; EXACT | VED closure difference comparison; §12 | CONSCIOUSNESS-LOCAL; source-local occurrence 8 |

```tex
\begin{equation}
\Delta C = C_s - C_f
\end{equation}
```

### CON-EQ-093

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA formal_mapping_ja.tex](../../consciousness/sections_ja/formal_mapping_ja.tex):214 | F14; raw block below | Delta v,Delta C | correspondence; no coordinate transformation function | CON-EQ-017; EXACT | VED closure difference comparison; §12 | SCHEMATIC; source-local occurrence 9 |

```tex
\begin{equation}
\Delta v \;\leftrightarrow\; \Delta C
\end{equation}
```

### CON-EQ-094

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA formal_mapping_ja.tex](../../consciousness/sections_ja/formal_mapping_ja.tex):222 | F15; raw block below | Delta C,Delta C_max | bounded difference interval | CON-EQ-018; EXACT | VED closure difference comparison; §12 | CONSCIOUSNESS-LOCAL; source-local occurrence 10 |

```tex
\begin{equation}
0 < \Delta C < \Delta C_{\max}
\end{equation}
```

### CON-EQ-095

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA formal_mapping_ja.tex](../../consciousness/sections_ja/formal_mapping_ja.tex):247 | F16; raw block below | C,t,J_C,a,Delta,C_*,Gamma,kappa_B,C_max,nabla | older field PDE; spatial domain unspecified | CON-EQ-019; EXACT | IFGT unified_equation eq:unified / eq:unified_external; §13 | HISTORICAL / OLDER-VERSION; source-local occurrence 11 |

```tex
\begin{equation}
\frac{\partial C}{\partial t} + \nabla \cdot J_C = a\Delta\!\left(1 - C/C_*\right) - \Gamma C - \frac{\kappa_B}{C_{\max} - C}
\end{equation}
```

### CON-EQ-096

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA formal_mapping_ja.tex](../../consciousness/sections_ja/formal_mapping_ja.tex):299 | F04; raw block below | T,kappa,Delta v,mu | effective index / parameter ratio | CON-EQ-020; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 12 |

```tex
\begin{equation}
\mathcal{T} =
\kappa
\frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-097

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA formal_mapping_ja.tex](../../consciousness/sections_ja/formal_mapping_ja.tex):311 | F06; raw block below | T_Phi,kappa,Delta v,mu,Phi,nabla | effective index; gradient norm convention unspecified | CON-EQ-021; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 13 |

```tex
\begin{equation}
\mathcal{T}_{\Phi}
\sim
\kappa
\frac{\Delta v}{\mu}
|\nabla \Phi|
\end{equation}
```

### CON-EQ-098

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA formal_mapping_ja.tex](../../consciousness/sections_ja/formal_mapping_ja.tex):339 | F41; raw block below | I,J_log,Phi,Delta v,mu,tau,T_Phi; Log Referencing | schematic argument list; spacing variant | CON-EQ-022; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | SCHEMATIC; source-local occurrence 14 |

```tex
\begin{equation}
\text{Consciousness}
\sim
\text{Log Referencing}
\left(
I,
J_{\log},
\Phi,
\Delta v,
\mu,
\tau,
\mathcal{T}_{\Phi}
\right)
\end{equation}
```

### CON-EQ-099

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):16 | F01; raw block below | Delta v,v_f,v_s | rate parameters; scalar-like, units unspecified | CON-EQ-023; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
\Delta v = v_f - v_s
\end{equation}
```

### CON-EQ-100

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):30 | F02; raw block below | Delta v | nonzero condition | CON-EQ-024; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
\Delta v \neq 0
\end{equation}
```

### CON-EQ-101

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):44 | F42; raw block below | C(t),cal F,Delta v,rho_s,tau,t | JA consciousness-opening function; codomain unspecified | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 3 |

```tex
\begin{equation}
C(t) \propto \mathcal{F}(\Delta v, \rho_s, \tau)
\end{equation}
```

### CON-EQ-102

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):62 | F18; raw block below | mu | positive parameter | CON-EQ-025; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 4 |

```tex
\begin{equation}
\mu > 0
\end{equation}
```

### CON-EQ-103

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):78 | F03; raw block below | tau,Delta v,mu | ratio/proportionality; constants unspecified | CON-EQ-026; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 5 |

```tex
\begin{equation}
\tau \propto \frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-104

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):94 | F19; raw block below | tau,tau_min,tau_max | open interval; numerical bounds unspecified | CON-EQ-027; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 6 |

```tex
\begin{equation}
\tau_{\min} < \tau < \tau_{\max}
\end{equation}
```

### CON-EQ-105

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):106 | F04; raw block below | T,kappa,Delta v,mu | effective index / parameter ratio | CON-EQ-028; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 7 |

```tex
\begin{equation}
\mathcal{T} = \kappa \frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-106

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):135 | F07; raw block below | I,t,J_I,sigma,nabla | window-local continuum template; spatial domain unspecified | CON-EQ-029; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 8 |

```tex
\begin{equation}
\frac{\partial I}{\partial t} + \nabla \cdot J_I = \sigma
\end{equation}
```

### CON-EQ-107

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):139 | F08; raw block below | J_I,D,I,mu_I,F,nabla | flow template; carrier/dimension unspecified | CON-EQ-030; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 9 |

```tex
\begin{equation}
J_I = -D \nabla I + \mu_I F
\end{equation}
```

### CON-EQ-108

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):143 | F09; raw block below | F,Phi,nabla | gradient template; coordinate domain unspecified | CON-EQ-031; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 10 |

```tex
\begin{equation}
F = -\nabla \Phi
\end{equation}
```

### CON-EQ-109

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):147 | F10; raw block below | Phi,K,I,* | kernel/convolution template; kernel signature unspecified | CON-EQ-032; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 11 |

```tex
\begin{equation}
\Phi = K * I
\end{equation}
```

### CON-EQ-110

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):159 | F20; raw block below | T_Phi,kappa,Delta v,mu,Phi,nabla | effective index; explicit left/right norm delimiters | CON-EQ-033; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 12 |

```tex
\begin{equation}
\mathcal{T}_{\Phi}
\sim
\kappa
\frac{\Delta v}{\mu}
\left|\nabla \Phi\right|
\end{equation}
```

### CON-EQ-111

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):179 | F21; raw block below | Delta v,Delta v_max | absolute-gap interval | CON-EQ-034; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 13 |

```tex
\begin{equation}
0 < |\Delta v| < \Delta v_{\max}
\end{equation}
```

### CON-EQ-112

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):183 | F22; raw block below | mu,mu_min,mu_max | open parameter interval | CON-EQ-035; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 14 |

```tex
\begin{equation}
\mu_{\min} < \mu < \mu_{\max}
\end{equation}
```

### CON-EQ-113

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):187 | F19; raw block below | tau,tau_min,tau_max | open interval; numerical bounds unspecified | CON-EQ-036; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 15 |

```tex
\begin{equation}
\tau_{\min} < \tau < \tau_{\max}
\end{equation}
```

### CON-EQ-114

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):191 | F23; raw block below | T_Phi,T_min,T_max | index interval; no T_Phi_min symbol defined | CON-EQ-037; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 16 |

```tex
\begin{equation}
\mathcal{T}_{\min}
<
\mathcal{T}_{\Phi}
<
\mathcal{T}_{\max}
\end{equation}
```

### CON-EQ-115

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):244 | F24; raw block below | Delta v,Phi,I,t,nabla | three nonzero conditions | CON-EQ-038; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 17 |

```tex
\begin{equation}
\Delta v \neq 0,
\qquad
\nabla \Phi \neq 0,
\qquad
\frac{\partial I}{\partial t} \neq 0
\end{equation}
```

### CON-EQ-116

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex):268 | F43; raw block below | Delta v,mu,tau,T_Phi,nabla Phi; Log Referencing | schematic argument list; spacing variant | CON-EQ-039; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | SCHEMATIC; source-local occurrence 18 |

```tex
\begin{equation}
\text{Consciousness}
\;\sim\;
\text{Log Referencing}
\left(
\Delta v,
\mu,
\tau,
\mathcal{T}_{\Phi},
\nabla \Phi
\right)
\end{equation}
```

### CON-EQ-117

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA structural_interpretation_ja.tex](../../consciousness/sections_ja/structural_interpretation_ja.tex):42 | F21; raw block below | Delta v,Delta v_max | absolute-gap interval | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
0 < |\Delta v| < \Delta v_{\max}
\end{equation}
```

### CON-EQ-118

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA structural_interpretation_ja.tex](../../consciousness/sections_ja/structural_interpretation_ja.tex):46 | F22; raw block below | mu,mu_min,mu_max | open parameter interval | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
\mu_{\min} < \mu < \mu_{\max}
\end{equation}
```

### CON-EQ-119

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA structural_interpretation_ja.tex](../../consciousness/sections_ja/structural_interpretation_ja.tex):50 | F19; raw block below | tau,tau_min,tau_max | open interval; numerical bounds unspecified | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 3 |

```tex
\begin{equation}
\tau_{\min} < \tau < \tau_{\max}
\end{equation}
```

### CON-EQ-120

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA structural_interpretation_ja.tex](../../consciousness/sections_ja/structural_interpretation_ja.tex):54 | F23; raw block below | T_Phi,T_min,T_max | index interval; no T_Phi_min symbol defined | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 4 |

```tex
\begin{equation}
\mathcal{T}_{\min}
<
\mathcal{T}_{\Phi}
<
\mathcal{T}_{\max}
\end{equation}
```

### CON-EQ-121

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA structural_interpretation_ja.tex](../../consciousness/sections_ja/structural_interpretation_ja.tex):138 | F44; raw block below | Consciousness; state; sustained non-closure | text-only equation environment; not numerical | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | SCHEMATIC; source-local occurrence 5 |

```tex
\begin{equation}
\text{Consciousness is not a state, but a sustained non-closure.}
\end{equation}
```

### CON-EQ-122

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA structural_interpretation_ja.tex](../../consciousness/sections_ja/structural_interpretation_ja.tex):150 | F26; raw block below | Phi,nabla; referencing bias | qualitative increase correspondence | CON-EQ-040; EXACT | not assigned from shared wording | SCHEMATIC; source-local occurrence 6 |

```tex
\begin{equation}
|\nabla \Phi| \uparrow
\quad \Rightarrow \quad
\text{referencing bias} \uparrow
\end{equation}
```

### CON-EQ-123

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA structural_interpretation_ja.tex](../../consciousness/sections_ja/structural_interpretation_ja.tex):170 | F06; raw block below | T_Phi,kappa,Delta v,mu,Phi,nabla | effective index; gradient norm convention unspecified | CON-EQ-041; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 7 |

```tex
\begin{equation}
\mathcal{T}_{\Phi}
\sim
\kappa
\frac{\Delta v}{\mu}
|\nabla \Phi|
\end{equation}
```

### CON-EQ-124

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA dynamics_log_referencing_ja.tex](../../consciousness/sections_ja/dynamics_log_referencing_ja.tex):92 | F03; raw block below | tau,Delta v,mu | ratio/proportionality; constants unspecified | CON-EQ-042; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
\tau \propto \frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-125

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA dynamics_log_referencing_ja.tex](../../consciousness/sections_ja/dynamics_log_referencing_ja.tex):118 | F09; raw block below | F,Phi,nabla | gradient template; coordinate domain unspecified | CON-EQ-043; EXACT | IFGT current fundamental dynamics; CT K*I locator also see §14 | IFGT-REUSED; source-local occurrence 2 |

```tex
\begin{equation}
F = -\nabla \Phi
\end{equation}
```

### CON-EQ-126

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA dynamics_log_referencing_ja.tex](../../consciousness/sections_ja/dynamics_log_referencing_ja.tex):152 | F06; raw block below | T_Phi,kappa,Delta v,mu,Phi,nabla | effective index; gradient norm convention unspecified | CON-EQ-044; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 3 |

```tex
\begin{equation}
\mathcal{T}_{\Phi}
\sim
\kappa
\frac{\Delta v}{\mu}
|\nabla \Phi|
\end{equation}
```

### CON-EQ-127

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA dynamics_log_referencing_ja.tex](../../consciousness/sections_ja/dynamics_log_referencing_ja.tex):174 | F23; raw block below | T_Phi,T_min,T_max | index interval; no T_Phi_min symbol defined | CON-EQ-045; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 4 |

```tex
\begin{equation}
\mathcal{T}_{\min}
<
\mathcal{T}_{\Phi}
<
\mathcal{T}_{\max}
\end{equation}
```

### CON-EQ-128

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA experimental_reinterpretation_ja.tex](../../consciousness/sections_ja/experimental_reinterpretation_ja.tex):52 | F01; raw block below | Delta v,v_f,v_s | rate parameters; scalar-like, units unspecified | CON-EQ-046; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
\Delta v = v_f - v_s
\end{equation}
```

### CON-EQ-129

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA experimental_reinterpretation_ja.tex](../../consciousness/sections_ja/experimental_reinterpretation_ja.tex):58 | F03; raw block below | tau,Delta v,mu | ratio/proportionality; constants unspecified | CON-EQ-047; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
\tau \propto \frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-130

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA experimental_reinterpretation_ja.tex](../../consciousness/sections_ja/experimental_reinterpretation_ja.tex):196 | F27; raw block below | fast preparation; delayed sedimentation; reportable timestamp | schematic temporal sequence | CON-EQ-048; EXACT | not assigned from shared wording | SCHEMATIC; source-local occurrence 3 |

```tex
\begin{equation}
\text{fast preparation}
\rightarrow
\text{delayed sedimentation}
\rightarrow
\text{reportable timestamp}
\end{equation}
```

### CON-EQ-131

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA experimental_reinterpretation_ja.tex](../../consciousness/sections_ja/experimental_reinterpretation_ja.tex):206 | F28; raw block below | localized processing; blocked transmission; asymmetric reportability | schematic pathway sequence | CON-EQ-049; EXACT | not assigned from shared wording | SCHEMATIC; source-local occurrence 4 |

```tex
\begin{equation}
\text{localized processing}
\rightarrow
\text{blocked transmission}
\rightarrow
\text{asymmetric reportability}
\end{equation}
```

### CON-EQ-132

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualia_boundary_ja.tex](../../consciousness/sections_ja/qualia_boundary_ja.tex):148 | F06; raw block below | T_Phi,kappa,Delta v,mu,Phi,nabla | effective index; gradient norm convention unspecified | CON-EQ-050; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
\mathcal{T}_{\Phi}
\sim
\kappa
\frac{\Delta v}{\mu}
|\nabla \Phi|
\end{equation}
```

### CON-EQ-133

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualia_boundary_ja.tex](../../consciousness/sections_ja/qualia_boundary_ja.tex):192 | F29; raw block below | qualia live; measurement; sedimented residue | schematic transformation | CON-EQ-051; EXACT | not assigned from shared wording | SCHEMATIC; source-local occurrence 2 |

```tex
\begin{equation}
\text{qualia live}
\rightarrow
\text{measurement}
\rightarrow
\text{sedimented residue}
\end{equation}
```

### CON-EQ-134

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA opening_model_ja.tex](../../consciousness/sections_ja/opening_model_ja.tex):92 | F06; raw block below | T_Phi,kappa,Delta v,mu,Phi,nabla | effective index; gradient norm convention unspecified | CON-EQ-052; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
\mathcal{T}_{\Phi}
\sim
\kappa
\frac{\Delta v}{\mu}
|\nabla \Phi|
\end{equation}
```

### CON-EQ-135

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA measurement_collapse_ja.tex](../../consciousness/sections_ja/measurement_collapse_ja.tex):62 | F29; raw block below | qualia live; measurement; sedimented residue | schematic transformation | CON-EQ-053; EXACT | not assigned from shared wording | SCHEMATIC; source-local occurrence 1 |

```tex
\begin{equation}
\text{qualia live}
\rightarrow
\text{measurement}
\rightarrow
\text{sedimented residue}
\end{equation}
```

### CON-EQ-136

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA measurement_collapse_ja.tex](../../consciousness/sections_ja/measurement_collapse_ja.tex):116 | F21; raw block below | Delta v,Delta v_max | absolute-gap interval | CON-EQ-054; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
0 < |\Delta v| < \Delta v_{\max}
\end{equation}
```

### CON-EQ-137

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA measurement_collapse_ja.tex](../../consciousness/sections_ja/measurement_collapse_ja.tex):120 | F22; raw block below | mu,mu_min,mu_max | open parameter interval | CON-EQ-054; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 3 |

```tex
\begin{equation}
\mu_{\min} < \mu < \mu_{\max}
\end{equation}
```

### CON-EQ-138

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA measurement_collapse_ja.tex](../../consciousness/sections_ja/measurement_collapse_ja.tex):124 | F19; raw block below | tau,tau_min,tau_max | open interval; numerical bounds unspecified | CON-EQ-054; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 4 |

```tex
\begin{equation}
\tau_{\min} < \tau < \tau_{\max}
\end{equation}
```

### CON-EQ-139

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA measurement_collapse_ja.tex](../../consciousness/sections_ja/measurement_collapse_ja.tex):128 | F23; raw block below | T_Phi,T_min,T_max | index interval; no T_Phi_min symbol defined | CON-EQ-054; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 5 |

```tex
\begin{equation}
\mathcal{T}_{\min}
<
\mathcal{T}_{\Phi}
<
\mathcal{T}_{\max}
\end{equation}
```

### CON-EQ-140

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA measurement_collapse_ja.tex](../../consciousness/sections_ja/measurement_collapse_ja.tex):146 | F45; raw block below | Delta v,C(t),t | JA collapse implication | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 6 |

```tex
\begin{equation}
\Delta v \to 0
\quad \Rightarrow \quad
C(t) \to 0
\end{equation}
```

### CON-EQ-141

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA non_localization_ja.tex](../../consciousness/sections_ja/non_localization_ja.tex):108 | F21; raw block below | Delta v,Delta v_max | absolute-gap interval | CON-EQ-055; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
0 < |\Delta v| < \Delta v_{\max}
\end{equation}
```

### CON-EQ-142

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA non_localization_ja.tex](../../consciousness/sections_ja/non_localization_ja.tex):112 | F22; raw block below | mu,mu_min,mu_max | open parameter interval | CON-EQ-055; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
\mu_{\min} < \mu < \mu_{\max}
\end{equation}
```

### CON-EQ-143

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA non_localization_ja.tex](../../consciousness/sections_ja/non_localization_ja.tex):116 | F19; raw block below | tau,tau_min,tau_max | open interval; numerical bounds unspecified | CON-EQ-055; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 3 |

```tex
\begin{equation}
\tau_{\min} < \tau < \tau_{\max}
\end{equation}
```

### CON-EQ-144

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA non_localization_ja.tex](../../consciousness/sections_ja/non_localization_ja.tex):120 | F23; raw block below | T_Phi,T_min,T_max | index interval; no T_Phi_min symbol defined | CON-EQ-055; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 4 |

```tex
\begin{equation}
\mathcal{T}_{\min}
<
\mathcal{T}_{\Phi}
<
\mathcal{T}_{\max}
\end{equation}
```

### CON-EQ-145

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualitative_predictions_ja.tex](../../consciousness/sections_ja/qualitative_predictions_ja.tex):10 | F20; raw block below | T_Phi,kappa,Delta v,mu,Phi,nabla | effective index; explicit left/right norm delimiters | CON-EQ-056; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
\mathcal{T}_{\Phi}
\sim
\kappa
\frac{\Delta v}{\mu}
\left|\nabla \Phi\right|
\end{equation}
```

### CON-EQ-146

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualitative_predictions_ja.tex](../../consciousness/sections_ja/qualitative_predictions_ja.tex):26 | F11; raw block below | Delta v | limit toward synchrony | CON-EQ-057; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
\Delta v \rightarrow 0
\end{equation}
```

### CON-EQ-147

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualitative_predictions_ja.tex](../../consciousness/sections_ja/qualitative_predictions_ja.tex):42 | F31; raw block below | Delta v | qualitative large-gap condition; numerical scale unspecified | CON-EQ-058; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 3 |

```tex
\begin{equation}
|\Delta v| \gg 0
\end{equation}
```

### CON-EQ-148

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualitative_predictions_ja.tex](../../consciousness/sections_ja/qualitative_predictions_ja.tex):60 | F32; raw block below | mu | limit toward zero | CON-EQ-059; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 4 |

```tex
\begin{equation}
\mu \rightarrow 0
\end{equation}
```

### CON-EQ-149

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualitative_predictions_ja.tex](../../consciousness/sections_ja/qualitative_predictions_ja.tex):68 | F33; raw block below | mu | limit toward infinity | CON-EQ-060; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 5 |

```tex
\begin{equation}
\mu \rightarrow \infty
\end{equation}
```

### CON-EQ-150

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualitative_predictions_ja.tex](../../consciousness/sections_ja/qualitative_predictions_ja.tex):76 | F22; raw block below | mu,mu_min,mu_max | open parameter interval | CON-EQ-061; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 6 |

```tex
\begin{equation}
\mu_{\min} < \mu < \mu_{\max}
\end{equation}
```

### CON-EQ-151

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualitative_predictions_ja.tex](../../consciousness/sections_ja/qualitative_predictions_ja.tex):88 | F03; raw block below | tau,Delta v,mu | ratio/proportionality; constants unspecified | CON-EQ-062; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 7 |

```tex
\begin{equation}
\tau \propto \frac{\Delta v}{\mu}
\end{equation}
```

### CON-EQ-152

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualitative_predictions_ja.tex](../../consciousness/sections_ja/qualitative_predictions_ja.tex):94 | F46; raw block below | tau,tau_min | lower-window violation | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 8 |

```tex
\begin{equation}
\tau < \tau_{\min}
\end{equation}
```

### CON-EQ-153

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualitative_predictions_ja.tex](../../consciousness/sections_ja/qualitative_predictions_ja.tex):102 | F47; raw block below | tau,tau_max | upper-window violation | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 9 |

```tex
\begin{equation}
\tau > \tau_{\max}
\end{equation}
```

### CON-EQ-154

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualitative_predictions_ja.tex](../../consciousness/sections_ja/qualitative_predictions_ja.tex):110 | F19; raw block below | tau,tau_min,tau_max | open interval; numerical bounds unspecified | CON-EQ-063; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 10 |

```tex
\begin{equation}
\tau_{\min} < \tau < \tau_{\max}
\end{equation}
```

### CON-EQ-155

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualitative_predictions_ja.tex](../../consciousness/sections_ja/qualitative_predictions_ja.tex):122 | F26; raw block below | Phi,nabla; referencing bias | qualitative increase correspondence | CON-EQ-064; EXACT | not assigned from shared wording | SCHEMATIC; source-local occurrence 11 |

```tex
\begin{equation}
|\nabla \Phi| \uparrow
\quad \Rightarrow \quad
\text{referencing bias} \uparrow
\end{equation}
```

### CON-EQ-156

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualitative_predictions_ja.tex](../../consciousness/sections_ja/qualitative_predictions_ja.tex):146 | F34; raw block below | measurement; boundary closure; sedimented residue | schematic implication chain | CON-EQ-065; EXACT | not assigned from shared wording | SCHEMATIC; source-local occurrence 12 |

```tex
\begin{equation}
\text{measurement}
\quad \Rightarrow \quad
\text{boundary closure}
\quad \Rightarrow \quad
\text{sedimented residue}
\end{equation}
```

### CON-EQ-157

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualitative_predictions_ja.tex](../../consciousness/sections_ja/qualitative_predictions_ja.tex):198 | F21; raw block below | Delta v,Delta v_max | absolute-gap interval | CON-EQ-066; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 13 |

```tex
\begin{equation}
0 < |\Delta v| < \Delta v_{\max}
\end{equation}
```

### CON-EQ-158

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualitative_predictions_ja.tex](../../consciousness/sections_ja/qualitative_predictions_ja.tex):202 | F22; raw block below | mu,mu_min,mu_max | open parameter interval | CON-EQ-066; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 14 |

```tex
\begin{equation}
\mu_{\min} < \mu < \mu_{\max}
\end{equation}
```

### CON-EQ-159

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualitative_predictions_ja.tex](../../consciousness/sections_ja/qualitative_predictions_ja.tex):206 | F19; raw block below | tau,tau_min,tau_max | open interval; numerical bounds unspecified | CON-EQ-066; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 15 |

```tex
\begin{equation}
\tau_{\min} < \tau < \tau_{\max}
\end{equation}
```

### CON-EQ-160

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualitative_predictions_ja.tex](../../consciousness/sections_ja/qualitative_predictions_ja.tex):210 | F23; raw block below | T_Phi,T_min,T_max | index interval; no T_Phi_min symbol defined | CON-EQ-066; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 16 |

```tex
\begin{equation}
\mathcal{T}_{\min}
<
\mathcal{T}_{\Phi}
<
\mathcal{T}_{\max}
\end{equation}
```

### CON-EQ-161

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA qualitative_predictions_ja.tex](../../consciousness/sections_ja/qualitative_predictions_ja.tex):271 | F48; raw block below | Delta v,mu,tau,T_Phi,nabla Phi; consciousness window | tuple membership; spacing variant | CON-EQ-067; EXACT | not assigned from shared wording | SCHEMATIC; source-local occurrence 17 |

```tex
\begin{equation}
\text{stable consciousness}
\quad \Leftrightarrow \quad
(\Delta v,\mu,\tau,\mathcal{T}_{\Phi},\nabla\Phi)
\in
\text{consciousness window}
\end{equation}
```

### CON-EQ-162

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA pathologies_limits_ja.tex](../../consciousness/sections_ja/pathologies_limits_ja.tex):18 | F21; raw block below | Delta v,Delta v_max | absolute-gap interval | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 1 |

```tex
\begin{equation}
0 < |\Delta v| < \Delta v_{\max}
\end{equation}
```

### CON-EQ-163

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA pathologies_limits_ja.tex](../../consciousness/sections_ja/pathologies_limits_ja.tex):22 | F22; raw block below | mu,mu_min,mu_max | open parameter interval | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
\mu_{\min} < \mu < \mu_{\max}
\end{equation}
```

### CON-EQ-164

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA pathologies_limits_ja.tex](../../consciousness/sections_ja/pathologies_limits_ja.tex):26 | F19; raw block below | tau,tau_min,tau_max | open interval; numerical bounds unspecified | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 3 |

```tex
\begin{equation}
\tau_{\min} < \tau < \tau_{\max}
\end{equation}
```

### CON-EQ-165

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA pathologies_limits_ja.tex](../../consciousness/sections_ja/pathologies_limits_ja.tex):30 | F23; raw block below | T_Phi,T_min,T_max | index interval; no T_Phi_min symbol defined | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 4 |

```tex
\begin{equation}
\mathcal{T}_{\min}
<
\mathcal{T}_{\Phi}
<
\mathcal{T}_{\max}
\end{equation}
```

### CON-EQ-166

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA pathologies_limits_ja.tex](../../consciousness/sections_ja/pathologies_limits_ja.tex):66 | F11; raw block below | Delta v | limit toward synchrony | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 5 |

```tex
\begin{equation}
\Delta v \rightarrow 0
\end{equation}
```

### CON-EQ-167

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA pathologies_limits_ja.tex](../../consciousness/sections_ja/pathologies_limits_ja.tex):90 | F49; raw block below | Delta v,Delta v_max | limit or beyond; qualitative phrase included | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 6 |

```tex
\begin{equation}
|\Delta v| \rightarrow \Delta v_{\max}
\quad \text{or beyond}
\end{equation}
```

### CON-EQ-168

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA pathologies_limits_ja.tex](../../consciousness/sections_ja/pathologies_limits_ja.tex):115 | F32; raw block below | mu | limit toward zero | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 7 |

```tex
\begin{equation}
\mu \rightarrow 0
\end{equation}
```

### CON-EQ-169

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA pathologies_limits_ja.tex](../../consciousness/sections_ja/pathologies_limits_ja.tex):141 | F33; raw block below | mu | limit toward infinity | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 8 |

```tex
\begin{equation}
\mu \rightarrow \infty
\end{equation}
```

### CON-EQ-170

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA pathologies_limits_ja.tex](../../consciousness/sections_ja/pathologies_limits_ja.tex):165 | F50; raw block below | Phi,nabla | weak-gradient limit | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 9 |

```tex
\begin{equation}
|\nabla \Phi| \rightarrow 0
\end{equation}
```

### CON-EQ-171

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA pathologies_limits_ja.tex](../../consciousness/sections_ja/pathologies_limits_ja.tex):189 | F51; raw block below | Phi,nabla | large-gradient limit | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 10 |

```tex
\begin{equation}
|\nabla \Phi| \rightarrow \infty
\end{equation}
```

### CON-EQ-172

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA pathologies_limits_ja.tex](../../consciousness/sections_ja/pathologies_limits_ja.tex):271 | F06; raw block below | T_Phi,kappa,Delta v,mu,Phi,nabla | effective index; gradient norm convention unspecified | JA-ONLY display; §21のinline/reprise/new-form内訳参照; JA-ONLY | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 11 |

```tex
\begin{equation}
\mathcal{T}_{\Phi}
\sim
\kappa
\frac{\Delta v}{\mu}
|\nabla \Phi|
\end{equation}
```

### CON-EQ-173

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA relation_to_note_ja.tex](../../consciousness/sections_ja/relation_to_note_ja.tex):105 | F52; raw block below | Delta v,mu,tau,T_Phi,nabla Phi; Log Referencing | schematic argument list; spacing variant | CON-EQ-068; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | SCHEMATIC; source-local occurrence 1 |

```tex
\begin{equation}
\text{Consciousness}
\sim
\text{Log Referencing}
\left(
\Delta v,
\mu,
\tau,
\mathcal{T}_{\Phi},
\nabla \Phi
\right)
\end{equation}
```

### CON-EQ-174

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA conclusion_ja.tex](../../consciousness/sections_ja/conclusion_ja.tex):82 | F52; raw block below | Delta v,mu,tau,T_Phi,nabla Phi; Log Referencing | schematic argument list; spacing variant | CON-EQ-069; MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE | not assigned from shared wording | SCHEMATIC; source-local occurrence 1 |

```tex
\begin{equation}
\text{Consciousness}
\sim
\text{Log Referencing}
\left(
\Delta v,
\mu,
\tau,
\mathcal{T}_{\Phi},
\nabla \Phi
\right)
\end{equation}
```

### CON-EQ-175

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA conclusion_ja.tex](../../consciousness/sections_ja/conclusion_ja.tex):101 | F21; raw block below | Delta v,Delta v_max | absolute-gap interval | CON-EQ-070; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 2 |

```tex
\begin{equation}
0 < |\Delta v| < \Delta v_{\max}
\end{equation}
```

### CON-EQ-176

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA conclusion_ja.tex](../../consciousness/sections_ja/conclusion_ja.tex):105 | F22; raw block below | mu,mu_min,mu_max | open parameter interval | CON-EQ-071; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 3 |

```tex
\begin{equation}
\mu_{\min} < \mu < \mu_{\max}
\end{equation}
```

### CON-EQ-177

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA conclusion_ja.tex](../../consciousness/sections_ja/conclusion_ja.tex):109 | F19; raw block below | tau,tau_min,tau_max | open interval; numerical bounds unspecified | CON-EQ-072; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 4 |

```tex
\begin{equation}
\tau_{\min} < \tau < \tau_{\max}
\end{equation}
```

### CON-EQ-178

| Source | Exact form | Local symbols | Apparent domain | EN/JA counterpart | Upstream analogue | Source identity / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [JA conclusion_ja.tex](../../consciousness/sections_ja/conclusion_ja.tex):113 | F23; raw block below | T_Phi,T_min,T_max | index interval; no T_Phi_min symbol defined | CON-EQ-073; EXACT | not assigned from shared wording | CONSCIOUSNESS-LOCAL; source-local occurrence 5 |

```tex
\begin{equation}
\mathcal{T}_{\min}
<
\mathcal{T}_{\Phi}
<
\mathcal{T}_{\max}
\end{equation}
```

## 3. Equation source identity

各出現への主分類は§2最終列。これはsourceが提示する出自・引用形式であり、上流と同一signature/同一carrierであるとの承認ではない。とくに「IFGT core relations」と呼ばれるkernel式と、本文が「older VED」と呼ぶPDEの**実際の照合先**は§13–14で分離する。

| Source identity | Entries | 適用対象 |
| --- | ---: | --- |
| CONSCIOUSNESS-LOCAL | 127 | gap/index/window/JA追加式などのlocal expression |
| IFGT-REUSED | 18 | 本文がIFGT templateとして提示するbalance/flow/force/kernel |
| VED-REUSED | 2 | node-pair C_ijの引用 |
| BIO-INSPIRED | 0 | Bio-inspired chainはinlineであり表示式件数に含めない |
| CT-REUSED | 2 | token couplingのbracket引用 |
| DOWNSTREAM-REPRISE | 0 | current displayに専用分類する出現なし。Intelligenceの語彙再利用は別表 |
| HISTORICAL / OLDER-VERSION | 2 | older VEDというラベルのPDE、EN/JA各1 |
| SCHEMATIC | 27 | correspondences、Log Referencing、順序、text-only equation |
| UNRESOLVED | 0 | 主たるsource presentationを分類できたという意味だけ。object identity未解決は§24 |
| Total | 178 | EN 73、JA 105 |

## 4. Symbol family inventory

「first」はcurrent読書順の導入であり歴史的発明時点ではない。sourceに数値域の宣言がなくscalar-like/vector-likeとする場合は演算位置からの限定的signature推定である。正確な空間集合や単位は補わない。`EQ-xxx`という短縮locatorはすべて§2の`CON-EQ-xxx`を指す。

| CON-SYM | Glyph | Source-local meaning | Signature/domain | First authoritative use | Collisions / upstream same-glyph objects |
| --- | --- | --- | --- | --- | --- |
| CON-SYM-001 | `t` | physical/external time | time parameter; exact domain未固定 | S03:7; S06 IFGT template | IFGT tau / Bio external t / CT x,tau |
| CON-SYM-002 | `\tau` | internal delay,buffer,retention; JA reference-duration | ratio-related temporal quantity; exact domain未固定 | S00; S03:8; S04 Internal Delay; JA S07:50 | VED ordering/Bio progression/CT long-time tau |
| CON-SYM-003 | `\mathcal{T}` | effective torque-like transformation load | effective index; scalar-like; exact domain未固定 | S00; S03:13; S05 Effective Torque | Intelligence I stopping operator; plain T not adopted |
| CON-SYM-004 | `\mathcal{T}_{\Phi}` | meaning-gradient-coupled effective index | scalar-like index; exact domain未固定 | S05 Bridge; EQ-008/084 | T versus T_i; no psychological strength identity |
| CON-SYM-005 | `v_f` | fast predictive/reactive dynamics | rate parameter; numerical type unresolved; exact domain未固定 | S00; S03:9; S04 | figure v_f; local Delta v_i |
| CON-SYM-006 | `v_s` | slow sedimentary dynamics | rate parameter; numerical type unresolved; exact domain未固定 | S00; S03:10; S04 | rho_s is not v_s |
| CON-SYM-007 | `\Delta v` | fast-minus-slow difference | difference; exact domain未固定 | S00; EQ-001/074 | Delta C / Delta v_i / source Delta |
| CON-SYM-008 | `\mu` | coupling viscosity | positive bounded parameter, scalar-like; exact domain未固定 | S00; S03:12; EQ-025/102 | IFGT/CT/Bio response mu; mu_I |
| CON-SYM-009 | `\mu_I` | flow mobility | coefficient; exact domain未固定 | S06:205; EQ-010/086 | coupling mu has different local description |
| CON-SYM-010 | `I` | re-referenceable log density | field, scalar-like; exact domain未固定 | S00/S03; S06:160 | IFGT traces; Bio constraint; CT tension; Intelligence effective I |
| CON-SYM-011 | `J` | plain flow glyph in working draft/upstream, not current core flow symbol | source-dependent vector/flow; exact domain未固定 | draft abstract; current upstream comparison | VED J_ij / IFGT J / Bio bold J |
| CON-SYM-012 | `J_I` | IFGT-template information flow | vector-like field under divergence; exact domain未固定 | S00; S06:190 | IFGT plain J; J_log not equated by formula |
| CON-SYM-013 | `J_{\log},J_{\mathrm{log}}` | local referencing flow | window-local flow; vector-like; exact domain未固定 | S00; S03:16; S06:37–40 | general J_I vs local use; typography log/mathrm |
| CON-SYM-014 | `\Phi` | information/meaning potential | potential field, scalar-like; exact domain未固定 | S00; S03:14; S06:163 | CT landscape; Bio Phi[I]; Intelligence global constraint |
| CON-SYM-015 | `F` | effective force from potential | gradient-shaped/vector-like; exact domain未固定 | S06:198,205 | Bio bold F / F_k / F(x;theta); Intelligence F(x_n) |
| CON-SYM-016 | `F_I` | CT quoted information-force glyph | source-dependent gradient field; exact domain未固定 | S09 CT quote:129 | IFGT F_I, current core F |
| CON-SYM-017 | `C` | field closure in older PDE | field, scalar-like; exact domain未固定 | S06 older PDE EQ-019/095 | C_ij, C_f/C_s, JA C(t), CT fixation |
| CON-SYM-018 | `C_{ij}` | closure degree between nodes in this quotation | node-pair scalar entry; exact domain未固定 | S06:261; EQ-015/091 | Vol.1 calls causal-log matrix entry |
| CON-SYM-019 | `C_f` | fast-layer effective closure degree | effective layer quantity, scalar-like; exact domain未固定 | S06:273 | matrix/field C, Delta C |
| CON-SYM-020 | `C_s` | slow-layer effective closure degree | effective layer quantity, scalar-like; exact domain未固定 | S06:273 | rho_s log density; C(t) opening |
| CON-SYM-021 | `\Delta C` | C_s minus C_f | difference; exact domain未固定 | EQ-016/092 | source claims same condition as Delta v |
| CON-SYM-022 | `C(t)` | conscious access / opening in JA | function of t; output type unspecified; exact domain未固定 | JA S07:42–52; EQ-101/140 | closure field C is not this source-local definition |
| CON-SYM-023 | `K` | kernel giving Phi from I | kernel; exact domain未固定 | S06:205; EQ-012/088 | CT convolution kernel, no current IFGT K*I locator found |
| CON-SYM-024 | `\sigma` | generation-dissipation term for I | source field, scalar-like; exact domain未固定 | EQ-009/085; S06:205 | IFGT decomposed source / VED rate / Bio source slot |
| CON-SYM-025 | `\kappa` | scale factor of T | parameter; exact domain未固定 | S05 Effective Torque | not kappa_B barrier strength |
| CON-SYM-026 | `D` | diffusion coefficient | parameter; exact domain未固定 | S06:205 | IFGT/CT/Bio diffusion parameters not numerically mapped |
| CON-SYM-027 | `\lambda [node]` | scale factor in C_ij expression | parameter; exact domain未固定 | S06:265 | upstream selection sensitivity; CT token lambda distinct use |
| CON-SYM-028 | `\lambda [token]` | coefficient in CT token coupling quote | coefficient, scalar-like; exact domain未固定 | EQ-007/083; S05 CT quote | same lambda glyph as node relation |
| CON-SYM-029 | `\rho_i` | difference density at node i | indexed density quantity; exact domain未固定 | S06:265 | current Vol.1 log density; Bio rho progression; JA rho_s |
| CON-SYM-030 | `H_{ij}` | node connection strength in quotation | node-pair quantity; exact domain未固定 | S06:265 | current Vol.1 accumulated causal history |
| CON-SYM-031 | `i,j [nodes]` | node labels | discrete index; exact domain未固定 | S06 VED Closure Degree | token/log i are different index carriers |
| CON-SYM-032 | `a` | old-PDE drive coefficient | parameter; definition not local; exact domain未固定 | EQ-019/095 | IFGT generation rate |
| CON-SYM-033 | `\Delta` | old-PDE difference source | source factor; not speed difference; exact domain未固定 | EQ-019/095 | IFGT difference source; gradient Delta not specified here |
| CON-SYM-034 | `C_*` | closure scale in drive term | parameter; local type not fixed; exact domain未固定 | EQ-019/095 | IFGT effective saturation scale |
| CON-SYM-035 | `C_{\max}` | saturation boundary in barrier denominator | upper-bound parameter; exact domain未固定 | EQ-019/095; S06 third-term prose | IFGT C_max=1 is upstream convention, not local C(t) bound |
| CON-SYM-036 | `\Gamma` | dissipation coefficient | parameter; local units absent; exact domain未固定 | EQ-019/095 | IFGT dissipation rate |
| CON-SYM-037 | `\kappa_B` | effective barrier coefficient | parameter; no relation to kappa given; exact domain未固定 | EQ-019/095 | IFGT barrier / VED effective barrier |
| CON-SYM-038 | `J_C` | closure-field current in older PDE | vector-like under divergence; exact domain未固定 | EQ-019/095 | IFGT eq:J_C separately specified, no local replacement rule |
| CON-SYM-039 | `x` | x in I(x,tau),nabla Phi(x) in CT correspondence | field argument; coordinate domain unspecified; exact domain未固定 | S09 CT quote; S20 table | Bio state x, Intelligence x_n, CT coordinate |
| CON-SYM-040 | `\Phi^*` | long-time landscape attractor | limiting field/state; exact domain未固定 | S09 CT quote:61; S20 | not T_Phi; no local basin signature |
| CON-SYM-041 | `\ell_i,\ell_{i}` | linguistic tokens in CT quote | indexed token with dot-gradient coupling; exact domain未固定 | EQ-007/083 | token type/codomain not specified in local quote |
| CON-SYM-042 | `A_i` | local attention weight in JA | indexed weight, scalar-like; exact domain未固定 | JA S05:114; EQ-079/081 | attention as temporal transformation elsewhere |
| CON-SYM-043 | `m_i` | log information mass / sedimentation in JA | indexed weight, scalar-like; exact domain未固定 | JA S05:114 | VED effective mass vs CT log/concept weight; not mass unit assigned |
| CON-SYM-044 | `\mathcal{T}_i` | local torque-like load in JA | indexed effective index; exact domain未固定 | JA S05:114–123; EQ-079/080 | global T/T_Phi, no local mu_i formula supplied |
| CON-SYM-045 | `\Delta v_i` | local speed gap in JA | indexed difference quantity; exact domain未固定 | EQ-080/081 | global Delta v; v_f,i and v_s,i not introduced |
| CON-SYM-046 | `\rho_s` | slow-layer sedimented log density in JA | density input to cal F; exact domain未固定 | JA S07:48; EQ-101 | I logs / rho_i nodes / Bio rho(I,J); equality not given |
| CON-SYM-047 | `\mathcal{F}` | function of Delta v,rho_s,tau in JA | three-argument function, codomain unspecified; exact domain未固定 | EQ-101 | F gradient force / F_k / F(x;theta) are distinct local signatures |
| CON-SYM-048 | `\Delta v_{\max};\Delta C_{\max}` | upper gap bounds | bound parameters; exact domain未固定 | EQ-018/034/094/111 | different gaps, no conversion factor |
| CON-SYM-049 | `\mu_{\min},\mu_{\max};\tau_{\min},\tau_{\max}` | window parameter bounds | bound parameters; exact domain未固定 | EQ-027/035 etc. | not numerical biological thresholds |
| CON-SYM-050 | `\mathcal{T}_{\min},\mathcal{T}_{\max}` | bounds applied to T_Phi | bound parameters; exact domain未固定 | EQ-037/114 | no subscript-Phi bounds declared; not alter glyph |
| CON-SYM-051 | `\Delta v_{\min}` | figure3 lower gap bound | figure bound, numerical value unspecified; exact domain未固定 | FIG-03 EN/JA text layer and higher-resolution render | body uses 0 < absolute gap; equality to zero not given |
| CON-SYM-052 | `i [log/token]` | log/concept index in JA, token index in CT quote | index carrier unspecified across uses; exact domain未固定 | JA S05:114; EQ-007/083 | node i,j not automatically same set |
| CON-SYM-053 | `\nabla,\nabla\cdot,\partial_t,*,\lvert\cdot\rvert` | gradient/divergence/derivative/convolution/norm notation | operators on locally unspecified fields/domains; exact domain未固定 | S06/S07 template; figure4 | geometry,boundary,kernel/norm conventions not supplied |
| CON-SYM-054 | `Log Referencing(...); consciousness window` | named schematic map / region | mapping/set signature unspecified; exact domain未固定 | EQ-022/039/067 | not a typed scalar consciousness measure |
| CON-SYM-055 | `M` | Bio-inspired chain morphogen-like field | borrowed model state; local signature unspecified; exact domain未固定 | S04:17–20 | Bio toy M, not Consciousness neural variable |
| CON-SYM-056 | `\mathcal{I}` | Bio-inspired chain constraint density | borrowed model state; local signature unspecified; exact domain未固定 | S04:17–20 | chain cal I vs Bio toy I vs local log I |
| CON-SYM-057 | `N` | Bio-inspired chain neural-like commitment | borrowed model state; local signature unspecified; exact domain未固定 | S04:17–20 | not node count or neural observable |
| CON-SYM-058 | `B` | Bio-inspired chain boundary-like accumulation | borrowed model state; local signature unspecified; exact domain未固定 | S04:17–20 | not kappa_B or self/world boundary |
| CON-SYM-059 | `E` | Bio-inspired chain eye-like commitment | borrowed model state; local signature unspecified; exact domain未固定 | S04:17–20 | not energy or phenomenal state |
| CON-SYM-060 | `\sigma_{\text{drive}}` | CT novel-input driving source in correspondence quotation | source component; local signature unspecified; exact domain未固定 | S09 CT correspondence quote | not the entire sigma or Bio gene source |

Entryのmacrosは両言語共通: `Info=I`, `Potential=Phi`, `Flow=J_log`, `physTime=t`, `intTime=tau`, `vfast=v_mathrm{f}`, `vslow=v_mathrm{s}`, `deltav=Delta v`, `Torque=mathcal{T}`, `viscosity=mu`, `kappaC=kappa`。macro名とglyphは別名参照であって新しいobjectではない。user指定のplain Tに対応するcurrent torque glyphは**mathcal T**。tauをtorqueと読むことをS03は明示的に否定する。

全inline mathの追加走査では、Bio chainのM/cal I/N/B/E、CTのsigma_drive、I(x,tau)>0、Phiの長時間極限、concept条件、node/closure極限も回収した。図のmin boundはCON-SYM-051。glyphを持たないSSO、projection、qualia等は§9・15–19へ分ける。

## 5. Collision ledger

「同じsignature?」は式形・引数・演算位置の比較に限る。「同じdomain?」が未固定ならUNRESOLVED。最終列は本phaseの認定ではなく、sourceのidentity wordingの有無だけを示す。上流の型をlocalへ自動転記しない。

| CON-COL | Glyph | Object A | Object B | Same signature? | Same domain? | Identity stated? | Identity established? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CON-COL-001 | I | local re-referenceable logs S06 | IFGT persistent traces / Bio constraints / CT unresolved tension | field-like共通、引数省略あり | separate projected windows | S06直接同定を否定 | NOT ASSESSED IN PHASE 01 |
| CON-COL-002 | J | local J_I,J_log | VED J_ij / IFGT vector J / Bio bold J / working plain J | pair-index vs vector-like vs local flow | 異なるcarrier記述 | local flowとgeneral flowを分離 | NOT ASSESSED IN PHASE 01 |
| CON-COL-003 | Phi / gradient | meaning bias S09 | CT concept geometry | gradient表記は共通 | window別 | S09 “same quantity”、S20非単純同一を併記 | SOURCE CLAIMS IDENTITY |
| CON-COL-004 | F | local -grad Phi / CT F_I | Bio F_k, F(x;theta) / Intelligence F(x_n) | vector-like/response/functionで異なる | UNRESOLVED cross-map | shared Fの同一式なし | NOT ASSESSED IN PHASE 01 |
| CON-COL-005 | C | older closure field / C_ij | JA C(t) conscious opening | field/matrix/functionの別定義 | node/field/opening別 | local equalityなし | NOT ASSESSED IN PHASE 01 |
| CON-COL-006 | C_f,C_s,Delta C / Delta v | effective layer closure gap | speed gap | difference形は類似、no transform | coordinate relation未固定 | S06 same condition / different coordinates | SOURCE CLAIMS IDENTITY |
| CON-COL-007 | tau | SSO delay / JA reference duration | IFGT ordering / VED time / Bio progression / CT long-time | ratio vs time parameter vs accumulation | separate sources | S03 subjective time自体を否定 | NOT ASSESSED IN PHASE 01 |
| CON-COL-008 | mu / mu_I | coupling viscosity | information-flow mobility / IFGT/Bio response coefficient | parameter共通、別式位置 | calibration未固定 | equalityなし | NOT ASSESSED IN PHASE 01 |
| CON-COL-009 | mathcal T | local effective torque | Intelligence I stopping operator | scalar-like index vs operator | distinct definitions | identityなし | NOT ASSESSED IN PHASE 01 |
| CON-COL-010 | T / T_Phi / T_i | global index、gradient extension | JA indexed local load | global vs indexed、relation別 | index set未固定 | S05 extension、JA local approximation | NOT ASSESSED IN PHASE 01 |
| CON-COL-011 | K | local kernel in Phi=K*I | CT kernel / IFGT source label | convolution-like共通 | kernel domain未固定 | “IFGT core”との出自表示 | NOT ASSESSED IN PHASE 01 |
| CON-COL-012 | sigma | local generation-dissipation slot | IFGT mismatch / VED source / Bio source | balance source位置類似 | same process未指定 | cross-process identityなし | NOT ASSESSED IN PHASE 01 |
| CON-COL-013 | sigma_drive | CT input spike S09 | whole local sigma | component vs whole source | map未固定 | 同一とは書かない | NOT ASSESSED IN PHASE 01 |
| CON-COL-014 | x | CT I(x,tau),Phi(x) | Bio state x / Intelligence state x_n | coordinate vs state argument | distinct carriers | equalityなし | NOT ASSESSED IN PHASE 01 |
| CON-COL-015 | t | external physical/evolution t | IFGT tau template / Bio recording t | different derivative parameter | translation未固定 | substitution law localになし | NOT ASSESSED IN PHASE 01 |
| CON-COL-016 | rho | node rho_i / JA slow rho_s | VED node density / Bio progression rho | indexed density vs rate function | distinct local uses | equalityなし | NOT ASSESSED IN PHASE 01 |
| CON-COL-017 | lambda | node C_ij scale | CT token coupling coefficient | parameter位置別 | index carrier別 | equalityなし | NOT ASSESSED IN PHASE 01 |
| CON-COL-018 | kappa / kappa_B | torque scale | older-PDE barrier coefficient | numerator scale vs barrier | units未固定 | equalityなし | NOT ASSESSED IN PHASE 01 |
| CON-COL-019 | i,j | nodes in C_ij,H_ij | token ell_i / JA log A_i,m_i | discrete index共通、carrier別 | node vs token/log | 同じindex集合との宣言なし | NOT ASSESSED IN PHASE 01 |
| CON-COL-020 | D | local template diffusion | IFGT/Bio toy diffusion | coefficient共通 | numeric translationなし | equalityなし | NOT ASSESSED IN PHASE 01 |
| CON-COL-021 | cal I / I | Bio chain constraint glyph | local log I / Bio toy I | source-local fields | chain/window別 | direct identityなし | NOT ASSESSED IN PHASE 01 |
| CON-COL-022 | N,B,E | borrowed toy state labels | neural/boundary/eye prose objects | state labels vs interpretive terms | Bio toy vs local window | S04 model-like scope | NOT ASSESSED IN PHASE 01 |
| CON-COL-023 | m_i | JA information mass/sedimentation | VED effective mass / projection mass assignment | weight-like vs other source quantities | no common unit supplied | equalityなし | NOT ASSESSED IN PHASE 01 |
| CON-COL-024 | cal F / F | JA three-input opening function | local gradient F / Bio response/evolution F | different arity / expression | different local domains | equalityなし | NOT ASSESSED IN PHASE 01 |
| CON-COL-025 | Delta | older-PDE driving difference | Delta v / Delta C / gradient operator | source factor vs differences vs operator | distinct expression positions | no identification rule | NOT ASSESSED IN PHASE 01 |
| CON-COL-026 | Phi* / C_* | CT long-time landscape | saturation parameter in old PDE | limiting object vs parameter | different carriers | same star not identity | NOT ASSESSED IN PHASE 01 |
| CON-COL-027 | J / J_I | local information/log flow | Intelligence II J(x) justification measure | vector-like flow vs state-to-real measure | field window vs inference state | identityなし | NOT ASSESSED IN PHASE 01 |

Intelligence collisionのcurrent locatorは[I stopping operator](../../intelligence-part1/sections/08_the_non_closure_of_individual_intelligence.tex):11（mathcal T / mathcal R）および[II inference](../../intelligence-part2/sections/02_inference_operator.tex):10–20（F(x_n)、J(x)）。これらはsource-local signature対照だけであり、Intelligenceの独立監査ではない。

## 6. Signature inventory

EXPLICITはsourceがparameter/kernel/function等の局所的型・引数を明記したもの、INFERREDは演算位置からの最小推定、UNRESOLVEDはrate/field/operator等の厳密型まで固定できないもの。EXPLICITも完全なdomain→codomain仕様の完成を意味しない。scalar-likeを実数値測定量へ昇格させない。

| SIG-ID | Object | Signature | Domain | Codomain | Source | Explicit / inferred |
| --- | --- | --- | --- | --- | --- | --- |
| SIG-001 | CON-SYM-001 | time parameter | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S03:7; S06 IFGT template | EXPLICIT |
| SIG-002 | CON-SYM-002 | ratio-related temporal quantity | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S00; S03:8; S04 Internal Delay; JA S07:50 | EXPLICIT |
| SIG-003 | CON-SYM-003 | effective index; scalar-like | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S00; S03:13; S05 Effective Torque | INFERRED |
| SIG-004 | CON-SYM-004 | scalar-like index | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S05 Bridge; EQ-008/084 | INFERRED |
| SIG-005 | CON-SYM-005 | rate parameter; numerical type unresolved | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S00; S03:9; S04 | UNRESOLVED |
| SIG-006 | CON-SYM-006 | rate parameter; numerical type unresolved | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S00; S03:10; S04 | UNRESOLVED |
| SIG-007 | CON-SYM-007 | difference | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S00; EQ-001/074 | EXPLICIT |
| SIG-008 | CON-SYM-008 | positive bounded parameter, scalar-like | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S00; S03:12; EQ-025/102 | INFERRED |
| SIG-009 | CON-SYM-009 | coefficient | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S06:205; EQ-010/086 | EXPLICIT |
| SIG-010 | CON-SYM-010 | field, scalar-like | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S00/S03; S06:160 | INFERRED |
| SIG-011 | CON-SYM-011 | source-dependent vector/flow | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | draft abstract; current upstream comparison | UNRESOLVED |
| SIG-012 | CON-SYM-012 | vector-like field under divergence | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S00; S06:190 | INFERRED |
| SIG-013 | CON-SYM-013 | window-local flow; vector-like | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S00; S03:16; S06:37–40 | INFERRED |
| SIG-014 | CON-SYM-014 | potential field, scalar-like | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S00; S03:14; S06:163 | INFERRED |
| SIG-015 | CON-SYM-015 | gradient-shaped/vector-like | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S06:198,205 | INFERRED |
| SIG-016 | CON-SYM-016 | source-dependent gradient field | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S09 CT quote:129 | INFERRED |
| SIG-017 | CON-SYM-017 | field, scalar-like | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S06 older PDE EQ-019/095 | INFERRED |
| SIG-018 | CON-SYM-018 | node-pair scalar entry | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S06:261; EQ-015/091 | INFERRED |
| SIG-019 | CON-SYM-019 | effective layer quantity, scalar-like | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S06:273 | INFERRED |
| SIG-020 | CON-SYM-020 | effective layer quantity, scalar-like | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S06:273 | INFERRED |
| SIG-021 | CON-SYM-021 | difference | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | EQ-016/092 | EXPLICIT |
| SIG-022 | CON-SYM-022 | function of t; output type unspecified | t / listed three arguments | UNRESOLVED（命名だけから数値域を補わない） | JA S07:42–52; EQ-101/140 | INFERRED |
| SIG-023 | CON-SYM-023 | kernel | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S06:205; EQ-012/088 | EXPLICIT |
| SIG-024 | CON-SYM-024 | source field, scalar-like | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | EQ-009/085; S06:205 | INFERRED |
| SIG-025 | CON-SYM-025 | parameter | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S05 Effective Torque | EXPLICIT |
| SIG-026 | CON-SYM-026 | parameter | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S06:205 | EXPLICIT |
| SIG-027 | CON-SYM-027 | parameter | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S06:265 | EXPLICIT |
| SIG-028 | CON-SYM-028 | coefficient, scalar-like | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | EQ-007/083; S05 CT quote | INFERRED |
| SIG-029 | CON-SYM-029 | indexed density quantity | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S06:265 | INFERRED |
| SIG-030 | CON-SYM-030 | node-pair quantity | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S06:265 | INFERRED |
| SIG-031 | CON-SYM-031 | discrete index | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S06 VED Closure Degree | EXPLICIT |
| SIG-032 | CON-SYM-032 | parameter; definition not local | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | EQ-019/095 | UNRESOLVED |
| SIG-033 | CON-SYM-033 | source factor; not speed difference | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | EQ-019/095 | UNRESOLVED |
| SIG-034 | CON-SYM-034 | parameter; local type not fixed | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | EQ-019/095 | UNRESOLVED |
| SIG-035 | CON-SYM-035 | upper-bound parameter | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | EQ-019/095; S06 third-term prose | INFERRED |
| SIG-036 | CON-SYM-036 | parameter; local units absent | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | EQ-019/095 | UNRESOLVED |
| SIG-037 | CON-SYM-037 | parameter; no relation to kappa given | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | EQ-019/095 | UNRESOLVED |
| SIG-038 | CON-SYM-038 | vector-like under divergence | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | EQ-019/095 | INFERRED |
| SIG-039 | CON-SYM-039 | field argument; coordinate domain unspecified | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S09 CT quote; S20 table | UNRESOLVED |
| SIG-040 | CON-SYM-040 | limiting field/state | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S09 CT quote:61; S20 | INFERRED |
| SIG-041 | CON-SYM-041 | indexed token with dot-gradient coupling | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | EQ-007/083 | UNRESOLVED |
| SIG-042 | CON-SYM-042 | indexed weight, scalar-like | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | JA S05:114; EQ-079/081 | INFERRED |
| SIG-043 | CON-SYM-043 | indexed weight, scalar-like | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | JA S05:114 | INFERRED |
| SIG-044 | CON-SYM-044 | indexed effective index | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | JA S05:114–123; EQ-079/080 | INFERRED |
| SIG-045 | CON-SYM-045 | indexed difference quantity | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | EQ-080/081 | INFERRED |
| SIG-046 | CON-SYM-046 | density input to cal F | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | JA S07:48; EQ-101 | INFERRED |
| SIG-047 | CON-SYM-047 | three-argument function, codomain unspecified | t / listed three arguments | UNRESOLVED（命名だけから数値域を補わない） | EQ-101 | EXPLICIT |
| SIG-048 | CON-SYM-048 | bound parameters | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | EQ-018/034/094/111 | EXPLICIT |
| SIG-049 | CON-SYM-049 | bound parameters | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | EQ-027/035 etc. | EXPLICIT |
| SIG-050 | CON-SYM-050 | bound parameters | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | EQ-037/114 | EXPLICIT |
| SIG-051 | CON-SYM-051 | figure bound, numerical value unspecified | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | FIG-03 EN/JA text layer and higher-resolution render | UNRESOLVED |
| SIG-052 | CON-SYM-052 | index carrier unspecified across uses | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | JA S05:114; EQ-007/083 | UNRESOLVED |
| SIG-053 | CON-SYM-053 | operators on locally unspecified fields/domains | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S06/S07 template; figure4 | UNRESOLVED |
| SIG-054 | CON-SYM-054 | mapping/set signature unspecified | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | EQ-022/039/067 | UNRESOLVED |
| SIG-055 | CON-SYM-055 | borrowed model state; local signature unspecified | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S04:17–20 | UNRESOLVED |
| SIG-056 | CON-SYM-056 | borrowed model state; local signature unspecified | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S04:17–20 | UNRESOLVED |
| SIG-057 | CON-SYM-057 | borrowed model state; local signature unspecified | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S04:17–20 | UNRESOLVED |
| SIG-058 | CON-SYM-058 | borrowed model state; local signature unspecified | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S04:17–20 | UNRESOLVED |
| SIG-059 | CON-SYM-059 | borrowed model state; local signature unspecified | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S04:17–20 | UNRESOLVED |
| SIG-060 | CON-SYM-060 | source component; local signature unspecified | source-local window / carrier; exact set UNRESOLVED | UNRESOLVED（命名だけから数値域を補わない） | S09 CT correspondence quote | UNRESOLVED |

集計は60行、EXPLICIT 14 / INFERRED 26 / UNRESOLVED 20。詳細域は各source-local window/index carrierに留まる。特にSIG-022はC(t)の引数t、SIG-047はcal Fの3引数であり、同じdomainではない。bound inequalitiesは対象量の許容範囲を述べるが、量の全codomain/単位を決めない。

## 7. Units / dimensional-status inventory

| UNIT-ID | Object | Status | Source / inventory note |
| --- | --- | --- | --- |
| UNIT-01 | v_f,v_s | absent | S04/S07 speed/rateという語。Hzやtime inverseの指定なし |
| UNIT-02 | Delta v | implicit | 差として明示、基礎rate単位未固定 |
| UNIT-03 | mu | absent | viscosity比喩から流体粘性単位を補わない |
| UNIT-04 | Delta v / mu | ratio-defined | 比は明示。dimensionlessとは書かれていない |
| UNIT-05 | tau | implicit | delay/time thicknessの語。比例定数とcalibration未固定 |
| UNIT-06 | T,T_Phi | ratio-defined | 有効index。mechanical torque単位を推定しない |
| UNIT-07 | I | absent | local log density、densityの分母/測度未指定 |
| UNIT-08 | J_I,J_log | absent | flow語とdivergence。transport unit未指定 |
| UNIT-09 | Phi,grad Phi,K | absent | potential/kernel/normの単位・正規化未指定 |
| UNIT-10 | C_ij,C_f,C_s,Delta C | unresolved | closure/boundsあり。upstreamの無次元規約をlocalへ自動継承しない |
| UNIT-11 | sigma,sigma_drive | absent | source slot/component、測定単位未指定 |
| UNIT-12 | kappa,D,mu_I | absent | scale/diffusion/mobilityの名称だけから単位を固定しない |
| UNIT-13 | a,Delta,Gamma,kappa_B,C_*,C_max | unresolved | old PDE係数群、local dimension tableなし |
| UNIT-14 | A_i,m_i,T_i,Delta v_i | implicit | JA weight/local load/minimal approximation、正規化・単位なし |
| UNIT-15 | C(t),cal F,rho_s | unresolved | JA opening/log-density。closure Cのunitと同一視しない |
| UNIT-16 | window min/max | absent | numerical thresholds / units未指定 |
| UNIT-17 | t and CT tau→infinity | implicit | time/orderの用途。source間calibration未指定 |

17 entries。主status内訳: absent 8、implicit 4、ratio-defined 2、unresolved 3。explicit units、明示dimensionless、明示normalizedに分類した行は0。これはdimensionの整合判定ではなく記載状態のみであり、inconsistent-lookingという判定も今回は付けない。

## 8. Fast / slow formal inventory

| FS-FORM-ID | Formal object / condition | Equation/source | Signature | Necessary? sufficient? source wording | Neural map present? | Phenomenal map present? |
| --- | --- | --- | --- | --- | --- | --- |
| FS-FORM-01 | v_f | S04/S07; CON-SYM-005 | rate未固定 | fast predictive/reactive layer | process vocabulary、typed map未指定 | 単独では意識を定義しないと記述 |
| FS-FORM-02 | v_s | S04/S07; CON-SYM-006 | rate未固定 | slow sedimentary layer | 同上 | 単独では定義しない |
| FS-FORM-03 | Delta v=v_f-v_s | EQ-001/074 | difference | source-local definition | rate measurement未指定 | gap自体と意識を区別 |
| FS-FORM-04 | Delta v not zero | EQ-002/075 | condition | “at least ... necessary” S04 | brain-local reading | window conditionという文章接続 |
| FS-FORM-05 | absolute gap finite upper bound | EQ-034/111 | interval | region satisfying conditions | scale未指定 | conscious-state window |
| FS-FORM-06 | synchrony limit | EQ-013/089; S04 | limit | boundary disappearsとの記述 | process interpretation | opening消失という接続 |
| FS-FORM-07 | dissociation / too-large gap | EQ-056/145; S16 | qualitative limit | reference fragments | map未指定 | fragmentation reading |
| FS-FORM-08 | coupling mu>0 | EQ-025/102 | inequality | gap alone does not establish state | no typed carrier | coupling condition |
| FS-FORM-09 | mu finite interval | EQ-035/112 | bounds | window component | threshold未指定 | fixation/fragmentationとの接続 |
| FS-FORM-10 | tau proportional to gap/mu | EQ-003/076 | proportionality | internal buffer | neural calibration未指定 | subjective time itselfではない |
| FS-FORM-11 | tau finite interval | EQ-027/104 | bounds | stability windowと命名 | values未指定 | conscious state intermediate region |
| FS-FORM-12 | T=kappa gap/mu | EQ-005/078 | index | will/consciousness strengthを否定 | mechanical identityではない | ego位置との文章対応 |
| FS-FORM-13 | T_Phi extension | EQ-008/084 | effective index | not generating consciousnessと明記 | map未指定 | referencing direction/strengthの記述 |
| FS-FORM-14 | T_Phi between bounds | EQ-037/114 | condition | window component | values未指定 | joint windowの文章 |
| FS-FORM-15 | Delta C counterpart | EQ-016–018/092–094 | difference/correspondence | same condition different coordinates | transformation未指定 | conscious/observation regime |
| FS-FORM-16 | nonzero gap/gradient/I change | EQ-038/115 | conjunction | minimal nonclosure conditions | measured variables未指定 | S07後半の条件 |
| FS-FORM-17 | JA C(t),local gaps | EQ-079–081/101/140 | indexed relations / function | access/openingとcollapseの文章 | local units未指定 | named opening functionあり、成功判定しない |

17 formal entries。Phase 00の10 claim familiesとは集計単位が違う。必要十分性のcolumnは**source wording**でありlogical-role verdictではない。

## 9. SSO formal inventory

S04の二つの展開を別objectとし、sourceが条件付きで“same structure can be read as”と接続する事実を残す。§6の3条件を§4の6条件の証明上の縮約とは扱わない。Phase 00の7 componentsも監査者のdocumentary decompositionであり第三の定義式ではない。

| SSO item | Local source object | S04 minimal conditions | S06 conditions | Phase00 component | Same object? / Source says? |
| --- | --- | --- | --- | --- | --- |
| SSO-01 | Speed-Scale Orchestration | 6条件の対象 | 3条件の対象 | 全体の読書用名称 | central-controlなしのtime-scale coordination |
| SSO-02 | Self-Sustaining Observer | stable temporal loopの読み | observerの独立条件集合なし | loopを含む読み | stable loop時のsame structureの別reading。subject追加を否定 |
| SSO-03 | S04 condition 1 | fast/slow exist | condition 1で前提 | fast + slow | 2 componentsと1条件、one-to-oneでない |
| SSO-04 | S04 condition 2 | finite speed difference | condition 1 | gap | finiteとexistsのwordingを保存 |
| SSO-05 | S04 condition 3 | not synchrony / not separation | condition 2、condition 3と関連 | gap/loop | 条件集合の等価式なし |
| SSO-06 | S04 condition 4 | partial plasticity gate | list内に明記なし | gate | S06でgate不要と推論しない |
| SSO-07 | S04 condition 5 | delay thickness retained | list内に明記なし | delay | omitted named condition |
| SSO-08 | S04 condition 6 | self-sustaining loop/no controller | list内に独立明記なし | loop | temporal-loop reading |
| SSO-09 | S06 condition 1 | conditions 1/2参照可能 | speed difference exists | fast/slow/gap | identity theoremではない |
| SSO-10 | S06 condition 2 | condition 3部分 | not completely separated | gap/loop | exact set equivalence未指定 |
| SSO-11 | S06 condition 3 | gate/loopと関連 | sedimentation not completely closed | gate/slow/loop | S04の一行に機械対応させない |
| SSO-12 | Phase00 fast component | condition 1 | condition 1 | fast | documentary component |
| SSO-13 | Phase00 slow component | condition 1/4 | condition 1/3 | slow | documentary component |
| SSO-14 | Phase00 gap component | conditions 2/3 | conditions 1/2 | gap | documentary component |
| SSO-15 | Phase00 gate component | condition 4 | list外の本文 | gate | documentary component |
| SSO-16 | Phase00 viscosity component | local S04 formula、6条件で独立列記なし | 3条件で独立列記なし | mu | component countとcondition countは別 |
| SSO-17 | Phase00 delay component | condition 5 | list外 | tau | documentary component |
| SSO-18 | Phase00 loop component | condition 6 | continuing referencing relation | loop | documentary component |

18 items = 展開名2 + S04条件6 + S06条件3 + Phase00 components7。S04末は“structure itself is not yet consciousness / without ... cannot obtain”、S06は3条件の後“Here the conscious state ... obtains”。両文言を保存し、role/necessity/sufficiencyの後続照合へ渡す。

## 10. TCA inventory

| CON-TCA | Object | Exact definition/form / source | Relation inventory |
| --- | --- | --- | --- |
| CON-TCA-01 | Torque Converter Attention | S05:23、異なる速度を単一速度へ潰さず接続するintermediate mechanism | source-local mechanism名称、判定は後phase |
| CON-TCA-02 | mechanical torque converter analogy | S05 Structural Analogy | angular velocity/fluid slipの説明。neural機械同等式は提示されない |
| CON-TCA-03 | mathcal T | EQ-005/078、scale factor kappa | effective structural index、will/agency/意識強度ではない |
| CON-TCA-04 | T_Phi | EQ-008/084 | gradientを含むextension、Tとの同一quantity宣言ではない |
| CON-TCA-05 | tau relation | EQ-006/082 | shared ratioだがTと異なるaspectとS03が明記 |
| CON-TCA-06 | JA T_i,A_i,m_i | EQ-079–081 | attention-weight/local approximation。EN式に統合しない |
| CON-TCA-07 | ego position | S05 From Attention to Ego | “corresponds to the position experienced as the ego”、subjectとは区別 |
| CON-TCA-08 | IFGT/VED/CT coupler | S05末、S06 Coupler、CT token quote | VED-type transmission / IFGT-type direction / CT spatial-axis correspondenceというsource claims |

## 11. Consciousness-window inventory

| WIN-ID | Condition | Mathematical form (source quotation) | Source | Status wording | Related figure |
| --- | --- | --- | --- | --- | --- |
| WIN-01 | minimal nonsynchrony | `Delta v != 0` | EQ-002/075 | necessaryという文章 | FIG-01/06 |
| WIN-02 | speed gap range | `0 < abs(Delta v) < Delta v_max` | EQ-034/111 | region satisfying conditions | FIG-01/06 |
| WIN-03 | viscosity positivity | `mu > 0` | EQ-025/102 | coupling condition | FIG-02/03 |
| WIN-04 | viscosity finite range | `mu_min < mu < mu_max` | EQ-035/112 | component of window | FIG-01/03 |
| WIN-05 | delay finite range | `tau_min < tau < tau_max` | EQ-027/104 | consciousness stability window | FIG-01 |
| WIN-06 | effective index range | `T_min < T_Phi < T_max` | EQ-037/114 | bounds name T, object T_Phi | FIG-02の式にboundsはなし |
| WIN-07 | nonzero gradient | `grad Phi != 0` | EQ-038/115内 | minimal nonclosure | FIG-04 |
| WIN-08 | density change | `partial I/partial t != 0` | EQ-038/115内 | conjunction | FIG-04ではPhi changeを表示 |
| WIN-09 | closure difference | `0 < Delta C < Delta C_max` | EQ-018/094 | observation/consciousness regime | FIG-06 |
| WIN-10 | synchrony boundary | `Delta v -> 0` | EQ-013/089、JA140 | collapse；JA C(t) implicationあり | FIG-03/06 |
| WIN-11 | dissociation boundary | `abs(Delta v)` too large | EQ-056/145、JA167 | disconnected referencing | FIG-03/06 |
| WIN-12 | fixation boundary | `mu -> 0` | EQ-057/146、JA168 | adhesion / fixed meaning well | FIG-03 |
| WIN-13 | fragmentation boundary | `mu -> infinity` | EQ-058/147、JA169 | slip / failed sedimentation | FIG-03 |
| WIN-14 | delay violations | `tau < tau_min` / `tau > tau_max` | JA152/153、S15 EN inline | immediate reaction / correspondence breaks | FIG-01 prose |
| WIN-15 | gradient weak/strong limits | `abs(grad Phi) -> 0` / infinity | JA170/171、S16 EN inline | fading direction / over-fixation | FIG-04 qualitative |
| WIN-16 | phase diagram lower bound | `Delta v_min < abs(Delta v) < Delta v_max` | FIG-03 EN/JA | diagram-bound, minと0の関係未指定 | FIG-03 |
| WIN-17 | named tuple membership | `(Delta v,mu,tau,T_Phi,grad Phi) in consciousness window` | EQ-067/161 | schematic region名、typed set未指定 | FIG-03は2-axis projection |

本表17条件family。S07のjoint statementは保存するが、全節・図の条件を追加でAND結合した新しい必要十分条件は作らない。境界・thresholdの数値、parameter provenance、空間/temporal integration kernelはsource未固定として残す。

## 12. Closure-family inventory

| Object | Source-local definition | Upstream analogue | Same glyph? | Same coordinate system? | Source identity claim? |
| --- | --- | --- | --- | --- | --- |
| CL-01 C_ij | S06 node-pair closure degree、EQ-015/091 | Vol.1 causal-log entry | YES | node pairだがquantity description差 | VED definitionとの出自表示 |
| CL-02 C field | old PDE、EQ-019/095 | IFGT C(x,tau) | YES | t vs tau、localarguments省略 | older VEDと呼ぶ |
| CL-03 C_f | fast layer effective closure degree | C_ij/field vocabulary | derived glyph | aggregation map未指定 | effectiveというlocal definition |
| CL-04 C_s | slow layer effective closure degree | 同上 | derived glyph | aggregation map未指定 | fastより高い傾向という文章 |
| CL-05 Delta C | C_s-C_f | closure difference | local | layer-level | definitionは明示 |
| CL-06 Delta v | v_f-v_s | Delta C counterpart | NO | “different coordinates” | same conditionとのsource claim、transform式なし |
| CL-07 C(t) | JA conscious access/opening | 上記closure Cとの式対応なし | same C | local conscious-function argument | same glyphをidentityにしない |
| CL-08 C_max / C_* | old PDE saturation boundary/scale | IFGT upper boundary/scale | YES | numeric adoptionは未指定 | C_max=1を本稿へ補わない |

8 objects。`C_ij ->1/0`、`Delta C=0`、`Delta C->Delta C_max`はS06 inlineにも存在し、表示式件数とは別に記録。sourceはnonidentity/projected usesとsame condition/quantityの両方を使用する。これらを整合化する新しい変換は導入しない。

## 13. Older VED PDE inventory

対象は**CON-EQ-019 / CON-EQ-095**（2出現、式形1）。exact raw blockは§2。EN [formal_mapping](../../consciousness/sections/formal_mapping.tex):301、JA [formal_mapping_ja](../../consciousness/sections_ja/formal_mapping_ja.tex):245。source labelは“older VED non-closure persistence condition”、直後に“phenomenological, coarse-grained approximation”、第三項に“revised Vol.4 interpretation”、後に“VED-grounded basis”。引用全体のrole/validityは判定しない。

| Locator | 現物照合 | Source/signature difference |
| --- | --- | --- |
| [IFGT unified_equation](../../Information-Field-Geometry-Theory/sections/unified_equation.tex), `eq:unified` | 同じthree-term RHSとC-current balanceのtau-formを所在確認 | primary derivativeはtau。Consciousnessはt。係数群を新たに同定しない |
| 同file `eq:unified_external` | effective t-formを別表示 | RHSはellipsis。Consciousnessのfull t-formとraw exact matchではない |
| 同file `eq:J_C` | current constructionを上流が別途記述 | ConsciousnessはJ_C constitutive formulaをその場で再掲しない |
| [VED inventory IFG-07](../ved_equation_audit/01_equation_inventory_v0.1_ja.md):183 | IFGT related-branch equationとして記録されている | current VED core equationへの自動編入ではない |
| [VED final RC-038](../ved_equation_audit/06_final_audit_record_v1.0_ja.md):123 | internal IFGT scopeのauthorityが存在 | 既存dispositionを変更せず、SSO self-maintenanceへの認定を継承しない |

Phase00 CON-U-003のexact **current analogue**は上記まで固定できる。一方「older VED」が意図する歴史version / Vol.4の同一PDE locatorは確定しない。current Vol.4のbarrier interpretationを、このfull PDEの出自と同じものにしない。Consciousnessは駆動項をfast→slow、散逸を過剰closure抑制、barrierをeffective resistanceと読む。これはsourceのinterpretation差のinventoryであって導出成否ではない。

Current [Vol.4 dynamic_barrier](../../paper/vol4/sections/dynamic_barrier.tex):6–14は旧barrierをB(L)のlog potentialとして引用する。Consciousnessのfull C-field PDEと同じ表示式ではなく、Vol.4への参照はbarrier解釈のlocatorとして保持する。

node-pair式は別件。[Vol.1 causal_logs_time](../../paper/vol1/sections/causal_logs_time.tex) `eq:Cij`とCON-EQ-015/091を照合。式形に対応があるが、Vol.1のC_ij=causal log、rho_i=log density、H_ij=accumulated causal historyという用語と、Consciousnessのclosure degree / difference density / connection strengthを分けて保存する。

## 14. IFGT template inventory

| IFGT object | Current IFGT form | Consciousness form | Same glyph? | Same signature? | Explicit translation? |
| --- | --- | --- | --- | --- | --- |
| IF-TPL-01 I | traces; I=f(1-C) | re-referenceable slow logs | YES | field-like、local args省略 | projected-window interpretation、typed map未固定 |
| IF-TPL-02 time | informational tau | external t in template; local delay tau | mixed | ordering vs derivative/buffer | no local time-conversion function |
| IF-TPL-03 balance | partial_tau I + div J = sigma | partial_t I + div J_I = sigma | time/current glyph差 | analogous slots、parameter差 | equation reuseというsource表示 |
| IF-TPL-04 flow | J=-D grad I+mu F_I | J_I=-D grad I+mu_I F | glyphswapあり | coefficient/force names別 | source-specific signatureとして保存 |
| IF-TPL-05 local flow | general vector J | J_log / J_mathrmlog | NO | local referencing vs general flow | prose effective-coordinate関係のみ |
| IF-TPL-06 force | F_I=-grad Phi=alpha grad C | F=-grad Phi | F/F_I別 | latter portion omitted | general/cognitive field直接同定を否定 |
| IF-TPL-07 potential | Phi=-alpha C+Phi_0 | Phi=K*I | Phi同じ、functional form別 | local kernel signature未固定 | current IFGT fundamentalにK*Iのexact locatorは未固定 |
| IF-TPL-08 kernel via CT | [CT formal_mapping](../../conceptual-topography/sections/formal_mapping.tex) eq:Phi_primary: Phi(x,tau)=(K*I)(x,tau) | Phi=K*I | YES | arguments省略 | **CTのexact analogue所在**とIFGT source labelを分離 |
| IF-TPL-09 sigma | mismatch source / drive-dissipation-barrier construction | generation-dissipation slot | YES | term decompositionをlocalで固定しない | same biological processとは推定しない |
| IF-TPL-10 closure PDE | tau-form unified / effective t-form | full t-form “older VED” | C/J_C等共通 | source-version difference | §13。equivalence未認定 |

10 correspondence entries。[IFGT fundamental_dynamics](../../Information-Field-Geometry-Theory/sections/fundamental_dynamics.tex)、[unified_equation](../../Information-Field-Geometry-Theory/sections/unified_equation.tex)を現物照合。CTのtokenは[CT core equations](../../conceptual-topography/sections/core_equations.tex)のtoken couplingと比較するが、local ell_iのcarrierを他式へ転記しない。upstreamに存在するtyped operatorを、Consciousnessの省略された引数の補完として採用しない。

## 15. Phenomenal-object inventory

| PH-OBJ-ID | Term | Formal object? | Functional object? | Phenomenal object? | Source definition | Same as another term? source claim |
| --- | --- | --- | --- | --- | --- | --- |
| PH-OBJ-01 | consciousness | no single conserved/additive scalarとS07 | log referencing | YESとして記述 | S00/S06/S07 | not I/J/Phi themselves |
| PH-OBJ-02 | conscious state | window/regimeの式 | current processing connects logs | YES | S07/S08 | regime/windowとの文章接続 |
| PH-OBJ-03 | conscious regime | named region | finite referencing conditions | YES | S07/S16 | typed state-space setは未指定 |
| PH-OBJ-04 | opening | JA C(t),その他prose | access boundary opens | YES | S07 JA/S12 | sourceによるconsciousness reading |
| PH-OBJ-05 | qualia | dedicated scalarなし | passage before sedimentation | YES | S11 | frontierのlive foreground、consciousness自体と区別 |
| PH-OBJ-06 | phenomenal surface | prose | boundary becoming experienceable | YES | S08/S11 | not a stored representation |
| PH-OBJ-07 | sedimentation frontier | no geometric signature | passing into slow logs | phenomenal boundary | S11/FIG-05 | live qualiaとsource同定 |
| PH-OBJ-08 | gate | no operator signature | partial passage/plasticity | condition for access | S04/S06 | gateそのものをqualiaとする式なし |
| PH-OBJ-09 | explicit consciousness | no scalar | report / referencing own response | YES | S09/S10 | report requirementを述べる |
| PH-OBJ-10 | conscious access | window; JA C(t) | present↔past referencing | access-to-phenomenal wording | S04/S07/FIG-03 | EN figure conscious access / JA 意識 |
| PH-OBJ-11 | reportability | no typed reporting map | reportable trace | experienceと区別/接続 | S09/S10/S13 | residueがreportable |
| PH-OBJ-12 | subjective experience | formal signatureなし | integration等の読解対象 | YES | S11/S18 | tau自体とは区別 |
| PH-OBJ-13 | ego | effective position、no coordinate map | temporal transformation point | experienced as ego | S05 | subject/cause/command centerを否定 |
| PH-OBJ-14 | self | landscape terrain | sedimented personal history | re-referenceされるself | S12 | egoのpositionと別説明 |
| PH-OBJ-15 | observer | stable referencing loop reading | own-log updating | subject追加ではない | S04/S18 | Self-Sustaining Observerの名 |
| PH-OBJ-16 | non-closure as consciousness | JA text-only EQ-121 | continuing reference condition | source identification wording | JA S08 | ENのstate/regime wordingとの差を保存 |

16 families。正式な数値signature、functional description、phenomenal referenceの有無を別列にした。phenomenal bridgeの成功/失敗を評価する表ではない。

## 16. Self / ego / observer split

| SELF-OBJ-ID | Term | Source | Local role | Formal status | Phenomenal status | Identity claims |
| --- | --- | --- | --- | --- | --- | --- |
| SELF-OBJ-01 | ego | S05 From Attention to Ego | transformation position | no coordinate definition | position experienced as ego | TCA correspondence、subjectではない |
| SELF-OBJ-02 | self | S12 Consciousness and Self | terrain/history arrangement | potential analogy | self is referenced | ego-positionとterrainを分離 |
| SELF-OBJ-03 | self-model | S18 theory comparisons | model/theory vocabulary | own typed self-model operatorなし | comparison context | egoと同一とは推定しない |
| SELF-OBJ-04 | observer | S04/S18 | own logsを参照する構造 | loop prose | no additional subject | observer-like character |
| SELF-OBJ-05 | Self-Sustaining Observer | S04 subsection | stable-loop reading of SSO | conditions→reading | subjectではないと記述 | Speed-Scale Orchestrationとのconditional naming |
| SELF-OBJ-06 | subject | S05/S04 | central causeとしての読みを否定 | independent variableなし | discussed / negated identification | ego is not a subject |
| SELF-OBJ-07 | reportable self | S09/S10自己応答報告の文脈 | own responseを参照・報告 | この名の独立formal objectは未所在 | explicit consciousnessとの接続 | named identity未固定 |
| SELF-OBJ-08 | narrative / sedimented terrain | S08/S09 narrative logs、S12 self terrain | history/log organization | Phi analogy、専用signatureなし | self-readingの背景 | “narrative terrain”という独立定義は未固定。narrative logsとself terrainを自動統合しない |

## 17. Access / report / qualia split

| ACC-ID | Object | Source | Other object | Relation stated | Exact signature / identity status |
| --- | --- | --- | --- | --- | --- |
| ACC-01 | conscious access | S04/S07 | referencing window | condition/opening | named region、scalarと決めない |
| ACC-02 | reportability | S09/S10 | referencing own response | explicit consciousnessへのrequirement | sourceのnecessary wording、十分性を補わない |
| ACC-03 | explicit consciousness | S09/S10 | report | report可能性との文章接続 | qualiaと同一measureではない |
| ACC-04 | introspection | S13 | live boundary→log | measurement/secondary sedimentation | 対象を変えるというsource description |
| ACC-05 | qualia | S11 | consciousness / residue | qualia not consciousness itself、not stored residue | dedicated map未固定 |
| ACC-06 | live foreground | S11/FIG-05 | sedimentation frontier | qualiaのlocal naming | source claims boundary identity、監査認定なし |
| ACC-07 | residue | S11/S13/FIG-05 | qualia→measurement | transformed / distinct | stored residue ≠ qualia itself |
| ACC-08 | measurement result | S13 | residue/report | stabilized trace | original live foregroundとのidentityは否定的記述 |

## 18. Time-object inventory

| TIME-ID | Object | Exact form / source | Signature | Source-local identity boundary |
| --- | --- | --- | --- | --- |
| TIME-01 | external t | S03/S06, partial_t I | derivative parameter | IFGT informational tauへ自動変換しない |
| TIME-02 | internal tau | EQ-003/076 | proportional delay / buffer | torqueではない、subjective time itselfでもない |
| TIME-03 | v_f | S04/S07 | fast rate、numerical definition未指定 | frequency/neural speedの単位未固定 |
| TIME-04 | v_s | S04/S07 | slow rate | retention density rho_sと同一ではない |
| TIME-05 | Delta v | EQ-001/074 | signed difference、windowではabsolute value | speed/time differenceという語の変化を保存 |
| TIME-06 | integration/window thickness | S04/S07 tau range | interval、kernelは未指定 | window≠experienced time |
| TIME-07 | six-step referencing order | S09 numbered six steps / FIG-04 | sequence, no timestep | processing→gate→sedimentation→gradient→bias→loop |
| TIME-08 | preparation→report order | EQ-046/128、S10 | schematic time sequence | biological causal lawとして新規認定しない |
| TIME-09 | CT long-time tau | S09 quote `Phi -> Phi*` as tau→infinity | limiting parameter | SSO delayと同じclock mapはなし |
| TIME-10 | experienced time | S03/S04/S18 | no own formal time variable | tauと直接同一ではない |
| TIME-11 | JA reference-duration tau | JA S07:50 / EQ-101 | third argument of cal F | buffer/timescaleのlocal use、Bio progressionと分離 |

11 objects。section順、説明順、dependency順、formal derivation順、biological generation順、phenomenal emergence順を同一視しない。sourceの六段階やpreparation→reportは**sourceが示す順序**としてのみ保持する。

## 19. Projection inventory

| PROJ-ID | Object / usage | Source | Source definition | Signature / domain | Cross-identity status |
| --- | --- | --- | --- | --- | --- |
| PROJ-01 | projection / mass assignment | S06 Projection as Fourth IFGT Primitive | specific state/representation acquires disproportionate influence | prose operation; typed map未指定 | 本稿のlocal definitionとupstream出自を分離 |
| PROJ-02 | projected uses | S06 methodological stance | different observation windows/effective coordinates | method, not same operator | Intelligenceとのstance reuse |
| PROJ-03 | physical biasing / biological prioritization / artificial weighting | S06 definition bullets | nonintentional instancesを含める | carrier-domain translation未固定 | one labelへのsource inclusion、同じmechanismと認定しない |
| PROJ-04 | attention selection | S05/S06 | prioritized log strengthening | formal weighting vs temporal TCA descriptions | JA A_i relationとgeneral projectionのsame-map式なし |
| PROJ-05 | plasticity gate | S04/S06 | partial passing of fast activity | gate kernel/range未指定 | projection instanceとsourceが呼ぶ |
| PROJ-06 | Phi→J direction | S06 | global bias localizes onto specific state | gradient/effective-index usage | general mapと同一operatorに統合しない |
| PROJ-07 | phenomenal residue selection / asymmetric report | S06/S10/S13 | qualia residue, split-brain referencing asymmetry | cognitive/phenomenal description | projection operationsというsource inclusion |
| PROJ-08 | downstream stopping / psychological projection contrast | S06 disclaimer; Phase00 DOWN-07–10 | unequal influenceをIntelligenceが再利用、psychological attributionと区別 | downstream operator独自signature | formal map/cognitive/biological/phenomenalを同一mapにしない |

## 20. Figure-symbol inventory

図は6families / EN・JA各6 PDF。FIG-番号はPhase00 file familyで、paper figure順は1,2,4,5,6,3。**図内symbol/relation/region-labelのfamily単位**で登録し、同じglyphの図中反復は同じ行内に含める。bodyの178 displaysとは別集計。source図PDFのtextとFIG-03/06のrenderを照合した。図版の英日文字列を字面で同じにする操作は行わない。

| FIG-SYM-ID | Figure | Symbol / relation / region label | Body counterpart | Exact match? | Figure-only? |
| --- | --- | --- | --- | --- | --- |
| FIG-SYM-001 | FIG-01 EN/JA | fast layer; v_f; high-frequency prediction/reaction/forward dynamics | S04 fast definition | glyph matches | NO |
| FIG-SYM-002 | FIG-01 EN/JA | slow layer; v_s; low-frequency memory/sedimentation/logs | S04 slow definition | glyph matches | NO |
| FIG-SYM-003 | FIG-01 EN/JA | Delta v=v_f-v_s; finite speed difference | EQ-001/074 | formula matches | NO |
| FIG-SYM-004 | FIG-01 EN/JA | tau proportional to gap/mu EN; tau ~ gap/mu JA | EQ-003/076 | JA symbol variant | NO |
| FIG-SYM-005 | FIG-01 EN/JA | mu; coupling viscosity | S03/S04 | matches | NO |
| FIG-SYM-006 | FIG-01 EN/JA | conscious access / 意識的アクセス; cross-scale log-reference boundary | S04 caption | named-object prose counterpart | NO |
| FIG-SYM-007 | FIG-01 EN/JA | dense updates / sparse stabilization | S04 fast/slow | qualitative density labels; no density formula | figure labels |
| FIG-SYM-008 | FIG-01 EN/JA | selected fast dynamics sediment into slow logs; connecting arrows | S04 plasticity gate | partial passage prose | NO |
| FIG-SYM-009 | FIG-01 EN/JA | neither complete synchrony nor complete separation | S04 conditions | matches wording | NO |
| FIG-SYM-010 | FIG-01 EN/JA | 0 < abs(Delta v) < Delta v_max | EQ-034/111 | matches | NO |
| FIG-SYM-011 | FIG-01 EN/JA | mu_min < mu < mu_max | EQ-035/112 | matches | NO |
| FIG-SYM-012 | FIG-01 EN/JA | tau_min < tau < tau_max | EQ-027/104 | matches | NO |
| FIG-SYM-013 | FIG-02 EN/JA | fast v_f / slow v_s boxes; high/low-frequency labels | S05 | matches | NO |
| FIG-SYM-014 | FIG-02 EN/JA | log feedback: logs → grad Phi → prediction | S05/S09 | prose/sequence counterpart | NO |
| FIG-SYM-015 | FIG-02 EN/JA | TCA; viscous temporal coupling chamber; rotation arrows | S05 analogy | conceptual diagram, no angular coordinate | diagram representation |
| FIG-SYM-016 | FIG-02 EN/JA | mu slip/viscosity; tau delay; T effective torque | S03/S05 | glyph matches | NO |
| FIG-SYM-017 | FIG-02 EN/JA | Delta v=v_f-v_s; speed difference enters | EQ-004/077 | matches | NO |
| FIG-SYM-018 | FIG-02 EN/JA | transformed without eliminating Delta v; difference preserved | S05 | wording counterpart | NO |
| FIG-SYM-019 | FIG-02 EN/JA | grad Phi; semantic potential gradient | S05/S06 | glyph matches | NO |
| FIG-SYM-020 | FIG-02 EN/JA | T=kappa Delta v/mu | EQ-005/078 | matches | NO |
| FIG-SYM-021 | FIG-02 EN/JA | T_Phi ~ kappa(Delta v/mu) abs(grad Phi) | EQ-008/084 | matches modulo typography | NO |
| FIG-SYM-022 | FIG-03 EN/JA | x-axis abs(Delta v); 0/small/large; y-axis mu; low/high | S07 window | two-axis diagram, no exact coordinate scale | axes |
| FIG-SYM-023 | FIG-03 EN/JA | Delta v_min, Delta v_max dashed bounds | WIN-02/16 | body lower bound 0; figure min unspecified | lower-bound glyph figure-only |
| FIG-SYM-024 | FIG-03 EN/JA | mu_min, mu_max dashed bounds | WIN-04 | matches | NO |
| FIG-SYM-025 | FIG-03 EN/JA | Delta v_min < abs(Delta v) < Delta v_max | WIN-16 | different lower-bound glyph from body | figure-specific form |
| FIG-SYM-026 | FIG-03 EN/JA | mu_min < mu < mu_max | EQ-035/112 | matches | NO |
| FIG-SYM-027 | FIG-03 EN/JA | non-closure window; EN conscious access / JA 意識; stable log referencing | S07/S08 | named-object wording variant | NO |
| FIG-SYM-028 | FIG-03 EN/JA | synchrony collapse; Delta v→0; automation/no boundary; left arrow | S16 | limit matches | NO |
| FIG-SYM-029 | FIG-03 EN/JA | dissociation; abs(Delta v) too large; fragmented referencing; right arrow | S16 | qualitative limit matches | NO |
| FIG-SYM-030 | FIG-03 EN/JA | fragmentation; mu→infinity; excess slip/sedimentation failure; upward arrow | S16 | limit matches | NO |
| FIG-SYM-031 | FIG-03 EN/JA | fixation; mu→0; adhesion/meaning-well lock-in; downward arrow | S16 | limit matches | NO |
| FIG-SYM-032 | FIG-03 EN/JA | finite phase region / inside-outside failure language | S07/S16 | prose, no new formal state-space set | NO |
| FIG-SYM-033 | FIG-04 EN/JA | non-closure gap; not fully closed; open dashed loop | S09 | open-loop description | representation |
| FIG-SYM-034 | FIG-04 EN/JA | non-closure loop; fast/slow mutually referenceable | S09 | prose matches | NO |
| FIG-SYM-035 | FIG-04 EN/JA | Delta v,mu,tau,Phi,grad Phi parameter list | S09/EQ-039 | body also has T_Phi in other summary | list is not full identity |
| FIG-SYM-036 | FIG-04 EN/JA | fast layer prediction/reaction/action candidates | S09 step1 | label matches | NO |
| FIG-SYM-037 | FIG-04 EN/JA | Plasticity Gate; partial passage; tau,mu | S09 step2 | prose matches | NO |
| FIG-SYM-038 | FIG-04 EN/JA | slow layer; sedimentation/memory stabilization | S09 step3 | prose matches | NO |
| FIG-SYM-039 | FIG-04 EN/JA | Phi updated; I changes → meaning field shifts | S09 steps3/4 | qualitative relation | NO |
| FIG-SYM-040 | FIG-04 EN/JA | partial Phi/partial t !=0 | S06 lists Phi change; core EQ-038/115 uses I change | derivative variable differs from core nonzero condition | figure nonzero Phi form |
| FIG-SYM-041 | FIG-04 EN/JA | grad Phi bias; referencing/prediction direction | S09 steps4/5 | prose matches | NO |
| FIG-SYM-042 | FIG-04 EN/JA | Delta v drives entry; selected traces sediment; density I changes; gradient biases next prediction | S09 | arrow labels, JA mixed English residual retained | NO |
| FIG-SYM-043 | FIG-04 EN/JA | Fast → Gate → Slow → I/Phi update → gradient bias → Fast | S09 six steps | schematic cycle not time-step equation | NO |
| FIG-SYM-044 | FIG-05 EN/JA | fast layer; volatile predictive flow/non-retained microstates | S11 | prose matches | NO |
| FIG-SYM-045 | FIG-05 EN/JA | Qualia live; transient boundary; not yet sedimented/stored | S11 | phenomenal local naming | NO |
| FIG-SYM-046 | FIG-05 EN/JA | approaching sedimentation / residue formation; downward progression | S11 | schematic transformation | NO |
| FIG-SYM-047 | FIG-05 EN/JA | slow layer; sedimented log structure | S11 | prose matches | NO |
| FIG-SYM-048 | FIG-05 EN/JA | stored residue != qualia itself | S11/S13 | distinction matches | NO |
| FIG-SYM-049 | FIG-05 EN/JA | reportable traces / labels / memory fragments | S11/S13 | prose matches | NO |
| FIG-SYM-050 | FIG-05 EN/JA | Measurement; stabilization/report; collapses live boundary | S13 | wording/arrow, not data map | NO |
| FIG-SYM-051 | FIG-05 EN/JA | qualia live → sedimented residue; converts arrow | EQ-049/131 | schematic counterpart | NO |
| FIG-SYM-052 | FIG-05 EN/JA | not retained as qualia; fast flow / slow residue side labels | S11 | semantic labels; no hidden field | NO |
| FIG-SYM-053 | FIG-06 EN/JA | SSO description / VED description | S06 | source windows | NO |
| FIG-SYM-054 | FIG-06 EN/JA | fast v_f / fast closure C_f; slow v_s / slow closure C_s | S06 | counterpart claims, not same glyph | NO |
| FIG-SYM-055 | FIG-06 EN/JA | high/volatile/predictive vs low/nonclosure-prone; low/sedimentary/stabilizing vs high/closure-prone | S06 | qualitative comparison | NO |
| FIG-SYM-056 | FIG-06 EN/JA | Delta v=v_f-v_s; SSO asymmetry | EQ-001/074 | matches | NO |
| FIG-SYM-057 | FIG-06 EN/JA | Delta C=C_s-C_f; VED asymmetry | EQ-016/092 | matches | NO |
| FIG-SYM-058 | FIG-06 EN/JA | structural equivalence ⇔; same condition/two descriptions; neither grounds other; cyclic/dashed matching arrows | EQ-017/093, S06 caption | correspondence and equivalence prose, no transform function | NO |
| FIG-SYM-059 | FIG-06 EN/JA | consciousness window: 0 < abs(Delta v) < Delta v_max | EQ-034/111 | matches | NO |
| FIG-SYM-060 | FIG-06 EN/JA | observation regime: 0 < Delta C < Delta C_max | EQ-018/094 | matches | NO |
| FIG-SYM-061 | FIG-06 EN/JA | Delta v→0 ⇔ Delta C→0; synchrony/closure | S06 prose limits | double-arrow form figure-local | figure relation form |
| FIG-SYM-062 | FIG-06 EN/JA | abs(Delta v) too large ⇔ Delta C→Delta C_max; rupture/disconnection | S06 prose | equivalence form figure-local | figure relation form |
| FIG-SYM-063 | FIG-06 EN/JA | JA fast-side 確率収束相; slow-side 古典相 | no exact named body counterpart located | JA-ONLY labels | YES |
| FIG-SYM-064 | FIG-06 EN/JA | footer: structural correspondence/not causal identity; corresponding observation regime | S06 caption/projected uses | EN explicit causal-identity qualifier vs JA shorter footer | wording variant |

重要な差は、FIG-01 JAのdelay式が`tau ~ Delta v / mu`、EN/bodyがproportionality、FIG-03の下限がDelta v_min（bodyは0）、FIG-03 EN conscious access / JA 意識、FIG-04のPhi time-changeとcoreのI time-change、FIG-06 JAのみの「確率収束相」「古典相」。等号・矢印・phase名をsource同一性の証明として用いない。

## 21. EN / JA equation parity

EXACTは**数式token列一致（改行/空白のみ除外）**であってbyte一致ではない。raw blockのbyte hashは独立に保持した。添字brace/TeX spacingの差および1display→4displaysの再配置をTYPOGRAPHICに記録した。非自明な数学的同値変形は行っていない。

| EN display | JA counterpart displays | Parity |
| --- | --- | --- |
| CON-EQ-001 | CON-EQ-074 | EXACT |
| CON-EQ-002 | CON-EQ-075 | EXACT |
| CON-EQ-003 | CON-EQ-076 | EXACT |
| CON-EQ-004 | CON-EQ-077 | EXACT |
| CON-EQ-005 | CON-EQ-078 | EXACT |
| CON-EQ-006 | CON-EQ-082 | EXACT |
| CON-EQ-007 | CON-EQ-083 | MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE |
| CON-EQ-008 | CON-EQ-084 | EXACT |
| CON-EQ-009 | CON-EQ-085 | EXACT |
| CON-EQ-010 | CON-EQ-086 | EXACT |
| CON-EQ-011 | CON-EQ-087 | EXACT |
| CON-EQ-012 | CON-EQ-088 | EXACT |
| CON-EQ-013 | CON-EQ-089 | EXACT |
| CON-EQ-014 | CON-EQ-090 | EXACT |
| CON-EQ-015 | CON-EQ-091 | EXACT |
| CON-EQ-016 | CON-EQ-092 | EXACT |
| CON-EQ-017 | CON-EQ-093 | EXACT |
| CON-EQ-018 | CON-EQ-094 | EXACT |
| CON-EQ-019 | CON-EQ-095 | EXACT |
| CON-EQ-020 | CON-EQ-096 | EXACT |
| CON-EQ-021 | CON-EQ-097 | EXACT |
| CON-EQ-022 | CON-EQ-098 | MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE |
| CON-EQ-023 | CON-EQ-099 | EXACT |
| CON-EQ-024 | CON-EQ-100 | EXACT |
| CON-EQ-025 | CON-EQ-102 | EXACT |
| CON-EQ-026 | CON-EQ-103 | EXACT |
| CON-EQ-027 | CON-EQ-104 | EXACT |
| CON-EQ-028 | CON-EQ-105 | EXACT |
| CON-EQ-029 | CON-EQ-106 | EXACT |
| CON-EQ-030 | CON-EQ-107 | EXACT |
| CON-EQ-031 | CON-EQ-108 | EXACT |
| CON-EQ-032 | CON-EQ-109 | EXACT |
| CON-EQ-033 | CON-EQ-110 | EXACT |
| CON-EQ-034 | CON-EQ-111 | EXACT |
| CON-EQ-035 | CON-EQ-112 | EXACT |
| CON-EQ-036 | CON-EQ-113 | EXACT |
| CON-EQ-037 | CON-EQ-114 | EXACT |
| CON-EQ-038 | CON-EQ-115 | EXACT |
| CON-EQ-039 | CON-EQ-116 | MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE |
| CON-EQ-040 | CON-EQ-122 | EXACT |
| CON-EQ-041 | CON-EQ-123 | EXACT |
| CON-EQ-042 | CON-EQ-124 | EXACT |
| CON-EQ-043 | CON-EQ-125 | EXACT |
| CON-EQ-044 | CON-EQ-126 | EXACT |
| CON-EQ-045 | CON-EQ-127 | EXACT |
| CON-EQ-046 | CON-EQ-128 | EXACT |
| CON-EQ-047 | CON-EQ-129 | EXACT |
| CON-EQ-048 | CON-EQ-130 | EXACT |
| CON-EQ-049 | CON-EQ-131 | EXACT |
| CON-EQ-050 | CON-EQ-132 | EXACT |
| CON-EQ-051 | CON-EQ-133 | EXACT |
| CON-EQ-052 | CON-EQ-134 | EXACT |
| CON-EQ-053 | CON-EQ-135 | EXACT |
| CON-EQ-054 | CON-EQ-136, CON-EQ-137, CON-EQ-138, CON-EQ-139 | MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE |
| CON-EQ-055 | CON-EQ-141, CON-EQ-142, CON-EQ-143, CON-EQ-144 | MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE |
| CON-EQ-056 | CON-EQ-145 | EXACT |
| CON-EQ-057 | CON-EQ-146 | EXACT |
| CON-EQ-058 | CON-EQ-147 | EXACT |
| CON-EQ-059 | CON-EQ-148 | EXACT |
| CON-EQ-060 | CON-EQ-149 | EXACT |
| CON-EQ-061 | CON-EQ-150 | EXACT |
| CON-EQ-062 | CON-EQ-151 | EXACT |
| CON-EQ-063 | CON-EQ-154 | EXACT |
| CON-EQ-064 | CON-EQ-155 | EXACT |
| CON-EQ-065 | CON-EQ-156 | EXACT |
| CON-EQ-066 | CON-EQ-157, CON-EQ-158, CON-EQ-159, CON-EQ-160 | MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE |
| CON-EQ-067 | CON-EQ-161 | EXACT |
| CON-EQ-068 | CON-EQ-173 | MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE |
| CON-EQ-069 | CON-EQ-174 | MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE |
| CON-EQ-070 | CON-EQ-175 | EXACT |
| CON-EQ-071 | CON-EQ-176 | EXACT |
| CON-EQ-072 | CON-EQ-177 | EXACT |
| CON-EQ-073 | CON-EQ-178 | EXACT |

| JA unmatched display | Source | Additional-display classification |
| --- | --- | --- |
| CON-EQ-079 | torque_converter_attention_ja.tex:116 | SOURCE-VERSION DIFFERENCE — JA-specific form/statement |
| CON-EQ-080 | torque_converter_attention_ja.tex:122 | SOURCE-VERSION DIFFERENCE — JA-specific form/statement |
| CON-EQ-081 | torque_converter_attention_ja.tex:128 | SOURCE-VERSION DIFFERENCE — JA-specific form/statement |
| CON-EQ-101 | core_equations_ja.tex:44 | SOURCE-VERSION DIFFERENCE — JA-specific form/statement |
| CON-EQ-117 | structural_interpretation_ja.tex:42 | JA-ONLY display — earlier bound reprise; EN prose |
| CON-EQ-118 | structural_interpretation_ja.tex:46 | JA-ONLY display — earlier bound reprise; EN prose |
| CON-EQ-119 | structural_interpretation_ja.tex:50 | JA-ONLY display — earlier bound reprise; EN prose |
| CON-EQ-120 | structural_interpretation_ja.tex:54 | JA-ONLY display — earlier bound reprise; EN prose |
| CON-EQ-121 | structural_interpretation_ja.tex:138 | SOURCE-VERSION DIFFERENCE — JA-specific form/statement |
| CON-EQ-140 | measurement_collapse_ja.tex:146 | SOURCE-VERSION DIFFERENCE — JA-specific form/statement |
| CON-EQ-152 | qualitative_predictions_ja.tex:94 | JA-ONLY display — counterpart is EN inline math |
| CON-EQ-153 | qualitative_predictions_ja.tex:102 | JA-ONLY display — counterpart is EN inline math |
| CON-EQ-162 | pathologies_limits_ja.tex:18 | JA-ONLY display — earlier bound reprise; EN prose |
| CON-EQ-163 | pathologies_limits_ja.tex:22 | JA-ONLY display — earlier bound reprise; EN prose |
| CON-EQ-164 | pathologies_limits_ja.tex:26 | JA-ONLY display — earlier bound reprise; EN prose |
| CON-EQ-165 | pathologies_limits_ja.tex:30 | JA-ONLY display — earlier bound reprise; EN prose |
| CON-EQ-166 | pathologies_limits_ja.tex:66 | JA-ONLY display — counterpart is EN inline math |
| CON-EQ-167 | pathologies_limits_ja.tex:90 | JA-ONLY display — counterpart is EN inline math |
| CON-EQ-168 | pathologies_limits_ja.tex:115 | JA-ONLY display — counterpart is EN inline math |
| CON-EQ-169 | pathologies_limits_ja.tex:141 | JA-ONLY display — counterpart is EN inline math |
| CON-EQ-170 | pathologies_limits_ja.tex:165 | JA-ONLY display — counterpart is EN inline math |
| CON-EQ-171 | pathologies_limits_ja.tex:189 | JA-ONLY display — counterpart is EN inline math |
| CON-EQ-172 | pathologies_limits_ja.tex:271 | JA-ONLY display — counterpart is EN inline math |

EN73対応groups = EXACT 65 + MATHEMATICALLY SAME / TYPOGRAPHIC DIFFERENCE 8。後者はsingle-display typography5 + four-bound split3。JA counterpartは82出現（65 + 5 + 12）。残るJA-ONLY display23 = EN inline対応9 + 同条件display再掲8 + source-version追加6。73+105=178、82+23=105。EN-ONLY 0、対になるdisplayの数学内容が異なるとして無理にpairにした行0。

六つのsource-version formはJA CON-EQ-079/080/081/101/121/140。これは「ENに対応displayがない」ことに加え、JAに固有のlocal式/statementとしてinventoryする。JAのopening functionとtext-only not-a-state statementを、ENのclosed-form-not-intended / state-regime wordingへ統合しない。windowやSSOの必要十分性をsource間で統一するのも本phaseの範囲外。

## 22. PDF spot-check

PDF skillを用いた。Popplerは所在しないため、既存pypdfで14 PDFs（main2+figure12）のpage/textを読み、Ghostscriptで**既存PDFを一時画像化**した。build/rebuild/figure生成はしない。text抽出だけでrenderを認定せず、window/closureの図を視認した。65dpiで小さい数式が不鮮明だったJA FIG-03は130dpiで再renderし、boundsが存在することを確認した。

| PDF / page (physical) | Spot-check | Inventory result |
| --- | --- | --- |
| [EN main](../../consciousness/main.pdf), 83 pages | core/template、old PDE、window、all section presenceを抽出textで照合 | key equationsのlocatorを確認。全ページ全式のrender認定ではない |
| [JA main](../../consciousness/main_ja.pdf), 97 pages | p13–14 A_i/T_i、p27 C(t)、p35 text-only nonclosure、p62 collapse implication | JA固有formのPDF存在をtext確認。p27をrender視認 |
| [EN figure3](../../consciousness/figures/figure3_nonclosure_window.pdf) / [JA figure3](../../consciousness/figures_ja/figure3_nonclosure_window_jp.pdf) | axes、min/max、4regimes、中央labelをrender | lower bound Delta v_minを両図で確認 |
| [EN figure6](../../consciousness/figures/figure6_observation_regime.pdf) / [JA figure6](../../consciousness/figures_ja/figure6_observation_regime_jp.pdf) | two descriptions/equivalence/windows/limitsをrender | JA-only phase labelsを確認、equivalenceの成否は未評価 |
| その他figure PDFs 8 | symbols/labels/arrowsをtext抽出しsource SVGと補助照合 | source/figure inventory、pixel provenanceの認定ではない |

PDF SHA-256: EN `1c0aa1b06a0323582ae20aef4bd95aa9ee297116742bccef9d66070835245ee3`、JA `dcadebf39d11013eabf3d936d396fb73fbc86be5c1028152b7c0e2244b0faed3`。Phase00と同じcurrent artifactsを読み、変更していない。一時抽出・render・hash資料は`${TEMP_EVIDENCE_ROOT}/consciousness_phase01.clDlrr/`に保持し、repoにhelperを追加しない。

## 23. Object authority hierarchy

| Family | Exact displayed definition | Prose definition | Figure definition | Analogy / borrowed / downstream | Conflict/identity treatment |
| --- | --- | --- | --- | --- | --- |
| gap/window | §2 raw definitions | S04/S07 minimal conditions | FIG-01/03/06 | Bio motivation、VED Delta C | min/0、signed/absolute gap、condition wordingを保持 |
| I/J/Phi | template expressions | effective/log window | FIG-04 | IFGT/CT/Bio glyphs | prose-local意味とupstream formは別authority |
| C family | C_ij / Delta C / old PDE / JA C(t) | closure / conscious access | FIG-06 | VED/IFGT reuse | scalar letterでmatrix/field/openingを統合しない |
| TCA | T / T_Phi / JA T_i | transmission index / ego | FIG-02 | mechanical analogy、CT token coupling、Intelligence stopping | no common operator inferred |
| SSO | gap/window only | two names、6条件と3条件 | FIG-01/04 | Phase00 7 components | documentary decompositionをformal定義へ昇格しない |
| qualia/access/self | schematic Log Referencing等、JA C(t) | frontier / terrain / ego position | FIG-03/05 | CT insight / downstream reuse | prose identity claimをtyped identityとしない |
| projection | dedicated typed projection式なし | mass assignment definition | gate/selection arrows | IFGT primitiveという名、Intelligence再利用 | source claimとexact upstream locatorを分離 |

Authority順は**local exact display → local prose → figure-local statement → analogy → upstream borrowed term → downstream reinterpretation**を各objectの引用同定の起点とする。ただし下位の矛盾を消す規則ではない。current EN/JA両buildはそれぞれ保持し、workingは非canonicalとして履歴を保存する。表の意味差を解決せずCON-Uへ渡す。

## 24. Phase-01 uncertainty ledger

Phase00 CON-U-001–018を変更せず、新規IDは019から開始する。以下の20行を本phaseの**unresolved equation/object identity issues**の集計単位とする。SIGのUNRESOLVED行数20とは別の集合であり合算しない。EXACT pairの存在とobject identity未解決は両立する。

| CON-U | Identity/signature issue | Source trace / what is fixed | What remains unresolved |
| --- | --- | --- | --- |
| CON-U-019 | IFGT template version | §14、EQ-009–012/085–088、Phase00 U001 | t/tau、J/J_I、F/F_I、K*Iを一つのcurrent IFGT formとするtranslation |
| CON-U-020 | C / Delta C / Delta v | §12、FIG-06、Phase00 U002 | same-condition claimのcoordinate transform / domain |
| CON-U-021 | SSO condition sets | §9、Phase00 U005 | 6条件/3条件/7componentsの同等性と二名称のformal object identity |
| CON-U-022 | T / T_Phi / T_i | §10、JA079–081 | index extension/localizationのtyped relation、proportionality constants |
| CON-U-023 | mu / mu_I | §5/14 | coupling viscosityとmobilityのrelation/calibration |
| CON-U-024 | older VED PDE history | §13、IFG-07/RC-038、Phase00 U003 | exact current IFGT analogueは所在、older historical version / Vol.4 locator意図は未固定 |
| CON-U-025 | access/report/qualia | §15/17、Phase00 U011 | explicit consciousness要件とlive qualiaのformal relation |
| CON-U-026 | self/ego/observer | §16、Phase00 U012 | position/terrain/loopを結ぶtyped map、reportable selfの独立定義 |
| CON-U-027 | projection signature | §19、Phase00 U009 | mass assignmentのdomain/codomain、local gateとの同一map |
| CON-U-028 | figure3 lower bound | WIN-16、FIG-03、Phase00 U017 | Delta v_minと本文0の関係、projectionされた他bounds |
| CON-U-029 | figure4 field-change condition | WIN-07/08、FIG-04 | partial_t Phiとpartial_t Iのrelation、nonzero同等性 |
| CON-U-030 | figure language variants | FIG-01/03/06 | tau比例記号、access/意識、JA phase labelsのsource意図 |
| CON-U-031 | JA attention object family | EQ-079–081 | A_i,m_i,T_i,Delta v_i carrier/index/unit、EN counterpartなし |
| CON-U-032 | JA C(t) opening family | EQ-101/140、SIG-022/047 | closure Cとのglyph collision、cal F codomainとrho_s map |
| CON-U-033 | JA not-state statement | EQ-121、S07/S08 | EN state/regimeおよびJA他節とのnamed-object identity |
| CON-U-034 | rates/units/bounds | §7/8/11、Phase00 U006 | rate dimensions、ratio normalizations、numerical bounds |
| CON-U-035 | CT token/gradient/limit reuse | EQ-007/083、S09/S20、§14 | local ell_i carrier、same quantity / Phi* correspondenceのexact typed map |
| CON-U-036 | t / delay tau / long-time tau | §18、Phase00 U007 | external derivative、reference duration、CT limit、experienced timeの別signature |
| CON-U-037 | node-pair terminology | EQ-015/091、Vol.1 eq:Cij | causal-log/history vs closure/connection wording、layer aggregation |
| CON-U-038 | named window/map signature | EQ-022/039/067ほか、SIG-054 | Log Referencing codomain、consciousness window set、norm/kernel/geometryのexact conventions |

## 25. Validation

### 25.1 集計の固定

| Inventory unit | Count | Counting rule |
| --- | ---: | --- |
| Displayed equation entries | 178 | EN73 + JA105、176 equation +2 bracket |
| Unique equation string families | 52 | body空白列のみ縮約したliteral family。object同一性とは別 |
| Symbol families | 60 | CON-SYM-001–060 |
| Collisions | 27 | CON-COL-001–027、identity認定なし |
| Signatures explicit / inferred / unresolved | 14 / 26 / 20 | SIG-001–060、partial signature classification |
| Unit-status entries | 17 | UNIT-01–17 |
| Fast/slow formal objects | 17 | FS-FORM-01–17 |
| SSO formal/documentary items | 18 | 2 names +6+3 conditions +7 components |
| TCA objects | 8 | CON-TCA-01–08 |
| Window conditions | 17 | WIN-01–17 |
| Closure-family objects | 8 | CL-01–08 |
| Older VED equation entries | 2 | EN/JA各1、equation familyは1 |
| IFGT template correspondences | 10 | IF-TPL-01–10 |
| Phenomenal / self / access objects | 16 / 8 / 8 | PH-OBJ / SELF-OBJ / ACC |
| Time / projection objects | 11 / 8 | TIME / PROJ |
| Figure-symbol entries | 64 | FIG-SYM-001–064、6 figure familiesのsymbol/relation/label sets |
| EN/JA EXACT pairs | 65 | whitespace除外token一致 |
| EN/JA typographic pairs/groups | 8 | single-display5 + one-to-four3 |
| EN/JA source-version additions | 6 | JA-specific display forms、§21。図中差はこの6に含めない |
| Other JA-only displays | 17 | EN-inline対応9 + bounds再掲8 |
| Unresolved identities (Phase01 issues) | 20 | CON-U-019–038、SIG unresolved countとは別集合 |
| New Phase01 uncertainties | 20 | Phase00 001–018は変更なし |

### 25.2 実施検査

| Check | Result / scope |
| --- | --- |
| current source paths / authority | PASS。44 TeX + bib、EN/JA21 input pairs。working2はcurrent抽出から除外 |
| TeX includes / environments | PASS。42 include paths存在、全44 TeXのbegin/end stack balance確認 |
| displayed equation extraction | PASS。独立再抽出178 blocksと本記録178 raw引用が文字列完全一致。追加/削除/変更0 |
| equation/symbol/collision/uncertainty IDs | PASS。連番、entry uniqueness、範囲参照、CON-U開始019を確認 |
| EN/JA counterpart coverage | PASS。EN73/73、JA82 paired +23 unmatched display。JA counterpart重複使用0 |
| figure references / PDFs | PASS。6 families、12 includegraphic pathsとfigure PDFs、main PDFs2の存在/page count確認 |
| PDF spot-check | PASS（限定scope）。key expressionsをtext、JA C(t)とFIG-03/06をrender確認。full distribution auditではない |
| SVG XML / figure symbols | 12 XMLをparse。PDF textと該当SVG文字列を補助照合、図の再生成なし |
| local Markdown links / fences / tables / display balance | PASS。source/recordリンクの存在、178 tex fencesの閉鎖、table列数、fence外math delimiters確認 |
| count consistency | PASS。上表と各entry表、§3 source-status、§21 counterpart内訳を照合 |
| immutability / dirty worktree preservation | PASS。開始時1,445既存filesのSHA-256と比較。README以外の既存file変更0、削除0。新規repo fileは本記録だけ |
| simulation / web / rebuild | NOT RUN。PDFは読む/renderするだけ、current source/figures/PDFを変更しない |
| git diff --check | PASS。untracked本記録も別途末尾空白/構造検査 |

Raw display aggregate SHA-256（EN→JA entry順、各raw block配列をUTF-8 JSON、ensure_ascii=false、separator comma/colon、空白挿入なし）:
`ec2c665b0ed93170e58fb85731816ba18fb2710bee479115dcea3c9cfb2ea503`。

Git上の既存dirty stateはtracked modifications 173件、untracked directory表示4件（generative_law_methodology、notes/bio_ifgt_audit、notes/consciousness_audit、notes/ved_equation_audit）を保持。本phase差分は本記録の新規作成とREADMEのphase/link更新のみ。既存diffを本phaseのsource変更として計上しない。

## 26. Stop boundary

Phase01はsource-local form/signature、same/different glyph、source claims identity/correspondence、source-version differences、identity unresolvedまでを記録した。式役割の最終分類、derivation valid/invalid、mechanism成立、phenomenal explanation成否、循環の善悪、empirical sufficiency、claim downgrade等は行っていない。

上流closureは維持し、research OPENを解決したとはしない。Phase02 **formal / neural / cognitive / phenomenal role auditは未着手**。本phaseで停止する。commit/pushなし。

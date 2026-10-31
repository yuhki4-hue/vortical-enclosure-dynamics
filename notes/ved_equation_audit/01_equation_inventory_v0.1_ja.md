# VED equation inventory v0.1

## 1. Status

Status:

- repository equation / symbol / claim inventory
- audit phase: **01 COMPLETE**
- inventory only
- not an equation-role audit
- not a preload or circularity audit
- not a validity audit
- not a generation-claim evidence audit
- not a revision proposal
- not a VED rewrite or validation
- [`00_connection_record_v0.1_ja.md`](./00_connection_record_v0.1_ja.md): **COMPLETE**
- `02_equation_role_audit_v0.1_ja.md`: **NOT STARTED**
- `03_preload_and_circularity_audit_v0.1_ja.md`: **NOT STARTED**
- `04_generation_claim_evidence_audit_v0.1_ja.md`: **NOT STARTED**
- `05_revision_candidates_v0.1_ja.md`: **NOT STARTED**
- `06_final_audit_record_v1.0_ja.md`: **NOT STARTED**
- VED core revision: **NOT STARTED**
- `generative_law_methodology`: **CLOSED / STOP-A**

本記録は、現行repositoryで使われているequations、symbols、derived quantities、
generation-related claim wordingの所在を記録する。式の正しさ、役割、必要な前提、循環性、
証拠の十分性、改訂要否は判定しない。

---

## 2. Scope

### 2.1 Inventory question

> 現行VEDで使われているequations / symbols / derived quantities /
> generation-related claimsはどこにあり、source間でどの記法関係を持つか。

Source of truthはこのinventory作成時点のrepositoryである。source wordingが複数ある場合は
統合せず併記し、唯一の定義を特定できない場合はその状態を記録する。一般的な数学知識による
補完やnormalizationは行わない。

### 2.2 Primary records read

- [top-level README](../../README.md)
- [top-level Japanese README](../../README_ja.md)
- [core equations](../../docs/core_equations.md)
- [overview](../../docs/00_overview.md)
- [claims](../../docs/claims.md)
- [methodology](../../docs/methodology.md)
- [methodological note](../../docs/methodological_note.md)
- [generative sequence](../../docs/navigation/generative_sequence.md)
- [Vol.1 minimal axiom](../../paper/vol1/sections/minimal_axiom.tex)
- [Vol.1 causal logs and time](../../paper/vol1/sections/causal_logs_time.tex)
- [Vol.1 flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex)
- [Vol.1 closure](../../paper/vol1/sections/closure.tex)
- [Vol.1 space](../../paper/vol1/sections/space.tex)
- [IFGT Japanese record](../../Information-Field-Geometry-Theory/ifgt_ja.md)
- [dimensionality module index](../../dimensionality-working-note/README.md)
- [dimensionality working note I](../../dimensionality-working-note/README_ja.md)
- [dimensionality working note II](../../dimensionality-working-note/README_II_ja.md)
- [audit branch README](./README_ja.md)
- [connection record](./00_connection_record_v0.1_ja.md)

Navigation controlsとして、[AI Spine generated order](../../docs/ai_spine/generated/canonical_derivation_order.md)、
[concept map](../../docs/navigation/concept_map.md)、
[translation table](../../docs/navigation/translation_table.md)、
[claim status](../../docs/navigation/claim_status.md)も参照した。

---

## 3. Source hierarchy

以下はinventory上のsource種別であり、truth hierarchyではない。

| Source class | Records used | Repository-facing status | Use in this inventory |
| --- | --- | --- | --- |
| **CORE DOC** | top READMEs、`docs/core_equations.md`、`docs/00_overview.md`、`docs/claims.md`、methodology docs | top READMEからcurrent guide / summaryとしてリンク | core-facing wordingとcompact equationsの所在 |
| **PAPER** | Vol.1 section TeX files | top READMEがpreprintとして列挙 | section-level equations、labels、近接説明 |
| **NAVIGATION** | generative sequence、AI Spine generated order、concept map、translation table、claim status | navigation / calibration layer | ordering、rank、claim-level wording。paper equationの代替定義とは扱わない |
| **WORKING NOTE** | dimensionality README / working notes | module自身がworking / exploratory statusを明記 | current symbol reuse、追加notation、明示された未決事項の所在 |
| **RELATED BRANCH** | IFGT Japanese record | VED上位layer / related paperとして配置 | IFGT側の\(I,C,J,\sigma,\tau\)とunified equationの所在 |
| **AUDIT RECORD** | branch README、connection record | audit preparation / provenance only | gateとsource lineage。VED equationの定義源にはしない |
| **PUBLIC ESSAY** | connection recordに列挙されたessay links | repository外 | 今回のprimary definition sourceには使用しない |

Currentnessの記録はrepository自身のlabelsに従う。

- top READMEsとそこからリンクされたcore/navigation docs: **current/core-facing**
- `paper/vol1/sections/*.tex`: **paper-facing**
- IFGT record: **related branch**
- dimensionality records: **working / exploratory**
- 明示された旧版・archive以外について、それ以上のsuperseded判定は行わない。
- source間で語義が異なり、repository内に優先規則を発見できない場合: **CURRENTNESS UNCLEAR**

---

## 4. Primary equation / symbol inventory

`Inventory status`は所在と記法状態だけを表す。validity statusではない。

### 4.1 Difference / gradient

| ID | Symbol / expression | Found wording / current meaning | Primary source | Other sources | Discrete / continuum / mixed | Inputs explicitly named | Related claim wording | Notation issue | Inventory status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DIF-01 | \(\delta\) | Vol.1はdifference / asymmetryを\(\delta\)で書く。overview / claimsでは\(\delta S=0\)のvariation記号にも現れる | [minimal axiom](../../paper/vol1/sections/minimal_axiom.tex) | [overview](../../docs/00_overview.md), [claims](../../docs/claims.md) | mixed | difference sourceは式内で未展開。\(\delta S\)では\(S\) | source says asymmetry implies a gradient | differenceとvariationで同じglyphの別usage | **MULTIPLE USAGES** |
| DIF-02 | \(\Delta\) | IFGTはVEDの「difference source」と呼び、\(\Delta=\Delta_{\to C}+\delta I\)およびdrive termに使用 | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | [dimensionality note II](../../dimensionality-working-note/README_II_ja.md) uses \(\Delta V,\Delta E,\Delta H\); Vol.1 closure uses \(\Delta_k\) | mixed | IFGT: \(\Delta_{\to C},\delta I\); drive: \(a,C,C_*\) | source calls \(\Delta\) the driver / source of closure formation | closure distanceやfinite incrementにも同じglyph | **MULTIPLE USAGES** |
| DIF-03 | \(\nabla\delta\), \(J\sim-\nabla\delta\) | Vol.1 minimal chainのdisplayed expressions | [minimal axiom](../../paper/vol1/sections/minimal_axiom.tex) | [Japanese Vol.1 guide](../../docs/vol1_foundations_ja.md) | continuum-looking notation | \(\delta,J\) | source says difference induces gradient and gradient drives flow | domain、coordinates、operator declarationは当該section内で未記載 | **PARTIALLY SPECIFIED** |
| DIF-04 | \(\nabla\Delta\) | 指定core/paper/IFGT sourcesではこのexact expressionを発見しなかった。IFGTには\(\nabla C\), \(\nabla I\)がある | — | repository search | — | — | — | \(\Delta\) sourceとgradient stageの併記はあるがexact formulaへ統合しない | **NOT LOCATED** |
| DIF-05 | gradient (symbolなし) | navigation rank 2 / generated stage、top READMEのsequence item | [generative sequence](../../docs/navigation/generative_sequence.md) | [README](../../README.md), [README ja](../../README_ja.md) | unspecified | registered differenceと記述 | directional structure across registered difference | navigation termと\(\nabla\delta\)の同一性を明示する式は未発見 | **PARTIALLY SPECIFIED** |

### 4.2 History / closure / causal record

| ID | Symbol / expression | Found wording / current meaning | Primary source | Other sources | Discrete / continuum / mixed | Inputs explicitly named | Related claim wording | Notation issue | Inventory status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LOG-01 | \(H_{ij}\ge0\) | Vol.1 source labels it **causal history**: total accumulated influence from \(i\) to \(j\), irreversible and unfiltered | [causal logs and time](../../paper/vol1/sections/causal_logs_time.tex) | [core equations](../../docs/core_equations.md), [overview](../../docs/00_overview.md), [dimensionality note II](../../dimensionality-working-note/README_II_ja.md) | discrete-indexed; derivative also used | nodes \(i,j\); later \(\dot H_{ij}\) | retained history is distinguished from total history | event sequence vs continuous quantity is explicitly left undecided in dimensionality note | **PARTIALLY SPECIFIED** |
| LOG-02 | \(C_{ij}\in[0,1)\) | Vol.1 / core equations call it **causal log**, selected persistent portion of \(H_{ij}\). Top README / navigation call it **closure degree**, rank-1 formal carrier, and call causal log its accumulated trace | [causal logs and time](../../paper/vol1/sections/causal_logs_time.tex) | [core equations](../../docs/core_equations.md), [README](../../README.md), [README ja](../../README_ja.md), [generative sequence](../../docs/navigation/generative_sequence.md), [AI Spine order](../../docs/ai_spine/generated/canonical_derivation_order.md) | discrete matrix / network | \(i,j\); selection equation adds \(\lambda,\rho_i,H_{ij}\) | paper: retained influence; navigation: first formal carrier generated from difference | causal-log identityとclosure-degree identityがsource間で一致しない | **MULTIPLE DEFINITIONS** |
| LOG-03 | \(C_{ij}=1-\exp(-\lambda\rho_iH_{ij})\) | Vol.1 source labels it **causal log equation** / self-referential selection equation | [causal logs and time](../../paper/vol1/sections/causal_logs_time.tex) | [core equations](../../docs/core_equations.md), [overview](../../docs/00_overview.md) | discrete-indexed | \(\lambda,\rho_i,H_{ij}\) | source says existing structure governs selection of new history | identity of \(C_{ij}\) inherits LOG-02 source conflict | **LOCATED** |
| LOG-04 | \(\rho_i=\sum_jC_{ij}\) | Vol.1 source labels it **log density at node \(i\)** | [causal logs and time](../../paper/vol1/sections/causal_logs_time.tex) | [core equations](../../docs/core_equations.md), [overview](../../docs/00_overview.md), [dimensionality note I](../../dimensionality-working-note/README_ja.md) | discrete / node-indexed | \(C_{ij}\), sum over \(j\) | core equations also calls it local time generation rate | continuum \(\rho\)とのmappingは別項目 | **MULTIPLE USAGES** |
| LOG-05 | \(\lambda>0\) | Vol.1 source calls it **selection sensitivity** and, in that equation section, “the sole external parameter” | [causal logs and time](../../paper/vol1/sections/causal_logs_time.tex) | [overview](../../docs/00_overview.md), [claims](../../docs/claims.md) | parameter | enters \(\lambda\rho_iH_{ij}\) | controls selection wording | repository全体には他parameterもあるため、“sole”のscopeは当該formulationとして記録 | **LOCATED** |
| LOG-06 | \(\rho_i=\sum_j[1-\exp(-\lambda\rho_iH_{ij})]\) | substitution後のself-referential fixed-point equation | [causal logs and time](../../paper/vol1/sections/causal_logs_time.tex) | [overview](../../docs/00_overview.md) | discrete / node-indexed | \(\lambda,H_{ij}\) | source associates stable \(\rho_i^*\) with persistent physical structure | iteration/update scheduleは当該displayで未指定 | **PARTIALLY SPECIFIED** |
| LOG-07 | \(\dot\rho_i=\lambda\rho_iB_i/(1-\lambda A_i)\) | Vol.1 source labels it **log-generation rate** derivation, with \(A_i\), \(B_i\) defined by sums | [causal logs and time](../../paper/vol1/sections/causal_logs_time.tex) | nearby source links it to continuum \(\sigma\) | mixed | \(\lambda,\rho_i,H_{ij},\dot H_{ij}\) | numerator described as new-history injection; denominator as saturation | exact map from this quantity to \(\sigma\) is not displayed | **PARTIALLY SPECIFIED** |

### 4.3 Time-related notation

| ID | Symbol / expression | Found wording / current meaning | Primary source | Other sources | Discrete / continuum / mixed | Inputs explicitly named | Related claim wording | Notation issue | Inventory status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TIM-01 | \(t\) | Vol.1 writes derivatives with respect to \(t\) but does not define \(t\) in the causal-logs section. IFGT separately labels \(t\) an external order parameter in a fixed-background effective description | [causal logs and time](../../paper/vol1/sections/causal_logs_time.tex) | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md), [overview](../../docs/00_overview.md) | continuum parameter | derivative variable | overview contrasts background \(t\) with derived time claims | whether Vol.1 \(t\) and IFGT effective \(t\) have identical source identity is unresolved | **SOURCE IDENTITY UNRESOLVED** |
| TIM-02 | \(\tau_i\) | Vol.1 calls it time at node \(i\); core equations calls it observational time | [causal logs and time](../../paper/vol1/sections/causal_logs_time.tex) | [core equations](../../docs/core_equations.md), [overview](../../docs/00_overview.md), [space](../../paper/vol1/sections/space.tex) | node-indexed continuous quantity | \(i,t,\rho_i\) | source wording: time is rate at which structure accumulates | IFGT has separate \(\tau\) and \(\tau_{\mathrm{VED}}\) distinction | **MULTIPLE USAGES** |
| TIM-03 | \(d\tau_i/dt=\rho_i\) | Vol.1 labels it in “Generation of Time”; core equations includes it in compact core equation | [causal logs and time](../../paper/vol1/sections/causal_logs_time.tex) | [core equations](../../docs/core_equations.md), [overview](../../docs/00_overview.md), [space](../../paper/vol1/sections/space.tex) | mixed node / continuum derivative | \(t,\rho_i\) | source says \(\rho_i\ge0\) makes \(\tau_i\) monotone | \(t\) local definition not located in Vol.1 section | **PARTIALLY SPECIFIED** |
| TIM-04 | \(\tau\), \(\tau_{\mathrm{VED}}\) | IFGT explicitly distinguishes informational time \(\tau\), generative time \(\tau_{\mathrm{VED}}\), and external order parameter \(t\) | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | application-layer files also reuse \(\tau\), not inventoried as VED core definitions | continuum / field parameter | difference-structure interaction in prose | IFGT says the two taus have different origins but are dynamically isomorphic / embeddable | no explicit embedding map is displayed | **MULTIPLE DEFINITIONS** |

### 4.4 Symmetric / antisymmetric decomposition

| ID | Symbol / expression | Found wording / current meaning | Primary source | Other sources | Discrete / continuum / mixed | Inputs explicitly named | Related claim wording | Notation issue | Inventory status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DEC-01 | \(S_{ij}=\tfrac12(C_{ij}+C_{ji})\) | Vol.1 source calls \(S_{ij}\) the symmetric part and says it encodes mutual connectivity / spatial component | [space](../../paper/vol1/sections/space.tex) | [overview](../../docs/00_overview.md) | discrete matrix | \(C_{ij},C_{ji}\) | source associates it with spatial proximity / connectivity | inherits \(C_{ij}\) identity ambiguity | **LOCATED** |
| DEC-02 | \(A_{ij}=\tfrac12(C_{ij}-C_{ji})\) | Vol.1 source calls \(A_{ij}\) the antisymmetric part and says it encodes directed flow / temporal and causal component | [space](../../paper/vol1/sections/space.tex) | [overview](../../docs/00_overview.md), [flow](../../paper/vol1/sections/flow_vorticity.tex) | discrete matrix | \(C_{ij},C_{ji}\) | source says time and space arise as aspects of \(C_{ij}\) | \(A_i\) in the \(\dot\rho_i\) formula is a different indexed quantity | **MULTIPLE USAGES** |

### 4.5 Flow / balance

| ID | Symbol / expression | Found wording / current meaning | Primary source | Other sources | Discrete / continuum / mixed | Inputs explicitly named | Related claim wording | Notation issue | Inventory status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FLW-01 | \(J_{ij}=C_{ij}-C_{ji}=2A_{ij}\) | Vol.1 source labels it **log-flow**, net directional transfer of causal influence | [flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex) | [overview](../../docs/00_overview.md) | discrete / antisymmetric matrix | \(C_{ij},C_{ji},A_{ij}\) | source says nonzero \(J_{ij}\) corresponds to directed propagation | relation to earlier \(J\sim-\nabla\delta\) not given as an explicit map | **LOCATED** |
| FLW-02 | \(\mathbf J(x)\) | Vol.1 says \(J_{ij}\) “becomes a vector field” in the coarse-grained limit | [flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex) | [overview](../../docs/00_overview.md), [methodology](../../docs/methodology.md) | continuum | \(x\); component dependence not expanded | used in continuity and vorticity expressions | coarse-graining map from \(J_{ij}\) is not displayed | **PARTIALLY SPECIFIED** |
| FLW-03 | \(\rho\), possible \(\rho(x,t)\) reading | Vol.1 continuity equation uses continuum \(\rho\) without explicit arguments. Exact \(\rho(x,t)\) notation was not located in the required core sources | [flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex) | [claims](../../docs/claims.md), [methodology](../../docs/methodology.md) | continuum | implicit \(x,t\) from PDE context | source calls it log density evolution | explicit map from \(\rho_i\) and explicit function signature absent | **PARTIALLY SPECIFIED** |
| FLW-04 | \(\partial_t\rho+\nabla\cdot\mathbf J=\sigma\) | Vol.1 source labels this the continuity equation and explicitly says it is not a conservation law when \(\sigma>0\) | [flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex) | [claims](../../docs/claims.md), [methodology](../../docs/methodology.md) | continuum | \(t,\rho,\mathbf J,\sigma\) | source associates \(\sigma=0\) with classical fixed-point regime | IFGT uses an analogous equation with \(I,\tau,J,\sigma\) | **MULTIPLE USAGES** |
| FLW-05 | \(\sigma\ge0\), \(\sigma>0\) | Vol.1 calls it log-generation rate and says it is not an external source; claims page calls \(\sigma>0\) generative-time regime | [flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex) | [claims](../../docs/claims.md), [overview](../../docs/00_overview.md), [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | mixed | VED paper: continuity fields; IFGT: drive/dissipation/barrier inputs | displayed source wording: \(\sigma>0\Longleftrightarrow\) time is being generated | VED log-generation and IFGT incompatibility term are described differently | **MULTIPLE DEFINITIONS** |
| FLW-06 | \(\mathbf J=\mathbf J_{\rm rot}+\mathbf J_{\rm pot}\) | Vol.1 labels this a Helmholtz decomposition | [flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex) | [overview](../../docs/00_overview.md) | continuum | \(\mathbf J\) | rot component carries vorticity; pot component carries divergence in source wording | conditions / domain for decomposition not stated in the listed section | **PARTIALLY SPECIFIED** |

### 4.6 Rotation / vorticity / enclosure

| ID | Symbol / expression | Found wording / current meaning | Primary source | Other sources | Discrete / continuum / mixed | Inputs explicitly named | Related claim wording | Notation issue | Inventory status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENC-01 | \(\omega=\nabla\times\mathbf J\) | Vol.1 source labels \(\omega\) vorticity of log-flow | [flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex) | [overview](../../docs/00_overview.md) | continuum | \(\mathbf J\) | source associates nonzero \(\omega\) with circulation and possible closed flow lines | domain / dimension / orientation declaration not in listed section | **PARTIALLY SPECIFIED** |
| ENC-02 | \(L\sim\lvert\omega\rvert\) | Vol.1 source calls \(L\) local intensity / closure density | [flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex) | [overview](../../docs/00_overview.md) | continuum / approximate | \(\omega\) | source calls \(L\) source of particle structure and gravitational effects | proportionality relation and normalization not specified here | **PARTIALLY SPECIFIED** |
| ENC-03 | \(L<L_{\max}\) | Vol.1 labels this non-closure constraint “at all times” | [minimal axiom](../../paper/vol1/sections/minimal_axiom.tex) | [overview](../../docs/00_overview.md), [claims](../../docs/claims.md) | scalar / effective | \(L,L_{\max}\) | complete closure treated as unattainable limit in source wording | meaning / normalization of \(L_{\max}\) is local to effective closure description | **PARTIALLY SPECIFIED** |
| ENC-04 | \(B(L)=-\kappa_B\log(1-L/L_{\max})\) | Vol.1 calls it an effective closure barrier / phenomenological encoding | [minimal axiom](../../paper/vol1/sections/minimal_axiom.tex) | [overview](../../docs/00_overview.md), [claims](../../docs/claims.md), [closure](../../paper/vol1/sections/closure.tex) | scalar / effective | \(L,L_{\max},\kappa_B\) | \(B(L)\to\infty\) as \(L\to L_{\max}\) | overview/claims use \(\kappa_{B,\mathrm{eff}}\), paper uses \(\kappa_B\) | **MULTIPLE USAGES** |
| ENC-05 | \(\Delta_k=L_{\max}-L_k\) | Vol.1 source labels it closure distance of stable configuration | [closure](../../paper/vol1/sections/closure.tex) | [overview](../../docs/00_overview.md), Vol.2 uses unindexed \(\Delta\) for closure deficit | scalar / indexed configuration | \(L_{\max},L_k\) | source relates it to effective mass scaling | same \(\Delta\) glyph is difference source and finite increment elsewhere | **MULTIPLE DEFINITIONS** |
| ENC-06 | \(E(A)=\alpha\lvert\sum_{i\in A}\vec e_i\rvert^2-\beta\Phi(A)+\gamma\lvert A\rvert+B(L(A))\) | Vol.1 source labels it closure energy of configuration \(A\) | [closure](../../paper/vol1/sections/closure.tex) | [dimensionality note I](../../dimensionality-working-note/README_ja.md) reuses it | mixed finite configuration / vector expression | \(A,\vec e_i,\Phi,\alpha,\beta,\gamma,B,L\) | source defines particle as a local minimum of this expression | \(\Phi\) here is non-degeneracy sum; IFGT \(\Phi\) is information potential | **MULTIPLE USAGES** |
| ENC-07 | \(m_k\propto\left.\frac{d^2E}{dL^2}\right\rvert_{L_k}\sim\kappa_B/\Delta_k^2\) | Vol.1 source presents effective mass scaling within phenomenological barrier approximation | [closure](../../paper/vol1/sections/closure.tex) | [overview](../../docs/00_overview.md), Vol.2 files | scalar / effective | \(E,L_k,\kappa_B,\Delta_k\) | nearby wording associates heavier structures with smaller closure distance | proportionalities and approximation scope appear source-dependent | **PARTIALLY SPECIFIED** |

### 4.7 Distance / geometry

| ID | Symbol / expression | Found wording / current meaning | Primary source | Other sources | Discrete / continuum / mixed | Inputs explicitly named | Related claim wording | Notation issue | Inventory status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GEO-01 | \(\widetilde S_{ij}=\max_{\gamma:i\to j}\prod_{(ab)\in\gamma}S_{ab}\) | Vol.1 source calls it propagation strength / maximum-path strength | [space](../../paper/vol1/sections/space.tex) | [overview](../../docs/00_overview.md) | discrete network | paths \(\gamma\), edge values \(S_{ab}\) | best available influence channel in source wording | admissible path family and edge-value endpoint policy not separately specified | **PARTIALLY SPECIFIED** |
| GEO-02 | \(d_{ij}=-\log\widetilde S_{ij}=\min_\gamma\sum_{(ab)\in\gamma}(-\log S_{ab})\) | Vol.1 source explicitly says “distance between nodes” and “shortest-path problem on a weighted network” | [space](../../paper/vol1/sections/space.tex) | [overview](../../docs/00_overview.md) | discrete network | \(S_{ab},\gamma\) | source says distance is resistance to influence propagation | source proposition names non-negativity and triangle inequality; other metric axioms are not enumerated there | **LOCATED** |
| GEO-03 | \(d_{ij}=\min_\gamma\sum[-\log S_{ab}+\epsilon L_{ab}]\) | overview calls this the unified distance with closure density contributing to path cost | [overview](../../docs/00_overview.md) | later gravity paper locations are referenced by overview | discrete weighted network | \(S_{ab},L_{ab},\epsilon,\gamma\) | source wording: gravity is distortion of distance by closure density | relation to Vol.1 \(d_{ij}\) is an added term; \(L_{ab}\) definition not given in overview | **MULTIPLE DEFINITIONS** |
| GEO-04 | \(d(x,y)^2\approx g_{\mu\nu}(x)(x^\mu-y^\mu)(x^\nu-y^\nu)\) | Vol.1 source calls this a smooth effective distance in a coarse-grained limit | [space](../../paper/vol1/sections/space.tex) | [overview](../../docs/00_overview.md) | continuum / approximate | \(x,y,g_{\mu\nu}\) | source calls metric tensor an effective description, not a fundamental field | explicit grouping / averaging map is not displayed | **PARTIALLY SPECIFIED** |
| GEO-05 | \(g_{\mu\nu}=\text{effective description of }d_{ij}\text{ under coarse-graining}\) | source's displayed wording | [space](../../paper/vol1/sections/space.tex) | [overview](../../docs/00_overview.md) | mixed discrete-to-continuum | \(d_{ij}\), unspecified coarse-graining | source says coordinates label coarse-grained blocks | no explicit limiting procedure or uniqueness statement located | **PARTIALLY SPECIFIED** |
| GEO-06 | \(\nabla^2\Psi\propto L\), \(g=-\nabla\Psi\) | overview presents closure density as source of gravitational potential | [overview](../../docs/00_overview.md) | Vol.3 is named as broader source | continuum | \(L,\Psi\) | source wording: gravity is sourced by closure density | \(g\) here is gravitational field, while \(g_{\mu\nu}\) is metric tensor | **MULTIPLE USAGES** |
| GEO-07 | \(g_{\mu\nu}=g^{(0)}_{\mu\nu}+\alpha_GL_{\mu\nu}[g]\) | overview calls this VED fixed-point equation and mentions weak-gravity linearization | [overview](../../docs/00_overview.md) | Vol.3 broader records | continuum tensor | \(g^{(0)},\alpha_G,L_{\mu\nu}[g]\) | nearby claim associates linearization with Einstein equations | \(L_{\mu\nu}[g]\) is not defined in overview | **PARTIALLY SPECIFIED** |

### 4.8 IFGT-related quantities and equations

| ID | Symbol / expression | Found wording / current meaning | Primary source | Other sources | Discrete / continuum / mixed | Inputs explicitly named | Related claim wording | Notation issue | Inventory status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IFG-01 | \(I\) | IFGT source labels it **information density**, density of persistent trace left by unclosed difference | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | dimensionality/core VED sources do not define bare \(I\) as interaction | continuum field / scalar | \(C\) through \(I=f(1-C)\) | source treats it as IFGT central quantity | no current primary-source definition of bare \(I\) as “interaction” located | **LOCATED** |
| IFG-02 | \(I=f(1-C)\), later \(I=1-C\) | IFGT first states a nondecreasing \(f\), then adopts linear approximation for unified equation | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | — | continuum field | \(C,f\) | source calls \(I,C\) complementary, not identical | general relation and linear approximation coexist | **MULTIPLE DEFINITIONS** |
| IFG-03 | \(C(x,\tau)\) | IFGT calls it a closure-degree field in the unified VED×IFGT equation | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | application branches reuse it | continuum field | \(x,\tau\) | source says unified equation connects VED and IFGT descriptions | explicit construction from discrete \(C_{ij}\) is not located | **PARTIALLY SPECIFIED** |
| IFG-04 | \(\partial_\tau I+\nabla\cdot J=\sigma\) | IFGT source labels it the basic equation for information-density evolution | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | structurally resembles VED continuum equation | continuum | \(I,\tau,J,\sigma\) | source describes transport plus generation | \(J,\sigma,\tau\) have VED-side and IFGT-side usages | **MULTIPLE USAGES** |
| IFG-05 | \(J=-D\nabla I+\mu F_I\), \(F_I=-\nabla\Phi=\alpha\nabla C\) | IFGT source labels \(J\) information flow, \(\Phi\) information potential, \(F_I\) constraint-potential gradient | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | VED paper uses \(J_{ij}\), \(\mathbf J\), and closure-energy \(\Phi(A)\) | continuum | \(D,I,\mu,F_I,\Phi,\alpha,C\) | source says closure-degree gradient biases information flow | same \(J,\Phi,C\) glyphs have other source meanings | **MULTIPLE DEFINITIONS** |
| IFG-06 | \(\sigma_{\rm drive}=a\Delta(1-C/C_*)\), \(\sigma_{\rm dissip}=-\Gamma C\), \(\sigma_{\rm barrier}=-\kappa_B/(C_{\max}-C)\) | IFGT source splits \(\sigma\) into drive, dissipation, barrier contributions | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | VED paper calls \(\sigma\) log-generation rate without this displayed split | continuum | \(a,\Delta,C,C_*,\Gamma,\kappa_B,C_{\max}\) | source connects mismatch to new difference / information-density change | VED / IFGT \(\sigma\) identity stated as correspondence in prose, not an explicit map | **MULTIPLE DEFINITIONS** |
| IFG-07 | \(\partial_\tau C+\nabla\cdot J_C=a\Delta(1-C/C_*)-\Gamma C-\kappa_B/(C_{\max}-C)\) | IFGT source labels it VED×IFGT unified equation, equation (5.2) | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | reused in application-layer files | continuum | \(C,\tau,J_C,a,\Delta,C_*,\Gamma,\kappa_B,C_{\max}\) | source lists possible solution classes but states individual identification / derivation is outside its scope | related-branch equation; not listed in `docs/core_equations.md` | **LOCATED** |
| IFG-08 | \(J_C=-D\nabla C-\mu\alpha C\nabla C\) | IFGT equation (5.3), written after linear \(I=1-C\) assumption | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | — | continuum | \(D,C,\mu,\alpha\) | source describes second term as constraint-potential-gradient term | relationship to Vol.1 \(\mathbf J\) not explicitly mapped | **PARTIALLY SPECIFIED** |

### 4.9 Other current core-facing expressions located

| ID | Symbol / expression | Found wording / current meaning | Primary source | Other sources | Discrete / continuum / mixed | Inputs explicitly named | Related claim wording | Notation issue | Inventory status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OTH-01 | \(C\to J\to\omega\to L\to g\) | core equations presents this as compact formal generative chain | [core equations](../../docs/core_equations.md) | [README](../../README.md), [generative sequence](../../docs/navigation/generative_sequence.md) | mixed | named stages only | source calls \(g\) effective geometry | no single displayed translation joins every arrow | **PARTIALLY SPECIFIED** |
| OTH-02 | \(L\sim\lvert\omega\rvert\to\) particle / gravity wording | paper and overview place particle structure and gravity near closure density | [flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex) | [overview](../../docs/00_overview.md), [closure](../../paper/vol1/sections/closure.tex) | mixed | \(L,\omega\) plus later expressions | source labels particles as closure-energy minima and gravity as distance distortion / potential relation | several equations participate; no unique single “generation equation” located | **MULTIPLE USAGES** |
| OTH-03 | \(\partial C/\partial t+\nabla\cdot J_C=\cdots\) | IFGT says this \(t\)-form is usable when background spacetime is approximately fixed; \(\tau\)-form remains basic there | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | application-layer files | continuum | \(C,t,J_C\); RHS abbreviated | source calls it effective description | ellipsis leaves exact equation implicit by reference to (5.2) | **PARTIALLY SPECIFIED** |

---

## 5. Notation conflicts

This section records same-glyph / adjacent-glyph usages. It does not recommend renaming.

### 5.1 \(\Delta\)

| Usage | Source wording | Source | Inventory status |
| --- | --- | --- | --- |
| \(\Delta\) | VED difference source / driver in IFGT correspondence | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | **LOCATED** |
| \(\Delta_k=L_{\max}-L_k\) | closure distance | [Vol.1 closure](../../paper/vol1/sections/closure.tex) | **LOCATED** |
| unindexed \(\Delta=L_{\max}-L\) | closure deficit in guide / Vol.2-facing wording | [Japanese Vol.1 guide](../../docs/vol1_foundations_ja.md) | **MULTIPLE USAGES** |
| \(\Delta V,\Delta E,\Delta\beta_1,\Delta H\) | finite increments in dimensionality working record | [dimensionality note II](../../dimensionality-working-note/README_II_ja.md) | **MULTIPLE USAGES** |

The repository contains both difference-source and closure-distance meanings. No source-level global
normalization rule was located.

### 5.2 \(C\)

| Usage | Source wording | Source | Inventory status |
| --- | --- | --- | --- |
| \(C_{ij}\) | causal log, selected retained influence | [Vol.1 causal logs](../../paper/vol1/sections/causal_logs_time.tex) | **LOCATED** |
| \(C_{ij}\) | closure degree, rank-1 formal carrier; causal log described as accumulated trace | [generative sequence](../../docs/navigation/generative_sequence.md), [README](../../README.md) | **MULTIPLE DEFINITIONS** |
| \(C\in[0,1]\) | VED closure degree in IFGT correspondence | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | **LOCATED** |
| \(C(x,\tau)\) | closure-degree field in unified equation | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | **PARTIALLY SPECIFIED** |

The discrete matrix, navigation-level closure degree, accumulated causal-log wording, scalar closure
degree, and continuum field are not collapsed into one inventory item.

### 5.3 \(I\)

| Usage | Source wording | Source | Inventory status |
| --- | --- | --- | --- |
| \(I\) | information density | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | **LOCATED** |
| \(I\) as interaction | no unique current definition located in the required core / paper / IFGT / dimensionality sources | repository search | **NOT LOCATED** |

Prose discusses interaction, but this inventory found no source that assigns the bare symbol \(I\) a
current VED-core meaning of interaction.

### 5.4 \(J\)

| Usage | Source wording | Source | Inventory status |
| --- | --- | --- | --- |
| \(J\sim-\nabla\delta\) | flow in minimal chain | [minimal axiom](../../paper/vol1/sections/minimal_axiom.tex) | **PARTIALLY SPECIFIED** |
| \(J_{ij}=C_{ij}-C_{ji}\) | discrete log-flow | [flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex) | **LOCATED** |
| \(\mathbf J(x)\) | coarse-grained vector field | [flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex) | **PARTIALLY SPECIFIED** |
| \(J\) | IFGT information flow | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | **MULTIPLE DEFINITIONS** |
| \(J_C\) | IFGT closure-degree flow after rewriting | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | **LOCATED** |

Vol.1 gives a verbal coarse-grained relation from \(J_{ij}\) to \(\mathbf J\), while the exact bridge
among all five usages is not displayed.

### 5.5 \(\rho\)

| Usage | Source wording | Source | Inventory status |
| --- | --- | --- | --- |
| \(\rho_i=\sum_jC_{ij}\) | node log density; core summary also says local time generation rate | [causal logs](../../paper/vol1/sections/causal_logs_time.tex), [core equations](../../docs/core_equations.md) | **MULTIPLE USAGES** |
| \(\rho\) in \(\partial_t\rho+\nabla\cdot\mathbf J=\sigma\) | continuum log density | [flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex) | **PARTIALLY SPECIFIED** |
| \(\rho\) in cosmology equations | homogeneous density-like quantity in overview | [overview](../../docs/00_overview.md) | **MULTIPLE USAGES** |

An explicit \(\rho_i\mapsto\rho(x,t)\) construction was not located in the listed current sources.

### 5.6 Additional same-glyph records

- \(A_{ij}\) is the antisymmetric part of \(C\), while \(A_i\) in the \(\dot\rho_i\) formula is a
  different node-indexed sum.
- \(\Phi(A)\) in closure energy is a non-degeneracy sum; \(\Phi\) in IFGT is information potential.
- \(g_{\mu\nu}\) is a metric tensor; \(g=-\nabla\Psi\) in overview is a gravitational field symbol.
- \(\tau_i\), \(\tau_{\mathrm{VED}}\), and IFGT \(\tau\) are not source-identical by notation alone.
- \(L\) is closure density; \(L_{ab}\) appears as an edge/path contribution in the unified distance
  overview without a local definition there.

No rename or preferred notation is proposed in this phase.

---

## 6. Discrete / continuum boundary inventory

Status labels in this section describe whether a map is written, not whether a transition is valid.

| Boundary ID | Source-side expression | Target-side expression | Current source wording | Mapping / limiting record located | Status |
| --- | --- | --- | --- | --- | --- |
| DC-01 | \(C_{ij}\) | \(C\), \(C(x,\tau)\) | IFGT correspondence table aligns closure degree \(C\) with \(I\), then writes continuum field \(C(x,\tau)\) | no explicit discrete-matrix-to-field map located | **NO MAP LOCATED** |
| DC-02 | \(J_{ij}=C_{ij}-C_{ji}\) | \(\mathbf J(x)\) | Vol.1 says “in the coarse-grained limit, \(J_{ij}\) becomes a vector field” | verbal correspondence; no operator / scaling / limit formula displayed | **INFORMAL CORRESPONDENCE** |
| DC-03 | \(\rho_i=\sum_jC_{ij}\) | continuum \(\rho\) in \(\partial_t\rho+\nabla\cdot\mathbf J=\sigma\) | Vol.1 passes from node log density to coarse-grained density wording | no interpolation or normalization map displayed | **INFORMAL CORRESPONDENCE** |
| DC-04 | network \((C_{ij},S_{ij},J_{ij})\) | continuum fields / derivatives | Vol.1 invokes a coarse-grained limit and Helmholtz decomposition | selected endpoint equations are explicit; intermediate mapping is not | **PARTIAL CORRESPONDENCE ONLY** |
| DC-05 | weighted-network \(d_{ij}\) | \(d(x,y),g_{\mu\nu}(x)\) | source says grouping nodes into blocks and averaging produces smooth effective distance | approximate metric expression is given; grouping / averaging rule is not | **PARTIAL CORRESPONDENCE ONLY** |
| DC-06 | relation metric \(d_{ij}=-\log\widetilde S_{ij}\) | gravity-modified path distance | overview adds \(\epsilon L_{ab}\) to path cost | displayed modified formula located; derivation from Vol.1 form not displayed | **EXPLICIT MAP LOCATED** |
| DC-07 | VED \(\sigma\) / \(\dot\rho_i\) | IFGT \(\sigma\) and split terms | paper says microscopic \(\dot\rho_i\) underlies \(\sigma\); IFGT says its \(\sigma\) corresponds to VED difference generation | no equality / projection map tying all usages together | **INFORMAL CORRESPONDENCE** |
| DC-08 | VED \(\tau_i\) | IFGT \(\tau_{\mathrm{VED}},\tau\) | IFGT says origins differ but dynamics are isomorphic and one is embeddable on the same time axis | no embedding map displayed | **INFORMAL CORRESPONDENCE** |
| DC-09 | graph / network | metric-readability and effective dimension records | dimensionality module describes finite graph observables and constructed shortest-distance fields | module has model-specific procedures; no repository-wide VED-core continuum map claimed | **PARTIAL CORRESPONDENCE ONLY** |

For DC-06, “EXPLICIT MAP LOCATED” means only that the overview writes the modified path-cost formula
from named inputs. It is not a verdict about its role, derivation, or physical interpretation.

---

## 7. Claim-location inventory

The wording below is attributed to its source. `Inventory note` does not assess truth.

| Claim ID | Claim wording | Source | Equation(s) cited nearby | Scope wording | Evidence reference in source | Inventory note |
| --- | --- | --- | --- | --- | --- | --- |
| CLM-01 | difference is the sole axiom; \(C_{ij}\), gradient, flow, vortex, enclosure follow in rank order | [README](../../README.md), [README ja](../../README_ja.md), [generative sequence](../../docs/navigation/generative_sequence.md) | textual chain; AI Spine ranked order | navigation says validated layers 0–1; later ranks are listed in generated order | links to AI Spine and Vol.1 | navigation / core-facing claim wording located; meaning of \(C_{ij}\) differs from Vol.1 label |
| CLM-02 | difference / asymmetry gives gradient and flow | [minimal axiom](../../paper/vol1/sections/minimal_axiom.tex) | \(\nabla\delta\ne0\), \(J\sim-\nabla\delta\) | paper calls chain necessary | nearby prose and generative-chain figure | claim located; domain and operator specification not inventoried as explicit in this section |
| CLM-03 | causal history is selectively retained as persistent structure | [causal logs and time](../../paper/vol1/sections/causal_logs_time.tex) | \(C_{ij}=1-e^{-\lambda\rho_iH_{ij}}\), \(\rho_i=\sum_jC_{ij}\) | node/network formulation | fixed-point discussion | paper-level claim and equation located |
| CLM-04 | local / observational time is generated by log accumulation | [causal logs and time](../../paper/vol1/sections/causal_logs_time.tex), [core equations](../../docs/core_equations.md) | \(d\tau_i/dt=\rho_i\) | node-indexed | monotonicity statements from \(\rho_i\ge0\) | claim located; \(t\) source identity unresolved |
| CLM-05 | irreversibility is structural / built into the time definition | [causal logs and time](../../paper/vol1/sections/causal_logs_time.tex), [overview](../../docs/00_overview.md) | \(d\tau_i/dt=\rho_i\), \(\rho_i\ge0\) | Vol.1 / overview | source gives monotonicity reasoning | source claim recorded without validity judgment |
| CLM-06 | antisymmetric causal log produces directional flow | [flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex) | \(J_{ij}=C_{ij}-C_{ji}\) | network, then coarse-grained wording | antisymmetry stated “by construction” | discrete equation located; continuum bridge inventoried separately |
| CLM-07 | \(\sigma>0\) corresponds to time being generated; conservation is phase-specific | [flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex), [claims](../../docs/claims.md) | continuity equation; \(\sigma>0\Longleftrightarrow\) time generated | classical fixed-point vs nonclosed regime | phase section referenced by paper | source wording located; evidence audit deferred to 04 |
| CLM-08 | vorticity enables enclosure / persistent structure | [flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex), [closure](../../paper/vol1/sections/closure.tex) | \(\omega=\nabla\times\mathbf J\), \(L\sim\lvert\omega\rvert\), closure energy | continuum plus finite configuration | Vol.1 scope | multiple neighboring expressions rather than one unique update equation |
| CLM-09 | triangular closure is the minimal persistent enclosure; particle is a local minimum of closure energy | [closure](../../paper/vol1/sections/closure.tex) | \(E(A)\), particle definition | Vol.1; later Vol.2 references | local argument and later-volume pointers | particle-related claim location recorded; no verdict |
| CLM-10 | distance is induced from symmetric connectivity / propagation strength | [space](../../paper/vol1/sections/space.tex), [overview](../../docs/00_overview.md) | \(S_{ij}\), \(\widetilde S_{ij}\), \(d_{ij}\) | weighted network | path construction and proposition | source labels distance explicitly; physical meaning not audited |
| CLM-11 | metric / space is a coarse-grained description of log-distance structure | [space](../../paper/vol1/sections/space.tex), [overview](../../docs/00_overview.md) | \(d(x,y)^2\approx g_{\mu\nu}\Delta x^\mu\Delta x^\nu\) | coarse-grained limit | prose says grouping / averaging | mapping record is partial; emergence evidence not judged |
| CLM-12 | closure density modifies distance and is associated with gravity | [overview](../../docs/00_overview.md) | modified path distance; \(\nabla^2\Psi\propto L\); fixed-point metric equation | overview says Vol.3 reconstruction | references Vol.3 and weak-gravity regime | core-facing summary claim located; detailed Vol.3 audit is not performed here |
| CLM-13 | closure density is associated with particle structure and effective mass | [flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex), [closure](../../paper/vol1/sections/closure.tex) | \(L\sim\lvert\omega\rvert\), \(E(A)\), \(m_k\sim\kappa_B/\Delta_k^2\) | phenomenological barrier approximation stated for mass | Vol.2 / Vol.3 pointers | multiple-step claim location recorded |
| CLM-14 | IFGT information dynamics and VED closure dynamics are joined by a unified \(C(x,\tau)\) equation | [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md) | equations (4.1), (5.1)–(5.3) | related branch; individual solution identification stated outside scope | internal section derivation | related-branch claim, not a `docs/core_equations.md` entry |
| CLM-15 | finite graph registration can produce topology / metric-readability windows in a model family | [dimensionality module](../../dimensionality-working-note/README.md), [working note II](../../dimensionality-working-note/README_II_ja.md) | model-specific \(\Delta V,\Delta E,\Delta\beta_1\), graph-distance constructions | explicitly working-note / v24 model-family scope | experiment logs and scripts linked by module | current symbol reuse and bounded claim only; not promoted to VED-core equation |
| CLM-16 | stable fixed points of the self-referential \(\rho_i\) equation correspond to persistent physical structure | [causal logs and time](../../paper/vol1/sections/causal_logs_time.tex), [overview](../../docs/00_overview.md) | fixed-point equation in \(\rho_i\) | Vol.1 / overview | source assertion adjacent to equation | claim located; stability conditions and evidence not assessed here |

### 7.1 Source-level claim strength labels located

[Claim status](../../docs/navigation/claim_status.md) distinguishes:

- Level 0: foundational stance
- Level 1: working formalism
- Level 2: structural reinterpretation
- Level 3: exploratory physical reconstruction
- Level 4: application-layer account

It places difference / non-closure at Level 0, \(C_{ij}\) and the generative sequence at Level 1,
time / space at Level 2, and gravity / Standard-Model-like reconstruction at Level 3. This is the
repository's own reading guide. The present inventory records that label without converting it into a
validity or evidence verdict.

---

## 8. Missing or unresolved source identities

1. **\(C_{ij}\) identity:** Vol.1 and `docs/core_equations.md` call \(C_{ij}\) a causal log;
   top README, generative-sequence navigation, and AI Spine call it closure degree and distinguish an
   accumulated causal log from it. No unique repository-wide reconciliation was located.
2. **Difference glyph:** Vol.1 writes primitive difference as \(\delta\); IFGT writes VED difference
   source as \(\Delta\). No explicit source map \(\delta\leftrightarrow\Delta\) was located.
3. **\(\nabla\Delta\):** no exact current expression was located in the required source set.
4. **\(t\) in \(d\tau_i/dt\):** the Vol.1 causal-logs section uses but does not locally define it.
   IFGT defines an effective external \(t\), but source identity with the Vol.1 symbol is unresolved.
5. **Discrete-to-continuum \(C\):** no explicit \(C_{ij}\mapsto C(x,\tau)\) map was located.
6. **Discrete-to-continuum \(J\) and \(\rho\):** verbal coarse-grained correspondences exist, but no
   explicit scaling / interpolation / limiting map was located.
7. **Coarse metric:** an approximate endpoint expression and grouping / averaging wording are present;
   no explicit coarse-graining operator or uniqueness statement was located.
8. **\(\sigma\) identity:** Vol.1 log-generation rate, microscopic \(\dot\rho_i\), and IFGT mismatch
   / three-term \(\sigma\) are linked verbally but not by one explicit map.
9. **\(I\) as interaction:** no unique current VED-core symbol definition was located; bare \(I\) is
   information density in IFGT.
10. **Unique irreversible update equation:** the repository contains irreversible-history wording,
    a fixed-point selection equation, field evolution equations, and model-specific update records.
    No single equation labeled as the repository-wide irreversible update rule was located.
11. **\(L_{ab}\) in modified path cost:** the overview uses it but does not define it locally.
12. **\(L_{\mu\nu}[g]\):** the overview fixed-point metric expression uses it without a local definition.

“Unresolved” here means unresolved by this source-location pass. It does not mean inconsistent,
invalid, circular, or unresolvable.

---

## 9. What this inventory does not establish

This record does not show that:

- any equation is correct;
- any equation is wrong;
- any equation is circular;
- any representation preload is ontologically problematic;
- any generation claim is established;
- any generation claim is refuted;
- any symbol needs renaming;
- any equation needs revision;
- VED is validated;
- VED is refuted;
- `generative_law_methodology` validates VED.

It also does not classify any expression finally as a definition, law, constraint, update rule,
constitutive relation, measurement, derived observable, phenomenological approximation, or generative
equation. Where such words appear above, they are explicitly reported as source wording.

The following have likewise not been performed:

- legality or domain audit of \(\nabla\), \(\nabla\times\), derivatives, path metrics, or tensor notation;
- preload / circularity audit;
- derivation reconstruction;
- evidence-quality or claim-burden audit;
- comparison against external mathematics or physics;
- revision planning.

---

## 10. Handoff to 02

The future `02_equation_role_audit_v0.1_ja.md` receives the following inventory groups without a
preassigned verdict.

### 10.1 Expressions with clear source labels

- “causal log equation” \(C_{ij}=1-e^{-\lambda\rho_iH_{ij}}\)
- “log density” \(\rho_i=\sum_jC_{ij}\)
- “log-flow” \(J_{ij}=C_{ij}-C_{ji}\)
- “continuity equation” \(\partial_t\rho+\nabla\cdot\mathbf J=\sigma\)
- “vorticity” \(\omega=\nabla\times\mathbf J\)
- “closure energy” \(E(A)\)
- “distance” \(d_{ij}=-\log\widetilde S_{ij}\)
- IFGT “basic equation” and “unified equation”

These are source labels, not accepted role classifications.

### 10.2 Expressions with role ambiguity or incomplete local specification

- \(\nabla\delta\), \(J\sim-\nabla\delta\)
- \(d\tau_i/dt=\rho_i\)
- \(L\sim|\omega|\)
- non-closure inequality and barrier expression
- discrete / continuum passage for \(C,J,\rho\)
- metric coarse-graining expression
- gravity-modified path cost and overview fixed-point metric expression
- IFGT \(t\)-form with ellipsis

### 10.3 Multiple-use / multiple-definition symbols

- \(C_{ij}\), \(C\)
- \(\delta,\Delta\)
- \(J\), \(\rho\), \(\sigma\), \(\tau\)
- \(A_i,A_{ij}\)
- \(\Phi(A),\Phi\)
- \(g,g_{\mu\nu}\)
- \(L,L_{ab}\)

### 10.4 Discrete / continuum pairs

- \(C_{ij}\) / \(C(x,\tau)\)
- \(J_{ij}\) / \(\mathbf J(x)\) / IFGT \(J,J_C\)
- \(\rho_i\) / continuum \(\rho\)
- weighted-network \(d_{ij}\) / coarse \(g_{\mu\nu}\)

### 10.5 Expressions adjacent to strong generation / emergence wording

- difference-to-gradient / flow chain
- \(C_{ij}\) selection and fixed-point persistence
- local-time equation and \(\sigma>0\) statement
- vorticity-to-closure sequence
- distance / metric / space statements
- particle / mass statements
- closure-density / gravity statements
- IFGT unified equation and its listed possible solution classes

02 may classify roles only after reading the cited sources and preserving these source identities.
It must not silently normalize the conflicts recorded here.

---

## 11. Closure / current audit status

| Record | Status |
| --- | --- |
| `00_connection_record_v0.1_ja.md` | **COMPLETE** |
| `01_equation_inventory_v0.1_ja.md` | **COMPLETE** |
| `02_equation_role_audit_v0.1_ja.md` | **NOT STARTED** |
| `03_preload_and_circularity_audit_v0.1_ja.md` | **NOT STARTED** |
| `04_generation_claim_evidence_audit_v0.1_ja.md` | **NOT STARTED** |
| `05_revision_candidates_v0.1_ja.md` | **NOT STARTED** |
| `06_final_audit_record_v1.0_ja.md` | **NOT STARTED** |
| VED core revision | **NOT STARTED** |

Current audit stage:

\[
\boxed{\text{01 COMPLETE / 02 NOT STARTED}}
\]

The hard gate remains **inventory before judgment**. This record closes phase 01 only and does not
authorize phase 02 conclusions or any VED modification.

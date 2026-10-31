# VED equation role audit v0.1

## 1. Status

Status:

- repository-internal equation-role audit
- audit phase: **02 COMPLETE**
- role classification only
- not a preload or circularity audit
- not an operator-legality or derivation-validity audit
- not an evidence-sufficiency or physical-emergence audit
- not a revision proposal
- not a VED rewrite or validation
- [`00_connection_record_v0.1_ja.md`](./00_connection_record_v0.1_ja.md): **COMPLETE**
- [`01_equation_inventory_v0.1_ja.md`](./01_equation_inventory_v0.1_ja.md): **COMPLETE**
- `03_preload_and_circularity_audit_v0.1_ja.md`: **NOT STARTED**
- `04_generation_claim_evidence_audit_v0.1_ja.md`: **NOT STARTED**
- `05_revision_candidates_v0.1_ja.md`: **NOT STARTED**
- `06_final_audit_record_v1.0_ja.md`: **NOT STARTED**
- VED core revision: **NOT STARTED**
- `generative_law_methodology`: **CLOSED / STOP-A**

本記録は、01 inventoryの49 entriesについて、source上で各expressionが担う役割を分類する。
ここでのconfidenceはsource wordingからroleを読み取れる明確さだけを表し、式の正しさや
証拠の強さを表さない。

---

## 2. Scope and basis

### 2.1 Audit question

> 01で所在を確定した現行VED equations / expressionsは、repository source上で何を定義し、
> 何を構成し、何を制約し、何を更新し、どの強い生成・創発claimに隣接しているか。

Primary basisは[01 equation inventory](./01_equation_inventory_v0.1_ja.md)である。role判定に必要な
範囲で、そこに記載されたVol.1 sections、core docs、navigation、IFGT recordを再読した。
外部sourceと一般教科書知識は用いていない。01のsource identity、notation conflict、currentness
uncertaintyは正規化しない。

### 2.2 Role vocabulary

Primary / secondary rolesには次だけを用いる。

- **DEFINITION**
- **DERIVED CONSTRUCTION**
- **LAW-LIKE CONSTRAINT**
- **UPDATE / EVOLUTION RULE**
- **BALANCE / CONTINUITY RELATION**
- **CONSTITUTIVE / CLOSURE RELATION**
- **PHENOMENOLOGICAL / EFFECTIVE ANSATZ**
- **OBSERVABLE / MEASUREMENT CONSTRUCTION**
- **ROLE UNRESOLVED**

**GENERATION CLAIM ADJACENT**はroleではなく、近接proseが`generated`、`emerges`、
`produces`、`source of`、`gives rise to`等を用いる場合の別tagである。

### 2.3 Classification controls

- sourceの明示labelとusageをsyntaxより優先する。
- equals sign、derivative、inequality、PDEだけからroleを決めない。
- 一つのexpressionが複数のsource functionを持つ場合はsecondary roleを記録する。
- repository-wideで意味またはroleが衝突する場合は無理に統合せず**ROLE UNRESOLVED**とする。
- equation roleと近接claimを分離する。

したがって、例えば

\[
\frac{d\tau_i}{dt}=\rho_i
\]

はsourceが「time is defined」と述べるためprimary roleを**DEFINITION**とするが、
「time is generated」は別のclaim-adjacency recordである。同様にdistanceのdefinitionと
space-emergence wordingも別に記録する。

---

## 3. Primary role table

`Source agreement`と`Role confidence`はsource記述の状態だけを表す。

### 3.1 Difference / gradient

| ID | Expression | Primary source role wording | Primary role | Secondary role(s) | Generation-claim adjacent? | Source agreement | Role confidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DIF-01 | \(\delta\) | Vol.1ではdifference / asymmetry、overviewでは\(\delta S\)のvariationとして使用 | **ROLE UNRESOLVED** | — | NO | **SOURCE CONFLICT** | **HIGH** | 同じglyphの二usageを単一roleへ統合しない |
| DIF-02 | \(\Delta\) | IFGTではVED difference source / driver、他sourceではclosure distanceまたはfinite increment | **ROLE UNRESOLVED** | — | YES | **SOURCE CONFLICT** | **HIGH** | source別usageのroleが異なる |
| DIF-03 | \(\nabla\delta\), \(J\sim-\nabla\delta\) | “asymmetry implies a gradient; a gradient drives a flow”というminimal chain | **DERIVED CONSTRUCTION** | — | YES | **SINGLE SOURCE ONLY** | **MODERATE** | implication / proportionality chainとして使用されるがdomainは03の対象 |
| DIF-04 | \(\nabla\Delta\) | exact expressionは01で未発見 | **ROLE UNRESOLVED** | — | NO | **ROLE UNRESOLVED** | **LOW** | 所在しないexpressionへroleを付与しない |
| DIF-05 | gradient（symbolなし） | navigationのgenerated stage / directional structure | **ROLE UNRESOLVED** | — | YES | **PARTIALLY CONSISTENT** | **LOW** | \(\nabla\delta\)とのsource-level同一化は未確立 |

### 3.2 History / closure / causal record

| ID | Expression | Primary source role wording | Primary role | Secondary role(s) | Generation-claim adjacent? | Source agreement | Role confidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LOG-01 | \(H_{ij}\ge0\) | “causal history”—total accumulated influence | **DEFINITION** | — | NO | **CONSISTENT** | **HIGH** | quantityのsource definitionを記録 |
| LOG-02 | \(C_{ij}\in[0,1)\) | paper / core equationsはcausal log、README / navigationはclosure degree | **ROLE UNRESOLVED** | — | YES | **SOURCE CONFLICT** | **HIGH** | repository-wide identity conflictにより一意roleを付けない |
| LOG-03 | \(C_{ij}=1-\exp(-\lambda\rho_iH_{ij})\) | “causal log equation” / “self-referential selection equation” | **CONSTITUTIVE / CLOSURE RELATION** | **LAW-LIKE CONSTRAINT** | YES | **PARTIALLY CONSISTENT** | **MODERATE** | named quantitiesを関係づけ、fixed-point条件にも入る。validityは未判定 |
| LOG-04 | \(\rho_i=\sum_jC_{ij}\) | “Define the log density at node \(i\)” | **DEFINITION** | **DERIVED CONSTRUCTION** | YES | **CONSISTENT** | **HIGH** | core summaryではlocal time generation rateとも呼ばれる |
| LOG-05 | \(\lambda>0\) | selection sensitivity / equation sectionのsole external parameter | **DEFINITION** | — | NO | **CONSISTENT** | **HIGH** | “sole”は当該formulationのsource wording |
| LOG-06 | \(\rho_i=\sum_j[1-\exp(-\lambda\rho_iH_{ij})]\) | substitution後のself-referential fixed-point equation | **LAW-LIKE CONSTRAINT** | **CONSTITUTIVE / CLOSURE RELATION** | YES | **CONSISTENT** | **HIGH** | stable solutionsへの条件として使用 |
| LOG-07 | \(\dot\rho_i=\lambda\rho_iB_i/(1-\lambda A_i)\) | “Taking the time derivative ... yields”; log-generation rate | **DERIVED CONSTRUCTION** | **UPDATE / EVOLUTION RULE** | YES | **SINGLE SOURCE ONLY** | **HIGH** | sourceは\(C_{ij}\)式からの導出として提示 |

### 3.3 Time-related notation

| ID | Expression | Primary source role wording | Primary role | Secondary role(s) | Generation-claim adjacent? | Source agreement | Role confidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TIM-01 | \(t\) | Vol.1ではderivative variable、IFGTではfixed-background effective descriptionのexternal order parameter | **ROLE UNRESOLVED** | — | NO | **SOURCE CONFLICT** | **HIGH** | source identityが未解決 |
| TIM-02 | \(\tau_i\) | time at node \(i\) / observational time | **DEFINITION** | **OBSERVABLE / MEASUREMENT CONSTRUCTION** | YES | **CONSISTENT** | **HIGH** | physical claimの十分性は04へ送る |
| TIM-03 | \(d\tau_i/dt=\rho_i\) | “Time ... is defined as the rate at which causal logs accumulate” | **DEFINITION** | **UPDATE / EVOLUTION RULE**; **OBSERVABLE / MEASUREMENT CONSTRUCTION** | YES | **CONSISTENT** | **HIGH** | generation wordingはroleと分離 |
| TIM-04 | \(\tau\), \(\tau_{\mathrm{VED}}\) | IFGTがinformational timeとgenerative timeを別々に定義・区別 | **DEFINITION** | **OBSERVABLE / MEASUREMENT CONSTRUCTION** | YES | **SINGLE SOURCE ONLY** | **HIGH** | “dynamically isomorphic” claimはrole分類ではない |

### 3.4 Symmetric / antisymmetric decomposition

| ID | Expression | Primary source role wording | Primary role | Secondary role(s) | Generation-claim adjacent? | Source agreement | Role confidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DEC-01 | \(S_{ij}=\tfrac12(C_{ij}+C_{ji})\) | “decompose ... into symmetric ... parts”; spatial component wording | **DERIVED CONSTRUCTION** | **DEFINITION** | YES | **CONSISTENT** | **HIGH** | spatial interpretationはnearby claim |
| DEC-02 | \(A_{ij}=\tfrac12(C_{ij}-C_{ji})\) | “decompose ... into ... antisymmetric parts”; temporal / causal component wording | **DERIVED CONSTRUCTION** | **DEFINITION** | YES | **CONSISTENT** | **HIGH** | \(A_i\)とは別quantity |

### 3.5 Flow / balance

| ID | Expression | Primary source role wording | Primary role | Secondary role(s) | Generation-claim adjacent? | Source agreement | Role confidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FLW-01 | \(J_{ij}=C_{ij}-C_{ji}=2A_{ij}\) | antisymmetric component “defines the log-flow” | **DEFINITION** | **DERIVED CONSTRUCTION** | YES | **CONSISTENT** | **HIGH** | flow claimとdefinitionを分離 |
| FLW-02 | \(\mathbf J(x)\) | \(J_{ij}\) “becomes a vector field” in the coarse-grained limit | **DERIVED CONSTRUCTION** | — | YES | **PARTIALLY CONSISTENT** | **MODERATE** | explicit coarse-graining mapは01で未発見 |
| FLW-03 | continuum \(\rho\) | continuity equation内のlog density; exact function signature未発見 | **ROLE UNRESOLVED** | — | NO | **ROLE UNRESOLVED** | **LOW** | node densityからのrole transferを推測しない |
| FLW-04 | \(\partial_t\rho+\nabla\cdot\mathbf J=\sigma\) | source labels it “continuity equation” and log-density evolution | **BALANCE / CONTINUITY RELATION** | **UPDATE / EVOLUTION RULE** | YES | **PARTIALLY CONSISTENT** | **HIGH** | IFGT analogous equationとはsource identityが異なる |
| FLW-05 | \(\sigma\ge0\), \(\sigma>0\) | Vol.1: log-generation rate; IFGT: differently decomposed generation term | **DEFINITION** | — | YES | **SOURCE CONFLICT** | **MODERATE** | source-specific definitionを一つへ統合しない |
| FLW-06 | \(\mathbf J=\mathbf J_{\rm rot}+\mathbf J_{\rm pot}\) | source labels it “Helmholtz decomposition” | **DERIVED CONSTRUCTION** | **DEFINITION** | YES | **SINGLE SOURCE ONLY** | **HIGH** | structure-formation wordingが隣接する |

### 3.6 Rotation / vorticity / enclosure

| ID | Expression | Primary source role wording | Primary role | Secondary role(s) | Generation-claim adjacent? | Source agreement | Role confidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENC-01 | \(\omega=\nabla\times\mathbf J\) | “Define the vorticity of the log-flow” | **DEFINITION** | **DERIVED CONSTRUCTION** | YES | **CONSISTENT** | **HIGH** | circulation / stable-structure wordingはadjacency |
| ENC-02 | \(L\sim\lvert\omega\rvert\) | local intensity “defines the closure density” | **DEFINITION** | **DERIVED CONSTRUCTION** | YES | **CONSISTENT** | **HIGH** | proportionalityの仕様・妥当性はここで判定しない |
| ENC-03 | \(L<L_{\max}\) | source labels it “non-closure constraint” at all times | **LAW-LIKE CONSTRAINT** | — | NO | **CONSISTENT** | **HIGH** | complete closureの解釈はrole外 |
| ENC-04 | \(B(L)=-\kappa_B\log(1-L/L_{\max})\) | “effective closure barrier” / “phenomenological encoding” | **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | **CONSTITUTIVE / CLOSURE RELATION** | NO | **CONSISTENT** | **HIGH** | microscopic originを主張しないというsource restrictionを維持 |
| ENC-05 | \(\Delta_k=L_{\max}-L_k\) | “closure distance” of a stable configuration | **DEFINITION** | **OBSERVABLE / MEASUREMENT CONSTRUCTION** | NO | **CONSISTENT** | **HIGH** | difference-source \(\Delta\)とは別usage |
| ENC-06 | \(E(A)=\alpha\lvert\sum\vec e_i\rvert^2-\beta\Phi(A)+\gamma\lvert A\rvert+B(L(A))\) | “Define the closure energy of a configuration” | **DEFINITION** | **CONSTITUTIVE / CLOSURE RELATION** | YES | **CONSISTENT** | **HIGH** | particle local-minimum claimは別tag |
| ENC-07 | \(m_k\propto d^2E/dL^2\rvert_{L_k}\sim\kappa_B/\Delta_k^2\) | “Within the phenomenological barrier approximation this yields” | **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | **DERIVED CONSTRUCTION** | YES | **PARTIALLY CONSISTENT** | **HIGH** | mass claimのevidenceは04へ送る |

### 3.7 Distance / geometry

| ID | Expression | Primary source role wording | Primary role | Secondary role(s) | Generation-claim adjacent? | Source agreement | Role confidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GEO-01 | \(\widetilde S_{ij}=\max_\gamma\prod_{(ab)\in\gamma}S_{ab}\) | source: “define its propagation strength” | **DEFINITION** | **DERIVED CONSTRUCTION**; **OBSERVABLE / MEASUREMENT CONSTRUCTION** | NO | **CONSISTENT** | **HIGH** | path policyのauditは03へ送る |
| GEO-02 | \(d_{ij}=-\log\widetilde S_{ij}=\min_\gamma\sum(-\log S_{ab})\) | “The distance between nodes is” / shortest-path problem | **DEFINITION** | **DERIVED CONSTRUCTION**; **OBSERVABLE / MEASUREMENT CONSTRUCTION** | YES | **CONSISTENT** | **HIGH** | space claimとmetric propertiesは別問題 |
| GEO-03 | \(d_{ij}=\min_\gamma\sum[-\log S_{ab}+\epsilon L_{ab}]\) | overview: “unified distance becomes” with closure-density path cost | **DEFINITION** | **OBSERVABLE / MEASUREMENT CONSTRUCTION**; **CONSTITUTIVE / CLOSURE RELATION** | YES | **SINGLE SOURCE ONLY** | **MODERATE** | \(L_{ab}\) source identityは01で未解決 |
| GEO-04 | \(d(x,y)^2\approx g_{\mu\nu}(x)(x^\mu-y^\mu)(x^\nu-y^\nu)\) | “In a coarse-grained limit ... smooth effective distance” | **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | **OBSERVABLE / MEASUREMENT CONSTRUCTION** | YES | **CONSISTENT** | **HIGH** | approximationとspace-emergence proseを分離 |
| GEO-05 | \(g_{\mu\nu}=\text{effective description of }d_{ij}\) | metric tensor is an “effective description” / “coarse-grained approximation” | **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | **DERIVED CONSTRUCTION**; **OBSERVABLE / MEASUREMENT CONSTRUCTION** | YES | **CONSISTENT** | **HIGH** | tensorのlegality・physical meaningは未判定 |
| GEO-06 | \(\nabla^2\Psi\propto L\), \(g=-\nabla\Psi\) | overview: closure density as source of gravitational potential / field | **CONSTITUTIVE / CLOSURE RELATION** | **DERIVED CONSTRUCTION** | YES | **SINGLE SOURCE ONLY** | **MODERATE** | 二式の細部roleは異なるがoverviewが一組で提示 |
| GEO-07 | \(g_{\mu\nu}=g^{(0)}_{\mu\nu}+\alpha_GL_{\mu\nu}[g]\) | overview labels it “VED fixed-point equation” | **LAW-LIKE CONSTRAINT** | **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | YES | **SINGLE SOURCE ONLY** | **MODERATE** | weak-gravity linearization wordingが隣接する |

### 3.8 IFGT-related quantities and equations

| ID | Expression | Primary source role wording | Primary role | Secondary role(s) | Generation-claim adjacent? | Source agreement | Role confidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IFG-01 | \(I\) | “information density” is introduced / defined as persistent trace density | **DEFINITION** | — | NO | **SINGLE SOURCE ONLY** | **HIGH** | bare \(I\) as interactionは01で未発見 |
| IFG-02 | \(I=f(1-C)\), later \(I=1-C\) | first a relation with nondecreasing \(f\); later an explicit linear assumption / approximation | **CONSTITUTIVE / CLOSURE RELATION** | **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | NO | **PARTIALLY CONSISTENT** | **HIGH** | general relationとlinear approximationを同一定義にしない |
| IFG-03 | \(C(x,\tau)\) | “closure-degree field” in the unified equation | **DEFINITION** | — | YES | **SINGLE SOURCE ONLY** | **HIGH** | discrete \(C_{ij}\)とのmapはrole外 |
| IFG-04 | \(\partial_\tau I+\nabla\cdot J=\sigma\) | “basic equation” for information-density evolution; transport plus generation | **BALANCE / CONTINUITY RELATION** | **UPDATE / EVOLUTION RULE** | YES | **SINGLE SOURCE ONLY** | **HIGH** | VED continuity equationとのsimilarityはidentityではない |
| IFG-05 | \(J=-D\nabla I+\mu F_I\), \(F_I=-\nabla\Phi=\alpha\nabla C\) | “information flow is prescribed by” density gradient and potential | **CONSTITUTIVE / CLOSURE RELATION** | **DERIVED CONSTRUCTION** | NO | **SINGLE SOURCE ONLY** | **HIGH** | source calls second equation a constraint-potential-gradient term |
| IFG-06 | \(\sigma_{\rm drive}\), \(\sigma_{\rm dissip}\), \(\sigma_{\rm barrier}\) | source expands \(\sigma\) into drive, dissipation, and effective barrier contributions | **CONSTITUTIVE / CLOSURE RELATION** | **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | YES | **SINGLE SOURCE ONLY** | **HIGH** | barrier term is explicitly phenomenological |
| IFG-07 | unified \(C(x,\tau)\) equation (5.2) | source calls it a single evolution equation / unified equation | **UPDATE / EVOLUTION RULE** | **BALANCE / CONTINUITY RELATION**; **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | YES | **SINGLE SOURCE ONLY** | **HIGH** | listed possible solution classes are nearby claims, not roles |
| IFG-08 | \(J_C=-D\nabla C-\mu\alpha C\nabla C\) | closure-flow expression after the linear \(I=1-C\) assumption | **CONSTITUTIVE / CLOSURE RELATION** | **DERIVED CONSTRUCTION**; **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | NO | **SINGLE SOURCE ONLY** | **HIGH** | linear assumption is explicitly source-scoped |

### 3.9 Other current core-facing expressions

| ID | Expression | Primary source role wording | Primary role | Secondary role(s) | Generation-claim adjacent? | Source agreement | Role confidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OTH-01 | \(C\to J\to\omega\to L\to g\) | core equations calls it a compact formal generative chain | **ROLE UNRESOLVED** | — | YES | **PARTIALLY CONSISTENT** | **LOW** | sequence recordであり、各arrowの単一equation roleは示されない |
| OTH-02 | \(L\sim\lvert\omega\rvert\to\) particle / gravity wording | several equations and prose participate; no unique generation equation located | **ROLE UNRESOLVED** | — | YES | **PARTIALLY CONSISTENT** | **LOW** | bundleを一つのroleへ圧縮しない |
| OTH-03 | \(\partial_tC+\nabla\cdot J_C=\cdots\) | IFGT: fixed-background regionで使えるeffective description | **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | **BALANCE / CONTINUITY RELATION**; **UPDATE / EVOLUTION RULE** | YES | **SINGLE SOURCE ONLY** | **HIGH** | \(\tau\)-formをbasic、\(t\)-formをeffectiveとするsource区別を保持 |

---

## 4. Role clusters

Primary role clusterを先に示し、secondary roleへの所属は括弧内で補う。

### 4.1 Definitions

Primary: LOG-01, LOG-04, LOG-05, TIM-02, TIM-03, TIM-04, FLW-01, FLW-05,
ENC-01, ENC-02, ENC-05, ENC-06, GEO-01, GEO-02, GEO-03, IFG-01, IFG-03.

Secondary: DEC-01, DEC-02, FLW-06.

### 4.2 Derived constructions

Primary: DIF-03, LOG-07, DEC-01, DEC-02, FLW-02, FLW-06.

Secondary: LOG-04, FLW-01, ENC-01, ENC-02, ENC-07, GEO-01, GEO-02, GEO-05,
GEO-06, IFG-05, IFG-08.

### 4.3 Constraints

Primary: LOG-06, ENC-03, GEO-07.

Secondary: LOG-03.

### 4.4 Updates / evolution

Primary: IFG-07.

Secondary: LOG-07, TIM-03, FLW-04, IFG-04, OTH-03.

### 4.5 Balance relations

Primary: FLW-04, IFG-04.

Secondary: IFG-07, OTH-03.

### 4.6 Constitutive / closure relations

Primary: LOG-03, GEO-06, IFG-02, IFG-05, IFG-06, IFG-08.

Secondary: LOG-06, ENC-04, ENC-06, GEO-03.

### 4.7 Effective / phenomenological expressions

Primary: ENC-04, ENC-07, GEO-04, GEO-05, OTH-03.

Secondary: GEO-07, IFG-02, IFG-06, IFG-07, IFG-08.

### 4.8 Measurement / observable constructions

Primary: none.

Secondary: TIM-02, TIM-03, TIM-04, ENC-05, GEO-01, GEO-02, GEO-03, GEO-04,
GEO-05.

ここでprimaryが0であることは、measurement roleが存在しないという意味ではない。sourceでの
主動詞がdefinitionまたはeffective descriptionであり、reading / distance / timeとしての使用を
secondaryに記録した結果である。

### 4.9 Generation-claim-adjacent expressions

DIF-02, DIF-03, DIF-05, LOG-02, LOG-03, LOG-04, LOG-06, LOG-07, TIM-02,
TIM-03, TIM-04, DEC-01, DEC-02, FLW-01, FLW-02, FLW-04, FLW-05, FLW-06,
ENC-01, ENC-02, ENC-06, ENC-07, GEO-02, GEO-03, GEO-04, GEO-05, GEO-06,
GEO-07, IFG-03, IFG-04, IFG-06, IFG-07, OTH-01, OTH-02, OTH-03.

### 4.10 Role-unresolved expressions

DIF-01, DIF-02, DIF-04, DIF-05, LOG-02, TIM-01, FLW-03, OTH-01, OTH-02.

---

## 5. Source conflicts affecting role classification

### 5.1 \(C_{ij}\)

Vol.1 paperと`docs/core_equations.md`は\(C_{ij}\)を、\(H_{ij}\)から選択・保持された
**causal log**とする。top README / generative sequence / AI Spineは\(C_{ij}\)を
**closure degree**またはrank-1 formal carrierとし、causal logをそのaccumulated traceとして
別に記述する。この差はsymbolのprimary roleと後続equationの読みに直接影響するため、LOG-02は
repository-wideで**ROLE UNRESOLVED**とした。reconciliationは提案しない。

### 5.2 \(\rho_i\)

Vol.1は\(\rho_i=\sum_jC_{ij}\)をlog densityとして明示定義する。`docs/core_equations.md`は同じ
quantityをlog densityかつlocal time generation rateと説明する。expressionのprimary roleは
definitionで一致するが、densityとrateのclaim-level usageは別に残る。

### 5.3 \(\sigma\)

Vol.1の\(\sigma\)はcontinuity equation内のlog-generation rateであり、external sourceではないと
説明される。IFGTの\(\sigma\)は現在のdifference chainとtrace structureのmismatchであり、drive、
dissipation、barrierへ分解される。FLW-05はsource-specific definitionの衝突を保持し、IFG-06は
IFGT内のconstitutive relationとして別分類した。

### 5.4 \(C\) / \(I\) in IFGT

IFGTは一般形\(I=f(1-C)\)を関係として置き、unified equationでは明示的に「linear assumption / 
approximation」\(I=1-C\)を採用する。従ってIFG-02はprimaryをconstitutive / closure relation、
linear special caseをsecondaryのphenomenological / effective ansatzとした。どちらか一方へ
repository-wideに正規化しない。

### 5.5 Time variables

- \(\tau_i\): Vol.1 node time / core summary observational time。
- \(\tau_{\mathrm{VED}}\): IFGTが区別して導入するgenerative time。
- \(\tau\): IFGT informational time。
- \(t\): Vol.1 derivative variable、IFGT fixed-background effective order parameter。

TIM-02〜04はsourceが各quantityを定義するためdefinitionと分類したが、これらのidentity、embedding、
physical interpretationはrole classificationから導かれない。TIM-01はsource identity unresolvedの
ままである。

### 5.6 Additional role-bearing conflicts

- \(\Delta\)はdifference source、closure distance、finite incrementでroleが異なる。
- \(J\)はminimal chain、discrete log-flow、coarse vector field、IFGT information flowでroleが異なる。
- \(A_{ij}\)と\(A_i\)、\(\Phi(A)\)とIFGT \(\Phi\)、\(g\)と\(g_{\mu\nu}\)はnotationだけで
  roleを移さない。

---

## 6. Generation-claim adjacency

この表は[01の16 claims](./01_equation_inventory_v0.1_ja.md#7-claim-location-inventory)を
引き継ぐ。`Role/claim conflation risk`は式のsource roleと近接する強いprose claimが同一視される
可能性であり、claim validityではない。

| Claim ID | Claim wording | Adjacent expression(s) | Expression role | Claim type wording | Role/claim conflation risk | Audit note |
| --- | --- | --- | --- | --- | --- | --- |
| CLM-01 | differenceからrank orderで後続構造が生じる | textual chain; \(C\to J\to\omega\to L\to g\) | **ROLE UNRESOLVED** sequence | “follow”, “generative chain” | **HIGH** | sequence表示は各arrowのroleや導出を単独では確定しない |
| CLM-02 | asymmetry gives gradient and flow | \(\nabla\delta\ne0\), \(J\sim-\nabla\delta\) | **DERIVED CONSTRUCTION** | “implies”, “drives” | **HIGH** | construction wordingとnecessity claimを分離 |
| CLM-03 | history is selectively retained as persistent structure | LOG-03, LOG-04 | **CONSTITUTIVE / CLOSURE RELATION**; **DEFINITION** | “generated by structure”, “selected into” | **MODERATE** | relation roleはendogenous selection claimの証拠評価ではない |
| CLM-04 | local / observational time is generated by accumulation | TIM-03 | **DEFINITION** with update / observable roles | “Generation of Time”, “defined as” | **HIGH** | time definitionとphysical generation claimを分離 |
| CLM-05 | irreversibility is structural / built into time definition | TIM-03 | **DEFINITION** with update role | “built into the definition” | **HIGH** | definitional monotonicityとphysical irreversibilityは同じrole claimではない |
| CLM-06 | antisymmetric causal log produces directional flow | FLW-01 | **DEFINITION** / **DERIVED CONSTRUCTION** | “defines”, “motion arises” | **MODERATE** | log-flow definitionとpropagation claimを分離 |
| CLM-07 | \(\sigma>0\) corresponds to time being generated | FLW-04, FLW-05 | **BALANCE / CONTINUITY RELATION**; **DEFINITION** | explicit biconditional wording | **HIGH** | balance equationのroleはtime-generation identificationを確立しない |
| CLM-08 | vorticity enables enclosure / persistent structure | ENC-01, ENC-02, FLW-06 | **DEFINITION** / **DERIVED CONSTRUCTION** | “responsible for formation”, “source” | **HIGH** | curl / decomposition roleとstable-structure claimを分離 |
| CLM-09 | triangular closure is minimal; particle is closure-energy minimum | ENC-06 | **DEFINITION** / **CONSTITUTIVE / CLOSURE RELATION** | topological result; particle definition | **HIGH** | energy definitionとminimality / particle claimを分離 |
| CLM-10 | distance is induced from connectivity | DEC-01, GEO-01, GEO-02 | **DERIVED CONSTRUCTION**; **DEFINITION** | “distance is”, “resistance to propagation” | **MODERATE** | distance definitionとinterpretive wordingを分離 |
| CLM-11 | metric / space is coarse-grained log-distance structure | GEO-04, GEO-05 | **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | “emergence of space”, “effective description” | **HIGH** | effective metric expressionとphysical-space claimを分離 |
| CLM-12 | closure density modifies distance and sources gravity | GEO-03, GEO-06, GEO-07 | **DEFINITION**; **CONSTITUTIVE / CLOSURE RELATION**; **LAW-LIKE CONSTRAINT** | “gravity is distortion”, “source” | **HIGH** | three role typesを一つのgravity claimへ圧縮しない |
| CLM-13 | closure density is associated with particles and mass | ENC-02, ENC-06, ENC-07 | **DEFINITION**; **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | “source of particle structure”, effective mass | **HIGH** | closure-density definitionとphenomenological mass relationを分離 |
| CLM-14 | IFGT and VED are joined by unified \(C(x,\tau)\) equation | IFG-03, IFG-07, IFG-08 | **DEFINITION**; **UPDATE / EVOLUTION RULE**; **CONSTITUTIVE / CLOSURE RELATION** | “unified equation”, “connects” | **HIGH** | naming an equation unified does not settle cross-theory identification |
| CLM-15 | finite graph registration produces topology / metric-readable windows | model-specific dimensionality expressions | working-note constructions; outside the 49 core roles | “produce”, bounded model-family scope | **MODERATE** | related working-note claimをVED core roleへ移さない |
| CLM-16 | stable fixed points correspond to persistent physical structure | LOG-06 | **LAW-LIKE CONSTRAINT** | “correspond to” | **HIGH** | fixed-point roleとphysical identificationを分離 |

---

## 7. Required summaries

### Summary A — primary-role counts

| Primary role | Count |
| --- | ---: |
| **DEFINITION** | 17 |
| **DERIVED CONSTRUCTION** | 6 |
| **LAW-LIKE CONSTRAINT** | 3 |
| **UPDATE / EVOLUTION RULE** | 1 |
| **BALANCE / CONTINUITY RELATION** | 2 |
| **CONSTITUTIVE / CLOSURE RELATION** | 6 |
| **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | 5 |
| **OBSERVABLE / MEASUREMENT CONSTRUCTION** | 0 |
| **ROLE UNRESOLVED** | 9 |
| **Total** | **49** |

Thirty-two expressions have one or more secondary roles. A secondary role records a second source
function; it does not duplicate the primary-role count.

### Summary B — unresolved / conflict

| ID | Expression | Conflict / ambiguity | Source(s) |
| --- | --- | --- | --- |
| DIF-01 | \(\delta\) | difference / asymmetry versus action variation | Vol.1 minimal axiom; overview / claims |
| DIF-02 | \(\Delta\) | difference source versus closure distance / increments | IFGT; closure; dimensionality notes |
| DIF-04 | \(\nabla\Delta\) | exact expression not located | repository search recorded in 01 |
| DIF-05 | gradient stage | navigation stage not explicitly identified with \(\nabla\delta\) | navigation; Vol.1 |
| LOG-02 | \(C_{ij}\) | causal log versus closure degree / accumulated trace identity | Vol.1 / core equations; README / navigation / AI Spine |
| TIM-01 | \(t\) | derivative variable versus explicit effective external order parameter | Vol.1; IFGT |
| FLW-03 | continuum \(\rho\) | function signature and map from \(\rho_i\) not located | Vol.1 flow; core docs |
| OTH-01 | \(C\to J\to\omega\to L\to g\) | sequence has no single equation role | core equations; navigation |
| OTH-02 | \(L\sim\lvert\omega\rvert\to\) particle / gravity | multiple equations and claims bundled | flow; closure; overview |

### Summary C — high claim-adjacency cases

| Expression | Adjacent claim | Primary role | Why separated |
| --- | --- | --- | --- |
| \(\nabla\delta\ne0\), \(J\sim-\nabla\delta\) | difference necessarily gives flow | **DERIVED CONSTRUCTION** | construction role does not itself settle necessity |
| \(d\tau_i/dt=\rho_i\) | time and irreversibility are generated | **DEFINITION** | source definition and physical generation claim have different evidence burdens |
| \(\partial_t\rho+\nabla\cdot J=\sigma\) | \(\sigma>0\) means time is generated | **BALANCE / CONTINUITY RELATION** | balance form and time identification are different claims |
| \(\omega=\nabla\times J\), \(L\sim\lvert\omega\rvert\) | vorticity produces persistent enclosure | **DEFINITION** | derived quantity names do not by themselves establish persistence |
| \(E(A)\) | particle is a stable / minimal enclosure | **DEFINITION** | defining an energy and identifying a physical object are separate |
| \(d_{ij}=-\log\widetilde S_{ij}\) | space emerges from propagation resistance | **DEFINITION** | mathematical distance construction and physical space claim are separate |
| coarse \(g_{\mu\nu}\) expressions | metric / space emerges under coarse-graining | **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | effective relation and physical interpretation are separate |
| gravity expressions | closure density produces gravitational behavior | mixed: constitutive relation / constraint | adjacent equations do not share one role |
| mass scaling | closure distance gives effective mass | **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | source-scoped approximation and physical identification differ |
| IFGT equation (5.2) | single field may generate broad solution classes | **UPDATE / EVOLUTION RULE** | evolution role does not establish listed solution identifications |
| fixed-point equation | stable roots correspond to persistent physical structure | **LAW-LIKE CONSTRAINT** | solution constraint and physical correspondence are separate |

---

## 8. Handoff to 03

The future `03_preload_and_circularity_audit_v0.1_ja.md` receives the following priority groups.
These are inspection targets only; no preload, circularity, or legality verdict is made here.

### 8.1 Operator-bearing expressions

- DIF-03: \(\nabla\delta\), \(J\sim-\nabla\delta\)
- FLW-04: \(\nabla\cdot\mathbf J\)
- FLW-06: Helmholtz decomposition and its divergence / curl conditions
- ENC-01: \(\nabla\times\mathbf J\)
- GEO-06: \(\nabla^2\Psi\), \(g=-\nabla\Psi\)
- IFG-04〜08: IFGT divergence and gradient expressions

### 8.2 Time-parameter-bearing expressions

- TIM-03: \(d\tau_i/dt\)
- LOG-07: \(\dot\rho_i\), \(\dot H_{ij}\)
- FLW-04: \(\partial_t\rho\)
- IFG-04 / IFG-07: \(\partial_\tau I\), \(\partial_\tau C\)
- OTH-03: effective \(t\)-form

### 8.3 Path / metric expressions

- GEO-01: \(\widetilde S_{ij}\)
- GEO-02: log / shortest-path distance
- GEO-03: modified path cost
- GEO-04 / GEO-05: coarse metric expressions

### 8.4 Discrete-to-continuum pairs

- LOG-02 / IFG-03: \(C_{ij}\to C(x,\tau)\)
- FLW-01 / FLW-02 / IFG-05 / IFG-08: \(J_{ij}\to\mathbf J(x)\to J,J_C\)
- LOG-04 / FLW-03: \(\rho_i\to\rho\)
- GEO-02 / GEO-04 / GEO-05: network distance to coarse metric

### 8.5 Higher-structure expressions

- FLW-06: Helmholtz decomposition
- GEO-04 / GEO-05: \(g_{\mu\nu}\)
- GEO-07: fixed-point metric equation

Handoff does not assert that these expressions preload any structure, are circular, are illegal, or
require revision. Those questions remain gated to phase 03 and later phases.

---

## 9. What this role audit does not establish

This record does not establish:

- whether any operator is legal on the stated domain;
- whether any expression preloads background structure;
- whether any definition or derivation is circular;
- whether any displayed derivation is valid;
- whether any metric, fixed point, decomposition, or PDE has the claimed properties;
- whether evidence near any generation / emergence claim is sufficient;
- whether any mathematical construction has a physical interpretation;
- whether any expression should be kept, revised, split, renamed, or retired;
- whether VED or IFGT is validated or refuted.

Primary role, secondary role, source agreement, and confidence are documentary classifications only.

---

## 10. Closure / current audit status

| Record | Status |
| --- | --- |
| `00_connection_record_v0.1_ja.md` | **COMPLETE** |
| `01_equation_inventory_v0.1_ja.md` | **COMPLETE** |
| `02_equation_role_audit_v0.1_ja.md` | **COMPLETE** |
| `03_preload_and_circularity_audit_v0.1_ja.md` | **NOT STARTED** |
| `04_generation_claim_evidence_audit_v0.1_ja.md` | **NOT STARTED** |
| `05_revision_candidates_v0.1_ja.md` | **NOT STARTED** |
| `06_final_audit_record_v1.0_ja.md` | **NOT STARTED** |
| VED core revision | **NOT STARTED** |

Current audit stage:

\[
\boxed{\text{02 COMPLETE / 03 NOT STARTED}}
\]

The hard gate remains **role before revision**. Phase 03 has not begun.

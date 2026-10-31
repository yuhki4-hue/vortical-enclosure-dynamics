# VED preload / circularity audit v0.1

## 1. Status

Status:

- repository-internal preload / circularity audit
- audit phase: **03 COMPLETE**
- evaluates representation preload, mathematical legality requirements, source-declared prior structure,
  generated-target overlap, and bridge dependence
- not a generation-claim evidence audit
- not a physical-emergence verdict
- not an equation or notation revision
- not a revision-candidate record
- not a VED rewrite or validation
- [`00_connection_record_v0.1_ja.md`](./00_connection_record_v0.1_ja.md): **COMPLETE**
- [`01_equation_inventory_v0.1_ja.md`](./01_equation_inventory_v0.1_ja.md): **COMPLETE**
- [`02_equation_role_audit_v0.1_ja.md`](./02_equation_role_audit_v0.1_ja.md): **COMPLETE**
- `04_generation_claim_evidence_audit_v0.1_ja.md`: **NOT STARTED**
- `05_revision_candidates_v0.1_ja.md`: **NOT STARTED**
- `06_final_audit_record_v1.0_ja.md`: **NOT STARTED**
- VED core revision: **NOT STARTED**
- `generative_law_methodology`: **CLOSED / STOP-A**

本記録は、式をlegal / meaningfulに書くためのprior structureと、同じsource chainで後から
generated / emergentと記述されるtargetとの交差を監査する。preloadの所在を記録することは、
そのstructureが物理的に先在する、systemが知っている、またはoutcomeが決定済みであるという
claimではない。

\[
\text{representation preload}
\neq
\text{physical ontology},
\qquad
\text{formal derivation}
\not\Rightarrow
\text{physical emergence}.
\]

---

## 2. Scope and source basis

### 2.1 Audit question

> 01 / 02で特定したexpressionを定義・評価・適用する前に、どのcarrier、domain、ordering、
> operator、path policy、scale、mappingが必要か。そのrequirementは近接する生成targetと同じか、
> 部分的に重なるか、またはsource不足により未解決か。

本記録のprimary basisは[01 inventory](./01_equation_inventory_v0.1_ja.md)と
[02 role audit](./02_equation_role_audit_v0.1_ja.md)である。必要箇所について、次のrepository sourceを
再読した。

- [Vol.1 minimal axiom](../../paper/vol1/sections/minimal_axiom.tex)
- [Vol.1 causal logs and time](../../paper/vol1/sections/causal_logs_time.tex)
- [Vol.1 flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex)
- [Vol.1 closure](../../paper/vol1/sections/closure.tex)
- [Vol.1 space](../../paper/vol1/sections/space.tex)
- [core equations](../../docs/core_equations.md)
- [overview](../../docs/00_overview.md)
- [methodology](../../docs/methodology.md)
- [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md)

外部web researchは行っていない。gradient、divergence、curl、Laplacian、derivative、logarithm、
path optimization、fixed point、Helmholtz decompositionの最低限のwell-definedness条件を述べる箇所は、
repository statementではなく**STANDARD MATHEMATICAL REQUIREMENT**と明記する。

### 2.2 Five kinds of record

1. **Representation preload:** 記法を使う前にrepresentationが固定するcarrier、indices、domain、type等。
2. **Mathematical legality requirement:** operator / constructionがwell-definedであるための条件。
3. **Source-declared prior structure:** repository sourceが明示的に先に置く入力・domain・parameter。
4. **Generated-later target:** 同じsource chainの近傍で後からgenerated / emergentと呼ばれる対象。
5. **Circularity candidate:** prior requirementとgenerated targetのidentityまたはsame-type overlapが
   source claimをself-presupposingにする可能性。

単なるsymbol reuse、formal dependency、またはstandard domain requirementだけではcircularityとしない。

### 2.3 Circularity vocabulary

- **NO CIRCULARITY LOCATED**
- **PRELOAD PRESENT / NO CIRCULARITY ESTABLISHED**
- **POSSIBLE CLAIM-LEVEL CIRCULARITY**
- **POSSIBLE REPRESENTATIONAL CIRCULARITY**
- **SOURCE-LEVEL CIRCULARITY LOCATED**
- **CIRCULARITY UNRESOLVED**

### 2.4 Preload and outcome vocabulary

Preload categoriesは**Structural**、**Temporal / ordering**、**Semantic / language**、
**Operational**、**Measurement / interpretation**とする。preload statusは次だけを用いる。

- **NO MATERIAL PRELOAD LOCATED**
- **PRELOAD EXPLICIT**
- **PRELOAD IMPLICIT**
- **PRELOAD UNRESOLVED**

Outcome classesは重複可である。

- **P0:** no material preload issue located
- **P1:** ordinary representation preload
- **P2:** source-implicit structural preload
- **P3:** generated-target overlap
- **P4:** bridge-dependent
- **P5:** circularity unresolved
- **P6:** source-level circularity located

---

## 3. Main audit table

`Required prior structure`内のcategory prefixは、S=Structural、T=Temporal / ordering、
L=Semantic / language、O=Operational、M=Measurement / interpretationを表す。

| ID | Expression | Primary role from 02 | Required prior structure | Requirement source | Generated-later target nearby | Preload status | Circularity status | Scope | Class | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DIF-03 | \(\nabla\delta\), \(J\sim-\nabla\delta\) | **DERIVED CONSTRUCTION** | S: scalar-field domain, neighborhood / differentiable structure; O: gradient; M: gradient convention | **STANDARD MATHEMATICAL REQUIREMENT** | gradient, flow, later space / geometry | **PRELOAD IMPLICIT** | **POSSIBLE CLAIM-LEVEL CIRCULARITY** | Vol.1 minimal chain | P2, P3 | \(\delta\)のdomainと\(\nabla\)のdomain declarationはsource内で未発見。operator backgroundとgenerated physical spaceのidentityは未確定 |
| LOG-01 | \(H_{ij}\ge0\) | **DEFINITION** | S: node / index carrier and directed pair; T: accumulation order; M: nonnegative scale | **MIXED** | retained history / persistent structure | **PRELOAD EXPLICIT** | **NO CIRCULARITY LOCATED** | Vol.1 discrete network | P1 | nodesとaccumulated influenceはsource wordingにあるがevent-order modelは未指定 |
| LOG-03 | \(C_{ij}=1-e^{-\lambda\rho_iH_{ij}}\) | **CONSTITUTIVE / CLOSURE RELATION** | S: indexed \(H,C,\rho\); L: symbol identities; O: real exponential and simultaneous solution concept; M: \(\lambda\) scale | **MIXED** | selected persistent structure | **PRELOAD EXPLICIT** | **PRELOAD PRESENT / NO CIRCULARITY ESTABLISHED** | Vol.1 causal-log identity | P1 | equation inputs are explicit; \(C_{ij}\) repository identity conflictは別途保持 |
| LOG-04 | \(\rho_i=\sum_jC_{ij}\) | **DEFINITION** | S: index set and outgoing \(C\) values; O: defined finite / convergent sum | **MIXED** | local time rate / persistent structure | **PRELOAD EXPLICIT** | **PRELOAD PRESENT / NO CIRCULARITY ESTABLISHED** | node-indexed definition | P1 | sum domainのsize / convergence policyはsource内で明示されない |
| LOG-06 | combined fixed-point equation | **LAW-LIKE CONSTRAINT** | S: admissible \(\rho\)-space; O: fixed-point map, solution criterion, optional iteration / stability notion | **MIXED** | persistent physical structure | **PRELOAD EXPLICIT** | **PRELOAD PRESENT / NO CIRCULARITY ESTABLISHED** | fixed-point formulation | P1, P2 | sourceはfixed-point iterationと呼ぶ。existence / uniqueness / initializationは明示されない |
| LOG-07 | \(\dot\rho_i=\lambda\rho_iB_i/(1-\lambda A_i)\) | **DERIVED CONSTRUCTION** | T: derivative parameter; S: differentiable \(H_{ij}\); O: derivative, nonzero denominator, update interpretation | **MIXED** | microscopic log generation, continuum \(\sigma\), time generation | **PRELOAD IMPLICIT** | **CIRCULARITY UNRESOLVED** | Vol.1 microscopic-to-continuum wording | P2, P3, P4, P5 | dot parameterと\(\sigma\) bridgeが未固定 |
| TIM-01 | \(t\) | **ROLE UNRESOLVED** | T: ordered / differentiable parameter; L: identity across Vol.1 and IFGT | **UNRESOLVED** | observational / generative time | **PRELOAD UNRESOLVED** | **CIRCULARITY UNRESOLVED** | Vol.1 derivative vs IFGT effective external parameter | P5 | IFGTの\(t\)はexplicitだがVol.1 \(t\)とのidentityは未解決 |
| TIM-03 | \(d\tau_i/dt=\rho_i\) | **DEFINITION** | T: differentiable ordering parameter \(t\); S: differentiable \(\tau_i(t)\); O: derivative / integration and initial value; M: clock interpretation / scale | **MIXED** | local / observational time and irreversibility | **PRELOAD IMPLICIT** | **CIRCULARITY UNRESOLVED** | Vol.1 “Generation of Time” | P2, P3, P5 | external parameterization、construction order、physical timeのどれかはsource identity不足で確定しない |
| TIM-04 | \(\tau\), \(\tau_{\mathrm{VED}}\) | **DEFINITION** | T: evolution order for \(\partial_\tau\); L: two time types and proposed embedding; M: progress / clock interpretation | **MIXED** | informational / generative time | **PRELOAD IMPLICIT** | **POSSIBLE CLAIM-LEVEL CIRCULARITY** | IFGT | P2, P3 | sourceは起源を区別し同一軸へembeddableと述べるがmapは未表示 |
| FLW-01 | \(J_{ij}=C_{ij}-C_{ji}\) | **DEFINITION** | S: ordered node pairs and directed \(C\); L: \(C\) identity; O: antisymmetric subtraction | **MIXED** | directional flow | **PRELOAD EXPLICIT** | **PRELOAD PRESENT / NO CIRCULARITY ESTABLISHED** | discrete network | P1 | direction is in ordered indices before continuum vector field is introduced |
| FLW-02 | \(\mathbf J(x)\) | **DERIVED CONSTRUCTION** | S: continuum domain and vector-field type; O: coarse-graining / interpolation from \(J_{ij}\) | **MIXED** | continuum flow, vorticity, enclosure | **PRELOAD IMPLICIT** | **PRELOAD PRESENT / NO CIRCULARITY ESTABLISHED** | coarse-grained limit | P2, P4 | source says “becomes” but explicit bridge is absent |
| FLW-03 | continuum \(\rho\) | **ROLE UNRESOLVED** | S: continuum scalar-field domain; T: dependence on \(t\); O: interpolation / normalization from \(\rho_i\) | **MIXED** | density evolution / generative-time regime | **PRELOAD IMPLICIT** | **CIRCULARITY UNRESOLVED** | continuum equation | P2, P4, P5 | exact \(\rho(x,t)\) signature and discrete bridge not located |
| FLW-04 | \(\partial_t\rho+\nabla\cdot\mathbf J=\sigma\) | **BALANCE / CONTINUITY RELATION** | S: continuum domain, scalar density, vector field; T: differentiable \(t\); O: partial derivative and divergence; M: density / source normalization | **MIXED** | time generation, effective conservation regime | **PRELOAD IMPLICIT** | **CIRCULARITY UNRESOLVED** | Vol.1 coarse-grained field equation | P2, P3, P4, P5 | \(t\) identityとdiscrete-to-continuum bridgeが未固定 |
| FLW-06 | Helmholtz decomposition | **DERIVED CONSTRUCTION** | S: continuum vector-field domain; O: regularity, boundary / decay conditions, decomposition convention | **STANDARD MATHEMATICAL REQUIREMENT** | vorticity and stable structure | **PRELOAD IMPLICIT** | **PRELOAD PRESENT / NO CIRCULARITY ESTABLISHED** | Vol.1 continuum flow | P2, P4 | source lists divergence / curl properties but not domain, boundary, or uniqueness conditions |
| ENC-01 | \(\omega=\nabla\times\mathbf J\) | **DEFINITION** | S: continuum vector field, dimension / orientation or equivalent differential structure; O: curl | **STANDARD MATHEMATICAL REQUIREMENT** | circulation, enclosure, later geometry | **PRELOAD IMPLICIT** | **POSSIBLE REPRESENTATIONAL CIRCULARITY** | Vol.1 coarse-grained flow | P2, P3, P4 | vector-calculus setting is prior at representation level; its identity with emergent physical geometry is unresolved |
| ENC-02 | \(L\sim\lvert\omega\rvert\) | **DEFINITION** | S: codomain for \(\omega\); M: magnitude / norm, proportionality and normalization | **STANDARD MATHEMATICAL REQUIREMENT** | particle structure and gravity | **PRELOAD IMPLICIT** | **PRELOAD PRESENT / NO CIRCULARITY ESTABLISHED** | closure-density approximation | P1, P4 | \(L\) mapping and normalization remain partial; magnitude structure is not itself particle / gravity |
| ENC-03 | \(L<L_{\max}\) | **LAW-LIKE CONSTRAINT** | L: comparable scalar type; M: closure scale \(L_{\max}\); T: “at all times” quantification | **MIXED** | persistent incomplete closure | **PRELOAD EXPLICIT** | **NO CIRCULARITY LOCATED** | effective non-closure description | P1 | ordering and bound are stated; physical status of the bound is not assessed |
| ENC-04 | \(B(L)=-\kappa_B\log(1-L/L_{\max})\) | **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | M: \(L,L_{\max},\kappa_B\), dimensionless positive log argument; O: logarithm | **MIXED** | non-closure resistance | **PRELOAD EXPLICIT** | **NO CIRCULARITY LOCATED** | source-declared phenomenological encoding | P1 | source explicitly denies final microscopic-origin status |
| ENC-06 | closure energy \(E(A)\) | **DEFINITION** | S: configurations, flux vectors, vector sum / norm, triples; O: \(\Phi(A)\), cardinality, barrier evaluation; M: coefficients | **MIXED** | particle as local minimum | **PRELOAD EXPLICIT** | **PRELOAD PRESENT / NO CIRCULARITY ESTABLISHED** | finite configuration plus vector expression | P1, P2 | vector / norm setting is not fully declared locally; particle evidence is deferred |
| ENC-07 | effective mass scaling | **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | S: differentiable energy as function of \(L\); O: second derivative and evaluation at \(L_k\); M: barrier approximation and scale | **MIXED** | effective particle mass | **PRELOAD EXPLICIT** | **PRELOAD PRESENT / NO CIRCULARITY ESTABLISHED** | phenomenological barrier approximation | P1, P2 | smoothness and identification burden are not evaluated here |
| GEO-01 | \(\widetilde S_{ij}=\max_\gamma\prod S_{ab}\) | **DEFINITION** | S: graph / network and edge relation; L: admissible path family and endpoint convention; O: product and maximum; M: edge strengths / ordering | **MIXED** | propagation channel / later distance | **PRELOAD EXPLICIT** | **PRELOAD PRESENT / NO CIRCULARITY ESTABLISHED** | weighted-network construction | P1, P2 | path admissibility and cycles / attainment policy are not separately stated |
| GEO-02 | \(d_{ij}=-\log\widetilde S_{ij}\) / shortest path | **DEFINITION** | S: relation and admissible paths; O: logarithm, path aggregation and minimization; M: positive strength domain, scale / normalization | **MIXED** | distance, metric, space | **PRELOAD EXPLICIT** | **PRELOAD PRESENT / NO CIRCULARITY ESTABLISHED** | weighted network | P1, P2 | source supplies network / weights; log endpoint and disconnected-pair policies are not fully declared |
| GEO-03 | modified path distance | **DEFINITION** | S: paths and edge data; L: identity of \(L_{ab}\); O: path minimization; M: \(\epsilon\), relative units / scale | **MIXED** | gravity as distance distortion | **PRELOAD UNRESOLVED** | **CIRCULARITY UNRESOLVED** | overview | P2, P5 | \(L_{ab}\) is unresolved in 01, so the added path-cost term cannot be fully typed from this source alone |
| GEO-04 | coarse distance / metric expression | **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | S: continuum neighborhood, coordinates, tensor field; O: coarse-graining / averaging and local approximation; M: distance scale | **MIXED** | smooth metric / space | **PRELOAD IMPLICIT** | **POSSIBLE REPRESENTATIONAL CIRCULARITY** | Vol.1 coarse-grained limit | P2, P3, P4 | endpoint expression is explicit; coarse-graining map and tensor-domain construction are not |
| GEO-05 | \(g_{\mu\nu}\) as effective description of \(d_{ij}\) | **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | S: tensor / coordinate domain; O: discrete-to-continuum coarse-graining; M: effective metric interpretation | **MIXED** | metric tensor / space | **PRELOAD IMPLICIT** | **POSSIBLE CLAIM-LEVEL CIRCULARITY** | Vol.1 | P2, P3, P4 | source says coordinates label blocks and metric is not fundamental; exact construction remains absent |
| GEO-06 | \(\nabla^2\Psi\propto L\), \(g=-\nabla\Psi\) | **CONSTITUTIVE / CLOSURE RELATION** | S: scalar field and spatial / metric domain; O: Laplacian and gradient; M: proportionality, units, boundary data | **STANDARD MATHEMATICAL REQUIREMENT** | gravitational field / effective geometry | **PRELOAD IMPLICIT** | **POSSIBLE REPRESENTATIONAL CIRCULARITY** | overview / Vol.3-facing summary | P2, P3, P4 | spatial operators precede the nearby gravity / geometry identification at representation level; physical identity is not settled |
| GEO-07 | fixed-point metric equation | **LAW-LIKE CONSTRAINT** | S: tensor-field space and background \(g^{(0)}\); O: functional \(L_{\mu\nu}[g]\), fixed-point solution and linearization; M: \(\alpha_G\) | **MIXED** | gravity / Einstein-equation relation | **PRELOAD IMPLICIT** | **POSSIBLE CLAIM-LEVEL CIRCULARITY** | overview | P2, P3 | metric field occurs on both sides by fixed-point form; source does not locally define \(L_{\mu\nu}\) |
| IFG-02 | \(I=f(1-C)\), then \(I=1-C\) | **CONSTITUTIVE / CLOSURE RELATION** | S: common scalar-field domain; O: nondecreasing \(f\), then linear approximation; M: normalization of \(C,I\) | **REPOSITORY EXPLICIT** | information field relation | **PRELOAD EXPLICIT** | **PRELOAD PRESENT / NO CIRCULARITY ESTABLISHED** | IFGT | P1 | general relationとlinear assumptionはsourceが区別 |
| IFG-03 | \(C(x,\tau)\) | **DEFINITION** | S: continuum field domain; T: \(\tau\); O: map from discrete / scalar VED \(C\) if identity intended | **MIXED** | unified closure dynamics | **PRELOAD IMPLICIT** | **CIRCULARITY UNRESOLVED** | IFGT related branch | P2, P4, P5 | \(C_{ij}\to C(x,\tau)\) bridge and source identity are absent |
| IFG-04 | \(\partial_\tau I+\nabla\cdot J=\sigma\) | **BALANCE / CONTINUITY RELATION** | S: continuum scalar / vector fields; T: differentiable \(\tau\); O: derivative and divergence; M: source normalization | **MIXED** | informational time and generated difference | **PRELOAD IMPLICIT** | **POSSIBLE CLAIM-LEVEL CIRCULARITY** | IFGT | P2, P3 | source defines \(\tau\) endogenously while using it as evolution parameter; construction relation is not displayed |
| IFG-05 | \(J=-D\nabla I+\mu F_I\), \(F_I=-\nabla\Phi=\alpha\nabla C\) | **CONSTITUTIVE / CLOSURE RELATION** | S: continuum scalar / vector fields and neighborhood structure; O: gradients; M: coefficients / potential scale | **MIXED** | information geometry / spatial structure candidates | **PRELOAD IMPLICIT** | **POSSIBLE REPRESENTATIONAL CIRCULARITY** | IFGT | P2, P3 | gradient setting is prior to the paper's geometrical interpretation; identity with physical geometry is not established |
| IFG-06 | split \(\sigma\) terms | **CONSTITUTIVE / CLOSURE RELATION** | S: scalar fields; L: identities of \(\Delta,C\); M: saturation / barrier scales and coefficients | **REPOSITORY EXPLICIT** | difference / information generation | **PRELOAD EXPLICIT** | **PRELOAD PRESENT / NO CIRCULARITY ESTABLISHED** | IFGT effective model | P1, P2 | most parameters are stated; relation to VED microscopic \(\sigma\) remains a separate bridge question |
| IFG-07 | unified \(C(x,\tau)\) equation | **UPDATE / EVOLUTION RULE** | S: continuum field domain; T: differentiable endogenous \(\tau\); O: derivative, divergence, flux relation and boundary / initial data; M: model parameters | **MIXED** | time-generation process and listed structure classes | **PRELOAD IMPLICIT** | **POSSIBLE CLAIM-LEVEL CIRCULARITY** | IFGT | P2, P3 | source says equation contains time generation; how \(\tau\) is constructed from updates is not given |
| IFG-08 | \(J_C=-D\nabla C-\mu\alpha C\nabla C\) | **CONSTITUTIVE / CLOSURE RELATION** | S: continuum scalar / vector field types; O: gradient and multiplication; M: coefficients | **MIXED** | closure-field / geometry-related dynamics | **PRELOAD IMPLICIT** | **POSSIBLE REPRESENTATIONAL CIRCULARITY** | IFGT after linear assumption | P2, P3 | fixed operator setting and physical geometry are not identified |
| OTH-03 | effective \(\partial_tC+\nabla\cdot J_C=\cdots\) | **PHENOMENOLOGICAL / EFFECTIVE ANSATZ** | S: fixed-background continuum; T: external \(t\); O: derivative and divergence | **REPOSITORY EXPLICIT** | effective late-regime dynamics | **PRELOAD EXPLICIT** | **PRELOAD PRESENT / NO CIRCULARITY ESTABLISHED** | IFGT fixed-background approximation | P1 | source explicitly limits this form to approximately fixed background and keeps \(\tau\)-form basic |

The table audits 35 priority expression records inherited from 02. It does not imply that the remaining
14 inventory entries have no prerequisites; they were not selected as independent priority rows because
their dependencies are covered by these expressions or their source role remained purely lexical.

---

## 4. Mandatory operator audit

### 4.1 Gradient chain

The repository writes

\[
\nabla\delta\neq0,
\qquad
J\sim-\nabla\delta,
\]

but the cited minimal-axiom section does not define the domain of \(\delta\), a neighborhood relation,
coordinates, a differentiable structure, or the gradient operator. A gradient requires an appropriate
domain and a rule converting local change into a vector / covector-like object; this is a **standard
mathematical requirement**, not an explicit repository statement.

The nearby chain calls gradient a generated stage. The prior operator setting and the generated
directional structure may overlap, but the source does not establish that the mathematical background
used to write \(\nabla\) is physically identical to the space later claimed to emerge. Verdict:
**PRELOAD IMPLICIT / POSSIBLE CLAIM-LEVEL CIRCULARITY**, not “geometry is circular.”

### 4.2 Continuity equation

\[
\partial_t\rho+\nabla\cdot\mathbf J=\sigma
\]

requires a differentiable parameter \(t\), scalar field \(\rho\), vector field \(\mathbf J\), compatible
continuum domain, divergence operator, and normalization relating density, flux, and source. The source
explicitly calls it a coarse-grained equation but does not display the bridges from \(\rho_i,J_{ij}\).
Vol.1 does not locally define \(t\); IFGT separately defines an effective external \(t\). Their identity is
unresolved. Since time is also a nearby generated target, circularity remains **UNRESOLVED**, not located.

### 4.3 Vorticity

\[
\omega=\nabla\times\mathbf J
\]

requires a continuum field and an appropriate dimension / orientation or equivalent structure in which
curl is defined. Those requirements are not stated in the cited section. The representation therefore
preloads a vector-calculus setting before using \(\omega\) to discuss enclosure and later geometry.
Whether that setting is the generated physical geometry is unresolved: **POSSIBLE REPRESENTATIONAL
CIRCULARITY**, not a source-level circularity finding.

### 4.4 Helmholtz decomposition

The source states

\[
\mathbf J=\mathbf J_{\mathrm{rot}}+\mathbf J_{\mathrm{pot}}
\]

and the divergence / curl properties of the two parts. It does not state the domain, boundary or decay
conditions, regularity, harmonic component policy, or uniqueness convention. These are **standard
mathematical requirements** whose exact form depends on the intended theorem. Their absence here is a
preload / specification record, not an invalidity verdict.

### 4.5 Gravity operators

\[
\nabla^2\Psi\propto L,
\qquad
g=-\nabla\Psi
\]

requires a scalar field \(\Psi\), a domain supporting gradient and Laplacian, boundary data for solution
selection, and proportionality / units. The overview does not locally construct this operator setting.
Because nearby prose associates the resulting field with gravity and the wider chain associates
\(g_{\mu\nu}\) with emergent geometry, this is a **POSSIBLE REPRESENTATIONAL CIRCULARITY**. The audit does
not identify the operator background with physical geometry and does not assess the gravity claim.

---

## 5. Mandatory time audit

### 5.1 Local time equation

For

\[
\frac{d\tau_i}{dt}=\rho_i,
\]

the three roles must remain distinct:

- \(t\): derivative / ordering parameter;
- \(\tau_i\): source-defined node / observational time;
- \(\rho_i\): source-defined log density.

Vol.1 uses but does not locally define \(t\). IFGT defines an external \(t\) only for a fixed-background
effective description, but no source map identifies it with Vol.1 \(t\). The equation thus requires an
ordered differentiable parameter before \(\tau_i\) can be obtained by integration. That parameter could be
bookkeeping order, an effective parameterization, or physical time; the repository source does not settle
which. Therefore the status is **CIRCULARITY UNRESOLVED**, not “time generation is invalid.”

### 5.2 Dot derivatives

The derivation of \(\dot\rho_i\) also uses \(\dot H_{ij}\). The surrounding section calls this a time
derivative, but does not separately identify its parameter, define a history update schedule, or state an
initial-value problem. It is plausible that the dot refers to the same \(t\) used in \(d\tau_i/dt\), but this
identity is not explicitly fixed. The later verbal link to continuum \(\sigma\) adds a bridge dependence.

### 5.3 IFGT \(\tau\)

IFGT explicitly distinguishes external \(t\), VED generative \(\tau_{\mathrm{VED}}\), and informational
\(\tau\). It calls the latter two dynamically isomorphic / embeddable but does not display the embedding.
Its basic and unified equations use \(\partial_\tau\) while also describing \(\tau\) as endogenously generated
by the update process. This is a **POSSIBLE CLAIM-LEVEL CIRCULARITY**: an evolution parameter is required to
write the equation that is said to contain its generation. It is not a source-level circularity finding,
because an independent construction / bookkeeping interpretation has not been excluded.

---

## 6. Mandatory path / metric audit

### 6.1 Propagation strength

\[
\widetilde S_{ij}
=
\max_{\gamma:i\to j}
\prod_{(ab)\in\gamma}S_{ab}
\]

uses a network, endpoints, edge strengths, admissible directed or undirected paths, path-product convention,
and a maximum / supremum policy. The source explicitly supplies paths and \(S_{ab}\), but does not separately
state the admissible path family, cycle policy, unreachable-pair policy, or attainment condition.

### 6.2 Distance

\[
d_{ij}=-\log\widetilde S_{ij}
=
\min_\gamma\sum_{(ab)\in\gamma}(-\log S_{ab})
\]

uses the same relation and path structure, plus a logarithm domain and a scale / normalization for strengths.
The source states a weighted-network shortest-path construction. Endpoint values, zero strengths,
disconnected pairs, symmetry, and normalization are not all declared locally. This record therefore finds
ordinary explicit / implicit construction preload, not circularity.

\[
\text{relation}
\neq
\text{metric}
\neq
\text{physical space}.
\]

The first relation is mathematical construction; the last is a physical interpretation whose evidence is
deferred to phase 04.

### 6.3 Modified path distance

\[
d_{ij}
=
\min_\gamma\sum_{(ab)\in\gamma}
[-\log S_{ab}+\epsilon L_{ab}]
\]

adds \(L_{ab}\), \(\epsilon\), relative units, and an aggregation policy. The overview supplies the formula
but does not locally define \(L_{ab}\). That identity remains **UNRESOLVED** as recorded in 01. This blocks a
complete typing / preload account for the added cost; it does not show that the construction is impossible.

### 6.4 Coarse metric

\[
d(x,y)^2
\approx
g_{\mu\nu}(x)(x^\mu-y^\mu)(x^\nu-y^\nu)
\]

requires a continuum neighborhood, coordinate labels, a tensor field, and a specified relation between the
discrete distance and the local approximation. The source says nodes are grouped into blocks and averaged,
but gives no explicit coarse-graining operator, limiting procedure, or uniqueness rule. The endpoint
expression is therefore **PRELOAD IMPLICIT / BRIDGE-DEPENDENT**. The same-type overlap with the later metric /
space claim is a possible representational or claim-level circularity only; no physical-space verdict follows.

---

## 7. Discrete / continuum boundary audit

| Boundary | Source mapping | Required bridge | Bridge located? | Preload introduced by target representation | Circularity relevance | Status |
| --- | --- | --- | --- | --- | --- | --- |
| \(C_{ij}\to C(x,\tau)\) | IFGT correspondence language; no matrix-to-field formula | carrier / interpolation, normalization, continuum domain, \(\tau\), identity of discrete and field \(C\) | NO | scalar-field and continuum / time parameter | \(C\) identity and generated-time relation unresolved | **NO BRIDGE LOCATED** |
| \(J_{ij}\to\mathbf J(x)\) | Vol.1 says “in the coarse-grained limit ... becomes” | embedding / averaging, orientation, scaling, vector-field domain | verbal only | continuum vector-field and differential operators | later vorticity / geometry use depends on this target representation | **INFORMAL BRIDGE** |
| \(\rho_i\to\rho(x,t)\) | node log-density followed by continuum density wording | interpolation / averaging, volume normalization, function signature and time parameter | verbal only | scalar density field and differentiable \(t\) | time identity and continuity equation remain bridge-dependent | **INFORMAL BRIDGE** |
| \(d_{ij}\to g_{\mu\nu}\) | grouping / averaging prose plus approximate endpoint equation | coarse-graining map, coordinate / block construction, limit, tensor reconstruction and uniqueness policy | endpoint only | continuum, coordinates, tensor-field and approximation scale | generated-space claim overlaps target representation type | **PARTIAL BRIDGE** |

`NO BRIDGE LOCATED` means that this source pass did not find the map. It does not mean that no bridge can be
defined or that the target representation is invalid.

---

## 8. Fixed-point and self-reference audit

The relevant system is

\[
C_{ij}=1-\exp(-\lambda\rho_iH_{ij}),
\qquad
\rho_i=\sum_jC_{ij},
\]

and hence

\[
\rho_i
=
\sum_j[1-\exp(-\lambda\rho_iH_{ij})].
\]

The source explicitly calls the last expression a self-referential fixed-point equation and states that
stable fixed points correspond to persistent physical structure. It also explicitly says the self-reference
is not circular and describes an iterative reading in which existing \(\rho_i\) governs selection into new
\(C_{ij}\).

The following are located:

- a displayed fixed-point equation;
- a source-proposed solution class (“stable fixed points”);
- an iterative interpretation in prose.

The following are not located in the cited section:

- an explicit update map with old / new time indices;
- initialization and iteration schedule;
- existence conditions;
- uniqueness conditions;
- convergence or stability criterion.

Thus:

\[
\text{self-referential equation}
\neq
\text{vicious circularity}.
\]

The fixed-point system has **PRELOAD PRESENT / NO CIRCULARITY ESTABLISHED**. This does not validate the
fixed-point claim. The correspondence between stable solutions and persistent physical structure is stronger
than the equation's documentary role and is passed to phase 04.

### 8.1 Causal history / update ordering

The prose contains two compatible but not fully operationalized readings:

1. \(H_{ij}\) is accumulated history; a portion is selected into \(C_{ij}\); \(\rho_i\) is then summed from
   \(C_{ij}\).
2. Existing \(\rho_i\) controls how new \(H_{ij}\) is selected into new \(C_{ij}\).

The displayed equations simultaneously impose

\[
H_{ij}\longrightarrow C_{ij}\longrightarrow\rho_i,
\qquad
\rho_i\longrightarrow C_{ij}.
\]

This is recorded as a self-consistency / fixed-point structure. The source does not specify old/new indices,
event ordering, or a complete update schedule. The absence of that schedule does not turn the equations into
a source-level circularity finding.

---

## 9. Claim-preload crossing table

| Claim | Adjacent expression | Generated target | Prior structure required by expression | Same object? | Crossing status |
| --- | --- | --- | --- | --- | --- |
| difference → gradient / flow | \(\nabla\delta\), \(J\sim-\nabla\delta\) | directional gradient / flow | differentiable neighborhood and gradient operator | operator background and generated target are not source-identified | **PARTIAL OVERLAP** |
| local time generation | \(d\tau_i/dt=\rho_i\) | observational \(\tau_i\) | differentiable ordering parameter \(t\) | identity of \(t\) with generated physical time unresolved | **IDENTITY UNRESOLVED** |
| structural irreversibility | \(d\tau_i/dt=\rho_i\), \(\rho_i\ge0\) | irreversible physical time / arrow | ordered parameter, integration convention, nonnegative \(\rho_i\) | mathematical monotonicity and physical irreversibility are not identical by source declaration | **PARTIAL OVERLAP** |
| vorticity → enclosure | \(\omega=\nabla\times J\), \(L\sim\lvert\omega\rvert\) | enclosure / persistent structure | continuum vector-calculus setting and magnitude | enclosure is not the operator domain itself | **NO CROSSING LOCATED** |
| distance → space | \(d_{ij}=-\log\widetilde S_{ij}\) | space | network relation, path family, weights, log transform | graph-distance structure and physical space are not source-identical at this step | **PARTIAL OVERLAP** |
| coarse metric → space | coarse \(g_{\mu\nu}\) expressions | smooth metric / space | coordinate / tensor continuum and coarse-graining rule | same-type metric language appears on both sides; physical identity unresolved | **SAME-TYPE PRELOAD** |
| closure density → gravity | modified path cost; \(\nabla^2\Psi\propto L\); fixed-point metric | gravity / effective geometry | path metric, spatial differential operators, tensor field | representation uses spatial / metric types involved in the target interpretation | **POSSIBLE CIRCULARITY** |
| IFGT unified equation | \(\partial_\tau C+\nabla\cdot J_C=\cdots\) | generated informational time and structure classes | endogenous \(\tau\) as differentiable evolution parameter; continuum fields | parameter / generated-time relation not constructed | **POSSIBLE CIRCULARITY** |
| fixed point → persistent structure | combined \(\rho_i\) equation | persistent physical structure | admissible state space, fixed-point / stability concept | mathematical solution class and physical structure are not identical by definition | **NO CROSSING LOCATED** |

Crossing is a relation between documentary dependency and nearby claim wording. It is not an evidence verdict.

---

## 10. Three meanings of “before”

### 10.1 Construction order

The order in which a calculation, iteration, derivation, simulation, or record is executed. Examples are
fixed-point iteration steps or a coarse-graining procedure.

### 10.2 Formal dependency order

The order in which expressions must be typed or defined: a path family before a shortest-path value, a field
domain before \(\nabla\), or an ordering parameter before a derivative.

### 10.3 Physical / ontological order

A claim that one physical structure exists or occurs before another in the world.

The first two do not establish the third:

\[
\text{formal dependency}
\not\Rightarrow
\text{physical precedence},
\qquad
\text{representation preload}
\not\Rightarrow
\text{ontological preexistence}.
\]

A formalism may preload a domain to make a calculation possible without claiming that the modeled system
physically possessed, knew, or predetermined that domain. Conversely, a physical-order claim requires its
own evidence; this phase does not assess it.

---

## 11. Required summaries

### Summary A — preload classes

Classes overlap. Counts are memberships among the 35 main-table rows, not a partition.

| Class | Count |
| --- | ---: |
| P0 — no material preload issue located | 0 |
| P1 — ordinary representation preload | 15 |
| P2 — source-implicit structural preload | 25 |
| P3 — generated-target overlap | 14 |
| P4 — bridge-dependent | 11 |
| P5 — circularity unresolved | 7 |
| P6 — source-level circularity located | 0 |

### Summary B — possible circularity cases

| ID | Expression | Circularity status | Why | What remains unresolved |
| --- | --- | --- | --- | --- |
| DIF-03 | gradient chain | **POSSIBLE CLAIM-LEVEL CIRCULARITY** | generated gradient is written with a prior gradient operator | operator background vs generated directional / physical structure identity |
| LOG-07 | dot-density equation | **CIRCULARITY UNRESOLVED** | time derivative feeds a quantity linked to time generation | dot parameter and \(\sigma\) bridge |
| TIM-01 | \(t\) | **CIRCULARITY UNRESOLVED** | derivative parameter coexists with generated-time language | Vol.1 and IFGT \(t\) identity |
| TIM-03 | local-time equation | **CIRCULARITY UNRESOLVED** | \(\tau_i\) is defined relative to \(t\) | bookkeeping / effective / physical-time status of \(t\) |
| TIM-04 | IFGT time variables | **POSSIBLE CLAIM-LEVEL CIRCULARITY** | endogenous \(\tau\) is also equation parameter | construction and embedding map |
| FLW-03 | continuum \(\rho\) | **CIRCULARITY UNRESOLVED** | field depends on an unmapped continuum / time representation | \(\rho_i\) bridge and function signature |
| FLW-04 | continuity equation | **CIRCULARITY UNRESOLVED** | uses \(t\), continuum domain, divergence near time-generation claim | time identity and discrete bridge |
| ENC-01 | vorticity | **POSSIBLE REPRESENTATIONAL CIRCULARITY** | vector-calculus structure precedes enclosure / geometry prose | mathematical domain vs physical geometry identity |
| GEO-03 | modified path distance | **CIRCULARITY UNRESOLVED** | added closure cost is not fully typed | \(L_{ab}\) identity and units |
| GEO-04 | coarse metric expression | **POSSIBLE REPRESENTATIONAL CIRCULARITY** | continuum coordinate / tensor setting is needed to state emergent metric form | coarse map and physical identity |
| GEO-05 | effective \(g_{\mu\nu}\) | **POSSIBLE CLAIM-LEVEL CIRCULARITY** | metric-type representation is used in metric / space emergence claim | discrete reconstruction and identity |
| GEO-06 | gravity operators | **POSSIBLE REPRESENTATIONAL CIRCULARITY** | spatial differential operators precede gravity / geometry identification | operator domain vs generated geometry |
| GEO-07 | fixed-point metric | **POSSIBLE CLAIM-LEVEL CIRCULARITY** | metric field and functional occur in a metric / gravity claim | \(L_{\mu\nu}[g]\), solution setting and claim identity |
| IFG-03 | \(C(x,\tau)\) | **CIRCULARITY UNRESOLVED** | continuum field identity is assumed by unified equation | discrete / field \(C\) bridge |
| IFG-04 | IFGT balance | **POSSIBLE CLAIM-LEVEL CIRCULARITY** | generated informational time is used as evolution parameter | update-to-\(\tau\) construction |
| IFG-05 | IFGT flow | **POSSIBLE REPRESENTATIONAL CIRCULARITY** | gradient geometry is used in geometrical interpretation | mathematical vs physical geometry identity |
| IFG-07 | unified equation | **POSSIBLE CLAIM-LEVEL CIRCULARITY** | equation is said to contain generation of its time variable | independent ordering / construction account |
| IFG-08 | closure flow | **POSSIBLE REPRESENTATIONAL CIRCULARITY** | gradient setting is fixed before geometry-related reading | operator background vs physical geometry |

No row receives **SOURCE-LEVEL CIRCULARITY LOCATED**.

### Summary C — generated-target overlap

| Generated target | Expression using prior structure | Overlap type | Status |
| --- | --- | --- | --- |
| gradient / flow | \(\nabla\delta\), \(J\sim-\nabla\delta\) | differentiable directional operator | **PARTIAL OVERLAP** |
| observational time | \(d\tau_i/dt=\rho_i\) | differentiable order parameter | **IDENTITY UNRESOLVED** |
| irreversible time | local-time and continuum equations | ordering / derivative structure | **PARTIAL OVERLAP** |
| enclosure / geometry | curl / Helmholtz / \(L\) chain | continuum vector-calculus representation | **POSSIBLE REPRESENTATIONAL CIRCULARITY** |
| space / metric | path distance and coarse tensor | path, coordinate, tensor and coarse-graining structure | **SAME-TYPE PRELOAD** at coarse representation |
| gravity | path-cost, Laplacian / gradient, metric fixed point | spatial / metric representation | **POSSIBLE CIRCULARITY** |
| informational time | IFGT \(\partial_\tau\) equations | differentiable \(\tau\) parameter | **POSSIBLE CLAIM-LEVEL CIRCULARITY** |
| persistent physical structure | self-referential fixed point | solution / stability concept | **NO CROSSING LOCATED** between mathematical and physical objects |

### Summary D — bridge-dependent cases

| Boundary | Missing bridge | Consequence for audit |
| --- | --- | --- |
| \(C_{ij}\to C(x,\tau)\) | carrier, interpolation, normalization, source identity | IFGT field preload and VED discrete identity cannot be compared completely |
| \(J_{ij}\to\mathbf J(x)\) | coarse-graining, scaling, orientation, vector-field construction | divergence / curl target requirements cannot be traced back uniquely |
| \(\rho_i\to\rho(x,t)\) | interpolation, volume normalization, time / function signature | continuity equation's inputs cannot be identified uniquely with node quantities |
| \(d_{ij}\to g_{\mu\nu}\) | grouping, averaging, limit, tensor reconstruction, uniqueness | coarse metric overlap remains representation- and bridge-dependent |
| \(\dot\rho_i\to\sigma\) | microscopic-to-continuum projection | log-generation rate identities cannot be merged |

---

## 12. Handoff to 04

Phase 04 receives the following claims. This section does not assess their evidence.

### 12.1 Time

- \(d\tau_i/dt=\rho_i\) and local-time generation;
- \(\sigma>0\Longleftrightarrow\) time generation;
- monotonicity and structural irreversibility.

### 12.2 Space

- weighted-network \(d_{ij}\);
- coarse \(g_{\mu\nu}\);
- “space emerges” / effective-space wording.

### 12.3 Enclosure / particle

- \(\omega\), \(L\), closure energy;
- particle / local-minimum identification;
- phenomenological mass scaling.

### 12.4 Gravity

- closure-modified path cost;
- \(\nabla^2\Psi\propto L\), \(g=-\nabla\Psi\);
- fixed-point metric equation and linearization claim.

### 12.5 Difference / flow

- \(\nabla\delta\);
- \(J\sim-\nabla\delta\);
- necessity wording in the minimal chain.

### 12.6 IFGT

- unified equation and listed solution-class interpretations;
- \(\tau\) / \(\tau_{\mathrm{VED}}\) relation;
- IFGT \(\sigma\) / VED difference-generation correspondence.

Phase 04 must compare the evidence burden of a mathematical construction with that of its adjacent physical
claim. This record does not perform that comparison.

---

## 13. What this audit does not establish

This record does not establish:

- that any VED or IFGT equation is valid or invalid;
- that any operator is ultimately legal or illegal in a completed model;
- that any preload is a physical ontology or hidden physical assumption;
- that time, space, enclosure, particles, gravity, or information physically emerge;
- that any such emergence claim is false;
- that self-reference is vicious circularity;
- that any source-level circularity has been located;
- that missing bridges are impossible to supply;
- that any equation, notation, claim, or file should be revised.

The strongest current statements are documentary and conditional: some expressions require prior mathematical
structure; some requirements overlap in type with later generated-target wording; several identities remain
bridge-dependent or unresolved.

---

## 14. Closure / current audit status

| Record | Status |
| --- | --- |
| `00_connection_record_v0.1_ja.md` | **COMPLETE** |
| `01_equation_inventory_v0.1_ja.md` | **COMPLETE** |
| `02_equation_role_audit_v0.1_ja.md` | **COMPLETE** |
| `03_preload_and_circularity_audit_v0.1_ja.md` | **COMPLETE** |
| `04_generation_claim_evidence_audit_v0.1_ja.md` | **NOT STARTED** |
| `05_revision_candidates_v0.1_ja.md` | **NOT STARTED** |
| `06_final_audit_record_v1.0_ja.md` | **NOT STARTED** |
| VED core revision | **NOT STARTED** |

Current audit stage:

\[
\boxed{\text{03 COMPLETE / 04 NOT STARTED}}
\]

The gates remain:

\[
\text{representation preload}\neq\text{physical ontology},
\qquad
\text{formal dependency}\not\Rightarrow\text{physical precedence},
\qquad
\text{self-reference}\neq\text{vicious circularity}.
\]

Phase 04 has not begun. No revision candidate is introduced.

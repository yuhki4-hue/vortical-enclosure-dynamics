# VED generation claim / evidence audit v0.1

## 0. Status

- repository-internal generation-claim / evidence audit
- phase 04: **COMPLETE**
- not an equation revision
- not a notation revision
- not a VED validation or refutation
- no physical-emergence theorem
- no new equation or theory proposal
- `generative_law_methodology`: **CLOSED / STOP-A**
- VED core revision: **NOT STARTED**

Current audit stage:

\[
\boxed{\text{04 COMPLETE / 05 NOT STARTED}}
\]

中心gateは次である。

\[
\text{mathematical construction}
\not\Rightarrow
\text{physical emergence}.
\]

このrecordは、[01 equation inventory](./01_equation_inventory_v0.1_ja.md)、
[02 equation-role audit](./02_equation_role_audit_v0.1_ja.md)、
[03 preload / circularity audit](./03_preload_and_circularity_audit_v0.1_ja.md)を入力とし、
01の16 claimsを全件引き継ぐ。phase 05のaction classificationは行わない。

---

## 1. Scope and source basis

### 1.1 Scope

今回評価するのは、各claimのlogical form、必要なevidence burden、repository内で確認できる
evidence class、support level、scope mismatchである。式のroleは02から、prior structureとbridge
statusは03から継承する。

次は対象外である。

- equation / notationの変更;
- preloadまたはcircularityの再判定;
- physical emergenceの新規証明;
- VED core claimの新設;
- phase 05のaction判断。

### 1.2 Repository sources reread for this audit

Primary and core-facing records:

- [VED overview](../../docs/00_overview.md)
- [core equations](../../docs/core_equations.md)
- [claims](../../docs/claims.md)
- [generative sequence](../../docs/navigation/generative_sequence.md)
- [Vol.1 minimal axiom](../../paper/vol1/sections/minimal_axiom.tex)
- [Vol.1 causal logs and time](../../paper/vol1/sections/causal_logs_time.tex)
- [Vol.1 flow and vorticity](../../paper/vol1/sections/flow_vorticity.tex)
- [Vol.1 closure](../../paper/vol1/sections/closure.tex)
- [Vol.1 space](../../paper/vol1/sections/space.tex)
- [Vol.1 discussion](../../paper/vol1/sections/discussion.tex)
- [Vol.2 closure energy](../../paper/vol2/sections/closure_energy.tex)
- [Vol.2 triangular closure](../../paper/vol2/sections/triangular_closure.tex)
- [Vol.2 particle classification](../../paper/vol2/sections/particle_classification.tex)
- [Vol.2 discussion](../../paper/vol2/sections/discussion.tex)
- [Vol.3 gravity distance](../../paper/vol3/sections/gravity_distance.tex)
- [Vol.3 closure density](../../paper/vol3/sections/closure_density.tex)
- [Vol.3 Einstein equation](../../paper/vol3/sections/einstein_equation.tex)
- [Vol.3 discussion](../../paper/vol3/sections/discussion.tex)

Related-branch records, kept at their declared scope:

- [IFGT](../../Information-Field-Geometry-Theory/ifgt_ja.md)
- [dimensionality working note](../../dimensionality-working-note/README.md)
- [dimensionality experiments](../../dimensionality-working-note/experiments/README.md)

No external research was used. Standard mathematical or methodological requirements below describe the
burden associated with a claim type; they are not reported as evidence already supplied by the repository.
The closed `generative_law_methodology` supplies audit discipline, not evidence for VED correctness.

---

## 2. Claim and evidence vocabularies

### 2.1 Claim types

| Code | Claim type | Audit meaning |
| --- | --- | --- |
| A | **MATHEMATICAL CONSTRUCTION** | a quantity, decomposition, fixed-point target, or metric-like object is formally constructed |
| B | **STRUCTURAL CLAIM** | a mathematical structure has persistence, stability, metric, closure, or related properties |
| C | **DYNAMICAL / MECHANISM CLAIM** | one structure produces, updates, or causally supports another |
| D | **EMERGENCE CLAIM** | time, space, gravity, particles, or another physical structure emerges |
| E | **PHYSICAL IDENTIFICATION CLAIM** | a mathematical object is identified with a physical object or observable |
| F | **UNIVERSALITY / NECESSITY CLAIM** | necessity, uniqueness, minimality, or broad generality is asserted |
| G | **CORRESPONDENCE / ANALOGY CLAIM** | two formalisms or quantities are said to correspond, embed, or be analogous |

One claim may have several types. These types describe logical burden, not validity.

### 2.2 Evidence classes located in the repository

| Code | Evidence class |
| --- | --- |
| E0 | wording only |
| E1 | definition / formal construction |
| E2 | algebraic / derivational support |
| E3 | finite model / computational witness |
| E4 | structural theorem / proof under explicit assumptions |
| E5 | cross-scale / mapping evidence |
| E6 | empirical / observational evidence |
| E7 | independent replication / external validation |

Multiple classes may apply. A label records only the kind of material located. It does not by itself make
that evidence sufficient for the whole claim.

### 2.3 Support statuses

This record uses only:

- **SUPPORTED WITHIN STATED FORMAL SCOPE**
- **PARTIALLY SUPPORTED**
- **SUPPORT DEPENDS ON UNRESOLVED BRIDGE**
- **CLAIM STRONGER THAN CURRENT EVIDENCE**
- **NOT ESTABLISHED**
- **NOT TESTED IN THIS BRANCH**
- **SOURCE CONFLICT / CLAIM IDENTITY UNRESOLVED**

---

## 3. Claim-specific evidence burdens

### 3.1 Definition burden

For “\(X\) is defined as \(Y\),” the minimum burden is a well-formed definition, identifiable source,
and domain / codomain or typing sufficient to read the expression. Physical evidence is not required for
the definition claim itself.

### 3.2 Mathematical-property burden

For monotonicity, metricity, existence, uniqueness, convergence, or stability, the burden is an argument or
proof with explicit assumptions. A finite witness supports only the encoded finite scope and cannot establish
an unrestricted property.

### 3.3 Mechanism burden

For “\(A\) generates \(B\),” the burden includes an update, causal, or constructive route; source and target
identity; dependency or temporal order; and, where the claim is stronger than a definition, controls against
mere redescription or an externally inserted target.

### 3.4 Physical-emergence burden

For “physical \(B\) emerges from \(A\),” a mathematical construction is necessary but not sufficient. The
claim additionally requires a representation-to-observable bridge, operational interpretation, scope-limited
structural or empirical support, and evidence that the purely representational reading does not exhaust the
intended physical claim.

### 3.5 Identification burden

For “mathematical \(X\) is physical \(Y\),” an explicit mapping, operational semantics, and evidence beyond
naming or analogy are required.

### 3.6 Universality / necessity burden

For “necessarily,” “uniquely,” or “universally,” the burden is a theorem with explicit quantifiers and
assumptions, or evidence whose breadth matches the stated empirical scope. A local argument, finite witness,
or phenomenological expression alone is insufficient.

---

## 4. Primary claim audit

`Claim type` uses the codes from §2.1. `Current evidence located` records repository material, not an
endorsement of the prose claim.

| Claim ID | Claim wording | Claim type | Adjacent expression(s) | Required evidence burden | Current evidence located | Missing evidence type | Support status | Scope | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CLM-01 | difference is the sole axiom; \(C_{ij}\), gradient, flow, vortex and enclosure follow in rank order | C, D, F | textual chain; \(C\to J\to\omega\to L\to g\) | typed stepwise constructions plus necessity / completeness argument across every arrow | E0; some downstream E1 | E2/E4 for the whole chain; bridges between stages; E5/E6 for physical identifications | **NOT ESTABLISHED** | core-facing, framework-wide wording | navigation labels only early layers as validated; separate expressions do not establish the whole ordered chain |
| CLM-02 | difference / asymmetry gives gradient and flow | A, C, F | \(\nabla\delta\ne0\), \(J\sim-\nabla\delta\) | domain and operator specification; derivation of implication; mechanism evidence if physical flow is intended; universality proof for “necessary” | E0, E1 | explicit domain-sensitive derivation; E4 for necessity; physical bridge | **CLAIM STRONGER THAN CURRENT EVIDENCE** | Vol.1 local chain | formulas supply a formal reading; the necessity and physical-mechanism scope is wider |
| CLM-03 | causal history is selectively retained as persistent structure | A, B, C | \(C_{ij}=1-e^{-\lambda\rho_iH_{ij}}\), \(\rho_i=\sum_jC_{ij}\) | well-formed selection model; update / fixed-point semantics; persistence criterion and evidence | E0, E1, E2 | operational update schedule; existence / stability evidence; physical persistence bridge | **PARTIALLY SUPPORTED** | node/network model | the selection and fixed-point expressions are present; persistent physical structure is not established by those definitions alone |
| CLM-04 | local / observational time is generated by log accumulation | A, C, D, E | \(d\tau_i/dt=\rho_i\) | definition plus monotonicity; map from \(\tau_i\) to duration / clocks; mechanism and physical identification evidence | E0, E1, E2 | identity of \(t\); duration and clock semantics; E5/E6; alternative-reading control | **CLAIM STRONGER THAN CURRENT EVIDENCE** | node-indexed Vol.1 quantity | definition and conditional monotonicity support less than physical-time generation |
| CLM-05 | irreversibility is structural / built into the time definition | B, D, E | \(d\tau_i/dt=\rho_i\), \(\rho_i\ge0\) | monotonicity proof; distinction from non-reconstructibility, thermodynamic irreversibility, and physical arrow; physical evidence for the latter | E0, E1, E2 | inverse / state-recovery analysis; thermodynamic or operational bridge; E6 | **PARTIALLY SUPPORTED** | formal monotonicity within Vol.1 assumptions | mathematical non-decrease is supported; broader physical irreversibility is not thereby established |
| CLM-06 | antisymmetric causal log produces directional flow | A, C | \(J_{ij}=C_{ij}-C_{ji}=2A_{ij}\) | algebraic construction; operational semantics for transfer; bridge to continuum or physical motion if intended | E0, E1, E2 | explicit dynamics and discrete-to-continuum bridge; physical observable mapping | **PARTIALLY SUPPORTED** | discrete network, followed by informal continuum wording | antisymmetry is by construction; “produces” physical propagation carries a higher burden |
| CLM-07 | \(\sigma>0\) corresponds biconditionally to time being generated; conservation is phase-specific | C, D, G | \(\partial_t\rho+\nabla\cdot J=\sigma\); \(\sigma>0\Longleftrightarrow\) time generation | both directions of biconditional; unique \(\sigma\) identity; micro-to-continuum map; phase and time criteria | E0, E1 | derivation of both directions; \(\dot\rho_i\to\sigma\) bridge; time identification; E5/E6 | **SOURCE CONFLICT / CLAIM IDENTITY UNRESOLVED** | Vol.1 continuum claim; IFGT uses another \(\sigma\) construction | the balance form does not supply the biconditional, and \(\sigma\) has multiple source usages |
| CLM-08 | vorticity enables enclosure / persistent structure | A, B, C, E | \(\omega=\nabla\times J\), \(L\sim\lvert\omega\rvert\), Helmholtz decomposition, \(E(A)\) | definitions plus dynamics connecting circulation to closure, existence and stability criteria, physical enclosure mapping | E0, E1 | domain-conditioned derivation; dynamical stability result; E4/E5/E6 as scope requires | **CLAIM STRONGER THAN CURRENT EVIDENCE** | Vol.1 continuum-to-configuration sequence | curl and \(L\) are constructed; persistence and physical enclosure do not follow from naming them |
| CLM-09 | triangular closure is the minimal persistent enclosure; particle is a local minimum of closure energy | A, B, E, F | triangular loop argument; \(E(A)\); local-minimum definition | minimality / uniqueness proof under stated graph and closure class; local-minimum existence and stability; physical particle mapping | E0, E1 | E4 for unrestricted minimality; minimizer / attractor analysis; E5/E6 for particle identification | **PARTIALLY SUPPORTED** | Vol.1–2 structural proposal | particle is source-defined by a local minimum and a three-node argument is given; Vol.2 says particle mappings are structural, not proofs of equivalence |
| CLM-10 | distance is induced from symmetric connectivity / propagation strength | A, B | \(\widetilde S_{ij}=\max_\gamma\prod S_{ab}\); \(d_{ij}=-\log\widetilde S_{ij}\) | definition, path policy and domains; proof of each claimed distance property under explicit assumptions | E0, E1, E2 | full assumptions and any unclaimed metric axioms; operational bridge only if physical distance is asserted | **SUPPORTED WITHIN STATED FORMAL SCOPE** | weighted-network construction | max-product to min-sum conversion and stated nonnegativity / triangle property support the formal network-distance claim, not physical space |
| CLM-11 | metric / space is a coarse-grained description of log-distance structure | A, D, E | \(d(x,y)^2\approx g_{\mu\nu}\Delta x^\mu\Delta x^\nu\) | explicit coarse map, scaling / limit, robustness and uniqueness; physical interpretation and observational bridge | E0, E1, partial E5 wording | explicit reconstruction / convergence; uniqueness; E6 for physical space | **SUPPORT DEPENDS ON UNRESOLVED BRIDGE** | coarse-grained / effective claim | grouping and averaging are described, but 03 found no complete \(d_{ij}\to g_{\mu\nu}\) map |
| CLM-12 | closure density modifies distance and is associated with gravity | A, C, D, E | modified path cost; \(g=g^{(0)}+\alpha_GL\); \(\nabla^2\Psi\propto L\); fixed-point metric | construction of \(L_{\mu\nu}\) and continuum bridge; derivation of field equations; recovery / comparison; physical observations | E0, E1, E2; partial E5 wording | explicit discrete-to-continuum derivation; coefficients; nonlinear solution; E6/E7 | **SUPPORT DEPENDS ON UNRESOLVED BRIDGE** | Vol.3 structural / qualitative scope | Vol.3 explicitly says the precise coupling and nonlinear recovery are not derived; formal distance modification is narrower than gravity emergence |
| CLM-13 | closure density is associated with particle structure and effective mass | A, B, E | \(L\sim\lvert\omega\rvert\), \(E(A)\), \(m_k\sim\kappa_B/\Delta_k^2\) | energy / minimizer analysis, stable configurations, mapping to observed particles, quantitative mass predictions | E0, E1, E2 | existence / stability analysis; quantitative matching; E6/E7 | **PARTIALLY SUPPORTED** | source-declared phenomenological barrier approximation | formal energy and scaling ansatz are present; Vol.2 calls particle mapping structural and mass relation an analogy rather than a derived equality |
| CLM-14 | IFGT information dynamics and VED closure dynamics are joined by a unified \(C(x,\tau)\) equation | A, C, G | IFGT (4.1), (5.1)–(5.3) | equation derivation plus explicit VED↔IFGT map; preserved objects; solution existence; physical interpretation where claimed | E0, E1, E2; partial E5 correspondence table | discrete / continuum identity; \(\tau\) map; \(\sigma\) map; solution analysis | **SUPPORT DEPENDS ON UNRESOLVED BRIDGE** | related branch, not a core-equation entry | the equation is algebraically assembled inside IFGT; calling it unified does not establish cross-theory identity |
| CLM-15 | finite graph registration can produce topology / metric-readability windows in a model family | A, B, C | model-specific \(\Delta V,\Delta E,\Delta\beta_1\), graph-distance and BSW instruments | executable model, registered finite controls, saved outputs, claim bounded to model and instruments | E1, E3 | MRW identification; broader mechanism / physical / dimensional bridge; replication beyond recorded family if scope expands | **PARTIALLY SUPPORTED** | dimensionality working-note / v24 family only | per-event Betti accounting supports the topology component and BSW diagnostics are recorded; the module explicitly says these are not MRW detection or a completed \(3+1\) derivation |
| CLM-16 | stable fixed points of the self-referential \(\rho_i\) equation correspond to persistent physical structure | B, E | \(\rho_i=\sum_j[1-e^{-\lambda\rho_iH_{ij}}]\) | existence, uniqueness where claimed, stability criterion, convergence / basin analysis, physical correspondence map | E0, E1 | E2/E4 for fixed-point properties; operational persistence; E5/E6 for physical identification | **CLAIM STRONGER THAN CURRENT EVIDENCE** | Vol.1 assertion | Vol.1 discussion lists generic existence and uniqueness as open; no stability analysis is displayed near the claim |

---

## 5. Mandatory claim decompositions

The following subclaims prevent support for a definition or formal relation from being counted automatically
as support for a physical statement. These 58 rows refine the 16 primary claims; they do not add new VED
claims.

### 5.1 Local time, ordering and irreversibility

| Subclaim | Logical content | Evidence | Support status | Audit note |
| --- | --- | --- | --- | --- |
| TIME-1 | \(\tau_i\) is defined by \(d\tau_i/dt=\rho_i\) | E1 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | source explicitly gives the definition; \(t\) identity remains unresolved |
| TIME-2 | if \(\rho_i\ge0\), \(\tau_i\) is non-decreasing in \(t\) | E2 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | conditional mathematical monotonicity only |
| TIME-3 | \(\tau_i\) supplies an ordering parameter along a modeled trajectory | E1, E2 | **PARTIALLY SUPPORTED** | plateaus at \(\rho_i=0\) and the role of \(t\) limit what is fixed by the equation alone |
| TIME-4 | \(\tau_i\) represents metric duration | E0 | **NOT ESTABLISHED** | scale, clock procedure and duration semantics are not constructed |
| TIME-5 | \(\tau_i\) is physical / observational time | E0, E1 | **CLAIM STRONGER THAN CURRENT EVIDENCE** | a name and evolution relation do not supply an operational clock bridge |
| TIME-6 | physical time is generated by log accumulation | E0, E1, E2 | **CLAIM STRONGER THAN CURRENT EVIDENCE** | construction order, duration and physical identification burdens remain |
| IRR-1 | \(\tau_i\) is mathematically monotone under \(\rho_i\ge0\) | E2 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | same limited result as TIME-2 |
| IRR-2 | microscopic states cannot be reconstructed from later states | E0 | **NOT ESTABLISHED** | no inverse-map, information-loss or state-recovery analysis is located |
| IRR-3 | the relation establishes thermodynamic irreversibility / the second law | E0, E2 | **CLAIM STRONGER THAN CURRENT EVIDENCE** | entropy, thermodynamic state and empirical bridge are absent |
| IRR-4 | the relation establishes a physical arrow of time | E0, E2 | **CLAIM STRONGER THAN CURRENT EVIDENCE** | mathematical monotonicity does not supply physical-time identification |
| SIG-1 | \(\sigma>0\) marks positive source in the displayed balance relation | E1 | **PARTIALLY SUPPORTED** | this is formal only; source identity and micro-bridge remain unresolved |
| SIG-2 | \(\sigma>0\Longleftrightarrow\) physical time is being generated | E0, E1 | **SOURCE CONFLICT / CLAIM IDENTITY UNRESOLVED** | neither implication is derived and \(\sigma\) differs across source contexts |

Thus the repository supports a conditional monotonic quantity. It does not thereby establish duration,
clock reading, thermodynamic irreversibility, or physical-time emergence.

### 5.2 Difference and flow

| Subclaim | Logical content | Evidence | Support status | Audit note |
| --- | --- | --- | --- | --- |
| DIF-1 | the source displays a nonzero gradient of \(\delta\) | E1 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | expression located; 03 records its implicit operator domain |
| DIF-2 | \(J\sim-\nabla\delta\) gives a formal flow-like quantity | E1 | **PARTIALLY SUPPORTED** | proportionality / approximation and typing are not fully specified |
| DIF-3 | any difference necessarily yields this gradient-and-flow chain | E0, E1 | **CLAIM STRONGER THAN CURRENT EVIDENCE** | no quantified theorem over admissible differences is located |
| DIF-4 | this chain establishes a pre-geometric physical mechanism | E0, E1 | **NOT ESTABLISHED** | physical and operator-domain bridges are absent |

### 5.3 Vorticity, enclosure, particle and mass

| Subclaim | Logical content | Evidence | Support status | Audit note |
| --- | --- | --- | --- | --- |
| ENC-1 | \(\omega=\nabla\times J\) defines vorticity in the continuum notation | E1 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | well-formedness remains conditional on 03's operator requirements |
| ENC-2 | \(L\sim\lvert\omega\rvert\) introduces a closure-density ansatz / relation | E1 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | support is for the source relation, not its physical interpretation |
| ENC-3 | nonzero vorticity produces closed circulation | E0, E1 | **PARTIALLY SUPPORTED** | curl records local circulation; a dynamical production route is not given |
| ENC-4 | vorticity guarantees stable, persistent enclosure | E0, E1 | **CLAIM STRONGER THAN CURRENT EVIDENCE** | stability, duration and perturbation criteria are not analyzed |
| ENC-5 | the mathematical enclosure is a persistent physical object | E0 | **NOT ESTABLISHED** | operational and empirical identification is absent |
| PAR-1 | a directed loop first becomes combinatorially possible with three nodes in the stated setup | E0, E1 | **PARTIALLY SUPPORTED** | source supplies a local node-count argument; admissible graph class is not fully quantified |
| PAR-2 | the triangle is the unique minimal persistent closure in the full intended class | E0, E1 | **CLAIM STRONGER THAN CURRENT EVIDENCE** | a proof with explicit closure and equivalence assumptions is not located |
| PAR-3 | \(E(A)\) is defined as the displayed closure-energy functional | E1 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | definition only |
| PAR-4 | “particle” is source-defined as a local minimum of \(E(A)\) | E1 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | lexical / model definition, not physical-particle identity |
| PAR-5 | relevant local minima exist and are dynamically stable attractors | E0, E1 | **NOT ESTABLISHED** | no minimizer existence, Hessian, basin or evolution analysis is located |
| PAR-6 | those minima identify observed physical particles | E0, E1 | **NOT ESTABLISHED** | Vol.2 explicitly calls the mapping structural rather than a proof of equivalence |
| MAS-1 | the barrier approximation yields the displayed \(m_k\sim\kappa_B/\Delta_k^2\) scaling within its ansatz | E1, E2 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | source declares the phenomenological scope |
| MAS-2 | \(m_k\) thereby equals observed physical mass or predicts mass ratios | E0, E1, E2 | **CLAIM STRONGER THAN CURRENT EVIDENCE** | Vol.1 and Vol.2 list quantitative derivation as open |

### 5.4 Network distance and physical space

| Subclaim | Logical content | Evidence | Support status | Audit note |
| --- | --- | --- | --- | --- |
| SPC-1 | \(\widetilde S_{ij}\) is defined by a max-product path construction | E1 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | admissible paths and weight domain remain source conditions |
| SPC-2 | \(d_{ij}=-\log\widetilde S_{ij}\) equals the displayed min-sum path quantity | E1, E2 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | logarithmic conversion is explicit |
| SPC-3 | nonnegativity and triangle inequality hold under the intended weighted-path assumptions | E1, E2 | **PARTIALLY SUPPORTED** | proposition is stated; full assumptions and proof are not displayed in the section |
| SPC-4 | \(d_{ij}\) is an ordinary metric on the intended node set | E0, E1 | **NOT ESTABLISHED** | symmetry, identity of indiscernibles, unreachable pairs and zero weights are not settled in the claim source |
| SPC-5 | \(d_{ij}\) is operational physical distance | E0, E1 | **CLAIM STRONGER THAN CURRENT EVIDENCE** | no measurement correspondence is located |
| SPC-6 | physical space emerges from \(d_{ij}\) / coarse \(g_{\mu\nu}\) | E0, E1; partial E5 wording | **SUPPORT DEPENDS ON UNRESOLVED BRIDGE** | coarse map, scaling and physical interpretation remain unresolved |

The closed methodology's finite metric test is relevant to burden separation only. It is not transferred as
evidence that the VED distance has all metric properties or that physical space emerges.

### 5.5 Gravity

| Subclaim | Logical content | Evidence | Support status | Audit note |
| --- | --- | --- | --- | --- |
| GRV-1 | \(w_{ab}=-\log S_{ab}+\epsilon L_{ab}\) and its min-path distance are formally defined | E1 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | a modified path-cost construction is present |
| GRV-2 | \(L_{ab}=\sum_k\phi_{abk}\) defines an edge closure-density quantity in Vol.3 | E1 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | relation to Vol.1 scalar \(L\) remains bridge-dependent |
| GRV-3 | \(g_{\mu\nu}=g^{(0)}_{\mu\nu}+\alpha_GL_{\mu\nu}\) supplies an effective metric relation | E0, E1; partial E5 wording | **PARTIALLY SUPPORTED** | tensorization is proposed through regional averaging; explicit continuum derivation is absent |
| GRV-4 | \(\nabla^2\Psi\propto L\), \(g=-\nabla\Psi\) supply the stated weak-field formal analogy | E0, E1 | **PARTIALLY SUPPORTED** | coefficients, boundary conditions and discrete bridge are not derived |
| GRV-5 | the metric relation forms the stated fixed-point target \(g=g^{(0)}+\alpha_GL[g]\) | E1 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | equation construction does not establish a solution |
| GRV-6 | linearization yields the Einstein equation with the displayed coefficient and source | E0, E1, E2 | **CLAIM STRONGER THAN CURRENT EVIDENCE** | Vol.3 states the result but its discussion says the precise \(8\pi\), coupling and assumption-free derivation are absent |
| GRV-7 | VED recovers observed gravitational behavior / GR across the claimed physical domain | E0, partial E2 | **NOT ESTABLISHED** | full nonlinear solution, parameter matching and empirical comparison are not supplied |
| GRV-8 | gravity and spacetime physically emerge from closure density | E0, E1, partial E5 wording | **SUPPORT DEPENDS ON UNRESOLVED BRIDGE** | formal modification of distance does not satisfy the physical-emergence burden |

The source itself characterizes Vol.3 interpretations as structural and qualitative. It reports that exact
nonlinear recovery, precise coefficients, coupling identification and continuum derivation remain open.

### 5.6 Self-referential fixed point

| Subclaim | Logical content | Evidence | Support status | Audit note |
| --- | --- | --- | --- | --- |
| FIX-1 | substitution gives \(\rho_i=\sum_j[1-e^{-\lambda\rho_iH_{ij}}]\) | E1, E2 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | algebraic fixed-point form is explicit |
| FIX-2 | a fixed point exists for the intended generic \(H_{ij}\) | E0, E1 | **NOT ESTABLISHED** | Vol.1 discussion lists generic existence as open |
| FIX-3 | the relevant fixed point is unique | E0 | **NOT ESTABLISHED** | explicitly listed as open |
| FIX-4 | the stated iteration converges from an identified class of initial states | E0 | **NOT ESTABLISHED** | update schedule and convergence proof are absent |
| FIX-5 | a stable fixed point exists under a stated stability criterion | E0 | **NOT ESTABLISHED** | no criterion or perturbation calculation is located |
| FIX-6 | such a point corresponds to persistent physical structure | E0, E1 | **CLAIM STRONGER THAN CURRENT EVIDENCE** | mathematical solution class and physical persistence lack an explicit bridge |

Self-reference is not treated here as invalidity. The evidence question is whether existence, uniqueness,
convergence, stability and physical identification have separately met their burdens; the current record does
not find that they have.

### 5.7 IFGT correspondence and unified equation

| Subclaim | Logical content | Evidence | Support status | Audit note |
| --- | --- | --- | --- | --- |
| IFG-1 | \(\partial_\tau I+\nabla\cdot J=\sigma\) is introduced as the IFGT balance equation | E1 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | equation role only |
| IFG-2 | \(\sigma\) is decomposed into drive, dissipation and barrier terms | E1 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | internal construction within IFGT |
| IFG-3 | substitution yields the displayed \(C(x,\tau)\) evolution equation | E1, E2 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | algebraic assembly within declared effective assumptions |
| IFG-4 | the listed stable, cyclic or global solution classes exist | E0 | **NOT TESTED IN THIS BRANCH** | IFGT explicitly leaves individual identification and derivation outside scope |
| IFG-5 | those solution classes identify physical, biological or cognitive structures | E0 | **NOT ESTABLISHED** | no solution analysis or operational / empirical map is supplied |
| IFG-6 | informational \(\tau\) and VED \(\tau_{\mathrm{VED}}\) are separately described in prose | E0, E1 | **SUPPORTED WITHIN STATED FORMAL SCOPE** | source definitions are located; they do not establish equivalence |
| IFG-7 | \(\tau\) and \(\tau_{\mathrm{VED}}\) are dynamically isomorphic | E0 | **SUPPORT DEPENDS ON UNRESOLVED BRIDGE** | no map or preserved structure is given |
| IFG-8 | informational \(\tau\) embeds on the same axis as \(\tau_{\mathrm{VED}}\) | E0 | **SUPPORT DEPENDS ON UNRESOLVED BRIDGE** | embedding function, injectivity and compatibility are not stated |
| IFG-9 | IFGT \(\sigma\) and VED difference generation are the same process in two descriptions | E0; partial E5 correspondence table | **SOURCE CONFLICT / CLAIM IDENTITY UNRESOLVED** | \(\sigma\) constructions and the discrete / continuum map are unresolved |

---

## 6. Unsupported-inference ledger

These entries identify an evidence gap. They do not state that the stronger claim is false and they do not
assign a phase 05 action.

| Current evidence | Does not by itself establish | Missing burden |
| --- | --- | --- |
| definition \(d\tau_i/dt=\rho_i\) | physical time generation | clock / duration semantics, physical mapping, mechanism evidence |
| monotonic \(\tau_i\) under \(\rho_i\ge0\) | thermodynamic irreversibility or physical arrow | state-recovery, entropy, operational and empirical evidence |
| \(\omega=\nabla\times J\), \(L\sim\lvert\omega\rvert\) | stable physical enclosure | stability, persistence, dynamics and physical identification |
| local-minimum definition for \(E(A)\) | observed physical particle | minimizer existence, attractor analysis and particle-observable mapping |
| phenomenological \(m\sim\kappa_B/\Delta^2\) | observed masses or mass ratios | parameter derivation and quantitative comparison |
| graph distance \(d_{ij}\) | physical space | full metric properties, coarse bridge and operational spatial interpretation |
| coarse metric ansatz | emergent physical geometry | explicit limit, uniqueness / robustness and physical evidence |
| closure-modified path cost and field analogies | gravity | continuum derivation, field-equation recovery and observation |
| fixed-point equation | stable persistent physical structure | existence, uniqueness where needed, stability, convergence and physical map |
| “unified equation” label | VED–IFGT unification | explicit translation, preserved structure and identity conditions |
| finite dimensionality-model witness | universal generation law or observed dimensionality | expanded quantifiers, model bridge and physical evidence |
| failure to locate a bridge | the bridge is impossible | universal negative argument over an explicit admissible class |

---

## 7. Supported-within-scope ledger

Positive evidence is retained at the same resolution as negative findings.

| Claim | Evidence | Supported scope |
| --- | --- | --- |
| \(C_{ij}\), \(\rho_i\), \(\tau_i\), \(J_{ij}\), \(\omega\), \(L\), \(E(A)\), \(\widetilde S_{ij}\), \(d_{ij}\) are introduced by displayed relations | E1 | source-level definitions / constructions, subject to the source typing recorded in 01–03 |
| \(S_{ij}\) / \(A_{ij}\) symmetric–antisymmetric decomposition and \(J_{ij}=2A_{ij}\) | E1, E2 | algebraic identity |
| max-product propagation becomes min-sum cost after \(-\log\) | E1, E2 | stated weighted-path construction |
| \(\tau_i\) is non-decreasing when \(\rho_i\ge0\) | E2 | conditional mathematical monotonicity |
| substitution of the selection relation yields a fixed-point equation in \(\rho_i\) | E1, E2 | formal fixed-point target; no existence or stability conclusion |
| closure barrier / mass relation is presented as phenomenological | E1, E2 | source-declared ansatz scope |
| Vol.3 path cost, closure tensor, effective metric relation and metric fixed-point target are displayed | E1; partial E2 | formal / structural proposal scope, not observed gravity |
| IFGT balance, \(\sigma\) decomposition and unified \(C\)-equation are algebraically assembled | E1, E2 | related-branch formalism under its declared assumptions |
| v24 registration changes \((V,E,\beta_1)\) as recorded by finite scripts and ledgers | E1, E3 | encoded dimensionality model family and saved finite runs only |

No E6 empirical support or E7 independent external validation was located for the physical emergence and
identification claims audited here. No E4 theorem / proof was located that discharges the broad physical or
universality claims in the primary table.

---

## 8. Evidence-scope mismatch

| Claim | Evidence scope | Claim scope | Mismatch |
| --- | --- | --- | --- |
| whole generative chain follows from difference | definitions and prose for separate stages | framework-wide necessity / completeness | local constructions do not establish every arrow or the universal chain |
| physical time generation | definition and monotonicity of \(\tau_i\) | physical duration, clock time and emergence | definition / order parameter is narrower than physical identification |
| structural irreversibility | scalar monotonicity | thermodynamic and physical arrow claims | monotonicity is not non-reconstructibility or thermodynamics |
| persistent enclosure | curl and closure-density relations | stable physical structure | derived vector-calculus quantities do not provide stability evidence |
| physical particle and mass | source definitions and phenomenological relation | observed particle identity and quantitative mass | structural analogy is narrower than physical equivalence |
| physical space | weighted graph distance and approximate coarse expression | physical metric geometry | formal distance and partial bridge do not provide operational emergence evidence |
| gravity | qualitative Vol.3 construction and structural analogy | Einstein recovery and observed gravity | explicit continuum derivation, coefficients, nonlinear recovery and empirical test are absent |
| VED–IFGT unification | related-branch algebra and correspondence table | cross-theory identity / preserved dynamics | correspondence is not an explicit translation or isomorphism |
| topology / metric-readable windows | finite v24-family simulations | general VED or observed \(3+1\) dimension | finite model evidence remains finite and instrument-relative |
| fixed point → world / persistent structure | equation and assertion | existence, stability and physical persistence | formal target is narrower than solution and identification claims |

---

## 9. Required summaries

### Summary A — primary support-status counts

The counts below partition the 16 claims in §4. They do not count the 58 subclaims in §5.

| Support status | Count |
| --- | ---: |
| **SUPPORTED WITHIN STATED FORMAL SCOPE** | 1 |
| **PARTIALLY SUPPORTED** | 6 |
| **SUPPORT DEPENDS ON UNRESOLVED BRIDGE** | 3 |
| **CLAIM STRONGER THAN CURRENT EVIDENCE** | 4 |
| **NOT ESTABLISHED** | 1 |
| **NOT TESTED IN THIS BRANCH** | 0 |
| **SOURCE CONFLICT / CLAIM IDENTITY UNRESOLVED** | 1 |
| **Total** | **16** |

### Summary B — primary claim-type counts

Types overlap, so this is a membership count rather than a partition.

| Claim type | Count |
| --- | ---: |
| A — MATHEMATICAL CONSTRUCTION | 12 |
| B — STRUCTURAL CLAIM | 8 |
| C — DYNAMICAL / MECHANISM CLAIM | 10 |
| D — EMERGENCE CLAIM | 6 |
| E — PHYSICAL IDENTIFICATION CLAIM | 8 |
| F — UNIVERSALITY / NECESSITY CLAIM | 3 |
| G — CORRESPONDENCE / ANALOGY CLAIM | 2 |

### Summary C — strongest currently supported claims

| Claim | Evidence | Scope |
| --- | --- | --- |
| weighted-network distance is explicitly constructed from propagation weights | E1, E2 | the stated finite / discrete path representation; not physical space |
| \(\tau_i\) is non-decreasing when \(\rho_i\ge0\) | E2 | mathematical monotonicity relative to \(t\) |
| the selection equation can be written as a fixed-point target | E1, E2 | algebraic formulation; not existence, uniqueness, stability or persistence |
| closure-distance mass scaling is present as a phenomenological barrier expression | E1, E2 | source-declared ansatz only |
| IFGT's displayed field equation follows by its stated substitutions | E1, E2 | internal related-branch formal construction |
| v24 per-event topological bookkeeping and registered diagnostics have executable finite witnesses | E1, E3 | recorded model family only |

### Summary D — strongest unsupported or overextended claims

| Claim | Current evidence | Missing burden |
| --- | --- | --- |
| the complete ordered VED chain necessarily follows from difference | E0 plus local E1 constructions | typed bridges and quantified derivation across all arrows |
| physical time / arrow of time is generated | E1 definition and E2 monotonicity | duration, clock, physical mapping and irreversibility evidence |
| vorticity yields persistent physical enclosure | E1 constructions | dynamics, stability and operational identification |
| closure minima are physical particles with quantitative masses | E1 and phenomenological E2 | existence / stability, physical map and quantitative test |
| graph / coarse metric is physical space | E1 plus partial bridge wording | explicit scale bridge, uniqueness / robustness and observation |
| closure density generates gravity and exact GR behavior | E1/E2 structural proposal | continuum derivation, coefficients, nonlinear recovery, E6/E7 |
| generic stable fixed points correspond to the physical world | E0/E1 | existence, uniqueness, convergence, stability and physical map |

### Summary E — bridge-dependent claims

| Claim | Missing bridge | Effect on evidence status |
| --- | --- | --- |
| \(\dot\rho_i\to\sigma\) and \(\sigma>0\leftrightarrow\) time generation | microscopic-to-continuum projection and \(\sigma\) identity | biconditional cannot be assessed as one fixed claim |
| \(J_{ij}\to\mathbf J(x)\), \(\rho_i\to\rho(x,t)\) | coarse-graining, scaling, vector-field and density construction | continuum mechanism claims remain conditional |
| \(d_{ij}\to g_{\mu\nu}\) | grouping, limit, tensor reconstruction, uniqueness | physical-space support remains bridge-dependent |
| \(L, L_{ab}\to L_{\mu\nu}\to g_{\mu\nu}\) | scalar / edge / tensor identity and continuum derivation | gravity interpretation exceeds the formal path-cost result |
| \(\tau\leftrightarrow\tau_{\mathrm{VED}}\) | explicit map, preserved structure, embedding conditions | “isomorphic” / “embeddable” remains unsupported by construction |
| VED \(\sigma\leftrightarrow\) IFGT \(\sigma\) | identity and translation between source formalisms | cross-theory generation correspondence remains unresolved |

### 9.1 Evidence-class distribution across primary claims

Evidence classes overlap.

| Evidence class located | Number of primary claims |
| --- | ---: |
| E0 | 15 |
| E1 | 16 |
| E2 | 8 |
| E3 | 1 |
| E4 | 0 |
| E5, including explicitly marked partial mapping evidence | 3 |
| E6 | 0 |
| E7 | 0 |

---

## 10. Handoff to phase 05

This section groups records by evidence status only. It does not select any modification or disposition.

### A. Claims with support aligned to scope

- CLM-10: formal weighted-network distance construction;
- CLM-15のうち、finite topology bookkeepingとbounded diagnosticsとして明示された部分;
- §5 definitions, algebraic decompositions and conditional monotonicity labeled
  **SUPPORTED WITHIN STATED FORMAL SCOPE**.

### B. Claims stronger than evidence

- CLM-02, CLM-04, CLM-08 and CLM-16;
- the physical and universal portions separated in §5 for time, irreversibility, enclosure, particle, mass,
  gravity and fixed points.

### C. Claims blocked by missing bridge

- CLM-11, CLM-12 and CLM-14;
- the boundaries listed in Summary E.

### D. Claims with source identity conflict

- CLM-07, especially the identity of \(\sigma\) and the \(\dot\rho_i\to\sigma\) boundary;
- IFG-9, where two source formalisms use correspondence wording without an explicit translation.

### E. Claims whose physical interpretation is not established

- physical time and arrow of time;
- physical space and metric geometry;
- persistent physical enclosure and particles;
- physical mass and gravity;
- fixed-point / physical-world identification;
- IFGT solution-class physical identifications.

### F. Claims with strong finite or phenomenological support only

- v24 model-family topological and diagnostic claims;
- barrier-based effective mass scaling;
- effective / qualitative Vol.3 relations where the source itself limits the reading;
- partial coarse-grained correspondences without a complete bridge.

Phase 05 may use these groups as inputs. This record does not determine what action, if any, follows.

---

## 11. What this audit does not establish

This record does not establish:

- that an unsupported claim is false;
- that a missing bridge cannot be supplied;
- that any equation is mathematically invalid;
- that a representation preload is an ontological commitment;
- that a physical emergence claim is established or universally impossible;
- that finite dimensionality experiments validate core VED;
- that IFGT and VED are or are not ultimately unifiable;
- that VED is validated or refuted;
- that any equation, symbol, claim, or source should be changed.

The strongest audit result is a burden separation: repository definitions, algebraic constructions and finite
witnesses support several limited formal claims, while physical identification, cross-scale emergence,
universality and cross-theory identity generally require evidence classes not currently located.

---

## 12. Closure / current audit status

| Record | Status |
| --- | --- |
| `00_connection_record_v0.1_ja.md` | **COMPLETE** |
| `01_equation_inventory_v0.1_ja.md` | **COMPLETE** |
| `02_equation_role_audit_v0.1_ja.md` | **COMPLETE** |
| `03_preload_and_circularity_audit_v0.1_ja.md` | **COMPLETE** |
| `04_generation_claim_evidence_audit_v0.1_ja.md` | **COMPLETE** |
| `05_revision_candidates_v0.1_ja.md` | **NOT STARTED** |
| `06_final_audit_record_v1.0_ja.md` | **NOT STARTED** |
| VED core revision | **NOT STARTED** |

Current audit stage:

\[
\boxed{\text{04 COMPLETE / 05 NOT STARTED}}
\]

Evidence has been classified and scoped. No equation or notation has been changed, no physical-emergence
verdict has been manufactured from a definition, and no phase 05 action has been introduced.

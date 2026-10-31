# VED revision candidates v0.1

## 0. Status

- repository-internal revision-candidate record
- phase 05: **COMPLETE**
- candidates only; no final disposition
- no VED core file has been changed
- no equation or notation has been adopted
- no new theory, axiom, bridge formula, or physical derivation
- `generative_law_methodology`: **CLOSED / STOP-A**
- `06_final_audit_record_v1.0_ja.md`: **NOT STARTED**
- VED core revision: **NOT STARTED**

Current audit stage:

\[
\boxed{\text{05 COMPLETE / 06 NOT STARTED}}
\]

このrecordは、[01 equation inventory](./01_equation_inventory_v0.1_ja.md)、
[02 equation-role audit](./02_equation_role_audit_v0.1_ja.md)、
[03 preload / circularity audit](./03_preload_and_circularity_audit_v0.1_ja.md)、
[04 generation-claim / evidence audit](./04_generation_claim_evidence_audit_v0.1_ja.md)からのみ
candidate actionを導く。06がfinal dispositionを固定するまで、どのcandidateもrepository sourceへの
変更を承認しない。

---

## 1. Scope and hard gate

### 1.1 Question

> 現行VEDのequation、symbol identity、bridge、claim、interpretation、navigationについて、
> 01–04で確認されたsource conflict、missing bridge、role mixture、evidence-scope mismatchを
> 最小差分で整合させるには、どのactionをcandidateとして06へ渡すべきか。

外部researchは行っていない。一次sourceの式やclaimを再導出せず、01–04の確定した記録を
candidate basisとして使用する。

### 1.2 Gate

\[
\text{candidate action}
\neq
\text{final disposition}
\neq
\text{implemented revision}.
\]

05でcandidate化し、06でfinal dispositionが固定されるまで、VED core filesを変更しない。
Missing bridgeは不可能性ではなく未解決状態として扱い、unsupported claimはfalseとは扱わない。

---

## 2. Action vocabulary

| Action | Meaning in this record | Boundary |
| --- | --- | --- |
| **KEEP** | current expression or wording can remain within its already supported scope | VED correctnessを意味しない |
| **REVISE** | same role / claim familyを保ち、scope、assumption、identityまたはbridge wordingを明確化するcandidate | substantive derivationを追加しない |
| **DOWNGRADE** | physical、necessary、exact、unified等のclaim strengthをcurrent evidenceの範囲へ下げるcandidate | underlying phenomenonを否定しない |
| **SPLIT** | one symbol / sentence / chainに混在するidentity、roleまたはclaimを別itemsとして扱うcandidate | new symbolはまだ選ばない |
| **RETIRE** | current formをfuture core claimとして用いないcandidate | 強いactionであり、今回該当なし |
| **OPEN** | issueは確認されたが、directionを固定するevidenceまたはbridgeが不足 | missing bridgeを不可能とはしない |

These actions are functions, not a severity or strength order:

\[
\text{KEEP},\ \text{REVISE},\ \text{DOWNGRADE},\ \text{SPLIT},\ \text{OPEN},\ \text{RETIRE}
\]

do not form a hierarchy.

---

## 3. Candidate construction rules

1. equation、symbol identity、bridge、claim、interpretation、navigationを別targetにする。
2. 04でformal scopeがsupportedなら、physical claimと分離してformal objectを保存する。
3. source conflictは一つの意味へ正規化せず、source-specific identitiesを先に区別する。
4. bridgeが未発見ならformulaを発明せず、bridge targetを**OPEN**にする。
5. physical wordingは、formal constructionより強い場合にのみscope candidateを置く。
6. preloadだけを理由に式を削除しない。
7. finite / phenomenological evidenceは、そのscopeを維持する。
8. smallest changeを優先し、新しい数学を補わない。

---

## 4. Main candidate table

| Candidate ID | Target | Target type | Current role / claim | Audit basis | Proposed action | Minimal change | What is preserved | What is no longer claimed | Dependency before finalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RC-001 | \(C_{ij}\) identity | SYMBOL IDENTITY | paper/core: causal log; README/navigation: closure degree / formal carrier | 01 LOG-02; 02 §5.1; 04 CLM-03 | **SPLIT** | distinguish the source-specific meanings in prose and inventories; choose no new symbol in 05 | both historical meanings and source lineage | that both meanings are automatically one object | decide source authority and relation between meanings |
| RC-002 | \(t\) identity | SYMBOL IDENTITY | Vol.1 derivative parameter; IFGT effective external order parameter | 01 TIM-01; 03 TIM-01/TIM-03; 04 TIME-1–6 | **SPLIT** | keep source-specific \(t\) usages separate until an identity map exists | each source equation and its parameter | that all \(t\) occurrences have one established physical identity | specify Vol.1 parameter role and compare with IFGT |
| RC-003 | \(\sigma\) identity | SYMBOL IDENTITY | Vol.1 log-generation rate; IFGT decomposed mismatch / generation term | 01 FLW-05; 02 §5.3; 04 CLM-07/IFG-9 | **SPLIT** | label each source-specific \(\sigma\) before any correspondence wording | both balance relations and IFGT decomposition | that the symbols are identical by glyph alone | RC-009 and RC-041 |
| RC-004 | \(L\), \(L_{ab}\), \(L_{\mu\nu}\) identities | SYMBOL IDENTITY | scalar vorticity intensity, edge closure density, coarse tensor | 01 ENC-02/GEO-03/GEO-07; 03 gravity crossing; 04 GRV-2/3 | **SPLIT** | state each carrier and source-specific definition separately | all three formal expressions | that scalar, edge and tensor quantities are already connected by identity | RC-010 |
| RC-005 | \(C_{ij}\to C(x,\tau)\) | BRIDGE | discrete causal-log / closure-degree object to IFGT field | 03 Summary D; 04 CLM-14 | **OPEN** | mark carrier, interpolation, normalization and identity map as not supplied | both endpoint formalisms | that correspondence wording supplies the map | RC-001 and source identity of \(C\) |
| RC-006 | \(J_{ij}\to\mathbf J(x)\) | BRIDGE | discrete antisymmetric log-flow to continuum vector field | 01 FLW-01/02; 03 boundary table; 04 CLM-06 | **OPEN** | record averaging, orientation and scaling as missing | discrete definition and continuum equations | that “becomes” is an explicit coarse-graining map | RC-001; domain specification |
| RC-007 | \(\rho_i\to\rho(x,t)\) | BRIDGE | node log density to continuum density field | 01 LOG-04/FLW-03; 03 boundary table; 04 CLM-07 | **OPEN** | record interpolation, volume normalization and function signature as missing | node definition and continuum balance notation | that both \(\rho\) usages are already identified | RC-002 and RC-006 |
| RC-008 | \(d_{ij}\to g_{\mu\nu}\) | BRIDGE | weighted-network distance to coarse tensor metric | 03 GEO-04/05 and Summary D; 04 CLM-11/SPC-6 | **OPEN** | mark grouping, limit, tensor reconstruction and uniqueness as unresolved | network distance and effective metric target | that an approximate endpoint is a completed emergence derivation | RC-030/031 |
| RC-009 | \(\dot\rho_i\to\sigma\) | BRIDGE | microscopic rate expression to continuum source term | 01 LOG-07; 03 Summary D; 04 CLM-07 | **OPEN** | record projection and units as absent | both displayed expressions | that verbal “underlies” establishes equality or biconditional | RC-003 and RC-007 |
| RC-010 | \(L,L_{ab}\to L_{\mu\nu}\) | BRIDGE | scalar / edge closure density to coarse closure tensor | 03 gravity audit; 04 CLM-12/GRV-2/3 | **OPEN** | record averaging, direction-vector construction, scaling and carrier relation as unresolved | scalar, edge and tensor constructions | that shared name establishes a continuum derivation | RC-004 and RC-006/008 |
| RC-011 | \(d\tau_i/dt=\rho_i\) | EQUATION | definition with update / observable roles | 02 TIM-03; 04 TIME-1 | **KEEP** | preserve the displayed relation explicitly as a model definition relative to \(t\) | equation and node-indexed formal quantity | no additional physical claim is attached by this action | RC-002 |
| RC-012 | \(\rho_i\ge0\Rightarrow\tau_i\) non-decreasing | CLAIM | conditional mathematical monotonicity | 04 TIME-2/IRR-1 | **KEEP** | retain the condition and formal scope next to the conclusion | conditional monotonicity | duration, entropy or physical arrow | RC-002 |
| RC-013 | “physical / observational time is generated” | CLAIM | mechanism, emergence and physical-identification claim | 04 CLM-04/TIME-4–6 | **DOWNGRADE** | state only that \(\tau_i\) is a defined accumulation / order quantity unless a clock bridge is supplied | the \(\tau_i\) construction and monotonicity | established duration, clock identity or physical-time emergence | RC-002 and a future operational bridge |
| RC-014 | “irreversibility is built into time” | CLAIM | mathematical monotonicity mixed with non-reconstructibility, thermodynamics and physical arrow | 02 CLM-05; 04 IRR-1–4 | **SPLIT** | record the four claims separately and preserve support only for monotonicity | the conditional mathematical result | that monotonicity alone establishes every irreversibility notion | RC-002; criteria for state recovery and physical time |
| RC-015 | \(\sigma>0\Longleftrightarrow\) time generation | CLAIM | strong biconditional | 03 time / bridge audit; 04 CLM-07/SIG-2 | **DOWNGRADE** | replace biconditional force with source-local positive-source wording; leave time relation unresolved | \(\sigma>0\) as a formal regime condition where defined | either direction of physical-time generation as established | RC-003, RC-007 and RC-009 |
| RC-016 | \(\nabla\delta\), \(J\sim-\nabla\delta\) | EQUATION | derived / proportional formal construction | 02 DIF-03; 03 gradient chain; 04 CLM-02/DIF-1/2 | **REVISE** | add explicit domain, operator status, proportionality scope and effective / formal reading | the displayed gradient–flow relation | unconditional or pre-geometric applicability | operator-domain declaration |
| RC-017 | “difference necessarily gives gradient and flow” | CLAIM | necessity / mechanism claim | 04 CLM-02/DIF-3 | **DOWNGRADE** | use conditional “in the stated field representation” wording | the proposed ordered relation | quantified necessity across all differences | RC-016 |
| RC-018 | pre-geometric reading of the gradient chain | INTERPRETATION | physical mechanism prior to geometry | 03 DIF-03 crossing; 04 DIF-4 | **OPEN** | state that operator background and generated directional structure are not yet identified | question of a pre-geometric interpretation | that current notation already supplies it | RC-016 and explicit source/target comparison |
| RC-019 | causal-log / \(\rho_i\) fixed-point equations | EQUATION | constitutive relation and fixed-point constraint | 02 LOG-03/06; 03 §8; 04 FIX-1 | **KEEP** | preserve as a formal self-consistency target | displayed equations and self-referential structure | existence, uniqueness, convergence or physical persistence | RC-001 |
| RC-020 | fixed-point update semantics | INTERPRETATION | prose iteration without old/new indices or schedule | 03 §8.1; 04 CLM-03/FIX-4 | **OPEN** | list state, initialization, update map and schedule as unresolved | fixed-point reading | that a complete dynamical mechanism is already specified | RC-001/019 |
| RC-021 | “stable fixed points correspond to persistent physical structure” | CLAIM | stability plus physical identification | 04 CLM-16/FIX-2–6 | **DOWNGRADE** | call persistent structure a candidate interpretation until existence and stability are shown | fixed-point target and research question | generic stable solutions or physical correspondence as established | RC-019/020 plus stability and physical map |
| RC-022 | \(\omega=\nabla\times\mathbf J\) | EQUATION | formal definition / derived construction | 02 ENC-01; 04 ENC-1 | **KEEP** | preserve as a continuum definition with its domain stated | vorticity definition | enclosure persistence or physical generation | RC-006 and vector-calculus domain |
| RC-023 | \(L\sim\lvert\omega\rvert\) | EQUATION | closure-density relation / ansatz | 02 ENC-02; 04 ENC-2 | **REVISE** | state proportionality, carrier and ansatz scope explicitly | formal closure-density candidate | exact identity or stability mechanism | RC-004/006/022 |
| RC-024 | “vorticity produces persistent enclosure” | CLAIM | mechanism and physical-structure claim | 04 CLM-08/ENC-3–5 | **DOWNGRADE** | describe circulation / enclosure as a candidate mechanism pending dynamics and stability | vorticity and closure-density constructions | guaranteed persistence or physical enclosure | RC-022/023 plus stability analysis |
| RC-025 | “triangle is the unique minimal persistent closure” | CLAIM | minimality / uniqueness claim | 04 CLM-09/PAR-1/2 | **DOWNGRADE** | limit to the stated finite configuration argument and explicit closure class | three-node candidate and local argument | unrestricted topological uniqueness | definition of admissible closure and equivalence |
| RC-026 | “particle” as a local minimum of \(E(A)\) | CLAIM | source-level model definition | 02 ENC-06; 04 PAR-3/4 | **KEEP** | retain explicitly as a model definition | closure-energy vocabulary | observed-particle identity | RC-027 kept separate |
| RC-027 | closure minimum = physical particle | INTERPRETATION | physical-identification claim | 04 PAR-5/6 | **DOWNGRADE** | use structural candidate / particle-like interpretation wording | energy minima as candidate configurations | equivalence with observed particles | minimizer, stability and observable map |
| RC-028 | \(m_k\sim\kappa_B/\Delta_k^2\) | EQUATION | phenomenological / effective ansatz | 02 ENC-07; 04 MAS-1 | **KEEP** | retain the explicit phenomenological qualifier and parameter dependence | formula within barrier approximation | quantitative observed-mass prediction | none for the scoped ansatz; RC-029 for physical wording |
| RC-029 | closure distance determines physical mass | CLAIM | physical identification / quantitative claim | 04 CLM-13/MAS-2 | **DOWNGRADE** | describe only a phenomenological scaling candidate | source-declared ansatz | observed masses or ratios as derived | quantitative parameter derivation and data comparison |
| RC-030 | \(d_{ij}=-\log\widetilde S_{ij}\) | EQUATION | weighted-network path construction | 02 GEO-01/02; 04 CLM-10/SPC-1/2 | **KEEP** | retain within the declared graph / path / weight domain | strongest supported formal distance construction | physical space or full metricity without assumptions | RC-031 for property wording |
| RC-031 | metric-property wording for \(d_{ij}\) | CLAIM | nonnegativity / triangle proposition; possible full-metric reading | 03 path audit; 04 SPC-3/4 | **REVISE** | list weight, reachability, symmetry, zero-distance and codomain assumptions beside each property | the proved or stated property under explicit conditions | unconditional ordinary metric status | RC-030 and declared path policy |
| RC-032 | “physical space emerges” | CLAIM | physical-emergence / identification claim | 03 coarse-metric overlap; 04 CLM-11/SPC-5/6 | **DOWNGRADE** | label \(d_{ij}\) and \(g_{\mu\nu}\) as formal / effective spatial candidates pending a bridge | distance construction and coarse target | physical space emergence as established | RC-008/031 and operational interpretation |
| RC-033 | closure-modified path cost | EQUATION | formal weighted path construction | 02 GEO-03; 04 GRV-1 | **KEEP** | retain as a definition with \(L_{ab}\), \(\epsilon\), units and path policy stated | modified cost and minimization form | gravity by definition alone | RC-004 and RC-010 |
| RC-034 | \(\nabla^2\Psi\propto L\), \(g=-\nabla\Psi\) | EQUATION | effective / analogical field relations | 02 GEO-06; 03 gravity operators; 04 GRV-4 | **REVISE** | mark domain, boundary conditions, coefficient and weak-field / analogy scope | field-equation candidates | derivation from the discrete model or exact gravity | RC-004/006/010 |
| RC-035 | \(g_{\mu\nu}=g^{(0)}_{\mu\nu}+\alpha_GL_{\mu\nu}[g]\) | EQUATION | formal metric fixed-point target | 02 GEO-07; 04 GRV-5 | **KEEP** | retain explicitly as a proposed fixed-point relation | formal self-consistency target | existence, solution, GR recovery or physical metric | RC-008/010 |
| RC-036 | Einstein-equation recovery | CLAIM | linearization / physical recovery claim | 04 GRV-6/7; Vol.3 limits recorded there | **DOWNGRADE** | state structural analogy / intended weak-field target unless derivation and coefficients are supplied | fixed-point motivation and comparison target | exact or assumption-free recovery | RC-034/035 and explicit linearization |
| RC-037 | gravity / spacetime physically emerges from closure density | CLAIM | mechanism, emergence and physical-identification claim | 04 CLM-12/GRV-8 | **DOWNGRADE** | state a structural / effective candidate interpretation and preserve unresolved bridge status | path-cost and metric proposals | physical emergence as established | RC-008/010/034–036 plus E6-type evidence |
| RC-038 | IFGT balance and unified \(C(x,\tau)\) equation | EQUATION | related-branch formal construction / evolution rule | 02 IFG-04/07; 04 IFG-1–3 | **KEEP** | retain within IFGT's declared assumptions and related-branch scope | internal algebraic construction | VED identity or solution-class realization | RC-005 and RC-040/041 for cross-branch claims |
| RC-039 | “VED–IFGT unified” | CLAIM | cross-theory identity / unification claim | 04 CLM-14/IFG-7–9 | **DOWNGRADE** | use formal correspondence / proposed connection wording until explicit maps exist | IFGT equation and comparison program | established unification or dynamic identity | RC-005, RC-040 and RC-041 |
| RC-040 | \(\tau\leftrightarrow\tau_{\mathrm{VED}}\) | BRIDGE | dynamic isomorphism / embedding wording | 03 TIM-04; 04 IFG-6–8 | **OPEN** | require an explicit map, preserved objects, direction and embedding conditions | separate time definitions | isomorphism or common axis from prose alone | RC-002 |
| RC-041 | VED \(\sigma\leftrightarrow\) IFGT \(\sigma\) | BRIDGE | same-process / correspondence wording | 02 §5.3; 04 IFG-9 | **OPEN** | require source/target quantities and translation before comparison | both source-specific generation terms | identity or same physical process | RC-003 and RC-009 |
| RC-042 | \(C\to J\to\omega\to L\to g\) and wider chain | NAVIGATION / GENERATIVE CHAIN | arrows mix definitions, constructions, ansätze, bridges and physical claims | 02 OTH-01/02; 04 CLM-01 | **SPLIT** | annotate or separate arrows by role and source scope | navigation order and links to each expression | one undifferentiated arrow semantics | RC-001–041 as applicable |
| RC-043 | “generative chain” strength | NAVIGATION / GENERATIVE CHAIN | sequence presentation suggests common mechanism / necessity | 04 CLM-01 and mismatch ledger | **DOWNGRADE** | present as an audit / dependency sequence unless each arrow meets mechanism burden | reader navigation and research program | full derivation, necessity or physical generation from the diagram alone | RC-042 after P1/P2 decisions |
| RC-044 | dimensionality finite results | CLAIM | model-family topology bookkeeping and BSW diagnostics | 04 CLM-15 | **KEEP** | retain working-note, finite, instrument-relative limits and BSW/MRW distinction | executable finite evidence and negative results | observed dimensionality or core VED validation | none within its existing related-branch scope |

---

## 5. Mandatory domain-specific candidate notes

### 5.1 Time

The equation, monotonicity, physical-time wording, irreversibility notions, \(t\) identity and
\(\sigma\)-biconditional are separate targets:

- RC-011 and RC-012 preserve the supported formal content.
- RC-002 prevents unresolved \(t\) identities from being merged.
- RC-013 separates accumulation / ordering from duration and physical time.
- RC-014 separates monotonicity, non-reconstructibility, thermodynamics and physical arrow.
- RC-003, RC-009 and RC-015 prevent the \(\sigma\) biconditional from bypassing identity and bridge burdens.

### 5.2 Difference and flow

RC-016 would preserve the formal relation while requiring an explicit domain. RC-017 would remove unqualified
necessity from that formal relation. RC-018 would leave the pre-geometric interpretation unresolved rather than
rejecting the expression because it has representation preload.

### 5.3 Fixed point

RC-019 preserves the self-consistency equations. RC-020 records missing update semantics without calling
self-reference invalid. RC-021 separates a formal solution target from existence, stability, persistence and
physical identification.

### 5.4 Enclosure, particle and mass

RC-022/023 would preserve the vorticity and \(L\) relations at their formal scope. RC-024/025 would adjust only stronger
persistence and universality wording. RC-026 would keep the source-level particle definition separate from
RC-027's physical identification. RC-028 would preserve the phenomenological status of mass scaling; RC-029
would prevent that ansatz from being read as a quantitative particle-mass derivation.

### 5.5 Space

RC-030 would retain the strongest supported path construction. RC-031 would make each metric-property claim
assumption-sensitive. RC-008 would keep the network-to-tensor bridge open, while RC-032 would treat physical space as
an interpretation whose evidence burden has not been met.

### 5.6 Gravity

RC-033 and RC-035 retain the formal path-cost and metric fixed-point targets. RC-004/010 preserve the
unresolved scalar / edge / tensor identity and bridge. RC-034 limits differential field equations to their
declared effective or analogical use. RC-036 and RC-037 do not remove Vol.3's structural program; they
prevent structural proposal from being recorded as demonstrated Einstein recovery or physical emergence.

### 5.7 IFGT

RC-038 retains the internal IFGT construction. RC-039 separates that construction from cross-theory
unification. RC-040/041 leave the \(\tau\) and \(\sigma\) bridges open and require explicit maps before
isomorphism, embedding or same-process wording can carry evidential force.

---

## 6. Candidate groups by action

### KEEP candidates

RC-011, RC-012, RC-019, RC-022, RC-026, RC-028, RC-030, RC-033, RC-035,
RC-038, RC-044.

### REVISE candidates

RC-016, RC-023, RC-031, RC-034.

### DOWNGRADE candidates

RC-013, RC-015, RC-017, RC-021, RC-024, RC-025, RC-027, RC-029, RC-032,
RC-036, RC-037, RC-039, RC-043.

### SPLIT candidates

RC-001, RC-002, RC-003, RC-004, RC-014, RC-042.

### OPEN candidates

RC-005, RC-006, RC-007, RC-008, RC-009, RC-010, RC-018, RC-020, RC-040,
RC-041.

### RETIRE candidates

None. The audit finds narrower, separated, explicitly conditional, or open records sufficient at the
candidate stage. No result requires discarding an entire equation family or underlying phenomenon.

---

## 7. Preserve versus stop claiming / make conditional

| Target | Preserve | Stop claiming / make conditional | Reason |
| --- | --- | --- | --- |
| local-time equation | \(d\tau_i/dt=\rho_i\) as a model definition relative to \(t\) | physical-time generation | definition and conditional monotonicity do not provide a clock bridge |
| monotonicity | \(\rho_i\ge0\Rightarrow\tau_i\) non-decreasing | non-reconstructibility, thermodynamic arrow, all physical irreversibility | 04 separates these burdens |
| \(\sigma>0\) regime | source-local positive-source statement | biconditional physical-time generation | \(\sigma\) identity and micro / continuum bridge are unresolved |
| gradient / flow chain | formal field-representation expressions | universal necessity and pre-geometric mechanism | domain and mechanism burdens remain |
| fixed-point system | self-consistency target | generic existence, stability and physical persistence | these properties are not established by the equation alone |
| vorticity / \(L\) | continuum definition and scoped ansatz | guaranteed persistent enclosure | stability evidence is absent |
| particle definition | model term “local minimum of \(E(A)\)” | equivalence with observed particle | source definition and physical identification differ |
| mass scaling | phenomenological barrier relation | quantitative physical masses / ratios | source explicitly limits the relation |
| network distance | max-product / min-sum construction | unconditional full metric and physical space | property assumptions and physical bridge differ |
| coarse metric | effective target expression | completed space-emergence derivation | explicit coarse map and physical interpretation are absent |
| gravity formalism | path cost, effective field relations and metric fixed-point target | exact Einstein recovery and physical gravity emergence | Vol.3 describes structural / qualitative scope and open derivations |
| IFGT equation | internal algebraic construction | established VED–IFGT identity | cross-theory maps for \(C,\tau,\sigma\) are absent |
| dimensionality evidence | bounded model-family results and negative controls | observed \(3+1\) derivation or core VED validation | E3 remains finite and instrument-relative |

---

## 8. Revision dependency graph

The audit-derived dependency order is:

```text
source identities: C_ij / t / sigma / L-family
        |
        v
bridge statuses: C, J, rho, distance, L, dot-rho, tau, sigma
        |
        v
equation scope and operator / path assumptions
        |
        v
physical and universality claim wording
        |
        v
navigation / generative-chain presentation
        |
        v
06 final audit record
        |
        v
VED core revision
```

This is documentary dependency, not severity and not authorization to edit the final node. Source identity
must generally be settled before bridge or physical-claim wording can be finalized.

---

## 9. Required summaries

### Summary A — action counts

| Action | Count |
| --- | ---: |
| **KEEP** | 11 |
| **REVISE** | 4 |
| **DOWNGRADE** | 13 |
| **SPLIT** | 6 |
| **OPEN** | 10 |
| **RETIRE** | 0 |
| **Total** | **44** |

### Summary B — equation-level candidates

| Candidate | Equation | Action |
| --- | --- | --- |
| RC-011 | \(d\tau_i/dt=\rho_i\) | **KEEP** |
| RC-016 | \(\nabla\delta,\ J\sim-\nabla\delta\) | **REVISE** |
| RC-019 | causal-log / \(\rho_i\) fixed-point equations | **KEEP** |
| RC-022 | \(\omega=\nabla\times\mathbf J\) | **KEEP** |
| RC-023 | \(L\sim\lvert\omega\rvert\) | **REVISE** |
| RC-028 | \(m_k\sim\kappa_B/\Delta_k^2\) | **KEEP** |
| RC-030 | \(d_{ij}=-\log\widetilde S_{ij}\) | **KEEP** |
| RC-033 | closure-modified path cost | **KEEP** |
| RC-034 | \(\nabla^2\Psi\propto L,\ g=-\nabla\Psi\) | **REVISE** |
| RC-035 | metric fixed-point relation | **KEEP** |
| RC-038 | IFGT balance / unified field equation | **KEEP** |

### Summary C — claim-level candidates

| Candidate | Claim | Action |
| --- | --- | --- |
| RC-012 | conditional monotonicity | **KEEP** |
| RC-013 | physical-time generation | **DOWNGRADE** |
| RC-014 | undifferentiated irreversibility | **SPLIT** |
| RC-015 | \(\sigma>0\) biconditional | **DOWNGRADE** |
| RC-017 | necessary difference-to-flow chain | **DOWNGRADE** |
| RC-021 | fixed point = persistent physical structure | **DOWNGRADE** |
| RC-024 | vorticity produces persistent enclosure | **DOWNGRADE** |
| RC-025 | unrestricted triangular minimality / uniqueness | **DOWNGRADE** |
| RC-026 | particle as model-defined energy minimum | **KEEP** |
| RC-029 | closure distance determines physical mass | **DOWNGRADE** |
| RC-031 | unconditional metric-property wording | **REVISE** |
| RC-032 | physical-space emergence | **DOWNGRADE** |
| RC-036 | Einstein-equation recovery | **DOWNGRADE** |
| RC-037 | gravity / spacetime emergence | **DOWNGRADE** |
| RC-039 | VED–IFGT unification | **DOWNGRADE** |
| RC-044 | finite dimensionality claims at declared scope | **KEEP** |

### Summary D — bridge candidates

| Candidate | Bridge | Action |
| --- | --- | --- |
| RC-005 | \(C_{ij}\to C(x,\tau)\) | **OPEN** |
| RC-006 | \(J_{ij}\to\mathbf J(x)\) | **OPEN** |
| RC-007 | \(\rho_i\to\rho(x,t)\) | **OPEN** |
| RC-008 | \(d_{ij}\to g_{\mu\nu}\) | **OPEN** |
| RC-009 | \(\dot\rho_i\to\sigma\) | **OPEN** |
| RC-010 | \(L,L_{ab}\to L_{\mu\nu}\) | **OPEN** |
| RC-040 | \(\tau\leftrightarrow\tau_{\mathrm{VED}}\) | **OPEN** |
| RC-041 | VED \(\sigma\leftrightarrow\) IFGT \(\sigma\) | **OPEN** |

### Summary E — source-identity candidates

| Candidate | Identity conflict | Action |
| --- | --- | --- |
| RC-001 | causal-log \(C_{ij}\) / closure-degree \(C_{ij}\) | **SPLIT** |
| RC-002 | Vol.1 \(t\) / IFGT effective \(t\) | **SPLIT** |
| RC-003 | Vol.1 \(\sigma\) / IFGT \(\sigma\) | **SPLIT** |
| RC-004 | \(L\) / \(L_{ab}\) / \(L_{\mu\nu}\) | **SPLIT** |

### Summary F — highest-priority candidates for 06

Priority is dependency order / audit importance, not severity.

| Priority | Candidates | Reason |
| --- | --- | --- |
| P1 | RC-001–010, RC-016, RC-020, RC-023, RC-040, RC-041 | source identity, bridge status and typing must precede dependent wording |
| P2 | RC-011–015, RC-017–019, RC-021–022, RC-024–039, RC-044 | equation scope and claim-strength alignment depend on P1 where noted |
| P3 | RC-042, RC-043 | navigation presentation depends on P1 and P2 decisions |

Counts:

| Priority | Count |
| --- | ---: |
| P1 | 15 |
| P2 | 27 |
| P3 | 2 |
| Total | 44 |

---

## 10. Handoff to phase 06

### 10.1 Candidate dispositions requiring final decision

All RC-001–044 require an explicit 06 disposition. The action in this document is proposed, not frozen.

### 10.2 Candidates with only one presently plausible action

- formal-scope preservation: RC-011, RC-012, RC-019, RC-022, RC-026, RC-028, RC-030,
  RC-033, RC-035, RC-038, RC-044;
- \(C_{ij}\) source-identity separation before downstream comparison: RC-001.

These remain candidates. “One presently plausible” means no competing action is supported by 01–04,
not that 06 must adopt them.

### 10.3 Candidates with multiple plausible actions

RC-002–004, RC-013–018, RC-020–025, RC-027, RC-029, RC-031, RC-032,
RC-034, RC-036, RC-037, RC-039, RC-042 and RC-043.

Typical alternatives are: explicit conditional wording versus leaving an interpretation open; separating a
compound claim versus lowering its total strength; or preserving a formal expression after its domain is
made explicit. 06 must choose without adding evidence that is not in the repository.

### 10.4 Candidates blocked by unresolved evidence

RC-005–010, RC-013, RC-015, RC-018, RC-020, RC-021, RC-024, RC-025,
RC-027, RC-029, RC-032, RC-036, RC-037, RC-039–041.

These are blocked by one or more of: source identity, formal bridge, stability / existence analysis,
operational physical map, quantitative derivation, or empirical evidence. Blocked does not mean impossible.

### 10.5 Candidates whose target should remain unchanged at candidate stage

RC-011, RC-012, RC-019, RC-022, RC-026, RC-028, RC-030, RC-033, RC-035,
RC-038 and RC-044 preserve supported formal or bounded content. Their stronger neighboring claims remain
separate targets and are not preserved by implication.

---

## 11. What phase 05 does not do

This record does not:

- implement any action;
- modify a VED, paper, IFGT, dimensionality, or navigation source;
- declare any candidate final;
- introduce a new equation, symbol family, bridge or theory;
- call an unsupported claim false;
- declare a missing bridge impossible;
- infer ontology from representation preload;
- validate or refute VED;
- reopen `generative_law_methodology`.

The minimal-change conclusion is procedural: supported formal objects can be preserved while source
identities, bridges and stronger physical claims receive separate decisions in 06.

---

## 12. Closure / current audit status

| Record | Status |
| --- | --- |
| `00_connection_record_v0.1_ja.md` | **COMPLETE** |
| `01_equation_inventory_v0.1_ja.md` | **COMPLETE** |
| `02_equation_role_audit_v0.1_ja.md` | **COMPLETE** |
| `03_preload_and_circularity_audit_v0.1_ja.md` | **COMPLETE** |
| `04_generation_claim_evidence_audit_v0.1_ja.md` | **COMPLETE** |
| `05_revision_candidates_v0.1_ja.md` | **COMPLETE** |
| `06_final_audit_record_v1.0_ja.md` | **NOT STARTED** |
| VED core revision | **NOT STARTED** |

\[
\boxed{\text{05 COMPLETE / 06 NOT STARTED}}
\]

Phase 05 stops here. No candidate has been implemented or finalized.

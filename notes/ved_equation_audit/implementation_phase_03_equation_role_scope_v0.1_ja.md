# VED core revision implementation Phase 03 — equation role / domain / scope v0.1

## 0. Status

- implementation phase: **03 — equation role / domain / scope clarification**
- status: **COMPLETE**
- authority: [06 final audit record v1.0](./06_final_audit_record_v1.0_ja.md)
- preceding implementations:
  - [Phase 01 symbol / source identity](./implementation_phase_01_symbol_identity_v0.1_ja.md) — **COMPLETE**
  - [Phase 02 bridge status](./implementation_phase_02_bridge_status_v0.1_ja.md) — **COMPLETE**
- implemented REVISE dispositions: **RC-016, RC-023, RC-031, RC-034**
- clarified KEEP dispositions: **RC-011, RC-019, RC-022, RC-028, RC-030, RC-033, RC-035, RC-038**
- audit branch: **CLOSED**
- core revision: **IN PROGRESS**
- Phase 04 physical / universality claim alignment: **NOT STARTED**
- displayed equation changed: **NO**
- bridge supplied: **NO**
- new equation / theory / notation: **NO**

This phase adds source-local documentation around existing expressions. It keeps the distinctions

\[
\text{equation role}\neq\text{physical interpretation},
\qquad
\text{domain declaration}\neq\text{ontological commitment},
\]

and does not reopen or alter the final audit dispositions.

## 1. Equation implementation table

| Equation ID | Expression | Role | Domain | Scope | Files changed | Deferred stronger claim |
| --- | --- | --- | --- | --- | --- | --- |
| EQ-GRAD | \(\nabla\delta,\ J\sim-\nabla\delta\) | DERIVED CONSTRUCTION / PHENOMENOLOGICAL / EFFECTIVE ANSATZ | CONTINUUM / LOCAL-FIELD REPRESENTATION | represented gradient and effective proportional flow relation; normalization and universal derivation are not supplied | Vol.1 minimal axiom and EN/JA guides | RC-017 necessity; RC-018 pre-geometric reading |
| EQ-TIME | \(d\tau_i/dt=\rho_i\) | DEFINITION | DISCRETE NODE / NETWORK with derivative parameter \(t\) | node-local time-like accumulation relative to \(t\); conditional non-decrease for \(\rho_i\geq0\); no clock identity | Vol.1 time source, overview, core equation summary and EN/JA guides | RC-013 physical time; RC-014 irreversibility |
| EQ-FIX | causal-log / \(\rho_i\) self-consistency system | CONSTITUTIVE / CLOSURE RELATION; proposed fixed-point target | NODE-INDEXED SELF-CONSISTENCY | not by itself an update map; no existence, uniqueness, convergence or stability theorem | Vol.1 time source, core summary and EN/JA guides | RC-020 update semantics; RC-021 persistent structure |
| EQ-CONT | \(\partial_t\rho+\nabla\cdot\mathbf J=\sigma\) | BALANCE / CONTINUITY RELATION | CONTINUUM FIELD REPRESENTATION | source-bearing balance equation, not unconditional conservation and not physical-time evidence | Vol.1 flow source and EN/JA guides | RC-015 biconditional; RC-014 physical irreversibility |
| EQ-VORT | \(\omega=\nabla\times\mathbf J\) | DEFINITION / DERIVED CONSTRUCTION | CONTINUUM FIELD REPRESENTATION supporting curl | vorticity of represented flow; no persistence theorem | Vol.1 flow source, overview and EN/JA/Vol.3 guides | RC-024 enclosure |
| EQ-L | \(L\sim\lvert\omega\rvert\) | PHENOMENOLOGICAL / EFFECTIVE ANSATZ | CONTINUUM FIELD REPRESENTATION; scalar \(L\) | effective proportional scalar measure; magnitude convention and normalization remain unspecified | Vol.1 flow source, overview and EN/JA/Vol.3 guides | RC-021/024 persistent enclosure |
| EQ-BARRIER | \(L<L_{\max}\), \(B(L)\) | LAW-LIKE CONSTRAINT / PHENOMENOLOGICAL / EFFECTIVE ANSATZ | PHENOMENOLOGICAL MODEL | modeled non-closure constraint and effective barrier encoding; no microscopic derivation | Vol.1 minimal axiom and EN/JA guides | physical interpretation of non-closure |
| EQ-ENERGY | \(E(A)\) | DEFINITION | PHENOMENOLOGICAL CLOSURE MODEL | model energy / scoring functional for configurations; physical particle identity is separate | Vol.1 closure source; Vol.2 closure-energy source and EN/JA guides | RC-027 particle identity |
| EQ-MASS | \(m_k\sim\kappa_B/\Delta_k^2\) | PHENOMENOLOGICAL / EFFECTIVE ANSATZ | PHENOMENOLOGICAL CLOSURE-BARRIER MODEL | qualitative barrier-based scaling only; no observed-mass calibration | Vol.1 closure source; Vol.2 particle source; overview and EN/JA guides | RC-029 physical mass |
| EQ-DIST | \(\widetilde S_{ij}\), \(d_{ij}=-\log\widetilde S_{ij}\) | DERIVED CONSTRUCTION | WEIGHTED PATH / GRAPH REPRESENTATION | admissible-path, max-product / min-sum path construction; physical space is not part of the definition | Vol.1 space source, overview/core and EN/JA/Vol.3 guides | RC-032 physical space |
| EQ-METRIC | metric-property wording for \(d_{ij}\) | conditional mathematical-property statement | WEIGHTED PATH / GRAPH REPRESENTATION | nonnegativity / triangle inequality only under stated path and edge conditions; ordinary metricity additionally needs symmetry, finite values and identity of indiscernibles | Vol.1 space source, overview/core and EN/JA guides | formal classification outside the stated cases |
| EQ-COARSE | \(d(x,y)^2\approx g_{\mu\nu}\Delta x^\mu\Delta x^\nu\) | PHENOMENOLOGICAL / EFFECTIVE ANSATZ | EFFECTIVE COARSE CONTINUUM | effective local endpoint; no reconstruction, uniqueness or physical-space theorem | Vol.1 space source and EN/JA guides | RC-032 physical space; RC-008 bridge |
| EQ-GRAV | \(\nabla^2\Psi\propto L,\ g=-\nabla\Psi\) | PHENOMENOLOGICAL / EFFECTIVE ANSATZ | CONTINUUM SCALAR-FIELD REPRESENTATION | weak-field / structural analogy; coefficients, units and boundary assumptions not fully fixed; no discrete derivation or exact GR recovery | overview, Vol.3 Schwarzschild source and EN guide | RC-036 exact recovery; RC-037 gravity / spacetime emergence |
| EQ-GFIX | \(g_{\mu\nu}=g^{(0)}_{\mu\nu}+\alpha_G L_{\mu\nu}[g]\) | CONSTITUTIVE / CLOSURE RELATION; proposed fixed-point target | EFFECTIVE COARSE CONTINUUM | formal self-consistency target; no solution, existence, uniqueness, convergence or stability theorem | Vol.3 fixed-point source and EN/JA guides; Vol.1 JA summary | RC-036/037 physical recovery / emergence |
| EQ-IFGT | IFGT balance and unified \(C(x,\tau)\) equations | BALANCE / CONTINUITY RELATION / UPDATE / EVOLUTION RULE | RELATED-BRANCH IFGT FIELD MODEL | internal IFGT evolution under its declared linear / phenomenological assumptions; cross-theory identity is not an equation role | IFGT EN/JA records and TeX equation sources | RC-039 unification; RC-040/041 bridges |

The role labels reproduce the vocabulary of
[02 equation-role audit](./02_equation_role_audit_v0.1_ja.md). They are documentation labels, not
new formal objects.

## 2. Domain / precondition matrix

| Expression | Required representation / domain | Explicit in source after Phase 03? | Still missing | Consequence |
| --- | --- | --- | --- | --- |
| \(\nabla\delta\), \(J\sim-\nabla\delta\) | local field / neighborhood with a gradient operator | YES, representation level | normalization and a stronger derivation | use only as represented gradient / effective proportional relation |
| \(d\tau_i/dt=\rho_i\) | node-indexed quantities and derivative / order parameter \(t\) | YES | physical clock map | mathematical accumulation statement remains separate from physical time |
| causal-log fixed point | node carrier, \(H_{ij},C_{ij},\rho_i,\lambda\), solution concept | PARTIAL | solution / update specification | formal self-consistency target only |
| continuum balance | continuum density, vector field, divergence, source and \(t\) | YES at target representation | discrete bridge and full field-domain conditions | retain equation internally; do not infer a discrete derivation |
| \(\nabla\times\mathbf J\) | continuum vector-field setting supporting curl | YES | detailed dimension / orientation / boundary conditions | definition is retained without a persistence theorem |
| \(L\sim\lvert\omega\rvert\) | scalar magnitude convention and proportionality normalization | PARTIAL | norm and normalization | effective proportional measure only |
| \(L<L_{\max}\), \(B(L)\) | scalar phenomenological closure model and admissible domain | YES | microscopic origin | constraint / effective barrier only |
| \(E(A)\) | configuration set, model terms and scoring parameters | YES | observational particle map | model functional remains separate from particle identity |
| mass scaling | closure deficit and phenomenological barrier regime | YES | units, calibration and physical map | qualitative phenomenological scaling only |
| network distance | graph, admissible paths, edge strengths and log domain | YES | global policy in disconnected / directed cases | classify only under declared conditions |
| coarse metric endpoint | coordinates / blocks and effective tensor representation | PARTIAL | reconstruction, convergence, scaling, normalization, uniqueness | partial / OPEN bridge remains |
| weak-field gravity relations | continuum scalar field with gradient / Laplacian and boundary data | PARTIAL | coefficients, units and complete derivation | effective / analogical scope only |
| metric fixed point | effective tensor fields and the functional \(L_{\mu\nu}[g]\) | PARTIAL | bridge-dependent functional and solution theory | proposed fixed-point target only |
| IFGT equations | IFGT continuum fields, \(\tau\), gradients / divergence and stated assumptions | YES internally | VED translation maps | internal algebra retained; cross-theory inference blocked |

Still missing is not an invalidity verdict. It limits the inference that may be drawn from the displayed
expression.

## 3. Phase-02 bridge truth table preserved

| Candidate | Relation | Phase-03 result |
| --- | --- | --- |
| RC-005 | \(C_{ij}\to C(x,\tau)\) | **OPEN — unchanged** |
| RC-006 | \(J_{ij}\to\mathbf J(x)\) | **OPEN — unchanged** |
| RC-007 | \(\rho_i\to\rho(x,t)\) | **OPEN — unchanged** |
| RC-008 | \(d_{ij}\to g_{\mu\nu}\) | **PARTIAL / OPEN — unchanged** |
| RC-009 | \(\dot\rho_i\to\sigma\) | **PROPOSED / INFORMAL; OPEN — unchanged** |
| RC-010 | \(L,L_{ab}\to L_{\mu\nu}\) | **PARTIAL / OPEN — unchanged** |
| RC-040 | \(\tau\leftrightarrow\tau_{\mathrm{VED}}\) | **PROPOSED CORRESPONDENCE / OPEN — unchanged** |
| RC-041 | VED \(\sigma\leftrightarrow\) IFGT \(\sigma\) | **PROPOSED CORRESPONDENCE / OPEN — unchanged** |

No domain or role annotation upgrades correspondence into a map, embedding, continuum limit or identity.

## 4. Files modified

| File group | Phase-03 clarification |
| --- | --- |
| [docs/core_equations.md](../../docs/core_equations.md), [docs/00_overview.md](../../docs/00_overview.md) | compact role/domain/scope qualifications for time, fixed point, distance, vorticity, \(L\), mass and weak-field gravity |
| [docs/vol1_foundations.md](../../docs/vol1_foundations.md), [docs/vol1_foundations_ja.md](../../docs/vol1_foundations_ja.md) | matching node/network, continuum, effective and phenomenological scopes |
| [paper/vol1/sections/minimal_axiom.tex](../../paper/vol1/sections/minimal_axiom.tex), [causal_logs_time.tex](../../paper/vol1/sections/causal_logs_time.tex), [flow_vorticity.tex](../../paper/vol1/sections/flow_vorticity.tex), [closure.tex](../../paper/vol1/sections/closure.tex), [space.tex](../../paper/vol1/sections/space.tex) | canonical Vol.1 equation contexts clarified |
| [docs/vol2_standard_model.md](../../docs/vol2_standard_model.md), [docs/vol2_standard_model_ja.md](../../docs/vol2_standard_model_ja.md), [paper/vol2/sections/closure_energy.tex](../../paper/vol2/sections/closure_energy.tex), [particle_classification.tex](../../paper/vol2/sections/particle_classification.tex) | \(E(A)\) and mass scaling kept in model / phenomenological scope |
| [docs/vol3_gravity_cosmology.md](../../docs/vol3_gravity_cosmology.md), [docs/vol3_gravity_cosmology_ja.md](../../docs/vol3_gravity_cosmology_ja.md), [paper/vol3/sections/gravity_distance.tex](../../paper/vol3/sections/gravity_distance.tex), [einstein_equation.tex](../../paper/vol3/sections/einstein_equation.tex), [schwarzschild.tex](../../paper/vol3/sections/schwarzschild.tex) | path construction, continuum vorticity, weak-field analogy and fixed-point target scoped |
| [Information-Field-Geometry-Theory/ifgt_en.md](../../Information-Field-Geometry-Theory/ifgt_en.md), [ifgt_ja.md](../../Information-Field-Geometry-Theory/ifgt_ja.md), [sections/fundamental_dynamics.tex](../../Information-Field-Geometry-Theory/sections/fundamental_dynamics.tex), [sections/unified_equation.tex](../../Information-Field-Geometry-Theory/sections/unified_equation.tex) | IFGT-internal equation roles separated from cross-theory claims |

## 5. Inspected but unchanged

| Area | Reason |
| --- | --- |
| [paper/vol3/sections/closure_density.tex](../../paper/vol3/sections/closure_density.tex) | Phase 01/02 already states carrier identities and the partial / OPEN metric and tensor bridges; no additional equation-role edit was necessary |
| [docs/claims.md](../../docs/claims.md) | physical and universality claim alignment is Phase 04 |
| [docs/navigation/generative_sequence.md](../../docs/navigation/generative_sequence.md) and compact chains | RC-042/043 arrow semantics are deferred |
| top-level README.md / README_ja.md | final synchronization follows upstream claim and chain work |
| [docs/correspondences.md](../../docs/correspondences.md) and exact-recovery prose | RC-036/037 physical correspondence is deferred |
| AI Spine / generated artifacts | not manually edited; source-of-truth synchronization remains later |
| audit records 00–06 | frozen authority; unchanged |
| generative_law_methodology/ | remains CLOSED / STOP-A; unchanged |

## 6. Deferred stronger-claim ledger

| Candidate | Deferred issue | Phase-03 boundary |
| --- | --- | --- |
| RC-013 | physical-time emergence | equation is now scoped relative to \(t\); claim action not implemented |
| RC-014 | monotonicity / non-reconstructibility / thermodynamic irreversibility / physical arrow | distinctions remain for Phase 04 |
| RC-015 | \(\sigma>0\) biconditional | unchanged in this phase |
| RC-017 | difference-to-flow necessity | equation role clarified; universality action deferred |
| RC-021 | fixed point to persistent physical structure | no solution theorem imported; claim action deferred |
| RC-024 | vorticity to enclosure / persistence | definition separated; physical mechanism action deferred |
| RC-025 | triangular minimality | not changed |
| RC-027 | local energy minimum to observed particle | model functional separated; identification action deferred |
| RC-029 | phenomenological scale to physical mass | phenomenological scope retained; identification action deferred |
| RC-032 | network distance / coarse metric to physical space | equation roles separated; emergence action deferred |
| RC-036 | Einstein recovery | weak-field role scoped; recovery claim action deferred |
| RC-037 | gravity / spacetime emergence | not implemented |
| RC-039 | VED–IFGT unification | internal IFGT algebra separated; cross-theory claim action deferred |
| RC-042 / RC-043 | compact generative chain and arrow semantics | no chain rewrite in Phase 03 |

## 7. Consistency result

- Gradient operator/domain wording is present.
- The local-time equation is a definition relative to \(t\), not a clock theorem.
- Fixed-point equations are formal self-consistency targets, not update / solution / stability theorems.
- The continuum equation is a source-bearing balance relation, not unconditional conservation.
- Vorticity is a continuum definition; \(L\sim|\omega|\) is an effective proportional relation.
- Non-closure barrier and mass scaling retain phenomenological scope.
- Network distance is a weighted-path construction; ordinary metricity is conditional.
- The coarse metric is an effective endpoint and its bridge remains OPEN.
- Weak-field gravity relations are continuum analogies, not discrete derivations or exact recovery.
- The metric fixed point is a proposed target with no solution theorem.
- IFGT equations retain internal algebraic scope without upgrading VED correspondence.

## 8. Closure

~~~text
Core revision implementation:
Phase 01 symbol / source identity separation: COMPLETE
Phase 02 bridge-status annotation: COMPLETE
Phase 03 equation role / domain / scope clarification: COMPLETE
Phase 04 physical / universality claim alignment: NOT STARTED
Audit branch: CLOSED
Core revision: IN PROGRESS
~~~

Phase 03 changes documentation around existing equations only. Phase 04 has not been started.

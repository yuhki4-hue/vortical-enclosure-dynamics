# VED core revision implementation Phase 05 — generative-chain / navigation role separation v0.1

## 0. Status

- implementation phase: **05 — generative-chain / navigation role separation**
- status: **COMPLETE**
- authority: [06 final audit record v1.0](./06_final_audit_record_v1.0_ja.md)
- preceding implementations:
  - [Phase 01 symbol / source identity](./implementation_phase_01_symbol_identity_v0.1_ja.md) — **COMPLETE**
  - [Phase 02 bridge status](./implementation_phase_02_bridge_status_v0.1_ja.md) — **COMPLETE**
  - [Phase 03 equation role / domain / scope](./implementation_phase_03_equation_role_scope_v0.1_ja.md) — **COMPLETE**
  - [Phase 04 physical / universality claim alignment](./implementation_phase_04_claim_alignment_v0.1_ja.md) — **COMPLETE**
- RC-042 compact / wider chain: **SPLIT implemented**
- RC-043 “generative chain” strength: **DOWNGRADE implemented**
- audit branch: **CLOSED**
- core revision: **IN PROGRESS**
- Phase 06 repository-wide synchronization: **NOT STARTED**
- new theory / equation / bridge / notation / evidence: **NO**
- physical claim upgraded: **NO**

この実装では、compact chainのdisplayed expressionを変更せず、各edgeをdefinition、derived
construction、effective relation、OPEN bridge、candidate physical interpretationへ分離した。
arrowに新しいformal semanticsは与えていない。

保持する原則は次である。

\[
\text{navigation order}
\neq
\text{proof order}
\neq
\text{formal dependency}
\neq
\text{physical generation},
\]

\[
\text{one arrow glyph}
\not\Rightarrow
\text{one logical relation}.
\]

## 1. Canonical navigation implementation

[Generative Sequence](../../docs/navigation/generative_sequence.md)を、単一rank / uniform-arrow
presentationからcanonical relation-role tableとlayered navigationへ変更した。各relationについて、
source、target、relation type、representation、audit status、許されない推論を明示した。

「generation」はprojectのorganizing questionとして残すが、formal construction、candidate
mechanism、proposed physical interpretation、navigation / genealogyを同一視しない。

## 2. Relation-role table

| Relation ID | Source | Target | Previous reading | Final navigation role | Formal status | Physical status | Files changed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| REL-01 | difference | navigation closure-degree \(C_{ij}\) | first generated object | source-local first formal carrier | navigation role; cross-source identity absent | physical generation not established | generative sequence, concept map |
| REL-02 | represented \(\delta\) | \(\nabla\delta\) | difference generates gradient | represented-field construction | scoped to a field domain | necessity / pre-geometric reading OPEN | generative sequence, core equations, Vol.1 guide |
| REL-03 | \(\nabla\delta\) | \(J\sim-\nabla\delta\) | gradient generates flow | effective proportional relation | formal / effective relation | candidate directional-flow description | generative sequence, core equations, Vol.1 guide |
| REL-04 | \(H_{ij},\rho_i\) | causal-log \(C_{ij}\) | one generative step | constitutive / self-consistency relation | formal target KEEP | persistence interpretation separate | generative sequence, Vol.1 guide / paper |
| REL-05 | \(C_{ij}\) | \(\rho_i\) | generated density | nodewise definition | formal definition KEEP | continuum / physical-density identity absent | generative sequence, Vol.1 guide / paper |
| REL-06 | \(\rho_i\) | \(\tau_i\) | physical time generated | accumulation definition relative to \(t\) | formal relation KEEP | physical-clock interpretation DOWNGRADED / OPEN | generative sequence, Vol.1 guide / paper |
| REL-07 | \(C_{ij}\) | \(S_{ij},A_{ij}\) | spatial and dynamical stages | algebraic decomposition | formal construction KEEP | physical meanings not implied | generative sequence |
| REL-08 | \(C_{ij},C_{ji}\) | \(J_{ij}\) | flow generated | discrete definition | formal definition KEEP | continuum / physical flow identity absent | generative sequence, core equations, Vol.1 guide / paper |
| REL-09 | \(J_{ij}\) | \(\mathbf J(x)\) | continuum limit completed | informal representation transition | OPEN bridge | no established continuum physical flow map | generative sequence, core equations, Vol.1/Vol.3 guide / paper |
| REL-10 | \(\mathbf J(x)\) | \(\omega\) | vortex physically generated | definition / derived curl construction | formal definition KEEP | persistence / enclosure not implied | generative sequence, core equations, Vol.1/Vol.3 guide / paper |
| REL-11 | \(\omega\) | scalar \(L\) | closure generated | effective / phenomenological proportional relation | scoped ansatz | enclosure is a candidate mechanism | generative sequence, core equations, Vol.1/Vol.3 guide / paper |
| REL-12 | \(S_{ij}\) | \(\widetilde S_{ij},d_{ij}\) | space generated | weighted-network path construction | formal construction KEEP under assumptions | physical space OPEN | generative sequence, core equations, Vol.1 guide / paper |
| REL-13 | \(d_{ij}\) | \(g_{\mu\nu}\) | metric derived seamlessly | partial coarse endpoint | PARTIAL / OPEN bridge | physical-space emergence OPEN | generative sequence, core equations, Vol.3 guide / paper |
| REL-14 | scalar \(L\) / edge \(L_{ab}\) | \(L_{\mu\nu}\) | automatic tensorization | carrier / coarse correspondence | OPEN bridge | no tensorial physical identity | generative sequence, Vol.3 guide / paper |
| REL-15 | \(L_{ab}\) and path cost | gravity-like distance bias | gravity produced | formal path modification plus candidate interpretation | construction KEEP | observed gravity OPEN | generative sequence, Vol.3 guide / paper |
| REL-16 | \(L\) or \(L_{\mu\nu}[g]\) | weak-field / metric target | Einstein equation derived | effective analogy / proposed fixed point | formal target KEEP | exact recovery DOWNGRADED / OPEN | generative sequence, Vol.3 guide / paper |
| REL-17 | local minimum of \(E(A)\) | particle-like / mass-like candidate | observed matter generated | model definition plus phenomenological relation | model-local content KEEP | observational identity OPEN | generative sequence, Vol.2 guide / paper |
| REL-18 | source-local \(C_{ij}\) | IFGT \(C(x,\tau)\) | same closure variable / unified theory | proposed formal correspondence | RC-005 OPEN | matrix-to-field identity and unification not established | generative sequence |
| REL-19 | IFGT \(\tau\) | \(\tau_{\mathrm{VED}}\) | dynamically isomorphic time | proposed temporal correspondence | RC-040 OPEN | embedding, isomorphism, and physical-time identity not established | generative sequence |
| REL-20 | VED \(\sigma\) | IFGT \(\sigma\) | same source process | proposed source-term correspondence | RC-041 OPEN | translation and source identity not established | generative sequence |
| REL-21 | \(\rho_i\) | \(\rho(x,t)\) | continuum density follows | informal representation transition | RC-007 OPEN | interpolation, normalization, units, and identity of \(t\) absent | generative sequence |
| REL-22 | \(\dot\rho_i\) | Vol.1 continuum \(\sigma\) | microscopic source becomes continuum source | proposed microscopic / continuum correspondence | RC-009 OPEN | projection, averaging, and unit map absent | generative sequence |

## 3. Layered-chain table

| Layer | Included relations | Allowed inference | Forbidden inference |
| --- | --- | --- | --- |
| formal / model-local construction | REL-01–02, REL-04–08, REL-10, REL-12 and formal parts of REL-15–17 | the quantity or target is organized, defined, or constructed in its stated domain | physical generation follows automatically |
| bridge / representation transition | REL-09, REL-13, REL-14, REL-18–22 | a proposed relation or endpoint is identified for audit | map, continuum limit, tensorization, embedding, or equivalence is complete |
| effective / phenomenological relation | REL-03, REL-11 and effective parts of REL-15–17 | the scoped relation organizes a model or comparison | universal necessity or exact physical recovery |
| physical interpretation | time, enclosure, particle, space, gravity / spacetime, IFGT relation | candidate interpretations remain explicit research targets | the formal sequence proves physical emergence |

このlayeringは新しいformal hierarchyではなく、Phase 01–04で確定した既存role / bridge /
claim statusをnavigation上で見えるようにするdocumentation structureである。

## 4. Arrow-semantics audit

| Arrow / wording form | Where used | Previous ambiguity | Phase-05 resolution |
| --- | --- | --- | --- |
| \(\to\) | compact Vol.1–3 and core summaries | definition、bridge、ansatz、physical interpretationが同一に見える | compact displayはmnemonicと明示し、local relation tableへ分解 |
| “generative chain” | core / navigation / Vol.1 | every edgeがcausal generation mechanismに見える | canonical titleをrole-separated navigationへ変更し、historical usesをscoped summaryへ変更 |
| “generates” | overview / chapter summaries | formal constructionからphysical emergenceまでを覆う | source-local formal contentとcandidate physical interpretationを分離 |
| “becomes” / “continuum limit” | discrete-to-continuum prose | explicit mapがあるように見える | INFORMAL / OPEN bridgeをnavigationにも表示 |
| “leads to” / “follows” | volume-level progressions | navigation orderがproof / necessityに見える | reading or program orderとして限定し、relation roleを併記 |
| “emerges” / “corresponds to” / “unified” | physical and IFGT endpoints | physical emergenceやcross-theory equivalenceが成立済みに見える | proposed interpretation / proposed correspondenceとして表示し、OPEN mapを維持 |

このauditはglyphごとにuniversal semanticsを割り当てない。contextごとのrole labelを要求する。

## 5. Files changed

| Area | Phase-05 change |
| --- | --- |
| [docs/navigation/generative_sequence.md](../../docs/navigation/generative_sequence.md) | canonical relation-role table、4-layer navigation、compact-chain reading ruleを導入 |
| [docs/navigation/concept_map.md](../../docs/navigation/concept_map.md) | role-separated recordをhuman-readable authorityとして指定し、AI Spine同期をdefer |
| [docs/core_equations.md](../../docs/core_equations.md) | compact chainをmnemonicとしてscopeし、edge-role tableを追加 |
| [docs/00_overview.md](../../docs/00_overview.md) | volume arrowsをreading orderとして限定 |
| [docs/vol1_foundations.md](../../docs/vol1_foundations.md), [docs/vol1_foundations_ja.md](../../docs/vol1_foundations_ja.md) | causal log、flow、vorticity、closure、time、distanceのedge roleを分離 |
| [paper/vol1/sections](../../paper/vol1/sections/) | introduction / flow / conclusionのcompact chainをrole-separated mnemonicとしてscope |
| [docs/vol2_standard_model.md](../../docs/vol2_standard_model.md), [docs/vol2_standard_model_ja.md](../../docs/vol2_standard_model_ja.md), [paper/vol2/sections/conclusion.tex](../../paper/vol2/sections/conclusion.tex) | finite closure construction、structural comparison、physical targetを分離 |
| [docs/vol3_gravity_cosmology.md](../../docs/vol3_gravity_cosmology.md), [docs/vol3_gravity_cosmology_ja.md](../../docs/vol3_gravity_cosmology_ja.md), [paper/vol3/sections](../../paper/vol3/sections/) | discrete definition、OPEN bridges、effective metric / Einstein comparison、cosmological interpretationを分離 |

## 6. Inspected but unchanged

| Area | Reason unchanged in Phase 05 |
| --- | --- |
| top-level README.md / README_ja.md | final repository synchronization is reserved for implementation Phase 06 |
| docs/ai_spine/spine.json and generated order files | machine source and generated artifacts require coordinated regeneration in Phase 06; no manual patch |
| paper/vol1/figures/fig1_generative_chain.svg and rendered figure | generated / visual artifact synchronization deferred; paper caption already marks mixed roles |
| docs/open_problems.md | no compact chain requiring RC-042 / RC-043 correction located |
| IFGT source files | Phase 01–04 already mark cross-theory relation as proposed and OPEN; no additional seamless navigation chain located |

## 7. OPEN bridge preservation

| Candidate | Relation | Phase-05 navigation status |
| --- | --- | --- |
| RC-005 | \(C_{ij}\to C(x,\tau)\) | **OPEN — unchanged** |
| RC-006 | \(J_{ij}\to\mathbf J(x)\) | **INFORMAL / OPEN — shown explicitly** |
| RC-007 | \(\rho_i\to\rho(x,t)\) | **INFORMAL / OPEN — unchanged** |
| RC-008 | \(d_{ij}\to g_{\mu\nu}\) | **PARTIAL / OPEN — shown explicitly** |
| RC-009 | \(\dot\rho_i\to\sigma\) | **PROPOSED / INFORMAL; OPEN — unchanged** |
| RC-010 | \(L,L_{ab}\to L_{\mu\nu}\) | **PARTIAL / OPEN — shown explicitly** |
| RC-040 | \(\tau\leftrightarrow\tau_{\mathrm{VED}}\) | **PROPOSED CORRESPONDENCE / OPEN — unchanged** |
| RC-041 | VED \(\sigma\leftrightarrow\) IFGT \(\sigma\) | **PROPOSED CORRESPONDENCE / OPEN — unchanged** |

Navigationはこれらをdefinitionやcompleted continuum limitと同じedge statusで表示しない。

## 8. Phase-04 claim ceilings preserved

- physical time: accumulation definitionから分離されたproposed / OPEN interpretation
- irreversibility: monotonicity、non-reconstructibility、thermodynamic sense、physical arrowを非同一化
- persistence / enclosure: candidate mechanism
- particle / mass: model-defined candidate / phenomenological scaling
- physical space: network constructionから分離されたOPEN interpretation
- Einstein recovery: structural analogy / intended weak-field target
- gravity / spacetime: proposed physical interpretation
- VED–IFGT: proposed formal correspondence; bridges OPEN

compact diagramはこれらのceilingを上書きしない。

## 9. Deferred synchronization ledger

| Deferred item | Phase-05 status | Next handling |
| --- | --- | --- |
| top-level README.md / README_ja.md | duplicated compact chains and high-level generation wording remain | Phase 06 repository-wide synchronization |
| AI Spine machine source | legacy rank / “generated” semantics remain in spine.json | Phase 06 source-of-truth review before regeneration |
| AI Spine generated Markdown / JSON | generated from the legacy machine source | Phase 06 regeneration; do not patch manually |
| generated / rendered diagrams | historical uniform-arrow graphics remain | Phase 06 source update / regeneration decision |
| duplicated compact summaries not selected for direct Phase-05 editing | canonical table now governs semantics | Phase 06 cross-language and repository-wide scan |
| historical titles containing “generative” or “unified” | title alone retained | Phase 06 checks local scope notes; no automatic rename |
| stale or cross-language navigation links | none promoted here | Phase 06 final link synchronization |

## 10. Consistency result

- canonical navigation distinguishes relation type, representation, bridge status, and physical ceiling for 22 relations.
- edited compact chains are identified as mnemonics or program / reading order, not uniform derivations.
- formal definitions and weighted-network constructions remain intact.
- effective / phenomenological relations are not presented as universal identities.
- all eight frozen bridge candidates remain OPEN.
- candidate physical interpretations are shown separately from the formal edges that motivate them.
- no new arrow notation, formal calculus, equation, bridge, or evidence was introduced.
- residual top-level and generated-output synchronization is explicitly deferred rather than silently treated as complete.

## 11. Validation

- repository-local Markdown links: **PASS**
- Markdown fences and display-math delimiters: **PASS**
- tables in Phase-05 Markdown targets: **PASS**
- Vol.1 / Vol.2 / Vol.3 temporary LaTeX builds: **PASS**
- `git diff --check`: **PASS**
- RC-042 / RC-043 traceability to 06: **PASS**
- RC-005–010 and RC-040–041 remain OPEN: **PASS**
- displayed VED equations, coefficients, symbols, operators, indices, and functional forms changed: **NO**

## 12. Closure

~~~text
Core revision implementation:
Phase 01 symbol / source identity separation: COMPLETE
Phase 02 bridge-status annotation: COMPLETE
Phase 03 equation role / domain / scope clarification: COMPLETE
Phase 04 physical / universality claim alignment: COMPLETE
Phase 05 generative-chain / navigation role separation: COMPLETE
Phase 06 repository-wide synchronization: NOT STARTED
Audit branch: CLOSED
Core revision: IN PROGRESS
~~~

Phase 05 implements RC-042 and RC-043 only. The next implementation phase is
repository-wide synchronization / top-level README / generated-navigation
alignment; it has not been started.

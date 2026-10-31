# Consciousness Phase 03 — preload / observer boundary / self-reference / circularity audit v0.1

## 0. Status

```text
Consciousness audit: IN PROGRESS
Phase 00 dependency / inheritance / source authority: COMPLETE
Phase 01 equation / symbol / object inventory: COMPLETE
Phase 02 formal / neural / cognitive / phenomenal role audit: COMPLETE
Phase 03 preload / observer boundary / self-reference / circularity audit: COMPLETE
Phase 04 claim / evidence burden audit: NOT STARTED
Upstream VED equation audit / core revision: CLOSED / CLOSED
Upstream Bio-IFGT audit / core revision: CLOSED / CLOSED
```

2026-09-09、current repositoryに対する構造監査。source・式・notation・図・PDF・code・過去の監査は変更しない。循環の型と候補の重大性を今回初めて分類するが、理論の真偽、実証適合・証拠十分性、現象的説明の最終成否、claim dispositionは扱わない。ID・P/C分類は監査用であり理論の新notationではない。

結論の範囲：feedbackと初期化問題、定義とphenomenal説明、相互引用と支持循環を分離した。source-level vicious circularityは確立していない。qualiaのphenomenal endpointを説明前提に含む一件をSERIOUSなclaim-threatening candidateとして保持する。これは説明失敗の最終判定ではない。

## 1. Authority

[Phase 00](00_dependency_inheritance_and_authority_record_v0.1_ja.md)、[Phase 01](01_equation_symbol_object_inventory_v0.1_ja.md)、[Phase 02](02_formal_neural_cognitive_phenomenal_role_audit_v0.1_ja.md)、[README](README_ja.md)を起点に、current modular EN/JAを再照合した。Phase02の40 transitions、24 conflations、20 conflicts、57 NS familiesをhistorical authorityとして保存する。

[VED final audit](../ved_equation_audit/06_final_audit_record_v1.0_ja.md)、[Bio final audit](../bio_ifgt_audit/07_final_audit_record_v1.0_ja.md)、[Bio closure recheck](../bio_ifgt_audit/implementation_final_consistency_recheck_v1.1_ja.md)のclosureをConsciousnessの成立へ継承しない。current [IFGT field](../../Information-Field-Geometry-Theory/sections/fundamental_dynamics.tex)、[IFGT persistence](../../Information-Field-Geometry-Theory/sections/unified_equation.tex)、[Bio life region](../../bio-ifgt/sections/life_attractor.tex)、[Bio second attractor](../../bio-ifgt/sections/intelligence_second_attractor.tex)は上流所在であり、本phaseで再監査・修正しない。

以下のS00–S20は同番号EN/JAのsource pair。特記しない短縮locatorは下表の当該小見出し・引用語句を指す。式番号はPhase01のCON-EQ、役割番号はPhase02のCON-RT等を保持する。working draftとcurrent sourceを統合しない。

| Source | EN | JA |
| --- | --- | --- |
| S00 | [S00 EN](../../consciousness/sections/abstract.tex) | [S00 JA](../../consciousness/sections_ja/abstract_ja.tex) |
| S01 | [S01 EN](../../consciousness/sections/introduction.tex) | [S01 JA](../../consciousness/sections_ja/introduction_ja.tex) |
| S02 | [S02 EN](../../consciousness/sections/intuitive_picture.tex) | [S02 JA](../../consciousness/sections_ja/intuitive_picture_ja.tex) |
| S03 | [S03 EN](../../consciousness/sections/notation.tex) | [S03 JA](../../consciousness/sections_ja/notation_ja.tex) |
| S04 | [S04 EN](../../consciousness/sections/sso.tex) | [S04 JA](../../consciousness/sections_ja/sso_ja.tex) |
| S05 | [S05 EN](../../consciousness/sections/torque_converter_attention.tex) | [S05 JA](../../consciousness/sections_ja/torque_converter_attention_ja.tex) |
| S06 | [S06 EN](../../consciousness/sections/formal_mapping.tex) | [S06 JA](../../consciousness/sections_ja/formal_mapping_ja.tex) |
| S07 | [S07 EN](../../consciousness/sections/core_equations.tex) | [S07 JA](../../consciousness/sections_ja/core_equations_ja.tex) |
| S08 | [S08 EN](../../consciousness/sections/structural_interpretation.tex) | [S08 JA](../../consciousness/sections_ja/structural_interpretation_ja.tex) |
| S09 | [S09 EN](../../consciousness/sections/dynamics_log_referencing.tex) | [S09 JA](../../consciousness/sections_ja/dynamics_log_referencing_ja.tex) |
| S10 | [S10 EN](../../consciousness/sections/experimental_reinterpretation.tex) | [S10 JA](../../consciousness/sections_ja/experimental_reinterpretation_ja.tex) |
| S11 | [S11 EN](../../consciousness/sections/qualia_boundary.tex) | [S11 JA](../../consciousness/sections_ja/qualia_boundary_ja.tex) |
| S12 | [S12 EN](../../consciousness/sections/opening_model.tex) | [S12 JA](../../consciousness/sections_ja/opening_model_ja.tex) |
| S13 | [S13 EN](../../consciousness/sections/measurement_collapse.tex) | [S13 JA](../../consciousness/sections_ja/measurement_collapse_ja.tex) |
| S14 | [S14 EN](../../consciousness/sections/non_localization.tex) | [S14 JA](../../consciousness/sections_ja/non_localization_ja.tex) |
| S15 | [S15 EN](../../consciousness/sections/qualitative_predictions.tex) | [S15 JA](../../consciousness/sections_ja/qualitative_predictions_ja.tex) |
| S16 | [S16 EN](../../consciousness/sections/pathologies_limits.tex) | [S16 JA](../../consciousness/sections_ja/pathologies_limits_ja.tex) |
| S17 | [S17 EN](../../consciousness/sections/relation_to_note.tex) | [S17 JA](../../consciousness/sections_ja/relation_to_note_ja.tex) |
| S18 | [S18 EN](../../consciousness/sections/discussion.tex) | [S18 JA](../../consciousness/sections_ja/discussion_ja.tex) |
| S19 | [S19 EN](../../consciousness/sections/conclusion.tex) | [S19 JA](../../consciousness/sections_ja/conclusion_ja.tex) |
| S20 | [S20 EN](../../consciousness/sections/correspondence_map.tex) | [S20 JA](../../consciousness/sections_ja/correspondence_map_ja.tex) |

Guards：preloaded representation ≠ illicit circularity; self-reference ≠ vicious circularity; feedback ≠ proof circularity; observer-like function ≠ generated phenomenal subject; boundary definition ≠ phenomenal boundary generated; consciousness window definition ≠ consciousness explanation; phenomenal label ≠ phenomenal bridge established; upstream inherited structure ≠ Consciousness-derived result。

「生成」はsourceの“opening / obtains / appears / maintained / interpreted”を含む監査対象語であり、sourceが否定する生成物モデルを監査者が再導入するものではない。

## 2. Preload taxonomy

| Type | Meaning | Not inferred |
| --- | --- | --- |
| P0 | representation / variable / category / bound / coordinate | 表現を採用しただけで循環とはしない |
| P1 | architecture / coupling / topology / pathway / partition | 構造の前提とその後の動態を分ける |
| P2 | prediction / memory / selection / meaning等の機能付与 | 神経実装・経験との同定を含めない |
| P3 | conscious / qualia / experienced ego等のendpoint label | phenomenalityの成立を認定しない |
| P4 | VED / IFGT / Bio / CT / four-layer inheritance | 上流導出済みという地位を含めない |

各PLに複数P型を許すためP0–P4合計はentry数を超える。severityは各行一つ：BENIGN REPRESENTATIONAL / STRUCTURALLY IMPORTANT / OUTPUT-SHAPING / OUTPUT-LOCATING / OUTPUT-LABELING / CLAIM-DEPENDENT / UNRESOLVED。OUTPUT-LOCATINGは機能的な「層の間／frontier」も含み、物理的脳位置を意味しない。C0–C8は§27のmasterだけで排他的に集計し、各sub-ledgerから同じ候補を重複加算しない。

## 3. Full preload inventory

| CON-PL | Object | Type | Source | Supplied before dynamics | Claimed later output | Severity |
| --- | --- | --- | --- | --- | --- | --- |
| CON-PL-001 | fast layer | P0,P1,P2 | S02/S04 | predictive/reactive layer and rate category | candidate activity and referenceable relation | STRUCTURALLY IMPORTANT |
| CON-PL-002 | slow layer | P0,P1,P2 | S04 | sedimentary/memory category | retained logs constrain later processing | STRUCTURALLY IMPORTANT |
| CON-PL-003 | Delta v | P0,P1 | S04/S07 | v_f/v_s and subtraction; finite-gap requirement | temporal nonclosure/window | OUTPUT-SHAPING |
| CON-PL-004 | mu | P0,P1 | S04/S05/S07 | coupling/viscosity role and allowed range | partial transformation not sync/separation | OUTPUT-SHAPING |
| CON-PL-005 | tau | P0,P1,P2 | S03/S04/S07 | delay/buffer relation and interval | referenceable thickness | OUTPUT-SHAPING |
| CON-PL-006 | external t | P0 | S03/S06 | time parameter of local template | evolution ordered in this parameter | BENIGN REPRESENTATIONAL |
| CON-PL-007 | gate existence | P0,P1 | S04/S12 | passage boundary included in architecture | partial opening/log passage | STRUCTURALLY IMPORTANT |
| CON-PL-008 | gate operation | P1,P2 | S04/S09 | selection/sedimentation assigned | some fast states retained | OUTPUT-SHAPING |
| CON-PL-009 | gate openness | P0,P1 | S11/S12 | closed/open/intermediate distinctions | nonfixed frontier and access | OUTPUT-SHAPING |
| CON-PL-010 | logs category | P0,P2 | S06/S09/S12 | re-referenceable retained structures | further logs and updated reference | STRUCTURALLY IMPORTANT |
| CON-PL-011 | I | P0,P2,P4 | S06 | effective log density under chosen biological-cognitive window | changing history distribution | OUTPUT-SHAPING |
| CON-PL-012 | J_I / J_log | P0,P2,P4 | S06 | current slots and log-reference interpretation | reference flow | OUTPUT-SHAPING |
| CON-PL-013 | Phi | P0,P2,P4 | S06/S09 | meaning potential/landscape reading | bias and future reference direction | OUTPUT-SHAPING |
| CON-PL-014 | K / gradient operators | P0,P4 | S06 template | kernel, field domain/differentiability conventions not fully specified | potential/gradient representation | BENIGN REPRESENTATIONAL |
| CON-PL-015 | T / T_Phi | P0,P2 | S05/S07 | effective index and meaning-gradient coupling | attention/clarity regime reading | OUTPUT-SHAPING |
| CON-PL-016 | TCA | P1,P2 | S05 | temporal conversion architecture/metaphor | difference converted into attention | STRUCTURALLY IMPORTANT |
| CON-PL-017 | Speed-Scale Orchestration | P0,P1,P2 | S04/S06 | two-layer/6-condition or3-condition description | sustained log referencing | STRUCTURALLY IMPORTANT |
| CON-PL-018 | Self-Sustaining Observer | P2 | S04:199–222 | observer-like name for own-log loop; no added subject | observer-like character when loop sustains | OUTPUT-LABELING |
| CON-PL-019 | consciousness window name | P0,P3 | S07/S15 | designated region called conscious/stable | state inside called conscious | OUTPUT-LABELING |
| CON-PL-020 | window bounds | P0,P1 | S07/S18 | symbolic min/max, numerical identification unspecified | qualitative stable/intermediate region | CLAIM-DEPENDENT |
| CON-PL-021 | projected observation window | P0,P4 | S06:17–64 | biological-cognitive effective coordinates selected | local correspondence | BENIGN REPRESENTATIONAL |
| CON-PL-022 | projection / unequal influence | P0,P2,P4 | S06:66–125 | umbrella operation / functional roles | attention, gate, residue selection described as instances | CLAIM-DEPENDENT |
| CON-PL-023 | C_ij | P0,P4 | S06:261 | upstream-labelled node relation | closure vocabulary for layer comparison | BENIGN REPRESENTATIONAL |
| CON-PL-024 | C_f / C_s / Delta C | P0,P1,P4 | S06:271–303 | layer closure roles/aggregation not specified | observation-regime counterpart | CLAIM-DEPENDENT |
| CON-PL-025 | older persistence PDE | P0,P4 | S06:305–321 | historical/effective template with 3 terms | SSO self-maintenance explained in this vocabulary | CLAIM-DEPENDENT |
| CON-PL-026 | VED observation regime | P0,P4 | S06/FIG-06 | nonclosure interval as comparison object | same-condition correspondence | CLAIM-DEPENDENT |
| CON-PL-027 | report pathway | P1,P2 | S09/S10 | route from retained logs to language/action | reportability / explicit access | STRUCTURALLY IMPORTANT |
| CON-PL-028 | neural/bodily substrate | P1,P4 | S14 | generic biological carrier context | temporal coupling regime, not one-site identity | STRUCTURALLY IMPORTANT |
| CON-PL-029 | self terrain | P2 | S12/S18 | retained-history landscape category | self-continuity after repeated openings | OUTPUT-SHAPING |
| CON-PL-030 | qualia frontier | P1,P2,P3 | S11:37–65 | transition between fast processing and slow log; experienced/phenomenal label | qualia appears at this frontier | OUTPUT-LOCATING |
| CON-PL-031 | measurement/residue distinction | P0,P2,P3 | S11/S13 | live versus recordable stipulated distinction | retained outcome called residue, not live quale | OUTPUT-LABELING |
| CON-PL-032 | own logs | P0,P1,P2 | S04:216/S09 | source assigns past traces to system; ownership rule unspecified | self-referencing observer reading | UNRESOLVED |
| CON-PL-033 | system/individual boundary | P0,P1 | S06/S18 | within-individual biological-cognitive window | observer/whole regime of that system | UNRESOLVED |
| CON-PL-034 | experienced ego | P3 | S05:148 | experience vocabulary brought to conversion point | TCA position interpreted as ego | OUTPUT-LABELING |
| CON-PL-035 | CT terrain | P0,P2,P4 | S04/S09/S20 | meaning landscape / invisible GPU comparison | thought/reference organization | STRUCTURALLY IMPORTANT |
| CON-PL-036 | CT Phi* | P0,P4 | S09/S20 | long-time landscape object from CT | slow sedimentation / concept stability correspondence | CLAIM-DEPENDENT |
| CON-PL-037 | Bio architecture motivation | P4 | S01/S04 | quasi-closure/life/toy labels as analogy | proposed fast/slow organization | STRUCTURALLY IMPORTANT |
| CON-PL-038 | VED nonclosure | P1,P4 | S06 | inherited persistence principle | local temporal nonclosure | CLAIM-DEPENDENT |
| CON-PL-039 | four-layer grammar | P4 | S06/S18/S20 | projected-layer comparative framework | conscious→self→intelligence relation | CLAIM-DEPENDENT |
| CON-PL-040 | JA C(t) | P0,P3 | CON-EQ-101/140 | named opening/access function | opening/collapse interpretation | OUTPUT-LABELING |
| CON-PL-041 | JA attention weights | P0,P2 | CON-EQ-079–081 | indexed log mass/weight and load | attention priority | OUTPUT-SHAPING |
| CON-PL-042 | figure region labels | P0,P3 | FIG-01/03/05 | conscious access / consciousness / qualia already written in diagram | diagram illustrates labeled phenomenon | OUTPUT-LABELING |
| CON-PL-043 | first-log initial state | P0,P1 | S09/S12 | source starts with processing and already sedimented logs; initialization not specified | continued log-reference loop | UNRESOLVED |

## 4. Preload-to-output audit

| OUT | Claimed output | Preloaded ingredients | Dynamical step | Truly new role claimed? | Source wording |
| --- | --- | --- | --- | --- | --- |
| OUT-001 | conscious regime | PL-001–005/007/010/019–020 | coupled reference relation opens | R2→R3 endpoint claimed; not verified here | S07/S12 consciousness opens, not object produced |
| OUT-002 | log referenceability | fast/slow/log/gate roles | selected retention and later reuse | functional relation active under supplied architecture | S04/S09 |
| OUT-003 | observer-like organization | own logs/system identity/loop | update from own traces without controller | observer-like name, not phenomenal subject | S04 |
| OUT-004 | ego | TCA and experienced ego vocabulary | gap transformation | experienced position correspondence | S05/S08 |
| OUT-005 | self | retained landscape and prior openings | repeated log/reference/self-narration | self terrain described as result | S12/S18 |
| OUT-006 | qualia | frontier plus phenomenal label | partial passage before retention | phenomenal role explicitly assigned | S11/S12 |
| OUT-007 | reportability | logs and language/action route | externalization | functional output, not universal consciousness identity | S09/S10 |
| OUT-008 | explicit consciousness | sedimentation/reference/report conditions | reportable access after processing | explicit-awareness role claimed | S10 |
| OUT-009 | nonlocal consciousness | local substrates and shared system window | temporal coupling among them | regime rather than brain-site identity | S14 |
| OUT-010 | conscious stability | intermediate-window labels/bounds | maintained nonclosure | stability terminology assigned to region | S07/S15 |
| OUT-011 | measurement residue | live/record distinction and measurement definition | stabilization/report/logging | recorded trace; phenomenal residue interpretation separate | S11/S13 |

## 5. Consciousness-window preload

| WIN-PRELOAD | Component | Independent definition? | Consciousness-labeled? | Derived / stipulated / unresolved |
| --- | --- | --- | --- | --- |
| WIN-PRELOAD-001 | rate difference | subtraction defined before label; units/carrier not fixed | becomes conscious-window coordinate | expression defined; empirical architecture independence not established by definition |
| WIN-PRELOAD-002 | gap bounds | symbolic 0 and upper bound | finite gap necessary wording | bound name supplied, numerical derivation not located |
| WIN-PRELOAD-003 | mu interval | coupling variable separately described | stable state intermediate range | symbolic bounds supplied; calibration unresolved |
| WIN-PRELOAD-004 | tau interval | buffer relation specified | time thickness of conscious reference | interval supplied; empirical bound extraction unresolved |
| WIN-PRELOAD-005 | T_Phi interval | effective index specified | conscious/qualia-related range | limits supplied; index alone does not generate consciousness |
| WIN-PRELOAD-006 | joint inequality region | mathematical membership meaningful once values/bounds supplied | named consciousness window | region definition, not independent phenomenal criterion |
| WIN-PRELOAD-007 | stable consciousness iff tuple in window | syntactic biconditional explicit | YES on both region description and endpoint | CON-EQ-067/161; definitional versus explanatory use must remain separated |
| WIN-PRELOAD-008 | empirical membership | source S18 says empirical window estimation undetermined | identification target already named | operational independence unresolved, not evidence grade |
| WIN-PRELOAD-009 | JA C(t) | named opening function, not closure C | YES | extra source-local expression; does not supply independent case labels |
| WIN-PRELOAD-010 | figure phase boundary | lower Delta v_min unlike body0; 2 axes | access/意識 prelabels | schematic limits supplied, not full multidimensional decision rule |

変数はtargetへの説明目的で選択されているが、「既知のpositive conscious casesにfittingした」という手続はsourceに所在しない。数値boundの導出も新しく補わない。循環の有無は「定義したwindowを同じ定義で再述する」場合と、「同じラベルを独立な説明根拠とする」場合で異なる（CIR-003–005/039）。

## 6. Fast / slow preload

| FS-PL | Component | Preloaded role | Later output | Dependency direction | Potential circularity type |
| --- | --- | --- | --- | --- | --- |
| FS-PL-001 | fast | predictive/reactive before conscious state | candidate stream | architecture→activity | C0, not assumed architecture alone circular |
| FS-PL-002 | slow | memory/sedimentary before conscious state | retained constraints | category→retention | C0 |
| FS-PL-003 | gap | finite difference required | nonclosure/access | rates→gap→window label | definition C1, interpretation C3 |
| FS-PL-004 | coupling mu | allows partial transmission | neither sync nor dissociation | coupling→reference possibility | C0; bound independence C8 |
| FS-PL-005 | delay tau | buffer already assigned | log referenceable thickness | ratio/delay→access | C0; experienced time not equated |
| FS-PL-006 | gate | partial passage structure given | selected logs | operation→retention | C0; gate generation not described |
| FS-PL-007 | Bio motivation | model-like vocabulary, not fast/slow result | proposed local two-layer premise | Bio analogy→local premise | C0, no inherited confirmation |
| FS-PL-008 | neural fast/slow | S14 assigns generic corresponding substrates after functional roles | coupled regime | function/category→carrier reading | independence unresolved, not proof cycle |

## 7. Gate preload

| GATE-PL | Aspect | Supplied before output | Claimed later | Classification / trace |
| --- | --- | --- | --- | --- |
| GATE-PL-001 | existence | gate in S04/S12 architecture | gates open/close | C0; no source gate-creation dynamics located |
| GATE-PL-002 | operation | selects what sediments and what flows away | partial logs | functional preload, not illicit by itself |
| GATE-PL-003 | openness | closed/open/intermediate conditions | rigidity/no trace/intermediate access | symbolic/qualitative control, no new gate variable supplied |
| GATE-PL-004 | frontier | transition placed between fast processing and retention | called sedimentation/closure frontier | functional location preloaded |
| GATE-PL-005 | phenomenal surface | experienced/live/qualia terms applied to frontier | explanation of felt foreground | label/identification→CIR-016 serious candidate, not gate operator=qualia equation |
| GATE-PL-006 | window-to-gate relation | appropriate T_Phi in named window | gate appropriate for reference and conscious state obtains | interpretation loop candidate CIR-004/007; no independent gate criterion supplied |

## 8. Log bootstrap

| LOG-CIRC | Step | Prior logs? | Prior consciousness? | Source bootstrap account | Circularity |
| --- | --- | --- | --- | --- | --- |
| LOG-CIRC-001 | fast activity | not an explicit log condition in step1 | not required by step1 | S09 starts with fast activity, no zero-state account | C0 for local step |
| LOG-CIRC-002 | gate sedimentation | existing gate/slow category, not necessarily prior content | not universally required in S04/S09 | fast passage produces logs before whole-loop claim | C0: do not assert all logs require consciousness |
| LOG-CIRC-003 | I/Phi update | some sedimented traces needed | no separate consciousness premise in formal template | selected traces alter field; initial field not prescribed | C2 during continuation |
| LOG-CIRC-004 | future prediction biased by Phi | history already retained | whole loop later called conscious | six-step recurrence | C2 feedback |
| LOG-CIRC-005 | opening from already sedimented logs | YES explicit | prior consciousness not explicitly demanded | S12: already-running processing and already-sedimented logs | C5 initial condition not explained |
| LOG-CIRC-006 | logs left while consciousness open | YES for maintenance relation | this subclass YES described as experience traces | S12 storage discussion, not universal origin of all logs | C2 maintenance; do not infer universal cycle |
| LOG-CIRC-007 | own-log observer | YES plus ownership | subject addition denied | S04 no first ownership/bootstrap rule | C5 ownership/initialization unresolved |
| LOG-CIRC-008 | first log / first conscious opening | no starting protocol supplied | source does not specify first conscious origin | no initialization or first-log demonstration located | C5, not established proof circularity |

## 9. Self-reference audit

| CON-SR | Source loop | Input | Output | Re-enters where? | Loop type | Vicious? | Master trace |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CON-SR-001 | S09 six-step process | fast activity plus prior traces | changed I/Phi and biased next fast | next prediction | FEEDBACK ONLY | NO | CIR-010 |
| CON-SR-002 | S04 own-log update | system-assigned past logs | updated system state | logs reused by same process | RECURSIVE INFORMATIONAL LOOP | NO | CIR-010/009 boundary separate |
| CON-SR-003 | SSO observer naming | sustained temporal loop | observer-like characterization | description of same loop | OBSERVER LOOP | NO | CIR-011 |
| CON-SR-004 | S18 self-model inside loop | retained self-representations | changed terrain/self-model | ongoing reference | SELF-MODEL LOOP | NO | CIR-014 |
| CON-SR-005 | S10 rationalization | available/missing response logs | coherent account/new logs | later self-reference | RECURSIVE INFORMATIONAL LOOP | NO | CIR-014 |
| CON-SR-006 | S12 opening/self/history | prior logs/openings | self terrain/new experience traces | subsequent opening | DEPENDENCY CYCLE | UNRESOLVED | CIR-015: initialization, not universal prior-consciousness requirement |
| CON-SR-007 | S13 introspection | own ongoing state | stabilized self-report/log | later internal reference | FEEDBACK ONLY | NO | CIR-020 |
| CON-SR-008 | S07/S15 window label | conscious-labelled region | same endpoint iff membership | region classification | DEFINITIONAL LOOP | NO | CIR-003, explanatory reading separate CIR-004 |
| CON-SR-009 | S11 frontier explanation | boundary already called phenomenal | qualia as frontier explained by position | prior phenomenal identification | PROOF CIRCULARITY CANDIDATE | POSSIBLE | CIR-016; serious criterion4 only |
| CON-SR-010 | S13 successful measurement | measured/stabilized residue | live state said not captured | theory classifies later measurements as residue | INTERPRETIVE LOOP | POSSIBLE | CIR-019; falsifiability not judged |
| CON-SR-011 | S20 CT mutual reading | own field/window roles plus other branch comparison | same-structure interpretation | each reading refers back | DEPENDENCY CYCLE | UNRESOLVED | CIR-029/032; claim return-edge separated |
| CON-SR-012 | S18 Intelligence complementarity | Consciousness window and Intelligence horizon | four-layer/transitional interpretation | citations refer back to source window | DEPENDENCY CYCLE | UNRESOLVED | CIR-033/035 |
| CON-SR-013 | S19 theory/object nonclosure | object named nonclosed | incomplete theory likened to object | method reinforces explanatory vocabulary | INTERPRETIVE LOOP | NO | CIR-027; not proof of object |

## 10. Observer audit

| OBS | Object | Source status | Input conditions | Claimed output | Subject identity? |
| --- | --- | --- | --- | --- | --- |
| OBS-001 | observer-like organization | functional description S04 | loop sustains own-log updates | observer-like character | no added contemplating subject |
| OBS-002 | Self-Sustaining Observer | conditional alternative reading of SSO | same temporal loop becomes self-sustaining | named observer | not independent phenomenal-subject derivation |
| OBS-003 | observing subject | source explicitly denies added subject/controller | not required in equations | none generated as separate variable | negative identification |
| OBS-004 | reportable subject/self | source response/self-report context S10 | traces plus available pathway | coherent reportable account | no formal reportable-subject identity rule |
| OBS-005 | phenomenal subject | experience/ego language present | not separate observer creation equation | experienced ego position, not a new subject entity | observer-like≠phenomenal subject |
| OBS-006 | self-model | inside-loop landscape S18 | repeated reference/sedimentation | revisable self terrain | source denies selfmodel as consciousness cause |

## 11. Observer/system boundary

| OBS-BND | Boundary | Exists before observer? | Generated? | Operational extraction? | Role / Phase00 trace |
| --- | --- | --- | --- | --- | --- |
| OBS-BND-001 | biological-cognitive window | YES chosen description | no generation protocol | not supplied | CON-BND-01; observer modeled within window |
| OBS-BND-002 | fast/slow system | YES architecture | interaction dynamic; partition given | carrier segmentation not fixed | CON-BND-02 |
| OBS-BND-003 | synchrony/disconnection window | symbolic limits before regime label | state changes, limits named | numbers not fixed | CON-BND-03 |
| OBS-BND-004 | gate passage | YES partial boundary condition | openness described, gate existence not derived | no specific anatomical rule | CON-BND-04 |
| OBS-BND-005 | sedimentation frontier | process distinction supplied | ongoing transition described | no independent phenomenal extraction | CON-BND-05 |
| OBS-BND-006 | observer / subject distinction | source naming/no-subject guard | observer-like read off loop | subject criterion not provided | CON-BND-06 |
| OBS-BND-007 | self/world and internal/external | implicit system/individual attribution | self terrain described formed | exact partition unspecified | CON-BND-07 |
| OBS-BND-008 | own-log ownership | YES implicit assignment to system | ownership not constructed | rule not supplied | S04 own logs; related CON-BND-06/07 |
| OBS-BND-009 | report pathway | YES route availability | report dynamic, pathway topology considered given | experiment-type pathway example only | CON-BND-08 |
| OBS-BND-010 | measurement subject/object | already chosen referenced state | measurement changes state | external/own observation process described | CON-BND-09 |
| OBS-BND-011 | local neural / nonlocal regime | local substrates initially considered | temporal relation opens | no system-extraction map | CON-BND-10 |
| OBS-BND-012 | VED observation / conscious window | distinct source descriptions supplied | correspondence not generated carrier | typed map unresolved | CON-BND-11 |
| OBS-BND-013 | within-individual / external stopping | biological individual window assumed | downstream transition proposed | boundary construction not supplied | CON-BND-12 |

## 12. Own-log dependency

| OWN-LOG | Dependency | Source fact | Unresolved node | Classification |
| --- | --- | --- | --- | --- |
| OWN-LOG-001 | what makes trace a log | S06 re-referenceable retained trace | exact extraction/proxy | representation dependence |
| OWN-LOG-002 | what makes log own | S04 current system references its own logs | assignment/ownership criterion | system attribution presupposed |
| OWN-LOG-003 | ownership→observer | own traces in self-sustaining loop yield observer-like reading | no phenomenal subject criterion | naming C1; ownership C5 |
| OWN-LOG-004 | system boundary→ownership | biological-cognitive/individual window supplies context | formal boundary independent of observer not constructed | C5 initialization/domain issue |
| OWN-LOG-005 | observer→ownership reverse | no explicit rule: only observer-produced logs count as own | reverse edge not located | do not invent proof cycle |
| OWN-LOG-006 | first assigned history→future own history | continued loop described | initial owner/log allocation unresolved | C5; no bootstrap repair |

## 13. Ego circularity

| EGO-CIRC | Use | Prior ego required? | Output role | Circularity status |
| --- | --- | --- | --- | --- |
| EGO-CIRC-001 | TCA transforms gap | equations use gap/mu/gradient, not ego | conversion | C0 no ego input |
| EGO-CIRC-002 | experienced ego position | experience vocabulary invoked for correspondence | interpreted ego | C3 labeling, not subject proof |
| EGO-CIRC-003 | ego selector/controller | source denies command center/cause | no executive agent added | C0 negative result |
| EGO-CIRC-004 | attention without chooser | projection explicitly not requiring intentional choice | unequal priority | C0 implicit intentional agent not forced |
| EGO-CIRC-005 | ego/self terrain | S18 terrain formed through repeated reference | maintained self/ego descriptions | C2 maintenance; identity tension retained, not vicious proof |

## 14. Self circularity

| SELF-CIRC | Use | Dependence | Cycle type | Result |
| --- | --- | --- | --- | --- |
| SELF-CIRC-001 | self follows openings | repeated reference→terrain/self | developmental description | not self as cause; S12/S18 |
| SELF-CIRC-002 | self continuity via logs | stored terrain→new narrative→new logs | recurrent maintenance loop | C2, time-ordered feedback |
| SELF-CIRC-003 | rationalization fills gaps | available logs→coherent account→future logs | recurrent maintenance loop | C2, not claim proven by its own report |
| SELF-CIRC-004 | own logs before self identity | system-assigned history required before observer reading | initialization problem | C5 ownership not independently specified |
| SELF-CIRC-005 | consciousness→logs→self→consciousness proposal | experience traces feed later opening; all-logs-require-consciousness reverse not stated | unresolved bootstrap rather than proof cycle | C5, do not generalize subclass of experience logs |
| SELF-CIRC-006 | self-model→consciousness cause | S18 explicitly denies this causal identification | no cycle | C0 negative result |

## 15. Qualia preload / circularity

| QUA-CIRC | Claim | Classification | Preloaded endpoint / support direction | Circularity trace |
| --- | --- | --- | --- | --- |
| QUA-CIRC-001 | transitional state experienced as qualia | DEFINITIONAL IDENTIFICATION | transition function described first; experienced-as supplied by identification sentence | CIR-016 stronger explanation reading; definition alone not vicious |
| QUA-CIRC-002 | qualia as phenomenal surface | PHENOMENAL LABEL | experiential surface is not derived by field equation in this passage | CIR-016 endpoint already named |
| QUA-CIRC-003 | gate/frontier location | MECHANISM CLAIM | passage→sedimentation locates functional transition | CIR-007 functional location vs phenomenality separate |
| QUA-CIRC-004 | qualia clarity from T_Phi | MECHANISM CLAIM | qualia label/clarity already used; index predicts qualitative changes | CIR-017 interpretation loop, not numerical experiential measure |
| QUA-CIRC-005 | live not stored | DEFINITIONAL IDENTIFICATION | stored category excluded from live definition | CIR-018 benign definitional distinction unless used as independent proof |
| QUA-CIRC-006 | measurement changes qualia | MEASUREMENT LOOP | prior live/residue distinction classifies all records | CIR-019 potential evidential closure, not falsifiability verdict |
| QUA-CIRC-007 | qualia cannot be captured unchanged | MEASUREMENT LOOP | successful stabilization is reason for noncapture | CIR-019; no actual disconfirming dataset adjudicated here |
| QUA-CIRC-008 | conditions/residue should be measured | UNRESOLVED BRIDGE | measured outputs need correspondence to named experience | source permits comparison/manipulation; not automatic shield |
| QUA-CIRC-009 | why felt foreground is central | UNRESOLVED BRIDGE | S11 already named frontier phenomenal, then cites frontier position as reason | CIR-016, SERIOUS criterion4 candidate |

phenomenalityはred/pain/sound/here-nowという経験語で導入されている（S11前半）。functional transitionを独立に記述する部分と、それをexperienced-asと名付ける部分を分ける。「経験語がある」ことだけで悪循環とはせず、同じ経験属性が説明の前提に再使用される箇所だけを§28で重大候補とする。経験の真偽やhard problemの成否は判定しない。

## 16. Measurement circularity

| MEAS-CIRC | Claim | Observable input | Theory output | Alters output? | Potential unfalsifiability loop? |
| --- | --- | --- | --- | --- | --- |
| MEAS-CIRC-001 | measurement stabilizes | comparison/record/report procedures | stabilized record | YES source | C1 definition/effective description, not itself unfalsifiable |
| MEAS-CIRC-002 | live qualia→residue | report/label/number/neural summary | trace classified not live quale | YES | CIR-018 distinction; source label may govern selection |
| MEAS-CIRC-003 | greater precision erases live qualia because measurement succeeds | more definite records | greater stabilization, no original live capture | YES source | CIR-019 C6 candidate: no-capture explained by theory rather than independent test |
| MEAS-CIRC-004 | all direct access classified as residue | source treats neural/behavior/report alike | indirect trace only | YES | CIR-019 evidential gate structure; no final falsifiability decision |
| MEAS-CIRC-005 | introspection logs own state | internal attention/verbalization | altered slow trace | YES | CIR-020 C2 feedback plus interpretive measurement premise |
| MEAS-CIRC-006 | conditions/residue are analyzable | source permits statistical comparison and manipulations | report-demand/attention/neural before-after differences | measurable changes anticipated | possible independent intervention node proposed, not demonstrated here |
| MEAS-CIRC-007 | measurement failure validates theory? | no actual contrary experimental case analyzed in source | no explicit universal rule that every outcome confirms theory | not determinable | do not assert an established immunity-to-testing policy |

## 17. Access / report cycle

| REPORT-CIRC | Object / direction | Source relation | Potential reverse edge | Classification |
| --- | --- | --- | --- | --- |
| REPORT-CIRC-001 | conscious state vs reportability | S09 explicitly not identical | general biconditional denied | C0, no invented conscious iff report loop |
| REPORT-CIRC-002 | conscious access | referenceable relation within window | route to report not automatically equivalence | C3 interpretation/criterion separation |
| REPORT-CIRC-003 | explicit consciousness | S10 requires sedimented/referenceable response and pathway | report used as marker of explicit access | C3 potential criterion-identification loop, not all phenomenality |
| REPORT-CIRC-004 | reportability | logs externalized via language/action | lack of verbal report not universally lack of consciousness | C0 pathway distinction retained |
| REPORT-CIRC-005 | qualia report | report is stabilized residue | direct report of unchanged quale excluded by definitions | C1/C6 distinction from explicit-access criterion |
| REPORT-CIRC-006 | empirical inference from report to state | source reinterprets experiments via log architecture | no general independent decision rule supplied | C8 criterion independence unresolved, not evidence grading |

## 18. Neural-substrate preload

| NEU-PL | Object | Independent carrier? | Functional role pre-assigned? | Consciousness role |
| --- | --- | --- | --- | --- |
| NEU-PL-001 | fast neural activity | S14 generic corresponding neural activity, no named rate calibration | prediction/reaction already assigned | local participating substrate, not conscious state itself |
| NEU-PL-002 | slow neural/bodily substrate | generic carrier class | retention/log role already assigned | temporal-loop participant |
| NEU-PL-003 | reporting/memory/sensory/motor/verbal pathways | listed local substrates | respective functions given | routes enabling reference/report |
| NEU-PL-004 | readiness potential | named experiment type in S10 | interpreted fast preparation afterward | reportable-intention delay context |
| NEU-PL-005 | split-brain transmission | named neuroanatomical constraint in S10 | availability/verbalization distinction interpreted | asymmetric report, not new consciousness criterion |
| NEU-PL-006 | whole nonlocal regime | local substrates and biological-cognitive system window given | functional temporal coupling assigned | regime opens jointly; system extraction not constructed |

独立carrierとは、sourceが名前・経路を先に例示する範囲と、model variableにtyped mapを与える範囲を分けた問い。genericであることを「神経機構が存在しない」という結論にしない。

## 19. Projection preload

| PROJ-PL | Use | Classification | Prior structure | Cycle check |
| --- | --- | --- | --- | --- |
| PROJ-PL-001 | observation window chosen | methodological grouping | effective coordinates/window | C0 representation selection |
| PROJ-PL-002 | mass assignment/unequal influence | formal operation | state/category and weighting distinction | C1 local definition; domain/codomain unresolved |
| PROJ-PL-003 | biological prioritization | functional analogy | biological functional roles | C3 same umbrella, not same carrier inference |
| PROJ-PL-004 | attention/TCA | functional analogy | temporal conversion/priority | C3 source retroactively groups previously named operations |
| PROJ-PL-005 | gate | methodological grouping / functional analogy | partial passage already defined in S04 | C3 included later in projection list |
| PROJ-PL-006 | residue and split-brain pathways | unresolved umbrella | different measurement/pathway descriptions | C3 common label not common causal map |
| PROJ-PL-007 | Intelligence stopping use | formal/functional correspondence | downstream possible stopping locus | mostly forward reuse; specific reverse proof edge not located |
| PROJ-PL-008 | psychological projection | cross-domain correspondence claim | subjectivity in psychological instance only | source structural definition explicitly presupposes no subject; no automatic subject preload |

## 20. Closure / nonclosure preload

| NC-PL | Use | Upstream preload | Local derivation? | Output explained |
| --- | --- | --- | --- | --- |
| NC-PL-001 | persistence principle | VED nonclosure | imported template/read across windows, not independent local theorem | motion/flow and SSO persistence |
| NC-PL-002 | Delta C vs Delta v | VED closure vocabulary | difference definitions explicit; coordinate transform not supplied | same observation condition claimed |
| NC-PL-003 | conscious window | vocabulary plus local bounds | named criterion not independent phenomenal derivation | intermediate conscious regime |
| NC-PL-004 | loop persistence | source architecture | six-step feedback description | continued update/reference |
| NC-PL-005 | opening | temporal nonclosure interpretation | relation rather than product stipulated | consciousness opens |
| NC-PL-006 | qualia frontier | partial closure boundary | functional transition plus phenomenal identification | live foreground |
| NC-PL-007 | observer persistence | self-sustaining loop | observer-like name read from operation | own-log observer |
| NC-PL-008 | theory incompleteness | same nonclosure word applied to object and theory | analogy/methodological statement, no theorem | why theory remains open |
| NC-PL-009 | CT positive I / Phi* | upstream/cross-branch terrain | source comparison, not complete operational translation | excluding complete closure across windows |

nonclosureの全purpose reuseを一覧化したが、語彙共通だけで全説明が循環するとはしない。とくにtheory incomplete→object nonclosedを経験的証拠として逆に推論する文は所在しない。sourceはobject descriptionとmethodの類似を述べる（CIR-027）。

## 21. Older VED PDE dependency

| VED-CIRC | Claim | Upstream support | Local support | Dependency tension | Circularity |
| --- | --- | --- | --- | --- | --- |
| VED-CIRC-001 | older PDE supports SSO maintenance | historical/phenomenological three-term persistence relation | fast→slow/dissipation/barrier readings | imported support versus local window description | CIR-028 C8: self-supporting proof return-edge not located |
| VED-CIRC-002 | neither description grounds other | S06 caption/projected stance | SSO and VED as coordinate descriptions | VED-grounded basis sentence coexists | dependency-language tension, not actual mutual theorem proof established |
| VED-CIRC-003 | same output window defined locally | Delta C interval and Delta v window | local conditions named before/after PDE | repeating target under another notation does not independently derive it | C3 correspondence; C8 translation |
| VED-CIRC-004 | source authority version | current IFGT unified tau-form located, full t-form quoted locally | older VED / revised Vol.4 interpretation label | exact historical version remains unresolved | no upstream audit reopen; no new equation equivalence |

参照：[IFGT unified source](../../Information-Field-Geometry-Theory/sections/unified_equation.tex)、[Vol.4 dynamic barrier](../../paper/vol4/sections/dynamic_barrier.tex)。Consciousness S06:305–321の「phenomenological, coarse-grained approximation」「VED-grounded basis」とS06:330–331のnon-groundingを両方保存する。OLD-PDE-ROLE-001–006を全て包含し、上流の正しさは再判定しない。

## 22. CT cross-dependency

新たにCTのcurrent sourceを参照方向だけ照合した。CTの理論全体を監査しない。CTのConsciousness noteとcurrent Consciousness Theory paperは同一出自として扱わない。CTにJA modular directoryは所在しないため、存在しないsections_ja pathをauthorityとして作らない。

| CON-XDEP | Claim/object | Consciousness→CT | CT→Consciousness | Closed support cycle? | Classification |
| --- | --- | --- | --- | --- | --- |
| CON-XDEP-001 | SSO/invisible GPU | S04:195 / S20 terrain comparison | CT relation_to_note:54–56 credits Consciousness note; future companion formalization | mutual documentary authority path; exact claim/proof return not fixed | C4 documentary loop; C7 not established |
| CON-XDEP-002 | Phi kernel / landscape | S06/S09 use CT structure | CT formal_mapping defines Phi and variable table using IFGT | its equation does not derive from SSO in current CT text | C0 independent local construction node located, not validation |
| CON-XDEP-003 | Phi* long-time terrain | S09/S20 use CT attractor terminology | CT formal_mapping/dynamics local field interpretation | no return proof using Consciousness loop located | C0 one-way analogue, stability not assessed |
| CON-XDEP-004 | qualia/insight same boundary | S20 claims same phenomenon | CT pathologies:18–22 explicitly excludes generating/explaining subjective experience | CT does not return same qualia conclusion as proof | C3 local interpretive mapping; no claim-level closed cycle located |
| CON-XDEP-005 | SSO needed for referenceable terrain | S20:29 only when SSO established; S04/S09 borrow terrain to describe SSO | CT says fast/slow to be formalized in companion paper | logical/temporal initialization direction unresolved | C5 bootstrap/cross-dependency, not mutual citation alone proof |
| CON-XDEP-006 | positivity / common grammar | S20 positive I not by itself identity | CT formal_mapping positive field with gradient proviso | shared upstream premise, not each citing other as sole proof | C0 shared dependency with local correspondence claim |

| Actual source | Relevant content |
| --- | --- |
| [CT intuitive picture](../../conceptual-topography/sections/intuitive_picture.tex):82 | Invisible GPU below conscious access; phenomenological illustrations |
| [CT note relation](../../conceptual-topography/sections/relation_to_note.tex):54 | CPU/GPU from Consciousness note; companion paper future; L3→L1 support language |
| [CT pathologies](../../conceptual-topography/sections/pathologies.tex):18 | does not generate or explain subjective experience; companion theory referral |
| [CT formal mapping](../../conceptual-topography/sections/formal_mapping.tex):13 | projected I, local Phi definition, variable table |
| [CT dynamics](../../conceptual-topography/sections/dynamics.tex) | landscape evolution terminology, not SSO proof |

## 23. Intelligence bidirectional dependency

| CON-XDEP | Claim/object | Consciousness→Intelligence | Intelligence→Consciousness | Claim-level return? | Classification |
| --- | --- | --- | --- | --- | --- |
| CON-XDEP-007 | projected-uses stance | S06 cites Intelligence §9.4 for inter-window context | I JA §4 and II preliminaries follow Consciousness stance | method complementarity, not independent proof of primitive | C0 reuse; authority route recorded |
| CON-XDEP-008 | four-layer grammar | S06/S18/S20 cite Intelligence for same-structure comparison | I §9 table/figure use conscious window from source | same comparative thesis passed between sources | C4 authority/expository loop, no independent identity theorem asserted |
| CON-XDEP-009 | transitional consciousness layer | S18 consciousness→self→intelligence cited with Intelligence | I JA §9:241–253 cites Consciousness §18 transition | reciprocal support of comparative placement | C4 handoff cycle; no proof of consciousness from downstream identity |
| CON-XDEP-010 | projection primitive/stopping | S06 local unequal-influence definition | II stopping:80 calls intelligence realization of Consciousness primitive | no reverse assertion that stopping proves original primitive located | C0 forward reuse |
| CON-XDEP-011 | intra-individual quasi-stopping | S18 comparison and local nonclosure | I JA §8/9 log referencing buffers horizon; §9 cites SSO | cognitive extension, not a phenomenal proof return located | C4 comparative dependency, boundary/translation unresolved |
| CON-XDEP-012 | second attractor / L_R / L_E | not Consciousness local input | II antecedent is Bio-specific, not automatically SSO | no Consciousness support cycle established | C0 no invented edge |

| Actual source | Checked dependency |
| --- | --- |
| [I §9 EN](../../intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex):65 | proposed four-layer comparison / no common carrier mechanism typed translation |
| [I §9 JA](../../intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex):238 | transitional layer; cites Consciousness SSO/§18 |
| [I §8 JA](../../intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex) | intra-individual referencing vs stopping conditions |
| [I §4 JA](../../intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex):92 | projected-use stance |
| [II preliminaries](../../intelligence-part2/sections/01_preliminaries.tex):6 | follows Consciousness projected uses |
| [II stopping](../../intelligence-part2/sections/05_emergent_stopping_layer.tex):80 | unequal-influence primitive reused for stopping locus |
| [II homology appendix](../../intelligence-part2/appendices/appendix_b_homology.tex):25 | Consciousness windowed stabilization comparison |

相互引用は確認できるが、Intelligenceの独自定理の成立を本phaseで再判定しない。Consciousnessが原始的なphenomenal claimをIntelligenceの証明だけで支え、Intelligenceが同じclaimを唯一の前提とする、という閉じたproof chainは確認していない。修復済みBio attribution ceilingも変更しない。

## 24. Definition vs explanation

| DEF-EXPL | Object | Definition/class | Explanation/class | Same statement reused? | Circularity risk |
| --- | --- | --- | --- | --- | --- |
| DEF-EXPL-001 | consciousness | DEFINITION/LABEL: nonclosed log-reference regime | CRITERION/EXPLANATION: window opens state | named regime is restated in conditions | C1 definitional reading / C3 explanatory reading; no numerical fitting inferred |
| DEF-EXPL-002 | qualia | DEFINITION/LABEL: live phenomenal frontier | EXPLANATION/MECHANISM: boundary position accounts for felt foreground | experienced endpoint already in premises | CIR-016 C7 SERIOUS candidate; not final failure |
| DEF-EXPL-003 | ego | CORRESPONDENCE: position experienced as ego | EXPLANATION: TCA transforms gap, not chooser | experiential naming follows functional account | C3, no prior ego equation input |
| DEF-EXPL-004 | self | DEFINITION: sedimented personal terrain | MECHANISM: repeated logs/openings maintain continuity | later self-description reuses retained terrain | C2 maintenance / C5 origin, not subject proof |
| DEF-EXPL-005 | observer | LABEL: Self-Sustaining Observer | CORRESPONDENCE: sustained own-log updates look observer-like | same operation renamed, subject explicitly denied | C1 benign naming; boundary dependency separate |
| DEF-EXPL-006 | phenomenal-subject bridge | FORWARD HYPOTHESIS / unresolved correspondence, not generated extra subject | source refuses added subject / whole closed-form solution | no subject-creation derivation asserted | C0 no claimed proof to circularly invalidate |

## 25. Necessary / sufficient circularity

| NS-CIRC | Condition | Target | Independent criterion? | Defined by target? | Risk |
| --- | --- | --- | --- | --- | --- |
| NS-CIRC-001 | S04 six conditions | SSO capable log referencing, necessary for consciousness | functional architecture partly explicit | not all named with consciousness; still not sufficient per S04 | C1/C0, avoid converse |
| NS-CIRC-002 | S06 three conditions | conscious state obtains | informal condition list, no equivalence to six given | state label attached at conclusion | C8 condition-set relation, not automatic circle |
| NS-CIRC-003 | finite gap | nonsynchrony/referenceability | difference defined independently once rates fixed | conscious bound chosen in target context | C1 formal / C3 interpretation |
| NS-CIRC-004 | mu/tau/T_Phi limits | stable regime | numerical bound calibration not fixed | intermediate state called conscious | C8 independence; no positive-case fitting procedure located |
| NS-CIRC-005 | window iff tuple | stable consciousness | membership computable after bounds/values supplied, biological extraction unresolved | target name appears in region label | C1 definition / C3 explanation candidate |
| NS-CIRC-006 | logs before opening | log referenceability | functional retention describable without first conscious claim | only experience-log subset presumes prior opening | C5 first-log bootstrap, not universal consciousness-required-log premise |
| NS-CIRC-007 | report pathway | explicit access/reportability | pathway distinction described in experiment-type examples | explicit-awareness inference uses reference/report terms | C3 operational identification loop candidate, not general consciousness iff report |
| NS-CIRC-008 | qualia condition | felt frontier | functional transition independent; phenomenality assigned by label | phenomenal endpoint named before explanatory use | CIR-016 serious criterion4 |
| NS-CIRC-009 | measurement residue | observable trace after live state | record exists as record; quale passage identification theory-dependent | residue defined as post-quale object | C6 potential evidence-loop structure |
| NS-CIRC-010 | CT SSO only-when terrain | referenceable landscape | CT terrain equation independently written, SSO accessibility interpretation local | shared cognitive endpoint | C5 cross-initialization question |
| NS-CIRC-011 | remaining NS families | source conditional predictions / negations / research requirements | constituent definitions differ; converse not inferred | no global necessary/sufficient union | Phase02 NS-ROLE-001–057 carried forward, coverage §32 |

## 26. Phenomenal bridge structural audit

Phase02のR0/R1/R2→R3 crossing 18件を全て再索引する。bridge typeはsourceの接続形式であり成立認定ではない。endpoint-in-premiseはphenomenal termそのものが説明前提に含まれるかを記録し、ただ対象名を紹介することだけでC7へ進めない。

| CON-PB | Phase02 crossing | Source bridge | Type | Endpoint in premise? | Circularity structure |
| --- | --- | --- | --- | --- | --- |
| CON-PB-001 | CON-RT-006 | gap/window→conscious regime; S07/S15 | NECESSITY | region name already conscious; rate difference itself not phenomenal | CIR-003/004 definition vs explanation |
| CON-PB-002 | CON-RT-009 | delay bounds→experienced time/self continuity; S15 | CORRESPONDENCE | delay premise not experienced time itself | C3 interpretation, no proof loop located |
| CON-PB-003 | CON-RT-012 | T_Phi→qualia clarity; S11 | CORRESPONDENCE | qualia assumed as named target, not generated by index | CIR-017; not independent phenomenality derivation |
| CON-PB-004 | CON-RT-016 | gradient→what appears; S09 | MECHANISTIC | appearance target named, gradient not defined as quale | C3 functional selection→experience interpretation |
| CON-PB-005 | CON-RT-017 | gate/frontier→phenomenal surface; S11 | IDENTIFICATIONAL | YES frontier named phenomenal before explanatory use | CIR-016 serious candidate |
| CON-PB-006 | CON-RT-019 | three SSO conditions→state obtains; S06 | SUFFICIENCY | conditions functional; state label attached afterward | CIR-039; S04 not-sufficient scope retained |
| CON-PB-007 | CON-RT-021 | TCA→experienced ego; S05 | CORRESPONDENCE | experienced ego vocabulary introduced; no ego operator input | CIR-013 interpretation not subject proof |
| CON-PB-008 | CON-RT-022 | feedback loop→conscious maintenance; S09 | IDENTIFICATIONAL | loop named conscious then maintenance described | CIR-010 feedback / CIR-004 regime interpretation separate |
| CON-PB-009 | CON-RT-023 | coupled substrates→regime; S14 | IDENTIFICATIONAL | conscious regime target named, substrate not identical | CIR-023 local/global distinction |
| CON-PB-010 | CON-RT-026 | pathways→explicit consciousness; S10/S14 | NECESSITY | explicit access specified via reference/report context | CIR-021 criterion interpretation |
| CON-PB-011 | CON-RT-027 | referenceable logs→explicit awareness; S10 | NECESSITY | functional logs independent as category; explicit label given | CIR-021 not general conscious iff report |
| CON-PB-012 | CON-RT-028 | measurement→qualia residue; S11/S13 | MECHANISTIC | YES live qualia and residue distinction premises | CIR-018/019: definition/evidence-loop candidate |
| CON-PB-013 | CON-RT-029 | introspection→changed foreground; S13 | MECHANISTIC | own experienced state is object before measurement | CIR-020 dynamics, ownership question separate |
| CON-PB-014 | CON-RT-031 | Delta C regime→conscious window; S06 | CORRESPONDENCE | target window already defined | CIR-028 non-grounding/basis tension, no transform invented |
| CON-PB-015 | CON-RT-035 | CT insight→qualia frontier; S20 | ANALOGICAL | qualia defined in Consciousness first; CT does not explain subjective experience | CIR-031 interpretation, return-proof edge not located |
| CON-PB-016 | CON-RT-036 | self terrain→experienced continuity; S12/S18 | CORRESPONDENCE | personal history category; selfness labeled later | CIR-014/015 maintenance vs bootstrap |
| CON-PB-017 | CON-RT-037 | tuple in window iff stable consciousness; S15 | DEFINITIONAL | YES endpoint labels window | CIR-003 benign reading / CIR-004 stronger reading candidate |
| CON-PB-018 | CON-RT-039 | JA C(t)→opening/collapse; S07/S13 | IDENTIFICATIONAL | C(t) already names opening | CIR-036 definitional interpretation, no external calibration |

## 27. Circularity master ledger

CIR-xxxは以下のCON-CIR-xxxの短縮、PL-xxxはCON-PL-xxxの短縮。各sub-ledgerで複数C分類を並べた場合は異なるaspectの分離を示し、master各行は一aspect・一classとする。C7はproof / claim-threatening **candidate**であり、viciousness確立とは別。C6はevidence-loopの潜在構造を示し、実証不適合や反証不能性の判定ではない。

| Class | Meaning | Decision boundary |
| --- | --- | --- |
| C0 | NO CYCLE | reverse dependence not located / explicit distinction / independent local node |
| C1 | BENIGN DEFINITIONAL LOOP | same construct renamed/re-expressed, not independent proof asserted in this reading |
| C2 | DYNAMICAL FEEDBACK LOOP | outputs alter later inputs; no support circularity inferred |
| C3 | INTERPRETIVE LOOP | labeled interpretation used to describe/select same relation |
| C4 | DEPENDENCY / AUTHORITY LOOP | reciprocal reference/support routing, proof-level exclusivity separately checked |
| C5 | BOOTSTRAP / INITIALIZATION LOOP | continuation depends on history/ownership whose first assignment is unspecified |
| C6 | EVIDENCE LOOP | theoretical identification governs what observations count as output/trace; potential loop not falsifiability verdict |
| C7 | PROOF / CLAIM-THREATENING CIRCULARITY | explanatory support includes substantially the target property; preserve as candidate where source definition vs proof remains distinguishable |
| C8 | UNRESOLVED | current direction/independence cannot be classified more precisely |

| CON-CIR | Candidate / dependency chain | Source / sub-ledger | Class | Why / missing reverse edge / limiting fact | Vicious established? |
| --- | --- | --- | --- | --- | --- |
| CON-CIR-001 | fast/slow assigned→structured process | S04; FS-PL-001/002 | C0 | architecture premise not claim of derivation from its output | NO |
| CON-CIR-002 | rates→gap→same rate difference description | CON-EQ-001/074 | C1 | literal subtraction definition, not independent proof | NO |
| CON-CIR-003 | defined window→membership→same regime label | S07/S15; WIN-PRELOAD-006/007 | C1 | definition reading is benign; do not treat as empirical identification | NO |
| CON-CIR-004 | conscious-labeled intermediate range→conscious stability explanation | S07/S12/S15 | C3 | semantic target recurs; source says not computing/generated consciousness | NOT ESTABLISHED |
| CON-CIR-005 | independently chosen bounds? | S07/S18 Remaining Questions | C8 | numeric derivation/extraction unresolved; no fitting to positive cases procedure located | NOT ESTABLISHED |
| CON-CIR-006 | gate existence→operation→logs | S04/S12; GATE-PL-001–003 | C0 | gate is supplied; output does not prove gate creation | NO |
| CON-CIR-007 | gate location→frontier→label of selected transition | S11/S12; GATE-PL-004/006 | C3 | functional boundary exists before phenomenal reading; stronger aspect separated016 | NOT ESTABLISHED |
| CON-CIR-008 | logs→reference→new logs with unspecified first logs | S09/S12; LOG-CIRC-005/008 | C5 | no universal prior consciousness requirement for log formation | NOT ESTABLISHED |
| CON-CIR-009 | system boundary→own logs→observer-like identity | S04; OWN-LOG-001–006 | C5 | initial ownership unresolved; observer→ownership reverse rule not located | NOT ESTABLISHED |
| CON-CIR-010 | fast→gate→logs→I/Phi→bias→next fast | S09; CON-SR-001/002 | C2 | dynamical feedback; explanatory sequence not proof cycle | NO |
| CON-CIR-011 | sustained loop→observer name→same loop characterization | S04; CON-SR-003 | C1 | conditional naming, subject expressly not added | NO |
| CON-CIR-012 | observer-like function→phenomenal subject? | S04/S05/S14; OBS-003/005 | C0 | source denies added contemplating subject; requested reverse identity not asserted | NO |
| CON-CIR-013 | TCA function→experienced ego→interpretive location | S05/S08; EGO-CIRC-001–005 | C3 | ego not input/controller; no hidden selector inferred | NOT ESTABLISHED |
| CON-CIR-014 | logs/self terrain→narrative→updated logs | S10/S12/S18; SELF-CIRC-002/003 | C2 | recurrent maintenance, no timeless self-proof | NO |
| CON-CIR-015 | experience logs→self→later opening / first self? | S12/S18; SELF-CIRC-004/005 | C5 | subclass of experience logs does not imply all logs need prior consciousness | NOT ESTABLISHED |
| CON-CIR-016 | phenomenal frontier definition→boundary-position explanation of qualia | S11:11–65,175–221; QUA-CIRC-001/002/009 | C7 | experienced endpoint is already in explanatory premise; stronger explanation reading is SERIOUS criterion4; definitional reading and hard-problem disclaimer retained | NOT ESTABLISHED; candidate only |
| CON-CIR-017 | T_Phi/qualia clarity described using named foreground | S11; QUA-CIRC-004 | C3 | target label assumed, index explicitly does not generate consciousness | NOT ESTABLISHED |
| CON-CIR-018 | live not retained→stored thing called residue | S11/S13; MEAS-CIRC-001/002 | C1 | category distinction, not independent empirical confirmation | NO |
| CON-CIR-019 | measurement succeeds→no live capture→all records classified residues | S13 Precision/Measurement Is Not Error | C6 | potential evidence-loop structure; no blanket every-outcome-confirms rule or contrary-data rejection established | NOT ESTABLISHED |
| CON-CIR-020 | own state→introspection→new log→own state | S13; MEAS-CIRC-005 | C2 | intervention/feedback is not proof circularity | NO |
| CON-CIR-021 | explicit awareness criterion→reportable evidence→same label | S10; REPORT-CIRC-003/006 | C3 | criterion/interpretation candidate; general conscious state/reportability explicitly distinct | NOT ESTABLISHED |
| CON-CIR-022 | conscious state iff reportability? | S09; REPORT-CIRC-001 | C0 | source explicitly denies identity; do not add biconditional | NO |
| CON-CIR-023 | functional roles→generic neural carriers→regime interpretation | S14; NEU-PL | C0 | no reverse neural measurement proof used to define same carrier in supplied account | NO |
| CON-CIR-024 | unequal influence→many selected phenomena→projection umbrella | S06; PROJ-PL | C3 | local definition plus retrospective instance grouping, not one typed operator proof | NOT ESTABLISHED |
| CON-CIR-025 | projection requires an intentional subject? | S06 psychological disclaimer | C0 | axiomatic structural definition explicitly presupposes no subject | NO |
| CON-CIR-026 | nonclosure required→persistent loop called nonclosed | S04/S06/S09; NC-PL | C3 | condition/explanatory reuse; external theorem validity not assessed | NOT ESTABLISHED |
| CON-CIR-027 | nonclosed object→unfinished theory→same descriptive vocabulary | S18/S19; NC-PL-008 | C3 | method/object analogy; theory incompleteness not explicit empirical proof of object | NO |
| CON-CIR-028 | VED-grounded basis versus neither grounds other | S06:305–331; VED-CIRC | C8 | support-language tension; no VED theorem proved from Consciousness found | NOT ESTABLISHED |
| CON-CIR-029 | Consciousness SSO→CT GPU→Consciousness note/future theory | CON-XDEP-001 | C4 | reciprocal authority routing, note/current paper distinct; exact same-claim proof loop unresolved | NOT ESTABLISHED |
| CON-CIR-030 | CT field/Phi*→Consciousness landscape analogy | CON-XDEP-002/003/006 | C0 | CT local formal construction supplies non-Consciousness node; no endorsement of its validity | NO |
| CON-CIR-031 | Consciousness qualia→CT insight comparison | CON-XDEP-004 | C3 | CT excludes subjective-experience explanation; no CT-returned qualia proof | NOT ESTABLISHED |
| CON-CIR-032 | referenceable CT terrain needs SSO, SSO references terrain | CON-XDEP-005 | C5 | accessibility versus landscape existence distinct; first-formation direction unresolved | NOT ESTABLISHED |
| CON-CIR-033 | Consciousness four-layer thesis↔Intelligence comparison | CON-XDEP-008 | C4 | mutual expository authority, not common-carrier/identity theorem | NOT ESTABLISHED |
| CON-CIR-034 | Consciousness projection→Intelligence stopping instance | CON-XDEP-007/010 | C0 | specific reverse proof of original primitive not located | NO |
| CON-CIR-035 | Consciousness precursor↔Intelligence transitional-layer account | CON-XDEP-009/011 | C4 | comparative handoff supports placement; no closed phenomenal proof chain established | NOT ESTABLISHED |
| CON-CIR-036 | JA C(t) names opening→gap collapse kills C(t) | CON-EQ-101/140; WIN-PRELOAD-009 | C3 | definition/collapse extension, not independently measured criterion | NOT ESTABLISHED |
| CON-CIR-037 | figure conscious/qualia label→illustration of same region | FIG-01/03/05 | C3 | output labeling; schematic not generated measurement | NOT ESTABLISHED |
| CON-CIR-038 | figure6 JA phase labels→equivalent regimes | FIG-06 | C8 | phase-name import not an explained bridge; loop contribution unresolved | NOT ESTABLISHED |
| CON-CIR-039 | six/three conditions, criterion independence and converse | S04/S06/S15; NS-CIRC | C8 | requirement scope differs; stronger sufficient reading must not be inferred from necessity | NOT ESTABLISHED |

## 28. Serious circularity candidates

SERIOUSはuser criteriaの少なくとも一つがsource上で実質的に見られる場合に限定する。分類表のHIGH role riskやP3 preloadを自動的にSERIOUSへ変換しない。今回のSERIOUSは1件、criterion4に限定。C7=1はsource-level vicious circularityの確立件数ではない。

| SERIOUS | Master | Criterion materially present | Exact source chain | Why not final invalidity / source counter-scope |
| --- | --- | --- | --- | --- |
| SERIOUS-001 | CON-CIR-016 | 4: phenomenal property is named in premise used for phenomenal explanation | S11 EN:12 foreground called phenomenal → :64 transition identified as experienced qualia → :179 reason for felt centrality is live-boundary position → :208/212/214 boundary-experience question is said answerable through gap/mu/tau/gradient/gate | stronger explanatory reading reuses experienced endpoint, so retain claim-threatening candidate. EN:216 explicitly does not claim solved; boundary placement may be a definition/repositioning, not independent proof. No final explanation failure or theory-invalid verdict |

候補の二つの読みを混ぜない。

- 定義としての読み：qualiaという語をlive frontierに割り当てる。これはC1/C3相当の命名・解釈であり、それだけではviciousではない。
- 説明としての読み：このfrontierがphenomenalであることを前提に、そのfrontierという位置を「なぜこの経験が現れるか」の根拠へ再使用する。この読みでは説明対象と実質的に同じ経験属性がsupport premiseに含まれるためC7候補を保持する。

独立のphenomenal endpoint同定があるかという問いはOPEN。ここではその実証十分性を判定しない。windowには定義独立性問題を残すが、既知positive casesだけで条件をfitした手続は所在せずcriterion6成立とはしない。own logsはsystem帰属を前提とするが、phenomenal subjectを前提として同subjectを導出する文ではないためcriterion3成立とはしない。相互引用はあるが唯一の根拠を閉じた同一claimから得るchainは未確立で、criterion5の重大候補へ自動昇格しない。測定は残余分析・操作の研究方向を許すため、非捕捉の説明をそのまま「全結果を確認とみなすshield」と断定しない。

## 29. Figure preload

| FIG-PL | Figure | Visual preload | Output label present? | Stronger than prose? |
| --- | --- | --- | --- | --- |
| FIG-PL-001 | FIG-01 SSO density | fast/slow streams, partial boundary and finite conditions drawn first | conscious access already central | S04 not-yet-consciousness qualifier is not represented by separate test; label/architecture scope difference, no new proof |
| FIG-PL-002 | FIG-02 TCA | converter/coupling chamber and log feedback supplied | TCA/attention name | effective mechanical analogy like body; no literal neural device inferred |
| FIG-PL-003 | FIG-03 phase window | two axes, min/max, finite central region | conscious access EN / 意識 JA | JA label broader; lower bound differs body. Neither version supplies independent classification data |
| FIG-PL-004 | FIG-04 loop | six-step connectivity/open loop already drawn | consciousness persists title | same maintenance reading as body; Phi-update display vs I-update condition kept distinct |
| FIG-PL-005 | FIG-05 qualia | middle transitional band and measurement arrow prepositioned | Qualia live / residue explicitly labeled | same strong phenomenal naming as body, not additional empirical result |
| FIG-PL-006 | FIG-06 closure mapping | paired layer boxes/equivalence arrows | consciousness window / observation regime | JA-only phase names add interpretation; neither grounds other retained |

| Figure | Current EN | Current JA |
| --- | --- | --- |
| FIG-01 | [EN](../../consciousness/figures/figure1_sso_density.pdf) | [JA](../../consciousness/figures_ja/figure1_sso_density_jp.pdf) |
| FIG-02 | [EN](../../consciousness/figures/figure2_tca.pdf) | [JA](../../consciousness/figures_ja/figure2_tca_jp.pdf) |
| FIG-03 | [EN](../../consciousness/figures/figure3_nonclosure_window.pdf) | [JA](../../consciousness/figures_ja/figure3_nonclosure_window_jp.pdf) |
| FIG-04 | [EN](../../consciousness/figures/figure4_log_referencing_loop.pdf) | [JA](../../consciousness/figures_ja/figure4_log_referencing_loop_jp.pdf) |
| FIG-05 | [EN](../../consciousness/figures/figure5_qualia_boundary.pdf) | [JA](../../consciousness/figures_ja/figure5_qualia_boundary_jp.pdf) |
| FIG-06 | [EN](../../consciousness/figures/figure6_observation_regime.pdf) | [JA](../../consciousness/figures_ja/figure6_observation_regime_jp.pdf) |

PDF skillで12図のtext layerを確認し、EN6図および高priority JA FIG-03/06を一時renderして視認した。Popplerはこの環境で未配置のため既存Ghostscriptを閲覧用rasterizationに使用。PDF/figure sourceのbuildや再生成・修正はしていない。図中の位相境界はoutput location/labelを供給するschematicであり、実測による領域抽出と呼ばない。

## 30. EN / JA parity

| PAR-CIRC | Family | EN/JA checked distinction | Classification |
| --- | --- | --- | --- |
| PAR-CIRC-001 | observer | both own-log loop; neither adds subject | SAME |
| PAR-CIRC-002 | SSO condition sets | both six necessary/not-yet versus three then state obtains | SAME |
| PAR-CIRC-003 | qualia frontier | both experienced boundary naming then explanatory reuse | SAME |
| PAR-CIRC-004 | qualia measurement | both stabilization/residue/precision rationale; no nothing-observable claim | SAME |
| PAR-CIRC-005 | self/ego | both derived terrain/conversion, not causal subject | SAME |
| PAR-CIRC-006 | window core iff | both explicit stable-consciousness/window biconditional | SAME |
| PAR-CIRC-007 | window figure target | EN conscious access versus JA 意識 | JA STRONGER |
| PAR-CIRC-008 | JA C(t) collapse | JA explicit gap→opening-function disappearance; EN only prose | DIFFERENT LOOP STRUCTURE |
| PAR-CIRC-009 | JA not-state display | JA non-state formulation beside regime/state prose; EN lacks display | DIFFERENT LOOP STRUCTURE |
| PAR-CIRC-010 | CT correspondence | both common grammar/qualia-insight with nonidentity/non-grounding | SAME |
| PAR-CIRC-011 | older PDE | both phenomenological basis wording and non-grounding caption | SAME |
| PAR-CIRC-012 | figure6 phases | JA adds probability/classical phase names, shorter causal qualifier | DIFFERENT LOOP STRUCTURE |
| PAR-CIRC-013 | TCA/experienced ego | both no agent equation/input; experiential correspondence | SAME |
| PAR-CIRC-014 | theory/object nonclosure | both methodological analogy/incomplete-theory wording | SAME |

DIFFERENT LOOP STRUCTUREは接続表現・endpointの追加差を指し、片言語だけviciousとする判定ではない。Intelligence I JAの長いtransitional-layer説明は§23に実sourceで別記し、ConsciousnessのEN/JA parity件数へ混入させない。

## 31. Phase-03 uncertainty ledger

| CON-U | Unresolved question | Trace | Next-phase boundary |
| --- | --- | --- | --- |
| CON-U-059 | first-log bootstrap | LOG-CIRC-001–008; CIR-008 | log formation continuationとfirst initiationを分離 |
| CON-U-060 | own-log ownership | OWN-LOG-001–006; CIR-009 | system帰属規則を新設しない |
| CON-U-061 | subject/system boundary | OBS-BND-006–008; OBS-003/005 | phenomenal subjectを勝手に補わない |
| CON-U-062 | gate existence vs operation | GATE-PL-001–003 | gate発生モデルを供給しない |
| CON-U-063 | frontier phenomenality preload | CIR-016; SERIOUS-001 | label/definitionと説明前提を後続claim auditへ |
| CON-U-064 | window independence | WIN-PRELOAD-001–010; CIR-004/005 | calibration/evidenceの十分性は未判定 |
| CON-U-065 | biconditional reading | CON-EQ-067/161; NS-CIRC-005 | definitional iffを独立現象同定としない |
| CON-U-066 | measurement/noncapture rationale | MEAS-CIRC-001–007; CIR-019 | falsifiabilityやempirical adequacyを未判定 |
| CON-U-067 | SSO observer naming | CON-SR-003; CIR-011/012 | functional observerとphenomenal subjectの別を保持 |
| CON-U-068 | old PDE basis vs non-grounding | VED-CIRC-001–004; CIR-028 | historical version/typed translation未解消 |
| CON-U-069 | CT reciprocal source authority | CON-XDEP-001–006; CIR-029/032 | note/current/future paperを同一supportとしない |
| CON-U-070 | Intelligence reciprocal placement | CON-XDEP-007–012; CIR-033/035 | downstream理論の独立監査へ拡大しない |
| CON-U-071 | projection umbrella | PROJ-PL-001–008; CIR-024 | 共通typed operationを供給しない |
| CON-U-072 | theory/object nonclosure | NC-PL-008; CIR-027 | method analogyからobject truthを推論しない |
| CON-U-073 | self maintenance vs origin | SELF-CIRC-001–006; CIR-014/015 | developmental orderと初期化の区別 |
| CON-U-074 | explicit access vs report criterion | REPORT-CIRC-001–006; CIR-021/022 | conscious stateのbiconditionalを新設しない |
| CON-U-075 | generic neural carrier vs independent selection | NEU-PL-001–006; CIR-023 | neural mechanism/evidence verdictは留保 |
| CON-U-076 | JA endpoint/figure phase differences | PAR-CIRC-007–009/012; CIR-036/038 | source修正/notation統合をしない |
| CON-U-077 | SSO necessary/sufficient scope | NS-CIRC-001/002; CIR-039 | 条件集合の等価証明を補わない |
| CON-U-078 | TCA/ego experience correspondence | EGO-CIRC-001–005; CIR-013 | experiential namingとimplicit agentの別を保持 |

## 32. Validation

### Coverage

| Frozen Phase02 universe | Current coverage | Boundary preserved |
| --- | --- | --- |
| CON-EQ-001–178 / 52 families | PL-003–006/011–015/020/023–026/040–041; window/old PDE/IFGT/CT sections | no new equation-role classification or expression change |
| CON-RT-001–040 | R3 crossings all18 in CON-PB; non-R3 fast/field/projection in PL/FS/LOG/PROJ; RT020 observer,RT040 method in SR | no implied transitive bridge |
| CON-RC-001–024 | 001window;002/003SSO;004/005TCA-ego;006self;007–009qualia-gate;010/011gap-closure;012index;013Phi;014projection;015loop;016observer;017time;018mu;019C(t);020PDE;021report;022CT;023Bio;024figures | all role-risk families considered, not copied as circularity verdict |
| FS-ROLE-001–017 | FS-PL/PL/window/CON-PB, including JA C(t)/weights | no neural rate calibration |
| SSO-ROLE-001–018 | PL-017/018; observer; NS-CIRC-001/002; six/three/seven documentary distinctions | condition sets not made equivalent |
| TCA-ROLE-001–008 | PL-004/005/013–016/034/041; EGO-CIRC; PROJ-PL | no hidden chooser inferred |
| LOOP-STEP-001–006 | LOG-CIRC/CON-SR-001; CIR-010 | temporal feedback not proof cycle |
| CONSC-001–018 | OUT/DEF-EXPL/window/report/neural/NS/CT | not all consciousness terms identical |
| QUA-001–013 / GATE-ROLE-001–005 | QUA-CIRC/GATE-PL/MEAS-CIRC; CIR-016–019 | phenomenal endpoint not automatically functional boundary |
| SELF-ROLE-001–008 | observer/own-log/ego/self ledgers | subject explicitly not added; narrative terrain not new single object |
| Phase00 SELF-01–10 | 01→CON-SR-002/003; 02→CON-SR-001; 03→LOG-CIRC-003/004; 04→CON-SR-006; 05→CON-SR-007; 06→CON-SR-004; 07→CON-SR-005; 08→VED-CIRC-001–004; 09→NEU-PL/CON-PB-009; 10→CON-SR-013 | 10/10 source families traced; recurring dynamics and proof support kept separate |
| ACCESS-REL-001–010 | REPORT-CIRC/MEAS-CIRC/DEF-EXPL | no conscious-state=reportability identity |
| BND-ROLE-001–014 / Phase00 CON-BND-01–12 | OBS-BND-001–013 and OWN-LOG | all original boundary families included; ownership separately decomposed |
| TIME-ROLE-001–011 | PL-003–006/036; FS-PL; PB-002; LOG-CIRC; NS-CIRC; CIR-032 | external time/delay/CT limit/experience distinct |
| PROJ-ROLE-001–008 | PROJ-PL-001–008 and XDEP007/010 | upstream/downstream same word not same operator |
| CLO-ROLE-001–008 | PL-023–026/038/040; NC-PL/NS-CIRC | closure field not conscious C(t) |
| OLD-PDE-ROLE-001–006 / IFGT-ROLE-001–010 | VED-CIRC; PL-011–014/021/025/038 | old VED label/current IFGT analogue/CT kernel distinct |
| CT-ROLE-001–007 | CON-XDEP-001–006 / NC-PL-009 / CON-PB-015 | mutual citation not self-proving identity |
| FIG-ROLE-001–006 | FIG-PL-001–006, current12 figure files | no image changes |
| NS-ROLE-001–057 | 001–013fast/gate/log;014–017TCA/projection;018–026window/PDE;027–032loop/report;033–041qualia/measurement/self;042–050neural/window/limits;051–057mapping/CT/method/additional gates | no inference of converse or AND-combination across all conditions |
| CON-RCF-001–020 / PAR-ROLE-001–016 | corresponding PL/circularity sub-ledgers; PAR-CIRC-001–014 | compatible/tension does not predetermine C class |
| CON-U-001–058 | historical records unchanged; new CON-U-059–078 | no unresolved question marked solved by wording |

### Counts

| Metric | Count |
| --- | --- |
| preload entries | 43 |
| P0 | 32 |
| P1 | 19 |
| P2 | 20 |
| P3 | 6 |
| P4 | 16 |
| BENIGN REPRESENTATIONAL | 4 |
| STRUCTURALLY IMPORTANT | 10 |
| OUTPUT-SHAPING | 11 |
| OUTPUT-LOCATING | 1 |
| OUTPUT-LABELING | 6 |
| CLAIM-DEPENDENT | 8 |
| UNRESOLVED | 3 |
| outputs | 11 |
| window | 10 |
| fast | 8 |
| gate | 6 |
| logs | 8 |
| selfref | 13 |
| observer | 6 |
| boundaries | 13 |
| ownership | 6 |
| ego | 5 |
| self | 6 |
| qualia | 9 |
| measurement | 7 |
| access | 6 |
| neural | 6 |
| projection | 8 |
| nonclosure | 9 |
| ved | 4 |
| ct | 6 |
| intelligence | 6 |
| definitions | 6 |
| ns | 11 |
| bridges | 18 |
| circularity | 39 |
| serious | 1 |
| figures | 6 |
| C0 | 8 |
| C1 | 4 |
| C2 | 3 |
| C3 | 11 |
| C4 | 3 |
| C5 | 4 |
| C6 | 1 |
| C7 | 1 |
| C8 | 4 |
| EN/JA loop differences | 4 |
| new uncertainties | 20 |
| new uncertainty range | CON-U-059–078 |
| source-level vicious circularity established | NO |

### Independent local checks

source paths、current TeX inputs、figure references、local links、table列、fences、全PL/CIR/SR/PB/XDEP/U ID一意性、旧uncertainty非重複、ledger件数と分類合計、Phase02 coverageを検査した。18 R3 endpointsはPhase02 RTの役割分類を変更せず18/18逆引きした。Phase00 self-reference 10/10、observer/boundary 12/12は上表・§11に対応を明記した。

独立検査結果：local links 87参照、primary ID 311件に重複なし。current EN/JA42 sectionのTeX environment、entry includes、figure referencesを確認し、Phase01に保存された178 raw表示式との完全一致を確認した。表示式連結SHA256は `c3ef85df91bb704c3b482e2fc12574b4cf7c305a2bb6af04bbf81504b8ee6ebe`。本phase開始時のexisting 1,447 filesに対し、README以外の1,446 filesがbyte不変、削除0。本recordのみ新規、既存変更はREADMEのみ。source/equation・PDF・図・code・上流/下流・過去の監査に変更なし。

新規作成は本recordだけ、変更する既存fileは監査READMEだけ。一時snapshot/helper/検索索引/閲覧renderはrepository外 `${TEMP_EVIDENCE_ROOT}/consciousness_phase03.9gPxkj/`。current EN/JA42 sectionを対象としたtarget search hit699行は候補所在の索引であり、循環件数ではない。旧監査、working draft、PDF、figure、code、upstream/downstreamは保存する。外部文献・web・simulation・buildは使わない。

PDF確認はpreload label/arrowの目視用でありdistribution freshnessの再判定ではない。相互引用の探索で存在しなかった想定path（CT sections_ja、Intelligence I 01_preliminaries）はauthorityに含めず、実際の§9/§4とIntelligence II preliminariesへ解決した。`git diff --check`はexit 0、untracked record自身の`git diff --no-index --check /dev/null`はwhitespace診断0（new-file差分のexit 1）だった。既存dirty treeのtracked modifications 173件・untracked directories 4件は保持し、本phaseの2ファイルと混同しない。

## 33. Stop boundary

Phase03は完了し、Phase04 claim / evidence burden auditには進まず停止する。

preloadは事実上の入力・表現・ラベルの分類でありbad/illicitの判定ではない。self-reference/feedbackは原則としてproof circularityと別。first-log/own-log bootstrapは未解決だが、sourceが全log形成に先行意識を必須としているとは確認しない。observer-like organizationの命名はphenomenal subjectの生成証明ではない。SERIOUS候補1件はphenomenal endpointを説明前提に含む構造を保持するもので、source-level vicious circularityが確立したという結論ではない。

実証適合、evidence sufficiency、最終phenomenal explanation成否、理論valid/invalid、claim downgrade/upgrade/dispositionは行っていない。新しい式・notation・理論・bootstrap解・typed bridge・測定mapは導入していない。上流VED/Bio audit/core revisionはCLOSEDのまま、Consciousnessの妥当性へ自動継承しない。commit/pushなし。

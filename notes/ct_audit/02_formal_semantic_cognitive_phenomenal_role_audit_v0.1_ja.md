# CT Phase 02 — formal / semantic / cognitive / phenomenal role audit v0.1

## 0. Status

CT audit: IN PROGRESS。Phase00/01 COMPLETE、Phase02 COMPLETE。Phase03以降NOT STARTED。
実施日: 2026-09-10。CT source revision / equation revision: NOT STARTED。

本記録のHIGH等はrole混同の文面上の注意度であり、truth・妥当性・circularity・証拠十分性・dispositionではない。
Sourceの同定/機構/導出という語を引用・分類しても、その成立を監査で認定したことにはならない。

## 1. Authority / scope

[Phase00](00_dependency_inheritance_and_authority_record_v0.1_ja.md)、[Phase01](01_equation_symbol_object_inventory_v0.1_ja.md)、[audit README](README_ja.md)を保持。現在の作業ツリーをtask-start snapshotと比較。
EN canonicalはmain +12 included sections。JA working MDは非canonicalの対照、canonical JA entryはNOT LOCATEDのまま。

| Locator | Source path |
| --- | --- |
| S00 | [conceptual-topography/main.tex](../../conceptual-topography/main.tex) |
| S01 | [conceptual-topography/sections/abstract.tex](../../conceptual-topography/sections/abstract.tex) |
| S02 | [conceptual-topography/sections/introduction.tex](../../conceptual-topography/sections/introduction.tex) |
| S03 | [conceptual-topography/sections/intuitive_picture.tex](../../conceptual-topography/sections/intuitive_picture.tex) |
| S04 | [conceptual-topography/sections/formal_mapping.tex](../../conceptual-topography/sections/formal_mapping.tex) |
| S05 | [conceptual-topography/sections/core_equations.tex](../../conceptual-topography/sections/core_equations.tex) |
| S06 | [conceptual-topography/sections/structural_interpretation.tex](../../conceptual-topography/sections/structural_interpretation.tex) |
| S07 | [conceptual-topography/sections/dynamics.tex](../../conceptual-topography/sections/dynamics.tex) |
| S08 | [conceptual-topography/sections/multiscale.tex](../../conceptual-topography/sections/multiscale.tex) |
| S09 | [conceptual-topography/sections/pathologies.tex](../../conceptual-topography/sections/pathologies.tex) |
| S10 | [conceptual-topography/sections/relation_to_note.tex](../../conceptual-topography/sections/relation_to_note.tex) |
| S11 | [conceptual-topography/sections/discussion.tex](../../conceptual-topography/sections/discussion.tex) |
| S12 | [conceptual-topography/sections/conclusion.tex](../../conceptual-topography/sections/conclusion.tex) |

JA locatorsは[working MD](../../conceptual-topography/conceptual_topography_ja.md)の行番号、Sxx:nは上記EN fileの1-based行番号。局所節番号はsource自身の§番号。
[CT README](../../conceptual-topography/README.md)はsupporting notation。式のrawとsignatureはPhase01がauthority（EN12 blocks/14 relation rows、JA14 blocks、14 EQF、24 INLINE、53 SYM、22 operators）。

監査層: T0=formal、T1=representational/semantic、T2=cognitive/functional、T3=phenomenal/subjective。
T0→T1→T2→T3はvalid generative chainではなく、source内の役割の読み替えを表示する監査記法。
formal definition ≠ semantic identity; semantic interpretation ≠ cognitive mechanism; cognitive function ≠ phenomenal experience; correspondence ≠ identity; role reuse ≠ typed translation; same equation ≠ same explanatory level; definition ≠ mechanism; model necessity ≠ empirical necessity。

inferential movementという監査語を新しいCT inference operatorへ変えない。sourceのphenomenologically rigidityという語も、直ちに主観体験T3とせず、explicit felt/sense/experienceがある場合と区別する。数式中のcalRは領域、C_*は下付きstar（Phase01の文字同定を保持）。

## 2. Equation-role audit

各familyを一度ずつprimary targetにする。T3欄の「later」は式自体ではなく後続の同objectについての記述。—はその文脈でhigher-roleを認定しないことを示す。

| ID | EQF | Family | T0 role | T1 role | T2 role | T3 role | Source wording / locator | Role shift? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CT-ROLE-EQ-001 | CT-EQF-001 | potential/convolution | scalar potential / convolution | conceptual landscape (S04 table) | least-resistance bias (S04:38–40) | S03:92–93 experiences reflect geometry (later prose) | S04:33–40/58–60;S03:92;JA171–183/155 | YES; definition vs later experience attribution |
| CT-ROLE-EQ-002 | CT-EQF-002 | balance | density evolution + divergence/source | landscape deformation via sigma | cognitive evolution S05:41–50 | — | S05:10–50;S06:47–49;JA214–236 | YES via interpreted terms; no direct T3 assignment |
| CT-ROLE-EQ-003 | CT-EQF-003 | flow | J_I gradient/force flow field | — (content explicitly excluded) | thought as flow / trajectory | content in experience is downstream, not J_I identity | S04:64–66/113–114;S02:81–83;JA184/201 | YES field→trajectory→thought; exclusion retained |
| CT-ROLE-EQ-004 | CT-EQF-004 | force | F_I gradient equality chain | landscape geometry | least cognitive resistance | — | S05:16–18;S04:61–63;JA183/218 | YES directional role; not separate neural force |
| CT-ROLE-EQ-005 | CT-EQF-005 | source decomposition | drive minus dissip minus barrier | conceptual terrain deformation | input / forgetting / resistance | — | S04:67–69;S05:21–50;JA185/222–236 | YES component interpretation; short suffixes not merged |
| CT-ROLE-EQ-006 | CT-EQF-006 | drive | a Delta saturation expression | novel conceptual input | perception/reward/prediction-error influx | experience named as input, not claim of producing experience | S05:28/42–43;S04:70–72;S11:33–35;JA186/234/531 | YES T2; no automatic phenomenal role from experience noun |
| CT-ROLE-EQ-007 | CT-EQF-007 | dissipation | Gamma C, repeated | flattened conceptual wells | forgetting/habituation/recall context | — | S05:30/44–45;S07:35–45;JA228/235/361–367 | YES; decay→memory interpretation |
| CT-ROLE-EQ-008 | CT-EQF-008 | barrier | reciprocal boundary term | conceptual overclosure | belief resistance / repetitive thought | phenomenologically rigidity, not necessarily first-person T3 | S05:32/46–50;S07:55–65;S09:31–38;JA230/236/374–375 | YES; EN effective vs JA prohibition |
| CT-ROLE-EQ-009 | CT-EQF-009 | coupling | L expression, token-gradient term | concept attractor / semantic drift context | reuse, stable recursion, lowers cost | — directly; understanding phenotype is separate chain | S05:54–92;S06:58–64;S07:24–31;JA240–248/352–357 | YES causal mechanism language distinct from term |
| CT-ROLE-EQ-010 | CT-EQF-010 | sedimentation | tau→infinity, Phi* target | mature conceptual landscape | learning/history/reuse | not inspected in experience (S01:9–12), not limit=experience | S05:96–122;S01:9–12;S07:10–31;JA254–256 | YES naming + history; nonstatic qualification retained |
| CT-ROLE-EQ-011 | CT-EQF-011 | concept stability | approximate zero gradient + perturbation stability | concept local definition | depth/resistance, context, precision used later | — in definition | S05:126–135;S06:35–44;JA261–265 | YES explicit local naming, not by itself conflation |
| CT-ROLE-EQ-012 | CT-EQF-012 | understanding | regional integral < theta | conceptual region, not epistemic correct meaning | understanding Definition | sense of understanding via S10:28/51–53 and S03:18–20 | S05:138–152;S10:28/51–53;JA267–272/488 | YES T0→T2 distinct from T2/T0→T3 correspondence |
| CT-ROLE-EQ-013 | CT-EQF-013 | positivity | I>0 quantified | no complete conceptual closure | future differentiation/innovation | — | S05:158–185;S08:83–88;JA276–284/430 | YES conceptual openness; EN not-pointwise guard |
| CT-ROLE-EQ-014 | CT-EQF-014 | vocabulary | set with S(ell_i)>epsilon | vocabulary / distribution naming | use/reuse shapes vocabulary | — | S06:69–82;JA326–335 | YES; set/distribution role difference |

## 3. Inline-role audit

Phase01の24familiesを別母数で照合。複数roleタグはtyped translationの成立ではない。

| ID | INLINE | Relation | Roles | Source | Audit distinction |
| --- | --- | --- | --- | --- | --- |
| CT-ROLE-INLINE-001 | CT-INLINE-001 | I=f(1-C) | T0→T1; T0→T2 | S04:14–25;JA163–167 | projection + unresolved tension / active regions; no empirical identity |
| CT-ROLE-INLINE-002 | CT-INLINE-002 | Phi=K*I | T0→T1 | S04:33–40/58;S10:24;JA182/484 | primary potential vs conceptual terrain |
| CT-ROLE-INLINE-003 | CT-INLINE-003 | linear Phi approximation | T0 only | S00:89–90;JA18 | no independent higher-layer assignment |
| CT-ROLE-INLINE-004 | CT-INLINE-004 | C<Cmax | T0→T1 | S00:93;S05:162–177;JA278 | ideal boundary vs conceptual completeness |
| CT-ROLE-INLINE-005 | CT-INLINE-005 | C range | T0→T1 | S04:52–54;JA180 | range attached to fixation; no unit inference |
| CT-ROLE-INLINE-006 | CT-INLINE-006 | C_*<Cmax | T0/T1 | S05:36–39 | saturation/ideal boundary within model; JA prose absent |
| CT-ROLE-INLINE-007 | CT-INLINE-007 | Q extraction | T0→T2; T1 representational token | S04:79–101;JA189–193 | operator output→re-addressable use, not intrinsic meaning |
| CT-ROLE-INLINE-008 | CT-INLINE-008 | recursive loop | T0→T1/T2 | S01:24–27;S05:105–110;FIG003;JA34 | sedimentation and search labels; no proof order inferred |
| CT-ROLE-INLINE-009 | CT-INLINE-009 | Phi→Phi* | T0→T1/T2 | S01:27;S05:119–122;JA34/256 | landscape/history; limit vs semantic maturation |
| CT-ROLE-INLINE-010 | CT-INLINE-010 | low-gradient concept | T0→T1 | S02:74–76;S06:22–23;JA87/297 | explicit naming / cognitive solution-class context |
| CT-ROLE-INLINE-011 | CT-INLINE-011 | positive I repetitions | T0→T1/T2 | S01:33–36;S08:83–88;JA41/95/430 | openness/differentiation; preserve ENJA qualifiers |
| CT-ROLE-INLINE-012 | CT-INLINE-012 | J_I flow | T0→T2 | S04:64–66;JA184 | field/trajectory/thought not automatically same object |
| CT-ROLE-INLINE-013 | CT-INLINE-013 | sigma short suffixes | T0→T1/T2 | S04:67–69;JA185 | landscape deformation rate; phase01 alias uncertainty retained |
| CT-ROLE-INLINE-014 | CT-INLINE-014 | gradient direction / magnitude | T0→T2; T0→T3 via context | S03:46–50/92;S04:61;JA130–131/155 | cognitive resistance vs ease; not same as potential |
| CT-ROLE-INLINE-015 | CT-INLINE-015 | coupling short term | T0→T2 | S05:67–69;FIG002 | reuse→deepening/lower cost |
| CT-ROLE-INLINE-016 | CT-INLINE-016 | JA positivity chain | T0→T1/T2 | JA280–284;EN S05:168–177 comparator | generically gradients/flow→no final conceptual stasis |
| CT-ROLE-INLINE-017 | CT-INLINE-017 | C→Cmax | T0→T2 | S07:55–65;JA373–375 | effective resistance vs divergent barrier rhetoric |
| CT-ROLE-INLINE-018 | CT-INLINE-018 | -min Phi depth | T0→T1/T2 | S06:35–37;JA307 | depth measures conceptual robustness |
| CT-ROLE-INLINE-019 | CT-INLINE-019 | token stability set | T0→T1; T2 input | S06:69–82;JA326–335 | vocabulary vs usage/stability functional |
| CT-ROLE-INLINE-020 | CT-INLINE-020 | -Phi passability | T0→T2 | S10:25;JA485 | note correspondence not new definition of meaning |
| CT-ROLE-INLINE-021 | CT-INLINE-021 | unbounded integral shorthand | T0→T3 | S10:28/51–53;JA488/502 | sense of understanding formal correspondence, not extra empirical criterion |
| CT-ROLE-INLINE-022 | CT-INLINE-022 | J_C README | T0 only / cross-source reuse | CT README Variable Convention | no CT-specific cognitive trajectory assigned to J_C |
| CT-ROLE-INLINE-023 | CT-INLINE-023 | notation macros | T0 presentation only | S00:47–51 | literal alias not role transition |
| CT-ROLE-INLINE-024 | CT-INLINE-024 | tau / Phi* / collective Phi bundle | T0→T3 / T0→T1 / T1→T2 | S04:76–86;S05:119–122;S08:59–75;JA188/256/417 | separate timing/history/social roles, not one composite mapping |

## 4. Role transitions

集計単位は主edgeを一つ持つsource-transition family。同じ主張のEN/JA・summary再掲は原則一行、意味が変わるJA経験語等は別行。
表中のfrom/toはlogical/generative dependencyではない。定義・否定的access relation・appositionもroleを明示しているため記録するが、単なる同paragraph内の共起は数えない。

| TRANS | Edge | Source | From object/role | To interpretation | Wording | Explicit/implicit |
| --- | --- | --- | --- | --- | --- | --- |
| CT-TRANS-001 | T0→T1 | S04:58–60;S01:9–10 | Phi scalar potential | conceptual landscape | the conceptual landscape itself / defined as | EXPLICIT |
| CT-TRANS-002 | T0→T1 | S04:14–21/55–57 | I density | unresolved conceptual tension | represents | EXPLICIT |
| CT-TRANS-003 | T0→T2 | S04:24–25 | high I | conceptually active regions | corresponds | EXPLICIT |
| CT-TRANS-004 | T0→T1 | S04:52–54 | C | conceptual fixation | table interpretation | EXPLICIT |
| CT-TRANS-005 | T0→T2 | S04:61–66;S02:81–83 | gradient/J_I field | least cognitive resistance / thought trajectory | thought is / direction of | EXPLICIT |
| CT-TRANS-006 | T0→T3 | S04:76–78;JA188 | tau ordering parameter | experiential time | table pairing | EXPLICIT |
| CT-TRANS-007 | T0→T1 | S05:126–135 | stable near-zero-gradient region | concept | Definition: is | EXPLICIT |
| CT-TRANS-008 | T0→T2 | S05:138–152 | integral threshold | understanding | Definition: is the state | EXPLICIT |
| CT-TRANS-009 | T2→T3 | S03:18–20;JA121 | movement through region of thought | experience of understanding | is not ... but a change in ease | EXPLICIT |
| CT-TRANS-010 | T0→T3 | S10:28/51–53;JA488 | traversal integral reduction | sense of understanding | formal correspondence | EXPLICIT |
| CT-TRANS-011 | T0→T1 | S03:64–65 | available trajectory set | meaning of a concept | is, in this framework | EXPLICIT |
| CT-TRANS-012 | T1→T3 | JA141 | attractor's available trajectory interpretation | meaning as experienced | 下流的解釈として扱う | EXPLICIT |
| CT-TRANS-013 | T0→T3 | S03:84–93;JA150–155 | uninspected Phi geometry | thoughts come naturally / sudden understanding | gives rise to / experiences reflect | EXPLICIT |
| CT-TRANS-014 | T1→T2 | S03:78–80 | similar conceptual landscapes | communication success | because | EXPLICIT |
| CT-TRANS-015 | T0→T2 | S05:42–43;S11:33–35 | drive term | input / prediction error influx | represents / corresponds | EXPLICIT |
| CT-TRANS-016 | T0→T2 | S05:44–45;S07:35–45 | Gamma C / flattening-redeepening | forgetting / remembering | represents / corresponds | EXPLICIT |
| CT-TRANS-017 | T0→T2 | S07:57–65 | barrier response | resistance to belief revision | accounts for | EXPLICIT |
| CT-TRANS-018 | T0→T2 | S05:54–92;S07:24–31 | token-gradient coupling | low-cost reuse / learning stabilization | requires / ensures / self-sustaining | EXPLICIT |
| CT-TRANS-019 | T0→T1 | S05:114–122 | Phi* long-time target | sedimented conceptual landscape | is | EXPLICIT |
| CT-TRANS-020 | T0→T2 | S05:119–122;S07:10–31 | history-dependent reshaping | learning/sedimentation | reflects history / process | EXPLICIT |
| CT-TRANS-021 | T0→T1 | S06:39–44 | width / curvature | contextual range / precision | measures / produces | EXPLICIT |
| CT-TRANS-022 | T1→T2 | S06:58–64 | concept boundary shift | semantic drift / conceptual change process | mechanistic account | EXPLICIT |
| CT-TRANS-023 | T0→T1 | S06:53–56;S07:49–53 | ridge/topological relocation | category distinction / concept meaning change | correspond / corresponds | EXPLICIT |
| CT-TRANS-024 | T0→T1 | S06:69–77 | stability set | vocabulary | constitutes / distribution | EXPLICIT |
| CT-TRANS-025 | T0→T2 | S06:21–25;S10:29 | limit-cycle flow | recurring/habitual thought | cognitive interpretation table | EXPLICIT |
| CT-TRANS-026 | T0→T2 | S07 heading:67 / 69–74 | rapid topology change/bifurcation | insight | Insight as / in field-theoretic terms | EXPLICIT (heading + paragraph) |
| CT-TRANS-027 | T0→T3 | S07:69–79;JA379–382 | topology threshold | phenomenology / subjective suddenness | corresponds / reflects | EXPLICIT |
| CT-TRANS-028 | T2→T3 | S07:69–71 | insight (problem resolution/connection) | sudden sense of resolution | phenomenology of insight — sudden sense | EXPLICIT apposition |
| CT-TRANS-029 | T0→T1 | S05:168–177;JA280 | I>0 nonclosure | no complete conceptual closure | excludes / 含意 | EXPLICIT; ENJA predicates separate |
| CT-TRANS-030 | T1→T2 | S08:83–88;JA430 | open social landscape | innovation/differentiation | remain possible / 保証 | EXPLICIT |
| CT-TRANS-031 | T0→T1 | S08:42–59 | correlated well geometry / collective Phi | shared conceptual landscape | emerges / collective Phi | EXPLICIT; scale extension separated |
| CT-TRANS-032 | T1→T2 | S08:56–66 | shared attractor depth | norms/institutions/stability | correspond / are / follows from | EXPLICIT |
| CT-TRANS-033 | T1→T2 | S08:70–81 | shared landscape maintenance | collective intelligence | Intelligence is | EXPLICIT |
| CT-TRANS-034 | T0→T2 | S09:31–46 | barrier or dissipation dominated wells | rigidity / unstable thought / durable understanding | corresponds phenomenologically / preventing | EXPLICIT; not automatically T3 |
| CT-TRANS-035 | T1→T2 | S09:48–55 | fragmented shared landscape | communication failure / polarization | structural basis | EXPLICIT |
| CT-TRANS-036 | T0→T1 | S12:66–71;JA576 | projected physical stabilization / equation regimes | concept/particle comparison | same generative grammar / 同一基礎方程式 | EXPLICIT cross-scale |
| CT-TRANS-037 | T0→T2 | S11:33–35 | well deepening | long-term error minimization | can be understood as | EXPLICIT comparison |
| CT-TRANS-038 | T0→T2 | S04:79–101;S08:13–16 | Q discrete output | re-addressing / internal control | discrete operator / function as | EXPLICIT |
| CT-TRANS-039 | T1→T3 | S01:9–12;S12:12–16 | conceptual structure that constrains thought | not directly accessible to inspection/experience | without being directly accessible | EXPLICIT negative access relation |

## 5. High-priority transitions

| Object | Separated uses | Trace |
| --- | --- | --- |
| Phi | potential→landscape; meaning-related available trajectories; collective landscapeを別に読む | TRANS001/011/031;MEANING004;SOCIALROLE004 |
| J_I | field→trajectory→thought、content否定、figure search labelsは別 | TRANS005/025;THOUGHT001–009 |
| tau | derivative/order、conceptual development、experiential timeを分離 | TRANS006;TIMEROLE001–009 |
| concept | low-gradient+perturbation Definition、属性の説明、semantic category | TRANS007/021/023;CONFL002/003 |
| understanding | integral/threshold cognitive definition、felt ease correspondence | TRANS008/009/010;CONFL004 |
| insight | topology event、cognitive resolution、subjective suddenness | TRANS026/027/028;INSIGHTROLE001–008 |
| collective Phi | correlated individual wells、shared semantics、institutions/intelligence | TRANS031/032/033;SOCIALROLE001–011 |
| token coupling | mathematical term、discrete unit、reuse-learning mechanism | TRANS018/038;TOKENROLE001–009;MECH001–011 |

### 5.1 Symbol/object coverage crosswalk

Phase01の全53symbol familiesをscopeに入れ、higher-layer役割が付かない係数・aliasesも明示。表中EQ001などはCT-ROLE-EQ、INLINEはCT-ROLE-INLINEを指す。REFの未定型演算は新しい型を補わない。

| Phase01 SYM | Glyph | Roles located | Role ledger / source | Phase00 OBJ |
| --- | --- | --- | --- | --- |
| CT-SYM-001 | x | T0/T1 | S04:20;FIGROLE001;conceptual position | 001 |
| CT-SYM-002 | x_1,x_2 | T0 | FIGROLE001 | 001 |
| CT-SYM-003 | \tau | T0/T2/T3 | TIMEROLE001–009;TRANS006 | 002 |
| CT-SYM-004 | C | T0/T1 | TRANS004;BARRIER002 | 003 |
| CT-SYM-005 | C_* | T0/T1 | BARRIER002;ROLEVAR006 | 020 |
| CT-SYM-006 | C_{\max} / \Cmax | T0/T1 | BARRIER002/006;POSROLE002 | 019 |
| CT-SYM-007 | I | T0/T1/T2 | TRANS002/003;POSROLE001 | 004 |
| CT-SYM-008 | f | T0; interpreted via I | EQF013;POSROLE002 | 004 |
| CT-SYM-009 | \delta I | T0/T1 | S04:73–75 unresolved conceptual residue | 012 |
| CT-SYM-010 | \Phi | T0/T1/T2/T3 in distinct passages | TRANS001/013;SCOPE002 | 005 |
| CT-SYM-011 | \Phi^{*} / \Phistar | T0/T1/T2 | ASYMROLE001–009 | 016 |
| CT-SYM-012 | K | T0 | EQF001;SCOPE007; no new semantic kernel | 006 |
| CT-SYM-013 | \nabla\Phi | T0/T2; T3 contextual ease | TRANS005;UNDERROLE003/008 | 007 |
| CT-SYM-014 | \nabla I | T0; cognitive flow context | EQF003;THOUGHT001 | 008 |
| CT-SYM-015 | \nabla C | T0 | EQF004;BARRIER004 context not independent cognitive C-gradient | 003 |
| CT-SYM-016 | J (flow) | T0/T2 labels | FIGROLE013;ROLECONFLICT013 | 008 |
| CT-SYM-017 | J_I / J_{\!I} / \JI | T0/T2 | THOUGHT001–009; content exclusion retained | 008 |
| CT-SYM-018 | J_C / J_{\!C} / \JC | T0 only CT use | INLINE022 | 009 |
| CT-SYM-019 | \sigma | T0/T1/T2 | EQF005;INLINE013 | 010 |
| CT-SYM-020 | \sigma_d,\sigma_p,\sigma_b | T0/T1/T2 table context | INLINE013; Phase01 alias uncertainty | 010 |
| CT-SYM-021 | \sigma_{\mathrm{drive}} | T0/T2 | TRANS015;MECHLANG015 | 010,011 |
| CT-SYM-022 | \sigma_{\mathrm{dissip}} | T0/T2 | TRANS016;ASYMROLE005 | 010,031 |
| CT-SYM-023 | \sigma_{\mathrm{barrier}} | T0/T1/T2 | BARRIER001–008 | 010 |
| CT-SYM-024 | F_I | T0/T2 context | EQF004;TRANS005 | 021 |
| CT-SYM-025 | \alpha | T0 | EQF004 effective coefficient; no independent semantic role | 021 |
| CT-SYM-026 | \mu | T0 | EQF003 coefficient; CT vs Con role not merged | 021 |
| CT-SYM-027 | D | T0 | EQF003 coefficient | 021 |
| CT-SYM-028 | \Gamma | T0/T2 effective decay context | EQF007;THOUGHT008 | 022,031 |
| CT-SYM-029 | a | T0 | EQF006 coefficient | 022 |
| CT-SYM-030 | \kappa_B | T0 | EQF008 coefficient | 022 |
| CT-SYM-031 | \ell_i | T0/T1/T2; intrinsic meaning denied | TOKENROLE001–009 | 013 |
| CT-SYM-032 | \ell (unindexed) | T0 unresolved argument | TOKENROLE005;MECH001 | 015 |
| CT-SYM-033 | i | T0 index | MECH001 | 013 |
| CT-SYM-034 | \lambda | T0 coupling coefficient | MECH001 | 015 |
| CT-SYM-035 | \mathcal L_{\mathrm{eff}} | T0; T2 context not L identity | MECH001–011 | 015 |
| CT-SYM-036 | \mathcal L_{\mathrm{field}}[I] | T0 | MECH001 | 015 |
| CT-SYM-037 | \mathcal L_{\mathrm{token}}[\ell] | T0 | MECH001 | 015 |
| CT-SYM-038 | \mathcal Q | T0/T2 extraction role | TOKENROLE003/004;IDREL011 | 014 |
| CT-SYM-039 | constraints / \cdot (Q slot) | T0 unresolved input slot | DEFROLE015 | 014 |
| CT-SYM-040 | \mathcal R | T0 region with T1 conceptual label | UNDERROLE001–003 | 018 |
| CT-SYM-041 | \theta | T0 cognitive criterion role | UNDERROLE002/004 | 018 |
| CT-SYM-042 | \mathcal V | T0/T1 | DEFROLE008;ROLECONFLICT006 | 025 |
| CT-SYM-043 | S(\ell_i) | T0 / T2 reuse inputs | INLINE019;NS025 | 025 |
| CT-SYM-044 | \epsilon | T0 threshold / T1 membership | NS025 | 025 |
| CT-SYM-045 | \Phi_0 | T0 offset only | INLINE003 | 021 |
| CT-SYM-046 | \|\nabla\Phi\| / \lvert\nabla\Phi\rvert | T0/T2/T3 via separate cost contexts | UNDERROLE001–008 | 018 |
| CT-SYM-047 | -\min\Phi | T0/T1/T2 | CONCEPTROLE005/006;IDREL014 | 023 |
| CT-SYM-048 | collective \Phi | T0 naming / T1/T2 extension | SOCIALROLE001–011 | 028 |
| CT-SYM-049 | A / B | T0 presentation / T1 named basins | FIGROLE002 | 017 |
| CT-SYM-050 | \JI,\JC,\Cmax,\Phistar,\seddto (macros) | T0 presentation aliases | INLINE023 | 008,009,016,019 |
| CT-SYM-051 | 0 / 1 / \infty | T0 constants/limit notation | EQF006/010/011/013 | 016,017,019 |
| CT-SYM-052 | J (language label) | non-theory documentary label | S10:18 Japanese-original column, not flow | — |
| CT-SYM-053 | \Delta | T0/T2 input | TRANS015;MECHLANG015 | 011 |

prose-only/geometry objectの補完: CT-OBJ-001(position)→FIGROLE001; 007(gradient)→THOUGHT004; 017/023/024/030(concept/depth-width-curvature/category/distance)→CONCEPTROLE001–010・IDREL014/024; 026(limit cycle)→THOUGHT006; 027(insight)→INSIGHTROLE; 029(projection/window)→SCOPE001・XROLE001; 032(meaning)→MEANING全行。32 OBJを新定義せずrole locatorへ対応づける。

## 6. Role conflations

HIGH=同じ語/式から別層の説明・機構へ強いis/ensures/reflectionを経て移る。MEDIUM=local namingと説明的使用の境界に注意。LOW=明示Definition/analogy/negative scopeが役割を区別し、定義だけではconflationとしない対照。UNRESOLVED=異なるroleの読み分け自体が未固定。
これはcandidate ledger（低risk対照を含む）であり成立した誤謬の件数ではない。

| CT-CONFL | Candidate / contrast | Source | Grade | Reason and preserved weak reading |
| --- | --- | --- | --- | --- |
| CT-CONFL-001 | Phi is conceptual landscape | S04:58–60 vs S03:92–93 | MEDIUM | T0/T1 local namingは明示。後のexperience attributionまで同じstatementが担うように読める点のみ候補 |
| CT-CONFL-002 | concept basin definition alone | S05:126–135;S11:49–52 | LOW | D0/D1の限定は明示、individuation未指定も明記。局所定義それ自体はconflation認定しない |
| CT-CONFL-003 | concept geometry explains semantic/cognitive attributes | S06:35–64 | MEDIUM | 幅/曲率/境界が文脈・precision・semantic driftの説明を担う移行 |
| CT-CONFL-004 | understanding threshold vs felt understanding | S05:138–152;S03:18–20;S10:28/51–53 | HIGH | Definitionとsubjective easeのcorrespondenceが同じunderstanding語を使う。閾値判定と感覚の判定を分離して記録する監査箇所 |
| CT-CONFL-005 | meaning = available trajectories | S03:60–65;S04:110;S09:15–16 | MEDIUM | primitive否定とframework内命名は両立し得る。軌跡集合の命名が意味説明として使われる場合を候補化 |
| CT-CONFL-006 | J_I field / trajectory / thought | S04:64–66;S02:81–83;FIG001 | HIGH | 同じJ_Iにfieldとtrajectoryとcognitive thoughtを圧縮。thought content exclusionは別途保持 |
| CT-CONFL-007 | tau formal / experiential time | S04:76–78;EQF002/010 | HIGH | tableでirreversible orderingとexperiential timeが同一行、区別するrole文が同所にない |
| CT-CONFL-008 | insight / bifurcation / suddenness | S07:69–79 | HIGH | correspondence、is a bifurcation、subjective reflectionが一段落群に連続 |
| CT-CONFL-009 | token coupling as cognitive mechanism | S05:54–92;S07:24–31 | HIGH | term提示→each reuse reinforces / ensures learningという説明的使用、numeric signatureとは別問題 |
| CT-CONFL-010 | meaning-neutral token | S04:106–119;S05:89–92 | LOW | intrinsic meaning否定とfieldへの作用は異なる主張。作用するだけでsemantic contentを持つとは読まない |
| CT-CONFL-011 | Phi* target / history-shaped terrain | S05:114–122 | UNRESOLVED | long-time targetと変形を続けるmemory-like構造のrole差。数学矛盾とは判定しない |
| CT-CONFL-012 | positivity → conceptual openness | S05:168–185;JA280–284 | MEDIUM | ENはconditional/generic guardを置く。formal positivityからlearning opennessへの役割の拡張を保持 |
| CT-CONFL-013 | barrier → conceptual prohibition | S05:46–50;JA191/236/374 | MEDIUM | EN effective guard、JA hard/prohibitionの差。主にversion/read-as問題 |
| CT-CONFL-014 | individual → collective same dynamics | S08:18–46;S11:55–58 | HIGH | same dynamicsで尺度を移すがformal treatment futureとの記述もある |
| CT-CONFL-015 | norms / institutions = attractors | S08:56–66 | HIGH | correspondenceからare/follows fromへ、semantic namingが制度安定の説明に移る |
| CT-CONFL-016 | intelligence = shared maintenance | S08:70–81;S12:48–49 | MEDIUM | 社会scale内のfunctional definitionはある。一般intelligenceへの拡張と区別 |
| CT-CONFL-017 | physical particle / concept | S12:66–71;JA576 | MEDIUM | EN nonidentity guard付きgrammar比較、JA同一equation解クラス。typed relationの認定ではない |
| CT-CONFL-018 | projection / nonredefinition | S00:86–96;README | LOW | 明示projected-use scope。scope文それ自体はderived semantic mechanismではない |
| CT-CONFL-019 | Q quantization name | S04:94–101;JA193 | LOW | analogyを明示してquantum theory claimを否定。isomorphic語はIDRELで別記 |
| CT-CONFL-020 | vocabulary set vs distribution | S06:69–82 | MEDIUM | T0 set selectionとT1 vocabulary distributionの役割を同じVに置く; formal-role conflictとして別記 |

## 7. Definition vs interpretation

D0 formal definition、D1 representational naming、D2 semantic interpretation、D3 cognitive interpretation、D4 phenomenal interpretation、D5 mixed/unclear。複数付与可。
「結果扱い」はsourceの修辞的使用を示し、本監査の数学的認定ではない。

| DEFROLE | Phase01 DEF | Object | Class | Source | Later result-like use / boundary |
| --- | --- | --- | --- | --- | --- |
| CT-DEFROLE-001 | CT-DEF-001 | concept | D0/D1 | S05:126–135 | S06:10–13/35–64;S12:23–27でstructural results/attribute説明へ。局所Definitionと区別 |
| CT-DEFROLE-002 | CT-DEF-002 | meaning | D2 (JA D4併記) | S03:64–65;JA141;S09:15–16 | S10:48–50はinterpretationと明記。semantic ontologyの定義とはしない |
| CT-DEFROLE-003 | CT-DEF-003 | understanding | D0/D3; S10 D4 | S05:138–152 | S10:28/51–53でfelt easeへ対応; formal resultへの無言転用候補 |
| CT-DEFROLE-004 | CT-DEF-004 | insight | D3/D4 | S07:69–79 | Definition environmentなし。bifurcation表現をtheoremと数えない |
| CT-DEFROLE-005 | CT-DEF-005 | thought | D3 | S02:81–83;S04:64–66 | S06 limit-cycle解クラスへ。flow/trajectory/contentを分離 |
| CT-DEFROLE-006 | CT-DEF-006 | intelligence | D3 | S08:70–81 | S12:48–49の結果要約。社会scale指定は保持 |
| CT-DEFROLE-007 | CT-DEF-007 | category boundary | D1/D2 | S06:53–64 | mechanistic account of semantic driftへ使用 |
| CT-DEFROLE-008 | CT-DEF-008 | vocabulary | D0/D1; D5 set/distribution | S06:69–82 | formal setをdistributionと呼ぶ、同じsignature認定はしない |
| CT-DEFROLE-009 | CT-DEF-009 | topology | D1/D3/D4 | S07:49–79 | merge/split描像からconceptual change/insightへ |
| CT-DEFROLE-010 | CT-DEF-010 | projection | D1 (scope) | S00:94–96;S04:16–18 | S11 grounding比較があるが新operator definitionにはしない |
| CT-DEFROLE-011 | CT-DEF-011 | observation window | D1 (scope) | S00:94–96;S05:36–39 | positivity再活性化の条件に使う、extraction rule未記載 |
| CT-DEFROLE-012 | CT-DEF-012 | token | D1/D3 | S04:79–83;S05:74–85 | Q output/field operator/dot operand/reuse role; D5境界あり |
| CT-DEFROLE-013 | CT-DEF-013 | Phi | D0/D1; D2/D4 elsewhere | S04:33–40/58–60 | S03:92 experiences reflect、negative meaning guardも保持 |
| CT-DEFROLE-014 | CT-DEF-014 | Phi* | D1/D2; D5 limit/history | S05:114–122 | formal targetとhistory-shaped terrainを並置 |
| CT-DEFROLE-015 | CT-DEF-015 | Q constraints | D5 | S01:21;S04:79/94–101 | named extraction/analogy; complete formal definition扱いしない |
| CT-DEFROLE-016 | CT-DEF-016 | calR/metric/path | D1; undefined metric | S05:138–150 | regionのみ。path gammaやscalar cost Rは導入しない |
| CT-DEFROLE-017 | CT-DEF-017 | tau | D4 + T0 ordering usage | S04:76–78;S05:11/114 | formal resultと体験時間の同一性は未認定 |
| CT-DEFROLE-018 | CT-DEF-018 | collective Phi | D2/D3; D5 aggregate | S08:42–81 | S11:55–58 future formal treatmentと併記 |

## 8. Concept roles

| CT-CONCEPTROLE | Role | Source | Layers / distinction |
| --- | --- | --- | --- |
| CT-CONCEPTROLE-001 | basin/valley | S03:54–65;JA135–141 | T0→T1, picture and local naming |
| CT-CONCEPTROLE-002 | locally stable region | S05:126–135;JA261 | T0→T1 explicit Definition |
| CT-CONCEPTROLE-003 | low-gradient predicate | EQF011;S06:22–23 | T0 predicate, not entire concept object |
| CT-CONCEPTROLE-004 | perturbation stability | EQF011;S11:49–52 | T0 criterion→T1 concept; individuation scope remains |
| CT-CONCEPTROLE-005 | semantic category | S06:39–64 | T1 contextual range/precision/category edge |
| CT-CONCEPTROLE-006 | cognitive object/belief | S06:23/35–44;S07:31 | T2 entrenched belief/learning result |
| CT-CONCEPTROLE-007 | token-addressable recurrence | S05:54–85;JA87 | T2 reuse; JA概念再定義の再入可能性を明示、concept=tokenとしない |
| CT-CONCEPTROLE-008 | social/shared attractor | S08:56–60 | T1 shared concepts → T2 institutional roles |
| CT-CONCEPTROLE-009 | solution class | S06:10–26;JA292–301 | T0 named solutions assigned cognitive interpretations |
| CT-CONCEPTROLE-010 | nonindividuated cluster | S11:49–52 | T1 concept vs related cluster; source自身の未指定scope |

## 9. Meaning roles

| CT-MEANING | Use | Source wording / locator | Role / strength |
| --- | --- | --- | --- |
| CT-MEANING-001 | intrinsic token meaning denied | S04:115–116;S05:89;JA202/247 | T1 primitive否定; field作用否定ではない |
| CT-MEANING-002 | meaning transfer denied | S03:69–80;JA145–148 | T1 transmission否定→T2 communication mechanism wording |
| CT-MEANING-003 | valley does not contain meaning | S03:60–65 | T0 attractorと意味容器を区別 |
| CT-MEANING-004 | available trajectories called meaning | S03:64–65 | T0→T1; framework-local is wording |
| CT-MEANING-005 | experienced meaning interpreted downstream | JA141 | T1/T3; ENよりinterpretiveだが経験roleを明示 |
| CT-MEANING-006 | Phi not meaning field | S04:110–112;JA200 | T0 potential nonidentity guard |
| CT-MEANING-007 | semantic drift | S06:58–64;JA320–322 | T1 distinction changes→T2 mechanism-language |
| CT-MEANING-008 | semantic theory excluded | S09:12–16;JA440 | reference/truth/content scope外、meaning emergent label |
| CT-MEANING-009 | note meaning ↔ depth | S10:48–50;JA501 | correspondence/interpretation, not definition |
| CT-MEANING-010 | meaning vs epistemic understanding | S02:78–79;S12:29–31 | T2 understanding not correct-meaning acquisition |
| CT-MEANING-011 | semantic importance vs frequency | S06:79–82;JA333–335 | frequency reflects accessibility not importance |
| CT-MEANING-012 | distributional semantics comparison | S11:20–28;JA525–528 | co-occurrence geometry vs use-history geometry; no metric identity |
| CT-MEANING-013 | no semantic primitives in central result | S12:12–18;JA556–557 | negative scope coexists with emergence language |

## 10. Thought / flow roles

| CT-THOUGHT | Role | Source | Boundary |
| --- | --- | --- | --- |
| CT-THOUGHT-001 | formal flow field | EQF003;S04:64 | T0; divergence/gradient syntax, signature Phase01 |
| CT-THOUGHT-002 | trajectory field label | S04:64–66 | T0/T2; field and path wording not identical types by audit |
| CT-THOUGHT-003 | thought trajectory definition | S02:81–83;S01:31–32 | T0→T2 is; no directing subject required |
| CT-THOUGHT-004 | movement along downhill gradient | S03:46–50 | T0 path picture→T2 thought movement |
| CT-THOUGHT-005 | thought content denied | S04:113–114 | J_I direction≠experienced content |
| CT-THOUGHT-006 | recurrent thought / inference-like movement | S06:24;S10:29 | limit-cycle → habitual thought; no dedicated inference operator |
| CT-THOUGHT-007 | search/integration/transmission | FIG003 | T2 image labels on bare J; not separate body equations |
| CT-THOUGHT-008 | cognitive block / repetition | S06:25;S09:35–46 | T0 flow terrain→T2 blocked/unstable thought |
| CT-THOUGHT-009 | non-deliberate thought ease | S03:13–28/84–93 | T2 movement vs T3 felt ease; not autonomous subject derivation |

## 11. Understanding roles

| CT-UNDERROLE | Element | Source | Role separation |
| --- | --- | --- | --- |
| CT-UNDERROLE-001 | regional integral | EQF012 | T0 expression; calR region not scalar R |
| CT-UNDERROLE-002 | system-dependent threshold | S05:146–150 | T0 condition; no new experience threshold |
| CT-UNDERROLE-003 | low traversal cost | S05:138–145;S03:49–50 | T0 cost → T2 entry/reentry |
| CT-UNDERROLE-004 | understanding Definition | S05:138–152 | D0/D3; conditional dynamics, not correct semantic answer |
| CT-UNDERROLE-005 | nonbinary entry/exit | S05:151–152 | T2 condition changes with Phi; not phenomenal scoring |
| CT-UNDERROLE-006 | felt ease example | S03:18–28;JA121–126 | T2 movement→T3 experience of understanding |
| CT-UNDERROLE-007 | note formal correspondence | S10:28/51–53 | T0 integral→T3 sense; source labels interpretation |
| CT-UNDERROLE-008 | sudden arrival | S03:87–93 | T3 experienced onset; not inferred from threshold alone |
| CT-UNDERROLE-009 | durable understanding / failure | S09:40–46 | T2 formation/stabilization role |
| CT-UNDERROLE-010 | summary non-epistemic guard | S12:29–31 | definition scope retained, not epistemic achievement |

## 12. Insight roles

| CT-INSIGHTROLE | Element | Source | Role |
| --- | --- | --- | --- |
| CT-INSIGHTROLE-001 | merger/split/displacement | S07:49–53 | T0 topology depiction→T1 change in meaning/scope |
| CT-INSIGHTROLE-002 | rapid change | S07:67–74 | T0 event→T2 insight heading |
| CT-INSIGHTROLE-003 | bifurcation | S07:72–74 | formal-language identification; no new formal model supplied here |
| CT-INSIGHTROLE-004 | threshold crossing | S07:76–79 | T0 threshold metaphor/formal-role description vs perceptual threshold |
| CT-INSIGHTROLE-005 | cognitive resolution / connection | S07:69–71 | T2 problem/idea relation |
| CT-INSIGHTROLE-006 | subjective suddenness | S07:69–79;JA379–382 | T3 explicit reflects/corresponds |
| CT-INSIGHTROLE-007 | natural sudden understanding | S03:87–93 | T3 experience attached to uninspected geometry |
| CT-INSIGHTROLE-008 | Con qualia comparison locator | Phase00 CON-XDEP008;Con correspondence map | CT source says insight, not qualia identity; reverse reference separate |

## 13. Time roles

| CT-TIMEROLE | Use | Source | Layer / collapse check |
| --- | --- | --- | --- |
| CT-TIMEROLE-001 | evolution argument | S04:14/20 | T0 field parameter; time role not seconds |
| CT-TIMEROLE-002 | derivative parameter | EQF002 | T0 partial_tau; no experienced-time equation |
| CT-TIMEROLE-003 | long-time limit | EQF010 | T0 order endpoint |
| CT-TIMEROLE-004 | irreversible ordering | S04:78;S05:109;FIG003 | T0 loop/order description, not automatic subjective duration |
| CT-TIMEROLE-005 | conceptual development | S04:76–78 | T2 sequence + T3 experiential time in same table row |
| CT-TIMEROLE-006 | experiential time | S04:77;JA188 | explicit T0→T3 naming, major candidate |
| CT-TIMEROLE-007 | suddenness / perceptual threshold | S07:76–79 | T3 timing description; no tau equality stated |
| CT-TIMEROLE-008 | social/history order | S08:51–52/78–81 | T2 collective prior/subsequent history; common tau not specified |
| CT-TIMEROLE-009 | Con internal delay comparison | Phase00 GLYPH004;Con log loop:61 | distinct source tau; no equality inferred |

## 14. Token roles

| CT-TOKENROLE | Use | Source | Role boundary |
| --- | --- | --- | --- |
| CT-TOKENROLE-001 | discrete token/symbol | S05:74–80 | T0/T1 representation, natural-language scope not exclusive |
| CT-TOKENROLE-002 | re-addressable unit | S05:54–58 | T2 recursion function assigned |
| CT-TOKENROLE-003 | Q output | S04:79–83 | T0 extraction notation; Q undefined constraints retained |
| CT-TOKENROLE-004 | operator on Phi | S04:83 | T0 operator-role name, not automatic numeric vector |
| CT-TOKENROLE-005 | dot-product operand | EQF009 | T0 expression role; no well-typedness judgment |
| CT-TOKENROLE-006 | meaning-neutral primitive | S04:115–116 | T1 content denied, not cognition denied |
| CT-TOKENROLE-007 | reuse event | S05:89–92;S07:20–31 | T2 activity→field change wording |
| CT-TOKENROLE-008 | internal control vs social anchor | S08:13–38 | T2 function changes, source says no property changed |
| CT-TOKENROLE-009 | vocabulary membership | EQF014;S06:76–82 | T1 stability selection; not semantic importance |

## 15. Coupling mechanism language

| CT-MECH | Claim / locator | Classification | Explicit intermediary / role |
| --- | --- | --- | --- |
| CT-MECH-001 | lambda sum term,EQF009 | mathematical term | T0; dot-product signature remains Phase01 question |
| CT-MECH-002 | local coupling mechanism,S05:58–60 | formal interpretation | figure illustrating T0/T2 claim |
| CT-MECH-003 | cannot sustain / requires discrete units,S05:54–58 | causal mechanism wording | T0 continuous/discrete distinction → T2 recursion |
| CT-MECH-004 | purely dynamical,S05:89–90 | formal interpretation | excludes encoded meaning but asserts field bias |
| CT-MECH-005 | each reuse reinforces gradient,S05:91–92 | causal mechanism wording | reuse→gradient intermediary named, no role translation supplied |
| CT-MECH-006 | deepens basin,S05:68/92 | causal mechanism wording | gradient/well used as T0/T1 intermediary |
| CT-MECH-007 | lowers traversal cost,S05:68;FIG002 | illustrative claim | T0 cost→T2 later traversal |
| CT-MECH-008 | coupling ensures each reuse deepens,S07:24–25 | causal mechanism wording | EQF009 explicitly cited as warrant; validity not assessed |
| CT-MECH-009 | self-sustaining concept,S07:27–31 | causal mechanism wording | well/cost/attractor sequence → learning |
| CT-MECH-010 | semantic drift,S06:58–64 | causal mechanism wording | ridge reinforcement/erosion → T1/T2 change |
| CT-MECH-011 | temporal sequence vs update law,S05:89–92;S07:10–31 | unresolved | per-reuse cognitive event and formal evolution roles not typed by this audit |

## 16. Positivity roles

| CT-POSROLE | Use | Source | Role / ENJA boundary |
| --- | --- | --- | --- |
| CT-POSROLE-001 | formal positivity | EQF013 EN/JA | T0 quantified statement only |
| CT-POSROLE-002 | nonclosure premise | S05:162–168;JA278 | T0 closure bound→conceptual exclusion |
| CT-POSROLE-003 | conceptual closure excluded | S05:168–177 | T0→T1 under-framework proposition |
| CT-POSROLE-004 | nonzero-gradient qualification | S04:28–30;S05:169–177 | EN conditional/generic, explicitly not pointwise implication |
| CT-POSROLE-005 | available flow directions | S05:171–173 | T0 directions named; not automatically thought occurring |
| CT-POSROLE-006 | local quiescence retained | S05:182–185;S12:40–42 | EN stable attractor not always nonzero local gradient |
| CT-POSROLE-007 | future differentiation | S08:83–88 | T1 open landscape→T2 innovation, conditional wording |
| CT-POSROLE-008 | JA generic implication | JA280 | T0 I>0 / gradPhi!=0 / J_I!=0 prose chain kept separate |
| CT-POSROLE-009 | JA always-gradient summaries | JA41/95/167/284/430/567 | stronger T1/T2 continued availability, not EN correction |
| CT-POSROLE-010 | no phenomenal inference added | S05:180–185 | intelligence/understanding implications not claim of T3 from positivity |

## 17. Barrier roles

| CT-BARRIER | Use | Source | Role distinction |
| --- | --- | --- | --- |
| CT-BARRIER-001 | reciprocal term | EQF008 | T0 boundary-dependent expression; no divergence proof assessed |
| CT-BARRIER-002 | effective saturation vs ideal limit | S05:36–39 | C_* vs Cmax; T0/T1 |
| CT-BARRIER-003 | projected resistance | S05:46–50 | T0→T2 effective analogue, explicitly not fundamental prohibition |
| CT-BARRIER-004 | belief revision resistance | S07:55–65 | T2 accounts-for language despite effective qualifier |
| CT-BARRIER-005 | overclosure pathology | S09:31–38 | T0 relative terms→T2 repetitive thought/rigidity |
| CT-BARRIER-006 | JA hard bound | JA191 | T0 boundary→structural exclusion label |
| CT-BARRIER-007 | JA prohibition execution | JA236 | stronger T1/T2 role than EN effective resistance |
| CT-BARRIER-008 | JA divergence / costly change | JA373–375 | T0 divergence wording → T2 belief resistance, no ENJA reconciliation |

## 18. Asymptotic roles

| CT-ASYMROLE | Use | Source | Role distinction |
| --- | --- | --- | --- |
| CT-ASYMROLE-001 | formal long-time target | EQF010 | T0 Phi*; no cognitive property inferred from arrow |
| CT-ASYMROLE-002 | attractor naming | S05:96–97/119 | T0 dynamical label |
| CT-ASYMROLE-003 | mature conceptual landscape | S04:84–86;S05:119 | T1 naming of target |
| CT-ASYMROLE-004 | history/learning sedimentation | S05:120–122;S07:10–31 | T2 interactions/maturation |
| CT-ASYMROLE-005 | memory-like persistence/recall | S07:35–45 | T2 forgetting/redeepening; not new memory variable |
| CT-ASYMROLE-006 | nonunique/nonstatic qualification | S05:120–122;JA256 | limit-object vs changing terrain roles, consistency undecided |
| CT-ASYMROLE-007 | concept topology continues changing | S07:49–53 | T1 meaning/scope evolution of Phi* |
| CT-ASYMROLE-008 | social Phi* | S10:33;JA493 | T1/T2 cross-agent maintenance, no shared limit rule |
| CT-ASYMROLE-009 | slow structure comparison | Phase00 CON-XDEP006;S10:54–56 | CT does not itself define Con slow-log identity |

## 19. Social / collective roles

| CT-SOCIALROLE | Use | Source | Transition / boundary |
| --- | --- | --- | --- |
| CT-SOCIALROLE-001 | individual field | S08:10–16 | T0 field→T2 recursion/compression |
| CT-SOCIALROLE-002 | same dynamics extension | S08:18–22 | cross-scale reuse, not domain identity established |
| CT-SOCIALROLE-003 | same token properties | S08:37–38 | T2 function inversion vs claimed property invariance |
| CT-SOCIALROLE-004 | correlated wells | S08:42–46 | T0 correlated geometry→T1 shared landscape |
| CT-SOCIALROLE-005 | shared semantic domain | S08:48–52 | T1 distributed terrain; no aggregate Phi definition |
| CT-SOCIALROLE-006 | norms | S08:56–60 | T1 shared stability→T2 social norm role |
| CT-SOCIALROLE-007 | institutions/paradigms | S08:56–66 | correspond→are/follows from; causal role |
| CT-SOCIALROLE-008 | collective intelligence | S08:70–76 | T1 terrain maintenance→T2 functional definition |
| CT-SOCIALROLE-009 | agents as transient operators | S08:78–81 | T2 transmit/reshape via logs, not math operator supplied |
| CT-SOCIALROLE-010 | innovation/noncompletion | S08:83–88;JA430 | positivity roles extended to social change |
| CT-SOCIALROLE-011 | formal treatment future | S11:55–58 | explicit separation: qualitative social description vs future formalization |

## 20. Neural / phenomenal scope

| CT-SCOPE | Guard | Locator | Positive roles coexisting / audit treatment |
| --- | --- | --- | --- |
| CT-SCOPE-001 | semantic interpretation only when stated | S00:91–96;JA19 | permits explicit mappings, does not make them semantic theorems |
| CT-SCOPE-002 | Phi/J_I/token nonidentity | S04:106–119 | geometry/flow/discrete unit distinguished from meaning/content |
| CT-SCOPE-003 | no semantic theory | S09:12–16 | meaning label still appears S03/S10 |
| CT-SCOPE-004 | does not generate or explain subjective experience | S09:18–22;JA442 | T3 time/ease/insight wording remains separately audited |
| CT-SCOPE-005 | conscious access downstream | S09:20–22 | S03 invisible GPU is positive phenomenological account, not neutralized automatically |
| CT-SCOPE-006 | neural abstraction | S09:24–27 | no concrete neural carrier inferred from field language |
| CT-SCOPE-007 | observable correspondence not established in source | S09:59–69 | documentary scope, not Phase02 evidence judgment |
| CT-SCOPE-008 | neural mapping open | S11:60–64 | future firing/connectivity/oscillation correspondences; no new map |
| CT-SCOPE-009 | quantum theory not claimed | S04:94–101 | quantization analogy still uses isomorphic |
| CT-SCOPE-010 | not directing subject | S02:81–83 | negative functional guard, not subject derivation |
| CT-SCOPE-011 | note interpretation not definition | S10:40–44/66–70 | formal referents claimed for phenomenology; boundary retained |
| CT-SCOPE-012 | multi-agent and individuation open | S11:48–58 | does not automatically retract S08 identity/causal wording |

## 21. Mechanism-language inventory

lexical hit数ではなく、同一文脈のEN/JAとsummary反復をまとめたfamily数。mechanisticも検索し、否定文・見出し・upstream背景語をpositive mechanismに数えない。

34は分類済みの総entry数であり、positive mechanism claimsの件数ではない。否定・documentary対照も明示して残す。

| CT-MECHLANG | Source / wording | Target layer | Formal intermediary explicit? / classification |
| --- | --- | --- | --- |
| CT-MECHLANG-001 | S01:18/23/26;JA32–34 generates/deepening/producing | T0→T1/T2 | YES potential/coupling/loop; summary causal wording |
| CT-MECHLANG-002 | S02:40/59;JA67/77 generation | T0 upstream / navigation | VED description/series label, not a CT cognitive mechanism |
| CT-MECHLANG-003 | S02:85–87;S12:33–36;JA93/565 deepening | T1/T2 | YES token-gradient; repeated central claim |
| CT-MECHLANG-004 | S03:74–80;JA145–148 deepens / produces similar shifts | T1→T2 | YES wells/trajectory; communication causal account |
| CT-MECHLANG-005 | S03:84–93;JA150–155 gives rise to / 生む | T3 | Phi named, but no separate phenomenal intermediary in passage |
| CT-MECHLANG-006 | S04:38–40;JA174 produced bias / determines direction | T0/T2 context | YES potential/gradient; formal interpretation |
| CT-MECHLANG-007 | S04:110–112;JA200 determines cheap/costly | T0→T2 | YES constraint geometry; semantic nonidentity guard |
| CT-MECHLANG-008 | S05:20–32;JA220–230 generation term decomposes | T0 | YES explicit source expressions; not itself higher-layer mechanism |
| CT-MECHLANG-009 | S05:58–69;FIG002 illustrates mechanism / reinforces / deepens / lowers | T0→T1/T2 | YES coupling term and schematic; illustrative + causal wording |
| CT-MECHLANG-010 | S05:89–92;JA247–248 purely dynamical / each reuse | T0→T2 | YES term adjacent; no empirical/typing judgment |
| CT-MECHLANG-011 | S05:96–122;JA252–257 approaches / history reshapes | T0→T1/T2 | YES limit/attractor; qualitative evolution language |
| CT-MECHLANG-012 | S01:35;S04:30;S05:170/185 generated field | T0/T1 | field adjective under positivity qualification, not a new mechanism family |
| CT-MECHLANG-013 | S06:43–45;JA311 curvature produces precision/polysemy | T0→T1 | YES curvature named, no separate semantic conversion stated |
| CT-MECHLANG-014 | S06:58–65;JA320–322 reinforces/erodes/mechanistic account | T1/T2 | YES ridge dynamics named; semantic drift causal wording |
| CT-MECHLANG-015 | S07:10–18;JA343–348 generates spike/gradient | T0→T2 | YES Delta/source/I/Phi/J_I sequence |
| CT-MECHLANG-016 | S07:20–25;JA350–352 ensures deepening | T0→T2 | YES EQ coupling explicitly cited; theorem-like warrant use |
| CT-MECHLANG-017 | S07:27–31;JA354–357 deepens/cost decreases/self-sustaining | T1/T2 | YES well/cost/attractor sequence, learning interpretation |
| CT-MECHLANG-018 | S07:35–45;JA361–367 forgetting/re-deepening | T0→T2 | YES Gamma C repeated plus Phi relaxation |
| CT-MECHLANG-019 | S07:55–65;JA373–375 accounts for belief resistance | T0→T2 | YES barrier; EN effective scope vs JA divergence wording |
| CT-MECHLANG-020 | S07:69–79;JA379–382 produce event / subjective reflects | T2/T3 | topology/perceptual thresholds juxtaposed; no separate phenomenal mapping stated |
| CT-MECHLANG-021 | S08:18–38;JA394–405 produces inversion | T2 social | constraint-cost shift named, not new formal operation |
| CT-MECHLANG-022 | S08:42–52;JA408–412 produces correlated deepening/shared terrain | T1/T2 | wells/shared inputs named; aggregate formal treatment deferred |
| CT-MECHLANG-023 | S08:56–66;JA416–420 follows from depth/accounts for history | T2 institutions | attractor depth is named intermediary |
| CT-MECHLANG-024 | S08:74–81;JA426–428 maintenance/transmit | T2 intelligence | landscape/logs named; functional definition/process |
| CT-MECHLANG-025 | S09:18–22;JA442 does not generate/explain + future mechanistic basis | T3 negative scope | exclusion and companion referral, not positive evidence |
| CT-MECHLANG-026 | S09:31–46;JA449–456 can no longer produce / preventing | T2 | source-term dominance→wells→thought/understanding |
| CT-MECHLANG-027 | S09:48–55;JA459–460 fail to produce / result | T1→T2 social | correlated perturbation failure named |
| CT-MECHLANG-028 | S10:21/48–53;JA481/501–502 deepening / correspondence | T1/T2/T3 | Phi/source/cost named; explicit interpretations, not definitions |
| CT-MECHLANG-029 | S11:14–18;JA522 grounding / explicit account | T0→T2 | VED/IFGT source attribution; derivation wording recorded only |
| CT-MECHLANG-030 | S11:20–28;JA525–528 emerges from coupling | T1 geometry | YES coupling vs co-occurrence comparison |
| CT-MECHLANG-031 | S11:30–37;JA530–532 error minimization / generative model | T2 comparison | drive/deepening explicit; Bayesian commitment denied |
| CT-MECHLANG-032 | S12:12–18/61–71;JA556/575–576 emerges / generates / grammar | T0→T1/T2 | field/coupling/source comparison named; physical/concept distinction recorded |
| CT-MECHLANG-033 | JA584/589 英語TeXから生成/反映 | documentary | working source history, not theory mechanism |
| CT-MECHLANG-034 | S01:38–40;S02:93–95;S12:44–49;JA43/97/569 same dynamics produce | T1/T2 social | summary of S08, no separate formal intermediary added |

## 22. Necessity / sufficiency

empirically necessary/sufficientとの認定は全行で行わない。sourceにonly-if/iffがない箇所へ双条件を補わない。

| CT-NS | Source / claim | Model-local? | Formal? | Semantic? | Cognitive? | Phenomenal? |
| --- | --- | --- | --- | --- | --- | --- |
| CT-NS-001 | S00:89–93;JA18–20 approximation only where stated / strict bound always | explicit scope | YES | — | — | — |
| CT-NS-002 | S02:81–83;JA91 thought does not require directing subject | within CT claim | J_I named | — | YES negative necessity | not subject-count criterion |
| CT-NS-003 | S05:54–58;JA240 continuous field cannot sustain low-cost recursion / discrete units required | context CT, sentence categorical | continuous/discrete | — | YES necessity | — |
| CT-NS-004 | S05:55–56 generically expensive/drift-prone | context CT | field reentry | — | YES qualification | — |
| CT-NS-005 | S05:126–135;JA261–265 concept satisfying slope+stability | explicit Definition | YES conditions | YES local concept | attribute uses later | — |
| CT-NS-006 | S05:138–152;JA267–272 understanding threshold | explicit Definition | YES threshold | not correct meaning | YES criterion naming | not direct phenomenal criterion |
| CT-NS-007 | S05:162–164;JA278 positivity follows from C bound/f | under-framework | YES implication wording | closure interpretation | — | — |
| CT-NS-008 | S05:168–177;JA280–284 excludes closure/generically | explicit framework; JA stronger | YES positivity | YES conceptual openness | flow availability | — |
| CT-NS-009 | S04:28–30 not by itself guarantee nonzero local gradient | explicit guard | YES pointwise distinction | — | — | — |
| CT-NS-010 | S03:78–80;JA147 sufficiently similar landscapes for communication | framework picture | similarity named, criterion not supplied | YES shared terrain | YES condition | — |
| CT-NS-011 | S07:24–25;JA352 coupling ensures every reuse deepens | model narrative | EQF009 cited | concept stabilization | YES sufficient-sounding causal assurance | — |
| CT-NS-012 | S07:55–56;JA373 perturbation sufficient to overcome depth required | model narrative | depth/perturbation | concept change | YES required+sufficient magnitude wording | — |
| CT-NS-013 | S07:76–79;JA382 threshold crossing then event | model narrative | topology threshold | — | insight context | YES perceptual threshold/suddenness |
| CT-NS-014 | S08:13–22;JA391–395 must reenter/compress/stabilize shared trajectories | under cost assumptions | continuous/discrete costs | shared representation | YES constraints | — |
| CT-NS-015 | S08:44–46;JA409 sufficiently similar priors and repeated shared perturbation | model narrative | wells named | shared landscape | YES conditional emergence | — |
| CT-NS-016 | S08:62–63;JA419 institutional stability does not require central enforcement; follows depth | context social CT, categorical wording | potential depth | norms | YES necessity denial + grounding | — |
| CT-NS-017 | S08:64–66;JA420 coordinated perturbation sufficient to overcome collective depth required | model narrative | depth/perturbation | social concepts | YES necessity/threshold | — |
| CT-NS-018 | S09:31–46;JA449–456 input can no longer change topology; prevents durable understanding | model failure mode | terms/wells | concept stabilization | YES impossibility/prevention wording | phenomenologically named but not first-person necessity |
| CT-NS-019 | S09:62–66;JA466–467 quantitative predictions require parameters/maps | explicit scope | YES future specification | — | research prerequisite | — |
| CT-NS-020 | S11:49–58;JA541–545 individuation criterion needed / shared-landscape conditions future | explicit open question | YES future criteria | YES individuation | social stability | — |
| CT-NS-021 | S11:61–64;JA548 requires empirical collaboration | methodological | map target named | — | research prerequisite | — |
| CT-NS-022 | S04:118–119;JA205 methodological necessities, not ultimate meaning/experience nature | explicit negative scope | — | YES | YES | YES exclusion |
| CT-NS-023 | S12:17–18;JA557 no semantic primitives/intentional units required | within central model result | field/coupling | YES denied input | intentional-state denial | not phenomenal explanation |
| CT-NS-024 | S08:83–88;JA430 innovation whenever perturbations/windows reactivate vs always gradient | framework | positivity/conditions | open social terrain | YES possibility vs guarantee | — |
| CT-NS-025 | S06:76–77;JA331 S>epsilon vocabulary membership | local definition | YES inequality | YES vocabulary | reuse input | — |
| CT-NS-026 | S09:19–27;JA442–444 no subjective explanation/neural architecture dependence | explicit scope | abstraction | — | neural exclusion | YES negative scope, not impossibility theorem |

## 23. Identity / correspondence wording

| CT-IDREL | Source | Wording / relation | Type | Roles |
| --- | --- | --- | --- | --- |
| CT-IDREL-001 | S02:13–15 | conceptual terrain same object as CT intuitive metaphor | local definition | name alias; not cross-domain identity |
| CT-IDREL-002 | S00:86–96;README;JA15–20 | not redefine / projected realizations | interpretation | upstream T0→cognitive window |
| CT-IDREL-003 | S04:14–25 | I represents tension / corresponds to active regions | correspondence | T0→T1/T2 |
| CT-IDREL-004 | S04:58–60 | Phi: conceptual landscape itself | local definition | T0→T1 naming |
| CT-IDREL-005 | S03:64–65 vs JA141 | meaning is trajectory set / downstream interpretation of experienced meaning | identity wording / interpretation | T0→T1 vs T1/T3 |
| CT-IDREL-006 | S04:110–116;JA200–202 | Phi not meaning / J_I not content / token not meaning unit | interpretation (negative scope) | distinct roles |
| CT-IDREL-007 | S02:74–76;S05:126–135 | concept is stable region, defined by | local definition | T0→T1 |
| CT-IDREL-008 | S02:81–83;S04:64–66 | thought is trajectory / thought as flow | identity wording | T0 field/path→T2 |
| CT-IDREL-009 | S05:138–152;S10:51–53 | understanding is condition / ease corresponds | local definition + correspondence | T0→T2 / T3 use |
| CT-IDREL-010 | S04:76–78 | experiential time / irreversible ordering same row | interpretation | T0/T3 role pairing |
| CT-IDREL-011 | S04:94–101;JA193 | structurally isomorphic; analogy; no quantum claim | analogy + identity wording | continuous/discrete comparison, not mathematical identity certified |
| CT-IDREL-012 | S05:119–122;JA256–257 | Phi* is sedimented landscape / reflects history | local definition / interpretation | T0→T1/T2 |
| CT-IDREL-013 | S06:10–26 | solution classes correspond to cognitive phenomena | correspondence | T0→T2 |
| CT-IDREL-014 | S06:35–45 | depth/width/curvature measures resistance/context/precision | interpretation | T0→T1/T2 |
| CT-IDREL-015 | S06:53–65 | ridges correspond to boundaries; mechanistic account | correspondence + explanation wording | T0→T1→T2 |
| CT-IDREL-016 | S06:69–82 | vocabulary not list but distribution; set display | local definition / unclear | T0 set/T1 distribution |
| CT-IDREL-017 | S07:35–45 | forgetting corresponds to relaxation; remembering to redeepening | correspondence | T0→T2 |
| CT-IDREL-018 | S07:49–79 | concept change/insight corresponds; this is bifurcation | correspondence + identity wording | T0→T1/T2/T3 |
| CT-IDREL-019 | S08:18–38 | same dynamics / no property changed | identity wording | individual/social scale |
| CT-IDREL-020 | S08:56–66 | norms/institutions correspond then are attractor regions | correspondence + identity wording | T1→T2 |
| CT-IDREL-021 | S08:70–81 | Intelligence is distributed maintenance | local definition / interpretation | T1 terrain→T2 social function |
| CT-IDREL-022 | S09:15–22 | meaning emergent label; conscious access downstream | interpretation | semantic/phenomenal scope |
| CT-IDREL-023 | S10:40–44/61–70 | interpretations rather than definitions / theoretical basis | correspondence + derivation-like authority wording | note exposition axis not T-layer proof |
| CT-IDREL-024 | S11:20–28 | structurally related to distributional semantics; fundamentally differs | analogy | two geometry roles not merged |
| CT-IDREL-025 | S11:33–37 | drive corresponds to error influx / deepening can be understood as minimization | correspondence | T0→T2 comparison |
| CT-IDREL-026 | S12:61–71 | same field / same generative grammar, not identical entities | analogy + identity wording with guard | T0 physical/projected conceptual |
| CT-IDREL-027 | JA575–576 | 同じ情報場 / 同一基礎方程式の解クラス | identity wording | stronger cross-domain formal identity language |
| CT-IDREL-028 | S02:105–106;JA104 | derives core equations / 導出 | derivation wording | source navigation claim, not audited derivation |
| CT-IDREL-029 | S01:9–12;S03:84–93 | not conscious inspection / experiences reflect geometry | interpretation / explanation wording | T1/T0→T3 |
| CT-IDREL-030 | S05:162–177;JA280 | follows from / generic implication | derivation wording | T0 positivity→conceptual closure |
| CT-IDREL-031 | S11:14–18;JA522 | grounding substrate / 最小公理から導出 | derivation wording | upstream T0→CT attractor account |
| CT-IDREL-032 | S10:54–56;JA503 | CPU/GPU corresponds to fast/slow to be formalized | correspondence / future | CT note-role→Con cognitive architecture |

## 24. Cross-scale roles

| CT-XROLE | Relation / source | Roles on both sides | Source direction / guard |
| --- | --- | --- | --- |
| CT-XROLE-001 | VED/IFGT→CT,S00:83–96;S04:14–18 | upstream formal T0 → CT T0/T1/T2 | projected reuse; no typed inheritance decision |
| CT-XROLE-002 | scalar C vs upstream node closure,Phase01 GLYPH006 | T0 upstream / CT T0 with T1 fixation | glyph reuse, no new aggregation |
| CT-XROLE-003 | physical particle ↔ concept,S12:66–71;JA576 | physical formal regime T0 ↔ T1 concept | EN projected nonidentity; JA same-equation wording |
| CT-XROLE-004 | individual↔collective,S08:18–52 | T0 individual field + T2 recursion ↔ T1 shared terrain + T2 synchronization | same dynamics claim; formal treatment deferred S11 |
| CT-XROLE-005 | Q↔quantization,S04:94–101 | continuous/discrete T0 ↔ physical quantization analogy | isomorphic name with explicit theory-claim denial |
| CT-XROLE-006 | CT invisible GPU↔Con note,S10:54–56 | CT T0 geometry / T2 bias / T3 access ↔ Con future fast/slow T2 | CT text refers to note/future paper, not current validation |
| CT-XROLE-007 | Con TCA/terrain/gradient→CT,Phase00 CON-XDEP005–007 | Con T0/T2 interpretations ↔ CT T0 coupling/Phi* | reverse comparison; no TCA claim imported into CT |
| CT-XROLE-008 | Con qualia↔CT insight,Phase00 CON-XDEP008 | Con T3 frontier ↔ CT T0 topology / T2 insight / T3 suddenness | CT does not name qualia here; current Con comparison no identity |
| CT-XROLE-009 | CT→future Intelligence,S02:63;S05:180–182 | CT conceptual nonclosure T1 ↔ future intelligence T2 | navigation/implication, no derivation inferred |
| CT-XROLE-010 | Intelligence→CT,Int2 JA appendix B:21–26 | formal inference/attractor T0/T2 ↔ CT concept/boundary T1 | downstream homology comparison, not CT support |
| CT-XROLE-011 | note L3/L1,S10:59–70 | formal discourse T0 ↔ intuitive/phenomenological descriptions T1/T2/T3 | exposition layers not audit layers |
| CT-XROLE-012 | distributional semantics / predictive processing,S11:20–37 | T1 geometric representation / T2 prediction ↔ CT field roles | comparison not empirical role certification |

## 25. Figure-role audit

§24の逆方向referenceは[Con CT map](../../consciousness/sections/correspondence_map.tex)、[Con log dynamics](../../consciousness/sections/dynamics_log_referencing.tex)、[Int2 JA appendix B](../../intelligence-part2/appendices/appendix_b_homology_ja.tex)を参照。CT本文への新しいrole付与の根拠にはしない。

3 PNGsを本Phaseで再度view_imageで視認。図を証拠/実行例として扱わず、T3が明示されないfigure labelに経験を足さない。

FIG001: [potential geometry](../../conceptual-topography/figures/fig1_potential_geometry.png)、FIG002: [token-field coupling](../../conceptual-topography/figures/fig2_token_field_coupling.png)、FIG003: [minimal recursive loop](../../conceptual-topography/figures/fig3_minimal_recursive_loop.png)。

| CT-FIGROLE | Figure / major label | Layers | Body comparison / compression |
| --- | --- | --- | --- |
| CT-FIGROLE-001 | FIG001 Phi(x,tau),x1,x2,gradient | T0 | no metric/consciousness variable added |
| CT-FIGROLE-002 | FIG001 concept basin A/B and gradPhi≈0 | T0/T1 | caption corresponds; image condenses full perturbation-stability definition |
| CT-FIGROLE-003 | FIG001 conceptual boundary ridge | T0/T1 | S06 explicitly extended high-cost region, label compressed |
| CT-FIGROLE-004 | FIG001 thought trajectory J_I | T0/T2 | caption represented as; graphic labels J_I on path, field/path distinction omitted visually |
| CT-FIGROLE-005 | FIG002 ell_i meaning-neutral discrete token | T0/T1 (negative meaning) | matches S05 token scope |
| CT-FIGROLE-006 | FIG002 -gradPhi weak/reinforced and J_I arrows | T0/T2 context | formal direction and functional response visually paired |
| CT-FIGROLE-007 | FIG002 before/after repeated reuse, deepened basin | T0/T1/T2 | causal sequence mirrors strong body coupling prose |
| CT-FIGROLE-008 | FIG002 lower traversal cost / more easily attracted | T0/T2 | no threshold/felt-understanding label; do not infer T3 |
| CT-FIGROLE-009 | FIG002 lambda sum term | T0 with T2 nearby | no typed token-vector map supplied by image |
| CT-FIGROLE-010 | FIG003 Delta residual and C fixation/structure formation | T0/T1 | formal/cognitive vocabulary in same nodes |
| CT-FIGROLE-011 | FIG003 I density accumulation | T0 | no new cognitive quantity from dots |
| CT-FIGROLE-012 | FIG003 Phi concept attractors | T0/T1 | potential formation / semantic labeling compressed |
| CT-FIGROLE-013 | FIG003 bare J search/integration/transmission | T0/T2 | figure gives broader process labels; caption J_I and README naming retained |
| CT-FIGROLE-014 | FIG003 tau / unidirectional causality / full loop | T0 order/causal diagram | no explicit T3 experiential label; do not transfer T3 from table automatically |

## 26. EN / JA role differences

| CT-ROLEVAR | Topic / locators | Classification | Role-strength difference |
| --- | --- | --- | --- |
| CT-ROLEVAR-001 | positivity pointwise guard,S04:26–30 vs JA167 | JA STRONGER | EN not guarantee local gradient; JAいかなる領域も不活性にならない |
| CT-ROLEVAR-002 | positivity proposition,S05:168–185 vs JA280–284 | JA STRONGER | EN conditional/generic + quiescent states; JA generic implication and all attractors residual gradients |
| CT-ROLEVAR-003 | social positivity,S08:83–88 vs JA430 | JA STRONGER | conditional reactivation vs always generative gradient |
| CT-ROLEVAR-004 | Cmax,S04:87–89 vs JA191 | JA STRONGER | ideal representation/not ordinary state vs hard upper bound / exclusion |
| CT-ROLEVAR-005 | barrier,S05:46–50;S07:57–65 vs JA236/374 | JA STRONGER | effective analogue vs structural prohibition/divergence role |
| CT-ROLEVAR-006 | C_* distinction,S05:36–39 vs JA226–230 | VERSION UNCLEAR | formula both, EN effective saturation prose only |
| CT-ROLEVAR-007 | meaning,S03:64–65 vs JA141 | DIFFERENT ROLE | EN is trajectory set; JA experienced meaning downstream interpretation (identity weaker, T3 more explicit) |
| CT-ROLEVAR-008 | negative meaning scope,S04:110–119 vs JA200–205 | SAME STRENGTH | Phi not meaning field/token not meaning unit |
| CT-ROLEVAR-009 | concept definition,S02:74–76 vs JA87 | DIFFERENT ROLE | JA explicit redefinition by recursive reentry; same core slope/stability formula |
| CT-ROLEVAR-010 | understanding,S05:138–152 vs JA267–272 | SAME STRENGTH | local threshold definition and nonbinary dynamics |
| CT-ROLEVAR-011 | experiential time,S04:76–78 vs JA188 | SAME STRENGTH | T0/T3 table pairing retained |
| CT-ROLEVAR-012 | insight,S07:69–79 vs JA379–382 | SAME STRENGTH | bifurcation/correspondence and subjective suddenness |
| CT-ROLEVAR-013 | Phi* qualification,S05:120–122 vs JA257 | JA STRONGER | not necessarily unique/static vs categorical neither unique nor static |
| CT-ROLEVAR-014 | same dynamics,S08:18–38 vs JA394–405 | SAME STRENGTH | individual/social reuse and no token property change |
| CT-ROLEVAR-015 | collective intelligence,S08:70–81 vs JA424–428 | SAME STRENGTH | social scale functional definition |
| CT-ROLEVAR-016 | concept/particle,S12:66–71 vs JA575–576 | JA STRONGER | same equation solution class vs guarded projected same grammar |
| CT-ROLEVAR-017 | neural/phenomenal scope,S09:18–27 vs JA442–444 | SAME STRENGTH | negative scope both, not cancellation of positive T3 language |
| CT-ROLEVAR-018 | note correspondence,S10:40–70 vs JA498–512 | SAME STRENGTH | interpretation vs definition and theoretical-basis wording |
| CT-ROLEVAR-019 | underclosure title,S09:40–46 vs JA453–456 | VERSION UNCLEAR | underclosure/過開放; same shallow-well cognitive effects |
| CT-ROLEVAR-020 | solution classes,S06:10–13 vs JA292 | JA STRONGER | EN detailed analysis deferred sentence absent in JA subsection; table role same |
| CT-ROLEVAR-021 | grounding,S11:14–18 vs JA522 | JA STRONGER | EN effective IFGT conventions vs JA minimal-axiom derived substrate |

## 27. Role conflicts

| CT-ROLECONFLICT | Role tension / source | Class | What is and is not fixed |
| --- | --- | --- | --- |
| CT-ROLECONFLICT-001 | Phi not meaning field / meaning called trajectories,S04:110;S03:64–65;S09:15–16 | semantic | primitive vs emergent label can differ; no contradiction verdict |
| CT-ROLECONFLICT-002 | flow field / path / thought,S04:64–66;S02:81;FIG001 | formal-role | type role compression, not proven type error |
| CT-ROLECONFLICT-003 | tau derivative / experiential time,S04:76–78;EQF002 | formal-role | different explanatory roles; equality not resolved |
| CT-ROLECONFLICT-004 | token neutral unit / numerical operand / cognitive operation,S04:79–83;EQF009 | formal-role | semantic neutrality does not entail inability to act |
| CT-ROLECONFLICT-005 | Phi* limit / continued change,S05:114–122 | formal-role | target and evolving terrain roles juxtaposed, no convergence judgment |
| CT-ROLECONFLICT-006 | vocabulary set / distribution,S06:69–82 | formal-role | selection object vs organization metaphor unresolved |
| CT-ROLECONFLICT-007 | collective same dynamics / future formal treatment,S08:18;S11:55–58 | cross-scale | source itself separates qualitative description and future formalization |
| CT-ROLECONFLICT-008 | understanding definition / felt ease,S05:138–152;S10:28 | semantic | cognitive criterion vs subjective correspondence |
| CT-ROLECONFLICT-009 | no subjective explanation / insight accounts,S09:19;S03:87;S07:76 | unresolved | negative scope and positive T3 language both retained |
| CT-ROLECONFLICT-010 | positivity EN vs JA,S05:168–185;JA280–284 | version | different scope of gradients, no correction |
| CT-ROLECONFLICT-011 | barrier effective / hard prohibition,S05:46–50;JA236 | version | role-strength divergence |
| CT-ROLECONFLICT-012 | physical/concept grammar vs same equation,S12:66–71;JA576 | cross-scale / version | not same explanatory level by audit inference |
| CT-ROLECONFLICT-013 | figure J/body J_I and process labels,FIG003 | documentary | name plus role expansion, not neural map |
| CT-ROLECONFLICT-014 | note interpretation / formal theoretical basis,S10:40–44/61–70 | documentary | support direction not proof or circularity verdict |
| CT-ROLECONFLICT-015 | concept named region / single-concept individuation open,S05:126;S11:49–52 | semantic | local definition vs individuation criterion distinguished |
| CT-ROLECONFLICT-016 | depth/gradient/cost linguistic compression,S05:68;S03:49;EQF012 | formal-role | reinforced gradient + lower cost roles; no mathematical incompatibility conclusion |

## 28. Strongest conflation candidates

優先照合候補でありdispositionではない。CT-CONFL-002の局所concept定義そのものをHIGHとしない。semantic/cognitive/phenomenal役割の妥当性・circularity・evidence burdenは次Phase以降で扱う。

| CT-TOPROLE | Conflation reference | Source pair | Phase03/04 handoff question |
| --- | --- | --- | --- |
| CT-TOPROLE-001 | CT-CONFL-004 | S05:138–152 ↔ S10:28 | integral-defined understandingとfelt understandingの橋渡しの読み |
| CT-TOPROLE-002 | CT-CONFL-006 | S04:64–66 ↔ FIG001 | field/path/thoughtの同一呼称の扱い |
| CT-TOPROLE-003 | CT-CONFL-007 | S04:76–78 ↔ EQF002 | tau演算parameterとexperiential timeの役割 |
| CT-TOPROLE-004 | CT-CONFL-008 | S07:69–79 | bifurcation・insight・subjective suddennessの説明段階 |
| CT-TOPROLE-005 | CT-CONFL-009 | EQF009 ↔ S07:24–31 | term→ensures reuse/learningというmechanism-language |
| CT-TOPROLE-006 | CT-CONFL-014 | S08:18–46 ↔ S11:55–58 | same dynamicsとqualitative social extensionの位置 |
| CT-TOPROLE-007 | CT-CONFL-015 | S08:56–66 | norm/institution naming→stability follows from depth |
| CT-TOPROLE-008 | CT-CONFL-005 | S03:64–65 ↔ S09:15–16 | trajectory-set namingとmeaning explanationの境界 |
| CT-TOPROLE-009 | CT-CONFL-003 | S05:126–135 ↔ S06:35–64 | local concept Definitionから属性/semantic drift説明への移行 |
| CT-TOPROLE-010 | CT-CONFL-017 | S12:66–71 ↔ JA575–576 | guarded grammar比較とsame-equation解クラスの差 |

## 29. Phase02 uncertainty ledger

新26件は既存CT-U-001–072の解決でも置換でもない。formal signature問題からrole使用の問題を分離した追加question。総数98、以前の72件はbyte unchanged。

| CT-U | New role question | Trace | Question left unresolved |
| --- | --- | --- | --- |
| CT-U-073 | local naming vs explanation | CONFL001/003;DEFROLE001/013 | 定義したlandscape/conceptを後で説明結果と呼ぶ役割の境界 |
| CT-U-074 | field/path/thought separation | CONFL006;THOUGHT001–005 | flow direction、trajectory、thought contentの区別をどの文が維持するか |
| CT-U-075 | understanding/felt understanding | CONFL004;UNDERROLE001–008 | cognitive Definitionと主観的easeのcorrespondenceは別claimか |
| CT-U-076 | meaning trajectory set vs emergent label | CONFL005;MEANING003–009 | 否定するprimitiveと肯定するmeaning-roleのscope |
| CT-U-077 | tau experience vs ordering | CONFL007;TIMEROLE001–007 | 形式順序parameterから体験時間への命名の範囲 |
| CT-U-078 | insight event vs suddenness | CONFL008;INSIGHTROLE002–006 | topology, cognitive connection, phenomenal suddennessの各claim |
| CT-U-079 | token neutral but causal | CONFL009/010;TOKENROLE003–007 | semantic neutralityとmechanism-languageが担う異なる役割 |
| CT-U-080 | coupling term used as assurance | MECH008;MECHLANG016 | ensures each reuseとtermの説明上の接続 |
| CT-U-081 | geometry of concept attributes | CONCEPTROLE005/006;CONFL003 | width/curvatureをcontext/precisionとする役割 |
| CT-U-082 | semantic drift mechanism | MECH010;TRANS022 | boundary mutationがsemantic change説明として使われる範囲 |
| CT-U-083 | positivity to innovation | POSROLE003–009 | formal condition、gradient availability、learning opennessの別claim |
| CT-U-084 | barrier effective/prohibitive role | BARRIER003–008 | EN effective analogueとJA禁止の同authority化を避ける |
| CT-U-085 | Phi* history/memory role | ASYMROLE001–007;ROLECONFLICT005 | target namingとcontinued history/recallの説明上の区別 |
| CT-U-086 | collective same dynamics role | SOCIALROLE002/011 | future formalizationとのscope関係 |
| CT-U-087 | institution attractor role | SOCIALROLE006/007 | namingとinstitutional stabilityの因果説明を分ける |
| CT-U-088 | collective intelligence scope | SOCIALROLE008;CONFL016 | 社会scale定義とgeneral intelligence claimの範囲 |
| CT-U-089 | negative phenomenal scope vs positives | SCOPE004/005;ROLECONFLICT009 | subjective explanation否定はpositive T3文をどこまで限定するか |
| CT-U-090 | conscious access without criterion | S03:84–93;SCOPE005 | invisible GPUのaccess対象とgeometryの役割 |
| CT-U-091 | vocabulary set/distribution role | ROLECONFLICT006;DEFROLE008 | formal selectionとsemantic organizationの説明上の違い |
| CT-U-092 | individual/social function inversion | TOKENROLE008;SOCIALROLE003 | same token propertyと異なるcognitive/social function |
| CT-U-093 | physical/concept same grammar | XROLE003;ROLEVAR016 | EN comparisonとJA same-equation identityの説明レベル |
| CT-U-094 | Q quantization analogy role | IDREL011;SCOPE009 | isomorphic語とanalogy/no quantum claimの範囲 |
| CT-U-095 | note interpretation vs theoretical basis | ROLECONFLICT014;SCOPE011 | L3/L1支援はformal→phenomenological説明としてどう使われるか |
| CT-U-096 | figure compressed roles | FIGROLE002/004/007/013 | bodyのdefinition/correspondenceとvisual identity風ラベルの区別 |
| CT-U-097 | ENJA meaning/concept version | ROLEVAR007/009 | JA経験的意味のinterpretationと再入による概念再定義 |
| CT-U-098 | downstream reciprocal role authority | XROLE006–010 | Con/Intelligence接続はCT側roleの根拠にしない |

## 30. Phase02 limits

役割移行の妥当性、conflationの致命性、token couplingのwell-typedness、positivityの正誤、concept/understanding定義の機能、insightとbifurcationの実在的同一性、social extensionの正当性、circularity、empirical supportの有無/十分性、claim disposition、式変更の要否は未判定。
新bridge/operator/semantic definition/cognitive mechanism/phenomenal criterionを一切追加しない。Consciousnessの改訂済み比較をCTの修正authority・成立根拠に使わない。

## 31. Validation

ローカル検証: PASS。IDは各primary table行を母数として連続番号・一意性・coverageを照合。繰返し引用は新entryに数えない。

| Inventory | Count |
| --- | --- |
| Equation roles / EQF coverage | 14 / 14 |
| Inline roles / INLINE coverage | 24 / 24 |
| Definitions / DEF coverage | 18 / 18 |
| Symbol-role crosswalk | 53 / 53 |
| Transition families | 39 |
| T0→T1 | 12 |
| T0→T2 | 13 |
| T0→T3 | 4 |
| T2→T3 | 2 |
| T1→T3 | 2 |
| T1→T2 | 6 |
| Conflation candidates + controls | 20 |
| HIGH / MEDIUM / LOW / UNRESOLVED | 7 / 8 / 4 / 1 |
| CT-CONCEPTROLE | 10 |
| CT-MEANING | 13 |
| CT-THOUGHT | 9 |
| CT-UNDERROLE | 10 |
| CT-INSIGHTROLE | 8 |
| CT-TIMEROLE | 9 |
| CT-TOKENROLE | 9 |
| CT-MECH | 11 |
| CT-POSROLE | 10 |
| CT-BARRIER | 8 |
| CT-ASYMROLE | 9 |
| CT-SOCIALROLE | 11 |
| CT-SCOPE | 12 |
| CT-MECHLANG | 34 |
| CT-NS | 26 |
| CT-IDREL | 32 |
| CT-XROLE | 12 |
| CT-FIGROLE | 14 |
| CT-ROLEVAR | 21 |
| CT-ROLECONFLICT | 16 |
| CT-TOPROLE | 10 |
| CT-U | 26 |
| Uncertainties old / new / total | 72 / 26 / 98 |

EN main include 12/12、JA workingの本文対応heading 12/12（subtitle/changelogは除く）、canonical JA entry NOT LOCATED。
EN12 displayed blocks / JA14 displayed blocksを再計数。全source bytesが開始時と同一のためraw表示式も不変。14 relation rows / 14 EQFはPhase01と照合済み。
3/3 PNGを視認して14 label-role entriesに記録。新記録の全33節、Markdown table列数・fence対応・READMEを含む31 local linksの存在を検証した。
EN/JAは21 role-strength variantsを記録、canonicalとworkingの権限差は維持。§21–23のscan familiesおよび§31.1行索引をcontextと照合した。

Task-start SHA-256 snapshot: repository内1462 files（.git除外、untracked/ignored artifactsも含む）。
比較結果: 既存1461 files unchanged、既存変更1（audit READMEのみ）、新規1（本Phase02 recordのみ）、削除0。
Phase00/01の記録、canonical main+12 sections、JA working、3 PNG、distribution PDF、refs.bib、他branchを含む非対象fileはbyte unchanged。
snapshotとread-only検証scriptはrepository外 `${TEMP_EVIDENCE_ROOT}/ct_phase02.XpSwaN/` に置いた。repo内helper fileは作成していない。
既存CT-U-001–072はauthority内に72/72存在し改変なし、新規CT-U-073–098は連続26件。未解決事項を解決/置換した記録はない。

`git diff --check`: PASS（診断なし）。untracked新recordも `git diff --no-index --check /dev/null <record>` で別検証。
`git status --short`: 既存の多数の変更と `?? notes/ct_audit/` が残る。statusを本taskの変更範囲と同一視せず、上記snapshotで2 fileだけと確認。
Source/equation/figure/PDF/BibTeX modification: NO。external research / simulation / build / commit / push: NOT RUN。
妥当性・circularity・evidence sufficiency・dispositionの判定は行っていない。

### 31.1 Lexical scan locator index

全canonical EN entry+12 sectionsとJA全589行をread/scan。TeX comments・entry preambleは除外。MECHはmechanism/mechanistic, causes, produces, generates, determines, ensures, gives rise to, accounts for, results in, leads to, reinforces, deepens等と日本語の生成/説明/強化/深化等。NSはnecessary/requires/sufficient/cannot/only if/excludes/ensures/follows from/generically等、IDはis/are/same/identical/equivalent/corresponds/reflects/represents/realizes/projected/isomorphic/solution class/generative grammar等と日本語相当語。

これはlexical hit行索引でありfamily数ではない。手読みにより複数行に分かれる文、同義語、否定・未来・navigation・標準理論の紹介をcontext判別し、§21–23のfamilyにまとめた。例えばS02:59/JA77のgenerationはseries label、JA584の生成は文書履歴、JA589の反映は編集履歴。これらを機構や役割移行として加算しない。

| Source | MECH hit lines | NS hit lines | ID hit lines |
| --- | --- | --- | --- |
| S00 | 0 | 0 | 88,89,92,93,94,95 |
| S01 | 18,23,26,35,38 | 33 | 9,17,29,31,38,39 |
| S02 | 40,59,86,93 | 83,89 | 13,14,15,20,22,28,46,50,51,53,74,78,81,82,93,108 |
| S03 | 76,80,87 | 14,79 | 18,23,25,27,30,38,39,40,41,46,48,49,54,55,56,57,61,64,76,78,80,85,86,92,93 |
| S04 | 30,38,39,111 | 26,118 | 8,16,17,19,24,37,42,89,95,97,100,101,110,111,112,113,114,115,118 |
| S05 | 20,60,66,68,91,170,185 | 54,55,57,162,168,172 | 10,15,26,42,44,46,48,55,69,74,75,89,109,119,120,127,139,146,149,151,182 |
| S06 | 44,45,62,64 | 0 | 8,11,12,19,36,37,41,47,54,56,59,70,76,77,80,81,82 |
| S07 | 11,15,20,23,24,25,28,30,44,64,78 | 24,55 | 10,21,23,28,30,35,40,43,44,50,59,70,72,76,79 |
| S08 | 24,45,51,65 | 44,62,63,64 | 8,12,18,42,43,45,48,51,56,58,70,74 |
| S09 | 19,21,33,34,49 | 10,63 | 13,15,16,20,21,26,27,37,45,53,65 |
| S10 | 21 | 0 | 11,19,42,49,52,55,62,70 |
| S11 | 34,37 | 63 | 22,23,25,27,33,34,37,41,46,51,52,55,61,63 |
| S12 | 36,44,64,67 | 18,38 | 12,18,20,23,26,29,35,44,46,48,58,63,67,68,69 |
| JA | 26,32,33,34,41,43,67,77,93,95,97,153,167,174,185,200,220,248,311,320,321,322,343,347,350,351,352,355,356,367,375,382,397,409,420,430,442,449,459,481,522,530,531,532,565,569,575,584 | 14,18,41,91,95,125,147,167,191,240,278,280,281,352,373,404,409,419,420,430,449,456,459,466,512,542,548,556,557,567,588 | 26,43,53,54,71,97,102,104,121,127,135,136,139,147,155,159,164,166,167,173,174,176,193,195,197,200,201,202,241,247,256,257,261,267,271,272,290,292,294,309,317,318,327,331,334,335,343,355,361,365,367,371,379,380,382,388,391,394,408,409,412,416,424,426,442,444,451,456,467,477,479,498,501,502,503,508,512,525,527,531,532,536,538,542,548,556,561,563,565,569,573,575,576,589 |

## 32. Stop boundary

Phase02 COMPLETEで停止。Phase03 preload / self-reference / circularity auditには進まない。
No CT source revised / No CT equation revised / No new theory introduced。

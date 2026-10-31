# Conceptual Topography / CT — Phase04 claim / evidence burden audit v0.1

## 0. Status

CT audit: IN PROGRESS

Phase 00–03: COMPLETE（既存authorityを保持）<br>
Phase 04 claim / evidence burden audit: COMPLETE<br>
Phase 05–07: NOT STARTED<br>
CT source revision: NOT STARTED<br>
CT equation revision: NOT STARTED

監査日: 2026-09-10。48 claim familiesのburden/support/gapを記録する。claim disposition・theory validity・最終falsifiabilityのfreezeではない。新規source/式/criterionは導入しない。

結論の範囲: YES 6 / PARTIAL 36 / NO 3 / UNRESOLVED 3。Repository evidence ceiling: CE2（既存外部文献への概念的参照まで）。独立CT mapping/data/predictive validationは未発見。SERIOUS 3件はRETAIN。

## 1. Authority / scope

- [Phase00](00_dependency_inheritance_and_authority_record_v0.1_ja.md)
- [Phase01](01_equation_symbol_object_inventory_v0.1_ja.md)
- [Phase02](02_formal_semantic_cognitive_phenomenal_role_audit_v0.1_ja.md)
- [Phase03](03_preload_selfreference_circularity_audit_v0.1_ja.md)
- [README](README_ja.md)

EN canonicalは[S00 main.tex](../../conceptual-topography/main.tex)と12 included sections。JAは[working Markdown](../../conceptual-topography/conceptual_topography_ja.md)、canonical JA entryはNOT LOCATED。JAは追加独立証拠でもcanonical修正版でもない。source locatorのS番号/行番号はtask-start fileに対応する。

| Locator | Canonical section |
| --- | --- |
| S01 | [abstract](../../conceptual-topography/sections/abstract.tex) |
| S02 | [introduction](../../conceptual-topography/sections/introduction.tex) |
| S03 | [intuitive_picture](../../conceptual-topography/sections/intuitive_picture.tex) |
| S04 | [formal_mapping](../../conceptual-topography/sections/formal_mapping.tex) |
| S05 | [core_equations](../../conceptual-topography/sections/core_equations.tex) |
| S06 | [structural_interpretation](../../conceptual-topography/sections/structural_interpretation.tex) |
| S07 | [dynamics](../../conceptual-topography/sections/dynamics.tex) |
| S08 | [multiscale](../../conceptual-topography/sections/multiscale.tex) |
| S09 | [pathologies](../../conceptual-topography/sections/pathologies.tex) |
| S10 | [relation_to_note](../../conceptual-topography/sections/relation_to_note.tex) |
| S11 | [discussion](../../conceptual-topography/sections/discussion.tex) |
| S12 | [conclusion](../../conceptual-topography/sections/conclusion.tex) |

[CT README](../../conceptual-topography/README.md)、[refs.bib](../../conceptual-topography/refs.bib)、[EN distribution](../../conceptual-topography/main.pdf)は別authority。PDFは同一sourceのpresentationであり独立supportではない。

比較locator: [Con-MAP](../../consciousness/sections/correspondence_map.tex)、[Con-LOOP](../../consciousness/sections/dynamics_log_referencing.tex)、[Con-TCA](../../consciousness/sections/torque_converter_attention.tex)、[Int2-I](../../intelligence-part2/sections/00_introduction_ja.tex)、[Int2-B](../../intelligence-part2/appendices/appendix_b_homology_ja.tex)。VED/IFGT actual source/version参照はPhase00 CT-DEP台帳を継承。[current IFGT](../../Information-Field-Geometry-Theory/main.tex)と[VED Vol1](../../paper/vol1/main.tex)の存在/再使用はCTでのtyped inheritanceやvalidationではない。

Task-start SHA-256 snapshotは.gitを除くrepository内1464ファイルを対象に取得（ignored/untracked含む）。開始時dirty changesを基準としgit HEADとの差を本taskの変更と誤認しない。

## 2. Claim-type taxonomy

| Type | Meaning | Primary family count |
| --- | --- | --- |
| DEF | definition | 6 |
| FORM | formal/internal | 17 |
| SEM | semantic | 21 |
| FUNC | cognitive/functional | 26 |
| MECH | mechanism | 15 |
| PHEN | phenomenal | 8 |
| OBS | observational | 3 |
| EMP | empirical | 5 |
| PRED | predictive | 8 |
| SOCIAL | social/institutional | 8 |
| XSC | cross-scale | 7 |
| ID | identity/equivalence | 17 |
| NEC | necessity | 5 |
| SUFF | sufficiency | 1 |
| METHOD | methodological | 9 |
| NEG | negative scope | 8 |
| DOC | documentary/authority | 8 |

複数選択。count合計は48を超える。EMP/OBS/PREDはsourceが負う主張の種類であって、data/testがあるという認定ではない。NEGを含む混合claimでもpositive成分を捨てない。T0 formal / T1 semantic / T2 cognitive / T3 phenomenalは監査層でありgenerative chainの認定ではない。

## 3. Evidence-type taxonomy

| Type | Meaning | Current presence |
| --- | --- | --- |
| E0 | definitional/source-local | 所在あり（§6の範囲に限定） |
| E1 | formal-internal | 所在あり（§6の範囲に限定） |
| E2 | model-local structural | 所在あり（§6の範囲に限定） |
| E3 | schematic/figure | 所在あり（§6の範囲に限定） |
| E4 | internal cross-source correspondence | 所在あり（§6の範囲に限定） |
| E5 | phenomenological example | 所在あり（§6の範囲に限定） |
| E6 | external-literature reference | 所在あり（§6の範囲に限定） |
| E7 | operational map | CT-linked artifact未発見 |
| E8 | empirical data | CT-linked artifact未発見 |
| E9 | replicated/independent empirical support | CT-linked artifact未発見 |
| E10 | held-out/predictive validation | CT-linked artifact未発見 |
| E11 | typed cross-scale translation | CT-linked artifact未発見 |
| E12 | social/behavioral operational evidence | CT-linked artifact未発見 |

E1は式/内部relationというartifact分類でありproof certificationではない。E6のbibliography metadataとactual citation anchorも区別する。E5は例でありparticipant dataではない。

## 4. Burden taxonomy

| Burden | Required type | Primary uses |
| --- | --- | --- |
| B0 | definitional coherence/source scope | 13 |
| B1 | formal specification/object/derivation | 23 |
| B2 | model-local consequence under assumptions | 20 |
| B3 | independent semantic mapping/criterion | 17 |
| B4 | cognitive-functional mapping | 24 |
| B5 | causal/process-level mechanism support | 15 |
| B6 | independent phenomenal mapping/criterion | 8 |
| B7 | observable extraction/calibration | 25 |
| B8 | actual empirical support | 24 |
| B9 | distinctive prospective/held-out prediction | 8 |
| B10 | typed cross-scale/domain-invariant translation | 7 |
| B11 | social/institutional operational relation | 8 |
| B12 | universality/generalization | 4 |

13/13 categories使用。要求される証拠の種類を挙げるもので、新しいmapping/protocolを作るものではない。

YES = 現在の限定されたclaim成分のburdenにsource内supportがある。PARTIAL = 式/定義/構造的説明などはあるが強い成分のburdenが未充足。NO = 要求される種類のsupportがrepository内に未発見（命題が偽という意味ではない）。UNRESOLVED = authority/対象/readingが未固定で全体supportを安全に確定できない。B0のYESはempirical validationではない。

## 5. Primary claim/burden table

| BURDEN | Claim / source / short claim | Claim type(s) | Required burden | Repository support | Gap | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CT-BURDEN-001 | CT-CLM-001;S01/S04;概念地形はPhiの長時間幾何 | DEF/FORM/SEM | B0 | YES; CT-EVID-001, CT-EVID-010, CT-EVID-015 | 当該scope内なし | source-local landscape naming only; convergence is CLM015 |
| CT-BURDEN-002 | CT-CLM-002;S02 §1.2/S06 §5.1;統一方程式の認知的解クラスを同定 | FORM/FUNC/ID/DOC | B1/B2/B4/B7/B8 | PARTIAL; CT-EVID-002, CT-EVID-003, CT-EVID-017, CT-EVID-031 | CT-GAP-001, CT-GAP-002, CT-GAP-022 | cognitive solution-class table, detailed analysis deferred |
| CT-BURDEN-003 | CT-CLM-003;S04 §3.1;Iは認知窓の未解決緊張を表現 | SEM/XSC/ID | B3/B7/B10 | PARTIAL; CT-EVID-001, CT-EVID-015, CT-EVID-031 | CT-GAP-001, CT-GAP-003, CT-GAP-018 | projected unresolved-tension representation; observable absent |
| CT-BURDEN-004 | CT-CLM-004;S04 §3.1;高Iはconceptually active領域 | FUNC/ID | B4/B7/B8 | NO; CT-EVID-015 | CT-GAP-003, CT-GAP-022 | high I→activity only correspondence assertion |
| CT-BURDEN-005 | CT-CLM-005;S04/S05;Phi幾何が後続flowの方向を拘束 | FORM | B1/B2 | PARTIAL; CT-EVID-001, CT-EVID-003, CT-EVID-004, CT-EVID-015 | CT-GAP-001, CT-GAP-002 | gradient/force relations supplied, full domain and evolution specification missing |
| CT-BURDEN-006 | CT-CLM-006;S05 §4.4/S02;conceptは局所安定領域 | DEF/FORM/SEM/ID | B0/B1 | PARTIAL; CT-EVID-011, CT-EVID-017, CT-EVID-034 | CT-GAP-004 | B0 local definition supported; perturbation norm/individuation not fixed; external anchor only conceptual precedent |
| CT-BURDEN-007 | CT-CLM-007;S05 §4.4;understandingはtraversal cost閾値条件 | DEF/FORM/FUNC | B0/B1 | PARTIAL; CT-EVID-012, CT-EVID-026 | CT-GAP-005 | B0 naming supported; region/metric/theta incomplete; felt claim separately017 |
| CT-BURDEN-008 | CT-CLM-008;S03 §2.1/S04;thoughtはflow trajectory | FUNC/ID | B1/B4/B7/B8 | PARTIAL; CT-EVID-003, CT-EVID-015, CT-EVID-017, CT-EVID-018 | CT-GAP-002, CT-GAP-022 | formal flow exists; field→trajectory→thought independent criterion absent |
| CT-BURDEN-009 | CT-CLM-009;S03 §2.2;meaningは利用可能なtrajectory集合 | DEF/SEM/ID/PHEN | B0/B3/B6 | PARTIAL; CT-EVID-018, CT-EVID-024, CT-EVID-025 | CT-GAP-006, CT-GAP-012 | local label survives; EN identity/JA experienced-meaning interpretation lacks independent map |
| CT-BURDEN-010 | CT-CLM-010;S03 §2.4;不可視の地形が自然な連想・突然の理解感を生む | FUNC/MECH/PHEN/OBS/EMP | B4/B5/B6/B7/B8 | PARTIAL; CT-EVID-018, CT-EVID-021 | CT-GAP-006, CT-GAP-022 | intuitive examples and internal geometric account, no model-specific participant data |
| CT-BURDEN-011 | CT-CLM-011;S04 table;tauは概念発展のexperiential time | FORM/PHEN/ID | B6/B7/B8 | NO; CT-EVID-015 | CT-GAP-007, CT-GAP-022 | evolution parameter present; experiential identification only table naming |
| CT-BURDEN-012 | CT-CLM-012;S05 §4.2;離散re-addressable unitは安定した低cost再帰に必要 | FORM/FUNC/NEC | B1/B2/B4/B8 | PARTIAL; CT-EVID-016 | CT-GAP-008, CT-GAP-022 | qualitative continuous/discrete argument; necessity theorem/comparative task absent |
| CT-BURDEN-013 | CT-CLM-013;S05 §4.2/FIG002;token reuseがgradient/井戸を強化 | FORM/FUNC/MECH/PRED | B1/B2/B4/B5/B7/B8/B9 | PARTIAL; CT-EVID-009, CT-EVID-019, CT-EVID-028 | CT-GAP-009, CT-GAP-010, CT-GAP-022, CT-GAP-023 | formula vs well-typedness vs consequence vs cognition separated |
| CT-BURDEN-014 | CT-CLM-014;S03 §2.3;communicationはsimilar landscapeの反応同期 | SEM/FUNC/MECH/SOCIAL/EMP | B3/B4/B5/B7/B8/B11 | PARTIAL; CT-EVID-018, CT-EVID-022 | CT-GAP-015, CT-GAP-016, CT-GAP-022 | similarity premise/communication explanation, no independent scoring |
| CT-BURDEN-015 | CT-CLM-015;S05 §4.3;repeated couplingでPhi→Phi* | FORM/SEM | B1/B2/B3 | PARTIAL; CT-EVID-010, CT-EVID-019 | CT-GAP-011 | limit notation + stages; convergence space/proof absent |
| CT-BURDEN-016 | CT-CLM-016;S05 §4.3;Phi*はhistoryを反映しなお変形する | FORM/SEM | B1/B2 | UNRESOLVED; CT-EVID-010, CT-EVID-019 | CT-GAP-011, CT-GAP-024 | nonstatic/nonunique qualification scope vs asymptotic target not fixed |
| CT-BURDEN-017 | CT-CLM-017;S03 §2.1/S10 table;理解した経験は移動の容易さの変化 | FUNC/PHEN/OBS/ID | B4/B6/B7/B8 | PARTIAL; CT-EVID-012, CT-EVID-018, CT-EVID-024 | CT-GAP-005, CT-GAP-006, CT-GAP-022 | ease example/structured correspondence, not independent felt criterion |
| CT-BURDEN-018 | CT-CLM-018;S05 §4.5 EN;I>0は通常状態として完全概念閉包を除外 | FORM/SEM/NEC | B1/B2/B3 | PARTIAL; CT-EVID-013, CT-EVID-023, CT-EVID-031 | CT-GAP-013 | conditional EN nonpointwise guard, semantic openness mapping not established |
| CT-BURDEN-019 | CT-CLM-019;JA §§概要/3.1/4.5/7.4/11;正値性は常時残余勾配を保証/含意する | FORM/SEM/FUNC/SOCIAL/NEC/PRED | B1/B2/B3/B4/B9/B11 | PARTIAL; CT-EVID-013, CT-EVID-038 | CT-GAP-013, CT-GAP-023, CT-GAP-024 | JA-only generic gradients/all attractors/always innovation wording; no stronger proof |
| CT-BURDEN-020 | CT-CLM-020;S06 §5.2;depth/width/curvatureが抵抗/文脈/精度を表す | SEM/FUNC/MECH/ID | B1/B3/B4/B5/B7/B8 | PARTIAL; CT-EVID-011, CT-EVID-017 | CT-GAP-004, CT-GAP-012, CT-GAP-022 | geometry descriptors provided; contextual range/precision criterion absent |
| CT-BURDEN-021 | CT-CLM-021;S06 §5.3;ridge変形がsemantic driftを説明 | SEM/FUNC/MECH/PRED | B1/B2/B3/B4/B5/B7/B8/B9 | PARTIAL; CT-EVID-017, CT-EVID-019 | CT-GAP-010, CT-GAP-012, CT-GAP-022, CT-GAP-023 | ridge evolution narrative, no semantic drift task |
| CT-BURDEN-022 | CT-CLM-022;S06 §5.4;vocabularyは安定性による集合/分布 | DEF/FORM/SEM/ID | B0/B1/B3 | PARTIAL; CT-EVID-014, CT-EVID-017 | CT-GAP-025 | set criterion present; S numeric rule/distribution semantics unspecified |
| CT-BURDEN-023 | CT-CLM-023;S07 §6.1;反復強化でconceptがself-sustainingになる | FORM/FUNC/MECH/PRED | B1/B2/B4/B5/B7/B8/B9 | PARTIAL; CT-EVID-009, CT-EVID-019 | CT-GAP-008, CT-GAP-009, CT-GAP-010, CT-GAP-022, CT-GAP-023 | ensures reinforcement/self-sustaining narrative; no executed model witness |
| CT-BURDEN-024 | CT-CLM-024;S07 §6.2;忘却/想起はflattening/re-deepening | FUNC/MECH/PRED | B2/B4/B5/B7/B8/B9 | PARTIAL; CT-EVID-007, CT-EVID-020 | CT-GAP-010, CT-GAP-011, CT-GAP-022, CT-GAP-023 | memory interpretation of relaxation; independent memory task absent |
| CT-BURDEN-025 | CT-CLM-025;S07 §6.3–4;conceptual change/insightはrapid topology change | SEM/FUNC/PHEN/ID | B1/B3/B4/B6/B7/B8 | PARTIAL; CT-EVID-017, CT-EVID-021 | CT-GAP-006, CT-GAP-012, CT-GAP-022 | topology alternatives vs cognitive resolution vs felt event not independently linked |
| CT-BURDEN-026 | CT-CLM-026;S07 §6.4;主観的突然性はtopology thresholdの反映 | PHEN/MECH/OBS/EMP | B5/B6/B7/B8 | PARTIAL; CT-EVID-021 | CT-GAP-006, CT-GAP-022 | threshold narrative is structured correspondence, not experienced-suddenness mechanism evidence |
| CT-BURDEN-027 | CT-CLM-027;S07 §6.3;effective barrierはbelief revision抵抗を説明 | FUNC/MECH/EMP | B2/B4/B5/B7/B8 | PARTIAL; CT-EVID-008, CT-EVID-020 | CT-GAP-014, CT-GAP-022 | effective barrier model, no calibrated belief resistance |
| CT-BURDEN-028 | CT-CLM-028;S08 §7.1;個体→社会で同一力学、支配costのみ交替 | FORM/FUNC/SOCIAL/XSC/ID | B1/B2/B4/B10/B11/B12 | PARTIAL; CT-EVID-022 | CT-GAP-015, CT-GAP-017 | same dynamics across agents asserted; aggregate space/map absent |
| CT-BURDEN-029 | CT-CLM-029;S08 §7.2;shared inputsがcorrelated wells/shared landscapeを生成 | SEM/FUNC/MECH/SOCIAL/PRED | B2/B3/B4/B5/B7/B8/B9/B11 | PARTIAL; CT-EVID-022 | CT-GAP-015, CT-GAP-016, CT-GAP-022, CT-GAP-023 | correlated-well argument; no shared-field estimator/data |
| CT-BURDEN-030 | CT-CLM-030;S08 §7.3;norms/institutionsはcollective attractor | SEM/SOCIAL/ID | B3/B7/B8/B11 | PARTIAL; CT-EVID-022 | CT-GAP-016, CT-GAP-022 | qualitative attractor analogy present; institution identity not independently supported |
| CT-BURDEN-031 | CT-CLM-031;S08 §7.3;制度安定はcentral authority不要、well depthから従う | MECH/SOCIAL/NEC/SUFF/EMP | B2/B5/B7/B8/B11 | PARTIAL; CT-EVID-022 | CT-GAP-016, CT-GAP-022 | depth→stability and threshold assertion; no institutional causal evidence |
| CT-BURDEN-032 | CT-CLM-032;S09 §8.2;overclosure/underclosureがrigidity/unstable thoughtに対応 | FUNC/PHEN/MECH/PRED | B2/B4/B5/B6/B7/B8/B9 | PARTIAL; CT-EVID-020 | CT-GAP-006, CT-GAP-014, CT-GAP-022, CT-GAP-023, CT-GAP-026 | regime/pathology correspondences, not diagnostic or phenomenal identity validation |
| CT-BURDEN-033 | CT-CLM-033;S09 §8.1;subjective experienceを生成/説明しない | NEG/METHOD/PHEN | B0 | YES; CT-EVID-025 | 当該scope内なし | authorial exclusion only, positive phenomenal statements retain own burden |
| CT-BURDEN-034 | CT-CLM-034;S09 §8.1/S11;neural implementationはfuture work | NEG/METHOD/DOC | B0 | YES; CT-EVID-025, CT-EVID-026 | 当該scope内なし | neural implementation deferred, not a carrier result |
| CT-BURDEN-035 | CT-CLM-035;S09 §8.2;sync breakdownはcommunication failure/polarizationの構造基盤 | SEM/FUNC/MECH/SOCIAL/PRED | B2/B3/B4/B5/B7/B8/B9/B11 | PARTIAL; CT-EVID-022 | CT-GAP-015, CT-GAP-016, CT-GAP-022, CT-GAP-023 | communication/polarization failure narrative only |
| CT-BURDEN-036 | CT-CLM-036;S09 §8.3/S11;parameters/observable correspondence/individuation未指定 | NEG/METHOD/DOC | B0 | YES; CT-EVID-026 | 当該scope内なし | missing specification explicitly acknowledged and checked locally |
| CT-BURDEN-037 | CT-CLM-037;S10 §9.2/S12;L3がL1 noteを理論的に支える | DOC/METHOD/SEM/FUNC | B1/B3/B4/B6 | UNRESOLVED; CT-EVID-024 | CT-GAP-019 | exact L1 artifact/version unfixed; theoretical basis ≠ independent note validation |
| CT-BURDEN-038 | CT-CLM-038;S10 §9.1;Consciousness note CPU/GPUと将来fast/slow対応 | DOC/XSC/FUNC | B4/B10 | UNRESOLVED; CT-EVID-024, CT-EVID-032 | CT-GAP-020 | future note/current Con authority mismatch; comparison exists but not typed support |
| CT-BURDEN-039 | CT-CLM-039;S08 §7.4/S12;intelligenceはshared landscape維持の分散過程 | DEF/FUNC/SOCIAL/ID | B0/B4/B7/B8/B11/B12 | PARTIAL; CT-EVID-022, CT-EVID-025 | CT-GAP-016, CT-GAP-017, CT-GAP-022 | local social maintenance definition yes; broader intelligence identity burden unmet |
| CT-BURDEN-040 | CT-CLM-040;S04 Q remark;quantizationとstructurally isomorphic、quantum主張は否定 | XSC/ID/NEG/METHOD | B0/B1/B10 | PARTIAL; CT-EVID-016, CT-EVID-025 | CT-GAP-008, CT-GAP-018 | explicit analogy/no quantum guard supported; isomorphic wording lacks typed map |
| CT-BURDEN-041 | CT-CLM-041;S11 §10.1;distributional semanticsと使用history/共起の違い | METHOD/SEM/DOC | B3/B7 | PARTIAL; CT-EVID-009, CT-EVID-040 | CT-GAP-012, CT-GAP-021 | conceptual comparison only; no dedicated semantic literature anchor/map |
| CT-BURDEN-042 | CT-CLM-042;S11 §10.1;driveはprediction error influx、deepeningはerror minimization | FUNC/MECH/DOC | B2/B4/B5/B7/B8 | PARTIAL; CT-EVID-006, CT-EVID-035 | CT-GAP-003, CT-GAP-010, CT-GAP-021, CT-GAP-022 | Friston anchor supports comparison background only; CT error-minimization mapping absent |
| CT-BURDEN-043 | CT-CLM-043;S12 EN末尾;concept/particleはsame generative grammarのprojected regimes | XSC/SEM/ID/NEG | B1/B3/B10/B12 | PARTIAL; CT-EVID-030, CT-EVID-031, CT-EVID-025 | CT-GAP-018 | projected grammar/nonidentity comparison; no common invariant/typed translation |
| CT-BURDEN-044 | CT-CLM-044;JA結論末尾;concept/particleは同一基礎方程式の解クラス | XSC/SEM/FORM/ID | B1/B3/B10/B12 | NO; CT-EVID-038, CT-EVID-030, CT-EVID-031 | CT-GAP-018, CT-GAP-024 | JA same-equation solution-class identity lacks a typed source-target statement |
| CT-BURDEN-045 | CT-CLM-045;S04 §3.3/S09;Phiはmeaning fieldでなくtokensはmeaning unitsでない | NEG/METHOD/SEM | B0 | YES; CT-EVID-025 | 当該scope内なし | meaning-neutral primitive exclusions source-local, not proof of positive meaning model |
| CT-BURDEN-046 | CT-CLM-046;S02/S09;thoughtにdirecting subjectを必要としない | NEG/METHOD/FUNC/NEC | B0/B2 | YES; CT-EVID-003, CT-EVID-025 | 当該scope内なし | model lacks directing-subject variable; not empirical universal exclusion |
| CT-BURDEN-047 | CT-CLM-047;S05 §4.1;drive/decay/barrierはinput/forgetting/overclosure抵抗 | FORM/FUNC/MECH | B1/B2/B4/B5/B7/B8 | PARTIAL; CT-EVID-005, CT-EVID-006, CT-EVID-007, CT-EVID-008, CT-EVID-020 | CT-GAP-001, CT-GAP-003, CT-GAP-014, CT-GAP-022 | source terms exist; input/forgetting/cognitive resistance mappings not calibrated |
| CT-BURDEN-048 | CT-CLM-048;S00/README;general variablesを再定義せずcognitive projectionとして使う | DOC/METHOD/XSC/NEG | B0/B1/B10 | PARTIAL; CT-EVID-015, CT-EVID-030, CT-EVID-031, CT-EVID-039 | CT-GAP-018, CT-GAP-024 | projected-use guard yes; exact Master authority and typed specialization not established |

48/48 primary targets exactly once。sub-burden tablesはこの48件の再分割であり新たなprimary CLMではない。CLM001のlandscape namingとCLM015のconvergence、CLM007のlocal thresholdとCLM017のfelt understandingを別のburdenとして読む。NOのCLM004/011/044でも命名/文言/式が存在しないという意味ではない。要求されるindependent activity/time/typed identity supportが未発見という意味。

## 6. Evidence inventory

| EVID | Actual support source | Locator | Evidence type | Independence | Limit |
| --- | --- | --- | --- | --- | --- |
| CT-EVID-001 | convolution | CT-EQF-001;Phase01 raw ledger | E0/E1 | INTERNAL SAME MODEL | expression present; typed completeness/proof/empirical identity not entailed |
| CT-EVID-002 | balance | CT-EQF-002;Phase01 raw ledger | E1 | INTERNAL SAME MODEL | expression present; typed completeness/proof/empirical identity not entailed |
| CT-EVID-003 | flow | CT-EQF-003;Phase01 raw ledger | E1 | INTERNAL SAME MODEL | expression present; typed completeness/proof/empirical identity not entailed |
| CT-EVID-004 | force | CT-EQF-004;Phase01 raw ledger | E1 | INTERNAL SAME MODEL | expression present; typed completeness/proof/empirical identity not entailed |
| CT-EVID-005 | source decomposition | CT-EQF-005;Phase01 raw ledger | E0/E1 | INTERNAL SAME MODEL | expression present; typed completeness/proof/empirical identity not entailed |
| CT-EVID-006 | drive | CT-EQF-006;Phase01 raw ledger | E1 | INTERNAL SAME MODEL | expression present; typed completeness/proof/empirical identity not entailed |
| CT-EVID-007 | dissipation | CT-EQF-007;Phase01 raw ledger | E1 | INTERNAL SAME MODEL | expression present; typed completeness/proof/empirical identity not entailed |
| CT-EVID-008 | barrier | CT-EQF-008;Phase01 raw ledger | E1 | INTERNAL SAME MODEL | expression present; typed completeness/proof/empirical identity not entailed |
| CT-EVID-009 | token coupling | CT-EQF-009;Phase01 raw ledger | E1 | INTERNAL SAME MODEL | expression present; typed completeness/proof/empirical identity not entailed |
| CT-EVID-010 | sedimentation limit | CT-EQF-010;Phase01 raw ledger | E1 | INTERNAL SAME MODEL | expression present; typed completeness/proof/empirical identity not entailed |
| CT-EVID-011 | concept predicate | CT-EQF-011;Phase01 raw ledger | E0/E1 | INTERNAL SAME MODEL | expression present; typed completeness/proof/empirical identity not entailed |
| CT-EVID-012 | understanding predicate | CT-EQF-012;Phase01 raw ledger | E0/E1 | INTERNAL SAME MODEL | expression present; typed completeness/proof/empirical identity not entailed |
| CT-EVID-013 | positivity | CT-EQF-013;Phase01 raw ledger | E1 | INTERNAL SAME MODEL | expression present; typed completeness/proof/empirical identity not entailed |
| CT-EVID-014 | vocabulary | CT-EQF-014;Phase01 raw ledger | E0/E1 | INTERNAL SAME MODEL | expression present; typed completeness/proof/empirical identity not entailed |
| CT-EVID-015 | variable-role table / inline guards | S00:83–96;S04:14–89;24 INLINE families | E0/E1 | INTERNAL SAME CLAIM | I,C,Phi,J_I,tau role assignments, not independent maps |
| CT-EVID-016 | Q/re-addressability and primitive exclusions | S04:79–119;S05:54–80 | E0/E2 | INTERNAL SAME MODEL | discrete units named; necessity argued verbally |
| CT-EVID-017 | depth/width/curvature/ridge interpretation | S06:21–65 | E2 | INTERNAL SAME MODEL | qualitative semantic attributes/solution classes, no independent analysis |
| CT-EVID-018 | intuitive cognition/ease/communication examples | S03:13–93 | E5 | PHENOMENOLOGICAL EXAMPLE | motivation and illustration, not participant observations |
| CT-EVID-019 | three-stage sedimentation/reinforcement | S07:10–31 | E2 | INTERNAL SAME MODEL | Delta→reinforcement→stabilization narrative |
| CT-EVID-020 | forgetting/recall/overclosure narrative | S07:35–65;S09:31–46 | E2 | INTERNAL SAME MODEL | decay and barrier interpretations, not task results |
| CT-EVID-021 | insight/threshold organization | S07:69–79 | E2/E5 | INTERNAL SAME MODEL | rapid change and subjective suddenness compared; same target restated |
| CT-EVID-022 | individual/social/institution/intelligence argument | S08:10–88;S09:48–55 | E2 | INTERNAL SAME MODEL | qualitative extension; no social dataset |
| CT-EVID-023 | positivity qualifications and proposition prose | S04:26–30;S05:162–185 | E1/E2 | INTERNAL SAME CLAIM | premises/conditional argument; no separate convergence/gradient proof |
| CT-EVID-024 | note correspondence | S10:8–70 | E4/E5 | INTERNAL SAME MODEL | exact note artifact unfixed; explanatory/pedagogical fit not independent data |
| CT-EVID-025 | negative scope | S04:106–119;S09:12–27;S12:29–31/66–71 | E0 | INTERNAL SAME CLAIM | supports authorial exclusions, not positive mechanisms |
| CT-EVID-026 | open-question inventory | S09:59–69;S11:42–64 | E0 | INTERNAL SAME CLAIM | documents missing parameters/maps/individuation/collective theory |
| CT-EVID-027 | FIG001 | figures/fig1_potential_geometry.png;S03:36–41 | E3 | FIGURE ONLY | basins/trajectory schematic |
| CT-EVID-028 | FIG002 | figures/fig2_token_field_coupling.png;S05:66–69 | E3 | FIGURE ONLY | before/after reuse schematic, not simulation |
| CT-EVID-029 | FIG003 | figures/fig3_minimal_recursive_loop.png;S05:105–109 | E3 | FIGURE ONLY | causal recurrence drawing, not dynamical witness |
| CT-EVID-030 | VED four-volume source/citations | S00:84;refs VED_vol1–4;paper/vol1–4 | E4 | INTERNAL OTHER BRANCH | upstream vocabulary only; no CT typed specialization proof |
| CT-EVID-031 | IFGT source/citation | S00:84;S02:44;refs IFGT;Information-Field-Geometry-Theory | E4 | INTERNAL OTHER BRANCH | imported field template, no cognitive/semantic carrier map |
| CT-EVID-032 | current Consciousness comparisons | Con-MAP:6–12/20–26;Con-LOOP:61/132 | E4 | INTERNAL OTHER BRANCH | explicit nonvalidation/no shared quantity; no transfer of ceiling |
| CT-EVID-033 | Intelligence Part II navigation/homology | Int2-I:104/243;Int2-B:5/21–26 | E4 | INTERNAL OTHER BRANCH | formal-role analogy not CT proof |
| CT-EVID-034 | Thelen/Smith bibliographic anchor | refs.bib:thelen1994dynamic;S11:10–18 | E6 | EXTERNAL LITERATURE | cognitive-attractor conceptual precedent only; contents not externally retrieved |
| CT-EVID-035 | Friston bibliographic anchor | refs.bib:friston2010free;S11:30–37 | E6 | EXTERNAL LITERATURE | predictive-processing/free-energy comparison only |
| CT-EVID-036 | Gibson metadata (uncited) | refs.bib:gibson1986 | E6 | EXTERNAL LITERATURE | no actual cite/use located; inventory only, raises no claim ceiling |
| CT-EVID-037 | EN distribution and build byproducts | main.pdf;main.bbl/aux/log/toc/out/blg | E0 | INTERNAL SAME CLAIM | presentation/documentary duplicates, not additional theoretical evidence |
| CT-EVID-038 | JA working counterpart | conceptual_topography_ja.md | E0/E1/E2 | INTERNAL SAME MODEL | noncanonical parallel/stronger text; not replication; evidence IDs above group duplicate formulas |
| CT-EVID-039 | README authority/notation | README.md Variable Convention | E0/E4 | INTERNAL SAME MODEL | scope/provenance; Master v2.1 exact authority unresolved |
| CT-EVID-040 | distributional semantics comparison | S11:20–28 | E2 | INTERNAL SAME MODEL | named comparator without dedicated citation, not operational embedding pipeline |

40 registry entriesはartifact/argument provenanceの台帳であり40 independent experimentsではない。EVID030はVED4巻を一つのreference familyにまとめる。EVID036未引用metadata、EVID037distribution、EVID038JAworkingは追加validationに数えない。

## 7. Evidence independence

| Independence class | Registry count | Interpretation |
| --- | --- | --- |
| INTERNAL SAME CLAIM | 5 | 同じsource/figure/modelの反復を独立証拠へ加算しない。 |
| INTERNAL SAME MODEL | 24 | 同じsource/figure/modelの反復を独立証拠へ加算しない。 |
| INTERNAL OTHER BRANCH | 4 | 同じsource/figure/modelの反復を独立証拠へ加算しない。 |
| EXTERNAL LITERATURE | 3 | 3登録のうちactual cited2、uncited1。独立CT dataではない。 |
| PHENOMENOLOGICAL EXAMPLE | 1 | 同じsource/figure/modelの反復を独立証拠へ加算しない。 |
| FIGURE ONLY | 3 | 同じsource/figure/modelの反復を独立証拠へ加算しない。 |
| NONE | 0 | 不足はE7–E12 absenceとして扱い、架空supportを登録しない。 |

同一式→figure→JA→PDFの再掲は独立性を増やさない。L1 noteがmodelを動機づけ、CTがnoteへ形式語彙を戻すことはindependent confirmationではない。Con/IntのreuseもE4でありE8/E11ではない。

## 8. Evidence ceiling

| Level | Definition | Exclusive primary claims | Members |
| --- | --- | --- | --- |
| CE0 | definitions/formal text only | 10 | CT-CLM-001, CT-CLM-004, CT-CLM-007, CT-CLM-011, CT-CLM-022, CT-CLM-033, CT-CLM-034, CT-CLM-036, CT-CLM-045, CT-CLM-046 |
| CE1 | internal structure/repository correspondence | 36 | CT-CLM-002, CT-CLM-003, CT-CLM-005, CT-CLM-008, CT-CLM-009, CT-CLM-010, CT-CLM-012, CT-CLM-013, CT-CLM-014, CT-CLM-015, CT-CLM-016, CT-CLM-017, CT-CLM-018, CT-CLM-019, CT-CLM-020, CT-CLM-021, CT-CLM-023, CT-CLM-024, CT-CLM-025, CT-CLM-026, CT-CLM-027, CT-CLM-028, CT-CLM-029, CT-CLM-030, CT-CLM-031, CT-CLM-032, CT-CLM-035, CT-CLM-037, CT-CLM-038, CT-CLM-039, CT-CLM-040, CT-CLM-041, CT-CLM-043, CT-CLM-044, CT-CLM-047, CT-CLM-048 |
| CE2 | externally cited conceptual/literature support | 2 | CT-CLM-006, CT-CLM-042 |
| CE3 | operational variable mapping | 0 | — |
| CE4 | empirical data | 0 | — |
| CE5 | replication/independent validation | 0 | — |
| CE6 | held-out/predictive validation | 0 | — |

CE0 10 / CE1 36 / CE2+ 2（全てCE2、CE3–CE6は0）。exclusive highest level: CE2。

CEはclaim内で実際に所在する最も高いsupport-typeの上限であり、mixed claim全体がそのburdenを満たしたという意味ではない。CLM006のattractor precedentとCLM042のpredictive-processing比較だけにactual external anchorsを対応づけた。文献本文/外部dataは未取得・未検証。E6 metadataをE8に変換しない。repository全体には他branchのsimulationがあるが、CTのobservable/typed mapにつながる証拠としては未発見。

## 9. Semantic ceiling

| Level | Meaning | Exclusive member count | Primary members |
| --- | --- | --- | --- |
| SE0 | semantic labels/definitions | 2 | CT-CLM-001, CT-CLM-022 |
| SE1 | internal semantic coherence/comparison | 17 | CT-CLM-003, CT-CLM-009, CT-CLM-014, CT-CLM-015, CT-CLM-016, CT-CLM-018, CT-CLM-019, CT-CLM-020, CT-CLM-021, CT-CLM-025, CT-CLM-029, CT-CLM-030, CT-CLM-035, CT-CLM-037, CT-CLM-041, CT-CLM-043, CT-CLM-044 |
| SE2 | external semantic/concept literature reference | 1 | CT-CLM-006 |
| SE3 | operational semantic mapping | 0 | — |
| SE4 | empirical semantic task/data | 0 | — |
| SE5 | independent validation | 0 | — |

Semantic ceiling: SE2。ただしS11:10–13のconcept-as-attractorという概念的先例の引用に限定し、external semantic task/resultを意味しない。positive/mixed SEM20件を母集団とし、純negative CLM045を除外。distributional semanticsは名前だけでdedicated citeなし。SE3–5未発見。

## 10. Cognitive ceiling

| Level | Meaning | Exclusive member count | Primary members |
| --- | --- | --- | --- |
| COG0 | cognitive labels/examples | 2 | CT-CLM-004, CT-CLM-007 |
| COG1 | internal structural interpretation | 22 | CT-CLM-002, CT-CLM-008, CT-CLM-010, CT-CLM-012, CT-CLM-013, CT-CLM-014, CT-CLM-017, CT-CLM-019, CT-CLM-020, CT-CLM-021, CT-CLM-023, CT-CLM-024, CT-CLM-025, CT-CLM-027, CT-CLM-028, CT-CLM-029, CT-CLM-032, CT-CLM-035, CT-CLM-037, CT-CLM-038, CT-CLM-039, CT-CLM-047 |
| COG2 | external cognitive literature reference | 1 | CT-CLM-042 |
| COG3 | operational task mapping | 0 | — |
| COG4 | behavioral/neural data | 0 | — |
| COG5 | independent validation | 0 | — |

Cognitive ceiling: COG2。S11 Friston/Thelenの背景比較まで。positive/mixed FUNC25件（pure model-subject exclusion CLM046除外）。CLM042の背景citeはCT error-minimization mechanismを支持しない。COG3–5未発見。

## 11. Phenomenal ceiling

| Level | Meaning | Exclusive member count | Primary members |
| --- | --- | --- | --- |
| PCE0 | phenomenological naming/example | 1 | CT-CLM-011 |
| PCE1 | structured internal correspondence | 1 | CT-CLM-009 |
| PCE2 | comparative phenomenological organization | 5 | CT-CLM-010, CT-CLM-017, CT-CLM-025, CT-CLM-026, CT-CLM-032 |
| PCE3 | operational phenomenal proxy | 0 | — |
| PCE4 | participant/behavioral data tied to model | 0 | — |
| PCE5 | independent validation | 0 | — |

Phenomenal ceiling: PCE2。S03のease/difficulty、S07のsubthreshold/sudden change、S09のrigidity/instabilityを比較配置する範囲。positive PHEN7件（pure negative CLM033除外）。PCE2は比較された例の構成であってparticipant protocolではない。PCE3–5未発見。Consciousnessのceilingを輸入していない。

## 12. Formal support audit

| CT-FORMALSUP | Aspect / source | Required burden | Current support / gap |
| --- | --- | --- | --- |
| CT-FORMALSUP-001 | CT-EQF-001 convolution;S04:33–40 | B0/B1 | 式あり。K/domain/measure/boundary未指定。CTで使用するimported template。 |
| CT-FORMALSUP-002 | CT-EQF-002 balance;S05:11 | B1/B2 | 式あり。初期境界条件・解空間・well-posedness proof未提示。 |
| CT-FORMALSUP-003 | CT-EQF-003 flow;S05:16 | B1/B2 | 式あり。JI vector/field/pathを接続するsignatureはPARTIAL。 |
| CT-FORMALSUP-004 | CT-EQF-004 force;S05:16 | B1/B2 | 式あり。convolutionとlocal approximationの使用範囲・同値条件の完全指定なし。 |
| CT-FORMALSUP-005 | CT-EQF-005 source decomposition;S05:21 | B0/B1 | 分解定義あり。全項を測定sourceへ変換する規則とは別。 |
| CT-FORMALSUP-006 | CT-EQF-006 drive;S05:27–32 | B1/B2 | 式あり。Delta/input・係数のcalibration、具体解なし。 |
| CT-FORMALSUP-007 | CT-EQF-007 dissipation;S05:27–32;S07:35–45 | B1/B2 | 式および反復使用あり。forgetting consequenceの証明・測定なし。 |
| CT-FORMALSUP-008 | CT-EQF-008 barrier;S05:27–50 | B1/B2 | reciprocal termあり。C_*（下付きstar）とCmaxの区別あり。硬いboundの力学的到達不能証明とは区別。 |
| CT-FORMALSUP-009 | CT-EQF-009 token coupling;S05:84–92 | B1/B2 | L_eff expressionあり。ell_i/common vector space/dot product/action signature未完。 |
| CT-FORMALSUP-010 | CT-EQF-010 sedimentation;S05:114–122 | B1/B2 | limit notationあり。convergence notion/proof/initial conditions未提示。非unique/nonstatic qualificationあり。 |
| CT-FORMALSUP-011 | CT-EQF-011 concept;S05:126–135 | B0/B1 | 明示definitionあり。small perturbationのnorm/time horizon、individuation未指定。 |
| CT-FORMALSUP-012 | CT-EQF-012 understanding;S05:138–152 | B0/B1 | region integralとthetaのdefinitionあり。domain/measure/thresholdの具体指定なし。 |
| CT-FORMALSUP-013 | CT-EQF-013 positivity;S05:158–185 | B1/B2 | propositionと前提・非pointwise guardあり。fの完全仕様・gradient consequenceの独立導出未提示。正誤は判定しない。 |
| CT-FORMALSUP-014 | CT-EQF-014 vocabulary;S06:70–82 | B0/B1 | set comprehensionあり。S numeric rule/epsilon calibration、prose distributionとの対応未指定。 |

14/14 EQF。式の存在はE1 artifact、証明完了の認定ではない。全signatureはPhase01のまま。図しかない正式方程式familyはなく、図は独立formal proofではない。

## 13. Token coupling burden

| CT-BURDEN-COUPLING | Aspect / source | Required burden | Current support / gap |
| --- | --- | --- | --- |
| CT-BURDEN-COUPLING-001 | discrete units necessary;CLM012;S05:54–60 | B1/B2/B4/B8 | qualitative cost argument E2。continuous alternativeの排除条件・comparative taskなし。 |
| CT-BURDEN-COUPLING-002 | coupling expression exists;CLM013;S05:84–88 | B0/B1 | 式存在YES E1。これだけで型・帰結・認知作用をYESにしない。 |
| CT-BURDEN-COUPLING-003 | ell_i dot gradient;Phase01 COUPLING | B1 | ell_i type/common space/sum domain/L type PARTIAL/UNRESOLVED。well-typedness verdictなし。 |
| CT-BURDEN-COUPLING-004 | each reuse reinforces gradient;S05:89–92;S07:24–25 | B1/B2/B5 | term E1 + causal prose E2 + FIG002 E3。符号/更新規則/解による帰結証明なし。 |
| CT-BURDEN-COUPLING-005 | deepens well / lowers cost;CLM013/023 | B2/B4/B5/B7 | geometry explanationあり。認知cost estimator・model-specific causal supportなし。 |
| CT-BURDEN-COUPLING-006 | self-sustaining concept;S07:27–31 | B2/B4/B9 | stages/feedback E2。stability witness/task/prospective resultなし。 |
| CT-BURDEN-COUPLING-007 | first token / basin / Q;Phase03 bootstrap | B1/B2/B4 | Q namingとco-development narrative。初期生成規則未指定、bootstrap未解消。 |
| CT-BURDEN-COUPLING-008 | empirical coupling support;CLM013/023 | B7/B8/B9 | CT対応E7/E8/E9/E10未発見。図はデータではない。 |


## 14. Understanding burden

| CT-BURDEN-UNDER | Aspect / source | Required burden | Current support / gap |
| --- | --- | --- | --- |
| CT-BURDEN-UNDER-001 | local threshold;CLM007;S05:138–152 | B0/B1 | definition E0/E1あり。region/metric/theta指定は未完。 |
| CT-BURDEN-UNDER-002 | cognitive understanding;CLM007/017 | B4/B7/B8 | 名前・internal interpretationあり。独立理解課題/正答以外の機能criterionも未指定。 |
| CT-BURDEN-UNDER-003 | felt ease;CLM010/017;S03:13–28;S10:28/51–53 | B6/B7/B8 | E5例とcost対応E2。participant reports/proxy validityなし。 |
| CT-BURDEN-UNDER-004 | durability;S07:27–31;S09:40–46 | B2/B4/B5/B9 | stable terrain説明。独立保持/転移criterion・継時dataなし。 |
| CT-BURDEN-UNDER-005 | failure/pathology;CLM032;S09:31–46 | B4/B6/B7/B8 | over/underclosureのqualitative contrast。診断基準/clinical or cognitive testなし。 |
| CT-BURDEN-UNDER-006 | semantic correctness excluded;S09:12–16;S10:40–53 | B0;positive reading B4/B6 | 否定scopeはsource-supported。correctnessを扱わないことはfelt/cognitive criterionを供給しない。CT-SERIOUS-001 RETAIN。 |


## 15. Insight burden

| CT-BURDEN-INSIGHT | Aspect / source | Required burden | Current support / gap |
| --- | --- | --- | --- |
| CT-BURDEN-INSIGHT-001 | topology merger/split/displacement;S07:49–53 | B1/B2/B3 | qualitative geometric alternatives。topology/invariant/update specificationなし。 |
| CT-BURDEN-INSIGHT-002 | cognitive resolution;CLM025;S07:69–75 | B4/B7/B8 | insight correspondence E2/E5。独立resolution endpointなし。 |
| CT-BURDEN-INSIGHT-003 | subjective suddenness;CLM026;S07:76–79 | B6/B7/B8 | threshold organizationあり。felt eventの独立判定・同期dataなし。 |
| CT-BURDEN-INSIGHT-004 | bifurcation/threshold explanation;CT-SERIOUS-002 | B1/B2/B5/B6 | 二つのthresholdがproseにあるだけで知覚変換証明とはしない。独立bridge未発見、RETAIN。 |


## 16. Institution burden

| CT-BURDEN-INST | Aspect / source | Required burden | Current support / gap |
| --- | --- | --- | --- |
| CT-BURDEN-INST-001 | attractor analogy;CLM030;S08:56–60 | B0/B2 | qualitative analogy E2は存在。 |
| CT-BURDEN-INST-002 | institution identity;S08:59–61 | B3/B7/B8/B11 | 制度の外部識別とcollective field mapなし。 |
| CT-BURDEN-INST-003 | stability follows depth;CLM031;S08:62–63 | B2/B5/B7/B8/B11 | depth説明E2。depthを安定性以外から推定する規則・causal comparisonなし。 |
| CT-BURDEN-INST-004 | coordinated perturbation sufficient;S08:64–65 | B2/B5/B7/B11 | threshold narrative。collective units/perturbation scale/threshold未指定。 |
| CT-BURDEN-INST-005 | historical difficulty;S08:65–66 | B8/B11/B12 | history一般への説明語。CT対応case/data/citation anchorなし。 |
| CT-BURDEN-INST-006 | institution evidence and serious status | B8/B11 | institutional dataset0。CT-SERIOUS-003 RETAIN、absenceだけでESCALATEDにしない。 |


## 17. Thought / flow burden

| CT-BURDEN-THOUGHT | Aspect / source | Required burden | Current support / gap |
| --- | --- | --- | --- |
| CT-BURDEN-THOUGHT-001 | JI field;S05:16 | B1 | formal expression E1。signature PARTIAL。 |
| CT-BURDEN-THOUGHT-002 | field to trajectory;S03:46–50;S04:64–66 | B1/B4 | path realization/initial value/trajectory extraction未指定。 |
| CT-BURDEN-THOUGHT-003 | thought identity;CLM008;S02:81–83 | B4/B7/B8 | interpretation/FIG001。独立thought-path criterionなし。 |
| CT-BURDEN-THOUGHT-004 | habitual thought;S06:24;S10:29 | B2/B4/B8 | limit-cycle analogy、observed recurrent thoughtとのmapなし。 |
| CT-BURDEN-THOUGHT-005 | blocked thought;S06:25;S09:31–38 | B4/B5/B7/B8 | barrier correspondence。逆診断はsource未実装、C6 risk保持。 |


## 18. Tau / experiential time burden

| CT-BURDEN-TIME | Aspect / source | Required burden | Current support / gap |
| --- | --- | --- | --- |
| CT-BURDEN-TIME-001 | derivative/evolution parameter;S05 equations | B1 | formal tauあり。unit/clock/sequence extraction未指定。 |
| CT-BURDEN-TIME-002 | irreversible order;S04 table;FIG003 | B1/B2 | ordered cycleの説明、不可逆性の導出/observableなし。 |
| CT-BURDEN-TIME-003 | experiential time;CLM011;S04:76–78 | B6/B7/B8 | 同一rowでnamingのみ。felt timing独立criterionなし。 |
| CT-BURDEN-TIME-004 | sudden/social time;S07:76–79;S08 | B6/B7/B10/B11 | perceptual thresholdとcollective extensionあり、common clock/Con tau equalityなし。calibration新設しない。 |


## 19. Positivity burden

| CT-BURDEN-POS | Aspect / source | Required burden | Current support / gap |
| --- | --- | --- | --- |
| CT-BURDEN-POS-001 | EN I>0;S05:158–164 | B1 | f/Cboundを前提としたformula/proseあり。全f条件・proof completeness未確認。 |
| CT-BURDEN-POS-002 | EN conceptual nonclosure;S05:168–177 | B2/B3 | framework proposition E1/E2。semantic closure独立criterionなし。 |
| CT-BURDEN-POS-003 | EN gradient availability;S04:28–30;S05:168–177 | B1/B2 | asymmetry/inhomogeneity/boundary付き。pointwise implicationは明示否定。 |
| CT-BURDEN-POS-004 | EN flow availability | B1/B2 | JI relationあり。gradient availabilityから個別flowを導く完全条件未指定。 |
| CT-BURDEN-POS-005 | EN open learning;S05:180–185 | B4/B7/B9 | local quiescenceとnew perturbation/wider windowのqualitative possibility。学習課題なし。 |
| CT-BURDEN-POS-006 | JA generic positivity chain;JA167/280–284 | B1/B2/B3 | working stronger implication。EN条件を自動移植して救済しない。 |
| CT-BURDEN-POS-007 | EN social innovation;S08:83–88 | B4/B9/B11 | 条件付きpossibility、social observable/testなし。 |
| CT-BURDEN-POS-008 | JA always residual gradient/social innovation;JA430 | B1/B4/B9/B11/B12 | working stronger guarantee。追加derivation/dataなし、ENと別burden。 |


## 20. Barrier burden

| CT-BURDEN-BARRIER | Aspect / source | Required burden | Current support / gap |
| --- | --- | --- | --- |
| CT-BURDEN-BARRIER-001 | reciprocal term;S05:27–32 | B1 | 式あり、domain/end-point dynamicsは未完。 |
| CT-BURDEN-BARRIER-002 | effective resistance;S05:46–50 | B2 | projected interpretation/guardあり。 |
| CT-BURDEN-BARRIER-003 | hard prohibition;JA236/374 | B1/B2 | EN effectiveと異なるworking強度。blow-up term≠証明済みunreachable bound。 |
| CT-BURDEN-BARRIER-004 | belief resistance;CLM027;S07:55–65 | B4/B5/B7/B8 | qualitative explanation、behavior mapping/dataなし。 |
| CT-BURDEN-BARRIER-005 | overclosure pathology;CLM032;S09:31–38 | B4/B7/B8 | relative-source regime命名、clinical criterionなし。 |
| CT-BURDEN-BARRIER-006 | social perturbation threshold;S08:64–66 | B5/B7/B11 | collective depth comparisonのみ。社会metric/causal evidenceなし。 |


## 21. Phi-star / sedimentation burden

| CT-BURDEN-SED | Aspect / source | Required burden | Current support / gap |
| --- | --- | --- | --- |
| CT-BURDEN-SED-001 | asymptotic expression;CLM015;S05:114 | B1 | limit notation E1。convergence space/norm/theorem未提示。 |
| CT-BURDEN-SED-002 | attractor/stability;S05:119–122 | B1/B2 | name/qualificationあり。solution/stability proofなし。 |
| CT-BURDEN-SED-003 | nonunique/nonstatic;CLM016 | B1/B2 | EN not necessarily / JA categorical wording。time-dependent targetの意味未固定。 |
| CT-BURDEN-SED-004 | history terrain;S07:10–31 | B2/B3 | update narrative E2。history→field estimatorなし。 |
| CT-BURDEN-SED-005 | memory/learning;CLM023/024 | B4/B5/B7/B8 | independent memory/learning criterion/task/dataなし。 |
| CT-BURDEN-SED-006 | stable concept;S05:126–135;S07:27–31 | B0/B1/B3/B4 | localdefinitionあり。concept individuation/retention mappingは別burden。 |


## 22. Meaning burden

| CT-BURDEN-MEANING | Aspect / source | Required burden | Current support / gap |
| --- | --- | --- | --- |
| CT-BURDEN-MEANING-001 | intrinsic token meaning denied;CLM045;S04:110–119 | B0 | local primitive exclusion supported。positive semanticsを証明しない。 |
| CT-BURDEN-MEANING-002 | meaning=available trajectories;CLM009;S03:64–65 | B0/B3/B7 | local interpretationあり。independent semantic equivalence criterionなし。 |
| CT-BURDEN-MEANING-003 | semantic drift;CLM021;S06:53–65 | B3/B4/B5/B8 | ridge mechanism narrative。drift corpus/task対応なし。 |
| CT-BURDEN-MEANING-004 | depth/experienced meaning;S10:48–53;JA141 | B3/B6 | note interpretation E4/E5。meaningの独立semantic/phenomenal endpointなし。 |
| CT-BURDEN-MEANING-005 | distributional semantics;CLM041;S11:20–28 | B3/B7 | conceptual comparisonのみ。dedicated citationなし、co-occurrence/historyの実測比較なし。 |


## 23. Concept burden

| CT-BURDEN-CONCEPT | Aspect / source | Required burden | Current support / gap |
| --- | --- | --- | --- |
| CT-BURDEN-CONCEPT-001 | basin naming;CLM006;S05:126–135 | B0 | local definition E0 yes。外部semantic identityとは別。 |
| CT-BURDEN-CONCEPT-002 | low gradient condition | B1 | formal predicateあり。approximation tolerance/context未指定。 |
| CT-BURDEN-CONCEPT-003 | perturbation stability | B1/B2 | stability clauseあり。norm/time horizon/solutionなし。 |
| CT-BURDEN-CONCEPT-004 | depth=resistance;S06:35–37 | B3/B4/B7 | formal depth名とinterpretation。resistance measurementなし。 |
| CT-BURDEN-CONCEPT-005 | width=context;S06:39–41 | B3/B7 | context scope独立mapなし。 |
| CT-BURDEN-CONCEPT-006 | curvature=precision;S06:43–45 | B3/B4/B7 | sharp/fuzzy contrastのみ。semantic precision estimatorなし。 |
| CT-BURDEN-CONCEPT-007 | ridge/category/individuation;S06:53–65;S11:48–52 | B1/B3/B7 | ridge analogyと未指定宣言。概念単位の外部criterionなし。 |


## 24. Collective / social burden

| CT-BURDEN-SOCIAL | Aspect / source | Required burden | Current support / gap |
| --- | --- | --- | --- |
| CT-BURDEN-SOCIAL-001 | same dynamics;CLM028;S08:8–38 | B1/B10/B11/B12 | cost-shift argument E2。共通state/aggregation/mapなし。 |
| CT-BURDEN-SOCIAL-002 | correlated wells;CLM029;S08:42–46 | B2/B3/B7/B8/B11 | prior/sharedinput condition。similarity/well correlation estimatorなし。 |
| CT-BURDEN-SOCIAL-003 | shared semantic domain;S08:47–52 | B3/B7/B11 | shared terrain説明、common domain未指定。 |
| CT-BURDEN-SOCIAL-004 | collective Phi;S08;S11:54–58 | B1/B10/B11 | glyph reuseのみでagent index/common K/tauは補わない。formalization future。 |
| CT-BURDEN-SOCIAL-005 | norm/institution;CLM030/031 | B5/B8/B11 | attractor analogyとdepth説明のみ。 |
| CT-BURDEN-SOCIAL-006 | collective intelligence;CLM039 | B0/B4/B8/B11/B12 | functional definition yes、一般intelligence能力への独立mappingなし。 |
| CT-BURDEN-SOCIAL-007 | innovation;S08:83–88;JA430 | B4/B9/B11 | EN条件付きdirection/JA guarantee差。prospective testなし。 |
| CT-BURDEN-SOCIAL-008 | communication/polarization;CLM014/035;S09:48–55 | B3/B5/B8/B9/B11 | qualitative success/failure contrast、behavior/social dataなし。 |


## 25. Physical / concept cross-scale burden

| CT-BURDEN-XPHYS | Aspect / source | Required burden | Current support / gap |
| --- | --- | --- | --- |
| CT-BURDEN-XPHYS-001 | EN projected regimes;CLM043;S12:61–71 | B0/B10 | comparison/nonidentity guardあり。typed translationなし。 |
| CT-BURDEN-XPHYS-002 | same generative grammar | B1/B10/B12 | internal shared notation/convention E4。domain/invariant preserved mapなし。 |
| CT-BURDEN-XPHYS-003 | JA same information field/equation solution classes;CLM044;JA575–576 | B1/B3/B10/B12 | working identity burden。source/target solutionsを結ぶruleなし。 |
| CT-BURDEN-XPHYS-004 | Q quantization isomorphism;CLM040;S04:94–101 | B1/B10 | explicit analogy/no quantum claim guard。mathematical isomorphism dataなし。 |
| CT-BURDEN-XPHYS-005 | upstream inheritance/grounding;CLM048;S00;S11:14–18 | B1/B10 | VED/IFGT source referencesは追跡可能。closed upstream≠CT derivation。8 upstream OPEN bridgesを閉じない。 |


## 26. Consciousness cross-reference burden

| CT-BURDEN-CON | Aspect / source | Required burden | Current support / gap |
| --- | --- | --- | --- |
| CT-BURDEN-CON-001 | CT future CPU/GPU fast/slow;CLM038;S10:54–56 | B4/B10;documentary identity | E4 correspondence/navigation。exact future note/version未固定。 |
| CT-BURDEN-CON-002 | CT subjective access referral;S09:18–22 | B0 for scope;B6 for positive map | future companion reference。独立phenomenal supportなし。 |
| CT-BURDEN-CON-003 | current Con token/terrain/gradient/insight comparisons | B10/B6 | Con-MAP:6–26;Con-LOOP:61/132;Con-TCA:140–147。明示comparison/nonvalidation。CTの正当化に流用しない。 |
| CT-BURDEN-CON-004 | reciprocal authority independence | B8/B10 | E4 INTERNAL OTHER BRANCH。model-specific independent data/proofは未発見。CT文言の修正はしない。 |


## 27. Intelligence cross-reference burden

| CT-BURDEN-INT | Aspect / source | Required burden | Current support / gap |
| --- | --- | --- | --- |
| CT-BURDEN-INT-001 | CT direct implications/collective function;S05:180;S08:70–81 | B4/B11/B12 | architectural/function interpretation。downstreamをevidenceにしていない。 |
| CT-BURDEN-INT-002 | Intelligence Part II homology;Int2-I:104/243;Int2-B:5/21–26 | B10 | E4 proposed comparison/representation tree。typed state-space translationなし。 |
| CT-BURDEN-INT-003 | reciprocal navigation vs validation | B8/B10 | 内部reuseは独立CT validationではない。IntelligenceのデータをCTへ接続するrule未発見。 |


## 28. External literature role

| CT-LIT | Bib key / actual locator | Role / evidence | Burden limit |
| --- | --- | --- | --- |
| CT-LIT-001 | VED_vol1;S00:84;S02:10/41 | internal foundation E4; cited | CT導出/empirical mapにはならない。 |
| CT-LIT-002 | VED_vol2;S00:84 | internal series E4; cited | Bibliography titleのみをcurrent exact versionと同定しない。 |
| CT-LIT-003 | VED_vol3;S00:84 | internal series E4; cited | 異分野引用をCT dataとしない。 |
| CT-LIT-004 | VED_vol4;S00:84 | internal series E4; cited | historical title/current version照合はPhase00のまま未固定。 |
| CT-LIT-005 | IFGT;S00:84;S02:10/44 | formal framework reuse E4; cited | 式/用語のsource support、typed CT specializationは別。 |
| CT-LIT-006 | thelen1994dynamic;S11:10–18 | conceptual precedent/background E6; cited | 本文がconcept-as-attractorの先例として引用。CT固有coupling/semantic taskの検証ではない。文献本文は未取得。 |
| CT-LIT-007 | friston2010free;S11:30–37 | cognitive background/comparison E6; cited | prediction-error/free-energy比較。CT変数への測定map/empirical resultは本文にない。文献内容を推測しない。 |
| CT-LIT-008 | gibson1986;refs.bibのみ | metadata; uncited | 使用箇所未発見。外部先例の実supportとしてCE2へ加算しない。 |

8 entries / 7 unique cited keys / unresolved cite keys 0。VED/IFGT5件はinternal。他の3件のうち実際のexternal anchorは2件。6 cite commands、11 key occurrencesは同一文献の反復であり独立証拠数ではない。Con/Int/noteはprose reference、bib keysなし。

## 29. Figure evidence

| CT-EVID-FIG | Figure / source | Class / independence | What it cannot establish |
| --- | --- | --- | --- |
| CT-EVID-FIG-001 | CT-FIG-001;S03 caption;EVID027 | E3 formal/semantic illustration; FIGURE ONLY | basin/concept、JI/thoughtを描く。data/simulation outputとするsource記載なし。 |
| CT-EVID-FIG-002 | CT-FIG-002;S05 coupling caption;EVID028 | E3 mechanism schematic; FIGURE ONLY | before/after deepeningは想定帰結の図示。executed dynamics/causal witnessなし。 |
| CT-EVID-FIG-003 | CT-FIG-003;S05 loop caption;EVID029 | E3 functional/causal schematic; FIGURE ONLY | ordered loop/irreversible causality labelはproof/dataではない。bare J vs caption JIは未修正。 |

3 PNGを今回再表示して確認。図形/軸/矢印は測定系列やsimulation resultへ昇格しない。PDFは再生成しない。

## 30. Prediction inventory

| CT-PRED | Source / linked claim | Source-suggested direction | Kind | Numerical / executable / operationalized / tested / validated | Falsifiable in principle |
| --- | --- | --- | --- | --- | --- |
| CT-PRED-001 | S05:89–92;S07:24–25;CLM013/023 | reuse→gradient reinforcement/deeper wells | directional | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-002 | S07:27–31;CLM023 | deepening→lower cost/self-sustaining concept | directional | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-003 | S07:35–43;CLM024 | less reinforcement/relaxation→shallower less accessible concepts | directional | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-004 | S07:43–45;CLM024 | recall/reuse→redeepening | directional | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-005 | S06:39–45;CLM020 | width/context;curvature/precision contrast | comparative | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-006 | S06:58–65;CLM021 | token use reinforces/erodes ridges;semantic drift | qualitative | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-007 | S07:55–65;CLM027 | perturbation/depth threshold and belief revision | directional | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-008 | S07:69–79;CLM025/026 | rapid topology/perceptual threshold and insight | qualitative/threshold | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-009 | S09:31–38;CLM032 | overclosure→rigidity/repetitive thought | directional | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-010 | S09:40–46;CLM032 | underclosure→unstable thought/lack of durable understanding | directional | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-011 | S03:78–80;CLM014 | sufficiently similar landscapes→communication | comparative | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-012 | S08:42–52;CLM029 | shared perturbations/similar priors→correlated wells | directional | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-013 | S08:62–66;CLM031 | collective depth/coordinated perturbations→stability/change | directional | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-014 | S09:48–55;CLM035 | divergence/manipulation→sync failure/conflict/polarization | directional | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-015 | S05:180–185;S08:83–88;CLM018 | new perturbations/wider windows can reactivate differentiation/innovation | conditional qualitative | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-016 | JA167/280–284/430;CLM019 | generic residual gradient/always innovation | working stronger direction | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-017 | S09:62–66;S11:41–46;CLM036 | kernel/parameter estimation from behavioral/linguistic/neural data | future research task | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-018 | S11:48–52;CLM036 | concept individuation criterion | future formal/semantic task | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-019 | S11:54–58;CLM028/036 | multi-agent shared-landscape formation/breakdown formalization | future research task | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-020 | S11:60–64;CLM034 | firing/connectivity/oscillation correspondence | future operational task | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |
| CT-PRED-021 | S09:20–22;S10:54–56;CLM038 | Consciousness companion/fast-slow formalization | future documentary/model task | NO / NO / NO / NO / NO | 方向を比較する余地はあるが独立endpoint未指定;Phase04未判定 |

21 entries = qualitative/directional/comparative families 16 + future-task families 5。後者を完成したpredictionに数えない。全てsource中の帰結・将来課題から抽出し、新しいtest/parameter manipulation/protocolは追加しない。predictionとしてのtruth/final falsifiabilityは未判定。

## 31. Mechanism burden

| CT-MECHBURDEN | Phase02 family / source wording | Required burden | Formal intermediary | Map / observable / causal evidence / alternatives |
| --- | --- | --- | --- | --- |
| CT-MECHBURDEN-001 | CT-MECHLANG-001;S01:18/23/26;JA32–34 generates/deepening/producing | B1/B2/B3/B4/B5 | YES potential/coupling/loop; summary causal wording | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-002 | CT-MECHLANG-002;S02:40/59;JA67/77 generation | B0/B10 | VED description/series label, not a CT cognitive mechanism | upstream/background/formal wording/negative or documentary control。positive cognitive mechanismとして集計しない。guardのB0はsourceで支持。 |
| CT-MECHBURDEN-003 | CT-MECHLANG-003;S02:85–87;S12:33–36;JA93/565 deepening | B2/B4/B5 | YES token-gradient; repeated central claim | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-004 | CT-MECHLANG-004;S03:74–80;JA145–148 deepens / produces similar shifts | B3/B4/B5/B11 | YES wells/trajectory; communication causal account | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-005 | CT-MECHLANG-005;S03:84–93;JA150–155 gives rise to / 生む | B6/B7/B8 | Phi named, but no separate phenomenal intermediary in passage | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-006 | CT-MECHLANG-006;S04:38–40;JA174 produced bias / determines direction | B1/B2/B4 | YES potential/gradient; formal interpretation | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-007 | CT-MECHLANG-007;S04:110–112;JA200 determines cheap/costly | B1/B4 | YES constraint geometry; semantic nonidentity guard | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-008 | CT-MECHLANG-008;S05:20–32;JA220–230 generation term decomposes | B0/B1 | YES explicit source expressions; not itself higher-layer mechanism | upstream/background/formal wording/negative or documentary control。positive cognitive mechanismとして集計しない。guardのB0はsourceで支持。 |
| CT-MECHBURDEN-009 | CT-MECHLANG-009;S05:58–69;FIG002 illustrates mechanism / reinforces / deepens / lowers | B1/B2/B4/B5 | YES coupling term and schematic; illustrative + causal wording | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-010 | CT-MECHLANG-010;S05:89–92;JA247–248 purely dynamical / each reuse | B1/B2/B4/B5 | YES term adjacent; no empirical/typing judgment | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-011 | CT-MECHLANG-011;S05:96–122;JA252–257 approaches / history reshapes | B1/B2/B4 | YES limit/attractor; qualitative evolution language | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-012 | CT-MECHLANG-012;S01:35;S04:30;S05:170/185 generated field | B1/B2/B3 | field adjective under positivity qualification, not a new mechanism family | upstream/background/formal wording/negative or documentary control。positive cognitive mechanismとして集計しない。guardのB0はsourceで支持。 |
| CT-MECHBURDEN-013 | CT-MECHLANG-013;S06:43–45;JA311 curvature produces precision/polysemy | B3/B4/B5 | YES curvature named, no separate semantic conversion stated | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-014 | CT-MECHLANG-014;S06:58–65;JA320–322 reinforces/erodes/mechanistic account | B3/B4/B5 | YES ridge dynamics named; semantic drift causal wording | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-015 | CT-MECHLANG-015;S07:10–18;JA343–348 generates spike/gradient | B1/B2/B4/B5 | YES Delta/source/I/Phi/J_I sequence | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-016 | CT-MECHLANG-016;S07:20–25;JA350–352 ensures deepening | B1/B2/B4/B5 | YES EQ coupling explicitly cited; theorem-like warrant use | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-017 | CT-MECHLANG-017;S07:27–31;JA354–357 deepens/cost decreases/self-sustaining | B2/B4/B5 | YES well/cost/attractor sequence, learning interpretation | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-018 | CT-MECHLANG-018;S07:35–45;JA361–367 forgetting/re-deepening | B2/B4/B5 | YES Gamma C repeated plus Phi relaxation | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-019 | CT-MECHLANG-019;S07:55–65;JA373–375 accounts for belief resistance | B2/B4/B5 | YES barrier; EN effective scope vs JA divergence wording | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-020 | CT-MECHLANG-020;S07:69–79;JA379–382 produce event / subjective reflects | B1/B4/B5/B6 | topology/perceptual thresholds juxtaposed; no separate phenomenal mapping stated | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-021 | CT-MECHLANG-021;S08:18–38;JA394–405 produces inversion | B2/B4/B10/B11 | constraint-cost shift named, not new formal operation | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-022 | CT-MECHLANG-022;S08:42–52;JA408–412 produces correlated deepening/shared terrain | B3/B4/B5/B11 | wells/shared inputs named; aggregate formal treatment deferred | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-023 | CT-MECHLANG-023;S08:56–66;JA416–420 follows from depth/accounts for history | B2/B5/B11 | attractor depth is named intermediary | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-024 | CT-MECHLANG-024;S08:74–81;JA426–428 maintenance/transmit | B0/B4/B11/B12 | landscape/logs named; functional definition/process | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-025 | CT-MECHLANG-025;S09:18–22;JA442 does not generate/explain + future mechanistic basis | B0/B6 | exclusion and companion referral, not positive evidence | upstream/background/formal wording/negative or documentary control。positive cognitive mechanismとして集計しない。guardのB0はsourceで支持。 |
| CT-MECHBURDEN-026 | CT-MECHLANG-026;S09:31–46;JA449–456 can no longer produce / preventing | B2/B4/B5 | source-term dominance→wells→thought/understanding | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-027 | CT-MECHLANG-027;S09:48–55;JA459–460 fail to produce / result | B3/B4/B5/B11 | correlated perturbation failure named | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-028 | CT-MECHLANG-028;S10:21/48–53;JA481/501–502 deepening / correspondence | B3/B4/B6 | Phi/source/cost named; explicit interpretations, not definitions | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-029 | CT-MECHLANG-029;S11:14–18;JA522 grounding / explicit account | B1/B4/B10 | VED/IFGT source attribution; derivation wording recorded only | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-030 | CT-MECHLANG-030;S11:20–28;JA525–528 emerges from coupling | B1/B3/B5 | YES coupling vs co-occurrence comparison | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-031 | CT-MECHLANG-031;S11:30–37;JA530–532 error minimization / generative model | B2/B4/B5 | drive/deepening explicit; Bayesian commitment denied | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-032 | CT-MECHLANG-032;S12:12–18/61–71;JA556/575–576 emerges / generates / grammar | B1/B3/B10/B12 | field/coupling/source comparison named; physical/concept distinction recorded | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |
| CT-MECHBURDEN-033 | CT-MECHLANG-033;JA584/589 英語TeXから生成/反映 | B0 | working source history, not theory mechanism | upstream/background/formal wording/negative or documentary control。positive cognitive mechanismとして集計しない。guardのB0はsourceで支持。 |
| CT-MECHBURDEN-034 | CT-MECHLANG-034;S01:38–40;S02:93–95;S12:44–49;JA43/97/569 same dynamics produce | B2/B4/B5/B10/B11 | summary of S08, no separate formal intermediary added | intermediaryは式/名前/prose/図の範囲。独立mapping・observable・CT因果data未発見。比較文献/病態対比はあるがcontrolled alternative explanation比較はない。B1/B2の強い帰結は未完、B4–B11を式存在だけで満たさない。 |

34/34 crosswalk、positive mechanism-language families 29、control/background families 5。対照も欠落扱いしない。数式介在YESはmechanism検証YESではない。

## 32. Necessity / sufficiency burden

| CT-NSBURDEN | Phase02 NS / source | Claim domain | Required burden | Support boundary |
| --- | --- | --- | --- | --- |
| CT-NSBURDEN-001 | CT-NS-001;S00:89–93;JA18–20 approximation only where stated / strict bound always | explicit scope;YES;—;—;— | B0/B1 | scope/research prerequisite/model-input exclusionはsource-localに支持。現実一般の必要・不可能性を証明しない。 |
| CT-NSBURDEN-002 | CT-NS-002;S02:81–83;JA91 thought does not require directing subject | within CT claim;J_I named;—;YES negative necessity;not subject-count criterion | B0/B2 | scope/research prerequisite/model-input exclusionはsource-localに支持。現実一般の必要・不可能性を証明しない。 |
| CT-NSBURDEN-003 | CT-NS-003;S05:54–58;JA240 continuous field cannot sustain low-cost recursion / discrete units required | context CT, sentence categorical;continuous/discrete;—;YES necessity;— | B1/B2/B4 | formal/model argumentはあるが帰結の完全条件・独立semantic/cognitive/social/phenomenal mapなし。経験的一般必要十分とは認定しない。 |
| CT-NSBURDEN-004 | CT-NS-004;S05:55–56 generically expensive/drift-prone | context CT;field reentry;—;YES qualification;— | B1/B2/B4 | formal/model argumentはあるが帰結の完全条件・独立semantic/cognitive/social/phenomenal mapなし。経験的一般必要十分とは認定しない。 |
| CT-NSBURDEN-005 | CT-NS-005;S05:126–135;JA261–265 concept satisfying slope+stability | explicit Definition;YES conditions;YES local concept;attribute uses later;— | B0/B1 | definition条件はE0/E1。signature/tolerance/criterion未指定分はB1、semantic/phenomenal同定は別burden。 |
| CT-NSBURDEN-006 | CT-NS-006;S05:138–152;JA267–272 understanding threshold | explicit Definition;YES threshold;not correct meaning;YES criterion naming;not direct phenomenal criterion | B0/B1 | definition条件はE0/E1。signature/tolerance/criterion未指定分はB1、semantic/phenomenal同定は別burden。 |
| CT-NSBURDEN-007 | CT-NS-007;S05:162–164;JA278 positivity follows from C bound/f | under-framework;YES implication wording;closure interpretation;—;— | B1/B2 | formal/model argumentはあるが帰結の完全条件・独立semantic/cognitive/social/phenomenal mapなし。経験的一般必要十分とは認定しない。 |
| CT-NSBURDEN-008 | CT-NS-008;S05:168–177;JA280–284 excludes closure/generically | explicit framework; JA stronger;YES positivity;YES conceptual openness;flow availability;— | B1/B2/B3/B4 | formal/model argumentはあるが帰結の完全条件・独立semantic/cognitive/social/phenomenal mapなし。経験的一般必要十分とは認定しない。 |
| CT-NSBURDEN-009 | CT-NS-009;S04:28–30 not by itself guarantee nonzero local gradient | explicit guard;YES pointwise distinction;—;—;— | B1/B2 | formal/model argumentはあるが帰結の完全条件・独立semantic/cognitive/social/phenomenal mapなし。経験的一般必要十分とは認定しない。 |
| CT-NSBURDEN-010 | CT-NS-010;S03:78–80;JA147 sufficiently similar landscapes for communication | framework picture;similarity named, criterion not supplied;YES shared terrain;YES condition;— | B3/B4/B11 | formal/model argumentはあるが帰結の完全条件・独立semantic/cognitive/social/phenomenal mapなし。経験的一般必要十分とは認定しない。 |
| CT-NSBURDEN-011 | CT-NS-011;S07:24–25;JA352 coupling ensures every reuse deepens | model narrative;EQF009 cited;concept stabilization;YES sufficient-sounding causal assurance;— | B1/B2/B4/B5 | formal/model argumentはあるが帰結の完全条件・独立semantic/cognitive/social/phenomenal mapなし。経験的一般必要十分とは認定しない。 |
| CT-NSBURDEN-012 | CT-NS-012;S07:55–56;JA373 perturbation sufficient to overcome depth required | model narrative;depth/perturbation;concept change;YES required+sufficient magnitude wording;— | B2/B4/B5 | formal/model argumentはあるが帰結の完全条件・独立semantic/cognitive/social/phenomenal mapなし。経験的一般必要十分とは認定しない。 |
| CT-NSBURDEN-013 | CT-NS-013;S07:76–79;JA382 threshold crossing then event | model narrative;topology threshold;—;insight context;YES perceptual threshold/suddenness | B1/B4/B6 | formal/model argumentはあるが帰結の完全条件・独立semantic/cognitive/social/phenomenal mapなし。経験的一般必要十分とは認定しない。 |
| CT-NSBURDEN-014 | CT-NS-014;S08:13–22;JA391–395 must reenter/compress/stabilize shared trajectories | under cost assumptions;continuous/discrete costs;shared representation;YES constraints;— | B1/B2/B4/B10/B11 | formal/model argumentはあるが帰結の完全条件・独立semantic/cognitive/social/phenomenal mapなし。経験的一般必要十分とは認定しない。 |
| CT-NSBURDEN-015 | CT-NS-015;S08:44–46;JA409 sufficiently similar priors and repeated shared perturbation | model narrative;wells named;shared landscape;YES conditional emergence;— | B3/B4/B11 | formal/model argumentはあるが帰結の完全条件・独立semantic/cognitive/social/phenomenal mapなし。経験的一般必要十分とは認定しない。 |
| CT-NSBURDEN-016 | CT-NS-016;S08:62–63;JA419 institutional stability does not require central enforcement; follows depth | context social CT, categorical wording;potential depth;norms;YES necessity denial + grounding;— | B2/B5/B11 | formal/model argumentはあるが帰結の完全条件・独立semantic/cognitive/social/phenomenal mapなし。経験的一般必要十分とは認定しない。 |
| CT-NSBURDEN-017 | CT-NS-017;S08:64–66;JA420 coordinated perturbation sufficient to overcome collective depth required | model narrative;depth/perturbation;social concepts;YES necessity/threshold;— | B2/B5/B11 | formal/model argumentはあるが帰結の完全条件・独立semantic/cognitive/social/phenomenal mapなし。経験的一般必要十分とは認定しない。 |
| CT-NSBURDEN-018 | CT-NS-018;S09:31–46;JA449–456 input can no longer change topology; prevents durable understanding | model failure mode;terms/wells;concept stabilization;YES impossibility/prevention wording;phenomenologically named but not first-person necessity | B2/B4/B5/B6 | formal/model argumentはあるが帰結の完全条件・独立semantic/cognitive/social/phenomenal mapなし。経験的一般必要十分とは認定しない。 |
| CT-NSBURDEN-019 | CT-NS-019;S09:62–66;JA466–467 quantitative predictions require parameters/maps | explicit scope;YES future specification;—;research prerequisite;— | B0/B7/B9 | scope/research prerequisite/model-input exclusionはsource-localに支持。現実一般の必要・不可能性を証明しない。 |
| CT-NSBURDEN-020 | CT-NS-020;S11:49–58;JA541–545 individuation criterion needed / shared-landscape conditions future | explicit open question;YES future criteria;YES individuation;social stability;— | B0/B1/B3/B11 | scope/research prerequisite/model-input exclusionはsource-localに支持。現実一般の必要・不可能性を証明しない。 |
| CT-NSBURDEN-021 | CT-NS-021;S11:61–64;JA548 requires empirical collaboration | methodological;map target named;—;research prerequisite;— | B0/B7 | scope/research prerequisite/model-input exclusionはsource-localに支持。現実一般の必要・不可能性を証明しない。 |
| CT-NSBURDEN-022 | CT-NS-022;S04:118–119;JA205 methodological necessities, not ultimate meaning/experience nature | explicit negative scope;—;YES;YES;YES exclusion | B0 | scope/research prerequisite/model-input exclusionはsource-localに支持。現実一般の必要・不可能性を証明しない。 |
| CT-NSBURDEN-023 | CT-NS-023;S12:17–18;JA557 no semantic primitives/intentional units required | within central model result;field/coupling;YES denied input;intentional-state denial;not phenomenal explanation | B0/B2/B3 | scope/research prerequisite/model-input exclusionはsource-localに支持。現実一般の必要・不可能性を証明しない。 |
| CT-NSBURDEN-024 | CT-NS-024;S08:83–88;JA430 innovation whenever perturbations/windows reactivate vs always gradient | framework;positivity/conditions;open social terrain;YES possibility vs guarantee;— | B1/B3/B4/B9/B11 | formal/model argumentはあるが帰結の完全条件・独立semantic/cognitive/social/phenomenal mapなし。経験的一般必要十分とは認定しない。 |
| CT-NSBURDEN-025 | CT-NS-025;S06:76–77;JA331 S>epsilon vocabulary membership | local definition;YES inequality;YES vocabulary;reuse input;— | B0/B1/B3 | definition条件はE0/E1。signature/tolerance/criterion未指定分はB1、semantic/phenomenal同定は別burden。 |
| CT-NSBURDEN-026 | CT-NS-026;S09:19–27;JA442–444 no subjective explanation/neural architecture dependence | explicit scope;abstraction;—;neural exclusion;YES negative scope, not impossibility theorem | B0 | scope/research prerequisite/model-input exclusionはsource-localに支持。現実一般の必要・不可能性を証明しない。 |

26/26。if/conditionをsourceにないiffへ変換しない。JA guaranteeの追加burdenはPOS/VARで別記。

## 33. Identity / correspondence burden

| CT-IDBURDEN | Phase02 IDREL / source | Relation type | Required burden | Current support boundary |
| --- | --- | --- | --- | --- |
| CT-IDBURDEN-001 | CT-IDREL-001;S02:13–15;conceptual terrain same object as CT intuitive metaphor | local definition | B0 | source-local alias/naming/exclusionはE0。外部identityを付加しない。 |
| CT-IDBURDEN-002 | CT-IDREL-002;S00:86–96;README;JA15–20;not redefine / projected realizations | interpretation | B0/B1/B10 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-003 | CT-IDREL-003;S04:14–25;I represents tension / corresponds to active regions | correspondence | B3/B4/B7 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-004 | CT-IDREL-004;S04:58–60;Phi: conceptual landscape itself | local definition | B0 | source-local alias/naming/exclusionはE0。外部identityを付加しない。 |
| CT-IDBURDEN-005 | CT-IDREL-005;S03:64–65 vs JA141;meaning is trajectory set / downstream interpretation of experienced meaning | identity wording / interpretation | B0/B3/B6 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-006 | CT-IDREL-006;S04:110–116;JA200–202;Phi not meaning / J_I not content / token not meaning unit | interpretation (negative scope) | B0 | source-local alias/naming/exclusionはE0。外部identityを付加しない。 |
| CT-IDBURDEN-007 | CT-IDREL-007;S02:74–76;S05:126–135;concept is stable region, defined by | local definition | B0/B1 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-008 | CT-IDREL-008;S02:81–83;S04:64–66;thought is trajectory / thought as flow | identity wording | B1/B4 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-009 | CT-IDREL-009;S05:138–152;S10:51–53;understanding is condition / ease corresponds | local definition + correspondence | B0/B1/B4/B6 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-010 | CT-IDREL-010;S04:76–78;experiential time / irreversible ordering same row | interpretation | B6/B7 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-011 | CT-IDREL-011;S04:94–101;JA193;structurally isomorphic; analogy; no quantum claim | analogy + identity wording | B1/B10 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-012 | CT-IDREL-012;S05:119–122;JA256–257;Phi* is sedimented landscape / reflects history | local definition / interpretation | B1/B2/B3/B4 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-013 | CT-IDREL-013;S06:10–26;solution classes correspond to cognitive phenomena | correspondence | B1/B4 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-014 | CT-IDREL-014;S06:35–45;depth/width/curvature measures resistance/context/precision | interpretation | B3/B4 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-015 | CT-IDREL-015;S06:53–65;ridges correspond to boundaries; mechanistic account | correspondence + explanation wording | B3/B4/B5 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-016 | CT-IDREL-016;S06:69–82;vocabulary not list but distribution; set display | local definition / unclear | B0/B1/B3 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-017 | CT-IDREL-017;S07:35–45;forgetting corresponds to relaxation; remembering to redeepening | correspondence | B2/B4/B5 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-018 | CT-IDREL-018;S07:49–79;concept change/insight corresponds; this is bifurcation | correspondence + identity wording | B1/B3/B4/B6 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-019 | CT-IDREL-019;S08:18–38;same dynamics / no property changed | identity wording | B1/B10/B11/B12 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-020 | CT-IDREL-020;S08:56–66;norms/institutions correspond then are attractor regions | correspondence + identity wording | B3/B11 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-021 | CT-IDREL-021;S08:70–81;Intelligence is distributed maintenance | local definition / interpretation | B0/B4/B11/B12 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-022 | CT-IDREL-022;S09:15–22;meaning emergent label; conscious access downstream | interpretation | B0/B3/B6 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-023 | CT-IDREL-023;S10:40–44/61–70;interpretations rather than definitions / theoretical basis | correspondence + derivation-like authority wording | B1/B3/B4/B6 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-024 | CT-IDREL-024;S11:20–28;structurally related to distributional semantics; fundamentally differs | analogy | B3 | conceptual comparison。一方の成果をCT mapping/dataへ転用しない。 |
| CT-IDBURDEN-025 | CT-IDREL-025;S11:33–37;drive corresponds to error influx / deepening can be understood as minimization | correspondence | B2/B4/B5 | conceptual comparison。一方の成果をCT mapping/dataへ転用しない。 |
| CT-IDBURDEN-026 | CT-IDREL-026;S12:61–71;same field / same generative grammar, not identical entities | analogy + identity wording with guard | B1/B3/B10/B12 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-027 | CT-IDREL-027;JA575–576;同じ情報場 / 同一基礎方程式の解クラス | identity wording | B1/B3/B10/B12 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-028 | CT-IDREL-028;S02:105–106;JA104;derives core equations / 導出 | derivation wording | B1 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-029 | CT-IDREL-029;S01:9–12;S03:84–93;not conscious inspection / experiences reflect geometry | interpretation / explanation wording | B6 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-030 | CT-IDREL-030;S05:162–177;JA280;follows from / generic implication | derivation wording | B1/B2/B3 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-031 | CT-IDREL-031;S11:14–18;JA522;grounding substrate / 最小公理から導出 | derivation wording | B1/B4/B10 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |
| CT-IDBURDEN-032 | CT-IDREL-032;S10:54–56;JA503;CPU/GPU corresponds to fast/slow to be formalized | correspondence / future | B4/B10 | 定義/式/内部解釈/比較の弱い成分は所在あり。B1の完全仕様とB3/B4/B6/B10/B11の独立mappingは区別。対応語だけで強いidentity supportにしない。 |

32/32。isを一律B10にせず、local definitionとsemantic/cognitive/phenomenal/social/cross-scale関係を分離。

## 34. Serious-candidate evidence audit

| CT-SERBURDEN | Serious | Weak reading support | Strong reading burden | Current support / gap | Serious status after Phase04 |
| --- | --- | --- | --- | --- | --- |
| CT-SERBURDEN-001 | CT-SERIOUS-001 | E0/E1 local integral threshold;E2/E5 ease correspondence | B4/B6/B7/B8 cognitive understanding/felt ease independently tied to cost | PARTIAL:region/metric/criterion/data absent。correctness exclusionはphenomenal bridgeではない。 | RETAIN |
| CT-SERBURDEN-002 | CT-SERIOUS-002 | E2/E5 rapid topology analogy;threshold organization | B1/B4/B6/B7/B8 topology→cognitive event→felt suddenness | PARTIAL:topology definitionとindependent cognitive/phenomenal endpointが未接続。 | RETAIN |
| CT-SERBURDEN-003 | CT-SERIOUS-003 | E2 attractor analogy/depth narrative | B5/B7/B8/B11 institution identity/depth/stability causal relation | PARTIAL:independent institution/depth observable・causal/social data absent。 | RETAIN |

Phase03の5条件を維持。support欠如だけでESCALATEDにしない。strong readingのburdenは残るがweak definition/analogyを否定しない。Source-level vicious circularity established?: NO はPhase03結論を保持し、新しいfinal circularity verdictは出さない。

## 35. C6 evidence-loop burden

| CT-C6BURDEN | Phase03 route / coverage | Independent quantity required (burden, not protocol) | Repository finding / executed? |
| --- | --- | --- | --- |
| CT-C6BURDEN-001 | CT-CIR-027;CT-EVIDLOOP-001/009 | understanding/blocked-thought endpointとcost/barrierを別に同定;B4/B6/B7 | 独立推定/逆推論ruleなし。sourceに実行済みevidence loopなし、candidate保持。 |
| CT-C6BURDEN-002 | CT-CIR-028;CT-EVIDLOOP-002 | insight endpointとtopology changeを独立識別;B4/B6/B7 | 両者の同定criteriaなし。単なる対応を観測証明にしない。 |
| CT-C6BURDEN-003 | CT-CIR-029;CT-EVIDLOOP-003 | communication successとprior-landscape similarity;B3/B7/B11 | success→similarity inverse rule未指定。potential loopで実測loopでない。 |
| CT-C6BURDEN-004 | CT-CIR-030;CT-EVIDLOOP-004 | institution persistenceとwell depth;B7/B11 | depthを持続から逆推定する実装なし。C6 risk保持。 |
| CT-C6BURDEN-005 | CT-CIR-031;CT-EVIDLOOP-005 | note/report provenanceとCT cost構造の独立性;B6/B7 | 同じintuitionを独立validationに数えない。exactnote authorityも未固定。 |
| CT-C6BURDEN-006 | CT-CIR-032;CT-EVIDLOOP-006 | 図示outcomeとは別のmodel witness/data;B1/B2/B8 | FIG002は描かれた帰結。executed witnessではない。 |
| CT-C6BURDEN-007 | CT-EVIDLOOP-007/008/010 controls | Phi* label;positivity guard;collective intelligence criterion | 007 not present、008 guarded、010 unresolvedを保持。6primary C6に新規実行loopを加えない。 |

7 burden entries = 6 primary C6 families + 1 control reconciliation row。10/10 EVIDLOOP細目を対応。必要な独立性を列記しただけで測定方法/operational protocolを設計しない。

## 36. Claim / evidence gaps

| CT-GAP | Category | Substantial unmet burden | Burden | Primary claim coverage |
| --- | --- | --- | --- | --- |
| CT-GAP-001 | formal signature | x/domain/measure,K,field/balance/initial-boundary specification | B1 | CT-CLM-002, CT-CLM-003, CT-CLM-005, CT-CLM-047 |
| CT-GAP-002 | formal signature / cognitive criterion | JI field vs path and thought extraction | B1/B4/B7 | CT-CLM-002, CT-CLM-005, CT-CLM-008 |
| CT-GAP-003 | semantic bridge / operationalization | I/C tension/activity and drive input mapping | B3/B4/B7 | CT-CLM-003, CT-CLM-004, CT-CLM-042, CT-CLM-047 |
| CT-GAP-004 | formal signature / semantic bridge | concept perturbation norm,individuation,geometric attributes | B1/B3/B7 | CT-CLM-006, CT-CLM-020 |
| CT-GAP-005 | formal signature / cognitive criterion | understanding region/metric/theta and independent understanding endpoint | B1/B4/B7 | CT-CLM-007, CT-CLM-017 |
| CT-GAP-006 | phenomenal criterion | felt ease/insight/pathology endpoints distinct from naming | B6/B7 | CT-CLM-009, CT-CLM-010, CT-CLM-017, CT-CLM-025, CT-CLM-026, CT-CLM-032 |
| CT-GAP-007 | operationalization / phenomenal criterion | tau irreversibility/experiential-time mapping | B6/B7 | CT-CLM-011 |
| CT-GAP-008 | formal signature / mechanism support | Q/token extraction,continuous/discrete necessity,bootstrap | B1/B2/B4 | CT-CLM-012, CT-CLM-023, CT-CLM-040 |
| CT-GAP-009 | formal signature | ell_i common type/dot product/L functional signature | B1 | CT-CLM-013, CT-CLM-023 |
| CT-GAP-010 | mechanism support | token/gradient/basin/cost update and causal consequences | B2/B5 | CT-CLM-013, CT-CLM-021, CT-CLM-023, CT-CLM-024, CT-CLM-042 |
| CT-GAP-011 | formal signature / cognitive criterion | Phi* convergence notion and history/memory relation | B1/B4 | CT-CLM-015, CT-CLM-016, CT-CLM-024 |
| CT-GAP-012 | semantic bridge | meaning/trajectory,category,ridge,context/precision mapping | B3 | CT-CLM-009, CT-CLM-020, CT-CLM-021, CT-CLM-025, CT-CLM-041 |
| CT-GAP-013 | formal signature / semantic bridge | EN conditional positivity vs JA generic gradient/openness inference | B1/B2/B3 | CT-CLM-018, CT-CLM-019 |
| CT-GAP-014 | mechanism support / operationalization | effective barrier vs hard prohibition and resistance calibration | B2/B4/B5/B7 | CT-CLM-027, CT-CLM-032, CT-CLM-047 |
| CT-GAP-015 | cross-scale translation / social mapping | individual-to-collective Phi common domain/aggregation | B1/B10/B11 | CT-CLM-014, CT-CLM-028, CT-CLM-029, CT-CLM-035 |
| CT-GAP-016 | social mapping / mechanism support | communication/institution/depth independently identified | B5/B7/B11 | CT-CLM-014, CT-CLM-029, CT-CLM-030, CT-CLM-031, CT-CLM-035, CT-CLM-039 |
| CT-GAP-017 | social mapping / independent validation | collective maintenance vs general intelligence/universality | B4/B11/B12 | CT-CLM-028, CT-CLM-039 |
| CT-GAP-018 | cross-scale translation | VED/IFGT/Q/physical-concept/source-target typed map | B1/B10/B12 | CT-CLM-003, CT-CLM-040, CT-CLM-043, CT-CLM-044, CT-CLM-048 |
| CT-GAP-019 | citation/provenance | exact note/L1 version and independent origin | B0/B3/B6 | CT-CLM-037 |
| CT-GAP-020 | citation/provenance / cross-scale translation | future Con/Int reference versus current comparison authority | B4/B10 | CT-CLM-038 |
| CT-GAP-021 | citation/provenance | dedicated semantic/cognitive/social anchors not present | B3/B4/B8/B11 | CT-CLM-041, CT-CLM-042 |
| CT-GAP-022 | operationalization / empirical data | no CT-linked observable extraction/calibration/dataset | B7/B8 | CT-CLM-002, CT-CLM-004, CT-CLM-008, CT-CLM-010, CT-CLM-011, CT-CLM-012, CT-CLM-013, CT-CLM-014, CT-CLM-017, CT-CLM-020, CT-CLM-021, CT-CLM-023, CT-CLM-024, CT-CLM-025, CT-CLM-026, CT-CLM-027, CT-CLM-029, CT-CLM-030, CT-CLM-031, CT-CLM-032, CT-CLM-035, CT-CLM-039, CT-CLM-042, CT-CLM-047 |
| CT-GAP-023 | independent validation | source-suggested predictions lack prospective/held-out test | B9 | CT-CLM-013, CT-CLM-019, CT-CLM-021, CT-CLM-023, CT-CLM-024, CT-CLM-029, CT-CLM-032, CT-CLM-035 |
| CT-GAP-024 | version authority | canonical EN/JA working/Master/history conflicts not silently merged | B0/B1/B10 | CT-CLM-016, CT-CLM-019, CT-CLM-044, CT-CLM-048 |
| CT-GAP-025 | formal signature / semantic bridge | S(token) numeric criterion;vocabulary set/distribution | B1/B3 | CT-CLM-022 |
| CT-GAP-026 | cognitive criterion / phenomenal criterion | pathology and failure-mode independent classification | B4/B6/B7 | CT-CLM-032 |

26 stable gap families。sentence単位の重複gapではない。primary tableのgap参照と逆対応。未発見はfalse判定ではなく、このrepository/authority範囲の不足。

## 37. Strong-language over-ceiling scan

| CT-OVER | Source / claim | Wording marker | Classification | Reason / surviving support |
| --- | --- | --- | --- | --- |
| CT-OVER-001 | S05:126–152;CLM006/007 | Definition concept/understanding | within ceiling | local B0。外部semantic/phenomenal identityは別。 |
| CT-OVER-002 | S04:28–30;S05:168–177 | not by itself guarantee / nonpointwise | guarded | EN条件を保持。 |
| CT-OVER-003 | S05:58–60;CLM012 | cannot sustain / requires discrete units | possibly over ceiling | model necessity argumentはあるが代替排除証明/taskなし。 |
| CT-OVER-004 | S05:89–92;S07:24–25;CLM013/023 | purely dynamical / ensures each reuse deepens | clearly over ceiling | 帰結を確立済み機構と読む強度は式/図の範囲を超える。well-typedness正誤は未判定。 |
| CT-OVER-005 | S06:10–13;CLM002 | solution classes / detailed analysis subsequent | possibly over ceiling | 分類tableとformal characterizationを区別。 |
| CT-OVER-006 | S06:43–45;CLM020 | curvature produces precision | clearly over ceiling | formal curvature→semantic precision mappingなし。 |
| CT-OVER-007 | S06:58–65;CLM021 | mechanistic account of semantic drift | clearly over ceiling | semantic driftのindependent criterion/causal evidenceなし。 |
| CT-OVER-008 | S03:84–93;CLM010 | gives rise to phenomenology | clearly over ceiling | phenomenal explanationはE5/internal correspondence超。 |
| CT-OVER-009 | S03:18–28;S10:51–53;CLM017 | what we experience … change in ease | possibly over ceiling | 例/対応として支持あり。独立identityとしては未支持。 |
| CT-OVER-010 | S04:76–78;CLM011 | experiential time table identity | possibly over ceiling | tau formal roleに独立experience mapなし。 |
| CT-OVER-011 | S07:69–79;CLM025/026 | this is bifurcation / subjective reflects | clearly over ceiling | strong cognitive/phenomenal説明のendpointが未接続。 |
| CT-OVER-012 | S08:8–38;CLM028 | same dynamics / no property changed | clearly over ceiling | collective common state/typed mapなし。 |
| CT-OVER-013 | S08:62–66;CLM031 | follows from depth / accounts for historical difficulty | clearly over ceiling | social operational/causal support未発見。 |
| CT-OVER-014 | S09:31–55;CLM032/035 | prevents / structural basis for polarization | possibly over ceiling | qualitative proposed regimesを越える実証readingは未支持。 |
| CT-OVER-015 | S10:61–70;CLM037 | theoretical basis of note | unresolved | exactnote authorityとsupport方向未固定。 |
| CT-OVER-016 | S11:14–18;CT-IDREL-031 | grounding substrate built from single axiom | possibly over ceiling | provenanceはあるがtyped derivation全体なし。 |
| CT-OVER-017 | S11:30–37;CLM042 | can be understood as error minimization | guarded | conceptual correspondence/E6 backgroundまで。CT検証にはしない。 |
| CT-OVER-018 | S12:61–71;CLM043 | same generative grammar / not identical | possibly over ceiling | nonidentity guardあり、typed grammar theoremなし。 |
| CT-OVER-019 | JA575–576;CLM044 | 同一基礎方程式の解クラス | version-specific | JA強いcross-scale identity burden。canonical ENと併合しない。 |
| CT-OVER-020 | JA167/280–284/430;CLM019 | always residual gradients/innovation | version-specific | EN条件付きより高burden、追加supportなし。 |
| CT-OVER-021 | JA236/374;CLM027/047 | structural prohibition / diverges | version-specific | effective ENとのversion差を保持。 |
| CT-OVER-022 | S09:59–69;S11:41–64;CLM036 | does not establish quantitative predictions/maps | within ceiling | 未指定の自己申告とrepo inventory整合。 |
| CT-OVER-023 | S03:64–65;CLM009 | what we call meaning / in this framework | guarded | ENは明示的なlocal vocabulary。独立semantic ontologyを主張したと自動判定しない。JAのexperienced-meaning対応や後続semantic説明には別burden。 |
| CT-OVER-024 | S04:94–101;CLM040 | structurally isomorphic / analogy only | guarded | 弱いanalogy有用性と強いisomorphism burdenを分ける。 |

24 scan entriesはstrong hitsとscope対照を含む。clearly/possiblyはその行の強い読みについてのburden判定であり、claim truth/dispositionではない。原文は修正しない。

## 38. Negative-scope claims

| CT-NEG | Source / linked primary | Negative scope | Support and boundary |
| --- | --- | --- | --- |
| CT-NEG-001 | S04:106–119;S09:12–16;CLM045 | not semantic/reference/truth theory;Phi not meaning field;token not meaning unit | B0/E0 YES。positive meaning/trajectory claimのB3は残る。 |
| CT-NEG-002 | S09:18–22;CLM033 | does not generate/explain subjective experience | B0/E0 YES。S03/S07 experiential wordingのB6を消さない。 |
| CT-NEG-003 | S09:24–27;S11:60–64;CLM034 | neural implementation deferred | B0/E0 YES。具体carrierを確立しない。 |
| CT-NEG-004 | S04:94–101;CLM040 | no quantum-theory claim | B0/E0 YES部分。isomorphic部分のB10は別。 |
| CT-NEG-005 | S02:81–83;CLM046 | no directing subject required within model | B0/B2 source support。経験的一般subject否定ではない。 |
| CT-NEG-006 | S09:12–16;S10:40–53;CLM007/017 | not correct-meaning account;note correspondences not definitions | B0/E0。cognitive/felt understandingの独立criterionを代替しない。 |
| CT-NEG-007 | S09:59–69;S11:41–58;CLM036 | no quantitative predictions/concrete maps/complete theory | B0/E0 inventoryと整合。positive mechanism strengthは別審査。 |
| CT-NEG-008 | S11:36–37;CLM042 | no Bayesian generative-model commitment | B0/E0。general fieldという語だけで外部理論より広い妥当性を証明しない。 |
| CT-NEG-009 | S12:61–71;CLM043;S10:61–70 | not identical/reducible;note not replaced | B0/E0。same grammar/theoretical basisの独立burdenは残る。 |
| CT-NEG-010 | S00:86–96;README;CLM048 | does not redefine general IFGT variables / projected use | B0/E0。typed inheritance/source-version equivalenceは未成立。 |

10 scope families。primary claim-type NEGの件数とは母集団が異なる。source omissionがtrue/false一般定理であるという読みを加えない。

## 39. Citation-anchor gaps

| CT-CITEGAP | Topic / source | Current anchor state | Unmet attribution boundary |
| --- | --- | --- | --- |
| CT-CITEGAP-001 | understanding/felt ease;S03/S05/S10 | 専用anchorなし;intuitive example | CT criterion/taskの出典は未固定。 |
| CT-CITEGAP-002 | insight/suddenness;S07:69–79 | 専用anchorなし | topology correspondenceを既存実証としない。 |
| CT-CITEGAP-003 | memory/forgetting/recall;S07:35–45 | 専用anchorなし | GammaCはempirical memory citationではない。 |
| CT-CITEGAP-004 | communication/synchronization/polarization;S03/S09 | 専用anchorなし | 背景例とCT social mechanismを区別。 |
| CT-CITEGAP-005 | institution/norm/historical stability;S08:56–66 | 専用anchorなし | social cases/dataに関する出典なし。 |
| CT-CITEGAP-006 | collective intelligence;S08:70–81 | 専用external anchorなし;Int2内部comparison | definitionと既存知見の実証帰属を区別。 |
| CT-CITEGAP-007 | neural firing/connectivity/oscillation;S11:60–64 | future targets only;dedicated anchorなし | 予定項目でありCT dataではない。 |
| CT-CITEGAP-008 | distributional semantics/embedding;S11:20–28 | named comparison;dedicated keyなし | 外部背景の内容確認は未実施。 |
| CT-CITEGAP-009 | physical quantization/isomorphism;S04:94–101 | analogy;dedicated external keyなし | typed formal relationは引用の追加だけでも供給されない。 |
| CT-CITEGAP-010 | note/Con/Int/Master current version;S00/S10 | prose/source names;exactnote/Master authority未固定 | internal artifact provenance gap。外部文献gapと区別。 |

10 anchor-gap families。citationの不存在はfalseを意味しない。source-local定義そのものにexternal citationを要求しない。新規引用/著者年の推測はしない。

## 40. EN / JA burden variants

| CT-BURDVAR | Variant / locators | Classification | Evidence-burden difference |
| --- | --- | --- | --- |
| CT-BURDVAR-001 | positivity;EN S04:28–30,S05:168–177 vs JA167/280–284 | JA HIGHER BURDEN | conditional/nonpointwise guard vs generic gradient implication;B1/B2/B3。 |
| CT-BURDVAR-002 | Cmax/barrier;EN S05:36–50 vs JA236/374 | JA HIGHER BURDEN | effective resistance vs structural prohibition;B1/B2/B5。 |
| CT-BURDVAR-003 | physical/concept;EN S12:61–71 vs JA575–576 | JA HIGHER BURDEN | projected grammar guard vs same-equation solution-class wording;B10/B12。 |
| CT-BURDVAR-004 | axiom grounding;EN S11:14–18 vs JA522 | JA HIGHER BURDEN | grounding attribution vs minimal-axiom derivation;B1/B10。 |
| CT-BURDVAR-005 | Phi* qualification;EN S05:119–122 vs JA256–257 | DIFFERENT BURDEN | not necessarily unique/static vs categorical nonunique/nonstatic;target meaning/proofB1未固定。 |
| CT-BURDVAR-006 | meaning;EN S03:64–65 vs JA141 | DIFFERENT BURDEN | EN semantic identityB3;JA experienced downstream interpretationB6を伴う。 |
| CT-BURDVAR-007 | concept reentry;EN S05:126–135 vs JA87/261–265 | DIFFERENT BURDEN | JA recursive/reentry framing追加;B1/B4bootstrap。 |
| CT-BURDVAR-008 | experiential time;EN S04:76–78 vs JA188 | SAME BURDEN | formal tau→experience bridge/calibrationは両方未指定。 |
| CT-BURDVAR-009 | insight;EN S07:69–79 vs JA379–382 | SAME BURDEN | topology/cognitive/subjective thresholdを結ぶB4/B6は両方必要。 |
| CT-BURDVAR-010 | social innovation;EN S08:83–88 vs JA430 | JA HIGHER BURDEN | conditional opportunity vs always gradients;B9/B11/B12。 |
| CT-BURDVAR-011 | S table/distribution;EN S06:70–82 vs JA328–334 | SAME BURDEN | set criterionあり;numeric S/domain/distribution mappingなし。 |
| CT-BURDVAR-012 | Con future/negative scope;EN S09/S10 vs JA442/503 | VERSION UNCLEAR | future authority/companion historyをcurrent Conとの同一sourceにしない。 |

12 working comparison families。JAはCANONICALではない。higher burdenはsource改訂指示/最終dispositionではない。

## 41. Tested / validated status

| CT-linked item | Located count | Boundary |
| --- | --- | --- |
| tested predictions | 0 | 21 inventory entries中実行済みtestなし |
| validated predictions | 0 | independent/held-out validationなし |
| executed cognitive experiments | 0 | future tasksを実行結果に数えない |
| CT-local code/simulation/data support | 0 | 28 local files inventory:TeX/MD/Bib/3PNG/PDF/build byproducts等のみ |
| simulation results | 0 | FIG002before/afterはsimulation outputと記載されていない |
| empirical datasets | 0 | CT-linked actual observations/dataなし |
| behavioral data | 0 | behavioralはfuture mapping target |
| neural data | 0 | firing/connectivity/oscillationsはfuture targets |
| social data | 0 | 制度/通信/分極化はqualitative examples |
| E7 operational map | 0 | parameters/observable extraction未指定 |
| E9/E10 independent/predictive validation | 0 | bibliographyから輸入しない |
| E11 typed translation | 0 | 同一glyph/文法はtyped mapではない |
| E12 social operational evidence | 0 | collectivePhi operationalization未発見 |

0はcurrent CT-linked repository inventoryの結果であり、外部世界に研究がないという主張ではない。empirical ceilingとexternal literatureの存在は両立する。

## 42. Current support matrix

| Domain | Strongest current support | Missing next rung |
| --- | --- | --- |
| formal | E0/E1 expressions/local definitions + E2 structural prose | signature/domain/initial-boundary conditions/derivation specification;mathematical correctness未判定 |
| semantic | SE2 conceptual precedent + SE1 internal geometry comparison | SE3 independent semantic map/criterion |
| cognitive | COG2 external background comparison + E2/E5 | COG3 task/variable correspondence |
| phenomenal | PCE2 comparative example organization | PCE3 independent phenomenal proxy;reportをidentityにしない |
| social | E2 qualitative collective/attractor narrative;E4downstream comparison | B10/B11 shared domain/independent social observable;E12 |
| cross-scale | E4 internal reuse/analogy/source reference | E11 typed translation/domain/invariant preservation |

claim type ↔ evidence typeを保つ。internal consistency≠empirical support、illustration≠evidence、named phenomenon≠model-specific support、downstream reuse≠upstream validation。strong readingが未支持でも定義/比喩/方法的比較が無用・falseとはならない。

## 43. Phase04 uncertainty ledger

| Uncertainty | Category | Linked burden | Unresolved question |
| --- | --- | --- | --- |
| CT-U-125 | claim component support | CT-GAP-001;CLM002/005 | 式存在E1とformal consequenceB1/B2を分けるため、未指定解空間/初期境界条件がどの帰結に必要か。 |
| CT-U-126 | field/path cognitive endpoint | CT-GAP-002;CLM008 | JI field→trajectory→thoughtの独立criterionを何が担うか。 |
| CT-U-127 | activity/tension calibration | CT-GAP-003;CLM003/004 | I/Cのsemantic namingとactive/inactive cognitive判断を区別できるsource-supported calibrationはあるか。 |
| CT-U-128 | concept individuation burden | CT-GAP-004;CLM006/020 | model basinの定義と外部concept単位/文脈/精度を区別するcriterionの所在。 |
| CT-U-129 | understanding formal vs functional | CT-GAP-005;CLM007 | region/thresholdのspecificationと独立cognitive understanding criterionをどう別々に審査するか。 |
| CT-U-130 | phenomenal independence | CT-GAP-006;CT-SERIOUS-001/002 | ease/suddenness例とindependent phenomenal proxyを区別する証拠は何か。 |
| CT-U-131 | time burden | CT-GAP-007;CLM011 | formal tauの順序と体験時間の対応を、同じnaming以外に固定できるか。 |
| CT-U-132 | necessity/initialization burden | CT-GAP-008;CLM012/023 | discreteness necessityとtoken/basin bootstrapの独立formal witnessの所在。 |
| CT-U-133 | coupling signature burden | CT-GAP-009;CLM013 | dot-product型・Lの種別未指定が、どのmechanism assertionのB1を制限するか。 |
| CT-U-134 | mechanism consequence burden | CT-GAP-010;CLM013/021/023 | reinforcement/depth/costを式の併記でなく帰結として支えるargumentと独立causal mappingの所在。 |
| CT-U-135 | sedimentation/memory burden | CT-GAP-011;CLM015/016/024 | Phi* convergence/nonstatic interpretationとmemory-task correspondenceにそれぞれ必要なsupport。 |
| CT-U-136 | semantic mapping independence | CT-GAP-012;CLM009/020/021/041 | trajectory/precision/driftをmodel語彙以外から識別するsemantic criterionの所在。 |
| CT-U-137 | positivity version burden | CT-GAP-013;CLM018/019 | EN条件付きとJAgeneric chainの異なるburdenを満たす既存derivationがあるか。 |
| CT-U-138 | barrier resistance burden | CT-GAP-014;CLM027/032/047 | effective termとhard prohibition/behavioral resistanceを区別する正式条件・observableの所在。 |
| CT-U-139 | collective typing burden | CT-GAP-015;CLM028/029 | individualとsocialに共通のdomain/aggregation/invariantを与えるsourceの所在。 |
| CT-U-140 | institution/communication independence | CT-GAP-016;CT-SERIOUS-003 | well depthやprior similarityを制度安定/通信成功から循環的に推定しない独立criterionの所在。 |
| CT-U-141 | intelligence generalization burden | CT-GAP-017;CLM039 | local landscape-maintenance definitionを超えるintelligence/generalization supportの所在。 |
| CT-U-142 | typed inheritance burden | CT-GAP-018;CLM040/043/044/048 | shared grammar/equation/isomorphismに必要なtyped translationの所在。 |
| CT-U-143 | note provenance burden | CT-GAP-019;CLM037 | L1 intuitionのexactsourceとCT support-directionを確定するdocumentary evidenceの所在。 |
| CT-U-144 | reciprocal-source burden | CT-GAP-020;CLM038 | future Con/Int referralと現行内部comparisonのsource identity、独立性の扱い。 |
| CT-U-145 | citation role boundary | CT-GAP-021;CT-LIT-006/007 | 二つの実外部anchorの概念的先例が支える範囲。未取得文献内容でCT mappingを補わない。 |
| CT-U-146 | CT-linked operational/data burden | CT-GAP-022 | repository他branchのdataをCT supportへ移すexplicit mapがない現状を、将来何で更新するか。 |
| CT-U-147 | predictive independence | CT-GAP-023;CT-PRED-001–021 | qualitative directionとfuture taskのどこに独立endpoint/held-out testing authorityが必要か。 |
| CT-U-148 | authority-specific support | CT-GAP-024;CT-BURDVAR | ENcanonical/JAworking/Master履歴差を同一claimの追加supportと誤集計しない単位。 |
| CT-U-149 | vocabulary support | CT-GAP-025;CLM022 | S function/set membershipの形式burdenとvocabulary accessibilityのsemantic burdenを分けるcriterionの所在。 |
| CT-U-150 | pathology/test-scope burden | CT-GAP-026;CLM032/035 | model failure-mode名と独立clinical/social classification・検証結果を区別するauthorityの所在。 |

CT-U-125–150の26件を追加。既存CT-U-001–124を変更・解消・再番号付けしない。計150。各行は既存object uncertaintyのburden-specific follow-upであり、proseによるsolutionや新protocolではない。

## 44. Phase04 limits

claim disposition（KEEP/REVISE/DOWNGRADE/SPLIT/RETIRE/OPEN）は付与しない。最終truth/validity/falsifiability、数学的正誤、式変更要否、source wording修正、semantic/social/phenomenal identityの成立を決めない。

Phase03 source-level vicious circularity established?: NO / global unfalsifiability established by Phase03?: NO を保持。C6は可能な逆推論loopのburdenを追跡したのみでglobal verdictを追加しない。3 serious candidatesのRETAINはclaim dispositionではない。source reuse≠derivation、same glyph≠same object、same formula≠same signatureを維持する。

## 45. Validation

| Count ledger | Result |
| --- | --- |
| primary claims | 48 |
| support YES | 6 |
| support PARTIAL | 36 |
| support NO | 3 |
| support UNRESOLVED | 3 |
| evidence entries | 40 |
| burden categories used | 13 |
| gap families | 26 |
| formal equation families | 14 |
| Token coupling burden | 8 |
| Understanding burden | 6 |
| Insight burden | 4 |
| Institution burden | 6 |
| Thought / flow burden | 5 |
| Tau / experiential time burden | 4 |
| Positivity burden | 8 |
| Barrier burden | 6 |
| Phi-star / sedimentation burden | 6 |
| Meaning burden | 5 |
| Concept burden | 7 |
| Collective / social burden | 8 |
| Physical / concept cross-scale burden | 5 |
| Consciousness cross-reference burden | 4 |
| Intelligence cross-reference burden | 3 |
| actual bibliography entries | 8 |
| unique cited keys | 7 |
| unresolved keys | 0 |
| figures | 3 |
| prediction/future inventory | 21 |
| qualitative direction families | 16 |
| future tasks | 5 |
| mechanism crosswalk | 34 |
| positive mechanism language | 29 |
| NS crosswalk | 26 |
| IDREL crosswalk | 32 |
| serious RETAIN | 3 |
| C6 burden entries | 7 |
| C6 primary families | 6 |
| EVIDLOOP details | 10 |
| strong-language scan entries | 24 |
| OVER within ceiling | 2 |
| OVER possibly over ceiling | 7 |
| OVER clearly over ceiling | 7 |
| OVER version-specific | 3 |
| OVER guarded | 4 |
| OVER unresolved | 1 |
| negative-scope ledger | 10 |
| citation anchor gaps | 10 |
| EN/JA burden variants | 12 |
| new uncertainties | 26 |
| total uncertainties | 150 |

Validation: PASS。

| Check | Result |
| --- | --- |
| Primary coverage | CT-CLM-001–048 / CT-BURDEN-001–048、48/48 exactly once、duplicate/missing 0 |
| Existing ledger crosswalk | CT-MECHLANG 34/34、CT-NS 26/26、CT-IDREL 32/32、EQF14/14 |
| Serious/C6 | SERIOUS3/3 RETAIN、C6 primary6/6、EVIDLOOP細目10/10（control含む） |
| Figures | PNG3/3再表示・source/caption照合、全てE3 illustration/schematic |
| Bibliography | entries8、cited unique keys7、commands6/key occurrences11、unresolved keys0 |
| Prediction / ceiling | inventory21の16 directions/5 future tasksを区別。tested/validated0。CE/SE/COG/PCE全levelの母集団・count照合 |
| Uncertainties | CT-U-125–150 sequential26件、旧124件未変更、計150 |
| Source / display preservation | canonical12sections、EN12display blocks/14relation rows/13labels、JA14blocks。CT28filesのSHA-256全一致 |
| Earlier authority | Phase00–03の4record SHA-256一致。README履歴保持 |
| Task delta | snapshot1464→1465files。new1本record、modified1 README、unchanged existing1463、removed0 |
| Upstream/downstream preservation | task-startとのSHA-256差なし。既存dirty changes保持 |
| Markdown / links | tables/fences PASS、local links38 checked（README含む） |
| Whitespace | git diff --check PASS、新規recordのgit diff --no-index --check PASS |
| Prohibited operations | source/式/図/PDF/Bib変更なし、web/retrieval/build/simulation/citation追加/commit/pushなし |

git status --shortには既存の多数のmodified filesおよび `?? notes/ct_audit/` が表示される。このtaskのsource変更を意味しない。今回のexact deltaはSHA-256表の2pathsのみ。監査directory自体がuntrackedのため、新record単独のwhitespace checkも実施した。

意味内容の再確認: ENの明示local definition/negative-scopeを自動的なoverclaimとせず、meaningの `what we call ... in this framework` はguarded対照に分類。SERIOUSの弱いdefinition/analogyを保持。JA positivity/硬いbarrier/same-equationはworking固有burdenとして別記し、ENへ正規化しない。

再現用のtask-start snapshot、validation script/outputはrepository外のtemporary directory `${TEMP_EVIDENCE_ROOT}/ct_phase04.yqaWLP/` に置く（永続authorityではない）。source/式/図/Bib/PDFのSHA-256がtask-startと一致することを確認し、既存dirty statusは保存する。新規Markdownはuntrackedのためgit diff --checkだけでなくno-index whitespace検査も行う。

## 46. Stop boundary

Phase04で停止。Phase05 correspondence auditへ進まない。変更許可は本recordとaudit READMEだけ。source/equation/notation/figure/PDF/BibTeX/upstream/downstreamは変更しない。web/external literature retrieval/citation addition/build/simulation/commit/pushを行わない。

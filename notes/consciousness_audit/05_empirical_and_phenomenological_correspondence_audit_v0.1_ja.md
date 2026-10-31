# Consciousness Phase 05 — empirical / phenomenological correspondence audit v0.1

## 0. Status

```text
Consciousness audit: IN PROGRESS
Phase 00–04: COMPLETE
Phase 05 empirical / phenomenological correspondence audit: COMPLETE
Phase 06 revision candidate synthesis: NOT STARTED
Upstream VED equation audit / core revision: CLOSED / CLOSED
Upstream Bio-IFGT audit / core revision: CLOSED / CLOSED
No source/equation/notation revised; no claim disposition assigned
```

2026-09-10のcurrent repositoryのみを対象とする。観測可能性・proxy・比較方向・protocolの具体度・反証条件の構造を分類する。新実験、simulation、外部文献取得、PDF rebuildは行わない。COR/PH-CORは対応の記述成熟度であり、対応が正しいという認定ではない。形式的定義を残したまま、独立した対象同定・測定手順・実行・dataを分ける。

observable proxy ≠ target identity; subjective report ≠ qualia itself; neural correlate ≠ consciousness; measurement residue ≠ live phenomenal state; testable direction ≠ specified test; specified test ≠ executed test; phenomenological fit ≠ mechanistic validation; empirical correspondence ≠ causal explanation。

本記録のIDは監査索引であり理論notationではない。最終妥当性、phenomenal explanationの最終成否、revision actionを決めない。

## 1. Authority

[Phase 00](00_dependency_inheritance_and_authority_record_v0.1_ja.md)

[Phase 01](01_equation_symbol_object_inventory_v0.1_ja.md)

[Phase 02](02_formal_neural_cognitive_phenomenal_role_audit_v0.1_ja.md)

[Phase 03](03_preload_observer_selfreference_circularity_audit_v0.1_ja.md)

[Phase 04](04_claim_and_evidence_burden_audit_v0.1_ja.md)

[README](README_ja.md)。Phase04の105 CLM、18 PRED、24 PH-CLM、28 HBとCE-E0/1を出発点とし、current modular EN/JA本文を再照合した。S00–S20は下表のsource pairを指す。小見出し名は両言語で共通、引用語句は所在確認用。単なるS番号は両言語を指し、JA-only差は明記する。

| Source | EN | JA |
| --- | --- | --- |
| S00 | [EN](../../consciousness/sections/abstract.tex) | [JA](../../consciousness/sections_ja/abstract_ja.tex) |
| S01 | [EN](../../consciousness/sections/introduction.tex) | [JA](../../consciousness/sections_ja/introduction_ja.tex) |
| S02 | [EN](../../consciousness/sections/intuitive_picture.tex) | [JA](../../consciousness/sections_ja/intuitive_picture_ja.tex) |
| S03 | [EN](../../consciousness/sections/notation.tex) | [JA](../../consciousness/sections_ja/notation_ja.tex) |
| S04 | [EN](../../consciousness/sections/sso.tex) | [JA](../../consciousness/sections_ja/sso_ja.tex) |
| S05 | [EN](../../consciousness/sections/torque_converter_attention.tex) | [JA](../../consciousness/sections_ja/torque_converter_attention_ja.tex) |
| S06 | [EN](../../consciousness/sections/formal_mapping.tex) | [JA](../../consciousness/sections_ja/formal_mapping_ja.tex) |
| S07 | [EN](../../consciousness/sections/core_equations.tex) | [JA](../../consciousness/sections_ja/core_equations_ja.tex) |
| S08 | [EN](../../consciousness/sections/structural_interpretation.tex) | [JA](../../consciousness/sections_ja/structural_interpretation_ja.tex) |
| S09 | [EN](../../consciousness/sections/dynamics_log_referencing.tex) | [JA](../../consciousness/sections_ja/dynamics_log_referencing_ja.tex) |
| S10 | [EN](../../consciousness/sections/experimental_reinterpretation.tex) | [JA](../../consciousness/sections_ja/experimental_reinterpretation_ja.tex) |
| S11 | [EN](../../consciousness/sections/qualia_boundary.tex) | [JA](../../consciousness/sections_ja/qualia_boundary_ja.tex) |
| S12 | [EN](../../consciousness/sections/opening_model.tex) | [JA](../../consciousness/sections_ja/opening_model_ja.tex) |
| S13 | [EN](../../consciousness/sections/measurement_collapse.tex) | [JA](../../consciousness/sections_ja/measurement_collapse_ja.tex) |
| S14 | [EN](../../consciousness/sections/non_localization.tex) | [JA](../../consciousness/sections_ja/non_localization_ja.tex) |
| S15 | [EN](../../consciousness/sections/qualitative_predictions.tex) | [JA](../../consciousness/sections_ja/qualitative_predictions_ja.tex) |
| S16 | [EN](../../consciousness/sections/pathologies_limits.tex) | [JA](../../consciousness/sections_ja/pathologies_limits_ja.tex) |
| S17 | [EN](../../consciousness/sections/relation_to_note.tex) | [JA](../../consciousness/sections_ja/relation_to_note_ja.tex) |
| S18 | [EN](../../consciousness/sections/discussion.tex) | [JA](../../consciousness/sections_ja/discussion_ja.tex) |
| S19 | [EN](../../consciousness/sections/conclusion.tex) | [JA](../../consciousness/sections_ja/conclusion_ja.tex) |
| S20 | [EN](../../consciousness/sections/correspondence_map.tex) | [JA](../../consciousness/sections_ja/correspondence_map_ja.tex) |

上流：[VED final](../ved_equation_audit/06_final_audit_record_v1.0_ja.md)、[VED closure](../ved_equation_audit/implementation_final_closure_recheck_v1.1_ja.md)、[Bio final](../bio_ifgt_audit/07_final_audit_record_v1.0_ja.md)、[Bio closure](../bio_ifgt_audit/implementation_final_consistency_recheck_v1.1_ja.md)、[IFGT dynamics](../../Information-Field-Geometry-Theory/sections/fundamental_dynamics.tex)、[Bio source](../../bio-ifgt/sections/minimal_developmental_simulation.tex)。closureをConsciousnessの観測map・phenomenal同定へ継承しない。

探索単位はcurrent entry2+sections42+refs.bib、branch内artifact tree、上流の明示参照先。working draft2とlocal figure exportsはnoncanonicalのまま。repositoryの別branchのtoy数値・CSVをConsciousness participant dataへ流用しない。Phase04のabsence判定を唯一の証拠とはせず、実sourceのLimits/Remaining Questions・cite接続・現物treeを再確認した。

## 2. Correspondence taxonomies

| Axis | Levels | Meaning / restriction |
| --- | --- | --- |
| COR | 0 NONE; 1 NAMED TARGET; 2 PROXY CANDIDATE; 3 OPERATIONAL SCHEMA; 4 EXECUTABLE / IMPLEMENTED; 5 EMPIRICAL DATA LINKED; 6 REPLICATED / PREDICTIVE | 順序を飛ばさない。3はproxyに加えてsource内の比較軸/操作方向があること。固定protocol・map・dataを意味しない |
| PH-COR | 0 LABEL ONLY; 1 INTROSPECTIVE EXAMPLE; 2 REPORT PROXY; 3 STRUCTURED CONTRAST; 4 OPERATIONAL PHENOMENOLOGY; 5 DATA-LINKED; 6 REPLICATED | 3はreport候補と条件対比。4には再現可能なreport/scoring/criterionが必要 |
| PM | 0 IDEA; 1 DIRECTIONAL CLAIM; 2 OBSERVABLE NAMED; 3 PROTOCOL SKETCH; 4 EXECUTABLE PROTOCOL; 5 DATA COLLECTED; 6 TESTED; 7 REPLICATED | 操作とoutcome比較があれば3のsketch。ただし実行条件・尺度・対照は未固定 |
| PE | 0 LABEL; 1 EXAMPLE; 2 REPORTABLE CONTRAST; 3 OPERATIONAL CONTRAST; 4 DATA; 5 REPLICATION | PE2は報告可能な対比まで。PE3は同じ条件で比較できる手順/判定を要する |
| EE | 0 PROSE ONLY; 1 NAMED EMPIRICAL PHENOMENON; 2 PROXY/MAP IDEA; 3 PROTOCOL; 4 DATA; 5 ANALYSIS; 6 REPLICATION; 7 PREDICTIVE VALIDATION | COR3の方向的schemaだけではEE3の実施protocolにならない |
| CE-E | 0 formal/source-local; 1 internal conceptual; 2 external literature anchored; 3 operational mapping; 4 empirical data; 5 replication; 6 predictive validation | Phase04から継承するevidence ceiling。CORとは別軸 |
| PCE | 0 labels; 1 examples; 2 structured report contrasts; 3 operational protocol; 4 data; 5 replication | phenomenal 24 familyの最大所在level。PH-COR2単独はPCE1、PH-COR3はPCE2 |

COR0は「理論的記述がない」ではなく、当該claim対象に観測接続が所在しないこと。empirical identityではないscope文もmandatory type selectionに含まれる場合があり、明記してCOR0とする。PH-COR/PE/PCEはpositive phenomenal families 24を母集団とし、EEはNEURAL/OBSERVATIONAL/EMPIRICALのunion 23を母集団とする。multi-role claimでも同一表内で重複加算しない。

## 3. Empirical correspondence master

Phase04 C-TYPE-04/05/10/11/12/13/14のunionにB3–B6 burden保有familyを加えた64件を全件掲載。残る41件も§30で追跡し、cross-scaleは§27、形式定義は§5に照合する。「なし」はcurrent sourceに未所在、対象の不存在ではない。proxyの「候補」はsourceが名指す又は明示した比較から読める候補に限定する。介入欄は提案/再解釈であり実施済みではない。

| CON-EC | CON-CLM | Target observable | Proxy | Intervention / comparison | COR level | Gap | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CON-EC-001 | CON-CLM-002 | log参照時のconscious state | report可能なログ | なし | COR-2 | report外部化はidentityでなく独立意識criterion未固定 | S00;S06 interface;S09 opening;S12 |
| CON-EC-002 | CON-CLM-004 | 安定意識/窓所属 | 主観報告の安定性 | 相図上の比較方向 | COR-3 | 座標抽出・閾値・独立positive/negativeラベル未固定 | S15 Summary;CON-EQ-067/161 |
| CON-EC-003 | CON-CLM-006 | 予測/反応/候補 | 行動・神経活動への一般的対応 | なし | COR-1 | fast eventを抽出する規則なし | S04;S09 Fast Dynamics |
| CON-EC-004 | CON-CLM-007 | 保持/再参照 | memory/言語ログ候補 | なし | COR-2 | log counting/保持量なし | S04;S09 Slow Dynamics |
| CON-EC-005 | CON-CLM-008 | fast/slow neural/bodily activity | 神経時系列の時間スケール差 | S15比較方向 | COR-3 | 部位・信号帯・rate抽出なし | S14 Local Substrates |
| CON-EC-006 | CON-CLM-010 | finite gapの意識必要性 | report安定性候補 | 同期側の対比 | COR-3 | 独立gapと独立意識基準なし | S04 finite gap;S07 nonclosure;S14 |
| CON-EC-007 | CON-CLM-013 | delay/reference thickness | 報告遅れ・self/time sense | tau/注意の変化方向 | COR-3 | 出来事端点/経験時間とのmapなし | S09 Delay;S15 Delay Window |
| CON-EC-008 | CON-CLM-015 | SSOなしでは意識なし | conscious state名のみ | なし | COR-1 | SSOと意識の独立検出器なし | S04 final paragraphs |
| CON-EC-009 | CON-CLM-016 | 三条件からconscious state | ログ参照/報告候補 | なし | COR-2 | 三条件抽出・phenomenal endpointなし | S06 SSO as Local Non-Closure |
| CON-EC-010 | CON-CLM-019 | 意識の持続 | 参照連続性/報告候補 | なし | COR-2 | 維持時間metric/loop観測なし | S09 loop/persistence |
| CON-EC-011 | CON-CLM-023 | attention変換 | 注意操作/参照bias候補 | S13/S15注意操作 | COR-3 | 操作からTCAへの同定なし | S05 ending;S06 Coupler |
| CON-EC-012 | CON-CLM-024 | 経験されるego位置 | egoという経験名 | なし | COR-1 | 位置を測る独立proxyなし | S05 From Attention to Ego;S08 |
| CON-EC-013 | CON-CLM-027 | 認知履歴/log density | 記憶・言語報告候補 | なし | COR-2 | 単位・count/field復元なし | S06/S09/S16 Limits |
| CON-EC-014 | CON-CLM-028 | J_I/J_log | S16が神経/言語/主観報告をmap先に列挙 | なし | COR-2 | flowの抽出規則なし | S06 Mapping;S09 |
| CON-EC-015 | CON-CLM-029 | meaning potential | 意味負荷・言語ログ候補 | S15意味負荷方向 | COR-3 | metric/kernel/field再構成なし | S06 Mapping;S09 meaning wells |
| CON-EC-016 | CON-CLM-031 | 勾配による参照bias | 意味負荷刺激への参照候補 | semantic load差 | COR-3 | bias尺度/勾配推定なし | S09 Meaning Gradient / steps5–6 |
| CON-EC-017 | CON-CLM-033 | projectionで注意/選択/残余 | report選択・参照bias | report/意味負荷操作 | COR-3 | 共通operatorへの対応は未固定 | S06 Projection instances |
| CON-EC-018 | CON-CLM-034 | psychological projection | 心理的投射という名称 | なし | COR-1 | 構造比較のみ、共通observableなし | S06 Psychological Notion |
| CON-EC-019 | CON-CLM-036 | experienced qualia frontier | 赤/痛み/音/いまここ例 | なし | COR-1 | 例はfrontierを独立同定しない | S11 EN:64 / JA:72 |
| CON-EC-020 | CON-CLM-037 | gateのphenomenal surface | live/記憶/言語labelの対照 | なし | COR-2 | surfaceとreportのproxy validity未固定 | S11 gate / EN:114–118 |
| CON-EC-021 | CON-CLM-038 | qualiaのcentrality | いま意識している感じの例 | なし | COR-1 | SERIOUS-001の独立endpointなし | S11 EN:179/208–216;SERIOUS-001 |
| CON-EC-022 | CON-CLM-039 | qualia clarity/fixation | 主観的diffuse/clear/vivid対比 | T_Phi大小方向 | COR-3 | 強度scale・T_Phi入力未校正 | S11 Effective Torque |
| CON-EC-023 | CON-CLM-041 | unchanged live qualia | 記憶/報告をresidueとする候補 | storage/measurement対比 | COR-3 | live不変性の独立criterionなし | S11 storage;S13 Precision |
| CON-EC-024 | CON-CLM-042 | measurement→residue | 報告/label/number/neural summary | 報告・言語化・選択 | COR-3 | before/after live同定とresidue尺度なし | S13 Plasticity Closure;S11 |
| CON-EC-025 | CON-CLM-043 | precision→sedimentation | residue明確さ | 測定精度/要求強度差 | COR-3 | precisionとdemandを数値分離せず | S13 Precision;S15 Residue Shift |
| CON-EC-026 | CON-CLM-044 | introspectionによる変化 | 言語化/強度評価 | 注意を向ける/言語化 | COR-3 | 内省前endpoint/scoreなし | S13 Introspection |
| CON-EC-027 | CON-CLM-045 | self terrain/coherence | 合理化された説明/ログ候補 | なし | COR-2 | narrative coherence尺度なし | S10 Rationalization;S12 Self;S18 |
| CON-EC-028 | CON-CLM-046 | self continuity | 自己/時間連続性の報告候補 | なし | COR-2 | 自己感とログ同一性の独立mapなし | S12 Self;S18 Higher-Order |
| CON-EC-029 | CON-CLM-048 | reportの三条件 | 言語/行動応答 | 経路非対称の比較 | COR-3 | processing/log/path別々の同定なし | S09/S10 Reporting Bottleneck |
| CON-EC-030 | CON-CLM-049 | explicit consciousness必要条件 | 報告可能性 | 経路/遅延の比較 | COR-3 | report criterionを意識identityに流用できない | S10 summary/experimental correspondence |
| CON-EC-031 | CON-CLM-050 | readiness/運動/意図報告の時刻 | simultaneous brain recordingとtimestamp | 自由時点の手首/指運動という実験叙述 | COR-3 | 既存実験のschema再話のみ、原data/再現protocolなし | S10 Libet first paragraphs |
| CON-EC-032 | CON-CLM-051 | readiness=fast候補 | readiness potential候補 | なし | COR-2 | 神経signalからfast rate/attractorへのmapなし | S10 Libet |
| CON-EC-033 | CON-CLM-052 | 準備→log変換遅延 | 準備/運動/意図報告timestamp | 時刻順の比較 | COR-3 | tauのstart/end・mu・比例定数なし | S10 Libet EN:40–56 / JA:48–64 |
| CON-EC-034 | CON-CLM-053 | free will否定の含意を退ける | 直接対象/検出器なし | なし | COR-0 | negative/methodological scope、逆の実証なし | S10 Free Will/What Experiments Do Not Show |
| CON-EC-035 | CON-CLM-054 | consciousness opening時点 | 意図報告/log時刻候補 | なし | COR-2 | report時刻とopening時刻の独立区別なし | S10 Libet final |
| CON-EC-036 | CON-CLM-055 | 行動/言語応答の非対称 | 刺激・適切な行動・言語応答 | callosal disconnectionの実験叙述 | COR-3 | Con実験なし、実施protocol/dataなし | S10 Split-Brain first paragraphs |
| CON-EC-037 | CON-CLM-056 | blocked log route | 行動対言語報告 | 経路断絶の比較 | COR-3 | generic経路とlog媒介の区別なし | S10 Split-Brain / Reporting |
| CON-EC-038 | CON-CLM-057 | 意識は二重化しない | 主体数という対象名 | なし | COR-1 | 報告経路数とは別のsubject countingなし | S10 What Do Not Show;S15 Split-Brain |
| CON-EC-039 | CON-CLM-058 | retrospective rationalization | 行為後の言語説明 | なし | COR-2 | 原report例/data/採点なし | S10 Rationalization first paragraphs |
| CON-EC-040 | CON-CLM-059 | missing-log completion | 行為への説明のcoherence候補 | アクセス可能/不能の比較 | COR-3 | 不可視logとcoherenceの同時測定なし | S10 Rationalization interpretation |
| CON-EC-041 | CON-CLM-060 | 二実験からexplicit条件 | timing/経路/報告候補 | 時間差/断絶の比較 | COR-3 | 互換な説明以上のmodel-specific判別なし | S10 both evidence shows / final |
| CON-EC-042 | CON-CLM-061 | neural/bodily dependence | 神経・身体活動 | なし | COR-1 | 依存関係のCon-specific検査なし | S14 opening/local substrates |
| CON-EC-043 | CON-CLM-062 | nonlocal conscious regime | 複数局所活動と報告候補 | 時間関係の比較 | COR-3 | 同時coupling/意識criteria未固定 | S14 Local Substrates/Distributed |
| CON-EC-044 | CON-CLM-064 | same activity/context差→report差 | 局所活動・主観/行動報告 | 局所活動を同じとし時間/文脈条件比較 | COR-3 | 同じ活動の許容差/操作/判定なし | S15 Non-Local Regime Prediction |
| CON-EC-045 | CON-CLM-065 | automation/weak access | 熟練行動・報告安定性候補 | gap小方向 | COR-3 | gap独立抽出なし | S15 Synchronization;S16 same |
| CON-EC-046 | CON-CLM-066 | dreamlike fragmentation | 夢様/解離様報告候補 | gap大方向 | COR-3 | state/rate尺度なし | S15 Excessive Differential;S16 |
| CON-EC-047 | CON-CLM-067 | fixation/repetition | 反復思考/固定の経験例 | mu小方向 | COR-2 | mu操作を観測行為に落とす記述なし | S15 Viscosity;S16 Low Viscosity |
| CON-EC-048 | CON-CLM-068 | memory/report fragmentation | 保持困難/報告の不安定さ | mu大方向 | COR-3 | mu推定・保持/連続性scoreなし | S15 Viscosity;S16 High Viscosity |
| CON-EC-049 | CON-CLM-069 | self/time/report変化 | 自己/時間感・報告 | tau差/attention manipulation | COR-3 | 注意操作の具体条件/tau端点なし | S15 Delay/Testable Directions |
| CON-EC-050 | CON-CLM-070 | reference bias | 意味負荷刺激への参照 | 負荷差の比較 | COR-3 | 刺激集合/負荷量/bias metricなし | S15 Meaning/Testable Directions |
| CON-EC-051 | CON-CLM-071 | narrative/trauma-like fixation | 強い記憶/反復の経験例 | gradient大方向 | COR-2 | 臨床指標/gradient操作なし | S15 Meaning;S16 Excessive Gradient |
| CON-EC-052 | CON-CLM-072 | diffuse/exploration | 散漫/自由連想の経験例 | gradient弱方向 | COR-2 | 他変数との切り分け・scoreなし | S16 Weak Meaning |
| CON-EC-053 | CON-CLM-073 | residue shift | 主観報告/言語/数値評価 | 要求・選択肢・言語化の強度差 | COR-3 | dose・comparison condition・residue metricなし | S13 Experimental Implication;S15 Shift |
| CON-EC-054 | CON-CLM-074 | sleep/dream/anesthesia/dissociation | state名・report/神経候補 | 状態間比較方向 | COR-3 | 各stateの予測符号・独立分類なし | S15 Testable Directions |
| CON-EC-055 | CON-CLM-075 | phase diagram classification | report/state安定性候補 | gap/mu軸・tau/gradient比較 | COR-3 | membershipを実測計算するpipelineなし | S15 Phase Diagram/Testable Directions;FIG03 |
| CON-EC-056 | CON-CLM-077 | 異状態の共通gap構造 | 夢/解離等の経験例 | 比較方向のみ | COR-2 | 同じ構造を別々に測る共通尺度なし | S16 Excessive Difference |
| CON-EC-057 | CON-CLM-082 | older PDEがSSOを維持 | SSO persistence名 | なし | COR-1 | 局所解/witness/観測mapなし | S06 EN:319–321 |
| CON-EC-058 | CON-CLM-087 | qualia/insight同じboundary | qualiaと洞察の経験例 | なし | COR-1 | 共同observable/translationなし | S20 correspondence table;S11 |
| CON-EC-059 | CON-CLM-090 | Con→self→Intelligence | 自己/知能の名づけ | なし | COR-1 | 順序の独立指標・発達dataなし | S18 Toward;S20 |
| CON-EC-060 | CON-CLM-097 | qualitative research directionというscope | 固有の経験targetなし | 個別予測は別CLM | COR-0 | scope文自体を実証claimにしない | S15 opening/Testable Directions |
| CON-EC-061 | CON-CLM-101 | prediction必要/非十分 | 予測処理/意識の対象名 | なし | COR-1 | 独立必要性testなし | S18 Predictive Processing |
| CON-EC-062 | CON-CLM-103 | JA weighted attention近似 | 注意の重み/massという説明 | なし | COR-1 | weightを推定する規則なし | JA S05;CON-EQ-079–081 |
| CON-EC-063 | CON-CLM-104 | JA C(t) opening function | openingという現象label | gap消失の形式方向のみ | COR-1 | 観測seriesとしてのC(t)なし | JA S07/S13;CON-EQ-101/140 |
| CON-EC-064 | CON-CLM-105 | 図access/意識領域 | conscious access/意識label | schematic phase境界 | COR-1 | 図のラベルはempirical classifierでない | FIG03/FIG06 vs S07;Phase02 RCF017–019 |

## 4. Observable inventory

| CON-OBSV | Candidate | Source | Target/proxy | Variable link | Operational definition |
| --- | --- | --- | --- | --- | --- |
| CON-OBSV-001 | neural activity | S13/S14 Local Substrates | direct recording target; consciousness proxy | v_f/v_s候補 | NO carrier/filter/extraction |
| CON-OBSV-002 | readiness potential | S10 Libet | recorded eventの再話; fast候補 | v_f/tau | NO onset rule |
| CON-OBSV-003 | 準備/運動/意図報告のtiming | S10 Libet | direct timing target; log proxy | tau | NO endpoint/calibration |
| CON-OBSV-004 | verbal report | S09/S10 | direct output; access proxy | logs/J_log | NO coding/score |
| CON-OBSV-005 | behavioral report | S10/S15 Non-Local | direct response; processing proxy | path/log | NO task criteria |
| CON-OBSV-006 | subjective report | S13/S15 Testable | direct report; state proxy | window | NO standardized protocol |
| CON-OBSV-007 | attention manipulation | S13 Experimental;S15 Testable | intervention candidate | tau/T_Phi | NO manipulation levels |
| CON-OBSV-008 | semantic load | S13/S15 | intervention candidate | Phi/gradient | NO stimulus scale |
| CON-OBSV-009 | sleep/dream/anesthesia | S15 Testable | named state comparison | gap/mu/tau | NO classifier/direction per state |
| CON-OBSV-010 | dissociation-like report | S15/S16 | analogy/report candidate | gap | NO diagnostic/score |
| CON-OBSV-011 | report demand intensity | S13/S15 Shift | intervention candidate | residue/window | NO dose |
| CON-OBSV-012 | measurement precision | S13 Precision | method attribute; intervention candidate | residue | NO unit/separation from demand |
| CON-OBSV-013 | memory/log residue | S11/S13 | recorded target; live proxy | I/J_log | NO counting/metric |
| CON-OBSV-014 | reaction time | S13 Measurement Is Not Error | named outcome, not selected tau identity | tau relation UNRESOLVED | NO event/task mapping |
| CON-OBSV-015 | pathway asymmetry | S10/S15 Split-Brain | verbal/behavioral contrast | log/report path | NO Con pathway extraction |
| CON-OBSV-016 | local activity pattern | S13 before/after;S15 Non-Local | recording target; matching variable | temporal coupling | NO sameness tolerance |
| CON-OBSV-017 | self/time-sense report | S15 Delay;S16 High Viscosity | subjective proxy | tau/mu | NO scale |
| CON-OBSV-018 | qualia clarity/vividness | S11 Effective Torque | phenomenal/report candidate | T_Phi | NO scoring |
| CON-OBSV-019 | narrative coherence/rationalization | S10 Rationalization | linguistic output proxy | self/log terrain | NO coherence metric |
| CON-OBSV-020 | report options/numerical rating/verbalization | S13 Plasticity;S15 Shift | report form/manipulation candidate | residue | NO response categories/rating anchors |

## 5. Variable-to-observable map

| CON-MAP | Variable | Proposed observable | Mapping type | Units known? | Extraction rule? | Status / source |
| --- | --- | --- | --- | --- | --- | --- |
| CON-MAP-001 | v_f | fast prediction/neural activity | verbal role | NO | NO | VERBAL ONLY;S03/S14 |
| CON-MAP-002 | v_s | slow memory/neural substrate | verbal role | NO | NO | VERBAL ONLY;S03/S14 |
| CON-MAP-003 | Delta v | neural timescale difference/report stability | proxy候補 | NO common rate unit | difference式のみ、rate抽出なし | PROXY CANDIDATE;S15 Testable |
| CON-MAP-004 | mu | slip/coupling・固定/断片化 | verbal index | dimensionless明記なし | NO | VERBAL ONLY;S05/S15 |
| CON-MAP-005 | tau | 準備/報告遅延 | proxy候補 | 時間的意味ありunit未指定 | start/end未固定 | PROXY CANDIDATE;S10/S13 |
| CON-MAP-006 | I | 言語/主観報告/認知ログ | proxy候補 | NO density unit | NO counting | PROXY CANDIDATE;S06/S16 |
| CON-MAP-007 | J_I | 神経/言語/主観報告 | map先候補 | NO | NO event-current rule | PROXY CANDIDATE;S16 Limits |
| CON-MAP-008 | J_log | referencing/report flow | map先候補 | NO | NO | PROXY CANDIDATE;S16 Limits |
| CON-MAP-009 | Phi | 意味構造/言語ログ | proxy候補 | NO | NO field reconstruction | PROXY CANDIDATE;S09/S18 |
| CON-MAP-010 | gradient Phi | semantic load/reference bias | proxy候補 | NO metric | NO spatial/semantic derivative extraction | PROXY CANDIDATE;S15 |
| CON-MAP-011 | mathcal T | attention変換負荷 | formal index | NO physical torque unit | NO input extraction | VERBAL ONLY;S05 |
| CON-MAP-012 | mathcal T_Phi | clarity/bias/attention | proxy候補 | NO | S16明示未確立 | PROXY CANDIDATE;S11/S16 |
| CON-MAP-013 | C_f | fast closure degree | effective formal degree | bounded rangeとphysical unitは別 | NO neural aggregate | NONE;S06 |
| CON-MAP-014 | C_s | slow closure degree | effective formal degree | bounded rangeとphysical unitは別 | NO neural aggregate | NONE;S06 |
| CON-MAP-015 | Delta C | closure mismatch | formal counterpart | difference-defined | NO rate-to-closure map | NONE;S06 |
| CON-MAP-016 | JA C(t) | opening/nonclosure | labelled function | unit未固定 | NO conscious-state timeseries | VERBAL ONLY;JA S07/S13 |

NONEは観測mapの状態であり、C_f/C_s/Delta Cの形式定義を消す意味ではない。PARTIAL OPERATIONAL以上の変数mapは0。tauの時間語、muの比、closureのboundednessから単位や無次元性を監査者が補わない。

## 6. Fast / slow observability

| FS-OBS | Object/question | Source answer | Independent of conscious label? | Gap |
| --- | --- | --- | --- | --- |
| FS-OBS-001 | v_fの測定対象 | S03 fast predictive/reactive;S14 neural substrate | 役割は先に置かれるが測定はNO | 振動/反応rate/処理latencyのどれかを選ぶ記述なし |
| FS-OBS-002 | v_sの測定対象 | S03 sedimentary/stabilizing;S09 logs | slowという役割と観測分類は別 | memory更新event・rate単位なし |
| FS-OBS-003 | Delta v | S04/S07 difference;S15 neural timescale/report対応方向 | symbolicには独立、観測上UNRESOLVED | 二rateの共通座標/窓長なし |
| FS-OBS-004 | synchrony/dissociation | S15極限と状態例 | 状態例からgapを逆算するとtarget依存 | 独立rate抽出を供給せず |
| FS-OBS-005 | Bio由来 | S04 proposed interpretation, not dedicated result | Bio closureでは校正できない | Bio toy timestepをvf/vsへ移さない |

## 7. Tau observability

| TAU-EVID | Use | Observable events | Units | Operational status |
| --- | --- | --- | --- | --- |
| TAU-EVID-001 | internal buffer/retention | S03処理と保持の関係 | physical unit未指定 | model delay、experienced timeそのものではない |
| TAU-EVID-002 | Delta v/mu relation | S05/S07入力のrate/coupling | 比例定数・各unit未固定 | formal proportional relationのみ |
| TAU-EVID-003 | Libet timing | S10 readiness/運動/意図報告 | timestamp言及、数値単位/端点なし | proxy;readiness onsetから報告までと一意定義しない |
| TAU-EVID-004 | reportable-log conversion | S13 Experimentalのlive→log | start live同定/stop log同定未固定 | report timing候補 |
| TAU-EVID-005 | attention manipulation | S15 Testable tau変化 | 未指定 | 操作方向あり、task/doseなし |
| TAU-EVID-006 | self/time sense | S15 Delay Window | 経験時間の尺度なし | 小/大tauの対比、tau=subjective timeではない |

## 8. Mu observability

| MU-OBS | Question | Located content | Operational status |
| --- | --- | --- | --- |
| MU-OBS-001 | dimensionless? | S03/S05 coupling viscosity、比に現れる | 無次元とは明記されない |
| MU-OBS-002 | performance/cross-layer lagから推定? | S15低mu固定/高mu断片化の傾向 | estimatorなし;結果から定義する逆算をしない |
| MU-OBS-003 | coupling strengthとして測る? | S05 slip/coupling metaphor/index | 信号pair・結合metric・calibrationなし |

## 9. T / T_Phi observability

| TPHI-OBS | Element | Formal definition / source | Observable candidate | Operational gap |
| --- | --- | --- | --- | --- |
| TPHI-OBS-001 | mathcal T | S05 mathcal T = kappa Delta v/mu | attention変換 | physical torqueではなくeffective量;入力とkappa校正なし |
| TPHI-OBS-002 | mathcal T_Phi | S05/S07 mathcal T_Phi ∼ kappa (Delta v/mu) magnitude(gradient Phi) | S11 diffuse/clear/fixed;S13 attention操作 | 式があることと計測量は別 |
| TPHI-OBS-003 | rate/viscosity inputs | v_f,v_s,mu | neural timing/report候補 | CON-MAP-001–004未固定 |
| TPHI-OBS-004 | gradient input | Phiのgradient magnitude | 意味負荷・参照bias | metric/kernel/field復元なし |
| TPHI-OBS-005 | output / JA variants | S11 qualia clarity;JA S05 weighted attention | vividness/重みの語 | 単位・採点・変種の測定同定なし |
| TPHI-OBS-006 | explicit limit | S16 Limits;S18 Remaining Questions | neural/bodily/subjective/linguistic mapping候補 | “not a concrete measurable quantity”;JA同趣旨 |

上表の式は既存sourceの転記説明であり、新しい計算式や推定法ではない。S16の明示的未確立をS15のqualitative predictionで閉じない。

## 10. I / Phi observability

| IPHI-OBS | Object | Suggested target / source | Located formal support | Missing operational element |
| --- | --- | --- | --- | --- |
| IPHI-OBS-001 | I/log density | S06/S09記憶・再参照可能ログ | density naming / balance | log counting/単位/独立trace検出 |
| IPHI-OBS-002 | J_I / J_log | S16 neural/linguistic/subjective report | effective flow slots | event aggregation/current estimation |
| IPHI-OBS-003 | Phi/meaning wells | S06/S09意味・narrative terrain | potential/kernel template | semantic score/embedding/domain metric |
| IPHI-OBS-004 | gradient/reference bias | S09/S15意味負荷刺激 | gradient方向の関係 | field reconstruction/derivative/behavior metric |
| IPHI-OBS-005 | K and field reconstruction | S06 K*I | convolution template | kernel estimation/fit/data |
| IPHI-OBS-006 | CT inheritance | S09 CT Phi-star/gradient比較 | source-correspondence | CT実装をConデータpipelineに使う記述なし |

## 11. Consciousness-window testability

| WIN-TEST | Variable / condition | Observable | Manipulable? source status | Threshold known? | Positive/negative criterion | Executed? |
| --- | --- | --- | --- | --- | --- | --- |
| WIN-TEST-001 | Delta v | neural timescale/report | 差の方向、抽出・介入未固定 | symbolic only | 同期/分離の名称、independent labelsなし | NO |
| WIN-TEST-002 | mu | coupling/fixation/fragment | indexの大小のみ | symbolic only | 固定/断片化例、metricなし | NO |
| WIN-TEST-003 | tau | report/準備遅延 | attention操作方向 | symbolic only | self/time/report安定性のscoreなし | NO |
| WIN-TEST-004 | T_Phi | clarity/reference bias | attention/意味負荷方向 | symbolic only | clear/diffuse/fixedのscoreなし | NO |
| WIN-TEST-005 | joint iff | tuple/window | S15 phase-axis比較 | numerical membershipなし | 意識/非意識ラベルを独立に決める規則なし | NO |
| WIN-TEST-006 | figure phase region | FIG03/06 labels | 操作protocolではない | 図境界はcalibrated thresholdでない | EN access/JA意識差保持 | NO |

任意の数値・boundを外から与えれば不等式の真偽は計算できる。しかしsourceが観測からtuple・bound・conscious/nonconscious labelsを独立抽出する方法は未供給であり、current repositoryのみでempirical iff分類testを実行することはできない。これは式の矛盾判定でも意識の反証でもない。

## 12. Report as proxy

| REPORT-REL | From | To | Source relation | Criterion drift guard |
| --- | --- | --- | --- | --- |
| REPORT-REL-001 | conscious state | reportability | S09/S10 externalization, not identity | report有無をstate有無へ双方向変換しない |
| REPORT-REL-002 | conscious access | report | S09一部の外部化 | accessと報告行為は別 |
| REPORT-REL-003 | explicit consciousness | log/reference/path | S10 only after/necessary wording | 意識criterionを同じreport条件で定義すると独立検査にならない |
| REPORT-REL-004 | processing | behavioral report | S10 behavior shows processing | processing evidence≠phenomenal identity |
| REPORT-REL-005 | processing | verbal report | S10 route制限で不可能もある | no verbal report≠no processing |
| REPORT-REL-006 | qualia live | subjective report | S11/S13 reportはresidue | proxyがtargetをそのまま保存するとはしない |
| REPORT-REL-007 | reportability | actual verbal/behavioral report | S10 pathway条件 | 能力と実際の応答は別 |
| REPORT-REL-008 | introspection | report/log residue | S13 internal measurement | 前のlive state同定は別課題 |
| REPORT-REL-009 | report as evidence | explicit consciousness condition | S10 evidence showsとの記述 | reportを否定しないが、ログ/経験の独立criterionが必要 |

## 13. Qualia observability

| Q-OBS | Phenomenal claim | Observable proxy | Independent criterion? | Manipulation / source | PH-COR |
| --- | --- | --- | --- | --- | --- |
| Q-OBS-001 | frontier experienced as qualia (036) | 赤/痛み/音/いまここ例 | NO | S11経験例、なし | PH-COR-1 |
| Q-OBS-002 | phenomenal surface/gate (037) | liveとmemory/labelのreport候補 | NO | S11 gateの状態説明、測定手順なし | PH-COR-2 |
| Q-OBS-003 | centrality explanation (038) | いま意識している感じ | NO | S11 Why Qualia Feel Central | PH-COR-1 |
| Q-OBS-004 | clarity/vividness (039) | diffuse/clear/fixed主観対比 | NO scoring | S11 low/intermediate/high T_Phi | PH-COR-3 |
| Q-OBS-005 | unchanged storage/capture (041) | memory/report residue | NO live-invariance rule | S11/S13 measurement対比 | PH-COR-3 |
| Q-OBS-006 | measurement transformation (042) | label/number/neural summary/report | NO live identity | S13 before/after;S15 demand差 | PH-COR-3 |
| Q-OBS-007 | introspection (044) | 感覚の言語化/強度評価 | NO | S13注意/言語化対比 | PH-COR-3 |
| Q-OBS-008 | qualia/insight (087) | 経験例の比較 | NO common endpoint | S20 source analogy | PH-COR-1 |

PH-COR3は固定されたreport scaleではない。redness/pain例をparticipant dataと数えず、sourceの“experienced as”を独立criterionに使わない。SERIOUS-001 / CON-CIR-016は定義readingと説明readingを併存させ、後者のendpoint同定を未解決のまま扱う。

## 14. Measurement / residue operational audit

| RES-OBS | Claim | Manipulation | Outcome | Protocol specificity | Current level |
| --- | --- | --- | --- | --- | --- |
| RES-OBS-001 | measurement intensity | 報告/選択/数値化/言語化 | report/log residue | 操作の種類、dose/採点なし | COR-3;S13 |
| RES-OBS-002 | report demand difference | 要求を強める | content/residue差 | 比較方向、control条件なし | COR-3;S15 Shift |
| RES-OBS-003 | precision | 精度向上 | residue明確さ | precision unitとdemandの独立性なし | COR-3;S13 Precision |
| RES-OBS-004 | before/after | 報告する | neural pattern | 前後比較軸、時刻窓/metricなし | COR-3;S13 Experimental |
| RES-OBS-005 | live proxy | measurement前state | 後のqualia-like report | 独立したlive indicatorなし | COR-2;S11/S13 |
| RES-OBS-006 | residue metric | semantic load/言語化 | ログ/label/number | 形式列挙のみ、score/countなし | COR-3;S13 Experimental |
| RES-OBS-007 | control condition | 同じ経験でreport形式差 | 残るログの差 | same experience照合・control固定なし | COR-3;S15 Shift |

## 15. Libet correspondence

| LIB-COR | Empirical event | Model mapping | Alternative compatibility (source-local) | Distinctive prediction? | COR |
| --- | --- | --- | --- | --- | --- |
| LIB-COR-001 | readiness before movement/report | fast候補 | S10自身が単一timeline解釈も紹介 | 候補形成の独立測定なし | COR-2 |
| LIB-COR-002 | voluntary wrist/finger + intention timestamp | slow reportable log | 記載されたdelayだけでも順序は表せる | Con固有testではない | COR-3 |
| LIB-COR-003 | preparation/report interval | tau proportional ratio | 単なる観測間隔と変換delayを分離せず | mu/率fitがなく区別未固定 | COR-3 |
| LIB-COR-004 | opening at transformation | phenomenal opening | report時刻とは独立のendpointが必要 | 反例を判定するcriterionなし | COR-2 |
| LIB-COR-005 | free-will inference | 問の再設定 | S10のinterpretations間の論点 | 検査可能なfree-will指標なし | COR-0 |

歴史的正確性・外部Libet研究の評価は行わない。反証方向として「tauとされた区間がratio/報告変換に対応しない」は考えられるが、これはsource関係の論理的否定を記した監査上の問いであり、新protocolではない。区間・rate・couplingの独立抽出なしに実行できない。dedicated citation/raw timestamps/source-specific fitは所在しない。

## 16. Split-brain correspondence

| SPLIT-COR | Event | Model mapping | Compatibility / distinction | Counter-observation status | COR |
| --- | --- | --- | --- | --- | --- |
| SPLIT-COR-001 | 刺激への適切行動/言語不能 | processing/report分離 | generic経路遮断の記述とも両立 | log mediatorを別測定する規則なし | COR-3 |
| SPLIT-COR-002 | callosal disconnection | log/reference route非対称 | neural routeとformal log flowのidentity未固定 | path別予測を数値化せず | COR-3 |
| SPLIT-COR-003 | inaccessible actionの説明 | slow coherence completion | 後付説明という現象名との適合 | coherence/log欠落の独立尺度なし | COR-3 |
| SPLIT-COR-004 | explicit consciousness | log/pathに到達する処理 | 報告不能と意識不能のcriterion drift | report以外のcriterion未固定 | COR-2 |
| SPLIT-COR-005 | not two consciousnesses | 主体数の解釈 | 経路数とsubject数は別 | 独立subject countingなし | COR-1 |

## 17. Neural-correlate correspondence

| NEURAL-COR | Object | Candidate / source | Level | Gap |
| --- | --- | --- | --- | --- |
| NEURAL-COR-001 | fast | neural prediction/reactive activity;S14 | COR-1 | site/frequency/event未選択 |
| NEURAL-COR-002 | slow | neural/bodily memory substrate;S14 | COR-1 | carrier/retention extraction未選択 |
| NEURAL-COR-003 | coupling | 時間関係;S14/S15 | COR-2 | pair/lag/strength metricなし |
| NEURAL-COR-004 | sedimentation | report前後神経pattern;S13 | COR-3 | pattern差をlog形成と同定するruleなし |
| NEURAL-COR-005 | meaning gradient | semantic load/behavior;S15/S16 | COR-2 | 神経gradient reconstructionなし |
| NEURAL-COR-006 | across sites | same local activity/context difference;S15 | COR-3 | 同じ活動条件/temporal control未固定 |
| NEURAL-COR-007 | NCC identity | S14相関と意識を分離 | COR-1 | 非同一性guardはpositive regime検証ではない |

## 18. Altered-state correspondence

| ALT-COR | State | Predicted parameter direction | Observable named? | Differentiating prediction? | Test status |
| --- | --- | --- | --- | --- | --- |
| ALT-COR-001 | sleep | S15状態間gap/mu/tau比較のみ、符号なし | state名 | NO | 未実行、診断/手順なし |
| ALT-COR-002 | dream | S15/S16大gapとの類似 | fragmentation/report候補 | 独立classifierなし | 未実行 |
| ALT-COR-003 | daydream | S15/S16大gap | association/fragmentation例 | 夢との判別条件なし | 未実行 |
| ALT-COR-004 | anesthesia | S15比較方向のみ、符号なし | state名 | NO | 未実行;新介入を提案しない |
| ALT-COR-005 | dissociation | S15/S16大gap類比 | self/time/report候補 | 診断同定をsourceが否定 | 未実行 |
| ALT-COR-006 | hallucination-like | S15/S16大gap類比 | 像/連想/fragmentation例 | 状態を同一化しない | 未実行 |
| ALT-COR-007 | skilled/automatic action | S16 gap小 | 熟練/習慣行動 | 独立rate/報告尺度なし | 未実行 |
| ALT-COR-008 | immersion | S16大gap類比 | immersive experience例 | 他状態と判別未固定 | 未実行 |

## 19. Self / ego correspondence

| SELF-COR | Claim | Proxy located | What not supplied | PH-COR |
| --- | --- | --- | --- | --- |
| SELF-COR-001 | ego transformation point;S05/S08 | 経験される位置という名 | 位置scale/neural proxy | PH-COR-0 |
| SELF-COR-002 | self terrain;S12 | 記憶/物語の経験例 | terrain metric | PH-COR-1 |
| SELF-COR-003 | self continuity;S12/S16 | 自己/時間連続性報告候補 | 尺度/score | PH-COR-2 |
| SELF-COR-004 | rationalization;S10 | 行為後の言語説明 | 語りのcoherence metric | PH-COR-2 |
| SELF-COR-005 | reportable self;S10/S12 | ログ外部化の報告 | self同定と報告経路の独立判定 | PH-COR-2 |

## 20. Phenomenological contrasts

| PH-CONTRAST | Contrast | Claimed driver | Report/observable candidate | Structured test? |
| --- | --- | --- | --- | --- |
| PH-CONTRAST-001 | vivid/diffuse | T_Phi/gradient;S11 | clarity報告候補 | 方向対比のみ、scaleなし |
| PH-CONTRAST-002 | fixed/flexible | mu/gradient;S16 | 反復/再解釈例 | 採点/操作なし |
| PH-CONTRAST-003 | continuous/fragmented | gap/mu;S15 | report continuity | 比較方向のみ |
| PH-CONTRAST-004 | immediate/delayed | tau;S15 | 反応/報告遅れ | start/endなし |
| PH-CONTRAST-005 | reportable/unreportable | path;S10 | verbal/behavior | 実験再話、Con protocolなし |
| PH-CONTRAST-006 | live/sedimented | measurement;S13 | 前後report/residue | 独立live criterionなし |
| PH-CONTRAST-007 | self-continuous/unstable | tau/mu;S15/S16 | self/time感 | report scaleなし |
| PH-CONTRAST-008 | automatic/conscious | small gap;S15/S16 | 熟練行動/report候補 | 意識criterion別途必要 |
| PH-CONTRAST-009 | dreamlike/stable | large gap/window;S15 | state/report例 | state classifierなし |

## 21. Falsifiability structure

Phase04 HB28を全件対象。以下「反する結果」はsourceの主張の論理的否定を監査者が記述した条件文であり、実施提案・独立criterionの新設ではない。CLEARには観測対象と否定条件が独立に固定される必要があるため現在0。sourceはresidue比較を許すので、理論全体があらゆる反証を構造的に拒むとは認定しない。

| FALS-ID | Phase04 HB / claim | Result against claim (conditional) | Source countercondition / independence gap | Classification |
| --- | --- | --- | --- | --- |
| FALS-001 | HB-001 / CON-CLM-002 | log参照と独立の意識判定が一致しない | S00;S06 interface;S09 opening;S12; 意識の独立criterionなし | TARGET-DEPENDENT |
| FALS-002 | HB-002 / CON-CLM-004 | window内で独立意識ラベルがnegative又は外でpositive | S15 Summary;CON-EQ-067/161; tuple/閾値/ラベル未固定 | TARGET-DEPENDENT |
| FALS-003 | HB-003 / CON-CLM-015 | SSOなしで独立した意識状態 | S04 final paragraphs; SSO検出と意識criterionなし | TARGET-DEPENDENT |
| FALS-004 | HB-004 / CON-CLM-016 | 三条件ありでも意識negative | S06 SSO as Local Non-Closure; 条件の操作化なし | TARGET-DEPENDENT |
| FALS-005 | HB-005 / CON-CLM-019 | loop持続と意識持続が分離 | S09 loop/persistence; 時間/loop/stateのmetricなし | PARTIAL COUNTERCONDITION |
| FALS-006 | HB-006 / CON-CLM-023 | TCA変化とattention結果が分離 | S05 ending;S06 Coupler; effective入力未測定 | PARTIAL COUNTERCONDITION |
| FALS-007 | HB-007 / CON-CLM-024 | 変換位置と経験egoが対応しない | S05 From Attention to Ego;S08; 位置/ego criterionなし | TARGET-DEPENDENT |
| FALS-008 | HB-008 / CON-CLM-036 | frontierと独立qualiaが対応しない | S11 EN:64 / JA:72; endpoint命名が独立でない | TARGET-DEPENDENT |
| FALS-009 | HB-009 / CON-CLM-037 | gate通過とsurface経験が分離 | S11 gate / EN:114–118; surface criterionなし | TARGET-DEPENDENT |
| FALS-010 | HB-010 / CON-CLM-038 | frontierの有無とcentralityが分離 | S11 EN:179/208–216;SERIOUS-001; SERIOUS-001の独立endpointなし | TARGET-DEPENDENT |
| FALS-011 | HB-011 / CON-CLM-039 | T_Phi大小とclear/diffuse/fixed対比が逆又は無関係 | S11 Effective Torque; index/clarity scoreなし | PARTIAL COUNTERCONDITION |
| FALS-012 | HB-012 / CON-CLM-041 | unchanged live captureが成立 | S11 storage;S13 Precision; 全記録をresidueと読む分類が独立不変性testを困難化 | MEASUREMENT LOOP RISK |
| FALS-013 | HB-013 / CON-CLM-042 | 測定でlive/residue変化なし | S13 Plasticity Closure;S11; liveを独立同定できずresidue側だけ比較可 | MEASUREMENT LOOP RISK |
| FALS-014 | HB-014 / CON-CLM-043 | 精度/要求増でもresidue明確化が起きない | S13 Precision;S15 Residue Shift; directionはあるがmetric/doseなし | PARTIAL COUNTERCONDITION |
| FALS-015 | HB-015 / CON-CLM-044 | 内省で対象変化なし | S13 Introspection; 前のlive stateと同一性基準なし | MEASUREMENT LOOP RISK |
| FALS-016 | HB-016 / CON-CLM-046 | ログ連続性とself経験連続性が分離 | S12 Self;S18 Higher-Order; 双方の独立尺度なし | TARGET-DEPENDENT |
| FALS-017 | HB-017 / CON-CLM-049 | ログ参照なしでexplicit consciousness | S10 summary/experimental correspondence; report=criterionの流用risk | TARGET-DEPENDENT |
| FALS-018 | HB-018 / CON-CLM-052 | 観測遅延がratio/変換と対応しない | S10 Libet EN:40–56 / JA:48–64; tau端点/mu/率なし | PARTIAL COUNTERCONDITION |
| FALS-019 | HB-019 / CON-CLM-054 | opening時点がlog変換と分離 | S10 Libet final; report以外のopening markerなし | TARGET-DEPENDENT |
| FALS-020 | HB-020 / CON-CLM-057 | 独立に二主体と同定される | S10 What Do Not Show;S15 Split-Brain; subject countingなし | TARGET-DEPENDENT |
| FALS-021 | HB-021 / CON-CLM-060 | 実験のreportが必要log条件なしで起きる | S10 both evidence shows / final; log未測定/意識criterion依存 | TARGET-DEPENDENT |
| FALS-022 | HB-022 / CON-CLM-062 | 時間結合差がreport差を伴わない | S14 Local Substrates/Distributed; 同じ活動とcouplingのmetricなし | PARTIAL COUNTERCONDITION |
| FALS-023 | HB-023 / CON-CLM-077 | 列挙状態間で共通gap構造なし | S16 Excessive Difference; 各state/rate共通測定なし | PARTIAL COUNTERCONDITION |
| FALS-024 | HB-024 / CON-CLM-080 | rate条件とclosure条件が対応しない | S06 FIG06 caption; common domain/mapなし、sourceはdiscriminating test未記載 | NO COUNTERCONDITION LOCATED |
| FALS-025 | HB-025 / CON-CLM-082 | PDE項からSSO維持へ対応しない | S06 EN:319–321; SSO specialization/witnessなし | NO COUNTERCONDITION LOCATED |
| FALS-026 | HB-026 / CON-CLM-086 | 同一量として共同比較できない | S09 CT §4.4; 量の共通unit/metricなし | NO COUNTERCONDITION LOCATED |
| FALS-027 | HB-027 / CON-CLM-087 | 洞察とqualiaの独立boundaryが非対応 | S20 correspondence table;S11; 共同phenomenal/semantic criterionなし | TARGET-DEPENDENT |
| FALS-028 | HB-028 / CON-CLM-089 | ある層に同型構造がない | S06 final;S18:223;S20:31; 同型を判別するinvariant/mapなし | NO COUNTERCONDITION LOCATED |

## 22. Measurement-loop structure

| MEAS-LOOP | Question | Source structure | Possible test path / gap | Conclusion |
| --- | --- | --- | --- | --- |
| MEAS-LOOP-001 | 全measurementがliveを変えるか | S13分類上全記録residue | live同一性が独立でない | CON-CIR-019のrisk保持 |
| MEAS-LOOP-002 | どの観測も理論支持になるか | S13精度成功でlive消失という読み | あらゆる結果をconfirmとする明文なし | global unfalsifiabilityは未確立 |
| MEAS-LOOP-003 | residue比較が独立経路か | S13ログは分析/比較/統計可能 | 報告要求差→residue差は比較方向を与える | 部分的test経路、metricは未固定 |
| MEAS-LOOP-004 | 何が失敗しうるか | S15 stronger demand changes logs | 独立要求/残余尺度を固定後、差なし/反対差が方向claimと緊張 | 条件付き反証方向のみ、phenomenal identityを自動反証しない |

## 23. Distinctive prediction audit

CON-PRED001–018はPhase04のIDをそのまま用いる。competing-compatibleとはsource自身にある「単なるdelay」「経路断絶」「一般的な負荷/報告変化」とも整合するという論理上の指摘で、外部競合理論を導入した比較ではない。model独特の語彙はquantitatively discriminating predictionと同じではない。

| PRED-DISC | CON-PRED | CON-CLM / prediction | Distinctiveness | Competing-compatible? | Operational gap |
| --- | --- | --- | --- | --- | --- |
| PRED-DISC-001 | CON-PRED-001 | CON-CLM-065 / Delta v small | DIRECTIONAL BUT NONUNIQUE | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | 変数抽出・対照・判別outcome/閾値なし |
| PRED-DISC-002 | CON-PRED-002 | CON-CLM-066 / Delta v large | DIRECTIONAL BUT NONUNIQUE | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | 変数抽出・対照・判別outcome/閾値なし |
| PRED-DISC-003 | CON-PRED-003 | CON-CLM-067 / mu low | DIRECTIONAL BUT NONUNIQUE | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | 変数抽出・対照・判別outcome/閾値なし |
| PRED-DISC-004 | CON-PRED-004 | CON-CLM-068 / mu high | DIRECTIONAL BUT NONUNIQUE | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | 変数抽出・対照・判別outcome/閾値なし |
| PRED-DISC-005 | CON-PRED-005 | CON-CLM-069 / tau too small | DIRECTIONAL BUT NONUNIQUE | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | 変数抽出・対照・判別outcome/閾値なし |
| PRED-DISC-006 | CON-PRED-006 | CON-CLM-069 / tau too large | DIRECTIONAL BUT NONUNIQUE | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | 変数抽出・対照・判別outcome/閾値なし |
| PRED-DISC-007 | CON-PRED-007 | CON-CLM-069 / attention manipulation / tau | DIRECTIONAL BUT NONUNIQUE | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | 変数抽出・対照・判別outcome/閾値なし |
| PRED-DISC-008 | CON-PRED-008 | CON-CLM-070 / semantic load / gradient | DIRECTIONAL BUT NONUNIQUE | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | 変数抽出・対照・判別outcome/閾値なし |
| PRED-DISC-009 | CON-PRED-009 | CON-CLM-071 / gradient excessive | DIRECTIONAL BUT NONUNIQUE | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | 変数抽出・対照・判別outcome/閾値なし |
| PRED-DISC-010 | CON-PRED-010 | CON-CLM-072 / gradient weak | DIRECTIONAL BUT NONUNIQUE | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | 変数抽出・対照・判別outcome/閾値なし |
| PRED-DISC-011 | CON-PRED-011 | CON-CLM-042 / measurement operation | UNTESTABLE AS WRITTEN | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | live target独立同定なし |
| PRED-DISC-012 | CON-PRED-012 | CON-CLM-073 / report demand intensity | DIRECTIONAL BUT NONUNIQUE | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | 変数抽出・対照・判別outcome/閾値なし |
| PRED-DISC-013 | CON-PRED-013 | CON-CLM-043 / measurement precision | DIRECTIONAL BUT NONUNIQUE | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | 変数抽出・対照・判別outcome/閾値なし |
| PRED-DISC-014 | CON-PRED-014 | CON-CLM-056 / report-pathway disruption | GENERIC COMPATIBILITY | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | 変数抽出・対照・判別outcome/閾値なし |
| PRED-DISC-015 | CON-PRED-015 | CON-CLM-059 / inaccessible logs | GENERIC COMPATIBILITY | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | 変数抽出・対照・判別outcome/閾値なし |
| PRED-DISC-016 | CON-PRED-016 | CON-CLM-064 / same local activity; temporal conditions varied | DIRECTIONAL BUT NONUNIQUE | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | 変数抽出・対照・判別outcome/閾値なし |
| PRED-DISC-017 | CON-PRED-017 | CON-CLM-074 / sleep/dream/anesthesia/dissociation windows | GENERIC COMPATIBILITY | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | 変数抽出・対照・判別outcome/閾値なし |
| PRED-DISC-018 | CON-PRED-018 | CON-CLM-075 / phase axes gap/mu; tau/gradient controls | UNTESTABLE AS WRITTEN | YES: source内の一般的delay/負荷/経路/状態変化と識別未固定 | window membership/独立state labelなし |

## 24. Prediction maturity

PM3は操作・対比・outcomeのsketchに限る。これはPhase04の「full protocolなし」と矛盾しない。PM4実行可能protocol、PM5収集、PM6検定、PM7反復はすべて0。

| CON-PRED | Prediction / named target | PM | Located specificity / gap |
| --- | --- | --- | --- |
| CON-PRED-001 | Delta v small / automation / report stability | PM2 | observable/state名あり、操作/抽出/判定手順なし; S15 Synchronization;S16 same |
| CON-PRED-002 | Delta v large / dream-like fragmentation | PM2 | observable/state名あり、操作/抽出/判定手順なし; S15 Excessive Differential;S16 |
| CON-PRED-003 | mu low / fixation / repetition | PM2 | observable/state名あり、操作/抽出/判定手順なし; S15 Viscosity;S16 Low Viscosity |
| CON-PRED-004 | mu high / memory / report fragmentation | PM2 | observable/state名あり、操作/抽出/判定手順なし; S15 Viscosity;S16 High Viscosity |
| CON-PRED-005 | tau too small / immediate reaction / weak referencing | PM2 | observable/state名あり、操作/抽出/判定手順なし; S15 Delay/Testable Directions |
| CON-PRED-006 | tau too large / time/self/report coherence | PM2 | observable/state名あり、操作/抽出/判定手順なし; S15 Delay/Testable Directions |
| CON-PRED-007 | attention manipulation / tau / delay and report changes | PM3 | 操作/比較/outcomeのsketchあり、量/手順/score/control未固定; S15 Delay/Testable Directions |
| CON-PRED-008 | semantic load / gradient / reference bias | PM3 | 操作/比較/outcomeのsketchあり、量/手順/score/control未固定; S15 Meaning/Testable Directions |
| CON-PRED-009 | gradient excessive / narrative fixation / trauma-like rereferencing | PM2 | observable/state名あり、操作/抽出/判定手順なし; S15 Meaning;S16 Excessive Gradient |
| CON-PRED-010 | gradient weak / diffuse attention / free association | PM2 | observable/state名あり、操作/抽出/判定手順なし; S16 Weak Meaning |
| CON-PRED-011 | measurement operation / live-to-residue claim | PM1 | live→residueは方向あるが独立live outcomeなし; S13 Plasticity Closure;S11 |
| CON-PRED-012 | report demand intensity / remaining log/report shifts | PM3 | 操作/比較/outcomeのsketchあり、量/手順/score/control未固定; S13 Experimental Implication;S15 Shift |
| CON-PRED-013 | measurement precision / residue definiteness | PM3 | 操作/比較/outcomeのsketchあり、量/手順/score/control未固定; S13 Precision;S15 Residue Shift |
| CON-PRED-014 | report-pathway disruption / verbal/behavioral asymmetry | PM2 | observable/state名あり、操作/抽出/判定手順なし; S10 Split-Brain / Reporting |
| CON-PRED-015 | inaccessible logs / rationalization / coherence | PM2 | observable/state名あり、操作/抽出/判定手順なし; S10 Rationalization interpretation |
| CON-PRED-016 | same local activity; temporal conditions varied / subjective/behavioral response difference | PM3 | 操作/比較/outcomeのsketchあり、量/手順/score/control未固定; S15 Non-Local Regime Prediction |
| CON-PRED-017 | sleep/dream/anesthesia/dissociation windows / cross-state gap/mu/tau changes | PM2 | observable/state名あり、操作/抽出/判定手順なし; S15 Testable Directions |
| CON-PRED-018 | phase axes gap/mu; tau/gradient controls / state classification | PM2 | observable/state名あり、操作/抽出/判定手順なし; S15 Phase Diagram/Testable Directions;FIG03 |

## 25. Phenomenological evidence maturity

Phase04 PH-CLM24 familyを一度ずつ追跡。PH-COR1は経験例、2はreport candidate、3はreport候補を条件で対比する記述が揃う場合のみ。形式windowへphenomenal labelが付いただけでは3にしない。PE3固定手順/criterionには至らない。

| PH-CLM history | CON-CLM | Located phenomenal correspondence | PH-COR | PE | Remaining gap |
| --- | --- | --- | --- | --- | --- |
| PH-CLM-001 | CON-CLM-002 | log-referenceable relationがconscious stateである; S00;S06 interface;S09 opening;S12 | PH-COR-2 | PE1 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-002 | CON-CLM-004 | stable consciousness iff tuple belongs to window; S15 Summary;CON-EQ-067/161 | PH-COR-3 | PE2 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-003 | CON-CLM-010 | finite gap is necessary for consciousness; S04 finite gap;S07 nonclosure;S14 | PH-COR-3 | PE2 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-004 | CON-CLM-013 | delay gives reference thickness / changes experienced time; S09 Delay;S15 Delay Window | PH-COR-3 | PE2 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-005 | CON-CLM-016 | SSO three conditions imply conscious state obtains; S06 SSO as Local Non-Closure | PH-COR-2 | PE1 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-006 | CON-CLM-019 | nonclosed loop maintains conscious state across time; S09 loop/persistence | PH-COR-2 | PE1 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-007 | CON-CLM-024 | TCA point is experienced ego position; S05 From Attention to Ego;S08 | PH-COR-0 | PE0 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-008 | CON-CLM-036 | transitional state is experienced as qualia; S11 EN:64 / JA:72 | PH-COR-1 | PE1 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-009 | CON-CLM-037 | gate passage is phenomenal surface / not product; S11 gate / EN:114–118 | PH-COR-2 | PE1 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-010 | CON-CLM-038 | qualia feels central because live boundary; explanation reframed; S11 EN:179/208–216;SERIOUS-001 | PH-COR-1 | PE1 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-011 | CON-CLM-039 | T_Phi determines diffuse/clear/fixed qualia relation; S11 Effective Torque | PH-COR-3 | PE2 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-012 | CON-CLM-041 | unchanged live qualia cannot be stored/measured; S11 storage;S13 Precision | PH-COR-3 | PE2 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-013 | CON-CLM-042 | measurement closes gate / transforms qualia into residue; S13 Plasticity Closure;S11 | PH-COR-3 | PE2 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-014 | CON-CLM-044 | introspection changes its state into logs/residue; S13 Introspection | PH-COR-3 | PE2 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-015 | CON-CLM-046 | sedimented terrain yields experienced self-continuity; S12 Self;S18 Higher-Order | PH-COR-2 | PE1 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-016 | CON-CLM-049 | explicit consciousness requires log sedimentation/reference; S10 summary/experimental correspondence | PH-COR-2 | PE1 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-017 | CON-CLM-054 | consciousness opens at preparation-to-log transformation point; S10 Libet final | PH-COR-2 | PE1 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-018 | CON-CLM-057 | split-brain does not double consciousness; S10 What Do Not Show;S15 Split-Brain | PH-COR-0 | PE0 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-019 | CON-CLM-062 | local substrates coupled temporally yield nonlocal conscious regime; S14 Local Substrates/Distributed | PH-COR-3 | PE2 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-020 | CON-CLM-065 | small gap → automation / weaker conscious access; S15 Synchronization;S16 same | PH-COR-3 | PE2 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-021 | CON-CLM-066 | excessive gap → dream/dissociation-like fragmentation; S15 Excessive Differential;S16 | PH-COR-3 | PE2 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-022 | CON-CLM-069 | tau manipulation alters report stability and time/self sense; S15 Delay/Testable Directions | PH-COR-3 | PE2 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-023 | CON-CLM-087 | qualia / CT insight same boundary phenomenon; S20 correspondence table;S11 | PH-COR-1 | PE1 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |
| PH-CLM-024 | CON-CLM-104 | JA C(t) opening function collapses with gap; JA S07/S13;CON-EQ-101/140 | PH-COR-0 | PE0 | report/経験例はparticipant dataではない。独立criterion・採点・protocolなし |

## 26. Empirical evidence maturity

NEURAL/OBSERVATIONAL/EMPIRICAL union 23 family。実験のnamed protocol再話はCon固有protocolの実装でない。EE2は対象名に加えてproxy/map案があるだけで、その妥当性は未判定。

| CON-CLM | Neural/behavioral/measurement target | EE | Limit |
| --- | --- | --- | --- |
| CON-CLM-008 | fast/slowに対応するneural/bodily layers; S14 Local Substrates | EE2 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-027 | I maps to retained cognitive history; S06/S09/S16 Limits | EE2 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-039 | T_Phi determines diffuse/clear/fixed qualia relation; S11 Effective Torque | EE2 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-041 | unchanged live qualia cannot be stored/measured; S11 storage;S13 Precision | EE2 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-042 | measurement closes gate / transforms qualia into residue; S13 Plasticity Closure;S11 | EE2 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-043 | precision increase causes more sedimentation and erasure; S13 Precision;S15 Residue Shift | EE2 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-044 | introspection changes its state into logs/residue; S13 Introspection | EE2 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-048 | report requires processing/retention/pathway; S09/S10 Reporting Bottleneck | EE2 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-050 | Libet protocol / readiness precedes reported intention; S10 Libet first paragraphs | EE1 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-051 | readiness potential is fast action-candidate preparation; S10 Libet | EE2 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-052 | Libet measured Delta v/mu transformation delay; S10 Libet EN:40–56 / JA:48–64 | EE2 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-055 | split-brain behavioral/verbal asymmetry description; S10 Split-Brain first paragraphs | EE1 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-056 | split-brain asymmetry is blocked log-reference route; S10 Split-Brain / Reporting | EE2 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-057 | split-brain does not double consciousness; S10 What Do Not Show;S15 Split-Brain | EE0 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-058 | rationalization/confabulation as experimental phenomenon; S10 Rationalization first paragraphs | EE1 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-059 | rationalization fills missing logs coherently; S10 Rationalization interpretation | EE2 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-060 | both experiment types establish explicit consciousness conditions; S10 both evidence shows / final | EE2 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-061 | conscious states depend on neural/bodily activity; S14 opening/local substrates | EE1 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-062 | local substrates coupled temporally yield nonlocal conscious regime; S14 Local Substrates/Distributed | EE2 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-064 | same local activity different temporal context gives different report; S15 Non-Local Regime Prediction | EE2 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-073 | report/measurement demand alters remaining residue; S13 Experimental Implication;S15 Shift | EE2 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-075 | phase diagram can classify altered conscious regimes; S15 Phase Diagram/Testable Directions;FIG03 | EE2 | Con-linked executable protocol/data/analysis/replicationは未所在 |
| CON-CLM-077 | dream/dissociation/etc share increased-gap referencing structure; S16 Excessive Difference | EE1 | Con-linked executable protocol/data/analysis/replicationは未所在 |

## 27. Cross-scale empirical testability

| XSC-TEST | Relation / claims | Common observable | Common units/invariant | Joint data / function | Current testability |
| --- | --- | --- | --- | --- | --- |
| XSC-TEST-001 | Delta v / Delta C;079/080 | なし | rate対effective closure、共通unit/invariant未固定 | なし | 形式対応、empirical testは未操作化;S06/FIG06 |
| XSC-TEST-002 | TCA / CT token;084 | なし | temporal/spatial類比、共通単位なし | なし | token運動をneural測定と同一視しない;S05 |
| XSC-TEST-003 | Phi same quantity;085/086 | 意味/地形の候補語 | metric/共同field reconstructionなし | なし | source比較のみ;S09 |
| XSC-TEST-004 | qualia / insight boundary;087 | 経験例の比較 | 共通phenomenal/semantic criterionなし | なし | 同一boundaryのtestなし;S20 |
| XSC-TEST-005 | four-layer grammar;088/089/090 | layerの対象名 | preserved invariant/typed translationなし | なし | 概念比較、共通生成原因testではない;S06/S18/S20 |
| XSC-TEST-006 | older PDE / SSO;081/082 | persistence名 | PDE→SSOの観測specializationなし | なし | 上流式がlocal神経実装を供給しない;S06 |

VED/IFGTの8 OPEN（discrete C→field、J→vector、rho→field、distance→metric、dot-rho→sigma、L→tensor、tau対応、VED/IFGT sigma対応）を閉じない。Bioのpixel-reproducible toyをConsciousness prediction maturityに加算しない。CT sourceの計算形式はConのneural/report pipelineに接続されていない。

## 28. Source-implied empirical program

SOURCE-IMPLIED EMPIRICAL PROGRAM。下表はS13/S15/S16/S18が述べた方向を依存順に並べた未実施taskであり、新研究提案/新測定定義ではない。まずobservableの同定、その後比較手順、最後data接続が必要という順序のみを整理する。具体的センサ、神経帯域、尺度、式、刺激集合は追加しない。CE-E1→CE-E3/4は今達成したとの意味ではない。

| EMP-TASK | Source-implied task | Source | Dependency / not supplied |
| --- | --- | --- | --- |
| EMP-TASK-001 | fast/slow差を神経時間関係へ対応づける | S15 Testable1;S18 Remaining1 | rate/同じunitの抽出を固定する必要、方法は未供給 |
| EMP-TASK-002 | tauとreport/準備の時刻を区別して対応づける | S10;S13 Experimental1;S15 Testable2 | event boundaries/calibration未供給 |
| EMP-TASK-003 | muとT_Phi入力の可測性を定める | S16 Limits2;S18 Remaining1 | gap/gradient/couplingの独立mapが先 |
| EMP-TASK-004 | I/J_I/J_log/Phiをbrain/behavior/logへ対応づける | S16 Limits3;S18 Remaining2 | count/flow/metric未供給 |
| EMP-TASK-005 | report要求/言語化/精度差とresidue比較を具体化する | S13 Experimental2/6;S15 Shift | 要求量/残余score/対照未供給 |
| EMP-TASK-006 | semantic loadと参照biasの比較を具体化する | S13 Experimental3;S15 Testable3 | 負荷とgradientを同じものと仮定しない |
| EMP-TASK-007 | report前後neural patternと同じ活動下の条件差を比較可能にする | S13 Experimental5;S15 Testable8 | matching/時間窓/score未供給 |
| EMP-TASK-008 | 状態間window推定/分類へ進む | S15 Testable5/9;S18 Remaining3 | 前記mapsと独立状態criteriaが先、data収集なし |

## 29. Source-implied phenomenological program

SOURCE-IMPLIED PHENOMENOLOGICAL PROGRAM。sourceが名づけたqualia/report/self/timeの区別を比較可能にする未完task。独立criterionの必要性はsourceの区別と本監査のgapからの依存要件であり、採用すべき哲学的criterionを発明していない。

| PH-TASK | Source-implied need | Source | Not supplied |
| --- | --- | --- | --- |
| PH-TASK-001 | qualiaそのものとreport proxyの判定を分ける | S11/S13;SERIOUS-001 | independent target criterion未固定 |
| PH-TASK-002 | 報告/評価/言語化の手順とscoreを固定する | S13 Plasticity/Experimental | protocol/anchors未供給 |
| PH-TASK-003 | diffuse/clear/vivid/fixedを比較可能なreportにする | S11 Effective Torque | 尺度・反復条件なし |
| PH-TASK-004 | live/residueの前後差をproxyとtargetを分けて扱う | S13/S15 Shift;CON-CIR-019 | live同一性・residue metricなし |
| PH-TASK-005 | self/time continuityの報告を条件差へ対応づける | S15 Delay;S16 High Viscosity | self/time尺度・tau校正なし |

## 30. Empirical ceiling recheck

Phase04 CE-E0=31、CE-E1=74、CE-E2–6=0を維持。新しい既存data artifactの発見0。named experimentの再解釈とsourceのprotocol sketchを再分類しただけでCE-E3 operational mapへ上げない。CON-EVID-019のIntelligence bibliographyは内部theory引用でありexternal empirical anchorではない。外部文献参照・data・mapの不在をfalsehoodと読まない。

| CON-CLM | Phase04 ceiling | Phase05 ceiling | Correspondence coverage / reason |
| --- | --- | --- | --- |
| CON-CLM-001 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-002 | CE-E1 | CE-E1 | CON-EC-001 |
| CON-CLM-003 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-004 | CE-E1 | CE-E1 | CON-EC-002 |
| CON-CLM-005 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-006 | CE-E1 | CE-E1 | CON-EC-003 |
| CON-CLM-007 | CE-E1 | CE-E1 | CON-EC-004 |
| CON-CLM-008 | CE-E1 | CE-E1 | CON-EC-005 |
| CON-CLM-009 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-010 | CE-E1 | CE-E1 | CON-EC-006 |
| CON-CLM-011 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-012 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-013 | CE-E1 | CE-E1 | CON-EC-007 |
| CON-CLM-014 | CE-E1 | CE-E1 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-015 | CE-E1 | CE-E1 | CON-EC-008 |
| CON-CLM-016 | CE-E1 | CE-E1 | CON-EC-009 |
| CON-CLM-017 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-018 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-019 | CE-E1 | CE-E1 | CON-EC-010 |
| CON-CLM-020 | CE-E1 | CE-E1 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-021 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-022 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-023 | CE-E1 | CE-E1 | CON-EC-011 |
| CON-CLM-024 | CE-E1 | CE-E1 | CON-EC-012 |
| CON-CLM-025 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-026 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-027 | CE-E0 | CE-E0 | CON-EC-013 |
| CON-CLM-028 | CE-E0 | CE-E0 | CON-EC-014 |
| CON-CLM-029 | CE-E1 | CE-E1 | CON-EC-015 |
| CON-CLM-030 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-031 | CE-E1 | CE-E1 | CON-EC-016 |
| CON-CLM-032 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-033 | CE-E1 | CE-E1 | CON-EC-017 |
| CON-CLM-034 | CE-E1 | CE-E1 | CON-EC-018 |
| CON-CLM-035 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-036 | CE-E1 | CE-E1 | CON-EC-019 |
| CON-CLM-037 | CE-E1 | CE-E1 | CON-EC-020 |
| CON-CLM-038 | CE-E1 | CE-E1 | CON-EC-021 |
| CON-CLM-039 | CE-E1 | CE-E1 | CON-EC-022 |
| CON-CLM-040 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-041 | CE-E1 | CE-E1 | CON-EC-023 |
| CON-CLM-042 | CE-E1 | CE-E1 | CON-EC-024 |
| CON-CLM-043 | CE-E1 | CE-E1 | CON-EC-025 |
| CON-CLM-044 | CE-E1 | CE-E1 | CON-EC-026 |
| CON-CLM-045 | CE-E1 | CE-E1 | CON-EC-027 |
| CON-CLM-046 | CE-E1 | CE-E1 | CON-EC-028 |
| CON-CLM-047 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-048 | CE-E1 | CE-E1 | CON-EC-029 |
| CON-CLM-049 | CE-E1 | CE-E1 | CON-EC-030 |
| CON-CLM-050 | CE-E1 | CE-E1 | CON-EC-031 |
| CON-CLM-051 | CE-E1 | CE-E1 | CON-EC-032 |
| CON-CLM-052 | CE-E1 | CE-E1 | CON-EC-033 |
| CON-CLM-053 | CE-E1 | CE-E1 | CON-EC-034 |
| CON-CLM-054 | CE-E1 | CE-E1 | CON-EC-035 |
| CON-CLM-055 | CE-E1 | CE-E1 | CON-EC-036 |
| CON-CLM-056 | CE-E1 | CE-E1 | CON-EC-037 |
| CON-CLM-057 | CE-E1 | CE-E1 | CON-EC-038 |
| CON-CLM-058 | CE-E1 | CE-E1 | CON-EC-039 |
| CON-CLM-059 | CE-E1 | CE-E1 | CON-EC-040 |
| CON-CLM-060 | CE-E1 | CE-E1 | CON-EC-041 |
| CON-CLM-061 | CE-E1 | CE-E1 | CON-EC-042 |
| CON-CLM-062 | CE-E1 | CE-E1 | CON-EC-043 |
| CON-CLM-063 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-064 | CE-E1 | CE-E1 | CON-EC-044 |
| CON-CLM-065 | CE-E1 | CE-E1 | CON-EC-045 |
| CON-CLM-066 | CE-E1 | CE-E1 | CON-EC-046 |
| CON-CLM-067 | CE-E1 | CE-E1 | CON-EC-047 |
| CON-CLM-068 | CE-E1 | CE-E1 | CON-EC-048 |
| CON-CLM-069 | CE-E1 | CE-E1 | CON-EC-049 |
| CON-CLM-070 | CE-E1 | CE-E1 | CON-EC-050 |
| CON-CLM-071 | CE-E1 | CE-E1 | CON-EC-051 |
| CON-CLM-072 | CE-E1 | CE-E1 | CON-EC-052 |
| CON-CLM-073 | CE-E1 | CE-E1 | CON-EC-053 |
| CON-CLM-074 | CE-E1 | CE-E1 | CON-EC-054 |
| CON-CLM-075 | CE-E1 | CE-E1 | CON-EC-055 |
| CON-CLM-076 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-077 | CE-E1 | CE-E1 | CON-EC-056 |
| CON-CLM-078 | CE-E0 | CE-E0 | §27 cross-scale/source comparison (not mandatory empirical-type union) |
| CON-CLM-079 | CE-E1 | CE-E1 | §27 cross-scale/source comparison (not mandatory empirical-type union) |
| CON-CLM-080 | CE-E1 | CE-E1 | §27 cross-scale/source comparison (not mandatory empirical-type union) |
| CON-CLM-081 | CE-E1 | CE-E1 | §27 cross-scale/source comparison (not mandatory empirical-type union) |
| CON-CLM-082 | CE-E1 | CE-E1 | CON-EC-057 |
| CON-CLM-083 | CE-E1 | CE-E1 | §27 cross-scale/source comparison (not mandatory empirical-type union) |
| CON-CLM-084 | CE-E1 | CE-E1 | §27 cross-scale/source comparison (not mandatory empirical-type union) |
| CON-CLM-085 | CE-E1 | CE-E1 | §27 cross-scale/source comparison (not mandatory empirical-type union) |
| CON-CLM-086 | CE-E1 | CE-E1 | §27 cross-scale/source comparison (not mandatory empirical-type union) |
| CON-CLM-087 | CE-E1 | CE-E1 | CON-EC-058 |
| CON-CLM-088 | CE-E1 | CE-E1 | §27 cross-scale/source comparison (not mandatory empirical-type union) |
| CON-CLM-089 | CE-E1 | CE-E1 | §27 cross-scale/source comparison (not mandatory empirical-type union) |
| CON-CLM-090 | CE-E1 | CE-E1 | CON-EC-059 |
| CON-CLM-091 | CE-E1 | CE-E1 | §27 cross-scale/source comparison (not mandatory empirical-type union) |
| CON-CLM-092 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-093 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-094 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-095 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-096 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-097 | CE-E0 | CE-E0 | CON-EC-060 |
| CON-CLM-098 | CE-E1 | CE-E1 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-099 | CE-E1 | CE-E1 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-100 | CE-E1 | CE-E1 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-101 | CE-E1 | CE-E1 | CON-EC-061 |
| CON-CLM-102 | CE-E0 | CE-E0 | formal/definition/negative/methodological scope; §5/12/30; new empirical target not asserted |
| CON-CLM-103 | CE-E0 | CE-E0 | CON-EC-062 |
| CON-CLM-104 | CE-E0 | CE-E0 | CON-EC-063 |
| CON-CLM-105 | CE-E1 | CE-E1 | CON-EC-064 |

## 31. Phenomenal ceiling

| CON-CLM | Maximum PCE | Located basis |
| --- | --- | --- |
| CON-CLM-002 | PCE1 | §25 PH-COR/PE entry; S00;S06 interface;S09 opening;S12 |
| CON-CLM-004 | PCE2 | §25 PH-COR/PE entry; S15 Summary;CON-EQ-067/161 |
| CON-CLM-010 | PCE2 | §25 PH-COR/PE entry; S04 finite gap;S07 nonclosure;S14 |
| CON-CLM-013 | PCE2 | §25 PH-COR/PE entry; S09 Delay;S15 Delay Window |
| CON-CLM-016 | PCE1 | §25 PH-COR/PE entry; S06 SSO as Local Non-Closure |
| CON-CLM-019 | PCE1 | §25 PH-COR/PE entry; S09 loop/persistence |
| CON-CLM-024 | PCE0 | §25 PH-COR/PE entry; S05 From Attention to Ego;S08 |
| CON-CLM-036 | PCE1 | §25 PH-COR/PE entry; S11 EN:64 / JA:72 |
| CON-CLM-037 | PCE1 | §25 PH-COR/PE entry; S11 gate / EN:114–118 |
| CON-CLM-038 | PCE1 | §25 PH-COR/PE entry; S11 EN:179/208–216;SERIOUS-001 |
| CON-CLM-039 | PCE2 | §25 PH-COR/PE entry; S11 Effective Torque |
| CON-CLM-041 | PCE2 | §25 PH-COR/PE entry; S11 storage;S13 Precision |
| CON-CLM-042 | PCE2 | §25 PH-COR/PE entry; S13 Plasticity Closure;S11 |
| CON-CLM-044 | PCE2 | §25 PH-COR/PE entry; S13 Introspection |
| CON-CLM-046 | PCE1 | §25 PH-COR/PE entry; S12 Self;S18 Higher-Order |
| CON-CLM-049 | PCE1 | §25 PH-COR/PE entry; S10 summary/experimental correspondence |
| CON-CLM-054 | PCE1 | §25 PH-COR/PE entry; S10 Libet final |
| CON-CLM-057 | PCE0 | §25 PH-COR/PE entry; S10 What Do Not Show;S15 Split-Brain |
| CON-CLM-062 | PCE2 | §25 PH-COR/PE entry; S14 Local Substrates/Distributed |
| CON-CLM-065 | PCE2 | §25 PH-COR/PE entry; S15 Synchronization;S16 same |
| CON-CLM-066 | PCE2 | §25 PH-COR/PE entry; S15 Excessive Differential;S16 |
| CON-CLM-069 | PCE2 | §25 PH-COR/PE entry; S15 Delay/Testable Directions |
| CON-CLM-087 | PCE1 | §25 PH-COR/PE entry; S20 correspondence table;S11 |
| CON-CLM-104 | PCE0 | §25 PH-COR/PE entry; JA S07/S13;CON-EQ-101/140 |

PCE2のstructured report contrastは事前に固定されたreport protocolでない。PCE3/4/5は0。label-only familyがあることと、全sourceに対比や実験方向がないことは別。経験例・比較の面白さを残し、mechanistic validationへ昇格しない。

## 32. Discrepancy ledger

| CON-DS | Trace | Discrepancy | Current gap / no action |
| --- | --- | --- | --- |
| CON-DS-001 | CON-CLM-004;WIN-TEST005 | stable iff window vs membership not computable from observations | bound/tuple/independent criterion OPEN |
| CON-DS-002 | CON-CLM-008/010;FS-OBS | neural timescale named vs fast/slow extractor未選択 | oscillation/latencyを勝手に選ばない |
| CON-DS-003 | CON-CLM-052;LIB-COR003 | “measured” delay vs tau event boundaries/ratio calibrationなし | experiment reinterpretation only |
| CON-DS-004 | CON-CLM-039;TPHI-OBS006 | qualia prediction uses T_Phi vs S16 explicitly not measurable | index/input/clarity OPEN |
| CON-DS-005 | CON-CLM-027/028/029;IPHI-OBS | density/flow/potential vs no counting/metric/field map | formal content保持 |
| CON-DS-006 | CON-CLM-049/060;REPORT-REL009 | report distinguished from state yet used as condition evidence | criterion drift risk |
| CON-DS-007 | CON-CLM-041/042;CON-CIR-019 | live unmeasurable wording vs residue proxy comparison | independent live target OPEN |
| CON-DS-008 | CON-CLM-043/073;RES-OBS | precision/demand/residue directions vs dose/metric not fixed | proxy experiment未実行 |
| CON-DS-009 | CON-CLM-056/059;SPLIT-COR | path asymmetry compatible vs distinctive log-mediated prediction未固定 | general pathway comparisonと区別 |
| CON-DS-010 | CON-CLM-062/064;NEURAL-COR | temporal relation claim vs site/coupling/sameness metricなし | NCC非同一性だけでは検証にならない |
| CON-DS-011 | CON-CLM-074/075/077;ALT-COR | state names/phase labels vs cross-state classifierなし | clinical/diagnostic読みしない |
| CON-DS-012 | CON-CLM-024/046;SELF-COR | experienced ego/self continuity vs no independent proxy criterion | namingと同定を分離 |
| CON-DS-013 | CON-CLM-080/086/087/089;XSC-TEST | same condition/quantity/grammar vs no common observable/invariant | translation OPEN |
| CON-DS-014 | CON-PRED-001–018;§23–24 | testable directions vs executable tests/data0 | PMと実行を分離 |
| CON-DS-015 | CON-CLM-104/105;CON-U-096 | JA C(t)/図accessと意識ラベル差 | version差は測定定義ではない |
| CON-DS-016 | CON-CLM-036/038;SERIOUS-001 | phenomenal label/explanation vs independent endpoint | 定義readingと説明readingを選別解消しない |

## 33. Phase-05 uncertainty ledger

| CON-U | Uncertainty | Trace | Status |
| --- | --- | --- | --- |
| CON-U-099 | independent consciousness criterion | 004/049;WIN-TEST;CON-U-079 | OPEN — stateラベルをwindow/reportから独立に定義できるか |
| CON-U-100 | proxy validity | 002/036/037;REPORT-REL | OPEN — report/神経/機能proxyとtargetの対応 |
| CON-U-101 | report criterion drift | 048/049/060;CON-U-095 | OPEN — explicit/access/stateの判定境界 |
| CON-U-102 | tau event boundaries | 052/069;TAU-EVID;CON-U-080 | OPEN — start/end・物理unit・経験時間の分離 |
| CON-U-103 | v_f/v_s extraction | 008/010;FS-OBS | OPEN — rate型と独立抽出 |
| CON-U-104 | mu operationalization | 011/067/068;MU-OBS | OPEN — coupling metric/単位/介入との対応 |
| CON-U-105 | T_Phi operationalization | 022/039;TPHI-OBS;CON-U-085 | OPEN — kappa/入力/clarityとのmap |
| CON-U-106 | I/Phi measurement | 027/028/029;IPHI-OBS | OPEN — count/field/metric/kernel |
| CON-U-107 | residue metric | 042/043/073;RES-OBS;CON-U-084 | OPEN — 残余の量とreport要求の独立尺度 |
| CON-U-108 | qualia report mapping | 036/037/038/039;CON-U-081 | OPEN — 独立phenomenal criterion/score |
| CON-U-109 | Libet distinctive prediction | 050–054;LIB-COR;CON-U-082 | OPEN — generic intervalとの差 |
| CON-U-110 | split-brain distinctive prediction | 055–060;SPLIT-COR;CON-U-083 | OPEN — generic経路遮断との差 |
| CON-U-111 | altered-state classifier | 074/075/077;ALT-COR | OPEN — stateを同一視せずwindow比較する基準 |
| CON-U-112 | cross-scale empirical bridge | 080/084/086/087/089;CON-U-088/094 | OPEN — common observable/unit/invariant |
| CON-U-113 | measurement-loop disconfirmation | CON-CIR-019;MEAS-LOOP | OPEN — 残余比較が何を否定し、何を否定しないか |
| CON-U-114 | same local activity control | 064;CON-U-097 | OPEN — matching toleranceと時間条件差 |
| CON-U-115 | phenomenological contrast protocol | PH-CONTRAST;CON-U-098 | OPEN — clarity/self/timeの再現可能なreport対比 |
| CON-U-116 | source-version observable status | 103/104/105;CON-U-096 | OPEN — JA weighted/C(t)/図の測定同定は未解決 |

CON-U-001–098の履歴を上書きせず、新しいoperational/testabilityの問いとして099以降へ延長する。同題の古い問いとのtraceを示しただけで解決・否定はしない。

## 34. Validation

検査対象は記録のID/coverage/集計、relative links、current EN/JA source pathとinclude、図参照、TeX構造、表示式内容、作業開始時の全既存file hash差分。PDF内容の新監査やbuildは行わず、figure PDF参照の存在を確認する。Markdown内の式説明は既存sourceへの引用/索引で、新たなdisplay equationを作らない。

| Check | Result / boundary |
| --- | --- |
| Phase04 CLM coverage | 105/105 (§3 selected64 + §30 remaining41); mandatory types and B3–B6 union 64/64 |
| Predictions | 18/18 distinctive + PM; Phase04 stable IDs retained |
| Phenomenal claims | 24/24 PH-COR + PE + PCE; no participant data substitution |
| High burden / measurement loop | 28/28 HB; CON-CIR-019 and SERIOUS-001 traced |
| Source versions | 21 EN/JA pairs; JA C(t)/attention/figure differences retained; no merge |
| Bibliography/data/code | refs.bib Intelligence 1; cite EN6/JA6; dedicated Con protocol/data/code not located |
| Figures | 6 families / 12 included PDFs; conceptual figures, not empirical results |
| Immutability | 44 TeX / 178 displayed blocks identical to Phase01 raw inventory and turn-start files; no source/artifact changes |
| Scope | Only new Phase05 record and README status/link; no build/simulation/web/commit/push |
| Validation execution | ID sequence/uniqueness, source links, table columns/fences, count sums, git diff --check checked; detailed counts below |

実検査結果：relative links 64件が存在。entryの42 inputs、図12 references、44 TeXのenvironment nestingを確認。current sourceの観測・測定・報告・予測・未確立wording scanはEN/JA計539 source-line hits（claim family数ではない）。主な対応差の扱いは次表。単なるgrep一致をempirical supportと数えない。

| EN/JA pair | Correspondence parity check | Preserved distinction |
| --- | --- | --- |
| S03 Notation | tは外的時間、tauはdelay/bufferでsubjective timeそのものではない | unit/event抽出を補わない |
| S05/S06 TCA / IFGT | effective indexとmeaning/log解釈、双方とも計測protocolなし | JA weighted attentionの追加近似を独立mapにしない |
| S10 Libet-Type / Split-Brain | 両言語とも実験の再解釈・準備/報告時刻・行動/言語非対称 | “measured”とCON-specific calibrationを区別 |
| S11 Qualia / Effective Torque | experienced-asとdiffuse/clear/fixed対比が双方にある | qualiaとconsciousness、clarityと安定性を同一化しない |
| S13 Measurement / Experimental Implication | residueの比較・統計を許し、要求/言語化/前後神経活動の方向を列挙 | JA C(t)追加collapse relationは保持、観測mapとして加算しない |
| S14/S15 Non-Local / Testable Directions | 同じ局所活動でも条件差でreport差、九つの調査方向 | 独立matching/control/thresholdは双方未固定 |
| S16 Limits / S18 Remaining Questions | EN “not a concrete measurable quantity”、JA「測定可能な定義は、まだ十分に確立されていない」 | I/J/Phi/log map・window推定は両言語とも未完 |
| S20 / FIG03 / FIG06 | correspondence/isomorphismの記述、図はconceptual region | EN access / JA意識のlabel差はCON-DS-015、同値/測定定義に統合しない |

表示式178 blocksのordered raw-content SHA-256（各blockを改行で連結）：`c3ef85df91bb704c3b482e2fc12574b4cf7c305a2bb6af04bbf81504b8ee6ebe`。Phase01全178 CON-EQの原文と完全一致。追加/削除/変更はいずれも0。

作業開始時の既存1449 filesをbyte hashで照合：READMEだけ変更、他1448 filesは一致。追加は本記録1件、削除0。simulation source/requirements、parametersを含むsource、PNG/PDF/GIF、上流・下流、Phase00–04 historyもこの不変集合に含まれる。`git status --short`は開始時と同じ177行（既存tracked modifications 173、untracked directories 4）。監査枝自体がuntrackedのため、status行数の不変だけに頼らずfile差分を検査した。

| Counting unit | Count |
| --- | --- |
| ec | 64 |
| observables | 20 |
| maps | 16 |
| fast | 5 |
| tau | 6 |
| mu | 3 |
| torque | 6 |
| iphi | 6 |
| window | 6 |
| report | 9 |
| qualia | 8 |
| residue | 7 |
| libet | 5 |
| split | 5 |
| neural | 7 |
| altered | 8 |
| self | 5 |
| contrasts | 9 |
| falsifiability | 28 |
| measurement | 4 |
| distinctive | 18 |
| cross | 6 |
| program_emp | 8 |
| program_ph | 5 |
| discrepancies | 16 |
| uncertainties | 18 |
| PM0 | 0 |
| PM1 | 1 |
| PM2 | 12 |
| PM3 | 5 |
| PM4 | 0 |
| PM5 | 0 |
| PM6 | 0 |
| PM7 | 0 |
| PE0 | 3 |
| PE1 | 10 |
| PE2 | 11 |
| PE3 | 0 |
| PE4 | 0 |
| PE5 | 0 |
| EE0 | 1 |
| EE1 | 5 |
| EE2 | 17 |
| EE3 | 0 |
| EE4 | 0 |
| EE5 | 0 |
| EE6 | 0 |
| EE7 | 0 |
| PCE0 | 3 |
| PCE1 | 10 |
| PCE2 | 11 |
| PCE3 | 0 |
| PCE4 | 0 |
| PCE5 | 0 |
| CE-E0 | 31 |
| CE-E1 | 74 |
| CE-E2 | 0 |
| CE-E3 | 0 |
| CE-E4 | 0 |
| CE-E5 | 0 |
| CE-E6 | 0 |
| COR-0 | 2 |
| COR-1 | 15 |
| COR-2 | 16 |
| COR-3 | 31 |
| COR-4 | 0 |
| COR-5 | 0 |
| COR-6 | 0 |

母数：EC64、PM18、PE/PCE24、EE23、CE105。COR/PMがschemaに達しても、計測入力/criterionが固定されたmapではないのでCE-E3は0のまま。source-implied tasksは将来必要な作業の整理で、現在のevidence件数に含めない。

## 35. Stop boundary

Phase05はCOMPLETE。現在の対応は対象名・proxy候補・比較方向/sketchまでで、Consciousness-linked executable protocol、独立運用map、participant data、tested/replicated predictionは所在しない。これはfalsehoodでも最終phenomenal explanation失敗でもない。測定loopにはdisconfirmation上のriskがあるが、residueの比較経路をsourceが開いているため、全面的な反証不能性は確定しない。

source、式、図、PDF、upstream/downstream、過去の監査は変更しない。proxy validity、phenomenal criterion、window calibration、typed translation、上流8橋はOPEN。claim disposition、新theory、新bridgeは付与しない。Phase06 revision candidate synthesisには進まず停止する。

# 実験系列 source map v0.1

- **地位:** 補助ファイル。traceability 集約のみ。分析・結論・散文は [`source architecture v0.1`](./theorem_proof_anatomy_experiment_source_architecture_v0.1_ja.md) 側にある。
- **目的:** 最終記録本文をファイル名の羅列にしないため、file-level の対応関係をここへ寄せる。
- **日付:** 2026-09-06
- **Archive note (2026-09-07):** archive reorganization に伴い relative links と下記の総数を更新した。分析・判定は変更していない。

archive に収録した系列資料は **83ファイル**（`.md` 74 + `.py` 8 + `.svg` 1）。この数には archive の案内用 `README.md` を含めない。旧記載の「70ファイル」と「`.md` 68 + `.py` 8」は集計が一致していなかったため、archive reorganization 時の実ファイル再集計で訂正した。系列外として除外したもの: `barrier_ja.md`（05-10）、`notes/README.md`（05-11）。両者は本系列の3か月前で、内容上も無関係である。

---

## 1. Phase table

| Phase | Question | Primary files | Key evidence | Outcome |
|---|---|---|---|---|
| **0** 起源と経験的枝<br>08-16 → 08-22 | 予測・観測の成功だけから生成構造を一意に同定できるか | `tool_truth_absence_working_note.md` / `_v0.2` / `_v0.3` / `_v0.4` + 3 diffs、`scientific_identifiability_case_01_quantum.md`、`quantum_identifiability_prior_art_network.md`、`deferred_resolution_case_01_gst.md` / `_v0.2` / diff / 2 reviews、`scientific_assurance_case_02_metrology.md` / `_preregistration` / `_control_reconstruction` / `_comparison`、`web_of_constraints_methodology_adversarial_review.md` / `_second_order_review_claudecode.md`、`validation_basis_transition_working_note_v0.1.md`、`case_01_hydro_target_artifact_discovery_v0.1.md`、`hydrology_negative_knowledge_preservation_note_v0.1/_v0.2.md`、`qualification_practices_comparative_study_design_v0.1.md`、`p0_generic_standards_baseline_v0.1.md`、`p1r_noneval_two_field_check_v0.1.md`、`tool_truth_absence_research_trajectory_summary.md` (+ `.svg`) | \(O=\mathrm{id}\)、有限 encoder、二ビット破壊測定、GST Erasure Test、計量学 M1、P0 の 14→1 | 普遍不可能定理を放棄。comparative methodology 終了、comparative review へ降格。8 つの方法規律を明文化 |
| **1** theorem anatomy<br>09-04 20:32 以前（内部順序不明） | 定理の各条件は何をしており、除去すると何が起きるか | `../01_theorem_anatomy/theorem_proof_anatomy_v1.1_ja.md` + 同ディレクトリの 10 stress tests | 21 定理 survey、R2 の偏在、C1 / S2* / A2 判定 | H2 暫定支持、H3 不支持。自前語彙を説明用へ降格 |
| **2** proof-formation<br>09-04 21:18 → 09-05 05:33 | 壊れた claim の訂正史を独立 reader が再構成できるか | `proof_formation_meta_experiment_v0.1.md`、`_frozen_toy_corpus_v0.1.md`、`_coder_instructions_v0.1.md` / `_v0.1.1.md`、`_adjudication_rules_v0.1.md`、`_reader_01_v0.1.md`、`_reader_01_calibration_note.md`、`_reader_02_claudecode_v0.1.1.md`、`_reader_02_adjudication_note_v0.1.md`、`_reader_03_v0.1.1.md`、`_reader_02_03_blind_comparison_v0.1.md`、`_inter_reader_adjudication_v0.1.md` | parent-level core の reader 横断一致、code 不一致、packet 到達不能な 3 コード | **P0-PASS**。claim identity / episode boundary が最脆弱点として事前予測どおり確認 |
| **3** 有限命題 prototype<br>09-05 05:51 → 06:57 | move の区別は semantic か record 由来か | `proof_formation_finite_propositional_prototype_v0.1.md` (+ checker)、`_stress_test_v0.1.md` (+ stress checker)、`_postmortem_architecture_v0.1.md` | exact-filter \(B=\varphi_{\Omega\setminus E}\)、M1↔scope 相互模倣、到達可能 \(E\) 族の一致、`withdrawn` の非還元性 | semantic identification を **DOWNGRADE**。区別は typed record が担う |
| **4** record frame<br>09-06 06:31 → 10:08 | 記録枠を変えると何が保たれ・潰れ・生じるか | `proof_formation_record_frame_sensitivity_test_v0.1.md`、`_cross_frame_persistence_test_v0.1.md`、`_visibility_transition_test_v0.1.md`、`_non_nested_frame_replication_test_v0.1.md`、`_minimal_separating_field_set_test_v0.1.md` (+ 各 checker 5 本) | H9/H10 の R4 初出、N-family の非単調 visibility、D5 の偶然 cue 分離 | **系列唯一の KILL 発火**（minimal separator の characterization claim）。枝を離脱 |
| **5** reachability stress<br>09-06 13:32 → 15:21 | 証明の中で実際に効いているものは何か | `theorem_proof_anatomy_reachability_test_1_plus_1_eq_2_v0.1_ja.md`、`_addition_commutativity_`、`_ivt_`、`_fta_`、`_cross_test_audit_v0.1.md`、`_synthesis_closure_v0.1_ja.md` | 可換律 countermodel、ℚ 上の \(q^2-2\)、FTA の Level 2 heterogeneity | 語彙 4 語を無損失還元。v2 を **retire**（延期ではない）。necessity 未確立 |
| **6** theoremhood 周辺 pilot<br>09-06 15:55 → 17:49 | 判断は何を settle するか → 証明の同一性 → 保存 → 体系間対応 | `theorem_closure_open_remainder_pilot_v0.1_ja.md`、`theorem_judgment_enrichment_boundary_pilot_v0.1_ja.md`、`theorem_proof_quotient_invariance_pilot_v0.1_ja.md` (+ `.py`)、`theorem_specification_change_preservation_pilot_v0.1_ja.md`、`theorem_cross_calculus_proof_class_preservation_pilot_v0.1_ja.md` | \(\lambda p.\pi_1p\neq\lambda p.\pi_2p\)、T1–T4 の 4 非同値概念、ND→raw LJ の well-definedness 失敗、\(L_{\text{once}}/L_{\text{twice}}\) | intrinsic proof identity / canonical proof / universal preservation を KILL。global bijection は **NOT ESTABLISHED** |
| **7** independent audit<br>09-06 18:01 | 何が残り、何が標準語へ還元されるか | `theorem_proof_anatomy_full_series_independent_audit_v0.1.md` | 全 novelty 評価が C 以下 | **Option 2**。STOP WITH SYNTHESIS |

---

## 2. Frozen corpus 対応表（Phase 2 の入力）

`proof_formation_frozen_toy_corpus_v0.1.md` の 12 episode が、Phase 0 と Phase 1 のどこから来たか。**Phase 2 は Phase 0 と Phase 1 の両方を対象化している**ことがこの表から直接読める。

| Episode | 題 | 出典ファイル | 該当箇所 | 由来 phase |
|---|---|---|---|---|
| E01 | Observation-map noninjectivity | `tool_truth_absence_working_note_v0.2.md` | Phase 1 | 0 |
| E02 | Self-containment impossibility and conditional capacity | 同上 | Phase 2 | 0 |
| E03 | Generation–log non-isomorphism | 同上 | Phase 3 | 0 |
| E04 | Pairwise separation versus global adaptive separator | 同上 | Phase 5 | 0 |
| E05 | v0.1→v0.2 internal/external interface correction | `tool_truth_absence_v0.1_to_v0.2_diff.md` / `_working_note_v0.2.md` | Major revision map / Phase 7 | 0 |
| E06 | GST Deferred Resolution v0.1→v0.2 | `deferred_resolution_case_01_gst.md` / `_v0.1_to_v0.2_diff.md` / `_v0.2.md` | §1.1, §22 / §2 / opening, §1.1 | 0 |
| E07 | Metrology H1→M1 | `scientific_assurance_case_02_metrology_preregistration.md` / `_comparison.md` | §4 / §§3, 14 | 0 |
| E08 | Hydrology preservation→documentary continuity | `hydrology_negative_knowledge_preservation_note_v0.1.md` / `_v0.2.md` | Current verdict / Changes + Current verdict | 0 |
| E09 | P0→P1-reduced termination | `p0_generic_standards_baseline_v0.1.md` / `p1r_noneval_two_field_check_v0.1.md` | §§5–6 / §§6, 9 | 0 |
| E10 | Gödel closure reversal→C1 | `../01_theorem_anatomy/godel_incompleteness_closure_reversal_stress_test_ja.md` | §§0, 1, 7–8 | 1 |
| E11 | Reflection S2→S2* | `../01_theorem_anatomy/reflection_principles_scope_stress_test_ja.md` | §§0, 2–3, 11, 21 | 1 |
| E12 | Ordinal scalar→fixed-package calibration | `../01_theorem_anatomy/proof_theoretic_ordinal_stress_test_ja.md` | opening, §§16–18, 25 | 1 |

**注記** `[SD]`: E06 の Erasure Test、E07 の §5/§6 preregistered criteria、E09 の reframing 文、E08 の C-1/C-2 は、いずれも出典ファイルには存在するが frozen excerpt には含まれない。answer key がこれらに依拠する箇所は blind reader には到達不能であった（`proof_formation_inter_reader_adjudication_v0.1.md` §0.1 が限定的 source return で確認済み）。

---

## 3. 実行可能 checker 一覧

| # | ファイル | Phase | 検証した内容 | 検証していない内容 |
|---|---|---|---|---|
| 1 | `proof_formation_finite_propositional_checker_v0.1.py` | 3 | Example A–E の valuation 計算、M1/M2/scope、T1/T2/T3 フラグ | status、identity、M17（欄自体が存在しない） |
| 2 | `proof_formation_finite_propositional_stress_checker_v0.1.py` | 3 | 34 findings。core identities（n=2 全数 / n=3 標本）、T1 回避、exact-filter、相互模倣、到達可能 \(E\) 族、record 整合性 12 件 | post-hocness、identity legitimacy、segmentation（原理的に不可能） |
| 3 | `proof_formation_record_frame_sensitivity_checker_v0.1.py` | 4 | R0–R4 射影下の H1–H10 + control の区別 | どの枠が正しいか |
| 4 | `proof_formation_cross_frame_persistence_checker_v0.1.py` | 4 | K1/K2 の全 projector からの抽出 | frame-independence（projector 設計の帰結） |
| 5 | `proof_formation_visibility_transition_checker_v0.1.py` | 4 | 全 pair 行列と逆向き消去 | action ontology |
| 6 | `proof_formation_non_nested_frame_replication_checker_v0.1.py` | 4 | N1–N5 での再現、非単調性、置換制御 | 一般的 robustness |
| 7 | `proof_formation_minimal_separating_field_set_checker_v0.1.py` | 4 | field ablation、singleton separator | 意図した区別の説明（KILL） |
| 8 | `theorem_proof_quotient_invariance_pilot_v0.1.py` | 6-D | 16 term の型検査、Q0–Q4 の class count | 強正規化・合流性、非形式的 IVT/FTA 証明の同値性 |

---

## 4. 系列外・周辺ファイル

以下は本系列の対象だが、上表の主要 chain には現れない。最終記録では脚注扱いで足りる。

| ファイル | 位置づけ |
|---|---|
| `tool_truth_absence_research_trajectory.svg` | trajectory summary の図。本文の主張は `.md` 側にある |
| `deferred_resolution_case_01_gst_adversarial_review_codex.md` / `_claudecode.md` | GST の敵対的レビュー 2 件。E06 の C-3 相当の訂正根拠 |
| `web_of_constraints_methodology_second_order_review_claudecode.md` | 枝 B の二次レビュー |
| `qualification_practices_comparative_study_design_v0.1.md` | 水文学枝の設計文書 |
| `proof_formation_reader_01_v0.1.md` / `_calibration_note.md` | pilot reader。coder instructions v0.1.1 の根拠だが、正式 reader 数には算入されない |
| `scientific_assurance_case_02_metrology_control_reconstruction.md` | 計量学の field-native control 側 |

---

## 5. Traceability caveats

1. `theorem_proof_anatomy/` の 11 ファイルは全て `09-04 20:32` の同一 mtime を持つ。ディレクトリ移動の痕跡であり、**内部順序は復元できない**。
2. mtime は最終更新であり作成時刻ではない。
3. 最古ファイル（`tool_truth_absence_working_note.md`, 08-16 07:08）自体が既に撤回史の再構成であり、問いの発生時点ではない。
4. Phase 0 と Phase 1 の間に 13 日の空白があり、その間の作業を示す資料は `notes/` にない。
5. Phase 2–7 は約 45 時間に集中している。独立な再検証は行われていない。
6. Phase 7 の independent audit は系列内で書かれたものであり、外部監査ではない。

---

**End of source map.** 分析・判定・章立ては source architecture 側にある。本ファイルは対応表のみを保持する。

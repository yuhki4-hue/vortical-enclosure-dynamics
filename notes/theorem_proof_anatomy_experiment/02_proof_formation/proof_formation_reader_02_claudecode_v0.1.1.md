# Proof-Formation Reader 02 (Claude Code) — Independent Reconstruction v0.1.1

- **Reader:** independent blind Reader 02
- **Instructions followed:** `proof_formation_coder_instructions_v0.1.1.md`
- **Input packet:** `proof_formation_frozen_toy_corpus_v0.1.md`
- **Date of coding:** 2026-09-05
- **Output type:** qualitative reconstruction only. No adjudication, no framework revision, no score, rank, geometry, agreement rate, or general law.

## 0. Isolation record

Read for this run: the two files above, and nothing else.

Original sources were **not** consulted. Several excerpts are thin (E06 Excerpt 2 is a single table row; E08 Excerpt 1 is a bare heading; E09/E10/E11/E12 rely on source-local ladders whose definitions are outside the packet). Under coder instructions this permits returning to a listed original source, but two of the listed paths are themselves `v0.1_to_v0.2` diff documents, i.e. secondary reconstructions of the trajectory, and the excerpt-insufficiency could not be resolved without them. I therefore coded from excerpts only and recorded the resulting gaps as `UNKNOWN` / `AMBIGUOUS` rather than closing them. Every such gap is listed in §4.8.

No adjudication rules, answer key, meta-experiment document, trajectory summary, calibration note, or other reader output was read.

## 1. Step 0 — Segmentation record (made before any move coding)

| Parent item | Subepisodes coded | Alternative segmentation retained? |
|---|---|---|
| E01 | E01 (single) | recorded, not source-compatible as two transitions |
| E02 | E02-a, E02-b | **yes — AMBIGUOUS boundary** |
| E03 | E03 (single) | recorded, not adopted |
| E04 | E04 (single) | **yes — AMBIGUOUS boundary** |
| E05 | E05-a, E05-b | **yes — AMBIGUOUS internal split of E05-a** |
| E06 | E06-a, E06-b, E06-c | **yes — AMBIGUOUS (single-episode reading)** |
| E07 | E07 (single) | none |
| E08 | E08 (single) | **yes — AMBIGUOUS (two-change reading)** |
| E09 | E09-a, E09-b | none (source states two stages explicitly) |
| E10 | E10 (single) | none |
| E11 | E11 (single) | none |
| E12 | E12-a, E12-b | none (two distinct 判定 blocks) |

18 subepisode blocks follow. Where an alternative segmentation is retained, the duplicated text must **not** be counted as two independent results.

Standing warning applied throughout: source-local labels (`M0`–`M3` in E07, `DR-1`/`Null C`/`Null D/E` in E06, `N-04`/`L-01`–`L-03` in E08, `NONEVAL`/`RET-DOWN`/`D 相当` in E09, `C1`–`C3` in E10, `S1`/`S2`/`S2*` in E11–E12, `A2`/`A3` in E12, `R0/R1/R2`) are **not** formation move codes M1–M17 and were never read as such.

---

## 2. Submission blocks

### E01

```text
parent_corpus_item: E01 — Observation-map noninjectivity
subepisode_id: E01

episode_boundary: Excerpt 1 (hypothesis) → Excerpt 2 (two witnesses) → Excerpt 3 (one [WITHDRAWN] + one [ESTABLISHED]). Single transition: the source records exactly one withdrawal and one retention.
alternative_segmentations: considered and NOT adopted — a split into (a) novelty-claim vs prior art and (b) content-claim vs the counterexample O=id_W. Rejected because both witnesses stand in one "何によって壊れたか" block and feed one withdrawal record; there is no second claim_after. Not marked AMBIGUOUS.

claim_identity: B01
claim_before: 候補世界集合 W、ログ空間 L、観測写像 O:W→L について、O(w1)=O(w2) かつ w1≠w2 ならばログから世界を一意に復元できない。「この構造を『観測写像の存在論的非一意性定理』として一般化できるのではないか」。
target_and_scope: target = 一般の観測写像 O:W→L（対象クラス無制限、モデルクラス指定なし）。quantifier strength = 一般定理として主張（universal）。required conclusion = ログからの世界の一意復元不可能性が新しい一般定理として成立すること。
obligation_type: 二重。(i) formal theorem（一般定理としての成立）と (ii) literature/novelty claim（「新しい」一般定理であること）。source は両方を要求しているので一方に決めない。

assumptions: W, L の存在と写像 O:W→L；ある w1≠w2 について O(w1)=O(w2)（非単射性）。
proof_or_evidence_resources: 「非単射写像に左逆がない」という初等的事実のみ（Excerpt 2 が claim の内容をこれに還元している）。それ以上の proof resource は source に現れない。
evaluation_or_decision_rules: 「非単射写像に左逆がないこと以上の内容は、O が非単射でなければならない条件を別途示さない限り得られない」＝ 内容性／新規性の判定規則（Excerpt 2）。

failure_witness: (i) prior art: 「これは inverse problems、identifiability、observational equivalence、quotient/fiber の基本設定そのものである」。(ii) counterexample: 「O=id_W は即座の反例である」（非単射性が一般には成り立たないことの witness）。
available_branches: 「O が非単射でなければならない条件を別途示す」— source が明示的に利用可能としつつ、この subepisode では取らない修復路。
adopted_side_claims: S01 = [ESTABLISHED]「観測同値類と採用した構造同型類は区別しなければならない。識別可能性はモデルクラスと実験族に相対的である。」

move_taken:
  M15 — prior-art absorption. 主張と語彙を inverse problems / identifiability / observational equivalence / quotient-fiber という既存設定へ戻す（Excerpt 2）。
  M17 — withdrawal. [WITHDRAWN]「観測写像の存在論的非一意性」を新しい一般定理として主張すること（Excerpt 3）。
  M14 — disambiguation / type correction. 観測同値類と構造同型類という二つの同値概念を分離する（Excerpt 3, S01）。
  considered and NOT coded: M5（target を代表元から同値類へ移す操作ではなく、二つの同値概念の区別の言明であるため）。M4（「モデルクラスと実験族に相対的」は相対性の言明であって、before/after の対象クラス狭化が示されていない）。
claim_after:
  A1: B01 — 新しい一般定理としての主張は取り下げられ、残るのは「非単射写像に左逆がない」という既存の初等事実のみ。
  A2 [S01]: 観測同値類 ≠ 採用した構造同型類。識別可能性はモデルクラスと実験族に相対的。
terminal_status:
  A1: withdrawn（source 表記 [WITHDRAWN]）
  A2 [S01]: retained / established（source 表記 [ESTABLISHED]）

provenance_label:
  claim_before: SOURCE-DERIVED (Excerpt 1)
  episode_boundary: SOURCE-DERIVED (Excerpts 1–3 の三部構成)
  dependencies: assumptions = SOURCE-DERIVED; proof_or_evidence_resources = SOURCE-DERIVED (Excerpt 2); evaluation_or_decision_rules = SOURCE-DERIVED (Excerpt 2)
  failure_witness: SOURCE-DERIVED (Excerpt 2)
  available_branches: SOURCE-DERIVED (Excerpt 2 の「別途示さない限り」)
  adopted_side_claims: SOURCE-DERIVED (Excerpt 3)
  move_taken: M15 SOURCE-DERIVED; M17 SOURCE-DERIVED; M14 INFERENCE（S01 の「区別しなければならない」を type correction と読む一段の推論）
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: あり（SOURCE-DERIVED）。conclusion（一意復元不可能性）が premise（非単射性）に含まれており、主張は「非単射写像に左逆がない」へ退化する。名目上の target（新しい一般定理）が、実際には既存の初等事実の再記述であるという leakage。
source_excerpts_used: E01 Excerpt 1, 2, 3
uncertainties:
  - obligation_type を formal theorem と novelty claim のどちらか一方に決められない。source は両方を同時に要求している。
  - S01 が「この episode で採用された side claim」なのか「もともと背景として知られていた事実の再確認」なのか、source からは決められない（[ESTABLISHED] タグは前者を示唆するが、Excerpt 2 の prior-art 指摘は後者を示唆する）。
  - M14 と M5 の境界。S01 は同値類の話だが target 変更ではない。
```

### E02-a

```text
parent_corpus_item: E02 — Self-containment impossibility and conditional capacity
subepisode_id: E02-a

episode_boundary: Excerpt 1（自己包含からの一般不可能性仮説）→ Excerpt 2（反構成・濃度・quine/Kleene・Breuer/Wolpert の追加条件）→ Excerpt 3（[WITHDRAWN] + [ESTABLISHED]）。Excerpt 4 は別 subepisode（E02-b）として分離。
alternative_segmentations: **AMBIGUOUS**。二つの segmentation が source-compatible。
  (S-i) 採用: E02-a（一般含意の撤回＋定性的 side claim）/ E02-b（条件付き容量命題の採用）。根拠: Excerpt 4 は独自の assumption 集合・独自の失効条件・独自の「定理ではない」判定を持つ。
  (S-ii) 非採用だが両立可能: E02 全体を一つの episode とし、Excerpt 3 の [ESTABLISHED] と Excerpt 4 の条件付き命題をともに claim_after (A2, A3) とする。根拠: Excerpt 4 冒頭の「残る」が Excerpt 3 の「残ったもの」と連続する。
  E02-a / E02-b の境界は AMBIGUOUS。両者を独立した二結果として数えないこと。

claim_identity: B02
claim_before: 「観測者が世界内部の物理過程なら、観測は静的写像ではなく W_t →^{O_A} (W_{t+1}, l) と書くべきであり、自己を含む世界の完全記述は一般に不可能ではないか。」撤回形での定式化は「self-containment ⇒ universal non-identifiability」。
target_and_scope: target = 自己を含む任意の世界／内部観測者。quantifier strength = 一般（universal、条件なし）。domain = 制限なし（有限・無限、計算モデル指定なし）。required conclusion = 完全記述／識別の不可能性。
obligation_type: formal theorem（一般不可能性定理）。

assumptions: 観測者は世界内部の物理過程である；観測は静的写像ではなく時間発展 W_t → (W_{t+1}, l) である。
proof_or_evidence_resources: 元の主張に対して提示された proof resource は source にない（UNKNOWN）。失敗側の resource は failure_witness に記載。
evaluation_or_decision_rules: 「自己包含だけでは非単射性は導けない」「それ単独では不可能性を生まない」＝ 自己包含のみを前提として非単射性が導けることを支持条件とする規則。
  provenance 注: 規則としては明示されておらず、「だけでは／単独では」の反復から再構成した（INFERENCE）。

failure_witness:
  (i) 反構成: 有限候補 Ω と十分大きな内部記憶 M に対する閉じた系 X = Ω×M, (θ,m0) ↦ (θ, enc(θ))。内部観測者が候補を一意に記録できる。
  (ii) 無限集合では真部分集合と全体が同じ濃度を持ちうる。
  (iii) quine および Kleene の再帰定理（適切な計算モデルでは自己記述が可能）。
  (iv) Breuer の自己測定制約・Wolpert の inference-device 不可能性には追加条件（真部分系への制限、全状態の識別要求、固定された出力意味論、自己問合せ閉包）がある。
available_branches: (iv) が列挙する追加条件——真部分系への制限／全状態の識別要求／固定された出力意味論／自己問合せ閉包——を主張へ加える路。source は明示するが、この subepisode では採らない（一部は E02-b で採用される）。
adopted_side_claims: S02 = [ESTABLISHED]「自己包含は、識別対象に観測者自身の状態や出力を含めるため、容量制約や対角化の前提を成立させることがある。しかし、それ単独では不可能性を生まない。」

move_taken:
  M17 — withdrawal. [WITHDRAWN] self-containment ⇒ universal non-identifiability（Excerpt 3）。
  M14 — disambiguation / type correction. 「前提を成立させること（enabling）」と「不可能性を生むこと（entailing）」を型として分離（Excerpt 3, S02）。
    注: M14 の例示リスト（truth/provability, local/uniform, stage/modality/ordinal, artifact/institution/field）にこの対は含まれない。一般カテゴリとしての M14 に入れた。
  considered and NOT coded: M15。quine/Kleene/Breuer/Wolpert は主張を既存定理へ「戻す」absorption ではなく、主張を否定または条件付き化する witness として使われている（instructions: counterexample / prior-art は通常 trigger または witness であって move ではない）。
claim_after:
  A1: B02 — 一般含意は撤回。
  A2 [S02]: 自己包含は容量制約・対角化の前提を成立させうるが、それ単独では不可能性を生まない。
terminal_status:
  A1: withdrawn（source 表記 [WITHDRAWN]）
  A2 [S02]: retained / established（source 表記 [ESTABLISHED]）

provenance_label:
  claim_before: SOURCE-DERIVED (Excerpt 1) / 撤回形の定式化は Excerpt 3 の式そのもの
  episode_boundary: INFERENCE — Excerpt 4 を別 subepisode とする判断は、独自 assumption 集合と「自己包含定理ではない」という別判定に基づく。AMBIGUOUS フラグ付き。
  dependencies: assumptions = SOURCE-DERIVED; proof_or_evidence_resources = UNKNOWN; evaluation_or_decision_rules = INFERENCE
  failure_witness: SOURCE-DERIVED (Excerpt 2)
  available_branches: SOURCE-DERIVED (Excerpt 2 の追加条件列挙)
  adopted_side_claims: SOURCE-DERIVED (Excerpt 3)
  move_taken: M17 SOURCE-DERIVED; M14 INFERENCE
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: この subepisode では退化の指摘はない。失敗は「定義への埋め込み」ではなく「前提からの導出不足」。target leakage の芽は E02-b に現れる（「自己包含定理」という名前が、実際には容量条件が生む結果を取り込むこと）。
source_excerpts_used: E02 Excerpt 1, 2, 3
uncertainties:
  - Excerpt 1 の「観測は静的写像ではなく W_t → (W_{t+1}, l) と書くべき」は、E01 の O:W→L を before とすれば M7（model/target 改訂）として coding しうる。しかし corpus item をまたぐ before の設定が許されるか instructions からは決められないため、ここでは coding せず uncertainty として記録する。
  - evaluation rule が規則として明示されていない（「だけでは」という否定形からの再構成）。
```

### E02-b

```text
parent_corpus_item: E02 — Self-containment impossibility and conditional capacity
subepisode_id: E02-b

episode_boundary: Excerpt 4 単独。before = 撤回された B02（Excerpt 3）、obstacle = E02-a の witness 群、move = 条件の追加と対象の限定、after = 条件付き容量命題。
alternative_segmentations: **AMBIGUOUS**（E02-a の欄と同一。S-ii では本ブロックは E02 の A3 になる）。E02-a と E02-b を独立した二結果として数えないこと。

claim_identity: B02'（B02 の後継として提示された条件付き命題）
claim_before: B02 = self-containment ⇒ universal non-identifiability（E02-a で撤回済み）。
target_and_scope: after 側の target = 有限世界 X = A×E、識別候補 Ω = X（全初期状態）、最終記録が真部分系 A に収まる場合の最終回答写像 r: X→A。quantifier strength = 指定条件下の全称（「任意の最終回答 r」）。required conclusion = r は単射になれない。
obligation_type: formal theorem（条件付き命題／proof step）。source は「これは『自己包含定理』ではなく…命題である」と明記する。

assumptions:
  (a) 世界は有限で X = A×E の形；
  (b) 識別候補は全初期状態 Ω = X；
  (c) 全ての利用可能な最終記録が真部分系 A に収まらなければならない；
  (d) |E| > 1。
  さらに source は、この単純な議論が使えなくなる条件を明示する：候補を小さな部分集合へ制限する／環境自由度を記憶として利用する／外部ログを認める／無限集合で濃度差が消える。これらは admissible cases を画定するので assumptions 欄に置く（否定形の境界条件）。
  役割注記: この四条件は「反論者による救済路」＝available_branches とも読める。source は役割を決めていない。重複記載を避け、assumptions に一度だけ置き、境界問題として §4.6 に記録した。
proof_or_evidence_resources: |X| = |A||E| > |A|（|E|>1）による計数論法。source は結論のみ述べ論法名を書いていないため INFERENCE。
evaluation_or_decision_rules: 「これは『自己包含定理』ではなく、自己包含に記録場所・候補範囲・有限容量を加えた命題である」＝ 何を定理名として認めるかの判定規則（naming/attribution rule）。

failure_witness: NOT APPLICABLE（この subepisode 内では新たな失敗は起きていない。before の失敗は E02-a の witness 群）。
available_branches: UNKNOWN（この subepisode で明示的に提示され採られなかった修復路は source にない）。
adopted_side_claims: NOT APPLICABLE（本 subepisode の after は side claim ではなく、条件付き後継主張そのもの）。

move_taken:
  M1 — assumption strengthening. 記録場所（最終記録が真部分系 A に収まる）・候補範囲（Ω = X）・有限容量を主張の条件として追加（Excerpt 4）。
  M4 — object / domain restriction. 一般の「自己を含む世界」から有限世界 X = A×E、|E|>1 へ対象を限定（Excerpt 4）。
  considered and NOT coded: M2。結論は「一般に不可能」から「r は単射になれない」へ変わったが、これは M1+M4 による条件化の帰結であり、結論そのものの弱化として独立に cite できる before/after が取れない。AMBIGUOUS として §4.4 に記録。
  considered and NOT coded: M8。計数論法は proof resource として記録したが、before に proof が存在しないため「route change」として before/after を cite できない。
claim_after:
  A1: 有限世界 X = A×E、Ω = X、最終記録は真部分系 A に収まる、|E|>1 のとき、任意の最終回答 r: X→A は単射になれない。
terminal_status:
  A1: retained as conditional（source: 「条件付きの容量命題は残る」）。明示的に「自己包含定理」ではないと格下げ命名されている。

provenance_label:
  claim_before: SOURCE-DERIVED (Excerpt 3)
  episode_boundary: INFERENCE（AMBIGUOUS フラグ付き）
  dependencies: assumptions = SOURCE-DERIVED; proof_or_evidence_resources = INFERENCE; evaluation_or_decision_rules = SOURCE-DERIVED
  failure_witness: NOT APPLICABLE
  available_branches: UNKNOWN
  adopted_side_claims: NOT APPLICABLE
  move_taken: M1 SOURCE-DERIVED; M4 SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: target leakage の明示的な遮断がある（SOURCE-DERIVED）。source は、不可能性を生んでいるのは自己包含ではなく追加された記録場所・候補範囲・有限容量であると述べ、「自己包含定理」という名前がその功績を取り込むことを拒否している。
source_excerpts_used: E02 Excerpt 3, 4
uncertainties:
  - 四つの失効条件の役割（assumptions か available_branches か）が source で決まらない。
  - A1 が B02 の後継なのか、独立に成立する別命題なのかは source からは決められない。「残る」という語のみが接続を示す。
  - M2 を coding すべきかどうか。
```

### E03

```text
parent_corpus_item: E03 — Generation–log non-isomorphism
subepisode_id: E03

episode_boundary: Excerpt 1（仮説）→ Excerpt 2（定義への埋め込み・逆向き反例・prior art）→ Excerpt 3（[WITHDRAWN] + [ESTABLISHED] 2 件）。単一 transition。
alternative_segmentations: 考慮したが採用せず — Excerpt 3 の第二文（Blackwell 的「後処理で得られる情報」≠ 物理的に同時実行可能な測定）を独立 subepisode とする案。独自の before/failure を欠くため transition として成立しない。A3 として同一ブロック内に置いた。AMBIGUOUS とはしない。

claim_identity: B03
claim_before: 「観測ログは生成ダイナミクスのコピーではなく、generation → constraint formation → stabilization → log を経るため、生成構造と安定ログ空間の同型は一般に失われるのではないか。」撤回形では「生成からログへの段階が存在するだけで、生成構造の非一意性が従う」。
target_and_scope: target = 任意の生成過程と観測ログの対。quantifier strength = 一般（「一般に失われる」）。required conclusion = 生成構造と安定ログ空間の非同型性／生成構造の非一意性。
obligation_type: formal theorem（一般命題）。

assumptions: 生成 → 制約形成 → 安定化 → ログ という段階の存在。
proof_or_evidence_resources: 元主張に対する resource は source にない（UNKNOWN）。「安定化＝多対一写像」「記録＝粗視化」という定義は、resource ではなく退化の原因として指摘されている。
evaluation_or_decision_rules: 「情報損失は仮定ではなく、具体的なチャネル、統計量、力学、同値関係について証明しなければならない」。
  役割注記: この文は source で [ESTABLISHED] タグ付きの retained claim でもある。判定規則と採用側主張の両方の役割を持ち、source は役割を決めていない → 役割 AMBIGUOUS。重複記載を避けるため adopted_side_claims (S03) に実体を置き、本欄では役割の重複のみ記録する。

failure_witness:
  (i) 定義への埋め込み: 「『安定化』を多対一写像、『記録』を粗視化として定義すれば、非同型性を定義へ埋め込んでいるだけである」。
  (ii) 逆向きの反例: 過程全体が可逆で全情報を保持する場合、またはログが生成状態を完全符号化する場合には同型または単射が可能。
  (iii) prior art: coarse graining、Blackwell comparison、sufficient statistics、bisimulation、minimal realization が「どの情報が保存されるかを既に精密化している」。
available_branches: 具体的なチャネル／統計量／力学／同値関係を固定して情報損失を証明する路（source は要求として明示するが、本 subepisode では実行されていない）。
adopted_side_claims:
  S03 = [ESTABLISHED] 情報損失は仮定ではなく、具体的なチャネル・統計量・力学・同値関係について証明しなければならない。
  S03b = [ESTABLISHED] Blackwell 的な「後処理で得られる情報」と物理的に同時実行可能な測定は同じではない。

move_taken:
  M17 — withdrawal. [WITHDRAWN] 段階の存在だけから生成構造の非一意性が従うという主張（Excerpt 3）。
  M15 — prior-art absorption. 主張を coarse graining / Blackwell comparison / sufficient statistics / bisimulation / minimal realization という既存の精密化へ戻す（Excerpt 2）。
  M14 — disambiguation / type correction. 「後処理で得られる情報」と「物理的に同時実行可能な測定」を型として分離（S03b）。
claim_after:
  A1: B03 — 撤回。
  A2 [S03]: 情報損失は具体的なチャネル・統計量・力学・同値関係について証明すべき対象であって、仮定ではない。
  A3 [S03b]: Blackwell 的 post-processing 情報 ≠ 物理的に同時実行可能な測定。
terminal_status:
  A1: withdrawn（[WITHDRAWN]）
  A2 [S03]: retained / established（[ESTABLISHED]）
  A3 [S03b]: retained / established（[ESTABLISHED]）

provenance_label:
  claim_before: SOURCE-DERIVED (Excerpt 1, 3)
  episode_boundary: SOURCE-DERIVED
  dependencies: assumptions = SOURCE-DERIVED; proof_or_evidence_resources = UNKNOWN; evaluation_or_decision_rules = AMBIGUOUS（S03 と役割重複）
  failure_witness: SOURCE-DERIVED (Excerpt 2)
  available_branches: SOURCE-DERIVED (Excerpt 3 の「証明しなければならない」)
  adopted_side_claims: SOURCE-DERIVED (Excerpt 3)
  move_taken: M17 SOURCE-DERIVED; M15 SOURCE-DERIVED; M14 SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: あり（SOURCE-DERIVED、明示）。「非同型性を定義へ埋め込んでいるだけである」＝ 結論が定義に前置されている退化。
source_excerpts_used: E03 Excerpt 1, 2, 3
uncertainties:
  - S03 が retained claim なのか判定規則なのかを source が決めていない。
  - available_branches（具体化して証明する路）と S03（そう証明せよという retained claim）が実質的に同一内容で、instructions は両欄への重複記載を禁じている。ここでは branch を「未実行の路」、S03 を「採用された主張」として書き分けたが、この分離自体が再構成である。
```

### E04

```text
parent_corpus_item: E04 — Pairwise separation versus a global adaptive separator
subepisode_id: E04

episode_boundary: Excerpt 1（量化順序の仮説）→ Excerpt 2（二ビット構成）→ Excerpt 3（外部でも同じ反例が成立／prior art／fresh preparation で消える）→ Excerpt 4（[WITHDRAWN] + [ESTABLISHED] + [SYNTHESIS]）。
alternative_segmentations: **AMBIGUOUS**。二つの segmentation が source-compatible。
  (S-i) 採用: 単一 episode。before = 「二ビット破壊例は内部性そのものが生む不可能性の例である」、after = A1 撤回 / A2 量化順序差の保持 / A3 synthesis。
  (S-ii) 非採用だが両立可能: E04-a = 量化順序仮説（Excerpt 1）が二ビット構成（Excerpt 2）によって支持される transition、E04-b = 内部性解釈（Excerpt 2 の用法）が Excerpt 3 によって撤回される transition。
  境界 AMBIGUOUS。同じ二ビット構成テキストを二つの独立結果として数えないこと。

claim_identity: B04
claim_before: 撤回対象として source が名指す形は「二ビット破壊例を、内部性そのものが生む不可能性の例として使うこと」。その背後の仮説は「各候補対を区別する実験が存在しても、それらを一つの適応的観測履歴へ統合できない系があるのではないか」（∀θ≠θ'∃e と ∃σ∀θ≠θ' の差）。
target_and_scope: target = 内部観測者。domain = 固定候補クラス Ω、単一コピー、破壊的操作。required conclusion = 内部性それ自体が大域的適応分離の不可能性を生む。
obligation_type: interpretation / reduction（構成例に対する原因帰属の主張）。付随して formal claim（量化順序の差）。

assumptions: 固定候補クラス Ω；候補は二ビット (a,b)；操作 A は a を読み b を破壊、操作 B は b を読み a を破壊；単一コピー；リセット不能；記憶は共通。
proof_or_evidence_resources: 二ビット破壊構成そのもの（Excerpt 2）。順序によらず片方を失うという議論。
evaluation_or_decision_rules: 「同じ単一コピー、同じ破壊的操作、同じ記憶、同じリセット不能を外部観測者へ課せば、外部でも同じ反例が成立する」＝ 資源を揃えた対照（matched-resource control）による原因帰属の判定。規則としては明示されず、適用の形で現れる（INFERENCE）。

failure_witness:
  (i) 対照結果: 同一資源条件を外部観測者へ課すと同じ反例が成立する。したがって障害は内部性に固有でない。
  (ii) prior art: 有限状態機械の adaptive distinguishing sequence、active diagnosis、sequential experiment design が適応的識別方策の存在を「既に扱っている」。
available_branches: 「外部インターフェースが同じ固定 θ に従う fresh preparation を有限回許すなら、この反例は消える」— source が明示する条件変更路。この subepisode では採らない。
  役割注記: これは修復路とも、反例の適用範囲を画定する scope condition とも読める。source は決めていない（§4.6）。
adopted_side_claims:
  S04 = [ESTABLISHED] ペアごとの実験可能性と単一方策による大域分離の間には量化順序の差がある。
  S04b = [SYNTHESIS] その差を接続するには、「内部性」というラベルではなく、対象モデルに適した逐次合成、記録保存、共通精密化、uniformity、誤差制御などを調べる必要がある。どれが必要十分かは設定ごとに異なる。

move_taken:
  M17 — withdrawal. [WITHDRAWN] 二ビット破壊例を内部性由来の不可能性例として使うこと（Excerpt 4）。
  M15 — prior-art absorption. 適応的識別方策の問題を adaptive distinguishing sequence / active diagnosis / sequential experiment design へ戻す（Excerpt 3）。
  M14 — disambiguation / type correction. (i) ∀∃ と ∃∀ の量化順序の分離（local な対分離 vs 大域方策＝ M14 の "local from uniform/global" に該当）、(ii)「内部性」というラベルと、実際に効いている資源条件（単一コピー・破壊性・リセット不能）の分離（Excerpt 3, 4）。
  considered and NOT coded: M16。S04b は「調べる必要がある」という研究方向であって、control comparison / document audit / finite test への置換ではない。
  considered and NOT coded: M8。二ビット構成は witness / resource であり、instructions により counterexample は通常 move ではない。
claim_after:
  A1: B04 — 内部性由来の不可能性例という解釈は撤回。
  A2 [S04]: ペアごとの実験可能性と単一方策による大域分離の間の量化順序の差（維持）。
  A3 [S04b]: 差の接続には、対象モデルに適した逐次合成・記録保存・共通精密化・uniformity・誤差制御を調べる必要がある。必要十分条件は設定依存。
terminal_status:
  A1: withdrawn（[WITHDRAWN]）
  A2 [S04]: retained / established（[ESTABLISHED]）
  A3 [S04b]: open（[SYNTHESIS]。source は必要十分性が設定ごとに異なるとして未決のまま残す）

provenance_label:
  claim_before: SOURCE-DERIVED (Excerpt 4 の撤回文 + Excerpt 1 の仮説)
  episode_boundary: AMBIGUOUS（上記 S-i / S-ii）
  dependencies: assumptions = SOURCE-DERIVED; proof_or_evidence_resources = SOURCE-DERIVED; evaluation_or_decision_rules = INFERENCE
  failure_witness: SOURCE-DERIVED (Excerpt 3)
  available_branches: SOURCE-DERIVED (Excerpt 3 末尾)
  adopted_side_claims: SOURCE-DERIVED (Excerpt 4)
  move_taken: M17 SOURCE-DERIVED; M15 SOURCE-DERIVED; M14 SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED（A3 の "open" は [SYNTHESIS] タグと「設定ごとに異なる」からの INFERENCE）

degenerate_or_target_leakage: target leakage あり（SOURCE-DERIVED）。反例を生んでいるのは資源条件（単一コピー・破壊的操作・リセット不能）であるのに、「内部性」という名目上の target がその結果を取り込んでいた。Excerpt 3 の対照がこれを露出させる。
source_excerpts_used: E04 Excerpt 1, 2, 3, 4
uncertainties:
  - segmentation が二通り残った（上記）。
  - fresh preparation 条件が available branch か scope condition かが決まらない。
  - A2（量化順序差）が本 episode で確立されたのか、Excerpt 1 の時点で既に前提だったのかが決まらない。S-ii を採ればこの点の扱いが変わる。
```

### E05-a

```text
parent_corpus_item: E05 — v0.1 to v0.2 internal/external interface correction
subepisode_id: E05-a

episode_boundary: Excerpt 1（diff 行：一般 equivalence が強すぎる→撤回し二分割、accepted）+ Excerpt 2（v0.1 の一般 [ESTABLISHED] とその混線）→ Excerpt 3（1. 規約的同値 / 2. 条件付きモデル対応）→ Excerpt 4 第一文（[WITHDRAWN]）。
alternative_segmentations: **AMBIGUOUS**。
  (S-i) 採用: 一つの transition、after は A2（規約的同値）と A3（条件付き補題）の二つ。根拠: 一つの撤回・一つの witness から二つの置換が同時に生じており、diff 行も一つの revision として記録している。
  (S-ii) 非採用だが両立可能: E05-a1（撤回→規約的同値）と E05-a2（撤回→条件付きモデル補題）へ分割。根拠: 二つの after は obligation_type が異なり（規約 vs 条件付き定理）、move も異なる。
  S-i を採ったため、下記 move_taken では各 move がどの after-claim に対応するかを注記した（submission block には move を after-claim 別に書く欄がない。§4.7）。

claim_identity: B05
claim_before: v0.1 の一般 [ESTABLISHED]「内部と外部の制御器に同じ入力、出力、記憶容量、コピー数、reset、敵対性、因果インターフェースを与えれば、生成可能な履歴集合は同じになる」。
target_and_scope: target = 一般の内部観測者と外部制御器。quantifier strength = 一般（無条件の [ESTABLISHED]）。required conclusion = 生成可能履歴集合の一致（＝識別能力の同値）。
obligation_type: formal theorem（一般同値命題）。source は事後に、これが存在命題と規約の混線であったと述べる。

assumptions: 「同じ入力、出力、記憶容量、コピー数、reset、敵対性、因果インターフェース」を与えること。source はこの assumption 自体が非形式的で内容未確定であったと指摘する。
proof_or_evidence_resources: v0.1 側の proof resource は「非形式的な仮定」のみ（Excerpt 4：「非形式的に仮定するだけで…証明される」）。v0.2 側では A3 に対して履歴長についての帰納法が resource として与えられる。
evaluation_or_decision_rules: 「『同じインターフェース』の中に何を含めるかが不十分」＝ インターフェース同一性の内容を完全に指定していない主張は一般命題として認めない、という判定。diff 行の判定値は accepted。

failure_witness: 「『同じインターフェース』の中に何を含めるかが不十分であり、実際の内部観測者をそのような外部制御器へ還元できるという存在命題と、同じ履歴能力を定義上与える規約とが混線していた」（Excerpt 2）。すなわち内部的な型混同が witness であり、外部の反例や prior art ではない。
available_branches: UNKNOWN。source は二つの置換を実際に採用しており、採られなかった路は excerpt に現れない。
adopted_side_claims: NOT APPLICABLE（下記 A2/A3 は side claim ではなく、撤回された主張の二つの後継として明示的に置かれている）。

move_taken:
  M17 — withdrawal（対象: B05）。v0.1 の一般 [ESTABLISHED] を撤回（Excerpt 1, 2, 4）。
  M14 — disambiguation / type correction（B05 → A2/A3 の分割そのもの）。「存在命題」と「定義上の規約」を型として分離する（Excerpt 2）。
  M1 — assumption strengthening（→ A2 に対応）。完全な実現可能インターフェース I（timing、concurrency、memory accessibility、memory vulnerability、computational cost、embodiment cost、self-readout、stochasticity、causal channels、reset/copy/fresh preparation、adversarial access）を指定する（Excerpt 3-1）。
  M1 — assumption strengthening（→ A3 に対応）。制御器状態が宣言された遷移だけにより更新される／宣言された記憶へのアクセスが保証される／計算遅延と embodiment cost が状態遷移へ明示される／状態写像が許容 action・transition・observation を可換に保つ（Excerpt 3-2）。
  M4 — object / model-class restriction（→ A3 に対応）。一般の観測者から「離散時間・turn-based の controlled transition system」へモデルクラスを限定（Excerpt 3-2）。
  M8 — proof-resource addition / route change（→ A3 に対応）。履歴長についての帰納法という証明経路を追加（Excerpt 3-2）。
  considered and NOT coded: M2。A3 の結論（同じ transcript 分布）は M1+M4 による条件化の帰結であり、結論自体の弱化として独立に cite できる before/after が取りにくい。AMBIGUOUS として記録。
  considered and NOT coded: M9。「一方の方策を他方へ移す」は保存内容を指定した reduction にも見えるが、source は consequence class の保存を指定しておらず transcript 分布の一致を述べている。
claim_after:
  A1: B05 — 一般形は撤回。
  A2（規約的同値）: 完全な実現可能インターフェース I を指定し、二つの制御器に許される protocol と transcript の関係を同一と定義すれば、両者の履歴集合は一致する。source 自身が「物理的に重要な同値定理というより、行動的インターフェースの同一性をどう定義したかの帰結」と限定する。
  A3（条件付きモデル対応）: 指定された離散時間・turn-based controlled transition system と可換な状態写像の下で、履歴長の帰納法により一方の方策を他方へ移して同じ transcript 分布を得られる。「指定モデル内の条件付き補題であり、そのような状態写像が現実の観測者について存在することを保証しない」。
terminal_status:
  A1: withdrawn（source 表記 [WITHDRAWN]、diff 判定 accepted）
  A2: retained as convention / definitional（退化の明示付き）
  A3: retained as conditional lemma（指定モデル内。現実の観測者への存在保証なし）

provenance_label:
  claim_before: SOURCE-DERIVED (Excerpt 2)
  episode_boundary: AMBIGUOUS（S-i / S-ii）
  dependencies: assumptions = SOURCE-DERIVED; proof_or_evidence_resources = SOURCE-DERIVED; evaluation_or_decision_rules = SOURCE-DERIVED (Excerpt 1, 2)
  failure_witness: SOURCE-DERIVED (Excerpt 2)
  available_branches: UNKNOWN
  adopted_side_claims: NOT APPLICABLE
  move_taken: M17 SOURCE-DERIVED; M14 SOURCE-DERIVED; M1(A2) SOURCE-DERIVED; M1(A3) SOURCE-DERIVED; M4 SOURCE-DERIVED; M8 SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: A2 に退化あり（SOURCE-DERIVED、明示）。「物理的に重要な同値定理というより、行動的インターフェースの同一性をどう定義したかの帰結」＝ 結論が定義に含まれている。A3 には退化の指摘はないが、source は現実の観測者への適用可能性を明示的に切り離しており、target leakage を自ら遮断している。
source_excerpts_used: E05 Excerpt 1, 2, 3, 4
uncertainties:
  - 一つの episode（A2/A3 併存）か二つの episode かが決まらない。
  - diff 行（Source path A）は二次文書の体裁を持つ。coder instructions は corpus 記載 path の原 source への復帰を許すが、diff 文書がその意味の「原 source」か「trajectory 再構成」かは判断できなかったため、excerpt のみで coding した。
  - A2 の「規約」に obligation_type を割り当てられない。instructions の列挙（formal theorem / proof step / interpretation or reduction / empirical / comparative / design decision / literature-novelty）に「定義的規約」に相当する型がない。
```

### E05-b

```text
parent_corpus_item: E05 — v0.1 to v0.2 internal/external interface correction
subepisode_id: E05-b

episode_boundary: Excerpt 4 第二文のみ。[WITHDRAWN]「`inside vs outside` という空間的位置だけを第一義的数学条件とすること」。E05-a とは claim identity が異なる（同値命題ではなく、何を第一義的な数学条件とするかという枠組み条件）。
alternative_segmentations: 考慮したが不採用 — Excerpt 4 の二つの [WITHDRAWN] を一つの決定として扱う案。二つは対象が異なる（同値命題／枠組み条件）ので分離した。ただし両者が一つの改訂判断の二側面である可能性は残る（§4.8）。

claim_identity: B05b
claim_before: `inside vs outside` という空間的位置を、識別能力を論じる際の第一義的な数学条件とすること。
target_and_scope: target = 内部／外部観測者の区別そのものの数学的地位。required conclusion = 空間的位置が一次的な区別条件である。
obligation_type: interpretation / reduction（枠組み条件の設定）。あるいは design decision。source は型を明示しない → AMBIGUOUS。

assumptions: 内部／外部が空間的位置として与えられること。
proof_or_evidence_resources: UNKNOWN（excerpt に現れない）。
evaluation_or_decision_rules: UNKNOWN。何をもって「第一義的数学条件」とするかの基準は excerpt にない。

failure_witness: excerpt 内に本主張専用の witness はない。Excerpt 2–3 が示すのは、実際に効いているのが列挙されたインターフェース属性（timing、memory accessibility/vulnerability、cost、self-readout、causal channels、reset/copy、adversarial access 等）であることであり、これを witness と読むのは再構成（INFERENCE）。AMBIGUOUS。
available_branches: UNKNOWN。
adopted_side_claims: 明示的な採用側主張は excerpt にない。Excerpt 3 のインターフェース属性群が代替条件として機能していると読めるが、source は「これを代わりに採用する」とは書いていない → UNKNOWN / INFERENCE。

move_taken:
  M17 — withdrawal. 空間的位置を第一義的数学条件とすることの撤回（Excerpt 4）。
  M14 — disambiguation / type correction. 空間的位置という記述と、識別能力を実際に決めるインターフェース属性とを型として分離（Excerpt 3 + 4 からの再構成）。
claim_after:
  A1: B05b — 撤回。
terminal_status:
  A1: withdrawn（[WITHDRAWN]）

provenance_label:
  claim_before: SOURCE-DERIVED (Excerpt 4)
  episode_boundary: INFERENCE（二つの [WITHDRAWN] を別 claim identity と読む判断）
  dependencies: UNKNOWN（assumptions を除き excerpt に情報がない）
  failure_witness: INFERENCE / AMBIGUOUS
  available_branches: UNKNOWN
  adopted_side_claims: UNKNOWN
  move_taken: M17 SOURCE-DERIVED; M14 INFERENCE
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: target leakage の疑い（INFERENCE）。空間的位置というラベルが、実際にはインターフェース属性が担う区別の功績を取り込んでいた。E04 の「内部性ラベル」に対する指摘と同型だが、E05 の excerpt 内でその接続は明示されていない。
source_excerpts_used: E05 Excerpt 3, 4
uncertainties:
  - この撤回が独立の transition か、E05-a の一部かが決まらない。
  - 専用の failure witness が excerpt にない。
  - 代替として何が第一義的条件になったのかが明示されていない。
```

### E06-a

```text
parent_corpus_item: E06 — GST Deferred Resolution v0.1 to v0.2
subepisode_id: E06-a

episode_boundary: Excerpt 1（Source A：ケース全体の最適判定は DR-1 Weak relocation、ただし Null C と Null D/E が強い読みを制限）→ Excerpt 2（diff：Final status = working positive case → frozen negative baseline）→ Excerpt 3（v0.2：Frozen negative result／「GST系列は、仮説した反復的なDeferred Resolution連鎖を支持しなかった」）+ Excerpt 4 第一項（ケース全体を支持結果とした旧判定を撤回）。
alternative_segmentations: **AMBIGUOUS**。
  (S-i) 採用: Excerpt 4 の三項目を三つの transition（E06-a ケース判定 / E06-b 機構名 / E06-c taxonomy）へ分割。根拠: claim identity が異なり、それぞれ独自の after を持つ。
  (S-ii) 非採用だが両立可能: E06 全体を一つの改訂 episode とし、A1–A4 を並べる。根拠: 三項目は一つの v0.2 §1.1 変更リストとして提示され、共通の witness（系列が連鎖を支持しなかった）を共有する。
  三 subepisode を独立した三結果として数えないこと。

claim_identity: B06a
claim_before: GST 系列は、仮説された反復的な Deferred Resolution 連鎖を支持する working positive case であり、ケース全体の最適判定は DR-1 — Weak relocation である。
target_and_scope: target = GST 系列全体（single case）。scope = 当該歴史系列に限定。source は「この判定は科学一般の法則を主張しない」と明記する。required conclusion = ケース全体が仮説を支持する陽性事例であること。
obligation_type: empirical claim（歴史的事例判定）／comparative claim。source 表記は case judgment。

assumptions: GST 系列を一つのケースとして扱えること。判定が科学一般の法則を主張しないこと（scope 制限として明示）。
proof_or_evidence_resources: excerpt からは判定の根拠資料が特定できない（UNKNOWN）。Null C / Null D/E は resource ではなく制限条件として現れる。
evaluation_or_decision_rules: (i) Null C（Solved by quotient）および Null D/E（historical sequencing / reviewer-imposed narrative）が全系列の強い読みを制限する、という null 判定規則。(ii) v0.2 の epistemic posture「field-native reconstruction first; no claim of a new mechanism」。
  注: Null C / D/E の定義は packet 内にない（UNKNOWN の内容）。規則の存在のみ SOURCE-DERIVED。

failure_witness: 「GST系列は、仮説した反復的なDeferred Resolution連鎖を支持しなかった」（Excerpt 3）。加えて Null C と Null D/E による強い読みの制限（Excerpt 1）。具体的な観察内容は excerpt 外（UNKNOWN）。
available_branches: UNKNOWN。excerpt には、採られなかった修復路（例: 別の判定 DR-2 等）が現れない。DR-1 判定自体が v0.2 で維持されたか否かも不明。
adopted_side_claims: excerpt 上、ケース判定を代替する側方主張は明示されない。Excerpt 5（既存語彙での再構成）は E06-b に置いた。

move_taken:
  M17 — withdrawal / negative-result fixation. 「ケース全体を支持結果とした旧判定を撤回した」（Excerpt 4）。加えて Status = Frozen negative result、diff の frozen negative baseline（Excerpt 2, 3）＝ 否定的判定の凍結。M17 の定義がこの二つ（撤回と negative result の凍結）を同一コードに含む。
  considered and NOT coded: M16。すでに経験的ケース研究であり、定理／枠組み新規性の対象を対照比較へ置換する transition ではない。
claim_after:
  A1: GST 系列は仮説された反復的 Deferred Resolution 連鎖を支持しなかった。ケースの status は frozen negative result（frozen negative baseline）。
terminal_status:
  A1: withdrawn（旧陽性判定）＋ negative result fixed / frozen（source 表記 "Frozen negative result", "frozen negative baseline", diff status "frozen"）。二つの status 語が一つの after-claim に付くが、これは同一決定の二側面として source が並記している。

provenance_label:
  claim_before: SOURCE-DERIVED (Excerpt 1, 2) — ただし Source A が改訂前テキストであるという読みは INFERENCE（§4.8）
  episode_boundary: AMBIGUOUS（S-i / S-ii）
  dependencies: assumptions = SOURCE-DERIVED; proof_or_evidence_resources = UNKNOWN; evaluation_or_decision_rules = SOURCE-DERIVED（内容は UNKNOWN）
  failure_witness: SOURCE-DERIVED (Excerpt 3)（witness の具体的内容は UNKNOWN）
  available_branches: UNKNOWN
  adopted_side_claims: NOT APPLICABLE
  move_taken: M17 SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: 明示的な退化指摘はない。Null D/E（historical sequencing / reviewer-imposed narrative）は、事後的な語りが陽性判定を作り出す形の leakage を警戒する規則と読めるが、excerpt がラベルのみで内容を欠くため INFERENCE にとどまる。
source_excerpts_used: E06 Excerpt 1, 2, 3, 4
uncertainties:
  - Source path A（`deferred_resolution_case_01_gst.md`、版表記なし）が改訂前テキストか、改訂後も併存する文書かが packet から決められない。claim_before の同定がこれに依存する。
  - DR-1 — Weak relocation が v0.2 で維持・撤回・再定義のいずれになったかが不明。
  - Null C / Null D/E の定義が packet 内にない。
```

### E06-b

```text
parent_corpus_item: E06 — GST Deferred Resolution v0.1 to v0.2
subepisode_id: E06-b

episode_boundary: Excerpt 4 第二項（Deferred Resolution を独立した機構名から、今回棄却された historical working hypothesis へ降格した）+ Excerpt 5（技術内容は既存語彙でより正確に再構成できる）。
alternative_segmentations: E06-a 欄と同じ **AMBIGUOUS**（S-ii では本ブロックは A2/A3 になる）。

claim_identity: B06b
claim_before: 「Deferred Resolution」は独立した機構名である（独自の機構を名指す語彙として成立する）。
target_and_scope: target = Deferred Resolution という機構名・語彙の地位。required conclusion = 独立機構としての成立。
obligation_type: literature/novelty claim（新機構語彙の主張）。

assumptions: 当該系列に共通機構が存在すること。
proof_or_evidence_resources: UNKNOWN（excerpt に新機構を支持する資料は現れない）。
evaluation_or_decision_rules: v0.2 の epistemic posture「field-native reconstruction first; no claim of a new mechanism」＝ 分野固有の再構成が先であり、新機構は主張しないという判定規則（Excerpt 3）。

failure_witness: 「技術内容は、conditional inverse problem、reference / nuisance uncertainty、joint estimation、identifiability modulo gauge、quotient parameterization、model checking、model-specific extension という既存語彙で、より正確に再構成できる」（Excerpt 5）。加えて E06-a の否定的ケース結果。
available_branches: UNKNOWN。
adopted_side_claims: S06b = Deferred Resolution は「今回棄却された historical working hypothesis」として保持される（機構名としてではなく、棄却済みの作業仮説として残る）。

move_taken:
  M15 — prior-art absorption. 技術内容を conditional inverse problem / reference・nuisance uncertainty / joint estimation / identifiability modulo gauge / quotient parameterization / model checking / model-specific extension という既存語彙へ戻す（Excerpt 5）。M15 の注記どおり、これは歴史的因果を立てるものでも、残余価値を消すものでもない。
  M17 — demotion. 独立機構名から棄却済み historical working hypothesis への降格（Excerpt 4）。
claim_after:
  A1: B06b — 独立機構名としての主張は降格・棄却。
  A2 [S06b]: Deferred Resolution は今回棄却された historical working hypothesis として記録される。
  A3: 技術内容は既存の分野語彙でより正確に再構成できる。
terminal_status:
  A1: demoted（source 表記「降格した」）
  A2 [S06b]: retained as rejected working hypothesis（棄却済みという地位で保持）
  A3: retained（source は再構成可能性を肯定形で述べる）

provenance_label:
  claim_before: INFERENCE — 「独立した機構名から降格した」という記述から before を再構成した。before 形の原文は excerpt にない。
  episode_boundary: AMBIGUOUS
  dependencies: assumptions = INFERENCE; proof_or_evidence_resources = UNKNOWN; evaluation_or_decision_rules = SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED (Excerpt 5)
  available_branches: UNKNOWN
  adopted_side_claims: SOURCE-DERIVED (Excerpt 4)
  move_taken: M15 SOURCE-DERIVED; M17 SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: target leakage あり（INFERENCE）。「Deferred Resolution」という機構名が、既存語彙で表現できる技術内容の説明力を取り込んでいた。Excerpt 5 がこれを露出させる。
source_excerpts_used: E06 Excerpt 3, 4, 5
uncertainties:
  - claim_before の原文が packet にない（降格記述からの逆算）。
  - 「棄却された historical working hypothesis として残す」ことが retention なのか完全な放棄なのか、source の語からは決めきれない。
```

### E06-c

```text
parent_corpus_item: E06 — GST Deferred Resolution v0.1 to v0.2
subepisode_id: E06-c

episode_boundary: Excerpt 4 第三項のみ（frequency、recurrence、formal invariance、diagnostic effect、modal impossibility を一列に並べた旧五段階 taxonomy を削除した）。
alternative_segmentations: E06-a 欄と同じ **AMBIGUOUS**（S-ii では本ブロックは A4 になる）。

claim_identity: B06c
claim_before: frequency、recurrence、formal invariance、diagnostic effect、modal impossibility を一列に並べた五段階 taxonomy が成立する。
target_and_scope: target = 当該五段階 taxonomy。required conclusion = 五項目が一つの段階列として並ぶこと。
obligation_type: AMBIGUOUS。分類体系の主張であり、instructions の型列挙（formal theorem / proof step / interpretation or reduction / empirical / comparative / design decision / literature-novelty / UNKNOWN）に taxonomy 主張の型がない。literature/novelty claim に近いが確定できない。

assumptions: 五項目が同一の尺度上に配置可能であること（削除理由が書かれていないため INFERENCE）。
proof_or_evidence_resources: UNKNOWN。
evaluation_or_decision_rules: UNKNOWN。削除の判定規則は excerpt に書かれていない。E06-a/b の epistemic posture が及んでいる可能性はあるが、source は接続を明示しない。

failure_witness: excerpt に taxonomy 固有の witness はない（UNKNOWN）。削除の事実のみが記録されている。
available_branches: UNKNOWN。
adopted_side_claims: NOT APPLICABLE（代替 taxonomy は excerpt に現れない）。

move_taken:
  M17 — abandonment. 旧五段階 taxonomy を削除（Excerpt 4）。
  considered and NOT coded: M14。五項目が異型（頻度・再帰・形式的不変性・診断効果・様相的不可能性）であることを理由とする型訂正と読むことはできるが、source は理由を書いていない。研究者の意図を推測しないという指示に従い coding しない。
claim_after:
  A1: 当該 taxonomy は存在しない（削除）。
terminal_status:
  A1: withdrawn / deleted（source 表記「削除した」）

provenance_label:
  claim_before: INFERENCE（削除記述からの逆算）
  episode_boundary: AMBIGUOUS
  dependencies: UNKNOWN
  failure_witness: UNKNOWN
  available_branches: UNKNOWN
  adopted_side_claims: NOT APPLICABLE
  move_taken: M17 SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: UNKNOWN。
source_excerpts_used: E06 Excerpt 4
uncertainties:
  - 削除理由が packet にない。したがって「失敗による撤回」なのか「編集上の整理」なのかが決められない。M17 は削除という事実にのみ基づく。
  - obligation_type に taxonomy 主張の受け皿がない。
```

### E07

```text
parent_corpus_item: E07 — Metrology H1 to M1
subepisode_id: E07

episode_boundary: Source A §4（H1 と支持条件）→ Source B §3（audit が産出しなかったものの列挙）+ §14 Q5（判定を変えたか＝No）→ §14 Q7（最終分類 M1）。単一 transition。
alternative_segmentations: なし。before（H1）、witness（七項目の null リストと Q5）、after（M1 分類、M0 は defensible、M2/M3 は却下）が一つの前後関係を成す。分割すると同一 witness を重複計上することになる。

*** 重要な用語注意 ***
本 episode の M0 / M1 / M2 / M3 は source-local な value ladder ラベルであり、formation move code M1（assumption strengthening）等とは無関係である。以下で「M1 — Organizational value」と書くときは常に source-local ラベルを指す。formation code は move_taken 欄にのみ現れる。

claim_identity: B07 = H1
claim_before: H1 — Transfer-loss diagnostic. 「The relevant information exists in field-native documents, but a generic transfer audit finds at least one path in which upstream scope, uncertainty, assumptions, or reference information is lost or distorted in downstream use, and the field-native control does not find the same issue as clearly or as early.」
target_and_scope: target = generic transfer audit の診断的付加価値。scope = field-native control corpus と対比される metrology の transfer chain。quantifier strength = 存在主張（at least one path）＋比較主張（control より明確または早期に発見する）。required conclusion = 診断的 transfer-loss の存在と、field-native control に対する優位。
obligation_type: empirical claim ＋ comparative claim（preregistered hypothesis）。

assumptions: 関連情報は field-native documents に存在する（H1 の前置き）。frozen control corpus が比較対照として固定されている。
proof_or_evidence_resources: generic transfer audit の実施結果、field-native control corpus、cross-chain display。
evaluation_or_decision_rules:
  (i) 「H1 is supported only if at least one preregistered success condition in §6 survives all applicable falsification conditions in §5」＝ preregistered な支持条件。
  (ii) M0–M3 の value ladder と、「M2 and M3 are rejected by the preregistered criteria」という preregistered 判定規則。
  §5 の falsification conditions と §6 の success conditions の内容は packet にない（UNKNOWN）。規則の存在と適用結果のみ SOURCE-DERIVED。

failure_witness: audit が産出しなかったものの列挙（Source B §3）— a new missing assumption / a new uncertainty component / a different judgment about a calibration scope / a different conformity decision / a new traceability break / a source absent from the frozen control corpus / a remedy not already present in field-native practice。加えて Q5「Did the generic audit change a judgment? No. It changed presentation and cross-chain visibility only.」
available_branches:
  (i) M0（より厳しいラベル）— 「M0 remains a defensible stricter label」＝ 利用可能だが採られなかった。
  (ii) M2 / M3 — 「rejected by the preregistered criteria」＝ 明示的に却下された救済路。
adopted_side_claims: S07 = audit は compact cross-chain display を産出した（presentation と cross-chain visibility の改善）。これが M1 — Organizational value として保持される内容。

move_taken:
  M17 — demotion / negative-result fixation. H1 の診断的主張を取り下げ、「no demonstrated diagnostic or methodological added value」を最終判定として固定（Q7）。
  considered and NOT coded: M16。本ケースは excerpt 開始時点ですでに preregistered な対照比較として設計されており、この subepisode 内で定理／枠組み新規性の対象を経験的比較へ置換する transition は起きていない。M16 を当てると、excerpt 外で完了していた設計判断をこの episode の move として誤帰属することになる。
  considered and NOT coded: M15。七項目 null リスト（特に「a remedy not already present in field-native practice」）は field-native practice への吸収を示すが、instructions により prior-art / control 結果は通常 witness であって move ではない。ここでは witness に置いた。M15 を move とする読みも source-compatible であり AMBIGUOUS として記録する。
  considered and NOT coded: M2。診断的価値から組織的価値への移動は「結論の弱化」というより価値の種類の変更であり、M2 の除外規定（単なる言い換え／対象クラス変更のみには使わない）との境界が定まらない。AMBIGUOUS。
claim_after:
  A1: H1 — 診断的 transfer-loss の主張は支持されず、diagnostic / methodological added value は示されなかった。
  A2 [S07]: M1 — Organizational value（source-local ラベル）。presentation と cross-chain visibility のみの価値。
terminal_status:
  A1: not supported / negative result fixed（Q5 の No、Q7 の "no demonstrated diagnostic or methodological added value"）
  A2 [S07]: retained as M1（source-local ラベル）。ただし M0 がより厳しいラベルとして defensible のまま残る＝ 判定は下方向に開いている。

provenance_label:
  claim_before: SOURCE-DERIVED (Source A §4)
  episode_boundary: SOURCE-DERIVED
  dependencies: assumptions = SOURCE-DERIVED; proof_or_evidence_resources = SOURCE-DERIVED; evaluation_or_decision_rules = SOURCE-DERIVED（§5/§6 の内容は UNKNOWN）
  failure_witness: SOURCE-DERIVED (Source B §3, §14 Q5)
  available_branches: SOURCE-DERIVED (§14 Q7)
  adopted_side_claims: SOURCE-DERIVED (Source B §3 冒頭)
  move_taken: M17 SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: leakage は明示的に遮断されている（SOURCE-DERIVED）。Q5 が「presentation と cross-chain visibility のみを変えた」と述べ、表示改善が診断的価値として計上されることを防いでいる。M1 ラベルはその遮断後に残った分だけを名指す。
source_excerpts_used: E07 Excerpt 1, 2, 3, 4
uncertainties:
  - §5 falsification conditions と §6 success conditions の具体内容が packet にない。「preregistered criteria により M2/M3 却下」の検証はできない。
  - M0–M3 ladder の定義が packet にない。M1 が何を含意するかは source-local ラベルとしてしか扱えない。
  - M15 / M2 を move として coding すべきかが決まらない（上記）。
```

### E08

```text
parent_corpus_item: E08 — Hydrology “preservation” to documentary continuity
subepisode_id: E08

episode_boundary: Source A（v0.1 の Current verdict「B. Partial preservation history identified」と、A を選ばない理由 (i)–(iv)、および「保存機構は忘却を防いだが、解決も、下流への完全な伝達も保証していない」）→ Source B C-3（N-04 と内部矛盾、Codex の指摘は正当、当該表現を削除）→ v0.1/v0.2 対照表（B → 「Documentary continuity identified; preservation effectiveness untested」）+ 「確認できていないこと」。
alternative_segmentations: **AMBIGUOUS**。
  (S-i) 採用: 単一 transition。verdict 文の削除と verdict ラベルの改称を一つの改訂として扱う。
  (S-ii) 非採用だが両立可能: E08-a（「保存機構は忘却を防いだ」の削除、C-3 として記録）と E08-b（verdict ラベル B → 「Documentary continuity identified; preservation effectiveness untested」、対照表として記録）。二つは source 上、異なる表に記録されている。
  両者は同一 witness（N-04）を共有するため、独立した二結果として数えないこと。

claim_identity: B08
claim_before: v0.1 Current verdict「B. Partial preservation history identified」および同 verdict 文「保存機構は忘却を防いだが、解決も、下流への完全な伝達も保証していない」。
target_and_scope: target = 当該分野の負の知識に関する保存機構。scope = 単一事例の文書系列（17C→17B 参照、下流ガイダンス、36 年間の未解決問題を含む）。required conclusion = 部分的な保存の歴史が同定され、保存機構が忘却を防いだこと。
obligation_type: empirical claim（文書史に基づく事例判定）。

assumptions: 文書系列が保存機構の作動を示す証拠になりうること。
proof_or_evidence_resources: 源泉の label 付き所見群 — N-04（有効性を示す証拠は 17C→17B の一回の参照を除きほとんどない）、L-01（明示的退役と無言の消滅が同一文書内に併存）、L-02（下流ガイダンス一文書で不確かさ・非定常性の語が消える）、L-03（未解決問題が 36 年間未解決）。
  注: N-04 / L-01–L-03 は source-local label であり move code ではない。
evaluation_or_decision_rules: 内部整合性規則 —「N-04（有効性は未確認）と内部矛盾。Codex の指摘は正当」。すなわち、自文書の未確認所見と矛盾する verdict 表現は削除する。加えて「実際の参照・利用・下流伝達・忘却防止効果は、いずれも測定していない」という測定要件（未測定の量について効果を主張しない）。

failure_witness: verdict 文「保存機構は忘却を防いだ」と N-04（有効性未確認）との内部矛盾。外部レビュー（Codex）の指摘によって同定された。
available_branches: verdict A（「A を選ばない理由」として明示的に却下されている選択肢）。A の内容は packet に現れない（UNKNOWN）。B より強い保存主張であったと推測されるが、推測は行わない。
adopted_side_claims: S08 = 文書上の再発見可能性は残る（「文書上の再発見可能性は残ったが、それ以上は言えない」）。これが改称後の verdict「Documentary continuity identified」の実体。

move_taken:
  M2 — conclusion weakening. 「保存機構は忘却を防いだ」という有効性主張を削除し、verdict を「Partial preservation history identified」から「Documentary continuity identified; preservation effectiveness untested」へ弱める（C-3 と対照表）。
  M14 — disambiguation / type correction. 「文書上の連続性（documentary continuity）」と「保存の有効性（preservation effectiveness）」を別型として分離し、後者を未検証として明示する。
  M17 — withdrawal. 有効性主張文そのものの削除（「当該表現を削除（§Verdict）」）。
    注: M17 の除外規定（未検証の主張を反証済みと呼ぶことに使わない）に従い、A2 の status は refuted ではなく untested とした。
claim_after:
  A1: Documentary continuity identified（文書上の再発見可能性は残る）。
  A2: Preservation effectiveness untested — 実際の参照・利用・下流伝達・忘却防止効果はいずれも測定していない。
terminal_status:
  A1: retained（弱められた形で保持）
  A2: untested / open（未測定。反証ではない）

provenance_label:
  claim_before: SOURCE-DERIVED (Source A)
  episode_boundary: AMBIGUOUS（S-i / S-ii）
  dependencies: assumptions = INFERENCE; proof_or_evidence_resources = SOURCE-DERIVED; evaluation_or_decision_rules = SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED (Source B C-3)
  available_branches: SOURCE-DERIVED（存在のみ。内容は UNKNOWN）
  adopted_side_claims: SOURCE-DERIVED (Source B)
  move_taken: M2 SOURCE-DERIVED; M14 SOURCE-DERIVED; M17 SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: あり（SOURCE-DERIVED）。v0.1 は文書上の連続性という証拠から「忘却を防いだ」という有効性結論を取り出しており、名目上の target（保存機構の有効性）が、実際には文書の存在のみが支える結論を取り込んでいた。C-3 がこれを内部矛盾として摘出する。
source_excerpts_used: E08 Excerpt 1, 2, 3, 4, 5
uncertainties:
  - verdict A の内容が packet にない。available branch の内容が特定できない。
  - Excerpt 1 が見出し一行のみで、v0.1 verdict の本文全体が packet にない。
  - 「Codex」が人的レビューアか自動レビューかが packet から決まらない。witness を内部矛盾の自己発見とするか外部指摘とするかがこれに依存する。
  - 単一 transition か二 transition かが決まらない（上記）。
```

### E09-a

```text
parent_corpus_item: E09 — P0 to P1-reduced termination
subepisode_id: E09-a

episode_boundary: Source A §§5–6。before = 設計文書の計画（三分野の完全な artifact chain 復元 P1–P5）とその前提（比較すべきコードが十分にある）→ obstacle = 14 コード中 1 コードのみ生存 → move = (iii) 不採用の明記と (i) 縮小継続の採用 → after = 縮小継続。
alternative_segmentations: なし。Source B が「その計画の前提は二段階にわたって否定された」と明記しており、二段階を二 subepisode とする根拠が source 側にある。

*** 用語注意 *** NONEVAL / RET-DOWN / (i)–(iv) / 推奨・次点・非推奨・許容範囲 は source-local ラベルであり move code ではない。

claim_identity: B09a
claim_before: 設計文書 Part VIII の計画（P1–P5、三分野の完全な artifact chain 復元）を設計どおり実行する。前提: 比較すべきコードが十分にある。
target_and_scope: target = 比較研究プログラムの実行範囲。scope = 三分野、14 コード。required conclusion = 完全比較の実行が正当化されること。
obligation_type: design decision。

assumptions: 比較すべきコードが十分にあること（設計の前提として source が明示）。
proof_or_evidence_resources: P0 baseline の 14 コード検査結果。
evaluation_or_decision_rules:
  (i) 前提検査規則 —「P0 の結果はその計画の前提（比較すべきコードが十分にある）を否定した」。
  (ii) メタ規則 —「設計どおりに進めることが、設計の目的に反する場合がある」。
  (iii) 選択肢に付された source-local な優先ラベル（推奨 / 次点 / 非推奨 / 許容範囲）とコスト評価（小 / 中 / 大 / ゼロ）。

failure_witness: 「14 コード中、比較研究の対象として生き残るのは実質 1 コード（NONEVAL）、保留が 1 コード（RET-DOWN）である。」
available_branches:
  (ii) RET-DOWN の検査（L2+L3 を持つ generic 系列を 1 組取得）— 次点、採らず。
  (iv) 終了（comparative review へ降格して終了）— 許容範囲、この時点では採らず。
  (iii) 設計どおりの P1–P5 — 非推奨、明示的に却下（「(iii) を採らないことを明記する」）。
adopted_side_claims: NOT APPLICABLE（採用されたのは side claim ではなく選択肢 (i) という design decision）。

move_taken:
  M17 — abandonment. (iii) 設計どおりの P1–P5 を採らないことを明記（Excerpt 3）。
  M4 — object / corpus restriction. 比較対象を 14 コードから NONEVAL 1 コードへ、検索対象を GUM/VIM と GRADE handbook へ限定（Excerpt 2 の (i)）。
  considered and NOT coded: M16。(i) は文献検索であり、定理／枠組み新規性の対象を対照比較・文書監査・有限試験へ置換する transition ではない（本プログラムは元から比較研究である）。
claim_after:
  A1: (iii) 設計どおりの P1–P5 は採らない。
  A2: (i) 縮小継続 — NONEVAL のみを対象に GUM/VIM と GRADE handbook を検索し、「評価していない」に相当する定型表現の有無を見る。
terminal_status:
  A1: terminated / not taken（source 表記「(iii) を採らないことを明記する」「非推奨」）
  A2: adopted（source 表記「推奨」）

provenance_label:
  claim_before: SOURCE-DERIVED (Excerpt 2 の (iii) 行, Excerpt 3)
  episode_boundary: SOURCE-DERIVED（Source B の「二段階にわたって」）
  dependencies: assumptions = SOURCE-DERIVED; proof_or_evidence_resources = SOURCE-DERIVED; evaluation_or_decision_rules = SOURCE-DERIVED
  failure_witness: SOURCE-DERIVED (Excerpt 1)
  available_branches: SOURCE-DERIVED (Excerpt 2)
  adopted_side_claims: NOT APPLICABLE
  move_taken: M17 SOURCE-DERIVED; M4 SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: 明示的に遮断されている（SOURCE-DERIVED）。「設計どおりに進めることが、設計の目的に反する場合がある」は、設計の実行そのものが成果として計上される形の leakage を拒否する。
source_excerpts_used: E09 Excerpt 1, 2, 3
uncertainties:
  - 14 コードの内容、NONEVAL / RET-DOWN の定義、L2/L3 の意味が packet にない。
  - 「実質 1 コード」の判定基準（何をもって「生き残る」とするか）が packet にない。
```

### E09-b

```text
parent_corpus_item: E09 — P0 to P1-reduced termination
subepisode_id: E09-b

episode_boundary: Source B §§6, 9。before = E09-a で採用された縮小継続（比較方法論としての存続）→ obstacle = P1-reduced 検査の結果 → move = 比較方法論としての終了と comparative review への降格 → after = D 相当の終了判定。
alternative_segmentations: なし（E09-a 欄参照）。

claim_identity: B09b
claim_before: NONEVAL に対象を絞れば、比較方法論としてのプログラムが成立する（E09-a の A2 を継続した状態）。
target_and_scope: target = 比較方法論としてのプログラムの存続。scope = NONEVAL 1 コード、二分野（GUM/VIM と GRADE handbook）。
obligation_type: design decision（継続／終了の判定）。

assumptions: 縮小後も比較方法論として成立するだけの対象が残ること。
proof_or_evidence_resources: P1-reduced two-field check の実施結果。検査内容そのものは packet にない（UNKNOWN）。
evaluation_or_decision_rules:
  (i) 「設計文書 Part IX の規定に従う」＝ 事前規定された停止規則。Part IX の内容は packet にない（UNKNOWN）。
  (ii) 「D 相当」という source-local な終了判定ラベル（定義は packet にない）。
  (iii) E09-a と共通の前提検査規則（計画の前提が否定されたか）。

failure_witness: 「P0 と本検査により、その計画の前提は二段階にわたって否定された」。本検査で何が観察されたかの具体的内容は packet にない（UNKNOWN）。
available_branches: UNKNOWN。この段階で提示され採られなかった路は excerpt に現れない（E09-a の (ii) RET-DOWN 検査が依然利用可能かどうかも不明）。
adopted_side_claims: S09 = comparative review としての継続（「downgrade to comparative review」）。比較方法論の終了後に残る活動形態。

move_taken:
  M17 — termination / demotion. 「terminate as comparative methodology; downgrade to comparative review」「比較方法論としては終了する」（Excerpt 4, 5）。
  considered and NOT coded（AMBIGUOUS）: M15。「downgrade to comparative review」は、M15 の定義にある「既存の review language へ戻す」とも読める。単なる降格（M17）か既存様式への吸収（M15）かを source は決めていない。
claim_after:
  A1: 比較方法論としてのプログラムは終了（D 相当）。
  A2 [S09]: comparative review へ降格して継続。
  A3: 設計文書 Part VIII の P1–P5（三分野の完全な artifact chain 復元）には進まない。
terminal_status:
  A1: terminated（source 表記 "terminate as comparative methodology"、「D 相当」）
  A2 [S09]: retained as downgraded form（comparative review）
  A3: terminated / not taken（前提が二段階で否定されたため）

provenance_label:
  claim_before: INFERENCE（E09-a の A2 の継続状態として再構成）
  episode_boundary: SOURCE-DERIVED
  dependencies: assumptions = INFERENCE; proof_or_evidence_resources = UNKNOWN; evaluation_or_decision_rules = SOURCE-DERIVED（内容は UNKNOWN）
  failure_witness: SOURCE-DERIVED（内容は UNKNOWN）
  available_branches: UNKNOWN
  adopted_side_claims: SOURCE-DERIVED (Excerpt 4)
  move_taken: M17 SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: UNKNOWN。excerpt に退化・leakage の指摘はない。
source_excerpts_used: E09 Excerpt 4, 5, 6
uncertainties:
  - P1-reduced 検査の観察内容が packet にない。witness を「検査結果」としか書けない。
  - 「D 相当」および Part IX の規定内容が packet にない。停止規則が事前規定であることは書かれているが、その中身は検証できない。
  - E09-a の available branch (iv)（終了）と E09-b の A1（終了）が同一の路かどうかを source が明示しない。submission block には subepisode 間の branch 追跡欄がない（§4.6, §4.7）。
```

### E10

```text
parent_corpus_item: E10 — Gödel “closure reversal” to C1
subepisode_id: E10

episode_boundary: §0（閉包語彙は比較のためのメタ記述であって標準用語ではない、という枠組み宣言）+ §1（第1定理の標準的言明）+ §7–8（第2定理の型、C1 判定、negative result の言明）。before = 「閉包反転」が Gödel を扱える独立した分類枠として働く、witness = 独立分類を与えず診断解像度が標準概念より低い、after = C1（説明比喩としてのみ有効）。
alternative_segmentations: 考慮したが採用せず — Excerpt 3（第2定理は外部の整合性仮定から内部文の非証明可能性を導くメタ定理である）を独立 subepisode とする案。これは Gödel の定理の型の記述であって、本稿の主張に対する before/failure/move/after を構成しないため、resource として同一ブロックに置いた。

*** 用語注意 *** C1 / C2 / C3 は source-local な評価ラダーのラベルであり move code ではない。「逃走経路」「閉じ方」「封鎖」「残差」「閉包」「閉包反転」も source が自ら「標準数理論理学・証明論の用語ではない」と宣言する比較用メタ記述である。

claim_identity: B10
claim_before: 「閉包反転」は Gödel の第1・第2不完全性定理を扱える分類枠として働き、C2・C3 に相当する地位（証明論的に独立した新分類）を主張しうる。
target_and_scope: target = 閉包語彙（特に「閉包反転」）の分類的地位。scope = 既存 21 定理との比較の中での Gödel 第1・第2定理。required conclusion = 証明論的に独立した新分類を与えること。
obligation_type: literature/novelty claim ＋ comparative claim（分析枠の適用可能性の主張）。

assumptions: 閉包語彙は比較のためのメタ記述であり、標準数理論理学・証明論の用語ではない（§0 の自己制限）。分析対象 T は Robinson arithmetic Q を含む計算可能公理化された古典一階理論。
proof_or_evidence_resources:
  (i) 第1不完全性定理の標準的言明（T が整合的なら T⊬R_T かつ T⊬¬R_T なる算術文 R_T が存在する）。
  (ii) 第2定理の型に関する記述（外部の整合性仮定から内部文の非証明可能性を導くメタ定理である）。
  (iii) 既存 21 定理との比較。
evaluation_or_decision_rules: C1/C2/C3 ラダーの昇格基準 —「証明論的に独立した新分類を与えず、標準概念より診断解像度が低い。従って C2・C3 へは上げない」。ラダーの正式な定義は packet にない（UNKNOWN）。

failure_witness: 「閉包反転」は証明論的に独立した新分類を与えず、標準概念より診断解像度が低い（§7–8）。加えて「閉包語彙は Gödel の機構を発見・区別する道具にはならず、標準的分析後の比較要約にのみ使える」。
available_branches: C2 / C3 への昇格 — source が明示的に検討し却下した路（「従って C2・C3 へは上げない」）。
adopted_side_claims: S10 = C1 — 説明比喩としてのみ有効。「条件が positive closure を作る場合と、条件が effective closure の限界を可視化する場合を対照させる短いラベル」としては働く。

move_taken:
  M15 — prior-art absorption. 閉包語彙を標準概念へ戻す（「標準概念より診断解像度が低い」「標準的分析後の比較要約にのみ使える」）。M15 の注記どおり、残余価値（C1 の比較ラベルとしての有効性）は消えていない。
  M17 — demotion / negative-result fixation. C2・C3 への昇格を否定し、C1 に固定。「negative result として重要なのは…と分かったこと」として否定的結論を確定させる（§8）。
  M14 — disambiguation / type correction. 「Gödel の機構を発見・区別する道具」と「標準的分析後の比較要約」を型として分離（§8）。§0 の「比較のためのメタ記述であって標準用語ではない」宣言も同型の区別。
  considered and NOT coded: M12。Excerpt 3（第2定理＝外部の整合性仮定から内部文の非証明可能性を導くメタ定理）は Gödel の定理自体のメタレベル構造の記述であり、本稿が自分の主張に対して行った操作ではない。instructions の「完成した証明の型は、義務を閉じられるようにした操作とは限らない」に従い coding しない。
  considered and NOT coded: M16。C1 判定は対照比較・文書監査・有限試験への置換ではない。
claim_after:
  A1: B10 — 「閉包反転」は証明論的に独立した新分類を与えない。C2・C3 へは上げない。
  A2 [S10]: C1 — 説明比喩としてのみ有効。既存 21 定理との比較において、positive closure を作る条件と effective closure の限界を可視化する条件を対照させる短いラベルとしては働く。
  A3: negative result — 閉包語彙は Gödel の機構を発見・区別する道具にはならず、標準的分析後の比較要約にのみ使える。
terminal_status:
  A1: demoted / not raised（source: 「C2・C3 へは上げない」）
  A2 [S10]: retained as explanatory metaphor（C1）
  A3: negative result fixed（source が明示的に negative result と呼ぶ）

provenance_label:
  claim_before: INFERENCE — before 形は「C1 へ下げる」という判定から逆算した。原文で before として明示されているのは「分析枠の試験適用」までである。
  episode_boundary: SOURCE-DERIVED
  dependencies: assumptions = SOURCE-DERIVED; proof_or_evidence_resources = SOURCE-DERIVED; evaluation_or_decision_rules = SOURCE-DERIVED（ラダー定義は UNKNOWN）
  failure_witness: SOURCE-DERIVED (§7–8)
  available_branches: SOURCE-DERIVED (§7)
  adopted_side_claims: SOURCE-DERIVED (§7)
  move_taken: M15 SOURCE-DERIVED; M17 SOURCE-DERIVED; M14 SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: leakage が明示的に遮断されている（SOURCE-DERIVED）。「Gödel が『閉包反転』の実例だと証明されたのではなく」— 枠組みラベルが Gödel の定理の成果を実例として取り込むことを source 自身が拒否している。§0 の用語宣言も同じ遮断として働く。
source_excerpts_used: E10 Excerpt 1, 2, 3, 4, 5
uncertainties:
  - C1/C2/C3 ラダーの定義が packet にない。
  - 「既存21定理」の内容が packet にない。比較の実体が検証できない。
  - claim_before の原文形が packet にない（判定からの逆算）。
```

### E11

```text
parent_corpus_item: E11 — Reflection S2 to S2*
subepisode_id: E11

episode_boundary: §0（中心仮説と kill test 宣言）→ §§2–3（Γ は scope definition である／T+ 構成と strength の scope 依存）+ §11（Löb と subject shift）→ §21（S2* 判定）。単一 transition。
alternative_segmentations: 考慮したが採用せず — §2（Γ は T の性質ではなく scope definition）と §11（subject shift）をそれぞれ独立 subepisode とする案。いずれも独自の before/after を持たず、S2 → S2* の witness / resource として働くため同一ブロックに置いた。

*** 用語注意 *** S1 / S2 / S2* は source-local な評価ラベルであり move code ではない。

claim_identity: B11
claim_before: S2 —「自己保証」は比較ラベルとして働く。中心仮説はこれに対する疑い:「『自己保証』が single local reflection では比較ラベルとして働いても、uniform / global reflection や semantic soundness まで含めると型とレベルの差を隠すのではないか」。source は「S2 を維持するのでなく、積極的に kill test する」と宣言する。
target_and_scope: target =「自己保証」という比較ラベルの適用範囲。scope = local reflection / uniform reflection / global reflection / semantic soundness を含む reflection principle 全域。required conclusion = ラベルが当該範囲全体で有効であること。
obligation_type: comparative claim（比較ラベルの妥当範囲の主張）。

assumptions: reflection principle は外部から T へ追加され、T+ = T + Rfn_Γ(T)、T + RFN_Γ(T)、T + GRP(T) のような stronger theory を構成する。formula class Γ は T の「性質」ではなく、どの reflection instances を追加するかという scope definition である。
proof_or_evidence_resources:
  (i) T+ 構成（T-provability から対象文・全数 instance・truth への橋を新しい axioms として与える）。
  (ii) 得られる strength、conservation、consistency strength が scope、Γ、base、truth axioms に依存し「単一の結論 P には還元できない」という観察。
  (iii) Löb の定理の適用範囲に関する記述（Löb は reflection principle の追加を禁止せず、「同じ T が自分に関する reflection を theorem にする」場合の collapse を述べる）。
evaluation_or_decision_rules: 「S2 を維持するのでなく、積極的に kill test する」＝ 維持ではなく反証を試みる評価方針。S1 / S2 / S2* ラダーの定義は packet にない（UNKNOWN）。
  注: kill test はここでは評価方針であって move ではない。

failure_witness: uniform / global reflection や semantic soundness まで広げると、ラベルが型・言語・メタレベルの差を隠して破綻する（§21）。具体的には (a) strength 等が scope/Γ/base/truth axioms に依存し単一結論に還元できない、(b) reflection theory は外部から旧理論 T を対象化して stronger theory を作るという subject shift を含み、「この subject shift がなければ progression 全体を誤読する」。
available_branches: UNKNOWN。S2 を維持するための救済路は excerpt に明示されない（§0 は維持しない方針を宣言するのみ）。
adopted_side_claims: S11 = S2*（限定的 S2）。local reflection では有効。

move_taken:
  M14 — disambiguation / type correction. local reflection と uniform / global reflection / semantic soundness を分離する（M14 の "local from uniform/global" に直接該当）。さらに object theory T と、それを外部から対象化する reflection theory との subject shift の分離、および provability と truth の橋渡しが新公理として与えられるという型の区別（§§3, 11, 21）。
  M2 — conclusion weakening. 「自己保証は比較ラベルとして働く」を、local reflection の範囲に限って有効という形へ弱める（S2 → S2*、§21）。
  considered and NOT coded（AMBIGUOUS）: M3。有効範囲を single local reflection に限ることは、どの reflection instances（＝どの formula class Γ の instance）を認めるかの制限とも読め、§2 は Γ を scope definition と明言する。M3（formula-class / language restriction）と M14 のどちらで扱うべきかを source は決めていない。
  considered and NOT coded: M6。T+ = T + Rfn_Γ(T) は分析対象である reflection theory 側の構成であって、本稿が自分の主張に対して行った操作ではない。resource に置いた。
  considered and NOT coded: M12。subject shift の記述はメタレベル構造の指摘だが、これも分析対象の構造であり、本稿の主張に対する評価の移動として cite できる before/after がない。
claim_after:
  A1 [S11]: S2* — 限定的 S2。local reflection では有効だが、uniform / global / soundness まで広げると型・言語・メタレベルの差を隠して破綻する。
terminal_status:
  A1 [S11]: demoted to limited form（S2 → S2*）。kill test は S2 を全面的に殺したのではなく、適用範囲を local に限定した形で残した。

provenance_label:
  claim_before: SOURCE-DERIVED (§0)
  episode_boundary: SOURCE-DERIVED
  dependencies: assumptions = SOURCE-DERIVED; proof_or_evidence_resources = SOURCE-DERIVED; evaluation_or_decision_rules = SOURCE-DERIVED（ラダー定義は UNKNOWN）
  failure_witness: SOURCE-DERIVED (§§3, 11, 21)
  available_branches: UNKNOWN
  adopted_side_claims: SOURCE-DERIVED (§21)
  move_taken: M14 SOURCE-DERIVED; M2 SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: target leakage あり（SOURCE-DERIVED）。「自己保証」ラベルが、local reflection で成り立つ事柄の説明力を uniform / global / soundness の範囲まで持ち越し、「型とレベルの差を隠す」。S2* はその持ち越しを止める判定である。
source_excerpts_used: E11 Excerpt 1, 2, 3, 4, 5
uncertainties:
  - S1 / S2 / S2* ラダーの定義が packet にない。「限定的 S2」が何を含意するかは source-local ラベルとしてしか扱えない。
  - S2 の元の主張文（何がどこまで「自己保証」と呼ばれていたか）の原文が packet にない。
  - M3 を coding すべきかどうかが決まらない（上記）。
  - E11 の S2* と E12 の S2* が同一ラダー上の同一ラベルかどうかは、両 excerpt からは決められない（同一文書系列であることは path から推測できるが、推測は行わない）。
```

### E12-a

```text
parent_corpus_item: E12 — Proof-theoretic ordinal scalar to fixed-package calibration
subepisode_id: E12-a

episode_boundary: opening（中心結論）+ §§16–17（|T|=|U| から何が従わないか）→ §18（判定 S2*）。S 軸（万能スカラー性）の transition。
alternative_segmentations: なし。E12 は二つの独立した判定ブロック（S2* と A2）を含み、対象となる主張が異なるため E12-a / E12-b へ分けた。両者は同一の witness を共有しない。

*** 用語注意 *** S1 / S2 / S2* / A2 / A3 は source-local な評価ラベルであり move code ではない。特に source の「判定: A2」は、本 submission block の after-claim ラベル A2 とは無関係である（§4.7 参照）。

claim_identity: B12a
claim_before: proof-theoretic ordinal は理論の全 strength を表す万能スカラーである（「|T|=α」が理論の強さを表す完全な指標として読める）。
target_and_scope: target = proof-theoretic ordinal の指標としての射程。scope = 任意の理論、任意の formula class、任意の interpretability / conservation notion。required conclusion = 単一のスカラーが理論の全 strength を表すこと。
obligation_type: formal theorem に関する comparative claim（calibration 指標の射程主張）。

assumptions: 「|T|=α」は、少なくとも notation、base/metatheory、formula class、reduction notion を省略した略記である（source が明示する suppressed parameters）。
proof_or_evidence_resources: 自然な理論群と標準 analysis package において、cut elimination、TI/WO、reflection、worm ordering が橋渡し定理により同じ ordinal へ収束するという事実（§18）。PA のような収束例。
evaluation_or_decision_rules: S1 / S2 / S2* ラダー —「単独の characterization 内だけなら S1、PA のような収束例まで含めて限定的 S2 と評価する」。ラダーの定義自体は packet にない（UNKNOWN）。

failure_witness: |T|=|U| から、一般には same theorem set / mutual interpretability / same consistency strength / same Π1-consequences / same induction schemas / same reflection rank のいずれも自動では従わない。従うのは「採用した ordinal calibration が T,U を同じ座標へ写した」ことだけである（§17）。
available_branches: 「追加結論には、その calibration と theorem inclusion、conservation、interpretability 等を結ぶ定理が要る」＝ 橋渡し定理を証明する路。source は要件として明示するが、一般の場合については実行していない。
adopted_side_claims: S12a = proof-theoretic ordinal は、比較方法を固定した自然な理論群に対しては強力でしばしば頑健な一次元 calibration である。

move_taken:
  M14 — disambiguation / type correction. 「同じ座標へ写された」ことと、theorem set / interpretability / consistency strength / Π1-consequences / induction schemas / reflection rank の一致とを型として分離する（§17）。「|T|=α」の略記が隠していた notation / base/metatheory / formula class / reduction notion を明示化することも同型の訂正（opening）。
  M2 — conclusion weakening. 「理論の全 strength を表す万能スカラー」から「比較方法を固定した自然な理論群に対する頑健な一次元 calibration」へ、結論の一般性を弱める（opening, §18）。
  M4 — object / model-class restriction. 対象を「自然な理論群」へ限定する（任意の理論ではない）（opening, §18）。
  M3 — formula-class restriction. 「任意の formula class を一つにする universal scalar ではない」とし、固定された formula class の下でのみ主張を保持する（§18）。M3/M4 の区別: M4 は理論群という対象クラスの制限、M3 は formula class という論理式クラスの制限であり、source は両者を別々に明示している。
  M1 — assumption strengthening. notation、base/metatheory、reduction notion を明示条件として主張へ組み込む（opening、§18 の「標準 analysis package」）。
  considered and NOT coded: M13。本 episode は既にある ordinal calibration の射程を制限しており、問題を conservativity / interpretability / reflection rank へ「移す」move ではない。橋渡し定理の要求は available_branches に置いた。なお M13 の除外規定（共有 ordinal から強さの万能スカラーや理論の同一性を推論しない）は、本 episode の内容と同型の注意である。
claim_after:
  A1: proof-theoretic ordinal は、任意の理論・任意の formula class・任意の interpretability/conservation notion を一つにする universal scalar ではない。
  A2 [S12a]: 比較方法を固定した自然な理論群と標準 analysis package に対しては、cut elimination / TI/WO / reflection / worm ordering が橋渡し定理により同じ ordinal へ収束し、ordinal は複数の標準 notions を統合する頑健な一次元 coordinate になる。判定 S2*（単独の characterization 内なら S1）。
terminal_status:
  A1: withdrawn（万能スカラー主張）
  A2 [S12a]: retained in restricted form — source-local ラベル S2*（限定的 S2）。単独 characterization 内では S1。

provenance_label:
  claim_before: INFERENCE — before 形（万能スカラー主張）は「万能スカラーではない」という否定文から逆算した。原文で誰がその主張を保持していたかは packet にない。
  episode_boundary: SOURCE-DERIVED
  dependencies: assumptions = SOURCE-DERIVED; proof_or_evidence_resources = SOURCE-DERIVED; evaluation_or_decision_rules = SOURCE-DERIVED（ラダー定義は UNKNOWN）
  failure_witness: SOURCE-DERIVED (§17)
  available_branches: SOURCE-DERIVED (§17)
  adopted_side_claims: SOURCE-DERIVED (opening, §18)
  move_taken: M14 SOURCE-DERIVED; M2 SOURCE-DERIVED; M4 SOURCE-DERIVED; M3 SOURCE-DERIVED; M1 SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: target leakage あり（SOURCE-DERIVED）。「|T|=α」という略記が notation / base/metatheory / formula class / reduction notion を省略しているため、座標の一致が strength の一致として読まれてしまう。§17 の否定リストがこの leakage を遮断する。
source_excerpts_used: E12 Excerpt 1, 2, 3
uncertainties:
  - claim_before の保持者・原文が packet にない（否定文からの逆算）。
  - S1 / S2 / S2* ラダーの定義が packet にない。
  - M1 / M3 / M4 を分けて coding したが、source は「比較方法を固定した」という一語でまとめており、五つの move code へ分解したのは reader の再構成である（各 code は個別の cite を持つが、分解の粒度自体は instructions に決め方が書かれていない）。
```

### E12-b

```text
parent_corpus_item: E12 — Proof-theoretic ordinal scalar to fixed-package calibration
subepisode_id: E12-b

episode_boundary: §25 の判定ブロック（判定: A2）単独。A 軸（architecture / 型区別）の transition。
alternative_segmentations: なし（E12-a 欄参照）。

claim_identity: B12b
claim_before: UNKNOWN / AMBIGUOUS。A 軸の before 形は packet にない。判定文から再構成できるのは「ordinal analysis に現れる型の差は、A3 に相当する固有の architecture 現象として扱うべきか」という問いのみ。A0–A3 ラダーの定義は packet にない。
target_and_scope: target = ordinal analysis における型・レベル構造の地位。scope = analyzed theory T、その proof を符号化する calculus、ordinal notation、reduction theorem、notation の well-foundedness を証明する metatheory。
obligation_type: AMBIGUOUS。interpretation（構造の型分析）と comparative claim（Turing–Feferman progression との対比、および A3 への昇格可否）の両方の性格を持つ。

assumptions: ordinal analysis が上記五つの構成要素を含むこと。
proof_or_evidence_resources: Turing–Feferman progression の subject/extension reindexing との対比。標準 metamathematical level distinction。
evaluation_or_decision_rules: 「標準 metamathematical level distinction で十分なので A3 ではない」＝ 標準的区別で説明できるものは上位ラベルへ上げないという判定規則。A ラダーの定義は packet にない（UNKNOWN）。

failure_witness: A3 相当の固有性を否定する witness は「標準 metamathematical level distinction で十分」であること。これは反例や prior-art 結果というより、既存概念による十分な被覆の確認である。
available_branches: A3 への昇格（明示的に却下）。Turing–Feferman progression の subject/extension reindexing と同一視する路（「同一ではない」として明示的に否定）。
adopted_side_claims: S12b = 「評価される理論」と「評価を正当化する理論」の区別は、ordinal-analysis 全般に安定する architecture feature である。

move_taken:
  M14 — disambiguation / type correction. analyzed theory T / proof を符号化する calculus / ordinal notation / reduction theorem / well-foundedness を証明する metatheory が「型が異なる」ことの分離、および「評価される理論」と「評価を正当化する理論」の区別（§25）。
  M15 — prior-art absorption. 当該 architecture feature を標準 metamathematical level distinction へ戻す（「標準 metamathematical level distinction で十分なので A3 ではない」）。M15 の注記どおり、残余（安定した architecture feature としての記述価値）は消えていない。
  considered and NOT coded（AMBIGUOUS）: M12。well-foundedness の証明を metatheory へ置くことはメタレベルでの評価だが、これは ordinal analysis の標準的構造の記述であって、本稿が自分の主張に対して行った操作ではない。M12 として coding する読みも source-compatible だが、instructions の「完成した証明の型は、義務を閉じられるようにした操作とは限らない」に従い coding しない。
claim_after:
  A1: 判定 A2（source-local ラベル）。当該型区別は A3 ではない。標準 metamathematical level distinction で十分。
  A2 [S12b]: 「評価される理論」と「評価を正当化する理論」の区別は ordinal-analysis 全般に安定する architecture feature である。Turing–Feferman progression の subject/extension reindexing とは同一ではない。
terminal_status:
  A1: not raised / classified as A2（source-local）
  A2 [S12b]: retained as architecture feature（標準的区別の範囲内で保持）

provenance_label:
  claim_before: UNKNOWN / AMBIGUOUS（A ラダーが packet にないため before を確定できない）
  episode_boundary: SOURCE-DERIVED（§25 が独立した判定ブロックであること）
  dependencies: assumptions = SOURCE-DERIVED; proof_or_evidence_resources = SOURCE-DERIVED; evaluation_or_decision_rules = SOURCE-DERIVED（ラダー定義は UNKNOWN）
  failure_witness: SOURCE-DERIVED（ただし「失敗」ではなく既存概念による被覆確認）
  available_branches: SOURCE-DERIVED (§25)
  adopted_side_claims: SOURCE-DERIVED (§25)
  move_taken: M14 SOURCE-DERIVED; M15 SOURCE-DERIVED
  claim_after_and_status: SOURCE-DERIVED

degenerate_or_target_leakage: leakage が遮断されている（SOURCE-DERIVED）。A3 という上位ラベルへ上げないことで、標準的なメタ数学的レベル区別が新しい architecture 発見として計上されることを防いでいる。
source_excerpts_used: E12 Excerpt 4
uncertainties:
  - claim_before が確定できない。A0–A3 ラダーの定義が packet にない。
  - この判定が「失敗による格下げ」なのか「最初から A2 と評価された」のかが packet からは決められない。before/after の transition として coding したが、単なる分類記録である可能性も残る。
  - M12 を coding すべきかどうかが決まらない。
```

---

## 3. Independent reader record

以下は Reader 02 の作業記録であり、adjudication でも framework 改訂提案でもない。

### 3.1 最も coding しやすかった episode

**E07（Metrology H1 → M1）。**

submission block が要求する欄が、ほぼすべて source 側に既に分離された形で存在していた。

- claim_before が preregistered hypothesis として一文で書かれている（H1 の全文）。
- 判定規則が claim と別に、明示的に preregistered なものとして書かれている（「H1 is supported only if at least one preregistered success condition in §6 survives all applicable falsification conditions in §5」）。
- witness が「産出しなかったもの」の閉じた七項目リストとして列挙されており、reader が一般的批判で代用する余地がない。
- available branch（M0 は defensible なまま／M2・M3 は却下）と adopted side claim（compact cross-chain display ＝ organizational value）が source 側で既に分かれている。
- 表示改善を診断的価値として数えない、という leakage 遮断が Q5 で明示されている。

次点は **E03** と **E01**。どちらも「当初の仮説／何によって壊れたか／撤回したもの／残ったもの」という四部構成が Step 1–4 の欄割りとほぼ一対一に対応した。作業中の主観として、この四部構成を持つ working note 系 episode（E01–E04）は、判定ラベルのみを提示する stress test 系 episode（E10–E12）より欄埋めが速かった。

### 3.2 最も曖昧だった episode

**E06（GST Deferred Resolution）。** 理由は四つ。

1. Source path A（`deferred_resolution_case_01_gst.md`）に版表記がなく、Excerpt 1 が改訂前の判定なのか改訂後も残る判定なのかが packet から決まらない。claim_before の同定がこれに依存する。
2. Excerpt 2 が diff の一行（`| Final status | working positive case | frozen negative baseline | frozen |`）のみで、何がその status 変更を引き起こしたかの本文がない。
3. DR-1 — Weak relocation、Null C（Solved by quotient）、Null D/E（historical sequencing / reviewer-imposed narrative）の定義が packet にない。評価規則の「存在」しか記録できず、「内容」は UNKNOWN のまま残った。
4. Excerpt 4 の三項目（ケース判定の撤回／機構名の降格／taxonomy の削除）が、一つの改訂か三つの transition かを source が決めていない。特に taxonomy 削除（E06-c）は、理由が一切書かれていないため、失敗による撤回か編集上の整理かを判定できなかった。

次点は **E12-b**。A0–A3 ラダーが packet になく、claim_before を UNKNOWN のままにせざるを得なかった。判定 A2 が「格下げの結果」なのか「最初からの分類記録」なのかも決められない。

### 3.3 複数 segmentation が残った episode

以下の五件で `alternative_segmentations` を残し、境界を AMBIGUOUS とした。いずれも、重複するテキストを二つの独立結果として数えてはならない。

| item | 採用した segmentation | 両立する代替 | 分岐点 |
|---|---|---|---|
| E02 | E02-a（一般含意の撤回）/ E02-b（条件付き容量命題） | 単一 episode、条件付き命題を A3 とする | Excerpt 4 冒頭の「残る」を、Excerpt 3 の「残ったもの」の続きと読むか、独自 assumption 集合を持つ別 transition と読むか |
| E04 | 単一 episode（A1 撤回 / A2 量化順序差 / A3 synthesis） | E04-a（二ビット構成による量化順序差の確立）/ E04-b（内部性解釈の撤回） | 二ビット構成が「仮説を支持する結果」でもあり「撤回対象の使用法」でもあるため |
| E05 | E05-a（一般同値の撤回＋二つの置換）/ E05-b（inside vs outside の撤回） | E05-a を a1（規約的同値）/ a2（条件付き補題）へさらに分割 | 二つの置換が obligation_type も move も異なるが、一つの撤回・一つの witness を共有する |
| E06 | E06-a / E06-b / E06-c | 単一の改訂 episode（A1–A4） | Excerpt 4 の三項目が一つの変更リストに並んでいる |
| E08 | 単一 episode（A1 continuity / A2 untested） | E08-a（verdict 文の削除、C-3）/ E08-b（verdict ラベルの改称、対照表） | 二つの変更が source 上は別の表に記録されているが、witness（N-04）は共通 |

E09 は二 subepisode としたが、これは代替ではない。source が「その計画の前提は二段階にわたって否定された」と明記しているため、二段階への分割は source-derived である。

### 3.4 M1–M17 で表現しにくかった transition

いずれも新コードは作らず、既存コードでの近似と、その近似が落としたものを記録するにとどめた。

1. **分類体系そのものの削除**（E06-c: 五段階 taxonomy の削除）。M17 は「主張の撤回・格下げ・終了・否定的結論の凍結」を扱うが、削除されたのは主張ではなく分類装置である。M17 で近似したが、撤回理由が書かれていないため、失敗による撤回なのか編集判断なのかも区別できない。
2. **語彙・名称の格下げ**（E06-b: 独立機構名 → 棄却済み historical working hypothesis）。M17（demotion）と M15（既存語彙への吸収）の両方が部分的に当たり、どちらか一方では transition の全体を表せない。両方を coding したが、これは「二つの操作が起きた」のか「一つの操作を二つのコードで近似した」のかを区別できていない。
3. **判定ラベルの改称**（E08: 「B. Partial preservation history identified」→「Documentary continuity identified; preservation effectiveness untested」）。改称そのものに対応するコードがない。M2（結論の弱化）＋ M14（型の分離）で近似した。
4. **自らの設計文書に従わないという決定**（E09-a: 「(iii) を採らないことを明記する」）。design decision の放棄は M17 で近似できるが、M17 の語彙（withdraw / demote / terminate / freeze）は主張に対する操作を前提としており、計画に対する操作としては座りが悪い。
5. **主張が定義的規約へ転位すること**（E05-a の A2）。source は結果を「同値定理というより、行動的インターフェースの同一性をどう定義したかの帰結」と位置づける。M1（条件の指定）で近似したが、「主張が分析的になった」という transition 自体を表すコードはない。
6. **失効条件の明示的な列挙**（E02-b: この議論が使えなくなる四条件の公表）。条件を assumptions として記録できるが、「反例条件を自分で列挙して主張の射程を確定する」という操作に対応するコードがない。
7. **複数軸への同時制限**（E12-a: 「比較方法を固定した自然な理論群」）。source は一語でまとめているが、coding 上は M1（notation / base / reduction notion）、M3（formula class）、M4（理論群）へ分解する必要があった。分解の粒度を決める規則が instructions にない。
8. **kill test を宣言して部分的に生き残らせること**（E11: S2 → S2*）。M2（結論の弱化）で近似したが、「反証を試みた結果、範囲を限定して残った」という過程は status 側にしか記録できない。

### 3.5 assumption / proof-or-evidence-resource / evaluation-rule の境界問題

instructions は三者を分けよと指示するが、次の箇所では source が役割を決めていない。

1. **E03**「情報損失は…具体的なチャネル、統計量、力学、同値関係について証明しなければならない」は、[ESTABLISHED] タグ付きの retained claim であり、同時に「何をもって情報損失の主張を認めるか」の判定規則でもある。重複記載禁止に従い adopted_side_claims に実体を置き、evaluation 欄には役割重複のみ記した。この処理は instructions からは一意に導けない。
2. **E02-b** の四つの失効条件（候補の部分集合への制限／環境自由度の記憶利用／外部ログ／無限集合での濃度差消失）は、admissible cases を画定する点で assumptions だが、救済路として読めば available_branches である。assumptions に置いたが決定的な根拠はない。
3. **E05-a** の完全な実現可能インターフェース I（timing、concurrency、memory accessibility/vulnerability、cost、self-readout、stochasticity、causal channels、reset/copy/fresh preparation、adversarial access）は、主張の条件（assumption）であると同時に、「何を『同じインターフェース』と呼ぶか」を決める規約＝判定規則でもある。source 自身が、この二重性が v0.1 の失敗原因だったと述べている。
4. **E08** の N-04 は、証拠所見（有効性を示す証拠がほとんどない）であり、同時に verdict 文を削除させた判定基準（内部矛盾の検出点）でもある。resource 欄と evaluation 欄の両方に実体を書かないよう、resource に置いた。
5. **E09-b** の「設計文書 Part IX の規定に従う」は事前規定された停止規則（evaluation rule）だが、規定内容が packet になく、実質的には「文書の権威に従う」という assumption としてしか検証できない。
6. **E10 / E11 / E12** の C1–C3、S1/S2/S2*、A2/A3 ラダーは明らかに evaluation rule だが、昇格・据置の基準が packet 内に定義されていない。規則の適用結果のみが source-derived で、規則自体は UNKNOWN。この状態では「規則に従った」という記録は検証不能な形でしか残せない。
7. 逆に **E07** は、この境界が source 側で完全に分離されていた唯一の episode である（§5 falsification / §6 success conditions が claim とは別文書節に置かれている）。

### 3.6 available branch / adopted side claim の境界問題

1. **同一の路が subepisode をまたいで状態を変える。** E09-a では (iv) 終了が available branch（許容範囲、採らず）だったが、E09-b では実質的に採用される。submission block には subepisode 間で branch を追跡する欄がなく、二つのブロックを並べても「同じ路が後に採られた」ことは記録できない。E02 でも同型のことが起きる（Breuer/Wolpert の追加条件が E02-a では available branch、E02-b では一部が採用される）。
2. **却下された路と、その却下の強さが区別できない。** E07 では M0 が「defensible stricter label」として開いたまま残り、M2/M3 は preregistered criteria により却下される。E10 では C2/C3 が明示的に却下される。instructions は両者を等しく available_branches に入れるよう指示するが、「開いたまま」と「規則により閉じた」の差は欄に残らない。E07 の A2 の status に注記する形で近似した。
3. **修復路と scope condition の区別がつかない。** E04 の fresh preparation（有限回許せば反例は消える）は、主張の修復路とも、反例の適用範囲の画定とも読める。E02-b の四条件も同じ問題（§3.5-2 と同一箇所）。
4. **available branch と adopted side claim の内容が実質同一になる場合がある。** E03 では「具体的なチャネル等について証明する路」が available branch であり、「そう証明しなければならない」が adopted side claim である。書き分けたが、この分離自体が reader の再構成である。
5. **adopted side claim を元 claim の成功と読まない、という規則は明確だった。** E01 の S01、E02-a の S02、E04 の S04、E07 の S07、E10 の S10 はいずれも元 claim とは別 ID を与え、terminal_status も別に付けた。この点で判断に迷う箇所はなかった。ただし **E06-b** の S06b（「棄却された historical working hypothesis として残す」）は、retention なのか放棄の記録なのかが source の語から決められない。

### 3.7 coder instructions（v0.1.1）の残存欠陥

記録のみ。改訂案は書かない。

1. **`degenerate_or_target_leakage` が定義されていない。** submission block には現れるが、本文のどこにも定義・例・provenance 指針がない。Reader 02 は「結論が定義や前提に埋め込まれている退化（E03 の明示例）」と「名目上の target が、実際には他の要因が生んだ結果を取り込む leakage（E04 の内部性ラベル）」の二つの読みを採ったが、これは reader が自分で決めた運用である。
2. **`move_taken` が after-claim 別に書けない。** `claim_after` は A1/A2/A3 と多重化でき、`terminal_status` も after-claim ごとに要求されるのに、`move_taken` は単一欄である。E05-a（A2 は規約化、A3 は条件付き補題で move が異なる）と E09-a（A1 は放棄、A2 は対象限定）では、欄外に注記して対応させるしかなかった。
3. **after-claim ラベル A1/A2 が source-local ラベルと衝突する。** instructions は source-local な「M1」と formation code M1 の混同を警告するが、A ラベルには触れていない。E12 では source の判定が「A2」であり、submission block の after-claim ラベル A2 と字面が一致する。E07 では source-local な value ladder が M0–M3 で、formation code と字面が一致する。
4. **`claim_identity` と `claim_before` の差が説明されていない。** 両欄が隣接して並ぶが、前者が ID なのか、claim の同定基準の記述なのかが本文にない。Reader 02 は ID として運用した。
5. **provenance の粒度が指示と欄割りで食い違う。** 本文は「最小の実用単位で provenance を付す」と指示するが、`provenance_label` の `dependencies` は assumptions / proof_or_evidence_resources / evaluation_or_decision_rules の三欄を一つにまとめている。三者に別々の provenance が必要な場合（E06-a: assumptions は source-derived、resources は UNKNOWN、rules は存在のみ source-derived）に欄が足りず、一行に三つ書き込んだ。
6. **Step 3 と Step 4 のラベル指定が競合する。** Step 3 は adopted side claim に「独自の claim ID を与え、同じ ID を claim_after と terminal_status で使え」と指示し、Step 4 は after-claim を「A1、A2 と label せよ」と指示する。両立させるため `A2 [S01]` の形で併記した。
7. **`alternative_segmentations` を残したあとの扱いが規定されていない。** 代替も coding するのか、採用した方だけを coding するのか、どちらを採用したかをどこに書くのかが本文にない。Reader 02 は採用した方のみを coding し、欄内に採否と根拠を書いた。
8. **subepisode 間のリンク欄がない。** E09-a → E09-b の branch 継承、E01 の O:W→L と E02 の W_t→(W_{t+1},l) の連続性、E04 の「内部性ラベル」と E05-b の「inside vs outside」の同型性を記録する場所がない。
9. **corpus item をまたぐ before の設定が許されるかが書かれていない。** E02 の Excerpt 1 は E01 の静的写像を明示的に否定する形で始まる。E01 を before に取れば M7 相当が coding できるが、item を container として扱う Step 0 の指示との関係が不明。
10. **obligation_type の列挙に受け皿のない型がある。** 定義的規約（E05-a の A2）、分類体系の主張（E06-c）がどれにも当たらない。UNKNOWN/AMBIGUOUS で処理した。
11. **status 語彙の調停規則がない。** 「status vocabulary may follow the source」とあるが、source 語（`frozen negative baseline`、`D 相当`、`M1 — Organizational value`、`S2*`、`C1`）と提示語彙（retained / conditional / demoted / withdrawn / terminated / negative result fixed / open）が衝突または重複するときの扱いが書かれていない。E06-a では一つの after-claim に withdrawn と negative-result-fixed の両方を付けた。
12. **isolation 規則と corpus の path 指定が部分的に矛盾する。** instructions は「corpus に path が書かれた原 source へは戻ってよい」とするが、E05 と E06 と E08 の指定 path には `v0.1_to_v0.2_diff` 文書が含まれる。これは trajectory を再構成した二次文書であり、「trajectory summaries を読むな」という同じ節の禁止と境界が接している。Reader 02 は復帰しないことで回避した。
13. **excerpt が構造的に不足している場合の指示がない。** E08 Excerpt 1 は見出し一行のみ、E06 Excerpt 2 は表の一行のみである。「excerpt が不十分なら原 source へ戻れ」という条件は、12 の制約と組み合わさると出口がなくなる。

### 3.8 source だけでは決められなかったこと

packet 内で解決できず、UNKNOWN / AMBIGUOUS のまま残した事項。

**文書の同定・版に関するもの**
- E06: Source path A（版表記なし）が改訂前テキストかどうか。claim_before の同定がこれに依存する。
- E06: DR-1 — Weak relocation が v0.2 で維持されたか、撤回されたか、再定義されたか。
- E08: 「Codex」が人的レビューアか自動レビューか。witness を自己発見とするか外部指摘とするかがこれに依存する。

**source-local ラダー・ラベルの定義**
- E06: Null C（Solved by quotient）、Null D/E（historical sequencing / reviewer-imposed narrative）の定義。
- E07: §5 falsification conditions、§6 success conditions の内容。M0–M3 ladder の定義。
- E08: verdict A の内容（「A を選ばない理由」だけが残り、A 自体が packet にない）。
- E09: 14 コードの内容、NONEVAL / RET-DOWN の定義、L2/L3 の意味、「D 相当」の定義、設計文書 Part IX の規定内容、「実質 1 コード」の判定基準。
- E10: C1/C2/C3 の昇格基準、「既存21定理」の内容。
- E11: S1/S2/S2* の定義、S2 の元の主張文。
- E12: A0–A3 の定義。E11 の S2* と E12 の S2* が同一ラダー上の同一ラベルか。

**episode 構造に関するもの**
- E02 / E04 / E05 / E06 / E08 の segmentation（§3.3）。
- E05: Excerpt 4 の二つの [WITHDRAWN] が一つの改訂判断か二つか。
- E06-c: taxonomy 削除の理由（失敗による撤回か編集判断か）。
- E12-b: 判定 A2 が格下げの結果か、最初からの分類記録か。
- corpus 全体: E01–E04 が一つの走る claim の連続段階なのか、独立した四つの episode なのか。excerpt は Phase 1/2/3/5 という順序を示すが、依存関係は明示されない（Phase 4 は corpus にない）。

**witness の内容**
- E06-a: 「系列が連鎖を支持しなかった」ことの具体的観察内容。
- E09-b: P1-reduced two-field check で何が観察されたか。
- E05-b: 空間的位置を第一義的条件とすることを撤回させた固有の witness。

**move coding の決定不能点**
- E02-a: M15 を coding すべきか（quine/Kleene/Breuer/Wolpert は witness か absorption か）。
- E02-b: M2 を coding すべきか。
- E07: M15 / M2 を coding すべきか。
- E09-b: 「downgrade to comparative review」が M17 単独か M15 を伴うか。
- E11: 「local に限定」を M3 と M14 のどちらで扱うか。
- E12-b: M12 を coding すべきか。
- E12-a: M1/M3/M4 への分解の粒度。

---

**End of Reader 02 output.** adjudication、framework 改訂、他 reader との比較は行っていない。既存ファイルは変更していない。

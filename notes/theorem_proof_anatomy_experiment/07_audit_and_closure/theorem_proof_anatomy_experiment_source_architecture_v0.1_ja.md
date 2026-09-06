# 実験系列 source architecture v0.1

- **地位:** 最終記録を書くための設計図。本文ではない。
- **日付:** 2026-09-06
- **対象:** `notes/` 内の 70 ファイル（origin 系列、theorem anatomy、proof-formation、reachability、theorem pilots、audits）
- **既存ファイル:** 一切変更していない。

## 0. Required stance

- **source architecture only.** 最終 synthesis の散文ではない。
- **not a theorem / not a new proof theory / not a new framework.** 章立てと台帳の設計だけを行う。
- **no novelty inflation.** textbook fact は textbook fact と書く。
- **preserve negative results.** KILL / RETIRE / NOT ESTABLISHED / OPEN をそのまま繰り越す。
- **preserve chronology.** 実際の作成順を保存し、後の結論を前の phase へ逆投影しない。
- **distinguish source-derived facts from retrospective interpretation.** 各 phase に confidence ラベルを付す。
- **standard terminology preferred.**
- **retired project-local vocabulary は technical term として復活させない。** §5 の terminological history でのみ、退役済みと明示して言及する。

最終記録の性格をここで固定する。

> これは「新しい理論が完成した物語」ではない。一連の essence 型仮説を順に検査し、候補概念を繰り返し KILL / RETIRE し、最後に audit discipline だけが残った実験史である。

この一文に反する書き方（発見譚、目的論、伏線回収）を最終記録で使わない。

---

## 1. Chronology

### 1.1 証拠の性質

順序は各ファイルの mtime から取った。**source-derived**。ただし三つの留保がある。

1. `theorem_proof_anatomy/` 配下の 11 ファイル（v1.1 + 10 stress tests）は全て `09-04 20:32` の同一タイムスタンプを持つ。これはディレクトリ移動の痕跡であり、**この 11 件の内部順序は mtime から復元できない**。内容上の依存（v1.1 が 21 定理の survey、stress tests がその適用）から順序を推定するのは retrospective interpretation である。
2. mtime は最終更新であり作成時刻ではない。同日内の分単位の順序は編集順を表すが、思考順とは限らない。
3. 最初期ノート（`tool_truth_absence_working_note.md`, 08-16 07:08）は、その本文自身が「一連の検討を…失敗・撤回・問題分解の履歴として再構成する」と述べる。**したがって file record 上の最古点は、問いの発生時点ではなく、既に一度撤回を経た後の整理時点である。** 最終記録はこの点を明示すること。

### 1.2 時系列（8 phase）

| Phase | 期間 | 主要ファイル数 | 一行要約 |
|---|---|---|---|
| **0** | 08-16 07:08 → 08-22 08:52 | 20 | 観測成功と存在論的一意性の分離。普遍不可能定理を放棄し、経験的比較へ縮小し、最後に comparative methodology を終了 |
| **1** | 09-04 20:32 以前（内部順序不明） | 11 | theorem anatomy v1.1 と 10 本の形式定理 stress test |
| **2** | 09-04 21:18 → 09-05 05:33 | 12 | proof-formation meta-experiment、frozen corpus、blind readers、adjudication |
| **3** | 09-05 05:51 → 06:57 | 5 | 有限命題 prototype、adversarial stress test、post-mortem |
| **4** | 09-06 06:31 → 10:08 | 10 | record-frame 系 5 テスト（sensitivity / persistence / visibility / non-nested / minimal separator） |
| **5** | 09-06 13:32 → 15:21 | 6 | reachability stress（1+1=2、可換律、IVT、FTA）、cross-test audit、synthesis closure |
| **6** | 09-06 15:55 → 17:49 | 6 | theoremhood / enrichment / quotient / specification / cross-calculus の 5 pilot |
| **7** | 09-06 18:01 | 1 | full-series independent audit（Option 2） |

Phase 0 と Phase 1 の間に **13 日の空白**がある。Phase 1 の内部日付が不明なため、この空白に何が起きたかは source から復元できない。最終記録では空白として記録し、埋めない。

Phase 2 以降は 09-04 21:18 から 09-06 18:01 までの **約 45 時間**に集中している。最終記録はこの密度を隠さないこと。密度は、後半が前半の材料を再利用した連続作業であったことの source-derived な証拠であり、独立な再検証が行われていないことの理由でもある。

### 1.3 phase 間の実質的依存（source-derived）

- Phase 1 の stress tests（Gödel closure reversal、reflection scope、proof-theoretic ordinal）は、Phase 2 の frozen corpus の episode **E10 / E11 / E12** として再利用された。Phase 1 は Phase 2 の *入力材料* である。
- Phase 0 の working notes と case studies は、同じ corpus の **E01–E09** である。したがって Phase 2 は Phase 0 と Phase 1 の両方を対象化した。
- Phase 5 の reachability tests は、Phase 3 の post-mortem が確立した「semantic 効果だけからは history を同定できない」を明示的に前提として引用する。
- Phase 6 の各 pilot は直前の pilot の未検査部分を次の問いに指定している（specification pilot の item 17 が cross-calculus pilot の問いをそのまま予告している）。これは source-derived な連鎖である。

---

## 2. Genealogy of the central question

一本道ではない。放棄された枝を残す。

```
根: 予測・観測の成功だけから、世界が唯一この存在論であると言えるか
 │
 ├─[枝 A: 放棄] 観測写像の非単射性から普遍的不可能定理
 │    → inverse problems / identifiability / observational equivalence に吸収
 │    → O = id が即座の反例
 │    → 自己包含だけでは非識別性が出ない（quine / Kleene / Breuer / Wolpert）
 │    → 生成―ログ非同型は情報損失を定義に埋め込めば循環
 │
 ├─[枝 B: 放棄] 前提スタック / web of constraints / validation basis
 │    → assurance case、traceability、evidence graph、model validation に吸収
 │
 ├─[枝 C: 終了] 経験的文書比較（GST → 計量学 → 水文学 → P0 → P1-reduced）
 │    → GST: frozen negative。計量学: M1 organizational value のみ
 │    → 14 コード中生存 1 → comparative methodology 終了、comparative review へ降格
 │
 ├─[枝 D] 定理の条件は何をしているか（theorem anatomy v1.1 + 10 stress tests）
 │    → hypothesis levels、closure roles、Erasure Test、R0/R1/R2
 │    → H2 暫定支持、H3（普遍的残差パターン）不支持
 │
 ├─[枝 E] 壊れた主張の訂正史は独立に再構成できるか（proof-formation）
 │    │  → M1–M17、K/A/R/D/U、L0/L1/L2 ladder、L3 は明示的に拒否
 │    │  → blind readers 2 名 + adjudication → P0-PASS
 │    │
 │    ├─[枝 E1] 有限命題 prototype で move 区別は semantic か
 │    │    → M1 と scope が相互模倣。E 挙動は 3 move を区別しない
 │    │    → 区別は typed record が担っていた
 │    │
 │    └─[枝 E2: KILL] record frame を変えれば何が見えるか
 │         → frame 相対、visibility は non-nested family で非単調
 │         → minimal separator は characterization claim が KILL
 │
 ├─[枝 F] 証明の中で実際に効いているものは何か（reachability stress）
 │    → 語彙は全て標準語へ無損失。v2 は延期ではなく retire
 │
 └─[枝 G] theoremhood は何を settle するか → proof equality → specification → cross-calculus
      → 全て標準 proof theory / metatheory へ帰着。independent audit: Option 2
```

**問いの変形の実際の順序**（source-derived）:

1. 成功する道具は真理を一意に指定するか（08-16）
2. → 何が識別可能性を支えているのか（前提スタック、08-16〜17）
3. → 一般語彙は field-native reconstruction より診断を加えるか（GST / 計量学、08-16〜21）
4. → 文書連鎖に audit-ready な実例は存在するか（水文学、08-21〜22）
5. → 定理の条件は何をしているか（Phase 1）
6. → 壊れた主張の訂正史は再構成可能か（Phase 2）
7. → その区別は semantic か record 由来か（Phase 3）
8. → 記録の枠を変えると何が見えるか（Phase 4、KILL）
9. → 証明の中で何が必要か（Phase 5）
10. → theoremhood は何を settle するか / 証明の同一性とは何か（Phase 6）

**注意すべき非連続点。** 4 → 5 は対象領域の交代（科学的主張 → 数学の定理）である。source にはこの交代を説明する文書がない。最終記録は「なぜ数学へ移ったか」を推測で埋めず、**source-silent な転換点**として記録すること。

---

## 3. Phase map

各 phase に固定フォーマットを適用する。confidence は
`[SD]` directly source-supported / `[RC]` reconstructed from multiple sources / `[RI]` retrospective interpretation。

### Phase 0 — 道具的成功と存在論的一意性

- **Question** `[SD]` 予測・観測の成功だけから、生成構造を一意に同定できるか。
- **Working hypothesis** `[SD]` 観測写像の非単射性、観測者の内部性、生成→安定ログ変換から、存在論的一意性についての一般的不可能定理が得られる。
- **Objects** `[SD]` 候補世界集合と観測写像、量子 identifiability、GST、計量学、水文学の文書連鎖、一般技術標準。
- **Test** `[SD]` 反例構成、prior-art 再構成、field-native control reconstruction、preregistered kill criteria、14 コードの generic baseline 比較。
- **Positive** `[SD]` 観測成功と唯一の存在論的解釈は論理的に別である。識別を支える条件は既存分野で個別に強く扱われている。
- **Negative** `[SD]` 普遍的不可能定理は得られなかった。一般監査語彙は GST と計量学で診断を変えなかった。水文学の文書形式の大半は generic standards lifecycle で説明できた。
- **KILL / RETIRE** `[SD]` 普遍的非一意性定理、Deferred Resolution（frozen negative）、一般 assurance 語彙の追加価値、comparative methodology そのもの。
- **What survived** `[SD]` 8 つの方法規律（field-native first、Erasure Test、control reconstruction、historical/logical separation、artifact/institution/field separation、time-sliced audit、selection-route logging、preregistered kill criteria）。
- **Why next** `[RC]` 経験的比較が終了し、残った規律を検査できる対象として形式的材料が選ばれた。ただし交代の理由は source に書かれていない `[RI]`。
- **Primary sources** `tool_truth_absence_working_note.md`〜`_v0.4.md` と 3 diffs、`scientific_identifiability_case_01_quantum.md`、`quantum_identifiability_prior_art_network.md`、`deferred_resolution_case_01_gst*.md`、`scientific_assurance_case_02_metrology*.md`、`web_of_constraints_*`、`validation_basis_transition_working_note_v0.1.md`、`case_01_hydro_target_artifact_discovery_v0.1.md`、`hydrology_negative_knowledge_preservation_note_v0.1/v0.2.md`、`p0_generic_standards_baseline_v0.1.md`、`p1r_noneval_two_field_check_v0.1.md`、`tool_truth_absence_research_trajectory_summary.md`
- **Confidence** `[SD]`。trajectory summary（08-22）が phase 全体を当事者自身が要約しており、証拠が強い。

> **最終記録で最も重要な事実の一つ:** 系列全体の最終的な生き残り（audit discipline）は、Phase 0 の終了時点（2026-08-22）で既に 8 項目として明文化されていた。後続 phase はそれを発見したのではなく、形式的設定で再導出し、logical form の観点から精密化した。目的論を避けるため、この順序を逆にしない。

### Phase 1 — theorem/proof anatomy v1.1

- **Question** `[SD]` 定理の各条件はどの機能を果たし、除去すると何が起きるか。
- **Working hypothesis** `[SD]` H2「定理横断で再現可能な機能分類が見える」、H3「残差再出現まで含む普遍パターンがある」。
- **Objects** `[SD]` 通常の 21 定理 + Gödel I/II、Tarski、Löb、GL、reflection、Turing–Feferman、GLP、proof-theoretic ordinal、theory-strength。
- **Test** `[SD]` 各定理に assumptions / hypothesis levels / condition types / closure roles / what_fails_if_removed / R0-R1-R2 / proof_resources を記入し、10 本の stress test で自前語彙を検査。
- **Positive** `[SD]` object/ambient/background/definitional の分離、仮定と proof resources の分離（IVT の上限性を proof resource と明記）、closure role の 6 クラスタが複数分野で再現。
- **Negative** `[SD]` H3 不支持。R2 は稀で Stokes / Gauss–Bonnet / 中国剰余 / Bayes に偏る。stress tests は自前語彙を C1 / S2* / A2 として説明用へ降格した。
- **KILL / RETIRE** `[SD]` 閉包語彙を独立分類とする読み（C1）、S2 の広い適用（S2*）、ordinal を万能スカラーとする読み。
- **What survived** `[SD]` v1.1 の field 群、Erasure Test、R0/R1/R2（この survey の内部でのみ）。
- **Why next** `[RC]` v1.1 の stress tests が「自前語彙が標準語に吸収される」を繰り返し示したため、その吸収過程自体を対象化する実験が構想された。
- **Primary sources** `theorem_proof_anatomy/` 全 11 ファイル
- **Confidence** `[SD]` 内容、`[RI]` 内部順序（mtime 使用不可）。

### Phase 2 — proof-formation の再構成可能性

- **Question** `[SD]` 壊れた claim candidate の訂正史を、独立 reader が source だけから再構成できるか。
- **Working hypothesis** `[SD]` M1–M17 の move codebook と K/A/R/D/U ledger。L0→L1→L2 の evidential ladder、L3（定理化）は 10 の理由で明示的に拒否。
- **Objects** `[SD]` Phase 0 と Phase 1 から選んだ 12 episode の frozen corpus。
- **Test** `[SD]` coder instructions（v0.1 → v0.1.1）、Reader 01（pilot）、Reader 02 / 03（blind）、self-adjudication、blind comparison、independent inter-reader adjudication。
- **Positive** `[SD]` 全 parent item で before / witness / withdrawal / remnant / terminal direction が reader 横断で同方向に再構成。P0-PASS。
- **Negative** `[SD]` move code は一致しない。claim identity と episode boundary が最も脆い。key が期待する 3 コードは packet から到達不能。`degenerate_or_target_leakage` は reader 向け文書に定義がない。
- **KILL / RETIRE** `[SD]` 一致率・kappa・score の使用、L3 の追求。
- **What survived** `[SD]` assumption / proof-resource 境界が最大の誤り源であること、segmentation の reader 依存性、evidence-type 別の裁定分類（A〜G）。
- **Why next** `[SD]` reader 実験が claim identity と boundary を脆弱点として特定したため、それらを完全に制御できる最小形式設定が必要になった。
- **Primary sources** `proof_formation_meta_experiment_v0.1.md`、`_frozen_toy_corpus_`、`_coder_instructions_v0.1/v0.1.1`、`_adjudication_rules_`、`_reader_01_*`、`_reader_02_claudecode_v0.1.1`、`_reader_02_adjudication_note_`、`_reader_03_v0.1.1`、`_reader_02_03_blind_comparison_`、`_inter_reader_adjudication_`
- **Confidence** `[SD]`。
- **記録すべき事前予測の的中** `[SD]` meta-experiment §16 は reader 実験の前に「claim identity / episode boundary — highest priority」と書いた。reader 実験と adjudication はこれを確認した。事後の説明ではなく事前登録された予測である。

### Phase 3 — 有限命題 prototype

- **Question** `[SD]` 完全に明示的な最小設定で、再構成可能な transition core と boundary 依存の move coding を分離できるか。
- **Working hypothesis** `[SD]` M1 / M2 / scope surrogate / M17 の区別は有限意味論の中で保たれる。
- **Objects** `[SD]` 有限命題の valuation 空間、\(M(H)\)、\(E(H,C)\)、admissible scope、identity token、trivial-rescue flags。
- **Test** `[SD]` prototype + checker、次に adversarial stress checker（34 findings、n=2 全数 / n=3 標本）。
- **Positive** `[SD]` core identities は全域で成立。M2 の方向制約は実際に強制される。M17 は slot typing に依存しない唯一の move。
- **Negative** `[SD]` M1 と scope は評価対象に対して同一操作。3 move の到達可能 after-\(E\) 族が一致。T1 は意味的に回避可能。exact-filter repair が一般に存在。identity token は両方向に無制約。state 型 successor で rescue control が適用不能になる。
- **KILL / RETIRE** `[SD]` semantic set behavior から formation history を読む読み。
- **What survived** `[SD]` typed record が区別を担うこと、A/B/C/D の記述的層分け（taxonomy ではない）、`withdrawn` に semantic surrogate がないこと。
- **Why next** `[SD]` post-mortem が「区別は record typing にある」と結論したため、記録の枠そのものを変える実験へ進んだ。
- **Primary sources** `proof_formation_finite_propositional_prototype_v0.1.md` + checker、`_stress_test_v0.1.md` + stress checker、`_postmortem_architecture_v0.1.md`
- **Confidence** `[SD]`。

### Phase 4 — record-frame 系（唯一 KILL が発火した枝）

- **Question** `[SD]` 同じ履歴を異なる記録枠で射影すると、どの区別が保たれ、潰れ、生じるか。以後、何が枠に依らず残るか → どの枠で初めて見えるか → 非入れ子の枠族でも再現するか → 区別を消すまで field をどこまで削れるか。
- **Working hypothesis** `[SD]` (i) self-state を記録すれば action type の事前登録バイアスを回避できる。(ii) 枠に依らない core が取り出せる。(iii) 区別は minimal separating field set で特徴づけられる。
- **Objects** `[SD]` 凍結した 10 履歴 + control、nested 枠族 R0–R4、non-nested 枠族 N1–N5、coordinatewise atomic projection。
- **Test** `[SD]` 5 本のテストと 5 本の checker。全 pair 行列、消去制御、置換制御、field ablation。
- **Positive** `[SD]` action label を事前入力せずに一部の区別を露出できた。provenance 依存（H9/H10）は field レベルで安定して再現。
- **Negative** `[SD]` 「bias を回避する」は維持できない。persistence は選んだ projector の設計効果。first-visible frame は区別の性質ではない。non-nested 族で visibility は非単調（visible→invisible→visible）。偶然の cue が pair を完全に分離しうる。
- **KILL / RETIRE** `[SD]` **minimal separating field set が区別を特徴づけるという主張は KILL。** coordinatewise projection の下では全ての separating set が separating singleton を含むため、minimal set の枚挙は field 差の枚挙以上を与えない。
- **What survived** `[SD]` field ablation inventory のみ（診断用、説明用ではない）。
- **Why next** `[RC]` この枝が KILL に達したため、記録設計の方向を離れ、定理そのものに対象を戻した。ただし転換の説明は source にない `[RI]`。
- **Primary sources** `proof_formation_record_frame_sensitivity_test_v0.1.md`、`_cross_frame_persistence_test_`、`_visibility_transition_test_`、`_non_nested_frame_replication_test_`、`_minimal_separating_field_set_test_` と各 checker
- **Confidence** `[SD]`。

### Phase 5 — reachability stress と退役

- **Question** `[SD]` 証明資源、仮定、理論、構造、解釈を変えると何が起きるか。
- **Working hypothesis** `[SD]` reachability / route / constraint propagation が標準の導出可能性を越える分析力を持つ。
- **Objects** `[SD]` 1+1=2、加法可換律、IVT、FTA。
- **Test** `[SD]` 各定理で明示的導出、条件削除、countermodel、citation expansion、事前登録した展開深度（FTA の Level 0/1/2 と stop rule）。
- **Positive** `[SD]` 3 種の erasure に異なる証拠が要ること。可換律の induction-free countermodel。IVT の ℚ control。FTA の Level 2 でも core library が異なること。
- **Negative** `[SD]` 語彙は全て標準語へ無損失。necessity は主要資源のどれについても確立せず。heterogeneity は presentation 相対。
- **KILL / RETIRE** `[SD]` 語彙 4 語、v2 rewrite（延期ではなく retire）、route intersection からの necessity 推論。
- **What survived** `[SD]` evidence-burden の 3 分割、occurrence ≠ necessity、setting migration ≠ falsification。
- **Why next** `[SD]` cross-test audit が「necessity 問題に道具がない」と指摘し、synthesis closure が rewrite を閉じた。残りは theoremhood 周辺の未検査部分だった。
- **Primary sources** 4 tests、`_cross_test_audit_v0.1.md`、`_synthesis_closure_v0.1_ja.md`
- **Confidence** `[SD]`。

### Phase 6 — theoremhood 周辺の 5 pilot

- **Question** `[SD]` (B) theoremhood は何を settle しないか →（C）statement を強めると何が settle するか →（D）同一 calculus 内で quotient は何を消すか →（E）specification を変えると何が保たれるか →（F）derivability 同値は proof class 対応へ持ち上がるか。
- **Working hypothesis** `[SD]` 順に、open remainder が対象になる／enrichment が外へ問題を押し出す／quotient が essence を取り出す／単一の preservation 概念がある／同じ定理なら同じ証明。
- **Objects** `[SD]` 固定文脈の導出可能性判断、proof term と finite deletion-minimality、products 付き STLC、命題論理の renaming / definitional extension / 強化、ND / STLC / LJ。
- **Test** `[SD]` 4 例の再利用、16 term の型検査つき checker、T1–T4 の 4 変換、\(T_A,U_A,T_B,U_B\) の 4 translation と quotient well-definedness 検査。
- **Positive** `[SD]` 全て finite に停止し、各問いは固定後に標準的な答えを持った。ND↔STLC は constructorwise bijection。\(\lambda p.\pi_1p\) と \(\lambda p.\pi_2p\) は全 level で別 class。
- **Negative** `[SD]` outward displacement も infinite regress も出ない。quotient は essence を出さない。単一の preservation 概念はない。ND→raw LJ は quotient map さえ well-defined でない。global bijection は NOT ESTABLISHED。
- **KILL / RETIRE** `[SD]` intrinsic proof identity、canonical proof、cut-free = canonical、Curry–Howard から普遍的 proof identity、universal preservation notion。
- **What survived** `[SD]` 4 つの独立検査（well-definedness / injectivity / surjectivity / round trips）と、preservation は map + object + scope + direction を指定して初めて意味を持つこと。
- **Why next** `[SD]` cross-calculus pilot 自身が「これ以上は literature の coherence theorem が要る」と述べ、次の falsification question を **none** と書いた。
- **Primary sources** 5 pilot + `theorem_proof_quotient_invariance_pilot_v0.1.py`
- **Confidence** `[SD]`。

### Phase 7 — independent audit

- **Question** `[SD]` 系列全体で何が残り、標準語へ還元でき、novelty がなく、それでも監査規律として有効か。
- **Test** `[SD]` 7 文書の横断監査、novelty A–E 評価、失敗方向の falsified / unsupported / ill-posed 分類。
- **Result** `[SD]` **Option 2**（coherent methodological result、no new mathematics）。最高 novelty 評価は C（checklist）。theorem anatomy という名称は Phase D で広すぎ、Phase F で誤導的。
- **Primary sources** `theorem_proof_anatomy_full_series_independent_audit_v0.1.md`
- **Confidence** `[SD]`。ただしこの audit は系列内で書かれており、外部の独立監査ではない `[RI]`。

---

## 4. 三種の歴史を分離する

最終記録は H1 / H2 / H3 を混ぜないこと。混ぜると「概念が進化した物語」に見えてしまう。

### H1 — 概念史（問いの変形）

§2 の genealogy がこれに当たる。要点は、**問いが深まったのではなく、対象領域が 3 回交代した**ことである。科学的主張（Phase 0）→ 定理の条件（Phase 1）→ 記録と証明（Phase 2–4）→ 定理と証明の同一性（Phase 5–6）。この交代の理由は source に書かれていない箇所がある。

### H2 — 実験史（実行した test / counterexample / pilot）

§7 の evidence ledger がこれに当たる。特徴は、**後半ほど実行可能な検査が増える**ことである。Phase 0–1 は文書比較と反例、Phase 2 は人間（reader）実験、Phase 3–4 と Phase 6-D は実行可能な checker を伴う。最終記録はこの methodological な強化を、結論の強化と混同しないこと。checker が増えても、結論は一貫して negative である。

### H3 — 用語史

| 用語 | 導入 | 導入理由 | 退役理由 | 標準的な置換 |
|---|---|---|---|---|
| 道具の真理不在性 | Phase 0 v0.1 | 成功が補助条件を自己証明しない直観の作業名 | 「真理の不在」と誤読される。v0.1 自身が改名対象と明記 | instrumental success does not self-certify its auxiliary conditions |
| assurance provenance / handoff / validation basis | Phase 0 | 保証の出所を追跡する索引語 | assurance case、traceability、evidence graph に吸収 | 既存の assurance / traceability 語彙 |
| Deferred Resolution | Phase 0（GST） | 反復的な問題再配置の機構名 | Erasure Test 後、既存語彙でより正確に記述できた | conditional inverse problem、nuisance parameter、identifiability modulo gauge 等 |
| web of constraints / claim transport | Phase 0 | claim の移送を描く図式 | 診断を変えなければ比喩に留まる、と自ら判定 | transport、extrapolation、applicability |
| R0 / R1 / R2 | Phase 1 | 条件除去後の残差挙動の記録ラベル | 21 定理 survey の外では使われず、R2 は後続で一度も使用されない | survey 内でのみ保持。外部では使わない |
| closure / escape route / blocking / residual | Phase 1 | 定理条件の機能比較のメタ記述 | stress test 自身が「標準用語ではない」と宣言し C1 へ降格 | 標準の proof theory 用語 |
| M1–M17 / K-A-R-D-U | Phase 2 | 訂正 move の codebook と ledger | code 一致は得られず、K/A/R/D/U は observable と価値判断が混在 | move は記述として保持可。score 化は禁止 |
| reachability / route / constraint propagation | Phase 5 | 導出可能性を形成過程の語で言い直す試み | 4 test で無損失に標準語へ戻る | derivability、proof organization、proof bookkeeping |
| closure / open remainder | Phase 6-B | 「settle された後に何が残るか」の平易な題 | 標準の導出可能性判断以上を加えない | fixed-context derivability、判断が答えない問い |
| judgment enrichment | Phase 6-C | 判断に情報を加える操作の作業句 | 標準語のほうが短く正確 | strengthening the statement |
| quotient invariance | Phase 6-D | 同値で割ったとき何が残るかの題 | 「invariance」が theorem-intrinsic な不変量を含意し、実際は関係相対 | quotient by a specified equivalence |
| specification (change) preservation | Phase 6-E | 仕様変更下の保存の題 | 自ら 7 種へ分解した対象を単一名で呼んでいる | conservativity、monotonicity、reflection、translation |
| cross-calculus proof-class preservation | Phase 6-F | 体系間の証明対応の題 | 標準語のほうが 4 検査を既に区別している | translation descends / faithful / full / equivalence |

**生き残っている唯一の用語的残渣** `[SD]`: Phase 6 の 5 pilot は本文中で自分の題名語を退役させているが、**ファイル名と題名は退役していない**。ディレクトリを一覧した読者は技術的プログラムの存在を推定してしまう。最終記録はこの点を明記し、題名を根拠に体系を再構成しないよう注意すること。

---

## 5. essence 探索の推移（歴史的反復として記録）

依頼で提示された連鎖を source と突き合わせた。**12 項すべて source-supported** である。

| 探した対象 | 実際に依存が移った先 | 主要 source |
|---|---|---|
| action | claim identity / episode boundary | meta-experiment §16、reader 02/03、inter-reader adjudication |
| semantic move | typed record | finite propositional stress test、post-mortem §3 |
| self-state | record-frame choice | record-frame sensitivity §17 |
| frame-independent core | projector design | cross-frame persistence §18–19 |
| first-visible frame | frame-family order | non-nested replication 3, 7 |
| visibility | separating basis | non-nested replication 9 |
| minimal separator | pair design / intended distinction | minimal separating field set D5、KILL |
| reachability | ordinary derivability | 4 reachability tests Q1 |
| dependency intersection | no theorem-level necessity | IVT §19–20、FTA §20 |
| quotient | chosen equivalence relation | quotient pilot 12, 14 |
| preservation | map + object + scope + direction | specification pilot §15 |
| cross-calculus sameness | proof equality + translation compatibility | cross-calculus pilot 8–11 |

### 5.1 これを法則としない三つの理由（重要）

1. **系列自身が反例を含む** `[SD]`。judgment enrichment pilot は、表現と比較クラスを固定すれば問いが有限で停止し、後続問題を生まないことを positive control で示した。したがって「必ず外へ移る」は系列内で falsified である。
2. **上の 12 行は同じ種類の移動ではない。** 前半 7 行は「記録設計上の選択へ移った」、後半 5 行は「標準的な既存概念へ吸収された」であり、型が違う。一列に並べると法則に見えるが、並べたのは本設計文書の側である `[RI]`。
3. **選択バイアス。** 12 行は全て「essence を探した問い」であり、essence を探さなかった問い（例：可換律の countermodel 構成）は移動していない。母集団が結論を含んでいる。

最終記録では **historical recurrence**（この系列がこの種の問いに対して繰り返し経験したこと）として書き、universal displacement law として書かない。

---

## 6. falsified / unsupported / ill-posed の分類

| 仮説・直観 | 判定 | 根拠 |
|---|---|---|
| 観測成功からの普遍的存在論的非一意性 | **falsified by explicit counterexample**（\(O=\mathrm{id}\)）+ **reduced to standard terminology**（inverse problems / identifiability） | Phase 0 |
| 自己包含 ⇒ 普遍的非識別性 | **falsified**（有限 encoder、quine / Kleene）+ 既存結果は追加条件付き | Phase 0 / corpus E02 |
| 生成―ログ非同型性 | **ill-posed**（情報損失を定義に埋め込むと循環）+ falsified（可逆・完全符号化の場合） | Phase 0 / E03 |
| 一般監査語彙の追加診断価値 | **falsified by negative controls**（GST、計量学 M1） | Phase 0 |
| 分野固有の深い認識論差（水文学） | **unsupported**（14 → 10 が generic baseline で再現） | Phase 0 |
| H3 普遍的残差パターン | **unsupported**（R2 は稀で偏在） | Phase 1 |
| move code の reader 間一致 | **unsupported**（core は一致、code は不一致） | Phase 2 |
| move 区別は semantic | **falsified**（M1 と scope の相互模倣、到達可能 \(E\) 族の一致） | Phase 3 |
| self-state 記録が bias を回避する | **falsified as stated**（carrier / typing / identity / provenance の事前選択が残る） | Phase 4 |
| frame-independent core | **ill-posed / unsupported**（persistence は projector 設計の帰結） | Phase 4 |
| minimal separator が区別を特徴づける | **falsified**（全 separating set が singleton を含む。偶然 cue が分離する） | Phase 4 |
| reachability を新 primitive とする | **reduced to standard terminology**（無損失） | Phase 5 |
| dependency intersection ⇒ necessity | **falsified**（IVT の完全性再出現 vs ℚ control） | Phase 5 |
| theorem essence | **ill-posed without further specification**（何が essence を反証するか一度も定義されていない） | Phase 5–7 |
| intrinsic proof identity | **ill-posed**（「intrinsic」未定義）+ 具体的読みは全て falsified（class は関係相対） | Phase 6-D/F |
| canonical proof | **falsified by explicit counterexample**（\(\pi_1/\pi_2\)、\(L_{\text{once}}/L_{\text{twice}}\)） | Phase 6-D/F |
| proof geometry | **ill-posed**、かつ一度も試行されていない（禁止事項一覧にのみ出現） | 全 phase |
| universal preservation notion | **falsified**（T1–T4 が 4 つの非同値な概念を実現） | Phase 6-E |
| outward displacement | **falsified as a universal claim**（有限停止の positive control） | Phase 6-C |
| infinite regress | **unsupported**、普遍形は falsified | Phase 6-C |
| quotient as essence extractor | **falsified**（licensed な bureaucracy のみ消え、\(F/G\) は残る） | Phase 6-D |
| **retained as methodological discipline** | Erasure Test / control reconstruction / preregistered kill criteria（Phase 0 起源）、evidence-burden の logical-form 分割（Phase 5 で追加）、equality と map の明示（Phase 6） | — |

---

## 7. Evidence ledger

最終記録が引用すべき具体的証拠。**「何を支持し、何を支持しないか」を必ず対にして書く。**

| # | 証拠 | 支持する主張 | 支持し **ない** 主張 | 初出 | 再利用 |
|---|---|---|---|---|---|
| E-1 | \(O=\mathrm{id}_W\) | 非単射性は一般には成り立たない | 観測写像に関するどんな一般定理も | tool_truth v0.1/v0.2 Phase 1 | corpus E01、reader 02/03 |
| E-2 | 有限 encoder \(X=\Omega\times M,\ (\theta,m_0)\mapsto(\theta,\mathrm{enc}(\theta))\) | 自己包含だけでは非識別性は出ない | 自己測定制約一般の否定 | tool_truth Phase 2 | corpus E02 |
| E-3 | 二ビット破壊測定 | pairwise separation は global adaptive separator を保証しない | 内部性固有の不可能性 | tool_truth Phase 5 | corpus E04 |
| E-4 | GST Erasure Test（固有語彙を消しても情報が失われない） | 一般語彙の追加価値の否定 | GST の技術内容の否定 | `deferred_resolution_case_01_gst_v0.2.md` §16 | corpus E06（ただし excerpt には未収録） |
| E-5 | 計量学 M0–M3 判定（M1 のみ） | generic audit は表示価値のみ | field-native review 一般の優位/劣位 | metrology comparison | corpus E07 |
| E-6 | P0 の 14 → 1 コード | 文書形式は水文学固有でない | 科学一般の普遍性 | `p0_generic_standards_baseline_v0.1.md` | corpus E09 |
| E-7 | \(1+1=2\) の 2 route（inline / lemma \(L\)） | route failure ≠ derivability failure | 定理の必要条件について何も | reachability test 1 | closure pilot Case I |
| E-8 | 可換律の induction-free countermodel（標準鎖 + 双無限鎖） | 縮小理論からの非導出可能性 | induction の唯一性・最小性 | reachability test 2 | closure pilot、specification pilot T4 |
| E-9 | `Add-0` / `Add-S` 削除の countermodel | defining clause の theorem-level 役割 | どちらが「本質」か | reachability test 1 | judgment enrichment E2 |
| E-10 | ℚ 上の \(q^2-2\) | 順序体公理だけでは IVT に不十分 | 完全性の一意な必要性、LUB の唯一性 | reachability test 3 | closure pilot Case III、cross-test audit |
| E-11 | FTA の Liouville route と winding route が Level 2 でも異なる | 同じ定理を異なる theorem library が証明する | heterogeneity が定理の性質であること | reachability test 4 | closure pilot Case IV |
| E-12 | 有限命題の exact-filter \(B=\varphi_{\Omega\setminus E}\) | M1 repair は一般に安価に存在し、T1/T2 を回避する | 全ての M1 が trivial であること | finite propositional stress test M1-C | post-mortem §4 |
| E-13 | M1 と scope の相互模倣 / 到達可能 \(E\) 族の一致 | 3 move の区別は typed record が担う | move 概念が無意味であること | 同 §6–7 | post-mortem、Phase 4 全体 |
| E-14 | `withdrawn` に semantic surrogate がないこと | M17 は history 層に属し、slot typing に依存しない | M17 が他より重要であること | 同 §11 MIN-STATUS | closure pilot Q8 |
| E-15 | H9/H10 が R0–R3 で不可視、R4 で初めて分離 | provenance は他の field で代替されない | R4 が正しい枠であること | visibility transition V9 | minimal separator D3 |
| E-16 | H9/H2 が N-family で visible→invisible→visible | visibility は枠族相対で非単調 | どの枠が優れているか | non-nested replication 2, 4 | — |
| E-17 | D5：偶然の provenance cue が H8/C-F を分離 | minimal separator は意図した区別を説明しない | field ablation が無用であること | minimal separating field set D5 | — |
| E-18 | 有限 deletion-minimality の停止 | 表現と比較クラスを固定すれば問いは有限停止する | displacement が起きないこと一般 | judgment enrichment E2 | §5.1 の反例として使用 |
| E-19 | \(\lambda p.\pi_1p \neq \lambda p.\pi_2p\)（\(A\times A\to A\)） | 正規形の一意性 ≠ 命題の証明の一意性 | proof identity 一般の否定 | quotient pilot P3 | cross-calculus 15 |
| E-20 | T1 renaming / T3 definitional extension / T4 strengthening | preservation は単一概念でない | どれかが「真の」preservation であること | specification pilot | cross-calculus 20 |
| E-21 | ND→raw LJ で quotient map が well-defined でない | derivability 同値は proof class 対応を含意しない | ND と LJ が本質的に異なること | cross-calculus 13 | — |
| E-22 | \(L_{\text{once}}\) / \(L_{\text{twice}}\)（別 cut-free 証明） | cut-free ≠ canonical | 置換同値の不要性 | cross-calculus N3 | — |
| E-23 | independent audit の Option 2 判定 | 一貫した方法論的結果、新数学なし | 系列が無価値であること | full-series audit §6 | — |

**引用規律** `[SD]`: E-4 は GST の原資料にあるが frozen corpus の excerpt には含まれない。E-10 と E-11 は Phase 5 の一次証拠だが Phase 6 では再利用のみ。最終記録は初出と再利用を区別し、**後の phase の再利用を前の phase の根拠として使わない**。

---

## 8. Evidence-burden table（最終記録の中心 artifact）

Phase 7 の表を土台にし、**各行がどの phase で育ったか**の source trace を付す。これが最終記録で最も実用的な成果である。

| 主張 | 論理形式 | 十分な証拠 | 不十分な証拠 | この規律が育った場所 |
|---|---|---|---|---|
| this proof fails | 一本のテキストについての否定 | 根拠を失った step の提示 | 定理については何も言えない | Phase 5 test 1（lemma \(L\) 削除） |
| theoremhood survives | 存在 | **一本**の代替導出 | 見つからないことは証拠にならない | Phase 5 test 1–2、Phase 6-B Q2 |
| theorem non-derivable | 全導出についての全称 | 縮小理論の countermodel + 健全性、または独立性論証 | 失敗した証明試行の数、citation 追跡 | Phase 5 test 2（E-8）、Phase 0（既存の countermodel 実践） |
| hypothesis necessary | 弱めた命題への反例（存在） | 当該仮定のみ削除した反例 | この定式化での必要性であって最小性ではない | Phase 1 v1.1 `what_fails_if_removed`、Phase 5 test 3–4 で精密化 |
| setting changed | 命題の同一性についての主張 | 記号の解釈・領域・対象クラスの変化の提示 | 移行前後の真理値比較はどちらの証拠にもならない | Phase 0（分野移行）、Phase 5（ℤ/2、max、ℚ、ℝ） |
| derivability preserved（順方向） | source 導出についての全称 | 導出に関する帰納、または翻訳証明の再生 | 例での定理集合の一致 | Phase 6-E T1/T2/T3 |
| reflection holds | 逆方向の全称 | target → source の独立な論証 | 単調性は順方向のみ。Phase 6-E T4 が常設の反例 | Phase 6-E T4 |
| proof translation exists | 構成 | constructor ごとの定義 + 型/導出保存の帰納 | 定理集合の対応 | Phase 6-F \(T_A,U_A,T_B,U_B\) |
| quotient map well-defined | 同値の生成子についての全称 | **各生成子**での検査 | 生成子 1 つの失敗で不成立（E-21） | Phase 6-F |
| injectivity | 全称 | target 同値を法とする左逆、または 2 class の像の分離 | 翻訳の存在 | Phase 6-F |
| surjectivity | 全称 | 右逆、または全 target class の原像構成 | injectivity + derivability 同値では出ない | Phase 6-F |
| proof-class correspondence | 上記の連言 | 両方向の round trip（各側の同値を法として） | 4 検査の真部分集合 | Phase 6-F |

**source trace の要点** `[SD]`: 表の根は Phase 5 ではなく **Phase 0** にある。trajectory summary（08-22）§11 が既に Erasure Test、control reconstruction、preregistered kill criteria、historical/logical separation を列挙している。Phase 5 が加えたのは *logical form による分割*（存在 vs 全称）であり、Phase 6 が加えたのは *翻訳に伴う 4 検査*である。最終記録はこの三段の積み上げを、Phase 5 の単独の発見として書かない。

---

## 9. Stopping boundary

Phase 7 の指摘（「名称は Phase D で広すぎ、Phase F で誤導的」）を検証した。**支持される。** ただし Phase 7 は theorem サブ系列の A–F を用いており、本設計文書の Phase 0–7 と番号が衝突する。最終記録では次の対応表を必ず置く。

| 本設計の phase | Phase 7 audit の呼称 | 対象領域 |
|---|---|---|
| Phase 5 | Phase A | 定理の条件と証明資源 → **theorem anatomy proper** |
| Phase 6-B | Phase B | 判断が何を主張するか → **ordinary logic**（定理は例示にすぎない） |
| Phase 6-C | Phase C | 命題の強化 → **ordinary logic** |
| Phase 6-D | Phase D | STLC の \(\alpha\beta\eta\) → **type theory / structural proof theory** |
| Phase 6-E | Phase E | conservativity、definitional extension → **metatheory** |
| Phase 6-F | Phase F | Curry–Howard、Gentzen 翻訳、cut elimination → **proof theory proper** |

境界の位置 `[RC]`:

- **theorem anatomy proper** は v1.1（Phase 1）と reachability stress（Phase 5）まで。ここでは対象が個別の定理文とその仮定である。
- **ordinary logic** は Phase 6-B/C。ここで定理は例示に落ち、どの 4 定理でも同じ結論になる。
- **type theory / proof theory** は Phase 6-D と 6-F。\(A\times A\to A\) は型であって誰かが解剖していた定理ではない。
- **metatheory** は Phase 6-E。
- 加えて、**Phase 2–4 は proof theory ではなく記録設計・監査方法論**である。Phase 7 はこの枝を扱っていないため、最終記録が独自に位置づける必要がある。

最終記録は「theorem anatomy」という名称を Phase 6-D 以降に適用しないこと。

---

## 10. 最終記録に入れるもの / 入れないもの

### 10.1 本文に必ず入れる

1. 起源（instrumental success / identifiability）と、普遍不可能定理の放棄
2. 経験的枝（GST / 計量学 / 水文学 / P0 / P1-reduced）とその終了
3. theorem anatomy v1.1 と 10 stress test、H2 支持 / H3 不支持
4. proof-formation の再構成実験（blind readers、adjudication、P0-PASS）
5. 有限命題 prototype と post-mortem（区別は typed record にある）
6. record-frame 枝と **minimal separator の KILL**（系列唯一の明示的 KILL 発火）
7. reachability stress と語彙の退役、v2 の retire
8. theoremhood 周辺 5 pilot と cross-calculus の 4 検査
9. independent audit の Option 2
10. **evidence-burden table**（§8）
11. **retirement list**（§4 の H3 表 + Phase 7 §15）
12. **open items**（§13）
13. stopping decision とその根拠

### 10.2 本文に入れないもの

- 新 framework、新 taxonomy、新 score、proof geometry
- 5 スロットの抽象図式（objects + predicates + equivalences + comparisons + translations）と矢印図 — Phase 7 が「too broad to be informative」と判定済み
- VED との接続（全 phase が明示的に否定）
- 形而上学的解釈（真理の不在、科学の不可能性）
- `theorem_proof_anatomy_v2`
- reachability の救済
- essence 命題の証明の試み
- 7 本目の pilot
- 一致率、kappa、agreement rate
- ファイル名の羅列（→ source map へ）
- 退役語彙を technical term として用いる記述

---

## 11. 最終記録の章立て案

三部構成を推奨する。相対分量は本文全体を 100 とする目安。

### Part I — Genealogy（約 20）

| 章 | 目的 | 主要 source | 中心証拠 | 中心 negative |
|---|---|---|---|---|
| 1. 出発点 | 何を問うて始まったか。真理不在ではなく自己証明能力の不在であること | tool_truth v0.1–v0.4、trajectory summary | E-1, E-2, E-3 | 普遍不可能定理は得られない |
| 2. 経験的枝とその終了 | 一般語彙が実例で消える過程 | GST、計量学、水文学、P0、P1r | E-4, E-5, E-6 | comparative methodology 終了 |
| 3. 対象の交代 | なぜ数学的材料へ移ったか（**source-silent** として明示） | Phase 0 末尾と Phase 1 の存在 | — | 転換理由は資料にない |

### Part II — Experiment（約 50）

| 章 | 目的 | 主要 source | 中心証拠 | 中心 negative |
|---|---|---|---|---|
| 4. 定理の解剖 v1.1 | 条件の機能分類と Erasure Test の原型 | `theorem_proof_anatomy/` | 21 定理 survey | H3 不支持、R2 は稀 |
| 5. 訂正史の再構成 | blind reader 実験と裁定 | proof-formation 12 files | P0-PASS | code 一致なし、claim identity が脆い |
| 6. 最小形式設定 | 区別は semantic か record か | 有限命題 3 files | E-12, E-13, E-14 | semantic identification は成立しない |
| 7. 記録の枠（KILL） | 枠を変えると何が見えるか | frame 系 5 tests | E-15, E-16, E-17 | minimal separator の characterization を KILL |
| 8. 証明の中で効いているもの | 4 定理の stress と退役 | reachability 6 files | E-7〜E-11 | 語彙の無損失還元、necessity 未確立 |
| 9. theoremhood と証明の同一性 | 5 pilot | Phase 6 の 6 files | E-18〜E-22 | intrinsic identity なし、単一 preservation なし |

### Part III — Closure（約 30）

| 章 | 目的 | 主要 source | 中心内容 |
|---|---|---|---|
| 10. 残ったもの | evidence-burden table と、その三段の由来 | §8 | Phase 0 起源 → Phase 5 の logical form → Phase 6 の 4 検査 |
| 11. 捨てたもの | 語彙 12 件と仮説 12 件の処分、falsified/unsupported/ill-posed の別 | §4 H3、§6 | KILL / RETIRE の理由を必ず残す |
| 12. 境界と停止 | どこから標準 proof theory か、なぜここで止めるか、open items | §9、§13 | 事前登録された gate に適合した終了であること |

**代替案の検討** `[RI]`: 「対象領域別（科学 / 定理 / 記録 / 証明）」の 4 部構成も可能だが、時系列が崩れて目的論的に見えやすい。三部構成のほうが historiography control（§14）を守りやすいため推奨する。

---

## 12. Source map を別ファイルにするか

**YES、warranted。** 理由:

1. 対象は 70 ファイル。本文に列挙すると読み物ではなくなる。
2. Phase 0 だけで 20 ファイルあり、その大半は本文で 1–2 行しか言及されない。
3. Phase 1 の内部順序が mtime から復元できないという **traceability 上の注記**を置く場所が必要。
4. frozen corpus の 12 episode が Phase 0/1 のどのファイルから来たかの対応表は、本文には重いが監査には要る。

推奨形式（列は最小限に）:

```
| Phase | Question | Primary files | Key evidence | Outcome |
```

追加で 2 つの補助表を置く:
- **corpus 対応表**: E01–E12 → 出典ファイル → 該当節
- **checker 一覧**: 7 本の実行可能スクリプトと、それぞれが検証した主張

本設計文書と同時に作成すると重複するため、**source map は最終本文の執筆と同時に作る**のが妥当。現時点では本設計文書がその役割を兼ねている。

---

## 13. Open items

| # | 項目 | 状態 | 扱い |
|---|---|---|---|
| **O1** | 外部校正。necessity / theorem strength が外部で既知の対象（例: 逆数学で strength が確定している定理）と、本系列の非形式的 necessity 監査を突き合わせる | **open、未実施** | 系列とは別項目。pilot 継続の理由にしない |
| **O2** | Pair B coherence。ND↔LJ の proof class 全域全単射 | **open、NOT ESTABLISHED** | informal pilot ではなく literature の coherence theorem の問題。pilot 継続の理由にしない |
| **O3** | proof-formation の **L2**（複数 corpus・別チームでの比較有用性） | **未着手** | meta-experiment §15 は「L1 または L2 が失敗した場合、annotated trajectory / review として終了する」と事前登録していた。L1 は通過、L2 は未実施。したがって現在の終了は **事前登録された gate に適合した終了**であり、恣意的な打ち切りではない |

**O3 は最終記録で強調する価値がある。** 系列が「疲れて止まった」のではなく、自ら定めた evidential ladder の規定どおりに annotated trajectory として閉じたことを示すからである `[SD]`。

---

## 14. Historiography controls

最終記録の執筆時に守る規則。各項目に、具体的な違反の形を添える。

| 制御 | 守る内容 | 具体的な違反例（避けるべき書き方） |
|---|---|---|
| **後知恵の排除** | 各 phase 時点の期待を、その時点の source から書く | 「当初から標準用語へ還元されると分かっていた」/ Phase 0 に Phase 7 の Option 2 を先取りさせる |
| **目的論の排除** | 全てが cross-calculus pilot へ向かっていたように書かない | 「この問いは必然的に proof identity へ至った」/ 放棄された枝を伏線として描く |
| **放棄仮説の保存** | 当時 reasonable だった仮説を、当時の理由とともに残す | 前提スタック、web of constraints、self-state 記録、minimal separator を「最初から筋が悪かった」と書く |
| **失敗した語彙の保存** | 導入理由と退役理由を対で残す | 退役語彙を最終記録から消して、最初から標準語だったように見せる |
| **不確実性の保存** | NOT ESTABLISHED / OPEN / unsupported を後から YES/NO にしない | Pair B の global bijection を「おそらく成立する」と書く / IVT の完全性必要性を確定させる |
| **source 順序の保存** | 後の audit を前の phase の根拠に使わない | Phase 7 の判定で Phase 2 の reader を評価する / Phase 5 の evidence-burden で Phase 0 を説明する |
| **phase 番号の衝突回避** | 本設計の Phase 0–7 と Phase 7 audit の A–F を明示的に対応づける | 番号を混用して読者に別系列と誤認させる |
| **密度の開示** | Phase 2–7 が約 45 時間に集中していること、独立再検証がないことを書く | 長期にわたる漸進的研究のように見せる |
| **自己監査の限界の開示** | Phase 7 の audit は系列内で書かれた | 「独立監査により検証された」と書く |

---

## 15. 最終結論候補文の評価

提示された候補:

> この実験は、定理の内部に隠された本質を発見して終わったのではない。定理の周囲に置かれていた問いを一つずつ検査し、それぞれがどの論理形式を持ち、何を固定し、どの証拠を要求する問いなのかを切り分けたところで終わった。

**判定: needs revision（内容は supported だが射程が狭すぎる）。**

支持される点 `[SD]`: 後半（Phase 5–7）の記述として正確であり、essence 発見譚を否定する姿勢も source に忠実である。

修正が必要な点:

1. **起源を落としている。** 系列は定理から始まっていない。観測・予測の成功と存在論的一意性の分離から始まり、対象が 3 回交代した。「定理の周囲の問い」だけでは Phase 0（20 ファイル）と Phase 2–4（22 ファイル）が入らない。
2. **反復の性質を落としている。** 各枝は「問いを切り分けた」だけでなく、**既存分野の語彙へ繰り返し吸収された**。これは系列で最も再現性の高い出来事である。
3. **「終わった」の根拠を落としている。** 終了は消耗ではなく、事前登録された gate（O3）に適合した閉じ方である。

**提案する最終文**（source に最も忠実な形）:

> この実験は、観測や証明の奥に隠れた本質を見つけて終わったのではない。成功する道具、成立した定理、書かれた証明のそれぞれについて、その周囲に置いていた問いを一つずつ形式化し、どの論理形式を持ち、何を先に固定させ、どの証拠を要求するのかを切り分け、そのたびに問いが既存分野の標準的な語彙へ戻っていくのを記録したところで終わった。残ったのは新しい理論ではなく、主張の型に証拠の型を合わせるという監査規律だけである。

代替（短縮版、章末用）:

> 残ったのは、定理の中身についての新しい知識ではなく、主張の論理形式に証拠の形式を合わせるという規律だけだった。

---

## 16. v1.1 revision scope の妥当性

Phase 7 の勧告は 2 点のみ:
(a) `what_fails_if_removed` を proof failure / non-derivability / setting change に分ける、
(b) `proof_resources` に citation / expansion depth の注記を加える。

**source chain 全体から見て妥当。** 検証:

- (a) の必要性は Phase 5 test 1–2 が直接示す（lemma 削除と induction 削除が同じ欄に同じ形で書かれてしまう）。**Phase 0 起源の Erasure Test の精密化**であり、v1.1 の結論を書き換えるものではない。
- (b) の必要性は Phase 5 test 3–4 が直接示す（v1.1 の `proof_resources` は平坦なリストで「引用した定理の選んだ証明の資源」を表現できない）。
- それ以上の改変が **不要**である理由 `[SD]`: hypothesis levels、condition types、closure role の 6 クラスタ、R0/R1/R2 の survey 結果、H2 暫定支持 / H3 不支持は、Phase 2–7 のどの結果とも矛盾していない。矛盾していないものを後続 pilot の都合で書き換えると、v1.1 が独立に持っていた 21 定理分の証拠が失われる。
- **やってはいけない改変**: 退役語彙（reachability、closure、quotient invariance 等）の v1.1 への逆輸入。Phase 6 の 4 検査を v1.1 の欄へ追加すること（v1.1 は定理の条件を扱う文書であり、証明翻訳の文書ではない）。R0/R1/R2 を後続 phase の用語で再定義すること。
- **改変ではなく注記で足りるもの**: v1.1 の IVT 項が既に「上限性は証明資源であり、B とは別の関数仮定ではない」と書いている事実は、Phase 5 test 3 が長い手続きで再導出した内容と同じである。これは v1.1 の側に注記を足すのではなく、**最終記録の側で「Phase 5 は v1.1 が既に持っていた区別を再導出した」と書く**のが正しい扱いである。

結論: **revision scope は narrow のままで妥当。追加の改変は推奨しない。**

---

**End of source architecture.** 本文は書いていない。新しい framework、score、taxonomy、geometry、metaphysics は導入していない。退役済み project-local vocabulary は §4 の用語史の中でのみ、退役済みと明示して言及した。既存ファイルは変更していない。

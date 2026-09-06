# Proof-Formation Meta-Experiment v0.1

- **Status:** working framework / exploratory meta-experiment / not a theorem
- **Date:** 2026-09-04
- **Scope:** `notes/` に保存された「道具の真理不在性」研究系列と `theorem_proof_anatomy` 系列の、source-bounded な比較再構成
- **Primary object:** 壊れた定理候補・仮説候補が、証明可能、比較可能、経験的に検査可能、または明示的に撤回可能な地点へ至るまでの変形記録
- **Novelty posture:** 新しい定理、証明論、普遍的 proof-formation theory、Gödel I / II の一般化を主張しない
- **Vocabulary posture:** 標準用語を優先する。`proof landscape`、`geometry`、`closure`、`shrinkage` などは、標準数学的構造が確認されない限り説明用の作業語に限る

## Evidence labels used in this note

- **[SOURCE-DERIVED]** 下記 source の本文、差分台帳、明示された status / verdict / kill criterion から直接確認できる記述。
- **[INFERENCE]** 複数 source を比較するために本稿が与える分類、順序づけ、または再構成。source 自身の主張ではない。
- **[OPEN HYPOTHESIS]** 今後の有限実験でのみ評価される候補。現時点の結論ではない。

一つの段落に複数ラベルが関係する場合、最も強いものを明記する。source の記述と本稿の分析を同じ声で書かない。

# 1. Purpose

**[SOURCE-DERIVED]** 「道具の真理不在性」系列は、普遍的不可能定理の候補を、反例、先行研究、型の混同、循環的定義、実例比較によって順次撤回・縮小した記録である。とくに後半では、追加条件によって初期直観を救うよりも、field-native terminology を優先し、Erasure Test と kill criteria によって固有語彙・方法論候補を降格または終了している。

**[SOURCE-DERIVED]** `theorem_proof_anatomy` 系列は、通常の定理、Gödel I / II、Tarski、Löb、GL、reflection、Turing–Feferman progressions、GLP、proof-theoretic ordinal、theory-strength relations を通じて、定理の仮定、証明資源、言語・理論・メタ理論、formula class、保存性、解釈可能性、順序数校正などを区別した。後半の stress test は、独自の比較語彙を標準 proof theory の代替にせず、説明用索引へ降格する negative result も明示している。

**[INFERENCE]** 本稿の目的は、両系列から普遍法則を抽出することではない。最小目的は、ある claim candidate が壊れたときに、次の四項を追跡できる correction ledger を作ることである。

1. 何が主張され、どの proof / evidence obligation が未充足だったか。
2. 何がその候補を壊したか。
3. 実際にどの変形または disposition が選ばれたか。
4. 変形後に何が残り、何が失われ、どの status で固定されたか。

この ledger は「証明を自動生成する方法」ではなく、研究判断の訂正可能性を保存するための記述枠である。

# 2. Non-claims

本稿は次を主張しない。

- proof formation に一つの普遍法則がある。
- claim の縮小が常に正しい、最小費用である、または全研究に一般化できる。
- 下記 move が完全、排他的、順序づけ可能、または互いに独立である。
- move に数値的距離、計量、vector-space structure、幾何学的構造がある。
- `K / A / R / D / U` が scalar、独立軸、加法的量、または最適化目的を構成する。
- Gödel I / II、Tarski、Löb、reflection の結論が、一般の研究過程や科学的方法へそのまま移る。
- theory extension による可証性が、元理論内での可証性を回復する。
- stronger theory、larger ordinal、longer progression、stronger reflection が一つの共通尺度で並ぶ。
- prior-art absorption が、元の問いの歴史的無価値や研究上の無価値を意味する。
- negative result を別の語で言い換えれば positive result になる。
- source に書かれた時系列が、合理的選択の因果系列や一意の論理依存を自動的に与える。
- 本稿または source 系列が VED を証拠的に支持する。

`proof-closing move` は、証明成功だけを意味しない。本稿では、対象を明確な条件付き定理、保存性・解釈可能性等の比較問題、有限な経験的検査、review/synthesis、または明示的 negative result へ移して未定義の obligation を閉じる disposition も含む。ただし、それぞれの終端型を同一視しない。

# 3. Source material

## 3.1 Inventory rule and source boundary

**[SOURCE-DERIVED]** 以下は `notes/` 内で「道具の真理不在性」本流、そこから明示的に派生した case / review / baseline / research plan、ならびに `theorem_proof_anatomy/` の全 Markdown source を対象にした。`README.md` と別主題の `barrier_ja.md` は inventory から除外した。

**[INFERENCE]** 同日ファイル間には時刻情報がないため、同日の並びは本文の `parent`、`source`、`revised note`、`先行`、`next step` による論理的依存順であり、厳密な作成時刻ではない。

参照されるが現在の `notes/` に存在しない `validation_basis_transition_case_01_hydro_feasibility_v0.1.md` と `deferred_resolution_case_01_gst_adversarial_review.md` は未読 source として補完せず、inventory 外とする。`tool_truth_absence_v0.1_to_v0.2_diff.md` が言及する外部査読ファイルも、当該 diff に記録された範囲を越えて推測しない。

## 3.2 「道具の真理不在性」系列 — 本流と検証枝

以下はすべて **[SOURCE-DERIVED]** の inventory である。

| Order | File | Research series | Main question | Initial claim / target | Final status | Negative result? | Main change toward next file |
|---:|---|---|---|---|---|---|---|
| 1 | [`tool_truth_absence_working_note.md`](../00_origin/tool_truth_absence_working_note.md) | TTA v0.1 本流 | 予測成功から生成構造・存在論的一意性へ進めるか | 非単射、内部性、生成–ログ、資源極限等から一般定理を探す | working synthesis。普遍 claims を撤回し、前提 stack と訂正履歴を残す | **Yes** — Phase 0–9 の多数の conjecture を撤回 | 一般 interface equivalence、線形 stack、先行研究との関係を再監査 |
| 2 | [`tool_truth_absence_v0.1_to_v0.2_diff.md`](../00_origin/tool_truth_absence_v0.1_to_v0.2_diff.md) | v0.1→v0.2 revision ledger | 査読が指摘した過剰主張をどう訂正するか | v0.1 の Phase と撤回履歴を保存しつつ精密化 | conservative correction ledger | **Yes** — general interface equivalence 等を追加撤回 | stack→network、within-model ID / class adequacy、CIF / independence / EA を分離 |
| 3 | [`tool_truth_absence_working_note_v0.2.md`](../00_origin/tool_truth_absence_working_note_v0.2.md) | TTA v0.2 本流 | 補助条件の非自己証明性を network として監査できるか | prerequisite network が具体例で診断力を持つ可能性 | corrigible synthesis / not a theorem。方法論価値は未実証 | **Yes** — 普遍不可能性、線形 hierarchy、新規 theorem を否定 | 量子論を adversarial case とし、prior art を先に再構成 |
| 4 | [`scientific_identifiability_case_01_quantum.md`](../00_origin/scientific_identifiability_case_01_quantum.md) | Quantum Case 01 | v0.2 network は量子論で追加診断を生むか | weak usefulness / methodological value を事前区別 | mixed。弱い整理上の usefulness は narrowly pass、methodological value は未通過 | **Yes** — 新しい量子区別・定理・実験判断は得られず | preparation、calibration、copy、query granularity を分け、prior-art reconstruction へ |
| 5 | [`quantum_identifiability_prior_art_network.md`](../00_origin/quantum_identifiability_prior_art_network.md) | Quantum prior-art branch | v0.2 に近い構造は既存量子研究だけで再構成できるか | field-native network を先に再構成 | Type B with strong Type A。organizational value plausible、methodological value unproven | **Yes** — local nodes / edges の大半は既存研究の方が精密 | v0.3 では ownership を既存分野へ戻し、generic terms を索引へ降格 |
| 6 | [`tool_truth_absence_v0.2_to_v0.3_diff.md`](../00_origin/tool_truth_absence_v0.2_to_v0.3_diff.md) | v0.2→v0.3 ledger | 量子ケースと prior art を本流へどう反映するか | general prerequisite network の中心性 | claim strength を減らし、assurance provenance / backgrounding / handoff へ再配置 | **Yes** — missing edge・conceptual novelty・methodological superiority を不支持 | field-native first、Erasure Test、cross-impact、controlled audit を追加 |
| 7 | [`tool_truth_absence_working_note_v0.3.md`](../00_origin/tool_truth_absence_working_note_v0.3.md) | TTA v0.3 本流 | 保証の出所・背景化・handoff を横断表示する価値はあるか | distributed assurance map / provenance の候補 | visualization / indexing / question generation が最大。framework / theorem は未確立 | **Yes** — unknown dark region や missing edge は未確立 | generic vocabulary を実例で消す GST stress test へ |
| 8 | [`deferred_resolution_case_01_gst.md`](../00_origin/deferred_resolution_case_01_gst.md) | GST / Deferred Resolution v0.1 | resolution→boundary relocation が GST で反復するか | DR-1 weak relocation を best fit とする provisional positive reading | working case。linear recurrent chain は失敗、局所 branching のみ | **Yes, partial** — DR-2–DR-4 不成立、ordinary refinement が最強説明 | adversarial Erasure Test と field-native reconstruction を要求 |
| 9 | [`deferred_resolution_case_01_gst_adversarial_review_codex.md`](../00_origin/deferred_resolution_case_01_gst_adversarial_review_codex.md) | GST adversarial review | DR を消して何が失われるか | DR-1 を独立概念として残せるか | description は presentation-only、methodology は no | **Yes** — technical / diagnostic loss なし | metrology を closure counterexample を含む次の test に提案 |
| 10 | [`deferred_resolution_case_01_gst_adversarial_review_claudecode.md`](../00_origin/deferred_resolution_case_01_gst_adversarial_review_claudecode.md) | GST second adversarial review | field-native reconstruction が DR を完全吸収するか | recurrent relocation / DR taxonomy | DR は捨てるべき再命名。handoff の経験的問いだけ残す | **Yes** — Erasure 後にむしろ精度上昇 | nuisance promotion、quotient、model checking / extension へ全面再記述 |
| 11 | [`deferred_resolution_case_01_gst_v0.1_to_v0.2_diff.md`](../00_origin/deferred_resolution_case_01_gst_v0.1_to_v0.2_diff.md) | GST revision ledger | reviews をどう negative-result freeze へ反映するか | v0.1 の weak-positive DR reading | conservative negative-result freeze | **Yes** — taxonomy、単線、ontological closure、positive verdict を削除 | Null A/E と Erasure negative を v0.2 へ固定 |
| 12 | [`deferred_resolution_case_01_gst_v0.2.md`](../00_origin/deferred_resolution_case_01_gst_v0.2.md) | GST v0.2 | distinct DR mechanism は残るか | field-native 語彙を対照にした最終 test | **Frozen negative result** | **Yes** — DR mechanism / diagnostic value を不支持 | future case に field-native control と diagnostic difference を必須化 |
| 13 | [`tool_truth_absence_v0.3_to_v0.4_diff.md`](../00_origin/tool_truth_absence_v0.3_to_v0.4_diff.md) | v0.3→v0.4 ledger | GST negative を本流へ最小反映するか | DR を新概念として追加する可能性 | minor correction / negative calibration。DR 不採用 | **Yes** | Erasure rule を強化し、handoff loss を別の経験的問いとして metrology へ |
| 14 | [`tool_truth_absence_working_note_v0.4.md`](../00_origin/tool_truth_absence_working_note_v0.4.md) | TTA v0.4 本流 | generic audit は field-native control を越えるか | assurance provenance を暫定 index として保持 | theorem なし。methodology 未確立。GST を negative baseline として保存 | **Yes** — DR、boundary mechanism、visualization=methodology を撤回 | metrology の preregistered head-to-head test へ |
| 15 | [`scientific_assurance_case_02_metrology_preregistration.md`](../00_origin/scientific_assurance_case_02_metrology_preregistration.md) | Metrology Case 02 design | generic transfer audit は native metrology を越えるか | H0 field-native sufficiency、H1 unique loss diagnosis、H2 explicit preservation | frozen preregistration | Negative を完全結果として許容 | control→generic audit の順、F1–F6、M0–M3 を事前固定 |
| 16 | [`scientific_assurance_case_02_metrology_control_reconstruction.md`](../00_origin/scientific_assurance_case_02_metrology_control_reconstruction.md) | Metrology native control | native concepts だけで三 chain を診断できるか | traceability / uncertainty / decision rules の再構成 | completed frozen control。native concepts で必要区別を回収 | **No independent positive for generic method** | 同一 corpus に generic audit を適用 |
| 17 | [`scientific_assurance_case_02_metrology.md`](../00_origin/scientific_assurance_case_02_metrology.md) | Metrology generic audit | generic ledger が独自 finding を出すか | handoff loss / transfer preservation の探索 | M1 provisional。organizational value only | **Yes** — H1 not supported、M2/M3 不成立 | head-to-head で false positives と closure counterexample を確定 |
| 18 | [`scientific_assurance_case_02_metrology_comparison.md`](../00_origin/scientific_assurance_case_02_metrology_comparison.md) | Metrology final comparison | diagnosis / scope / decision / retrieval は変わったか | generic audit の methodological added value | H0 retained、H1 not supported、H2 corpus 内で supported、最終 M1 | **Yes** — generic-only diagnosis なし | 実 record の paired audit 以外では拡張しない |
| 19 | [`web_of_constraints_methodology_adversarial_review.md`](../00_origin/web_of_constraints_methodology_adversarial_review.md) | Web of Constraints review | claim/evidence/scope/transport の一般 framework は成立するか | web / observability map / claim transport methodology | theorem/formal noveltyなし、conceptual low、methodological unproven | **Yes** — existing frameworks への高い absorption risk | claim-centered controlled comparison だけを候補として残す |
| 20 | [`web_of_constraints_methodology_second_order_review_claudecode.md`](../00_origin/web_of_constraints_methodology_second_order_review_claudecode.md) | second-order review | 横断構成自体にも prior art があるか | framework を最低限救えるか | framework としては dead。transport-license review と一件の empirical hypothesis のみ | **Yes** — boundary object / context-of-use にも吸収 | claim individuation と two-sided native controls を中心にさらに縮小 |
| 21 | [`validation_basis_transition_working_note_v0.1.md`](../00_origin/validation_basis_transition_working_note_v0.1.md) | Validation Basis restart | source→target reuse の material・unstated change を incremental に検出できるか | universal map でなく artifact-level omission の head-to-head test | research program only。negative controls 2、positive 0、one narrow empirical question | **Yes** — prior hypothesesを demotion log に固定 | time-sliced hydrology artifact search と preregistered comparisonへ |
| 22 | [`case_01_hydro_target_artifact_discovery_v0.1.md`](../00_origin/case_01_hydro_target_artifact_discovery_v0.1.md) | Hydro artifact branch | audit-ready な地点固有 source–target chain は取得可能か | HYD-A01 を含む document-chain discovery | search ledger only。partial chain / archive gap、判定禁止 | **Not yet a hypothesis result** | readiness gate を通るまで audit へ進まない |
| 23 | [`hydrology_negative_knowledge_preservation_note_v0.1.md`](../00_origin/hydrology_negative_knowledge_preservation_note_v0.1.md) | Hydrology documentary branch v0.1 | failure / limitation は保存・再利用されたか | negative-knowledge preservation mechanisms | B: partial preservation history identified。ただし efficacy 未確認 | **Yes** — disaster-origin、暗黙化、効果を確認できず | factual review と generic baseline を要求 |
| 24 | [`qualification_practices_comparative_study_design_v0.1.md`](../00_origin/qualification_practices_comparative_study_design_v0.1.md) | Qualification comparison design | hydrology の形式は他 guidance と異なるか | 14 codes を複数分野で比較する B-level plan | viable comparative review、methodological value unproven、D risk high | Negative を予定済み | まず安価な P0 を実行し、早期 kill を許可 |
| 25 | [`hydrology_negative_knowledge_preservation_note_v0.2.md`](../00_origin/hydrology_negative_knowledge_preservation_note_v0.2.md) | Hydrology documentary branch v0.2 | limitation 等がどう記載・変更・参照されたか | preservation を前提にする語り | documentary continuity identified; preservation effectiveness untested | **Yes** — 事実誤り2、内部矛盾1、固有性を大幅撤回 | P0 で generic standards baseline を検査 |
| 26 | [`p0_generic_standards_baseline_v0.1.md`](../00_origin/p0_generic_standards_baseline_v0.1.md) | P0 kill test | hydrology codes は generic standards にもあるか | 14-code comparative program | C: organizational synthesis only。実質 `NONEVAL` 1、`RET-DOWN` 未検査 | **Yes** — 10/14 generic、2 artifact-type | full P1–P5 を選ばず `NONEVAL` 一問だけへ縮小 |
| 27 | [`p1r_noneval_two_field_check_v0.1.md`](../00_origin/p1r_noneval_two_field_check_v0.1.md) | P1-reduced kill test | `NONEVAL` は分野固有の差か | metrology / GRADE との二分野 check | comparative methodology を terminate、comparative review へ降格 | **Yes** — artifact type + governance、実質 n=1 | full comparison を中止。個別 hydrology note の訂正だけ残す |
| 28 | [`tool_truth_absence_research_trajectory_summary.md`](../00_origin/tool_truth_absence_research_trajectory_summary.md) | retrospective trajectory | 普遍定理探索から現在まで何が残ったか | 系列全体の source-bounded summary | narrow empirical comparison only。自己訂正規律が最大の残存物 | **Yes** — strong/general readings を列挙して否定 | current snapshot。次は限定的 controlled comparison のみ |
| 29 | [`tool_truth_absence_research_trajectory.svg`](../00_origin/tool_truth_absence_research_trajectory.svg) | companion visualization | 上記 trajectory を図示する | narrative overview | visual artifact。独立の claim / evidence は持たない | No independent result | 本稿では内容根拠でなく navigation aid としてのみ扱う |

## 3.3 `theorem_proof_anatomy` 系列

この系列には日付がない。以下は主文書から、各 stress test が本文で明示する継承関係と、依頼で指定された順序に沿う。全項目は **[SOURCE-DERIVED]** である。

| Order | File | Research series | Main question | Initial claim / target | Final status | Negative result? | Main change toward next file |
|---:|---|---|---|---|---|---|---|
| P0 | [`theorem_proof_anatomy_v1.1_ja.md`](../01_theorem_anatomy/theorem_proof_anatomy_v1.1_ja.md) | 21 theorem anatomy | 仮定の機能、proof resources、条件除去後を横断比較できるか | closure / escape / residual の比較枠 | H2: 機能分類は再現。ただし H3 的な普遍 residual pattern は未支持 | **Yes** — R2 は少数、labels は非排他的 | Gödel I / II で positive closure でない theorem を stress test |
| P1 | [`godel_incompleteness_closure_reversal_stress_test_ja.md`](../01_theorem_anatomy/godel_incompleteness_closure_reversal_stress_test_ja.md) | Gödel I / II | incompleteness と self-consistency limitation を同じ anatomy で扱えるか | 「閉包反転」候補 | C1: 比喩のみ。標準語彙が優先。G1 structural analogy | **Yes** — 一般 closure theory / R2 reading を不支持 | truth と provability を Tarski で分離 |
| P2 | [`tarski_truth_undefinability_stress_test_ja.md`](../01_theorem_anatomy/tarski_truth_undefinability_stress_test_ja.md) | Tarski | same-language truth の undefinability は何を禁止するか | internalization / semantic boundary の比較 | D1: 「断絶交渉」は比喩のみ、R1、T1 analogy | **Yes** — truth absence、一般 externality、Gödel同一視を不支持 | provability reflection を Löb で検査 |
| P3 | [`lob_theorem_reflection_stress_test_ja.md`](../01_theorem_anatomy/lob_theorem_reflection_stress_test_ja.md) | Löb | provable local reflection が何を強制するか | 「自己保証」「閉包反転」の候補 | S2 は local reflection の比較ラベルとしてのみ、C1、R1 | **Yes** — truth / soundness / general self-guarantee reading を不支持 | modal abstraction GL へ |
| P4 | [`godel_lob_provability_logic_gl_stress_test_ja.md`](../01_theorem_anatomy/godel_lob_provability_logic_gl_stress_test_ja.md) | GL | Löb 構造の何が modal level に保存されるか | arithmetic Löb の構造を GL で抽象化 | S2/C1 は限定、P2 comparison frame、E1 Erasure | **Yes** — `Box` を ordinary closure operator とする読みを否定 | local/uniform/global reflection scope を分解 |
| P5 | [`reflection_principles_scope_stress_test_ja.md`](../01_theorem_anatomy/reflection_principles_scope_stress_test_ja.md) | reflection family | local / uniform / global / consistency / soundness は同じ型か | 「自己保証」family 全体への適用 | S2* は local 限定、P2、RX、E1 | **Yes** — family-wide S2 と residual 語彙を不支持 | reflection を theory progression として反復 |
| P6 | [`turing_feferman_progressions_stress_test_ja.md`](../01_theorem_anatomy/turing_feferman_progressions_stress_test_ja.md) | Turing–Feferman | same-theory limitation と next-theory extension をどう index 化するか | moving boundary / subject–extension asymmetry | M2、A2、P2 は説明用。RX。notation dependence を強調 | **Yes** — ordinal value=stage theory、limit=reflection を否定 | GLP / worms で自然な progression の canonicalization を検査 |
| P7 | [`glp_worms_ordinal_reflection_calculus_stress_test_ja.md`](../01_theorem_anatomy/glp_worms_ordinal_reflection_calculus_stress_test_ja.md) | GLP / worms | modality、nesting、ordinal rank、stage を分けられるか | modal syntax による progression 圧縮 | C2 natural cases、M2*/A2* 限定、P2、RX、E1 | **Yes** — arbitrary progression の canonicalization、generic residual を不支持 | consistency と uniform reflection の operator 差を直接比較 |
| P8 | [`consistency_vs_uniform_reflection_progressions_stress_test_ja.md`](../01_theorem_anatomy/consistency_vs_uniform_reflection_progressions_stress_test_ja.md) | progression comparison | 同じ段数・順序数長で strength を比較できるか | consistency と uniform reflection の一本化 | same count N1、same length O1 は operator 固定時のみ。V2/P2、M1、RX | **Yes** — universal scalar / cross-operator stage measure を否定 | proof-theoretic ordinal 自体の型を監査 |
| P9 | [`proof_theoretic_ordinal_stress_test_ja.md`](../01_theorem_anatomy/proof_theoretic_ordinal_stress_test_ja.md) | ordinal anatomy | proof-theoretic ordinal は何を測り何を潰すか | theory strength の ordinal scalar 候補 | S2* は natural analysis 内、A2/P2/C2*、E1 | **Yes** — theorem set / interpretability / spectrum の universal measure を否定 | ordinal が潰す複数 order を明示 |
| P10 | [`theory_strength_order_structures_stress_test_ja.md`](../01_theorem_anatomy/theory_strength_order_structures_stress_test_ja.md) | theory-strength relations | “stronger” はどの relation か | strength vector / order bundle の候補 | O2/B2/V2 は typed audit 表、P2/C2*、M0、RX、E1 | **Yes** — universal total order / new invariant を否定 | 現段階の終端。relation と quotient を必ず指定 |

# 4. Unit of analysis

## 4.1 Claim episode

**[INFERENCE]** 最小単位を、完成した論文・理論・研究者ではなく、一つの **claim episode** とする。これは新しい論理形式ではなく、次の source fields を同じ行に置くための記録単位である。

| Field | Required content |
|---|---|
| `claim_before` | 変更前の定理候補、仮説候補、方法論 claim、または比較問い |
| `target_and_scope` | 対象、量化範囲、formula class、theory / language、model class、artifact / corpus、intended use |
| `obligation_type` | formal proof、counterexample exclusion、prior-art novelty、empirical discrimination、reproducibility、decision relevance 等 |
| `assumptions` | theorem assumptions。object / ambient / background / definitional を可能な限り区別 |
| `proof_or_evidence_resources` | proof resources、data、literature corpus、review procedure。assumptions と混同しない |
| `failure_witness` | counterexample、logical objection、prior art、Erasure result、failed control、factual correction、missing evidence |
| `available_branches` | source が明示する代替救済、縮小、別問題化、または終了候補 |
| `move_taken` | 実際に採用された変形。反実仮想の branch と分ける |
| `claim_after` | 変更後の claim / question と scope |
| `terminal_status` | proved / conditionally proved / comparative result / empirical protocol / synthesis / open / withdrawn / frozen negative |
| `provenance_label` | source-derived / inference / open hypothesis |

## 4.2 Transition, not final proof type

**[INFERENCE]** 分析対象は、完成済み証明の「型」ではなく、

```text
claim_before + obligation + failure_witness
    -> move_taken
    -> claim_after + terminal_status
```

という transition である。たとえば「compactness proof」「diagonal proof」「ordinal analysis」は完成した証明や解析の型であり、そのまま formation move ではない。formation move は、仮定を追加した、formula class を制限した、別理論へ拡張した、reduction problem に移した、または claim を撤回した、という変更側に置く。

## 4.3 Distinct terminal states

**[INFERENCE]** 次は同じ「成功」にまとめない。

1. 元 claim が元 assumptions のまま証明された。
2. assumptions または scope を変更した別 theorem が証明された。
3. full theorem でなく指定 consequence class の reduction / conservation が得られた。
4. interpretability、ordinal、strength relation の比較問題へ移った。
5. theorem question が有限な empirical / comparative question へ移った。
6. review / synthesis / indexing に降格した。
7. claim が withdrawn または frozen negative result になった。

# 5. Proof-formation moves

## 5.1 Candidate taxonomy after source audit

以下は **[INFERENCE]** の coding taxonomy であり、標準用語をできるだけそのまま使う。排他的分類ではない。一 transition に複数 move を記録してよい。

| Code | Move | Candidate-list disposition | What changes | What must not be conflated |
|---|---|---|---|---|
| M1 | Assumption strengthening | Aを保持 | theorem / claim assumptions を追加・強化する | 結論そのものの再導入、proof resource、ambient の黙示化 |
| M2 | Conclusion weakening | Bを保持 | 結論の量化、精度、一意性、必然性、一般性を弱める | 単なる言い換え、対象 class の変更 |
| M3 | Formula-class / language restriction | Cから分離保持 | `Sigma_n / Pi_n`、closed sentence、same-language 等へ制限 | object-class restriction、conservativity の結果 |
| M4 | Object / domain / model-class restriction | Dを保持 | 対象の class、dimension、finiteness、candidate class、artifact corpus を狭める | formula fragment、proof resource |
| M5 | Quotient / equivalence-class target reformulation | sourceにより追加 | representative でなく observational / gauge / interpretability degree 等を target にする | unresolved physical ambiguity、単なる conclusion weakening |
| M6 | Formal theory extension | Eを分割保持 | `T` から `T + axiom/schema`、次 stage、truth-expanded language へ移る | `T` 自身が元文を証明したという主張 |
| M7 | Model / estimand / target-class revision | Eの empirical 側を分割 | nuisance parameter の joint estimation、richer model、別 estimand へ移る | formal theory extension、元 model の失敗一般化 |
| M8 | Proof-resource addition or route change | Fを保持 | lemma、coding、compactness、cut elimination、experimental design、追加資料等を用いる | theorem assumption。resource を増やして claim を変えない場合もある |
| M9 | Reduction with specified preservation | Gを分割 | 別 calculus / progression へ proof を写し、保存する consequence class を指定 | theory equality、full deductive equivalence |
| M10 | Interpretation / translation | Gを分割 | formula / model / theory を translation 後に比較する | same-language theorem inclusion |
| M11 | Internalization | Hを保持、formal setting限定 | syntax、proof relation、substitution 等を object language / theory 内に表現する | semantic truth、外部 soundness、自己証明 |
| M12 | Metalevel shift / external evaluation | Iを分割 | truth、soundness、well-foundedness、consistency、non-provability を metatheory から評価する | internal formula/schema。reflection 追加は M6 と併記 |
| M13 | Comparison / calibration | Jを保持 | conservativity、interpretability、relative consistency、reflection rank、ordinal analysis 等へ問いを移す | universal “strength” scalar、同じ ordinal=同じ theory |
| M14 | Disambiguation / type correction | sourceにより追加 | truth/provability、local/uniform/global、stage/modality/ordinal、artifact/institution/field 等を分離 | claim strengthening。これはしばしば proof 前の問題訂正 |
| M15 | Prior-art absorption | Kを保持 | 独自 claim / vocabulary を既存 theorem、method、standard、review language へ戻す | 歴史的因果の断定、研究価値全体の否定 |
| M16 | Conversion to empirical / comparative question | Jから独立化 | theorem / framework novelty の問いを control comparison、document audit、finite test へ移す | theorem proof、単なる case illustration |
| M17 | Withdrawal / abandonment / negative-result fixation | Lを保持 | claim を撤回、降格、終了、または frozen negative として保存 | “別名で復活”、未検証を反証済みとすること |

`reflection` は単一の汎用 move code にしない。single local reflection を同じ `T` が証明する場合、外部から `RFN_Gamma(T)` を加えて `T+RFN_Gamma(T)` を作る場合、truth-expanded language で global reflection を置く場合、external soundness を仮定する場合は型が違う。必要に応じて M3、M6、M11、M12を組み合わせ、reflection scope を明記する。

## 5.2 Controls and observations that are not moves

以下は **[SOURCE-DERIVED]** の区別に基づく **[INFERENCE]** である。

| Item | Role | Why it is not itself a formation move |
|---|---|---|
| Counterexample | failure witness | claim を壊すが、その後にどの修正を選ぶかは決めない |
| Prior art | novelty / coverage witness | M15を動機づけるが、exact / partial / analogue の判定が別に要る |
| R0 / R1 / R2 | condition-removal observation | 条件を外した後の挙動であり、proof obligation を移す操作ではない |
| Conservation | comparison result | M9/M13の成否を表す relation。assumption でも proof type の万能名でもない |
| Interpretability | translation-based relation | M10/M13の対象。theorem inclusion と同じではない |
| Ordinal calibration | fixed analysis package 上の result | M13の出力。progression length や universal theory strength ではない |
| Erasure Test | ablation / naming control | 独自語彙を消した際の情報・判断差を調べる。claimを直接証明しない |
| Kill criterion | stopping / demotion rule | 研究継続の disposition を決める。発火後の M17 と区別する |

## 5.3 Assumptions and proof resources

**[SOURCE-DERIVED]** theorem anatomy の最も再利用可能な区別は、定理文に必要な assumptions と、そこから結論を導く proof resources を分けることである。さらに assumptions は少なくとも次へ分ける。

- `object`: 対象そのものの性質。連続性、線形性、理論の効果的公理化など。
- `ambient`: 有限次元空間、言語、基礎論理、base theory などの舞台。
- `background`: metatheory、標準意味論、well-foundedness の外部評価など。
- `definitional`: 非退化条件、provability predicate、formula class、ordinal notation、comparison relation の固定など。

**[INFERENCE]** formation ledger では、M1 と M8 を同じ `added condition` 欄へ入れてはならない。たとえば diagonal lemma、partition of unity、Henkin construction、Solovay function は代表 proof resources であり、元 theorem statement の assumptions ではない。一方、formula class、provability predicate、candidate class、same-language restriction は target または definition の一部であり、証明道具ではない。

# 6. Shrinkage trajectory case study

## 6.1 Branch-preserving trajectory graph

次の図は **[SOURCE-DERIVED]** の明示的 parent / next question / revision relation を骨格とし、配置だけを **[INFERENCE]** として与える。`not chosen` は source が代替条件または救済可能性を明示したが、本流の普遍 claim の継続には採用しなかった branch である。

```text
N0  Predictive success -> unique generating structure / ontology?
 |
 +-> N1  Non-injective observation map theorem candidate
 |       |-- prior art + identity counterexample -> universal novelty withdrawn
 |       `-- retain: model- and experiment-relative identifiability
 |
 +-> N2  Self-containment -> universal non-identifiability?
 |       |-- finite self-recording / recursion counterexamples -> withdrawn
 |       |-- [not chosen rescue] finite proper-subsystem capacity assumptions
 |       `-- retain: conditional capacity / query conditions matter
 |
 +-> N3  Generation -> stabilization -> log forces non-isomorphism?
 |       |-- circular if loss is built into “stabilization”; reversible encodings exist
 |       |-- [not chosen rescue] stipulate a lossy channel
 |       `-- retain: prove information loss for a specified channel/statistic
 |
 +-> N4  Resource growth leaves a persistent ontological fiber?
 |       |-- finite separation and limit-point counterexamples -> universal claim withdrawn
 |       `-- retain: resource/model/topology-relative fiber notation
 |
 +-> N5  Pairwise experiments vs one realizable adaptive history
 |       |-- two-bit destructive example establishes quantifier/composition gap
 |       |-- not internal-observer-specific
 |       `-- [not chosen rescue] fresh preparation / product closure
 |
 +-> N6  Experimental amalgamation / common refinement
 |       |-- narrow finite deterministic informational equivalence retained
 |       |-- physical joint realizability separated
 |       `-- no new general theorem
 |
 +-> N7  Internal/external interface equivalence
 |       |-- v0.1 overstates a general established result
 |       `-- v0.2 correction: stipulative equality vs implementation theorem separated
 |
 +-> N8  “Interface factorization” split into CIF and EA
 |       `-- dynamic causal shielding, preparation independence, composition separated
 |
 +-> N9  Diagonal adversary / randomness / initial correlation
 |       |-- internality alone insufficient
 |       |-- [not chosen rescue] code visibility, query closure, no private randomness, etc.
 |       `-- theorem search exits toward an assumption audit
 |
 `-> N10 prerequisite stack -> prerequisite network
         |
         +-> N11 Quantum case + prior-art reconstruction
         |       `-- existing local networks dominate -> generic terms become indexes
         |
         `-> N12 distributed assurance / provenance / handoff (v0.3)
                 |
                 +-> N13 GST “Deferred Resolution” case
                 |       |-- provisional DR-1 description
                 |       `-- Erasure + prior art -> frozen negative (v0.2)
                 |
                 +-> N14 v0.4 -> Metrology preregistration/control/audit
                 |       `-- H1 rejected; M1 organizational only; closure counterexample
                 |
                 `-> N15 Web of Constraints proposal + two adversarial reviews
                         |-- framework / universal map abandoned
                         `-> N16 Validation Basis: artifact-level comparative question only
                                |
                                +-> N17 Hydro artifact discovery: partial chain; no verdict
                                |
                                `-> N18 Hydrology documentary branch
                                       |-- “preservation” -> documentary continuity only
                                       |-- P0: 10/14 generic; full comparison not chosen
                                       `-- P1-reduced: n=1 + governance/artifact null
                                           -> comparative methodology terminated

N19 current snapshot:
    one narrow, preregistered, time-sliced, head-to-head empirical question remains;
    otherwise retain review, negative calibrations, Erasure and kill discipline.
```

## 6.2 Node ledger

各行の target、failure witness、actual disposition、remnant は **[SOURCE-DERIVED]**、それらを一つの node に束ねたこと、M-codeへの割当、flags は **[INFERENCE]** である。

Flags: `W` claim weakened、`A` assumption added in the **chosen main move**、`S` scope restricted、`F` reformulated、`P` prior-art absorption、`E` theorem/framework question converted to empirical/comparative question、`X` claim abandoned or negative-fixed。`no` は代替 branch に条件追加がなかったという意味ではなく、本流で救済条件として採用しなかったことを指す。

| Node | Target claim | What failed / witness | Actual move taken | Flags W/A/S/F/P/E/X | What remained |
|---|---|---|---|---|---|
| N0 | success から unique ontology へ進めるか | prediction、ID、generator uniqueness、ontology を一矢印にしていた | M14で命題を分離 | yes/no/yes/yes/no/no/no | 各 bridge assumption を問う research question |
| N1 | non-injective `O` から新しい universal theorem | `O=id`、非単射なら左逆なしは初等的、inverse problems 等 | M15 + M17、結論を model-relative ID へM2/M4 | yes/no/yes/yes/yes/no/yes | observational equivalence と structural equivalence の区別 |
| N2 | self-containment alone -> non-ID | finite internal encoder、infinite cardinality、recursion theorem。Breuer/Wolpert は追加条件付き | universal implication をM17、条件付き capacity resultだけ保持 | yes/no/yes/yes/yes/no/yes | self-containment は追加条件を活性化しうるが十分でない |
| N3 | stabilization/logging が必ず情報損失 | loss を定義へ入れる循環、可逆・完全符号化例 | M14 + M15 + M17 | yes/no/yes/yes/yes/no/yes | specified channel/statistic ごとの sufficiency / loss question |
| N4 | resource infinityでもfiberが必ず残る | finite candidate の有限分離、無限候補の極限一点化、class dependence | M2/M4/M13 + M17 | yes/no/yes/yes/yes/no/yes | resource-bounded / asymptotic ID の条件付き記法 |
| N5 | destructive single-history failureは内部性固有 | 同じ interface の external observer でも失敗。fresh preparationなら消える | M14で location と resource/composition を分離 | yes/no/yes/yes/yes/no/yes(part) | `forall-exists` と `exists-forall`、共同実現可能性の差 |
| N6 | amalgamation が一般境界 theorem を与える | finite deterministic では初等的、probabilistic / physical cases は別構造 | M3/M4で狭い情報命題のみ保持、M14 | yes/yes/yes/yes/yes/no/yes(part) | narrow common-refinement equivalence と open formalization |
| N7 | same informal interface -> internal/external equivalence | definition上の equality と実装対応を混同 | v0.2でM14 + M17。一般 `[ESTABLISHED]` を撤回 | yes/no/yes/yes/no/no/yes | inside/outside label alone では差を導けない |
| N8 | CIF と EA は同じ interface condition | 二ビット例等で非含意、initial independence も別 | M14で三者を型分離 | yes/no/yes/yes/yes/no/yes(part) | causal shielding、preparation independence、composition の別監査 |
| N9 | internality + diagonalization / randomness で固有限界 | external code leakageでも同じ、private randomnessなら反例不能、candidate 後付け禁止 | universal claimをM17、M14で causal assumptions へ | yes/no/yes/yes/yes/yes/yes | conditional adversarial / causal-interface questions |
| N10 | fixed prerequisite stack | conditions が代替、支援、feedback、cross-impact を持つ | stack→networkへM14、次にM16で case test | yes/no/yes/yes/no/yes/no | audit inventory。普遍 hierarchy ではない |
| N11 | network に量子論で独自診断力 | quantum content は largely reclassification、prior art がより精密 | M15、M14、organizational claimへM2 | yes/no/yes/yes/yes/yes/no | Type B / cross-domain indexing candidate |
| N12 | assurance provenance が独自 framework | missing edgeもmethod valueも未実証、強い assurance prior art | M15で field ownershipへ戻し、M16で実 testへ | yes/no/yes/yes/yes/yes/no | provenance/backgrounding/handoff の provisional index |
| N13 | GST が recurrent Deferred Resolution を示す | quotientでgauge closes、model extensionsは別枝、年代も単線でない、Erasureで精度上昇 | M5/M7/M15/M17、frozen negative | yes/no/yes/yes/yes/yes/yes | nuisance promotion、quotient ID、model checking / extension |
| N14 | generic handoff auditがmetrologyを越える | frozen native controlが全 finding を先取り、generic側false-positive risk、2019 SI closure | M13/M16後、H1をM17、M1にM2 | yes/no/yes/yes/yes/yes/yes(part) | organizational index、actual-practice auditはopen |
| N15 | Web of Constraints が methodology/framework | SACM等だけでなく boundary object / context-of-use も強い先行形。claim individuation 不安定 | M14/M15/M17、transport-license reviewと経験仮説へM16 | yes/no/yes/yes/yes/yes/yes | field-native controls に対する diagnostic delta question |
| N16 | broad validation / transport program | conceptual components mostly prior art、negative controls 2、positive 0 | artifact-level omissionへM2/M4/M16 | yes/no/yes/yes/yes/yes/yes(part) | time-sliced source–target comparison research plan |
| N17 | hydrology positive/negative audit | minimum document chain未完成、materiality/bridge未評価 | readiness scopeを固定し判定保留 | yes/no/yes/yes/no/yes/no | partial chainと検索・selection ledger |
| N18 | negative knowledge preservation と分野固有 mechanism | factual errors、efficacy未測定、10/14 generic、`NONEVAL` はgovernance/artifact+n=1 | M14/M15/M17。documentary continuityへM2、methodology終了 | yes/no/yes/yes/yes/yes/yes | comparative review、個別 documentary facts、search failure lesson |
| N19 | current general method | diagnostic delta未観測、terms/units未確定 | これ以上の概念増加を止め、finite Phase 0だけを提案 | yes/no/yes/yes/yes/yes/no | correction ledger の検査可能性という最小 open question |

## 6.3 Main transition-to-move correspondence

以下は作業4に対する **[INFERENCE]** の対応表である。`failure witness` 自体は move に数えない。

| Transition | Source-observed sequence | Move codes |
|---|---|---|
| N0→N1 | broad philosophical question → observation map | M14, M4 |
| N1→N2 | universal nonuniqueness → identity counterexample / prior art → model-relative ID | M2, M4, M15, M17 |
| N2→N3 | self-containment theorem → self-recording counterexample → conditional capacity only | M2, M4, M14, M15, M17 |
| N3→N4 | generic logging loss → circularity / reversible example → specified-channel question | M4, M14, M15, M17 |
| N4→N5 | persistent fiber → model/resource dependence → quantifier-order problem | M2, M4, M13, M14, M17 |
| N5→N6 | pairwise separators → destructive-history obstruction → composition/refinement question | M4, M8, M13, M14 |
| N6→N7 | general amalgamation hope → narrow elementary theorem → interface comparison | M3, M4, M14, M15 |
| N7(v0.1)→N7(v0.2) | “same interface” established claim → stipulation/implementation conflation | M14, M17 |
| N7→N9 | inside/outside → CIF/EA split → causal assumptions | M14, M4, M15 |
| N9→N10 | conditional diagonal limitations → no universal theorem → assumption audit network | M2, M14, M16, M17 |
| N10→N11 | generic prerequisite network → quantum case → native distinctions dominate | M14, M15, M16 |
| N11→N12 | network ownership → prior-art reconstruction → provenance/index only | M2, M14, M15 |
| N12→N13 | new generic vocabulary → GST reconstruction → Erasure → frozen negative | M5, M7, M14, M15, M17 |
| N13→N14 | negative calibration → stricter preregistered native-control comparison | M13, M16 |
| N14→N15 | generic audit M1 only → wider web proposal → adversarial prior-art absorption | M2, M14, M15, M16, M17 |
| N15→N16 | methodology proposal → framework dead → artifact-level empirical question | M2, M4, M14, M15, M16, M17 |
| N16→N17 | broad claim extension question → audit-readiness document search | M4, M16 |
| N16→N18 | preservation story → factual correction → documentary continuity | M2, M4, M14, M15 |
| N18→P0 | 14-code comparison → generic baseline → one live code | M4, M13, M15, M16 |
| P0→P1r | full P1–P5 possible → deliberately not chosen → one-code kill test | M4, M16 |
| P1r→N19 | remaining difference → governance/artifact+n=1 → methodology termination | M14, M15, M17 |

# 7. Alternative rescue branches

この節は、source が実際に示した代替条件と、本稿の counterfactual inference を分ける。

| Episode | Available rescue | Source status | Why the main trajectory did not use it |
|---|---|---|---|
| Non-injective observation | `O` が非単射となる class / experiment family を仮定する | **[SOURCE-DERIVED]** 非単射なら非一意は成立 | それは条件付きの既知 identifiability result であり、class-independent theorem や novelty を救わない |
| Self-containment | finite world、proper-subsystem record、all-state target、capacity bound を追加 | **[SOURCE-DERIVED]** 条件付き容量命題として明示 | self-containment 単独という元仮説を救わず、追加条件が仕事をするため。本流は普遍含意を撤回 |
| Generation–log | stabilization を many-to-one / coarse-graining と定義 | **[SOURCE-DERIVED]** 可能だが循環と判定 | 結論を定義へ埋め込む trivial rescue だから不採用。specific channel で証明する問題へ戻す |
| Persistent fiber | model class、resource order、topology、noise、computability を制限 | **[SOURCE-DERIVED]** class-relative theory は多数存在 | universal persistent fiber ではなく既存の条件付き問題になるため、一般 claim を撤回 |
| Pairwise→global | fresh preparation、product closure、reset、安全な sequential composition を加える | **[SOURCE-DERIVED]** 二ビット反例が消える条件を明示 | internality theorem の救済でなく、interface を変更した別問題。actual branch は joint realizability の型分離 |
| Amalgamation | finite candidate、deterministic outcomes、arbitrary postprocessing に制限 | **[SOURCE-DERIVED]** 初等的必要十分対応を保持 | 無限・確率・物理共同実行まで一般化しない。狭い result を novelty claim に昇格しない |
| Internal/external equivalence | 両者の履歴能力を定義上同じにする | **[SOURCE-DERIVED]** 規約的事実として区別 | 現実の controller embedding の存在を証明しないため、一般 established theorem を撤回 |
| Diagonal adversary | code visibility、query closure、fixed semantics、no private randomness 等を追加 | **[SOURCE-DERIVED]** Breuer/Wolpert近縁の条件付き制約へ接続 | internality alone を救わない。本流は causal/resource assumptions の監査へ移動 |
| Prerequisite network | 各分野に共通の fixed list として保持 | **[SOURCE-DERIVED]** v0.1 の stack 読み | 代替・支援・cross-impact を消し、field-native structuresより粗いため network / indexへ降格 |
| Deferred Resolution | DR-1 を presentation label として保持 | **[SOURCE-DERIVED]** reviews は description-only survival を認める | v0.2 は methodologyとして採用せず frozen negative にした。名称による救済を拒否 |
| Metrology generic audit | “見やすさ”を methodological success に数える | **[SOURCE-DERIVED]** preregistration が明示的に禁止 | M1 organizational value に固定し、M2/M3へ上げない |
| Web of Constraints | fixed slots、positive cases、native controls を追加して framework を維持 | **[SOURCE-DERIVED]** reviews は将来の test conditions を提示 | framework labelは維持せず、一件の empirical license-omission hypothesisへ縮小 |
| Hydrology preservation | documentary continuity を effectiveness の proxy とする | **[SOURCE-DERIVED]** v0.1 内部矛盾として訂正 | “再発見可能”と“忘却防止・実務改善”を分け、effectiveness untested を固定 |
| Full qualification study | P0 後も予定した P1–P5 を完遂する | **[SOURCE-DERIVED]** 明示的に not chosen | 比較対象が1 codeへ崩れ、計画継続が停止規則の目的に反するため P1-reduced だけ実施 |

**[INFERENCE]** この系列の特徴は「assumption strengthening を一切使わない」ことではない。狭い条件付き命題や protocol eligibility conditions は使われている。特殊 policy は、追加条件を使って元の universal claim の看板を維持することを避け、条件が実質的な仕事をするなら別 claim として型付けし、novelty / methodology status を上げないことにある。

# 8. Candidate evaluation dimensions

## 8.1 General rule

`K / A / R / D / U` は **[OPEN HYPOTHESIS]** の候補 dimension である。現段階では数値化せず、scalar、vector、独立軸、全順序を仮定しない。評価は各 dimension の観察可能な構成要素を列挙し、二つの rescue を比較できるときも partial / incomparable を許す。

## 8.2 K — rescue cost

1. **Sourceから直接観察できる成分 [SOURCE-DERIVED]:** 新しい theorem assumptions、formula class、base theory、language、proof predicate、ordinal notation、external corpus、control arm、proof resource、対象変更、撤回された旧 claim。版間 diff の追加・削除項目。
2. **推定しかできない成分 [INFERENCE]:** 研究者の労力、認知負荷、実装費、説明複雑性、社会的受容、将来保守費用、ある変更が“高価”かという価値判断。
3. **Operationalization候補 [OPEN HYPOTHESIS]:** 数え上げや加重点ではなく、`added dependency / changed target / added resource / new external validation / lost comparability` の typed ledger を二案で並べる。優劣が一意でなければ incomparable と記録する。
4. **Circularity risk:** 望ましくない rescue を事後的に “costly” と定義し、採用案を低費用とする危険。
5. **Gaming / trivial-rescue risk:** assumption を `definition` や `background` に移して cost を隠す、強い oracle / truth set / target theorem を無償の proof resource と呼ぶ。
6. **Kill criterion:** explicit delta を source から復元できない、または K の判定が A/D/R の言い換えに尽きるなら、独立 dimension として採用しない。

## 8.3 A — added arbitrariness

A は最重要 adversarial target とする。

1. **Sourceから直接観察できる成分 [SOURCE-DERIVED]:** 追加した assumption、candidate / object class、equivalence relation、formula class、provability predicate、base theory、ordinal notation、threshold、corpus cutoff、selection route、success criterion。追加が counterexample を排除するためだけに導入されたか、prior art / independent evidence / preregistration を持つか。
2. **推定しかできない成分 [INFERENCE]:** 著者の意図、ad hocness、自然さ、理論的必然性、代替 choices の全範囲、community acceptance。`standard` であることだけから非恣意性は出ない。
3. **Operationalization候補 [OPEN HYPOTHESIS]:** 次を別欄で監査する。
   - 追加前後の exact statement diff。
   - object / ambient / background / definitional / proof-resource の型。
   - failure witness と追加条件の独立性。
   - 条件の外部 warrant、事前指定、field-native motivation。
   - nearby alternatives を選んだ場合の結論安定性。
   - 条件を除くと元 counterexample が本当に戻るか。
   - 条件が結論を含意・言い換え・成功例だけに selection していないか。
4. **Circularity risk:** “元 claim を多く保持する条件ほど自然”と定義すると R と循環する。“証明できた条件は非恣意的”と定義すると可証性と循環する。
5. **Gaming / trivial-rescue risk:** 次は必ず degenerate candidate として flag する。
   - 結論 `P` を assumption として加え、`P -> P` を証明する。
   - “P を満たす objects”を対象 class と定義し直す。
   - counterexample を列挙排除するだけで独立 characterization を与えない。
   - `T` での未証明 `P` に対して `T+P` へ移り、`T |- P` が救われたと表示する。
   - required truth / soundness / consistency を、元 claim と同じ強さの background oracle として置く。
   - outcomeを見てから corpus、cutoff、success criterion、claim identity を調整する。
6. **Kill criterion:** independent warrant と target-leakage test を通らない added condition を正当な rescue と数える必要があるなら A dimension、またはその episode の rescue claimを棄却する。分析者間で「何が追加されたか」すら一致しない場合も operationalization を停止する。

## 8.4 R — retained original claim / scope

1. **Sourceから直接観察できる成分 [SOURCE-DERIVED]:** quantifier、対象 class、conclusion、theory / language、formula class、model target、evidential status、intended use の before / after。
2. **推定しかできない成分 [INFERENCE]:** どの部分が“核心”か、scope loss の重要性、言い換え間の semantic equivalence、著者が本当に保持したかった内容。
3. **Operationalization候補 [OPEN HYPOTHESIS]:** percentage にせず、`claim content / domain / quantification / target equivalence / conclusion type / status` の保存表を作る。異なる型の変更を合算しない。
4. **Circularity risk:** 修正版を見てから original core を再定義し、全て保持されたことにする。
5. **Gaming / trivial-rescue risk:** universal theorem を“この一ケースでは説明できる”へ変えて同じ title を維持する、または quotient target を元の unique representative claim と同じと表示する。
6. **Kill criterion:** `claim_before` を revision 前に固定できない、または independent reader が core/scope decomposition を再構成できないなら R を比較しない。

## 8.5 D — downstream lock-in / distortion

1. **Sourceから直接観察できる成分 [SOURCE-DERIVED]:** 新しい dependencies、excluded objects、required stronger theory、fixed formula class、new language、chosen equivalence、future checks、停止した branches、下流文書への影響。
2. **推定しかできない成分 [INFERENCE]:** 将来研究を狭める度合い、概念的 path dependence、tooling / community lock-in、長期的 distortion。
3. **Operationalization候補 [OPEN HYPOTHESIS]:** 変更後に新しく必須となる decisions と、アクセス不能になった旧 questions を列挙する。reversible correction、local convention、hard dependency を分ける。
4. **Circularity risk:** scope restriction を常に distortion と呼ぶ、または後続の不都合をすべて当該 move の因果結果とする。
5. **Gaming / trivial-rescue risk:** restrictive choice を `canonical`、`natural`、`standard` と呼んで alternatives を見えなくする。ordinal notation や formula class を固定したことを universal result と表示する。
6. **Kill criterion:** downstream recordがまだ存在せず因果を観察できない場合、Dは `unknown` に止める。speculative future costを比較結論に使う必要があるならdimensionを棄却する。

## 8.6 U — reusability

1. **Sourceから直接観察できる成分 [SOURCE-DERIVED]:** 同じ distinction / procedure の複数 case への適用、field-native reconstruction 後の残存、controlとの差、versionを越えた再使用、actual decision / retrieval / design change。
2. **推定しかできない成分 [INFERENCE]:** 未試験 domain での有用性、教育効果、将来採用、cross-domain transferability。
3. **Operationalization候補 [OPEN HYPOTHESIS]:** codebook を新語追加なしで held-out episode に適用し、native distinctions、judgment、false positives、unknowns が保たれるか比較する。Erasure Testも併用する。
4. **Circularity risk:** taxonomy を全 source を見て作り、その同じ source への fit を reusability と数える。
5. **Gaming / trivial-rescue risk:** `reformulation` や `scope change` のように広すぎる label で全 episode を覆い、coverageを有用性と呼ぶ。
6. **Kill criterion:** held-out casesで毎回 field-native rewrite の方が同等以上に精密で、診断・status・retrievalが変わらず、generic code が unknown を減らす代わりに意味を潰すなら、methodological Uを認めない。indexing valueだけは別 status に残してよい。

## 8.7 No aggregate rescue score

**[INFERENCE]** たとえば low K / low A / high R が常に望ましいとは限らない。大きな proof resource を追加して元 theorem を正しく証明する場合と、低費用で conclusion をほぼ空にする場合を一尺度で比べられない。D は将来未観測、U は held-out case 未実施であることが多い。したがって v0.1 は dominance rule、weighted score、Pareto frontier、vector norm を導入しない。

# 9. Degenerate / trivial cases

以下は **[INFERENCE]** の adversarial checklist である。

1. **Conclusion-as-assumption:** `P` を仮定して `P` を証明する。形式的には証明が閉じても元 obligation は解かれていない。
2. **Success-class definition:** domain を `{x | P(x)}` と定義して `forall x, P(x)` を得る。object restriction の正当化が独立に必要。
3. **Counterexample deletion:** known counterexamples を名前で除外するだけで structural characterization を与えない。
4. **Stronger-theory relabeling:** `T+P |- P` を `T` の問題の解決と呼ぶ。theory extension の結果としてのみ記録する。
5. **Reflection collapse:** `T+RFN(T)` と same-`T` reflection を混同する。Löb/Gödel IIの対象が変わる。
6. **Proof-resource laundering:** stronger oracle、truth predicate、unproved well-foundedness を“道具”と呼び、assumption/background dependency を隠す。
7. **Definitional information loss:** “stabilization”をmany-to-oneと定義し、non-isomorphismを発見したとする。
8. **Post hoc scope:** outcome後に candidate class、formula class、corpus、cutoff、metric、claim identity を狭める。
9. **Quotient laundering:** unique representative を失ったのに、equivalence-class identification を同じ結論として表示する。
10. **Conservation laundering:** `Gamma`-conservative / `Pi_n`-equivalent を theory equality と表示する。
11. **Ordinal laundering:** 同じ ordinal、同じ stage count、同じ worm rank を同じ theory strength と表示する。
12. **Vocabulary rescue:** Erasure後に判断差がない固有語を、説明しやすいという理由だけでmethodologyと呼ぶ。
13. **Negative-result rescue:** failed hypothesis を“失敗を発見した framework の成功”へ自動変換する。correction discipline と hypothesis support を分ける。
14. **Infinite branch proliferation:** kill criterionが発火するたびに新しい qualifier / case / vocabularyを追加し、終了を不可能にする。

Phase 0 では、各 episode が上記のいずれかを必要とするなら `degenerate` と記録し、それを正当な rescue と数えない。

# 10. Relation to Gödel I / II and reflection

## 10.1 Source-derived distinctions

**[SOURCE-DERIVED]** Gödel I の採用版は、十分な算術表現力、c.e. 公理化、整合性等の下で theory-relative な independent sentence を与える。Gödel II は、固定した標準 provability predicate と consistency sentence に相対し、整合的な `T` がその `Con(T)` を証明できないとする。Tarski は same-language full truth predicate の definability を扱い、Löb は same `T` における provable local reflection から theoremhood を導く。これらは truth、provability、soundness、consistency、reflection scope を交換できるという結果ではない。

**[SOURCE-DERIVED]** 外部から `Con(T)` または `RFN_Gamma(T)` を加えて `T+...` を作ることは、same-theory self-certification ではない。Turing–Feferman progression はこの subject theory / extension theory の index shift を明示する。limit stage は新 reflection axiom ではなく、指定された先行 theory の effective union である。

## 10.2 Limited relevance to this meta-experiment

**[INFERENCE]** 本稿への関係は、次の typing rule に限る。

- claim を object language 内へ internalize したのか、metatheory から評価したのかを記録する。
- theoryを拡張したなら、元 theory と extension を別 object とする。
- reflectionを加えたなら local / uniform / global、formula class、truth-expanded language の有無を記録する。
- reduction / conservation の結果を full theory equality としない。
- ordinal notation、progression stage、worm rank、theory ordinalを同一 indexとしない。

真理不在性系列の自己訂正、review、assumption audit は、Gödel coding、diagonal lemma、derivability conditions、formal reflection progression を実装していない。したがって両者の関係は、level confusion を防ぐための比較上の注意であり、Gödel I / II の一般化でも形式写像でもない。

# 11. Relation to theorem/proof anatomy

## 11.1 Directly reusable distinctions

以下は **[SOURCE-DERIVED]** であり、formation ledger に直接再利用できる。

1. theorem assumptions と proof resources の分離。
2. object / ambient / background / definitional の分離。
3. 採用する theorem version、language、theory、provability predicate、formula class の固定。
4. 条件除去後の falsehood、framework undefinability、new freedom、explicit correction term の区別。
5. syntactic provability、standard-model truth、semantic completeness、external soundness の分離。
6. internalization と metalevel verification の往復。
7. same theory と external theory extension の非対称性。
8. local / uniform / global reflection と consistency の scope差。
9. reduction / conservation と theory equality の分離。
10. theorem inclusion、interpretability、relative consistency、reflection ordering、ordinal comparison の relation型の分離。
11. ordinal value、notation、progression length、worm rank、theory ordinal の分離。
12. Erasure Test と kill criteria による独自語彙の降格。

## 11.2 What is not transferred as a universal move

**[INFERENCE]** 次はそのまま formation law にしない。

- `closure_role` や `escape route` は説明用メタ記述であり標準数学用語ではない。
- R0/R1/R2 は条件除去後の記録ラベルで、研究 transition の完全分類ではない。
- 通常定理で assumption strengthening が有効でも、壊れた universal hypothesis を同じ名前で救う正当性は自動的に出ない。
- proof-theoretic reduction、reflection、ordinal calibration は、empirical documentary study の move と形式的に同型ではない。
- theorem anatomy の15項目が全 research claim に必要十分であるとは source も本稿も主張しない。

## 11.3 Minimal combined ledger

**[INFERENCE]** 両系列を同時に扱う最小 ledger は次で足りる。

| Layer | Fields |
|---|---|
| Statement | claim version、target、scope、terminal status |
| Assumptions | object / ambient / background / definitional |
| Route | proof resources / evidence resources / corpus / controls |
| Failure | counterexample / logical objection / prior art / factual correction / negative control |
| Transformation | M1–M17、複数可 |
| Comparison | preserved consequence / translation / theory change / target change |
| Evaluation | K/A/R/D/U のtyped observations、Erasure、kill |
| Provenance | source-derived / inference / open hypothesis |

# 12. Proposed Phase 0 finite toy experiment

## 12.1 Aim

**[OPEN HYPOTHESIS]** 目的は、M1–M17 が真であることや完全であることを示すことではない。有限の既知 episode に対して、二人以上の reader が、固有語彙を追加せずに claim transition を再構成できるかを調べる。

## 12.2 Frozen toy corpus

最初の corpus は、同じ系列への過適合を少しでも露出させるため formal / conceptual / empirical を混ぜる。ただし一般化には使わない。

1. observation-map noninjectivity。
2. self-containment impossibility。
3. generation–log non-isomorphism。
4. pairwise separation vs global adaptive separator。
5. v0.1→v0.2 internal/external interface correction。
6. GST Deferred Resolution v0.1→v0.2。
7. Metrology Case 02 H1→M1 negative comparison。
8. hydrology preservation v0.1→documentary continuity v0.2。
9. P0→P1-reduced termination。
10. Gödel closure-reversal label→C1。
11. reflection S2→S2*。
12. proof-theoretic ordinal scalar→fixed-package calibration。

選定理由と除外理由を freeze する。toy corpus は convenience sample であり、prevalence や universality を推定しない。

## 12.3 Materials shown to coders

各 episode について次だけを一組にする。

- revision前 source excerpt。
- failure witness excerpt。
- revision後 source excerpt。
- source metadata と明示された parent / version relation。

trajectory summary、本稿の node ledger、他 coder の判定は coding 終了まで見せない。formal episode では theorem statement と採用版を含める。empirical episode では preregistered criterion と final comparison を含める。

## 12.4 Coding task

各 coder は数値scoreを使わず、次を記録する。

1. `claim_before` と `claim_after`。
2. obligation type。
3. failure witness の型。
4. actual move codes。primary / secondary を許すが単一選択を強制しない。
5. actual assumption addition と alternative rescue branch の区別。
6. terminal status。
7. K/A/R/D/U について direct observation / inference / unknown。
8. degenerate / trivial rescue flag。
9. source-derived でない解釈を明示。

## 12.5 Comparison without a score

**[OPEN HYPOTHESIS]** v0.1 では aggregate agreement score を作らない。episodeごとに次の disagreement table を公開する。

- claim boundary disagreement。
- assumption vs proof-resource disagreement。
- scope restriction vs conclusion weakening disagreement。
- theory extension vs same-theory reading disagreement。
- prior-art absorption の exact / partial 判定 disagreement。
- terminal status disagreement。
- source / inference boundary disagreement。

agreementがあること自体を成功とせず、disagreementがどの未定義語に集中するかを Phase 0 の主結果とする。

## 12.6 Phase 0 outcomes

- **Continue unchanged:** coder が同じ claim boundaries と terminal status を再構成し、move taxonomy が field-native distinctions を潰さない。
- **Revise:** 少数の隣接 move の境界だけが不安定で、source fields の追加により解消可能。
- **Collapse categories:** M2/M4、M9/M10/M13 等が source 上区別不能なら統合または階層化。
- **Stop framework claim:** claim individuation、assumption/resource、actual/alternative branch が再現不能で、adjudicator の事後物語だけで成立する。

# 13. Kill criteria

以下のいずれかが確認された場合、meta-experiment を review / annotated trajectory に降格し、general framework claim を終了する。

1. claim episode の境界が coder 間で再構成できず、違いが単なる記述粒度ではなく move / status を変える。
2. actual move と source が言及しただけの alternative rescue を安定して区別できない。
3. theorem assumptions と proof resources を安定して分けられない。
4. object / ambient / background / definitional の適用が形式数学外では恣意的で、追加情報を生まない。
5. M1–M17 を消しても、before / witness / after / status の通常の revision ledger と比べ判断が変わらない。
6. field-native description の方が同等以上に精密で、generic move codes が型の差を消す。
7. taxonomyが全 episodeを `reformulation + restriction` と再記述するだけで、誤分類防止に寄与しない。
8. A の target-leakage / trivial-rescue test が reviewer judgment に完全依存し、再検査不能である。
9. R の “original core” が revision 後にしか定義できない。
10. K/A/R/D/U のうち複数が同じ evidence の言い換えに尽き、独立名を維持する利益がない。
11. D を評価するために sourceにない因果史・研究者心理・将来影響を補う必要がある。
12. U が broad labels の post hoc coverage だけで成立し、held-out case で判断差を生まない。
13. negative result を framework の成功として数えないと継続理由がなくなる。
14. Phase 0 の問題を直すために move、dimension、例外 clause を増やし続け、停止条件が消える。
15. Gödel / reflection / ordinal の語彙が、形式対応なしに empirical research trajectory へ権威づけとして使われる。
16. source-derived / inference / open hypothesis の境界が維持できない。

# 14. What would count as L0 / L1 / L2

L0–L2 は theory strength、ordinal、数値scoreではなく、この meta-experiment 自身の evidential status である。

## L0 — Annotated source inventory

次を満たす状態。

- source inventory と version / branch relationが訂正可能に記録される。
- claim_before、failure witness、move_taken、claim_after、statusを source excerpt に結びつける。
- alternative rescue と actual route を分ける。
- Erasure / kill / negative results を保存する。
- 新しい方法論的有用性は主張しない。

**Current status: L0 candidate.** 本稿はこの水準を目標にしているが、独立 coding をまだ受けていない。

## L1 — Reproducible local coding procedure

少なくとも一つの frozen finite corpus で、独立 reader が次を source から再構成できる。

- claim boundaries と terminal status。
- assumption / proof-resource / target / theory の型。
- actual move と rejected rescue branch。
- trivial rescue の主要 flag。
- source-derived と inference の境界。

一致を単一scoreで表さず、decision-relevant disagreement が解消可能であることを episodeごとに示す。L1でも普遍分類やmethodologyを主張しない。

## L2 — Comparative utility beyond an ordinary revision ledger

複数の独立 corpus と別 team で、通常の version diff / research log と比較し、少なくとも次のいずれかを再現する。

- assumption と proof resource の混同を防ぐ。
- same-theory と theory extension の誤読を防ぐ。
- rejected rescue を採用 route と誤認することを防ぐ。
- conclusion weakening / scope restriction / quotient reformulation を区別する。
- trivial rescue または negative-result resurrection を通常 ledger より早期かつ正確に発見する。
- kill decision、terminal status、source provenance の判断を改善する。

同時に、field-native terminology を保持し、false positive や semantic flattening が増えないことを示す。L2でも新しい証明論や普遍理論を意味しない。

# 15. Explicit reason not to target L3 theorem completion yet

ここでいう仮の `L3 theorem completion` は、move taxonomy やK/A/R/D/Uから一般 theorem、必要十分条件、最適 rescue rule、普遍的順序を構成する段階を指す。本稿はこれを目標にしない。

理由は次の通りである。

1. unit of analysis である claim episode と claim identity が未検証である。
2. formal theorem、methodology claim、documentary hypothesis は obligation type が異なり、共通 domain さえ確立していない。
3. move codes の完全性、排他性、合成則、同値関係がない。
4. K/A/R/D/U は観察可能成分と価値判断が混在し、order relation が定義されていない。
5. source corpus は一つの自己訂正的研究系列と、そのために選ばれた theorem stress tests であり、selection bias が大きい。
6. shrinkage はこの系列の research policy であり、proof formation 一般の law ではない。
7. theorem anatomy 自身が、独自語彙の多くを E1 / C1 / RX として説明用へ降格している。
8. theory strength と ordinal の stress tests は、異型 relation を一尺度へ圧縮することの危険を直接示している。
9. Phase 0 の独立再構成も held-out comparison も未実施である。
10. theorem を先に目標化すると、追加 assumptions、定義的 rescue、post hoc scope restriction によって“証明可能性”を作る incentive が生じ、A の最重要リスクを自ら導入する。

したがって L3 を議論する前に、L0の source fidelity とL1の再構成可能性を反証的に検査する。L1またはL2が失敗した場合、annotated trajectory / reviewとして終了する。

# 16. Undefined terms and dangerous assumptions to resolve before any computational experiment

優先順位は、未解決のまま code 化したときに結果を最も強く歪める順である。

1. **Claim identity / episode boundary — highest priority.** 何を同じ claim の revision とし、何を new claim / neighboring question とするか。`P/Q`分解やtitle continuityだけでは足りない。
2. **Actual move versus available rescue.** source が“可能”と述べた条件付き theorem と、研究本流が実際に採用した変更をどう区別するか。
3. **Added arbitrariness.** independent warrant、target leakage、counterexample deletion、post hoc scope を、研究者意図を推測せずどう判定するか。
4. **Trivial rescue.** `assume P`、success-class definition、`T+P`、strong oracle、outcome-conditioned corpus を機械的に検出できる最小規則。
5. **Assumption versus proof/evidence resource.** とくに background theory、truth / soundness、well-foundedness、additional literature、control design の扱い。
6. **Conclusion weakening versus scope / object restriction versus quotient reformulation.** 同じ before/after が複数 move に見える場合の typing rule。
7. **Terminal status.** proved、conditional theorem、reduction result、empirical question、review、open、withdrawn、frozen negative の境界。
8. **Prior-art absorption strength.** exact coverage、counterexample、close analogue、formal vocabulary、partial constraint を誰がどう判定するか。
9. **Retained original claim.** revision後に“核心”を再定義する循環を避けるため、before-state の固定手順が必要。
10. **Rescue cost.** change ledger と価値判断を分けられるか。labor / complexity を sourceなしで推定しない規則が必要。
11. **Downstream lock-in / distortion.** 将来予測でなく、既存 revision chain に観察可能な依存だけを使う範囲。
12. **Reusability.** broad label coverage と decision-relevant utility を分ける held-out design。
13. **Source chronology.** same-day logical dependencyを実時系列・因果系列と誤認しないための metadata rule。
14. **Negative-result fixation.** 新しい証拠による正当な再検討と、語彙変更による resurrection を分ける規則。
15. **Formal-to-empirical transfer.** Gödel / reflection / ordinal distinctionsを、形式写像なしに empirical episode の分類根拠へしない境界。
16. **Category completeness.** moveを追加する条件、統合する条件、frameworkを終了する条件を Phase 0 前に freezeする。

計算実験へ進む前の最小作業は、上位6項目について二つずつの positive / negative example を source excerpt から作り、coder instructions と adjudication rule を一ページ以内に固定することである。数値score、optimization、embedding、geometry、automatic ranking はその後も導入しない。

# Closing status

**[SOURCE-DERIVED]** 両系列が最も強く支持するのは、新しい普遍構造ではなく、対象・仮定・資源・言語・理論・比較 relation を分け、反例・prior art・Erasure・kill criteria による降格を保存する規律である。

**[INFERENCE]** 本稿がそこから追加する最小案は、`claim_before / obligation / failure_witness / move_taken / claim_after / terminal_status` を一つの episode として記録することだけである。

**[OPEN HYPOTHESIS]** この episode ledger が通常の version diff より再現可能または有用かは、Phase 0 の有限・独立 coding が行われるまで未確立である。

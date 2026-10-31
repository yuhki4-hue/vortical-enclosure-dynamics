# 法則式／生成律式 記述方法論

> Status:
> - closed methodology study (Phase 0–4; STOP-A)
> - not a theorem
> - not a new mathematical framework
> - not yet a revision of VED
> - negative results are primary evidence

## Purpose

この directory は、**法則の式（law equation）が何を記述し、生成に関する式や規則が何を追加で主張するのか**を、VED の既存式からいったん離れて監査するための新しい研究枝である。最終目的は VED の正当化でも、既存式の即時改稿でもない。

研究順序を次に固定する。

1. 固定された specification 内で law-like description が何を制約するかを調べる。
2. specification 間の変更として語られる generation claim を分解する。
3. state transition、renaming、representation change、definitional extension、structural enlargement を区別する。
4. claim の論理形ごとに sufficient evidence と insufficient evidence を分ける。
5. 既存の数学・論理・計算機科学で記述できる範囲を確認する。
6. 標準概念へ無損失に翻訳できない残差が反復して得られた場合にだけ、生成律固有の記法を検討する。
7. その後にだけ、VED の既存式を個別監査する。

## Non-goals

- VED の妥当性を先に仮定しない。
- generative law / generative equation の数学的独自性を仮定しない。
- 新しい theory、calculus、framework、score、metric、hierarchy を宣言しない。
- 「法則＝時間発展」「生成＝仕様が違うこと」「生成＝開き」を定義にしない。
- 哲学的な生成、存在論的な生成、formal expressivity の増加を同一視しない。
- 一つの construction failure から生成不能を推論しない。
- finite toy model から universal theorem を推論しない。
- 既存 VED ファイルをこの branch の成果が出る前に書き換えない。

## Research posture

本枝は、[theorem / proof anatomy experiment の最終記録](../notes/theorem_proof_anatomy_experiment/07_audit_and_closure/theorem_proof_anatomy_experiment_final_record_v1.0_ja.md)から、次の監査規律だけを引き継ぐ。

- claim の logical form に evidence の形を合わせる。
- existential claim と universal claim を区別する。
- route failure、impossibility、setting / target change を混同しない。
- source specification、target specification、map、scope、direction、preserved / changed object を明示する。
- representation change と substantive change を分ける。
- counterexample、failed distinction、ill-posed definition、negative result を保存する。
- standard terminology で十分なら project-local vocabulary を増やさない。

ただし、同 archive で退役した theorem / proof anatomy 固有語彙を、この研究の technical vocabulary として輸入しない。

## Initial records

| Record | Role | Current status |
|---|---|---|
| [final record v1.0](./generative_law_methodology_final_record_v1.0_ja.md) | Phase 0–4の終了記録、negative results、final dispositions | **closed / STOP-A** |
| [working note](./generative_law_methodology_working_note_v0.1_ja.md) | repository inspection、現行仮説、標準概念との対応、実験経過 | historical working record v0.1 |
| [law equation specification](./law_equation_specification_v0.1_ja.md) | law-like description の形と固定条件 | v0.1 |
| [generative equation specification](./generative_equation_specification_v0.1_ja.md) | specification change と generation claim の分解 | v0.1; special notation downgraded |
| [evidence-burden table](./generative_claim_evidence_burden_v0.1_ja.md) | 生成 claim ごとの証拠要件 | v0.1 |
| [redescription vs generation test](./redescription_vs_generation_test_v0.1_ja.md) | eight toy controls と G0–G5 stress | first pass complete |
| [Phase 4 cross-test synthesis](./phase4_cross_test_synthesis_v0.1_ja.md) | five finite tests の横断判定、negative-result ledger、stopping audit | complete; **STOP-A** |
| [toy models](./toy_models/README_ja.md) | toy-model scope と将来の executable checks | no checker yet |
| [observable-independence finite test](./stress_tests/observable_independence_finite_model_v0.1_ja.md) | definitional access と distinguishable model expansions の分離 | complete; 6 finite cases |
| [finite checker](./stress_tests/observable_independence_finite_model_v0.1.py) | fibers、observational quotients、functional dependence の完全列挙 | all assertions pass |
| [graph-growth dual-encoding test](./stress_tests/graph_growth_dual_encoding_v0.1_ja.md) | fixed-state rewrite と changing-carrier record の保存範囲 | complete; 13 states / 20 transitions |
| [graph-growth checker](./stress_tests/graph_growth_dual_encoding_v0.1.py) | translations、predicates、histories、isomorphism、preload controls | all assertions pass |
| [construction/internal-order test](./stress_tests/construction_vs_internal_order_v0.1_ja.md) | linear construction history と internal partial order の分離 | complete; 24 permutations exhausted |
| [order-model checker](./stress_tests/construction_vs_internal_order_v0.1.py) | linear extensions、history quotient、timestamps、fixed-state control | all assertions pass |
| [relation-to-metric boundary test](./stress_tests/relation_to_metric_boundary_v0.1_ja.md) | metric axiomsとweight/direction/connectivity/policyの境界 | complete; cases A–H plus coarse control |
| [metric-boundary checker](./stress_tests/relation_to_metric_boundary_v0.1.py) | shortest paths、axioms、quotient、negative cycle、coarse policies | all assertions pass |
| [rule-space-as-data test](./stress_tests/rule_space_as_data_v0.1_ja.md) | operational-rule change と fixed interpreter 上の state change の比較 | complete; finite controls A–I |
| [rule-space checker](./stress_tests/rule_space_as_data_v0.1.py) | traces、subsets、parameters、derived rules、types、history、meta-rule lift | all assertions pass |
| [stress tests](./stress_tests/README_ja.md) | Phase 4 finite tests and stopping gate | five tests and synthesis complete |
| [VED reconstruction](./ved_reconstruction/README_ja.md) | 適用前 gate と将来の監査 schema | **not started** |

## Current working hypotheses

| ID | Working hypothesis | Initial disposition |
|---|---|---|
| H-L1 | law-like description は、固定した specification 内の admissible states / histories / distributions / relations を制約する | **RETAIN WITH REVISION**。写像や時間発展に限定しない |
| H-L2 | law equation と generative equation は式の外形だけで区別できる | **KILL candidate**。同じ更新式が state transition にも graph growth にも読める |
| H-G1 | generation claim は source / target specifications と比較 map を明示すれば検査可能になる | **RETAIN as audit requirement**。これだけで generation の独自概念は得られない |
| H-G2 | new symbol / observable / relation / dimension は同じ意味で「新しい」 | **KILL candidate**。定義拡張と自由度追加を区別する必要がある |
| H-G3 | G0–G5 は generation の強さを表す hierarchy である | **DOWNGRADE / likely KILL**。定義可能な observable、order、metric が段階を横断する |
| H-G4 | generation は law-like restriction に対する structural enlargement として一括できる | **OPEN / weak**。確率法則や型形成、rule generation では包含関係が一意でない |
| H-G5 | VED の既存生成 claim には独自記法が必要である | **NOT ESTABLISHED**。現段階では標準概念が広い範囲を覆う |

## Kill / downgrade criteria

### KILL candidates

- generative equation が、固定 state space 上の通常の transition と区別できない。
- redescription / definitional extension / generation の分類が、translation や comparison map の選び方だけで自由に入れ替わる。
- generation claim が、standard rewriting、state-space change、definitional / conservative extension、interpretability、expressive-power comparison だけで無損失に尽くされる。
- provisional notation が既存の map、relation、rule application 以上の検査可能な内容を追加しない。
- source / target / admissible comparison class を固定しても再現する residual distinction がない。

### DOWNGRADE candidates

- 独自数学ではないが、複数分野に散らばる distinctions の監査手順として有用である。
- VED の式を law / constraint / constitutive / measurement / update に分ける用途には有効だが、一般理論にはならない。
- generative が expository shorthand としてのみ有用である。

### SURVIVE condition

標準概念へ翻訳した後にも、同じ source / target / map / scope のもとで、通常の state transition、representation change、definitional extension のいずれでもない specification transition が反復して形式化され、false positive controls を通過し、claim-specific evidence burden が満たされること。これは現時点では満たされていない。

## Phase plan

| Phase | Question | Gate | Status |
|---|---|---|---|
| 0 | law equation は固定仕様内の何を制約するか | 六つの標準形式を比較 | v0.1 complete |
| 1 | generation claim を source / target / map でどう書くか | state change と specification change を分離 | v0.1 complete |
| 2 | redescription false positives を除けるか | Toy A–H | first pass complete |
| 3 | standard mathematics で何が十分か | field-by-field reduction table | initial mapping complete |
| 4 | distinction は representation / comparison map に耐えるか | paired stress tests と countermodels | complete; **STOP-A** |
| 5 | residual notation は必要か | standard translation failure の反復証拠 | **not entered; special notation frozen** |
| 6 | VED の現行式へ適用できるか | Phase 4–5の結果と式別 evidence audit | **not started; separate audit only** |

## Relation to VED

repository inspection では、VED が “difference → closure degree → gradient → flow → vortex → enclosure” という生成順序、因果履歴 \(H\)、因果ログ \(C\)、密度 \(\rho\)、局所時間 \(\tau\)、流れ \(J\)、渦度、距離 \(d\) などを既に用いていることを確認した。これらは本研究の最終監査対象であり、初期仕様の正解を決める evidence ではない。

特に \(\nabla\)、\(\nabla\times\)、\(d/dt\)、\(d(x,y)\) が必要とする幾何・向き・時間・metric structure は、後の circularity audit の対象である。現時点で「誤っている」とは判定しない。

## Relation to the prior experiment

前系列から継承するのは、**主張ごとに十分な証拠を分ける方法**である。前系列の退役語彙や theorem-specific taxonomy は継承しない。本枝で route failure などの平易な表現を使う場合も、特定 construction の失敗という通常の意味に限る。

## Current status

Phase 0–2 の初回文書化、Phase 4 の五つの finite test、およびcross-test synthesisが完了した。raw fiber size は independent freedom の十分条件ではなく、observational separationもcomparison specificationに相対的だった。bounded graph growthは二encoding間で多くのbehaviorを保存できたが、stage-local languageは無条件には一致しなかった。construction orderはinternal partial orderのlinear extensionであり得るが同一ではない。relation-to-metric testでは、positivity、zero weights、connectivity、directedness、negative cycles、weighting、coarse policyがdistance classificationとuniquenessを分け、fully fixed shortest-path metricもindependent metric freedomやphysical spaceを示さなかった。rule-space testでは、有限に事前宣言したrules、active subsets、parameters、derived rules、bounded history、meta-rule codeを固定interpreter下のstate dataとして扱えた一方、stage-local availability、type formation、interpreter boundaryはpreloadまたは追加仕様として残った。

横断監査では、標準数学へ還元できない同一の形式的残差は反復しなかった。[stopping audit](./phase4_cross_test_synthesis_v0.1_ja.md)は **STOP-A / STOP AND SYNTHESIZE AS AUDIT METHODOLOGY** を採用した。[Final record v1.0](./generative_law_methodology_final_record_v1.0_ja.md)はこの判定を変更せず研究枝を閉じる。generative equationは **NOT ESTABLISHED**、placeholderは **DOWNGRADE**、special notationは凍結し、Phase 5へ進まない。VED-specificな肯定判定や式の書換えはなく、VED reconstructionは開始していない。

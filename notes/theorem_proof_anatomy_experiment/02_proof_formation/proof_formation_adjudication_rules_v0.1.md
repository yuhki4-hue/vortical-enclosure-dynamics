# Proof-Formation Inter-Reader Test — Adjudication Rules v0.1

- **Status:** pre-Phase-0 qualitative adjudication protocol and withheld answer key
- **Basis:** [`proof_formation_meta_experiment_v0.1.md`](./proof_formation_meta_experiment_v0.1.md)
- **Coder form:** [`proof_formation_coder_instructions_v0.1.md`](./proof_formation_coder_instructions_v0.1.md)
- **Frozen inputs:** [`proof_formation_frozen_toy_corpus_v0.1.md`](./proof_formation_frozen_toy_corpus_v0.1.md)
- **Access rule:** 独立readerの提出完了まで、本ファイルのexample bankとanswer keyをreaderへ渡さない

## 1. Adjudication priority

不一致は次の順で処理する。下位の推論で上位の明示記述を上書きしない。

1. **Source wording:** 原文に実際に書かれたclaim、否定、modal、status語。
2. **Exact before/after statement:** 量化、対象、theory/language、formula/model/corpus scope、結論型の差。
3. **Explicit status/verdict:** `[WITHDRAWN]`、`[ESTABLISHED]`、frozen negative、supported / not supported、採用／非採用。
4. **Explicit dependency change:** parent、revision ledger、accepted diff、prerequisite、追加・削除されたdependency。
5. **Inference:** M-code、episode grouping、primary/secondary、動機、counterfactual reconstruction。

多数決、権威、文章の流暢さ、frameworkに都合のよい整合性は判定根拠にしない。上位資料が両方のreadingを許す場合は、下位推論で一意化せず `UNRESOLVED` とする。

## 2. Qualitative adjudication procedure

1. readerごとの記録を、field単位で並べる。
2. disagreementを `claim identity / episode boundary / assumption-resource / M2-M3-M4 / actual-available / provenance / status / other` の既存欄へ置く。
3. 各readerが根拠にしたexact excerptを確認する。source外説明は一度除く。
4. 上の優先順位で、`SOURCE-RESOLVED`、`BOTH PERMITTED`、`SOURCE SILENT`、`BOUNDARY-DEPENDENT`のいずれかを文章で記録する。
5. `SOURCE-RESOLVED`の場合だけ記録を訂正する。それ以外は`UNRESOLVED`とし、両案と必要な追加sourceを残す。
6. 新しいmoveや例外規則をその場で追加しない。既存M-codeで表せないこと自体をtest resultとして記録する。

一致率、kappa、precision、recall、weighted score、rankを計算しない。episodeごとの不一致内容と解消根拠だけを保存する。

## 3. Mandatory non-resolution cases

次の場合は無理に解決しない。

- sourceに`claim_before`が固定されていない。
- episode boundaryが複数可能で、どれを選ぶかによりmove/statusが変わる。
- 採用したtheorem versionによって同じ項目がassumptionにもproof resourceにもなる。
- rescue branchがsource明示か、本稿側の反実仮想かを確認できない。
- added arbitrarinessの判定に著者の意図、自然さ、community acceptanceの推定が必要。
- same title / same vocabularyしかclaim identityの根拠がない。
- exact / partial prior-art absorptionを判定するための比較sourceがpacketにない。
- mathematical operationがsource内で説明されているだけか、当該episodeで実際に採用されたmoveかが境界依存。

`UNKNOWN`は資料不足、`AMBIGUOUS`は複数readingをsourceが許す場合、`UNRESOLVED`はadjudication後も残る不一致に用いる。

# 4. Source-anchored example bank

この節の`positive`はsource wordingだけで区別をかなり固定できる例、`boundary`は複数code、UNKNOWN、AMBIGUOUS、UNRESOLVEDを正答として許す例を指す。

## 4.1 Claim identity

### CI-P1 — Positive: internal/external claimの明示的改訂

- **Source file:** `notes/theorem_proof_anatomy_experiment/00_origin/tool_truth_absence_v0.1_to_v0.2_diff.md`
- **Exact excerpt:** “一般的な internal/external interface equivalence が強すぎる | v0.1 の一般 `[ESTABLISHED]` を撤回。完全な履歴能力を同一と定義する規約的同値と、離散時間 turn-based controlled transition system における条件付き実装対応へ分離”
- **Correct coding:** 明示された一つのversioned revision episode。ただし`claim_after`は元の一般命題と同一ではなく、規約的帰結と条件付き補題の二つへ分離された。M14とM17。必要なら二つのafter-branchを別行にする。
- **Tempting wrong coding:** 同じinterface-equivalence theoremにassumptionsを追加しただけなので、claim identityは完全に保存されM1のみ。
- **Why wrong:** sourceは一般`[ESTABLISHED]`の撤回と二命題への分離を明記する。
- **Uncertainty note:** 規約的同値と条件付きモデル対応を一episodeの二branchとするか、二episodeとするかは`AMBIGUOUS`を許す。

### CI-P2 — Positive: preservationからdocumentary continuityへの訂正

- **Source file:** `notes/theorem_proof_anatomy_experiment/00_origin/hydrology_negative_knowledge_preservation_note_v0.2.md`
- **Exact excerpt:** “| B. Partial preservation history identified | **Documentary continuity identified; preservation effectiveness untested** |”
- **Correct coding:** 同じ文書系列を扱うrevisionだが、効果を含む`preservation` claimは保持されず、documentary continuityという弱い結論へ変更された。M2/M14、元の効果claimはM17。
- **Tempting wrong coding:** “preservation”の言い換えなのでclaimは不変。
- **Why wrong:** sourceは“「保存機構」の存在を主張しない。確認できたのは文書上の連続性のみ”と明示する。
- **Uncertainty note:** corpus scopeはほぼ同じだが、事実訂正も同時にあるため、全変更を一claim identityへ束ねない。

### CI-B1 — Boundary: reflection familyを一つのclaimとしない

- **Source file:** `notes/theorem_proof_anatomy_experiment/01_theorem_anatomy/reflection_principles_scope_stress_test_ja.md`
- **Exact excerpt:** “single local、schema、uniform、global、consistency、soundness は異なる型である。”
- **Correct coding:** 数学的claim identityはscopeごとに分ける。“自己保証S2”という比較ラベルの評価は一つのmeta-episodeとして扱えるが、その対象であるreflection principlesを一命題にしない。
- **Tempting wrong coding:** すべて同じself-guarantee claimの強弱であり、一軸上の同一claim。
- **Why wrong:** sourceはformula class、量化、truth-expanded language、metalevelの型差を中心結論にする。
- **Uncertainty note:** meta-labelのidentityと数学的statementのidentityをどちらに問われているか不明なら`AMBIGUOUS`。

### CI-B2 — Boundary: P0からP1-reducedはdependencyだけでidentityを決めない

- **Source file:** `notes/theorem_proof_anatomy_experiment/00_origin/p1r_noneval_two_field_check_v0.1.md`
- **Exact excerpt:** “P0 の結果、14 コード中で比較対象として生き残ったのは `NONEVAL` 一つだった。本検査はこの一コードのみを扱う。”
- **Correct coding:** P0への明示dependencyとscope restrictionはsource-derived。14-code comparative programとone-code two-field checkが同一claimの縮小か、neighboring testかは`AMBIGUOUS`。
- **Tempting wrong coding:** `先行`が明記されているので同じclaim、またはfileが別なので必ず別claim。
- **Why wrong:** dependencyもfile boundaryもlogical identityを単独では決めない。
- **Uncertainty note:** coderが固定した`claim_before`の粒度を併記してunresolvedを許す。

## 4.2 Episode boundary

### EB-P1 — Positive: GST revision ledger

- **Source file:** `notes/theorem_proof_anatomy_experiment/00_origin/deferred_resolution_case_01_gst_v0.1_to_v0.2_diff.md`
- **Exact excerpt:** “| Final status | working positive case | frozen negative baseline | frozen |”
- **Correct coding:** v0.1のworking positive verdictからv0.2のfrozen negativeまでを一つの明示的revision episodeとして切れる。
- **Tempting wrong coding:** GST technical history全体を一episodeにする、またはreviewごとに無関係なepisodeへ分解する。
- **Why wrong:** revision ledgerがbefore/after/status dependencyを直接固定する一方、個々のGST technical stageは別objectである。
- **Uncertainty note:** 個別のquotient、model extension、bibliographic correctionはsub-episodeとして分離可能。

### EB-P2 — Positive: preregistered H1からfinal verdictまで

- **Source file:** `notes/theorem_proof_anatomy_experiment/00_origin/scientific_assurance_case_02_metrology_preregistration.md`; `notes/theorem_proof_anatomy_experiment/00_origin/scientific_assurance_case_02_metrology_comparison.md`
- **Exact excerpt:** “H1 is supported only if at least one preregistered success condition in §6 survives all applicable falsification conditions in §5.” / “No. It changed presentation and cross-chain visibility only.”
- **Correct coding:** H1、frozen control、generic audit、head-to-head verdictを一つのpreregistered empirical episodeとして扱う。terminal statusはH1 not supported、M1 organizational only。
- **Tempting wrong coding:** control、audit、comparisonを互いに無関係な三episodeとし、H1との対応を切る。
- **Why wrong:** preregistrationとcomparisonが同じsuccess/falsification条件を明示的に参照する。
- **Uncertainty note:** chain A/B/Cは内部subcasesであり、個別episode化も可能だがH1 verdictを分断しない。

### EB-B1 — Boundary: Gödel I、Gödel II、meta-vocabulary verdict

- **Source file:** `notes/theorem_proof_anatomy_experiment/01_theorem_anatomy/godel_incompleteness_closure_reversal_stress_test_ja.md`
- **Exact excerpt:** “第1は「各文を決定する能力」の限界、第2は「自分の標準的整合性文を証明する能力」の限界である。第2は第1を単に言い換えたものではなく、第1定理の証明可能性 reasoning を内部形式化する追加段階を持つ。”
- **Correct coding:** Gödel I、Gödel II、そして“閉包反転”C1判定は少なくとも区別可能なepisode。課題がstress-test全体ならcomposite boundaryとして`AMBIGUOUS`を許す。
- **Tempting wrong coding:** 同じGödel episodeのbefore/witness/afterとして一行に圧縮。
- **Why wrong:** conclusion、assumptions、proof predicate、metalevelが異なる。
- **Uncertainty note:** E10 packetは意図的にcompositeであり、複数episodeへの分割が正当な回答になりうる。

### EB-B2 — Boundary: hydrology v0.2の複数訂正

- **Source file:** `notes/theorem_proof_anatomy_experiment/00_origin/hydrology_negative_knowledge_preservation_note_v0.2.md`
- **Exact excerpt:** “いずれも Codex が正しく、v0.1 に事実誤りが二件、内部矛盾が一件あった。”
- **Correct coding:** C-1、C-2、C-3は別failure witnessと別claimを持つため、原則別sub-episode。全体verdict変更を上位episodeとして置くこともでき、boundaryは`AMBIGUOUS`。
- **Tempting wrong coding:** 一回のreviewだから単一episode、または三件すべて同じconclusion weakening。
- **Why wrong:** 二件はfactual correction、一件はevidential overclaim/internal contradictionで型が違う。
- **Uncertainty note:** aggregation levelを明記すれば両方を許し、無言の統合だけを誤りとする。

## 4.3 Assumption strengthening versus proof-resource addition

### AR-P1 — Positive: Gödelのconditionsとdiagonal lemma

- **Source file:** `notes/theorem_proof_anatomy_experiment/01_theorem_anatomy/godel_incompleteness_closure_reversal_stress_test_ja.md`
- **Exact excerpt:** “self-reference enablement は単独の仮定ではない。B・Cによって構文と証明関係を算術へ写す条件が整い、proof resource である diagonal lemma を適用した結果として自己適用文が得られる。”
- **Correct coding:** 算術的表現力・effective axiomatizationはassumptions、diagonal lemmaはproof resource。self-referenceを追加assumptionにしない。
- **Tempting wrong coding:** diagonal lemma/self-referenceをM1 assumption strengtheningとして記録。
- **Why wrong:** sourceがproof resourceと明記する。
- **Uncertainty note:** 採用版が変われば必要なsoundness条件は変わるが、このexcerptの区別は明示的。

### AR-P2 — Positive: reflection scopeとanalysis tools

- **Source file:** `notes/theorem_proof_anatomy_experiment/01_theorem_anatomy/reflection_principles_scope_stress_test_ja.md`
- **Exact excerpt:** “formula class \(\Gamma\) は \(T\) の「性質」ではなく、どの reflection instances を追加するかという scope definition である。” / “特に diagonal lemma、ordinal analysis、GLP を assumptions に昇格させない。”
- **Correct coding:** \(\Gamma\)はtarget/definitional scope、diagonal lemma・ordinal analysis・GLPはproof/analysis resources。M3とM8を混同しない。
- **Tempting wrong coding:** reflection proofに使うものはすべてassumptions、または\(\Gamma\)もproof tool。
- **Why wrong:** sourceが両者の役割を明示的に分ける。
- **Uncertainty note:** base theoryのinduction strengthはambient/object assumptionであり、単なるresourceではない。

### AR-B1 — Boundary: metrology controlの二重の見え方

- **Source file:** `notes/theorem_proof_anatomy_experiment/00_origin/scientific_assurance_case_02_metrology_preregistration.md`
- **Exact excerpt:** “H1 is supported only if at least one preregistered success condition in §6 survives all applicable falsification conditions in §5.” / “The control must solve the problem using field-native concepts.”
- **Correct coding:** frozen controlとreview procedureはevidence resources。success/falsification conditionsはH1のevaluation rule / definitional eligibilityである。方法論claimの“assumption”と呼ぶreadingもあるため、形式数学と同じ型付けを強制せず`AMBIGUOUS`を許す。
- **Tempting wrong coding:** controlをM1で追加したためH1が救済された、またはすべてM8。
- **Why wrong:** controlはH1を成立しやすくせず、むしろ反証条件を固定する。sourceはH1をsupportしなかった。
- **Uncertainty note:** empirical protocolでassumption/resource境界が再現不能なら、そのことをframeworkのfragilityとして残す。

### AR-B2 — Boundary: ordinal well-foundedness / TI / WO

- **Source file:** `notes/theorem_proof_anatomy_experiment/01_theorem_anatomy/proof_theoretic_ordinal_stress_test_ja.md`
- **Exact excerpt:** “ordinal assignment 自体は soundness を与えず、reduction step の正当性と notation の well-foundedness が必要。” / “proof_resources: infinitary embedding、cut elimination、ordinal assignment、fundamental sequences、TI/WO、reflection reduction、GLP/worm calculus”
- **Correct coding:** どのtheoremをstatementとして固定するかにより、well-foundedness/TIはbackground assumptionにもproof resourceにもなりうる。packetだけで単一判定せず`AMBIGUOUS`。
- **Tempting wrong coding:** terminology listに一度`proof_resources`とあるため、全出現を常にM8。
- **Why wrong:** relative consistency theoremではwell-foundedness principleが明示前提になることがある。
- **Uncertainty note:** exact theorem versionがない限りunresolved。

## 4.4 Conclusion weakening versus scope restriction

### WS-P1 — Positive: efficacy claimの弱化

- **Source file:** `notes/theorem_proof_anatomy_experiment/00_origin/hydrology_negative_knowledge_preservation_note_v0.2.md`
- **Exact excerpt:** “**確認できていないこと。** 実際の参照・利用・下流伝達・忘却防止効果は、いずれも測定していない。**文書上の再発見可能性は残ったが、それ以上は言えない。**”
- **Correct coding:** 同じdocumentary recordについて、effectivenessを含む結論から再発見可能性だけへM2。単なるcorpus restrictionではない。
- **Tempting wrong coding:** 水文学系列だけへ対象を狭めたM4のみ。
- **Why wrong:**主要なdeltaは何を結論するかであり、効果を明示的に除いた。
- **Uncertainty note:** 用語中立化M14もsecondaryとして許す。

### WS-P2 — Positive: 14-code programからone-code test

- **Source file:** `notes/theorem_proof_anatomy_experiment/00_origin/p0_generic_standards_baseline_v0.1.md`
- **Exact excerpt:** “比較研究として問うべき対象が `NONEVAL` 一つに縮小した以上、これは「比較研究プログラム」ではなく「一つの記述形式についての限定的な問い」である。”
- **Correct coding:** 対象code/domainを狭めるM4と、limited comparative questionへのM16。元の14-code conclusionを弱く証明したとしない。
- **Tempting wrong coding:** 14-code仮説の結論を少し弱めたM2だけ。
- **Why wrong:**検査対象そのものが一codeへ変更される。
- **Uncertainty note:** program statusの降格をM2と併記するreadingは許すが、M4を落とさない。

### WS-B1 — Boundary: finite deterministic common refinement

- **Source file:** `notes/theorem_proof_anatomy_experiment/00_origin/tool_truth_absence_working_note_v0.2.md`
- **Exact excerpt:** “この同値は、固定有限候補、決定論的結果、任意の後処理を許すという条件では初等的であり、新定理ではない。”
- **Correct coding:** 対象/model class restriction M4（場合によりlanguage/formal setting M3）と、一般amalgamation claimからinformational equivalenceへのM2/M14が共存する。primaryを強制しない。
- **Tempting wrong coding:** scope restrictionだけ、またはconclusion weakeningだけ。
- **Why wrong:** domainとconclusion typeの両方が変わる。
- **Uncertainty note:** before statementの厳密なformalizationがないため、M2/M4の境界は`AMBIGUOUS`でもよい。

### WS-B2 — Boundary: ordinal S2*

- **Source file:** `notes/theorem_proof_anatomy_experiment/01_theorem_anatomy/proof_theoretic_ordinal_stress_test_ja.md`
- **Exact excerpt:** “自然な理論群と標準 analysis packageでは、cut elimination、TI/WO、reflection、worm ordering が橋渡し定理により同じ ordinalへ収束し、ordinal は複数の標準 notions を統合する頑健な一次元 coordinateになる。だが任意の理論、任意の formula class、任意の interpretability/conservation notionを一つにする universal scalarではない。”
- **Correct coding:** universal conclusionの否定/弱化M2、natural theory/analysis packageへのscope restriction M4/M3、comparison/calibration M13を併記できる。
- **Tempting wrong coding:** “scalar” claimがそのまま証明された、またはM4だけ。
- **Why wrong:** sourceは限定範囲でのpositiveとuniversal readingのnegativeを同時に固定する。
- **Uncertainty note:** S2→S2*というlabel changeをM2とするかM14とするかは複数可。

## 4.5 Actual move versus available rescue

### AB-P1 — Positive: P0の選択肢と不採用branch

- **Source file:** `notes/theorem_proof_anatomy_experiment/00_origin/p0_generic_standards_baseline_v0.1.md`
- **Exact excerpt:** “**推奨は (i)。**” / “**(iii) を採らないことを明記する。**”
- **Correct coding:** one-code searchがactual route M4/M16。full P1–P5はavailableだがexplicitly not chosen。
- **Tempting wrong coding:** 表に存在する(ii)〜(iv)も`move_taken`へ列挙。
- **Why wrong:** sourceが採否を明記する。
- **Uncertainty note:** (iv) terminationはP1-reduced後にactualとなるので、P0時点と後続episodeを分ける。

### AB-P2 — Positive: self-containmentのwithdrawalと別の条件付き命題

- **Source file:** `notes/theorem_proof_anatomy_experiment/00_origin/tool_truth_absence_working_note_v0.2.md`
- **Exact excerpt:** “これは「自己包含定理」ではなく、自己包含に記録場所・候補範囲・有限容量を加えた命題である。”
- **Correct coding:** universal implicationのactual dispositionはM17。finite capacity resultは追加条件を持つ別のconditionally retained claim（M1/M4）で、元claimの看板を救済しない。
- **Tempting wrong coding:** assumptionsを加えてself-containment theoremが証明されたため、元claimはrescued。
- **Why wrong:** sourceが別命題であると明示する。
- **Uncertainty note:** ledgerを一行にするならactual moveとside branchを別欄に置く。二episode化も許す。

### AB-B1 — Boundary: reflection extensionは対象かmoveか

- **Source file:** `notes/theorem_proof_anatomy_experiment/01_theorem_anatomy/reflection_principles_scope_stress_test_ja.md`
- **Exact excerpt:** “reflection theory は、外部から旧理論 \(T\) を対象化して stronger theory を作る。この subject shift がなければ progression 全体を誤読する。”
- **Correct coding:** 数学的transition \(T\to T+\mathrm{RFN}_\Gamma(T)\) を対象episodeとするならM6/M3/M12。S2→S2*というmeta-vocabulary episodeだけを対象とするなら、M6は説明対象であって`move_taken`とは限らない。boundary依存で`AMBIGUOUS`。
- **Tempting wrong coding:** reflectionという語があれば常にM6、またはtheory extensionは単なるproof-resource M8。
- **Why wrong:** subject theory、extension、meta-label revisionは別transition。
- **Uncertainty note:** E11で最も重要なadjudication point。episode boundaryを先に決める。

### AB-B2 — Boundary: bridge theorem requirement

- **Source file:** `notes/theorem_proof_anatomy_experiment/01_theorem_anatomy/proof_theoretic_ordinal_stress_test_ja.md`
- **Exact excerpt:** “追加結論には、その calibration と theorem inclusion、conservation、interpretability等を結ぶ定理が要る。”
- **Correct coding:** 追加dependencyのsource-derived記述。実際にそのbridge theoremを採用・証明したとは書かれていないため、M8/M9/M10を`move_taken`にしない。`available_branches`も研究上の選択肢として明示されたかは`AMBIGUOUS`。
- **Tempting wrong coding:** bridge theorem追加によってsame ordinal=same theoryが救済された。
- **Why wrong:** sourceは追加結論が自動でない理由を述べ、bridge theoremの存在・採用を主張しない。
- **Uncertainty note:** dependency conditionとしてassumptions欄に置くかavailable branch欄に置くかはunresolvedを許す。

## 4.6 Added arbitrariness

### AA-P1 — Positive: lossを定義へ埋め込む

- **Source file:** `notes/theorem_proof_anatomy_experiment/00_origin/tool_truth_absence_working_note_v0.2.md`
- **Exact excerpt:** “「安定化」を多対一写像、「記録」を粗視化として定義すれば、非同型性を定義へ埋め込んでいるだけである。”
- **Correct coding:** conclusion-as-definitionによるtarget leakage / degenerate rescue。Aの直接観察可能なflag。正当なM1/M4 rescueとして数えない。
- **Tempting wrong coding:** lossy stabilization assumptionを加えれば定理が閉じるのでsuccessful assumption strengthening。
- **Why wrong:** 追加条件が結論を言い換えており、独立warrantがない。
- **Uncertainty note:** 特定の物理channelが独立に固定され、そのlossを証明する別episodeならdegenerateとは限らない。

### AA-P2 — Positive: quotientによる定義的一意性

- **Source file:** `notes/theorem_proof_anatomy_experiment/00_origin/tool_truth_absence_working_note_v0.2.md`
- **Exact excerpt:** “\(\cong\) を指定しなければ、同型な再記述を別存在論として数える自明化と、観測同値で全てを商にして一意性を定義的に得る自明化の両方が起こる。”
- **Correct coding:** equivalence relationが未固定、または成功を保証するよう選ばれる場合はtarget leakage / quotient launderingのflag。M5自体を常に否定しない。
- **Tempting wrong coding:** quotientを取れば一意性問題は一般に解決した。
- **Why wrong:** 何を同一視するかが結論を決めてしまう。
- **Uncertainty note:** field-native gauge equivalenceなど独立に正当化されたquotientのAは別評価。

### AA-B1 — Boundary: convenience sampleと既知のheader

- **Source file:** `notes/theorem_proof_anatomy_experiment/00_origin/p0_generic_standards_baseline_v0.1.md`
- **Exact excerpt:** “**選定経路** | **`convenience`。**” / “RFC が `Obsoletes:` / `Updates:` ヘッダを持つことは既知だった。したがって **`VER` と `RET` が立つことは選定前に予期していた。** 一方、`NONEVAL` と `OPEN` が現れるかは選定前に知らなかった”
- **Correct coding:** selection riskは直接観察可能。ただしtarget leakageはcodeごとに異なり、VER/RETでは高い懸念、NONEVAL/OPENでは同じ結論を出せない。Aはtyped `AMBIGUOUS/mixed`。
- **Tempting wrong coding:** convenienceだから全結果が恣意的、または事前開示したからAはゼロ。
- **Why wrong:** sourceは予備知識の範囲を限定している。
- **Uncertainty note:** 著者意図を推測せず、selection routeとknown informationだけを記録する。

### AA-B2 — Boundary: reflection formula classの固定

- **Source file:** `notes/theorem_proof_anatomy_experiment/01_theorem_anatomy/reflection_principles_scope_stress_test_ja.md`
- **Exact excerpt:** “formula class \(\Gamma\) は \(T\) の「性質」ではなく、どの reflection instances を追加するかという scope definition である。”
- **Correct coding:** \(\Gamma\)の追加・固定は観察できるが、それが恣意的かは比較目的、標準定理、independent warrantなしには判定不能。A=`UNKNOWN`。
- **Tempting wrong coding:** scope choiceはすべてarbitrary、または標準formula classだから自動的にnon-arbitrary。
- **Why wrong:** arbitrarinessは追加の事実であり、標準性・制限性だけからは出ない。
- **Uncertainty note:** 意図推定が必要なら必ずunresolved。

# 5. Withheld answer key for the frozen toy corpus

これは唯一の正解列ではない。sourceが直接固定する最小coreと、許容される複数codingを示す。`Ambiguity`は設計上の境界例であり、readerの失敗を意味しない。

| ID | Difficulty / flags | Minimal claim transition and witness | Expected move coding | Terminal status / key adjudication |
|---|---|---|---|---|
| E01 | easy | new general nonuniqueness theorem → prior art + \(O=\mathrm{id}\) → model/experiment-relative identifiability | M15, M17; M2/M4/M14 allowed | general novelty withdrawn; relative distinction established |
| E02 | hard; **ambiguous** | self-containment alone → encoder/recursion counterexamples → universal claim withdrawn; separate finite-capacity claim remains | main: M17/M14; side claim: M1/M4. Do not merge silently | withdrawn + separate conditional result. actual/rescue boundary |
| E03 | easy; **trivial-rescue/target-leakage** | generic stabilization loss → definitional circularity + reversible encoding → specified-channel question | M14, M15, M17; M4 allowed | universal claim withdrawn; concrete loss must be proved |
| E04 | medium; **ambiguous** | internal-specific pairwise/global obstruction → same external obstruction + prior art; fresh-preparation branch | M14, M15, M17; retained comparison may take M13. Fresh preparation is not main move | internal-specific use withdrawn; quantifier gap established |
| E05 | hard; **ambiguous; trivial-rescue/target-leakage** | general interface equivalence → stipulative equality/implementation existence conflation → two limited statements | M14, M17; conditional lemma may take M1/M4 as separate branch | general `[ESTABLISHED]` withdrawn. Definitional equality is not implementation theorem |
| E06 | medium | DR-1 weak positive → Erasure/prior-art reconstruction → frozen negative | M15, M17; field-native rewrite may also take M5/M7/M14 | frozen negative result; no new mechanism |
| E07 | easy; **label collision** | H1 unique diagnostic → frozen control duplicates all findings → organizational visibility only | M17 for H1/method value; M2 for organizational-only weakening; M16 for next real-record question. Source-local `M1` is not formation M1 | H1 not supported; source verdict `M1 — Organizational value` only |
| E08 | medium; **ambiguous boundary** | preservation/effectiveness reading → factual corrections + internal contradiction → documentary continuity only | M2, M14; uniqueness claim also M15/M17 where P0 is included | corrected documentary result; effectiveness untested |
| E09 | easy | 14-code program → generic absorption and one-code test → governance/artifact+n=1 → termination | M4, M15, M16, M17 | comparative methodology terminated; review remains |
| E10 | hard; **ambiguous composite** | closure-reversal candidate applied to Gödel → standard vocabulary and metalevel distinctions dominate → C1 | M12, M14, M15/M17. Do not treat diagonal proof as move | comparison metaphor only; Gödel I/II remain standard theorems |
| E11 | hard; **ambiguous; theory-extension** | broad self-guarantee label → local/uniform/global/soundness type split; external \(T^+\) distinguished from same-\(T\) | meta episode: M2/M3/M14/M17; mathematical extension sub-episode: M6 + M3 + M12 | S2* local only. M6 depends on episode boundary |
| E12 | hard; **ambiguous; calibration/metalevel** | universal ordinal scalar → relation/counterexample audit → fixed-package natural-family calibration | M13, M14, M2/M3/M4; metatheory distinction M12 | S2* limited; universal scalar denied |

### 5.1 Assumption and resource anchors

- E02の有限性、全初期状態、真部分系記録、\(|E|>1\)はconditional side claimのassumptions。encoder/quine/recursion examplesはfailure witnesses。
- E05のturn-based system、state map、commutation条件はconditional lemmaのassumptions。履歴長帰納法はproof route。
- E10の\(Q\)以上、c.e. axiomatization、consistencyはadopted Gödel–Rosser theorem assumptions。diagonal lemmaはproof resource。external consistencyからinternal unprovabilityを判断する箇所はM12に関係する。
- E11のbase、provability predicate、formula class、truth-expanded languageはscopeに応じたassumptions/definitions。diagonal lemma、partial truth、conservation theorem、GL/GLPはanalysis resources。
- E12のtheory、notation、formula class、reduction、metatheoryはcalibration package。cut elimination等はresourcesだが、個別relative-consistency theoremではwell-foundednessがassumptionにもなりうる。

### 5.2 Provenance anchors

- quoted claim/status/witnessはSOURCE-DERIVED。
- M-code、difficulty、episode grouping、primary/secondaryはINFERENCE。
- sourceが将来のreal-record auditや未証明bridgeを提案する場合のみOPEN HYPOTHESIS。提案をcompleted moveとしない。
- `ambiguous`と`trivial-rescue`のdesign flagはこのpackageのINFERENCEであり、source自身のstatus labelではない。

# 6. Expected fragility

## 6.1 Most fragile concepts

1. **Claim identity:** target、scope、statusが同時に変わると、“同じclaimの弱化”と“別claimへの移動”の境界がsourceだけでは一意でない。
2. **Episode boundary:** 一つのrevision fileが複数failure witnessesをまとめ、逆に一つのhypothesis testが複数fileへ分散している。
3. **Added arbitrariness:** 追加条件自体は観察できても、自然さ・独立warrant・意図はsource外推定になりやすい。

## 6.2 Likely inter-reader disagreements

- M2 conclusion weakening と M3/M4 scope restrictionの併記範囲。
- conditional side theoremを元claimのM1 rescueと数えるか、別episodeとするか。
- empirical protocolのcontrol / eligibility conditionをassumptionとresourceのどちらへ置くか。
- theory extensionがepisodeのactual moveか、stress testで比較される対象か。
- source固有のMetrology `M1`やstress-test `S2*`をformation move codeと誤読するか。
- prior-art absorptionをexact / partialのどちらとするか。
- `withdrawn`と、狭いremnantの`established/open`を一つのterminal statusへ潰すか。
- sourceが示す必要条件を`available branch`と呼べるか。
- Aでobserved selection riskとunobservable author intentを混ぜるか。

# 7. Gate to the Phase 0 finite toy experiment

次の条件が文章で確認できた場合だけ、同じ12 episodeを用いるPhase 0へ進む。

1. 全readerがanswer keyを見ず、同じfrozen corpus versionとcoder instructionsを用いて独立提出した。
2. 各episodeで、少なくともsource-derivedなbefore / witness / after / explicit statusを記録できるか、記録不能の理由を`UNKNOWN`としてsourceに結びつけた。
3. claim identityとepisode boundaryの相違が隠されず、複数boundaryを許す規則で記録された。
4. assumption/resource、M2/M3/M4、actual/availableの不一致を、新しいmoveやscoreなしで記述できた。
5. E03とE05のtarget-leakage候補を“証明が閉じた”として無条件に成功扱いしなかった。
6. E11でsame-\(T\) reflection、external theory extension、metalevel evaluationを混同しなかった。
7. source-derived / inference / open hypothesisの境界をadjudication後も保持できた。
8. unresolved判定がframeworkに不利という理由で上書きされなかった。
9. field-native terminologyをM-codeが置換せず、exact statementとstatusがcodeより先に残った。
10. recurring disagreementがsource wordingの不足によるものか、coder ruleの不明確さによるものかを区別できた。

gateを通らない場合は、計算・score化へ進まない。claim identity、episode boundary、またはassumption/resourceがadjudicatorの事後物語によってしか成立しないなら、基準文書のkill criteriaに従い、frameworkをannotated trajectory / ordinary revision ledgerへ降格する。

# 8. Package-level conclusion

最も壊れやすいのはclaim identity、episode boundary、added arbitrarinessである。最も頻繁なcoder間不一致候補はM2対M3/M4、M1対M8、actual move対available rescue、そしてM6がactual transitionか分析対象かという境界である。Phase 0へのgateは高い一致ではなく、sourceに基づいて一致・不一致・unresolvedを同じ規則で再構成できることである。

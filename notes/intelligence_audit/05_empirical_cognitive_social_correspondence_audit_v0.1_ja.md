# Intelligence independent audit — Phase05 empirical / cognitive / social correspondence

## 0. Status

```text
Intelligence audit: IN PROGRESS
Phase00–04: COMPLETE / inherited unchanged
Phase05 empirical / cognitive / social correspondence audit: COMPLETE
Phase06 revision candidate synthesis: NOT STARTED
Phase07 final audit / frozen dispositions: NOT STARTED
Theorem/proof validity: NOT AUDITED
Final dispositions: NOT ASSIGNED
Source revision: NOT STARTED
Equation revision: NOT STARTED
Distribution revision: NOT STARTED
```

本記録は観測対象と理論記述の対応成熟度を判定する。真偽・証明の正当性・新規実験・新規測度・改訂案は扱わない。記号や候補名の存在と、測定・抽出・校正・実行の存在を分ける。

主な結果: correspondence ceilingはformal-to-observable / cognitive / behavioral / biological / social / AIがCOR3、phenomenalがCOR1、cross-domainがX3、operational ceilingがOP2。いずれも上限を達成する局所候補があるという意味であり、全変数がその水準にあるのではない。Intelligence-specific operational maps / datasets / simulations / tested / validatedは0。新規研究route群24はすべてOPEN。

## 1. Authority inheritance / source scope

最上位authorityはPhase00–04と監査README。Phase00のPart I JA=current distributed build authority、Part I EN=current parallel source（primary status未確定）、Part II JA=primary manuscript、Part II EN=working English draftをそのまま継承する。ENを自動的にcanonicalへ昇格しない。P2A–Eは各言語のappendix authorityであり本文の独立validationではない。source_md/working Markdown/図/PDF/READMEのpresentation・履歴・navigation roleを混同しない。

Phase04固定値: claims95、support YES25/PARTIAL64/NO3/UNRESOLVED3、strong62（supported1/overstated25/possibly26/guarded4/version5/unresolved1）、gaps31（HIGH22/CRITICAL5/MEDIUM4）。FE2/CE2/SE2/BE3/PE1/XE2/PRE2/OE0を保持する。BE3は引用背景のみ、Int-specific biological mappingの実証ではない。Phase03のSERIOUS5 RETAIN、source-level vicious circularity established?: NO、global unfalsifiability established?: NOを変更しない。

I0=formal、I1=representational/computational、I2=cognitive/functional、I3=social/collective、I4=phenomenalはaudit layersである。LF/LR/LEやPart番号と同一視しない。以下のP1/P2§番号は次のsource mapに解決する。無印P2の細部はJA primaryを基準にEN draftを照合し、JA-only detailをENにもあると扱わない。略記CORR001/OBS001/OPEN001等は、それぞれINT-CORR-001/INT-OBS-001/INT-OPEN-001を指す。

| source unit | EN locator | JA locator |
|---|---|---|
| P1 abstract | intelligence-part1/sections/abstract.tex | intelligence-part1/sections_ja/abstract_ja.tex |
| P1 §1 | intelligence-part1/sections/01_introduction.tex | intelligence-part1/sections_ja/01_introduction_ja.tex |
| P1 §2 | intelligence-part1/sections/02_the_decomposition_perception_recognition_knowledge_and_intelligence.tex | intelligence-part1/sections_ja/02_the_decomposition_perception_recognition_knowledge_and_intelligence_ja.tex |
| P1 §3 | intelligence-part1/sections/03_minimal_axioms_of_intelligence.tex | intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex |
| P1 §4 | intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex | intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex |
| P1 §5 | intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex | intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex |
| P1 §6 | intelligence-part1/sections/06_the_gettier_problem_as_a_structural_diagnostic.tex | intelligence-part1/sections_ja/06_the_gettier_problem_as_a_structural_diagnostic_ja.tex |
| P1 §7 | intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex | intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex |
| P1 §8 | intelligence-part1/sections/08_the_non_closure_of_individual_intelligence.tex | intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex |
| P1 §9 | intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex | intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex |
| P1 §10 | intelligence-part1/sections/10_summary_convergence_and_outlook.tex | intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex |
| P2 §0 | intelligence-part2/sections/00_introduction.tex | intelligence-part2/sections/00_introduction_ja.tex |
| P2 §1 | intelligence-part2/sections/01_preliminaries.tex | intelligence-part2/sections/01_preliminaries_ja.tex |
| P2 §2 | intelligence-part2/sections/02_inference_operator.tex | intelligence-part2/sections/02_inference_operator_ja.tex |
| P2 §3 | intelligence-part2/sections/03_nonclosure_theorem.tex | intelligence-part2/sections/03_nonclosure_theorem_ja.tex |
| P2 §4 | intelligence-part2/sections/04_response_channels.tex | intelligence-part2/sections/04_response_channels_ja.tex |
| P2 §5 | intelligence-part2/sections/05_emergent_stopping_layer.tex | intelligence-part2/sections/05_emergent_stopping_layer_ja.tex |
| P2 §6 | intelligence-part2/sections/06_animism.tex | intelligence-part2/sections/06_animism_ja.tex |
| P2 §7 | intelligence-part2/sections/07_god.tex | intelligence-part2/sections/07_god_ja.tex |
| P2 §8 | intelligence-part2/sections/08_religion.tex | intelligence-part2/sections/08_religion_ja.tex |
| P2 §9 | intelligence-part2/sections/09_social_blockchain.tex | intelligence-part2/sections/09_social_blockchain_ja.tex |
| P2 §10 | intelligence-part2/sections/10_gettier_problem.tex | intelligence-part2/sections/10_gettier_problem_ja.tex |
| P2 §11 | intelligence-part2/sections/11_instability_region.tex | intelligence-part2/sections/11_instability_region_ja.tex |
| P2 §12 | intelligence-part2/sections/12_constructive_clauses.tex | intelligence-part2/sections/12_constructive_clauses_ja.tex |
| P2 §13 | intelligence-part2/sections/13_conclusion.tex | intelligence-part2/sections/13_conclusion_ja.tex |
| P2 A | intelligence-part2/appendices/appendix_a_master_table.tex | intelligence-part2/appendices/appendix_a_master_table_ja.tex |
| P2 B | intelligence-part2/appendices/appendix_b_homology.tex | intelligence-part2/appendices/appendix_b_homology_ja.tex |
| P2 C | intelligence-part2/appendices/appendix_c_part1_mapping.tex | intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex |
| P2 D | intelligence-part2/appendices/appendix_d_optional_notes.tex | intelligence-part2/appendices/appendix_d_optional_notes_ja.tex |
| P2 E | intelligence-part2/appendices/appendix_e_emergence_homology.tex | intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex |

66 included TeX filesの開始時hashはPhase04開始時から変更なし。sourceを再照合し、特にP1§3–9、P2§2–5/7–13、A–Eの応答・profile・phase・future記述を確認した。既存support表の結果を対応成熟度の代用にはしない。

## 2. Correspondence taxonomy

| level | 判定条件 |
|---|---|
| COR0 | 対応未所在。formal objectだけで観測との対応にならない |
| COR1 | verbal/qualitative naming |
| COR2 | structured role correspondence |
| COR3 | 理論変数/構造と名前を持つcandidate observableとの明示関係 |
| COR4 | operational definition / estimator |
| COR5 | calibrated / executed mapping |
| COR6 | independently validated mapping |

COR3はcandidateの具体性で判定し、identity記号の強さで判定しない。例えばQ→J/D→I、hidden states→S、vinf→step数/time、LR→記録はCOR3候補である。一方、Φext≡Φnetは独立した測定候補を二側に与えないためCOR2。COR3であってもsourceがそのcandidateを因果的・排他的に説明できるという判断ではない。

## 3. Operationalization taxonomy

| level | 判定条件 |
|---|---|
| OP0 | none |
| OP1 | observable concept named |
| OP2 | variable candidate named |
| OP3 | extraction rule / estimator specified |
| OP4 | calibration / threshold / units specified |
| OP5 | executed protocol |
| OP6 | validated protocol |

本phaseで最大OP2。P2JA§11.2のvinfは「単位時間あたりに生成する推論ステップの数」というrate候補を明示するが、何を一stepとするか、どのclockを使うか、human/AIでどう切り出すかを規定しない。これは数値抽出器を持つOP3ではない。rho_respの「局所測度」、Σの「測る量」、Cの「operational stability」も測度名を抽出規則へ読み替えない。P1§5のcm/hours-days等のscale例は存在するが、Intelligence変数のunits/calibrationへ移入しない。

## 4. Cross-scale taxonomy

| level | 判定条件 |
|---|---|
| X0 | vocabulary reuse only |
| X1 | structural analogy |
| X2 | role homology |
| X3 | explicit source→target variable correspondence |
| X4 | typed translation |
| X5 | implemented bridge |
| X6 | validated bridge |

same glyph/form/role≠same object/signature/dynamics。対応表をX3と数える場合でもstate space、unit、time、invariant、変換器は別のburdenである。X4以上のbridgeは未所在。upstream closure/downstream reuseをvalidationに使わない。

## 5. Primary correspondence inventory

最大成熟度はfamily内の最も具体的なsource-local candidateで判定する。一般主張への拡張はmissing bridge欄で制限する。E0は定義/式、E1はprofile/table/schema、E2はP1で引用された外部背景のみ。全行のInt-specific実行dataは未所在。

| CORR | object | theoretical role | proposed observable / absence | COR | OP | source locator | layer | unresolved mapping | evidence source kind |
|---|---|---|---|---|---|---|---|---|---|
| INT-CORR-001 | S / X | 状態空間 | P1:管網・Transformer hidden statesという実体候補。P2:Xは認知状態の抽象空間 | COR3 | OP2 | P1§3,5; P2§2 / EN set-valued F | I0→I1/I2 | 例の状態記録からS/Xへの符号化・P1/P2同一性なし | E0/E1; P1引用E2は背景のみ |
| INT-CORR-002 | F (P1 update) | 状態更新 | 管網の再配分、Transformer layer transition | COR3 | OP2 | P1§3,5 | I0→I1 | sourceで対応先を指定するが実行traceとの対応器なし | E0/E1; P1引用E2は背景のみ |
| INT-CORR-003 | F (P2 inference) | 正当化を進める推論 | 問い・仮説・判断更新 | COR2 | OP1 | P2§2–3 | I0→I2 | 推論step同定・入力出力・正当化評価の独立criterionなし | E0/E1 source-local prose/schema |
| INT-CORR-004 | J(x) | 正当化関数 | more justifiedという解釈のみ | COR1 | OP1 | P2§3,D | I0→I2 | 正当化score/annotator/順序判定なし; flux Jではない | E0/source-local formal definition |
| INT-CORR-005 | I | 未解決差分/情報密度 | P1 Dへのlexical対応; P2未解決推論緊張 | COR3 | OP2 | P1§4; P2§1–2 | I0→I1/I2 | D→Iは候補のみ。P2 tensionはCOR1、尺度未定 | E0/E1; P1引用E2は背景のみ |
| INT-CORR-006 | C | 閉包・運用安定性 | 判断の安定/改訂・停止との役割対応 | COR2 | OP1 | P2§1,10 | I0→I2 | truthと区別。安定の観測窓/値の抽出なし | E0/E1 source-local prose/schema |
| INT-CORR-007 | Cij | 二ノード閉包 | 対話等で環境が応答を返すこと | COR3 | OP2 | P2JA§2.5,4.1 | I0→I2/I3 | ρi/Hijの推定なし;応答有無だけでCij値は求まらない | E0/E1 source-local prose/schema |
| INT-CORR-008 | Φ (P1) | 全域bias | 管網の境界/栄養配置、学習weights/loss/data distribution | COR3 | OP2 | P1§3–5 | I0→I1 | 全域scalar値や同定法なし。複数carrierを同一量としない | E0/E1; P1引用E2は背景のみ |
| INT-CORR-009 | Φbio | 生物的全域bias | 栄養/境界条件・流れの全体拘束 | COR3 | OP2 | P1§5 | I0→I1/biological | 境界条件からfield値への写像なし; cited背景のみ | E0/E1; P1引用E2は背景のみ |
| INT-CORR-010 | Φtr | Transformer全域bias | 学習済重み・loss/training distributionの効果 | COR3 | OP2 | P1§5 | I0→I1 | loss/weights/分布を一scalarへ集約する規則なし | E0/E1; P1引用E2は背景のみ |
| INT-CORR-011 | Φext | 外部参照場 | 外部の停止参照/委任先 | COR2 | OP1 | P2§5.8,7 | I0→I2/I3 | 参照対象の存在とfield測定が別。独立field値なし | E0/E1 source-local prose/schema |
| INT-CORR-012 | Φnet | LE相互同期network | 共有参照・社会的受容 | COR2 | OP1 | P2§5.8,9 | I0→I3 | LE node/edge判定、集約、同期量なし | E0/E1 source-local prose/schema |
| INT-CORR-013 | Ωθ | 拘束下の運動可能領域 | 応答/沈黙として扱う範囲 | COR2 | OP1 | P2§2,4 | I0→I2 | 状態集合の外部抽出なし | E0/E1 source-local prose/schema |
| INT-CORR-014 | θ | 運動領域の拘束parameter | 応答性境界の位置、BioではDNA/反応傾向 | COR3 | OP2 | P2§2.6–7,B.4 | I0→I2/biological | Int側候補境界のみ。DNAからInt閾値への換算なし | E0/E1 source-local prose/schema |
| INT-CORR-015 | μθ | 閾値を内発的に組み替える能力 | 同じ環境を応答/沈黙として扱い分ける変化 | COR3 | OP2 | P2§2.7,4.3,11 | I0→I2 | 閾値shift推定・内発/受動分離・error独立基準なし | E0/E1 source-local prose/schema |
| INT-CORR-016 | LF | 推論層 | 粘菌流動/Transformer token生成/人間推論 | COR3 | OP2 | P2§5.4 | I0/I1→I2 | profileで具体対象、commonstep/認知判定は未定 | E0/E1 source-local prose/schema |
| INT-CORR-017 | LR | 再帰参照ログ層 | slime跡、weights/context、記憶・言語・記録 | COR3 | OP2 | P2§5.2,5.4,9 | I1→I2/I3 | storageの所在≠参照運動検出。凍結/動的を分ける | E0/E1 source-local prose/schema |
| INT-CORR-018 | LE | 外部依存停止attractor | 餌到達時network安定/判断停止のprofile | COR3 | OP2 | P2§5.3–5.4 | I0→I2 | 観測候補ありもLE独立検出なし;一般機構COR2 | E0/E1 source-local prose/schema |
| INT-CORR-019 | E (external stopping) | 停止operator | EOS/task仕様/外部decode制御とのstop-role対比 | COR3 | OP2 | P2§5.4,5.7 | I0→I1/I2 | EOSをEそのものとする実装写像なし | E0/E1 source-local prose/schema |
| INT-CORR-020 | H / Hij / Hji | 相互拘束と返りの方向 | 対話・実験・社会相互作用の出力と応答 | COR3 | OP2 | P2§2.5,4.1,5 | I0→I2/I3 | 方向別応答の選別・重み・時間窓なし | E0/E1 source-local prose/schema |
| INT-CORR-021 | ρresp | 応答channel密度 | 環境への応答性付与/応答channel | COR2 | OP1 | P2JA§1.8,6,A | I0→I2/I3 | 局所測度という名のみ、channelの母集団/分母なし | E0/E1 source-local prose/schema |
| INT-CORR-022 | vinf | 推論速度 | 単位時間あたり生成する推論step数 | COR3 | OP2 | P2JA§11.2 | I0→I2 | rate候補は明示。step抽出・時間単位・human/AI共通clockなし | E0/E1 source-local prose/schema |
| INT-CORR-023 | vLR | ログ参照速度 | 痕跡を再帰参照しpatternを取り込むrate | COR3 | OP2 | P2§11.2–4 | I0→I2 | 参照event切出し・取り込み判定・vinfとの単位整合なし | E0/E1 source-local prose/schema |
| INT-CORR-024 | Δvintel | 生成/参照速度差 | 上記二候補の差 | COR3 | OP2 | P2§11 | I0→I2 | 候補間relationは明示、rate estimator/critical値なし | E0/E1 source-local prose/schema |
| INT-CORR-025 | rres | 推論解像度 | 区別・因果分解の細かさ | COR3 | OP2 | P2§11.2 | I0→I2 | 区別の粒度符号化/scaleなし。定量値は未所在 | E0/E1 source-local prose/schema |
| INT-CORR-026 | η | 停止硬度 | 判断が改訂されやすい/されにくい | COR3 | OP2 | P2§11.2 | I0→I2 | 改訂抵抗候補は明示、観測条件とscoreなし | E0/E1 source-local prose/schema |
| INT-CORR-027 | Σ | LE発達度・活性度 | 独立endpoint未提示;量化を後続へ委ねる | COR1 | OP1 | P2JA§1.8,13.4,A | I0→I2 | phase region setではない;clinical指標を発明しない | E0/E1 source-local prose/schema |
| INT-CORR-028 | stopping | 複数の停止役割 | 判断終了/行動、EOS、中断、合意 | COR3 | OP2 | P1§8; P2§3,5,9 | I1→I2/I3 | 同じ観測から内部完結/外部停止を分けるruleなし | E0/E1 source-local prose/schema |
| INT-CORR-029 | knowledge | 暫定的停止構造 | 採用済み判断 | COR2 | OP1 | P1§2,6; P2§10 | I2 | truth/正当化/実用採用の独立codingなし | E0/E1 source-local prose/schema |
| INT-CORR-030 | intelligence | 改訂可能motion/三層維持状態 | 3profileと持続運用 | COR2 | OP1 | P1§3,5; P2§5,12 | I1→I2/I3 | 一般必要十分criterionなし。速度単独のscoreは明示的に拒む | E0/E1 source-local prose/schema |
| INT-CORR-031 | consensus / social block | 暫定的な共同停止 | 複数nodeが受容する判断・fork/merge | COR3 | OP2 | P2JA§9.2–3 | I2→I3 | 受容証拠/母集団/多数条件/期間なし | E0/E1 source-local prose/schema |
| INT-CORR-032 | legitimacy | 歴史的受容 | 誰がいつ受容したか・持続時間・責任 | COR3 | OP2 | P2JA§9.4 | I3 | factor列挙と正統性の選択criterionは別、非計算主張から測度作成不可 | E0/E1 source-local prose/schema |
| INT-CORR-033 | J / JI (flux) | 情報流の語彙 | P1 Q管流対応; CTではflowfield | COR3 | OP2 | P1§4; P2B | I0→I1 | Q→J lexicalのみ、J(x) justificationと非同一 | E0/E1; P1引用E2は背景のみ |
| INT-CORR-034 | JC | 閉包flux | 直接観測候補なし | COR0 | OP0 | P2JA§1,A | I0 | closure PDEの記号、知性測定写像なし | E0/source-local formal definition |
| INT-CORR-035 | Φ(L,H) | 創発schema/operator | 下位運動＋相互拘束→上位層の役割表 | COR2 | OP1 | P2§1,5,E | I0→I2 | scalar Φと型別; 実行/上位検出/収束modeなし | E0/E1 source-local prose/schema |
| INT-CORR-036 | Qij / Dij / Lij / pi | Physarum参照model | 流れ・conductance・管長・圧力 | COR3 | OP2 | P1§4–5 | I0→biological | 外部sourceの対象名; repo原データもInt変換器もなし | E0/E1; P1引用E2は背景のみ |
| INT-CORR-037 | \|V\| / \|E\| / b / d | 推論graph | 命題node/接続・分岐数・depth | COR3 | OP2 | P1JA§7; EN§7 | I0→I1/I2 | graphを所与にすれば組合せ量、認知発話→graph抽出なし | E0/E1 source-local prose/schema |
| INT-CORR-038 | I(s) / div J | 分岐領域の未解決量/発散 | 選択肢/枝増加との解釈 | COR2 | OP1 | P1§7 | I0→I2 | branch countと同一量にしない; formalfluxと心理発散の橋なし | E0/E1 source-local prose/schema |
| INT-CORR-039 | S predicate | 内部stop二値述語 | rule内ではS=1→F(x)=x;行動候補なし | COR0 | OP0 | P2§3,D | I0 | formalpredicate≠observable stop classifier | E0/source-local formal definition |
| INT-CORR-040 | Ftr | layer更新 | hidden state列/layer index | COR3 | OP2 | P1§5 | I0→I1 | 対象model/dump/iteration照合なし | E0/E1; P1引用E2は背景のみ |
| INT-CORR-041 | Fbio(x;θ) | 生物局所発展との比較 | 反応傾向と環境条件 | COR2 | OP1 | P2§2,B.4–5 | I0→biological | 同名F非同一、Bioclosure継承なし | E0/E1 source-local prose/schema |
| INT-CORR-042 | Cmax / horizon | 完全閉包境界 | ultimate understandingという解釈 | COR1 | OP1 | P1§9; P2§1,3,D | I0→I2 | 理解の独立endpoint/境界測定なし | E0/E1 source-local prose/schema |
| INT-CORR-043 | τ / t / n | 時間/更新順序 | P1 sequence・Transformer layer index | COR3 | OP2 | P1§3,5,9; P2§11,A | I0→I1/I2 | 順序と物理/生物/社会時間を統合しない | E0/E1 source-local prose/schema |

### 5.1. 95 primary claimsへの照合索引

support statusは再判定せずPhase04から保持する。SCOPEはnegative/local-scope statementで、経験測定を必須とせず、対応を過剰に輸入しないための境界。Xは§22–23のcross-domain ledgers、FUTUREは§25の将来課題。CLM081の旧略称にΣ相図という語があっても、Phase01で区別した通りΣは発達度でありregion setとしない。

| claim | source locator | correspondence ledger / boundary |
|---|---|---|
| INT-CLM-001 | P1 E/J abstract,§1–2 | CORR030 |
| INT-CLM-002 | P1 E/J §2 | CORR030, CORR029 |
| INT-CLM-003 | P1 E/J §2,6 | CORR029, CORR006 |
| INT-CLM-004 | P1 E/J §2 | CORR030, CORR017 |
| INT-CLM-005 | P1 E/J §3,10 | CORR001, CORR008, CORR043 |
| INT-CLM-006 | P1 E/J §3 | CORR001 |
| INT-CLM-007 | P1 E/J §3 | CORR043 |
| INT-CLM-008 | P1 E/J §3–4 | CORR008 |
| INT-CLM-009 | P1 E/J §3 | SCOPE |
| INT-CLM-010 | P1 E/J §4 | CORR005, CORR008, CORR033 |
| INT-CLM-011 | P1 E/J §4 | CORR005, CORR033, CORR036 |
| INT-CLM-012 | P1 E/J abstract,§4–5,10 | CORR008, CORR009, CORR036 |
| INT-CLM-013 | P1 E/J §5 | CORR001, CORR009, CORR010, CORR040 |
| INT-CLM-014 | P1 E/J §5 | SCOPE |
| INT-CLM-015 | P1 E/J §6 | CORR029, CORR006 |
| INT-CLM-016 | P1 E/J §6 | CORR029, CORR004 |
| INT-CLM-017 | P1 E/J §7 | CORR037, CORR038 |
| INT-CLM-018 | P1 E/J §7 | CORR037 |
| INT-CLM-019 | P1 E/J §7 | CORR022, CORR028 |
| INT-CLM-020 | P1 J §7 | CORR038 |
| INT-CLM-021 | P1 E/J §8 | CORR028, CORR039 |
| INT-CLM-022 | P1 E/J §8（J詳細） | CORR028 |
| INT-CLM-023 | P1 E/J §8（J強化） | CORR028 |
| INT-CLM-024 | P1 E/J §8–9 | CORR017, CORR028, CORR031 |
| INT-CLM-025 | P1 E/J §9 | CORR042 |
| INT-CLM-026 | P1 E/J §1,9 | CORR042 |
| INT-CLM-027 | P1 E/J §9 | CORR028, CORR031 |
| INT-CLM-028 | P1 E/J §9 | SCOPE |
| INT-CLM-029 | P1 E/J §9 | X |
| INT-CLM-030 | P1 J §9 | X |
| INT-CLM-031 | P1 E/J §1,9 | X |
| INT-CLM-032 | P1 J §9; Con参照 | X |
| INT-CLM-033 | P1 E/J §10 | SCOPE |
| INT-CLM-034 | P1 E/J §10 | X |
| INT-CLM-035 | P1 E/J §10 | FUTURE |
| INT-CLM-036 | P2 J §0; E abstract | X |
| INT-CLM-037 | P2 E/J §0,5,12 | CORR016, CORR017, CORR018 |
| INT-CLM-038 | P2 E/J §0 | CORR031, CORR032 |
| INT-CLM-039 | P2 J §0.2 | X |
| INT-CLM-040 | P2 E/J §1,10 | CORR006 |
| INT-CLM-041 | P2 J §1,A; E簡略 | CORR034 |
| INT-CLM-042 | P2 E/J §1,3 | CORR042 |
| INT-CLM-043 | P2 E/J §1–2 | CORR013, CORR014 |
| INT-CLM-044 | P2 E/J §1,E | CORR035 |
| INT-CLM-045 | P2 E/J §1,B,E | X |
| INT-CLM-046 | P2 E/J §2 | CORR003 |
| INT-CLM-047 | P2 E/J §2,5 | CORR016, CORR036, CORR040 |
| INT-CLM-048 | P2 J §2 | CORR007, CORR020 |
| INT-CLM-049 | P2 E/J §2,5 | CORR015 |
| INT-CLM-050 | P2 J §2,B | CORR014, CORR015 |
| INT-CLM-051 | P2 E/J §3,D | CORR003, CORR004 |
| INT-CLM-052 | P2 E/J §3; J D | CORR039 |
| INT-CLM-053 | P2 E/J §3; J D | CORR042 |
| INT-CLM-054 | P2 E/J §3; J D | CORR028 |
| INT-CLM-055 | P2 E/J §4 | CORR020, CORR014 |
| INT-CLM-056 | P2 E/J §4 | CORR038 |
| INT-CLM-057 | P2 E/J §4–5 | CORR017, CORR018 |
| INT-CLM-058 | P2 E/J §5 | CORR017 |
| INT-CLM-059 | P2 E/J §5 | CORR018 |
| INT-CLM-060 | P2 E/J §5 | CORR015, CORR018, CORR035 |
| INT-CLM-061 | P2 E/J §5 | CORR016, CORR017, CORR018, CORR019 |
| INT-CLM-062 | P2 E/J §5; J B | X |
| INT-CLM-063 | P2 E/J §5 | CORR019 |
| INT-CLM-064 | P2 E/J §5,D | CORR011, CORR012 |
| INT-CLM-065 | P2 E/J §5,C | CORR008, CORR012 |
| INT-CLM-066 | P2 E/J §5,10 | CORR006, CORR028 |
| INT-CLM-067 | P2 E/J §6 | CORR021 |
| INT-CLM-068 | P2 J §6 | CORR021 |
| INT-CLM-069 | P2 E/J §7 | CORR011, CORR012 |
| INT-CLM-070 | P2 E/J §7 | CORR011, CORR012 |
| INT-CLM-071 | P2 E/J §8 | CORR021, CORR031 |
| INT-CLM-072 | P2 E/J §8–9,D | CORR031 |
| INT-CLM-073 | P2 E/J §8 | CORR026 |
| INT-CLM-074 | P2 E/J §9 | CORR031 |
| INT-CLM-075 | P2 E/J §9 | CORR031 |
| INT-CLM-076 | P2 E/J §9 | CORR032 |
| INT-CLM-077 | P2 E/J §9 | CORR031 |
| INT-CLM-078 | P2 E/J §10 | CORR006, CORR029 |
| INT-CLM-079 | P2 J §10（EN簡略） | CORR029, CORR031 |
| INT-CLM-080 | P2 J §10,D; E弱いcoupling | CORR015 |
| INT-CLM-081 | P2 E/J §11 | CORR022, CORR025, CORR026, CORR027 |
| INT-CLM-082 | P2 E/J §11 | CORR024 |
| INT-CLM-083 | P2 E/J §11 | CORR022, CORR025, CORR030 |
| INT-CLM-084 | P2 E/J §11 | CORR022, CORR024 |
| INT-CLM-085 | P2 J §12; E7clauses | CORR030 |
| INT-CLM-086 | P2 J §12; E §12 | CORR030, CORR015 |
| INT-CLM-087 | P2 E/J §0,5,12 | CORR015, CORR018 |
| INT-CLM-088 | P2 E/J §0,13 | SCOPE |
| INT-CLM-089 | P2 E/J §5,13,D,E | FUTURE |
| INT-CLM-090 | P2 J A; E A辞書 | X |
| INT-CLM-091 | P2 J B; E B短縮 | X |
| INT-CLM-092 | P2 J C; §13 | FUTURE |
| INT-CLM-093 | P2 E/J E | CORR035, CORR018 |
| INT-CLM-094 | P2 E D; revision_notes | CORR019 |
| INT-CLM-095 | P2 E/J §0,8,D | SCOPE |

## 6. Observable inventory

sourceに名前/例として現れる25 candidate families。全行でrepo measured=NO、Int dataset=未所在、calibrated threshold=未所在。unitの名前や時間scale例があってもInt測定単位の設定とはしない。extraction欄は実行規則の欠如を明記し、当監査が新しい観測量を提案するものではない。

| OBS | candidate | source term | domain | direct/indirect | qualitative/quantitative | source | extraction / unit / threshold status | independent criterion |
|---|---|---|---|---|---|---|---|---|
| INT-OBS-001 | 管網の流れ/管のconductance | Q/D | 生物 | 直接候補 | quantitative | P1§4–5 | 外部modelの変数、Int再測定なし | 外部paper背景;独立Int対応criterionなし |
| INT-OBS-002 | 管長/圧力/接続 | Lij/pi/network | 生物 | 直接候補 | quantitative | P1§4 | 管網変数。Int側換算なし | physical quantitiesとcognitive labels非同一 |
| INT-OBS-003 | maze/path形成・栄養源到達 | maze/food/paths | 生物 | 直接候補 | qualitative/quantitative candidate | P1§5; P2§5.4 | pathと到達の例のみ | 停止判定≠LE独立検出 |
| INT-OBS-004 | rhythmic flow / oscillation | rhythmic shuttle | 生物 | 直接候補 | temporal candidate | P1§5 | 周期抽出/clockはこのrepoにない | 外部citation背景 |
| INT-OBS-005 | slime跡と再参照/忌避 | externalized log | 生物 | 直接候補 | qualitative | P2§5.4 | trailはcarrier候補、ログ利用判定なし | 記録の存在≠recursive reference |
| INT-OBS-006 | hidden-state sequence | hidden vectors h / Ftr | AI | 内部記録候補 | quantitative candidate | P1§5 | layer対応のみ、model runなし | architecture記述≠Intcalibration |
| INT-OBS-007 | layer order | layer index | AI | 直接候補 | discrete | P1§5 | 更新順序は明示、他時間との換算なし | 物理時間ではない |
| INT-OBS-008 | attention/weights/training distribution | global bias | AI | 内部記録候補 | quantitative candidate | P1§5 | Φtrへの数値抽出なし | 複数carrierを同一fieldとしない |
| INT-OBS-009 | token generation/context reference | LF/LR | AI | 内部記録候補 | discrete/temporal | P2§5.4 | 生成・参照の実行ログなし | token生成≠cognitiveinferencecriterion |
| INT-OBS-010 | EOS/task/decoding termination | external stopping | AI | 直接候補 | discrete | P2§5.4 | 対象model・終端選別protocolなし | selfLE不在をEOS観測だけで判定不可 |
| INT-OBS-011 | 出力への応答/無応答 | responsive/silent | 認知/環境/社会 | 直接候補 | binary-like qualitative | P2§2.6,4.1–3 | 応答window/有意判定なし | 無応答≠channel不存在 |
| INT-OBS-012 | 判断終了/行動へ移る | stopping | 認知/行動 | 直接候補 | qualitative | P2§5.1 | 停止・中断・完結の選別なし | 内部/外部cause独立判定なし |
| INT-OBS-013 | 疲労等による中断と再開 | resumption | 行動/生物 | 直接候補 | temporal qualitative | P1§8 | 時間/同じ推論の判定なし | 可能例を全称予測にしない |
| INT-OBS-014 | 判断・仮説更新の頻度 | vinf | 認知 | 間接候補 | rate candidate | P2JA§11.2 | 単位時間/step数という意味のみ、event抽出なし | OP2;算式形だけでOP3にしない |
| INT-OBS-015 | 痕跡参照/pattern取込rate | vLR | 認知 | 間接候補 | rate candidate | P2§11.2–4 | 参照/取込eventの認定なし | 生成rateと同一単位未確定 |
| INT-OBS-016 | 因果分解/区別の細かさ | rres | 認知 | 間接候補 | ordinal candidate | P2§11.2 | 分解/粒度のcodingなし | 高解像度≠正しさ |
| INT-OBS-017 | 判断の改訂されやすさ | η | 認知 | 間接候補 | ordinal candidate | P2§11.2 | 同じ条件での比較ruleなし | 停止硬度と硬直endpointの重複注意 |
| INT-OBS-018 | 応答性境界の移動 | θ/μθ | 認知 | 間接候補 | qualitative/parameter candidate | P2§2.7,4.3 | 前後境界推定も内発分離も未提示 | μを結果から逆同定するrisk |
| INT-OBS-019 | 命題/接続/branch/depth | V/E/b/d | 推論graph | 間接候補 | count candidate | P1§7 | 所与graphの数と認知graph抽出を区別 | 正しさから辺が増える写像なし |
| INT-OBS-020 | 判断と理由の永続記録 | social log | 社会 | 直接候補 | record candidate | P2JA§9.2 | corpus/記録選別なし | records≠LR再帰の実行証拠 |
| INT-OBS-021 | 複数nodeによる採用判断 | block/consensus | 社会 | 直接候補 | event candidate | P2JA§9.2–3 | 受容/複数/期間のruleなし | 成立条件を後付けしない |
| INT-OBS-022 | 分岐・統合・破棄/rollback cost | fork/merge | 社会/計算比較 | 間接候補 | qualitative cost | P2§9.3 | cost単位/同条件比較なし | Git比喩は実装protocolでない |
| INT-OBS-023 | 儀礼/祈り/禁忌/祝祭 | maintenance | 社会 | 直接候補 | practice candidate | P2§8.2–3 | case/corpus選択なし | 観察行為と維持機能の独立criterionなし |
| INT-OBS-024 | 受容主体・時期・持続・責任 | legitimacy factors | 社会/歴史 | 直接/間接候補 | record/temporal candidate | P2JA§9.4 | 史料/期間/責任codingなし | 因子の列挙≠正統性classifier |
| INT-OBS-025 | 改訂/errorを許容する運用 | error tolerance | 認知/社会 | 間接候補 | qualitative | P2JA§10.6,12 | errorの独立判定/訂正endpointなし | μ同値の定義を独立測度としない |

## 7. Cognitive correspondence

| ID | cognitive term | theoretical object | endpoint | behavior candidate | COR | OP | source | missing bridge |
|---|---|---|---|---|---|---|---|---|
| INT-COGCORR-001 | inference | F/LF | 問い・仮説更新 | OBS014 | COR2 | OP1 | P2§2–3 | 認知step→Fの同定なし |
| INT-COGCORR-002 | justification | J(x) | より正当化された状態 | なし | COR1 | OP1 | P2§3,D | truth/score/改訂と区別する尺度なし |
| INT-COGCORR-003 | stopping | S/E/LE | 判断終了/行動 | OBS012 | COR3 | OP2 | P2§3,5 | 観測stopと不動点の同一判定なし |
| INT-COGCORR-004 | knowledge | stopping structure | 採用済判断 | OBS012/021 | COR2 | OP1 | P1§2,6; P2§10 | 採用と真/知識の独立endpointなし |
| INT-COGCORR-005 | revision | μ/η | 判断変更/応答扱い変更 | OBS017/018/025 | COR3 | OP2 | P2§10–12 | 条件/内発性/誤りcriterionなし |
| INT-COGCORR-006 | memory/log | LR | 過去痕跡の再参照 | OBS005/009/020 | COR3 | OP2 | P2§5,9 | 保存と因果的参照を分けるruleなし |
| INT-COGCORR-007 | reasoning speed | vinf | 更新頻度 | OBS014 | COR3 | OP2 | P2§11.2 | step segmentationなし |
| INT-COGCORR-008 | resolution | rres | 区別・因果分解の粒度 | OBS016 | COR3 | OP2 | P2§11.2 | coding scaleなし |
| INT-COGCORR-009 | rigidity | η/LE | 停止の固定/改訂抵抗 | OBS017 | COR3 | OP2 | P2§11 | ηと結果側rigidityを独立にしない |
| INT-COGCORR-010 | error tolerance | μ | 誤りうる/改訂する構造 | OBS025 | COR2 | OP1 | P2JA§10.6,D | error測定でなくrevisability定義 |
| INT-COGCORR-011 | free inference | movable stops | 有限系で推論が持続 | OBS018 | COR2 | OP1 | P2§5,12 | 自由の主観報告や独立function testなし |
| INT-COGCORR-012 | instability | Δv/三軸 | 生成と参照の不均衡 | OBS014/015 | COR3 | OP2 | P2§11 | 崩壊marker/critical値なし |
| INT-COGCORR-013 | overexplanation | branching/regress | 説明・正当化の増殖 | OBS019 | COR2 | OP1 | P1§7; P2§4 | 心理負荷/説明過多の独立criterionなし |
| INT-COGCORR-014 | fourfold collapse | LF/LR/LE/Φnet | 層の機能不全 | OBS014/015/017 | COR2 | OP1 | P2§11.4 | 同じ生成・硬直記述から全層を逆同定不可 |

## 8. Behavioral correspondence

source-implied behaviorだけを記録する。response latency test、feedback correction task等を追加しない。ここでの9行はbehavior候補群の数であり、Phase04から継承する16 failure directionsの成熟度件数とは別母数。

| ID | behavior | source | observable | maturity | missing rule |
|---|---|---|---|---|---|
| INT-BEHCORR-001 | 判断終了/行動 | P2§5.1 | OBS012 | measurable candidate | choice/task条件・終了と内部完結の区別なし |
| INT-BEHCORR-002 | 環境への出力に応答が返る | P2§4 | OBS011 | measurable candidate | 対話/実験という例、response latency protocolなし |
| INT-BEHCORR-003 | 同じ環境の応答/沈黙扱いを変える | P2§2.7,4.3 | OBS018 | measurable candidate | 再開/閾値変更を独立codingしていない |
| INT-BEHCORR-004 | 判断を改訂/誤りを許容 | P2§10,12 | OBS017/025 | conceptual | feedback後correction trialは未指定 |
| INT-BEHCORR-005 | 推論が持続する | P1§3,8; P2§12 | OBS014 | conceptual | 持続のduration/cutoffなし |
| INT-BEHCORR-006 | 推論分岐が増える | P1§7 | OBS019 | conceptual | actualreasoning→graphなし |
| INT-BEHCORR-007 | EOS/task/decodeで止まる | P2§5.4 | OBS010 | measurable candidate | 対象モデルのbenchなし |
| INT-BEHCORR-008 | 疲労中断後に再開しうる | P1§8 | OBS013 | measurable candidate | 一つの例、universalrecoveryではない |
| INT-BEHCORR-009 | 過去ログを現在推論へ反映 | P2§5.2 | OBS009/020 | conceptual | 記録存在と参照の機能検出の橋なし |

## 9. Biological correspondence

引用文献のPhysarum対象とIntelligenceへの対応を二段階に分ける。外部文献そのものをwebで確認せず、sourceの引用/要約範囲のみを記録する。BE3からCOR5/OP5を導かない。

| ID | subject | theory correspondence | candidate | COR | OP | source | missing bridge |
|---|---|---|---|---|---|---|---|
| INT-BIOCORR-001 | Physarum flow | Q→J / LF | OBS001 | COR3 | OP2 | P1§4–5; P2§5.4 | 引用された管網modelとInt写像は別 |
| INT-BIOCORR-002 | conductance/geometry | D→I; Lij/pi | OBS001/002 | COR3 | OP2 | P1§4 | 数値変換/Int同定なし |
| INT-BIOCORR-003 | maze/path/food | trajectory/LE-like stop | OBS003 | COR3 | OP2 | P1§5; P2§5.4 | 外部behavior背景とLE独立検出は別 |
| INT-BIOCORR-004 | oscillation | temporal ordering | OBS004 | COR3 | OP2 | P1§5 | 共通time/周期推定なし |
| INT-BIOCORR-005 | external slime log | LR | OBS005 | COR3 | OP2 | P2§5.4 | trail/avoidance source記述、repo新測定なし |
| INT-BIOCORR-006 | biological threshold | DNA/反応傾向θ | 反応/環境条件 | COR2 | OP1 | P2§2.7,B.4 | Intθとの換算未定 |
| INT-BIOCORR-007 | Bio second attractor | Ωlife/Ωintel→LE比較 | なし | COR2 | OP0 | P2§1,5,E | set relation≠LE observable |
| INT-BIOCORR-008 | interruption/homeostasis | fatigue/metabolic limits | OBS013 | COR2 | OP1 | P1§8–9 | 生理指標/採血等を新規追加しない |

## 10. Transformer / AI correspondence

architecture factはsourceが述べる内容のラベルであり、現在の全AIへの外部事実認定ではない。全行でbenchmark/data/executable mapping=未所在。学習済weightsを凍結LR、contextを動的/揮発LRとするsourceの区別を保存する。

| ID | subject | theory correspondence | candidate | COR | OP | source | missing bridge |
|---|---|---|---|---|---|---|---|
| INT-AICORR-001 | hidden state | S / hidden vectors h | OBS006 | COR3 | OP2 | P1§5 | モデル/checkpoint/runなし |
| INT-AICORR-002 | layer index | temporalorder | OBS007 | COR3 | OP2 | P1§5 | physicalclockと同一でない |
| INT-AICORR-003 | attention | globalinteraction | OBS008 | COR3 | OP2 | P1§5 | attention値→Φtr estimatorなし |
| INT-AICORR-004 | weights/loss/data distribution | Φtr/globalbias | OBS008 | COR3 | OP2 | P1§5 | architecture背景のみ、独立Intmap未実行 |
| INT-AICORR-005 | context | dynamic/volatileLR | OBS009 | COR3 | OP2 | P2§5.4 | 参照利用のtrace/scoreなし |
| INT-AICORR-006 | training weights | frozenLR | OBS008 | COR3 | OP2 | P2§5.4 | 凍結保存を再帰運動と同一視不可 |
| INT-AICORR-007 | EOS | externalstopprofile | OBS010 | COR3 | OP2 | P2§5.4 | EOS観測≠selfLE不存在の十分条件 |
| INT-AICORR-008 | task specification/decode | suppliedstop/E比較 | OBS010 | COR3 | OP2 | P2§5.4 | 実際の制御codeなし |
| INT-AICORR-009 | self-generated LE/μ | ownstop/threshold | なし | COR2 | OP1 | P2§5.4 | 自前/外部の独立判定なし;sourceのprofileに限定 |
| INT-AICORR-010 | speed/autonomy | vinf/Δv/phase | OBS014/015 | COR3 | OP2 | P2§11 | benchmark/対象agent/閾値なし |
| INT-AICORR-011 | external evaluator/logs | externalizedstop | 外部評価/社会応答のrole | COR2 | OP1 | P1§8–10; P2§5,13 | 実装案/安全protocolは未来課題のみ |
| INT-AICORR-012 | paperclip/AI safety | nonclosurethoughtcase | なし | COR1 | OP0 | P1§8–10 | thought experimentで実験dataなし |

## 11. Social correspondence

歴史categoryそのものはobservableでない。具体的に名指しされた儀礼・記録・共同受容をcandidateと数えても、その社会的機能や普遍性の測定にはならない。全行でdataset/corpus/selection rule/比較criterion=未所在。

| ID | subject | theory correspondence | candidate | COR | OP | source | missing bridge |
|---|---|---|---|---|---|---|---|
| INT-SOCCORR-001 | animism | response-channel installation | 応答的に扱う自然対象 | COR2 | OP1 | P2§6 | 対象選択・channel判定なし |
| INT-SOCCORR-002 | God | centralizedstoppingreference | 委任/中心化の記述 | COR2 | OP1 | P2§7 | node/中心性/曖昧性の測定なし |
| INT-SOCCORR-003 | religion | maintenance | 儀礼・祈り・禁忌・祝祭 | COR3 | OP2 | P2§8 | practiceは名指し、機能判定とcase選択なし |
| INT-SOCCORR-004 | science | revisionmanagement | 停止の改訂という役割 | COR2 | OP1 | P2§8–9 | 研究実践corpus/改訂codingなし |
| INT-SOCCORR-005 | social blockchain | log/block/fork/merge | 判断理由記録/受容判断 | COR3 | OP2 | P2§9.2 | 実行protocolでない、acceptedblock選別なし |
| INT-SOCCORR-006 | consensus | provisionalstop | 複数nodeによる判断受容 | COR3 | OP2 | P2§9.2–3 | 誰/何人/何期間という条件なし |
| INT-SOCCORR-007 | legitimacy | historicallysustainedacceptance | 受容者/時期/持続/責任 | COR3 | OP2 | P2§9.4 | 因子候補だけ。正統性classifierなし |
| INT-SOCCORR-008 | institutionalstopping | LE/network運用 | 制度/共同体の停止形態 | COR2 | OP1 | P2§9,11 | 制度集団→LE edgeの規則なし |
| INT-SOCCORR-009 | maintenance/revision | 停止の維持/変更 | 儀礼/記録/判断の変更 | COR3 | OP2 | P2§8–9 | 独立maintenanceendpointなし |
| INT-SOCCORR-010 | centralization/ambiguity | 圧縮と停止曖昧性低下 | 定量indicatorなし | COR2 | OP1 | P2§7 | 中心化を結果から逆定義しない |
| INT-SOCCORR-011 | individualcreation/socialstabilization | 役割分担 | 個人判断と共同受容 | COR2 | OP1 | P2§9 | 創造event/帰属ruleなし |
| INT-SOCCORR-012 | socialcost | fork/merge/rollback | 分岐/統合/破棄の高低 | COR3 | OP2 | P2§9.3 | commonunit/比較対象群なし |

## 12. Historical correspondence

全6行でInt-specific dates、選択済case corpus、selection criteria、systematic comparative history、counterexample collection、longitudinal dataは未所在。一般的な歴史形態名・世代という時間語と史料datasetを区別する。figure7は運用レパートリーであり、測定した時系列と扱わない。

| ID | historical category | source claim kind | source | record/selection status |
|---|---|---|---|---|
| INT-HISTCORR-001 | animism | structural historical interpretation | P2§6 | 自然対象例、日時/文化case/corpus/選択規則なし |
| INT-HISTCORR-002 | God/centralization | causal historical reading | P2§7 | 圧縮・委任による説明、具体史料/比較群なし |
| INT-HISTCORR-003 | religion | structural historical interpretation | P2§8 | 世代を跨ぐ維持;儀礼名はあるが縦断recordなし |
| INT-HISTCORR-004 | science | case naming / revision role | P2§8–9 | 改訂重視の対比、史料selection/counterexample listなし |
| INT-HISTCORR-005 | social blockchain | functional comparison | P2§9 | Gitとのcost対比、実社会protocol/corpusなし |
| INT-HISTCORR-006 | staircase/evolution | non-progress repertoire | P2§9 figure7 | 年代順dataではない;混在/nonlinear guard維持 |

## 13. Phenomenal correspondence

自由/責任の主たるsource roleはI2/I3であり、そのままI4の観測endpointとしない。P2JA§13は意味・主観性・理解をfuture哲学へ送る。全行で独立report measure/実測behavioral proxy=未所在、Con引用はcompanionの説明を移入する許可でない。

| ID | term | endpoint/source role | source | COR | OP | independent report / proxy |
|---|---|---|---|---|---|---|
| INT-PHENCORR-001 | freedom | 自由な推論の持続;I2が中心 | P2§0,5,12 | COR1 | OP1 | 主観的自由感との写像は未提示 |
| INT-PHENCORR-002 | burden/exhaustion | 無限後退/責任負担の語 | P1§7–8; P2§3,7 | COR1 | OP1 | 自己報告・生理proxyなし |
| INT-PHENCORR-003 | understanding | ultimate understanding / futurephilosophy | P1§9; P2§13 | COR1 | OP1 | feltunderstanding独立criterionなし; futureのみ |
| INT-PHENCORR-004 | subjectivity/conscious access | companion navigation / negative scope | P1§1,9; P2§13 | COR0 | OP0 | Conの対応を移入しない |
| INT-PHENCORR-005 | responsibility | 社会的委任/受容;I3 | P2§6–7,9,13 | COR1 | OP1 | responsibility感のmeasureなし |
| INT-PHENCORR-006 | uncertainty relief | 未決定性の消去でなく保持責任委任 | P2§7 | COR0 | OP0 | reliefという実測endpoint未所在。委任を主観的安堵へ読み替えない |

## 14. Stopping operationalization

観測された終端がsourceのいうgenuine stoppingを十分に同定するというruleは未所在。fixed pointとbinary Sはformal relationとして記載されるが、認知的中断との境界判定を与えない。sourceのTHM001–004のproof validityをここで論じない。

| ID | kind | formal/theory role | observable | COR | OP | source | independent classification |
|---|---|---|---|---|---|---|---|
| INT-STOPCORR-001 | fixed point | F(x)=x | formal state equality only | COR0 | OP0 | P2§3,D | 認知終了のobservableなし; theorem premiseの正誤は未判定 |
| INT-STOPCORR-002 | binary S | 停止述語 | S=1と不動点のsource-local関係 | COR0 | OP0 | P2§3,D | 実際の停止classifier未指定 |
| INT-STOPCORR-003 | task termination | EOS/task/decode | 終了token/制御 | COR3 | OP2 | P2§5.4 | 終了≠内部完結;運用対象・traceなし |
| INT-STOPCORR-004 | interruption | fatigue/distraction/deadline | 中断と再開しうる例 | COR3 | OP2 | P1§8 | 内部停止と中断を独立区分する規則なし |
| INT-STOPCORR-005 | biological cessation | food/network stabilization | 餌到達に伴う探索停止 | COR3 | OP2 | P2§5.4 | 停止窓・安定基準・LE独立検出なし |
| INT-STOPCORR-006 | externally supplied | E/response/task | 外部応答とタスク制御 | COR3 | OP2 | P2§4–5 | 外部原因の判定を観測stopだけで行えない |
| INT-STOPCORR-007 | LE stopping | attractor/function | 安定停止と記述 | COR2 | OP1 | P2§5.3,5.5 | 停止観測→LE存在→停止説明の戻りを独立化する基準なし |
| INT-STOPCORR-008 | consensus stop | socialblock | 判断の共同受容 | COR3 | OP2 | P2§9 | 社会的採用と個体の推論終了が異なる |
| INT-STOPCORR-009 | revisable stop | LR/network/μ | 後に改訂しうる判断 | COR3 | OP2 | P2§5.8,10–12 | potentialrevisabilityと実際改訂eventを区別するruleなし |

## 15. LE observability

一般LE機構はCOR2/OP1。profile内のfood/network例はCOR3/OP2まで具体化するが、これはLEの存在・不存在を停止現象とは独立に測れることを意味しない。stopの有無だけをpositive/negative LE labelに使うと、SERIOUS002のburdenが残る。

| ID | object / aspect | meaning / candidate | source | COR | OP | unresolved operational burden |
|---|---|---|---|---|---|---|
| INT-LECORR-001 | attractor | 安定停止状態 | P2§5.3 | COR2 | OP1 | 力学/停止汎関数の形式化はfuture。固有mode/収束閾値なし |
| INT-LECORR-002 | LR convergence | traceの再帰運動→LE | P2§5.5 | COR2 | OP1 | recursionとconvergenceの独立観測規則なし |
| INT-LECORR-003 | external dependence | Hに依存して個体内に成立 | P2§5.3 | COR2 | OP1 | 外部依存と内部実装を別々に検出するruleなし |
| INT-LECORR-004 | E action | 推論を停止/中断させる作用 | P2§5.7 | COR2 | OP1 | operatorの定義だけでLE検出は不可 |
| INT-LECORR-005 | network synchronization | 他個体LEとの相互維持 | P2§5.8 | COR2 | OP1 | node/同期値が先にLE判定を要する |
| INT-LECORR-006 | concrete profile | 餌到達/探索安定・EOSとの差異 | P2§5.4 | COR3 | OP2 | 物理/AIevent候補はあるがLE-positive/negative labelの独立根拠なし |

## 16. μθ observability

「閾値を動かす」という意味を、微分量・新規estimator・pre/post taskへ置き換えない。sourceの(A)/(B)と内発/受動区別を保存し、その検出規則が不足していると記録する。

| ID | object / aspect | meaning / candidate | source | COR | OP | unresolved operational burden |
|---|---|---|---|---|---|---|
| INT-MUCORR-001 | direct variable | θを動かす能力という名 | P2§2.7 | COR2 | OP1 | rawrecordに直接対応する数値channelなし |
| INT-MUCORR-002 | derivative | 移動/二階の運動というprose | P2§2.7,12 | COR1 | OP1 | dθ/dtという新しい定義を与えない |
| INT-MUCORR-003 | threshold-shift candidate | 同環境の応答/沈黙扱い変更 | P2§4.3,11 | COR3 | OP2 | estimator・事前事後protocolは未指定 |
| INT-MUCORR-004 | revisability proxy | 再配置/判断変更 | P2§10,12 | COR3 | OP2 | 同じ性質をμ/効果の両側へ置くrisk |
| INT-MUCORR-005 | error correction proxy | 誤りうる余地/error tolerance | P2JA§10.6,D | COR2 | OP1 | errorの独立真偽criterionなし、訂正testは未設計 |
| INT-MUCORR-006 | endogenous/passive profile | 内発短期/環境受動/外部設定 | P2§5.4,B.4 | COR3 | OP2 | prompt/環境変化と内発再配置の分類基準なし |

## 17. Φext / Φnet observability

ΦextとΦnetを別々に測って一致を確認したartifactは未所在。二面性という定義/説明はCOR2に留まる。社会的recordや受容という候補の存在だけではnetwork field値を与えない。

| ID | object / aspect | meaning / candidate | source | COR | OP | unresolved operational burden |
|---|---|---|---|---|---|---|
| INT-PHICORR-001 | node | 個体内LE | P2§5.8 | COR2 | OP1 | 実際の個体node候補はあってもLE-bearing nodeの独立同定なし |
| INT-PHICORR-002 | edge | 相互干渉/維持/Hij | P2§5.8 | COR2 | OP1 | 重み・方向・期間のgraph extractionなし |
| INT-PHICORR-003 | aggregation | networkとして形成 | P2§5.8 | COR2 | OP1 | 個体→network→field集約ruleなし |
| INT-PHICORR-004 | shared reference | 外部共通参照基盤 | P2§5.8,7 | COR2 | OP1 | 参照対象の同一性とfield値の同定なし |
| INT-PHICORR-005 | field value | Φext/Φnet同型 | P2§5.8,D | COR2 | OP1 | 二つの独立測定列なし;two-view definitionはcalibrationでない |
| INT-PHICORR-006 | synchronization/consensus | 社会的共同受容 | P2§9 | COR3 | OP2 | 受容event候補→同期量/LE同一性は未設定 |

## 18. Phase-variable correspondence

全6行: data/fit/calibration/execution=未所在。stable bandの数値境界、臨界Δv、各軸の単位/尺度/閾値は未固定。数式として速度差が書かれることと二速度のempirical extractionが完成することは別。figure8の相図は測定phase spaceではない。

| ID | object / aspect | meaning / candidate | source | COR | OP | unresolved operational burden |
|---|---|---|---|---|---|---|
| INT-PHASECORR-001 | vinf | 単位時間の推論/判断/仮説更新step数 | P2JA§11.2 | COR3 | OP2 | step segmentation・具体clockなし |
| INT-PHASECORR-002 | vLR | 痕跡再参照とpattern取込rate | P2§11.2 | COR3 | OP2 | 参照eventと取込criterion・単位なし |
| INT-PHASECORR-003 | Δvintel | 生成と参照の速度差 | P2§11.2,11.4 | COR3 | OP2 | difference式≠rate抽出。common scale/critical値なし |
| INT-PHASECORR-004 | rres | 区別/因果分解の細かさ | P2§11.2 | COR3 | OP2 | 粒度estimator・unitなし |
| INT-PHASECORR-005 | η | 停止固定度/判断改訂抵抗 | P2§11.2 | COR3 | OP2 | thresholdもrangeも較正なし |
| INT-PHASECORR-006 | Σ | LE発達/活性 | P2JA§1.8,13.4,A | COR1 | OP1 | 量化は明示的future;相図領域集合として扱わない |

## 19. Branching correspondence

sourceはgraphのnode/edge/branch/depthに数学的記述を置く。しかし認知命題/発話/理由からgraphを生成する選別規則は未所在。所与graph上の組合せ、推論更新、心理的発散、停止不在の四層を別々に保持する。graph自体の数学的正しさは判定しない。

| ID | object / aspect | meaning / candidate | source | COR | OP | unresolved operational burden |
|---|---|---|---|---|---|---|
| INT-BRANCHCORR-001 | \|V\| | 命題node数 | P1JA§7 | COR3 | OP2 | graphは形式対象、actualpropositionの同定ruleなし |
| INT-BRANCHCORR-002 | \|E\| | 接続辺数 | P1§7 | COR3 | OP2 | 正当な関連/推論edgeの抽出なし |
| INT-BRANCHCORR-003 | b | branching factor | P1JA§7 | COR3 | OP2 | 平均/一定/局所分岐の観測定義なし |
| INT-BRANCHCORR-004 | d | path depth | P1JA§7 | COR3 | OP2 | 起点・stepの切出しなし |
| INT-BRANCHCORR-005 | I(s) | 局所未解決差分 | P1§7 | COR2 | OP1 | 枝数から情報密度へのmetricなし |
| INT-BRANCHCORR-006 | div J | 流れ/分岐発散 | P1§7 | COR2 | OP1 | graph countからcontinuum divergenceへの写像なし |
| INT-BRANCHCORR-007 | correctness | 正しさの蓄積 | P1§7 | COR1 | OP1 | 真/妥当性の独立scoring未設定 |
| INT-BRANCHCORR-008 | actual inference branches | 次の推論候補が増える | P1§7; P2§4 | COR2 | OP1 | cognitivepropositions→V/E map未所在。figurecurveはsimulationでない |

## 20. Gettier correspondence

外部哲学例の存在は、Intelligence-specific C/LE値やcase分類の独立性を与えない。sourceはC≠truthをguardとして述べる一方、Gettierを確認材料と呼ぶ。既にそのcategoryで解釈したcaseから同じcategoryを検証するoperational backedgeに注意し、Phase03の判定を上書きしない。

| ID | object / aspect | meaning / candidate | source | COR | OP | unresolved operational burden |
|---|---|---|---|---|---|---|
| INT-GETTIERCORR-001 | philosophical case | justifiedtruebeliefの反例 | P1§6; P2§10 | COR2 | OP1 | 外部論点の引用/再記述、behavioralcasecodingではない |
| INT-GETTIERCORR-002 | stopping structure | 安定して採用されるbelief | P1§6; P2§10 | COR2 | OP1 | 採用とstoppingを別criterionで分類していない |
| INT-GETTIERCORR-003 | dynamic guarantee | 真理に至る経路の非偶然性 | P1§6 | COR1 | OP1 | path評価rule未指定 |
| INT-GETTIERCORR-004 | C | 運用安定性≠truth | P2§10 | COR2 | OP1 | caseからCを推定する方法なし |
| INT-GETTIERCORR-005 | truth / justification | Gettierのsource条件 | P1§6; P2§10 | COR2 | OP1 | J(x)scoreとの結合なし |
| INT-GETTIERCORR-006 | LE | 改訂可能停止/知性確認 | P2§10 | COR2 | OP1 | GettierexampleからLEを独立検出不可 |

## 21. General-intelligence correspondence

P1は3axiomsのlower-boundと不完全定義のscopeを併記する。P2JA§12は測定可能能力量として知性を定義しないと明記する。したがって、本監査はgeneric intelligence scoreを作らない。R1–R6/最終条項Iとsapiens追加μを区別し、N1のΦnet一般化や末尾「七つ」のscope差をMAPCONFLICT014へ残す。

| ID | object / aspect | meaning / candidate | source | COR | OP | unresolved operational burden |
|---|---|---|---|---|---|---|
| INT-GENCORR-001 | intelligence-like | 3axioms: S/order/globalbias | P1§3–5 | COR2 | OP1 | 必要性sourceclaim;carrier例あり、独立十分criterionなし |
| INT-GENCORR-002 | general intelligence | LF/LR/LE+外部停止/誤り許容/改訂 | P2§12 | COR2 | OP1 | model-localdefinition、実測scoreを明示的に定義しない |
| INT-GENCORR-003 | sapiens intelligence | general+内発μ | P2§5.4,12 | COR2 | OP1 | species/profile命名と内発能力判定が重なる |
| INT-GENCORR-004 | biological intelligence | Physarum profile | P1§5; P2§5.4 | COR3 | OP2 | flow/path例≠全生物の必要十分分類 |
| INT-GENCORR-005 | artificial intelligence | Transformer profile | P1§5; P2§5.4 | COR3 | OP2 | hiddenstates/EOS候補≠generalAIcriterion |
| INT-GENCORR-006 | social intelligence | network/log/sharedstop | P2§9,12 | COR2 | OP1 | 個体と共同体のboundary・aggregate評価なし |

## 22. Homology / cross-domain correspondence

Phase00のINT-HOMO-001–021を一対一対応。共通units/state space/time/invariantの検証、mapping estimator、calibration、executionは全21行で未所在。外部sourceの変数名とformal mapを区別する。P1§5には異なるsubstrate/scaleが明記されるが、共有尺度を定義するものではない。

| XCORR | upstream homology | source→target / locator | preserved role (source claim) | X | explicit variable relation / kind | unresolved bridge |
|---|---|---|---|---|---|---|
| INT-XCORR-001 | INT-HOMO-001 | P1 §4 Tero Q,D,reinforcement,BC → J,I,projection,Φ | flow/log/bias; I0/I1 | X3 | Q→J、D→I、reinforcement→projection、BC→Φは表に明示 | 管網量からInt値への校正/単位/時刻対応なし |
| INT-XCORR-002 | INT-HOMO-002 | P1 §5 Physarum ↔ Transformer | S/order/Φ三公理; I1/I2 | X3 | 管網/hidden states→S、時間/layer→order、境界/weights→Φ | 3carrier対応は明示、共通state/units/estimatorなし |
| INT-XCORR-003 | INT-HOMO-003 | P1 §9 VED4DH ↔ Int localhorizon | unreachability/divergence/finiteabsorption; I0/I2 | X2 | nonreachability/horizonの役割 | Cmaxと認知endpointのmapなし |
| INT-XCORR-004 | INT-HOMO-004 | P1 §9 physical ↔ Bio ↔ Con ↔ Int | fourlayerroles; I0/I2/I4/I3 | X2 | physical/Bio/Con/Int四層の役割表 | 同じcarrier/time/invariant未指定 |
| INT-XCORR-005 | INT-HOMO-005 | P1 J §8 paperclip ↔ individual nonclosure | nointernalstop; I1/I2 | X1 | paperclipとnonstopの構造例 | thoughtcaseでstate/observableの対応なし |
| INT-XCORR-006 | INT-HOMO-006 | P2 §3,D nonfixedF ↔ Cmax ↔ DH | nonclosure; I0/I2 | X2 | noFP/Cmax/DHの同一nonclosure役割を主張 | isomorphismという語や記号はtypedmapでない |
| INT-XCORR-007 | INT-HOMO-007 | P2 §4 regress ↔ branching | sameinferenceextension; I0/I2 | X2 | regressとbranchingの推論延長役割 | graph/regressstepの対応なし |
| INT-XCORR-008 | INT-HOMO-008 | P2 §1,E physicalparticle ↔ life ↔ LE | lower motion+H→upperattractor; I0/I2 | X2 | lower motion+H→upper attractor | U/Φのschema、typedtranslationでない |
| INT-XCORR-009 | INT-HOMO-009 | P2 J B.1 CT ↔ physical/Bio/Con/Int | closure/attractor/horizon/branching; I0/I1/I2/I4 | X2 | CT含む非閉包/attractor/境界/branching表 | 同じ役割列だけ、CT→Int値mapなし |
| INT-XCORR-010 | INT-HOMO-010 | P2 J B.2 / fig5 threeemergencecases | particle/life/stopping; I0/I2 | X2 | particle/life/stopの提案的比較 | formalrole guard。共通機構/観測量なし |
| INT-XCORR-011 | INT-HOMO-011 | P2 §5,B.3 Conprojection ↔ IntE-siteprojection ↔ psychprojection | projection role; I1/I2/I4 | X2 | projectionの影響力/設置役割 | commonoperatorなし;心理側は比較に限定 |
| INT-XCORR-012 | INT-HOMO-012 | P2 J §2,B.4 DNAθ ↔ Intθ ↔ sapiensμ | constraintmobility; I0/I2 | X3 | DNA/反応傾向θ→Intθ/μの時間scale表 | source-target parameter対応は名指し、units/time換算なし |
| INT-XCORR-013 | INT-HOMO-013 | P2 §2,B.5 BioF ↔ inferenceF | localstateevolution role; I0/I1 | X2 | BioFとIntFの局所発展役割 | 非同一型guard、sharedvectorfieldなし |
| INT-XCORR-014 | INT-HOMO-014 | P2 §5,B.6 Physarum/Transformer/sapiens | LF/LR/LEstorage/μprofiles; I1/I2 | X3 | LF/LR/LE/μとflow/trails/weights/context/EOSのprofile | 表対応先明示、role実在検出や同値判定なし |
| INT-XCORR-015 | INT-HOMO-015 | P2 §6–9,B.6 animism/God/religion/socialBC | LEinstallation/compression/maintenance/sync; I2/I3 | X2 | installation/compression/maintenance/revision/sync | 歴史形態の役割列、社会変数mapなし |
| INT-XCORR-016 | INT-HOMO-016 | P2 §9 Git ↔ socialBC | branch/merge/rollback vsconsensus; I1/I3 | X2 | Git/socialのbranch/merge/rollback role/cost比較 | literal protocol translationでない |
| INT-XCORR-017 | INT-HOMO-017 | P2 §5,D Φext ↔ Φnet | same stopping relation external/internalview; I0/I3 | X2 | ΦextとΦnetを停止関係の二面とする | 独立field/node/edge測定なし。identity記号だけでX3としない |
| INT-XCORR-018 | INT-HOMO-018 | P2 J §10,D error tolerance ↔ μθ | revisability/endogenousmovement; I0/I2 | X2 | error toleranceとμのrevisability | 同じ定義役割で独立error候補/typed equivalenceなし |
| INT-XCORR-019 | INT-HOMO-019 | P2 §11 ConΔv ↔ IntΔvintel | speedgap/logtracking; I0/I2/I4 | X3 | ConΔvとΔvintel=生成/参照の差という名指し対応 | 同じunits/clock/観測scaleなし |
| INT-XCORR-020 | INT-HOMO-020 | P2 B/E/fig9 physics/Bio/Con/Int/social | nonclosure→attractor→sustaineddynamics; I0–I4 | X2 | 非閉包→attractor→持続運動の表/図 | crossdomain invariantを測定していない |
| INT-XCORR-021 | INT-HOMO-021 | P2 J E VEDemergence ↔ weak/strong/holistic/functional emergence | dynamicrelationalposition; I0/I2 | X1 | weak/strong/holistic/functionalemergenceの概念比較 | formalstate/variable写像なし |

## 23. Cross-branch bridge audit

Phase02 INT-XFER-001–042を全件照合。分類のformal correspondenceは、変数名/式再利用の明示を意味し、X4 typed translationを意味しない。vocabulary onlyにはdocumentary navigation/negative inheritance guardを含む。candidate typed translation / implemented bridge / validation transferは、成立した関係としては0。強いvalidation/derivation wordingの存在はPhase04のburdenを保持し、ここでvalidated bridgeと認めない。

| XBRIDGE | Phase02 transfer | source locator / transfer | class | X | operational bridge status |
|---|---|---|---|---|---|
| INT-XBRIDGE-001 | INT-XFER-001 | P2 J §0.2 theory-tree/representation row, §0.6–0.7; B.1 → CT concept/terrain/closure | role mapping | X2 | CT主題とclosure/attractor表。typedmapなし |
| INT-XBRIDGE-002 | INT-XFER-002 | P2 J B.1 → CT概念準安定/attractor/境界/分岐 | role mapping | X2 | CT用語の役割対応。field値は未対応 |
| INT-XBRIDGE-003 | INT-XFER-003 | P2 §2 F acts within existing conceptual landscape → CT-like landscape vocabulary | vocabulary only | X0 | landscape語、exactCTpointerを推定しない |
| INT-XBRIDGE-004 | INT-XFER-004 | P2 §5 LR/sedimented terrain/reentry → CT-like vocabulary | vocabulary only | X0 | sedimentation/log語。CT由来は確定しない |
| INT-XBRIDGE-005 | INT-XFER-005 | CT sections/multiscale.tex Intelligence as Landscape Maintenance → Int papers | role mapping | X2 | landscape維持のInt比較;一般Intvalidation guard |
| INT-XBRIDGE-006 | INT-XFER-006 | CT sections/introduction.tex table; conclusion.tex; core_equations.tex → Intelligence | vocabulary only | X0 | CT→Intのnav/handoffで測定橋なし |
| INT-XBRIDGE-007 | INT-XFER-007 | P1 §1,9 → consciousness fast/slow log referencing | role mapping | X2 | fast/slow/logのarchitecture比較 |
| INT-XBRIDGE-008 | INT-XFER-008 | P1 J §9 → Con §4.1 Bio, §7 SSO | role mapping | X2 | Con subsection pointer、version固定なし |
| INT-XBRIDGE-009 | INT-XFER-009 | P1 J §9 → Con §18.10 selfsediments/Intflowback | role mapping | X2 | self/flowbackのsequence比較、typedlinkなし |
| INT-XBRIDGE-010 | INT-XFER-010 | P1 §9 window Δv,μ,τ,TΦ,∇Φ | formal correspondence | X3 | Δv等の変数名比較は明示、clock未対応 |
| INT-XBRIDGE-011 | INT-XFER-011 | P2 §2,5 → Consciousness projection/fourthprimitive | role mapping | X2 | projectionのE-siteへの具現主張、実operatorなし |
| INT-XBRIDGE-012 | INT-XFER-012 | P2 B → projection vspsychologicalprojection | role mapping | X1 | psychprojectionへの作用類似guard |
| INT-XBRIDGE-013 | INT-XFER-013 | P2 B,fig9 → SSO/TCA/temporalnonclosure | role mapping | X2 | SSO/TCA/nonclosureの役割表 |
| INT-XBRIDGE-014 | INT-XFER-014 | P2 §11 Δvintel speedgap → Confastslowcomparison | formal correspondence | X3 | Δv対Δvintel、別clock/別対象 |
| INT-XBRIDGE-015 | INT-XFER-015 | Con sections/formal_mapping.tex → Intelligence projecteduses/§9.4 | vocabulary only | X0 | Conmethodologicalwindowとのguard、validation移送なし |
| INT-XBRIDGE-016 | INT-XFER-016 | Con sections/discussion.tex,conclusion.tex,correspondence_map.tex → Intelligence | vocabulary only | X0 | Con→Int future/doc handoff |
| INT-XBRIDGE-017 | INT-XFER-017 | P1 §4 → Tero2007Physarum solver | formal correspondence | X3 | Q/D/BC→J/I/Φ表。独立実証的収束/確認というvalidation-transfer wordingはあるが、Int mappingの独立検証を伴わない。Phase04 GAP005を保持 |
| INT-XBRIDGE-018 | INT-XFER-018 | P1 §5 → Nakagaki2000/Kobayashi2006/Vaswani2017 | formal correspondence | X3 | Physarum/Transformer3axiomscarrier対応。外部対象研究のvalidated statusをInt対応へ移すことはできない。convergence wordingとmapping maturityを分離 |
| INT-XBRIDGE-019 | INT-XFER-019 | P1 J §2 → Gibson1986/ecologicalperception | role mapping | X1 | Gibson背景類似、JAonly |
| INT-XBRIDGE-020 | INT-XFER-020 | P1 §8 → fatigue/reward/attention/energy/homeostasis | vocabulary only | X0 | fatigue等の一般例、Bio固有bridgeでない |
| INT-XBRIDGE-021 | INT-XFER-021 | P1 J §9 → life必要基盤/Conbuffer | role mapping | X2 | life prerequisite主張、測定可能subset criterionなし |
| INT-XBRIDGE-022 | INT-XFER-022 | P1 §9 → Bioquasiclosure/metabolic/reproductivecycles | role mapping | X2 | Bio代謝/再生cycle比較 |
| INT-XBRIDGE-023 | INT-XFER-023 | P2 §1,E → Bio Ωlife/Ωintel第二attractor | role mapping | X2 | Ωlife/ΩintelとInt第二attractor。実装future |
| INT-XBRIDGE-024 | INT-XFER-024 | P2 §2,B → Bio F(x;θ), DNA-likeθ | role mapping | X2 | BioF比較と非同一guard |
| INT-XBRIDGE-025 | INT-XFER-025 | P2 §2,B → evolutionlongtime/sapiensshorttimeθmobility | formal correspondence | X3 | DNAθ/Intθ/μ/長短期の対応表、共通unitなし |
| INT-XBRIDGE-026 | INT-XFER-026 | P2 §5 → Physarum externaltrail/networkstopping | formal correspondence | X3 | Physarumtrail→LR/foodstop→LEの候補表 |
| INT-XBRIDGE-027 | INT-XFER-027 | P2 §9,E → Bio memory/language/interactionfuture | vocabulary only | X0 | Bio-memory/language/sharefuture、bridge未作成 |
| INT-XBRIDGE-028 | INT-XFER-028 | bio-ifgt sections/intelligence_second_attractor.tex,relation_to_note.tex,discussion.tex | role mapping | X2 | BioforwardproposalからIntへのhandoff、validationでない |
| INT-XBRIDGE-029 | INT-XFER-029 | P1 §1 | vocabulary only | X0 | VED1–4 navigation/語彙 |
| INT-XBRIDGE-030 | INT-XFER-030 | P1 §3 | vocabulary only | X0 | P1axioms独立guard、upstream妥当性を要求しない |
| INT-XBRIDGE-031 | INT-XFER-031 | P1 §4 | role mapping | X2 | IFGT I/J/Φ projecteduse、直接identity否定 |
| INT-XBRIDGE-032 | INT-XFER-032 | P1 §9 | role mapping | X2 | DH同境界role、認知境界の測定なし |
| INT-XBRIDGE-033 | INT-XFER-033 | P1 §9 | role mapping | X1 | renormalization/finiteabsorption analogy |
| INT-XBRIDGE-034 | INT-XFER-034 | P2 J §0,13 | role mapping | X2 | difference→layers派生language。source reuse≠typedderivation |
| INT-XBRIDGE-035 | INT-XFER-035 | P2 J §1 | formal correspondence | X3 | closurePDEの式再用、signature/測定写像不明 |
| INT-XBRIDGE-036 | INT-XFER-036 | P2 §1 | formal correspondence | X3 | I=f(1-C)/FI=α∇C再用、calibrationなし |
| INT-XBRIDGE-037 | INT-XFER-037 | P2 J §2 | formal correspondence | X3 | Cij式再用。node/rho/HのInt推定なし |
| INT-XBRIDGE-038 | INT-XFER-038 | P2 §3,D | role mapping | X2 | noFP/Cmax/horizonclaimedisomorphism;typedmap未所在 |
| INT-XBRIDGE-039 | INT-XFER-039 | P2 J A | vocabulary only | X0 | Master predecessor provenanceOPEN;表再録はbridgeでない |
| INT-XBRIDGE-040 | INT-XFER-040 | P2 J E | role mapping | X2 | E(A)極小とLE比較、同エネルギー/尺度なし |
| INT-XBRIDGE-041 | INT-XFER-041 | P2 §1,E | role mapping | X2 | U=Φ(L,H)同grammar、commontypedmapなし |
| INT-XBRIDGE-042 | INT-XFER-042 | root README/docs/navigation/claim_status.md | vocabulary only | X0 | rootnavigation/claimstatus、independentvalidationでない |

## 24. Falsification routes

Phase04 INT-FALS-001–016を継承。comparator欄はsourceが既に対比している対象/方向の所在であり、新規対照群・controlsの設計ではない。全行でoperational map、confound/control指定、protocol、execution=未所在。sourceの条件付き方向を、無条件の結果保証にも実行済反証手順にも変換しない。

| FALS05 | upstream | claim / source | failure direction | observable candidate | source comparator / missing specification | maturity | operational / control / executed |
|---|---|---|---|---|---|---|---|
| INT-FALS05-001 | INT-FALS-001 | Physarum path/flow correspondence; P1§4–5 | 記述されたflow/path挙動が対応するglobal-bias説明に合わない | OBS001–003 | sourceのpath/globalbias対応方向; 外部modelの挙動対象、Int写像の選別法未定 | measurable candidate | 未所在 / 未指定 / NO |
| INT-FALS05-002 | INT-FALS-002 | Transformer ordered layer profile; P1§5 | 記述したlayer/attentionの順序関係と対象architectureが合わない | OBS006–008 | sourceのordered-layer profile; 特定モデル/run未指定 | measurable candidate | 未所在 / 未指定 / NO |
| INT-FALS05-003 | INT-FALS-003 | global Φ lower bound; P1§3–5 | global役割を持たないとされた系が定義対象の持続motionを示す | なし(global-roleの独立criterion未所在) | globalbias欠如/持続motionというsource対比; global役割と対象motionの独立判定未定 | conceptual only | 未所在 / 未指定 / NO |
| INT-FALS05-004 | INT-FALS-004 | correctness→branching; P1§7 | 正しさ蓄積が推論枝増加に対応しない | OBS019 | 正しさ蓄積とbranching方向; correctness/graph extraction未定 | conceptual only | 未所在 / 未指定 / NO |
| INT-FALS05-005 | INT-FALS-005 | capability increase→nonstop; P1§7–8 | 能力/速度増加がsourceでいう停止不在を伴わない | OBS012/014 | 能力増加とgenuine-stop有無; genuine-stop criterion未定 | conceptual only | 未所在 / 未指定 / NO |
| INT-FALS05-006 | INT-FALS-006 | fatigue→resumption; P1§8 | 中断後に再開しうるというsource例が対応しない | OBS013 | 中断と再開の例; 例であって全疲労の再開予測ではない | measurable candidate | 未所在 / 未指定 / NO |
| INT-FALS05-007 | INT-FALS-007 | external log/response→revisability; P1§8–9 | 外化が改訂可能停止を支えない | OBS011/020 | 外部log/応答とrevisability; 外化/持続条件が未限定 | conceptual only | 未所在 / 未指定 / NO |
| INT-FALS05-008 | INT-FALS-008 | response/silent threshold; P2§2,4 | 時間/解像度に応じたresponse区分がsource方向に移動しない | OBS011/018 | 同環境のresponsive/silent区分; response対象は名付け済、測定規則なし | measurable candidate | 未所在 / 未指定 / NO |
| INT-FALS05-009 | INT-FALS-009 | LR/H→LE; P2§5 | recursive logsとHの下で想定LEが生じない | OBS005/009/012 | LR/HとLE発生; LE独立検出が未定 | conceptual only | 未所在 / 未指定 / NO |
| INT-FALS05-010 | INT-FALS-010 | μ/error tolerance; P2§10–12 | threshold可変性と改訂/error toleranceが結びつかない | OBS018/025 | μ可動性とerror/revision; 独立endpoint未定 | conceptual only | 未所在 / 未指定 / NO |
| INT-FALS05-011 | INT-FALS-011 | centralization→ambiguity; P2§7 | 中心化により停止曖昧性が減らない | なし(ambiguity語のみ) | 中心化とambiguity; ambiguity/cost尺度なし | conceptual only | 未所在 / 未指定 / NO |
| INT-FALS05-012 | INT-FALS-012 | religion/science operation comparison; P2§8–9 | 維持/改訂の割当が対象の運用に対応しない | OBS023/020 | 維持/改訂というrole対比; case-selection criteriaなし | conceptual only | 未所在 / 未指定 / NO |
| INT-FALS05-013 | INT-FALS-013 | Git/social cost contrast; P2§9 | 分岐/merge/rollback costの対比方向が成立しない | OBS022 | Git/social costcontrast; 単位・対象条件なし | conceptual only | 未所在 / 未指定 / NO |
| INT-FALS05-014 | INT-FALS-014 | speed/log gap→collapse; P2§11 | 生成速度と参照速度の差が層崩壊方向に対応しない | OBS014/015 | 生成/参照rateとcollapse; rate候補のみ; critical値/層検出なし | measurable candidate | 未所在 / 未指定 / NO |
| INT-FALS05-015 | INT-FALS-015 | high η→rigidity; P2§11 | stopping hardness増加が想定硬直に対応しない | OBS017 | ηとrigidity; hardnessとrigidity独立criterionなし | conceptual only | 未所在 / 未指定 / NO |
| INT-FALS05-016 | INT-FALS-016 | human/AI same-phase extension; P2§11 | 同条件とされたhuman/AIで同failure方向が成立しない | OBS014/015/017 | human/AI samephase主張; common operational scaleなし | conceptual only | 未所在 / 未指定 / NO |

集計: conceptual only11 / measurable candidate5 / operationalized0 / executed0。absence of operationalizationをglobal unfalsifiabilityへ読み替えない。また、候補の存在をexecutable falsifiabilityと認証しない。

## 25. Prediction operationalization

Phase04の20 entriesを一対一照合。P0は例・formal/editorial/philosophical future等の非実証予測を含む。以下の全行でthreshold / protocol / dataset / exclusion criterion / execution=未所在（非予測agendaにはnot applicable）。期待方向はsourceにある範囲のみ。P0:12/P1:6/P2:2/P3–P6:0を維持し、測定規則を補作してP3へ進めない。

| PRED05 | Phase04 / draft | source | variables | observable / endpoint candidate | direction / kind | P | operationalization judgment |
|---|---|---|---|---|---|---|---|
| INT-PRED05-001 | INT-PRED04-001 / INT-PRED-DRAFT-001 | P1 §4–5 | Q/D/path | OBS001–004 | external example; Int expected directionは別 | P0 | 外部実例。Intの新規予測でない; behavior/source citationあり、mappingは未試験 |
| INT-PRED05-002 | INT-PRED04-002 / INT-PRED-DRAFT-002 | P1 §5 | hidden/layer/Φtr | OBS006–008 | architecture comparison | P0 | architecture比較例。hidden/layer記号はあるがInt固有testなし |
| INT-PRED05-003 | INT-PRED04-003 / INT-PRED-DRAFT-003 | P1 §7 | I/J/V/E/b/d | OBS019 | correctness↑とbranch↑のdirection | P1 | I/J/graph増大の方向、correctness/edgeの独立observable extractionなし |
| INT-PRED05-004 | INT-PRED04-004 / INT-PRED-DRAFT-004 | P1 §7–8 | speed/capability/stop | OBS014/012 | 能力増加だけでselfstopしないdirection | P1 | 速度・能力増加でselfstopしない方向、genuine-stop endpoint未定 |
| INT-PRED05-005 | INT-PRED04-005 / INT-PRED-DRAFT-005 | P1 J §8 | fatigue/restart | OBS013 | 再開しうる例、実測caseなし | P0 | 疲労後再開のsource例、観察report/datasetはない |
| INT-PRED05-006 | INT-PRED04-006 / INT-PRED-DRAFT-006 | P1 §9–10 | E/externalstop | なし(agenda) | design questionのみ | P0 | future design agendaで数値予測ではない |
| INT-PRED05-007 | INT-PRED04-007 / INT-PRED-DRAFT-007 | P1 §9–10 | Bio/Con/Int transition | なし | future bridge | P0 | cross-layer transitionのfuture agenda、変数間map未定 |
| INT-PRED05-008 | INT-PRED04-008 / INT-PRED-DRAFT-008 | P1 §10 | other organisms | なし(対象未指定) | futurecomparison | P0 | 他生物へのfuture比較、指定taskなし |
| INT-PRED05-009 | INT-PRED04-009 / INT-PRED-DRAFT-009 | P2 §2,4 | H/θ/vinf/rres/η | OBS011/018 | response regimeが設定に依存 | P2 | 同じ環境のresponse/nonresponseと速度・resolution差を比較するsource方向。実行protocolではない |
| INT-PRED05-010 | INT-PRED04-010 / INT-PRED-DRAFT-010 | P2 §5 | LF/LR/LE/μ | OBS003/005/009/010 | profile comparison | P0 | 三層profile比較例。独立LE/μ分類未提示 |
| INT-PRED05-011 | INT-PRED04-011 / INT-PRED-DRAFT-011 | P2 §5,13,E | stoppingfunctional | なし | future formalization | P0 | stopping-functional formalization予定。scientific predictionではなくformal future task |
| INT-PRED05-012 | INT-PRED04-012 / INT-PRED-DRAFT-012 | P2 §6–7 | centralization/cost/ambiguity | なし(語義のみ) | 中心化→ambiguity低下 | P1 | 低cost/中心化→曖昧性低下の社会方向。cost/ambiguity尺度なし |
| INT-PRED05-013 | INT-PRED04-013 / INT-PRED-DRAFT-013 | P2 §8–9 | maintenance/revision | OBS023/020 | 運用形態の役割方向 | P1 | 維持・改訂・同期の比較方向。史料選択・測定なし |
| INT-PRED05-014 | INT-PRED04-014 / INT-PRED-DRAFT-014 | P2 §9 | branch/merge/rollback cost | OBS022 | Git/socialのcost方向 | P1 | branch/merge/rollbackの比較方向。cost定義/データなし |
| INT-PRED05-015 | INT-PRED04-015 / INT-PRED-DRAFT-015 | P2 §11 | vinf/vLR/rres/η/Δv | OBS014–017 | gap増大→collapse候補 | P2 | vinf/vLR gap増大と崩壊の比較候補。rate名はあるがstep extraction/critical値なし |
| INT-PRED05-016 | INT-PRED04-016 / INT-PRED-DRAFT-016 | P2 §8,11,13 | Σ/pathology | なし | clinicalfuture・diagnosticguard | P0 | clinical応用はfuture/guard。診断予測ではない |
| INT-PRED05-017 | INT-PRED04-017 / INT-PRED-DRAFT-017 | P2 §10–12 | μ/error tolerance | OBS018/025 | 可動性と改訂のdirection | P1 | μ relocationと改訂/error tolerance方向。独立error endpointなし |
| INT-PRED05-018 | INT-PRED04-018 / INT-PRED-DRAFT-018 | P2 §13 | meaning/subjectivity | なし | philosophicalfuture | P0 | 哲学的意味/主観へのfuture課題。経験予測ではない |
| INT-PRED05-019 | INT-PRED04-019 / INT-PRED-DRAFT-019 | P2 E D; J §13; revision_notes | AI stoppingcost | なし(agenda) | engineeringfuture | P0 | AIcost/practical design問題。プロトコルや結果でない |
| INT-PRED05-020 | INT-PRED04-020 / INT-PRED-DRAFT-020 | P2 J §13,C | P1 edits | NA | editorialfuture | P0 | P1四微修正はeditorial task。scientific prediction母数に含めない |

tested predictions: 0 / validated predictions: 0。実例・章題のtest/convergenceという表現、図curve、外部モデルの式を、このIntelligence対応のtest実行に数えない。

## 26. Empirical route families — OPEN

24群はsource-implied missing correspondenceの分類であり、研究計画・新しいexperiment提案・metric提案ではない。内容が似るuncertaintyをまとめるが旧INT-Uを消去しない。全行status=OPEN、formal/empirical/authorityのどれも解決しない。今後必要な選択の内容を本phaseでは決めない。

| OPEN | source-implied route family | source/ledger basis | unresolved correspondence | status |
|---|---|---|---|---|
| INT-OPEN-001 | 状態・推論stepの同定 | CORR001–003/016; P1§3,5; P2§2 | 観測列からS/X/F/LFへの符号化・切出し未所在 | OPEN |
| INT-OPEN-002 | 正当化とtruthの独立endpoint | CORR004; GETTIERCORR005; P2§3,10 | J、correctness、truthの観測基準が別途未定 | OPEN |
| INT-OPEN-003 | C/Cij/Hの観測対応 | CORR006–007/020; P2§1–4 | 安定性・双方向応答から値を同定するruleなし | OPEN |
| INT-OPEN-004 | I/fluxと認知分岐 | CORR005/033–034/038; P1§4,7; P2§1 | density、flow、closureflux、心理発散の橋未定 | OPEN |
| INT-OPEN-005 | Φのglobal-bias同定 | CORR008–010; P1§3–5 | boundary/weights/loss等の役割比較からscalar値へのmapなし | OPEN |
| INT-OPEN-006 | 停止の識別 | STOPCORR001–009; P1§8; P2§3,5 | 不動点・終了・中断・外部停止の独立区分なし | OPEN |
| INT-OPEN-007 | LR保存・参照の分離 | CORR017; P2§5,9 | 痕跡所在と再帰的利用の観測を区別するruleなし | OPEN |
| INT-OPEN-008 | LE存在・創発・作用の独立検出 | LECORR001–006; P2§5,E | stop観測だけに依存しないLE/収束判定が未定 | OPEN |
| INT-OPEN-009 | θ/μの境界・内発性 | MUCORR001–006; P2§2,4,5 | 応答境界shiftと内発再配置の独立同定なし | OPEN |
| INT-OPEN-010 | μとerror tolerance | MUCORR004–005; P2§10,12,D | 改訂能力と誤り/許容の別endpointなし | OPEN |
| INT-OPEN-011 | Φext/Φnetの個体・network対応 | PHICORR001–006; P2§5,7,9 | LE node/edge・field値・独立二面測定なし | OPEN |
| INT-OPEN-012 | phase rates/axes/boundaries | PHASECORR001–005; P2§11 | vinf/vLRの尺度共有、rres/η/collapse境界が未定 | OPEN |
| INT-OPEN-013 | Σ発達度・clinical boundary | PHASECORR006; P2§1,8,13,A | Σ量化はfuture。clinical指標を本監査で作らない | OPEN |
| INT-OPEN-014 | 認知内容とgraph組合せ | BRANCHCORR001–008; P1§7 | 命題/理由からV/E/b/dへの抽出なし | OPEN |
| INT-OPEN-015 | Physarum固有mapping | BIOCORR001–005; P1§4–5; P2§5 | 外部文献の生物量とInt変数の独立mapping未実行 | OPEN |
| INT-OPEN-016 | Transformer profile/stop provenance | AICORR001–012; P1§5; P2§5,11 | 対象モデル・trace・self/external stopの分類なし | OPEN |
| INT-OPEN-017 | 社会的record/consensus | SOCCORR005–006/008; P2§9 | node・受容block・制度とLEの対応判定未定 | OPEN |
| INT-OPEN-018 | 歴史形態・維持/改訂 | HISTCORR001–006; P2§6–9 | 史料/corpus/selection/comparatorなし。形態分類≠歴史法則 | OPEN |
| INT-OPEN-019 | 社会cost・正統性・創造帰属 | SOCCORR007/010–012; P2§7,9 | cost単位、正統性/創造の独立criterionなし | OPEN |
| INT-OPEN-020 | Gettier case独立分類 | GETTIERCORR001–006; P1§6; P2§10 | theory再記述から独立したC/LE/case分類なし | OPEN |
| INT-OPEN-021 | 一般・sapiens・collective知性criterion | GENCORR001–006; P1§3,5; P2§5,12 | profile命名と必要十分観測基準が未分離 | OPEN |
| INT-OPEN-022 | phenomenal endpointとscope | PHENCORR001–006; P1§9; P2§7,13 | free inference/責任の機能語≠主観報告。futurehandoff維持 | OPEN |
| INT-OPEN-023 | cross-domain型・尺度・時間対応 | XCORR001–021; XBRIDGE001–042; P2B–E | homologyを越すtyped/implemented/validatedbridge未所在 | OPEN |
| INT-OPEN-024 | prediction/failure routeの実行境界 | PRED05-001–020; FALS05-001–016; P2§11,13 | source候補はあるがprotocol/threshold/comparator/実行結果なし | OPEN |

## 27. Mapping conflicts

14群。ここでのconflictは測定対応の多義性/逆同定riskであり、数学的矛盾の証明でもfinal dispositionでもない。複数carrierを同じmetricへ統合しない。

| MAPCONFLICT | object | multiple mappings | identification conflict | source | OPEN route |
|---|---|---|---|---|---|
| INT-MAPCONFLICT-001 | stopping | S/Ffixedpoint ↔ 終了/中断/E/LE/consensus | 同じ終了から異なる原因・型を識別するruleなし | P1§8; P2§3,5,9 | OPEN006 |
| INT-MAPCONFLICT-002 | Φ | scalarbias/Φbio/Φtr vs emergenceoperator/Φnet | 同記号をfield値に統合不可 | P1§3–5; P2§5,E | OPEN005/011/023 |
| INT-MAPCONFLICT-003 | J | flux/Q対比 vs justificationJ(x) | 測定量・domainが別、glyphを結合しない | P1§4; P2§3 | OPEN002/004 |
| INT-MAPCONFLICT-004 | C | 運用安定/閉包/応答/ultimateunderstanding | truth negativeguardと理解endpointが別 | P2§1,4,10 | OPEN002/003 |
| INT-MAPCONFLICT-005 | μ | 能力/境界shift/内発性/error tolerance | 同じ改訂を予測変数と結果の双方にしうる | P2§2,10–12 | OPEN009/010 |
| INT-MAPCONFLICT-006 | intelligence | P1ongoingmotion vs P2三層 vs sapiensμ | profileからgeneralcriterionを自動生成不可 | P1§3; P2§5,12 | OPEN021 |
| INT-MAPCONFLICT-007 | LE | 餌停止/人間判断attractor vsAIexternalstop | 反転profileだけでpresence/absence判定不可 | P2§5.4–5.7 | OPEN006/008/016 |
| INT-MAPCONFLICT-008 | LR | slime/weights/context/memory/socialrecords | 保存場所と再帰参照過程が異なる | P2§5.2,5.4,9 | OPEN007 |
| INT-MAPCONFLICT-009 | consensus/legitimacy | 共同受容/正統性/Φnet同期 | 同じ受容recordを別構造の存在証拠にしない | P2§5.8,9 | OPEN011/017/019 |
| INT-MAPCONFLICT-010 | stability | C/LEattractor/stableband/institutionmaintenance | 安定という語だけで単一observableにしない | P2§1,5,8,11 | OPEN003/008/012/018 |
| INT-MAPCONFLICT-011 | time/rate | layerindex/biocycle/socialhistory/vinf/vLR | rate差の共通unit・timewindowなし | P1§5,9; P2§11,B | OPEN012/023 |
| INT-MAPCONFLICT-012 | H/ρresp | 実応答/付与された応答性/拘束/density | 自然対象を応答的に扱うことと返答観測が別 | P2§2,4,6,A | OPEN003/009/018 |
| INT-MAPCONFLICT-013 | graph | formalV/E/b/d vs発話・命題の分岐 | 図curveをactualreasoninggraphと同定不可 | P1§7 | OPEN014 |
| INT-MAPCONFLICT-014 | generality/socialscope | N1全知性Φnet vsR4外部停止source | JA§12のsource内scope差が対象選別に影響 | P2JA§12 | OPEN016/021 |

## 28. Operational circularity

Phase03 SERIOUS001–005について、将来同定が説明対象と同じoutcomeへ依存しうるかを限定監査する。実測がないため「実行済の循環測定」を認定するものではない。

| OPCIRC | SERIOUS | source target | possible identification return | independent criterion | COR / OP | route |
|---|---|---|---|---|---|---|
| INT-OPCIRC-001 | INT-SERIOUS-001 | internal cognitive stopping | 停止行動を不動点と認定してから不動点不在で内部停止を説明するrisk | NO | COR2 / OP1 | OPEN001/002/006 |
| INT-OPCIRC-002 | INT-SERIOUS-002 | LE emergence | LEをstopから同定し、LEでstopを説明するrisk | NO | COR2 / OP1 | OPEN007/008 |
| INT-OPCIRC-003 | INT-SERIOUS-003 | Φext / Φnet | 共有参照でnetworkを定義し、networkで共有参照を同定するrisk | NO | COR2 / OP1 | OPEN011/017 |
| INT-OPCIRC-004 | INT-SERIOUS-004 | μθ / error tolerance | 改訂をμ・error tolerance両側のcriterionにするrisk | NO | COR3 / OP2 | OPEN009/010 |
| INT-OPCIRC-005 | INT-SERIOUS-005 | Gettier confirmation | C/LE読みを先に置いたcase再記述をmapping確認へ戻すrisk | NO | COR2 / OP1 | OPEN002/020 |

source-local definitionを使うだけなら運用上の循環の立証にならない。問題となるのは、同じoutcomeによるラベルを独立な説明/確認として再利用する場面である。停止や改訂を定義として保持する可能性と、一般機構の実証に使うburdenを分ける。5件ともPhase03 RETAINは不変。

## 29. Correspondence ceilings

| domain | ceiling | ceiling witness | limit |
|---|---|---|---|
| Formal-to-observable | COR3 | CORR036–037; Q/D/graph candidate | 形式式からInt observationへの実行器なし |
| Cognitive | COR3 | CORR022–026; step rate/粒度/改訂抵抗 | 一般LE/justificationのendpointまで整備された意味ではない |
| Behavioral | COR3 | STOPCORR003–005; task終了/中断再開/餌到達 | source例、protocol0 |
| Biological | COR3 | BIOCORR001–005; externally cited流れ/path/trail | BE3はcitation背景、Int固有calibration0 |
| Social | COR3 | SOCCORR003/005–007;儀礼/判断理由record/受容event | category単独はCOR2以下、historiography dataset0 |
| Phenomenal | COR1 | PHENCORR001–003/005; 機能語に伴うsubjective reading | independentreport0、meaning/subjectivityはfuture |
| AI | COR3 | AICORR001–008; hidden/layer/weights/context/EOS | selectedmodel/benchmark/run0 |
| Cross-domain bridge | X3 | XCORR001/002/012/014/019; variable/carrier table | typed X4/implemented X5/validated X6未所在 |
| Operational | OP2 | OBS014/015; rate候補、profilecarrier候補 | extraction OP3以上未所在 |

Phase04 evidence ceilings FE2/CE2/SE2/BE3/PE1/XE2/PRE2/OE0は変更なし。COR3/X3はsourceが具体的対応先を名指しする成熟度であって、Phase04 evidence level3の独立観察/引用supportへ昇格させる操作ではない。OE0は実行可能なInt-specific operational mapが0であること、OP2はその手前のcandidateがあることを示す。両者は矛盾しない。

## 30. Operational artifact inventory

対象: intelligence-part1/ と intelligence-part2/ のhidden/ignored filesを含む全file。`rg --files --hidden --no-ignore`で拡張子・data/benchmark/protocol/calibration/experiment/simulation/scoringを探索し、current TeX/appendixの同語出現もcontext確認した。理論・simulation codeは実行していない。Makefileは内容を読みbuild用と確認しただけで実行しない。

| artifact class | count in Intelligence scope | path / negative evidence |
|---|---|---|
| dataset CSV/TSV/JSON/JSONL/parquet/HDF/NumPy等 | 0 | no candidate file located |
| notebooks/scientific scripts / simulation outputs | 0 | no .ipynb/.py/.r/.jl 等 located |
| benchmark/results / scoring functions | 0 | sourceのarchitecture例、図、文献だけ |
| protocols / experiment logs | 0 | experiment語は対話/実験という例やfuture、具体protocolなし |
| calibration files / estimators | 0 | metric namesと式だけ、extraction/calibration artifactなし |
| executed operational mappings | 0 | source-local relation/tableを実行写像へ数えない |
| build Makefile | 1 (excluded) | intelligence-part2/Makefile: LuaLaTeX/BibTeX route |
| TeX source | 66 (excluded) | 本文/entry/appendices、測定resultではない |
| bibliography | 2 (excluded) | P1 refs.bib13 entries; P2 refs.bib empty |
| figure/source/presentation | PNG10 / SVG28 / PDF24 (excluded) | PDF24は図・root配布・旧build配布を含む、24 datasetsではない |
| font/build cache | Lua46 / LUC93 / GZ49 (excluded) | .texmf-var/luatex-cache 等。モデルcode/resultsではない |
| build logs | log4 / aux4 / bbl2 / blg2 / out4 / toc4 (excluded) | TeX実行履歴はempirical executionでない |

P1の外部Physarum文献・Vaswani2017・Gettier等は外部対象の背景であり、その元研究にdataが存在しないという主張はしない。ここで0なのはrepository-local Intelligence-specific artifactsである。上流branchのcode/data/closureをこの母数へ加算しない。過去figure formal-role14 familiesとcaption/bodyはE1 schemaのまま。相図/growthcurveをfitted resultへ読み替えない。

## 31. Observable-to-variable matrix

compact matrixのJ列はjustification J(x)、F列は文脈に応じたP1/P2 update/inferenceであり同一signatureを意味しない。NONE=source link未所在、VERBAL=語義だけ、STRUCTURED=役割対応、EXPLICIT CANDIDATE=具体対象を名指し、OPERATIONAL=抽出済。全cellにOPERATIONALはない。これらは新しい写像でなく既出ledgerへの索引。

| source observable | C | F | J(x) | LR | LE | μθ | Φnet | phase variables | general intelligence |
|---|---|---|---|---|---|---|---|---|---|
| 応答/無応答 (OBS011) | EXPLICIT CANDIDATE | STRUCTURED | NONE | NONE | STRUCTURED | EXPLICIT CANDIDATE | STRUCTURED | EXPLICIT CANDIDATE | STRUCTURED |
| 判断終了 (OBS012) | STRUCTURED | STRUCTURED | NONE | STRUCTURED | STRUCTURED | VERBAL | STRUCTURED | STRUCTURED | STRUCTURED |
| 疲労後再開 (OBS013) | NONE | VERBAL | NONE | VERBAL | NONE | NONE | NONE | NONE | VERBAL |
| 推論step頻度 (OBS014) | NONE | STRUCTURED | NONE | NONE | NONE | NONE | NONE | EXPLICIT CANDIDATE | VERBAL |
| trace参照rate (OBS015) | NONE | NONE | NONE | EXPLICIT CANDIDATE | STRUCTURED | NONE | NONE | EXPLICIT CANDIDATE | STRUCTURED |
| 判断改訂抵抗 (OBS017) | STRUCTURED | NONE | NONE | STRUCTURED | STRUCTURED | STRUCTURED | STRUCTURED | EXPLICIT CANDIDATE | STRUCTURED |
| 応答境界shift (OBS018) | STRUCTURED | STRUCTURED | NONE | NONE | STRUCTURED | EXPLICIT CANDIDATE | NONE | EXPLICIT CANDIDATE | STRUCTURED |
| 管流/管網 (OBS001) | VERBAL | EXPLICIT CANDIDATE | NONE | STRUCTURED | NONE | NONE | NONE | NONE | STRUCTURED |
| slime跡 (OBS005) | NONE | NONE | NONE | EXPLICIT CANDIDATE | STRUCTURED | NONE | NONE | NONE | STRUCTURED |
| hidden/token/context (OBS006/009) | NONE | EXPLICIT CANDIDATE | NONE | EXPLICIT CANDIDATE | NONE | NONE | NONE | NONE | STRUCTURED |
| EOS/task終端 (OBS010) | NONE | STRUCTURED | NONE | STRUCTURED | STRUCTURED | VERBAL | NONE | NONE | STRUCTURED |
| graph枝 (OBS019) | NONE | STRUCTURED | NONE | VERBAL | NONE | NONE | NONE | VERBAL | VERBAL |
| 社会record (OBS020) | STRUCTURED | NONE | NONE | EXPLICIT CANDIDATE | STRUCTURED | NONE | STRUCTURED | NONE | STRUCTURED |
| 共同受容 (OBS021) | STRUCTURED | NONE | NONE | STRUCTURED | STRUCTURED | NONE | STRUCTURED | NONE | STRUCTURED |
| 儀礼/祈り (OBS023) | STRUCTURED | NONE | NONE | NONE | STRUCTURED | NONE | STRUCTURED | NONE | VERBAL |

## 32. SERIOUS correspondence burden

central claimの成熟度を評価する。LEの具体profileはCOR3でも、一般LE emergenceの独立endpointはCOR2であり、その違いをtableに保持する。formal/circularity statusとPhase05 burdenは別欄。

| SERIOUS burden | source target | observable candidate | independent endpoint | operationalization | mapping return | COR | OP | Phase05 status | Phase03 | route |
|---|---|---|---|---|---|---|---|---|---|---|
| INT-SER-CORR-001 / INT-SERIOUS-001 | internal cognitive stopping | 判断終了/中断・S/Ffixedpoint | NO | 未所在 | 停止行動を不動点と認定してから不動点不在で内部停止を説明するrisk | COR2 | OP1 | CORRESPONDENCE GAP CRITICAL | RETAIN | OPEN001/002/006 |
| INT-SER-CORR-002 / INT-SERIOUS-002 | LE emergence | stable stop、LRtrace、Physarum foodstop候補 | NO | 未所在 | LEをstopから同定し、LEでstopを説明するrisk | COR2 | OP1 | CORRESPONDENCE GAP CRITICAL | RETAIN | OPEN007/008 |
| INT-SER-CORR-003 / INT-SERIOUS-003 | Φext / Φnet | 共有参照・受容、個体間干渉 | NO | 未所在 | 共有参照でnetworkを定義し、networkで共有参照を同定するrisk | COR2 | OP1 | CORRESPONDENCE GAP CRITICAL | RETAIN | OPEN011/017 |
| INT-SER-CORR-004 / INT-SERIOUS-004 | μθ / error tolerance | response境界の変更、revisability | NO | 未所在 | 改訂をμ・error tolerance両側のcriterionにするrisk | COR3 | OP2 | CORRESPONDENCE GAP STRONG | RETAIN | OPEN009/010 |
| INT-SER-CORR-005 / INT-SERIOUS-005 | Gettier confirmation | Gettier哲学例・採用判断 | NO | 未所在 | C/LE読みを先に置いたcase再記述をmapping確認へ戻すrisk | COR2 | OP1 | CORRESPONDENCE GAP CRITICAL | RETAIN | OPEN002/020 |

001/002/003/005: CORRESPONDENCE GAP CRITICAL、004: CORRESPONDENCE GAP STRONG。これは新しいfinal dispositionでもcircularity resolutionでもない。独立endpointやmapが未所在であることを、claim falseへ変換しない。

## 33. New uncertainty ledger

INT-U-189–218、30件。Phase04までの188件は変更/削除/閉鎖しない。以下は既存evidence-gapのうちPhase05で区別した観測・同定問題の子項目で、独立証拠欠如の件数として合算しない。旧parent IDを付して同じ未解決事項の関連を保存する。新旧合計218。

| uncertainty | parent evidence uncertainty | route | Phase05 identification question | status |
|---|---|---|---|---|
| INT-U-189 | INT-U-159 | OPEN001 | 認知state/stepの切出しがvinf/LF/F間で共通に定まるか | OPEN |
| INT-U-190 | INT-U-170 | OPEN002 | J正当化順位をC安定性・truth・改訂頻度から独立に同定できるか | OPEN |
| INT-U-191 | INT-U-178 | OPEN003 | C値と観測される判断安定性の対応範囲・観測窓 | OPEN |
| INT-U-192 | INT-U-178 | OPEN003 | Hの方向別応答とCijを観測に結ぶ選別・weightの未指定 | OPEN |
| INT-U-193 | INT-U-168 | OPEN004 | density I・flux J/JCと認知branch量が異なるときの対応関係 | OPEN |
| INT-U-194 | INT-U-164 | OPEN005 | boundary/weights/loss/分布の複数carrierからΦを同定する基準 | OPEN |
| INT-U-195 | INT-U-171 | OPEN006 | 停止・中断・再開可能性・内部完結の独立観測区分 | OPEN |
| INT-U-196 | INT-U-165 | OPEN006 | EOS/task終了と自前LE/E不在との関係を判定するcriterion | OPEN |
| INT-U-197 | INT-U-165 | OPEN007 | 保存traceと再帰参照運動を別々に検出するrule | OPEN |
| INT-U-198 | INT-U-179 | OPEN008 | stopを前提としないLE存在・attractor到達の検出criterion | OPEN |
| INT-U-199 | INT-U-179 | OPEN008 | LR/HとLE生成endpointの独立対応 | OPEN |
| INT-U-200 | INT-U-178 | OPEN009 | 応答/沈黙boundaryの移動を無応答/観測時間差から区別するrule | OPEN |
| INT-U-201 | INT-U-165 | OPEN009 | μの内発性を外部設定/受動変化から分ける観測criterion | OPEN |
| INT-U-202 | INT-U-180 | OPEN010 | error toleranceとμを別endpointとして同定する関係 | OPEN |
| INT-U-203 | INT-U-181 | OPEN011 | LE-bearing node/edgeとΦnetの観測構成規則 | OPEN |
| INT-U-204 | INT-U-181 | OPEN011 | ΦextとΦnetの二面を別測定から対応づけられるか | OPEN |
| INT-U-205 | INT-U-185 | OPEN012 | vinf/vLRのstep・参照event・共通clock/scale | OPEN |
| INT-U-206 | INT-U-185 | OPEN012 | rres/ηの語義から独立な粒度/改訂抵抗の抽出 | OPEN |
| INT-U-207 | INT-U-185 | OPEN012 | stableband/fourfoldcollapseの状態境界が実測markerを持つか | OPEN |
| INT-U-208 | INT-U-169 | OPEN013 | Σ量化がclinical名称だけに依存しないendpointを持つか | OPEN |
| INT-U-209 | INT-U-168 | OPEN014 | cognitive propositions/correctnessからgraph vertices/edgesへの対応 | OPEN |
| INT-U-210 | INT-U-162 | OPEN015 | Physarum外部modelの変数対応をInt固有mappingとして識別する基準 | OPEN |
| INT-U-211 | INT-U-165 | OPEN016 | Transformerprofileの適用対象・実行trace・self/externalstop境界 | OPEN |
| INT-U-212 | INT-U-182 | OPEN017 | 社会log/blockの受容対象・node集団・期間の選別 | OPEN |
| INT-U-213 | INT-U-182 | OPEN018 | 歴史categoryを維持/改訂機能から独立に比較する史料criterion | OPEN |
| INT-U-214 | INT-U-184 | OPEN019 | socialcost/正統性/創造帰属の観測因子と構造説明の分離 | OPEN |
| INT-U-215 | INT-U-166 | OPEN020 | GettiercaseのC/LE分類をtheory再記述から独立に判定できるか | OPEN |
| INT-U-216 | INT-U-186 | OPEN021 | 一般/sapiens/social必要条件とprofile観測の適用範囲 | OPEN |
| INT-U-217 | INT-U-175 | OPEN022/023 | functional freedom/Con比較からphenomenal reportへの未所在bridge | OPEN |
| INT-U-218 | INT-U-188 | OPEN024 | 候補failure directionのendpoint・comparator・実行状態の対応 | OPEN |

## 34. Validation

開始時snapshot: `${TEMP_EVIDENCE_ROOT}/int_phase05.yNsicA/baseline.json`。1495 repository files（.git除外、ignored/untrackedを含む）のSHA-256を保存。manifest SHA-256: `ff4d8c997fa0ff6501964f826bd29d9bb547ca75edcca2d565c5c30792d83236`。

| authority | task-start SHA-256 |
|---|---|
| 00_dependency_inheritance_and_authority_record_v0.1_ja.md | ffb891b9039a71a2173574652f72776a307be6618070a74f2fcc64bc0a312d64 |
| 01_equation_symbol_object_inventory_v0.1_ja.md | ecb64a12dd4d5e4defab076c2118cc6a6f9f842ab278f03c975ce9f082891d14 |
| 02_role_definition_homology_audit_v0.1_ja.md | aee8d40a4241869918d6724305a3c94dc667ec2e352ed496614439d775148318 |
| 03_preload_selfreference_circularity_audit_v0.1_ja.md | 1596b90ca99baeeb19cf5e6fb655f5f5a4c925f63b551de33c8b0b4bfac7c05d |
| 04_claim_and_evidence_burden_audit_v0.1_ja.md | 9255a79991bb0073e9384ddc2ea6f4a6e051a9179563736b0cf411cc9a7697ee |

### 34.1. Coverage and ID validation

PASS。primary correspondence43（COR0:2 / COR1:3 / COR2:11 / COR3:27; OP0:2 / OP1:14 / OP2:27）、95 claimsへの索引、observable25、cognitive14 / behavioral9 / biological8 / AI12 / social12 / historical6 / phenomenal6を照合した。

Stopping9 / LE6 / μ6 / Φext-net6 / phase6 / branching8 / Gettier6 / general-intelligence6。21 homologiesはX1:2 / X2:14 / X3:5、42 XFERは全件にbridge statusを付した。20 predictionsはP0:12 / P1:6 / P2:2、16 falsification directionsはconceptual11 / measurable candidate5。SERIOUS5は別々にcorrespondence判定、循環status RETAINを保持した。

全local ledger IDの連続性・一意性、homology/XFER/prediction/falsificationの旧IDとの一対一対応、Markdown table列数、INT-U-189–218の30件とtotal218を検証。OPEN routes24、mapping conflicts14、operational circularity5を確認した。source-localな候補名/役割/未所在事項の記録だけで、新規experiment、metric、estimator、threshold、IC/BC、protocol、dataset、bridgeは作成していない。theorem/proof validityとfinal dispositionsは未判定。

### 34.2. SHA-256 / repository boundary

開始時1495filesに対し、new Phase05 record1件のみ追加、README1件のみhash変更。残る1494filesはbyte-identical、削除0。Intelligence included TeX66files、Phase00–04 authority5files、全source/math/figures/PDF/BibTeXを変更していない。式/inline/labelsはTeX全体のraw byte同一性で包含検証した。外部research、PDF rebuild、simulation、theory/bridge追加、commit/pushなし。

検証用script/logはrepository外の `${TEMP_EVIDENCE_ROOT}/int_phase05.yNsicA/validate.py`、`validation.json`、`git_status_short.txt`。これは文書ID/ファイルhash検査でありtheory simulationではない。`git diff --check`: PASS（exit 0）。`git status --short`: 250行、開始時と同一。既存dirty worktreeとuntracked `notes/intelligence_audit/` を保持したためGit statusだけでは新規record追加を区別できないが、開始時hash全件比較で上記2file境界を確認した。

### 34.3. Ceiling / stop validation

Phase04 support95件の内訳・evidence ceilingsは不変。COR/OP/Xは本phaseの新しい監査taxonomyであり、経験supportの増加ではない。Int-specific maps/datasets/simulations/tested/validated0、SERIOUS5 RETAIN、source-level vicious circularity NO/global unfalsifiability NOは保持。Phase06/07とsource/equation/distribution revisionはNOT STARTED。

## 35. Stop boundary

Phase05で停止する。Phase06/07未開始。source/equation/distribution revision未開始。新規experiment/metric/estimator/threshold/dataset/protocolを作成しない。現行式・記号・figures・BibTeX・PDF・上流/下流sourceを変更しない。web research、simulation、proof validation、final disposition、commit/pushは行わない。OPEN routes24とSERIOUS5 RETAINを後続authorityへ引き渡すが、未解決を仮定で埋めない。

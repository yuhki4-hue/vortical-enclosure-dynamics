# Post-audit implementation 28 — LR / LE' / LE Source Migration Design Packet

## 1. Status / authority / bounded design

```text
Post-audit implementation 28: COMPLETE — DESIGN ONLY
Verdict: LR/LE'/LE SOURCE MIGRATION DESIGN READY WITH HOLDS
Preferred layer policy: mixed, scoped functional shorthand + explicit historical enclosures
Preferred implementation: one coordinated additive prose transaction, after independent authorization
Canonical units: U28-001–033 (031までprose design; 032 protection; 033 HOLD)
Maximum proposed source file scope: 35 TeX files, not an authorization
Planned new display / inline math: 0 / 0
Planned mutation of existing math / headings / definitions / proof / tables / figures: 0
LE': one canonical prose-only scaffold-regime introduction per language, NOT a new type
FIG009 coexistence: SAFE WITH STRONG GUARD, source-only and unreleased
Source implementation / figure / caption / equation / proof authorization: NO
Next gate: separate independent source-migration design / authorization review
```

2026-09-23。Primaryは[impl27](impl27_independent_architecture_contract_review_lr_leprime_le_fig009_v0.1_ja.md)。受理された[impl26](impl26_lr_leprime_le_architecture_specification_fig009_semantic_contract_v0.1_ja.md)のsupport/role/regime契約をsourceへ説明するためのdesignのみを行う。impl27の選定owner Aを越えて、FIG009新版の配置・描画・caption案、E/Φ/plasticityを設計しない。

Supporting authority: [impl25](impl25_post_migration_formal_debt_rebaseline_and_next_owner_selection_v0.1_ja.md)、[impl24](impl24_independent_post_migration_acceptance_audit_f_j_active_historical_split_v0.1_ja.md)、[impl18](impl18_selected_formal_contract_adoption_and_type_scope_acceptance_v0.1_ja.md)、[impl16](impl16_author_clarification_and_formal_specification_contract_v0.1_ja.md) AR003/004/007、[impl14](impl14_independent_consistency_audit_author_decisions_v0.1_ja.md)、[impl13](impl13_author_decision_record_d001_d018_v0.1_ja.md) D009/016/017、[impl11](impl11_proof_theorem_review_v0.1_ja.md)、[impl10](impl10_formal_equation_review_v0.1_ja.md)、[Phase07](07_final_audit_and_frozen_dispositions_v1.0_ja.md)、[README](README_ja.md)。source上に残る過去の「未解決」という文書的記述を、後続author decisionがなかったことにも、現在すべて形式化済みであることにもしない。

保存: Phase07 KEEP23 / REVISE8 / DOWNGRADE21 / SPLIT41 / RETIRE0 / OPEN2 =95 FROZEN。SERIOUS001–005 RETAIN、OPEN24/24、uncertainties236、impl08 PASS/CLOSED、impl24 bounded F/J ACCEPTED/CLOSED不変。FE2/CE2/SE2/BE3 citation-background-only/PE1/XE2/PRE2/OE0、formal/cognitive/behavioral/biological/social/AI COR3・phenomenal COR1・X3・OP2、maps/data/sims/tested/validated=0不変。新たなmaterial contradictionを見つけていないためF/J受入を再openしない。global blocker closure0。

本packetは**既存bytesを置換しない追加型design**を選ぶ。RELABEL/REINTERPRETは隣接する新しいstatus文による意味上の処置で、旧句の削除や同じ式の再定義ではない。旧定義を「現在の唯一の定義」と読ませないbegin/end境界と、肯定的なactive role説明を両方置く。全章を単にhistoricalと宣言する方法は採用しない。

## 2. Current source inventory / locator convention

42 P2 TeX（main/preamble、28 section files、10 appendix files）を対象に、LR/LE、layer、trace/log、attractor/emergence、Transformer/Physarum、own/inside/externalと日本語対応語を検索し、該当paragraph・table・周辺guardを照合した。P1 TeXへの直接LR/LE参照検索も行ったが、本migrationのP1編集対象は0。直接consumerは下表の意味blockで束ねる。繰り返しmentionは同じblockのscopeに含め、図/式内は保護として分離する。本文の記号がないE07/DEもstoppingの間接consumerとして確認した。

### File aliases（すべてrepository-relative）

E/Jは英語/日本語。例えばE05は左列、J05は右列の**別file**を指す。lineはtask-start locatorであり実行offsetではない。§16のliteral anchorとprotected hashで再解決する。

| Alias | EN file | JA file |
|---|---|---|
| M | `intelligence-part2/main.tex` | `intelligence-part2/main_ja.tex` |
| 00 | `intelligence-part2/sections/00_introduction.tex` | `intelligence-part2/sections/00_introduction_ja.tex` |
| 01 | `intelligence-part2/sections/01_preliminaries.tex` | `intelligence-part2/sections/01_preliminaries_ja.tex` |
| 02 | `intelligence-part2/sections/02_inference_operator.tex` | `intelligence-part2/sections/02_inference_operator_ja.tex` |
| 03 | `intelligence-part2/sections/03_nonclosure_theorem.tex` | `intelligence-part2/sections/03_nonclosure_theorem_ja.tex` |
| 04 | `intelligence-part2/sections/04_response_channels.tex` | `intelligence-part2/sections/04_response_channels_ja.tex` |
| 05 | `intelligence-part2/sections/05_emergent_stopping_layer.tex` | `intelligence-part2/sections/05_emergent_stopping_layer_ja.tex` |
| 06 | `intelligence-part2/sections/06_animism.tex` | `intelligence-part2/sections/06_animism_ja.tex` |
| 07 | `intelligence-part2/sections/07_god.tex` | `intelligence-part2/sections/07_god_ja.tex` |
| 08 | `intelligence-part2/sections/08_religion.tex` | `intelligence-part2/sections/08_religion_ja.tex` |
| 09 | `intelligence-part2/sections/09_social_blockchain.tex` | `intelligence-part2/sections/09_social_blockchain_ja.tex` |
| 10 | `intelligence-part2/sections/10_gettier_problem.tex` | `intelligence-part2/sections/10_gettier_problem_ja.tex` |
| 11 | `intelligence-part2/sections/11_instability_region.tex` | `intelligence-part2/sections/11_instability_region_ja.tex` |
| 12 | `intelligence-part2/sections/12_constructive_clauses.tex` | `intelligence-part2/sections/12_constructive_clauses_ja.tex` |
| 13 | `intelligence-part2/sections/13_conclusion.tex` | `intelligence-part2/sections/13_conclusion_ja.tex` |
| A | `intelligence-part2/appendices/appendix_a_master_table.tex` | `intelligence-part2/appendices/appendix_a_master_table_ja.tex` |
| B | `intelligence-part2/appendices/appendix_b_homology.tex` | `intelligence-part2/appendices/appendix_b_homology_ja.tex` |
| C | `intelligence-part2/appendices/appendix_c_part1_mapping.tex` | `intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex` |
| D | `intelligence-part2/appendices/appendix_d_optional_notes.tex` | `intelligence-part2/appendices/appendix_d_optional_notes_ja.tex` |
| E | `intelligence-part2/appendices/appendix_e_emergence_homology.tex` | `intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex` |

Appendix aliasはAE/AJ、BE/BJ等と記す（EE/EJはAppendix E）。mainはME/MJ。M以外のsectionはE00/J00形式。

| Locator / exact wording anchor | Current role / dependency | Status | Migration need / owner |
|---|---|---|---|
| ME18 “The three-layer dynamics”; MJ18 `% ここに概要を移植`; titles5–6 | abstract→§5、titleは既存名称 | mixed / placeholder | MEにactive役割概要、MJ/両title KEEP。U013 |
| E00:11–15 “The central structure”; J00:15–24,50–57 “第三線 — 三層動力学と創発停止” | old LF→LR→LE chain→§5 | mixed | chainを旧機構と限定、activeは§5へ。U014 |
| E00:21,27,42,46; J00:72,78,115,134,144,164,197,209,237,275,300,329,343–355 | social/P1/profile/outline/notation summaries | mixed | role shorthandと旧矢印の読み分けを導入全体に適用、table/見出し保持。U014 |
| E01:48–60 “Emergence”; J01:210–267 VED的創発・Bio対応 | generic schema→intelligence attractor | historical proposal | LR/LE適用のみhistorical／HOLD、親理論の定義を変更しない。U015 |
| E01:74–80 variables; J01:280–294 preview、315–321 rows、330,367,369 | reference lexicon→§5/appendA | mixed | active役割と旧関数/attractor rowを分離。U015/016 |
| J02:98 “最下層である”,114,213,227–235,251,255 | LF必要性・μ開放窓→architecture | historical/hypothesis | 新supportへ必要性を移さないouter notes。U017。E02 KEEP |
| E03:68; J03:10,228,240–242,262–284; FIG006 figurenotes | old theorem→architecture動機 | historical guarded | 全file KEEP、§5に逆方向の非導出guard。U032 |
| E04:39–43 “The Preview”; J04:107–157 “ログ層…予兆”,trace堆積/summary131 | trace→LR/LE preview | mixed | 登録/保持/参照を別とし、旧regress chainは仮説。U018 |
| E05:4–13; J05:4–16 | chapter scope / outline | mixed | active scope convention新設、旧F/J guard保存。U001 |
| E05:35–43 “Problem Setting” / “The log layer”; J05:42–78 problem / 定義5.1 | stopping question→LR definition | mixed | 問題設定は旧停止構成の動機、LR新roleと旧processを分ける。U001–003 |
| E05:47–60 Definition5.1/schema/FIG010; J05:86–127 定義5.2 / attractor / future functional | LE定義と生成・収束 | historical/HOLD | 定義全文保存、別active説明。U004/005 |
| E05:23–31; J05:26–34 “Historical architecture figure” /「歴史的architecture図の境界」 | FIG009 asset/caption→old architecture | historical guarded | 新role契約との非同一を追加。U006 |
| E05:64–70; J05:135–208 profiles/table | Physarum・Transformer・sapiens、own/内外 | mixed | B1/B2/B3とUnknown、旧比較を観測判定にしない。U007/008 |
| E05:74–91; J05:216–256 “Proposed Emergence Mechanism” / 四段階 | μ→E-site→convergence→LE、projection | historical mechanism | role reassessmentの規則でない。U009 |
| E05:93–117; J05:261–329 E / Φ / recoverability | role→action / network / revisability | old E、Φ unresolved | 式・節を修理せずroleを認証しないouter note。U010 |
| E05:121 Summary; J05:337–362 系5.5;373–385 summary | 三層同時運動・一般知性 | mixed | 系全文historical、active役割への短い戻り文。U011/012 |
| E06:11; J06:8,88–116,134–135 | environmental LE/Physarum/animism | role analogy/hypothesis | 環境所在≠認定LE、同carrierでない。U019 |
| E07:7–21 compression; J07:65–83,97,119,128,144,165 | 神/centralized LE/Φ | interpretation | 支持物合成≠LE/subject、地域的安定解は旧仮説。U020 |
| E08:7–23; J08:57,118–148 | maintenance/intergeneration | interpretation | 長いpersistenceだけでLE/ownnessを認定しない。U021 |
| E09:33–42; J09:35–43,93,109,121–151 | social logs/network/sync | interpretation | 永続logも全history/個体ownLEではない。U022 |
| E10:13,36; J10:22,36,71–108,130–144 | Gettier / knowledge=stop / stability | diagnostic local proposal | 停止からLE認定する循環を禁止、truth/C/μ改訂なし。U023 |
| E11:20–34,49–58; J11:44–66,87–115,127,143–179,205–206 | rate gap / LE不形成・固着 / FIG013 | qualitative hypothesis | 旧phaseがnew role判定器にならない。U024 |
| E12:15,19,31; J12:20–80,93–121,140–164 | R2/R3/N/最終条項 | proposal | 古い必要性/存在判定は採用しない。U025 |
| E13:15,31,35; J13:53,65,94–97,105–124,136,148,165–168 | summary/future/P1 proposal | mixed | active roleと旧mechanismを総括で区別。U026 |
| AE25–27,33; AJ64–65,82,84,121,138,157,168,180 | Master role/function/signature inventory | documentary | 表全bytes保存、外側からLR/LE語のcrosswalk。U027 |
| BE7–34; BJ26–27,51,139–151,176,178 | homology/歴史/Transformer tables | analogy | common support/同じrole criteriaでない。U028 |
| CE19–21; CJ29–35,61,78,109–122,139,147 | P1への未実装提案 | historical editorial | 提案の採用/ownLE/必要性を認定しない。U029、P1 KEEP |
| DJ118,152–162,172–180; DE9–23 | 証明sketch vs EN optional interpretation | historical / indirect | DJ proof全体外にrole非認証、DE既存guardのままKEEP。U030/032 |
| EE7–29; EJ107–126,165 | emergence analogy / stopping functional | historical/HOLD | new quasi-stability≠attractor/minimum、式を再解釈で救済しない。U031 |

sourceのcurrent LR/LE support契約はまだ実装されていない。この表の“active”はimpl27受入contractの移行先であり、current sourceが既にそれを言っているという判定ではない。

## 3. Semantic crosswalk

| Current term | Post-migration role / boundary | Operation |
|---|---|---|
| log layer LR | historical process語は保存。activeはsupport上のscoped trace role。process全体と一支持物は別 | SPLIT |
| emergent stopping layer LE | 名称/章名は履歴を残す。activeはscope/window付きquasi-stable retention role | RELABEL by adjacent note |
| three-layer architecture | functional shorthandは可、三carrier/解剖学的層でない。旧dynamics chainは別 | KEEP WITH SCOPE GUARD |
| LR emerges from traces | registration、retention、actual referenceの別を記す | REINTERPRET |
| LE emerges from LR | 機構仮説の歴史、new roleからの生成則にしない | HISTORICAL ONLY |
| LE is attractor | 旧比較/仮説として保持、active criterionから除く | REMOVE FROM ACTIVE READING |
| inside individual | 宣言system sideに相対化、所在とrole/ownness別 | KEEP WITH SCOPE GUARD |
| externally dependent | path/maintenanceの記述であって外部LE必然lawではない | KEEP WITH SCOPE GUARD |
| Transformer has LR/LE / lacks own LE | 旧profileを保存、三boundaryとcriterion未指定ならUnknown | HISTORICAL ONLY for categorical instance reading |
| trace accumulation | retained traces≠全generated history≠現在accessible archive | REINTERPRET |
| recursive reference | role/processとして維持、pathとsupportと実効feedbackを別 | KEEP WITH SCOPE GUARD |
| stable stop / basin | 停止機構/収束の旧模式、role安定と同じでない | HISTORICAL ONLY |
| stopping supplied by LE | STOPPING HYPOTHESIS。命名から因果を認証しない | HOLD |
| permanent social log | 旧社会的比喩。persistenceはwindow付き証拠が必要 | KEEP WITH SCOPE GUARD |
| LE' | same-support scaffold regimeをproseで名指す略称、専用carrierなし | PROSE ONLY insertion |

## 4. LR migration design

| Element | Minimal active meaning / source action | Consumer / protection |
|---|---|---|
| Canonical active LR paragraph | 宣言scope/windowで再参照対象になりうる登録・保持traceの役割。support同一性とrole評価を分ける | U003、E05:43後/J05:78後。旧paragraphはPS28-06/07 |
| Historical compatibility | log layerは再帰参照processの旧語、supportはその参照対象。全layer/processを一objectに置き換えない | U002、旧定義・所在examples保存 |
| Identity/access | copyは別support、transform/compositeはpolicy/witness、inaccessible≠lost、resurfacing≠自動復帰 | U001に一回、U003から参照 |
| History separation | traceは全generated historyでも必ずaccessibleなmemoryでもない。J/positionをLRへcastしない | §4、§1、§9、Masterに伝播 |
| Missing evidence | registration/参照可能性不明ならcandidate/Unknown。既知access failureだけでsupport消失にしない | U001共通status |

最小意味文案（TeX patchではない）: “Here LR denotes a registered or retained-trace role of a tracked support within a declared scope and window; the historical log-layer process is not identified with that support.” / 「ここでLRは、宣言したscopeとwindowにおける支持物の登録・保持痕跡の役割を指す。旧ログ層の再帰運動全体を、その支持物と同一視しない。」

## 5. LE' insertion design

| Decision | Selected design | Boundary |
|---|---|---|
| First introduction | U003のactive LR段落の直後、同じ一組の新prose内 | §5.2にnumbered subsection/definitionを増やさない |
| Name | “temporary scaffold regime” /「一時的足場regime」を主語、LE'は初出のplain-text別名一回 | new math0、LE-prime carrier/型/層boxなし |
| Meaning | 同じLR supportが以前のtraceとcurrent updateを結ぶ利用可能pathの下で一時的に働く | 単にtrace/cacheがあるだけでは認定しない |
| Reversibility | 弱化、LE-like安定化、access loss、support loss、LE-likeからの弱化を別assessmentとして許す | progression/promotion/inverse operator/thresholdなし |
| Summaries | §5 summary、intro/§13から「§5のscaffold regime」を通常文で参照 | LE'記号をtable/式/全章へ複製しない |
| Sufficiency | canonical explanation EN/JA各一回で十分、profileにはboundary参照のみ | 例をempirical instanceとして追加しない |

意味文案: “The temporary scaffold regime (called LE' in the architecture discussion) is a use-regime of the same LR support, not an additional object or layer.” / 「一時的足場regime（architecture上の呼称LE'）は同じLR支持物の利用regimeであり、追加の物体や層ではない。」plain textの表記自体も独立reviewで確認し、primeの数式notationへ変更する必要はない。

## 6. LE migration design

| Current claims / locator | Classification | Design |
|---|---|---|
| E05:48/J05:91役割名 | ROLE SAFE WITH GUARD | 旧定義scopeは保存。U005がactive quasi-stable roleを独立に説明 |
| E05:52/J05:97,103 internal/external | HISTORICAL ARCHITECTURE | 固定個体を全scopeの必要条件にしない。U004/005 |
| J05:108–127 attractor/minimum | CONVERGENCE HOLD | 全block保存、quasi-stabilityへ式を移植しない |
| E05:74–87/J05:216–242 | EMERGENCE HOLD | four stagesをsame-support regime遷移と同一視しない。U009 |
| E05:97–101/J05:266–285 E acts via LE | STOPPING HYPOTHESIS | E型をrepairしない。U010外側noteのみ |
| positive role criteria | ROLE SAFE | U005: identity/trace・re-reference path・window安定・current-update feedback availability・独立criterion/witnessが必要 |
| FIG009 old basin/stop label | PRESENTATION DEBT | U006で旧図に封じ、asset/caption unchanged |
| simple reference to retention in consumers | ROLE SAFE WITH GUARD | 支持物duration/access/control/autonomyは別と明記、conditionalな役割使用は残す |

active最小意味: LEは宣言scope/windowのquasi-stable retention roleであり、naming、reuse count、large k、一回feedback、old noFP、図のbox、長期存続だけでは肯定しない。first-order availabilityは当該roleの必要な方向だが十分でない。role証拠未確認はUnknownで、不存在の断定でも生成証明でもない。停止したからLE、LEだから停止という循環を禁止する。これをold numbered definitionの差替えに使わず、旧式ブロックの外側のactive段落とする。

## 7. Layer-language policy comparison

| Policy | Readability / compatibility | Ontology risk / EN–JA / figure cost | Choice |
|---|---|---|---|
| A historical/model-local only | 旧章名を保存しやすい | active説明までarchiveに見える危険 | 一部採用 |
| B functional shorthand everywhere | 短く読みやすい | attractor/形成式までrole定義に見える | 単独不採用 |
| C activeすべてsupport/roleへ置換 | distinctionは明瞭 | inline math・旧定義・図・引用の全面修理を誘発 | 今回不採用 |
| D mixed | active paragraphでrole/regimeを定義し、layerは限定shorthand、旧mechanismは局所enclosure | JA長い旧定義とEN短いdraftを別に包める。図はlegacyと明示 | **SELECTED** |

章名、subsection名、definition/corollary番号、literal old math、引用内のlayer語はKEEP。activeな普通文のlayerは機能的な略称まで。新support-role contractは旧layer ontologyの存在・不存在の判定ではない。新active paragraphを§5とsummaryに明示し、「全てhistoricalだから何もactiveでない」という退行を防ぐ。

## 8. Active / historical architecture split

| Layer of assertion | Active source destination | Historical / HOLD boundary |
|---|---|---|
| support identity | U001のscope note、U003のLR説明 | file/bytes/content一致だけで同一物としない |
| LR role / LE' regime | U003、参照U018/016/027 | 旧LR process-definitionは保存、全履歴archiveでない |
| LE quasi-stable role | U005、summary U012/U026 | old attractor/Definition5.1 EN・5.2 JAはU004で囲う |
| Unknown / ownness | U001/U007 | own/not-ownの旧profileから肯定・否定を自動採用しない |
| three discrete layers / one-way formation | 機能略称だけactiveで可 | 旧chain/display/図/系5.5は歴史的構成案 |
| old Φ emergence / E placement | 新contractへ数学的に合成しない | U009/010で旧mechanism、式は完全保存 |
| old Transformer possession | B1/B2/B3ごとの未知assessment | EN categorical否定/JA留保、旧表の差を保存 |

## 9. FIG009 coexistence design

| Aspect | Current evidence / planned boundary | Decision |
|---|---|---|
| Existing body guard | E05:23/J05:26は旧F/Jと形成/own-layer証明の非同一を既に明示 | 必要だがnew support-role契約との区別には追加が必要 |
| Minimum addition U006 | 同paragraph**後**、figure begin**前**に一つの普通文段落を追加。「図の三box・停止basin・LR→LEは保存された旧architecture。active support-role/regime評価の図ではなく、LE'を独立boxに足して読むこともしない」 | SAFE WITH STRONG GUARD |
| Caption / figurenote | E05:25–31/J05:28–34全bytes保護 | 編集0、captionだけ新meaningにすることは禁止 |
| Adjacent new prose | U001で新/旧の読み方を予告し、U003/U005を旧式外へ置く | 図の存在をLE認定の証拠にしない |
| Contradiction / release | assetの強い表示はlegacyとして限定、source-only共存は可能 | 新図受入・PDF配布のreadyではない。build/release HOLD |
| Wait for redesign? | source designは待たない。実装後の独立auditで境界が読めるか検査 | 共存不成立ならsource transaction受入を止め、captionへ無断拡張しない |

新guardは既存guardを弱めない。FIG009の現行SVG/PDFを改変/再生成/再renderするtaskではない。impl27の視覚確認と今回のcurrent body/asset hash不変を参照する。FIG008/010/011/012/013/014の既存captionにも役割/生成語があるため、後述chapter/appendix scope noteがそれらを新role認証として使わないと明記する。図の独立修理には進まない。

## 10. System-boundary source policy

| Boundary | Canonical source addition U007 | Prevented inference / instance status |
|---|---|---|
| B1 Transformer-only | 指定model invocationと可視input/history、外部が管理するcontext/cacheは境界のどちら側か要宣言 | runtime memory→native memory禁止。LE'/LEはpath/criterion未確認ならUnknown |
| B2 model + runtime | storage/controller/retrievalと再投入を分け、停止・保持・再参照・rule管理担当を記載またはUnknown | system-level retention→Transformer ownLE禁止 |
| B3 human-tool/shared environment | 人間・tool・shared supportのrecipientとreturnを別記 | co-maintenance→AI autonomy、境界拡大→subject形成禁止 |

U007はprofiles冒頭にEN/JA各一つのcompact prose note（番号付き新節/新tableを作らない）。以降のPhysarum/Transformer/sapiensは旧比較例であり、実在instanceにSUPPORTEDを付す表ではない。JA summary table直前U008に短い「旧profileの要約、own/not-ownは独立判定でない」注記を置く。ENにJAの表を追加しない。

## 11. Ownness wording policy

| Current word | Future reading / operation | Forbidden shortcut |
|---|---|---|
| inside individual / internal | 宣言scopeのsystem側という位置記述、旧固定個体語はhistory | 内側だからown LE |
| external / externally dependent | path/maintenanceの外側をscope相対に記述 | 外側だから役割が不成立、又は全停止に外部が必須 |
| own / 自前 | 帰還方向・持続・recipient・reuse/control・target別effectの記述bundle | binary ownness、legal ownership、subject predicate |
| autonomous / 自律 | 旧profileの強語は歴史/仮説として保存、active説明で認証に使わない | shared artifactやfeedbackだけでagency |
| internal stopping layer | role/source-of-stop/場所/実効性を分ける | system memory=autonomous stop |

U001でbundle要件を一度宣言し、U007の三boundaryへ適用する。state、surfaced history、update conditions、external structureの変化先を分け、context/parameter変化をrule更新へ格上げしない。predominantly internal/external、reciprocal、weak、indeterminateは必要なら解釈注記までで、今回はsourceにclassifierや全annotation一覧を導入する必要はない。

## 12. Unknown / evidence-status convention

| Status | Compact source convention U001 | Consumer consequence |
|---|---|---|
| SUPPORTED IN DECLARED MODEL | 宣言modelの独立criterionとwitnessに限った肯定 | 現実存在/一般能力の検証としない |
| CONDITIONAL MODEL ASSIGNMENT | 仮定を明記した役割例 | empirical支持に昇格しない |
| NOT SUPPORTED UNDER CRITERION | 指定criterion下の限定的非支持 | 世界全体の不存在・永久的不可能性でない |
| UNKNOWN | 欠測/競合/未指定/異scopeの理由を残す | absent/zero/false/inaccessible/weak/non-autonomous/not-LEへ変換しない |

一つのarchitecture-scope noteで十分な事項は毎paragraphへ複写しない。独立に読まれやすいprofiles、Master、homologyには短い参照を付す。common bindingはsupport tracking、scope、window/timescale、system/environment sides、recipient、re-reference/transformation path、criterion/evidence reference。Unknownで記載できるがcritical Unknownがある肯定認定はしない。

## 13. Consumer coverage and dependency audit

| Consumer | Owner units | Coverage / scope |
|---|---|---|
| main EN summary / JA placeholder | 013 / 032 | COVERED WITH GUARD / NON-TARGET |
| intros / role chains / outline tables | 014 | COVERED WITH GUARD — 矢印と役割名を区別 |
| preliminaries schema / preview / variables | 015/016 | COVERED WITH GUARD — 同じ形の式をactive化しない |
| J02 necessity / opening window | 017 | COVERED WITH GUARD — F/J ports外、μ修理なし |
| §3 proofs / FIG006 | 032 + 001側の非導出 | HOLD — 旧限定済みsource全体を保護 |
| §4 preview of LR / summary | 018 | COVERED WITH GUARD |
| §5 problem setting | 001/004 | COVERED WITH GUARD — 停止問題は動機であってrole認定でない |
| §5 LR definition / scaffold regime | 002/003 | COVERED |
| §5 LE definition / attractor comparison | 004/005 | COVERED WITH GUARD |
| §5 profiles / JA table | 007/008 | COVERED WITH GUARD |
| §5 emergence mechanism / projection | 009 | HOLD formal repair; COVERED WITH GUARD documentary boundary |
| §5 E / Φ / recoverability | 010 | HOLD formal repair; COVERED WITH GUARD role non-transfer |
| §5 corollary / summary | 011/012 | COVERED WITH GUARD |
| §6–9 social / God / religion / shared logs | 019–022 | COVERED WITH GUARD — domain claimsに新criterionを逆適用しない |
| Gettier | 023 | COVERED WITH GUARD — SERIOUS005維持 |
| phase/instability / FIG013 | 024 | COVERED WITH GUARD — ηやvLRをnew support classifierにしない |
| general intelligence / six-seven clauses | 025 | COVERED WITH GUARD — newroleが普遍必要条件ではない |
| conclusions / P1 handoff | 026 | COVERED WITH GUARD |
| Master tables / signatures / relation summary | 027 | COVERED WITH GUARD — oldtable全体保護、来歴不変 |
| homology tables / social profiles | 028 | COVERED WITH GUARD |
| P1 mapping appendix | 029 | COVERED WITH GUARD — P1実装0 |
| Appendix D JA / EN optional notes | 030 / 032 | COVERED WITH GUARD outside proof / NON-TARGET direct role migration |
| Appendix E | 031 | COVERED WITH GUARD — functional future status維持 |
| FIG009 body / assets / caption | 006 / 032 | COVERED WITH GUARD / HOLD edit |
| P1・Bio・CT本体、source_md、working caption Markdown | 032 | NON-TARGET、全面保護 |

現current sourceで未所有のdirect consumerは発見されなかった。これは検索語だけの完全性証明ではなく、section/file inventoryと境界を照合したdesign判定。独立authorization reviewで新consumerや挿入位置の衝突が出たらpacketをHOLDに戻す。既存historical/仮説がsourceに残ること自体を、新しいactive欠陥として数えない。

## 14. Protected content / negative allowlist

このdesignでは**旧TeXの全bytesを保持し、指定paragraph境界へのprose挿入のみ**を想定する。全tableもセル/列/行を変更しない。数学の新規追加はdisplay/inlineとも0、旧104/2199の順序とbytesを保持する。普通文のLR/LE/LE'は新formal signatureではない。追加prose以外を削除・整形・移動する必要が出れば実装を止める。

| Object / span | Status | Allowed surrounding action / forbidden mutation | Verification |
|---|---|---|---|
| accepted F/J ports E02 / J02:13–37 | PROTECTED HISTORICAL/ACTIVE as already accepted | E02全体KEEP。J02の挿入は98/227前のみ。Scopeやpositionをnewsupportへcastしない | PS01/02 + accepted port raw bytes |
| EQF026/027、§3 theorem/corollaries/proof/heading | HOLD / PROTECTED HISTORICAL | E03/J03全体no-edit、§5から役割非導出を明記するだけ | PS03/04、全oldmath/headings一致 |
| DJ全proof-like material | PROTECTED HISTORICAL | 15行以降はheadingから末尾までNO-EDIT。U030は既存intro8後のみ | PS05、sketch bytes |
| old LR definitions | PROTECTED HISTORICAL | E41–43/J56–78外で旧process/newrole区別 | PS06/07 |
| old LE definitions / attractor / FIG010 / future functional | PROTECTED HISTORICAL | E47–60/J86–127を囲う。中の式/定義文・図を修理しない | PS08/09 |
| J05 系5.5と付随説明 | PROTECTED HISTORICAL | U011は337前、本文/heading/箇条書きはKEEP | PS10 |
| E operator / non-membership / Φ identity subsection | HOLD / PROTECTED HISTORICAL | E93–117/J261–320への挿入も不可。U010は直後のみ | PS11/12 |
| FIG009 environment | PROTECTED HISTORICAL | U006は既存body paragraph後、figure begin前。caption/label/figurenote無変更 | PS13/14 |
| μ→E-site→LR convergence mechanism | PROTECTED HISTORICAL | E74–91/J216–256外のscope noteのみ。rule/Φ/E未形式化 | PS15/16 |
| Ω / μ-error / rate / stopping functional / all non-target equations | HOLD / PROTECTED | 既存math・関連定義を変更せず、architectureとの非同一だけouterで説明 | 66TeX旧math配列104/2199一致 |
| LR/LE新prose paragraphs | MIGRATION TARGET, future review pending | 新独立definition番号・predicate・carrier作成なし | U003/U005のpayloadとstatus照合 |
| LR/LE既存普通文・table読み方 | PROSE-SCOPE EDITABLE by additions only | 旧文自体はKEEP、新scope attributionだけ追加 | baselineから追加owneddiff以外一致 |
| all assets / captions / figurenotes | PROTECTED / NO-EDIT | SVG/PNG/PDF全不変、全figure環境保護 | file SHA、TeX figure fragments |
| P1 / Bio F / flow J / J_C / source_md / working Markdown | PROTECTED / NON-TARGET | P2の比較から親sourceを変更しない | full repo manifest |
| labels/refs/cites/macros/counters/input/heading commands | PROTECTED / NO-EDIT | 新label/counter/numbered section/citeなし、既存S参照保持。新参照は通常文で既存§5等を指す | command列比較、raw command保持 |
| titles / MJ abstract / preambles | PROTECTED / NO-EDIT | JA概要補完・title改題・全体整理は対象外 | 全file/fragment SHA |

### PS28 protected fragment hashes

hashはUTF-8 raw bytesの指定inclusive line範囲、末尾改行を含む。future implementationは下記start/endのliteral文字列を含む元fragmentを一意に探索し、line shiftに依存せず再hashする。本文の表記差やhash不一致があればbaselineを黙って更新しない。元66TeX raw bytesは§22 snapshotにも保存した。以下の省略anchorは探索の説明であり、hash対象を省略した意味ではない。

| PS28 | File / current span / anchor boundary | SHA-256 |
|---|---|---|
| 01 | E02:1–74 whole file（English draft comment→final bigskip） | `412df1bc10ec5ae25c75e774932d91b5491f783daa314f58c795f642f18584f3` |
| 02 | J02:13–37 推論演算子Fの定義heading→保存する旧局所状態模型paragraph inclusive | `a42b673a9d8be929649caed17dae36c1ab5a5b41bb2cfc4b423ec443d6a03c16` |
| 03 | E03:1–70 whole file | `f0997b6301f0961fb912fadcf73e20617ba59bcbde93113304e44c13d36e034f` |
| 04 | J03:1–286 whole file | `34dde6cad3e336c9417a66eb2f23f56adeef30a94da570b69880429ea40052c7` |
| 05 | DJ:15–202 定理3.1 subsection→EOF | `3286112ed48169ebb7a8e078f307bb3ccf69ba1cf0ac1cb49bc081b14bc5a8dc` |
| 06 | E05:41–43 “The log layer”→“both individually and socially.” | `6537cc07d847a20f2dc61f33094e3a7c1b5ac83feb96fc856cab7e56b8f34aa4` |
| 07 | J05:56–78 “予兆として示した”paragraph→Bio-IFGT typed translation paragraph | `bbda169cf310ae261e51979f0644770fd9df16aed5c819529b5b3a324f180d00` |
| 08 | E05:47–60 Definition5.1→FIG010 end figure | `a9d1eaaab56f3969a26b5cb0ab4c6d5934d487c2da0a105147977b2396c9fecd` |
| 09 | J05:86–127 “ログ層…を基盤として”→停止汎関数future paragraph | `740e2eb758b8a7cea09ecabfc97e44f392972a4a7ac389685c3b9f256fae9c34` |
| 10 | J05:337–362 “本章の構成案を”→“以降の章は”paragraph | `7addc14739406500d87a3041082c780f0bf59b817b02d69a709b25a47a46892d` |
| 11 | E05:93–117 External Stopping Operator heading→FIG011 end figure | `5e906778398cdc42a408ef4adc883ebb9f177d71ab25c2e302baf1d928c0262b` |
| 12 | J05:261–320 外部停止演算子heading→FIG011 end figure | `9ae913e4ae7b7b1b3016c3fa3f57733b016f3824153632522a97ebd3f0062d2d` |
| 13 | E05:25–31 FIG009 complete environment | `aa28aa7e4e560e908955d291c0b04f3f373f98489798a356f94c1bb15885893b` |
| 14 | J05:28–34 FIG009 complete environment | `bcfd14301dbd469f1c39da9ba70f5f4055057e4d7d4e46812044bd8baed4f1e2` |
| 15 | E05:74–91 emergence paragraph→projection comparison paragraph | `cad0e604f976c02c94a2ea09890aa821746320b5f1c810e9c373d618821a1546` |
| 16 | J05:216–256 機構仮説paragraph→psychological disclaimer paragraph | `eae7c18571564d9b3f9c5307e9827f3fd1fb3600075bba36a28d72244dcea909` |

16fragmentsは追加の強い保護であり、それ以外のold textを編集してよいというallowlistではない。former PS21保護、impl24受入F/J status段落も、今回の全oldbytes preservationで維持される。

## 15. Edit semantics / shared rollback rules

次表のU28はcanonical design units。unit番号は本record内でのみ短縮する。各行の`before/after`は**anchorを含む元paragraph/環境の外側**への挿入で、anchor textは変更しない。共通条件は各unitへ適用する。

- D0 prerequisite: impl27の契約、今回のsource baseline、全PS28・oldmath一致、独立authorization。現在は最後のauthorizationが未充足。
- P0 prohibited: 存在/収束/停止/ownness/新J証明の認定、sourceのoldbytes・math・refs・caption・heading変更。追加proseにも数式delimitersやnew formal symbolsを入れない。
- R0 rollback: anchor不一意、protected overlap、source drift、P0違反があればSTOP。将来実装中ならそのtaskの**owned additionsのみ**をreverse patchで戻す。既存dirty changesをresetしない。意味受入はtransaction全体で行い、一unitだけ完成扱いしない。
- Review requires semantic payload equality, not word-for-word translation. 下表の短いintentを越える理論変更・実系判定が必要なら独立reviewへ差戻す。

## 16. U28 source edit units

| Unit / exact file + anchor | Problem / operation / bounded intended meaning | Dependency / protected interaction | Additional rollback trigger |
|---|---|---|---|
| U28-001 E05:8 “The three profiles retain”; J05:8 “三profileの具体例は保持する” **after paragraph** | ADD GUARD + active scope note。§5でsupport identity、役割、assessment scope/window/recipient、criterion/Unknown、ownness bundleを説明。problem settingと図・旧定義は存在認証でない | D0。既存4/6/8のguardと11–14 F/J境界はKEEP。U003/005が肯定的意味の実体 | scope noteが全章をarchivalにしてactive rolesまで消す |
| U28-002 E05:41 “The log layer”; J05:56 “予兆として示したログ層” **before paragraph** | HISTORICAL ENCLOSURE。続く旧LR definition/processと所在例は保存、endをE43/J78までと指示し、新role説明は直後 | U001。PS06/07の直前、heading/定義文改変なし | 旧layer processを単一supportに再定義 |
| U28-003 E05:43 “both individually and socially.”; J05:78 “typed translationを確立したわけではない。” **after paragraph** | SPLIT / active LR + temporary scaffold prose。§4/5の最小文案とtrace/history/access分離、LE' regime・可逆assessmentをここだけで定義 | U001/002、PS06/07の外。新節/式なし | LE'独立type、必須promotion、全履歴archive |
| U28-004 E05:47 `Definition 5.1 (Emergent stopping layer)`; J05:86 “ログ層…を基盤として” **before** | HISTORICAL ENCLOSURE。旧LE numbered definition、schema、attractor比較と図を保存。E60/J127まで旧architecture、new definition portではない | U001、PS08/09直前。EN/JA定義番号差KEEP | historical enclosureが新role証拠に読める |
| U28-005 E05:60 `end{figure}`（fig5_three_examplesに属するもの）; J05:127 “形式化は後続研究の課題とする。” **after** | active LE prose。scope/window準安定role、独立criterion/witness、feedback必要方向≠十分、support存在/停止の非認定。旧blockの終了も明記 | U001/003/004、PS08/09外。captionに接触しない | attractorやstopping functionalを準安定roleの定義に移植 |
| U28-006 E05:23 “Historical architecture figure.”; J05:26 “歴史的architecture図の境界。” **after paragraph** | ADD GUARD。§9の最小追加、次図はnewrole/LE' diagramでない。unchanged captionも同じ旧scope | U001、PS13/14直前。既存guard完全KEEP | old assetをactive contract図として必要とする、caption変更が必要 |
| U28-007 E05:64 “Three systems clarify”; J05:135 “機能的解釈を比較するため” **after paragraph** | SPLIT。B1/B2/B3、ownnessはbundle、実例criterion不明はUnknown。続くE66–70/J137–208は旧profile比較でsupported/absence判定でない | U001/003/005。旧profile text/μ保持、E72/J213でenclosure終了 | model-nativeへruntime capabilityを帰属、Physarum実証追加 |
| U28-008 J05:183 `begin{longtable}`（“三者は二つの軸”直後） **before**; EN no counterpart | ADD GUARD。表は旧profile要約、自前/非自前は独立criterionの判定でなくU007に従う | U007。表183–196全bytesKEEP | cell修理・新EN表・μcolumn変更 |
| U28-009 E05:74 “The emergence ... four schematic stages”; J05:216 “ここまで ... 機構仮説” **before paragraph** | HISTORICAL ENCLOSURE。段階/矢印/投影は旧未実行機構であり、newrole評価やLE'遷移則でない。E91/J256まで | U004/005。PS15/16外 | E/Φ/μ modelやproofを補う必要 |
| U28-010 E05:117 `end{figure}`（fig6_phi_ext_phi_net）; J05:320同environment **after** | ADD GUARD。preceding E/Φ notationはnew support/roleへ移植しない。re-reference/returnは作用・同期・回復の証明でなく、JA後続325–329も仮説のまま | U001/005、PS11/12外。old E/Φ subsection全KEEP | E/F^k代入、Φ関係の修理、回復の保証 |
| U28-011 J05:337 “本章の構成案を” **before paragraph**; EN no corollary counterpart | HISTORICAL ENCLOSURE。系5.5と362までの帰結は旧構成案。newroleの必要十分条件・一般知性判定でない | U005/007、PS10外。系heading/本文/箇条書きKEEP | 系を別propositionへ改名、number変更 |
| U28-012 E05:121 “The proposed architecture relates” **after**; J05:370 “本章で区別して提示したのは” **after** | SPLIT summary。新たに採用するのはscoped support/role/regimeの記述契約、残す列挙は旧定義/未確立mechanism、停止仮説は別 | U003/005/007/009–011。既存summary数学と項目不変 | readerがactive roleを特定できない、旧式を新式と読める |
| U28-013 ME18 abstract paragraph **after**, before `end{abstract}`; MJ KEEP | ADD active summary sentence。retention rolesとtemporary scaffold、oldemergence/図の非認証を明示。新notationなし | U001/003/005。title/abstract既存math/authority line保持 | JA placeholderを補完、EN abstract既存claim改稿 |
| U28-014 E00/J00:4 scope paragraph **after**; 加えてE00:11 “The central structure” / J00:50 “第三線” **before** | ADD GUARD。全introのlayer/shorthandは§5 role説明へ、矢印は旧機構。oldprofile/table/outline/P1対応は歴史/仮説でrole認証でない | U001/012。旧display/heading/table/notation J300KEEP。P1変更なし | 全introや社会比較をretireする、新3層存在law |
| U28-015 E01/J01:4 scope paragraph **after** | ADD GUARD。LR/LEへのemergence適用とprofile previewは旧案、新roleは§5へ。generic VED/Bio定義・flow Jを変更しない | U003/005。E48–60/J210–294保護oldbytes | 親schemaやBio subsetをnewroleに再署名 |
| U28-016 E01:64 first Variables longtable **before**; J01:304 “新規導入する変数” longtable **before** | ADD GUARD。LR/LE rowsのlayer/attractor/関数語は旧inventory、active scoped rolesは§5。表後summaryもこの区分 | U015/027、全table構造/rows/oldmath保持 | row追加・削除、oldF/J表の再修理 |
| U28-017 J02:98 “最下層である” **before paragraph**; J02:227 “機構仮説の候補が” **before paragraph**; E02 KEEP | HISTORICAL ENCLOSURE。旧LF→LR/LE依存語とopen-window chainは旧構成案。後続profile参照はnewscopeの肯定証拠でない | U001/003/005。PS02や他F/J guardに触れず、μ式完全KEEP | accepted F/J coreのsignatureや意味を変更 |
| U28-018 E04:41 “Traces of inference”; J04:114 “この堆積した痕跡を” **before paragraph** | REINTERPRET by note。章末までのLR previewは保持・参照の候補。newregistered-roleは§5、regress/chainは旧仮説 | U003。figure/proof-like regressを修理せず、旧chain保持 | continuedF⇒LR/LE、保持=access |
| U28-019 E06/J06:4 scope paragraph **after** | ADD GUARD。chapterのenvironmental LE/Physarum比較はrole analogy、support/recipient/criterion未指定を埋めない | U001/007。全式/親field/社会解釈の内容保持 | 社会・生物instanceをsupported LEと認定 |
| U28-020 E07/J07:4 scope paragraph **after** | ADD GUARD。centralized/shared supportという解釈とliteral同一LE/subjectを分ける。E/Φ機構を直さない | U001/007/010。oldΦ・God equation保持 | God=E、新network map、composite⇒LE |
| U28-021 E08/J08:4 scope paragraph **after** | ADD GUARD。長期maintained roleとの比較はconditional、persistence alone≠LE/ownness | U001/005/007。歴史・宗教・μ修理対象外 | 世代持続だけでrole証拠やautonomy |
| U28-022 E09/J09:4 scope paragraph **after** | ADD GUARD。social LR extensionは別scope assessment、sharedlog≠全history、network≠個体LEの認証。chapter全summaryとFIG012に適用 | U001/003/007。figure/caption/theoryclaim旧bytes保持 | 群体から個体へscope lifting、Φ修理 |
| U28-023 E10/J10:4 scope paragraph **after** | ADD GUARD。Gettier診断・旧knowledge/stopping局所定義はrole同定の証拠でない、stopped⇒LE⇒stopの循環禁止 | U005。C/truth/μ/equivalence・見出し保持 | Gettier由来のLE証明、μやtruth理論変更 |
| U28-024 E11/J11:4 scope paragraph **after** | ADD GUARD。新role assessmentと旧vLR/η/四重崩壊/FIG013は別。速度gap/欠如命名からLE不在を認定しない | U003/005。全rate/phase/math・figure保持 | newthreshold/classifierやrule-modelを追加 |
| U28-025 E12/J12:4 scope paragraph **after** | ADD GUARD。R2/R3/最終条項の旧構成条件とactive役割説明を分離、newregimeを普遍条件へ追加しない | U005/007/011。N/R数・最終条項・Φ式全KEEP | necessity adoption、six/seven統一、μ修理 |
| U28-026 E13:15 “Third: three-layer dynamics” paragraph **after**; J13:53第三線paragraph **after** | SPLIT。active roleの現在寄与を一段落で示し、後のΣ/functional/P1handoffはfuture/未実装。旧summaryに新proofなし | U012/025/029。P1引用/J13:107–113等不変 | sourceacceptanceをLE証明に拡張、P1採用 |
| U28-027 AE9 “Historical inference inventory” **after**; AJ49 “推論演算子と三層動力学” heading **after** | ADD GUARD。LR/LE entries、E供給/Φnetwork consumerは旧role inventoryと未確立機構。active説明へのprose pointer、新rowなし | U003/005/010。AJ64/65/82/84/121/138/157/168/180を含め表・式保持 | v2.1 gapを解消、flowJ/Bio/oldJと混同 |
| U28-028 BE/BJ:4 scope paragraph **after** | ADD GUARD。全homology表のLR/LEは旧comparative vocabulary、support identity/role基準の移送やTransformer分類をしない | U001/007/027。全table/ENJA列差保持 | sharedtable⇒commoncarrier/LE実在 |
| U28-029 CE/CJ:4 scope paragraph **after** | HISTORICAL ENCLOSURE。P1への三層profile/生成/必要性の記述は保存された未実装提案、新contractが採用した証明/改稿指示でない | U007/026。引用・表・優先順位・P1全KEEP | CJ147公開時P1改稿の実行、auto-sync |
| U28-030 DJ8 “本補遺は、本論文で提示した” paragraph **after**; DE KEEP | ADD GUARD。全以下sketchのLR/LE・収束・ネットワークは旧仮説、newrole認定ではない。旧proof内容をnewroleで救済しない | U005/010。既存DJ13guardとPS05不変 | sketch heading/premise/closing text変更 |
| U28-031 EE/EJ:4 scope paragraph **after** | ADD GUARD。LE attributionとstopping-functional/minimumは旧analogy/future。quasi-stabilityは新attractor定義でない | U004/005。EJ43定義/式/foreigndomain記述不変 | functional採用、newΦ関数、parent物理の修理 |
| U28-032 E02、E03/J03、MJ、DE、preambles、P1/Bio/figures/all oldmath | KEEP / PROTECTED / NO-EDIT | D0/PS、§14のnegative allowlist全適用 | 一byteでもauthorized addition以外の変更 |
| U28-033 newEQF026/027、E/Φ/μ/rule-model、figure/caption/newnotation | HOLD | 別design・別authorization・必要な型/証拠なしには着手不可 | sourceprose taskをformal/visual修理へ拡張 |

U013–031のguardはchapter-wideにもかかわらず**architecture attributionだけ**を対象とする。生物学・Gettier・社会史・phaseの議論全体を新たに否定/退役させる文章にはしない。oldclaimsの強さは既存guardに従う。追加noteがそれを再強化したり、全historyへ埋没させたりしないかを将来独立auditで検査する。

## 17. EN / JA authority and notation

| Slice | Bilingual mode | Constraints |
|---|---|---|
| active scope / LR / LE' / LE paragraphs | JA-first semantic migration; safe parallel migration after semantic check | 同じaccepted meaningをENへ、word countやparagraph位置は合わせない |
| historical definitions / profiles | language-specific historical retention | JA定義5.1LR/5.2LE、EN定義5.1LEの非対称を保持。ENにJA表を増設しない |
| EN abstract / JA placeholder | EN documentary summary only | MJ全KEEP、P2 JA primary/EN working-draft文不変 |
| Master / homology | EN documentary mirror of meaning, not table shape | EN no-J row、JA additionalcolumns/provenanceを保存 |
| Appendix D / P1 proposals | language-specific historical retention | EN optionalnotesをJA proof集へ変えない。P1 JA intent/EN stabilizationはP1編集許可でない |
| all formal correction | HOLD | JA priorityで証明・存在・typed equivalenceを決定しない |

| Possible notation | Selected classification | Reason |
|---|---|---|
| RetentionSupport | DESCRIPTIVE METAVARIABLE / prose explanation | 仕様対象sortの名前として説明可、sourceに新数学carrier宣言しない |
| LR role predicate | NOT NEEDED | 普通文のscoped roleで足りる |
| LE' | PROSE ONLY | 一度別名を与えるだけ、prime変数/新layerなし |
| LE role predicate | FORMAL SYMBOL LATER | instance認定を計算するpredicateを今追加しない |
| assessment record notation | NOT NEEDED | field obligationsはcompact scope noteで記す |
| newhardness/ownness/viscosity symbols | NOT NEEDED | score/threshold/単位を選定しない |

新display/inlineを一つも要求しない。plain-textのLR/LE/LE'やScope/Unknownは記述ラベルで、旧math glyphを無資格に別signatureへ流用したものではない。新command/macro/label/heading番号も不要。

## 18. Transaction strategy

| Option | Risk / dependency assessment | Decision |
|---|---|---|
| A one coordinated prose transaction | 旧定義の囲い、active説明、全consumerのstatusを一体で受入可能 | **SELECTED** |
| B active definition first / consumers later accepted | tables/summaryが旧層をactiveで再導入するmixed state | 不採用 as separate accepted states |
| C EN/JA staged acceptance | authority/asymmetry比較前に片言語だけ新roleになる | 不採用 as separate accepted states |
| D historical enclosure first / active later | 全archivalに見える中間状態が残る | 内部作業順のみ可、完了扱い不可 |

future transaction内部順: preflight baseline/PS → U001共通scope + U002/004/009/011historical境界 → U003/005active定義 → U006/007/008図/profile境界 → U010/012 → U013–031consumer → U032negative allowlist → implementer self-check → independent post-migration acceptance。どの中間段階もaccepted sourceとしない。

最大proposed allowlist35files: ME、E00/J00、E01/J01、J02、E04/J04、E05/J05、E06/J06、E07/J07、E08/J08、E09/J09、E10/J10、E11/J11、E12/J12、E13/J13、AE/AJ、BE/BJ、CE/CJ、DJ、EE/EJ。将来独立reviewで不要と判定したunit/fileは明示的に除外してよいが、consumer coverageの穴を残してはならない。impl22の旧28files allowlistを流用した権限ではない。

rollbackはuserの既存変更を含むrepo resetでなく、task開始時snapshotとの差分のうちowned additionsのみを戻す。oldbytes・math順序・proof・captions等が変わったらtransaction全体を未受入へ戻す。将来の独立reviewで追加段落だけでは意味を安全に区分できない箇所があれば、そのunitを勝手にrewriteへ拡張せず、amendmentを要求する。

## 19. FIG009 handoff boundary / release conditions

source designの前提は旧assetの現状維持とU006のbody境界であり、redraw、caption rewrite、E/Φ/μ模型完成、LE存在proofを要求しない。後続FIG009ownerへ渡すのはimpl26/27のsemantic constraints、actual source migration受入後のactive語彙、legacy図の存続statusとcoexistence debt。node配置、line style具体案、caption新文案は本packetに含めない。

FIG009新版を後で作る際はsupport/role/Scopeの区別とUnknownを図自身にも表現し、本文guardを読まないと安全にならないactive新図にしない。一方このsource-only packetは旧図を新図として認めず、release/buildはNOを維持する。FIG011修理も選定していない。

## 20. Readiness / independent authorization handoff

| Work | Status | Release condition / limitation |
|---|---|---|
| source migration design packet | READY WITH GUARD | current consumer map・U28・PS28を独立に再検査する |
| source implementation authorization | HOLD | 別taskでunit/anchor/protection/coexistence/semantic payloadを独立承認するまで不可 |
| FIG009 redesign design | PARTIAL | semantic inputは既存受入済み、別owner選定/packet必要。今回は開始しない |
| FIG009 asset redraw | NO | source受入とは別のdesign/authorizationが必要 |
| caption rewrite | NO | 現assetとのcoordinated designなしには不可 |
| equation edit | NO | newmath0、EQF026/027/E/Φ/μ/Ω/functional HOLD |
| proof edit | NO | oldtheorem/kernel・proof-like materialを保護 |
| build / distribution | NO | sourceimplementationさえ未実施。図debt/別build/parity auditも未完 |

このpacketはauthorの意味選択を増やしていない。新author clarification: **NO**。threshold、instance判定、notation、layoutをauthor questionへすり替えない。次のtaskは本designの**independent authorization reviewのみ**が適切で、source migrationをここでauthorizeしていない。

## 21. Verdict / explicit questions

**LR/LE'/LE SOURCE MIGRATION DESIGN READY WITH HOLDS**。

| # | Question | Answer |
|---|---|---|
| 1 | LR source migration design ready? | YES |
| 2 | LE' insertion design ready? | YES — canonical prose regime only |
| 3 | LE source migration design ready? | YES — role scope, no existence result |
| 4 | Layer-language policy selected? | YES — D mixed |
| 5 | Active/historical split clear? | YES in design; current source not migrated |
| 6 | Direct consumers completely mapped? | YES for current inspected source; independently recheck before authorization |
| 7 | FIG009 legacy coexistence safe? | YES under strong body guard, source-only and unreleased |
| 8 | B1/B2/B3 source policy ready? | YES |
| 9 | Ownness wording policy ready? | YES — descriptor-only |
| 10 | Unknown/evidence policy ready? | YES |
| 11 | Negative allowlist complete? | YES within selected prose slice; all oldbytes also protected |
| 12 | EN/JA migration path specified? | YES |
| 13 | New notation immediately required? | NO |
| 14 | New author clarification required? | NO |
| 15 | Source implementation may be authorized next? | PARTIAL — separate independent review can consider this packet; authorization not inherited |
| 16 | FIG009 redesign may begin next? | NO — not separately selected |
| 17 | Equation editing allowed? | NO |
| 18 | Proof editing allowed? | NO |
| 19 | Source edited? | NO |
| 20 | Figure edited? | NO |
| 21 | Build performed? | NO |
| 22 | Commit/push performed? | NO |

## 22. Validation

task-start snapshot: `${TEMP_EVIDENCE_ROOT}/int_impl28.X3Mlar/baseline.json`、SHA-256 `278730e8c5dbc710a960f1ec7c0af54809ec83bc3152c448bdb2a2804123c432`。1525 regular repository files（ignored/untracked含む、`.git`内部除外）のSHA-256、66IntelligenceTeX rawbytes、README originalbytesを保存した。currentTeXはimpl27 baselineとも一致、material source drift0。

task-start `git status --short` 全文: `${TEMP_EVIDENCE_ROOT}/int_impl28.X3Mlar/task_start_git_status.txt`、SHA-256 `7acabaa3e1d8d38213e97a94af0d85612d59ae4d7dab1ca790b691b716e1da5e`。M289/??9、298entries。audit directoryはuntracked directoryとして集約表示されるため、本taskの新recordはfile manifestで個別確認する。user-owned dirty changesを本taskの変更と取り違えない。

| Check | Result / method |
|---|---|
| Allowed changes | impl28新規 + README appendのみ、1525→1526files、deleted0 |
| README append-only | baselineの原bytesが完全prefix |
| Phase00–07 / impl01–27 | 35既存records SHA-256不変 |
| TeX / math | 66files byte-identical、display104 / inline2199不変 |
| theorem/proof/equation/caption | 全TeX不変。PS28-01–16をraw fragmentから算出、current bytes保存 |
| figures/PDF/BibTeX/P1/Bio/source_md/working Markdown | README以外の既存file全SHA一致 |
| git diff --check | PASS。新untracked recordのtrailing whitespaceも別検査 |
| git status --short | task-startと完全一致、既存変更保存 |
| No prohibited actions | source/figure/caption edits0、web/build/distribution/simulation/commit/push0 |

validatorはrepo外 `${TEMP_EVIDENCE_ROOT}/int_impl28.X3Mlar/check.py`。snapshotが保証するのはfile contentであり、git内部objects/metadataの固定ではない。本recordの候補文・unit・hashは設計証拠であって、source editを行った結果ではない。

## 23. Stop boundary

source migration design、consumer coverage、protected-boundary設計、transaction/readiness、validationで停止。migration実行、FIG009 redraw/caption rewrite、equation/proof/E/Φ/plasticity実装、build/distributionへ進まない。

# Consciousness core revision — Implementation 01 v0.1

## 0. Status

```text
Consciousness audit: CLOSED
Final dispositions: FROZEN
Consciousness core revision: IN PROGRESS
Implementation 01 source identity / provenance / version / scope: COMPLETE
Implementation 02 core / window / SSO / TCA / loop: NOT STARTED
```

2026-09-10。対象14 FINALの今回指定されたsource identity / provenance / citation / version / scopeだけを実装した。KEEPの保持検査とOPENの明示も実装に含むが、研究問題の解決を意味しない。core revision全体の完了・closureではない。

Theory source EN6 / JA6を変更、本記録を作成、監査READMEを更新。数式・notationの置換、図・caption・PDF・code・旧監査の変更、外部研究、commit/pushは0。

## 1. Frozen authority

最上位authorityは[Phase07 final audit](07_final_audit_and_frozen_dispositions_v1.0_ja.md) §4、17、22、24–26、29–32、および[監査README](README_ja.md)。105 final dispositionsと44 KEEP /20 REVISE /21 DOWNGRADE /19 SPLIT /0 RETIRE /1 OPENを変更していない。今回の対象集合はユーザー指定の14件。

式baselineには[Phase01 inventory](01_equation_symbol_object_inventory_v0.1_ja.md)の178 raw blockも使用。current [IFGT fundamental dynamics](../../Information-Field-Geometry-Theory/sections/fundamental_dynamics.tex)のtau/J/F_Iと[IFGT unified equation](../../Information-Field-Geometry-Theory/sections/unified_equation.tex)の三項・外的時間近似を読んだが、歴史的帰属をこれから推定しない。

source reuse ≠ source identity; citation ≠ validation; historical provenance ≠ current formal equivalence; local variant ≠ canonical merge; projected use ≠ typed translation; background empirical claim ≠ Consciousness validation。

## 2. Target FINAL dispositions

| CON-FINAL | Frozen action | Source location (EN/JA) | Implementation 01 handling | OPEN preserved |
| --- | --- | --- | --- | --- |
| CON-FINAL-026 | KEEP | S06 IFGT Mapping | 再参照可能log densityの定義を保持し、model量の文脈を明示 | CON-OPEN-006 |
| CON-FINAL-027 | REVISE | S06 I paragraph | cognitive historyをIにより表現。計数・測定mapは未供給 | CON-OPEN-006 |
| CON-FINAL-028 | REVISE | S06 J_log paragraph | J_Iのformal slotとJ_logのeffective flowを区別、担体・同定未供給 | CON-OPEN-006 |
| CON-FINAL-030 | REVISE | S06 IFGT Core Relations / S07 IFGT Coupling / S16 Limits | current IFGTとCon局所templateの記号・時間・versionを分離 | CON-OPEN-006/020/021 |
| CON-FINAL-032 | KEEP | S06 Projection Definition | disproportionate influence定義と非意図性を保持、共通typed operatorを定義したとしない | CON-OPEN-024 |
| CON-FINAL-050 | REVISE | S10 Libet / section opening / repeated attributions | 背景記述と本稿の読みを分離、直接測定・検証への帰属を修正 | CON-OPEN-014/026 |
| CON-FINAL-055 | REVISE | S10 Split-Brain / correspondence / summary | 行動・言語非対称を背景とし、log-flow観測としない | CON-OPEN-015/026 |
| CON-FINAL-058 | REVISE | S10 Rationalization / repeated attribution | well-knownを背景例に変更、補完の読みを実験結果としない | CON-OPEN-015/026 |
| CON-FINAL-061 | REVISE | S14 opening / summary | 神経・身体依存をgeneric背景前提とし固有モデルの根拠にしない | CON-OPEN-013/026 |
| CON-FINAL-078 | REVISE | S06 VED Closure Degree | C_ijの節点対とC_f/C_s/Delta Cの層量を区別、集約規則なし | CON-OPEN-017/020 |
| CON-FINAL-081 | OPEN | S06 older PDEの直後 | 旧VED/改訂Vol4帰属を保持し、exact history/version未解決注記のみ | CON-OPEN-020/025 |
| CON-FINAL-093 | KEEP | S06 projected uses / S07 nonidentity | 既存非同一guardを保持し、局所templateの冒頭でtyped translationなしを明示 | CON-OPEN-020 |
| CON-FINAL-096 | KEEP | S16 Theoretical Limits | T_Phi非測定量・neural/report map未完成を保持。future promiseなし | CON-OPEN-001/005/006/013/029 |
| CON-FINAL-103 | REVISE | S05 figure2直後、JA weighted approximation | JA source-local現象論的近似という両版注記。式・版差不変 | CON-OPEN-005/021 |

14/14 coverage。081は「OPENを保った出典注記」の実装完了であり、provenance問題の完了ではない。026/032/093/096はKEEPを別dispositionへ変更していない。

S10の反復帰属を整える際、052/054/056/059/060に接する「measured」「shows」「可視化」「実験が示した」の主語・scopeのみも修正した。050/055/058の背景と解釈の分離が同節後半で撤回されないための隣接処理である。これら隣接FINAL全体を実装済みとは数えない。必要十分性、自由意志・主体数・現象的opening・補完機構の本格的status修正は後続段階へ残す。

## 3. Source files changed

| Source pair | EN | JA | Change scope |
| --- | --- | --- | --- |
| formal_mapping | [EN](../../consciousness/sections/formal_mapping.tex) | [JA](../../consciousness/sections_ja/formal_mapping_ja.tex) | I/J・IFGT局所template・projection定義guard・閉包object・旧PDE由来 |
| core_equations | [EN](../../consciousness/sections/core_equations.tex) | [JA](../../consciousness/sections_ja/core_equations_ja.tex) | 一般IFGT変数という一文だけを局所使用へ |
| experimental_reinterpretation | [EN](../../consciousness/sections/experimental_reinterpretation.tex) | [JA](../../consciousness/sections_ja/experimental_reinterpretation_ja.tex) | 背景と再解釈の帰属、未確認出典・未測定の明示 |
| non_localization | [EN](../../consciousness/sections/non_localization.tex) | [JA](../../consciousness/sections_ja/non_localization_ja.tex) | generic neural/body背景前提とsummaryのscope |
| torque_converter_attention | [EN](../../consciousness/sections/torque_converter_attention.tex) | [JA](../../consciousness/sections_ja/torque_converter_attention_ja.tex) | JA限定3式のlocal variant注記（ENに式を移植しない） |
| pathologies_limits | [EN](../../consciousness/sections/pathologies_limits.tex) | [JA](../../consciousness/sections_ja/pathologies_limits_ja.tex) | observable未完成を維持し、局所定義という一語句を同期 |

12 source files（6 EN/JA pairs）、既存監査README1、new record1。開始時の未commit変更を基準に追加分だけを比較した。core_equationsの変更はIFGT変数の帰属一文のみであり、Implementation02のcore/window/SSO作業ではない。limitsもlocal definitionへの一語句の変更のみ。

Source単独差分はgit diff --statで追加75行／削除61行。下表の開始時比較はdifflib集計で追加81行／削除67行となるが、差分の区切り方による違いで純増14行は同じ。以下は開始時と変更後のSHA-256であり、既存dirty treeをHEADと同一と仮定しない。

| File | Before SHA-256 | After SHA-256 | + / − lines (turn baseline) |
| --- | --- | --- | --- |
| [consciousness/sections/formal_mapping.tex](../../consciousness/sections/formal_mapping.tex) | `45e7eef5070a92d13fcc01b47655ec9c6f78bbd63709b7dffcdbb32181e61978` | `a51e0cc4ff0026eadcacd07e2fc8c4fa140aede8b488d21c5d0bf67be177b13f` | 11 / 5 |
| [consciousness/sections_ja/formal_mapping_ja.tex](../../consciousness/sections_ja/formal_mapping_ja.tex) | `19b8df88662369f994e9c55db600dce654b318fd69c9d29dd2f6d21a749e2e24` | `c73a6ab0e756b23e7bf7d7cea4d00ba5a7422f4b5859e0e98fe49e0ab4a28dc7` | 11 / 5 |
| [consciousness/sections/experimental_reinterpretation.tex](../../consciousness/sections/experimental_reinterpretation.tex) | `4a883cb7bde66feb435a58de82a70c597068610e6082068c075f6e5241a32e19` | `1f5bd8e8c9880e1cbe7885badfa87844353378190588f9cee0e8f7276c45fcd1` | 23 / 23 |
| [consciousness/sections_ja/experimental_reinterpretation_ja.tex](../../consciousness/sections_ja/experimental_reinterpretation_ja.tex) | `70f226e8f94b8dd051fa02357d8859bfa848d98ab914a6fc9ae6512ffeb6174c` | `dfebe0f86e551392be5e8f82351665587d972d3359a5520897241aa6c200e910` | 23 / 25 |
| [consciousness/sections/non_localization.tex](../../consciousness/sections/non_localization.tex) | `9cd663020a9b5e928a4a0a8222006e75f12aec1ada35953085525747f37a106d` | `8857d81deb438695ba21a4c736c665b5bc8d4046c736cc802ad6e94c8682d3a2` | 2 / 2 |
| [consciousness/sections_ja/non_localization_ja.tex](../../consciousness/sections_ja/non_localization_ja.tex) | `2d4ee652fe6355c586198ac1989f193c730ac88114717e5a7ca4fa919099a7ce` | `d3f9feeac4227b3c96e2d0938ba11f88ef2b414706284b64cdead08f0fe43ab3` | 2 / 2 |
| [consciousness/sections/torque_converter_attention.tex](../../consciousness/sections/torque_converter_attention.tex) | `a87df1e226ae9ba2caec40b9483238ab25e10f686f6616506082c6d4543ec9ab` | `3d391dd717d1f2474adfd412a3aa1d2e4e5158a999b5b5817cfbec597680e427` | 2 / 0 |
| [consciousness/sections_ja/torque_converter_attention_ja.tex](../../consciousness/sections_ja/torque_converter_attention_ja.tex) | `bc7e40c43fc0b18f49787ca69a0d1d1b9d7a2d7184c550d3ab08e16eebe0ca9d` | `ec014bf818f778aec6a7448d050a1fa58ad2d60a8a32e78288a7364f84dff01d` | 3 / 1 |
| [consciousness/sections/core_equations.tex](../../consciousness/sections/core_equations.tex) | `f3ce1e4090b7e58e683af42d3f490f20b872e6b533ef726d7e5ecb4816c7fdd4` | `3e6a5c0f4d29abdb601ee0c0374b73ceb59b0b932b6e19bb401ba7d34a92bdbe` | 1 / 1 |
| [consciousness/sections_ja/core_equations_ja.tex](../../consciousness/sections_ja/core_equations_ja.tex) | `da2b58178df775453214a734501452e7bf8532bc557da0a7d2cea0840915c2a4` | `875a5022c2fec0548ae2f290e0f900b094a0805b4a12def420b48aeb5372cb09` | 1 / 1 |
| [consciousness/sections/pathologies_limits.tex](../../consciousness/sections/pathologies_limits.tex) | `ff3a8e7ff2823a29d38441244cd05ca770b93d7905bda6a1ea80e647654ba283` | `78e6e8441339ed9b6deeb983e503158d9192f3da7992315057f6c0f26d22a1bf` | 1 / 1 |
| [consciousness/sections_ja/pathologies_limits_ja.tex](../../consciousness/sections_ja/pathologies_limits_ja.tex) | `b3dc52de0bbbeb956b7b05541e2f00e2db487b14ecd6689b74c4977297c05c92` | `027d3470e3663b8dd6208ea2599d257c81075d6a5d3bb4e87c7a1e46603c85a3` | 1 / 1 |

## 4. I/J/Phi scope changes

S06でIを「再参照可能な形で沈殿したlogの密度」とする定義を保持。認知履歴をこのモデル量で表現するという読みを残し、実測密度・計数規則・校正を供給していないと明示した。

J_Iは局所field templateのflow slot、J_logはlog-referencingを記述する窓内のeffective flowとして説明。直接観測されたcognitive currentとせず、担体mapも両変数の同一性も追加していない。式中の両記号をmerge/renameしない。

Phiは既存projected-use guardの対象として保持し、local IFGT-inspired vocabulary/templateという文脈を整えた。meaning生成の機構を扱うCON-FINAL-029やCTのsame-quantityを扱う086は今回は未実装。新しい意味測定・kernel推定・operational mapはない。

## 5. IFGT template/version changes

S06の「IFGTの基本変数」「IFGTの最小関係」を「本稿がIFGTに着想を得て用いる局所語彙／有効template」へ修正。current IFGTのtau/J/F_Iと、Conのt/J_I/F/Kはsource-localな役割・signatureとして区別した。前者を導入した比較文は既存上流記号への参照であり、新しいCon notation familyを定義しない。

S07にも同じ一般変数帰属が反復されていたため、その一文をS06のsource/version区別に従うものへ変更。t→tau、J_I→J、F→F_Iの置換は一切行わない。局所templateのfield identity、time同一性、typed translationを供給しない。

## 6. Projection local-scope preservation

disproportionate influence/mass assignmentの定義はそのまま保持。「意図的選択を要求しない」という既存文も不変。定義だけで全具体例の単一typed operatorを指定するのではないという一文を両版に追加した。

gate/attention/residue/心理学的projectionを共通機構とする他の文脈はImplementation05の対象であり、今回その理論をrewriteしない。032のKEEPは033/034を達成済みとする意味ではない。

## 7. Libet provenance/attribution changes

S10冒頭で全実験記述をbackground summaryとし、個別一次資料anchor未確認を明記。Libetの設定・時間関係は本稿が取り上げる背景説明へ帰属させ、「よく知られた」ことを根拠の代用にしない。

「Libetが変換遅延を測った」を、本稿が背景の時間差をそのように再解釈する、と変更。Delta v/mu/tauを直接測定したというclaimを明示否定した。対応図式前・summaryの帰属も合わせ、背景実験によるモデル検証としない。具体的著者・年・装置・数値・データを追加せず、背景記述の史実精度を今回確定したとはしない。

## 8. Split-brain provenance/attribution changes

行動応答と言語報告の非対称を、ここで採用する背景記述として分離。新しいConsciousness観測でもlog flowの測定でもないと明示した。

log sedimentation/pathwayによる説明は本稿の解釈として帰属させ、「両実験のevidenceがlog条件を示した」という反復を修正した。経路モデルの実装・主体数・explicit consciousnessの必要十分性をこの段階で決着させない。

## 9. Rationalization provenance changes

「well-known / よく知られる」を背景例へ変更し、個別実験の出典確認を要することを明記。confabulation/rationalizationの語彙と例の説明上の役割は保持した。

背景現象と、slow-log completionによる解釈を区別。後者を実験が直接示したという反復帰属も本稿の解釈へ修正した。具体的患者・研究者・文献情報を想像で加えていない。059の機構全体、ego/selfの説明は後続に残る。

## 10. Neural background scope changes

S14冒頭とsummaryで身体・脳への依存をgeneric background premiseと明示し、固有fast/slow/logモデルの証拠・validationにしない。専用経験的引用anchorは要確認、前提だけからcarrier mapは得られないとした。

local fast/slowの具体的神経対応やnonlocal conscious regimeの強い読みは008/062等の後続Implementation04対象。背景前提の修正でそれらが自動解決したとは扱わない。

## 11. Closure-object scope changes

S06でC_ijは継承した節点対の閉包関係、C_f/C_s/Delta Cは比較用の有効層量と明示した。集約規則が供給されていないことを記し、同じCという字形を演算可能な同一性にしない。

既存の節点式、層差式、窓式、対応矢印を全て保持。Delta v/Delta Cの同じ条件という080、およびその図captionの実装修正は後続に残す。

## 12. Older VED PDE provenance handling

旧VED PDE直後に、旧VED／改訂Vol.4という歴史ラベルは本sourceの帰属表現として保持するが、正確な歴史的由来・版関係はrepository内で未解決、と両版に注記。

current IFGTの関連する持続式の所在だけを述べ、それをhistorical identityの証拠とはしない。PDE本体と旧ラベルは不変。082の「VED-grounded basis／VED的根拠」とnon-groundingの調整はImplementation05へ残す。この注記で上流auditを再開したりprovenanceを解決したりしていない。

## 13. Projected-use / future-calibration scope

S06/S07の「一般IFGT場との直接同一ではない」というguardを保持し、S06の導入を達成済みimplementationでなく提案的structural correspondenceへ明確化した。

S16のT_Phiは構造式で具体的測定量ではない、neural/linguistic/subjective reportとのmapは未完成、というguardを保持。そこにあるIFGT定義の帰属だけをCon-local IFGT-inspiredと明記した。future workを実装予定の約束や、既存測定規則に変えていない。

## 14. JA local-variant handling

JA S05のA_i、m_i、T_i等による既存3表示式は完全保持。直前にsource-localな現象論的近似であり、canonical IFGT equationsでも確立済み測定mapでもないと明記した。

ENにも対応する版差注記のみを追加。JA限定式・記号をENへ移植せず、両版の関係意図はOPENのままとした。canonical JAをworking draft扱いに格下げしていない。

## 15. Citation handling

既存文体の通常proseによる出典要確認注記を採用し、架空citation key、TODO引用、fake BibTeXは追加していない。

| Item | Before | After |
| --- | --- | --- |
| Consciousness refs.bib entries | 1（Intelligence） | 1、不変 |
| EN cite occurrences | 6 | 6、不変 |
| JA cite occurrences | 6 | 6、不変 |
| Unresolved dedicated anchors (frozen ledger) | 14 | 14、未取得 |
| New citations / bibliography entries | 0 | 0 |
| External research / retrieval | 0 | 0 |

Libet、split-brain、rationalization、generic neural背景の4anchorは未確認を明示。既存repository内の別枝に書誌metadataが存在することを、Con固有claimの検証へ流用しない。引用はvalidationでない。

## 16. EN/JA parity

§3の6組を、ターン開始時からの差分で全文比較した。targeted phrase検査に加え、変更文のsemantic strengthを手作業で照合した。

| Pair | Shared revised meaning | Intentional difference preserved |
| --- | --- | --- |
| formal_mapping | local I/J、template、typed mapなし、node/layer区別、由来OPEN | 旧PDEと図の配置順、既存表示式の空白差 |
| core_equations | S06に従うCon-local変数 | JA C(t)等の既存local式 |
| experimental_reinterpretation | 背景／解釈を分離、モデル変数を測定済みにしない | JAの分割displayと終端の次節案内 |
| non_localization | generic前提であって固有モデル証拠でない | 既存窓displayの分割 |
| torque_converter_attention | JA近似はlocal variant、版意図OPEN | weighted3式はJAにだけ保持 |
| pathologies_limits | 局所定義の測定mapは未完成 | T_PhiのEN inline／JA display |

literal translationやequation mergeはしていない。全稿のphenomenal/cross-scale claim-strength parityを完了したとは主張しない。

## 17. Equation immutability check

EN/JA entryの各21 inputから、equation/align/gather/multline/displaymathのstar variants、bracket、double-dollarを同じ抽出器で走査。変更前後に加えPhase01の保存raw block配列とも比較した。

| Check | Result |
| --- | --- |
| Displayed blocks before / after | 178 / 178 |
| EN / JA occurrences | 73 / 105、不変 |
| Whitespace-collapsed string families | 52、不変 |
| Raw block match | 178/178 byte-identical |
| Added / removed / changed displays | 0 / 0 / 0 |
| t vs tau、J_I/J_log、F/K | 式文字不変 |
| C_ij、C_f/C_s/Delta C、older PDE | 式文字不変 |
| JA weighted attention three equations | 不変・EN追加0 |
| Figure caption / section / label structure | 不変 |

Raw aggregate SHA-256（EN→JA entry順、各raw blockをLFで連結、UTF-8）:

`c3ef85df91bb704c3b482e2fc12574b4cf7c305a2bb6af04bbf81504b8ee6ebe`

Phase07と同じ連結規約。係数・sign・operator・index・functional formの変更も0。新しい数式・notation family・物理的同一性を導入していない。

## 18. OPEN preservation

30 CON-OPEN familiesと124 uncertaintyの凍結分類を変更していない。特に今回に接する006（I/Phi/flow observable）、013（neural carrier）、014/015（実験対応・出典）、017（closure translation）、020（上流橋）、021（版意図）、024（projection operator）、025（older PDE由来）、026（引用anchor）は未解決のまま。

全8 upstream bridgesもOPEN。ConのtとIFGT tau、node Cとlayer C、projected useとtyped translationを同一視しない。first-log/ownership、独立phenomenal criterion、window校正、measurement-loopの未解決も変化なし。

SERIOUS-001は既存final扱いのまま。source-level vicious circularityやglobal unfalsifiabilityを新たに認定していない。経験的ceiling CE-E1、phenomenal ceiling PCE2、tested/validated predictions0は不変。

## 19. Validation

| Check | Result |
| --- | --- |
| Frozen targets | PASS — 指定14件を§2に一度ずつ、action再判定なし |
| Scope / source diffs | PASS — 6 EN/JA pairsだけ、各変更を対象と照合。隣接claimは帰属scopeのみ |
| EN/JA semantic parity | PASS — 6組の改訂文の意味と未解決scopeが対応 |
| TeX inputs / environments | PASS — 21+21 input存在、environment nesting整合 |
| Equation immutability | PASS — 開始時およびPhase01 rawとの178/178一致 |
| Bibliography / citations | PASS — refs.bib hash、cite列・count不変。未解決key0、新entry0 |
| Figures / PDFs / code | PASS — 全既存図・PDF・codeのhash不変。figure refs12存在、caption不変 |
| Frozen audit / upstream / downstream | PASS — 旧監査と上流・下流sourceのhash不変 |
| Targeted attribution scan | PASS — Libet measured-model-delay、well-known導入、evidence-shows-log-conditionの対象反復を解釈へ変更 |
| OPEN / version scan | PASS — 旧PDE由来・計数規則・map・local variant未解決を明示 |
| Markdown / links / README | PASS — record21節、14 target ID、table/fence整合、relative links42件、READMEのCLOSED/FROZENとcore IN PROGRESSを確認 |
| git diff --check | PASS — source差分の末尾空白等0 |

開始時1452 existing filesのSHA-256を保存。最終変更は12 source+READMEの13 existing files、新規は本記録1。残る1439 existing filesのhash不変を確認した。statusの既存untracked directory集約表示だけに依存せずfile単位で比較した。

未修復の強いsource wordingは今回の対象外として明示的に残している。たとえばS06のsame-underlying-structure/grounded basis、S14のspecific neural correspondence、S10のfree-will／主体数／explicit consciousnessの実質条件は後続FINALの対象である。今回のscan PASSを、全稿のunsupported claimが0になったという意味にはしない。

PDFは意図的に未build。既存PDFはこのsource変更を未反映であり、現在の改訂sourceと同期済みとは扱わない。後続distribution phaseまで差を記録して保留する。図pixel/図PDFを変更せず、main PDFも同一hashである。

一時baseline/validatorはrepository外 `${TEMP_EVIDENCE_ROOT}/consciousness_impl01.6EHaIZ/` に置いた。repositoryにhelper/codeを追加していない。外部研究・文献取得・simulation・build・commit/pushなし。

## 20. Stop boundary

Implementation 01を完了し停止。Implementation 02以降はNOT STARTED。TCA/SSO/windowの必要十分性、phenomenal説明、neural carrier、cross-scale共通機構を今回修復完了としない。

Final dispositionsはFROZEN、Consciousness auditはCLOSED、core revisionはIN PROGRESS。旧PDE由来、版意図、citation anchor、operational map、phenomenal criterionをsource注記によって解決済みにしない。core revision CLOSEDやdistribution FRESHを宣言せず、PDF rebuildも行わない。

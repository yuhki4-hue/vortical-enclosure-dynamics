# Consciousness core revision — Implementation06

## 0. Status

- 実施日: 2026-09-10。
- Consciousness audit: CLOSED / Final dispositions: FROZEN（変更なし）。
- Implementation01–05: COMPLETE。Implementation06: COMPLETE。
- Consciousness core revision: IMPLEMENTATION COMPLETE。
- Independent final consistency check: NOT STARTED。
- Distribution PDFs: FRESH。freshnessは理論・神経機構・現象的同一性のvalidationではない。
- 対象はpresentation、図、caption、局所版差の注記、配布同期のみ。

## 1. Frozen authority

[最終凍結記録](07_final_audit_and_frozen_dispositions_v1.0_ja.md) §23–25・29・31を最上位とし、
[01](implementation_01_source_identity_provenance_version_scope_v0.1_ja.md)、
[02](implementation_02_core_window_sso_tca_loop_v0.1_ja.md)、
[03](implementation_03_qualia_measurement_self_time_v0.1_ja.md)、
[04](implementation_04_libet_splitbrain_neural_report_v0.1_ja.md)、
[05](implementation_05_crossscale_pde_projection_handoff_v0.1_ja.md) の本文をbaselineとして保持。
[README](README_ja.md) の上流VED/Bio audit/core CLOSEDは不変。

figure≠evidence、caption≠new authority、diagram correspondence≠equivalence theorem、visual label≠phenomenal criterion、EN/JA parity≠formula merge、fresh PDF≠validationを適用。
PDF skillのrender→visual verificationを使用。既存LuaLaTeX/latexmkとSVGを継続し、Poppler未配置のため既存Ghostscriptで画像化、pypdfで頁数・抽出・参照を補助確認した。外部取得なし。

## 2. Figure inventory

全6 familiesはPDF-onlyではなく編集可能なSVGを持つ。配置・色・曲線・箱・矢印経路を保持。
audit family番号と本文掲載番号は異なる。本文順はFIG01, FIG02, FIG06, FIG03, FIG04, FIG05（本文図1–6）。

| Family | EN assets | JA assets | SVG size / PDF MediaBox |
|---|---|---|---|
| FIG01 | EN SVG（公開版未収録: `../../consciousness/figures/figure1_sso_density.svg`） / [PDF](../../consciousness/figures/figure1_sso_density.pdf) | JA SVG（公開版未収録: `../../consciousness/figures_ja/figure1_sso_density_jp.svg`） / [PDF](../../consciousness/figures_ja/figure1_sso_density_jp.pdf) | 1600×950 / 1200×712.5 pt |
| FIG02 | EN SVG（公開版未収録: `../../consciousness/figures/figure2_tca.svg`） / [PDF](../../consciousness/figures/figure2_tca.pdf) | JA SVG（公開版未収録: `../../consciousness/figures_ja/figure2_tca_jp.svg`） / [PDF](../../consciousness/figures_ja/figure2_tca_jp.pdf) | 1600×950 / 1200×712.5 pt |
| FIG03 | EN SVG（公開版未収録: `../../consciousness/figures/figure3_nonclosure_window.svg`） / [PDF](../../consciousness/figures/figure3_nonclosure_window.pdf) | JA SVG（公開版未収録: `../../consciousness/figures_ja/figure3_nonclosure_window_jp.svg`） / [PDF](../../consciousness/figures_ja/figure3_nonclosure_window_jp.pdf) | 1600×1050 / 1200×787.5 pt |
| FIG04 | EN SVG（公開版未収録: `../../consciousness/figures/figure4_log_referencing_loop.svg`） / [PDF](../../consciousness/figures/figure4_log_referencing_loop.pdf) | JA SVG（公開版未収録: `../../consciousness/figures_ja/figure4_log_referencing_loop_jp.svg`） / [PDF](../../consciousness/figures_ja/figure4_log_referencing_loop_jp.pdf) | 1600×1050 / 1200×787.5 pt |
| FIG05 | EN SVG（公開版未収録: `../../consciousness/figures/figure5_qualia_boundary.svg`） / [PDF](../../consciousness/figures/figure5_qualia_boundary.pdf) | JA SVG（公開版未収録: `../../consciousness/figures_ja/figure5_qualia_boundary_jp.svg`） / [PDF](../../consciousness/figures_ja/figure5_qualia_boundary_jp.pdf) | 1600×1050 / 1200×787.5 pt |
| FIG06 | EN SVG（公開版未収録: `../../consciousness/figures/figure6_observation_regime.svg`） / [PDF](../../consciousness/figures/figure6_observation_regime.pdf) | JA SVG（公開版未収録: `../../consciousness/figures_ja/figure6_observation_regime_jp.svg`） / [PDF](../../consciousness/figures_ja/figure6_observation_regime_jp.pdf) | 1600×1050 / 1200×787.5 pt |

既存JA PNG6件はcanonical includeではないlocal exportsだが、古い図を残さないため同SVGから同pixel寸法で再生成。新asset形式は導入していない。

## 3. FIG01

subtitleをmodel-local proposalへ変更。中央は「proposed conscious access／意識的アクセス（提案）」、下段はmodel-level log-reference boundary。
captionはSSO構造図とし、現象的判定基準・較正済み神経領域とはしない。
speed/delay/viscosity・全boundsは保持。ENのτ∝とJAのτ∼は局所版差として保持し、同値を推定しない。
文字変更6件、式変更0。PASS WITH ADVISORY（τ版差）。

## 4. FIG02

subtitle/footer/captionをstructural analogy / effective modelへ同期。ego位置は現象論的対応の提案であり、主体生成・神経機構・較正済み測定ではない。
元図に独立したegoラベルはなく、新たな主体・担体を描いていない。全T/T_Phi式と回転的比喩を保持。

log-feedback注記とslow-layer説明の近接を解消するため、EN/JA下部の二つの注記のx位置を945へ移動。
EN旧x=1045/1045、JA旧x=1010/1045。y・文言・式・経路は不変。
文字変更4件、位置調整4 text nodes。PASS。

## 5. FIG03

title/subtitleをmodel-defined schematic parameter regionへ変更。EN「proposed access」、JA「アクセス（提案）」で同じ強度。
footer/captionに実証的分類器ではないこと、empirical thresholdと独立criterionがOPENであることを明示。
図のDelta-v-min下限と本文のzero-bound、図内のEN/JA large表記を保持。較正・統合はしない。
文字変更8件。PASS WITH ADVISORY（bound/source-version差）。

## 6. FIG04

subtitle/footer/captionを提案段階の機能的feedback loopへ同期。executed witnessやphenomenal persistenceの実証とはしない。
JA混在誤記「∇Φバイアスes next prediction」を「∇Φが次の予測を偏らせる」へ修正し、勾配記号は保持。
figureのPhi update、I changes、時間微分表示、六段階の流れは不変。captionで二つの対象と版選択OPENを明示。
footerのFast/Gate等はモデルnode名として両版で残す（数式・索引の統合なし）。
文字変更5件。PASS WITH ADVISORY（I/Phi update表現）。

## 7. FIG05

frontierをlocal phenomenological modelとして保持し、title/central labelはproposalを明示。
measurement boxと矢印説明はhypothesis／may transformへ変更。live/residue非同一性は保持。
captionは定義・提案的同定・現象的why-questionを分離し、捕捉不可能性の証明・validated measurement law・hard-problem解決を主張しない。
残余比較の研究方向を保持。SERIOUS-001とCON-CIR-019を図で解消しない。
英語Measurement hypothesisが箱を越えたためfont-sizeのみ27→20。箱・経路は不変。
文字変更19件。PASS。

## 8. FIG06

title/subtitle/中央説明をstructural comparison／proposed comparisonへ同期し、same condition、structural equivalence/isomorphismという読みを除去。

非数式の中央図式connectorだけをEN text index20／JA index22（zero-based）の「⟺」から「↔」へ変更。
178 theory displaysには含まれず、新しい理論演算子を定義しない。captionでcomparison onlyと指定。

下段二本の境界式に含まれる「⟺」は数式保存のため保持。
直近footerとcaptionで「模式的対置でありlogical biconditionalではない」と限定。数学的記号を黙って書き換えていない。
Delta-v/Delta-C定義、窓のbounds、JA「確率収束相」「古典相」は保持し、相名はsource-version labelと明記。
common units/invariants/typed translation/groundingは追加していない。
文字・connector変更15件（うちconnector2件）。PASS WITH ADVISORY（境界記号と相名の版差）。

## 9. Caption synchronization

| Family | TeX section pair | Classification | Final reading |
|---|---|---|---|
| FIG01 | sso | wording revision + version note | model architecture / proposed access |
| FIG02 | torque_converter_attention | wording revision | effective analogy / ego proposal |
| FIG03 | core_equations | parity revision + version note | schematic window / uncalibrated |
| FIG04 | dynamics_log_referencing | wording/parity + version note | functional loop / distinct I,Phi |
| FIG05 | qualia_boundary | wording revision | definition vs proposal / measurement hypothesis |
| FIG06 | formal_mapping | wording/parity + version note | comparison / no equivalence or grounding |

全12 figure environments/captionsを確認・修正。includegraphics、width、label、参照先は保持。
captionを新claim authorityやevidenceとして用いず、本文のfrozen weaker readingへ合わせた。

## 10. EN/JA local variants

| Frozen family | Handling | Status |
|---|---|---|
| JA weighted attention | A_i/m_i/T_i式とImpl01注記を保持。ENへcopyしない | OPEN VERSION INTENT |
| JA C(t) | local opening function、非測定量・非VED CというImpl03 guardを保持 | OPEN VERSION INTENT |
| JA non-state | 両版structural_interpretationに最小版注記を追加。JA displayはraw保存 | OPEN VERSION INTENT |
| FIG03 labels/bounds | 意味強度のみ同期、Delta-v-minと0を統合しない | OPEN VERSION INTENT |
| FIG06 phase names | JA相名保持、captionでsource-version labelへ限定 | OPEN VERSION INTENT |
| FIG04 I/Phi update | 二対象の区別と版差をcaptionで保持 | OPEN VERSION INTENT |
| IFGT t/tau/J/F | local effective template guardを保持、current IFGTと統合しない | OPEN |
| SSO six/three | 異なるlist・SSO readingを保持、七 documentary componentsも公理化しない | OPEN |

FIG01のτ∝/τ∼は追加観察としてOPEN-021へ保持。正準版の選択は行わない。

## 11. Figure asset changes

12 SVG→12 figure PDFsをrsvg-convert 2.62.1で再生成。page size、MediaBox、幾何学的図式、styleを保持。
57 text-content changes（55 wording/clerical + 2非数式connector）。別途位置調整4、font-size調整1。
既存JA PNG6件も同SVGから既存pixel sizeで再生成。PDFのraster編集やimage generationはしていない。
新しいrepo build system/codeは作成せず、一時commandで既存資産を再生成した。
全変更既存ファイルのSHA-256 before/afterを§23に記録する。

## 12. Equation immutability

| Check | Before | After | Result |
|---|---:|---:|---|
| EN canonical displays | 73 | 73 | raw 73/73 |
| JA canonical displays | 105 | 105 | raw 105/105 |
| Total | 178 | 178 | raw 178/178 |
| Equation families | 52 | 52 | unchanged |
| Phase01 inventory | 178 | 178 | raw 178/178 |

連結raw block SHA-256: c3ef85df91bb704c3b482e2fc12574b4cf7c305a2bb6af04bbf81504b8ee6ebe。
equation/align/gather/multline/displaymath、bracket、double-dollarをinclude順に抽出。
bounds/coefficient/sign/operator/index/function form、T/T_Phi、tau、Delta-v/Delta-C、旧PDE、JA独自displayは不変。
図中の数学的ラベルも保持。量に言及するprose subtitle/footerは比較の文言へ修正し、数式自体は変更していない。

## 13. Figure visual verification

元12PDFをGhostscriptで96dpi PNG化して全件目視し、修正・再生成後も全12件を確認。
FIG05文字fitとFIG02注記位置を修正して再確認。最終版に文字欠け、boxからのはみ出し、読めない重なり、font corruptionは認めない。

| Family | EN | JA | Advisory |
|---|---|---|---|
| FIG01 | PASS WITH ADVISORY | PASS WITH ADVISORY | τ版差 |
| FIG02 | PASS | PASS | なし |
| FIG03 | PASS WITH ADVISORY | PASS WITH ADVISORY | bound版差 |
| FIG04 | PASS WITH ADVISORY | PASS WITH ADVISORY | I/Phi版意図 |
| FIG05 | PASS | PASS | SERIOUS/circularityはQAで解消しない |
| FIG06 | PASS WITH ADVISORY | PASS WITH ADVISORY | 境界glyph・JA相名は限定注記付き保持 |

advisoryは数学版意図であり、文字欠落やbuild failureをPASS扱いしたものではない。

## 14. EN PDF build

既存fontspec対応LuaLaTeX route。cwd=consciousness。
latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=${TEMP_EVIDENCE_ROOT}/consciousness_impl06.PiCvsN/en main.tex
で成功（exit0、再実行後up-to-date）。88頁。

初回の長い複合語によるoverfullを減らすためmain.texにpresentation-onlyのemergencystretch=2emを追加。文言・displayは不変。
最終Overfull hboxは1件、1.1919pt（pathologies_limits summary、頁74）。全頁と該当頁の拡大確認で切れ・重なりはなく軽微なadvisory。
欠字・undefined reference/citationは0。補助生成物は一時outdir、確認済みPDFだけをmain.pdfへ反映。

## 15. JA PDF build

latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=${TEMP_EVIDENCE_ROOT}/consciousness_impl06.PiCvsN/ja main_ja.tex
で成功（exit0、再実行後up-to-date）。103頁。ltjsarticle/luatexjaの既存routeを保持。

Overfull0、欠字0、undefined reference/citation0。
caption default warning、数式fontの4.5→5pt substitution（最大0.5pt）は残るが、目視で破綻なし。
理論をtoolchain都合で改変していない。確認済みPDFだけをmain_ja.pdfへ反映。

## 16. PDF visual inspection

両PDF全頁（EN88/88、JA103/103、計191）を72dpi画像化し、全17 contact sheetsを確認。
図掲載頁は130dpi拡大確認も実施。FIG02の最終位置調整後は191頁を再renderし、既確認頁との差分がEN13、JA14だけであることをpixel hash比較で確認。この2頁を最終拡大画像で再目視した。

| Family | EN page / printed figure | JA page / printed figure |
|---|---|---|
| FIG01 | 8 / 1 | 8 / 1 |
| FIG02 | 13 / 2 | 14 / 2 |
| FIG03 | 29 / 4 | 33 / 4 |
| FIG04 | 38 / 5 | 44 / 5 |
| FIG05 | 47 / 6 | 54 / 6 |
| FIG06 | 22 / 3 | 24 / 3 |

欠落図、空白頁、壊れた参照、重大なoverfull、欠字、古いcaptionは認めない。scope・版注記・JA local displaysもrenderに存在。
参考文献頁EN88/JA103の既存1件を確認。citation key解決はdedicated empirical anchorsの成立ではない。

## 17. Distribution freshness

[EN distribution](../../consciousness/main.pdf): FRESH、88頁。
[JA distribution](../../consciousness/main_ja.pdf): FRESH、103頁。
flsは12 current figure PDFsを参照。既存JA local PNG exportsも更新済み。
一時build成果物とcopy先PDFのSHA一致を検証。freshnessは現行canonical distributionとfigure assetsの範囲であり、historical draftsをcurrent authorityへ昇格しない。

EN SHA-256: c41793d20e12a00d87ce4df5a7412276c6fb8cb7c15d7ff5536183339b179149。
JA SHA-256: 7a689be63157ff29004bb2c2c3c2c287ad8e2b11689ca93d908359d29169d9e1。
新experiment、simulation、citation、empirical mapはない。

## 18. Body / figure consistency

| Construct | Body authority preserved | Figure/caption ceiling |
|---|---|---|
| SSO | model premise・必要性はmodel-local・observer非主体 | proposed access architecture |
| window | formal region vs empirical classifier、FINAL004/075 SPLIT | schematic region、未較正、bound版差 |
| TCA | effective analogy vs neural mechanism、ego提案 | analogy/effective model、非測定量 |
| log loop | six-step loop vs continued consciousness仮説 | proposed architecture、I/Phi非同定 |
| qualia | local definition vs identity/explanation | proposed frontier、hard-problem limitation |
| measurement | live/residueカテゴリと変換仮説を分離 | may transform、比較経路を閉じない |
| neural/local | candidate carrier・背景依存≠validation | 図をneural mapへ変更しない |
| cross-scale | comparison≠typed translation≠grounding | structural comparison、equivalence未成立 |

本文の簡略なmodel vocabularyは既存canonical scope下で読み、captionで強い独立主張を再導入しない。
実装closureを妨げる新たなbody/figure contradictionは認めない。独立最終整合性監査の実施・代替ではない。

## 19. EN / JA parity

全21 modular pairsをliteral translationでなくclaim strength・scope・OPEN・local variant保持について確認。

| Pair | Sources | Focus | Result |
|---|---|---|---|
| 01 | [abstract EN](../../consciousness/sections/abstract.tex) / [JA](../../consciousness/sections_ja/abstract_ja.tex) | 定義／意識への提案／projected use | PASS |
| 02 | [introduction EN](../../consciousness/sections/introduction.tex) / [JA](../../consciousness/sections_ja/introduction_ja.tex) | canonical model-local scope | PASS |
| 03 | [intuitive_picture EN](../../consciousness/sections/intuitive_picture.tex) / [JA](../../consciousness/sections_ja/intuitive_picture_ja.tex) | 二層前提・機能割当 | PASS |
| 04 | [notation EN](../../consciousness/sections/notation.tex) / [JA](../../consciousness/sections_ja/notation_ja.tex) | 局所記号・tau非同定 | PASS |
| 05 | [sso EN](../../consciousness/sections/sso.tex) / [JA](../../consciousness/sections_ja/sso_ja.tex) | SSO二つの読み・六/三条件・図01 | PASS |
| 06 | [torque_converter_attention EN](../../consciousness/sections/torque_converter_attention.tex) / [JA](../../consciousness/sections_ja/torque_converter_attention_ja.tex) | 有効類比・ego提案・JA重み異形・図02 | PASS |
| 07 | [formal_mapping EN](../../consciousness/sections/formal_mapping.tex) / [JA](../../consciousness/sections_ja/formal_mapping_ja.tex) | provenance OPEN・projected use・比較・図06 | PASS WITH ADVISORY |
| 08 | [core_equations EN](../../consciousness/sections/core_equations.tex) / [JA](../../consciousness/sections_ja/core_equations_ja.tex) | formal window／empirical未較正・JA C(t)・図03 | PASS WITH ADVISORY |
| 09 | [structural_interpretation EN](../../consciousness/sections/structural_interpretation.tex) / [JA](../../consciousness/sections_ja/structural_interpretation_ja.tex) | state/regimeとJA non-state版意図を注記 | PASS WITH ADVISORY |
| 10 | [dynamics_log_referencing EN](../../consciousness/sections/dynamics_log_referencing.tex) / [JA](../../consciousness/sections_ja/dynamics_log_referencing_ja.tex) | 機能loop／維持仮説・I/Phi区別・図04 | PASS |
| 11 | [experimental_reinterpretation EN](../../consciousness/sections/experimental_reinterpretation.tex) / [JA](../../consciousness/sections_ja/experimental_reinterpretation_ja.tex) | 背景／再解釈／report非同定 | PASS |
| 12 | [qualia_boundary EN](../../consciousness/sections/qualia_boundary.tex) / [JA](../../consciousness/sections_ja/qualia_boundary_ja.tex) | 定義／同定提案／測定仮説・図05 | PASS |
| 13 | [opening_model EN](../../consciousness/sections/opening_model.tex) / [JA](../../consciousness/sections_ja/opening_model_ja.tex) | openingと自己地形はmodel-local | PASS |
| 14 | [measurement_collapse EN](../../consciousness/sections/measurement_collapse.tex) / [JA](../../consciousness/sections_ja/measurement_collapse_ja.tex) | live/residueと測定仮説・比較経路 | PASS |
| 15 | [non_localization EN](../../consciousness/sections/non_localization.tex) / [JA](../../consciousness/sections_ja/non_localization_ja.tex) | 候補担体・NCC非同定・神経的実証と区別 | PASS |
| 16 | [qualitative_predictions EN](../../consciousness/sections/qualitative_predictions.tex) / [JA](../../consciousness/sections_ja/qualitative_predictions_ja.tex) | 未検証の定性的方向・窓の模式性 | PASS |
| 17 | [pathologies_limits EN](../../consciousness/sections/pathologies_limits.tex) / [JA](../../consciousness/sections_ja/pathologies_limits_ja.tex) | 非診断的scope・計測未確立 | PASS |
| 18 | [relation_to_note EN](../../consciousness/sections/relation_to_note.tex) / [JA](../../consciousness/sections_ja/relation_to_note_ja.tex) | L1–L3 handoffはpedagogical | PASS |
| 19 | [discussion EN](../../consciousness/sections/discussion.tex) / [JA](../../consciousness/sections_ja/discussion_ja.tex) | 外部理論比較・自己・cross-scale scope | PASS |
| 20 | [conclusion EN](../../consciousness/sections/conclusion.tex) / [JA](../../consciousness/sections_ja/conclusion_ja.tex) | 構造／提案の分離・理論nonclosureの類比 | PASS |
| 21 | [correspondence_map EN](../../consciousness/sections/correspondence_map.tex) / [JA](../../consciousness/sections_ja/correspondence_map_ja.tex) | CT比較・共通量／共有機構を認定しない | PASS |

図・captionのsemantic strengthを一致させた。意図がOPENの数式、JA固有display、相名、更新対象は同一化しない。

## 20. Previous implementation preservation

caption以外のcanonical TeX baseline非空行4657件を全件保持。追加は両版non-state版注記とEN組版設定のみ。
各実装before snapshotと次段階baselineを比較し、追加された非空source行の存在も確認。

| Implementation | Added/revised lines retained |
|---|---:|
| 01 | 65/65 |
| 02 | 175/175 |
| 03 | 200/200 |
| 04 | 151/151 |
| 05 | 174/174 |

変更sourceはcaption6組、版注記structural_interpretation1組、EN main組版設定（計15 TeX）。
旧implementation recordsとfinal auditはhash不変。root README・上流/downstream source・BibTeX・simulation/codeに変更なし。

## 21. OPEN preservation

CON-OPEN-001–030を全件継続。全30行を持つ凍結authorityはhash不変。実装完了は研究OPENの閉鎖ではない。

| OPEN IDs | Preserved boundary |
|---|---|
| 001–006 | window criterion、rate/tau/mu/TCA/I-J-Phi operationalization |
| 007–012 | phenomenal criterion、live/residue、first-log、own logs、subject/system、report drift |
| 013–016 | neural carrier、Libet/split-brain provenance/test、altered-state classifier |
| 017–020 | rate/closure、CT、four-layer/Intelligence、IFGT/upstream eight bridges |
| 021–025 | version intent、SSO lists、gate origin、projection、older PDE provenance |
| 026–030 | citation anchors、note/L1–L3、theory/object analogy、protocol、self continuity |

特に図01/03/04/06の版差、JA non-state、旧PDE provenanceはOPEN。
SERIOUS-001: RETAINED SERIOUS CANDIDATE。
CON-CIR-019: C6 evidence-loop risk RETAINED。
source-level vicious circularity、global unfalsifiability、generated phenomenal subject、independent phenomenal criterion、typed translationの成立を新たに認定しない。

## 22. Core revision implementation status

Impl01–05 COMPLETE、6図scope同期（版差はadvisory）、21組parity確認、2PDF build・画像確認、178display保存、frozen disposition非変更、OPEN非解決を確認。

Consciousness core revision: IMPLEMENTATION COMPLETE。
Independent final consistency check: NOT STARTED。
audit CLOSEDの再判定ではなく、既に凍結された修正の実装完了である。

## 23. Validation

| Validation | Result |
|---|---|
| Families/assets/captions | 6/6 families、12/12 figure PDFs、12/12 captions確認・修正 |
| Labels | 57変更（55 wording/clerical + 2 diagram connectors） |
| EN/JA | 21/21 source pairs、6/6 figure pairs |
| Equations | 178/178 raw match、52 families、Phase01とも一致 |
| Prior body | 4657 baseline lines、01–05追加行すべて保持 |
| Authority/OPEN | final/01–05 record hash不変、30 OPEN・8 upstream bridges保持 |
| Distribution | EN88/JA103、191頁画像確認、12図掲載頁拡大確認 |
| References/citations | include/figure/label/cite key解決、BibTeX不変 |
| Changed-file boundary | 48既存files + 本record新規1、他1409files hash不変 |
| Source/code boundary | 15 TeX + 12 SVG + 12 figure PDF + 6既存PNG + 2main PDF + README + recordのみ |
| External/new content | 外部研究・citation追加・new equation/theory/bridge・simulationなし |
| Git | git diff --check PASS。既存dirty worktree保持、commit/pushなし |

snapshotは ${TEMP_EVIDENCE_ROOT}/consciousness_impl06.PiCvsN/before.json（repo既存1457files）。
helper・render・build logは同temp directoryに置き、repoに新codeを追加していない。
git status --shortは226行のdirty worktreeを示す（audit directoryは既にuntracked）。このターンの境界はgitのM全件でなく開始時hashとの比較。詳細statusも一時検証結果に保存。

### Existing changed files: SHA-256 before / after

caption/source・全asset・READMEを列挙。本recordは新規であり自己hash再帰を避けて表外とする。

| Path | Before SHA-256 | After SHA-256 |
|---|---|---|
| `consciousness/figures_ja/figure1_sso_density_jp.pdf` | `1ce552d3cd1e74bce175500618a2fc560e2d8f4953c557a17aee6f8857efd7ce` | `f1ae63fa64e940f9d77281e089f989db24df5bf754b0e7b0642acf61e4c318a7` |
| `consciousness/figures_ja/figure1_sso_density_jp.png` | `e0417299d697c0a5304600258f4d5790933dc1dc5749f881fa3cb58cb7809422` | `81d3b57abbe1b3412cbe9ddda346e7f64409ba92992f0fc9c143a2fbf5d48f7a` |
| `consciousness/figures_ja/figure1_sso_density_jp.svg` | `5424ae6751563d8a41a3115d39878cccce50d7ff2b3746411af875c60c7d3659` | `470e26fc6b4088c4cc3648f0fbdb3e96b9ad4e2688ebc4e4ddfb228e5421bc71` |
| `consciousness/figures_ja/figure2_tca_jp.pdf` | `acd418b3395b5a18dbffcdb5771fc809af7685a7dbc8230fcc183c09a5cd14d5` | `32a80b54d3dcc8ad10627f1c93e1d4ea6d02e55e32117b0a9b9264dd7970d420` |
| `consciousness/figures_ja/figure2_tca_jp.png` | `bc6b39ccc25301f268b3af2c8a60327509c5ef7a5e7d476f2408a0a01e547993` | `757d6e4ed52bbf5a8d2a8583619a0acd66cf8ba04abcead2ec0b3d3dda513385` |
| `consciousness/figures_ja/figure2_tca_jp.svg` | `003054a6143243263b4324ecb4fadcc6b96610dc45abb0560813b1e5dd066023` | `e6adecb40604da43ecc668516ed7828cd398029f580a12803fa0201251704d4e` |
| `consciousness/figures_ja/figure3_nonclosure_window_jp.pdf` | `863f91f201536a5b164f8c49bd319df1b979c241492094f6bba490677c931060` | `d36ec70cb8824357cf6a671d7243fa08dd1abbd42bbdd5e92d2722746378f89d` |
| `consciousness/figures_ja/figure3_nonclosure_window_jp.png` | `764de66baccb135ba7ee19acbca2f875afe43dc76f8712638144e07e0a3605c5` | `50bb4ef32a55e2b991b904fddd578a2461bf5b3016284191a89eb4eb8f36e854` |
| `consciousness/figures_ja/figure3_nonclosure_window_jp.svg` | `fd53fd9d348b4853e526053b52d418ce41105ee93fa86caa91225a1af1fce7c0` | `4805ddd67e4034768a0f7ae7326559b4836d17603a9dbbd0b73395593ca7a981` |
| `consciousness/figures_ja/figure4_log_referencing_loop_jp.pdf` | `df90b16dbe666a65668cb0065ea2119c6dd598eda39524655a7c221da494e4c0` | `5dd532c97c0660a482f9496e2fcf9af1f9ecff092a13767552f7248f6ee2c451` |
| `consciousness/figures_ja/figure4_log_referencing_loop_jp.png` | `27aa019abd6a31bf56d02ffcb039a7a95c5809fc9ef1c22889a3519bb9a84153` | `73183e39a8bdf26e28291b75810a793e6401be5d5a45d057d64c27e6124f0b35` |
| `consciousness/figures_ja/figure4_log_referencing_loop_jp.svg` | `f10794cb99c18536620b5be46299515ba4358dd60868ac4070a85ee5b4ce62b0` | `e38c07e49ef2f330e654a21c724a9c7029c215766cfbfeff031e77d0a369c999` |
| `consciousness/figures_ja/figure5_qualia_boundary_jp.pdf` | `46006d53b9e83edfc60fd5a5de0ca9d37d4c6813208cbb644eab337b91bc4545` | `55e235872d3fe11c0bd90c367f94882698c6287b450eac7e0ea0e807a04e3cf3` |
| `consciousness/figures_ja/figure5_qualia_boundary_jp.png` | `b19d22147e2516357dce58f41b275b786ea6309efdfc1a53eff197d68883f636` | `c0c51454d8416018e6e071c21810e364ed573e4c999849c61abb57e6ee0fa794` |
| `consciousness/figures_ja/figure5_qualia_boundary_jp.svg` | `1ac7d4ebf8ddeb54919cca3f98989449b82ad7b3321d1836996fa8d252adc651` | `d8cb654767b0d91f1d9616eaa8d14bbbe4a0647bdddaf201410151c6c13759ba` |
| `consciousness/figures_ja/figure6_observation_regime_jp.pdf` | `e8089ecb513d0b4039c94e3b3edda78721840233e5e2f51b0d5f14c67ae57df1` | `8213fad4c1d58b7a28af50661d3abdcd5c7640ca854a612ed2c60703dbcc98f2` |
| `consciousness/figures_ja/figure6_observation_regime_jp.png` | `58929daf253ff78c181b85c72f8ce58ddb3779d0000eeb4cf58d9f22895fc257` | `7fb8d7a1349be755b5d5ad3a0c0cb0b3ca1f3216a433a3ec06afa5cbe8c8dcb1` |
| `consciousness/figures_ja/figure6_observation_regime_jp.svg` | `f36a33208e8c8b1051e107ef3106b6a72430a425193b53f30301aa0b84f349d5` | `87c5d22f6f357a4e25df5ac61f6b7300cd5d7c35283e656f623dd8b2a7c8976a` |
| `consciousness/figures/figure1_sso_density.pdf` | `13d87f1410ace924029bd4ef7d46c6a76c1cc47f171ede0f5436fda4b0812eb2` | `18450be2e0f06ff1ad2331c688b8f86700d48576fd24b599a980508f1e191660` |
| `consciousness/figures/figure1_sso_density.svg` | `ba08aba53b7da98c2118fd9efef28a3d4b8ceffd118cd9235bf6b7ab7202867c` | `b3b38f822d2c4f37b85027e0e6c9965cddf443ea037571ce651f2c292ec97671` |
| `consciousness/figures/figure2_tca.pdf` | `be3d301fd2b5caf9c787d6a3feb6f8f20a2bd2b9a63b3fb813ad6b4aa7167cb9` | `bb4f840ea3f0821a8212a9b784915eee06c90e89488b75205d8fb2ee1778b400` |
| `consciousness/figures/figure2_tca.svg` | `583f9de4bd48de2ad3f36a876c6c18237831409bd2c70409458b409c1566324a` | `0b38f7bfa394fc073a5573a352fa350d59cd48e5d3b3d54378569f498f7cde51` |
| `consciousness/figures/figure3_nonclosure_window.pdf` | `5726267a3a6a99e44ee31603e58ff13233f5df1bb3b409118ab3521496484f15` | `f8928763f4543fe3842ca9c75f50a600b133f23ff9bc4c856801fd4157752ca8` |
| `consciousness/figures/figure3_nonclosure_window.svg` | `c3f52ddb4ab42bf9706b555a32e453de9c972c776e307fea96d5acd498e695a1` | `8124b27156a9cca0a2374c857487ff019e9cda180795805682cb13e843a0f4e1` |
| `consciousness/figures/figure4_log_referencing_loop.pdf` | `d2e22483b977339ecdd319d7e507d7a479283a7738d55b495f812a6311c00a6b` | `5bf9ac6d39121864a3e68eaac771be97647c16b4c0d46d2948b7154a6c66ab0a` |
| `consciousness/figures/figure4_log_referencing_loop.svg` | `e17fc3d3620026909d3f8de4b8f69ec6cb5fabbb5634b55ec509764f16bc9d1a` | `3d60fbe68ab2cd72e835d0b8712dab36a6970c85deb72b4761fdea16f77fb0f7` |
| `consciousness/figures/figure5_qualia_boundary.pdf` | `d290d0228a8ebbabb8b5e71ad294eca63b76c03ad3f7563c051d6743ec68ea04` | `3e3228411cfcd7fc8d3985afc9be3ad5270b684f79a51a453a302a3a41cb30f9` |
| `consciousness/figures/figure5_qualia_boundary.svg` | `e0e770f58bba82691116b824060dfc0d5a1e2c517b2de467fc37097ba98d6cb0` | `3e9ef2307728cf5d2dfe5fae762e3fff8405bcc7e7e53fd09879803f9eeb3461` |
| `consciousness/figures/figure6_observation_regime.pdf` | `186b42c15c62ce3a746377eb96fd240bf80e4f663a5389118198890d8f6e2317` | `acf5db214b46418aac8158659b6f0a3faf5d505d49ca657d7fa45ca823e83cfd` |
| `consciousness/figures/figure6_observation_regime.svg` | `0c1a3ed1486704b9a26db4468850f03c6dc138deca0bf7cae18f05ca00e2746b` | `296e1280e69e266efe46757671d27dfeff5b714b587b3297db4c1835bfba5473` |
| `consciousness/main_ja.pdf` | `dcadebf39d11013eabf3d936d396fb73fbc86be5c1028152b7c0e2244b0faed3` | `7a689be63157ff29004bb2c2c3c2c287ad8e2b11689ca93d908359d29169d9e1` |
| `consciousness/main.pdf` | `1c0aa1b06a0323582ae20aef4bd95aa9ee297116742bccef9d66070835245ee3` | `c41793d20e12a00d87ce4df5a7412276c6fb8cb7c15d7ff5536183339b179149` |
| `consciousness/main.tex` | `8f9f5af5442991543066a9e159caf4909e0016cb4888a4cacbbb89785ea33e5d` | `8b13abe4f28f1a907f504073773394294f7b1cba448b230f0d9dff8902023526` |
| `consciousness/sections_ja/core_equations_ja.tex` | `8d199e63c7a827792acaa91f18448d80dc8336481c312e2f42b66075fc5eba11` | `e89977c365369689d6b7025dbd8bec462bf9bcd3861f006087bd02f884fce835` |
| `consciousness/sections_ja/dynamics_log_referencing_ja.tex` | `d1cf2379dd2b18913f5e87ab29affe885bcd598cc3dc1836ff0d1b59025816ee` | `7829206a68a84fa6da0219ac79e3654220640ce3e40a528e41296d3db13aa512` |
| `consciousness/sections_ja/formal_mapping_ja.tex` | `0204b594acbf1d21ace99d71288c695a101b4274ad69bd3b3335113ef12b4597` | `f6aa0c67dc54f5fd88a8d51b90600f23a9d26ab04e04101d0a98f9ee520a6634` |
| `consciousness/sections_ja/qualia_boundary_ja.tex` | `2dce474da9f65be33f97ac3c8f29ca4f1e577c07a4492d8b09c1c190ae0ac20f` | `f7fc6d97a7436b5f58cbfb016dd3d4e1c29204e47401523bc2eeeb819d2b69c8` |
| `consciousness/sections_ja/sso_ja.tex` | `2623e82a7db0257b690db157088519e86000e7fd7013d8457e95181ee8d5fa85` | `0d271160f1b00c0f6d05e23449780900ed015646f3f24feb0aa214ad7eaef16d` |
| `consciousness/sections_ja/structural_interpretation_ja.tex` | `deb4920264deb5046d02942346c0b7ed8ab417ed17672c3b98c5d850887e08db` | `2b8a557496d772838550315d3c7c3383b58588819d1c14c70d3344f6de9c3c14` |
| `consciousness/sections_ja/torque_converter_attention_ja.tex` | `03d3af030df798399cd4811ff6ba113e5b4599cda304547dd0d24ea86a63233f` | `2da1f4ebc8e225aaefb8ec03a3debdacbf07ff25ae096264676f6251a737ca78` |
| `consciousness/sections/core_equations.tex` | `4119599fff01c9da02f5af7dc474cfa77564519953ad74492b199b58629e20f6` | `0ce5f6a78581300938d5c34875836749c519852958a5209b87e56293e0a3417c` |
| `consciousness/sections/dynamics_log_referencing.tex` | `9ea9ecd8f7d20edc5a199d8e1f0d499b7ad257f333dea6744f61a99fcb76dc54` | `8cd0b1caa48bc355241956e03db6f4379921f9a4faafc380a273d5430fa5f2ba` |
| `consciousness/sections/formal_mapping.tex` | `4da2e1e8d690fc17a932e2a4fd62bc8d4f51d1631fa69a88f7022e4f4aa2aea6` | `b4fd07c87613deacc934e14710041a85528c320d37a85f714c9687a9230008f2` |
| `consciousness/sections/qualia_boundary.tex` | `189ce81c7dae73f27cf787d4c59fa3015115bb8ed47cf1543a23dbbdc8699c58` | `55e3f0d36d3ec052e5625d44508230206176b728131f40ea6eb1ea31849e4eac` |
| `consciousness/sections/sso.tex` | `4ec3dd59bf49eb3606e8450c10f89fc5f6ffc2024c2e76b6759ac435645d4342` | `4445704b82a5810e72049bdbc40a4256e8fb4e9b7be2fa618ae5a5c9b8ba34c8` |
| `consciousness/sections/structural_interpretation.tex` | `f546a51f0e6539fea33b0c6fe5afe9bc9bd5de1883dc884c557821e51acefdf4` | `b987cc90e54e32e8901d31ba75bb528554a07e69199495e2a04cbd70a9500e23` |
| `consciousness/sections/torque_converter_attention.tex` | `ed3d1035ab82b57795928751b2dbbc3936c83450f127402078d8b6e9bb682c66` | `401255fe9cace7c42eff9241d01c3e6b16d5764ee95b8b274aacdbfd4a1b454c` |
| `notes/consciousness_audit/README_ja.md` | `7b33521567468cc5d4bdf7e6104b88a64e5bcb3497508bc34becaf8b81651a91` | `8a5e114abe873e2eb464e5c07e7a4f8746de83fca17da8161477240a5efc4cea` |

## 24. Stop boundary

Implementation06で停止する。Independent final consistency checkは行わない。
追加理論・新しい経験的判定・上流監査再開・downstream改稿・commit/pushは行っていない。
研究OPENと版差は保持し、見た目の同期で解決したことにしない。

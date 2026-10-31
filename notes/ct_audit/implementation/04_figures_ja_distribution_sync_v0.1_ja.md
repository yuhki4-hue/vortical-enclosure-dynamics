# CT Implementation 04 — figures / JA working / distribution synchronization v0.1

## 0. Status

実施日: 2026-09-11。Implementation01/03後のcanonical ENへpresentationを同期した。

```text
CT audit: CLOSED
Final dispositions: FROZEN
Implementation 01: COMPLETE
Implementation 02: COMPLETE
Implementation 03: COMPLETE
Implementation 04 figures / JA / distribution synchronization: COMPLETE
Independent post-implementation consistency audit: NOT STARTED
CT core/source revision: IMPLEMENTED / PENDING INDEPENDENT CONSISTENCY AUDIT
Equation revision: REVIEW COMPLETE / NO EQUATION CHANGE IMPLEMENTED
Global equation-change requirement: OPEN
Canonical EN distribution: FRESH
JA authority: WORKING / noncanonical
```

FRESHはImplementation01/03/04 sourceとの同期であり、validationではない。
今回の保護・表示検査はこの実装のvalidationに限る。独立post-implementation consistency auditを実施したとはしない。

## 1. Authority / boundary

- [Phase07 frozen authority](../07_final_audit_and_frozen_dispositions_v1.0_ja.md)：FIGFINAL001–003、JAFINAL、FINAL019/044 DOWNGRADE、FINAL016 OPEN、22研究OPEN。
- [Implementation01](01_canonical_en_scope_revision_record_v0.1_ja.md)：本文のscope・role split。
- [Implementation02](02_formal_open_equation_review_v0.1_ja.md)：6 OPEN式の未解決事項。
- [Implementation03](03_formal_clarification_implementation_v0.1_ja.md)：未採用のformal assumptions、template/typing/authorityのscope。
- [Audit README](../README_ja.md)、[canonical EN entry](../../../conceptual-topography/main.tex)、[JA working](../../../conceptual-topography/conceptual_topography_ja.md)。

Final dispositionsはKEEP7 / REVISE9 / DOWNGRADE17 / SPLIT14 / RETIRE0 / OPEN1を変更しない。
図≠証拠、caption≠新claim authority、JA同期≠canonical昇格、fresh PDF≠new validationを保持する。

## 2. Task-start preservation / source inventory

task-startに.gitを除くrepository全1472ファイル（ignored/untrackedを含む）のSHA-256を取得した。
開始時git statusは241行（M236、untracked directory entries5）。既存dirty差分を本task差分とは見なさない。
一時検証資料は `${TEMP_EVIDENCE_ROOT}/ct_impl04.0vW43a/` に限定：
baseline.json、texts.json、edits.json、validate.py、build/、page-01〜22.png、detail-12.png。
新たなhelper sourceをrepositoryへ追加しない。

CT内は3 PNGのみで、editable SVG/TikZ/plot/code sourceは所在確認できなかった。
repository内filename検索でも同名のeditable sourceを確認できなかったため、imagegenスキルのbuilt-in editを使用。
3図を修正前・修正後に目視し、元の構成、色、等高線、矢印、既存数式を保持するpromptとした。
生成画像の細部はraster再生成のため画素不変とは言わない。数式labelの内容は目視比較し、
FIG003の指定されたbare J→J_I以外に変更がないことを確認した。

## 3. Files changed

| File | Task-local change |
| --- | --- |
| [fig1](../../../conceptual-topography/figures/fig1_potential_geometry.png) | RELABEL。構成・数式label保持。1536×1024→1536×1024。 |
| [fig2](../../../conceptual-topography/figures/fig2_token_field_coupling.png) | RELABEL。hypothesis/non-executedを明示。1536×1024→1536×1024。 |
| [fig3](../../../conceptual-topography/figures/fig3_minimal_recursive_loop.png) | SYMBOL FIX + RELABEL。1254×1254→1254×1254。 |
| [intuitive_picture.tex](../../../conceptual-topography/sections/intuitive_picture.tex) | FIG001 captionのみ。includegraphics幅・path・label不変。 |
| [core_equations.tex](../../../conceptual-topography/sections/core_equations.tex) | FIG002/003 captionsのみ。本文、式、includegraphics幅・path・label不変。 |
| [main.tex](../../../conceptual-topography/main.tex) | 図が「同期待ち」という古いstatusを、同期済みschematic scopeへ更新しただけ。 |
| [JA working](../../../conceptual-topography/conceptual_topography_ja.md) | 全12対応節のclaim strength/formal scope。旧数学・固有working解釈保持。 |
| [main.pdf](../../../conceptual-topography/main.pdf) | canonical EN distribution再build・視覚検査後の置換。 |
| [CT README](../../../conceptual-topography/README.md) | authority、freshness、FIG003修正済み、未解決境界を簡潔に同期。 |
| [audit README](../README_ja.md) | 別立てimplementation statusと本記録link。closed audit履歴を保持。 |
| 本記録 | 新規。 |

既存ファイルの内容変更は10、新規は本記録1。build一時生成物はrepo外。
既存repo内の補助buildファイルは最終SHA比較で変更なし。BibTeX sourceは不変。
他10 EN sectionsはtask-startとbyte-identical。2変更sectionsもfigure環境を除いた本文はbyte-identical。
Phase00–07とImplementation01–03、upstream/downstreamは全ファイルhash一致。

## 4. FIG001 — potential geometry

Final action: RELABEL / CAPTION REVISE。Visual: PASS。

| Old label | New label |
| --- | --- |
| Information potential | Schematic information potential |
| thought trajectory J_I | illustrative path for J_I |
| （なし） | proposed thought representation（直下の補足） |

Phi(x,tau)、x1/x2、Phi軸、2箇所のgradient≈0、negative gradient、
3箇所のJ_I、basin A/B・ridge・conceptual boundaryと既存経路・矢印を保持。
pathはillustration、flow fieldは別object、thoughtは提案的認知解釈とcaptionで分離。
測定・再構成された認知pathではない。

## 5. FIG002 — token-field coupling

Final action: RELABEL / CAPTION REVISE。Visual: PASS。

| Old label | New label |
| --- | --- |
| Before reuse | Before reuse (schematic) |
| After repeated reuse | Hypothesized after reuse |
| deepened basin / reinforced gradient | proposed deepening / proposed reinforcement |
| repeated token-field coupling (reuse) | token-field coupling hypothesis (reuse) |
| lower traversal cost | proposed lower traversal cost |
| more easily attracted to the basin | hypothesized easier entry |
| (reinforced) | (hypothesized) |
| acts locally on the field | proposed local action |
| (pulls flow downhill) | (directional bias) |
| trajectory of information flow | flow; path illustrated |
| coupling term: | schematic coupling term: |
| （なし） | Qualitative hypothesis; not simulation output |

2 panelの浅い／深い井戸、token dots、矢印、ell_i、J_I、negative-gradient表示、
lambda・sum/index・dot・gradientを含む既存coupling formulaを保持。
token vectorization、pairing、Lの数学種類は図で補っていない。
深まりの対比は仮説の例示であり、実行witnessでも式から導出された結果でもない。

## 6. FIG003 — minimal recursive loop

Final action: SYMBOL FIX / RELABEL / CAPTION REVISE。Visual: PASS。

| Location / old wording | Implemented wording |
| --- | --- |
| 左node、下部legend、boxed chainのbare J | J_I（capital I subscript）、3/3箇所 |
| Minimal recursive loop | Proposed recursive loop |
| （central補足なし） | model-level schematic |
| Unidirectional causality (irreversible) | Schematic directional ordering |
| Flow induces new residuals | Proposed residual feedback |
| Residual re-emerges | Proposed residual renewal |
| Transition along gradient · Flow, search, integration, and transmission | Directional flow · Proposed search, integration, and transmission |
| Specification of concept attractors | Proposed concept-attractor interpretation |

Delta/C/I/Phi/tauと5 node、既存arrow topology、central irreversible orderingは保持。
J→J_IはPhase07が指定した局所CT flowのpresentation整合のみで、上流bare Jとの同一性ではない。
新しい数学関係・node・arrow・dynamicsを追加していない。

## 7. Caption synchronization / exact resulting captions

3/3 figure環境を照合した。caption内のinline数式は文字列・出現順とも不変。
既存float指定[t]、画像幅0.92/0.95/0.82 linewidth、path、labelも保持する。

### Entry figure-scope status

```tex
figures and their captions are scoped as conceptual schematics, not measured
trajectories, executed dynamics, or evidence for the proposed interpretations.
```

### intuitive_picture.tex

```tex
  Schematic conceptual landscape as information-potential geometry.
  The surface illustrates the model potential $\Phi(x,\tau)$.
  Basins depict the local concept definition where $\nabla\Phi \approx 0$.
  The drawn path is an illustrative representation associated with the flow field $J_I$, not the field itself or a measured thought path.
  Its cognitive reading is proposed; ridges illustrate model-level conceptual boundaries.
```

### core_equations.tex

```tex
  Schematic token--field coupling hypothesis, not simulation output.
  Discrete tokens $\ell_i$ are not assigned intrinsic meaning; their proposed local coupling to $\nabla\Phi$ motivates the illustration.
  Deepening and lower traversal cost for paths associated with $J_I$ are hypothesized effects, not executed or derived results.
  The expression $\lambda \sum_i \ell_i \cdot \nabla\Phi$ remains schematic: token realization and pairing are unresolved.
```

### core_equations.tex

```tex
  Proposed recursive loop in the VED$\times$IFGT vocabulary.
  The schematic sequence
  $\Delta \to C \to I \to \Phi \to J_I \to \Delta$
  links residual asymmetry $\Delta$, closure $C$, information density $I$, potential structure $\Phi$, and information flow $J_I$ within the proposed feedback architecture.
  The ordering parameter $\tau$ expresses the model's irreversible-ordering premise; arrows are not a proof of causality or an executed dynamical witness.
```

## 8. JA working synchronization / section crosswalk

JAのprose置換132操作とclerical整理を行った。操作数はclaim数ではなく編集単位。
12/12対応節を確認。式をENへ合わせず、解釈の強度を同期した。

| Working section | Main synchronization / frozen claim families |
| --- | --- |
| scope / 概要 | WORKING明示、Master帰属未定、source reuse≠typed derivation、landscape局所命名、flow/path/thought分離。001–005/008/011–019/028/039/043/048。 |
| §1 introduction | established solution classes/確立・導出を候補的分類へ。concept・understanding局所定義とsubject非要求を保持。002/006/007/012/046。 |
| §2 intuitive picture | 理解感≠threshold定義、geometry≠experience生成、meaning/reentryをworking解釈として保持、通信は比較仮説。008–010/014/017/045。 |
| §3 formal mapping | activity較正なし、tau ordering≠experience、Cmax hard wallでない、Qの同型を類比へ。003–005/011/019/040/045。 |
| §4 core equations | balance template、force近似scope、barrier非不到達証明、coupling typing未定、Phi-star version保留、positivity各負担の分離。013/015/016/018/019/047。 |
| §5 structural interpretation | 解クラス未証明、depth/width/curvature比較、drift機構仮説、語彙の選択集合≠確率分布。020–022。 |
| §6 dynamics | feedback≠自己維持証明、bootstrap OPEN、忘却/想起対応、insight geometry/cognition/felt suddenness分離。023–027。 |
| §7 multiscale | same dynamics未成立、shared terrain条件付き仮説、制度attractor類比とdepth/stability仮説を分離、知性の局所命名。028–031/039。 |
| §8 limits | negative scope保持、failure regimeは定性的非診断的仮説、神経map将来、quantitative gaps。032–036/045。 |
| §9 note | CT内教育的比較を保持、note exact artifact OPEN、現行companion≠旧note identity、相互検証なし。037/038。 |
| §10 discussion | groundingは再利用・動機、distributional semanticsとprediction errorは比較、未指定maps等保持。036/041/042/048。 |
| §11 conclusion | positivity・same dynamics・制度・一般知性・同一場／同一方程式の強い読みを再導入しない。019/039/043/044/048。 |

## 9. Mandatory JA targets / retained divergences

| Target | Implemented result | Remaining version/authority boundary |
| --- | --- | --- |
| positivity | generic含意を確立した帰結として採用せず、局所静止・追加条件付き再分化を明記。innovation保証なし。 | 旧inlineのI>0、gradient≠0、flow≠0はraw保存し否定的なscope文で扱う。f/range/PDE保存を補わない。 |
| barrier | effective resistance、reciprocal divergence≠dynamic inaccessibility/invariant proof。 | 係数符号・Cの正規化・boundaryは採用しない。 |
| same equation | shared-field/equation identityをheuristic motif・projected-regime比較へ。 | JA-only CLM044はworking-only。ENへのpromotionなし、typed map/common state space OPEN。 |
| grounding | 最小公理からのCT導出を主張せず、上流語彙の動機・比較へ。 | Master exact artifact/version、typed inheritance OPEN。 |
| Phi-star | 旧JAの「一意でも静的でもない…再形成され続ける」を引用として保持。ENのnot necessarilyとの差を明示。 | CT-FINAL-016 OPEN。limit mode・moving target・fixed/driven条件を選ばない。 |
| meaning / reentry | 低コスト再入と経験される意味の固有内容をworking interpretationとして保持。 | semantic ontology・phenomenal criterionへ昇格せず、ENへの追加なし。 |
| Q | 量子化という名称と連続／離散の類比、no-quantum guardを保持。 | isomorphism/map未定。 |
| vocabulary | set選択と分布的proseを分離。 | Sの計算・計測・確率分布を定義しない。 |
| underclosure | 「過開放」のJA名称保持、非診断的regime仮説に限定。 | literal translationやphase-name統一はしない。 |
| document structure | JA12対応heading、広い言語媒体の例示、note表を保持。 | JA14 displayとEN12 displayは各々保存。line-by-line parityは主張しない。 |

canonical JA entryはNOT LOCATEDのまま。main_ja.tex/JA PDF新設・buildなし。
版注・変更履歴はworking scope同期として追記し、旧draft 0.1 / 2026-04の来歴を残した。

## 10. SERIOUS / OPEN preservation

SERIOUS001 understanding/felt ease、002 insight/suddenness、003 institution/stabilityは全てRETAIN。
JAで低コスト定義を理解感の証拠にせず、topologyをfelt suddennessの説明にせず、
institution stabilityをdepthの定義とその独立証拠の双方にしない。
これは文言上の分離であり、独立criterionの供給でも解消判定でもない。

CT-OPEN-001–022を全てOPENとして保持。OPEN-022のlabel/caption実装を行っても研究familyは閉じない。
EQF002/004/008/009/010/013はPhase07のOPENおよびImplementation03のclarified statusを維持。
CT-FINAL-016 OPEN、global equation-change requirement OPEN。
token typing、convergence、positive preservation、semantic/phenomenal/social maps、source/version、
prediction executionをpresentation同期で解消していない。

## 11. Mathematical immutability

task-start raw抽出とafterをfileごとに比較した。display環境はequation/align/gather/multline/
displaymath/eqnarray/alignat/flalignとstarred版、bracket/dollar displayを対象とし、inlineはdisplayを除去して別抽出。
全ての数学文字列（空白・delimiter・式内labelを含む）を順序込みで比較した。

| Protected scope | Before | After | Raw match |
| --- | ---: | ---: | --- |
| canonical EN display blocks | 12 | 12 | 12/12 |
| EN relation occurrences / EQF | 14 / 14 | 14 / 14 | 全14 relationを含む12 blocks完全一致 |
| EN inline math | 202 | 202 | 202/202 |
| EN label/ref/eqref等commands | 45 | 45 | 45/45 |
| EN citation commands / cited keys | 6 / 7 | 6 / 7 | 完全一致、7 keysすべて解決 |
| JA working display blocks | 14 | 14 | 14/14 |
| JA working inline math | 158 | 158 | 158/158 |
| BibTeX entries | 8 | 8 | file hash不変 |

数式・記号・係数・sign・limit・inequality・macroは追加削除変更なし。
図のbare J→J_Iは3箇所のpresentation例外として分離し、一般的な「全symbol画素不変」とは報告しない。

Raw-list digestはUTF-8 JSON（ensure_ascii=False、separators=(',',':')）、snapshot text manifest順。
ENファイル順: main.tex, sections/structural_interpretation.tex, sections/dynamics.tex, sections/discussion.tex, sections/core_equations.tex, sections/conclusion.tex, sections/abstract.tex, sections/introduction.tex, sections/relation_to_note.tex, sections/intuitive_picture.tex, sections/formal_mapping.tex, sections/multiscale.tex, sections/pathologies.tex。

| Raw list | Before = after SHA-256 |
| --- | --- |
| EN display | `585d017c63351a87743f75c97da18efb961506c07438e82a1b3d41bff61978fb` |
| EN inline | `151c210e8a80e14142e65e7b683e9aab243656af691c2a07cf05a15a0ea9ad69` |
| EN labels/refs | `d277b0218dc09ebabc04ed3796061978df1e2640b8f29f302d4bd13f290277df` |
| JA display | `9407ed9e1a2ab0e3feda8b4d9466019f4166a13708c0f3f96e84028cd64a0f76` |
| JA inline | `23f5319d5441055e3311a0b5786976b3a103ef7a232eacc8a1a1573e6106e4bb` |

## 12. EN build route / result

既存CT READMEのlatexmk -pdf routeを使用。新build systemは追加しない。
一時output-directoryだけを外部tempへ指定し、検査済みPDFを既存distribution pathへcopyした。

```bash
# cwd: conceptual-topography
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=${TEMP_EVIDENCE_ROOT}/ct_impl04.0vW43a/build main.tex
```

Exit status: 0。pdfLaTeX 3 passes / BibTeX 1 pass。全targets up-to-dateで完了。
EN main.pdf: 22 pages / A4 / 4,926,349 bytes。
SHA-256: `c16f737651b79cfbafcf75353ee7642633e8847485dc64aa87db4cd2bd22acbc`。
copy先と視覚検査対象のhashは一致。旧配布版19頁→22頁はImplementation01/03 proseを初めて反映した改頁を含む。
JA workingはEN build inputではなく、JA PDFを作っていない。

最終log: missing glyph 0、undefined citation/reference 0、fatal error 0。
既存BibTeXのempty institution warnings 5（IFGT、VED_vol1–4）はそのまま記録し、refs.bibを変更しない。
Underfull hbox 7（formal mapping表6 / structural table1）、overfull hbox 1（note比較表13.09097pt）。
初回passの未解決reference警告は最終passで解消。TeXの数式や本文をcompileのために変更していない。

## 13. PDF visual inspection

pdfスキルに従いbundled Popplerで22頁すべてをPNG化して目視した。
system PATHにPopplerはなかったがbundled runtimeを使用し、install/web取得は不要だった。

```bash
${LOCAL_TOOL_BIN}/pdftoppm -r 85 -png ${TEMP_EVIDENCE_ROOT}/ct_impl04.0vW43a/build/main.pdf ${TEMP_EVIDENCE_ROOT}/ct_impl04.0vW43a/page
# FIG003 subscriptはpage12を150dpiでも再確認
```

| Pages | Checked content | Result |
| --- | --- | --- |
| 1–4 | title、scope、abstract、目次、page breaks | PASS WITH ADVISORY：2/4頁は既存newpageと長いabstract/目次の続きによる余白大。完全白紙ではない。 |
| 5–8 | introduction、FIG001、caption、thought-field区別、potential式 | PASS |
| 9–10 | variable表、formal scope、balance/force/source/barrier式 | PASS WITH ADVISORY：表内のjustify間隔・hyphenationあり、重なりや切れなし。 |
| 11 | FIG002、仮説label、caption、coupling式 | PASS。小文字は元の紙面幅を保持。元PNGでも確認。 |
| 12 | FIG003全3箇所J_I、caption、sedimentation式 | PASS。150dpi追加確認。 |
| 13–16 | concept/understanding/positivity、class表、vocabulary、dynamics、multi-scale表 | PASS |
| 17–20 | social、limits、note表、discussion、conclusion冒頭 | PASS WITH ADVISORY：note表は約13pt右へ出るが紙面内で全列読取可。既存romanized note語彙のchinden末尾caret様表記も保存。今回のcaption変更由来ではなく、範囲外本文を変更しない。 |
| 21–22 | conclusion、references、最終頁 | PASS WITH ADVISORY：22頁はbibliography継続1項目のみ。既存paginationを保持し、欠落なし。 |

全22頁に内容があり、欠落図・切れた数式・caption overlap・font corruptionなし。
3 figure XObjectsは7/11/12頁。pypdf/PillowでRGB復号画素をcurrent PNGと比較し、
3/3がexact match。TeXのincludegraphics pathも全てcurrent assetへ解決。stale figureの残留なし。
links/refsのsource解決と最終logを併用し、視覚検査をtext extractionだけで代用しなかった。
表示検査総合: PASS WITH ADVISORIES（既存の軽微な組版警告と疎な継続頁、内容読取を妨げない）。

## 14. Distribution freshness

Canonical EN distribution: FRESH relative to Implementation01/03/04 source。
current source + current figures + successful build + visual inspection + embedded pixel matchを満たす。
source変更後に未buildのcanonical inputsはない。BibTeX/citation keysを更新せず、全7引用は解決する。
JA WORKINGの独自内容はEN PDFのauthorityへ移送しない。
FRESH ≠ empirical validation、FRESH ≠ equation OPEN resolution。

## 15. Evidence / correspondence ceiling preservation

CE2 / SE2 / COG2 / PCE2を維持。
COR3 / SM3 / CM3 / PM1 / SOM3 / X3を維持。
Operational maps / empirical datasets / tested predictions / validated predictions: 0 / 0 / 0 / 0。
神経・行動・社会データ、simulation、new theory、new bridge、new metric/proxy/protocolは追加していない。
imagegenは既存schematicのpresentation編集であり、data生成・証拠生成ではない。
external web researchなし。既存文献・citation keysを追加・変更しない。

## 16. Asset/source hash changes

SHA-256。本記録自身のhashは自己参照を避け、最終検証出力で管理する。
旧audit/implementation recordsを改訂しない。

| File | Before | After |
| --- | --- | --- |
| `conceptual-topography/main.pdf` | `cbd54b5c08ae9b1b2dcad89ecc3b273eaf7080ca28485bada6538962e00f72fd` | `c16f737651b79cfbafcf75353ee7642633e8847485dc64aa87db4cd2bd22acbc` |
| `conceptual-topography/conceptual_topography_ja.md` | `9d503e349f581c5fced73618f8a694c590994ee5e4a9a23ad1d4f440fd2a4d95` | `af46d519d5ef160a91e57a3f209a4d7920338039a5771df97dc259fd36758e7f` |
| `conceptual-topography/main.tex` | `45ed3f9e2a90bec0a6ebd6a87d24a2bf57eff7e2d299f8488adb51480ce3ccaa` | `cb6f76d2b931055ccc4cf3c21b60e12794bbdf0c08ffde82feb0a885c774e937` |
| `conceptual-topography/README.md` | `94ee6445f5f7ed7b8c0ba54dc1c40d223469e79edee072e86c07ad9362d39034` | `f4f18045c6ea5462d13fedfcd0634eecda816fc4351eb89c8897f1df7ded7c57` |
| `conceptual-topography/sections/core_equations.tex` | `d7855efd6d5d673fc1302dbe81d9e7683da3a7b3e111a9e25c37880bd4ccb7dc` | `42d2c0096c989634e72a5c938402fa780f2b3c064d73f0ffc5617b4c2bb9d996` |
| `conceptual-topography/sections/intuitive_picture.tex` | `3421db396d03be718ad4cd12d5d6447d9fb0fd5d568decec688c960993d61a8c` | `b0b4b932a9902de8bb4005d52e799a5c22cd56b4b1a00d24f62fa5937e4580d6` |
| `conceptual-topography/figures/fig3_minimal_recursive_loop.png` | `8014f6559a21f2a7a22d0b9818147ddac738d48f64fbd0e539de5f92a25fe046` | `9ba24fe33d5b8b38ad3d849b6ab2d68c6c0dde3a9c25d58e1e23788ef3c6bf8c` |
| `conceptual-topography/figures/fig2_token_field_coupling.png` | `40e8d60efde93886b476a9e0e67e20e0769ce495f427c4a46f95955129e8118e` | `79665dac190a39763c5e5d31ca7407b5ef79d8473642e24bc604216bb555b5ca` |
| `conceptual-topography/figures/fig1_potential_geometry.png` | `46350f3a8fee18e628b62a31347f5ff92dcbfcac80196f0ac6ae132bb9d701b7` | `2eb338e358fa6878c8926eeb8c6bd38c8d5b30dc1475144edfa6b4b7f3a81ec4` |
| `notes/ct_audit/README_ja.md` | `a864d9110ba380f29e5789b7fed5a524380a5ca364918c3a2706acad6bdbbc6a` | `ce0805bdbd797b1d4ca6b3cf221a12250bdddc8b9bb34608b3cb92d7d68a12af` |

## 17. Validation / task-local diff

- 3/3 figure actions実装、全3 caption同期、FIG003 bare J alignment 3/3。
- 12/12 JA対応節をreview、強いpositivity/barrier/same-equation/groundingを限定、固有meaning/reentry/Phi-star version差保持。
- EN数学12 displays/14 relations/14 EQF、202 inline、45 references/labels、citation keys完全一致。
- JA数学14 displays/158 inline完全一致。canonical JA新設なし。
- Implementation01/03本文はfigure環境を除き保持。entryは古いfigure statusの2行のみ同期。
- Phase00–07、Implementation01–03、refs.bib、upstream/downstreamはtask-start全file hashes一致。
- 22研究OPEN、6 EQF OPEN、CT-FINAL-016、SERIOUS3 RETAIN、frozen dispositionsを保持。
- EN build exit0、22/22頁視覚確認、3/3embedded PNG画素一致、references解決。
- repository-local helper追加なし。task-start1472→1473 files（本記録1件）。
- 変更10既存files＋新規1。git statusの既存dirty変更を今回の編集として数えない。
- git diff --check: PASS。untracked本記録も別途whitespace/Markdown links/fencesを検査。
- git status --short: 246行（M241、untracked directory entries5）。task-startから新たにdirtyになったtracked pathはJA/PNG3/PDFの5、他変更は既存dirty path上へのtask-local修正。
- commit/pushなし。

## 18. Imagegen skill / reproducible prompt record

built-in imagegen editを3 calls使用（CLI/API fallbackなし）。元PNGをview_imageで確認後に編集し、
生成outputを指定された既存figure pathへcopyした。余分な新しいasset familyやeditable-sourceの新設なし。
以下は実際の最終prompt。厳密な画素再現を保証するseedではなく、編集範囲の記録である。

### FIG001

```text
Use case: text-localization. Image 1 is the edit target, an existing scientific schematic. Change ONLY these labels, keeping composition, surface geometry, contours, all arrows, colors, aspect ratio, axes, every mathematical symbol and all other text unchanged. Replace top-left "Information potential" with "Schematic information potential". Replace bottom "thought trajectory J_I" with "illustrative path for J_I" (retain mathematical J with subscript capital I). Directly below this label add small plain text "proposed thought representation". Keep Phi(x,tau), both gradient-Phi approximately zero formulas, negative gradient Phi, x_1, x_2, Phi axis, and the two standalone J_I labels exactly. Do not draw new geometry, arrows, equations or numbers. Same academic serif style and readable typography. No redesign.
```

### FIG002

```text
Use case: text-localization. Image 1 is edit target existing two-panel scientific schematic. Preserve both surfaces, their shallow/deep contrast, all contour lines, colors, all arrows and arrowheads, exact composition/aspect, token dots, every existing mathematical symbol and the bottom coupling formula exactly. ONLY replace text as follows: "Before reuse" -> "Before reuse (schematic)"; "After repeated reuse" -> "Hypothesized after reuse"; "deepened basin" -> "proposed deepening"; "reinforced gradient" -> "proposed reinforcement"; center "repeated token-field coupling (reuse)" -> "token-field coupling hypothesis (reuse)"; right "lower traversal cost" -> "proposed lower traversal cost"; right-bottom "more easily attracted to the basin" -> "hypothesized easier entry"; under right negative-gradient formula "(reinforced)" -> "(hypothesized)"; legend "acts locally on the field" -> "proposed local action"; legend "(pulls flow downhill)" -> "(directional bias)"; legend "trajectory of information flow" -> "flow; path illustrated"; bottom "coupling term:" -> "schematic coupling term:". Keep all J_I, ell_i, minus-gradient-Phi signs, lambda sum over i ell_i dot gradient Phi absolutely unchanged. Add small plain-text line in white lower margin: "Qualitative hypothesis; not simulation output". Use same serif typography, fit labels without overlapping. Do not add any math or arrows. No aesthetic redesign.
```

### FIG003

```text
Use case: text-localization. Image 1 is edit target an existing five-node recursive-loop schematic. Preserve every node, arrow, contour, icon, color, arrangement and aspect ratio. Change ONLY these exact textual labels: change all THREE bare J symbols (left node title, bottom legend, and bottom boxed chain) to J_I, with capital I rendered as a proper subscript; leave Delta C I Phi tau all unchanged. Replace "Minimal recursive loop" with "Proposed recursive loop". Replace "Unidirectional causality (irreversible)" with "Schematic directional ordering". Replace "Flow induces new residuals" with "Proposed residual feedback". Replace "Residual re-emerges (new asymmetry)" with "Proposed residual renewal (new asymmetry)". Keep central tau (irreversible ordering) but add small text directly underneath the central loop title "model-level schematic". In left node supporting text replace "Transition along gradient · Flow, search, integration, and transmission" with "Directional flow · Proposed search, integration, and transmission". In Phi node replace "Specification of concept attractors" with "Proposed concept-attractor interpretation". Retain all other symbols and text. No new nodes, arrows, equations, variables, measurements, or quantitative structure. Same serif scientific typography, no clipping/overlap, no redesign.
```

## 19. Stop boundary

Implementation04完了で停止。
independent post-implementation consistency auditには進まない。
equation decision、formal OPEN resolution、research OPEN closure、SERIOUS解消判定も行わない。
監査CLOSED/FROZENとsource実装済み・独立監査待ちを区別したまま引き渡す。

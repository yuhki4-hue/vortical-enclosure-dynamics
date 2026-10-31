# CT Phase 00 — dependency / inheritance / source authority record v0.1

## 0. Status

CT audit: IN PROGRESS。Phase 00: COMPLETE。Phase 01以降: NOT STARTED。
実施日: 2026-09-10。対象は作業ツリーの現在内容であり、git HEADだけではない。

本記録はsource locatorとsourceが使う関係語を固定する。成立・真偽・数学的／意味的／認知的／経験的妥当性・循環性・証拠十分性・dispositionは未判定。以下の「定義」「導出」「機構」「同じ」はsource wordingの分類であり監査の認定ではない。

## 1. Scope

対象branchは [conceptual-topography](../../conceptual-topography/README.md)。branchは理論directoryの意味であり、git branchの切替は行わない。本文全12 modular sections、entry、JA working MD全589行、README、bibliography、3画像、配布PDF、ignored build artifactsも調査した。全repositoryのpath・明示参照を検索し、周辺sourceはCTへの接点に限って読む。

保持するguard:

- source reuse ≠ derivation、same notation ≠ same object。
- formal geometry ≠ semantic ontology、semantic representation ≠ cognitive mechanism。
- cognitive interpretation ≠ phenomenal consciousness。
- Consciousness citation ≠ CT validation、Intelligence reuse ≠ CT established result。
- navigation order ≠ proof order ≠ generation order。

監査層T0=formal、T1=representational/semantic、T2=cognitive/functional、T3=phenomenal/subjective。sourceのL0/L1（シリーズ）、L1/L3（note/formal）と別物。T3は主理論層と仮定しないが、§2.4・§6.4等に実際の経験語があるためinventoryする。

## 2. Canonical source authority

| Authority item | 根拠 | Phase00で固定する扱い |
|---|---|---|
| EN current entry | CT README Repository Structure / Build、main.tex:100–117のinput、root READMEの配布リンク | main.texと12 included TeXをCANONICALとする |
| JA current canonical entry | main_ja.tex、sections_ja、JA PDFはbranchにもCT名の別配布先にも未発見 | NOT LOCATED。対等なcanonical JAを捏造しない |
| JA working source | conceptual_topography_ja.md:7 draft 2026-04、580–589「draft 0.1」「英語TeXから生成」「本MDを作業台として修正し、TeXに反映」 | WORKING。現存JA対応内容を全節比較するがENと同格のbuild authorityではない |
| PDF | root README.md:165およびCT build route | DISTRIBUTION。TeXの代わりに意味authorityにしない |
| Git/documentary history | git logのb2199b9（2026-05-19 closure alignment）、d56016b（同日README）、[CHANGELOG](../../CHANGELOG.md):139–147 | 現在ENのprojection/barrier変更を記す文書史。JAへの自動反映とは扱わない |
| Master Variable Table v2.1 | README、entry、S02/S04に準拠宣言 | その名の独立canonical table/version locatorは未固定。Intelligence Part IIのmaster tableを同じものと推定しない |
| Companion note | S10にL1/L3対応、Consciousness noteのCPU/GPU | exact note title/path/versionは指定なし。JA working MDをそのL1 noteと同定しない |

参照用の外部directory locator（すべてrepository内）:

| Alias | 実ファイル | Authority role |
|---|---|---|
| UP-VED | [Vol1](../../paper/vol1/main.tex)、[Vol2](../../paper/vol2/main.tex)、[Vol3](../../paper/vol3/main.tex)、[Vol4](../../paper/vol4/main.tex) | 現在entry。CTのbibタイトルとの歴史的同一性は別問題 |
| UP-IFGT | [entry](../../Information-Field-Geometry-Theory/main.tex)、[fundamental dynamics](../../Information-Field-Geometry-Theory/sections/fundamental_dynamics.tex)、[unified equation](../../Information-Field-Geometry-Theory/sections/unified_equation.tex) | 現在のJ/tau/source decompositionとOPEN bridge scopeを確認 |
| UP-BIO | [entry](../../bio-ifgt/main.tex)、[audit status](../bio_ifgt_audit/README_ja.md) | CT自身にBioの名指し継承は未発見。周辺比較から逆輸入しない |
| CON | [entry EN](../../consciousness/main.tex)、[JA](../../consciousness/main_ja.tex)、[status](../consciousness_audit/README_ja.md)、[frozen record](../consciousness_audit/07_final_audit_and_frozen_dispositions_v1.0_ja.md) | audit/core CLOSEDをcurrent READMEで確認。CT validationには使わない |
| CON-MAP | [EN map](../../consciousness/sections/correspondence_map.tex)、[JA map](../../consciousness/sections_ja/correspondence_map_ja.tex) | downstream comparison vocabularyの現状 |
| CON-SSO | [EN](../../consciousness/sections/sso.tex)、[JA](../../consciousness/sections_ja/sso_ja.tex) | CT §2.4への比較 |
| CON-TCA | [EN](../../consciousness/sections/torque_converter_attention.tex)、[JA](../../consciousness/sections_ja/torque_converter_attention_ja.tex) | CT §4.2の式引用 |
| CON-LOOP | [EN](../../consciousness/sections/dynamics_log_referencing.tex)、[JA](../../consciousness/sections_ja/dynamics_log_referencing_ja.tex) | CT §6.1、§4.4への比較 |
| CON-SCOPE | [EN](../../consciousness/sections/formal_mapping.tex)、[JA](../../consciousness/sections_ja/formal_mapping_ja.tex) | four-window / projection guard |
| INT1 | [README](../../intelligence-part1/README.md)、[entry](../../intelligence-part1/main.tex)、[JA](../../intelligence-part1/main_ja.tex) | CT名指し接続は検索対象内で未発見。一般の知性語をCT引用に数えない |
| INT2 | [README](../../intelligence-part2/README.md)、[JA entry](../../intelligence-part2/main_ja.tex)、[EN draft entry](../../intelligence-part2/main.tex) | READMEはJA primary / EN draftと明記 |
| INT2-I | [JA introduction](../../intelligence-part2/sections/00_introduction_ja.tex) | 表現層104行、tree226行、同位接続243行 |
| INT2-B | [JA homology](../../intelligence-part2/appendices/appendix_b_homology_ja.tex) | CT列15–26行。冒頭は提案的比較guard |
| INT2-MD | [combined](../../intelligence-part2/source_md/intelligence_part2_combined_ja.md)、[appendices](../../intelligence-part2/source_md/intelligence_part2_appendices_ja.md) | 下流working source。current TeXと別authority |
| NAV | [reading paths](../../docs/navigation/reading_paths.md)、[concept map](../../docs/navigation/concept_map.md)、[concept traps](../../docs/navigation/concept_traps.md) | SUPPORTING navigation。LLMのCT読みはconcept_traps:225–233 |
| UP-AUDIT | [VED audit](../ved_equation_audit/README_ja.md) | VED/Bio closed statusを維持し再開しない |

## 3. Source tree

開始時のCT directoryはhidden/ignoredを含め28 files。次表は全ファイルを列挙する。CANONICAL textはentry+12 sections=13、bibliographyはSUPPORTINGに別計上。HISTORICAL standalone fileは0、WORKINGは1。履歴はgit/CHANGELOGにあり、main_arxiv.texはREADME上の生成可能性であって現存ファイルではない。

| File | Class | SHA-256（開始時） |
|---|---|---|
| .DS_Store（公開版未収録: `../../conceptual-topography/.DS_Store`） | NONCANONICAL | eae983b1bb19ec5863c49caa24c102596eb03887e84b24574d941a383eab28d4 |
| [.gitignore](../../conceptual-topography/.gitignore) | SUPPORTING | f5a2121bd6f552beb83267c33aab69b4acabb0b1e2fb3e1ab16d484666f9076f |
| [README.md](../../conceptual-topography/README.md) | SUPPORTING | c7dcceedf47c9902f8e9c4049cb20fb0c87a0c96592e1cc8350224a9ecaa3ea8 |
| [conceptual_topography_ja.md](../../conceptual-topography/conceptual_topography_ja.md) | WORKING | 9d503e349f581c5fced73618f8a694c590994ee5e4a9a23ad1d4f440fd2a4d95 |
| [figures/fig1_potential_geometry.png](../../conceptual-topography/figures/fig1_potential_geometry.png) | FIGURE | 46350f3a8fee18e628b62a31347f5ff92dcbfcac80196f0ac6ae132bb9d701b7 |
| [figures/fig2_token_field_coupling.png](../../conceptual-topography/figures/fig2_token_field_coupling.png) | FIGURE | 40e8d60efde93886b476a9e0e67e20e0769ce495f427c4a46f95955129e8118e |
| [figures/fig3_minimal_recursive_loop.png](../../conceptual-topography/figures/fig3_minimal_recursive_loop.png) | FIGURE | 8014f6559a21f2a7a22d0b9818147ddac738d48f64fbd0e539de5f92a25fe046 |
| main.aux（公開版未収録: `../../conceptual-topography/main.aux`） | NONCANONICAL | 7867ba717b508e8ad2ace1532cfe289b587b5bbcfa260f119a48ca61dc4aff4a |
| main.bbl（公開版未収録: `../../conceptual-topography/main.bbl`） | NONCANONICAL | 3abe241153560d6c6cdffff4b9ed7c61ae0db8fc59c9341499033175ad3e3330 |
| main.blg（公開版未収録: `../../conceptual-topography/main.blg`） | NONCANONICAL | 777710124f7d1a152da734b585e39aadfcca5abc02758e88fd34c620840cfc35 |
| main.log（公開版未収録: `../../conceptual-topography/main.log`） | NONCANONICAL | 303a64f97757454834e794b90a79040d522e3d6f083d964b02d9c7eeecb7d962 |
| main.out（公開版未収録: `../../conceptual-topography/main.out`） | NONCANONICAL | e33ee18b3b85ca510d284c903e19cdc15286e98f9b05708c6b6be8479c8dfe54 |
| [main.pdf](../../conceptual-topography/main.pdf) | DISTRIBUTION | cbd54b5c08ae9b1b2dcad89ecc3b273eaf7080ca28485bada6538962e00f72fd |
| [main.tex](../../conceptual-topography/main.tex) | CANONICAL | b82ea57b3ce2037eac50bd4bce4d95e30be535f01c459ded5a8a04cae2215035 |
| main.toc（公開版未収録: `../../conceptual-topography/main.toc`） | NONCANONICAL | 0c23031991d9518dc8f6562251d48dcdbc61ff9857d7936eb1c77f5d4906f6c9 |
| [refs.bib](../../conceptual-topography/refs.bib) | SUPPORTING | 54c7a17b14d07443356266c39a17dd1c82b3a56a421e2b69ad9ec00bff0fb715 |
| [sections/abstract.tex](../../conceptual-topography/sections/abstract.tex) | CANONICAL | 474f497c8fbeeb2a8ad77e6795f2635c4a78e96fdb5ecfe6ee1f1c4afc1b8035 |
| [sections/conclusion.tex](../../conceptual-topography/sections/conclusion.tex) | CANONICAL | 2e132a816ffc6058a0192b7db614a41003261d32d25037faed6f7fa3afb54b73 |
| [sections/core_equations.tex](../../conceptual-topography/sections/core_equations.tex) | CANONICAL | a08b520602716c5ea62ccfcb9912e1d77a4e2f3bcf12e1ff3711f2a2b3a32039 |
| [sections/discussion.tex](../../conceptual-topography/sections/discussion.tex) | CANONICAL | 6b7b337d42e58554bd9ea613f0c55457f29811e8880bbb22069beb52cbcdbf4d |
| [sections/dynamics.tex](../../conceptual-topography/sections/dynamics.tex) | CANONICAL | ceac29c3208e0bb5578b33e62a3ce9515dcad890d570085491a95d493073d590 |
| [sections/formal_mapping.tex](../../conceptual-topography/sections/formal_mapping.tex) | CANONICAL | 76294b3896715a58b61666c22155b2e7bdfe5f93d259e2395a31d7b7949b6cec |
| [sections/introduction.tex](../../conceptual-topography/sections/introduction.tex) | CANONICAL | b975ffe1a65e199b1650cfb717326033cc0b431adc56abff7e77e62c05bc692b |
| [sections/intuitive_picture.tex](../../conceptual-topography/sections/intuitive_picture.tex) | CANONICAL | c9be1ce2d882cc3744ec8b5ceec0e9590cf4e15dcc2baf9305560be0afc55914 |
| [sections/multiscale.tex](../../conceptual-topography/sections/multiscale.tex) | CANONICAL | 87fdb936f024280524a4a9165e4950e3420f1302491b4f7718bf060e5e4171fa |
| [sections/pathologies.tex](../../conceptual-topography/sections/pathologies.tex) | CANONICAL | 02c8a078abf741ea8bad884ba1b3e9bf2f4fd736ae3d507f5e9c16e16ab2b6b0 |
| [sections/relation_to_note.tex](../../conceptual-topography/sections/relation_to_note.tex) | CANONICAL | 47e218c28fc47596439980fcbc177f0e34b7481c68cd63bd801156d32fc79ab5 |
| [sections/structural_interpretation.tex](../../conceptual-topography/sections/structural_interpretation.tex) | CANONICAL | a0c6ea617ebe4031a3327ee847abd29a910d943a284c919a8fcb8e7407021e59 |

branch外の接点は§2のpath registryが範囲。Consciousness/Intelligence本文はCTから見たDOWNSTREAM/reciprocal source、root README・CHANGELOG・navigation・upstream auditはSUPPORTING。CT固有コード、notebook、dataset、SVG/TikZ/editable figure source、別draft archive、別JA entryは未発見。「ない」は今回探索範囲の結果であり外部の不存在ではない。

## 4. EN / JA entry structure

S番号はinclude/navigation順でありproof順ではない。JA欄は同一working MDのheading/行でありincludeされない。canonical entry 1、EN input 12（abstract1+番号付き本文11）、JA input 0、JA対応heading 12。欠落JA heading 0だがcanonical JA module pairは0。

| Source ID | EN | JA | Canonical? | Included? | Notes |
|---|---|---|---|---|---|
| CT-S00 | [main.tex](../../conceptual-topography/main.tex) | [working MD](../../conceptual-topography/conceptual_topography_ja.md):1–23,580–589 | EN YES / JA NO | entry / JA no | scope/metadata |
| CT-S01 | [abstract.tex](../../conceptual-topography/sections/abstract.tex) | working MD:24 (Abstract) | EN YES / JA WORKING | EN YES / JA NO | include 1/12 |
| CT-S02 | [introduction.tex](../../conceptual-topography/sections/introduction.tex) | working MD:49 (§1) | EN YES / JA WORKING | EN YES / JA NO | include 2/12 |
| CT-S03 | [intuitive_picture.tex](../../conceptual-topography/sections/intuitive_picture.tex) | working MD:114 (§2) | EN YES / JA WORKING | EN YES / JA NO | include 3/12 |
| CT-S04 | [formal_mapping.tex](../../conceptual-topography/sections/formal_mapping.tex) | working MD:159 (§3) | EN YES / JA WORKING | EN YES / JA NO | include 4/12 |
| CT-S05 | [core_equations.tex](../../conceptual-topography/sections/core_equations.tex) | working MD:208 (§4) | EN YES / JA WORKING | EN YES / JA NO | include 5/12 |
| CT-S06 | [structural_interpretation.tex](../../conceptual-topography/sections/structural_interpretation.tex) | working MD:288 (§5) | EN YES / JA WORKING | EN YES / JA NO | include 6/12 |
| CT-S07 | [dynamics.tex](../../conceptual-topography/sections/dynamics.tex) | working MD:339 (§6) | EN YES / JA WORKING | EN YES / JA NO | include 7/12 |
| CT-S08 | [multiscale.tex](../../conceptual-topography/sections/multiscale.tex) | working MD:386 (§7) | EN YES / JA WORKING | EN YES / JA NO | include 8/12 |
| CT-S09 | [pathologies.tex](../../conceptual-topography/sections/pathologies.tex) | working MD:434 (§8) | EN YES / JA WORKING | EN YES / JA NO | include 9/12 |
| CT-S10 | [relation_to_note.tex](../../conceptual-topography/sections/relation_to_note.tex) | working MD:474 (§9) | EN YES / JA WORKING | EN YES / JA NO | include 10/12 |
| CT-S11 | [discussion.tex](../../conceptual-topography/sections/discussion.tex) | working MD:516 (§10) | EN YES / JA WORKING | EN YES / JA NO | include 11/12 |
| CT-S12 | [conclusion.tex](../../conceptual-topography/sections/conclusion.tex) | working MD:552 (§11) | EN YES / JA WORKING | EN YES / JA NO | include 12/12 |

bibliographyはmain.tex末尾のbibliography{refs}、plainnat/natbib。figureはS03でFIG001、S05でFIG002/003をincludegraphics。JA working MDにimage includeは0。

## 5. Distribution artifacts

| Artifact | Role / count | Repository-local observation |
|---|---|---|
| [main.pdf](../../conceptual-topography/main.pdf) | EN DISTRIBUTION、19頁 | pypdfで全頁text/image objects読取。PDF metadata Creation/ModDate 2026-05-19 05:46:21 +09:00、producer pdfTeX-1.40.27 |
| JA PDF | NOT LOCATED | main_ja.pdfなし。root EN/JA READMEもCTにはEN main.pdfのみリンク |
| 図掲載 | 3 image objects | FIG001 p6、FIG002 p10、FIG003 p11。各embedded RGB画素と現行PNGが3/3一致 |
| bibliography | p18–19、7 cited entries | refs.bib全8件を全て印刷しているわけではない |
| freshness | APPARENTLY ALIGNED / NOT FULLY CERTIFIED | cognitive observation window、非pointwise-gradient guard、not identical entitiesを抽出textで確認。PDF mtimeはentry/結論mtimeより後。これだけで全行最新とは断定しない |

PDFスキルに従い図3枚を画像表示し、PDF p6をGSで一時PNGへrenderして視認した。Poppler未導入のため既存Ghostscriptを使用、install/networkなし。これは既存PDFの閲覧でありrebuildではない。図の掲載とラベルを確認するspot-checkであり出版品質の全頁検査ではない。PDFの語分割により単純phrase検索が一致しない箇所もあり、mtimeや検索だけからstale判定しない。

## 6. Upstream dependencies

| DEP | Upstream source | CT source | Object/vocabulary reused | Claimed relation | Exact wording type |
|---|---|---|---|---|---|
| CT-DEP-001 | UP-VED Vol1–4 | S00 scope、S02 §1.2 | difference/gradient/flow/closure | foundational framework | terminology reuse / dependency; “operates within” |
| CT-DEP-002 | UP-IFGT | S04 §3.1 | I=f(1-C)、cognitive observation window | projected realization, not new primitive | formal reuse / interpretation |
| CT-DEP-003 | UP-IFGT / Master v2.1 declaration | S00/S04、README | Phi=K*I primary、linear approximation | applies, does not redefine | formal reuse; current IFGTのlinear formとの版接続は未固定 |
| CT-DEP-004 | UP-IFGT fundamental dynamics | S05 §4.1 | balance、J_I、F_I | governing field equations | equation reuse; upstream裸Jと区別 |
| CT-DEP-005 | UP-IFGT unified equation | S05 §4.1、S07 §6.3 | drive/dissip/barrier、C*/Cmax | cognitive-domain analogue of effective barrier | equation reuse / analogy / interpretation |
| CT-DEP-006 | VED×IFGT loop vocabulary | S01/S05 §4.3 FIG003 | Delta→C→I→Phi→J_I→Delta | irreversible loop assumed throughout | formal reuse / dependency |
| CT-DEP-007 | UP-VED/IFGT | S05 §4.5、S12 | positivity / nonclosure | “follows from”、framework proposition | derivation wording（成立判定なし） |
| CT-DEP-008 | unified VED×IFGT equation | S02 §1.2、S06 §5.1 | solution classes→cognitive phenomena | identifies solution classes | structural correspondence / derivation vocabulary |
| CT-DEP-009 | VED foundation / IFGT conventions | S11 §10.1、S12末尾 | particle/concept、generative grammar | grounded attractors; projected stabilization regimes | motivation / correspondence; JAは同一基礎方程式 |
| CT-DEP-010 | Consciousness note / future paper | S10 §9.1、S09 §8.1 | CPU/GPU、fast/slow、access | corresponds / will be formalized / downstream | interpretation / future dependency |
| CT-DEP-011 | unnamed note series | S10 §9.2、S12 | terrain/flow/sedimentation | formal theory supports L1 | claimed support / interpretation、exact source unclear |
| CT-DEP-012 | Master Variable Table v2.1 | S00/S02/S04、README | variable convention and non-redefinition | “All variables conform” | terminology/formal reuse、document locator unclear |

Bio-IFGTのCT内名指しdependencyは0。Intelligenceは同列future paperと社会的知性解釈であり、CTがIntelligence Part I/IIの式を輸入する箇所は未発見。Consciousnessのfour-layer tableからBio→CTの導出を補わない。UP-IFGTの現在sourceはcross-theory/matrix-to-field bridgeをOPENと明記するが、それを使ってCTのclaimをこのphaseで判定しない。

## 7. Consciousness reciprocal dependencies

下表は方向付きfamily。CT locatorが「未発見」の行はCon側だけが具体的CT節を参照している。相互citationが対称に存在するという意味ではない。SSO/TCA/qualiaの名称とfour-layer表はCT本文に未発見。insight/log/terrainはCT自身の語として存在する。

| ID | CT locator | Consciousness locator/object | Source wording / authority direction | CT側での扱い |
|---|---|---|---|---|
| CT-CON-XDEP-001 | S02 series table、JA §1.2 | companion Consciousness | CT→future paper “forthcoming” | future work / navigation |
| CT-CON-XDEP-002 | S09 §8.1 | conscious access / mechanism | CT→companion “mechanistic basis is the subject” | downstream resultを将来paperへ委ねる |
| CT-CON-XDEP-003 | S10 §9.1 | Consciousness note CPU/GPU | note→CT説明; fast/slow “will be formalized” | input vocabulary / future relation |
| CT-CON-XDEP-004 | S03 §2.4 | CON-SSO EN197 / JA190 | Con→CT invisible GPUとの比較 | CTは独自のbelow-conscious-access記述。SSO名なし |
| CT-CON-XDEP-005 | S05 §4.2 | CON-TCA EN140 / JA163 | Con→CT coupling式の引用・比較 | CTのtoken mechanism claim。TCA名なし |
| CT-CON-XDEP-006 | S05 §4.3、S07 §6.1 | CON-LOOP EN61 / JA63 | Con→CT Phi* sedimentation analogy | CTは長時間attractor。slow-logとの同一化をCTは明示しない |
| CT-CON-XDEP-007 | S04 §3.2、S05 §4.4 | CON-LOOP EN132 / JA143 | Con→CT gradient/concept comparison | CTはleast cognitive resistance。Conのmeaning fieldと別locator |
| CT-CON-XDEP-008 | S07 §6.4 | CON-MAP qualia/insight row | Con→CT boundary-like analogy、no phenomenal identity | CTはinsight phenomenology→topology correspondence。qualia名なし |
| CT-CON-XDEP-009 | S05 §4.4 | CON-MAP log reference/understanding row | Con→CT traversal cost comparison | CTはunderstanding definition |
| CT-CON-XDEP-010 | S05 §4.5 | CON-MAP positivity row | Con→CT two windows comparison | CTのnonclosure proposition。共通phenomenal objectとしない |
| CT-CON-XDEP-011 | CTにfour-window table未発見 | CON-SCOPE / CON-MAP末尾 | Con→VED/Bio/CT/Intelligence比較 | CTのseries L0/L1表とは別。shared grammarの相互承認とは数えない |
| CT-CON-XDEP-012 | S04 projected-use scope | CON introduction EN45 / JA44 | Con→CT cognitive-window stabilization motivation | CTはcognitive projection、Conのfast/slow実証入力ではない |

current Con側はcomparison/no shared limit/no same quantity/no typed translation/no mutual validationを明示する。Con audit/core CLOSEDはその側の文書状態のみ。CTの現在claimをCon wordingで書き換えたり、CTのvalidity根拠に用いたりしない。

## 8. Intelligence handoff dependencies

| ID | CT source | Intelligence / navigation source | Relation wording | Authority direction |
|---|---|---|---|---|
| CT-INT-XDEP-001 | S02 §1.2 | series Intelligence [forthcoming] | future relation / peer application | CT→future theory（Part I/IIの特定なし） |
| CT-INT-XDEP-002 | S05 §4.5 Remark | theories of intelligence/understanding | “direct implications” | CT nonclosure→知性の一般的含意、formal handoffは未特定 |
| CT-INT-XDEP-003 | S08 §7.4、S12 | socially distributed intelligence | “Intelligence is … maintenance” | CT内の知性定義。既存Intelligence論文からの引用ではない |
| CT-INT-XDEP-004 | token/vocabulary一般 | INT2-I:104、226 | representation/symbol layer・CT | Intelligence→CT navigation / substrate-like naming |
| CT-INT-XDEP-005 | CT branch一般 | INT2-I:243 | 同位の領域横断ホモロジー | Intelligence→CT comparison; serial derivationではない |
| CT-INT-XDEP-006 | closure / metastability / boundary / branching | INT2-B:21–26 | CT列とのproposed homology | Intelligence→CT structural comparison |
| CT-INT-XDEP-007 | CT vocabularyを再使用 | INT2-MD combined:77/158/172、appendices:138–143 | representation/tree/homology | downstream working duplicate、独立supportに加算しない |
| CT-INT-XDEP-008 | S03 landscape / S07 sedimentation | NAV concept_traps:225–233 | inference traverses CT, does not re-sediment | supporting LLM解釈。CTの実行モデルやInt1引用ではない |

INT2のJA TeXはmain_jaから実際にincludeされる。EN introduction/homology counterpartには同じCT named列が未発見であり、JAの記述をENに自動継承しない。INT1 canonical sections EN/JAおよびCT bibliographyでCT名指しreferenceは未発見。概念・学習・推論という一般語だけでCT→Intelligence generationを推定しない。

## 9. Formal object families

First sourceはEN input順（entry内の単なる宣言を含む）。括弧に主要定義箇所。これはnamed-family locatorでありPhase01 signature/type定義ではない。記号未供給のobjectを補わない。

| OBJ | Symbol/name | First source / main locator | Roles | Upstream origin claimed? / Notes |
|---|---|---|---|---|
| CT-OBJ-001 | x / x1,x2 | S01、FIG001 | T0/T1 | conceptual position、図の座標。domain/metricは後続確認 |
| CT-OBJ-002 | tau | S00、S04 table | T0/T2/T3 | Master/IFGT継承、irreversible orderingとexperiential timeを併記 |
| CT-OBJ-003 | C | S00、S04 table | T0/T1 | IFGT projected closure / conceptual fixation |
| CT-OBJ-004 | I=f(1-C) | S00/S01、S04 | T0/T1/T2 | cognitive-window unresolved tension。Con log densityと合併しない |
| CT-OBJ-005 | Phi=K*I | S00/S01、S04 | T0/T1/T2 | potential / landscape、意味場ではないという除外もある |
| CT-OBJ-006 | K | S00、S04/S11 | T0 | convolution kernel、具体形はsourceでfuture work |
| CT-OBJ-007 | grad Phi / -grad Phi | S01、S03/S04 | T0/T2 | constraint force / least cognitive resistance |
| CT-OBJ-008 | J_I / macro JI | S00/S01、S05 | T0/T2 | flow / thought trajectory。FIG003裸Jを別記録 |
| CT-OBJ-009 | J_C / macro JC | S00、README | T0 | VED-side closure flow。CT本文の主evolutionではない |
| CT-OBJ-010 | sigma / three terms | S00、S04/S05 | T0/T2 | source term / landscape deformation、input/forgetting/barrier |
| CT-OBJ-011 | Delta | S01、S04 table | T0/T2 | residual asymmetry / novel experience,input |
| CT-OBJ-012 | delta I | S04 table | T0/T1 | unresolved conceptual residue / trace |
| CT-OBJ-013 | ell_i / linguistic token | S01、S05 §4.2 | T0/T1/T2 | discrete re-addressable unit、meaning-neutralと記載。位置vectorを監査で補わない |
| CT-OBJ-014 | Q / constraints | S01、S04 remark | T0/T1 | quantization naming; physical analogy/isomorphic wording |
| CT-OBJ-015 | L_eff,L_field,L_token,lambda | S05 §4.2 | T0/T2 | token-field coupling、full signatureはPhase01対象 |
| CT-OBJ-016 | Phi* / sedimentation | S01、S05 §4.3 | T0/T1/T2 | long-time attractor、mature terrain、not necessarily unique/static |
| CT-OBJ-017 | concept / well | S01、S05 Definition | T0/T1 | locally stable region + perturbation stability |
| CT-OBJ-018 | R / traversal cost / theta | S01概念、S05 Definition | T0/T2 | understanding threshold; theta値未指定 |
| CT-OBJ-019 | Cmax | S00、S05 | T0/T1 | ideal boundary、JAのhard upper bound wordingと別記録 |
| CT-OBJ-020 | C* | S05 §4.1 | T0/T1 | effective saturation、EN C*<Cmax prose |
| CT-OBJ-021 | D,mu,alpha,F_I,Phi0 | S00/S04、S05 | T0 | response/diffusion/constraint/linear approximation。Con muとは同定しない |
| CT-OBJ-022 | a,Gamma,kappa_B | S05 §4.1 | T0/T2 | input,decay,barrier parametersの認知的解釈 |
| CT-OBJ-023 | depth,width,curvature | S03、S06 §5.2 | T0/T1/T2 | resistance/contextual range/precision |
| CT-OBJ-024 | ridge / boundary / category edge | S03 FIG001、S06 | T0/T1/T2 | high potential/traversal cost。category individuationはS11で未指定 |
| CT-OBJ-025 | V,S(ell_i),epsilon | S06 §5.4 | T0/T1 | vocabulary/stability functional; reuse,persistence,depthからderivedとの文言 |
| CT-OBJ-026 | limit cycle / recurring thought | S06 §5.1 | T0/T2 | solution-class interpretation |
| CT-OBJ-027 | topology / bifurcation / insight | S07 §6.3–4 | T0/T1/T2/T3 | merger/split/thresholdとfelt suddenness |
| CT-OBJ-028 | social/collective Phi / shared terrain | S01、S08 | T0/T1/T2 | 同glyphによるmulti-agent拡張、individual fieldと別context |
| CT-OBJ-029 | projection / cognitive observation window | S00/S01 | T0/T1 | coarse-grained realizationと記述。演算子を新設しない |
| CT-OBJ-030 | distance / similarity / adjacency | S03 §2.3、S06 §5.3、S11 §10.1 | T1/T2 | similar landscapes / neighboring wells / embedding proximity。CT metric dやsimilarity式は未発見 |
| CT-OBJ-031 | memory / reuse / forgetting | S03、S07 §6.1–2 | T0/T2 | sedimentation/relaxation、separate memory variableは未発見 |
| CT-OBJ-032 | meaning / available trajectories | S03 §2.2、S04 §3.3、S09 | T1/T2/T3 | meaning-neutral primitiveとdownstream meaning解釈を両方記録 |

## 10. Symbol / glyph reuse

YESはsourceが同一またはmacro aliasと明示、NOは明示区別、UNCLEARは接続未特定。監査のobject同一性判定ではない。

| ID | Symbol | Locations | Local meanings | Same object explicitly claimed? | Possible collision |
|---|---|---|---|---|---|
| CT-GLYPH-001 | Phi | S00/S04 vs UP-IFGT fundamental | K*I primary vs linear closure potential | UNCLEAR（CT非再定義宣言あり） | general templateとcognitive projection |
| CT-GLYPH-002 | Phi | S04 vs CON-LOOP | constraint geometry / effective meaning landscape | NO（current Con区別） | cognitive fieldとCon meaning quantity |
| CT-GLYPH-003 | Phi* | S05/S07 vs CON-LOOP | asymptotic terrain / slow-log analogy | NO（Con no shared limit） | limit objectの相互流用 |
| CT-GLYPH-004 | tau | S04/S05 vs Con core/timing | experiential order,long-time parameter / internal delay | NO（CON-LOOP区別） | 時間・順序・遅延 |
| CT-GLYPH-005 | J,J_I,JI | README、S05、FIG003、UP-IFGT | no bare J convention / subscript flow / image bare J | UNCLEAR（JI macro=J_IはYES） | 図だけ裸J |
| CT-GLYPH-006 | C,Cmax | S04/S05、JA §3/4、UP-VED | effective scalar/fixation / matrix causal logs / ideal vs hard bound | UNCLEAR | 同glyphからmatrix→fieldを推定不可 |
| CT-GLYPH-007 | sigma_d,p,b / drive,dissip,barrier | S04 table / S05 / UP-IFGT unified | short vs long names、signed upstream terms vs CT正量を差引 | UNCLEAR | suffixと符号 conventionの翻訳未固定 |
| CT-GLYPH-008 | ell_i | S04 table / S05 dot product / FIG002 | discrete unit/operator / gradient coupling input | UNCLEAR | token、位置、vector型を自動同定不可 |
| CT-GLYPH-009 | Phi / collective Phi | S04 / S08 | individual vs social field | UNCLEAR（“same dynamics”） | common state-space/aggregationは未特定 |
| CT-GLYPH-010 | mu | S05 / CON-TCA | flow response / effective viscosity | NO（Con source-local comparison） | sharedunits/meaningを推定不可 |
| CT-GLYPH-011 | C* / Cmax | S05 §4.1、JA対応 | saturation / ideal boundary | NO（EN区別） | JA定義補足欠落 |
| CT-GLYPH-012 | Phi | CT vs INT2-B U=Phi(L,H) | scalar potential / emergence-form notation | UNCLEAR | 接点近傍の別glyph-use、同一CT輸入とは数えない |

## 11. Equation / formal relation locator

ENのequation/align環境をraw区切りで数えると12 blocks。alignの3行を別relation occurrenceにすると14 occurrences、うちdissipationが§6.2で再出現、named labelsは13。JAは14個の$$ display、同じrelation集合に対応する（翻訳・macro・組版差を残す）。entryにはdisplayなし。本文inline、tables、caption、画像内式はこのblock数に含めない。

| Locator family | EN locator | JA locator | Phase00 observation |
|---|---|---|---|
| Potential | S04 eq:Phi_primary | §3.1 | K convolution |
| Balance | S05 eq:I_evolution | §4.1 | IFGT-like tau/J_I balance |
| Flow/force | S05 eq:JI | §4.1 | J_I,F_I,-grad Phi,alpha grad C |
| Source decomposition | S05 eq:sigma | §4.1 | drive minus dissip minus barrier |
| Three contributions | S05 align eq:sigma_drive/dissip/barrier | §4.1の3 displays | 1 EN block vs3 JA blocks、関係数は3 |
| Coupling | S05 eq:coupling | §4.2 | L_effとlambda sum dot-gradient |
| Sedimentation | S05 eq:sedimentation | §4.3 | tau→infinity,Phi* |
| Concept | S05 eq:concept | §4.4 | grad≈0、perturbation stability（言語部分差あり） |
| Understanding | S05 eq:understanding | §4.4 | R integral < theta |
| Positivity | S05 eq:positivity | §4.5 | I>0,forall x,tau |
| Vocabulary | S06 eq:vocabulary | §5.4 | set and S threshold |
| Dissipation repeat | S07 §6.2 unlabeled | §6.2 | repeated Gamma C |

主要importはbalance/flow/three-source、明示CT-local追加はtoken coupling・concept/understanding/vocabularyの定義位置。輸入の成否を判定しない。J_C式とQ token extractionはREADME/inline/tableに存在するがdisplay inventoryに混入させない。ENだけのC*<Cmax prose-inline、JAだけのpositivity→gradient→flow prose-inline chainがある。figure独自のx1/x2、bare J cycleは§19。完全signature/展開/妥当性はPhase01以降。

## 12. Claim families

同じEN/JA主題・summary反復は1 familyに集約。強度の違いはlocatorを併記して§20へ渡す。48は今回見つけたmajor familiesの行数であり理論の全命題数ではない。
Crossing欄はsourceが形式・意味・機能・経験を接続する所在。T0→T1等は監査の説明用directionであり成立したbridgeではない。

| CLM | Source | Short claim | Claim vocabulary | T-layer crossing | Strong wording marker |
|---|---|---|---|---|---|
| CT-CLM-001 | S01/S04 | 概念地形はPhiの長時間幾何 | definition / landscape | T0→T1 | defined as |
| CT-CLM-002 | S02 §1.2/S06 §5.1 | 統一方程式の認知的解クラスを同定 | solution class | T0→T2 | identifies / establishes |
| CT-CLM-003 | S04 §3.1 | Iは認知窓の未解決緊張を表現 | projected representation | T0→T1 | represents |
| CT-CLM-004 | S04 §3.1 | 高Iはconceptually active領域 | activity interpretation | T0→T2 | corresponds |
| CT-CLM-005 | S04/S05 | Phi幾何が後続flowの方向を拘束 | formal dynamics | — | encodes / determines |
| CT-CLM-006 | S05 §4.4/S02 | conceptは局所安定領域 | concept definition | T0→T1 | is / defined |
| CT-CLM-007 | S05 §4.4 | understandingはtraversal cost閾値条件 | functional definition | T0→T2 | is the state |
| CT-CLM-008 | S03 §2.1/S04 | thoughtはflow trajectory | thought interpretation | T0→T2 | is |
| CT-CLM-009 | S03 §2.2 | meaningは利用可能なtrajectory集合 | semantic interpretation | T0→T1 | EN is / JA下流的解釈 |
| CT-CLM-010 | S03 §2.4 | 不可視の地形が自然な連想・突然の理解感を生む | phenomenology | T0→T3 | gives rise to / reflect |
| CT-CLM-011 | S04 table | tauは概念発展のexperiential time | time interpretation | T0→T3 | table identity-like |
| CT-CLM-012 | S05 §4.2 | 離散re-addressable unitは安定した低cost再帰に必要 | necessity / token | T0→T2 | cannot / requires |
| CT-CLM-013 | S05 §4.2/FIG002 | token reuseがgradient/井戸を強化 | coupling mechanism | T1→T2 | purely dynamical / reinforces |
| CT-CLM-014 | S03 §2.3 | communicationはsimilar landscapeの反応同期 | communication | T1→T2 | succeeds not because … but because |
| CT-CLM-015 | S05 §4.3 | repeated couplingでPhi→Phi* | asymptotic geometry | T0→T1 | approaches |
| CT-CLM-016 | S05 §4.3 | Phi*はhistoryを反映しなお変形する | asymptotic qualification | — | not necessarily unique or static |
| CT-CLM-017 | S03 §2.1/S10 table | 理解した経験は移動の容易さの変化 | felt understanding | T2→T3 | is not … but |
| CT-CLM-018 | S05 §4.5 EN | I>0は通常状態として完全概念閉包を除外 | framework proposition | T0→T1 | excludes / generically |
| CT-CLM-019 | JA §§概要/3.1/4.5/7.4/11 | 正値性は常時残余勾配を保証/含意する | JA local stronger wording | T0→T1 | 保証 / 含意 |
| CT-CLM-020 | S06 §5.2 | depth/width/curvatureが抵抗/文脈/精度を表す | geometry interpretation | T0→T1 | measures / produces |
| CT-CLM-021 | S06 §5.3 | ridge変形がsemantic driftを説明 | boundary mechanism | T0→T1; T1→T2 | mechanistic account |
| CT-CLM-022 | S06 §5.4 | vocabularyは安定性による集合/分布 | semantic organization | T0→T1 | constitutes / is |
| CT-CLM-023 | S07 §6.1 | 反復強化でconceptがself-sustainingになる | learning/sedimentation | T0→T2 | ensures / becomes |
| CT-CLM-024 | S07 §6.2 | 忘却/想起はflattening/re-deepening | memory | T0→T2 | corresponds / do not disappear |
| CT-CLM-025 | S07 §6.3–4 | conceptual change/insightはrapid topology change | semantic/cognitive event | T0→T1; T0→T2; T0→T3 | corresponds / is bifurcation |
| CT-CLM-026 | S07 §6.4 | 主観的突然性はtopology thresholdの反映 | subjective event | T0→T3 | reflects |
| CT-CLM-027 | S07 §6.3 | effective barrierはbelief revision抵抗を説明 | belief mechanism | T0→T2 | accounts for |
| CT-CLM-028 | S08 §7.1 | 個体→社会で同一力学、支配costのみ交替 | cross-scale generalization | T0→T2 | same dynamics / no property changed |
| CT-CLM-029 | S08 §7.2 | shared inputsがcorrelated wells/shared landscapeを生成 | social learning | T1→T2 | produces / emerges |
| CT-CLM-030 | S08 §7.3 | norms/institutionsはcollective attractor | social ontology wording | T0→T1 | are |
| CT-CLM-031 | S08 §7.3 | 制度安定はcentral authority不要、well depthから従う | social mechanism | T0→T2 | does not require / follows from |
| CT-CLM-032 | S09 §8.2 | overclosure/underclosureがrigidity/unstable thoughtに対応 | pathology interpretation | T0→T2; T0→T3 | corresponds phenomenologically |
| CT-CLM-033 | S09 §8.1 | subjective experienceを生成/説明しない | negative scope | — | does not generate or explain |
| CT-CLM-034 | S09 §8.1/S11 | neural implementationはfuture work | negative scope | — | deferred / open question |
| CT-CLM-035 | S09 §8.2 | sync breakdownはcommunication failure/polarizationの構造基盤 | social function | T1→T2 | identifies as structural basis |
| CT-CLM-036 | S09 §8.3/S11 | parameters/observable correspondence/individuation未指定 | methodological scope | — | does not establish / needed |
| CT-CLM-037 | S10 §9.2/S12 | L3がL1 noteを理論的に支える | document authority | — | theoretical basis / provides |
| CT-CLM-038 | S10 §9.1 | Consciousness note CPU/GPUと将来fast/slow対応 | cross-paper correspondence | — | corresponds / will be formalized |
| CT-CLM-039 | S08 §7.4/S12 | intelligenceはshared landscape維持の分散過程 | functional definition | T1→T2 | Intelligence is |
| CT-CLM-040 | S04 Q remark | quantizationとstructurally isomorphic、quantum主張は否定 | cross-scale analogy | — | isomorphic / analogy |
| CT-CLM-041 | S11 §10.1 | distributional semanticsと使用history/共起の違い | methodological comparison | — | differs fundamentally |
| CT-CLM-042 | S11 §10.1 | driveはprediction error influx、deepeningはerror minimization | functional correspondence | T0→T2 | corresponds / can be understood |
| CT-CLM-043 | S12 EN末尾 | concept/particleはsame generative grammarのprojected regimes | cross-scale generalization | T0→T1 | same / not identical entities |
| CT-CLM-044 | JA結論末尾 | concept/particleは同一基礎方程式の解クラス | JA cross-scale wording | T0→T1 | 同一 / 存在論的種類ではなく |
| CT-CLM-045 | S04 §3.3/S09 | Phiはmeaning fieldでなくtokensはmeaning unitsでない | negative semantic scope | — | not / methodological |
| CT-CLM-046 | S02/S09 | thoughtにdirecting subjectを必要としない | functional scope | — | does not require |
| CT-CLM-047 | S05 §4.1 | drive/decay/barrierはinput/forgetting/overclosure抵抗 | cognitive interpretation | T0→T2 | represents |
| CT-CLM-048 | S00/README | general variablesを再定義せずcognitive projectionとして使う | inheritance scope | T0→T1 | does not redefine / applies |

## 13. Layer crossings

| Source-local crossing | Families（edgeごとの重複なし） |
|---|---|
| T0→T1 | 15 |
| T0→T2 | 14 |
| T0→T3 | 5 |
| T1→T2 | 6 |
| T1→T3 | 0 |
| T2→T3 | 1 |

いずれかのcrossingを持つunique claim families: 37 / 48。

複数edgeを持つfamilyはedgeごとに1回数え、同一claimのabstract/conclusion反復は増やさない。「—」は非crossing、scopeのみ、または同層比較。T3の所在はCLM010/011/017/025/026/032などの体験語であり、CTを意識主理論に再分類しない。Sourceの「主観経験を生成／説明しない」という除外（CLM033）もそのまま保持する。

## 14. Semantic preload inventory

Pは仮ラベル。preloadの存在≠不正・循環。定義の良否も判定しない。

| ID | Source | Supplied object / wording | Provisional type | Later interpreted role |
|---|---|---|---|---|
| CT-PRELOAD-001 | S04/S05 | x,scalar field,gradient,convolution | P0 purely formal | landscape geometry |
| CT-PRELOAD-002 | S00/S04 | cognitive observation window | P1 representational naming | general-field projected use |
| CT-PRELOAD-003 | S04 table | C=conceptual fixation | P2 semantic preload | entrenched concept |
| CT-PRELOAD-004 | S04 §3.1 | I=unresolved conceptual tension | P2 semantic preload | conceptually active regions |
| CT-PRELOAD-005 | S04 table | Phi=conceptual landscape itself | P1 representational naming | terrain emergence |
| CT-PRELOAD-006 | S01/S05 | ell_i already linguistic/re-addressable | P1 representational naming | stable recursion; content-neutral guard retained |
| CT-PRELOAD-007 | S03/S05 | concept=stable basin | P2 semantic preload | concept formation / stability |
| CT-PRELOAD-008 | S05 Definition | low cost labeled understanding | P3 cognitive preload | understanding obtains |
| CT-PRELOAD-009 | S04 table | gradient=least cognitive resistance、flow=thought | P3 cognitive preload | biases thought |
| CT-PRELOAD-010 | S04 table | tau=experiential time | P4 phenomenal preload | conceptual development order |
| CT-PRELOAD-011 | S06 §5.2 | width=context、curvature=precision | P2 semantic preload | sharp/fuzzy concepts |
| CT-PRELOAD-012 | S06 §5.3 | ridge=category boundary | P2 semantic preload | semantic drift / concept change |
| CT-PRELOAD-013 | S07 §6.4 | topology change linked to felt insight | P4 phenomenal preload | sudden understanding interpretation |
| CT-PRELOAD-014 | S08 §7.2 | agents with similar prior landscapes | P3 cognitive preload | shared landscape / intelligence |
| CT-PRELOAD-015 | S04 Q remark | “constraints” argument not instantiated | P5 unresolved | discrete stable units / compression |
| CT-PRELOAD-016 | S03 §2.3、S08 | same/similar input and landscape | P5 unresolved | communication/synchronization criterion |

## 15. Representation / ontology distinctions

| ID | Source | Formal object | Semantic/cognitive interpretation | Wording strength |
|---|---|---|---|---|
| CT-REP-001 | S00/S04 | projected I,C,Phi | cognitive realization | “should be read as projected” / does not redefine |
| CT-REP-002 | S04 table | Phi | conceptual landscape | “itself” |
| CT-REP-003 | S05 Definition | stable potential region | concept | definition “is” |
| CT-REP-004 | S05 Definition | traversal integral<threshold | understanding | definition “is the state” |
| CT-REP-005 | S03 §2.2 | attractor trajectories | meaning | EN “is”; JA downstream interpretation |
| CT-REP-006 | S04 table/§3.3 | J_I | thought / not thought content | identity-like naming + negative scope |
| CT-REP-007 | S05 §4.2 | ell_i-gradient coupling | meaning-neutral language | “purely dynamical”, “do not encode” |
| CT-REP-008 | S06 §5.2 | geometry depth/width/curvature | resistance/range/precision | “measures”, “produces” |
| CT-REP-009 | S07 §6.4 | bifurcation | experienced insight | “corresponds”, “reflects” |
| CT-REP-010 | S08 §7.3 | collective attractor | norms/institutions | “are”, “follows from” |
| CT-REP-011 | S12末尾、JA結論 | physical/conceptual stabilization | cross-domain entity status | EN projected regimes/not identical、JA same-equation solution classes |
| CT-REP-012 | S09 §8.1 | semantic/phenomenal exclusions | no subjective experience generation | explicit negative scope、ontologyを決めない旨 |

## 16. Asymptotic / convergence claims

| ID | Source | Object / relation | Math/prose/import | Semantic / cognitive attachment |
|---|---|---|---|---|
| CT-ASYM-001 | S01 | long-time geometry under recursive interaction | inline Phi→Phi* / framework loop | mature conceptual landscape |
| CT-ASYM-002 | S05 §4.3 | tau→infinity limit | displayed relation | sedimented terrain |
| CT-ASYM-003 | S05直後、JA §4.3 | not necessarily unique/static vs 一意でも静的でもない | prose qualification | history-dependent continual reshaping |
| CT-ASYM-004 | S05 concept definition | local stability under perturbation | displayed predicate | concept |
| CT-ASYM-005 | S06 §5.1 | metastable/deep stable/limit cycle | table/formal labels、unified equation reuse | beliefs/recurring thought |
| CT-ASYM-006 | S07 §6.1 | perturbation→reinforcement→stabilization | prose stages + coupling reference | self-sustaining concept |
| CT-ASYM-007 | S07 §6.2 | relaxation/forgetting/reactivation | Gamma C display + prose | memory/accessibility |
| CT-ASYM-008 | S07 §6.3 | Phi* merges/splits/displaces | prose topology changes | semantic/cognitive revision |
| CT-ASYM-009 | S08 §7.2–4 | shared sedimentation/maintenance | qualitative extension | institutions/collective intelligence |
| CT-ASYM-010 | S05 §4.5、S12 | local quiescence / no final closure | positivity display + prose | open conceptual development |

fixed pointという独立CT変数/定理は未発見。S06のlimit-cycle名、S05のlimit式、S07の更新中Phi*を同じ主張に潰さない。収束証明や安定性の妥当性は未判定。

## 17. Insight / boundary inventory

| ID | Source | Statement location | Source roles / wording |
|---|---|---|---|
| CT-INSIGHT-001 | S03 §2.1 | felt ease/difficulty of understanding | cognitive/phenomenal example、terrain metaphor |
| CT-INSIGHT-002 | S03 §2.4 | understanding arrives suddenly | phenomenal event attributed to invisible geometry |
| CT-INSIGHT-003 | S06 §5.1/5.3、FIG001 | ridge/category edge | formal boundary ↔ semantic distinction |
| CT-INSIGHT-004 | S06 §5.3 | ridge erosion/reinforcement | semantic transition、mechanistic account wording |
| CT-INSIGHT-005 | S07 §6.3 | merger/split/displacement of Phi* | topological conceptual change |
| CT-INSIGHT-006 | S07 §6.4前段 | sudden resolution/connection | cognitive+phenomenal insight corresponds to bifurcation |
| CT-INSIGHT-007 | S07 §6.4後段 | accumulated perturbation crosses threshold | subjective suddenness reflects topological event |
| CT-INSIGHT-008 | S10 table | “sense of understanding” ↔ integral reduction | note phenomenology/formal correspondence |

Conのqualia比較はCT-CON-XDEP-008。CT側がqualia=insightと述べたことにはしない。CTのinsight章自体にphase-changeの独立定義式・subject criterionは未発見、妥当性/十分性は判定しない。

## 18. Time / order inventory

| ID | Source | Time/order object | Distinction retained |
|---|---|---|---|
| CT-TIME-001 | S04 table | tau experiential time / irreversible ordering | two source roles、physical tとは同定しない |
| CT-TIME-002 | S05 balance | partial_tau I | formal evolution parameter |
| CT-TIME-003 | S05 sedimentation | tau→infinity | long-time limit、finite learning durationと別 |
| CT-TIME-004 | S07 §6.1 | three stages / repeated reuse | developmental explanatory sequence、discrete update-index式なし |
| CT-TIME-005 | S06 S(ell_i) | persistence time / reuse frequency | stability functional inputs、clock/extraction未指定 |
| CT-TIME-006 | S07 §6.4 | suddenness / accumulated subthreshold perturbation | subjective vs event order、latency calibration未指定 |
| CT-TIME-007 | S08 §7.4 | subsequent agents / ongoing interaction | social/historical order、tauの共同clock未指定 |
| CT-TIME-008 | CT §4.3 vs CON-LOOP | CT long-time tau / Con delay tau | Con明示区別、CTに逆同一化文未発見 |

外部時間tの独立CT evolution、iteration n、learning-rate/update-index式はcanonical本文で未発見。図のtauはorderingラベルであり、監査が秒単位を与えない。

## 19. Figure inventory

3 families / 3 PNG assets。editable source、figure PDF、JA variant、JA MD includeは未発見。図は説明assetであり証拠とみなさない。画像を実際に表示して文字・式を読んだ。

| ID | File / format / variant | Caption locator / PDF | Formal labels | Semantic / cognitive / cross-scale labels | Downstream reuse |
|---|---|---|---|---|---|
| CT-FIG-001 | [potential geometry](../../conceptual-topography/figures/fig1_potential_geometry.png)、1536×1024、EN PNG | S03 caption、p6 | Phi(x,tau),x1,x2,grad Phi≈0,-grad Phi,J_I | concept basin A/B、conceptual boundary、thought trajectory | 同名assetの外部include未発見 |
| CT-FIG-002 | [token field](../../conceptual-topography/figures/fig2_token_field_coupling.png)、1536×1024、EN PNG | S05 §4.2 caption、p10 | ell_i,-grad Phi,J_I,lambda sum ell_i dot grad Phi | before/after reuse、deepened basin、lower traversal cost、meaning-neutral | Conがcoupling式を引用するがこのPNG再利用ではない |
| CT-FIG-003 | [recursive loop](../../conceptual-topography/figures/fig3_minimal_recursive_loop.png)、1254×1254、EN PNG | S05 §4.3 caption、p11 | Delta,C,I,Phi,裸J,tau; Delta→C→I→Phi→J→Delta | conceptual attractors、flow/search/integration/transmission、unidirectional causality | VED×IFGT minimal loop名。外部への同asset include未発見 |

FIG003 captionはJ_I、画像は裸J。READMEはbare J not usedと明記。Phase00はこのpresentation authority差だけ記録し、どちらへ直すか決めない。FIG002はreinforced gradientとlower traversal costを同図に置く；定義域・cost読みに関する評価は後続phaseへ渡す。画像生成codeや測定dataを図から推定しない。

## 20. EN / JA variants

EN/JAの概念対応headingは12/12、同格canonical pairは0。JAの版はdraft、ENには2026-05-19のclosure alignmentが記録される。差異がすべて誤訳なのか版更新未反映なのかは決めない。

| ID | Locator | EN | JA working MD | Classification |
|---|---|---|---|---|
| CT-VAR-001 | entries / metadata | modular TeX、2026 | draft 2026-04 / 作業台 | probable version difference |
| CT-VAR-002 | S00/S01/S04 vs JA scope/§3.1 | projected/coarse-grained cognitive windowを明示 | その補足がない | probable version difference |
| CT-VAR-003 | S05 §4.5 vs JA §4.5 | pointwise gradient非含意を明示 | I>0→grad Phi≠0→J_I≠0（一般に） | probable version difference / stronger JA |
| CT-VAR-004 | S01/S02/S04/S08/S12のpositivity | asymmetry/inhomogeneity/new perturbationを条件として記載 | 常に生成的勾配を保証/残余勾配保持 | probable version difference |
| CT-VAR-005 | S05 §4.1 vs JA §4.1 | C* saturation、C*<Cmax prose | 同式のC*説明補足がない | probable version difference、式を補完しない |
| CT-VAR-006 | S04 table/S05/S07 vs JA | Cmax ideal boundary、effective resistance | hard upper bound / structural prohibition / barrier発散 | probable version difference |
| CT-VAR-007 | S12末尾 vs JA結論 | projected regimes、not identical/reducible | 同一基礎方程式の解クラス、ontologyでなくdepth等 | probable version difference / stronger JA |
| CT-VAR-008 | S03 §2.2 | meaning “is … set of trajectories” | 体験される意味を下流的解釈とする | local variant / weaker JA identity |
| CT-VAR-009 | S02 §1.3 | conceptのstable-region定義 | 再帰的再入可能性で再定義する追加文 | local variant |
| CT-VAR-010 | S05 §4.3 | not necessarily unique or static | 一意でも静的でもない | translation difference / logical strength |
| CT-VAR-011 | S04 Q remark | quantization in physical sense / stable values | 量子力学 / 離散固有値 | translation difference / scope emphasis |
| CT-VAR-012 | S09 failure modes heading | Underclosure | 過開放 | translation difference |
| CT-VAR-013 | S03/S05 figures / S11 cites | 3PNG include/captions、citation commands | figures/captions/citekeys/bibliographyなし | source-format/local variant |
| CT-VAR-014 | S05 math / S10 table / S11 foundation | align3行、macros、romanized note語、single axiom+effective conventions | $$3blocks、literal glyph、日本語note語、最小公理から導出 | format difference + probable version difference |

表示式の数学familyが片側だけにあるものは今回の14 relation対応では0。ENのinline C*<Cmax、JAのinline implication chainは「式なし」として落とさない。FIG003のbare J問題はEN/JA翻訳差ではなくfigure/body差。JA figure labelそのものは不存在。

## 21. Citation / bibliography inventory

refs.bibは8 entries（techreport5、book2、article1）。実際のcite/citep commandは6、key usageは11、unique cited keysは7、unresolved keysは0。未引用はgibson1986の1。既存main.bbl/auxと配布PDFには7 references。著者/年/title等はrepository内metadataとして読むだけで外部確認しない。

| ID | Claim/topic/key | CT locator | Citation / entry status | Role inventory |
|---|---|---|---|---|
| CT-CITE-001 | VED_vol1 | S00/S02 | cited / entry present | internal foundation |
| CT-CITE-002 | VED_vol2 | S00 | cited / entry present | internal series |
| CT-CITE-003 | VED_vol3 | S00 | cited / entry present | internal series |
| CT-CITE-004 | VED_vol4 | S00 | cited / entry present | internal series、current Vol4 titleと版照合未確定 |
| CT-CITE-005 | IFGT | S00/S02 | cited / entry present | framework reuse |
| CT-CITE-006 | thelen1994dynamic | S11 §10.1 | cited / entry present | dynamical/embodied cognition precedent |
| CT-CITE-007 | friston2010free | S11 §10.1 | cited / entry present | predictive processing/free energy comparison |
| CT-CITE-008 | gibson1986 | refs.bibのみ | entry present、uncited | bibliography metadata、本文anchorなし |
| CT-CITE-009 | distributional semantics / embedding | S11 §10.1 | named、dedicated citeなし | comparison |
| CT-CITE-010 | physical quantization / JA量子力学 | S04 remark | named、dedicated citeなし | analogy/isomorphic wording |
| CT-CITE-011 | insight/understanding/forgetting | S03/S07 | examples/phenomena、dedicated citeなし | experience/cognitive examples |
| CT-CITE-012 | neural firing/connectivity/oscillations | S11 open questions | named、dedicated citeなし | future correspondence targets |
| CT-CITE-013 | Consciousness | S02/S09/S10 | prose referenceのみ、bib keyなし | companion/future/note |
| CT-CITE-014 | Intelligence | S02/S05/S08 | prose/generic term、bib keyなし | future theory / social definition |
| CT-CITE-015 | companion note series | S10 | exact citation/pathなし | L1/L3 correspondence |
| CT-CITE-016 | Master Variable Table v2.1 | S00/S02/S04 | version nameのみ、entryなし | notational authority declaration |

Consciousness→CTはCT節番号のprose citationと式引用、INT2→CTはtree/tableであり、CTのrefs.bibからのbacklinkとは別。引用の有無は所在inventoryであってadequacy採点ではない。JA working sourceにbib/cite接続は0。

## 22. Code / simulation / dataset inventory

| Search class | Located artifact | Classification |
|---|---|---|
| CT Python/notebook/JS/numerical code | 0 | absent in branch |
| CT simulation / numerical result / dataset / validation script | 0 | absent in branch；測定/検証の成否は判断しない |
| PNG3 | FIG001–003 | visualization。generated plot/data由来かはsource未特定 |
| TeX main+sections / bib | 13 text +1bib | source support / typesetting、simulationではない |
| README build commands / .gitignore | 2 | helper/documentation、今回runしない |
| aux,bbl,blg,log,out,toc | 6 | generated build helpers、empirical outputsではない |
| .DS_Store | 1 | noncanonical OS metadata |
| Bio toy / other repo code | branch外 | CTから実行・data入力として参照未発見、CT証拠に転用しない |

## 23. Documentary dependency cycles

| ID | Documentary path | Located status / limitation |
|---|---|---|
| CT-DOC-CYCLE-001 | CT S09/S10→Consciousness future/note；Con-SSO/TCA/LOOP/MAP→CT具体節 | paper-level reciprocal reference。CT側noteとcurrent Conのexact version identityはOPEN |
| CT-DOC-CYCLE-002 | CT S02 future Intelligence / S08 generic intelligence；INT2-I/B→CT | topic/paper-family往復、CT→Part II theorem supportは未発見 |
| CT-DOC-CYCLE-003 | note L1→CT intuitive picture；CT L3→note theoretical basis | claimed documentary cycle。exact L1 artifact未固定 |
| CT-DOC-CYCLE-004 | S02がS04/05/06をforward案内；S06/S07がS05のequationsへback-reference | internal expositionの相互参照、proof loopとは呼ばない |

循環性の存在・良悪・viciousnessは一切判定しない。これらは「参照が往復する／往復を主張する」というinventory。

## 24. Navigation / dependency orders

| Order | Located sequence | What remains unfixed |
|---|---|---|
| Source navigation | S00→S01 abstract→S02 introduction→…→S12 conclusion→refs | 演繹順ではない。JA headingsも同じ概略順 |
| Claimed conceptual dependency | VED generation + IFGT structure→cognitive-window I/Phi→token interaction→sedimented terrain→concept/thought/understanding→social synchronization/intelligence | source自身のexplanatory order。Consciousnessはforthcoming peer / downstream accessと記載され、必要な生成順は未固定 |
| Formal/equation dependency (partial) | I=f(1-C),Phi=K*I→F_I/flow/balance/source terms；coupling→Phi* notation；stable region/integral→concept/understanding definitions | closed proof DAGは未提示。Q,L_field,L_token,S具体形・boundary/initial conditions・convergenceとの導出辺はPhase01以降で確認 |
| Feedback vs order | Delta→C→I→Phi→J_I→Delta | sourceのrecursive dynamical pictureであり、linear proof orderにはできない |
| External reading path | NAV reading_paths:16 CT→Consciousness | 読者案内。Con-MAPは逆順の読みも案内し、導出順にしない |

## 25. Authority conflicts

「conflict」は比較対象のauthority/wording差を記録する見出しであり、矛盾の数学判定ではない。

| ID | Objects compared | Documentary finding | Handling in Phase00 |
|---|---|---|---|
| CT-AUTH-001 | canonical EN vs JA working | build authorityとdraft roleが異なる | EN canonical、JA WORKINGとして区別。今後の更新意図OPEN |
| CT-AUTH-002 | CT README forthcoming vs current repo | Con/Intelligence actual entries/PDFが存在 | 古いnavigation markerの所在固定、修正しない |
| CT-AUTH-003 | Master v2.1 declaration vs located docs | exact master document未固定 | 外部/他branch tableをcanonicalに代入しない |
| CT-AUTH-004 | FIG003 vs README/body | bare J vs explicit no-bare-J / J_I | figure差保存 |
| CT-AUTH-005 | EN vs JA positivity | residual conditions/pointwise guard vs gradient含意 | CT-VAR-003/004へ |
| CT-AUTH-006 | EN vs JA barrier/C* | ideal boundary/effective resistance vs hard prohibition | CT-VAR-005/006へ |
| CT-AUTH-007 | CT framework identity vs current IFGT | CT non-redefinition/solution-class語、IFGTにはsource-local/open bridge guard | 同glyphと現行formal identityを分離 |
| CT-AUTH-008 | CT entry series L1 vs S10 L3 | application-layer labelとexposition-layer labelが共存 | 別axisとして所在固定、単一序列に統合しない |
| CT-AUTH-009 | semantic/phenomenal exclusions vs positive interpretations | S04/S09除外とS03/S07 meaning/insight文 | role auditへ、成否判定しない |
| CT-AUTH-010 | limit Phi* vs continued deformation | limit notationと非unique/staticの補足 | asymptotic roleの同定OPEN |
| CT-AUTH-011 | CT physical/concept conclusion EN/JA | EN非identityとJA same-equation ontology wording | version差の所在固定 |
| CT-AUTH-012 | CT Con-future/note vs revised Con comparison | citation方向・版・強度が非対称 | Con closureをCTへ移さない |
| CT-AUTH-013 | CT social intelligence vs INT2 CT representation layer | topic定義とtheory-tree位置が別 | 同じIntelligence objectと推定しない |
| CT-AUTH-014 | CT bib Vol titles vs current entries | refs metadataにはFoundations/Standard Model/Gravity and Cosmology等 | exact historical source/version未固定、citation改訂しない |

## 26. Initial uncertainty ledger

すべて初期inventoryのUNRESOLVEDであり、claim dispositionのOPENを割り当てた表ではない。canonical ENの発見自体はdocumentary確定だが、別版・翻訳・relationの研究意図は保持する。

| ID | Unresolved item | Source / follow-up locator |
|---|---|---|
| CT-U-001 | JA working→canonical移行・同期の意図 | JA末尾、AUTH001 |
| CT-U-002 | Master Variable Table v2.1 exact artifact/version | S00/README、AUTH003 |
| CT-U-003 | VED/IFGT bibliographyとcurrent sourceのhistory | refs、AUTH014 |
| CT-U-004 | companion note L1のexact title/path/version | S10 |
| CT-U-005 | CT→Con future/noteとcurrent Conの版対応 | XDEP001–003 |
| CT-U-006 | CT→Intelligence generic topicとPart I/IIの対応 | INT-XDEP001–003 |
| CT-U-007 | cognitive projectionのdomain/translation | S00/S04、DEP002 |
| CT-U-008 | CT Phi=K*Iとcurrent IFGT linear Phiの版・役割 | GLYPH001 |
| CT-U-009 | current IFGT JとCT J_Iの型/継承 | GLYPH005 |
| CT-U-010 | FIG003 bare Jとbody/captionの対応 | FIG003、AUTH004 |
| CT-U-011 | sigma short suffix / source terms / signsの対応 | GLYPH007、S05 |
| CT-U-012 | scalar C、VED Cij、cognitive fixationの関係 | GLYPH006 |
| CT-U-013 | C* saturationとCmax ideal/hard boundのEN/JA差 | VAR005/006 |
| CT-U-014 | xのdomain、metric、distance/similarity/adjacency | OBJ001/030 |
| CT-U-015 | token ell_iの型とQ/constraintsの構成 | OBJ013–015 |
| CT-U-016 | meaning-neutral namingとsemantic interpretationの関係 | PRELOAD006、REP005/007 |
| CT-U-017 | Lagrangian couplingとreinforcement/sedimentationの依存 | S05、CLM013/015 |
| CT-U-018 | Phi*のlimit/attractor/変形中landscapeの区別 | ASYM002/003/008 |
| CT-U-019 | concept/basin境界と個体化criterion | S05/S11 |
| CT-U-020 | traversal cost/understanding/felt understandingの区別 | REP004、INSIGHT008 |
| CT-U-021 | tau formal order/experiential time/Con delay | TIME001/008 |
| CT-U-022 | insight topology/event/phenomenal correspondence | INSIGHT006/007 |
| CT-U-023 | semantic exclusionとmeanings/precision/contexts命名 | REP005/008/012 |
| CT-U-024 | positivityとgradient/stasisのEN/JA wording差 | CLM018/019、VAR003/004 |
| CT-U-025 | individual/social同glyph・同力学の拡張 | GLYPH009、CLM028 |
| CT-U-026 | similarity/shared perturbationの指定 | PRELOAD014/016 |
| CT-U-027 | norms/institutions/collective intelligenceとgeometryの関係 | S08 |
| CT-U-028 | CT/Con gradient・terrain・qualia/insight比較のtyped relation | CON-XDEP005–010 |
| CT-U-029 | CT/INT2 tree/homologyとconcept/boundary語 | INT-XDEP004–007 |
| CT-U-030 | L0/L1 seriesとL1/L3 expositionのaxis | AUTH008 |
| CT-U-031 | Q physical quantizationのanalogy/isomorphic wording | VAR011、CLM040 |
| CT-U-032 | 図のeditable origin、bareJ以外のbody/visual関係 | FIG001–003、reinforced gradient/lower cost |
| CT-U-033 | neural/behavioral/linguistic observableとのsource-local接続 | S09/S11 |
| CT-U-034 | 同じgenerative grammar/同一基礎方程式のEN/JA差 | CLM043/044 |
| CT-U-035 | JA一意性/意味解釈/underclosure等の翻訳意図 | VAR008–012 |
| CT-U-036 | reciprocityがどのclaim supportに使われるか | DOC-CYCLE001–004、判定はPhase03 |
| CT-U-037 | PDF全行のfreshness、stale artifactの有無 | §5 spot-check以上の認証は未実施 |
| CT-U-038 | symbol fieldsとdownstream emergence Phiのcollision | GLYPH012 |
| CT-U-039 | S(ell_i)のstabilityとfrequency/persistence/basin関係 | S06 §5.4 |
| CT-U-040 | code/data/figure生成由来のrepository外所在 | §22、外部探索は未実施 |

## 27. Phase00 limits

未判定事項を明示する：CTの数学的validity、semantic geometryの実在、tokenがconceptを表現するか、Phi*が学習概念に対応するか、gradientが認知機構か、insightがboundary transitionか、Consciousness/Intelligenceへの写像、same-structure claim、循環性、経験的support、equation変更要否、KEEP/REVISE/DOWNGRADE/SPLIT/RETIRE/OPEN disposition。

sourceの“derives”“establishes”“mechanistic account”“isomorphic”“same dynamics”は所在とtypeのみを記録した。sourceのnegative scopeもpositive wordingとともに保存し、どちらかで他方を正当化／無効化しない。preloadの仮分類はcircularity verdictではない。

## 28. Validation

検査対象の開始時snapshotはrepository全体（.git内部を除く）1459 files。
取得後、source read/PNG閲覧/PDF renderのみを行い、監査2ファイル以外へ書き込まない。
snapshot保存先: ${TEMP_EVIDENCE_ROOT}/ct_audit_phase00.a6vyzv/start_sha256.json。
ソートした相対path + NUL + SHA256 + newline列の集約SHA256:
0900149937a4b376769baa2c17a08a55400037d375ebe983f1cdf4fd323e9973。

§3にはCT全28fileの開始hashを永続記録した。git HEADでなくdirty working treeの開始hashを比較基準とする。

| Check | Result |
|---|---|
| CT canonical entry / modules | EN1 / 12、canonical text13。全includeが存在。JA canonical entry0、working counterpart12 |
| Source tree | hidden/ignored込み28/28 filesを分類 |
| Formal relation locators | EN12 blocks /14 relation occurrences、JA14 blocks。13 named equation labels |
| Bibliography | refs.bib存在、8 entries、7 unique cited keys、unresolved key0、cite commands6 |
| Figure paths / assets | 3/3存在・画像視認、PDF embedded RGB3/3一致、外部同名include未発見 |
| Distribution | EN PDF19頁、JA未発見。p6視認、freshnessは限定的localevidenceのみ |
| Upstream / downstream | §2path registry、CT明示source wordingとCon/INT2戻り参照を区別 |
| ID uniqueness / ledger counts | machine check結果を下記に記録 |
| Markdown paths / tables / fences | machine check結果を下記に記録 |
| Task mutation boundary | 開始hashとの比較結果を下記に記録 |
| git diff --check | 実行結果を下記に記録 |
| Prohibited actions | source/equation/figure/PDF/bib/code変更なし、simulation/build/web/commit/pushなし |

集計規約: familiesは各台帳の主ID行数。crossingsだけはedge単位とunique claimの両方を示す。source反復やEN/JA同主題を別claimに水増ししない。

| Ledger | Entries |
|---|---|
| CT-DEP | 12 |
| CT-CON-XDEP | 12 |
| CT-INT-XDEP | 8 |
| CT-OBJ | 32 |
| CT-GLYPH | 12 |
| CT-CLM | 48 |
| CT-PRELOAD | 16 |
| CT-REP | 12 |
| CT-ASYM | 10 |
| CT-INSIGHT | 8 |
| CT-TIME | 8 |
| CT-FIG | 3 |
| CT-VAR | 14 |
| CT-CITE | 16 |
| CT-DOC-CYCLE | 4 |
| CT-AUTH | 14 |
| CT-U | 40 |

Layer-crossing unique families: 37。Equation-heavy source: S04/S05/S06/S07。Working/historical: 1/0、figure families:3、distribution PDFs:1、code/simulation/data files:0。

最終機械検査: PASS。主IDは全17台帳でunique/連番、30 required sections、28 Markdown tables、90 local linksを確認。表の見出し列数1件を記録内だけ修正して再検査した。fenceは0、未展開placeholderは0。canonical TeXのinclude/ref/eqref/cite対象は全件存在する。

開始時1459/1459 filesがSHA-256一致、既存ファイルmodified 0 / deleted 0。newは本recordとREADMEの2件のみ。したがってCT・upstream/downstreamのsource/式/図/PDF/code/BibTeXおよび既存dirty editsはすべて不変。git diff --checkはexit 0。untracked監査2ファイルも別途末尾空白とMarkdownを検査した。

git status --short（repository全体）は既存M222 entriesと??5 directoriesを表示する。今回の差分は?? notes/ct_audit/の追加だけであり、他の??（generative_law_methodology、bio_ifgt_audit、consciousness_audit、ved_equation_audit）は開始snapshotに含まれる既存内容。statusだけからtask変更範囲を推定していない。commit/pushなし。


## 29. Stop boundary

Phase00のsource mapを固定して停止。Phase01 equation/symbol/objectのfull audit、role妥当性、preload/circularity判定、burden判定、disposition、source/core revisionには進まない。Consciousness audit/core closure、VED/Bio closureを再開しない。simulation、PDF rebuild、external research、citation追加、commit/pushは実行していない。

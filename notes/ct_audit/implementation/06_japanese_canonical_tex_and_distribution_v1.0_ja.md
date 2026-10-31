# CT Japanese Canonical TeX / JA Distribution Cycle v1.0

## 0. Status / outcome

実施日: 2026-09-11。現行canonical ENを唯一のcontent authorityとして、新しい日本語TeX翻訳版を作成した。旧JA workingをcanonical化したのではない。

```text
CT audit: CLOSED
Final dispositions: FROZEN
CT core/source revision: CLOSED WITH ADVISORIES
Japanese canonical TeX cycle: COMPLETE
Canonical EN: main.tex + 12 sections / content authority unchanged
Canonical JA: main_ja.tex + 12 sections_ja / authorized translation counterpart
Canonical EN distribution: FRESH WITH ADVISORIES / unchanged
Canonical JA distribution: FRESH WITH ADVISORIES / 23 pages
JA working Markdown: retained unchanged / WORKING / historical reference
Global equation-change requirement: OPEN
Research OPEN families: 22 remain OPEN
CT-U-193: DOCUMENTARY RESOLVED
```

48 claim parity: MATCH **40** / MATCH WITH LANGUAGE ADAPTATION **8** / MISMATCH **0** / NOT LOCATED **0**。
Frozen KEEP7 / REVISE9 / DOWNGRADE17 / SPLIT14 / RETIRE0 / OPEN1は不変。
SERIOUS001–003の説明的backedgeの構造的解消を保持する。経験的criterionの確立ではない。

翻訳対応 ≠ 理論検証。canonical JA ≠ working draftの昇格。fresh PDF ≠ empirical validation。
以下の確認は翻訳・組版の検査であり、数学の正しさや研究OPENの解消を判定していない。

## 1. Authority / task-start protection

最上位audit authority: [Phase07](../07_final_audit_and_frozen_dispositions_v1.0_ja.md)。
source-revision cycleのconsistency authority: [Implementation05](05_independent_post_implementation_consistency_audit_v1.0_ja.md)。
status: [audit README](../README_ja.md)。
翻訳内容は現行EN entryと全12 included sectionsだけから採る。過去監査は範囲・凍結判断の照合に用い、旧ENの文言を翻訳元にしない。
[JA working](../../../conceptual-topography/conceptual_topography_ja.md)は訳語・履歴の参照に限定する。

開始時、repositoryの.gitを除く全既存file **1474件**（ignore対象を含む）をSHA-256でsnapshotした。dirty worktreeのHEADとの差ではなくtask-startとの差で保護を検査した。
snapshot manifest: `${TEMP_EVIDENCE_ROOT}/ct_jacan.U6hyjT/baseline.json`。
manifest SHA-256: `a06895b55e4bd5f2c75d638d32f4db345c4eb461c0e49905a565f05551f8d685`。
一時抽出・build・render・検証scriptはrepository外の同temporary directoryに置いた。
ファイル内容の書込みはapply_patch、最終PDFの配置のみビルド済みbinaryのcopyを使用した。

## 2. Created / modified / source map

新設15 files = entry1 + section12 + JA PDF1 + 本record1。
既存変更2 files = branch README / audit README。
EN13 TeX・EN PDF・PNG3・refs.bib・JA working・Phase00–07・Implementation01–05・他branchには変更なし。

S/J番号はinclude順のlocatorで、本文節番号ではない。行番号は本cycleのsource、S00/J00はentry。以下が48 claim台帳のsource mapである。

| Locator | EN source | New JA source | Display / inline (each language) |
| --- | --- | --- | --- |
| S00 / J00 | [main.tex](../../../conceptual-topography/main.tex) | [main_ja.tex](../../../conceptual-topography/main_ja.tex) | 0 / 15 |
| S01 / J01 | [sections/abstract.tex](../../../conceptual-topography/sections/abstract.tex) | [sections_ja/abstract_ja.tex](../../../conceptual-topography/sections_ja/abstract_ja.tex) | 0 / 16 |
| S02 / J02 | [sections/introduction.tex](../../../conceptual-topography/sections/introduction.tex) | [sections_ja/introduction_ja.tex](../../../conceptual-topography/sections_ja/introduction_ja.tex) | 0 / 12 |
| S03 / J03 | [sections/intuitive_picture.tex](../../../conceptual-topography/sections/intuitive_picture.tex) | [sections_ja/intuitive_picture_ja.tex](../../../conceptual-topography/sections_ja/intuitive_picture_ja.tex) | 0 / 10 |
| S04 / J04 | [sections/formal_mapping.tex](../../../conceptual-topography/sections/formal_mapping.tex) | [sections_ja/formal_mapping_ja.tex](../../../conceptual-topography/sections_ja/formal_mapping_ja.tex) | 1 / 34 |
| S05 / J05 | [sections/core_equations.tex](../../../conceptual-topography/sections/core_equations.tex) | [sections_ja/core_equations_ja.tex](../../../conceptual-topography/sections_ja/core_equations_ja.tex) | 9 / 42 |
| S06 / J06 | [sections/structural_interpretation.tex](../../../conceptual-topography/sections/structural_interpretation.tex) | [sections_ja/structural_interpretation_ja.tex](../../../conceptual-topography/sections_ja/structural_interpretation_ja.tex) | 1 / 14 |
| S07 / J07 | [sections/dynamics.tex](../../../conceptual-topography/sections/dynamics.tex) | [sections_ja/dynamics_ja.tex](../../../conceptual-topography/sections_ja/dynamics_ja.tex) | 1 / 10 |
| S08 / J08 | [sections/multiscale.tex](../../../conceptual-topography/sections/multiscale.tex) | [sections_ja/multiscale_ja.tex](../../../conceptual-topography/sections_ja/multiscale_ja.tex) | 0 / 2 |
| S09 / J09 | [sections/pathologies.tex](../../../conceptual-topography/sections/pathologies.tex) | [sections_ja/pathologies_ja.tex](../../../conceptual-topography/sections_ja/pathologies_ja.tex) | 0 / 10 |
| S10 / J10 | [sections/relation_to_note.tex](../../../conceptual-topography/sections/relation_to_note.tex) | [sections_ja/relation_to_note_ja.tex](../../../conceptual-topography/sections_ja/relation_to_note_ja.tex) | 0 / 18 |
| S11 / J11 | [sections/discussion.tex](../../../conceptual-topography/sections/discussion.tex) | [sections_ja/discussion_ja.tex](../../../conceptual-topography/sections_ja/discussion_ja.tex) | 0 / 12 |
| S12 / J12 | [sections/conclusion.tex](../../../conceptual-topography/sections/conclusion.tex) | [sections_ja/conclusion_ja.tex](../../../conceptual-topography/sections_ja/conclusion_ja.tex) | 0 / 7 |

12/12 include順一致。要旨＋本文11 section、subsection/paragraphの階層・出現数も各対応fileで一致。
追加のauthority noteはJ00冒頭のみであり、ENにない理論内容ではない。
主な組版差はltjsarticle、定義/命題/注意・見出し・captionの日本語化、二つの表の列幅調整。
ノート比較表のローマ字による日本語語彙を日本語表記に戻した。ENの`chindenˆ`の余分な末尾記号は、数学ではない転写上の体裁としてcanonical JAへ複製しない。artifact identityの未解決性は保持。

## 3. Translation principles / review

ENの段落・列挙・table cells・captionを直接対応させ、数式を一時的に保護して翻訳後に元のraw textを復元した。
意味上の限定、否定、提案、local definition、非validationを保持し、抽象的語彙を観測量に変換していない。
日本語の「仮定する」はENのhypothesizedに対応する仮説記述であり、新たな数学的仮定の採用ではない。
SERIOUS対応段落・要旨・序論・結論を再読し、分離したclaimを要約で再結合していない。

MATCHは通常の翻訳として内容・強度・範囲が対応することを意味し、文字列一致ではない。
MATCH WITH LANGUAGE ADAPTATIONは語義上の注意、表の日本語化、または旧JA-only claimへのcurrent EN側の限定表現を追跡する場合。弱い日本語へ独自に改訂する分類ではない。

## 4. Mathematical / structural parity

| Check | EN | JA | Result |
| --- | --- | --- | --- |
| Displayed blocks | 12 | 12 | raw全文（環境/label含む）一致 |
| Display relation occurrences | 14 | 14 | alignの3行を別occurrenceとして集計 |
| Equation families | 14 | 14 | Phase01/07のfamily分割を保持。block数から新規分類しない |
| Inline mathematics | 202 | 202 | fileごとのraw multiset一致、式の追加・欠落・置換0 |
| label/ref/eqref commands | 45 | 45 | raw command multiset一致 |
| Figure includes | 3 | 3 | 同じpath・同じ順序 |
| Citation commands | 6 | 6 | optional argumentを含め各fileで一致 |
| Cited keys / bibliography entries | 7 / 8 | 7 / 8 | shared refs.bib、追加/削除0 |
| Duplicate labels / unresolved internal refs | 0 / 0 | 0 / 0 | source照合・最終build双方で確認 |
| Notation macros | 5 | 5 | 定義raw一致 |

### Hash method

13 fileをS00→S12の順で走査。displayはraw occurrence list、inlineはraw listをsortしたmultiset相当のlistを、UTF-8のcompact JSON（ensure_ascii=False, separators=(',', ':')）にしてSHA-256を計算した。
過去の監査が別のfile走査順で作ったhashと直接比較せず、今回のEN/JAを同じ手順で比較する。

- EN display = JA display: `b82fa64e7ddaf45e5a1b0d3cd80c004b21634ca306d5bda05926bb23e35eefcc`
- EN inline multiset = JA inline multiset: `af927c24341818245462165e5649a2967fe3a730309a9cfafef58960ef40cc66`

Inlineの並びが変わるfileはabstract、intuitive_picture、core_equations、pathologies、relation_to_note、conclusionの6件。
例: 「potentialの領域、conditionを満たす」を「conditionを満たすpotentialの領域」へ、領域を通るflow、driveを介したPhi等を日本語語順へ移動した。
式そのもの・出現数・関連付けは不変。残り7 fileのinlineは順序も一致する。
数式内の英語`constraints`や`with stability under small perturbations of`もraw数学保護のため原文通り残した。翻訳上の新たな形式条件はない。

### Family crosswalk

| EQF | Existing EN label / occurrence | JA result |
| --- | --- | --- |
| CT-EQF-001 | eq:Phi_primary | raw一致 |
| CT-EQF-002 | eq:I_evolution | raw一致 / OPEN保持 |
| CT-EQF-003 | eq:JIのflow成分 | raw一致 |
| CT-EQF-004 | eq:JIのforce成分 | raw一致 / OPEN保持 |
| CT-EQF-005 | eq:sigma | raw一致 |
| CT-EQF-006 | eq:sigma_drive | raw一致 |
| CT-EQF-007 | eq:sigma_dissipとdynamicsの反復表示 | raw一致 |
| CT-EQF-008 | eq:sigma_barrier | raw一致 / OPEN保持 |
| CT-EQF-009 | eq:coupling | raw一致 / OPEN保持 |
| CT-EQF-010 | eq:sedimentation | raw一致 / OPEN保持 |
| CT-EQF-011 | eq:concept | raw一致 |
| CT-EQF-012 | eq:understanding | raw一致 |
| CT-EQF-013 | eq:positivity | raw一致 / OPEN保持 |
| CT-EQF-014 | eq:vocabulary | raw一致 |

EN/JAは別job名main/main_ja・別auxを使用するため、式・図・節labelは同名を安全に再利用できる。JA suffixはsource filename/input pathにのみ使用する。記号・方程式identityを改名しない。

## 5. 48 frozen claim parity ledger

CLM019と044は歴史的にJA-working-onlyの強いclaimを含むfamilyである。これらをcanonical ENに存在する肯定命題と偽らない。
そのfinal DOWNGRADEに対応するcurrent ENのconditional/非identityの扱いをcanonical JAへ翻訳し、旧JA固有の強い内容は採用していない。
48 familyを追跡することと、48個の独立した肯定命題を新しい本文へ新設することは異なる。

| ID | Claim | EN locator | JA locator | Frozen disposition | Translation parity | Basis / strength protection |
| --- | --- | --- | --- | --- | --- | --- |
| CT-JACAN-001 | CT-CLM-001; 概念地形はPhiの長時間幾何 | S01:9 | J01:3 | REVISE | MATCH | モデル内の呼称と長時間/経験上の未確立性を保持。 |
| CT-JACAN-002 | CT-CLM-002; 統一方程式の認知的解クラスを同定 | S06:12 | J06:6 | DOWNGRADE | MATCH | 候補クラスであり存在・分類定理でない。 |
| CT-JACAN-003 | CT-CLM-003; Iは認知窓の未解決緊張を表現 | S04:18 | J04:10 | REVISE | MATCH | 認知窓での提案的使用、typed identity未確立。 |
| CT-JACAN-004 | CT-CLM-004; 高Iはconceptually active領域 | S04:26 | J04:15 | DOWNGRADE | MATCH | 高I/activityは比較案であり較正指標でない。 |
| CT-JACAN-005 | CT-CLM-005; Phi幾何が後続flowの方向を拘束 | S04:42 | J04:27 | REVISE | MATCH | 拡散項を含む全flowと勾配寄与を区別。 |
| CT-JACAN-006 | CT-CLM-006; conceptは局所安定領域 | S05:163 | J05:124 | KEEP | MATCH | 局所stable-region定義・摂動安定条件を維持。 |
| CT-JACAN-007 | CT-CLM-007; understandingはtraversal cost閾値条件 | S05:176 | J05:135 | KEEP | MATCH | 閾値のモデル状態定義を経験基準へ変更しない。 |
| CT-JACAN-008 | CT-CLM-008; thoughtはflow trajectory | S03:49 | J03:35 | SPLIT | MATCH WITH LANGUAGE ADAPTATION | 流れ場・軌道表現・思考の認知解釈を別文で維持。 |
| CT-JACAN-009 | CT-CLM-009; meaningは利用可能なtrajectory集合 | S03:70 | J03:48 | REVISE | MATCH | この枠組みの意味語彙、普遍的意味存在論ではない。 |
| CT-JACAN-010 | CT-CLM-010; 不可視の地形が自然な連想・突然の理解感を生む | S03:97 | J03:64 | DOWNGRADE | MATCH | 経験例との対応提案と経験生成の非説明を保持。 |
| CT-JACAN-011 | CT-CLM-011; tauは概念発展のexperiential time | S04:99 | J04:55 | SPLIT | MATCH WITH LANGUAGE ADAPTATION | 形式的順序と経験的時間を分離。経験的はempiricalの意味ではなくexperiential。 |
| CT-JACAN-012 | CT-CLM-012; 離散re-addressable unitは安定した低cost再帰に必要 | S05:76 | J05:54 | DOWNGRADE | MATCH | 再アドレス性をarchitecture上の提案要件に限定。 |
| CT-JACAN-013 | CT-CLM-013; token reuseがgradient/井戸を強化 | S05:111 | J05:87 | SPLIT | MATCH | 表式/定性的機構/typing・pairing・更新未指定を分離。 |
| CT-JACAN-014 | CT-CLM-014; communicationはsimilar landscapeの反応同期 | S03:83 | J03:56 | DOWNGRADE | MATCH | 反応類似の比較仮説であり成功から幾何を逆算しない。 |
| CT-JACAN-015 | CT-CLM-015; repeated couplingでPhi→Phi* | S05:125 | J05:92 | SPLIT | MATCH | 沈殿templateと収束結果を分離。 |
| CT-JACAN-016 | CT-CLM-016; Phi*はhistoryを反映しなお変形する | S05:149 | J05:115 | OPEN | MATCH | not necessarilyを必ずしも…ではないと訳し版・limit問題を未決のまま保持。 |
| CT-JACAN-017 | CT-CLM-017; 理解した経験は移動の容易さの変化 | S03:54 | J05:148 | DOWNGRADE | MATCH | 低コスト定義をfelt easeの独立証拠や説明にしない。 |
| CT-JACAN-018 | CT-CLM-018; I>0は通常状態として完全概念閉包を除外 | S05:199 | J05:152 | SPLIT | MATCH | 許容条件/正出力前提/保存責務と条件付き分化を分離。 |
| CT-JACAN-019 | CT-CLM-019; 正値性は常時残余勾配を保証/含意する | S05:218 | J05:164 | DOWNGRADE | MATCH WITH LANGUAGE ADAPTATION | 旧JA-only generic含意は移入せず、current ENの非pointwise・非保証・静穏の対応箇所を訳す。 |
| CT-JACAN-020 | CT-CLM-020; depth/width/curvatureが抵抗/文脈/精度を表す | S06:44 | J06:34 | DOWNGRADE | MATCH | 深さ/幅/曲率は定性的比較でありsemantic calibrationでない。 |
| CT-JACAN-021 | CT-CLM-021; ridge変形がsemantic driftを説明 | S06:62 | J06:47 | DOWNGRADE | MATCH | semantic driftは候補的動的記述、確立済み機構でない。 |
| CT-JACAN-022 | CT-CLM-022; vocabularyは安定性による集合/分布 | S06:71 | J06:52 | REVISE | MATCH WITH LANGUAGE ADAPTATION | 語彙の安定性選択集合と分布的記述を区別し確率分布にしない。 |
| CT-JACAN-023 | CT-CLM-023; 反復強化でconceptがself-sustainingになる | S07:12 | J07:19 | SPLIT | MATCH | 3段階feedbackと自己維持仮説を区別、bootstrap/updateは未解決。 |
| CT-JACAN-024 | CT-CLM-024; 忘却/想起はflattening/re-deepening | S07:38 | J07:29 | DOWNGRADE | MATCH | 忘却/想起をflatten/re-deepen類比に限定、消滅不可能とはしない。 |
| CT-JACAN-025 | CT-CLM-025; conceptual change/insightはrapid topology change | S07:80 | J07:46 | SPLIT | MATCH | 幾何/認知終点/感じられる出来事を別claimにする。 |
| CT-JACAN-026 | CT-CLM-026; 主観的突然性はtopology thresholdの反映 | S07:84 | J07:48 | DOWNGRADE | MATCH | 突然性は閾値描像との仮説であり命名による説明でない。 |
| CT-JACAN-027 | CT-CLM-027; effective barrierはbelief revision抵抗を説明 | S07:71 | J07:41 | DOWNGRADE | MATCH | effective抵抗であり認知的禁止を導出しない。 |
| CT-JACAN-028 | CT-CLM-028; 個体→社会で同一力学、支配costのみ交替 | S08:35 | J08:26 | SPLIT | MATCH | トークン役割比較と同一 dynamics・集約・typed mapを区別。 |
| CT-JACAN-029 | CT-CLM-029; shared inputsがcorrelated wells/shared landscapeを生成 | S08:43 | J08:29 | DOWNGRADE | MATCH | 共有入力と類似priorの条件付きsocial hypothesis。 |
| CT-JACAN-030 | CT-CLM-030; norms/institutionsはcollective attractor | S08:55 | J08:37 | DOWNGRADE | MATCH | 制度とattractorは構造類比であってidentityでない。 |
| CT-JACAN-031 | CT-CLM-031; 制度安定はcentral authority不要、well depthから従う | S08:60 | J08:39 | SPLIT | MATCH | depth/stability仮説とhistorical説明・独立criterionを分離。 |
| CT-JACAN-032 | CT-CLM-032; overclosure/underclosureがrigidity/unstable thoughtに対応 | S09:32 | J09:21 | DOWNGRADE | MATCH | 非診断・非臨床・非必要十分条件を明記、underclosureは閉包不足。 |
| CT-JACAN-033 | CT-CLM-033; subjective experienceを生成/説明しない | S09:19 | J09:12 | KEEP | MATCH | 主観的経験を生成・説明しないnegative scopeを保持。 |
| CT-JACAN-034 | CT-CLM-034; neural implementationはfuture work | S09:28 | J09:18 | KEEP | MATCH | 神経実装への対応は将来課題。 |
| CT-JACAN-035 | CT-CLM-035; sync breakdownはcommunication failure/polarizationの構造基盤 | S09:51 | J09:36 | DOWNGRADE | MATCH | 分極化等は比較候補で測定領域や幾何のみからの推論でない。 |
| CT-JACAN-036 | CT-CLM-036; parameters/observable correspondence/individuation未指定 | S11:40 | J11:24 | KEEP | MATCH | K/parameters/individuation/social/neuralの欠落を保持。 |
| CT-JACAN-037 | CT-CLM-037; L3がL1 noteを理論的に支える | S10:11 | J10:6 | SPLIT | MATCH WITH LANGUAGE ADAPTATION | ノート表のローマ字を日本語表記へ適応。CT-local比較・非検証・exact artifact未決を維持。 |
| CT-JACAN-038 | CT-CLM-038; Consciousness note CPU/GPUと将来fast/slow対応 | S10:59 | J10:45 | REVISE | MATCH | current sourceとolder note版関係の未解決、比較のみを保持。 |
| CT-JACAN-039 | CT-CLM-039; intelligenceはshared landscape維持の分散過程 | S08:79 | J08:52 | SPLIT | MATCH | 社会的知性のlocal機能呼称を一般知性の成立や定義にしない。 |
| CT-JACAN-040 | CT-CLM-040; quantizationとstructurally isomorphic、quantum主張は否定 | S04:108 | J04:60 | SPLIT | MATCH WITH LANGUAGE ADAPTATION | 量子化という名称の非形式的類比と数学的同型/量子理論の非主張を保持。 |
| CT-JACAN-041 | CT-CLM-041; distributional semanticsと使用history/共起の違い | S11:20 | J11:11 | REVISE | MATCH | use/co-occurrenceの概念的比較のみ、優位性/corpus/mapなし。 |
| CT-JACAN-042 | CT-CLM-042; driveはprediction error influx、deepeningはerror minimization | S11:31 | J11:20 | REVISE | MATCH | prediction-error/free-energy変数の同一性を否定。 |
| CT-JACAN-043 | CT-CLM-043; concept/particleはsame generative grammarのprojected regimes | S12:68 | J12:38 | SPLIT | MATCH | projected stabilization比較と共通方程式/量/場/typed translationを分離。 |
| CT-JACAN-044 | CT-CLM-044; concept/particleは同一基礎方程式の解クラス | S12:70 | J12:39 | DOWNGRADE | MATCH WITH LANGUAGE ADAPTATION | 旧JA-only同一方程式解クラスを移入せずcurrent ENのheuristic/非identity guardを訳す。 |
| CT-JACAN-045 | CT-CLM-045; Phiはmeaning fieldでなくtokensはmeaning unitsでない | S04:120 | J04:68 | KEEP | MATCH | Phi非意味場、JI非内容、token非意味単位と方法論的範囲を保持。 |
| CT-JACAN-046 | CT-CLM-046; thoughtにdirecting subjectを必要としない | S02:87 | J02:51 | KEEP | MATCH | モデル内でdirecting subject不要という範囲を維持。 |
| CT-JACAN-047 | CT-CLM-047; drive/decay/barrierはinput/forgetting/overclosure抵抗 | S05:59 | J05:45 | REVISE | MATCH | source termsの有効な認知的解釈を測定機構にしない。 |
| CT-JACAN-048 | CT-CLM-048; general variablesを再定義せずcognitive projectionとして使う | S00:85 | J00:92 | SPLIT | MATCH WITH LANGUAGE ADAPTATION | 非再定義/認知的使用/出典版とtyped継承未決を分離。 |

全48を一度ずつ確認。KEEP7のlocal定義・除外範囲は弱めず、REVISE9/DOWNGRADE17/SPLIT14/OPEN1は現行EN実装に従う。
要旨・序論・結論の「候補」「モデル内」「提案」「未解決」「非検証」を保持し、旧JA文の「同じ方程式」「経験される意味」等をsummaryに挿入しない。

## 6. Formal OPEN / serious protection

| Target | Canonical JA location | Protected boundary |
| --- | --- | --- |
| EQF002 | J05 §4.1 | template。domain/IC/BC/regularity/positive preservation未指定。存在・一意性・well-posedness未確立 |
| EQF004 | J05 §4.1 | 負勾配のforce定義とlocal/effective特殊化を分離。一般畳み込みからの導出を主張しない |
| EQF008 | J05 §4.1 | 逆数発散とboundary inaccessibility/invariant domainを区別。符号・上限正規化等を採用しない |
| EQF009 | J05 §4.2 | 数値/vector実現・dot pairing・L項の種類・parameter未決。Euler–Lagrange/updateを導出しない |
| EQF010 / CT-FINAL-016 | J05 §4.3 | long-time template、mode未決、limit/renewed-input reshaping・version intent未決。「必ずしも一意または静的ではない」を採り、旧JA categorical句は採らない |
| EQF013 | J05 §4.5 | admissibility/positive-output premise/dynamical preservationを別責務へ。positiveだけでgradient/flow非零やinnovationを保証しない |
| SERIOUS001 | J03 §2.1 / J05 §4.4 | 理解local定義とfelt ease仮説を分離。定義は独立証拠/経験説明でない |
| SERIOUS002 | J07 §6.4 | geometry/topology、cognitive resolution、subjective suddennessを分離 |
| SERIOUS003 | J08 §7.3 | attractor類比、depth/stability仮説、歴史的説明・独立criterionを分離 |

SERIOUS3はImplementation05のRESOLVED BY IMPLEMENTATION（構造的）を保持、retained0/resolved3。
新しい経験的基準・較正・metric・spaces・units・IC/BC・kernel・token embedding・variational dynamics・convergence mode・positivity proofは導入しない。
Global equation-change requirementはOPEN。今回の数学的複製は式改訂または形式的closureではない。

## 7. JA working divergence ledger

working全文と主要差を参照したが、本文生成元はENのみ。working MDのhashはtask-start不変。

| Working locator / unique item | Classification | Canonical JA handling |
| --- | --- | --- |
| MD:262–264 Phi-star「一意でも静的でもない」旧解釈 | AUTHORITY OPEN | working内の保留記述に留め、ENのnot necessarilyとversion未決を翻訳 |
| MD:89 再帰的再入可能性をconcept解釈へ追加 | KEEP IN WORKING ONLY | ENにあるlow-cost re-entryの動機だけ訳し、concept定義へ追加条件を移さない |
| MD:142 経験される意味を下流解釈とする案 | KEEP IN WORKING ONLY | ENの「この枠組みで意味と呼ぶもの」を訳し、経験的意味の固有案を挿入しない |
| MD:196 Qを量子力学の離散固有値操作と比較する詳細 | SAFE TO TRANSLATE ONLY IF EN EQUIVALENT EXISTS | ENの連続→離散のinformal analogyと非isomorphism/非quantum claimだけを翻訳 |
| MD:458 「過開放」の名称 | KEEP IN WORKING ONLY | EN underclosureを「閉包不足」と訳し、別の過開放概念を導入しない |
| MD:289 旧generic positivity chainへの言及 | DOCUMENTARY NOTE ONLY | ENのnonpointwise guardと条件付き分化を訳す。旧chain自体を新数式として挿入しない |
| MD:239付近 hard barrier/prohibitionの旧強度 | SAFE TO TRANSLATE ONLY IF EN EQUIVALENT EXISTS | current ENのeffective resistanceと不変領域未証明だけを翻訳 |
| MD:577 同一情報場/同一基礎方程式の解クラスという旧強度 | DOCUMENTARY NOTE ONLY | current ENのprojected-regime比較・heuristic grammar・非shared equationを訳す |
| MD:524 最小公理/groundingの旧主張の限定 | SAFE TO TRANSLATE ONLY IF EN EQUIVALENT EXISTS | ENのsource reuseはaxiomからの導出/機構確立でないとの文を訳す |
| MD:485–497 note tableの独自式・表記差 | KEEP IN WORKING ONLY | EN tableの数式をそのまま複製。workingの追加inline/式shapeを採らない |

既存working14 display / inline158をcanonicalの基準にせず、EN12 display / inline202に従った。
JA workingの削除・上書き・status banner追加は不要であり行っていない。
canonical JAの新設で古いnote/Master provenanceやPhi-starの意図が解決したわけではない。

## 8. Terminology

| EN | Canonical JA usage |
| --- | --- |
| Conceptual Topography / conceptual landscape | Conceptual Topography（CT、概念地形）/ 概念地形 |
| information potential | 情報ポテンシャル |
| unresolved conceptual tension | 未解決の概念的緊張 |
| flow field / trajectory | 流れ場 / 軌道（経路の描像とは必要に応じ区別） |
| token / re-addressable | トークン / 再アドレス可能 |
| sedimentation / closure | 沈殿 / 閉包 |
| overclosure / underclosure | 過閉包 / 閉包不足 |
| attractor / correspondence | アトラクタ / 対応 |
| projected regime | 投影された領域 |
| model-level / schematic | モデルレベル / 模式的 |
| phenomenological correspondence | 現象学的対応（現象的対応という読みも同じ限定内） |
| experiential time | 経験的時間（experienced、時計較正やempirical dataの意味ではない） |
| typed translation | 型を明示した翻訳 |
| independent criterion / operational mapping | 独立した基準 / 操作的な対応写像 |

語感のために因果的・経験的な成立へ強めない。用語選択はENの内容を限定/拡張する新定義ではない。

## 9. Figures / captions

図assetは編集も再生成もせず、3 PNGを同じ順序・同じパスで使用。
PDFから取り出した画像をRGBへ変換し、元PNGとのpixel hash一致を確認した。

| Figure | JA PDF page | Caption protection | Embedded pixel SHA-256 |
| --- | --- | --- | --- |
| FIG001 | 7 | 模式/例示、JI場と描画pathを非同一、非measured path、cognitive proposed | a4bd61234dc5b8a0196b720867554952e6ea6a8882fac20124f73328997f31b5 |
| FIG002 | 12 | coupling hypothesis、非simulation、非executed/derived、token実現/pairing未決 | 32dd49a21fb5eb35cc4a391f4fe161ff507fe14a6f6455955502ae462f3a7957 |
| FIG003 | 13 | proposed feedback/ordering、非causal proof/非executed witness、既存JI表記維持 | 1c7b52a66ef2a4d511eae20bcf1013a9440baa83edd981b4e8122b9c14a794b0 |

英語の図内labelを意図的に保持。日本語label版の新設は別タスクとして未実施。
FIG003の短いlegend（motion along gradient等）の孤立読みに関する既存advisoryは、caption/bodyの限定と併せて保持する。翻訳により図を独立証拠へ昇格していない。

## 10. Bibliography / references

既存shared `refs.bib`、style `plainnat`、BibTeXを再使用。8 entriesのうち7 keysをEN/JA双方で引用:
`IFGT, VED_vol1, VED_vol2, VED_vol3, VED_vol4, friston2010free, thelen1994dynamic`。
引用コマンド6件、optional argument `[e.g.,][]`を含め原文保持。
BibTeX SHA-256: `54c7a17b14d07443356266c39a17dd1c82b3a56a421e2b69ad9ec00bff0fb715`。
新規文献・引用追加・reference転用なし。最終aux/sourceで未解決ref/citeなし。
ENと同じlabel番号を別job内で使用。共有auxのcollisionなし。

## 11. Build route / artifacts

repository既存のbio-ifgt/main_ja.tex、consciousness等の日本語論文と整合する **LuaLaTeX / LuaTeX-ja / ltjsarticle** を採用。
TeX Live 2025、LuaHBTeX 1.21.0、latexmk 4.86a。
日本語fontはTeX配布済みHaranoAjiMincho-Regular / HaranoAjiGothic-Medium。
欧文・数式はENのPalatino/T1および既存AMS構成を保持。font binary追加・download・system設定変更なし。

作業directory: `conceptual-topography/`。
実行command:

```bash
latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=${TEMP_EVIDENCE_ROOT}/ct_jacan.U6hyjT/build main_ja.tex
```

latexmkがLuaLaTeX/BibTeX/参照解決の再runを管理。exit status **0**。
補助生成物はtmpのみに置き、視覚検査合格後のPDFだけを`conceptual-topography/main_ja.pdf`へcopy。
通常の再build commandはbranch READMEに`latexmk -lualatex -interaction=nonstopmode -halt-on-error main_ja.tex`として記載。
新しいbuild system、latexmkrc、system-wide config、package installは不要。

初回buildでltjsarticleとmicrotypeのfont-size preset警告、表の3pt overfullを確認し、日本語entryでのみmicrotypeを外し、変数表の列幅を0.48から0.46 textwidthへ調整した。
ノート比較表は日本語行送りに対応するp列を使用。EN TeXには反映していない。
最終log: overfull **0** / underfull **0** / missing character **0** / undefined reference/citation **0**。
残存warningはcaptionのunknown-class/default選択1件、4.5pt→5ptの既存math font substitution3件＋集約1件。
BibTeXには既存5文献のempty institution warningが残る。書誌内容を補修する権限はなく、変更しない。
これらは目視で欠落・clippingを生じていないことを確認しadvisoryとして記録する。

JA PDF: **23 pages**, A4, **5,162,471 bytes**。
SHA-256: `63641c9c35c6f07b8cceae4e14cbe70bb7c87f365662b5be18ae6f2dc6f63229`。
EN PDF: 22 pages、開始hash不変 `c16f737651b79cfbafcf75353ee7642633e8847485dc64aa87db4cd2bd22acbc`。
最終JA log SHA-256: `976c58fe32e1e1a5a2aaa3e99d8e8fa40e07ab9ef6906652d565db315a565521`。
最終BibTeX log SHA-256: `64cf34ac97849c617acd042ded7d2ff6499b26e1aada3caf381ca2405936078f`。

## 12. Full-page visual inspection

PDF skillに従い、compile成功だけで完了とせず、Popplerで最終buildの**23/23頁**をPNGへrenderして全頁を直接目視した。
render command: `pdftoppm -scale-to 1250 -png ${TEMP_EVIDENCE_ROOT}/ct_jacan.U6hyjT/build/main_ja.pdf ${TEMP_EVIDENCE_ROOT}/ct_jacan.U6hyjT/page`。
PDF text extractionはページ/画像/参照の補助確認にのみ使用した。

| Pages | Inspected content | Result |
| --- | --- | --- |
| 1–2 | 日本語title、author、authority note、scope、要旨、inline math | 字形・数式・引用・行組み読取可。要旨継続page2に余白あり |
| 3–4 | 全目次、11本文sectionとsubsection、頁番号 | 参照・日本語・heading hierarchy一致。page4に余白あり |
| 5–6 | 序論、series table、6claims、本文参照、直観 | 欠落/重なりなし |
| 7–8 | FIG001、caption、field/path区別、意味、GPU、potential | current図とcaption一致、式(1)読取可 |
| 9–10 | 変数table、Q注意、negative scope、formal template、flow | 表clippingなし。小さいscript含む式・記号読取可 |
| 11–12 | source terms、coupling、FIG002、sedimentation、concept定義 | 機構hypothesis/typing未決保持。数式内英語は意図的raw保持 |
| 13–14 | FIG003、理解定義/独立criterion、positive guard、構造table | JIとcaption一致、式/定義/表読取可 |
| 15–16 | attributes、vocabulary、sedimentation/forgetting/insight | 数式(13)(14)とprose分離確認 |
| 17–18 | suddenness、social、institution、intelligence、negative scope | 三つのSERIOUS backedge分離を確認 |
| 19–20 | scope、note tableと限界 | 表は単頁内に収まりclippingなし。表前に余白あり |
| 21–23 | note handoff、discussion、conclusion、bibliography全7件 | refs/glyph欠落なし、結論の非identity・非validation保持 |

内容を隠す重なり、欠字、未解決参照、式の欠落は未検出。
ENに対応するfront matterの余白、図floatに伴う文の改頁、表を分割しないための余白は軽微な組版advisoryとして保持。
captionの模式性・非測定性を弱めるために文章を削ることはしない。
JA distributionは**FRESH WITH ADVISORIES**。ENを再buildせず、既存FRESH WITH ADVISORIESを維持。

## 13. OPEN / ceiling preservation

22研究familyはすべて研究上OPENのまま。日本語translation対応とCT-U-193解消はdocumentary subissueであり、family closureではない。

| OPEN IDs | Preserved research burden |
| --- | --- |
| 001–004 | geometry/domain/kernel、field/path/behavior、I/C/input/activity、concept individuation/attributes |
| 005–007 | understanding/transfer、phenomenal endpoint、time mapping |
| 008–011 | token/Q/coupling/bootstrap、Phi-star/sedimentation/memory、meaning/category/drift、vocabulary/S |
| 012–015 | positivity/reactivation、barrier/pathology、collective aggregation、institution/depth |
| 016–018 | communication/similarity、intelligence scope、typed cross-scale translation |
| 019 | source/version/citation authority。JA翻訳の新source statusは確定したが、older note/Master等は未解決 |
| 020–022 | test execution、neural map、figure/presentation correspondence。図再利用は経験的証拠ではない |

Evidence ceilings: **CE2 / SE2 / COG2 / PCE2**。
Correspondence ceilings: **COR3 / SM3 / CM3 / PM1 / SOM3 / X3**。
Operational maps / empirical datasets / tested predictions / validated predictions: **0 / 0 / 0 / 0**。
翻訳・build・render・数学照合をempirical testやsimulationとして集計しない。

## 14. README / CT-U-193

[branch README](../../../conceptual-topography/README.md)を、canonical EN/JA、working保持、二言語PDF、LuaLaTeX route、独立監査完了へ同期した。
古い「Independent post-implementation consistency audit has not started」を削除し、実際のPASS WITH ADVISORIES / CLOSED WITH ADVISORIESに更新。
**CT-U-193はDOCUMENTARY RESOLVED**。元I05台帳は変更せず、このrecordが後続解消記録となる。

[audit README](../README_ja.md)にはJapanese cycleの独立status/linkを追加。
旧Phase00–07/Implementation01–05の当時「canonical JA not located」等は履歴として残し、現在statusとは区別する。
既存193 uncertainty IDを保持し、新規IDは作らない。
現在の集計: STILL OPEN165 / DOCUMENTARY RESOLVED3 / SCOPE RESOLVED16 / IMPLEMENTATION VERIFIED9 / REOPENED0 / NEW0 = **193**。
研究family countは22のまま。

## 15. Validation / task delta

- entry + 12 sections存在、include orderと見出し階層対応。
- CT-JACAN-001–048重複・欠番なし、disposition7/9/17/14/0/1を保持。
- raw display12/12、inline202/202、14 EQF、refs45/45、citation commands6/6、keys7/7、figures3/3。
- 未解決ref/cite0、duplicate label0、notation macro5一致。
- 6 EQF OPEN、CT-FINAL-016、SERIOUSの構造分離、22研究OPEN・ceilings・0/0を保持。
- 開始hash比較で既存変更はREADME2件だけ。全保護対象・他branchのdirty内容を保持。
- repository内の新設は許可された15件のみ。aux/log/cache/render/helperはtmpのみ。
- JA build exit0、PDF23/23頁目視、embedded image3/3画素一致。
- git diff --check: PASS。新規TeX/recordも別途末尾空白・conflict marker・marker残留検査。
- git status --shortは開始時の大量dirtyを保持。開始246行（M241/??5）から249行（M241/??8）へ。追加表示はmain_ja.tex / main_ja.pdf / sections_ja/。新recordは既存untracked notes/ct_audit/内。
- commit / push: 未実施。

最終検査結果: **PASS**。1474→1489 files、新設15件、既存変更README2件のみ、残る既存1472件はtask-start SHA-256と一致。
48 claim ID/primary disposition/parity件数、全relativeリンクの実在、12節の数学・参照・引用・見出し対応、許可path制限、TeXの未復元marker・conflict marker・末尾空白なしを検証した。
git status --shortは249行（M241 / ??8）。git diff --checkはexit0。最終PDF hashも上記と一致する。

## 16. Stop boundary

Japanese canonical TeX / JA distribution cycleを完了して停止する。
追加の理論改訂、equation resolution、研究OPEN解決、external research、simulation、commit/pushへは進まない。

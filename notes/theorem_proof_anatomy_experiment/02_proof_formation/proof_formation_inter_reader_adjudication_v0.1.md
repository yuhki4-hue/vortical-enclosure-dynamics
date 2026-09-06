# Proof-Formation Inter-Reader Adjudication v0.1

- **Role:** independent inter-reader adjudication of Reader 02 and Reader 03
- **Unit:** frozen parent items E01–E12, with subepisodes used only where the source supports them
- **Purpose:** classify differences and decide whether the transition core is reconstructible enough to enter Phase 0
- **Not performed:** score, percentage, kappa, ranking, winner selection, framework revision, new move code, new field schema, geometry, general law, or theorem claim
- **Date:** 2026-09-05

Reader 02 の self-adjudication と blind comparison は、論点発見の索引としてだけ使用した。そこにある結論は authority とせず、frozen packet、coder instructions、adjudication rules、および下記の限定的 source return から再判定した。

## 0. Adjudication classification and source-return record

本報告では次の分類を用いる。複数該当時は primary / secondary を明記する。

- **A. SOURCE-RESOLVED:** source wording、exact before/after、explicit verdict から一意に決まる。
- **B. GENUINE SOURCE AMBIGUITY:** source 自体が複数の reading または segmentation を許す。
- **C. PACKET DEFECT:** frozen packet に必要情報がなく、blind reader には決められない。
- **D. FRAMEWORK BOUNDARY:** source は読めるが、現行 field、M1–M17、role distinction では自然に表しにくい。
- **E. READER-SPECIFIC RECONSTRUCTION:** source-compatible な複数 reconstruction の一つ。
- **F. CODER ERROR:** source と reader-facing instructions から訂正できる reader-side error。
- **G. NOT ENOUGH EVIDENCE:** packet にも指定 original source にも十分な根拠がない。

### 0.1 Limited source return

source return は shared gap が packet 欠落か source 自体の欠落かを分けるためにのみ行った。

| Adjudication point | Returned source | Finding |
|---|---|---|
| E06 Null C/D/E、Erasure、case reversal と taxonomy deletion の根拠 | `deferred_resolution_case_01_gst.md`; `deferred_resolution_case_01_gst_v0.1_to_v0.2_diff.md`; `deferred_resolution_case_01_gst_v0.2.md` | Null C/D/E の内容、Erasure Test の negative result、旧 taxonomy の異種尺度混在と field-native scale 不在は source にあり packet にはない。 |
| E07 preregistered §5–§6、M0–M3、real-record question | `scientific_assurance_case_02_metrology_preregistration.md`; `scientific_assurance_case_02_metrology_comparison.md` | F1–F6、七つの success conditions、M0–M3 定義、将来の real-protocol audit は source にあり packet にはない。後者は proposal であり completed move ではない。 |
| E09 P0 reframing と P1-reduced の具体結果 | `p0_generic_standards_baseline_v0.1.md`; `p1r_noneval_two_field_check_v0.1.md` | 「比較研究プログラム」から限定的な一記述形式の問いへの変更、検索訂正、確定値、artifact/governance explanation、n=1、kill criteria は source にあり packet にはない。 |
| E10 21-theorem comparison と C1–C3 | `godel_incompleteness_closure_reversal_stress_test_ja.md` | compactness、Banach、Stokes/Gauss–Bonnet との具体比較と local kill criteria は source にある。全21 case の内容と一般的 C1–C3 ladder 定義はこの source にも揃わない。 |
| E11 S1/S2/S2* と subject shift | `reflection_principles_scope_stress_test_ja.md` | S2 kill test、S2* の local-only meaning、same-`T` と external `T+` の差は source にある。一般的 S-ladder の完全定義はない。 |
| E12 S/A ladders と calibration package | `proof_theoretic_ordinal_stress_test_ja.md` | local S2* / A2 verdict の意味、複数 characterization、PA の concrete package は source にある。単一の universal fixed package と完全な S/A ladder は source 自身が固定していない。 |
| E08 answer key が参照する C-1/C-2 | `hydrology_negative_knowledge_preservation_note_v0.1.md`; `hydrology_negative_knowledge_preservation_note_v0.2.md` | 二件の factual correction は source にあり packet にはない。packet が提示する effectiveness transition は C-3 だけである。 |

source return で得た packet 外情報を blind reader の誤り判定へ遡及使用しない。

## 1. Blindness and protocol integrity audit

### Reader 02 — **VALID BLIND RESULT**

- Reader output 自身に、許可された二ファイルだけを読んだこと、original source へ戻らなかったこと、answer key、adjudication、meta-experiment、他 reader を読まなかったことの明示的 isolation record がある。
- file chronology でも Reader 02 output は Reader 02 self-adjudication、Reader 03 output、blind comparison より先に作成されている。chronology は内容非閲覧の完全証明ではないが、自己申告と矛盾しない。
- packet にない ladder、witness、reduced-check details を UNKNOWN のまま残しており、answer-key leakage を示す内容はない。
- 有限濃度の counting argument は packet の式からの明示的 INFERENCE で、欠落を外部知識で埋めたものではない。
- 後に self-adjudication material を見たことは、既に固定された blind output を汚染しない。self-adjudication note 自体には独立裁定としての地位を与えない。

### Reader 03 — **VALID WITH LIMITATION**

- output は input を coder instructions と frozen corpus の二ファイルだけと明記し、original source の packet 外 details を埋めずに UNKNOWN としている。内容面に answer-key leakage の徴候はない。
- ただし Reader 02 self-adjudication が既に workspace に存在した後に Reader 03 file が作成されており、Reader 03 には Reader 02 のような詳細な isolation chronology がない。「二ファイルだけ」という自己申告を否定する証拠はないが、非閲覧を独立に監査できない。
- blind comparison は Reader 03 output より後に作成されており、blind result 自体を汚染しない。
- source にない future branch を一部 `OPEN HYPOTHESIS` とした箇所は coder-side provenance 問題であり、blindness invalidation の証拠ではない。

したがって Reader 03 を INVALID にはしない。ただし formal blindness の監査可能性には限定が残る。

## 2. Parent-level transition-core adjudication

segmentation の数ではなく、parent-level の before / principal witness / withdrawal or demotion / remnant / terminal direction を比較した。

| Parent | claim_before core | Principal failure witness | Principal withdrawal / demotion | Retained remnant / side claim | Terminal direction | Judgment |
|---|---|---|---|---|---|---|
| E01 | 非単射写像から新しい一般的 nonuniqueness theorem を得る | prior-art absorption と `O=id_W` | general novelty/theorem claim を撤回 | observational equivalence と structural isomorphism の区別、model/experiment-relative identifiability | general claim withdrawn; relative distinction established | **CORE CONVERGENCE** |
| E02 | self-containment alone から universal non-identifiability | finite encoder、infinite cardinality、quine/Kleene、既存 impossibility results の追加条件 | universal implication を撤回 | self-containment は追加前提を成立させうる；finite capacity proposition は別の conditional result | original withdrawn; qualitative remnant and conditional proposition retained | **CORE CONVERGENCE** |
| E03 | staged generation-to-log structure だけから general non-isomorphism | conclusion-as-definition、reversible/full encoding countercase、既存情報比較語彙 | stage-existence implication を撤回 | concrete channel 等で loss を証明する必要、Blackwell information と physical joint measurement の区別 | universal claim withdrawn; methodological distinctions established | **CORE CONVERGENCE** |
| E04 | destructive two-bit example を internality-specific impossibility として使う | matched external observer でも同じ obstruction、fresh preparation、prior art | internality-specific use を撤回 | pairwise `∀∃` と global `∃∀` の差；bridge conditions は setting-dependent | attribution withdrawn; quantifier gap retained; synthesis open | **CORE CONVERGENCE** |
| E05 | informal “same interface” から general internal/external history equivalence | stipulative equality と implementation-existence の混線、interface underspecification | general `[ESTABLISHED]` を撤回 | definitional convention と controlled-transition/state-map conditional correspondence | general claim withdrawn; two differently qualified successors retained | **PARTIAL CONVERGENCE** — Reader 03 は明示的な spatial inside/outside withdrawal を terminal record に残していない |
| E06 | GST を positive Deferred Resolution case / independent mechanism とする | iterative chain 不支持、Null/Erasure、field-native reconstruction | positive verdict を frozen negative へ；mechanism demotion；taxonomy deletion | technical content は field-native terms で保持 | negative fixed; mechanism demoted; taxonomy deleted; technical remnant retained | **CORE CONVERGENCE** — grouping は違うが parent core は同じ |
| E07 | generic audit が field-native control より早く／明確に diagnostic difference を出す H1 | new finding / judgment change がなく presentation だけ変化 | diagnostic/methodological added value を not supported と固定 | organizational / cross-chain visibility value | H1 negative; organizational value retained | **CORE CONVERGENCE** |
| E08 | documentary chain が preservation effectiveness / forgetting prevention を示す | N-04 との内部矛盾、effect outcomes 未測定 | effectiveness expression を削除し untested へ | documentary continuity / rediscoverability | efficacy withdrawn/untested; continuity retained | **CORE CONVERGENCE** |
| E09 | full P1–P5 viability、その後の reduced comparative-methodology viability | P0 の 14→1 narrowing と P1-reduced の second premise failure | full design を abandon、後に comparative methodology を terminate | reduced search を一時採用し、comparative review のみ保持 | two-stage narrowing then termination/demotion | **CORE CONVERGENCE** |
| E10 | “closure reversal” が Gödel の独立分類／diagnostic tool になりうる | standard concepts より低い resolution、mechanism discovery に寄与しない | C2/C3 を拒否し negative result を固定 | post-analysis explanatory comparison metaphor として C1 | novelty/diagnostic claim denied; C1 retained | **CORE CONVERGENCE** |
| E11 | broad S2 “self-assurance” を local/uniform/global/soundness にまたがって使う | type、language、formula scope、metalevel、subject shift の差 | broad S2 を S2* へ demote | local reflection に限る comparative use | limited survival, not total kill | **CORE CONVERGENCE** — technical material の episode 化は parent core を変えない |
| E12 | universal ordinal scalar；別軸で architecture novelty の可否 | equal ordinal の非含意群；standard metamathematical distinction で十分 | universal scalar を拒否；A3 へ上げない | fixed-package natural-family calibration S2*；standard A2 architecture feature | scalar restricted; architecture retained but not novel | **PARTIAL CONVERGENCE** — A-axis の before を Reader 02 は UNKNOWN、Reader 03 は INFERENCE で補う |

parent-level に **CORE DIVERGENCE** または **NOT COMPARABLE** はない。これは agreement の集計ではなく、全 parent で主要 transition direction を比較可能だったという qualitative finding である。

## 3. Segmentation adjudication

| Item | Reader 02 segmentation | Reader 03 segmentation | Source-explicit boundary | Source-underdetermined boundary | Move coding effect | Terminal-status effect | Classification |
|---|---|---|---|---|---|---|---|
| E02 | withdrawal/remnant `a` + conditional capacity `b`; single-block alternative retained | 同じ二分；boundary を source-derived とする | Excerpt 3 の withdrawn/established pair と、Excerpt 4 の独自 assumption set | 「条件付き命題は残る」が同じ after branch か別 successor episode か | 統合時は M1/M4 が同じ block に入り、分割時は conditional branch の move になる。E02-a の M2/M14 差自体は境界だけでは決まらない | parent status 不変 | **Primary B; secondary D**（cross-subepisode linkage） |
| E04 | single；quantifier-gap establishment / internality-attribution withdrawal の split alternative | single | Excerpt 4 の `[WITHDRAWN]`、`[ESTABLISHED]`、`[SYNTHESIS]` は別 status | two-bit construction を positive result と withdrawn use の共通 material とするか | split すると M14/M15/M17 の配置が変わる | parent status 不変；subepisode ごとの status 配置のみ変化 | **Primary B; secondary E** |
| E05 | `a`: general withdrawal + definitional/implementation replacements；`b`: spatial inside/outside withdrawal | `a`: general withdrawal；`b`: convention；`c`: implementation。spatial withdrawal の独立 terminal record なし | 一つの general withdrawal、番号付き二 replacement、さらに spatial condition の別 `[WITHDRAWN]` が明示 | replacement を one/two/three blocks にするか；spatial withdrawal を独立 episode にするか同じ revision の after にするか | definitional branch の M1/M2/M14、implementation branch の M1/M4/M7/M8/M10 の配置が大きく変わる | general/convention/implementation statuses は同じ。spatial withdrawal は Reader 03 で欠落 | Boundary: **Primary B; secondary D**。Spatial withdrawal omission: **Primary F, source basis A** |
| E06 | case verdict / mechanism / taxonomy の三分 | case verdict / mechanism+taxonomy の二分 | v0.1→v0.2 verdict と変更リストの三対象は明示 | bullets を一 revision とするか別 transitions とするか | taxonomy を独立させると M17 のみで witness UNKNOWN；統合すると M15 context が及ぶ | parent status は同じ | **Primary B; secondary C**（taxonomy-specific reason packet-missing）、**D**（taxonomy deletion fit） |
| E08 | single；sentence deletion / verdict relabel の二分 alternative | single | packet には C-3 deletion と verdict relabel が別記録としてある | 同じ N-04 witness を共有する one change か two changes か | primary coding は双方 M2/M14/M17。split 時に配置だけ変化 | parent status 不変 | **Primary B; secondary C**。C-1/C-2 を含む key segmentation は packet-inaccessible |
| E10 | single；Gödel II を別 episode とする案を却下 | single；alternative なし | Gödel I、Gödel II、C1 verdict は claim type と section が別 | theorem exposition を formation episode とするか、C1 judgment の analysis object/resource とするか | 独立化すれば M12 が可能；meta-vocabulary episode なら非coding | C1 terminal status は不変；数学的 statements に別 status を付すかだけが変わる | Substance: **Primary D; secondary B**。Step 0 で boundary-dependent alternative を残さなかった点は両 reader の **F (minor procedural)** |
| E11 | single S2→S2*；`T→T+` を resource として非coding | `a`: label judgment；`b`: technical reflection correction；integrated alternative retained | S2→S2* label judgment と external stronger-theory construction / subject shift は明示的に別 claim identities | technical correction が独立 formation transition か label judgment の evidence か | 独立時 M6/M12/(M3)；統合時は resource/analysis object | S2* status 不変；Reader 03 だけ technical after-claims を established とする | **Primary D; secondary B**。Reader 02 が alternative を segmentation 欄へ残さなかった点は **F (minor procedural)** |
| E12 | `a`: scalar/S judgment；`b`: architecture/A judgment | 同じ二分 | source に別の `判定: S2*` と `判定: A2` block | A2 block が before→after transition か初回 classification か | E12-a/b 間では move を混ぜない。A-axis 内の M12/M15 は transition 読みに依存 | S2* と A2 は双方同じ。A-axis の prior status は UNKNOWN | Split: **A**。A-axis transitionality: **Primary D; secondary G** |

### 3.1 Focus findings

- **E05:** general withdrawal、definitional convention、conditional implementation correspondence はいずれも source-explicit だが、analytic boundary は一意でない。spatial inside/outside withdrawal は boundary が曖昧でも記録自体は省略できない。
- **E06:** case verdict、mechanism demotion、taxonomy deletion は terminal objects が異なる。これらを別 episode とするか一 revision とするかは source が決めないが、taxonomy deletion の理由が packet にないことは別問題である。
- **E11:** S2→S2* label judgment と `T→T+` reflection construction は subject が異なる。独立 episode 化の可否こそが M6/M12 差の原因であり、code を先に裁定してはならない。

## 4. Move-coding adjudication

単純な code-set 一致ではなく、同じ source operation がどこに置かれたかを裁定した。

| Focus | Reader difference | Difference type | Adjudication |
|---|---|---|---|
| E02-a: M2 vs M14 | Reader 02 は enabling と entailing の type correction として M14。Reader 03 は universal sufficiency から premise-enabling remnant への M2 | **optional co-code difference**、かつ code-versus-side-claim identity difference | retained remnant を元 claim の weakening と見るなら M2、別 side claim と見るなら M14 が自然。**Primary E; secondary D**。どちらも M17 は同じ。 |
| E05 general correction | 両者 M14/M17 | **same move under same boundary** | source-resolved。一般 claim の撤回と convention/existence 分離が core。 |
| E05 definitional branch | Reader 02 M1；Reader 03 M1/M2/M14 | **boundary-dependent move difference** と **optional co-code difference** | stipulation による analytic consequence は M1/M2 のいずれにも完全には合わない。**Primary D; secondary B/E**。physical equivalence theorem として数えない terminal reading は一致。 |
| E05 implementation branch | Reader 02 M1/M4/M8；Reader 03 M1/M7/M8/M10 | M8 は **same move**；M4/M7 は **optional co-code/operation typing**；M10 は **code-versus-resource difference** | controlled-transition model への限定は M4 が直接的だが M7 も source-compatible。state map は theorem assumption/resource でも explicit translation でもあり得る。**Primary D; secondary E**。 |
| E05 spatial condition | Reader 02 M17/M14；Reader 03 は terminal record を欠く | **source-resolved coding/coverage error** | spatial inside/outside を primary mathematical condition とすることの `[WITHDRAWN]` は明示。M17 相当の disposition をどこかに残す必要がある。**F** for Reader 03；M14 co-code は **E**。 |
| E07: M2 | 両者とも final code には含めず、Reader 02 のみ候補として保留 | **optional co-code difference** relative to key, not a reader-reader difference | H1 と organizational value を別 claim identity とすれば M2 は不要。同一 audit-value claim の弱化とすれば M2 を付せる。**Primary B/E; secondary D**。両 reader の非codingは source-compatible。 |
| E07: M16 | 両者非coding；key は次の real-record question に期待 | **packet-inaccessible expected code**、かつ proposal-versus-completed-move difference | packet に real-protocol proposal がないため reader error ではない。source return 後も proposal は OPEN HYPOTHESIS で、completed M16 とする key reading は内部的に緊張する。**Primary C; secondary D**。 |
| E10: M12 | 両者 noncoding | **code-versus-analysis-object difference** dependent on unrecorded alternative boundary | C1 framework episode では Gödel II の metalevel は analysis object/resource。Gödel II を独立 transition とすれば M12。**Primary D; secondary B**。noncoding 自体は error ではない。 |
| E10: M2 vs M14 | Reader 02 M14、Reader 03 M2 | **optional co-code difference** | independent diagnostic tool→metaphor は M2、discovery tool→post-analysis summary の型分離は M14。両方 source-compatible。**E**。 |
| E11 main label | 両者 M2/M14；M3 は Reader 02 noncoding candidate、Reader 03 technical blockで ambiguous；M17 はなし | **same move** plus **optional co-code difference** | broad S2→local S2* は M2/M14 で十分再構成される。formula-class restriction M3 と demotion M17 は optional；status label は自動的 move ではない。**Primary B/E**。 |
| E11 technical reflection | Reader 02 は M6/M12 を resource/analysis object、Reader 03 は E11-b の moves | **boundary-dependent**, **code-versus-resource**, **code-versus-analysis-object** | independent technical correction を立てる場合だけ M6/M12 が move。統合 boundary では非coding。**Primary D; secondary B/E**。 |
| E12-a: M1/M3/M4 | 両者が全て coding | **same move under same boundary**, with an internal role boundary | M3 formula-class dimension と M4 natural-theory-family restriction は source-supported。M1 は新条件追加とも suppressed calibration parameters の明示化とも読める。M1 の適用は **D/E**、M3/M4 は **A/B**。 |
| E12-a: M13 | Reader 03 coding、Reader 02 は analysis object として非coding | **code-versus-analysis-object difference** | universal strength claim から calibration question への reformulation と見れば M13。source が冒頭から calibration を analysis target として固定したと見れば非coding。**Primary D; secondary E**。 |
| E12-b: M12 vs M15 | Reader 03 M12/M14；Reader 02 M15/M14、M12非coding | **code-versus-analysis-object difference** と **optional co-code difference** | technical metatheory placement を transition とすれば M12。A3 novelty candidate が standard level distinction に吸収された classification transition なら M15。A-axis が transition か自体不明なので強制しない。**Primary D; secondary G/E**。 |

### 4.1 Source-resolved coding errors

1. **Reader 03, E05:** explicit spatial inside/outside withdrawal をどの after/status にも残していない。boundary は自由でも disposition の欠落は訂正可能である。
2. **Reader 03, E02-b:** source がすでに「条件付きの容量命題は残る」と確定形で述べる proposition の prospective before を `OPEN HYPOTHESIS` と記した。これは source status と provenance label の不一致である。conditional proposition の core status 自体は正しく established とされている。
3. **Reader 03, E08:** future effectiveness measurement を source-explicit でないまま `OPEN HYPOTHESIS inferred` とした。instructions は OPEN HYPOTHESIS を source が明示的に開いた prospective possibility に限るため、この label は外すべきである。
4. **両 reader, E10:** M12 が boundary により変わるのに、Gödel I / Gödel II / C1 composite alternative を `alternative_segmentations` に残さなかった。これは substantive move error ではなく Step 0 の procedural under-recording である。
5. **Reader 02, E11:** `T→T+` の独立 episode possibility を move note では認識したが segmentation alternative として残さなかった。これも procedural under-recording である。

Reader 02 self-adjudication が主張した **E07 M2 の必須追加**は採用しない。claim identity を分けた現在の両 reader reading は instructions と source に整合し、M2 は optional co-code に留まる。また Reader 02 が OPEN HYPOTHESIS を使わなかったこと自体も error とはしない。source-derived open status または available branch として事実を過大確定していなければ、provenance label の不使用だけから誤りは出ない。

## 5. Role adjudication

| Role boundary | Main instances / reader difference | Adjudication |
|---|---|---|
| assumption vs proof/evidence resource | E05 state map、E12 well-foundedness/package。Reader 03 は failure materials も resources に広く重複、Reader 02 は witness に寄せる | Positive theorem conditions と history-length induction の差は **A**。state map と ordinal well-foundedness/TI は theorem version により二役を持ちうるため **Primary B; secondary D**。failure material の resource 欄への重複は **E**；ambiguity 未表示なら minor **F**。 |
| assumption vs evaluation rule | E05 complete interface；E07 preregistered criteria | E07 §5–§6 は evaluation rule、control は evidence resource が primary だが、empirical-method claim の admissible design condition とする reading も許される：**B/D**。E05 の stipulation は assumption と rule を分けにくい：**D**。 |
| proof resource vs failure witness | E01–E04 で Reader 03 は counterconstruction/prior art を両欄、Reader 02 は principal role を witness とすることが多い | 「何によって壊れたか」に置かれた material の principal role は failure witness として **A**。同じ material を investigation resource とも呼ぶことは source-compatible だが no-duplication rule と衝突するため **Primary D; secondary E**。 |
| available branch vs scope condition | E02 countersettings、E04 fresh preparation | source は「この場合は argument/counterexample が使えない」とだけ述べ、repair choice と admissible-scope boundary を一意化しない。**Primary B; secondary E**。fresh preparation を main move にしない点は source-resolved。 |
| available branch vs adopted side claim | E03 concrete-loss route、E09 option (iv) termination、E12 bridge theorem | E03 は retained methodological claim と future route が同じ文に重なるため **D**。E09 は available→later adopted の branch-state transitionで **D**。E12 bridge theorem は requirement/available route で、completed move ではないことが **A**。 |
| retained claim vs evaluation rule | E03「具体的に証明しなければならない」 | 同じ sentence が normative retained claim と success rule を担う。duplicate prohibition 下では一方を主欄に置くしかない。**D**。 |
| source-local classification vs terminal status | E07 M1、E10 C1、E11 S2*、E12 S2*/A2 | final source-local verdict を terminal status として保存することは **A**。その verdict assignment 自体が formation move か、既存 move を持つかは **D**。 |
| rejected hypothesis as retained record | E06 Reader 02 は “retained as rejected historical working hypothesis”、Reader 03 は demoted claim とする | source は historical hypothesis へ降格した記録を残すが、claim-content の retention を主張しない。**Primary E; secondary D**。terminal direction は demoted/rejected で source-resolved。 |
| OPEN HYPOTHESIS | Reader 02 は使用なし。Reader 03 は E02-b、E05-c、E08 で使用 | 明示的 prospective proposal にのみ使う。E02-b と E08 は **F**。E05-c の real-observer map existence は source が保証しないことまでは明示するが、研究 proposal ではないため **E/G**；UNKNOWN/open limitation が安全。Reader 02 の不使用は error でない。 |

## 6. Shared packet gaps

まず両 reader の blind outputs だけから共通 missing/UNKNOWN を抽出し、その後に §0.1 の source return で分類した。

| Topic | Blind-stage finding | After limited source return | Classification |
|---|---|---|---|
| E06 Null C/D/E と concrete witness | 両者が detailed null tests、Erasure、item-level mapping を欠く | original source に definitions、Erasure negative result、chronology/narrative failure がある | **SHARED PACKET GAP → SOURCE-RESOLVABLE BUT PACKET-MISSING**。Primary **C** |
| E06 taxonomy deletion reason | Reader 02 は UNKNOWN、Reader 03 は shared mechanism context から再構成 | diff source に heterogeneous scale の混在と field-native scale 不在がある | **SOURCE-RESOLVABLE BUT PACKET-MISSING**。Reader 03 reading は source-compatible だが blind packet からは **E** |
| E07 preregistered §5–§6 | 両者が full criteria と application details を欠く | F1–F6 と七 success conditions が source にある | **SHARED PACKET GAP → SOURCE-RESOLVABLE BUT PACKET-MISSING**。Primary **C** |
| E07 M0–M3 definitions | Reader 02 が明示、Reader 03 も full threshold 不足を認識 | source に全定義がある | **SOURCE-RESOLVABLE BUT PACKET-MISSING**。Primary **C** |
| E09 reduced-check details | 両者が second-stage witness を summary level に留める | corrected search、zero findings、functional equivalence、artifact/governance explanation、n=1、kill criteria が source にある | **SHARED PACKET GAP → SOURCE-RESOLVABLE BUT PACKET-MISSING**。Primary **C** |
| E10 21-theorem comparison | 両者が比較実体を欠く | designated source に三つの具体比較と overall contrast はあるが、全21 case record はない | Comparison reasoning: **SOURCE-RESOLVABLE BUT PACKET-MISSING (C)**。Complete 21-case basis: **G** |
| E10 C1–C3 | 両者が full ladder definition を欠く | local C1 decision rule/kill criteria は source にあるが general ladder はない | Local verdict: **SOURCE-RESOLVABLE BUT PACKET-MISSING (C)**。Full ladder: **G**, not reader error |
| E11 S1/S2/S2* | 両者が full ladder を欠く | source は S2 kill test と S2* local-only semantics を明示するが general ladder を定義しない | Local transition is already packet-resolvable **A**；full ladder is **SHARED GAP but G**, not a packet-only defect |
| E12 S/A ladders | 両者が full definitions を欠く | source は local S2*/A2 meaning と rejection grounds を示すが full ladders はない | Local verdicts **A**；full ladders **G** |
| E12 fixed calibration package | 両者が concrete unique package を欠く | source は複数 characterization と PA example を示し、単一無条件 package を意図的に固定しない | **SHARED GAP, but primary B**, not reader error and not merely packet defect |
| E08 C-1/C-2 | 両者は packet の C-3 transition だけを reconstruction | original source に二 factual corrections がある | key が三訂正を episode 化する部分は **SOURCE-RESOLVABLE BUT PACKET-MISSING (C)**。reader outputs の C-3 core は正しい |
| E07 real-record proposal / E09 M16 anchor | 両者が coding しない | 両 source にあるが packet にはない | E09 reframing is **C** and source-resolvable。E07 proposal is **C** plus proposal/move **D** |

### 6.1 Reader-specific gaps

- Reader 02 の「E06 Source A が pre-revision か不明」は **READER-SPECIFIC GAP**。parent title、Source B の exact diff、Source C の v0.2 label から before role は packet 内でも十分に定まる。core reconstruction は正しかったため minor **F**（過剰な UNKNOWN）に留める。
- Reader 02 の E08 verdict A の内容は designated original source にも定義文がないため **G**。これは source-resolvable gap ではない。
- Reader 02 の “Codex が human reviewer か automated reviewer か” は source に `Codex adversarial review` とある以上、transition witness の内容には影響しない。agent ontology は **G** かつ adjudication に不要である。
- Reader 03 の E02-b での empty-domain concern は packet/source が扱わない local edge conditionで **G**。parent transition core の欠落ではない。

## 7. Framework-boundary adjudication

| Boundary pressure | Verdict | Grounds |
|---|---|---|
| definitional / stipulative transition | **REAL FRAMEWORK BOUNDARY** | E05 convention は source-clear だが、M1/M2/M14 はいずれも「claim が analytic consequence へ変わった」ことを自然には単独表現しない。 |
| taxonomy deletion | **REAL FRAMEWORK BOUNDARY** | M17 は deletion disposition を近似できるが、claim withdrawal と classification apparatus deletion を区別しない。理由欠落は別に packet artifact。 |
| verdict relabel | **REAL FRAMEWORK BOUNDARY** | E08 の label change は M2/M14/M17 の組合せで内容を保持できるが、source-local verdict relabel 自体とは一致しない。 |
| state-map simulation | **REAL FRAMEWORK BOUNDARY** | E05 の commuting state map は condition、resource、M10 translation、M7 model revision の境界にある。 |
| branch-state transition | **REAL FRAMEWORK BOUNDARY** | E02 extra conditions と E09 termination branch は subepisode をまたいで available→adopted へ変わるが、その同一性を現在の block だけでは自然に保持できない。 |
| object-level mathematical operation vs formation move | **REAL FRAMEWORK BOUNDARY** | E10 M12、E11 M6/M12、E12-b M12 が、episode boundary により analysis object から move へ変わる。 |
| multiple-axis restriction | **REAL FRAMEWORK BOUNDARY** | E12 の一つの fixed-package qualification が M1/M3/M4 に分解され、分解粒度を source が一意に決めない。 |
| kill-test with limited survival | **REAL FRAMEWORK BOUNDARY** | E11 は kill-test process と S2* limited survival を明示するが、M2/M17/status のどれがその process を担うか一意でない。 |
| multiple after-claims | **REAL FRAMEWORK BOUNDARY** | E05 の withdrawal、convention、conditional lemma は異なる moves/statuses を持ち、single `move_taken` では対応関係が曖昧になる。 |
| `degenerate_or_target_leakage` | **REAL FRAMEWORK BOUNDARY** | reader-facing instructions は required field を定義しない。E03/E05 の conclusion-as-definition は安定して復元されたが、E04/E07/E09 等への拡張適用は reader-specific になった。 |
| provenance referent | **REAL FRAMEWORK BOUNDARY** | `move_taken` の provenance が source の action wording を指すのか、M-code assignment を指すのか不明。answer key は後者を INFERENCE とするが reader-facing instructions だけでは一意でない。 |
| cross-subepisode linkage | **REAL FRAMEWORK BOUNDARY** | shared before、later-adopted branch、dependent alternative segmentation の linkage が record 内で弱い。E02/E05/E09/E11 で両 reader が別の workaround を用いた。 |

これらは主要 transition core を破壊していない。一方だけの好みとして現れた leakage 拡張や細分化は **READER-SPECIFIC ONLY** だが、上表の基礎的 pressure 自体は両 output または source comparison で再現されている。**NOT SUPPORTED** と判定すべき重点項目はない。

## 8. Withheld answer-key comparison

answer key は source-anchored expectation として比較し、唯一の正解列とは扱わない。

| Episode | Qualitative relation to key |
|---|---|
| E01 | **both match expected core**。Reader 02 の M14 は permitted co-code、Reader 03 の side-claim split も source-compatible。 |
| E02 | **both match expected core**。Reader 02 は main M14 で key に近いが、Reader 03 の M2 は source-compatible。二 episode 化も許容範囲。 |
| E03 | **both match expected core**。M4 を加えないことも許容される。 |
| E04 | **both match expected core**。M13 は optional。fresh preparation を main move にしていない。 |
| E05 | **both match expected general/convention/conditional core**。Reader 02 は packet の second spatial withdrawal も保持し、Reader 03 はそこだけ source-resolved omission。key 自身は branch segmentation を underdetermine する。 |
| E06 | **both match expected terminal core**。key の Erasure witness は packet-inaccessible information に依存する。taxonomy-specific reason も packet 外であり、reader failure としない。 |
| E07 | **both match negative H1 / organizational remnant core**。M2 は identity-dependentで両 reader の非codingも source-compatible。key の M16 は packet-inaccessible proposal に依存し、key の「proposal を completed move にしない」という provenance anchor と緊張する。 |
| E08 | **both match expected visible core**。key の C-1/C-2/C-3 partition は C-1/C-2 が packet-inaccessible。visible C-3 transition の reader reconstruction は妥当。 |
| E09 | **both match expected scope/termination core**。key の M16 anchor は packet 外 source にあるため欠落を reader failure としない。M15 の有無も review demotion の operation reading に依存する。 |
| E10 | Reader 02 は M14/M15/M17 で row に近く、Reader 03 は M2/M15/M17 で **source-compatible**。key の M12 は Gödel-II subepisode を立てる場合に妥当で、single meta-episode では analysis object。**both differ in boundary record, but source ambiguity permits the move difference**。 |
| E11 | Reader 03 は technical subepisode で key の M6/M12 を直接表す。Reader 02 は key の own AB-B1 boundary note と同じ resource readingを採る。**both are source-compatible; key itself is boundary-sensitive**。Reader 02 の欠陥は alternative の記録位置。 |
| E12 | Reader 03 は M13/M12 で expected row に近く、Reader 02 の M13/M12 noncoding と M15 は source-compatible。A-axis before と unique calibration package は underdetermined。**key is not a unique coding column**。 |

key についての独立した問題は二つある。

1. E06 Erasure、E07 next real-record question、E09 limited-question reframing、E08 C-1/C-2 は packet 外情報へ依存する。これらを blind reader failure として扱えない。
2. E07 M16 expectation は、同じ key の「future proposal を completed move としない」という provenance anchor と内部的に緊張する。これは **key itself internally tense** であり、forced resolution しない。

## 9. Cross-reader reconstructibility result

### A. Stable transition core

- 全 parent item で principal before、failure direction、withdrawal/demotion、retained remnant、terminal direction が比較可能だった。
- 特に E01–E04、E07–E10 は source wording と explicit verdict が強く、reader-specific segmentation を吸収しても core が変わらない。
- E05/E06/E11 でも boundary は揺れたが、general withdrawal、negative verdict、limited survival は同方向だった。

### B. Stable ambiguity hotspots

- E05 の one-revision versus separate definitional/implementation episodes。
- E06 の case/mechanism/taxonomy grouping。
- E10/E11 の mathematical object versus formation episode。
- E12-b の A2 classification が transition か standing verdict か。

### C. Boundary-dependent coding

- E05 M1/M2/M4/M7/M10、E10 M12、E11 M6/M12/M3、E12 M13/M12/M15 は、source content の不一致ではなく episode/role boundary の違いから生じる。
- この coding disagreement は parent-level core disagreement を意味しない。

### D. Shared packet limitations

- E06、E07、E09 は core verdict は読めるが、decision procedure または concrete witness が packet から落ちている。
- E08 key の追加 factual corrections と、E10 の concrete comparison body も packet 外である。
- E10–E12 の full ladders は original source にも完備せず、packetだけの欠陥と誤認してはならない。

### E. Framework boundaries

- stipulation、taxonomy deletion、verdict relabel、state-map simulation、branch-state change、multiple after-claims、provenance referent、cross-subepisode linkage が再現性のある pressure point だった。
- これらは現行 code/field の限界を示すが、before/failure/after/status の復元を妨げなかった。

### F. Reader-specific reconstructions

- Reader 02 は additional ambiguity と UNKNOWN を広く保持し、spatial withdrawal と taxonomy deletion を独立化した。
- Reader 03 は conditional/technical successors を独立化し、state-map、reflection、metatheory、calibration を moves として多く coding した。
- いずれの傾向も、明示的 omission または provenance misuse を除き、source-compatible な reconstruction style である。

### G. Adjudicable coder errors

- Reader 03 の E05 spatial withdrawal omission。
- Reader 03 の E02-b / E08 `OPEN HYPOTHESIS` misuse。
- 両 reader の E10 boundary-dependent alternative under-recording。
- Reader 02 の E11 alternative-segmentation under-recording。
- Reader 02 の E06 Source A role に対する過剰な UNKNOWN。

これらはいずれも principal terminal direction を反転させない。

### H. Useful negative results

- 同じ text を読んでも object-level mathematical operation を formation move とするかは一意にならない。
- key が期待する move の一部は blind packet から到達不能である。
- source-local verdict は安定して転記できても、その verdict assignment に対応する M-code は必ずしもない。
- `degenerate_or_target_leakage` の canonical cases は再構成できたが、field の reader-facing definition がないため周辺適用は不安定になった。
- full ladder がなくても local before/failure/after/status は復元できた。逆に ladder label だけでは独立の transition を作れない。

## 10. Phase-0 gate

### Verdict: **P0-PASS**

有限命題論理 prototype へ進めるだけの reconstructibility がある。

1. **Parent transition core:** segmentation style が異なっても、主要 before/failure/after/status は全 parent で同方向に再構成された。
2. **Localized ambiguity:** ambiguity は E05/E06/E10/E11/E12-b 等に局所化され、segmentation、role、code-versus-analysis-object として型付けできる。
3. **Packet versus framework:** E06/E07/E09 の source-resolvable packet欠落と、stipulation/state-map/cross-linkage 等の framework boundary を区別できた。
4. **Move versus core:** move disagreement は多いが、principal withdrawal、remnant、terminal direction の崩壊を伴わない。
5. **Claim identity / terminal status:** main claim と side claim は概して分離され、withdrawn claim が narrow remnant の成功へ無言で変換されていない。
6. **Adjudication burden:** recurring differences は少数の既存境界型へ戻せ、新しい例外規則を episode ごとに作る必要はなかった。

この PASS は move taxonomy の完成、packet の完全性、framework の確定、または L3 completion を意味しない。Reader 03 の blindness audit limitation と上記 packet gaps は記録として残るが、現時点の目的である L1/L2 前段の independent reconstructibility を否定するほどではない。

## 11. Final report

1. **Reader 02 blindness verdict:** VALID BLIND RESULT。
2. **Reader 03 blindness verdict:** VALID WITH LIMITATION。二ファイルのみ使用との申告と内容上の blind signature はあるが、先行 adjudication material が workspace に存在した状態での独立非閲覧を外部監査できない。
3. **Strongest convergence:** main claim の withdrawal/demotion と narrow remnant の別 status が、segmentation によらず保たれたこと。E02、E07、E09 が特に明瞭。
4. **Strongest ambiguity hotspot:** E11 の S2→S2* label judgment と `T→T+` technical reflection transition の境界。M6/M12 の有無がここから直接変わる。
5. **Strongest packet defect:** E06 の concrete Null/Erasure witness、E07 の preregistered criteria、E09 の reduced-check observations が source にはあるのに frozen excerpts から落ちていること。
6. **Strongest framework boundary:** source 内の mathematical structure / simulation / metatheory placement を formation move とするか analysis object とするかの境界。
7. **Clear coder errors:** Reader 03 E05 spatial withdrawal omission、Reader 03 の二つの OPEN HYPOTHESIS misuse、E10 の両-reader boundary under-recording、Reader 02 E11 boundary under-recording。substantive core reversal はない。
8. **Useful negative result:** code-set disagreement は transition-core disagreement の proxy にならず、key expectation 自体も packet accessibility と episode boundary に依存する。
9. **Phase-0 gate verdict:** **P0-PASS**。


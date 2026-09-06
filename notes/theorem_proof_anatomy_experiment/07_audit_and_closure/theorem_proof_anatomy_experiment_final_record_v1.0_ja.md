# theorem / proof anatomy 実験系列 最終記録 v1.0

## Status / posture

- **final experimental record**
- **not a theorem**
- **not a new proof theory**
- **not a new framework**
- **not `theorem_proof_anatomy_v2`**
- **no novelty inflation**
- **negative results are primary evidence**
- **retired terminology is recorded historically, not revived technically**
- **standard terminology is preferred**
- **source chronology has known gaps and uncertainties**
- **the “independent audit” is internal to this series, not external peer review**

本稿は discovery narrative、success story、理論完成報告、proof-theoretic manifesto、または形而上学的結論ではない。観測・予測に用いる道具の成功と識別可能性をめぐる問いから始まり、定理の条件、証明形成の記録、有限形式実験、記録枠、個別定理の証明依存、定理性が含む情報、証明同値、仕様間翻訳、異なる calculus 間の証明対応へ対象を移した一連の作業について、**何を問い、何を期待し、何を試し、どこで主張が壊れ、何だけが残ったか**を記録する。

詳細な file-level traceability は [source map v0.1](./theorem_proof_anatomy_experiment_source_map_v0.1_ja.md) を参照されたい。本稿の執筆規約と phase map は [source architecture v0.1](./theorem_proof_anatomy_experiment_source_architecture_v0.1_ja.md)、停止判断と novelty 評価は系列内の [full-series independent audit v0.1](./theorem_proof_anatomy_full_series_independent_audit_v0.1.md) に基づく。ただし、これら二文書を一次証拠の代用にはしていない。working hypothesis、counterexample、当時の `KILL` / `RETIRE` / `DOWNGRADE` / `OPEN` / `NOT ESTABLISHED` は、可能な限り各 primary record に戻って確認した。

初稿時の source map 冒頭には、「70ファイル」と「`.md` 68 + `.py` 8（合計76）」が同時に記載される内部不整合があった。archive reorganization 時の実ファイル再集計により、系列資料は83ファイル（`.md` 74 + `.py` 8 + `.svg` 1、archive READMEを除く）と確認され、source map の該当箇所は subsequently corrected された。phase mapping や実験上の判定は変更していない。

---

# Part I — Genealogy

## 1. どこから始まったか

### 1.1 「最初」の資料は起源そのものではない

現存する最古の file record は 2026-08-16 の [tool truth absence working note](../00_origin/tool_truth_absence_working_note.md) である。しかしこの文書自体が、すでに以前の主張と撤回を振り返って再構成している。したがって、これを問いの真の発生時点と呼ぶことはできない。ここで記録できるのは、**現存資料に現れる最初の形**だけである。

その形は、概ね次の分離から成っていた。

- 予測または観測への適合
- model / tool の実用上の成功
- その成功を生む存在論の一意性
- 観測写像の injectivity と parameter identifiability
- auxiliary conditions の妥当性
- observational equivalence のもとで残る複数候補

当時の「道具の真理不在性」という名称は、「真理が存在しない」という主張ではなかった。中心にあったのは、**道具の成功は、その道具が前提とする補助条件や存在論的一意性を、それだけでは自己証明しない**という直観である。この直観は後に inverse problems、identifiability、robustness、applicability、validation などの標準語彙へ分解されたが、最初からその還元を目的としていたわけではない。

### 1.2 chronology に関する六つの留保

本系列の時系列は、主として file mtime と明示日付から再構成した。ただし次の留保がある。

1. 最古の file record 自体が、それ以前の撤回史の再構成である。
2. `theorem_proof_anatomy/` の v1.1 と10 stress tests、計11ファイルは、すべて 2026-09-04 20:32 の同一 bulk mtime を持つ。directory 移動の痕跡と考えられ、内部順序は復元できない。
3. Phase 0 と Phase 1 の間には13日の undocumented gap がある。
4. Phase 2 から Phase 7 は、2026-09-04 21:18 から 09-06 18:01 までの約45時間に集中している。
5. mtime は最終更新時刻であり、作成時刻でも思考順序でもない。
6. “independent audit” は系列内部で書かれた cross-series audit であり、外部 peer review ではない。

従って、本稿は後の結果を初期の目的へ逆投影しない。とくに、この系列が最初から theorem anatomy、proof identity、cross-calculus comparison へ向かっていたとは書かない。

### 1.3 source-derived phase map

| Phase | おおよその時期 | 主対象 | 当時の中心問い | 終端 |
|---|---:|---|---|---|
| 0 | 08-16〜08-22 | 科学的 tool / claim | 成功から生成構造や存在論を一意に同定できるか | 普遍定理候補を撤回、比較計画を終了・降格 |
| 1 | 09-04以前、内部順序不明 | 21定理と10 stress tests | 条件が何をし、除去時に何が起きるか | H2暫定支持、H3 unsupported |
| 2 | 09-04〜09-05 | correction history | 別 reader が claim transition を再構成できるか | P0-PASS、code disagreement 保存 |
| 3 | 09-05 | 有限命題 model | move の差は意味論か記録か | semantic identification を DOWNGRADE |
| 4 | 09-06午前 | record frames | 枠を変えると差はどう見えるか | minimal-separator characterization を KILL |
| 5 | 09-06午後前半 | 4定理の proof dependency | proof failure と theorem failure を分けられるか | bespoke vocabulary を標準語へ還元し RETIRE |
| 6 | 09-06午後後半 | theoremhood / equality / translation | 判断・同値・仕様変更・calculus変更は何を保存するか | relation-relative な標準問題へ分解 |
| 7 | 09-06 18:01 | 系列内 audit | 何が残り、どこで止めるべきか | Option 2、STOP WITH SYNTHESIS |

この表は因果系列ではない。Phase 0→1 の対象交代の理由は source に記録されておらず、Phase 4→5 も枝の終了後に別方向へ移った事実だけが確認できる。

### Primary records

- [tool truth absence working note](../00_origin/tool_truth_absence_working_note.md)
- [tool truth absence trajectory summary](../00_origin/tool_truth_absence_research_trajectory_summary.md)
- [source architecture](./theorem_proof_anatomy_experiment_source_architecture_v0.1_ja.md)
- [source map](./theorem_proof_anatomy_experiment_source_map_v0.1_ja.md)

---

## 2. 道具の真理不在性と識別可能性

Phase 0 は単なる前史ではない。最終的に残った audit discipline の大部分は、形式的証明を扱う前に、科学的 claim と文書比較を監査する過程で形成されていた。

### 2.1 universal impossibility theorem candidate

初期の期待は強かった。観測された出力や予測成功から、内部生成構造を一意に回収できないことを、広い普遍的不可能性として定式化できないかが検討された。

しかし候補を論理形にすると、異なる失敗が現れた。

1. 観測写像 $O:W\to Y$ の非単射性から非識別性を導く案には、非単射性そのものが仮定として必要だった。$O=\mathrm{id}_W$ は明示的 counterexample であり、普遍主張を壊した。
2. self-containment が universal non-identifiability を含意するという案は、有限 encoder や可逆な自己記述の control に耐えなかった。自己参照に関する既知定理も、追加仮定なしの一般的不可能性を与えなかった。
3. generation と log の non-isomorphism を一般化する案は、「log は情報を失うもの」と定義した場合に結論を前提へ埋め込む循環を起こした。可逆・完全符号化の場合にはその読みは偽になる。
4. resource bounds による制約は条件付き結果にはなり得たが、存在論的一意性一般の否定にはならなかった。

ここで重要なのは、普遍主張が「反例をまだ見つけていない」ために保留されたのではない点である。$O=\mathrm{id}$ などの control が、主張の全称形へ直接応答した。一方、generation–log の一部は false というより **ill-posed / circular** だった。この二つは後の記録でも区別された。

### 2.2 pairwise separation と global separator

個々の候補対を区別する実験が存在することと、未知の候補集合全体に対して一つの adaptive separator があることも分けられた。二ビットの destructive measurement control は、局所的な識別可能性から global strategy を自動推論できないことを示した。

これは後年の proof-class correspondence と同じ問題だった、と書くべきではない。当時の対象は科学的観測と実験選択だった。ただし、**存在証拠と全称主張の証拠を区別する習慣**はここですでに形成され始めていた。

### 2.3 general vocabulary を field-native control にかける

普遍不可能定理の後には、`premise stack`、`web of constraints`、`claim transport`、assurance provenance などの一般監査語彙が試された。導入理由は、source claim から target use へ移る間に、補助条件・適用範囲・保証の出所がどう変わるかを横断的に追跡することだった。

しかし各 case は一般語彙の追加価値に厳しい制限を置いた。

- **GST:** 当時 “Deferred Resolution” と呼ばれた記述は、conditional inverse problem、nuisance parameter、gauge、model discrepancy などの既存語彙を消去した後に独自診断を残さなかった。Erasure Test 後、一般機構としては frozen negative になった。
- **metrology:** measurement uncertainty、traceability、calibration scope、conformity assessment の field-native reconstruction が、generic audit と同じ重要差を捉えた。最終的に残った M1 は新機構でなく、主に organizational / indexing value だった。より強い M2/M3 は支持されなかった。
- **hydrology:** negative knowledge の「保存」という初期表現は、資料から確認できる documentary continuity へ弱められた。実際の意思決定で知識が保持・利用されたという efficacy claim は出なかった。
- **generic standards baseline:** 14の候補 code のうち大半は一般的な標準・assurance practice で再構成され、比較後に固有候補として残ったのは実質一つの `NONEVAL` だけだった。その後の二分野 control でも固有性は残らず、comparative methodology は終了し、comparative review へ降格した。

これらは「分野固有語彙は常に十分」という普遍主張を証明しない。支持したのは、テストした資料では generic vocabulary の superiority が示されなかったこと、そして分野固有の深い epistemic difference という解釈が **unsupported** だったことまでである。

### 2.4 Phase 0 で既に明文化された八つの規律

2026-08-22 の trajectory summary は、次を明記している。

1. **Field-native first:** 一般語彙より先に、その分野自身の最強の説明を再構成する。
2. **Erasure Test:** 固有語彙を消して結論が残るなら、追加価値を表示・索引以上に数えない。
3. **Control reconstruction:** 同じ資料を field-native terminology だけで読む対照を作る。
4. **Historical and logical separation:** 時系列と論理的依存を混同しない。
5. **Artifact / institution / field separation:** 一文書の omission、制度的未運用、分野全体の欠如を分ける。
6. **Time-sliced audit:** 後知恵を遮断し、当時利用可能な資料で検査する。
7. **Selection-route logging:** source / target の選び方と convenience を記録する。
8. **Preregistered kill criteria:** 差が出なければ語彙・仮説・計画を降格または終了する。

したがって、後半の formal pilots が audit discipline を発見した、とは書けない。後半はこの規律を別対象で再使用し、証拠の論理形、translation、quotient equality へ精密化した。

### 2.5 Phase 0 が残した問い

Phase 0 の終端は普遍理論ではなかった。残された狭い問いは、固定時点の同じ資料について field-native control と structured comparison を独立に行い、後者だけが material で未明示かつ decision-relevant な条件差を再現可能に検出するか、という経験的比較だった。これが確認できなければ終了する、という kill condition まで明示された。

この comparative program 自体は所期の superiority を示さず終了した。しかし、失敗を区別し、対照を再構成し、語彙を消去し、選択経路を記録する実務は残った。

### Primary records

- [tool truth absence working note v0.4](../00_origin/tool_truth_absence_working_note_v0.4.md)
- [trajectory summary](../00_origin/tool_truth_absence_research_trajectory_summary.md)
- [GST v0.2](../00_origin/deferred_resolution_case_01_gst_v0.2.md)
- [metrology comparison](../00_origin/scientific_assurance_case_02_metrology_comparison.md)
- [hydrology preservation note v0.2](../00_origin/hydrology_negative_knowledge_preservation_note_v0.2.md)
- [generic standards baseline](../00_origin/p0_generic_standards_baseline_v0.1.md)
- [two-field check](../00_origin/p1r_noneval_two_field_check_v0.1.md)

---

## 3. 定理へ対象を移した時点

Phase 0 の最終記録と Phase 1 の theorem anatomy files の間には13日の gap がある。現存 source は、なぜ scientific claims から formal theorems へ対象が移ったかを直接説明しない。本稿はそこへ「より純粋な対象を求めた」「識別可能性の本質を定理に見た」などの因果を補わない。

資料上確認できるのは、問いが次の形へ変わったことだけである。

> 定理の各条件は何をしているか。条件を除くと、証明、結論、定式化、または周辺構造の何が変わるか。

この対象交代には連続点もあった。Phase 0 の Erasure Test と control reconstruction は、定理の仮定を外したときの挙動を監査する方法と相性がよかった。しかし「相性がよい」ことは、対象交代の歴史的理由を示さない。

また、Phase 1 の11ファイルは同一 mtime である。v1.1 が21定理 survey、各 stress test がその語彙を引き継ぐという内容上の依存は読めるが、執筆の細かな順序は retrospective interpretation に留まる。

この phase の出発時点では、`object`、`ambient`、`background`、`definitional`、`closure role`、`escape route`、`residual` といった working vocabulary に、分野横断の機能差を捉える期待があった。その後この語彙の多くが降格・退役したからといって、導入時から単なる言い換えと考えられていたわけではない。

### Primary records

- [trajectory summary](../00_origin/tool_truth_absence_research_trajectory_summary.md)
- [theorem / proof anatomy v1.1](../01_theorem_anatomy/theorem_proof_anatomy_v1.1_ja.md)
- [source map: traceability caveats](./theorem_proof_anatomy_experiment_source_map_v0.1_ja.md#5-traceability-caveats)

---

# Part II — Experiment

## 4. theorem / proof anatomy v1.1

### 4.1 question と survey design

[theorem / proof anatomy v1.1](../01_theorem_anatomy/theorem_proof_anatomy_v1.1_ja.md) は、解析、位相、代数、確率、統計などから21定理を取り、各定理を同じ record fields で比較した。主要 fields は次である。

- theorem object と ambient setting
- assumptions を object / ambient / background / definitional に分けた `hypothesis_levels`
- condition types
- conditions が果たす `closure_roles`
- blocked escape routes
- `what_fails_if_removed`
- `what_reappears_if_removed`
- assumptions と区別した `proof_resources`
- theorem statement と一つの proof organization の差

ここで有効だったのは、すべての固定事項を axiom と呼ばず、対象の条件、周囲の構造、通常省略される背景、記号や演算を利用可能にする定義を分けたことである。また、定理の仮定と、その証明で便宜的・派生的に使う lemma や theorem を別欄にした。

### 4.2 condition removal と R0 / R1 / R2

条件除去後の記録には、当時次の作業ラベルが使われた。

- `R0`: 定理の偽化または定式化不能が起きるが、自然な補正項は確認されない。
- `R1`: 非一意性、別極限、新しい自由度、別構造が現れる。
- `R2`: 一般化された同じ式に境界項・補正項・追加項が明示的に現れる。

survey では R2 が Stokes の無限遠境界項、Gauss–Bonnet の境界測地曲率、中国剰余の fiber-product compatibility、Bayes の欠落仮説項などに集中した。多数例は R1 または R0 だった。同じ条件除去でも、どこまでを「自然な一般化」とするかでラベルが変わり得ることも明記された。

条件機能の横断比較では、次の六 clusters が記録された。

1. 逃走・極限回収
2. 有限次元閉包
3. 正則性・飛躍禁止
4. 会計・正規化
5. 独立性・対称性制限
6. 局所から大域への接続

これらは排他的分類ではなく、同じ条件が複数機能を持ち得る。v1.1 自身も個数や主タグが coding rule に依存することを認めていた。

したがって二つの working hypotheses の判定は非対称だった。

- **H2:** object / ambient / definitional の分離や、極限回収、有限次元、会計・正規化、局所大域などの機能差は複数定理で再現したため、**tentative support**。
- **H3:** 条件除去後に residual が普遍的に再出現する強い pattern は、R2 の稀少性と偏在のため **unsupported**。

### 4.3 special stress tests が加えた制限

Gödel、Tarski、Löb、GL、reflection、Turing–Feferman progressions、GLP worms、reflection progressions、proof-theoretic ordinals などの stress tests は、標準 proof theory の区別を project-local metaphor で置換できないことを繰り返し示した。

- Gödel の independent sentence は Stokes 型の R2 correction term ではなく、independence、unprovability、reflection limitation で記述すべきだった。「closure reversal」は説明比喩として `C1` に降格した。
- reflection scope は formula class、base theory、uniformity、provability predicate に相対した。単一の scope ordering という強い読みは修正された。
- ordinal は fixed analysis package 内では robust calibration になり得るが、全 theory strength の universal scalar ではなかった。最終判定 `S2*` は自然な analysis family 内の限定的頑健性、`A2` は system / metatheory の既知の型差を示したにすぎない。

これは H2 を偽にしなかったが、その意味を狭めた。比較表としての anatomy は残る一方、`closure`、`blocking`、`residual` は標準数学用語ではなく、独立した proof-theoretic classification でもなかった。ordinal scalar や一般化された residual pattern への過剰な読みは維持されなかった。

### 4.4 ここでまだ判明していなかったこと

v1.1 の `what_fails_if_removed` は、少なくとも後に次の三つへ分かれることになる。

1. displayed proof が壊れる。
2. fixed reduced theory から target が導出できない。
3. domain や interpretation が変わり、同じ claim を問えていない。

ただし、この三分は Phase 1 の完成済み結論として書かれてはいなかった。後の arithmetic tests と countermodels が、同じ欄では証拠責任が混ざることを具体化した。ここで後続結果を先取りして v1.1 の失敗と断定するのではなく、**後に精密化された未分離点**として扱う。

### Primary records

- [theorem / proof anatomy v1.1](../01_theorem_anatomy/theorem_proof_anatomy_v1.1_ja.md)
- [Gödel stress test](../01_theorem_anatomy/godel_incompleteness_closure_reversal_stress_test_ja.md)
- [reflection principles stress test](../01_theorem_anatomy/reflection_principles_scope_stress_test_ja.md)
- [Turing–Feferman progressions stress test](../01_theorem_anatomy/turing_feferman_progressions_stress_test_ja.md)
- [proof-theoretic ordinal stress test](../01_theorem_anatomy/proof_theoretic_ordinal_stress_test_ja.md)

---

## 5. proof-formation を対象化する

### 5.1 訂正の内容から訂正史へ

Phase 2 は、Phase 0 と Phase 1 の「何が正しいか」を再び判定するよりも、それらの主張訂正が別 reader によって再構成可能かを問うた。[proof-formation meta-experiment](../02_proof_formation/proof_formation_meta_experiment_v0.1.md) は、claim transition を M1–M17 の move codes と K/A/R/D/U の typed observations で記録する案を提示した。

M1–M17 は assumption strengthening、conclusion weakening、scope change、retraction などの複数 move を許し、単一 score を作らなかった。K/A/R/D/U も、何が保持され、追加され、削除され、残り、未決定かを別 slots に置く意図だった。

evidential status は次のように事前登録された。

- **L0:** annotated source inventory
- **L1:** finite corpus で再現可能な local coding procedure
- **L2:** ordinary revision ledger を越える比較有用性を、複数 corpus・別チームで示す
- **L3:** taxonomy から一般定理、必要十分条件、最適 rescue rule、普遍的順序を作る段階

L3 は、claim identity、episode boundary、code completeness、order relation、reader robustness などが未検証である十の理由により、明示的に拒否された。

### 5.2 risks were preregistered

reader experiment 前から、最高 priority risk は **claim identity / episode boundary** とされた。何を同じ claim の revision とし、何を neighboring question または new claim とするかが揺れれば、move code 自体が変わるからである。この脆弱性は、reader disagreement を見てから導入された説明ではない。

corpus は Phase 0 の E01–E09 と Phase 1 の E10–E12、計12 episodes に frozen された。Reader01 は pilot calibration に使われ、正式な blind comparison は Reader02 と Reader03 で行われた。coder instructions と adjudication rules も分離された。

### 5.3 blind comparison と adjudication

二 reader は、各 parent transition の before claim、failure、withdrawal / repair、retained remnant、terminal direction について大筋で一致した。一方、M-code sets、primary / secondary move、claim boundary の取り方には不一致が残った。

さらに answer key が期待した三 codes は、frozen packet 内の excerpt から到達不能だった。たとえば GST の Erasure Test、metrology の一部 preregistered criterion、P0 termination の reframing は原 source にはあるが、blind reader に渡された抜粋には含まれていなかった。adjudication はこれを reader error とせず、packet accessibility の問題として残した。

最終判定 `P0-PASS` は、parent-level transition core の independent reconstructibility を支持した。これは move taxonomy の完成、packet の完全性、または L3 completion を意味しない。code-set agreement は transition-core agreement の proxy にならず、key expectation 自体が claim boundary と excerpt selection に依存した。

### 5.4 phase result

Phase 2 が支持したのは、有限 corpus での local reconstruction、すなわち **L1 PASS** である。L2 は実施されていない。M1–M17 と K/A/R/D/U が ordinary revision ledger を越える比較有用性を持つかは未確認である。

これは後の停止判断に重要である。meta-experiment は「L1またはL2が失敗した場合、annotated trajectory / review として終了する」と gate を事前登録した。現状は L2 failure ではない。**L2 NOT ATTEMPTED** であり、その未実施を越えて framework claim を上げないことが、事前登録された evidential boundary に適合する。

### Primary records

- [proof-formation meta-experiment](../02_proof_formation/proof_formation_meta_experiment_v0.1.md)
- [frozen toy corpus](../02_proof_formation/proof_formation_frozen_toy_corpus_v0.1.md)
- [coder instructions v0.1.1](../02_proof_formation/proof_formation_coder_instructions_v0.1.1.md)
- [Reader02 / Reader03 blind comparison](../02_proof_formation/proof_formation_reader_02_03_blind_comparison_v0.1.md)
- [inter-reader adjudication](../02_proof_formation/proof_formation_inter_reader_adjudication_v0.1.md)

---

## 6. 有限命題 prototype と semantic collapse

### 6.1 なぜ有限 model を作ったか

reader coding の不一致を、より小さく実行可能な形式設定で検査するため、Phase 3 は有限命題論理へ移った。目的は proof-formation 全般を形式化することではなく、M1 assumption strengthening、M2 conclusion weakening、scope surrogate、M17 withdrawal の差が semantic behavior だけから回収できるかを見ることだった。

有限 valuation space $\Omega$ 上で、hypothesis $H$ の model set $M(H)$ と、conclusion $C$ に対する error set $E(H,C)$ を計算した。prototype checker は例 A–E の valuation と初期 flags を検査し、stress checker は $n=2$ の全数と $n=3$ の標本について34 findings を確認した。

### 6.2 exact-filter repair と T1 circumvention

M1 型 repair には、除外したい valuation set (E) に対する exact filter

\[
B=\varphi_{\Omega\setminus E}
\]

を追加すれば、有限 setting では target errors を正確に消せる。この構成は M1 repair が test-local に容易に存在することを示したが、自然さ、post-hocness、または科学的正当化を与えない。

また、target identity を literal token で固定する T1 型 test は、意味的に同値な formula へ書き換えることで回避できた。identity token を追加しても、その token の同一性規則を外から選ぶ必要があり、形式的内容は増えなかった。

### 6.3 M1 / M2 / scope の相互模倣

最も強い negative result は、異なる形成履歴が同じ after-semantics を作れることだった。

- premise を強める M1 と、対象 scope を狭める surrogate は、有限 domain 上で相互に模倣できた。
- M1、M2、scope change が到達できる (E)-family は一致した。
- 同じ endpoint / model-set behavior から、どの move が行われたかは逆算できなかった。
- `withdrawn` という M17 status には semantic surrogate がなく、history layer の typed field に残った。

従って、**semantic behavior alone did not recover formation history**。区別を担ったのは、どの slot を変更したか、どの status を付けたかという typed record だった。

これは「M1、M2、scope、M17 の区別は無意味である」ことを示さない。異なる履歴を記述する語としては有用であり得る。否定されたのは、endpoint semantics が move identity を一意に決めるという読みである。

### 6.4 checker の証拠範囲

checker は encoded finite claims を再計算した。証明したのは valuation equality、特定 construction、selected class counts、record consistency である。次は証明していない。

- repair が post hoc かどうか
- claim identity の正当性
- episode segmentation の自然さ
- move の意図
- 任意の proof-formation corpus への一般化

code output は一般定理の代用ではなかった。むしろ、何を計算でき、何が record judgment に残るかを切り分けた。

### Primary records

- [finite propositional prototype](../03_finite_propositional/proof_formation_finite_propositional_prototype_v0.1.md)
- [prototype checker](../03_finite_propositional/proof_formation_finite_propositional_checker_v0.1.py)
- [finite propositional stress test](../03_finite_propositional/proof_formation_finite_propositional_stress_test_v0.1.md)
- [stress checker](../03_finite_propositional/proof_formation_finite_propositional_stress_checker_v0.1.py)
- [postmortem architecture](../03_finite_propositional/proof_formation_finite_propositional_postmortem_architecture_v0.1.md)

---

## 7. record-frame branch と KILL

Phase 4 は、semantic endpoint が履歴を同定しないなら、どの記録 field が差を可視化するかを調べた。これは最終的な「真の frame」を探す作業として始まったわけではないが、途中で frame-independent core、first-visible frame、minimal separator という候補が順に検査された。

### 7.1 nested record frames

[record-frame sensitivity test](../04_record_frame/proof_formation_record_frame_sensitivity_test_v0.1.md) は R0–R4 の nested projections を作り、同じ histories がどの fields で区別できるかを調べた。action label を捨てても、carrier、slot typing、claim identity、provenance が残れば一部の区別は再構成できた。しかし、これは action ontology から自由になったことを意味しなかった。別の設計選択が carrier と projection に移ったからである。

### 7.2 persistence は projector design だった

[cross-frame persistence test](../04_record_frame/proof_formation_cross_frame_persistence_test_v0.1.md) は複数 projectors に共通して残る K1/K2 を候補 core とした。しかし「全 selected projectors がその fields を保持する」と設計すれば、共通性は設計の帰結になる。frame-independent invariant という強い読みは支持されなかった。

### 7.3 visibility は単調でも順序独立でもない

[visibility transition test](../04_record_frame/proof_formation_visibility_transition_test_v0.1.md) では provenance を持つ H9/H10 が R0–R3 では見えず、R4 で初めて分離した。ただしこれは R4 の正しさを示さない。

さらに [non-nested replication](../04_record_frame/proof_formation_non_nested_frame_replication_test_v0.1.md) の N-family では、ある pair が visible→invisible→visible と変化した。従って visibility は frame richness の単調関数ではなく、`first visible` も frame-family の列挙順に依存した。provenance は、それを保持する frames では安定したが、普遍的 core ではなかった。

### 7.4 minimal separator と偶然の cue

[minimal separating field set test](../04_record_frame/proof_formation_minimal_separating_field_set_test_v0.1.md) は、各 history pair を区別する最小 field set を探索した。coordinate-wise projection の有限実験では、分離可能な pair はすべて separating singleton を持った。

しかし singleton の小ささは説明力を与えなかった。D5 では、介入の有無という意図した差と直接関係しない provenance cue が H8/C-F を単独で分離した。最小 separator は「この二 record は違う」を示しても、「数学的・歴史的に重要な差は何か」を特徴づけなかった。

この時点で、**minimal separator が intended distinction を characterize / explain するという主張は KILL** された。残ったのは field ablation inventory だけである。これは source map が記録する系列唯一の explicit KILL branch であり、この枝はここで終了した。

### 7.5 recurrence は法則ではない

この枝には次の historical recurrence があった。

\[
\begin{aligned}
\text{action} &\to \text{claim identity / episode boundary},\\
\text{semantic move} &\to \text{typed record},\\
\text{self-state} &\to \text{frame choice},\\
\text{frame-independent core} &\to \text{projector design},\\
\text{first-visible frame} &\to \text{frame-family order},\\
\text{visibility} &\to \text{separating basis},\\
\text{minimal separator} &\to \text{pair design / accidental cue}.
\end{aligned}
\]

これは universal displacement law ではない。有限な設計変更を追ったこの branch の履歴であり、後の finite termination controls は「問題は必ず外へ動く」「無限後退する」という一般化を支持しなかった。

### 7.6 checker の限界

五つの checker は有限 projection、pairwise distinguishability、visibility matrix、singleton separator を正しく再計算した。どの frame が正しいか、provenance が真か、区別が説明的に重要か、任意の record family で再現するかは判定していない。

### Primary records

- [record-frame sensitivity](../04_record_frame/proof_formation_record_frame_sensitivity_test_v0.1.md)
- [cross-frame persistence](../04_record_frame/proof_formation_cross_frame_persistence_test_v0.1.md)
- [visibility transition](../04_record_frame/proof_formation_visibility_transition_test_v0.1.md)
- [non-nested replication](../04_record_frame/proof_formation_non_nested_frame_replication_test_v0.1.md)
- [minimal separating field set](../04_record_frame/proof_formation_minimal_separating_field_set_test_v0.1.md)

---

## 8. reachability stress と退役

Phase 4 の branch termination 後、資料は再び個別定理へ移った。なぜこの方向転換が選ばれたかは source に説明されていない。当時は theorem / proof anatomy を、固定条件のもとで target へ至る derivation、具体的 route、formation history として読み替える案が試された。以下では、その当時の名称を歴史的に “reachability” と呼ぶが、現在の technical term としては使用しない。

### 8.1 (1+1=2): 最小 control

Peano-style numerals と

\[
x+0=x,\qquad x+S(y)=S(x+y)
\]

を固定すると、

\[
S(0)+S(0)=S(S(0)+0)=S(S(0))=2
\]

という inline derivation が得られる。同じ内容を lemma node 経由でも書ける。named lemma を library から除けばその displayed organization は壊れるが、inline 化すれば同じ theory と target で derivation は残る。

一方、Add-S または Add-0 を theory side から消すと、残った clause を満たし target を偽にする operation を自然数上に与えられる。ここで初めて、one route failure と reduced theory からの non-derivability が別の証拠を要することが明示された。numeral definition を消す場合には false より先に underdefinition が起こり、$\mathbb Z/2\mathbb Z$ へ移る場合には setting が変わる。

### 8.2 addition commutativity: induction と countermodel

第二引数について再帰定義された加法の可換律

\[
\forall x\forall y\,(x+y=y+x)
\]

には、standard modular proof で次の derived lemmas が使われた。

\[
L_1:\ 0+x=x,\qquad
L_2:\ S(x)+y=S(x+y).
\]

(L_1)、(L_2)、main theorem を induction で証明する route と、main induction variable を交換する route が比較された。named (L_1/L_2) の削除は inline proof または equivalent lemma で回避でき、lemma nodes は theorem assumptions ではなく route-level compression resources だった。

これに対して induction principle を除いた reduced theory には、standard successor chain に bi-infinite chain を付加した model を作り、defining equations を満たしながら commutativity を失わせることができた。Add-0 / Add-S の各削除にも explicit alternate operations が与えられた。従って、この限定された theory については non-derivability が countermodel + soundness によって支持された。ただし induction が唯一または最弱の原理であること、任意の alternative axiomatization に必要であることは示していない。

### 8.3 IVT: displayed dependency と expanded dependency

Intermediate Value Theorem では、二つの proof organizations が比較された。

1. 負値集合を作り $c=\sup S$ とし、continuity から $f(c)<0$ と $f(c)>0$ を排除する supremum proof。
2. $[a,b]$ の connectedness、continuous image of a connected set、connected subsets of $\mathbb R$ are intervals を使う proof。

displayed level では、一方は order completeness、他方は topology / connectedness を前面に出す。ところが「区間は connected」の標準 proof を一段展開すると least-upper-bound property が再び現れた。これは citation boundary の内側へ dependency が移っていたことを示す。

しかし、one chosen expansion に completeness が現れることは logical necessity の証明ではない。別の証拠として、$\mathbb Q$ の区間 $[1,2]\cap\mathbb Q$ 上の $q\mapsto q^2-2$ は連続で符号を変えるが rational root を持たない。この control が示すのは、ordered-field axioms alone では analogous IVT schema を保証しないことまでである。LUB formulation が唯一必要であることは示さない。また $\mathbb R\to\mathbb Q$ は standard real IVT の反証ではなく、specific intended structure から別 setting への変更でもある。

### 8.4 FTA: preregistered expansion boundary

Fundamental Theorem of Algebra では、

- zero-free polynomial (p) の reciprocal (1/p) を bounded entire function にして Liouville contradiction を得る analytic proof、
- large circle 上の (p) を leading term と homotopy し、zero-free disk extension の null-homotopy と winding number を衝突させる topological-heavy proof

が比較された。

ここでは dependency expansion を Level 0 / Level 1 / Level 2 と事前に固定し、Level 2 で停止した。Level 0 では Liouville と winding obstruction は明確に heterogeneous だった。Level 1–2 では continuity と elementary compactness を共有したが、その役割は異なった。analytic route では compact disk 上の boundedness を globalize し、topological route では parameterized lifts / homotopies の局所情報を globalize した。core support は Cauchy integral theory と covering-space lifting に分かれたままだった。

選択された winding/lift route は Level 2 まで Cauchy theory を再輸入しなかった。argument principle を使う別 route なら analytic machinery が入るため、proof selection に依存する。逆に analytic route は compactnessを使うが、winding や fundamental group を使わなかった。従って displayed heterogeneity は expansion で消滅しなかったが、それを theorem-intrinsic property とする根拠もなかった。

$p=1$ は nonconstant hypothesis、$e^z$ は finite polynomial object class が load-bearing であることを示した。一方、$\mathbb Q(i)$ は incomplete かつ non-algebraically-closed なので、completeness alone の必要性を判定する control には confounding がある。completeness、compactness、Cauchy theory、winding number の theorem-level necessity は **NOT ESTABLISHED** のまま残った。

### 8.5 cross-test audit と語彙の退役

四 tests を横断すると、当時の中心語は次へ無損失に翻訳できた。

| 当時の語 | 最終的に使う標準語 |
|---|---|
| reachability | derivability、$\Gamma\vdash\varphi$ |
| route | proof / derivation organization |
| constraint propagation | ordinary proof bookkeeping |
| imported theorem expansion | citation expansion / dependency tracing |
| setting migration | theory、structure、domain、interpretation の変更 |

“theorem as compressed reachability” は、$\Gamma\vdash\varphi$ が proof の存在を assert するという通常の意味を越えなかった。proof-as-route も derivation と proof organization を越えなかった。dependency の再出現は参照先を展開する通常の作業だった。

従って [cross-test audit](../05_reachability_stress/theorem_proof_anatomy_reachability_cross_test_audit_v0.1.md) と [synthesis closure](../05_reachability_stress/theorem_proof_anatomy_reachability_synthesis_closure_v0.1_ja.md) は、rewrite を「postponed」ではなく **RETIRED** とした。ここで退役した語彙を本稿の現在の分析装置として復活させない。

退役後にも一つの小さい audit improvement は残った。

\[
\text{displayed proof failure}
\neq
\text{non-derivability in a reduced theory}
\neq
\text{change of setting or claim}.
\]

これは新理論ではない。それぞれに alternative derivation、countermodel / independence argument、interpretation audit という異なる証拠を要求する、標準的だが実務上有効な区別である。

### Primary records

- [(1+1=2) stress test](../05_reachability_stress/theorem_proof_anatomy_reachability_test_1_plus_1_eq_2_v0.1_ja.md)
- [addition commutativity stress test](../05_reachability_stress/theorem_proof_anatomy_reachability_test_addition_commutativity_v0.1_ja.md)
- [IVT stress test](../05_reachability_stress/theorem_proof_anatomy_reachability_test_ivt_v0.1_ja.md)
- [FTA stress test](../05_reachability_stress/theorem_proof_anatomy_reachability_test_fta_v0.1_ja.md)
- [cross-test audit](../05_reachability_stress/theorem_proof_anatomy_reachability_cross_test_audit_v0.1.md)
- [synthesis closure](../05_reachability_stress/theorem_proof_anatomy_reachability_synthesis_closure_v0.1_ja.md)

---

## 9. theoremhood / proof equality / translation へ

Phase 5 の branch retirement 後、Phase 6 は同じ framing を続けなかった。中心対象は standard derivability judgment、proof object、equivalence relation、conservative extension、proof translation へ移った。五 pilots は約2時間に集中しており、長期の独立再検証ではない。

### 9.1 theoremhood が答えること、答えないこと

[theorem closure pilot](../06_theorem_proof_pilots/theorem_closure_open_remainder_pilot_v0.1_ja.md) は、固定した language、theory $\Gamma$、rules $R$、target $\varphi$ に対する

\[
\Gamma\vdash_R\varphi
\]

が何を assert するかを、(1+1=2)、加法可換律、IVT、FTA の既存四例で再確認した。

この judgment が settle するのは、fixed context で少なくとも一つの derivation が存在することである。proof choice、proof uniqueness、minimal assumptions、特定 resource の necessity、canonical proof equivalence、foundation choice、presentation choice、formation history は judgment 単独には含まれない。

各例には、theory と target を維持した variation があった。inline / lemma、induction variable、supremum / connectedness、Liouville / winding の差である。従って、判断が答えない項目は単なる「私たちの情報不足」だけではなく、判断の内容に符号化されていない。もっとも、それらが数学的に unknowable だという意味ではない。reverse mathematics や proof identity theory が別途答える可能性は残る。

“closure” や “open remainder” は新 object にならず、fixed-context theoremhood と judgment が assert しない別 questions という標準的記述へ戻された。

### 9.2 stronger statement と finite minimality

[judgment enrichment pilot](../06_theorem_proof_pilots/theorem_judgment_enrichment_boundary_pilot_v0.1_ja.md) は、判断が含まない情報を明示的に statement へ加えると何が変わるかを調べた。

IVT では、単に proof exists とする代わりに、supremum proof の特定 representation $\pi_{\sup}$ が proof predicate を満たすと指定すれば、「which displayed witness?」は settle した。ただし alpha-renaming、citation expansion、macro use、bureaucratic rearrangement を同じ proof と呼ぶには、calculus、syntax、expansion policy、equivalence relation を別途固定する必要があった。informal IVT records だけから formal proof-object identity は判定できなかった。

加法可換律では、tested finite set \(\{\mathrm{Add0},\mathrm{AddS},\mathrm{Ind}\}\) の各 deletion が derivability を壊すことを countermodels で確認し、その **chosen finite deletion order における deletion-minimality** を settle できた。これは arbitrary weakening、restricted induction schema、alternative recursion axioms、weakest equivalent base theory を settle しない。

重要な positive control は、有限 poset / deletion set を固定すれば minimality question が実際に terminate したことである。「一つを固定すると問題が必ず外へ移る」という universal claim は falsified され、infinite regress は確立されなかった。追加 specification が必要なことは、より強い真理や intrinsic ontology を示さない。

### 9.3 quotient in STLC

[proof quotient pilot](../06_theorem_proof_pilots/theorem_proof_quotient_invariance_pilot_v0.1_ja.md) は simply typed lambda calculus with products を固定し、raw syntax、alpha、beta、eta、product beta/eta を別々に比較した。

\[
\lambda x.x\quad\text{と}\quad\lambda y.y
\]

の差は alpha quotient で消え、

\[
\lambda x.(\lambda z.z)x
\]

の detour は beta normalization で消えた。function / product eta equations はそれぞれ対応する expansion bureaucracy を消した。

しかし同じ type $A\times A\to A$ の

\[
\lambda p.\pi_1p
\qquad\text{と}\qquad
\lambda p.\pi_2p
\]

は、採用した full alpha-beta-eta-product equations の下でも異なる normal proof classes に残った。従って unique normal form per term は unique proof per proposition を含意しない。quotient は選んだ equations が許す差だけを消し、class count 自体が equivalence relation に依存した。

companion checker は16 terms の typing、selected reductions、class counts を確認したが、STLC の strong normalization や confluence の一般定理を証明していない。quotient は proof essence の extractor ではなかった。

### 9.4 specification change

[specification-change pilot](../06_theorem_proof_pilots/theorem_specification_change_preservation_pilot_v0.1_ja.md) は、保存を一つの言葉で済ませず、source / target specification、map、object、scope、direction、evidence を固定した。

- **bijective renaming:** literal formula は変わるが、renaming と inverse renaming により translated derivability は iff で保たれ、proof tree は nodewise transport できた。
- **derived lemmas の追加:** 加法可換律の $L_1,L_2$ は元 theory から導出済みなので、同じ language で axioms/resources として追加しても deductive closure は変わらない。しかし proof length、named citations、organization は変わり得る。
- **explicit definitional extension:** fresh symbol $d\leftrightarrow(P\land Q)$ は elimination translation により old-language consequences を conservative に保つ。一方、extended language の formulas、vocabulary、proof records は新しくなる。
- **genuine strengthening:** induction を追加すれば source derivations は monotonicity で forward に保存されるが、commutativity の countermodel により reflection は失敗する。

同じ theoremhood、same old-language theorem set、literal identity、semantic satisfaction、proof translation、raw proof identity は別 claims だった。単一の universal preserved object は得られず、conservativity、monotonicity、reflection、translation という標準語で尽くされた。

### 9.5 cross-calculus proof classes

[cross-calculus pilot](../06_theorem_proof_pilots/theorem_cross_calculus_proof_class_preservation_pilot_v0.1_ja.md) は、derivability equivalence が chosen proof equalities の quotient classes まで持ち上がるかを調べた。

**Pair A: natural deduction ↔ STLC.** Implication と conjunction / products の rules、term constructors、beta/eta equations を対応させた Curry–Howard presentation では、translation は constructorwise で、classes 上 well-defined、injective、surjective、両 round trips は equality up to で成立した。この強さは両 calculus を matching presentation として選んだ standard correspondence に由来し、全 calculi の proof identity を示さない。

**Pair B: natural deduction ↔ single-conclusion LJ fragment.** derivability は双方向に保存された。しかし raw LJ equality を採ると、ND で beta-equivalent な identity proof と beta-expanded proof の translations が、cut を含む derivation と cut-free derivationとして raw-distinct になった。従って ND beta classes から raw LJ derivations への map は **well-defined でさえない**。

cut reduction、identity equations、independent rule permutations を含む標準的な matching conversions $E_{\mathrm{perm}}$ を固定すると、tested generators 上で quotient maps は well-defined になった。$U_BT_B\simeq\mathrm{id}$ により ND→LJ は classes 上 injective、LJ→ND は surjective となった。

しかし arbitrary LJ derivations の全 coherence cases は列挙・証明されず、external coherence theorem も引用されなかった。従って

\[
T_BU_B\simeq\mathrm{id},
\]

ND→LJ の global surjectivity、LJ→ND の global injectivity、Pair B の global bijection はすべて **NOT ESTABLISHED** である。証拠がないことを non-surjectivity の証拠にはしていない。

また、二つの cut-free raw LJ derivations $L_{\mathrm{once}},L_{\mathrm{twice}}$ は permutation equality で collapse し得た一方、first / second projection proofs は quotient 後も distinct だった。従って cut-free は canonical proof を意味しない。ND normalization と LJ cut elimination も、対応する detour を消す別 operations であり、同一操作ではない。

この phase の中心結果は、

\[
\Gamma\vdash_{C_0}\varphi
\iff
\Gamma\vdash_{C_1}\varphi
\]

が proof-set nonemptiness の対応しか与えず、proof translation、quotient descent、injectivity、surjectivity、round trips はそれぞれ別に検査しなければならない、という標準的区別だった。

### 9.6 Phase 6 の総括

五 pilots は、theoremhood の「外側」に新しい object を発見しなかった。むしろ、問いを precise にするたびに次の standard parameters が必要になった。

- proof syntax と calculus
- proof equality
- comparison class / weakening order
- formula translation
- source / target language
- preservation direction
- proof translation と round-trip equations

固定後の有限 questions は普通に terminate し得た。essence、intrinsic proof identity、outward displacement、infinite regress、universal preservation notion は支持されなかった。

### Primary records

- [theoremhood pilot](../06_theorem_proof_pilots/theorem_closure_open_remainder_pilot_v0.1_ja.md)
- [stronger-statement pilot](../06_theorem_proof_pilots/theorem_judgment_enrichment_boundary_pilot_v0.1_ja.md)
- [STLC quotient pilot](../06_theorem_proof_pilots/theorem_proof_quotient_invariance_pilot_v0.1_ja.md)
- [quotient checker](../06_theorem_proof_pilots/theorem_proof_quotient_invariance_pilot_v0.1.py)
- [specification-change pilot](../06_theorem_proof_pilots/theorem_specification_change_preservation_pilot_v0.1_ja.md)
- [cross-calculus pilot](../06_theorem_proof_pilots/theorem_cross_calculus_proof_class_preservation_pilot_v0.1_ja.md)

---

# Part III — Closure

## 10. 残ったもの

### 10.1 中心 artifact: evidence-burden table

系列全体で最も強く残った結果は、新しい mathematical object ではなく、**主張の論理形に証拠の型を合わせる**という監査規律である。次表は、Phase 0 の control discipline、Phase 5 の existential / universal 分離、Phase 6 の translation / quotient checks を一つに集約する。

| Claim | Logical form | Sufficient evidence | Insufficient evidence |
|---|---|---|---|
| **this displayed proof fails** | 特定 witness についての否定 | 指定 step / citation / rule が使えず、その derivation が閉じないことを示す | 他の proof が見つからないこと。theorem の非導出 |
| **theoremhood survives** | proof の存在 | 同じ theory・rules・target で一つの alternative derivation を与える | proof survey。元 proof の修理不能だけ |
| **target is non-derivable** | 全 derivations についての否定 | reduced theory の model で target を偽にし、soundness を使う。または independence argument | 失敗した proof attempts、citation tracing、二つの known proofs の破壊 |
| **a hypothesis is necessary for this formulation** | weakened statement への counterexample の存在 | 他条件を保持し当該 hypothesis を外した explicit counterexample | 一つの proof がその hypothesis を使うこと。最弱 base theory の主張 |
| **the setting / claim changed** | identity と interpretation の監査 | domain、symbol interpretation、object class、target translation の差を明示 | 変更前後の truth value の比較だけ |
| **forward derivability is preserved** | source derivations 全体への写像 | rules / derivations による induction、または replay construction | selected examples の一致 |
| **reflection holds** | target derivability から source derivability への全称含意 | inverse translation、elimination theorem、conservativity / reflection proof | monotonicity、forward translationだけ |
| **a proof translation exists** | 各 source proof への target proof construction | constructorwise definitionと typing / conclusion preservation の induction | theorem-set equality、proof existence の対応 |
| **translation descends to quotient** | source equalityをtarget equalityが尊重 | source equalityの各 generatorについて images が target-equivalent と示す | translationの存在。代表例だけ。generator一つの未検査 |
| **injective on proof classes** | image equalityからsource equality | left inverse up to chosen equality、または全 image classes の separation | well-definedness、derivability equivalence、translation existence |
| **surjective on proof classes** | 各target classにpreimageが存在 | right inverse up to equality、または全classesへのpreimage construction | injectivity、各formulaで proof が存在すること |
| **proof-class correspondence** | well-definedness + injectivity + surjectivity | 両 quotient maps と両 round trips、または同等の coherence theorem | selected examples、片側 round trip、derivability equivalence |

この表の要点は、単なる「強い主張には強い証拠が要る」ではない。具体的には、**existential claim を一つの witness で証明できる場合と、universal negative を countermodel / independence で支える場合を交換しない**ことである。

### 10.2 表は一度に発見されたのではない

この discipline の genealogy は三段階に分かれる。

1. **Phase 0:** field-native control、Erasure Test、time slice、kill criteria が、一般語彙の追加価値と普遍主張を監査した。
2. **Phase 5:** alternative proof は theoremhood survival の existential evidence、countermodel は non-derivability の universal evidence、setting change は identity audit だと分けた。
3. **Phase 6:** map の存在、equality preservation、reflection、injectivity、surjectivity、round trips を別 obligations として検査した。

後半ほど executable checks は増えたが、結論の novelty が増えたわけではない。checker は狭い finite facts を確かめ、general theorem は標準 proof theory / model theory の証拠に依存した。

### 10.3 concrete anchors

この規律を抽象 slogan にしないため、系列内の代表例を対応させる。

- (L_2) named lemma の削除後に inline proof が残ることは theoremhood survival を示すが、lemma content の不必要性は示さない。
- induction-free model は specified reduced arithmetic theory から Comm が non-derivable であることを示すが、induction が weakest possible support であることは示さない。
- $\mathbb Q$ 上の $q^2-2$ は ordered-field assumptions alone が analogous IVT に不足することを示すが、LUB axiom の唯一必要性は示さない。
- FTA の二 proof が compactness を共有しても、それは theorem-level necessity を示さない。実際、その necessity は未確立だった。
- $\lambda p.\pi_1p$ と $\lambda p.\pi_2p$ は normal forms の一意性と proposition-level proof uniqueness の差を示すが、proof identity 一般を否定しない。
- ND→raw LJ の failure は quotient map の well-definedness が equality choice に依存することを示すが、matching quotient での global non-bijection は示さない。

### 10.4 novelty judgment

系列内 audit の判定は **Option 2: coherent methodological result, no new mathematics** だった。最高 novelty rating は C で、対象は checklist / combined workflow である。A は textbook facts、B は監査上有用な標準事実、C はそれらを一つの反証的 workflow として継続使用したことに対応する。D/E に相当する新概念・新定理・新 framework はなかった。

これは「実験に価値がなかった」という結論ではない。価値は、新語を保存したことではなく、誤った証拠推論を具体例と countercontrols で止める手順にある。ただし audit 自身も、この判定は Option 1 と僅差であり、evidence table と同一診断の反復を除けば textbook rediscoveries の集積に近い、と自己限定した。

### Primary records

- [trajectory summary §11](../00_origin/tool_truth_absence_research_trajectory_summary.md#11-研究全体を通じて残った方法上の規律)
- [addition commutativity test](../05_reachability_stress/theorem_proof_anatomy_reachability_test_addition_commutativity_v0.1_ja.md)
- [IVT test](../05_reachability_stress/theorem_proof_anatomy_reachability_test_ivt_v0.1_ja.md)
- [FTA test](../05_reachability_stress/theorem_proof_anatomy_reachability_test_fta_v0.1_ja.md)
- [cross-calculus pilot](../06_theorem_proof_pilots/theorem_cross_calculus_proof_class_preservation_pilot_v0.1_ja.md)
- [full-series audit](./theorem_proof_anatomy_full_series_independent_audit_v0.1.md)

---

## 11. 捨てたもの

廃棄した主張を一つの “false” にまとめない。明示的 counterexample で falsified されたもの、証拠不足で unsupported のもの、定義が結論を埋め込み ill-posed だったもの、標準語へ還元されたもの、歴史的 descriptive vocabulary として退役したものを分ける。

### 11.1 falsified

| Claim | Status | Evidence and limit |
|---|---|---|
| 観測成功から universal ontological non-identifiability が従う | **FALSIFIED** | $O=\mathrm{id}$。ただし個別 inverse problem の非識別性は否定しない |
| self-containment alone が universal non-identifiability を含意 | **FALSIFIED** | finite encoder / reversible self-description controls。条件付き自己測定限界は否定しない |
| normalization が proposition ごとに unique proof を与える | **FALSIFIED for the concrete reading** | $A\times A\to A$ の二 projections |
| cut-free proof は canonical proof である | **FALSIFIED for the tested reading** | raw-distinct cut-free LJ derivationsとdistinct projection proofs |
| theoremhood の同値から proof-class correspondence が自動的に従う | **FALSIFIED** | ND→raw LJ translation が quotient に descend しない |
| problem specification は必ず外へ移動し、finite fixing が停止しない | **FALSIFIED as a universal claim** | finite deletion-minimality と finite quotient classification が終了した |
| quotient が全 presentation dependence を消す | **FALSIFIED** | equivalenceを変えるとclassesが変わり、distinct normal classesも残った |

### 11.2 unsupported / NOT ESTABLISHED

| Claim | Status | Reason |
|---|---|---|
| H3 universal residual pattern | **UNSUPPORTED** | R2 が稀で特定 clusters に偏った |
| move code の reader-independent uniqueness | **UNSUPPORTED** | core reconstruction は一致したが codes と boundaries が不一致 |
| theorem-level necessity of completeness / compactness / Cauchy / winding for FTA | **NOT ESTABLISHED** | proof use と common expanded support しかなく、independent necessity evidenceがない |
| Pair B ND↔LJ の global proof-class bijection | **NOT ESTABLISHED** | 一方の round trip と全 coherence cases が未証明 |
| infinite regress in specification | **UNSUPPORTED** | finite examplesから無限一般化できず、termination controlsがある |
| general comparative advantage over field-native review | **UNSUPPORTED** | GST、metrology、standards controlsで追加診断が残らなかった |

`NOT ESTABLISHED` は `NO` ではない。とくに Pair B は failure counterexample があるのではなく、global coherence theorem が本系列で用意されなかった。

### 11.3 ill-posed / underspecified

generation–log non-isomorphism は「log は lossy」と定義すれば循環し、可逆 coding を許せば一般には成立しない。`true core`、`intrinsic proof identity`、`theorem essence`、`representation-free proof`、`final foundational layer` のような essence-shaped claims も、どの equality、comparison class、map、scope を問うかがない限り、true / false を判定できる形にならなかった。

正しい最終記述は次である。

> essence-shaped claims were repeatedly underspecified and therefore not testable until translated into standard, relation-relative questions.

これは「essence は存在しないと証明した」という意味ではない。具体的な読みへ落としたときに反例で壊れたものと、そもそも testable claim にならなかったものを区別する。

### 11.4 reduced to standard terminology

| Historical working expression | Standard replacement / result |
|---|---|
| premise stack / web of constraints | auxiliary assumptions、applicability、assurance / traceability |
| semantic move identity | model-set transformation + typed revision record |
| frame-independent core | invariance under an explicitly chosen family of projections |
| minimal separator as explanation | finite feature ablation / pairwise distinguishability |
| reachability | derivability |
| route | derivation / proof organization |
| constraint propagation | proof bookkeeping |
| dependency relocation | citation expansion / dependency tracing |
| open remainder | questions not asserted by a derivability judgment |
| judgment enrichment | strengthening a statement / adding a proof predicate or minimality clause |
| specification preservation | renaming、conservativity、monotonicity、reflection、translation |
| cross-calculus preservation | quotient descent、injectivity、surjectivity、round trips、coherence |

### 11.5 retired descriptive vocabulary

- `R0/R1/R2` は v1.1 の21-theorem condition-removal survey 内でのみ歴史的役割を保持する。外部の general taxonomy としては RETIRE。
- `closure / escape route / blocking / residual` は Phase 1 の比較メタ記述として保存するが、technical proof-theoretic terms としては RETIRE / DOWNGRADE。
- `M1–M17` と `K/A/R/D/U` は corpus coding の記録として保存する。reader-independent ontology や score にはしない。
- “reachability-oriented theorem/proof anatomy” は **RETIRED**。v2 line は再開しない。
- “open remainder”、“judgment enrichment”、“quotient invariance”、“specification preservation”、“cross-calculus proof-class preservation” は pilot titles の歴史として残すが、独立 technical terms としては RETIRE。
- theorem essence、intrinsic proof identity、canonical proof geometry、universal preserved object は採用しない。

### 11.6 what was not discarded

語彙や強い hypotheses の退役は、元の数学や標準方法の否定ではない。IVT、FTA、normalization、cut elimination、conservativity、Curry–Howard correspondence は、その標準的内容のまま残る。また proof histories、provenance、citation boundaries が実務上無意味になったわけでもない。否定されたのは、それらから一意的・普遍的・本質的な structure を追加証拠なしに読むことだった。

### Primary records

- [finite propositional postmortem](../03_finite_propositional/proof_formation_finite_propositional_postmortem_architecture_v0.1.md)
- [minimal separating field test](../04_record_frame/proof_formation_minimal_separating_field_set_test_v0.1.md)
- [reachability synthesis closure](../05_reachability_stress/theorem_proof_anatomy_reachability_synthesis_closure_v0.1_ja.md)
- [quotient pilot](../06_theorem_proof_pilots/theorem_proof_quotient_invariance_pilot_v0.1_ja.md)
- [cross-calculus pilot](../06_theorem_proof_pilots/theorem_cross_calculus_proof_class_preservation_pilot_v0.1_ja.md)
- [full-series audit](./theorem_proof_anatomy_full_series_independent_audit_v0.1.md)

---

## 12. 境界と停止

### 12.1 where theorem anatomy ends

“theorem anatomy” という名称が適切に指す範囲は、個別 theorem statement、hypotheses、condition types、proof resources、condition removal の監査である。v1.1 と四 theorem stress tests はこの範囲にある。

後半は対象領域が異なる。

系列内 audit は theorem サブ系列を A–F と呼んだため、本稿の Phase 0–7 とは番号体系が異なる。対応は次の通りである。

| 本稿の phase | 系列内 audit の呼称 | 対象領域 |
|---|---|---|
| Phase 5 | Phase A | 定理の条件と証明資源：theorem anatomy proper |
| Phase 6 の第1 pilot | Phase B | 判断が何を主張するか：ordinary logic |
| Phase 6 の第2 pilot | Phase C | statement strengthening：ordinary logic |
| Phase 6 の第3 pilot | Phase D | STLC の alpha-beta-eta：type theory / structural proof theory |
| Phase 6 の第4 pilot | Phase E | conservativity、definitional extension：metatheory |
| Phase 6 の第5 pilot | Phase F | Curry–Howard、Gentzen translation、cut elimination：proof theory proper |

| 対象 | より正確な標準領域 |
|---|---|
| $\Gamma\vdash\varphi$ が何を assert するか | judgment semantics / metatheoretic bookkeeping |
| STLC proof terms の alpha-beta-eta quotient | type theory / structural proof theory |
| derived-lemma addition、definitional extension、reflection | metatheory、conservativity、translation theory |
| ND / LJ proof translations と proof equality | proof theory proper、coherence questions |
| Phase 2–4 の corpus / record frames | record design と audit methodology。proof theoryではない |

従って “theorem anatomy” は後半へ行くほど広すぎた。系列内 audit の別記号では Phase D で broad、Phase F で misleading とされたが、本稿の Phase 0–7 とその A–F label は混用しない。ここでは対象領域を標準分野名で分けるだけにする。

### 12.2 why stop

停止には三つの独立した根拠がある。

#### A. cross-calculus pilot の証拠境界

Pair B の global bijection を解くには、任意 LJ derivation に対する complete coherence argument または適切な literature theorem が要る。selected examples と generator checks を増やすだけでは全称 claim を満たさない。従って次の informal pilot を重ねることは正当化されない。

#### B. full-series audit の判定

系列内 audit は **Option 2 — a coherent methodological result, but no new mathematics**、最高 novelty C、**STOP WITH SYNTHESIS** と判定した。これは外部 validation ではないが、本系列の事前 kill discipline に沿う停止判断である。さらに pilot を追加すれば、standard proof theory を標準文献より少ない資源で再演する可能性が高い。

#### C. proof-formation の preregistered gate

meta-experiment は L1 / L2 を framework claim 前の gate とした。現在の status は：

- **L1 PASS:** frozen corpus における local reconstructibility。
- **L2 NOT ATTEMPTED:** multiple independent corpora / teams による ordinary revision ledger を越える比較有用性は検査していない。

L2 を failed と書いてはならない。しかし、未実施の L2 を越えて general framework を主張せず、annotated trajectory / review として閉じることは、事前登録された evidential boundary に適合する。これは真理の最終境界ではなく、現在の experiment が持つ証拠の境界である。

### 12.3 open items

終了後にも三項目は別枝として残る。

#### O1 — external calibration

reverse mathematics、proof-theoretic strength、既知の necessity results などと、v1.1 の condition-removal claims を照合する作業。これは major resource necessity が未確立だった点を外部標準で校正できる。ただし closed pilot series を再開する理由にはしない。

#### O2 — Pair B coherence

chosen ND / LJ calculi と proof equalitiesについて、全 LJ proof classes に及ぶ round trip / bijection が成立するか。これは **NOT ESTABLISHED** の literature / coherence problem であり、selected-term pilot で代用しない。

#### O3 — proof-formation L2

複数 corpus・独立 teams・ordinary revision ledger control を用いた comparative utility test。status は **UNATTEMPTED**。現在閉じた annotated trajectory とは別 experiment である。

### 12.4 v1.1 の将来 revision scope

本稿は [theorem / proof anatomy v1.1](../01_theorem_anatomy/theorem_proof_anatomy_v1.1_ja.md) を変更しない。将来別作業で検討する revision は二点に限定する。

1. `what_fails_if_removed` を少なくとも次へ分ける。
   - displayed proof failure
   - non-derivability in the reduced theory
   - setting / interpretation change
2. `proof_resources` に citation depth / expansion depth の note を追加する。

これ以上は推奨しない。retired vocabulary を逆輸入せず、Phase 6 の translation machinery を追加せず、R0/R1/R2 を再定義せず、`theorem_proof_anatomy_v2` を作らない。v1.1 の hypothesis levels、condition types、six functional clusters、H2 / H3 の historical verdict は、その survey 自体の結果として保存する。

### 12.5 final assessment

この系列は、観測や証明の奥に隠れた本質を見つけて終わったのではない。成功する道具、成立した定理、書かれた証明のそれぞれについて、その周囲に置いていた問いを一つずつ形式化し、どの論理形式を持ち、何を先に固定させ、どの証拠を要求するのかを切り分け、そのたびに問いが既存分野の標準的な語彙へ戻っていくのを記録したところで終わった。残ったのは新しい理論ではなく、**主張の型に証拠の型を合わせるという監査規律**だけである。

no mathematically new concept emerged. これは失敗を隠す文でも、全作業を無価値とする文でもない。普遍的 non-identifiability、residual pattern、semantic move identity、frame-independent core、minimal separator、new derivability primitive、proof essence、universal preservation、automatic cross-calculus correspondence といった候補を、反例、有限 control、reader disagreement、countermodel、translation check によってそれぞれ適切な status へ下げた、という実験記録である。

ここで停止する。

### Primary records

- [proof-formation meta-experiment](../02_proof_formation/proof_formation_meta_experiment_v0.1.md)
- [reachability synthesis closure](../05_reachability_stress/theorem_proof_anatomy_reachability_synthesis_closure_v0.1_ja.md)
- [cross-calculus pilot](../06_theorem_proof_pilots/theorem_cross_calculus_proof_class_preservation_pilot_v0.1_ja.md)
- [full-series independent audit](./theorem_proof_anatomy_full_series_independent_audit_v0.1.md)
- [source architecture](./theorem_proof_anatomy_experiment_source_architecture_v0.1_ja.md)

---

## Compact disposition ledger

| Item | Final experimental status |
|---|---|
| universal ontological non-identifiability from successful observation | FALSIFIED in the general form |
| self-containment implies universal non-identifiability | FALSIFIED |
| generation–log non-isomorphism | partly ILL-POSED / circular; general reading falsified by reversible controls |
| Phase 0 comparative methodology | terminated; comparative review only |
| v1.1 H2 functional distinctions | TENTATIVELY SUPPORTED within survey |
| v1.1 H3 universal residual pattern | UNSUPPORTED |
| M1–M17 local coding | L1 PASS, with code / boundary fragility |
| proof-formation L2 | NOT ATTEMPTED |
| semantic recovery of formation history | DOWNGRADED / negative |
| minimal separator as characterization | KILL |
| reachability-oriented rewrite / v2 | RETIRED / KILL as new line |
| theorem-level necessity from common proof resources | KILL as an inference rule |
| outward displacement / infinite regress | universal form falsified or unsupported |
| quotient as proof essence extractor | KILL |
| single universal preservation notion | KILL |
| derivability equivalence implies proof-class correspondence | KILL |
| Pair B global proof-class bijection | NOT ESTABLISHED |
| final novelty | Option 2; coherent methodology, no new mathematics |

**End of final experimental record.**

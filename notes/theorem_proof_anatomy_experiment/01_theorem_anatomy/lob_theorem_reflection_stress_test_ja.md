# Löb の定理：証明の解剖 special stress test

## 0. 目的と参照枠

本稿は、theorem_proof_anatomy_v1.1_ja.md、godel_incompleteness_closure_reversal_stress_test_ja.md、tarski_truth_undefinability_stress_test_ja.md の分析枠を継承し、算術的 Löb の定理を stress test する。

「閉包」「閉包反転」「残差」「断絶交渉」「内部化」「自己保証」「閉鎖条件」は比較用のメタ記述であって、標準 proof theory / provability logic の用語ではない。技術記述では provability predicate、Hilbert–Bernays–Löb derivability conditions、local reflection、fixed point、theoremhood を優先する。

検査原則は次である。

1. theorem assumptions と proof resources を分ける。
2. object / ambient / background / definitional を分ける。
3. 条件除去後を R0 / R1 / R2 で記録する。
4. syntactic provability、semantic truth、soundness、consistency を混同しない。
5. object theory と metatheory の位置を明示する。
6. diagonal fixed point を自然言語の liar paradox と同一視しない。
7. 標準語彙の方が精密なら標準語彙を優先する。

# 1. 採用版の固定

## 1.1 主分析：算術的 Löb の定理

固定した計算可能な公理提示を持つ古典一階算術理論 \(T\supseteq I\Sigma_1\) を採用する。有限な \(T\)-証明の標準的算術化から得られる \(\Sigma_1\) provability predicate を

\[
\mathrm{Pr}_T(x)\;:\!\equiv\;\exists p\,\mathrm{Prf}_T(p,x)
\]

とする。任意の \(T\)-文 \(\varphi\) について、

\[
T\vdash \mathrm{Pr}_T(\ulcorner\varphi\urcorner)\to\varphi
\quad\Longrightarrow\quad
T\vdash\varphi
\]

である。

\(I\Sigma_1\) は、標準的な構文算術化、\(\Sigma_1\) 完全性、導出可能性条件を一括して安全に扱える代表的な下限として採用した。diagonal lemma 自体は \(Q\) 程度のより弱い理論でも得られるが、単に \(T\supseteq Q\) と書くだけでは、選んだ provability predicate に対する D1–D3、とりわけ D3 の内部検証まで自動的に明示したことにはならない。本稿は最弱の基礎理論を求めず、標準版を固定する。

整合性は Löb の定理そのものの仮定ではない。\(T\) が矛盾していれば結論 \(T\vdash\varphi\) は自明に成立する。整合性は、\(\varphi\equiv0=1\) として第2不完全性定理を系として取り出す際に用いる。

## 1.2 Hilbert–Bernays–Löb derivability conditions

\(\Box\varphi\) を \(\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\) の略記とする。

- **D1:** \(T\vdash\varphi\Rightarrow T\vdash\Box\varphi\)。これは外部の theoremhood を入力とするメタレベルの schema である。
- **D2:** \(T\vdash\Box(\varphi\to\psi)\to(\Box\varphi\to\Box\psi)\)。
- **D3:** \(T\vdash\Box\varphi\to\Box\Box\varphi\)。

D2・D3 は各 \(\varphi,\psi\) に対する \(T\) 内部の formula schema である。D3 は semantic な「体系が自分の真理を知る」ことではなく、証明可能性主張をもう一度 provability predicate の対象へ入れられるという構文的性質である。

# 2. 通常15項目＋special stress-test

1. **theorem_name:** 算術的 Löb の定理

2. **domain:** 数理論理・証明論・provability logic

3. **standard_statement:** 固定した計算可能な公理提示を持つ古典一階算術理論 \(T\supseteq I\Sigma_1\) と、その提示に関する標準的 provability predicate \(\mathrm{Pr}_T(x)\) を取る。これが D1–D3 を満たすとき、任意の \(T\)-文 \(\varphi\) について、\(T\vdash\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\to\varphi\) なら \(T\vdash\varphi\) である。

4. **assumptions_ABC:**
   - A: \(T\) は必要な構文・有限証明・初等計算を算術化できる古典一階算術理論であり、本稿では \(T\supseteq I\Sigma_1\)
   - B: \(T\) は固定した計算可能な公理提示を持ち、有限証明関係を効果的に coding できる
   - C: その提示から標準的 provability predicate \(\mathrm{Pr}_T(x)\) を固定する
   - D: \(\mathrm{Pr}_T\) が D1–D3 を満たす
   - E: \(\varphi\) は \(T\) の言語の文
   - F: \(T\vdash\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\to\varphi\)。固定した一文についての local reflection instance が \(T\) で可証、という主要条件
   - G: 通常のメタ理論で自然数、finite proof、Gödel code、\(T\vdash\cdot\) を扱う

5. **hypothesis_levels:**
   - A: ambient＋object。論理・算術の舞台と \(T\) の強さ
   - B: object。理論の公理提示に課される効果性
   - C: definitional＋object。どの proof relation を算術化した述語かを固定
   - D: object。固定した predicate に課される proof-theoretic 条件
   - E: definitional。代入・Gödel code・theoremhood の対象を確定
   - F: object。内部 formula に関する外部の可証性条件
   - G: background。object theory \(T\) の追加公理ではない

6. **condition_types:**
   - A: 算術的表現力・古典一階形式性
   - B: 効果的公理化・proof coding
   - C: 証明可能性述語の標準性・提示依存性
   - D: 導出可能性条件・内部推論保存・positive introspection
   - E: 言語適合性
   - F: 局所反射条件
   - G: メタ数学的背景

7. **closure_roles:**
   - A: expressive strength / fixed-point enablement
   - B: effective proof coding
   - C: syntax-to-provability bridge
   - D1: theoremhood recognition
   - D2: derivability closure / internalized modus ponens
   - D3: positive introspection / iterated provability
   - E: domain enclosure
   - F: internal reflection / provability-to-content bridge
   - G: meta-level verification

   self-reference は独立の仮定ではない。A–D が構文と provability の内部表現を可能にし、proof resource である diagonal lemma が固定点を与える。

8. **conclusion_P:** \(T\vdash\varphi\) である。これは \(\varphi\) が標準モデルで真、\(T\) が sound、または \(\Box\varphi\to\varphi\) が外部的に真である、という結論ではない。結論は固定した \(T\) における syntactic theoremhood だけである。

9. **blocked_escape_routes:**
   - A: provability と自分の構文について fixed-point argument を行えないほど弱い体系へ退く道を塞ぐ
   - B: proof set を非効果的・未符号化の認可関係にして \(\mathrm{Prf}_T\) を算術化できなくする道を塞ぐ
   - C: provability を任意の人工述語へ読み替える自由を制限し、固定公理提示の有限証明へ結びつける
   - D1: 実際に得られた \(T\)-定理を \(\Box\) が認識しない道を塞ぐ
   - D2: implication と modus ponens を \(\Box\) 内で追跡できない道を塞ぐ
   - D3: \(\Box\lambda\) から \(\Box\Box\lambda\) へ進めず、証明可能性の反復が切れる道を塞ぐ
   - E: \(\varphi\) やその code が対象言語外にあるという型のずれを防ぐ
   - F: \(\Box\varphi\) から内容 \(\varphi\) へ戻る橋を \(T\) 自身が持たない、という通常の状態を排除する
   - G: D1 の適用、fixed point の存在、最終 theoremhood を外部から確認する場所を確保する。ただし \(T\) 内の逃走経路ではない

10. **what_fails_if_removed:**
   - Aを外すと: diagonalization や構文表現に足りない弱い体系では採用版を適用できない。直ちに反例を与えるというより、同じ定理文の枠組みが失われる
   - Bを外すと: 標準的 arithmetized proof predicate を得る保証がない。完全だが非効果的な theory の derivability は別問題
   - Cを外すと: Rosser provability、slow provability、人工的 provability-like predicate など多数の選択肢が生じ、標準述語についての結論をそのまま移せない
   - D1を外すと: \(P(x)\equiv\bot\) とし、\(T\) の非定理 \(\varphi\) を取る。D2・D3 型の式と \(T\vdash P(\ulcorner\varphi\urcorner)\to\varphi\) は成立するが \(T\nvdash\varphi\)。実際の定理を \(P\) が認識しないためである
   - D2を外すと: \(\Box(\lambda\to\cdots)\) と \(\Box\lambda\) から必要な provability conclusion を内部で運べない。D1・D3だけから Löb 結論が一般に従うとはいえない。ただし個々の条件の最小独立性は predicate の設計に敏感であり、単純な標準述語の反例は捏造しない
   - D3を外すと: 標準証明の核心 \(\Box\lambda\to\Box\Box\lambda\) が失われる。positive introspection を欠く非標準的 provability-like predicate に Löb 原理を一律適用できず、D1・D2だけで十分とは主張しない
   - Eを外すと: \(\ulcorner\varphi\urcorner\) と \(\Box\varphi\) の定式化が対象言語内で閉じず、型不適合になる
   - Fを外すと: Löb の trigger がないので、任意の非定理 \(\varphi\) がそのまま候補になり、定理は可証性を強制しない
   - Gを外すと: object theory が反例になるのでなく、D1、fixed point、\(T\vdash\varphi\) を述べるメタ数学的枠が失われる
   - reflection を formula class に制限すると: local / uniform restricted reflection theory へ移る。外部の強い理論が \(T\) の制限反射を証明する場合を Löb は禁止しない

11. **what_reappears_if_removed:**
   - A: **R1** — 限定された self-reference、decidability、別の弱い proof theory が現れ得る。ただし一律の反例定理ではない
   - B: **R0/R1** — 標準 proof predicate が定まらなければ枠組みは失われる（R0）。別の非効果的 derivability notion を選べば自由度が現れる（R1）
   - C: **R1** — provability predicate dependence と非標準述語の自由度
   - D1: **R1** — theoremhood と predicate extension のずれ
   - D2: **R1** — implication transport を保存しない derivability notions
   - D3: **R1** — positive introspection を欠く notions と反復 provability の未処理自由度
   - E: **R0** — 型不適合により同じ定理文が成立しない
   - F: **R0** — trigger condition が消えるだけで自然な補正項はない
   - restricted reflection: **R1** — formula-class relative reflection、stronger theory、proof-theoretic strength の段階
   - G: **R0** — theoremhood judgment の背景が失われる

   全体判定は R1 である。現れるのは述語選択、反射範囲、理論拡張などの altered freedom であり、Stokes 型の明示的補正項ではない。R2 は採用しない。

12. **proof_resources:**
   - representative_route: diagonal lemma と D1–D3 を用いる標準的内部導出
   - resources:
     - Gödel numbering と finite proof relation の算術化
     - 標準 provability predicate
     - diagonal / fixed-point lemma
     - D1–D3
     - propositional reasoning inside \(T\)
   - proof skeleton:
     1. **metatheory:** diagonal lemma により \(\lambda\) を選び、\(T\vdash\lambda\leftrightarrow(\Box\lambda\to\varphi)\) を得る。
     2. **metatheory→object theory:** \(T\vdash\lambda\to(\Box\lambda\to\varphi)\) に D1 を適用し、その theoremhood を \(\Box\) 内へ写す。
     3. **object theory:** D2 を使い、\(T\vdash\Box\lambda\to\Box(\Box\lambda\to\varphi)\) を得る。
     4. **object theory:** D2 から \(T\vdash\Box(\Box\lambda\to\varphi)\to(\Box\Box\lambda\to\Box\varphi)\)、D3 から \(T\vdash\Box\lambda\to\Box\Box\lambda\)。従って \(T\vdash\Box\lambda\to\Box\varphi\)。
     5. **object theory:** 仮定 \(T\vdash\Box\varphi\to\varphi\) と合わせて \(T\vdash\Box\lambda\to\varphi\)。fixed-point biconditional の逆向きから \(T\vdash\lambda\)。
     6. **metatheory→object theory:** D1 により \(T\vdash\Box\lambda\)。したがって \(T\vdash\varphi\)。
   - note: diagonal lemma は proof resource であって、\(T\) が自己言及を公理として仮定するわけではない。D1 は object theory 内の一個の万能文ではなく、外部 theoremhood を入力とする schema である。

13. **closure_style:** 局所反射崩壊型／theoremhood 回収型

14. **theorem_vs_proof_comment:** 定理が固定するのは、算術理論、効果的公理提示、標準 provability predicate、D1–D3、および一つの local reflection instance の可証性である。証明は diagonal lemma で \(\lambda\) を構成し、D1–D3 によって provability を反復・伝播させる。fixed point を仮定へ昇格させると、どの条件が self-reference を可能にし、どの道具が実際に self-referential sentence を構成するかが見えなくなる。

15. **short_comment:** Löb の定理は「体系が自分を信じてはいけない」とは述べない。固定した文 \(\varphi\) について、標準 provability predicate に対する local reflection を \(T\) 自身が証明できるなら、その反射は新しい保証ではなく、すでに \(T\vdash\varphi\) であることへ回収される。

16. **closure_target:** 固定した文 \(\varphi\) に関する **internal local reflection**、すなわち \(T\) 内部での \(\Box\varphi\to\varphi\) を対象とする。閉じようとしているのは \(T\) の全真理でも体系全体の soundness でもなく、特定文について provability から内容へ戻る一つの橋である。

17. **self_reference_mechanism:**
   1. finite proof relation を自然数上へ算術化する。
   2. \(\mathrm{Pr}_T(x)\) を固定する。
   3. diagonal lemma で \(\lambda\leftrightarrow(\Box\lambda\to\varphi)\) となる fixed point を構成する。
   4. D1・D2で fixed-point equivalence の theoremhood を provability 内へ運ぶ。
   5. D3で \(\Box\lambda\) を \(\Box\Box\lambda\) へ反復する。
   6. local reflection \(\Box\varphi\to\varphi\) と組み合わせ、\(\lambda\)、次いで \(\varphi\) の theoremhood を得る。

   Gödel 第1では fixed point が自分の非可証性または Rosser 条件を表し、整合性条件のもとで independence を示す。Gödel 第2では \(\varphi=\bot\) に対する local reflection を consistency sentence として用いる。Löb は一般の \(\varphi\) について、reflection instance の内部可証性が theoremhood へ collapse することを示す。

18. **meta_level_transition:**
   - **metatheory:** \(T\)、公理提示、proof code、\(\mathrm{Pr}_T\)、D1–D3 の成立を固定
   - **metatheory:** diagonal lemma を適用し、\(\lambda\) の存在と \(T\vdash\lambda\leftrightarrow(\Box\lambda\to\varphi)\) を得る
   - **object theory:** D2・D3、propositional logic、仮定された local reflection を使って式を導出
   - **境界通過:** D1 は外部の \(T\vdash\theta\) を内部文 \(\Box\theta\) の theoremhood へ移す。これを二度用いる
   - **metatheory:** 最終結果を \(T\vdash\varphi\) と判定

   証明全体が \(T\) 内部へ消えるわけではない。fixed point の選択、D1 の適用、theoremhood の結論はメタレベルに残る。

19. **reflection_scope:**
   - **local reflection:** 固定した sentence \(\varphi\) に対する \(\Box_T\varphi\to\varphi\)。Löb が直接扱う
   - **uniform reflection:** formula \(\theta(x)\) と数値代入についての reflection schema。local reflection 一個より強く、exact formulation は predicate と formula class に依存
   - **global reflection:** 全 sentence にわたる schema、または truth / satisfaction machinery を伴う包括的表現。単一 local instance と同一でない
   - **consistency statement:** \(\mathrm{Con}(T)\equiv\neg\Box_T\bot\)。古典論理では \(\Box_T\bot\to\bot\) と同値なので、\(\varphi=\bot\) の local reflection instance
   - **soundness:** 外部意味論で「\(T\) の全定理が真」とする metatheoretic property。local reflection schema や \(\mathrm{Con}(T)\) と同一でない

20. **residual_location:** 「真理が体系外に残る」とは言わない。制約の位置は、同じ \(T\) における **未証明の local reflection instance**、より強い理論 \(U\) から見た \(T\)-reflection、formula-class restricted reflection、provability-predicate dependence の間にある。固定した \(\varphi\) については、\(T\vdash\Box_T\varphi\to\varphi\) iff \(T\vdash\varphi\) である。逆向きは propositional logic だけで従う。より強い \(U\) が \(\Box_T\varphi\to\varphi\) を証明することは、Löb の antecedent \(T\vdash\Box_T\varphi\to\varphi\) ではない。

# 3. Gödel 第1との比較

| 項目 | Gödel 第1 | Löb |
|---|---|---|
| main predicate | \(T\)-provability | \(T\)-provability |
| fixed point role | 非可証性／Rosser 条件を表す independent-sentence construction | local reflection と相互作用する \(\lambda\leftrightarrow(\Box\lambda\to\varphi)\) |
| conclusion | 適切な整合性条件のもとで independence | reflection instance の可証性から \(T\vdash\varphi\) |
| role of consistency | Rosser 版の両側非可証性に本質的 | Löb 本体には不要。矛盾理論では結論が自明 |
| meta-level remainder | \(T\nvdash G,T\nvdash\neg G\) という外部判定 | \(T\vdash\varphi\) という外部 theoremhood 判定 |
| target | effective theory の syntactic completeness | 同じ \(T\) 内の local reflection |

「Gödel は決められない文を構成し、Löb は『\(\varphi\) が証明可能なら \(\varphi\)』を内部証明すると \(\varphi\) 自身が定理になる」と要約してよい。ただし前者は採用版と整合性条件に依存し、後者は semantic correctness ではなく theoremhood collapse である。

# 4. Gödel 第2との重点比較

\(\bot\) を \(0=1\) とし、\(\mathrm{Con}(T):\!\equiv\neg\Box_T\bot\) と置く。古典論理では

\[
\neg\Box_T\bot\quad\leftrightarrow\quad(\Box_T\bot\to\bot)
\]

なので、\(\mathrm{Con}(T)\) は \(\varphi=\bot\) の local reflection instance に対応する。

1. \(T\vdash\mathrm{Con}(T)\) と仮定する。
2. すると \(T\vdash\Box_T\bot\to\bot\)。
3. Löb を \(\varphi=\bot\) に適用して \(T\vdash\bot\)。
4. 外部で \(T\) が整合的、すなわち \(T\nvdash\bot\) なら、\(T\nvdash\mathrm{Con}(T)\)。

従って標準的 Gödel 第2は、Löb に \(\bot\) を代入し、外部整合性を加えて得られる系である。ただし両者は同一ではない。

| 項目 | Gödel 第2 | Löb |
|---|---|---|
| 対象 | 標準内部整合性文 \(\mathrm{Con}(T)\) | 任意の文 \(\varphi\) の local reflection |
| 結論 | 整合的なら \(T\nvdash\mathrm{Con}(T)\) | reflection が可証なら \(T\vdash\varphi\) |
| 整合性 | 外部仮定として必要 | 本体には不要 |
| 論理的位置 | 非可証性定理 | theoremhood を強制する条件定理 |

Löb の方が一般であるが、第2定理は \(\mathrm{Con}(T)\) の形式、標準 predicate、外部整合性を明示した重要な系である。

# 5. Tarski との比較

| 項目 | Tarski | Löb |
|---|---|---|
| 内部化候補 | standard-model truth predicate | finite-proof provability predicate |
| 基本式 | \(\mathrm{Tr}(\ulcorner\varphi\urcorner)\leftrightarrow\varphi\) | \(\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\to\varphi\) |
| 可否 | total same-language truth definition は存在しない | standard provability predicate 自体は算術的に定義できる |
| 制約 | full T-schema と diagonal sentence が contradiction | local reflection が可証なら \(\varphi\) がすでに定理 |
| 結論型 | undefinability | theoremhood implication |
| 外部残余 | metalanguage の satisfaction / truth definition | metatheoretic theoremhood、より強い理論からの reflection |

「truth predicate は full same-language definition 自体が成立しないが、provability predicate は内部定義でき、その predicate への reflection を同じ \(T\) で自由に加えられない」という非対称性は妥当である。ただし Tarski は semantic biconditional、Löb は syntactic reflection implication を扱う。両者を単なる自己適用禁止と一括してはならない。

# 6. 「自己保証」仮説

## 6.1 仮説が捉えるもの

provability predicate の内部化と、その predicate に対する reflection の内部可証性は別である。\(T\) は有限証明関係を算術化できるが、固定した非定理 \(\varphi\) に対して \(\Box_T\varphi\to\varphi\) を自分で証明できない。もし証明できれば Löb により \(\varphi\) も証明されるからである。

この意味で「自己保証」は、proof relation の内部化だけでは soundness bridge が得られないことを短く示す。ただし必ず local reflection と併記する。

## 6.2 混同してはならない四層

| 層 | 標準的内容 | Löbとの関係 |
|---|---|---|
| proof relation の内部化 | \(\mathrm{Prf}_T(p,x),\mathrm{Pr}_T(x)\) の算術的定義 | 前提構造。可能 |
| reflection の内部化 | \(\Box_T\varphi\to\varphi\) | Löb の直接対象 |
| consistency の内部化 | \(\neg\Box_T\bot\) | \(\varphi=\bot\) の特殊例 |
| truth の内部化 | full truth predicate / T-schema | Tarski の対象。provability と同一でない |

## 6.3 判定

**S2 — 既存の reflection 概念をうまく横断比較できる。**

「自己保証」は四層を分解して用いる限り、Gödel 第2・Tarski・研究ログとの比較軸になる。ただし新しい proof-theoretic 概念ではなく、標準的 local reflection の説明ラベルにすぎないので S3 には進めない。

# 7. 「証明の閉鎖条件の自己保証」との比較

通常の数学的証明が前提・推論規則・背景構造のもとで結論を導くことと、その形式体系が自分の derivability に reflection を付与することは別問題である。

- **proof relation の内部化:** finite proof checking の算術化。標準算術では可能。
- **soundness / reflection の内部化:** provability から formula へ戻る原理。Löb の直接対象は固定文の local reflection。
- **consistency の内部化:** contradiction が provable でないという特定文。local reflection at \(\bot\)。
- **truth の内部化:** standard-model truth の total same-language definition。Tarski の別種の制約。

従って「証明が自分の閉鎖条件を保証する」は、どの reflection scope と provability predicate かを指定した場合だけ数理的内容を持つ。一般の証明実践や認識道具へ直ちに適用できない。

# 8. 研究ログとの比較

| research-log side | Löb side | 判定 |
|---|---|---|
| 「全認識道具」の真理保証を一般化 | 固定 \(T\)、固定 \(\mathrm{Pr}_T\)、固定 \(\varphi\) | Löb の方がはるかに局所的・形式的 |
| 証明自身も対象へ含める | proof relation を自然数上へ算術化 | 対象化の限定的類似 |
| universal self-guarantee で自己適用問題 | local reflection と diagonal fixed point | 構造類似はあるが形式写像はない |
| 普遍主張を縮退 | \(T\vdash\Box\varphi\to\varphi\) iff \(T\vdash\varphi\) | 保証追加が自由でないという限定的対応 |

## 類似判定

**L1 — structural analogy**

内部化された評価装置が自身に関する保証条件と結びつくと強い制約が生じる、という限定的類似はある。しかし研究ログ側には natural-number coding、provability predicate、D1–D3、diagonal fixed point に対応する形式構造がない。L2 の formally transferable には達せず、L3 の same mechanism は棄却する。

# 9. 「閉包反転」との比較

Löb では、local reflection を内部で証明可能にして保証を追加しようとすると、保証対象 \(\varphi\) がすでに theoremhood へ回収される。この点は Gödel 第1より反転的イメージに近い。

しかし標準的には、これは Löb condition、derivability conditions、diagonal lemma、local reflection で精密化される。「閉包反転」は predicate、theory、reflection scope を単独では示さない。

## 判定

**C1 — 説明比喩としてのみ有効。**

Gödel stress test より図式への適合は鮮明だが、追加の予測・保存定理・同値条件を与えないため C2 へ上げない。C3 は棄却する。

# 10. kill criteria

| kill criterion | 検査結果 |
|---|---|
| 1. derivability conditions＋diagonal lemma＋reflection で十分説明できる | **成立。** 独自語彙は技術説明を置換できない |
| 2. 「自己保証」が soundness / reflection / consistency を曖昧にする | **条件付き成立。** local reflection と限定すれば比較ラベルとして残せる |
| 3. 「閉包」が local / uniform / global reflection を混同する | **成立する危険が高い。** scope の明記が必須 |
| 4. 「残差」が stronger theory / unprovable reflection / predicate dependence を混同する | **成立する危険が高い。** R1 は索引以上に使わない |
| 5. 研究ログとの類似が self-assessment 以上に進まない | **成立。** 形式写像がなく L1 に留まる |

negative result は明確である。「自己保証」は S2 の比較ラベルとして残せるが、「閉包反転」は C1、「残差」は R1 の粗い挙動記録に留まる。

# 11. 最終判定

## A. Löb の定理の解剖

- \(T\supseteq I\Sigma_1\)、計算可能な公理提示、標準 \(\mathrm{Pr}_T\)、D1–D3 を固定する。
- \(T\vdash\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\to\varphi\) なら \(T\vdash\varphi\)。
- diagonal lemma が \(\lambda\leftrightarrow(\Box\lambda\to\varphi)\) を作り、D2・D3 が provability を内部伝播する。
- 結論は theoremhood であり truth や soundness ではない。
- 整合性は Löb 本体でなく Gödel 第2を導く際に用いる。

## B. Gödel 第1との最大の違い

1. Gödel 第1は整合性条件のもとで independent sentence を得る。
2. Löb は local reflection の可証性から対象文の theoremhood を得る。
3. Löb 本体は整合性を仮定しない。

## C. Gödel 第2との最大の違い

1. 第2は \(\varphi=\bot\) の consistency instance、Löb は任意の \(\varphi\) を扱う。
2. 第2は外部整合性から \(\mathrm{Con}(T)\) の非可証性を結論する。
3. Löb は reflection antecedent から theoremhood を結論する一般定理。

## D. Tarskiとの最大の違い

1. Tarski は full same-language truth definition の不存在、Löb は definable provability predicate への local reflection 制約。
2. Tarski の結論型は undefinability、Löb は theoremhood implication。
3. T-schema は semantic biconditional、Löb antecedent は syntactic reflection implication。

## E. residual 判定

**R1 — altered freedom。** predicate、reflection scope、stronger theory、弱い算術への移行が現れる。明示的補正項ではないため R2 ではない。

## F. 「自己保証」判定

**S2 — 既存の reflection 概念をうまく横断比較できる。** local reflection と明記する場合に限り、新しい proof-theoretic 概念ではない。

## G. 「閉包反転」判定

**C1 — 説明比喩のみ。** 反転的図式は Gödel より鮮明だが、標準的 Löb condition と reflection 以上の分類能力はない。

## H. 研究ログとの類似

**L1 — structural analogy。** 内部化された評価装置と自己保証条件の相互作用という類似はあるが、形式写像がない。

## I. 次の検査候補

1. **modal provability logic GL:** Löb axiom \(\Box(\Box p\to p)\to\Box p\) により、「反転」が標準 modal structure だけで尽くされるかを検査できる。
2. **reflection principles:** local / uniform / global reflection と formula-class restrictions を分け、S2 判定の解像度を検査できる。
3. **Gödel completeness theorem:** semantic consequence と formal provability の対応を調べ、Tarski や Löb と別種の「閉鎖」であることを確認できる。

# 12. 検証資料

- [M. H. Löb, “Solution of a Problem of Leon Henkin” (1955), Journal of Symbolic Logic](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/m-h-lob-solution-of-a-problem-of-leon-henkin-the-journal-of-symbolic-logic-vol-20-1955-pp-115118/E508099485154BD8561596302CBC80A8)
- [Taishi Kurahashi, “A note on derivability conditions”](https://arxiv.org/pdf/1902.00895)
- [Taishi Kurahashi, “Rosser provability and the second incompleteness theorem”](https://arxiv.org/pdf/1902.06863)
- [Solomon Feferman, historical discussion of Henkin–Löb](https://math.stanford.edu/~feferman/papers/My_Henkin_Year.pdf)

# Gödel 不完全性定理：証明の解剖 special stress test

## 0. 目的と参照枠

本稿は theorem_proof_anatomy_v1.1_ja.md の分析枠を、Gödel の第1・第2不完全性定理へ試験適用する。ここでいう「逃走経路」「閉じ方」「封鎖」「残差」「閉包」「閉包反転」は比較のためのメタ記述であって、標準数理論理学・証明論の用語ではない。

検査上、次を維持する。

- theorem assumptions と proof resources を分ける。
- object / ambient / background / definitional を分ける。
- 条件除去後を R0 / R1 / R2 で記録する。
- syntactic incompleteness、standard model での truth、semantic completeness を混同しない。
- 自己参照を liar paradox や「真理は証明できない」という一般命題へ単純化しない。

## 1. 採用版の固定

### 1.1 第1不完全性定理

本稿では **Gödel–Rosser 版**を採用する。

> \(T\) を、Robinson arithmetic \(Q\) を含む、計算可能に公理化された古典一階理論とする。\(T\) が整合的なら、ある算術文 \(R_T\) が存在し、\(T\nvdash R_T\) かつ \(T\nvdash\neg R_T\) である。

したがって必要なのは通常の整合性であり、Gödel 原版の \(\omega\)-consistency ではない。Rosser の工夫を使わない通常の Gödel 文 \(G_T\leftrightarrow\neg\mathrm{Prov}_T(\ulcorner G_T\urcorner)\) について「\(G_T\) も \(\neg G_T\) も証明できない」と結論する場合には、原版では \(\omega\)-consistency、現代的な別版では 1-consistency や適切な soundness 条件が関与する。この違いを本稿の採用版へ混入させない。

結論の主部は **syntactic incompleteness** である。構成された Rosser 文は、外部メタ理論で \(T\) の整合性と標準的符号化を認めれば標準モデル \(\mathbb N\) で真と確認できるが、「任意の独立文が真」「\(T\) の全ての非定理が真」という意味ではない。

### 1.2 第2不完全性定理

本稿では **標準的 provability predicate と Hilbert–Bernays–Löb 導出可能性条件を用いる Löb 型**を採用する。

固定した計算可能な公理提示を持つ理論 \(T\supseteq I\Sigma_1\) に対し、

\[
\mathrm{Pr}_T(x):\equiv\exists p\,\mathrm{Prf}_T(p,x)
\]

を、その提示に関する標準的な \(\Sigma_1\) 証明可能性述語とする。また

\[
\mathrm{Con}(T):\equiv\neg\mathrm{Pr}_T(\ulcorner 0=1\urcorner)
\]

と定める。標準的算術化によって \(\mathrm{Pr}_T\) が Hilbert–Bernays–Löb 条件 D1–D3 を満たし、\(T\) が整合的なら、

\[
T\nvdash\mathrm{Con}(T)
\]

である。

D1–D3 は次である。

- D1: \(T\vdash\varphi\) なら \(T\vdash\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\)
- D2: \(T\vdash\mathrm{Pr}_T(\ulcorner\varphi\to\psi\urcorner)\to(\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\to\mathrm{Pr}_T(\ulcorner\psi\urcorner))\)
- D3: \(T\vdash\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\to\mathrm{Pr}_T(\ulcorner\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\urcorner)\)

D1 は外部の導出可能性から内部文への schema、D2・D3 は \(T\) 内の文である。第2定理は任意の「証明可能性らしい述語」や任意の「整合性らしい文」について成立するわけではない。provability predicate と consistency sentence の選択に敏感である。

### 1.3 メタ理論上の整合性と内部文の区別

- **メタ理論上の整合性:** 外部から見て \(T\nvdash 0=1\) であるという \(T\) の性質。
- **内部の整合性文:** \(T\) の言語内の特定の文 \(\neg\mathrm{Pr}_T(\ulcorner0=1\urcorner)\)。

両者は標準的符号化のもとで意図した対応を持つが、同一のレベルにあるものではない。第2定理の結論は、外部の整合性仮定から内部文の **非証明可能性** を導くメタ定理である。

# 2. 第1不完全性定理の解剖

1. **theorem_name:** Gödel–Rosser 第1不完全性定理

2. **domain:** 数理論理・証明論・再帰理論

3. **standard_statement:** \(T\) を、Robinson arithmetic \(Q\) を含む、計算可能に公理化された古典一階理論とする。\(T\) が整合的なら、ある算術文 \(R_T\) が存在して \(T\nvdash R_T\) かつ \(T\nvdash\neg R_T\) となる。従って \(T\) は syntactically incomplete である。

4. **assumptions_ABC:**
   - A: \(T\) が標準的な有限的証明概念を持つ古典一階算術理論である
   - B: \(T\supseteq Q\)、すなわち構文・計算の必要部分を算術的に表現できるだけの強さを持つ
   - C: \(T\) が計算可能に公理化されている。公理集合は c.e. で、有限証明を効果的に符号化できる
   - D: \(T\) が整合的である
   - E: 通常のメタ理論で自然数、有限列、再帰関数、\(T\) の証明について推論する

5. **hypothesis_levels:**
   - A: ambient（論理体系・証明カテゴリーの指定）
   - B: object（\(T\) に課される表現力条件）
   - C: object（\(T\) の公理提示に課される効果性条件）
   - D: object（object theory \(T\) に関するメタレベルの性質）
   - E: background。\(T\) の内部仮定ではなく、定理を述べ証明するメタ理論側の基盤

6. **condition_types:**
   - A: 形式性・一階性・有限構文
   - B: 算術的表現力
   - C: 効果的公理化・可算列挙可能性
   - D: 整合性
   - E: メタ数学的背景

7. **closure_roles:**
   - A: syntactic closure / finitary derivation
   - B: arithmetic self-representation capacity
   - C: effective enumerability / proof coding
   - D: consistency constraint / trivial-completeness suppression
   - E: meta-level verification

   self-reference enablement は単独の仮定ではない。B・Cによって構文と証明関係を算術へ写す条件が整い、proof resource である diagonal lemma を適用した結果として自己適用文が得られる。

8. **conclusion_P:** \(T\) の言語内に、\(T\) では証明も反証もできない算術文 \(R_T\) が存在する。これは syntactic independence の主張である。外部メタ理論では、採用した Rosser 文は \(T\) の整合性から標準モデル \(\mathbb N\) で真と確認できるが、その semantic truth は \(T\) 内部での可証性と同一ではない。

9. **blocked_escape_routes:**
   - A: 「証明」を無制約・非有限的な認可関係にしてしまう逃げ道を塞ぎ、対象を形式的導出へ限定する
   - B: \(T\) が自らの構文・証明関係を算術式として表現できないほど弱い、という逃げ道を塞ぐ
   - C: 必要な文をその都度非効果的に公理へ加え、標準算術の全真理を最初から列挙外の集合として採用する逃げ道を塞ぐ
   - D: \(R_T\) と \(\neg R_T\) を両方証明し、explosion によって全てを決定する空虚な完全性を塞ぐ
   - E: 外部から proof code と実際の有限証明の対応を検証不能にすることを防ぐ。ただしこれは \(T\) 内の逃走経路ではない

10. **what_fails_if_removed:**
   - Aを外すと: Bの \(Q\) 包含も同時に再定式化が必要となり、独立な一条件除去にならない。不完全性は他の論理体系にも存在するため、「一階性を外せば完全になる」とは言えない
   - Bを外すと: Presburger arithmetic のような弱い算術には、整合的・計算可能公理化・完全・decidable な理論が存在する。従って十分な表現力は本質的である
   - Cを外すと: 標準自然数について真である全一階算術文の理論 \(\mathrm{Th}(\mathbb N)\) は整合的かつ完全だが、計算可能に公理化できない
   - Dを外すと: 古典論理の矛盾理論は explosion により全ての文とその否定を証明し、syntactic completeness が空虚に成立する
   - Eを外すと: 定理の対象が反例化するのではなく、符号化と非可証性を示すメタ数学的枠組みが失われる

11. **what_reappears_if_removed:**
   - A: **R0** — Aだけの独立除去は Bと連動し、同じ定理文を保てない。自然な単一残差はない
   - B: **R1** — decidability と syntactic completeness が回復し得る代わりに、証明関係の内部表現能力が失われる
   - C: **R1** — semantic completion が可能になる代わりに、非効果性・非列挙可能性が戻る
   - D: **R1** — triviality と explosion が戻る。完全性は回復しても識別能力を失う
   - E: **R0** — 比較を行うメタ理論が失われるだけで、式に戻る補正項はない

   いずれも R2 ではない。条件除去後に境界項が同じ等式へ戻るのではなく、完全性、決定可能性、意味論、効果性の交換関係が別構造として現れる。

12. **proof_resources:**
   - representative_route: Rosser trick を用いる標準的算術化証明
   - resources:
     - Gödel numbering による式・有限列・証明の自然数符号化
     - primitive recursive coding と構文関係の表現可能性
     - \(T\) の proof relation \(\mathrm{Prf}_T(p,x)\) の算術化
     - diagonal / fixed-point lemma
     - Rosser 文

       \[
       R_T\leftrightarrow
       \forall p\bigl(\mathrm{Prf}_T(p,\ulcorner R_T\urcorner)
       \to\exists q\le p\,\mathrm{Prf}_T(q,\ulcorner\neg R_T\urcorner)\bigr)
       \]

     - 最小証明番号を比較する Rosser trick
     - 外部メタ理論からの整合性 argument
   - note: Gödel numbering と diagonal lemma は proof resources であり、\(T\) が「自己言及を公理として持つ」という意味ではない。Gödel 原版の文を用いる証明では仮定構成が異なる。

13. **closure_style:** 効果的完全化限界型／閉包反転候補

14. **theorem_vs_proof_comment:** 定理が固定するのは、効果的に提示され、十分な算術表現力を持ち、矛盾していない理論 \(T\) である。証明は外部で構文を数へ符号化し、diagonal lemma と Rosser trick により、その固定された証明関係に相対的な文を構成する。「自己言及」を仮定へ昇格させると、効果的構文の算術化と対角化という二段階が見えなくなる。

15. **short_comment:** 条件は \(T\) を「閉じれば全算術文を決定できる」方向へ運ぶのではなく、\(T\) 自身の proof relation を算術対象として取り扱える地点まで運ぶ。そこで得られるのは truth 一般の外部残差ではなく、各 \(T\) に相対的で extension-dependent な独立文である。

16. **closure_target:** 一つの整合的・計算可能公理化された算術理論 \(T\) によって、\(T\) の全ての文について \(T\vdash\varphi\) または \(T\vdash\neg\varphi\) を成立させる **syntactic completeness**。対象は算術文に対する theory-internal derivability であり、「世界」「意味」「真理一般」ではない。

17. **self_reference_mechanism:**
   1. メタ理論で syntax と finite proof を自然数へ符号化する。
   2. \(Q\) 以上の算術内で proof relation を表す式 \(\mathrm{Prf}_T(p,x)\) を得る。
   3. diagonal lemma により、自分自身の Gödel 番号を適切な一変数式へ代入した固定点 \(R_T\) を構成する。
   4. Rosser 文は、自分の証明があればそれ以下の番号の反証がある、という proof-ordering に関する文になる。

   liar sentence「この文は偽である」は semantic truth predicate と否定を直接循環させる。Rosser 文は、形式化された有限証明関係についての算術文であり、矛盾を直接生成せず、整合性のもとで非証明可能性を生成する。

18. **meta_level_transition:**
   - metatheory: \(T\) の式・証明・公理提示を自然数へ符号化する
   - object theory: 符号化された proof relation と diagonal fixed point を算術式として扱う
   - metatheory: 仮に \(T\vdash R_T\) または \(T\vdash\neg R_T\) としたときの有限 proof code を取り、\(T\) の整合性と照合して不可能性を示す

   証明全体が \(T\) 内部へ落ちるわけではない。\(T\) の整合性を仮定し、実際の proof code の有無を評価する外部メタ理論が最後まで残る。

19. **residual_location:** 文 \(R_T\) 自体は **theory internal** であるが、「\(R_T\) が \(T\) で undecidable」という判定は **metatheoretically identifiable** である。採用版の構成文は外部から standard model で真と確認できるが、その位置づけは特定の \(T\) と符号化に相対的である。\(T+R_T\) へ拡張すれば \(R_T\) は決定されるが、その新しい理論が整合的・効果的なら別の独立文が現れる。従って残差は固定された一文というより **extension-dependent moving boundary** にある。

# 3. 第2不完全性定理の解剖

1. **theorem_name:** Gödel 第2不完全性定理（標準 provability predicate／Löb 型）

2. **domain:** 数理論理・証明論・provability logic

3. **standard_statement:** \(T\) を、固定された計算可能な公理提示を持つ古典一階理論で \(I\Sigma_1\) を含むものとする。その提示から得られる標準的 \(\Sigma_1\) 証明可能性述語 \(\mathrm{Pr}_T\) が Hilbert–Bernays–Löb 条件 D1–D3 を満たすとする。\(T\) が整合的なら、\(T\nvdash\mathrm{Con}(T)\)、ただし \(\mathrm{Con}(T):=\neg\mathrm{Pr}_T(\ulcorner0=1\urcorner)\) である。

4. **assumptions_ABC:**
   - A: \(T\) が古典一階算術理論で \(I\Sigma_1\) を含む
   - B: \(T\) が固定された計算可能な公理提示を持つ
   - C: その提示に対する標準的 \(\Sigma_1\) provability predicate \(\mathrm{Pr}_T\) を採用し、D1–D3 が成立する
   - D: \(T\) が整合的である
   - E: \(\mathrm{Con}(T)\) を \(\neg\mathrm{Pr}_T(\ulcorner0=1\urcorner)\) と定義する
   - F: 通常のメタ理論で \(T\) の有限証明と標準自然数について推論する

5. **hypothesis_levels:**
   - A: ambient＋object（論理舞台と表現力）
   - B: object（公理提示の効果性）
   - C: object＋definitional（どの provability predicate を用いるかと、その内部挙動）
   - D: object（\(T\) に関するメタレベル性質）
   - E: definitional
   - F: background

6. **condition_types:**
   - A: 算術的表現力
   - B: 効果的公理化
   - C: 導出可能性・証明可能性表現
   - D: 整合性
   - E: 内部整合性文の固定
   - F: メタ数学的背景

7. **closure_roles:**
   - A: expressive strength / internal arithmetic reasoning
   - B: proof coding / effective enumerability
   - C: derivability closure / provability iteration
   - D: consistency constraint
   - E: target fixation / nonambiguity
   - F: meta-level verification

8. **conclusion_P:** \(T\) は、指定された provability predicate に相対的な標準的整合性文 \(\mathrm{Con}(T)\) を証明できない。これは \(\mathrm{Con}(T)\) が偽であるという結論ではない。外部で \(T\) が整合的なら、標準モデルでは \(\mathrm{Con}(T)\) は真である。また、より強い理論 \(U\) が \(\mathrm{Con}(T)\) を証明する可能性は排除されない。

9. **blocked_escape_routes:**
   - A: \(T\) が provability の反復や diagonal argument を内部で扱えないほど弱い、という逃げ道を塞ぐ
   - B: 「\(T\) の証明」を非効果的・算術化不能な関係にする逃げ道を塞ぐ
   - C: provability の modus ponens 保存や positive introspection を持たない人工的述語へ差し替える逃げ道を塞ぐ
   - D: 矛盾によって \(\mathrm{Con}(T)\) まで証明する空虚な自己保証を塞ぐ
   - E: 「整合性」を別の内部文へ読み替えて定理の対象を移動させることを防ぐ
   - F: 内部文と外部の実際の整合性を無区別に扱うことを防ぐ

10. **what_fails_if_removed:**
   - Aを外すと: 弱い理論では標準証明可能性述語の必要性質を内部検証できず、第2定理のこの版は適用不能になる。弱い体系には適切に定式化された自己整合性を証明する例もあり、単に「全ての形式体系が自己整合性を証明できない」とは言えない
   - Bを外すと: \(\mathrm{Th}(\mathbb N)\) のような非効果的理論では標準的な有限 proof predicate を同じ方法で算術化できず、この定理文の \(\mathrm{Con}(T)\) が固定できない
   - Cを外すと: 非標準的・Rosser 型・人工的 provability predicate では、対応する consistency sentence が理論内で証明可能になる場合がある。従って「provability predicate なら何でもよい」は偽
   - Dを外すと: 矛盾理論は explosion により \(\mathrm{Con}(T)\) も証明するため、結論 \(T\nvdash\mathrm{Con}(T)\) が偽になる
   - Eを外すと: 「\(T\) は自身の整合性を証明できない」の対象文が曖昧になり、異なる consistency statements に異なる第2定理が対応する
   - Fを外すと: 対象 \(T\) の反例ではなく、非証明可能性を述べる外部枠組みが失われる

11. **what_reappears_if_removed:**
   - A: **R1** — 弱さによって decidability や限定的 reflection が可能になる一方、proof relation の内部表現力が失われる
   - B: **R1** — semantic completion と非効果性が戻る
   - C: **R1** — provability predicate と consistency sentence の選択自由度が戻る。これは第2定理固有の重要な sensitivity である
   - D: **R1** — triviality と explosion が戻る
   - E: **R1** — 複数の非同値な内部 consistency formulations が未決定成分として現れる
   - F: **R0** — メタ数学的判定枠が失われるだけで、明示的補正項はない

   ここでも R2 は確認されない。第2定理の制約は式へ戻る境界項ではなく、provability predicate、reflection、理論拡張の選択自由度として R1 的に現れる。

12. **proof_resources:**
   - representative_route: Löb の定理を経由する証明
   - resources:
     - Gödel numbering と標準 proof predicate
     - diagonal lemma
     - 仮定として固定した Hilbert–Bernays–Löb 条件 D1–D3
     - Löb の定理

       \[
       T\vdash\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\to\varphi
       \quad\Longrightarrow\quad T\vdash\varphi
       \]

     - \(\varphi\equiv(0=1)\) への適用
     - 外部の整合性仮定
   - note: もし \(T\vdash\mathrm{Con}(T)\)、すなわち \(T\vdash\mathrm{Pr}_T(\ulcorner0=1\urcorner)\to0=1\) なら、Löb により \(T\vdash0=1\) となる。ここで diagonal lemma は Löb の定理を証明する資源であり、\(\mathrm{Con}(T)\) 自体が liar sentence なのではない。第1定理の証明を \(T\) 内で形式化する別ルートもある。

13. **closure_style:** 内部自己保証限界型／閉包反転候補

14. **theorem_vs_proof_comment:** 定理が固定するのは、十分な算術、効果的公理提示、標準 provability predicate、その導出可能性条件、整合性文の形式である。証明は diagonal lemma を含む Löb の定理を使って、内部 reflection が成立すれば矛盾が証明されることを示す。provability predicate の条件を単なる proof resource として隠すと、「どの \(\mathrm{Con}(T)\) についての定理か」という第2定理の感度が見えなくなる。

15. **short_comment:** 第2定理は「体系は自分について何も証明できない」とは述べない。特定の標準的 provability predicate に基づく、自分の無矛盾性の一括 reflection を、整合的な \(T\) 自身では閉じられないと述べる。

16. **closure_target:** \(T\) 内部で、固定した proof predicate に関する「矛盾の proof code は存在しない」という一文 \(\mathrm{Con}(T)\) を導出し、\(T\) の信頼性を \(T\) 自身の derivability だけで保証すること。対象は internal consistency statement であり、体系の意味論的健全性、全ての公理の真理性、推論一般の正当化ではない。

17. **self_reference_mechanism:** 第2定理の標準的 \(\mathrm{Con}(T)\) は、文字通り「この文は証明できない」と自己の Gödel 番号を指す文ではない。自己適用は、(i) \(T\) の proof relation を \(T\) 内に表し、(ii) D3 により「証明可能なら、その証明可能性も証明可能」を扱い、(iii) diagonal lemma で Löb fixed point を構成するところに現れる。従って自己参照機構は **provability の反復と fixed point** にあり、liar paradox の truth-negation 循環とは異なる。

18. **meta_level_transition:**
   - metatheory: 固定した公理提示から \(\mathrm{Prf}_T\)、\(\mathrm{Pr}_T\)、\(\mathrm{Con}(T)\) を定める
   - object theory: D2・D3と fixed point を用いて Löb の内部導出を行う
   - metatheory: \(T\vdash\mathrm{Con}(T)\) なら \(T\vdash0=1\) となることと、外部仮定「\(T\) は整合的」を照合して \(T\nvdash\mathrm{Con}(T)\) と結論する

   最終結論は \(T\) 内の定理ではなく、\(T\) に関する外部メタ定理である。

19. **residual_location:** \(\mathrm{Con}(T)\) は **theory internal**、その非証明可能性は **metatheoretic**、外部整合性のもとでの真理性は **standard-model semantic** である。より強い \(U\) は \(\mathrm{Con}(T)\) を証明し得るが、\(U\) が同じ条件を満たして整合的なら \(\mathrm{Con}(U)\) は \(U\) 内に残る。この意味で位置は一体系の外部へ固定された残差ではなく、理論強化に伴って移動する **reflection boundary** である。

# 4. 第1・第2不完全性定理の差

| 項目 | 第1不完全性 | 第2不完全性 |
|---|---|---|
| closure target | 全算術文の syntactic decision | 標準 provability predicate による自己整合性文の内部証明 |
| main fixed conditions | \(Q\) 以上、c.e. 公理化、整合性 | \(I\Sigma_1\) 以上、c.e. 提示、標準 \(\mathrm{Pr}_T\)、D1–D3、整合性 |
| self-reference mechanism | proof coding＋diagonal lemma＋Rosser proof comparison | provability iteration＋diagonal lemma＋Löb fixed point |
| conclusion | ある \(R_T\) が証明も反証も不能 | 特定の \(\mathrm{Con}(T)\) が証明不能 |
| residual location | \(T\) 内の extension-dependent independent sentence | \(T\) 内の consistency sentence に対する moving reflection boundary |
| role of consistency | 両側の非証明可能性を得て trivial completeness を除く | \(T\vdash\mathrm{Con}(T)\Rightarrow T\vdash\bot\) と外部整合性を衝突させる |
| meta-level dependence | proof code と実際の可証性を外部で照合 | 内部 Löb 導出と外部整合性を照合 |
| closure_style candidate | 効果的完全化限界型 | 内部自己保証限界型 |

第1は「各文を決定する能力」の限界、第2は「自分の標準的整合性文を証明する能力」の限界である。第2は第1を単に言い換えたものではなく、第1定理の証明可能性 reasoning を内部形式化する追加段階を持つ。

# 5. 既存21定理との比較

## 5.1 一階述語論理のコンパクト性定理

コンパクト性定理は、任意の一階理論 \(S\) について

\[
\text{全ての有限部分理論が充足可能}
\quad\Longrightarrow\quad
S\text{ がモデルを持つ}
\]

という **semantic model existence** を閉じる。Gödel–Rosser は、特定の c.e. 算術理論 \(T\) について、全ての文を \(T\) が証明または反証する **syntactic completeness** が不可能だと示す。

両者は逆向きではない。Gödel completeness theorem により、一階論理の semantic validity と derivability は対応する一方、個別理論 \(T\) が全ての文を決定するとは限らない。さらに compactness は非標準モデルの存在を許すため、算術理論の syntactic incompleteness と矛盾しない。「有限から大域を閉じる」と「効果的理論に独立文がある」は、異なる closure target を持つ直交的現象である。

## 5.2 Banach 不動点定理

Banach では完備性・自己写像性・一様収縮が、反復軌道を唯一の点へ収束させる。条件を強めるほど、同じ固定点候補に対する距離自由度が単調に減る。

Gödel では事情が異なる。\(T\) に \(R_T\) または \(\mathrm{Con}(T)\) を適切に追加すれば、その特定文は決定できる。しかし新しい理論 \(T'\) が整合的・効果的・十分強ければ、\(T'\) に相対的な別の独立文または \(\mathrm{Con}(T')\) が現れる。従って「条件強化で一つの残差点へ収束する」のではなく、**対象理論の更新に伴い限界文が再添字化される**。

この差を説明する限りで「通常閉包／閉包反転」という対比は有用だが、Banach と Gödel が同じ形式構造の正逆になっているわけではない。

## 5.3 Stokes・Gauss–Bonnet

Stokes の無限遠境界項や Gauss–Bonnet の境界測地曲率項は R2 であり、一般化された同じ積分公式の右辺へ明示項として戻る。項の値を計算し、等式の会計へ組み込める。

Gödel の独立文や \(\mathrm{Con}(T)\) は、この意味の residual term ではない。

- 元の等式に加える数値的・代数的補正項ではない。
- 一つの固定文を公理として加えても、新理論に相対的な限界が再生成する。
- 「残差」の位置は証明可能性関係と理論提示に依存する。

従って Gödel を R2 と読むことは棄却する。比喩的に residual と呼ぶ場合でも、分類上は **R1 に近い extension-dependent freedom** と明記すべきである。

# 6. 研究ログとの構造比較

## 6.1 対応する範囲

| research-log side | Gödel side | 判定 |
|---|---|---|
| 「あらゆる認識道具」を対象化しようとした | 十分強い効果的算術理論 \(T\) を対象化する | 対象化という操作だけが類似。Gödel の対象クラスは厳密に限定される |
| 証明自身も認識道具に含まれる可能性 | proof relation を算術化して \(T\) 内へ戻す | 装置が自身の操作記述を対象に含めるという限定的類似 |
| 条件厳密化で普遍主張が縮退 | 仮定を Q以上・c.e.・整合的理論へ限定 | スコープ制御の類似。縮退を起こす数学機構は同じとは限らない |
| 局所的・条件付き比較へ降りた | 各 \(T\) に相対的な \(R_T\)、各提示に相対的な \(\mathrm{Con}(T)\) | 結論の indexicality / relativity に限定的類似 |

## 6.2 非対応部分

研究ログ側には現時点で、少なくとも次が与えられていない。

- 対象となる「認識道具」の有効な構文と列挙可能な公理集合
- proof relation に相当する primitive recursive relation
- その関係を内部表現する十分な算術
- diagonal lemma が適用できる明示的 coding map
- Rosser 文または Löb fixed point に対応する構成

また、研究ログで普遍主張が縮退した理由は、対象範囲、語の定義、反例可能性、証明自身の包含などの方法論的圧力である。Gödel 側の縮退は、効果的算術体系についての明示的符号化と対角化による定理である。

## 6.3 類似判定

**G1 — structural analogy**

対象化した証明・推論装置が、自身の操作記述を対象領域へ戻したときに追加制約を生成する、という限定された類似はある。しかし研究ログ側に Gödel numbering、representability、diagonal fixed point に対応する形式化がないため、G2 の formally transferable には達しない。G3 の same mechanism は明確に棄却する。

# 7. 「閉包反転」仮説の査定

## 7.1 仮説が捉えているもの

通常21定理では、多くの場合、条件が無限遠、跳躍、非一意性、境界、相関などの非P自由度を減らし、存在・収束・等式・最適性を結論する。Gödel では、効果性・表現力・整合性の組が、体系の proof relation を算術的対象にできる範囲を定め、その結果として syntactic completeness または internal consistency proof の不可能性が結論される。

この差を「条件が閉包を完成させるのでなく、閉包不能性を可視化する」と要約することはできる。特に、整合的・効果的拡張が特定の独立文を決定しても、新しい限界文が理論に相対的に再生成する点は、既存21定理の静的な escape prevention とは異なる。

## 7.2 仮説が捉えていないもの

しかし、次の制限がある。

1. Gödel の数理的機構は、標準語彙では **arithmetization of syntax、representability、diagonalization、Rosser trick、derivability conditions、reflection** によってすでに精密に分解される。
2. 「効果的公理化・表現力・整合性を強く閉じたから不完全性が生じる」という因果表現は正確でない。これらは単一順序上の「強化」ではなく、異なる役割の条件である。
3. 任意の公理追加が不完全性を増やすわけではない。特定の独立文は決定できるが、条件を保つ拡張全体に essential incompleteness が再適用される。
4. 独立文は Stokes や Gauss–Bonnet の R2 型補正項ではない。
5. 不完全性定理も形式上は通常通り \(A,B,C\Rightarrow P\)、ただし \(P\) が「完全性の不成立」であるという定理であり、特別な論理形式を持つわけではない。

## 7.3 kill criteria

| kill criterion | 検査結果 |
|---|---|
| 1. self-reference / diagonalization だけで説明でき、closure が追加診断を与えない | **部分成立。** 証明機構の説明は標準語彙の方が明確。moving boundary の比較要約だけが追加価値 |
| 2. 通常の \(A,B,C\Rightarrow P\) に収まり特別分類不要 | **成立。** 数理形式上は通常の条件付き不可能性定理として収まる |
| 3. closure_target が形式的対象に対応しない | **不成立。** syntactic completeness と internal \(\mathrm{Con}(T)\) に限定すれば明確 |
| 4. residual_location が比喩で、標準的 independence より粗い | **成立。** residual は independent / unprovable / standard-true / extension-dependent の区別を単独では保持できない |
| 5. proof theory / model theory の既存語彙の方が明確 | **成立。** 技術的記述では既存語彙を優先すべき |

## 7.4 判定

**C1 — 説明比喩としてのみ有効**

「閉包反転」は、既存21定理との比較において、条件が positive closure を作る場合と、条件が effective closure の限界を可視化する場合を対照させる短いラベルとしては働く。しかし、証明論的に独立した新分類を与えず、標準概念より診断解像度が低い。従って C2・C3 へは上げない。

negative result として重要なのは、Gödel が「閉包反転」の実例だと証明されたのではなく、**閉包語彙は Gödel の機構を発見・区別する道具にはならず、標準的分析後の比較要約にのみ使える**と分かったことである。

# 8. 最終出力

## A. Gödel 第1の解剖

- \(Q\) 以上の表現力、c.e. 公理化、整合性を固定すると、Rosser 文 \(R_T\) が \(T\) で証明も反証もできない。
- 結論は syntactic incompleteness であり、「全ての真理に証明不能性がある」という一般命題ではない。
- 自己参照は仮定でなく、syntax coding と diagonal lemma から構成される。
- 独立文は \(T\) 内部にあるが、その独立性判定はメタ理論にある。

## B. Gödel 第2の解剖

- 標準 \(\Sigma_1\) provability predicate と D1–D3 を固定したとき、整合的な \(T\) は \(\mathrm{Con}(T)=\neg\mathrm{Pr}_T(\ulcorner0=1\urcorner)\) を証明できない。
- 結論は \(\mathrm{Con}(T)\) の偽性でも、強い外部理論による証明不能性でもない。
- Löb の定理が、内部 reflection から矛盾の可証性への帰結を与える。
- provability predicate と consistency sentence の選択は定理の一部であり、曖昧化できない。

## C. 通常21定理との最大の違い

1. 結論 \(P\) が positive closure ではなく、syntactic completeness または internal self-certification の限界である。
2. 限界文は理論 \(T\) に相対的で、整合的・効果的な拡張に伴って再生成される moving boundary である。
3. Gödel の限界は R2 型補正項ではなく、標準分類では independence / unprovability / reflection limitation である。

## D. 「閉包反転」判定

**C1 — 説明比喩としてのみ有効。** 技術分類としては diagonalization、representability、essential incompleteness、reflection の方が明確である。

## E. 今回の研究ログとの類似判定

**G1 — structural analogy。** 推論装置を対象化し自身の操作記述を戻すと制約が生じる、という限定的類似はあるが、形式的写像はまだない。

## F. 次の検査候補

1. **Tarski undefinability theorem:** semantic truth と syntactic provability の境界を直接検査し、「真だが証明不能」の混同をさらに分解できる。
2. **Löb’s theorem:** 第2不完全性定理の核である internal reflection の条件を単独で調べ、「閉包反転」より精密な標準構造を確認できる。
3. **Gödel completeness theorem:** 一階論理の semantic completeness と算術理論の syntactic incompleteness が両立する理由を固定し、既存の compactness 分析との接続を検査できる。

# 9. 検証資料

- [Gödel, “On Formally Undecidable Propositions…” 英訳](https://jamesrmeyer.com/ffgit/godel-original-english) — 原版が \(\omega\)-consistency を用いること、および構文の再帰的定義可能性・表現可能性の役割の確認。
- [Rosser, “Extensions of Some Theorems of Gödel and Church”](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/barkley-rosser-extensions-of-some-theorems-of-godel-and-church-the-journal-of-symbolic-logic-vol-1-1936-pp-8791/F675C77B8DB265503F632E5649E629EB) — plain consistency への改良の原典。
- [Kirst & Larchey-Wendling, “Gödel’s Theorem Without Tears”](https://drops.dagstuhl.de/opus/volltexte/2023/17491/pdf/LIPIcs-CSL-2023-30.pdf) — \(Q\) の全ての整合的公理化拡張が独立文を持つという現代的・形式化された確認。
- [Kurahashi, “A Note on Derivability Conditions”](https://arxiv.org/pdf/1902.00895) — D1–D3、Löb の定理、第2不完全性定理の関係。
- [Kurahashi, “On the Second Incompleteness Theorem and Provability Predicates”](https://www2.kobe-u.ac.jp/~tk/jp/slides/2021_Goedel90_Kurahashi.pdf) — consistency sentence と provability predicate の選択に対する第2定理の感度。

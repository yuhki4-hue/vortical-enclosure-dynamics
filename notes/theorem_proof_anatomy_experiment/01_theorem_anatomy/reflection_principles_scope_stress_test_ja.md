# Reflection principles：証明の解剖 special stress test

## 0. 目的と参照枠

本稿は、通常21定理、Gödel、Tarski、Löb、GL の stress test を継承し、reflection principles を単一定理ではなく **scope-indexed proof-theoretic architecture** として分析する。

「閉包」「閉包反転」「残差」「自己保証」「断絶交渉」「証明デザイン」は比較用のメタ記述であり、標準 proof theory の用語ではない。技術記述では local / uniform / global reflection、formula-class restriction、consistency、soundness、theory progression、ordinal analysis、GL / GLP を優先する。

今回の中心仮説は、「自己保証」が single local reflection では比較ラベルとして働いても、uniform / global reflection や semantic soundness まで含めると型とレベルの差を隠すのではないか、である。S2 を維持するのでなく、積極的に kill test する。

# 1. 対象理論と表記の固定

## 1.1 主分析の理論

最弱条件競争を避け、次を標準設定とする。

- \(B\): coding と初等的 metamathematics を扱う基礎理論。原則として \(EA\) または必要に応じて \(I\Sigma_1\)
- \(T\): \(B\) を含む、計算可能に公理化された古典一階算術理論。代表例は \(PA\)
- \(\mathrm{Prf}_T(p,x)\): 固定した公理提示に関する有限 \(T\)-proof relation
- \(\mathrm{Pr}_T(x)\equiv\exists p\,\mathrm{Prf}_T(p,x)\): 標準 provability predicate
- \(\Gamma\): \(\Sigma_1,\Pi_1,\Sigma_n,\Pi_n\) など、reflection の対象を制限する formula class

どの base theory がどの coding・partial truth・induction・conservation proof を形式化できるかは結果ごとに異なる。本稿は \(EA/I\Sigma_1\) を安全な代表基礎として使い、全ての最弱条件を一つに統一しない。

## 1.2 coding と numeral substitution

\(\varphi(v)\) の code と数 \(x\) から \(\varphi(\bar x)\) の code を返す primitive recursive substitution function を \(\mathrm{Sub}(\ulcorner\varphi(v)\urcorner,x)\) と書く。慣用記法

\[
\mathrm{Pr}_T(\ulcorner\varphi(\dot x)\urcorner)
\]

は

\[
\mathrm{Pr}_T(\mathrm{Sub}(\ulcorner\varphi(v)\urcorner,x))
\]

の略記とする。uniform reflection ではこの内部 substitution が本質的である。

# 2. Reflection family の採用定義

## 2.1 Single local reflection

固定した閉じた算術文 \(\varphi\) に対する一つの文

\[
\mathrm{Rfn}_\varphi(T):
\quad
\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\to\varphi.
\]

Löb の定理が直接扱うのは、同じ \(T\) がこの一文を証明する場合である。

## 2.2 Local reflection schema

全ての閉じた \(L_T\)-文 \(\sigma\) に対する schema

\[
\mathrm{Rfn}(T)
=
\{
\mathrm{Pr}_T(\ulcorner\sigma\urcorner)\to\sigma
:
\sigma\text{ is an }L_T\text{-sentence}
\}.
\]

一つの formula ではなく、文ごとの axioms の集合である。

## 2.3 Restricted local reflection

formula class \(\Gamma\) を固定し、

\[
\mathrm{Rfn}_\Gamma(T)
=
\{
\mathrm{Pr}_T(\ulcorner\sigma\urcorner)\to\sigma
:
\sigma\in\Gamma\text{ and }\sigma\text{ is closed}
\}
\]

とする。\(\Gamma\subseteq\Delta\) なら axiom inclusion はあるが、base theory 上の proof-theoretic strength が常に strict な全順序になるとは限らない。

## 2.4 Uniform reflection

\(\Gamma\)-formula \(\varphi(v)\) に対する schema

\[
\mathrm{RFN}_\Gamma(T)
=
\left\{
\forall x\,
\bigl(
\mathrm{Pr}_T(\mathrm{Sub}(\ulcorner\varphi(v)\urcorner,x))
\to
\varphi(x)
\bigr)
:
\varphi\in\Gamma
\right\}.
\]

複数変数・parameters を許す版もあるが、本稿では自由変数が \(v\) 一つの parameter-free 版を主表示とする。uniform sentence は全ての domain elements、nonstandard model では nonstandard elements も一括して量化するため、標準 numeral ごとの local instances の単なる外部的列挙ではない。

## 2.5 Global reflection

「global reflection」には複数の用法がある。本稿では、元の算術言語 \(L_T\) に新しい truth predicate \(\mathrm{Tr}\) を加えた typed expanded language を採用し、\(L_T\)-sentence codes について

\[
\mathrm{GRP}(T):
\quad
\forall y\,
\bigl(
\mathrm{Sent}_{L_T}(y)\land\mathrm{Pr}_T(y)
\to
\mathrm{Tr}(y)
\bigr)
\]

とする。\(\mathrm{Tr}\) には少なくとも \(L_T\)-formulas に対する compositional truth axioms または適切な T-biconditionals を与える。truth-containing expanded language 自身の全 truth を同じ predicate が無制限に扱うとは仮定しない。

これは一つの expanded-language sentence に全 theorem codes をまとめる形式であり、arithmetic-only local / uniform schemas から qualitative shift している。

## 2.6 Consistency

\[
\mathrm{Con}(T)
\equiv
\neg\mathrm{Pr}_T(\ulcorner\bot\urcorner).
\]

古典論理では

\[
\mathrm{Pr}_T(\ulcorner\bot\urcorner)\to\bot
\]

と同値なので、single local reflection at \(\bot\) である。ただし contradiction の非可証性だけを述べ、全 reflection schema や semantic soundness と同一ではない。

## 2.7 External semantic soundness

意図された構造 \(\mathbb N\) に対して

\[
T\vdash\sigma
\quad\Longrightarrow\quad
\mathbb N\models\sigma
\]

が全 \(L_T\)-sentences \(\sigma\) について成り立つ、という metatheoretic property。これは \(T\) 内部の formula/schema ではない。internal reflection や \(\mathrm{Con}(T)\) と同じレベルへ置かない。

# 3. 通常15項目による architecture anatomy

1. **system_or_principle_name:** Arithmetic reflection principles family

2. **domain:** proof theory・metamathematics・arithmetical theories・ordinal analysis

3. **standard_definitions:** 計算可能に公理化された算術理論 \(T\) と標準 \(\mathrm{Pr}_T\) に相対して、single local、local schema、\(\Gamma\)-restricted local、\(\Gamma\)-uniform、truth predicate を用いる global reflection、consistency、external soundness を上記のとおり区別する。

4. **assumptions_ABC:**
   - A: coding・induction・初等 metamathematics を扱う base theory \(B\)
   - B: reflected theory \(T\) の言語 \(L_T\) と、\(T\) の計算可能な公理提示
   - C: その提示に関する標準 proof / provability predicate \(\mathrm{Prf}_T,\mathrm{Pr}_T\)
   - D: reflection scope。single sentence、all sentences、formula class \(\Gamma\)、uniform formulas のいずれか
   - E: uniform reflection では numeral-substitution coding
   - F: global reflection では expanded language、truth predicate \(\mathrm{Tr}\)、その compositional / disquotational axioms
   - G: iteration を行う場合の reflection operator、ordinal notation system、successor / limit stage rule
   - H: 外部から truth、soundness、consistency、conservativity を判定する metatheory
   - I: 必要な coding と schema を検証する induction strength

5. **hypothesis_levels:**
   - A: ambient。形式化を行う基礎舞台
   - B: object＋ambient。反射される対象理論とその言語
   - C: definitional＋object。どの presentation の theoremhood かを固定
   - D: definitional。reflection scope の型と formula complexity を固定
   - E: background＋definitional。uniform schema の構文操作
   - F: ambient＋object。global reflection 用の拡張言語と truth theory
   - G: definitional＋ambient。theory progression の生成規則と index
   - H: background。internal axiom ではない
   - I: ambient＋object。base theory の証明能力

   formula class \(\Gamma\) は \(T\) の「性質」ではなく、どの reflection instances を追加するかという scope definition である。

6. **condition_types:**
   - A: 基礎算術
   - B: 効果的公理化・対象言語
   - C: proof coding・provability predicate
   - D: formula-class restriction・reflection scope
   - E: substitution / numeralization
   - F: truth / satisfaction machinery
   - G: transfinite iteration
   - H: semantic metatheory
   - I: induction strength

7. **closure_roles:**
   - A: formalization base
   - B: reflected-object fixation
   - C: theoremhood internalization
   - D: scope control / complexity calibration
   - E: instance-to-uniform bridge
   - F: semantic packaging / global quantification
   - G: strength progression
   - H: external correctness judgment
   - I: coding and induction support

   「自己保証」は closure role に採用しない。どの reflection scope かを示さないためである。

8. **conclusion_or_strengthening_P:** reflection principle を外部から \(T\) へ追加して

\[
T^+=T+\mathrm{Rfn}_\Gamma(T),
\quad
T^+=T+\mathrm{RFN}_\Gamma(T),
\quad\text{or}\quad
T^+=T+\mathrm{GRP}(T)
\]

のような stronger theory を構成し、\(T\)-provability から対象文・全数 instance・truth への橋を新しい axioms として与える。得られる strength、conservation、consistency strength は scope、\(\Gamma\)、base、truth axioms に依存し、単一の結論 \(P\) には還元できない。

9. **blocked_escape_routes:**
   - A: reflection を形式化できないほど弱い metatheoretic base へ退く自由を制限する
   - B: proof set を非効果的にして provability predicate を失う道を塞ぐ
   - C: presentation / provability predicate を任意に変更して reflection sentence の意味を変える自由を制限する
   - D: 対象 formula complexity を無制限に混ぜる道を塞ぎ、strength comparison の単位を固定する
   - E: 標準 numeral の各 instance だけを外部から確認し、nonstandard assignments を含む全 \(x\) の主張を避ける道を塞ぐ
   - F: sentence ごとの schema に留まり、全 theorem codes を一文で semantic にまとめない道を塞ぐ。ただし代わりに truth theory を導入する
   - G: 一段の extension で止まり、新理論自身への reflection を問わない道を塞ぐ
   - H: internal reflection と external soundness を無区別にすることを防ぐ
   - I: substitution・partial truth・schema reasoning の内部検証が induction 不足で停止する道を制限する

10. **what_fails_if_removed:**
   - Aを外すと: coding や reflection schema の内部形式化ができず、同じ architecture を述べられない場合がある
   - Bの効果的公理化を外すと: 標準的 arithmetized provability predicate を得る保証がなくなり、reflection formula の型が変わる
   - Cを外すと: Rosser、slow、Fefermanian など別 provability predicates が入り、\(\mathrm{Con}(T)\) と reflection strength が predicate-dependent になる
   - Dを外すと: restricted / full、local / uniform が混ざり、strength comparison が未指定になる。「reflectionを追加した」というだけでは定理にならない
   - Eを外すと: uniform reflection の antecedent code を変数 \(x\) と連動させられず、local instances の集合へ戻る
   - Fを外すと: 採用した global reflection sentence \(\forall y(\mathrm{Pr}_T(y)\to\mathrm{Tr}(y))\) を表現できない。arithmetic-only schemas は残る
   - Gを外すと: 一段の reflection extension は残るが、progression・limit stage・ordinal analysis は生じない
   - Hを外すと: external soundness や「reflection axioms が \(\mathbb N\) で正しい」という判定場所が失われる
   - Iを弱めると: reflection schema 自体は書けても、equivalence・conservation・iteration の内部証明可能性が変わる。単純な反例でなく別の弱基礎上の理論へ移る

11. **what_reappears_if_removed:**
   - A: **R0/R1** — 形式化不能（R0）、またはより弱い coding regime（R1）
   - B: **R1** — 非効果的 theory / alternative derivability notions
   - C: **R1** — provability-predicate dependence
   - D: **R1** — formula-class remainder と非比較可能な strength choices
   - E: **R1** — standard-instance schema と nonstandard assignments の隔たり
   - F: **R1** — truth-free local / uniform schemas への後退。global packaging は失われる
   - G: **R1** — next-stage question を未定義にした単発 extension
   - H: **R0** — semantic correctness の判定枠が失われる
   - I: **R1** — base-theory sensitivity、induction / conservation の追加自由度

   個別除去には R1 が現れるが、family 全体を「残差」で束ねる有用性は後で RX として再検査する。

12. **proof_resources:**
   - representative routes:
     - arithmetization of syntax と derivability conditions
     - diagonal lemma / Löb theorem による internal unprovability analysis
     - partial truth definitions for \(\Sigma_n/\Pi_n\) classes
     - induction on formula complexity
     - conservation theorems and reductions between local / uniform reflection
     - transfinite recursion on ordinal notations
     - cut elimination、\(\omega\)-rule、reflection calculus
     - GL for one provability modality、GLP / reflection calculi for graded modalities
   - note: これらは reflection principles の定義仮定ではない。特に diagonal lemma、ordinal analysis、GLP を assumptions に昇格させない。

13. **architecture_style:** scope-indexed reflection progression／階層的理論強化

14. **principle_vs_metatheory_comment:** reflection axioms が固定するのは、どの \(T\)-provability を、どの formula class と量化形式で、どの extension theory に受け入れるかである。証明資源はその extension の consistency strength、conservation、iteration を分析する。external soundness を reflection axiomとして数えると、object-language schema と metatheoretic correctness property が混同される。

15. **short_comment:** reflection family は「体系がどれだけ自分を信じるか」という一軸ではない。sentence scope、variable uniformity、formula complexity、truth language、iteration stage が独立に strength と型を変える多軸 architecture である。

# 4. Reflection scope matrix

| principle | 対象 | 形式 | truth predicate 必要? | strength | Löbとの直接関係 |
|---|---|---|---|---|---|
| single local reflection | 固定 sentence \(\varphi\) | \(\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\to\varphi\) | 不要 | \(\varphi\) に依存。一文だけでは一般に順位づけ不能 | **直接**。同じ \(T\) が証明すれば Löb により \(T\vdash\varphi\) |
| local reflection schema | 全 closed sentences | 文ごとの \(\mathrm{Rfn}_\sigma(T)\) | 不要 | 各 single instance を含み、\(\mathrm{Con}(T)\) も含む | instanceごとに直接。schema 全体は一文ではない |
| \(\Gamma\)-restricted reflection | \(\Gamma\)-sentences | \(\mathrm{Rfn}_\Gamma(T)\) | 不要。固定 arithmetical class には partial truth を補助的に使える | \(\Gamma\)、base、predicate に依存。包含はあるが単純な strict chain とは限らない | \(\Gamma\) 内の各 instance に直接 |
| uniform reflection | formulas \(\varphi(x)\) と全 domain elements | \(\forall x(\mathrm{Pr}_T(\ulcorner\varphi(\dot x)\urcorner)\to\varphi(x))\) | arithmetic-only schema には不要 | 対応する standard local instances の単なる集合より一般に強い。formula class が主要因 | closed formulaを含む限り instancewise に接続するが、uniformity全体は単一 Löb formulaで尽くされない |
| global reflection | 全 \(T\)-sentence codes | \(\forall y(\mathrm{Sent}(y)\land\mathrm{Pr}_T(y)\to\mathrm{Tr}(y))\) | **必要**（採用版） | truth theory と induction に依存。arithmetic-only reflection と単純全順序化しない | truth biconditionals から local instancesを回収するため間接的 |
| consistency | contradiction \(\bot\) | \(\neg\mathrm{Pr}_T(\ulcorner\bot\urcorner)\) | 不要 | single local instance。full reflection より scope が狭い | **直接**。Löb at \(\bot\)、Gödel II |
| external soundness | 全 \(T\)-theorems と intended model | \(T\vdash\sigma\Rightarrow\mathbb N\models\sigma\) | external satisfaction が必要 | theory axiomの strength ではなく metatheoretic property | internal Löbの直接対象でない。外部から consistency を含意 |

strength 欄は axiom inclusion、conservation、proof-theoretic ordinalなど、採用した比較基準がある場合だけ意味を持つ。「自己保証度」という単一スカラーは置かない。

# 5. Löb の S2 を直接ストレステスト

## Q1. Single local instance と local schema 全体は同じか

同じではない。single instance は一つの closed sentence \(\varphi\) に相対する。local schema は無限個の sentence instances を新理論の axioms として加え、その中に \(\varphi=\bot\) の \(\mathrm{Con}(T)\) も含む。

Löb は各 instance について

\[
T\vdash\mathrm{Rfn}_\varphi(T)
\quad\Longrightarrow\quad
T\vdash\varphi
\]

を与える。しかし外部から \(T+\mathrm{Rfn}(T)\) を構成することは禁止しない。前者は same-theory theoremhood、後者は theory extension である。

## Q2. Uniform reflection は local reflection の単なる束か

単なる束ではない。uniform axiom

\[
\forall x\,
(\mathrm{Pr}_T(\ulcorner\varphi(\dot x)\urcorner)\to\varphi(x))
\]

は、各 standard numeral \(\bar n\) の local instanceを全て導く。しかし、逆向きに外部から standard instances を無限に並べても、weak/nonstandard model 内の全 \(x\) を一つの universal sentence で統制することにはならない。

numeral substitution の coding、formula parameters、induction、nonstandard proof codes が関与するため、local→uniform は単なる量的拡大ではなく proof-theoretic strength の変化を伴う。restricted \(\Sigma_n/\Pi_n\) uniform reflection は、算術断片の strength calibration に用いられる。

## Q3. Global reflection は uniform reflection のさらに強い版か

採用版では質的に異なる。global reflection は variable \(x\) についての一つの formula familyでなく、任意の sentence code \(y\) の内容を \(\mathrm{Tr}(y)\) で評価する。そのため expanded language と truth axioms が必要になる。

適切な compositional truth axioms の下で global reflection から多くの local / uniform reflection consequences を得られる場合がある。しかし truth theory の induction、typing、compositionality により strength が変わり、arithmetic-only uniform reflection との無条件な全順序比較はできない。

## Q4. Consistency は「最小の自己保証」か

構文上は single local reflection at \(\bot\) という最小 scope の代表例である。しかし「最小の自己保証」と呼ぶと、consistency が全 theorem の correctness を少しずつ保証するかのように誤解される。実際には contradiction の非可証性だけを述べる。

従って正確な位置は **one distinguished local reflection instance** であり、一般的 soundness の低い度数ではない。

## Q5. External soundness と internal reflection を同じ語で呼べるか

技術的には不可である。external soundness は metatheory で \(T\vdash\sigma\Rightarrow\mathbb N\models\sigma\) と判断する property、internal reflection は arithmetic formula/schema である。global reflection で両者を接続するには truth predicate と truth axiomsを新言語へ導入する必要がある。

「自己保証」は、この level transition を隠す限り危険な一括語になる。

# 6. Same theory と external extension の決定的区別

## 6.1 Same theory

固定した \(\varphi\) について

\[
T\vdash
\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\to\varphi
\]

なら、Löb により \(T\vdash\varphi\)。従って非定理 \(\varphi\) に対する local reflection instance を、同じ \(T\) が自由に証明することはできない。

特に \(\varphi=\bot\) なら、外部で \(T\) が整合的なとき \(T\nvdash\mathrm{Con}(T)\)。

## 6.2 External extension

外部メタ理論から

\[
T^+
=
T+\{
\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\to\varphi
\}
\]

または

\[
T^+
=
T+\mathrm{RFN}_\Gamma(T)
\]

を定義することはできる。ここで追加 axiom の provability predicate は \(\mathrm{Pr}_{T^+}\) でなく \(\mathrm{Pr}_T\) を参照する。Löb の antecedent \(T\vdash\mathrm{Rfn}_\varphi(T)\) は成立していないので、矛盾はない。

新理論 \(T^+\) は元の \(T\)-reflection を持つが、同種の \(T^+\)-reflection を自動的には持たない。\(T^+\) が十分強く整合的なら、少なくとも \(\mathrm{Con}(T^+)\) について再び Gödel II の制約を受ける。

この差は reflection theory 全体の最重要点である。「体系が自分を保証する」と「外部から元体系の reflection を公理化する」を同一視してはならない。

# 7. Reflection progression と moving boundary

## 7.1 採用する progression

formula class \(\Gamma\) と有効な ordinal notation system を固定し、

\[
T_0=T,
\]

\[
T_{\alpha+1}
=
T_\alpha+\mathrm{RFN}_\Gamma(T_\alpha),
\]

\[
T_\lambda
=
\bigcup_{\beta<\lambda}T_\beta
\quad(\lambda\text{ limit})
\]

とする。local reflection、uniform reflection、consistencyだけを反復する別 progressions もある。採用する reflection operator が違えば同じ ordinal index でも theory strength は変わる。

## 7.2 Strength growth

successor stage \(T_{\alpha+1}\) は \(T_\alpha\) の reflection axioms を持つ。適切な soundness conditions の下では通常 \(T_\alpha\) より強いが、どの sentence class に関する conservativity / nonconservativity を測るかで比較は変わる。

limit stage は以前の axioms の union であり、新たな一個の semantic truth principle を自動的に加えるわけではない。notation system の有効性と base theory 内での progression の表現可能性も別条件である。

## 7.3 Moving boundary

\(T_{\alpha+1}\) は \(T_\alpha\) の reflection を扱えても、自身の同じ reflection を自動的に証明しない。特に適切な整合性条件のもとで

\[
T_{\alpha+1}\nvdash\mathrm{Con}(T_{\alpha+1}).
\]

従って「強い理論へ移れば旧 boundary を越えるが、新理論に相対した boundary が現れる」という構造は、Gödel / Löb より reflection progression で明示的になる。

ただし標準名は **Turing–Feferman progression / iterated reflection hierarchy** である。「moving residual」や「残差保存」と呼ぶ追加的理由はない。

# 8. Ordinal analysis との接続

transfinite reflection progression は、ordinal notation \(\alpha\) に沿って理論を反復し、どの段階までの reflection が対象理論の theorem strength を再現・保存するかを測る。Schmerl 型の fine-structure / conservation results は、異なる complexity level の local・uniform reflection iterations 間の関係を与える。Beklemishev 型の分析では、こうした progressions を算術断片の proof-theoretic analysis に用いる。

ここで ordinal は単なる「保証量」ではない。

- どの notation system を採用するか
- どの reflection operator を反復するか
- どの formula class の consequences を測るか
- どの base theory 上で equivalence / conservation を証明するか

が必要である。従って「自己保証度」という一次元量では ordinal analysis を代替できない。

一方、「証明デザイン」P2 は、base＋formula class＋reflection operator＋iteration rule が proof-theoretic strength を組織するという architecture comparison まで耐える。ただしこれは既存 ordinal analysis の再記述であり新理論ではない。

# 9. Formula-class restriction の役割

## 9.1 Restricted local

\(\mathrm{Rfn}_{\Sigma_n}(T)\)、\(\mathrm{Rfn}_{\Pi_n}(T)\) は、closed sentence の complexity を制限する。class inclusion がある場合には axiom inclusion を得るが、base theory が syntactic class の変換をどこまで証明できるか、dual class に対する conservation があるかによって実質 strength は変わる。

## 9.2 Restricted uniform

\(\mathrm{RFN}_{\Sigma_n}(T)\)、\(\mathrm{RFN}_{\Pi_n}(T)\) は、formula \(\varphi(x)\) の complexity を制限する。外部的には corresponding \(\Gamma\)-soundness を表すが、内部 axiom schema と external soundness property は同一レベルではない。

各固定 \(n\) には arithmetical partial truth / satisfaction predicates を構成できるため、restricted reflection を一文または有限 complexity の形式へまとめるルートがある。しかし全 arithmetical hierarchy を一つの同一言語 truth predicate で覆うこととは違い、Tarski の full truth obstacle を回避するのは complexity bound が固定されているからである。

## 9.3 一軸化できない理由

formula class の拡大、local→uniform、base theory の強化、iteration length の増大は別の座標である。例えば「\(\Sigma_n\) から \(\Sigma_{n+1}\)」と「一段 reflection を追加」は同じ操作ではない。従って family の strength を単なる自己保証の大小として並べない。

# 10. Gödel 第2との比較

| 項目 | Gödel II | Reflection principles |
|---|---|---|
| target | \(\mathrm{Con}(T)\) | local / uniform / global schemas と extensions |
| scope | \(\bot\) | 一文、class、variables、全 sentence codes |
| formula class | single \(\Pi_1\) consistency sentence（標準 coding） | \(\Sigma_n,\Pi_n\)、full arithmetic、truth language 等 |
| theory extension | 結論は \(T\nvdash\mathrm{Con}(T)\)。外部から \(T+\mathrm{Con}(T)\) は構成可能 | reflection axiomsを外部から加えて \(T^+\) を構成 |
| iteration | consistency iteration / Turing progression へ拡張可能 | local / uniform reflection progressions を直接扱う |
| strength growth | 一段ごとに元理論の consistency strength を加える | scope と class に応じ、より細かな conservation / ordinal strength を持つ |

Gödel II は、標準 \(\mathrm{Con}(T)\) を single local reflection at \(\bot\) と見る意味で reflection family の **最小 scope の代表的特殊例**である。ただし「全 reflection の最弱原理」という一般順序を自動的に与えるわけではなく、proof predicate と比較基準に依存する。

# 11. Löbとの比較

| 項目 | Löb | Reflection extension |
|---|---|---|
| theory | 同じ \(T\) | 新理論 \(T^+\supset T\) |
| premise | \(T\vdash\mathrm{Rfn}_\varphi(T)\) | metatheory が \(\mathrm{Rfn}_\varphi(T)\) / schema を axiom として選ぶ |
| predicate | \(\mathrm{Pr}_T\) | added axioms は通常 \(\mathrm{Pr}_T\) を参照 |
| conclusion | \(T\vdash\varphi\) | \(T^+\vdash\mathrm{Rfn}_\varphi(T)\)。一般に \(T^+\) はより強い |
| new boundary | 非定理への internal local reflection は不可 | \(T^+\) 自身の reflection / consistency が次の問題 |

Löb は reflection principle の追加を禁止しない。「同じ \(T\) が自分に関する reflection を theorem にする」場合の collapse を述べる。reflection theory は、外部から旧理論 \(T\) を対象化して stronger theory を作る。この subject shift がなければ progression 全体を誤読する。

# 12. GL / GLPとの比較

## 12.1 単一 modality GL の射程

GL の一つの \(\Box\) は、固定した provability predicate の normal modal principles、provability iteration、Löb axiom

\[
\Box(\Box p\to p)\to\Box p
\]

を捉える。従って single local reflection と same-theory Löb constraint の抽象化には適する。

しかし propositional GL 単独では、次を内部的に区別できない。

- \(\Sigma_n/\Pi_n\) formula complexity
- numeral substitution を伴う uniform reflection
- truth predicate を持つ global reflection
- transfinite stages \(T_\alpha\)
- 異なる strength の複数 provability predicates

## 12.2 GLP / polymodal provability logic

Japaridze の GLP は modalities

\[
[0],[1],[2],\ldots
\]

を持ち、arithmetical interpretations では段階の異なる強い provability / \(n\)-provability notions を表す。dual modalities \(\langle n\rangle\) は \(n\)-consistency / restricted reflection strength と接続し、Beklemishev の ordinal analysis では modal words が reflection progressions と ordinal notations を符号化する。

これは、reflection hierarchy が single \(\Box\) の GL だけでは粗すぎることを示す。ただし GLP でさえ、採用した global truth predicate や external semantic soundness をそのまま同一 operator familyへ還元するわけではない。

full uniform reflection を扱うには、variablesを sentencesでなく theoriesへ解釈する reflection calculi や、追加 modality \(\langle\omega\rangle\) を持つ拡張が用いられる。この事実は、「自己保証 S2」が単一 local modality の範囲では安定しても、reflection family 全体の一軸分類としては不足することを示す。

# 13. Tarskiとの境界

local / restricted / uniform arithmetic reflection は、各 formula \(\varphi\) 自体を consequent に置く schema なので、full truth predicate を同一算術言語に定義する必要はない。formula class を固定すれば partial satisfaction predicates も利用できる。

一方、全 sentence codes \(y\) を一つの変数で走査し、その内容が真であると一文で言う global reflection

\[
\forall y\,
(\mathrm{Sent}_{L_T}(y)\land\mathrm{Pr}_T(y)\to\mathrm{Tr}(y))
\]

には truth predicate が必要になる。Tarski の定理により、十分強い算術言語自身の full standard truth を同じ算術式で定義することはできない。従って採用版は typed expanded language と compositional truth axioms を用いる。

ここが provability theory から truth theory へ接触する地点である。

\[
\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\to\varphi
\]

は一つの reflection instanceであり、

\[
\mathrm{Tr}(\ulcorner\varphi\urcorner)\leftrightarrow\varphi
\]

は truth predicate の adequacy condition である。前者を全 instances へ拡大しても、後者を同じ算術言語内に定義したことにはならない。

# 14. 「証明デザイン」P2 の再検査

reflection theory では

\[
\text{base theory}
+\text{formula class}
+\text{reflection form}
+\text{iteration rule}
+\text{ordinal notation}
\]

が、どの extension と proof-theoretic strength を得るかを組織する。これは theorem anatomy より一段上の theory architecture であり、比較軸として実質的に機能する。

**再判定: P2 — proof architecture / theory architecture の比較枠として有効。**

P2 が有効なのは、各軸を標準用語で分離するからである。「設計」という語だけでは conservation theorem や ordinalを予測しない。標準 reflection theory / ordinal analysis を超える P3 には進めない。

# 15. 「残差」再検査

候補として挙げられるものは相互に異なる。

- unproved reflection instance: sentence / schema の theoremhood status
- stronger theory: axiom extension
- formula-class remainder: scope selection
- next reflection stage: progression operator の適用結果
- ordinal progression: theory hierarchy の index

\(T_\alpha\) の次に \(T_{\alpha+1}\) があることを「残差が再生成された」と呼んでも、どの reflection operator、formula class、conservation levelかは分からない。standard theory progression の方がはるかに明確である。

**判定: RX — residual vocabulary not useful here.**

局所的な条件除去表では R1 を記録できるが、reflection progression 自体の分類には residual vocabulary を棄却する。R2 の明示的補正項もない。

# 16. Erasure Test

「自己保証」「閉包」「閉包反転」「残差」「断絶交渉」を全削除しても、次だけで今回の技術的差分を記述できる。

- local / restricted / uniform / global reflection
- consistency と external soundness
- same-theory provability と external theory extension
- formula complexity と partial truth
- reflection progression と ordinal analysis
- GL / GLP / reflection calculus
- Tarski undefinability と typed truth theories

数学的内容、strength comparison、level distinction、iteration structureは何も失われない。一方、既存 stress tests との横断的導線、すなわち local reflection から scope を広げたとき比較ラベルが壊れる、という教育的見通しは少し弱くなる。

**判定: E1 — 教育的・比較的な見通しだけ失う。**

E2・E3 は棄却する。

# 17. 「自己保証」S2 の kill test

| kill condition | 検査結果 |
|---|---|
| 1. local / uniform / global が proof-theoretically 異なり、一括語が差を隠す | **成立** |
| 2. consistency と soundness を同一軸へ置くと level confusion が起きる | **成立** |
| 3. truth predicate の有無が qualitative difference を作る | **成立**。global reflection で expanded truth languageへ移る |
| 4. formula class が strength hierarchy の主要因 | **成立** |
| 5. reflection iteration が ordinal analysis に接続し、単純比喩で不足 | **成立** |
| 6. standard reflection terminology だけで比較可能 | **成立** |

kill conditions はほぼ全面的に成立する。ただし single local reflection に限れば、「内部化した proof predicate に対する特定文の correctness bridge」という Löb / GL との比較点を「自己保証」が短く示す。restricted local も必ず \(\Gamma\) を併記すれば、その局所比較を保持できる。

## 最終再判定

**S2\* — 限定的S2。**

- single local reflection: 比較ラベルとして有効
- \(\Gamma\)-restricted local reflection: scope を明記する場合に限り限定的に有効
- uniform reflection: 一括語では substitution・quantification・nonstandard instances を隠す
- global reflection: truth machinery への qualitative shift を隠す
- consistency: local at \(\bot\) と明記しないと誤解を生む
- external soundness: internal principle と層が違うため「自己保証」に含めない

従って S2 は reflection family 全体へ拡張できない。S0 まで棄却しないのは、Löb / GL の local comparison では依然として明確な限定用途があるためである。S3 は棄却する。

# 18. 研究ログとの比較

| research-log side | reflection side | 判定 |
|---|---|---|
| universal truth guarantee を試みる | global reflection / semantic soundness | 語の類似だけでは level が違う |
| self-application 問題 | \(\mathrm{Pr}_{T_\alpha}\) に対する同段階 reflection | 構造的類似 |
| scope を狭める | local / \(\Gamma\)-restricted reflection | scope control の類似 |
| global guarantee から局所比較へ縮退 | global→uniform→local の分解 | methodology-level の類似 |
| 次段階へ移る | \(T_\alpha\mapsto T_{\alpha+1}\) | formal progression は reflection side にのみ存在 |

**類似判定: Q1 — scope enlargement に伴う制約という構造類似。**

研究ログ側に provability predicate、formula class、uniform substitution、truth predicate、ordinal-indexed progression の形式写像はない。従って Q2 の formal reflection hierarchy との対応は未成立であり、Q3 は棄却する。

# 19. 最終比較表

「inside same \(T\)?」は、同じ算術言語で表現できるかと、同じ \(T\) が実際に証明できるかを分けて記す。

| structure | inside same \(T\)? | formula scope | truth needed? | stronger theory generated? | iterable? | Löb constraint? |
|---|---|---|---|---|---|---|
| proof predicate | **表現可能**。標準 \(\mathrm{Pr}_T\) を \(T\) 内に定義 | 全 proof / sentence codes | 不要 | それ自体では no | modal nesting は可 | D1–D3を通じ Löb の前提構造 |
| single local reflection | **同言語で表現可能**。非定理 \(\varphi\) について同じ \(T\) では通常不可 | 一つの closed \(\varphi\) | 不要 | 外部から加えれば yes | 対象 theory を更新すれば yes | **直接** |
| local reflection schema | **各式は同言語**。整合的 \(T\) は全 schema を自力で持てない | 全 closed sentences | 不要 | yes | yes | 各 instance に直接 |
| restricted reflection | **各式は同言語** | \(\Gamma\)-sentences / formulas | 通常不要 | yes | yes、class-indexed | 対象 instance に直接・uniformity全体には不足 |
| uniform reflection | **同算術言語の schema**。substitution coding が必要 | \(\varphi(x)\) と全 \(x\) | full truth は不要 | yes、一般に local standard instances より強い | yes | closed instancesを介し間接。全 uniform structure は GL/Löb一式で尽くされない |
| global reflection | 採用版では **元の \(L_T\) 外**。truth-expanded language | 全 \(T\)-sentence codes | **yes** | truth theoryを伴い yes | typed truth / reflection iterationとして可 | local reflectionを回収する限り間接 |
| consistency | **同言語で表現可能**。整合的 \(T\) では一般に非可証 | \(\bot\) 一文 | 不要 | 外部追加で yes | Turing progressionとして yes | **直接**、Löb at \(\bot\) |
| semantic soundness | **no**。metatheoretic property | 全 theorems と intended semantics | external satisfaction | property自体は extensionでない。形式化すれば別 | metatheory hierarchyとして別問題 | internal Löbの直接対象でない |

# 20. kill criteria

| criterion | 判定 |
|---|---|
| 1. 「自己保証」が reflection scope の違いを消す | **成立** |
| 2. consistency / reflection / soundness の level 差を消す | **成立** |
| 3. uniform reflection を local の量的拡大と誤認させる | **成立** |
| 4. global reflection で Tarski 的 truth machinery を隠す | **成立** |
| 5. progression を moving residual と呼んでも ordinal analysis 以上の情報がない | **成立** |
| 6. GLP / polymodal logic が hierarchy を既に精密化する | **成立。ただし full global truth まで一括しない** |
| 7. 「証明デザイン」が既存 strength comparison の言い換えになる | **成立する限界あり。** P2 の横断整理に留め、P3へ上げない |

negative result を保存する。今回の語彙で最も安定したのは「証明デザイン」P2、最も明確に降格したのは reflection family 全体への「自己保証」S2、最も不要になったのは「残差」RX である。

# 21. 最終出力

## A. Reflection family の核心

- reflection は理論 \(T\)、provability predicate、formula class、scope に相対する。
- single local、schema、uniform、global、consistency、soundness は異なる型である。
- 外部から reflection を加えると stronger theory が生じる。
- 新理論自身の reflection は自動的に得られず、progression が形成される。
- strength は formula complexity、uniformity、truth axioms、iteration に依存する。

## B. local / uniform / global の最大の違い

1. local は固定 closed sentence またはその schema。
2. uniform は substitution coding と全 \(x\) の量化を含み、standard local instances の列挙ではない。
3. formula-class restriction が uniform reflection の strength を大きく左右する。
4. global は全 sentence codes を一文で扱うため、採用版では truth-expanded language が必要。
5. external soundness はこれらの internal principles ではなく metatheoretic property。

## C. Gödel II の位置

\(\mathrm{Con}(T)\) は single local reflection at \(\bot\)。reflection family の最小 scope の代表例だが、一般 soundness の弱い版ではない。外部から consistency を反復すれば Turing progression へ移る。

## D. Löb の位置

Löb は same \(T\) が固定 local reflection instance を証明する場合の theoremhood collapse を扱う。外部から旧 \(T\) の reflection を追加して \(T^+\) を作ることは禁止しない。両者の subject theory の違いが核心。

## E. GL / GLP の位置

- GL は single provability modality と local Löb structure を抽象化する。
- formula class、uniformity、transfinite stagesは単一 GL では表せない。
- GLP は複数 modalities により graded provability / reflection strength を扱う。
- reflection calculi と ordinal notations は progression の分析に接続する。
- global truth reflection と external soundness は GLP へそのまま還元されない。

## F. 「自己保証」最終判定

**S2\* — 限定的S2。** local reflection では有効だが、uniform / global / soundness まで広げると型・言語・メタレベルの差を隠して破綻する。

## G. 「証明デザイン」再判定

**P2。** base theory、formula class、reflection operator、iteration rule を分ける proof / theory architecture の比較枠として有効。新しい proof-theoretic framework ではない。

## H. residual 判定

**RX — residual vocabulary not useful here.** theory progression、unproved instance、formula remainder、counterpart theoryを一語でまとめる利点がない。

## I. Erasure Test

**E1。** 独自語彙を消しても数学的内容は全て残り、既存文書との教育的導線だけ少し失う。

## J. 研究ログとの類似

**Q1。** scope enlargement に伴う制約という構造類似のみ。formal reflection hierarchy との写像はない。

## K. 最も重要な新規観察

1. S2 は family 全体には耐えず、local reflection 限定の **S2\*** へ降格する。
2. uniform reflection は local instances の量的集合でなく、substitution・全称量化・nonstandard elementsを伴う質的強化である。
3. global reflection で truth languageへ移る地点が、provability reflection と semantic soundness の境界を可視化する。

## L. 次の一手

1. **GLP / reflection calculus anatomy:** multiple modalities が formula complexity と reflection iteration をどこまで正確に符号化するかを検査する。
2. **Turing–Feferman progressions:** consistency iteration と uniform reflection iteration の差を ordinal notation と conservation の観点から分解する。
3. **Global reflection / axiomatic truth theories:** truth predicate、induction、global reflection の strength を Tarski stress test と直接接続する。

# 22. 検証資料

- [L. D. Beklemishev, “Reflection Principles and Provability Algebras in Formal Arithmetic”](https://dspace.library.uu.nl/bitstream/handle/1874/26862/preprint236.pdf%3Bsequence%3D1) — local / uniform reflection の標準定義と provability-algebraic analysis。
- [L. D. Beklemishev, “Proof-Theoretic Analysis by Iterated Reflection”](https://link.springer.com/article/10.1007/s00153-002-0158-7) — local / uniform reflection hierarchies、conservation、算術断片の分析。
- [S. Feferman, “Transfinite Recursive Progressions of Axiomatic Theories”](https://www.mathnet.ru/eng/mat619) — transfinite theory progressions の基礎。
- [P. Pudlák, “Reflection Principles, Propositional Proof Systems, and Theories”](https://arxiv.org/pdf/2007.14835) — local / global reflection と soundness の形式的区別。
- [G. Berger and L. D. Beklemishev, “A Many-Sorted Variant of Japaridze’s Polymodal Provability Logic”](https://arxiv.org/pdf/1601.02857) — GLP、graded consistency、full uniform reflection modality。
- [L. D. Beklemishev and F. N. Pakhomov, “Reflection Algebras and Conservation Results for Theories of Iterated Truth”](https://arxiv.org/abs/1908.10302) — truth theories、reflection operators、ordinal notations。
- [M. Z. Łełyk, “Model Theory and Proof Theory of the Global Reflection Principle”](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/model-theory-and-proof-theory-of-the-global-reflection-principle/0A19B0BE4D761FD35A91113376794C07) — global reflection の形式的研究。

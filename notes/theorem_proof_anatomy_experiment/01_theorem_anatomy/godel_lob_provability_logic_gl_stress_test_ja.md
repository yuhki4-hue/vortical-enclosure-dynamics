# Gödel–Löb provability logic GL：証明の解剖 special stress test

## 0. 目的と参照枠

本稿は、theorem_proof_anatomy_v1.1_ja.md、Gödel・Tarski・Löb の三つの stress test を継承し、単一定理ではなく propositional modal logic GL を分析する。

「閉包」「閉包反転」「残差」「自己保証」「断絶交渉」「証明デザイン」「反射」「再入力」は比較用のメタ記述であり、標準 modal logic / provability logic の用語ではない。技術記述では modal derivability、normality、necessitation、Löb axiom、arithmetical realization、Kripke frame、fixed-point theorem を優先する。

維持する原則は次である。

1. system の定義条件と、その soundness / completeness の証明資源を分ける。
2. object / ambient / background / definitional を分ける。
3. 条件除去後を R0 / R1 / R2 で記録する。
4. syntactic provability、semantic truth、modal validity を混同しない。
5. pure modal derivability、arithmetical interpretation、Kripke semantics を分離する。
6. \(\Box\) を truth predicate や通常の closure operator と同一視しない。
7. modal fixed point を自然言語の liar paradox と同一視しない。
8. modal abstraction の成功を、本分析独自の語彙や研究仮説の正当化に使わない。

# 1. 採用定義

## 1.1 言語と Hilbert system

主分析では GL を、命題変数 \(p,q,\ldots\)、古典命題論理結合子、単項 modal operator \(\Box\) を持つ propositional modal logic とする。

**公理 schema**

1. 全ての古典命題論理 tautology
2. K axiom

   \[
   \Box(A\to B)\to(\Box A\to\Box B)
   \]

3. Löb axiom

   \[
   \Box(\Box A\to A)\to\Box A
   \]

**推論規則**

1. modus ponens
2. necessitation

   \[
   \vdash_{\mathrm{GL}}A
   \quad\Longrightarrow\quad
   \vdash_{\mathrm{GL}}\Box A.
   \]

通常どおり uniform substitution を axiom schema の理解に含める。GL では

\[
\Box A\to\Box\Box A
\]

すなわち axiom 4 が導出可能である。本稿の採用定義では 4 を独立公理に加えない。従って GL は K4 を含むが、\(\Box A\to A\) を持つ S4 とは両立しない。

## 1.2 最初に分離すべき三層

### A. pure modal syntax

GL の formula、axiom schema、modus ponens、necessitation、modal theoremhood \(\vdash_{\mathrm{GL}}A\)。ここでは \(\Box\) は形式記号であり、まだ特定の算術理論の provability predicate ではない。

### B. arithmetic interpretation

理論 \(T\) と標準 provability predicate \(\mathrm{Pr}_T\) を固定し、arithmetical realization \(f\) によって命題変数を \(T\) の閉じた算術文へ写し、

\[
f_T(\Box A)
=
\mathrm{Pr}_T(\ulcorner f_T(A)\urcorner)
\]

と解釈する。ここで初めて \(\Box\) は「\(T\) で証明可能」を表す。

### C. Kripke semantics

frame \((W,R)\)、valuation \(V\) に対して

\[
w\models\Box A
\quad\Longleftrightarrow\quad
\forall v\,(wRv\Rightarrow v\models A)
\]

と定める。\(wRv\) は modal evaluation の accessibility relation であり、算術的 proof relation そのものではない。

次は別々の主張である。

- **syntactic derivability:** \(\mathrm{GL}\vdash A\)
- **Kripke completeness:** 適切な frame class で \(A\) が valid なら \(\mathrm{GL}\vdash A\)
- **arithmetical completeness:** 全ての適切な provability realizations で算術的に可証なら \(\mathrm{GL}\vdash A\)

# 2. 通常15項目による system anatomy

1. **theorem_or_system_name:** Gödel–Löb provability logic GL

2. **domain:** modal logic・provability logic・proof theory

3. **standard_definition:** 古典命題論理を基礎とし、K axiom、Löb axiom、modus ponens、necessitation を備えた normal propositional modal logic。uniform substitution は axiom schema の運用に含まれる。

4. **assumptions_ABC:**
   - A: classical propositional base
   - B: unary modal operator \(\Box\) を持つ言語
   - C: K axiom \(\Box(A\to B)\to(\Box A\to\Box B)\)
   - D: necessitation rule \(\vdash A\Rightarrow\vdash\Box A\)
   - E: Löb axiom \(\Box(\Box A\to A)\to\Box A\)
   - F: modus ponens と uniform substitution を含む標準 Hilbert-style derivation
   - G: arithmetic interpretation を行う場合にのみ、適切な算術理論 \(T\)、標準 \(\mathrm{Pr}_T\)、arithmetical realizations を固定する
   - H: Kripke interpretation を行う場合にのみ、frame、valuation、forcing relation を固定する

   G・H は pure GL の定義条件ではない。fixed-point theorem も GL の定義公理ではなく、GL から証明される metatheorem である。

5. **hypothesis_levels:**
   - A: ambient。基礎論理
   - B: definitional＋ambient。formula language の型
   - C: object。modal operator に課す normality principle
   - D: object＋definitional。theorem set の生成規則
   - E: object。GL を他の normal modal logics から区別する中心公理
   - F: definitional。導出関係の形成規則
   - G: ambient＋background（arithmetical interpretation side のみ）
   - H: ambient＋background（Kripke semantics side のみ）

6. **condition_types:**
   - A: 古典性
   - B: modal language
   - C: normality・implication preservation
   - D: theoremhood lifting
   - E: Löb principle・reflection constraint
   - F: syntactic derivation closure
   - G: 算術的 provability interpretation
   - H: relational semantics

7. **closure_roles:**
   - A: propositional deductive base
   - B: provability iteration syntax
   - C: internalized implication / normality
   - D: theoremhood lifting
   - E: reflection control / Löb stabilization
   - F: derivational closure
   - G: arithmetic interpretation bridge
   - H: semantic frame realization

   4 に相当する provability iteration は E から導出される。frame-side の transitivity / converse well-foundedness は H の意味論的特徴であり、C–E と同一種類の「仮定」ではない。

8. **conclusion_or_core_principle_P:** GL の中心 principle は

   \[
   \Box(\Box A\to A)\to\Box A.
   \]

   pure modal level では GL-theorem である。arithmetical interpretation の下では「\(T\) が local reflection formula を証明するなら、\(T\) が対象文を証明する」という Löb 構造を内部式として表す。結論 \(\Box A\) は truth ではなく modalized provability である。

9. **blocked_escape_routes:**
   - A: classical propositional equivalence・背理・否定の運用を別基礎論理へ変える自由を固定する
   - B: theoremhood / provability を反復して表せない非 modal 言語へ退く道を塞ぐ
   - C: \(\Box\) が implication と modus ponens を保存しない非 normal operator になる道を塞ぐ
   - D: theorem を modal level へ持ち上げられない道を塞ぐ
   - E: provable local reflection と対象の provability を切り離す K / K4 的自由を塞ぐ
   - F: axiom instances から theorem set を生成する方法を固定する
   - G: arithmetic reading では、\(\Box\) を任意の modality と読む自由を標準 provability predicate へ制限する
   - H: Kripke reading では、modal non-theorem を relational countermodel として表す舞台を与える

10. **what_fails_if_removed:**
   - Aを外すと: intuitionistic provability logic などへ移る。古典 GL の tautology・dualities・frame semanticsをそのまま維持できない。単なる弱化でなく別体系への遷移
   - Bを外すと: K、necessitation、Löb axiom を定式化できず、propositional classical logic に戻る
   - Cを外すと: \(\Box\) が internalized modus ponens を保存する保証を失い、standard arithmetical provability interpretation の共通原理を捉えない non-normal modal setting へ移る
   - Dを外すと: theoremhood を \(\Box\)-level へ持ち上げられない。arithmetical D1 に対応する段階と、arithmetical Löb rule を modal axiomから回収する過程が壊れる
   - Eを外すと: この公理基底から直接残るのは K であって K4 ではない。4 を別に保持すれば K4 となるが、provable reflection が provability を強制する GL 固有の原理は失われる
   - Fを外すと: 同じ axiom list でも theorem set が確定しない。これは反例より system definition の不成立
   - Gを外すと: pure GL と Kripke theory は残るが、「\(\Box\)=\(T\)-provability」という適用と Solovay completeness を語れない
   - Hを外すと: pure syntax と arithmetic interpretation は残るが、frame validity、finite countermodel、decidability route を失う
   - frame の transitivity を外すと: 4 が一般に invalid となり、従って GL soundness が失われる
   - converse well-foundedness を外すと: infinite ascending chain 上で Löb axiom が失敗し得る。例えば \((\mathbb N,<)\) で \(p\) を全点 false とすれば、各点で \(\Box p\) は false、後続点では \(\Box p\to p\) が true なので、\(\Box(\Box p\to p)\) は true だが \(\Box p\) は false
   - irreflexivity を外すと: self-loop \(wRw\) だけの frame で \(p\) を false とすると、同様に Löb axiom が失敗する

11. **what_reappears_if_removed:**
   - A: **R1** — intuitionistic base、Heyting-algebraic semantics、別の provability logic
   - B: **R0** — modal anatomy 自体が定式化不能
   - C: **R1** — non-normal modalities、implication transport の選択自由度
   - D: **R1** — theoremhood lifting を持たない consequence systems
   - E: **R1** — K、または 4 を別に残す K4 の広い frame class と、reflection collapse を欠く modal models
   - F: **R0** — theoremhood relation が未定義
   - G: **R1** — temporal・epistemic・relational など別の \(\Box\)-interpretations
   - H: **R1** — algebraic・arithmetical・proof-theoretic semantics だけを用いる別ルート
   - transitivity / converse well-foundedness / irreflexivity: **R1** — nontransitive frames、infinite ascending chains、reflexive points、対応する countermodels

   いずれも同じ式へ補正項が戻る R2 ではない。system・frame・interpretation の選択域が広がる R1 が中心である。

12. **proof_resources:**
   - representative_route 1: Hilbert calculus
   - resources:
     - substitution instances
     - propositional derivations
     - K
     - necessitation
     - Löb axiom
   - representative_route 2: Kripke completeness
   - resources:
     - finite saturated sets / canonical-style countermodel construction
     - finite transitive irreflexive frames
     - truth lemma
     - finite model property
   - representative_route 3: arithmetical completeness
   - resources:
     - standard proof predicate and derivability conditions
     - finite GL countermodel
     - Solovay function
     - arithmetical realization
   - note: Kripke completeness、Solovay completeness、de Jongh–Sambin fixed-point theorem は GL の定義仮定ではなく、GL について証明される metatheorems とその証明資源である。

13. **closure_style:** modal反射制御型／反復証明可能性型

14. **theorem_vs_system_comment:** GL が固定するのは一つの対象 \(T\) ではなく、formula language、axiom schema、inference rules からなる theorem-generating system である。Kripke frame conditions と arithmetic provability interpretation は、その system の意味論的・算術的 characterization であり、定義公理ではない。これらを混同すると、GL が何を stipulate し、Solovay・Segerberg・de Jongh–Sambin の結果が何を発見したかが見えなくなる。

15. **short_comment:** GL は算術的 Löb 現象を一つの normal modal logic へ圧縮する。圧縮後にも implication preservation、theoremhood lifting、provability iteration、provable reflection の制約が残るが、具体的 proof coding や特定理論の truth は消える。

# 3. Löb axiom 自体の解剖

中心式を再掲する。

\[
\Box(\Box p\to p)\to\Box p.
\]

## 3.1 outer \(\Box\)

outer \(\Box\) は、reflection formula \(\Box p\to p\) が単に成り立つことではなく、それ自体が provable / necessary と modalize されていることを表す。算術的には

\[
\mathrm{Pr}_T\bigl(
\ulcorner
\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\to\varphi
\urcorner
\bigr)
\]

に対応する。

算術的 Löb theorem の前提は、外部メタレベルで

\[
T\vdash\Box_T\varphi\to\varphi
\]

と述べられる。これを object-language formula へ写すのが D1 / modal necessitation に対応し、outer \(\Box\) が現れる。従って outer \(\Box\) は装飾ではなく、theoremhood premise の内部表現である。

\[
(\Box p\to p)\to p
\]

ではこの対応にならず、GL theorem でもない。これは reflection formula の truth を antecedent にした別の、はるかに強い式である。

## 3.2 inner reflection

\[
\Box p\to p
\]

は固定した \(p\) についての local reflection の modal analogue である。arithmetical reading では「\(T\) が \(\varphi\) を証明するなら \(\varphi\)」という object-language formula になる。ただし pure modal syntax だけでは「真」「sound」という意味は付与されていない。

## 3.3 antecedent

\[
\Box(\Box p\to p)
\]

は「reflection が真」ではなく、「reflection formula が \(\Box\)-化されている」を表す。arithmetical interpretation の下でのみ「\(T\) がその reflection instance を証明する」と読む。二重 modal 構造は、provability predicate が自分を含む formula へ再入力されている点にある。

## 3.4 conclusion

\[
\Box p
\]

は pure GL では modal formula、arithmetical interpretation では \(T\)-provability である。\(p\)、semantic truth、standard-model truth は結論されない。

# 4. 算術的 Löb theorem との対応

| 算術側 | modal側 | 注意 |
|---|---|---|
| 算術文 \(\varphi\) | propositional variable / formula \(A\) | arithmetical realization が対応を与える |
| \(\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\) | \(\Box A\) | \(\Box\) は pure syntax では未解釈 |
| \(T\vdash\theta\Rightarrow T\vdash\Box_T\theta\) | necessitation \(\vdash A\Rightarrow\vdash\Box A\) | どちらも theoremhood を modal level へ上げる |
| provability が modus ponens を内部追跡 | K axiom | D2 の modal core |
| \(\Box_T\varphi\to\Box_T\Box_T\varphi\) | 4: \(\Box A\to\Box\Box A\) | GL では Löb axiom から導出 |
| \(T\vdash\Box_T\varphi\to\varphi\Rightarrow T\vdash\varphi\) | Löb rule: \(\vdash\Box A\to A\Rightarrow\vdash A\) | meta-level rule の対応 |
| 内部化された Löb principle | \(\Box(\Box A\to A)\to\Box A\) | GL の中心公理 |

modal Löb axiom から Löb rule を得るには、\(\vdash\Box A\to A\) に necessitation を適用して \(\vdash\Box(\Box A\to A)\) とし、Löb axiom で \(\vdash\Box A\)、元の theorem と modus ponens して \(\vdash A\) とする。

逆に、算術的 soundness では K・necessitation・Löb axiom の各 arithmetical realization が \(T\) または弱い metatheory で証明できることを示す。「同じ記号列だから同じ定理」なのではなく、realization と soundness theorem が橋を与える。

# 5. Solovay arithmetical completeness

## 5.1 採用版

正確さのため、まず Peano arithmetic \(PA\) とその標準 provability predicate を固定する。arithmetical realization \(f\) は各 propositional variable を閉じた算術文へ写し、Boolean connectives を保ち、

\[
f(\Box A)
=
\mathrm{Pr}_{PA}(\ulcorner f(A)\urcorner)
\]

と再帰的に定める。Solovay の定理は

\[
\mathrm{GL}\vdash A
\quad\Longleftrightarrow\quad
\text{全ての arithmetical realizations }f\text{ について }PA\vdash f(A)
\]

と述べる。

より一般には、標準的 presentation と provability predicate を持つ、十分強い \(\Sigma_1\)-sound な計算可能算術理論 \(T\) に対して同型の completeness が成立する。一般化の最弱条件には複数版があるため、本稿の主表示は原典に近い \(PA\) 版へ固定する。

## 5.2 soundness と completeness の分離

- **arithmetical soundness:** \(\mathrm{GL}\vdash A\) なら、全 realizations \(f\) について \(PA\vdash f(A)\)。K は D2、necessitation は D1、Löb axiom は算術的 Löb theorem によって検証される。
- **arithmetical completeness:** \(\mathrm{GL}\nvdash A\) なら、ある realization \(f\) が存在して \(PA\nvdash f(A)\)。有限 Kripke countermodel と Solovay function を用いて、その modal failure を arithmetic へ埋め込む。

この completeness が、「算術の詳細を消しても残る構造」の最も強い検査である。GL は単なる比喩的要約でなく、標準 \(PA\)-provability の全 propositional modal principles をちょうど捉える。ただし coding の全情報を復元するわけではなく、一変数 operator \(\Box\) で表現できる fragment に限る。

# 6. 算術的 Löb からの保存／消去

| 分類 | GL に保存されたもの | GL で消去・抽象化されたもの |
|---|---|---|
| theoremhood | necessitation | \(T\) の具体的 proof sequence |
| implication | K による internalized implication | primitive recursive proof checker の定義 |
| iteration | 導出可能な 4: \(\Box A\to\Box\Box A\) | D3 の算術的検証手順 |
| reflection | Löb axiom / Löb rule | 特定文 \(\varphi\) の算術的内容 |
| fixed point | GL fixed-point theorem | Gödel numbering・substitution function |
| theory | 一般的 provability pattern | \(I\Sigma_1\)、PA、特定の公理提示 |
| semantics | Kripke / algebraic characterization | standard model \(\mathbb N\) の truth |
| metatheory | modal theoremhood と realization theorem | metatheory内の自然数計算の具体形 |

## 6.1 保存された核心

1. theoremhood lifting
2. implication preservation
3. positive introspection / provability iteration
4. provable local reflection が provability を強制する Löb principle
5. modalized formula に対する fixed-point capacity

## 6.2 失われた具体性

1. Gödel numbering と primitive recursive syntax
2. particular proof predicate とその presentation dependence
3. 基礎算術 \(I\Sigma_1\) / \(PA\) の具体的強さ
4. particular sentence \(\varphi\) の数論的内容
5. truth、soundness、standard model に関する情報

# 7. Kripke semantics の解剖

## 7.1 採用する frame class

GL は、有限の transitive irreflexive Kripke frames に関して sound and complete である。treelike frames へさらに制限しても completeness が成り立つ。より一般的な標準表現では、\(R\) が transitive、irreflexive、conversely well-founded、すなわち infinite \(R\)-ascending chain を持たない strict partial order である frames に対して sound であり、finite frames によって completeness を得る。

finite transitive irreflexive frame は自動的に conversely well-founded である。逆に infinite な場合、transitive・irreflexive だけでは converse well-foundedness は従わない。

## 7.2 accessibility relation

\[
wRv
\]

は、world \(w\) から \(v\) が modal evaluation 上 accessible であることを表す。Kripke completeness proof や Solovay embedding では provability pattern をモデル化するが、\(R\) 自体は自然数上の \(\mathrm{Prf}_T(p,x)\) ではなく、world 間の二項関係である。

## 7.3 transitivity

transitive frame では \(wRv\) かつ \(vRu\) なら \(wRu\)。これにより

\[
\Box A\to\Box\Box A
\]

が valid になる。従って frame-side transitivity は modal axiom 4 に対応する。ただし arithmetic D3 の証明と relational transitivity は、soundness / completeness を介して対応する異なる層の記述である。

## 7.4 converse well-foundedness

converse well-foundedness は、任意の非空部分集合に \(R\)-successorを持たない maximal point がある、同値な標準的状況では infinite ascending chain がないことを要求する。Löb axiom の validity proof では、反例があると仮定した領域から maximal counterexample world を選ぶ。この「上へ無限に逃げない」条件が決定的である。

## 7.5 irreflexivity

self-loop \(wRw\) を許すと、\(p\) false の一点 model が Löb axiom の countermodel になる。GL は axiom T

\[
\Box A\to A
\]

を持たず、GL に T を加えると Löb axiom との組合せで体系が trivialize する。従って GL の \(\Box\) を S4 の reflexive necessity や topological interior と同一視できない。

# 8. fixed-point structure の位置

## 8.1 de Jongh–Sambin fixed-point theorem

modal formula \(A(p)\) の \(p\) の全出現が \(\Box\) の scope 内にある、すなわち \(A\) が \(p\) について modalized されているとする。このとき \(p\) を含まない modal formula \(B\) が存在し、

\[
\mathrm{GL}\vdash B\leftrightarrow A(B)
\]

となる。fixed point は GL-provable equivalence の意味で一意であり、effective に構成できる。

## 8.2 arithmetic diagonal lemma との関係

- arithmetic diagonal lemma は syntax code と substitution function を用いて算術文の fixed point を作る。
- GL fixed-point theorem は modalized formula に対し、pure modal methods で fixed point を作る。
- arithmetical realization を施すと、modal fixed point は算術的 fixed-point pattern に対応する。

従って自己参照構造は、特定の Gödel numbering の偶然だけではない。provability operator が満たす GL structure の中にも fixed-point capacity が再構成される。ただしこれは de Jongh–Sambin theorem という既存の精密な結果であり、「再入力」などの独自語彙を必要としない。

## 8.3 Löb axiom との関係

fixed-point theorem は GL の metatheorem であり、Löb axiom と normal modal reasoning を備えた体系の強い definability property を示す。逆に、fixed-point theorem を GL の独立した定義公理として数えてはならない。Löb axiom は fixed-point pattern を theoremhood へ組み込む中心原理であり、fixed-point theorem はその体系内でより一般の modalized equations が解けることを示す。

# 9. \(\Box\) は通常の closure operator か

## 9.1 ordinary closure operator との比較

命題の entailment order \(A\le B\) を \(A\to B\) が valid であることとして比較する。通常の closure operator \(C\) は典型的に次を満たす。

1. extensive: \(A\le C(A)\)
2. monotone
3. idempotent: \(C(C(A))=C(A)\)

GL の \(\Box\) については次のとおりである。

| 性質 | GL の状況 |
|---|---|
| monotonicity | admissible。\(A\to B\) が theorem なら K＋necessitation により \(\Box A\to\Box B\) |
| finite-meet preservation / normality | 成立。normal modal operator |
| \(A\to\Box A\) | 一般に不成立。extensive でない |
| \(\Box A\to\Box\Box A\) | 成立。4 |
| \(\Box\Box A\to\Box A\) | 一般に不成立 |
| idempotence | 不成立 |
| \(\Box A\to A\) | 不成立。T を持たない |

従って \(\Box\) は ordinary closure operator ではない。さらに topological interior operator に必要な \(\Box A\to A\) と idempotence もないため、S4 的 interior operator とも同一でない。

## 9.2 適切な標準構造

代数的には、\(\Box\) は Boolean algebra 上の normal modal operator であり、GL / provability algebra / diagonalizable algebra の Löb 条件を満たす作用素として扱うのが正確である。「閉包」は純粋な比較比喩に留めるべきで、数学的 closure operator という分類は棄却する。

# 10. 三つの仮説の再検査

## 10.1 「自己保証」S2 の再検査

算術的詳細を消しても、

\[
\Box(\Box p\to p)\to\Box p
\]

が GL の中心公理として残る。ここには次の型が保存されている。

1. 対象 \(p\) の modalization \(\Box p\)
2. local reflection analogue \(\Box p\to p\)
3. reflection formula の再 modalization \(\Box(\Box p\to p)\)
4. 結論としての \(\Box p\)

従って「自己保証」という比較ラベルが指していた構造は、特定の \(I\Sigma_1\)、Gödel coding、文 \(\varphi\) にだけ依存するものではない。modal provability structure として残る。

**再判定: S2 — modal level でも reflection structure を横断比較する有効なラベルとして残る。**

ただし technical name は provable local reflection / Löb principle である。「自己保証」は soundness、truth、global reflection を含意しない。GL がすでにこの構造を標準的に切り出しているため、S3 の独自 modal classification には進めない。

## 10.2 「閉包反転」C1 の再検査

GL と近隣体系を比較する。

| logic | 主な公理・frame | Löb pattern |
|---|---|---|
| K | normality、全 Kripke frames | なし |
| K4 | K＋4、transitive frames | provability iteration はあるが Löb axiom はない |
| S4 | K＋T＋4、reflexive transitive frames | \(\Box\) は interior-like。GL とは非両立 |
| GL | K＋Löb、transitive converse-well-founded strict frames | provable reflection \(\Rightarrow\) provability |

この比較により、Löb axiom の有無は再現可能な modal classification difference を与える。しかしその差はすでに K / K4 / S4 / GL、frame correspondence、Löb axiom で完全に表される。また \(\Box\) は ordinary closure operator でないため、「閉包反転」は operator の数学的型を誤認させる危険がある。

**再判定: C1 — 説明比喩としてのみ有効。**

arithmetic details を除いても反転的図式は残るが、図式が残ることと「閉包」が適切な分類名であることは別である。C2・C3には上げない。

## 10.3 「証明デザイン」仮説

通常21定理では、固定された対象条件・ambient 条件・正則性などから一つの結論を導く設計を解剖した。GL では、次の選択が theorem set を組織する。

\[
\text{language}
+\text{axiom schemas}
+\text{inference rules}
+\text{semantics / interpretations}.
\]

これは比喩だけではない。K、necessitation、Löb axiom の選択は syntactic derivability を変え、transitivity・irreflexivity・converse well-foundedness は sound / complete な frame class を特徴づける。ただし axiom と frame condition は同じ層の設計部品ではなく、correspondence theorem を通じて接続される。

**判定: P2 — theorem anatomy から logic anatomy への拡張として比較上有効。**

「どの反復・reflection・countermodel を許すか」を system-level conditions として比較できるため P1 より強い。しかし標準 modal proof theory、algebra、frame correspondence を越える新枠組みではないので P3 ではない。

# 11. Gödel I / Tarski / Löb / GL 四者比較

| 項目 | Gödel I | Tarski | Löb | GL |
|---|---|---|---|---|
| primary object | arithmetic theory \(T\) | truth definition | local reflection instance | modal provability structure |
| key predicate / operator | \(\mathrm{Prov}_T\) | \(\mathrm{Tr}\) | \(\mathrm{Prov}_T\) | \(\Box\) |
| internalization status | proof relation は可能 | full same-language truth は不可能 | proof relation は可能 | abstract operator として公理化 |
| fixed-point role | independence construction | undefinability contradiction | reflection-triggered theoremhood | Löb axiomとmodal fixed-point theorem |
| conclusion type | incompleteness / independence | undefinability | theoremhood implication | modal derivability / validity |
| consistency role | 版に依存し本質的 | semantic版では不要 | 本体では不要 | pure modal systemでは不要 |
| main boundary | theory extension | language / truth hierarchy | stronger reflection theory | frame / modal logic / interpretation boundary |
| truthとの関係 | 外部真理と可証性を区別 | standard-model truth が主対象 | truthを結論しない | pure syntaxでは truth interpretation 未固定 |

## 11.1 具体性が失われ、構造として残るもの

1. Gödel I から Löb / GL へ進むと、特定 independent sentence と consistency assumption は消え、provability iteration と fixed-point pattern が残る。
2. Tarski の semantic truth predicate は GL の \(\Box\) へ移されない。GL は truth abstraction でなく provability abstraction である。
3. arithmetic Löb から GL へ進むと、Gödel coding、proof checker、基礎算術は消え、K・necessitation・Löb principle が残る。
4. Solovay completeness により、残った modal principles は標準算術的 provability の propositional modal fragment を正確に特徴づける。
5. de Jongh–Sambin theorem により、fixed-point capacity も pure modal level で再構成されるが、特定の算術文の内容や standard truth は回復しない。

# 12. residual の位置

## 12.1 候補の分離

- **GLで証明不能な formulas:** syntactic non-theorems
- **finite countermodels:** Kripke completeness により non-theorem を反駁する semantic witnesses
- **frame condition除去後の models:** infinite ascending chains、reflexive points、nontransitive frames
- **stronger / different modal logics:** GL extensions、K、K4、S4、intuitionistic variants
- **arithmetical interpretation dependence:** theory や provability predicate を変えた場合の provability logic

これらは同一種類の対象ではない。non-theorem は formula の status、countermodel は witness、stronger logic は theorem set の変更、interpretation dependence は application-side variation である。「残差」と一括すると区別が失われる。

## 12.2 判定

条件除去の anatomy に限れば **R1 — altered freedom** と記録できる。Löb axiomを外すと K / K4 frames、converse well-foundedness を外すと infinite chains、classical baseを外すと intuitionistic structures が現れるからである。

ただし GL 内部の non-theorem や countermodel を一般に「残差」と呼ぶのは有用でない。R1 は system transition の索引としてのみ使い、modal abstraction level では residual vocabulary の診断価値は低い。R2 はない。

# 13. 研究ログとの比較

| research-log side | GL side | 判定 |
|---|---|---|
| 普遍的認識保証を構想 | propositional modal formula 全体に対する calculus | scope の大きさだけが類似 |
| 証明自身が対象に入る | nested provability \(\Box\Box p\) | self-assessment の限定的類似 |
| 自己保証の一般化で制約 | \(\Box(\Box p\to p)\to\Box p\) | reflection pattern の類似 |
| 主張を縮退 | exact modal theoremhood / countermodel へ限定 | 形式的局所化の類似 |

**類似判定: M1 — self-assessment / reflection の構造的類似。**

研究ログ側に、命題集合、normal modal operator、K、necessitation、Löb axiom、arithmetical realization または Kripke frame に対応する具体的写像はない。従って M2 の modal formalization は未成立であり、M3 は棄却する。

# 14. Erasure Test

「閉包」「閉包反転」「残差」「自己保証」「断絶交渉」を全て削除しても、次で GL の技術的差分は記述できる。

- K と necessitation による normal modal logic
- Löb axiom と導出可能な 4
- finite transitive irreflexive Kripke completeness
- converse well-foundedness による Löb validity
- Solovay arithmetical completeness
- de Jongh–Sambin fixed-point theorem
- local reflection、Löb rule、arithmetical realization

従って数学的内容、予測、countermodel construction、classification は失われない。一方、通常21定理から Gödel・Tarski・Löb・GLへ続く文書群で、「対象条件の anatomy」から「system-level constraints の anatomy」へ移ったことを短く比較する見通しは少し失われる。

**判定: E1 — 教育的・比較的な見通しだけ少し失う。**

E2・E3 は棄却する。独自語彙は標準理論にない構造を発見していない。

# 15. kill criteria

| kill criterion | 検査結果 |
|---|---|
| 1. K＋necessitation＋Löb axiom＋standard semantics で核心を記述できる | **成立** |
| 2. 「閉包」が ordinary closure operator と混同を起こす | **成立。** \(\Box\) は extensive・idempotent でない |
| 3. 「自己保証」が local reflection と theoremhood を曖昧にする | **条件付き成立。** local reflection と併記すれば S2 の比較ラベルとして残せる |
| 4. 「残差」が non-theorem / countermodel / stronger logic を混同する | **成立。** R1 は条件除去時だけに限定 |
| 5. 独自語彙で予測・分類が増える | **不成立。** 標準的 logic / frame classification が優越 |
| 6. Solovay completeness が算術–modal対応を十分与える | **成立** |
| 7. de Jongh–Sambin theorem が fixed-point structure を標準的に抽象化する | **成立** |

negative result は明確である。GL は arithmetic details を消去しても Löb structure が残ることを強く示すが、それは provability logic 自身の成功であって、「閉包」語彙の新理論化を支持しない。

# 16. 最終判定

## A. GL の核心

- GL は classical propositional base＋K＋necessitation＋Löb axiom からなる normal modal logic。
- 中心式は \(\Box(\Box p\to p)\to\Box p\)。
- outer \(\Box\) は reflection の truth でなく、その modalized theoremhood を表す。
- GL は finite transitive irreflexive frames に関して complete。
- Solovay theorem により標準算術的 provability の propositional modal principles を捉える。

## B. arithmetic Löb から保存されたもの

1. theoremhood lifting
2. implication preservation
3. positive introspection
4. provable local reflection \(\Rightarrow\) provability
5. fixed-point compatible structure

## C. arithmetic Löb から消えたもの

1. Gödel numbering の具体形
2. primitive recursive proof relation
3. \(I\Sigma_1\) / PA と公理提示
4. particular sentence \(\varphi\)
5. standard-model truth

## D. 「自己保証」再判定

**S2。** local reflection の modal structure を横断比較するラベルとして残るが、標準用語を置換しない。

## E. 「閉包反転」再判定

**C1。** 反転的形は modal level に残るが、\(\Box\) は closure operator でなく、GL / K4 の標準比較以上の分類力がない。

## F. 「証明デザイン」判定

**P2。** theorem anatomy を、axiom・rule・operator・frame を分ける logic anatomy へ拡張する比較枠として有効。新 proof theory ではない。

## G. residual 判定

**R1（低効用）。** 条件除去後の logic / frame transition には使えるが、non-theorem、countermodel、extension を一括する用途には適用不適。

## H. Erasure Test

**E1。** 独自語彙を消しても数学的内容は失われず、文書群を横断する教育的見通しだけ少し失う。

## I. 研究ログとの類似

**M1。** self-assessment / reflection の構造的類似のみ。modal interpretation の形式写像はない。

## J. 最も重要な新規観察

1. Solovay completeness により、Löb structure は算術的偶然でなく、provability の正確な modal fragment として残る。
2. de Jongh–Sambin theorem により、fixed-point capacity も Gödel coding の具体形を越えて GL 内に再構成される。
3. それでも \(\Box\) は ordinary closure operator ではない。この negative result が「閉包反転」C1を最も強く制限する。

## K. 次の検査候補

1. **de Jongh–Sambin fixed-point theorem:** fixed-point existence・uniqueness・effective construction を単独で解剖し、「再入力」の標準的限界を確定できる。
2. **reflection principles:** local / uniform / global reflection と proof-theoretic strength を分け、S2 と P2 の有効範囲を検査できる。
3. **modal logic K / K4 / S4 comparative anatomy:** operator axiomsとframe propertiesを横並びにし、「閉包」語彙が誤分類を生む地点を最も直接に確認できる。

# 17. 検証資料

- [R. M. Solovay, “Provability Interpretations of Modal Logic” (1976)](https://link.springer.com/article/10.1007/BF02757006) — PA-provability interpretations と arithmetical completeness の原典。
- [Solovay paper: IBM Research record and abstract](https://research.ibm.com/publications/provability-interpretations-of-modal-logic) — realization と \(\Box\)-interpretationの原典要約。
- [S. Artemov and L. Beklemishev, “Provability Logic”](https://sartemov.ws.gc.cuny.edu/files/2012/10/Artemov-Beklemishev.-Provability-logic.pdf) — GL の Hilbert system、Kripke semantics、arithmetical completeness、reflection、provability algebras。
- [G. Sambin, “An Effective Fixed-Point Theorem in Intuitionistic Diagonalizable Algebras” (1976)](https://link.springer.com/article/10.1007/BF02123402) — modal fixed-point theorem の原典。
- [L. Reidhaar-Olson, “A New Proof of the Fixed-Point Theorem of Provability Logic”](https://projecteuclid.org/journals/notre-dame-journal-of-formal-logic/volume-31/issue-1/A-new-proof-of-the-fixed-point-theorem-of-provability/10.1305/ndjfl/1093635331.pdf) — GL fixed-point theorem の semantic proof。
- [M. Maggesi and C. Perini Brogi, “Mechanising Gödel–Löb Provability Logic in HOL Light”](https://link.springer.com/article/10.1007/s10817-023-09677-z) — finite irreflexive transitive frames に対する soundness / completeness の形式検証。

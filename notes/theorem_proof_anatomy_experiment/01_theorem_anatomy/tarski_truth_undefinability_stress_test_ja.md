# Tarski 真理定義不可能性定理：証明の解剖 special stress test

## 0. 目的と参照枠

本稿は、theorem_proof_anatomy_v1.1_ja.md と godel_incompleteness_closure_reversal_stress_test_ja.md の分析枠を継承し、Tarski の真理定義不可能性定理を stress test する。

「逃走経路」「閉じ方」「封鎖」「残差」「閉包」「閉包反転」「内部化」「断絶交渉」は比較用のメタ記述であり、標準数理論理学用語ではない。標準的な object language / metalanguage、definability、truth、satisfaction、diagonalization、semantic hierarchy の区別を優先する。

維持する検査原則は次である。

1. theorem assumptions と proof resources を分ける。
2. object / ambient / background / definitional を分ける。
3. 条件除去後を R0 / R1 / R2 で記録する。
4. syntactic provability、semantic truth、standard-model truth を混同しない。
5. object language と metalanguage の位置を常に明示する。
6. formal diagonal sentence と自然言語の liar paradox を同一視しない。
7. 標準語彙の方が精密なら標準語彙を優先する。

# 1. 採用版の固定

## 1.1 主分析：算術・標準モデル版

主分析では次の **semantic arithmetic version** を採用する。

> \(L_A=\{0,S,+,\times,<,\ldots\}\) を、構文の Gödel coding と diagonalization を扱える一階算術言語とし、\(\mathbb N\) をその標準自然数構造とする。真なる \(L_A\)-文の Gödel code の集合
>
> \[
> \mathrm{Th}(\mathbb N)
> =\{\ulcorner\varphi\urcorner\mid
> \varphi\text{ は }L_A\text{-sentence かつ }\mathbb N\models\varphi\}
> \]
>
> は \(\mathbb N\) において算術的に定義できない。すなわち、全ての \(L_A\)-文 \(\varphi\) について
>
> \[
> \mathbb N\models
> \mathrm{Tr}(\ulcorner\varphi\urcorner)
> \leftrightarrow\varphi
> \]
>
> を満たす \(L_A\)-式 \(\mathrm{Tr}(x)\) は存在しない。

ここでの結論は **undefinability in \(\mathbb N\)** である。特定理論における unprovability や undecidability を直接述べてはいない。「真理は存在しない」「真理は常に言語外にある」という一般哲学命題でもない。

## 1.2 nearby formulation：内部 T-schema 版

十分強い整合的算術理論 \(T\) と、その同じ算術言語内の式 \(\mathrm{Tr}(x)\) を考える。全ての算術文 \(\varphi\) に対して

\[
T\vdash
\mathrm{Tr}(\ulcorner\varphi\urcorner)\leftrightarrow\varphi
\]

を要求すると、diagonal lemma により \(T\vdash L\leftrightarrow\neg\mathrm{Tr}(\ulcorner L\urcorner)\) となる文 \(L\) が得られ、両 biconditional から矛盾する。従って、整合的な十分強い \(T\) は、同じ言語内の一つの式について全ての算術文の T-biconditionals を証明できない。

これは主分析の semantic definability 版と近いが同一ではない。

- 主分析: \(\mathbb N\) における真理集合が算術式で定義できるか。
- nearby formulation: 理論 \(T\) が全 T-biconditionals を証明できるか。
- 前者には理論 \(T\) の整合性仮定は要らない。
- 後者は syntactic derivability と整合性を扱う。

## 1.3 適用範囲

Tarski が禁止するのは、十分表現力のある言語についての **自己適用可能な、同一言語内の、全ての文を正しく扱う完全な真理定義**である。次は区別される。

- **truth in \(\mathbb N\):** 標準自然数構造における閉じた算術文の真偽。
- **satisfaction relation:** 自由変数を持つ式と assignment の関係。sentence truth は satisfaction の特別な場合。
- **internal truth predicate:** object language 自身の式として置かれる候補 \(\mathrm{Tr}(x)\)。
- **external truth definition:** metalanguage、例えば set theory から \(L_A\) の satisfaction を再帰的に定義するもの。
- **partial truth predicate:** \(\Delta_0,\Sigma_n,\Pi_n\) など限定された formula class だけを正しく扱う述語。
- **expanded language:** 新記号 \(\mathrm{Tr}_0\) を加え、元の \(L_0\)-文だけを評価させる言語。
- **typed hierarchy:** \(\mathrm{Tr}_i\) が自分より低い言語レベルだけに適用される階層。
- **nonclassical / partial theory:** truth-value gap などを許し、全自己適用文への classical bivalent T-schema を要求しない理論。

「真理は定義できない」という無限定な要約は、これらの可能性を消してしまうため採用しない。

# 2. 通常15項目＋special stress-test

1. **theorem_name:** Tarski の算術的真理定義不可能性定理

2. **domain:** 数理論理・モデル理論・形式意味論

3. **standard_statement:** 一階算術言語 \(L_A\) と標準構造 \(\mathbb N\) に対し、真なる \(L_A\)-文の Gödel code 集合 \(\mathrm{Th}(\mathbb N)\) は \(L_A\)-式によって \(\mathbb N\) 内で定義できない。すなわち、全ての算術文 \(\varphi\) について \(\mathbb N\models\mathrm{Tr}(\ulcorner\varphi\urcorner)\leftrightarrow\varphi\) を満たす算術式 \(\mathrm{Tr}(x)\) は存在しない。

4. **assumptions_ABC:**
   - A: object language \(L_A\) が一階算術を表し、diagonal coding に十分な表現力を持つ
   - B: \(L_A\) の syntax に固定された有効な Gödel coding があり、substitution などの構文操作を算術的に扱える
   - C: truth predicate 候補 \(\mathrm{Tr}(x)\) が同じ object language \(L_A\) の算術式である
   - D: \(\mathrm{Tr}\) に、全ての \(L_A\)-文について標準モデル上で正しい T-biconditional を要求する
   - E: \(\mathbb N\) に通常の classical bivalent semantics を与える
   - F: metalanguage / metatheory から \(\mathbb N\)、syntax coding、satisfaction を扱う

5. **hypothesis_levels:**
   - A: ambient（言語と表現力の舞台）
   - B: definitional＋background（syntax と number を結ぶ固定 coding。独立した semantic truth 仮定ではない）
   - C: object＋ambient（候補式という対象条件と same-language 条件）
   - D: definitional（何を「完全な真理定義」と呼ぶかを固定する adequacy target）
   - E: ambient＋background（採用する意味論）
   - F: background（定理を述べ、\(\mathbb N\models\varphi\) を評価する外部層）

6. **condition_types:**
   - A: 算術的表現力
   - B: 構文符号化
   - C: 同一言語内定義
   - D: 全域性・material adequacy
   - E: 古典意味論・二値性
   - F: メタ意味論的背景

7. **closure_roles:**
   - A: expressive strength / semantic self-representation capacity
   - B: syntax coding / self-application bridge
   - C: same-language closure
   - D: truth-totality requirement / partiality suppression
   - E: classical contradiction recognition
   - F: meta/object distinction / external satisfaction

   self-application enablement は単一条件ではない。A・Bにより formula code と substitution を扱い、C・Dにより同じ言語の全 sentence へ truth candidate を適用し、proof resource である diagonal lemma を使って初めて固定点が得られる。

8. **conclusion_P:** \(\mathrm{Th}(\mathbb N)\) は arithmetically definable でない。従って完全な算術的 truth predicate \(\mathrm{Tr}(x)\) は同じ算術言語内に存在しない。これは特定文の unprovability、理論の incompleteness、または truth set の単なる non-recursiveness と同義ではない。後二者と関係はあるが、結論の型は **semantic set の non-arithmetical definability** である。

9. **blocked_escape_routes:**
   - A: 言語が自分の syntax を数として扱えないほど弱い、という適用外への道を塞ぐ
   - B: truth candidate を自分自身の sentence code へ適用できないよう coding を欠かせる道を塞ぐ
   - C: truth definition をより強い metalanguage または別 sort へ移す道を塞ぐ
   - D: \(\Sigma_n\) だけ、あるいは truth-free sentences だけを扱う partial predicate へ制限する道を塞ぐ
   - E: liar-like fixed point に truth-value gap や paraconsistent value を与える道を塞ぐ
   - F: object language の truth と、外部で用いる satisfaction relation を無区別にすることを防ぐ

10. **what_fails_if_removed:**
   - Aを外すと: diagonalization に十分でない弱い言語にはこの定理は適用できない。decidable な弱い言語や有限的言語の truth は外部で定義可能だが、それだけで同一言語内 truth predicate が必ず得られるとは限らない
   - Bを外すと: 「文の code に truth predicate を適用する」という定理文自体が定式化できない。これは反例というより枠組みの喪失
   - Cを外すと: set theory などのより強い metalanguage から、固定された object language \(L_A\) と構造 \(\mathbb N\) の satisfaction / truth を再帰的に定義できる。これは Tarski への反例でなく適用範囲外への移動
   - Dを外すと: 各固定 \(n\) について \(\Sigma_n\)・\(\Pi_n\) formula class の partial truth predicates を算術的に構成できる。全 complexity level を一つで覆わないため矛盾しない
   - Eを外すと: Kripke 型 fixed-point theory のように truth-value gap を許し、grounded sentences に部分的 truth predicate を与える方法がある。classical total T-schema を維持した反例ではない
   - Fを外すと: \(\mathbb N\models\varphi\) を評価する場所が消え、semantic theorem を述べる枠組みが失われる
   - standard model を nonstandard model \(M\models\mathrm{PA}\) に替えると: 同一言語内で \(M\) 自身の全真理を definable にすることは一般に Tarski の障害を免れない。一方、適切な nonstandard model は、外部集合としての非定義的 full satisfaction class を持つ expansion を許すことがある。これは definability から expansion existence への別問題である

11. **what_reappears_if_removed:**
   - A: **R1** — 弱い表現力と decidability、または外部からの truth evaluation が可能になる場合がある
   - B: **R0** — syntax-to-number bridge がなくなり、自然な補正項より先に定式化が失われる
   - C: **R1** — metalanguage と semantic hierarchy が現れる
   - D: **R1** — complexity-bounded partial truth predicates と satisfaction predicates が現れる
   - E: **R1** — partial valuation、truth-value gap、非古典的 fixed point が現れる
   - F: **R0** — semantic evaluation の背景自体が失われる
   - standard model の変更: **R1** — nonstandard syntax codes、external satisfaction classes、model-dependent expansion が現れる

   R2 は確認されない。truth definition が同じ式の追加項として戻るのではなく、言語レベル、formula complexity、valuation regime、model expansion の変更として再配置される。

12. **proof_resources:**
   - representative_route: semantic diagonal lemma による背理法
   - resources:
     - Gödel numbering と syntax coding
     - substitution / diagonal function の算術的表現
     - semantic diagonal lemma
     - truth candidate \(\mathrm{Tr}(x)\) の全域的 adequacy
     - liar-like fixed-point sentence

       \[
       \mathbb N\models
       L\leftrightarrow\neg\mathrm{Tr}(\ulcorner L\urcorner)
       \]

     - 仮定された truth biconditional

       \[
       \mathbb N\models
       \mathrm{Tr}(\ulcorner L\urcorner)\leftrightarrow L
       \]

     - classical negationによる contradiction
   - note: diagonal lemma は proof resource であり、「言語が自己言及文を公理として持つ」という仮定ではない。自然言語 liar と違い、固定 coding、形式的 substitution、同一言語内 truth candidate、全域 T-biconditional が揃って初めて矛盾が構成される。

13. **closure_style:** 同一言語真理定義限界型／意味論的内部化限界型

14. **theorem_vs_proof_comment:** 定理が固定するのは、算術言語、標準モデル、same-language の候補式、全 sentence に対する truth adequacy である。証明は syntax coding と semantic diagonal lemma により、その候補を自分自身の code へ適用する文を構成する。diagonalization を定理の仮定へ昇格させると、表現力・coding・全域性の組が fixed point を可能にするという役割分担が見えなくなる。

15. **short_comment:** Tarski の定理は truth 一般を外部へ追放する定理ではない。固定された十分強い object language が、自分の全 sentence の standard truth を、同じ言語の一式で完全に定義することを禁じる。

16. **closure_target:** \(L_A\) の全算術文についての semantic truth を、一つの \(L_A\)-式 \(\mathrm{Tr}(x)\) によって同じ object language の内部で全域的に記述すること。対象は **total same-language truth definition for arithmetic sentences** であって、真理一般、全構造の satisfaction、認識の正当性ではない。

17. **self_reference_mechanism:**
   1. metalanguage で \(L_A\)-syntax を自然数へ coding する。
   2. same-language truth candidate \(\mathrm{Tr}(x)\) を仮定する。
   3. diagonal lemma により \(L\leftrightarrow\neg\mathrm{Tr}(\ulcorner L\urcorner)\) を満たす object-language sentence \(L\) を作る。
   4. \(\mathrm{Tr}\) を \(\ulcorner L\urcorner\) へ適用する。
   5. 全域 T-biconditional と組み合わせて \(\mathbb N\models L\leftrightarrow\neg L\) を得る。

   Gödel 第1では内部化される関係は finite proof / provability であり、構成文から unprovability / independence を得る。Tarski では内部化候補が semantic truth であり、完全な truth definition の存在仮定そのものが contradiction する。この違いは本質的である。

18. **meta_level_transition:**
   - metalanguage: \(L_A\)、\(\mathbb N\)、syntax code、satisfaction を定める
   - object language: \(\mathrm{Tr}(x)\) 候補と diagonal sentence \(L\) を構成する
   - metalanguage: \(\mathbb N\models L\leftrightarrow\neg\mathrm{Tr}(\ulcorner L\urcorner)\) と truth adequacy を照合して contradiction を認識する

   truth predicate を object language に戻そうとしても、metalanguage は消えない。coding の正しさ、standard model の解釈、T-biconditional の成立を評価する外部意味論が証明全体に残る。

19. **residual_location:** 「真理そのもの」が外に残るとは判定しない。再配置されるのは **truth-definition の言語レベルと適用範囲**である。全 \(L_0\)-truth はより強い metalanguage \(L_1\) から定義でき、固定 complexity class には partial truth predicate を置ける。しかし \(L_1\) 自身の全 truth を同じ \(\mathrm{Tr}_0\) が覆うわけではない。従って位置は **metalanguage / partial hierarchy / language-extension dependent boundary** である。

20. **hierarchy_generation:** Tarski 型の解決は典型的に

\[
L_0
\longrightarrow
L_1=L_0+\mathrm{Tr}_0
\longrightarrow
L_2=L_1+\mathrm{Tr}_1
\longrightarrow\cdots
\]

という typed hierarchy を誘導する。各 \(\mathrm{Tr}_i\) は原則として自分より低い level の truth だけを扱い、自分自身を含む全 sentence へ無制限に適用しない。ただし hierarchy は唯一の対応ではない。

- complexity-bounded partial truth predicates
- axiomatic compositional truth theories
- Kripke fixed-point semantics と truth-value gaps
- revision theory
- paraconsistent / nonclassical truth theories
- nonstandard models の external satisfaction classes

これらは、classical・total・same-language・fully self-applicable T-schema のどれかを弱める。従って「無限階層しか解決法がない」とは結論しない。

# 3. Gödel 第1との直接比較

| 項目 | Gödel 第1 | Tarski |
|---|---|---|
| internalized relation | finite proof / provability | standard-model truth の候補 |
| target | effective theory の syntactic completeness | arithmetic truth set の same-language definability |
| coding target | syntax と proof sequence | syntax と truth predicate application |
| fixed-point role | \(T\) に相対的な independent sentence | truth candidate と衝突する liar-like sentence |
| conclusion type | unprovability / independence | undefinability |
| main consistency role | Rosser 版では両側の非証明可能性に必要 | 主分析の semantic arithmetic 版には不要 |
| meta-level remainder | proof code と independence judgment | \(\mathbb N\)-truth と satisfaction definition |
| moving boundary | theory extension \(T\mapsto T'\) | language / truth-level extension \(L_i\mapsto L_{i+1}\) |
| standard vocabulary | arithmetization、diagonalization、incompleteness | diagonalization、undefinability、semantic hierarchy |

## 3.1 「証明の内部化」と「真理の内部化」

proof relation は有限列の効果的検査に基づくため、計算可能に公理化された \(T\) について \(\mathrm{Prf}_T(p,x)\) を primitive recursive または適切な arithmetical relation として表現できる。provability predicate は内部化できるが、その述語は truth predicate ではなく、soundness を自動的に保証しない。

これに対し \(\mathrm{Th}(\mathbb N)\) は、全算術文の semantic truth を集めた集合であり、同じ算術言語で定義できない。従って次の要約には限定的な妥当性がある。

- Gödel: **definable provability relation を内部へ戻したうえで、その決定能力の限界を示す。**
- Tarski: **全域的 semantic truth relation を同じ言語へ戻す定義そのものを禁じる。**

しかし「Gödel は証明の閉包限界、Tarski は真理の閉包限界」という要約だけでは、definability と provability、semantic theorem と syntactic theorem、consistency 仮定の有無が失われる。比較見出しとしては使えても、技術記述には不十分である。

## 3.2 共通点と非同一性

共通する核は syntax coding と diagonal fixed point である。だが fixed point が作用する predicate の型が違う。

- \(\mathrm{Prov}_T\) は「\(T\) に有限証明がある」という syntactic predicate。
- \(\mathrm{Tr}\) は「\(\mathbb N\) で真である」という semantic predicate 候補。

Gödel 文は contradiction を直接生成せず、整合性条件のもとで independence を生む。Tarski の truth candidate は全域的 T-schema と fixed point を同時に満たすと classical contradiction を直接生む。この差は「どちらも自己参照」で潰してはならない。

# 4. Gödel 第2との比較

## 4.1 provability predicate と truth predicate

第2不完全性定理では、標準 \(\Sigma_1\) provability predicate \(\mathrm{Pr}_T(x)\) を \(T\) 内部に定義し、Hilbert–Bernays–Löb 条件を通じて provability の反復を扱う。これは可能である。制約は、整合的な \(T\) が特定の internal reflection 文

\[
\mathrm{Con}(T)=\neg\mathrm{Pr}_T(\ulcorner0=1\urcorner)
\]

を証明できないことである。

Tarski では、全算術文に対し

\[
\mathrm{Tr}(\ulcorner\varphi\urcorner)\leftrightarrow\varphi
\]

を正しく満たす same-language predicate 自体が存在しない。provability は内部定義可能だが完全・sound な truth surrogate ではなく、truth は全域的・同一言語的・自己適用可能な形では内部定義不能である、と限定すれば比較は正しい。

## 4.2 reflection の違い

- Gödel 第2 / Löb: \(\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\to\varphi\) という内部 reflection の可証性に制約がある。
- Tarski: \(\mathrm{Tr}(\ulcorner\varphi\urcorner)\leftrightarrow\varphi\) という全域 semantic disquotation を同じ言語で与える定義に制約がある。

前者は特定の theory-relative proof predicate に関する derivability limit、後者は standard-model truth set の definability limit である。moving reflection boundary と truth hierarchy は似た「再添字化」を示すが、同じ定理機構ではない。

# 5. 既存21定理との比較

## 5.1 Stokes / Gauss–Bonnet

Stokes の無限遠境界項、Gauss–Bonnet の境界測地曲率項は R2 である。条件を緩めた一般式の中へ、積分可能な明示項として戻る。

Tarski の metalanguage、partial truth predicate、typed hierarchy はその種の補正項ではない。

- 同じ等式へ足されない。
- 一つの値として会計できない。
- 言語、式クラス、意味論の regime を変更する。
- 上位 truth predicate は下位言語の truth を扱うが、自分自身の全 truth まで同時に閉じない。

従って両者の類似は「条件除去後に未処理成分が見える」という最も粗いレベルだけであり、R2 的同種性は棄却する。

## 5.2 一階述語論理のコンパクト性定理

compactness は、全ての有限部分が satisfiable なら理論全体に model があるという **semantic model existence** の定理である。Tarski は、特定の standard model \(\mathbb N\) についての全 sentence truth set が object language で definable かという **semantic definability** の定理である。

外部 metalanguage で satisfaction を扱うことは compactness の標準的意味論にも必要である。しかし、モデルの存在を外部から述べられることと、そのモデルの truth set をモデル自身の言語内で定義できることは別問題である。compactness は Tarski の boundary を埋めず、Tarski も compactness の model existence を否定しない。

## 5.3 代数学の基本定理

複素数体への ambient extension が実多項式の根を収容することと、metalanguage extension が object-language truth を定義することには、ごく限定的な比較しかない。

- 根は拡大体の元として固定され、複素数体は自分自身の多項式についても代数的に閉じている。
- truth language extension は下位言語の truth を扱えるが、拡張言語自身の全 truth に対して同じ役割を完了しない。

従って「外へ逃げた対象を ambient extension が収容する」という表面的類似はあるが、FTA の algebraic closure と Tarski hierarchy を同じ closure class に置くことは棄却する。

# 6. 研究ログとの比較

## 6.1 対応候補

| research-log side | Tarski side | 判定 |
|---|---|---|
| 「全認識道具」を対象にしようとした | 全算術文の truth predicate を同一言語に置く | 全域評価を対象化するという限定的類似 |
| 証明自身まで射程に入れると自己適用問題が現れた | syntax coding と diagonal sentence | self-application の一般形だけが類似 |
| 背景を内部化すると新たな背景が必要に見えた | \(L_0\)-truth を \(L_1\) で定義し、\(L_1\)-truth にはさらに上位層が必要 | object/meta level の再設定に構造的類似 |
| 普遍主張を縮退させ局所比較へ降りた | full truth から \(\Sigma_n\)-truth、typed truth、grounded truth へ制限 | 適用範囲を限定して構成可能性を回復する点が類似 |

## 6.2 欠けている形式対応

研究ログ側には、少なくとも次がまだない。

- 「認識道具」を表す形式言語とその syntax code
- truth predicate に対応する明示的 unary formula
- 全対象についての T-schema に対応する adequacy condition
- substitution / diagonal function
- fixed-point sentence と contradiction derivation
- object level と metalanguage level の形式的モデル

従って「背景を内部化すると新たな背景が必要」という読みは構造的連想に留まる。Tarski 型の theorem transfer ではない。

## 6.3 類似判定

**T1 — structural analogy**

評価装置を同一レベルへ全域的に内部化しようとすると、適用範囲またはメタ層を再設定する必要がある、という限定的類似はある。しかし研究ログ側に truth-predicate、coding、diagonalization の具体的対応がないため T2 には進めない。T3 は棄却する。

# 7. 「断絶交渉」仮説

## 7.1 比較上見えるもの

Tarski の定理は、object language が扱う算術対象と、metalanguage が与える semantic evaluation の境界を完全には同一平面化できない例として読める。truth definition を object language へ戻す範囲は、次の選択で変わる。

- 下位言語だけを評価する
- formula complexity を限定する
- truth-value gap を許す
- truth predicate の自己適用を型で制限する
- 外部 satisfaction class を expansion として加える

この意味で「どこまで内部で扱い、どこからを外部・上位・部分へ置くかを交渉する」という説明は、各 truth theory の設計差を俯瞰する補助線にはなる。

## 7.2 標準語彙に対する限界

しかし「断絶交渉」は、次の標準区別より粗い。

- definability と axiomatizability
- object language と metalanguage
- full truth と partial truth
- typed と untyped
- classical total valuation と partial / nonclassical valuation
- definable predicate と external satisfaction class

また Tarski は「断絶が存在論的に必要」と証明するのではなく、特定条件を同時に満たす truth definition の不可能性を示す。従って「背景は必ず外にある」という一般命題へ拡張できない。

## 7.3 判定

**D1 — 説明比喩としてのみ有効**

object / meta 境界、適用範囲、truth theory の設計選択を並べる見出しとしては働く。しかし diagonalization、undefinability、semantic hierarchy 以上の予測や形式分類を与えないため D2・D3 には上げない。

# 8. 「残差」仮説

truth predicate の same-language total definition が不可能でも、次は可能である。

- metalanguage における下位 object-language truth definition
- fixed complexity class の partial truth predicate
- typed truth hierarchy
- expanded nonstandard model の external satisfaction class
- partial / nonclassical fixed-point semantics

ここで観察されるのは truth の存在論的保存ではなく、**truth-definition の位置・適用範囲・semantic regime の変更**である。

判定は **R1 — altered freedom** とする。R0 ではないのは、条件緩和後に複数の明確な代替構造が現れるためである。R2 ではないのは、それらが同じ式に戻る明示的補正項ではないためである。

# 9. hierarchy_generation の評価

Tarski hierarchy は moving boundary の明瞭な例である。\(L_{i+1}\) は \(L_i\) の truth を扱えるが、\(L_{i+1}\) 自身の全 truth をその同じ truth predicate が扱うわけではない。

ただし、これは「真理が無限に逃げる」という存在論的記述ではない。各 level で定義対象の language class が変わっている。また Kripke 型 fixed point は level hierarchy 以外の対応を示すが、classical totality の代わりに partiality を導入する。従って一般パターンは「必ず上位へ移動」ではなく、**same-language / total / classical / self-applicable の同時要求をどこかで緩める**ことである。

# 10. kill criteria

| kill criterion | 検査結果 |
|---|---|
| 1. diagonalization / undefinability / semantic hierarchy で十分明確 | **成立。** 標準機構の技術記述に追加語彙は不要 |
| 2. closure が object language / metalanguage の差を曖昧にする | **部分成立。** closure target を限定しない用法は危険 |
| 3. residual が truth / satisfaction / hierarchy の区別を失わせる | **成立。** residual 単独では definability と external class を区別できない |
| 4. hierarchy を残差移送と呼んでも追加予測がない | **成立。** 比較要約以上の予測は得られない |
| 5. 研究ログとの対応が self-reference 以上にない | **部分不成立。** object/meta 再設定という G1/T1 レベルの類似はあるが形式写像はない |

negative result は、今回の語彙が Tarski の発見機構を説明するのではなく、標準分析後の配置図にしかならないことである。

# 11. 最終判定

## A. Tarski 定理の解剖

- \(\mathrm{Th}(\mathbb N)\) は同じ一階算術言語の式では定義できない。
- 条件は十分な算術表現力、syntax coding、same-language candidate、全 sentence の truth adequacy、classical semantics である。
- diagonal lemma が liar-like fixed point を構成し、全域 T-biconditional と衝突する。
- 結論は undefinability であり、特定文の unprovability や真理一般の外在性ではない。
- metalanguage、partial truth、typed / nonclassical truth theory は禁止されない。

## B. Gödel 第1との最大の違い

1. Gödel は definable proof predicate から independence を得るが、Tarski は total truth predicate の definability 自体を否定する。
2. Rosser 第1では consistency が必要だが、Tarski の semantic arithmetic 版には theory consistency 仮定がない。
3. Gödel の限界は theory-relative、Tarski の限界は language / standard-model definability-relative である。

## C. Gödel 第2との最大の違い

1. \(\mathrm{Pr}_T\) は内部定義可能だが、\(\mathrm{Tr}\) は full same-language predicate として定義不能。
2. 第2は \(\mathrm{Con}(T)\) という特定 reflection 文の非可証性、Tarski は全 T-biconditionals を支える predicate の不存在。
3. moving reflection boundary と truth hierarchy は類似するが、derivability limit と semantic definability limit は別である。

## D. residual 判定

**R1 — altered freedom。** metalanguage、partial truth、typed hierarchy、partial / nonclassical semantics へ truth-definition の位置と範囲が変わる。R2 ではない。

## E. 「断絶交渉」判定

**D1 — 説明比喩としてのみ有効。** object/meta 境界の設計選択を並べる補助線にはなるが、標準語彙以上の分類能力は確認できない。

## F. 研究ログとの類似

**T1 — structural analogy。** 背景的評価装置を内部化すると適用範囲またはメタ層の再設定が必要になる、という限定的類似はある。形式的写像はない。

## G. 次の検査として Löb に進む価値

**high**

Löb の定理は、truth ではなく provability に対する internal reflection \(\mathrm{Prov}(\ulcorner\varphi\urcorner)\to\varphi\) の条件を精密化する。Tarski の semantic disquotation と Gödel 第2の reflection の差を、標準 proof-theoretic 語彙で直接比較できる。

# 12. 検証資料

- [Tarski, “The Concept of Truth in Formalized Languages”](https://authortomharper.com/wp-content/uploads/2022/04/1935-The-Concept-of-Truth-in-Formalized-Languages-Tarski.pdf) — object language / metalanguage、material adequacy、形式言語の真理定義という原典的枠組み。
- [Salehi, “Tarski’s Undefinability Theorem and the Diagonal Lemma”](https://arxiv.org/pdf/2009.00315) — semantic Tarski theorem と semantic diagonal lemma、syntactic nearby formulation の区別。
- [Serény, “The Diagonal Lemma as the Formalized Grelling Paradox”](https://arxiv.org/pdf/math/0606425) — arithmetic の self-reference capacity と diagonal lemma の形式的役割。
- [Kripke, “Outline of a Theory of Truth”](https://www.impan.pl/~kz/truthseminar/Kripke_Outline.pdf) — truth-value gaps と fixed-point truth による非階層的・部分的対応。
- [Kotlarski, “Full Satisfaction Classes: A Survey”](https://projecteuclid.org/journals/notre-dame-journal-of-formal-logic/volume-32/issue-4/Full-satisfaction-classes-a-survey/10.1305/ndjfl/1093635929.pdf) — nonstandard models と外部 satisfaction classes。

# Theory-strength order structures
## interpretability・conservativity・deductive inclusion・consistency・reflection・ordinal comparison の special stress test

本稿でいう「multiple order」「order bundle」「strength profile」「proof architecture」「canonicalization」「moving boundary」「residual」は比較用の解剖的メタ記述であり、標準 proof theory / interpretability theory / model theory の用語ではない。技術記述では theorem inclusion、conservative extension、relative interpretability、bi-interpretability、relative consistency、reflection ordering、proof-theoretic reducibility、ordinal analysis を優先する。

中心結論を先に述べる。**“\(T\) is stronger than \(U\)” は relation を指定しない限り、数学的主張として著しく不完全である。** Theory strength は一つの全順序ではなく、対象言語・formula class・translation notion・metatheory に相対する複数の preorders、strict orders、equivalence relations、quotient orders が部分的に整列した構造である。

## 0. Relation の固定

以下では「右側の \(T\) が左側の \(U\) 以上に強い」という向きに可能な限り揃える。ただし conservativity は extension に対する**非増加条件**であり、consistency/reflection の自己証明型 relation は strict で、同じ型へ無理に揃えない。

### 0.1 Deductive inclusion

同じ言語 \(L\)、または明示された言語埋込みの下で

\[
U\le_{\mathrm{Th}}T
\quad:\Longleftrightarrow\quad
\operatorname{Th}_L(U)\subseteq\operatorname{Th}_L(T).
\]

これは theorem set の包含であり、axiom presentation の包含ではない。

### 0.2 Axiomatic extension

共通の ambient signature を固定して

\[
U\subseteq_{\mathrm{ax}}T
\]

を公理集合の literal inclusion とする。冗長公理を加えただけでも strict inclusion になり得るため、deductive strength より presentation-sensitive である。

### 0.3 Conservative extension

\(T\) が \(U\) の extension であり、すべての \(U\)-language sentence \(\varphi\) について

\[
T\vdash\varphi\Longrightarrow U\vdash\varphi
\]

なら full conservative extension とする。Formula class \(\Gamma\) に制限した場合は

\[
T\vdash\varphi, \varphi\in\Gamma
\Longrightarrow U\vdash\varphi
\]

を \(\Gamma\)-conservativity とする。これは「\(T\) が \(U\) より強い」という order ではなく、**extension が旧言語／指定 class で新定理を増やさない**という relation である。

別に、

\[
U\le_\Gamma T
\quad:\Longleftrightarrow\quad
\operatorname{Th}_\Gamma(U)
\subseteq
\operatorname{Th}_\Gamma(T)
\]

を \(\Gamma\)-consequence strength preorder と呼ぶ。\(T\) が \(U\) の \(\Gamma\)-conservative extension なら、両理論の \(\Gamma\)-theories は等しい。

### 0.4 Interpretability

\[
T\triangleright U
\]

は、\(U\) の language を \(T\) の formulas へ写す relative interpretation \(k=(\delta,F)\) が存在し、\(T\) が各 translated \(U\)-axiom を証明することを意味する。量化は domain formula \(\delta\) へ relativize され、equality も definable equivalence relation として解釈され得る。本稿の主設定では finite relational signatures、one-dimensional、parameter-free relative interpretations を基準とし、多次元・parameter interpretations は別 variant として明記する。[Joosten](https://arxiv.org/abs/1602.00555)

### 0.5 Mutual interpretability

\[
T\triangleright U
\quad\text{and}\quad
U\triangleright T.
\]

Interpretability preorder が両向きに成立することをいう。合成した interpretations が元の対象を回復するとは要求しない。

### 0.6 Bi-interpretability

両向き interpretations に加え、その合成が各 theory 内で definable isomorphism により identity interpretation と同型になることを要求する。Mutual interpretability より強い equivalence notion である。[Visser–Friedman](https://www.cambridge.org/core/journals/review-of-symbolic-logic/article/when-biinterpretability-implies-synonymy/00B8CAF9978904070D017C303308F414)

### 0.7 Consistency strength

二つの型を分ける。

1. **internal certification / strict relation**
   \[
   U<_{\mathrm{Con}}T
   \quad:\Longleftrightarrow\quad
   T\vdash\mathrm{Con}(U).
   \]
   Consistent c.e. \(T\) について \(T<_{\mathrm{Con}}T\) は Gödel II により失敗するため、これは reflexive preorder ではない。
2. **relative-consistency preorder over \(B\)**
   \[
   U\le^{B}_{\mathrm{rCon}}T
   \quad:\Longleftrightarrow\quad
   B\vdash\mathrm{Con}(T)\to\mathrm{Con}(U).
   \]
   固定 formalizations の下では reflexive・transitive で、equiconsistency による quotient が自然である。

両者を「consistency strength」と一語で交換しない。

### 0.8 Reflection strength

Formula class \(\Gamma\) と local/uniform/global scope を固定し、strict form を

\[
U<_\Gamma^{\mathrm{RFN}}T
\quad:\Longleftrightarrow\quad
T\vdash\mathrm{RFN}_\Gamma(U)
\]

と書く。これは通常自己反射を持たず、全 theories 上の無条件な preorder ではない。Sound natural theories の適切な領域では well-founded reflection ordering と rank を考えられる。[Pakhomov–Walsh](https://arxiv.org/abs/1805.02095)

### 0.9 Proof-theoretic reducibility / ordinal comparison

Proof-theoretic reducibility は、\(T\)-proofs を \(U\) または \(U+\mathrm{TI}(\alpha)\)、reflection progression 等へ変換し、指定 consequence class を保存する reduction relation の総称とする。単一の universal definition ではない。

\[
|U|_{\mathcal A}\le |T|_{\mathcal A}
\]

は、前稿どおり analysis package \(\mathcal A\)（notation、sound theory class、reduction notion、formula class、metatheory）に相対する ordinal comparison とする。

## 1. Relation の型

| relation | same language required? | translation allowed? | formula class dependent? | reflexive? | transitive? | antisymmetric? |
|---|---:|---:|---:|---:|---:|---:|
| axiom inclusion \(\subseteq_{ax}\) | 共通 signature/埋込みが必要 | no | no | yes | yes | literal axiom sets 上 yes |
| theorem inclusion \(\le_{Th}\) | yes／明示的埋込み | 通常 no | no | yes | yes | deductively closed sets 上 yes |
| \(\Gamma\)-strength \(\le_\Gamma\) | yes | 通常 no | **yes** | yes | yes | no；same \(\Gamma\)-theory quotient で yes |
| \(\Gamma\)-conservative extension | language inclusion | no | **yes** | yes | compatible extension chains で yes | strength orderとしては非該当 |
| interpretability \(\triangleright\) | no | **yes** | 通常 no | yes | yes | no；mutual interpretability quotient で yes |
| mutual interpretability | no | yes | no | yes | yes（equivalence） | no syntactically |
| bi-interpretability | no | yes | no | yes | yes（equivalence） | no syntactically |
| \(T\vdash \mathrm{Con}(U)\) | proof coding共有 | coding translation | no | **no** for consistent c.e. \(T\) | 無条件には no | strict relationとして扱う |
| relative consistency \(\le^B_{rCon}\) | codingを \(B\) で比較 | possible | no | yes | yes | no；equiconsistency quotient で yes |
| reflection \(<^{RFN}_\Gamma\) | coding/translation必要 | variant dependent | **yes** | 通常 no | domain/definition dependent | strict ordering domainで扱う |
| ordinal \(\le_\mathcal A\) | no | analysis bridge | package dependent | yes | yes | no；same ordinal quotient で yes |

Strict \(<\) relationsに reflexivity や antisymmetryを要求しない。Ordinal comparison は \(\mathcal A\) の共通 domain では total preorder になり得るが、異なる packages 間や ordinal 未分析 theories を含めた universal total order ではない。

## 2. Preorder・partial order・equivalence

| starting relation | natural equivalence \(T\sim U\) | quotient result |
|---|---|---|
| theorem inclusion | \(\mathrm{Th}(T)=\mathrm{Th}(U)\) | partial order of deductive theories |
| \(\Gamma\)-strength | \(\mathrm{Th}_\Gamma(T)=\mathrm{Th}_\Gamma(U)\) | partial order of \(\Gamma\)-theories |
| interpretability | mutual interpretability | interpretability degrees の partial order |
| relative consistency | \(B\)-provable equiconsistency | relative-consistency degrees の partial order |
| ordinal comparison | \(|T|_\mathcal A=|U|_\mathcal A\) | ordinal-indexed linear order on assigned degrees |
| mutual interpretability | relation自体が equivalence | quotient 後は identity。新たな strength direction はない |
| bi-interpretability | relation自体がより細かい equivalence | bi-interpretability classes |

「何で quotient したか」を消すと、同じ “degree” が deductive degree、interpretability degree、ordinal degree のどれか分からなくなる。

## 3. “Stronger” の意味一覧

| informal reading | precise statement | primary target |
|---|---|---|
| more axioms | \(U\subseteq_{ax}T\) | presentation |
| more theorems | \(\mathrm{Th}(U)\subseteq\mathrm{Th}(T)\) | same-language derivability |
| stronger on \(\Pi_n\) | \(\mathrm{Th}_{\Pi_n}(U)\subseteq\mathrm{Th}_{\Pi_n}(T)\) | consequence fragment |
| can simulate | \(T\triangleright U\) | translated structure/proofs |
| consistency stronger | \(T\vdash \mathrm{Con}(U)\) or \(B\vdash \mathrm{Con}(T)\to \mathrm{Con}(U)\) | internal certificate / relative consistency |
| reflection stronger | \(T\vdash \mathrm{RFN}_\Gamma(U)\) | correctness of \(U\)-proofs on \(\Gamma\) |
| induction stronger | induction schema inclusion/conservation | formula complexity |
| functionally stronger | provably total functions inclusion | computational consequences |
| ordinal stronger | \(|U|_\mathcal A<|T|_\mathcal A\) | fixed ordinal-analysis quotient |

Direct axiom inclusion normally yields theorem inclusion and identity interpretation. Beyond that, the arrows are conditional, class-relative, or false in general。

## 4. 通常 anatomy

1. **concept_name:** theory-strength order structures
2. **domain:** proof theory、interpretability theory、model theory、arithmetized metamathematics、ordinal analysis
3. **relations_compared:** axiom/theorem inclusion、conservativity、interpretability、consistency、reflection、proof-theoretic reduction、ordinal comparison
4. **assumptions:** languages、theory presentations、proof predicates、base theory、formula class、translation notion、soundness/reflexivity domain
5. **relation_types:** preorder、strict relation、equivalence relation、quotient partial order、class-relative conservation relation
6. **equivalence_quotients:** deductive equivalence、same \(\Gamma\)-theory、mutual/bi-interpretability、equiconsistency、same ordinal
7. **architecture_roles:** direct comparison、translation/simulation、old-language preservation、internal certification、reflection ranking、ordinal calibration
8. **comparison_targets:** axioms、theorems、models under translation、proof predicates、formula fragments、well-order/reflection ranks
9. **blocked_confusions:** extension≠new old-language consequences、interpretability≠inclusion、mutual≠bi、consistency proof≠reflection、ordinal≠universal strength
10. **implication_failures:** 第21節
11. **counterexamples_or_separations:** 第22節
12. **proof_resources:** deduction theorem、translation induction、Henkin construction、Pudlák lemma、Orey–Hájek、Gödel II、conservation/reduction theorems、ordinal analysis
13. **order_style:** **型付き複数順序**（比較ラベル）
14. **object_language_translation_comment:** Same-language inclusion は式をそのまま比較する。Interpretability は \(U\)-formula \(\varphi\) と \(T\)-formula \(\varphi^k\) を比較するため、翻訳を消して theorem inclusion のように読めない
15. **short_comment:** “stronger” は一つの hidden scalar を指すのではなく、選んだ relation の略記である。自然な theory family で複数 relations が同方向に揃うことは theorem/analysis の成果であり、一般定義ではない

## 5. Same-language theorem inclusion

同じ \(L\) 上で

\[
\operatorname{Th}_L(U)\subseteq\operatorname{Th}_L(T)
\]

は最も直接的である。Identity translation により \(T\triangleright U\) も得る。しかし language enrichment が入ると、\(T\) の新記号を含む theorem と \(U\)-sentences を同じ集合として比較できない。Definitional extension、Morita extension、conservative enrichment では、共通言語への reduct または translation を指定する必要がある。

## 6. Conservative extension の anatomy

例えば \(PA\) に新しい relation \(<\) と

\[
x<y\leftrightarrow\exists z\;x+Sz=y
\]

を加える definitional extension は、公理・語彙を増やすが、旧 \(PA\)-language の theorem を増やさない。従って

\[
\text{more symbols/axioms}
\not\Rightarrow
\text{more old-language consequences}.
\]

Full conservativity はすべての旧言語文、\(\Pi_n\)-conservativity はその class のみを保存する。後者では higher-complexity consequences が増えてよい。Extension と consequence strength の軸が直交する典型例である。

## 7. Interpretability の anatomy

Interpretation \(k=(\delta,F)\) は次を指定する。

- \(T\) 内で \(U\)-objects を表す domain formula \(\delta(x)\)
- 各 \(U\)-relation の \(T\)-formula \(F(R)\)
- equality の翻訳と quotient 条件
- Boolean connectives の保存
- quantifiers の \(\delta\)-relativization
- 各 \(U\)-axiom \(\sigma\) に対する \(T\vdash\sigma^k\)

One-dimensional interpretation は一つの \(T\)-object で \(U\)-object を表し、multidimensional interpretation は tuples を用いる。Parameters を許す variant、identity-preserving/definitional interpretations は strength が異なる。Interpretability は「\(T\) が \(U\) の各文をそのまま証明する」ことではなく、**translation 後の theory を内部再現する**ことだ。[Joosten](https://arxiv.org/html/1602.00555v1)

## 8. Interpretability と consistency strength

Main numberizable setting では Henkin construction により

\[
T\vdash\mathrm{Con}(U)
\Longrightarrow
T\triangleright U
\]

が成立する。これは「consistency と interpretation は同じ定義」という意味でなく、formalized completeness/Henkin model が与える theorem である。[Joosten, Theorem 4.5](https://arxiv.org/html/1602.00555v1)

逆向き

\[
T\triangleright U
\Longrightarrow
T\vdash\mathrm{Con}(U)
\]

は一般に偽である。反例は \(T=U\): identity interpretation により \(T\triangleright T\) だが、consistent c.e. \(T\) は自身の consistency を証明しない。Interpretation から一般に移せるのは、外部 relative consistency、または追加条件下の finite consistency / \(\Pi_1\)-consequence inclusion である。

従って「consistency comparison without interpretability」の具体例を \(T\vdash \mathrm{Con}(U)\) という強い形で探すのは、今回の standard numberizable setting では失敗する。この negative result を保存する。一方、外部 equiconsistency や \(B\vdash \mathrm{Con}(T)\leftrightarrow \mathrm{Con}(U)\) は、無条件には specific interpretation を与えない。

## 9. Orey–Hájek characterization

主版を次に固定する。\(T,U\) を suitable numberized/sequential、recursive、reflexive arithmetical theories とし、必要な coding・exponentiationを弱い base で形式化する。このとき概略、

\[
T\triangleright U
\]

は次と対応する。

\[
\forall n\quad T\vdash\mathrm{Con}_n(U),
\]

\[
\operatorname{Th}_{\Pi_1}(U)
\subseteq
\operatorname{Th}_{\Pi_1}(T).
\]

ここで \(\mathrm{Con}_n(U)\) は \(U\) の finite/bounded fragment の consistency であり、full \(\mathrm{Con}(U)\) ではない。Reflexivity、sequentiality/numberization、smooth vs axioms interpretability、base の induction/exponentiation条件は弱い arithmetic で本質的である。[Joosten](https://arxiv.org/abs/1602.00555)

従って Orey–Hájek は三 relation を無条件に同一化するのでなく、**特定 domain で interpretability preorder を finite consistency と \(\Pi_1\)-consequence preorder により characterize する bridge theorem**である。

## 10. Interpretability logic IL

IL は unary provability modality \(\Box\) に binary connective

\[
A\triangleright B
\]

を加え、arithmetical realizations の下で \(T+A^*\) が \(T+B^*\) を interprets する構造を modalize する。Basic IL は Löb principles に加え、interpretability の transitivity、provable implication から interpretation、consistency preservation 等を表す J-axioms を持つ。[Goris–Joosten](https://arxiv.org/abs/2004.12685)

- **ILM:** full induction/reflexive arithmetic で現れる Montagna principle を加えた代表 logic。
- **ILP:** finitely axiomatized sufficiently strong theories に対応する代表 logic。
- **IL(All):** reasonable theories 全体で共通する principles。完全な同定には未解決部分がある。

GLP が graded provability/reflection modalities を扱うのに対し、IL は theory extensions 間の binary interpretability を抽象化する。Modality index と interpretation target を同一視しない。

## 11. Mutual interpretability と bi-interpretability

Mutual interpretability は「両方向に内部モデルを一様構成できる」ことまでであり、往復して元の model/structure を回復する保証がない。Bi-interpretability は合成 interpretation と identity の間に definable isomorphisms を要求する。

標準的 separation として、ZFC は ZF を identity で interprets し、ZF は constructible universe \(L\) によって ZFC を interprets するため mutually interpretable である。しかし \(M\mapsto L^M\) は一般に元の ZFC-model を回復せず、ZF と ZFC は bi-interpretable でない。[Freire–Hamkins](https://arxiv.org/abs/2001.05262)

従って mutual interpretability を “same theory” と呼ぶのは、interpretability degree についてのみ許される。

## 12. Definitional・Morita・categorical equivalence

- **definitional equivalence / synonymy:** 共通 definitional extension を持つ、または identity-preserving translations が厳密に往復する強い sameness。
- **bi-interpretability:** definable isomorphism まで戻るが、一般には definitional equivalence より弱い。実際、bi-interpretable だが synonymous でない sequential theories が存在する。[Visser–Friedman](https://www.cambridge.org/core/journals/review-of-symbolic-logic/article/when-biinterpretability-implies-synonymy/00B8CAF9978904070D017C303308F414)
- **Morita equivalence:** sorts/products/quotients 等の definitional resources を許す language-relative sameness。
- **categorical equivalence:** categories of models の equivalence。選ぶ morphisms と functorial structure に依存し、一般に bi-interpretability と同一でない。

“same theory” にも equivalence hierarchy があるため、strength preorder の quotient を一意に選べない。

## 13. \(\Gamma\)-consequence ordering

\[
U\le_\Gamma T
\iff
\operatorname{Th}_\Gamma(U)
\subseteq
\operatorname{Th}_\Gamma(T)
\]

は \(\Gamma\) ごとに別 preorder を作る。

\[
\le_{\Pi_1},\ \le_{\Pi_2},\ \le_{\Sigma_1},\ldots
\]

は同じ relation の数値 parameter ではなく、異なる sentence domains 上の inclusions である。Class inclusion から一部の含意は得られるが、例えば \(\Sigma_n\) と \(\Pi_n\) の比較や uniform parameters の扱いには追加 theorem が必要になる。

## 14. Conservation spectrum

Theory pair \((T,U)\) に対して

\[
\mathrm{Spec}_{\mathrm{cons}}(T/U)
=
\{\Gamma:T\text{ is }\Gamma\text{-conservative over }U\}
\]

という説明的表示を置ける。標準的には conservativity spectrum / conservation profile と呼ぶべき内容である。

Single rank より spectrum が自然なのは、reduction theorem が「full equality」ではなく \(\Pi_n\)-conservation を返し、class を変えると結論が変わる場合である。ただし classes は包含関係や duality を持つため、単なる Boolean vector でもない。

## 15. Ordinal ordering と interpretability ordering

Natural sound arithmetic families では、larger ordinal、stronger reflection、interpretability が同方向に並ぶことが多い。しかし

\[
|U|_\mathcal A<|T|_\mathcal A
\not\Rightarrow
T\triangleright U
\]

は一般 implication でない。Ordinal は \(\mathcal A\) が捉える WO/TI/reflection quotient、interpretability は language translation の existence を測る。逆向きも、共通 analysis package と ordinal monotonicity theorem なしには出ない。

## 16. Ordinal ordering と conservativity

Same ordinal は同じ \(\Pi_n\)-theoriesを意味しない。Ordinal calibration が観測しない complexity の公理を追加すれば conservation spectrum は変わり得る。

逆に

\[
T\equiv_{\Pi_n}U
\]

から same ordinal も一般には従わない。採用 ordinal が \(\Pi_n\) より高い well-order/reflection information を測る可能性がある。特定 analysis で ordinal order が \(\Pi^1_1\)-theorem quotient と一致する結果は、この gap を埋める追加 characterization theorem である。[Walsh](https://arxiv.org/abs/2209.09765)

## 17. Consistency ordering


\[
U<_{\mathrm{Con}}T\iff T\vdash \mathrm{Con}(U)
\]

について:

- **irreflexive:** consistent c.e. \(T\) は通常 \(T\nvdash \mathrm{Con}(T)\)。
- **transitivity:** proof predicates、numberizations、soundnessを固定しない無条件な transitivity は置かない。\(U\) が false consistency statement を証明し得るため、mere consistency だけでは truth transfer がない。
- **coding dependence:** standard proof predicates 間では頑健でも、人工的 predicates では変わる。
- **non-strict replacement:** \(B\vdash \mathrm{Con}(T)\to \mathrm{Con}(U)\) は fixed \(B\) 上の relative-consistency preorder になる。
- **quotient:** mutual relative consistency による equiconsistency degree。

Strict self-certification order と relative-consistency preorder を分けることが、relation-type の監査上重要である。

## 18. Reflection ordering

\[
U<_\Gamma^{\mathrm{RFN}}T
\iff
T\vdash \mathrm{RFN}_\Gamma(U)
\]

は consistency ordering の \(\bot\)-instance より豊かで、\(\Gamma\)-correctness を対象にする。Scope と formula class を変えると別 relation になる。

Suitable \(\Pi^1_1\)-sound extensions の domain では reflection ordering が well-founded になり rank を持ち、natural theory classes では proof-theoretic ordinal と一致する結果がある。しかし arbitrary theories では ill-foundedness・人工的分岐・rank/ordinal の非一致が起こり得る。[Pakhomov–Walsh](https://arxiv.org/abs/1805.02095)

## 19. “Multiple order” 仮説

**判定: O2。**

Theory strength を複数の標準 preorders / strict orders / equivalence quotients の重なりとして扱うことは、単なる教育比喩でなく実務的に正確である。Orey–Hájek、ordinal characterization、reduction theorem は、それらが特定 domain で一致する条件を研究する。ただし各 relation は既に標準理論を持つため、universal multi-order theory という O3 の新概念ではない。

## 20. Order bundle 仮説

説明用に

\[
\mathfrak S(T,U)=
(\le_{Th},\le_{\Pi_1},\le_{\Pi_2},
\triangleright,\le^B_{rCon},<_\Gamma^{RFN},
\le_\mathcal A^{ord})
\]

と記録することはできる。ただし components は truth values、preorder positions、strict relations、ordinal values が混在し、代数演算を持つ vector ではない。

**判定: B2。** Cross-theory audit table として有効だが、新 invariant の B3 ではない。

## 21. Implication graph

| source | target | status | conditions / failure reason |
|---|---|---|---|
| axiom inclusion | theorem inclusion | **always** | common logic/signature |
| theorem inclusion | interpretability | **always** | same language、identity interpretation |
| theorem inclusion | \(T\vdash \mathrm{Con}(U)\) | **generally false** | \(T=U\) と Gödel II |
| conservative extension | theorem inclusion | **always** | extension directionでは \(\mathrm{Th}(U)\subseteq \mathrm{Th}(T)\) |
| conservative extension | equal old-language consequences | **always** | definitionそのもの |
| full conservativity | \(\Gamma\)-conservativity | **always** | \(\Gamma\) が旧言語文の class |
| \(T\vdash \mathrm{Con}(U)\) | \(T\triangleright U\) | **under standard numberizability; very broad** | formalized Henkin construction |
| \(T\triangleright U\) | \(T\vdash \mathrm{Con}(U)\) | **generally false** | identity interpretation counterexample |
| \(T\triangleright U\) | finite \(\mathrm{Con}_n(U)\) in \(T\) | **under assumptions** | reflexive/sequential Orey–Hájek setting |
| \(T\triangleright U\) | \(\mathrm{Th}_{\Pi_1}(U)\subseteq \mathrm{Th}_{\Pi_1}(T)\) | **under assumptions** | reflexivity/Pudlák/Orey–Hájek conditions |
| bi-interpretability | mutual interpretability | **always** | definitions |
| mutual interpretability | bi-interpretability | **generally false** | ZF/ZFC-type loss on round trip |
| definitional equivalence | bi-interpretability | **under standard notions** | definitional translations yield definable return |
| bi-interpretability | definitional equivalence | **generally false** | additional identity-preserving hypotheses needed |
| \(T\vdash \mathrm{RFN}_\Gamma(U)\) | \(\mathrm{Th}_\Gamma(U)\subseteq \mathrm{Th}_\Gamma(T)\) | **under proof-coding assumptions** | fixed \(U\)-proofを \(T\) が認識して reflection適用 |
| larger ordinal | interpretability | **generally false / package mismatch** | ordinal rank does not supply translation |
| interpretability | ordinal inequality | **under specific natural analyses only** | monotonicity/reduction theorem required |
| same \(\Pi_n\)-theory | same ordinal | **generally false** | ordinal may observe higher class |

この表の核心は、無条件の太い矢印が axiom/theorem inclusion 周辺に集中し、他の alignment は bridge theorem に依存することである。

## 22. Counterexamples / separations

1. **Same ordinal, not deductively equivalent:** common calibration では \(PRA\) と \(I\Sigma_1\) がともに \(\omega^\omega\) と表示されるが、理論は deductively identical でない。Parsons-type conservation は低 complexity の近さを説明するだけである。
2. **Conservative but syntactically larger:** \(PA\) に definable \(<\) を追加した definitional extension。公理・語彙は増えるが旧言語 consequences は同じ。
3. **Mutual but not bi-interpretable:** ZF と ZFC。ZFC→ZF は identity、ZF→ZFC は \(L\) interpretation。往復は元の model を回復しない。
4. **Same low consequences, different higher theory:** \(I\Sigma_1\) は standard setting で \(PRA\) に対し \(\Pi_2\)-conservative とされるが、full deductive equivalence ではない。
5. **Interpretability without same-language inclusion:** ZF は \(L\) で ZFC を interprets するが、ZF は Choice をそのまま証明しない。
6. **Full consistency proof without interpretation:** adopted numberizable setting では作れない。\(T\vdash \mathrm{Con}(U)\) から Henkin interpretation が得られる。外部 equiconsistencyへ弱めれば interpretation は自動しない。

## 23. Linear hierarchy stress test

よく描かれる

\[
EA\subset I\Sigma_1\subset I\Sigma_2
\subset\cdots\subset PA
\]

は、共通言語・標準 presentation では axiom/theorem inclusion の chain である。Identity interpretations により interpretability も同方向へ並ぶ。標準 ordinal analyses でも増大する。しかし:

- adjacent consistency/reflection claims には別 metatheorem が要る。
- \(\Pi_n\)-conservation では一部段階が同値に潰れる場合がある。
- ordinal growth rate は axiom count で決まらない。
- language/presentation を変えると literal inclusion は消えても interpretability は残り得る。

一本線は複数 relations が一致する**自然 family 内の投影**である。

## 24. Natural theories と arbitrary theories

Natural arithmetic fragments は、共通 base、同じ language、nested induction classes、canonical proof predicates、既知 ordinal analyses を共有する。この選択が theorem inclusion、interpretability、reflection、ordinal の方向を揃えやすくする。

Arbitrary independent extensions、異なる signatures、人工的 provability predicates、soundnessを欠く theoriesを許すと、preorders は分岐・同値化・非比較化する。従って theory strength が一本に見えるのは、自然 family の選択と bridge theorems の成功による部分が大きい。

## 25. Canonicality C2*

**再判定: C2\*.**

Natural arithmetic families では複数 relations が同じ方向に整列し、ordinal/reflection/interpretability degrees に相当の canonicality が現れる。しかし arbitrary theories では quotient equivalence 自体が relation ごとに違い、一本の canonical hierarchy はない。前稿の “natural analysis families では安定、一般には非一意” という限定をさらに支持する。

## 26. Proof architecture P2

Theory comparison は

\[
(T,U,L_T,L_U,R,\Gamma,k,B,\text{coding})
\]

を固定して初めて明確になる。ここで \(R\) は比較 relation、\(k\) は language translation、\(B\) は formalized metatheory である。

**再判定: P2。** Comparison parameters を明示する audit architecture として、theorem→logic→progression→ordinal→theory-pair comparison まで耐える。標準 interpretability/conservation theory を置換する P3 ではない。

## 27. Strength profile V2

前稿の「複数数値成分」という読みを修正する。より正確には strength profile は

- theorem sets の inclusion
- \(\Gamma\)-consequence preorders
- interpretation existence
- consistency/reflection strict relations
- ordinal rank

という**異型 relations の profile**である。共通 vector space、距離、加法はない。

**再判定: V2。** 多数の relation/preorder を監査する実用的メタ表現として維持するが、標準 conservativity spectrum・interpretability degree・reflection rank を超える invariant ではない。

## 28. Moving boundary

Interpretability/conservativity comparison では stage reindexing は中心でなく、relation type と quotient choice が情報の本体である。

**再判定: M0。** 今回は教育的要約としてもほぼ追加情報を持たず、主分析から外す。Turing/reflection progression の stage anatomy に限れば M1 を保持できる。

## 29. Residual

Uninterpretable fragment、nonconservative consequence、unproved consistency、missing reflection、larger ordinal は型が異なる。これらを一つの「残差」にまとめると、まさに今回分離した relations を再混同する。

**判定: RX — residual vocabulary not useful here.**

## 30. Erasure Test

“multiple order”“order bundle”“strength profile”“proof architecture”“canonicalization”“moving boundary”“residual” を削除しても、theorem inclusion、conservativity、interpretability、Orey–Hájek、bi-interpretability、relative consistency、reflection ordering、ordinal analysis、IL だけで数学的内容は完全に記述できる。

一方、「stronger」の省略を監査し、異型 relations を一枚に並べる見通しは少し失われる。

**判定: E1。** 技術的内容は失わず、cross-document audit の可読性だけを失う。

## 31. 最終比較表

| relation | compares what | same language? | quotient equivalence | gives total order? | standard use |
|---|---|---:|---|---:|---|
| axiom inclusion | literal presentations | common signature | literal equality | no | direct extension bookkeeping |
| theorem inclusion | deductive closures | yes/embedding | deductive equivalence | no | same-language strength |
| \(\Pi_n\)-strength / conservativity | formula fragments | yes | same \(\Pi_n\)-theory | no | conservation/reduction theorems |
| interpretability | translated theories/internal models | no | mutual interpretability | no | relative reduction、undecidability、consistency transfer |
| mutual interpretability | two-way simulation | no | relation自体 | n/a | interpretability degree equality |
| bi-interpretability | recoverable two-way interpretation | no | relation自体 | n/a | strong structural sameness |
| relative consistency | formalized Con implications | coding base | equiconsistency | no | consistency strength comparison |
| reflection ordering | theory correctness over \(\Gamma\) | coding/translation | equal reflection degree/rank | natural domainで時に well-order | ordinal analysis、reflection progression |
| proof-theoretic ordinal | chosen reduction/WO rank | no | same assigned ordinal | assigned domainでは yes | one-dimensional calibration |

## 32. “Stronger” safe-language checklist

| Bad | Better |
|---|---|
| \(T\) is stronger than \(U\). | \(T\) is a deductive extension of \(U\) in language \(L\). |
| \(T\) adds strength. | \(T\) adds axioms but is conservative over \(U\) for \(U\)-language sentences. |
| \(T\) and \(U\) have the same strength. | \(T\) and \(U\) have the same \(\Pi_1\)-consequences. |
| \(T\) contains \(U\). | \(T\) interprets \(U\) via interpretation \(k\). |
| \(T\) is consistency-stronger. | \(T\vdash \mathrm{Con}(U)\) for the standard proof predicate. |
| \(T\) is reflection-stronger. | \(T\vdash \mathrm{RFN}_{\Pi_n}(U)\). |
| \(T\) has more ordinal strength. | \(|U|_\mathcal A<|T|_\mathcal A\) under analysis package \(\mathcal A\). |

Final checklist:

1. 同じ language か、translation を使うか。
2. 公理、全定理、どの formula class を比較するか。
3. Internal proof \(T\vdash \mathrm{Con}(U)\) か external relative consistency か。
4. Reflection の scope と \(\Gamma\) は何か。
5. Quotient equivalence は deductive、mutual interpretation、equiconsistency、same ordinal のどれか。
6. Ordinal analysis package は何か。

## 33. Kill criteria

| criterion | result |
|---|---|
| relation未指定の “stronger” は未定義に近い | 成立 |
| theorem inclusion と interpretability は別 preorder | 成立 |
| conservativity は formula class に依存 | 成立 |
| consistency と interpretability は無条件に一致しない | 成立。Henkin/Orey–Hájekで条件付き接続 |
| ordinal comparison は別 quotient/order | 成立 |
| natural-family alignment は一般化できない | 成立 |
| order bundle に標準 relations以上の予測力がない | 成立。B2 audit table に限定 |
| proof architecture は parameter audit に留まる | 成立。P2 |
| residual vocabulary は不要 | 成立。RX |

Negative result を保存する。今回の新規価値は新しい multi-order mathematics ではなく、標準 relations の型を横断表にして「どの stronger か」を強制的に明示することにある。

## 34. 最終出力

### A. Theory strength の核心

- “stronger” は binary relation を指定しない限り不完全である。
- Same-language theorem inclusion、translation-based interpretability、class-relative conservativity は別 relations。
- Consistency/reflectionには strict self-certification と non-strict relative orders の差がある。
- Ordinal comparison は固定 analysis quotient 上の calibration である。
- Natural families での整列は一般定義でなく bridge theorems の成果である。

### B. 最重要 relations

1. deductive inclusion
2. \(\Gamma\)-consequence inclusion / conservativity
3. interpretability
4. bi-interpretability
5. relative consistency / internal \(Con\)-proof
6. \(\Gamma\)-reflection ordering
7. proof-theoretic reducibility / ordinal comparison

### C. Deductive inclusion と interpretability

- Inclusion は同じ式を比較し、interpretability は translation 後の式を比較する。
- Inclusion は common language を要し、interpretability は異言語間で働く。
- Inclusion は identity interpretation を与える。
- Interpretation は original theorem inclusion を一般に与えない。
- Interpretability preorder の quotient は mutual interpretability degree である。

### D. Conservativity の位置

- Extension が旧言語／指定 class で新定理を増やさない条件。
- 「公理が増えた＝旧言語 strength が増えた」を否定する。
- Full と \(\Pi_n\)-conservativityを分ける。
- Relationではなく conservation spectrum として見る場合がある。
- Theory equality ではない。

### E. Consistency / reflection ordering

- \(T\vdash \mathrm{Con}(U)\) は strict certification であり preorder ではない。
- \(B\vdash \mathrm{Con}(T)\to \mathrm{Con}(U)\) は relative-consistency preorder。
- \(T\vdash \mathrm{Con}(U)\Rightarrow T\triangleright U\) は標準 setting で Henkin theorem。
- Reverse は full Con では偽、finite Con/\(\Pi_1\) では Orey–Hájek 条件下で対応。
- Reflection ordering は \(\Gamma\) と scope に相対し consistency より細かい。

### F. Ordinal ordering

- Fixed analysis package 上の one-dimensional quotient order。
- Deductive、interpretability、conservation ordersを一般には決定しない。
- Natural theoriesでは reflection/WO orders と一致する場合がある。
- Same ordinal は same theory を意味しない。
- Larger ordinal は universal stronger を意味しない。

### G. Multiple-order 判定

**O2** — theory strength を複数の標準 preorders / quotient orders として扱うのが実用的に正確。新 formalism ではない。

### H. Order-bundle 判定

**B2** — cross-theory audit table として有効。新 invariant ではない。

### I. Strength-profile 再判定

**V2** — 数値 vector ではなく、異型 relations の typed profile として更新・維持。

### J. Proof architecture 再判定

**P2** — theory pair、languages、relation、formula class、translation、metatheory の監査枠として有効。

### K. Canonicalization 再判定

**C2\*** — natural arithmetic familiesでは alignment が安定するが、arbitrary theoriesには一本の canonical order はない。

### L. Moving boundary

**M0** — 今回の order comparison には追加情報を与えない。

### M. Residual

**RX** — nonconservativity、noninterpretability、unproved reflection等を一括しない。

### N. Erasure Test

**E1** — 独自語彙なしで数学は全記述でき、横断監査の見通しのみ少し失う。

### O. 最も重要な新規観察

1. Theory strength は「多軸の数値」より、まず**型の異なる relations の束**として理解する方が正確である。
2. Orey–Hájek は relation の同一性でなく、reflexive/sequential theories 上の conditional alignment theorem である。
3. Natural arithmetic hierarchy が一本に見えるのは、common language・nested axioms・canonical coding・ordinal analyses が複数 orders を揃えるためである。

### P. 次の一手

1. **interpretability logic IL / ILM stress test** — binary interpretability relation の modal abstraction が order bundle のどこを保存するか検査できる。
2. **definitional / Morita / categorical equivalence** — “same theory” 側の quotient choices を独立に解剖できる。
3. **natural theory families と strength alignment** — 複数 orders が一本に揃う十分条件と破綻例を比較できる。

## 参考資料

- [Joost J. Joosten, “Characterizations of Interpretability in Bounded Arithmetic”](https://arxiv.org/abs/1602.00555) — relative interpretation、Henkin construction、finite consistency、Orey–Hájek の条件。
- [Evan Goris and Joost J. Joosten, “The Interpretability Logic of All Reasonable Arithmetical Theories”](https://arxiv.org/abs/2004.12685) — IL、arithmetical interpretations、IL(All)。
- [Fedor Pakhomov and James Walsh, “Reflection Ranks and Ordinal Analysis”](https://arxiv.org/abs/1805.02095) — reflection ordering、rank、proof-theoretic ordinalとの一致範囲。
- [James Walsh, “Characterizations of Ordinal Analysis”](https://arxiv.org/abs/2209.09765) — ordinal analysis が与える quotient/order の特徴づけ。
- [Alfredo Roque Freire and Joel David Hamkins, “Bi-interpretation in Weak Set Theories”](https://arxiv.org/abs/2001.05262) — mutual interpretability と bi-interpretability の separation。
- [Albert Visser and Harvey Friedman, “When Bi-interpretability Implies Synonymy”](https://www.cambridge.org/core/journals/review-of-symbolic-logic/article/when-biinterpretability-implies-synonymy/00B8CAF9978904070D017C303308F414) — bi-interpretability、synonymy、identity-preserving conditions。

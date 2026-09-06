# Theorem closure / open remainder pilot v0.1

## 0. Status / posture

本稿は次の地位に限定される。

- **exploratory pilot**
- **not a theorem**
- **not a new proof theory**
- **not a new semantics**
- **not a new closure calculus**
- **not a new notion of theoremhood**
- **no new score**
- **no geometry / topology of proofs**
- **no metaphysical conclusion**
- **no VED claim**
- **reachability-oriented vocabulary remains retired**
- **prefer standard terminology whenever possible**

今回の目的は “what is the essence of a theorem?” を問うことではない。次のものも探さない。

- true core
- essential resource
- canonical proof
- proof geometry
- final foundational layer

表題の “closure” と “open remainder” は問題提起の平易な語であり、technical termsではない。新しい operator、hierarchy、invariantを定義しない。中心問いは次である。

> A theorem can be settled while many surrounding questions remain unsettled.
> What exactly is settled by theoremhood, and what may remain open without
> preventing theoremhood?

結論を先に述べる。四例すべてで、固定された formal context における derivability judgment は成立しながら、proof choice、dependency minimality、background choice、presentation、formation historyはその judgmentだけでは決まらなかった。しかも少なくとも一つの具体的 variationが、同じ theory・rules・targetを保ったまま各例で実在した。

ただしこれは新発見ではない。derivability judgmentが何を主張するかと、何を主張しないかを四例で監査したにすぎない。“theorem closure” は standard derivability languageを越える内容を加えなかった。

---

## 1. Standard formal reading

基本形を

\[
\Gamma\vdash_R\varphi
\]

と書く。これは新 notationではなく、通常省略される componentsを明示した standard derivability notationである。

- \(\mathcal L\): language。どの symbolsと formulasを使うか。
- \(\Gamma\): theory / assumptions。premises、axioms、theorem hypotheses。
- \(R\): fixed inference rules / calculus。
- \(\varphi\): target formula。

formal proof witnessを \(\pi\) と書けば、通常

\[
\pi:\Gamma\vdash_R\varphi
\]

は \(R\) に従って \(\Gamma\) から \(\varphi\) を導く有限 derivationを表す。少なくとも一つの適格な \(\pi\) が存在することが derivabilityを witnessする。

ただし次を区別する。

1. \(\varphi\): formula。
2. \(\Gamma\vdash_R\varphi\): derivability judgment。
3. \(\pi\): その judgmentの一つの proof witness。
4. intended structureでの \(\varphi\) の truth: soundness、interpretation等を通じて別途関係づけられる semantic claim。

本稿の “theoremhood settled” は 2 が確立したことを指す。1、2、3、4を同一視しない。特に一つの \(\pi\) は theoremhoodを witnessするが、theoremhoodそのものと同一ではない。

### 1.1 Exactly what the judgment says

固定した \((\mathcal L,\Gamma,R,\varphi)\) に対して \(\Gamma\vdash_R\varphi\) が成立するなら、少なくとも次が答えられる。

- \(R\) が認める \(\Gamma\)-derivationで conclusion \(\varphi\) に至るものが存在する。
- 従って、その fixed context内では targetは derivableである。
- 提示された \(\pi\) が正しければ、それが existence claimの witnessになる。

この judgmentだけからは、proofの一意性、最短性、自然さ、発見史、\(\Gamma\) の最小性、各 resourceの不可欠性は従わない。

---

## 2. Central distinction to test

working hypothesisは次である。

\[
\text{theoremhood settled}
\not\Rightarrow
\text{all surrounding dependency questions settled}.
\]

より具体的には、\(\Gamma\vdash_R\varphi\) が成立しても、次は judgmentの内容に自動的には含まれない。

- proof identity / which witness was used
- proof uniqueness or proof minimality
- minimal assumptions / weakest base theory
- necessity of a displayed or imported proof resource
- a canonical proof or canonical proof-equivalence criterion
- why this foundation、language、presentation was chosen
- historical discovery and construction record
- motivation、naturalness、best exposition
- whether all proofs share a resource

これは「これらは決して解けない」という claimではない。定理の judgment単独が答えない、という限定的 hypothesisである。四例で concrete variationを見つけられなければ、単なる情報不足の言い換えとして downgradeする。

---

## 3. Reused cases and evidence policy

新しい theoremは追加しない。次の四例だけを再利用する。

1. \(1+1=2\)
2. addition commutativity
3. Intermediate Value Theorem (IVT)
4. Fundamental Theorem of Algebra (FTA)

既存 stress testsの証明と counterexamplesを再発明せず、その記録を evidenceとして使う。retired済みの project-local framingは復活させず、standard termsへ戻す。

variation controlは次を満たす場合だけ採用する。

- same \(\mathcal L\) または明示された conservative notationの範囲
- same \(\Gamma\)
- same inference rules \(R\)
- same target \(\varphi\)
- derivation witnessまたはその presentationだけが変わる

field、domain、operation interpretation、theorem hypothesis、targetを変えるものは「theoremhoodを保った variation」の primary evidenceには数えない。そうした comparisonは別 judgmentの例にすぎない。

---

## 4. Four theorem records

### 4.1 Case I — \(1+1=2\)

#### A. Fixed context

- **Language:** \(0,S,+,=\)。
- **Theory / definitions:** \(x+0=x\)、\(x+S(y)=S(x+y)\)、numeral abbreviations \(1:=S(0)\), \(2:=S(S(0))\)。
- **Rules:** ordinary equality, substitution, definitional unfolding。
- **Domain / intended structure:** Peano-style natural numbers。
- **Target:** \(1+1=2\)。

#### B. Judgment

この fixed arithmetic contextを \(\Gamma_{1+1}\) とすれば

\[
\Gamma_{1+1}\vdash_R 1+1=2.
\]

#### C. Witness

一つの derivationは

\[
S(0)+S(0)
=S(S(0)+0)
=S(S(0))
=2.
\]

順に Add-S、Add-0、numeral definitionを使う。

#### D. Settled by theoremhood

- fixed theory/rulesから targetが derivable。
- 少なくとも一つの derivationが存在する。
- 上の calculationがその witnessになる。

#### E. Not settled by theoremhood

- この derivationを macro-expanded formと同じ proofと数えるべきか。
- universal lemma \(\forall x\,(x+1=S(x))\) を先に証明する presentationがより自然か。
- recursion equationsが最小の baseか。
- numeral abbreviationsをどう選んだ理由。
- historical discovery order、pedagogical best form。

#### F. Open remainder that varies while theoremhood survives

同じ \(\Gamma_{1+1},R,\varphi\) で少なくとも二つの recordsを作れる。

1. **Inline:** 上の三段 rewriteを直接行う。
2. **Lemma-mediated:** まず同じ theory内で \(L:\forall x\,(x+S(0)=S(x))\) を Add-S と Add-0から導き、\(x=S(0)\) を代入して numeral definitionを展開する。

後者は derived lemmaを含む syntactically different derivation organizationである。どちらでも target judgmentは同じ。両者がある proof-equivalence relationの下で “essentially same” かは、theoremhoodが答える必要のない別問題である。

notation renamingも corresponding judgmentを保存し得るが、それは厳密には presentation translationを伴うため、same-language variationの主 controlには用いない。

---

### 4.2 Case II — addition commutativity

#### A. Fixed context

- **Language:** \(0,S,+,=\)。
- **Theory:** successor background、Add-0、Add-S、induction schema。
- **Rules:** first-order logic with equality and substitution。
- **Domain / intended structure:** natural numbers。
- **Target:**
  \[
  \forall x\forall y\,(x+y=y+x).
  \]

#### B. Judgment

\[
\Gamma_{+}\vdash_R\forall x\forall y\,(x+y=y+x).
\]

#### C. Witness

既存 testは \(L_1:\forall x(0+x=x)\) と \(L_2:\forall x\forall y(Sx+y=S(x+y))\) を inductionで導出し、\(y\) について inductionする proofを完全展開した。baseは Add-0 と \(L_1\)、stepは Add-S、induction hypothesis、\(L_2\) で閉じる。

#### D. Settled by theoremhood

- fixed arithmetic theory内で universal commutativity formulaが derivable。
- 少なくとも一つの induction proofが存在する。

#### E. Not settled by theoremhood

- induction variableを \(x\) と \(y\) のどちらにするか。
- \(L_1,L_2\) を named lemmasにするか inlineするか。
- 二つの induction organizationsが essentially sameか。
- helper lemmasや induction schemaの exact minimality。
- proof discovery order、best exposition、weakest base theory。

#### F. Open remainder that varies while theoremhood survives

既存 testには、同じ \(\Gamma_+,R,target\) で

- \(y\) について inductionする organization
- \(x\) について inductionする organization
- named \(L_1,L_2\) を使う modular presentation
- それらの derivationsを theorem proof内へ inlineする presentation

がある。二つの induction proofsは homologousであり、深い多様性を示す controlではない。それでも theoremhoodが induction variableや lemma boundaryを選ばないことを示すには十分である。

---

### 4.3 Case III — IVT

#### A. Fixed context

- **Language / setting:** standard real analysis over \(\mathbb R\)。
- **Theory / background:** ordered-field structure、real completeness、order topology、ordinary logic/equality。
- **Hypotheses:** \(f:[a,b]\to\mathbb R\) continuous、\(a<b\)、\(f(a)<0<f(b)\)。
- **Rules:** standard real-analysis reasoning。
- **Target:** \(\exists c\in(a,b)\,f(c)=0\)。

#### B. Judgment

\[
\Gamma_{\mathrm{IVT}}\vdash_R
\bigl(f(a)<0<f(b)\to\exists c\in(a,b)\,f(c)=0\bigr),
\]

where continuity and domain assumptions are included in \(\Gamma_{\mathrm{IVT}}\)。

#### C. Witness

既存 testは二 proofsを記録した。

1. \(N=\{x\in[a,b]:f(x)<0\}\), \(c=\sup N\) とし、continuityで \(f(c)<0\), \(f(c)>0\) を排除する supremum proof。
2. \([a,b]\) connected、continuous image connected、connected subset of \(\mathbb R\) is an intervalを用いる connectedness proof。

#### D. Settled by theoremhood

- fixed real settingと hypothesesの下で zero-existence targetが derivable。
- 少なくとも一つ、実際には二つの displayed proofsが存在する。

#### E. Not settled by theoremhood

- どちらの proofが用いられたか、より自然か、より explanatoryか。
- connectedness theoremを citationとして止めるか、その proofを展開するか。
- completenessが all proofsまたは theorem itselfに必要か。
- weakest base theory、chosen foundation、historical discovery path。
- 二 proofsを同じ proofと数える equivalence criterion。

#### F. Open remainder that varies while theoremhood survives

同じ \(\Gamma_{\mathrm{IVT}},R,target\) を保持して supremum proofと connectedness proofを交換できる。また connectedness proofの cited resultsを black boxとして表示するか、その standard proofsを inlineするかで dependency recordの粒度を変えられる。

後者は theoremや mathematical contentの変更ではなく presentation/citation boundaryの変更である。ただし、どこまで inlineした recordsを同じ formal proof objectとみなすかは calculusと proof representationに依存するので、本 pilotは答えを要求しない。

---

### 4.4 Case IV — FTA

#### A. Fixed context

- **Language / setting:** complex polynomials over standard \(\mathbb C\)。
- **Theory / background:** field/norm algebra、standard complex analysis and topology。
- **Hypothesis:** \(p\in\mathbb C[z]\), \(\deg p\ge1\)。
- **Rules:** standard mathematical reasoning in the fixed development。
- **Target:** \(\exists c\in\mathbb C\,p(c)=0\)。

#### B. Judgment

\[
\Gamma_{\mathrm{FTA}}\vdash_R
\forall p\in\mathbb C[z]\,
(\deg p\ge1\to\exists c\in\mathbb C\,p(c)=0).
\]

#### C. Witness

既存 testは二 proofsを記録した。

1. no rootを仮定し、\(1/p\) を bounded entire functionにして Liouville theoremから contradictionを得る analytic proof。
2. large circle上の \(p\) を leading term loopへ homotopyし winding number \(n\) を得る一方、zero-free disk extensionなら null-homotopicで winding number \(0\) となる topological proof。

#### D. Settled by theoremhood

- fixed complex settingで全 nonconstant polynomialに少なくとも一つ complex rootがあることが derivable。
- 少なくとも一つ、実際には異なる theorem librariesを用いる二 proof witnessesがある。

#### E. Not settled by theoremhood

- Liouville/Cauchy organizationと winding/covering organizationのどちらを選んだか。
- common compactness supportが theorem-level necessaryか。
- Cauchy theory、winding theory、completenessの exact necessity。
- proof comparisonをどの citation depthで止めるか。
- canonical proof identity、best proof、historical motivation、weakest foundation。

#### F. Open remainder that varies while theoremhood survives

同じ \(\Gamma_{\mathrm{FTA}},R,target\) で Liouville proofと winding proofを交換できる。直接引用する libraryは bounded entire/Cauchy theoryと winding/covering theoryで大きく異なるが、theoremhoodは同じである。

また各 proofを displayed formに保つか、事前に固定した二段階まで citationsを展開するかで dependency recordを変えられる。展開後も theoremhoodは変わらず、major resource necessityが未決でも proof witnessesは有効である。

---

## 5. Concrete variation controls

| theorem | fixed across comparison | actual variation | theoremhood preserved? | caution |
|---|---|---|---|---|
| \(1+1=2\) | language, recursion equations, equality rules, target | inline calculation vs derived universal lemma then instantiation | yes | notation translationは primary controlにしない |
| addition commutativity | arithmetic theory, induction, target | induction on \(y\) vs \(x\); named lemmas vs inline | yes | proofs are homologous; no strong diversity claim |
| IVT | standard \(\mathbb R\), continuity/domain hypotheses, zero target | supremum proof vs connectedness proof; citation black boxes vs expansion | yes | \(\mathbb R\to\mathbb Q\) は variation controlでなく different setting |
| FTA | standard \(\mathbb C\), polynomial/nonconstant hypotheses, root target | Liouville proof vs winding proof; different theorem libraries | yes | \(\mathbb C\to\mathbb R\) は different setting |

四例すべてで、theorem/setting/targetを変えずに少なくとも一つの proofまたは presentation recordを変えられた。従って “open remainder” は単に未知の alternativeを想像したものではない。

ただし、variationがあることは無限個の proofs、non-equivalent proofs、あるいは canonical proofの不存在を示さない。存在する複数 recordsを theoremhood judgmentが選ばない、という範囲だけが supportedである。

---

## 6. Three kinds of openness

以下はこの pilotの整理用 labelsであり、新 taxonomyではない。

### O1. Proof-open

複数の proof witnesses / organizations / presentationsがあり、どれが chosenか \(\Gamma\vdash_R\varphi\) だけでは決まらない。

- \(1+1=2\): inline vs lemma-mediated。
- commutativity: induction-variable / lemma-boundary variation。
- IVT: supremum vs connectedness。
- FTA: Liouville vs winding。

### O2. Dependency-open

どの assumptions/resourcesが minimalまたは theorem-level necessaryかは、bare derivability judgmentだけでは決まらない。

- IVT theoremhoodは、displayed/expanded completeness dependencyの necessity分析が完了する前から成立する。
- FTA theoremhoodは、compactness、completeness、Cauchy、windingの exact necessityが未確定でも成立する。
- addition commutativityでは induction deletionの countermodelが別途 necessity evidenceを与えたが、その情報は元の positive judgmentだけから出たのではない。

### O3. Background-open

なぜこの language、theory、calculus、foundation、presentationを選んだかは judgmentに含まれない。\(\Gamma\) と \(R\) は評価時には fixedだが、その選択理由や代替基礎との関係は別問題である。

O1–O3は互いに排他的とは限らず、complete listでもない。歴史、motivation、pedagogyは別の open questionsになり得るが、新しい階層にはしない。

---

## 7. Open is not unknown

中心区別は

\[
\text{not settled by theoremhood}
\ne
\text{mathematically unknowable}.
\]

“not settled by theoremhood” は、\(\Gamma\vdash_R\varphi\) という judgmentの内容からその答えが出ないという意味である。“we do not know” は調査者の epistemic stateであり、別である。

例を挙げる。

- theoremhoodはどの proofを使ったかを encodeしないが、論文や proof objectを見れば分かり得る。
- weakest base theoryは positive derivability judgmentだけから決まらないが、reverse mathematicsや proof theoryにより外部的に既知の場合がある。
- two proofsの equivalenceは bare theoremhoodが答えないが、特定の proof calculusと equivalence relationを固定すれば研究可能である。
- historical discovery pathは formal proofに含まれないが、historical recordsから判明し得る。

従って open remainderを arbitrary ignoranceの箱にしてはならない。何に対して未決なのかを常に明示する。本稿では **the theoremhood judgment aloneに対して未決** という意味で用いる。

---

## 8. Theorem-level completion vs foundational completion

### Theorem-level completion

fixed \((\mathcal L,\Gamma,R,\varphi)\) のもとで、適格な derivation \(\pi\) が与えられ \(\Gamma\vdash_R\varphi\) が確立している。

### Foundational completion

なぜその axioms、rules、number/field construction、logic、semantic interpretationを採用したか、代替基礎とどう対応するか、さらに何がそれらを正当化するかまで説明が完了している状態。

四例のどれでも、後者は前者の必要条件ではなかった。

- arithmetic examplesは natural-number theoryを固定すれば proofが進み、その theory選択の究極的正当化を要求しない。
- IVTは standard \(\mathbb R\) developmentを固定すれば証明でき、real constructionや weakest base theoryを完了させる必要がない。
- FTAは standard \(\mathbb C\) と chosen theorem librariesで証明でき、Cauchy theoryや covering theoryの final foundational layerを必要としない。

従って supportedなのは標準的な次の statementである。

> Theoremhood is evaluated relative to a fixed formal context.

これは真理の相対主義でも、axiomsが arbitraryだという claimでもない。固定した contextの選択理由を judgment外に残せる、というだけである。“local closure” のような新 technical termは導入しない。

---

## 9. Does theoremhood depend on proof-history completion?

各例で答えは **NO** である。

| theorem | proof witness sufficient for theoremhood | history not required by the judgment |
|---|---|---|
| \(1+1=2\) | finite rewrite derivation | なぜ direct rewriteを先に選んだか、lemmaをいつ考えたか |
| commutativity | completed induction proof | direct attempt、helper-lemma introduction、induction-variable selectionの順序 |
| IVT | supremum proofまたは connectedness proof | sign-set/image-setのどちらを最初に着想したか、citationをいつ展開したか |
| FTA | Liouville proofまたは winding proof | reciprocal strategyと large-circle strategyの選択・放棄履歴 |

formal proof witnessには、その calculusで正当化に必要な derivation stepsまたは有効な theorem citationsが含まれなければならない。しかし、その proofがどのように発見・編集・圧縮されたかという formation historyの完全記録は不要である。

proof-formation strandは、semantic endpointや coarse recordから history、identity、provenanceが復元できないことをより細かく示していた。本 pilotはそれを新 theorem anatomyへ変換しない。standard theoremhood judgmentが historical recordを fieldとして持たない、という対応だけを確認する。

また、historyが theoremhoodに不要であることは historyが無価値だという意味ではない。explanation、credit、error diagnosis、proof discovery研究には重要でも、\(\Gamma\vdash_R\varphi\) の成立条件とは別である。

---

## 10. Does theoremhood depend on necessity / minimality analysis?

### 10.1 Positive proof and minimality ask different questions

一つの proof \(\pi\) は

\[
\exists\pi\;\mathrm{Proof}_R(\pi,\Gamma,\varphi)
\]

を witnessする。これに対して assumptions/resourcesの minimalityは、subtheories、alternative proofs、models等を比較する別の問いである。

例えば「\(\Gamma\) の全要素が必要」は、各 \(\gamma\in\Gamma\) について \(\Gamma\setminus\{\gamma\}\nvdash_R\varphi\) を示すような universal/comparative claimを含む。positive derivation一本では答えられない。

### 10.2 Four controls

- **\(1+1=2\):** direct proofは derivabilityをsettleする。Add-0/Add-Sや numeral definitionsのexact minimal presentationを決める必要はない。
- **Commutativity:** induction-free countermodelは induction supportに関する追加 evidenceを与えたが、これは positive theoremhoodとは別の model-theoretic analysisである。
- **IVT:** completenessが displayed/expanded proofsに現れても exact theorem-level necessityが未決のまま、IVTの theoremhoodは成立していた。
- **FTA:** compactness、completeness、Cauchy theory、winding theoryの exact necessityを確立しなくても、二つの proofsが FTA-rootをsettleした。

従って theoremが “proved” と数えられる前に、all resourcesの necessity、minimal assumptions、weakest base theoryを知らなければならない、という requirementは四例に支持されない。

### 10.3 Important limitation

proof内で実際に引用した lemmaが \(\Gamma,R\) から利用可能であることは確認しなければならない。これはその witnessの **validity** の問題である。全 alternative proofsを横断して lemmaが necessaryかを決めることは **minimality / necessity** の問題であり、別である。

---

## 11. Does theoremhood depend on canonical proof equivalence?

各例の positive judgmentを確立するために、二 proofsが “essentially the same” かを決める必要はなかった。

- commutativityの \(x\)-inductionと \(y\)-inductionが variable renaming以上に違うか。
- IVTの supremum proofと connectedness proofが imported citationsを展開するとどこまで同じか。
- FTAの analytic proofと topological proofが foundationまで下げると共通化するか。

これらは proof calculus、proof terms、normalization、permitted bureaucracy、equivalence relationを固定して初めて precise questionになり得る。しかし、どの criterionも FTA/IVT等の theoremhoodの前提ではなかった。

従って supportedなのは

> A canonical proof-equivalence relation is not required merely to establish
> that at least one valid proof exists.

という限定的 statementである。「proof identityは原理的に不可能」「canonical proofは存在し得ない」という一般命題は導かない。

---

## 12. First structural question

問いは次だった。

> Does theoremhood require completion of the whole dependency structure,
> or only completion of a derivability judgment in a fixed context?

四例が支持する答えは後者である。ただし “completion of a derivability judgment” は、選んだ proof witness自体の open obligationsを放置してよいという意味ではない。

### Required for the positive judgment

- \(\mathcal L,\Gamma,R,\varphi\) が十分明確である。
- 少なくとも一つの candidate \(\pi\) の各 step / citationが \(R\) と \(\Gamma\) の下で正当化される。
- \(\pi\) の conclusionが target \(\varphi\) である。

### Not required for that judgment

- all proofsの enumerationまたは分類
- proof uniqueness / canonicality
- every resourceの theorem-level necessity
- minimal/weakest \(\Gamma\)
- foundation choiceの最終正当化
- complete historical/provenance record
- best、most natural、most explanatory proofの決定

従って標準語での最終 statementは次に尽きる。

> A theoremhood judgment may be settled while questions about proof choice,
> dependency minimality, alternative foundations, presentation, and formation
> history remain unsettled.

ここから theoremの essence、hidden core、metaphysical closureについて何も推論しない。

---

## 13. Strong falsification questions

### Q1. Does every example show theoremhood with some open remainder?

**YES.** 各例で少なくとも proof/presentation choiceと background-choice explanationが judgmentに含まれない。

### Q2. Can at least one remainder be varied while theoremhood survives?

**YES in all four.** inline/lemma、induction organization、supremum/connectedness、Liouville/windingを同じ context/target内で交換できる。

### Q3. Is the remainder merely lack of information, or genuinely not encoded by theoremhood?

**Not encoded by the bare judgment.** \(\Gamma\vdash_R\varphi\) は proof witnessの存在を主張するが、chosen witness、history、minimality claimを fieldとして持たない。ただし、それらが外部的に unknownとは限らない。

### Q4. Does theoremhood require proof uniqueness?

**NO.** 複数 witnessesがある casesでも同じ judgmentが成立する。

### Q5. Does theoremhood require minimal assumptions?

**NO.** 有効だが冗長な \(\Gamma\) からも derivability judgmentは成立する。minimalityは別の comparative propertyである。

### Q6. Does theoremhood require theorem-level necessity analysis?

**NO.** IVT/FTAが最も明瞭な controlsである。

### Q7. Does theoremhood require a canonical proof-equivalence relation?

**NO for existence of a proof.** 特定の proof-classification taskには必要になり得る。

### Q8. Does theoremhood require full formation history?

**NO.** valid derivationと discovery/edit historyを分ける。

### Q9. Does theoremhood require foundational completion?

**NO.** fixed contextへの相対的 derivabilityで足りる。foundationの整合性・soundness等を別目的で問うことは妨げない。

### Q10. Does bespoke language erase without loss?

**YES.** 結果は ordinary derivability、multiple proofs、proof validity、assumption minimality、proof identity、historical recordの区別で完全に書ける。

---

## 14. Kill criteria

### 14.1 Triggered negative results

- **“Closure” as added mathematics — KILL.** fixed-context derivability以上の operatorや propertyは得られない。
- **Open remainder as a new object — KILL.** judgmentが答えない別 questionsの plain-language集合にすぎない。
- **Hidden essence / true core search — KILL.** 四例はその必要を示さない。
- **Unknown / unknowable reading — KILL.** judgment silenceは epistemic impossibilityでない。
- **Canonical hierarchy of openness — KILL.** O1–O3はチェック用の非網羅的区別に留まる。

### 14.2 Did the pilot collapse to “a theorem can have multiple proofs”?

**Largely, but not entirely.** O1だけならその textbook factの再記述である。O2は positive derivabilityと minimality/necessity analysisの論理形式の差、O3は fixed contextと context-selection explanationの差を加える。しかしこれらも標準的 distinctionsであり、noveltyはない。

### 14.3 Non-triggered control

“no example shows a varying remainder” はtriggerされない。四例すべてに actual variationがある。しかも primary controlsでは theorem、theory、targetを保った。従って pilotは arbitrary ignoranceの列挙だけにはcollapseしなかった。

### 14.4 Overall kill verdict

新しい theory/anatomyとしては **KILL**。standard theoremhoodの情報境界を確認する audit checklistとしては **RETAIN, modestly**。最強の結果は positive structureではなく、何を theoremhoodへ要求してはいけないかという negative clarificationである。

---

## 15. Compare with the previous phase

### Previous phase

前段階は次を問うた。

> What happens when proof resources, assumptions, theories, structures, or
> interpretations are altered?

そこで残ったのは、specific proof failure、non-derivability、hypothesis counterexample、setting changeに異なる evidenceを要求する standard audit disciplineだった。project-local rewriteと vocabularyは closure noteで retiredされた。

### This pilot

本 pilotは変更操作から出発しない。先に \(\Gamma\vdash_R\varphi\) が成立しているとし、次を問う。

> After theoremhood is already established, which adjacent questions need not
> be answered for that judgment to stand?

答えは proof choice、minimality/necessity、background rationale、canonical equivalence、formation historyである。previous phaseの retirementを取り消さず、標準 derivability judgmentの主張範囲を監査しただけである。

### Relation without revival

previous stress recordsは concrete variationsの evidence sourceとして参照した。しかし、その旧 framingを説明原理として再導入していない。“theorem closure” も replacement vocabularyではなく、この pilotの問いを短く表す仮題に留まる。

---

## 16. Final report

1. **Exact working question:** fixed-context theoremhoodが確立した後も、proof choice、dependency minimality、foundation/presentation choice、historyは未決であり得るか。
2. **\(1+1=2\):** same arithmetic judgmentを inline calculationと derived-lemma-mediated derivationが witnessする。theoremhoodはどちらを選ばない。
3. **Addition commutativity:** induction on \(x\)/\(y\)、named/helper-inline organizationが変わっても same judgmentが残る。proofsが homologousであるという prior negativeも保持する。
4. **IVT:** supremum proofと connectedness proofが同じ real theoremを証明する。citation expansionと completeness necessityの決定は theoremhoodに不要。
5. **FTA:** Liouville/Cauchyと winding/coveringという異なる theorem librariesが同じ complex root-existence judgmentを証明する。major resource necessityは未決のままでよい。
6. **What theoremhood settles:** fixed \(\mathcal L,\Gamma,R,target\) に対し少なくとも一つの valid derivationが存在し、targetが derivableであること。
7. **What it does not settle:** chosen/unique/canonical/best proof、minimal assumptions、all-proof resource necessity、weakest foundation、presentation rationale、formation history、motivation。
8. **Strongest varying remainder:** FTAの Liouville/Cauchy proofと winding/covering proof。same setting/targetのまま proof witnessと直接使用する theorem libraryが大きく変わる。
9. **Does theoremhood require whole dependency closure?:** **NO.** chosen proofの dependenciesは正当化が必要だが、all proofsや resource minimalityの完全分析は不要。
10. **Does it require foundational closure?:** **NO.** derivabilityは fixed contextに相対して評価できる。
11. **Does it require proof-history closure?:** **NO.** valid proof recordと discovery/formation historyは別である。
12. **Does it require minimality / necessity analysis?:** **NO.** positive witnessと universal/comparative necessity claimは別問題である。
13. **Strongest negative result:** “theorem closure” と “open remainder” は standard derivability judgmentの情報内容を越える新概念を一切生まなかった。
14. **Strongest surviving methodological observation:** proof validityに必要な unresolved obligationと、theoremhoodがそもそも答えない adjacent questionを明示的に分けると、minimalityやhistoryを proof completionの条件と誤認しにくい。
15. **Is a second pilot warranted?:** **NO by default.** 四例すべてで working hypothesisは確認され、数学的新規性はnegativeだった。variationを増やすだけなら反復になる。
16. **Next falsification question, if any:** judgmentを proof term、minimality clause、または fixed-base-theory strength claimまで明示的に強化したとき、現在 “not settled” とした項目は judgmentの一部へ移り、open/settled distinctionが judgment-relativeだったことを確認できるか。この問いを precise formal settingで事前固定する場合だけ次 pilotに値する。

### Closing verdict

四例は一貫して次を支持した。

> A derivability judgment can be settled without settling every question about
> its proofs, dependencies, foundations, presentation, or history.

しかし、これは ordinary logic of derivability judgmentsの範囲を出ない。theoremhoodは fixed context内の derivabilityをsettleする。周辺の比較・説明・歴史問題を自動的にはsettleしない。それ以上の “closure” theoryは不要であり、retired済みの旧 rewriteも復活しない。

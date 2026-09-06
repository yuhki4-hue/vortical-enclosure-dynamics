# Theorem judgment enrichment boundary pilot v0.1

## 0. Status / posture

本稿は次の地位に限定される。

- **exploratory pilot**
- **not a theorem**
- **not a new proof theory**
- **not a new semantics**
- **not a closure calculus**
- **not a hierarchy of theoremhood**
- **not a displacement theorem**
- **not an infinite-regress theorem**
- **no score**
- **no geometry / topology of proofs**
- **no metaphysical conclusion**
- **no VED claim**
- **reachability-oriented vocabulary remains retired**
- **prefer standard terminology whenever possible**

今回の目的は “open questions always move outward” を証明することではない。次も探さない。

- hidden essence
- true core
- final boundary
- ultimate foundation
- intrinsic proof identity
- canonical minimal theory

“judgment enrichment” は、もとの formal statementに情報を明示的に加える、という平易な working phraseに限る。新 technical apparatusではない。中心問いは次である。

> If one item left unspecified by a derivability judgment is explicitly added
> to the judgment, what becomes settled, and what additional specification is
> required to make the stronger judgment precise?

先に結論を述べる。

- proof witnessを raw proof representationまで指定すれば、どの represented witnessを指定したかはsettleする。ただし proof syntax、calculus、citation policyを固定する必要がある。proof equivalenceは比較したい場合にだけ生じる別問題で、J1のvalidityに必須ではない。
- addition commutativityでは、三 resource blocks \(\{\mathrm{Add0},\mathrm{AddS},\mathrm{Ind}\}\) と complete block deletionを固定すれば、既存 countermodelsにより deletion-minimalityはsettleする。しかし arbitrary weakeningや weakest theoryはsettleしない。
- 新しい未決問題が必ず発生する、無限に外側へ移動する、という結果は得られない。一度 representation / comparison classを固定すれば enriched judgmentはordinaryでpreciseである。

最強の negative resultは、全 exerciseが textbook facts about proof predicates, syntactic identity, equivalence relations, and minimal elements in a chosen orderへ無損失で戻ることである。

---

## 1. Starting point from the previous pilot

前 pilotは standard derivability judgment

\[
J_0:\quad \Gamma\vdash_R\varphi
\]

について、次を確認した。

- \(J_0\) は fixed \(\Gamma,R,\varphi\) の下で少なくとも一つの valid derivationが存在することをsettleする。
- \(J_0\) 単独は chosen proof witness、proof identity、minimal assumptions、proof-resource necessity、canonical proof equivalence、foundation choice、formation historyを指定しない。
- これらが \(J_0\) に含まれないことは、それらが mathematically unknowableという意味ではない。

今回の working formは

\[
J_0\longrightarrow J_1
\]

であり、\(J_1\) は \(J_0\) に欠けていた情報を明示的に含む。各 enrichmentで次の四点を別々に監査する。

1. former unspecified itemは本当にsettledしたか。
2. 何をadded specificationとして加えたか。
3. \(J_1\) をwell-definedにするため何を追加固定したか。
4. \(J_1\) がなお答えない別問題はあるか。

第4点がyesでも「新しい open question must appear」「problem moved outward」とは推論しない。単に \(J_1\) のcontent外に別questionがある場合と、\(J_1\) 自体のwell-definednessに specificationが必要な場合を分ける。

---

## 2. Only two enrichment types

### E1. Proof-witness enrichment

\[
J_0:\Gamma\vdash_R\varphi
\]

から、proof-object representation \(\mathcal P\) と coding / citation policy \(C\) を固定して

\[
J_1:\mathrm{Proof}_{R,\mathcal P,C}(\pi,\Gamma,\varphi)
\]

へ進む。これは「\(\pi\) が指定した representationにおいて \(R\)-validな proof objectで、premises \(\Gamma\)、conclusion \(\varphi\) を持つ」という standard proof predicateである。

### E2. Minimality enrichment

positive judgmentに、明示された comparison classでの minimality clauseを加える。本 pilotの具体形は、addition commutativity theoryを三つの resource blocksに分けた有限 deletion testである。

\[
J_1:\quad
\Gamma_+\vdash_R\mathrm{Comm}
\quad\land\quad
\bigwedge_{B\in S_{\mathrm{test}}}
(\Gamma_+\setminus B)\nvdash_R\mathrm{Comm}.
\]

ここで \(S_{\mathrm{test}}\) と “\(\setminus B\)” の意味はSection 5で固定する。これを general minimalityや weakest-base claimへ拡張しない。

---

## 3. Existing cases and evidence restriction

新しい theoremは追加しない。

- proof-witness enrichmentの主 case: IVT。
- minimality enrichmentの主 case: addition commutativity。
- \(1+1=2\) はraw syntax / macroの trivial controlに限る。
- FTAは異なる theorem librariesを持つ補助 comparisonに限る。

既存 filesはinformal mathematical proofsを記録しているが、特定 proof assistantのmachine-checkable proof termsを含まない。従って次を守る。

- displayed proof recordを指定した、とは言える。
- chosen formal representationの下でどの distinctionが生じるか、conditionalに言える。
- actual formal proof termsが syntactically equal / definitionally equal / normalized equalだという実証 claimは作らない。
- addition countermodelsは既存 testで完全に与えられているので、新 modelは作らない。

---

## 4. Test A — Proof-witness enrichment

### A1. J0

primary IVT formを固定する。standard \(\mathbb R\) 上で continuous \(f:[a,b]\to\mathbb R\)、\(f(a)<0<f(b)\) なら \(\exists c\in(a,b)\,f(c)=0\) である。背景と hypothesesを \(\Gamma_{\mathrm{IVT}}\)、targetを \(\varphi_{\mathrm{IVT}}\) とする。

\[
J_0:\quad
\Gamma_{\mathrm{IVT}}\vdash_R\varphi_{\mathrm{IVT}}.
\]

#### Open item in J0

\(J_0\) は proof existenceをassertするが、既存の supremum proofと connectedness proofのどちらを指定したかを記録しない。

### A2. Added specification and J1

まず document-level witnessを

\[
\pi^{\mathrm{disp}}_{\sup}
\]

と名づける。これは既存 IVT testの displayed supremum proof、すなわち

\[
N=\{x\in[a,b]:f(x)<0\},\quad c=\sup N,
\]

として endpointを処理し、continuityにより \(f(c)<0\) と \(f(c)>0\) を排除する記録である。

proof representation \(\mathcal P_{\mathrm{disp}}\) を「formula / subclaim nodes、rule or theorem labels、ordered parent linksを持つ finite proof tree」、citation policy \(C_{\mathrm{black}}\) を「既に \(R,\Gamma\) で利用可能な named theoremを labelled citation nodeとして許す」と仮定する。この条件下で enrichmentを

\[
J_1:\quad
\mathrm{Proof}_{R,\mathcal P_{\mathrm{disp}},C_{\mathrm{black}}}
(\pi^{\mathrm{disp}}_{\sup},
 \Gamma_{\mathrm{IVT}},
 \varphi_{\mathrm{IVT}})
\]

と書ける。

#### What became settled

- which displayed proof record? — **the designated supremum record** と答えられる。
- \(J_0\) より、witnessの構成 nodesと citation boundaryに関する情報が増えた。
- raw tree/codeを完全に固定すれば、その exact syntactic objectがvalidかを問える。

ただし本稿は machine encodingを作成していない。従って上の \(J_1\) は proof representationを固定した場合のprecise schemaであり、既存 Markdown proofが特定 proverでtype-checked済みだとは主張しない。document levelで実証できる positive controlは「supremum proofを明示的に選んだ」までである。

### A3. Individuation stress

| variation | raw syntactic object | same under an additional criterion? | current evidence |
|---|---|---|---|
| supremum proof vs connectedness proof | different displayed trees | no criterion fixed; do not say “essentially different” | two organizations actually recorded |
| named citation vs cited proof inline | different trees/codes | may be identified by a citation-expansion relation | conceptual only; no formal terms |
| helper lemma as macro vs expanded steps | different raw syntax | may be identified by macro-expansion equivalence | \(1+1=2\) / commutativity provide controls |
| alpha-renaming of bound variables | different raw strings | same modulo alpha-equivalence if chosen | conceptual standard fact |
| bureaucratic rearrangement of independent steps | possibly different sequences/trees | depends on permutation/conversion relation | not formally tested here |
| proof before vs after normalization | possibly different terms | same normal form only in a specified calculus with stated properties | OPEN for these informal proofs |

従って “same \(\pi\)” には少なくとも二つの読みがある。

1. exact raw representation equality。
2. equivalence class under a chosen relation \(\sim\)。

前者は representationを固定すればordinary syntactic identityとしてdeterminateになる。後者は \(\sim\) を定義しなければ未定義である。これは proofにintrinsic identityがある/ないという ontologyの結果ではない。

### A4. Evidence burden

次を分ける。

| claim | required evidence |
|---|---|
| one concrete proof object is valid | fixed syntax/calculusで全 nodesの rule check |
| two proof objects are syntactically distinct | fixed codingで raw objectsが unequal |
| two proofs are equivalent under \(\sim\) | \(\sim\) を定義し、pairが relationを満たすことを示す |
| two proofs are “essentially the same” | “essentially” のcriterionが必要。未指定ならclaimを使わない |

\(J_1\) のvalidityは raw proof objectを一つ指定すれば問える。proof equivalenceは複数 objectsを比較したい場合にだけ追加される independent questionである。従って enrichmentが必ず equivalence problemや次の specificationを生成するわけではない。

### A5. FTA auxiliary comparison

FTAの Liouville/Cauchy proofと winding/covering proofは、IVT以上に異なる displayed theorem librariesを使う。proof-object enrichmentで片方の raw representationを指定すれば “which displayed witness?” は同様にsettleする。しかし formal equivalenceについては calculusも relationもないため何も結論しない。この comparisonは IVT verdictを補強するが、新 theorem testではない。

---

## 5. Test B — Minimality enrichment

### B1. J0

language \(\{0,S,+,=\}\)、ordinary first-order equality calculus \(R\)、successor background、addition equations、full induction schemaを用いる。

\[
\mathrm{Comm}:=\forall x\forall y\,(x+y=y+x),
\]

\[
J_0:\quad\Gamma_+\vdash_R\mathrm{Comm}.
\]

#### Open item in J0

positive derivabilityだけでは、どの axiom/resource blocksを完全削除しても derivabilityが残るかを答えない。

### B2. Preregistered resource presentation

固定 backgroundを

\[
\Gamma_{\mathrm{base}}
=\{\text{logic/equality conventions, successor axioms S0/S1}\}
\]

とする。比較する三 blocksだけを

\[
A_0:=\{\forall x\;(x+0=x)\},
\]

\[
A_S:=\{\forall x\forall y\;(x+S(y)=S(x+y))\},
\]

\[
I:=\{\text{all instances of the specified induction schema}\}
\]

とする。\(I\) は一 formulaではなくschema blockである。

\[
S_{\mathrm{test}}=\{A_0,A_S,I\},
\qquad
\Gamma_+=\Gamma_{\mathrm{base}}\cup A_0\cup A_S\cup I.
\]

“\(\Gamma_+\setminus B\)” は、primitive presentationから block \(B\) 全体を削り、残る axiomsから consequencesを再計算することを意味する。削除前に導出された theoremを新 axiomとして持ち越さない。

### B3. Added specification and J1

enriched judgmentを

\[
\begin{aligned}
J_1:\quad &\Gamma_+\vdash_R\mathrm{Comm},\\
&\Gamma_+\setminus A_0\nvdash_R\mathrm{Comm},\\
&\Gamma_+\setminus A_S\nvdash_R\mathrm{Comm},\\
&\Gamma_+\setminus I\nvdash_R\mathrm{Comm}.
\end{aligned}
\]

とする。これは full theoryのabsolute minimalityではなく、固定した三 block subset comparisonにおける deletion-minimality claimである。

### B4. Existing evidence

既存 addition-commutativity testは各 conjunctを支える。

| deleted block | retained setting / countermodel | Comm | conclusion by soundness |
|---|---|---:|---|
| \(I\) | one standard successor chain plus a bi-infinite chain; Add-0/Add-S hold | false | \(\Gamma_+\setminus I\nvdash_R\mathrm{Comm}\) |
| \(A_0\) | standard \(\mathbb N\), \(a\oplus b=2a+b\); Add-S and induction hold | false | \(\Gamma_+\setminus A_0\nvdash_R\mathrm{Comm}\) |
| \(A_S\) | standard \(\mathbb N\), \(a\oplus b=a\); Add-0 and induction hold | false | \(\Gamma_+\setminus A_S\nvdash_R\mathrm{Comm}\) |

positive conjunct \(\Gamma_+\vdash_R\mathrm{Comm}\) は既存 induction proofがwitnessする。従って \(J_1\) の四 conjunctは既存 evidenceでsupportedである。

### B5. What became settled

- the full three-block node derives Comm。
- each of the three complete single-block deletions does not derive Comm。
- derivabilityのmonotonicityにより、これらの single-deletion theoriesより小さい任意の block subsetも Commをderiveしない。従って \(\Gamma_{\mathrm{base}}\) を固定した \(2^{S_{\mathrm{test}}}\) subset order内では、full nodeがCommをderiveする唯一かつ inclusion-minimalな nodeである。

これは positive controlである。minimalityは固定した有限 comparison classでは完全にsettleし得る。“minimality always escapes” は偽である。

### B6. What had to be fixed

- languageと calculus \(R\)
- fixed base \(\Gamma_{\mathrm{base}}\)
- resource blocksのidentityとgranularity
- inductionを一 blockとして扱う convention
- admissible comparison class \(2^{S_{\mathrm{test}}}\)
- orderを block inclusionとすること
- weakening operationを complete block deletionとすること
- non-derivabilityをmodel + soundnessで評価する metatheoretic background

これらを固定しない bare word “minimal” には、この testで一意な meaningがない。

### B7. What remains unsettled

\(J_1\) は次を答えない。

- induction schemaのproper fragmentでCommを証明できるか。
- \(A_0,A_S\) より弱い equationsや別の recursive axiomatizationで足りるか。
- definitionsを変えた conservative presentationとの strength comparison。
- arbitrary theory weakeningに対する minimality。
- weakest equivalent base theory。
- logical strength under a standard reverse-mathematical comparison。

これらは \(J_1\) のwell-definednessに必要な未充足条件ではない。\(J_1\) はすでにpreciseでtrueである。より広い comparison classを問うなら生じる **separate substantive questions** である。

### B8. Presentation dependence control

deletion-minimalityは theoremのintrinsic propertyではなく、axiom presentationと block partitionに依存する。例えば logically equivalentな冗長 presentation

\[
S'_{\mathrm{test}}=\{A_0,A_0\cup A_S,I\}
\]

を resource-labelled blocksとして採れば、standalone \(A_0\) blockを削除しても conjunction block \(A_0\cup A_S\) 内に同じ equationが残る。この presentationではそのblock deletionはderivabilityを壊さない。

ここで新 theoremや countermodelは不要である。同じ deductive closureを持つ冗長 axiomatizationでも syntactic block-deletion minimalityが変わり得る、という standard factを示している。従って block identity / packagingは specificationの一部である。

### B9. Weakening-order stress

次を自動的に同一視しない。

| question | comparison relation |
|---|---|
| complete deletion | selected blockを丸ごと除く |
| schema restriction | induction instancesのclassを狭める |
| weaker principle | implication / interpretability / proof-theoretic reduction等、事前に固定した order |
| conservative reformulation | theorem setを保つ presentation translation |
| weakest base theory | fixed language/comparison framework内のglobal strength question |

general “minimal under weakening” は allowed weakening relationまたは preorderを指定して初めてdefinedになる。exact preorderを固定すれば、そのposet/preorder内の minimal elementというordinary questionになる。deletion-minimal \(\Rightarrow\) arbitrary-minimal \(\Rightarrow\) weakest baseという推論は成立しない。

---

## 6. Required schema for both tests

| field | E1 proof-witness enrichment | E2 minimality enrichment |
|---|---|---|
| **J0** | \(\Gamma_{\mathrm{IVT}}\vdash_R\varphi_{\mathrm{IVT}}\) | \(\Gamma_+\vdash_R\mathrm{Comm}\) |
| **Open item in J0** | which displayed witness? | which tested blocks survive complete deletion? |
| **Added specification** | designated \(\pi^{\mathrm{disp}}_{\sup}\) | three non-derivability conjuncts |
| **J1** | \(\mathrm{Proof}_{R,\mathcal P,C}(\pi^{\mathrm{disp}}_{\sup},\Gamma,\varphi)\) | positive derivability plus failure after deleting each block |
| **What became settled** | the represented supremum witness is the designated valid witness | deletion-minimality within \(2^{S_{\mathrm{test}}}\) |
| **What had to be fixed** | proof syntax/coding、calculus、citation policy、raw equality convention | base theory、block partition、deletion operation、finite comparison class、inclusion order |
| **What remains unsettled** | equivalence to other encodings if no \(\sim\) is chosen; discovery history | schema fragments、alternative axioms、arbitrary weakening、weakest base |
| **Is remainder substantive?** | equivalence is substantive only if proof comparison is asked; not needed for J1 validity | wider-strength questions are substantive but not missing conditions of the finite J1 |
| **Standard translation** | ordinary proof predicate over a fixed syntax | minimal element / deletion-minimality in a fixed finite subset order |

二 casesとも、added informationはformer unspecified itemを実際にsettleした。ただし何を statementに加えたかが異なる。

- E1は existential derivabilityの witness parameterを明示した。
- E2は positive derivabilityに複数の negative derivability claimsをconjoinした。

J1は “deeper theoremhood” ではなく information contentが異なる stronger statementである。

---

## 7. Main falsification question

candidateは次だった。

> Enriching a judgment can settle a previously unspecified item, but the
> stronger judgment may require additional specification concerning
> representation, equivalence, or comparison class.

### E1 verdict

**Result B**, with a limited **Result C** only if comparison is requested。

- proof representation、calculus、citation policyを固定すれば、raw \(\pi\) のvalidityとidentityはordinary syntactic questionsとしてpreciseになる。
- 別 encodingとの equivalenceを問うなら \(\sim\) が必要になる。これは J1を成立させるための obligationではなく、追加の comparison questionである。

### E2 verdict

**Result B**, followed optionally by **Result C**。

- finite resource blocksと inclusion orderを固定すれば deletion-minimalityはfully preciseで、今回の J1はsettledした。
- arbitrary weakeningや weakest baseを問うなら、新しい comparison relationを指定する別 substantive questionになる。

### Novelty verdict

**Result D also applies at the level of novelty.** 全結果は textbook proof-object syntaxと minimality in a chosen preorderで尽くされる。useful structural residueがあるとしても、「claimの精度に対応する specificationを明記せよ」というaudit reminderだけである。

「新しい specificationが必ず必要」「新しい未決問題が必ず現れる」はfalsifiedされた。raw syntax equalityや固定 finite posetでは、それ以上のquestionを追加せず answerが完結する。

---

## 8. Important controls

### 8.1 Stronger judgment is not deeper truth

J1は J0より多くの conjuncts / parametersを持つ。そこから “deeper”, “closer to essence”, “more fundamental” は導かれない。

### 8.2 Specification is not ontology

\(\mathcal P,C,\sim\) や \(S_{\mathrm{test}}\), inclusion orderを固定することは、proofやtheoremがそれらをintrinsically持つことを示さない。これは問いをwell-definedにするための mathematical setupである。

### 8.3 No infinite regress

本稿で観察したのは最大でも次だけである。

\[
\text{derivability}
\to\text{specified proof predicate}
\to\text{optional proof-comparison question},
\]

または

\[
\text{positive derivability}
\to\text{finite deletion-minimality}
\to\text{optional wider weakening question}.
\]

この有限 sequenceから indefinite continuationは推論できない。実際、raw identityとfinite subset orderでは current questionが完全にterminateした。

### 8.4 Canonical choices remain possible

特定 calculusで normalization theoremやcanonical formsが存在する可能性、特定 comparison frameworkで weakest theoryが存在する可能性を排除しない。本稿はそれらを固定も検査もしていない。

### 8.5 All questions remain mathematical

J0に含まれない proof equivalence、minimal bases、historical formalization等も standard mathematical/historical studyの対象になり得る。“not in J0” は “outside mathematics” ではない。

---

## 9. Explicit proof-witness controls

IVT recordsから次を区別する。

### 9.1 Same theorem, different displayed witness

supremum proofと connectedness proofは同じ \(\Gamma_{\mathrm{IVT}},R,\varphi_{\mathrm{IVT}}\) に対する異なる displayed treesである。\(J_1\) に \(\pi^{\mathrm{disp}}_{\sup}\) を入れることで、どちらをdesignateしたかはsettleした。

### 9.2 Same proof idea, different encoding

supremum proofをlinear sequence、natural-deduction tree、proof term、Markdown paragraphsのどれでencodeするかにより raw objectsは変わる。既存 filesはそれらを横断する formal translationを与えないため、同一 proof objectという実証 claimはしない。

### 9.3 Alpha-renaming

bound variablesだけをrenameした raw stringsはsyntactically distinctになり得る。alpha-equivalenceを representationのequalityに組み込めば同じ equivalence classになる。どちらを採るかを明記すれば questionはpreciseである。

### 9.4 Normalization

“same modulo normalization” は proof calculus、reduction rules、normal formsの存在/一意性を固定して初めて意味を持つ。既存 IVT proofsは formal proof termsでないため、この equivalenceは **NOT TESTED**。

### 9.5 Citation expansion

named theorem citationをatomic nodeとする treeと、そのtheorem proofをinlineした treeはraw syntaxではdifferentである。citation-expansion equivalenceを定義すれば同一視できる場合があるが、本稿は新 relationを発明しない。

### 9.6 Control conclusion

1–5を一つの “proof identity” questionにcollapseしない。raw syntax equalityは固定 representationでanswerable、alpha/normalization/citation equivalenceは各 relationにrelative、informal “essential sameness” はcriterionなしでは使わない。

---

## 10. Explicit minimality controls

addition commutativityについて、既存 evidenceが支える範囲を段階別に固定する。

| level | statement | status here |
|---|---|---|
| 1 | \(\Gamma_+\vdash_R\mathrm{Comm}\) | **ESTABLISHED** by induction proof |
| 2 | tested block \(B\) を一つ削除すると non-derivable | **ESTABLISHED** for \(A_0,A_S,I\) by three countermodels |
| 3 | deletion-minimal over preregistered \(2^{S_{\mathrm{test}}}\) | **ESTABLISHED** using Level 1, Level 2, and monotonicity |
| 4 | minimal under arbitrary weakening | **NOT ESTABLISHED / not yet defined without a comparison relation** |
| 5 | weakest equivalent base theory | **NOT ESTABLISHED** |

Level 3から4/5を推論しない。特に complete deletionと weaker replacementは異なる。\(I\) 全体の削除が failureを生むことは、どの induction fragmentが十分かを答えない。

また deletion-minimalityは resource packagingにsensitiveである。redundant but deductively equivalent presentationでは single-block deletionの結果が変わり得る。これは Level 3が無意味ということではなく、その quantifier domainが selected presentationのblocksだという意味である。

---

## 11. Comparison with the previous pilot

### Previous pilot

前 pilotは次を問うた。

> What may remain unspecified after \(\Gamma\vdash_R\varphi\) is established?

そこで proof choice、minimality、dependency necessity、foundation、history等が positive judgmentにencodedされないことを四例で確認した。

### This pilot

今回はそのうち二つをstatement内へ入れた。

- witness parameter \(\pi\) と proof predicateを加える。
- finite block-deletion non-derivability conjunctsを加える。

結果として former unspecified itemsは限定された意味でsettledした。これは前 pilotの “open remainder” を objectやtechnical categoryへ昇格させるものではない。単に異なる statementsは異なる informationをassertするということを確認した。

retired済みの旧 rewriteは復活させない。本稿の矢印 \(J_0\to J_1\) も calculusや theorem hierarchyではなく、二 statementsの比較表示にすぎない。

---

## 12. Kill criteria

### Triggered

- **“More detailed questions require more detailed definitions.”** 数学的内容の大半はこれにreduceする。novelty claimは **KILL**。
- proof-witness enrichment as new method: ordinary proof-term / proof-predicate syntaxなので **KILL**。
- minimality enrichment as new theory: chosen preorder内のminimality definitionなので **KILL**。
- “boundary”, “displacement”, “closure” as explanatory project vocabulary: **KILL**。standard representation / comparison classで足りる。
- intrinsic proof identityまたは canonical minimal theoryの探索: **KILL** for this pilot。

### Not triggered

- former unspecified itemが一つもsettleしない、はfalse。E1でdesignated raw witness、E2でfinite deletion-minimalityがsettledした。
- alleged new remainderがtheorem/setting changeだけから生じる、はfalse。same IVT/addition judgments内の representation/comparison specificationである。
- infinite regressは推論していない。finite positive controlsで停止した。

### Overall

新しい structural theoryとしては **KILL**。standard claimsのevidence scopeを明示するaudit exerciseとしては **RETAIN modestly**。negative resultを主結果とする。

---

## 13. Strongest possible positive result

四例と二 enrichmentsが支持する最大限のstatementは次である。

> A stronger judgment can settle information left unspecified by a positive
> derivability judgment, but its exact content is relative to explicitly fixed
> choices such as proof representation or the class and order of theory
> comparisons.

さらに具体的には：

- raw proof representationを固定した \(\mathrm{Proof}(\pi,\Gamma,\varphi)\) はchosen \(\pi\) のvalidityをsettleできる。
- finite resource-block subset orderを固定した positive/negative derivability conjunctionは deletion-minimalityをsettleできる。
- proof equivalenceや wider minimalityを問わない限り、追加 specificationを続ける必要はない。

従って以下は支持されない。

- every closure generates a new exterior
- every fixed answer displaces the problem
- theoremhood is essentially incomplete
- no final formalization is possible

---

## 14. Final report

1. **Exact working question:** \(J_0\) が指定しなかった witnessまたはminimality情報を \(J_1\) に加えると何がsettleし、\(J_1\) のprecisionに何を追加固定する必要があるか。
2. **Proof-witness enrichment:** supremum proof recordを \(\pi^{\mathrm{disp}}_{\sup}\) と指定することで “which displayed witness?” はsettledした。exact formal-object validityは chosen syntaxへのformal encodingが必要で、本稿はmachine checkを主張しない。
3. **Minimality enrichment:** \(S_{\mathrm{test}}=\{A_0,A_S,I\}\) のcomplete block deletionsについて、既存 countermodelsにより \(\Gamma_+\) は固定 subset order内で deletion-minimalとsettledした。
4. **What J0 did not settle:** chosen witness、raw proof identity、tested deletionsのnon-derivability、comparison-class-relative minimality。
5. **What J1 settled:** E1ではdesignated represented proof、E2では三 single deletionsと全proper block subsetsでのnon-derivability。
6. **Extra specifications:** E1は proof syntax/coding、calculus、citation policy。equivalenceを問う場合のみ \(\sim\)。E2は fixed base、resource partition、deletion operation、finite comparison class、inclusion order。
7. **Strongest specification dependence:** logically equivalentだが冗長な axiom packagingに変えると syntactic block-deletion minimalityが変わり得る。proof側では citation node対inline treeがraw identityを変える。
8. **Did a genuine new unresolved question appear?:** **Not necessarily.** raw witness validityとfinite deletion-minimalityは各 setup内で完結した。proof equivalence / arbitrary weakeningは選択的に問える別questionsである。
9. **Substantive or definitional?:** representation/comparison classの指定はwell-definednessに必要。そこから先の equivalenceや weakest-base問題はsubstantiveになり得るが、J1のdefectではない。
10. **Standard-language expressibility:** **Complete.** proof predicates、syntactic equality、equivalence relations、theory inclusion、non-derivability、minimal elementsで尽くされる。
11. **Strongest negative result:** “outward movement” も infinite regressも得られず、enrichmentはordinary strengthening of a statementだった。
12. **Strongest methodological observation:** claimを強める際、追加 conjunct/parameterだけでなく、そのquantifier domain、representation、comparison relationを同時に明記すると overclaimを防げる。
13. **Should “judgment enrichment” continue as a working phrase?:** **Only descriptively.** convenient shorthandだが technical termやprogram名にしない。
14. **Is another pilot warranted?:** **NO by default.** proof witnessとfinite minimalityのpositive controls、noveltyのnegative resultが得られた。
15. **Exact next falsification question if pursued:** fixed formal calculus with an existing normalization/equivalence theoremを選び、raw proof-object distinctionが quotient judgmentで本当に消えるかを検査する。この questionを既存 standard formalismで事前固定する場合に限る。

---

## 15. Final self-audit

| check | result |
|---|---|
| Did I accidentally assume outward displacement? | **No.** optional comparison questionsとJ1 well-definednessを分け、finite termination controlsを示した。 |
| Did I turn finite examples into an infinite-regress claim? | **No.** indefinite continuationを明示的に否定した。 |
| Did I confuse a proof representation with the proof itself? | **No.** claimsをrepresented raw objectまたはchosen equivalence classにrelative化した。 |
| Did I confuse deletion-minimality with weakest-theory results? | **No.** finite block subset orderのLevel 3で停止した。 |
| Did I claim formal proof equivalence without a fixed calculus? | **No.** IVT recordsについて normalization等は NOT TESTEDとした。 |
| Did I use new terminology where standard terminology suffices? | **No substantive use.** proof predicate、syntactic identity、preorder、minimalityへ翻訳した。 |
| Did I preserve the previous retirement decisions? | **Yes.** retired framingを復活させず、新 v2/calculusを作っていない。 |
| Did I retain negative results? | **Yes.** novelty、outward-movement、infinite-regress claimsを棄却した。 |

### Closing verdict

proof-witness enrichmentと deletion-minimality enrichmentは、former unspecified itemを実際にsettleできた。ただし答えは proof representationまたは comparison classにrelativeである。一度それらを固定すれば、必ず次の未決問題が生じるわけではなく、ordinary formal questionとして停止できる。

従って今回得られたのは displacement principleではない。より情報の多いstatementには、その情報を解釈する domainとidentity conditionsを明記する必要がある、という標準的な specification disciplineだけである。

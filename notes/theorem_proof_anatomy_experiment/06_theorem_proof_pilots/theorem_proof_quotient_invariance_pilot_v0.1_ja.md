# Theorem / proof quotient invariance pilot v0.1

## 0. Status / posture

本稿は次の地位に限定される。

- **exploratory pilot**
- **not a theorem**
- **not a new proof theory**
- **not a new semantics**
- **not a new proof geometry**
- **not a quotient theory of theoremhood**
- **not an invariant theory of proofs**
- **no score**
- **no metric**
- **no metaphysical conclusion**
- **no VED claim**
- **no claim that quotienting reveals the essence of proof**
- **no claim that a quotient class is theorem-intrinsic**
- **prefer standard proof-theoretic / type-theoretic terminology**

今回の目的は “what is the true proof underneath presentation?” を問うことではない。次も探さない。

- essential proof
- intrinsic proof identity
- canonical proof geometry
- theorem soul/core
- final proof object
- representation-free proof

前 pilotの negative resultsを維持する。stronger statementは、明示的に固定した representationまたは comparison classにrelativeに情報をsettleできる。新しい未決問題が必ず生じるわけではなく、infinite regressは示されず、finite formal questionsは実際にterminateし得る。

今回の中心問いは標準的な quotient languageだけで述べる。

> When a formally specified equivalence relation identifies some proof
> representations, what information is removed by the quotient, and what
> information remains distinguishable?

先に結果を要約する。

- alpha quotientはbound-variable namesだけを消した。
- arrow beta quotientはconstructed redex bureaucracyを消した。
- arrow eta quotientはfree function \(f\) と \(\lambda x.fx\) を同一視した。
- product beta/eta equationsはprojection/pair bureaucracyをさらに消した。
- それでも \(A\times A\to A\) の二 proofs \(\lambda p.\pi_1p\) と \(\lambda p.\pi_2p\) は異なる full quotient classesに残った。

従って unique normal form for each termはunique proof class for each propositionを意味しない。得られるclassificationはchosen calculusとchosen equationsにrelativeであり、theorem-intrinsicな invariantは得られない。数学的内容はstandard simply typed lambda calculus (STLC) with productsの範囲を出ない。

---

## 1. Central question

proof terms \(\pi_1,\pi_2\) と明示された equivalence relation \(\sim\) に対し

\[
\pi_1\sim\pi_2,
\qquad
[\pi]_{\sim}
\]

と書く。これはordinary equivalence class notationである。

primary transformationは

\[
\text{raw syntactic distinction}
\longrightarrow
\text{identification under a chosen quotient}
\]

である。次を別々に検査する。

1. which raw differences disappear?
2. which normal proof terms remain distinct?
3. does a proposition acquire a unique proof class?
4. how does the answer change when the equations change?
5. does any quotient become independent of representation/calculus choice?

quotientがsome distinctionを消すことから、all differences、proof uniqueness、theorem-level canonicality、intrinsic identityは導かない。

---

## 2. Fixed standard calculus

### 2.1 Calculus

simply typed lambda calculus with binary productsを使う。Curry–Howard対応ではtermsをintuitionistic natural-deduction proofsとして読めるが、新 calculusは設計しない。

### 2.2 Types

atomic types \(A,B,C\) から

\[
T,U ::= A\mid B\mid C\mid T\to U\mid T\times U
\]

を作る。

### 2.3 Terms

\[
t,u ::= x
\mid \lambda x:T.t
\mid t\,u
\mid \langle t,u\rangle
\mid \pi_1t
\mid \pi_2t.
\]

### 2.4 Typing rules

standard rulesだけを用いる。

\[
\frac{x:T\in\Gamma}{\Gamma\vdash x:T}\;(\mathrm{Var})
\]

\[
\frac{\Gamma,x:T\vdash t:U}
{\Gamma\vdash\lambda x:T.t:T\to U}\;(\to I),
\qquad
\frac{\Gamma\vdash f:T\to U\quad\Gamma\vdash t:T}
{\Gamma\vdash ft:U}\;(\to E)
\]

\[
\frac{\Gamma\vdash t:T\quad\Gamma\vdash u:U}
{\Gamma\vdash\langle t,u\rangle:T\times U}\;(\times I)
\]

\[
\frac{\Gamma\vdash p:T\times U}{\Gamma\vdash\pi_1p:T},
\qquad
\frac{\Gamma\vdash p:T\times U}{\Gamma\vdash\pi_2p:U}.
\]

### 2.5 Scope

termsはexplicit type annotations付きASTとして扱う。companion checkerはparserやproof searchを持たず、本文で構成した有限termsをtype-checkしてnormalizeするだけである。

---

## 3. Exact equivalence relations

一つの曖昧な “same proof” relationを使わない。比較を分離するため、以下はcumulative levelsとして固定する。

### Q0. Raw syntactic identity

variable names、constructors、tree shape、annotationsまでexactly同じASTであること。\(=_{\mathrm{raw}}\) と書ける。

### Q1. Alpha-equivalence

bound-variable renamingだけを同一視する。free-variable namesやterm constructorsは変えない。

\[
\lambda x:T.t\equiv_\alpha\lambda y:T.t[y/x]
\]

ただしcaptureを避ける。

### Q2. Alpha + arrow beta-convertibility

Q1に standard function beta equation

\[
(\lambda x:T.t)u\to_\beta t[u/x]
\]

を加える。本稿のQ2ではproduct projectionsのbeta equationsをまだ加えない。

### Q3. Alpha + arrow beta/eta

Q2に arrow eta equationを加える。

\[
\lambda x:T.fx\equiv_\eta f
\qquad(x\notin FV(f)).
\]

### Q4. Add product beta/eta equations

Q3に

\[
\pi_1\langle t,u\rangle\to_{\beta\times}t,
\qquad
\pi_2\langle t,u\rangle\to_{\beta\times}u,
\]

\[
\langle\pi_1p,\pi_2p\rangle\equiv_{\eta\times}p
\]

を加える。

従って表中の “Q3” はarrow equationsまで、“Q4” はproduct equationsも含む。alpha、beta、eta、product lawsを一列にcollapseしない。

### 3.1 Standard normalization facts used

このSTLC fragmentのstandard resultとして、well-typed termsはstrongly normalizingで、beta reductionはconfluentであり、beta-normal formはalpha-equivalenceまでuniqueである。standard beta/eta theory with productsにもnormal-form decision proceduresがある。本稿はこれらをexternal textbook resultsとして使い、新たに証明しない。

companion checkerのdeterministic normalizerはconstructed finite termsについてQ2–Q4のoriented equationsを計算する。有限outputからcalculus全体のnormalization theoremを推論しない。

---

## 4. Proposition selection

三つだけ使う。

### P1. Identity

\[
A\to A.
\]

alpha/beta/product-bureaucracyが消えるtrivial control。

### P2. Product commutativity

\[
A\times B\to B\times A.
\]

bound namingとbeta-expanded function applicationを比較する。

### P3. Projection choice

\[
A\times A\to A.
\]

同じ propositionにfull beta/eta quotient後もdistinct normal proofsが残るかを検査する主negative control。これは新しい大 theoremではなく、product eliminationの最小例である。

product associativityとcompositionは追加しない。上の三つでalpha、beta、product equations、multiple normal classesを検査でき、varietyのための追加は不要である。

etaだけをisolateするため、closed propositionsとは別に二つのfixed-context sequentsを補助controlとして使う。

\[
f:A\to B\vdash A\to B,
\qquad
p:A\times B\vdash A\times B.
\]

---

## 5. Explicit proof terms and typing

### 5.1 P1 terms

\[
I_x=\lambda x:A.x,
\qquad
I_y=\lambda y:A.y.
\]

Varと\(\to I\) により両方とも \(\vdash A\to A\)。

\[
I_\beta=\lambda x:A.(\lambda z:A.z)x.
\]

inner abstractionは \(A\to A\)、applicationは \(A\)、従って \(\vdash I_\beta:A\to A\)。

\[
I_{\beta\times}=\lambda x:A.\pi_1\langle x,x\rangle.
\]

\(x:A\vdash\langle x,x\rangle:A\times A\)、従って projectionは \(A\)、全体は \(A\to A\)。

### 5.2 P2 terms

\[
S_p=\lambda p:A\times B.\langle\pi_2p,\pi_1p\rangle,
\]

\[
S_q=\lambda q:A\times B.\langle\pi_2q,\pi_1q\rangle.
\]

context \(p:A\times B\) では \(\pi_2p:B\), \(\pi_1p:A\) なのでpairは \(B\times A\)。従って両方とも \(\vdash A\times B\to B\times A\)。

\[
S_\beta=
\lambda p:A\times B.
(\lambda q:A\times B.\langle\pi_2q,\pi_1q\rangle)p.
\]

application bodyは \(B\times A\)、従って同じtarget typeを持つ。

### 5.3 P3 terms

\[
F=\lambda p:A\times A.\pi_1p,
\qquad
G=\lambda p:A\times A.\pi_2p.
\]

両 projectionはcontext \(p:A\times A\) でtype \(A\)。従って

\[
\vdash F:A\times A\to A,
\qquad
\vdash G:A\times A\to A.
\]

さらにbureaucratic variant

\[
F_{\beta\times}
=\lambda p:A\times A.
\pi_1\langle\pi_1p,\pi_2p\rangle
\]

も同じtypeを持つ。

### 5.4 Eta and product controls in context

arrow eta:

\[
f:A\to B\vdash f:A\to B,
\]

\[
f:A\to B\vdash\lambda x:A.fx:A\to B.
\]

両termsはbeta-normalだがQ3でeta-equivalent。

product eta:

\[
p:A\times B\vdash p:A\times B,
\]

\[
p:A\times B\vdash\langle\pi_1p,\pi_2p\rangle:A\times B.
\]

両termsはarrow-beta/etaでは同一化されず、Q4のproduct etaで同一化される。

product beta:

\[
x:A,y:B\vdash\pi_1\langle x,y\rangle:A,
\qquad
x:A,y:B\vdash x:A.
\]

Q4のproduct betaで同一化される。

### 5.5 Eta applicability caution

atomic \(A\) を用いたclosed \(A\to A\) termsでは、etaだけの効果をbeta effectからcleanly isolateしにくい。そのためeta controlはfixed context内の \(f\) を使った。contextとtargetをpair内で固定しており、theorem/context changeを隠してはいない。

全16 termsのtypeはcompanion checkerで再検査し、すべてPASSした。

---

## 6. Primary test table

Q2–Q4はSection 3のcumulative relationsである。

| Pair | Raw identical? | Q1 alpha-eq? | Q2 arrow-beta? | Q3 arrow-eta? | Q4 product eqs? | Same sequent target? | Notes |
|---|---:|---:|---:|---:|---:|---:|---|
| \(I_x,I_y\) | no | yes | yes | yes | yes | yes | binder nameだけ消える |
| \(I_x,I_\beta\) | no | no | yes | yes | yes | yes | function beta-redexが消える |
| \(I_x,I_{\beta\times}\) | no | no | no | no | yes | yes | product projection redexはQ4まで残る |
| \(S_p,S_q\) | no | yes | yes | yes | yes | yes | binder rename |
| \(S_p,S_\beta\) | no | no | yes | yes | yes | yes | outer application redex |
| \(F,G\) | no | no | no | no | no | yes | different projections remain |
| \(F,F_{\beta\times}\) | no | no | no | no | yes | yes | product beta bureaucracy |
| \(f,\lambda x.fx\) | no | no | no | yes | yes | yes | arrow eta-only control |
| \(p,\langle\pi_1p,\pi_2p\rangle\) | no | no | no | no | yes | yes | product eta-only control |
| \(\pi_1\langle x,y\rangle,x\) | no | no | no | no | yes | yes | product beta-only control |

raw proof setに同じ quotientを一括適用した有限class countsは次である。

| proposition / constructed set | Q0 raw | Q1 alpha | Q2 arrow beta | Q3 arrow beta/eta | Q4 + product beta/eta |
|---|---:|---:|---:|---:|---:|
| P1: \(I_x,I_y,I_\beta,I_{\beta\times}\) | 4 | 3 | 2 | 2 | 1 |
| P2: \(S_p,S_q,S_\beta\) | 3 | 2 | 1 | 1 | 1 |
| P3: \(F,G,F_{\beta\times}\) | 3 | 3 | 3 | 3 | 2 |

このcountはconstructed finite sample内だけの値であり、各typeの全proof termsをenumerateしていない。scoreやtheorem invariantではない。

---

## 7. Does quotienting yield proof uniqueness?

### 7.1 Accidental positive controls

constructed samplesでは、P1の四termsとP2の三termsはQ4でそれぞれ一classへmergeした。これはselected variantsがbinder namingとreducible bureaucracyだけを違いとしていたからである。

この有限結果から「P1/P2には全体として一proof classしかない」とは推論しない。sample class countとall well-typed termsのclassificationは別claimである。

### 7.2 Negative control: two projections

P3には

\[
F=\lambda p:A\times A.\pi_1p,
\qquad
G=\lambda p:A\times A.\pi_2p
\]

という二つのclosed proof termsがある。両方ともQ4 equationsに関してredexを持たず、alpha-renamingでも一方を他方へ変えられない。

さらに standard set interpretationでatomic type \(A\) を \(\{0,1\}\) と解釈すると

\[
F(0,1)=0,
\qquad
G(0,1)=1.
\]

standard beta/eta/product equationsはこのsemanticsでsoundなので、FとGはQ4-equivalentではない。従って

\[
[F]_{Q4}\ne[G]_{Q4}.
\]

同じ proposition \(A\times A\to A\) に少なくとも二つの quotient classesが残る。

### 7.3 Verdict

\[
\text{quotient by alpha/beta/eta/product equations}
\not\Rightarrow
\text{one proof class per proposition}.
\]

normalizationは各termのrepresentativeを簡約できるが、異なるnormal termsを一つにするとは限らない。

---

## 8. Theorem uniqueness vs proof-class uniqueness

次を区別する。

| claim | P3 status |
|---|---|
| proposition \(A\times A\to A\) is derivable | yes, witnessed by F or G |
| at least one raw proof term exists | yes |
| many raw proof terms exist | yes: F, G, \(F_{\beta\times}\), alpha variants等 |
| one class under a chosen quotient exists | yes, trivially \([F]\) exists |
| exactly one class under Q4 exists | no: \([F]_{Q4}\ne[G]_{Q4}\) |

Curry–Howard readingでtheoremhoodは

\[
\exists\pi\; (\vdash\pi:A\times A\to A)
\]

に対応する。これは

\[
\exists![\pi]_{\sim}\;
(\vdash\pi:A\times A\to A)
\]

を意味しない。proof-class uniquenessはcalculusとequivalence relationを固定した上で別途証明すべき stronger statementである。

---

## 9. Quotient dependence

同じraw termsに異なるrelationsを適用した結果はSection 6のcountsの通り変わる。

- Q0からQ1: \(I_x/I_y\), \(S_p/S_q\) がmergeする。
- Q1からQ2: \(I_\beta\), \(S_\beta\) が各base termとmergeする。
- Q2からQ3: open-context pair \(f,\lambda x.fx\) が初めてmergeする。closed sample countsは今回変わらない。
- Q3からQ4: \(I_{\beta\times}\), \(F_{\beta\times}\)、product eta/beta controlsがmergeする。
- 全levelsで: FとGはdistinct。

従って classificationはchosen relationにrelativeである。

> Quotienting removes exactly those distinctions licensed by the fixed
> equations, together with their congruence/conversion consequences.

これは “everything is relative” を意味しない。fixed syntax + fixed relationではclass membershipはordinary precise mathematical questionであり、checkerもselected pairsについてdeterministic answerを返す。また、relation choiceに依存することから “there is no legitimate quotient” とも推論しない。

---

## 10. Canonical normal-form control

### 10.1 What the standard theorem says

fixed STLC fragmentでstrong normalizationは各well-typed termのreductionが無限に続かないこと、confluenceは異なるreduction sequencesがjoinできることを与える。従ってbeta-normal formはalpha-equivalenceまでuniqueである。

この “unique” のquantificationは

> for each starting term, its beta-normal form is unique up to alpha

である。

### 10.2 What it does not say

それは

> for each inhabitable type, all inhabitants have the same normal form

とは言わない。P3のF/Gは同じtypeを持つ異なるnormal termsなので、直接のcounterexampleになる。

### 10.3 Eta and products

Q3/Q4ではeta/product equationsもorientedしてselected termsをnormalizeした。F/Gには該当redexがなく、set interpretationでも区別される。従ってfull selected quotientでもmultiple classesという結論はnormalizerのstrategy artifactではない。

本稿はuntyped lambda calculus、sum types、dependent types、proof irrelevance、classical control operatorsへ一般化しない。

---

## 11. Quotient erasure test

| quotient | what disappears in the examples | what remains | what must be supplied |
|---|---|---|---|
| Q0 raw | nothing | all naming/tree distinctions | exact AST and annotations |
| Q1 alpha | bound-variable names | redexes、constructors、projection choice | binding structure / capture-avoiding renaming |
| Q2 arrow beta | function redex bureaucracy | product redexes、eta expansions、F/G | arrow substitution and convertibility |
| Q3 arrow beta/eta | function eta expansion | product bureaucracy、F/G | eta side condition and congruence |
| Q4 + product beta/eta | pair/projection introduction-elimination bureaucracy | F/G and any other inequivalent normal inhabitants | product equations and full chosen conversion |

quotientによってintroduceされたのは、新しいproof essenceではなく次のsetupである。

- chosen term syntax and typing calculus
- chosen equations and congruence closure
- chosen treatment of alpha-renaming
- chosen normalization / equality decision procedure

“erasure” はこの表の説明語にすぎず、新operationやcalculus名ではない。

---

## 12. Representation dependence vs quotient dependence

前 pilotで確認した通り、raw proof-object identityはrepresentationに依存する。今回さらに、quotient classificationはequivalence relationに依存することをfinite controlsで確認した。

二つの依存を区別する。

1. **Representation dependence:** linear derivation、tree、lambda term、citation node等、何をraw objectとするか。
2. **Equivalence dependence:** そのraw objects間でalpha、beta、eta、product equationsのどれを同一視するか。

quotientは2の指定に従って1内の一部の差を消すが、representation choiceそのものを自動的に消さない。異なるcalculi間のproof translationやequivalenceは別途定義が必要である。

しかし fixed calculus + fixed relationの内部では、\([\pi]_{\sim}\) はstandard quotient set/classとしてpreciseである。classificationのrelative characterをontological relativismへ拡張しない。

---

## 13. Strongest possible positive result

今回supportedされた最大限のstatementは次である。

> Standard quotients can remove specified representational differences from
> proof terms, while other distinctions remain as distinct equivalence
> classes. The classification is relative to the chosen calculus and
> equivalence relation.

具体的にはQ1がnames、Q2がfunction redexes、Q3がfunction eta expansion、Q4がproduct bureaucracyを消した一方、F/Gのprojection choiceは残った。

ここから次は導かれない。

- quotient reveals the essence of proof
- quotient class is theorem-intrinsic
- proof identity is impossible
- all representation dependence can be removed
- canonical proof does not exist in any system
- theorem has an inherent proof geometry

---

## 14. Strong negative controls

### N1. “Alpha-equivalence reveals proof identity”

**KILL.** Q1が消すのはbound-variable namingだけである。\(I_x/I_\beta\)、product bureaucracy、F/Gは残る。

### N2. “Normalization reveals the unique proof”

**KILL.** F/Gは同じpropositionのdistinct full-normal representativesである。unique normal form per termとunique inhabitant per typeを混同していた。

### N3. “Quotient removes all presentation dependence”

**KILL.** Q1–Q4でclass countsが変わり、raw representationとcalculusも先に固定する必要がある。

### N4. “Remaining classes are essential proofs”

**KILL.** remaining distinctionはQ4で非同一というだけで、essence、naturalness、historical identityを与えない。

### N5. “More quotienting is always better or truer”

**KILL.** stronger relationはmore pairsをidentifyするだけである。何をpreserveすべきかという目的なしにquality orderは生じない。

---

## 15. Comparison with previous phases

### Previous pilot 1

問いは「theoremhood確立後に何がunspecifiedであり得るか」だった。proof choice、minimality、history等がpositive derivability judgmentに含まれないことを確認した。

### Previous pilot 2

問いは「unspecified itemをstronger statementに加えると何がsettleするか」だった。raw witnessやfinite deletion-minimalityは追加setupにrelativeにsettleし、indefinite continuationは必要でないと確認した。

### This pilot

今回はfixed formal terms間のraw differencesをchosen standard equivalenceでidentifyした。消える差と残るclassesをactual typing/normalization controlsで分けた。

これらは新しい “open remainder”, “boundary”, “displacement” のtheoryを構成しない。standard proof termsとquotientsの連続した三つのaudit questionsだっただけである。

---

## 16. Kill criteria

### Criteria check

| criterion | outcome |
|---|---|
| textbook alpha/beta/etaだけで新規性なし | **Triggered for novelty.** 数学は完全にstandard。 |
| no distinct raw pair constructed | not triggered; ten pairsを構成 |
| no multiple quotient-class example | not triggered; P3のF/G |
| quotient choice not fixed | not triggered; Q0–Q4を分離 |
| terms not type-checked | not triggered; rulesとcheckerで全16 termsを確認 |
| informal intuition replaces terms | not triggered for primary controls |
| unique normal form confused with unique proof | not triggered;Section 10で分離 |
| quotient class called intrinsic/essential | not triggered; explicitly rejected |
| new proof geometry invented | not triggered |
| theorem/context silently changed | not triggered; open-context eta controlsはcontextを明記 |

### Overall verdict

新しい proof theory / invariant theoryとしては **KILL**。audit valueは **RETAIN, limited**：equivalenceを名指しせず “same proof” と言うこと、normalizationからproposition-level uniquenessを推論することを実例で防げた。

---

## 17. Concrete executable experiment

companion checker `theorem_proof_quotient_invariance_pilot_v0.1.py` は次を行う。

1. types/termsをstandard ASTとして構成。
2. Var、arrow introduction/elimination、pair、projectionsをtype-check。
3. de Bruijn-style alpha keyでalpha-equivalenceを判定。
4. capture-avoiding substitutionでarrow betaをnormalize。
5. optional arrow eta、product beta/etaを別flagsでnormalize。
6. ten selected pairsと三closed-term groupsのclass countsを出力。

実行：

```bash
python3 notes/theorem_proof_anatomy_experiment/06_theorem_proof_pilots/theorem_proof_quotient_invariance_pilot_v0.1.py
```

observed summary：

```text
TYPE CHECKS: PASS
P1 A->A class counts: 4 | 3 | 2 | 2 | 1
P2 AxB->BxA class counts: 3 | 2 | 1 | 1 | 1
P3 AxA->A class counts: 3 | 3 | 3 | 3 | 2
SELECTED ASSERTIONS: PASS
```

limitations：

- parser、proof search、term enumerationはない。
- deterministic reductionはconstructed termsだけをcheckする。
- calculus全体のstrong normalization/confluenceを有限実行から証明しない。
- output countsをscoreやtheorem propertyとして扱わない。
- informal IVT/FTA proofsのformal equivalenceを判定しない。

---

## 18. Final report

1. **Exact working question:** fixed formal equivalenceがproof representationsをidentifyするとき、何が消え、何がdistinct classesとして残るか。
2. **Fixed calculus:** intuitionistic STLC with arrows and binary products under Curry–Howard。
3. **Fixed syntax:** typed variables、abstraction、application、pairing、first/second projectionsのAST。
4. **Relations tested:** Q0 raw; Q1 alpha; Q2 alpha + arrow beta; Q3 + arrow eta; Q4 + product beta/eta。
5. **Propositions:** \(A\to A\), \(A\times B\to B\times A\), \(A\times A\to A\); eta用に二fixed-context sequents。
6. **Terms:** 16 type-checked terms、ten comparison pairs。identity、swap、two projections、redex/eta variantsをexplicitに構成。
7. **Disappeared under alpha:** \(I_x/I_y\), \(S_p/S_q\) のbinder-name differences。
8. **Disappeared under beta:** \(I_\beta\), \(S_\beta\) のfunction-application redexes。product redexはQ2では消えない。
9. **Disappeared under eta:** \(f\) and \(\lambda x.fx\) under Q3。product etaはQ4でのみ消える。
10. **Multiple classes after quotient?:** **YES.** \([F]_{Q4}\ne[G]_{Q4}\) for \(A\times A\to A\)。
11. **Strongest counterexample to uniqueness:** \(\lambda p.\pi_1p\) and \(\lambda p.\pi_2p\) are distinct full-normal inhabitants of the same type。
12. **Did classification depend on equivalence?:** **YES.** class counts changed at Q1、Q2、Q3 controls、Q4。
13. **Beyond standard proof theory?:** **NO.** standard typing、conversion、normalization、quotient classesで尽くされる。
14. **Strongest negative result:** normalization gives a unique normal form per term, not a unique proof per proposition; no intrinsic proof class emerged。
15. **Strongest audit observation:** state the exact equality/conversion relation before claiming two proof representations are “the same,” and keep inhabitant uniqueness separate from normal-form uniqueness。
16. **Another pilot warranted?:** **NO by default.** requested quotient question has positive and negative controls, and novelty is exhausted by standard theory。
17. **Exact next falsification question if pursued:** in a fixed proof-irrelevant or extensional standard calculus with a published equality theory, does quotienting collapse F/G while preserving decidable type checking, and which information is intentionally lost? Only this precisely fixed comparison would add a new test。

---

## 19. Final self-audit

| question | answer |
|---|---|
| Did I confuse theoremhood with proof-class uniqueness? | **No.** existential inhabitation and unique quotient inhabitant were separated。 |
| Did I confuse normal-form uniqueness with theorem-level proof uniqueness? | **No.** F/G is the explicit control。 |
| Did I treat alpha/beta/eta as one vague relation? | **No.** Q0–Q4 were fixed separately and cumulatively。 |
| Did I call a quotient class intrinsic? | **No.** every class claim is relation/calculus-relative。 |
| Did I use actual formal proof terms? | **Yes.** terms and contexts are explicit。 |
| Were all terms type-correct? | **Yes.** hand derivations and checker both pass。 |
| Did I preserve previous retirement decisions? | **Yes.** no retired framework was revived。 |
| Did I avoid essence language? | **Yes.** all such interpretations were rejected。 |
| Did I retain negative results? | **Yes.** novelty、intrinsic identity、unique-proof claims were killed。 |
| Did I avoid inventing a new theory? | **Yes.** only standard STLC and standard quotient relations were used。 |

### Closing verdict

Chosen quotients removed exactly the licensed syntactic bureaucracy in the constructed terms。They did not turn derivability into proof-class uniqueness。The remaining F/G distinction is a distinction in the fixed STLC equality theory, not an “essential proof” or theorem-intrinsic invariant。

The finite classification terminates once syntax and equations are fixed。No outward-displacement or infinite-regress claim survives。

# Operational rule change と rules-as-data の有限 stress test v0.1

## 0. Status / posture

Status:

- finite rule/state representation stress test
- not a theorem
- not a new operational semantics
- not a new higher-order transition calculus
- not a proof of new-law creation
- not a universal meta-rule reduction
- not evidence for a distinct generative equation
- negative results are primary evidence
- standard transition-system、interpreter、truth-table、trace-equivalence の語彙を優先する

本実験は、stageごとにoperational ruleが変わる記述と、rule codeをstate dataに含めて
fixed interpreter / meta-transitionで処理する記述を有限範囲で比較する。

前実験の判定を維持する。

- distinct generative equation: **NOT ESTABLISHED**
- bounded graph growthはfixed state transitionに埋め込める
- construction order `≠` internal partial order
- metric availability `≠` independent metric freedom `≠` physical space
- standard conceptsで尽くせないresidualが反復しない限りspecial notationを追加しない
- finite positive resultをuniversal generation claimへ拡張しない

関連記録：

- [working note](../generative_law_methodology_working_note_v0.1_ja.md)
- [generative-equation specification](../generative_equation_specification_v0.1_ja.md)
- [evidence-burden table](../generative_claim_evidence_burden_v0.1_ja.md)
- [redescription controls](../redescription_vs_generation_test_v0.1_ja.md)
- [observable-independence test](./observable_independence_finite_model_v0.1_ja.md)
- [graph-growth dual encoding](./graph_growth_dual_encoding_v0.1_ja.md)
- [construction/internal-order test](./construction_vs_internal_order_v0.1_ja.md)
- [relation-to-metric test](./relation_to_metric_boundary_v0.1_ja.md)
- [companion checker](./rule_space_as_data_v0.1.py)

---

## 1. Experiment question

中心問いは次である。

> `R_t≠R_{t+1}` と表示される有限operational-rule changeを、rule identity / behaviorを
> dataとして含むfixed state spaceとfixed meta-transition `M`へ、指定したobservationsを
> 保存して埋め込めるか。その再記述には何をpreloadする必要があり、stage-local
> expressibilityやtype formationの何が保存されないか。

比較するのは次の二記述である。

### Description A — explicit changing rule

\[
A_t=(x_t,R_t),
\qquad
x_t\xrightarrow{R_t}x_{t+1},
\qquad
R_t\to R_{t+1}.
\]

`x_t`はobject state、`R_t`はそのstageでoperationalに利用可能なrule recordと読む。

### Description B — rules as state/data

\[
s_t=(x_t,r_t)\in X\times\mathcal R_{\mathrm{code}},
\]

\[
\mathcal M(s_t)=s_{t+1}.
\]

`r_t`はrule behaviorのcode、`M`はcodeを解釈しobject valueとactive codeを更新するfixed
transitionである。

同じtuple形で書けること自体を結論にせず、translation、traces、rule-change events、
language availabilityを個別に検査する。

---

## 2. Finite object and rule model

### 2.1 Object state

\[
X=\{0,1,2\}.
\]

### 2.2 Base operational rules

\[
r_+(x)=\min(x+1,2),
\]

\[
r_-(x)=\max(x-1,0),
\]

\[
r_0(x)=x.
\]

truth-table codesはそれぞれ

\[
\operatorname{code}(r_+)=(1,2,2),
\]

\[
\operatorname{code}(r_-)=(0,0,1),
\]

\[
\operatorname{code}(r_0)=(0,1,2).
\]

### 2.3 Fixed finite interpreter

任意のunary code

\[
c=(c_0,c_1,c_2)\in X^X
\]

に対し

\[
U(c,x)=c_x
\]

とする。finite unary truth tablesは

\[
|X^X|=3^3=27
\]

個である。`U`のcode syntax、state ordering、valid output setは最初から固定される。

### 2.4 Active-rule update

current ruleを適用して得た値を `x'` とし、

\[
r'=
\begin{cases}
r_- & x'=2,\\
r_+ & x'=0,\\
r   & x'=1
\end{cases}
\]

とする。このboundary-switch policyが本modelのfixed meta-rule `M`である。

---

## 3. Encoding A — explicit changing rule record

core controlではactive rule setをsingletonとして

\[
A_t=(x_t,\{r_t\})
\]

と読む。実装recordではsingleton bracesを省きlabel `r_t`を保存する。

一stepは

1. stage `t` のrule `r_t`でobject stateを更新する
2. boundary-switch policyで次stageのoperational ruleを更新する

という二component updateである。表示上、

\[
\{r_+\}\neq\{r_-\}
\]

はrule-set changeである。

ただしrecord全体 `(x_t,r_t)` をmathematical stateと見れば、すでにproduct stateの更新として
も読める。このrole distinctionをsyntaxだけで決めない。

---

## 4. Encoding B — fixed higher-order transition

state spaceを

\[
S_B=X\times X^X
\]

とし、stateを `(x,c)` とする。fixed transition `M`は

1. `x'=U(c,x)`を計算
2. fixed boundary policyにより`c'`を選択
3. `(x,c)↦(x',c')`

とする。

object-level active behaviorは変わるが、interpreter `U`、valid code universe `X^X`、boundary
policy、product carrierは変わらない。この意味でBはordinary fixed transition systemで
ある。

---

## 5. Translation A ↔ B and core result

base rule labelsのcodesは互いに異なるため、core repertoire上で

\[
T_{AB}(x,r)=(x,\operatorname{code}(r)),
\]

\[
T_{BA}(x,c)=(x,\operatorname{decode}(c))
\]

がbijectionになる。

checkerは初期state `(0,r+)` から8 transitionsを実行した。

```text
object_trace=[0, 1, 2, 1, 0, 1, 2, 1, 0]
active_rule_trace=[r_plus, r_plus, r_minus, r_minus,
                   r_plus, r_plus, r_minus, r_minus, r_plus]
rule_change_event_steps=[2, 4, 6, 8]
```

reachable core statesは両側4個であり、次がliteralに一致した。

- reachable `(object, active-rule)` states
- one-step translated transitions
- object-value trace
- active-rule trace
- rule-change event positions
- final outcomes at each finite horizon
- A/B round trips

従って、このcore finite classではDescription Aのrule changeはBのordinary state transitionへ
無損失に埋め込まれた。

これはall rule changeについてのclaimではない。

---

## 6. Control A — finite predeclared repertoire

\[
\mathcal R_{\mathrm{base}}=\{r_+,r_-,r_0\}
\]

を最初から固定する。変わるのはactive memberだけである。

この場合、

\[
(x,r)\to(x',r')
\]

は明示したfinite product上のordinary transitionであり、rule activation/changeのための別
equation typeを必要としなかった。

限定的verdict:

> **RULE ACTIVATION WITHIN A PREDECLARED FINITE REPERTOIRE IS ORDINARY
> HIGHER-ORDER STATE TRANSITION IN THIS ENCODING.**

---

## 7. Control B — active rule subsets

single ruleではなく

\[
R_t\subseteq\mathcal R_{\mathrm{base}},
\qquad R_t\neq\varnothing
\]

をstate componentとし、各active ruleからnondeterministic successorを許す。

fixed subset-update policyは、updated object valueが

- `2`なら `{r-,r0}`
- `0`なら `{r+}`
- `1`ならcurrent subsetを維持

とする。

初期 `(0,{r+,r0})` からcheckerは

```text
subset_reachable_states=6
subset_transition_pairs=10
subset_size_enable_disable_controls=True
```

を得た。reachable partには

- multiple applicable rules
- rule-set size change
- rule enable
- rule disable

がすべて現れる。

しかしfixed state space

\[
X\times\mathcal P(\mathcal R_{\mathrm{base}})
\]

とfixed transition relationで完全に記述できる。

---

## 8. Control C — rule parameter update

parameter familyを

\[
r_\theta(x)=\operatorname{clamp}(x+\theta,0,2),
\qquad
\theta\in\{-1,0,1\}
\]

とする。これはそれぞれ `r-`, `r0`, `r+` と同じtruth tableを持つ。

stateを

\[
(x,\theta)
\]

とし、boundaryで `θ`を更新するfixed ruleを置く。checkerは9 possible `(x,θ)` statesの
すべてについて、

\[
T(\operatorname{step}_\theta(x,\theta))
=
\mathcal M(T(x,\theta))
\]

を確認した。

parameter value changeはこのfinite familyではordinary state updateである。parameter domain
自体の拡張、formula syntaxの変更、new arityは別claimである。

---

## 9. Control D — new rule name, definable behavior

fresh symbol

\[
r_{\mathrm{hold\_alias}}
\]

を導入し、

\[
r_{\mathrm{hold\_alias}}(x)=r_0(x)
\quad\text{for all }x\in X
\]

とする。labelsは異なるがtruth tableは同一である。

selected observationsをobject outputsとすると、二ruleはall input statesでbehaviorally
equivalentである。label-to-code translationはこのaliasを入れるとmany-to-oneになり、raw
symbol identityは失うがbehaviorは失わない。

> **NEW RULE SYMBOL DOES NOT IMPLY NEW OPERATIONAL BEHAVIOR.**

これはobservable-independence experimentのexplicit definitional extension controlに対応
する。

---

## 10. Control E — composition-generated rule

new lookup entryを

\[
r_{++}=r_+\circ r_+
\]

とする。そのtruth tableは

\[
\operatorname{code}(r_{++})=(2,2,2).
\]

このtableはbase three rulesのいずれとも同一でなく、`x=0`では

\[
r_{++}(0)=2,
\qquad
r_+(0)=1.
\]

従ってatomic one-step observationではnew behaviorである。一方、

\[
r_{++}(x)=r_+(r_+(x))
\]

なので既存rule algebraからexplicitにderivedできる。

この差はstep granularityに依存する。one macro stepとtwo base stepsを同一時間尺度で比較
するならtrace lengthは異なるが、compositional behaviorは既存である。

Verdict:

> **DERIVED RULE AVAILABILITY, NOT YET INDEPENDENT RULE GENERATION**

### 10.1 Independence relative to a chosen rule algebra

base rulesのcomposition closureは8 truth tablesだった。code

\[
c_{\mathrm{outside}}=(0,0,2)
\]

は27-table universeには属するが、その8-element composition closureには属さない。

これは「base rulesとcompositionだけ」というfixed admissible algebraに相対したbehavioral
independenceを示す。しかし`c_outside`をsystemがendogenously作ったことは示さない。modelerが
codeを追加しただけでも同じ事実が成立する。

---

## 11. Controls F/G — availability and finite repertoire growth

### 11.1 Stage records

stage-local named repertoiresを

\[
\mathcal R_0=\{r_+,r_-,r_0\},
\]

\[
\mathcal R_1=\mathcal R_0\cup\{r_{++}\},
\]

\[
\mathcal R_2=\mathcal R_1\cup\{r_{\mathrm{hold\_alias}}\}
\]

とした。sizesは `3,4,5` である。

### 11.2 Ex-post maximal repertoire

finite run全体のunion

\[
\mathcal R_{\max}=\bigcup_t\mathcal R_t
\]

は5 labelsである。各stage repertoireを5-bit availability vectorとしてencode / decodeでき、
checkerはround tripを確認した。

従ってfinite ex-post recordは

\[
X\times\mathcal P(\mathcal R_{\max})
\]

へ埋め込める。

### 11.3 Four availability statuses

次を同一視しない。

1. **globally coded and active**
2. **globally coded but inactive / stage-locally unavailable**
3. **stage-local languageではill-formedだがmaximal languageにはnameable**
4. **selected meta-repertoire / code typeにも含まれない**

`r++`はBのmaximal encodingではpreloadedされるがstage 0ではunavailableである。stage languageを
`R0`のnamesだけに限定すれば、そのsymbolはill-formedになる。

一方、unary truth-table interpreterを27 tables全部へ広げれば、named `Rmax`外のcodeも実行
できる。binary ruleはunary code type自体には入らず、次節のtype controlを要する。

### 11.4 Epistemic / ontological limit

ex-post unionをmodelerが構成できることは、system自身がfuture repertoireを事前に知っていた
ことや、そのpossibilitiesがphysical ontologyとして存在したことを意味しない。

固定encodingが示すのはrepresentation possibilityであってsystem knowledgeではない。

---

## 12. Control H — syntax / type formation change

### 12.1 Stage-local type change

initial rule typeをunary

\[
r:X\to X
\]

だけとし、later stageでbinary

\[
q:X\times X\to X,
\qquad q(x,y)=\max(x,y)
\]

を許す。

これはunary parameterやmembership bitの変更ではない。arity、well-formed application、input
carrierが変わる。

### 12.2 Fixed tagged encoding

有限controlではcodeを

\[
(\operatorname{arity},\operatorname{truth\ table})
\]

というtagged dataにし、arity 1/2を処理するfixed interpreterとvalidity checkerを最初から
置いた。checkerは

```text
typed_unary_result=2
typed_binary_result=2
stage_arity_growth=[[1], [1, 2]]
arity_checker_rejects_bad_input=True
```

を確認した。

### 12.3 Result

この特定のfinite type extensionはsum/tagged universeへpreloadできる。しかしBは

- arities `{1,2}`
- product input encoding
- both truth-table formats
- arity checker
- dispatcher

を最初から持つ。Aのstage-local formation rule changeとBのfull type universeはliteralには
同じではない。

未知のfuture types、unbounded arity、new value domains、dependent typing等が同様に一つの
finite tag universeへ収まるとは示していない。

---

## 13. Control I — finite universal-style interpreter

`X={0,1,2}`上の全unary deterministic functionsは27 truth tablesとしてenumerateできる。
fixed `U(code,x)`はその全behaviorを実行する。

従ってfinite unary範囲では

> rule behavior change itself can be represented as rule-code state change under a fixed interpreter

が成立する。

ただし次がpreloadedされる。

- finite object carrier and its enumeration
- code length and ordering
- deterministic unary function class
- valid output alphabet
- interpreter semantics
- admissible code class

この27-table resultはcontinuous、stochastic、higher-order、unbounded、self-modifying、new-type
rulesのuniversal interpreterではない。

---

## 14. Exogenous, endogenous, stochastic, and open updates

### 14.1 Exogenous rule change

modelerがschedule `r0,r1,...` を外から指定する。finite known scheduleはschedule pointerと
remaining scheduleをstateへ入れ、fixed executorで再記述できる。ただしそのscheduleの由来は
system dynamicsから説明されない。

### 14.2 Endogenous rule update

core boundary-switch modelでは

\[
r_{t+1}=F(x_t,r_t)
\]

がfixed `F`で決まる。これはBへ完全にencodeできた。

### 14.3 Stochastic rule update

finite kernel exampleとして次rule codesへのprobabilities

\[
P(r_+)=\frac12,
\quad
P(r_-)=\frac13,
\quad
P(r_0)=\frac16
\]

を固定し、sumが1であることを確認した。これはfixed Markov transition kernelとして記述
できる。sample realizationは変わり得るがkernel自体は固定である。

### 14.4 Open rule introduction

available meta-language、code class、type universeで事前enumerationされていなかったruleが
導入されるというstrong claimは、このfinite preloaded experimentでは検査できない。

Status: **OPEN / NOT ESTABLISHED IN THIS MODEL.**

---

## 15. History-dependent rule update

bounded finite controlで

\[
s_t=(x_t,r_t,H_t)
\]

をstateとし、updated history内のvalue `1` の出現回数のparityでnext ruleを選ぶfixed function
を置いた。

同じvisible pair `(x=1,r=r0)`でも、

\[
H_1=(1),
\qquad
H_2=(1,1)
\]

ではnext ruleがそれぞれ`r-`と`r+`になった。

これはhistoryを無視したprojectionではnon-Markovianに見えるが、bounded `H`をstateに含めれば
fixed ordinary transitionになる。

history liftingが可能であることは、historyがphysicalにirrelevantであることも、unbounded
historyをfinite memoryへ常に圧縮できることも示さない。

---

## 16. Behavioral equivalence and rule identity

本testでは

\[
r\sim_{\mathrm{beh}}r'
\iff
\forall x\in X,\ U(\operatorname{code}(r),x)=U(\operatorname{code}(r'),x)
\]

をone-step full-input behavioral equivalenceとする。deterministic repeated applicationでも
同じtraceを与える。

`r_hold_alias ~beh r0`だがlabelsは異なる。従って

\[
\text{rule representation difference}
\neq
\text{behavioral difference}.
\]

また`r++`はone-step behaviorとしてbase labelsと異なるがcomposition-derivedである。さらに
`c_outside`はchosen composition closure外だが、27-table interpreterでは単なるvalid codeで
ある。

従って少なくとも次を分ける必要がある。

- syntactically new label
- behaviorally new truth table
- outside a chosen derivation/composition closure
- stage-locally executable macro
- introduced by an endogenous mechanism

最後のclaimは先の四つから導けない。

---

## 17. Meta-rule recursion control

### 17.1 One-level absorption

object rule changeはfixed `M`のstate transitionへencodeした。

\[
R\text{-change}
\longrightarrow
M\text{-controlled state change}.
\]

### 17.2 Meta-rule change as data

finite controlとして二meta rulesを用意した。

- `bounce`: core boundary-switch `M`
- `keep`: current active ruleを維持するmeta-policy

stateを

\[
(x,r,m)
\]

とし、fixed interpreter `M*`がmeta-code `m`をdispatchする。checkerでは `bounce→keep` の
meta-code updateをordinary state changeとしてencodeできた。

\[
M\text{-change}
\longrightarrow
M^*\text{-controlled state change}.
\]

### 17.3 What remains fixed

この再記述は

- meta-code repertoire `{bounce,keep}`
- dispatch semantics
- `M*` transition
- meta-code validity

を一段上に固定する。

### 17.4 No regress theorem

ここから「必ず無限後退する」「ultimate fixed lawが存在する／しない」のいずれも導かない。
finite known hierarchyを一段上のtagged stateへflattenできたにすぎない。

genuinely open meta-languageやnot-preenumerated interpretersをどう比較するかは **OPEN** である。

---

## 18. Preload audit

rules-as-data encodingが本testの保存結果を得るためにpreloadしたものを列挙する。

| Preloaded item | Role | If omitted |
| --- | --- | --- |
| object carrier `X` | truth-table domain/codomain | code meaningが決まらない |
| rule-code syntax | behaviorをdataとして保持 | arbitrary tokenを実行できない |
| interpreter `U` | code application | codeは単なるdataのまま |
| valid-code checker | malformed codeを排除 | transition domainが曖昧 |
| base/maximal repertoire | name/availability comparison | stage union encodingが未定義 |
| parameter domain | `rθ` family | parameter update scopeが未定義 |
| allowed arities/types | tagged dispatch | type-change controlをencode不能 |
| meta-transition `M` | object/rule update | endogenous change ruleが未指定 |
| meta-interpreter `M*` | meta-code execution | meta-rule changeをdata化できない |
| history bound/format | history-sensitive state | finite checker scopeを越える |

preloadingはmathematical representation conditionであり、systemがfuture possibilitiesを
知ること、またはphysical ontologyとして所有することを意味しない。

---

## 19. Preservation table

| Item | Core A↔B | Larger controls | Qualification |
| --- | --- | --- | --- |
| object state | preserved/reflected | preserved where translation fixed | common `X` |
| reachable `(x,r)` states | bijective | conditional | core base codes unique |
| one-step transitions | preserved/reflected | conditional | same fixed policy |
| object trace | preserved | preserved | selected finite horizons |
| active-rule trace | preserved | bitset/code translation | labels may alias |
| rule-change events | preserved | preserved if availability record retained | event definition fixed |
| raw rule symbol identity | preserved in core | **not preserved** with aliases | label→code many-to-one |
| behavior | preserved | truth-table equality | finite `X` only |
| stage-local availability | explicit in A | recoverable by availability bits | full B language preloads names |
| stage-local well-formedness | **not literal** | needs language policy | inactive `≠` ill-formed |
| type formation change | not in core | encoded only with preloaded tagged types | arbitrary new types untested |
| history dependence | preserved after state lifting | bounded example | projection loses `H` |
| meta-rule change | finite code translation | two meta codes only | `M*` remains fixed |

---

## 20. Evidence-burden audit

| Claim | Evidence supplied | What it establishes | What it does not establish |
| --- | --- | --- | --- |
| core A/B are equivalent | explicit bijection + traces + reachable states | this finite encoded process | all rule change reduces |
| subset enable/disable is state | six states / ten transitions | finite powerset encoding | unbounded rule creation |
| parameter update is state update | commutation on all nine `(x,θ)` pairs | selected family | syntax/type changes are parameters |
| alias is behaviorally redundant | equality on all three inputs | exact finite behavioral equivalence | labels/provenance are irrelevant under all observations |
| `r++` is derived | explicit composition identity | behavior in base composition algebra | endogenous creation mechanism |
| outside-closure behavior exists | 8-table closure vs code `(0,0,2)` | independence relative to chosen algebra | generation of that code |
| finite repertoire growth embeds | bitset round trips for sets of sizes 3/4/5 | ex-post finite representation | system foreknowledge or open-ended repertoire |
| binary rule can be coded | tagged arity1/2 interpreter | this finite type universe | arbitrary future type formation |
| history dependence can be lifted | explicit bounded `H` state | selected finite update | all history has finite sufficient statistic |
| meta change can be coded | two meta codes under `M*` | one finite higher level | universal fixed interpreter or infinite regress |
| new law was generated | no sufficient evidence | nothing positive | mechanism, open novelty, universality |

禁止する推論：

\[
R_t\neq R_{t+1}
\centernot\Rightarrow
\text{a new law was generated},
\]

\[
\text{one finite rules-as-data encoding exists}
\centernot\Rightarrow
\text{all rule generation is reducible},
\]

\[
\text{the encoding fixes a meta-level}
\centernot\Rightarrow
\text{an ultimate fixed law exists physically}.
\]

---

## 21. Hypothesis verdicts

### H-RULE1

> operational rule change is always mathematically distinct from state change.

**KILL.** core rule activation、subset enable/disable、parameter updateはproduct/powerset stateの
ordinary transitionsとしてencodeできた。“always”に対するfinite counterexampleである。

### H-RULE2

> finite rule change can be represented as ordinary state change in a fixed higher-order state space.

**RETAIN WITH SCOPE.** core、subset、parameter、finite repertoire、tagged type、bounded history、
two-meta-rule controlsでwitnessを構成した。arbitrary finite systemの一般定理ではない。

### H-RULE3

> if traces and rule-change events are preserved, a distinct equation type is unnecessary for that encoded class.

**RETAIN WITH SCOPE.** core classではstandard transition systemが指定した全behavioral recordsを
保持した。language/provenanceなどtarget外の情報まで不要とは言わない。

### H-RULE4

> rules-as-data encoding preloads a rule representation language, interpreter, and candidate repertoire.

**RETAIN WITH SCOPE.** 本encodingでは明示的に必要だった。別encodingで同一listがnecessaryと
いうuniversal claimではない。

### H-RULE5

> inactive-but-preloaded rules are equivalent without qualification to rules unavailable in the stage language.

**KILL.** full code languageではfuture codeをreferできるがstage-local languageではill-formedに
できる。availability observationと言語policyを固定した場合にだけequivalenceを論じられる。

### H-RULE6

> a fixed meta-rule suffices to encode endogenous finite rule updates.

**RETAIN WITH SCOPE.** `r'=F(x,r)`、bounded `F(x,r,H)`、finite stochastic kernelをfixed transition /
kernelとして書けた。open-ended rule introductionは含まない。

### H-RULE7

> change of the meta-rule itself establishes a distinct generative equation.

**KILL as an inference.** two meta rulesのchangeはfixed `M*`のstateとしてencodeできた。任意の
meta-rule hierarchyを一つに吸収できるかは **OPEN / NOT ESTABLISHED**。

### H-RULE8

> parameter change, rule-symbol addition, and rule-type formation change are the same novelty.

**KILL.** parameter value、definitional alias、composition macro、availability、arity/type formationは
異なるsource/target dataとpreservation conditionsを持つ。

### H-RULE9

> behaviorally distinct rule action implies endogenous rule generation.

**KILL.** `r++`はbase rulesとone-step behaviorが異なるがcomposition-derivedである。またclosure外
codeもmodelerが外から指定でき、mechanismを示さない。

### H-RULE10

> all rule-space growth universally reduces to fixed-state dynamics.

**NOT ESTABLISHED.** finite predeclared codesについてのpositive encodingsしかない。open rule
language、unbounded type formation、unknown interpretersへのuniversal quantificationを検査していない。

---

## 22. Strongest results

### 22.1 Strongest equivalence result

predeclared finite unary repertoireとfixed endogenous switch policyでは、explicit rule-change
recordとtruth-table-code stateの間にbijectionがあり、reachable states、object traces、rule
traces、change eventsがすべて保存・反映された。subset、parameter、bounded historyもstandard
state liftingで扱えた。

### 22.2 Strongest nonequivalence result

full fixed encodingはcode syntax、future repertoire、interpreter、allowed typesをpreloadする。
stage-local rule symbolのill-formednessやtype formation changeは、availability bitだけのstate
translationではliteralに保存されない。policy/tagged universeを追加すればrecoverできるが、
その追加自体がcomparison specificationである。

### 22.3 Strongest negative result

finite rule activation、enable/disable、parameter adaptation、definitional alias、composition macro、
bounded history dependence、finite meta-rule switchingのいずれもdistinct generative equationを
必要としなかった。standard transition/interpreter descriptionsで十分だった。

同時に、これをall rule-space growthのreductionへ一般化する証拠も得られなかった。

### 22.4 Best false-positive control

`r++=r+∘r+`が最も明瞭である。new symbol、new stored entry、new atomic one-step behaviorを持つが、
behaviorは既存rulesからexplicitにderivedされる。visible newnessをendogenous new-law creationと
誤認する推論を阻止する。

---

## 23. Checker

[rule_space_as_data_v0.1.py](./rule_space_as_data_v0.1.py) はPython standard libraryだけを使い、
次をassertする。

- 3 object states、27 unary truth tables、fixed interpreter
- core A/B translations and round trips
- four reachable core states
- object / active-rule traces and rule-change events
- active subset systemの6 states / 10 transition pairs
- all nine parameter statesのcommuting translation
- exact behavioral alias
- composition-derived code `(2,2,2)`
- base composition closure size 8 とclosure外code `(0,0,2)`
- stage repertoire sizes `3,4,5` とavailability bitset round trips
- unary/binary tagged interpreter and arity rejection
- bounded history-sensitive next-rule difference
- finite stochastic kernel normalization
- two meta-rule codes under fixed `M*`

実行結果の主要部：

```text
finite_unary_rule_tables=27
core_reachable_states_a=4
core_reachable_states_b=4
object_trace=[0, 1, 2, 1, 0, 1, 2, 1, 0]
active_rule_trace=[r_plus, r_plus, r_minus, r_minus,
                   r_plus, r_plus, r_minus, r_minus, r_plus]
rule_change_event_steps=[2, 4, 6, 8]
reachable_state_preservation=True
object_trace_preservation=True
rule_trace_preservation=True
rule_change_event_preservation=True
subset_reachable_states=6
subset_transition_pairs=10
parameter_encoding_commutes=True
alias_behavior_equivalent=True
composition_rule_code=[2, 2, 2]
base_composition_closure_size=8
behavior_code_outside_composition_closure=[0, 0, 2]
stage_rule_set_sizes=[3, 4, 5]
maximal_repertoire_size=5
availability_bitset_roundtrips=True
stage_arity_growth=[[1], [1, 2]]
history_same_visible_pair_different_next_rule=True
stochastic_kernel_sums_to_one=True
finite_meta_rule_codes=2
meta_change_encoded_under_fixed_star=True
all_assertions_passed=True
```

checkerはencoded finite rule/state combinatoricsだけを検証する。open-ended generation、new-law
creation、ontology、universal meta-rule reductionを証明しない。

---

## 24. What is ordinary state, preloaded, and open

### Encoded as ordinary state

- current object value
- active rule code or active rule subset
- finite rule parameter
- stage availability bits
- bounded history record
- finite meta-rule code
- finite external schedule pointer, if explicitly supplied

### Must be preloaded in this encoding

- object/rule code carriers
- rule vocabulary or truth-table grammar
- interpreter and validity checker
- allowed parameters
- tagged type/arity universe
- active-rule update policy `M`
- finite candidate repertoire / ex-post union
- `M*` for meta-rule codes

### Remains representation-relative

- rule label identity versus truth-table behavior
- atomic macro step versus multi-step composition
- inactive but globally coded versus stage-locally ill-formed
- whether history is explicit state or hidden dependency
- whether arity/type alternatives are predeclared tags or later language extensions
- observational horizon and chosen behavioral equivalence

### Remains genuinely OPEN

- fixed admissible coding classでnot-preenumerated rule introductionをどう検査するか
- unbounded/new type formationをfixed universeへ無損失にencodeできる範囲
- arbitrary meta-rule changesに対するuniversal interpreter
- whether any repeated residual requires special notation
- physical meaning of rule availability/adaptation
- endogenous mechanism for a genuinely outside-closure behavior

---

## 25. “Law-like representation can distort generation” implication

「歪み」はtechnical termとして採用しない。本testが支持する正確な記述は次である。

> rule changeをfixed interpreter下のstate transitionへ翻訳すると、object/rule tracesを保存
> できる一方、possible rule vocabulary、code syntax、interpreter、type universe、admissible
> meta-transitionsをlaw/meta-specification側へpreloadする。

そのpreloadはsystem自身のforeknowledgeやphysical ontologyを意味しない。またstage-local
expressibilityを隠す場合があるが、availability/language fieldsを加えれば回復できる。

従って「fixed law representationはrule generationを歪める」という一般命題は **NOT
ESTABLISHED**。現時点で言えるのは、preserved behaviorとpreloaded specificationを別々に
記録すべきだという方法論的結果だけである。

---

## 26. Limited implication for future VED audit

VED本体へはまだ適用しない。将来、update rule、closure update、history dependence、transition
admissibility、rule adaptation、coarse-grained effective lawを監査する場合、最低限次を分ける。

1. object/state value change
2. parameter change
3. active rule change
4. available rule-set change
5. rule-language / type formation change
6. meta-rule change

さらにexogenous schedule、endogenous update、stochastic kernel、effective coarse lawを同一視しない。
このlistはVEDへのpositive/negative verdictではない。

---

## 27. Current methodology status

### What is established

1. several finite rule-change descriptions have explicit fixed-state encodings.
2. core translation preserves reachable states、object/rule traces、change events.
3. aliases and compositions separate symbol novelty from behavior novelty.
4. active repertoire growth over a finite run embeds into an ex-post powerset.
5. finite type and meta-rule changes embed when tagged universes/interpreters are preloaded.
6. history dependence alone does not force a new equation class.

### What remains NOT ESTABLISHED

- open-ended rule generation
- a new-law creation mechanism
- universal fixed-interpreter reduction
- an ultimate physical meta-law
- arbitrary type/language growth equivalence
- distinct generative equation
- any VED-specific result

### Does this support a distinct generative equation?

**NO / NOT ESTABLISHED.** finite tested changes were ordinary higher-order state transitions after
explicit coding. The residuals concern representation language、preload boundary、type scope、and
meta-level choice, not a demonstrated new equation kind.

### Does this strengthen only the audit methodology?

**YES, at present.** rule label、behavior、composition closure、parameter、availability、type、history、
meta-rule、interpreter boundaryを分離する具体的workflowが得られた。

---

## 28. Next recommended step

Phase 4のpreregistered five testsが完了したため、直ちにVED reconstructionやspecial notationへ
進まない。まず **Phase 4 cross-test synthesis / stopping audit** を作成し、四つではなく五つの
finite testsに共通して残ったものを標準語へ翻訳する。

中心falsification questionは一つに限定する。

> observable、carrier、order、metric、rule changeの全test後に、ordinary model extension、
> transition system、partial order、metric construction、interpreter codingで表せない同一の
> residualが反復しているか。

答えがNOならspecial generative-equation branchをRETIRE / DOWNGRADEし、VEDへの適用は式分類と
evidence auditだけに限定する。答えがOPENなら追加testのevidence burdenを先に定める。

commit / pushおよびVED本文の変更はこの記録のscope外である。

---

## 29. Final self-audit

- `R_t≠R_{t+1}`からnew-law creationを推論していない。
- finite encodingからuniversal reductionを推論していない。
- rule label、behavior、composition、parameter、typeを分けた。
- alias translationのmany-to-one lossを隠していない。
- ex-post repertoireとsystem foreknowledgeを同一視していない。
- history liftingをall history compression theoremにしていない。
- meta-code controlからinfinite regressやultimate lawを推論していない。
- behavioral independenceをgeneration mechanismと呼んでいない。
- checkerのfinite scopeを越えていない。
- previous **NOT ESTABLISHED / DOWNGRADE** verdictsを維持した。
- VED本体を評価・変更していない。

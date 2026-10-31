# 同一有限 graph-growth 過程の dual encoding stress test v0.1

## 0. Status / posture

Status:

- finite representation-comparison stress test
- not a theorem
- not a new graph-rewriting formalism
- not a new proof theory or semantics
- not a proof of a distinct generative law
- not a universal reduction of generation to dynamics
- negative results are primary evidence
- standard transition-system、graph-isomorphism、translation の語彙を優先する

この記録は、同一の有限 graph-growth 過程を、固定 state space 上の
ordinary rewrite と changing-carrier record の二方式で表し、明示した
translation が何を保存し、何を保存しないかを調べる。

前実験の判定を維持する。

- distinct generative equation: **NOT ESTABLISHED**
- `G : Σ₀ ⇝ Σ₁`: provisional placeholder / **DOWNGRADE**
- observable independence: comparison map と observational equivalence に相対的な有限診断
- independently distinguishable structural freedom `≠` generation mechanism
- source / target specification、map、observable、equivalence の固定が必要

本実験が扱うのは固定された有限過程だけである。ここで二記述が一致しても、
任意の generation が ordinary dynamics に還元されるとは言えない。逆に一部の
metadata が一致しなくても、distinct generative equation の存在は導けない。

関連記録：

- [working note](../generative_law_methodology_working_note_v0.1_ja.md)
- [generative-equation initial specification](../generative_equation_specification_v0.1_ja.md)
- [evidence-burden table](../generative_claim_evidence_burden_v0.1_ja.md)
- [redescription versus generation controls](../redescription_vs_generation_test_v0.1_ja.md)
- [observable-independence finite test](./observable_independence_finite_model_v0.1_ja.md)
- [companion checker](./graph_growth_dual_encoding_v0.1.py)

---

## 1. Experiment question

中心問いは次である。

> 同一の有限 graph-growth 過程を、(A) 十分大きな固定 graph-state space
> 上の transition と、(B) stage ごとに carrier と language が増える record
> として表したとき、reachable graphs、target predicates、one-step relation、
> histories、identity、future reference はどこまで translation 下で一致するか。

ここで「同一過程」は結論ではなく、以下で与える二つの transition system が
state translation の下で一致するかによって検査される。

### 1.1 Preregistered hypotheses

| Hypothesis | Candidate claim |
| --- | --- |
| H-GR1 | bounded finite graph growth は十分大きな固定 state space 上の ordinary transition として表せる |
| H-GR2 | 同じ有限過程を changing-carrier specifications としても表せる |
| H-GR3 | reachable graph sets と選択した target predicates は適切な translation 下で保存される |
| H-GR4 | 両記述は検査対象となる全構造について完全に同値である |
| H-GR5 | inactive-but-preloaded node は常に not-yet-existent node と同値である |
| H-GR6 | history / provenance の差を保持するには changing-carrier formalism が必要である |
| H-GR7 | full equivalence の失敗は distinct generative equation を確立する |

---

## 2. Common finite process

### 2.1 Bound and labels

最大 node 数を `N = 3` とし、比較用の有限名集合を

\[
U=\{a,b,c\}
\]

とする。`a` は初期 node かつ distinguished root である。許容する有向 edge は

\[
E^*=\{(a,b),(a,c),(b,c)\}
\]

に限定する。この制限は graph theory 上の必要条件ではなく、完全列挙を小さく
保つ実験設計である。

初期 graph は

\[
G_0=(\{a\},\varnothing)
\]

である。

### 2.2 Fixed growth rules

両 encoding で同じ二 rule を使う。

1. **Node activation / carrier extension**: 現在存在しない候補 node を一つ追加し、edge は追加しない。
2. **Edge addition**: active な二 endpoint の間に、`E*` に含まれる未追加 edge を一つ追加する。

一 step は node 一つまたは edge 一つだけを追加する。削除はなく、`N` を越えない。
rule space 自体は全 stage で固定する。本実験は rule generation を扱わない。

### 2.3 Finite scope

許容 labeled graph は 13 個である。

| Active carrier | Edge choices | State count |
| --- | ---: | ---: |
| `{a}` | なし | 1 |
| `{a,b}` | `a→b` | 2 |
| `{a,c}` | `a→c` | 2 |
| `{a,b,c}` | `a→b`, `a→c`, `b→c` | 8 |
| **total** |  | **13** |

checker は 13 個すべてが `G0` から reachable であることを確認した。

---

## 3. Encoding A — fixed state-space rewrite

### 3.1 Specification

\[
\Sigma_A=(\mathcal L_A,X_A,\mathcal O_A,\Theta_A)
\]

を次のように固定する。

- `L_A`: node constants `a,b,c` と active-node / edge predicates を表現できる language
- `X_A`: `a ∈ V ⊆ U`、`E ⊆ E* ∩ (V×V)` を満たすすべての `(V,E)`
- `O_A`: 後で区別する restricted view または full-preload view
- `Θ_A`: `U`、`E*`、root `a`、node bound `N=3`、二 growth rules

状態は

\[
G=(V,E),\qquad V\subseteq U,
\qquad E\subseteq E^*\cap(V\times V)
\]

である。rewrite relation

\[
R_A\subseteq X_A\times X_A
\]

は §2.2 の二 rule による one-step pair の集合である。reachable sub-system には
20 個の directed transition pair がある。

### 3.2 What is preloaded

Encoding A は初期 specification に次を置く。

- future node candidates `b,c`
- node-name identity
- 最大 carrier `U`
- future に可能な edge `E*`
- bound `N`
- growth rules

したがって node の「追加」は数学的には

\[
V_t\subsetneq V_{t+1}\subseteq U
\]

という active subset の変更として表せる。これだけを見る限り ordinary state
transition であり、独自の generative equation を必要としない。

ただし、preloaded node を stage `t` で object language から参照可能にするかは
別の specification choice である。これは §10 で分離する。

---

## 4. Encoding B — changing carrier / changing specification

### 4.1 Stage record

各 state に canonical record

\[
\Sigma_k=(\mathcal L_k,V_k,E_k,\mathcal O_k,\Theta_k)
\]

を対応させる。

- `V_k`: その stage に存在する active carrier
- `E_k`: `V_k` 内の現在 edge
- `L_k`: `V_k` の node だけを constant として持つ stage-local language
- `O_k`: active graph にだけ適用される observables
- `Θ_k`: finite comparison の meta-level では `U`、`E*`、bound、fixed rules を保持

canonical record では

\[
\operatorname{Const}(\mathcal L_k)=V_k
\]

とする。

### 4.2 Two types of B step

node addition では

\[
V_k\subsetneq V_{k+1},
\qquad
\mathcal L_k\subsetneq\mathcal L_{k+1}
\]

となる。edge addition では carrier と constants は変えず、`E_k` だけが増える。

この記録は「carrier 自体が増える」という presentation を明示する。ただし exact
finite comparison のため、候補 `U` と rule は meta-specification に既知である。
したがって、object-domain の stage-local growth と、meta-level で全候補が未知で
あることを同一視していない。

### 4.3 Constant addition versus domain extension

本モデルでは node step は同時に

- object carrier への node 追加
- その node を指す constant の stage language への追加

を行う。constant-name だけを追加して既存 object を命名する definitional operation
ではない。ただし fixed Encoding A から見れば、同じ step は predeclared object の
activation として表せる。この差がまさに comparison 対象であり、「ontology が生成
された」という結論を先に置かない。

---

## 5. Explicit translations

### 5.1 A to B

各 labeled graph `G=(V,E)` に対し、

\[
T_{AB}(G)
=
(\operatorname{Const}(\mathcal L)=V,\;V,\;E)
\]

という canonical B record を作る。

### 5.2 B to A

canonical B record `S=(L,V,E)` に対し、

\[
T_{BA}(S)=(V,E)\in X_A
\]

とする。

### 5.3 Round trips

canonical labeled records に限定すれば checker は

\[
T_{BA}T_{AB}(G)=G
\]

および

\[
T_{AB}T_{BA}(S)=S
\]

を literal equality として確認した。これは B record に余分な history や
provenance field を含めなかったからである。そうした field を加えれば、graph
state だけへの `T_BA` は一般に情報を忘れる。

### 5.4 Equality notions

本実験は三つを分ける。

1. **labeled graph equality**: `V` と `E` が文字通り同じ
2. **root-preserving graph isomorphism**: `a` を固定し、他 label の置換を許す
3. **history equality**: state 列が step ごとに同じ

labeled state round trip の成立から history equality や label-free equality を自動的に
推論しない。

---

## 6. Preservation audit

### 6.1 Summary table

| Object | Preservation result | Scope / qualification |
| --- | --- | --- |
| P1 reachable labeled graphs | **YES, iff** | 13 A states と 13 canonical B records |
| P2 selected target predicates | **YES** | predicate の定義域も含めて比較 |
| P3 one-step adjacency | **YES, iff** | fixed common rules; 20 pairs |
| P4 path history and length | **YES if paths are records** | final state aloneでは両方とも失う |
| P5 node-introduction provenance | **CONDITIONAL** | path/event logで保存、state-only translationでは非保存 |
| P6 future successor set | **YES** | common `U`, `E*`, rulesをmeta-levelで固定 |
| P7 stage-local language growth | **NO as literal language identity** | Aのrestricted policyまたはBのenrichmentでbehaviorを合わせられる |
| P8 rule space | **YES by stipulation** | rule changesは未試験 |

### 6.2 P1 — reachable graph set

checker result:

```text
admissible_a=13
reachable_a=13
reachable_b=13
roundtrip_labeled=True
```

従って、この finite labeled class では

\[
G\in\operatorname{Reach}_A(G_0)
\iff
T_{AB}(G)\in\operatorname{Reach}_B(T_{AB}(G_0)).
\]

これは reachable graph content の一致を支持する。graph-growth 一般、unbounded
growth、未知の node type、rule-space change には及ばない。

### 6.3 P2 — target predicates

三 predicate を使った。

\[
B_1(G): |V|=3,
\]

\[
B_2(G): \text{there is a directed path }a\leadsto c,
\]

\[
B_3(G): \text{the underlying undirected active graph is connected}.
\]

`B2` は `c` が active carrier にない stage では **undefined** とした。false と
undefined を混同しない。全 translated reachable states で、definedness と truth
value の双方が一致した。

```text
predicate_preservation=True
```

### 6.4 P3 — transition adjacency

A と B はともに 20 one-step pairs を持ち、

\[
(G,G')\in R_A
\iff
(T_{AB}(G),T_{AB}(G'))\in R_B
\]

が列挙上成立した。

```text
transition_pairs_a=20
transition_pairs_b=20
one_step_preservation=True
```

これは state bijection だけでなく、この finite reachable part における labeled
transition-system isomorphism を与える。

### 6.5 P4 / P5 — history and provenance

final graph

\[
G_f=(\{a,b,c\},\{(a,b),(b,c)\})
\]

への monotone histories は 5 本あった。例えば、

\[
h_1:
a
\to
\{a,b\}
\to
\{a,b;a\to b\}
\to
\{a,b,c;a\to b\}
\to G_f,
\]

と、

\[
h_2:
a
\to
\{a,b\}
\to
\{a,b,c\}
\to
\{a,b,c;b\to c\}
\to G_f
\]

では最後の step で `a→b` を加える。この二 route は同じ final state を持つが、
異なる state sequence である。全 histories の length は 4 transitions だった。

```text
histories_to_final=5
history_lengths=[4]
pathwise_history_preservation=True
b_introduction_steps=[1, 2]
c_introduction_steps=[1, 2, 3]
```

translation を path の各 state に適用すれば history、length、node introduction
step は保存される。final state だけを保存すれば history は両 encoding で失われる。
従って、

\[
\text{state equality}\neq\text{history equality}.
\]

また history preservation は changing-carrier formalism 固有ではない。Encoding A
も transition path または event log を record すれば同じ情報を保持できる。

### 6.6 P6 — future possibility set

対応する各 state の immediate successors は translation 下で一致する。これは
双方が同じ `U`、`E*`、bound、rules を使うためである。

ただし B の object language が future node をまだ命名できないことと、B の
meta-specification が possible next extension を計算できることは別である。

### 6.7 P7 — language growth

B では node `c` の追加時に `c` constant が初めて object language に入る。A の
full language は `c` を最初から持つ。この literal language difference は graph-state
translation では保存されない。

A の expression policy を「active node constants のみ使用可能」に制限すれば、
B の stage-local expressibility を再現できる。しかし、この prohibition は state
graph そのものからは出ず、追加の admissibility policy である。

逆に B record に global name registry と inactive predicate を加えれば、A の full
preload view を再現できる。従って残差は明示した language/observation specification
に関する差であり、distinct equation の証拠ではない。

---

## 7. Graph-isomorphism control

### 7.1 Root-preserving quotient

node labels を構造の一部としない control として、`a` を固定し、その他の active
node label を permutation する directed graph isomorphism を採用した。

13 labeled reachable states は 10 root-preserving isomorphism classes になった。

```text
rooted_isomorphism_classes=10
label_variants_collapse_under_isomorphism=True
```

例えば

\[
(\{a,b\},\{a\to b\})
\cong
(\{a,c\},\{a\to c\})
\]

である。fresh name `b` / `c` の差はこの quotient では消える。

### 7.2 Predicate invariance is separate

`path a→c` は `c` を distinguished name とするため、上の root-only isomorphism
quotient 上で well-defined ではない。full-carrier graphs

\[
G_1=(\{a,b,c\},\{a\to b\}),
\qquad
G_2=(\{a,b,c\},\{a\to c\})
\]

は root-preserving isomorphic だが、`B2(G1)=false`、`B2(G2)=true` である。

従って、structure quotient を選ぶなら predicate も quotient-invariant に直すか、
`c` を追加の distinguished node として同型概念に含めなければならない。

この control は、label identity を消せば encoding 差がすべて消える、という推論を
阻止する。何を quotient するかと、どの observable を保存するかは同時に指定する
必要がある。

---

## 8. Preloaded-universe control

### 8.1 Three observation policies

初期 A state `G0` と初期 B record を次の三条件で比較した。

#### A0 — active-only observation

A でも observables を active induced graph `(V,E)` に限定する。このとき初期 view は
B の active view と一致する。

```text
restricted_active_view_matches=True
```

#### A1 — inactive predicate

A の full specification では

\[
\operatorname{Inactive}(c)
\]

を true と評価できる。B の初期 object language には `c` がないため、同じ式は
well-formed でない。

```text
inactive_c_observable_in_a=True
c_well_formed_in_initial_b=False
```

#### A2 — future identity reference

A は現在 active でない `c` を future edge candidate や future identity として事前
参照できる。B の stage-local object language では参照できない。ただし B の
meta-level rule enumerator は `c` を候補として知っている。

### 8.2 Result

従って、

\[
\text{inactive but represented}
\neq
\text{not currently in the object domain}
\]

は、inactive/future reference を observable に含める specification では operationally
distinguishable である。「常に同値」は false である。

一方、active-only interface に限定すれば、tested transition behavior は一致する。
差が現れるかは observable language に依存する。これは前実験の
observational-equivalence dependence と同型の監査問題であり、ontology に関する
無条件の結論ではない。

---

## 9. Displayed growth versus encoded process

Encoding B は各 stage に現在 carrier だけを書くため、node addition を表示上明確に
する。Encoding A は全候補を `U` に predeclare し、activation bit の変化として書く。

この finite case では、A が preloaded / hidden にするものは次である。

- future node-name pool
- node bound
- possible edge pool
- fixed extension rules
- stage-local language growth（full `L_A` を使う場合）

B が表示上明確にするものは次である。

- current carrier membership
- current stage で利用できる constants
- node-introduction event as carrier extension
- object-level expressibility boundary

しかし path record を持つ A は introduction history を回復でき、active-language policy
を付けた A は B の object-level expressibility を模倣できる。反対に global registry を
付けた B は A の preload view を回復できる。

よって、この model における差は「一方にしか記述不能な process」ではなく、
state、path、language、observation policy のどれを record に含めたかの差として
十分に記述できる。

---

## 10. Expected false positives

| False positive | Control | Verdict |
| --- | --- | --- |
| FP1: node count 増加だから generative mechanism | A で ordinary activation transition として同一増加を再現 | **KILL** |
| FP2: carrier set が変わるから独自 generation | bounded B carrier を fixed `U` に埋め込み、reachable transition system を保存 | **KILL WITHIN TESTED CLASS** |
| FP3: constant 追加だから ontology addition | A は names を predeclareできる。B でも name addition と object additionを分離可能 | **KILL as inference** |
| FP4: history が違うから state specification が違う | 同じ final stateへの5 paths。path recordはA/B双方で可能 | **KILL** |
| FP5: translation failureだから generation proven | future-reference failureはlanguage policy mismatchであり、restriction/enrichmentで回復可能 | **KILL** |

最も強い false-positive control は FP2 と FP5 の組である。carrier growth は fixed
universe に埋め込めるが、full future-reference language まで同一とすると mismatch
する。この mismatch は preserved object の指定不足を示し、distinct generative law
を示さない。

---

## 11. Evidence-burden audit

| Claim | Evidence in this test | What it establishes | What it does not establish |
| --- | --- | --- | --- |
| A/B have the same reachable labeled graphs | complete enumeration + bijective round trips | this finite reachable-state correspondence | all graph growth reduces to dynamics |
| target predicates are preserved | exhaustive evaluation of three predicates | definedness/value preservation for `B1`–`B3` | preservation of every language formula |
| transitions are preserved | equality of translated 20-pair relations | one-step transition-system correspondence | correspondence under changed rules |
| histories are preserved | pathwise translation of five histories | encoded paths and introduction steps survive | final state determines history |
| stage languages differ | `c` well-formed in A-full, absent in initial B language | literal expressibility is not preserved | ontological superiority of B |
| inactive and nonexistent differ | inactive predicate/future-reference control | difference under specified observables | difference under all observational interfaces |
| distinct generative equation exists | no adequate evidence | nothing positive | mechanism, universality, new mathematical object |

論理形式に合わせた重要な制約は次である。

\[
\text{same finite reachable graphs}
\centernot\Rightarrow
\text{all generation reduces to dynamics},
\]

かつ

\[
\text{some metadata not preserved}
\centernot\Rightarrow
\text{a distinct generative equation exists}.
\]

---

## 12. Hypothesis verdicts

### H-GR1

> finite graph growth can be represented as ordinary transition in a fixed sufficiently large graph-state space.

**RETAIN WITH SCOPE.** `N=3`、fixed `U`、fixed rules の encoded process では完全に
成立した。unbounded / open-ended carrier、unknown future types、rule changes には
一般化しない。

### H-GR2

> the same finite process can be represented as changing-carrier specifications.

**RETAIN WITH SCOPE.** canonical B records と stage-local languages で表せ、Aとの
state/transition translation を構成できた。ただし meta-specification は候補 `U` と
rules を保持する。

### H-GR3

> reachable graph sets and selected target predicates are preserved under translation.

**RETAIN WITH SCOPE.** 13 reachable labeled graphs、20 transitions、三 target predicates
で成立した。`B2` では undefinedness も含めた。all formulas や all equivalence choices
の保存ではない。

### H-GR4

> fixed-universe and changing-carrier descriptions are fully equivalent with respect to all tested structure.

**KILL.** graph-state、transition、path は一致するが、full A language の inactive /
future reference と B stage-local language は literal には一致しない。policy を足せば
回復できるという事実は、無条件の full equivalence を復活させない。

### H-GR5

> inactive-but-preloaded nodes are always equivalent to not-yet-existent nodes.

**KILL.** inactive predicate または future-name reference を許すと区別できる。
active-only observation の下でのみ observationally equivalent である。

### H-GR6

> history/provenance differences require changing-carrier formalism.

**KILL.** fixed-state rewrite でも path/event log を record すれば五 histories と node
introduction steps を保持できる。state-only record が history を失うのは両方式共通。

### H-GR7

> failure of full equivalence establishes a distinct generative equation.

**KILL.** 残った failure は language/observation policy と record content の差として
説明でき、mechanism の独自性を支持しない。より一般にも一つの translation failure
は alternative translation の不在を示さない。

---

## 13. Strongest results

### 13.1 Strongest equivalence result

この bounded labeled process では、canonical B records と A active graphs の間に、
reachable states と one-step relation を保存・反映する bijection がある。選択した
state predicates と explicit paths も翻訳できる。

標準語では、tested reachable parts は labeled transition systems として isomorphic
である。これ以上の project-local concept は不要である。

### 13.2 Strongest nonequivalence result

Encoding A の full preloaded language は inactive node `c` を初期 stage から指示し、
その inactive status を評価できる。Encoding B の初期 stage-local languageには `c`
がない。この literal well-formedness / future-reference information は state graph
translationだけでは保存されない。

ただしこれは A の active-only restriction、または B の global-registry enrichment
で回復可能であり、representation/interface choice に相対的である。

### 13.3 Strongest negative result

少なくともこの finite bounded graph-growth class では、carrier enlargement、node-count
increase、constant introduction は、reachable graph dynamics に独自の数学的内容を
加えなかった。changing-carrier notation はその process を別の record boundary で
表示した。

一方、これを「すべての generation は dynamics である」という universal claim に
拡張する証拠はない。

---

## 14. Checker

[graph_growth_dual_encoding_v0.1.py](./graph_growth_dual_encoding_v0.1.py)
は Python standard library のみを用い、次を完全列挙・assert する。

- 13 admissible / reachable A graphs
- 13 reachable canonical B records
- A/B labeled round trips
- 20 one-step transition pairs の保存
- `B1`–`B3` の definedness/value 保存
- one final graph への 5 histories と pathwise translation
- introduction-step provenance
- 10 root-preserving isomorphism classes
- label-sensitive predicate がその quotient 上で不変でない control
- active-only view の一致
- inactive/future-reference language の差
- future successor set の一致

実行結果：

```text
graph growth dual encoding finite checker v0.1
admissible_a=13
reachable_a=13
reachable_b=13
transition_pairs_a=20
transition_pairs_b=20
roundtrip_labeled=True
predicate_preservation=True
one_step_preservation=True
histories_to_final=5
history_lengths=[4]
pathwise_history_preservation=True
b_introduction_steps=[1, 2]
c_introduction_steps=[1, 2, 3]
rooted_isomorphism_classes=10
label_variants_collapse_under_isomorphism=True
label_sensitive_predicate_not_quotient_invariant=True
restricted_active_view_matches=True
inactive_c_observable_in_a=True
c_well_formed_in_initial_b=False
future_successors_preserved=True
rules_fixed=True
all_assertions_passed=True
```

checker は encoded finite graph system の combinatorial equivalence /
nonequivalence だけを検証する。generation、ontology、physical emergence、universal
reducibility、unbounded process を証明しない。

---

## 15. Implication for the current methodology branch

### What is now established

1. bounded fixed-rule graph growth の少なくとも一例は fixed-space rewrite と
   changing-carrier record の双方で表せる。
2. map と scope を固定すれば reachable states、one-step transitions、選択 predicates、
   recorded historiesを保存・反映できる。
3. fixed-universe preload と not-yet-in-domain は、future referenceを許すかどうかで
   区別され得る。
4. history retention は changing carrier の専有物ではなく、record design に依存する。
5. graph isomorphism quotient と label-sensitive observables は別々に整合性を確認する
   必要がある。

### What remains NOT ESTABLISHED

- distinct generative equation
- endogenous carrier-generation mechanism
- unbounded / open-ended growth の fixed-universe reduction
- rule space 自体が変わる場合の translation
- future object types が事前列挙不能な場合の対応
- stage-local language difference の ontological interpretation
- arbitrary graph-growth formalisms 間の equivalence theorem

### Current status of “generative equation”

**NOT ESTABLISHED.** この test は provisional `Σ_k → Σ_{k+1}` 表示に独自の
mathematical content を与えなかった。bounded carrier growth は ordinary transition
system で無損失に再現できる範囲が大きい。

### Does this strengthen only the audit methodology?

**YES, at present.** 保存を一語で述べず、state、transition、predicate、path、language、
identity、future reference を分ける監査手順が具体化した。これは standard
translation / transition-system terminology で十分に表せる。

---

## 16. Implication for “law-like representation can distort generation”

「歪み」は technical term として採用しない。本実験が支持する正確な言い方は次で
ある。

> fixed-state representation は、tested graph behavior を保存できる一方、future
> carrier、name pool、bound、rule pool を initial meta-specification に preload し、
> stage-local language growth を full language の内部へ隠すことがある。

しかし hidden information は失われたとは限らず、active-set field と history log
から回復できる。また observation policy を揃えれば behavior は一致する。従って
「law-like representation は generation を歪める」という一般命題は **NOT
ESTABLISHED** である。現時点で言えるのは、translation の preserved object と
preloaded metadata を明記しなければ、二記述の比較を誤る、という方法論的結果だけ
である。

---

## 17. Next recommended experiment

次は preregistered order に従い、**construction order versus internal order** を小さい
finite system で検査する。独立な二 construction step を入れ替えたとき、

- final structure
- construction history
- bookkeeping index
- generated internal partial order

を分ける。特に meta-level derivation order を emergent physical time と誤認しない
control を中心にする。

この次段階でも VED 本体の式は変更せず、distinct generative equation を前提にしない。

---

## 18. Final self-audit

- fixed finite state correspondenceからuniversal reductionを推論していない。
- language mismatchからdistinct generative lawを推論していない。
- labeled equality、graph isomorphism、history equalityを分けた。
- state-only recordとpath recordを分けた。
- inactive nodeとdomain-external nodeをobservable policyに相対化した。
- rule-space changeを扱ったと偽っていない。
- checkerの有限scopeを越えて一般 theorem を主張していない。
- prior **NOT ESTABLISHED / DOWNGRADE** verdictsを維持した。
- VED本体へpositive verdictを出していない。

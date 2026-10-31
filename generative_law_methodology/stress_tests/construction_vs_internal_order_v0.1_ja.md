# Construction order と internal partial order の有限 stress test v0.1

## 0. Status / posture

Status:

- finite order-theoretic stress test
- not a theorem
- not a theory of physical time
- not a theory of causality
- not a temporal-emergence result
- not a new proof theory or generative calculus
- not evidence for a distinct generative equation
- negative results are primary evidence
- standard partial-order、linear-extension、timestamp、transition-system の語彙を優先する

本実験は、construction / bookkeeping sequence と target 内部の mathematical
partial order を有限例で分離する。「時間が生成される」「partial order が物理的
causality である」「stage index が physical time である」という主張は行わない。

前実験の判定を維持する。

- distinct generative equation: **NOT ESTABLISHED**
- bounded graph growth は fixed-state rewrite と changing-carrier record の双方で表せる
- history は path / event log があれば fixed-state representation でも保存できる
- stage-local language と future reference は representation / admissibility policy に依存する
- construction history と final state は異なる記録対象である
- stage index と physical time を同一視してはならない

関連記録：

- [working note](../generative_law_methodology_working_note_v0.1_ja.md)
- [generative-equation specification](../generative_equation_specification_v0.1_ja.md)
- [evidence-burden table](../generative_claim_evidence_burden_v0.1_ja.md)
- [redescription controls](../redescription_vs_generation_test_v0.1_ja.md)
- [observable-independence test](./observable_independence_finite_model_v0.1_ja.md)
- [graph-growth dual-encoding test](./graph_growth_dual_encoding_v0.1_ja.md)
- [companion checker](./construction_vs_internal_order_v0.1.py)

---

## 1. Experiment question

中心問いは次である。

> 一つの internal partial order に複数の valid construction histories が対応する
> とき、construction-stage sequence は internal order と同一か。また、stage
> index、order-preserving timestamp、duration、physical clock time の間に何が
> 成立し、何が成立しないか。

主 control は

\[
h_1\neq h_2,
\qquad
Q(h_1)=Q(h_2)=P
\]

を完全列挙で示すことである。

ただし、construction order と internal order が完全に無関係だという仮説は置かない。
検査するより正確な関係は

\[
h\in\operatorname{Lin}(P)
\]

であり、history の total order が `P` を延長する一方で、一般には `P` そのものでは
ないという関係である。

---

## 2. Fixed finite order model

### 2.1 Event set and generating relation

event set を

\[
E=\{a,b,c,d\}
\]

とする。cover relation を

\[
R_0=\{(a,c),(b,c),(c,d)\}
\]

とし、その transitive closure を strict precedence relation `≺` とする。

\[
P=(E,\prec),
\]

\[
\prec
=
\{(a,c),(b,c),(c,d),(a,d),(b,d)\}.
\]

`≺` は irreflexive、asymmetric、transitive である。`a` と `b` の間には

\[
a\nprec b,
\qquad
b\nprec a
\]

が成立する。

### 2.2 Interpretation limit

この `≺` は本実験では **mathematical dependency / precedence relation** である。
“causal candidate order” と説明することはできるが、partial-order axiomsだけから
physical causality、signal propagation、spacetime order、empirical timeを導かない。

---

## 3. Encoding A — sequential construction history

### 3.1 History syntax

construction history は全 event を一度ずつ含む linear sequence

\[
h=(e_1,e_2,e_3,e_4)
\]

である。construction index

\[
k\in\{1,2,3,4\}
\]

は、どの event を何番目に record / execute したかを表す meta-level bookkeeping
index とする。

### 3.2 Validity rule

event `e` を追加できるのは、`P` におけるすべての predecessor がすでに active な
場合だけとする。history `h` の position map を `pos_h` とすれば、

\[
h\text{ is valid}
\iff
\forall(x,y)\in\prec,
\operatorname{pos}_h(x)<\operatorname{pos}_h(y).
\]

すなわち valid histories は `P` の linear extensions である。

### 3.3 Construction total order

各 history は strict total order

\[
L_h
=
\{(e_i,e_j):i<j\}
\]

を与える。validityから

\[
\prec\ \subseteq L_h
\]

は成立する。しかし `a,b` のような incomparable pair にも `L_h` は向きを付ける。
従って一般に

\[
L_h\neq\prec.
\]

---

## 4. Encoding B — internal partial order

target は sequence ではなく

\[
P=(E,\prec)
\]

である。`P` が記録するのは、target specificationで要求された precedence pairs
だけである。incomparable event のconstruction順序は記録しない。

history-forgetting map を

\[
Q:\mathcal H_{\mathrm{valid}}\to\mathcal P,
\qquad
Q(h)=P
\]

とする。ここで本実験の `H_valid` は固定した `P` のlinear extensions、`P` space は
この主modelで一つのtargetだけを含む。

これは一般のhistoryからpartial orderを発見するalgorithmではない。固定した
predecessor ruleに従う historiesから、linearizationを忘れてtarget orderを返す
明示的 projection である。

---

## 5. Exhaustive linear-extension control

### 5.1 Enumeration

4 events の全24 permutationsを列挙した。valid linear extensionsはちょうど二つである。

\[
h_1=(a,b,c,d),
\]

\[
h_2=(b,a,c,d).
\]

残り22 permutationsはpredecessor conditionを少なくとも一つ破る。

従って、

\[
|\operatorname{Lin}(P)|=2>1,
\]

\[
h_1\neq h_2,
\qquad
Q(h_1)=Q(h_2)=P.
\]

### 5.2 What changes and what does not

| Item | `h1` versus `h2` |
| --- | --- |
| event set | same |
| final partial order | same |
| transitive precedence relation | same |
| `a,b` incomparable | same |
| `a` construction stage | different |
| `b` construction stage | different |
| total construction order | different |
| pure-order target predicates | same |

`h1`では `(a,b)∈L_h1`、`h2`では `(b,a)∈L_h2` だが、どちらのpairも `≺`
には含まれない。よって、incomparable eventsのconstruction orderingはpure-order
targetに保存されない。

### 5.3 Selected target predicates

次を確認した。

- carrier is exactly `{a,b,c,d}`
- `a` and `b` are incomparable
- `a≺c` and `b≺c`
- `c≺d`
- `a≺d` and `b≺d`

すべて `Q(h1)` と `Q(h2)` で同じ値を取る。これはselected pure-order predicates
の保存であり、arbitrary history-sensitive observablesの保存ではない。

---

## 6. Permutation and dependent-step controls

### 6.1 Independent permutation

`a,b` はincomparableなので、先頭二stepを交換してもvalidである。

\[
(a,b,c,d)\longleftrightarrow(b,a,c,d).
\]

交換は `P`、そのtransitive relation、selected target predicatesを変えない。pure-order
targetだけを比較する限り、この差はnon-invariantかつquotientableなhistory detailで
ある。

“gauge” は採用しない。gauge theoryの技術的構造を与えていないからである。

### 6.2 Dependent permutation

例えば

\[
h_{\mathrm{bad}}=(a,b,d,c)
\]

では `c≺d` に反して `d` が先に現れる。従ってこれは同じ `P` に対するvalid
constructionの別表現ではなく、**invalid construction** である。

`h_bad` をvalidとするには、predecessor ruleを緩めるかtarget orderを変える必要が
ある。その場合はsame-target comparisonではない。

よって、

\[
\text{arbitrary permutation}
\neq
\text{linear extension of the same partial order}.
\]

---

## 7. Quotient by equal internal target

### 7.1 Pure-order equivalence

test-local relationを

\[
h_1\sim_P h_2
\iff
Q(h_1)=Q(h_2)
\]

とする。これはstandard equality of images under a mapであり、新しいproof equalityや
temporal equivalenceを提案するものではない。

主modelでは二 valid historiesが一つのequivalence classになる。

\[
|\mathcal H_{\mathrm{valid}}|=2,
\qquad
|\mathcal H_{\mathrm{valid}}/{\sim_P}|=1.
\]

その一classは唯一のpure-order target `P` に対応する。

### 7.2 Scope of the quotient

この quotient が情報を失わないのは、targetを `(E,≺)` だけに固定したときである。
provenance、duration、resource state、intermediate observables、stochastic likelihood、
irreversible side effectsをtargetに含めるなら、`Q(h1)=Q(h2)`だけでは同一視の十分な
根拠にならない。

従って `~P` はuniversal history identityではない。

---

## 8. History-sensitive metadata control

### 8.1 Deliberately path-dependent cost

historyのstep `k` にevent-specific weight `w(e)` を掛ける有限controlを置く。

\[
w(a)=1,
\quad w(b)=2,
\quad w(c)=3,
\quad w(d)=4,
\]

\[
C(h)=\sum_{k=1}^{4}k\,w(e_k).
\]

すると

\[
C(h_1)=30,
\qquad
C(h_2)=29.
\]

よって

\[
Q(h_1)=Q(h_2)
\quad\text{but}\quad
C(h_1)\neq C(h_2).
\]

targetを `(P,C)` にenrichすれば二historyは二classesに分かれる。

### 8.2 What this control establishes

これは

\[
\text{same internal partial order}
\neq
\text{same value for every history-sensitive observable}
\]

を示す。construction orderingを消せるかは、何をtarget dataと宣言したかに相対的で
ある。

### 8.3 What it does not establish

`C` はfalse-positive controlのために定義した数学的observableであり、physical
energy、action、duration、entropyではない。この一例は、すべてのconstruction
historiesが物理的に異なることも、history detailがphysicalであることも示さない。

---

## 9. Timestamp controls

### 9.1 T1 — order-preserving timestamp

timestamp候補を

\[
\tau:E\to\mathbb Z
\]

とし、

\[
x\prec y\Rightarrow\tau(x)<\tau(y)
\]

を要求する。

例えば、

\[
\tau_1(a)=0,
\quad\tau_1(b)=0,
\quad\tau_1(c)=1,
\quad\tau_1(d)=2
\]

と

\[
\tau_2(a)=10,
\quad\tau_2(b)=20,
\quad\tau_2(c)=30,
\quad\tau_2(d)=100
\]

はいずれもorder-preservingである。

### 9.2 T2 — non-uniqueness

rangeを有限集合 `{0,1,2,3}` に限定しても、strict order-preserving timestampsは6個
存在した。従って `P` は `τ` を一意に決めない。

さらに、strictly increasing affine transformation

\[
\tau'(e)=2\tau(e)+7
\]

もorderを保存する。このfreedomはlarger codomainではさらに増える。

### 9.3 T3 — construction index as a timestamp

history内positionを

\[
\tau_h(e)=\operatorname{pos}_h(e)
\]

と置けば、valid historyごとにorder-preserving timestampが得られる。しかし

\[
\tau_{h_1}(a)=1,
\quad
\tau_{h_2}(a)=2,
\]

であり、同じ `P` から一意には決まらない。T3はlinear extensionが選ぶ一つの
embeddingであり、internal orderそのものではない。

### 9.4 Duration is not recovered

`τ1` と `τ2` では、同じcomparable pair `a≺d` に対し

\[
\tau_1(d)-\tau_1(a)=2,
\]

\[
\tau_2(d)-\tau_2(a)=90.
\]

よってpartial orderだけからmetric durationは決まらない。timestampを追加すれば
数値差は定義できるが、そのunit、scale、clock procedure、dynamical meaning、empirical
adequacyは別の仕様と証拠を要する。

中心的分離は

\[
\text{order}
\neq
\text{duration}
\neq
\text{clock reading}
\]

である。

---

## 10. Metatime audit

### 10.1 Two orders

construction processには外部sequence index `n` がある。target内部には `≺` がある。
`n` は全eventsをlinearに並べるが、`≺` は `a,b` を比較しない。

従って具体的に

\[
n\text{-order}\not\equiv\prec.
\]

ただしvalid historiesでは

\[
h\in\operatorname{Lin}(E,\prec)
\]

というcompatibilityがある。正確には `L_h` は `≺` を保存するtotal extensionであり、
`≺` の一意な表現ではない。

### 10.2 Five notions kept separate

| Notion | This model records | Not justified by that record |
| --- | --- | --- |
| construction order | algorithm/logでeventを追加した順番 | target-internal necessity |
| topological sort | `P`とcompatibleなlinear ordering | unique history |
| event-log order | retained sequence of recorded updates | physical causation |
| internal precedence | target relation `≺` | metric duration or clock time |
| physical time interpretation | not supplied | not inferable from the four mathematical records alone |

### 10.3 Causal language limit

本modelで確立したのはdependency orderだけである。`x≺y` を physical cause と読むには、
intervention、signal、dynamical law、empirical identification等の追加条件が必要になり
得るが、本実験は必要十分条件を定めない。

---

## 11. Fixed-state representation control

### 11.1 State space

前回graph-growth testと同様、最大event setとprecedence relationを最初にpreloadする。
stateを

\[
S=(A,R),
\]

\[
A\subseteq E,
\qquad
R=\prec\cap(A\times A)
\]

とする。`A` はactive events、`R` はそのstageでactiveなinternal relationである。

### 11.2 Ordinary transition

全predecessorsが `A` に入った未active eventを一つ追加する。これは固定state space上の
ordinary transition relationである。

checkerは次を得た。

```text
fixed_states_reachable=6
fixed_state_transitions=6
fixed_state_histories=2
fixed_state_history_correspondence=True
```

二 pathから追加eventを順に読み出すと、ちょうど `h1,h2` になる。final fixed stateは
どちらも `(E,≺)` である。

### 11.3 Result

construction historyとinternal orderの分離は、changing specificationを必要としない。
fixed transition systemでもstate/pathの区別として完全に記録できる。

従ってこの分離自体は、新しいequation classやgenerative notationの必要性を支持しない。

---

## 12. Preservation and recoverability table

| Item | From `h` to `P` | From `P` to `h` | Qualification |
| --- | --- | --- | --- |
| event carrier | preserved | recoverable | fixed complete history |
| internal precedence | preserved by `Q` | given directly | fixed target rule |
| linear construction order | forgotten | not unique | two linear extensions |
| incomparable-event ordering | forgotten | not recoverable | absent from `P` |
| selected pure-order predicates | preserved | evaluable | only chosen predicates tested |
| construction timestamp `τ_h` | forgotten | not unique | depends on linear extension |
| arbitrary order-preserving `τ` | not part of `Q` | not unique | six even in finite range 0–3 |
| path-dependent cost `C` | not preserved | not recoverable | unless target is enriched |
| metric duration | not supplied | not recoverable | timestamp/metric/clock specification required |
| physical causality / time | not supplied | not recoverable | empirical/interpretive evidence absent |

---

## 13. Evidence-burden audit

| Claim | Evidence supplied | What it establishes | What it does not establish |
| --- | --- | --- | --- |
| multiple constructions give one `P` | exhaustive 24-permutation enumeration | two valid histories have identical image | every order has multiple histories |
| `h1,h2` differ only representationally | equality of pure-order target data | quotient is valid for the declared pure-order target | equality of all physical/history data |
| invalid dependent swap | predecessor-rule check | `abdc` is not a linear extension of this `P` | no alternative target could admit it |
| `P` does not determine history | two distinct linear extensions | non-uniqueness in this finite model | reconstruction impossible with added provenance |
| timestamps are non-unique | six bounded assignments plus explicit examples | order alone underdetermines timestamp | no physical clock can be selected |
| duration is absent from `P` | same pair receives differences 2 and 90 | metric duration is not fixed by order | metric time is impossible to add |
| fixed-state encoding exists | explicit six-state transition system | this construction can be ordinary dynamics | every temporal-generation proposal reduces similarly |
| physical time is generated | no suitable evidence | nothing positive | empirical time, causal semantics, clock behavior |

禁止する推論：

\[
|\operatorname{Lin}(P)|>1
\centernot\Rightarrow
\text{time is emergent},
\]

\[
P\text{ is a partial order}
\centernot\Rightarrow
P\text{ is physical causality},
\]

\[
\text{construction order is non-unique}
\centernot\Rightarrow
\text{internal order is unreal}.
\]

---

## 14. Hypothesis verdicts

### H-ORD1

> construction stage order is identical to the internal partial order.

**KILL.** 各valid historyのlinear orderは `P` を延長するが、`a,b`に余分な向きを
付ける。`L_h`と`≺`は一致しない。

### H-ORD2

> different construction histories can yield the same internal partial order.

**RETAIN WITH SCOPE.** `abcd`と`bacd`がexplicit witnessesである。この有限target
についてのexistential resultであり、すべてのpartial orderについてのclaimではない。

### H-ORD3

> the construction history can be recovered uniquely from the internal partial order.

**KILL.** `|Lin(P)|=2`なので、pure `P`からhistoryを一意復元できない。追加provenance
があれば別だが、それはtarget specificationのenrichmentである。

### H-ORD4

> the construction ordering of incomparable events shows an internal physical difference.

**KILL as an unqualified inference.** pure-order targetにはその差がない。history-sensitive
costを追加すればenriched target上の差は作れるが、そのphysical meaningは別証拠を要する。

### H-ORD5

> the stage index can be used directly as emergent physical time.

**KILL.** position mapは一つのorder-preserving timestampを与えるだけで、linear-extension
choiceに依存する。metric duration、clock procedure、empirical interpretationを与えない。

### H-ORD6

> adding event timestamps to a partial order establishes physical time.

**KILL as stated.** timestampは追加数学構造を与え、指定した数値差を定義できる。
しかしorder-preserving assignmentsは非一意であり、physical timeとしての同定は
**NOT ESTABLISHED**。

### H-ORD7

> separating construction order from internal order requires a distinct generative equation.

**KILL.** standard order theoryとfixed-state transition systemで区別を完全に記述できた。
distinct generative equationの必要性は出なかった。

---

## 15. Strongest results

### 15.1 Strongest equivalence result

pure-order targetだけを保持する場合、二linear extensionsは `Q` により一つのclassに
なり、唯一のtarget `P` に対応する。またchanging-stage presentationを使わずとも、
fixed six-state transition systemの二 pathsとして同じconstruction historiesを保持できる。

### 15.2 Strongest nonequivalence result

construction total orderはinternal partial orderより細かい。`a,b` の相対順序、position
timestamp、path-dependent costはpure `P` に保存されず、`P`から回復できない。

### 15.3 Strongest negative result

stage sequence、partial order、timestampのいずれも、それ単独ではphysical time、metric
duration、physical causalityを確立しない。construction/internal orderの分離はstandard
order-theoretic terminologyで尽くされ、distinct generative notationの必要性をさらに
弱めた。

### 15.4 Best false-positive control

最も明瞭なcontrolは、

\[
\tau_h(e)=\operatorname{pos}_h(e)
\]

である。各historyについてvalidなtimestampを与えるため時間らしく見えるが、同じ
internal `P` に対し `τ_h1≠τ_h2` であり、durationも一意でない。stage indexをphysical
timeと読む推論を直接阻止する。

---

## 16. Checker

[construction_vs_internal_order_v0.1.py](./construction_vs_internal_order_v0.1.py)
はPython standard libraryだけを使い、次をassertする。

- `P`のstrict partial-order propertiesとtransitive closure
- 24 permutations中2 valid linear extensions / 22 invalid permutations
- dependent-step swap `abdc` のinvalidity
- two historiesからone pure-order targetへのcollapse
- selected target predicatesの一致
- path-dependent cost `30≠29`
- enriched `(P,C)` targetではtwo classesになること
- range `0..3` 内の6 order-preserving timestamps
- construction-position timestampsの非一意性
- duration examples `2` と `90`
- fixed state spaceの6 states、6 transitions、2 paths

実行結果：

```text
construction versus internal order finite checker v0.1
events=4
precedence_pairs_after_transitive_closure=5
all_permutations=24
valid_linear_extensions=2
invalid_permutations=22
valid_histories=['abcd', 'bacd']
distinct_pure_order_targets=1
pure_order_quotient_classes=1
selected_target_predicates_preserved=True
dependent_swap_abdc_valid=False
history_costs={'abcd': 30, 'bacd': 29}
history_enriched_target_classes=2
bounded_order_preserving_timestamps_0_to_3=6
construction_timestamps_distinct=True
duration_a_to_d_examples=[2, 90]
fixed_states_reachable=6
fixed_state_transitions=6
fixed_state_histories=2
fixed_state_history_correspondence=True
all_assertions_passed=True
```

checkerはfinite order-theoretic / combinatorial factsだけを検証する。physical time、
causality、ontological generation、universal temporal emergenceを証明しない。

---

## 17. What each record contains

### Construction stage index records

- selected execution / insertion sequence
- prefix completion count
- event-log position under one scheduler / construction
- one chosen linear extension of the target dependency order

### Internal partial order records

- target-internal required precedence
- incomparability where no required precedence is supplied
- transitive dependency consequences
- all compatible linear extensions indirectly, but not which one occurred

### Neither record establishes

- physical causation
- elapsed metric duration
- clock synchronization or unit
- empirical clock readings
- dynamical rate law
- why one history was physically selected
- ontological or temporal emergence

### Extra structure needed for metric time

少なくとも数値 assignment、duration comparison、scale/unit、clock or operational
procedure、dynamical/empirical interpretationを別途指定する必要がある。これらが十分か
どうかは本実験では **OPEN** であり、timestampを付けただけでは足りない。

---

## 18. Limited implication for later VED audit

VED本体には適用せず、将来の監査項目だけを記録する。

\[
\frac{d\tau_i}{dt}=\rho_i
\]

やirreversible history `H_ij` を扱う場合、最低限次を分ける必要がある。

- external bookkeeping parameter `t`
- event / update sequence
- internal partial causal candidate order
- accumulated local observable `τ`
- metric duration
- empirical clock time

このlistはVEDへのnegative/positive verdictではない。とくに `dτ/dt` の数学的妥当性、
`τ` のphysical interpretation、`H` のcausal adequacyは本testで評価していない。

---

## 19. Current methodology status

### What is established

1. 一つのfinite posetは二つの異なるconstruction sequencesを持ち得る。
2. valid sequenceのtotal orderはinternal orderのlinear extensionであり、internal order
   そのものではない。
3. pure-order quotientはこのmodelで二historiesを一targetに正しく対応させる。
4. history-sensitive dataをtargetへ加えると同じquotientは情報を失う。
5. partial orderはtimestampとdurationを一意に定めない。
6. 同じ区別をfixed-state ordinary transitionで表現できる。

### What remains NOT ESTABLISHED

- physical or emergent time
- physical causality
- any unique physical timestamp
- metric duration from order alone
- an endogenous temporal-generation mechanism
- a distinct generative equation
- universal equivalence of construction histories modulo partial order

### Does this support a distinct generative equation?

**NO / NOT ESTABLISHED.** むしろtested distinctionはstandard order theory、linear
extensions、quotients、path records、timestamp embeddingsで無損失に記述できた。

### Does this strengthen only the audit methodology?

**YES, at present.** stage indexをtimeと読む前に、construction log、internal order、
timestamp、duration、physical interpretationを別々に固定する手順が具体化した。

---

## 20. Next recommended experiment

preregistered sequenceの次は **relation-to-metric construction boundary test** とする。
有限weighted graphで positivity、symmetry、zero distance、disconnectedness、quotientを
変え、constructionがmetric、pseudometric、extended metric、またはfailureのどれを
与えるかを判定する。

目的は「metric生成」を証明することではなく、derived distance observableとindependent
metric structure、およびmetric axiomsを満たすための条件を分離することである。

VED本体はまだ変更しない。Phase 4のmetric control完了とrule-space testのscopingまでは
VED reconstruction gateを開かない。

---

## 21. Final self-audit

- construction orderをinternal orderと同一視していない。
- linear extension compatibilityを「完全に無関係」と誤記していない。
- multiple historiesからtime emergenceを推論していない。
- partial orderからphysical causalityやmetric timeを推論していない。
- timestamp追加をphysical clockの確立と呼んでいない。
- history-sensitive costをphysical observableと偽っていない。
- invalid permutationとdifferent targetを分けた。
- pure-order quotientをuniversal history identityにしていない。
- fixed finite modelからuniversal theoremを作っていない。
- previous **NOT ESTABLISHED / DOWNGRADE** verdictsを維持した。
- VED本体を評価・変更していない。

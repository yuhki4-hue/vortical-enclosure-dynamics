# Relation から metric-like structure への有限 boundary stress test v0.1

## 0. Status / posture

Status:

- finite graph-and-distance boundary stress test
- not a theorem
- not a new metric theory
- not a theory of spatial emergence
- not a proof that distance or space is generated
- not evidence for a distinct generative equation
- negative results are primary evidence
- standard graph distance、metric、pseudometric、extended metric、quasi-metric の語彙を優先する

本実験は、有限 relation / weighted graph に shortest-path construction を適用したとき、
何が入力として固定され、どの metric axioms が成立し、どの条件で失敗するかを監査する。

前実験の判定を維持する。

- distinct generative equation: **NOT ESTABLISHED**
- bounded graph growth は fixed-state rewrite と changing-carrier record の双方で表せる
- construction order `≠` internal partial order
- partial order `≠` timestamp `≠` duration `≠` clock reading
- new structure のdefinability `≠` independent structural freedom
- standard mathematicsで十分ならspecial generative notationを追加しない

関連記録：

- [working note](../generative_law_methodology_working_note_v0.1_ja.md)
- [generative-equation specification](../generative_equation_specification_v0.1_ja.md)
- [evidence-burden table](../generative_claim_evidence_burden_v0.1_ja.md)
- [redescription controls](../redescription_vs_generation_test_v0.1_ja.md)
- [observable-independence test](./observable_independence_finite_model_v0.1_ja.md)
- [graph-growth dual encoding](./graph_growth_dual_encoding_v0.1_ja.md)
- [construction/internal-order test](./construction_vs_internal_order_v0.1_ja.md)
- [companion checker](./relation_to_metric_boundary_v0.1.py)

---

## 1. Experiment question

finite weighted graph

\[
G=(V,E,w)
\]

から

\[
d_G(x,y)
=
\inf_{\gamma:x\leadsto y}
\sum_{e\in\gamma}w(e)
\]

を構成したとき、`d_G` はどの仮定の下でordinary metricになり、どの仮定を外すと
pseudometric、extended metric、asymmetric distance、またはill-behaved infimumになるか。

さらに、`d_G` が一意に計算できることからindependent metric degree of freedomや
physical space emergenceを推論できるかを検査する。

### 1.1 Path convention

positive / zero-weight casesではsimple pathとrepeated-vertex walkのinfimumは同じになる。
negative-cycle controlでは、edgeを反復できるwalkを `γ` に含める。そのためnegative
cycleを何度も回ればinfimumが `-∞` になり、finite shortest pathが存在しない。

このconventionを明示しないまま「negative cycleで最短距離が `-∞`」とは言わない。

### 1.2 Axiom checklist

ordinary metricについて次を個別に確認する。

1. finite-valuedness: `d(x,y)∈R`
2. nonnegativity: `d(x,y)≥0`
3. zero diagonal: `d(x,x)=0`
4. identity of indiscernibles: `d(x,y)=0 ⇒ x=y`
5. symmetry: `d(x,y)=d(y,x)`
6. triangle inequality:
   \[
   d(x,z)\le d(x,y)+d(y,z)
   \]

axiom failureを一語の「distance failure」にまとめない。

---

## 2. Finite cases and terminology

全caseで

\[
V=\{a,b,c\}
\]

を使う。undirected edgeは両方向の同weight arcとして計算する。

本記録での用語は次に限定する。

- **metric**: finite-valued、nonnegative、zero diagonal、identity、symmetry、triangle
- **pseudometric**: metricからidentityだけを緩める
- **extended metric**: metricからfinite-valuednessだけを緩め、`+∞`を許す
- **quasi-metric**: 本testではfinite-valued、nonnegative、zero diagonal、identity、triangleを満たし、symmetryを要求しない

“quasi-metric”のconventionには文献差があるため、名称だけでなく上のaxiomsを併記する。

---

## 3. Case A — positive undirected connected graph

### 3.1 Input

undirected weighted edgesを

\[
w(a,b)=2,
\qquad
w(b,c)=3,
\qquad
w(a,c)=10
\]

とする。graphはconnectedで、すべてのedge weightsはstrictly positiveである。

### 3.2 Shortest-path output

\[
d(a,b)=2,
\qquad
d(b,c)=3,
\qquad
d(a,c)=5
\]

である。`a→b→c` がdirect edge `a→c` より短い。

### 3.3 Axiom audit

| Axiom | Result | Reason in this case |
| --- | --- | --- |
| finite-valued | YES | connected finite graph |
| nonnegative | YES | positive edge sums |
| zero diagonal | YES | empty path has length 0 |
| identity | YES | distinct verticesを結ぶpathはpositive |
| symmetry | YES | undirected equal weights |
| triangle | YES | path concatenation |

Verdict:

> **STANDARD METRIC CONSTRUCTION FROM PREEXISTING WEIGHTED RELATION**

これは「metricが計算可能になった」ことを示すが、independent metric variableやphysical
spaceの生成は示さない。

---

## 4. Triangle inequality audit

shortest-path constructionでtriangle inequalityが成立する理由を分離する。

`x→y` の任意path `γ1` と `y→z` の任意path `γ2` はconcatenateでき、`x→z` walk
`γ1γ2` を与える。従って

\[
d(x,z)
\le
\operatorname{len}(\gamma_1)+\operatorname{len}(\gamma_2).
\]

infimumを取れば

\[
d(x,z)\le d(x,y)+d(y,z)
\]

となる。finite nonnegative caseではminimumが存在するため、同じことをshortest paths
のconcatenationとして直接書ける。

従ってCase A/Fのtriangle inequalityは別個のphysical lawとして追加されたのではなく、
path concatenationとinfimum definitionから従う。

ただしnegative-cycleで `-∞` が現れるcaseでは、ordinary real-valued metric axiomの
audit自体が適用できない。そこでtriangleを「成立」と形式的に押し通さない。

---

## 5. Case B — zero-weight edge

### 5.1 Input and output

\[
w(a,b)=0,
\qquad
w(b,c)=2,
\qquad
w(a,c)=5.
\]

すると

\[
d(a,b)=0,
\qquad a\neq b,
\]

\[
d(a,c)=d(b,c)=2.
\]

### 5.2 Axiom audit

nonnegativity、zero diagonal、symmetry、triangleは成立するが、identity of
indiscerniblesが失敗する。従ってprimary classificationは

> **PSEUDOMETRIC, NOT METRIC**

である。

### 5.3 Zero-distance quotient

\[
x\sim_0 y
\iff
d(x,y)=0
\]

と置く。このcaseのclassesは

\[
[a]=[b]=\{a,b\},
\qquad
[c]=\{c\}.
\]

pseudometricではclass representativesを変えてもclass間distanceが同じであり、

\[
\bar d([x],[y])=d(x,y)
\]

がwell-definedになる。checkerは二点quotient上でordinary metric axiomsが成立することを
確認した。

これはstandard metric identification / quotient constructionで十分であり、special
generative operationを必要としない。

---

## 6. Case C — disconnected graph

### 6.1 Input

undirected edge `a—b` にweight 1を与え、`c`をisolatedとする。

### 6.2 Policy C1 — infinity

到達不能pairについて

\[
d(x,y)=+\infty
\]

と定める。このcaseではordered unreachable pairsが4個ある。

\[
(a,c),(c,a),(b,c),(c,b).
\]

nonnegativity、identity、symmetry、extended triangle inequalityは成立するが、
finite-valuednessが失敗する。従って

> **EXTENDED METRIC, NOT AN ORDINARY FINITE METRIC**

である。

### 6.3 Policy C2 — componentwise

connected components

\[
\{a,b\},
\qquad
\{c\}
\]

ごとにrestrictionすれば、それぞれordinary metricを持つ。ただし異なるcomponents間の
単一distanceは与えない。

### 6.4 Policy C3 — undefined

到達不能pairでは `d` をpartial functionとしてundefinedにすることもできる。この場合、
全`V×V`上のmetricではなくcomponent-local distance familyになる。

Verdict:

> **DISTANCE STATUS DEPENDS ON THE DECLARED CODOMAIN / POLICY**

disconnectednessだけから「distanceが存在しない」とは言えない。

---

## 7. Case D — directed asymmetric relation

### 7.1 Input

positive directed cycleを

\[
a\to b,
\qquad
b\to c,
\qquad
c\to a
\]

とし、全arc weightを1とする。

### 7.2 Output

graphはstrongly connectedなので全distancesはfiniteだが、

\[
d(a,b)=1,
\qquad
d(b,a)=2.
\]

### 7.3 Classification

finite-valuedness、nonnegativity、zero diagonal、identity、triangleは成立するが、symmetry
が失敗する。本testで明示したconventionの下ではquasi-metricである。

> **ASYMMETRIC DISTANCE-LIKE STRUCTURE, NOT AN ORDINARY METRIC**

directed shortest-path distanceをsymmetrizeする選択も可能だが、`max`、`sum`、`min`など
どのpolicyを採用するかは元のdirected relationだけでは指定されない。

---

## 8. Case E — negative weights

### 8.1 E1: negative edge, no negative cycle

directed cycleを

\[
w(a,b)=-1,
\qquad
w(b,c)=2,
\qquad
w(c,a)=2
\]

とする。cycle totalは3でnegative cycleはない。graphはstrongly connectedなので全pairの
infimumはfiniteである。

しかし

\[
d(a,b)=-1,
\qquad
d(a,c)=1.
\]

従ってnonnegativityが失敗する。triangle inequalityはこのfinite matrixでは成立するが、
ordinary metricでも本testのquasi-metricでもない。

このcontrolは、negative edgeがあれば必ずundefinedになる、という過剰主張も避ける。
値はfiniteに決まってもmetric axiomが失敗し得る。

### 8.2 E2: negative cycle

\[
w(a,b)=1,
\qquad
w(b,c)=-3,
\qquad
w(c,b)=1.
\]

`b→c→b` のcycle totalは `-2` である。repeated walksを許すため、cycleへ到達でき、
そこから到達できるpairsでは

\[
d(x,y)=-\infty.
\]

checkerでは9 ordered pairs中6 pairsが `-∞` となり、`d(b,b)=-∞`も含む。zero diagonal、
nonnegativity、real-valuednessが壊れる。ordinary metric-style triangle auditは
**NOT APPLICABLE** とした。

Verdict:

> **NEGATIVE-CYCLE CASE IS ILL-BEHAVED AS A METRIC CONSTRUCTION**

これは「有用なstructureが一切ない」という結論ではない。例えばnegative-cycle detection
自体にはalgorithmic meaningがあるが、metric classificationとは別である。

---

## 9. Case F — relation only, edge-count construction

### 9.1 Input and rule

unweighted undirected path

\[
a-b-c
\]

を取り、path lengthをedge countと定義する。これは暗黙に各edgeへunit weight 1を与える
construction ruleと同じである。

### 9.2 Output

\[
d(a,b)=1,
\qquad
d(b,c)=1,
\qquad
d(a,c)=2.
\]

ordinary metric axiomsが成立する。

このcaseは

> metric-like structureにはcontinuous manifoldやdifferential geometryが常に必要である

という推論をKILLする。finite relationとedge-count ruleだけでmetricは定義できる。

ただしrelation「だけ」がunique metricを決めたわけではない。edge countという追加の
construction conventionを固定している。

---

## 10. Case G — same relation, different weights

Case Fと同じundirected relation

\[
a-b-c
\]

に対し、二weightingを比較する。

\[
w_1(a,b)=1,
\qquad
w_1(b,c)=1,
\]

\[
w_2(a,b)=2,
\qquad
w_2(b,c)=5.
\]

どちらもpositive weighted shortest-path metricを与えるが、

\[
d_{w_1}(a,c)=2,
\qquad
d_{w_2}(a,c)=7.
\]

よってunweighted relation structureだけではmetric valuesは一意でない。

> **SAME RELATION, DIFFERENT VALID METRICS**

relationがreachability/path alternativesを制約しても、length assignmentはweightingと
construction ruleに依存する。

---

## 11. Case H — distance transforms

Case Fのmetric `d` に三つのtransformを適用した。

### 11.1 Positive rescaling

\[
d_1(x,y)=2d(x,y).
\]

finite checkerではmetric axiomsがすべて保存された。

### 11.2 Positive off-diagonal shift

\[
d_2(x,x)=0,
\qquad
d_2(x,y)=d(x,y)+1\quad(x\neq y).
\]

このfinite caseでもmetric axiomsが保存された。元metricと数値は異なる。

### 11.3 Nonlinear square

\[
d_3(x,y)=d(x,y)^2.
\]

すると

\[
d_3(a,c)=4
>
d_3(a,b)+d_3(b,c)=2,
\]

となりtriangle inequalityが失敗する。

このcontrolは「monotone transformならmetric性が自動保存される」をKILLする。また、
positive rescaling等が可能なためmetric valuesのcanonicityはmetric axiomだけから出ない。

---

## 12. Coarse-graining control

### 12.1 Fixed microscopic input

Case Fのmicroscopic metricを固定し、quotient map

\[
q(a)=q(b)=AB,
\qquad
q(c)=C
\]

を固定する。

### 12.2 Three coarse policies

clusters `AB` と `C` のdistanceを次で定義する。

1. minimum intercluster distance:
   \[
   \bar d_{\min}(AB,C)=1
   \]
2. average intercluster distance:
   \[
   \bar d_{\mathrm{avg}}(AB,C)=\frac{2+1}{2}=1.5
   \]
3. representative `a` を使うdistance:
   \[
   \bar d_{a}(AB,C)=d(a,c)=2
   \]

二点quotient上では三つともordinary metricになるが、値は相互に異なる。

### 12.3 Result

microscopic relation、microscopic metric、cluster map `q`を固定しても、aggregation /
representative policyが未指定ならcoarse metricは一意に決まらない。

> **MICROSCOPIC DATA DO NOT BY THEMSELVES SELECT A UNIQUE COARSE METRIC POLICY**

これはfinite two-cluster controlであり、continuum limitやall coarse-grainingsについての
一般定理ではない。

---

## 13. Definitional construction and independent freedom

### 13.1 Uniquely derived metric

Case Aでweighted graph、directedness policy、path aggregation、unreachable-pair policyを
すべて固定すると、shortest-path matrix `d_G` は一意に計算される。

この意味では

> a metric became explicitly available

と言える。しかしtarget metric valuesはsource dataのfunctionであり、同じsource graphの
上でindependently variableではない。

前の[observable-independence test](./observable_independence_finite_model_v0.1_ja.md)の語で
言えば、unique model expansion / functional dependenceに近いcontrolである。

### 13.2 Independent metric field would be a different claim

independent metric degree of freedomを主張するなら、同一source relationの上に複数の
admissible metric assignmentsがあり、それらがspecified observationsやdynamicsで区別
されることなど、追加のsource/target/model-expansion specificationが必要になる。

Case Gはweights未固定なら複数metricsを作れることを示すが、weightsを外部から選んだだけ
であり、metricを生成するmechanismを示さない。

従って

\[
\text{uniquely definable metric}
\neq
\text{independently variable metric field}
\neq
\text{metric-generation mechanism}.
\]

---

## 14. Uniqueness / canonicity audit

### U1 — fully fixed weighted shortest-path specification

以下を固定する。

- vertex and edge sets
- directed / undirected interpretation
- edge weights
- admissible paths / walks
- path-length aggregation by sums
- infimum / minimum rule
- unreachable-pair codomain policy

このときfinite casesのdistance matrixはdeterministically一意に定まる。これは
construction-relative uniquenessである。

### U2 — relation only

weightsまたはedge-count conventionが未指定ならCase F/Gのように多数のmetricsが可能で
ある。relation aloneからunique metricは出ない。

### U3 — coarse-graining policy omitted

weighted graphとmicroscopic metricを固定しても、cluster distanceをminimum、average、
representative等のどれで作るかが未指定ならeffective/coarse metricは一意でない。

### Canonicity verdict

“canonical”をtechnical resultとして主張する証拠はない。U1のuniquenessは、入力と
construction ruleをすべて固定した関数評価の一意性であって、そのruleが唯一自然、
物理的、fundamentalであることを示さない。

---

## 15. Axiom-result table

| Case | Finite | Nonnegative | Identity | Symmetric | Triangle | Primary classification |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| A positive undirected connected | YES | YES | YES | YES | YES | metric |
| B zero edge | YES | YES | **NO** | YES | YES | pseudometric |
| B quotient | YES | YES | YES | YES | YES | metric |
| C disconnected, `+∞` policy | **NO** | YES | YES | YES | YES | extended metric |
| D directed positive cycle | YES | YES | YES | **NO** | YES | quasi-metric under stated convention |
| E1 negative edge, no negative cycle | YES | **NO** | YES | NO | YES | not metric/quasi-metric here |
| E2 negative cycle | **NO** | **NO** | **NO** | not central | NOT APPLICABLE | `-∞`-affected infimum |
| F unweighted edge count | YES | YES | YES | YES | YES | metric |
| G alternate positive weights | YES | YES | YES | YES | YES | different metric |
| H square transform | YES | YES | YES | YES | **NO** | not metric |

“Primary”としたのは、ordinary metricが同時にpseudometric等の弱いaxiom setも満たすため
である。

---

## 16. Main distinction under stress

次をlinear hierarchyとしては採用しないが、別claimとして維持する。

\[
\text{relation exists}
\neq
\text{distance function is definable}
\neq
\text{metric axioms hold}
\]

\[
\neq
\text{metric is unique/canonical}
\neq
\text{metric is operationally meaningful}
\neq
\text{physical space has emerged}.
\]

理由は次の通りである。

- relationがあってもdirected/disconnected/negative policyによりordinary metricにならない。
- distance-like functionが定義できてもidentity、symmetry、nonnegativity等が失敗し得る。
- metric axiomsが成立してもweights、transform、coarse policyで複数metricsがあり得る。
- uniquely computed metricでもそのuniquenessはfixed constructionに相対的である。
- mathematical metricだけではmeasurement operationやempirical spatial interpretationを含まない。

---

## 17. Evidence-burden audit

| Claim | Evidence supplied | What it establishes | What it does not establish |
| --- | --- | --- | --- |
| Case A shortest paths form a metric | exhaustive 3-node matrix + standard path-concatenation reason | stated finite model and standard construction | physical space or independent metric freedom |
| zero edge yields pseudometric | explicit `d(a,b)=0`, all other axiom checks | identity failure in Case B | every zero-weight graph has exactly this quotient |
| quotient metric exists | representative-independence + finite axiom check | Case B zero-class metricization | quotient is physically correct |
| disconnected graph has distance-like structure | `+∞`, componentwise, undefined policies | multiple standard treatments exist | one universally preferred policy |
| directed case is useful despite symmetry failure | explicit finite quasi-metric | failure of metric does not erase all structure | empirical directionality or geometry |
| negative cycle causes `-∞` | explicit reachable cycle under repeated-walk convention | six affected pairs in E2 | all negative-edge systems are ill-defined |
| relation does not fix metric values | same edge relation, two positive weightings | non-uniqueness without weighting | no canonical weighting can ever be justified |
| coarse metric is policy-dependent | one fixed `q`, three metric outputs | finite ambiguity under omitted aggregation rule | all coarse-graining is nonunique |
| space emerged | no evidence of required kind | nothing positive | operational/empirical spatial claim |

禁止する推論：

\[
\text{shortest path defines a metric}
\centernot\Rightarrow
\text{physical space was generated},
\]

\[
\text{one metric axiom fails}
\centernot\Rightarrow
\text{no useful distance-like structure exists},
\]

\[
\text{metric is uniquely derived under a fixed rule}
\centernot\Rightarrow
\text{metric is physically fundamental}.
\]

---

## 18. Hypothesis verdicts

### H-MET1

> any relation supports a metric.

**KILL under the relevant derived-distance reading.** Arbitrary directed、disconnected、negative
relationsのshortest-path outputはordinary metricにならない。carrier上にrelationと無関係な
discrete metricを置けるというliteral readingは可能だが、relation-to-metric claimとして
内容が弱すぎる。

### H-MET2

> a connected undirected positive weighted graph shortest-path construction yields a metric.

**RETAIN WITH SCOPE.** Case Aで全axiomsを確認し、triangleはpath concatenationから従う。
本checkerは有限exampleのsanity checkであり、一般result自体はstandard graph metric factで
ある。

### H-MET3

> zero-weight shortest path still always yields a metric.

**KILL.** Case Bでdistinct `a,b` がdistance zeroとなる。pseudometricおよびzero-distance
quotient metricは残る。

### H-MET4

> a disconnected relation has no meaningful distance structure.

**KILL.** `+∞`によるextended metric、componentwise metrics、partial/undefined policyが
利用可能である。どれを採るかはdeclared codomainと目的に依存する。

### H-MET5

> a directed relation naturally yields an ordinary metric.

**KILL.** Case Dはpositive・finite・triangle-preservingだがasymmetricである。本testの
conventionではquasi-metricであり、ordinary metricではない。

### H-MET6

> if a metric is definable from relation data, an independent metric structure has been generated.

**KILL.** Case A/Fのoutputはfixed source dataとconstruction ruleのfunctionであり、
independent variationを示さない。

### H-MET7

> relation data alone uniquely determines a metric.

**KILL.** same path relationにunit weightsとweights `(2,5)` を与えると `d(a,c)=2` と
`7` が得られる。coarse policyでも `1,1.5,2` に分岐する。

### H-MET8

> triangle inequality in a shortest-path metric requires an independent law.

**KILL.** applicable casesではpath concatenationとinfimum/minimum definitionから従う。
別のindependent lawとして追加する必要はない。

### H-MET9

> failure of ordinary metric axioms implies failure of every useful distance-like structure.

**KILL.** Case Bはpseudometric、Cはextended metric、Dはquasi-metricとして正確に分類
できる。E2だけをこれらと一括しない。

### H-MET10

> a standard metric construction establishes physical spatial emergence.

**KILL as an inference; physical emergence NOT ESTABLISHED.** Mathematical distanceの
constructionは、measurement、continuum approximation、empirical spatial interpretationを
供給しない。

---

## 19. Strongest results

### 19.1 Strongest standard-construction result

connected finite undirected graph、strictly positive weights、sum-based path length、shortest-path
ruleを固定すれば、ordinary metricが一意に計算される。zero weights、disconnection、
directedness、negative weightsを個別に緩めると、どのaxiomがどのように失われるかを
標準的なdistance notionsで記述できた。

### 19.2 Strongest nonequivalence result

「distance-like valueが定義できる」と「ordinary metric axiomsが成立する」は同じでない。
さらに「metricが成立する」と「そのvalues / coarse versionがcanonicalである」も同じで
ない。

### 19.3 Strongest negative result

全caseがstandard graph algorithms、metric axioms、pseudometric quotient、extended
distance、quasi-metric、coarse-policy comparisonで十分に記述できた。distinct generative
equationやspace-generation primitiveの必要性は一切出なかった。

### 19.4 Best false-positive control

Case Aが最も強いcontrolである。source weighted graphとruleを固定すれば完全なmetricが
新たに「利用可能」になるが、その値は一意にderivedであり、independent metric degree of
freedomでもphysical spaceでもない。

---

## 20. Checker

[relation_to_metric_boundary_v0.1.py](./relation_to_metric_boundary_v0.1.py)
はPython standard libraryだけを使い、次をassertする。

- Floyd–Warshall shortest-path matrices
- negative-cycle到達範囲への `-∞` propagation
- finite-valuedness、nonnegativity、zero diagonal、identity、symmetry、triangle
- Case A positive metric
- Case B pseudometricとzero-distance quotient metric
- Case C extended metric、components、unreachable pairs
- Case D finite asymmetric quasi-metric
- Case E1 finite negative distances without a negative cycle
- Case E2 six `-∞`-affected ordered pairs
- Case F edge-count metric
- Case G same relation / different metrics
- Case H rescaling、off-diagonal shift、square transform
- three coarse-graining policies

実行結果の主要部：

```text
case_a_d_a_c=5.0
case_b_d_a_b=0.0
case_b_zero_classes=[['a', 'b'], ['c']]
case_b_quotient_metric=True
case_c_unreachable_ordered_pairs=4
case_c_components=[['a', 'b'], ['c']]
case_d_d_a_b_vs_b_a=[1.0, 2.0]
case_e1_d_a_b_and_a_c=[-1.0, 1.0]
case_e2_negative_cycle_minus_inf_pairs=6
case_e2_triangle_audit=None
case_f_d_a_c=2.0
case_g_d_a_c=7.0
case_h_positive_rescaling_metric=True
case_h_off_diagonal_shift_metric=True
case_h_square_transform_triangle=False
coarse_policy_distances=[1.0, 1.5, 2.0]
coarse_policy_metrics=True
all_assertions_passed=True
```

checkerはencoded finite graph and distance factsだけを検証する。physical space、metric
emergence、geometry generation、universal reductionを証明しない。

---

## 21. What each input determines

### Relation data determines

- admissible adjacency / directedness
- which paths or walks exist
- connectivity / reachability pattern
- possible concatenations

relation data aloneは一般にedge length、symmetrization、unreachable-pair value、coarse policyを
決めない。

### Weighting determines

- cost assigned to each supplied edge
- zero / positive / negative edge behavior
- path-cost comparisons after an aggregation rule is fixed

weightingだけでもadmissible paths、sum rule、shortest/average policyは決まらない。

### Construction rule determines

- how edge values combine along a path
- whether minimum / infimum、edge count、resistance等を使うか
- directednessを保つかsymmetrizeするか
- unreachable pairsに `∞` / undefined / componentwise treatmentのどれを使うか
- whether and how zero-distance points are quotiented

### What remains extra choice

- weights when relation is unweighted
- transform / unit / scale
- coarse-graining map and aggregation policy
- representative selection
- target codomain and handling of infinities
- operational meaning and empirical calibration

### What is still needed for physical-space interpretation

最低限、distance observableのmeasurement procedure、units、physical referents、dynamicsとの
coupling、coarse/continuum map、approximation regime、empirical adequacyを別に示す必要がある。
これらが十分かは本実験では **OPEN** である。

---

## 22. Limited implication for later VED audit

VED本体へはまだ適用しない。将来、

\[
d_{ij}=-\log\widetilde S_{ij}
\]

とshortest weighted path、および

\[
d(x,y)^2\approx g_{\mu\nu}\Delta x^\mu\Delta x^\nu
\]

への接続を監査するとき、最低限次を分ける必要がある。

- domain and connectivity
- symmetry / directedness
- positivity and zero weights
- disconnected pairs and codomain policy
- metric versus pseudometric / extended / asymmetric structure
- uniqueness and empirical basis of weighting
- zero-distance quotient
- coarse-graining map and aggregation rule
- continuum approximation and error regime
- empirical spatial interpretation

このlistはVED distanceの妥当性または失敗を判定しない。とくに `-log` weightingのdomain、
symmetry、zero/infinite values、coarse continuum limitは本testで検査していない。

---

## 23. Current methodology status

### What is established

1. finite relation dataからstandard shortest-path constructionsによりmetric-like functionsを
   定義できる具体例がある。
2. positive、zero、disconnected、directed、negativeの条件差がaxiom statusを変える。
3. zero-distance quotientによりCase Bをmetricizeできる。
4. relation alone、transform choice、coarse policyはmetric valuesを一意に決めない。
5. fully fixed weighted shortest-path ruleはmetric matrixを一意に計算する。
6. triangle inequalityはapplicable shortest-path casesでconstructionから従う。

### What remains NOT ESTABLISHED

- independent metric degree of freedom generated by a mechanism
- a canonical weighting or coarse-graining policy
- continuum geometry
- physical or operational distance
- empirical spatial emergence
- a distinct generative equation
- universal reduction of spatial structure to graph relations

### Does this support a distinct generative equation?

**NO / NOT ESTABLISHED.** tested casesはstandard construction and axiom auditで尽くされた。
special generative notationが追加する検査可能な内容は見つからなかった。

### Does this strengthen only the audit methodology?

**YES, at present.** relation、weighting、path rule、codomain、quotient、coarse policy、physical
interpretationを別々に固定する必要性が具体化した。

---

## 24. Next recommended experiment

Phase 4で残る **rule-space-as-data control** を次にscopeする。

小さいrewrite systemで、

1. active rule setをdataとしてfixed meta-ruleが変更するencoding
2. operational semantics自体をstageごとに交換するencoding

を比較し、reachable configurations、rule provenance、future rule availability、translation
scopeを監査する。

このtestでもrule changeをdistinct generative equationと先に呼ばない。Phase 5のresidual
notation gateおよびVED reconstructionにはまだ進まない。

---

## 25. Final self-audit

- relation existence、distance definability、metric axioms、canonicity、physical spaceを分けた。
- positive exampleからspace generationを推論していない。
- metric axiom failureからall useful structure failureを推論していない。
- uniquely derived metricをindependent freedomと呼んでいない。
- disconnected policyを一つに固定していない。
- directed distanceをordinary metricと呼んでいない。
- negative edgeとnegative cycleを分けた。
- repeated-walk conventionを明記した。
- nonlinear transformのfinite counterexampleをgeneral classificationへ拡張していない。
- coarse controlをcontinuum theoremとして扱っていない。
- previous **NOT ESTABLISHED / DOWNGRADE** verdictsを維持した。
- VED本体を評価・変更していない。

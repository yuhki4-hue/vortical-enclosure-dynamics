# Law equation specification v0.1

> Status:
> - exploratory specification
> - not a theorem
> - not a definition of every scientific law
> - not a new formalism
> - VED-independent first pass

## 1. Working question

> 法則式は、何を固定したうえで、何を許容または禁止する記述なのか。

この文書は「法則とは必ず写像である」「法則とは必ず時間発展である」と定義しない。比較対象は、dynamical law、conservation law、constraint equation、probabilistic law、variational formulation、constitutive relation である。

## 2. Provisional specification record

法則式を単独の文字列として読まず、少なくとも次を伴う記述として監査する。

\[
\Sigma=(\mathcal L,X,\mathcal R,\mathcal O,\Theta).
\]

- \(\mathcal L\): 使用言語、変数の型、式の well-formedness。
- \(X\): states、configurations、fields、paths、probability distributions などの admissible objects。
- \(\mathcal R\): relations、constraints、transition relations、admissibility conditions。
- \(\mathcal O\): observables / operations。何を評価・比較できるか。
- \(\Theta\): parameters と背景構造。時間、測度、位相、微分構造、境界条件などを含み得る。

これは新しい mathematical object の提案ではなく、式を読む際の ordinary specification checklist である。分野によっては \(X\) が trajectory space を表し、\(\mathcal R\) が不要であり、\(\Theta\) の一部が \(X\) の定義へ吸収される。tuple の切り方自体に canonicality は主張しない。

## 3. Candidate forms

### 3.1 Discrete dynamics

\[
x_{n+1}=F_\theta(x_n).
\]

固定済みの \(X\)、index set、parameter \(\theta\)、map \(F_\theta:X\to X\) のもとで trajectory を定める。非決定的系なら map ではなく relation

\[
x_n\to x_{n+1}
\]

または set-valued map が必要になる。

### 3.2 Continuous dynamics

\[
\frac{dx}{dt}=F_\theta(x).
\]

この式は時間 parameter、微分可能性、tangent structure、initial / boundary data を前提にする。solution の存在・一意性は式の記載だけからは従わない。

### 3.3 Implicit differential / algebraic law

\[
F_\Sigma(x,\dot x,\ldots)=0,
\qquad
g_\Sigma(x)=0.
\]

law-like content は update algorithm ではなく、admissible states / jets / histories の部分集合を指定することにある。

### 3.4 Conservation law

\[
Q(x(t))=Q(x(0)),
\qquad
\frac{dQ}{dt}=0,
\]

または局所形

\[
\partial_t\rho+\nabla\cdot J=0.
\]

保存量、時間、divergence、domain、boundary flux を固定する必要がある。conservation は一般に state update の全内容を与えず、許容 trajectory を制約する。

### 3.5 Probabilistic law

\[
P_\theta(x,A),
\qquad
\mu_{n+1}(A)=\int_X P_\theta(x,A)\,d\mu_n(x).
\]

ここで law は一つの次状態を指定せず、conditional distribution や distribution evolution を制約する。測度構造と sigma-algebra は背景に含まれる。

### 3.6 Variational formulation

\[
x\in\operatorname*{arg\,min}_{z\in\mathcal A}S[z]
\quad\text{or}\quad
\delta S[x]=0.
\]

configuration / path class \(\mathcal A\)、functional \(S\)、allowed variations、boundary conditions を固定する。Euler–Lagrange equation との同値には regularity 等の追加条件が要る。

### 3.7 Constitutive relation

\[
J=-D\nabla \rho,
\qquad
\sigma=\mathsf C:\varepsilon.
\]

material response や effective closure を与える。conservation / balance lawとは別の役割を持ち、両者を組み合わせて evolution が閉じることがある。

## 4. Cross-form audit

| Form | Directly specifies | Usually presupposes | Does not by itself establish |
|---|---|---|---|
| deterministic dynamics | next state / vector field | state space、time/index、regularity | unique global solution、physical adequacy |
| transition relation | admissible step | configurations、labels/rules | probability、continuous time、unique run |
| constraint equation | admissible subspace | ambient objects、equation semantics | an update route |
| conservation law | invariant / balance | observable、time/domain、flux structure | full dynamics、fundamentality |
| probabilistic law | transition probabilities / distributions | measurable space、conditioning | realized trajectory、causal mechanism |
| variational form | stationary/minimizing histories | action、variation class、boundary data | unique minimizer、equivalence to another form |
| constitutive relation | response relation | selected variables、regime | conservation、microscopic derivation |

## 5. Initial hypothesis test

Working hypothesis:

> law-like description は、既に固定された specification の内部で、許容状態・関係・軌道・分布・変化を制約する。

### Support

- update equation は admissible trajectories を選ぶ。
- algebraic constraint は admissible states を選ぶ。
- conservation law は histories の一部を除外する。
- probabilistic law は admissible transition kernels / distributions を定める。
- variational principle は comparison class 内の stationary / minimizing histories を定める。
- constitutive relation は variable 間の admissible response を定める。

### Required revision

constraint を「状態集合を小さくすること」だけに限定すると狭すぎる。probabilistic law は weights を与え、equation は新しい trajectory を計算可能にし、constitutive law はモデルを closure することがある。したがってここでの constrain は、**固定仕様内で admissible relation / solution / distribution を特定する**という広い通常語である。

### Negative result

式の外形だけから law type は決まらない。同じ \(x'=F(x)\) でも、fundamental dynamics、effective model、numerical update、definition のいずれとしても使える。role は surrounding specification と claim に依存する。

## 6. Law equation audit record

ある式 \(E\) を law-like と評価する際は、最低限次を記録する。

1. **Language / types:** 変数と演算は well-defined か。
2. **Admissible objects:** states、histories、fields、distributions のどれか。
3. **Background structure:** time、topology、metric、measure、differential structure、order。
4. **Equation role:** update、constraint、balance、probabilistic、variational、constitutive、definition、measurement。
5. **Scope:** exact / effective / phenomenological / numerical / asymptotic のどれか。
6. **Solution notion:** classical、weak、distributional、stochastic 等。
7. **Evidence claim:** derivation、fit、well-posedness、prediction、structural consistency のどれを主張するか。
8. **Non-claim:** 式が単独では何を示さないか。

## 7. Relation to generation claims

固定した \(X\) 上の

\[
x_{n+1}=F(x_n)
\]

は通常の state transition を記述できる。その trajectory 上で新しい pattern が現れることはあり得るが、それだけでは source language、object class、degree of freedom、law space 自体が変わったことを意味しない。

逆に graph rewrite のように state が graph structureを含む場合、node / edge の追加は一つの state transition として完全に記述できる。したがって「state transition で書ける」ことは generation を否定せず、「state transition である」ことも独自な generative law を確立しない。この境界は [generative equation specification](./generative_equation_specification_v0.1_ja.md) で分解する。

## 8. Disposition

- **RETAIN:** law-like description の役割を、固定 specification 内の admissibility / evolution / weighting の指定として読む。
- **KILL:** law は必ず自己写像または時間発展式である、という狭い定義。
- **DOWNGRADE:** law equation を式の syntax class とみなすこと。現段階では式の role を指す説明語である。
- **OPEN:** specification 自体の変更を law の一部として扱うべきか、それとも meta-level rule として分けるべきか。標準 rewriting / operational semantics がこの区別を吸収する可能性がある。

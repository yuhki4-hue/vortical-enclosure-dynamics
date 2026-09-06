# Reachability-oriented theorem/proof anatomy: 加法可換律 stress test v0.1

## 0. Status / posture

本稿は **exploratory stress test** である。

- **not a theorem**
- **not a new proof theory**
- **not a new semantics**
- **not a new arithmetic foundation**
- **not a replacement for standard proof theory**
- **no new metric**
- **no rigidity score**
- **no geometry / topology**
- **no universal claim about all proofs**
- **no metaphysical conclusion**
- **no VED claim**

`reachability` は今回も ordinary derivability の working paraphrase に限定する。

\[
\text{“the target is reachable from \(\Gamma\)”}
\quad:=\quad
\Gamma\vdash\text{target}
\]

という説明上の略記以上の意味を与えない。新しい primitive、calculus、semantics、invariant、ordering は導入しない。

中心問いは次である。

> When induction, auxiliary lemmas, and multiple proof organizations are genuinely required,
> does the distinction between proof route failure and theorem-level derivability failure remain analytically useful?

先に結果を要約すると、**yes, as an audit distinction** である。named lemma の削除は modular route を壊しても、inline proof や別 organization により theoremhood を保持できる。一方、今回固定する弱い arithmetic presentation から induction を theory-level に削除すると、両加法再帰式を満たしながら可換律を偽にする明示的 model がある。したがって

\[
\text{ROUTE FAILURE}
\neq
\text{DERIVABILITY FAILURE}
\neq
\text{SETTING / CLAIM-IDENTITY MIGRATION}
\]

は前回より強い形で維持される。

ただし、この区別は標準的な proof dependency、axiom deletion、model-theoretic non-derivability の整理であり、新 proof theory ではない。negative result も先に固定する。`reachability` は依然として \(\vdash\) の言い換え、`proof route` は依然として derivation organization、`constraint propagation` は依然として ordinary induction bookkeeping の説明的 gloss に留まる。

---

## 1. 一つの標準 arithmetic setting を固定する

### 1.1 言語

一階等号論理の言語

\[
\mathcal L_{\mathrm A}=\{0,S,+\}
\]

を用いる。`0` は定数記号、\(S\) は一項関数記号、\(+\) は二項関数記号である。intended interpretation は standard natural numbers \(\mathbb N\)、zero、successor、ordinary addition である。

numeral abbreviations は今回の target と proof に不要なので導入しない。

### 1.2 theory \(\Gamma_{\mathrm A}\)

固定 theory は、Peano-style arithmetic のうち本テストに必要な部分を明示したものとする。

#### Logical background

- classical first-order logic;
- universal instantiation and universal generalization;
- modus ponens または同等の sequent / natural-deduction rules;
- equality reflexivity, symmetry, transitivity;
- equality substitution / congruence:
  \[
  a=b\Rightarrow S(a)=S(b),
  \]
  および function / formula context 内で equals may replace equals。

#### Successor background

\[
\tag{S0}\forall x\;S(x)\neq0,
\]

\[
\tag{S1}\forall x\forall y\;(S(x)=S(y)\to x=y).
\]

これらは standard Peano-style successor setting を明示するために含める。ただし、後の positive proof は S0/S1 を使用しない。

#### Addition recursion equations

加法は第二引数について再帰させる。

\[
\tag{Add-0}\forall x\;(x+0=x),
\]

\[
\tag{Add-S}\forall x\forall y\;(x+S(y)=S(x+y)).
\]

一階 presentation では \(+\) は primitive function symbol であり、Add-0/Add-S は nonlogical equations として theory に入る。同時に、それらの mathematical role は ordinary addition の recursive definition を与えることである。`fixed in this test`、`axiom in a presentation`、`definition in mathematical role` を同一分類にしない。

#### Induction

parameters \(\bar z\) を許す全 \(\mathcal L_{\mathrm A}\)-formula \(\varphi(n,\bar z)\) について、

\[
\tag{Ind}
\bigl(
\varphi(0,\bar z)
\land
\forall n(\varphi(n,\bar z)\to\varphi(S(n),\bar z))
\bigr)
\to
\forall n\,\varphi(n,\bar z)
\]

を induction schema として固定する。以下では induction variable と parameter を毎回明記する。

### 1.3 target と二つの level

target は

\[
\tag{Comm}\forall x\forall y\;(x+y=y+x)
\]

である。

- semantic statement:
  \[
  \mathbb N\models\mathrm{Comm};
  \]
- theorem-level derivability:
  \[
  \Gamma_{\mathrm A}\vdash\mathrm{Comm}.
  \]

本稿の `reachability` は後者だけを指す。theoremhood と intended-model truth を同一視しない。

---

## 2. 一つの explicit standard proof

第二引数再帰の presentation では、main induction をそのまま始めると左右の recursion orientation が揃わない。実際に必要になる補題だけを先に証明する。

### 2.1 Lemma L1 — left zero

\[
\tag{L1}\forall x\;(0+x=x).
\]

**Proof.** \(P(x)\equiv(0+x=x)\) と置き、\(x\) について induction する。

Base \(x=0\):

\[
0+0=0
\qquad\text{by Add-0 with \(x=0\).}
\]

Step: induction hypothesis

\[
\tag{IH1}0+x=x
\]

を仮定する。すると

\[
\begin{aligned}
0+S(x)
&=S(0+x)
&&\text{by Add-S}\\
&=S(x)
&&\text{by IH1 and congruence of \(S\).}
\end{aligned}
\]

Ind により \(\forall x(0+x=x)\)。\(\square\)

### 2.2 Lemma L2 — successor in the first argument

\[
\tag{L2}\forall x\forall y\;(S(x)+y=S(x+y)).
\]

**Proof.** \(x\) を arbitrary parameter として固定し、

\[
Q(y)\equiv\bigl(S(x)+y=S(x+y)\bigr)
\]

について \(y\) induction を行う。

Base \(y=0\):

\[
S(x)+0=S(x)
\qquad\text{by Add-0},
\]

また

\[
S(x+0)=S(x)
\qquad\text{by Add-0 and congruence}.
\]

従って symmetry / transitivity により

\[
S(x)+0=S(x+0).
\]

Step: induction hypothesis

\[
\tag{IH2}S(x)+y=S(x+y)
\]

を仮定する。すると

\[
\begin{aligned}
S(x)+S(y)
&=S(S(x)+y)
&&\text{by Add-S}\\
&=S(S(x+y))
&&\text{by IH2 and congruence}\\
&=S(x+S(y))
&&\text{by Add-S, read inside the outer \(S\).}
\end{aligned}
\]

最後の行は \(x+S(y)=S(x+y)\) から congruence により

\[
S(x+S(y))=S(S(x+y))
\]

を得て、その symmetry を使ったものである。Ind により \(\forall y\,Q(y)\)、arbitrary parameter \(x\) を generalize して L2 を得る。\(\square\)

### 2.3 Theorem — addition commutativity

\[
\forall x\forall y\;(x+y=y+x).
\]

**Proof.** \(x\) を arbitrary parameter として固定し、

\[
R(y)\equiv(x+y=y+x)
\]

について \(y\) induction を行う。

Base \(y=0\):

\[
\begin{aligned}
x+0
&=x
&&\text{by Add-0}\\
&=0+x
&&\text{by L1, symmetry.}
\end{aligned}
\]

従って \(x+0=0+x\)。

Step: induction hypothesis

\[
\tag{IH3}x+y=y+x
\]

を仮定する。すると

\[
\begin{aligned}
x+S(y)
&=S(x+y)
&&\text{by Add-S}\\
&=S(y+x)
&&\text{by IH3 and congruence}\\
&=S(y)+x
&&\text{by L2 with \(x:=y,\ y:=x\), symmetry.}
\end{aligned}
\]

従って \(x+S(y)=S(y)+x\)。Ind により

\[
\forall y\;(x+y=y+x).
\]

\(x\) は arbitrary だったので universal generalization により

\[
\Gamma_{\mathrm A}\vdash
\forall x\forall y\;(x+y=y+x).
\]

\(\square\)

### 2.4 何が実際に必要だったか

この modular route では L1 と L2 の両方が実際に使用された。

- L1 は main induction の base \(x+0=0+x\) を閉じる。
- L2 は main induction の step で \(S(y+x)\) を \(S(y)+x\) へ結ぶ。

どちらも飾りではない。ただし「この route が named lemma として必要とする」ことと、「theorem statement が L1/L2 を追加 assumption として必要とする」ことは別である。L1/L2 は \(\Gamma_{\mathrm A}\) 内で先に証明された theorems であって axioms ではない。

---

## 3. Four layers

### A — Fixed constraints

| kind | fixed item | role |
|---|---|---|
| logic | classical FOL, quantifier rules | admissible derivation を定める |
| equality machinery | reflexivity, symmetry, transitivity, congruence | local equations と IH を term context 内で運ぶ |
| induction | formula schema Ind | successor-generated partから universal statement へ進む |
| recursive equations | Add-0, Add-S | second-argument computation を定める |
| successor background | S0, S1 | Peano-style ambient を拘束する |
| intended structure | standard \(\mathbb N\) | ordinary arithmetic reading を固定する |
| definitions | \(+\) の recursive specification | operation を internal manipulation に供給する |

fixed status は formal type ではない。logic、rule、axiom schema、defining equation、semantic interpretation をすべて `axiom` と呼ばない。

### B — Theorem-level derivability

\[
\Gamma_{\mathrm A}\vdash
\forall x\forall y(x+y=y+x).
\]

これは少なくとも一つの admissible derivation が存在するという static claim であり、どの induction variable、lemma boundary、rewrite order を採ったかを記録しない。

### C — Actual proof route

今回の代表 route は次である。

1. \(x\)-induction で L1 を証明する。
2. parameter \(x\) を持つ \(y\)-inductionで L2 を証明する。
3. parameter \(x\) を持つ \(y\)-inductionで Comm を証明する。
4. main base で Add-0 + L1、main step で Add-S + IH3 + L2 を使う。

これは一つの modular derivation organization である。

### D — Formation history

今回実際に採った test-local construction history は次である。

1. second-argument recursion に合わせ、まず target の \(y\) induction skeleton を書いた。
2. base を展開すると \(x=0+x\) が未解決 obligation として残ったため L1 を分離した。
3. step を展開すると \(S(y+x)=S(y)+x\) が未解決 obligation として残ったため L2 を分離した。
4. L1/L2 をそれぞれ induction で証明し、main route へ戻した。
5. control として main induction variable を \(x\) に変えた route も構成した。
6. recursion orientation を変更する case は same-theory route でなく presentation change として別枠へ置いた。

これは mathematicians が歴史的にこの順で可換律を発見したという主張ではない。今回の stress test で route obligations を露出させた construction log だけである。

---

## 4. Main test: route dependence

### R1 — lemma を route から外す

#### L1 を library から外す

第2.3節の modular route は base で

\[
x+0=x
\]

までは進むが、\(x=0+x\) を閉じる named resource を失う。従って**その modular route は ROUTE FAILURE** である。

しかし \(\Gamma_{\mathrm A}\) は変わっていない。次の回避がある。

- L1 の induction proof を main base の前へ inline する。
- symmetry-oriented equivalent lemma
  \[
  \forall x\;(x=0+x)
  \]
  を証明して使う。
- L1 と L2 をまとめた mirrored-recursion package を先に証明する。

いずれも theory や target を変えない。従って theorem-level derivability は残る。

#### L2 を library から外す

main step は

\[
x+S(y)=S(x+y)=S(y+x)
\]

まで進むが、\(S(y+x)=S(y)+x\) を閉じる named resource を失う。これも modular route の **ROUTE FAILURE** である。

回避は可能である。

- L2 の \(y\)-induction proof を main proof の前または内部へ inline する。
- equivalent orientation
  \[
  \forall a\forall b\;(S(a+b)=S(a)+b)
  \]
  を使う。
- first-argument successor equationを導出済みの rewrite package として使う。

named lemma の消去は theorem axiom の消去ではない。

### R2 — induction variable を変える

同じ L1/L2 を先に得たうえで、\(y\) を parameter として \(x\) に induction する route を作れる。

Base \(x=0\):

\[
\begin{aligned}
0+y
&=y
&&\text{by L1}\\
&=y+0
&&\text{by Add-0, symmetry.}
\end{aligned}
\]

Step hypothesis:

\[
x+y=y+x.
\]

Then

\[
\begin{aligned}
S(x)+y
&=S(x+y)
&&\text{by L2}\\
&=S(y+x)
&&\text{by IH and congruence}\\
&=y+S(x)
&&\text{by Add-S, symmetry.}
\end{aligned}
\]

従って \(\forall x\forall y(x+y=y+x)\)。

二 route の差は実在する。

- \(y\)-induction route は左辺を Add-S で開き、右辺を L2 で閉じる。
- \(x\)-induction route は左辺を L2 で開き、右辺を Add-S で閉じる。

ただし、この二 route は完全に異質な proofs ではない。同じ mirrored equations L1/L2 と同じ induction machinery を使い、再帰 orientation の非対称性を左右から処理する homologous organizations である。`genuinely different` は induction variable と local dependency order の違いまでに限定し、proof space 全体の代表とはしない。

### R3 — recursion orientation を変える

first-argument recursive presentation を

\[
\tag{AddL-0}0+y=y,
\]

\[
\tag{AddL-S}S(x)+y=S(x+y)
\]

とする。この presentation では、元の Add-0/Add-S が mirrored helper lemmas になる。

これは単に original \(\Gamma_{\mathrm A}\) 内で induction variable を変えた route ではない。axiom / defining-equation list が変わるので、**別 presentation** である。

ただし induction を含む現在の setting では、

- Add-0/Add-S から induction により AddL-0/AddL-S、すなわち L1/L2 を導出できる。
- AddL-0/AddL-S から対称な induction argument により Add-0/Add-S を導出できる。

従って共通の logic、successor setting、full induction schema のもとで、両 presentation は relevant additive fragment について mutually derivable である。これは qualification 付きの equivalent presentation であり、syntax と axiom list が literal に identical という意味ではない。とくに induction を消去した後まで同値性を自動延長してはならない。

---

## 5. Stronger erasure levels

前回の E1/E2/E3 を、今回も test-local diagnostic questions として再利用する。formal taxonomy には昇格させない。

### E1 — Route erasure

one named lemma、one induction arrangement、one rewrite occurrence、one library resource を特定 route から消す。

中心質問：

> この具体的 derivation organization は壊れるか。

L1/L2 library erasure、\(y\)-induction arrangement の禁止が例である。theory \(\Gamma_{\mathrm A}\) は保持される。

### E2 — Derivability erasure

Ind、Add-0、Add-S のような theory-side support を削除する。

中心質問：

> reduced theory が許すあらゆる proof route を考えても Comm は derivable か。

一つの proof failure だけでは答えない。第6–7節では target を偽にする explicit model / interpretation を与え、soundness により non-derivability を確認する。

### E3 — Setting / identity erasure

domain、successor structure、operation interpretation、logic / equality notion を変更する。

中心質問：

> まだ ordinary natural-number addition の同じ Comm を問うているか。

同じ glyph `+` を残しても operation が違えば claim identity は保たれない。

### Interim verdict

\[
\text{ROUTE FAILURE}
\neq
\text{DERIVABILITY FAILURE}
\neq
\text{SETTING / CLAIM-IDENTITY MIGRATION}
\]

は今回も維持される見込みがある。ただしこれを確認するには、E2 で countermodel を実際に示す必要がある。

---

## 6. Induction erasure

### 6.1 Reduced theory

\(\Gamma_{\mathrm A}^{-\mathrm{Ind}}\) を、\(\Gamma_{\mathrm A}\) から induction schema だけを外し、logic、equality、S0、S1、Add-0、Add-S を保持した theory とする。

L1、L2、main theorem の三 induction proofs はすべて壊れる。しかし、この事実だけから

\[
\Gamma_{\mathrm A}^{-\mathrm{Ind}}\nvdash\mathrm{Comm}
\]

とはまだ言えない。別 route の可能性があるからである。

### 6.2 Explicit countermodel

domain \(D\) を二つの disjoint successor chains

\[
D=\{n_m:m\in\mathbb N\}\;\dot\cup\;\{z_k:k\in\mathbb Z\}
\]

の和とする。\(n_m\) は standard one-sided chain、\(z_k\) は bi-infinite chain である。

zero と successor を

\[
0^D=n_0,
\]

\[
S(n_m)=n_{m+1},\qquad S(z_k)=z_{k+1}
\]

で定める。\(S\) は injective で、どの \(S(a)\) も \(n_0\) ではない。従って S0/S1 を満たす。

addition を、右引数の chain に応じて次で定める。

\[
\tag{A}a+n_m:=S^m(a),
\]

\[
\tag{B}a+z_k:=z_{k+1}
\qquad
\text{for every \(a\in D,\ k\in\mathbb Z\).}
\]

#### Add-0 check

\[
a+0^D=a+n_0=S^0(a)=a.
\]

従って Add-0 を満たす。

#### Add-S check on the \(n\)-chain

\[
a+S(n_m)
=a+n_{m+1}
=S^{m+1}(a)
=S(S^m(a))
=S(a+n_m).
\]

#### Add-S check on the \(z\)-chain

\[
a+S(z_k)
=a+z_{k+1}
=z_{k+2},
\]

一方、

\[
S(a+z_k)=S(z_{k+1})=z_{k+2}.
\]

従って Add-S も満たす。

#### Commutativity failure

\[
0^D+z_0=z_1
\]

だが、

\[
z_0+0^D=z_0
\]

であり、\(z_1\neq z_0\)。従って Comm はこの model で偽である。

### 6.3 Why induction fails in this model

\[
\varphi(u)\equiv(0+u=u)
\]

を考える。

- \(\varphi(n_0)\) は真。
- \(\varphi(u)\to\varphi(S(u))\) は全 \(u\) で真。\(n\)-chain では true が successor へ保存され、\(z\)-chain では antecedent が false。
- しかし \(\varphi(z_0)\) は \(z_1=z_0\) を要求するので偽。

従って induction instance for \(\varphi\) は失敗する。この model が induction-free setting にだけ許される追加 chain を持つことが、明示的に確認できる。

### 6.4 Derivability verdict

\(D\models\Gamma_{\mathrm A}^{-\mathrm{Ind}}\) かつ \(D\not\models\mathrm{Comm}\) である。sound first-order calculus では、もし reduced theory から Comm が derivable なら全 model で真でなければならない。従って

\[
\Gamma_{\mathrm A}^{-\mathrm{Ind}}
\nvdash
\forall x\forall y(x+y=y+x).
\]

判定は **DERIVABILITY FAILURE** である。単なる ROUTE FAILURE ではない。

この判定は、指定した reduced theory に相対する。別の induction-free theory が commutativity を axiom や別の強い principle として持つ可能性を否定しない。「induction なしでは数学的に可換律を絶対に証明できない」という無制限主張ではない。

---

## 7. Addition clause erasure

### F1 — Add-0 を外す

\(\Gamma_{\mathrm A}^{-\mathrm{Add0}}\) は Add-S、Ind、successor axioms を保持する。

standard domain \(\mathbb N\)、standard \(0,S\) 上で glyph \(+\) を次の operation \(\oplus\) として解釈する。

\[
a\oplus b:=2a+b.
\]

ここで \(1=S(0)\)、\(2=S(S(0))\) は counterinterpretation を説明するための最小限の metalinguistic numeral abbreviations である。

すると

\[
a\oplus S(b)=2a+(b+1)=S(2a+b)=S(a\oplus b),
\]

なので Add-S を満たす。一方、

\[
1\oplus0=2,\qquad 0\oplus1=1,
\]

なので commutativity は偽である。Add-0 は \(1\oplus0=1\) を要求するが満たされない。

standard \(\mathbb N\) 上の expansion なので、全 first-order induction instances は保たれる。従って failure は induction loss のせいではない。

判定：

- modular proof の base、L1/L2 base が壊れるので **ROUTE FAILURE**;
- counterinterpretation があるので reduced theory で **DERIVABILITY FAILURE**;
- 残った Add-S だけでは \(+\) の value at right zero を固定せず、その自由度が全右 successor へ伝わるので **UNDERDETERMINATION OF \(+\)**。

### F2 — Add-S を外す

\(\Gamma_{\mathrm A}^{-\mathrm{AddS}}\) は Add-0、Ind、successor axioms を保持する。

standard \(\mathbb N\) 上で

\[
a\oplus b:=a
\]

という left-projection operation を glyph \(+\) の interpretation とする。これは

\[
a\oplus0=a
\]

なので Add-0 を満たす。しかし

\[
1\oplus2=1,\qquad 2\oplus1=2
\]

であり可換でない。standard \(\mathbb N\) 上なので induction schema は保持される。

判定：

- L1 step、L2 step、main step の recursion が使えず **ROUTE FAILURE**;
- target-falsifying interpretation があり **DERIVABILITY FAILURE**;
- positive right arguments での operation が拘束されず **UNDERDETERMINATION OF \(+\)**。

### 7.1 Clause-erasure summary

| erased support | remaining clause satisfied by | Comm? | diagnosis |
|---|---|---:|---|
| Add-0 | \(a\oplus b=2a+b\) on standard \(\mathbb N\) | false | route + derivability failure; underdetermination |
| Add-S | \(a\oplus b=a\) on standard \(\mathbb N\) | false | route + derivability failure; underdetermination |

この二例は ordinary addition の反例ではない。reduced axioms が別 operations を許すことを示す counterinterpretations である。

---

## 8. Lemma necessity と route convenience

### 8.1 Library lemma deletion

L1/L2 の statement と proof を library から削除しても、\(\Gamma_{\mathrm A}\) の axiom set は変わらない。従って起きるのは modular route の failure であり、theorem theory の weakening ではない。

### 8.2 Inline replacement

`fully expanded proof` では、L1/L2 という name と別 section boundary を消し、その induction derivations を main proof の前提 obligation が現れた位置へ埋め込める。このとき derivation tree の subtrees は残るが、library nodes は消える。

従って

\[
\text{named lemma necessary for a route}
\not\Rightarrow
\text{lemma is a theorem assumption}.
\]

### 8.3 Equivalent lemma replacement

main proof に必要な equality orientation に合わせ、

\[
\tag{L1'}\forall x\;(x=0+x),
\]

\[
\tag{L2'}\forall a\forall b\;(S(a+b)=S(a)+b)
\]

を用いてもよい。これらは L1/L2 の equality symmetry による variants である。route record は変わるが theory と target は変わらない。

### 8.4 Organization change

\(y\)-induction route と \(x\)-induction route は L1/L2 を反対側で用いる。さらに L1/L2 を先に `mirrored recursion package` として証明する、必要時に inline する、first-argument presentation から始める、という organizations がある。

### 8.5 Is lemma-content theorem-level load-bearing?

慎重な答えは二段階になる。

1. **Named lemma nodes are not theorem-level assumptions.** L1/L2 は \(\Gamma_{\mathrm A}\) から導出されるので、library から外しても theoremhood は変わらない。
2. **Their mathematical content is not arbitrary decoration.** Add-0/Add-S のもとで Comm から L1/L2 を回収できる。

実際、

\[
0+x=x+0=x
\]

なので Comm + Add-0 から L1 が従う。また

\[
\begin{aligned}
S(x)+y
&=y+S(x)
&&\text{by Comm}\\
&=S(y+x)
&&\text{by Add-S}\\
&=S(x+y)
&&\text{by Comm and congruence}
\end{aligned}
\]

なので Comm + Add-S から L2 が従う。

従って lemma contents は theorem と密接だが、**proof premise として外部から追加された assumptions ではない**。今回の anatomy で最初に付けるべき status は `route-compression / derived-resource` であり、`axiom` ではない。

---

## 9. Proof compression

### 9.1 Fully expanded proof

L1/L2 の names を使わず、必要な subderivations を main derivation tree 内へ inline する。formal content は第2節と同じで、三つの induction instancesに対応する subtrees が残る。

### 9.2 Lemma-based proof

第2節の route である。L1/L2 の proofs を一度閉じ、main induction では lemma instances を呼ぶ。dependency boundary が見やすくなる。

### 9.3 Alternate induction proof

第4節 R2 の \(x\)-induction route である。同じ theorem、同じ \(\Gamma_{\mathrm A}\)、同じ helper contents を持つが、Add-S と L2 が左右で担う local role を交換する。

### 9.4 Compression verdict

| record | preserves | erases / hides |
|---|---|---|
| theorem statement Comm | target formula | all route organization |
| theoremhood \(\Gamma_{\mathrm A}\vdash\mathrm{Comm}\) | theory-relative derivability status | chosen proof witness |
| expanded proof | every induction and rewrite occurrence | modular lemma boundary |
| lemma-based proof | reusable dependency nodes | internal lemma steps when omitted from display |
| formation history | why this organization was selected | other unrecorded possible searches |

短い proof が stronger proof とは限らない。長い proof が more foundational とも限らない。compression は record granularity と reuse の違いであり、theorem strength の尺度ではない。

---

## 10. Dependency audit

### 10.1 Subproof-level audit

| proof component | induction instance | Add-0 | Add-S | equality machinery | helper lemma | unused ambient |
|---|---|---:|---:|---|---|---|
| L1 | \(P(x):0+x=x\) | base | step | congruence, transitivity | none | S0, S1 |
| L2 | \(Q(y):S(x)+y=S(x+y)\), parameter \(x\) | base, both sides | step, both sides | symmetry, transitivity, congruence | none | S0, S1 |
| Comm, \(y\)-route | \(R(y):x+y=y+x\), parameter \(x\) | base | step | symmetry, transitivity, congruence | L1 in base; L2 in step | S0, S1 |
| Comm, \(x\)-route | \(T(x):x+y=y+x\), parameter \(y\) | base | step | symmetry, transitivity, congruence | L1 in base; L2 in step | S0, S1 |

### 10.2 Theory inclusion vs actual use

| ingredient | included in \(\Gamma_{\mathrm A}\)? | used in displayed positive proof? | theory-level load-bearing in tested erasure? |
|---|---:|---:|---:|
| classical quantifier logic | yes | yes | not separately erased |
| equality congruence/transitivity/symmetry | yes | yes | not separately erased |
| S0: \(Sx\neq0\) | yes | no | no evidence from this theorem |
| S1: successor injectivity | yes | no | no evidence from this theorem |
| Add-0 | yes | yes | yes relative to tested reduction; F1 countermodel |
| Add-S | yes | yes | yes relative to tested reduction; F2 countermodel |
| full induction schema | yes | three instances used | yes relative to \(\Gamma_{\mathrm A}^{-\mathrm{Ind}}\); explicit countermodel |
| intended standard \(\mathbb N\) | semantic reading | not a derivation premise | fixes ordinary claim identity |

`included in background` と `actually load-bearing in this proof` は同じでない。S0/S1 は ordinary Peano-style setting の一部だが、displayed proof からは使われていない。逆に induction は theorem statement に局所 assumption として書かれないが、この theory presentation では derivability に load-bearing である。

---

## 11. Counterfactual proof-route test

Route A を main \(y\)-induction、Route B を main \(x\)-induction とする。

| dependency | Route A only | Route B only | both |
|---|---:|---:|---:|
| main induction formula \(x+y=y+x\) indexed by \(y\) | yes | no | no |
| main induction formula \(x+y=y+x\) indexed by \(x\) | no | yes | no |
| Add-S opens left side of main step | yes | no | no |
| Add-S closes right side of main step | no | yes | no |
| L2 closes right side of main step | yes | no | no |
| L2 opens left side of main step | no | yes | no |
| L1 content | no | no | yes |
| L2 content | no | no | yes |
| Add-0/Add-S | no | no | yes |
| induction machinery | no | no | yes |
| equality congruence/transitivity | no | no | yes |

この表が示すのは二つの displayed routes の dependency intersection だけである。

> shared by two routes
> does not imply
> theorem-level necessary.

theorem-level necessity を示すには、全 proof space を量化する metatheorem、independence result、または今回のような reduced-theory countermodel が必要である。二 route の共通 field を数えるだけでは足りない。これは minimal separating field-set test の

\[
\text{pairwise distinction}\neq\text{explanatory adequacy}
\]

という negative result と一致する。

---

## 12. Formation-history stress

### 12.1 Proof repair without theorem change

第3節 D の test-local history は、

\[
\text{direct induction skeleton}
\to
\text{open base/step obligations}
\to
\text{helper lemmas}
\to
\text{closed proof}
\]

という organization change を持つ。

その間、

- target Comm は変わらない。
- \(\Gamma_{\mathrm A}\) は変わらない。
- domain は変わらない。
- operation interpretation は変わらない。
- assumptions は追加されない。

追加されたのは外部 premise でなく、既存 theory から導出した intermediate theorems と modular boundaries である。従ってこれは theorem-level terrain change ではなく **route reorganization / proof repair** と記述できる。

induction variable を \(y\) から \(x\) へ変える control も同様である。target / theory は同じまま、local obligations の左右配置が変わる。

### 12.2 What would count as theorem change?

次は同じ proof repair として扱えない。

- Comm 自体を axiom として追加する：theory extension であり、元 theory からの proof ではない。
- domain を successor-generated finite initial segmentだけに restriction する：domain / statement scope が変わる。
- target を \(\forall x(x+0=0+x)\) に weaken する：successor claim / weaker theorem である。
- hypothesis `\(x=0\) or \(y=0\)` を追加する：conditional target への変更である。
- operation を別の commutative operation に置換する：interpretation / claim identity の変更である。

これらを採った記録が元 Comm と同じ endpoint status を `established` と書いても、same theorem proof とみなせない。

### 12.3 Connection to proof-formation results

proof-formation 系の結果を今回へ移すと次のようになる。

1. **action classification instability:** `introduce lemma`、`inline derivation`、`change induction variable` という label は record typing であり、theoremhood から一意に回収されない。
2. **semantic collapse of different histories:** Route A/B は同じ theorem-level result に至るが histories は異なる。
3. **record-frame dependence:** theorem statementだけの frame は全 route differences を消し、annotated derivation frame は induction variable と lemma calls を保つ。
4. **cross-frame persistence caution:** 全 frame が target を保持するよう設計されていれば theorem の persistence は projector design にも依存する。
5. **visibility-transition caution:** route detail が richer record で初めて visible でも、late visibility は depth や importance の尺度ではない。
6. **non-nested-frame caution:** lemma-call field、raw derivation field、formation-note field は別々に保持・消去でき、visibility sequence は canonical でない。
7. **minimal-separator failure:** `induction_variable=y` 一 fieldが routes を分離しても、それは validity や dependency necessity を説明しない。

今回の positive addition は、history difference を merely record するだけでなく、**theory unchanged / target unchanged** を同時に監査すれば proof repair と theorem change を区別できることにある。ただし identity legitimacy や naturalness が record から自動的に決まるわけではない。

---

## 13. Static theoremhood vs historical theoremhood record

### Static

\[
\Gamma_{\mathrm A}\vdash
\forall x\forall y(x+y=y+x).
\]

この assertion は route witness の存在を述べるが、その identity を指定しない。

### Historical

今回の representative proof record は、

- second-argument recursion;
- L1 by \(x\)-induction;
- L2 by \(y\)-induction with parameter \(x\);
- Comm by \(y\)-induction with parameter \(x\);
- Add-S → IH3 → L2 という main step order;
- 後から \(x\)-induction route を control として構成;

を含む。

同じ static theoremhood からこの history は逆算できない。前回の \(1+1=2\) では複数 route の差が一行の macro / inline choiceに近かった。今回は induction variable、三つの induction instances、helper-lemma boundaries、local rewrite roles が theoremhood から消えるため、**static / historical separation は前回より明確に見える**。

しかしこれは theoremhood が histories の formal quotient であるという新定義ではない。標準的 theorem statement が proof object を記録しないという事実を、formation-history audit と接続しただけである。

---

## 14. Does theorem-as-route-organization improve?

working hypothesis:

> theorem may be usefully viewed as a stable reachability relation
> across multiple proof organizations.

### 14.1 What the two routes show

Route A/B は、

- same \(\Gamma_{\mathrm A}\);
- same target Comm;
- different main induction variable;
- different local use of Add-S and L2;
- same theoremhood;

を持つ。従って theorem-level information は any one route record より粗く、route-specific でないことが前回より具体的に確認できる。

### 14.2 What they do not show

二 route の存在は、

- theorem に新しい invariant がある;
- proof space に topology / geometry がある;
- theorem が metaphysically stable である;
- all routes が一つの canonical class を作る;
- route-independent strength を測れる;

ことを示さない。

`stable` はこの test では「複数の明示した organizations のいずれでも同じ sequent が導出された」という限定的記述にすぎない。`robust` や `route-independent` を formal invariant にしない。

### 14.3 Verdict

前回より pedagogically vivid だが、mathematically は依然として

\[
\Gamma_{\mathrm A}\vdash\mathrm{Comm}
\]

と「異なる derivations が同じ conclusion を持つ」という標準事実で尽くされる。**REVISE / DOWNGRADE:** `theorem-as-stable-reachability` は audit gloss として保持できるが、新 analytical object ではない。

---

## 15. Does “constraint propagation” improve?

induction を含む三つの step を分解する。

| induction step | fixed hypothesis / parameter | induction hypothesis | defining equation | equality operation | newly derived statement |
|---|---|---|---|---|---|
| L1 | target form \(0+u=u\) | \(0+x=x\) | \(0+Sx=S(0+x)\) | congruence under \(S\) | \(0+Sx=Sx\) |
| L2 | arbitrary parameter \(x\) | \(Sx+y=S(x+y)\) | Add-S on \(Sx+y\) and \(x+y\) | congruence, symmetry, transitivity | \(Sx+Sy=S(x+Sy)\) |
| Comm Route A | arbitrary parameter \(x\) | \(x+y=y+x\) | \(x+Sy=S(x+y)\) | congruence, symmetry, transitivity | \(x+Sy=Sy+x\) |
| Comm Route B | arbitrary parameter \(y\) | \(x+y=y+x\) | \(y+Sx=S(y+x)\) | congruence, symmetry, transitivity | \(Sx+y=y+Sx\) |

`constraint propagation` という語は、fixed recursion equation、temporary induction hypothesis、equality transport が違う status を持ちながら一 step に合流することを見やすくする。

しかし

> “constraint propagation” says more than ordinary induction bookkeeping?

への答えは **mostly no** である。表の各行は標準的 induction proof の bookkeeping で完全に記述できる。追加価値は、IH を permanent axiom と誤認せず、defining equation と equality rule と分けて表示する監査上の見通しだけである。physical causation、truth production、force transmission の含意は KILL する。

---

## 16. Deep fixed constraints

`deepness score` は作らない。代わりに、役割と tested dependence を分ける。

| support | status | displayed routes | erasure result |
|---|---|---|---|
| logic / quantifiers | inference machinery | generalization と induction use に必要 | not separately tested |
| equality | inference machinery | every nontrivial step | not separately tested |
| induction | axiom schema / rule, presentation-dependent | L1, L2, Comm | removal admits explicit noncommutative model |
| Add-0 | recursive defining equation | all bases | removal admits \(2a+b\) interpretation |
| Add-S | recursive defining equation | all steps | removal admits left projection |
| S0/S1 | mathematical successor axioms | unused | no load-bearing result here |
| standard domain interpretation | semantic background | not a syntactic proof premise | ordinary claim identity を固定 |
| ordinary \(+\) interpretation | semantic background / intended model | equations reflect it | change causes claim migration |

前回の \(1+1=2\) は induction を使わず、deep background の多くが unused だった。今回は induction が route-visible であるだけでなく、指定した reduced theory に対する countermodel separation により theorem-level support としても確認された。ここが前回からの最大の実質的増分である。

ただし first-order induction schema は formal setting の一部であって metaphysical foundation claim ではない。別 formalization で commutativity を別 axioms や recursion principles から得る可能性を否定しない。

---

## 17. Representation-preserving change

### 17.1 Pure notation rename

\[
0\mapsto z,\qquad S\mapsto\sigma,\qquad +\mapsto\oplus
\]

という signature isomorphism を行い、

\[
a\oplus z=a,\qquad
a\oplus\sigma(b)=\sigma(a\oplus b)
\]

および対応する induction schema を保つ。第2節の各 formula を一様に translate すれば、

\[
\forall a\forall b\;(a\oplus b=b\oplus a)
\]

の derivation が得られる。これは representation-preserving re-derivability である。

### 17.2 Equivalent recursive presentation

第4節 R3 の first-argument presentationでは AddL-0/AddL-S が primitive defining equations になり、Add-0/Add-S を mirrored lemmas として induction で得る。その後、同じ形の commutativity proofを再構成できる。

inductionを含む common background のもとで両 equation packages が mutually derivable であることが preservation condition である。単に「どちらも addition と呼ぶ」から identical theories なのではない。

### 17.3 Verdict

notation change と equivalent presentation change の双方で corresponding commutativity relation は再導出された。ただし前者は signature renaming、後者は axiom presentation と primitive/derived role の交換であり、同じ種類の変更ではない。

---

## 18. Structure-change control

standard domain \(\mathbb N\) と numerals を保ちつつ、glyph `+` を

\[
a\star b:=2a+b
\]

と解釈する。すると

\[
1\star0=2,\qquad 0\star1=1,
\]

なので

\[
\forall a\forall b(a\star b=b\star a)
\]

は偽である。

これは ordinary natural-number addition theorem の反証ではない。operation interpretation を変え、Add-0 も失っている。

判定：

- **SETTING / OPERATION MIGRATION**;
- ordinary Comm に対する **CLAIM-IDENTITY BREAK**;
- altered operation 内での noncommutativity。

同じ glyph、同じ carrier set、同じ quantifier shape は、operation meaning の保存を保証しない。

---

## 19. Strong falsification questions

### Q1. Does route failure / derivability failure separation remain useful here?

**Yes.** L1/L2 library deletion は modular route のみを壊し、inline / equivalent-lemma / alternate-induction routes が残る。Ind deletion は explicit target-falsifying model を許す。両者を同じ `proof failed` と書くと theorem-level status を誤る。

### Q2. Does induction make the separation more informative than in \(1+1=2\)?

**Yes, materially within this test.** 前回は defining equations の数 step と lemma macro の差だった。今回は三つの induction instances が route structure を持ち、さらに induction-free countermodel が theorem-level dependence を示す。E1/E2 の差が単なる inline / macro differenceを越えた。

### Q3. Are helper lemmas theorem-level necessities or route-level conveniences?

**Named lemmas are route-level derived resources / compression devices.** L1/L2 の named nodes は axioms でも external assumptions でもない。contents は target と defining equationsに密接で、Comm からも回収できるが、別 proof organization で names を消せる。従って `lemma required by this modular proof` と `lemma required as a theorem assumption` は分離される。

### Q4. Can two proof organizations expose different dependencies?

**Yes, locally.** \(y\)-induction route は Add-S で left sideを開き L2 で right sideを閉じ、\(x\)-induction route は L2 で left sideを開き Add-S で right sideを閉じる。ただし両 route は同じ helper contents と inductionを共有する homologous proofs であり、全 proof space の diversityを示さない。

### Q5. Does theorem-as-reachability remain mostly ordinary derivability?

**Yes.** \(\Gamma_{\mathrm A}\vdash\mathrm{Comm}\) 以上の数学的内容は得られない。multiple routes は theoremhood が route record より粗いことを可視化するが、新 invariant を与えない。

### Q6. Does proof-as-route remain mostly ordinary derivation?

**Yes.** induction variable、lemma dependencies、rewrite orderを持つ derivation tree / sequence で尽くされる。

### Q7. Does formation history add information not contained in theoremhood?

**Yes.** どの direct skeleton がどの obligation を残し、L1/L2をいつ分離し、どの induction variableへ変更したかは theoremhood に含まれない。ただし history record は選択の正当性や唯一性を自動判定しない。

### Q8. Does the new anatomy reveal anything v1.1 did not already record?

**Limited yes.** v1.1 は theorem assumptions と proof resources をすでに分けていた。今回の追加は、それを E1 route erasure / E2 theory erasure / E3 setting-identity change という別 test にし、named lemma deletion と induction deletionを同じ Erasure result にしないことである。発見された数学は standard arithmetic / model theory の範囲内であり、新 theorem content はない。

### Q9. Is the added value methodological rather than mathematical?

**Yes.** 追加価値は dependency audit、counterfactual classification、static/history separation の運用にある。可換律の proof、countermodels、presentation equivalence は標準的対象であり、reachability vocabulary が新しい mathematics を生んでいない。

---

## 20. Candidate findings

| candidate | result | reason |
|---|---|---|
| C1 route failure and theorem derivability failure remain distinct | **SUPPORTED strongly** | lemma erasure vs induction/clause countermodels |
| C2 induction can be route-visible while theoremhood remains route-agnostic | **SUPPORTED** | theoremhood omits all three induction instances |
| C3 helper lemmas compress route without becoming theorem assumptions | **SUPPORTED strongly** | inline and equivalent variants preserve \(\Gamma\) |
| C4 different induction organizations expose different local dependencies | **SUPPORTED with qualification** | Add-S/L2 roles swap; lemma set remains same |
| C5 proof history carries information erased by theoremhood | **SUPPORTED** | obligation discovery and organization are absent from sequent |
| C6 theorem statement is less route-specific than any one proof | **SUPPORTED** | Routes A/B share target |
| C7 reachability adds little beyond standard derivability | **SUPPORTED strongly as negative result** | no new object or consequence |
| C8 constraint propagation adds little beyond ordinary bookkeeping | **SUPPORTED strongly as negative result** | induction table exhausts content |
| C9 E1/E2/E3 survives a nontrivial theorem | **SUPPORTED** | explicit examples at each level |
| C10 strongest revision is route / theorem / setting-identity separation | **SUPPORTED test-locally** | old proof-resource distinction gains separate erasure questions |

C4 は誇張しない。二 routes は local dependency order が異なるが、独立な axiom packages や radically different proof methods を使うわけではない。

---

## 21. RETAIN / REVISE / DOWNGRADE / KILL

複数 disposition を許す。すべて今回の setting に限定する。

### H1 — “axioms/background are the fixed anchors of theorem formation”

**REVISE + DOWNGRADE.** fixed support は axiomsだけでなく logic、equality、induction schema、recursive definitions、intended interpretationを含む。`anchor` は audit metaphor に留める。`everything fixed = axiom` は KILL。

### H2 — “proof is a record of constraint propagation”

**RETAIN + DOWNGRADE.** induction stepで IH、defining equation、equality substitutionがどう結論へ合流するかを表示できる。しかし ordinary induction derivation 以上の内容はない。causal / physical reading は KILL。

### H3 — “theorem is compressed reachability under fixed constraints”

**REVISE + DOWNGRADE.** bare formulaでなく theoremhood assertion \(\Gamma_{\mathrm A}\vdash\mathrm{Comm}\) なら複数 routes の存在を route-unspecified に記録する。しかし standard derivability notation の言い換えである。new theorem object とする読みは KILL。

### H4 — “route failure and theorem-reachability failure should be separated”

**RETAIN strongly.** L1/L2 erasure と Ind/Add clause erasure は、代替 derivation と countermodelにより明確に分かれた。前回より evidence が強い。

### H5 — “definitions function as entry conditions into the formal world”

**REVISE + DOWNGRADE.** Add-0/Add-S は \(+\) の internal manipulationを可能にするが、今回中心的だったのは entry より recursion orientation と induction interaction である。標準 definitional practice を越えない。

### H6 — “\(1+1=2\) illustrates re-derivability under preserved structure rather than metaphysical immobility”

**RETAIN with strict qualification; not independently enlarged.** 今回も signature rename と equivalent recursion presentationで対応する relationが再導出されたため、前回の preservation readingと整合する。しかし \(1+1=2\) の metaphysical statusについて新しい結論はない。

### H7 — “multiple proof routes make theorem-level dependency visibly different from route-level dependency”

**RETAIN + REVISE.** multiple routes は route-specific fields が theoremhood に含まれないことを明瞭にする。ただし theorem-level necessity はroute intersectionから出ず、別途 countermodel / independence argumentが必要である。

### H8 — “helper lemmas are better treated first as route-compression devices than as theorem assumptions”

**RETAIN.** L1/L2 は derived theoremsであり、library nodesとしては route compression devicesである。`merely convenient content` まで弱める読みは REVISE する。内容自体は main proof obligationsを正確に表し、Commからも回収できる。

### H9 — “induction erasure provides a stronger test of theorem-level dependency than lemma erasure”

**RETAIN within the specified theory.** lemma erasureは別 routeで回避できるが、Ind erasureには explicit countermodelがある。`stronger` は score でなく、route failureを越えて non-derivabilityまで証明できたという意味に限定する。

### 21.1 Disposition summary

| hypothesis | disposition |
|---|---|
| H1 | REVISE + DOWNGRADE; all-fixed-is-axiom reading KILL |
| H2 | RETAIN + DOWNGRADE; causal reading KILL |
| H3 | REVISE + DOWNGRADE; new-object reading KILL |
| H4 | RETAIN strongly |
| H5 | REVISE + DOWNGRADE |
| H6 | RETAIN with strict qualification |
| H7 | RETAIN + REVISE |
| H8 | RETAIN; “mere convenience” reading REVISE |
| H9 | RETAIN within specified reduced-theory test |

---

## 22. Kill criteria

| kill criterion | audit result |
|---|---|
| all distinctions reduce trivially to standard proof-theory terminology | **Technically yes.** Strong novelty claim is DOWNGRADED / KILLED |
| route changes reveal nothing beyond assumptions/proof resources | **Partly yes.** v1.1 already had the categories; separate erasure outcomes add audit discipline, not new mathematics |
| E1/E2/E3 adds no audit value | **No.** lemma deletion, induction non-derivability, operation migration would otherwise be conflated |
| formation history does not distinguish proof repair from theorem change | **No.** target/theory-preserving lemma introduction differs from axiom addition or target weakening |
| helper-lemma analysis merely restates dependency graphs | **Mathematically yes.** Any claim of new proof structure is KILLED; methodological use remains |
| no nontrivial distinction survives beyond vocabulary | **A limited distinction survives:** different evidence obligations for route failure vs non-derivability vs identity migration |

### 22.1 Negative result retained

独自語彙をすべて消しても、今回の technical content は次で完全に記述できる。

- first-order arithmetic with equality;
- recursive equations for addition;
- induction proofs of L1, L2, Comm;
- alternative induction variables;
- derived lemmas and inlining;
- mutual derivability of two recursive presentations under induction;
- countermodels after axiom deletion;
- semantic change after operation reinterpretation.

従って reinterpretation は standard proof theory / model theory を置換しない。`reachability`、`route`、`constraint propagation` の強い novelty claim は KILL される。

それでも E1/E2/E3 は、**何を消したのかに応じて必要な証拠が違う**ことを一つの audit に固定する。

- E1: alternate derivation を示せば theoremhood survival の witness になる。
- E2: non-derivabilityには countermodel / independence argument が要る。
- E3: truth valueより先に interpretation preservationを問う。

この methodological distinction が今回の最小 surviving result である。

---

## 23. Final report

1. **Formal setting.** Classical first-order equality logic、language \(\{0,S,+\}\)、successor axioms S0/S1、second-argument recursion Add-0/Add-S、full formula induction schema、standard \(\mathbb N\) intended interpretation。

2. **Explicit commutativity proof.** L1 \(\forall x(0+x=x)\) を \(x\)-induction、L2 \(\forall x\forall y(Sx+y=S(x+y))\) を \(y\)-inductionで証明し、main theoremを \(y\)-inductionする。baseは Add-0 + L1、stepは Add-S + IH + L2。

3. **Required helper lemmas.** displayed modular routeには L1 と L2 の両方が必要。不要な補題は追加していない。

4. **Clearest route-only failure.** L2を libraryから削除すると main \(y\)-induction stepは \(S(y+x)\) で止まるが、L2 proofの inline化または equivalent lemma L2′で同じ \(\Gamma_{\mathrm A}\) から完走できる。

5. **Clearest theorem-level failure.** induction schemaを削除した \(\Gamma_{\mathrm A}^{-\mathrm{Ind}}\) には、one-sided \(n_m\)-chainと bi-infinite \(z_k\)-chainを持ち、Add-0/Add-Sを満たしながら \(0+z_0=z_1\neq z_0=z_0+0\) となる model がある。soundness により Comm は非導出。

6. **Clearest induction-related dependency.** induction は L1/L2/main routeで visible なだけでなく、上の model-theoretic separationにより指定 reduced theoryに対して theorem-level load-bearing と確認された。

7. **Clearest alternate route.** main induction variableを \(y\) から \(x\) へ変更し、L2で左辺を開き Add-Sで右辺を閉じる route。元 routeでは役割が逆になる。

8. **Clearest setting migration.** \(\mathbb N\) 上で glyph \(+\) を \(a\star b=2a+b\) と再解釈すると commutativity は失敗するが、ordinary addition theorem の反証ではなく operation migration / claim-identity break。

9. **Did theoremhood remain route-agnostic?** Yes。theoremhood assertion は induction variable、lemma boundaries、rewrite order、formation historyを記録しない。

10. **Were helper lemmas route-level or theorem-level?** Named L1/L2は route-level derived resources / compression nodesで、theorem assumptionsではない。contentsは非自明で Commとも密接だが、namesと modular boundariesは inline可能。

11. **Did E1/E2/E3 survive?** Yes。E1は lemma/organization erasure、E2は Ind/Add clause erasureと countermodels、E3は operation reinterpretationでそれぞれ異なる診断と証拠を要求した。

12. **What was genuinely new relative to \(1+1=2\)?** 三 induction instances、二 helper lemmas、二 main induction organizations、そして induction-free explicit countermodelにより、route dependencyと theory dependencyの差が macro/inline差を越えて検査できた。

13. **What collapsed back into standard terminology?** Reachability = derivability、route = derivation organization、constraint propagation = induction/equality bookkeeping、stable across routes = multiple proofs of one sequent。新 mathematical object はない。

14. **H1–H9.** H1 REVISE+DOWNGRADE; H2 RETAIN+DOWNGRADE; H3 REVISE+DOWNGRADE; H4 RETAIN strongly; H5 REVISE+DOWNGRADE; H6 RETAIN with strict qualification; H7 RETAIN+REVISE; H8 RETAIN; H9 RETAIN within the specified theory。

15. **Should one more theorem be tested?** Qualified yes。今回の two routes は induction variableを交換する homologous proofs で、proof resourcesはほぼ共通だった。次は、同じ theoremに genuinely heterogeneous proof methods があり、route-specific imported theoremsが異なる例を一つ検査する価値がある。これは一般理論化の許可ではない。

16. **Should `theorem_proof_anatomy_v2` remain postponed?** Yes。E1/E2/E3 の audit value は再現したが、核心語彙は標準 derivability、derived lemma、induction、countermodel、interpretation change に吸収される。二つの arithmetic testsだけで v2 を書く根拠はまだない。

### Overall verdict

今回もっとも強く生き残ったのは、

> lemma-level route repair can preserve theoremhood,
> whereas induction-level theory erasure can destroy derivability,
> and operation reinterpretation can change the claim rather than refute it.

という三分離である。

induction は test を materially improved した。理由は proof が長くなったからではなく、induction deletionに対して target-falsifying modelを構成でき、E1とE2に異なる evidential burden があることを示せたからである。

一方、theorem-as-reachability と proof-as-route は依然として標準用語の説明的再配置に留まる。従って一つの heterogeneous-proof theorem への follow-up は warranted だが、v2 rewrite は postponed のままとする。

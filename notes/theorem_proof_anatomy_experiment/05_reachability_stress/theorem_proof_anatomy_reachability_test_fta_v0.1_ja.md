# Reachability-oriented theorem/proof anatomy: 代数学の基本定理 stress test v0.1

## 0. Status / posture

本稿の地位を最初に限定する。

- **exploratory stress test**
- **not a theorem**
- **not a new proof theory**
- **not a new semantics**
- **not a new complex-analysis foundation**
- **not a new topology**
- **not a replacement for standard proof theory**
- **no new score**
- **no rigidity metric**
- **no proof geometry**
- **no universal claim about all proofs**
- **no metaphysical conclusion**
- **no VED claim**

前回までの negative results を初期値として保持する。

- reachability \(\approx\) derivability
- proof route \(\approx\) derivation organization
- constraint propagation \(\approx\) ordinary proof bookkeeping
- imported theorem expansion \(\approx\) dependency / citation tracing

`reachability` を新しい mathematical primitive、calculus、invariant として導入しない。今回の問いは標準的な proof-dependency audit として次に限定される。

> Do genuinely different analytic / topological proof organizations remain
> meaningfully different after a preregistered amount of dependency expansion,
> and what support actually survives as theorem-level evidence?

先に結論を要約すると、選んだ二 route は Level 0–2 を通して largely heterogeneous のままである。共通する主要 support は continuity、field/norm algebra、および選んだ標準展開における compactness だが、compactness の役割は異なる。topological route は argument principle を使わないため Cauchy theory を再 import しない。analytic route は elementary compactness を使うが winding number や homotopy invariant を import しない。いずれの共通 proof resource についても theorem-level necessity は確立しない。

従って、前回の二つの分離

\[
\text{ROUTE FAILURE}
\ne
\text{THEOREM-LEVEL FAILURE}
\ne
\text{SETTING / CLAIM-IDENTITY MIGRATION}
\]

および

\[
\text{displayed-route dependency}
\ne
\text{expanded imported dependency}
\ne
\text{theorem-level necessity evidence}
\]

は今回も監査上残る。ただし数学的内容は derivation、dependency graph、counterexample、field change という標準語で尽くせる。

---

## 1. 一つの precise FTA statement を固定する

### 1.1 Primary target

\[
p(z)=a_nz^n+a_{n-1}z^{n-1}+\cdots+a_0\in\mathbb C[z],
\qquad n\ge1,\quad a_n\ne0
\]

とする。今回の primary theorem は次だけである。

> **FTA-root.** Every nonconstant polynomial \(p\in\mathbb C[z]\) has at least one zero in \(\mathbb C\):
> \[
> \exists c\in\mathbb C\quad p(c)=0.
> \]

### 1.2 Stronger familiar formとの関係

「degree \(n\) の complex polynomial は multiplicity を込めてちょうど \(n\) 個の根を持つ」は stronger presentation である。FTA-root から一つの根 \(c\) を得た後、factor theorem で

\[
p(z)=(z-c)q(z),\qquad \deg q=n-1
\]

とし、次数について帰納すれば完全分解が得られる。逆に完全分解形は当然一つの根の存在を含む。

この reduction は関係を説明するだけであり、本 stress test の target は root-existence form のままにする。証明途中で multiplicity-counting theorem や full factorization を target にすり替えない。

### 1.3 Static theoremhood

標準的な複素解析・位相の背景を \(\Gamma_{\mathrm{FTA}}\) と書けば、static assertion は

\[
\Gamma_{\mathrm{FTA}}\vdash
\forall p\in\mathbb C[z]\,
(\deg p\ge1\to\exists c\in\mathbb C\;p(c)=0)
\]

である。本稿の reachability はこの \(\vdash\) の説明的 paraphrase にすぎず、theoremhood と model-theoretic truth を同一視しない。

---

## 2. Preregistered expansion boundary

dependency expansion の深さ自体が proof-formation choice になるため、route を比較する前に停止位置を固定する。

### Expansion Level 0 — displayed proof

proof 本文で名前だけ呼ぶ theorem は black box のままにする。

- Route A の主要 black boxes: Liouville theorem、closed disk 上の continuous function の boundedness。
- Route B の主要 black boxes: winding number の homotopy invariance、leading loop の winding number、disk extension が boundary loop を null-homotopic にすること。

### Expansion Level 1 — immediate imported theorem expansion

FTA proof が直接 import した主要 nodes だけを一段展開する。

- **A1:** Liouville theorem を Cauchy estimate による標準証明へ展開する。
- **A2:** compact disk 上の boundedness を Heine–Borel と continuous-image / extreme-value argument へ展開する。
- **A3:** polynomial growth estimate を係数と triangle inequality まで展開する。
- **B1:** winding number の homotopy invariance を lift endpoint の整数値が homotopy parameterに沿って一定であることまで展開する。
- **B2:** leading-term homotopy を explicit inequality まで展開する。
- **B3:** zero-free disk extension を explicit radial homotopy まで展開する。

### Expansion Level 2 — foundational support for immediate imports

Level 1 に現れた主要 support をもう一段だけ展開する。

- Route A: Cauchy estimate \(\leftarrow\) Cauchy integral formula / theorem と contour estimate。closed-disk compactness \(\leftarrow\) \(\mathbb R^2\) の Heine–Borel と completeness。
- Route B: winding number / homotopy invariance \(\leftarrow\) \(\exp(i\theta):\mathbb R\to S^1\) の path and homotopy lifting、parameter interval/square の compactness、basic topology of \(\mathbb C^*=\mathbb C\setminus\{0\}\)。

### STOP RULE

Level 2 で停止する。以下は展開しない。

- 集合論、論理体系、実数や複素数の construction
- Riemann integral の完全構成
- Cauchy integral theorem の triangle subdivision 以下の全基礎化
- covering-space lifting theorem の局所貼り合わせ以下の全基礎化
- Heine–Borel と real completeness のさらに下の公理的同値関係

Level 2 の boundary node のさらに下でしか比較できない claim は **OPEN AT THIS BOUNDARY** とする。

この preregistration は唯一正しい展開深度を主張しない。比較を後付けで都合よく深くしたり浅くしたりする自由を減らすための test-local protocol である。

### Route B selection rule

Route B は argument principle を使わない。argument principle は標準証明を展開すると contour integration と Cauchy theory を直接呼ぶため、今回求める heterogeneity を citation boundary だけで作る危険が大きい。代わりに winding numberを、loop lifting / homotopy class に基づく topological invariant として用いる。従って Route B は **topological-heavy** だが、polynomial algebra と norm estimate も使うので “purely topological” とは呼ばない。

---

## 3. Route A — analytic / Liouville-style proof

\(p\) が zero を持たないと仮定し、矛盾を導く。

### 3.1 Polynomial growth at infinity

\[
M=\sum_{k=0}^{n-1}|a_k|
\]

と置く。\(|z|\ge1\) なら \(|z|^k\le|z|^{n-1}\)（\(k\le n-1\)）なので

\[
\left|\sum_{k=0}^{n-1}a_kz^k\right|
\le M|z|^{n-1}.
\]

従って reverse triangle inequality により

\[
|p(z)|
\ge |a_n||z|^n-M|z|^{n-1}
=|z|^{n-1}(|a_n||z|-M).
\]

\(R\ge1\) を十分大きく取り、\(M\le |a_n|R/2\) かつ \((|a_n|/2)R^n\ge1\) とする。すると \(|z|\ge R\) に対し

\[
|p(z)|\ge \frac{|a_n|}{2}|z|^n\ge1.
\]

特に \(|p(z)|\to\infty\) as \(|z|\to\infty\) である。

### 3.2 Reciprocal is entire

反証仮定により全ての \(z\in\mathbb C\) で \(p(z)\ne0\)。polynomial は entire であり、reciprocal map \(w\mapsto1/w\) は \(\mathbb C^*\) 上 holomorphic なので

\[
g(z)=\frac1{p(z)}
\]

は entire である。

### 3.3 Boundedness outside and inside

上の \(R\) に対し、\(|z|\ge R\) なら

\[
|g(z)|=\frac1{|p(z)|}\le1.
\]

一方、closed disk

\[
\overline D_R=\{z\in\mathbb C:|z|\le R\}
\]

は compact で、\(g\) はその上で continuous である。従って \(|g|\) は最大値 \(K<\infty\) を持つ。よって全平面で

\[
|g(z)|\le\max\{1,K\}.
\]

したがって \(g\) は bounded entire function である。

### 3.4 Liouville contradiction

Liouville theorem により bounded entire function \(g\) は constant。しかも \(g\) は zero でないので、その reciprocal \(p=1/g\) も constant となる。これは \(\deg p=n\ge1\) に反する。

従って反証仮定が偽で、ある \(c\in\mathbb C\) が存在して \(p(c)=0\) である。

### 3.5 Displayed dependency record

この route は直接、次を使う。

- polynomial coefficient estimate と norm/field algebra
- no-zero assumption から \(1/p\) の entire 性
- outside disk の明示的 bound
- compact disk 上の continuous boundedness
- Liouville theorem
- contradiction with nonconstancy

表示された history は

\[
\text{assume no root}
\to 1/p\text{ entire}
\to 1/p\text{ globally bounded}
\to \text{Liouville}
\to \text{contradiction}
\]

である。

---

## 4. Route B — topological / winding-number proof

同じく \(p\) が zero を持たないと仮定する。ここで winding number は、loop \(\gamma:S^1\to\mathbb C^*\) の homotopy class に対応する integer として使う。argument principle や contour-integral formula は使わない。

### 4.1 Leading-term domination on a large circle

Route A と同じ \(M=\sum_{k<n}|a_k|\) を置き、\(R\ge1\) を

\[
M R^{n-1}<|a_n|R^n
\]

すなわち \(M<|a_n|R\) となるよう取る。\(z=Re^{it}\) に対し

\[
q(z)=\sum_{k=0}^{n-1}a_kz^k
\]

と書けば \(|q(z)|\le MR^{n-1}<|a_n|R^n=|a_nz^n|\)。

### 4.2 Explicit boundary homotopy

\[
H(s,t)=a_nR^ne^{int}+s\,q(Re^{it}),
\qquad 0\le s\le1,
\quad 0\le t\le2\pi
\]

と置く。全ての \((s,t)\) について

\[
|H(s,t)|
\ge |a_n|R^n-s|q(Re^{it})|
>0.
\]

従って \(H\) は \(\mathbb C^*\) 内の homotopy で、leading loop

\[
\lambda_R(t)=a_nR^ne^{int}
\]

と polynomial loop

\[
\gamma_R(t)=p(Re^{it})
\]

を結ぶ。winding number の homotopy invariance と \(\operatorname{wind}(\lambda_R,0)=n\) により

\[
\operatorname{wind}(\gamma_R,0)=n.
\]

### 4.3 Zero-free extension gives null-homotopy

反証仮定では disk 全体で \(p(z)\ne0\)。従って

\[
K(s,t)=p(sRe^{it}),
\qquad 0\le s\le1
\]

は \(\mathbb C^*\) 内の homotopy である。\(s=1\) では \(K(1,t)=\gamma_R(t)\)、\(s=0\) では \(K(0,t)=p(0)\) という constant loop になる。従って \(\gamma_R\) は null-homotopic であり、homotopy invarianceから

\[
\operatorname{wind}(\gamma_R,0)=0.
\]

### 4.4 Contradiction

\(n\ge1\) なので

\[
n=\operatorname{wind}(\gamma_R,0)=0
\]

は矛盾する。従って \(p\) は少なくとも一つ zero を持つ。

### 4.5 Displayed dependency record

この route は直接、次を使う。

- polynomial leading-term estimate と norm/field algebra
- large circle と boundary loop
- explicit homotopies \(H\), \(K\)
- winding number の homotopy invariance
- leading loop の winding number \(n\)
- constant loop の winding number \(0\)

表示された history は

\[
\text{assume no root}
\to \text{large-circle loop}
\to \text{leading-term homotopy}
\to \operatorname{wind}=n
\to \text{disk null-homotopy}
\to \operatorname{wind}=0
\to \text{contradiction}
\]

である。

---

## 5. Displayed-route heterogeneity audit

| resource / move | Route A: Liouville | Route B: winding |
|---|---|---|
| direct complex differentiability | \(1/p\) is entire | absent; polynomial continuity suffices |
| direct Cauchy theory | hidden in Liouville, not displayed | absent |
| bounded entire functions | central | absent |
| compactness | closed disk boundedness | not displayed |
| homotopy | absent | central: \(H\) and \(K\) |
| winding number / degree | absent | central |
| contour integration | not displayed | absent |
| contradiction structure | bounded entire reciprocal would force constancy | one loop would have wind \(n\) and \(0\) |
| imported theorems | Liouville; compact continuous boundedness | winding homotopy invariance; loop degree facts |
| local / quantitative estimates | growth at infinity | leading-term domination on one circle |
| global topological invariant | absent | winding number |

**Level-0 verdict: YES, genuinely heterogeneous.** Route A converts absence of roots into a bounded entire reciprocal. Route B converts absence of roots into a null-homotopy incompatible with the large-circle degree.両者は同じ contradiction template を共有するが、中間 objects、imported libraries、closure step は異なる。

ただし Route B も polynomial algebra と norm estimate を使うため、pure topology ではない。診断は **analytic-heavy versus topological-heavy** であり、これは plain-language description に留める。

---

## 6. Level-1 imported theorem expansion

### A1. Liouville theorem

\(g\) を \(|g(z)|\le B\) for all \(z\in\mathbb C\) を満たす entire function とする。任意の \(z_0\in\mathbb C\) と任意の \(r>0\) について、Cauchy derivative estimate は

\[
|g'(z_0)|\le \frac{B}{r}
\]

を与える。\(g\) は entire なので \(r\) を任意に大きくでき、\(r\to\infty\) から \(g'(z_0)=0\)。\(z_0\) は任意だから \(g'\equiv0\)、従って connected domain \(\mathbb C\) 上で \(g\) は constant である。

Level 1 では Cauchy derivative estimate / formula を新たな imported node として記録し、その証明は Level 2 に送る。

### A2. Boundedness on a compact disk

\(\overline D_R\subseteq\mathbb C\cong\mathbb R^2\) は closed and bounded なので Heine–Borel により compact。continuous map \(|g|:\overline D_R\to\mathbb R\) の image は compact であり、従って最大値を持つ。これが Route A の inside bound \(K\) である。

Level 1 では Heine–Borel、continuous image of compact is compact、compact subset of \(\mathbb R\) has a maximum を immediate support として露出させる。

### A3. Polynomial growth estimate

これは大きな theorem node を隠していない。\(|z|\ge1\) に対し

\[
\sum_{k<n}|a_k||z|^k
\le\left(\sum_{k<n}|a_k|\right)|z|^{n-1}
\]

と reverse triangle inequality を用い、leading term が lower terms を支配する \(R\) を選ぶだけである。使うのは有限和、Archimedean な大きさの選択、複素 modulus の乗法性と triangle inequality である。

### B1. Homotopy invariance of winding number

loop \(\gamma:[0,1]\to\mathbb C^*\) を normalization

\[
u(t)=\frac{\gamma(t)}{|\gamma(t)|}\in S^1
\]

へ移す。\(u\) の lift \(\theta:[0,1]\to\mathbb R\) を

\[
e^{i\theta(t)}=u(t)
\]

となるよう選ぶ。loop condition により \(\theta(1)-\theta(0)\in2\pi\mathbb Z\) で、

\[
\operatorname{wind}(\gamma,0)
=\frac{\theta(1)-\theta(0)}{2\pi}\in\mathbb Z
\]

と定める。

loops の homotopyを lift すると、各 parameter \(s\) に対する endpoint difference は連続に変化する一方で \(2\pi\mathbb Z\) に値を取る。connected parameter interval 上の continuous integer-valued function は constant なので winding number は変わらない。

ここでは lift の存在・一意性と homotopy lifting を Level 2 の imported support として残す。

### B2. Leading-term homotopy

Section 4.1 の strict inequality

\[
|q(Re^{it})|<|a_n|R^n
\]

により、全 \(s\in[0,1]\) で

\[
|a_nR^ne^{int}+s q(Re^{it})|>0.
\]

従って straight-line homotopy は \(\mathbb C^*\) を出ない。leading loop の normalized lift は

\[
\theta(t)=\arg(a_n)+nt
\]

と取れ、\(t:0\to2\pi\) で角度差は \(2\pi n\)。従って winding number は \(n\) である。

### B3. Zero-free extension implies zero winding

no-zero assumption の下で \(F:\overline D_1\to\mathbb C^*\), \(F(w)=p(Rw)\) は boundary loop \(\gamma_R\) の extension である。explicit radial contraction \(w=s e^{it}\) を \(F\) と合成した

\[
K(s,t)=p(sRe^{it})
\]

は \(\gamma_R\) を constant loop \(p(0)\) に結ぶ。constant loop の lift endpoint difference は \(0\) なので winding number は \(0\)。これは argument principle を使わない。

### Level-1 verdict

heterogeneity は強く残る。Route A から Cauchy estimate と compact maximum が現れ、Route B から lift、homotopy invariance、integer degree が現れた。共通するのは polynomial estimate、continuity、basic norm/topologyであり、core imported libraries はまだ異なる。

---

## 7. Level-2 support expansion

### 7.1 Route A support

#### Cauchy estimate support

Cauchy integral formula を \(|\zeta-z_0|=r\) 上で使うと

\[
g'(z_0)=\frac{1}{2\pi i}
\int_{|\zeta-z_0|=r}
\frac{g(\zeta)}{(\zeta-z_0)^2}\,d\zeta.
\]

contour の長さが \(2\pi r\)、integrand の絶対値が高々 \(B/r^2\) なので ML estimate により \(|g'(z_0)|\le B/r\)。Cauchy integral formula は Cauchy integral theorem、contour integration、disk 内の holomorphicityから得られる。

この Level 2 では Cauchy integral theorem と contour integral の基礎構成を boundary nodes とし、それ以下へは進まない。従って Route A は Level 2 で明確に Cauchy-analytic supportを持つ。

#### Compactness support

\(\mathbb C\cong\mathbb R^2\) の closed disk が compact であることは finite-dimensional Heine–Borel による。その標準証明の背後には real completenessがある。continuous image of compact is compact は open-cover definition から示せ、compact subset of \(\mathbb R\) の最大値存在にも order completeness が現れる。

ここでは real/complex numbers の constructionや completeness equivalences へは下げない。

### 7.2 Route B support

#### Winding number support

normalization \(\mathbb C^*\to S^1\) と covering map

\[
\pi:\mathbb R\to S^1,\qquad \pi(\theta)=e^{i\theta}
\]

を用いる。path lifting theorem は、initial liftを固定すれば path の lift が存在して一意であることを与える。homotopy lifting theorem は loops の homotopy 全体を連続に lift する。これにより endpoint difference / winding number の homotopy invariance が正当化される。

これらの標準的な局所貼り合わせ proof では、\([0,1]\) または \([0,1]^2\) の compactnessを使って evenly covered neighborhoods に従属する有限 subdivisionを選ぶ。ここで elementary compactness が Route B に現れる。

#### Disk extension support

disk は radial contraction \((s,e^{it})\mapsto se^{it}\) により contractible である。\(F:\overline D\to\mathbb C^*\) と合成すれば boundary loop が constantへ縮む。この step は basic topology と continuity を使うが Cauchy integral theoremは使わない。

#### STOP

covering-space lifting の証明を局所座標や実数構成まで展開しない。\(\pi_1(S^1)\cong\mathbb Z\) の別証明との比較も行わない。これらは **OPEN BELOW LEVEL 2** である。

### Level-2 verdict

両 route は elementary compactness と continuity に部分的に収束する。しかし Route A の core は Cauchy integral formula / estimate、Route B の core は covering lift / homotopy invariant であり、nearly identical にはならない。topological route に Cauchy theory は再登場せず、analytic route に winding number、fundamental group、degree は再登場しない。

---

## 8. Detect partial convergence

| level | Route A core | Route B core | common visible support | diagnosis |
|---|---|---|---|---|
| L0 | bounded entire reciprocal + Liouville | large-circle winding + null-homotopy | field/norm algebra, contradiction | very heterogeneous |
| L1 | Cauchy estimate, compact maximum | lift endpoint, homotopy invariance | continuity, polynomial domination | largely heterogeneous |
| L2 | Cauchy formula/theorem, Heine–Borel | covering lift, contractibility, compact parameter spaces | elementary compactness, continuity, \(\mathbb C\) topology | partial convergence only |

FTA では IVT より convergence が弱い。IVT の topological route では interval connectedness の選んだ展開が直接 LUB completeness に戻った。今回の Route B は argument principleを避けたため、Cauchy theoryへ戻らない。

ただしこれは「全 topological FTA proofs が analytic supportを避ける」という universal claim ではない。argument principle、Rouché theorem、complex integrationで degree を計算する別 route を選べば、analytic loading は増える。comparison は route selection と library boundary に依存する。

---

## 9. Avoid fake heterogeneity

### 9.1 Rejected mixed route

もし Route B を

\[
\frac{1}{2\pi i}\int_{|z|=R}\frac{p'(z)}{p(z)}\,dz
\]

で zeros を数える argument principle proof としたなら、displayed level では winding languageが前景化しても、Level 1–2 で contour integration、Cauchy theorem、local factorizationが現れる。その場合の正確な診断は **mixed analytic/topological** であり、purely topological ではない。

### 9.2 Selected route diagnosis

本稿の Route B は topological definition of winding、homotopy invariance、disk contractionを使い、argument principleを使わない。一方、large-circle dominationには algebraic/norm estimateを要する。従って診断は **topological-heavy with algebraic estimates** である。

Route A は **analytic-heavy with elementary compactness** である。compactnessという topologyの標準概念を使うが、homotopy invariantや fundamental groupを使わない。

この plain-language diagnosisを taxonomy や ranking に昇格させない。

---

## 10. Route erasure E1

### 10.1 Remove Liouville as a library node

- displayed Route A は bounded entire \(1/p\) から constancyへ進めず停止する。
- A1 の Cauchy-estimate proof を inline すれば同じ route contentを回復できる。
- Route B は Liouvilleを使わず残る。

従って named Liouville nodeの削除は **ROUTE FAILURE** であり、FTA-root の failureではない。Liouville theoremは imported derived resourceであって FTA assumptionではない。

### 10.2 Remove winding homotopy invariance as a library node

- displayed Route B は leading loop と polynomial loop の integerを同一視できず停止する。
- B1 の lift argumentを inline すれば contentを回復できる。
- Route A は winding numberを使わず残る。

これも **ROUTE FAILURE**。winding theoremの contentを theoryから排除したことでも、FTA-root が non-derivable と示したことでもない。

### 10.3 Control verdict

同じ \(\mathbb C\)、同じ polynomial class、同じ target を保持した alternate proof が明示されているので、E1 は両方向で成立する。named node deletionと theorem-support deletionを分ける最も明瞭な controlである。

---

## 11. Theory/support erasure E2 — completeness / compactness

### E2a — Compactness

closed disk compactnessを利用できなければ、Route A の「continuous \(1/p\) is bounded inside」の書かれた step は壊れる。local boundednessを各点で得ても、有限個へまとめるには compactnessまたは同等の uniformizationが必要になる。

しかし、ここから FTA-root の theorem-level failure は従わない。

- Route B は closed-disk boundednessを使わない。
- Route A にも minimum-modulus principleなど別の organizationがあり得るが、その proof resourcesを別途監査する必要がある。
- 「compactnessを使えない setting」が何を意味するかを固定しなければ countermodelにならない。

従って compactness deletionについての判定は、**Route A failure established; theorem-level necessity OPEN** である。

### E2b — Completeness

incomplete subfield controlとして

\[
F=\mathbb Q(i)=\{a+bi:a,b\in\mathbb Q\}
\]

を usual norm の subspace field として考える。\(F\) は completeではなく、polynomial

\[
x^2-2\in F[x]
\]

は \(F\) に rootを持たない。実際 \((a+bi)^2=2\) なら \(2ab=0\)。\(b=0\) なら \(a^2=2\) で不可能、\(a=0\) なら \(-b^2=2\) で不可能である。

従って FTA-like schema はこの incomplete fieldで失敗する。しかし同時に

- carrierを \(\mathbb C\) から \(\mathbb Q(i)\) へ変えた、
- fieldは incomplete になった、
- fieldは algebraically closedでなくなった、
- analytic/topological ambientも変わった、

ので、これは completeness alone の necessityを隔離しない。**confounded setting control** である。

さらに \(\mathbb R\) は completeだが \(x^2+1\) の real rootを持たない。従って completeness alone は FTA-like root propertyに sufficientでもない。以上から

\[
\text{incomplete and rootless}
\not\Rightarrow
\text{completeness alone is necessary}
\]

である。complex completenessの theorem-level exact necessityは本稿では **OPEN**。

---

## 12. Algebraic-closure / field-change control

| field / setting | test polynomial or status | analogous root schema | diagnosis relative to complex FTA |
|---|---|---|---|
| \(\mathbb C\) | primary setting | true by FTA | target itself |
| \(\mathbb R\) | \(x^2+1\) | false | field / setting migration |
| \(\mathbb Q\) | \(x^2-2\) | false | field / setting migration |
| \(\mathbb Q(i)\) | \(x^2-2\) | false | incomplete and non-algebraically-closed; confounded migration |
| an algebraically closed field \(K\) | definition supplies roots for nonconstants | true by definition of algebraic closure | different theorem setting; no analytic proof implied |

「every nonconstant polynomial has a root」は fieldの algebraic closednessを述べる schemaである。しかし “\(\mathbb C\) is algebraically closed” を FTA proof の assumptionにすれば conclusionを仮定する循環になる。standard \(\mathbb C\) を ambientとして選ぶことと、その fieldが algebraically closedであると証明することを分ける。

また nonconstant hypothesisを外すと \(p(z)=1\) が immediate counterexampleになる。これは field migrationを伴わない、明示的 theorem-hypothesis weakeningの controlである。

さらに object class を polynomial から arbitrary entire functionへ広げると、\(e^z\) は nonconstant entireだが zeroを持たない。従って finite polynomial formも statement-sideで load-bearingである。ただし「polynomial よりどこまで広い classなら結論が残るか」という exact boundaryは本稿では調べない。

### 12.1 E1 / E2 / E3 control

- **E1 Route erasure:** Liouvilleまたは winding-invarianceの named nodeを消す。alternate route / inline proofが残る。
- **E2 Theorem-support weakening:** nonconstantを落とすと \(p=1\)、polynomial restrictionを entireへ広げると \(e^z\) が counterexampleになる。
- **E3 Setting / claim-identity migration:** \(\mathbb C\to\mathbb R,\mathbb Q,\mathbb Q(i)\) は analogous field schemaへの移動であり complex FTAの falsificationではない。

completeness/compactnessの削除は、isolated weaker theoryを十分に固定できていないため E2 necessity controlとしては OPENに留める。この evidence burdenの差により三分離は今回も維持される。

---

## 13. Continuity / compactness / Cauchy dependence audit

表中の語は **directly used / imported / appears after expansion / absent / not tested** に限定する。

| resource | Route A L0 | Route A L1–2 | Route B L0 | Route B L1–2 |
|---|---|---|---|---|
| field algebra | directly used | directly used | directly used | directly used |
| completeness of \(\mathbb C\) / \(\mathbb R\) | not displayed | appears after expansion via integration/Heine–Borel; exact role below STOP partly open | absent | not established as used; parameter compactness appears |
| compactness | directly used for closed disk | expanded via Heine–Borel | absent | appears after expansion in standard lifting proof |
| continuity | directly used for compact bound | directly used | directly used in homotopies | directly used |
| holomorphicity | directly used: \(1/p\) entire | central | absent | absent |
| Cauchy theorem / formula | imported inside Liouville | appears after expansion | absent | absent |
| Liouville | directly imported | expanded | absent | absent |
| homotopy | absent | absent | directly used | central |
| winding number | absent | absent | directly used | expanded by lifts |
| \(\pi_1(\mathbb C^*)\) / covering lift | absent | absent | imported implicitly | appears after expansion |
| argument principle | absent | absent | absent by route selection | absent |
| degree | absent | absent | winding as integer degree, directly used | expanded through lift endpoint |

“completeness of \(\mathbb C\)” を Route A の一個の nodeとして雑に数えない。closed disk compactness、contour integralの存在、Cauchy theoryの証明で役割が分かれ、Level 2 boundary以下の exact dependencyは本稿では追わない。

---

## 14. Imported theorem relocation

IVT で得た working hypothesis は FTA でも成立する。

> imported theorem may hide support inside citation boundaries.

- displayed Route A の “Liouville” の内部には、chosen expansionでは Cauchy derivative estimate、Cauchy formula、contour integrationがある。
- “continuous on compact disk is bounded” の内部には Heine–Borel、continuous-image compactness、maximum existenceがある。
- displayed Route B の “winding is homotopy invariant” の内部には path/homotopy lifting、integer-valued endpoint difference、parameter compactnessがある。
- rejected argument-principle routeを選べば、その citation内に Cauchy/contour machineryが入る。

従って citation boundaryは dependencyを消すのではなく、visible recordから imported node内へ relocateし得る。

ただし

\[
\text{appears in a chosen expansion}
\not\Rightarrow
\text{logically necessary for FTA-root}
\]

である。特に Cauchy theoryは Route A の chosen proofには重要だが Route B には現れない。winding theoryについては逆である。compactnessは両 expansionに現れるが、二 route intersectionだけでは necessityを示さない。

---

## 15. Same theorem, different proof cultures

Route A と B は異なる standard theorem librariesを使って同じ theoremhood assertionを certifyする。

- Route A: entire function、Cauchy estimate、Liouville、compact maximumという complex-analysis library。
- Route B: loops、homotopy、winding / degree、covering lift、disk contractionという algebraic-topology / topological-complex-analysis library。

この library differenceは static formula

\[
\Gamma_{\mathrm{FTA}}\vdash\mathrm{FTA\text{-}root}
\]

から復元できない。これは sociologyや proof communityの評価ではなく、「異なる derived theorem resourcesが同じ conclusionを証明できる」という限定的事実である。

`theorem_proof_anatomy_v1.1` はすでに Liouville routeと最大値原理、Rouché、argument principle、topological degreeなどの alternativesを proof resourcesとして区別した。今回新たに行ったのは、選んだ二 routeを preregistered depthまで展開し、visible dependencyと expanded dependencyを theorem necessityから分離したことである。

proof-formation testsとの接続では、同じ endpoint/theoremhoodが route historyを復元しないこと、library boundaryという record frameが依存の可視性を変えること、二 historyを区別する fieldが theorem necessityを説明するとは限らないことが再確認された。

---

## 16. Displayed vs expanded vs theorem-level

| support | displayed dependency | expanded dependency through L2 | independent theorem-level evidence | verdict |
|---|---|---|---|---|
| Liouville | A direct; B absent | A: Cauchy estimate/formula | B survives Liouville-node erasure | route-specific derived resource |
| winding / homotopy | B direct; A absent | B: covering lift and contractibility | A survives winding-node erasure | route-specific derived resource |
| Cauchy theory | A hidden in Liouville; B absent | A explicit; B absent | no weakening/countermodel test isolates it | necessity NOT ESTABLISHED |
| compactness | A direct; B hidden | A closed disk; B parameter subdivision | no isolated weaker-setting counterexample | common expanded support; necessity OPEN |
| continuity | both, in different forms | both | no isolation test; changing topology changes setting | common route support, exact necessity OPEN |
| field/norm algebra | both direct | both | field-change controls alter claim identity | fixed ambient support, minimality not established |
| nonconstant hypothesis | theorem statement direct | unchanged | \(p=1\) after deletion | load-bearing theorem hypothesis established |
| finite polynomial object class | theorem statement direct | unchanged | broaden to entire functions: \(e^z\) | load-bearing restriction; exact maximal class not established |
| complex coefficient/root field | theorem ambient | unchanged | \(\mathbb R,\mathbb Q(i)\) analogues fail | field-specific support; controls are setting migrations |

この表の第三列までが proof dependency record、第四列が別の evidence typeである。named-node erasure、expanded-route intersection、counterexampleを同じ強さの証拠として扱わない。

---

## 17. Formation-history stress

以下は数学史ではなく test-local construction historyである。

### Route A history

\[
\text{assume no root}
\to \text{invert }p
\to \text{separate outside/inside bounds}
\to \text{bounded entire}
\to \text{Liouville contradiction}
\]

### Route B history

\[
\text{assume no root}
\to \text{restrict to a large circle}
\to \text{compare with leading term}
\to \text{winding }n
\to \text{zero-free disk contraction}
\to \text{winding }0
\to \text{contradiction}
\]

同じ FTA-root theoremhoodからどちらの historyを通ったかは逆算できない。Route Aを放棄して Bへ切り替えても、\(\mathbb C\)、polynomial class、nonconstant hypothesis、targetを保てば route reorganizationであり theorem changeではない。

一方、root fieldを \(\mathbb C\) から extensionへ変える、holomorphic function全体へ object classを広げる、rootではなく approximate minimumを targetにする場合は theorem/setting identityが変わる。proof repairと自動的には呼べない。

---

## 18. Expansion-boundary sensitivity

| boundary | heterogeneity diagnosis | newly visible relation |
|---|---|---|
| Level 0 | very heterogeneous | Liouville versus winding/null-homotopy |
| Level 1 | largely heterogeneous | Cauchy estimate versus lift/homotopy invariance; polynomial domination is shared |
| Level 2 | partial convergence but cores distinct | compactness/continuity shared; Cauchy theory versus covering topology remains |

従って proof-route heterogeneityは **partly** an artifact of where expansion stopsだが、今回の差は boundaryだけの artifactではない。Level 2でも core imported theorem familiesが異なる。

preregistrationは次を改善した。

- Route Bだけを Cauchy theoryに達するまで深く掘り、Aを浅く保つといった post hoc asymmetryを抑えた。
- “reappeared” がどの levelの claimかを固定した。
- Level 2以下の disputeを OPENとして止められた。

一方で route selection、各 imported theoremにどの標準証明を選ぶか、major supportの粒度は依然 judgment-dependentである。従って reproducibilityは改善するが完全にはならない。

---

## 19. Can common support be role-different?

答えは **YES in the chosen expansions** である。

| common name | Route A role | Route B role | same role? |
|---|---|---|---|
| compactness | closed disk上の \(|1/p|\) の pointwise continuityを一つの global boundへまとめる | local covering liftsを parameter interval/square上の finite subdivisionへまとめる | no |
| continuity | reciprocalを compact disk上で boundedにし、holomorphic theoryへ接続 | homotopies \(H,K\) と normalized loopsを有効に保つ | no |
| polynomial growth / domination | outside diskで reciprocalを小さくする | boundary loopを leading loopへ zero-free homotopyする | no |
| field/norm algebra | reciprocal、entire性、absolute bound | leading term、triangle inequality、\(\mathbb C^*\) avoidance | partially shared, operationally different |
| contradiction | bounded nonconstant entire functionを排除 | incompatible winding valuesを排除 | abstract form only |

従って

\[
\text{same resource name}\ne\text{same proof role}.
\]

ただしこの役割分類も displayed/expanded recordに相対する。新 taxonomyではなく、dependency intersectionを粗く読むことへの注意である。

---

## 20. Theorem-level necessity controls

| candidate support | in both routes? | after expansion? | weaker-setting / deletion evidence | exact necessity established? | confounding |
|---|---|---|---|---|---|
| compactness | not L0; yes in chosen L2 | closed disk vs parameter compactness | no isolated countermodel; alternate route survives A-node deletion | **NO / OPEN** | “remove compactness” setting underspecified |
| completeness | not directly both | A foundation; B only possible below basic compactness, not isolated | \(\mathbb Q(i)\) rootless but also non-algebraically-closed | **NO** | strong field/closure confounding |
| Cauchy theory | A only | A explicit | B proves target without it | **NO** | route-specific sufficiency only |
| winding / homotopy | B only | B explicit | A proves target without it | **NO** | route-specific sufficiency only |
| topology on \(\mathbb C\) | both broadly | both | changing topology changes continuity/homotopy and claim setting | **NO exact minimality result** | setting identity |
| algebraic closedness | equivalent to root schema for the field | not a proof resource unless assumed | nonclosed fields give failures | **equivalent property, not independent explanatory support** | assuming it for \(\mathbb C\) is circular |
| nonconstant hypothesis | yes, theorem statement | unchanged | \(p=1\) | **YES, statement-side** | none |
| polynomial object class | yes, theorem statement | both exploit finite leading term | \(e^z\) is nonconstant entire and zero-free | **YES as a load-bearing restriction** | exact maximal class not tested |
| coefficient/root field \(\mathbb C\) | ambient both | unchanged | \(\mathbb R\): \(x^2+1\); \(\mathbb Q(i)\): \(x^2-2\) | field choice load-bearing for this formulation | comparisons are E3 migrations |

### Completeness caution

\(\mathbb C\) is complete と \(\mathbb C\) is algebraically closed を同一視しない。\(\mathbb R\) は completeだが algebraically closedでない。\(\mathbb Q(i)\) は incompleteかつ nonclosedなので、そこから completenessの単独必要性は読めない。

### Topology caution

Route B が homotopy/windingを使うことは、この specific topological machineryが FTA theoremhoodに logically necessaryだという証拠ではない。Route Aが反例になる。

### Cauchy caution

Cauchy theoryは Liouville expansionで load-bearingだが、FTA-rootの全 proofsに必要とはいえない。used-by-proof と necessary-for-theoremを分ける。

今回 independent counterexamplesで load-bearing と確認できた statement-side supportは nonconstant hypothesisと finite polynomial restrictionである。後者の exact maximal object classまでは確立しない。field controlsは formulationの ambientが load-bearingであることを示すが、元の complex FTAの falsificationではない。compactness、completeness、Cauchy、windingの exact theorem-level necessityは確立しない。

---

## 21. Re-evaluate prior hypotheses

H5/H6 は今回の指定リストでは中心外だが、final numberingを途切れさせないため prior dispositionを明示して not independently retested とする。

| hypothesis | disposition | reason |
|---|---|---|
| **H1:** fixed support includes multiple formal roles | **RETAIN** | field、nonconstant hypothesis、holomorphic rules、compactness、derived theoremsを一括して axiomにできない。 |
| **H2:** proof as constraint-propagation record | **DOWNGRADE** | two contradiction historiesを記述するが ordinary proof bookkeepingを越えない。 |
| **H3:** theorem as compressed reachability | **DOWNGRADE** | route-unspecified \(\Gamma\vdash T\) の言い換えに留まる。 |
| **H4:** route failure and theorem-level failure should be separated | **RETAIN** | Liouville/winding node deletionと \(p=1\)/field controlsは異なる evidenceを要求する。 |
| **H5:** definitions as entry conditions | **DOWNGRADE; not independently retested** | polynomial、entire、windingの操作可能性を与えるが standard definition practice以上ではない。 |
| **H6:** preserved-structure re-derivability versus metaphysical immobility | **RETAIN prior qualification; not retested** | FTAから新 metaphysical evidenceは得ていない。 |
| **H7:** multiple routes expose route/theorem dependency difference | **RETAIN** | Cauchy-only and winding-only dependenciesが明瞭に分かれた。 |
| **H8:** helper/imported theorems are derived route resources, not theorem assumptions | **RETAIN** | Liouvilleと winding invarianceは inline可能で theorem assumptionsではない。 |
| **H9:** theory-side erasure requires stronger evidence than named-node deletion | **RETAIN** | alternate routeと counterexample/countermodelを区別した。 |
| **H10:** heterogeneous displayed proofs can hide common deeper support | **REVISE** | compactnessは再出現したが core supportは収束しなかった。 |
| **H11:** expansion locates displaced dependency | **RETAIN** | Liouville内の Cauchy theory、winding内の liftingを定位した。 |
| **H12:** reappearance does not prove theorem necessity | **RETAIN** | common compactnessにも独立 necessity evidenceはない。 |
| **H13:** heterogeneity partly depends on record granularity | **RETAIN** | L0–L2で診断は変わるが差は消えない。 |
| **H14:** preregistered boundary improves reproducibility | **RETAIN with qualification** | post hoc depth変更を抑えるが node selectionの judgmentは残る。 |
| **H15:** common support can reappear with different proof roles | **RETAIN** | compactness、continuity、dominationで具体的に確認した。 |
| **H16:** common expanded support needs independent weakening evidence for necessity | **RETAIN** | compactness intersectionから necessityを推論しなかった。 |
| **H17:** same theoremhood can be certified by substantially different theorem libraries | **RETAIN** | Cauchy/Liouville libraryと covering/winding libraryが同じ targetを証明した。 |

最も強く残るのは H4、H8、H12、H15、H16、H17。H2/H3の強い novelty readingは引き続き支持されない。

---

## 22. Strong falsification questions

1. **Q1 — Level 0 heterogeneity?** **YES.** bounded entire reciprocal対 winding obstruction。
2. **Q2 — Level 1 survival?** **LARGELY.** Cauchy estimate対 lift/homotopy invarianceで coreは別。
3. **Q3 — Level 2 survival?** **LARGELY, with partial convergence.** compactness/continuityを共有するが Cauchy theoryと covering topologyは分かれる。
4. **Q4 — Does B import Cauchy machinery?** **NO for the selected route through Level 2.** argument-principle routeなら yesだが今回は採用しない。
5. **Q5 — Does A import significant topological machinery?** **NO algebraic-topological invariant.** elementary compactness/topologyは importする。
6. **Q6 — Common resource with different roles?** **YES.** compactnessが bound globalization対 lift globalizationを担う。
7. **Q7 — More than citation chasing?** **NO mathematically.** preregistered record disciplineという methodological valueだけ。
8. **Q8 — Does preregistration improve reproducibility?** **YES, partially.** stop depthは固定するが theorem-node selectionは残る。
9. **Q9 — Does route/theorem/setting separation prevent conflations?** **YES.** \(\mathbb Q(i)\) を complex FTAの反証や completeness necessityと誤読するのを防ぐ。
10. **Q10 — Any theorem-level necessity established?** **Only statement-side restrictions, narrowly:** nonconstant and polynomial-form controls have counterexamples after weakening. Major proof resourcesの exact necessityは未確立。
11. **Q11 — Reachability collapse?** **YES, into derivability.**
12. **Q12 — Constraint propagation collapse?** **YES, into proof bookkeeping.**
13. **Q13 — Does heterogeneity survive normalized boundaries?** **YES through the preregistered L2**, though route selection remains presentation-dependent。
14. **Q14 — Strongest result methodological?** **YES.** 新数学ではなく dependency/evidence auditである。

---

## 23. Kill criteria

### Triggered

- reachabilityを derivability以上とする reading: **KILL**。
- constraint propagationを standard proof record以上とする reading: **KILL / DOWNGRADE to gloss**。
- expansionを ordinary dependency graph inspection以上の数学的方法とする claim: **KILL**。
- common expanded supportから logical necessityを推論する rule: **KILL**。
- incomplete nonclosed fieldから completeness-alone necessityを読む推論: **KILL**。
- displayed route Bを “purely topological” と呼ぶ diagnosis: **KILL**。algebra/norm estimatesを使う。

### Not triggered

- Route heterogeneityは Level 1でほぼ消えなかった。Level 2でも partial convergenceに留まった。
- preregistered stop ruleは恣意性を消さないが、どの claimが boundary-relativeかを再現可能にした。
- E1/E2/E3は named-node failure、statement weakening、field migrationの実際の混同を防いだ。
- displayed/expanded/necessityの分離は、compactness reappearanceを necessityへ昇格させない働きをした。

negative resultは明確である。bespoke vocabularyを消しても全数学的結果は standard complex analysis、algebraic topology、dependency expansion、counterexamplesで保存できる。残る価値は audit protocolだけである。

---

## 24. Final report

1. **Exact FTA statement:** every nonconstant \(p\in\mathbb C[z]\) has at least one complex zero。
2. **Route A:** no root \(\Rightarrow1/p\) entire; growth plus compact disk gives boundedness; Liouville forces constancy; contradiction。
3. **Route B:** large-circle polynomial loop is homotopic to degree-\(n\) leading loop, but zero-free disk extension makes it null-homotopic; winding \(n=0\) contradiction。
4. **Displayed-level heterogeneity:** **YES, strong**。
5. **Level-1 heterogeneity:** **largely survives**; Cauchy estimate versus covering-lift logic。
6. **Level-2 heterogeneity:** **largely survives with partial convergence** through compactness/continuity。
7. **Clearest route-only failure:** delete Liouville or winding-invariance library node; the displayed route fails, inline content or the other route survives。
8. **Clearest setting migration:** \(\mathbb C\to\mathbb R\) makes \(x^2+1\) rootless but does not refute complex FTA。
9. **Clearest theorem-support weakening:** broaden polynomial to arbitrary entire function; \(e^z\) is nonconstant and zero-free。Deleting “nonconstant” also gives \(p=1\)。\(\mathbb Q(i)\) is only a confounded field control。
10. **Strongest common expanded support:** elementary compactness, continuity, field/norm algebra。
11. **Different roles?:** **YES**; compactness globalizes an inside-disk bound in A and local lifts over parameter space in B。
12. **Did B re-import analytic machinery?:** **NO Cauchy machinery through L2** for the selected winding/lift route; it remains topological-heavy, not pure topology。
13. **Did A re-import topological machinery?:** elementary compactness **YES**, homotopy/winding/fundamental-group machinery **NO**。
14. **Any major theorem-level necessity established?:** **NO** for completeness, compactness, Cauchy, or winding. Only nonconstant and finite-polynomial statement restrictions are independently shown load-bearing under the tested weakenings。
15. **Did preregistered expansion help?:** **YES, partially**; it fixed the comparison stop and exposed OPEN-below-L2 claims, while node-selection judgment remained。
16. **Did E1/E2/E3 survive?:** **YES**。
17. **Genuinely new relative to IVT:** the routes did not converge on one major foundational theorem; common support reappeared with demonstrably different proof roles; preregistered expansion made that comparison sharper。
18. **What collapsed again:** reachability \(=\) derivability paraphrase; route \(=\) proof organization; constraint propagation \(=\) bookkeeping; expansion \(=\) citation tracing。
19. **H1–H17:** H1 RETAIN; H2 DOWNGRADE; H3 DOWNGRADE; H4 RETAIN; H5 DOWNGRADE/not retested; H6 RETAIN prior qualification/not retested; H7 RETAIN; H8 RETAIN; H9 RETAIN; H10 REVISE; H11 RETAIN; H12 RETAIN; H13 RETAIN; H14 RETAIN qualified; H15 RETAIN; H16 RETAIN; H17 RETAIN。
20. **One more theorem warranted?:** **NO by default.** The preregistered heterogeneous-proof question has now received a positive methodological control and strong negative novelty result. A further theorem requires a new falsification question, not repetition。
21. **Should `theorem_proof_anatomy_v2` remain postponed?:** **YES.** The audit distinctions survived, but all core notions remain expressible in standard terminology and major necessity claims remain open。

### Final disposition

最も強い surviving resultは

\[
\text{common resource name}
\ne
\text{same proof role}
\ne
\text{theorem-level necessity}
\]

を preregistered Level 0–2 で具体化できたことである。analytic/topological heterogeneityは expansion後も残ったが、これは新 invariantではない。FTAは第四段階の stress targetとして十分に機能した一方、結果は新 anatomyの確定ではなく standard dependency auditの精密化に留まる。従って追加テストは自動的には warrantedでなく、v2 rewriteは postponedのままとする。

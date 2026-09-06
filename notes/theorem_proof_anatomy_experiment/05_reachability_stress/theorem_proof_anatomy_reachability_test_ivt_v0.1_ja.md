# Reachability-oriented theorem/proof anatomy: 中間値の定理 stress test v0.1

## 0. Status / posture

本稿は次の地位に限定される。

- **exploratory stress test**
- **not a theorem**
- **not a new proof theory**
- **not a new semantics**
- **not a new topology**
- **not a new real-analysis foundation**
- **not a replacement for standard proof theory**
- **no new score**
- **no rigidity metric**
- **no proof geometry**
- **no universal claim about all proofs**
- **no metaphysical conclusion**
- **no VED claim**

`reachability` は今回も ordinary derivability の説明的 paraphrase に限る。新しい primitive、calculus、invariant を導入しない。出発点となる negative result も固定する。

- reachability \(\approx\) derivability
- proof route \(\approx\) derivation organization
- constraint propagation \(\approx\) ordinary proof bookkeeping

したがって、この語彙から正の新理論を無理に取り出さない。今回の中心問いは、標準的な proof-dependency audit として次がどこまで有効かである。

> When the same theorem is proved through substantially different imported
> mathematical structures, can route-specific dependency be separated from
> theorem-level dependency without merely hiding common support inside imported theorems?

先に結論を短く述べる。表示された二つの証明は genuinely heterogeneous だが、位相ルートを展開すると、区間の連結性の標準証明に least-upper-bound completeness が再登場する。しかし、これは一つの展開で依存が再登場したという事実であって、completeness の theorem-level necessity を単独で証明しない。後者への独立な control は、不完備順序体 \(\mathbb Q\) 上の \(q\mapsto q^2-2\) が与える。この区別により

\[
\text{ROUTE FAILURE}
\ne
\text{THEOREM-LEVEL FAILURE}
\ne
\text{SETTING / CLAIM-IDENTITY MIGRATION}
\]

は今回も監査上有用である。ただし、その数学的中身は標準的な derivability、dependency expansion、countermodel の語で尽くせる。

---

## 1. 一つの precise IVT statement を固定する

### 1.1 General IVT

標準実数 \(\mathbb R\) と \(a<b\) を固定する。一般形を次とする。

> **IVT.** \(f:[a,b]\to\mathbb R\) が連続で、\(y\) が \(f(a)\) と \(f(b)\) の間にある、すなわち
> \[
> \min\{f(a),f(b)\}\le y\le\max\{f(a),f(b)\}
> \]
> ならば、ある \(c\in[a,b]\) が存在して \(f(c)=y\) である。

### 1.2 Primary working form

二つの route の比較では、strict zero-crossing form を主対象にする。

> **ZIVT.** \(f:[a,b]\to\mathbb R\) が連続で
> \[
> f(a)<0<f(b)
> \]
> ならば、ある \(c\in(a,b)\) が存在して \(f(c)=0\) である。

一般形から ZIVT は \(y=0\) の場合として従う。逆に一般形で endpoint equality があれば \(c=a\) または \(c=b\) を取る。strict に間にある場合は \(g(x)=f(x)-y\) を置き、符号の向きが逆なら \(-g\) を用いて ZIVT を適用する。したがって両形式は標準的な簡単な reduction で結ばれるが、同じ文字列の target ではない。本稿の直接証明対象は ZIVT、一般 IVT への移行は明記した reduction による。

### 1.3 Static assertion

以下で固定する標準実解析の背景を \(\Gamma_{\mathrm{IVT}}\) と書けば、static な主張は

\[
\Gamma_{\mathrm{IVT}}\vdash
\bigl(f\text{ continuous on }[a,b]\land f(a)<0<f(b)\bigr)
\to \exists c\in(a,b)\, f(c)=0
\]

である。本稿でいう reachability は、この derivability assertion の説明的言い換え以上ではない。model-theoretic truth と proof-theoretic derivability も同一視しない。

---

## 2. Formal / background ingredients

「実数」「連続性」「完備性」を一括して background と呼ばず、役割を分ける。

| ingredient | formal role | status in this test | route-level appearance |
|---|---|---|---|
| classical first-order / set-theoretic reasoning | logical background | fixed | both routes |
| equality and substitution | inference machinery | fixed | both routes |
| ordered-field laws of \(\mathbb R\) | mathematical assumptions / structure | fixed | both routes |
| trichotomy, order density, interval order-convexity | order consequences | fixed or derived from ordered-field structure | explicit in A; partly explicit in B |
| least-upper-bound property | completeness principle | fixed property of standard \(\mathbb R\) | direct in A; hidden then recovered in one expansion of B1 |
| \([a,b]=\{x\in\mathbb R:a\le x\le b\}\) | definition plus domain restriction | fixed | both routes |
| continuity on \([a,b]\) | theorem hypothesis; definable by neighborhoods or \(\varepsilon\)-\(\delta\) | fixed per instance | local use in A; continuous-image use in B |
| order topology on \(\mathbb R\) | topological structure induced by order | fixed | mostly B; continuity can also be stated through it |
| connectedness | topological definition | not an extra axiom about all sets | B |
| \([a,b]\) is connected | derived theorem in the chosen expansion | imported in displayed B | B1 |
| continuous image of a connected space is connected | general topological theorem | imported, then expanded | B2 |
| connected subsets of \(\mathbb R\) are intervals | order-topological theorem | imported, then expanded | B3 |
| separation / relative open sets | definitional and proof machinery | fixed through topology | expanded B |

Definitions make phrases such as “continuous”, “interval”, and “connected” internally usable; they are not therefore axioms. Likewise, the three imported theorems in Route B are derived proof resources, not theorem assumptions merely because the displayed proof cites them.

The full ambient foundation may contain much more—set construction, function coding, compactness theorems—but the displayed arguments below do not directly use all of it. “Included in ambient background” and “load-bearing in this route” will remain separate.

---

## 3. Route A — direct completeness / supremum proof

ZIVT を supremum で証明する。以下での連続性は \([a,b]\) への相対連続性である。

### 3.1 Sign-set and supremum

\[
N=\{x\in[a,b]:f(x)<0\}
\]

と置く。

1. \(f(a)<0\) なので \(a\in N\)。従って \(N\ne\varnothing\)。
2. \(N\subseteq[a,b]\) なので \(b\) は \(N\) の上界である。
3. \(\mathbb R\) の least-upper-bound property により
   \[
   c=\sup N
   \]
   が存在する。
4. \(a\in N\) かつ \(b\) が上界なので \(a\le c\le b\)。従って \(c\in[a,b]\)。

ここで実際に直接使った completeness principle は「空でなく上に有界な実数部分集合は supremum を持つ」である。

### 3.2 Endpoint exclusion

後の左右への移動を正当化するため、まず \(a<c<b\) を示す。

#### \(c<b\)

\(f(b)>0\) と \(b\) での相対連続性により、ある \(\delta_b>0\) が存在して

\[
x\in[a,b],\quad |x-b|<\delta_b
\quad\Longrightarrow\quad f(x)>0
\]

となる。例えば連続性の値側の許容幅を \(f(b)/2\) と取ればよい。

\[
u=b-\min\{\delta_b/2,(b-a)/2\}
\]

と置くと \(a<u<b\) である。\(x\in N\) なら \(f(x)<0\) なので、上の正値近傍には入れず \(x\le u\) である。従って \(u\) も \(N\) の上界であり、\(c=\sup N\le u<b\)。

#### \(a<c\)

同様に \(f(a)<0\) と \(a\) での相対連続性から、ある \(\delta_a>0\) が存在して

\[
x\in[a,b],\quad |x-a|<\delta_a
\quad\Longrightarrow\quad f(x)<0
\]

となる。

\[
v=a+\min\{\delta_a/2,(b-a)/2\}
\]

なら \(a<v<b\) かつ \(v\in N\)。よって \(c=\sup N\ge v>a\)。

### 3.3 Why \(f(c)<0\) fails

反対に \(f(c)<0\) と仮定する。連続性により、ある \(\delta>0\) が存在して

\[
x\in[a,b],\quad |x-c|<\delta
\quad\Longrightarrow\quad f(x)<0
\]

となる。ここでは値側の許容幅を \(-f(c)/2>0\) と取れる。

\[
h=\min\{\delta/2,(b-c)/2\}>0
\]

とすれば \(c+h\in[a,b]\)、\(|(c+h)-c|<\delta\) なので \(f(c+h)<0\)。従って \(c+h\in N\) だが \(c+h>c\) であり、\(c\) が \(N\) の上界であることに反する。ゆえに \(f(c)<0\) ではない。

### 3.4 Why \(f(c)>0\) fails

反対に \(f(c)>0\) と仮定する。連続性により、ある \(\delta>0\) が存在して

\[
x\in[a,b],\quad |x-c|<\delta
\quad\Longrightarrow\quad f(x)>0
\]

となる。値側の許容幅を \(f(c)/2\) と取ればよい。

\[
h=\min\{\delta/2,(c-a)/2\}>0,\qquad t=c-h<c
\]

と置く。\(c=\sup N\) なので、\(t<c\) は \(N\) の上界ではない。従ってある \(s\in N\) が存在して

\[
t<s\le c
\]

である。すると \(|s-c|<h\le\delta/2<\delta\) なので \(f(s)>0\)。しかし \(s\in N\) から \(f(s)<0\) であり矛盾する。ゆえに \(f(c)>0\) ではない。

### 3.5 Conclusion and route record

実数の trichotomy により、\(f(c)<0\) でも \(f(c)>0\) でもないことから \(f(c)=0\)。また \(a<c<b\) なので \(c\in(a,b)\) である。これで ZIVT が証明された。

この route の並びは

\[
\text{target}
\to \text{negative sign-set}
\to \sup N
\to \text{two local continuity contradictions}
\to f(c)=0
\]

である。supremum は結論ではなく、この route が選んだ witness candidate の組織化装置である。

---

## 4. Route B — connectedness proof

同じ ZIVT を、表示上は supremum を用いずに証明する。

### 4.1 Displayed proof

次の三つの標準定理を imported theorem として使う。

- **B1:** 実数の区間 \([a,b]\) は connected である。
- **B2:** connected space の continuous image は connected である。
- **B3:** \(\mathbb R\) の connected subset は interval、すなわち order-convex である。

これらを用いると、証明は次の通りである。

1. B1 により \([a,b]\) は connected。
2. \(f\) は連続なので、B2 により \(f([a,b])\) は connected。
3. B3 により \(f([a,b])\subseteq\mathbb R\) は interval。
4. \(f(a)<0<f(b)\) かつ \(f(a),f(b)\in f([a,b])\) である。
5. interval は両端の間の全点を含むため、\(0\in f([a,b])\)。
6. 従ってある \(c\in[a,b]\) が存在して \(f(c)=0\)。endpoint の値は strict に非零なので \(c\ne a,b\)、従って \(c\in(a,b)\)。

これは imported results を black box として許す displayed proof として完全である。ただし、dependency audit としては B1–B3 の名前の背後を次節で一段展開する。

### 4.2 Route record

表示された route の並びは

\[
\text{target}
\to [a,b]\text{ connected}
\to f([a,b])\text{ connected}
\to f([a,b])\text{ interval}
\to 0\in f([a,b])
\]

である。Route A の function-dependent sign-set、supremum、局所的な二つの contradiction は本文に現れない。

---

## 5. First heterogeneous-route audit

まず displayed proof の粒度で比較する。

| resource / move | Route A: supremum | Route B: connectedness |
|---|---|---|
| direct use of order | sign、upper bound、supremum、左右移動、trichotomy | endpoint values の間に \(0\) があること |
| direct use of completeness | yes: \(c=\sup N\) | no, at displayed level |
| direct use of supremum | yes | no, at displayed level |
| direct use of topology | relative continuity を neighborhood として使うが、connectedness は使わない | yes |
| direct use of connectedness | no | yes, domain and image |
| continuous-image theorem | no | imported B2 |
| connected-subset/interval characterization | no | imported B3 |
| local contradiction | \(f(c)<0\), \(f(c)>0\) を個別に排除 | no local sign contradiction |
| imported lemmas / theorems | LUB property、continuity consequences | B1, B2, B3 |
| unused ambient examples | compactness、uniform continuity、sequential compactness | supremum construction、extreme value theorem |

**Displayed-level verdict:** yes。二つの proof organization は実質的に異なる。Route A は function-specific subset から witness candidate を構成する。Route B は domain の global topological property を image へ運び、image の order-convexity から witness の存在を読む。

ただし、この yes は表示粒度に相対的である。B1–B3 がどの support から証明されるかを隠したまま、「一方は completeness、他方は topology だから独立」と結論してはならない。

---

## 6. Imported theorem expansion test

### B1. Why is \([a,b]\) connected?

標準的な proof を一つ展開する。\([a,b]\) が disconnected だと仮定し、相対位相での separation

\[
[a,b]=U\cup V
\]

があるとする。すなわち \(U,V\) は互いに素、非空、\([a,b]\) で相対的に open である。\(u\in U\), \(v\in V\) を取り、必要なら \(U,V\) の名前を交換して \(u<v\) とする。

\[
A=U\cap[u,v]
\]

と置く。\(u\in A\) なので非空、また \(v\) で上に有界である。least-upper-bound property により

\[
c=\sup A\in[u,v]
\]

が存在する。\(c\in U\cup V\) なので場合分けする。

- **\(c\in U\) の場合。** \(c\ne v\) である。なぜなら \(v\in V\) で \(U\cap V=\varnothing\) だからである。\(U\) の相対 openness により、\(c\) の十分近くで \([a,b]\) に属する点は \(U\) に入る。そこで \(c<d<v\) を十分近く取れば \(d\in U\cap[u,v]=A\) となり、\(d>c\) は \(c\) が上界であることに反する。
- **\(c\in V\) の場合。** \(c\ne u\) である。\(u\in U\) だからである。\(V\) の相対 openness により、ある \(r<c\) があって \((r,c]\cap[a,b]\subseteq V\) とできる。一方 \(r<c=\sup A\) なので \(r\) は \(A\) の上界ではなく、ある \(d\in A\) が \(r<d\le c\) を満たす。すると \(d\in U\cap V\) となり矛盾する。

従って separation は存在せず、\([a,b]\) は connected である。

この expansion は least-upper-bound completeness を明示的に使う。supremum の対象は Route A の sign-set \(N\) ではなく、仮想的 separation の片側 \(U\cap[u,v]\) である。

### B2. Why is a continuous image of a connected set connected?

\(X\) を connected、\(f:X\to Y\) を連続とする。\(f(X)\) が separation \(P\cup Q\) を持つと仮定する。すると

\[
f^{-1}(P),\qquad f^{-1}(Q)
\]

は連続性により \(X\) で open、互いに素、非空で、その和は \(X\) 全体である。これは \(X\) の connectedness に反する。従って \(f(X)\) は connected。

この証明は一般位相の定義と preimage preservation of openness を使い、実数の least-upper-bound property を直接は使わない。

### B3. Why are connected subsets of \(\mathbb R\) intervals?

\(C\subseteq\mathbb R\) を connected とし、\(p,q\in C\), \(p<q\) とする。\(p<r<q\) なのに \(r\notin C\) となる \(r\) があると仮定する。このとき

\[
C_-=C\cap(-\infty,r),\qquad
C_+=C\cap(r,\infty)
\]

は \(C\) の相対位相で open、互いに素、非空で、\(C=C_-\cup C_+\) である。これは separation なので connectedness に反する。従って \(r\in C\)、すなわち \(C\) は interval である。

この証明は実数の order topology と linear order を使うが、least-upper-bound property を直接は使わない。

### Expansion verdict

completeness は B1 のこの標準的展開で再登場する。B2 と B3 には直接再登場しない。従って正確な記録は次である。

1. Route A は completeness を本文で直接使う。
2. displayed Route B は completeness を明記しない。
3. displayed Route B が import する B1 の一つの標準証明は completeness を使う。
4. 以上だけから「completeness は IVT の theorem-level logically necessary resource である」とはまだ言えない。

---

## 7. Dependency hiding / relocation

今回の working hypothesis は限定付きで成立する。

> importing a theorem may remove a dependency from the visible proof record
> without removing it from the chosen expanded dependency structure.

Route B の本文には `sup` が一度も出ない。しかし B1 を上の仕方で展開すれば、LUB completeness が現れる。これは「依存の削除」ではなく、表示された citation node の内部への **relocation** と読むことができる。

ただし、次の三つは別である。

| claim | evidence here | status |
|---|---|---|
| completeness is hidden from displayed Route B | B1 が black box だから | ESTABLISHED for this presentation |
| completeness occurs in an expanded proof of B1 | 上の supremum proof | ESTABLISHED for this expansion |
| completeness is logically necessary for IVT | chosen expansion とは独立の non-derivability evidence が必要 | NOT established by reappearance alone |

特に

\[
\text{reappears in one expansion}
\not\Rightarrow
\text{theorem-level necessity}
\]

である。別の foundational presentation、別の completeness principle、connectedness を primitive support とする theory では dependency record が異なり得る。逆に、依存が表示されないことも、その内容が不要であることを意味しない。

この区別は新しい proof theory ではなく、ordinary citation chasing / proof dependency expansion を明示的に theorem-erasure audit へ接続したものである。

---

## 8. Route erasure E1

E1 は特定の construction や named theorem node を proof record から消し、同じ theory と target を保持したまま代替 route が残るかを問う。

### 8.1 Route A から supremum construction を消す

- sign-set \(N\) を作っても \(c=\sup N\) を導入できなければ、上に書いた Route A は witness candidate を失い停止する。
- これは明確な **ROUTE FAILURE** である。
- 同じ標準 \(\mathbb R\)、同じ continuity hypothesis、同じ ZIVT target の下で、displayed Route B は残る。
- 従って、この erasure 単独から theorem-level failure は従わない。

ここで「supremum construction を route から消す」と「theory から completeness を削る」は別操作である。前者が E1、後者は E2 である。

### 8.2 Route B から connectedness theorem を消す

たとえば library resource としての B1「\([a,b]\) is connected」を消す。

- displayed Route B は第一段階で停止するので **ROUTE FAILURE**。
- B1 の内容を `inline` して上の supremum proof を書けば、同じ topological organization を回復できる。
- あるいは Route A に切り替えれば ZIVT を回復できる。
- named theorem の削除は、その theorem の数学的内容を theory から消したことではない。

B2 を named node として消しても、その preimage proof を inline できる。B3 も separation proof を inline できる。従って imported theorem の名前は route compression resource であって、axiom ではない。

### 8.3 E1 control verdict

両方向で alternate derivation が実在するため、E1 は「一つの proof が壊れた」ことを「IVT が導出不能になった」ことから切り離せる。これは今回の最も明瞭な route-only control である。

---

## 9. Theory/support erasure E2 — completeness

### 9.1 「\(\mathbb R\) から completeness を消す」の二義性

standard \(\mathbb R\) は complete ordered field である。従って次を混同しない。

1. **Syntactic theory weakening:** ordered-field axioms は残すが LUB axiom を公理集合から削除する。一方、intended structure としての standard \(\mathbb R\) は念頭に置き続ける。
2. **Semantic model control:** 弱めた ordered-field theory の model として、\(\mathbb Q\) など不完備な ordered field を許す。
3. **Specific theorem over \(\mathbb R\):** carrier と interpretation を standard \(\mathbb R\) に固定した IVT。
4. **Schema over ordered fields:** 任意の ordered field で同様の IVT が成り立つ、というより一般の主張。

公理を syntactically 削っても、standard \(\mathbb R\) という intended structure 内で IVT の真理値が変わるわけではない。しかし弱い theory だけから schema が derivable かは別問題であり、その反証には弱い theory の countermodel が使える。

### 9.2 Explicit incomplete ordered-field control

\(\mathbb Q\) に通常の順序と order topology を入れ、

\[
D=[1,2]_{\mathbb Q}=\{q\in\mathbb Q:1\le q\le2\}
\]

とする。関数

\[
f:D\to\mathbb Q,\qquad f(q)=q^2-2
\]

は polynomial なので、この order topology で連続である。また

\[
f(1)=-1<0<2=f(2).
\]

しかし \(f(q)=0\) となる rational \(q\) は存在しない。実際、既約分数 \(q=p/r\) が \(q^2=2\) を満たすとすると \(p^2=2r^2\)。従って \(p\) は偶数であり、\(p=2k\) と置くと \(r^2=2k^2\) なので \(r\) も偶数となり、既約性に反する。

同じ例は topological route の欠損も可視化する。連続な \(f\) に対して

\[
U=f^{-1}((-\infty,0)),\qquad V=f^{-1}((0,\infty))
\]

は \(D\) の互いに素な非空 open subsets で、rational root がないため \(D=U\cup V\) である。従って \([1,2]_{\mathbb Q}\) は connected ではない。Route B の B1 に対応する事実も、この weaker setting では成立しない。

従って、ordered-field axioms と通常の連続性だけから全 ordered field 上の ZIVT schema は導けない。この control は一つの proof route の失敗ではなく、弱い theory に analogous target を偽にする model があることを示す。

### 9.3 Classification

- ordered-field schema の水準では、これは completeness support を欠く theory における **THEOREM-LEVEL FAILURE / countermodel** である。
- standard \(\mathbb R\) 上の specific IVT に対しては、\(\mathbb R\to\mathbb Q\) は **SETTING MIGRATION** であり、実数上の IVT の反証ではない。
- この counterexample は「ordered-field axioms alone は不足する」という独立な証拠を与える。
- しかし「Dedekind LUB completeness という特定の formulation が、あらゆる形式化で唯一必要である」とまでは示さない。IVT property、Cauchy completeness、connectedness などの等価性や含意は theory と基礎づけに相対する。

したがって、Route A/B の交差だけで completeness necessity を推測するより、\(\mathbb Q\) control の方が theorem-support audit として強い。ただしこれは score や普遍的な “strength ranking” の導入ではなく、証拠の種類が違うという意味である。

---

## 10. Completeness vs real-number identity

前節の区別を claim identity の観点から固定する。

| operation | carrier / interpretation | proposition being tested | diagnosis |
|---|---|---|---|
| LUB axiom だけを formal theory から削除 | intended model は standard \(\mathbb R\) のまま | specific IVT over \(\mathbb R\) | truth は維持され得るが、弱い公理からの derivability は別途要監査 |
| weakened theory の全 model を許す | arbitrary ordered fields | IVT schema over ordered fields | \(\mathbb Q\) が countermodel |
| carrier を \(\mathbb Q\) に変更 | \(\mathbb Q\), usual order/topology | analogous rational IVT | false for \(q^2-2\); setting migration from real IVT |
| standard \(\mathbb R\) を保持 | complete ordered field | original IVT | neither route erasure nor \(\mathbb Q\) counterexample refutes it |

「completeness を消しても同じ \(\mathbb R\)」は、axiomatization の削減と structure の変更のどちらを意味するか指定しなければ不十分である。前者なら theorem-level derivability question、後者なら setting / identity audit が必要になる。

---

## 11. Connectedness erasure

### 11.1 Derived resource として消す

standard real analysis の presentation で「\([a,b]\) is connected」を derived library theorem として扱い、その node を消すとする。

- displayed Route B は壊れる。
- B1 の content を inline すれば回復する。
- Route A は connectedness を経由せずに残る。

従って、この操作は E1 の **ROUTE FAILURE** であり、connectedness の theorem-level necessity を示さない。

### 11.2 Hypothesis として置く

別の一般定理

> \(X\) が connected、\(f:X\to\mathbb R\) が continuous なら \(f(X)\) は interval

を target にするなら、connectedness は theorem hypothesis である。その hypothesis を外せば、後述の disconnected-domain counterexample により結論は失敗する。

つまり connectedness の役割は presentation によって異なる。

- specific IVT over real interval では、\([a,b]\) の connectedness は固定された order/completeness から導出される compressed route resource になり得る。
- general connected-domain theorem では、connectedness は明示的な theorem assumption である。

この役割差を一つのラベルに固定しない。imported theorem と axiom、derived fact と theorem hypothesis を分けることが重要である。

---

## 12. Continuity erasure

continuity は単なる helper resource ではなく、IVT statement の明示的 hypothesis である。その削除を control する。

\([-1,1]\) 上で

\[
f(x)=
\begin{cases}
-1,&x<0,\\
1,&x\ge0
\end{cases}
\]

と定める。すると \(f(-1)=-1<0<1=f(1)\) だが、どの \(x\) に対しても \(f(x)\ne0\) である。\(f\) は \(0\) で不連続である。

この例から分かるのは次である。

- Route A では、\(c\) の近傍に符号を保持させる二つの step が失敗する。
- Route B では、continuous-image theorem を適用できない。
- より強く、continuity を落とした theorem schema 自体に counterexample がある。

従ってこれは **ROUTE FAILURE only** ではなく、hypothesis weakening に対する **THEOREM-LEVEL FAILURE** である。元の continuous-IVT が偽になったわけではなく、target statementを弱い hypothesis へ変更した successor claim が偽である。

---

## 13. Interval / connected-domain erasure

domain を

\[
D=\{-1,1\}\subseteq\mathbb R
\]

とし、subspace topology を入れる。identity map

\[
f:D\to\mathbb R,\qquad f(x)=x
\]

は連続で、\(f(-1)<0<f(1)\) だが、\(D\) に \(f(c)=0\) となる点はない。

これは次を分離する。

- 「domain が interval」は mere notation / presentation choice ではない。
- Route B では actual structural support は domain connectedness として直接見える。
- Route A では sign-set の supremumは \(-1\) だが、domain 内でその右側に近い点を取る step がない。interval の order-convexity / local no-gap property が局所 contradiction の背後で働いていた。
- domain hypothesis を arbitrary subset に弱めた schema は counterexample を持つ。

従って、specific theorem の \([a,b]\) を単に消すのは E2 型の hypothesis weakening であり、carrier/domain を実際に \(D\) へ変える comparison は E3 型の setting migration でもある。どちらの問いをしているかを明示する必要がある。

---

## 14. Helper theorem necessity

Route B の B2 と B3 を、named theorem node と mathematical content に分ける。

### 14.1 Named node deletion

- “continuous image of connected is connected” という library 名を使えなくしても、preimage separation proof を inline できる。
- “connected subsets of \(\mathbb R\) are intervals” という library 名を使えなくしても、cut point \(r\) による separation proof を inline できる。

従って named nodes は displayed route を短くする **route-compression devices** であり、それ自体が theorem assumptions ではない。

### 14.2 Content deletion

一方、B2 の content に相当する推論を何らかの形で利用できなければ、connectedness を domain から image へ運ぶこの organization は停止する。B3 の content に相当する order-convexity を利用できなければ、image が connected であることから \(0\) の所属へ進めない。

従って

\[
\text{named theorem necessity}
\ne
\text{content dependency of this route}.
\]

さらに、content がこの route で load-bearing であることから、IVT のあらゆる proof にその theorem が named or implicit に必要だとはいえない。Route A が control になる。

これは前回の加法可換律における L1/L2 の inline test と同型だが、今回は imported theorem の内部が大きく、内部に別の foundational support が移され得ることが新しい。

---

## 15. Two levels of proof route

今回の audit に限り、次の二つの記録粒度を区別する。この二層を canonical hierarchy や新 formal taxonomy にはしない。

### Displayed route

論文・教科書に書かれた proof body と、その場で名前だけ呼ばれる theorem nodes の記録。

- A: sign-set → supremum → local contradictions
- B: connected interval → connected image → interval image

### Expanded route

imported theorem を、比較に必要な範囲まで選んだ証明で展開した dependency record。

- A: LUB は background principle のまま保持
- B: B1 を展開すると separation-set の supremumが出現し、B2/B3 を展開すると preimage と order cut が出現

### Does heterogeneity survive?

**Partially, yes.** 両 route は completeness に部分的に合流するが、ほぼ同じ proof にはならない。

- Route A の supremum は \(f\) の符号から作られ、直接 root candidate を与える。
- expanded Route B の supremum は仮想的 separation の境界を作り、まず domain connectedness を証明する。
- B2 は一般位相的な preimage argument、B3 は order cut argument であり、Route A の二つの local sign contradiction と同じ derivation sequence ではない。

一方、heterogeneous という見え方は record granularity に依存する。B1 を primitive library fact として止めれば差は大きく見え、基礎まで展開すれば共通 support が増える。どこまで展開するかに presentation-neutral な唯一の終点は、この test からは得られない。

---

## 16. Formation-history stress

これは数学史の主張ではなく、今回の test-local construction log である。

### Route A history

1. zero-crossing target を固定した。
2. negative side を集める \(N\) を選んだ。
3. LUB property により \(c=\sup N\) を candidate にした。
4. endpoint を除外した。
5. continuity で \(f(c)<0\) と \(f(c)>0\) を別々に排除した。

### Route B history

1. 同じ zero-crossing target を固定した。
2. individual root candidate の構成ではなく image set \(f([a,b])\) を選んだ。
3. domain connectedness を image へ移した。
4. connected subset of \(\mathbb R\) を interval と読んだ。
5. endpoint values の間に \(0\) を挿入した。

Route A の construction を使えなくして Route B に切り替えても、\(\Gamma_{\mathrm{IVT}}\) と target が同じなら **route reorganization** であって theorem change ではない。

一方、continuity assumption を追加し直す、domain を connected subset に制限し直す、conclusion を approximate zero に弱める、という変更は target/hypothesis を変える。これは同じ theorem の proof repair と自動的にはみなせず、successor claim の identity audit が要る。

この差は proof-formation stress tests の結果と整合する。endpoint と static theoremhood だけから、sign-set を先に選んだか image connectedness を先に選んだかは復元できない。record frame が中間 construction や imported citations を保存しなければ、history の差は不可視になる。

---

## 17. Static vs historical vs imported-dependency record

三つの record を混同しない。

| record | content | what it does not determine |
|---|---|---|
| Static | \(\Gamma_{\mathrm{IVT}}\vdash\mathrm{ZIVT}\) | どの proof を通ったか |
| Historical | 今回 Route A または B をこの順で構成した | imported theorem の任意の証明史すべて |
| Imported-dependency | この B1 の展開が LUB、B2 が preimage、B3 が order cut を使った | それらが全 derivations で logically necessary か |

Imported-dependency information は theoremhood assertion には含まれない。同じ \(\Gamma\vdash T\) から、どの library theorem を呼び、どこまで inline し、どの B1 proof を採用したかは逆算できない。

ただし、expanded dependency record も中立な「真の全履歴」ではない。どの imported theorem をどの証明で展開するか、どの foundation で止めるかは新たな proof-formation choice である。この点で、record-frame dependence は今回も残る。

### 17.1 Prior anatomy / proof-formation connection

`theorem_proof_anatomy_v1.1` はすでに IVT の assumptions、ambient/background、proof resources、supremum route と connectedness escape route を区別できた。今回それを置換せず、次の監査を追加した。

- old anatomy の **proof resource / escape route** を、displayed node の削除と alternate derivation の実在で具体的に検査した。
- proof-formation の **semantic collapse of different moves** は、A/B が同じ static conclusionへ到達しても history が違うこととして再現した。
- **record-frame dependence** は、B1–B3を black box のまま残す frame と inline する frame の差として強く現れた。
- history を区別する separator があっても、それだけでは theorem-level necessity を説明しない。この点は prior **minimal separator failure** と整合する。
- route label の命名より、どの resource が displayed / expanded / countermodel level で働くかを優先した。これは prior **action-classification instability** への対応である。

従って新しい点は object/ambient/assumption の再発見ではなく、imported theorem 内へ移った dependency と theorem-level necessity evidence を明示的に分けたことに限られる。

---

## 18. E1 / E2 / E3 再検査

これらは今回も test-local diagnostic labels であり、新 formal taxonomy ではない。

### E1 — Route erasure

**操作:** specific lemma、named theorem、supremum construction、displayed organization を消す。

**必要証拠:** 同じ theory と target を保持した alternate derivation の実在。

**今回の control:** Route A の supremum construction を消して Route B を残す。Route B の B1 node を消して inline expansion または Route A を残す。

**判定:** **ROUTE FAILURE**。theoremhood の failure ではない。

### E2 — Theorem-support erasure

**操作:** theorem hypothesis または theory-side support を弱める。

**必要証拠:** 単なる proof failure ではなく、counterexample、countermodel、または適切な independence / non-derivability argument。

**今回の controls:** continuity を外した step function、connected interval hypothesis を外した two-point domain、ordered-field axiomsだけへ弱めたときの \(\mathbb Q\) model。

**判定:** weakened statement/schema の **THEOREM-LEVEL FAILURE** を支持する。ただし、どの statement/schema を弱めたかを固定する。

### E3 — Setting / identity migration

**操作:** carrier \(\mathbb R\to\mathbb Q\)、domain \([a,b]\to\{-1,1\}\)、または topology / interpretation を変更する。

**必要証拠:** 何を保存し、何を変更し、元の claim と対応する analogous claim が何かを明示する。

**今回の control:** rational IVT の失敗は standard real IVT の falsification ではない。carrier、codomain、completeness、intervalの意味が変わっている。

**判定:** **SETTING MIGRATION**。変更が大きい場合は **CLAIM-IDENTITY MIGRATION / BREAK** も併記する。

### Three-way verdict

今回の heterogeneous routes でも

\[
\mathrm{E1}\ne\mathrm{E2}\ne\mathrm{E3}
\]

は維持される。特に同じ \(\mathbb Q\) example でも、ordered-field schema の countermodel と見ると E2、specific real theorem から carrier を変えた comparison と見ると E3 である。ラベルは object language の性質ではなく、どの counterfactual question を問うかに依存する。

---

## 19. Strong question: does completeness reappear?

三段階で答える。

### A. Direct appearance

Route A は \(N\) が非空かつ上に有界であることから \(c=\sup N\) を得る際に completeness を直接使う。

### B. Appearance in one expansion

displayed Route B に supremum はない。しかし B1「\([a,b]\) is connected」を本稿で選んだ標準証明に展開すると、\(U\cap[u,v]\) の supremum を得るため completeness が再登場する。

### C. Theorem-level necessity

A と B の二-route intersection だけから C は従わない。二つの route が proof space 全体を代表する保証はなく、B1 の別 presentation もあり得るからである。

\(\mathbb Q\) control は別種の証拠を追加する。それは、少なくとも ordered-field structure alone では一般 IVT schema を保証しないことを示す。従って completeness またはそれに相当する no-gap support が数学的に無関係だという読みを退ける。しかし LUB axiom の唯一性や、あらゆる基礎づけにおける literal necessity までは確立しない。

最終判定は次である。

> completeness reappears in the chosen expansion of Route B;
> the reappearance locates a displaced dependency, while the \(\mathbb Q\)
> countermodel—not the reappearance itself—supplies independent evidence
> that ordered-field axioms alone are insufficient.

---

## 20. Theorem-level necessity audit

| resource | displayed Route A | displayed Route B | expanded Route B | weakening control | warranted conclusion |
|---|---|---|---|---|---|
| continuity | local sign preservation | continuous-image theorem | B2 uses preimages of open sets | discontinuous step function | load-bearing hypothesis for stated schema |
| LUB completeness | direct: \(\sup N\) | not visible | direct in chosen B1 proof | \(\mathbb Q\), \(q^2-2\) | ordered-field axioms alone insufficient; LUB uniqueness not proved |
| interval / connected domain | order-convex domain enables nearby domain points | B1 direct as imported fact | B1 derives connectedness | \(D=\{-1,1\}\) | arbitrary-domain weakening fails |
| ordered-field / linear-order structure | signs, bounds, trichotomy | “between” and interval image | B1/B3 order arguments | not erased separately here | common fixed support in chosen setting, not separately proved minimal |
| connectedness | not named | direct | derived for \([a,b]\), transported by B2 | disconnected domain | route-level in A, explicit structural content in B |
| continuous-image theorem B2 | unused | named | preimage argument | Route A survives its deletion | Route-B dependency, not theorem assumption |
| connected-subset characterization B3 | unused | named | order-cut separation | Route A survives its deletion | Route-B dependency, not theorem assumption |

この表は三つの証拠型を分ける。

1. **displayed-route use:** 書かれた proof body が直接引用する。
2. **expanded-route use:** imported theorem の選んだ証明に現れる。
3. **weakening control:** support を落とした statement/schema に counterexample がある。

route-shared resource であることは theorem-level necessity の証明ではない。逆に、一つの route にしか表示されない resource も、展開すれば別 route の内部に現れ得る。この監査は「included in background」と「actually load-bearing in this displayed or expanded proof」も分ける。

---

## 21. Re-evaluate old working hypotheses

判定はこの test に限定される。

| hypothesis | disposition | reason |
|---|---|---|
| **H1:** fixed support includes axioms/background/definitions/rules, not just axioms | **RETAIN** | IVT では ordered-field assumptions、continuity definition、logic、LUB、topology、derived theoremsの役割が明確に異なる。 |
| **H2:** proof as constraint-propagation record | **DOWNGRADE** | continuity hypothesisや connectedness が結論へ使われる順序を説明できるが、ordinary proof bookkeeping を越える内容は確認できない。 |
| **H3:** theorem as compressed reachability | **DOWNGRADE** | theorem statement が二 route を区別しないことは示すが、\(\Gamma\vdash T\) の説明的言い換えに留まる。 |
| **H4:** route failure and theorem-level failure should be separated | **RETAIN** | E1 の alternate route と E2 の counterexamples が別の証拠責任を持つ。 |
| **H5:** definitions as entry conditions | **DOWNGRADE** | continuity・interval・connectednessを操作可能にするという限定的説明は有効だが、標準的 definitional practice の再記述である。 |
| **H6:** \(1+1=2\) illustrates re-derivability under preserved structure rather than metaphysical immobility | **RETAIN (not independently retested)** | 本 test の対象外。前回の限定付き判定を変更する新証拠はない。 |
| **H7:** multiple routes make route-level dependency visibly different from theorem-level dependency | **REVISE** | displayed level では強く成立するが、expanded level では common support が増える。record granularity を明示する必要がある。 |
| **H8:** helper lemmas/theorems should first be treated as derived route resources, not theorem assumptions | **RETAIN** | B1–B3 の named nodes は削除・inline可能で、axiomやIVT hypothesisではない。 |
| **H9:** theory-side erasure is stronger evidence than named-lemma erasure | **RETAIN** | “stronger” は score ではなく証拠型の差。\(\mathbb Q\) countermodel は named-node deletion より theorem-support claim に直接応答する。 |
| **H10:** heterogeneous displayed proofs can hide common deeper support | **REVISE** | chosen B1 expansion では成立。ただし hidden support が全 expansion で同じとは証明されない。 |
| **H11:** imported theorem expansion is useful for locating displaced dependencies | **RETAIN** | displayed B から見えない LUB use を B1 内に定位できた。ただし手法自体は ordinary citation chasing である。 |
| **H12:** dependency reappearance under expansion does not itself prove theorem-level necessity | **RETAIN** | 二-route intersection と logical necessity を分離する中心的 safeguard になった。 |
| **H13:** proof-route heterogeneity is partly a function of record granularity | **RETAIN** | black-box B と expanded B で共通 support の見え方が変わった。 |

H2、H3、H5 は語彙上の直観として完全に無意味ではないが、新しい mathematical capability としては支持されない。H4、H8、H12 が最も強く残る。

---

## 22. Strong falsification questions

### Q1. Are Route A and Route B genuinely heterogeneous?

**YES at the displayed level.** witness candidate を sign-set の supremum から作る組織と、connected image を interval と読む組織は異なる。

### Q2. Do they remain heterogeneous after imported theorems are expanded?

**PARTIALLY YES.** completeness で部分的に収束するが、supremum の対象と役割、B2 の preimage argument、B3 の order cut は異なる。完全な独立性も完全な同一化も得られない。

### Q3. Does completeness reappear in the topological route?

**YES, in the chosen standard expansion of B1.** B2/B3 には直接現れない。

### Q4. If it does, is that merely a property of this expansion?

**At least that much only.** どの expansion にも不可避だという結論は、本稿の二 proof だけから出ない。

### Q5. Can completeness dependence be supported independently by an incomplete ordered-field counterexample?

**YES, with qualification.** \(\mathbb Q\) 上の \(q^2-2\) は ordered-field axioms alone の不足を示すが、LUB formulation の唯一性までは示さない。

### Q6. Does E1/E2/E3 remain useful?

**YES as an audit discipline.** route deletion、hypothesis/theory weakening、carrier/claim migrationに別の証拠を要求し、実際の conflation を防ぐ。

### Q7. Does imported theorem expansion reveal something absent from theoremhood?

**YES.** B1 の内部で completeness が使われるという selected dependency/history は \(\Gamma\vdash\mathrm{IVT}\) だけには含まれない。

### Q8. Is this just an ordinary dependency graph with extra vocabulary?

**LARGELY YES.** 数学的内容は citation graph、inline expansion、countermodel analysis で記述できる。新 object は得られない。

### Q9. Does “reachability” again collapse into standard derivability?

**YES.** 独立の意味論も calculus も追加していない。

### Q10. Does “constraint propagation” again collapse into standard proof bookkeeping?

**YES.** induction より heterogeneous な IVT でも、assumption、import、substitution、contradiction の通常記録を越えない。

### Q11. Is route heterogeneity robust to presentation choice?

**NOT FULLY.** displayed organization の差は実在するが、その大きさと共通依存の可視性は library boundary と expansion choice に依存する。

### Q12. Does this test reveal a genuinely new methodological layer: visible dependency vs imported/expanded dependency?

**MODESTLY YES, methodologically; NO as new mathematics.** 以前の route/theorem distinction に、dependency relocation を監査する実用的な中間 record が加わった。ただしこれは標準的 proof-dependency tracing の明示化である。

---

## 23. Kill criteria

### 23.1 What was killed or strongly downgraded

- reachability を derivability 以上の概念として扱う案: **KILL**。
- constraint propagation を ordinary proof bookkeeping 以上の説明原理とする案: **KILL / DOWNGRADE to metaphorical gloss**。
- 二つの proof が同じ resource を使うことから theorem-level necessity を推論する案: **KILL**。
- displayed heterogeneity を presentation-independent property とする案: **KILL**。
- imported theorem expansion を新しい数学的方法とする案: **DOWNGRADE**。ordinary citation/dependency tracing である。

### 23.2 What survived the kill criteria

- routes は expansion 後も trivially identical にはならず、partial convergence に留まった。
- named theorem deletion と theory/hypothesis weakening は、alternate proof と counterexample という異なる evidence burden を持った。
- E1/E2/E3 は少なくとも、\(\mathbb Q\) counterexampleを実数 IVT の反証と誤読すること、library nodeを axiom と誤読することを防いだ。
- formation history は、proof repair と theorem/setting change を区別する記録を保持した。
- completeness reappearance はそれ単独では presentation-relative だが、\(\mathbb Q\) control と組み合わせることで「visible use」「expanded use」「weak-theory insufficiency」を分けられた。

全 bespoke vocabulary を標準語へ置換しても数学的結論は失われない。その意味で新 theory としての結果は negative である。しかし、三種の erasure と displayed/expanded dependency を一枚の監査表に置く methodological value は残った。

---

## 24. Final report

1. **Exact IVT statement:** primary target は、standard \(\mathbb R\) 上で continuous \(f:[a,b]\to\mathbb R\)、\(f(a)<0<f(b)\) なら \(\exists c\in(a,b), f(c)=0\)。一般 IVT とは \(g=f-y\) と endpoint cases で接続した。
2. **Route A:** \(N=\{x:f(x)<0\}\) を作り、\(c=\sup N\) とし、continuityで \(f(c)<0\) と \(f(c)>0\) を排除した。
3. **Route B:** \([a,b]\) connected、continuous image connected、connected subset of \(\mathbb R\) is an interval を経て \(0\in f([a,b])\) を得た。
4. **Clearest route-only failure:** Route A の supremum construction を消しても displayed Route B が同じ setting/target で残る。逆に B1 nodeを消しても inline または A で回復する。
5. **Clearest theorem-hypothesis failure:** continuity を消した step function は endpoint signs を満たすが zero を取らない。
6. **Clearest completeness control:** \([1,2]_{\mathbb Q}\) 上の \(q^2-2\) は連続で符号を変えるが rational root を持たない。
7. **Clearest setting migration:** \(\mathbb R\to\mathbb Q\) は real IVT の falsification ではなく、incomplete ordered-field setting への移動である。
8. **Displayed heterogeneity:** **YES**。local supremum witness route と global connected-image route は異なる organization である。
9. **Expanded heterogeneity:** **PARTIALLY YES**。B1展開で completeness に収束するが、supremum の役割と残る B2/B3 structure は異なる。
10. **Completeness reappearance in B:** **YES**, chosen standard proof of interval connectedness に再登場した。
11. **Did reappearance establish necessity?:** **NO**。一つの expansion の dependency と theorem-level logical necessity は別である。
12. **Did the incomplete-field control strengthen the claim?:** **YES, narrowly**。ordered-field axioms alone の不足を route intersection と独立に示した。LUB の唯一性は示さない。
13. **Was imported theorem expansion useful?:** **YES methodologically**。visible dependency の citation 内への relocation を定位したが、手法は標準的 citation chasing である。
14. **Did theoremhood remain route-agnostic?:** **YES**。static \(\Gamma\vdash\mathrm{IVT}\) は sign-set history と connected-image history のどちらも符号化しない。
15. **Did E1/E2/E3 survive?:** **YES**。alternate route、counterexample/countermodel、same-claim/setting audit が別々の証拠を要求した。
16. **What was genuinely new relative to addition commutativity:** heterogeneous imported structures、displayed vs expanded dependency、dependency hiding/relocation、chosen-expansion reappearance と independent countermodel evidence の分離。
17. **What collapsed again:** reachability は derivability、route は proof organization、constraint propagation は bookkeeping、expansion は dependency/citation tracing に戻った。
18. **Dispositions H1–H13:** H1 RETAIN; H2 DOWNGRADE; H3 DOWNGRADE; H4 RETAIN; H5 DOWNGRADE; H6 RETAIN but not retested; H7 REVISE; H8 RETAIN; H9 RETAIN; H10 REVISE; H11 RETAIN; H12 RETAIN; H13 RETAIN。
19. **Is one more heterogeneous theorem warranted?:** **QUALIFIED YES**。FTA の analytic / topological proofs など、imported support の展開境界を事前固定した一件で、今回の partial convergence が一般化するかを最後に試す価値はある。ただし新語彙の増設ではなく、この audit distinction の falsification test に限定する。
20. **Should theorem_proof_anatomy_v2 remain postponed?:** **YES**。今回得られた追加価値は methodological dependency audit であり、新 theorem/proof anatomy を確定するにはまだ不十分である。

### Final disposition

最も強く残った区別は

\[
\text{displayed-route dependency}
\ne
\text{expanded imported dependency}
\ne
\text{theorem-level necessity evidence}
\]

である。ただしこの区別は標準的 terminology で完全に言い直せる。今回の成果は新しい mathematics ではなく、route failure、support weakening、setting migration を同じ言葉で処理してしまう誤りを減らすための監査手順である。

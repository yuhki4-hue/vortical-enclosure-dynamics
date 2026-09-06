# Reachability-oriented theorem/proof anatomy: \(1+1=2\) 再解剖テスト v0.1

## 0. Status / posture

本稿は **exploratory reinterpretation / stress test** である。

- **not a theorem**
- **not a new logic**
- **not a new proof theory**
- **not a new semantics**
- **not a new arithmetic foundation**
- **not a replacement for standard proof theory**
- **not a claim that mathematical truth is merely relative**
- **not a claim that \(1+1=2\) is false or unstable in ordinary arithmetic**
- **not a claim that axioms are metaphysically arbitrary**
- **no new score**
- **no metric**
- **no geometry / topology / lattice**
- **no universal claim about all mathematics**
- **no VED claim**

中心問いは次である。

> If theorem/proof anatomy is re-described in terms of fixed constraints,
> reachability, route, and formation history,
> what becomes visible in the simplest arithmetic case \(1+1=2\)?

ここで `reachability` は、固定した形式設定で admissible derivation が存在する、という通常の導出可能性を言い換える作業語にすぎない。新しい primitive、意味論、計算体系、不変量は導入しない。中心的な試験結果を先に述べると、**一つの proof path の失敗、理論からの derivability の失敗、形式設定または claim identity の移動を別々に監査する区別は有用だった。しかし `reachability` 自体は、この例ではほぼ完全に通常の \(\Gamma\vdash\varphi\) に吸収された。**

参照した既存系列の方針も維持する。`object / ambient / background / definitional` は層を取り違えないための記述、`R0 / R1 / R2`、escape、closure、blocking、residual は比較用の作業語であって標準数学用語ではない。proof-formation 系で得られた「意味論的結果だけから formation history は復元できない」「record frame が履歴の可視性を決める」「pairwise separation は説明ではない」という否定結果も変更しない。

---

## 1. 最初に固定する一つの標準形式設定

### 1.1 言語と intended interpretation

一階等号論理の言語

\[
\mathcal L_{\mathrm{A}}=\{0,S,+\}
\]

を用いる。`0` は定数記号、\(S\) は一項関数記号、\(+\) は二項関数記号である。通常の算術として読むときの intended interpretation は自然数 \(\mathbb N\)、\(0\)、後者関数 \(n\mapsto n+1\)、通常の加法である。

ただし、次の二つを混同しない。

1. \(\mathbb N\models 1+1=2\) は intended structure における semantic truth の主張である。
2. \(\Gamma_{\mathrm{A}}\vdash 1+1=2\) は固定した calculus と非論理的 axioms / defining equations における syntactic derivability の主張である。

今回 `reachability` と呼ぶのは 2 だけである。1 を 2 に還元する主張はしない。

### 1.2 numerals

numeral は successor notation の略記として置く。

\[
1:=S(0),\qquad 2:=S(S(0)).
\]

この `:=` は、本テストでは object theory の新しい算術公理ではなく、式を展開・縮約できる **metalinguistic definitional abbreviation** を表す。したがって `1` と `2` を原始定数として追加しているのではない。

### 1.3 addition の defining equations

加法は第二引数についての標準的な再帰式で与える。

\[
\tag{Add-0}\forall x\;(x+0=x),
\]

\[
\tag{Add-S}\forall x\forall y\;(x+S(y)=S(x+y)).
\]

一階形式化で \(+\) を原始関数記号として扱う以上、これらは \(\Gamma_{\mathrm{A}}\) に入る非論理的 universally quantified equations である。同時に、数学的役割は \(+\) の recursive definition を与えることである。**形式体系内で axiom として使われること**と、**概念上 definitional role を持つこと**は両立し、同一分類ではない。

Peano-style successor structure の通常の背景として、\(S(x)\neq0\)、\(S(x)=S(y)\to x=y\)、必要なら induction schema を含む標準的算術を ambient に置いてよい。しかし以下の有限導出はそれらを一切使わず、`Add-0`、`Add-S`、numeral abbreviations、等号規則だけで成立する。この unused background を proof resource として二重計上しない。

### 1.4 最小限の equality / inference machinery

今回実際に用いるのは次で足りる。

- universal instantiation;
- equality reflexivity;
- equality symmetry（rewrite direction を反転するときだけ必要）;
- equality transitivity;
- congruence / substitution: \(a=b\) なら \(S(a)=S(b)\)、また文脈内で equals may replace equals;
- definitional abbreviation の展開と縮約。

左辺から右辺への rewrite 表示は証明を読みやすくする記法であり、新しい rewrite calculus ではない。

### 1.5 完全な導出

\[
\begin{aligned}
1+1
&= S(0)+S(0)
&&\text{numeral definition \(1:=S(0)\) を二箇所で展開}\\
&= S\bigl(S(0)+0\bigr)
&&\text{Add-S を \(x=S(0),y=0\) で使用}\\
&= S\bigl(S(0)\bigr)
&&\text{Add-0 を \(x=S(0)\) で使用し、\(S\) の congruence を使用}\\
&=2
&&\text{numeral definition \(2:=S(S(0))\) を縮約。}
\end{aligned}
\]

transitivity により最初と最後を結び、

\[
\Gamma_{\mathrm{A}}\vdash 1+1=2
\]

を得る。ここで induction、\(S\) の injectivity、\(0\) が successor でないこと、commutativity、associativity は使っていない。

---

## 2. 四層の分離

### Layer A — Fixed constraints

この test で動かさないものを、formal category を潰さずに並べる。

| category | fixed ingredient | role | 上の route で使用したか |
|---|---|---|---:|
| logical background | 一階論理、universal instantiation、等号論理 | 何を admissible derivation と数えるか | yes |
| equality machinery | substitution / congruence / transitivity | 局所等式を全体の等式へ運ぶ | yes |
| ambient intended domain | standard \(\mathbb N\) と successor reading | ordinary arithmetic としての意味を固定 | syntactic route には no |
| mathematical background axioms | Peano-style successor axioms、必要なら induction | 自然数 theory の通常の舞台 | no |
| recursive defining equations | `Add-0`, `Add-S` | \(+\) を再帰的に拘束する | yes |
| numeral definitions | \(1:=S(0)\), \(2:=S(S(0))\) | 記号を successor terms に接続する | yes |
| representational convention | 第二引数再帰、左から右への表示 | route を短く可視化する | second-argument recursion は yes、rewrite orientation は表示上のみ |

「この test では fixed」という status と、「axiom」「definition」「inference rule」「ambient assumption」という formal type は別である。fixed なものをすべて axiom と呼ばない。

### Layer B — Reachability claim

\[
\Gamma_{\mathrm{A}}\vdash 1+1=2.
\]

working meaning は厳密に次だけである。

> the target formula has at least one admissible finite derivation under the fixed formal setting.

これは証明の本数、長さ、自然さ、発見順序を述べない。また \(\mathbb N\models1+1=2\) という semantic claim と同じ記号でも同じ種類の主張でもない。

### Layer C — Proof route

第1.5節の四行が一つの route である。その route は

\[
\text{numeral expansion}\to\text{Add-S}\to\text{Add-0 under \(S\)}\to\text{numeral contraction}
\]

を実際に通る。定理の derivability はこの一列より粗く、この一列は derivability の一 witness である。

### Layer D — Formation history

今回の test-local construction history は次である。

1. ordinary arithmetic との同一性を保つため、standard \(\mathbb N\) と successor numerals を採用した。
2. \(1+1\) を短く正規化できるため、第二引数についての recursion clauses を採用した。
3. `1` と `2` を原始定数でなく abbreviation とした。
4. direct calculation が見える route を代表 route に選び、commutativity や induction を経由する長い route を選ばなかった。
5. rule provenance を監査できるよう、各等号に label を付した。

これは Peano 算術や加法が歴史的にこの順序で発見されたという主張ではない。今回の文書をどう構成したかという局所的 history だけである。同じ theoremhood に別の construction history があり得る。

---

## 3. Main distinction: proof path と theorem reachability

> proof path failure is not automatically theorem reachability failure.

### 3.1 同じ \(\Gamma_{\mathrm{A}}\) 内の実在する代替 route

まず次の標準補題を \(\Gamma_{\mathrm{A}}\) 内で証明できる。

\[
\tag{L}\forall x\;(x+1=S(x)).
\]

任意の \(x\) について、

\[
x+1=x+S(0)=S(x+0)=S(x)
\]

だからである。すると別 route は

\[
1+1=S(1)=2
\]

となる。

- route A: 補題 \(L\) を一つの proof resource として呼び出す。
- route B: 第1.5節のように `Add-S` と `Add-0` を inline 展開する。

補題 \(L\) を使用可能な library から消せば route A はそのままでは壊れるが、\(\Gamma_{\mathrm{A}}\) を保持する限り route B が残る。これは明確な **ROUTE FAILURE without REACHABILITY FAILURE** である。

逆向きの route-local erasure もできる。第1.5節の target calculation で `Add-0` の inline rewrite occurrence を使わない、と制限すれば route B はその列のままでは完走しない。しかし既に証明済みの \(L\) を呼び出せる route A は完走する。これは `Add-0` を theory から消したのではなく、一つの route における展開方法を禁じただけである。補題 \(L\) の過去の証明まで監査すれば、その依存先に `Add-0` があることは隠してはならない。

逆に `Add-S` 自体を \(\Gamma_{\mathrm{A}}\) から消すことは、単に route A の一行を消すことではない。補題 \(L\) の根拠も direct route も同時に失わせ得る。この違いが E1/E2 分離の必要性である。

### 3.2 別の標準 presentation

加法を第一引数について

\[
0\oplus y=y,\qquad S(x)\oplus y=S(x\oplus y)
\]

と再帰させる標準 presentation でも、

\[
S(0)\oplus S(0)=S(0\oplus S(0))=S(S(0))
\]

を得る。これは original \(\Gamma_{\mathrm{A}}\) 内の別 proof path ではなく、同じ standard natural-number addition を別の defining presentation で与えた例である。両 presentation の同値性を無証明で仮定して「同じ theory 内の別 route」と数えてはならない。本稿では、3.1 を same-theory route alternative、3.2 を structure-preserving re-presentation として分ける。

---

## 4. 既存 theorem/proof anatomy の読み替え

完全な一対一対応は成立しない。無理に合わせるときは `MISMATCH / OPEN` を残す。

| old anatomy item | reachability-oriented reading in this test | verdict |
|---|---|---|
| object | formal world 内で操作される terms \(0,S(0),S(S(0)),1,2,1+1\) と equality target | FIT |
| ambient | language、calculus、equality、自然数として読む intended structure | FIT。ただし syntax と semantics を分ける必要あり |
| background | 通常は毎行再記載しない一階論理、successor arithmetic、definitional-extension conventions | FIT |
| definitional | `1`, `2`, \(+\) を内部操作可能な expression にする entry support | FIT with qualification |
| assumptions | closed target に対する局所仮定はない。代わりに theory \(\Gamma_{\mathrm{A}}\) の nonlogical axioms がある | **MISMATCH**。`A,B,C ⇒ P` の object hypotheses を強制しない |
| proof resources | defining equations の instances、equality congruence、既証明の補題 \(L\) | FIT。ただし theorem-level necessity と route-level convenience を分ける |
| R0 | clause 消去後に反例 model があり、自然な補正項がない場合 | partial FIT |
| R1 | alternative operations / presentations が許される場合の altered freedom | partial FIT。ただし underdefinition と setting migration を一括しやすい |
| R2 | 同じ式に明示的 correction term が戻る場合 | この例では clear instance なし |
| Erasure Test | 「この route が壊れるか」「全 route を通じた derivability が失われるか」「同じ claim か」を別々に問う | **REVISE** |
| escape route | weakened clauses を満たしつつ target を偽にする interpretations、または別 proof routes | metaphor only。model freedom と proof alternative を混同しない |
| closure / blocking | recursion clauses が \(+\) の admissible interpretations を拘束すること | **MISMATCH risk**。位相的 closure でも新 operator でもない |
| residual | clause 除去後に残る alternative operations、未定義記号、移動先の target | low utility。異なる型を一語でまとめない |

この例で old anatomy から最も有効に継承されたのは、ambient / background / definitional / proof resource の層別である。最も適合しなかったのは residual と closure/blocking であり、標準的な axiom deletion、countermodel、definitional extension、derivability の語で十分である。

---

## 5. Three erasure levels

以下は test-local diagnostic levels であり、新しい formal taxonomy ではない。

### E1 — Route erasure

一つの derivation step、lemma、rewrite occurrence、library resource を消す。

中心質問：

> この具体的 proof path は壊れるか。

例：補題 \(L\) を library から外すと route A は壊れる。しかし `Add-0` と `Add-S` が \(\Gamma_{\mathrm{A}}\) に残るので route B により theoremhood は残る。

### E2 — Reachability erasure

特定の nonlogical axiom、recursion clause、definitional support を theory / presentation から消す。

中心質問：

> retained setting が許す全 route を考えても target は derivable か。

非導出を述べるには「この証明が見つからない」だけでは足りない。以下では reduced axioms を満たして target を偽にする interpretation を示し、少なくとも sound calculus では derivability が残らないことを確認する。

### E3 — Identity erasure

domain、numeral interpretation、operation interpretation、equality notion のような深い固定を変える。

中心質問：

> まだ ordinary arithmetic の同じ \(1+1=2\) を問うているか。

E3 では false / true を判定する前に、対象命題が移動している可能性がある。glyph が同じでも interpretation が違えば claim identity は保存されない。

---

## 6. Fixed constraints の個別 stress

ここで使う labels はすべて test-local diagnostics である。

- **ROUTE FAILURE:** 一つの具体的 proof path が使えない。
- **REACHABILITY FAILURE:** retained formal setting から target が derivable でない。
- **UNDERDEFINITION:** 必要な symbol / operation / numeral の指定が不足する。
- **TARGET MIGRATION:** 近接する別 target が derivable になる。
- **TERRAIN / SETTING MIGRATION:** formal environment または interpretation が変わる。
- **CLAIM-IDENTITY BREAK:** 同じ proposition を論じているという同一性が失われるか、不成立になる。

複数 label を同時に付けてよい。これは score や順序ではない。

### F1 — numeral definition \(2:=S(S(0))\) を外す

採用 setting では `2` は abbreviation である。これを消すと、文字列 `1+1=2` の右辺 `2` はこの presentation 内で展開規則を持たない。

- expanded target \(S(0)+S(0)=S(S(0))\) は依然として導出できる。
- したがって ordinary arithmetic relation が偽になったわけではない。
- しかし token `2` を含む target は、採用した略記規約では **UNDERDEFINITION** になる。
- `2` を原始定数へ変更し defining axiom だけを外す別読みでは、`2` は任意の自然数を指し得る。standard \(\mathbb N\) と standard \(+\) のまま `2` を 3 と解釈する model が target を偽にするため、その拡張言語の reduced theory では **REACHABILITY FAILURE + UNDERDEFINITION** になる。

後者は元の abbreviation presentation から原始定数 presentation への変更も含む。両者を「theorem false」の一語でまとめない。最も適切な主判定は **UNDERDEFINITION** である。

### F2 — `Add-0`: \(x+0=x\) を外す

direct route は

\[
S(0)+S(0)=S(S(0)+0)
\]

で停止する。しかもこれは route の偶然ではない。standard domain \(\mathbb N\) と standard successor を保ち、二項演算を

\[
a\oplus b:=a+b+1
\]

と定めると、

\[
a\oplus S(b)=S(a\oplus b)
\]

なので残った `Add-S` は満たすが、\(1\oplus1=3\neq2\) である。よって reduced equational theory から target は導出できない。

判定：**ROUTE FAILURE + REACHABILITY FAILURE + UNDERDEFINITION**。underdefinition は、残った clause だけでは operation を standard addition に一意に拘束しない、という意味である。これは standard addition 自体が不安定という意味ではない。

### F3 — `Add-S`: \(x+S(y)=S(x+y)\) を外す

最初の computational step が使えない。さらに \(\mathbb N\) と standard successor を保ち、

\[
a\oplus0:=a,\qquad a\oplus b:=0\quad(b>0)
\]

とすれば `Add-0` は満たすが \(1\oplus1=0\neq2\) である。

判定：**ROUTE FAILURE + REACHABILITY FAILURE + UNDERDEFINITION**。ここでも reduced theory が standard addition を十分に指定しなくなったのであり、ordinary \(\mathbb N\) の addition theorem の反証ではない。

### F4 — numeral representation を変え、natural-number structure を保つ

単なる記号変更として

\[
0\mapsto z,\qquad S\mapsto\sigma,\qquad +\mapsto\oplus
\]

を行い、

\[
\mathsf{one}:=\sigma(z),\qquad \mathsf{two}:=\sigma(\sigma(z)),
\]

\[
x\oplus z=x,\qquad x\oplus\sigma(y)=\sigma(x\oplus y)
\]

とする。対応する derivation は

\[
\mathsf{one}\oplus\mathsf{one}
=\sigma(z)\oplus\sigma(z)
=\sigma(\sigma(z)\oplus z)
=\sigma(\sigma(z))
=\mathsf{two}.
\]

これは symbol-for-symbol translation であり、算術関係を保存する。判定は **no failure; representation-preserving re-derivability**。表示が変わっただけで structural change はない。

### F5 — algebraic structure を \(\mathbb Z/2\mathbb Z\) へ変える

mod 2 addition では

\[
\overline1+\overline1=\overline0.
\]

これは ordinary natural-number addition における \(1+1=2\) の反証ではない。domain と operation が変わった **TERRAIN / SETTING MIGRATION** である。

さらに注意が要る。integer numeral `2` を residue class \(\overline2\) と読むなら \(\overline2=\overline0\) なので、

\[
\overline1+\overline1=\overline2
\]

も同じ構造内で真である。表示を `1+1=0` にしたとき起きたのは、ordinary target の偽化ではなく、canonical residue representative への **TARGET MIGRATION** である。glyph `2` を残すか消すかだけで数学的対立を演出してはならない。

判定：**TERRAIN / SETTING MIGRATION + TARGET MIGRATION + ordinary claim に対する CLAIM-IDENTITY BREAK**。

### F6 — domain と numerals を保ち、`+` の interpretation だけを変える

\(\mathbb N\)、\(0\)、\(S\)、従って \(1,2\) を保つが、glyph `+` を

\[
a+b:=\max(a,b)
\]

と解釈し直すと、\(1+1=1\) であり \(1+1=2\) は偽になる。しかしこの operation は `Add-S` を満たさず、ordinary addition ではない。

判定：**TERRAIN / SETTING MIGRATION + TARGET MIGRATION + CLAIM-IDENTITY BREAK**。文字列が同じでも proposition の interpretation は同じでない。

### 6.1 stress summary

| stress | route | derivability under retained reduced theory | main diagnosis |
|---|---|---|---|
| lemma \(L\) の route-level removal | route A fails | route B survives | ROUTE FAILURE |
| F1 numeral abbreviation `2` removal | displayed route cannot close as written | expanded relation survives | UNDERDEFINITION; presentation issue |
| F2 `Add-0` removal | stalls | countermodel exists | ROUTE + REACHABILITY FAILURE; UNDERDEFINITION |
| F3 `Add-S` removal | first computation unavailable | countermodel exists | ROUTE + REACHABILITY FAILURE; UNDERDEFINITION |
| F4 notation renaming | old inscription changes | translated derivation survives | representation-preserving re-derivability |
| F5 mod 2 | ordinary route is no longer the governing route | nearby residue relation holds | SETTING + TARGET MIGRATION; identity break |
| F6 reinterpret `+` | original arithmetic route inapplicable | altered-operation target differs | SETTING + TARGET MIGRATION; identity break |

---

## 7. Failure mode classification の監査

この例は、old `R0/R1/R2` だけでは少なくとも三つの差を失う。

1. F1 の abbreviation loss は ordinary falsehood ではなく underdefinition である。
2. F2/F3 は reduced theory の underconstraint と non-derivability を同時に起こす。
3. F5/F6 は同じ theorem の failure より先に setting / claim identity を変える。

R0 と書けば F1–F3 のかなりの部分を一括でき、R1 と書けば F4–F6 の変化を一括できる。しかしその圧縮は今回知りたい型の差を消す。R2 に相当する自然な explicit correction term は確認できない。従って本テストでは R0/R1/R2 を置換しない一方、主診断には使わない。

これは新 taxonomy の提案ではない。単一 stress test で誤読を避けるため、標準語 `non-derivable`, `underdefined`, `different interpretation`, `different target` を大文字 labels で一時的に見やすくしただけである。

---

## 8. 実際に何が「fixed」なのか

問いは次である。

> Is \(1+1=2\) fixed, or are the deeper constraints fixed such that \(1+1=2\) is re-required?

形式的には、bare formula \(1+1=2\) が自分自身を固定しているわけではない。固定された言語、numeral conventions、addition clauses、inference machinery のもとで、その formula が derivable になる。

しかし、これを「命題は単なる可変な convention」と読んではならない。標準自然数構造と通常の加法を十分に保存すれば、対応する有限算術関係は異なる notation や標準 presentation でも繰り返し導出される。慎重な結論は次である。

> under sufficiently preserved natural-number structure,
> the corresponding arithmetic relation is repeatedly derivable.

この安定性は強い。だが本テストはそこから “the proposition itself is metaphysically immovable” を導かない。逆に、その形而上学的文を否定する証明にもなっていない。

---

## 9. Axiom と definition を分ける

### 9.1 category audit

| ingredient | fixed by stipulation in this test? | formal status | mathematical role |
|---|---:|---|---|
| classical first-order derivation rules | yes | logical background / inference machinery | admissible inference を定める |
| equality congruence and transitivity | yes | logical rules / axioms of equality, calculus に依存 | equality を term context 内で運ぶ |
| Peano successor axioms | yes as ambient arithmetic background | nonlogical mathematical axioms | natural-number structure を拘束する |
| induction | may be included in ambient | axiom schema / rule, presentation に依存 | general arithmetic reasoning; 今回 unused |
| `Add-0`, `Add-S` | yes | object theory では nonlogical equations; role は recursive definition | \(+\) を拘束し計算を可能にする |
| \(1:=S(0),2:=S(S(0))\) | yes | metalinguistic definitions / abbreviations | numerals を successor terms に接続する |
| standard \(\mathbb N\) interpretation | yes for ordinary-reading audit | semantic ambient choice, axiomではない | symbols の intended meaning を固定する |

したがって “axiom = immovable thing” は採用しない。axiom は formal presentation 内の sentence / schema という型であり、「この test で動かさない」は実験上の posture である。同じ item が fixed でも、definition、rule、semantic interpretation、representational convention のいずれかであり得る。

### 9.2 defining equation の二重 status

`Add-0` と `Add-S` は特に注意を要する。first-order language で \(+\) を primitive function symbol とすれば、証明内では axioms として instance 化される。一方、primitive recursion から \(+\) を導入する definitional extension の presentation では、同じ equations が operation の definition を保証する。

従って「axiom か definition か」は文面だけでなく presentation に相対する。しかしそれは arbitrary という意味ではない。どの presentation でも、conservativity、existence / uniqueness、intended interpretation との一致など、必要な preservation conditions がある。

---

## 10. Definition as entry condition

working hypothesis は次である。

> a definition can function as an entry condition that makes a concept
> available for internal manipulation.

### `1`

`1:=S(0)` は短い name を与える。これを消しても \(S(0)\) という term と対応する自然数は消えない。消えるのはこの presentation での shorthand と、その shorthand を展開する明示的 license である。

### `2`

`2:=S(S(0))` も同様である。F1 が示すように、definition の削除はまず token `2` の underdefinition を起こす。expanded relation は残り得る。

### `+`

二つの recursion clauses は、単なる短縮名より強い。式 \(x+y\) を successor terms へ計算的に結び、operation の振る舞いを内部推論へ供給する。片方を消すと F2/F3 の alternative operations が許される。

### 判定

definition は concept を無から存在させるとは限らない。alternative notation や definition で同じ relation を再導入できる。また definition が外部から truth を「生む」とも言わない。今回の definitions は

- terms を well-specified にし、
- operation の admissible behavior を拘束し、
- relation を形式言語内で記述・計算可能にする。

従って entry-condition 読みは略記と recursive operation の役割差を可視化する限り有用だが、標準的 definitional practice 以上の原理ではない。

---

## 11. Theorem as route organization / reachability compression

working hypothesis は次である。

> a theorem is better viewed here as a compressed statement of reachable relation
> under fixed constraints than as a fixed object.

この文は三つに分けないと曖昧になる。

1. **theorem formula \(1+1=2\):** target formula であり、route でも \(\Gamma\) でもない。
2. **theoremhood claim \(\Gamma_{\mathrm{A}}\vdash1+1=2\):** fixed theory と target の間の derivability status を圧縮している。
3. **proof object / derivation:** theoremhood claim の witness となる具体的 finite sequence / tree である。

したがって theorem statement itself = route ではない。statement = endpoint だけ、と言うのも、背景 \(\Gamma_{\mathrm{A}}\) を消すなら粗すぎる。最も正確なのは、**bare statement ではなく sequent / theoremhood assertion が compressed derivability information を持つ**、である。

route A と route B が同じ target を証明することからも、theoremhood は route-specific でない。ただし “reachability compression” は \(\Gamma\vdash\varphi\) に新しい数学的内容を加えない。この stress test では説明比喩としてのみ残る。

---

## 12. Proof as constraint-propagation record

working hypothesis は次である。

> a proof records how fixed constraints propagate into an unavoidable conclusion.

第1.5節を stepwise に監査する。

| step | already fixed | applied resource | newly available equality | something created? |
|---|---|---|---|---|
| \(1+1=S(0)+S(0)\) | numeral abbreviations | definitional expansion | shorthand-free left term | new arithmetic fact は created されない |
| \(S(0)+S(0)=S(S(0)+0)\) | `Add-S` | instance \(x=S(0),y=0\) | outer successor form | defining equation の consequence を露出 |
| \(S(S(0)+0)=S(S(0))\) | `Add-0` and equality congruence | \(S(0)+0=S(0)\) を \(S(\cdot)\) 内へ substitution | normalized successor term | permitted consequence を露出 |
| \(S(S(0))=2\) | numeral abbreviation for 2 | definitional contraction | target notation | new object / truth は created されない |
| endpoint | prior equalities | transitivity | \(1+1=2\) | derivation record が theoremhood の witness になる |

“constraint propagation” は、rules と equations の repeated application を一つの視野に置く説明である。物理的な force、causal transmission、時間発展ではない。また「unavoidable」は、\(\Gamma_{\mathrm{A}}\) と calculus を固定したとき否定を任意に選べないという意味であり、metaphysical necessity を意味しない。

この読みは「証明が truth を作る」という主張を退ける点では有効である。しかし標準的には、これは等式規則による derivation / normalization の記録である。新しい proof theory は得られない。

---

## 13. Static reading と historical reading

### Static

\[
\Gamma_{\mathrm{A}}\vdash1+1=2.
\]

少なくとも一つの derivation が存在する。どの derivation を人が先に書いたか、どの notation が選ばれたか、補題を library から呼んだかはこの assertion に含まれない。

### Historical

今回の construction は、第二引数 recursion、successor numerals、direct normalization、rule labels を選んだ。別 construction は補題 \(L\) を先に作り、二行で target に到達する。第一引数 recursion presentation を採る construction もある。

同じ theoremhood が同じでも、formation history は複数あり得る。逆に、同じ endpoint inscription だけを記録しても、どの route が通られたかは復元できない。

この点は proof-formation 系の結果に直接接続する。

- endpoint semantics は route history を同定しない。
- typed transition record は history を**記録**できるが、どの history が正当だったかをそれだけで証明しない。
- theoremhood の static record と construction の historical record は別 field を必要とする。

---

## 14. Deep fixed constraints

問いは次である。

> Some fixed constraints may be so deep and routinely shared
> that they are rarely restated. Does that explain why \(1+1=2\) feels immovable?

部分的には yes である。ただし “deep axiom” という新用語は定義しない。少なくとも次を分ける。

- **explicit fixed constraints:** `Add-0`, `Add-S`, numeral expansions;
- **tacit/background fixed constraints:** logic、equality、term formation、standard proof conventions;
- **representational conventions:** successor notation、第二引数 recursion、glyph `+`;
- **logical machinery:** instantiation、congruence、transitivity;
- **semantic ambient choice:** symbols を ordinary \(\mathbb N\) と standard addition で読むこと。

\(1+1=2\) が極めて安定して感じられる理由の一部は、この多くが共有され、通常の計算では再記載されないこと、しかも結論が induction すら不要なごく短い defining-equation consequence であることにある。

しかし sufficiently deep な constraint、たとえば domain や operation interpretation を変えると、それは theorem の一条件を弱めるというより formal setting の変更になる場合がある。F5/F6 はその例である。そこでの failure は ordinary theorem failure でなく claim-identity break を伴う。

---

## 15. “Return”, “reappear”, “re-required” の意味

これらを時間的復元力として扱わない。本稿で許す working meaning は次だけである。

> after a representation-preserving or structure-preserving reformulation,
> an equivalent or corresponding relation is again derivable.

F4 では、symbol translation 後に対応する derivation が再構成された。3.2 では、standard addition の別 recursive presentation で対応する relation が導出された。どちらにも、命題が自力で元位置へ戻る過程や restoring force はない。

\[
\text{IMMOBILE}\neq\text{RE-DERIVABLE UNDER TRANSFORMATION}.
\]

`is re-required` も「保存条件を満たす reformulation の後、対応する target が再び consequence になる」という略記に限定する。

---

## 16. “Elasticity” analogy の stress

最低限、次を分ける。

| expression | 本稿での慎重な読み |
|---|---|
| immobility | claim 自体が動かないという強い形而上学的読み。今回 support しない |
| re-derivability after admissible change | F4 のように preservation conditions 下で対応 relation が再導出される |
| fragility | 一つの route または presentation support の小変更で表示・導出が壊れる |
| underdetermination | F2/F3 のように reduced clauses が operation を十分拘束しない |
| migration | F5/F6 のように別 structure / interpretation / target へ移る |

`elasticity`, `restoring force`, `rigidity` は、使うとしても **metaphor only** である。数値、ordering、metric、formal invariant は定義しない。この例ではむしろ、elasticity 語彙は route repair、representation invariance、model underdetermination を一語に潰す危険が高く、技術記述からは外す方がよい。

---

## 17. Why this is not “anything goes”

形式条件への相対化は unrestricted relativism を意味しない。

1. **fixed theory は derivability を拘束する。** \(\Gamma_{\mathrm{A}}\) からは \(1+1=2\) が導出され、同じ consistent ordinary arithmetic で \(1+1=7\) を好みで選ぶことはできない。
2. **arbitrary reinterpretation は problem を変える。** `+` を `max` に変えた F6 は、同じ glyph を保っても同じ addition claim ではない。
3. **not every target is derivable.** fixed consistent theory では derivability と non-derivability の差がある。
4. **十分深い変更は claim identity を壊す。** その場合「元 theorem が false」と報告する前に、何を保存したかを問う必要がある。
5. **successful re-expression には preservation conditions が要る。** F4 は language translation が constants、successor、operation、equality を対応させるから成功する。単なる文字置換一般が成功するのではない。
6. **truth と proof を同一視しない。** 本稿は \(\Gamma\vdash\varphi\) を扱うが、formal derivability が mathematical truth の全てを尽くすとは主張しない。

従って「条件が変われば結論も変わり得る」から「どんな結論でも同じ意味のまま自由に選べる」は従わない。

---

## 18. Prior proof-formation stress tests への接続

### 18.1 action classification instability

過去の有限 propositional tests では、semantic effect が move label を一意に決めず、M1 / M2 / scope の区別は主に typed record に担われた。今回も route を “unfolding”, “lemma use”, “normalization” などと label しても、その label 自体は theoremhood の primary fact ではない。重要なのは、どの formal resource がどの equality を正当化したかである。

**再配置:** route label は primary でなく、derivation validity と resource dependence の annotation である。

### 18.2 semantic collapse of different moves

direct route、lemma route、別 presentation は、保存条件を明示すれば対応する endpoint に至る。しかし formation histories は異なる。same endpoint / reachability effect から一つの construction history を逆算できない。

**再配置:** static theoremhood は multiple histories を quotient したように見えるが、本稿は formal quotient object を導入しない。単に theoremhood assertion が history を記録しないと述べる。

### 18.3 record-frame dependence

endpoint だけを保つ frame では route A/B は collapse する。rule-labelled sequence を保つ frame なら区別でき、definition choice や選択理由まで保つ frame なら formation history の差が見える。しかし richer frame はその history の正当性、自然さ、重要性を自動的に証明しない。

visibility-transition / non-nested-frame tests の結果どおり、「最初に見える frame」や可視性 sequence は frame-family-relative である。今回も theorem statement < sequent < derivation < annotated construction history という並びを canonical hierarchy に昇格させない。

### 18.4 cross-frame persistence

複数 record frame に共通して endpoint equality を残すよう設計すれば \(1+1=2\) は persistent に見える。しかしその persistence は shared projector design の結果でもあり、route、representation choice、provenance を保存しない。frame-independent invariant とは呼ばない。

### 18.5 minimal separator failure

二つの proof histories を `used_lemma_L` の一 field で区別できても、その singleton separator は、なぜ一方が mathematically valid か、なぜ theorem reachability が保存されたかを説明しない。pairwise distinguishability と explanatory adequacy は別である。

**再配置:** history record は route difference を保存できるが、reachability difference の理由は axioms / rules / countermodels の分析から得る。metadata separation からは得ない。

### 18.6 接続結果

この再解剖は、過去の否定結果を撤回しない。むしろ

\[
\text{static derivability}\quad/\quad\text{route witness}\quad/\quad\text{recorded formation history}
\]

を分けることで、semantic collapse と historical non-identifiability を theorem anatomy 側へ配置し直す。proof-formation record は theoremhood を置換せず、theoremhood は formation history を復元しない。

---

## 19. Strong falsification questions

### Q1 — Does “reachability” add anything beyond ordinary derivability notation?

**ほぼ no。** この例では “reachable” は \(\Gamma_{\mathrm{A}}\vdash\varphi\) の言い換えである。新しい判定手続き、意味論、invariant、theorem は得られない。追加価値があるとすれば、「特定 route の有効性」と「何らかの route の存在」を会話上分けやすくすることだけである。

### Q2 — Does “proof as route” add anything beyond ordinary derivation sequence?

**数学的には no。** route は derivation sequence / tree で尽くされる。formation history と接続する説明上の利点はあるが、標準 proof object を越えない。

### Q3 — Does separating route failure from reachability failure materially improve the old anatomy?

**yes, relative to the old audit.** old anatomy も assumptions と proof resources を分けていたが、Erasure Test を E1/E2 に明示分割すると、「一つの補題を外す」「defining clause を theory から外す」を同じ failure と報告する誤りを防げる。さらに E3 により setting migration を theorem failure から分けられる。これは新 proof theory ではないが、監査上の実質的改善である。

### Q4 — Does “definition as entry condition” clarify anything?

**limited yes.** `2` の abbreviation loss と `+` の recursive underdetermination を区別し、definition が concept を存在させることと notation / manipulation を可能にすることを分ける。ただし内容は standard definitional practice の再記述である。

### Q5 — Does “fixed constraints → re-required relation” avoid a false metaphysical impression?

**qualified yes.** preservation conditions と re-derivability を明示することで immobility metaphor を弱められる。ただし standard invariance under translation / equivalent presentation の説明で十分であり、形而上学的結論は正負どちらにも出ない。

### Q6 — New analytical capability or intuitive vocabulary?

**主として intuitive / audit vocabulary。** 新能力に最も近いのは、old Erasure Test を route / derivability / setting-identity の三質問へ分けたことだけである。その区別自体も標準論理学に既にある。従って「新しい theorem anatomy が成立した」とはまだ言えない。

---

## 20. Candidate findings

| candidate | result | audit |
|---|---|---|
| C1 Proof path と theorem derivability を分ける | **SUPPORTED** | lemma route erasure と inline route が分離例 |
| C2 definitions、axioms、rules、background は別役割 | **SUPPORTED** | fixed status は formal type でない |
| C3 representation change can preserve relation | **SUPPORTED with preservation conditions** | F4 の explicit translation |
| C4 structure change can alter corresponding proposition without refuting ordinary claim | **SUPPORTED** | F5/F6 |
| C5 deep background change may cause identity break | **SUPPORTED** | operation/domain/equality interpretation の変更 |
| C6 theorem statement is less route-specific than proof history | **SUPPORTED** | route A/B が同じ target |
| C7 proof as consequence exposure / constraint propagation record | **SUPPORTED as a gloss** | step audit は可能。causal/physical reading は棄却 |
| C8 reachability is mostly standard derivability re-description | **SUPPORTED strongly** | Q1/Q2 の negative result |
| C9 strongest useful distinction is route / reachability / setting-identity | **SUPPORTED test-locally** | E1/E2/E3 と F1–F6 が分離 |
| C10 anatomy may connect theorem erasure and formation history | **SUPPORTED as an audit bridge** | static theoremhood と historical route を同一視しない。replacement theory ではない |

C9 を「新しい formal taxonomy」として昇格させない。新規なのは数学的内容ではなく、既存 anatomy 内で三種類の erasure question を同じ欄に置かない運用である。

---

## 21. Retain / revise / downgrade / kill

複数 disposition を許す。判定はこの toy test に限定する。

### H1 — “axioms/background are the fixed anchors of theorem formation”

**REVISE + DOWNGRADE.** fixed ingredients は axioms/background だけでなく definitions、logical rules、equality machinery、semantic interpretation、representation conventions を含む。“anchor” は説明語としては使えるが formal category ではない。`everything fixed = axiom` は KILL する。

### H2 — “proof is a record of constraint propagation”

**RETAIN + DOWNGRADE.** 各等式 step が fixed equations の consequence を露出する記録、という読みは機能する。しかし標準的 derivation / normalization 以上の内容はなく、physical causation や truth creation の読みは KILL する。

### H3 — “theorem is compressed reachability under fixed constraints”

**REVISE + DOWNGRADE.** bare formula でなく \(\Gamma\vdash\varphi\) という theoremhood claim なら compressed derivability statement と読める。だがそれは普通の sequent notation の言い換えである。「theorem は fixed object でない」を新 ontological thesis にする読みは KILL する。

### H4 — “route failure and theorem-reachability failure should be separated”

**RETAIN.** 今回もっとも明確に生き残った仮説である。lemma erasure と defining-clause erasure の差を実際に区別した。さらに setting / identity migration を第三の結果として分ける revision を加える。

### H5 — “definitions function as entry conditions into the formal world”

**REVISE.** numerals では shorthand への entry、\(+\) では internal manipulation を可能にする behavior specification として有効。しかし definition が concept や relation を無から作るわけではなく、alternative representation / conservative definition があり得る。標準 definitional practice 以上の強い読みは DOWNGRADE する。

### H6 — “\(1+1=2\) illustrates re-derivability under preserved structure rather than metaphysical immobility”

**RETAIN with strict qualification.** F4 と alternate recursion presentation は corresponding relation の再導出を示す。ただし metaphysical immobility を反証したのでも、truth を convention に還元したのでもない。主張は structure-preserving reformulation に限定する。

---

## 22. Strongest caution

本テストから次を結論してはならない。

- mathematical truth is just convention;
- axioms are arbitrary;
- \(1+1=2\) can be made false without changing meaning;
- all theorems are equally relative;
- proof creates truth;
- formal derivability exhausts truth;
- model-theoretic truth and proof-theoretic derivability are the same;
- “reachability” is already a new theorem or invariant;
- physical-world truth follows from this toy arithmetic test.

とくに F5/F6 は「意味を保ったまま \(1+1=2\) を偽にした」例ではない。意味または formal setting を変えたため、ordinary claim への反例にならない。また本稿の derivation は syntactic result であり、model-theoretic truth との接続には soundness、completeness、intended interpretation 等を別途区別して扱う必要がある。

---

## 23. Final report

1. **Exact fixed ingredients.** 一階等号論理、\(\mathcal L_{\mathrm A}=\{0,S,+\}\)、Peano-style natural-number / successor background、`Add-0`、`Add-S`、\(1:=S(0)\)、\(2:=S(S(0))\)、instantiation・congruence・transitivity。実際の短い proof は recursion clauses、numeral definitions、equality machinery だけを使った。

2. **One explicit proof route.**
   \[
   1+1=S(0)+S(0)=S(S(0)+0)=S(S(0))=2.
   \]
   順に numeral expansion、`Add-S`、`Add-0` under congruence、numeral contraction である。

3. **Clearest route failure.** 既証明補題 \(L:\forall x(x+1=S(x))\) を library resource から消すと lemma route は壊れるが、inline route は残る。

4. **Clearest reachability failure / underdefinition.** `Add-S` を消すと残った `Add-0` を満たしつつ \(1\oplus1=0\) となる operation が \(\mathbb N\) 上にあり、reduced theory は target を導出しない。operation は underdetermined になる。`2` definition の消去はより純粋な underdefinition 例である。

5. **Clearest setting migration.** ordinary \(\mathbb N\) から \(\mathbb Z/2\mathbb Z\) へ移り、canonical residue 表示で \(1+1=0\) とする場合。

6. **Clearest claim-identity break.** 同じ glyph `+` を \(\max\) と再解釈して \(1+1=1\) とする場合。文字列の類似は ordinary addition proposition の同一性を保存しない。

7. **Did representation change preserve the relation?** Yes, explicit symbol translation と対応 recursion clauses を保つ F4 では、対応 relation がそのまま再導出された。

8. **Was proof-path / theorem-reachability separation useful?** Yes。今回もっとも強く生き残った区別である。proof resource の loss と theory support の loss を分け、さらに setting migration を theorem failure と分けた。

9. **Did definition-as-entry clarify anything?** Limited yes。numeral shorthand の loss、operation specification の loss、concept disappearance を別々に述べられた。ただし標準的 definition の説明を越えない。

10. **Was theorem-as-reachability compression more than metaphor?** Mostly no。bare theorem formula には不十分で、\(\Gamma\vdash\varphi\) と書けば通常の derivability statement そのものである。新しい数学的対象は得られなかった。

11. **What genuinely changed relative to `theorem_proof_anatomy_v1.1`.** Erasure Test を route erasure、derivability erasure、setting / identity erasure に分割したこと、proof route と test-local formation history を別層として明示したこと、proof resource の消去と theorem condition の消去を別質問にしたこと。

12. **What did not change.** object / ambient / background / definitional / proof-resource の層別、標準 derivability、standard arithmetic truth、既存 proof theory の優先、R-labels が説明用にすぎないこと、独自語彙を消しても数学的内容が残るという過去 stress tests の negative result。

13. **H1–H6 disposition.** H1 `REVISE + DOWNGRADE`; H2 `RETAIN + DOWNGRADE`; H3 `REVISE + DOWNGRADE`; H4 `RETAIN`; H5 `REVISE`（strong reading は `DOWNGRADE`）; H6 `RETAIN with strict qualification`。

14. **Should this anatomy be tested on a nontrivial theorem next?** Qualified yes。今回の target は category errors を露出する calibration target として良かったが、induction、nontrivial lemma dependence、multiple genuinely different proof routes、local assumptions をほぼ使わない。次は、同じ arithmetic setting での加法可換律 \(\forall x\forall y(x+y=y+x)\) のような、induction と補助補題を実際に要する theorem が適切である。

15. **Should a v2 rewrite remain postponed?** Yes。H4 は nontrivial follow-up test に値するが、H3 の reachability vocabulary と H2 の route vocabulary はこの例では標準 derivability / derivation sequence にほぼ完全に collapse した。一つの極小例だけで anatomy v2 を書く根拠はない。

### Overall verdict

\(1+1=2\) は、reachability-oriented reading の**最初の calibration / falsification target としては良かった**。短すぎるため proof-theoretic richness は試せなかったが、その単純さのおかげで、語彙の追加価値を数学的複雑さで隠さずに済んだ。

生き残った中心は

\[
\boxed{\text{route failure}\neq\text{derivability failure}\neq\text{setting / claim-identity migration}}
\]

という監査上の分離である。ただし箱の式は新 theorem でも formal trichotomy でもなく、既存の標準的区別を old anatomy の Erasure Test に明示的に持ち込んだ要約である。新 anatomy は非自明な follow-up test を一回行う価値を得たが、v2 rewrite は引き続き postponed とする。

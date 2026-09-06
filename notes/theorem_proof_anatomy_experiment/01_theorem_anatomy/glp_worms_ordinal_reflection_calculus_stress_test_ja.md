# Japaridze の多重様相証明可能性論理 GLP・worms・順序数表記／reflection calculus
## special stress test

本稿でいう「moving boundary」「固定する側／固定される側」「証明デザイン」「段階化」「再入力」「残差」は、定理・論理体系を比較するための解剖的メタ記述であり、標準的な様相論理・証明論の用語ではない。技術的主張には GLP、算術的証明可能性解釈、worms、Beklemishev 順序、reduction property、reflection calculus、保存性、proof-theoretic ordinal という標準語彙を優先する。

## 0. 採用する GLP の版

主分析では、古典命題論理に可算個の様相演算子

\[
[0],[1],[2],\ldots
\]

を加えた \(\mathrm{GLP}_\omega\) を採用する。双対を

\[
\langle n\rangle A:=\neg[n]\neg A
\]

と定める。Hilbert 系は、古典命題論理の恒真式、modus ponens、各 \(n\) についての necessitation

\[
\vdash A\quad\Longrightarrow\quad\vdash[n]A
\]

に加え、次を持つ。

\[
[n](A\to B)\to([n]A\to[n]B)
\tag{K_n}
\]

\[
[n]([n]A\to A)\to[n]A
\tag{L_n}
\]

\[
[m]A\to[n]A\qquad(m\le n)
\tag{Mon}
\]

\[
\langle m\rangle A\to[n]\langle m\rangle A
\qquad(m<n).
\tag{Mix}
\]

最後の二つが modality 間の interaction axioms である。添字の向きは重要で、\(n\) が大きいほど算術的解釈で強い証明可能性を表す。本稿では \(4_n:[n]A\to[n][n]A\) を独立公理に加えない。各 \(n\) の GL 部分で導出されるからである。この定義は標準的な \(\mathrm{GLP}_\omega\) の提示に従う。[Pakhomov, GLP の公理系](https://www.mi-ras.ru/~pakhfn/preprints/2013/elm_thr_glp0.pdf)、[Joosten, GLP と ordinal analysis](https://arxiv.org/abs/1212.2395)

ここで pure modal system、算術的解釈、closed fragment の worms、reflection calculus は別物である。後三者は GLP の定義公理ではなく、解釈または派生した解析装置である。

## 1. GL と GLP の違い

GL は一つの \(\Box\) によって一つの証明可能性概念の反復を抽象化する。GLP は複数の \([n]\) を置き、異なる複雑度・反射強度の証明可能性概念と、その間の相互作用を抽象化する。

ただし modality index \(n\) は Turing–Feferman progression の stage \(a\) ではない。標準算術解釈では \(n\) は概ね「どの複雑度の真な算術文を補助資源として許すか」または「どの反射レベルを扱うか」を示す。一方 stage index は、同じ operator を何回・どの順序数長まで反復したかを示す。同じ \(n\) を worm 内で反復するだけでも長い progression が表現され得る。

## 2. 四つの index の分離

| index | 例 | 数学的役割 | 同一視してはいけない対象 |
|---|---|---|---|
| modality index | \([n]\), \(\langle n\rangle\) の \(n\) | 証明可能性・反射の複雑度レベル | theory stage |
| worm の位置・入れ子 | \(\langle n_k\rangle\cdots\langle n_1\rangle\top\) | operator の有限反復と混合順序 | modality index 単独 |
| ordinal assignment | \(o(A)\) | worm 同値類の順序型・ランク | worm という構文そのもの |
| theory-stage notation | \(T_a\) の \(a\) | recursive progression の段階を提示 | GLP の modality index |

対応が生じるのは解釈と保存定理を介した場合だけである。有限 worm の modal depth、最大 modality、\(o(A)\)、Turing notation \(|a|\) は四つの異なる量である。

## 3. 通常 anatomy

### 3.1 system_name

Japaridze’s polymodal provability logic \(\mathrm{GLP}_\omega\)、その worm fragment、Beklemishev ordering、および関連する reflection calculus。

### 3.2 domain

多重様相論理、算術的証明可能性論理、反射原理、proof-theoretic ordinal、保存性解析。

### 3.3 standard_definition

Pure \(\mathrm{GLP}_\omega\) は第0節の公理・規則で定義される。worm は \(\top\) から有限回 dual modalities を前置して得られる閉式である。算術的解釈では \([n]\) を段階づけられた証明可能性、\(\langle n\rangle\) をその双対である段階づけられた整合性として読む。Beklemishev ordering は、適切な worm 集合上で

\[
A<_n B
\quad:\Longleftrightarrow\quad
\mathrm{GLP}_\omega\vdash B\to\langle n\rangle A
\]

により定める。

### 3.4 assumptions_ABC

- A: 古典命題論理を基礎とする。
- B: 可算個の normal modalities \([n]\) を持つ。
- C: 各 modality が \(K_n\)、\(L_n\)、necessitation を満たす。
- D: \(Mon\) と \(Mix\) の inter-modal interaction axioms を持つ。
- E: worm fragment では、命題変数を除き \(\top\) と \(\langle n\rangle\) だけから閉式を作る。
- F: 算術解釈を論じる場合、十分な初等算術的基礎理論（主例では EA）と形式化された partial truth／proof predicates を固定する。
- G: ordinal analysis では、worm を GLP-provable equivalence で割り、\(<_n\) の適切な定義域を固定する。
- H: reflection calculus や reduction property を使う場合、その正の言語、算術解釈、保存する式クラスを別途固定する。

F–H は pure GLP の公理ではない。F は interpretation-side、G は解析対象の定義、H は派生体系・メタ定理の条件である。

### 3.5 hypothesis_levels

- A: ambient — 基礎論理を固定する。
- B: definitional / ambient — GLP の言語を固定する。
- C: definitional / object — 各 modality の論理的挙動を固定する。
- D: definitional / object — modalities 間の強度順序と相互作用を固定する。
- E: definitional — worm という部分構文を切り出す。
- F: ambient / background — 算術的意味づけの舞台と符号化を固定する。
- G: definitional / background — 順序比較の商構造とメタ理論を固定する。
- H: ambient / object — reflection-calculus 側の言語と保存性の対象クラスを固定する。

### 3.6 condition_types

- A: 古典性
- B: 多重様相構造
- C: normality、Löb 条件、theoremhood lifting
- D: 段階づけ、inter-modal coherence
- E: 閉式・正の反復断片
- F: 算術的解釈、部分真理、効果的証明関係
- G: 同値類化、順序づけ、well-foundedness
- H: 正の反射言語、保存性、reduction

### 3.7 architecture_roles

- A: propositional consequence base
- B: graded provability
- C: intra-level derivability closure / Löb fixed-point discipline
- D: inter-level transfer / reflection-level differentiation
- E: modal iteration compression
- F: arithmetic realization
- G: ordinal coding / normal-form comparison
- H: conservation compression / progression simulation

### 3.8 core_principles_P

核心は一つの結論ではなく、次の組合せである。

1. 各 \([n]\) は GL 型の証明可能性構造を持つ。
2. interaction axioms は異なる強度レベルを一つの多重様相体系へ結合する。
3. worms は段階づけられた整合性・反射 operator の有限反復を圧縮する。
4. worms の証明論的順序が ordinal notation を与える。
5. reduction property と reflection calculus は、高い一段の反射と低い反射の反復との保存性関係を記述する。

### 3.9 blocked_escape_routes

- \(K_n\) は、含意の証明可能性を内部で modus ponens に追跡できない自由を除く。
- necessitation は、GLP の定理を各証明可能性レベルへ持ち上げない自由を除く。
- \(L_n\) は、Löb 型 fixed-point／reflection 制約を持たない normal modality への退避を除く。
- \(Mon\) は、弱いレベルでの証明を強いレベルが認識しない自由を除く。
- \(Mix\) は、低い段階の整合性主張を高い段階が安定に認識しない自由を除く。
- worm restriction は、命題変数による内容依存性を除き、反射 operator の配列そのものを比較可能にする。
- 算術解釈は「単なる抽象 modality」として意味を未固定にする余地を除くが、これは pure GLP の要件ではない。
- normal form／ordinal assignment は、同値な modal expressions を無関係な表記として扱い続ける自由を、選択した自然断片内で減らす。

### 3.10 what_fails_if_removed

- A を外す: intuitionistic GLP など別の論理へ移る。古典的双対 \(\langle n\rangle A=\neg[n]\neg A\) や標準算術解釈をそのまま移せない。
- B を一 modality に縮める: GL になり、異なる反射複雑度の相互作用と mixed worms が消える。
- \(K_n\) を外す: \([n]\) は implication-preserving normal modality でなくなり、proof predicate の標準的抽象として機能しない。
- necessitation を外す: theoremhood lifting が失われ、算術的証明可能性の基本的挙動とずれる。
- \(L_n\) を外す: polymodal \(K\) や \(K4\) 型の体系へ弱まり、Löb の反射制約と対応する順序解析を失う。
- D を外す: 独立な GL の fusion に近づき、modality index の強度順序、worm の横断比較、reduction property の基盤が失われる。
- E を外す: GLP 全体は残るが、worms による閉式の ordinal analysis は対象を失う。
- F を外す: pure modal theoremhood は残るが、\([n]\) を算術的証明可能性、\(\langle n\rangle\) を整合性／反射として読む根拠は失われる。
- G を外す: worms は構文列として残るが、同値類・ordinal rank・canonical comparison は得られない。
- H を外す: GLP は残るが、高位一段と低位反復の保存性を reflection calculus で圧縮する橋が失われる。

### 3.11 what_reappears_if_removed

- B を一 modality にする: **R1** — 証明可能性レベル間の差を区別しない自由が戻り、GL へ遷移する。
- D を外す: **R1** — modalities を独立に選ぶ自由が戻る。
- \(L_n\) を外す: **R1** — より広い polymodal frames／logics が現れる。
- E–G を外す: **R1** — arbitrary syntax presentation が戻るが、これは明示的補正項ではない。
- H を外す: **R1** — 保存性比較を個別の算術的議論へ戻す必要がある。

いずれも Stokes や Gauss–Bonnet の境界項のような R2 の明示的残差ではない。体系全体への総合判定は後述のとおり RX とする。

### 3.12 proof_resources

- representative_route: GLP の閉式断片から ordinal notation を得る標準ルート
- resources:
  - GLP の Hilbert calculus と interaction axioms
  - 算術的 provability interpretation
  - worms の GLP-provable equivalence
  - Beklemishev ordering \(<_n\)
  - well-foundedness／線形性のメタ証明
  - Beklemishev normal form
  - ordinal assignment
  - reduction property
  - reflection calculus と conservation theorem
- note: これらは GLP の「仮定」ではない。ordinal assignment や reduction property は、定義済みの体系について証明されるメタ定理である。

### 3.13 architecture_style

**段階的証明可能性圧縮型**。

これは説明用ラベルであり、新しい modal logic の分類名ではない。

### 3.14 syntax_semantics_arithmetic_comment

Pure GLP theoremhood は有限記号列の導出可能性である。arithmetical interpretation は各 \([n]\) に算術式を割り当て、GLP の定理を算術理論内の証明可能性へ移す。worm ordering と ordinal assignment はさらにその閉式断片をメタ理論から順序づける。これらを一つの「階層」と呼ぶと、modal index、operator iteration、ordinal rank、theory stage の型の違いが消える。

### 3.15 short_comment

GLP の重要性は、多数の反射原理を単に並べるのでなく、その相互作用を有限の modal calculus に圧縮する点にある。worms はその中でも内容変数を消し、operator 配列だけを ordinal analysis の対象にする。ただし、この圧縮は自然な算術解釈と保存性クラスに相対しており、任意の recursive progression を canonicalize するものではない。

## 4. assumptions_ABC の層別確認

Pure GLP の定義条件は A–D であり、worm の定義条件は E である。F は arithmetic interpretation の条件、G は ordinal-analysis side の定義、H は reflection calculus／reduction theorem の条件であって、GLP の公理へ昇格させない。この切分けにより「GLP の定理」「GLP の算術的健全性」「worm ordering の well-foundedness」「reduction property」を別々の主張として扱う。

## 5. architecture_roles の補足

graded provability は modality index の差、modal iteration は worm nesting、ordinal coding は同値類の metatheoretic rank、conservation compression は reflection calculus の役割である。四者をすべて「階層化」とだけ分類しないことが、今回の architecture analysis の中心的制約である。

## 6. 算術的解釈

主例として EA を基礎理論とし、概略

\[
[n]_T\varphi
\quad\text{を}\quad
T+\operatorname{Th}_{\Pi_n}(\mathbb N)
\text{ で }\varphi\text{ が証明可能}
\]

と読む。固定された算術階層について partial truth definition を用いるのであり、同一言語内の全算術的真理述語を仮定するのではない。添字のずれは文献の規約に依存するため、「\([n]\) は真な \(\Pi_n\) 文を補助資源とする \(n\)-provability」という採用規約を明示して使用する。

双対

\[
\langle n\rangle_T\varphi
\equiv
\neg[n]_T\neg\varphi
\]

は、理論 \(T+\varphi\) の \(n\)-consistency と読める。したがって

\[
\langle n\rangle\top
\]

は \(T\) の \(n\)-consistency を表す。標準的条件の下で、これは適切な複雑度の uniform reflection と結びつく。ただし \(\langle n\rangle\top\) は「\(n\) 番目の theory stage」ではない。

この解釈は GLP の算術的健全性・完全性を支える代表的解釈の一つであり、Japaridze の ω-rule 型解釈など別ルートもある。[Joosten](https://arxiv.org/abs/1212.2395)、[Beklemishev, provability algebras の講義](https://homepage.mi-ras.ru/~bekl/Papers/lclect-e.pdf)

## 7. Worm の定義

worm の集合 \(W\) を

\[
\top\in W,\qquad
A\in W\Longrightarrow\langle n\rangle A\in W
\]

で定める。したがって

\[
A=\langle n_k\rangle\cdots\langle n_1\rangle\top
\]

は命題変数を持たない GLP の閉式である。一般の GLP formula と worm を混同しない。

## 8. Worm の proof-theoretic 意味

算術解釈の下で、worm は \(n\)-consistency／対応する反射 operator の有限反復または混合を表す。順序は可換ではないので、

\[
\langle0\rangle\langle1\rangle\top
\quad\text{と}\quad
\langle1\rangle\langle0\rangle\top
\]

を単なる「二段階」として同一視できない。各 operator がどの理論を引数に取るか、interaction axioms によってどの式へ正規化されるかが strength を左右する。

## 9. Beklemishev ordering

適切な worm class \(W_n\)（現れる modality がすべて \(n\) 以上）について

\[
A<_n B
\quad:\Longleftrightarrow\quad
\mathrm{GLP}_\omega\vdash B\to\langle n\rangle A
\]

とする。この関係は provable equivalence 上で定義される。特に \(<_0\) は \(\mathrm{GLP}_\omega\) の worms の同値類を well-order し、その順序型は \(\varepsilon_0\) である。worm は構文、\(\varepsilon_0\) は同値類順序のメタ理論的 order type であり、両者は同一の対象ではない。[Joosten](https://arxiv.org/abs/1212.2395)

Transfinite \(\mathrm{GLP}_\Lambda\) では modalities 自体を ordinal まで拡張し、一般化された worm order \(o_\xi\) を hyperations／cohyperations で計算する。これは \(\mathrm{GLP}_\omega\) での \(\varepsilon_0\) だけを普遍化した単純な「worm = ordinal」図式ではない。[Fernández-Duque & Joosten](https://arxiv.org/abs/1212.3468)

## 10. Worms と ordinal notation

### 10.1 well-order と order type

\(\mathrm{GLP}_\omega\) の closed worm fragment を provable equivalence で割り、\(<_0\) で順序づけると \(\varepsilon_0\) の notation system が得られる。有限文字列で無限順序数を表す点は通常の ordinal notation と共通するが、その順序は GLP theoremhood により内在的に定義される。

### 10.2 normal form

選択した Beklemishev normal form では、各 worm 同値類に正規代表を与え、順序比較を計算可能な構文操作へ落とす。従って、完全な ordinal assignment \(o\) を同値類上の order-isomorphism として固定すれば、

\[
o(A)=o(B)
\]

は \(A\) と \(B\) の GLP-provable equivalence に対応する。異なる文字列が同じ同値類を表すことはあるが、normal form はその表示冗長性を除く。

ただしこの一意性は GLP／worm の選択した fragment 内の一意性である。任意の recursive ordinal notation \(a,b\) について

\[
|a|=|b|\Longrightarrow T_a=T_b
\]

を保証しない。

### 10.3 大きな体系

\(\mathrm{GLP}_\omega\) の全 worm 順序の標準的到達点は \(\varepsilon_0\) である。transfinite modalities や強い reflection calculi では hyperexponentials、Veblen 型進行、より大きい ordinal notation が現れる。どの順序数まで表現できるかは modality set、ordering、arithmetical interpretation に依存する。

## 11. Ordinal notation canonicalization stress test

### Q1. 同じ worm order type を持つ distinct worms は同値か

採用した完全な ordinal assignment が GLP 同値類から ordinal への order-isomorphism なら、同じ値は同じ GLP 同値類を表す。文字列として同一とは限らない。

### Q2. normal form はどの意味で unique か

選択した closed fragment と GLP-provable equivalence に相対して一意である。Reflection calculus の拡張では、variable-free formulas に fat／thin normal forms があり、thin normal form は constituent worms の同値を除いて一意となる。[Beklemishev, Reflection calculus and conservativity spectra](https://arxiv.org/abs/1703.09314)

### Q3. arbitrary recursive notation の presentation dependence を除去するか

除去しない。worm normal form は一つの自然な modal notation system を canonicalize するだけで、任意の notation system の path dependence や、その notation に沿って定義された theory progression の差を消さない。

### Q4. 適用範囲

自然な consistency／reflection progressions のうち、GLP または reflection calculus の算術解釈と保存定理で捉えられる範囲では強い canonicalization が得られる。Feferman 型の任意の recursive progression 全般には及ばない。

**判定: C2。** natural reflection progressions の proof-theoretic equivalence／conservation class をかなり canonical に表現するが、C3 の一般性はない。

## 12. Turing–Feferman progression との対応

| Turing–Feferman side | GLP / worm side |
|---|---|
| \(T_a\) | 算術解釈を介して worm／正の formula が表す theory extension。pure syntax だけでは特定の \(T_a\) ではない |
| consistency operator | \(A\mapsto\langle0\rangle A\)、または一般に \(A\mapsto\langle n\rangle A\) の \(n\)-consistency 解釈 |
| reflection operator | 適切な \(\langle n\rangle\) の uniform-reflection 解釈、または reflection calculus の modality |
| successor stage | 限定された自然 progression では modality の前置に対応。任意の successor clause とは対応しない |
| mixed reflection step | mixed worm \(\langle n_k\rangle\cdots\langle n_1\rangle\top\) |
| ordinal notation | worm normal form と \(o(A)\)。Turing notation \(a\) そのものではない |
| limit behavior | worm rank の supremum／fundamental sequence。有限 worm に theory union の直接表現はない |
| conservation relation | reduction property、Schmerl formulas、reflection calculus の導出関係 |
| proof-theoretic strength | worm order／conservativity spectrum が与える complexity-relative measure |

この対応は「Turing progression 全体 = GLP」とする同型ではない。GLP は自然な反射 operator の代数を抽象化し、特定の consequence class 上で progression を圧縮する。

## 13. Successor stage と worm concatenation

Turing progression の

\[
T_{a+1}=T_a+\operatorname{Con}(T_a)
\]

に対し、算術解釈された

\[
A\longmapsto\langle n\rangle A
\]

は、「\(A\) が表す extension に \(n\)-consistency／対応する reflection を適用する」という自然な一段を表す。この限定範囲では prefixing は operator application を正確に符号化する。

しかし次の三点で一般の successor stage とは異なる。

1. \(n\) は stage 数ではなく operator の複雑度である。
2. \(\langle n\rangle A\) の ordinal rank は一般に \(o(A)+1\) とは限らず、高い \(n\) は指数関数的・Veblen 型の跳躍を生む。
3. arbitrary recursive extension operator \(F\) は GLP の一 modality に対応するとは限らない。

**判定: W2（natural reflection progression に限定）。** GLP の標準算術解釈に沿う自然な consistency／reflection progression は正確に符号化できるが、arbitrary progression を一般に表す W3 ではない。

## 14. Limit stage

有限 worm には

\[
T_\lambda=\bigcup_{\beta<\lambda}T_\beta
\]

という literal infinite union は存在しない。区別すべきものは次である。

- worm sequence: 有限式の外部列
- ordinal supremum: 各 worm rank の上限
- fundamental sequence: limit ordinal への計算可能な近似
- reflection theory union: 公理集合の外部和
- modal normal form: 一つの有限式の同値代表

Reduction property の \(Q_n^k(A)\) 列は高位 modality の一種の fundamental sequence として働くが、有限 worm 一個が limit theory の全公理和になるわけではない。したがって ordinal assignment の limit と progression の limit union は同一でない。

## 15. Reduction property

代表的な標準形として

\[
Q_n^0(A):=\langle n\rangle A,\qquad
Q_n^{k+1}(A):=\langle n\rangle(A\land Q_n^k(A))
\]

と置く。EA 上の適切な算術解釈では

\[
\mathrm{EA}+\langle n+1\rangle A
\]

は

\[
\mathrm{EA}+\{Q_n^k(A):k<\omega\}
\]

に対して \(\Pi_{n+1}\)-conservative である、という reduction theorem が得られる。添字と consequence class は採用規約に依存するため、この版に固定する。[Joosten, Theorem 3.10](https://arxiv.org/abs/1212.2395)

意味は次の三点である。

1. 「高い一段」は、適切な低複雑度 consequences に関して「低い operator の ω 回反復」に還元できる。
2. これは theory equality ではなく、指定された式クラスについての conservation である。
3. stage 数、modality index、proof-theoretic strength は一軸でない。

この定理は「moving boundary」より精密であり、何が保存され、どの consequence class で比較されるかを明示する。

## 16. Schmerl formulas・reflection calculus・conservation

Reflection Calculus RC は、\(\top\)、命題変数、\(\land\)、positive modalities からなる strictly positive fragment で、modalities を uniform reflection principles として解釈する。変数なし fragment の worms／normal forms は、反射原理の反復と保存性を計算するための代数的記法になる。

Schmerl formulas は、異なる反射複雑度と反復長の組合せを変換し、mixed progressions 間の conservation spectra を記述する。RC の拡張 \(RC^\nabla\) では、理論の \(\Pi_{n+1}\)-fragment を取る operator も表現し、variable-free normal forms が複雑度ごとの保存性スペクトルを canonical に記録する。[Beklemishev](https://arxiv.org/abs/1703.09314)

従って P2 の「proof architecture」が捉えていたものの大部分は、標準的には provability algebra、reflection calculus、Schmerl formulas、conservativity spectrum として既に精密化されている。

## 17. M2 moving boundary の再検査

Turing–Feferman progression の

\[
T_{a+1}\vdash\operatorname{Con}(T_a),\qquad
T_{a+1}\nvdash\operatorname{Con}(T_{a+1})
\]

は stage-relative provability の index shift である。GLP の

\[
[n]\quad\text{対}\quad[n+1]
\]

は通常、同じ shift ではなく、証明可能性の複雑度・反射強度の差である。反復 stage はむしろ worm nesting に表れる。

したがって「moving boundary」は、旧 theory を次の extension から評価する progression の説明には使えるが、modality-index hierarchy まで一括すると二種類の index を潰す。

**再判定: M2\*.** stage-relative reindexing を横断比較する限定ラベルとして有効だが、modality index と stage index を一つの moving boundary と呼ぶと破綻する。

## 18. A2 subject theory / extension theory 非対称性の再検査

算術解釈の下では

\[
\langle n\rangle A
\]

は \(T+A\) の \(n\)-consistency と読め、operator を適用する metatheoretic base／extension と、operator 内で対象化される theory を区別できる。ここには「どの proof predicate が対象か」という typing が残る。

しかし pure GLP の式 \(\langle n\rangle A\) は、単独では特定の subject theory \(T_a\) と extension theory \(T_{a+1}\) を名指さない。その区別は arithmetical realization を入れたときに回復される。

**再判定: A2\*.** 算術解釈下では consistency／reflection progressions を横断する安定した非対称性だが、pure modal syntax だけには subject/extension の理論名は保存されない。

## 19. P2「証明デザイン」の再検査

GLP では

\[
\text{modalities}
+\text{interaction axioms}
+\text{worm syntax}
+\text{normal forms}
+\text{ordinal ordering}
+\text{arithmetical interpretation}
\]

が、どの反射反復を区別し、どの保存性クラスで同一視するかを決める。この意味で

\[
\text{theorem anatomy}
\to
\text{logic anatomy}
\to
\text{progression anatomy}
\to
\text{algebra／normal-form anatomy}
\]

という比較枠は成立する。

ただし標準理論では、これを provability algebra、positive fragment、reflection calculus、ordinal analysis としてより精密に扱う。

**再判定: P2。** architecture comparison として有効だが、新しい proof-theoretic framework である P3 ではない。

## 20. 「固定する側／固定される側」の言い換えテスト

独自語彙なしでは次のように言える。

- \([n]_T\) は固定した theory \(T\) と複雑度 \(n\) に相対する provability predicate である。
- \(\langle n\rangle_T A\) は \(T+A\) の \(n\)-consistency を表す。
- worm nesting はこれらの operator composition を表す。
- GLP interaction axioms は異なる \(n\) の provability predicates の関係を表す。
- ordinal assignment は worm 同値類の well-order rank である。

この標準記述で technical content は尽くされる。A2\* は文書横断の比較ラベルとしてのみ残る。

## 21. Residual RX の再検査

weaker modality、stronger reflection step、worm tail、ordinal remainder、modal non-theorem、stronger theory は互いに異なる対象である。「残差」と一括すると、syntax、theory extension、ordinal arithmetic、non-derivability を混同する。

**判定: RX — residual vocabulary not useful here.** GLP では normal form、counterexample、conservation remainder、next reflection stage をそれぞれ標準語彙で分離すべきである。

## 22. Erasure Test

「moving boundary」「固定する側／固定される側」「証明デザイン」「残差」「閉包」「再入力」を削除しても、GLP、modalities、worms、Beklemishev ordering、normal forms、arithmetical interpretation、ordinal assignment、reduction property、conservation、reflection calculus だけで数学的差分はすべて記述できる。

失われるのは、既存文書の theorem anatomy・logic anatomy・progression anatomy を同じ比較表へ置く教育的見通しだけである。

**判定: E1。** 技術情報は失われず、横断的な見通しだけが少し失われる。

## 23. Canonicalization 仮説の判定

Worm normal form と ordinal assignment は、GLP／RC が表す natural reflection fragment の表示冗長性を大幅に除く。一方で、この canonicalization は arithmetic interpretation、provable equivalence、conservation class に相対しており、任意の recursive theory progression の同一性を決めない。従って第11節の判定どおり **C2** とし、C3 は棄却する。

## 24. Ordinal value と theory strength の分離

| object | type | canonical? | arithmetic meaning | strength meaning |
|---|---|---|---|---|
| worm | modal syntax | 文字列としては非一意 | iterated/mixed \(n\)-consistency | operator 配列が strength を提示 |
| worm normal form | modal syntax の正規代表 | 選択した fragment と同値関係に相対して一意 | 同じ算術的 reflection content の標準表示 | conservation/equivalence class の比較を容易化 |
| ordinal assignment \(o(A)\) | metatheoretic rank | worm 同値類上で canonical | 直接には算術文でない | \(<_0\) に関する相対 strength rank |
| modality index \(n\) | modal syntax の level | GLP の signature 内で固定 | \(n\)-provability／反射複雑度 | stage 長でなく operator の種類 |
| Turing notation \(a\) | recursive presentation | 一般に非 canonical | progression の effective stage code | operator・path・notation system に依存 |
| theory stage \(T_a\) | formal theory | progression 定義に相対 | 公理・定理の集合 | deductive、reflection、conservation、ordinal strength は別々 |

## 25. 研究ログとの比較

研究ログ側には、scope の拡張、self-application、level shift、局所化という記述がある。GLP 側には、複数の provability levels、reflection operator の composition、ordinal ordering、normal forms、conservation theoremsという形式構造がある。

しかし研究ログ側に \([n]\) の算術的解釈、interaction axioms、worm ordering、reduction property に対応する形式写像はまだない。

**判定: Q1。** scope／level architecture の限定的な構造類似に留まり、Q2・Q3 を支持しない。

## 26. 最終比較表

| structure | index type | operator | iteration representation | limit representation | ordinal connection | canonicality |
|---|---|---|---|---|---|---|
| Gödel II | 固定 theory \(T\) | \(\operatorname{Con}(T)\) | 本体には反復なし | なし | 間接的 | 文の形式化に相対 |
| Löb | 固定 \(T,\varphi\) | \(\Pr_T\) と local reflection | fixed point 内の provability nesting | なし | 直接なし | provability predicate に相対 |
| GL | 一つの modality | \(\Box,\Diamond\) | modal nesting | 有限式には直接なし | fixed-point／frame analysis、単独では progression ordinal でない | logic と同値関係に相対 |
| GLP | modality index \(n\) | \([n],\langle n\rangle\) | mixed modal nesting | pure finite syntaxには直接なし | closed fragment の worms を介する | Hilbert system は固定、stage theory は interpretation-dependent |
| worms | modality 列の位置と値 | prefix \(\langle n\rangle\) | finite word | 外部列、supremum、fundamental sequence | \(\mathrm{GLP}_\omega\) の \(<_0\) は \(\varepsilon_0\) | normal form は GLP 同値類に相対して高い |
| Turing progression | recursive notation \(a\) | consistency／chosen recursive operator | transfinite recursion | theory union | notation system と ordinal analysis | 一般に presentation-sensitive |
| uniform reflection progression | stage notation \(a\) と formula class \(\Gamma\) | \(\mathrm{RFN}_\Gamma\) | transfinite operator iteration | theory union | operator と class に相対 | 一般には非 canonical、自然断片を GLP/RC が圧縮 |

## 27. Kill criteria の査定

1. moving boundary は modality／stage reindexing の言い換えだけではなく比較上の注意喚起にはなるが、両者を一括すると誤る。よって M2\*。
2. subject／extension asymmetry は pure modal syntax だけでは消える。よって A2\*。
3. worms と normal forms は自然な reflection architecture を標準的に十分圧縮する。独自語彙は降格。
4. reduction property は「高い一段対低い多段」を consequence class 付きで精密に記述する。moving-boundary 比喩より優先。
5. ordinal assignment は natural fragment を canonicalize するが、arbitrary recursive progression まではしない。よって C2。
6. residual vocabulary は対象型を混同する。よって RX。
7. proof design は provability algebra／reflection calculus の言い換え以上の形式的不変量をまだ与えない。P2 に留める。

## 28. 最終出力

### A. GLP の核心

- GLP は複数の GL 型 provability modalities と、その強度間 interaction を一体系へ統合する。
- modality index は theory stage ではなく、標準解釈では provability／reflection の複雑度を表す。
- 算術的内容は interpretation により与えられ、pure modal validity と区別される。
- closed fragment は worms を通じて ordinal analysis と接続する。

### B. Worm の核心

- worm は \(\top\) に dual modalities を有限回前置した closed formula である。
- 算術解釈では graded consistency／reflection operators の反復を表す。
- nesting の順序が重要で、単なる「段数」では strength を決められない。
- GLP 同値類上の Beklemishev ordering が \(\mathrm{GLP}_\omega\) では \(\varepsilon_0\) を与える。

### C. GL から GLP への最大の変化

1. 一つの provability から、複雑度で段階づけられた複数の provability へ移る。
2. 各 modality 内の Löb 構造に、inter-modal interaction が加わる。
3. 単一 operator の反復から mixed reflection operators の代数へ移る。
4. worms と conservation calculus により ordinal analysis が直接化する。
5. modality index と iteration depth という二軸が分離される。

### D. Turing–Feferman progression との対応

1. worm prefix は natural graded consistency／reflection operator の一回適用に対応する。
2. worm nesting は有限の mixed progression を圧縮する。
3. modality index は Turing stage index ではない。
4. finite worm は limit theory union を直接表さない。
5. GLP/RC は自然な progression の conservation class を canonicalize するが、任意の recursive progression は覆わない。

### E. Reduction property の意味

1. 高い reflection operator 一回を、低い operator の \(\omega\)-反復へ還元する。
2. 還元は指定した算術階層についての conservation であり、theory equality ではない。
3. strength が「stage 数」一軸でないことを示す。

### F. moving boundary 再判定

**M2\*** — stage-relative reindexingには有効だが、modality-index hierarchy と一括すると壊れる。

### G. subject / extension asymmetry 再判定

**A2\*** — arithmetic interpretation 下では安定するが、pure GLP syntax では subject theory の区別が消える。

### H. proof design 再判定

**P2** — theorem／logic／progression／algebraを比較する architecture 枠として有効。ただし標準 provability algebra の代替ではない。

### I. canonicalization 判定

**C2** — natural reflection progressions の同値・保存性クラスを normal form と ordinal assignment でかなり canonical に表す。arbitrary progressions には及ばない。

### J. residual 判定

**RX** — residual vocabulary はこの抽象度では有用でない。

### K. Erasure Test

**E1** — 技術内容はすべて標準語彙で保存され、失われるのは教育的な横断比較だけである。

### L. 研究ログとの類似

**Q1** — scope／level architecture の構造類似のみ。modal／ordinal mapping は未構成である。

### M. 最も重要な新規観察

1. stage index、modality index、worm nesting、ordinal rank は別々の型を持ち、「階層」の一語では扱えない。
2. reduction property は「高い一段」と「低い多段」を conservation class に相対して交換し、stage 数と strength の単純対応を否定する。
3. GLP／worms は自然な reflection architecture をかなり canonicalize するため、独自比較語彙は新理論ではなく説明用索引へさらに降格する。

### N. 次の一手

1. **consistency vs uniform reflection progression comparison** — 同じ worm／ordinal がどの consequence class で異なる progression operators を表すかを直接比較できる。
2. **reflection calculus / Schmerl formulas** — C2 canonicalization の正確な範囲を conservation spectra と normal forms で検証できる。
3. **proof-theoretic ordinal anatomy** — ordinal value、conservation strength、full deductive strength の非一致を体系横断で分解できる。

## 29. 総括

今回の stress test の negative result は明確である。Turing–Feferman progression で比較語として残った M2、A2、P2 のうち、GLP／worms によって標準化されるのは主に reflection operators の段階差、有限反復、保存性順序、natural ordinal notation である。M2 と A2 はそれぞれ M2\*、A2\* へ限定され、P2 は比較枠として残るが、技術的内容は provability algebra と reflection calculus に吸収される。

したがって、GLP は「moving boundary」の形式化そのものではない。より正確には、自然な graded reflection progressions の一部を modal syntax、normal forms、ordinal ordering、reduction theorems により圧縮する既存の標準理論である。その範囲では独自語彙を消しても数学は失われず、今回の語彙の役割は異なる分析文書間の型違いを警告する比較的・教育的索引に限られる。

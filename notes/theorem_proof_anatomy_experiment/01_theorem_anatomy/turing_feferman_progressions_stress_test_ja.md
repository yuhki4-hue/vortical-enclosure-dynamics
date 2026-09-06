# Turing–Feferman progressions：証明の解剖 special stress test

## 0. 目的と参照枠

本稿は、通常21定理、Gödel、Tarski、Löb、GL、reflection principles の stress test を継承し、Turing–Feferman progressions / transfinite recursive progressions of theories を **stage-indexed proof-theoretic architecture** として分析する。

「閉包」「残差」「moving boundary」「固定」「外部化」「証明デザイン」「段階化」は比較用のメタ記述であり、標準 proof theory の用語ではない。技術記述では Turing progression、iterated consistency、iterated reflection、recursive ordinal notation、successor / limit stage、conservation、proof-theoretic ordinal、ordinal analysis を優先する。

今回の中心問題は、

\[
T\vdash \mathrm{Con}(T)
\]

という same-theory claim と、外部から

\[
T^+=T+\mathrm{Con}(T)
\]

を構成することの差が、transfinite recursion の各段階でどのように index 化されるかである。

# 1. 用語と歴史的範囲の固定

## 1.1 現代的 Turing progression

現代文献で **Turing progression** と呼ばれる代表形は、基礎理論 \(T\) から consistency を反復する列である。

\[
T^0=T,
\qquad
T^{\alpha+1}=T^\alpha+\mathrm{Con}(T^\alpha),
\qquad
T^\lambda=\bigcup_{\beta<\lambda}T^\beta.
\]

ただし、これは actual ordinals だけで書いた metatheoretic 略記である。各 \(T^\alpha\) を計算可能に公理化された理論として扱うには、後述する recursive ordinal notation と、各 stage の axiom predicate の一様な構成が必要になる。

歴史的 Turing (1939) の ordinal logics は、この現代的略式の「consistencyだけの単純反復」と完全に同一ではない。Turing は constructive ordinal notations に沿う logics と、local reflection に近い強化も扱った。本稿では歴史的由来と現代的用語法を区別する。

## 1.2 Feferman-style recursive progression

Feferman-style progression は、recursive notation \(a\) ごとに c.e. theory \(T_a\) を一様に割り当て、successor で指定した extension operator を作用させ、limit で有効に与えられた先行列を集約する一般構成である。operator は consistency に限らず、local / uniform reflection や、別の recursive extension operator でもよい。

したがって「Feferman progression」は一つの固定列ではなく、少なくとも次に相対する。

- base theory
- ordinal notation system と notation path / presentation
- successor operator
- limit rule
- formula class
- stage theory の axiom presentation

## 1.3 Reflection progression

formula class \(\Gamma\) を固定する reflection progression の代表形は、

\[
T^0=T,
\qquad
T^{\alpha+1}=T^\alpha+\mathrm{RFN}_\Gamma(T^\alpha),
\qquad
T^\lambda=\bigcup_{\beta<\lambda}T^\beta.
\]

local reflection \(\mathrm{Rfn}_\Gamma\) を使う版と uniform reflection \(\mathrm{RFN}_\Gamma\) を使う版は区別する。consistency は \(\bot\) に対する single local reflection なので、consistency progression は reflection family の特殊な progression と比較できるが、full uniform reflection iteration と同じ強さではない。

## 1.4 主分析の採用版

主分析には、**standard provability predicate に基づく notation-indexed iterated consistency progression** を採用する。

- base \(B=EA\) または必要に応じて \(I\Sigma_1\)
- \(T_0=T\supseteq B\): 整合的で計算可能に公理化された古典一階算術理論
- \(\mathcal O^\ast\): 0・successor・effective limit constructors を持つ effective ordinal notation system
- \(a\in\mathcal O^\ast\): stage を指定する notation
- \(\mathrm{Pr}_{T_a}(x)\): \(a\) に一様な stage-provability predicate
- successor operator \(F(S)=S+\mathrm{Con}(S)\)

reflection progression、Feferman completeness、autonomous progression は比較節で扱う。最弱条件の同定は目的としない。

ここで “effective” は、notation constructors と選択した predecessor / limit presentation を計算可能に操作できるという意味である。notation 全体への membership が decidable だとは仮定しない。Kleene の \(\mathcal O\) を使う場合、\(a\in\mathcal O\) の判定自体は効果的でない。

# 2. Actual ordinal と ordinal notation

## 2.1 二つの index

actual ordinal を \(\alpha,\beta,\lambda\)、有限な記号・自然数 code としての notation を \(a,b,c\) と書く。notation \(a\) が ordinal \(\alpha\) を表すとき、

\[
|a|=\alpha
\]

と書く。

ordinal \(\alpha\) は外延的な順序型である。一方 notation \(a\) は、successor predecessor や limit fundamental sequence を計算可能に提示する **intensional data** である。recursive progression が直接入力として使うのは \(\alpha\) そのものではなく \(a\) とその presentation である。

## 2.2 Notation-indexed recursion

記法 constructors を概略

\[
0_{\mathcal O},\qquad s(a),\qquad \ell(e)
\]

とする。\(\ell(e)\) は、partial recursive function \(\varphi_e\) が与える増大列

\[
\varphi_e(0)<_{\mathcal O^\ast}
\varphi_e(1)<_{\mathcal O^\ast}\cdots
\]

の limit notation である。主 progression は一様な c.e. axiom presentations を使って

\[
T_{0_{\mathcal O}}=T,
\]

\[
T_{s(a)}=T_a+\mathrm{Con}(T_a),
\]

\[
T_{\ell(e)}=\bigcup_{n<\omega}T_{\varphi_e(n)}
\]

と定める。recursion theorem / effective transfinite recursion により、\(a\mapsto\)「\(T_a\) の axiom predicate」の一様な fixed-point construction を行う。

## 2.3 同じ ordinal、異なる notation

\(|a|=|b|\) でも、一般には \(a\) と \(b\) が同じ predecessor path、同じ fundamental sequence、同じ c.e. axiom presentation を与えるとは限らない。そのため unrestricted recursive progressions では、

\[
|a|=|b|
\quad\not\Rightarrow\quad
T_a=T_b
\]

であり、deductive equivalence さえ自動的ではない。

これは単なる表記上の冗長性ではない。Turing 型 completeness results では、真な文 \(\sigma\) に応じて同じ order type を持つ特別な computable presentation を組み、その presentation に \(\sigma\) の情報を埋め込める。従って「必要な ordinal length」だけを文の強さとみなすと、path / presentation dependence を見落とす。

自然な正規記法系、well-behaved progression、適切な invariance theorem のもとでは order type による安定した strength calibration が可能な場合がある。しかしそれは追加結果であり、recursive notation 一般からは従わない。

## 2.4 Well-foundedness の位置

\(a\in\mathcal O^\ast\) であること、すなわち notation が本当に well-founded ordinal presentation を与えることは、通常 metatheory 側で判定・仮定される。自然数 code \(a\) に対し stage axiom predicate を形式的に生成できても、\(a\) が不正な pseudo-notation なら soundness や consistency は保証されず、構成によっては \(T_a\) が矛盾する。

したがって、

- stage theory の syntactic generation
- notation の genuine well-foundedness
- stage theory の consistency / soundness

は別の主張である。

# 3. 通常15項目による progression anatomy

1. **system_name:** Notation-indexed Turing consistency progression（reflection / Feferman progressions を比較対象とする）

2. **domain:** proof theory・metamathematics・recursive ordinal notation theory・ordinal analysis・provability logic

3. **standard_definition:** \(T_0=T\)、successor notation で \(T_{s(a)}=T_a+\mathrm{Con}(T_a)\)、effective limit notation で \(T_{\ell(e)}=\bigcup_nT_{\varphi_e(n)}\) とする一様な c.e. theory progression。actual ordinal 添字は notation-indexed definition の略記に限る。

4. **assumptions_ABC:**
   - A: base theory \(B\) と出発理論 \(T_0=T\supseteq B\)
   - B: progression operator \(F(S)=S+\mathrm{Con}(S)\)
   - C: 各 stage presentation に対応する標準 proof / provability predicate
   - D: recursive ordinal notation system \(\mathcal O^\ast\) と effective relation / constructors
   - E: successor-stage clause
   - F: limit-stage clauseと、limit notation が与える effective cofinal sequence
   - G: \(a\mapsto T_a\) の一様な c.e. presentation / effectiveness
   - H: notation の well-foundedness、stage consistency、conservation を判定する metatheory
   - I: reflection progression 比較時の formula class \(\Gamma\) と local / uniform の選択
   - J: stage theories とその proof predicates の Gödel coding

5. **hypothesis_levels:**
   - A: ambient＋object。formalization base と最初の対象理論
   - B: definitional＋object。何を一段の strength increase とするかを固定
   - C: definitional＋object。stage-relative theoremhood の presentation
   - D: ambient＋definitional。transfinite recursion の有効な index space
   - E: definitional。successor transition
   - F: definitional＋ambient。limit aggregation の計算可能な提示
   - G: object＋definitional。各 \(T_a\) を formal theory に保つ条件
   - H: background。internal stage axiom ではない
   - I: definitional。reflection operator の scope / complexity
   - J: background＋definitional。syntax-to-number coding と stage reindexing

   stage index \(a\) は theory の性質ではなく、notation system 内の object-level code である。actual ordinal \(|a|\) はその code に対する metatheoretic interpretation である。

6. **condition_types:**
   - A: 基礎算術・初期理論
   - B: recursive extension operator
   - C: provability coding
   - D: ordinal notation・effective ordering
   - E: successor recursion
   - F: limit union・fundamental sequence
   - G: effective axiomatizability
   - H: well-foundedness / soundness metatheory
   - I: formula-class restriction・reflection scope
   - J: uniform syntactic coding

7. **architecture_roles:**
   - A: base fixation
   - B: successor strengthening
   - C: stage-relative provability
   - D: ordinal control
   - E: consistency transfer
   - F: limit aggregation
   - G: recursion control
   - H: external validation
   - I: strength calibration
   - J: proof-predicate reindexing

8. **stage_transition_P:** valid notation \(a\) と指定 operator に対し、\(T_{s(a)}\) は旧 stage \(T_a\) の consistency を証明する c.e. extension となる。limit notation では、指定された先行 stages の axioms を一様に集約した c.e. theory が得られる。適切な consistency / soundness 条件のもとで progression は increasing だが、各 successor が自身の consistency を得るわけではない。

9. **blocked_escape_routes:**
   - A: starting strength と coding capacity の未指定を防ぐ
   - B: 「強化」の意味を consistency / reflection / arbitrary truth addition の間で漂わせない
   - C: \(\mathrm{Con}(T_a)\) がどの axiom presentation の非矛盾性かという自由度を固定する
   - D: actual ordinal を直接 algorithm の入力にしたふりをする逃げ道を塞ぐ
   - E: next stage が旧 stage のどの statement を採用するかを固定する
   - F: limit で任意の追加公理を忍び込ませる自由度を塞ぎ、先行列の effective union に限定する
   - G: stage theories が非効果的な truth sets へ変質する道を塞ぐ
   - H: syntactic recursion と genuine well-founded / sound progression の混同を防ぐ
   - I: consistency と local / uniform reflection の強さを一括する逃げ道を塞ぐ
   - J: successor ごとに provability predicate の subject theory を曖昧にする道を塞ぐ

10. **what_fails_if_removed:**
   - Aを外す: progression の初期強度と coding capacity が不定になる。同じ operator でも異なる base から異なる hierarchy が生じる
   - Bを外す: successor theory が定まらず、単なる increasing chain 一般へ戻る
   - Cを外す: \(\mathrm{Con}(T_a)\) の標準的意味が定まらない。人工的 predicate では Gödel II / Löb 接続が壊れ得る
   - Dを外す: finite syntax で transfinite stages を一様に指定できない。actual ordinalだけでは c.e. stage theoryを生成できない
   - Eを外す: successor で strength を増す規則が消える
   - Fを外す: limit stage が未定義になり、finite / successor recursion で停止するか、恣意的 limit extension になる
   - Gを外す: stage が非-c.e. theory になり得て、標準 proof predicate と Gödel II の適用枠が失われる
   - Hを外す: pseudo-notation と genuine notation、formal generation と soundnessを区別できない
   - Iを外す: reflection progression の比較対象が不定。operator strengthを一軸化できない
   - Jを外す: \(\mathrm{Pr}_{T_a}\) を次 stage で算術化できず、iteration の定式化が壊れる

11. **what_reappears_if_removed:**
   - A: **R1** — base-theory dependence と異なる初期 strength
   - B: **R1** — arbitrary recursive extension operators の選択自由度
   - C: **R1** — provability-predicate / presentation dependence
   - D: **R0/R1** — effective transfinite framework 自体は失われる（R0）。非効果的 ordinal-indexed hierarchy を許せば別構造へ移る（R1）
   - E: **R0** — strengthening clause が消えるだけで自然な補正項はない
   - F: **R1** — limit theory の選択自由度、または progression の successor-only 化
   - G: **R1** — non-c.e. axiom sets、semantic truth unions、標準 incompleteness hypotheses の喪失
   - H: **R1** — ill-founded paths、inconsistent pseudo-stages、未証明の soundness assumptions
   - I: **R1** — consistency / local / uniform / complexity-indexed operators の非同値な選択肢
   - J: **R0** — stage-relative consistency statement の形成自体が不能

   いずれも Stokes / Gauss–Bonnet 型の明示的補正項ではなく、主に architecture choice の再出現である。

12. **proof_resources:**
   - representative_route: notation-indexed effective recursion と metatheoretic induction
   - resources:
     - Gödel numbering と一様な proof-predicate construction
     - Kleene recursion theorem / fixed-point construction
     - recursive ordinal notations と effective limit sequences
     - transfinite induction in the metatheory
     - Gödel 第2不完全性定理
     - Hilbert–Bernays–Löb derivability conditions
     - reflection / conservation theorems
     - GL / GLP、reflection calculus（対応分析時）
   - note: これらは progression の定義条件と、その soundness・strictness・completeness・ordinal strength を証明する資源を区別した一覧である。notation の well-foundedness を proof resource だけで自動取得するわけではない

13. **architecture_style:** notation-indexed recursive strengthening／stage-relative reflection progression

14. **system_vs_metatheory_comment:** progression が固定するのは、base、stage axiom presentation、extension operator、notation constructors、successor / limit rulesである。metatheory は notation の well-foundedness、stage soundness、strictness、conservation、ordinal calibration を証明する。同じ \(T_a\) 内で \(\mathrm{Con}(T_a)\) を証明することと、metatheory がそれを \(T_{s(a)}\) の axiom に選ぶことを混同すると、progression の index shift が消える。

15. **short_comment:** Turing–Feferman progression は「不完全性を消す単一極限理論」ではなく、stage-relative provability を recursive notation に沿って更新する architecture である。strength は ordinal lengthだけでなく、base、operator、formula class、presentation、測定する consequence class に依存する。

# 4. Successor stage の解剖

## 4.1 Subject theory

主 progression では

\[
T_{s(a)}=T_a+\mathrm{Con}(T_a)
\]

であり、追加文は

\[
\mathrm{Con}(T_a)\equiv
\neg\mathrm{Pr}_{T_a}(\ulcorner\bot\urcorner)
\]

である。ここで参照されるのは \(\mathrm{Pr}_{T_a}\) であり、\(\mathrm{Pr}_{T_{s(a)}}\) ではない。

reflection progression でも同様に、

\[
T_{s(a)}
=
T_a+\mathrm{RFN}_\Gamma(T_a)
\]

の reflection axioms は \(T_a\)-proofs を対象にする。new theory の proof predicate へ無断で置換してはならない。

## 4.2 Same-theory と next-theory

外部で \(T_a\) が整合的で、Gödel II の通常条件を満たすなら、

\[
T_a\nvdash\mathrm{Con}(T_a).
\]

一方、definition により

\[
T_{s(a)}\vdash\mathrm{Con}(T_a).
\]

この二式は矛盾しない。証明主体が \(T_a\) から \(T_{s(a)}\) へ変わっているからである。successor operation は \(T_a\) の内部能力ではなく、metatheory が旧 stage の consistency statement を新 stage の axiom として選ぶ construction である。

## 4.3 Reindexing された新しい制約

\(T_{s(a)}\) が十分強く整合的なら、Gödel II は新しい predicate に対して

\[
T_{s(a)}\nvdash\mathrm{Con}(T_{s(a)})
\]

を与える。旧 statement \(\mathrm{Con}(T_a)\) は処理されたが、\(\mathrm{Con}(T_{s(a)})\) は同じ文の「残り」ではない。subject theory が更新された別の arithmetical sentence である。

# 5. Limit stage の解剖

## 5.1 Union の意味

limit notation \(\ell(e)\) が effective cofinal sequence \(a_n=\varphi_e(n)\) を与えるとき、

\[
T_{\ell(e)}
=
\bigcup_{n<\omega}T_{a_n}.
\]

これは各先行 theory の axioms を一つの stage presentationへまとめる操作である。limit に固有の新しい consistency / reflection axiomを一個追加するのではない。

## 5.2 Effectiveness

\(n\mapsto a_n\) が computable で、\(a\mapsto\mathrm{Ax}_{T_a}(x)\) が一様に c.e. なら、pairs \((n,x)\) を dovetail することで union axioms を c.e. に列挙できる。従って \(T_{\ell(e)}\) に標準 proof predicate を再び割り当てられる。

これに対し、「全ての真の ordinal notations に対応する theories の union」は、個々の effective limit stage と別物である。Kleene の \(\mathcal O\) 全体への membership は効果的に判定できず、その総 union は一般に一つの c.e. formal theory ではない。

## 5.3 Successor との質的差

- successor: 一つ前の stage を subject とする新 axiom / schema を加える
- limit: notation に組み込まれた先行 presentation を effective union する
- limit の次の successor: 初めて \(\mathrm{Con}(T_{\ell(e)})\) または \(\mathrm{RFN}_\Gamma(T_{\ell(e)})\) を加える

したがって limit は「無限回反射したので完全になった stage」ではない。適切に c.e. で十分強い limit theory なら、それ自身も incompleteness の対象になる。

# 6. Monotonicity と strength measures

## 6.1 Inclusion

definition が cumulative なら、notation path 上で

\[
a<_{\mathcal O^\ast}b
\quad\Longrightarrow\quad
T_a\subseteq T_b
\]

という axiom inclusion、したがって theorem inclusion を得る。

## 6.2 Strictness

標準 provability predicate を持ち、\(T_a\) が Gödel II の条件を満たし整合的なら、\(\mathrm{Con}(T_a)\) は \(T_a\) の theorem でなく \(T_{s(a)}\) の theorem なので deductive inclusion は strict である。

uniform reflection progression での strictness は、formula class、base theory、soundness assumptions、比較する consequences に依存する。全 operator について「successorなら常に同じ意味で strict」とは言わない。

## 6.3 同一視できない六つの尺度

| 尺度 | 内容 |
|---|---|
| axiom inclusion | axiom sets の包含 |
| deductive strength | theorem sets の包含・非包含 |
| consistency strength | どの theory の consistency を証明するか |
| reflection strength | どの formula class / uniformity の reflection を持つか |
| conservation strength | \(\Pi_n\) 等、特定 class の新 consequences があるか |
| ordinal strength | 指定した reduction / notation system による proof-theoretic calibration |

同じ ordinal lengthでも operator が違えばこれらの尺度は変わる。逆に theory extensions が異なっても、特定 class に関して conservative である場合がある。

# 7. Gödel 第2との接続

Gödel II は、適切な \(T_a\) について

\[
T_a\nvdash\mathrm{Con}(T_a)
\]

を与える。これにより、外部で \(\mathrm{Con}(T_a)\) を正しいと受け入れる根拠があるなら、

\[
T_a+\mathrm{Con}(T_a)
\]

は strict extension を作る自然な候補になる。

ただし Gödel II 自身は次の stage を採用せよと命令しない。\(\mathrm{Con}(T_a)\) の真理・受容、notation path の well-foundedness、iteration の正当化は metatheoretic / foundational choice である。

| 項目 | Gödel II | Consistency progression |
|---|---|---|
| 主対象 | 一つの c.e. theory \(T\) | notation-indexed family \(T_a\) |
| 結論 / rule | \(T\nvdash\mathrm{Con}(T)\) | \(T_{s(a)}:=T_a+\mathrm{Con}(T_a)\) |
| 性格 | limitation theorem | external recursive construction |
| index | 固定 \(T\) | subject theory を stage ごとに更新 |
| iteration | 主張しない | notation と operator を追加して初めて生じる |

# 8. Löbとの接続

固定文 \(\varphi\) に対する Löb の定理は、

\[
T_a\vdash
\mathrm{Pr}_{T_a}(\ulcorner\varphi\urcorner)
\to\varphi
\quad\Longrightarrow\quad
T_a\vdash\varphi
\]

である。

一方、external reflection extension は

\[
T_{s(a)}
=
T_a+
\bigl(
\mathrm{Pr}_{T_a}(\ulcorner\varphi\urcorner)
\to\varphi
\bigr)
\]

と定義できる。Löb の antecedent は「\(T_a\) が reflection を証明する」であり、後者は「\(T_{s(a)}\) が \(T_a\)-reflection を axiom として持つ」なので一致しない。

**明示判定:** same-theory collapse と external strengthening は、subject theory の index を

\[
a\longmapsto s(a)
\]

と一段ずらすことで形式的に分離されている。この index shift は progression の核心である。ただし「Löb を回避する技巧」ではなく、異なる theory を定義しているだけである。

# 9. Consistency / local / uniform reflection progression

| progression operator | successor stage | scope | truth predicate | 典型的比較点 |
|---|---|---|---|---|
| consistency | \(S\mapsto S+\mathrm{Con}(S)\) | \(\bot\) 一文 | 不要 | consistency strength、\(\Pi_1\) consequences |
| local reflection | \(S\mapsto S+\mathrm{Rfn}_\Gamma(S)\) | closed \(\Gamma\)-sentences | 不要 | local reflection・conservation |
| uniform reflection | \(S\mapsto S+\mathrm{RFN}_\Gamma(S)\) | \(\Gamma\)-formulasと全 parameters | full truth は不要 | induction / uniform soundness strength |

同じ notation \(a\)、同じ \(|a|\) でも、operator が違えば \(T_a\) の strength は違う。さらに \(\Gamma=\Pi_1,\Pi_n\)、full arithmetic の違いも独立変数である。

Feferman completeness theorem は、PA 上で full uniform reflection を適切な recursive notations に沿って反復すれば、任意の真な arithmetical sentence がある stage で証明される、と述べる。これは「一つの progression path / 一つの c.e. union が arithmetic truth 全体になる」という主張ではない。文ごとに適切な notation / presentation を選ぶ存在主張であり、その notation が genuine であることの認識は元の truth judgment より容易とは限らない。

# 10. Turing / Feferman completeness の限定

## 10.1 Turing 型 \(\Pi_1\) completeness

Turing 型の結果では、任意の真な \(\Pi_1\) sentence \(\sigma\) に対し、\(|a|=\omega+1\) を持つ suitable notation \(a=a(\sigma)\) が存在し、対応 stage が \(\sigma\) を証明する。

重要なのは次の三点である。

1. \(a\) は \(\sigma\) に依存する
2. 同じ order type \(\omega+1\) でも presentation が違う
3. 一つの c.e. stage が全真 \(\Pi_1\) sentences をまとめて証明するわけではない

この結果は ordinal valueだけで strengthを測ることへの反例になる。

## 10.2 Feferman 型 arithmetic completeness

full uniform reflection progression では、任意の真な arithmetical sentence \(\theta\) に対して suitable recursive notation \(a\) が存在し、

\[
\mathrm{RFN}^{a}(PA)\vdash\theta
\]

となる。現代的な改良では必要な order type の sharp bounds も研究される。

しかし、

- truth 全体を一つの c.e. theory にしたわけではない
- notation membership / well-foundedness の認識が非自明
- theorem ごとに path / presentation を選び得る
- natural notation systems に制限した ordinal analysis と unrestricted completeness trick は区別される

ため、「transfinite iteration が arithmetic truth へ収束する」と要約してはならない。

## 10.3 Pathwise incompleteness

固定した effective / definable path に沿う union は、適切な条件下でなお一つの形式的または definability-bounded theoryとして incompleteness を持つ。all-notes union や theorem-dependent path selection と、one fixed progression path を混同しない。

# 11. Feferman autonomous progression / predicativity

通常の recursive progression では、notation の well-foundedness は外部 metatheory から与えられる。autonomous progression では、ある notation \(a\) まで上昇することを許すのは、すでに受け入れた以前の theory が \(a\) の accessibility / well-foundedness を適切に認証できる場合に限る、という bootstrapping restriction を置く。

これは単に iteration length を短くする条件ではない。

- どの ordinal notations を正当と認めるか
- その正当性をどの既受容 theory で証明できるか
- reflection extension を受け入れる epistemic / predicative basis は何か

を progression 内部の acceptance architecture に組み込む。

Feferman–Schütte 型 predicative analysis との接続はここにある。ただし本稿では predicativity の philosophical characterization や \(\Gamma_0\) の正当性論争へは進まない。

# 12. Notation dependence stress test

## 12.1 Extensional equality と intensional path

| 項目 | actual ordinal | recursive notation |
|---|---|---|
| identity | order-isomorphism type | finite code / computable presentation |
| predecessor data | 全ての小さい ordinals | code が参照する predecessor path |
| limit data | order-theoretic limit | effective fundamental sequence / presentation |
| algorithm input | 直接は不可 | 可能 |
| multiplicity | ordinal は一つ | 同じ ordinal に複数 notations |
| theory assignment | 単独では不足 | recursive progression を実行できる |

## 12.2 Canonicality problem

unrestricted notation systems では、同じ \(\alpha\) を表す notations が異なる c.e. presentations を生成し得る。従って

\[
\alpha\mapsto T_\alpha
\]

が order type だけで well-defined だと仮定してはならない。必要なのは、例えば次のいずれかである。

- unique / canonical notation discipline
- computable well-order presentationを固定
- different presentations 間の invariance / conservation theorem
- natural progression と consequence class を固定した ordinal analysis

## 12.3 Ordinal は strength の量そのものではない

proof-theoretic ordinal は、どの reduction relation、well-ordering principle、reflection operator、consequence class で strength を測るかに相対する。notation length は重要な calibration device だが、単独の「理論強度メーター」ではない。

# 13. Progression monotonicity と conservation

consistency operator では successor ごとに新しい \(\Pi_1\) consistency sentence が加わる。uniform \(\Pi_n\)-reflection operator では、より高い complexity の consequences や induction principles が現れ得る。

Schmerl 型 conservation formulas や reflection calculus は、短い強 reflection iterationと長い弱 reflection iterationが、指定 formula classについて同じ consequencesを持つ場合を記述する。このため、

\[
\text{stage index の大小}
\]

と

\[
\text{全言語での deductive strength}
\]

と

\[
\Pi_n\text{-conservativity}
\]

は別々に記録しなければならない。

# 14. “Moving boundary” 仮説

## 14.1 捉える構造

appropriate \(T_a\) について、典型的には

\[
T_a\nvdash\mathrm{Con}(T_a),
\]

\[
T_{s(a)}\vdash\mathrm{Con}(T_a),
\]

\[
T_{s(a)}\nvdash\mathrm{Con}(T_{s(a)}).
\]

「強い stage は旧 stage の制約文を採用できるが、新 stage-relative constraint が形成される」という読みは、consistency progression と適切な reflection progression に繰り返し現れる。

## 14.2 限界

しかし “boundary” は technical object ではない。実際に変化するのは、

- subject theory \(T_a\)
- provability predicate \(\mathrm{Pr}_{T_a}\)
- consistency / reflection formula
- extension theory \(T_{s(a)}\)

である。また operator、formula class、notation path によって progression の strength は変わるため、moving boundary を単一量として測れない。

## 14.3 判定

**M2 — 異なる consistency / reflection progressions に再現する比較軸として有効。**

M1 より高いのは、subject-theory reindexing が複数 operator に共通し、same-theory theorem と external extension を横断比較できるためである。ただし technical classification は stage-relative provability / reflection progression で十分であり、新しい proof-theoretic invariant ではないので M3 ではない。

# 15. 「固定する側 / 固定される側」の非対称性

## 15.1 標準語彙での再記述

この比較語彙が指すものは、**reflection / consistency axiom の subject theory と extension theory の非同一性**である。

\[
\underbrace{T_{s(a)}}_{\text{axiomを持つ extension}}
\vdash
\underbrace{\mathrm{Con}(T_a)}_{\text{旧 subject theory に相対}}
\]

であって、

\[
T_{s(a)}\vdash\mathrm{Con}(T_{s(a)})
\]

ではない。reflection predicate の subscript が \(a\) に留まり、証明主体の subscript が \(s(a)\) へ移ることが本体である。

## 15.2 単なる bookkeeping か

index を誤ると、

- Löb の same-theory premise と external axiom additionを同一視する
- Gödel II に反して successor が self-consistency を証明したように見える
- reflection progression がなぜ反復を必要とするかを説明できない

ため、これは装飾的 bookkeeping ではない。一方、標準記法 \(\mathrm{Pr}_{T_a}\)、\(T_{a+1}\) で完全に表現でき、新原理ではない。

## 15.3 判定

**A2 — consistency / local / uniform reflection progressions を横断する安定した architecture feature。**

A3 は棄却する。これは新しい proof-theoretic principle でなく、subject theory と extension theory の stage-relative typing を可視化する比較記述である。

# 16. 「証明デザイン」P2 の再検査

今回の hierarchy は、

\[
\text{base theory}
+
\text{extension operator}
+
\text{ordinal notation}
+
\text{successor rule}
+
\text{limit rule}
\]

から生成される。さらに proof predicate presentation、formula class、consequence measure が strength comparison を決める。

これにより、既存文書の比較枠は次の三段階へ拡張された。

1. **theorem anatomy:** assumptions が一つの conclusion を支える
2. **logic anatomy:** axioms・rules・modal operator が theoremhood を組織する
3. **progression anatomy:** theory-transformer・notation・stage rules が theory hierarchy を組織する

**再判定: P2 — proof / theory architecture の比較枠として有効。**

P3 は棄却する。standard recursive progressions、reflection theory、ordinal analysis の再編成であり、新 proof-theoretic framework ではない。

# 17. 「残差」RX の再検査

候補を分離する。

- \(\mathrm{Con}(T_a)\): stage-relative unprovable sentence
- \(T_{s(a)}\): recursive extension
- different notation: alternative computable presentation
- unaccepted reflection: foundational acceptance problem
- later stage: progression operator の反復結果

これらは同じ数学的型ではない。特に \(\mathrm{Con}(T_{s(a)})\) は \(\mathrm{Con}(T_a)\) の残りや補正項でなく、新 subject theory に相対する別文である。

**判定: RX — residual vocabulary not useful here.**

stage-relative unprovability、notation dependence、theory progression、operator iteration の標準語彙がより精密である。R2 のような明示的補正項はない。

# 18. Erasure Test

「閉包」「残差」「moving boundary」「固定」「外部化」「証明デザイン」を全削除しても、次で技術内容を記述できる。

- recursive progression と notation-indexed theory family
- stage-relative provability predicates
- iterated consistency / reflection
- effective successor / limit clauses
- Gödel II と Löb
- notation / presentation dependence
- conservation と ordinal analysis
- GL / GLP / reflection calculus

数学的内容と prediction は失われない。一方、same-theory / next-theory の index shift が Gödel、Löb、reflection principles を通じて反復されることを一目で比較する教育的導線は少し失われる。

**判定: E1 — 教育的・横断比較的な見通しだけ失う。**

E2・E3 は棄却する。

# 19. GL / GLPとの接続

## 19.1 GL

GL の単一 modality \(\Box\) は、固定 theory \(T\) の標準 provability predicateについて、K、necessitation、Löb principle、finite nesting \(\Box^n\) を抽象化する。

しかし pure propositional GL だけでは、

- stage theory \(T_a\) の c.e. presentation
- arbitrary recursive ordinal notation
- limit-stage union
- formula-class indexed reflection
- multiple strength measures

を表せない。

## 19.2 GLP と graded progressions

GLP の modalities \([0],[1],[2],\ldots\) と dual consistency modalities \(\langle n\rangle\) は、異なる \(n\)-provability / reflection strength を区別する。closed modal formulasである worms は、iterated consistency / reflection patterns と ordinal notations を接続する。

これは single \(\Box\) より progression analysis に適するが、arbitrary Feferman progression の notation dependence、global truth reflection、external soundness を全て一つに還元するわけではない。

## 19.3 Reflection calculus

reflection calculus や Turing–Schmerl calculi は、異なる consistency notions と progression stages の inclusion / conservation relations を modal / algebraic に圧縮する。従って「moving boundary」を形式化したいなら、独自語彙より、これらの standard calculi の方が強い。

# 20. Ordinal analysis との接続

ordinal analysis は、対象 theory の proofs / consequences を、well-founded notation system、transfinite induction、reflection progression 等へ還元し、その strength を較正する。

progression length の役割を正確に読むには、少なくとも次を固定する。

- base theory
- notation system とその well-founded segment
- successor operator
- formula class
- equivalence / conservation の対象 class
- metatheory で許す transfinite induction

proof-theoretic ordinal はこれらの analysis setup に相対する。ordinal value を理論の内在的な一個の重量とみなさない。

# 21. 研究ログとの比較

| research-log side | progression side | 判定 |
|---|---|---|
| universal guarantee を試みる | all arithmetic truth を capture する completeness question | 問題設定の類似のみ |
| self-application で scope が問題 | \(\mathrm{Pr}_{T_a}\) と same-stage reflection | 構造的類似 |
| scope を局所化 | formula class / local reflection を固定 | scope control の類似 |
| one level を別 level から評価 | \(T_{s(a)}\) が \(T_a\)-reflection を採用 | level shift の類似 |
| 次 level に新制約 | stage-relative \(\mathrm{Con}(T_{s(a)})\) | moving index の類似 |
| transfinite hierarchy | recursive notation progression | research-log側に形式対応なし |

**類似判定: Q1 — level shift / scope shift の構造類似。**

research-log 側に c.e. theory、standard provability predicate、recursive notation system、successor operator、limit rule の形式写像はない。従って Q2・Q3 は選ばない。

# 22. 最終比較表

| structure | indexed object | next-stage operator | same-stage self-application? | limit operation | strength measure | canonical? |
|---|---|---|---|---|---|---|
| Gödel II | 固定 c.e. theory \(T\) | theorem自体は operatorを与えない | 整合的 \(T\) は標準 \(\mathrm{Con}(T)\) を証明不可 | なし | consistency limitation | provability presentation に相対 |
| Löb local reflection | \(T,\varphi\) | theorem自体は extensionを作らない | \(T\vdash(\mathrm{Pr}_T(\ulcorner\varphi\urcorner)\to\varphi)\Rightarrow T\vdash\varphi\) | なし | local theoremhood | standard predicateに相対 |
| consistency progression | notation \(a\) と \(T_a\) | \(T_a\mapsto T_a+\mathrm{Con}(T_a)\) | old consistency を next stageへ。new self-consistency は不可 | effective union | consistency / \(\Pi_1\) / ordinal strength | 一般には notation-sensitive |
| uniform reflection progression | notation \(a\)、\(T_a\)、\(\Gamma\) | \(T_a\mapsto T_a+\mathrm{RFN}_\Gamma(T_a)\) | same-stage full reflectionとは別 | effective union | reflection / induction / conservation / ordinal strength | operator・class・notationに相対 |
| GL | modal formula、single \(\Box\) | external stage operatorなし | Löb axiomが local provable reflectionを制約 | なし | modal theoremhood / frame validity | systemとして固定 |
| GLP | modal formula、modalities \([n]\) | graded consistency / reflection interpretation | modalityごとの Löb structure | pure syntaxには theory-unionなし | modal ordering、worms、conservation | interpretationとnormal formに相対 |

# 23. Kill criteria

| criterion | 検査結果 |
|---|---|
| 1. moving boundary が stage-relative provability の言い換え | **技術的には成立**。ただし横断要約として M2 |
| 2. 「固定する側 / 固定される側」が index bookkeeping にすぎない | **半成立**。標準 indexで尽くせるが、誤ると same/next theoryを混同するため比較価値は A2 |
| 3. strength が operator / class / notation に依存し一軸化不能 | **成立** |
| 4. ordinal notation theory が architecture を十分説明 | **成立** |
| 5. GLP / reflection calculus が iterationを精密化 | **成立。ただし arbitrary notation dependence 全体ではない** |
| 6. 「証明デザイン」は既存 architecture の言い換え | **成立する限界あり。P2に留める** |
| 7. residual vocabulary が technical distinctionsを潰す | **成立。RX維持** |

negative result を保存する。“moving boundary” と非対称性には比較上の価値があるが、standard stage indexing を越える theorem / invariant は生まれない。

# 24. 最終出力

## A. Turing–Feferman progression の核心

- c.e. theories を recursive ordinal notations に沿って反復的に強化する architecture。
- successor は旧 stage の consistency / reflection を新 stage の axiom にする。
- limit は effective predecessor stages の union で、新 reflection axiomではない。
- strength は base、operator、formula class、notation presentation、比較尺度に依存する。
- actual ordinal と computable notation を同一視してはならない。

## B. Successor stage の核心

1. \(T_{s(a)}\) が持つのは \(\mathrm{Con}(T_a)\) / \(\mathrm{RFN}(T_a)\) である。
2. \(T_a\nvdash\mathrm{Con}(T_a)\) と \(T_{s(a)}\vdash\mathrm{Con}(T_a)\) は主体が違う。
3. \(\mathrm{Con}(T_{s(a)})\) は自動的に得られず、新しい stage-relative statement になる。

## C. Limit stage の核心

1. effective cofinal presentation に沿う先行 axioms の union。
2. 一様 c.e. presentation があれば limit theory も c.e. に保てる。
3. 完全化でも新 reflection axiom の追加でもなく、次 successor で limit theory 自身が対象化される。

## D. Gödel II / Löb との最大の違い

1. Gödel II と Löb は fixed theory に関する limitation / theoremhood theorem。
2. progression は metatheory が定義する family construction。
3. Gödel II は successor axiomの採用を命令しない。
4. Löb の same-theory premise と next-stage axiom addition は index shift で分離される。
5. transfinite iteration には別途 notation、successor / limit rule、acceptance conditions が必要。

## E. Notation dependence の重要性

1. actual ordinal は algorithm の入力でなく、recursive notation が stage presentation を与える。
2. 同じ ordinal に対する異なる notations が異なる stage theoriesを生成し得る。
3. ordinal lengthだけでは strength を測れず、naturalness / invariance / conservation の追加結果が必要。

## F. “Moving boundary” 判定

**M2。** consistency / reflection operatorsを横断する stage-reindexing の比較軸として有効。ただし標準的 stage-relative provability の要約であり、新 invariant ではない。

## G. 「固定する側 / 固定される側」の非対称性判定

**A2。** extension \(T_{s(a)}\) と reflection subject \(T_a\) の非同一性は複数 progressions に安定して現れる。新原理ではなく、subject / extension typing の可視化である。

## H. 「証明デザイン」再判定

**P2。** theorem anatomy → logic anatomy → theory progression anatomy への比較枠の拡張として有効。standard proof theoryを置換しない。

## I. Residual 判定

**RX。** unprovable consistency、next stage、alternative notation、unaccepted reflectionは異なる型であり、「残差」でまとめる利益がない。

## J. Erasure Test

**E1。** 独自語彙を消しても技術内容は全て残り、既存 stress tests との教育的な横断線だけ少し失う。

## K. 研究ログとの類似

**Q1。** level shift / scope shift の構造類似のみ。formal stage hierarchy との写像はない。

## L. 最も重要な新規観察

1. progression の本体は「限界の反復」より、provability predicate の **subject-theory reindexing** にある。
2. limit stage は強化 operator ではなく effective aggregation operator であり、successor と役割が異なる。
3. same ordinal value でも notation path が違えば theory が変わり得るため、ordinal value単独の strength 読みは成立しない。

## M. 次の一手

1. **GLP / worms / ordinal notation anatomy:** modal normal forms が natural notation と reflection iteration をどこまで canonicalize するかを検査する。
2. **Consistency vs uniform reflection progression:** 同じ notation lengthでの conservation・induction・arithmetical hierarchy差を比較する。
3. **Proof-theoretic ordinal anatomy:** ordinal assignment が何に相対し、どの invarianceを要求するかを独立に解剖する。

# 25. 検証資料

- [A. M. Turing, “Systems of Logic Based on Ordinals”](https://doi.org/10.1112/plms/s2-45.1.161) — ordinal logics、constructive ordinal presentations、invariance / completeness question の原典。
- [S. Feferman, “Transfinite Recursive Progressions of Axiomatic Theories”](https://www.mathnet.ru/eng/mat619) — recursive progressions、reflection operators、notation-indexed theory families の基礎。
- [Michael Rathjen and Wilfried Sieg, “Turing’s and Feferman’s Results on Recursive Progressions”](https://plato.stanford.edu/entries/proof-theory/appendix-b.html) — Turing / Feferman completeness とその circularity・path dependence の精密な解説。
- [Fedor Pakhomov, Michael Rathjen, Dino Rossegger, “Feferman’s Completeness Theorem”](https://arxiv.org/abs/2405.09275) — computable presentationsへの依存、uniform reflection completeness、order-type bounds の現代的分析。
- [Eduardo Hermo Reyes and Joost J. Joosten, “The Logic of Turing Progressions”](https://arxiv.org/abs/1604.08705) — 複数 consistency notions と formalized Turing progressions の modal analysis。
- [David Fernández-Duque and Joost J. Joosten, “Turing Progressions and Their Well-Orders”](https://personal.us.es/dfduque/cie.pdf) — Turing progressions、GLP、worms、ordinal well-orders の接続。
- [Stanford Encyclopedia of Philosophy, “Proof Theory”](https://plato.stanford.edu/entries/proof-theory/) — autonomous progressions、predicativity、ordinal analysis の標準的概観。

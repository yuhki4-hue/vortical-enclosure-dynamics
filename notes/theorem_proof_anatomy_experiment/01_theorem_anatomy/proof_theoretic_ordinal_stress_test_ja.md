# Proof-theoretic ordinal（証明論的順序数）
## special stress test

本稿でいう「strength profile」「proof architecture」「canonicalization」「固定／外部化」は比較用の解剖的メタ記述であり、標準 proof theory の用語ではない。技術的記述では、ordinal notation、transfinite induction、well-ordering strength、cut elimination、reflection progression、conservation、interpretability、ordinal analysis を優先する。

中心結論を先に述べる。**proof-theoretic ordinal は、比較方法を固定した自然な理論群に対しては強力でしばしば頑健な一次元 calibration だが、理論の全 strength を表す万能スカラーではない。** 「|T|=\alpha」は、少なくとも notation、base/metatheory、formula class、reduction notion を省略した略記である。

## 0. 「proof-theoretic ordinal」の採用定義

一つの無条件な定義へ固定せず、次の近接した characterizations を区別する。

### 0.1 Transfinite-induction characterization

recursive notation system \((\mathcal O,<_{\mathcal O},|-|)\) と formula class \(\Gamma\) を固定し、

\[
|T|^{\mathrm{TI}}_{\Gamma,\mathcal O}
:=
\sup\{|a|:a\in\mathcal O, T\vdash
\mathrm{TI}_{\Gamma}(<_a)\}
\]

と測る。\(\mathrm{TI}\) を schema とするか、progressiveness から全域性をいう一文とするか、parameters を許すかで値は変わり得る。

### 0.2 Well-ordering characterization

特に second-order arithmetic では、primitive recursive linear order \(a\) に対する \(\mathrm{WO}(a)\) を用い、

\[
|T|_{\mathrm{WO}}
:=sup\{|a|:T\vdash\mathrm{WO}(a)\}
\]

とする標準的定義がある。外部から genuine well-order である notation のみを数えるため、\(T\) の適切な soundness と、notation を評価する metatheory が背景に残る。[Pakhomov–Walsh](https://arxiv.org/abs/1805.02095)

### 0.3 Reduction / cut-elimination characterization

\(T\) の有限証明を infinitary calculus へ埋め込み、proof/cut に ordinal label を割り当てる。cut reduction のたびに measure が真に下降し、ある \(\alpha\) までの well-foundedness が normalization、consistency、または指定 class に対する reduction を支えるとき、その最小上界を ordinal calibration とする。

### 0.4 Reflection characterization

base \(B\)、formula class \(\Gamma\)、reflection operator を固定し、\(T\) の指定 consequence class が

\[
R^\Gamma_\alpha(B)
\]

のどの長さで再現・保存・還元されるかを測る。これは progression length そのものではなく、\(T\) と progression を結ぶ conservation/reduction theorem を含む characterization である。

### 0.5 Worm / provability-algebra characterization

GLP worms の provable-equivalence class を Beklemishev ordering で並べ、ordinal assignment \(o(A)\) を与える。worm ordinal が theory ordinal になるのは、算術解釈と reduction/conservation theorem により、その worm が特定の consistency/reflection extension を表す場合に限る。[Joosten](https://arxiv.org/abs/1212.2395)

従って本稿では、裸の \(|T|\) を「選択済みの自然な ordinal-analysis package に相対する略記」と読む。異なる characterizations の一致は一般には**定義ではなく定理**である。

## 1. 代表例の固定

主例は \(PA\) と Gentzen 型 \(\varepsilon_0\)-analysis とする。弱い算術は値そのものより、値の定義依存性を示す stress test として用いる。

| theory | よく用いられる calibration | この表が意味する範囲 |
|---|---:|---|
| \(EA=I\Delta_0+\exp\) | 弱い算術では定義により表示が揺れる | formula class、provably total functions、WO/TI の選択を必ず指定 |
| \(PRA\) | 典型的に \(\omega^\omega\) | finitistic reduction／provably recursive calibration に相対 |
| \(I\Sigma_1\) | 典型的に \(\omega^\omega\) | \(PRA\) と同じ値でも deductive equality を意味しない |
| \(I\Sigma_n\) | 典型的に有限 \(\omega\)-towerで校正 | indexing convention と induction/reflection class に依存 |
| \(PA=\bigcup_n I\Sigma_n\) | \(\varepsilon_0\) | Gentzen、TI、標準 reflection analysis が橋渡し定理により収束 |

弱い理論では reasonable definitions が一致しないことがあり、「表の値」は theorem-independent な固有重量ではない。反対に \(PA\) の \(\varepsilon_0\) は複数の標準分析が一致する代表的な頑健例である。[SEP: Proof Theory](https://plato.stanford.edu/entries/proof-theory/)

## 2. Actual ordinal と notation system

次を分離する。

| object | 型 | 内容 |
|---|---|---|
| \(\alpha\) | metatheoretic ordinal | well-order の order type |
| \(a\) | finite/recursive syntax | \(\alpha\) を表す notation |
| \(\mathcal O\) | recursive presentation | notations と comparison/fundamental sequence の体系 |
| \(|a|=\alpha\) | external interpretation | notation の order type を外部で同定する主張 |
| \(|T|=\alpha\) | calibration claim | 選択した analysis における \(T\) の上界／supremum |
| \(T_a\) | formal theory | notation \(a\) に沿って構成された progression stage |

\(|a|=\alpha\) は一つの syntax object の意味を述べる。\(|T|=\alpha\) は、理論全体と analysis method の関係を述べる。さらに \(|a|=|b|\) でも、notation-sensitive progression では \(T_a=T_b\) は自動でない。

## 3. 「ordinal of a theory」は一意か

- **Q1:** 異なる standard characterizations が同じ ordinal を与えることは、一般定義ではなく、cut-elimination、reflection reduction、WO/TI equivalence などの**橋渡し定理**である。
- **Q2:** notation を変えても同じ値と呼ぶには、order-type invariance に加え、分析が notation の presentation でなく適切な equivalence class に不変であることが要る。
- **Q3:** 同一理論に複数の reasonable ordinal analyses があり得る。特に弱い理論では formula complexity や representation による差が前景化する。
- **Q4:** “the proof-theoretic ordinal” は、\(PA\) の Gentzen/standard reflection analysis のように自然な分析群が一致すると確認済みの範囲では正当な慣用である。任意の理論・任意の strength notion には拡張できない。

Pakhomov–Walsh は、一定の sound な自然理論では reflection rank と well-ordering ordinal が一致する一方、一般には分離する例があることを示す。これは定冠詞の使用が invariance theorem に依存する好例である。[Reflection Ranks and Ordinal Analysis](https://arxiv.org/abs/1805.02095)

## 4. 通常 anatomy

1. **concept_name:** proof-theoretic ordinal / ordinal analysis
2. **domain:** proof theory、arithmetical・second-order theories、infinitary calculi、reflection theory、provability algebras
3. **standard_definitions:** 第0節の TI、WO、reduction、reflection、worm の五 characterization。単一無条件定義ではない
4. **assumptions:** theory、language、notation、reduction notion、formula/consequence class、base/metatheory、必要な soundness
5. **hypothesis_levels:** 第5節
6. **measurement_types:** 第6節
7. **architecture_roles:** proof descent control、well-order calibration、reflection calibration、conservation comparison、normal-form ranking
8. **calibrated_object:** theorem set 全体ではなく、指定された proof transformations または consequence class に関する \(T\) の強さ
9. **blocked_confusions:** notationとordinal、progression lengthとtheory ordinal、同値と保存、WOとfull theoremhood、rankとinterpretabilityの混同を遮断
10. **what_fails_if_definition_changed:** 値、sharpness、比較順序が変わり、別 characterization との一致には新たな橋渡し定理が必要
11. **what_reappears:** formula-class dependence、notation dependence、conservation profile、metatheoretic well-foundedness、別 preorder が再び可視化される
12. **proof_resources:** infinitary embedding、cut elimination、ordinal assignment、fundamental sequences、TI/WO、reflection reduction、GLP/worm calculus
13. **calibration_style:** **相対的順序数校正**（説明ラベル）
14. **object_vs_metatheory_comment:** \(T\) は分析対象であり、notation の genuine well-foundedness、reduction theorem、soundness は通常 stronger metatheory で証明される。\(T\) 内部の notation code と、外部でその order type を認識することを同一視しない
15. **short_comment:** ordinal analysis は無限証明変形を well-order の下降へ還元し、複雑な proof strength を比較可能にする。ただし得られる数値は、先に固定した観測窓の上での座標である

## 5. Characterization ごとの assumptions

| assumption | TI | WO | cut reduction | reflection | worm |
|---|---:|---:|---:|---:|---:|
| theory \(T\) / language | 必要 | 必要 | 必要 | 必要 | arithmetic interpretation 時に必要 |
| ordinal notation \(\mathcal O\) | 必要 | 必要 | 必要 | stage 表示に必要 | ordinal assignment に必要 |
| formula class \(\Gamma\) | TI class | WO formula の型 | end-sequent/cut class | 本質的 | modality 解釈に埋込 |
| infinitary calculus / embedding | 不要 | 不要 | 本質的 | ルート依存 | 不要 |
| base theory \(B\) | 比較に必要 | coding に必要 | formalization に必要 | 本質的 | arithmetic completeness/reduction に必要 |
| soundness / consistency | genuine ordinal 抽出に必要 | genuine WO 抽出に必要 | consistency 結論に必要 | reflection acceptance に必要 | arithmetic strength 読みで必要 |
| metatheory | notation と supremum を扱う | WO 判定 | termination proof | progression比較 | order type と interpretation |

`background` は recursive syntax、通常の集合論、外部自然数、有限 proof coding。`ambient` は言語・calculus・notation system・base theory。`object` は対象理論 \(T\) とその induction/reflection/proof rules。`definitional` は formula class、rank domain、soundnessを要求する比較対象クラスなどである。

## 6. measurement_types

| measurement | indexed object | 主に測るもの | ordinal が担う役割 |
|---|---|---|---|
| proof height | infinitary derivation | derivation tree の高さ | proof の局所 measure |
| cut rank | cuts/formulas | elimination complexity | reduction と組にした二重 measure |
| induction length | notation + formula class | 証明可能な TI の範囲 | supremum calibration |
| well-ordering strength | recursive orders | 証明可能な WO statements | order-type supremum |
| reflection length | progression | reflection iteration | operator 固定後の stage coordinate |
| conservation rank/spectrum | consequence classes | 各 \(\Gamma\) での保存関係 | class ごとに別 rank があり得る |
| modal/worm rank | worm equivalence class | provability-algebra order | syntax normal form の rank |
| interpretability rank | theories/interpretations | translation による relative strength | ordinalとは別 preorder |

## 7. Gentzen-style ordinal analysis

PA の有限証明を、構造が見える infinitary proof system へ埋め込む。各 derivation/cut configuration に \(\varepsilon_0\) 未満の notation を割り当て、cut reduction がその measure を真に減少させるよう設計する。\(\varepsilon_0\) までの適切な transfinite induction／well-foundedness を metatheory で用いると、無限下降がなく reduction が終了し、矛盾の cut-free proof が存在しないことから \(\mathrm{Con}(PA)\) を得る。

従って ordinal が直接制御するのは**proof transformation の termination**である。PA の theorem set を一つの ordinal に写したのではない。Gentzen の分析では、\(PA\) が各 \(\alpha<\varepsilon_0\) までの適切な TI を証明する一方、\(\varepsilon_0\) 全体の当該原理は consistency proof を可能にするため、sharp boundary が得られる。[SEP: Proof Theory](https://plato.stanford.edu/entries/proof-theory/)

## 8. \(\varepsilon_0\) が指すもの

| 用法 | 直接 \(\varepsilon_0\) か | 注記 |
|---|---:|---|
| canonical Cantor-normal-form notation system | yes | order type が \(\varepsilon_0\) |
| cut-reduction measure の上界 | yes | chosen Gentzen calculus に相対 |
| PA が証明する TI の supremum | yes（標準 characterization） | formula class・notation を固定 |
| reflection progression length | bridge theorem 次第 | base/operator により length 変換が入る |
| GLP\(_\omega\) worm \(<_0\) order | yes | worm equivalence classes の order type |
| PA の theorem set | no | 集合とordinalは異型 |
| PA の全 strength | no | interpretability、conservation spectrum等を含まない |

## 9. \(|PA|=\varepsilon_0\) の解剖

- **A — notation:** 通常は \(0,+,\alpha\mapsto\omega^\alpha\) と Cantor normal form で \(\varepsilon_0\) 未満を表す recursive notation を用いる。
- **B — lower bound:** 各固定 \(\alpha<\varepsilon_0\) について、PA は選択した範囲の transfinite induction / well-ordering を証明できる。
- **C — upper/sharpness:** \(\varepsilon_0\) 全体の適切な TI を finitistic base が利用できれば Gentzen reduction により \(\mathrm{Con}(PA)\) が従う。PA 自身がその十分な原理を証明することは、整合性のもとで Gödel II と衝突する。
- **D — reduction theorem:** PA proofs を \(\varepsilon_0\)-controlled infinitary reductionsへ写す定理が必要。
- **E — meaning of equality:** \(\varepsilon_0\) は到達する最大 notation というより、PA が扱える標準 well-order/TI の**supremum**であり、指定 reduction notion の sharp calibration である。

## 10. \(PRA/EA/I\Sigma_n/PA\) の比較

| theory | ordinal-analysis 上の典型的位置 | 省略してはいけない点 |
|---|---|---|
| \(EA\) | elementary base として progression/formalization を支える | 弱い体系では ordinal definition 間の差が大きい |
| \(PRA\) | \(\omega^\omega\) 型の finitistic/provably recursive calibration が標準的 | language と function symbols、TI formula class に依存 |
| \(I\Sigma_1\) | 同じく \(\omega^\omega\) と表示される標準 calibration がある | \(PRA\) と theorem sets が同一という意味ではない |
| \(I\Sigma_n\) | \(n\) に応じた有限 \(\omega\)-tower | tower の indexing convention を明記 |
| \(PA\) | finite fragments の supremum として \(\varepsilon_0\) | standard analyses の一致は bridge theorems による |

同じ ordinal 表示が違う theory を同一化しない例として \(PRA\) と \(I\Sigma_1\) が有用である。Parsons 型 conservativity は、指定された低複雑度 consequences で両者が近い理由を説明するが、deductive equality や同一 induction schema を与えない。ここでも ordinal は consequence-sensitive な圧縮である。

## 11. Progression length との違い

\[
C_\alpha(B),\qquad R^\Gamma_\alpha(B)
\]

の \(\alpha\) は、**operator と base を固定した progression coordinate**である。resulting theory の proof-theoretic ordinal は、その theory を別途分析して得る。一般に

\[
\text{progression length }\alpha
\neq
|R^\Gamma_\alpha(B)|.
\]

operator の一回がどれほどの reflection strength を加えるか、base が既に何を証明するか、どの consequences で還元するかを通じて変換関数が入る。

## 12. Schmerl formulas

既存分析で採用した標準的 schematic relation

\[
R^{\alpha}_{\Pi^0_{n+m}}(EA^+)
\equiv_{\Pi^0_n}
R^{\omega_m(\alpha)}_{\Pi^0_n}(EA^+),
\]

\[
\omega_0(\alpha)=\alpha,qquad
\omega_{m+1}(\alpha)=\omega^{\omega_m(\alpha)}
\]

は、operator complexity を一段変えると、同じ低位 consequence class で必要な iteration length が ordinal transform を受けることを示す。左辺と右辺は theory equality ではなく \(\Pi^0_n\)-conservation/equivalence である。従って裸の \(\alpha\) は universal strength ではなく、**operator × consequence class** を固定した座標である。[Pakhomov–Walsh](https://arxiv.org/abs/1805.02095)

## 13. Worm ordinal

worm \(A=\langle n_k\rangle\cdots\langle n_1\rangle\top\) は finite modal syntax である。\(o(A)\) は、GLP provable equivalence で割った worms を \(<_0\) 等で並べた metatheoretic ordinal rank である。

\[
o(A)\quad\not\equiv\quad |T+A^*|
\]

は型の違う対象である。両者を接続するには、各 modality の arithmetic interpretation、worm の consistency/reflection 読み、そして resulting theories に関する reduction/conservation theorem が必要である。GLP\(_\omega\) の closed worms の \(<_0\) order type が \(\varepsilon_0\) であることは PA の \(\varepsilon_0\)-analysis と強く対応するが、その対応自体が provability-algebraic ordinal analysis の成果である。[Joosten](https://arxiv.org/abs/1212.2395)

## 14. Reflection rank

reflection rank は、理論を

\[
T<_\mathrm{RFN}U
\quad\text{iff}\quad
U\text{ proves an appropriate reflection principle for }T
\]

のような relation で順序づけ、その well-founded part における rank を取る。どの reflection class、base、sound theory class を採るかが定義の一部である。

適切な自然理論群では reflection rank と \(|T|_{WO}\) が一致する定理がある。しかし一般には一致せず、reflection rank と proof-theoretic ordinal を無条件に同義語にはできない。[Pakhomov–Walsh](https://arxiv.org/abs/1805.02095)

## 15. Conservation rank / spectrum

理論 \(S\) の情報を

\[
\mathcal C(S)=
(\Pi_1(S),\Pi_2(S),\ldots)
\]

という説明的 profile で見ると、ordinal はその全成分を通常は保存しない。同じ ordinal calibration を持つ theory でも、追加公理が ordinal definition の観測窓に入らない complexity に作用すれば conservation spectrum は異なり得る。

Pakhomov–Walsh の characterization は、適切な second-order setting で \(\Pi^1_1\)-theorems と true \(\Sigma^1_1\) oracle に相対した quotient/order が ordinal analysis と一致することを示す。これは ordinal が「何も見落とさない」のではなく、**どの情報を同一視する quotient かを精密化した結果**である。[Characterizations of Ordinal Analysis](https://arxiv.org/abs/2209.09765)

## 16. Same ordinal = same theory strength?

\[
|T|=|U|
\]

から、一般には次のいずれも自動ではない。

- same theorem set
- mutual interpretability
- same consistency strength
- same \(\Pi_1\)-consequences
- same induction schemas
- same reflection rank

従うのは、まず「採用した ordinal calibration が \(T,U\) を同じ座標へ写した」ことだけである。追加結論には、その calibration と theorem inclusion、conservation、interpretability 等を結ぶ定理が要る。

## 17. Larger ordinal = stronger theory?

\[
|T|<|U|
\]

は、同じ notation system・sound theory class・reduction notion の中では、\(U\) がより長い WO/TI または reflection rank を持つという meaningful な比較になり得る。しかし full theorem inclusion \(T\subseteq U\)、\(U\) による \(T\) の interpretation、あるいは全 complexity での conservativity failure までは含まない。

従って “stronger” と書くなら、**WO-stronger、\(\Gamma\)-reflection-stronger、\(\Pi_n\)-consequence-stronger、interpretability-stronger** のいずれかを指定する。

## 18. “Ordinal scalar” 判定

**判定: S2\*.**

自然な理論群と標準 analysis package では、cut elimination、TI/WO、reflection、worm ordering が橋渡し定理により同じ ordinalへ収束し、ordinal は複数の標準 notions を統合する頑健な一次元 coordinate になる。だが任意の理論、任意の formula class、任意の interpretability/conservation notionを一つにする universal scalar ではない。単独の characterization 内だけなら S1、PA のような収束例まで含めて限定的 S2 と評価する。

## 19. Strength profile V2 との関係

proof-theoretic ordinal は、strength profile の単なる一 component とだけ見ると過小評価である。自然な ordinal analysis では、複数成分を reduction theorem により**圧縮した summary coordinate**である。ただし圧縮前の conservation spectrum、interpretability order、language-sensitive induction strengthを復元できない。

従って前回の V2 は維持するが新 invariant とはしない。標準用語では conservativity spectrum、reflection rank、proof-theoretic reducibility の組がより精密である。

## 20. Interpretability ordering

以下は別 relation である。

| statement | 意味 |
|---|---|
| \(T\) interprets \(U\) | \(U\) の言語・公理を \(T\) 内で translation/model として実現 |
| \(T\vdash\mathrm{Con}(U)\) | 固定 proof predicate に関する consistency statement の証明 |
| \(|T|>|U|\) | 固定 ordinal calibration における順序 |
| \(\mathrm{Th}(U)\subseteq\mathrm{Th}(T)\) | 同じ言語上の deductive inclusion |

自然な系列で相関しても、論理的同値ではない。interpretability は language translation を許す preorder、ordinal comparison は特定 reduction invariant の order である。

## 21. Collapsing functions と notation extension

強い impredicative theory の分析では Veblen hierarchy、Buchholz \(\psi\)-functions、ordinal diagrams などを用いる。これらは、大きな recursive well-ordersを有限構文で制御し、cut reduction/reflection の構造を符号化する道具である。

notation の式が長い、\(\Omega\) や \(\psi\) を含む、という表面的複雑さはそれ自体 strength ではない。必要なのは、comparison algorithm、fundamental sequences、well-foundedness proof、proof reductionとの対応である。同じ actual ordinal に異なる notation systems があり、見た目の巨大さは invariant でない。

## 22. \(\Gamma_0\) の位置

Feferman–Schütte \(\Gamma_0\) は Veblen progression による autonomous/predicative ordinal analysis の標準的 landmark であり、\(\varphi_\alpha(0)=\alpha\) の最初の非零 fixed point として表される。しかし「predicative mathematics の絶対限界」という主張には、何を autonomous acceptance と認めるかという哲学的・形式的選択が入る。

従って \(\Gamma_0\) は特定の predicative progression architecture の sharp calibration として扱い、predicativity 一般の無条件な存在論的境界とはしない。境界を越える別の predicative analysis も提案されている。[Weaver](https://arxiv.org/abs/math/0509244)

## 23. Ordinal analysis と consistency proof

ordinal analysis は consistency proof と同義ではない。

- Gentzen route では ordinal reduction + well-foundedness から relative consistency が得られる。
- modern analyses はしばしば theorem reduction、\(\Gamma\)-conservativity、reflection equivalence を主結果とする。
- ordinal assignment 自体は soundness を与えず、reduction step の正当性と notation の well-foundedness が必要。
- metatheory がどの部分を形式化できるかにより、relative consistency statement の強さが変わる。

## 24. Incompleteness との関係

\(T\) 自身が「自分の ordinal analysis に十分な」well-foundedness principle を証明できるとは限らない。Gentzen 型に \(B+\mathrm{TI}(\alpha)\vdash\mathrm{Con}(T)\) が成り立ち、\(T\) がその全前提を内部証明できれば、Gödel II の制約が現れる。

しかしこれは「\(T\) は \(\alpha\) を理解できない」という意味ではない。\(T\) は各 \(\beta<\alpha\) の fixed instance を証明できても、uniform に境界全体を覆う schema/principle を証明できないことがある。分析対象理論と well-foundedness を正当化する metatheory の level を分ける必要がある。

## 25. Subject / metatheory asymmetry

**判定: A2。**

analyzed theory \(T\)、その proof を符号化する calculus、ordinal notation、reduction theorem、notation の well-foundedness を証明する metatheory は型が異なる。これは Turing–Feferman progression の subject/extension reindexing と同一ではないが、「評価される理論」と「評価を正当化する理論」の区別として ordinal-analysis 全般に安定する architecture feature である。標準 metamathematical level distinction で十分なので A3 ではない。

## 26. Proof architecture P2

ordinal analysis は

\[
(T,\text{calculus},\mathcal O,\Gamma,
\text{reduction},\text{metatheory})
\]

の組で設計される。この tuple を明示することで theorem anatomy → logic anatomy → progression/algebra anatomy → ordinal analysis という横断比較ができる。

**再判定: P2。** 省略された comparison parameters を監査する architecture table として有効だが、既存 ordinal analysis の新しい代替 framework ではない。

## 27. Canonicalization C2

**再判定: C2\*.**

PA、標準 \(\varepsilon_0\)-notations、自然な reflection/worm analyses のような family では、normal form と invariance/bridge theorems が強い canonicalization を与える。しかし arbitrary recursive presentations、弱い理論、異なる reduction notions、異なる consequence classes 全般について一意な ordinal は得られない。GLP worms の C2 は natural provability-algebra fragment 内の canonicalization であり、ordinal analysis 一般へは C2\* として限定される。

## 28. Partial order / preorder stress test

proof-theoretic ordinals は選択した sound natural theory class をしばしば well-order 的に並べるが、全理論を全順序化しない。

- 異なる言語では theorem inclusion 自体が直接定義されない。
- interpretability、consistency strength、\(\Gamma\)-conservation は別々の preorders である。
- independent axioms や人工的 extensions は一つの ordinal observation では比較不能または同値に潰れ得る。
- non-arithmetic theories では accepted notation/reduction package 自体が未確定な場合がある。

従って ordinal order は universal total order ではなく、自然な比較領域と quotient を固定したときに最もよく働く。

## 29. Erasure Test

「strength profile」「proof architecture」「canonicalization」「moving boundary」「fixed/external」「residual」を削除しても、proof-theoretic ordinal、TI、WO、cut elimination、reflection rank、conservation spectrum、interpretability、GLP/worms、ordinal analysis だけで数学的内容は全て記述できる。

失われるのは、既存系列の定理・論理・progression と並べたときに「どの parameter が省略されたか」を一目で監査する教育的見通しである。

**判定: E1。** 技術的情報は失わないが、横断比較の索引を少し失う。

## 30. 最終比較表

| notion | indexed object | ordinal? | what it measures | depends on | canonical? |
|---|---|---:|---|---|---|
| progression length | stage/operator application | yes | operator 固定後の反復座標 | base, operator, notation, limit rule | 同一 progression 内で相対的 |
| recursive notation | finite/recursive syntax | それ自体は no | recursive order の presentation | notation system, comparison rules | normal form があっても system 相対 |
| proof-theoretic ordinal | theory + analysis package | yes | WO/TI/reduction/reflection の supremum/rank | theory class, notation, formula class, metatheory | natural family では高いが一般には限定的 |
| worm ordinal | GLP worm equivalence class | yes | Beklemishev ordering 上の rank | modality set, ordering, logic | GLP fragment 内で高い |
| reflection rank | theory | yes/rank | reflection order における位置 | reflection class, base, soundness domain | 一致定理の範囲でのみ theory ordinal と同じ |
| conservation rank/spectrum | theory pair + consequence class | ordinal または profile | 各 class での保存・還元 | \(\Gamma\), base, operator | 多軸で、単一値への圧縮は相対的 |
| transfinite induction strength | theory + formula class + notation | yes/supremum | 証明可能な TI の長さ | parameters, schema, coding | convention と bridge theorem に相対 |

## 31. Kill criteria

| criterion | result |
|---|---|
| ordinal が reduction notion に相対する | 成立。万能スカラー読みを棄却 |
| same ordinal が deductive equivalence を意味しない | 成立 |
| larger ordinal が universal stronger を意味しない | 成立 |
| progression length と theory ordinal が別物 | 成立 |
| worm ordinal は interpretation theorem 経由 | 成立 |
| conservation spectrum は ordinal が落とす情報を持つ | 成立 |
| interpretability は別 preorder | 成立 |
| standard ordinal analysis が architecture を説明する | 成立。独自語彙は比較索引へ降格 |
| canonicality は natural analysis family に限定 | 成立 |

Negative result を保存する。「the proof-theoretic ordinal」という標準表現を捨てる必要はないが、それを理論に内在する絶対重量と読むことはできない。独自語彙の追加予測力はなく、その役割は省略された相対化パラメータの監査に限られる。

## 32. 最終出力

### A. Proof-theoretic ordinal の核心

- recursive well-orders、TI、proof reductions、reflection iterations を用いて理論を ordinal で校正する。
- ordinal は proof transformation や指定 consequence class の strength を測る。
- 複数 characterization の一致は bridge theorem であり、無条件な定義的一致ではない。
- 自然な理論群では非常に頑健だが、全 deductive information を保持しない。

### B. 何を測っているのか

- 指定 class の transfinite-induction / well-ordering strength
- cut-elimination・normalization の termination measure
- 指定 reflection progression に対する reduction length
- natural theory class 内の reflection/well-order rank
- arithmetic interpretation 下の worm/provability-algebra rank

### C. 何を測っていないのか

- theorem set 全体または axiom inclusion
- mutual interpretability
- 全 formula classes の conservation spectrum
- language-independent な induction/reflection content
- theory strength の universal total order

### D. PA / \(\varepsilon_0\) の正確な意味

- PA proofs の Gentzen reduction は \(\varepsilon_0\) 未満の下降 measure で制御される。
- PA は標準的意味で各 \(\alpha<\varepsilon_0\) までの TI を証明する。
- 境界全体の十分な TI は metatheory で \(\mathrm{Con}(PA)\) を導く。
- \(\varepsilon_0\) は supremum/sharp calibration であり PA の theorem set ではない。
- reflection/worm との一致には別の reduction theorem が要る。

### E. Progression length との違い

- progression length は operator 固定後の stage coordinate。
- theory ordinal は resulting theory を reduction/WO/TI で別途測る値。
- operator complexity により Schmerl 型 ordinal transform が入る。

### F. Worm ordinal との違い

- worm は modal syntax、\(o(A)\) はその equivalence class の rank。
- theory ordinal への接続には arithmetic interpretation が要る。
- reduction/conservation theorem なしに両者は同一でない。

### G. Conservation spectrum との違い

- spectrum は consequence class ごとの保存関係を保持する。
- ordinal は指定 quotient/reduction に沿ってそれを圧縮する。
- same ordinal でも異なる spectrum を排除しない。

### H. Ordinal scalar 判定

**S2\*** — natural analysis families では複数標準 notions を統合する robust coordinate。全 theory strength の universal scalar ではない。

### I. Subject / metatheory asymmetry 判定

**A2** — analyzed theory と reduction/well-foundedness を正当化する metatheory の型の違いは安定した architecture feature。ただし標準 level distinction 以上の新原理ではない。

### J. Proof architecture 再判定

**P2** — theory、calculus、notation、reduction、consequence class、metatheory を比較する監査枠として有効。

### K. Canonicalization 再判定

**C2\*** — PA/GLP 等の natural families では強いが、任意の notation・definition・reduction notion には及ばない。

### L. Erasure Test

**E1** — 独自語彙を消しても数学は失われず、横断比較の見通しだけ少し失われる。

### M. 最も重要な新規観察

1. ordinal が一次元に見えるのは、先に theory class・reduction notion・consequence class を固定して quotient を取った後である。
2. \(PA=\varepsilon_0\) の頑健性は「ordinal の絶対性」ではなく、複数の標準分析を結ぶ bridge theorems の強さである。
3. progression length、worm rank、reflection rank、theory ordinal は同じ ordinal 表記を共有しても、indexed object が異なる。

### N. 次の一手

1. **interpretability / conservativity partial order** — ordinal が潰す非全順序的情報を直接比較できる。
2. **induction vs reflection anatomy** — PA fragments の ordinal calibration が formula complexity とどう交換されるかを精密化できる。
3. **ordinal analysis of PA / predicativity** — \(\varepsilon_0\) と \(\Gamma_0\) で canonicality の成立範囲を具体的に比較できる。

## 参考資料

- [Stanford Encyclopedia of Philosophy, “Proof Theory”](https://plato.stanford.edu/entries/proof-theory/) — Gentzen analysis、PA、\(\varepsilon_0\)、transfinite induction。
- [Fedor Pakhomov and James Walsh, “Reflection Ranks and Ordinal Analysis”](https://arxiv.org/abs/1805.02095) — well-ordering ordinal、reflection rank、一致範囲と非一致例。
- [James Walsh, “Characterizations of Ordinal Analysis”](https://arxiv.org/abs/2209.09765) — ordinal analysis がどの theory quotient/order を測るかの抽象 characterization。
- [Joost J. Joosten, “Ordinal Analysis Beyond First-Order Arithmetic”](https://arxiv.org/abs/1212.2395) — GLP、worms、\(\varepsilon_0\)、reflection-based ordinal analysis。
- [Nik Weaver, “Predicativity beyond \(\Gamma_0\)”](https://arxiv.org/abs/math/0509244) — \(\Gamma_0\) を predicativity の無条件な絶対限界としないための反対側の検討。


# Iterated consistency progression と uniform reflection progression の比較
## special stress test

本稿でいう「strength vector」「moving boundary」「proof architecture」「残差」「閉包」「外部化」は比較用の解剖的メタ記述であり、標準 proof theory の用語ではない。技術的記述では、iterated consistency、uniform reflection、conservation、reduction property、Schmerl formulas、reflection rank、provability algebra、proof-theoretic ordinal を優先する。

今回の問いは「どちらが強いか」ではなく、**どの比較関係・どの consequence class・どの operator の下で強いか**である。

## 0. 比較対象の固定

基礎理論を

\[
B:=EA=I\Delta_0+\exp
\]

とし、\(T\) は elementary に公理化された \(EA\) の拡張とする。標準 proof predicate を固定し、必要な箇所では \(T\) の整合性・算術的 soundness を外部仮定として明示する。

### A. consistency progression

\[
C_0(T):=T,
\]

\[
C_{\alpha+1}(T):=
C_\alpha(T)+\operatorname{Con}(C_\alpha(T)),
\]

\[
C_\lambda(T):=
\bigcup_{\beta<\lambda}C_\beta(T).
\]

### B. uniform reflection progression

\[
R^\Gamma_0(T):=T,
\]

\[
R^\Gamma_{\alpha+1}(T):=
R^\Gamma_\alpha(T)+
\operatorname{RFN}_\Gamma(R^\Gamma_\alpha(T)),
\]

\[
R^\Gamma_\lambda(T):=
\bigcup_{\beta<\lambda}R^\Gamma_\beta(T).
\]

ここで実順序数 \(\alpha\) は略記である。progression を効果的な形式理論として扱うには recursive ordinal notation、各 stage の一様な axiom numeration、successor／limit clause を固定する必要がある。

主比較では

\[
\Gamma=\Sigma^0_2
\]

を採用する。理由は、標準的に

\[
EA+\operatorname{RFN}_{\Sigma^0_2}(EA)
\equiv I\Sigma_1
\]

となり induction strength との接続が明瞭であり、GLP の標準解釈では一段高い consistency／reflection operator を普通の consistency の \(\omega\)-反復へ \(\Pi^0_1\)-保存的に還元する reduction property と直接比較できるからである。[Kolmakov](https://arxiv.org/abs/1907.06464)

## 1. Formula class \(\Gamma\)

Uniform reflection は、各 \(\varphi(x)\in\Gamma\) について

\[
\forall x\,
\bigl(
\operatorname{Pr}_S(
\ulcorner\varphi(\dot x)\urcorner)
\to\varphi(x)
\bigr)
\]

を加える schema である。

| class | reflection が主張する外部的正しさ | 注意点 |
|---|---|---|
| \(\Sigma^0_1\) | \(S\) の \(\Sigma_1\)-soundness に対応 | 単なる consistency より強い。witness／nonstandard proof code が関与 |
| \(\Pi^0_1\) | \(S\) の \(\Pi_1\)-soundness に対応 | \(\Sigma_1\) 版との同一視には別定理が必要 |
| \(\Sigma^0_n\) | \(\Sigma_n\) formulas の uniform reflection | \(n\) と base により induction hierarchy と接続 |
| \(\Pi^0_n\) | \(\Pi_n\) formulas の uniform reflection | Schmerl formulas で complexity 間を比較しやすい |

Class inclusion \(\Gamma\subseteq\Delta\) があるときは、同じ \(S\) について

\[
S+\operatorname{RFN}_\Gamma(S)
\subseteq
S+\operatorname{RFN}_\Delta(S)
\]

という axiom／theorem inclusion がある。ところが \(\Sigma_n\) と \(\Pi_n\) は単純な包含関係ではない。双対性だけから reflection extensions の同値や全順序性を結論してはならない。

主比較を \(\Sigma_2\) としつつ、Schmerl formula を扱う節では文献の \(\Pi_n\)-reflection notation に切り替え、その都度規約を明示する。

## 2. Consistency はどの reflection instance か

\[
\operatorname{Con}(S)
\equiv
\neg\operatorname{Pr}_S(\ulcorner\bot\urcorner)
\]

は古典論理で

\[
\operatorname{Pr}_S(\ulcorner\bot\urcorner)\to\bot
\]

と同値である。従って \(\bot\) に対する single local reflection instance である。

しかし uniform reflection は、変数を含む formula の numeral substitution を proof predicate 内で coding し、全ての \(x\)—非標準モデルでは非標準元を含む—について一つの内部全称文を要求する。従って

\[
\text{consistency progression}
\neq
\text{weak uniform reflection progression}
\]

である。Consistency は reflection family の最小の closed-instance の一つだが、uniformity、parameters、formula complexity、induction interaction を含まない。

## 3. Strength axes の固定

| strength axis | consistency progression | uniform reflection progression |
|---|---|---|
| axiom inclusion | successor ごとに一つの \(\Pi_1\) consistency sentence | successor ごとに \(\Gamma\)-uniform reflection schema |
| theorem inclusion | operator と stage presentation に相対 | \(\Gamma\) が \(\bot\) を含めば一段目で consistency extension を包含。高 stage は形式化を要する |
| consistency strength | 各 stage が直前 stage の consistency を加える | 各 reflection schema は少なくとも直前 stage の consistency を含む |
| \(\Pi_1\)-strength | iterated consistency が直接増やす主軸 | 強い一段が弱い \(\omega\)-反復と \(\Pi_1\)-conservative になる場合がある |
| \(\Pi_n\)-strength | 長さだけでは決まらない | formula class と reduction theorem に強く依存 |
| induction strength | 一般に induction schema を直接追加しない | 例: \(EA+\mathrm{RFN}_{\Sigma_{n+1}}(EA)\equiv I\Sigma_n\)（\(n\ge1\)） |
| reflection strength | \(\bot\) への single local instance を反復 | formula class 全体への uniform schema を反復 |
| conservation profile | 比較する \(\Pi_n\) ごとに別 | reduction／Schmerl formulas が class-relative profile を与える |
| proof-theoretic ordinal | base、notation、測定定義に相対 | base、\(\Gamma\)、iteration、測定定義に相対 |
| progression length | operator 固定後の coordinate | 同じ。異なる operator 間の universal strength 単位ではない |

この表の各行は異なる preorder または calibration を与える。全行を一つの “strength” へ射影する標準的な万能尺度はない。

## 4. 通常 anatomy

### 4.1 comparison_name

Iterated consistency progression と \(\Sigma_2\)-uniform reflection progression の多軸比較。

### 4.2 domain

一階算術の proof theory、reflection principles、Turing–Feferman progressions、conservation、ordinal analysis。

### 4.3 systems_compared

\[
(C_\alpha(T))_\alpha
\quad\text{と}\quad
(R^{\Sigma_2}_\alpha(T))_\alpha.
\]

\(\Sigma_1,\Pi_1,\Sigma_n,\Pi_n\) reflection progressions は formula-class sensitivity の比較対象とする。

### 4.4 assumptions

- A: base theory \(EA\) とその算術言語
- B: elementary／c.e. に公理化された \(T\supseteq EA\)
- C: 各 stage の standard provability predicate
- D: consistency operator \(S\mapsto S+\operatorname{Con}(S)\)
- E: uniform reflection operator \(S\mapsto S+\operatorname{RFN}_\Gamma(S)\)
- F: formula class \(\Gamma\)
- G: recursive ordinal notation と effective stage recursion
- H: successor／limit clauses
- I: 比較する consequence class \(\Pi_n\) 等
- J: strictness、soundness、ordinal calibration を論じる metatheory

### 4.5 hypothesis_levels

- A: ambient
- B: object / ambient
- C: definitional / object
- D: definitional / object
- E: definitional / object
- F: definitional — reflection scope の定義
- G: ambient / definitional
- H: definitional
- I: definitional — comparison relation の一部
- J: background

### 4.6 operator_types

- D: sentence-valued、local、parameter-free、\(\Pi_1\)
- E: schema-valued、uniform、parameter-sensitive、complexity-indexed
- successor: theory-extension operator
- limit: effective union operator

### 4.7 architecture_roles

- A–C: base and proof-predicate fixation
- D: stage-relative consistency transfer
- E: formula-class-relative uniform reflection
- F: operator complexity control
- G–H: transfinite iteration control
- I: conservation lens
- J: soundness／well-foundedness／strictness verification

### 4.8 comparison_targets

Theorem inclusion、consistency strength、\(\Pi_n\)-consequences、induction、reflection scope、conservation profile、proof-theoretic ordinal、iteration length を別々に比較する。

### 4.9 blocked_confusions

- D と E の区別が「一段」の同一視を防ぐ。
- F が formula classes の違いを隠す道を塞ぐ。
- G–H が ordinal value と stage presentation の混同を防ぐ。
- I が theory equality と \(\Pi_n\)-conservation の混同を防ぐ。
- J が object theory 内の主張と外部 soundness judgment の混同を防ぐ。

### 4.10 what_fails_if_operator_changed

- consistency を uniform reflection に換えると、同じ stage 数でも parameters、substitution、formula complexity、induction consequences が追加される。
- \(\Gamma\) を変えると、同じ reflection iteration length でも theorem set と conservation profile が変わる。
- base \(EA\) を \(I\Sigma_1\) 等へ変えると、既に利用可能な induction、coding、reflection equivalences が変わる。
- local reflection に換えると uniform quantification と nonstandard elements への一括適用が失われる。
- limit union の presentation を変えると、effective axiomatizability と stage proof predicate が変わり得る。

### 4.11 what_reappears

- operator を弱める: **R1** — 同じ consequence を得るために長い iteration が必要になる場合がある。
- formula class を狭める: **R1** — higher-complexity consequences が未決定のまま残る。
- uniformity を外す: **R1** — nonstandard instances／parameter-uniformity の自由度が戻る。
- consequence class を変える: **R1** — 以前の conservation equivalence が消える。

明示的補正項 R2 ではなく、比較 profile の変化である。全体判定は RX とする。

### 4.12 proof_resources

- formalized provability と partial truth predicates
- Gödel coding／numeral substitution
- Gödel II と Löb theorem
- reflexive induction
- reduction property
- Schmerl formulas
- Leivant–Ono／Kreisel–Lévy 型 reflection–induction equivalences
- provability algebra／GLP／reflection calculus
- ordinal notation と conservation theorem

これらは progression の assumptions ではなく、二つの progression の関係を証明する resources である。

### 4.13 comparison_style

**保存性プロファイル比較型**。

これは説明ラベルであり、標準 invariant の名称ではない。

### 4.14 theorem_vs_progression_comment

Progression の定義が固定するのは base、operator、formula class、stage recursion である。reduction theorem や Schmerl formula は、定義された progressions がどの consequence class で一致するかを外部から示す。両者を混同すると、一段の強い operator と多段の弱い operator が theory equality で交換できるかのような誤読が生じる。

### 4.15 short_comment

「同じ一段」は operator を固定しない限り数学的情報が薄い。「同じ \(\alpha\)」も progression の座標が同じだけであり、operator complexity を含まない。比較の実体は theorem inclusion、class-relative conservation、reflection／induction equivalence にある。

## 5. Operator type の違い

| feature | \(C(S)=S+\operatorname{Con}(S)\) | \(R_\Gamma(S)=S+\operatorname{RFN}_\Gamma(S)\) |
|---|---|---|
| logical form | 一つの sentence | formula ごとの schema |
| reflection scope | \(\bot\) への single local reflection | \(\Gamma\)-formulasへの uniform reflection |
| parameters | なし | あり得る |
| substitution coding | 不要または最小 | \(\varphi(\dot x)\) の coding が本質 |
| formula complexity | consistency sentence は通常 \(\Pi_1\) | \(\Gamma\) により可変 |
| nonstandard models | 非標準 proof code の不存在を一文で主張 | 非標準 \(x\) を含む全 domain elements に内部量化 |
| induction interaction | 直接は induction schema でない | 特定 class では induction fragments と同値 |
| semantic reading | external に「\(S\) は無矛盾」 | external に「\(S\) は \(\Gamma\)-sound」 |

## 6. 一段 vs 一段

同じ \(T\) について

\[
T+\operatorname{Con}(T)
\quad\text{と}\quad
T+\operatorname{RFN}_\Gamma(T)
\]

を比較する。

### Q1. どちらが stronger か

\(\Gamma\) が \(\bot\) を含む通常の class なら、reflection schema は \(\operatorname{Con}(T)\) を含むため

\[
T+\operatorname{Con}(T)
\subseteq
T+\operatorname{RFN}_\Gamma(T)
\]

が成り立つ。一段目では literal axiom instance として比較できる。

### Q2. どの consequence class で stronger か

Full theorem inclusion では reflection extension が上である。しかし「どの程度上か」は \(\Gamma\) と consequence class に依存する。主例では

\[
EA+\operatorname{RFN}_{\Sigma_2}(EA)
\equiv I\Sigma_1,
\]

なので induction consequences まで得る。単なる \(EA+\operatorname{Con}(EA)\) と同じではない。

### Q3. Full theorem inclusion はあるか

一段目にはある。高 stage についても、standard monotone presentations の下では reflection progression が consistency progression を theorem-wise に支配することを帰納的に示せるが、各 stage の proof predicate と notation recursion を固定する必要がある。Literal axiom inclusion と deductive inclusion は区別する。

### Q4. Conservation theorem はあるか

ある。ただし一般に reflection extension が consistency extension 一段に conservative なのではない。強い reflection 一段を、弱い consistency／reflection の**多段反復**へ還元する形が中心である。

### Q5. \(\Gamma\) によって変わるか

大きく変わる。\(\Sigma_1\)-soundness、\(\Pi_1\)-soundness、\(\Sigma_2\)-reflection、full reflection は異なる schema であり、同じ「reflection 一段」ではない。

## 7. 一段 consistency vs 多段 consistency

\[
C_1(T)=T+\operatorname{Con}(T)
\]

に対し、

\[
C_k(T),\qquad
C_\omega(T)=\bigcup_{k<\omega}C_k(T)
\]

を考える。

- finite \(k\): 各 successor が直前 theory の新しい consistency sentence を加える。
- \(\omega\): 全有限 iterate を含む effective union で、単一の「\(\omega\) 回目の consistency axiom」を加えるのではない。
- transfinite: recursive notation と limit union に沿って反復する。長さだけで strictness や final strength は決まらない。

適切な consistency assumptions の下で

\[
C_k(T)\nvdash\operatorname{Con}(C_k(T)),
\qquad
C_{k+1}(T)\vdash\operatorname{Con}(C_k(T))
\]

という stage-relative strictness がある。しかしこれは operator を固定した内部比較であり、uniform reflection progression との横断尺度にはならない。

## 8. 一段 uniform reflection vs 多段 consistency

主例では、GLP の標準算術解釈で \(\langle0\rangle\) を ordinary consistency、\(\langle1\rangle\) を一段高い consistency／対応する \(\Sigma_2\)-uniform reflection と読む。

\[
Q_0^0(\top):=\langle0\rangle\top,
\]

\[
Q_0^{k+1}(\top)
:=
\langle0\rangle
\bigl(
\top\land Q_0^k(\top)
\bigr).
\]

標準 reduction property は、概略

\[
EA+\langle1\rangle\top
\]

が

\[
EA+\{Q_0^k(\top):k<\omega\}
\]

に対して \(\Pi_1\)-conservative であることを述べる。右辺は ordinary consistency の有限反復全体に対応する。従って、一段の \(\Sigma_2\)-reflection／1-consistency は、その \(\Pi_1\)-profile に関して ordinary consistency の \(\omega\)-iteration へ還元される。[Joosten](https://arxiv.org/abs/1212.2395)

これは

\[
EA+\operatorname{RFN}_{\Sigma_2}(EA)
=
C_\omega(EA)
\]

という theory equality ではない。左辺は \(I\Sigma_1\) と deductively equivalent であり、右辺との一致は指定された \(\Pi_1\)-consequences に限られる。

## 9. Reduction property の算術的読替え

一般の \(n\) について

\[
EA+\langle n+1\rangle A
\]

は

\[
EA+\{Q_n^k(A):k<\omega\}
\]

に対して \(\Pi_{n+1}\)-conservative となる標準形を採用する。

ここで交換可能なのは

\[
\text{強い operator 一回}
\quad\leftrightarrow\quad
\text{弱い operator の }\omega\text{-反復}
\]

そのものではなく、

\[
\text{指定された }\Pi_{n+1}\text{-consequences}
\]

である。Full theorem sets、induction schema、higher-complexity consequences は一致を保証されない。

## 10. Conservation profile

説明上、理論 \(S\) の profile を

\[
\mathcal C(S):=
\bigl(
\operatorname{Th}_{\Pi_1}(S),
\operatorname{Th}_{\Pi_2}(S),
\operatorname{Th}_{\Pi_3}(S),
\ldots
\bigr)
\]

と書ける。これは新定義ではなく、各 arithmetical class における consequence sets を並べたメタ表記である。

標準 proof theory には既に conservativity spectrum、conservation profile、reflection rank、provability algebra というより精密な道具がある。特に \(RC^\nabla\) は、複雑度ごとの theory fragments と reflection operators を一つの algebra に記録する。[Beklemishev](https://arxiv.org/abs/1703.09314)

重要なのは、二理論が

\[
\operatorname{Th}_{\Pi_1}(S)
=
\operatorname{Th}_{\Pi_1}(U)
\]

でも deductively equivalent とは限らないことである。同じ \(\Pi_1\)-座標と異なる \(\Pi_2\)-座標を持ち得る。

## 11. “Strength vector” 仮説

「strength vector」は、theorem inclusion、consistency、各 \(\Pi_n\)-consequence set、induction、reflection rank、ordinal calibration を一つの一覧として可視化する比較ラベルとして有効である。

しかし数学的には、各成分は同じ数値空間の coordinate ではない。Theorem set は集合、conservation は preorder、proof-theoretic ordinal は選択した reduction に相対する ordinal、induction strength は schema inclusion／conservation で測られる。「vector」の加法・スカラー倍・距離はない。

**判定: V2。** conservation／reflection／induction を横断比較する実用的なメタ表現として有効だが、既存の conservativity spectrum 等を超える V3 の invariant ではない。

## 12. Ordinal length と strength の非同一性

同じ notation \(\alpha\) を使っても

\[
C_\alpha(T)
\quad\text{と}\quad
R^\Gamma_\alpha(T)
\]

は一般に同じ theory strength を持たない。

- operator dependence: Con と RFN は一段の内容が違う。
- formula-class dependence: \(\Gamma\) が違えば reflection scope が違う。
- base dependence: base が既に持つ induction／reflection が違う。
- conservation-class dependence: \(\Pi_1\) で同じでも \(\Pi_2\) 以上で異なり得る。

\(\alpha\) は operator を反復する coordinate であり、operator の強さを符号化しない。

## 13. 同じ ordinal に異なる operator を載せる

\[
C^\alpha(T)
\quad\text{と}\quad
R^\alpha_\Gamma(T)
\]

の上付き \(\alpha\) が同じであることは、同じ長さの recursion を使うことしか示さない。Operator を

\[
\operatorname{Con}
\to
\operatorname{RFN}_{\Sigma_2}
\to
\operatorname{RFN}_{\Sigma_3}
\]

と変えれば一 step の proof-theoretic content が変わる。

従って ordinal は progression の「長さ」を示すが、operator complexity を含まない。異なる operator 間の校正には reduction theorem や Schmerl formula が必要であり、同じ \(\alpha\) という事実だけでは足りない。

## 14. Proof-theoretic ordinal の位置

| notion | 対象 | 何を測るか |
|---|---|---|
| progression length \(\alpha\) | stage recursion | operator の反復長 |
| proof-theoretic ordinal of \(S\) | formal theory | 採用した well-ordering／reduction notion による strength |
| worm ordinal \(o(A)\) | GLP worm 同値類 | Beklemishev ordering の rank |
| reflection rank | theory と reflection relation | 反射 progression における相対位置 |
| conservation rank／spectrum | theory fragments | complexity ごとの consequence strength |

Proof-theoretic ordinal は theory strength の有力な calibration だが万能スカラーではない。同じ ordinal assignment を持つ理論が、言語、induction、function symbols、higher-complexity consequences まで同じとは限らない。また progression length と resulting theory の proof-theoretic ordinal は別の ordinal であり得る。

## 15. Induction strength

標準的な Leivant–Ono 型対応として、\(n\ge1\) について

\[
EA+\operatorname{RFN}_{\Sigma_{n+1}}(EA)
\equiv I\Sigma_n
\]

がある。また full uniform reflection では

\[
EA+\operatorname{RFN}(EA)
\equiv PA
\]

という Kreisel–Lévy 型対応がある。[reflection–induction の標準対応](https://arxiv.org/abs/1907.06464)

これらは「reflectionを増やす＝inductionを増やす」という無条件な原理ではない。

- base が \(EA\) である。
- reflection の formula class が指定されている。
- schema の形式と language が固定されている。
- deductive equivalence なのか class-relative conservation なのかを区別する。

Consistency iteration は induction axiomを直接加えないが、長い反復が低 complexity consequences について induction fragment と一致する場合がある。その一致は reduction／conservation theorem の内容であり、operator 定義から自動的には出ない。

## 16. Local vs uniform の質的差

Local reflection schema は各 standard closed sentence \(\varphi\) に対して

\[
\operatorname{Pr}_T(\ulcorner\varphi\urcorner)\to\varphi
\]

を加える。Uniform reflection は formula \(\varphi(x)\) ごとに

\[
\forall x
\bigl(
\operatorname{Pr}_T(\ulcorner\varphi(\dot x)\urcorner)
\to\varphi(x)
\bigr)
\]

を加える。

外部から見ると uniform formula は standard numeral instances を全て含むが、非標準モデル内では全称量化が非標準元まで及ぶ。従って uniform reflection は local instances の単なる外部的な集合ではなく、substitution coding、parameters、nonstandard elements、induction／collection と相互作用する質的に異なる schema である。

## 17. Same stage count stress test

有限 \(k\) について

\[
C_k(T)
\quad\text{と}\quad
R^\Gamma_k(T)
\]

を比べても、「どちらも \(k\) 段」は operator の適用回数が同じことしか示さない。一段目から

\[
\operatorname{Con}(T)
\quad\text{対}\quad
\operatorname{RFN}_\Gamma(T)
\]

という質的差があるため、cross-operator strength measure にはならない。

**判定: N1。** stage count は operator、base、formula class を固定した progression 内の座標としてのみ有効。

## 18. Same ordinal length stress test

同じ \(\alpha\) を使うことも、有限 \(k\) の場合を transfinite に拡張しただけである。Operator を固定すれば \(\alpha\) は progression coordinate として重要だが、operator 間比較では Schmerl-type re-calibration

\[
\alpha\mapsto\omega_m(\alpha)
\]

のような変換が必要になる。同じ \(\alpha\) 自体が校正を与えるわけではない。

**判定: O1。** ordinal length は operator 固定時の progression coordinate。Operator 間の部分校正は可能だが、「同じ length」が比較尺度になる O2 ではない。

## 19. GLP / worms との対応

| proof-theoretic item | GLP / worm representation |
|---|---|
| ordinary consistency | \(\langle0\rangle\) 型 |
| stronger graded consistency／reflection | \(\langle n\rangle\) 型 |
| iteration depth | worm nesting |
| operator complexity | modality index \(n\) |
| mixed progression | mixed worm |
| \(\Pi_{n+1}\)-conservation | reduction property／reflection calculus |
| theory stage | arithmetic interpretation を入れた後にのみ特定 |
| ordinal calibration | worm ordering／ordinal assignment |

前回判定 C2 のとおり、worms は natural reflection fragments を normal form 化する。しかし modality index、worm depth、theory stage、progression ordinal length、consequence class は別々の index である。

## 20. Schmerl formulas

ここでは Pakhomov–Walsh の notation に従う。\(R^\alpha_{\Pi^0_k}(EA^+)\) を、\(\Pi^0_k\)-uniform reflection を \(\alpha\) 回反復した progression とする。また

\[
\omega_0(\alpha):=\alpha,
\qquad
\omega_{m+1}(\alpha):=\omega^{\omega_m(\alpha)}.
\]

標準的な Schmerl formula の一形は

\[
R^\alpha_{\Pi^0_{n+m}}(EA^+)
\equiv_{\Pi^0_n}
R^{\omega_m(\alpha)}_{\Pi^0_n}(EA^+).
\]

ここで \(\equiv_{\Pi^0_n}\) は同じ \(\Pi^0_n\)-consequences を持つことを表し、deductive equivalence ではない。[Pakhomov & Walsh, Theorem 4.1](https://arxiv.org/abs/1805.02095)

この式は、

\[
\text{高 complexity operator の短い反復}
\]

を

\[
\text{低 complexity operator の長い反復}
\]

へ consequence-class-relative に変換する。Operator level と iteration length は独立だが無関係ではなく、Schmerl formula が両者の交換率を指定する。

## 21. Progression path dependence

同じ \(\Pi_n\)-consequence profile へ

- 高い operator を少数回
- 低い operator を多数回
- mixed operators

で到達することがある。しかしこれは path independence ではない。

\[
S\equiv_{\Pi_n}U
\]

から

\[
S=U
\quad\text{または}\quad
S\equiv U
\]

は従わない。正確な語は **consequence-class-relative equivalence／conservation** である。Higher-complexity consequences、induction schema、proof lengths、interpretability profile が異なる可能性は残る。

## 22. “Distance” 仮説の禁止

Theory 間の「距離」「strength量」「guarantee量」「closure量」は導入しない。Theorem inclusion や interpretability は preorder、conservation は formula class に相対する関係、ordinal rank は選択した well-ordering に相対する。共通 metric は与えられていない。

「一段分遠い」「\(\omega\) だけ強い」という表現は、operator と ordinal calibration を固定した局所的略記に限る。

## 23. “Strength vector” と標準概念

| proposed axis | standard concept |
|---|---|
| complexity ごとの consequences | conservativity spectrum／conservation profile |
| ordinal による校正 | proof-theoretic ordinal／reflection rank |
| theory 間の翻訳可能性 | interpretability ordering |
| consistency の反復 | Turing progression／consistency strength |
| operator の相互作用 | provability algebra／GLP／reflection calculus |
| induction fragments | induction hierarchy と conservation theorems |

従って “strength vector” はこれらを一枚に並べる索引として V2 だが、新しい invariant ではない。標準概念は各 coordinate の型と比較関係を既に区別している。

## 24. Partial order stress test

固定言語で theorem inclusion を使えば theories は inclusion preorder をなす。しかし別々の測定を入れると、一つの全順序にはならない。

- \(S\equiv_{\Pi_1}U\) でも full theorem inclusion は一方向または非同値であり得る。
- \(\Gamma\subseteq\Delta\) なら対応する reflection extensions は比較しやすいが、非包含な \(\Sigma_n,\Pi_n\) classes は追加の conservation theorem なしに並べられない。
- 同じ proof-theoretic ordinal は full deductive equivalence を意味しない。
- Interpretability、consistency strength、\(\Pi_n\)-conservation は別の preorders を与える。

従って「全 theories が本質的に incomparable」と誇張する必要はないが、**どの preorder かを指定しない stronger は未定義に近い**。

## 25. Proof architecture P2 の再検査

今回の strength profile は

\[
\text{base}
+\text{operator kind}
+\text{formula class}
+\text{iteration length}
+\text{consequence class}
\]

に依存する。この tuple を可視化する点で proof architecture は横断比較に有効である。

しかし reduction property、Schmerl formulas、conservativity spectra、provability algebra が、その相互作用を既に形式的に記述する。

**再判定: P2。** 複数の標準比較軸を取り違えない architecture table として有効。新 framework の P3 ではなく、P1 へ下げるほど単なる装飾でもない。

## 26. Moving boundary M2* の再検査

各 stage が直前 stage の consistency／reflection を採用し、自身について同じ principle を自動的には持たない、という stage-relative shift は残る。

しかし consistency progression と uniform reflection progression の strength 差を決める主因は、

- operator kind
- formula class
- iteration length
- consequence class

である。Moving boundary は stage recursion を要約するが、二 progression の比較や reduction rate を与えない。

**再判定: M1。** stage shift の教育的要約としてのみ保持し、strength comparison の M2\* 軸から降格する。

## 27. Residual RX

Consistency remainder、unproved reflection instances、higher \(\Pi_n\)-consequences、next stage、induction deficit は異なる型である。「残差」と一括すると comparison lens が消える。

**判定: RX — residual vocabulary not useful here.**

## 28. Erasure Test

「strength vector」「moving boundary」「proof architecture」「residual」「閉包」「外部化」を削除しても、

- consistency progression
- uniform reflection progression
- theorem inclusion
- reduction property
- Schmerl formulas
- conservativity spectrum
- induction hierarchy
- proof-theoretic ordinal
- provability algebra／GLP／worms

だけで数学的差分はすべて記述できる。

失われるのは、既存 stress tests の用語を跨いで「どの軸を省略したか」を素早く発見する教育的チェックリストである。

**判定: E1。** 技術内容は失われず、横断的な監査視点だけが少し失われる。

## 29. 最終比較表

| comparison | consistency | uniform reflection | same? | comparison notion |
|---|---|---|---|---|
| one step | 一つの \(\operatorname{Con}(T)\) | \(\Gamma\)-schema 全体 | no | theorem inclusion、reflection scope |
| finite iteration | \(k\) 回の stage-relative consistency | \(k\) 回の class-relative reflection | no | operator-relative stage count |
| \(\omega\)-iteration | 全有限 consistency iterates の union | 全有限 uniform-reflection iterates の union | no | effective union、conservation |
| same ordinal length | Con operator を \(\alpha\) 回 | RFN operator を \(\alpha\) 回 | no | 同じ recursion coordinate のみ |
| \(\Pi_1\)-consequences | ordinary consistency iteration が中心 | 強い一段と弱い \(\omega\)-iterationが一致する場合 | sometimes profile-equivalent | \(\Pi_1\)-conservation |
| \(\Pi_n\)-consequences | operator／length に依存 | \(\Gamma\)、Schmerl変換に依存 | theorem-dependent | \(\Pi_n\)-conservation |
| induction strength | 直接 schema を追加しない | \(EA+\mathrm{RFN}_{\Sigma_{n+1}}(EA)\equiv I\Sigma_n\) | no | deductive equivalence／conservation |
| ordinal strength | iteration notation と resulting ordinal は別 | 同様。operator level で変わる | no universal equality | ordinal analysis |
| GLP representation | \(\langle0\rangle\) と nesting | \(\langle n\rangle\)、mixed worms | related, not identical | provability algebra／reduction |

## 30. Kill criteria

| criterion | result |
|---|---|
| 1. strength vector は conservativity spectrum の言い換え | 技術的には成立。V2 の比較索引に限定 |
| 2. stage count は operator 固定時にしか意味がない | 成立。N1 |
| 3. ordinal length は operator strength を含まない | 成立。O1 |
| 4. reduction／Schmerl が operator×iteration tradeoff を精密化 | 成立。独自語彙を降格 |
| 5. proof-theoretic ordinal は万能一軸でない | 成立 |
| 6. proof architecture は reflection calculus の整理以上でない | 技術的には成立。P2 の横断表に限定 |
| 7. moving boundary より conservation relation が重要 | 成立。M1へ降格 |
| 8. residual vocabulary は不要 | 成立。RX |

Negative result を保存する。今回最も有効だった独自表現は「strength vector」そのものではなく、比較軸を省略しないための profile table である。その数学的内容は conservativity spectrum と既存の複数 preorders に吸収される。

## 31. 最終出力

### A. Consistency progression の核心

- 各 successor で直前 theory の consistency sentence 一つを加える。
- Consistency は \(\bot\) に対する single local reflection instance である。
- Iteration length は operator 固定後の stage coordinate である。
- 主に consistency／低 complexity consequences の fine structure を作る。

### B. Uniform reflection progression の核心

- Formula class \(\Gamma\) に相対する uniform reflection schema を反復する。
- Parameters、numeral substitution、nonstandard elements が関与する。
- Formula class により induction、reflection、conservation strength が変わる。
- Consistency progression の単なる「強い版」一軸では記述できない。

### C. 最大の違い

1. sentence 対 schema。
2. single local reflection 対 uniform parameter reflection。
3. fixed \(\Pi_1\) consistency 対 formula-class-dependent operator。
4. inductionとの直接接続の有無。
5. 同じ stage length でも consequence profile が異なる。

### D. 一段 vs 多段

1. Uniform reflection 一段は consistency 一段を通常包含する。
2. 主例の \(\Sigma_2\)-reflection 一段は \(I\Sigma_1\) と同値である。
3. その \(\Pi_1\)-consequences は ordinary consistency の \(\omega\)-iterationへ還元できる。
4. これは theory equality ではない。
5. Higher consequence classes では別の比較が必要である。

### E. Reduction / Schmerl の意味

1. Operator complexity と iteration length の交換率を与える。
2. 高い一段／短反復を低い長反復へ移す。
3. 等価性は指定した \(\Pi_n\)-consequences に相対する。
4. Same stage count や same ordinal length が universal measure でないことを形式的に示す。

### F. Same stage count 判定

**N1** — operator 固定時のみ有効。

### G. Same ordinal length 判定

**O1** — operator 固定時の progression coordinate。Cross-operator calibration は別定理を要する。

### H. Strength vector 判定

**V2** — 多軸比較の実用的メタ表現。ただし conservativity spectrum 等の標準概念を超える invariant ではない。

### I. Proof architecture 再判定

**P2** — base、operator、formula class、length、consequence class を分離する比較枠として有効。

### J. Moving boundary 再判定

**M1** — stage shift の教育的要約に降格。Progression 比較では conservation relation の方が重要。

### K. Residual 判定

**RX** — 異なる consequence deficits を一括する利益がない。

### L. Erasure Test

**E1** — 数学的内容はすべて標準語彙で残り、横断監査の見通しだけ少し失われる。

### M. 最も重要な新規観察

1. Theory strength は一つの数でなく、複数の標準 preorders／conservation profiles を選び分けて比較する対象である。
2. Operator complexity と iteration length は独立変数だが、reduction property と Schmerl formulas が consequence-class-relative な交換率を与える。
3. 「同じ段数」「同じ ordinal length」は operator を固定しない限り strength 情報をほぼ持たない。

### N. 次の一手

1. **proof-theoretic ordinal anatomy** — progression length、reflection rank、worm ordinal、theory ordinal の非同一性を単独で精査する。
2. **interpretability / conservativity partial order** — 複数の strength preorders が一致・分岐する条件を比較する。
3. **induction vs reflection anatomy** — \(I\Sigma_n\equiv EA+\mathrm{RFN}_{\Sigma_{n+1}}(EA)\) の条件と conservation consequences を分解する。

## 参考資料

- [L. D. Beklemishev, Reflection Principles and Provability Algebras in Formal Arithmetic](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=1401&what=fullteng)
- [J. J. Joosten, \(\Pi^0_1\)-Ordinal Analysis Beyond First-Order Arithmetic](https://arxiv.org/abs/1212.2395)
- [F. Pakhomov and J. Walsh, Reflection Ranks and Ordinal Analysis](https://arxiv.org/abs/1805.02095)
- [L. D. Beklemishev, Reflection Calculus and Conservativity Spectra](https://arxiv.org/abs/1703.09314)
- [E. Kolmakov, Local Reflection, Definable Elements and 1-Provability](https://arxiv.org/abs/1907.06464)

## 総括

今回の仮説は限定付きで支持される。Proof-theoretic strength を単一スカラーとして扱うより、theorem inclusion、consistency、\(\Pi_n\)-consequences、induction、reflection、ordinal calibrationを分ける方が正確である。

しかし「strength vector」を新概念にする必要はない。標準 proof theory は conservativity spectra、reflection ranks、interpretability、provability algebras、Schmerl formulas によって、各軸の型と交換関係を既により精密に記述している。今回の独自表現の役割は、一語の “stronger” がどの比較関係を省略したかを監査することに限られる。

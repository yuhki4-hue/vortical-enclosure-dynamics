# Cross-calculus proof-class preservation pilot v0.1

## 0. Status / posture

本稿の地位は次に限定される。

- **exploratory pilot**
- **not a theorem**
- **not a new proof theory**
- **not a new semantics**
- **not a new proof equivalence theory**
- **not a categorical equivalence theorem unless an existing theorem is explicitly cited**
- **not a proof identity theorem**
- **no score**
- **no metric**
- **no proof geometry**
- **no metaphysical conclusion**
- **no VED claim**
- **no claim that cross-calculus proof correspondence reveals proof essence**
- **prefer standard proof-theoretic / type-theoretic terminology**

目的は “same theorems means same proofs” を確認することではなく、その推論を stress-test することである。intrinsic proof identity、canonical proof object、final proof class、representation-free proof、theorem essence、全 calculi に共通する universal correspondence は探さない。以前に退役させた project-local vocabulary も説明原理として再導入しない。

先に結論を述べる。

1. Natural deduction (ND) と simply typed lambda calculus (STLC) は、規則と proof equality を Curry–Howard 対応に沿って一致させた今回の fragment では、proof classes に強い双方向対応を持つ。
2. ND と LJ は同じ formulas を導出するが、それだけでは proof classes の対応は出ない。raw LJ equality では、ND の一つの beta-class が異なる raw LJ derivations へ写り、quotient map さえ well-defined でない。
3. cut、identity、permutation に関する matching equations を採ると quotient maps は well-defined になり、ND から LJ への map は classes 上 injective になる。しかし全 LJ classes への surjectivity と第二の round trip は本稿では確立しない。
4. \(A\land A\to A\) の first/second projection は ND、STLC、LJ のいずれでも別 classes として残る。same theoremhood は proof-class uniqueness を意味しない。

数学的新規性については negative である。結果は standard Curry–Howard translation、Gentzen translation、normalization、cut elimination、permutative conversion の役割分担で尽くされる。

---

## 1. Central question

standard calculi \(C_0,C_1\)、formula translation \(F\)、proof equalities \(\sim_0,\sim_1\) を固定し、

\[
\Gamma\vdash_{C_0}\varphi
\iff
F(\Gamma)\vdash_{C_1}F(\varphi)
\]

が成立するとする。proof translation

\[
T:\operatorname{Proof}_{C_0}(\Gamma,\varphi)
\longrightarrow
\operatorname{Proof}_{C_1}(F\Gamma,F\varphi)
\]

について次を別々に問う。

### Q1. Well-definedness on quotient

\[
\pi_1\sim_0\pi_2
\Longrightarrow
T(\pi_1)\sim_1T(\pi_2)?
\]

これが成立するときだけ

\[
\bar T:[\pi]_{\sim_0}\longmapsto[T(\pi)]_{\sim_1}
\]

が well-defined である。

### Q2. Injectivity on chosen classes

\[
T(\pi_1)\sim_1T(\pi_2)
\Longrightarrow
\pi_1\sim_0\pi_2?
\]

categorical functor を構成していないので “faithful” は使わない。

### Q3. Surjectivity on chosen classes

\[
\forall[\rho]_{\sim_1}\ \exists[\pi]_{\sim_0}\quad
\bar T([\pi])=[\rho]?
\]

同じ理由で categorical な “full” は使わない。

### Q4. Bijection

Q1 が成立し、Q2/Q3 がともに成立する場合だけ proof classes 間の bijection と言う。

### Q5. Inverse translation

逆 translation \(U\) があるとき、

\[
U(T(\pi))\sim_0\pi,
\qquad
T(U(\rho))\sim_1\rho
\]

を別々に調べる。一方から他方を推論しない。

---

## 2. Derivability equivalence is not proof correspondence

derivability の biconditional が述べるのは、各 side に少なくとも一つの proof が存在するかどうかの一致である。それ単独には次の data はない。

- individual proof translation
- source/target proof equality
- equivalence preservation
- quotient map
- injectivity / surjectivity
- inverse-up-to-equality
- canonical proof selection

従って derivability equivalence を proof correspondence の証拠として使わない。Pair A/B とも formula-level theorem と proof-level translation を別に確認する。

---

## 3. Common fragment

### 3.1 Formula grammar

\[
A,B ::= p\mid A\to B\mid A\land B.
\]

falsehood、disjunction、quantifiers は扱わない。

### 3.2 Labelled assumptions

assumption occurrence は \(x:A\) のように label を持つ。bound labels の一貫した renaming は alpha-equivalence で同一視する。

同じ formula を持つ \(x:A,y:A\) は別 assumption occurrences である。この区別により \(A\land A\to A\) の two projections を追跡できる。

---

## 4. \(C_{\mathrm{ND}}\): intuitionistic natural deduction

### 4.1 Context and proof objects

context は distinct labels を持つ finite map。proof object は constructor annotation を持つ labelled derivation tree とし、context の並べ替えや unused assumptions の表示差は別 node にしない。annotations を省略した推論図でも、その constructor tree は保持されているものとする。weakening は unused labels、contraction は一つの assumption variable の multiple use として扱う。linear calculus ではない。

### 4.2 Rules

\[
\infer[\mathrm{Ax}]{\Gamma,x:A\vdash A}{}
\]

\[
\infer[\to I]{\Gamma\vdash A\to B}
      {\Gamma,x:A\vdash B}
\qquad
\infer[\to E]{\Gamma\vdash B}
      {\Gamma\vdash A\to B & \Gamma\vdash A}
\]

\[
\infer[\land I]{\Gamma\vdash A\land B}
      {\Gamma\vdash A & \Gamma\vdash B}
\]

\[
\infer[\land E_1]{\Gamma\vdash A}{\Gamma\vdash A\land B}
\qquad
\infer[\land E_2]{\Gamma\vdash B}{\Gamma\vdash A\land B}.
\]

必要なら premise derivations を weakening して共通 context \(\Gamma\) に揃える。この presentation では structural context management を proof constructor として数えない。

### 4.3 ND proof equalities

\(\equiv_{\mathrm{ND}}^\beta\) は alpha と congruence に加え、arrow introduction/elimination detour と conjunction introduction/projection detour の standard beta reductions で生成する。

\(\equiv_{\mathrm{ND}}^{\beta\eta}\) はこれに arrow eta と product eta を加える。arrow eta には通常の freshness condition を置き、product eta は proof \(D:A\land B\) と、その two projections を再び pair にした proof を同一視する。

二 relations を一つの曖昧な “same ND proof” として扱わない。

---

## 5. \(C_\lambda\): STLC with products

### 5.1 Terms and typing

formulas を types と読み、terms を

\[
t,u ::= x\mid\lambda x:A.t\mid tu
       \mid\langle t,u\rangle\mid\pi_1t\mid\pi_2t
\]

で生成する。typing judgments は \(\Gamma\vdash t:A\)。variable、abstraction、application、pair、projections の standard rules を使う。

### 5.2 STLC proof equality

\(\equiv_\lambda^{\beta\eta}\) は alpha、arrow beta/eta、product beta/eta、congruence で生成する。

\[
(\lambda x.t)u\equiv_\beta t[u/x],
\]

\[
\pi_1\langle t,u\rangle\equiv_{\beta\land}t,\qquad
\pi_2\langle t,u\rangle\equiv_{\beta\land}u,
\]

\[
\lambda x.fx\equiv_\eta f\quad(x\notin FV(f)),
\]

\[
\langle\pi_1p,\pi_2p\rangle\equiv_{\eta\land}p.
\]

well-typed STLC with products の strong normalization、confluence、beta-normal-form uniqueness up to alpha は external standard results として使う。ただし一つの term の unique normal form から、一つの type の unique inhabitant は推論しない。Pair A で比較する ND proof object は上の constructor-annotated representation なので、同じ term annotation を持ちながら context bookkeeping だけが違う trees を別 proof として数えない。

---

## 6. \(C_{\mathrm{LJ}}\): labelled single-conclusion LJ

### 6.1 Sequents and contexts

sequents は

\[
\Gamma\Rightarrow A
\]

で、succedent は一 formula。antecedent は labelled formula occurrences の finite sequence。exchange、weakening、contractionを explicit structural rules として許す。

### 6.2 Identity and structural rules

\[
\infer[\mathrm{Id}]{x:A\Rightarrow A}{}
\]

\[
\infer[W_L]{\Gamma,x:A\Rightarrow C}{\Gamma\Rightarrow C}
\qquad
\infer[C_L]{\Gamma,z:A\Rightarrow C}
      {\Gamma,x:A,y:A\Rightarrow C}.
\]

\(E_L\) は adjacent antecedent occurrences を交換する。contraction は premise の \(x,y\) を conclusion の \(z\) に identify する。

### 6.3 Logical rules

\[
\infer[\to R]{\Gamma\Rightarrow A\to B}
      {\Gamma,x:A\Rightarrow B}
\]

\[
\infer[\to L]{\Gamma,\Delta,f:A\to B\Rightarrow C}
      {\Gamma\Rightarrow A & \Delta,y:B\Rightarrow C}
\]

\[
\infer[\land R]{\Gamma\Rightarrow A\land B}
      {\Gamma\Rightarrow A & \Gamma\Rightarrow B}
\]

\[
\infer[\land L]{\Gamma,p:A\land B\Rightarrow C}
      {\Gamma,x:A,y:B\Rightarrow C}.
\]

premises の antecedents は weakening/exchange により同じ sequence \(\Gamma\) に揃える。list ordering は exchange で処理する。

### 6.4 Cut

raw calculus には cut を含める。

\[
\infer[\mathrm{Cut}]{\Gamma,\Delta\Rightarrow C}
      {\Gamma\Rightarrow A & \Delta,x:A\Rightarrow C}.
\]

LJ cut elimination はこの fragment の external standard theorem として使う。これは各 derivable sequent が cut-free derivation を持つことを与えるが、cut-free proof の uniqueness は与えない。

### 6.5 Three LJ proof equalities

#### \(E_{\mathrm{raw}}\)

literal derivation-tree identity modulo bound-label alpha-renaming only。cut reduction、exchange cancellation、rule permutation は含めない。

#### \(E_{\mathrm{cut}}\)

\(E_{\mathrm{raw}}\) に standard Gentzen principal/commutative cut reductions、identity-cut deletion、identity expansion/contractionを加えた congruence。cut detours を消すが、cut-free independent-rule permutations をすべて同一視するとは仮定しない。

#### \(E_{\mathrm{perm}}\)

\(E_{\mathrm{perm}}\) は \(E_{\mathrm{cut}}\) と以下の standard permutative-conversion schemas を含む最小の congruence とする。

- disjoint formula occurrences に作用する adjacent inferences の交換。
- \(\land L\) と、その principal formula を使わない \(\land R\) branches の commutation。
- weakening/exchange/contraction の位置だけが異なる structural bureaucracy。
- ND eta に対応する identity expansion/contraction。

これは standard conversions の fragment restriction であり、新 equality の提案ではない。ただし complete presentation や coherence theorem は本稿で証明せず、引用もしない。従って \(E_{\mathrm{perm}}\) の下で全 LJ proof classes が ND classes と bijective だという global claim は **NOT ESTABLISHED** とする。

---

## 7. Pair A — ND and STLC

### 7.1 Formula and proof translations

\[
F_A(A\to B)=F_A(A)\to F_A(B),\qquad
F_A(A\land B)=F_A(A)\times F_A(B).
\]

\(T_A\) と \(U_A\) は次の constructor table の両方向の読みである。

| ND rule | STLC constructor |
|---|---|
| assumption \(x:A\) | variable \(x:A\) |
| \(\to I\) | \(\lambda x.t\) |
| \(\to E\) | \(tu\) |
| \(\land I\) | \(\langle t,u\rangle\) |
| \(\land E_i\) | \(\pi_i t\) |

この pair は proof annotations と term constructors を意図的に一致させた strong positive control である。

### 7.2 A1: identity

\[
\infer[\to I]{\vdash A\to A}
      {\infer[\mathrm{Ax}]{x:A\vdash A}{}}
\]

は

\[
I=\lambda x:A.x:A\to A
\]

へ移る。beta-expanded proof は

\[
I_\beta=\lambda x:A.(\lambda z:A.z)x:A\to A
\]

で type-correct、かつ \(I_\beta\equiv_\beta I\)。対応する ND detour も一 beta reduction で direct identity proof へ戻る。

### 7.3 A2: conjunction commutativity

\[
\vdash A\land B\to B\land A
\]

の ND proof は \(p:A\land B\) から \(\land E_2,\land E_1\) で \(B,A\) を得て pair にする。対応 term は

\[
S=\lambda p:A\times B.\langle\pi_2p,\pi_1p\rangle.
\]

\[
p:A\times B\vdash\pi_2p:B,\qquad
p:A\times B\vdash\pi_1p:A
\]

なので type-correct である。

### 7.4 A3: two projections

\[
\vdash A\land A\to A
\]

には first/second elimination を選ぶ two normal ND proofsがある。対応 terms は

\[
P_1=\lambda p:A\times A.\pi_1p,\qquad
P_2=\lambda p:A\times A.\pi_2p.
\]

両方 type-correct かつ beta-eta-normal。atomic \(A\) を二要素集合で解釈すると \(P_1(a_1,a_2)=a_1\)、\(P_2(a_1,a_2)=a_2\)。chosen equations はこの interpretation で sound なので

\[
P_1\not\equiv_\lambda^{\beta\eta}P_2.
\]

対応する ND proofs も distinct classes である。

### 7.5 Pair A quotient result

各 ND equality generator は対応する lambda equation へ移り、その逆も同じ constructor table で成立する。従って

\[
\bar T_A:
\operatorname{Proof}_{\mathrm{ND}}(\Gamma,A)/{\equiv_{\mathrm{ND}}^{\beta\eta}}
\longrightarrow
\operatorname{Term}_{\lambda}(\Gamma,A)/{\equiv_\lambda^{\beta\eta}}
\]

は well-defined で、

\[
U_A(T_A(D))\equiv_{\mathrm{ND}}^{\beta\eta}D,\qquad
T_A(U_A(t))\equiv_\lambda^{\beta\eta}t.
\]

従って classes 上 injective、surjective、bijective。この強さは ND rules/conversions と lambda constructors/equations を matching させた presentation choice に由来し、一般の calculi へは拡張しない。

---

## 8. Pair B — ND and LJ translations

### 8.1 Formula translation and derivability

\(F_B\) は formula 上 identity。labels も保つが、ND context split と LJ sequence order の差には exchange を入れる。

standard translations \(T_B:\mathrm{ND}\to\mathrm{LJ}\)、\(U_B:\mathrm{LJ}\to\mathrm{ND}\) を以下で固定する。これらにより

\[
\Gamma\vdash_{\mathrm{ND}}A
\iff
\Gamma\Rightarrow_{\mathrm{LJ}}A
\]

が得られる。derivability equivalence は proof translations から従うのであり、その逆ではない。

### 8.2 \(T_B\): ND to LJ

- assumption は identity plus required weakenings。
- \(\to I\) は \(\to R\)。
- \(\land I\) は \(\land R\)。
- \(\to E\) は function proof を \(\to L\) application context へ cut。
- \(\land E_i\) は proof of \(A\land B\) を standard projection sequent \(A\land B\Rightarrow A_i\) へ cut。

例えば \(D_f:\Gamma\Rightarrow A\to B\)、\(D_a:\Delta\Rightarrow A\) から

\[
\infer[\to L]{\Delta,f:A\to B\Rightarrow B}
      {D_a:\Delta\Rightarrow A & y:B\Rightarrow B}
\]

を作り、\(D_f\) と cut して \(\Gamma,\Delta\Rightarrow B\) を得る。この cut が ND application を表す。

### 8.3 \(U_B\): LJ to ND

LJ derivation に proof term を assign する standard reading を使う。

- identity は variable。
- \(\to R\) は abstraction。
- \(\land R\) は pair。
- \(\land L\) は premise term の \(x,y\) を \(\pi_1p,\pi_2p\) で同時 substitution。
- \(\to L\) は second premise の \(y:B\) に \(fu:B\) を substitution。ここで \(u:A\) は first premise の term。
- cut は proof substitution。
- weakening は unused variable、contraction は labels の identification、exchange は context reorder。

従って各 LJ derivation から type-correct ND/STLC term が得られる。

---

## 9. Pair B concrete tests

### 9.1 B1: identity and translated beta detour

direct LJ proof は

\[
\infer[\to R]{\Rightarrow A\to A}
      {x:A\Rightarrow A}.
\]

ND term \(I_\beta=\lambda x.(\lambda z.z)x\) の translation は、inner identity function を application context へ cut する。outer \(\to R\) の premise は schematically

\[
\infer[\mathrm{Cut}_{A\to A}]{x:A\Rightarrow A}
 {
  \infer[\to R]{\Rightarrow A\to A}{z:A\Rightarrow A}
  &
  \infer[\to L]{x:A,f:A\to A\Rightarrow A}
    {x:A\Rightarrow A & y:A\Rightarrow A}
 }.
\]

raw tree は direct proof と異なるが、principal cut reduction 後は direct proof にreduceする。従って

\[
I_\beta\equiv_{\mathrm{ND}}^\beta I
\]

なのに

\[
T_B(I_\beta)\not\mathrel{E_{\mathrm{raw}}}T_B(I).
\]

よって ND beta quotient から raw LJ classes への map は **not well-defined**。\(E_{\mathrm{cut}}\) ならこの tested pair は同一 class になる。

### 9.2 B2: conjunction commutativity and permutation

同じ sequent

\[
\Rightarrow(A\land B)\to(B\land A)
\]

に two cut-free organizations がある。

**\(L_{\mathrm{once}}\): decompose once.**

\[
\infer[\to R]{\Rightarrow(A\land B)\to(B\land A)}
 {
  \infer[\land L]{p:A\land B\Rightarrow B\land A}
   {
    \infer[\land R]{x:A,y:B\Rightarrow B\land A}
     {
      \infer[W_L]{x:A,y:B\Rightarrow B}{y:B\Rightarrow B}
      &
      \infer[W_L]{x:A,y:B\Rightarrow A}{x:A\Rightarrow A}
     }
   }
 }.
\]

**\(L_{\mathrm{twice}}\): introduce the result conjunction first.**

\[
\infer[\to R]{\Rightarrow(A\land B)\to(B\land A)}
 {
  \infer[\land R]{p:A\land B\Rightarrow B\land A}
   {
    \infer[\land L]{p:A\land B\Rightarrow B}
     {\infer[W_L]{x:A,y:B\Rightarrow B}{y:B\Rightarrow B}}
    &
    \infer[\land L]{p:A\land B\Rightarrow A}
     {\infer[W_L]{x:A,y:B\Rightarrow A}{x:A\Rightarrow A}}
   }
 }.
\]

both are raw-distinct and cut-free。\(U_B\) は両方を

\[
\lambda p.\langle\pi_2p,\pi_1p\rangle
\]

へ送る。従って raw LJ derivations から ND beta-eta classes への \(U_B\) は non-injective。

この pair は \(\land L\) と \(\land R\) の standard commuting conversion で \(E_{\mathrm{perm}}\)-equivalent になる。この一例から全 LJ bureaucracy が消えるとは推論しない。

### 9.3 B3: first and second projections survive

first projection:

\[
\infer[\to R]{\Rightarrow(A\land A)\to A}
 {
  \infer[\land L]{p:A\land A\Rightarrow A}
   {\infer[W_L]{x:A,y:A\Rightarrow A}{x:A\Rightarrow A}}
 }.
\]

second projection:

\[
\infer[\to R]{\Rightarrow(A\land A)\to A}
 {
  \infer[\land L]{p:A\land A\Rightarrow A}
   {\infer[W_L]{x:A,y:A\Rightarrow A}{y:A\Rightarrow A}}
 }.
\]

\(U_B\) はそれぞれ \(P_1,P_2\) へ送る。Section 7.4 の set interpretation により \(P_1\not\equiv_\lambda^{\beta\eta}P_2\)。\(E_{\mathrm{perm}}\) の listed generators は term interpretation で sound なので、この LJ proofs も同一化されない。

従って normal ND、beta-eta-normal STLC、cut-free LJ の三 side すべてで same proposition に multiple chosen proof classes が残る。

---

## 10. Pair B quotient lifting

### 10.1 Raw equality: F2

source を \(\equiv_{\mathrm{ND}}^\beta\)、target を \(E_{\mathrm{raw}}\) とすると、Section 9.1 により \(T_B\) は source-equivalent proofs を target-distinct derivations へ送る。proof translation exists だが quotient map は存在しない。

### 10.2 Matched equations: well-defined maps

source を \(\equiv_{\mathrm{ND}}^{\beta\eta}\)、target を \(E_{\mathrm{perm}}\) とする。

- ND arrow beta は principal implication cut reduction へ移る。
- ND product beta は principal conjunction cut reduction へ移る。
- ND arrow/product eta は identity expansion/contraction へ移る。
- alpha は label alpha へ移る。
- congruence は derivation-context congruence へ移る。

従って \(T_B\) は chosen quotients 上 well-defined。

逆に \(U_B\) では、cut reduction は substitution/betaへ、identity equations は etaへ、independent rule permutations と structural bureaucracy は同じ term または beta-eta equal terms へ移る。従って \(U_B\) も well-defined。

これは equality generators の compatibility から得た。derivability equivalenceから推論したのではない。

### 10.3 Injectivity and one round trip

ND derivationについてのstructural inductionで

\[
U_B(T_B(D))\equiv_{\mathrm{ND}}^{\beta\eta}D.
\]

introduction rules は同じ constructors へ戻り、eliminationを表す LJ cut は ND substitution/applicationへ戻る。よって \(\bar T_B\) は classes 上 injective、\(\bar U_B\) は classes 上 surjective。

### 10.4 Surjectivity and second round trip

selected proofsでは

\[
T_B(U_B(\rho))\mathrel{E_{\mathrm{perm}}}\rho
\]

を確認できる。direct identity、translated cut proof、\(L_{\mathrm{once}}/L_{\mathrm{twice}}\)、two projectionsはそれぞれcut/permutation conversions後に戻る。

しかし arbitrary LJ derivation に必要な全 coherence casesを本稿は列挙・証明せず、external theoremも引用していない。従って次は **NOT ESTABLISHED**。

- \(\bar T_B\) の global surjectivity。
- \(\bar U_B\) の global injectivity。
- every LJ class に対する second round trip。
- Pair B proof classes の global bijection。

これは counterexample ではなく evidence boundary である。

---

## 11. Main quotient-lifting table

Pair B primary columnsでは \(\equiv_{\mathrm{ND}}^{\beta\eta}/E_{\mathrm{perm}}\) を使う。

| property | Pair A ND→STLC | Pair A STLC→ND | Pair B ND→LJ | Pair B LJ→ND |
|---|---:|---:|---:|---:|
| formula translation | **YES**, formula/type | **YES**, type/formula | **YES**, identity | **YES**, identity |
| derivability preservation | **YES** | **YES** | **YES** | **YES** |
| reflection | **YES** | **YES** | **YES**, via \(U_B\) | **YES**, via \(T_B\) |
| proof translation | **YES** | **YES** | **YES**, may add cut | **YES**, term assignment |
| source equality preserved? | **YES** | **YES** | **YES**, generator check | **YES**, generator check |
| quotient map well-defined? | **YES** | **YES** | **YES** | **YES** |
| injective on classes? | **YES** | **YES** | **YES** | **NOT ESTABLISHED globally** |
| surjective on classes? | **YES** | **YES** | **NOT ESTABLISHED globally** | **YES** |
| inverse up to equality? | **YES** | **YES** | \(U_BT_B\simeq id\): **YES** | \(T_BU_B\simeq id\): **NOT ESTABLISHED globally** |

equality sensitivity:

| Pair B target equality | ND→LJ quotient result | evidence |
|---|---:|---|
| \(E_{\mathrm{raw}}\) | **NO** for ND beta quotient | \(I\equiv_\beta I_\beta\), translations raw-distinct |
| \(E_{\mathrm{cut}}\) | **YES for tested beta pairs**; full match not claimed | translated beta detour reduces |
| \(E_{\mathrm{perm}}\) | **YES** for fixed ND beta-eta equality | listed generators match |

強い target quotient が多くの bureaucracy を消しても、それを “more essential” な proof class とは呼ばない。

---

## 12. Failure modes

### F1. No proof translation

Pair A/Bではtriggerされない。両方向 translations を明示した。ただし一般の derivability-equivalent calculi に proof translation が自動的に存在するとは推論しない。

### F2. Translation exists but quotient map is not well-defined

**Triggered.** ND beta classesから \(E_{\mathrm{raw}}\)-LJ classesへの \(T_B\)。\(I,I_\beta\) が witness。

### F3. Well-defined but non-injective

raw LJ derivationsからND classesへの \(U_B\)。\(L_{\mathrm{once}}\ne L_{\mathrm{twice}}\) as raw treesだが、同じtermへ移る。matched \(E_{\mathrm{perm}}\) quotientでglobal non-injectivityは示していない。

### F4. Well-defined but non-surjective

matched Pair B でglobal non-surjectivity のcounterexampleはない。surjectivity proofも完了していないため **NOT ESTABLISHED**。lack of proofをfailure evidenceにしない。

### F5. Bijective up to chosen equalities

**Triggered for Pair A.** annotated ND modulo matching beta-eta conversions と STLC terms modulo matching equations の間で成立する。Pair Bでは主張しない。

---

## 13. Raw proofs and proof classes

| target | raw ND / classes | raw STLC / classes | raw LJ / \(E_{\mathrm{perm}}\)-classes |
|---|---|---|---|
| \(A\to A\) controls | direct/beta-expanded; tested pair one class | \(I,I_\beta\); one | direct/cut detour; one tested class |
| \(A\land B\to B\land A\) | direct/detours; one tested class | \(S\) and expansions; one | \(L_{\mathrm{once}},L_{\mathrm{twice}}\); one tested class |
| \(A\land A\to A\) | first/second; at least two | \(P_1,P_2\); at least two | first/second; at least two |

countsはconstructed finite setについてのみで、all proofsをenumerateしていない。

\[
\exists\text{ a proof of }A
\centernot\Rightarrow
\exists!\text{ a proof class of }A.
\]

---

## 14. Normalization, cut elimination, permutation

### ND normalization

introduction followed by matching eliminationというdetourをsubstitutionへreduceする。eta採用時はunnecessary expansionもcontractする。

### STLC normalization

term redexをsubstitution/projectionへreduceする。Pair AではND normalizationのrule-by-rule image。

### LJ cut elimination

cut formulaとadjacent rulesに従いcutをcommute/reduceし、最終的にcutを除く。

### Rule permutation

cut-freeでもindependent left/right rulesやstructural rulesのorderは異なり得る。これを消すにはcut eliminationとは別のpermutative conversionsが必要。

従って literal operations として

\[
\text{ND normalization}\ne\text{LJ cut elimination}.
\]

また

\[
\text{cut-free}\centernot\Rightarrow\text{unique LJ proof},
\qquad
\text{normal ND proof}\centernot\Rightarrow\text{unique ND proof}.
\]

\(A\land A\to A\) のtwo projectionsが双方のcontrolである。

---

## 15. Cross-calculus comparison is equality-relative

evidenceは次を支持する。

> Whether a derivability equivalence lifts to a correspondence between proof
> classes depends on the specified proof translations and on the specified
> proof equalities on both sides.

同じ \(T_B\) でもtarget equalityにより結果が変わる。

- \(E_{\mathrm{raw}}\): ND beta quotientからのmapはnot well-defined。
- \(E_{\mathrm{cut}}\): tested beta detourは消えるがeta/permutation全体は未処理。
- \(E_{\mathrm{perm}}\): fixed generator checksによりmaps are well-defined。left inverseからND→LJ injectivityも得る。
- global surjectivity/bijection: complete coherence evidenceなしにはnot established。

fixed calculi、translations、equalitiesの下ではordinary precise questionsである。“proof identity is inherently relative” や “no true proof exists” とは言わない。

---

## 16. Executable-check decision

companion scriptは作成しない。

- Pair Aはconstructor tableとtyped examplesでhand-checkできる。
- Pair Bの中心はfinite beta normalizationではなく、LJのcut/permutation equalityをどこまで採るかである。
- custom normalizerを作ると、実装したrewrite relationをstandard LJ proof equalityと誤認させる危険がある。
- finite examplesからglobal surjectivity/coherence theoremは推論できない。

codeなしの方がevidence boundaryを明瞭に保てる。

---

## 17. Strong negative controls

### N1. “Same derivability means same proofs”

**KILL.** Pair Bのraw equalityではquotient mapさえwell-definedでない。

### N2. “Normalization and cut elimination are the same operation”

**KILL.** objects/rulesが異なる。translationsの下でselected reductionsが対応するだけ。

### N3. “Cut-free proof means canonical proof”

**KILL.** \(L_{\mathrm{once}},L_{\mathrm{twice}}\) はraw-distinct cut-free proofs。two projectionsはquotient後もdistinct。

### N4. “Curry–Howard proves all calculi share proof identity”

**KILL.** Pair Aのstrengthはconstructors/equationsをmatchingさせたことによる。

### N5. “A bijection reveals theorem essence”

**KILL.** Pair Aのbijectionはchosen annotated presentations and equationsのstandard correspondence。

### N6. “Proof translation implies injectivity”

**KILL.** raw \(U_B\) は \(L_{\mathrm{once}},L_{\mathrm{twice}}\) を同じND classへ送る。

### N7. “Injectivity plus derivability equivalence implies surjectivity”

**KILL.** derivability equivalenceは各sequentのproof-set nonemptinessだけを比較する。Pair Bではinjectivityを得てもglobal surjectivityはnot established。

---

## 18. Kill-criteria audit

| criterion | result |
|---|---|
| calculi not fixed | not triggered; grammar, contexts, rules, cut status are explicit |
| proof equalities vague | tested levels are separated; global completeness is not claimed |
| proof translation absent | not triggered; \(T_A,U_A,T_B,U_B\) specified |
| derivability used as proof correspondence evidence | not triggered |
| normalization conflated with cut elimination | not triggered |
| cut-free assumed unique | not triggered |
| no concrete pair | not triggered; identity, swap, projections |
| quotient well-definedness unchecked | not triggered; raw failure and matched success |
| injectivity/surjectivity overclaimed | not triggered; Pair B global claims remain open |
| only Curry–Howard | not triggered; Pair B gives F2/F3 controls |
| project vocabulary replaces standard terms | not triggered |
| essence claim | not triggered; killed |
| negative results suppressed | not triggered |

### Overall verdict

新しい proof theory としては **KILL**。standard proof-translation audit としては **RETAIN, limited**。Pair A/Bの差はequation matchingとcoherence evidenceの差で説明できる。

---

## 19. Strongest acceptable positive statement

> For fixed calculi, fixed proof equalities, and explicit proof translations,
> a derivability equivalence may or may not lift to a well-defined, injective,
> surjective, or bijective correspondence between proof classes. Each property
> must be checked separately.

Pair Aではmatched Curry–Howard presentationによりbijectionまで得た。Pair Bではmatched quotients上well-definednessとone-sided round tripを得たが、global bijectionは得ていない。

---

## 20. Relation to the previous specification-preservation pilot

前 pilotはspecification changeについてliteral syntax、formula translation、derivability、reflection、semantic transport、proof translationを分離した。proof-class preservationは限定的にしか扱わなかった。

今回はderivability equivalenceがあるcalculi間でchosen proof equalitiesまで固定し、その未検査部分を直接扱った。結果は

\[
\text{derivability equivalence}
\centernot\Rightarrow
\text{well-defined quotient map}.
\]

translationがequality generatorsをrespectすればquotient mapができる。bijectionにはinjectivity、surjectivity、both round tripsの別証拠が要る。

previous quotient pilotはfixed calculus内でequalityを変えた。今回はdifferent calculi間のtranslationがthose equalitiesをrespectするかを見た。両者を混同しない。

---

## 21. Final report

1. **Exact working question:** derivability-equivalentなtwo calculiのproof translationsが、chosen equalitiesによるclasses間のwell-defined / injective / surjective / bijective mapへliftするか。
2. **Calculi:** labelled intuitionistic ND、STLC with products、labelled single-conclusion LJ for \(\to,\land\)。
3. **Proof equalities:** ND/STLC alpha + arrow/product beta/eta。LJは \(E_{\mathrm{raw}},E_{\mathrm{cut}},E_{\mathrm{perm}}\) を分離。
4. **Translations:** ND rule constructors ↔ STLC constructors。ND→LJはeliminationsをcutで表し、LJ→NDはterm assignment/substitution。
5. **Derivability equivalence:** **YES** for Pair A/B in the fixed fragment。
6. **Pair A:** quotient maps are well-defined, injective, surjective, and inverse up to matched beta-eta equality。
7. **Pair B:** raw equalityではND-beta quotient mapなし。\(E_{\mathrm{perm}}\) ではmaps are well-defined、\(U_BT_B\simeq id\)。global other round trip/bijectionは **NOT ESTABLISHED**。
8. **Well-definedness:** Pair A **YES** both ways。Pair B **NO** for ND quotient→raw LJ、**YES** both ways for matched equations。
9. **Injectivity:** Pair A **YES**。matched ND→LJ **YES** by left inverse。matched LJ→ND **NOT ESTABLISHED globally**。raw LJ→NDはconcretely non-injective。
10. **Surjectivity:** Pair A **YES**。matched LJ→ND **YES** by left inverse。matched ND→LJ **NOT ESTABLISHED globally**。
11. **Inverse up to equality:** Pair A both directions **YES**。Pair B \(U_BT_B\simeq id\) **YES**、\(T_BU_B\simeq id\) **NOT ESTABLISHED globally**。
12. **Strongest preservation example:** ND normalization classes と STLC beta-eta classes の constructorwise bijection。
13. **Strongest mismatch example:** \(I\equiv_\beta I_\beta\) in ND while their LJ translations are distinct under \(E_{\mathrm{raw}}\); translation does not descend。
14. **Normalization/cut elimination:** corresponding reductions align under translations but are not the same operation; permutations need additional equations。
15. **Did theoremhood imply same proof classes?:** **NO.** theoremhood matches proof existence only; \(A\land A\to A\) retains multiple classes。
16. **Strongest negative result:** no cross-calculus proof identity follows from same derivability; even well-definedness depends on matching both equalities。
17. **Strongest methodological observation:** fix calculi, translations, both equalities, then check well-definedness、injectivity、surjectivity、round trips separately。
18. **Anything beyond standard proof theory?:** **NO.** Curry–Howard、Gentzen translations、normalization、cut elimination、proof equivalenceで尽くされる。
19. **Another pilot warranted?:** **NO by default.** Pair Bのglobal bijection問題にはinformal pilotでなく、complete conversion systemとliterature-backed coherence theoremが必要。
20. **Exact next falsification question:** none, because no further pilot is recommended。

---

## 22. Final self-audit

| check | answer |
|---|---|
| Did I fix the exact calculi? | **Yes.** grammar, contexts, rules, structural rules, cut status, proof objectsを明示。 |
| Did I fix proof equality separately? | **Yes.** ND/STLC beta-eta and LJ raw/cut/permutation levels。 |
| Did I distinguish derivability from proof correspondence? | **Yes.** Section 2 and raw mismatch。 |
| Did I verify quotient-map well-definedness? | **Yes.** generator checks and raw counterexample。 |
| Did I distinguish injective from surjective? | **Yes.** Pair B obtains only one side through \(U_BT_B\simeq id\)。 |
| Did I confuse normalization with cut elimination? | **No.** |
| Did I assume cut-free = canonical? | **No.** explicit counterexamples。 |
| Did I use actual proof examples? | **Yes.** typed terms and LJ trees。 |
| Did I avoid essence language? | **Yes.** all such readings are rejected。 |
| Did I preserve prior negative results? | **Yes.** no universal correspondence or final class。 |
| Did I use standard terminology? | **Yes.** |
| Did I invent a new proof theory? | **No.** |

### Closing verdict

same derivability does not itself identify proofs。Pair A gives a proof-class bijection because ND syntax/conversions and STLC terms/equations were matched constructor by constructor。Pair B shows that a standard proof translation can fail to descend when target equality is too fine。matching cut、identity、permutation equations restore well-definedness, but global bijection still requires an independent coherence result。

従って cross-calculus proof-class preservation is not automatic。fixed translations and equalitiesに対するwell-definedness、injectivity、surjectivity、round tripsというordinary mathematical questionsに分解される。

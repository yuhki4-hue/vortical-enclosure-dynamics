# Theorem specification-change preservation pilot v0.1

## 0. Status / posture

本稿は次の地位に限定される。

- **exploratory pilot**
- **not a theorem**
- **not a new proof theory**
- **not a new semantics**
- **not a theory of invariants**
- **not a theory of mathematical essence**
- **not a universal preservation theorem**
- **no score**
- **no metric**
- **no proof geometry**
- **no metaphysical conclusion**
- **no VED claim**
- **no claim that preserved structure is theorem-intrinsic**
- **prefer standard terminology**

今回の目的は “find the thing that remains unchanged underneath every presentation” ではない。次も探さない。

- true theorem core
- representation-free theorem
- final invariant
- intrinsic proof identity
- canonical specification
- universal structure preserved under all translations

以前の pilotsで確認した negative resultsを維持する。fixed formal questionsはrepresentation、equivalence relation、comparison classを明示すれば通常の有限問題としてterminateし得る。そこからessence、indefinite displacement、universal invariantは得られなかった。

今回の問いは次である。

> What, if anything, is preserved when the specification itself changes?

先に結論を述べる。単一の “preserved theorem” relationは得られなかった。bijective renamingはtranslated derivabilityを双方向に保ち、derived lemmasの追加は同じlanguageのdeductive closureを保ち、explicit definitional extensionはold-language consequencesを保ち、genuine strengtheningはderivabilityをforwardにだけ保った。literal syntax、semantic truth、proof translation、raw proof recordは別々に監査する必要がある。

これはstandard facts about renaming, monotonicity, derived-rule elimination, and definitional extensionsの再確認であり、新 structural residueはない。

---

## 1. Central question

specificationを説明用に

\[
S=(\mathcal L,\Gamma,R,C)
\]

と書く。\(\mathcal L\) はlanguage、\(\Gamma\) はaxioms/assumptions、\(R\) はinference rules、\(C\) はこのtestに関係するrepresentation/citation conventionsである。これはordinary tupleであり、新 technical objectではない。

source/targetを

\[
S_0=(\mathcal L_0,\Gamma_0,R_0,C_0),
\qquad
S_1=(\mathcal L_1,\Gamma_1,R_1,C_1)
\]

とし、それらを結ぶ map、inclusion、translation、interpretationを個別に \(T\) と書く。

中心問いは：

> When \(S_0\) is replaced by \(S_1\), which judgments are preserved, in what
> exact sense, and because of which standard preservation property?

“preserved” と言うたびに、対象がformula、derivability judgment、semantic valuation、proof object、proof classのどれかを明記する。

---

## 2. Separate preservation claims

以下は新 taxonomyではなく、曖昧なpreservation claimを展開するchecklistである。

### P0. Same literal formula

同じcharacter string / AST \(\varphi\) が \(\mathcal L_0,\mathcal L_1\) の両方でwell-formedか。renaming後の \(T(\varphi)\) とliteral \(\varphi\) は通常異なる。

### P1. Formula translation

\[
T:\mathrm{Form}(\mathcal L_0)\to\mathrm{Form}(\mathcal L_1)
\]

が定義されるか。definitional eliminationでは逆向きのtranslationもあり得る。

### P2. Forward derivability preservation

\[
\Gamma\vdash_{S_0}\varphi
\Longrightarrow
T(\Gamma)\vdash_{S_1}T(\varphi).
\]

### P3. Reflection / converse

\[
T(\Gamma)\vdash_{S_1}T(\varphi)
\Longrightarrow
\Gamma\vdash_{S_0}\varphi.
\]

### P4. Equivalence of derivability

P2とP3の両方が、明示されたformula scopeで成立すること。

\[
\Gamma\vdash_{S_0}\varphi
\iff
T(\Gamma)\vdash_{S_1}T(\varphi).
\]

### P5. Proof translation

source proof \(\pi\) からtarget proof \(T_\pi(\pi)\) をnodewiseまたはeffectiveに構成できるか。theorem-set inclusionだけから自動的には従わない。

### P6. Proof identity / proof-class preservation

raw treesがliteralに同じか、またはfixed equivalence classesが対応するか。P2–P5とは別であり、本稿では必要な範囲だけ問う。

### Semantic preservation

semantic claimにはmodel/valuation translationを別途定義する。syntactic derivability preservationだけから、soundness/completeness assumptionsなしにsemantic preservationを推論しない。

---

## 3. Four small standard transformations

次の四つだけを使う。

1. **T1 — bijective renaming / signature isomorphism:** clean two-way control。
2. **T2 — adding already-derived helper lemmas:** addition commutativityの \(L_1,L_2\)。
3. **T3 — explicit definitional extension:** fresh propositional atom \(d\) with \(d\leftrightarrow(P\land Q)\)。
4. **T4 — genuine strengthening:** addition theory without inductionからfull induction theoryへのinclusion。

T4はone-way preservationのnegative controlとして必要なので採用する。新 countermodelは作らず、既存 addition-commutativity testのmodelを再利用する。

---

## 4. T1 — Pure renaming / signature isomorphism

### A. Source specification \(S_0\)

- \(\mathcal L_0\): intuitionistic propositional natural deduction with atoms \(A,B\)、\(\to,\times\)。
- \(\Gamma_0\): arbitrary \(\mathcal L_0\)-assumptions。
- \(R_0\): standard introduction/elimination rules。
- convention: proof trees carry formula labels and rule names。

### B. Target specification \(S_1\)

同じ calculusだが atomsを \(A',B'\) とする isomorphic signature \(\mathcal L_1\)。rulesのshapeは同じ。

### C. Translation

bijection \(\rho\) を

\[
\rho(A)=A',\qquad \rho(B)=B'
\]

とし、connectivesへhomomorphically extendする。

\[
\rho(X\to Y)=\rho(X)\to\rho(Y),
\qquad
\rho(X\times Y)=\rho(X)\times\rho(Y).
\]

proof treeには全formula labelsを \(\rho\) で置換し、rule labels/tree shapeを保つ \(\rho_\pi\) を定義する。inverse renaming \(\rho^{-1}\) もある。

### D. Candidate preserved judgment

\[
\Gamma\vdash_{R_0}\varphi
\iff
\rho(\Gamma)\vdash_{R_1}\rho(\varphi).
\]

例として product commutativity

\[
A\times B\vdash B\times A
\]

は

\[
A'\times B'\vdash B'\times A'
\]

へ移る。

### E. Exact direction

- P0 literal formula: **NO** for formulas containing renamed atoms。
- P1 formula translation: **YES**, bijective。
- P2 forward derivability: **YES**。
- P3 reflection: **YES**, by \(\rho^{-1}\)。
- P4 iff: **YES** for all translated formulas。
- P5 proof translation: **YES**, nodewise in both directions。
- P6 raw proof identity: **NO**; formula labels differ。tree-shape isomorphismは保たれる。

### F. Evidence

derivation heightについてのstructural induction。各 natural-deduction ruleはmetavariablesのrenameにinvariantなので、last ruleを同じruleのrenamed instanceへ送れる。inverse translationでconverseを得る。

semanticsでは Heyting algebra 上の valuation \(v\) を \(v'(\rho(A))=v(A)\) とtransportすればformula valueが対応し、したがってvalidityも対応する。これはvaluation mapを明示した別argumentである。

### G. What is not preserved

- literal syntax / raw proof labels
- sourceとtargetのsymbol names
- historical/pedagogical meaning of the chosen names
- an intrinsic identity claim about proof objects

### H. Scope

all \(\rho\)-translated formulas and proof trees。これはstrongest clean positive controlだが、standard syntactic isomorphism以上ではない。

---

## 5. T2 — Add already-derived helper lemmas

addition commutativityの既存 settingを使う。

### A. Source specification \(S_0\)

- \(\mathcal L=\{0,S,+,=\}\)。
- \(\Gamma_+\): successor background、Add-0、Add-S、induction schema。
- \(R\): standard first-order logic with equality。
- source citation convention: \(L_1,L_2\) をaxiom leavesとしては使わず、必要ならderiveまたはinlineする。

既存 proofsにより

\[
\Gamma_+\vdash_R L_1,
\qquad
L_1:=\forall x\;(0+x=x),
\]

\[
\Gamma_+\vdash_R L_2,
\qquad
L_2:=\forall x\forall y\;(S(x)+y=S(x+y)).
\]

### B. Target specification \(S_1\)

languageとrulesは同じで、axiom presentation / available citation resourcesだけを

\[
\Gamma_+'=\Gamma_+\cup\{L_1,L_2\}
\]

へ変える。

### C. Inclusion / proof transformations

formula mapはidentity \(\iota(\varphi)=\varphi\)。source proofはそのままtargetでreplayできる。target proof中の \(L_1,L_2\) axiom leavesを、既存の \(\Gamma_+\)-derivationsで置換すればsource proofへ戻せる。

### D. Candidate preserved judgment

全てのsame-language formulas \(\varphi\) について

\[
\Gamma_+\vdash_R\varphi
\iff
\Gamma_+'\vdash_R\varphi.
\]

特に \(\mathrm{Comm}:=\forall x\forall y(x+y=y+x)\) は両方でderivable。

### E. Exact direction

- P0: **YES**; languageは同じ。
- P1: **YES**, identity。
- P2: **YES**, monotonicity / proof replay。
- P3: **YES**, derived-lemma inlining。
- P4: **YES**, same deductive closure for all formulas of \(\mathcal L\)。
- P5: **YES** both ways, but backward translation may expand proof trees。
- P6 raw proof identity: **NO in general**; named leaves become subderivations。

### F. Evidence

forwardはweakening/monotonicity。backwardはtarget derivationのheightと、extra axiom leafのreplacementについてのinduction、すなわちstandard derived-rule eliminationである。

“conservative extension” を広い意味で使うことはできるが、standard usageにはfresh languageを伴うconservative extensionもある。ここでは曖昧さを避け、**same-language theories have the same deductive closure** と言う。

### G. What is not preserved

- proof length: named lemma leavesによりshorterになり得る。
- proof tree / citation boundaries: inline subproofがnamed leafへ変わる。
- proof search behavior and library lookup。
- deletion-minimality relative to the axiom presentation: redundant derived axiomsを加えると変わり得る。
- raw proof-object identity。

### H. Scope

same language \(\mathcal L\) の全formulas。theorem setは変わらないが proof records / available resourcesは変わる。

---

## 6. Bridge case: derivability preserved, proof record changed

既存 commutativity proofでは \(L_1,L_2\) をnamed lemmasとして使うorganizationと、内容をmain proofへinlineするorganizationがあった。今回additionを逆向きに見る。

\[
\Gamma_+longrightarrow\Gamma_+'
\]

では、\(L_1,L_2\) はすでにsourceでderivableなのでnew theoremを生まない。しかしtarget proofではそれらをprimitive available leavesのようにciteできる。

従って最も明瞭な bridge resultは：

\[
\text{same deductive closure}
\centernot\Rightarrow
\text{same proof record or citation structure}.
\]

ここでhelper lemmasをtheorem assumptionsと混同しない。sourceではderived theorems、targetではaxiom presentationに追加された formulasであり、どちらの場合もComm statementのhypothesesではない。

---

## 7. T3 — Explicit definitional extension

### A. Source specification \(S_0\)

- \(\mathcal L_0\): atoms \(P,Q\)、connectives \(\land,\to\)。
- \(\Gamma\): arbitrary set of \(\mathcal L_0\)-formulas。
- \(R\): standard intuitionistic propositional natural deduction。
- define \(X\leftrightarrow Y\) as \((X\to Y)\land(Y\to X)\)。

### B. Target specification \(S_1\)

fresh propositional atom \(d\notin\mathcal L_0\) を追加し

\[
\mathcal L_1=\mathcal L_0\cup\{d\},
\]

\[
\Delta_d=\{d\leftrightarrow(P\land Q)\},
\qquad
\Gamma^d=\Gamma\cup\Delta_d
\]

とする。rulesは同じconnective rulesである。

### C. Inclusion and elimination translation

old-to-new inclusion \(i\) はold formulasをそのまま読む。elimination translation \(\tau:\mathrm{Form}(\mathcal L_1)\to\mathrm{Form}(\mathcal L_0)\) を

\[
\tau(d)=P\land Q,
\qquad
\tau(P)=P,
\qquad
\tau(Q)=Q,
\]

かつ \(\tau\) が \(\land,\to\) と可換するようrecursively定める。old formula \(\varphi\) には \(\tau(i(\varphi))=\varphi\)。

### D. Candidate preserved judgment

old-language formulas \(\varphi\in\mathrm{Form}(\mathcal L_0)\) について

\[
\Gamma\vdash_R\varphi
\iff
\Gamma^d\vdash_R i(\varphi).
\]

### E. Exact direction

- P0: **YES for old formulas**, which remain literally well-formed in \(\mathcal L_1\); **NO** for formulas containing \(d\) in source。
- P1: **YES**, inclusion \(i\) and elimination \(\tau\)。
- P2: **YES**, old proof replay。
- P3: **YES for old-language conclusions**, by definitional elimination。
- P4: **YES, restricted to old-language consequences**。
- P5: **YES**: forward replay; backward translate each formula and replace the defining axiom by a derivation of \((P\land Q)\leftrightarrow(P\land Q)\)。
- P6 raw proof identity: **NO in general**。

### F. Evidence

target derivationについてのinduction。logical rule instancesは \(\tau\) でsame rule instancesへ移る。definition axiomは

\[
\tau(d\leftrightarrow(P\land Q))
=(P\land Q)\leftrightarrow(P\land Q),
\]

となり、identity derivationsから証明できる。従ってold conclusionのtarget proofをsource proofへeliminateできる。

semantic controlでは、任意の Heyting algebra \(\mathcal H\) とその上の old-language valuation \(v\) は

\[
v^d(d)=v(P)\mathbin{\wedge_{\mathcal H}}v(Q)
\]

によりdefinitionを満たすtarget valuationへ一意にextendする。このvaluation translationを通じold formulasのvalues、したがってvalidityは保存される。これはsyntactic proofとは別のevidenceである。

### G. What is not preserved

- language identity and literal availability of \(d\)。
- theorem set as one literal set of strings: source cannot formulate \(d\leftrightarrow(P\land Q)\)。
- proof length / syntax: \(d\) を使うshort proofはeliminationでexpandし得る。
- proof search vocabulary and intermediate formulas。
- raw proof identity and quotient-class counts。

### H. Scope

conservativity claimは **old-language formulas only**。extended languageはfresh-symbol formulasを新たにexpress/proveできる。“same theory” とは言わない。

---

## 8. Definitional-extension control questions

1. **Every old proof still works?** Yes。inclusionによるliteral replay。
2. **Can a proof of an old conclusion using \(d\) be eliminated?** Yes, for the fixed explicit definition and standard substitution-preserving rules, by \(\tau\)-translation。
3. **Old-language conservativity?** Yes。
4. **Proofs literally identical?** No in general。\(d\)-nodesとtheir eliminations differ。
5. **New formulas with \(d\)?** Yes。definition itselfなどをtargetだけがformulateする。

従って

\[
\text{same old-language consequences}
\centernot\Rightarrow
\text{same language, same proof syntax, or same total theorem-string set}.
\]

---

## 9. Renaming / isomorphism control

T1は今回のstrongest clean positive controlである。

| item | result |
|---|---|
| literal formula | generally changes |
| translated formula | uniquely fixed by \(\rho\) |
| derivability | iff under \(\rho\) |
| proof tree | nodewise transport available |
| raw labels | change |
| semantic truth | preserved under explicit valuation transport |

ここで保たれたのはspecified isomorphismに沿ったsyntactic/semantic patternである。“representation-independent theorem structure” やtheorem essenceではない。

---

## 10. T4 — Genuine theory strengthening

### A. Source specification \(S_0\)

\(\Gamma_0=\Gamma_+\setminus I\)。すなわち arithmetic language、successor axioms、Add-0、Add-Sを持つが induction schema \(I\) を持たない。calculus \(R\) は同じ。

### B. Target specification \(S_1\)

\[
\Gamma_1=\Gamma_0\cup I=\Gamma_+.
\]

language、formula syntax、logic rulesは同じで、axiom theoryだけをstrictにstrengthenする。

### C. Inclusion

\(T\) はformula上identity、theory inclusion \(\Gamma_0\subseteq\Gamma_1\)。source proofを同じraw treeとしてtargetへreplayできる。

### D. Candidate preservation and counterexample

全formulas \(\varphi\) についてmonotonicityにより

\[
\Gamma_0\vdash_R\varphi
\Longrightarrow
\Gamma_1\vdash_R\varphi.
\]

converseはCommで失敗する。既存 testのbi-infinite-successor-chain modelは \(\Gamma_0\) を満たすがCommを満たさない。soundnessにより

\[
\Gamma_0\nvdash_R\mathrm{Comm}.
\]

一方、full induction proofにより

\[
\Gamma_1\vdash_R\mathrm{Comm}.
\]

### E. Exact direction

- P0: **YES**, same language。
- P1: **YES**, identity。
- P2: **YES**, forward monotonicity。
- P3: **NO**, witnessed by Comm。
- P4: **NO**。
- P5: **YES forward** by raw replay; **NO general backward translation**。
- P6: source proof replayはraw-preservedだが、new target proofs need not have source counterparts。

### F. Evidence

forwardはstandard derivability monotonicity。converse failureはexisting countermodel + soundnessであり、failed proof attemptだけではない。

semantically、\(\mathrm{Mod}(\Gamma_1)\subsetneq\mathrm{Mod}(\Gamma_0)\)。stronger theoryはfewer modelsを持ち、more consequencesを持ち得る。syntactic resultとsemantic model inclusionを同一視せず、それぞれのstandard theoremで関係づける。

### G. What is not preserved

- full theorem set: Commがtargetだけに加わる。
- reflection/backward derivability。
- general backward proof translation。
- model class identity。
- axiom minimality and proof-search behavior。

### H. Scope

forward preservationはsame-language all formulas。strictness witnessはspecific formula Comm。

---

## 11. Preservation table

| Change | Literal formula preserved? | Formula translation? | Forward derivability? | Reflection? | Proof translation? | Raw proof preserved? |
|---|---:|---:|---:|---:|---:|---:|
| T1 bijective renaming | **NO generally** | **YES**, \(\rho\) | **YES** | **YES**, \(\rho^{-1}\) | **YES**, nodewise both ways | **NO**, renamed labels |
| T2 add derived \(L_1,L_2\) | **YES** | **YES**, identity | **YES** | **YES**, inline derived proofs | **YES**, replay / expansion | **NO in general**; target citations differ |
| T3 definitional extension | **YES for old formulas** | **YES**, \(i,\tau\) | **YES** | **YES for old formulas** | **YES**, replay / elimination | **NO in general** |
| T4 add induction | **YES** | **YES**, identity | **YES** | **NO**, Comm | **YES forward only** | **CONDITIONAL**: old proof replay only |

semantic resultsは別表にする。

| Change | Semantic comparison | Evidence / condition |
|---|---|---|
| T1 | satisfaction corresponds | transport valuations along \(\rho\) |
| T2 | same model class in same language | \(L_1,L_2\) are derivable; soundness |
| T3 | old valuations uniquely extend; old truth preserved | set \(v^d(d)=v(P\land Q)\) |
| T4 | \(\mathrm{Mod}(\Gamma_1)\subsetneq\mathrm{Mod}(\Gamma_0)\) | induction adds constraints; existing source-only model |

第一表のderivability resultから第二表をassumptionなしに推論していない。各rowにvaluation/model mapまたはsoundnessを明示した。

---

## 12. Strongest structural question

問いは：

> Is there a single thing called “the preserved theorem,” or does preservation
> decompose into several standard relations between specifications?

### Result

**Result B + Result D.** tested changesは異なるものを保った。

- T1: formula/proof translationとderivability iff。
- T2: same-language deductive closureとexpandable proof citations。
- T3: old-language conservativityとdefinitional elimination。
- T4: one-way monotonicityだけ。

従ってliteral identity、translated derivability、reflection、old-language consequence、semantic satisfaction、proof transportを一つのpropertyへcollapseできない。

同時に、全exerciseはtextbook translation / conservativity / monotonicity factsで尽くされる。新しい structural residueはない。standard notion “conservative extension” はT2を広義に、T3を通常のlanguage-extension senseで扱えるが、renaming isomorphismやstrict strengtheningのone-way caseまですべて同じrelationとしてsubsumesしない。

---

## 13. Important negative controls

### N1. “If theoremhood is preserved, the proof is preserved”

**KILL.** T2/T3ではderivabilityが保たれてもnamed citations、inline expansions、fresh-symbol steps、proof lengthが変わる。proof translationがあることとraw identityも別である。

### N2. “Same old-language theorems means same theory”

**KILL.** T3はlanguageとexpressive vocabularyが異なる。T2もaxiom presentation / available resourcesが異なる。“same theory” を言うにはdeductive equivalence、definitional equivalence等のcriterionが必要である。

### N3. “Conservative extension means nothing changed”

**KILL.** T3ではfresh symbol \(d\)、definition、new formulas、proof search/intermediate syntaxが加わる。変わらないのはold-language consequencesという限定されたobjectである。

### N4. “Translation-preserved means literal identity”

**KILL.** T1で \(A\times B\to B\times A\) と \(A'\times B'\to B'\times A'\) はliteralにdifferentだが、\(\rho\) の下でderivability patternが対応する。

### N5. “What survives is the theorem’s essence”

**KILL.** preservationはchosen mapとobjectにrelativeなstandard relationである。essence claimへのevidenceはない。

### N6. “Every specification change has a nontrivial invariant”

**KILL.** arbitrary changeにはtranslationさえない場合があり、本稿はuniversal claimを検査も証明もしていない。T4ではreflectionが実際に失敗する。

---

## 14. Relation to the previous quotient pilot

previous quotient pilotは

\[
\text{fixed calculus and raw term space}
+\text{change the equality relation}
\]

を検査した。alpha/beta/eta/product equationsが許すraw distinctionsだけが消え、\(A\times A\to A\) のtwo projection classesは残った。

今回変えたのはspecification itselfである。

- T1: signature labels。
- T2: axiom/resource presentation。
- T3: languageとexplicit definition。
- T4: axiom strength / model class。

前回のquotient classesを今回のpreservation objectとして自動的にtransportしていない。proof-class preservationを言うには、各specificationのproof syntax/equalityとclasses間のmapを別途固定する必要がある。本稿のP6はその理由で限定的にしか判定していない。

---

## 15. Useful surviving observation

今回残せる最大限のstatementは次である。

> Preservation under specification change is not a single property. State the
> translation and the exact object being preserved: literal syntax,
> derivability, old-language consequence, semantic satisfaction, or proof
> data.

さらにT2/T3は次を具体化した。

> A change can preserve derivability while changing proof representation,
> citation structure, proof length, or available vocabulary.

これはnew theoryではなく、preservation claimのdomain/codomainとdirectionを明記するaudit disciplineである。

---

## 16. Kill criteria

| criterion | outcome |
|---|---|
| preservation left undefined | not triggered; P0–P6とsemantic claimを分離 |
| no explicit source/target | not triggered; T1–T4 each specify both |
| no map | not triggered; \(\rho\), identity inclusion, \(i/\tau\), theory inclusion |
| preservation from superficial similarity | not triggered; structural induction/replay/elimination/countermodelを使用 |
| derived lemma addition treated as deep result | not triggered; same deductive closureというstandard factに限定 |
| definitional extension unrestricted by language | not triggered; old-language scopeを明記 |
| monotonicity mistaken for equivalence | not triggered; Commでreflection failure |
| proof translation inferred from theorem sets | not triggered; explicit node replacementを記録 |
| semantics inferred without bridge assumptions | not triggered; valuation maps/soundnessを別記 |
| result becomes “everything depends on specification” | not triggered; fixed mapsでprecise YES/NOを得た |
| essence/intrinsic terminology used positively | not triggered; all rejected |
| project jargon replaces standard terms | not triggered in the analysis |

### Overall verdict

新しいinvariant theoryとしては **KILL**。audit checklistとしては **RETAIN, limited**。最も有用なのはpreservationのobject、scope、direction、evidenceを同時に書くことだけである。

---

## 17. Executable-check decision

companion scriptは作成しない。

理由：

- T1のgeneral claimはderivation induction、T2はderived-proof substitution、T3はdefinitional-elimination induction、T4はmonotonicityと既存countermodelで支えられる。
- finite examplesを再計算するscriptはこれらgeneral preservation resultsのproofにならない。
- 前 pilotのlambda-term checkerを再利用する必要もない。今回はfixed raw term setのnormalizationではなくspecification間translationが対象だからである。

codeを追加しないことがevidenceを弱めるcaseではない。

---

## 18. Final report

1. **Exact working question:** \(S_0\to S_1\) のchangeで、どのjudgment/objectがどのdirectionに、どのstandard propertyによりpreservedされるか。
2. **Specifications tested:** propositional natural deductionのrenamed signatures、addition theory before/after derived lemmas、propositional definitional extension、addition theory before/after induction。
3. **Transformations:** bijective renaming \(\rho\)、same-language axiom addition、fresh-symbol inclusion/elimination \(i/\tau\)、strict theory inclusion。
4. **Preservation notions:** literal well-formedness、formula translation、forward derivability、reflection/iff、semantic satisfaction under model maps、proof translation、raw proof identity。
5. **Renaming result:** all translated derivability judgments and proof trees correspond bijectively; literal syntax does not。
6. **Derived-lemma result:** \(\Gamma_+\) and \(\Gamma_+'\) have the same deductive closure; proofs can shorten/change citation structure。
7. **Definitional-extension result:** \(d\leftrightarrow(P\land Q)\) is conservative for old-language formulas via elimination; extended vocabulary/theorem strings and proof records differ。
8. **Strengthening result:** adding induction preserves source derivations forward by monotonicity but reflection fails for Comm by the existing countermodel。
9. **Strongest derivability-preserved/proof-changed example:** adding \(L_1,L_2\) leaves every theorem unchanged while named leaves replace inline derivations。
10. **Strongest one-way example:** \(\Gamma_+\setminus I\subseteq\Gamma_+\); Comm is derivable only on the stronger side。
11. **One notion covering all cases?:** **NO.** renaming isomorphism、deductive equivalence、old-language conservativity、one-way monotonicity differ。
12. **Did “preserved theorem” decompose?:** **YES**, into distinct standard syntactic、semantic、and proof-translation claims。
13. **Strongest negative result:** no theorem-intrinsic preserved object emerged; the whole analysis reduces to standard translation/conservativity/monotonicity theory。
14. **Strongest audit observation:** always state map、object、scope、direction、evidence before saying “preserved.”
15. **Anything beyond standard theory?:** **NO.** only an operational checklist survived。
16. **Another pilot warranted?:** **NO by default.** T1–T4 provide clean iff、conservative、and one-way controls, while novelty is exhausted。
17. **Exact next falsification question if pursued:** for two standard proof calculi connected by a published sound-and-complete translation, does derivability equivalence lift to a faithful map on proofs modulo each calculus’s fixed proof equality? Only that pre-specified cross-calculus question would test P6 rather than repeat P0–P5。

---

## 19. Final self-audit

| check | answer |
|---|---|
| Did I define exactly what “preserved” means? | **Yes.** every claim is assigned to P0–P6 or explicit semantic transport。 |
| Did I distinguish literal identity from translation? | **Yes.** T1 is the clean counterexample。 |
| Did I distinguish forward preservation from reflection? | **Yes.** T4 has forward only。 |
| Did I distinguish theorem-set preservation from proof preservation? | **Yes.** T2/T3 record proof changes。 |
| Did I restrict conservativity correctly? | **Yes.** T3 is old-language only; T2 is same-language deductive equivalence。 |
| Did I distinguish derived-theorem addition from language extension? | **Yes.** T2 and T3 are separate。 |
| Did I call preserved structure essential? | **No.** no intrinsic claim is made。 |
| Did I use standard terminology? | **Yes.** renaming、translation、conservativity、monotonicity、reflection。 |
| Did I preserve prior negative results? | **Yes.** no essence、universal invariant、or nontermination claim。 |
| Did I invent a new invariant theory? | **No.** P0–P6 are a checklist, not formal taxonomy。 |

### Closing verdict

specification changeの下で何かがpreservedされるかは、changeだけでは決まらない。chosen map、formula scope、direction、そして対象がderivability、semantics、proof dataのどれかを固定すると、ordinary mathematicsとしてpreciseに決まる。

T1–T4に共通するtheorem-intrinsic objectは抽出されなかった。得られたのは、同じ “preserved” という語でisomorphism、deductive equivalence、old-language conservativity、one-way monotonicityを混同しないというstandard disciplineだけである。

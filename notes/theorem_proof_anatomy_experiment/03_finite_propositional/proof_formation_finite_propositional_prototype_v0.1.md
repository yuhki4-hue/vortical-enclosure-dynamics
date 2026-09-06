# Proof-Formation Finite Propositional Prototype v0.1

- **Status:** exploratory finite prototype after the Phase-0 passage
- **Environment:** finite propositional semantics only
- **Purpose:** separate a reconstructible transition core from episode-boundary-dependent move coding in the smallest fully explicit setting
- **Date:** 2026-09-05

## 0. Status / non-claims

This document is an **exploratory finite prototype**. It is:

- not a theorem about all proof formation;
- not a theory of mathematical discovery;
- not a Gödel generalization;
- not a geometry theorem;
- not evidence that all M1–M17 admit propositional realization;
- not evidence that the K/A/R/D/U dimensions are scalar, vector, independent, ordered, or optimizable;
- not a proof that episode boundaries are objective;
- not a proof that transition-core reconstructibility in the toy corpus generalizes beyond the corpus.

The success condition is limited to this: **finite propositional logic makes the meanings and failure conditions of a few formation moves explicit**. The prototype does not reinterpret the Reader 02 / Reader 03 records to force agreement. It uses their adjudicated qualitative result only as motivation: the main before/failure/after/status structure was stable, while some move codes depended on claim and episode boundaries.

## 1. Base formal setting

Fix a finite set of propositional variables

\[
V=\{p_1,\ldots,p_n\}
\]

and let

\[
\Omega=\{0,1\}^n
\]

be the set of all valuations. For a propositional formula \(\varphi\), define

\[
M(\varphi)=\{\omega\in\Omega:\omega\models\varphi\}.
\]

For a finite set of formulas \(H\), define

\[
M(H)=\bigcap_{h\in H}M(h),
\qquad M(\varnothing)=\Omega.
\]

A claim candidate is initially represented as

\[
X=(H,C),
\]

where \(H\) is a finite set of assumptions and \(C\) is the target formula. This prototype uses semantic consequence, not provability:

\[
H\models C
\quad\Longleftrightarrow\quad
M(H)\subseteq M(C).
\]

When consequence fails, define the **counterexample region**

\[
E(H,C)=M(H)\setminus M(C).
\]

Every \(\omega\in E(H,C)\) is a concrete failure witness. Here \(E\) is only a working object: a finite set of valuations at which all assumptions hold and the target fails. No further mathematical structure is attributed to it.

## 2. Minimal transition core

A failure-driven transition record contains five typed parts:

1. **Before:** \(X=(H,C)\).
2. **Failure witness:** a displayed \(\omega\in E(H,C)\).
3. **Move:** one explicitly defined transformation.
4. **After:** \(X'=(H',C')\), or a withdrawal record plus an optional successor claim.
5. **Terminal relation:** either \(H'\models C'\) or \(H'\not\models C'\), except that withdrawal fixes the original status without making the original consequence true.

For a consequence-seeking move, the record may be written compactly as

\[
(H,C;\omega)\longrightarrow_M(H',C').
\]

The notation does not identify an episode boundary by itself. In particular, it does not decide whether \((H',C')\) is a revised state of the same claim or a new successor claim. That distinction is tested in §§7–8.

## 3. Prototype moves

Only M1, M2, a finite-domain surrogate related to M3/M4, and M17 receive explicit treatment.

### 3.1 M1 — assumption strengthening

For a finite formula set \(B\),

\[
(H,C)\longrightarrow_{M1}(H\cup B,C).
\]

Because

\[
M(H\cup B)=M(H)\cap M(B),
\]

the formal success condition is

\[
M(H\cup B)\subseteq M(C),
\]

equivalently

\[
E(H\cup B,C)=\varnothing.
\]

Formal success alone does not establish that the transition is an acceptable repair. In particular, \(B=\{C\}\), an inconsistent \(H\cup B\), and a post-hoc filter require the controls in §4.

### 3.2 M2 — conclusion weakening

Choose \(C'\) such that

\[
M(C)\subseteq M(C'),
\]

that is, \(C\models C'\). Then

\[
(H,C)\longrightarrow_{M2}(H,C').
\]

The formal success condition is

\[
M(H)\subseteq M(C').
\]

M2 changes the target while keeping the assumptions fixed. This is different from removing valuations by adding assumptions.

### 3.3 Finite-domain surrogate for scope restriction

Formula-class restriction and model-class restriction have much less of their original theoretical content in a finite propositional universe. This prototype therefore does **not** identify the following operation with M3 or M4.

Introduce an admissible valuation set \(S\subseteq\Omega\) and define

\[
H\models_S C
\quad\Longleftrightarrow\quad
M(H)\cap S\subseteq M(C),
\]

and

\[
E_S(H,C)=(M(H)\cap S)\setminus M(C).
\]

A scope restriction replaces \(S\) by \(S'\subseteq S\), leaving \(H\) and \(C\) unchanged. Its success condition is

\[
E_{S'}(H,C)=\varnothing.
\]

This is a **finite-domain surrogate for scope restriction**, not a realization of the formula-language distinctions in M3 and not a full realization of the object/model-class distinctions in M4.

### 3.4 M17 — withdrawal

For an original claim \(X=(H,C)\) with \(H\not\models C\), M17 records

\[
\operatorname{status}(X)=\texttt{withdrawn}.
\]

It does not alter \(H\) or \(C\) so that \(H\models C\), and it does not erase \(E(H,C)\). If a narrower or conditional statement is subsequently introduced, the prototype may record a distinct successor

\[
X'=(H',C')
\]

with its own identity and consequence status. M17 is therefore not a consequence-producing repair. It is a terminal operation that honestly fixes the failure of the original claim.

## 4. Trivial rescue / target leakage controls

Unrestricted M1 can make any target formally successful. The transition record therefore carries a non-numeric typed control flag. More than one positive flag may apply; no priority or aggregate value is assigned.

### 4.1 T1 — direct target insertion

If \(C\in B\), then

\[
H\cup\{C\}\models C.
\]

The target has been inserted directly among the assumptions. Record:

`DIRECT TARGET INSERTION`

This is formally successful but is not treated on the same footing as a nontrivial repair.

### 4.2 T2 — inconsistent repair

If \(H\cup B\) is inconsistent, then

\[
M(H\cup B)=\varnothing.
\]

Consequently, \(M(H\cup B)\subseteq M(C)\) for every target \(C\). In this semantic prototype, the effect is explained by inclusion from the empty model set, not by invoking a syntactic proof rule. Record:

`INCONSISTENT REPAIR`

### 4.3 T3 — post-hoc domain filter

Suppose \(B\) is selected after the failure is known, solely so that

\[
M(H\cup B)\subseteq M(C),
\]

for example so that \(M(H\cup B)=M(H)\cap M(C)\). Record:

`POST-HOC DOMAIN FILTER`

The truth table can verify the set relation but cannot determine why or when \(B\) was selected. Therefore this flag requires an explicit history or provenance statement; it is not inferred from successful exclusion alone.

### 4.4 No positive flag or missing provenance

- `NO FLAG` means that T1 and T2 are false and the transition record explicitly supplies non-post-hoc selection provenance.
- `UNKNOWN` means that T1 and T2 are false but the record does not determine whether T3 applies.

Together these implement the requested `NO FLAG / UNKNOWN` alternative without quantifying ad hocness or naturalness.

## 5. Counterexample-region behavior

### 5.1 M1

Direct calculation gives

\[
\begin{aligned}
E(H\cup B,C)
&=(M(H)\cap M(B))\setminus M(C)\\
&=E(H,C)\cap M(B).
\end{aligned}
\]

Thus assumption strengthening removes those prior counterexample valuations that fail at least one new assumption.

### 5.2 M2

If \(M(C)\subseteq M(C')\), then

\[
E(H,C')=M(H)\setminus M(C')
\subseteq
M(H)\setminus M(C)=E(H,C).
\]

Thus conclusion weakening can also shrink the counterexample region.

### 5.3 Scope restriction surrogate

If \(S'\subseteq S\), then

\[
E_{S'}(H,C)
=
(M(H)\cap S')\setminus M(C)
\subseteq
(M(H)\cap S)\setminus M(C)
=E_S(H,C).
\]

M1, M2, and the scope surrogate can therefore all shrink the counterexample set. They are nevertheless different operations:

- M1 changes the assumption set;
- M2 changes the target formula;
- the scope surrogate changes the admissible valuation set;
- M17 changes the original claim's status and may introduce a separately identified successor, without requiring any shrinkage of the original \(E(H,C)\).

The common set effect does not make the moves identical.

## 6. Toy non-identifiability example

Let \(V=\{p,q\}\), with valuations abbreviated by

\[
\omega_{ab}(p)=a,\qquad \omega_{ab}(q)=b.
\]

Start from

\[
H=\{p\lor q\},\qquad C=p.
\]

Then

\[
M(H)=\{\omega_{01},\omega_{10},\omega_{11}\},
\quad
M(C)=\{\omega_{10},\omega_{11}\},
\quad
E(H,C)=\{\omega_{01}\}.
\]

The same initial failure and the same terminal observation “the relevant counterexample set is empty” can arise by at least three typed histories:

| Route | Explicit operation | After-state | Terminal calculation |
|---|---|---|---|
| Repair A | M1 with \(B=\{\neg q\}\) | \((\{p\lor q,\neg q\},p)\) | \(M(H\cup B)=\{\omega_{10}\}\subseteq M(p)\) |
| Repair B | M2 with \(C'=p\lor q\) | \((\{p\lor q\},p\lor q)\) | \(M(H)\subseteq M(p\lor q)\) |
| Repair C | scope surrogate with \(S'=\Omega\setminus\{\omega_{01}\}\) | \((H,C)\) evaluated over \(S'\) | \(M(H)\cap S'=\{\omega_{10},\omega_{11}\}\subseteq M(p)\) |

This is a **toy non-identifiability example**, not a theorem. If the record preserves the fully typed after-state—assumptions, target, admissible set, and operation history—the three routes are distinguishable. If it preserves only the before failure, a successful terminal relation, and elimination of the displayed counterexample, move identity is not recoverable. Counterexample elimination alone is therefore an insufficient move record.

## 7. Episode-boundary sensitivity prototype

Use exactly the same formulas and witness as in §6, with \(B=\{\neg q\}\).

### Segmentation A — one repaired claim

Maintain one claim identity \(x_0\):

\[
X_0=(x_0,\{p\lor q\},p)
\longrightarrow_{M1}
X_0'=(x_0,\{p\lor q,\neg q\},p).
\]

The witness is \(\omega_{01}\). The after-state is semantically successful because its assumption models are \(\{\omega_{10}\}\). The terminal record reads: “the same claim identity is established under strengthened assumptions.”

### Segmentation B — withdrawn original plus distinct successor

Keep the original identity and its failure fixed:

\[
X_0=(x_0,\{p\lor q\},p),
\qquad
\operatorname{status}(X_0)=\texttt{withdrawn}.
\]

Then introduce a distinct successor:

\[
X_1=(x_1,\{p\lor q,\neg q\},p),
\qquad x_1\ne x_0,
\]

for which \(\{p\lor q,\neg q\}\models p\). On this segmentation, M17 applies to \(X_0\); the establishment of \(X_1\) is recorded separately and is not represented as an M1 rescue of \(X_0\).

### What changes with the boundary

| Record aspect | Segmentation A | Segmentation B |
|---|---|---|
| claim identity | \(x_0\) continues through changed assumptions | \(x_0\) ends; \(x_1\) begins |
| move taken on original | M1 | M17 |
| original terminal status | established under strengthened assumptions | withdrawn |
| retained original scope | original assumption scope is not retained, but identity is | original scope remains attached to the failed/withdrawn record |
| successor status | not separate | \(x_1\) established |
| target-leakage interpretation | flag attaches to the repair of \(x_0\) | the same provenance concern attaches to construction of \(x_1\), not to a rescue of \(x_0\) |

Neither segmentation is declared correct by the propositional formulas. If \(\neg q\) was selected only after observing \(\omega_{01}\), `POST-HOC DOMAIN FILTER` remains relevant under either segmentation; changing identity does not remove the control. If its selection provenance is absent, the flag is `UNKNOWN`.

This is the formal toy analogue of the blind-reader finding “same source material → different episode boundary → different move coding.” It does not decide any disputed boundary in the corpus.

## 8. Claim identity

The pair \(X=(H,C)\) specifies propositional content but does not encode whether a later pair is:

- the same claim repaired;
- the old claim withdrawn;
- a newly introduced conditional successor.

For §§7 and 9E only, use the minimal extension

\[
X=(\mathit{id},H,C).
\]

The identifier is a bookkeeping token, not a semantic property derived from \(M(H)\) or \(M(C)\). Two claims may have the same formulas and different identifiers, or one identifier may be continued across a recorded revision. This extension makes the two histories expressible, but it does not prove that the chosen identity or episode boundary is objective. It is not proposed here as a new formal framework schema.

## 9. Small worked examples

All examples use

\[
V=\{p,q\},
\qquad
\Omega=\{\omega_{00},\omega_{01},\omega_{10},\omega_{11}\}.
\]

### Example A — pure M1 success

- \(V=\{p,q\}\), \(\Omega=\{\omega_{00},\omega_{01},\omega_{10},\omega_{11}\}\).
- \(H=\{p\lor q\}\), \(C=p\).
- \(M(H)=\{\omega_{01},\omega_{10},\omega_{11}\}\).
- \(M(C)=\{\omega_{10},\omega_{11}\}\).
- \(E(H,C)=\{\omega_{01}\}\); choose witness \(\omega_{01}\).
- **Move:** M1 with \(B=\{\neg q\}\).
- **After:** \(H'=\{p\lor q,\neg q\}\), \(C'=p\); \(M(H')=\{\omega_{10}\}\), \(M(C')=\{\omega_{10},\omega_{11}\}\), and \(E(H',C')=\varnothing\).
- **Status:** established under strengthened assumptions. For this example the addition is stipulated to have independent pre-failure provenance, so the control is `NO FLAG`; the truth table alone could not supply that provenance.

### Example B — pure M2 success

- \(V=\{p,q\}\), \(\Omega=\{\omega_{00},\omega_{01},\omega_{10},\omega_{11}\}\).
- \(H=\{p\lor q\}\), \(C=p\).
- \(M(H)=\{\omega_{01},\omega_{10},\omega_{11}\}\).
- \(M(C)=\{\omega_{10},\omega_{11}\}\).
- \(E(H,C)=\{\omega_{01}\}\); choose witness \(\omega_{01}\).
- **Move:** M2 with \(C'=p\lor q\). Indeed, \(M(p)\subseteq M(p\lor q)\).
- **After:** \(H'=H\), \(M(C')=\{\omega_{01},\omega_{10},\omega_{11}\}\), and \(E(H',C')=\varnothing\).
- **Status:** the weakened conclusion is established; the original target \(p\) is not established from \(H\).

### Example C — scope-restriction surrogate

- \(V=\{p,q\}\), \(\Omega=\{\omega_{00},\omega_{01},\omega_{10},\omega_{11}\}\).
- \(H=\{p\lor q\}\), \(C=p\), initially \(S=\Omega\).
- \(M(H)=\{\omega_{01},\omega_{10},\omega_{11}\}\).
- \(M(C)=\{\omega_{10},\omega_{11}\}\).
- \(E_S(H,C)=\{\omega_{01}\}\); choose witness \(\omega_{01}\).
- **Move:** replace \(S\) by \(S'=\{\omega_{00},\omega_{10},\omega_{11}\}\).
- **After:** \(H'=H\), \(C'=C\), \(M(H')\cap S'=\{\omega_{10},\omega_{11}\}\), and \(E_{S'}(H',C')=\varnothing\).
- **Status:** established only relative to \(S'\). The unrestricted claim over \(\Omega\) still fails. This is the finite-domain surrogate, not M3 or M4 itself.

### Example D — trivial rescue / target leakage

Here \(V=\{p,q\}\) and \(\Omega=\{\omega_{00},\omega_{01},\omega_{10},\omega_{11}\}\). The common before-state is again

\[
H=\{p\lor q\},\quad C=p,\quad
M(H)=\{\omega_{01},\omega_{10},\omega_{11}\},\quad
M(C)=\{\omega_{10},\omega_{11}\},\quad
E(H,C)=\{\omega_{01}\}.
\]

Choose \(\omega_{01}\) as witness.

| Case | Move | After model set | After consequence | Status/control |
|---|---|---|---|---|
| D1 | M1 with \(B_1=\{p\}=\{C\}\) | \(M(H\cup B_1)=\{\omega_{10},\omega_{11}\}\) | \(H\cup B_1\models p\) | formally successful only; `DIRECT TARGET INSERTION` |
| D2 | M1 with \(B_2=\{\neg(p\lor q)\}\) | \(M(H\cup B_2)=\varnothing\) | empty-set inclusion gives \(H\cup B_2\models p\) | formally successful only; `INCONSISTENT REPAIR` |
| D3 | M1 with \(B_3=\{p\lor\neg q\}\), stipulated to have been chosen after the failure solely to remove \(\omega_{01}\) | \(M(H\cup B_3)=\{\omega_{10},\omega_{11}\}=M(H)\cap M(C)\) | \(H\cup B_3\models p\) | formally successful only; `POST-HOC DOMAIN FILTER` |

All three have empty after-counterexample sets. None is thereby promoted to an acceptable repair.

### Example E — one repair versus withdrawal plus successor

- \(V=\{p,q\}\), \(\Omega=\{\omega_{00},\omega_{01},\omega_{10},\omega_{11}\}\).
- Original \(H=\{p\lor q\}\), \(C=p\).
- \(M(H)=\{\omega_{01},\omega_{10},\omega_{11}\}\).
- \(M(C)=\{\omega_{10},\omega_{11}\}\).
- \(E(H,C)=\{\omega_{01}\}\); witness \(\omega_{01}\).
- The shared mathematical after-material is \(H^+=\{p\lor q,\neg q\}\), \(C^+=p\), with \(M(H^+)=\{\omega_{10}\}\) and \(E(H^+,C^+)=\varnothing\).
- **Segmentation A move/after/status:** M1, \((x_0,H,C)\to(x_0,H^+,C^+)\); \(x_0\) is established under strengthened assumptions.
- **Segmentation B move/after/status:** M17 fixes \((x_0,H,C)\) as withdrawn; a distinct \((x_1,H^+,C^+)\) is established as successor.

The valuations and formulas do not select between these records. The difference lies in identity continuity and episode segmentation.

## 10. Tiny checker

`proof_formation_finite_propositional_checker_v0.1.py` accompanies this note. It uses only the Python standard library and performs:

- valuation enumeration;
- truth-table evaluation through simple callables;
- semantic consequence and counterexample-region calculation;
- M1 assumption-set extension;
- M2 conclusion replacement with a weakening check;
- admissible-set restriction;
- the four trivial-rescue control outputs.

It verifies the calculations in Examples A–D and the common after-material in Example E. It is only a checker for these finite examples, not a proof device for a broader theory. `POST-HOC DOMAIN FILTER`, `NO FLAG`, and `UNKNOWN` depend on explicit provenance inputs because valuation enumeration cannot recover selection history.

## 11. Relation to M1–M17

| Formation move | Finite propositional realization status | Direct / surrogate / not attempted | Reason |
|---|---|---|---|
| M1 — assumption strengthening | Explicitly defined | direct | Add finite formulas to \(H\); model intersection and success are computable. |
| M2 — conclusion weakening | Explicitly defined | direct | Replace \(C\) by \(C'\) with \(M(C)\subseteq M(C')\). |
| M3 — formula-class / language restriction | No direct realization | surrogate only | An admissible valuation set can mimic restricted evaluation but does not represent formula classes or languages. |
| M4 — object / domain / model-class restriction | Limited finite analogue | surrogate only | Restricting \(S\subseteq\Omega\) represents only a finite admissible domain, not realistic object/model-class structure. |
| M5 — quotient / equivalence-class target reformulation | Unspecified | not attempted | No equivalence-class target structure is introduced. |
| M6 — formal theory extension | Unspecified | not attempted | The prototype has valuations and semantic consequence, not formal theories or axiom progressions. |
| M7 — model / estimand / target-class revision | Unspecified | not attempted | No estimand or model-revision semantics is supplied. |
| M8 — proof-resource addition or route change | Unspecified | not attempted | Proof resources and routes are outside truth-table consequence. |
| M9 — reduction with specified preservation | Unspecified | not attempted | No calculi, reductions, or preservation classes are represented. |
| M10 — interpretation / translation | Unspecified | not attempted | No translation between languages, models, or theories is introduced. |
| M11 — internalization | Unspecified | not attempted | Syntax and proof predicates are not represented inside the object language. |
| M12 — metalevel shift / external evaluation | Unspecified | not attempted | The finite semantic evaluator is not itself coded as a formation transition. |
| M13 — comparison / calibration | Unspecified | not attempted | No comparison or calibration relation is introduced. |
| M14 — disambiguation / type correction | Explicit claim retyping is representable only as a record | not attempted (partial representability) | A reader can rewrite typed claim components, but no semantics of type correction is formalized here. |
| M15 — prior-art absorption | Unspecified | not attempted | Historical and literature relations are absent. |
| M16 — conversion to empirical / comparative question | Unspecified | not attempted | Empirical questions, controls, and corpora are absent. |
| M17 — withdrawal / abandonment / negative-result fixation | Explicitly defined as status/identity operation | direct | The failed original is marked withdrawn; any successor receives a separate identity. |

The table is deliberately conservative. A truth-table encoding that happens to resemble a move is not enough to claim realization of that move's source-level role.

## 12. Explicit limitations

This prototype does not yet handle:

- proof resource addition;
- proof route change;
- theory extension;
- interpretation;
- internalization;
- metalevel shift;
- reflection;
- comparison/calibration;
- prior-art absorption;
- empirical conversion;
- theorem identity in realistic mathematics;
- proof length;
- proof complexity;
- discovery history;
- human intention;
- naturalness / arbitrariness;
- publication practice;
- downstream propagation D;
- reuse U;
- K/A/R/D/U aggregate structure.

Counterexample-region inclusion is only set inclusion among explicitly enumerated valuations. It is not called or used as a distance, geometry, or strength order.

## 13. Kill / revise criteria applied to the prototype

- **RETAIN — satisfied:** M1 changes \(H\), M2 changes \(C\), the scope surrogate changes \(S\), and M17 changes status/identity. These differences remain explicit in finite semantics.
- **REVISE — triggered for the bare pair representation:** without an identity token, the record cannot express the distinction between same-claim repair and withdrawn original plus successor. The local \((\mathit{id},H,C)\) extension is therefore needed for this test.
- **DOWNGRADE — triggered for move inference from counterexample sets:** changes in \(E\) alone cannot identify whether M1, M2, or the scope surrogate occurred, and they say nothing sufficient about M17.
- **KILL — not triggered:** before, failure witness, after, and terminal status can be written consistently for every worked example.

These are separate experimental dispositions, not a score or ranking: retain the explicit finite core, revise identity bookkeeping, downgrade any claim that counterexample-set behavior identifies a move, and do not kill the prototype.

## 14. Final verdict

1. **Directly formalized:** M1, M2, and M17; semantic consequence, concrete failure witnesses, after-states, and terminal relations are fully enumerable.
2. **Surrogate only:** restriction of an admissible valuation set supplies a finite-domain surrogate related to M3/M4, but is not identified with either move.
3. **Claim identity:** needed to express the difference between a continuing repaired claim and a withdrawn original followed by a distinct successor. The identifier records a boundary choice; it does not validate that choice.
4. **Trivial-rescue control:** necessary because direct target insertion, inconsistency, and post-hoc filtering can all make the after-counterexample set empty.
5. **Information lost by counterexample sets:** the changed component, operation history, identity continuity, original terminal status, and selection provenance are not determined by counterexample elimination.
6. **Episode-boundary sensitivity:** identical formulas can support either a single M1 record or an M17 original plus an established successor, with different `move_taken` and statuses.
7. **Why generalization to M1–M17 is withheld:** most moves require proof resources, theories, translations, metalevel relations, prior art, empirical evidence, or realistic claim identity, none of which is present in finite truth-table semantics.
8. **Prototype verdict:** **RETAIN** the M1/M2/scope-surrogate/M17 separation; **REVISE** the bare claim representation with local identity bookkeeping; **DOWNGRADE** move inference from counterexample-set behavior alone; **KILL is not triggered**.

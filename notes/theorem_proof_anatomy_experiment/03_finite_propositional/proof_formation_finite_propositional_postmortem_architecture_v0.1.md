# Finite Propositional Prototype — Post-mortem / Architecture Note v0.1

- **Sources read:** [`prototype v0.1`](./proof_formation_finite_propositional_prototype_v0.1.md), [`checker v0.1`](./proof_formation_finite_propositional_checker_v0.1.py), [`stress test v0.1`](./proof_formation_finite_propositional_stress_test_v0.1.md), [`stress checker v0.1`](./proof_formation_finite_propositional_stress_checker_v0.1.py), [`inter-reader adjudication v0.1`](../02_proof_formation/proof_formation_inter_reader_adjudication_v0.1.md), [`Reader 02/03 blind comparison v0.1`](../02_proof_formation/proof_formation_reader_02_03_blind_comparison_v0.1.md)
- **Date:** 2026-09-05
- **Files modified:** none. This file is additive.

## 0. Status and posture

- This is a **post-mortem note**. It is **architecture clarification only**.
- **Not a new framework.** **Not a v0.2 proposal.** **Not a repair plan.** No schema, no field list, no implementation is designed here.
- **Not a theorem.** Every quantified statement below is an observation over an explicitly stated finite range, taken from the stress test's enumeration.
- **Not a general theory of proof formation**, and **not a claim that the finite prototype explains realistic mathematics**. Finite propositional semantics is a setting in which every subset of the valuation space is definable; several distinctions die there for that reason alone, and their death there says nothing about their status elsewhere.
- **No new move codes. No new scoring scheme. No geometry, metric, lattice or topology. No claim that episode boundaries are objective.** No naturalness criterion, no ad hocness quantification.
- **The blind-reader results are not rewritten.** They are referenced only where this note says so explicitly, and only as prior records.

**The single question this note answers:** of the distinctions prototype v0.1 treated as living in its semantics, which ones were actually carried by how a record was typed and how a history was written down? The answer is organized by layer, after the fact, from the stress-test findings.

---

## 1. The v0.1 architecture, reconstructed after the fact

Prototype v0.1 does **not** present itself as a two-layer construction, and nothing below should be read as claiming that it did. It defines a semantic setting, then adds record apparatus where the semantic setting turned out not to reach — §8's identity token is introduced "for §§7 and 9E only", and §4's controls are introduced because "unrestricted M1 can make any target formally successful". Read forward, that is a sequence of local additions. Read backward from the stress test, the additions fall into a pattern, and the pattern is what this note describes.

### 1.1 The ingredients, sorted retrospectively

| Ingredient | Where v0.1 introduces it | Role visible after the stress test |
|---|---|---|
| \(\Omega\), \(M(H)\), \(M(C)\) | §1 | semantic; fully enumerable |
| \(H\), \(C\) | §1, as the claim \(X=(H,C)\) | semantic content, and also two of the record's slots |
| semantic consequence \(H\models C\) | §1 | semantic |
| \(E(H,C)\) | §1, "only a working object" | derived; display of failure |
| admissible scope \(S\) | §3.3, **not part of \(X\)** | semantic in effect, typed in role |
| move label (M1 / M2 / scope / M17) | §3 | record typing |
| identity token \(\mathit{id}\) | §8, "for §§7 and 9E only" | record/history |
| terminal status | §2 item 5, §3.4 | mixed: two values derived, one not |
| provenance flag (T1/T2/T3, `NO FLAG`, `UNKNOWN`) | §4 | provenance, partly computed |
| episode segmentation | §7, as two alternative readings | history |
| successor relation | §2 ("a withdrawal record plus an optional successor claim"), §3.4 | history |

### 1.2 The structural fact underneath everything else

v0.1 never fixes what a claim record consists of. §1 says \(X=(H,C)\). §3.3 evaluates relative to an \(S\) that is not in \(X\). §8 uses \(X=(\mathit{id},H,C)\), scoped to two sections. So there are three different carriers in one document.

This matters because of a second fact the stress test made explicit: **everything v0.1 evaluates — every success condition in §§3–5 — is a function of the pair \(\big(M(H)\cap S,\ M(C)\big)\).** The evaluation therefore factors through an object strictly coarser than any of the three carriers. Distinctions that live only in the difference between carrier and evaluated pair are record distinctions, whatever section of the note they appear in.

---

## 2. What was genuinely semantic

"Genuinely semantic" is used here in one narrow sense only: **truth tables alone can audit it**, without any statement about how the record was written or how the claim came about.

- valuation membership \(\omega\models\varphi\);
- model sets \(M(\varphi)\), \(M(H)=\bigcap_{h\in H}M(h)\), \(M(\varnothing)=\Omega\);
- semantic consequence \(M(H)\subseteq M(C)\), and its scoped form \(M(H)\cap S\subseteq M(C)\);
- the counterexample region \(E(H,C)=M(H)\setminus M(C)\) and \(E_S(H,C)\), **as a computation** (its status as information is §7);
- failure-witness membership: whether a displayed \(\omega\) is in \(E(H,C)\);
- the M1 after-model-set calculation \(M(H\cup B)=M(H)\cap M(B)\), and §5.1's identity \(E(H\cup B,C)=E(H,C)\cap M(B)\);
- the M2 weakening direction \(M(C)\subseteq M(C')\), including its refusal of an incomparable target;
- whether a proposed target change is a **proper** weakening \(M(C)\subsetneq M(C')\) or a no-op;
- the scope subset relation \(S'\subseteq S\);
- inconsistency \(M(H\cup B)=\varnothing\);
- vacuous success, in both its forms — empty model set and empty admissible set;
- whether a recorded `established` or `failed` agrees with the after-state entailment;
- whether §3.4's M17 precondition \(H\not\models C\) holds.

All of these were re-derived by enumeration in the stress checker and hold. This layer is not in dispute, and nothing in this note weakens it.

Two entries deserve a flag. **Vacuous success** is semantic as a calculation but its two forms sit in different slots (\(M(H\cup B)=\varnothing\) versus \(S'=\varnothing\)), and only the first carries a control — that asymmetry is a record fact, not a semantic one. **Established/failed agreement** and the **M17 precondition** are semantic checks that v0.1 does not perform, because its checker has no status field; they are listed here as auditable-in-principle, and §10 separates that from implemented.

---

## 3. What looked semantic but was typed-record structure

This is the centre of the post-mortem.

### 3.1 M1 versus the scope surrogate

v0.1 §5.3 lists the moves as different because "M1 changes the assumption set; M2 changes the target formula; the scope surrogate changes the admissible valuation set", and closes: "The common set effect does not make the moves identical." That sentence is true. What the stress test establishes is **what makes it true**.

For every checked \((H,C)\): a scope restriction to \(S'\) is matched by M1 with \(B=\{\varphi_{S'}\}\), and an M1 with \(B\) is matched by the scope restriction \(S'=S\cap M(B)\), with identical surviving valuations, identical counterexample region, and identical terminal consequence. In finite propositional semantics every subset of \(\Omega\) is the model set of an explicit DNF over minterms, so assumption selection and admissible-set selection draw on the same supply of sets; and since the evaluation sees only \(\big(M(H)\cap S,\ M(C)\big)\), both moves act on the first component in the same way.

The consequence for architecture:

> The difference between "assumption strengthening" and "scope restriction" is **not** a result of the finite semantics. It is a function of which typed slot the record says was changed.

| Kept in the record | M1 versus scope distinguishable? |
|---|---|
| typed triple \((H,C,S)\), before and after | **yes** — the changed slot names the move |
| evaluated pair \((M(H)\cap S,\ M(C))\), before and after | no |
| counterexample regions, before and after | no |
| terminal consequence only | no |

This is the same phenomenon v0.1 §6 exhibits as its "toy non-identifiability example" and correctly refuses to call a theorem. The post-mortem point is narrower and more uncomfortable: v0.1 reads the difference off the record while presenting it, in §5.3 and §11, as a property of the operations.

### 3.2 M1 versus M2 versus the scope surrogate

v0.1 §5 observes that all three can shrink \(E\). The stress test's enumeration gives the stronger observation:

> Over the checked \((H,C)\) range, the after-counterexample regions reachable by M1, by M2 and by the scope surrogate form **the same family** — every subset of \(E(H,C)\).

Range and method, stated so the observation is not read as more than it is: all definable \(H,C\) for \(n=2\); a fixed deterministic sample of definable \(H,C\) for \(n=3\); the move parameter ranging over every subset of \(E(H,C)\); verified by enumeration through the v0.1 functions. **This is a stress-test observation on a checked finite range, not a theorem**, and it is not extended to any other setting. The reason it holds here is visible in v0.1's own identities together with finite definability, which is exactly the feature that will not be present in the settings the M-codes were written for.

Architecturally: counterexample-region behaviour does not narrow the move down even to a pair. The prototype's §13 DOWNGRADE ("changes in \(E\) alone cannot identify whether M1, M2, or the scope surrogate occurred") is correct, and the exception clause it might have been read to leave open — that the *empty* after-region case is special — is not there either.

One asymmetry does survive, and it survives in the record rather than in \(E\): M1 and scope shrink the left side of the inclusion, M2 grows the right side. That is visible in the typed slots and invisible in the counterexample regions.

### 3.3 The move label

Given a complete typed before/after record \((H,C,S)\to(H',C',S')\), the changed slot identifies which of M1 / M2 / scope occurred; the label adds nothing. Given only the evaluated sets, the label is the only thing that identifies the move.

Stated carefully, and without turning it into a claim about move labels in general: **within this prototype, the move label functions as a compressed restatement of the record's typing, not as a carrier of semantic content.** It is redundant exactly when the record is fully typed, and indispensable exactly when it is not. M17 is the exception and is treated in §6.

Two consequences worth separating:

1. The label cannot be *checked* against the semantics beyond the shape conditions of §2 — that an M1 record's \(H'\) is \(H\cup B\), that an M2 record's \(C'\) is a weakening, that a scope record's \(S'\) is a subset. Those are checks on the typing, not on the choice of label.
2. Two records with the same evaluated content and different labels are both consistent. The stress test's mutual simulation is precisely a construction of such pairs.

---

## 4. What was irreducibly historical or provenance-dependent

None of the following is recoverable from valuation semantics, at any level of implementation effort:

- post-hocness of a repair;
- why \(B\) was selected;
- why \(S\) or \(S'\) was selected;
- whether a scope restriction was independently justified;
- whether a successor is genuinely new;
- whether a claim identity should continue;
- whether a claim identity should break;
- which segmentation of a history is appropriate;
- whether a move was chosen before or after the failure was observed.

### 4.1 Why this is not a checker gap

The distinction that matters for the post-mortem is between *an unimplemented computation* and *a computation that does not exist*. The stress test settles this for the trivial/non-trivial repair boundary, and the argument is worth stating in full because it is the load-bearing finding of this section.

For every failing \((H,C)\) in the checked range, adding the DNF over \(\Omega\setminus E(H,C)\) makes M1 succeed. That \(B\) never triggers T1 (it is not the target) and triggers T2 only when \(M(H)\cap M(C)=\varnothing\). It produces exactly \(M(H\cup B)=M(H)\cap M(C)\) — which is **the shape v0.1 §4.3 itself offers as its example of a post-hoc domain filter**.

So the exact-filter repair and an independently motivated repair can occupy the same semantic position: same after-model set, same empty counterexample region, same terminal consequence. And the situation is worse than a shape test would fix. In v0.1's own worked examples, Example A (`NO FLAG`, provenance stipulated independent, \(B=\{\lnot q\}\)) leaves \(\{\omega_{10}\}\), while Example D3 (`POST-HOC DOMAIN FILTER`, \(B=\{p\lor\lnot q\}\)) leaves \(\{\omega_{10},\omega_{11}\}\). **The unflagged example discards strictly more than the flagged one.** A computed test for the exact-filter shape would therefore be evaded by discarding more than the counterexamples, which is what the unflagged example already does.

> Provenance dependence here is a property of the semantic landscape, not of the checker. §4.3's decision not to infer T3 from the set relation is, in retrospect, the right call for a reason v0.1 does not give: the shape it declines to infer from is evadable in the direction of *greater* restriction.

### 4.2 What this leaves the provenance layer doing

It is the only layer that can distinguish records which the semantic layer cannot separate at all. It is also the layer v0.1 supplies least: T3 is an input rather than a computation (correctly), the scope surrogate has no provenance apparatus whatsoever, and `UNKNOWN` is the honest default that most records will carry.

---

## 5. Claim identity post-mortem

### 5.1 What \(\mathit{id}\) did

- Made two histories into two records. Without it, v0.1 §9 Example E's Segmentation A and Segmentation B are the same record; with it they are two.
- Let a withdrawn original and an established successor be held simultaneously, without the successor's success being attributed to the original. This is the property that keeps §7's two segmentations from silently collapsing into "the claim was repaired".
- Gave a field on which an **internal** contradiction is mechanically detectable: a record asserting "same claim" while changing the token is caught.

### 5.2 What \(\mathit{id}\) did not do

- Decide whether a continuation is legitimate. The same token survives an arbitrary \((H,C)\to(H',C')\); nothing constrains how far content may change.
- Decide whether a successor is genuinely new.
- Justify an episode boundary. It records a boundary choice; it adjudicates none. v0.1 §8 says this, and the stress test confirms it in the strong form: no check discriminates between the two expressions.
- Prevent failure laundering by relabelling. Withdraw \(x_0\), introduce \(x_1\) carrying the exact counterexample filter as a fresh state: both records pass every mechanical check.
- Prevent replacement laundering by continuity. One token maintained through \(C\to\top\) passes as "same claim established".

The two failures are opposite in direction, which is the point: the token is unconstrained both ways. Unconstrained discontinuity launders a failure history; unconstrained continuity launders a replacement as a repair.

### 5.3 What the token therefore was

Descriptively — and **not** as proposed framework vocabulary, not as a term this note is introducing for reuse:

> \(\mathit{id}\) functioned as a **recorded identity assertion**, a bookkeeping token. It did not function as a **claim identity criterion**.

The distinction is that a criterion would constrain which records are admissible; the token only makes an assertion expressible and internally checkable against the record's own other fields. v0.1's §14 item 3 already says "The identifier records a boundary choice; it does not validate that choice", and the stress test found no case in which it did more than that.

---

## 6. Terminal status post-mortem

### 6.1 The split

| Status | Recomputable from the after-state? |
|---|---|
| `established` | yes — \(H'\models C'\) |
| `failed` | yes — \(H'\not\models C'\) |
| `withdrawn` | **no** |

A failed claim and a withdrawn claim can have identical semantic content: same \(H\), same \(C\), same \(M(H)\), same \(M(C)\), same non-empty \(E(H,C)\). What differs is the research-history disposition — that the claim's failure has been fixed as terminal rather than left open. No computation over valuations recovers that difference, because there is nothing in the valuations to recover it from.

The consequence is that status is **redundant exactly where the semantics reaches, and irredundant exactly at M17**.

### 6.2 Why M17 was the strongest surviving distinction

The stress test found M17 to be the one move whose distinctness does not depend on slot typing, and §6.1 explains why. M1, M2 and the scope surrogate are distinguished by which slot a record says changed (§3); remove the typing and they merge. M17 is distinguished by a status value that has **no semantic surrogate at all** — so there is nothing for it to merge with, and no typing decision it depends on.

This inverts the natural reading of the result. M17 did not survive because it was better grounded in the semantics than the other three. It survived because it was never semantic in the first place, and v0.1 located it correctly: §3.4 defines it as a status and identity operation, explicitly "not a consequence-producing repair". **A distinction survived precisely by being placed in the history layer rather than claimed for the semantic one.**

Two riders. First, this makes M17 the move most exposed to record-form problems rather than semantic ones — §9.3 below. Second, `withdrawn` is not thereby unauditable: a record that is semantically repaired and labelled withdrawn is a detectable internal contradiction. The non-recoverability is one-directional — you cannot compute the status, but you can check it against the rest of the record.

---

## 7. Counterexample region \(E\) post-mortem

- \(E(H,C)\) is computable from \(H\) and \(C\), and \(E_S(H,C)\) from \(H\), \(C\) and \(S\).
- Therefore \(E\) **is not independent information**. Removing it from a record loses nothing that the before-state does not already fix. v0.1's own §1 anticipates this — "\(E\) is only a working object" — and the minimality audit confirms it.
- \(E\) **does not identify formation history**: the reachable after-\(E\) families of M1, M2 and the scope surrogate coincide over the checked finite range (§3.2).
- \(E\) **remains useful** for displaying failure witnesses. §2 of the prototype requires "a displayed \(\omega\in E(H,C)\)", and that display is what makes a witness claim auditable at all: a record naming a witness outside \(E\) is mechanically caught, and a record naming no witness cannot be checked in that respect.

The two statements are not in tension and neither should be dropped:

> As a **data carrier**, \(E\) is redundant. As a **failure display**, it is useful.

What \(E\) was over-credited with, in retrospect, is discrimination. v0.1 §5 presents the three moves' effects on \(E\) as evidence that they are different operations that happen to share a set effect; the stress test shows the shared effect is total on the checked range. \(E\) shows *that* a claim fails and *where*; it does not show *what was done about it*.

---

## 8. Scope \(S\) post-mortem

Two faces, both real, and they point in different directions.

**Semantic reach.** Anything reachable by restricting \(S\) is reachable by M1 with the corresponding definable formula, and conversely. Dropping \(S\) from the prototype would lose no reachable evaluated state.

**Typed role.** Keeping \(S\) is what allows a record to distinguish "the assumptions were changed" from "the admissibility domain was changed". That distinction is not visible in the evaluated pair, and it is not recoverable once the record is reduced to model sets.

> Within this finite prototype, \(S\) carries more **typed-distinction** work than **semantic-necessity** work.

Three limits on that statement, all of which matter:

1. It is a statement about this prototype and this range, not about restriction as an operation.
2. It says nothing about M3 or M4. v0.1 §3.3 is explicit that the admissible-set surrogate is not identified with either, and §11 records both as "surrogate only". **No conclusion about M3 or M4 in general is drawn here**, and the fact that the surrogate collapses into M1 in finite propositional semantics is not evidence that formula-class or model-class restriction collapses anywhere else. If anything it is evidence that this setting is too poor to represent them.
3. The collapse depends on both selections being unconstrained. v0.1 constrains neither which \(B\) may be added nor which \(S'\) may be chosen. Whether a constrained version would separate them was not tested and is not proposed.

---

## 9. Rescue-control post-mortem

### 9.1 What each control actually covers

| Control | Covers | Does not cover |
|---|---|---|
| T1 direct target insertion | the target formula itself appearing in \(B\) — §4.1 states the condition as \(C\in B\), and the checker tests object identity | a semantically equivalent rewrite of the target, which succeeds and returns `NO FLAG` |
| T2 inconsistent repair | exactly \(M(H\cup B)=\varnothing\) | anything short of empty; a \(B\) leaving a single surviving valuation is unflagged |
| T3 post-hoc domain filter | whatever the provenance statement says | anything the record does not state — and by §4.1 above, the set-relation shape it would be inferred from is evadable |

Two coverage facts follow. **M2 has no control of any kind**: \(C'=\top\) is a legal weakening that succeeds against every \(H\). **The scope surrogate has no control of any kind**: \(S'=S\setminus E_S(H,C)\) always succeeds, and \(S'=\varnothing\) succeeds vacuously without anything corresponding to T2. The controls were written for M1 and were not carried to the operations that turned out to be able to imitate it.

### 9.2 Two failure modes that must not be merged

The stress test's most easily blurred finding, kept apart here:

**A. Provenance is unavailable.** The record does not say when or why \(B\) or \(S'\) was chosen, so T3 cannot be evaluated and the honest output is `UNKNOWN`. This is a missing-information problem. It is what v0.1 §4.4 is designed for, and it is handled correctly.

**B. The control cannot attach, because the record form contains no transition.** v0.1 §2 permits an After consisting of "a withdrawal record plus an optional successor claim", with no requirement that the successor be reached by a typed move. A successor entered as a *state* has no \(B\) and no \(H\to H\cup B\) step. T1, T2 and T3 are therefore not negative — they are **inapplicable**, having nothing to range over.

These are different in kind. B can occur when provenance is fully available and fully stated: a recorder may say exactly why the successor's assumption set was chosen and still produce a record to which no control attaches, because the controls are defined on transitions and the record is a state. Conversely A can occur on a perfectly well-formed transition. Treating B as a species of A would misdescribe it as a documentation gap, when it is a mismatch between where the controls live (typed transitions) and what record forms the schema permits (states).

### 9.3 The interaction with M17

B is reachable through the one move §6 identified as best located. Withdraw \(x_0\); introduce \(x_1\) as a state whose assumption set is the exact counterexample filter of the withdrawn claim; both records pass every mechanical check.

The post-mortem reading is **not** that M17 launders anything. M17 does exactly what §3.4 says: it fixes the original's failure and does not make \(H\models C\). What produces the hole is the combination of a withdrawal with a state-typed successor introduction — that is, a history-layer operation composed with a record-form permission. v0.1 §7 sees the concern in prose ("the same provenance concern attaches to construction of \(x_1\)") and has no mechanism that carries it, because the mechanism it would need lives in a different layer from the concern.

---

## 10. Mechanically auditable versus not

The essential column is the third: **why** something is not audited. "Not implemented in v0.1" and "not semantically recoverable" are different situations with different consequences, and collapsing them would misstate the post-mortem.

### 10.1 Mechanically auditable from truth tables

| Item | Implemented in v0.1? | Note |
|---|---|---|
| witness membership \(\omega\in E(H,C)\) | no | computed in the stress checker; **not implemented**, not unrecoverable |
| model sets, \(M(H)\), \(M(C)\) | yes | |
| semantic consequence, scoped and unscoped | yes | |
| M1 shape \(H'=H\cup B\) | partly — `m1` constructs it; nothing checks a claimed \(H'\) against it | **not implemented** as a check |
| M2 weakening \(M(C)\subseteq M(C')\) | yes | the one enforced direction constraint |
| M2 no-op \(M(C)=M(C')\) | no | **not implemented**; the check is available on the same truth tables |
| M1 no-op (surviving set unchanged) | no | **not implemented** |
| scope subset \(S'\subseteq S\) | yes | |
| inconsistency \(M(H\cup B)=\varnothing\) | yes (T2) | |
| `established`/`failed` against entailment | no — v0.1 has no status field | **not implemented** |
| M17 precondition \(H\not\models C\) | no — v0.1 has no M17 function | **not implemented** |
| internal identity-field consistency | no — v0.1 has no identity field | **not implemented** |
| direct target insertion, verbatim | yes (T1) | covers the verbatim case only |

Every row here is a computation over the same enumerated valuations. Where the answer is "no", the gap is coverage.

### 10.2 Not mechanically auditable from truth tables

| Item | Why not |
|---|---|
| post-hocness | there is nothing in the valuations that records when a formula was chosen |
| identity legitimacy | the token is not a function of \(M(H)\) or \(M(C)\) by construction |
| segmentation legitimacy | the same formulas support both segmentations of Example E, and both are consistent |
| successor novelty | a successor's content may coincide with, extend, or be unrelated to the predecessor's, in any combination, without semantic obstruction |
| independent justification of \(B\) or \(S'\) | successful and trivially successful repairs occupy the same semantic positions (§4.1) |
| researcher intent | absent from the setting entirely |
| move preference | no ordering exists here and none is introduced |
| naturalness / arbitrariness | not defined, and deliberately not defined |

Every row here is **not semantically recoverable**. Implementation effort does not move a row from 10.2 to 10.1.

---

## 11. Post-mortem descriptive decomposition

The following is a **descriptive summary of where v0.1's distinctions turned out to live**. It is not a taxonomy, not a schema, not a proposed layering for any successor, and nothing below is offered as a formal object. A different cut would be acceptable provided it keeps semantic / record / history / provenance apart, since that separation is what the stress test forced.

**Layer A — semantic content.** \(H\), \(C\), \(S\), model sets, consequence, failure witnesses. Auditable by truth tables alone. §2 above.

**Layer B — typed transition record.** Which slot changed, the move label, the before/after association. This is where the M1 / M2 / scope distinction actually lives (§3). Auditable only as *internal shape agreement* — that a record's parts fit each other — never as a check on which label was appropriate.

**Layer C — history and status.** `withdrawn`, the successor relation, identity assertions, episode segmentation. Not derivable from A; checkable against A only for contradiction, never for correctness. §§5–6.

**Layer D — provenance.** Why and when a restriction was chosen, post-hocness, independent motivation, the basis for a branch selection. Not derivable from A, B or C. §4.

Three observations about how v0.1 sat across these, stated as post-mortem description only:

1. **The prototype's controls sit in B while its permissions reach C.** T1/T2/T3 are defined on typed transitions; §2 permits successors introduced as states. That is §9.2's failure mode B, restated in layer terms.
2. **The distinctions v0.1 presented as A were often B.** §5.3 and §11's realization table describe M1 / M2 / scope as different operations; what differs, on the checked range, is the slot the record says changed.
3. **The one distinction v0.1 placed in C survived best.** M17 (§6.2). The prototype located it correctly and did not claim it for A.

---

## 12. What v0.1 actually established

### Established

- The finite consequence calculations are internally consistent; §§5.1–5.3's identities hold across the checked range.
- Before-state, failure witness, after-state and terminal relation can be fully enumerated and displayed for a claim in this setting.
- Typed records can distinguish different **declared** operations, and a record's parts can be checked against each other.
- **Semantic effects alone do not identify move history** — not via terminal consequence, not via the evaluated pair, not via counterexample regions.
- An identity assertion is **expressible but not adjudicable**.
- Provenance is **indispensable** for the trivial/non-trivial repair distinction, and this is a property of the semantic landscape rather than an implementation gap (§4.1).
- **Withdrawal is not reducible to semantic failure**; `failed` and `withdrawn` can share all semantic content.

### Not established

- Any objective claim identity.
- Any objective episode boundary. (Both segmentations of Example E remain consistent, and this note asserts nothing about which is right.)
- Any natural-repair criterion.
- Any semantics for M1–M17 in general — v0.1 §11 attempts four of seventeen, two of them as surrogates, and §12 lists what is absent.
- Anything about realistic theorem formation.
- Any semantic basis for the move taxonomy. The move distinctions that survived did so through record typing and status, not through the semantics.
- Any law about proof discovery.

---

## 13. Open questions for future work

Questions only. No answers, no designs, no v0.2. Each is stated as the stress test left it.

1. **What is the carrier of a claim record?** v0.1 uses three (§1.2). Which one a successor version fixes determines which of §3's distinctions it can express at all.
2. **Which parts of a formation record are semantic and which are historical?** §11 is a description of one prototype's answer, not a general one.
3. **Must every successor carry an explicit transition provenance?** §9.2's failure mode B exists because the schema permits state-typed successors; whether requiring transitions is right, or merely moves the problem, is untested.
4. **How should terminal status be checked against semantics?** The mismatches are computable (§10.1); which agreements should be required is not settled by that fact.
5. **Can claim identity be constrained without pretending it is semantic?** Both directions of laundering (§5.2) are unconstrained; any constraint would be a record discipline, and whether a useful one exists is open.
6. **Which move distinctions survive outside finite definability?** The M1/scope collapse rests on every subset being definable. Nothing here indicates what happens where that fails, which is the case of interest.
7. **How should formula-equivalent target insertion be treated?** T1 as stated is syntactic; a semantic version was not tested, and §4.1 suggests any shape test is evadable by over-restriction.
8. **Can control coverage be made symmetric across M1, M2 and scope without defining "natural repair"?** M2 and scope currently have none; whether symmetric coverage is achievable without importing a naturalness criterion is open, and this note does not attempt it.
9. **What would distinguish a record whose provenance is unstated from one whose form admits no provenance attachment?** §9.2's A/B distinction is drawn here for the first time and has no representation in v0.1.
10. **Is the display role of \(E\) worth its redundancy as data?** §7 keeps both findings; nothing decides the trade-off.

---

## 14. Final post-mortem verdict

1. **What was genuinely semantic.** Model sets, consequence (scoped and unscoped), the counterexample region as a computation, witness membership, the M1 after-model-set calculation, M2's weakening direction and its properness, the scope subset relation, inconsistency, vacuous success, agreement of `established`/`failed` with entailment, and M17's failure precondition. All auditable by truth tables alone; the last three not implemented in v0.1.

2. **What was only a typed-record distinction.** M1 versus the scope surrogate — mutually simulable on surviving valuations, counterexample region and terminal consequence. M1 versus M2 versus scope as read off \(E\) — the reachable after-region families coincide on the checked range. And the move label itself, which is redundant given a fully typed before/after record and indispensable given only the evaluated sets.

3. **What was irreducibly historical.** `withdrawn` as distinct from `failed`; the successor relation; identity continuation and identity break; episode segmentation. None is derivable from valuations; all are checkable against a record only for internal contradiction.

4. **What provenance contributed.** The only separation available between a repair that works and a repair that works because it was built from the failure. This is not a checker gap: the exact-filter repair yields \(M(H\cup B)=M(H)\cap M(C)\), the very shape §4.3 declines to infer, and a shape test would be evaded by discarding more — as v0.1's own unflagged Example A already does relative to its flagged Example D3.

5. **What \(\mathit{id}\) really did.** It made two histories two records, held a withdrawn original alongside an established successor, and gave a field on which an internal contradiction is detectable. It decided no legitimacy question, in either direction, and did not carry the rescue controls across a withdrawal. It was a recorded identity assertion, not a claim identity criterion — and that phrase is descriptive here, not proposed vocabulary.

6. **Why M17 survived.** Because it was never semantic. `failed` and `withdrawn` can share every semantic property, so `withdrawn` has no surrogate to merge with and no typing decision to depend on. v0.1 placed it in the status/identity layer and did not claim it for the semantics, and that placement is why it is the strongest surviving distinction.

7. **Why \(E\) was weaker than expected.** It is computable from the before-state, so it is not independent information; and the three consequence-seeking moves reach the same family of after-regions on the checked range, so it does not discriminate. It remains useful as a failure display and as the object against which a claimed witness is checked. Redundant as a data carrier, useful as a display — both, not one.

8. **Strongest architecture mistake in v0.1.** The carrier of a claim record was never fixed, and the evaluation factors through an object coarser than any of the three carriers used. Distinctions that lived in the gap between carrier and evaluated pair were then presented — in §5.3, in §11's realization table, in §13's RETAIN — as properties of the operations. They are properties of the record.

9. **Strongest surviving architecture insight.** That some distinctions have **no semantic surrogate at all**, and that this is stable rather than an implementation gap: `withdrawn` against `failed`, an identity assertion, and the provenance of a selection. The prototype's most durable result is a negative one located positively — it identified, in a fully explicit setting, exactly which of its own distinctions the semantics was never going to carry.

10. **What must remain open before v0.2.** All ten questions of §13, and in particular the first, the third and the ninth: the carrier question, the successor-transition question, and the distinction between provenance being unstated and the record form admitting no provenance attachment. Designing a successor before those are settled would re-inscribe the mistake in item 8 — it would fix a schema, and the schema is what the mistake was made of.

---

**End of post-mortem.** No existing file was modified. No framework, schema, move code, score, geometry, metric, lattice or topology was introduced; no result is extended beyond the finite prototype; no objective identity, boundary or naturalness criterion is asserted; and no blind-reader result has been rewritten.

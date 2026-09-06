# Finite Propositional Prototype — Adversarial Stress Test v0.1

- **Target:** [`proof_formation_finite_propositional_prototype_v0.1.md`](./proof_formation_finite_propositional_prototype_v0.1.md) and [`proof_formation_finite_propositional_checker_v0.1.py`](./proof_formation_finite_propositional_checker_v0.1.py)
- **Companion script:** [`proof_formation_finite_propositional_stress_checker_v0.1.py`](./proof_formation_finite_propositional_stress_checker_v0.1.py) (new; the v0.1 checker is imported unchanged)
- **Date:** 2026-09-05
- **Files modified:** none. Both new files are additive.

## 0. Status and posture

- This is an **adversarial stress test**. Its purpose is to break the prototype, not to defend it.
- **Not a theorem.** Every quantified statement below is an observation over an explicitly stated finite range, verified by enumeration.
- **Not a validation report.** Checks that the prototype survives are reported, but they are not the point.
- **Not a proof-formation theory**, and not an attempt to rescue the prototype.
- **Negative results are the primary output.** Where a distinction collapses under finite semantics, the collapse is recorded as the finding.
- **No assumption is added to save the prototype.** Where the prototype is unconstrained, the unconstrained version is attacked.
- **No generalization.** Nothing here transfers to realistic mathematics, to first-order or infinite settings, or to the remaining M-codes. Finite propositional semantics is a setting where almost everything is definable; that is exactly why some distinctions die here, and their death here is not evidence about their status elsewhere.
- **Prohibitions observed:** no new move code, no new taxonomy, no score, no metric, ordering, geometry, lattice or topology, no optimization, no K/A/R/D/U quantification, no definition of "natural repair", no numerical ad hocness, no claim that episode boundaries are objectively determined, and no claim that the identity token solves claim identity.

Findings tagged `[XX]` below are produced by the companion script; the tag matches its output line.

---

## 1. Audit of the current formal core

### 1.1 Internal consistency: what holds

Re-derived by enumeration rather than read off the note.

- \(E(H,C)=M(H)\setminus M(C)\), and prototype §5.1's identity \(E(H\cup B,C)=E(H,C)\cap M(B)\), §5.2's \(C\models C'\Rightarrow E(H,C')\subseteq E(H,C)\), and §5.3's \(S'\subseteq S\Rightarrow E_{S'}\subseteq E_S\) all hold — over **all** definable \(H,C,B,C',S'\) for \(n=2\), and over a fixed deterministic sample for \(n=3\) `[CORE-OK]`.
- Worked Examples A–E recompute exactly as printed, and the v0.1 checker's own assertions all pass `[EXAMPLES-OK]`.
- M2's direction constraint is genuinely enforced: an incomparable target raises rather than being silently accepted `[M2-D]`.

The formal core is internally consistent and the checker agrees with the note. Everything after this section is about what that consistency fails to buy.

### 1.2 Defects found at the definition level

These are properties of the note as written, not only of the implementation.

1. **The carrier of a claim is never fixed.** §1 defines \(X=(H,C)\); §3.3 evaluates relative to an \(S\) that is not part of \(X\); §8 introduces \(X=(\mathit{id},H,C)\) "for §§7 and 9E only". So the prototype has three different state notions and no single record carrier. Since §§6, 7 and 11 below all turn on *which slots the record keeps*, this is not cosmetic.
2. **T1 is stated syntactically.** §4.1's condition is \(C\in B\). A semantically equivalent rewrite of the target is not \(C\), so it evades the flag by definition, not merely by implementation accident `[M1-A]`.
3. **The trivial-rescue controls exist only for M1.** §4 defines T1, T2 and T3 on \(B\) and \(H\cup B\). M2 and the scope surrogate have no controls of any kind `[M2-A]` `[S1]` `[S3]`.
4. **The controls are transition-typed, but §2 permits state-typed successors.** §2's After clause allows "a withdrawal record plus an optional successor claim", with no requirement that the successor be reached by a typed move. A successor entered as a state has no \(B\), so T1/T2/T3 are not merely negative — they are inapplicable `[I4]` `[W2/W3]`.
5. **M17's precondition is unenforced.** §3.4 says "For an original claim \(X=(H,C)\) with \(H\not\models C\)", but nothing checks it, and the v0.1 checker contains no M17 function, no status field and no identity field at all `[W4]`.
6. **§13's KILL test is weaker than the question it answers.** It records KILL as untriggered because "before, failure witness, after, and terminal status can be written consistently for every worked example". Consistent *writability* is not evidence that the moves are *distinguishable*; §§6–7 below attack the latter, which §13 never tests.
7. **§5.3's closing sentence is right but load-bearing in an unadvertised way.** "The common set effect does not make the moves identical" is true — but only of the typed records, and §§6–7 show the common effect is much larger than §5.3's "all three can shrink \(E\)" suggests.

---

## 2. Claim identity stress test

### I1 — Same formulas, different identities

Two records with identical \((H,C)\) and different tokens both pass every mechanical check `[I1]`. Nothing in the prototype constrains the token as a function of \(M(H)\) or \(M(C)\), and §8 says so explicitly ("a bookkeeping token, not a semantic property").

**Is the token merely an arbitrary label?** With respect to the semantics, yes: it is chosen freely and no computation over valuations constrains it. It is not *nothing*, because two records that differ only in tokens denote different histories — but the difference is carried entirely by the recorder's assertion. The token is a place where a claim about history is written down, not a means of checking one.

### I2 — Same identity, changed content

The same token survives an arbitrary \((H,C)\to(H',C')\) `[I2]`. The only case the stress auditor catches is a *no-op* M1 (surviving set unchanged), and it catches that for an unrelated reason.

**How far can content change and still be "the same claim"?** Finite propositional logic cannot fix that boundary. Any candidate criterion — \(C'=C\), \(M(C)\subseteq M(C')\), \(H\subseteq H'\), \(M(H')\subseteq M(H)\) — is a stipulation about record discipline, not a semantic fact recoverable from truth tables. The prototype stipulates none, so the answer inside v0.1 is: arbitrarily far.

### I3 — Different identity, same after-content

The same after-content is recordable as a fresh claim or as a continuation, and both records pass `[I3]`. This confirms the prototype's own §8 statement in the sharpest form: the token **expresses** a boundary choice and **no check discriminates** between the two expressions. Nothing here decides which boundary is correct, and this note makes no such claim.

### I4 — Identity laundering

The attack that works: withdraw \(x_0=(\{p\lor q\},p)\); then introduce \(x_1\) whose assumption set is the exact counterexample filter of the withdrawn claim, **as a state rather than as a move**. Result: both records are mechanically clean, \(x_1\) is established, and no trivial-rescue flag is even applicable, because there is no \(B\) to flag `[I4]`.

The prototype anticipates the concern in prose — §7 says "the same provenance concern attaches to construction of \(x_1\)" — but supplies no mechanism that carries it. So the risk is not that the prototype *asserts* "new id ⇒ legitimate successor"; it is that the schema permits a successor to be introduced in a form to which its only controls cannot attach. **Recorded as a defect, with no repair proposed.**

### I5 — Identity collapse

One token maintained through \(C\to\top\) passes as "same claim established" `[I5]`. Unconstrained continuity lets a replacement be recorded as a repair. Combined with I4 this is a two-sided failure: unconstrained *discontinuity* launders failure history, unconstrained *continuity* launders replacement as repair. The token is unconstrained in both directions.

### What the identity token solves and does not solve

**Solves (expressibility only).**
- It makes the two histories of Example E distinct records at all — without it they are the same record.
- It lets a withdrawn original and an established successor coexist without the successor's success being attributed to the original.
- It gives the machine-checkable field pair on which an internal contradiction is detectable (a record asserting "same claim" while changing the token is caught `[REC-CAUGHT]`).

**Does not solve.**
- Whether a continuation is legitimate (I2, I5).
- Whether a successor is genuinely new rather than the same claim relabelled (I4).
- Which segmentation of a history is correct (I3).
- Anything about the *content* relation between predecessor and successor: the token is orthogonal to \(M(H)\) and \(M(C)\) by construction.
- It does not make the trivial-rescue controls travel across a withdrawal (I4).

---

## 3. M1 stress tests

### M1-A — Target insertion, and its evasion

`[M1-A]` T1 fires when the target formula object is in \(B\). Substituting \(\lnot\lnot p\) for \(p\): same model set, \(M(H\cup B)\subseteq M(C)\), entailment succeeds, and with declared independent provenance the control returns `NO FLAG`. The evasion is available at the definition level (§4.1 states membership \(C\in B\)) and in the implementation (`formula is target`). Target insertion is therefore blocked only against an opponent who inserts the target verbatim.

### M1-B — Inconsistency, and the flag's discontinuity

`[M1-B]` T2 fires exactly when \(M(H\cup B)=\varnothing\). A \(B\) leaving a single surviving valuation is unflagged. The control is a boundary condition at emptiness and says nothing about the neighbourhood of emptiness. Recorded as a qualitative discontinuity; no cardinality is used as a measure and none is implied.

### M1-C — Exact counterexample exclusion

For every failing \((H,C)\) in the checked range, take \(B=\{\varphi\}\) where \(\varphi\) is the explicit DNF over the minterms of \(\Omega\setminus E(H,C)\). Then \(E(H\cup B,C)=E(H,C)\cap M(B)=\varnothing\) and M1 succeeds `[M1-C]`.

Three properties of this construction, all verified:

1. It never triggers T1 — \(\varphi\) is not the target.
2. It triggers T2 only in the degenerate case \(M(H)\cap M(C)=\varnothing\). In the checked range, 98 instances were blocked this way and 256 succeeded with `NO FLAG`.
3. It yields exactly \(M(H\cup B)=M(H)\cap M(C)\) — which is **precisely the shape §4.3 offers as its example of a post-hoc domain filter**, and which §4.3 explicitly declines to infer from the set relation.

So the one construction that makes M1 repair generically available is the one the prototype deliberately refuses to detect automatically. **Does this show that "M1 repair existence is trivial in finite propositional semantics"?** Within this prototype and this range: repair existence is cheap wherever a claim is not self-defeating, and cheapness is a property of finite definability, not of the repair being good. No theorem is asserted, and nothing is claimed about settings where arbitrary subsets are not definable — which is most of the settings the M-codes were written for.

### M1-D — Irrelevant strengthening

\(B=\{\top\}\) is a well-formed M1 whose after-\(E\) equals the before-\(E\) `[M1-D]`. The move label does not entail that anything changed. Detecting it requires an explicit no-op comparison, which v0.1 does not perform.

### M1-E — Overrestriction, and an inversion in the note's own examples

`[M1-E]` Example A (\(B=\{\lnot q\}\), stipulated independent provenance, `NO FLAG`) leaves \(\{\omega_{10}\}\). Example D3 (\(B=\{p\lor\lnot q\}\), stipulated post-hoc, `POST-HOC DOMAIN FILTER`) leaves \(\{\omega_{10},\omega_{11}\}=M(H)\cap M(C)\).

**The unflagged example discards strictly more than the flagged one.** The flag is not tracking how much the repair throws away, and the exact-filter shape that makes D3 recognizable is evaded by discarding *more* than the counterexamples. The two examples differ only by a stipulation the truth table cannot see. This is a qualitative observation about which example receives which flag; no quantity is being compared as a measure.

---

## 4. M2 stress tests

### M2-A — Tautology collapse

\(C'=\top\) passes the v0.1 weakening check and succeeds against every \(H\) `[M2-A]`. Since §4's controls are defined on M1 additions only, **M2 has no trivial-rescue control at all**. The prototype's asymmetry is: M1 is unconstrained in what may be added but has (evadable) flags; M2 is constrained in direction but has no flags.

### M2-B — Near-tautology weakening

The smallest weakening that empties the counterexample region is \(C'\) with \(M(C')=M(H)\) — the note's own Example B `[M2-B]`. Nothing in the prototype separates Example B from \(C'=\top\): both are legal M2 with empty after-\(E\). The distinction a reader would want here ("weakened just enough" versus "weakened to nothing") is not represented.

### M2-C — No-op weakening

A logically equivalent \(C'\) passes, because the condition is \(M(C)\subseteq M(C')\) and not proper inclusion `[M2-C]`. A syntactic rewrite is recordable as an M2 move with zero semantic change. Unlike most findings here, this one **is** mechanically detectable — testing proper inclusion is a computation over the same truth tables — and the stress auditor reports it as an inconsistency `[REC-CAUGHT]`.

### M2-D — Incomparable target

`[M2-D]` \(C\not\models C'\) and \(C'\not\models C\) is rejected. This is the one direction constraint the prototype actually enforces on any move. Such a change is simply **not representable** in v0.1: it is not M2, and no code is assigned to it. Whether it resembles a target-class revision or a type correction is left unrecorded; no code is created for it here.

---

## 5. Scope-surrogate stress tests

### S1 — Exact counterexample deletion

\(S'=S\setminus E_S(H,C)\) always succeeds `[S1]`, by the same definability fact as M1-C. Since no flag of any kind is defined for scope restriction, this route to formal success is **less controlled than M1's**, not equally controlled.

### S2 — Empty scope

\(S'=\varnothing\) gives vacuous success through empty-intersection inclusion `[S2]`. The semantic effect *resembles* T2's inconsistent repair: in both, nothing survives evaluation and every target follows. The two are **not identified here**: one empties \(M(H)\), the other empties the admissible set; they live in different slots, they have different after-records, and only the first is flagged. The resemblance is recorded as a resemblance.

### S3 — Arbitrary admissibility

No computation over truth tables selects \(S\) `[S3]`. Admissible-set choice has the same provenance status as T3, and unlike T3 it has no flag to attach provenance to. Selection provenance is therefore required for scope in the same sense as for M1, and is even less provided for.

### S4 — Definability

Every subset of \(\Omega\) is the model set of an explicit DNF over minterms, verified exhaustively for \(n=2\) and \(n=3\) `[S4]`. Assumption selection and scope selection draw on the *same* supply of definable sets. This is the fact §6 rests on.

---

## 6. M1 versus scope surrogate — equivalence pressure

This is the strongest collapse found.

**Finding `[SIM-M1-SCOPE]`.** For every checked \((H,C)\): each scope restriction to \(S'\) is matched by M1 with \(B=\{\varphi_{S'}\}\), and each M1 with \(B\) is matched by the scope restriction \(S'=S\cap M(B)\), with

- identical surviving valuations,
- identical counterexample region,
- identical terminal consequence value.

The reason is visible in the prototype's own definitions: everything v0.1 evaluates — \(H\models_S C\), \(E_S(H,C)\), and every success condition in §§3–5 — is a function of the pair \(\big(M(H)\cap S,\ M(C)\big)\). M1 and the scope surrogate both act on the first component by intersecting it with a definable set, and by S4 the available sets are the same. **Relative to the prototype's own evaluation, they are one operation.**

**Does the move identity survive anyway?** Yes, but only in one place, and it is worth being exact about where `[SIM-RESIDUE]`:

| Kept in the record | M1 versus scope distinguishable? |
|---|---|
| Typed triple \((H,C,S)\) before and after | **Yes** — the changed slot names the move |
| Evaluated pair \((M(H)\cap S,\ M(C))\) before and after | **No** |
| Counterexample regions before and after | **No** |
| Terminal consequence only | **No** |

So the honest statement is the one the brief anticipates: **same mathematical effect, different typed history.** The difference is not in the semantics; it is in which slot the recorder wrote the restriction into. In v0.1 nothing constrains which \(B\) or which \(S'\) may be chosen, so there is no residual asymmetry to appeal to — with both unconstrained, the two operations have the same reach. Whether a constrained version would separate them is not tested here and no such version is proposed.

---

## 7. M1 versus M2 — equivalence pressure

**Finding `[SIM-M1-M2]`.** The after-counterexample regions reachable from a given \((H,C)\) are, for each of the three moves, **the same family: every subset of \(E(H,C)\)**.

- M1: \(E(H\cup B,C)=E(H,C)\cap M(B)\), and \(M(B)\) ranges over all definable sets.
- M2: \(E(H,C')=E(H,C)\setminus\big(M(C')\setminus M(C)\big)\), and the deleted part ranges over all subsets of \(\Omega\setminus M(C)\supseteq E(H,C)\).
- Scope: \(E_{S'}(H,C)=E(H,C)\cap S'\).

Verified by enumeration over the checked \((H,C)\) range with the move parameter ranging over every subset of \(E(H,C)\).

**This is new information relative to prototype §6.** §6 observes that the three routes can all empty the counterexample set, and its toy example exhibits one before-state where three routes converge. The stronger statement is that the *reachable families coincide exactly*: counterexample-region behaviour cannot even narrow the move down to a pair, at any before-state in the checked range, for any target after-region — not only for the empty one. So this is **not** a duplicate of §6's finding; it is the same phenomenon with the exception clause removed.

The after-*states* still differ (\(H\)-slot, \(C\)-slot, \(S\)-slot), which is again the §6 residue and not a semantic difference. Note also the direction asymmetry that does survive: M1 and scope shrink the left side, M2 grows the right side. That asymmetry is invisible in \(E\) but visible in the typed record — the same place as everything else that survives.

---

## 8. M17 stress tests

### W1 — Withdrawal without successor

Consistent, and \(E(H,C)\) is not erased `[W1]`. This is the case the prototype handles best: a terminal operation that fixes a failure and claims nothing.

### W2 — Withdrawn plus identical successor content

Mechanically clean `[W2/W3]`. It buys nothing on its own: identical content means the successor also fails, and a record claiming otherwise is caught by the status check. Laundering by relabelling alone does not produce success.

### W3 — Withdrawn plus trivially repaired successor

This is the live hole. The successor's assumption set is the exact counterexample filter of the withdrawn claim; entered as a state, the record is clean and established; entered as an M1 transition from \(x_0\), the flags would attach `[W2/W3]`. **Whether the trivial-rescue control applies depends on the recording form chosen for the successor, not on what was done.** M17 does not itself launder anything — it is the combination of a withdrawal with a state-typed successor introduction that puts the successor outside the controls' reach.

### W4 — Repaired original labelled withdrawn

Schema-permissible in v0.1, since status is never compared with semantics there. The stress auditor detects it once status and after-state entailment are compared `[W4]`. So the inconsistency is mechanically checkable; v0.1 simply does not check it, having no status field at all. **Recorded as a problem; no constraint is proposed.**

---

## 9. Transition-core consistency stress test

Twelve deliberately malformed or laundered records were run against a consistency auditor implementing only conditions already stated in prototype §§2–4.

**Detected `[REC-CAUGHT]`:**

| Corruption | What catches it |
|---|---|
| witness \(\omega\notin E(H,C)\) | membership test |
| M1 record whose \(H'\ne H\cup B\) | shape test |
| M2 record with \(C\not\models C'\) | inclusion test |
| M2 no-op (\(M(C)=M(C')\)) | proper-inclusion test |
| status `established` but \(H'\not\models C'\) | entailment test |
| status `withdrawn` with no original failure | \(E(H,C)=\varnothing\) test |
| M17 on a claim that does not fail | §3.4's own precondition |
| repaired-then-labelled-withdrawn (W4) | status against recorded move |
| "same claim" asserted while the token changes | internal field agreement |

**Not detected, and not detectable by any computation over valuations `[REC-MISSED]`:** whether \(B\) or \(S'\) was chosen after the failure was seen; whether a successor is genuinely new; whether an identity continuation is legitimate; which segmentation is correct. The laundering records W2 and W3 come back clean.

The split is therefore sharp: **every mismatch internal to a record is mechanically checkable; everything about how the record came to be written is not.**

---

## 10. What the checker can and cannot audit

### Auditable, and confirmed working in v0.1

valuation enumeration; model sets; semantic consequence; \(E(H,C)\) and \(E_S(H,C)\); the M1 transformation shape; the M2 weakening condition; the scope subset relation; inconsistency of \(H\cup B\); direct target insertion **when the target object itself is inserted**.

### Auditable but absent from v0.1, added in the stress checker

proper inclusion for M2 (no-op detection); no-op detection for M1; status against after-state entailment; M17's failure precondition; witness membership; internal identity-field agreement. These are computations over the same truth tables — their absence is a coverage gap, not a limit in principle.

### Not auditable by truth tables at all

post-hocness of \(B\) or \(S'\); claim-identity legitimacy; episode boundary; naturalness; researcher intent; whether a successor is genuinely new; whether a scope restriction is independently justified; whether one move should be preferred to another.

### Implementation-level findings about v0.1

- `trivial_rescue_flags` tests `formula is target`, so T1 is object-identity based `[M1-A]`.
- The checker has **no** identity field, **no** status field and **no** M17 function; prototype §§7, 8 and 9E are entirely outside its coverage.
- `m2` accepts equivalence; `m1` accepts tautologies; neither is a no-op check.
- `restrict_scope` does check \(S'\subseteq S\) — the scope surrogate's only enforced constraint.
- Flags are computed for M1 only.

---

## 11. Minimality audit

Each element of the prototype is removed in turn; the question is what becomes indistinguishable. No element is added.

| Removed | What becomes indistinguishable | Verdict |
|---|---|---|
| \(H\) | There is no counterexample region relative to assumptions and no M1 at all. Everything collapses. | **load-bearing** |
| \(C\) | No consequence, no failure, no transition. | **load-bearing** |
| witness \(\omega\) | *Nothing about failure detection:* \(E\ne\varnothing\) already fixes that the claim fails `[MIN-WITNESS]`. What is lost is the ability to audit a record that claims a specific witness — a misplaced witness is caught only if a witness is recorded. | **redundant for detection, non-redundant for auditing** |
| \(E(H,C)\) | *Nothing.* \(E\) is definable from \((H,C,S)\) `[MIN-E]`, and the prototype itself calls it "only a working object". It stores no information the before-state does not already fix. | **strictly redundant as data; a display device** |
| \(\mathit{id}\) | The two segmentations of Example E become the same record `[MIN-ID-PROV]`. This is the prototype's own REVISE finding and it survives the stress test. | **load-bearing, and irreplaceable by any semantic surrogate** |
| move label | *Nothing, if the typed triple \((H,C,S)\) is kept before and after* — the changed slot names the move `[MIN-MOVE-LABEL]`. *Everything, if only the evaluated sets are kept.* | **redundant given typed states; the label carries record typing, not semantics** |
| terminal status | `established` and `failed` are recomputable from the after-state. `withdrawn` is **not**: a withdrawn claim and a merely failed claim have identical semantics `[MIN-STATUS]`. | **irredundant exactly at M17** |
| provenance flag | T3 becomes unavailable and the exact-filter repair becomes indistinguishable from an independently motivated one `[MIN-ID-PROV]`. Nothing recovers it. | **load-bearing, and irreplaceable by any semantic surrogate** |
| admissible scope \(S\) | *No reachable evaluated state is lost*, since M1 covers the same family (§6). Only the typed distinction between restricting assumptions and restricting admissibility is lost `[MIN-SCOPE]`. | **semantically redundant; typing-only** |

Two elements have no semantic surrogate at all: **\(\mathit{id}\)** and the **provenance flag**. Both are exactly the elements that record something about how the claim was handled rather than what it says. Two elements are strictly redundant: **\(E\)** as data, and **\(S\)** as reachable semantics. The move label sits in between: redundant given a fully typed record, indispensable given a semantic one.

---

## 12. Strongest collapse candidates

Multiple classifications hold simultaneously. No score, ranking or weighting is attached.

### C1 — "M1/M2/scope/M17 distinctions are sufficiently preserved inside finite semantics"

**Not supported in the semantic reading; supported only in the typed-record reading.** M1 and the scope surrogate act identically on everything v0.1 evaluates (§6); M1, M2 and scope reach the same family of after-counterexample regions (§7). What preserves the distinctions is the record's slot typing, not the finite semantics. M17 is preserved for a different reason — it changes a status that has no semantic surrogate (§11) — and is the only one of the four whose distinctness does not depend on slot typing.

### C2 — "M1 and the scope surrogate mutually simulate; without a typed record they are indistinguishable"

**Confirmed, exhaustively over the checked range** `[SIM-M1-SCOPE]` `[S4]`. This is the strongest single collapse found, and it is stronger than the prototype's §6 acknowledges: not "both can shrink \(E\)" but "both act on the same component in the same way with the same reach".

### C3 — "The identity token is needed, but identity legitimacy is entirely undecidable here"

**Confirmed** `[I1]`–`[I5]`. Needed: without it Example E has one record instead of two. Undecidable: continuity, discontinuity, novelty of a successor, and boundary correctness are all unconstrained in both directions.

### C4 — "\(E\) is useful bookkeeping but too weak to identify formation history"

**Confirmed, and strengthened** `[SIM-M1-M2]` `[MIN-E]`. \(E\) is not merely weak at identifying the move; it is redundant as data (definable from the before-state) and its reachable after-values are identical across all three consequence-seeking moves. Its real function is display of a concrete witness, not identification.

### C5 — "Without provenance/history, trivial rescue and non-trivial repair cannot be separated"

**Confirmed** `[M1-C]` `[M1-E]` `[S3]` `[REC-MISSED]`. The exact-filter repair is available generically, evades T1 and T2, and is exactly the shape §4.3 declines to infer without provenance. The note's own Examples A and D3 differ only by stipulation — and the unflagged one discards more. Declining to compute T3 is defensible precisely *because* a computed shape test would be evaded by over-restriction; the cost is that the separation is irreducibly provenance-dependent.

### C6 — "Terminal status and semantic success are separate and need consistency checking"

**Confirmed** `[W4]` `[REC-CAUGHT]`. Status/semantics mismatches are mechanically detectable but unchecked in v0.1, which has no status field. The specific pairs needing agreement are listed in §9; no constraint set is proposed here.

**Additional collapse not on the list.** The trivial-rescue controls are **transition-typed while the schema permits state-typed successors**, so whether a control applies depends on the recording form rather than on what was done `[I4]` `[W2/W3]`. This is adjacent to C5 but is not the same finding: C5 is about provenance being unavailable; this is about the controls being inapplicable even when provenance would be available.

---

## 13. Relation to the blind-reader findings

Strictly limited to the five listed aspects, and stated as toy analogue only. **Nothing here explains, confirms, or reconstructs any blind-reader result.** The corpus episodes are not propositional, the readers' disagreements were about source texts, and no finite-semantics fact bears on them evidentially.

| Aspect | Formal pressure observed here | Relation |
|---|---|---|
| episode boundary sensitivity | The same formulas and witness support either one M1 record or an M17 plus an established successor, and no computation selects between them (§2 I3, prototype §7) | **toy analogue** of the earlier observation that segmentation changed move coding without changing the parent transition direction |
| move identity under different segmentation | Whether a successor is a continuation or a fresh claim changes which move is recorded and whether the rescue controls apply at all (§8 W3) | **formal pressure consistent with** the earlier finding that boundary choice, not source content, drove the coding differences |
| claim identity | The token expresses a boundary choice and constrains nothing (§2) | **toy analogue** of the earlier observation that claim identity was the most fragile concept and could not be settled by dependency or file boundary |
| code versus analysis object | Not reproduced. The prototype has no analysis-object/formation-move distinction, since it contains no object-level mathematics that a record could be *about*. The nearest thing is §11's move-label redundancy: the label is a property of the record, not of the mathematics | **no analogue available**; recorded as a limit of the prototype, not as agreement |
| provenance dependence | T3, scope selection, and the trivial/non-trivial separation are all irreducibly provenance-dependent (§12 C5) | **formal pressure consistent with** the earlier finding that post-hocness and legitimacy were never recoverable from the material itself |

The fifth row is the only place where the prototype adds anything: it shows *why* provenance dependence is irreducible in at least one fully explicit setting — because the successful and the trivially successful repairs occupy the same semantic positions. That is a statement about this prototype, not about the corpus.

---

## 14. Kill / revise decision

Multiple dispositions, as permitted.

### DOWNGRADE — triggered, strongly

Any reading on which **semantic set behaviour identifies formation history** must be dropped, further than prototype §13 already drops it. §13 downgrades "move inference from counterexample sets". The stress test extends this in two directions:

- not only counterexample sets but the entire evaluated pair \((M(H)\cap S, M(C))\) fails to distinguish M1 from scope (§6);
- not only the empty after-region but *every* reachable after-region is common to M1, M2 and scope (§7).

What remains is: **the typed record carries the move; the semantics does not.**

### REVISE — triggered, on three specific points

1. **Identity bookkeeping is unconstrained in both directions** (I2 laundering by continuity, I4 laundering by discontinuity).
2. **The trivial-rescue controls are transition-typed while successors may be state-typed**, so the controls can be sidestepped by recording form (W3).
3. **Control coverage is asymmetric:** M1 has (evadable) flags, M2 and scope have none, and status is never checked against semantics (M2-A, S1, S3, W4).

No revision is designed here. These are recorded as located deficiencies.

### RETAIN — triggered, but weaker than the prototype claims

The four operations remain distinguishable **as typed records**, and two things survive on their own merits: M2's direction constraint is genuinely enforced and rejects incomparable targets (M2-D); M17 changes a status with no semantic surrogate, so it is the one move whose distinctness does not depend on slot typing (§11). The prototype's §13 RETAIN — "M1 changes \(H\), M2 changes \(C\), the scope surrogate changes \(S\)" — is literally true and is exactly, and only, a statement about which slot the recorder wrote in.

### KILL — not triggered for the typed-record version; triggered for the semantic version

The distinctions survive with typed records, so KILL as posed ("cannot be maintained even with typed records") is not triggered. But the reading on which finite semantics itself supports the M1/scope distinction is dead, and that is recorded here as a killed reading rather than as a downgraded one.

---

## 15. Final report

1. **Strongest surviving distinction.** M17 versus everything else. Withdrawal changes a status that has no semantic surrogate — a withdrawn claim and a merely failed claim are semantically identical — so it is the only one of the four moves whose distinctness does not depend on which slot a recorder chose. Runner-up: M2's enforced direction constraint, the single semantic constraint any move in v0.1 actually imposes.

2. **Strongest collapse.** M1 and the scope surrogate. Everything v0.1 evaluates is a function of \((M(H)\cap S, M(C))\); both moves intersect the first component with an arbitrary definable set; by definability the available sets are the same. Same surviving valuations, same counterexample region, same terminal consequence. Only the slot typing separates them. Secondarily: M1, M2 and scope reach exactly the same family of after-counterexample regions, so \(E\)-behaviour cannot narrow the move down even to a pair.

3. **Did the identity token help?** Yes, in exactly one way and no more: it makes two histories two records. Without it Example E's segmentations are indistinguishable; with it they are distinct records that no check can adjudicate.

4. **What the token cannot decide.** Whether a continuation is legitimate; whether a successor is genuinely new; which segmentation is correct; anything about the content relation between predecessor and successor. It is unconstrained in both directions — continuity launders replacement as repair, discontinuity launders failure history — and it does not carry the rescue controls across a withdrawal.

5. **Can M1 always be trivially repaired in finite semantics?** In this prototype and the checked range: wherever \(M(H)\cap M(C)\ne\varnothing\), the DNF over \(\Omega\setminus E(H,C)\) is a formula whose addition makes M1 succeed, evades T1, and is flagged by T2 only in the self-defeating case. The construction yields exactly the post-hoc filter shape §4.3 declines to infer. This is a property of finite definability, recorded as an observation, not asserted as a theorem, and not extended beyond finite propositional semantics.

6. **Can scope restriction imitate M1?** Yes, and conversely, with identical surviving sets, identical counterexample regions and identical terminal consequence, for every checked \((H,C)\). Scope is additionally the less controlled route, having no flags whatsoever.

7. **Does terminal status need consistency checks?** Yes. `established` and `failed` are recomputable from the after-state, `withdrawn` is not, and a repaired-but-labelled-withdrawn record is schema-permissible in v0.1 because status is never compared with semantics there. The mismatches are mechanically checkable; v0.1 has no status field to check.

8. **What the checker can verify.** Valuation enumeration, model sets, consequence, counterexample regions, M1 shape, M2 weakening, scope subset, inconsistency, verbatim target insertion — plus, once added, no-op detection for M1 and M2, status against entailment, M17's failure precondition, witness membership, and internal identity-field agreement. All are computations over the same truth tables.

9. **What remains provenance-dependent.** Post-hocness of \(B\) or \(S'\); legitimacy of an identity continuation; novelty of a successor; correctness of a segmentation; independent justification of a scope restriction; any preference between moves. None of these is recoverable from valuations, and the exact-filter repair occupies the same semantic position as an independently motivated one — which is why declining to compute T3 is defensible and why the dependence is irreducible rather than merely unimplemented.

10. **Verdict.** **DOWNGRADE** (strongly — semantic set behaviour identifies nothing about formation history; the typed record carries all of it) **+ REVISE** (identity bookkeeping unconstrained in both directions; rescue controls sidesteppable by state-typed successors; control coverage asymmetric and status unchecked) **+ RETAIN** (weakly — the four operations remain distinguishable as typed records; M17 and M2's direction constraint survive on their own merits). **KILL is not triggered** for the typed-record version of the prototype, and **is** triggered for the reading that finite semantics itself supports the M1/scope distinction.

---

**End of stress test.** No existing file was modified. No new move code, taxonomy, score, metric, ordering, geometry, general law, or framework revision was introduced, and no finding is extended beyond finite propositional semantics.

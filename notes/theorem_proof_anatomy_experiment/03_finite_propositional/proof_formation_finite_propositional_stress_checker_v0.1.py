"""Adversarial stress checker for the finite propositional prototype v0.1.

Companion to `proof_formation_finite_propositional_stress_test_v0.1.md`.

Posture: this script tries to BREAK the prototype, not to validate it. Every
check below is an attempt to make a distinction the prototype claims collapse,
or to make an unacceptable record pass. Failures to break are reported too.

It imports `proof_formation_finite_propositional_checker_v0.1.py` unchanged and
adds nothing to the prototype's vocabulary: no new move code, no score, no
metric, no ordering, no new field beyond the five-part record of prototype
sections 2, 4 and 8 (id, H, C, S, witness, move, after, status, provenance).

Standard library only.
"""

from __future__ import annotations

import importlib.util
from itertools import chain, combinations, product
from pathlib import Path
from typing import Iterable, Optional, Sequence

BASE = Path(__file__).resolve().parent
_SPEC = importlib.util.spec_from_file_location(
    "fp_checker_v01",
    BASE / "proof_formation_finite_propositional_checker_v0.1.py",
)
assert _SPEC and _SPEC.loader
fp = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(fp)

Valuation = tuple[int, ...]
VAR_NAMES = ("p", "q", "r", "s")

FINDINGS: list[str] = []


def note(tag: str, text: str) -> None:
    FINDINGS.append(f"[{tag}] {text}")
    print(f"[{tag}] {text}")


# ---------------------------------------------------------------- utilities


def powerset(items: Iterable) -> list[frozenset]:
    pool = tuple(items)
    return [
        frozenset(combo)
        for size in range(len(pool) + 1)
        for combo in combinations(pool, size)
    ]


def subset_family(universe) -> list[frozenset]:
    """All subsets for n<=2; a fixed deterministic sample above that.

    Every finding below states which family it ranged over, so that a sampled
    range is never reported as an exhaustive one.
    """
    pool = tuple(universe)
    full = powerset(pool)
    if len(pool) <= 4:
        return full
    step = max(1, len(full) // 12)
    sample = list(full[::step])
    for extra in (
        frozenset(),
        frozenset(pool),
        frozenset(pool[:1]),
        frozenset(pool[1:]),
    ):
        if extra not in sample:
            sample.append(extra)
    return sample


def minterm_label(valuation: Valuation) -> str:
    parts = [
        (VAR_NAMES[i] if bit else f"~{VAR_NAMES[i]}")
        for i, bit in enumerate(valuation)
    ]
    return "(" + " & ".join(parts) + ")"


def formula_for_set(valuation_set: Iterable[Valuation]) -> fp.Formula:
    """The explicit DNF over minterms of the given valuation set.

    In a finite propositional universe every subset of Omega is the model set of
    such a formula. The evaluator is written as set membership; the label shows
    the DNF the membership test stands for.
    """
    frozen = frozenset(valuation_set)
    label = " | ".join(minterm_label(v) for v in sorted(frozen)) or "FALSE"
    return fp.Formula(label, lambda v, s=frozen: v in s)


def E(universe, H, C, S=None) -> frozenset:
    return fp.counterexample_region(universe, H, C, S)


def surviving(universe, H, S=None) -> frozenset:
    m = fp.models_of_assumptions(universe, H)
    return m if S is None else m & frozenset(S)


# ------------------------------------------------- 1. core identities audit


def audit_core_identities() -> None:
    print("\n=== 1. Prototype core identities, exhaustively re-derived ===")
    for n in (2, 3):
        omega = fp.valuations(n)
        subsets = subset_family(omega)
        for h_set in subsets:
            H = (formula_for_set(h_set),)
            for c_set in subsets:
                C = formula_for_set(c_set)
                base = E(omega, H, C)
                assert base == (frozenset(h_set) - frozenset(c_set))
                # section 5.1  E(H u B, C) = E(H, C) & M(B)
                for b_set in subsets:
                    B = (formula_for_set(b_set),)
                    assert E(omega, fp.m1(H, B), C) == base & frozenset(b_set)
                # section 5.2  C |= C'  implies  E(H, C') subset E(H, C)
                for c2_set in subsets:
                    if frozenset(c_set) <= frozenset(c2_set):
                        assert E(omega, H, formula_for_set(c2_set)) <= base
                # section 5.3  S' subset S implies E_{S'} subset E_S
                for s_set in subsets:
                    assert E(omega, H, C, s_set) <= base
    note(
        "CORE-OK",
        "sections 5.1-5.3 identities hold for every (H, C, B, C', S') with "
        "H, C, B, C', S' ranging over all definable sets for n=2, and over a "
        "fixed deterministic sample of definable sets for n=3.",
    )


def audit_worked_examples() -> None:
    print("\n=== 1b. Worked examples A-E versus the v0.1 checker ===")
    omega = fp.valuations(2)
    p = fp.Formula("p", lambda v: v[0] == 1)
    p_or_q = fp.Formula("p or q", lambda v: bool(v[0] or v[1]))
    not_q = fp.Formula("not q", lambda v: v[1] == 0)
    H = (p_or_q,)
    assert E(omega, H, p) == frozenset({(0, 1)})
    assert surviving(omega, fp.m1(H, (not_q,))) == frozenset({(1, 0)})
    assert fp.semantically_entails(omega, fp.m1(H, (not_q,)), p)
    assert fp.semantically_entails(omega, H, fp.m2(omega, p, p_or_q))
    assert fp.semantically_entails(omega, H, p, {(0, 0), (1, 0), (1, 1)})
    note("EXAMPLES-OK", "Examples A, B, C, D and E recompute as printed in the note.")


# ------------------------------------------------ 2/8. identity and records
# Record fields are exactly those of prototype sections 2, 4 and 8.


def audit_record(rec: dict, omega) -> list[str]:
    """Machine-checkable consistency conditions already stated in the prototype.

    Returns the list of detected inconsistencies. An empty list means only that
    nothing mechanically checkable is wrong; it is not an endorsement.
    """
    problems: list[str] = []
    H, C = rec["H"], rec["C"]
    S = rec.get("S")
    before_E = E(omega, H, C, S)

    w = rec.get("witness")
    if w is not None and w not in before_E:
        problems.append("witness is not in the before counterexample region")

    move = rec.get("move")
    aH, aC = rec.get("after_H", H), rec.get("after_C", C)
    aS = rec.get("after_S", S)

    if move == "M1":
        expected = fp.m1(H, rec.get("additions", ()))
        if tuple(aH) != tuple(expected):
            problems.append("M1 record but after-H is not H union B")
        if aC is not C:
            problems.append("M1 record but the target was also changed")
        if surviving(omega, aH, aS) == surviving(omega, H, S):
            problems.append("M1 record with no change to the surviving set")
    elif move == "M2":
        if not fp.models(omega, C) <= fp.models(omega, aC):
            problems.append("M2 record but C does not entail C'")
        if tuple(aH) != tuple(H):
            problems.append("M2 record but the assumptions were also changed")
        if fp.models(omega, C) == fp.models(omega, aC):
            problems.append("M2 record with a semantically equivalent target")
    elif move == "SCOPE":
        if not frozenset(aS) <= frozenset(S if S is not None else omega):
            problems.append("scope record but S' is not a subset of S")
        if tuple(aH) != tuple(H) or aC is not C:
            problems.append("scope record but H or C also changed")
    elif move == "M17":
        if not before_E:
            problems.append("M17 record but the original claim does not fail")
        if rec.get("after_H") is not None or rec.get("after_C") is not None:
            problems.append("M17 record that also alters H or C")

    status = rec.get("status")
    entails_after = fp.semantically_entails(omega, aH, aC, aS)
    if status == "established" and not entails_after:
        problems.append("status established but the after-state does not entail")
    if status == "withdrawn":
        if not before_E:
            problems.append("status withdrawn but there is no original failure")
        if move not in (None, "M17"):
            problems.append("status withdrawn but a consequence-producing move is recorded")
    if status == "failed" and entails_after:
        problems.append("status failed but the after-state entails")

    if "same_claim" in rec and "after_id" in rec:
        if rec["same_claim"] and rec["after_id"] != rec["id"]:
            problems.append("record asserts same claim but changes the identity token")
        if not rec["same_claim"] and rec["after_id"] == rec["id"]:
            problems.append("record asserts a new claim but reuses the identity token")
    return problems


def audit_identity() -> None:
    print("\n=== 2. Claim identity stress (I1-I5) ===")
    omega = fp.valuations(2)
    p = fp.Formula("p", lambda v: v[0] == 1)
    p_or_q = fp.Formula("p or q", lambda v: bool(v[0] or v[1]))
    not_q = fp.Formula("not q", lambda v: v[1] == 0)
    top = fp.Formula("TRUE", lambda v: True)
    H = (p_or_q,)

    # I1 same formulas, different identity tokens: both records pass.
    r1 = dict(id="x0", H=H, C=p, witness=(0, 1), status="failed")
    r2 = dict(id="x9", H=H, C=p, witness=(0, 1), status="failed")
    assert audit_record(r1, omega) == [] and audit_record(r2, omega) == []
    note(
        "I1",
        "identical (H, C) carrying different identity tokens both pass every "
        "mechanical check: the token is not a function of M(H) or M(C).",
    )

    # I2 same identity, arbitrarily changed content.
    r3 = dict(
        id="x0", H=H, C=p, witness=(0, 1), move="M1", additions=(not_q,),
        after_id="x0", after_H=fp.m1(H, (not_q,)), same_claim=True,
        status="established",
    )
    assert audit_record(r3, omega) == []
    r4 = dict(
        id="x0", H=H, C=p, witness=(0, 1), move="M1", additions=(top,),
        after_id="x0", after_H=fp.m1(H, (top,)), same_claim=True, status="failed",
    )
    problems = audit_record(r4, omega)
    assert "M1 record with no change to the surviving set" in problems
    note(
        "I2",
        "identity continuity is unconstrained: the same token survives any "
        "H-change. Only a no-op M1 is caught, and only because the surviving "
        "set is unchanged, not because the claim changed too much.",
    )

    # I3 different identity, same after-content.
    r5 = dict(id="x1", H=fp.m1(H, (not_q,)), C=p, status="established")
    assert audit_record(r5, omega) == []
    note(
        "I3",
        "the same after-content is recordable as a fresh claim x1 or as the "
        "continuation of x0; both pass. The token records the boundary choice "
        "and no check discriminates between the two records.",
    )

    # I4 identity laundering: withdraw, then reintroduce as a fresh claim.
    withdrawal = dict(id="x0", H=H, C=p, witness=(0, 1), move="M17", status="withdrawn")
    filt = formula_for_set(surviving(omega, H) & fp.models(omega, p))
    laundered = dict(id="x1", H=fp.m1(H, (filt,)), C=p, status="established")
    assert audit_record(withdrawal, omega) == []
    assert audit_record(laundered, omega) == []
    assert fp.semantically_entails(omega, laundered["H"], p)
    note(
        "I4",
        "withdrawal of x0 followed by a fresh x1 whose assumption set is the "
        "exact counterexample filter passes every check. Because x1 is entered "
        "as a state and not as an M1 transition, no B exists, so T1/T2/T3 are "
        "not even applicable: the trivial-rescue controls are transition-typed "
        "and a fresh-claim introduction has no transition to attach them to.",
    )

    # I5 identity collapse: keep one token across an unrelated replacement.
    collapse = dict(
        id="x0", H=H, C=p, witness=(0, 1), move="M2", after_id="x0",
        after_C=top, same_claim=True, status="established",
    )
    assert audit_record(collapse, omega) == []
    note(
        "I5",
        "one token maintained through C -> TRUE passes as 'same claim "
        "established'. Unconstrained continuity lets replacement be recorded "
        "as repair.",
    )


# ------------------------------------------------------------ 3. M1 stress


def audit_m1() -> None:
    print("\n=== 3. M1 stress (A-E) ===")
    omega = fp.valuations(2)
    p = fp.Formula("p", lambda v: v[0] == 1)
    p_or_q = fp.Formula("p or q", lambda v: bool(v[0] or v[1]))
    not_q = fp.Formula("not q", lambda v: v[1] == 0)
    H = (p_or_q,)

    # M1-A target insertion and its evasion.
    assert fp.trivial_rescue_flags(omega, H, (p,), p) == ("DIRECT TARGET INSERTION",)
    not_not_p = fp.Formula("~~p", lambda v: not (not v[0] == 1))
    assert fp.models(omega, not_not_p) == fp.models(omega, p)
    flags = fp.trivial_rescue_flags(
        omega, H, (not_not_p,), p, selection_provenance="independent"
    )
    assert flags == ("NO FLAG",) and fp.semantically_entails(omega, fp.m1(H, (not_not_p,)), p)
    note(
        "M1-A",
        "T1 fires on object identity ('formula is target'), so a semantically "
        "equivalent rewrite of the target (~~p) inserts the target, succeeds, "
        "and is returned as NO FLAG. Direct target insertion is evadable by "
        "rewriting, at the definition level as well as in the implementation: "
        "prototype 4.1 states T1 as the membership condition C in B.",
    )

    # M1-B inconsistency, and the flag's discontinuity at emptiness.
    contradiction = fp.Formula("~(p | q)", lambda v: not (v[0] or v[1]))
    assert fp.trivial_rescue_flags(omega, H, (contradiction,), p) == ("INCONSISTENT REPAIR",)
    near = fp.Formula("p & ~q", lambda v: v[0] == 1 and v[1] == 0)
    assert surviving(omega, fp.m1(H, (near,))) == frozenset({(1, 0)})
    assert fp.trivial_rescue_flags(omega, H, (near,), p, selection_provenance="independent") == ("NO FLAG",)
    note(
        "M1-B",
        "T2 is a boundary condition at exactly the empty model set. A B leaving "
        "a single surviving valuation is unflagged; the flag does not vary with "
        "how little survives, it only distinguishes 'nothing survives'.",
    )

    # M1-C exact counterexample exclusion, exhaustively.
    trivialisable = 0
    blocked = 0
    for n in (2, 3):
        om = fp.valuations(n)
        subsets = subset_family(om)
        for h_set in subsets:
            Hn = (formula_for_set(h_set),)
            for c_set in subsets:
                Cn = formula_for_set(c_set)
                base = E(om, Hn, Cn)
                if not base:
                    continue
                B = (formula_for_set(frozenset(om) - base),)
                strengthened = fp.m1(Hn, B)
                assert fp.semantically_entails(om, strengthened, Cn)
                assert surviving(om, strengthened) == frozenset(h_set) & frozenset(c_set)
                fl = fp.trivial_rescue_flags(om, Hn, B, Cn, selection_provenance="independent")
                if fl == ("NO FLAG",):
                    trivialisable += 1
                else:
                    assert fl == ("INCONSISTENT REPAIR",)
                    assert not (frozenset(h_set) & frozenset(c_set))
                    blocked += 1
    note(
        "M1-C",
        "for every failing (H, C) in the checked range (all definable sets for "
        "n=2, a fixed sample for n=3), the DNF over Omega minus "
        "E(H, C) is a formula B making M1 succeed. It never triggers T1, and it "
        f"triggers T2 only in the degenerate case M(H) & M(C) = empty ({blocked} "
        f"such cases; {trivialisable} cases succeed unflagged). The construction "
        "yields exactly M(H u B) = M(H) & M(C), which is the shape prototype 4.3 "
        "gives as its example of a post-hoc filter and explicitly declines to "
        "infer. Observation about this prototype's discriminating power, not a "
        "theorem, and not generalised beyond finite propositional semantics.",
    )

    # M1-D irrelevant strengthening.
    top = fp.Formula("TRUE", lambda v: True)
    assert E(omega, fp.m1(H, (top,)), p) == E(omega, H, p)
    note(
        "M1-D",
        "B = TRUE is a well-formed M1 whose after-E equals the before-E. The "
        "move label does not entail that anything changed; only an explicit "
        "no-op comparison detects it.",
    )

    # M1-E overrestriction versus the note's own Example A / Example D3 pair.
    exampleA = surviving(omega, fp.m1(H, (not_q,)))
    p_or_not_q = fp.Formula("p | ~q", lambda v: bool(v[0] or not v[1]))
    exampleD3 = surviving(omega, fp.m1(H, (p_or_not_q,)))
    assert exampleA < exampleD3 == (surviving(omega, H) & fp.models(omega, p))
    note(
        "M1-E",
        "Example A (NO FLAG, stipulated provenance) removes strictly more "
        "valuations than Example D3 (POST-HOC DOMAIN FILTER): {(1,0)} against "
        "{(1,0),(1,1)}. The flag is not tracking how much the repair discards, "
        "and the exact-filter shape that D3 exhibits is evaded by over-"
        "restricting. The two examples differ only by stipulated provenance.",
    )


# ------------------------------------------------------------ 4. M2 stress


def audit_m2() -> None:
    print("\n=== 4. M2 stress (A-D) ===")
    omega = fp.valuations(2)
    p = fp.Formula("p", lambda v: v[0] == 1)
    p_or_q = fp.Formula("p or q", lambda v: bool(v[0] or v[1]))
    top = fp.Formula("TRUE", lambda v: True)
    H = (p_or_q,)

    c_top = fp.m2(omega, p, top)
    assert fp.semantically_entails(omega, H, c_top) and E(omega, H, c_top) == frozenset()
    note(
        "M2-A",
        "C' = TRUE is accepted by the v0.1 m2 weakening check and succeeds for "
        "every H. Prototype section 4 defines T1, T2 and T3 on M1 additions "
        "only, so there is no trivial-rescue control of any kind on M2.",
    )

    near_top = formula_for_set(surviving(omega, H))
    assert fp.semantically_entails(omega, H, fp.m2(omega, p, near_top))
    note(
        "M2-B",
        "the smallest weakening that empties the counterexample region is "
        "C' with M(C') = M(H), which is Example B in the note. Nothing in the "
        "prototype separates it from C' = TRUE: both are legal M2 with empty "
        "after-E.",
    )

    p_again = fp.Formula("p (rewritten)", lambda v: v[0] == 1)
    c_noop = fp.m2(omega, p, p_again)
    assert fp.models(omega, c_noop) == fp.models(omega, p)
    assert E(omega, H, c_noop) == E(omega, H, p)
    note(
        "M2-C",
        "a logically equivalent C' passes m2, because the check is M(C) subset "
        "M(C') and not proper inclusion. A syntactic rewrite is recordable as "
        "an M2 move with no semantic change. This one IS mechanically "
        "detectable (test proper inclusion) and the stress auditor reports it.",
    )

    q = fp.Formula("q", lambda v: v[1] == 1)
    try:
        fp.m2(omega, p, q)
    except ValueError:
        note(
            "M2-D",
            "an incomparable target is rejected by m2. This is the one "
            "direction constraint the prototype actually enforces on a move. "
            "Such a change is simply not representable here; no code is "
            "assigned to it.",
        )
    else:  # pragma: no cover
        raise AssertionError("incomparable target was accepted")


# --------------------------------------------------------- 5. scope stress


def audit_scope() -> None:
    print("\n=== 5. Scope-surrogate stress (S1-S4) ===")
    omega = fp.valuations(2)
    p = fp.Formula("p", lambda v: v[0] == 1)
    p_or_q = fp.Formula("p or q", lambda v: bool(v[0] or v[1]))
    H = (p_or_q,)

    S_prime = frozenset(omega) - E(omega, H, p)
    assert fp.semantically_entails(omega, H, p, S_prime)
    note(
        "S1",
        "S' = S minus E_S(H, C) always succeeds, by the same definability fact "
        "as M1-C. Scope restriction carries no flag at all, so this is even "
        "less controlled than the M1 route.",
    )

    assert fp.semantically_entails(omega, H, p, frozenset())
    note(
        "S2",
        "S' = empty gives vacuous success through the empty-intersection "
        "inclusion. The semantic effect resembles T2 inconsistent repair "
        "(both succeed because nothing survives evaluation); recorded as a "
        "resemblance only. The prototype does not identify them and neither "
        "does this check: one empties M(H), the other empties the admissible "
        "set, and only the first is flagged.",
    )

    note(
        "S3",
        "no computation over truth tables selects S. Admissible-set choice has "
        "the same provenance status as T3 and the prototype supplies no "
        "counterpart of T1/T2/T3 for it.",
    )

    for n in (2, 3):
        om = fp.valuations(n)
        for s_set in powerset(om):
            phi = formula_for_set(s_set)
            assert fp.models(om, phi) == frozenset(s_set)
    note(
        "S4",
        "every subset of Omega is the model set of an explicit DNF over "
        "minterms, verified for n=2 and n=3. Scope selection and assumption "
        "selection therefore draw on the same supply of definable sets.",
    )


# ------------------------------- 6/7. mutual simulation and reachable families


def audit_simulation() -> None:
    print("\n=== 6/7. M1 versus scope, and M1 versus M2 ===")
    for n in (2, 3):
        om = fp.valuations(n)
        subsets = subset_family(om)
        for h_set in subsets:
            H = (formula_for_set(h_set),)
            for c_set in subsets:
                C = formula_for_set(c_set)
                base = E(om, H, C)

                # 6. every scope step is matched by an M1 step and conversely.
                for s_set in subsets:
                    B = (formula_for_set(s_set),)
                    assert surviving(om, fp.m1(H, B)) == surviving(om, H, s_set)
                    assert E(om, fp.m1(H, B), C) == E(om, H, C, s_set)
                    assert fp.semantically_entails(om, fp.m1(H, B), C) == (
                        fp.semantically_entails(om, H, C, s_set)
                    )

                # 7. reachable after-E families.
                # containment in the powerset of the before-region, over the
                # sampled family of moves:
                for x in subsets:
                    assert E(om, fp.m1(H, (formula_for_set(x),)), C) <= base
                    assert E(om, H, C, x) <= base
                    if frozenset(c_set) <= frozenset(x):
                        assert E(om, H, formula_for_set(x)) <= base
                # and every subset of the before-region is actually reached by
                # each of the three moves:
                target_family = set(powerset(base))
                by_m1 = {
                    E(om, fp.m1(H, (formula_for_set(b),)), C) for b in powerset(base)
                }
                by_scope = {E(om, H, C, s) for s in powerset(base)}
                by_m2 = {
                    E(om, H, formula_for_set(frozenset(c_set) | (base - keep)))
                    for keep in powerset(base)
                }
                assert by_m1 == by_scope == by_m2 == target_family
    note(
        "SIM-M1-SCOPE",
        "for every checked (H, C) (all definable sets for n=2, a fixed sample "
        "for n=3): each admissible-set restriction to "
        "S' is matched by M1 with B = phi_{S'} and conversely, with identical "
        "surviving set, identical counterexample region and identical terminal "
        "consequence. The prototype's evaluation depends on (H, C, S) only "
        "through the pair (M(H) & S, M(C)), and M1 and the scope surrogate act "
        "on the first component in exactly the same way.",
    )
    note(
        "SIM-M1-M2",
        "the after-counterexample regions reachable by M1, by M2 and by scope "
        "restriction are the same family, namely every subset of the before-"
        "region E(H, C). This goes beyond the note's section 6 observation that "
        "all three can shrink E: the reachable families coincide exactly, so a "
        "record of E-behaviour alone cannot even narrow the move down to a "
        "pair. Verified by enumeration for n=2 and n=3; recorded as an "
        "observation about these finite instances, not as a theorem, and not "
        "extended beyond finite propositional semantics.",
    )
    note(
        "SIM-RESIDUE",
        "what still separates the three is the typed after-state: M1 changes "
        "the H slot, M2 the C slot, scope the S slot. Given the typed triple "
        "the move is readable off the record; given only the evaluated sets it "
        "is not.",
    )


# ------------------------------------------------------------ 8/9. M17 and
# record consistency


def audit_m17_and_records() -> None:
    print("\n=== 8/9. M17 stress and transition-core consistency ===")
    omega = fp.valuations(2)
    p = fp.Formula("p", lambda v: v[0] == 1)
    p_or_q = fp.Formula("p or q", lambda v: bool(v[0] or v[1]))
    not_q = fp.Formula("not q", lambda v: v[1] == 0)
    q = fp.Formula("q", lambda v: v[1] == 1)
    H = (p_or_q,)

    caught: list[str] = []
    missed: list[str] = []

    def trial(name: str, rec: dict, expect_detection: bool) -> None:
        problems = audit_record(rec, omega)
        (caught if problems else missed).append(f"{name}: {problems or 'clean'}")
        assert bool(problems) == expect_detection, (name, problems)

    trial("W1 withdrawal, no successor",
          dict(id="x0", H=H, C=p, witness=(0, 1), move="M17", status="withdrawn"), False)
    trial("W2 withdrawn + identical-content successor",
          dict(id="x1", H=H, C=p, status="failed"), False)
    trial("W3 withdrawn + trivially repaired successor",
          dict(id="x1", H=fp.m1(H, (formula_for_set(surviving(omega, H) & fp.models(omega, p)),)),
               C=p, status="established"), False)
    trial("W4 semantically repaired but labelled withdrawn",
          dict(id="x0", H=H, C=p, witness=(0, 1), move="M1", additions=(not_q,),
               after_H=fp.m1(H, (not_q,)), after_id="x0", status="withdrawn"), True)
    trial("M17 on a claim that does not fail",
          dict(id="x0", H=fp.m1(H, (not_q,)), C=p, move="M17", status="withdrawn"), True)
    trial("witness outside E(H, C)",
          dict(id="x0", H=H, C=p, witness=(1, 1), status="failed"), True)
    trial("M1 record whose after-H is not H union B",
          dict(id="x0", H=H, C=p, witness=(0, 1), move="M1", additions=(not_q,),
               after_H=(p_or_q, q), after_id="x0", status="established"), True)
    trial("M2 record without weakening",
          dict(id="x0", H=H, C=p, witness=(0, 1), move="M2", after_C=q,
               after_id="x0", status="failed"), True)
    trial("established but no entailment",
          dict(id="x0", H=H, C=p, witness=(0, 1), status="established"), True)
    trial("withdrawn without any original failure",
          dict(id="x0", H=fp.m1(H, (not_q,)), C=p, status="withdrawn"), True)
    trial("same_claim asserted while the token changes",
          dict(id="x0", H=H, C=p, witness=(0, 1), move="M1", additions=(not_q,),
               after_H=fp.m1(H, (not_q,)), after_id="x7", same_claim=True,
               status="established"), True)
    trial("no-op M2 recorded as a move",
          dict(id="x0", H=H, C=p, witness=(0, 1), move="M2",
               after_C=fp.Formula("p again", lambda v: v[0] == 1),
               after_id="x0", status="failed"), True)

    note("W1", "withdrawal with no successor is consistent and leaves E(H, C) intact.")
    note(
        "W2/W3",
        "both laundering records are mechanically clean. W3 succeeds because "
        "the successor is entered as a state: no B, hence no T1/T2/T3, hence "
        "no trace that the successor's assumption set is the exact "
        "counterexample filter of the withdrawn claim.",
    )
    note(
        "W4",
        "a status/semantics mismatch IS detectable once status is compared "
        "with the after-state entailment. The v0.1 checker never does this: it "
        "has no status field, no identity field and no M17 function at all.",
    )
    note(
        "REC-CAUGHT",
        "detected by the stress auditor: status/semantics mismatch, M17 without "
        "failure, witness outside E, malformed M1 after-state, M2 without "
        "weakening, M2 no-op, withdrawn without failure, same_claim with a "
        "changed token.",
    )
    note(
        "REC-MISSED",
        "not detectable by any computation over truth tables: whether B or S' "
        "was chosen after the failure was seen, whether a successor is "
        "genuinely new, whether an identity continuation is legitimate, and "
        "which segmentation of a history is correct.",
    )
    print("\n  caught:")
    for line in caught:
        print(f"    - {line}")
    print("  clean (not detectable here):")
    for line in missed:
        print(f"    - {line}")


# ------------------------------------------------------- 11. minimality audit


def audit_minimality() -> None:
    print("\n=== 11. Minimality: what each element is doing ===")
    omega = fp.valuations(2)
    p = fp.Formula("p", lambda v: v[0] == 1)
    p_or_q = fp.Formula("p or q", lambda v: bool(v[0] or v[1]))
    not_q = fp.Formula("not q", lambda v: v[1] == 0)
    H = (p_or_q,)

    assert E(omega, H, p) == surviving(omega, H) - fp.models(omega, p)
    note("MIN-E", "E is definable from (H, C, S); it stores nothing that the "
                  "before-state does not already fix.")

    m1_after = (fp.m1(H, (not_q,)), p, None)
    m2_after = (H, fp.m2(omega, p, p_or_q), None)
    sc_after = (H, p, frozenset(omega) - E(omega, H, p))
    assert len({m1_after[0], m2_after[0], sc_after[0]}) == 2
    assert (m1_after[1] is p) and (m2_after[1] is not p) and (sc_after[1] is p)
    note(
        "MIN-MOVE-LABEL",
        "given the typed triple (H, C, S) before and after, the changed slot "
        "identifies which of M1 / M2 / scope occurred, so the move label adds "
        "nothing on top of the typed record. Given only the evaluated sets it "
        "adds everything. The label is carrying record typing, not semantics.",
    )
    note(
        "MIN-STATUS",
        "established and failed are recomputable from the after-state; "
        "withdrawn is not, because a withdrawn claim and a merely failed claim "
        "have the same semantics. Status is irredundant exactly at M17.",
    )
    note(
        "MIN-WITNESS",
        "a displayed omega is not needed to detect failure (E non-empty "
        "suffices). It is needed to audit a record that claims a particular "
        "witness.",
    )
    note(
        "MIN-SCOPE",
        "dropping S loses no reachable evaluated state, since M1 covers the "
        "same family (SIM-M1-SCOPE). It loses only the typed distinction "
        "between restricting assumptions and restricting the admissible set.",
    )
    note(
        "MIN-ID-PROV",
        "id and the provenance flag are the two elements with no semantic "
        "surrogate: without id the two segmentations of Example E are the same "
        "record; without provenance T3 is unavailable and the exact-filter "
        "repair is indistinguishable from an independently motivated one.",
    )


def main() -> None:
    audit_core_identities()
    audit_worked_examples()
    audit_identity()
    audit_m1()
    audit_m2()
    audit_scope()
    audit_simulation()
    audit_m17_and_records()
    audit_minimality()
    print(f"\n=== {len(FINDINGS)} findings recorded. "
          "No score, ordering, metric or new move code was produced. ===")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Finite checker for the proof-term pairs in the quotient pilot.

Scope: simply typed lambda calculus with binary products.  Terms are built as
ASTs below; this is not a parser, enumerator, prover, or general theorem about
proof identity.  The checker verifies types and compares the selected terms
under four cumulative, explicitly configured equality levels.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Union


@dataclass(frozen=True)
class Atom:
    name: str


@dataclass(frozen=True)
class Arrow:
    source: "Type"
    target: "Type"


@dataclass(frozen=True)
class Product:
    left: "Type"
    right: "Type"


Type = Union[Atom, Arrow, Product]


@dataclass(frozen=True)
class Var:
    name: str


@dataclass(frozen=True)
class Lam:
    variable: str
    variable_type: Type
    body: "Term"


@dataclass(frozen=True)
class App:
    function: "Term"
    argument: "Term"


@dataclass(frozen=True)
class Pair:
    left: "Term"
    right: "Term"


@dataclass(frozen=True)
class Fst:
    pair: "Term"


@dataclass(frozen=True)
class Snd:
    pair: "Term"


Term = Union[Var, Lam, App, Pair, Fst, Snd]
Context = Mapping[str, Type]


def type_of(term: Term, context: Context) -> Type:
    if isinstance(term, Var):
        if term.name not in context:
            raise TypeError(f"unbound variable: {term.name}")
        return context[term.name]
    if isinstance(term, Lam):
        extended = dict(context)
        extended[term.variable] = term.variable_type
        return Arrow(term.variable_type, type_of(term.body, extended))
    if isinstance(term, App):
        function_type = type_of(term.function, context)
        argument_type = type_of(term.argument, context)
        if not isinstance(function_type, Arrow):
            raise TypeError(f"application of non-function: {function_type}")
        if argument_type != function_type.source:
            raise TypeError(
                f"argument mismatch: expected {function_type.source}, got {argument_type}"
            )
        return function_type.target
    if isinstance(term, Pair):
        return Product(type_of(term.left, context), type_of(term.right, context))
    if isinstance(term, Fst):
        pair_type = type_of(term.pair, context)
        if not isinstance(pair_type, Product):
            raise TypeError(f"fst of non-product: {pair_type}")
        return pair_type.left
    if isinstance(term, Snd):
        pair_type = type_of(term.pair, context)
        if not isinstance(pair_type, Product):
            raise TypeError(f"snd of non-product: {pair_type}")
        return pair_type.right
    raise AssertionError(term)


def free_variables(term: Term) -> set[str]:
    if isinstance(term, Var):
        return {term.name}
    if isinstance(term, Lam):
        return free_variables(term.body) - {term.variable}
    if isinstance(term, App):
        return free_variables(term.function) | free_variables(term.argument)
    if isinstance(term, Pair):
        return free_variables(term.left) | free_variables(term.right)
    if isinstance(term, (Fst, Snd)):
        return free_variables(term.pair)
    raise AssertionError(term)


def all_variables(term: Term) -> set[str]:
    if isinstance(term, Var):
        return {term.name}
    if isinstance(term, Lam):
        return {term.variable} | all_variables(term.body)
    if isinstance(term, App):
        return all_variables(term.function) | all_variables(term.argument)
    if isinstance(term, Pair):
        return all_variables(term.left) | all_variables(term.right)
    if isinstance(term, (Fst, Snd)):
        return all_variables(term.pair)
    raise AssertionError(term)


def fresh_name(avoid: set[str], stem: str = "v") -> str:
    index = 0
    while f"{stem}{index}" in avoid:
        index += 1
    return f"{stem}{index}"


def substitute(term: Term, variable: str, replacement: Term) -> Term:
    """Capture-avoiding substitution [replacement/variable]term."""
    if isinstance(term, Var):
        return replacement if term.name == variable else term
    if isinstance(term, Lam):
        if term.variable == variable:
            return term
        if term.variable in free_variables(replacement):
            avoid = all_variables(term.body) | all_variables(replacement) | {variable}
            renamed = fresh_name(avoid, term.variable)
            renamed_body = substitute(term.body, term.variable, Var(renamed))
            return Lam(
                renamed,
                term.variable_type,
                substitute(renamed_body, variable, replacement),
            )
        return Lam(
            term.variable,
            term.variable_type,
            substitute(term.body, variable, replacement),
        )
    if isinstance(term, App):
        return App(
            substitute(term.function, variable, replacement),
            substitute(term.argument, variable, replacement),
        )
    if isinstance(term, Pair):
        return Pair(
            substitute(term.left, variable, replacement),
            substitute(term.right, variable, replacement),
        )
    if isinstance(term, Fst):
        return Fst(substitute(term.pair, variable, replacement))
    if isinstance(term, Snd):
        return Snd(substitute(term.pair, variable, replacement))
    raise AssertionError(term)


def alpha_key(term: Term, binders: tuple[str, ...] = ()) -> tuple:
    """A de Bruijn-style key: equal exactly when terms are alpha-equivalent."""
    if isinstance(term, Var):
        for distance, binder in enumerate(reversed(binders)):
            if term.name == binder:
                return ("bound", distance)
        return ("free", term.name)
    if isinstance(term, Lam):
        return (
            "lam",
            term.variable_type,
            alpha_key(term.body, binders + (term.variable,)),
        )
    if isinstance(term, App):
        return ("app", alpha_key(term.function, binders), alpha_key(term.argument, binders))
    if isinstance(term, Pair):
        return ("pair", alpha_key(term.left, binders), alpha_key(term.right, binders))
    if isinstance(term, Fst):
        return ("fst", alpha_key(term.pair, binders))
    if isinstance(term, Snd):
        return ("snd", alpha_key(term.pair, binders))
    raise AssertionError(term)


@dataclass(frozen=True)
class Equations:
    arrow_beta: bool = False
    arrow_eta: bool = False
    product_beta: bool = False
    product_eta: bool = False


Q1_ALPHA = Equations()
Q2_ALPHA_BETA = Equations(arrow_beta=True)
Q3_ALPHA_BETA_ETA = Equations(arrow_beta=True, arrow_eta=True)
Q4_FULL_PRODUCTS = Equations(
    arrow_beta=True, arrow_eta=True, product_beta=True, product_eta=True
)


def normalize(term: Term, equations: Equations) -> Term:
    """Normalize the selected finite terms under oriented standard equations."""
    if isinstance(term, Var):
        return term
    if isinstance(term, Lam):
        body = normalize(term.body, equations)
        if (
            equations.arrow_eta
            and isinstance(body, App)
            and isinstance(body.argument, Var)
            and body.argument.name == term.variable
            and term.variable not in free_variables(body.function)
        ):
            return normalize(body.function, equations)
        return Lam(term.variable, term.variable_type, body)
    if isinstance(term, App):
        function = normalize(term.function, equations)
        argument = normalize(term.argument, equations)
        if equations.arrow_beta and isinstance(function, Lam):
            return normalize(
                substitute(function.body, function.variable, argument), equations
            )
        return App(function, argument)
    if isinstance(term, Pair):
        left = normalize(term.left, equations)
        right = normalize(term.right, equations)
        if (
            equations.product_eta
            and isinstance(left, Fst)
            and isinstance(right, Snd)
            and alpha_key(left.pair) == alpha_key(right.pair)
        ):
            return normalize(left.pair, equations)
        return Pair(left, right)
    if isinstance(term, Fst):
        pair = normalize(term.pair, equations)
        if equations.product_beta and isinstance(pair, Pair):
            return normalize(pair.left, equations)
        return Fst(pair)
    if isinstance(term, Snd):
        pair = normalize(term.pair, equations)
        if equations.product_beta and isinstance(pair, Pair):
            return normalize(pair.right, equations)
        return Snd(pair)
    raise AssertionError(term)


def equivalent(left: Term, right: Term, equations: Equations) -> bool:
    return alpha_key(normalize(left, equations)) == alpha_key(normalize(right, equations))


A = Atom("A")
B = Atom("B")

I_X = Lam("x", A, Var("x"))
I_Y = Lam("y", A, Var("y"))
I_BETA = Lam("x", A, App(Lam("z", A, Var("z")), Var("x")))
I_PRODUCT_BETA = Lam("x", A, Fst(Pair(Var("x"), Var("x"))))

SWAP = Lam("p", Product(A, B), Pair(Snd(Var("p")), Fst(Var("p"))))
SWAP_ALPHA = Lam("q", Product(A, B), Pair(Snd(Var("q")), Fst(Var("q"))))
SWAP_BETA = Lam(
    "p",
    Product(A, B),
    App(
        Lam("q", Product(A, B), Pair(Snd(Var("q")), Fst(Var("q")))),
        Var("p"),
    ),
)

CHOOSE_FIRST = Lam("p", Product(A, A), Fst(Var("p")))
CHOOSE_SECOND = Lam("p", Product(A, A), Snd(Var("p")))
CHOOSE_FIRST_PRODUCT_BETA = Lam(
    "p",
    Product(A, A),
    Fst(Pair(Fst(Var("p")), Snd(Var("p")))),
)

FREE_FUNCTION = Var("f")
FREE_FUNCTION_ETA = Lam("x", A, App(Var("f"), Var("x")))
FREE_PRODUCT = Var("p")
FREE_PRODUCT_ETA = Pair(Fst(Var("p")), Snd(Var("p")))
PRODUCT_BETA_LEFT = Fst(Pair(Var("x"), Var("y")))
PRODUCT_BETA_RESULT = Var("x")


TERMS: dict[str, tuple[Term, Context]] = {
    "I_x": (I_X, {}),
    "I_y": (I_Y, {}),
    "I_beta": (I_BETA, {}),
    "I_product_beta": (I_PRODUCT_BETA, {}),
    "swap": (SWAP, {}),
    "swap_alpha": (SWAP_ALPHA, {}),
    "swap_beta": (SWAP_BETA, {}),
    "choose_first": (CHOOSE_FIRST, {}),
    "choose_second": (CHOOSE_SECOND, {}),
    "choose_first_product_beta": (CHOOSE_FIRST_PRODUCT_BETA, {}),
    "free_function": (FREE_FUNCTION, {"f": Arrow(A, B)}),
    "free_function_eta": (FREE_FUNCTION_ETA, {"f": Arrow(A, B)}),
    "free_product": (FREE_PRODUCT, {"p": Product(A, B)}),
    "free_product_eta": (FREE_PRODUCT_ETA, {"p": Product(A, B)}),
    "product_beta_left": (PRODUCT_BETA_LEFT, {"x": A, "y": B}),
    "product_beta_result": (PRODUCT_BETA_RESULT, {"x": A, "y": B}),
}

PAIRS = [
    ("I_x", "I_y"),
    ("I_x", "I_beta"),
    ("I_x", "I_product_beta"),
    ("swap", "swap_alpha"),
    ("swap", "swap_beta"),
    ("choose_first", "choose_second"),
    ("choose_first", "choose_first_product_beta"),
    ("free_function", "free_function_eta"),
    ("free_product", "free_product_eta"),
    ("product_beta_left", "product_beta_result"),
]

LEVELS = {
    "Q1-alpha": Q1_ALPHA,
    "Q2-alpha-beta": Q2_ALPHA_BETA,
    "Q3-alpha-beta-eta": Q3_ALPHA_BETA_ETA,
    "Q4-plus-product-beta-eta": Q4_FULL_PRODUCTS,
}


def class_count(names: list[str], equations: Equations) -> int:
    keys = {
        alpha_key(normalize(TERMS[name][0], equations))
        for name in names
    }
    return len(keys)


def main() -> None:
    inferred: dict[str, Type] = {}
    for name, (term, context) in TERMS.items():
        inferred[name] = type_of(term, context)

    print("TYPE CHECKS: PASS")
    for name in TERMS:
        print(f"  {name}: {inferred[name]}")

    print("\nPAIR MATRIX")
    header = ["pair", "Q0-raw", *LEVELS]
    print(" | ".join(header))
    for left_name, right_name in PAIRS:
        left, left_context = TERMS[left_name]
        right, right_context = TERMS[right_name]
        same_sequent = left_context == right_context and inferred[left_name] == inferred[right_name]
        if not same_sequent:
            raise AssertionError(f"pair has different sequents: {left_name}, {right_name}")
        values = [
            f"{left_name}/{right_name}",
            str(left == right),
            *(str(equivalent(left, right, equations)) for equations in LEVELS.values()),
        ]
        print(" | ".join(values))

    groups = {
        "P1 A->A": ["I_x", "I_y", "I_beta", "I_product_beta"],
        "P2 AxB->BxA": ["swap", "swap_alpha", "swap_beta"],
        "P3 AxA->A": [
            "choose_first",
            "choose_second",
            "choose_first_product_beta",
        ],
    }
    print("\nCLASS COUNTS AMONG CONSTRUCTED CLOSED TERMS")
    for group_name, names in groups.items():
        counts = [str(len(set(TERMS[name][0] for name in names)))]
        counts.extend(str(class_count(names, eqs)) for eqs in LEVELS.values())
        print(" | ".join([group_name, *counts]))

    assert inferred["I_x"] == Arrow(A, A)
    assert inferred["swap"] == Arrow(Product(A, B), Product(B, A))
    assert inferred["choose_first"] == Arrow(Product(A, A), A)
    assert not equivalent(CHOOSE_FIRST, CHOOSE_SECOND, Q4_FULL_PRODUCTS)
    print("\nSELECTED ASSERTIONS: PASS")


if __name__ == "__main__":
    main()

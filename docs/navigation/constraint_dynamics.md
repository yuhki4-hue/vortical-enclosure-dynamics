# Constraint Dynamics

This document clarifies how the word **constraint** is used across VED, IFGT,
and the application-layer papers. It is a navigation aid, not a new formal
definition.

## Core Usage

In VED / IFGT, a constraint is a structure that makes later states less
arbitrary than they would otherwise be. It can restrict, bias, stabilize, or
redirect possible motion.

This means that "constraint" is not limited to one familiar meaning such as
physical force, energy barrier, rule, loss function, or Bayesian update. Those
can be specific realizations of constraint in different layers.

The general question is:

```text
Given a possible field of motion, what structure makes some paths more
reachable, stable, likely, costly, or sustainable than others?
```

## Common Realizations

| Realization | Example | VED / IFGT reading |
|---|---|---|
| Physical or energetic constraint | barrier term, boundary condition, energy cost | A material or dynamical condition that limits reachable states or makes some transitions costly. |
| Geometric constraint | closure gradient, enclosure boundary, local horizon | A relation that bends or organizes possible paths without needing to be a literal wall. |
| Probabilistic constraint | biased transition probabilities, posterior concentration, learned distribution | A statistical structure that makes some future states more likely than others. |
| Biological constraint | metabolism, reward gradients, DNA-derived parameters, environmental coupling | A substrate-level condition shaping which living-system trajectories remain viable. |
| Cognitive / inferential constraint | attention, learned representation, stopping condition, external response | A structure that reduces otherwise open-ended inference or redirects reasoning. |
| Social constraint | shared record, consensus, institution, scientific protocol | A distributed structure that stabilizes or updates stopping conditions across agents. |

## Physical Constraint vs Probabilistic Bias

The two are not interchangeable, but VED / IFGT can treat both as constraint
when they play the same structural role.

- A physical barrier constrains by making some motion dynamically or
  energetically difficult.
- A probabilistic update constrains by changing the distribution of likely
  future states.
- A social consensus constrains by making some interpretations or actions
  collectively stable and others costly or unavailable.

The common feature is not the substrate. The common feature is the reduction or
organization of reachable trajectories.

## Comparison With Existing Concepts

| Existing concept | Overlap | Boundary |
|---|---|---|
| Energy barrier | Captures cost, resistance, and blocked transition. | VED / IFGT constraint is not always energetic or physical. |
| Boundary condition | Captures how a global or external condition shapes local dynamics. | Constraint can also be accumulated, statistical, biological, or social. |
| Bayesian posterior | Captures how new information biases later expectations. | VED / IFGT does not reduce all constraint to probabilistic belief update. |
| Loss function / training distribution | Captures learned bias in artificial systems. | The constraint is the structural effect on later motion, not the engineering objective alone. |
| Affordance | Captures environment-relative possibility. | IFGT formalizes this as a closure/constraint structure rather than only an ecological description. |

## Reading Rule

When reading "constraint" in this repository, ask which layer is being
discussed:

```text
physical layer      -> barrier, boundary, energy, closure geometry
IFGT layer          -> potential gradient, flow bias, quasi-closure structure
biological layer    -> viability, metabolism, DNA/environment parameters
cognitive layer     -> attention, representation, inference path bias
intelligence layer  -> stopping condition, external response, consensus
social layer        -> record, institution, shared update protocol
```

Do not automatically translate all of these into one substrate. The point is
that each can play an analogous structural role: shaping what can continue,
what becomes stable, and what paths remain open.

## Related

- [Translation Table](translation_table.md)
- [Common Misreadings: Constraint](common_misreadings.md#constraint)
- [IFGT fundamental dynamics](../../Information-Field-Geometry-Theory/sections/fundamental_dynamics.tex)
- [IFGT unified equation](../../Information-Field-Geometry-Theory/sections/unified_equation.tex)
- [Intelligence Part I](../../intelligence-part1/)

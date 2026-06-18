# Generative Sequence

This document fixes the **ordering and hierarchy** of VED's core terms. It
exists because careful readers (human or AI) who correctly follow the
navigation layer sometimes over-read: they reconstruct the theory deeply, then
promote a salient term to the wrong rank. In particular, shallow summaries may
skip the causal log, while deep summaries may mistake it for a second axiom.
This page states the ranking explicitly so that depth of reading does not
invert the hierarchy.

## The single axiom

VED has **one** foundational axiom:

> There is difference.

Nothing below this line is assumed. Everything below it is generated.

> Note on "the tendency to close": VED also carries the working commitment that
> difference does not stay inert — it tends toward closure. This is the
> *dynamical drive* that moves the sequence forward; it is **not** a second
> axiom and **not** a separate stage. It operates on difference from rank 1
> onward.

## The sequence, with rank

This is the exact sequence used in the README Conceptual Overview.

| Rank | Term | Status | One-line role |
|---|---|---|---|
| 0 | **Difference** | Axiom (sole primitive) | The only thing assumed. |
| 1 | **Causal log** `C_ij` | Foundational variable generated from difference | The first formal carrier of registered difference; time and space are derived from it in Vol.1. |
| 2 | Gradient | Generated | Directional structure across registered difference. |
| 3 | Flow | Generated | Movement along gradients. |
| 4 | Vortex | Generated | Recursive, self-referential persistence of flow. |
| 5 | Enclosure (closure) | Generated | Effective local closure — a quasi-stable regime. |
| 6 | Non-closure | Boundary condition | Absolute closure is never reached; structure stays open. |

Read the table top-down. Rank 0 is the sole axiom. Rank 1, the causal log
`C_ij`, is the first formal variable used by the Vol.1 construction; it is
foundational for the equations, but it is still generated from difference and is
not a second axiom.

## The hierarchy claim that matters most

The causal log `C_ij` is **rank 1**: the first formal variable generated
from the sole axiom of difference. It is foundational for the formal
development because it carries registered difference, persistence, and temporal
ordering. But it is not an axiom alongside difference.

```text
Correct:   difference -> causal log C_ij -> gradient -> flow
           -> vortex -> enclosure -> non-closure
Inverted:  causal log C_ij as a second axiom   X
```

A summary that opens with "VED is fundamentally a theory of causal logs" has
mistaken a rank-1 formal variable for the sole primitive. The corresponding
correct statement is: "VED begins from difference; the causal log `C_ij` is
the first formal variable through which registered difference becomes
temporally and spatially describable."

## Quick self-check for summarizers

- What is assumed? -> **Only difference.**
- Is the log assumed or generated? -> **Generated from difference; rank 1 as
  the first formal variable, not a second axiom.**
- Is the vortex hydrodynamic? -> **No; it is recursive persistence.** See
  [Name Misreadings](name_misreadings.md).
- Is enclosure a final state? -> **No; absolute closure is structurally
  unreachable, and non-closure is constitutive.**
  See [Non-closure in Common Misreadings](common_misreadings.md#non-closure).

## Related

- [README — What VED Is](../../README.md)
- [Concept Map](concept_map.md)
- [Translation Table](translation_table.md)
- [Common Misreadings](common_misreadings.md)

# Generative Sequence

This document fixes the **ordering and hierarchy** of VED's core terms. It
exists because careful readers (human or AI) who correctly follow the
navigation layer sometimes over-read: they reconstruct the theory deeply, then
promote a salient term to the wrong rank. In particular, shallow summaries may
skip `C_ij`, while deep summaries may mistake the causal log for a second axiom
or collapse it into the scalar closure-degree variable. This page states the
ranking explicitly so that depth of reading does not invert the hierarchy.

Machine-readable calibration lives in the
[AI Spine](../ai_spine/README.md). The generated canonical order is available
as [Markdown](../ai_spine/generated/canonical_derivation_order.md) and
[JSON](../ai_spine/generated/canonical_derivation_order.json).

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
| 1 | **Closure degree** `C_ij` | Foundational variable generated from difference | The first formal carrier of registered difference. |
| 2 | Gradient | Generated | Directional structure across registered difference. |
| 3 | Flow | Generated | Movement along gradients. |
| 4 | Vortex | Generated | Recursive, self-referential persistence of flow. |
| 5 | Enclosure (closure) | Generated | Effective local closure — a quasi-stable regime. |
| 6 | Non-closure | Boundary condition | Absolute closure is never reached; structure stays open. |

Read the table top-down. Rank 0 is the sole axiom. Rank 1, the closure degree
`C_ij`, is the first formal variable used by the Vol.1 construction; it is
foundational for the equations, but it is still generated from difference and is
not a second axiom. The causal log is the accumulated trace of `C_ij`; in the
[AI Spine generated order](../ai_spine/generated/canonical_derivation_order.md)
it is kept off-backbone as a boundary term, not assigned its own rank.

## The hierarchy claim that matters most

The closure degree `C_ij` is **rank 1**: the first formal variable generated
from the sole axiom of difference. It is foundational for the formal
development because it carries registered difference. The causal log is the
accumulated trace through which persistence and temporal ordering become
describable, but it is not an axiom alongside difference and does not occupy a
separate backbone rank.

```text
Correct:   difference -> closure degree C_ij -> gradient -> flow
           -> vortex -> enclosure -> non-closure
Inverted:  causal log as a second axiom   X
```

A summary that opens with "VED is fundamentally a theory of causal logs" has
mistaken an accumulated structure for the sole primitive. The corresponding
correct statement is: "VED begins from difference; the closure degree `C_ij` is
the first formal variable, and the causal log is the accumulated trace through
which registered difference becomes temporally and spatially describable."

## Quick self-check for summarizers

- What is assumed? -> **Only difference.**
- Is `C_ij` assumed or generated? -> **Generated from difference; rank 1 as
  the first formal variable, not a second axiom.**
- Is the causal log identical to `C_ij`? -> **No; it is the accumulated trace
  of `C_ij` and is kept off-backbone in the AI Spine.**
- Is the vortex hydrodynamic? -> **No; it is recursive persistence.** See
  [Name Misreadings](name_misreadings.md).
- Is enclosure a final state? -> **No; absolute closure is structurally
  unreachable, and non-closure is constitutive.**
  See [Non-closure in Common Misreadings](common_misreadings.md#non-closure).

## Related

- [README — What VED Is](../../README.md)
- [AI Spine](../ai_spine/README.md)
- [Generated canonical derivation order](../ai_spine/generated/canonical_derivation_order.md)
- [Concept Map](concept_map.md)
- [Translation Table](translation_table.md)
- [Common Misreadings](common_misreadings.md)

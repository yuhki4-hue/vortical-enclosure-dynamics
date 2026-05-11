# VED Overview

## Vortical Enclosure Dynamics: A Reader’s Map

*This document is a guide to the full framework. For formal derivations, see Vol.1-Vol.4.*

-----

## What This Framework Is

Vortical Enclosure Dynamics (VED) is an attempt to derive the structure of physical reality — time, space, particles, forces, gravity, and cosmology — from a single irreducible axiom, without importing background structures.

The starting point is not a Lagrangian, not a metric, not a symmetry group. It is a statement about difference:

> **差がある** — *There is difference.*

This is not a metaphor. It is a structural claim: a world with no internal asymmetry has no gradients, no flows, no dynamics, no observability. The existence of difference is the minimal condition for anything to happen at all.

From this axiom, VED constructs everything else through a sequence of well-defined steps. Each step is intended to introduce no independent physical primitives, but to develop the consequences of what came before.

-----

## The Problem With Existing Approaches

Before stating what VED does, it is worth stating what it refuses to do, and why.

**The Lagrangian approach** presupposes a background time parameter $t$ and a notion of reversible variation $\delta S = 0$. But if time itself is what we are trying to derive, we cannot use it as a foundation. The problem is not technical — it is structural. Irreversibility cannot be inserted into a time-symmetric framework from outside; it must be internal to the construction.

**General Relativity** takes the metric $g_{\mu\nu}$ as a primitive field and matter as an external input. VED derives both from the same underlying structure.

**The Standard Model** assumes gauge groups $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$ as given. VED derives them from the geometry of triangular closure.

**Conservation laws** — including $\nabla_\mu T^{\mu\nu} = 0$ — are taken as axioms in most frameworks. In VED, they are effective properties of a particular phase, not foundational principles.

The common thread: existing frameworks are effective theories of a specific phase of the underlying structure. VED attempts to describe that structure itself.

-----

## The Central Variable

The fundamental object is the **causal log** $C_{ij}$, a real-valued asymmetric matrix defined on a network of nodes.

Two objects are distinguished:

- $H_{ij}$: **causal history** — the irreversibly accumulated record of all causal influence from node $i$ to node $j$
- $C_{ij}$: **causal log** — the selectively retained portion of that history

The distinction $H \neq C$ is the key. Not all history becomes structure. The world is not the sum of everything that happened — it is the sum of what was selected.

The selection rule is self-referential:

$$\boxed{C_{ij} = 1 - \exp(-\lambda \rho_i H_{ij}), \qquad \rho_i = \sum_j C_{ij}}$$

The log density $\rho_i$ — how much structure node $i$ has already accumulated — determines how sharply it selects from new history. Structure generates selectivity; selectivity generates structure.

This self-referential equation has stable fixed points. Those fixed points are what we call the physical world.

-----

## Time and Space

From $C_{ij}$, time and space emerge as two aspects of the same process.

**Time** is the accumulation of causal logs:

$$\frac{d\tau_i}{dt} = \rho_i$$

The observational time $\tau_i$ at node $i$ advances in proportion to its log density. Where $\rho_i = 0$, time does not pass. Irreversibility is not assumed — it follows from the fact that $\rho_i \geq 0$ by definition. The second law of thermodynamics becomes a structural consequence, not a puzzle.

**Space** is the structure of causal connectivity. Decompose $C_{ij}$ into symmetric and antisymmetric parts:

$$S_{ij} = \tfrac{1}{2}(C_{ij} + C_{ji}), \qquad A_{ij} = \tfrac{1}{2}(C_{ij} - C_{ji})$$

$S_{ij}$ encodes spatial proximity; $A_{ij}$ encodes causal direction. Distance is defined as:

$$d_{ij} = -\log \tilde{S}_{ij}$$

where $\tilde{S}_{ij}$ is the maximum-path strength — the best available channel for influence to propagate from $i$ to $j$. The metric tensor $g_{\mu\nu}$ is the coarse-grained limit of this structure. It is not a primitive field. It is an effective description.

-----

## Particles and the Standard Model

The Standard Model emerges from the geometry of **triangular closure**.

A triangular closure is a stable configuration of three nodes where the causal log structure forms a self-sustaining loop. Such configurations are the minimal closed structures in the network — the smallest objects that can persist.

Whether a triangular closure is **non-degenerate** (full area in the abstract space of causal vectors) or **degenerate** (collapsed to lower dimension) determines the particle type:

- Non-degenerate closure → **baryons** (quarks, protons)
- Degenerate closure → **leptons** (electrons, muons)
- Extreme degenerate closure → **neutrinos**

The symmetry groups of these closure types are not assumed. They are derived:

- **SU(3)**: the group preserving non-degenerate triangular closure (3-component phase redistribution)
- **SU(2)**: the group mixing the two branches of degenerate closure (left/right)
- **U(1)**: global phase redundancy

$$
\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)
\;\longleftarrow\;
\text{closure geometry}
$$

Electric charge emerges from phase flux deviation within the triangle. The fractional charges $+2/3$ and $-1/3$ are interpreted as stable configurations under an effective non-closure constraint.

Mass is the curvature of the closure energy at the attractor:

$$m_k \propto \frac{1}{\Delta_k^2}, \qquad \Delta_k := L_{\max} - L_k$$

Heavy particles live close to the complete-closure limit. This limit should be read as a boundary representation, not as an ordinary attainable state. Three generations follow from the three edges of the triangle — each generation corresponds to one edge locking into place, in sequence, because simultaneous locking would erase the asymmetry required for dynamics.

-----

## Gravity

Gravity enters through a modification of the distance definition.

In Vol.1, distance was defined purely from $S_{ij}$. But closure density — the local concentration of triangular closures — distorts the effective cost of traversing a path. The unified distance becomes:

$$d_{ij} = \min_{\gamma: i\to j} \sum_{(ab)\in\gamma} \left[-\log S_{ab} + \epsilon L_{ab}\right]$$

This is not a new force. It is the same distance, with closure density contributing to path cost. Gravity is the distortion of distance by closure density.

In the continuous limit, the log-flow $J_{ij} = C_{ij} - C_{ji}$ has a Helmholtz decomposition:

$$J = J_\text{rot} + J_\text{pot}, \qquad \omega = \nabla \times J, \qquad L \sim |\omega|$$

The closure density $L$ is the vorticity of the log-flow. This is the sense in which the framework is **vortical**: stable closures are vortices in causal flow, and their density sources the gravitational potential:

$$\nabla^2 \Psi \propto L, \qquad g = -\nabla\Psi$$

The Einstein equations appear as the linearization of VED’s fixed-point equation $g_{\mu\nu} = g^{(0)}_{\mu\nu} + \alpha_G L_{\mu\nu}[g]$ in the weak-gravity, classical-active phase.

Newton’s constant is not primitive in this structural reading:

$$G \sim \frac{\eta_\phi , \epsilon}{4\pi , \kappa_{B,\mathrm{eff}}^2} , F(\lambda, \beta, \ldots)$$

Here $\kappa_{B,\mathrm{eff}}$ denotes an effective non-closure scale. Vol.4 reinterprets this kind of barrier parameter as a projected or coarse-grained quantity, rather than as a fundamental external prohibition. Its universality across particle species is a dynamic convergence property of the classical phase, not an axiom.

-----

## Black Holes and Cosmology

**Black holes** are not regions where spacetime ends. They are phase transitions.

Outside the horizon, the classical fixed-point condition holds: $\sigma \approx 0$, $\nabla\cdot J \approx 0$, the geometry is stable. At the horizon, this condition breaks down — the closure density $L$ grows until the fixed-point geometry can no longer be maintained.

The interior is a non-equilibrium closure phase, where log-generation $\sigma > 0$ reignites. The center is not treated as an ordinary singular object. In the older effective notation, the non-closure resistance was written as:

$$B(L) = -\kappa_{B,\mathrm{eff}} \log\!\left(1 - \frac{L}{L_{\max}}\right) \to \infty \quad \text{as } L \to L_{\max}$$

This term summarizes the fact that the system cannot be represented as fully closed within the generated description. The center is an asymptotic closure limit, not a literal divergence object.

**Cosmology** is the global regime where $\sigma > 0$ persists everywhere. In the homogeneous, isotropic limit, the framework reduces to:

$$\frac{d\rho}{d\tau} + 3\gamma\rho^2 = \sigma(\rho), \qquad H_\tau = \gamma\rho$$

The log-generation rate $\sigma(\rho) = \xi\rho(1-\rho/\rho_{\max})$ is derived from the self-referential structure of $C_{ij}$. This equation has a stable fixed point at $\rho_* = \xi/(\xi/\rho_{\max} + 3\gamma)$, corresponding to de Sitter expansion. The cosmological constant is not a free parameter — it is determined by the same closure structure that determines $G$.

-----

## The Phase Structure

A unifying theme across all scales is the **phase structure** of the causal log network.

The network admits four qualitatively distinct regimes, controlled by the effective coupling $\alpha_i = \lambda h_i$:

|Phase           |Condition      |Character                               |
|----------------|---------------|----------------------------------------|
|Subcritical     |$\alpha < 1$   |No time generation; no structure        |
|Critical        |$\alpha = 1$   |Phase boundary; maximum sensitivity     |
|Classical-active|$\alpha \sim 1$|Stable attractors; effective laws emerge|
|Saturated       |$\alpha \gg 1$ |Maximum log density; difference vanishes|

The laws of physics — conservation laws, gauge symmetries, the Einstein equations — are properties of the **classical-active phase**. They are not universal across all phases. This is why they break down at black hole interiors (saturated phase) and at the cosmological origin (transition from subcritical to active).

-----

## What Is and Is Not Claimed

VED is a **structural framework**, not yet a predictive theory.

What has been structurally formulated:

- Derivation of $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$ from closure geometry
- Qualitative mass hierarchy and charge quantization
- Weinberg angle as a geometric ratio
- Newton’s law from a vorticity Poisson equation
- Linearized Einstein equations from the fixed-point structure
- Schwarzschild-type exterior solution
- Non-singular black hole interior as a phase
- Cosmological expansion from sustained log-generation

What remains open:

- Quantitative derivation of any specific observable
- Exact nonlinear Schwarzschild solution
- CP violation and neutrino mass
- Formal quantization
- Computation of $G$, $\Lambda$, $v_{\mathrm{Higgs}}$ from microscopic parameters

The open problems are not failures of the framework — they are its next frontier. They are listed explicitly in [Open Problems](open_problems.md).

-----

## How to Read the Documents

```
Vol.1 — Foundations
  Axiom → C_ij → τ (time) → d_ij (space) → g_μν (metric)
  Key: why the Lagrangian was abandoned; phase diagram

Vol.2 — Standard Model
  Triangular closure → SU(3)×SU(2)×U(1) → particles, charges,
  masses, generations, electroweak unification, Higgs

Vol.3 — Gravity and Cosmology
  Log-flow → vorticity → gravity → Einstein equations →
  Schwarzschild → black hole interior → cosmological expansion

Vol.4 — Differential Horizon
  Divergence → renormalization → observation boundary →
  differential horizon → theory replacement and limits
```

Each volume builds on the previous. The reader who wants the full derivation should follow this sequence. The reader who wants a specific result can go directly to the relevant section using the correspondence table in the README.

-----

*VED does not claim to be the final word. It claims to be a coherent starting point — a structure that generates questions as clearly as it generates answers.*

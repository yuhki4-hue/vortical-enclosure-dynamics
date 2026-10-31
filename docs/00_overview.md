# VED Overview

## Vortical Enclosure Dynamics: A Reader’s Map

*This document is a guide to the full framework. For formal derivations, see Vol.1-Vol.4.*

-----

## What This Framework Is

Vortical Enclosure Dynamics (VED) is an attempt to construct a connected
formal account and candidate physical interpretations of time, space,
particles, forces, gravity, and cosmology from a single axiom.

The starting point is not a Lagrangian, not a metric, not a symmetry group. It is a statement about difference:

> **差がある** — *There is difference.*

This is not a metaphor. It is a structural claim: a world with no internal asymmetry has no gradients, no flows, no dynamics, no observability. The existence of difference is the minimal condition for anything to happen at all.

From this axiom, VED proposes a sequence of constructions with different
formal roles.  The sequence is not, by itself, a universal physical-emergence
derivation.

-----

## The Problem With Existing Approaches

Before stating what VED does, it is worth stating what it refuses to do, and why.

**The Lagrangian approach** commonly uses a background time parameter $t$ and
reversible variation $\delta S=0$. If physical time is itself the target of an
emergence claim, the relation between that parameter and the target clock must
be made explicit. VED proposes an internal accumulation construction but does
not thereby establish thermodynamic irreversibility.

**General Relativity** takes the metric $g_{\mu\nu}$ as a primitive field and
matter as an external input. VED proposes effective closure-based candidates
for comparison with those structures.

**The Standard Model** takes its gauge groups as part of its formal structure.
VED proposes a structural comparison with transformations of triangular
closure; exact physical derivation is not established here.

**Conservation laws** — including $\nabla_\mu T^{\mu\nu} = 0$ — are taken as axioms in many frameworks. In the current VED balance model, $\sigma=0$ marks a source-free phase regime. This formal classification does not establish whether physical conservation laws are fundamental or emergent.

The common thread: existing frameworks are effective theories of a specific phase of the underlying structure. VED attempts to describe that structure itself.

-----

## The Central Variable

The fundamental object is the **causal log** $C_{ij}$, a real-valued asymmetric matrix defined on a network of nodes.

**Source-identity note.** This overview follows the Vol.1 usage in which
$C_{ij}$ is the causal log. The navigation layer also uses $C_{ij}$ for a
closure-degree / rank-1 formal carrier and describes the causal log separately.
Those source-specific meanings are not identified here; their exact relation
remains open.

Two objects are distinguished:

- $H_{ij}$: **causal history** — the irreversibly accumulated record of all causal influence from node $i$ to node $j$
- $C_{ij}$: **causal log** — the selectively retained portion of that history

The distinction $H \neq C$ is the key. Not all history becomes structure. The world is not the sum of everything that happened — it is the sum of what was selected.

The selection rule is self-referential:

$$\boxed{C_{ij} = 1 - \exp(-\lambda \rho_i H_{ij}), \qquad \rho_i = \sum_j C_{ij}}$$

The log density $\rho_i$ — how much structure node $i$ has already accumulated — determines how sharply it selects from new history. Structure generates selectivity; selectivity generates structure.

The equations specify a fixed-point target.  Existence, stability, convergence,
and identification with persistent physical structure remain separate, open
requirements.

-----

## Time and Space

From $C_{ij}$, the model constructs a time-like accumulation quantity and a
network-distance quantity.  Their physical interpretations remain proposed.

**Time** is the accumulation of causal logs:

$$\frac{d\tau_i}{dt} = \rho_i$$

Here $t$ is the derivative / ordering parameter of this formulation. This
notation does not by itself identify $t$ with $\tau_i$, physical clock time,
or IFGT's effective external $t$.

At equation level this is a node-local accumulation definition relative to
$t$. The conditional implication $\rho_i\geq0\Rightarrow\tau_i$ is
non-decreasing is retained; physical-clock and physical-emergence claims are
not consequences of the displayed relation alone.

The quantity $\tau_i$ advances in proportion to log density and is
non-decreasing when $\rho_i\geq0$.  This establishes mathematical monotonicity
only.  State non-reconstructibility, thermodynamic irreversibility, and a
physical arrow of time are distinct claims and remain open here.

**Space** is the structure of causal connectivity. Decompose $C_{ij}$ into symmetric and antisymmetric parts:

$$S_{ij} = \tfrac{1}{2}(C_{ij} + C_{ji}), \qquad A_{ij} = \tfrac{1}{2}(C_{ij} - C_{ji})$$

$S_{ij}$ encodes spatial proximity; $A_{ij}$ encodes causal direction. Distance is defined as:

$$d_{ij} = -\log \tilde{S}_{ij}$$

where $\tilde{S}_{ij}$ is the maximum-path strength — the best available channel for influence to propagate from $i$ to $j$. The metric tensor $g_{\mu\nu}$ is proposed as an effective continuum description of the coarse-grained structure. The endpoint relation is a partial bridge: reconstruction, convergence, scaling, normalization, and uniqueness remain open. It is not a primitive field in this presentation.

Here $d_{ij}$ is a weighted-network path construction. Calling it an
ordinary metric additionally requires the relevant edge-domain, reachability,
symmetry, zero-distance, and disconnected-pair conventions; these are not all
fixed by the compact display.

-----

## Particle-Like Structures and Standard-Model Comparisons

The model proposes structural comparisons between **triangular closure** and
Standard-Model organization.

Within the finite simple-loop closure class used here, a triangle is the first
candidate enclosure.  Unrestricted uniqueness, persistence, and observational
particle identity are not established by that finite argument.

Within the model, triangular closures are grouped by whether they are
**non-degenerate** (full area in the abstract space of causal vectors) or
**degenerate** (collapsed to lower dimension). The resulting groups are
compared with particle-like types:

- Non-degenerate closure → **baryon-like candidate**
- Degenerate closure → **lepton-like candidate**
- Extreme degenerate closure → **neutrino-like candidate**

The following symmetry groups are proposed as structural correspondences for
these model closure types:

- **SU(3)**: the group preserving non-degenerate triangular closure (3-component phase redistribution)
- **SU(2)**: the group mixing the two branches of degenerate closure (left/right)
- **U(1)**: global phase redundancy

$$
\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)
\;\longleftarrow\;
\text{closure geometry}
$$

Electric charge receives a proposed phase-flux interpretation within the
triangle.  The fractional values are model configurations rather than
observationally derived charges here.

The model assigns a phenomenological mass-like scale from closure-energy
curvature:

$$m_k \propto \frac{1}{\Delta_k^2}, \qquad \Delta_k := L_{\max} - L_k$$

This scaling is phenomenological within the closure-barrier model; it is not,
at equation level, a calibrated derivation of observed particle mass.

Larger values of the phenomenological mass-like scale occur close to the
complete-closure limit. This limit is a boundary representation, not an
ordinary attainable state. The three edges motivate a candidate three-stage
generation interpretation; they do not establish observed particle generations.

-----

## Gravity

Gravity enters through a modification of the distance definition.

The closure quantities used below have different carriers: $L$ is the Vol.1
scalar closure-density / vorticity-intensity quantity, $L_{ab}$ is an
edge-level path-cost quantity, and $L_{\mu\nu}$ is a proposed tensorial /
coarse-grained quantity. Shared lettering does not identify them, and no
complete cross-carrier map is fixed in this overview.

In Vol.1, distance was defined purely from $S_{ij}$. But closure density — the local concentration of triangular closures — distorts the effective cost of traversing a path. The unified distance becomes:

$$d_{ij} = \min_{\gamma: i\to j} \sum_{(ab)\in\gamma} \left[-\log S_{ab} + \epsilon L_{ab}\right]$$

This adds closure density to the same path-cost construction.  Its reading as
physical gravity is a candidate effective interpretation, not an established
identification.

At the continuum level, the source uses a vector-field representation of the
log-flow and applies a Helmholtz decomposition. The bridge from discrete
$J_{ij}=C_{ij}-C_{ji}$ to that field is informal and open: no averaging,
scaling, orientation, or vector-field map is supplied here.

$$J = J_\text{rot} + J_\text{pot}, \qquad \omega = \nabla \times J, \qquad L \sim |\omega|$$

Within this continuum field representation, the curl is a derived definition
of vorticity. The $L\sim|\omega|$ relation is an effective proportional scalar
measure; its norm and normalization are not fixed and it is not a universal
identity.

The scalar $L$ is related effectively to the magnitude of log-flow vorticity.
This motivates a candidate vortical-enclosure and gravity-like interpretation:

$$\nabla^2 \Psi \propto L, \qquad g = -\nabla\Psi$$

These are effective weak-field / analogical relations in a continuum
scalar-field representation supporting the gradient and Laplacian. Their
coefficients, units, and boundary assumptions are not fully fixed here; they
are neither a discrete graph derivation nor an exact GR-recovery statement.

The Einstein equations are an intended weak-field comparison target for the
metric fixed-point relation.  A complete linearization with fixed coefficients
and nonlinear recovery is not supplied.

Newton’s constant is not primitive in this structural reading:

$$G \sim \frac{\eta_\phi , \epsilon}{4\pi , \kappa_{B,\mathrm{eff}}^2} , F(\lambda, \beta, \ldots)$$

Here $\kappa_{B,\mathrm{eff}}$ denotes an effective non-closure scale. Vol.4
reinterprets this kind of barrier parameter as a projected or coarse-grained
quantity, rather than as a fundamental external prohibition. Universality
across particle species is an open coarse-graining target, not an established
dynamic-convergence result.

-----

## Black Holes and Cosmology

**Black holes** receive a candidate phase-transition interpretation in this
model; this is not an established replacement for their physical spacetime
description.

In this proposed phase picture, the exterior is modeled by the classical fixed-point conditions $\sigma \approx 0$, $\nabla\cdot J \approx 0$. Loss of this regime near the horizon as closure density $L$ grows is a candidate interpretation, not an established stability result or a derivation of physical horizon dynamics.

The interior is proposed as a non-equilibrium closure phase in which a
$\sigma>0$ source regime is used. The center is treated as a candidate
asymptotic closure limit. In the older effective notation, the non-closure
resistance was written as:

$$B(L) = -\kappa_{B,\mathrm{eff}} \log\!\left(1 - \frac{L}{L_{\max}}\right) \to \infty \quad \text{as } L \to L_{\max}$$

This term encodes the model's non-closure constraint. Identifying the physical
center with that asymptotic limit remains an open interpretation.

**Cosmology** is modeled using a global $\sigma>0$ regime. Under the stated
homogeneous and isotropic approximation, the framework writes:

Here and in the Vol.1-derived continuum discussion, $\sigma$ denotes the
source-local log-generation rate. It is not identified here with microscopic
$\dot\rho_i$ or with IFGT's separately constructed generation term.

The continuum $\rho$ and $J$ in this regime are associated informally with
their node / edge quantities; interpolation, normalization, and the complete
discrete-to-continuum map remain open.

$$\frac{d\rho}{d\tau} + 3\gamma\rho^2 = \sigma(\rho), \qquad H_\tau = \gamma\rho$$

The logistic form $\sigma(\rho)=\xi\rho(1-\rho/\rho_{\max})$ is adopted as a
phenomenological source ansatz motivated by self-referential selection. The
displayed algebra has the stated fixed-point candidate
$\rho_*=\xi/(\xi/\rho_{\max}+3\gamma)$ and motivates a de Sitter-type comparison.
Stability, observed expansion, and the physical identities of $\Lambda$ and
$G$ are not established by that formal construction.

-----

## The Phase Structure

A unifying theme across all scales is the **phase structure** of the causal log network.

The network admits four qualitatively distinct regimes, controlled by the effective coupling $\alpha_i = \lambda h_i$:

|Phase           |Condition      |Character                               |
|----------------|---------------|----------------------------------------|
|Subcritical     |$\alpha < 1$   |Negligible time-like accumulation; no modeled structure|
|Critical        |$\alpha = 1$   |Phase boundary; maximum sensitivity     |
|Classical-active|$\alpha \sim 1$|Candidate stable structures and effective-law regime|
|Saturated       |$\alpha \gg 1$ |Maximum log density; difference vanishes|

Conservation, gauge, and gravitational structures are proposed as effective
features of the **classical-active phase**. Their identification with physical
laws and their behavior in black-hole or cosmological regimes remain open.

-----

## What Is and Is Not Claimed

VED is a **structural framework**, not yet a predictive theory.

What has been proposed or formally constructed:

- Structural comparison of $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$ with closure geometry
- Qualitative mass hierarchy and charge quantization
- Weinberg angle as a geometric ratio
- A gravity-motivated vorticity / Poisson analogy
- An intended weak-field Einstein comparison from the fixed-point structure
- A Schwarzschild-type exterior comparison
- Candidate non-singular black-hole-interior phase
- Candidate cosmological interpretation of sustained log-generation

What remains open:

- Quantitative derivation of any specific observable
- Exact nonlinear Schwarzschild solution
- CP violation and neutrino mass
- Formal quantization
- Computation of $G$, $\Lambda$, $v_{\mathrm{Higgs}}$ from microscopic parameters

The open problems are not failures of the framework — they are its next frontier. They are listed explicitly in [Open Problems](open_problems.md).

-----

## How to Read the Documents

The following is a reading order, not a sequence of identically typed
derivations. Each arrow means “continue to the next topic.” Formal definitions,
effective relations, OPEN representation bridges, and proposed physical
interpretations must be distinguished using the
[role-separated navigation table](navigation/generative_sequence.md).

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

Each volume uses material introduced earlier, but this ordering does not by
itself establish every displayed target as derived or physically generated.
The reader who wants the full argument should follow this sequence. The reader
who wants a specific result can go directly to the relevant section using the
correspondence table in the README.

-----

*VED does not claim to be the final word. It claims to be a coherent starting point — a structure that generates questions as clearly as it generates answers.*

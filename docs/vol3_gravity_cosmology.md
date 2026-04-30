# VED Vol.3 — Gravity and Spacetime Unification
## Vortical Enclosure Dynamics: From Closure Density to Gravity and Cosmology
*Independent Research Draft — 2026*

---

## Preface

Vol.1 began from a single axiom — *there is difference* — and derived the causal log $C_{ij}$ as the foundational variable from which time $\tau$ and space $d_{ij}$ emerge.

Vol.2 extended the same $C_{ij}$ to show that the structure of the Standard Model — particles, gauge groups, electric charge, mass, and generations — can be interpreted as consequences of closure geometry.

Vol.3 addresses gravity. The central claim is one:

$$\boxed{\text{Gravity is not a new force. It is a modification of the definition of distance.}}$$

The distance definition $d_{ij} = -\log\tilde{S}_{ij}$ from Vol.1 is determined by structure alone. Gravity, however, is a local bias in that structure. Incorporating this bias into the distance definition yields — in a single coherent line — the Einstein equation, the Schwarzschild solution, black holes, and cosmology.

*This theory does not yet possess quantitative predictive power. Structural organization is the present goal.*

---

## Chapter 1 — Where Does Gravity Come From?

### 1.1 The Distance of Vol.1 and Its Limitation

In Vol.1, distance was defined purely from the causal log structure:

$$d_{ij} = -\log \tilde{S}_{ij}, \qquad \tilde{S}_{ij} = \max_{\gamma: i\to j} \prod_{(ab)\in\gamma} S_{ab}$$

This definition selects the path of maximal propagation strength. Distance is therefore determined by the most permeable structural path.

$$\boxed{\text{Distance is determined solely by the structure of } C_{ij}.}$$

This construction yields a consistent geometry derived entirely from relational structure. However, an important limitation appears.

$$\boxed{\text{Gravity does not explicitly emerge from this definition.}}$$

The reason is that the distance above assumes structural homogeneity. All regions are treated equally except for variations encoded in propagation strength. No mechanism exists that biases path selection according to accumulated structure.

Gravity, however, appears precisely as such a bias.

---

### 1.2 What Is Gravity?

In conventional physics, gravity is introduced either as a force acting between masses, or as curvature of spacetime. VED adopts a different starting point.

$$\boxed{\text{Gravity is the phenomenon by which closure density distorts the distance structure.}}$$

This represents a shift in perspective. The conventional approach introduces a new interaction. VED modifies the definition of distance itself.

$$\boxed{\text{Gravity is not added. It is a reinterpretation of existing structure.}}$$

Thus gravity is not an independent entity, but an emergent bias in the same structural geometry already defined in Vol.1.

---

### 1.3 Extension of Distance

To incorporate this bias, assign a cost to each edge $(a,b)$:

$$w_{ab} = -\log S_{ab} + \epsilon\, L_{ab}$$

The first term represents geometric permeability, identical to Vol.1. The second term introduces a congestion cost due to closure density. Distance is then defined by minimizing total path cost:

$$\boxed{d_{ij} = \min_{\gamma: i\to j} \sum_{(ab)\in\gamma} w_{ab}}$$

This expression unifies geometry and gravitational effect within a single path selection principle.

---

### 1.4 What the Unified Path Implies

It is essential that both terms are evaluated along the same path. If propagation strength and closure density were evaluated on different paths, the geometry would split into separate structures.

$$\boxed{\text{Gravity alters path selection itself.}}$$

This mirrors the conceptual shift introduced by general relativity. Einstein replaced force with curvature. VED replaces curvature with path cost. The two descriptions differ in interpretation but agree structurally.

---

### 1.5 Summary of Chapter 1

By incorporating closure density into the distance definition, gravity emerges naturally from the same structural framework.

$$\boxed{\text{Gravity is not a new force.}}$$

$$\boxed{\text{It appears as a modification of the definition of distance.}}$$

This establishes the foundation for deriving gravitational geometry from closure structure in the following chapters.

---

## Chapter 2 — Closure Density and Geometry

### 2.1 The Quantity Called Closure Density

Chapter 1 introduced the quantity $L_{ab}$ as the additional contribution to the path cost:

$$\boxed{L_{ab} = \sum_k \phi_{abk}}$$

This represents the total contribution of triangular closures containing the edge $(a,b)$. Each triangle contributes to structural congestion, and the sum measures how densely that edge is embedded in closure structure.

Intuitively, regions with many triangles are structurally dense; regions with few triangles are structurally sparse.

$$\boxed{\text{Closure density = density of structure.}}$$

This interpretation follows directly from Vol.2, where triangular closure was identified as the minimal persistent structure.

---

### 2.2 Why It Distorts Distance

The modified edge cost introduced in Chapter 1 was $w_{ab} = -\log S_{ab} + \epsilon L_{ab}$. The first term favors highly permeable paths; the second penalizes structurally congested regions. Thus, large closure density increases traversal cost.

$$\boxed{\text{Closure density effectively stretches distance.}}$$

This reproduces the qualitative behavior associated with gravity: dense regions become harder to traverse, propagation paths bend around them, and effective geometry is distorted. Unlike general relativity, however, curvature is not introduced as a fundamental geometric postulate. It emerges from the modification of path selection.

---

### 2.3 Tensorization

Closure density is directional. An edge contributes differently depending on orientation. To describe this, define a coarse-grained tensor over a region $U$:

$$L_{\mu\nu}(x) = \left\langle L_{ab}\,\hat{e}^{(ab)}_\mu \hat{e}^{(ab)}_\nu \right\rangle_U$$

Here $\hat{e}^{(ab)}_\mu$ is the direction vector determined internally from the distance structure. No external embedding space is assumed.

$$\boxed{L_{\mu\nu} = \text{closure tensor.}}$$

This tensor encodes directional structural congestion and therefore determines anisotropic modifications of distance.

---

### 2.4 Relation to the Metric

The modification of distance can be absorbed into an effective metric:

$$g_{\mu\nu} = g^{(0)}_{\mu\nu} + \alpha_G L_{\mu\nu}$$

where $g^{(0)}_{\mu\nu}$ is the background metric derived in Vol.1, $L_{\mu\nu}$ is the closure tensor, and $\alpha_G$ is a structural coupling constant.

$$\boxed{\text{The metric is determined by closure density.}}$$

This is structurally analogous to the statement that matter curves spacetime, but no matter field has been introduced. Geometry is determined entirely by closure structure.

---

### 2.5 $G$ as an Effective Coupling

The coefficient $\alpha_G$ plays the role of gravitational coupling:

$$\boxed{G_{\text{eff}} \sim \alpha_G}$$

This constant is not fundamental. It arises as an effective parameter of coarse-grained closure structure. At microscopic scales, different particle closures may contribute differently; at macroscopic scales, coarse-graining averages these contributions. This produces an approximately universal gravitational coupling.

$$\boxed{\text{The universality of } G \text{ emerges dynamically.}}$$

---

### 2.6 Summary of Chapter 2

Closure density has been identified as the source of gravitational distortion.

$$\boxed{\text{Gravity = closure density.}}$$

The modification of distance induces an effective metric, and spacetime geometry emerges from coarse-grained closure structure.

$$\boxed{\text{Spacetime emerges as coarse-grained closure geometry.}}$$

This provides the geometric basis for deriving gravitational field equations in the next chapter.

---

## Chapter 3 — The Einstein Equation as a Fixed-Point Structure

### 3.1 Positioning the Question

So far, the following structure has been established: distance is derived from $C_{ij}$; gravity appears as closure density $L$; the metric takes the form $g_{\mu\nu} = g^{(0)}_{\mu\nu} + \alpha_G L_{\mu\nu}$. The next question is therefore unavoidable:

$$\boxed{\text{What equation does this structure obey?}}$$

In conventional physics, the Einstein equation $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ is postulated as a fundamental law. Within VED, the situation is reversed.

$$\boxed{\text{The gravitational equation is not assumed.}}$$

Instead, it must emerge from the same self-consistent closure structure.

---

### 3.2 Starting Point: The Fixed-Point Equation

Vol.1 introduced the self-referential structure:

$$C_{ij} = 1 - \exp(-\lambda \rho_i H_{ij}), \qquad \rho_i = \sum_j C_{ij}$$

This defines a nonlinear fixed-point problem.

$$\boxed{\text{Structure determines itself.}}$$

Geometry, density, and flow are all determined simultaneously by this self-consistency condition. This self-referential nature is the key to the emergence of gravitational field equations.

---

### 3.3 Continuum Limit and Vorticity

Upon coarse-graining, define the flow $J_{ij} = C_{ij} - C_{ji}$. In the continuum limit:

$$\omega = \nabla \times J, \qquad L \sim |\omega|$$

$$\boxed{\text{Closure density appears as vorticity of the flow.}}$$

This connects the microscopic closure structure to macroscopic geometric distortion.

---

### 3.4 Fixed-Point Condition

In the classical phase established in Vol.1:

$$\sigma \approx 0, \qquad \nabla \cdot J \approx 0$$

These conditions correspond to approximate conservation.

$$\boxed{\text{Conservation laws are properties of the phase.}}$$

Under these conditions, closure structure stabilizes and the metric becomes time-independent. This is the regime in which gravitational geometry emerges.

---

### 3.5 Self-Consistency Condition for the Metric

From Chapter 2, $g_{\mu\nu} = g^{(0)}_{\mu\nu} + \alpha_G L_{\mu\nu}$. However, $L_{\mu\nu}$ depends on flow, which depends on distance, which depends on the metric itself. Therefore $L_{\mu\nu} = L_{\mu\nu}[g]$, and the metric must satisfy:

$$\boxed{g_{\mu\nu} = g^{(0)}_{\mu\nu} + \alpha_G L_{\mu\nu}[g]}$$

This defines a fixed-point problem for the metric.

---

### 3.6 Linearization and the Form of the Equation

In the weak-gravity limit $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ ($|h_{\mu\nu}| \ll 1$), expanding the fixed-point equation to first order yields:

$$\boxed{G_{\mu\nu} = 8\pi G_{\text{eff}} L_{\mu\nu}}$$

$$\boxed{\text{Structurally analogous to the Einstein equation.}}$$

Thus the Einstein equation appears as the linear approximation of the self-consistent closure structure.

---

### 3.7 The Inversion

Conventional understanding: the Einstein equation = a fundamental law.

VED:

$$\boxed{\text{The Einstein equation is a linear approximation of a fixed-point structure.}}$$

It holds in the classical phase where closure is stable, but need not hold outside this regime. Gravity is therefore not fundamental but emergent.

---

### 3.8 Why General Relativity Works

This interpretation explains the empirical success of GR.

$$\boxed{\text{GR is not incorrect.}}$$

$$\boxed{\text{It is an effective theory of the classical closure phase.}}$$

In this phase, closure density varies slowly, conservation approximately holds, and the metric is stable. Under these conditions, the Einstein equation provides an accurate description.

---

### 3.9 Bridge to Chapter 4

The gravitational field equation has now emerged from closure structure. The next step is to examine specific solutions.

$$\boxed{\text{What do the solutions of this structure look like?}}$$

The simplest case is a localized concentration of closure density, leading to the Schwarzschild solution. This is examined in Chapter 4.

---

## Chapter 4 — The Schwarzschild Solution as Exterior Closure

### 4.1 What This Chapter Does

Chapter 3 showed that gravitational dynamics arise as a fixed-point structure of closure density. The next step is to examine the simplest configuration: static, spherically symmetric, and with localized closure density.

$$\boxed{\text{Closure concentrated at a single point.}}$$

In general relativity, this leads to the Schwarzschild solution. Within VED, the same structure emerges from modification of distance.

---

### 4.2 Definition of the Exterior Vacuum

Consider a localized closure distribution $L(x) = M\,\delta(x)$. Outside the localized region ($r > R$), $L(r) = 0$. In this region, closure density vanishes but the metric remains influenced by the boundary conditions imposed by the central structure.

The potential equation becomes:

$$\nabla^2\Psi \propto L = 0 \qquad \Rightarrow \qquad \nabla^2\Psi = 0$$

For spherical symmetry, the solution is:

$$\boxed{\Psi(r) = -\frac{G_{\text{eff}} M}{r}}$$

$$\boxed{\text{The Newtonian potential.}}$$

---

### 4.3 Form of the Metric

In the weak-gravity limit, the metric takes the form:

$$\boxed{ds^2 \approx -\left(1-\frac{2GM}{r}\right)dt^2 + \left(1+\frac{2GM}{r}\right)dr^2 + r^2 d\Omega^2}$$

This expression corresponds to the first-order expansion of the Schwarzschild metric.

$$\boxed{\text{Consistent with the Schwarzschild solution (weak-gravity limit).}}$$

The full nonlinear expression emerges when the fixed-point equation is solved beyond linear order.

---

### 4.4 What Is Happening

General relativity interprets this solution as curvature of spacetime. VED interprets it differently.

$$\boxed{\text{Distance cost is modified by closure density.}}$$

As a result, propagation paths change, light trajectories bend, time dilation appears, and an effective metric emerges. The observable consequences coincide, while the interpretation differs.

---

### 4.5 VED Interpretation of the Horizon

The Schwarzschild radius is $r_s = 2GM$. At this radius, $g_{tt} \to 0$. Within VED, this does not represent geometric breakdown.

$$\boxed{\text{The horizon is a critical point of path structure.}}$$

At this point, path cost diverges, propagation freezes, and closure density approaches a critical value. The horizon is therefore a phase boundary.

---

### 4.6 Summary of Chapter 4

The exterior gravitational solution emerges naturally from closure density.

$$\boxed{\text{The Schwarzschild solution appears as a limit of closure geometry.}}$$

No new force or curvature postulate is required.

$$\boxed{\text{Gravity emerges from modified distance.}}$$

---

### 4.7 Bridge to Chapter 5

The exterior solution describes the region outside the horizon. The next question concerns the interior. In general relativity, a singularity appears. Within VED, a different interpretation emerges.

$$\boxed{\text{Crossing the horizon changes the phase.}}$$

$$\boxed{\text{Black hole interior = non-equilibrium closure phase.}}$$

This is explored in Chapter 5.

---

## Chapter 5 — Black Hole Interior as a Non-Equilibrium Phase

### 5.1 Revisiting the Meaning of the Horizon

Chapter 4 showed that the Schwarzschild radius $r_s = 2GM$ appears as a critical point of the modified distance structure. At this radius, propagation cost diverges and the exterior solution ceases to apply.

$$\boxed{\text{The horizon is a phase boundary.}}$$

This interpretation differs from the conventional geometric breakdown. Instead, the horizon marks a transition between two regimes of closure dynamics.

---

### 5.2 Exterior vs. Interior

Outside the horizon, the classical phase holds:

$$\sigma \approx 0, \qquad \nabla \cdot J \approx 0, \qquad \partial_t C \approx 0$$

In this regime, closure structure is stable, conservation laws hold, and the metric is well-defined.

$$\boxed{\text{Exterior = classical closure phase.}}$$

Crossing the horizon changes these conditions.

---

### 5.3 Reignition of $\sigma$

Inside the horizon, the generation term becomes nonzero:

$$\boxed{\sigma > 0}$$

Log generation resumes and the fixed-point structure breaks down: $\partial_t C \neq 0$. This implies that geometry is no longer static.

$$\boxed{\text{Time begins to be generated again.}}$$

The interior therefore corresponds to a non-equilibrium regime of closure.

---

### 5.4 Collapse of the Fixed Point

In the exterior, $\partial_t C \approx 0$; in the interior, $\partial_t C \neq 0$. The metric is no longer determined by a fixed-point condition.

$$\boxed{\text{The fixed-point structure collapses.}}$$

Geometry becomes dynamically generated rather than static.

---

### 5.5 The Singularity Does Not Exist

General relativity predicts a singularity at the center. VED prohibits perfect closure. From Vol.1:

$$B(L) = -\kappa_B \log\!\left(1 - \frac{L}{L_{\max}}\right) \to \infty \qquad (L \to L_{\max})$$

$$\boxed{\text{Perfect closure is dynamically forbidden.}}$$

Therefore, the center is not a singularity but an unreachable limit.

---

### 5.6 Interior Dynamics

With $\sigma > 0$, closure structure is continuously regenerated.

$$\boxed{\text{The interior is a region of structural regeneration.}}$$

Logs are generated, closure reorganizes, and geometry evolves. The interior is therefore dynamically active rather than a state of collapse.

---

### 5.7 The Inversion

Conventional interpretation: black hole = endpoint.

VED:

$$\boxed{\text{Black hole = entry into a new phase.}}$$

The exterior is a fixed world; the interior is a world under generation.

---

### 5.8 Correspondence with the Early Universe

The early universe is characterized by $\sigma > 0$. The black hole interior also satisfies $\sigma > 0$.

$$\boxed{\text{The early universe and black hole interior are the same phase at different scales.}}$$

---

### 5.9 Conclusion of Chapter 5

$$\boxed{\text{The black hole interior is not a singularity.}}$$

$$\boxed{\text{It is a non-equilibrium closure phase.}}$$

Closure continues to evolve, and geometry remains dynamically generated.

---

### 5.10 Bridge to Chapter 6

The black hole interior corresponds to a local region with $\sigma > 0$. The next question is global:

$$\boxed{\text{What happens when this phase fills the entire universe?}}$$

This leads naturally to cosmology.

---

## Chapter 6 — Cosmology: The Global $\sigma > 0$ Phase

### 6.1 Shift in the Question

Chapter 5 identified the black hole interior as a local non-equilibrium closure phase characterized by $\sigma > 0$. This raises the natural global question:

$$\boxed{\text{What happens when the } \sigma > 0 \text{ phase extends across the entire universe?}}$$

Within the VED framework, the answer is direct:

$$\boxed{\text{Cosmic expansion emerges as a global } \sigma > 0 \text{ phase.}}$$

Thus cosmology is interpreted not as an initial condition, but as a phase of the closure dynamics.

---

### 6.2 The Fundamental Equation

From Vol.1, the continuity equation for log density is $\partial_t \rho + \nabla \cdot J = \sigma$. Under the homogeneous and isotropic approximation, $\nabla \cdot J \approx 3H\rho$, which yields:

$$\boxed{\dot{\rho} + 3H\rho = \sigma}$$

The first term represents dilution due to expansion; the second represents generation of structure.

---

### 6.3 The Equation in $\tau$-Time

Using the time definition from Vol.1, $d\tau/dt = \rho$, the equation becomes:

$$\boxed{\frac{d\rho}{d\tau} + 3H_\tau \rho = \sigma(\rho)}$$

The scale factor is defined structurally as $a(\tau) \sim \langle d_{ij}(\tau)\rangle$. Since the expansion rate is determined by density, $H_\tau \sim \rho$, giving:

$$H^2 \propto \rho \quad \Longleftrightarrow \quad \text{structurally analogous to the Friedmann equation.}$$

---

### 6.4 Final Form

Substituting $H_\tau \sim \rho$, the evolution equation becomes:

$$\boxed{\frac{d\rho}{d\tau} + 3\gamma \rho^2 = \sigma(\rho)}$$

Here $3\gamma\rho^2$ represents dilution due to expansion and $\sigma(\rho)$ represents generation of logs. Cosmology therefore emerges as competition between generation and dilution.

---

### 6.5 The Form of $\sigma$

From the self-referential structure of Vol.1, the minimal effective form is:

$$\boxed{\sigma(\rho) = \xi \rho \left(1 - \frac{\rho}{\rho_{\max}}\right)}$$

This corresponds to growth at low density and saturation at high density. The logistic form arises naturally from self-referential selection.

---

### 6.6 Fixed Point and de Sitter Phase

The fixed-point solution satisfies $3\gamma\rho_*^2 = \sigma(\rho_*)$, giving:

$$\rho_* = \frac{\xi}{\xi/\rho_{\max} + 3\gamma}$$

At the fixed point, $H_* = \gamma\rho_* = \text{const}$, and therefore:

$$\boxed{a(\tau) \sim e^{H_*\tau}}$$

$$\boxed{\text{de Sitter-type accelerated expansion.}}$$

---

### 6.7 Origin of the Cosmological Constant

The effective cosmological constant is:

$$\boxed{\Lambda_{\text{eff}} \sim \gamma^2\rho_*^2}$$

The cosmological constant is therefore not fundamental, but determined by closure structure.

---

### 6.8 The Inversion

Conventional cosmology: expansion = initial condition.

VED:

$$\boxed{\text{Cosmic expansion = phase selection.}}$$

If $\sigma = 0$, the universe is static. If $\sigma > 0$, the universe expands.

---

### 6.9 Unification with Black Holes

The black hole interior satisfies $\sigma > 0$; the expanding universe also satisfies $\sigma > 0$.

$$\boxed{\text{Black hole interior and cosmic expansion are the same phase at different scales.}}$$

---

### 6.10 Conclusion of Chapter 6

Cosmology emerges as global closure dynamics.

$$\boxed{\text{The universe is continuously generated.}}$$

$$\boxed{\text{Expansion is a consequence of } \sigma > 0.}$$

The large-scale dynamics of the universe follow directly from closure structure.

---

## Chapter 7 — Synthesis: The World as Structure

### 7.1 The Flow of This Theory

This work began from a single axiom:

$$\boxed{\text{There is difference.}}$$

From difference, gradients emerge. From gradients, flow appears. From flow, vorticity forms. From vorticity, closure develops.

$$\boxed{\text{Structure emerges from dynamics.}}$$

This sequence defines the foundation of VED.

---

### 7.2 The Overall Structure

The entire theory can be summarized by a single chain:

$$\boxed{\text{Difference} \;\rightarrow\; C_{ij} \;\rightarrow\; J \;\rightarrow\; \omega \;\rightarrow\; L \;\rightarrow\; g \;\rightarrow\; \text{Einstein equation} \;\rightarrow\; \text{Universe}}$$

| Quantity | Meaning |
|---|---|
| $C_{ij}$ | causal log |
| $J$ | flow of logs |
| $\omega$ | vorticity |
| $L$ | closure density |
| $g$ | effective metric |
| Einstein equation | fixed-point structure |
| Universe | global phase |

$$\boxed{\text{Everything forms a single structural chain.}}$$

---

### 7.3 Correspondence Across Volumes

The three volumes form a unified progression.

**Vol.1 — Generation:** causal log $C_{ij}$; time $d\tau/dt = \rho$; space $d_{ij} = -\log\tilde{S}_{ij}$. Structure is generated.

**Vol.2 — Structure:** triangular closure; gauge symmetry $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$; particles, charge, mass. Structure stabilizes.

**Vol.3 — Dynamics:** closure density → gravity; fixed-point structure → Einstein equation; $\sigma > 0$ phase → cosmic expansion. Structure evolves.

$$\boxed{\text{Generation, structure, and dynamics are unified.}}$$

---

### 7.4 Reinterpreting Conservation Laws

Conventional physics treats conservation laws as fundamental; violations appear as exceptions. Within VED, the continuity equation is:

$$\partial_t \rho + \nabla \cdot J = \sigma$$

Two regimes appear: $\sigma = 0$ implies conservation holds; $\sigma > 0$ implies generation occurs.

$$\boxed{\text{Conservation laws are properties of a phase.}}$$

Conservation is therefore not fundamental, but emergent.

---

### 7.5 Reinterpreting Gravity

Conventional interpretations treat gravity as force or as curvature. VED interprets it differently.

$$\boxed{\text{Gravity = modification of distance.}}$$

$$\boxed{\text{Gravity = closure density.}}$$

This connects gravitational dynamics directly to structural accumulation.

---

### 7.6 Black Holes and the Universe

The black hole interior satisfies $\sigma > 0$; the expanding universe also satisfies $\sigma > 0$.

$$\boxed{\text{Black hole interior and cosmic expansion are the same phase.}}$$

The difference is only scale.

---

### 7.7 The Final Inversion

Conventional physics begins by assuming spacetime, fields, and symmetry. VED instead derives them from structure.

$$\boxed{\text{Everything emerges from closure structure.}}$$

Time is generated. Space is relational. Particles are closure attractors. Forces are flow. The universe is a phase.

---

### 7.8 The Final Statement

The entire theory reduces to a single principle:

$$\boxed{\text{The world is not closed.}}$$

$$\boxed{\text{It exists by never fully closing.}}$$

This statement serves both as the starting point and the conclusion of VED.

$$\text{Difference} \;\rightarrow\; C_{ij} \;\rightarrow\; J \;\rightarrow\; \omega \;\rightarrow\; L \;\rightarrow\; g_{\mu\nu} \;\rightarrow\; \text{Einstein equation} \;\rightarrow\; \text{Universe}$$

$$\boxed{\begin{aligned}
\text{Time}     &= \text{quantity of logs} \\
\text{Space}    &= \text{structure of logs} \\
\text{Particle} &= \text{closure attractor} \\
\text{Gravity}  &= \text{potential from closure density} \\
\text{Universe} &= \text{phase of continuous generation}
\end{aligned}}$$

$$\boxed{\text{Everything emerges from a single root: } C_{ij}.}$$

---

## Appendix: Notation

| Symbol | Definition | Source |
|---|---|---|
| $C_{ij}$ | causal log matrix | Vol.1 |
| $\rho_i = \sum_j C_{ij}$ | log density | Vol.1 |
| $S_{ab}$ | symmetric component of $C_{ij}$ | Vol.1 |
| $d_{ij}$ | weighted shortest distance | Vol.3 §1 |
| $L_{ab} = \sum_k\phi_{abk}$ | local closure density | Vol.2+Vol.3 |
| $J_{ij} = C_{ij}-C_{ji}$ | log flow (antisymmetric) | Vol.3 |
| $\omega = \nabla\times J$ | vorticity | Vol.3 |
| $\sigma$ | log generation rate (source of time) | Vol.3 |
| $\Psi$ | gravitational potential | Vol.3 |
| $\alpha_G$ | gravitational coupling constant (structural) | Vol.3 |
| $G_{\text{eff}}$ | effective gravitational constant | Vol.3 |
| $r_s = 2G_{\text{eff}}M$ | Schwarzschild radius | Vol.3 §4 |
| $\sigma(\rho)$ | effective model of log generation rate | Vol.3 §6 |
| $\rho_*$ | cosmological fixed-point density | Vol.3 §6 |
| $H_*$ | de Sitter expansion rate | Vol.3 §6 |

---

*VED Vol.3 — Gravity and Spacetime Unification: From Closure Density to the Universe — 2026*

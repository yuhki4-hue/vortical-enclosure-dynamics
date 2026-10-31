# Information Field Geometry Theory (IFGT)

**— The Geometry of Quasi-Closure —**

---

## Abstract

This paper proposes Information Field Geometry Theory (IFGT). IFGT is a framework for describing information not as a substance or a description of states, but as a **quasi-closure**: a residual structure that persists when difference does not fully close in the process of approaching closure.

The theory is motivated by Vortical Enclosure Dynamics (VED) and proposes a
formal correspondence with its difference, flow, and closure vocabulary. IFGT
treats persisting unclosed structure as information. This is a related-branch
comparison, not an established identity or unification of the two theories.

IFGT introduces five basic variables: information density $I$, information flow $J$, information potential $\Phi$, informational time $\tau$, and the generation term $\sigma$. The relation between $I$ and $C$ is given by $I = f(1 - C)$, and $\sigma$ is defined as the mismatch between the current difference chain and the existing trace structure. In the final chapter, these components are assembled into an IFGT evolution equation for the closure-degree field $C(x,\tau)$ and presented as a proposed VED×IFGT correspondence. The cross-theory maps for $C$, time, and $\sigma$ remain OPEN.

Within this framework, information is not a static object of description but a dynamic process that participates in structural formation through the persistence of difference and the constraint of flow. IFGT thus provides a foundational theory for describing the general structure that may encompass informational behavior observed in biological and computational systems.

---

## 1. Introduction

The Information Field Geometry Theory (IFGT) proposed in this paper is a
framework for describing information not as a substance but as a geometric
structure. It is positioned as an upper-layer effective model motivated by VED;
the cross-theory connection is a proposed correspondence.

Information has traditionally been understood primarily as a description of states. When modern physics claims that "matter is also information," this information typically functions as a label attached to the state of a system. The information treated in this paper differs from this usage. Here, information refers to a **structural constraint** arising as a trace left behind when difference does not fully dissipate. Such information has no independent substance; it acts by constraining the paths and distributions of difference chains.

Information is not difference itself. Information appears when difference persists in a distinguishable form and becomes referable in relation to other differences. In this sense, information is a trace produced by the persistence of difference and functions as a scaffold for subsequent difference chains. Information is, therefore, the structure that makes the chaining of differences possible.

This structure is modeled as a fluctuation of difference that remains while
approaching closure and is called a **quasi-closure**. The relation of this
IFGT construction to VED physical persistence is proposed, not identified.

The IFGT model represents this interaction as circular: quasi-closure
constrains difference chains and biases flow, while subsequent differences may
remain as quasi-closures. Interpreting this model cycle as physical conversion
between information and matter is not established.

Information does not exist statically; it becomes manifest at boundaries where structural change occurs. Such a boundary functions as a front of change and affects the direction and intensity of difference chains. This boundary structure is especially prominent in biological and computational systems, where the interference of past traces with present change is observed as fluctuations of behavior or state.

Such information is concretely implemented in the nervous systems of organisms, the memory of computers, and the internal states of transformer models. These are not information itself but instances in which the structure that retains traces of difference and constrains flow is realized within a physical system. This paper does not address these specific implementations but aims to describe the general structure underlying them.

Thus, the information in this theory is understood as a structure of difference that persists in the process of approaching closure. This structure is described as a geometry that produces the flow and constraint of differences. IFGT provides a framework to describe this informational geometric structure with a minimal set of variables and relations.

### 1.1 On the notion of information

The term *information* is used with considerably different meanings across disciplines, and the position of this paper should be located within that landscape. We here organize four principal notions.

**Shannon information.**
In information theory, information is defined as a reduction of probabilistic uncertainty, quantified by $H = -\sum_i p_i \log p_i$. Meaning and weight are intentionally excluded from the formalism. This makes the theory mathematically powerful and domain-independent, but it does not address what information *is*, only how much of it is transmitted.

**Physical information (It from Bit).**
In the tradition of Wheeler and Landauer, information is treated as a label attached to the state of a physical system, with measurable consequences such as the thermodynamic cost of erasure. This formulation is rigorous, but its scope is constrained by the requirement of observability: only quantities that can be measured as physical observables enter the theory. As a consequence, aspects of information such as weight (the degree to which a particular informational structure shapes subsequent dynamics) and semantic interactions below a certain threshold tend to be excluded, not because they are absent, but because they are not directly captured by the available measurement formalism.

**Affordance (Gibson).**
In ecological psychology, Gibson (*The Ecological Approach to Visual Perception*, 1986) proposed that information resides not in the environment alone nor in the perceiver alone, but in the **relational structure** between them. An affordance — the possibility of action offered to an organism by its environment — carries a weight that is determined dynamically by context, rather than as a fixed physical magnitude. This captures an aspect of information that the physical formulation cannot: relationality, context-dependence, and dynamic weighting. However, the notion has remained largely descriptive and has not been given a dynamical formulation.

**The informal notion.**
In everyday usage, information is something that persists as meaning and continues to influence subsequent states. This notion is closer to the structural and dynamic aspects that the strict physical formulation leaves out, and it retains the relational character emphasized by affordance.

**Position of this paper.**
The information treated in IFGT is not Shannon information, nor a physical state label, but can be understood as **a dynamical formulation of the relational structure suggested by affordance and by the informal notion**. Concretely, it refers to the **structural constraint that persists as a quasi-closure** — a residue of difference that has not fully closed and that biases subsequent difference chains. The weight of such information is expressed geometrically, as the local depth of the closure-degree field $C$ (see §2.2 and §4.4). In this sense, IFGT aims to provide a dynamical description of the informational structure whose relational and weighted character has been recognized, but not formalized, in the preceding traditions.

---

## 2. Relation to VED

### 2.1 Division of roles

IFGT is presented as an upper-layer effective theory and proposes a comparison
with the **unclosed side** of the structure described by VED.

The division of roles between VED and IFGT is organized as follows.

- **VED**: Proposes physical interpretations of difference, gradient, flow, and closure constructions.
- **IFGT**: Uses its source-local scalar / field closure-degree variable to describe informational structure as a **quasi-closure**.

VED and IFGT are not treated as opposing theories; they are proposed as
complementary descriptions. No common-state-space identity, translation, or
equivalence is established.

### 2.2 The asymmetry between $I$ and $C$

The central quantity of VED is the closure degree $C \in [0,1]$. The central quantity of IFGT, the information density $I$, is related to $C$ by

**Source-identity note.** The $C$ and $C(x,\tau)$ used in this paper are the
scalar / field closure-degree quantities of IFGT. Shared lettering does not
identify them automatically with the causal-log matrix $C_{ij}$ defined in
Vol.1, and this paper supplies no identity map between those source-specific
objects.

**Bridge status: OPEN.** No matrix-to-field carrier map, interpolation,
normalization, or preserved-structure statement is supplied.

$$
I = f(1 - C),
$$

where $f$ is a non-decreasing function satisfying $I \to 0$ as $C \to 1$. In the region of complete closure, where $C$ reaches unity, information does not exist; information is defined only in the region where $C < 1$.

This relation shows that $I$ and $C$ are **not two expressions of the same quantity but complementary quantities**. $C$ describes "the degree of closedness," while $I$ describes "the density of the residue that failed to close." Both arise from the same field but can behave as independent quantities (for example, two regions with the same $C$ may have different spatial distributions of $I$ depending on their history).

This asymmetry is precisely what embodies the division of roles between VED and IFGT at the level of variables.

### 2.3 Informational time $\tau$ and generative time $\tau_{\mathrm{VED}}$

Three notions of time appear in this paper; we organize them here.

- **Ordering parameter $t$**: an externally given time axis. It is meaningful only in the effective description where the background spacetime is fixed (see §5.2).
- **Generative time $\tau_{\mathrm{VED}}$**: the observational time of VED Vol. 1. It is defined endogenously as the progression of difference consumption accompanying closure formation.
- **Informational time $\tau$**: the time introduced in IFGT. It is defined endogenously as the accumulation of **mutual interference between difference and the existing trace structure**.

$\tau_{\mathrm{VED}}$ and $\tau$ **differ in origin**. The former advances as closure proceeds; the latter advances as traces are updated.

The effective external $t$ used here is an IFGT source-local parameter. This
paper fixes no map identifying it with the derivative parameter $t$ used in
Vol.1.

This paper proposes a **dynamical correspondence** between the two and intends
IFGT's $\tau$ to be comparable with $\tau_{\mathrm{VED}}$. An isomorphism or
embedding is not established: no map, preserved structure, inverse, or common
axis construction is supplied. The bridge remains OPEN.

### 2.4 The circular relation

The relation between VED and IFGT is not a unidirectional reduction. The informational quasi-closure is not merely added on top of physical structure; through its mutual interference with physical structure, it alters subsequent difference generation and flow. Conversely, physical structure produces new differences, which in turn form informational structures as quasi-closures.

$$
\text{difference} \xrightarrow{\text{partial closure}} \text{quasi-closure (IFGT)} \xrightarrow{\text{constraint}} \text{structure (VED)} \xrightarrow{\text{regeneration}} \text{difference}
$$

(See Fig. 3.)

This cycle is particularly prominent in the nervous systems of organisms, the memory of computers, and the internal states of transformer models, all of which are concrete examples of quasi-closures in which traces of difference are retained and subsequent flows are biased. This paper does not address these specific implementations but aims to describe the general structure underlying them.

---

## 3. Correspondence with VED

The division of roles described in the previous chapter is now organized in terms of variable correspondence and dynamical correspondence.

### 3.1 Variable correspondence table

| VED | IFGT | Relation |
|-----|------|----------|
| closure degree $C \in [0,1]$ | information density $I$ | $I = f(1 - C)$ |
| difference $\Delta$ | information difference $\delta I$ | difference residue as trace |
| gradient $\nabla C$ | information gradient $\nabla I$ | opposite direction via $I=f(1-C)$ |
| closure flow $J_C$ | information flow $J$ | different aspects of the same flow |
| closure potential | information potential $\Phi$ | $\Phi = -\alpha C + \Phi_0$ |
| generative time $\tau_{\mathrm{VED}}$ | informational time $\tau$ | proposed correspondence; map OPEN |
| — | generation term $\sigma$ | proposed correspondence to VED difference generation; translation OPEN |

### 3.2 Difference $\Delta$ and information difference $\delta I$

In VED, the difference $\Delta$ is a primitive quantity derived directly from the foundational axiom "*there is difference*" and serves as the driver of closure formation. In IFGT, the information difference $\delta I$ is the residual difference that remains when difference does not fully close.

Whereas $\Delta$ is unprocessed difference itself, $\delta I$ is interpreted as "the part that did not contribute to closure." The following relation therefore holds:

$$
\Delta = \Delta_{\to C} + \delta I,
$$

where $\Delta_{\to C}$ is the component of difference that contributes to closure and $\delta I$ is the component that persists as a quasi-closure.

### 3.3 Structural correspondence

In the proposed VED field representation, difference, gradient, flow, and
closure are connected by formal and effective relations. This comparison does
not establish universal necessity or physical persistence across every step.

In IFGT, when difference does not fully close, it persists as a quasi-closure. This quasi-closure accumulates as a trace, constituting the information density $I$. The non-uniformity of traces produces the information gradient $\nabla I$, which drives the information flow $J$. Furthermore, the accumulation of quasi-closures constrains the flow, which is described as the information potential $\Phi$.

### 3.4 Dynamical correspondence

| Aspect | VED | IFGT |
|--------|-----|------|
| structure | closure (stable, tending to rest) | quasi-closure (circulatory, persisting motion) |
| terminal state | complete closure $C \to 1$ | metastable circulation |
| time evolution | closure formation | trace update |

Closure is a stable structure tending toward rest, whereas a quasi-closure forms a circulatory structure while maintaining flow. This circulation strengthens local constraints and draws in surrounding flow.

### 3.5 Generation and mismatch

The generation term $\sigma$ in IFGT represents the mismatch between the current difference chain and the existing quasi-closure structure. This mismatch corresponds to the generation of new differences in VED and induces the update of structure.

Thus this paper places a **proposed correspondence** between difference
generation in VED and generation through $\sigma$ in IFGT. It does not establish
that the two quantities are identical descriptions of one process, and no
explicit translation is fixed here.

---

## 4. Fundamental Dynamics

IFGT is a theory that describes motion within a quasi-closure, which appears as a fluctuation of difference that does not fully close. A quasi-closure is not separated from physical structure but interacts with it within the same generative process. Through this mutual interference, the informational quantities evolve in time.

This chapter defines the basic variables of the information field and introduces their evolution equations.

### 4.1 Definition of basic variables

**Information density $I$.**
The information density $I$ is the density of traces left behind when differences fail to dissipate — the accumulation of persisting history. As stated in the previous chapter, $I$ is related to VED's closure degree $C$ by $I = f(1 - C)$.

**Information flow $J$.**
The information flow $J$ is a vector quantity representing the direction and manner in which difference propagates. It describes the paths and distributions of change within a quasi-closure.

**Information potential $\Phi$.**
The information potential $\Phi$ is a scalar quantity representing the strength with which the information flow is constrained and biased toward specific paths. It acts as interference with fluctuations and restricts the degrees of freedom of difference chains. The relation between $\Phi$ and $C$ is given by $\Phi = -\alpha C + \Phi_0$, where $\alpha$ is the constraint coupling constant and $\Phi_0$ is an arbitrary constant (which vanishes under the gradient and thus does not contribute to the dynamics).

**Informational time $\tau$.**
The informational parameter $\tau$ is defined as an ordering / accumulation
quantity associated within IFGT with interaction between difference chains and
structural constraints (see §2.3). This is an internal model interpretation,
not an established emergence of physical time.

**Generation term $\sigma$.**
The generation term $\sigma$ is the quantity representing the mismatch between the current difference chain and the existing informational trace structure. Such mismatch arises when the compatibility between structure and flow breaks down, inducing the generation of new differences and changes in the information density. The concrete construction of $\sigma$ is developed in Chapter 5.

This $\sigma$ is a source-specific IFGT quantity. This paper does not identify
it with the Vol.1 continuum log-generation rate $\sigma$ or with microscopic
$\dot\rho_i$.

### 4.2 Basic equation

The time evolution of the information density is determined by transport via the information flow and by the generation term:

$$
\frac{\partial I}{\partial \tau} + \nabla \cdot J = \sigma.
\qquad (4.1)
$$

This is a balance / evolution relation within the related-branch IFGT
continuum field model. Its equation role is internal to IFGT's field
assumptions and does not identify its fields with VED Vol.1 quantities across
the OPEN bridges.

The first term on the left represents the time change of information density, and the second term represents the transport effect due to the divergence of the information flow. The right-hand side $\sigma$ represents the difference generation due to mismatch.

### 4.3 Construction of the information flow

The information flow is specified by the gradient of trace density and by the information potential:

$$
J = -D \nabla I + \mu F_I,
\qquad (4.2)
$$

$$
F_I = -\nabla \Phi = \alpha \nabla C.
\qquad (4.3)
$$

Here $D$ is the diffusion coefficient, $\mu$ the potential response coefficient, and $\alpha$ the constraint coupling constant. The first term represents a diffusive flow that resolves the non-uniformity of trace density; the second term represents a flow following the potential gradient.

The $F_I$ given by (4.3) acts as a **constraint force** drawing the information flow toward specific paths through the gradient of the closure degree. In regions where $\nabla C$ is large (the boundaries of closure), strong constraint is exerted and the flow is drawn in.

**Terminology.** The structure expressed by (4.3) — "the gradient of the closure degree draws in the flow" — could, by analogy with existing physics, be called **information gravity**. This is a useful designation that aids intuitive understanding: if $\nabla C$ is read as $\nabla \Phi_{\mathrm{grav}}$, then it plays formally the same role as the potential gradient in Newtonian gravity.

However, this paper does not identify $F_I$ with gravity in the usual sense (a force arising from the curvature of spacetime). We treat it solely as a potential gradient that geometrically constrains the degrees of freedom of difference chains. In what follows, we therefore prioritize descriptive clarity and unify the terminology as "**constraint potential gradient**" or "**information-geometric force**." The designation *information gravity* may be used for intuitive explanation or as a bridge to other domains, but within the internal description of the theory we adopt the vocabulary of information geometry.

### 4.4 Quasi-closure and circulatory structure

When the bias of informational traces grows stronger, the fluctuations of the difference chain become fixed along specific paths, and the degrees of freedom of flow decrease. However, since complete closure is not attained, the flow does not stop; instead, it forms a circulatory structure.

This circulation strengthens local constraints and draws in surrounding flow. As a consequence, this structure can be described as possessing **inertial properties**. The mass-like quantity in IFGT is characterized by the local depth of $C$ (closure strength) and is understood as the degree of update resistance.

---

## 5. The Unified VED×IFGT Equation

The evolution equation (4.1) of the information field introduced in the previous chapter does not specify the concrete construction of $\sigma$. In this chapter, we expand $\sigma$ as the mismatch between the difference chain and the existing trace structure and assemble a single equation for the IFGT closure-degree field $C(x,\tau)$ used in the proposed VED–IFGT correspondence. The internal equation is retained; the matrix-to-field and cross-theory bridges remain OPEN.

### 5.1 Expansion of the generation term $\sigma$

$\sigma$ consists of three contributions.

**(i) Driving term — supply of unclosed difference**

In regions where differences have not yet been incorporated into closure, new quasi-closures are generated. This contribution is proportional to the closure margin $(1 - C/C_*)$ and the difference source $\Delta$:

$$
\sigma_{\mathrm{drive}} = a \, \Delta \, (1 - C/C_*).
$$

Here $\Delta$ denotes the difference source in VED (§3.2), $a$ is the generation rate, and $C_*$ is the effective closure upper bound. As $C \to C_*$, the driving vanishes.

**(ii) Dissipation term — collapse of traces**

Quasi-closures decay over time, either being reabsorbed into closure or being released again as difference. This contribution is proportional to the trace density (equivalently, the local strength of $C$):

$$
\sigma_{\mathrm{dissip}} = -\Gamma \, C,
$$

where $\Gamma$ is the dissipation rate.

**(iii) Effective barrier term — non-closure constraint**

Complete closure at $C = C_{\max} = 1$ is not treated as an ordinary attainable state, because it would remove the residual difference required for quasi-closure and informational persistence. In the present effective model, this non-closure constraint is represented by a repulsive phenomenological term:

$$
\sigma_{\mathrm{barrier}} = -\frac{\kappa_B}{C_{\max} - C},
$$

where $\kappa_B$ is an effective barrier strength. This term does not claim to be the microscopic origin of non-closure; it encodes, at the present level of description, the resistance to complete closure required for circulation as a quasi-closure.

### 5.2 The unified VED×IFGT equation

Substituting the above into (4.1) and expressing the information density $I$ as a function of $C$, we obtain a single evolution equation for the closure-degree field $C(x,\tau)$.

For the relation between $I$ and $C$, we adopt the **linear assumption** as the leading-order approximation:

$$
I = f(1 - C) = 1 - C.
\qquad (5.1)
$$

Nonlinear corrections $f(x) = x + O(x^2)$ are left for future work. Under this assumption, $\nabla I = -\nabla C$, and the sign is inverted when the information flow $J$ is rewritten as the closure flow $J_C$.

Substituting into (4.1), we obtain the following unified equation:

$$
\boxed{
\frac{\partial C}{\partial \tau} + \nabla \cdot J_C = a \, \Delta \, (1 - C/C_*) - \Gamma \, C - \frac{\kappa_B}{C_{\max} - C}
}
\qquad (5.2)
$$

This equation is understood on the effective domain
$0 \le C < C_{\max}$. Near both boundaries, additional regularization terms
may be required in a microscopic model.

For equation-role purposes, (5.2) is an IFGT-internal evolution equation
under the stated linear and phenomenological assumptions. The word “unified”
does not establish an identity, translation, or derivation across the OPEN
VED–IFGT bridges.

$$
J_C = -D \nabla C - \mu \alpha \, C \nabla C.
\qquad (5.3)
$$

The second term on the right-hand side of (5.3) originates from the constraint potential gradient $F_I = \alpha\nabla C$ given in (4.3), rewritten in terms of $C$ under the linear assumption (5.1).
Here $C_*$ denotes the effective saturation scale of quasi-closure, while
$C_{\max}=1$ denotes the ideal complete-closure boundary. In general,
$C_* < C_{\max}$ in informational regimes.

**On the temporal argument.** The time derivative in (5.2) is taken with
respect to IFGT's informational parameter $\tau$ (§2.3). The model interprets
$\tau$ as tied to closure-field updating. This supplies an internal ordering
interpretation, not an established emergence of physical time.

However, in the approximate regime in which $C$ is sufficiently mature and the background spacetime may be regarded as nearly fixed, $\tau$ can be replaced by an external time $t$:

$$
\frac{\partial C}{\partial t} + \nabla \cdot J_C = \cdots,
\qquad (5.2')
$$

and this form is directly comparable with existing reaction–diffusion equations and Ginzburg–Landau-type equations. In this paper, the $\tau$-form (5.2) is taken as fundamental, while the $t$-form (5.2′) is positioned as an effective description.

### 5.3 Interpretation of the unified equation

Equation (5.2) could, in principle, generate an extremely broad class of structures from the single field $C(x,\tau)$. Although detailed analysis is beyond the scope of this paper, we list below, as a guide for future development, the directions in which structures might be identified. Note that when "circulation" or "limit cycle" is mentioned below, it refers to circulation as a solution of equation (5.2); this is a different level of discourse from the conceptual circulation between VED and IFGT described in §2.4.

- **Spatial structure** — potentially corresponding to smooth gradient regions of $\nabla C$
- **Temporal structure** — potentially corresponding to the $\tau$-evolution as a relaxation process
- **Particle-like structure** — potentially corresponding to deeply localized stable solutions (regions where $C$ is locally close to $C_*$)
- **Meaning-like structure** — potentially corresponding to shallowly localized metastable solutions (regions where $C$ stays at intermediate values)
- **Life-like structure** — potentially corresponding to limit-cycle-type circulatory solutions
- **Intelligence-like structure** — potentially corresponding to nontrivial global solutions involving closure reconfiguration

These may be investigated as candidate solution classes of (5.2), but their
existence and physical identification lie beyond this paper. The historical
label “unified” refers to the internal assembly of IFGT terms; equation (5.2)
does not supply the open VED–IFGT translation maps.

### 5.4 The minimal foundation and effective tendency

Equation (5.2) is built from one foundational axiom and one effective
dynamical tendency:

1. *There is difference.* (the foundational axiom of VED)
2. *Difference tends to form partial closure.* (an effective dynamical tendency used at the IFGT layer)

From the foundational axiom, the driving and effective barrier terms are
motivated; from the effective tendency, the dissipation term and the
construction of the information flow are introduced. The IFGT equation does
not add a second VED axiom, but neither does it establish a unified
cross-theory system without the open translation maps.

---

## 6. Conclusion

This paper has proposed Information Field Geometry Theory (IFGT) and redefined information as the structure of a quasi-closure that persists as a trace of difference. Under this framing, information is understood not as a description of states or an independent substance, but as a geometric structure that constrains the paths and distributions of difference chains.

IFGT is positioned as an upper-layer theory motivated by VED and proposes a
correspondence between physical-persistence and quasi-closure vocabularies. The
two are potentially complementary frameworks, not established descriptions of
one identical structure. The relation $I=f(1-C)$ is internal to IFGT's
source-local closure-degree field and does not close the VED bridge.

The theory introduces the information density $I$, the information flow $J$, the information potential $\Phi$, the informational time $\tau$, and the generation term $\sigma$ to describe motion within a quasi-closure. In Chapter 5, $\sigma$ is expanded into three contributions — driving, dissipation, and barrier — and a single IFGT evolution equation for the closure-degree field $C(x,\tau)$ is presented as a proposed VED×IFGT correspondence. The cross-theory maps remain OPEN. This equation is built from the foundational VED axiom "*there is difference*" together with the IFGT-layer effective tendency that difference forms partial closure.

Within this framework, information is modeled as a dynamic process involved in
structural formation through persistent difference and constrained flow. A
cyclic relation to physical structure is proposed; cross-theory physical
identity is not established.

This paper has not addressed the concrete implementations in biological or computational systems, but the structure described by IFGT is suggested to appear prominently in such systems. The theory aims at a general description of structure that does not depend on any particular domain.

The scope of the theory is, at present, limited to the minimal description of informational structure and the introduction of the unified equation. Further developments may include the correspondence with concrete structures in domains such as life, consciousness, language, and intelligence, as well as detailed analysis of the unified equation (5.2) (classification of stable solutions, existence conditions for limit-cycle solutions, renormalization structure, and so on), but these lie beyond the direct scope of this paper.

In sum, IFGT provides a minimal theory for describing, as geometry, the motion of quasi-closure that persists in the process by which structure is generated from difference. This paper presents its foundational framework; detailed developments and applications remain as future work.

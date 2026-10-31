# Core Equations

This note collects the compact equation-level summary that previously appeared in the top-level README.

## Core Equation

This equation set defines a causal-log self-consistency target and a
node-local time-like accumulation quantity. A physical-time interpretation is
proposed separately.

$$C_{ij} = 1 - \exp(-\lambda \rho_i H_{ij}), \qquad \rho_i = \sum_j C_{ij}, \qquad \frac{d\tau_i}{dt} = \rho_i$$

**Role / domain scope.** The first two relations form a node-indexed
constitutive / self-consistency target; they are not by themselves an update
map or an existence, uniqueness, convergence, or stability result. The last
relation defines a node-local time-like accumulation quantity relative to the
derivative parameter $t$. Conditional on $\rho_i\geq0$, $\tau_i$ is
non-decreasing with respect to that parameter; no physical-clock identity is
implied by the equation alone.

$H_{ij}$: causal history (irreversibly accumulated)  
$C_{ij}$: causal log (selectively retained — $H \neq C$ is the key)  
$\rho_i$: log density (rate input to the local accumulation definition)
$\tau_i$: node-local time-like quantity (conditionally monotone; physical-clock identity open)

**Source-identity scope.** In this Vol.1-derived equation set, $C_{ij}$ denotes
the causal log. Some navigation records use the same glyph for a
closure-degree / first-formal-carrier variable and distinguish the causal log
as its accumulated trace. No identity map between those source-specific uses
is fixed here. Likewise, $t$ is the derivative / ordering parameter used in
this formulation, and $\sigma$ below is the Vol.1 continuum log-generation
rate; neither is identified here with physical clock time, microscopic
$\dot\rho_i$, or IFGT's source-specific $t$ and $\sigma$.

## Core Structure

The following historical compact summaries are navigation mnemonics:

```text
difference → gradient → flow → vortex → closure → particle → time → space
```

and, in carrier-compressed form:

```text
C → J → ω → L → g
```

They do not assign one logical meaning to every arrow. The canonical
[role-separated navigation table](navigation/generative_sequence.md) records
the source and target, representation, formal status, bridge status, and
physical ceiling of each relation. In particular:

| Local relation | Role / status |
|---|---|
| represented difference $\to\nabla\delta$ | represented-field construction |
| $\nabla\delta\to J$ | effective proportional relation |
| causal-log $C_{ij}\to J_{ij}$ | discrete definition |
| $J_{ij}\to\mathbf J(x)$ | informal / OPEN bridge |
| $\mathbf J(x)\to\omega$ | continuum definition |
| $\omega\to L$ | effective / phenomenological relation |
| $S_{ij}\to d_{ij}$ | weighted-network construction |
| $d_{ij}\to g_{\mu\nu}$ | partial / OPEN bridge |
| formal quantities $\to$ physical time, particle, space, or gravity | proposed physical interpretation, not an established implication |

Carrier labels used in the compact form are:

- **C**: causal log (selected interactions)
- **J**: log flow
- **ω**: vorticity (curl of flow)
- **L**: closure density (vortical enclosure)
- **g**: effective geometry (metric structure)

Here $L$ is the Vol.1 scalar closure-density / intensity quantity. The
edge-level $L_{ab}$ and tensorial $L_{\mu\nu}$ used in Vol.3 are distinct
carrier-specific quantities. Shared lettering does not supply a map among
them.

**Bridge-status scope.** The discrete-to-continuum relations for $J$ and
$\rho$, the network-distance-to-metric relation, and the scalar/edge/tensor
$L$ relations are informal or partial endpoints and remain OPEN. This summary
supplies no interpolation, projection, tensorization, convergence, or identity
map among them.

**Equation-role scope.** In continuum passages, $\omega=\nabla\times J$ is a
derived definition and $L\sim|\omega|$ is an effective proportional scalar
measure whose norm and normalization are not fixed. Network distance is a
weighted-path construction; ordinary metric status needs additional
positivity, reachability, symmetry, zero-distance, and disconnected-pair
conditions. These equation roles do not themselves supply the physical
interpretations named in the mnemonic.

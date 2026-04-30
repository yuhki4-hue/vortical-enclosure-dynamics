# Core Equations

This note collects the compact equation-level summary that previously appeared in the top-level README.

## Core Equation

This equation defines how irreversible causal history ($H$) is selectively compressed into causal logs ($C$), thereby generating time locally.

$$C_{ij} = 1 - \exp(-\lambda \rho_i H_{ij}), \qquad \rho_i = \sum_j C_{ij}, \qquad \frac{d\tau_i}{dt} = \rho_i$$

$H_{ij}$: causal history (irreversibly accumulated)  
$C_{ij}$: causal log (selectively retained — $H \neq C$ is the key)  
$\rho_i$: log density (= local time generation rate)  
$\tau_i$: observational time (monotone by definition; irreversibility is built in)

## Core Structure

The entire framework can be summarized as a generative chain:

```text
difference → gradient → flow → vortex → closure → particle → time → space
```

and more formally:

```text
C → J → ω → L → g
```

Where:

- **C**: causal log (selected interactions)
- **J**: log flow
- **ω**: vorticity (curl of flow)
- **L**: closure density (vortical enclosure)
- **g**: effective geometry (metric structure)

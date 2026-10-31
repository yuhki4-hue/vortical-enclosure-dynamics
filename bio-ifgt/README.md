# Bio-IFGT

Bio-IFGT: Biological Morphogenesis as Information-Flow Attractor Dynamics is a LaTeX paper that explores a proposed biological-scale description related to IFGT/VED.

The project frames biological development through biological constraint-density \(\I\), information flow \(\J\), induced potential \(\PhiI\), and a proposed attractor-based interpretation. DNA is treated as a parameter set or operator-only medium. Morphogenesis, life, robustness, and regeneration are interpretive/model targets: concrete convergence, basin stability, operational biological identification, maintenance, and reconstruction remain open.

This repository is related to the note essay as a formalization layer. The note may motivate the conceptual background, but this paper keeps the technical language centered on non-closure, flow, stability, sustained dynamics, and effective attraction or gradient-driven bias. Intelligence appears only near the end as a second attractor built upon life.

## Structure

- `main.tex`: Canonical English LaTeX entry point; it builds from `sections/`.
- `main_ja.tex`: Canonical, self-contained Japanese LaTeX entry point.
- `sections/`: Section files in paper order.
- `sections_ja/`: Japanese working sections; these files are not inputs to `main_ja.tex` and may preserve versioned notation or wording.
- `refs.bib`: Bibliography file.
- `simulations/minimal_neural_field/simulate.py`: Execution authority for the current finite toy simulation.
- `simulations/minimal_neural_field/README.md`: Execution and artifact documentation for that simulation.
- `simulations/minimal_neural_field/outputs/`: Tracked figure assets used by the toy-model section; these are distribution artifacts, not equation or execution authority.
- `notes/handoff.md`: Design rules and terminology constraints.

The distributed `main.pdf` and `main_ja.pdf` are built artifacts. They do not supersede the corresponding TeX sources. The English and Japanese manuscripts are the current-facing theory sources; working Markdown, executable code, and distributed artifacts retain their separate roles.

The seven tracked PNGs are current model outputs whose pixels were reproduced by the Phase-05 audit; byte hashes differ because their encoded metadata/compression differs. This is pixel-level artifact provenance, not empirical validation. The lineage of the historical alternate GIF remains unresolved and is not used as current evidence.

## Source-local notation

Shared glyphs do not by themselves establish identity across VED, IFGT, Bio-IFGT, the toy manuscript, and the finite code. In particular:

- Bio-IFGT \(I(\mathbf r,t)\), the toy field \(I\), and the code array `I` retain source-local definitions; none is made identical to the general IFGT \(I=f(1-C)\) by notation alone.
- Bio-IFGT \(\mathbf J(\mathbf r,t)\) is distinct from VED \(J_{ij}\); the toy code does not directly integrate a `J` or `Phi` array.
- Bio-IFGT \(\rho(I,\mathbf J)\) and \(\rho(x)\) are progression-rate forms, not upstream density variables. Bio \(\sigma\), gene-related source wording, and the toy source `sigma_M` are likewise source-specific.
- External \(t\), interpretive Bio \(\tau\), upstream time variables, and the simulation loop step/`DT` are not one clock.
- \(\mathbf F=-\nabla\Phi\), the response function \(F_k\), and the state-space field \(F(x;\theta)\) are different objects.
- The paper's raw \(G=|\nabla I|\), the code's normalized gradient input, and the accumulated state `B` are different objects. The paper's symbolic \(S(z)\) also does not identify the code's two sigmoid implementations, which use different steepness constants.
- Other reused glyphs remain local as well: \(\theta\) and \(\theta_k\) are a parameter set and its thresholds; each \(D\) belongs to its stated diffusion term; sequence length \(N\) is not the toy array `N`; state label B is not the toy array `B`; spatial coordinates and state vector \(x\) have different domains. Nucleotide letters, model labels, code arrays, and upstream quantities that reuse `A`, `B`, `C`, `E`, `G`, `S`, `N`, or `k` are not identified by their spelling.

The canonical manuscript retains the conditional probability factorization. The repeated \(P_{\mathrm{life}}\) product in the Japanese working section is preserved as an unresolved source-version variant; it is not silently treated as a typo, shorthand, or equivalent formula.

## Formal and execution roles

The continuum equations in the manuscript are state/domain declarations, balance relations, and constitutive or effective relations in their stated representation. The toy equations are symbolic continuous or per-step model descriptions, while simulate.py supplies the source-specific finite update order. A compact field sequence is therefore a staged reading aid, not an assertion that every arrow is a direct code dependency or a biological cause. Model diagnostics and visualization transforms are likewise distinct from state variables; in particular, the code's normalized gradient quantity feeds B, whereas printed means, maxima, threshold fractions, contours, and RGB normalization report or display a run without defining biological observables.

The tracked toy outputs record a reproducible pattern at the reported finite horizon. They do not establish a stationary attractor, an invariant basin, general bidirectional return, biological robustness or regeneration, or membership in the proposed life region \(\Omega_{\mathrm{life}}\). The life-attractor and second-attractor terms remain conditional conceptual vocabulary rather than completed biological identifications.

## Biological and empirical scope

Bio-IFGT's fields and toy arrays are model quantities, not operationally identified biological observables. The current finite simulation supplies model-local, qualitative structural analogies; this repository does not pair them with an external biological dataset, measurement calibration, or operational variable-to-observable map. This ceiling records an open correspondence problem, not biological falsification.

Relations between Bio-IFGT, IFGT, VED, and different biological scales are proposed formal analogies or correspondences unless a typed map is stated. They are not identities, derivations, or established coarse-graining limits. In particular, Bio-local definitions do not complete the eight upstream VED/IFGT bridges concerning \(C\), \(J\), \(\rho\), distance/metric, microscopic source/\(\sigma\), \(L\)-carriers, \(\tau\), or the VED/IFGT \(\sigma\) correspondence; those remain open.

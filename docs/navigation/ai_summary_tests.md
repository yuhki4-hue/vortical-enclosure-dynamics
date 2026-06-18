# AI Summary Tests

This document records AI summary experiments and retests. Do not populate
entries with fabricated data. Add only observed tests.

## How to read this log

- **Probe.** A blank-slate model is given the repository URL (or pasted
  contents) and the six fixed questions: What is VED? / What is non-closure? /
  How does VED differ from FEP? / from Enactivism? / How does VED explain
  consciousness? / What do the Vol.4 simulations demonstrate?
- **Provenance.** Rounds 1–2 are recorded from the author's own analysis of the
  outputs (raw transcripts not stored here). Round 3 (2026-06-18) is recorded
  from observed model outputs.
- **Models.** GPT, Grok, Gemini. Gemini was additionally tested under several
  access conditions (see Access axis below).

## Experiment summary (as of 2026-06-18)

### Three diagnostic axes

The experiment separated three independent things that all look like "the model
got VED wrong":

1. **Access** — did the model actually load the repository at all?
2. **Navigation** — given access, did it read the structure correctly?
3. **Disclosure** — when it could not access the repo, did it say so visibly, or
   pass off a reconstruction as a grounded answer?

### Reader-depth taxonomy

- **Grok — deep traverser.** Reads the navigation documents and reproduces them
  closely, including a rank table verbatim. Consequence: it also propagates
  navigation-layer *errors* faithfully.
- **GPT — README + structure skimmer.** Reads the README and paper titles; does
  not descend into the navigation documents. High-leverage surface for GPT is
  the README itself.
- **Gemini — all-or-nothing by access.** Produces nothing useful when
  access-starved; produces the deepest read in the whole experiment when fed the
  full PDFs. Was never the weak reader — it was access-starved.

### Model trajectories

- **GPT:** Round 1 died at the entry layer (name → CFD). Round 3: clean
  README-level pass, CFD rejected, heavily hedged.
- **Grok:** Strong from the start; Round 3 near the ceiling of what navigation
  can deliver. Note: reproduced an erroneous rank placement from the nav layer.
- **Gemini:** Rounds 1–2 collapsed early (CFD, then complex-systems /
  biological-vortex). Round 3 showed this was an *access* artifact: starved →
  hallucination; fed README/nav → correct framing; fed PDFs → deepest read.

### Interventions applied between baseline (rounds 1–2) and retest (round 3)

- Restructured README to lead with a positive definition (single axiom:
  difference) before any negation.
- Added `generative_sequence.md` (term hierarchy).
- Added `not_just_complex_systems.md` (complex-systems / dissipative-structure
  boundary).
- Strengthened the non-closure entry (PATCH): absolute closure is unreachable
  and constitutive, not unfinished.
- 2026-06-18: corrected `generative_sequence.md` rank error (causal log moved
  from a late "rank 5 trace" to **rank 1 foundational variable** `C_ij`),
  anchoring ranks to Vol.1 variables.

### Key meta-findings

- The navigation rank error (log placed too late) was invisible to shallow
  readers, **caught only by the deep reader** (Gemini reading the PDFs), and
  **actively propagated by Grok**. Good readers amplify signage errors.
- **TOE-inflation risk is depth-correlated.** The shallow reader (GPT)
  under-claimed ("speculative"); the deepest reader (Gemini-PDF) mildly
  over-claimed ("a grand unified theory"). The more scope a reader sees, the
  more "grand unification" the frame feels.
- **Load-bearing corrections belong in the README.** Deep navigation documents
  reach only deep traversers and fully-fed models; README changes reach everyone
  who reads at all.

## Before / after matrix (round 3 status)

| Question | Baseline failure (rounds 1–2) | Round 3 status |
|---|---|---|
| What is VED? | GPT & Gemini → CFD (name adsorption) | CFD rejected by all reading models; positive generative frame held. |
| Non-closure | "closure never complete" / failure framing | Resolved for Grok & Gemini (unreachable, constitutive). **GPT residual**: English still "final completion never occurs". |
| vs FEP | "FEP = maintenance, VED = generation" oversimplified | All correct: starting-point distinction, no identity claim. |
| vs Enactivism | minor; mostly correct early | Clean across models. |
| Consciousness | log-referencing read phenomenologically; recursive-self-model drift | Correct: opening regime, stability window, SSO, log referencing; IIT/GWT/self-model rejected. |
| Vol.4 simulations | read as empirical / biological self-organization | Correct: conceptual diagrams; divergence = boundary signal; not empirical proof. |

## Per-question records

### Q1 — What is VED?

**Baseline (rounds 1–2, author-reported).**
- GPT: collapsed to CFD on the name alone (entry-layer adsorption).
- Gemini: confirmed VED = CFD, generated Navier–Stokes / lid-driven cavity /
  vorticity content before reaching theory content.
- Grok: read the README; recovered difference → gradient → flow → vortex →
  closure correctly.

**Fix applied.** Positive-first README ("What VED Is"), explicit "What VED Is
Not" (not CFD, not complex systems), `generative_sequence.md`.

**Retest (round 3, observed).**
- GPT: led with the generative sequence; "vortex/enclosure mainly conceptual
  rather than fluid-mechanical"; heavily hedged. CFD resolved.
- Grok: generative structural framework from the single axiom; reproduced the
  rank table; explicitly not CFD / not complex systems.
- Gemini (fed README/nav): rejected both CFD and complex-systems at the top;
  reproduced the rank hierarchy.
- Gemini (no access): hallucinated a self-sustaining-vortex agent from the name.
- Gemini (Deep Research): confabulated a false field from unrelated literature
  (CFD vortex-enclosure flow, ferroelectric flux-closure domains, Neppe–Close
  TDVP). Access failure, not navigation failure.

### Q2 — What is non-closure?

**Baseline.** GPT adsorbed to "closure failure / closure never complete"; Grok
leaned "asymptotic / openness".

**Fix applied.** Non-closure PATCH in `common_misreadings.md` and
`concept_traps.md`: absolute closure is unreachable, would cancel generation,
constitutive not defect.

**Retest (round 3, observed).**
- Grok: "complete closure is asymptotic and unreachable"; constitutive; would
  end generation. Resolved.
- Gemini (fed): strongest phrasing — "cannot close in order to keep existing; an
  ontological driving principle; essence, not remainder." Resolved.
- GPT: got the constitutive reason ("fully closed → static / dies"), but English
  answer still tilts to "final completion never occurs" (unfinished framing).
  **Residual** — fixable by promoting the crisp line into the README.

### Q3 — How does VED differ from FEP?

**Baseline.** Oversimplified to "FEP = maintenance vs VED = generation".

**Retest (round 3, observed).** All reading models correct: FEP centers
free-energy minimization / Markov blanket; VED begins from difference and the
generative sequence; FEP treated as a downstream biological-cognitive neighbor,
no identity claim. GPT framed it crisply ("FEP: how a system maintains itself;
VED: how self-maintaining systems arise"). Gemini (PDF) added the IFGT
distinction (information = residual un-dissipated difference, not prediction).

### Q4 — How does VED differ from Enactivism?

**Baseline.** Mostly correct early; no strong failure recorded.

**Retest (round 3, observed).** Clean across models: Enactivism begins from
embodied cognition / autopoiesis; VED begins from difference, with biology /
cognition re-situated as one layer of the generative sequence.

### Q5 — How does VED explain consciousness?

**Baseline.** Log referencing read phenomenologically (GPT); drift toward
recursive self-model (Gemini, access-starved).

**Retest (round 3, observed).**
- Grok: temporal non-closure, cross-scale log referencing, opening regime,
  externalized stopping.
- Gemini (fed): "finite non-closure stability window"; SSO; the
  fixation/dissipation middle window; IIT-Φ, GWT broadcast, and self-model
  explicitly rejected.
- Gemini (PDF): full mechanism — SSO (Δv = v_f − v_s), TCA, J_log.
- GPT: opening regime, not a generated object, temporal non-closure, log
  referencing; slight drift toward "process philosophy" framing.

### Q6 — What do the Vol.4 simulations demonstrate?

**Baseline.** Tendency to read as empirical proof; Gemini read them as
biological self-organization simulations.

**Fix applied (earlier).** `simulation_reading_guide.md`; reinforced by
`not_just_complex_systems.md`.

**Retest (round 3, observed).** All reading models correct: conceptual
simulations / dynamic diagrams; divergence reread as boundary signal;
renormalization as finite re-expression; Differential Horizon as a limit of
describability; explicitly not empirical validation and not biological
self-organization.

## Residuals identified by round 3 and repository follow-up

- **GPT non-closure residual** → promoted the crisp non-closure line
  (unreachable / not unfinished / would cancel generation / constitutive) into
  the README body, since GPT-class readers do not reliably descend into
  `common_misreadings.md`.
- **README implicit order** → added a clause placing the causal log `C_ij` as
  the rank-1 foundational variable immediately after difference, with time and
  space derived from it.
- **`concept_map.md` note** → changed the causal-log note to "rank-1 formal
  variable", matching the corrected `generative_sequence.md`.
- **Access layer (out of repo control, partially mitigable)** → still open.
  The GitHub "About" field and search-index snippets may need separate manual
  adjustment so shallow fetches surface "not CFD / derived from difference";
  search-first / non-reading agents may remain out of scope.

---

## Test Entry Template

## Question

...

### Model

...

### Summary

...

### Correct Capture

...

### Misreadings

...

### Fix Applied

...

### Retest

...

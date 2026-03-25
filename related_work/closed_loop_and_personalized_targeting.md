# Closed-loop and personalized targeting

## Current synthesis

The good neuromodulation papers are converging on a stricter standard than the field used to tolerate.

If a paper claims precision stimulation, it should specify:

1. **Target** — what circuit, tract, node, or state variable is being targeted?
2. **Readout** — what signal says the target is engaged or the patient state changed?
3. **Controller / selection logic** — how does the intervention decide where, when, or how to stimulate?
4. **Validation** — what evidence shows the stimulation changed the intended signal or circuit, not just a downstream clinical score?

## Pattern from recent papers

### Stronger pattern

- Personalized target discovery tied to symptom-linked physiology.
- Explicit biomarker or state-estimation logic.
- Evidence of target engagement beyond anatomy.
- Closed-loop or adaptive rules that are actually implemented, not just proposed.
- Willingness to show what the controller is optimizing.

### Weaker pattern

- “Network-guided” targeting that never demonstrates network engagement.
- “AI-guided” or “precision” branding with no real control logic.
- Small open-label studies with huge claims and no serious comparator.
- Reliance on average symptom change without state specificity or subgroup reasoning.

## Working judgment

Right now, invasive work is still ahead on mechanistic credibility because it can directly sense and perturb the relevant circuit. Noninvasive work is improving, especially when it uses online optimization, but it still often lacks durable state readouts and sufficiently strong behavioral endpoints.

## Useful design heuristic for future scouting

Prefer papers that make the following chain explicit:

**symptom or state -> biomarker/readout -> target selection -> stimulation -> measured circuit change -> clinical or behavioral effect**

When that chain is broken, the paper is usually weaker than the title suggests.

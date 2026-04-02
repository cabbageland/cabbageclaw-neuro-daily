# Personalized fMRI-Guided TMS Targeting the Threat Neurocircuitry in PTSD: A Randomized Clinical Trial

## Basic info

* Title: Personalized fMRI-Guided TMS Targeting the Threat Neurocircuitry in PTSD: A Randomized Clinical Trial
* Authors: S. J. H. van Rooij et al.
* Year: 2026
* Venue / source: American Journal of Psychiatry
* Link: https://pubmed.ncbi.nlm.nih.gov/41922982/
* Date surfaced: 2026-04-02
* Why selected in one sentence: It is a relatively serious psychiatric TMS trial because target personalization is tied to a symptom-relevant circuit hypothesis and checked against a mechanistic imaging endpoint.

## Quick verdict

* Highly relevant

This is one of the better recent psychiatric TMS papers because it does not just say personalized and hope nobody asks personalized to what. The target is defined by individual functional connectivity between right dorsolateral prefrontal cortex and right amygdala, and the trial tests whether that circuit engagement actually changes. The main caveat is that the cleanest between-group effect is on amygdala threat reactivity and later follow-up symptoms, not on every immediate endpoint, so this is encouraging rather than decisive.

## One-paragraph overview

The authors ran a double-blind randomized trial in fifty adults with PTSD symptoms, delivering ten twice-daily sessions of active or sham one-hertz TMS to a right dorsolateral prefrontal target chosen from functional MRI as the cortical site most strongly connected to the right amygdala. Their primary mechanistic endpoint was right amygdala threat reactivity on functional MRI, with skin conductance during trauma recall as a second physiological endpoint. Active TMS reduced amygdala threat reactivity relative to sham, but did not significantly change skin-conductance reactivity. Immediate symptom reductions occurred across both groups, while follow-up between three and six months favored active treatment for hyperarousal and total PTSD symptoms. The useful read is that this is a targeting paper with some actual circuit evidence behind it, but not yet a fully clean efficacy story.

## Model definition

### Inputs
Subject-specific functional MRI used to identify the right dorsolateral prefrontal cortical site with the strongest functional connection to the right amygdala, plus clinical PTSD symptoms and physiological measurements collected before and after treatment.

### Outputs
A personalized cortical stimulation target for each participant, post-treatment changes in right amygdala threat reactivity, skin-conductance reactivity during trauma recall, and symptom change on the PTSD Checklist for DSM-5.

### Training objective (loss)
There is no trainable predictive model described in the accessible abstract. The key learned element is the individualized target selection based on functional connectivity rather than a supervised model optimized with an explicit loss.

### Architecture / parameterization
A personalized target-selection pipeline using functional MRI connectivity between dorsolateral prefrontal cortex and amygdala, embedded inside a double-blind sham-controlled TMS clinical trial.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
PTSD TMS results have been inconsistent, and one plausible reason is that cortical targets are chosen too crudely. The paper tries to determine whether circuit-guided individual targeting can improve both mechanistic engagement and clinical outcome.

### 2. What is the method?
Randomize participants with PTSD to active or sham low-frequency TMS, but choose each active target using that participant’s functional MRI connectivity to the right amygdala.

### 3. What is the method motivation?
If PTSD symptoms are partly maintained by dysregulated threat circuitry, then a cortical stimulation site should be chosen for its relationship to that circuitry rather than by scalp heuristics or one-size-fits-all coordinates.

### 4. What data does it use?
The abstract reports fifty adults with PTSD symptoms in a double-blind clinical trial. The paper uses pre- and post-treatment functional MRI, skin conductance during trauma recall, and PTSD symptom scales with later follow-up between three and six months.

### 5. How is it evaluated?
By comparing active and sham groups on right amygdala threat reactivity, skin conductance reactivity, hyperarousal, and total PTSD symptoms across treatment and follow-up.

### 6. What are the main results?
Active TMS significantly reduced right amygdala threat reactivity relative to sham. Skin conductance did not show a significant treatment effect. Immediate post-treatment symptom reductions appeared across groups without significant between-group separation, but active treatment showed superior reductions in hyperarousal and total PTSD symptoms at follow-up.

### 7. What is actually novel?
The main novelty is not simply that functional MRI is used somewhere in the workflow. It is that the personalization claim is anchored to a threat-circuit hypothesis, and the trial directly measures whether the hypothesized neural target engagement occurred.

### 8. What are the strengths?
- Stronger targeting logic than generic dorsolateral prefrontal cortex TMS trials.
- Randomized, sham-controlled, double-blind design.
- Includes a mechanistic neural endpoint rather than symptoms alone.
- Longitudinal follow-up is more informative than immediate post-treatment measurement alone.

### 9. What are the weaknesses, limitations, or red flags?
- The abstract leaves many practical details unspecified at inspection level.
- Skin conductance, one of the primary physiological endpoints, did not show the hoped-for treatment effect.
- Symptom separation seems clearer at follow-up than immediately after treatment, which is interesting but less tidy.
- Fifty participants is respectable for this kind of trial but still not enough to settle personalization claims broadly.
- Functional connectivity-defined targeting is still only a partial proxy for causal circuit control.

### 10. What challenges or open problems remain?
Replication, parameter sensitivity, identifying which PTSD subgroups benefit most, and determining whether functional connectivity alone is sufficient for target definition or should be combined with structural and behavioral information.

### 11. What future work naturally follows?
Larger multicenter trials, deeper analysis of responder heterogeneity, comparison against non-personalized target strategies, and efforts to link target engagement to symptom dimensions more granularly than total PTSD severity.

### 12. Why does this matter for cabbageland?
Because it is a cleaner example of circuit-guided neuromodulation than most psychiatric TMS papers. The study at least tries to bind together target selection, mechanistic readout, and delayed clinical effect instead of waving vaguely at precision psychiatry.

### 13. What ideas are steal-worthy?
- If you claim personalized targeting, define the target from an explicit symptom-relevant circuit.
- Pair symptom outcomes with a mechanistic endpoint that should move if the target logic is real.
- Treat delayed follow-up effects as important rather than assuming immediate symptom movement is the only meaningful timescale.
- Compare neural endpoint success and clinical endpoint messiness instead of forcing them into a fake single-story win.

### 14. Final decision
Keep. This is not definitive proof that personalized threat-circuit TMS works, but it is a worthwhile benchmark for how psychiatric neuromodulation trials should tie targeting rhetoric to measurable circuit engagement.
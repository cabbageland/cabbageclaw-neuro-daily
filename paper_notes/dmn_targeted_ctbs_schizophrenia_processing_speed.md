# Accelerated DMN-targeted cTBS improves processing speed deficits in schizophrenia

## Basic info

* Title: Accelerated DMN-targeted cTBS improves processing speed deficits in schizophrenia
* Authors: Jillian G. Connolly, Sophia H. Blyth, Gulcan Yildiz, Baxter P. Rogers, Simon Vandekar, Mark A. Halko, Roscoe O. Brady Jr., Heather B. Ward
* Year: 2026
* Venue / source: Molecular Psychiatry update; detailed inspection through the PMC-hosted medRxiv preprint
* Link: https://doi.org/10.1038/s41380-026-03798-8
* Date surfaced: 2026-08-26
* Why selected in one sentence: It is one of the cleaner recent papers on personalized network targeting because it explicitly shows that a single session is not enough, while a multi-session DMN-targeted cTBS protocol can move schizophrenia-related processing-speed measures and associated network connectivity.

## Quick verdict

* Highly relevant

This is a real keep, but not a victory lap. The useful move is that the paper does not stop at a single-session connectivity wiggle and declare mechanism solved. It runs a sham-controlled single-session study that does not improve processing speed, then shows that a five-session accelerated protocol aimed at the same individualized default-mode target does. The main caution is that the multi-session arm has no sham control and the entire detailed read comes from the accessible preprint version rather than the final journal full text.

## One-paragraph overview

The paper links two studies around the same personalized default-mode-network target in the left posterior inferior parietal lobule. In the first, ten schizophrenia participants completed a randomized crossover comparison of single-session intermittent theta-burst stimulation, continuous theta-burst stimulation, and sham, with pre/post resting-state fMRI and processing-speed testing. That study found no cognitive gain from one session. In the second, seventeen schizophrenia participants and twelve non-psychosis controls received five accelerated cTBS sessions in one day, again with pre/post resting-state fMRI and processing-speed assessment roughly a week apart. In the schizophrenia group, composite processing speed improved, digit-symbol coding improved more clearly than the other subtests, multi-session cTBS outperformed the single-session cTBS change profile, and greater reduction in DMN connectivity tracked greater cognitive improvement. The useful lesson is not that DMN targeting is already clinically settled. It is that personalized network targeting starts to look interesting only once the intervention dose is large enough to change behavior rather than only connectivity.

## Model definition

This is not a learned prediction paper. The central model-like object is the personalized network-targeting and connectivity-analysis pipeline.

### Inputs
Pre-treatment resting-state fMRI used to define an individualized left posterior inferior parietal default-mode target, TMS condition or session schedule, pre/post processing-speed task scores, and pre/post default-mode-network functional connectivity values derived from target-to-network correlations.

### Outputs
Individualized stimulation targets, pre/post composite processing-speed T-scores and subtest scores, pre/post DMN connectivity measures, and correlations between connectivity change, age, and cognitive change.

### Training objective (loss)
There is no trainable clinical predictor or controller in the paper. The accessible full text shows rule-based target selection from resting-state connectivity and downstream statistical comparisons of pre/post cognitive and network change.

### Architecture / parameterization
The intervention architecture is personalized network-targeted theta-burst stimulation. The target is a participant-specific left posterior inferior parietal node within the default mode network. Study 1 uses single-session iTBS, cTBS, and sham in randomized crossover form. Study 2 uses five accelerated cTBS sessions in one day with a 30-minute intersession interval.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
There are still no approved treatments for the cognitive impairment that drives much of schizophrenia-related disability. The paper tries to test whether a personalized default-mode-network target can improve the most impaired cognitive domain, processing speed, rather than only nudge a network metric.

### 2. What is the method?
The method is a two-study design. First, run a sham-controlled single-session crossover study in schizophrenia to test whether one dose of DMN-targeted TMS changes processing speed. Second, run an accelerated five-session cTBS intervention aimed at the same individualized DMN target in schizophrenia and non-psychosis controls, then relate pre/post cognitive change to pre/post DMN connectivity change.

### 3. What is the method motivation?
The motivation is good and unusually explicit. If schizophrenia-related processing-speed deficits are tied to DMN hyperconnectivity, then a network-targeted intervention should reduce that connectivity and improve cognition. But the authors also test whether intervention dose matters, instead of pretending that one stimulation session should already look therapeutic.

### 4. What data does it use?
The single-session study analyzed ten schizophrenia participants who completed single-session iTBS, cTBS, and sham visits with resting-state fMRI and BACS digit-symbol testing before and after each session. The accelerated study included twenty-nine total participants, seventeen with schizophrenia or schizoaffective disorder and twelve non-psychosis controls, with pre/post resting-state fMRI and a MATRICS processing-speed composite built from digit symbol coding, animal fluency, and Trail Making Test Part A.

### 5. How is it evaluated?
The paper evaluates whether single-session and multi-session stimulation change processing-speed scores, whether multi-session change exceeds the single-session cTBS change profile, and whether change in DMN connectivity from the personalized target tracks cognitive improvement. It also tests whether age moderates the cognitive response.

### 6. What are the main results?
Single-session stimulation did not improve processing speed. The accelerated multi-session cTBS study did improve the schizophrenia-group composite processing-speed score, with the paper reporting `p = 0.0124`, and digit-symbol coding improved more clearly than the other two subtests. Multi-session cTBS also outperformed the single-session cTBS change profile, with the paper reporting `p = 0.0148`. In schizophrenia participants, greater reduction in DMN connectivity was associated with greater processing-speed improvement, reported as `p = 0.021`. Age mattered too: younger schizophrenia participants showed larger processing-speed gains, with the paper reporting `p = 0.006`.

### 7. What is actually novel?
The novelty is not just personalized targeting. There are already plenty of papers selling personalization as geometry theater. The stronger novelty is the explicit single-session versus multi-session comparison around a schizophrenia cognition target, plus the choice to target a participant-specific left posterior inferior parietal DMN node rather than staying inside the usual depression-style left DLPFC obsession.

### 8. What are the strengths?
- It asks a sharper question than most precision-TMS papers by separating one-session target engagement from multi-session cognitive effect.
- The target-selection logic is explicit and network-based rather than scalp-rule folklore.
- The paper combines cognition with connectivity instead of reporting only one or the other.
- The accelerated study includes a non-psychosis comparison group rather than only a patient-only pre/post design.
- The result is clinically more interesting because it targets cognitive disability rather than only symptom score movement.

### 9. What are the weaknesses, limitations, or red flags?
- The accelerated multi-session study has no sham control, which is the biggest problem and the first thing any skeptical reader should attack.
- Sample sizes are modest: ten analyzed participants in the single-session study and twenty-nine total in the accelerated study.
- The detailed inspection in this run comes from the accessible PMC-hosted medRxiv preprint, not the final Molecular Psychiatry full text.
- The pre/post interval in the accelerated study is about a week, which leaves some room for retest or nonspecific effects even though the single-session null result helps a bit.
- The behavioral gain is mostly a processing-speed story, not broad cognitive rescue.

### 10. What challenges or open problems remain?
The field still needs a sham-controlled multi-session replication, durability data beyond the immediate post window, and a direct comparison against other plausible targets. It also remains unclear whether DMN connectivity reduction is the active mechanism or just a correlated marker of a broader state shift.

### 11. What future work naturally follows?
Run a larger sham-controlled accelerated trial, test whether more days or more sessions improve durability, compare left posterior inferior parietal DMN targeting against other network nodes, and examine whether pretreatment age, illness duration, or baseline DMN hyperconnectivity can stratify who benefits.

### 12. Why does this matter for cabbageland?
Because it sharpens intervention logic. The paper says a personalized network target is not enough by itself. What matters is whether the dose is sufficient to move cognition, whether network change tracks that movement, and whether subgroup structure like age changes the result.

### 13. What ideas are steal-worthy?
- Treat single-session target engagement and multi-session behavioral change as different claims that need separate tests.
- Use individualized left posterior parietal DMN targeting for cognition-focused interventions instead of defaulting automatically to frontal mood targets.
- Track whether connectivity reduction is proportional to behavioral gain rather than only reporting group means.
- Build age or plasticity stratification into network-targeted neuromodulation studies from the start.

### 14. Final decision
Preserve. This is not decisive proof that DMN-targeted cTBS solves schizophrenia-related cognitive impairment, but it is a much more useful paper than the usual personalization rhetoric because it shows that one session is not enough, multi-session dose matters, and the network-change story stays tied to a concrete behavioral outcome.

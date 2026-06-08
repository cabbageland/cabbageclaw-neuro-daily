# Selective disruption of sleep slow-waves increases motor cortical excitability in major depressive disorder

## Basic info

* Title: Selective disruption of sleep slow-waves increases motor cortical excitability in major depressive disorder
* Authors: Jennifer R Goldschmied, Santiago Lopez Pereyra, Desmond J Oathes
* Year: 2026
* Venue / source: Clinical Neurophysiology
* Link: https://doi.org/10.1016/j.clinph.2026.2111902
* Date surfaced: 2026-06-08
* Why selected in one sentence: It turns sleep from background hygiene into an experimentally perturbed plasticity-state variable and shows that the same slow-wave disruption pushes next-morning cortical excitability in opposite directions in depression versus healthy controls.

## Quick verdict

* Highly relevant

This is a real keep because it sharpens state-aware stimulation logic without pretending to be a finished treatment paper. The useful point is not merely that sleep matters. The useful point is that experimentally disrupting slow waves changes next-morning motor-cortex excitability in major depressive disorder in a direction opposite to healthy controls, which is exactly the sort of state-dependent leverage a serious neuromodulation stack should care about. The main caveat is access: this note is based on the PubMed abstract plus publisher-side methods, results, and limitations excerpts surfaced through indexed ScienceDirect text rather than a clean full-PDF read.

## One-paragraph overview

The paper asks whether selectively disrupting slow-wave sleep changes next-morning cortical excitability differently in people with major depressive disorder than in healthy controls. Participants completed two overnight lab sessions in counterbalanced order: a baseline night and a slow-wave-disruption night using auditory tones to interrupt visually detected slow waves, followed the next morning by single-pulse and paired-pulse transcranial magnetic stimulation of motor cortex. The key result is that slow-wave disruption increased raw motor-evoked-potential amplitudes in major depressive disorder but tended to decrease them in healthy controls. Relative intracortical facilitation and inhibition ratios changed much less clearly, so the paper's best read is not "we solved depression physiology." The better read is that overnight sleep state may directly tune the plasticity or excitability regime in which stimulation lands.

## Model definition

This paper does not present a trainable predictive model. It uses an experimental sleep perturbation and TMS-derived physiological readouts to probe cortical-state regulation.

### Inputs
Participant group status (major depressive disorder versus healthy control), overnight condition (baseline versus slow-wave disruption), sleep-stage measurements from laboratory EEG, and next-morning single-pulse and paired-pulse motor-cortex TMS measurements.

### Outputs
Changes in motor-evoked-potential amplitudes, resting motor-threshold-related cortical excitability readouts, and paired-pulse intracortical facilitation and inhibition patterns after baseline versus slow-wave-disruption nights.

### Training objective (loss)
There is no learnable model or explicit optimization loss. The core analytic question is whether the overnight manipulation changes next-morning cortical excitability differently across groups.

### Architecture / parameterization
A within-subject counterbalanced sleep-manipulation experiment with physiological readout via single-pulse and paired-pulse TMS over motor cortex.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Whether depression-related excitatory and inhibitory dysregulation can be probed by perturbing sleep-dependent synaptic downscaling and then reading out next-morning cortical excitability.

### 2. What is the method?
Run two overnight laboratory sessions per participant, one baseline and one slow-wave-disruption night, reduce slow waves using auditory stimulation during sleep, and measure next-morning motor-cortex excitability with single-pulse and paired-pulse TMS.

### 3. What is the method motivation?
If slow waves help downscale excitatory synaptic strength overnight, then disrupting them should alter the excitability state in which morning stimulation lands. If depression has abnormal homeostatic plasticity, the perturbation should not affect patients and controls the same way.

### 4. What data does it use?
Thirty-seven adults completed the main protocol: thirteen healthy controls and twenty-four participants with major depressive disorder. The publisher-side excerpt shows some sleep tables with twenty-three major-depression participants, suggesting at least one participant had incomplete data for parts of the analysis. Each participant completed two non-consecutive overnight lab sessions with sleep EEG plus next-morning TMS measures.

### 5. How is it evaluated?
The study checks whether slow-wave disruption actually reduces stage-three sleep, then compares baseline-versus-disruption changes in raw motor-evoked potentials and paired-pulse intracortical facilitation and inhibition patterns across healthy-control and major-depression groups.

### 6. What are the main results?
- Slow-wave disruption reliably reduced stage-three sleep in both groups, by about thirty-three percent in healthy controls and about twenty-six percent in major depressive disorder.
- In major depressive disorder, slow-wave disruption increased motor-evoked-potential amplitudes during both single-pulse and paired-pulse TMS.
- Healthy controls showed the opposite broad pattern, with decreased excitability after slow-wave disruption.
- Both groups showed baseline intracortical facilitation and inhibition.
- After slow-wave disruption, inhibitory effects weakened in healthy controls but were preserved in major depressive disorder.
- Relative intracortical-facilitation and inhibition ratios did not shift enough to support a clean "this is a GABA story" interpretation, so the authors point instead toward a broader AMPA-mediated excitability account.

### 7. What is actually novel?
The novelty is not merely linking sleep and depression. It is experimentally pushing slow-wave sleep and then reading out a next-morning neuromodulation-relevant physiological state, with a clear group-by-condition divergence.

### 8. What are the strengths?
- Within-subject counterbalanced design is much better than a one-shot group comparison.
- The slow-wave-disruption manipulation appears to have worked cleanly in both groups.
- TMS gives a direct physiological readout instead of relying only on subjective symptoms.
- The paper asks a mechanistic state question that could actually matter for stimulation timing and response prediction.

### 9. What are the weaknesses, limitations, or red flags?
- This is still motor-cortex physiology, not a therapeutic intervention study.
- Motor-evoked potentials are a proxy for corticospinal excitability rather than a pure measure of cortical synaptic state.
- The final analyzed sample was smaller than planned and appears to lose at least one major-depression participant in some analyses.
- The major-depression sample was only mild to moderately depressed, which may blunt clinical generalization.
- I did not get a clean full-body article read; this note relies on the abstract plus indexed publisher excerpts for methods, results, and limitations.

### 10. What challenges or open problems remain?
The big open question is whether sleep-state manipulation or sleep-state monitoring actually improves response to therapeutic stimulation in depression. Another is whether the same logic holds outside motor cortex and outside this relatively mild major-depression cohort.

### 11. What future work naturally follows?
Combine overnight sleep-state measures with next-day therapeutic TMS, test whether sleep-derived state markers add value to EEG or connectivity biomarkers, use region-specific readouts beyond motor cortex, and prospectively ask whether poor-sleep or low-slow-wave nights should change stimulation scheduling or dosing.

### 12. Why does this matter for cabbageland?
Because it says the relevant brain state may begin before the stimulation session starts. If sleep architecture changes whether the cortex wakes up in a more or less excitable regime, then state-aware neuromodulation should not pretend the only useful state variable is the EEG recorded in the minute before the pulse.

### 13. What ideas are steal-worthy?
- Treat overnight sleep structure as a pre-stimulation state prior, not just a nuisance covariate.
- Distinguish broad excitability shifts from specific inhibitory-circuit claims instead of collapsing everything into one neurotransmitter story.
- Use mechanistic perturbations that change plasticity state before testing stimulation-response hypotheses.
- Ask whether scheduling, gating, or dosing neuromodulation around sleep-derived state could reduce response variability.

### 14. Final decision
Preserve. This is not a clinical win paper, but it sharpens a genuinely important idea: precision stimulation may need to know what kind of cortex showed up that morning, and sleep is one plausible way that state gets set.

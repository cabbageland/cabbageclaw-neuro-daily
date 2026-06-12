# Loss of regional theta differentiation in TMS-EEG response marks network dysfunction in psychosis risk

## Basic info

* Title: Loss of regional theta differentiation in TMS-EEG response marks network dysfunction in psychosis risk
* Authors: Nadja Zimmermann, Matthias Liebrand, Chantal Michel, Miriam Stueble, Arndt-Lukas Klaassen, Eva Burkhardt, Roland Wiest, Michael Kaess, Jochen Kindler, Yosuke Morishima
* Year: 2026
* Venue / source: Translational Psychiatry
* Link: https://doi.org/10.1038/s41398-026-04030-5
* Date surfaced: 2026-06-12
* Why selected in one sentence: It turns psychosis-risk dysconnectivity into a direct perturbational fingerprint by showing that clinical high-risk participants lose site-specific theta responses to TMS.

## Quick verdict

* Highly relevant

This is a useful biomarker paper because it does something more informative than another resting-state correlation study. Healthy controls showed a clear site-specific theta hierarchy after stimulation, while the CHR-P group lost that differentiation because theta responses flattened upward across regions. The main caveat is that the compensation story is still interpretive, not causal, and the first-episode psychosis sample is too small to anchor a clean developmental progression claim.

## One-paragraph overview

The paper applies single-pulse TMS with concurrent EEG to three frontoparietal targets in people at clinical high risk for psychosis and matched healthy controls. The core result is not a simple mean reduction. Instead, healthy participants show a differentiated theta pattern by stimulation site, with the largest theta response after left dorsolateral prefrontal stimulation and smaller responses after left posterior parietal and dorsomedial prefrontal stimulation. CHR-P participants lose that hierarchy because theta responses are elevated into a flatter pattern across sites. Gamma differences are not convincing. Higher theta in certain sites tracks less severe unusual thought content, avolition, reduced emotional experience, and role deterioration, which the authors interpret as a possible compensatory response to early network dysfunction.

## Model definition

The paper does not build a predictive decoder or adaptive controller. It is mainly a perturbation-analysis study.

### Inputs
TMS-evoked EEG recordings after stimulation of left dorsolateral prefrontal cortex, left posterior parietal cortex, and dorsomedial prefrontal cortex; participant group labels; psychopathology measures including SIPS; and neurocognitive and functioning measures.

### Outputs
Theta and gamma power estimates over predefined time-frequency windows, permutation-derived site-differentiation maps, linear mixed-model coefficients, and correlations between oscillatory responses and symptoms or functioning.

### Training objective (loss)
There is no central trainable predictive model with a single optimization loss. The signal processing stack uses Morlet wavelet decomposition to estimate time-frequency power, and the inferential layer relies on permutation tests and linear mixed models rather than a learned clinical prediction objective.

### Architecture / parameterization
A concurrent TMS-EEG analysis pipeline with Morlet wavelet time-frequency decomposition, predefined theta and gamma windows, cluster-corrected permutation testing, and linear mixed-effects modeling across group and stimulation site.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Psychosis-risk states are often described as dysconnectivity syndromes, but those claims are usually based on passive measurements. This paper asks whether direct perturbation reveals an early loss of region-specific functional specialization.

### 2. What is the method?
Single-pulse TMS was delivered at 110 percent active motor threshold to left dorsolateral prefrontal cortex, left posterior parietal cortex, and dorsomedial prefrontal cortex while EEG was recorded. The authors analyzed theta and gamma time-frequency responses, tested whether responses differed by site and group, and related those responses to symptoms and cognition.

### 3. What is the method motivation?
If psychosis risk truly involves frontoparietal network dysfunction, then directly perturbing different nodes should not produce the same response pattern as in healthy participants. TMS-EEG gives a way to test that claim rather than infer it indirectly.

### 4. What data does it use?
Fifty-eight healthy controls and forty-four CHR-P participants entered the main analyses after exclusions for data quality. There was also a very small first-episode psychosis group described mainly in supplementary material, not strong enough for primary inference.

### 5. How is it evaluated?
The main evaluation is whether theta and gamma responses differ across stimulation sites within each group, whether group-by-site interactions appear in mixed models, and whether oscillatory responses correlate with positive symptoms, negative symptoms, and functioning.

### 6. What are the main results?
Healthy controls showed a differentiated theta response by stimulation site, strongest at left dorsolateral prefrontal cortex and smaller at left posterior parietal and dorsomedial prefrontal cortex. CHR-P participants lost that differentiation, largely because theta responses at parietal and dorsomedial sites were elevated. Mixed models supported higher theta in CHR-P at DMPFC and trend-level higher theta at lPPC. Theta responses correlated inversely with unusual thought content, avolition, reduced emotional experience, and deterioration in role functioning. Gamma findings were largely null.

### 7. What is actually novel?
The novelty is applying multi-site TMS-EEG in CHR-P and turning psychosis-risk circuitry into a site-specific perturbation problem. The key claim is not just abnormal theta, but loss of regional theta differentiation.

### 8. What are the strengths?
- Direct perturbational readout instead of purely passive dysconnectivity claims.
- Multiple stimulation sites make the loss-of-differentiation argument much stronger.
- Reasonable main-sample sizes for a TMS-EEG study.
- Symptom correlations are directionally interpretable rather than arbitrary.
- The induced-activity analyses help argue the effects are not only phase-locked auditory artifacts.

### 9. What are the weaknesses, limitations, or red flags?
- The compensatory interpretation is plausible but not proven.
- The first-episode psychosis comparison is too underpowered to support a staged progression story.
- TMS-EEG artifact handling is always a vulnerability, especially with interpolation around the pulse.
- Only three cortical sites were tested, so the functional-fingerprint claim is still partial.
- No longitudinal conversion analysis shows whether this marker predicts who will transition to psychosis.

### 10. What challenges or open problems remain?
The big open question is whether this flattened theta fingerprint predicts later conversion, treatment response, or specific cognitive trajectories. It is also unclear how stable the marker is over time and how sensitive it is to medication, arousal, or comorbid mood states.

### 11. What future work naturally follows?
Follow CHR-P participants longitudinally, test whether the theta fingerprint normalizes or worsens with progression, integrate TMS-EEG with structural connectivity or symptoms at the individual level, and examine whether stimulation can deliberately reshape the flattened response pattern.

### 12. Why does this matter for cabbageland?
Because it shows how a biomarker paper can earn the word mechanism a little more honestly. Instead of claiming diffuse dysconnectivity, it asks whether specific perturbation fingerprints survive across cortical sites.

### 13. What ideas are steal-worthy?
- Use loss of site-specific perturbation structure as a disease marker, not just mean power changes.
- Treat theta as a readout of long-range functional specialization under perturbation rather than only a resting-state oscillation.
- Build biomarker logic around direct perturbation plus symptom association, not passive connectivity alone.
- Separate null gamma findings from positive theta findings instead of forcing a full-band story.

### 14. Final decision
Keep as a strong perturbational biomarker note. It does not yet prove longitudinal clinical value, but it gives a much better mechanistic starting point for psychosis-risk circuitry than most passive-network papers.

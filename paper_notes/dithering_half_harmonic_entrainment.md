# Dithering suppresses half-harmonic neural synchronisation to photic stimulation in humans

## Basic info

* Title: Dithering suppresses half-harmonic neural synchronisation to photic stimulation in humans
* Authors: Benoit Duchet et al.
* Year: 2026
* Venue / source: Brain Stimulation
* Link: https://pubmed.ncbi.nlm.nih.gov/42049166/
* Date surfaced: 2026-05-04
* Why selected in one sentence: It takes a control-theoretic nuisance in rhythmic stimulation, unwanted harmonic entrainment, and tests a concrete mitigation strategy in humans rather than leaving it as a modeling curiosity.

## Quick verdict

* Highly relevant

This is a compact but conceptually important methods paper. The useful idea is not the specific photic-stimulation implementation. It is the broader claim that temporal regularity itself is a stimulation-control variable, and that slight jitter can suppress unwanted half-harmonic locking without just reducing delivered energy. The obvious limitation is that transfer from photic flicker in healthy humans to electrical or magnetic therapeutic stimulation is still inferential.

## One-paragraph overview

The paper tests whether slight temporal jitter, called dithering, can preserve desired entrainment while reducing unwanted half-harmonic synchronisation during rhythmic stimulation. Healthy participants underwent EEG recording during periodic photic stimulation, dithered photic stimulation, reduced-strength periodic stimulation, and control conditions. The authors quantify synchronisation using spectral power and phase-locking value, then compare how the different stimulation schedules shape activity at the stimulation frequency and at the half-harmonic. Their core result is that dithering suppresses half-harmonic synchronisation more strongly than it suppresses target-frequency synchronisation, consistent with earlier theoretical predictions. The practical implication is that stimulation waveform timing may need to be engineered not only to create desired locking but also to avoid pathological or unwanted subharmonic structure.

## Model definition

This paper does not center on a learned predictive model, but it does use a mechanistic oscillator model to interpret the observed responses.

### Inputs
Stimulation timing condition, including periodic versus dithered photic flicker, along with EEG recordings from healthy participants.

### Outputs
Measured synchronisation strength at stimulation and half-harmonic frequencies, quantified through spectral power and phase-locking value, plus qualitative model fit to observed response patterns.

### Training objective (loss)
The accessible abstract does not specify a fitted loss. The modeling component is described as synthetic-data and minimal-oscillator analysis used to compare explanations for the observed half-harmonic responses.

### Architecture / parameterization
Experimental stimulation comparison plus a minimal oscillator model intended to distinguish genuine half-harmonic entrainment from mere superposition of evoked responses.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Rhythmic stimulation can accidentally entrain activity at subharmonics or superharmonics, not only at the intended frequency. That can be a real control problem if those unintended modes are biologically undesirable.

### 2. What is the method?

Compare periodic, dithered, reduced-strength, and control photic stimulation in healthy humans while measuring EEG synchronisation metrics, then use synthetic-data and oscillator modeling to interpret the pattern.

### 3. What is the method motivation?

Prior mathematical work suggested that slight timing jitter might preserve desired entrainment while disrupting unwanted harmonic locking. This study asks whether that idea actually works in humans.

### 4. What data does it use?

Human EEG recordings collected during photic stimulation under multiple timing conditions in healthy adults.

### 5. How is it evaluated?

By comparing spectral power and phase-locking at the stimulation frequency and the half-harmonic across conditions, and by checking whether the response pattern is better explained by entrainment dynamics than by simple evoked-response summation.

### 6. What are the main results?

Dithering suppresses half-harmonic synchronisation relative to perfectly periodic flicker, while affecting synchronisation at the stimulation frequency less strongly. Reduced-strength periodic stimulation shows a similar selective effect. Modeling supports the interpretation that the half-harmonic response reflects real half-harmonic entrainment more than simple superposed evoked responses.

### 7. What is actually novel?

The novelty is translating a control-theoretic idea about dithered stimulation into a human experiment and tying the result to a mechanistic oscillator interpretation rather than leaving it as a descriptive EEG quirk.

### 8. What are the strengths?

- Tests a concrete intervention on stimulation timing rather than only describing an artifact.
- Bridges theory and human experiment.
- Focuses on a failure mode that could matter across many entrainment-style interventions.
- The result is conceptually transferable beyond photic stimulation.

### 9. What are the weaknesses, limitations, or red flags?

- Healthy-participant photic stimulation is not the same regime as therapeutic electrical or magnetic stimulation.
- Abstract-level access leaves sample size and parameter robustness unclear.
- The desired-versus-undesired entrainment distinction is context dependent, so the design rules may not transfer cleanly.

### 10. What challenges or open problems remain?

The main open problem is whether dithering helps in clinically relevant stimulation modalities, brain targets, and symptom-linked rhythms, and whether it can be folded into adaptive controllers without blunting desired effects.

### 11. What future work naturally follows?

Apply the same logic to transcranial alternating current stimulation, temporal interference, transcranial magnetic stimulation, and deep brain stimulation; test different jitter regimes; and ask whether dithering improves symptom-linked outcomes or only spectral cleanliness.

### 12. Why does this matter for cabbageland?

Because it sharpens a good control instinct: stimulation timing regularity is not neutral. If a controller ignores the harmonic structure it induces, it may create exactly the wrong dynamics.

### 13. What ideas are steal-worthy?

- Treat unwanted harmonic entrainment as a first-class design constraint.
- Use mild temporal irregularity as a control knob rather than assuming periodicity is always optimal.
- Pair theory-led waveform design with human validation early.
- Distinguish entrainment from evoked-response summation instead of collapsing them.

### 14. Final decision

Keep as a highly relevant methods-and-control note. It is not a therapy paper, but it improves intervention logic in a way many therapy papers do not.
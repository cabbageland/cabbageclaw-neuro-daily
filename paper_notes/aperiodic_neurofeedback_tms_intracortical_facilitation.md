# Closed-loop control of sensorimotor aperiodic neural dynamics can manipulate excitatory-inhibitory balance in humans

## Basic info

* Title: Closed-loop control of sensorimotor aperiodic neural dynamics can manipulate excitatory-inhibitory balance in humans
* Authors: Satoshi Mutsuda; Seitaro Iwama; Junichi Ushiba
* Year: 2026
* Venue / source: bioRxiv preprint, version 1, posted November 24, 2026; not peer reviewed
* Link: https://doi.org/10.64898/2026.11.09.765129
* Date surfaced: 2026-11-26
* Why selected in one sentence: It couples voluntary aperiodic EEG state modulation with state-triggered intracortical TMS probes, while showing why a state contrast must not be mistaken for a continuous E/I decoder.

## Quick verdict

* Highly relevant

Preserve as a physiological state-conditioning assay, not as proof of a calibrated E/I biomarker or an effective treatment. Steeper-feedback states have lower intracortical facilitation than flatter-feedback states, but continuous trial-wise exponent does not predict that response. Full-text inspection covered the main PDF's Results, Methods, Discussion, and Figures 1–5 captions; supplements, raw figure images, data, and code were not audited.

## One-paragraph overview

Healthy adults used visual feedback to move the sensorimotor EEG aperiodic exponent toward flatter or steeper spectra. Reaching a 15% change triggered TMS at the left M1 hand hotspot; single-pulse motor-evoked potentials (MEPs), short-interval intracortical inhibition (SICI), and intracortical facilitation (ICF) supplied physiological readouts. Twenty-nine participants contributed analyzed data. The steeper state had lower normalized ICF than the flatter state and rest, whereas single-pulse excitability and SICI changed with feedback engagement rather than direction. Periodic theta/alpha/beta contrasts were nonsignificant after aperiodic correction. Crucially, trial-level spectral exponent did not predict ICF. The experiment therefore links an experimentally selected feedback state to an intracortical response, without uniquely identifying synaptic E/I, validating a single-trial decoder, or testing therapeutic stimulation.

## Model definition

### Inputs

- **Online estimator:** 64-channel EEG acquisition, using a small C3-centered Laplacian for the feedback signal. Data are downsampled from 1,000 to 200 Hz, band-pass filtered at 1–70 Hz, and notch-filtered at 50 Hz. Each FFT uses a two-second segment ending 200 ms before the update; the ten latest spectra are averaged.
- **Reference/state rule:** The preceding five-second resting segment supplies a screened reference exponent. Relative change is `100 × (χtask − χrest) / χrest`; the instructed direction determines the feedback sign.
- **Exploratory response models:** Trial-wise exponent, periodic alpha and beta peak power, participant identity, and MEP-derived outcomes. A separate model uses feedback state as the predictor. Offset is excluded from multivariable models because of strong collinearity with exponent.

### Outputs

- **Estimator:** Aperiodic exponent and offset plus periodic peaks; the online control variable is exponent change, not an E/I probability or concentration.
- **Loop:** Visual circle size and a deterministic TMS trigger at a 15% directional change. If no hit occurs, a fallback pulse occurs at a randomly selected 11–12 seconds after trial onset; fallback trials are excluded from the main EEG/MEP analyses.
- **Statistical models:** Expected single-pulse MEP amplitude or conditioned/unconditioned MEP ratios. These are explanatory fits, not demonstrated out-of-sample physiological predictions.

### Training objective (loss)

No end-to-end E/I decoder, learned stimulation policy, or therapeutic reward is trained. Spectral parameterization uses specparam with fixed aperiodic mode over 2–40 Hz and modeled periodic peaks; the main paper does not state its numerical fitting loss, so no specific loss is inferred here. The response models are Gamma-distribution GLMMs with log link, fitted by maximum pseudo-likelihood. Their target is the observed positive MEP-derived response, not directly measured synaptic excitation or inhibition.

### Architecture / parameterization

A modular signal-processing/parametric-estimation/threshold-trigger stack, with a human acting through visual neurofeedback. Online estimates update every 100 ms but integrate roughly 2.9 seconds of EEG and end 200 ms before the update: update cadence is not effective temporal resolution. Specparam uses peak-width limits of 0.5–12 Hz, no upper peak-count limit, minimum peak height 0, and peak threshold 2; negative exponent estimates are invalidated. Offline estimates use a related but nonidentical pipeline. GLMMs include a participant random intercept; the state–ICF model is also checked with a participant-specific state slope. Adaptive allocation of probe types balances acquired samples; it is not an adaptive treatment controller.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

The aperiodic spectral exponent is frequently called an E/I marker, despite depending on multiple physiological and measurement processes. Can humans deliberately modulate this feature, and do the resulting states differ under an independent intracortical physiological assay? That is narrower and more defensible than asking whether one EEG scalar measures synaptic E/I.

### 2. What is the method?

Randomized-order within-participant flatter and steeper feedback conditions are compared with a resting condition. Participants try to enlarge a feedback circle without being told the target direction. Robot-assisted, MRI-free navigation maintains the coil at an individually mapped M1 hotspot. Paired-pulse intervals are individualized from 2/3 ms for SICI and 10/15 ms for ICF. Each feedback condition targets 12 successful probes per stimulation type; six to twelve 15-trial blocks are required. Conditioned MEPs are normalized by the corresponding single-pulse response. Resting physiological measurements use passive, prerecorded feedback, while an independent one-minute eyes-open recording supplies resting EEG estimates.

### 3. What is the method motivation?

M1 allows perturbational interrogation of circuitry through EMG, rather than validating an EEG-derived state solely with another EEG statistic. Separating periodic peaks from broadband background also tests whether apparent theta/beta changes are really oscillatory. Selecting state first and then probing physiology reverses the usual “alter physiology, observe slope” approach—but does not make the exponent an independently randomized mediator.

### 4. What data does it use?

Forty-seven right-handed healthy volunteers aged 19–30 were recruited. Seventeen exceeded the motor-threshold inclusion limit of 84% maximum stimulator output; one of 30 completers was excluded for signal/exponent quality, leaving 29 (8 women, 21 men). Modalities are scalp EEG, first dorsal interosseous EMG/MEPs, stimulation timing, and coil-position quality control. Source reconstruction uses template anatomy and a 100-parcel Schaefer atlas, not individual MRI. Exploratory complete-case models retain 793 single-pulse, 751 SICI, and 767 ICF trials; these are repeated observations from 29 people, not independent participants.

### 5. How is it evaluated?

Repeated-measures ANOVAs and Bonferroni-corrected pairwise tests compare slope and physiology across states. Conventional band-power effects are compared with aperiodic-corrected periodic effects. Source-parcel contrasts use FDR correction; reconstructed aperiodic time–frequency maps use cluster permutation tests. Secondary Gamma GLMMs assess trial-wise spectral associations and a separate state effect. The exploratory feature tests are not multiplicity-corrected; no held-out participant/site evaluation, predictive calibration, clinical endpoint, or prospective treatment-policy comparison is reported.

### 6. What are the main results?

- **State acquisition is reference-dependent.** Both directions differ from their condition-specific baselines. Against independent rest, steepening is significant (corrected p = .010), whereas flattening is not (p = .263). Symmetric departure from an independent baseline is not demonstrated.
- **Physiological state contrast:** Normalized ICF is lower in steeper than flatter feedback (corrected p = .037; reported d = .27) and lower than rest (p = .004; d = .94). Flatter versus rest is nonsignificant (p = .098).
- **Not a generic direction-dependent excitability effect:** Both feedback states increase single-pulse MEPs and increase normalized SICI responses relative to rest; neither measure distinguishes the two feedback directions. A higher conditioned/unconditioned SICI ratio means less measured inhibition, not more.
- **No validated trial-wise E/I decoder:** Exponent does not significantly predict single-pulse MEP, SICI, or ICF in multivariable models; the ICF coefficient is .002, p = .979. The separate categorical state effect remains with a random state slope (p = .017). These are different inferential questions, not contradictory claims.
- **Spectral decomposition matters:** Conventional theta/beta contrasts disappear after aperiodic correction. Periodic-band nulls do not establish equivalence or total physiological independence.
- **Not spatially focal:** The source-space contrast has the same sign in 99/100 parcels; 15 survive FDR, including the C3-associated somatomotor parcel (pFDR = .034, dz = −.61). Template source estimates support cortical expression, not an isolated M1 mechanism.

### 7. What is actually novel?

The useful combination is online aperiodic feedback, threshold-contingent TMS, and an intracortical response assay in humans. It provides a concrete way to investigate state preparation beyond oscillatory phase/power. It does not establish that slope uniquely determines E/I, that neurofeedback specifically caused a synaptic E/I change, or that stimulation selected by this rule is therapeutically superior. Priority over all prior aperiodic feedback work was not independently audited.

### 8. What are the strengths?

An orthogonal physiological readout; within-participant direction contrasts; individualized hotspot/paired-pulse intervals; robotic placement monitoring; decomposition of periodic and aperiodic activity; an independent resting reference; and explicit reporting of the trial-level null. The state–trial dissociation makes this more useful than a paper reporting only successful target acquisition.

### 9. What are the weaknesses, limitations, or red flags?

- **Mechanistic identification:** ICF depends on interacting facilitatory and inhibitory processes, not a pure glutamatergic channel or a quantitative E/I ratio. No direct synaptic or pharmacological identification closes that gap.
- **Feedback specificity:** There is no yoked/sham-feedback control or independent arousal manipulation. Active effort, attention, strategy, and baseline shifts can travel with the target state. Randomizing condition order does not randomize exponent independently of those factors.
- **Selection:** Eighteen of 47 recruits do not contribute analyzed results. Only successful threshold-triggered trials are retained; weak MEPs and poor estimates are also filtered. This limits transport and makes the estimand “selected successful feedback states,” not all attempted states.
- **Target acquisition is not validation:** A large hit-versus-miss exponent difference is partly built into the trigger. The independent MEP assay is the relevant additional evidence.
- **Time and space:** Smoothing produces a seconds-scale state estimate; template source reconstruction and widespread effects limit focal/fast-control interpretations. Online and offline pipelines differ.
- **Prediction and heterogeneity:** Random effects handle repeated measurements but do not demonstrate who benefits, cross-session reliability, patient transport, or held-out response prediction. Modest uncorrected alpha associations remain exploratory.

### 10. What challenges or open problems remain?

Can physiological differences be reproduced across days, devices, sexes, ages, high-threshold participants, and patient populations? Does an exponent target add value beyond engagement or pupil-indexed arousal? Is the ICF contrast predictable before intervention, and does it survive alternative spectral fits, reference windows, and retention of non-hit trials? Can similar exponent values correspond to different intracortical states? The paper's trial-level null makes that last question central.

### 11. What future work naturally follows?

Run randomized true versus yoked feedback with an active attention control; measure pupil/EMG artifacts and prespecify the independent baseline. Interleave scheduled probes so non-hit states remain evaluable. Lock the estimator and test prospective held-out response prediction against periodic features, arousal, and history. Then test whether state preparation changes a separate plasticity or behavioral endpoint. Clinical symptom benefit and mediation would require a further trial, not extrapolation from M1 physiology.

### 12. Why does this matter for cabbageland?

It makes the estimator–intervention interface explicit while demonstrating its identifiability limit. For closed-loop neuromodulation, “we can move the feature,” “the state has a physiological correlate,” and “the feature tells us which action will help” are separate achievements. The same discipline applies to hypnosis/suggestion state biomarkers and CBT–stimulation sequencing, but this experiment tests neither hypnosis nor psychotherapy nor psychiatric treatment.

### 13. What ideas are steal-worthy?

1. Validate a feedback target with a perturbational assay from a different measurement channel.
2. Report effective signal history and age alongside update frequency; a 10-Hz display is not a 100-ms state estimate.
3. Maintain both a trial-local reference and an independent reference to expose apparent bidirectionality created by baseline shifts.
4. Treat state uncertainty and dynamics uncertainty separately, as in the existing PALDI note; test identified models on a different control objective rather than target acquisition alone.
5. Use categorical state effects and continuous response prediction as separate gates. A feature can help define an experimental condition without becoming a transferable decoder.

### 14. Final decision

Keep as **Highly relevant**, directly relevant methods/state-estimation evidence with adjacent translational value. Reuse its independent-probe design and its state-versus-trial distinction. Do not reuse the title as shorthand for demonstrated, selective control of synaptic E/I, nor call it an adaptive therapeutic controller. The next worthwhile result is prospective physiological prediction or improved learning under controlled state preparation—not another large slope contrast.

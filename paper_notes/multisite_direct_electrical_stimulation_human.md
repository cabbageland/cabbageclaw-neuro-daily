# Electrophysiology of multisite direct electrical stimulation in the human brain

## Basic info

* Title: Electrophysiology of multisite direct electrical stimulation in the human brain
* Authors: Devang Sehgal; Angelique C. Paulk; Peter N. Hadar; Jaquelin D. Peralta; Pariya Salami; John D. Rolston; R. Mark Richardson; Sydney S. Cash; Rina Zelmann
* Year: 2026
* Venue / source: bioRxiv preprint, version 1 posted November 13, 2026; not peer reviewed
* Link: https://www.biorxiv.org/content/10.64898/2026.11.11.765993v1
* Date surfaced: 2026-11-15
* Why selected in one sentence: It measures how simultaneous inputs combine in human brain networks and tests the additive baseline before invoking multisite synergy.

## Quick verdict

* Highly relevant

Preserve for network perturbation and input-map design, not clinical efficacy. Most dual-site responses are explained by linear addition; the valuable exceptions have spatial and temporal structure. Lower current at each site is not equivalent to lower total stimulation resources, and wider response spread is not automatically a desirable therapeutic state.

## One-paragraph overview

Twenty adults undergoing epilepsy stereo-EEG monitoring received interleaved single-site and synchronous dual-site electrical pulses, with three-site conditions in a subset. The authors compare the measured simultaneous response with the sum of separately elicited responses, separating additional responsive channels from genuinely nonlinear waveform interactions. Much broader response detection can arise when individually weak signals add past a threshold. Sublinear interactions concentrate near stimulation, whereas supralinear effects preferentially occupy later response components and can occur farther away. Regression and participant-held-out analyses ask whether anatomy and response features improve prediction beyond the simple sum; for magnitude, very little is gained.

## Model definition

### Inputs

For the additive baseline: baseline-normalized, trial-median single-site evoked waveforms A(t) and B(t) from the same recording channel and intensity. For the fitted models: summed-response amplitude, absolute area under the curve (AUC), peak timing, amplitude-weighted single-site peak offset, categorical stimulation/recording anatomy, and whether the recording site is within 15 mm of stimulation. Participant identity supplies a random intercept. Nonresponsive channels are excluded from the mixed-effects analysis.

### Outputs

The fixed baseline emits A(t)+B(t), or the three-site equivalent, and a threshold-based predicted responsiveness label. Separate linear mixed-effects models predict dual-site peak-to-peak amplitude, absolute AUC, and time of the maximum absolute deflection. A cluster-bootstrap procedure labels significant supra/sublinear time points and channel-level interactions; this is a hypothesis test, not a learned controller or clinical-response classifier.

### Training objective (loss)

The additive waveform model has no trained weights or optimization loss. Mixed-effects coefficients estimate continuous dual-site response features from z-normalized predictors with a participant random intercept. The inspected paper does not state the exact likelihood/fitting criterion, including ML versus REML; do not invent it. Model comparison uses AIC and leave-one-participant-out prediction assessed with R²; simple feature regressions also report normalized RMSE. Cluster testing uses a bootstrap null of exact additivity rather than a predictive training loss.

### Architecture / parameterization

Fixed waveform superposition plus feature regressions and random-intercept linear mixed-effects models:

`FeatureAB ~ 1 + AmpA+B + AUCA+B + PkTimingA+B + Pkoffset + StimLoc + RecordingLoc + isLocal + (1 | participant)`

No latent dynamical state, feedback policy, mechanistic E/I circuit model, or optimized stimulation prescription is identified. The model estimates acute input-response composition, not controllability of a therapeutic trajectory.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

When two brain locations are stimulated together, does a network simply add their effects, suppress them, or amplify them? Without that input-composition map, selecting multiple targets independently has no principled account of their joint action.

### 2. What is the method?

Deliver interleaved single-site and simultaneous dual-site pulses; compare the measured joint response with the sum of separate responses. Quantify evoked-potential responsiveness, high-frequency activity (HFA, 70–150 Hz), amplitude/AUC/timing, and interaction residuals. Extend to three sites and compare lower per-site intensity combinations with higher-intensity single-site stimulation.

Pulse phases are 90 µs each with a 53-µs interphase interval; conditions use 2, 4, or 7 mA per site, approximately 20 trials per condition, and 4–5-s interstimulus intervals with jitter. Bipolar recording, pathological-channel exclusion, and −5-to-15-ms artifact blanking/interpolation precede analysis. Main waveform features use 20–750 ms after stimulation.

### 3. What is the method motivation?

Linear superposition is the defensible first null, not a straw man. It distinguishes recruitment by summing subthreshold responses from genuinely nonlinear interactions. Time-resolved residuals can reveal where additional model complexity is needed without pretending that every extra responsive electrode indicates emergent synergy.

### 4. What data does it use?

Twenty adults with drug-resistant epilepsy, ages 21–63, ten female, implanted for clinical monitoring. At 7 mA: 87 stimulation pairs and 2,561 retained bipolar recording channels; 17 participants/66 pairs also received 4 mA, and seven participants/27 pairs received 2 mA. Three-site testing involved seven participants/11 triplets at 4 and 7 mA; fewer contributed at 2 mA.

Clinical implantation constrains coverage, concentrated in frontal/temporal areas. Where possible, screening of 20–60 single sites selects pairs with common responsive recording channels; otherwise broad connectivity/gray-white boundary placement guides selection. This enriches convergence and is not representative sampling of arbitrary target pairs.

### 5. How is it evaluated?

Apply the same evoked-potential detector to measured simultaneous and summed single-site responses. Bootstrap trial-level differences over 20–750 ms with 10,000 resamples and a maximum-cluster-mass correction across time within a channel. A supra/sublinear channel requires more than 75 ms of corresponding significant time points; this is total duration, not necessarily one contiguous segment. Rates generally use qualifying stimulation pairs/triplets as units, requiring at least five channels in the relevant denominator.

Compare waveform features with simple regression and richer mixed-effects models, then use leave-one-participant-out cross-validation. Regional/rate comparisons use permutation tests, including sign flips for paired intensity comparisons. Participant-held-out prediction is stronger than an arbitrary channel split, but pooled channels, repeated pairs, and dependent constituent pairs/triplets still require careful uncertainty interpretation. Fold-specific preprocessing is not fully specified in the inspected text.

### 6. What are the main results?

- At 7 mA, additional TSEP-responsive channels amount to **20.4 ± 1.3%** relative to the single-site-responsive union; the HFA figure is **25.1 ± 2.7%**. Denominators and eligible pair counts differ by criterion; these are not percentages of patients benefiting.
- The summed single-site waveform correctly classifies responsiveness in **86.7%** of recording channels. This is response detection, not symptom prediction; class balance matters.
- **97.8%** of additionally TSEP-responsive channels are classified as linear; for additionally HFA-responsive channels the figure is **90.5%**. Most expanded detection therefore does not require nonlinear amplification.
- Among channels responsive to **both** single sites, mean pair-level rates at 7 mA are **13.3 ± 2.1% supralinear** and **7.5 ± 1.4% sublinear**; categories can overlap over time. Sublinearity concentrates locally; supralinearity peaks around 100–200 ms and can occur remotely.
- At 7 mA, simple feature regression gives amplitude **R² = 0.950**, but peak timing only **R² = 0.249**. In held-out participants, richer models yield amplitude **0.95 versus 0.95**, AUC **0.91 versus 0.91**, and timing **0.29 versus 0.24** relative to the simpler model. Better in-sample AIC does not translate into major predictive gain.
- Two 4-mA sites exceed both single-site 7-mA responses by AUC in **18.8%** of included channel observations, fall below both in **16.0%**, and are intermediate/tied in **65.2%**. This is conditional physiology, not universal superiority or a matched-energy treatment trial.
- Three-site results broadly support composition/recruitment patterns, but the reported increase in sublinearity at 7 mA is a **nonsignificant trend (p = 0.070)**, not a confirmed scaling law. Uncertainties above are reported SEM across qualifying pairs, not independent participants.

### 7. What is actually novel?

A systematic human characterization of synchronous multisite response composition across anatomy, intensity, and response time, with an explicit and surprisingly strong additive baseline. Neither multisite stimulation nor linear superposition is new. The contribution is measuring where their combination works and fails, not inventing precision neurostimulation or proving a therapeutic network mechanism.

### 8. What are the strengths?

Direct perturbation rather than resting correlation; within-recording single/joint conditions; matched baseline normalization; complementary voltage and HFA readouts; temporal interaction tests; explicit lower-intensity comparisons; and participant-held-out prediction. The weak benefit of richer models is reported instead of buried. HFA remains a proxy, not direct cell-resolved firing.

### 9. What are the weaknesses, limitations, or red flags?

- Epilepsy, medication/pathology, clinical sampling, and convergence-enriched pair selection limit population and target generalization. Excluding seizure-onset/IED channels does not make the remaining brain healthy.
- Repeated channels and stimulation pairs are not independent subjects. Participant random intercepts in prediction do not automatically resolve dependence in every descriptive/permutation comparison.
- Artifact blanking and high early-response variance weaken detection of early nonlinearities. Temporal cluster control is not automatically family-wise control over every channel, pair, intensity, and regional hypothesis.
- “Linear” means no qualifying detected departure under this test/trial count, not proof of exact physiological linearity.
- Broader electrophysiological recruitment has no established desirable direction here. Late supralinearity does not directly identify inhibition, rebound, or a cell-type-specific mechanism.
- Lower per-site current does not establish lower total charge, energy, chronic side effects, or clinical burden. Resource balancing depends on waveform, impedance, and number of stimulated sites.
- Single pulses are not therapeutic trains; the small three-site sample cannot settle scalability. Code/data release is promised with publication, not verified here.

### 10. What challenges or open problems remain?

Predict timing and interaction residuals in unseen people; separate genuine physiology from threshold/artifact sensitivity; identify when wider recruitment is useful rather than off-target; and extend composition maps to trains, changing brain states, chronic stimulation, and meaningful behavior. These measurements do not yet identify a state-space model or establish safe closed-loop control.

### 11. What future work naturally follows?

Preregister held-out-participant/session tests with hierarchical uncertainty. Compare single and multisite protocols under explicit total-charge and energy constraints as well as peak-current limits, with randomized waveform/intensity ordering where feasible. Test asynchronous offsets, train history, and disease-relevant behavioral endpoints. Add connectivity or state features only if they improve out-of-sample prediction beyond the additive baseline. Resolve proposed inhibitory mechanisms with independent measurements rather than assigning them from latency alone.

### 12. Why does this matter for cabbageland?

It supplies an empirical input-composition check upstream of adaptive intervention. Network-guided stimulation earns the network-engagement label here through measured perturbation responses; it does not earn therapeutic targeting or closed-loop labels. The existing [depression-DBS composition note](https://cabbageland.github.io/cabbageclaw-neuro-daily-web/#/paper_notes/combinatorial_multisite_stimulation_trd.md) asks a related question using trains and band power, while [feasible latent control](https://cabbageland.github.io/cabbageclaw-neuro-daily-web/#/paper_notes/feasible_closed_loop_latent_dynamics_control.md) makes the remaining sensing/actuation problem explicit. Do not equate their endpoints or pool their cohorts.

### 13. What ideas are steal-worthy?

- Build a single-input library and make its sum the first multisite predictor.
- Keep three outputs separate: thresholded recruitment, time-resolved interaction residual, and desired functional/clinical change.
- Plot spatial and temporal failure maps of additivity rather than one global “synergy” score.
- Demand subject-held-out gain before adding anatomy/model complexity.
- Optimize under separate peak-current, total-dose, sensing, latency, and safety budgets; never silently substitute one budget for another.

### 14. Final decision

**Preserve as highly relevant human network-perturbation evidence.** Inspection used the primary version-1 full-text PDF: main results, relevant captions, discussion, cohort/protocol, preprocessing, response/nonlinearity definitions, and predictive/statistical methods. Supplementary files, raw data, and code were not independently audited or reproduced. The exact mixed-model estimation criterion is not stated in the inspected text. Useful for additive baselines and experiment design; not evidence of clinical multisite superiority, a proven inhibitory mechanism, or a deployed controller.

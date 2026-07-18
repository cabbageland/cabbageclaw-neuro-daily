# Device-embedded accelerometry complements neural signals for tracking parkinsonian motor states

## Basic info

* Title: Device-embedded accelerometry complements neural signals for tracking parkinsonian motor states
* Authors: Tao Liu, Jiaang Yao, Bahman Abdi-Sargezeh, Abhinav Sharma, Camille Lasbareilles, Robert Tsi Lok Ho, Jackson T.S. Cheung, Timothy Denison, Huiling Tan, Wolf-Julian Neumann, Minghan Max Zhu, Sebastian Liu, Philip A. Starr, Simon Little, Ashwini Oswal
* Year: 2026
* Venue / source: bioRxiv preprint
* Link: https://www.biorxiv.org/content/10.64898/2026.07.08.737286v1
* Date surfaced: 2026-07-18
* Why selected in one sentence: It tests a more honest adaptive-DBS question than most decoder papers ask by checking which biomarkers still track Parkinsonian motor state once continuous stimulation is already altering the circuit.

## Quick verdict

* Highly relevant

This is a strong keep because it treats biomarker robustness under active therapy as part of the actual control problem instead of a footnote. The paper shows that implanted accelerometry can outperform several canonical neural features during chronic stimulation, while also clarifying why total beta is often too blunt a control signal. The main caveat is scale and target definition: the cohort is small, the labels come from wearable PKG scores rather than clinician ratings in real time, and the best-performing behavioral readout partly shares the same kinematic domain as the target it predicts.

## One-paragraph overview

The paper analyzes chronic home recordings from Parkinson's patients implanted with sensing-enabled subthalamic and cortical leads plus a chest-implanted device accelerometer. The authors pair more than 1,900 hours of neural and accelerometry data with two-minute PKG-derived bradykinesia and dyskinesia estimates, then compare neural-only, accelerometry-only, and combined regressors before and during continuous STN stimulation. The useful result is that periodic and aperiodic neural components behave differently, and several popular neural biomarkers degrade once stimulation is active. Implanted accelerometry stays comparatively stable and often decodes motor state better than neural features alone. The paper does not prove that accelerometry should replace neural sensing, but it makes a compelling case that behavioral and neural control signals should be combined hierarchically rather than judged in isolation.

## Model definition

The paper contains several trainable symptom-decoding models rather than one single canonical model.

### Inputs
For each two-minute window, the models take neural features from subthalamic and sensorimotor cortical field potentials, device-embedded accelerometry features from the implanted pulse generator, or both. Neural inputs include total and periodic band power in low beta, high beta, low gamma, and high gamma ranges, aperiodic offset and exponent from FOOOF decomposition, and cortico-subthalamic coherence. Accelerometry inputs include the Euclidean norm of triaxial acceleration plus 29 movement-related features such as entropy, jerk, and time-below-threshold summaries.

### Outputs
The models predict continuous PKG-derived bradykinesia or dyskinesia severity scores for the corresponding two-minute interval. The paper also outputs feature-importance estimates, cross-validated coefficient-of-determination scores, and correlation statistics linking features to symptom severity.

### Training objective (loss)
The main text states that four regression models were trained to predict PKG symptom scores and were evaluated by mean cross-validated R². The exact optimization details differ by model family and are delegated to Supplementary Table 3. From the accessible main text, the paper does not give one shared explicit loss beyond regression to symptom scores, so the precise training objective is model-specific rather than uniformly specified.

### Architecture / parameterization
This is a multimodel regression benchmark rather than one architecture. The model families are Random Forest, Support Vector Machine, ElasticNet, and a Fully Connected Neural Network. Random Forest achieved the best performance and is treated as the main decoder for pairwise feature-set comparisons and importance analyses.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Adaptive DBS needs biomarkers that stay informative while stimulation is already running. Many papers implicitly assume that a neural marker discovered off stimulation will remain equally useful on stimulation. This paper asks whether that assumption is actually true and whether the implanted device accelerometer offers a more robust behavioral signal for tracking Parkinsonian motor state.

### 2. What is the method?
The authors record chronic home data from sensing-enabled Parkinson's implants, combining cortical and subthalamic field potentials with the pulse generator's triaxial accelerometer and contralateral wrist-worn PKG estimates of bradykinesia and dyskinesia. They extract periodic, aperiodic, and coherence-based neural features plus a library of accelerometry features, correlate those features with symptom severity, and train four regression models per hemisphere to decode PKG scores before and during continuous stimulation.

### 3. What is the method motivation?
The main motivation is that the control variable for closed-loop DBS should be judged in the state where it will actually be used. If stimulation itself suppresses or distorts the biomarker, the controller may be chasing a moving target. Implanted accelerometry is attractive because it is always present, requires no external wearable, and may remain behaviorally meaningful even when neural oscillations are being actively perturbed.

### 4. What data does it use?
The study includes 11 patients with idiopathic Parkinson's disease implanted bilaterally with Medtronic Summit RC+S systems, each with STN leads and cortical paddle leads. All 11 contributed chronic neural recordings, while 8 of the 11 also contributed concurrent device-embedded accelerometry. The paper analyzes 986 hours without stimulation and 915 hours with continuous STN stimulation, segmented into two-minute windows aligned to bilateral PKG symptom scores. After exclusions for sleep-like immobility and zero or invalid symptom-score windows, the authors retained 29,568 off-stimulation windows and 27,457 on-stimulation windows for bradykinesia analyses, plus 25,094 off-stimulation and 21,167 on-stimulation windows for dyskinesia analyses.

### 5. How is it evaluated?
Evaluation has two layers. First, the paper computes subject-level correlations between extracted features and PKG scores, with multiple-comparison correction across feature families. Second, it trains four regressors under stratified five-fold cross-validation repeated twice and evaluates mean R² per hemisphere. The authors then compare neural-only, accelerometry-only, and combined feature sets, inspect out-of-bag permutation importance in the Random Forest models, and repeat the whole logic under active stimulation to test robustness.

### 6. What are the main results?
Off stimulation, periodic STN beta power is a stronger bradykinesia marker than total beta, while aperiodic features and gamma-related measures carry complementary information. Implanted accelerometry robustly tracks both bradykinesia and dyskinesia, with inverted entropy of acceleration magnitude working best for bradykinesia and jerk working best for dyskinesia. In decoding benchmarks, Random Forest performs best overall. Accelerometry significantly outperforms STN-only and cortex-only neural feature sets, and combined models do best overall. A practical hybrid using STN plus accelerometry nearly matches the full combined model, with R² around 0.28 versus 0.29. Under continuous stimulation, neural-symptom relationships weaken substantially, especially for periodic STN beta, whereas accelerometry degrades much less and continues to outperform neural-only models. Combined-model bradykinesia prediction drops modestly from R² 0.292 off stimulation to 0.247 on stimulation, while dyskinesia prediction remains more stable.

### 7. What is actually novel?
The novelty is not just "we added another sensor." The real novelty is testing biomarker robustness under chronic active stimulation in naturalistic home recordings and showing that the implanted pulse generator's accelerometer can remain behaviorally useful when canonical neural markers lose traction. The paper also sharpens the distinction between total beta power and its periodic versus aperiodic components in a control-relevant context.

### 8. What are the strengths?
The paper uses chronic home data rather than short laboratory tasks, and it explicitly compares off-stimulation and on-stimulation regimes instead of hiding the latter. It combines translational practicality with mechanistic spectral decomposition, rather than choosing one and ignoring the other. The feature extraction is causal and real-time compatible. The model comparison is sensible rather than theatrical, and the conclusion is operational: a robust behavioral signal can coexist with more mechanistic but less stable neural features.

### 9. What are the weaknesses, limitations, or red flags?
The patient count is small, even if the number of windows is large. Only 8 of 11 patients contributed concurrent implanted accelerometry, so the strongest behavioral claim rests on a narrower cohort than the neural claim. The prediction target is PKG-derived symptom severity, which is itself a wearable kinematic proxy rather than a gold-standard latent disease-state label. That means accelerometry may partly win because it lives in the same measurement family as the target. The paper is also a preprint, not a settled clinical trial result, and it does not yet demonstrate that an accelerometry-informed controller improves patient outcomes prospectively.

### 10. What challenges or open problems remain?
The field still needs to show whether behavioral and neural signals can be fused prospectively in a controller that improves efficacy, side effects, or energy use relative to simpler adaptive schemes. It also needs to determine when behavioral readouts are enough and when neural specificity genuinely adds value. Another open problem is whether similar robustness patterns hold for symptoms that are less kinematically obvious than bradykinesia and dyskinesia, including freezing, gait instability, mood state, or cognitive burden.

### 11. What future work naturally follows?
The obvious next step is a prospective stimulation-state–aware controller that explicitly weights implanted accelerometry and neural features differently depending on whether stimulation is off, ramping, or fully on. Another natural extension is to test whether the same hierarchy works for gait, freezing, or nonmotor Parkinson states that are poorly captured by wrist-worn proxies. A third step is to move from symptom decoding to actual closed-loop policy evaluation, asking whether the more robust feature stack leads to better control decisions than conventional beta-threshold systems.

### 12. Why does this matter for cabbageland?
Because cabbageland cares about causal and control-relevant biomarkers, not just attractive correlations. This paper gives a clean reminder that a good adaptive signal is not the one that looks prettiest in the quiet state. It is the one that still carries actionable information once the intervention is pushing on the system. That principle transfers well beyond Parkinson's disease to any closed-loop neuromodulation setting where the therapy changes the measurement regime.

### 13. What ideas are steal-worthy?
One steal-worthy move is to redefine biomarker quality in terms of robustness under active intervention rather than off-line correlation strength. Another is to decompose canonical oscillatory markers into periodic and aperiodic components before giving them controller status. A third is the hierarchical hybrid-control framing: use a stable implanted behavioral measure as the coarse state-estimation backbone, then let neural features add mechanistic precision where they remain trustworthy. The paper also quietly models good translational taste by preferring causal, real-time compatible feature extraction over offline benchmark ornament.

### 14. Final decision
Keep as a highly relevant adaptive-neuromodulation note. It does not close the loop clinically by itself, but it sharpens how future adaptive DBS systems should choose, combine, and distrust their own biomarkers.

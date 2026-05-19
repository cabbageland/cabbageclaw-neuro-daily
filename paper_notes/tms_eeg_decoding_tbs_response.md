# Exploratory decoding of TMS-EEG: Predicting TEP response to intermittent and continuous theta burst stimulation

## Basic info

* Title: Exploratory decoding of TMS-EEG: Predicting TEP response to intermittent and continuous theta burst stimulation
* Authors: Sofie Carrette, Arnaud Falisse, Marie E. Vandriessche, and Vincent Vandenbulcke
* Year: 2026
* Venue / source: NeuroImage
* Link: https://doi.org/10.1016/j.neuroimage.2026.121957
* Date surfaced: 2026-05-18
* Why selected in one sentence: It directly tests whether baseline EEG can predict protocol-specific cortical response to theta-burst stimulation, which is one of the real bottlenecks for personalized noninvasive neuromodulation.

## Quick verdict

* Highly relevant

The paper asks the right question, and that matters more than the fact that it is still small. If baseline resting EEG contains predictive signal for post-TBS TEP changes, then response variability becomes a modeling problem rather than an excuse. The main constraint is that this note is based on abstract-level inspection plus limited Elsevier metadata access, so the implementation details and robustness checks are not fully verified.

## One-paragraph overview

The study uses pre-stimulation resting-state EEG to predict changes in six TMS-evoked-potential components after intermittent or continuous theta-burst stimulation over left primary motor cortex. In 15 healthy male participants in a randomized single-blind crossover design, the authors compare a linear Lasso regressor and a nonlinear CatBoost regressor against a random baseline. Both learned models beat random guessing, but which model worked best depended on the specific TEP component and stimulation protocol. The transferable idea is that stimulation response may be partially forecastable from baseline neurophysiology, but the study is still exploratory and far from proving stable clinical personalization.

## Model definition

### Inputs
Pre-stimulation resting-state EEG features, including spectral-power and connectivity-derived measures, with analyses centered on predicting responses to intermittent and continuous theta-burst stimulation delivered to left primary motor cortex.

### Outputs
Predicted post-stimulation change in six TMS-evoked-potential component amplitudes: N15, P30, N45, P60, N100, and P180.

### Training objective (loss)
The exact loss is not stated in the accessible text. The abstract reports prediction performance using mean absolute error relative to a random-guessing baseline.

### Architecture / parameterization
Two regression model families were tested: Lasso regression as the linear sparse model and CatBoost regression as the nonlinear gradient-boosted model.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Theta-burst stimulation effects are highly variable across people and sessions, which makes personalized TBS hard to justify. The paper asks whether baseline EEG can predict who will show which cortical-response changes.

### 2. What is the method?
Record resting EEG before stimulation, apply iTBS or cTBS over motor cortex, measure post-stimulation TEP changes, and train regression models to map baseline EEG features to those TEP shifts.

### 3. What is the method motivation?
If stimulation outcome depends on current physiological state, then state-sensitive models could eventually inform protocol selection, timing, or adaptation.

### 4. What data does it use?
Fifteen healthy male participants in a randomized single-blind crossover study, with resting EEG and TMS-EEG readouts around iTBS and cTBS.

### 5. How is it evaluated?
The learned models are compared with a random-guessing baseline, using mean absolute error across six TEP components and across the two TBS protocols.

### 6. What are the main results?
Both Lasso and CatBoost outperform random guessing. Best model choice varies by protocol and component. Adding feature deltas apparently does not help much. Spectral-power and connectivity features appear especially predictive.

### 7. What is actually novel?
Not TMS-EEG by itself. The useful novelty is the explicit attempt to predict protocol-specific TEP response from baseline resting EEG rather than merely associating post hoc changes with stimulation.

### 8. What are the strengths?
It frames stimulation variability as something potentially decodable, uses both linear and nonlinear models instead of one arbitrary method, and focuses on physiologically closer outcomes than distant clinical scores.

### 9. What are the weaknesses, limitations, or red flags?
The sample is tiny, male-only, healthy-participant-only, and motor-cortex-specific. This is still a biomarker-exploration study, not a clinically validated personalization pipeline. Full text was not accessible here, so preprocessing, cross-validation discipline, leakage safeguards, and exact feature construction could not be directly checked.

### 10. What challenges or open problems remain?
Generalization across cohorts, sessions, cortical targets, and clinical populations is unresolved. It is also unclear whether predictive signal for TEP shifts will translate into clinically useful prediction of symptom outcomes.

### 11. What future work naturally follows?
Larger mixed-sex cohorts, preregistered validation, prospective protocol assignment based on baseline EEG, and linking predicted TEP response to downstream behavioral or clinical gains.

### 12. Why does this matter for cabbageland?
Because it supports a more serious intervention logic: stimulation response may depend on measurable brain state, and that state may be partially modelable before the pulse train starts.

### 13. What ideas are steal-worthy?
Use baseline state features as priors for protocol assignment. Keep component-specific rather than single-score prediction targets. Compare sparse linear versus nonlinear models instead of assuming complexity wins.

### 14. Final decision
Keep. This is not decisive evidence, but it is the kind of compact modeling paper that sharpens personalized neuromodulation thinking.

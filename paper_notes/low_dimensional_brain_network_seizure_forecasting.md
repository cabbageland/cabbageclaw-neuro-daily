# Low-dimensional representation of brain networks for seizure risk forecasting

## Basic info

* Title: Low-dimensional representation of brain networks for seizure risk forecasting
* Authors: Steven Rico-Aparicio, Martin Guillemaud, Alice Longhena, Vincent Navarro, Louis Cousyn, Mario Chavez
* Year: 2026
* Venue / source: arXiv preprint
* Link: https://arxiv.org/abs/2505.00856
* Date surfaced: 2026-06-20
* Why selected in one sentence: It turns daily seizure-risk estimation from brief resting-state intracranial EEG into an interpretable state-estimation problem instead of another continuous-monitoring black box.

## Quick verdict

* Highly relevant

This is a good preserve because it asks a clinically real question with a cleaner evaluation setup than most seizure-forecasting papers. The useful part is not that Euclidean geometry wins benchmarks. It mostly does not. The useful part is that short daily resting-state recordings, node-level geometric shifts, and a pseudo-prospective forecast can already produce a usable patient-specific risk signal. The main caution is that the cohort is tiny, the best results rely on patient-specific band selection, and stronger baselines still match or beat it.

## One-paragraph overview

The paper builds daily seizure-risk forecasts from short resting-state intracranial EEG recordings in drug-resistant focal epilepsy. For each patient, the authors compute phase-locking-value connectivity graphs from seizure-onset-zone electrodes, embed each graph into a two-dimensional Euclidean space with diffusion maps, align embeddings across days with Procrustes analysis, and then model each electrode's interictal and preictal spatial distribution as a Gaussian. A likelihood-ratio biomarker, called ℬ, compares whether a node in a new recording looks more like the learned interictal or preictal distribution. Node scores are aggregated into segment-level and then day-level classifications. The interesting claim is that a compact geometric representation can localize informative electrodes and produce competitive pseudo-prospective day-ahead seizure forecasts from ten-minute daily sessions rather than continuous long-horizon monitoring.

## Model definition

### Inputs
Daily 10-minute resting-state intracranial EEG recordings from seizure-onset-zone electrodes in drug-resistant focal epilepsy, split into 30 non-overlapping 20-second epochs per day. The pipeline uses phase-locking-value connectivity matrices in delta, theta, alpha, beta, low gamma, and high gamma bands, plus prior interictal and preictal labels from earlier days.

### Outputs
Two-dimensional embeddings of connectivity graphs, node-level Bhattacharyya distances and significance scores, a node-level biomarker ℬ comparing interictal versus preictal likelihoods, segment-level class labels, and day-level preictal probabilities and forecasts.

### Training objective (loss)
There is no end-to-end learned predictor with a standard loss. The method fits node-wise Gaussian reference distributions for interictal and preictal embeddings, uses permutation-tested Bhattacharyya distance to choose informative nodes, and then classifies new points with a likelihood-ratio rule.

### Architecture / parameterization
Diffusion-map embedding to two dimensions, Procrustes alignment across days, node-wise Gaussian modeling of embedded coordinates, permutation-based node selection, and patient-specific frequency-band selection based on classification performance.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to forecast seizure risk from short daily intracranial EEG recordings rather than from continuous monitoring, while keeping the state representation interpretable enough to localize which electrodes actually carry the preictal signal.

### 2. What is the method?
The authors build phase-locking-value connectivity graphs from daily seizure-onset-zone intracranial EEG, embed those graphs into a two-dimensional Euclidean space with diffusion maps, align them across days, estimate interictal and preictal node distributions, and classify new segments with a likelihood-ratio biomarker. Day-level forecasts are then formed by averaging segment predictions.

### 3. What is the method motivation?
If preictal states are real network states rather than only local waveform anomalies, then their geometry should appear in compact connectivity embeddings. A low-dimensional representation also makes it easier to compare days, identify informative electrodes, and avoid the interpretability collapse of heavier black-box predictors.

### 4. What data does it use?
The dataset contains daily 10-minute resting-state intracranial EEG recordings from 10 patients with drug-resistant focal epilepsy collected between 2019 and 2021 at Pitie-Salpetriere. The paper labels 69 days as interictal and 38 as preictal, where preictal means a seizure occurs within the next 24 hours. Only seizure-onset-zone electrodes are retained for analysis, and the number of electrodes varies by patient.

### 5. How is it evaluated?
The paper uses leave-one-out day-level classification and a pseudo-prospective forecasting setup where each day is predicted only from preceding days once both classes are present in the training set. Performance is summarized with F1-score, balanced accuracy, accuracy, Brier score, and group-level permutation tests. The approach is also compared against a hyperbolic-embedding model and an SVM baseline on the same cohort.

### 6. What are the main results?
- Averaged across all bands and patients, the classifier is near chance, with F1 around 0.45 and balanced accuracy around 0.54.
- When the best-performing band is selected per patient, performance improves to F1 0.64 ± 0.32 and balanced accuracy around 0.78, with a group-level permutation result reported as p = 0.001.
- In pseudo-prospective forecasting, the best band per patient reaches mean accuracy 0.86 ± 0.18 with Brier score 0.13 ± 0.11, with group-level permutation results reported around p = 0.026 for accuracy and p = 0.029 for Brier score.
- Across 28 preictal days, 22 are correctly flagged, for sensitivity 78.57 percent. Across 23 interictal days, 17 are correctly classified, for specificity 73.91 percent.
- The Euclidean method is competitive with prior hyperbolic and SVM approaches on the same data, but does not clearly outperform them.

### 7. What is actually novel?
The novelty is not raw accuracy. It is the combination of daily short-session forecasting, node-level geometric biomarker construction, and pseudo-prospective evaluation inside an interpretable Euclidean embedding. That is more useful than another paper that posts a better classifier score without clarifying what state changed where.

### 8. What are the strengths?
- The pseudo-prospective setup is much closer to a real forecasting workflow than a generic shuffled split.
- The method stays interpretable at the electrode level.
- It avoids pretending one universal frequency band works for everyone.
- It demonstrates that short, vigilance-controlled daily recordings can still carry useful preictal information.
- It compares itself to stronger prior baselines on the same cohort instead of inventing an easier benchmark.

### 9. What are the weaknesses, limitations, or red flags?
- The cohort is very small.
- The best results depend on patient-specific band selection, which helps clinically but weakens any claim to universal biomarker structure.
- The Euclidean method is competitive rather than clearly superior to hyperbolic or SVM baselines.
- Only seizure-onset-zone electrodes are used, so it is not obvious how the method generalizes to broader or noninvasive recordings.
- The preictal label is a coarse within-24-hours definition, which may mix multiple pathophysiological sub-states.
- This is a preprint, not a peer-reviewed clinical validation.

### 10. What challenges or open problems remain?
The main open problems are prospective deployment in a larger cohort, calibration drift over longer horizons, and deciding what to do with the false positives. Those may be mere errors, or they may reflect genuinely elevated but unrealized seizure susceptibility. Another big question is whether the same representation can guide stimulation timing rather than only forecast risk.

### 11. What future work naturally follows?
Run a true prospective validation study, test whether false positives correspond to clinically meaningful high-risk states, combine the geometric biomarker with stimulation-response data, and compare Euclidean embeddings with stronger learned state-space models under the same real-time constraints.

### 12. Why does this matter for cabbageland?
Because it sharpens a key closed-loop lesson: useful neuromodulation systems need a state-estimation layer, not just an actuator. This paper makes that layer legible. It suggests that daily compact network snapshots can be enough to support individualized control logic if the representation is good and the evaluation is honest.

### 13. What ideas are steal-worthy?
- Use short, standardized daily recordings instead of assuming continuous monitoring is always necessary.
- Treat preictal structure as a geometric change in network state, not just a local signal-feature anomaly.
- Keep electrode-level interpretability instead of collapsing everything into a single opaque decoder.
- Benchmark interpretable geometric models directly against stronger black-box baselines under identical data constraints.

### 14. Final decision
Preserve. Not because it wins the forecasting leaderboard, but because it offers a clean, interpretable scaffold for daily seizure-risk estimation and makes the next closed-loop question obvious: can this state estimate actually improve intervention timing?

# Phase estimation with autoregressive padding (PEAP): addressing inaccuracies and biases in EEG analysis

## Basic info

* Title: Phase estimation with autoregressive padding (PEAP): addressing inaccuracies and biases in EEG analysis
* Authors: Miriam Kirchhoff, Johanna Roesch, Maria Ermolova, Oskari Ahola, Sarah Harders, Juliana Hougland, Ulf Ziemann
* Year: 2026
* Venue / source: arXiv preprint, q-bio.NC
* Link: https://arxiv.org/abs/2604.02212
* Date surfaced: 2026-06-14
* Why selected in one sentence: It attacks a quiet but central failure mode in phase-dependent EEG-TMS by showing that common instantaneous-phase estimators can be systematically biased, then proposing a cleaner alternative that improves accuracy without the same phase-bin distortions.

## Quick verdict

* Highly relevant

This is exactly the kind of methods paper worth preserving because a lot of phase-dependent stimulation rhetoric quietly assumes the phase estimator is already trustworthy. The useful contribution is not just slightly higher average accuracy. It is the argument that established methods can overproduce some phases, shift others in time, and therefore distort both reported optimal phases and cross-study comparability. The main caution is that the validation is still offline, the stroke cohort is small, and the ground truth itself depends on an acausally filtered continuous signal rather than some direct physiological oracle.

## One-paragraph overview

The paper studies a practical problem in EEG-TMS and related closed-loop stimulation work: how to estimate the instantaneous phase at the very edge of an EEG segment without letting filtering artifacts quietly bias the answer. Existing approaches such as Phastimate, ETP, SSPE, and PhastPadding either trim away edge-contaminated samples and extrapolate forward or avoid filtering in other ways, but the authors show that these choices can still introduce systematic phase biases. PEAP takes a different route. It pads the unfiltered signal with autoregressively forecast data before bandpass filtering, which pushes the filtering edge artifact away from the time point of interest rather than trying to repair the damage after the fact. Across resting-state EEG from young healthy adults, older healthy adults, and chronic stroke participants, PEAP achieves the best instantaneous-phase accuracy, improves continuous phase estimation by about 3.2 to 9.2 percent over established methods, and largely avoids the strong phase-bin biases seen in competing pipelines.

## Model definition

### Inputs
Resting-state EEG data, target frequency band around the mu rhythm, trial windows ending at the stimulation-relevant sample, and method-specific hyperparameters for forecasting or phase inference.

### Outputs
Estimated instantaneous phase at the target sample, future phase forecasts for short horizons, and method-level accuracy and bias summaries relative to a continuous-signal reference phase.

### Training objective (loss)
PEAP is not a learned model in the deep-learning sense, but its autoregressive padding hyperparameters are selected on training data by minimizing circular root mean squared error while rejecting settings that fail a Kuiper-test distribution check against the reference phase distribution.

### Architecture / parameterization
PEAP fits an autoregressive model to the unfiltered EEG segment, appends simulated oscillatory samples beyond the segment boundary, then applies bandpass filtering and a Hilbert transform so that the filtering edge artifact falls in the padded region instead of the sample being analyzed. The paper compares this against Phastimate, ETP, SSPE, and PhastPadding.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to solve the edge-artifact problem in instantaneous EEG phase estimation. In phase-dependent stimulation work, the scientifically important sample is often the last one before a pulse. Standard filtering and Hilbert-transform workflows distort that sample, and many repair strategies introduce their own biases.

### 2. What is the method?
The method is PEAP, or Phase Estimation with Autoregressive Padding. Instead of filtering first and then cutting or extrapolating the damaged edge, it pads the raw signal with autoregressively predicted oscillatory data, filters the extended signal, and extracts phase afterward. This shifts the strongest filtering artifact away from the target sample.

### 3. What is the method motivation?
If the estimator systematically favors some phases or phase slopes, then downstream claims about optimal stimulation timing can be wrong even when the rest of the experiment is clean. The motivation is therefore intervention honesty: prevent the filtering artifact rather than compensating for it after the signal has already been distorted.

### 4. What data does it use?
The evaluation uses resting-state EEG from seventy-two participants split across fifty-four young healthy controls, ten older healthy controls, and eight chronic stroke participants. Data were recorded with a 128-channel EEG system during five to ten minutes of open-eyes rest, then processed into training and test sets with virtual TMS markers for offline phase-estimation benchmarking.

### 5. How is it evaluated?
The paper computes a reference phase from the continuous signal, then compares PEAP against Phastimate, ETP, SSPE, and PhastPadding using instantaneous-phase accuracy, forecasting accuracy across time, phase-bin bias analyses, and linear mixed-effects modeling across methods, datasets, and phase bins. It also uses circular Kuiper tests to ask whether estimated phase distributions deviate systematically from the reference distribution.

### 6. What are the main results?
- PEAP achieves the highest median instantaneous-phase accuracy at the target sample, ahead of the other tested methods.
- The reported gain over established methods is about 3.2 to 9.2 percent for continuous phase estimation.
- The method-by-dataset interaction is not significant, suggesting that the relative method differences do not meaningfully change between healthy and stroke datasets.
- Established methods show phase-bin biases and time shifts, whereas PEAP largely avoids those distortions.
- Forecast accuracy for all methods decays into the future, but PEAP remains the strongest performer over the evaluated window.

### 7. What is actually novel?
The novelty is not merely using autoregression. The useful novelty is padding the unfiltered signal before bandpass filtering so that the edge artifact is displaced rather than patched, then explicitly treating estimator bias as a first-class evaluation target instead of only reporting average error.

### 8. What are the strengths?
- It attacks a real hidden confound in phase-dependent neuromodulation rather than another cosmetic benchmark problem.
- It compares against several established alternatives instead of a single weak baseline.
- It measures systematic bias, not just average accuracy.
- It includes both healthy and stroke data, which makes the result more relevant to translational stimulation work.
- It is directly actionable for offline analysis and plausibly relevant for real-time adaptation.

### 9. What are the weaknesses, limitations, or red flags?
- The validation is offline, not a full online closed-loop deployment.
- The reference phase is still derived from an acausally filtered continuous signal, so the benchmark is careful but not metaphysically ground truth.
- The stroke cohort is small.
- The paper does not benchmark runtime in a way that would settle real-time deployability.
- Results are shown within a relatively simple preprocessing stack, so integration with more complex pipelines remains to be tested.

### 10. What challenges or open problems remain?
The main open problems are whether the same advantage survives in noisier clinical recordings, whether PEAP remains computationally practical in strict real-time settings, and how it behaves when embedded earlier in richer preprocessing chains such as ICA-heavy or artifact-heavy pipelines.

### 11. What future work naturally follows?
Online validation in real phase-dependent stimulation experiments is the obvious next step. After that, it would make sense to package PEAP into a broader comparison toolbox, test it under harsher artifact conditions, and examine whether improved phase honesty changes reported optimal phases in existing EEG-TMS paradigms.

### 12. Why does this matter for cabbageland?
Because a lot of closed-loop stimulation logic lives or dies on whether the state variable is real. If the phase estimate itself is biased, then the whole story about trough versus peak stimulation, state dependence, or personalized timing can turn into beautifully quantified folklore.

### 13. What ideas are steal-worthy?
- Treat phase-estimator bias as a scientific confound, not just a signal-processing nuisance.
- Pad unfiltered data before filtering when the scientifically important sample sits at the edge.
- Use both error metrics and distributional tests when comparing phase estimators.
- Evaluate forecasting accuracy over time instead of only a single endpoint sample.

### 14. Final decision
Preserve. This is a strong methods note for phase-dependent neuromodulation because it improves the calibration layer underneath a lot of closed-loop claims and does so in a way that is concrete, testable, and immediately useful.
